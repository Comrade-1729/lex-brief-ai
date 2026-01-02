from documents.domain.clauses import ClauseType
from documents.services.risk_analysis.models import Risk, RiskLevel


def check_non_compete(clauses):
    risks = []

    for clause in clauses:
        if clause.clause_type != ClauseType.NON_COMPETE:
            continue

        text = clause.text.lower()
        score = 0.3
        reasons = ["Non-compete clause detected."]

        if "worldwide" in text or "global" in text:
            score += 0.3
            reasons.append("Scope appears worldwide.")

        if "5 year" in text or "five year" in text:
            score += 0.2
            reasons.append("Duration exceeds common enforceability norms.")

        if "any business" in text:
            score += 0.2
            reasons.append("Restriction applies to any business.")

        if score >= 0.7:
            level = RiskLevel.HIGH
        elif score >= 0.4:
            level = RiskLevel.MEDIUM
        else:
            level = RiskLevel.LOW

        risks.append(
            Risk(
                clause=clause,
                score=min(score, 1.0),
                level=level,
                explanation=" ".join(reasons),
            )
        )

    return risks
