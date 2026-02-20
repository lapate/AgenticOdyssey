# Lab 01: Introduction to AI Agents

## Overview

In this lab you will explore the fundamental concepts behind AI agents — autonomous systems that perceive their environment, reason about it, and take actions to achieve a goal. You will implement the classic **ReAct** (Reason + Act) pattern using Azure OpenAI and a small set of custom tools.

**Duration:** ~30 minutes

---

## Learning Objectives

By the end of this lab you will be able to:

1. Explain what an AI agent is and how it differs from a simple chatbot
2. Describe the **ReAct** (Thought → Action → Observation) loop
3. Define tools (functions) that an agent can call
4. Trace through an agent's reasoning steps in the output
5. Identify when to use an agent versus a single LLM call

---

## Prerequisites

- Completed [environment setup](../../docs/SETUP.md)
- Python virtual environment activated
- `.env` file configured with Azure OpenAI credentials

---

## Background: What Is an AI Agent?

A **chatbot** takes a user message and returns a response — one turn, no external actions.

An **AI agent** goes further: it has access to **tools** (functions, APIs, databases), and it can decide *which tools to call*, *in what order*, and *when to stop* — all driven by the LLM reasoning over its own intermediate outputs.

```
User Goal
    │
    ▼
┌────────────────────────────────┐
│           Agent Loop           │
│                                │
│  Thought → Action → Observation│
│       ↑________________________│
└────────────────────────────────┘
    │
    ▼
Final Answer
```

The **ReAct** pattern (Yao et al., 2022) interleaves *reasoning* traces and *acting* steps, giving agents the ability to plan, correct mistakes, and incorporate new information.

---

## Step 1: Explore the Starter Code

Open `solution/react_agent.py` and read through the file before running it. Notice:

- **Tool definitions** — Python functions decorated with a simple schema
- **System prompt** — instructs the model to follow the Thought/Action/Observation format
- **Agent loop** — calls the model, parses its response, calls a tool if requested, feeds the observation back, and repeats

---

## Step 2: Run the Agent

```bash
cd labs/lab01-intro-to-agents
python solution/react_agent.py
```

You should see output like:

```
🤖 Agent starting…

[Thought] I need to find the current weather in Seattle, then convert the temperature to Fahrenheit.
[Action]  get_weather(city="Seattle")
[Obs]     {"city": "Seattle", "temp_c": 12, "condition": "Overcast"}

[Thought] Temperature is 12°C. I'll convert that to Fahrenheit: 12 * 9/5 + 32 = 53.6°F
[Action]  calculate(expression="12 * 9/5 + 32")
[Obs]     53.6

[Thought] I now have all the information needed.
[Answer]  The current weather in Seattle is Overcast and 12°C (53.6°F).
```

---

## Step 3: Add a New Tool

The agent currently has two tools: `get_weather` and `calculate`. Add a third tool called `get_time` that returns the current UTC time.

1. Open `solution/react_agent.py`
2. Add a `get_time` function following the existing pattern
3. Register it in the `TOOLS` dictionary
4. Update the system prompt to mention the new tool
5. Change the user goal to ask: *"What is the current time in UTC, and what will the temperature in London be?"*

> 💡 **Hint:** Use `datetime.utcnow()` from Python's `datetime` module.

---

## Step 4: Observe Multi-Step Reasoning

Ask the agent a question that requires multiple tool calls:

```python
USER_GOAL = (
    "What is the weather in Tokyo and Paris? "
    "Which city is warmer, and by how many degrees Celsius?"
)
```

Trace through the output and answer:
- How many tool calls did the agent make?
- Did it plan ahead, or discover the next step after each observation?
- What happens if you remove the `calculate` tool from the TOOLS dictionary?

---

## Key Takeaways

| Concept | Description |
|---------|-------------|
| **Tool / Function** | A Python function the LLM can call by name |
| **Thought** | The model's reasoning before taking an action |
| **Action** | A tool call with arguments |
| **Observation** | The tool's return value, fed back to the model |
| **Agent Loop** | Repeat Thought → Action → Obs until a final answer is reached |

---

## Next Steps

Proceed to **[Lab 02: Building Your First Agent](../lab02-first-agent/README.md)** to build a production-ready agent using the Azure OpenAI Assistants API with persistent memory and file tools.
