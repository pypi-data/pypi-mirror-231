import typing
from TransformsAI.Animo.Learning.Sensors import SensorConfig, SensorSpec, Sensor, GridSensorShape
from TransformsAI.Animo.Objects.Character import CharacterObject
from TransformsAI.Animo.Numerics import Vec2Int
from System import Span_1, Array_1
from TransformsAI.Animo.Learning.Sensors.Vector import VectorSensor
from System.Collections.Generic import Dictionary_2, IComparer_1
from TransformsAI.Animo.Constants import TypeIds
from TransformsAI.Animo import GridObject

class ActorAtCellSensor(CellSensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    ActorLength : int
    Id : str
    RotationLength : int
    SensorName : str
    UnknownActorCode : int
    VariantLength : int
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetObservations(self, character: CharacterObject, absoluteCell: Vec2Int, values: Span_1[float]) -> None: ...


class CellSensor(Sensor):
    SensorName : str
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    # Skipped GetObservations due to it being static, abstract and generic.

    GetObservations : GetObservations_MethodGroup
    class GetObservations_MethodGroup:
        @typing.overload
        def __call__(self, character: CharacterObject, absoluteCell: Vec2Int, values: Span_1[float]) -> None:...
        @typing.overload
        def __call__(self, character: CharacterObject, absoluteCell: Vec2Int, observations: Array_1[float], offset: int = ...) -> None:...



class FlattenedGridSensor(VectorSensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    Id : str
    SensorName : str
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetObservations(self, character: CharacterObject, values: Span_1[float]) -> None: ...


class GridSensor(Sensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    Id : str
    SensorName : str
    XLengthProperty : str
    ZLengthProperty : str
    @property
    def GridShape(self) -> GridSensorShape: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetGridObservations(self, character: CharacterObject, xzdObservations: Array_1[float]) -> None: ...


class HeldObjectAtCellSensor(CellSensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    Id : str
    SensorName : str
    SensorObservationEncodingProperty : str
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetObservations(self, character: CharacterObject, absoluteCell: Vec2Int, values: Span_1[float]) -> None: ...


class MediumAtCellOneHotSensor(CellSensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    Id : str
    SensorName : str
    UnknownMediumIndex : int
    @property
    def Length(self) -> int: ...
    @classmethod
    @property
    def MediumTypeIds(cls) -> Dictionary_2[TypeIds, int]: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetObservations(self, character: CharacterObject, absoluteCell: Vec2Int, values: Span_1[float]) -> None: ...


class ObjectOnFloorAtCellSensor(CellSensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    AdditiveObservationEncodingProperty : str
    Id : str
    SensesActorsObjectGroupsProperty : str
    SensesHeldObjectProperty : str
    SensesMediumsObjectGroupsProperty : str
    SensesRegularObjectGroupsProperty : str
    SensorName : str
    SensorObservationEncodingProperty : str
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetObservations(self, character: CharacterObject, absoluteCell: Vec2Int, values: Span_1[float]) -> None: ...

    class ObjectGroupPriorityComparer(IComparer_1[GridObject]):
        def __init__(self) -> None: ...
        def Compare(self, a: GridObject, b: GridObject) -> int: ...



class TerrainAtCellSensor(CellSensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    Id : str
    SensorName : str
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetObservations(self, character: CharacterObject, absoluteCell: Vec2Int, values: Span_1[float]) -> None: ...

