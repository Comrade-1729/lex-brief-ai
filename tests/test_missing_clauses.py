from documents.services.risk_analysis.rules.missing_clause import check_missing_clauses
from documents.domain.clauses import Clause, ClauseType

def test_missing_payment_clause_detected():
    clauses = [
        Clause(
            clause_type=ClauseType.CONFIDENTIALITY,
            text="Confidential info",
            confidence=0.9,
        )
    ]

    risks = check_missing_clauses(clauses)
    explanations = [r.explanation for r in risks]

    assert any("Payment clause not found" in e for e in explanations)
