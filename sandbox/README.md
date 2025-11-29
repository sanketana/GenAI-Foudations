# Dell PowerStore MCP Server

A Model Context Protocol (MCP) server that wraps the Dell PowerStore REST API (v4.1.0) for storage management. This server provides a standardized interface for interacting with Dell PowerStore storage systems through MCP tools.

## Features

- **CA Certificate Authentication**: Secure authentication using CA certificates
- **Storage Management**: Query volumes, hosts, and their mappings
- **MCP Integration**: Standard MCP protocol for easy integration with MCP clients
- **Extensible Design**: Easy to add additional API endpoints

## Prerequisites

- Python 3.8 or higher
- Access to a Dell PowerStore system
- CA certificate file for API authentication
- Dell PowerStore REST API base URL

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd S178
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The server requires two configuration parameters:

1. **Dell API Base URL**: The base URL of your PowerStore REST API
2. **CA Certificate Path**: Path to the CA certificate file for authentication

### Configuration Methods

You can provide configuration in two ways:

#### Method 1: Environment Variables (Recommended)

Create a `.env` file in the project root:

```bash
# Dell PowerStore API Configuration
DELL_API_BASE_URL=https://<PowerStore-mgmt-ip/fqdn>/api/rest

# CA Certificate Path (absolute path recommended)
DELL_CA_CERT_PATH=/path/to/ca_certificate.pem
```

Or set environment variables directly:

```bash
export DELL_API_BASE_URL="https://your-powerstore.example.com/api/rest"
export DELL_CA_CERT_PATH="/path/to/ca_certificate.pem"
```

**Note on Certificate Path:**
- The certificate file can be located anywhere on the filesystem
- **Absolute paths are recommended** (e.g., `/etc/ssl/certs/dell_ca.pem` or `C:\certs\dell_ca.pem`)
- If using a relative path, it will be resolved from the **current working directory** where the server is run (not from the server code location)
- The path must point to a valid, readable certificate file

#### Method 2: Programmatic Configuration

You can also pass configuration programmatically when initializing the `Config` class (see code examples).

### API Base URL Format

The API base URL should follow this format:
```
https://<PowerStore-mgmt-ip/fqdn>/api/rest
```

For example:
```
https://192.168.1.100/api/rest
https://powerstore.example.com/api/rest
```

## Usage

### Running the MCP Server

Run the server using Python's `-m` flag:

```bash
python -m dell_mcp_server
```

The server will start and listen for MCP requests via stdio transport.

### Available MCP Tools

The server exposes the following MCP tools:

#### 1. `list_volumes`

List all volumes from the Dell PowerStore system.

**Parameters:**
- `select` (optional): Comma-separated list of fields to select (e.g., "name,type,state,size")
- `filter` (optional): Filter expression for volumes

**Example:**
```json
{
  "name": "list_volumes",
  "arguments": {
    "select": "name,type,state,size"
  }
}
```

#### 2. `get_volume_details`

Get detailed information about a specific volume.

**Parameters:**
- `volume_id` (required): The ID of the volume to retrieve

**Example:**
```json
{
  "name": "get_volume_details",
  "arguments": {
    "volume_id": "volume-id-123"
  }
}
```

#### 3. `list_hosts`

List all hosts from the Dell PowerStore system.

**Parameters:**
- `select` (optional): Comma-separated list of fields to select
- `filter` (optional): Filter expression for hosts

**Example:**
```json
{
  "name": "list_hosts",
  "arguments": {
    "select": "name,type,os_type"
  }
}
```

#### 4. `get_host_details`

Get detailed information about a specific host.

**Parameters:**
- `host_id` (required): The ID of the host to retrieve

**Example:**
```json
{
  "name": "get_host_details",
  "arguments": {
    "host_id": "host-id-456"
  }
}
```

#### 5. `get_volume_host_mappings`

Get host mappings for a specific volume.

**Parameters:**
- `volume_id` (required): The ID of the volume to get host mappings for

**Example:**
```json
{
  "name": "get_volume_host_mappings",
  "arguments": {
    "volume_id": "volume-id-123"
  }
}
```

### Response Format

All tools return JSON strings with the following structure:

**Success Response:**
```json
{
  "success": true,
  "data": { ... },
  "count": 5
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error message",
  "status_code": 404
}
```

## Testing with MCP Inspector

You can test the server using the MCP Inspector:

```bash
npx -y @modelcontextprotocol/inspector
```

Then configure the inspector to connect to your server.

## Project Structure

```
S178/
├── dell_mcp_server/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Main entry point
│   ├── server.py            # MCP server implementation
│   ├── dell_client.py       # Dell API client
│   ├── config.py            # Configuration management
│   └── models.py            # Data models
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Error Handling

The server includes comprehensive error handling:

- **Configuration Errors**: Validates configuration on startup
- **API Errors**: Handles HTTP errors (4xx, 5xx) from Dell API
- **Network Errors**: Handles connection and timeout errors
- **Unexpected Errors**: Catches and logs all unexpected exceptions

All errors are returned in a structured format with descriptive error messages.

## Extending the Server

To add new API endpoints:

1. **Add a method to `DellAPIClient`** in `dell_mcp_server/dell_client.py`:
   ```python
   async def get_new_endpoint(self, param: str) -> APIResponse:
       return await self._make_request("GET", "new_endpoint", params={"param": param})
   ```

2. **Add a tool to the MCP server** in `dell_mcp_server/server.py`:
   ```python
   @mcp.tool()
   async def new_tool(param: str) -> str:
       """Description of the tool."""
       response = await dell_client.get_new_endpoint(param)
       # Process and return response
   ```

3. **Update data models** in `dell_mcp_server/models.py` if needed.

## Dependencies

- `mcp>=1.0.0` - MCP Python SDK
- `httpx>=0.25.0` - Async HTTP client with CA cert support
- `pydantic>=2.0.0` - Data validation
- `python-dotenv>=1.0.0` - Environment variable management

## Troubleshooting

### Certificate Errors

If you encounter SSL/certificate errors:

1. Verify the CA certificate file path is correct
2. Ensure the certificate file is readable
3. Check that the certificate is valid and not expired
4. Verify the certificate matches your PowerStore system

### Connection Errors

If you cannot connect to the API:

1. Verify the `DELL_API_BASE_URL` is correct
2. Check network connectivity to the PowerStore system
3. Ensure the PowerStore system is accessible
4. Verify firewall rules allow connections

### Configuration Errors

If you see configuration errors:

1. Ensure both `DELL_API_BASE_URL` and `DELL_CA_CERT_PATH` are set
2. Verify the certificate file exists at the specified path
3. Check file permissions on the certificate file

## License

This project is provided as-is for use with Dell PowerStore systems.

## Support

For issues related to:
- **Dell PowerStore API**: Refer to [Dell PowerStore API Documentation](https://developer.dell.com/apis/3898/versions/4.1.0/docs)
- **MCP Protocol**: Refer to [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- **This Server**: Check the code and error messages for troubleshooting

