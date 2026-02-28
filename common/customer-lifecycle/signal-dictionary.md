# Customer Lifecycle Signal Dictionary

Shared vocabulary for all customer-lifecycle labs and guides.

## Canonical Learning Levels and Pass/Fail Boundary
- **L100 (foundational orientation):** Understand scenario context, data sources, and shared vocabulary. No pass/fail completion gate.
- **L200 (intermediate):** Build practical familiarity with tooling and transformation patterns before baseline grading.
- **L300 (advanced hands-on baseline, WWL-aligned):** Advanced hands-on practice that builds on L100 and L200; this is the required workshop exercise level for completion/pass.
- **L400 (optional complexity):** Extension work that deepens L300 outcomes and is excluded from pass/fail.
- **Workshop pass/fail boundary:** **L300 is required for pass. L400 is optional and must not affect pass/fail.**
- **Canonical pathing:** `labs/customer-lifecycle/level-300/` is the required baseline path; `labs/customer-lifecycle/level-400/` is the optional complexity path for after-class extensions.

## Standard Terms
| Term | Definition |
|---|---|
| Customer health | A plain-language view of whether a customer is stable or showing early decline risk. |
| Risk signals | Observable negative shifts in lifecycle behavior (recency, frequency, spend, margin, mix). |
| Tiers | Customer value segments: VIP, Gold, Silver, Bronze. |
| Actions | Recommended human follow-up steps to reduce retention risk. |

## Foundry 4-Agent Terminology (Level 300)
| Agent | Canonical name | Required output/handoff |
|---|---|---|
| Agent 1 | RFM scoring | `agent1_rfm` with `recency_days`, `frequency_90d`, `monetary_90d` |
| Agent 2 | Tier + health scoring | `agent2_tier_health` with `tier`, health indicators, `negative_signal_count`, `risk_status` |
| Agent 3 | VIP recency threshold alert | `agent3_vip_recency_alerts` using `tier='VIP' AND recency_days > 60`, including threshold evidence field |
| Agent 4 | News-based action evaluation | `agent4_news_action_eval` with event-scoped rationale and action recommendation |

## Foundry Artifact Status Model (FR-016)
Use only these statuses when assessing each of the four required Foundry artifacts:
- `complete`: artifact exists and passes its checklist criteria.
- `incomplete`: artifact is missing or not yet run.
- `needs rework`: artifact exists but fails one or more checklist criteria.

No other status values are allowed in Level 300 Foundry progress checkpoints.

## Signal Definitions (Learner Visible)
| Signal | What it measures | Negative condition (counts toward risk) | Why it matters |
|---|---|---|---|
| Recency | Days since last order | Recency is above tier median or exceeds 60 days | Larger order gaps are an early churn indicator. |
| Frequency | Orders per recent 90-day window vs prior 90-day window | Recent order count declines by 20%+ | Fewer order events indicate reduced engagement. |
| Spend | Net revenue in recent 90 days vs prior 90 days | Spend declines by 15%+ | Revenue decline can precede account loss. |
| Margin | Gross margin % trend | Margin declines by 5 percentage points+ | Margin pressure can signal pricing or discount stress. |
| Mix | Product category diversity or strategic SKU participation | Category count or strategic SKU share declines materially | Narrower mix can indicate shrinking relationship depth. |

## Tier Handling Notes
- Level 300 baseline triage focuses on **VIP and Gold**.
- Silver and Bronze remain in portfolio totals for context.
- Tier naming must remain unchanged across all artifacts.

## Synthetic News Dataset Scope and Exception Rules (Agent 4)
- Dataset name must be **`synthetic_regional_news_24m`**.
- Scope is restricted to rows with `event_date` in the **last 24 months**.
- Rows must include regional event context and at least one fictional-company reference (for example Contoso, Fabrikam, or Northwind).
- Exception handling:
  - Missing region -> mark row as `exception_missing_region`; exclude from action correlation.
  - Non-fictional company reference -> mark row as `exception_non_fictional_company`; exclude from action correlation.
  - Malformed date -> mark row as `exception_malformed_date`; exclude from action correlation.
  - Out-of-window/stale row (>24 months old) -> mark row as `exception_stale_record`; exclude from action correlation.
