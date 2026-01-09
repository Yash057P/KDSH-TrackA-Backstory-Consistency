# KDSH-TrackA-Backstory-Consistency

Evidence-based detection of character backstory consistency in long-form narratives.  
This project was developed for **Kharagpur Data Science Hackathon 2026 – Track A**.

---

## 📌 Problem Overview

Given:
- A character backstory (caption + content)
- The full novel text (100k+ words)

The task is to determine whether the backstory is:
- **Consistent (1)** or  
- **Contradictory / Unsupported (0)**  

with respect to the original narrative.

The system also produces a **short rationale** explaining the decision.

---

## 🧠 Approach Summary

The pipeline follows an **evidence-driven and explainable reasoning approach**:

                             Backstory
                                 ↓
                          Claim Extraction
                                 ↓
                   Chapter-level Evidence Retrieval
                                 ↓
                    Consistency Prediction (0 / 1)
                                 ↓
                      Human-readable Rationale


Key design principles:
- Long-context handling using chapter-based chunking
- Claim decomposition for interpretability
- Conservative, evidence-first prediction logic
- Reproducible execution using Docker

---

## 📂 Project Structure
```
.
├── src/
│   ├── ingest.py              # Dataset loading
│   ├── utils.py               # Novel loading utilities
│   ├── chunking.py            # Chapter-based text chunking
│   ├── claims.py              # Claim extraction from backstory
│   ├── retrieval.py           # Evidence retrieval + Pathway integration
│   ├── main.py                # Single-sample pipeline demo
│   └── generate_result.py     # Batch inference (creates results.csv)
│
├── data/
│   ├── test.csv
│   └── novels/
│       ├── The Count of Monte Cristo.txt
│       └── In search of the castaways.txt
│
├── results.csv                # Final predictions with rationale
└── README.md
```

---

## 🔧 Reproducibility & Environment

This project uses **Pathway**, which requires a Linux-based environment with
specific Python compatibility.

To ensure reproducibility across systems, all experiments are executed inside
the **official Pathway Docker container**.

---

## ▶️ How to Run (Docker Required)

### 1. Install Docker
Ensure Docker Desktop is installed and running.

### 2. Run the container
From the project root directory:

```bash
docker run -it --rm -v "$(pwd):/app" -w /app pathwaycom/pathway:latest bash
```

## Generate Results
Inside Container:
```bash
python src/generate_result.py
```
This will generate:
results.csv

containing:
- id
- prediction (0 / 1)
- rationale

--- 

## 📊 Output Format
Example row from 'results.csv:'
```bash
id,prediction,rationale
95,1,"Claim supported by narrative evidence from Chapter 1..."
```

--- 
## ⚠️ Limitations

- The current system is conservative and may over-predict consistency.
- Subtle temporal or causal contradictions are not explicitly modeled.
- Retrieval relies on lexical overlap rather than deep semantic inference.

---

## 🚀 Future Improvements

- Temporal reasoning for date and event order validation
- Explicit contradiction and negation detection
- Aggregation over multiple claims and evidence passages

