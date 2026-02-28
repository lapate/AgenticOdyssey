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
1. Customer ID and tier
2. Triggered signal list
3. `negative_signal_count` (must be >=2)
4. Plain-language explanation of risk drivers
5. Mapped human action (from action mapping matrix)

## C. Foundry FR-015 Artifact Contract (Exactly Four Required)
| Agent | Required artifact (must exist) | Required fields | Required evidence fields |
|---|---|---|---|
| Agent 1 (RFM) | `agent1_rfm` | `customer_id`, `recency_days`, `frequency_90d`, `monetary_90d` | `rfm_window_days` (90), `rfm_run_timestamp` |
| Agent 2 (Tier + health) | `agent2_tier_health` | `customer_id`, `tier`, `negative_signal_count`, `risk_status`, `triggered_signals` | `risk_gate_rule_text` (`negative_signal_count >= 2 => at_risk`), `tiering_method_note` |
| Agent 3 (VIP threshold alert) | `agent3_vip_recency_alerts` | `customer_id`, `tier`, `recency_days`, `vip_recency_threshold_days`, `agent3_rule_text`, `alert_flag` | `vip_recency_threshold_days` (=60), `agent3_rule_text` (`tier='VIP' AND recency_days > 60`) |
| Agent 4 (News action eval) | `agent4_news_action_eval` | `customer_id`, `event_id`, `event_date`, `region`, `event_scope_status`, `action_recommendation`, `action_rationale` | `news_dataset_name` (`synthetic_regional_news_24m`), `scope_window_months` (24) |

Only these four artifacts are required for Foundry baseline completion. No additional artifact category is mandatory for Level 300 pass/fail.

## D. Rule Enforcement (Required)
- A customer with 0 signals: `healthy`
- A customer with 1 signal: `watch`
- A customer with 2+ signals: `at_risk`
- Any output labeling 0/1-signal customer as at-risk is a baseline failure.

## E. Pass/Fail Boundary
- **Pass (Level 300):** Sections A+B+C+D fully met.
- **Not required for pass:** Any Level 400 extension artifact.
- **Grading rule:** L300 is the required baseline; L400 is optional enrichment and must not change pass/fail.
