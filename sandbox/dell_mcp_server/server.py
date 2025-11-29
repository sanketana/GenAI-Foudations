"""MCP Server for Dell PowerStore storage management."""

import logging
import json
from typing import Optional
from mcp.server.fastmcp import FastMCP
from .config import Config
from .dell_client import DellAPIClient


logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("Dell PowerStore Storage Manager")

# Global client instance (will be initialized in main)
dell_client: Optional[DellAPIClient] = None


def initialize_client(config: Config):
    """
    Initialize the Dell API client.
    
    Args:
        config: Configuration object
    """
    global dell_client
    dell_client = DellAPIClient(config)
    logger.info("Dell API client initialized")


@mcp.tool()
async def list_volumes(
    select: Optional[str] = None,
    filter: Optional[str] = None
) -> str:
    """
    List all volumes from the Dell PowerStore system.
    
    Args:
        select: Optional comma-separated list of fields to select (e.g., "name,type,state,size")
        filter: Optional filter expression for volumes
    
    Returns:
        JSON string containing list of volumes or error message
    """
    if dell_client is None:
        return json.dumps({
            "success": False,
            "error": "Dell API client not initialized"
        })
    
    try:
        response = await dell_client.get_volumes(select=select, filter=filter)
        
        if response.success:
            return json.dumps({
                "success": True,
                "data": response.data,
                "count": len(response.data) if isinstance(response.data, list) else 1
            })
        else:
            return json.dumps({
                "success": False,
                "error": response.error,
                "status_code": response.status_code
            })
    
    except Exception as e:
        logger.error(f"Error listing volumes: {e}", exc_info=True)
        return json.dumps({
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        })


@mcp.tool()
async def get_volume_details(volume_id: str) -> str:
    """
    Get detailed information about a specific volume.
    
    Args:
        volume_id: The ID of the volume to retrieve
    
    Returns:
        JSON string containing volume details or error message
    """
    if dell_client is None:
        return json.dumps({
            "success": False,
            "error": "Dell API client not initialized"
        })
    
    if not volume_id:
        return json.dumps({
            "success": False,
            "error": "volume_id is required"
        })
    
    try:
        response = await dell_client.get_volume_by_id(volume_id)
        
        if response.success:
            return json.dumps({
                "success": True,
                "data": response.data
            })
        else:
            return json.dumps({
                "success": False,
                "error": response.error,
                "status_code": response.status_code
            })
    
    except Exception as e:
        logger.error(f"Error getting volume details: {e}", exc_info=True)
        return json.dumps({
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        })


@mcp.tool()
async def list_hosts(
    select: Optional[str] = None,
    filter: Optional[str] = None
) -> str:
    """
    List all hosts from the Dell PowerStore system.
    
    Args:
        select: Optional comma-separated list of fields to select
        filter: Optional filter expression for hosts
    
    Returns:
        JSON string containing list of hosts or error message
    """
    if dell_client is None:
        return json.dumps({
            "success": False,
            "error": "Dell API client not initialized"
        })
    
    try:
        response = await dell_client.get_hosts(select=select, filter=filter)
        
        if response.success:
            return json.dumps({
                "success": True,
                "data": response.data,
                "count": len(response.data) if isinstance(response.data, list) else 1
            })
        else:
            return json.dumps({
                "success": False,
                "error": response.error,
                "status_code": response.status_code
            })
    
    except Exception as e:
        logger.error(f"Error listing hosts: {e}", exc_info=True)
        return json.dumps({
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        })


@mcp.tool()
async def get_host_details(host_id: str) -> str:
    """
    Get detailed information about a specific host.
    
    Args:
        host_id: The ID of the host to retrieve
    
    Returns:
        JSON string containing host details or error message
    """
    if dell_client is None:
        return json.dumps({
            "success": False,
            "error": "Dell API client not initialized"
        })
    
    if not host_id:
        return json.dumps({
            "success": False,
            "error": "host_id is required"
        })
    
    try:
        response = await dell_client.get_host_by_id(host_id)
        
        if response.success:
            return json.dumps({
                "success": True,
                "data": response.data
            })
        else:
            return json.dumps({
                "success": False,
                "error": response.error,
                "status_code": response.status_code
            })
    
    except Exception as e:
        logger.error(f"Error getting host details: {e}", exc_info=True)
        return json.dumps({
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        })


@mcp.tool()
async def get_volume_host_mappings(volume_id: str) -> str:
    """
    Get host mappings for a specific volume.
    
    Args:
        volume_id: The ID of the volume to get host mappings for
    
    Returns:
        JSON string containing host mappings or error message
    """
    if dell_client is None:
        return json.dumps({
            "success": False,
            "error": "Dell API client not initialized"
        })
    
    if not volume_id:
        return json.dumps({
            "success": False,
            "error": "volume_id is required"
        })
    
    try:
        response = await dell_client.get_volume_host_mappings(volume_id)
        
        if response.success:
            return json.dumps({
                "success": True,
                "data": response.data,
                "count": len(response.data) if isinstance(response.data, list) else 0
            })
        else:
            return json.dumps({
                "success": False,
                "error": response.error,
                "status_code": response.status_code
            })
    
    except Exception as e:
        logger.error(f"Error getting volume host mappings: {e}", exc_info=True)
        return json.dumps({
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        })

