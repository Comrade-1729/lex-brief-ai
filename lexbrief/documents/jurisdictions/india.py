from documents.jurisdictions.base import JurisdictionEngine


class IndiaJurisdiction(JurisdictionEngine):
    code = "IN"

    def analyze(self, text: str, clauses: list, risks: list) -> list:
        notes = []

        clause_types = {c["type"] for c in clauses}

        if "Governing Law" not in clause_types:
            notes.append(
                "Indian contracts typically specify governing law "
                "under the Indian Contract Act, 1872."
            )

        if "Termination" in clause_types:
            notes.append(
                "Termination clauses are subject to reasonableness "
                "and public policy under Indian law."
            )

        return notes
