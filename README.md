# LangGraph Greeting Agent (Python)

A minimal LangGraph implementation showcasing the framework's core concepts without LLM dependencies. This project demonstrates how to build a simple single-node agent using StateGraph, proper state management, and START → node → END flow.

## 🎯 Purpose

This is a learning project that focuses on:
- Understanding LangGraph's basic architecture
- Working with StateGraph and state schemas
- Implementing nodes without LLM complexity
- Following best practices for Python package management with `uv`

## ✨ Features

- ✅ Single-node agent with clear state schema
- ✅ No LLM dependencies - pure Python logic
- ✅ Proper START → greeting_node → END structure
- ✅ Managed with `uv` for modern Python packaging
- ✅ Interactive and programmatic usage modes
- ✅ Well-documented development process

## 🚀 What It Does

Accepts a user's name as input and returns a personalized greeting message.

**Input:** `{"name": "Sedat"}`  
**Output:** `{"greeting": "Hello, Sedat! Welcome!"}`

## 📋 Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) package manager

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/LangGraph-Agent-Implementation-Python.git
cd LangGraph-Agent-Implementation-Python
```

2. Install dependencies with uv:
```bash
uv sync
```

Or manually install:
```bash
uv pip install -e .
```

## 💻 Usage

### Interactive Mode (Recommended)

Run the agent interactively and enter names when prompted:
```bash
uv run python -m greeting_agent.interactive
```

**Example session:**
```
============================================================
🤖 LangGraph Greeting Agent - Interactive Mode
============================================================

This agent will greet you by name!
Type 'quit', 'exit', or 'q' to stop.

👤 Enter your name: Sedat
🤖 Hello, Sedat! Welcome!

👤 Enter your name: Alice
🤖 Hello, Alice! Welcome!

👤 Enter your name: quit
👋 Goodbye! Thanks for using the greeting agent!
```

### Demo Mode

Run the agent with predefined test cases:
```bash
uv run python -m greeting_agent.main
```

**Output:**
```
==================================================
LangGraph Greeting Agent - Test Run
==================================================

📥 Input: Sedat
📤 Output: Hello, Sedat! Welcome!

📥 Input: Alice
📤 Output: Hello, Alice! Welcome!

📥 Input: Bob
📤 Output: Hello, Bob! Welcome!

📥 Input: 世界
📤 Output: Hello, 世界! Welcome!

==================================================
```

### Programmatic Usage

Use the agent in your own Python code:
```python
from greeting_agent.graph import create_graph

# Create the graph
graph = create_graph()

# Invoke with a name
result = graph.invoke({"name": "Sedat"})

print(result["greeting"])  # Output: Hello, Sedat! Welcome!
```

## 📁 Project Structure
```
LangGraph-Agent-Implementation-Python/
├── src/
│   └── greeting_agent/
│       ├── __init__.py          # Package initialization
│       ├── state.py             # State schema definition
│       ├── graph.py             # Graph and node implementation
│       ├── main.py              # Demo/test script
│       └── interactive.py       # Interactive CLI
├── .gitignore                   # Git ignore rules
├── pyproject.toml              # Project metadata and dependencies
├── README.md                   # This file
└── dev-history.md              # Development process log
```

## 🏗️ Graph Architecture
```
START → greeting_node → END
```

**State Schema:**
```python
class GreetingState(TypedDict):
    name: str       # Input: user's name
    greeting: str   # Output: greeting message
```

**Node Function:**
```python
def greeting_node(state: GreetingState) -> dict:
    name = state["name"]
    greeting_message = f"Hello, {name}! Welcome!"
    return {"greeting": greeting_message}
```

## 🧪 Testing

Run the demo script to verify everything works:
```bash
uv run python -m greeting_agent.main
```

## 📝 Development History

See [dev-history.md](dev-history.md) for detailed development process, AI prompts used, and manual changes made during implementation.

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

MIT License - feel free to use this code for learning purposes.

## 🔗 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [LangChain Documentation](https://python.langchain.com/)

---

**Note:** This project is part of an internship technical task focused on demonstrating research skills, environment setup, and ability to work with new technologies. The simplicity of the code is intentional - the emphasis is on understanding LangGraph fundamentals and proper development practices.