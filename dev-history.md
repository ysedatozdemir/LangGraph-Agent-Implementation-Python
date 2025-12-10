# Development History

## Commit 1: Initial Setup
**Date:** 2024-12-10

**What I did:**
- Ran `uv init .` to create project structure
- Added langgraph with `uv add langgraph`
- Created `.gitignore` and basic package structure

**AI prompts:**
- "Need a professional GitHub description for a Python LangGraph greeting agent"
- "After uv init, what's next for setting up a LangGraph project with proper structure?"

**Manual changes:**
- Executed all terminal commands
- Created directory structure as suggested

---

## Commit 2: Core Implementation
**Date:** 2024-12-10

**What I did:**
- Implemented `GreetingState` schema with TypedDict
- Created `greeting_node` - simple string formatting, no LLM
- Built graph with START → greeting_node → END flow
- Added both demo script and interactive CLI

**AI prompts:**
- "Show me how to build a single-node LangGraph agent without LLM, using TypedDict for state"
- "Should I use TypedDict, dataclass, or Pydantic for a simple greeting state?"

**Manual changes:**
- Ran `uv pip install -e .` to fix import errors
- Tested with `uv run python -m greeting_agent.main`
- Removed `.idea/` directory (PyCharm config)

**Challenges:**
- **Python version mismatch**: Project initially used Python 3.9, but LangGraph requires 3.11+. Updated `pyproject.toml` to specify `requires-python = ">=3.11"`
- **ModuleNotFoundError**: Package wasn't installed in editable mode. Fixed with `uv pip install -e .`
- **Wrong virtual environment**: IDE was using another project's venv. Used `uv run` for reliability

**Resources used:**
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph Tutorial - How to Build Advanced AI Agent Systems](https://www.youtube.com/watch?v=EXAMPLE)

---

## Commit 3: Documentation
**Date:** 2024-12-10

**What I did:**
- Created comprehensive README with installation, usage examples, and architecture
- Added three usage modes: interactive, demo, and programmatic
- Documented project structure and graph flow

**AI prompts:**
- "Create a README for a LangGraph greeting agent with uv installation, interactive CLI, demo mode, and programmatic API examples"

**Manual changes:**
- Adjusted examples based on actual file paths
- Added emoji markers for better readability

---

## Summary

**Key learnings:**
- LangGraph works great without LLMs - just pure Python functions
- `uv run` is more reliable than IDE execution
- TypedDict is perfect for simple state schemas
- Documenting AI assistance improves transparency
