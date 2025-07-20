# Google Search CLI Tool

A lightweight and powerful command-line tool that fetches the **top 10 organic Google search results** using [SerpAPI](https://serpapi.com/), with a focus on clean code and extensibility via LangChain tools.

## Features

* Simple CLI to perform Google searches
* Uses **SerpAPI** for reliable and fast results
* Clean output formatting with `rich` and `textwrap`
* Implements a `LangChain` `StructuredTool` for easy integration in agent frameworks
* Designed using OOP and best practices for AI startup development

---

## Requirements

* Python **3.8+** (tested on 3.13)
* A free [SerpAPI API key](https://serpapi.com/users/sign_up)

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Setup

1. Clone the repo and create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

2. Add your SerpAPI key to a `.env` file in the project root:

```
SERPAPI_API_KEY=your_key_here
```

3. Run the CLI:

```bash
python main.py "your search query"
```

---

## Project Structure

```
main.py         # Main logic and CLI entrypoint
.env            # Environment variables (API key)
requirements.txt
README.md
```



## LangChain Integration

The class `GoogleSearchTool` provides a `StructuredTool` for integration with LangChain-based agentic frameworks. To use it:

```python
from main import GoogleSearchTool

search_tool = GoogleSearchTool().as_langchain_tool()
```

This makes the search tool compatible with autonomous agents powered by LangChain or LangGraph.

---

## Next Steps with LangChain

Your search tool can now power more advanced AI workflows:

* **LLM Agents**: Plug it into a LangChain `initialize_agent()` function to build an agent that can decide when to search.
* **Multi-tool Pipelines**: Combine with web scrapers, summarizers, and emailers to automate tasks.
* **LangGraph Workflows**: Use with LangGraph to add memory and logic to multi-step AI agents.
* **FastAPI Deployment**: Expose your tool as a web service for broader usage.
* **Langfuse Observability**: Monitor performance, token usage, and tool behavior.


## Example Output

```
Top Google Search Results:

1. What Are AI Agents and How Do They Work?
   https://www.example.com/what-are-ai-agents

2. Types of Artificial Intelligence Agents
   https://www.example.com/types-of-ai-agents
```

---

## Testing

To test the CLI tool:

```bash
python main.py "latest AI agent frameworks"
```

You should see up to 10 formatted organic results printed to the terminal.

---

## Credits

* [SerpAPI](https://serpapi.com/) — Google Search Results API
* [LangChain](https://www.langchain.com/) — LLM-powered framework
* [Rich](https://github.com/Textualize/rich) — Terminal formatting

