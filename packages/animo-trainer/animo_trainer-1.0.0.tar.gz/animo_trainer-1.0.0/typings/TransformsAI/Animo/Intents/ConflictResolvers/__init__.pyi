import abc
from System.Collections.Generic import List_1
from TransformsAI.Animo.Intents import Intent

class ExecuteAllConflictResolver(abc.ABC):
    @staticmethod
    def Resolve(originalIntents: List_1[Intent]) -> None: ...

