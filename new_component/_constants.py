from pathlib import Path

import new_component

DEFAULT_COMPONENTS_DIR = "src/components/"
DEFAULT_FILE_EXTENSION = "js"  # jsx, ts, etc.

INSTALLED_LOCATION = new_component.__file__
TEMPLATES_DIR = INSTALLED_LOCATION.replace("__init__.py", "")
TEMPLATES_PATH = Path(TEMPLATES_DIR) / "templates"

CONFIG_FILE = ".new-component.json"
LOCAL_CONFIG_FILE = Path(f"./{CONFIG_FILE}")

GLOBAL_CONFIG_FILE = Path("~/.config/new-component/settings.json")
