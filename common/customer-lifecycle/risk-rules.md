# At-Risk Rule Contract

## Rule ID
`RISK-2PLUS-NEGATIVE-SIGNALS`

## Canonical VIP Recency Alert Threshold (Agent 3)
- Threshold value: **60 days**.
- Canonical Agent 3 rule expression: **`tier='VIP' AND recency_days > 60`**.
- This Agent 3 alert rule is an explicit VIP escalation signal and does not override the baseline at-risk gate (`negative_signal_count >= 2`).

### Agent 3 Threshold Evidence Fields (Required)
Every `agent3_vip_recency_alerts` output row must include:
- `vip_recency_threshold_days` (=60),
- `agent3_rule_text` (`tier='VIP' AND recency_days > 60`),
- `alert_flag` (true/false result of the threshold rule).

These fields are required evidence that the threshold check was applied as documented.

## Baseline Classification Contract (Level 300)
1. Evaluate all five lifecycle signals: recency, frequency, spend, margin, and mix.
2. Mark each signal as `negative` or `not negative`.
3. Count negatives as `negative_signal_count`.
4. Classify customer status:
   - `at_risk` when `negative_signal_count >= 2`
   - `watch` when `negative_signal_count = 1`
   - `healthy` when `negative_signal_count = 0`
5. Level 300 intervention outputs are required for at-risk VIP/Gold only.

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
