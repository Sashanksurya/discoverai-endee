"""
agents/synthesizer.py — Synthesis Agent using Groq (free tier)
"""

from __future__ import annotations
import json
from typing import Any, Dict, List

from groq import Groq
from config.settings import GROQ_API_KEY

SYNTHESIZER_SYSTEM_PROMPT = """You are a friendly and knowledgeable movie recommendation assistant.

You receive:
- The original user query
- A list of candidate movies from a semantic vector search, each with a similarity score and metadata

Your job is to write a warm, helpful recommendation response that:
1. Briefly acknowledges what the user is looking for (mood, theme, genre)
2. Presents each movie with 1-2 sentences explaining WHY it matches (reference themes, tone, director style)
3. Mentions stand-out details like the director, year, or a defining narrative element
4. Ends with a short friendly closing line

Format rules:
- Use the header "🎬 Movie Recommendations"
- List movies in order of relevance (highest similarity first)
- Keep it concise but insightful
- Use natural, conversational language
- Do NOT just repeat the description field; personalise the reasoning
"""


class SynthesisAgent:
    def __init__(self) -> None:
        self._client = Groq(api_key=GROQ_API_KEY)

    def synthesize(self, user_query: str, results: List[Dict[str, Any]]) -> str:
        context_lines = [f"User query: {user_query}\n", "--- MOVIE RESULTS ---"]
        for i, item in enumerate(results, 1):
            similarity_pct = int(item.get("similarity", 0) * 100)
            context_lines.append(
                f"{i}. [{similarity_pct}% match] {item.get('title', 'Unknown')}"
            )
            meta = {
                k: v
                for k, v in item.items()
                if k not in ("id", "similarity", "title")
            }
            context_lines.append(f"   Metadata: {json.dumps(meta)}")

        context = "\n".join(context_lines)

        response = self._client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYNTHESIZER_SYSTEM_PROMPT},
                {"role": "user", "content": context},
            ],
            max_tokens=800,
        )
        return response.choices[0].message.content.strip()
