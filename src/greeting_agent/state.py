"""State schema for the greeting agent."""
from typing_extensions import TypedDict


class GreetingState(TypedDict):
    """State for the greeting graph.

    Attributes:
        name: The input name to greet
        greeting: The output greeting message
    """
    name: str
    greeting: str