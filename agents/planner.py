"""
agents/planner.py — Planner Agent using Groq (free tier)
"""

from __future__ import annotations
import json
from groq import Groq
from config.settings import GROQ_API_KEY

PLANNER_SYSTEM_PROMPT = """You are a Planner Agent in a movie recommendation system.

Your job is to analyse the user's request and rewrite it as a rich, descriptive
semantic search query that will be used to find similar movies via vector search.

Return a JSON object with this exact structure (no markdown fences, pure JSON):
{
  "query": "a rich descriptive query for the movie vector search",
  "reasoning": "Brief explanation of the themes/mood/genres you identified"
}

Rules:
- Expand the query with relevant themes, mood, setting, genre, tone, and narrative style
- Keep it descriptive and thematic — not just keywords
- Do NOT add genres or themes the user did not imply
"""


class PlannerAgent:
    def __init__(self) -> None:
        self._client = Groq(api_key=GROQ_API_KEY)

    def plan(self, user_query: str) -> dict:
        response = self._client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": PLANNER_SYSTEM_PROMPT},
                {"role": "user", "content": f"User request: {user_query}"},
            ],
            max_tokens=300,
        )
        raw = response.choices[0].message.content.strip()

        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        raw = raw.strip()

        return json.loads(raw)
