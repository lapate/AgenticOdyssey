# Level 200 Lab: Microsoft Foundry (60 Minutes)

## Goal
Build structured lifecycle scoring outputs and enforce the Level 200 at-risk rule (`negative_signal_count >= 2`) before handing results to Agent Framework.

## Required Inputs
- `data/Zava Sales Data - FY2024-2026.xlsx`
- `data/customer-lifecycle/derived-fields.md`
- `common/customer-lifecycle/signal-dictionary.md`
- `common/customer-lifecycle/risk-rules.md`
- `labs/customer-lifecycle/level-200/output-contract.md`

## Step-by-Step (Navigate / Click / Type)
1. Open your Foundry project.
   - **Navigate:** Go to your Microsoft Foundry workspace.
   - **Click:** Open the project for this workshop.
   - **Click:** Open Data (or equivalent data management page).

2. Upload the workshop workbook.
   - **Click:** Upload data / Add file.
   - **Type:** Select `data/Zava Sales Data - FY2024-2026.xlsx`.
   - **Click:** Confirm upload.
   - **Verify:** Dataset appears in project assets.

3. Open a notebook/query workspace for transformation.
   - **Navigate:** Go to your project’s notebook, dataflow, or query tool.
   - **Click:** Create new analysis artifact.
   - **Type:** Title it `level-200-lifecycle-baseline`.

4. Create derived lifecycle fields.
   - **Type:** Implement derived fields from `data/customer-lifecycle/derived-fields.md` for recency, frequency, spend trend, margin trend, and mix trend.
   - **Click:** Run transformation.
   - **Verify:** Derived columns are present and populated.

5. Flag negative signals per customer.
   - **Type:** For each of the five signals, create a boolean/flag column that marks `negative` vs `not negative`.
   - **Click:** Run and preview results.
   - **Verify:** Every customer has five signal flags.

6. Calculate `negative_signal_count`.
   - **Type:** Sum all five negative flags into `negative_signal_count`.
   - **Click:** Run and preview.
   - **Verify:** Count is integer in range 0-5.

7. Apply risk classification rule.
   - **Type:** `if negative_signal_count >= 2 then at_risk; if =1 then watch; if =0 then healthy`.
   - **Click:** Run and save output table.
   - **Verify:** `risk_status` exists for all rows.

8. Produce the VIP/Gold at-risk subset.
   - **Type:** Filter where tier in (`VIP`, `Gold`) and `risk_status = at_risk`.
   - **Click:** Run and save as `vip_gold_at_risk`.
   - **Verify:** No row has `negative_signal_count < 2`.

9. Produce mandatory portfolio summary.
   - **Type:** Build tier-level summary with:
     - tier counts
     - at-risk counts
     - at-risk % by tier
   - **Click:** Run and save summary output.
   - **Verify:** Metrics are present for VIP, Gold, Silver, Bronze.

10. Run boundary validation samples.
   - **Type:** Pull at least one sample row each for 0, 1, 2, and 3+ negative signals.
   - **Click:** Compare each sample risk_status to rule.
   - **Verify:** 0=healthy, 1=watch, 2+=at_risk.

11. Save outputs for downstream lab.
   - **Click:** Persist/export customer-level baseline table, VIP/Gold subset, and portfolio summary.
   - **Verify:** Outputs are ready for `labs/customer-lifecycle/level-200/agent-framework.md`.

## Timebox Guidance
1. **0-10 min:** Load data and inspect schema.
2. **10-30 min:** Build derived fields.
3. **30-45 min:** Create flags/count.
4. **45-55 min:** Apply rule and generate outputs.
5. **55-60 min:** Validate boundary samples and save artifacts.
