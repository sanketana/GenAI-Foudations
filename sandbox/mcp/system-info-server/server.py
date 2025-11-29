from mcp.server.fastmcp import FastMCP
import os
import psutil

server = FastMCP(name="local-info")

@server.tool()
def get_system_info() -> dict:
    """Return basic host system metrics """

    return {
        "cpu_percentage": psutil.cpu_percent(),
        "memory_percentage": psutil.virtual_memory().percent,
        "cwd": os.getcwd(),
    }