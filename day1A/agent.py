from dotenv import load_dotenv
import os 
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.genai import types

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


root_agent = Agent(
    name="helpful_assistant",
    model="gemini-2.5-flash-lite",
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)

