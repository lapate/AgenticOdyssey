"""
Lab 02 — Solution: Research Assistant with Azure OpenAI Assistants API
=======================================================================

Demonstrates:
  - Creating an Assistant with function calling + code interpreter
  - Managing threads (persistent conversation)
  - Handling tool calls in a run loop
  - Streaming responses

Run:
    python labs/lab02-first-agent/solution/assistant_agent.py
    python labs/lab02-first-agent/solution/assistant_agent.py --thread-id <id>
"""

import argparse
import json
import os
import time

from dotenv import load_dotenv
from openai import AzureOpenAI
from openai.types.beta.threads import Run
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()

# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------
client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
)
MODEL = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")

# ---------------------------------------------------------------------------
# Tool: web_search (stub — replace with real Bing call if desired)
# ---------------------------------------------------------------------------
def web_search(query: str, count: int = 5) -> list[dict]:
    """Simulated web search. Replace with Bing Search API for real results."""
    return [
        {
            "title": f"Result {i + 1} for: {query}",
            "url": f"https://example.com/result-{i + 1}",
            "snippet": f"This is a simulated snippet about '{query}' result {i + 1}.",
        }
        for i in range(count)
    ]


TOOL_IMPLEMENTATIONS = {"web_search": web_search}

# ---------------------------------------------------------------------------
# Tool schemas
# ---------------------------------------------------------------------------
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
                    "query": {"type": "string", "description": "The search query"},
                    "count": {
                        "type": "integer",
                        "description": "Number of results to return (default 5)",
                        "default": 5,
                    },
                },
                "required": ["query"],
            },
        },
    },
]

SYSTEM_INSTRUCTIONS = (
    "You are a helpful research assistant. "
    "When asked about recent events or facts you are unsure of, use the web_search tool. "
    "When asked to perform calculations or data analysis, use the code interpreter. "
    "Always cite your sources and explain your reasoning clearly."
)

# ---------------------------------------------------------------------------
# Assistant helpers
# ---------------------------------------------------------------------------

def create_assistant() -> str:
    """Create a new assistant and return its ID."""
    assistant = client.beta.assistants.create(
        name="Research Assistant",
        instructions=SYSTEM_INSTRUCTIONS,
        model=MODEL,
        tools=TOOLS,  # type: ignore[arg-type]
    )
    console.print(f"[dim]Assistant created: {assistant.id}[/]")
    return assistant.id


def get_or_create_thread(thread_id: str | None = None) -> str:
    """Retrieve an existing thread or create a new one."""
    if thread_id:
        thread = client.beta.threads.retrieve(thread_id)
        console.print(f"[dim]Resumed thread: {thread.id}[/]")
    else:
        thread = client.beta.threads.create()
        console.print(f"[dim]New thread: {thread.id}[/]")
    return thread.id


def handle_run(run: Run, thread_id: str) -> Run:
    """Poll the run, handle tool calls, and return the completed run."""
    while run.status in ("queued", "in_progress", "requires_action"):
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)

        if run.status == "requires_action" and run.required_action:
            tool_outputs = []
            for tc in run.required_action.submit_tool_outputs.tool_calls:
                func_name = tc.function.name
                func_args = json.loads(tc.function.arguments)
                console.print(f"[bold yellow][Tool call][/] {func_name}({func_args})")

                if func_name in TOOL_IMPLEMENTATIONS:
                    result = TOOL_IMPLEMENTATIONS[func_name](**func_args)
                else:
                    result = {"error": f"Unknown tool: {func_name}"}

                tool_outputs.append({"tool_call_id": tc.id, "output": json.dumps(result)})

            run = client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread_id,
                run_id=run.id,
                tool_outputs=tool_outputs,
            )
    return run


# ---------------------------------------------------------------------------
# Main conversation loop
# ---------------------------------------------------------------------------

def chat(assistant_id: str, thread_id: str) -> None:
    """Interactive conversation loop."""
    console.print(Panel(
        "[bold]Research Assistant[/] ready.\n"
        f"Thread ID: [cyan]{thread_id}[/]\n"
        "Type [bold red]exit[/] to quit.",
        title="AgenticOdyssey — Lab 02",
    ))

    while True:
        user_input = console.input("\n[bold green]You:[/] ").strip()
        if user_input.lower() in ("exit", "quit", "q"):
            console.print("[dim]Goodbye![/]")
            break
        if not user_input:
            continue

        # Add user message to thread
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_input,
        )

        # Create and execute run
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
        )
        run = handle_run(run, thread_id)

        if run.status != "completed":
            console.print(f"[red]Run ended with status: {run.status}[/]")
            continue

        # Retrieve and print the latest assistant message
        messages = client.beta.threads.messages.list(thread_id=thread_id, limit=1)
        for msg in messages.data:
            if msg.role == "assistant":
                for block in msg.content:
                    if hasattr(block, "text"):
                        console.print(f"\n[bold blue]Assistant:[/] {block.text.value}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Lab 02 — Research Assistant")
    parser.add_argument("--thread-id", help="Resume an existing thread by ID")
    parser.add_argument("--assistant-id", help="Use an existing assistant by ID")
    args = parser.parse_args()

    assistant_id = args.assistant_id or create_assistant()
    thread_id = get_or_create_thread(args.thread_id)

    try:
        chat(assistant_id, thread_id)
    finally:
        if not args.assistant_id:
            client.beta.assistants.delete(assistant_id)
            console.print(f"[dim]Assistant {assistant_id} deleted.[/]")


if __name__ == "__main__":
    main()
