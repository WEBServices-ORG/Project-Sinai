#!/usr/bin/env python3

import typer
import subprocess
import sys
import webbrowser
import json
import urllib.request
import urllib.error
from sinai_core.api.sinai import Sinai

app = typer.Typer(help="Project Sinai CLI tool", add_completion=False)


@app.callback()
def main():
    pass


@app.command()
def server():
    """Start the Sinai server"""
    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "uvicorn",
                "sinai_server.app:app",
                "--reload",
                "--host",
                "0.0.0.0",
                "--port",
                "8000",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        typer.echo(f"Failed to start server: {e}")
        raise typer.Exit(1)


@app.command()
def desktop():
    """Launch the Sinai desktop app"""
    try:
        subprocess.run(
            ["open", "ui/web/dist-electron/mac-arm64/Sinai.app"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        typer.echo(f"Failed to launch desktop app: {e}")
        raise typer.Exit(1)


@app.command()
def webui():
    """Open the Sinai web UI in browser"""
    webbrowser.open("http://localhost:8000")


@app.command()
def ask(query: str, k: int = 5):
    """Query the Sinai AI"""
    sinai = Sinai()
    result = sinai.ask(query, k)
    for item in result:
        has_hebrew = any("\u0590" <= c <= "\u05ff" for c in item["answer"])
        label = "מקור:" if has_hebrew else "Source:"
        if has_hebrew:
            # Right align Hebrew text
            lines = item["answer"].split("\n")
            max_len = max(len(line) for line in lines) if lines else 0
            aligned_lines = [line.rjust(80) for line in lines]
            answer = "\n".join(aligned_lines)
        else:
            answer = item["answer"]
        typer.echo(f"Sinai AI Response:\n{answer}\n{label} {item['source']}")


@app.command()
def status():
    """Check Sinai core status"""
    sinai = Sinai()
    result = sinai.get_status()
    typer.echo(json.dumps(result, indent=2))


if __name__ == "__main__":
    app()
