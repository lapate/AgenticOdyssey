# Facilitator Guide: VIP Customer Lifecycle Workshop

## Storyline Alignment
- Business problem: detect early lifecycle decline in high-value customers and act sooner.
- Primary audience: mixed technical levels, business-first framing.
- Baseline scope: Level 200 only; Level 300 is optional enrichment.

## Phase Checkpoints (Timeboxed)
| Phase | Target time | Facilitator checkpoint |
|---|---:|---|
| Copilot Studio | <=30 min | Learner produced at-risk VIP/Gold list with plain-language explanations |
| Foundry | <=60 min | Learner produced structured signals, 2+ rule output, and portfolio summary |
| Agent Framework | <=10 min | Learner showed explain-only alerts with mapped actions |

## Misclassification Mitigation Prompts
Use these prompts when learners over-classify:
1. "How many negative signals are present for this customer?"
2. "Is the count at least two? If not, should status be watch instead of at-risk?"
3. "Which two concrete signals justify the at-risk label?"

## Portfolio Metric Interpretation Guidance
- Tier counts show portfolio composition.
- At-risk counts identify concentration of intervention workload.
- At-risk % by tier normalizes risk across differently sized tiers.
- Prioritize outreach queue: VIP at-risk first, Gold at-risk second.

## Documentation Parity Notes
- Labs and guides use shared terms: customer health, risk signals, tiers, actions.
- Baseline logic in all phases must match `common/customer-lifecycle/risk-rules.md`.
