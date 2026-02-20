"""
Lab 02 — Starter: Research Assistant with Azure OpenAI Assistants API
======================================================================

Your task:
  1. Implement the `web_search` function using the Bing Search REST API.
  2. (Optional) Add a `get_stock_price` tool that returns mock stock prices.
  3. Run and verify the assistant uses your new tools.

See README.md for detailed instructions.
"""

import argparse
import json
import os
import time

import requests  # noqa: F401  (used in your web_search implementation)
from dotenv import load_dotenv
from openai import AzureOpenAI
from openai.types.beta.threads import Run
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
)
MODEL = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")

# ---------------------------------------------------------------------------
# TODO: Implement web_search
# ---------------------------------------------------------------------------

def web_search(query: str, count: int = 5) -> list[dict]:
    """Search the web using Bing Search API.

    Instructions:
        - Use requests to call https://api.bing.microsoft.com/v7.0/search
        - Pass the header: {"Ocp-Apim-Subscription-Key": os.getenv("BING_SEARCH_API_KEY")}
        - Pass params: {"q": query, "count": count, "mkt": "en-US"}
        - Parse the response and return a list of dicts with keys:
            "title", "url", "snippet"
    """
    # TODO: Replace this with your implementation
    raise NotImplementedError("Implement web_search using the Bing Search API")


# ---------------------------------------------------------------------------
# Tool registry and schemas — update if you add new tools
# ---------------------------------------------------------------------------
TOOL_IMPLEMENTATIONS = {"web_search": web_search}

TOOLS = [
    {"type": "code_interpreter"},
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for up-to-date information on a topic.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "count": {"type": "integer", "default": 5},
                },
                "required": ["query"],
            },
        },
    },
]

SYSTEM_INSTRUCTIONS = (
    "You are a helpful research assistant. "
    "Use web_search for recent information. "
    "Use the code interpreter for calculations and data analysis."
)


# ---------------------------------------------------------------------------
# Helper functions (already implemented — do not modify)
# ---------------------------------------------------------------------------

def create_assistant() -> str:
    assistant = client.beta.assistants.create(
        name="Research Assistant (Starter)",
        instructions=SYSTEM_INSTRUCTIONS,
        model=MODEL,
        tools=TOOLS,  # type: ignore[arg-type]
    )
    return assistant.id


def get_or_create_thread(thread_id: str | None = None) -> str:
    if thread_id:
        return client.beta.threads.retrieve(thread_id).id
    return client.beta.threads.create().id


def handle_run(run: Run, thread_id: str) -> Run:
    while run.status in ("queued", "in_progress", "requires_action"):
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        if run.status == "requires_action" and run.required_action:
            tool_outputs = []
            for tc in run.required_action.submit_tool_outputs.tool_calls:
                func_name = tc.function.name
                func_args = json.loads(tc.function.arguments)
                result = TOOL_IMPLEMENTATIONS[func_name](**func_args) if func_name in TOOL_IMPLEMENTATIONS else {"error": f"Unknown: {func_name}"}
                tool_outputs.append({"tool_call_id": tc.id, "output": json.dumps(result)})
            run = client.beta.threads.runs.submit_tool_outputs(thread_id=thread_id, run_id=run.id, tool_outputs=tool_outputs)
    return run


def chat(assistant_id: str, thread_id: str) -> None:
    console.print(Panel(f"Thread: [cyan]{thread_id}[/]  |  Type [red]exit[/] to quit.", title="Lab 02 Starter"))
    while True:
        user_input = console.input("\n[green]You:[/] ").strip()
        if user_input.lower() in ("exit", "quit", "q"):
            break
        if not user_input:
            continue
        client.beta.threads.messages.create(thread_id=thread_id, role="user", content=user_input)
        run = handle_run(client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id), thread_id)
        if run.status == "completed":
            for msg in client.beta.threads.messages.list(thread_id=thread_id, limit=1).data:
                if msg.role == "assistant":
                    for block in msg.content:
                        if hasattr(block, "text"):
                            console.print(f"\n[blue]Assistant:[/] {block.text.value}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--thread-id")
    args = parser.parse_args()
    assistant_id = create_assistant()
    thread_id = get_or_create_thread(args.thread_id)
    try:
        chat(assistant_id, thread_id)
    finally:
        client.beta.assistants.delete(assistant_id)


if __name__ == "__main__":
    main()
