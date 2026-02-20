"""
Lab 01 — Solution: ReAct Agent with Tool Use
=============================================

This script implements a minimal ReAct (Reason + Act) agent using Azure OpenAI
function calling.  The agent is given a set of tools and a user goal, and it
loops until it either produces a final answer or exceeds MAX_STEPS.

Run:
    python labs/lab01-intro-to-agents/solution/react_agent.py
"""

import json
import os
import sys
from typing import Any

from dotenv import load_dotenv
from openai import AzureOpenAI
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()

# ---------------------------------------------------------------------------
# Azure OpenAI client
# ---------------------------------------------------------------------------
client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
)
MODEL = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")

# ---------------------------------------------------------------------------
# Tool implementations
# ---------------------------------------------------------------------------

def get_weather(city: str) -> dict[str, Any]:
    """Return simulated current weather for a city."""
    # Simulated data — replace with a real weather API call if desired.
    weather_db: dict[str, dict[str, Any]] = {
        "seattle":  {"city": "Seattle",  "temp_c": 12, "condition": "Overcast"},
        "tokyo":    {"city": "Tokyo",    "temp_c": 28, "condition": "Sunny"},
        "paris":    {"city": "Paris",    "temp_c": 18, "condition": "Partly cloudy"},
        "london":   {"city": "London",   "temp_c": 15, "condition": "Rainy"},
        "new york": {"city": "New York", "temp_c": 22, "condition": "Clear"},
    }
    return weather_db.get(city.lower(), {"city": city, "temp_c": None, "condition": "Unknown"})


def calculate(expression: str) -> float | str:
    """Safely evaluate a simple arithmetic expression and return the result."""
    # Allow only numbers and basic operators to prevent code injection.
    allowed = set("0123456789+-*/(). ")
    if not all(c in allowed for c in expression):
        return "Error: expression contains disallowed characters."
    try:
        return eval(expression, {"__builtins__": {}})  # noqa: S307
    except Exception as exc:  # noqa: BLE001
        return f"Error: {exc}"


# ---------------------------------------------------------------------------
# Tool registry (name → implementation)
# ---------------------------------------------------------------------------
TOOLS: dict[str, Any] = {
    "get_weather": get_weather,
    "calculate": calculate,
}

# OpenAI function schemas
TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather conditions for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "The city name, e.g. 'Seattle'"},
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a simple arithmetic expression and return the numeric result.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A valid Python arithmetic expression, e.g. '12 * 9/5 + 32'",
                    },
                },
                "required": ["expression"],
            },
        },
    },
]

# ---------------------------------------------------------------------------
# Agent loop
# ---------------------------------------------------------------------------
MAX_STEPS = 10
SYSTEM_PROMPT = (
    "You are a helpful AI agent. You have access to tools to help you answer questions. "
    "Think step-by-step. Use the tools as needed. When you have a final answer, "
    "reply with ONLY the answer — do not call any more tools."
)


def run_agent(user_goal: str) -> str:
    """Run the ReAct agent loop until a final answer is produced."""
    console.print(Panel(f"[bold cyan]User Goal:[/] {user_goal}", expand=False))
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_goal},
    ]

    for step in range(1, MAX_STEPS + 1):
        console.print(f"\n[dim]── Step {step} ──[/]")

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOL_SCHEMAS,
            tool_choice="auto",
        )
        msg = response.choices[0].message

        # No tool call → final answer
        if not msg.tool_calls:
            answer = msg.content or ""
            console.print(f"[bold green][Answer][/] {answer}")
            return answer

        # Process each tool call
        messages.append(msg)  # type: ignore[arg-type]
        for tc in msg.tool_calls:
            func_name = tc.function.name
            func_args = json.loads(tc.function.arguments)

            console.print(f"[bold yellow][Action][/]  {func_name}({func_args})")

            if func_name in TOOLS:
                result = TOOLS[func_name](**func_args)
            else:
                result = f"Error: unknown tool '{func_name}'"

            console.print(f"[bold blue][Obs][/]     {result}")

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": json.dumps(result),
                }
            )

    return "Error: maximum steps reached without a final answer."


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    goal = (
        sys.argv[1]
        if len(sys.argv) > 1
        else (
            "What is the weather in Seattle? "
            "Convert the temperature to Fahrenheit and tell me the full weather report."
        )
    )
    run_agent(goal)
