from pathlib import Path

import typer


def _create_new_component_echo(
    component_name: str, full_path_to_component_directory: Path
) -> None:
    """
    Echos the newly created component and directory.
    """

    message_start = "Created a new "
    component = typer.style(component_name, fg=typer.colors.GREEN, bold=True)
    message_end = " Component 💅 🚀!"
    new_directory_path = typer.style(
        full_path_to_component_directory, fg=typer.colors.GREEN, bold=True
    )
    message = message_start + component + message_end
    typer.echo(message)
    typer.echo(new_directory_path)


def _create_components_dir_echo(components_directory: Path) -> None:
    message = f"Warning: created the {components_directory} directory."
    styled_message = typer.style(message, fg=typer.colors.YELLOW, bold=True)
    typer.echo(styled_message)
