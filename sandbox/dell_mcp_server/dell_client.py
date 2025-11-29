"""Dell PowerStore API client with CA certificate authentication."""

import logging
from typing import Optional, List, Dict, Any
import httpx
from .config import Config
from .models import Volume, Host, VolumeHostMapping, APIResponse


logger = logging.getLogger(__name__)


class DellAPIClient:
    """Client for interacting with Dell PowerStore REST API."""
    
    def __init__(self, config: Config):
        """
        Initialize Dell API client.
        
        Args:
            config: Configuration object with API base URL and CA cert path
        """
        self.config = config
        self.base_url = config.api_base_url
        self.ca_cert_path = config.ca_cert_path
        
        # Create HTTP client with CA certificate verification
        self.client = httpx.AsyncClient(
            verify=self.ca_cert_path,
            timeout=30.0,
            follow_redirects=True
        )
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()
    
    async def __aenter__(self):
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
    
    async def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None
    ) -> APIResponse:
        """
        Make an HTTP request to the Dell API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (relative to base URL)
            params: Query parameters
        
        Returns:
            APIResponse object with success status and data
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = await self.client.request(
                method=method,
                url=url,
                params=params
            )
            response.raise_for_status()
            
            # Parse JSON response
            data = response.json()
            
            return APIResponse(
                success=True,
                data=data,
                status_code=response.status_code
            )
        
        except httpx.HTTPStatusError as e:
            error_msg = f"HTTP error {e.response.status_code}: {e.response.text}"
            logger.error(error_msg)
            return APIResponse(
                success=False,
                error=error_msg,
                status_code=e.response.status_code
            )
        
        except httpx.RequestError as e:
            error_msg = f"Request error: {str(e)}"
            logger.error(error_msg)
            return APIResponse(
                success=False,
                error=error_msg,
                status_code=None
            )
        
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return APIResponse(
                success=False,
                error=error_msg,
                status_code=None
            )
    
    async def get_volumes(
        self,
        select: Optional[str] = None,
        filter: Optional[str] = None
    ) -> APIResponse:
        """
        List all volumes.
        
        Args:
            select: Comma-separated list of fields to select (e.g., "name,type,state,size")
            filter: Filter expression for volumes
        
        Returns:
            APIResponse with list of volumes
        """
        params = {}
        if select:
            params["select"] = select
        if filter:
            params["filter"] = filter
        
        return await self._make_request("GET", "volume", params=params)
    
    async def get_volume_by_id(self, volume_id: str) -> APIResponse:
        """
        Get specific volume details by ID.
        
        Args:
            volume_id: Volume ID
        
        Returns:
            APIResponse with volume details
        """
        return await self._make_request("GET", f"volume/{volume_id}")
    
    async def get_hosts(
        self,
        select: Optional[str] = None,
        filter: Optional[str] = None
    ) -> APIResponse:
        """
        List all hosts.
        
        Args:
            select: Comma-separated list of fields to select
            filter: Filter expression for hosts
        
        Returns:
            APIResponse with list of hosts
        """
        params = {}
        if select:
            params["select"] = select
        if filter:
            params["filter"] = filter
        
        return await self._make_request("GET", "host", params=params)
    
    async def get_host_by_id(self, host_id: str) -> APIResponse:
        """
        Get specific host details by ID.
        
        Args:
            host_id: Host ID
        
        Returns:
            APIResponse with host details
        """
        return await self._make_request("GET", f"host/{host_id}")
    
    async def get_volume_host_mappings(self, volume_id: str) -> APIResponse:
        """
        Get host mappings for a specific volume.
        
        Args:
            volume_id: Volume ID
        
        Returns:
            APIResponse with host mappings
        """
        # First get volume details to find mappings
        volume_response = await self.get_volume_by_id(volume_id)
        
        if not volume_response.success:
            return volume_response
        
        # Extract host mappings from volume data
        volume_data = volume_response.data
        if isinstance(volume_data, dict):
            mappings = volume_data.get("host_virtual_volume_mappings", [])
            return APIResponse(
                success=True,
                data=mappings,
                status_code=volume_response.status_code
            )
        
        return APIResponse(
            success=False,
            error="Unable to extract host mappings from volume data"
        )

