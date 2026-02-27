# Level 200 Lab: Agent Framework (10 Minutes)

## Goal
Demonstrate proactive, explain-only alerts for at-risk VIP/Gold customers using Level 200 outputs from Foundry.

## Inputs
- Level 200 scoring outputs from Foundry lab
- `common/customer-lifecycle/risk-rules.md`
- `common/customer-lifecycle/action-mapping.md`

## Step-by-Step (Navigate / Click / Type)
1. Open your Agent Framework project/session.
   - **Navigate:** Open the environment where the workshop agent flow is configured.
   - **Click:** Open the lifecycle alert workflow.
   - **Verify:** Workflow canvas/config is visible.

2. Load Foundry Level 200 outputs.
   - **Click:** Add input dataset / bind data source.
   - **Type:** Select the Foundry customer-level output and VIP/Gold at-risk subset generated in the prior lab.
   - **Click:** Confirm data binding.
   - **Verify:** Input schema includes `customer_id`, `tier`, `triggered_signals`, `negative_signal_count`, `risk_status`.

3. Configure alert trigger gating.
   - **Click:** Open trigger/filter configuration.
   - **Type:** Set filter to `tier in (VIP, Gold)` and `negative_signal_count >= 2` and `risk_status = at_risk`.
   - **Click:** Save trigger settings.
   - **Verify:** One-signal (`watch`) records are excluded.

4. Configure required alert payload.
   - **Click:** Open alert message template.
   - **Type:** Include fields:
     1. customer identifier and tier
     2. triggered negative signals
     3. plain-language risk explanation
     4. recommended human action bundle
   - **Click:** Save template.
   - **Verify:** Template contains all four required sections.

5. Run a test execution.
   - **Click:** Run test / simulate workflow.
   - **Type:** Use current Level 200 dataset snapshot.
   - **Click:** Execute.
   - **Verify:** Alerts are generated only for at-risk VIP/Gold customers.

6. Validate L200-only completion boundary.
   - **Click:** Review test output records.
   - **Verify:** No autonomous action is performed (explain-only alerts).
   - **Verify:** No 0/1-signal customer is alerted as at-risk.
   - **Verify:** Output remains aligned to `labs/customer-lifecycle/level-200/output-contract.md`.

7. Save evidence for facilitator.
   - **Click:** Export/copy alert run output.
   - **Type:** Record final check: "L200 complete; L300 not required for pass/fail."

## Timebox Guidance
1. **0-3 min:** Load outputs and configure trigger.
2. **3-7 min:** Configure template and run test.
3. **7-10 min:** Validate gating and save evidence.

## Baseline Constraints
- Alerts are explain-only (no autonomous customer contact).
- One-signal customers stay in watch status; no at-risk alert.
- Level 200 completion is sufficient for pass/fail; L300 is optional.
