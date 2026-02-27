# Learner Guide: VIP Customer Lifecycle Scenario

## Learning Levels (Canonical)
- **L100 (foundational orientation):** Understand scenario context, data sources, and shared vocabulary. No pass/fail completion gate.
- **L200 (required baseline hands-on competency):** Deliver required workshop outputs for completion/pass.
- **L300 (advanced hands-on practice, WWL-aligned):** Advanced hands-on practice that builds on L100 and L200; optional enrichment and excluded from pass/fail.

## Level 200 Completion Criteria (Pass/Fail)
To pass the workshop baseline, you must deliver all four outputs:
1. At-risk VIP/Gold identification using the **2+ negative-signal rule**.
2. Plain-language explanation for each at-risk VIP/Gold customer.
3. Recommended human action for each at-risk VIP/Gold customer.
4. Portfolio summary with tier counts, at-risk counts, and at-risk % by tier.

Pass/fail boundary:
- **Pass requires L200 completion.**
- **L300 is optional and does not affect pass/fail.**

## Phase Outcomes
| Phase | Outcome artifact |
|---|---|
| Copilot Studio | Conversational at-risk explanation + action outputs |
| Foundry | Structured risk scoring table with 2+ signal rule |
| Agent Framework | Proactive explain-only alerts for at-risk VIP/Gold |

## Run Sequence (Use This Order)
1. `labs/customer-lifecycle/level-200/copilot-studio.md`
2. `labs/customer-lifecycle/level-200/foundry.md`
3. `labs/customer-lifecycle/level-200/agent-framework.md`
4. Validate against `labs/customer-lifecycle/level-200/output-contract.md`

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

## Optional Extensions (After L200 Complete)
- Use `labs/customer-lifecycle/level-300/extensions.md` only after L200 is complete.
- L300 work is enrichment only and is outside workshop pass/fail.
