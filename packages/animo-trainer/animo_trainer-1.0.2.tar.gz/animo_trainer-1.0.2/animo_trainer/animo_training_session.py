import pathlib, os, shutil, time, yaml, threading
import numpy as np
from typing import Dict, List, Optional, Tuple

from mlagents.trainers.cli_utils import parser as ml_agents_parser
from mlagents.trainers.settings import RunOptions, TrainerSettings

from TransformsAI.Animo.Data import AgentData, LevelData, CheckpointData
from TransformsAI.Animo.Tools import AgentCheckpointAccumulator
from TransformsAI.Animo.Serialization import AnimoSerializer
from TransformsAI.Animo.Rewards import RewardEvaluator

INPUT_FOLDER_NAME = "Input"
OUTPUT_FOLDER_NAME = "Output"
AGENTS_FOLDER_NAME = "Agents"
CONFIG_FILE_NAME = "config.yaml"
LEVEL_FILE_NAME = "level.json"
AGENT_DATA_FILE_NAME = "AgentData.json"
AGENT_CHECKPOINT_FILE_NAME = "checkpoint.pt"

BehaviorName = str


class AnimoTrainingSessionConfig:
    def __init__(self, folder_path: str, daemon_pid: Optional[int] = None) -> None:
        self.id: str
        self.agent_output_paths: Dict[BehaviorName, str] = {}

        self._run_options: RunOptions
        self._lock = threading.Lock()
        self._checkpoint_accumulators: Dict[BehaviorName, AgentCheckpointAccumulator] = {}
        self._agent_datas: Dict[BehaviorName, AgentData] = {}
        self._level_data: LevelData

        if daemon_pid is not None:
            self.should_check_daemon = True
            self.daemon_pid: int = daemon_pid
        else:
            self.should_check_daemon = False

        # Input folders
        training_session_full_folder_path = pathlib.Path(folder_path)
        if not os.path.isdir(training_session_full_folder_path):
            raise ValueError("Training session folder not found")

        input_folder_full_path = os.path.join(training_session_full_folder_path, INPUT_FOLDER_NAME)
        if not os.path.isdir(input_folder_full_path):
            raise ValueError("Input folder not found")

        input_agents_full_path = os.path.join(input_folder_full_path, AGENTS_FOLDER_NAME)
        if not os.path.isdir(input_agents_full_path):
            raise ValueError("Input agents folder not found")

        # Config
        input_config_full_path = os.path.join(input_folder_full_path, CONFIG_FILE_NAME)
        if not os.path.isfile(input_config_full_path):
            raise ValueError("Config.yaml not found")

        args = ml_agents_parser.parse_args([input_config_full_path])
        self.run_options = RunOptions.from_argparse(args)

        if self.run_options.env_settings.seed == -1:
            self.run_options.env_settings.seed = np.random.randint(0, 10000)  # type:ignore

        self.id = training_session_full_folder_path.name
        self.run_options.checkpoint_settings.run_id = self.id
        self.run_options.checkpoint_settings.results_dir = str(
            os.path.join(training_session_full_folder_path, OUTPUT_FOLDER_NAME, AGENTS_FOLDER_NAME))

        # Level
        input_level_full_path = os.path.join(input_folder_full_path, LEVEL_FILE_NAME)
        if not os.path.isfile(input_level_full_path):
            raise ValueError("Level.json not found")

        json_level = None
        with open(input_level_full_path, mode='r') as file:
            json_level = file.read()
        level_data: LevelData = AnimoSerializer.FromJson[LevelData](json_level)
        self.level_data = level_data

        # Agents
        characters = level_data.SavedGrid.Characters

        if characters.Count < 1:
            raise ValueError("Level.json does not contain any characters")

        for character in characters:
            if character.CharacterId < 1:
                continue

            character_id: str = str(character.CharacterId)

            agent_full_path = os.path.join(input_agents_full_path, character_id)
            if not os.path.isdir(agent_full_path):
                raise ValueError(f"Agent {character_id} folder not found")

            agent_data_full_path = os.path.join(agent_full_path, AGENT_DATA_FILE_NAME)
            if not os.path.isfile(agent_data_full_path):
                raise ValueError(f"Agent {character_id} AgentData.json not found")

            json_agent_data = None
            with open(agent_data_full_path, mode='r') as file:
                json_agent_data = file.read()

            agent_data = AnimoSerializer.FromJson[AgentData](json_agent_data)
            self._agent_datas[character_id] = agent_data
            self._checkpoint_accumulators[character_id] = AgentCheckpointAccumulator()

            agent_checkpoint_full_path = os.path.join(agent_full_path, AGENT_CHECKPOINT_FILE_NAME)
            if os.path.isfile(agent_checkpoint_full_path):
                trainer_settings: TrainerSettings = self.run_options.behaviors.get(character_id)  # type: ignore
                trainer_settings.init_path = agent_checkpoint_full_path

            self.agent_output_paths[character_id] = os.path.join(training_session_full_folder_path, OUTPUT_FOLDER_NAME,
                                                                 AGENTS_FOLDER_NAME, character_id)

        # Output folders and files
        output_folder_full_path = os.path.join(training_session_full_folder_path, OUTPUT_FOLDER_NAME)
        if os.path.isdir(output_folder_full_path):
            timestamp = int(time.time_ns() / 1000)
            new_folder_name = OUTPUT_FOLDER_NAME + "_" + str(timestamp)
            new_folder_full_path = os.path.join(training_session_full_folder_path, new_folder_name)
            print(f"Found existing output folder. Renaming it to {new_folder_name}")
            os.rename(output_folder_full_path, new_folder_full_path)

        os.mkdir(output_folder_full_path)

        output_config_full_path = os.path.join(output_folder_full_path, CONFIG_FILE_NAME)
        with open(output_config_full_path, 'x') as f:
            yaml.dump(self.run_options.as_dict(), f, sort_keys=False)

        output_level_full_path = os.path.join(output_folder_full_path, LEVEL_FILE_NAME)
        shutil.copy(input_level_full_path, output_level_full_path)

    def get_agent_datas(self) -> List[AgentData]:
        with self._lock:
            return [clone(agent_data) for agent_data in self._agent_datas.values()]

    def episode_ended(self, step_index: int):
        with self._lock:
            for accumulator in self._checkpoint_accumulators.values():
                accumulator.OnEpisodeEnded(step_index)

    def on_agent_step(self, name: BehaviorName, step_index: int, evaluator: RewardEvaluator):
        with self._lock:
            accumulator = self._checkpoint_accumulators[name]

            for i, rwd in enumerate(evaluator.Rewards):
                for _ in range(evaluator.GetExecutionCount(rwd)):
                    accumulator.AddReward(i, step_index)

    def create_new_checkpoint(self, behaviour_name: str, timestamp: int) -> Tuple[AgentData, Optional[CheckpointData]]:
        with self._lock:
            accumulator = self._checkpoint_accumulators[behaviour_name]
            agent_data = self._agent_datas[behaviour_name]

            new_checkpoint = accumulator.OnCheckpointCreated(timestamp, agent_data.Id, self.id, agent_data.CurrentRewards)

            if new_checkpoint:
                agent_data.AddAndSelectCheckpoint(new_checkpoint)

            return (clone(agent_data), new_checkpoint)


def clone(agent_data: AgentData) -> AgentData:
    return AnimoSerializer.FromJson[AgentData](AnimoSerializer.ToJson(agent_data))
