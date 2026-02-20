# Lab 03: Multi-Agent Orchestration with AutoGen

## Overview

In this lab you will use **Microsoft AutoGen** to build a team of specialized AI agents that collaborate to solve problems. You'll create a **planner**, a **researcher**, a **coder**, and a **critic** — each with a distinct role — and orchestrate them in a group conversation.

**Duration:** ~60 minutes

---

## Learning Objectives

By the end of this lab you will be able to:

1. Describe the difference between a single agent and a multi-agent system
2. Create specialized agents with distinct system prompts in AutoGen
3. Configure a `GroupChat` with custom speaker selection logic
4. Observe agents debating, correcting each other, and reaching consensus
5. Implement human-in-the-loop approval before executing generated code

---

## Prerequisites

- Completed [Lab 02](../lab02-first-agent/README.md)
- `pyautogen` installed (included in `requirements.txt`)
- `.env` configured with Azure OpenAI credentials

---

## Background: Why Multi-Agent?

Single agents work well for simple tasks, but complex workflows benefit from **specialization** and **checks-and-balances**:

```
User Request
      │
      ▼
  ┌───────────┐      ┌────────────┐      ┌───────────┐
  │  Planner  │─────▶│ Researcher │─────▶│   Coder   │
  └───────────┘      └────────────┘      └─────┬─────┘
        ▲                                       │
        │              ┌────────────┐           │
        └──────────────│   Critic   │◀──────────┘
                       └────────────┘
```

Each agent sees the full conversation history, contributing its specialized perspective until the group reaches a satisfactory result.

---

## Agent Roles

| Agent | Role | Behavior |
|-------|------|----------|
| **Planner** | Decomposes the task | Breaks the user goal into subtasks; assigns work to others |
| **Researcher** | Gathers information | Searches (or recalls) relevant facts; cites sources |
| **Coder** | Writes and runs code | Produces Python solutions; explains the code |
| **Critic** | Reviews and improves | Identifies flaws, suggests improvements, approves final output |

---

## Step 1: Run the Multi-Agent Team

```bash
cd labs/lab03-multi-agent
python solution/multi_agent_team.py
```

Observe how agents take turns and how the conversation converges to a solution.

---

## Step 2: Change the Task

Edit the `TASK` variable in `solution/multi_agent_team.py`:

```python
TASK = (
    "Analyze the sales data in the CSV below and produce: "
    "(1) a summary of key trends, "
    "(2) Python code to visualize total sales by month, "
    "(3) three actionable recommendations.\n\n"
    "Data (month,sales):\n"
    "Jan,42000\nFeb,38000\nMar,51000\nApr,47000\nMay,55000\nJun,62000"
)
```

Run again and observe how each agent adapts to the new task.

---

## Step 3: Add a Human Proxy

AutoGen supports a `UserProxyAgent` that pauses the conversation and asks for your input before executing code. Uncomment the `human_proxy` block in `solution/multi_agent_team.py` and re-run.

When the Coder produces code, you will be prompted:
```
Human proxy — do you approve running this code? (yes/no):
```

This pattern is essential for production systems where autonomous code execution must be gated.

---

## Step 4: Implement the Starter

Open `starter/multi_agent_team.py`. Several agent definitions are incomplete (marked with `# TODO`). Fill them in and run the starter to verify your implementation matches the solution output.

---

## Key Takeaways

| Concept | Description |
|---------|-------------|
| **GroupChat** | AutoGen construct for multi-agent conversations |
| **Speaker selection** | Who speaks next (round-robin, auto, or custom) |
| **UserProxyAgent** | A human-in-the-loop agent that can execute code |
| **Termination condition** | When to stop the conversation (`TERMINATE` keyword) |

---

## Next Steps

Proceed to **[Lab 04: RAG-Powered Agents](../lab04-rag-agents/README.md)** to ground your agents in your own documents using Azure AI Search.
