"""
agents/movie_agent.py — Movie Domain Agent
"""

from __future__ import annotations
from typing import Any, Dict, List

from tools.embedder import Embedder
from tools.endee_client import EndeeClient
from config.settings import DEFAULT_TOP_K, MOVIE_INDEX


class MovieAgent:
    def __init__(self) -> None:
        self._embedder = Embedder()
        self._endee = EndeeClient()

    def search(self, query: str, top_k: int = DEFAULT_TOP_K) -> List[Dict[str, Any]]:
        vector = self._embedder.embed(query)
        index = self._endee._get_index(MOVIE_INDEX)
        raw_results = index.query(vector=vector, top_k=top_k)

        results = []
        for r in raw_results:
            print(f"[DEBUG] type={type(r)} val={r}")
            if isinstance(r, dict):
                results.append({
                    "id": r.get("id", ""),
                    "similarity": round(float(r.get("similarity", 0)), 4),
                    **( r.get("meta") or {} ),
                })
            else:
                results.append({
                    "id": getattr(r, "id", ""),
                    "similarity": round(float(getattr(r, "similarity", 0)), 4),
                    **( getattr(r, "meta", None) or {} ),
                })
        return results
