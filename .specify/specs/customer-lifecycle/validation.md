# Validation Checklist and Dry-Run Record

## Checklist
| Check | Status | Evidence |
|---|---|---|
| Spec-to-plan traceability exists for FR-001..FR-008 and NFR-001..NFR-005 | Pass | `.specify/specs/customer-lifecycle/traceability.md` |
| Level 200 baseline outputs defined (at-risk VIP/Gold, explanation, action, portfolio summary) | Pass | `labs/customer-lifecycle/level-200/output-contract.md` |
| 2+ negative-signal rule consistently enforced | Pass | `common/customer-lifecycle/risk-rules.md`, `labs/customer-lifecycle/level-200/foundry.md`, `docs/customer-lifecycle/learner-guide.md` |
| Terminology consistency (customer health, risk signals, tiers, actions) | Pass | `common/customer-lifecycle/signal-dictionary.md`, `docs/customer-lifecycle/*.md` |
| Optional extension isolation from baseline pass/fail | Pass | `labs/customer-lifecycle/level-300/extensions.md`, `labs/customer-lifecycle/level-200/output-contract.md` |
| Documentation parity (labs vs facilitator/learner guides) | Pass | `docs/customer-lifecycle/facilitator-guide.md`, `docs/customer-lifecycle/learner-guide.md` |

## Dry-Run Outcomes (Documentation Walkthrough)
Scope reviewed:
- `labs/customer-lifecycle/level-200/copilot-studio.md`
- `labs/customer-lifecycle/level-200/foundry.md`
- `labs/customer-lifecycle/level-200/agent-framework.md`
- `docs/customer-lifecycle/facilitator-guide.md`
- `docs/customer-lifecycle/learner-guide.md`

### Result Summary
| Scenario | Outcome | Notes |
|---|---|---|
| 0 negative signals | Pass | Correctly described as `healthy` |
| 1 negative signal | Pass | Correctly described as `watch`; no at-risk label |
| 2 negative signals | Pass | Correctly described as `at_risk` with action mapping |
| 3+ negative signals | Pass | Correctly escalated as at-risk with stronger action bundle |
| Portfolio roll-up presence | Pass | Tier counts + at-risk counts + at-risk % by tier explicitly required |
| Level 300 isolation | Pass | Optional pack marked non-blocking for Level 200 |

## Follow-Ups
- None blocking. Baseline requirements and parity checks are satisfied.
