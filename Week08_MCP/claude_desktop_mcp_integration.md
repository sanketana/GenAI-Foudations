# 🧩 Claude Desktop + MCP Server Integration Guide

This guide explains how to integrate **local MCP servers** with **Claude Desktop** using `claude_desktop_config.json`.

It covers:

- When to **let Claude start the server** vs when to run it **manually**
- The difference between **STDIO** and **HTTP** transports
- The structure of the **config JSON entry**
- Practical examples (including `uv`, FastMCP, and Node-based servers)
- Common pitfalls and troubleshooting tips

---

## 1. Big Picture: How Claude Talks to MCP Servers

Claude Desktop can talk to local MCP servers in two main ways:

1. **STDIO transport**  
   - Claude launches the server as a child process.
   - MCP messages flow over **stdin / stdout**.
   - Managed via `claude_desktop_config.json` → `mcpServers` section.
   - ✅ Recommended for **Claude Desktop**.

2. **HTTP transport**  
   - Server exposes an MCP endpoint over HTTP (e.g. `http://localhost:8000/mcp`).
   - You typically start this server **manually** or via a script.
   - More common for **remote clients / editors / MCP CLI**, not Desktop.

For **Claude Desktop**, the smoothest experience is:

> **Use STDIO and let Claude start the server.**

---

## 2. Don’t Run the Server Manually (for STDIO)

When you configure a server in `claude_desktop_config.json`, Claude will:

1. Read your configuration.
2. Launch the MCP server as a subprocess.
3. Speak MCP over STDIO.
4. Restart it if it crashes.

So:

- ❌ You do **not** run `uv run ...` or `python server.py` manually.
- ✅ Claude Desktop will run the command you specify in `mcpServers`.

Manual runs are only needed when:
- You are testing an **HTTP-based** server, or
- You are using **MCP CLI / editors / other clients** instead of Desktop.

---

## 3. STDIO vs HTTP Transport

### 3.1 STDIO (Recommended for Claude Desktop)

Typical Python FastMCP server:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo", json_response=True)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()  # Defaults to transport="stdio"
```

Key points:

- **No** `transport=` argument → default is `stdio`.
- Claude starts this program and talks MCP over stdin/stdout.
- You configure it in `claude_desktop_config.json` (see below).

### 3.2 HTTP Transport (for other clients)

If you instead run:

```python
mcp.run(transport="http", host="127.0.0.1", port=8000)
```

Then:

- The server exposes an HTTP endpoint (usually `/mcp`).
- You must run it yourself, e.g.:

  ```bash
  uv run --with mcp fastmcp_quickstart.py
  ```

- Claude Desktop will **not** automatically discover HTTP servers from config alone.  
  (They are more suitable for MCP CLI, editors, or remote setups.)

---

## 4. `claude_desktop_config.json` Structure

On macOS, the config is usually located at:

```text
~/Library/Application Support/Claude/claude_desktop_config.json
```

Minimal structure:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "executable-or-absolute-path",
      "args": ["arg1", "arg2", "..."],
      "env": {
        "OPTIONAL_ENV_VAR": "value"
      }
    }
  }
}
```

### Fields

- **`mcpServers`**  
  A map of server names → launch configuration.

- **Server name (e.g. `"fastmcp-demo"`):**  
  A friendly identifier that will appear in Claude Desktop.

- **`command`**  
  The executable to run (`python3`, full path to `uv`, `npx`, `node`, etc.).  
  ⚠️ On macOS, GUI apps don’t always get your shell `$PATH`, so using an **absolute path** is safest.

- **`args`**  
  An array of arguments passed to `command`.  
  This is exactly what you’d type in your terminal after the command name.

- **`env` (optional)**  
  Extra environment variables to set for that server. Often not needed.

---

## 5. Example: FastMCP Server with `uv` (STDIO)

Say you have this file:

```text
/Users/abhinav/Documents/Sanketana/GenAI-Foundations/Week08_MCP/code/fastmcp_quickstart.py
```

And you normally run it as:

```bash
uv run --with mcp python fastmcp_quickstart.py
```

First, find the full path to `uv`:

```bash
which uv
# e.g. /opt/homebrew/bin/uv
```

Then configure Claude Desktop like this:

```json
{
  "mcpServers": {
    "fastmcp-demo": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "run",
        "--with",
        "mcp",
        "python",
        "/Users/abhinav/Documents/Sanketana/GenAI-Foundations/Week08_MCP/code/fastmcp_quickstart.py"
      ]
    }
  }
}
```

