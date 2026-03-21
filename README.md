# 🎬 DiscoverAI — Agentic Movie Recommendation Engine with Endee

> **An Agentic AI Workflow** that understands natural language queries and autonomously searches for semantic movie recommendations — powered by [Endee](https://github.com/endee-io/endee) as the vector database.

---

## 🧠 Project Overview & Problem Statement

Finding the right movie to watch is hard. Traditional keyword search fails to understand **mood, theme, and narrative style** — searching "dark thriller" returns everything tagged as thriller, not what actually *feels* dark and tense.

**DiscoverAI** solves this using **semantic vector search**. Instead of matching keywords, it converts both movie descriptions and user queries into dense numerical vectors and finds movies that are *semantically closest* — meaning they share similar themes, tone, and narrative style — even if they share no common words.

The system is built as a **multi-agent agentic workflow**:
- A **Planner Agent** interprets what the user *really* means
- A **Movie Agent** searches Endee's vector database semantically
- A **Synthesis Agent** explains *why* each movie matches

---

## 🏗️ System Design & Technical Approach

### Architecture

```
User Query
    │
    ▼
┌─────────────────────┐
│   Planner Agent     │  ← Uses Groq LLaMA 3.3 to refine query
└────────┬────────────┘
         │
         ▼
    Movie Agent           ← Embeds query → searches Endee
         │
    ┌────▼────────────┐
    │  Endee Vector   │  ← HNSW semantic similarity search
    │  Database       │     (cosine distance, INT8 precision)
    └─────────────────┘
         │
    ┌────▼────────────┐
    │ Synthesis Agent │  ← Uses Groq LLaMA 3.3 to write response
    └─────────────────┘
         │
    🎬 Movie Recommendations
```

### Key Features

- 🤖 **Agentic workflow** — 3 specialized agents working in a pipeline
- 🔍 **Semantic search** — Natural language mapped to 384-dim dense vectors
- ⚡ **Endee vector DB** — High-performance HNSW indexing, up to 1B vectors
- 🆓 **Fully free** — Groq free tier + Endee cloud free tier
- 🎬 **Rich metadata** — genre, director, rating, year stored alongside vectors
- 🐍 **Pure Python** — Simple setup, easy to extend

---

## 🔧 How Endee Is Used

Endee is the **core vector database** of this project. Here is exactly how it is integrated:

### 1. Index Creation
A single `movies` index is created in Endee cloud with these parameters:

| Index    | Dimension | Space  | Precision | Algorithm |
|----------|-----------|--------|-----------|-----------|
| `movies` | 384       | cosine | INT8      | HNSW      |

### 2. Data Ingestion (seed_data.py)
Each movie's description is converted into a 384-dimensional vector using `sentence-transformers/all-MiniLM-L6-v2` and upserted into Endee along with metadata:

```python
client.create_index(name="movies", dimension=384, space_type="cosine", precision=Precision.INT8)
index.upsert([{ "id": "mov_001", "vector": [...384 floats...], "meta": { "title": "Inception", ... } }])
```

### 3. Semantic Search (movie_agent.py)
At query time, the user's refined query is embedded and sent to Endee which returns the top-K most similar movies using HNSW approximate nearest neighbor search:

```python
vector = embedder.embed("psychological thriller with a twist ending")
results = index.query(vector=vector, top_k=5)
```

Endee returns results ranked by **cosine similarity** — movies whose semantic meaning is closest to the query.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- [Groq API key](https://console.groq.com) (free)
- [Endee cloud account](https://dapp.endee.io) (free)

### 1. Clone the Repository

```bash
git clone https://github.com/Sashanksurya/discoverai-endee.git
cd discoverai-endee
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your `.env` file

```bash
cp .env.example .env
```

Fill in your keys:
```
GROQ_API_KEY=your_groq_api_key_here
ENDEE_BASE_URL=https://your-cluster.endee.io/api/v1
ENDEE_AUTH_TOKEN=your_endee_auth_token_here
```

- **GROQ_API_KEY** → [console.groq.com](https://console.groq.com) → API Keys → Create Key
- **ENDEE_BASE_URL** → [dapp.endee.io](https://dapp.endee.io) → Your Project → Getting Started
- **ENDEE_AUTH_TOKEN** → [dapp.endee.io](https://dapp.endee.io) → Auth Tokens → Create Token

### 4. Seed the Vector Database

```bash
python seed_data.py
```

This creates the `movies` Endee index and loads 10 movies with embeddings.

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
discoverai-endee/
├── docker-compose.yml      # Endee local setup (alternative to cloud)
├── requirements.txt        # Python dependencies
├── main.py                 # Entry point — interactive agent loop
├── seed_data.py            # Loads movie data into Endee
├── .env.example            # Environment variable template
├── config/
│   └── settings.py         # Reads API keys from .env
├── agents/
│   ├── planner.py          # Planner Agent — refines user queries via Groq
│   ├── movie_agent.py      # Movie Agent — queries Endee vector database
│   └── synthesizer.py      # Synthesis Agent — writes recommendations via Groq
├── tools/
│   ├── endee_client.py     # Endee Python SDK wrapper
│   └── embedder.py         # Sentence-transformers embedding utility
└── data/
    └── sample_data.py      # 10 movies with descriptions and metadata
```

---

## 🤖 Agent Details

### Planner Agent (`agents/planner.py`)
- **Model**: Groq LLaMA 3.3 70B
- **Input**: Raw user query (e.g. *"dark thriller"*)
- **Output**: Rich semantic query (e.g. *"psychological thriller with complex morally ambiguous characters in a dark urban setting"*)

### Movie Agent (`agents/movie_agent.py`)
- **Embedding**: `all-MiniLM-L6-v2` (384 dimensions)
- **Search**: Endee HNSW cosine similarity, top-5 results
- **Output**: Ranked list of movies with similarity scores and metadata

### Synthesis Agent (`agents/synthesizer.py`)
- **Model**: Groq LLaMA 3.3 70B
- **Input**: User query + ranked movie results
- **Output**: Natural language recommendation explaining why each film matches

---

## 📦 Tech Stack

| Component | Technology |
|-----------|-----------|
| Vector Database | Endee Cloud (HNSW, cosine, INT8) |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| LLM | Groq — LLaMA 3.3 70B (free tier) |
| Language | Python 3.9+ |
| SDK | endee, groq, sentence-transformers |

---

## 🤝 Contributing

Pull requests are welcome! Ideas for extension:
- Add more movies to the dataset
- Add a Streamlit or Gradio web UI
- Implement user preference memory across sessions
- Add hybrid search (vector + keyword filters on genre/year)

---

## 📄 License

MIT License
