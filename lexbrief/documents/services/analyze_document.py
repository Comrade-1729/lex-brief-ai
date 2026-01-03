from documents.services.document_type import detect_document_type, DocumentType
from documents.pipelines.extract_text import extract_text
from documents.pipelines.preprocess import clean_text
from documents.pipelines.chunking import chunk_text
from documents.services.clause_extraction import extract_clauses
from documents.services.risk_analysis.engine import analyze_risks
from documents.jurisdictions.registry import get_jurisdiction_engine
from documents.jurisdictions.services.detect_jurisdiction import detect_jurisdiction
from documents.evaluation.clause_recall import evaluate_clause_recall
from documents.config.limits import MAX_DOCUMENT_WORDS
import time

def analyze(
    file_path: str,
    summarizer,
    jurisdiction_code: str | None = None
) -> dict:
    
    if len(clean.split()) > MAX_DOCUMENT_WORDS:
        return {
            "error": "Document too large for analysis",
            "max_words": MAX_DOCUMENT_WORDS,
        }

    start_total = time.time()
    # 1. Extract + clean
    raw_text = extract_text(file_path)
    clean = clean_text(raw_text)
    t_extract = time.time()

    # 2. Detect document type
    doc_type = detect_document_type(clean)

    # 3. Resolve jurisdiction
    if jurisdiction_code:
        jurisdiction = jurisdiction_code
    else:
        detected = detect_jurisdiction(clean)
        jurisdiction = detected.value if detected else "IN"

    # 4. Summarization (always allowed)
    chunks = chunk_text(clean)
    summaries = [summarizer.summarize(chunk) for chunk in chunks]
    final_summary = " ".join(summaries)
    t_summary = time.time()

    result = {
        "summary": final_summary,
        "document_type": doc_type.value,
        "jurisdiction": jurisdiction,
        "clauses": [],
        "risks": [],
        "jurisdiction_notes": [],
    }

    # 5. Clause + Risk analysis (structured only)
    if doc_type == DocumentType.STRUCTURED:
        clauses = extract_clauses(clean)
        risks = analyze_risks(clauses)

        result["clauses"] = [c.to_dict() for c in clauses]
        result["risks"] = [r.to_dict() for r in risks]

        jurisdiction_engine = get_jurisdiction_engine(jurisdiction)
        if jurisdiction_engine:
            try:
                result["jurisdiction_notes"] = jurisdiction_engine.analyze(
                    text=clean,
                    clauses=clauses,
                    risks=risks,
                )
            except Exception as e:
                result["jurisdiction_notes"] = [
                    "Jurisdiction analysis failed",
                    str(e),
                ]
        try:
            predicted_clause_types = [c.clause_type.value for c in clauses]
            recall_metrics = evaluate_clause_recall(
                predicted_clause_types,
                "documents/evaluation/data/india_employment.gold.json"
            )
            result["evaluation"] = recall_metrics
        except Exception:
            result["evaluation"] = None
    else:
        result["note"] = (
            "Clause extraction and risk analysis are disabled "
            "for unstructured documents."
        )
    
    end_total = time.time()

    result["latency"] = {
        "extract_seconds": round(t_extract - start_total, 3),
        "summarize_seconds": round(t_summary - t_extract, 3),
        "analysis_seconds": round(end_total - t_summary, 3),
        "total_seconds": round(end_total - start_total, 3),
    }

    return result
