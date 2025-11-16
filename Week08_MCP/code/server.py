# server.py
from mcp.server.fastmcp import FastMCP
import os
import psutil

server = FastMCP(name="local-info")


@server.tool()
def get_system_info() -> dict:
    """Return basic host system metrics."""
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "cwd": os.getcwd(),
    }


if __name__ == "__main__":
    server.run()