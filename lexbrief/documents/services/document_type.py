from enum import Enum

class DocumentType(Enum):
    STRUCTURED = "STRUCTURED"
    UNSTRUCTURED = "UNSTRUCTURED"

def detect_document_type(text: str) -> DocumentType:
    keywords = ["agreement", "party", "termination", "liability"]
    matches = sum(1 for k in keywords if k in text.lower())
    return DocumentType.STRUCTURED if matches >= 2 else DocumentType.UNSTRUCTURED
