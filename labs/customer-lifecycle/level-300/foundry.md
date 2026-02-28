# Lab: Microsoft Foundry (60 Minutes)

## Goal
Build a learner-friendly **3-5 agent** Foundry workflow that produces Level 300 outcomes:
1. at-risk VIP/Gold identification,
2. plain-language explanation,
3. recommended human action,
4. portfolio summary.

## Recommended Demo Topology (Default = 4 Agents)
Use this default unless you intentionally teach a 3-agent or 5-agent variation.

| Agent | Stage outcome artifact |
|---|---|
| `agent1-ingest-score` | `stage1_ingest_score` |
| `agent2-tier-risk` | `stage2_tier_risk` |
| `agent3-explain-action` | `stage3_explain_action` |
| `agent4-portfolio-summary` | `stage4_portfolio_summary` |
| `agent5-news-enrichment` (optional) | `stage5_news_enrichment` |

Notes:
- **3-agent option:** merge Stage 3 + Stage 4 responsibilities into one agent.
- **5-agent option:** keep all 4 baseline agents and add Stage 5 enrichment.
- You must stay within **3 to 5 agents** and still satisfy `output-contract.md`.

## Required Inputs
- `data/Zava Sales Data - FY2024-2026.xlsx`
- Exported sheet files in `data/exported-sheets/`
- `labs/customer-lifecycle/level-300/output-contract.md`
- Synthetic dataset `synthetic_regional_news_24m` (required only when Stage 5 is used)

## Step-by-Step (Navigate / Click / Type)
1. Open Foundry and project workspace.
   - **Navigate:** `https://ai.azure.com`
   - **Click:** Enable **New Foundry**.
   - **Verify:** Project workspace opens and Build menu is available.

2. Upload source data files.
   - **Click:** **Build -> Data -> Files**.
   - **Type/Select:** Upload files from `data/exported-sheets/`.
   - **Verify:** Upload completes with no file errors.

3. (If using enrichment) create synthetic news dataset.
   - **Click:** **Build -> Data** -> create table/dataset.
   - **Type:** Name `synthetic_regional_news_24m`.
   - **Type:** Include fields `event_id`, `region`, `event_date`, `event_type`, `severity`, `demand_signal`, `affected_companies`, `event_summary`.
   - **Verify:** Rows are within the last 24 months and include fictional company references.

4. Build Agent 1 (`agent1-ingest-score`) for Stage 1.
   - **Click:** **Build -> Agent -> Create Agent**.
   - **Type:** Name `agent1-ingest-score`.
   - **Type (instructions):** `Parse uploaded source rows, compute customer-level RFM, and output artifact stage1_ingest_score with required fields/evidence from output-contract.md. Use source-derived values only.`
   - **Click:** **Save**.
   - **Test (Message the agent...):** `Return only the row for customer_name='Contoso, Ltd.' from stage1_ingest_score. If not found, return not_found.`
   - **Verify:** Response contains real values (not placeholders).

5. Build Agent 2 (`agent2-tier-risk`) for Stage 2.
   - **Click:** **Build -> Agent -> Create Agent**.
   - **Type:** Name `agent2-tier-risk`.
   - **Type (instructions):** `Use stage1_ingest_score to derive tier and risk outputs in stage2_tier_risk. Enforce risk gate: negative_signal_count >= 2 => at_risk.`
   - **Click:** **Save**.
   - **Test (Message the agent...):** `Return stage2_tier_risk row for customer_name='Contoso, Ltd.' with tier, triggered_signals, negative_signal_count, and risk_status.`
   - **Verify:** 0/1/2+ mapping appears correctly.

