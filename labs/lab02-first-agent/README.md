# Lab 02: Building Your First Agent

## Overview

In this lab you will build a **personal research assistant** agent using the Azure OpenAI **Assistants API**. Unlike the basic ReAct loop from Lab 01, the Assistants API provides built-in thread management (persistent memory), a code interpreter tool, and file handling — giving you a production-ready agent foundation with minimal boilerplate.

**Duration:** ~45 minutes

---

## Learning Objectives

By the end of this lab you will be able to:

1. Create and configure an Azure OpenAI Assistant
2. Add tools: **function calling**, **code interpreter**, and **file search**
3. Manage conversation threads (persistent context)
4. Run an assistant and stream its responses
5. Clean up assistant resources programmatically

---

## Prerequisites

- Completed [Lab 01](../lab01-intro-to-agents/README.md)
- Azure OpenAI resource with `gpt-4o` deployment
- `.env` configured (see [Setup Guide](../../docs/SETUP.md))

---

## Background: Azure OpenAI Assistants API

The **Assistants API** abstracts the agent loop for you:

```
Thread (persistent history)
    │
    ▼
Run (invoke the assistant on the thread)
    │
    ├── Function calls → your code handles them → returns results
    ├── Code interpreter → Azure executes Python in a sandbox
    └── File search → Azure searches uploaded documents
    │
    ▼
Message (assistant's reply added to thread)
```

Key concepts:

| Resource | Description |
|----------|-------------|
| **Assistant** | A configured AI with instructions, model, and tools |
| **Thread** | A persistent conversation history |
| **Message** | A single turn in a thread |
| **Run** | An invocation of the assistant on a thread |

---

## Step 1: Create the Assistant

Open `solution/assistant_agent.py` and run it:

```bash
cd labs/lab02-first-agent
python solution/assistant_agent.py
```

The script creates a research assistant that can:
- Answer questions using its built-in knowledge
- Execute Python code via the code interpreter
- Call a custom `web_search` stub (you'll make it real in Step 3)

---

## Step 2: Understand Thread Persistence

After the first run, the script prints the **Thread ID**. Run the script again, passing the thread ID as an argument to continue the same conversation:

```bash
python solution/assistant_agent.py --thread-id <thread_id_from_above>
```

Notice the assistant remembers the previous conversation — this is thread persistence in action.

---

## Step 3: Connect a Real Web Search Tool

The starter code (`starter/assistant_agent.py`) has a `web_search` function that returns placeholder data. Your task is to implement it using the Bing Search REST API.

1. Add your `BING_SEARCH_API_KEY` to `.env`
2. Open `starter/assistant_agent.py`
3. Implement the `web_search` function:

```python
def web_search(query: str, count: int = 5) -> list[dict]:
    """Search the web using Bing Search API."""
    # TODO: Implement using requests + Bing Search v7 API
    # Endpoint: https://api.bing.microsoft.com/v7.0/search
    # Headers: {"Ocp-Apim-Subscription-Key": BING_SEARCH_API_KEY}
    # Params:  {"q": query, "count": count, "mkt": "en-US"}
    # Return:  list of {"title": ..., "url": ..., "snippet": ...}
    raise NotImplementedError
```

4. Run and verify the agent now returns real search results.

---

## Step 4: Upload a File and Use File Search

1. Create a text file `my_notes.txt` with a few paragraphs about a topic you're interested in
2. Uncomment the file-upload block in `solution/assistant_agent.py`
3. Ask the assistant a question that requires reading from the file
4. Observe how the assistant cites the file in its response

---

## Key Takeaways

| Feature | Benefit |
|---------|---------|
| Thread persistence | No manual history management |
| Code interpreter | Safe Python execution in the cloud |
| File search | Grounding on your documents without a separate RAG pipeline |
| Streaming | Real-time token-by-token responses |

---

## Next Steps

Proceed to **[Lab 03: Multi-Agent Orchestration](../lab03-multi-agent/README.md)** to coordinate multiple specialized agents using the AutoGen framework.
