from pathlib import Path

import new_component

INSTALLED_LOCATION = new_component.__file__
TEMPLATES_DIR = INSTALLED_LOCATION.replace("__init__.py", "")
TEMPLATES_PATH = Path(TEMPLATES_DIR) / "templates"
