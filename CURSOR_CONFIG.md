# Cursor MCP Configuration Guide

## Manual Configuration Steps

### 1. Open or create the config file
```bash
# Create the directory if it doesn't exist
mkdir -p ~/.cursor

# Edit the config file
nano ~/.cursor/mcp.json
# or
code ~/.cursor/mcp.json
```

### 2. Add this configuration to `~/.cursor/mcp.json`:

**Option A: Using full path to uv (Recommended if you want to use uv):**

```json
{
  "mcpServers": {
    "AI Sticky Notes": {
      "command": "/home/itachi/.local/bin/uv",
      "args": [
        "run",
        "/home/itachi/2_Projects/example-mcp-server/main.py"
      ],
      "cwd": "/home/itachi/2_Projects/example-mcp-server"
    }
  }
}
```

**Option B: Using virtual environment Python (Recommended - ensures dependencies are available):**

```json
{
  "mcpServers": {
    "AI Sticky Notes": {
      "command": "/home/itachi/2_Projects/example-mcp-server/.venv/bin/python",
      "args": [
        "/home/itachi/2_Projects/example-mcp-server/main.py"
      ],
      "cwd": "/home/itachi/2_Projects/example-mcp-server"
    }
  }
}
```

### 3. If you already have other MCP servers configured:

Just add the `"AI Sticky Notes"` entry to your existing `mcpServers` object:

```json
{
  "mcpServers": {
    "Existing Server": {
      ...
    },
    "AI Sticky Notes": {
      "command": "/home/itachi/.local/bin/uv",
      "args": [
        "run",
        "/home/itachi/2_Projects/example-mcp-server/main.py"
      ],
      "cwd": "/home/itachi/2_Projects/example-mcp-server"
    }
  }
}
```

### 4. Configuration Fields Explained:

- **`command`**: The command to run (`uv` in your case)
- **`args`**: Arguments passed to the command
  - `"run"` - tells uv to run
  - The absolute path to your `main.py` file
- **`cwd`**: Working directory (optional but recommended)

### 5. After saving:

1. **Restart Cursor completely** (quit and reopen)
2. Your MCP server should appear in Cursor's MCP settings
3. You can now use the tools: `add_note`, `read_notes`, and `note_summary_prompt`

### Alternative: Using Python directly

If `uv` is not in your PATH, you can use Python directly:

```json
{
  "mcpServers": {
    "AI Sticky Notes": {
      "command": "python3",
      "args": [
        "/home/itachi/2_Projects/example-mcp-server/main.py"
      ],
      "cwd": "/home/itachi/2_Projects/example-mcp-server"
    }
  }
}
```

Or if you want to use the virtual environment's Python:

```json
{
  "mcpServers": {
    "AI Sticky Notes": {
      "command": "/home/itachi/2_Projects/example-mcp-server/.venv/bin/python",
      "args": [
        "/home/itachi/2_Projects/example-mcp-server/main.py"
      ],
      "cwd": "/home/itachi/2_Projects/example-mcp-server"
    }
  }
}
```
