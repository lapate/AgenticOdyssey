# Tasks: customer-lifecycle

## Phase 1 - Foundation
- [x] T001 Align and lock canonical L100/L200/L300 definitions in `common/customer-lifecycle/signal-dictionary.md` and reference completion/pass boundaries (L200 required, L300 optional).
- [x] T002 Update `common/customer-lifecycle/risk-rules.md` with explicit 2+ negative-signal at-risk rule examples for 0/1/2/3+ signals.
- [x] T003 Sync required L200 output contract language in `labs/customer-lifecycle/level-200/output-contract.md` (VIP/Gold at-risk identification, plain-language explanation, recommended action, portfolio summary with tier counts + at-risk counts + at-risk % by tier).

## Phase 2 - Feature Delivery
- [x] T004 Convert `README.md` into a Getting Started entry point with near-top TOC, top-level workshop flow (Copilot Studio → Foundry → Agent Framework), first-step onboarding, and returning-user fast path.
- [x] T005 Add explicit L100/L200/L300 definitions and a pass/fail boundary section to `README.md`, matching wording from `common/customer-lifecycle/*`.
- [x] T006 Rewrite `labs/customer-lifecycle/level-200/copilot-studio.md` as strict numbered click-by-click learner instructions where each step includes navigate/click/type actions and exact text to enter where applicable.
- [x] T007 Update `labs/customer-lifecycle/level-200/foundry.md` to the same numbered navigate/click/type format, aligned to required L200 outputs.
- [x] T008 Update `labs/customer-lifecycle/level-200/agent-framework.md` to the same numbered navigate/click/type format, aligned to required L200 outputs and L200-only completion gating.
- [x] T009 Update `docs/customer-lifecycle/learner-guide.md` to include explicit L100/L200/L300 definitions, L200 completion criteria, and links to the updated L200 lab sequence.
- [x] T010 Update `docs/customer-lifecycle/facilitator-guide.md` with matching L100/L200/L300 definitions, L200-only grading enforcement, and timing rubric (Copilot Studio ≤30m, Foundry ≤60m, Agent Framework ≤10m).
- [x] T011 Update `labs/customer-lifecycle/level-300/extensions.md` to clearly label all content as optional L300 enrichment and outside workshop pass/fail.

## Phase 3 - Validation and Cleanup
- [x] T012 Update `.specify/specs/customer-lifecycle/validation.md` with checks for README TOC/top-level flow/first step/fast path, plus link integrity to L200 labs.
- [x] T013 Add and execute a step-completeness validation pass for `labs/customer-lifecycle/level-200/copilot-studio.md`, verifying every learner action is explicit (navigate/click/type) and recording findings in `.specify/specs/customer-lifecycle/validation.md`.
- [x] T014 Add and execute parity validation for L100/L200/L300 definitions across `README.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md`, `labs/customer-lifecycle/level-200/*.md`, and `labs/customer-lifecycle/level-300/extensions.md`; record pass/fail in `.specify/specs/customer-lifecycle/validation.md`.
- [x] T015 Add and execute L200 output validation against `labs/customer-lifecycle/level-200/output-contract.md` and the learner/facilitator docs, confirming all required outputs are consistently defined and assessed; record results in `.specify/specs/customer-lifecycle/validation.md`.
- [x] T016 Add and execute at-risk rule test validation (0/1/2/3+ signals) across `common/customer-lifecycle/risk-rules.md`, `labs/customer-lifecycle/level-200/output-contract.md`, and `docs/customer-lifecycle/facilitator-guide.md`; record results and remediation items in `.specify/specs/customer-lifecycle/validation.md`.
- [x] T017 Run final documentation parity cleanup across `README.md`, `labs/customer-lifecycle/level-200/*.md`, `labs/customer-lifecycle/level-300/extensions.md`, and `docs/customer-lifecycle/*.md`, then reconcile any mismatches discovered in T012-T016.

## Dependency Notes
- T002 depends on T001.
- T003 depends on T001 and T002.
- T004 depends on T001.
- T005 depends on T001 and T004.
- T006 depends on T001 and T003.
- T007 depends on T001, T003, and T006.
- T008 depends on T001, T003, and T006.
- T009 depends on T001, T003, T006, T007, and T008.
- T010 depends on T001, T003, T005, and T009.
- T011 depends on T001 and T010.
- T012 depends on T004 through T011.
- T013 depends on T006 and T012.
- T014 depends on T005, T009, T010, T011, and T012.
- T015 depends on T003, T007, T008, T009, T010, and T012.
- T016 depends on T002, T003, T010, and T012.
- T017 depends on T013, T014, T015, and T016.
