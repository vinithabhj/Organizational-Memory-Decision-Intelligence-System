# Organizational Memory & Decision Evolution Engine
RAG + Knowledge Graph + Multi-Agent System

---

## 📌 Overview

The **Organizational Memory & Decision Evolution Engine** is an AI system designed to capture, store, and reason over **organizational decisions**, not just documents.

Unlike traditional chatbots or basic RAG systems that retrieve text, this project focuses on **decision intelligence** — explaining *why* a decision was made, *what rationale supported it*, and *how confident the system is in the answer*.

The system combines **Retrieval-Augmented Generation (RAG)**, a **Knowledge Graph**, and a **Multi-Agent architecture** to build persistent and explainable organizational memory.

---

## ❓ Problem Statement

In real organizations:

- Important decisions are made during meetings and discussions
- The reasoning behind decisions is often lost over time
- New team members lack historical context
- Document search answers *what*, but not *why*

Traditional AI systems:
- Treat documents as plain text
- Lack long-term memory
- Provide answers without confidence or explanation

---

## 💡 Solution

This project solves the above problem by:

- Extracting **structured decisions** from unstructured organizational text
- Storing decisions as **persistent memory** in a Knowledge Graph (Neo4j)
- Using **Graph-Augmented RAG** for grounded retrieval
- Applying a **Multi-Agent system** for retrieval, reasoning, and verification
- Adding **confidence scoring** to reduce hallucinations

The result is an AI system that remembers decisions across sessions and explains its answers.

---

## 🏗️ System Architecture

```
User Query
   ↓
Agent Orchestrator
   ↓
Retriever Agent
   ├── Vector Database (semantic similarity)
   └── Knowledge Graph (decision memory)
   ↓
Reasoning Agent (LLM)
   ↓
Verifier Agent (grounding + confidence)
   ↓
Final Answer + Confidence
```

---

## 🤖 Multi-Agent Design

### 1️⃣ Decision Extraction Agent
- Processes raw organizational text (meeting notes, transcripts, documents)
- Extracts:
  - Decision
  - Rationale
  - Assumptions
  - Alternatives
- Runs before embedding to reduce noise

### 2️⃣ Retriever Agent
- Performs semantic search using vector embeddings
- Retrieves related decisions from Neo4j Knowledge Graph
- Combines vector-based and graph-based context

### 3️⃣ Reasoning Agent
- Uses an LLM to generate answers
- Works only on retrieved context
- Isolated from memory and retrieval logic

### 4️⃣ Verifier Agent
- Checks grounding between answer and context
- Computes a confidence score
- Provides safe fallback responses for low-confidence answers

### 5️⃣ Agent Orchestrator
- Controls execution order of all agents
- Acts as the single entry point for the application
- Ensures clean separation of responsibilities

---

## 🧠 Key Design Highlights

- **Decision-Aware RAG**  
  Embeds structured decision summaries instead of raw documents

- **Graph-Augmented Retrieval**  
  Combines semantic similarity with decision relationships

- **Persistent Organizational Memory**  
  Decisions stored in Neo4j Aura persist across sessions

- **Trust & Explainability**  
  Verifier agent provides confidence scores and explanations

- **Scalable by Design**  
  Supports automated ingestion from organizational tools

---

## 🛠️ Tech Stack

- Programming Language: Python
- LLM: OpenAI
- RAG Framework: LangChain + FAISS
- Knowledge Graph: Neo4j Aura
- Architecture: Multi-Agent System
- UI: Streamlit
- Configuration: dotenv

---

## 📂 Project Structure

```
org-memory-ai/
├── src/
│   ├── agents/
│   │   ├── decision_extractor.py
│   │   ├── reasoning_agent.py
│   │   └── agent_orchestrator.py
│   ├── rag/
│   │   ├── vector_store.py
│   │   └── retriever.py
│   ├── graph/
│   │   ├── neo4j_client.py
│   │   └── graph_builder.py
│   └── prompts/
├── data/
│   └── raw/
├── app.py
├── .env.example
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Create and activate virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Configure environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key
NEO4J_URI=neo4j+s://<your-id>.databases.neo4j.io
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
```

### 4️⃣ Run the application
```
streamlit run app.py
```

---

## 💬 Example Queries

- Why was microservices chosen?
- What rationale supported this decision?
- What assumptions influenced the architecture?
- How confident is the answer?

---

## 📊 What Makes This Project Different

| Feature | Typical RAG | This Project |
|-------|-------------|--------------|
| Decision awareness | No | Yes |
| Knowledge Graph memory | No | Yes |
| Multi-agent architecture | No | Yes |
| Confidence scoring | No | Yes |
| Explainable reasoning | No | Yes |

---

## 🎯 Use Cases

- Organizational knowledge management
- Architecture decision tracking
- Team onboarding
- Decision traceability
- Internal consulting and strategy analysis

---

## 📝 One-Line Summary

A decision-aware organizational memory system using RAG, knowledge graphs, and multi-agent orchestration to preserve and explain why decisions were made.
