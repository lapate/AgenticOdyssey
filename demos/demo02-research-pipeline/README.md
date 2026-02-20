# Demo 02: Multi-Agent Research Pipeline

## Overview

This demo showcases a **multi-agent research pipeline** where a team of specialized agents collaborates to produce a comprehensive research brief on any topic. The pipeline demonstrates real-world orchestration patterns including **parallel agent execution**, **result synthesis**, and **structured output generation**.

**Estimated demo time:** 10–15 minutes

---

## Pipeline Architecture

```
User Topic
    │
    ▼
┌────────────────────────────────────────────────────────────┐
│                    Orchestrator Agent                       │
│  Decomposes topic into research angles; assigns subtasks   │
└─────────┬──────────────────┬───────────────────────────────┘
          │                  │
          ▼                  ▼
  ┌──────────────┐   ┌──────────────────┐
  │  Researcher  │   │  Fact Checker    │
  │  (finds info)│   │  (verifies claims│
  └──────┬───────┘   └────────┬─────────┘
         │                    │
         └──────────┬─────────┘
                    │
                    ▼
          ┌─────────────────┐
          │  Writer Agent   │
          │ (structures     │
          │  the brief)     │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  Editor Agent   │
          │ (refines tone & │
          │  quality)       │
          └────────┬────────┘
                   │
                   ▼
          📄 research_brief.md
```

---

## Key Concepts Demonstrated

| Concept | Description |
|---------|-------------|
| **Orchestration** | One agent decomposes tasks and delegates to specialists |
| **Role specialization** | Each agent has a narrow, well-defined job |
| **Fact checking** | A dedicated agent challenges unsupported claims |
| **Structured output** | Final brief written in clean Markdown |
| **File output** | Result saved to `research_brief.md` |

---

## Prerequisites

- Completed Lab 03 (Multi-Agent Orchestration)
- `.env` configured with Azure OpenAI credentials
- (Optional) Bing Search API key for real web search

---

## Running the Demo

```bash
cd demos/demo02-research-pipeline
python research_pipeline.py
```

Or specify a topic:

```bash
python research_pipeline.py --topic "The impact of AI agents on software development workflows"
```

---

## Expected Output

The demo produces `research_brief.md` in the current directory with sections:

1. **Executive Summary** — 3–5 sentence overview
2. **Key Findings** — Bullet points from the Researcher
3. **Fact-Check Notes** — Claims verified or flagged by the Fact Checker
4. **Analysis** — Synthesis by the Writer
5. **Recommendations** — Actionable next steps
6. **Sources** — URLs or references used

---

## Talking Points

- The **Fact Checker** prevents hallucinations by challenging the Researcher's claims
- The **Writer** transforms raw findings into a readable narrative
- The **Editor** ensures consistent tone — essential for enterprise outputs
- Saving to a file makes the output shareable and auditable

---

## Extension Ideas

- Add a **Translator** agent that renders the brief in a second language
- Integrate with Microsoft 365 via Graph API to post directly to SharePoint
- Add a **Citation Manager** agent that normalizes references to APA format
