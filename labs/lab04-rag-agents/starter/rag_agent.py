"""
Lab 04 — Starter: RAG-Powered Agent
=====================================

Your task:
  1. Implement the `search_documents` function using hybrid search
     (keyword + vector).  The solution currently uses keyword-only search.

  2. Add a `list_sources` tool that returns the unique source filenames
     currently in the index, so users know what documents are available.

See README.md for detailed instructions.
"""

import json
import os

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv
from openai import AzureOpenAI
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()

aoai_client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
)
MODEL = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")

search_client = SearchClient(
    endpoint=os.environ["AZURE_SEARCH_ENDPOINT"],
    index_name=os.environ.get("AZURE_SEARCH_INDEX_NAME", "workshop-index"),
    credential=AzureKeyCredential(os.environ["AZURE_SEARCH_API_KEY"]),
)

# ---------------------------------------------------------------------------
# TODO: Implement search_documents with hybrid search
# ---------------------------------------------------------------------------

def search_documents(query: str, top: int = 5) -> list[dict]:
    """Search the knowledge base.

    Currently uses keyword-only search.
    TODO: Upgrade to hybrid (keyword + vector) search.

    Steps:
      1. Generate a query embedding using aoai_client.embeddings.create(...)
      2. Create a VectorizedQuery from azure.search.documents.models
      3. Pass both search_text=query and vector_queries=[...] to search_client.search
    """
    # Keyword-only search (starter implementation)
    results = search_client.search(
        search_text=query,
        select=["source", "content"],
        top=top,
    )
    return [{"source": r["source"], "content": r["content"]} for r in results]


# TODO: Implement list_sources


TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "search_documents",
            "description": "Search the knowledge base for relevant information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "top": {"type": "integer", "default": 5},
                },
                "required": ["query"],
            },
        },
    },
    # TODO: Add schema for list_sources
]

TOOL_IMPLEMENTATIONS: dict = {"search_documents": search_documents}

SYSTEM_PROMPT = (
    "You are a helpful knowledge assistant. "
    "Use search_documents to find relevant context before answering. "
    "Always cite the source filename in your answer."
)


def run_agent(messages: list[dict]) -> str:
    for _ in range(10):
        response = aoai_client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOL_SCHEMAS,
            tool_choice="auto",
        )
        msg = response.choices[0].message
        if not msg.tool_calls:
            return msg.content or ""
        messages.append(msg)  # type: ignore[arg-type]
        for tc in msg.tool_calls:
            func_name = tc.function.name
            func_args = json.loads(tc.function.arguments)
            if func_name in TOOL_IMPLEMENTATIONS:
                result = TOOL_IMPLEMENTATIONS[func_name](**func_args)
            else:
                result = {"error": f"Unknown tool: {func_name}"}
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": json.dumps(result)})
    return "Error: max turns reached."


def main() -> None:
    console.print(Panel("[bold]RAG Agent Starter[/] — Lab 04", title="AgenticOdyssey"))
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    while True:
        user_input = console.input("\n[green]You:[/] ").strip()
        if user_input.lower() in ("exit", "quit", "q"):
            break
        if not user_input:
            continue
        messages.append({"role": "user", "content": user_input})
        answer = run_agent(messages)
        console.print(f"\n[blue]Assistant:[/] {answer}")
        messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()
