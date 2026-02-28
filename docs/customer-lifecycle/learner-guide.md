# Learner Guide: VIP Customer Lifecycle Scenario

## Learning Levels (Canonical)
- **L100 (foundational orientation):** Understand scenario context, data sources, and shared vocabulary. No pass/fail completion gate.
- **L200 (intermediate):** Build practical familiarity with tools, transformations, and terminology before baseline grading.
- **L300 (advanced hands-on baseline, WWL-aligned):** Advanced hands-on practice that builds on L100 and L200; this is the required workshop exercise level for completion/pass.
- **L400 (optional complexity):** Extension work that deepens L300 outcomes and is excluded from pass/fail.

## Level 300 Completion Criteria (Pass/Fail)
To pass the workshop baseline, you must deliver all four outputs:
1. At-risk VIP/Gold identification using the **2+ negative-signal rule**.
2. Plain-language explanation for each at-risk VIP/Gold customer.
3. Recommended human action for each at-risk VIP/Gold customer.
4. Portfolio summary with tier counts, at-risk counts, and at-risk % by tier.

Pass/fail boundary:
- **Pass requires L300 completion.**
- **L400 is optional and does not affect pass/fail.**

## Phase Outcomes
| Phase | Outcome artifact |
|---|---|
| Copilot Studio | Built/configured Copilot Studio baseline artifact + conversational at-risk explanation/action outputs |
| Foundry | Multi-agent workflow outputs (RFM, tier/health, VIP recency alert using `tier='VIP' AND recency_days > 60`, news-based action evaluation) with 2+ signal rule alignment |
| Agent Framework | Built/configured Agent Framework baseline alert workflow + proactive explain-only alerts |

## Run Sequence (Use This Order)
1. `labs/customer-lifecycle/level-300/copilot-studio.md`
2. `labs/customer-lifecycle/level-300/foundry.md`
3. `labs/customer-lifecycle/level-300/agent-framework.md`
4. Validate against `labs/customer-lifecycle/level-300/output-contract.md`

## Level 300 Build/Configure Checkpoints (Required)
- In Copilot Studio, you must **build/configure** the workshop copilot/topic instructions before running insight prompts.
- In Agent Framework, you must **build/configure** the workshop alert workflow (data binding, trigger gating, alert template) before running proactive alert demonstrations.
- Running conversations against prebuilt assets without completing baseline build/configuration does not satisfy Level 300 expectations.

## Foundry Navigation and Auth Checkpoints (Required)
- Use **New Foundry** portal mode (toggle enabled).
- Use signed-in user/project access; **do not configure Project API keys** (disabled path).
- Follow navigation sequence:
  1. Optional project creation: **Start building -> Design workflow**.
  2. Data setup: **Build -> Data** (load workbook + `synthetic_regional_news_24m`).
  3. Agent orchestration: **Build -> Workflows** (run all 4 agents with handoff chain).
- Agent 4 must enforce synthetic news scope and exception handling (missing region, non-fictional company, malformed date, stale record).

## Foundry Progress and Iteration (FR-015..FR-019)
Use this checklist during Foundry execution:
1. `agent1_rfm` complete with RFM fields and run evidence (`rfm_window_days`, `rfm_run_timestamp`).
2. `agent2_tier_health` complete with tier/health fields and risk-gate evidence (`risk_gate_rule_text`).
3. `agent3_vip_recency_alerts` complete with threshold evidence (`vip_recency_threshold_days` = 60, `agent3_rule_text`).
4. `agent4_news_action_eval` complete with scope evidence (`news_dataset_name` = `synthetic_regional_news_24m`, `scope_window_months` = 24).

Artifact status transitions (use only these):
- `incomplete` -> artifact missing or not run yet.
- `needs rework` -> artifact exists but fails checklist criteria.
- `complete` -> artifact exists and passes checklist criteria.

Iteration decisions:
1. Check progress.
2. Detect remaining work (`incomplete` or `needs rework`).
3. Process remaining work.
4. Iterate until all four artifacts are `complete`.

Stop only when both are true:
- all four required artifacts are `complete`, and
- your outputs cover identification, explanation, action, and portfolio summary.

Scope guardrail:
- Keep this within the existing four-agent Level 300 baseline; do not add net-new mandatory agent categories.

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

## Optional Extensions (After L300 Complete)
- Use `labs/customer-lifecycle/level-400/extensions.md` only after L300 is complete.
- L400 work is enrichment only and is outside workshop pass/fail.
- If class time requires cuts, move non-essential items to `labs/customer-lifecycle/level-400/extensions.md` as after-class extensions. Do not delete deferred learning items.
