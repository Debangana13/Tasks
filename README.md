# NLP Chatbot Suite — NullClass Data Science Internship

> Apr 2025 – Jun 2025 · NullClass Edtech Pvt. Ltd.

![accuracy](https://img.shields.io/badge/Summarization_Accuracy-87%25-1D9E75?style=flat-square) ![retrieval](https://img.shields.io/badge/Query_Retrieval-90%25-1D9E75?style=flat-square) ![Python](https://img.shields.io/badge/Python-blue?style=flat-square) ![TensorFlow](https://img.shields.io/badge/TensorFlow-orange?style=flat-square) ![FAISS](https://img.shields.io/badge/FAISS-purple?style=flat-square) ![LangChain](https://img.shields.io/badge/LangChain-teal?style=flat-square)

---

## Overview

Two NLP systems built end-to-end during a 2-month Data Science internship focused on real-world chatbot architecture, dynamic knowledge management, and interface development.

---

## Project 1 — Extractive Summarization Chatbot

### What it does
Takes long-form text input and extracts the most important sentences to produce a concise summary. Built with traditional NLP + a TensorFlow classification model.

### How it works
1. Text preprocessing — tokenization, stopword removal, lemmatization (NLTK)
2. Feature extraction — Bag of Words representation
3. Sentence scoring — TensorFlow model ranks sentences by importance
4. GUI — Tkinter desktop interface for input/output

### Results
**87% summarization accuracy** on held-out test data

### Stack
`Python` `TensorFlow` `NLTK` `Bag of Words` `Tkinter`

---

## Project 2 — Self-Updating Knowledge Chatbot

### What it does
A Q&A chatbot that can ingest new documents and update its knowledge base dynamically — no retraining required. Uses vector search for retrieval and basic entity recognition to keep responses grounded.

### How it works
1. Document ingestion — XML/CSV files parsed and chunked
2. Vector indexing — FAISS stores and retrieves embeddings
3. Dynamic updates — new documents added to the index at runtime via LangChain
4. Entity recognition — basic NER to improve response grounding
5. UI — Streamlit interface for chat interaction

### Results
**90% correct response retrieval** on unseen queries

### Stack
`Python` `FAISS` `LangChain` `NLTK` `Streamlit`

---

## Repo Structure

```
Tasks/
├── task1/
│   ├── SummaryTask1.ipynb     # Extractive summarization model (TF + BoW)
│   └── requirements.txt
├── taskno3/
│   ├── app.py                 # Streamlit UI
│   ├── gui.py                 # Tkinter interface
│   ├── intentsMed.json        # Knowledge base / intents data
│   ├── requirement.txt
│   └── updateknowledge.py     # Dynamic FAISS knowledge base updates
└── README.md
```

> Update folder names above to match your actual structure

---

## Run locally

```bash
git clone https://github.com/Debangana13/Tasks
cd Tasks

# Project 1 — Summarization
pip install -r task1/requirements.txt
jupyter notebook task1/SummaryTask1.ipynb

# Project 2 — Self-updating chatbot
pip install -r taskno3/requirement.txt
streamlit run taskno3/app.py
```

---

*Part of NullClass Edtech Pvt. Ltd. Data Science Internship · Certificate issued Jun 2025*  
*Built by [Debangana Ghosh](https://linkedin.com/in/debanganaghosh2702)*
