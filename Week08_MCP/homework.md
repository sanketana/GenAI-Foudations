# Week 08 Homework — Model Context Protocol

## Objectives
- Reproduce the in-class MCP server setup
- Experiment with registering custom tools and resources
- Document observations about interoperability and debugging

## Tasks
1. **Bootstrap an MCP server locally**
   - Use the classroom template or the official quickstart as a reference
   - Configure at least one file-system backed resource and one custom tool
2. **Connect an LLM client to your MCP server**
   - Test tool invocation from LangChain or another preferred SDK
   - Capture logs showing successful tool execution
3. **Extend the deployment**
   - Add a retrieval or analytics tool relevant to your capstone topic
   - Write a short description of the tool contract (inputs/outputs)
4. **Reflection**
   - Summarize challenges, debugging steps, and best practices learned

## Submission Checklist
- Git commit (or shared repo link) with your MCP server configuration and code
- README snippet explaining how to start the server and client
- Log excerpts or screenshots demonstrating tool execution
- Reflection notes (≈200 words)

## Stretch Goals (Optional)
- Secure the MCP transport with API key or OAuth-style auth
- Add structured tracing via LangSmith or an equivalent observability stack
- Prototype a multi-step workflow chaining multiple MCP tools
