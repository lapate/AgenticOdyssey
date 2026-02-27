# Level 200 Lab: Copilot Studio (30 Minutes)

## Goal
Use conversational prompts to identify at-risk **VIP/Gold** customers, explain risk in plain language, and propose a human action.

## Inputs
- `data/Zava Sales Data - FY2024-2026.xlsx`
- Derived field logic from `data/customer-lifecycle/derived-fields.md`
- Shared terminology and rules from `common/customer-lifecycle/*.md`

## Timebox Plan
1. **0-5 min**: Load context and ask for lifecycle objective summary.
2. **5-15 min**: Prompt for at-risk VIP/Gold list using 2+ negative-signal gate.
3. **15-25 min**: Prompt for plain-language explanation + action per customer.
4. **25-30 min**: Produce portfolio summary snippet for facilitator review.

## Required Prompt Flow
1. Ask for customers where tier in (VIP, Gold).
2. Require `negative_signal_count` and reject `at_risk` labels where count < 2.
3. For each at-risk customer, return:
   - Triggered signals
   - Plain-language explanation
   - Recommended human action bundle
4. Return portfolio summary:
   - Tier counts
   - At-risk counts
   - At-risk % by tier

## Minimum Deliverable
- Table of at-risk VIP/Gold customers with `negative_signal_count >= 2`
- One plain-language explanation per at-risk customer
- One action recommendation per at-risk customer
- Portfolio summary metrics

## Guardrails
- Do not use external data.
- Do not classify a one-signal customer as at-risk.
- Keep wording business-friendly (no model jargon).
