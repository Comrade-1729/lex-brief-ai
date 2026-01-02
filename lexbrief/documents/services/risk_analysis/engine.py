from documents.services.risk_analysis.rules.missing_clause import check_missing_clauses
from documents.services.risk_analysis.rules.non_compete import check_non_compete


def analyze_risks(clauses):
    risks = []

    risks.extend(check_missing_clauses(clauses))
    risks.extend(check_non_compete(clauses))

    return risks
