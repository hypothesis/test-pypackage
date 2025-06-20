from subprocess import run


def test_help():
    """Test the test-pypackage --help command."""
    run(["test-pypackage", "--help"], check=True)  # noqa: S607


def test_version():
    """Test the test-pypackage --version command."""
    run(["test-pypackage", "--version"], check=True)  # noqa: S607
