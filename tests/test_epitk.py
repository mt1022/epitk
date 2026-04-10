"""Tests for epitk package."""

import epitk


def test_version():
    """Package exposes a __version__ string."""
    assert isinstance(epitk.__version__, str)
    assert epitk.__version__ != ""


def test_version_format():
    """Version follows basic semver format (MAJOR.MINOR.PATCH)."""
    parts = epitk.__version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)