6. Build Agent 3 (`agent3-explain-action`) for Stage 3.
   - **Click:** **Build -> Agent -> Create Agent**.
   - **Type:** Name `agent3-explain-action`.
   - **Type (instructions):** `Use stage2_tier_risk to generate plain-language risk explanation and action recommendation into stage3_explain_action with required evidence fields.`
   - **Click:** **Save**.
   - **Test (Message the agent...):** `Return stage3_explain_action row for customer_name='Contoso, Ltd.' with risk_explanation_plain, action_recommendation, and action_rationale.`
   - **Verify:** Explanation is business-readable and action is explicit.

7. Build Agent 4 (`agent4-portfolio-summary`) for Stage 4.
   - **Click:** **Build -> Agent -> Create Agent**.
   - **Type:** Name `agent4-portfolio-summary`.
   - **Type (instructions):** `Aggregate stage2_tier_risk into stage4_portfolio_summary with tier_count, at_risk_count, and at_risk_pct by tier plus required evidence fields.`
   - **Click:** **Save**.
   - **Test (Message the agent...):** `Return stage4_portfolio_summary for all tiers.`
   - **Verify:** Tier counts, at-risk counts, and at-risk % are present.

8. (Optional) Build Agent 5 (`agent5-news-enrichment`) for Stage 5.
   - **Click:** **Build -> Agent -> Create Agent**.
   - **Type:** Name `agent5-news-enrichment`.
   - **Type (instructions):** `Enrich thresholded customers with synthetic_regional_news_24m into stage5_news_enrichment. Include event_scope_status and news_exception_code for excluded rows.`
   - **Click:** **Save**.
   - **Test (Message the agent...):** `Return enrichment row for customer_name='Contoso, Ltd.' including news_dataset_name and scope_window_months.`
   - **Verify:** Dataset and scope evidence are present.

9. Create workflow and wire agent chain.
   - **Click:** **Build -> Workflows -> Create (Sequential)**.
   - **Type:** Name `vip-lifecycle-management-flow`.
   - **Wire (default 4-agent):**
     - `agent1-ingest-score` -> `agent2-tier-risk` -> `agent3-explain-action` -> `agent4-portfolio-summary`
   - **Wire (if 5-agent):**
     - Add `agent5-news-enrichment` after Stage 3 or Stage 4 according to your teaching pattern.
   - **Verify:** Total agent count is between 3 and 5.

10. Run workflow (primary path) and save artifacts.
   - **Click:** Run workflow.
   - **Type:** Save outputs as stage artifacts:
     - `stage1_ingest_score`
     - `stage2_tier_risk`
     - `stage3_explain_action`
     - `stage4_portfolio_summary`
     - `stage5_news_enrichment` (if used)
   - **Verify:** Artifacts exist and required fields/evidence are populated per `output-contract.md`.

11. Run required validation checks.
   - **Named-customer spot-check (required):**
     - Trace `Contoso, Ltd.` from Stage 1 -> Stage 3 (and Stage 5 if used).
   - **Aggregate artifact check (required):**
     - Validate Stage 4 tier counts, at-risk counts, and at-risk % by tier.
   - **Verify:** Outputs cover identification, explanation, action, and portfolio summary with source-derived values.

12. Apply failure handling if needed.
   - `guardrail_blocked` -> switch to fallback path (Step 13), then re-run Step 11.
   - `placeholder_output` -> rerun failed stage with source-only and explicit field constraints.
   - `missing_required_fields` -> mark artifact `needs rework`, rerun failed stage and downstream stages.

13. Guardrail-safe fallback path (artifact-first).
   - **Run stages individually** in Workflows/Artifacts (avoid full-table chat response requests).
   - **Validate each stage artifact** before moving to the next stage.
   - **Assemble final outputs** from saved artifacts.
   - **Re-run Step 11 checks** and keep the same evidence set.

## Timebox Guidance
1. **0-10 min:** Data setup + create first two agents.
2. **10-30 min:** Build Stage 1-3 agents and quick spot-checks.
3. **30-45 min:** Build Stage 4 (and Stage 5 if used) + wire workflow.
4. **45-60 min:** Run full workflow + required validation + fallback remediation if needed.
