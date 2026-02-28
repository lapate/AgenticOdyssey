# Tasks: customer-lifecycle

## Phase 1 - Foundation
- [x] T001 Update Foundry artifact definitions in `labs/customer-lifecycle/level-300/output-contract.md` to require exactly four FR-015 artifacts and explicit evidence fields for each.
- [x] T002 Update Foundry state model language in `common/customer-lifecycle/signal-dictionary.md` to allow only FR-016 statuses: `complete`, `incomplete`, and `needs rework`.
- [x] T003 Add/confirm Agent 3 threshold evidence requirements in `common/customer-lifecycle/risk-rules.md` and mirror vocabulary in `common/customer-lifecycle/action-mapping.md` for FR-015/FR-018 parity.
- [x] T004 Update `.specify/specs/customer-lifecycle/spec.md` clarifications/requirement text as needed so FR-015..FR-019 wording remains canonical and consistent with the updated implementation plan.

## Phase 2 - Feature Delivery
- [x] T005 Rewrite Foundry progress-checkpoint section in `labs/customer-lifecycle/level-300/foundry.md` to enumerate the exact four required artifacts and checklist criteria (FR-015).
- [x] T006 Rewrite Foundry status-assessment section in `labs/customer-lifecycle/level-300/foundry.md` to use only `complete`, `incomplete`, and `needs rework` with learner-facing definitions (FR-016).
- [x] T007 Implement the explicit learner iteration loop in `labs/customer-lifecycle/level-300/foundry.md`: check progress -> detect remaining work -> process remaining work -> iterate (FR-017).
- [x] T008 Implement the dual stop condition in `labs/customer-lifecycle/level-300/foundry.md` requiring both artifact completeness and Level 300 outcome coverage (identification, explanation, action, portfolio summary) (FR-018).
- [x] T009 Add explicit scope-boundary guardrails in `labs/customer-lifecycle/level-300/foundry.md` and `labs/customer-lifecycle/level-400/extensions.md` to preserve the existing four-agent baseline and prevent net-new mandatory agent categories (FR-019).
- [x] T010 Mirror FR-015..FR-019 learner execution guidance in `docs/customer-lifecycle/learner-guide.md`, including artifact checklist usage, state transitions, and iteration decisions.
- [x] T011 Mirror FR-015..FR-019 facilitator assessment rubric in `docs/customer-lifecycle/facilitator-guide.md`, including pass/fail checks for stop conditions and scope-boundary enforcement.
- [x] T012 Refresh workshop entry-point summary in `README.md` so the top-level Foundry flow reflects the updated iteration loop and stop-condition framing without introducing scope creep.

## Phase 3 - Validation and Cleanup
- [x] T013 Update `.specify/specs/customer-lifecycle/traceability.md` with explicit FR-015, FR-016, FR-017, FR-018, and FR-019 mappings to all updated implementation documents.
- [x] T014 Rewrite `.specify/specs/customer-lifecycle/validation.md` checklist items to validate: exact artifact set, exact status set, explicit iteration loop, dual stop condition, and scope-boundary preservation.
- [x] T015 Execute document-level validation and record evidence in `.specify/specs/customer-lifecycle/validation.md` by simulating at least one `needs rework` path and confirming loop continuation until all four artifacts are `complete`.
- [x] T016 Perform final cross-document terminology reconciliation across `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/output-contract.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md`, `README.md`, and `.specify/specs/customer-lifecycle/traceability.md`.

## Dependency Notes
- T002 depends on T001.
- T003 depends on T001 and T002.
- T004 depends on T001, T002, and T003.
- T005 depends on T001 and T004.
- T006 depends on T002 and T005.
- T007 depends on T005 and T006.
- T008 depends on T001 and T007.
- T009 depends on T003 and T008.
- T010 depends on T005, T006, T007, T008, and T009.
- T011 depends on T005, T006, T007, T008, T009, and T010.
- T012 depends on T007, T008, and T009.
- T013 depends on T010, T011, and T012.
- T014 depends on T005, T006, T007, T008, T009, T010, T011, and T013.
- T015 depends on T014.
- T016 depends on T013, T014, and T015.
