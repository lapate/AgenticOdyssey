# Demo 01: Autonomous Coding Agent

## Overview

This demo showcases an **autonomous coding agent** powered by Azure OpenAI that can:

1. Read and understand a natural language feature request
2. Write Python code to implement the feature
3. Write unit tests for the code
4. Execute the tests and fix failures — all without human intervention

This demonstrates the full **code-generate → test → fix** agentic loop in action.

**Estimated demo time:** 10–15 minutes

---

## Key Concepts Demonstrated

| Concept | Where You'll See It |
|---------|-------------------|
| Multi-turn agentic loop | Agent iterates until tests pass |
| Code generation | GPT-4o writes implementation + tests |
| Code execution | `UserProxyAgent` runs pytest in a sandbox |
| Self-healing | Agent reads test failures and fixes its own code |
| Human-in-the-loop gate | Optional approval before first execution |

---

## Prerequisites

- Completed Lab 02 or Lab 03 (familiarity with Azure OpenAI + AutoGen)
- Docker Desktop running (optional, for isolated code execution)
- `.env` configured with Azure OpenAI credentials

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                 Coding Agent System                  │
│                                                      │
│  Feature Request                                     │
│       │                                              │
│       ▼                                              │
│  ┌─────────┐   code    ┌──────────┐  test results   │
│  │ Coder   │──────────▶│ Executor │────────────────┐ │
│  │ (LLM)   │◀──────────│ (proxy)  │                │ │
│  └─────────┘  fix code └──────────┘                │ │
│       │                                            │ │
│       │ all tests pass                             │ │
│       ▼                                            │ │
│  ┌─────────┐                                       │ │
│  │ Reviewer│◀──────────────────────────────────────┘ │
│  │ (LLM)   │                                         │
│  └─────────┘                                         │
└─────────────────────────────────────────────────────┘
```

---

## Running the Demo

```bash
cd demos/demo01-coding-agent
python coding_agent.py
```

Or provide a custom feature request:

```bash
python coding_agent.py --task "Implement a Python function that parses a CSV string and returns a list of dictionaries. Include edge cases for empty rows and missing headers."
```

---

## What to Watch For

1. **Thought process** — The Coder explains what it's about to write before writing it
2. **Test output** — The Executor prints pytest results inline
3. **Self-correction** — If a test fails, the Coder reads the error message and patches the code
4. **Review pass** — The Reviewer agent does a final code quality check

---

## Talking Points

- The agent loop converges in **2–3 iterations** for most tasks
- The Reviewer adds docstrings and type hints that the Coder missed
- Notice the agent never hard-codes the test data — it generates edge-case tests autonomously
- With Docker execution enabled, all code runs in an isolated container

---

## Extension Ideas

- Add a **Documentation Writer** agent that produces Sphinx-style docstrings
- Integrate with GitHub via the `gh` CLI so the agent opens a real PR
- Use AutoGen's `nested_chats` to spawn a separate architecture discussion before coding
