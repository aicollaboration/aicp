import json
import os

import typer

import aicp.service
import aicp.solution
from aicp.backend import load_config, write_config

app = typer.Typer()

@app.command()
def info():
    typer.echo(f"AICP: AICP")


@app.command()
def config():
    config = load_config()
    if not config:
        typer.echo("No config.json found in home directory")
        typer.echo("Please run 'aicp init' to create one")
        return
    typer.echo(f"AICP: AICP")
    typer.echo(f"Config: {config}")


@app.command()
def init():
    # ask for config url and secret
    config_url = typer.prompt("Config URL")
    secret = typer.prompt("Secret")
    username = typer.prompt("User")
    password = typer.prompt("Password")

    config_json_path = write_config(config_url, secret, username, password)
    
    typer.echo(f"Config created at {config_json_path}")


app.add_typer(aicp.service.app, name="service")
app.add_typer(aicp.solution.app, name="solution")

if __name__ == "__main__":
    app()
