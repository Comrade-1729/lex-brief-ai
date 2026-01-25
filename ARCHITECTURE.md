# 🏗️ ARCHITECTURE.md

## LexBrief AI — System Architecture & Design Rationale

---

## 1. Architectural Philosophy

LexBrief AI is designed as a **production-aware, safety-first legal document intelligence system**.

The core philosophy is:

> **Correctness, explainability, and operational safety matter more than raw model power.**

Legal documents are high-risk inputs.
Therefore, the system prioritizes:

* Deterministic behavior
* Explainable outputs
* Clear separation of concerns
* Infrastructure-aware AI deployment
* Explicit non-advisory boundaries

This architecture is intentionally **not end-to-end ML**.

---

## 2. High-Level System Flow

```
User Upload
   ↓
File Ingestion & Validation
   ↓
Text Extraction (PDF / DOCX / TXT)
   ↓
Text Cleaning & Preprocessing
   ↓
Chunking (bounded memory)
   ↓
Summarization Engine (feature-flagged)
   ↓
Clause Extraction (structured docs only)
   ↓
Rule-Based Risk Analysis
   ↓
Jurisdiction Enrichment (informational)
   ↓
Evaluation & Latency Metrics
   ↓
UI Rendering
```

Each stage is **independently testable** and **replaceable**.

---

## 3. Layered Architecture

LexBrief AI follows a **clean, layered architecture**:

```
┌──────────────────────────┐
│        UI Layer          │  Django views & templates
└──────────▲───────────────┘
           │
┌──────────┴───────────────┐
│    Application Services  │  Orchestration & workflows
└──────────▲───────────────┘
           │
┌──────────┴───────────────┐
│     Domain Layer         │  Clauses, Risks, Jurisdiction
└──────────▲───────────────┘
           │
┌──────────┴───────────────┐
│    AI / Intelligence     │  Summarization, classification
└──────────▲───────────────┘
           │
┌──────────┴───────────────┐
│ Infrastructure & Config  │  Limits, feature flags
└──────────────────────────┘
```

No layer reaches “up” the stack.

---

## 4. Domain-Centric Design

### 4.1 Domain Objects (Single Source of Truth)

Core legal concepts live in **pure Python domain objects**:

* `Clause`
* `ClauseType`
* `Risk`
* `RiskLevel`
* `Jurisdiction`

These objects:

* Contain **no Django dependencies**
* Are serializable
* Are used consistently across services
* Represent **legal reasoning units**, not UI artifacts

This ensures portability beyond Django if needed.

---

## 5. Document Processing Pipeline

### 5.1 Text Extraction

Supported formats:

* PDF → `pdfminer.six`
* DOCX → `python-docx`
* TXT → direct read

Design choices:

* Extraction **never crashes** the pipeline
* Errors degrade gracefully to empty text
* No document content is used for training

---

### 5.2 Preprocessing

Responsibilities:

* Null byte removal
* Whitespace normalization
* Line cleanup

This step is intentionally simple to preserve **legal phrasing fidelity**.

---

### 5.3 Chunking (Memory Safety)

Documents are chunked by word count:

* Prevents OOM errors
* Enables bounded inference
* Supports large documents safely

Chunk size is centrally configured in `documents/config/limits.py`.

---

## 6. Summarization Architecture

### 6.1 Feature-Flagged Summarization

Summarization is **explicitly feature-flagged**:

```bash
USE_DUMMY_SUMMARIZER=1  # default
USE_DUMMY_SUMMARIZER=0  # full inference
```

### 6.2 Summarizer Factory (Singleton)

```python
summarizer = get_summarizer()
```

Guarantees:

* Models load only once
* Cold start cost is isolated
* No accidental transformer loading in production

---

### 6.3 Dummy Summarizer (Default)

Used in:

* Public demos
* Low-memory environments
* CI / test runs

Purpose:

* Preserve pipeline behavior
* Maintain latency predictability
* Demonstrate system logic, not model throughput

---

### 6.4 LegalT5 Summarizer (Opt-in)

Characteristics:

* Deterministic (no sampling)
* Beam search only
* Token-limited input/output
* Explicit GPU/CPU handling

This reflects **real-world ML deployment discipline**.

---

## 7. Clause Extraction Engine

Clause extraction is **not ML-based** in v1.

Pipeline:

1. Section splitting using regex heuristics
2. Keyword-based classification
3. Confidence assignment
4. Domain object creation

Why heuristic-first?

* Legal clause boundaries are often structural
* Determinism > recall in early versions
* Explainability is mandatory

This layer is intentionally replaceable with ML in future versions.

---

## 8. Risk Analysis Engine

### 8.1 Rule-Based by Design

Risk analysis uses **explicit, auditable rules**.

Reasons:

* Legal risk scoring must be explainable
* Rules can be reviewed by humans
* Avoids hallucinated risk explanations

Each risk rule:

* Lives in its own file
* Produces structured `Risk` objects
* Includes a human-readable explanation

---

### 8.2 Supported Risk Types (v1)

* Missing standard clauses
* Non-compete enforceability risks
* Scope, duration, and breadth violations

Rules are composable and order-independent.

---

## 9. Jurisdiction Engine

### 9.1 Jurisdiction Detection

Jurisdiction is inferred using **legal references**, not geography:

* Statutes
* Legal terms
* Explicit mentions

Fallback is always safe (`GENERIC`).

---

### 9.2 Jurisdiction Engines

Each jurisdiction has:

* Its own engine
* Isolated logic
* Informational-only output

Example:

* India-specific non-compete unenforceability under Section 27

🚫 Jurisdiction engines **never**:

* Give legal advice
* Guarantee enforceability
* Override risk analysis

---

## 10. Evaluation & Metrics

LexBrief AI embeds **evaluation into the system**, not as an afterthought.

Metrics include:

* Clause recall (gold-standard comparison)
* Latency per pipeline stage
* End-to-end runtime

These metrics are:

* Computed during analysis
* Visible in the UI
* Useful for debugging and tuning

---

## 11. Django’s Role in the System

Django is used as:

* Request router
* Persistence layer
* Template renderer

Django is **not**:

* A business logic container
* A domain model authority
* A testing framework (pytest is used instead)

This keeps the system framework-agnostic.

---

## 12. Testing Strategy

Tests are organized by **system boundary**, not by framework:

* Clause extraction tests
* Risk rule tests
* Summarizer selection tests
* Pipeline smoke tests
* View availability tests

Principles:

* Fast
* Deterministic
* Minimal mocking
* CI-friendly

---

## 13. Safety & Responsibility Guarantees

LexBrief AI explicitly guarantees:

* No legal advice
* No training on user documents
* No hidden ML behavior
* No silent transformer loading
* No jurisdiction overreach

Failures degrade gracefully.

---

## 14. Why This Architecture Matters

This system demonstrates:

* Production ML awareness
* Legal-domain sensitivity
* Explainable AI design
* Backend engineering maturity
* Responsible AI boundaries

LexBrief AI is designed to be **explained, defended, and extended** — not just executed.

---

## 15. Future Architectural Extensions

Planned extensions fit cleanly into this design:

* Async pipelines (Celery)
* GPU-backed summarization
* ML-assisted clause classification
* Jurisdiction expansion
* Contract comparison engines

No architectural rewrite is required.

---

## 16. Final Note

This architecture intentionally favors:

> **Clarity over cleverness**
> **Safety over scale**
> **Reasoning over raw output**

That tradeoff is what makes LexBrief AI a **serious system**, not a demo.

---
