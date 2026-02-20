"""
Demo 02: Multi-Agent Research Pipeline
=======================================

A four-agent pipeline (Orchestrator → Researcher → Fact Checker → Writer → Editor)
that produces a structured Markdown research brief for any topic.

Run:
    python demos/demo02-research-pipeline/research_pipeline.py
    python demos/demo02-research-pipeline/research_pipeline.py --topic "Your topic"

Requirements:
    pip install pyautogen
    .env with Azure OpenAI credentials
"""

import argparse
import os
from datetime import datetime, timezone
from pathlib import Path

from autogen import AssistantAgent, GroupChat, GroupChatManager, UserProxyAgent
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
    "temperature": 0.2,
}

# ---------------------------------------------------------------------------
# Agents
# ---------------------------------------------------------------------------

orchestrator = AssistantAgent(
    name="Orchestrator",
    system_message=(
        "You are the research orchestrator. When given a topic:\n"
        "1. Break it into 3–4 distinct research angles.\n"
        "2. Ask the Researcher to investigate each angle.\n"
        "3. After the Researcher reports, ask the FactChecker to verify key claims.\n"
        "4. Once fact-checking is done, ask the Writer to draft the brief.\n"
        "5. Finally, ask the Editor to polish it.\n"
        "6. When the Editor finishes, output the final brief between "
        "   <brief> and </brief> tags, then say 'TERMINATE'."
    ),
    llm_config=LLM_CONFIG,
)

researcher = AssistantAgent(
    name="Researcher",
    system_message=(
        "You are an expert researcher with broad knowledge. "
        "When asked to research a topic or angle:\n"
        "- Provide key facts, statistics, and insights.\n"
        "- Note the recency of information (pre/post your training cutoff).\n"
        "- Be thorough but concise — bullet points preferred.\n"
        "Do not fabricate specific statistics; flag uncertain data as '(unverified)'."
    ),
    llm_config=LLM_CONFIG,
)

fact_checker = AssistantAgent(
    name="FactChecker",
    system_message=(
        "You are a rigorous fact-checker. Review the Researcher's findings:\n"
        "- Identify any claims that are likely inaccurate or unverifiable.\n"
        "- Mark verified facts as ✅ and questionable claims as ⚠️.\n"
        "- Suggest corrections where possible.\n"
        "Be skeptical but fair."
    ),
    llm_config=LLM_CONFIG,
)

writer = AssistantAgent(
    name="Writer",
    system_message=(
        "You are a professional technical writer. Using the research and fact-check notes:\n"
        "Draft a structured research brief in Markdown with these sections:\n"
        "1. Executive Summary\n"
        "2. Key Findings\n"
        "3. Analysis\n"
        "4. Recommendations\n"
        "Write in clear, professional prose. Target audience: senior technical managers."
    ),
    llm_config=LLM_CONFIG,
)

editor = AssistantAgent(
    name="Editor",
    system_message=(
        "You are a senior editor. Review the Writer's draft:\n"
        "- Fix grammar, clarity, and flow issues.\n"
        "- Ensure consistent tone (professional, objective).\n"
        "- Add a one-paragraph 'Executive Summary' if missing.\n"
        "Output the FINAL polished brief in its entirety."
    ),
    llm_config=LLM_CONFIG,
)

human_proxy = UserProxyAgent(
    name="Human",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=0,
    is_termination_msg=lambda msg: "TERMINATE" in (msg.get("content") or ""),
    code_execution_config=False,
)

# ---------------------------------------------------------------------------
# Group chat
# ---------------------------------------------------------------------------
group_chat = GroupChat(
    agents=[human_proxy, orchestrator, researcher, fact_checker, writer, editor],
    messages=[],
    max_round=20,
    speaker_selection_method="auto",
)
manager = GroupChatManager(groupchat=group_chat, llm_config=LLM_CONFIG)

# ---------------------------------------------------------------------------
# Output extraction
# ---------------------------------------------------------------------------

def extract_brief(chat_messages: list[dict]) -> str | None:
    """Extract the final brief from between <brief> ... </brief> tags."""
    for msg in reversed(chat_messages):
        content = msg.get("content") or ""
        if "<brief>" in content and "</brief>" in content:
            start = content.index("<brief>") + len("<brief>")
            end = content.index("</brief>")
            return content[start:end].strip()
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_pipeline(topic: str) -> None:
    print(f"\n{'='*60}")
    print("AgenticOdyssey — Demo 02: Multi-Agent Research Pipeline")
    print(f"{'='*60}")
    print(f"\nTopic: {topic}\n")
    print("="*60 + "\n")

    human_proxy.initiate_chat(
        manager,
        message=(
            f"Please research the following topic and produce a comprehensive brief:\n\n"
            f"**{topic}**"
        ),
    )

    # Save the brief to a file
    brief = extract_brief(group_chat.messages)
    if brief:
        timestamp = datetime.now(tz=timezone.utc).strftime("%Y%m%d_%H%M%S")
        output_path = Path(f"research_brief_{timestamp}.md")
        output_path.write_text(
            f"# Research Brief: {topic}\n\n"
            f"*Generated by AgenticOdyssey Demo 02 — {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}*\n\n"
            f"{brief}\n",
            encoding="utf-8",
        )
        print(f"\n✅ Research brief saved to: {output_path.resolve()}")
    else:
        print("\n⚠️  Could not extract formatted brief from conversation.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demo 02 — Multi-Agent Research Pipeline")
    parser.add_argument(
        "--topic",
        default="The rise of agentic AI: patterns, frameworks, and real-world applications in 2025",
        help="Research topic",
    )
    args = parser.parse_args()
    run_pipeline(args.topic)
