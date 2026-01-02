from dataclasses import dataclass
from enum import Enum
from typing import Optional, List


class ClauseType(str, Enum):
    TERMINATION = "Termination"
    GOVERNING_LAW = "Governing Law"
    CONFIDENTIALITY = "Confidentiality"
    PAYMENT = "Payment"
    LIABILITY = "Liability"
    INDEMNITY = "Indemnity"
    FORCE_MAJEURE = "Force Majeure"
    DISPUTE_RESOLUTION = "Dispute Resolution"
    NON_COMPETE = "Non-Compete"
    ASSIGNMENT = "Assignment"
    AMENDMENT = "Amendment"
    UNKNOWN = "Unknown"

@dataclass
class Clause:
    clause_type: ClauseType
    text: str                     # full clause text (single source of truth)
    confidence: float             # model confidence (0.0–1.0)

    title: Optional[str] = None   # extracted heading if available
    parties: Optional[List[str]] = None
    obligation: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "clause_type": self.clause_type.value,
            "title": self.title,
            "text": self.text,
            "confidence": round(self.confidence, 3),
            "parties": self.parties or [],
            "obligation": self.obligation,
        }
