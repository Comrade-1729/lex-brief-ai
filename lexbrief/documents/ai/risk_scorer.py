from abc import ABC, abstractmethod

class RiskScorer(ABC):
    @abstractmethod
    def score(self, clauses: list) -> dict:
        pass
