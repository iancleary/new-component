import importlib.metadata as importlib_metadata
import importlib.resources

# https://github.com/pdm-project/pdm/blob/cea09584c7e18f038b01a9ce0aabe18991c0d02b/src/pdm/compat.py

resources_read_text = importlib.resources.read_text


def read_version() -> str:
    try:
        return importlib_metadata.version(__package__ or "new_component")
    except importlib_metadata.PackageNotFoundError:
        return resources_read_text("new_component", "VERSION").strip()


__version__ = read_version()
