# Step 1: Setup API Keys for Groq and Tavily
import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# Step 2: Setup LLM & Tools
from langchain_groq import ChatGroq

# Safe import — try new package first, fall back to community package
try:
    from langchain_tavily import TavilySearch
    def make_search_tool():
        return TavilySearch(max_results=2)
except ImportError:
    from langchain_community.tools.tavily_search import TavilySearchResults
    def make_search_tool():
        return TavilySearchResults(max_results=2)

# Step 3: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt):
    llm = ChatGroq(model=llm_id)

    tools = [make_search_tool()] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )

    state = {"messages": [("user", query)]}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]





