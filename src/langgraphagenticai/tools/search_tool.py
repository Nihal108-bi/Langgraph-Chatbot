from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langgraph.prebuilt import ToolNode

def get_tools():
    # Initialize INSIDE the function so it looks for the key 
    # only when the graph is actually being built.
    search = TavilySearchAPIWrapper() 
    return [TavilySearchResults(api_wrapper=search)]

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)

