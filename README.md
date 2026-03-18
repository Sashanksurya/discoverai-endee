# 🎬 DiscoverAI — Agentic Movie Recommendation Engine with Endee

> **An Agentic AI Workflow** that understands natural language queries and autonomously searches for semantic movie recommendations — powered by [Endee](https://github.com/endee-io/endee) as the vector database.

---

## 🧠 Project Overview

DiscoverAI is a multi-agent AI system where a **Planner Agent** interprets the user's natural language request and refines it into an optimised semantic query, which a **Movie Agent** uses to search Endee, before a **Synthesis Agent** composes a natural-language recommendation response.

### Architecture

```
User Query
    │
    ▼
┌─────────────────────┐
│   Planner Agent     │  ← Interprets intent, refines search query
└────────┬────────────┘
         │
         ▼
    Movie Agent           ← Queries Endee with refined sub-query
         │
    ┌────▼────────────┐
    │  Endee Vector   │  ← Semantic similarity search (HNSW index)
    │  Database       │
    └─────────────────┘
         │
    ┌────▼────────────┐
    │ Synthesis Agent │  ← Generates final natural-language response
    └─────────────────┘
         │
    Movie Recommendations
```

### Key Features

- 🤖 **Agentic workflow** — Planner Agent interprets intent and refines the search query
- 🔍 **Semantic search** — Natural language queries mapped to dense embeddings
- ⚡ **Endee vector DB** — High-performance HNSW indexing, up to 1B vectors
- 🎬 **Movie-focused** — Rich metadata: genre, director, rating, year
- 🐍 **Pure Python** — Simple setup, easy to extend

---

## 🚀 Quick Start

### 1. Start Endee (Docker)

```bash
docker compose up -d
```

Endee will be available at `http://localhost:8080`.

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Your API Key

```bash
export  _API_KEY=your_key_here
```

### 4. Seed the Vector Database

```bash
python seed_data.py
```

This creates the `movies` Endee index and loads sample data with embeddings.

### 5. Run the Agent

```bash
python main.py
```

---

## 💬 Example Queries

```
You: I want something thrilling with time travel, like Interstellar.

You: Show me dark psychological thrillers.

You: Find me movies about survival in the wild.

You: Something with a mind-bending plot and great cinematography.
```

---

## 📁 Project Structure

```
endee-agent/
├── docker-compose.yml      # Endee vector database
├── requirements.txt        # Python dependencies
├── main.py                 # Entry point — interactive agent loop
├── seed_data.py            # Loads movie data into Endee
├── config/
│   └── settings.py         # Configuration (Endee URL, model, etc.)
├── agents/
│   ├── planner.py          # Planner Agent — refines user queries
│   ├── movie_agent.py      # Movie Agent — queries Endee
│   └── synthesizer.py      # Synthesis Agent — final response generation
├── tools/
│   ├── endee_client.py     # Endee vector DB wrapper
│   └── embedder.py         # Text embedding utility
└── data/
    └── sample_data.py      # Sample movie dataset
```

---

## 🏗️ How It Works

### Step 1 — Planner Agent
Receives the user query and uses  to:
- Understand the mood, genre, themes, and intent
- Rewrite it as a rich descriptive query optimised for vector search

### Step 2 — Movie Agent
1. Takes the refined sub-query from the Planner
2. Generates a dense 384-dim embedding via `sentence-transformers`
3. Queries Endee's HNSW index for the top-K most similar movies
4. Returns structured results with full metadata

### Step 3 — Synthesis Agent
Receives the results and uses AI Agent to:
- Rank and present the most relevant movies
- Write a natural language recommendation explaining *why* each film matches
- Add director/genre context for discovery

---

## 🔧 Endee Integration

One index is created:

| Index    | Dimension | Space  | Precision |
|----------|-----------|--------|-----------|
| `movies` | 384       | cosine | INT8      |

Each movie stored includes:
- `id` — unique identifier
- `vector` — 384-dim embedding from `all-MiniLM-L6-v2`
- `meta` — title, director, genre, rating, year, description

---

## 📦 Requirements

- Docker & Docker Compose (for Endee)
- Python 3.9+
- API key (for AI Agent)

---

## 🤝 Contributing

Pull requests are welcome! Ideas for extension:
- Add more movies to the dataset
- Add a Streamlit or Gradio web UI
- Implement user preference memory across sessions
- Add hybrid search (vector + keyword filters on genre/year)

---

## 📄 License

MIT License — see [LICENSE](LICENSE)
