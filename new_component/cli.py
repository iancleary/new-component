from pathlib import Path
from typing import Optional

import typer

from new_component._echos import _create_components_dir_echo, _create_new_component_echo
from new_component._jinja import _create_jinja_environment
from new_component._utils import _create_directory
from new_component._version import _version_callback

app = typer.Typer()

DEFAULT_COMPONENTS_DIR = "src/components/"
DEFAULT_FILE_EXTENSION = "js"  # jsx, ts, etc.
JINJA_ENVIRONMENT = _create_jinja_environment()


def _create_output(
    new_directory: Path,
    template_name: str,
    variables: dict,
    extension: str,
    filename: str = None,
) -> None:
    """
    Write new file to disk, within `new_directory`,
    by rendering the jinja template `template_name`
    """
    if filename is None:
        filename = template_name

    template = JINJA_ENVIRONMENT.get_template(f"{template_name}.js.j2")
    output = template.render(variables)

    with open(f"{new_directory}/{filename}.{extension}", "w") as f:
        f.write(output)


@app.command()
def main(
    name: str = typer.Argument(
        ...,  # Required to give name, as in `new-component ContactForm`
        help="Name of component to create.",
    ),
    directory: str = typer.Option(
        DEFAULT_COMPONENTS_DIR,
        "--directory",
        "-d",
        help="The directory in which to create the component.",
    ),
    extension: str = typer.Option(
        DEFAULT_FILE_EXTENSION,
        "--extension",
        "-e",
        help="The file extension for the created component files.",
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

    if components_directory.exists() is False:
        # Could set creation with a variable
        _create_directory(directory=components_directory)
        _create_components_dir_echo(components_directory=components_directory)

    new_component_directory = components_directory / name
    full_path_to_component_directory = Path.cwd() / new_component_directory

    # Allow user to abort if component already exists
    if full_path_to_component_directory.exists() is True:
        warning_message = (
            f"{name} component already exists in ./{components_directory}/."
        )
        styled_warning = typer.style(warning_message, typer.colors.YELLOW, bold=True)
        styled_component = typer.style(f"{name}", typer.colors.YELLOW, bold=True)
        confirm_message = (
            "Are you sure you want to overwrite your "
            + styled_component
            + " component?"
        )
        typer.echo(styled_warning)
        typer.confirm(confirm_message, abort=True)
    else:
        _create_directory(directory=full_path_to_component_directory)

    # Jinja Variables used in template render
    variables = {"ComponentName": name}

    # Render component files in your components directory
    _create_output(
        new_directory=full_path_to_component_directory,
        template_name="index",
        variables=variables,
        extension=extension,
    )
    _create_output(
        new_directory=full_path_to_component_directory,
        template_name="component",
        variables=variables,
        extension=extension,
        filename=f"{name}",
    )

    # Echo status to user
    _create_new_component_echo(
        component_name=name,
        full_path_to_component_directory=full_path_to_component_directory,
    )
