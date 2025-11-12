import os 
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types

api_key = os.environ("GOOGLE_API_KEY")