from documents.domain.clauses import ClauseType

CLAUSE_KEYWORDS = {
    ClauseType.TERMINATION: ["terminate", "termination", "expiry"],
    ClauseType.CONFIDENTIALITY: ["confidential", "non-disclosure"],
    ClauseType.GOVERNING_LAW: [
        "governing law",
        "jurisdiction",
        "courts at",
        "subject to the laws of"
    ],
    ClauseType.PAYMENT: ["payment", "fees", "consideration"],
    ClauseType.LIABILITY: ["liability", "liable"],
    ClauseType.INDEMNITY: ["indemnity", "indemnify"],
    ClauseType.FORCE_MAJEURE: ["force majeure"],
}

def classify_clause(title: str, content: str):
    text = (title + " " + content).lower()
    for clause_type, keywords in CLAUSE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return clause_type, 0.9
    return ClauseType.UNKNOWN, 0.3
