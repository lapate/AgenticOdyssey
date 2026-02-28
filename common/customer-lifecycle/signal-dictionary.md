# Customer Lifecycle Signal Dictionary

Shared vocabulary for all customer-lifecycle labs and guides.

## Canonical Learning Levels and Core Learning Boundary
- **L100 (foundational orientation):** Understand scenario context, data sources, and shared vocabulary.
- **L200 (intermediate):** Build practical familiarity with tooling and transformation patterns before the core multi-agent baseline.
- **L300 (advanced hands-on baseline, WWL-aligned):** Advanced hands-on practice that builds on L100 and L200; this is the required workshop baseline for learning outcomes and multi-agent pattern mastery.
- **L400 (optional complexity):** Extension work that deepens L300 outcomes and is optional enrichment after L300.
- **Workshop core-learning boundary:** **L300 defines core learning completion. L400 is optional and must not block core completion.**
- **Canonical pathing:** `labs/customer-lifecycle/level-300/` is the required baseline path; `labs/customer-lifecycle/level-400/` is the optional complexity path for after-class extensions.

## Standard Terms
| Term | Definition |
|---|---|
| Customer health | A plain-language view of whether a customer is stable or showing early decline risk. |
| Risk signals | Observable negative shifts in lifecycle behavior (recency, frequency, spend, margin, mix). |
| Tiers | Customer value segments: VIP, Gold, Silver, Bronze. |
| Actions | Recommended human follow-up steps to reduce retention risk. |

## Foundry Stage Terminology (Level 300, Architecture-Agnostic)
| Stage | Responsibility | Required output/handoff |
|---|---|---|
| Stage 2 (combined scoring + tier/risk) | RFM + tier/risk classification | `agent2-tier-report-{{customer_id}}` with `recency_days`, `frequency_90d`, `monetary_90d`, `tier`, `negative_signal_count`, `risk_status`, `triggered_signals` |
| Stage 3 | Explanation + action mapping | `stage3_explain_action` with explanation/action fields linked to Stage 2 |
| Stage 4 | Portfolio summary | `stage4_portfolio_summary` with tier counts, at-risk counts, and at-risk % by tier |
| Stage 5 (optional) | Synthetic news enrichment | `stage5_news_enrichment` with event scope and action-context evidence |

Topology rule:
- Learners may implement these outcomes with any **3-5 agent** workflow.
- Stage outcomes are mandatory; fixed agent names are not mandatory.

## Foundry Artifact Status Model (FR-016)
Use only these statuses when assessing required Foundry stage artifacts:
- `complete`: artifact exists and passes its checklist criteria.
- `incomplete`: artifact is missing or not yet run.
- `needs rework`: artifact exists but fails one or more checklist criteria.

No other status values are allowed in Level 300 Foundry progress checkpoints.

## Foundry Failure/Remediation Terms (FR-017, FR-020)
Use these terms consistently in learner and facilitator documents:
- `guardrail_blocked` -> primary prompt pattern blocked by tenant guardrails.
- `placeholder_output` -> output is generic/example-like and not source-derived.
- `missing_required_fields` -> one or more required handoff fields absent.
- `fallback_path_primary_to_artifact_first` -> switch from blocked chat prompt to artifact-first/stage-by-stage execution.
- `targeted_stage_rework` -> rerun only the failed stage and downstream dependents.

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
