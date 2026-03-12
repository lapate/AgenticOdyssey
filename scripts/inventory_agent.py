#!/usr/bin/env python3
from __future__ import annotations

import logging
import os
import sys

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    MCPTool,
    PromptAgentDefinition,
    Tool
)
from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# ─── Configuration ────────────────────────────────────────────────────────────

_PROJECT_ENDPOINT = os.getenv("AZURE_AI_PROJECT_ENDPOINT", "")
_MODEL = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
_MCP_URL = os.getenv("MCP_URL")

# Fixed logical name — used to look up an existing registration before creating.
_AGENT_NAME = "ZavaGroceriesInventoryAgent"

# ─── System Prompt ────────────────────────────────────────────────────────────

_SYSTEM_PROMPT = """\
You are ZavaGroceriesInventoryAgent, an AI assistant for Zava Groceries.

You have access to live store data through a set of tools. You can:
- Look up daily financial records (chickens bought, sold, revenue, profit) by date and store
- Look up hourly sales data (chickens cooked and sold by hour) by date, store, and hour
- Create new records when inventory is received or sales are logged
- Update existing records to correct errors or reflect adjustments
- Delete records that were entered in error

When answering questions:
- Always use the tools to retrieve live data — never make up numbers
- When asked about a specific store or date, filter your queries accordingly
- Present financial figures clearly, using USD formatting where appropriate
- If asked to make a change, confirm the record ID and the new values before updating
- Be concise but complete in your responses

Available stores: Store-001
"""

# ─── Client Construction ──────────────────────────────────────────────────────


def _build_client() -> AIProjectClient:
    """Create an AIProjectClient (azure-ai-projects>=2.0.0b1).

    Authenticates with DefaultAzureCredential (``az login`` or managed
    identity).  The endpoint must be the full Foundry *project* URL:
      https://<hub>.services.ai.azure.com/api/projects/<project-name>
    """
    if not _PROJECT_ENDPOINT:
        raise EnvironmentError(
            "AZURE_AI_PROJECT_ENDPOINT is not set. "
            "Set it to your Foundry project endpoint URL, e.g. "
            "https://<hub>.services.ai.azure.com/api/projects/<project-name>"
        )
    return AIProjectClient(
        endpoint=_PROJECT_ENDPOINT,
        credential=DefaultAzureCredential(),
    )


# ─── Tool Construction ────────────────────────────────────────────────────────


def _build_tools() -> list[Tool]:
    """Assemble the tool list to attach to the PromptAgentDefinition.

    In azure-ai-projects>=2.0.0b1, tools are a plain list[Tool] rather than a
    ToolSet object.  The two tools used here are:

    - BingGroundingAgentTool – live web search for current Azure guidance,
      wired to the Bing connection provisioned in the Foundry hub.
    - MCPTool – structured Microsoft Learn content via the MCP endpoint.
    """
    tools: list[Tool] = []

    tools.append(
        MCPTool(
            server_label="inventory-mcp",
            server_url=_MCP_URL,
            require_approval="never",  
        )
    )
    logger.info("MCP tool enabled (url: %s)", _MCP_URL)

    return tools


# ─── Agent Registration ───────────────────────────────────────────────────────


def get_or_create_agent(client: AIProjectClient) -> str:
    """Return the Foundry agent ID for this session (azure-ai-projects>=2.0.0b1).

    Looks up the agent by its fixed logical name first.  If it exists the
    current definition (model, instructions, tools) is updated in-place so
    that re-running the script always keeps the registration in sync with the
    code.  If the agent does not yet exist it is created fresh.

    Returns the agent's ID, which is used as the ``model`` parameter when
    invoking via the OpenAI Responses API.
    """
    tools = _build_tools()
    definition = PromptAgentDefinition(
        model=_MODEL,
        instructions=_SYSTEM_PROMPT,
        tools=tools,
    )

    try:
        existing = client.agents.get(agent_name=_AGENT_NAME)
        logger.info("Found existing Foundry agent '%s' (id: %s) — updating.", _AGENT_NAME, existing.id)
        agent = client.agents.update(
            agent_name=_AGENT_NAME,
            definition=definition,
        )
        logger.info("Foundry agent updated: %s", agent.id)
        return agent.id
    except HttpResponseError as exc:
        if exc.status_code != 404:
            raise

    logger.info("Registering new Foundry agent '%s' (model: %s)…", _AGENT_NAME, _MODEL)
    agent = client.agents.create(
        name=_AGENT_NAME,
        definition=definition,
    )
    logger.info("Foundry agent created: %s", agent.id)
    return agent.id

# ─── Entry Point ──────────────────────────────────────────────────────────────


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    client = _build_client()
    agent_id = get_or_create_agent(client)

    print()
    print(f"  Foundry Agent     : {_AGENT_NAME}")
    print(f"  Foundry Agent ID  : {agent_id}")
    print()

if __name__ == "__main__":
    main()