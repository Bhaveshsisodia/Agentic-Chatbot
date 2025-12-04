from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns a list of tool instances to be used in the chatbot with tools graph."""

    tools = [TavilySearchResults(max_results=3)]
    return tools


def create_tool_node(tools):

    """
    Creates and returns a ToolNode instance configured with the provided tools and language model.
    Args:
        tools (list): A list of tool instances to be integrated into the ToolNode.
        llm: The language model to be used by the ToolNode.
    Returns:
        ToolNode: An instance of ToolNode configured with the specified tools and language model.
    """
    return ToolNode(tools=tools)