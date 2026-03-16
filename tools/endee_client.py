"""
tools/endee_client.py — Wrapper around the Endee Python SDK.
"""

from __future__ import annotations
from typing import Any, Dict, List

from endee import Endee, Precision
from config.settings import (
    ENDEE_BASE_URL,
    ENDEE_AUTH_TOKEN,
    EMBEDDING_DIM,
    DEFAULT_TOP_K,
)


class EndeeClient:
    def __init__(self) -> None:
        token = ENDEE_AUTH_TOKEN or None
        self._client = Endee(token) if token else Endee()
        self._client.set_base_url(ENDEE_BASE_URL)
        self._index_cache: Dict[str, Any] = {}

    def ensure_index(self, name: str) -> None:
        raw = self._client.list_indexes()
        existing = []
        for idx in raw:
            if isinstance(idx, dict):
                existing.append(idx.get("name", ""))
            else:
                existing.append(getattr(idx, "name", ""))

        if name not in existing:
            self._client.create_index(
                name=name,
                dimension=EMBEDDING_DIM,
                space_type="cosine",
                precision=Precision.INT8,
            )
            print(f"[Endee] Created index '{name}'")
        else:
            print(f"[Endee] Index '{name}' already exists — skipping creation")

    def _get_index(self, name: str):
        if name not in self._index_cache:
            self._index_cache[name] = self._client.get_index(name=name)
        return self._index_cache[name]

    def upsert(self, index_name: str, items: List[Dict[str, Any]]) -> None:
        index = self._get_index(index_name)
        index.upsert(items)

    def query(
        self,
        index_name: str,
        vector: List[float],
        top_k: int = DEFAULT_TOP_K,
    ) -> List[Dict[str, Any]]:
        index = self._get_index(index_name)
        raw_results = index.query(vector=vector, top_k=top_k)

        results = []
        for r in raw_results:
            # Print type for debugging
            print(f"[DEBUG] result type: {type(r)}, value: {r}")
            try:
                if isinstance(r, dict):
                    results.append({
                        "id": r.get("id", ""),
                        "similarity": round(float(r.get("similarity", 0)), 4),
                        "meta": r.get("meta") or {},
                    })
                else:
                    results.append({
                        "id": getattr(r, "id", str(r)),
                        "similarity": round(float(getattr(r, "similarity", 0)), 4),
                        "meta": getattr(r, "meta", None) or {},
                    })
            except Exception as e:
                print(f"[DEBUG] error parsing result: {e}, raw: {r}")
        return results
