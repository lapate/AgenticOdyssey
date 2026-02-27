# Level 200 Lab: Microsoft Foundry (60 Minutes)

## Goal
Prepare structured lifecycle scoring outputs using the provided dataset and enforce the 2+ negative-signal at-risk rule.

## Inputs
- `data/Zava Sales Data - FY2024-2026.xlsx`
- `data/customer-lifecycle/derived-fields.md`
- `common/customer-lifecycle/signal-dictionary.md`
- `common/customer-lifecycle/risk-rules.md`

## Timebox Plan
1. **0-10 min**: Ingest workbook and inspect core fields.
2. **10-30 min**: Build derived fields (recency, frequency, spend, margin, mix).
3. **30-45 min**: Create signal flags and `negative_signal_count`.
4. **45-55 min**: Apply risk classification with 2+ gate.
5. **55-60 min**: Generate portfolio summary outputs.

## Baseline Logic Contract
```text
if negative_signal_count >= 2 -> at_risk
if negative_signal_count = 1  -> watch
if negative_signal_count = 0  -> healthy
```

## Required Outputs
1. Customer-level table containing:
   - Customer ID, Tier
   - Triggered signals
   - negative_signal_count
   - risk_status
2. VIP/Gold at-risk subset (`risk_status = at_risk` and tier in VIP/Gold)
3. Portfolio summary with:
   - Tier counts
   - At-risk counts
   - At-risk percentage by tier

## Quality Checks
- Validate sample records for 0/1/2/3+ signal behavior.
- Confirm no at-risk record has `negative_signal_count < 2`.
- Confirm terminology uses customer health/risk signals/tiers/actions consistently.
