"""Basic tests for strands-teams package."""

import pytest


def test_import():
    """Test that the package can be imported."""
    from strands_teams import teams

    assert teams is not None


def test_version():
    """Test that version is defined."""
    import strands_teams

    assert hasattr(strands_teams, "__version__")
    assert strands_teams.__version__ == "0.1.0"


def test_tool_has_required_attributes():
    """Test that teams tool has required attributes."""
    from strands_teams import teams

    # Check that it's a tool with a name
    assert hasattr(teams, "name")
    assert isinstance(teams.name, str)
    assert len(teams.name) > 0


def test_templates_import():
    """Test that templates can be imported."""
    from strands_teams.templates import teams_templates

    assert hasattr(teams_templates, "notification")
    assert hasattr(teams_templates, "approval_card")
    assert hasattr(teams_templates, "status_update")
    assert hasattr(teams_templates, "simple_message")

