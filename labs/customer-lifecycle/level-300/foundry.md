# Lab: Microsoft Foundry (60 Minutes)

## Goal
Build a four-agent Foundry workflow that turns raw sales data into business-ready lifecycle guidance:
1. Agent 1: Compute RFM (Recency, Frequency, Monetary),
2. Agent 2: Compute tiers + simple health indicators,
3. Agent 3: Apply rule `tier='VIP' AND recency_days > 60`,
4. Agent 4: Evaluate short-term actions using synthetic regional news signals.

## Why this lab matters (Story Arc Mapping)
| Story arc outcome | Foundry multi-agent output |
|---|---|
| Identify who needs attention now | Agent 3 alert table for VIP high-recency risk |
| Explain why risk is emerging | Agent 1 + Agent 2 scoring features and health signals |
| Recommend next human step | Agent 4 short-term action justification |
| Leadership visibility | Portfolio summary (tier counts, at-risk counts, at-risk % by tier) |

## Required Inputs
- `data/Zava Sales Data - FY2024-2026.xlsx`
- Facilitator-provided lifecycle definitions and output checklist

> **Upload note:** In Foundry, upload exported sheet files in Step 3 and create the synthetic news dataset in Step 9.

## Portal Assumptions (Tenant-Specific)
- Use the **New Foundry** portal experience for this lab (turn on the New Foundry toggle in the UI).
- **Project API key authentication is disabled** in this tenant; use signed-in user/project access only.
- Navigation path assumptions:
  - Optional project creation: **Start building -> Design workflow**.
  - Agent setup: **Build -> Agent**.
  - Data ingestion: **Build -> Data -> Files**.
  - Agent authoring/orchestration: **Build -> Workflows**.

## Synthetic News Guidance (for Agent 4)
- Use synthetic dataset **`synthetic_regional_news_24m`** covering the **most recent 24 months** only.
- Include regional events such as:
  - natural disasters,
  - major public events that may increase short-term demand,
  - supply disruptions affecting operations.
- Include fictional company references (for example: Contoso, Fabrikam, Northwind) in some events.
- Minimum recommended fields per news event:
  - `event_id`, `region`, `event_date`, `event_type`, `severity`,
  - `demand_signal` (`increase` or `decrease`),
  - `affected_companies`,
  - `event_summary`.
- Correlation guidance: compare customer behavior windows before/after events (for example 30 days pre vs 30 days post) to justify tactical actions.
- Exception handling rules:
  - Missing `region` -> `exception_missing_region` (exclude from correlation),
  - Non-fictional company references -> `exception_non_fictional_company` (exclude),
  - Malformed `event_date` -> `exception_malformed_date` (exclude),
  - Event outside last 24 months -> `exception_stale_record` (exclude).

## Step-by-Step (Navigate / Click / Type)
1. Open Foundry and enable New Foundry experience.
   - **Navigate:** Go to `https://ai.azure.com`.
   - **Type:** Log in with your tenant credentials.
   - **Click:** Turn on the **New Foundry** toggle in the page header (if not already on).
   - **Verify:** New Foundry layout is active.

2. (optional) Project setup.
   > **Note:** If a workshop project already exists, skip this step and continue to Step 3.
   - **Click:** Create project (if prompted).
   - **Type:** Name `customer-lifecycle-workshop`.
   - **Click:** Create and open project.
   - **Verify:** Project opens successfully.

