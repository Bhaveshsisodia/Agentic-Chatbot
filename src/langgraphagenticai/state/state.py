from typing import TypedDict , List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """Defines the state structure for the LangGraph Agentic AI application."""
    messages: Annotated[List, add_messages]