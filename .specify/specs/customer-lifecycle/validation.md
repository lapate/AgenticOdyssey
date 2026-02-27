# Validation Checklist and Dry-Run Record

## T012 - README Getting Started + Link Integrity
| Check | Status | Evidence |
|---|---|---|
| TOC appears near top of README | Pass | `README.md` ("Table of Contents" section) |
| Top-level flow order is Copilot Studio -> Foundry -> Agent Framework | Pass | `README.md` ("Workshop Demo Flow") |
| First-step onboarding is explicit | Pass | `README.md` ("First-Time Onboarding") |
| Returning-user fast path is explicit | Pass | `README.md` ("Returning Learner Fast Path") |
| L200 lab links present and internally consistent | Pass | `README.md`, `docs/customer-lifecycle/learner-guide.md` |

## T013 - Copilot Studio Step-Completeness Validation
Scope reviewed:
- `labs/customer-lifecycle/level-200/copilot-studio.md`

| Validation point | Status | Findings |
|---|---|---|
| Every step is strictly numbered | Pass | Steps 1-9 are numbered and sequential |
| Every step includes explicit navigate/click/type action(s) | Pass | Each numbered step includes action labels |
| URL for Copilot Studio is explicit | Pass | `https://copilotstudio.preview.microsoft.com/` included in Step 1 |
| Required output prompts include exact text to enter | Pass | Steps 3-8 provide exact prompt text |

## T014 - L100/L200/L300 Definition Parity Validation
Artifacts checked:
- `README.md`
- `docs/customer-lifecycle/learner-guide.md`
- `docs/customer-lifecycle/facilitator-guide.md`
- `common/customer-lifecycle/signal-dictionary.md`
- `labs/customer-lifecycle/level-200/*.md`
- `labs/customer-lifecycle/level-300/extensions.md`

| Validation point | Status | Findings |
|---|---|---|
| L100 definition parity | Pass | Wording aligned across README + learner/facilitator + common dictionary |
| L200 definition parity | Pass | Marked as required baseline for completion/pass in all learner/facilitator entry docs |
| L300 WWL-aligned optional definition parity | Pass | Explicit "advanced hands-on practice building on L100/L200; optional; excluded from pass/fail" retained |
| Pass/fail boundary parity (L200 required, L300 optional) | Pass | Consistent across README, facilitator guide, learner guide, extensions, output contract |

## T015 - L200 Output Contract Validation
Artifacts checked:
- `labs/customer-lifecycle/level-200/output-contract.md`
- `labs/customer-lifecycle/level-200/foundry.md`
- `labs/customer-lifecycle/level-200/agent-framework.md`
- `docs/customer-lifecycle/learner-guide.md`
- `docs/customer-lifecycle/facilitator-guide.md`

| Required output | Status | Evidence |
|---|---|---|
| At-risk VIP/Gold identification | Pass | Output contract + Foundry + Copilot Studio instructions |
| Plain-language explanation | Pass | Output contract + Copilot Studio + Agent Framework |
| Recommended human action | Pass | Output contract + Copilot Studio + Agent Framework |
| Portfolio summary (tier counts, at-risk counts, at-risk % by tier) | Pass | Output contract + Foundry + learner guide |

## T016 - At-Risk Rule Test Validation (0/1/2/3+)
Artifacts checked:
- `common/customer-lifecycle/risk-rules.md`
- `labs/customer-lifecycle/level-200/output-contract.md`
- `docs/customer-lifecycle/facilitator-guide.md`

| Scenario | Expected | Status | Notes |
|---|---|---|---|
| 0 negative signals | healthy | Pass | Explicit in risk rules + output contract |
| 1 negative signal | watch | Pass | Explicit in risk rules + facilitator mitigation prompts |
| 2 negative signals | at_risk | Pass | Explicit in risk rules + output contract |
| 3+ negative signals | at_risk | Pass | Explicit `3+` example included in risk rules |

## T017 - Final Documentation Parity Cleanup
Final reconciliation across:
- `README.md`
- `labs/customer-lifecycle/level-200/*.md`
- `labs/customer-lifecycle/level-300/extensions.md`
- `docs/customer-lifecycle/*.md`

Outcome:
- Pass. No remaining wording conflicts on:
  - 2+ signal rule
  - L200 baseline requirement
  - L300 optional boundary
  - Required Level 200 outputs
