from documents.jurisdictions.services.jurisdiction import Jurisdiction


def detect_jurisdiction(text: str) -> Jurisdiction:
    t = text.lower()

    if "constitution of india" in t or "indian penal code" in t or "article" in t:
        return Jurisdiction.INDIA

    if "united states code" in t or "usc" in t:
        return Jurisdiction.USA

    if "uk act" in t or "parliament of the united kingdom" in t:
        return Jurisdiction.UK

    return Jurisdiction.GENERIC
