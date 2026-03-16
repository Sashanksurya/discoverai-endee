"""
config/settings.py — Central configuration for DiscoverAI
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ── Endee Vector Database ─────────────────────────────────────────────────────
ENDEE_BASE_URL = os.getenv("ENDEE_BASE_URL", "http://localhost:8080/api/v1")
ENDEE_AUTH_TOKEN = os.getenv("ENDEE_AUTH_TOKEN", "")

# ── Groq ──────────────────────────────────────────────────────────────────────
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# ── Embedding Model ───────────────────────────────────────────────────────────
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_DIM = 384

# ── Endee Index Name ──────────────────────────────────────────────────────────
MOVIE_INDEX = "movies"

# ── Search Settings ───────────────────────────────────────────────────────────
DEFAULT_TOP_K = 5
MAX_TOP_K = 10
