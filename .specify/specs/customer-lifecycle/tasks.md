# Tasks: VIP Customer Lifecycle Workshop Scenario

## Phase 1 - Foundation
- [x] T001 Create baseline folder structure for lifecycle assets in `labs/customer-lifecycle/`, `common/customer-lifecycle/`, `docs/customer-lifecycle/`, and `data/customer-lifecycle/`.
- [x] T002 Author shared signal dictionary in `common/customer-lifecycle/signal-dictionary.md` defining recency, frequency, spend, margin, mix, and standard terms (`customer health`, `risk signals`, `tiers`, `actions`).
- [x] T003 Define the at-risk rule contract in `common/customer-lifecycle/risk-rules.md`, including explicit 2+ negative-signal gating and example cases for 0/1/2/3+ signals.
- [x] T004 Create action mapping matrix in `common/customer-lifecycle/action-mapping.md` linking risk patterns to recommended human actions (retention outreach, follow-up, pricing/margin review, targeted offers).
- [x] T005 Document learner-visible derived fields sourced from `data/Zava Sales Data - FY2024-2026.xlsx` in `data/customer-lifecycle/derived-fields.md` (source columns, transformation, business interpretation).

## Phase 2 - Feature Delivery
- [x] T006 Build Level 200 Copilot Studio lab instructions in `labs/customer-lifecycle/level-200/copilot-studio.md` for at-risk VIP/Gold identification and plain-language explanation within a 30-minute flow.
- [x] T007 Build Level 200 Foundry lab instructions in `labs/customer-lifecycle/level-200/foundry.md` for structured scoring preparation, 2+ signal classification, and portfolio summary outputs within a 60-minute flow.
- [x] T008 Build Level 200 Agent Framework lab instructions in `labs/customer-lifecycle/level-200/agent-framework.md` for proactive alert demonstration and action recommendation within a 10-minute flow.
- [x] T009 Add mandatory output contract to `labs/customer-lifecycle/level-200/output-contract.md` covering tier counts, at-risk counts, at-risk percentage by tier, at-risk explanations, and mapped actions.
- [x] T010 Add optional Level 300 extension pack in `labs/customer-lifecycle/level-300/extensions.md`, explicitly labeled optional and isolated from Level 200 pass/fail criteria.
- [x] T011 Update facilitator guidance in `docs/customer-lifecycle/facilitator-guide.md` with storyline alignment, timebox checkpoints, risk-misclassification mitigation prompts, and portfolio metric interpretation guidance.
- [x] T012 Update learner guidance in `docs/customer-lifecycle/learner-guide.md` with phase outcomes, expected artifacts, glossary terms, and baseline-vs-optional boundaries.

## Phase 3 - Validation and Cleanup
- [x] T013 Create FR/NFR traceability matrix in `.specify/specs/customer-lifecycle/traceability.md` mapping FR-001..FR-008 and NFR-001..NFR-005 to concrete files in `labs/`, `common/`, `docs/`, and `data/`.
- [x] T014 Add validation checklist in `.specify/specs/customer-lifecycle/validation.md` to verify baseline outputs, 2+ signal rule behavior, terminology consistency, optional extension isolation, and documentation parity.
- [x] T015 Execute a dry-run review using `labs/customer-lifecycle/level-200/*.md` and `docs/customer-lifecycle/*.md`, then record pass/fail outcomes and required follow-ups in `.specify/specs/customer-lifecycle/validation.md`.
- [x] T016 Perform final documentation parity cleanup by reconciling lab behavior vs guides and updating `docs/customer-lifecycle/facilitator-guide.md` and `docs/customer-lifecycle/learner-guide.md` where mismatches are found.

## Dependency Notes
- T002 depends on T001.
- T003 depends on T002.
- T004 depends on T002 and T003.
- T005 depends on T001.
- T006 depends on T002, T003, and T005.
- T007 depends on T002, T003, T005, and T006.
- T008 depends on T002, T003, T004, and T007.
- T009 depends on T003, T004, T006, T007, and T008.
- T010 depends on T006, T007, T008, and T009.
- T011 depends on T006, T007, T008, and T009.
- T012 depends on T006, T007, T008, and T009.
- T013 depends on T002 through T012.
- T014 depends on T003, T009, T011, T012, and T013.
- T015 depends on T014.
- T016 depends on T015.
