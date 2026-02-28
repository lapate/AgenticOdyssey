# Lab: Copilot Studio (30 Minutes)

## Goal
Build/configure a Copilot Studio artifact, then use it to deliver baseline outputs:
1. at-risk VIP/Gold identification,
2. plain-language risk explanation,
3. recommended human action,
4. portfolio summary metrics.

## Why this lab matters (Story Arc Mapping)
| Story arc outcome | What you produce in this lab |
|---|---|
| Identify who needs attention now | At-risk VIP/Gold list with `negative_signal_count >= 2` |
| Explain why risk is emerging | Plain-language explanation per at-risk customer |
| Recommend next human step | One action recommendation per at-risk customer |
| Provide leadership visibility | Tier counts, at-risk counts, and at-risk % by tier |

## Required Inputs
- `data/Zava Sales Data - FY2024-2026.xlsx`
- Facilitator-provided lifecycle definitions and output checklist
- `labs/customer-lifecycle/level-300/output-contract.md` (for stage outcome parity with Foundry)

## Preview UI Note (Important)
Use these UI anchors for this lab:
- Left nav: **Agents**
- In an opened agent: **Overview**, **Knowledge**, **Activity**

If your tenant labels differ slightly, follow the intent of each step.

## Phase 1 - Build/Configure Artifact (0-10 min)
1. Open portal and select environment.
   - **Navigate:** `https://copilotstudio.preview.microsoft.com/`
   - **Click:** Environment selector and choose workshop environment.
   - **Verify:** Copilot Studio home loads.

2. Create (or open editable) copilot.
   - **Click:** Left nav **Agents**.
   - **Click:** Create/New agent (or open facilitator draft with edit rights).
   - **Type:** Name: `Customer Lifecycle Baseline`
   - **Click:** Create/Open.
   - **Verify:** Agent opens and **Overview** and **Knowledge** tabs are available.

3. Configure behavior contract (required baseline config).
   - **Click:** Top tab **Overview**.
   - **Click:** Instructions / System message field.
   - **Type (paste):**
     ```text
     Use only workshop-provided customer lifecycle data context.
     Apply risk rule exactly:
     - at_risk when negative_signal_count >= 2
     - watch when negative_signal_count = 1
     - healthy when negative_signal_count = 0
     For at-risk VIP/Gold customers, return:
     customer_id, tier, triggered_signals, negative_signal_count,
     plain-language explanation, recommended human action.
     Also provide tier counts, at-risk counts, and at-risk % by tier.
     ```
   - **Click:** Save.
   - **Verify:** Saved instructions are visible.

4. Add knowledge/data context.
   - **Click:** Top tab **Knowledge**.
   - **Click:** Add source.
   - **Type/Select:** Attach workshop source (Excel file or facilitator-provided prepared data context).
   - **Click:** Save/Connect.
   - **Verify:** Source appears as active/connected.

5. Save (and publish draft if your UI requires it before testing).
   - **Click:** Save.
   - **Click:** Publish (if enabled/required in your tenant).
   - **Verify:** No blocking validation errors.

## Phase 2 - Run Guided Conversation (10-27 min)
6. Start fresh test chat.
   - **Navigate:** **Overview** test chat panel (or equivalent test pane in your tenant).
   - **Click:** New chat / Reset.
   - **Type:** `Start customer lifecycle analysis for VIP and Gold tiers only.`
   - **Click:** Send.

7. Confirm rule lock (quality gate).
   - **Type:** `Confirm the exact risk gate and statuses: at_risk >=2, watch =1, healthy =0.`
   - **Click:** Send.
   - **Verify:** Response matches 0/1/2+ contract exactly.

8. Generate at-risk VIP/Gold list (Story arc: who needs attention).
   - **Type:** `List VIP/Gold customers with risk_status = at_risk. Include customer_id, tier, triggered_signals, negative_signal_count. Exclude any row with negative_signal_count < 2.`
   - **Click:** Send.
   - **Verify:** Every returned at-risk row has `negative_signal_count >= 2`.

9. Generate explanations + actions (Story arc: why + what next).
   - **Type:** `For each listed at-risk VIP/Gold customer, provide a plain-language explanation and one recommended human action with brief justification.`
   - **Click:** Send.
   - **Verify:** Every customer has explanation + action.

10. Generate portfolio summary (Story arc: leadership visibility).
    - **Type:** `Provide a portfolio summary table with tier counts, at-risk counts, and at-risk percentage by tier for VIP, Gold, Silver, and Bronze.`
    - **Click:** Send.
    - **Verify:** All 3 metrics appear for each tier.

## Phase 3 - Validate in Activity (27-30 min)
11. Run boundary validation.
    - **Type:** `Show one example each for 0, 1, 2, and 3+ negative signals and confirm risk_status for each.`
    - **Click:** Send.
    - **Verify:** 0=healthy, 1=watch, 2+=at_risk.

12. Use Activity as the validation source (no export required for this lab).
    - **Click:** Top tab **Activity**.
    - **Click:** Open one of your completed conversations.
    - **Click:** Toggle view between **Transcript + map view** and **map view**.
    - **Compare:** Use this conversation as your source to confirm all required outputs in the workshop output checklist:
      1. at-risk VIP/Gold list with `negative_signal_count >= 2`,
      2. plain-language explanations,
      3. recommended human actions,
      4. portfolio summary metrics,
      5. 0/1/2/3+ boundary check.
    - **Verify:** You can locate each required output in Activity-backed conversation history.

## Foundry Parity Note
- Copilot Studio outputs should align with Foundry stage outcomes:
  - identification parity with `stage2_tier_risk`,
  - explanation/action parity with `stage3_explain_action`,
  - portfolio summary parity with `stage4_portfolio_summary`.
- Do not assume or require a fixed Foundry topology; parity is outcome-based.
