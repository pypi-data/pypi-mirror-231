import typing
from TransformsAI.Animo.Learning.Sensors import SensorConfig, SensorSpec, Sensor
from System import ValueTuple_4, Span_1, Array_1
from TransformsAI.Animo.Constants import TypeIds
from TransformsAI.Animo.Objects.Character import CharacterObject

class CompassSensor(VectorSensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    CompassIgnoreVariantIdProperty : str
    CompassIndex : int
    CompassIndexProperty : str
    CompassTypeIdProperty : str
    CompassVariantIdProperty : str
    Id : str
    MaxCompassDistance : float
    SensorName : str
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetCompassParameters(self) -> ValueTuple_4[int, TypeIds, int, bool]: ...
    def GetObservations(self, character: CharacterObject, values: Span_1[float]) -> None: ...
    def UpdateCompass(self, typeId: TypeIds, variantId: int, ignoreVariantId: bool) -> None: ...


class SurroundingsSensor(VectorSensor):
    def __init__(self, sensorConfig: SensorConfig) -> None: ...
    Id : str
    SensorName : str
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    def GetObservations(self, character: CharacterObject, values: Span_1[float]) -> None: ...


class VectorSensor(Sensor):
    SensorName : str
    @property
    def Length(self) -> int: ...
    @property
    def SensorSpec(self) -> SensorSpec: ...
    # Skipped GetObservations due to it being static, abstract and generic.

    GetObservations : GetObservations_MethodGroup
    class GetObservations_MethodGroup:
        @typing.overload
        def __call__(self, character: CharacterObject, values: Span_1[float]) -> None:...
        @typing.overload
        def __call__(self, character: CharacterObject, observations: Array_1[float], offset: int = ...) -> None:...


