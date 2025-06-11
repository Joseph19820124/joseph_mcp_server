# Example MCP Server using FastMCP

## Prerequisites
- uv
- python 3.12

## Install

After checking out the repo, run `uv venv` and `uv sync`

## How to run

### on Mac (replace folder name with the root of the repo)

`uv run --python /Users/chenjian/Documents/ai_projects/my_mcp_server/.venv/bin/python fastmcp run /Users/chenjian/Documents/ai_projects/my_mcp_server/main.py`

or

`uv run -p /Users/chenjian/Documents/ai_projects/my_mcp_server/.venv/bin/python fastmcp run /Users/chenjian/Documents/ai_projects/my_mcp_server/main.py`


## Adding this MCP on IDEs

- With `Claude Desktop` and `cursor`

```json
{
  "mcpServers": {
    "my_mcp_server": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--python",
        "/Users/chenjian/Documents/ai_projects/.venv/bin/python",
        "fastmcp",
        "run",
        "/Users/chenjian/Documents/ai_projects/my_mcp_server/main.py"
      ]
    }
  }
}
```

- With `Claude Code`

```sh
claude mcp add uv run --python /Users/chenjian/Documents/ai_projects/my_mcp_server/.venv/bin/python fastmcp run /Users/chenjian/Documents/ai_projects/my_mcp_server/main.py
```

or 

```sh
claude mcp add uv run -p /Users/chenjian/Documents/ai_projects/my_mcp_server/.venv/bin/python fastmcp run /Users/chenjian/Documents/ai_projects/my_mcp_server/main.py
```
