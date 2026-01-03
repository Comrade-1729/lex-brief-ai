from documents.services.risk_analysis.models import RiskLevel, RiskType, Risk

EXPECTED_CLAUSES = {
    "Confidentiality",
    "Termination",
    "Payment",
    "Governing Law",
}

def check_missing_clauses(detected_clauses):
    detected_types = {c.clause_type.value for c in detected_clauses}
    missing = EXPECTED_CLAUSES - detected_types

    risks = []
    for clause_name in missing:
        risks.append(
            Risk(
                clause=None,
                score=0.6,
                level=RiskLevel.MEDIUM,
                explanation=f"{clause_name} clause not found in the document."
            )
        )
    return risks
