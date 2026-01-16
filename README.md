# 🗒️ AI Sticky Notes - MCP Server Example

A simple MCP (Model Context Protocol) server example that adds sticky notes functionality to your AI assistant.

## Features

- **Add Notes** - Save notes that persist across sessions
- **Read Notes** - Retrieve all saved notes
- **Latest Note** - Quick access to the most recent note
- **Summary Prompt** - Ask AI to summarize your notes

## Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

```bash
# Clone the repo
git clone https://github.com/MANOJ-80/0xMCP-Example.git
cd 0xMCP-Example

# Install dependencies
uv sync
```

### Configure with Cursor IDE

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "AI Sticky Notes": {
      "command": "/path/to/project/.venv/bin/python",
      "args": ["/path/to/project/main.py"],
      "cwd": "/path/to/project"
    }
  }
}
```

> 💡 Replace `/path/to/project` with your actual project path

**Restart Cursor** after saving the config.

## MCP Tools

| Tool                    | Description                     |
| ----------------------- | ------------------------------- |
| `add_note(message)`     | Add a new sticky note           |
| `read_notes()`          | Read all saved notes            |
| `note_summary_prompt()` | Get a prompt to summarize notes |

## Resources

| Resource    | URI              | Description              |
| ----------- | ---------------- | ------------------------ |
| Latest Note | `notes://latest` | Get the most recent note |

## License

MIT
