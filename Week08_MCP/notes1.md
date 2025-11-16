# Week 08: Model Context Protocol (MCP) - Instructor Notes
====
- Overview
- Host, Client, Server
- Example with Claude Code
    - everything server
    - File system demo
- Example with Cursor

- Example using an existing remote server
- Example using a local server
- Advanced local server
- Advanced concepts, prompts, resources, context, sampling etc
- Integrated example



Use cases
- Example multi-server travel planning
- Database call
- API calls
- File system ops
- Web search
====

Project flow
- Simple dummy MCP
- 

Local vs Remote MCP servers

- MCP Python SDK
- UV Installation
- MCP Inspector
- MCP Tools, Context, Resources, Prompts (with examples)
- Others - sampling, elicitation, root, auth

Good description
https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file



## Learning Objectives
- Explain the goals and architecture of the Model Context Protocol
- Demonstrate how MCP standardizes tool and data access for LLM applications
- Configure an MCP server and connect it to an LLM client
- Extend an MCP deployment with custom tools and schemas

## Session Outline
1. Conceptual overview of the MCP specification and ecosystem
2. Anatomy of an MCP server: transports, capabilities, authentication
3. Registering tools, resources, and prompts within MCP
4. Client integration patterns (LangChain, custom SDKs, CLI utilities)
5. Observability, logging, and security considerations

## Hands-on Plan
- Inspect the official MCP reference implementation
- Stand up a minimal MCP server with a filesystem tool
- Connect the classroom LLM client to the server and execute tool calls
- Add a custom retrieval tool backed by vector search
- Trace interactions and debug using MCP inspection utilities

## Discussion Topics
- Comparing MCP with ad-hoc tool calling or REST integrations
- Versioning strategies for MCP capabilities
- Managing secrets and credentials in MCP deployments
- When to build versus adopt existing MCP tools

## Follow-up Ideas
- Explore multi-tenant MCP architectures
- Investigate latency optimizations for synchronous tool calls
- Prototype MCP-driven workflows for internal knowledge bases
