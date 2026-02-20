"""
Demo 01: Autonomous Coding Agent
=================================

Demonstrates a two-agent AutoGen system where a Coder LLM writes Python code
and tests, and a UserProxyAgent executes them.  The agents iterate until all
tests pass, showcasing a self-healing code-generation loop.

Run:
    python demos/demo01-coding-agent/coding_agent.py
    python demos/demo01-coding-agent/coding_agent.py --task "Your custom task"

Requirements:
    pip install pyautogen
    .env with Azure OpenAI credentials
"""

import argparse
import os

from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
LLM_CONFIG = {
    "config_list": [
        {
            "model": os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o"),
            "api_type": "azure",
            "azure_endpoint": os.environ["AZURE_OPENAI_ENDPOINT"],
            "api_key": os.environ["AZURE_OPENAI_API_KEY"],
            "api_version": os.environ.get("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
        }
    ],
    "temperature": 0.1,
}

# ---------------------------------------------------------------------------
# Agents
# ---------------------------------------------------------------------------
coder = AssistantAgent(
    name="Coder",
    system_message=(
        "You are an expert Python developer. When given a coding task:\n"
        "1. First explain your approach in 2-3 sentences.\n"
        "2. Write the implementation in a ```python ... ``` block.\n"
        "3. Write pytest unit tests (including edge cases) in a second ```python ... ``` block.\n"
        "   The test file must be named `test_solution.py`.\n"
        "4. If the executor reports test failures, read the error carefully and provide a fix.\n"
        "When all tests pass and the Reviewer approves, end your message with 'TERMINATE'."
    ),
    llm_config=LLM_CONFIG,
)

reviewer = AssistantAgent(
    name="Reviewer",
    system_message=(
        "You are a senior Python code reviewer. After the Executor confirms all tests pass:\n"
        "1. Check for missing type hints, docstrings, and PEP 8 violations.\n"
        "2. Suggest any improvements.\n"
        "3. If the code is acceptable, say 'LGTM — TERMINATE' to end the session."
    ),
    llm_config=LLM_CONFIG,
)

# UserProxyAgent acts as the executor: runs code blocks and relays output
executor = UserProxyAgent(
    name="Executor",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda msg: "TERMINATE" in (msg.get("content") or ""),
    code_execution_config={
        "work_dir": "/tmp/coding_agent_workspace",
        "use_docker": False,   # Set True if Docker is available for isolation
    },
)

# ---------------------------------------------------------------------------
# Default task
# ---------------------------------------------------------------------------
DEFAULT_TASK = (
    "Implement a Python module `solution.py` with a function:\n\n"
    "    def top_k_frequent(nums: list[int], k: int) -> list[int]:\n"
    "        ...\n\n"
    "The function returns the k most frequent integers from the list `nums`. "
    "If two elements have the same frequency, return the one with the lower value first. "
    "Include a complete docstring with examples. "
    "Then write `test_solution.py` with at least 4 pytest test cases covering "
    "normal inputs, ties, k=1, and an empty list."
)


def run_demo(task: str) -> None:
    print(f"\n{'='*60}")
    print("AgenticOdyssey — Demo 01: Autonomous Coding Agent")
    print(f"{'='*60}")
    print(f"\nTask:\n{task}\n")
    print("="*60 + "\n")

    # The executor initiates the conversation and triggers the Coder
    executor.initiate_chat(
        coder,
        message=task,
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demo 01 — Autonomous Coding Agent")
    parser.add_argument("--task", default=DEFAULT_TASK, help="The coding task to solve")
    args = parser.parse_args()
    run_demo(args.task)
