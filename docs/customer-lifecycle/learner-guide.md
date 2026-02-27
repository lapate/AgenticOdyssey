# Learner Guide: VIP Customer Lifecycle Scenario

## What You Will Deliver (Level 200 Baseline)
1. Identify at-risk VIP/Gold customers.
2. Explain risk in plain business language.
3. Recommend one practical human action per at-risk customer.
4. Summarize portfolio metrics:
   - Tier counts
   - At-risk counts
   - At-risk percentage by tier

## Phase Outcomes
| Phase | Outcome artifact |
|---|---|
| Copilot Studio | Conversational at-risk explanation + action outputs |
| Foundry | Structured risk scoring table with 2+ signal rule |
| Agent Framework | Proactive explain-only alerts for at-risk VIP/Gold |

## Baseline Rule You Must Follow
- Count negative lifecycle signals per customer.
- `2+` negative signals => `at_risk`
- `1` negative signal => `watch`
- `0` negative signals => `healthy`

## Glossary
- Customer health: business view of relationship stability.
- Risk signals: negative shifts in recency, frequency, spend, margin, mix.
- Tiers: VIP, Gold, Silver, Bronze.
- Actions: recommended human steps to reduce lifecycle risk.

## Level 200 vs Level 300 Boundary
- **Level 200 (required):** all baseline outputs and 2+ gating rule.
- **Level 300 (optional):** enhancement experiments only.
- Your Level 200 pass/fail does **not** depend on Level 300 outputs.
