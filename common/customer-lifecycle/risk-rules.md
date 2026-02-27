# At-Risk Rule Contract

## Rule ID
`RISK-2PLUS-NEGATIVE-SIGNALS`

## Baseline Classification Contract (Level 200)
1. Evaluate all five lifecycle signals: recency, frequency, spend, margin, and mix.
2. Mark each signal as `negative` or `not negative`.
3. Count negatives as `negative_signal_count`.
4. Classify customer status:
   - `at_risk` when `negative_signal_count >= 2`
   - `watch` when `negative_signal_count = 1`
   - `healthy` when `negative_signal_count = 0`
5. Level 200 intervention outputs are required for at-risk VIP/Gold only.

## Explicit Gating Requirement
A customer **must not** be labeled at-risk from a single signal.  
At-risk status requires **two or more** negative signals in the same scoring window.

## Example Cases
| Negative signals | Example pattern | Classification | Action intensity |
|---:|---|---|---|
| 0 | Stable recency, frequency, spend, margin, mix | Healthy | No intervention; monitor normally |
| 1 | Frequency down only | Watch | Soft check-in only; no at-risk label |
| 2 | Recency up + spend down | At-risk | Retention outreach + account follow-up |
| 3+ | Recency up + frequency down + margin down (or broader decline) | At-risk | Escalated outreach + pricing/margin review; consider full recovery plan |

## Output Fields
- `negative_signal_count`
- `risk_status` (`healthy`, `watch`, `at_risk`)
- `triggered_signals` (list of signal names)
- `recommended_action_bundle`
