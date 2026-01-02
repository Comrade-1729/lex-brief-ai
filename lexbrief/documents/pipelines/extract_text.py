from pdfminer.high_level import extract_text as pdf_extract
import docx

def extract_text(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        return pdf_extract(file_path)
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
