# Level 200 Lab: Copilot Studio (30 Minutes)

## Goal
Use Copilot Studio to produce required Level 200 outputs: at-risk VIP/Gold identification, plain-language explanations, recommended actions, and portfolio summary metrics.

## Required Inputs
- `data/Zava Sales Data - FY2024-2026.xlsx`
- `data/customer-lifecycle/derived-fields.md`
- `common/customer-lifecycle/signal-dictionary.md`
- `common/customer-lifecycle/risk-rules.md`
- `labs/customer-lifecycle/level-200/output-contract.md`

## Step-by-Step (Navigate / Click / Type)
1. Open Copilot Studio.
   - **Navigate:** Go to `https://copilotstudio.preview.microsoft.com/`.
   - **Click:** Select your workshop environment.
   - **Click:** Open the copilot or topic assigned by your facilitator.

2. Create a new test conversation for this lab run.
   - **Navigate:** Open the test chat panel in Copilot Studio.
   - **Click:** New conversation (or Reset conversation).
   - **Type:** `Start Level 200 customer lifecycle analysis for VIP and Gold tiers only.`
   - **Click:** Send.

3. Set the scope and at-risk rule before analysis.
   - **Type:** `Use only the provided Zava workshop dataset and derived fields. Apply this rule: at_risk only when negative_signal_count >= 2; watch when =1; healthy when =0. Confirm this rule back to me before listing customers.`
   - **Click:** Send.
   - **Verify:** Response confirms the exact 0/1/2+ rule.

4. Request at-risk VIP/Gold identification.
   - **Type:** `List all customers where tier is VIP or Gold and risk_status is at_risk. Include customer_id, tier, triggered_signals, and negative_signal_count. Exclude any record with negative_signal_count < 2.`
   - **Click:** Send.
   - **Verify:** Every returned at-risk customer has `negative_signal_count >= 2`.

5. Request plain-language explanation for each at-risk VIP/Gold customer.
   - **Type:** `For each listed at-risk VIP/Gold customer, explain risk drivers in plain business language (no technical jargon) using recency, frequency, spend, margin, and mix signals where relevant.`
   - **Click:** Send.
   - **Verify:** Each customer has a readable business explanation.

6. Request one recommended human action per at-risk VIP/Gold customer.
   - **Type:** `For each at-risk VIP/Gold customer, provide one recommended human action (retention outreach, account follow-up, pricing/margin review, or targeted offer) and briefly justify it.`
   - **Click:** Send.
   - **Verify:** Every listed customer includes one concrete human action.

7. Request portfolio summary metrics (mandatory).
   - **Type:** `Provide a portfolio summary table with tier counts, at-risk counts, and at-risk percentage by tier for VIP, Gold, Silver, and Bronze.`
   - **Click:** Send.
   - **Verify:** All three metrics are present for each tier.

8. Run boundary check for 0/1/2/3+ signals.
   - **Type:** `Show one example each for customers with 0, 1, 2, and 3+ negative signals and confirm risk_status for each example according to the 2+ rule.`
   - **Click:** Send.
   - **Verify:** 0=healthy, 1=watch, 2+=at_risk.

9. Save your Level 200 result evidence.
   - **Click:** Copy/export the final response set from the chat.
   - **Type:** Save notes with sections: At-risk VIP/Gold list, explanations, actions, portfolio summary, boundary check.
   - **Verify:** Evidence includes all required Level 200 outputs from `output-contract.md`.

## Timebox Guidance
1. **0-5 min:** Open environment and set rule/scope.
2. **5-15 min:** Identify at-risk VIP/Gold customers.
3. **15-25 min:** Add explanations and actions.
4. **25-30 min:** Produce portfolio summary and boundary check.

## Guardrails
- Use only workshop-provided inputs.
- Never label 0/1-signal customers as at-risk.
- Keep language business-friendly.
