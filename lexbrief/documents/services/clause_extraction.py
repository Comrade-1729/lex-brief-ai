from typing import List
from documents.domain.clauses import Clause, ClauseType
from documents.pipelines.section_splitter import split_sections
from documents.ai.clause_classifier import classify_clause


def extract_clauses(text: str) -> List[Clause]:
    """
    Extracts legal clauses from structured documents.

    Pipeline:
    1. Split document into sections
    2. Classify each section into a ClauseType
    3. Return Clause domain objects (model-agnostic)

    NOTE:
    - This function MUST NOT perform risk scoring
    - This function MUST NOT apply jurisdiction logic
    """

    sections = split_sections(text)
    clauses: List[Clause] = []

    for title, content in sections:
        clause_type, confidence = classify_clause(title, content)

        clause = Clause(
            clause_type=clause_type,
            title=title,
            text=content,
            confidence=confidence
        )

        clauses.append(clause)

    return clauses
