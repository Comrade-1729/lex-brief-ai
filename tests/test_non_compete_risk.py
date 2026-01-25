from documents.services.risk_analysis.rules.non_compete import check_non_compete
from documents.domain.clauses import Clause, ClauseType
from documents.services.risk_analysis.models import RiskLevel

def test_high_risk_non_compete():
    clause = Clause(
        clause_type=ClauseType.NON_COMPETE,
        title="Non-Compete",
        text="Employee shall not engage in any business worldwide for five years.",
        confidence=0.9,
    )

    risks = check_non_compete([clause])

    assert len(risks) == 1
    assert risks[0].level == RiskLevel.HIGH
