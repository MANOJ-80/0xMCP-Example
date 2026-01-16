#!/usr/bin/env python3
"""
Setup script to configure Cursor IDE to use this MCP server.
"""
import json
import os
from pathlib import Path

def setup_cursor_config():
    """Configure Cursor IDE to use this MCP server."""
    # Path to Cursor config file
    cursor_config_path = Path.home() / ".cursor" / "mcp.json"
    
    # Get absolute path to main.py
    project_dir = Path(__file__).parent.absolute()
    main_py_path = project_dir / "main.py"
    
    # Check if main.py exists
    if not main_py_path.exists():
        print(f"❌ Error: {main_py_path} not found!")
        return False
    
    # Create .cursor directory if it doesn't exist
    cursor_config_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Read existing config or create new one
    if cursor_config_path.exists():
        try:
            with open(cursor_config_path, "r") as f:
                config = json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️  Warning: Invalid JSON in {cursor_config_path}, creating new config")
            config = {"mcpServers": {}}
    else:
        config = {"mcpServers": {}}
    
    # Ensure mcpServers key exists
    if "mcpServers" not in config:
        config["mcpServers"] = {}
    
    # Add or update the server configuration
    server_name = "AI Sticky Notes"
    config["mcpServers"][server_name] = {
        "command": "uv",
        "args": [
            "run",
            str(main_py_path)
        ],
        "cwd": str(project_dir)
    }
    
    # Write the configuration
    try:
        with open(cursor_config_path, "w") as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Cursor MCP configuration updated successfully!")
        print(f"   Config file: {cursor_config_path}")
        print(f"   Server name: {server_name}")
        print(f"   Command: uv run {main_py_path}")
        print(f"\n📝 Next steps:")
        print(f"   1. Restart Cursor IDE completely")
        print(f"   2. Your MCP server should appear in Cursor's MCP settings")
        print(f"   3. You can now use the tools: add_note, read_notes, and note_summary_prompt")
        return True
    except Exception as e:
        print(f"❌ Error writing config: {e}")
        return False

if __name__ == "__main__":
    setup_cursor_config()
