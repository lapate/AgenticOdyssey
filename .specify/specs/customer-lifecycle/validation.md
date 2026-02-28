# Validation Checklist and Evidence Record

## FR-013..FR-020 Validation Checklist
| Check | Status | Evidence |
|---|---|---|
| Foundry guidance is architecture-agnostic and enforces 3-5 agents (FR-013, FR-019) | Pass | `labs/customer-lifecycle/level-300/foundry.md` (Core Design Rule), `labs/customer-lifecycle/level-300/output-contract.md` (Stage-Based Contract), `docs/customer-lifecycle/facilitator-guide.md` |
| Learner-visible stage map defines responsibilities, handoffs, and outcome markers (FR-015, FR-018) | Pass | `labs/customer-lifecycle/level-300/output-contract.md` (Section C), `labs/customer-lifecycle/level-300/foundry.md` (Stage Outcomes), `docs/customer-lifecycle/learner-guide.md` |
| Synthetic news scope remains explicit (24 months, regional events, fictional companies) (FR-014) | Pass | `labs/customer-lifecycle/level-300/foundry.md` (Synthetic News Constraints), `labs/customer-lifecycle/level-300/output-contract.md` (Stage 5 evidence fields), `common/customer-lifecycle/signal-dictionary.md` |
| Validation requires named-customer spot-check + aggregate artifact check (FR-016) | Pass | `labs/customer-lifecycle/level-300/foundry.md` (Validation Requirements), `docs/customer-lifecycle/learner-guide.md` (fallback runbook checks), `docs/customer-lifecycle/facilitator-guide.md` (FR-016 gate) |
| Failure-handling path covers blocked prompt, placeholder output, missing fields (FR-017) | Pass | `labs/customer-lifecycle/level-300/foundry.md` (Failure Handling Decision Path), `common/customer-lifecycle/risk-rules.md`, `common/customer-lifecycle/signal-dictionary.md` |
| Guardrail-safe fallback path preserves primary-path outcomes/evidence (FR-020) | Pass | `labs/customer-lifecycle/level-300/foundry.md` (Guardrail-Safe Fallback Pattern), `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md` |

## Validation Walkthrough Records (T014)

### Walkthrough 1: Named-Customer Spot-Check
- Customer used: `Contoso, Ltd.`
- Path executed:
  1. Confirm row exists in `stage1_ingest_score`.
  2. Confirm `Contoso, Ltd.` carries forward to `stage2_tier_risk` with `triggered_signals`, `negative_signal_count`, `risk_status`.
  3. Confirm `stage3_explain_action` includes plain-language explanation and recommended action for same `customer_id`.
- Outcome: **Pass**
- Remediation needed: None.

### Walkthrough 2: Aggregate Portfolio Check
- Artifact used: `stage4_portfolio_summary`
- Checks executed:
  1. Tier counts present for VIP/Gold/Silver/Bronze.
  2. At-risk counts present per tier.
  3. At-risk % by tier present and formula-consistent (`at_risk_count / tier_count`).
- Outcome: **Pass**
- Remediation needed: None.

### Walkthrough 3: Failure Scenario A - Guardrail Blocked Prompt
- Triggered failure code: `guardrail_blocked`
- Primary-path issue: table-wide prompt blocked by tenant guardrails.
- Remediation steps:
  1. Switched to artifact-first execution in Workflows.
  2. Re-ran stage artifacts sequentially.
  3. Re-ran named-customer and aggregate checks.
- Outcome after remediation: **Pass**
- Notes: Fallback path produced equivalent Level 300 outcomes/evidence.

### Walkthrough 4: Failure Scenario B - Placeholder/Generic Output
- Triggered failure code: `placeholder_output`
- Primary-path issue: output returned example-like text without source lineage.
- Remediation steps:
  1. Re-ran failed stage with explicit source-only constraints.
  2. Required evidence fields were enforced in output.
  3. Downstream stage was rerun for consistency.
- Outcome after remediation: **Pass**
- Notes: No placeholder artifacts remained.

### Walkthrough 5: Failure Scenario C - Missing Required Fields
- Triggered failure code: `missing_required_fields`
- Primary-path issue: one stage artifact omitted required handoff/evidence fields.
- Remediation steps:
  1. Marked artifact `needs rework`.
  2. Applied targeted stage rework.
  3. Reran downstream dependent stage(s).
  4. Rechecked status until required artifacts were `complete`.
- Outcome after remediation: **Pass**
- Notes: Stop condition satisfied only after field completeness restored.

## Cross-Document Parity Notes
- Terminology now consistently uses stage outcomes + 3-5 agent architecture-agnostic wording.
- L300 core completion remains mandatory; L400 remains optional-only.
- Validation gates now consistently reference source-derived evidence and fallback parity.
