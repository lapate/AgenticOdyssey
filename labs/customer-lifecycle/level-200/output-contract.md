# Level 200 Mandatory Output Contract

All Level 200 submissions must satisfy this contract.

## A. Portfolio Metrics (Required)
| Metric | Required format |
|---|---|
| Tier counts | Count of customers by VIP/Gold/Silver/Bronze |
| At-risk counts | Count of `risk_status = at_risk` by tier |
| At-risk % by tier | `at-risk count / tier count` for each tier |

## B. At-Risk Customer Outputs (Required)
For each at-risk VIP/Gold customer:
1. Customer ID and tier
2. Triggered signal list
3. `negative_signal_count` (must be >=2)
4. Plain-language explanation of risk drivers
5. Mapped human action (from action mapping matrix)

## C. Rule Enforcement (Required)
- A customer with 0 signals: `healthy`
- A customer with 1 signal: `watch`
- A customer with 2+ signals: `at_risk`
- Any output labeling 0/1-signal customer as at-risk is a baseline failure.

## D. Pass/Fail Boundary
- **Pass (Level 200):** Sections A+B+C fully met.
- **Not required for pass:** Any Level 300 extension artifact.
