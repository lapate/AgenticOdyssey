# Customer Lifecycle Signal Dictionary

Shared vocabulary for all customer-lifecycle labs and guides.

## Standard Terms
| Term | Definition |
|---|---|
| Customer health | A plain-language view of whether a customer is stable or showing early decline risk. |
| Risk signals | Observable negative shifts in lifecycle behavior (recency, frequency, spend, margin, mix). |
| Tiers | Customer value segments: VIP, Gold, Silver, Bronze. |
| Actions | Recommended human follow-up steps to reduce retention risk. |

## Signal Definitions (Learner Visible)
| Signal | What it measures | Negative condition (counts toward risk) | Why it matters |
|---|---|---|---|
| Recency | Days since last order | Recency is above tier median or exceeds 60 days | Larger order gaps are an early churn indicator. |
| Frequency | Orders per recent 90-day window vs prior 90-day window | Recent order count declines by 20%+ | Fewer order events indicate reduced engagement. |
| Spend | Net revenue in recent 90 days vs prior 90 days | Spend declines by 15%+ | Revenue decline can precede account loss. |
| Margin | Gross margin % trend | Margin declines by 5 percentage points+ | Margin pressure can signal pricing or discount stress. |
| Mix | Product category diversity or strategic SKU participation | Category count or strategic SKU share declines materially | Narrower mix can indicate shrinking relationship depth. |

## Tier Handling Notes
- Level 200 baseline triage focuses on **VIP and Gold**.
- Silver and Bronze remain in portfolio totals for context.
- Tier naming must remain unchanged across all artifacts.
