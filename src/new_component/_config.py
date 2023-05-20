import json

import typer

from new_component._constants import (
    DEFAULT_COMPONENTS_DIR,
    DEFAULT_FILE_EXTENSION,
    GLOBAL_CONFIG_FILE,
    LOCAL_CONFIG_FILE,
)


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

    # Merge directory config and parameter
    if directory is not None:
        config.update({"directory": directory})
    elif "directory" in config.keys():
        # directory configured via global or local config file
        pass
    else:
        # no config nor option specified, use default
        config.update({"directory": DEFAULT_COMPONENTS_DIR})

    # Merge directory config and parameter
    if extension is not None:
        config.update({"extension": extension})
    elif "extension" in config.keys():
        # extension configured via global or local config file
        pass
    else:
        # no config nor option specified, use default
        config.update({"extension": DEFAULT_FILE_EXTENSION})

    # DEBUG
    # with open("./.new-component-merged-config.json", "w") as outfile:
    #     json.dump(config, outfile, indent=4)

    return config


def _config_callback(value: bool) -> None:
    if value:
        file_config = _load_config()
        typer.echo(f"global_config: {GLOBAL_CONFIG_FILE}")
        if "global" in file_config.keys():
            global_config = file_config["global"]
            typer.echo(f"\t{global_config}")
        else:
            typer.echo("No global config file found.")

        typer.echo(f"local config: {LOCAL_CONFIG_FILE}")
        if "local" in file_config.keys():
            local_config = file_config["local"]
            typer.echo(f"\t{local_config}")
        else:
            typer.echo("No local config found.")

        merged_config = _merge_config(file_config)

        typer.echo("merged config:")
        typer.echo(f"\t{merged_config}")

        raise typer.Exit()
