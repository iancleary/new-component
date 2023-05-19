from new_component._version import read_version


def test_package_version() -> None:
    """Test package version calculation."""
    # will be like either
    # "0.1.0" # installed from pypi
    # or
    # v0.1.dev22+gb22a45f.d20230519 # installed from source
    version = read_version()
    assert isinstance(version, str)