3. Build RFM Agent.
   - **Click:** **Build** -> **Agent** -> **Create Agent**.
   - **Type:** Name the agent `agent1-rfm`.
   - **Type (instructions):** `Create one output row per customer_id with recency_days, frequency_90d, and monetary_90d using the uploaded files. Use recency as days since most recent purchase date. Use 90-day windows for frequency and monetary.`
   - **Click:** **Upload files**.
     - **Type/Select:** Drag and drop the files in `.\data\exported-sheets\`.
   - **Click:** **Save** the agent.
   - **Test (Message the agent...):** `Compute RFM for all customers and return customer_id, recency_days, frequency_90d, and monetary_90d.`
   - **Verify:** `recency_days`, `frequency_90d`, and `monetary_90d` are present with one row per customer.

4. Build Tiering Agent.
   - **Click:** **Build** -> **Agent** -> **Create Agent**.
   - **Type:** Name the agent `agent2-tier-health`.
   - **Type (instructions):** `Use Agent 1 RFM output to derive tiers (VIP/Gold/Silver/Bronze) and simple health indicators. Calculate negative_signal_count, triggered_signals, and risk_status using 0=healthy, 1=watch, 2+=at_risk.`
   - **Click:** **Upload files**.
     - **Type/Select:** Drag and drop the files in `.\data\exported-sheets\` (if they are not already available in this agent context).
   - **Click:** **Save** the agent.
   - **Test (Message the agent...):** `Using RFM input, return customer_id, tier, triggered_signals, negative_signal_count, and risk_status for all customers.`
   - **Verify:** Tier, signal, and risk-status fields are populated with 0/1/2+ mapping.

5. Build Threshold Agent.
   - **Click:** **Build** -> **Agent** -> **Create Agent**.
   - **Type:** Name the agent `agent3-vip-recency-alert`.
   - **Type (instructions):** `Apply rule tier='VIP' AND recency_days > 60. Add evidence fields vip_recency_threshold_days (=60) and agent3_rule_text (tier='VIP' AND recency_days > 60). Keep baseline risk gate aligned to 2+ negative signals => at_risk.`
   - **Click:** **Upload files**.
     - **Type/Select:** Drag and drop the files in `.\data\exported-sheets\` (if they are not already available in this agent context).
   - **Click:** **Save** the agent.
   - **Test (Message the agent...):** `Return VIP customers where recency_days > 60 and include customer_id, tier, recency_days, vip_recency_threshold_days, and agent3_rule_text.`
   - **Verify:** Alert rows are rule-driven and include threshold evidence fields.

6. Build News Agent.
   - **Click:** **Build** -> **Agent** -> **Create Agent**.
   - **Type:** Name the agent `agent4-news-scope-enforcement`.
   - **Type (instructions):** `Validate synthetic_regional_news_24m rows before correlation. Flag missing region as exception_missing_region, non-fictional company references as exception_non_fictional_company, malformed dates as exception_malformed_date, and stale/out-of-window rows as exception_stale_record. Exclude exception rows from downstream action evaluation.`
   - **Click:** **Upload files**.
     - **Type/Select:** Drag and drop the files in `.\data\exported-sheets\` (if they are not already available in this agent context).
   - **Click:** **Save** the agent.
   - **Test (Message the agent...):** `Validate synthetic regional news rows and return event_id with event_scope_status and exception code when applicable.`
   - **Verify:** Only in-scope rows continue and exception rows are clearly flagged.

7. Create/open the workflow artifact.
   - **Click:** **Build** -> **Workflows** -> **Create (Sequential)**.
   - **Click:** Save.
   - **Type:** Name `vip-lifecycle-management-flow`.
   - **Verify:** Workflow artifact is editable.

8. Define inter-agent handoff chain.
   - **Map:** `agent1_rfm` -> `agent2_tier_health` -> `agent3_vip_recency_alerts` -> `agent4_news_action_eval`.
     - **Click:** The first stubbed-out **Agent** node in the workflow canvas (this opens the configuration menu on the right).
     - **Type/Select:** Set this node to output `agent1_rfm` and click **Done**.
     - **Click:** The next stubbed-out **Agent** node and set its input to `agent1_rfm`, then set output to `agent2_tier_health`.
     - **Repeat:** Wire the next nodes to produce `agent3_vip_recency_alerts` and then `agent4_news_action_eval`.
   - **Click:** Save.

9. Create synthetic news source with exception-ready schema.
   - **Click:** **Build** -> **Data**.
   - **Click:** Create new table/dataset.
   - **Type:** Name `synthetic_regional_news_24m`.
   - **Type:** Add fields `event_id`, `region`, `event_date`, `event_type`, `severity`, `demand_signal`, `affected_companies`, `event_summary`.
   - **Type:** Add synthetic rows limited to last 24 months, including regional events and fictional companies.
   - **Verify:** Dataset exists and includes both increase/decrease demand examples.

10. Build Agent 4 (news-based short-term action evaluation).
    - **Click:** **Build** -> **Workflows**.
    - **Type:** Join customer/region/time context with validated synthetic news events.
    - **Type:** Generate short-term action rationale (for example outreach, promotion, retention focus) based on internal + external signal alignment.
    - **Click:** Run Agent 4 logic.
    - **Type:** Save output as `agent4_news_action_eval`.
    - **Verify:** Each recommended action includes event-based justification plus `event_scope_status`.

11. Produce required outputs.
    - **Type:** Compile final outputs:
      - at-risk VIP/Gold list,
      - explanation fields,
      - recommended actions,
      - portfolio summary (tier counts, at-risk counts, at-risk % by tier).
    - **Click:** Run and save final table(s).
    - **Verify:** Output matches the workshop output checklist.

12. Validate rule boundaries and agent coherence.
    - **Type:** Pull samples for 0/1/2/3+ negative-signal scenarios.
    - **Click:** Confirm status mapping (`0=healthy`, `1=watch`, `2+=at_risk`).
    - **Click:** Confirm Agent 3 rule text matches exactly `tier='VIP' AND recency_days > 60`.
    - **Click:** Spot-check at least 2 records where Agent 4 adds external context to justify short-term action.
    - **Verify:** Multi-agent outputs remain consistent with baseline rule contract.

13. Save outputs for downstream Agent Framework lab.
   - **Click:** Persist/export `agent2_tier_health`, `agent3_vip_recency_alerts`, and final output table.
   - **Verify:** Outputs are ready for the downstream Agent Framework lab.

## Timebox Guidance
1. **0-10 min:** Ingest source + create orchestration artifact.
2. **10-25 min:** Build Agent 1 and Agent 2.
3. **25-35 min:** Build Agent 3 rule output.
4. **35-50 min:** Build synthetic news dataset + Agent 4 evaluation.
5. **50-60 min:** Final output assembly + boundary validation.

## Scope-Cut Rule
If time runs short, keep Agents 1-3 and baseline outputs in class, then move deeper Agent 4 expansion to the after-class extensions backlog (do not delete).
