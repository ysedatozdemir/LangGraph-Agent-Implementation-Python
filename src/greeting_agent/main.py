"""Main entry point for the greeting agent."""
from greeting_agent.graph import create_graph


def main():
    """Run the greeting agent with sample inputs."""
    # Create the graph
    graph = create_graph()

    # Test with different names
    test_names = ["Sedat", "Alice", "Bob", "世界"]  # Including non-ASCII

    print("=" * 50)
    print("LangGraph Greeting Agent - Test Run")
    print("=" * 50)

    for name in test_names:
        print(f"\n📥 Input: {name}")

        # Invoke the graph
        result = graph.invoke({"name": name})

        print(f"📤 Output: {result['greeting']}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()