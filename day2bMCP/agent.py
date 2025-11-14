from dotenv import load_dotenv
import os 

import uuid
from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from google.adk.apps.app import App, ResumabilityConfig
from google.adk.tools.function_tool import FunctionTool

from IPython.display import display, Image as IPImage
import base64

print("✅ ADK components imported successfully.")

load_dotenv()

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

# MCP integration with Everything Server

mcp_image_server = McpToolset(
    connection_params= StdioConnectionParams(
        server_params= StdioServerParameters(
            command="npx", #Run MCP Server
            args=[
                "-y",
                "@modelcontextprotocol/server-everything",
            ],
            tool_filter=["getTinyImage"],
        ),
        timeout = 30,
    )

)

image_agent = LlmAgent(
    model= Gemini(model="gemini-2.5-flash-lite", retry_options= retry_config),
    name="image_agent",
    instruction= "Use the MCP tool to generate images for user queries",
    tools=[mcp_image_server],
)

root_agent = image_agent

# Note: The image display code should be in a separate script or notebook,
# not at module level. The agent will handle responses automatically when run via ADK CLI.