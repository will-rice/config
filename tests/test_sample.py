"""Tests for the config package."""

import subprocess
import sys


def test_main_prints_hello_world() -> None:
    """The package entry point prints the expected greeting."""
    result = subprocess.run(
        [sys.executable, "-c", "from config.main import main; main()"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout == "Hello, World!\n"
