"""Interactive command-line interface for the greeting agent."""
from greeting_agent.graph import create_graph


def main():
    """Run the greeting agent interactively with user input."""
    # Create the graph once
    graph = create_graph()

    print("=" * 60)
    print("🤖 LangGraph Greeting Agent - Interactive Mode")
    print("=" * 60)
    print("\nThis agent will greet you by name!")
    print("Type 'quit', 'exit', or 'q' to stop.\n")

    while True:
        # Get user input
        name = input("👤 Enter your name: ").strip()

        # Check for exit commands
        if name.lower() in ['quit', 'exit', 'q', '']:
            print("\n👋 Goodbye! Thanks for using the greeting agent!")
            break

        # Invoke the graph with user input
        try:
            result = graph.invoke({"name": name})
            print(f"🤖 {result['greeting']}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    main()