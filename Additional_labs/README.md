# Zava Rotisserie Chicken Planning Labs

These labs walk you through building, orchestrating, and evaluating AI agents for rotisserie chicken operations at the **Zava** store.

## Lab Structure

| Lab | Title | What You'll Do |
|-----|-------|---------------|
| **Lab 1** | Build Agent | Create a `RotisseriePlannerAgent` that recommends cooking schedules |
| **Lab 2** | Orchestrate Agents | Build 4 specialized agents and orchestrate them in a pipeline |
| **Lab 3** | Evaluate Agents | Run violence, fluency, and task adherence evaluations against the live agent |
| **Lab 4** | Tool Call Accuracy | Evaluate whether the agent selects the correct tools with proper parameters |
| **Lab 5** | Red Team Security | Run adversarial security scans to find vulnerabilities |

## Data Files

The `data/` folder contains two authoritative data sources:

- **`chicken_hourly_store_sales.json`** — Hourly sales patterns, waste logs, stockout events
- **`chicken_daily_orders_financials.json`** — 31 days of daily sales, costs, waste, and financials

## Sample Prompt

> What should I cook tomorrow and when?

## Prerequisites

- Azure AI Foundry project with a deployed model (e.g., `gpt-4o-mini`)
- Python 3.10+
- Azure CLI authenticated: `az login`
- VS Code with Jupyter extension

## Getting Started

1. Start with **Lab 1** to create your first agent
2. Proceed to **Lab 2** to build a multi-agent pipeline
3. Complete **Lab 3** to evaluate your agents' quality
