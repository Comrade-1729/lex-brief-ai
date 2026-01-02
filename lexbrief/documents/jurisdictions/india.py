from documents.jurisdictions.base import JurisdictionEngine
from documents.domain.clauses import ClauseType
from documents.services.risk_analysis.models import RiskLevel

class IndiaJurisdiction(JurisdictionEngine):
    """
    India-specific jurisdiction enrichment layer.

    IMPORTANT:
    - Informational only
    - No legal advice
    - No enforceability guarantees
    """

    code = "IN"

    def analyze(self, text: str, clauses: list, risks: list) -> list:
        notes: list[str] = []

        clause_types = {c.clause_type for c in clauses}

        # --- Governing Law ---
        if ClauseType.GOVERNING_LAW not in clause_types:
            notes.append(
                "No governing law clause detected. "
                "Indian contracts typically specify governing law under the Indian Contract Act, 1872."
            )

        # --- Termination ---
        if ClauseType.TERMINATION in clause_types:
            notes.append(
                "Termination clauses in India are subject to reasonableness "
                "and public policy considerations under Indian contract law."
            )

        # --- Non-compete ---
        for risk in risks:
            if (
                risk.clause
                and risk.clause.clause_type == ClauseType.NON_COMPETE
                and risk.level == RiskLevel.HIGH
            ):
                notes.append(
                    "Non-compete obligations may be unenforceable in India "
                    "under Section 27 of the Indian Contract Act, 1872, "
                    "except in limited circumstances."
                )
                break

        # --- Liability ---
        if ClauseType.LIABILITY in clause_types:
            notes.append(
                "Limitation of liability clauses in India are generally enforceable, "
                "but may be restricted in cases involving fraud, gross negligence, "
                "or statutory violations."
            )

        # --- Missing clauses (system-level risks) ---
        for risk in risks:
            if risk.clause is None and risk.level == RiskLevel.MEDIUM:
                notes.append(
                    "Certain standard clauses appear to be missing. "
                    "Indian commercial contracts typically include confidentiality, "
                    "termination, payment, and governing law provisions."
                )
                break

        return notes
