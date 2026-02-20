"""
Lab 03 — Starter: Multi-Agent Orchestration with AutoGen
=========================================================

Your tasks:
  1. Fill in the system_message for the Researcher and Critic agents (see TODOs).
  2. Add a fifth agent: "Documenter" that writes markdown documentation
     for any code produced by the Coder.
  3. Register the Documenter in the GroupChat agents list.

See README.md for details.
"""

import os

from autogen import AssistantAgent, GroupChat, GroupChatManager, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

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

# Planner is done for you
planner = AssistantAgent(
    name="Planner",
    system_message=(
        "You are a strategic planner. Decompose the task and coordinate the team. "
        "When the task is fully resolved, end with 'TERMINATE'."
    ),
    llm_config=LLM_CONFIG,
)

# TODO: Fill in a meaningful system_message for the Researcher
researcher = AssistantAgent(
    name="Researcher",
    system_message="TODO",  # Replace with your system message
    llm_config=LLM_CONFIG,
)

coder = AssistantAgent(
    name="Coder",
    system_message=(
        "You are a senior Python developer. Write clean, well-commented code. "
        "Format code inside ```python ... ``` blocks."
    ),
    llm_config=LLM_CONFIG,
)

# TODO: Fill in a meaningful system_message for the Critic
critic = AssistantAgent(
    name="Critic",
    system_message="TODO",  # Replace with your system message
    llm_config=LLM_CONFIG,
)

# TODO: Create a "Documenter" AssistantAgent that writes markdown docs for code

human_proxy = UserProxyAgent(
    name="Human",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=0,
    code_execution_config=False,
)

# TODO: Add your Documenter to the agents list below
group_chat = GroupChat(
    agents=[human_proxy, planner, researcher, coder, critic],
    messages=[],
    max_round=15,
    speaker_selection_method="auto",
)

manager = GroupChatManager(groupchat=group_chat, llm_config=LLM_CONFIG)

TASK = (
    "Write a Python function that takes a list of integers and returns "
    "the top-3 most frequent elements. Include docstring, type hints, "
    "and at least two unit tests using pytest."
)

if __name__ == "__main__":
    human_proxy.initiate_chat(manager, message=TASK)
