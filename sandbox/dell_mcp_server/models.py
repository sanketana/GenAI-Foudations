"""Data models for Dell PowerStore API responses."""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class Volume(BaseModel):
    """Volume data model."""
    
    id: Optional[str] = Field(None, description="Volume ID")
    name: Optional[str] = Field(None, description="Volume name")
    type: Optional[str] = Field(None, description="Volume type (e.g., Primary, Snapshot)")
    state: Optional[str] = Field(None, description="Volume state (e.g., Ready)")
    size: Optional[int] = Field(None, description="Volume size in bytes")
    description: Optional[str] = Field(None, description="Volume description")
    app_type: Optional[str] = Field(None, description="Application type")
    app_type_other: Optional[str] = Field(None, description="Other application type")
    creation_timestamp: Optional[str] = Field(None, description="Creation timestamp")
    protection_policy_id: Optional[str] = Field(None, description="Protection policy ID")
    protection_data: Optional[Dict[str, Any]] = Field(None, description="Protection data")
    
    class Config:
        """Pydantic config."""
        extra = "allow"  # Allow additional fields from API


class Host(BaseModel):
    """Host data model."""
    
    id: Optional[str] = Field(None, description="Host ID")
    name: Optional[str] = Field(None, description="Host name")
    type: Optional[str] = Field(None, description="Host type")
    os_type: Optional[str] = Field(None, description="Operating system type")
    description: Optional[str] = Field(None, description="Host description")
    initiators: Optional[List[Dict[str, Any]]] = Field(None, description="Host initiators")
    host_group_id: Optional[str] = Field(None, description="Host group ID")
    host_virtual_volume_mappings: Optional[List[Dict[str, Any]]] = Field(
        None, description="Virtual volume mappings"
    )
    
    class Config:
        """Pydantic config."""
        extra = "allow"  # Allow additional fields from API


class VolumeHostMapping(BaseModel):
    """Volume to host mapping data model."""
    
    id: Optional[str] = Field(None, description="Mapping ID")
    volume_id: Optional[str] = Field(None, description="Volume ID")
    host_id: Optional[str] = Field(None, description="Host ID")
    volume_name: Optional[str] = Field(None, description="Volume name")
    host_name: Optional[str] = Field(None, description="Host name")
    logical_unit_number: Optional[int] = Field(None, description="Logical unit number")
    
    class Config:
        """Pydantic config."""
        extra = "allow"  # Allow additional fields from API


class APIResponse(BaseModel):
    """Generic API response wrapper."""
    
    success: bool = Field(description="Whether the API call was successful")
    data: Optional[Any] = Field(None, description="Response data")
    error: Optional[str] = Field(None, description="Error message if any")
    status_code: Optional[int] = Field(None, description="HTTP status code")

