# Learner Guide: VIP Customer Lifecycle Scenario

## Learning Levels (Canonical)
- **L100 (foundational orientation):** Understand scenario context, data sources, and shared vocabulary.
- **L200 (intermediate):** Build practical familiarity with tools, transformations, and terminology before the core multi-agent baseline.
- **L300 (advanced hands-on baseline, WWL-aligned):** Advanced hands-on practice that builds on L100 and L200; this is the required workshop baseline for core learning outcomes and multi-agent pattern mastery.
- **L400 (optional complexity):** Extension work that deepens L300 outcomes and is optional enrichment after L300.

## Level 300 Completion Criteria (Core Learning Outcomes)
To complete the workshop core learning baseline, deliver all four outputs:
1. At-risk VIP/Gold identification using the **2+ negative-signal rule**.
2. Plain-language explanation for each at-risk VIP/Gold customer.
3. Recommended human action for each at-risk VIP/Gold customer.
4. Portfolio summary with tier counts, at-risk counts, and at-risk % by tier.

Core learning boundary:
- **Core completion requires L300 outputs.**
- **L400 is optional and does not block core completion.**

## Phase Outcomes
| Phase | Outcome artifact |
|---|---|
| Copilot Studio | Built/configured Copilot Studio baseline artifact + conversational at-risk explanation/action outputs |
| Foundry | Architecture-agnostic 3-5 agent workflow producing stage artifacts (`stage1_ingest_score`..`stage4_portfolio_summary`, optional `stage5_news_enrichment`) with 2+ signal rule alignment |
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
  3. Agent orchestration: **Build -> Workflows** (run your selected **3-5 agent** topology).
- If news enrichment is used, enforce synthetic news scope and exception handling (missing region, non-fictional company, malformed date, stale record).

## Foundry Progress and Iteration (FR-015..FR-020)
Use this checklist during Foundry execution:
1. `stage1_ingest_score` complete with scoring fields and source-lineage evidence.
2. `stage2_tier_risk` complete with tier/risk fields and risk-gate evidence (`negative_signal_count >= 2 => at_risk`).
3. `stage3_explain_action` complete with plain-language explanation and mapped action.
4. `stage4_portfolio_summary` complete with tier counts, at-risk counts, at-risk % by tier.
5. `stage5_news_enrichment` complete when used, with scope evidence (`news_dataset_name` = `synthetic_regional_news_24m`, `scope_window_months` = 24).

Artifact status transitions (use only these):
- `incomplete` -> artifact missing or not run yet.
- `needs rework` -> artifact exists but fails checklist criteria.
- `complete` -> artifact exists and passes checklist criteria.

Iteration decisions:
1. Check progress.
2. Detect remaining work (`incomplete` or `needs rework`).
3. Process remaining work.
4. Iterate until required artifacts are `complete`.

Stop only when both are true:
- required stage artifacts are `complete`, and
- your outputs cover identification, explanation, action, and portfolio summary.

Guardrail-safe fallback runbook:
1. If prompt is blocked (`guardrail_blocked`), switch to artifact-first stage execution in Workflows.
2. If output is generic (`placeholder_output`), rerun with source-only constraints + required fields.
3. If fields are missing (`missing_required_fields`), mark `needs rework` and rerun failed stage + downstream dependents.
4. Re-run both validation checks:
   - named-customer spot-check (for example `Contoso, Ltd.`),
   - aggregate portfolio check (tier counts, at-risk counts, at-risk % by tier).

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
- L400 work is enrichment only and is outside core completion requirements.
- If class time requires cuts, move non-essential items to `labs/customer-lifecycle/level-400/extensions.md` as after-class extensions. Do not delete deferred learning items.
