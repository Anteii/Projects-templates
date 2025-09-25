import logging

import typer
from {{cookiecutter.package_name}}.logging_config import configure_logging

from {{cookiecutter.package_name}}.__version__ import __version__


app = typer.Typer()
logger = logging.getLogger(__name__)


@app.callback()
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
    debug: bool = typer.Option(False, "--debug", help="Enable debug logging (very verbose)"),
):

    log_level = logging.DEBUG if debug else (logging.INFO if verbose else logging.WARNING)
    configure_logging(log_level)
    
    # Store the verbosity in the Typer context if needed for subcommands
    ctx.obj = {"VERBOSE": verbose, "DEBUG": debug}

@app.command()
def version(ctx: typer.Context):
    logger.info(f"Called {ctx.command.name}")
    
    typer.echo(f"{{cookiecutter.project_name}} version is {__version__}")

@app.command()
def hello(ctx: typer.Context, name: str = "World"):
    logger.info(f"Called {ctx.command.name}")
    
    typer.echo(f"Hello, {name}!")

if __name__ == "__main__":
    app()