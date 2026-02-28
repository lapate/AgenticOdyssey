# Level 300 Mandatory Output Contract

All Level 300 submissions must satisfy this contract.

## Level 300 Baseline Requirement (Completion Boundary)
Every learner must submit:
1. **At-risk VIP/Gold identification** (using the 2+ negative-signal rule)
2. **Plain-language explanation** for each at-risk VIP/Gold customer
3. **Recommended human action** for each at-risk VIP/Gold customer
4. **Portfolio summary** with tier counts, at-risk counts, and at-risk % by tier

## A. Portfolio Metrics (Required)
| Metric | Required format |
|---|---|
| Tier counts | Count of customers by VIP/Gold/Silver/Bronze |
| At-risk counts | Count of `risk_status = at_risk` by tier |
| At-risk % by tier | `at-risk count / tier count` for each tier |

## B. At-Risk Customer Outputs (Required)
For each at-risk VIP/Gold customer:
1. `customer_id` and `tier`
2. `triggered_signals`
3. `negative_signal_count` (must be `>=2`)
4. Plain-language explanation of risk drivers
5. Mapped human action (from action mapping matrix)

## C. Stage-Based Foundry Artifact Contract (3-5 Agent Compatible)
Use any 3-5 agent topology as long as these stage outcomes and handoffs are present.

| Required stage outcome | Minimum handoff artifact | Required fields | Required source-lineage / evidence fields | L300 outcome coverage marker |
|---|---|---|---|---|
| Stage 1 - Ingest + score | `stage1_ingest_score` | `customer_id`, `customer_name`, `recency_days`, `frequency_90d`, `monetary_90d` | `source_dataset_name`, `source_row_count`, `rfm_window_days` (=90), `rfm_run_timestamp` | Identification input |
| Stage 2 - Tier + risk classification | `stage2_tier_risk` | `customer_id`, `tier`, `triggered_signals`, `negative_signal_count`, `risk_status` | `risk_gate_rule_text` (`negative_signal_count >= 2 => at_risk`), `signal_window_note` | Identification |
| Stage 3 - Explanation + action mapping | `stage3_explain_action` | `customer_id`, `tier`, `risk_explanation_plain`, `action_recommendation`, `action_rationale` | `action_mapping_version`, `derived_from_stage2_artifact` | Explanation + Action |
| Stage 4 - Portfolio summary | `stage4_portfolio_summary` | `tier`, `tier_count`, `at_risk_count`, `at_risk_pct` | `summary_source_artifact`, `summary_run_timestamp` | Portfolio summary |
| Stage 5 (optional) - Synthetic news enrichment | `stage5_news_enrichment` | `customer_id`, `event_id`, `event_date`, `region`, `event_scope_status`, `event_company_reference` | `news_dataset_name` (`synthetic_regional_news_24m`), `scope_window_months` (=24), `news_exception_code` (if excluded) | Action refinement |

Notes:
- Stage 5 is optional for topology, but synthetic-news evidence requirements apply whenever enrichment is used.
- Implementations may merge or split stages across 3-5 agents, but required fields and evidence must remain learner-visible.

## D. Handoff Validation States (Required)
Use only:
- `complete` -> artifact exists and passes required-field checks.
- `incomplete` -> artifact missing or not run.
- `needs rework` -> artifact exists but fails required fields/evidence checks.

## E. Rule Enforcement (Required)
- A customer with 0 signals: `healthy`
- A customer with 1 signal: `watch`
- A customer with 2+ signals: `at_risk`
- Any output labeling 0/1-signal customer as at-risk requires baseline rework.

## F. Validation and Fallback Gate (Required)
- Named-customer spot-check must trace one customer row from Stage 1 through Stage 3 (and Stage 5 if used).
- Aggregate check must validate Stage 4 tier counts, at-risk counts, and at-risk % by tier.
- If primary prompt flow is blocked by guardrails, run a documented guardrail-safe fallback path and re-run the same checks.

## G. Core Learning Boundary
- **Core complete (Level 300):** Sections A+B+C+D+E+F are met.
- **Not required for core completion:** Any Level 400 extension artifact.
- **Learning focus rule:** L300 is the required baseline; L400 is optional enrichment and must not block core completion.
