# mcp_k8s_server.py
from mcp.server.fastmcp import FastMCP
# from Tools.kubectl import KubectlTool
import sys
from k8s_assistant.tools.tool_config import tools

sys.stdout.reconfigure(line_buffering=True)


def register_tools(server: FastMCP):
    """
    Load all tools.
    This function can be used to load any additional tools in the future.
    """
    # Currently, we are only loading the Kubectl tool
    for tool in tools:
        module = __import__(f"tools.{tool}", fromlist=[tool])
        tool_class = getattr(module, tool)
        tool_instance = tool_class()
        print(f"Loaded tool: {tool_instance.name}")
        # Register the tool with the server
        server.add_tool(
            tool_instance.run,
            name=tool_instance.name,
            description=tool_instance.description
        )


def initialize_server():
    """
    Initialize the FastMCP server.
    This function can be used to initialize any additional settings in the future.
    """
    server = FastMCP(
        name="MCP Server",
        instructions="This is an MCP Server for Cloud Operations tools.",
        settings={
            "host": "localhost",
            "port": 8080,
        }
    )
    return server


def run_server():
    
    # # Initialize the kubectl tool
    # kubectl = KubectlTool()
    
    # # Register the kubectl tool
    # server.add_tool(
    #     kubectl.run,
    #     name="kubectl",
    #     description="Execute a kubectl command against the Kubernetes cluster."
    # )
    
    # Start the server
    print(f"Starting server {server.name} on {server.settings.host}:{server.settings.port}...")
    server.run(transport="stdio")
    print("Server started. Listening for requests...")
    
if __name__ == "__main__":
    
    print("Starting MCP server...")
    
    # Initialize the server
    server = initialize_server()
    
    # Register all tools
    register_tools(server)
    
    # Run the server
    run_server()
