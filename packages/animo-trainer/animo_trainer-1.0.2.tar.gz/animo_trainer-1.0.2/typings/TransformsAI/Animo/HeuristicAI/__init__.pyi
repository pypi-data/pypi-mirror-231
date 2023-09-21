import typing, abc
from System.Runtime.CompilerServices import ConditionalWeakTable_2
from TransformsAI.Animo.Objects.Character import CharacterObject
from TransformsAI.Animo.Constants import TypeIds
from System import Predicate_1
from TransformsAI.Animo import GridObject

class HeuristicBehaviourExtensions(abc.ABC):
    CrystalChopperSightDistance : int
    CrystalChopperStates : ConditionalWeakTable_2[CharacterObject, HeuristicBehaviourExtensions.CrystalChopperState]
    CrystalChopperStepsBeforeAttack : int
    CrystalChopperTriggerDuration : int
    MaxSightDistance : int
    RandomRotationFrequency : float
    @staticmethod
    def ChopAllTrees(character: CharacterObject, targetAnimoOnMissingTarget: bool) -> CharacterObject.Actions: ...
    @staticmethod
    def DecideAction(autoBehaviour: HeuristicBehaviours, character: CharacterObject) -> CharacterObject.Actions: ...
    @staticmethod
    def GetCrystalChopperAction(character: CharacterObject) -> CharacterObject.Actions: ...
    @staticmethod
    def GetCrystalChopperTriggeredAction(character: CharacterObject, chopperState: HeuristicBehaviourExtensions.CrystalChopperState) -> CharacterObject.Actions: ...
    @staticmethod
    def MoveRandomly(character: CharacterObject) -> CharacterObject.Actions: ...
    @staticmethod
    def SmackAllBalls(character: CharacterObject, targetAnimoOnMissingTarget: bool) -> CharacterObject.Actions: ...
    @staticmethod
    def UseOnTargetWithTool(character: CharacterObject, tool: TypeIds, targetDiscriminant: Predicate_1[GridObject], targetAnimoOnMissingTarget: bool) -> CharacterObject.Actions: ...
    @staticmethod
    def WaterWiltedFlowers(character: CharacterObject, targetAnimoOnMissingTarget: bool) -> CharacterObject.Actions: ...

    class CrystalChopperState:
        def __init__(self) -> None: ...
        StepsBeforeAttack : typing.Optional[int]
        StepsSinceTriggeredByAnimo : typing.Optional[int]
        Triggerer : CharacterObject



class HeuristicBehaviours(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    StandStill : HeuristicBehaviours # 0
    MoveRandomly : HeuristicBehaviours # 1
    ChopTreesWithAxe : HeuristicBehaviours # 2
    WaterAllFlowers : HeuristicBehaviours # 3
    CrystalChopper : HeuristicBehaviours # 4
    SmackBallsWithBat : HeuristicBehaviours # 5

