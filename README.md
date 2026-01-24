# ⚖️ LexBrief AI

**Production-Grade Legal Document Intelligence System**.

LexBrief AI transforms long, unreadable legal documents into **actionable, explainable legal insights**.

Unlike generic summarizers, it is designed as a **real-world, production-aware system** that combines NLP, domain logic, and infrastructure constraints to safely analyze legal text.

> ⚠️ LexBrief AI provides **informational insights only** and does **not** offer legal advice.
> See [DISCLAIMER.md](DISCLAIMER.md) for legal and usage limitations.

---

## 🧠 What Makes LexBrief AI Different?

LexBrief AI goes **beyond summarization** by integrating:

* 🧩 **Hierarchical legal summarization**
* ⚖️ **Clause-level intelligence**
* 🚨 **Explainable, rule-based risk analysis**
* 🌏 **Jurisdiction-aware insights (India-first)**

This project is intentionally built as a **portfolio-grade system**, not a demo toy.

---

## 🏗 High-Level Architecture

User Upload
    ↓
Text Extraction (PDF / DOCX / TXT)
    ↓
Preprocessing & Chunking
    ↓
Summarization Engine
    ↓
Clause Extraction & Classification
    ↓
Risk Analysis (Explainable Rules)
    ↓
Jurisdiction Intelligence
    ↓
UI Output + Metrics

---

## 🚀 Core Capabilities

* 📂 Secure ingestion of **PDF, DOCX, and TXT** legal documents
* 🧠 Hierarchical summarization using **LegalT5** (feature-flagged)
* ⚖️ Clause extraction and classification
  *(termination, payment, non-compete, liability, etc.)*
* 🚨 Rule-based legal risk analysis with **human-readable explanations**
* 🌏 Jurisdiction-aware insights (India, extensible to US/UK)
* 📊 Built-in evaluation:

  * Clause recall
  * ROUGE metrics
  * Latency profiling (visible in UI)

---

## ⏱ Performance Characteristics

* **Cold-start latency** is dominated by transformer initialization
* **Clause extraction + risk analysis** consistently execute in **< 50 ms**
* **Jurisdiction analysis** is deterministic and constant-time
* End-to-end latency scales primarily with document length

All latency metrics are surfaced directly in the UI for transparency.

---

## 🏗 Production & Deployment Considerations

* Transformer models are **loaded once** using a singleton factory
* Heavy ML inference is **feature-flagged** for infrastructure safety
* Designed to survive:

  * Low-memory cloud environments
  * Worker restarts
  * Cold starts
* Uploaded documents are **not used for training**
* Jurisdiction logic is **informational only** (no legal advice)

---

## 📦 Tech Stack

* **Backend:** Django (Python)
* **AI / NLP:** PyTorch-based LegalT5, heuristic clause classifiers
* **Parsing:** pdfminer.six, python-docx
* **Frontend:** HTML + TailwindCSS
* **Database:** SQLite (PostgreSQL-ready)
* **Evaluation:** ROUGE-L, clause recall, latency metrics
* **Deployment:** Docker + Gunicorn (Render-compatible)

---

## ⚠️ Deployment Note (IMPORTANT)

LexBrief AI supports transformer-based summarization using **LegalT5**.

However, **lightweight cloud platforms (e.g. Render free tier)** cannot safely load large transformer models.

### Default Production Behavior

* Transformer inference is **disabled**
* A deterministic **Dummy Summarizer** is used
* System remains fully functional and stable

### Enable LegalT5 (GPU / High-Memory Only)

```bash
USE_DUMMY_SUMMARIZER=0
```

This design demonstrates:

* Feature flagging
* Infrastructure-aware ML deployment
* Production-safe fallback strategies

---

## 🧠 Key Design Decisions

### Why rule-based risk analysis?

Legal risk scoring must be **explainable and auditable**.
Rule-based logic provides deterministic reasoning suitable for legal contexts.

### Why feature-flagged transformers?

Transformer models require significant memory.
Disabling them by default prevents crashes and mirrors real-world ML deployment practices.

### Why jurisdiction engines?

Legal interpretation varies by country.
Each jurisdiction is isolated to avoid logic coupling and allow safe extensibility.

### Why not end-to-end ML?

Pure ML approaches risk hallucinations and lack explainability.
LexBrief AI prioritizes **correctness, traceability, and safety**.

---

## ⚠️ Known Limitations

* Clause classification is heuristic-based (v1)
* Jurisdiction insights are informational only
* No legal enforceability guarantees
* Very large documents may incur higher latency

These constraints are **intentional** to preserve explainability and safety.

---

## 🔮 Future Enhancements

* Async processing with **Celery + Redis**
* GPU-backed LegalT5 deployment
* ML-based risk scoring with explanation layers
* Additional jurisdictions (EU, Singapore)
* Contract comparison & version diffing

---

## 🎓 Why This Project Matters

LexBrief AI demonstrates:

* Real-world NLP system design
* Legal-domain reasoning
* Explainable AI over black-box outputs
* Production-aware backend engineering
* Responsible AI boundaries

This repository is designed to be **discussed in interviews**, not just run.

---

## 📄 Research & Publication

This system is accompanied by a technical whitepaper describing
its safety-first architecture, evaluation philosophy, and
deployment constraints.

* **LexBrief AI: A Safety-First, Explainable Legal Document Intelligence System**
* Status: Preprint (arXiv submission in progress)
* PDF: `paper/lexbrief_ai.pdf`

---

## 📚 Citation

If you reference this system, please cite:

LexBrief AI: A Safety-First, Explainable Legal Document Intelligence System  
Ishaan Shanker Srivastava, January 2026

---
