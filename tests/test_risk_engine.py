from documents.services.risk_analysis.engine import analyze_risks
from documents.domain.clauses import Clause, ClauseType

def test_risk_engine_runs():
    clauses = [
        Clause(
            clause_type=ClauseType.NON_COMPETE,
            text="Global restriction for five years",
            confidence=0.8,
        )
    ]

    risks = analyze_risks(clauses)
    assert len(risks) > 0
