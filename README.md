# strands-teams

[![PyPI version](https://img.shields.io/pypi/v/strands-teams.svg)](https://pypi.org/project/strands-teams/)
[![Python Support](https://img.shields.io/pypi/pyversions/strands-teams.svg)](https://pypi.org/project/strands-teams/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Microsoft Teams notifications tool for [Strands Agents SDK](https://github.com/strands-agents/strands). Enables powerful adaptive card notifications and rich messaging for AI agents.

## Features

- **Adaptive Cards**: Rich, interactive message cards
- **Pre-built Templates**: Notifications, approvals, status updates
- **Custom Cards**: Full adaptive card schema support
- **Action Buttons**: Add interactive elements to messages
- **Rich Formatting**: Markdown support, images, and media
- **Type Safe**: Full type hints and validation
- **Easy Integration**: Drop-in tool for Strands agents

## Requirements

- Python 3.9+
- Strands Agents SDK 1.11.0+
- Microsoft Teams webhook URL

## Installation

```bash
pip install strands-teams
```

## Quick Start

```python
from strands import Agent
from strands_teams import teams

# Create an agent with Teams tool
agent = Agent(tools=[teams])

# Simple notification
agent("send a Teams message: New lead from Acme Corp")

# Use pre-built templates
agent("send an approval request to Teams for the Q4 budget")

# Status updates
agent("send a status update to Teams: website redesign is 75% complete")
```

## Configuration

Set your Teams webhook URL as an environment variable:

```bash
TEAMS_WEBHOOK_URL=your_webhook_url  # Optional - can be provided per call
```

**Setup webhook:** Teams Channel → Connectors → Incoming Webhook

## Supported Templates

### Notification Template

```python
agent("send a notification to Teams about new sales leads")
```

**Features:**

- Color-coded cards (default, good, attention, warning, accent)
- Title and message content
- Markdown formatting support

### Approval Template

```python
agent("send an approval request to Teams for budget approval")
```

**Features:**

- Attention-grabbing style
- Approve and Reject action buttons
- Detailed description section

### Status Update Template

```python
agent("send a status update to Teams: project is 75% complete")
```

**Features:**

- Project and status information
- Color-coded by status
- Status emojis (✅, 🔄, ⏸️, 🚫, ❌)

### Simple Message

```python
agent("send a simple message to Teams: Meeting in 15 minutes")
```

**Features:**

- Basic title and message
- Clean formatting
- Quick notifications

## Custom Adaptive Cards

You can send fully custom adaptive cards:

```python
from strands import Agent
from strands_teams import teams

agent = Agent(tools=[teams])

agent("""
Send this custom Teams card:
{
    "type": "AdaptiveCard",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "text": "Custom Card",
            "weight": "Bolder",
            "size": "Large"
        }
    ]
}
""")
```

For more information on adaptive cards, see: [adaptivecards.io](https://adaptivecards.io/)

## Testing

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- **PyPI**: [pypi.org/project/strands-teams](https://pypi.org/project/strands-teams/)
- **GitHub**: [github.com/eraykeskinmac/strands-teams](https://github.com/eraykeskinmac/strands-teams)
- **Strands Agents SDK**: [github.com/strands-agents/strands](https://github.com/strands-agents/strands)
- **Adaptive Cards**: [adaptivecards.io](https://adaptivecards.io/)

---

**Built for the Strands community** 🚀
