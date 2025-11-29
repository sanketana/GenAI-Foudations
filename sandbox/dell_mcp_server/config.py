"""Configuration management for Dell PowerStore MCP Server."""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv


# Load environment variables from .env file if it exists
load_dotenv()


class Config:
    """Configuration class for Dell PowerStore API connection."""
    
    def __init__(
        self,
        api_base_url: Optional[str] = None,
        ca_cert_path: Optional[str] = None
    ):
        """
        Initialize configuration.
        
        Args:
            api_base_url: Dell API base URL. If not provided, reads from DELL_API_BASE_URL env var.
            ca_cert_path: Path to CA certificate. If not provided, reads from DELL_CA_CERT_PATH env var.
        
        Raises:
            ValueError: If required configuration is missing or invalid.
        """
        # API Base URL
        self.api_base_url = api_base_url or os.getenv("DELL_API_BASE_URL")
        if not self.api_base_url:
            raise ValueError(
                "Dell API base URL must be provided either as parameter or "
                "DELL_API_BASE_URL environment variable"
            )
        
        # Ensure URL doesn't end with trailing slash
        self.api_base_url = self.api_base_url.rstrip("/")
        
        # CA Certificate Path
        self.ca_cert_path = ca_cert_path or os.getenv("DELL_CA_CERT_PATH")
        if not self.ca_cert_path:
            raise ValueError(
                "CA certificate path must be provided either as parameter or "
                "DELL_CA_CERT_PATH environment variable"
            )
        
        # Resolve the certificate path
        # If it's an absolute path, use it as-is
        # If it's a relative path, resolve it relative to current working directory
        cert_path = Path(self.ca_cert_path)
        if not cert_path.is_absolute():
            # Resolve relative path (relative to current working directory)
            cert_path = cert_path.resolve()
            self.ca_cert_path = str(cert_path)
        
        # Validate certificate file exists and is readable
        if not cert_path.exists():
            raise ValueError(
                f"CA certificate file not found: {self.ca_cert_path}\n"
                f"Note: Relative paths are resolved from the current working directory: {os.getcwd()}"
            )
        
        if not cert_path.is_file():
            raise ValueError(f"CA certificate path is not a file: {self.ca_cert_path}")
        
        if not os.access(cert_path, os.R_OK):
            raise ValueError(f"CA certificate file is not readable: {self.ca_cert_path}")
    
    def __repr__(self) -> str:
        """String representation of configuration."""
        return (
            f"Config(api_base_url='{self.api_base_url}', "
            f"ca_cert_path='{self.ca_cert_path}')"
        )

