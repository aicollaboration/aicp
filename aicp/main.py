import typer
import aicp.service
import aicp.solution

app = typer.Typer()

@app.command()
def info():
    typer.echo(f"AICP: AICP")


app.add_typer(aicp.service.app, name="service")
app.add_typer(aicp.solution.app, name="solution")

if __name__ == "__main__":
    app()