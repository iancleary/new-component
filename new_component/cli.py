from pathlib import Path
from typing import Optional

import typer

import new_component
from new_component import __app_name__, __version__

app = typer.Typer()

__COMPONENTS_DIR__ = "src/components/"


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.command()
def main(
    name: str = typer.Argument(
        None,
        help="Name of component to create.",
        # callback=_create_component
    ),
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:

    components_directory = Path(__COMPONENTS_DIR__)

    new_directory = components_directory / name

    if new_directory.exists() is False:
        new_directory.mkdir(
            parents=True
        )  # Create directory, creating missing parent folders

    # index_file = new_directory / "index.js"

    print(new_component.__file__)
