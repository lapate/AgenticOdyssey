# Agentic AI with AgenticOdyssey - Hands-on Workshop (Labs 1–3)

This repository contains a 3-lab, Python-first workshop for building, orchestrating, and evaluating AI agents using **Microsoft Foundry**.

## Labs
- **Lab 1 (Portal):** Build a persistent agent (**ProductInventoryManager**) in Microsoft Foundry (no code)
- **Lab 2 (Python):** Reuse the Lab 1 agent from code and orchestrate multiple agents
- **Lab 3 (Python):** Evaluate agent quality using the Azure AI Evaluation SDK

## Quickstart (Codespaces / Devcontainer)
1. Open this repo in GitHub Codespaces (or locally in VS Code using the Dev Container).
2. When the container finishes, open a terminal and authenticate:
   ```bash
   az login
   ```
3. Copy `.env.example` to `.env` and fill in your values.
4. Follow the lab folders under `labs/`.

## Repo Layout
- `.devcontainer/` — Codespaces-ready environment
- `labs/` — student-facing lab materials + notebooks
- `docs/screenshots/` — drop screenshots here for slides/handouts
- `common/` — shared setup/troubleshooting guides

> Note: This repo intentionally **does not** include GitHub Actions for running Lab 3.
