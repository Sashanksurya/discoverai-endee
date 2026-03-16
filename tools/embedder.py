"""
tools/embedder.py — Thin wrapper around sentence-transformers for generating
dense embeddings used by all Domain Agents before querying Endee.
"""

from __future__ import annotations
from typing import List
from sentence_transformers import SentenceTransformer
from config.settings import EMBEDDING_MODEL


class Embedder:
    """Singleton embedding model — loaded once, reused across agents."""

    _instance: "Embedder | None" = None

    def __new__(cls) -> "Embedder":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._model = SentenceTransformer(EMBEDDING_MODEL)
        return cls._instance

    def embed(self, text: str) -> List[float]:
        """Return a 384-dim embedding for a single string."""
        return self._model.encode(text, normalize_embeddings=True).tolist()

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Return embeddings for a batch of strings."""
        return self._model.encode(texts, normalize_embeddings=True).tolist()
