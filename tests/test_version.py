from new_component.__version__ import __version__


def test_package_version() -> None:
    """Test package version calculation."""
    [major, minor, patch] = __version__.split(".")
    assert isinstance(major, str)
    assert isinstance(minor, str)
    assert isinstance(patch, str)
