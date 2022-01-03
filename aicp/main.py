import typer
import aicp.service
import aicp.solution
import supabase
import os
import json

# load json file from home directory
def load_config_json_from_home_dir():
    home_dir = os.path.expanduser("~")
    config_json_path = os.path.join(home_dir, ".aicp", "config.json")
    if os.path.exists(config_json_path):
        with open(config_json_path) as config_json_file:
            return json.load(config_json_file)
    return None

app = typer.Typer()

@app.command()
def info():
    typer.echo(f"AICP: AICP")


@app.command()
def config():
    config = load_config_json_from_home_dir()
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
    # create config.json
    home_dir = os.path.expanduser("~")
    config_json_path = os.path.join(home_dir, ".aicp", "config.json")

    if not os.path.exists(os.path.dirname(config_json_path)):
        os.makedirs(os.path.dirname(config_json_path))

    config_json = {
        "config_url": config_url,
        "secret": secret
    }
    with open(config_json_path, "w") as config_json_file:
        json.dump(config_json, config_json_file)
    typer.echo(f"Config created at {config_json_path}")


app.add_typer(aicp.service.app, name="service")
app.add_typer(aicp.solution.app, name="solution")

if __name__ == "__main__":
    app()