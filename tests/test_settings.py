import pytest
import typer
from new_component._config import _config_callback


def test_settings_output() -> None:
    """Test settings output."""
    with pytest.raises(typer.Exit):
        _config_callback(value=True)
