"""
Lab 03 — Solution: Multi-Agent Orchestration with AutoGen
==========================================================

Demonstrates a four-agent team (Planner, Researcher, Coder, Critic) working
together in a GroupChat powered by Azure OpenAI.

Run:
    python labs/lab03-multi-agent/solution/multi_agent_team.py
"""

import os

from autogen import AssistantAgent, GroupChat, GroupChatManager, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Azure OpenAI config for AutoGen
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

planner = AssistantAgent(
    name="Planner",
    system_message=(
        "You are a strategic planner. When given a task, decompose it into "
        "clear subtasks and delegate them to the appropriate specialist: "
        "Researcher for information gathering, Coder for implementation, "
        "and Critic for review. Coordinate the team toward a final answer. "
        "When the task is fully resolved, end your message with 'TERMINATE'."
    ),
    llm_config=LLM_CONFIG,
)

researcher = AssistantAgent(
    name="Researcher",
    system_message=(
        "You are an expert researcher. Your role is to gather, synthesize, and "
        "present accurate information relevant to the task. Cite facts clearly "
        "and flag uncertainty when you are unsure. Do not write code."
    ),
    llm_config=LLM_CONFIG,
)

coder = AssistantAgent(
    name="Coder",
    system_message=(
        "You are a senior Python developer. Write clean, well-commented Python code "
        "to solve the coding subtasks assigned by the Planner. "
        "Always include a brief explanation of what the code does. "
        "Format code inside ```python ... ``` blocks."
    ),
    llm_config=LLM_CONFIG,
)

critic = AssistantAgent(
    name="Critic",
    system_message=(
        "You are a rigorous quality reviewer. Review the work produced by other agents. "
        "Point out errors, ambiguities, or missing edge cases. "
        "Provide specific, actionable feedback. "
        "When you are satisfied with the final output, say 'LGTM' (Looks Good To Me)."
    ),
    llm_config=LLM_CONFIG,
)

# Human proxy — set human_input_mode="NEVER" to run fully autonomously,
# or "TERMINATE" to only ask for input when TERMINATE is received.
human_proxy = UserProxyAgent(
    name="Human",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=0,
    code_execution_config=False,
)

# ---------------------------------------------------------------------------
# Group chat
# ---------------------------------------------------------------------------
group_chat = GroupChat(
    agents=[human_proxy, planner, researcher, coder, critic],
    messages=[],
    max_round=15,
    speaker_selection_method="auto",
)

manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=LLM_CONFIG,
)

# ---------------------------------------------------------------------------
# Task
# ---------------------------------------------------------------------------
TASK = (
    "Write a Python function that takes a list of integers and returns "
    "the top-3 most frequent elements. Include docstring, type hints, "
    "and at least two unit tests using pytest."
)

if __name__ == "__main__":
    print(f"\n{'='*60}")
    print("AgenticOdyssey — Lab 03: Multi-Agent Orchestration")
    print(f"{'='*60}\n")
    print(f"Task: {TASK}\n")

    human_proxy.initiate_chat(
        manager,
        message=TASK,
    )
