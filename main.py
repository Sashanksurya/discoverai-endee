"""
main.py — DiscoverAI Movie Agent Interactive Loop
"""

from __future__ import annotations
import sys

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from config.settings import GROQ_API_KEY
from agents.planner import PlannerAgent
from agents.movie_agent import MovieAgent
from agents.synthesizer import SynthesisAgent

console = Console()

WELCOME_BANNER = """
# 🎬 DiscoverAI — Agentic Movie Recommendation Engine

Powered by **Endee** vector database + **Groq (LLaMA 3.3)** AI

Ask me anything about movies! Examples:
- *"I want something thrilling with time travel, like Interstellar"*
- *"Dark psychological thrillers with great cinematography"*
- *"Movies about survival in extreme conditions"*
- *"Something mind-bending with a twist ending"*

Type **quit** or **exit** to leave.
"""


def process_query(user_query, planner, movie_agent, synthesizer):
    console.print("\n[dim]🧠 Planner Agent refining your query...[/dim]")
    plan = planner.plan(user_query)
    refined_query = plan.get("query", user_query)
    reasoning = plan.get("reasoning", "")
    console.print(f"   → Refined query: [italic]{refined_query}[/italic]")
    console.print(f"   → Reasoning: [dim]{reasoning}[/dim]")

    console.print("\n[dim]🔍 Movie Agent searching Endee vector database...[/dim]")
    results = movie_agent.search(refined_query, top_k=5)
    console.print(f"   → Found [bold]{len(results)}[/bold] candidate movies")

    console.print("\n[dim]✨ Synthesis Agent composing recommendations...[/dim]\n")
    response = synthesizer.synthesize(user_query, results)
    return response


def main():
    if not GROQ_API_KEY:
        console.print("[bold red]Error:[/bold red] GROQ_API_KEY not set in .env file.")
        sys.exit(1)

    console.print(Panel(Markdown(WELCOME_BANNER), border_style="blue"))

    planner = PlannerAgent()
    movie_agent = MovieAgent()
    synthesizer = SynthesisAgent()

    while True:
        try:
            console.print()
            user_input = console.input("[bold green]You:[/bold green] ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("quit", "exit", "q"):
                console.print("\n[dim]Goodbye! Enjoy your next watch. 🎬[/dim]\n")
                break

            response = process_query(user_input, planner, movie_agent, synthesizer)
            console.print(
                Panel(
                    Markdown(response),
                    title="[bold blue]DiscoverAI Recommendations[/bold blue]",
                    border_style="blue",
                    padding=(1, 2),
                )
            )
        except KeyboardInterrupt:
            console.print("\n\n[dim]Interrupted. Goodbye![/dim]\n")
            break
        except Exception as e:
            console.print(f"\n[bold red]Error:[/bold red] {e}\n")


if __name__ == "__main__":
    main()
