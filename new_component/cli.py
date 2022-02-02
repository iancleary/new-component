from pathlib import Path
from typing import Optional

import typer

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
        ...,  # Required to give name, as in `new-component ContactForm`
        help="Name of component to create.",
    ),
    directory: str = typer.Option(
        __COMPONENTS_DIR__,
        "--directory",
        "-d",
        help="The directory in which to create the component.",
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
    """
    Creates an new component directory in a React project,
    with opinionated defaults for styled-components.

    See https://styled-components.com/ for more information.
    """

    components_directory = Path(directory)
    new_directory = components_directory / name

    if new_directory.exists() is False:
        new_directory.mkdir(
            parents=True
        )  # Create directory, creating missing parent folders

    # index_file = new_directory / "index.js"

    new_directory_full_path = Path.cwd() / new_directory
    message_start = "Created a new "
    component = typer.style(name, fg=typer.colors.GREEN, bold=True)
    message_end = " Component 💅 🚀!"
    new_directory_path = typer.style(
        new_directory_full_path, fg=typer.colors.GREEN, bold=True
    )
    message = message_start + component + message_end
    typer.echo(message)
    typer.echo(new_directory_path)
