# Lab 1 – Build a Rotisserie Chicken Planning Agent

## Scenario

You will create a **RotisseriePlannerAgent** in your Azure AI Foundry project. This agent acts as a rotisserie chicken planning assistant for the **Zava** store.

**What the agent does:**
- Recommends how many chickens to cook each day
- Recommends when to cook them during the day
- Suggests simple real-time adjustments to reduce waste
- Uses past sales (not orders) to guide recommendations

The agent uses two authoritative data files:
- `chicken_hourly_store_sales.json` – Hourly sales patterns, waste logs, and stockout events
- `chicken_daily_orders_financials.json` – 31 days of daily sales, costs, waste, and financials

## Prerequisites

- Azure AI Foundry project with a deployed model (e.g., `gpt-4o-mini`)
- Python 3.10+
- Azure CLI authenticated: `az login`

## Deliverables

After completing this lab you will have:
- **Project Endpoint** (your Foundry project URL)
- **RotisseriePlannerAgent** agent name/ID
- A working agent that answers questions like: *"What should I cook tomorrow and when?"*

## Instructions

Run the notebook `Lab1_Build_Rotisserie_Agent.ipynb` in this folder.
