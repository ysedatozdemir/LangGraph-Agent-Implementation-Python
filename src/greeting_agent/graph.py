"""LangGraph greeting agent implementation with LangSmith tracing."""
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langsmith import traceable
from greeting_agent.state import GreetingState

# Load environment variables
load_dotenv()


@traceable(name="greeting_node")
def greeting_node(state: GreetingState) -> dict:
    """Generate a greeting message from the input name.

    This node does NOT use any LLM - it's pure Python logic.
    Traced with LangSmith for observability.

    Args:
        state: The current state containing the name

    Returns:
        Dictionary with the greeting message
    """
    name = state["name"]
    greeting_message = f"Hello, {name}! Welcome!"
    return {"greeting": greeting_message}


@traceable(name="create_greeting_graph")
def create_graph() -> StateGraph:
    """Create and compile the greeting graph.

    Graph structure:
        START -> greeting_node -> END

    Returns:
        Compiled StateGraph ready to use
    """
    # Initialize the graph with our state schema
    builder = StateGraph(GreetingState)

    # Add the greeting node
    builder.add_node("greeting_node", greeting_node)

    # Define the flow: START -> greeting_node -> END
    builder.add_edge(START, "greeting_node")
    builder.add_edge("greeting_node", END)

    # Compile the graph
    graph = builder.compile()

    return graph