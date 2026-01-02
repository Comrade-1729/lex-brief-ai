from abc import ABC, abstractmethod


class JurisdictionEngine(ABC):
    code: str  # IN, US, UK

    @abstractmethod
    def analyze(self, text: str, clauses: list, risks: list) -> list:
        """
        Returns jurisdiction-specific informational notes.
        Must NOT give legal advice.
        """
        pass