Notes:

- `command` = full path to `uv` (so Claude can always find it).
- `args` = what follows `uv` in your terminal: `run --with mcp python fastmcp_quickstart.py`.
- The Python file uses `mcp.run()` with **STDIO**, so Claude can speak MCP directly.

After saving:

1. Quit Claude Desktop completely (`Cmd + Q`).
2. Reopen it.
3. Go to **Settings → Developer → Local MCP servers**.  
   You should see `fastmcp-demo` as **running** (not failed).
4. In a chat, you can ask Claude to use the `fastmcp-demo` tools.

---

## 6. Other Examples (Node, Filesystem, Fetch)

### 6.1 “Everything” server (Node + npx)

```json
{
  "mcpServers": {
    "everything": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-everything"
      ]
    }
  }
}
```

Claude will run:

```bash
npx -y @modelcontextprotocol/server-everything
```

### 6.2 Filesystem server

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/abhinav/Documents"
      ]
    }
  }
}
```

This gives Claude a view into the specified directory via MCP.

### 6.3 Fetch server (Python + `uvx`)

```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": [
        "mcp-server-fetch"
      ]
    }
  }
}
```

Here `uvx` runs the `mcp-server-fetch` CLI without a permanent install.

---

## 7. The `@` Syntax (Auto-download Servers)

In some setups you can use an **`@` syntax** with tools like `uvx` or `npx` to automatically fetch a server from a package.

For example (conceptual pattern):

```json
{
  "mcpServers": {
    "my-pypi-server": {
      "command": "uvx",
      "args": [
        "@my-mcp-server-package"
      ]
    }
  }
}
```

Or for Node:

```json
{
  "mcpServers": {
    "my-node-server": {
      "command": "npx",
      "args": [
        "-y",
        "@my-org/my-mcp-server"
      ]
    }
  }
}
```

The idea:

- You don’t keep the code locally.
- Claude (via `uvx` or `npx`) downloads and runs the server on demand.
- This is handy for **students, demos, and shared tools**.

(Exact behavior depends on how the package is published and which runner you use.)

---

## 8. When to Use STDIO vs HTTP

### Use **STDIO** when:

- You are integrating with **Claude Desktop**.
- The server is installed **locally**.
- You want Claude to start/stop the server automatically.
- You’re okay with MCP traffic staying on the local machine.

### Use **HTTP** when:

- You want to **share** the server across machines.
- You are building integrations for **editors or other MCP clients**.
- You’re comfortable starting the server manually or via a separate service.

Remember:
- Claude Desktop’s config is primarily meant to describe **how to start local STDIO servers**.
- HTTP is better handled by other clients or wrappers.

---

## 9. Troubleshooting Checklist

If you see errors like **“Server disconnected”** or **“failed”** in Claude Desktop:

1. **Check the logs**  
   - In Claude Desktop → Developer → Local MCP servers → `Open Logs Folder`.
   - Look for messages like `command not found` or `No such file or directory`.

2. **Verify paths**  
   - Use `which uv`, `which python3`, `which npx` in terminal.
   - Use those **absolute paths** in the `command` field if needed.
   - Confirm the `.py` or script path actually exists with `ls /path/to/file.py`.

3. **Keep JSON clean**  
   - `claude_desktop_config.json` must be **valid JSON only**.
   - No comments, no extra separators, no Python code mixed in.

4. **Restart Claude Desktop**  
   - Changes to config are picked up on restart.
   - Fully quit using `Cmd + Q` (not just closing the window).

5. **Check transport**  
   - For Claude Desktop-managed servers, make sure your code is using `mcp.run()` with default STDIO.
   - If you’re using HTTP, remember Claude won’t auto-manage it from this config alone.

---

## 10. Quick Summary

- Use **STDIO** + `mcp.run()` (default) for Claude Desktop.
- Describe your servers in **`claude_desktop_config.json` → `mcpServers`**.
- Let **Claude start the server**; don’t run it manually in a terminal for the Desktop flow.
- Use **absolute paths** for tools like `uv`, `python3`, and `npx` if necessary.
- Use **HTTP transport** for other MCP clients or remote scenarios, not as the primary Claude Desktop path.

Once this is set up, you can teach or demo:

> “Look, we’ve built our own MCP server, wired it into Claude Desktop, and now Claude can call our custom tools like `add`, `get_greeting`, and more.” 🎉
