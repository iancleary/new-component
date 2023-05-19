import importlib.metadata as importlib_metadata
import importlib.resources

import typer

from new_component import __app_name__


def read_version() -> str:
    # https://github.com/pdm-project/pdm/blob/cea09584c7e18f038b01a9ce0aabe18991c0d02b/src/pdm/compat.py
    resources_read_text = importlib.resources.read_text

    try:
        return importlib_metadata.version(__package__ or __app_name__)
    except importlib_metadata.PackageNotFoundError:
        return resources_read_text(__app_name__, "VERSION").strip()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{read_version()}")
        raise typer.Exit()
