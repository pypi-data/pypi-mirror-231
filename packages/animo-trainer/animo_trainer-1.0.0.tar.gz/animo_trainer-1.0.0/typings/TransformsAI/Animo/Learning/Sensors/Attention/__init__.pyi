import typing
from TransformsAI.Animo.Learning.Sensors import Sensor, SensorConfig, AttentionSensorShape, SensorSpec
from TransformsAI.Animo.Objects.Character import CharacterObject
from System import Array_1, Span_1
from TransformsAI.Animo import GridObject

class AttentionSensor(Sensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    Id : str
    MaxNumEntitiesProperty : str
    SensorName : str
    @property
    def AttentionSensorShape(self) -> AttentionSensorShape: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetAttentionObservations(self, character: CharacterObject, numObjNumValsObservations: Array_1[float]) -> None: ...


class ObjectEntitySensor(Sensor):
    SensorName : str
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    # Skipped GetObservations due to it being static, abstract and generic.

    GetObservations : GetObservations_MethodGroup
    class GetObservations_MethodGroup:
        @typing.overload
        def __call__(self, character: CharacterObject, sensedObject: GridObject, values: Span_1[float]) -> None:...
        @typing.overload
        def __call__(self, character: CharacterObject, sensedObject: GridObject, observations: Array_1[float], offset: int = ...) -> None:...



class ObjectTypeAndLocationSensor(ObjectEntitySensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    Id : str
    IsHeldObservationLength : int
    LocationObservationLength : int
    SensorName : str
    SensorObservationEncodingProperty : str
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetObservations(self, character: CharacterObject, sensedObject: GridObject, values: Span_1[float]) -> None: ...

