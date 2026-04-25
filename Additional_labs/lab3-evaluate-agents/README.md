# Lab 3 – Evaluate Rotisserie Chicken Agents

## Scenario

In this lab, you will evaluate the quality, safety, and task adherence of the agents created in Labs 1 and 2 using the **Azure AI Evaluation SDK**.

This lab demonstrates **offline, repeatable evaluation** — a critical step before deploying agents into production.

## What You'll Evaluate

- **Relevance**: Are responses related to rotisserie chicken planning?
- **Groundedness**: Are recommendations supported by actual sales data?
- **Task Adherence**: Does the agent follow its instructions?
- **Quality across scenarios**: Peak days, slow days, weather impacts, real-time adjustments

## Evaluation Dataset

The evaluation dataset (`eval_data.jsonl`) contains **20 diverse test cases** covering:
- Daily planning for every day of the week
- Weather-impacted scenarios
- Real-time adjustment decisions
- Waste reduction strategies
- Financial/cost analysis
- Edge cases (holidays, equipment failure, unexpected rush)

## Prerequisites

- Completed **Lab 1** and **Lab 2**
- Python 3.10+
- Azure CLI authenticated: `az login`

## Instructions

Run the notebook `Lab3_Evaluate_Rotisserie_Agents.ipynb` in this folder.
