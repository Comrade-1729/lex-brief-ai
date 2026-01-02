from documents.domain.clauses import ClauseType
from documents.services.risk_analysis.models import Risk, RiskLevel


REQUIRED_CLAUSES = {
    ClauseType.TERMINATION,
    ClauseType.GOVERNING_LAW,
    ClauseType.JURISDICTION,
}


def check_missing_clauses(clauses):
    risks = []

    present = {clause.clause_type for clause in clauses}
    missing = REQUIRED_CLAUSES - present

    for clause_type in missing:
        risks.append(
            Risk(
                clause=None,
                score=0.6,
                level=RiskLevel.MEDIUM,
                explanation=f"Missing mandatory clause: {clause_type.value}."
            )
        )

    return risks
