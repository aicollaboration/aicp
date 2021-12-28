import typer
import os


def fetch_openapi():
    files = os.listdir(os.getcwd())

    if "openapi.yaml" in files:
        with open("openapi.yaml", "r") as file:
            return file.read()

    if "openapi.yml" in files:
        with open("openapi.yml", "r") as file:
            return file.read()

    if "openapi.json" in files:
        with open("openapi.json", "r") as file:
            return file.read()

    return None


app = typer.Typer()


@app.command('create')
def create_service(name: str):
    typer.echo(f"Create service: {name}")


@app.command('import')
def import_service():
    typer.echo(f"Import service")

    openapi = fetch_openapi()
    if openapi is None:
        typer.echo("No openapi file found")
        return

    typer.echo(openapi)
