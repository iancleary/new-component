from new_component import __version__, package_version


def test_package_version() -> None:
    """Test package version calculation."""
    [major, minor, patch] = package_version().split(".")
    assert isinstance(major, str)
    assert isinstance(minor, str)
    assert isinstance(patch, str)


def test_package_version_not_found() -> None:
    """Test package version calculation when package is not installed."""
    assert package_version(package="incorrect") == "Package not found."

