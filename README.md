# LexBrief AI

LexBrief AI is a production-oriented legal document intelligence system that transforms
long, unreadable legal documents into **actionable legal insights**.

It goes beyond summarization by combining:

- Hierarchical legal summarization
- Clause-level intelligence
- Risk-aware analysis
- Jurisdiction-sensitive insights (India-first)

⚠️ LexBrief AI provides **informational insights only** and does **not** offer legal advice.

> ⚠️ See [DISCLAIMER.md](DISCLAIMER.md) for legal and usage limitations.

---

## 🏠 Architecture Diagram

Upload
  ↓
Text Extraction
  ↓
Preprocessing & Chunking
  ↓
Summarization Engine
  ↓
Clause Intelligence
  ↓
Risk Analysis
  ↓
Jurisdiction Notes
  ↓
UI Output

---

## 🚀 Core Capabilities

- 📂 Secure ingestion of PDF, DOCX, and TXT legal documents
- 🧠 Hierarchical summarization using LegalT5
- ⚖️ Clause extraction and classification (termination, payment, liability, etc.)
- 🚨 Rule-based legal risk analysis with explainable reasoning
- 🌏 Jurisdiction-aware insights (India, extensible to US/UK)
- 📊 Evaluation using ROUGE, clause recall, and latency metrics

---

## ⏱ Performance Notes

- **Cold-start latency** is dominated by transformer model initialization.
- **Clause extraction and rule-based risk analysis** consistently execute in under **50 ms**.
- **Jurisdiction analysis** is deterministic and constant-time.
- End-to-end latency is primarily influenced by document length and summarization cost.

Measured metrics are exposed directly in the UI for transparency.

---

## 🏗 Production Considerations

- Transformer models should be **loaded once at application startup** (singleton pattern).
- GPU acceleration is recommended for summarization workloads.
- Asynchronous task queues (Celery / Redis) are advised for large documents.
- Uploaded documents are not used for training and can be auto-deleted for privacy.
- Jurisdiction logic is strictly informational and avoids legal advice.

---

## 📦 Tech Stack

- **Backend:** Django (Python)
- **AI Models:** LegalT5, rule-based clause heuristics
- **Parsing:** pdfminer.six, python-docx
- **Frontend:** HTML, TailwindCSS
- **Database:** SQLite (PostgreSQL-ready)
- **Evaluation:** ROUGE-L, clause recall, latency profiling

---

## 🎓 Why This Project Matters

LexBrief AI demonstrates:

- Real-world NLP system design
- Legal domain understanding
- Explainable AI over black-box outputs
- Production-aware backend engineering
- Responsible AI boundaries

This project is designed as a **top-tier portfolio artifact** rather than a demo toy.

---

## Limitations

- Clause classification is heuristic-based in v1
- Jurisdiction insights are informational only
- No legal enforceability guarantees
- Large documents may incur higher latency

These limitations are intentional to preserve safety and explainability.

---

## ⚠️ Deployment Note (IMPORTANT!)

LexBrief AI supports transformer-based summarization using LegalT5.
However, due to memory constraints on lightweight cloud platforms
(e.g. Render free tier), transformer inference is disabled in production.

Production deployments use a deterministic dummy summarizer by default.
The LegalT5 pipeline can be enabled on GPU-backed or high-memory instances
by setting:

USE_DUMMY_SUMMARIZER=0

This design demonstrates production-safe ML deployment practices,
feature flagging, and infrastructure-aware system design.

---
