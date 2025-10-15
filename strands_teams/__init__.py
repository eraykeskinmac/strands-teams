"""Microsoft Teams notifications tool for Strands Agents SDK.

This package provides a comprehensive Microsoft Teams integration for Strands agents,
enabling rich adaptive card notifications and messaging.

Example usage:
    ```python
    from strands import Agent
    from strands_teams import teams

    agent = Agent(tools=[teams])
    agent("send a Teams notification about new leads")
    ```
"""

from .teams import teams

__version__ = "0.1.0"
__all__ = ["teams"]

