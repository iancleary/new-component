import json

from new_component._constants import GLOBAL_CONFIG_FILE, LOCAL_CONFIG_FILE


def _load_config() -> dict:
    """
    Loads config from global and local scopes, if they exist.
    """
    file_config = {}

    if LOCAL_CONFIG_FILE.exists():
        f = open(LOCAL_CONFIG_FILE)
        file_config["local"] = json.load(f)
        f.close()

    if GLOBAL_CONFIG_FILE.exists():
        f = open(GLOBAL_CONFIG_FILE)
        file_config["global"] = json.load(f)
        f.close()

    return file_config


def _merge_config(
    file_config: dict, directory: str = None, extension: str = None
) -> dict:
    """
    Merge config values, with command-line values overwriting local values,
    and local values overwriting global ones.
    """

    config = {}

    # This should confirm keys match API
    if "global" in file_config.keys():
        config.update(file_config["global"])

    # This should confirm keys match API
    if "local" in file_config.keys():
        config.update(file_config["local"])

    if directory is not None:
        config.update({"directory": directory})

    if extension is not None:
        config.update({"extension": extension})

    return config
