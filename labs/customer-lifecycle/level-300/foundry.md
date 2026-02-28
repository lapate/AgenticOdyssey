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
| `agent1-customers` | `agent1-customer-index` |
| `agent2-tier` | `agent2-tier-report-{{customer_id}}` |
| `agent3-explain-action` | `stage3_explain_action` |
| `agent4-portfolio-summary` | `stage4_portfolio_summary` |

Notes:

- **3-agent option:** keep `agent1-customers`, then merge Stage 3 + Stage 4 responsibilities.
- **4-agent default:** keep `agent1-customers`, `agent2-tier`, `agent3-explain-action`, and `agent4-portfolio-summary` as separate agents.
- **5-agent option:** split Stage 2 logic back into a separate helper agent if you want to teach finer-grained handoffs.
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

2. (optional) Project setup.
   > **Note:** If a workshop project already exists, skip this step and continue to Step 3.
   - **Click:** Create project (if prompted).
   - **Type:** Name `customer-lifecycle-workshop`.
   - **Click:** Create and open project.
   - **Verify:** Project opens successfully.

3. Build Agent 1 (`agent1-customers`) for customer indexing.
   - **Click:** **Build -> Agent -> Create Agent**.
   - **Type:** Name `agent1-customers`.
   - **Type/Select (model):** Choose `gpt-5-mini`.
   - **Type (instructions):**

      ```text
      ## Role & Task
      You are **Agent 1 (Customer Indexer)** in a multi-agent customer lifecycle workflow.  
      Your task is to process all uploaded source files and produce a baseline list of unique customers used for downstream scoring, tiering, and alerting steps.

      ## Input Selection Rules
      - Use uploaded source data (`*.txt` parsed as CSV) as the required underlying data source.
      - Do not use any external data sources.

      ## Input Parsing Rules
      For every uploaded `*.txt` file, parse as CSV with first row as column headers, delimiter `,` and text qualifier `"` (double quote).

      ## Computation Rules
      - Deduplicate customers so each customer appears once.
      - If a requested customer is not found, return `not_found`.
      - Do **not** return example or placeholder data.

      ## Output Requirements
      - Create and return **only** a markdown table as an artifact named `agent1-customer-index` with the following headers:  
      `customer_id | customer_name`
      - Create one output row per unique customer/company.
      - Do **not** include any additional commentary or notes.
      ```

   - **Click:** **Upload files -> Attach**
     > **Drag and Drop** the files in `.\data\exported-sheets\`.
   - **Click:** **Save**.
   - **Test (Message the agent...):** `Return the customer list.`
   - **Verify:** Output contains unique customer rows with no duplicates.

4. Build Agent 2 (`agent2-tier`) for Stage 2.
   - **Click:** **Build -> Agent -> Create Agent**.
   - **Type:** Name `agent2-tier`.
   - **Type/Select (model):** Choose `gpt-5-chat`.
   - **Type (instructions):**

      ```text
      ## Role & Task
      You are **Agent 2 (Tier)** in a multi-agent customer lifecycle workflow.
      Your task is to process **exactly one customer per run** and produce a combined **RFM + Tier** report for downstream explanation and portfolio steps.

      ## Input Selection Rules
      - Use uploaded source data (`*.txt` parsed as CSV) as the required underlying data source.
      - Identify **exactly one** customer by `customer_name` or `customer_id` from `agent1-customer-index`.
        - If `agent1-customer-index` is not available, resolve the customer directly from the uploaded source data using the prompt value and set `customer_id` as 'UNDEFINED'.
        - If the prompt does **not** resolve to exactly one customer, return `not_found` or `multiple_matches`.

      ## Input Parsing Rules
      For every uploaded `*.txt` file, parse as CSV with first row as column headers, delimiter `,` and text qualifier `"` (double quote).

      ## Fixed Field Mapping (no clarification)
      - Purchase date: use `Order Date` for recency and 90-day window calculations.
      - Monetary field: use `Total Revenue` for `monetary_90d` (parse currency-formatted values to numeric).
      - Customer entity: treat each distinct `Customer` value as a unique customer/company (including labels like `Direct eCommerce` and `Sporting Goods Retail`).
      - `rfm_window_days` = `90`.
      - `rfm_run_timestamp` = current run date in `YYYY-MM-DD` format.

      ## Computation Rules
      For the **resolved customer only**:
      - `recency_days`: days since the most recent `Order Date`.
      - `frequency_90d`: number of purchases in the trailing 90 days.
      - `monetary_90d`: sum of `Total Revenue` in the trailing 90 days.
      - Derive `tier` and health/risk outputs from the RFM values.
      - Enforce risk gate: if `negative_signal_count >= 2`, then `risk_status = at_risk`.
      - Do **not** return example or placeholder data.

      ## Output Requirements
      - Create and return **only** a markdown table with the following headers as an artifact named `agent2-tier-report-{{customer_id}}`
      `customer_id | customer_name | recency_days | frequency_90d | monetary_90d | rfm_window_days | rfm_run_timestamp | tier | triggered_signals | negative_signal_count | risk_status | risk_gate_rule_text`
      - Do **not** include any additional commentary or notes.
      ```

   - **Click:** **Upload files -> Attach**
     > **Select** the existing Index (generated with `agent1-customers` configuration).
   - **Click:** **Save**.
   - **Test (Message the agent...):** `Generate a report for 'Contoso, Ltd.'`
   - **Verify:** Response contains real values (not placeholders).

5. Build Agent 3 (`agent3-explain-action`) for Stage 3.
   - **Click:** **Build -> Agent -> Create Agent**.
   - **Type:** Name `agent3-explain-action`.
   - **Type/Select (model):** Choose `gpt-5-chat`.
   - **Type (instructions):**

      ```text
      ## Role & Task
      You are **Agent 3 (Explain + Action)** in a multi-agent customer lifecycle workflow.
      Your task is to process **exactly one customer per run** and produce a plain-language risk explanation plus recommended action from Stage 2 outputs.

      ## Input Selection Rules
      - Use `agent2-tier-report-{{customer_id}}` as the required upstream input.
      - Identify exactly one customer by `customer_name` or `customer_id` from that Stage 2 artifact.
      - If the Stage 2 artifact is unavailable, run/stitch `agent1-customers -> agent2-tier` first, save `agent2-tier-report-{{customer_id}}`, then rerun Agent 3.
      - If the prompt does not resolve to exactly one customer (0 or multiple matches), return `not_found`.

      ## Computation Rules
      For the resolved customer only:
      - Generate `risk_explanation_plain` in clear business language grounded in Stage 2 fields.
      - Generate `action_recommendation` and `action_rationale` aligned to tier/risk context.
      - Preserve Stage 2 risk-gate interpretation (`negative_signal_count >= 2 => at_risk`) in the explanation.
      - If enrichment mode is enabled, also populate `stage5_news_enrichment` using `synthetic_regional_news_24m` with `event_scope_status` and `news_exception_code`.
      - Do **not** return example or placeholder data.

      ## Output Requirements
      - Create and return **only** a markdown table as artifact `stage3_explain_action` with headers:
      `customer_id | tier | risk_explanation_plain | action_recommendation | action_rationale | action_mapping_version | derived_from_stage2_artifact`
      - Do **not** include additional commentary or notes.
      ```

   - **Click:** **Upload files -> Attach**
     > **Select** `agent2-tier-report-{{customer_id}}` for the target customer (generate via `agent1-customers -> agent2-tier` workflow first if needed).
   - **Click:** **Save**.
   - **Test (Message the agent...):** `Return stage3_explain_action row for customer_name='Contoso, Ltd.' with risk_explanation_plain, action_recommendation, and action_rationale.`
   - **Verify:** Explanation is business-readable and action is explicit.

6. Build Agent 4 (`agent4-portfolio-summary`) for Stage 4.
   - **Click:** **Build -> Agent -> Create Agent**.
   - **Type:** Name `agent4-portfolio-summary`.
   - **Type (instructions):** `Aggregate agent2-tier-report-{{customer_id}} into stage4_portfolio_summary with tier_count, at_risk_count, and at_risk_pct by tier plus required evidence fields.`
   - **Click:** **Save**.
   - **Test (Message the agent...):** `Return stage4_portfolio_summary for all tiers.`
   - **Verify:** Tier counts, at-risk counts, and at-risk % are present.

7. (Optional) Enable Stage 5 news enrichment in Agent 3.
   - **Type:** In `agent3-explain-action`, enable enrichment mode using `synthetic_regional_news_24m`.
   - **Type:** Ensure output includes `stage5_news_enrichment` fields when enrichment is used.
   - **Verify:** Enrichment rows include `news_dataset_name`, `scope_window_months`, `event_scope_status`, and `news_exception_code`.

8. Create workflow and wire agent chain.
   - **Click:** **Build -> Workflows -> Create (Sequential)**.
   - **Type:** Name `vip-lifecycle-management-flow`.
   - **Prerequisite:** Ensure `agent1-customer-index` is available as input for `agent2-tier`.
   - **Wire (default 4-agent):**
     - `agent1-customers` -> `agent2-tier` -> `agent3-explain-action` -> `agent4-portfolio-summary`
   - **Wire (if 3-agent variant):**
     - Keep `agent1-customers` first, then merge Stage 3 + Stage 4 responsibilities while preserving required artifacts.
   - **Wire (if 5-agent variant):**
     - Add an optional helper between `agent2-tier` and `agent3-explain-action`.
   - **Verify:** Total agent count is between 3 and 5.

9. Run workflow (primary path) and save artifacts.
   - **Click:** Run workflow.
   - **Type:** Save outputs as stage artifacts:
      - `agent1-customer-index`
     - `agent2-tier-report-{{customer_id}}`
     - `stage3_explain_action`
     - `stage4_portfolio_summary`
     - `stage5_news_enrichment` (if used)
   - **Verify:** Artifacts exist and required fields/evidence are populated per `output-contract.md`.

10. Run required validation checks.
    - **Named-customer spot-check (required):**
      - Trace `Contoso, Ltd.` from Stage 2 -> Stage 3 (and Stage 5 if used).
   - **Customer index check (required):**
      - Verify `agent1-customer-index` contains unique `customer_id` + `customer_name` rows.
   - **Aggregate artifact check (required):**
     - Validate Stage 4 tier counts, at-risk counts, and at-risk % by tier.
   - **Verify:** Outputs cover identification, explanation, action, and portfolio summary with source-derived values.

11. Apply failure handling if needed.
   - `guardrail_blocked` -> switch to fallback path (Step 12), then re-run Step 10.
   - `placeholder_output` -> rerun failed stage with source-only and explicit field constraints.
   - `missing_required_fields` -> mark artifact `needs rework`, rerun failed stage and downstream stages.

12. Guardrail-safe fallback path (artifact-first).
   - **Run stages individually** in Workflows/Artifacts (avoid full-table chat response requests).
   - **Validate each stage artifact** before moving to the next stage.
   - **Assemble final outputs** from saved artifacts.
   - **Re-run Step 10 checks** and keep the same evidence set.

## Timebox Guidance
1. **0-10 min:** Data setup + create first two agents.
2. **10-30 min:** Build Stage 2-3 agents and quick spot-checks.
3. **30-45 min:** Build Stage 4 (and Stage 5 if used) + wire workflow.
4. **45-60 min:** Run full workflow + required validation + fallback remediation if needed.
