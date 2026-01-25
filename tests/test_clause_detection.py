from documents.services.clause_extraction import extract_clauses
from documents.domain.clauses import ClauseType

SAMPLE_TEXT = """
1. Confidentiality
Employee shall keep secrets.

2. Termination
Company may terminate anytime.
"""

def test_clause_extraction_basic():
    clauses = extract_clauses(SAMPLE_TEXT)
    types = {c.clause_type for c in clauses}

    assert ClauseType.CONFIDENTIALITY in types
    assert ClauseType.TERMINATION in types
