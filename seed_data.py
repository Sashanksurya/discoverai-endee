"""
seed_data.py — Seeds the Endee 'movies' index with sample data.

Run once before using the agent:
    python seed_data.py

This script:
  1. Ensures the 'movies' index exists in Endee
  2. Embeds each movie's `embed_text` using sentence-transformers
  3. Upserts all movies with their metadata into Endee
"""

from __future__ import annotations
import sys
from rich.console import Console
from rich.progress import track

from config.settings import MOVIE_INDEX
from data.sample_data import MOVIES
from tools.embedder import Embedder
from tools.endee_client import EndeeClient

console = Console()


def main() -> None:
    console.rule("[bold blue]DiscoverAI — Endee Movie Index Seeder[/bold blue]")

    embedder = Embedder()
    client = EndeeClient()

    console.print(f"\n[bold cyan]Seeding index:[/bold cyan] [yellow]{MOVIE_INDEX}[/yellow]")
    client.ensure_index(MOVIE_INDEX)

    payload = []
    for movie in track(MOVIES, description="  Embedding movies..."):
        vector = embedder.embed(movie["embed_text"])
        payload.append(
            {
                "id": movie["id"],
                "vector": vector,
                "meta": movie["meta"],
            }
        )

    client.upsert(MOVIE_INDEX, payload)
    console.print(f"  ✅ Upserted [bold]{len(payload)}[/bold] movies into '{MOVIE_INDEX}'")

    console.rule()
    console.print(
        "\n[bold green]✨ Movie index seeded successfully![/bold green]\n"
        "You can now run [bold]python main.py[/bold] to start the agent.\n"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}")
        console.print(
            "\n[dim]Make sure Endee is running:[/dim] [cyan]docker compose up -d[/cyan]"
        )
        sys.exit(1)
