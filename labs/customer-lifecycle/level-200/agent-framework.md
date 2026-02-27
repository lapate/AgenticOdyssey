# Level 200 Lab: Agent Framework (10 Minutes)

## Goal
Demonstrate proactive, explain-only alerts for at-risk VIP/Gold customers based on the baseline lifecycle rule.

## Inputs
- Level 200 scoring outputs from Foundry lab
- `common/customer-lifecycle/risk-rules.md`
- `common/customer-lifecycle/action-mapping.md`

## Timebox Plan
1. **0-3 min**: Load prepared customer risk output.
2. **3-7 min**: Trigger alert generation for VIP/Gold where `negative_signal_count >= 2`.
3. **7-10 min**: Review alert explanations and recommended actions.

## Alert Contract
Each alert must include:
- Customer identifier and tier
- Triggered negative signals
- Plain-language risk explanation
- Recommended human action bundle

## Baseline Constraints
- Alerts are explain-only (no autonomous customer contact).
- One-signal customers stay in watch status; no at-risk alert.
- Portfolio roll-up is preserved from Level 200 output contract.
