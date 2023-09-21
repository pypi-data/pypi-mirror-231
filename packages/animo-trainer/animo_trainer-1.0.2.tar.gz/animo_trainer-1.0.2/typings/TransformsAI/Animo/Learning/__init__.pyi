import typing, abc
from TransformsAI.Animo.Objects.Character import CharacterObject
from System import Array_1
from System.Collections.Generic import HashSet_1
from TransformsAI.Animo.Constants import TypeIds
from TransformsAI.Animo import VoxelGrid

class CharacterActionMask(abc.ABC):
    @staticmethod
    def ApplyActionMask(character: CharacterObject, mask: Array_1[bool]) -> None: ...


class EndCondition:
    def __init__(self) -> None: ...
    NeedsCharacters : bool
    RequiredObjects : HashSet_1[TypeIds]
    StepLimit : typing.Optional[int]
    def IsMet(self, grid: VoxelGrid, stepCount: int) -> bool: ...
    def Validate(self, grid: VoxelGrid) -> None: ...

