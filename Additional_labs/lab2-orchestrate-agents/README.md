# Lab 2 – Orchestrate Rotisserie Chicken Agents

## Scenario

You will reuse the **RotisseriePlannerAgent** from Lab 1 and create additional specialized agents, then orchestrate them in a sequential workflow using the **Microsoft Agent Framework**.

### Agents in this lab

| Agent | Responsibility |
|-------|---------------|
| **CoordinatorAgent** | Structures the user request into a brief for downstream agents |
| **DemandForecasterAgent** | Predicts daily/hourly demand using historical sales patterns |
| **CookingSchedulerAgent** | Creates batch cooking schedules aligned to demand peaks |
| **WasteReductionAgent** | Identifies waste risks and suggests real-time adjustments |
| **RotisseriePlannerAgent** | (from Lab 1) Produces the final consolidated plan |

## Prerequisites

- Completed **Lab 1** (you have the Foundry project endpoint and RotisseriePlannerAgent)
- Python 3.10+
- Azure CLI authenticated: `az login`

## Instructions

Run the notebook `Lab2_Orchestrate_Rotisserie_Agents.ipynb` in this folder.
