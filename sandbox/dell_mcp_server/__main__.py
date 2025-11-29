"""Main entry point for Dell PowerStore MCP Server."""

import asyncio
import logging
import sys
from .config import Config
from .server import mcp, initialize_client


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr)
    ]
)

logger = logging.getLogger(__name__)


def main():
    """Main entry point for the MCP server."""
    try:
        # Load configuration from environment variables or parameters
        config = Config()
        logger.info(f"Configuration loaded: API URL={config.api_base_url}")
        
        # Initialize Dell API client
        initialize_client(config)
        logger.info("Dell API client initialized successfully")
        
        # Run the MCP server with stdio transport
        logger.info("Starting MCP server with stdio transport...")
        mcp.run()
    
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        sys.exit(1)
    
    except KeyboardInterrupt:
        logger.info("Server interrupted by user")
        sys.exit(0)
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

