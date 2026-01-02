from dataclasses import dataclass
from typing import Optional
from enum import Enum
from documents.domain.clauses import Clause


class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


@dataclass
class Risk:
    clause: Optional[Clause]
    score: float
    level: RiskLevel
    explanation: str

    def to_dict(self):
        return {
            "clause_type": self.clause.clause_type.value if self.clause else "Missing",
            "title": self.clause.title if self.clause else None,
            "score": round(self.score, 2),
            "level": self.level.value,
            "explanation": self.explanation,
        }
