"""
Lab 04 — Solution: RAG-Powered Agent
=====================================

Implements a ReAct-style agent with a `search_documents` tool backed by
Azure AI Search (keyword + vector hybrid search).

Run:
    python labs/lab04-rag-agents/solution/rag_agent.py
"""

import json
import os

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from dotenv import load_dotenv
from openai import AzureOpenAI
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()

# ---------------------------------------------------------------------------
# Clients
# ---------------------------------------------------------------------------
aoai_client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
)
MODEL = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")
EMBEDDING_DEPLOYMENT = os.environ.get("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-small")

search_client = SearchClient(
    endpoint=os.environ["AZURE_SEARCH_ENDPOINT"],
    index_name=os.environ.get("AZURE_SEARCH_INDEX_NAME", "workshop-index"),
    credential=AzureKeyCredential(os.environ["AZURE_SEARCH_API_KEY"]),
)

# ---------------------------------------------------------------------------
# Tool: search_documents
# ---------------------------------------------------------------------------

def search_documents(query: str, top: int = 5) -> list[dict]:
    """Search the knowledge base using hybrid keyword + vector search."""
    # Generate embedding for the query
    embedding_response = aoai_client.embeddings.create(
        model=EMBEDDING_DEPLOYMENT,
        input=[query],
    )
    query_vector = embedding_response.data[0].embedding

    vector_query = VectorizedQuery(
        vector=query_vector,
        k_nearest_neighbors=top,
        fields="content_vector",
    )

    results = search_client.search(
        search_text=query,          # BM25 keyword component
        vector_queries=[vector_query],  # Vector component
        select=["source", "content"],
        top=top,
    )

    return [
        {"source": r["source"], "content": r["content"]}
        for r in results
    ]


# ---------------------------------------------------------------------------
# Tool schemas
# ---------------------------------------------------------------------------
TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "search_documents",
            "description": (
                "Search the internal knowledge base for relevant information. "
                "Use this tool whenever the user asks a question that may be answered "
                "by the indexed documents."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "A natural language search query",
                    },
                    "top": {
                        "type": "integer",
                        "description": "Number of results to return (default 5)",
                        "default": 5,
                    },
                },
                "required": ["query"],
            },
        },
    }
]

TOOL_IMPLEMENTATIONS = {"search_documents": search_documents}

SYSTEM_PROMPT = (
    "You are a helpful knowledge assistant. "
    "You MUST use the search_documents tool to retrieve relevant context "
    "before answering any factual question. "
    "After retrieving results, synthesize the information and always cite "
    "the source filename (e.g., 'According to azure_openai_overview.txt, …'). "
    "If the search returns no relevant results, say so honestly."
)

MAX_TURNS = 10

# ---------------------------------------------------------------------------
# Agent loop
# ---------------------------------------------------------------------------

def run_agent(messages: list[dict]) -> str:
    """Single agent turn: may call search_documents, then returns final answer."""
    for _ in range(MAX_TURNS):
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
            console.print(f"  [dim][Tool] {func_name}({func_args})[/]")

            if func_name in TOOL_IMPLEMENTATIONS:
                result = TOOL_IMPLEMENTATIONS[func_name](**func_args)
            else:
                result = {"error": f"Unknown tool: {func_name}"}

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": json.dumps(result),
                }
            )

    return "Error: maximum turns reached."


# ---------------------------------------------------------------------------
# Interactive chat
# ---------------------------------------------------------------------------

def main() -> None:
    console.print(Panel(
        "[bold]RAG Knowledge Assistant[/]\n"
        "Powered by Azure AI Search + Azure OpenAI\n"
        "Type [red]exit[/] to quit.",
        title="AgenticOdyssey — Lab 04",
    ))

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        user_input = console.input("\n[bold green]You:[/] ").strip()
        if user_input.lower() in ("exit", "quit", "q"):
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        answer = run_agent(messages)
        console.print(f"\n[bold blue]Assistant:[/] {answer}")
        messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()
