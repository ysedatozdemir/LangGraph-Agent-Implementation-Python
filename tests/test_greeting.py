"""Unit tests for the greeting agent."""
import pytest
from greeting_agent.graph import create_graph, greeting_node
from greeting_agent.state import GreetingState


class TestGreetingNode:
    """Test the greeting_node function."""

    def test_simple_greeting(self):
        """Test greeting with a simple name."""
        state: GreetingState = {"name": "Alice", "greeting": ""}
        result = greeting_node(state)

        assert result["greeting"] == "Hello, Alice! Welcome!"

    def test_different_names(self):
        """Test greeting with different names."""
        test_cases = [
            ("Sedat", "Hello, Sedat! Welcome!"),
            ("Bob", "Hello, Bob! Welcome!"),
            ("Charlie", "Hello, Charlie! Welcome!"),
        ]

        for name, expected in test_cases:
            state: GreetingState = {"name": name, "greeting": ""}
            result = greeting_node(state)
            assert result["greeting"] == expected

    def test_unicode_names(self):
        """Test greeting with Unicode characters."""
        state: GreetingState = {"name": "世界", "greeting": ""}
        result = greeting_node(state)

        assert result["greeting"] == "Hello, 世界! Welcome!"

    def test_empty_name(self):
        """Test greeting with empty name."""
        state: GreetingState = {"name": "", "greeting": ""}
        result = greeting_node(state)

        assert result["greeting"] == "Hello, ! Welcome!"


class TestGreetingGraph:
    """Test the complete greeting graph."""

    def test_graph_creation(self):
        """Test that graph can be created without errors."""
        graph = create_graph()
        assert graph is not None

    def test_graph_invoke_simple(self):
        """Test graph invocation with a simple name."""
        graph = create_graph()
        result = graph.invoke({"name": "Alice"})

        assert "greeting" in result
        assert result["greeting"] == "Hello, Alice! Welcome!"

    def test_graph_invoke_multiple(self):
        """Test graph with multiple invocations."""
        graph = create_graph()

        test_cases = [
            ("Sedat", "Hello, Sedat! Welcome!"),
            ("Bob", "Hello, Bob! Welcome!"),
            ("世界", "Hello, 世界! Welcome!"),
        ]

        for name, expected in test_cases:
            result = graph.invoke({"name": name})
            assert result["greeting"] == expected

    def test_graph_state_structure(self):
        """Test that graph output has correct structure."""
        graph = create_graph()
        result = graph.invoke({"name": "Test"})

        assert isinstance(result, dict)
        assert "name" in result
        assert "greeting" in result
        assert result["name"] == "Test"