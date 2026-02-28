# Tasks: customer-lifecycle

## Phase 1 - Foundation
- [x] T001 Update canonical requirement wording in `.specify/specs/customer-lifecycle/spec.md` so FR-013..FR-020 consistently enforce architecture-agnostic outcomes, a strict 3-5 agent solution band, and guardrail-safe fallback expectations.
- [x] T002 Recast `labs/customer-lifecycle/level-300/output-contract.md` to a stage-based contract (not fixed agent names) with required handoff fields, source-lineage evidence fields, and Level 300 outcome coverage markers.
- [x] T003 Standardize shared terminology in `common/customer-lifecycle/signal-dictionary.md`, `common/customer-lifecycle/action-mapping.md`, and `common/customer-lifecycle/risk-rules.md` for stage responsibilities, validation states, 2+ signal risk gating, and fallback/remediation terms.
- [x] T004 Enforce Level 300/Level 400 scope boundaries in `labs/customer-lifecycle/level-400/extensions.md` so topology variants and advanced orchestration experiments are explicitly optional-only and isolated from baseline requirements.

## Phase 2 - Feature Delivery
- [x] T005 Rewrite `labs/customer-lifecycle/level-300/foundry.md` to define an architecture-agnostic 3-5 agent flow with explicit stage responsibilities, handoff artifacts, and learner-visible checkpoints mapped to Level 300 outcomes.
- [x] T006 Add guardrail-safe failure handling to `labs/customer-lifecycle/level-300/foundry.md` as a concise decision path for blocked prompts, generic/placeholder outputs, and missing required fields, including targeted rework instructions.
- [x] T007 Update `labs/customer-lifecycle/level-300/foundry.md` and `labs/customer-lifecycle/level-300/output-contract.md` to preserve FR-014 synthetic news constraints (24-month scope, regional events, fictional company references) as learner-visible evidence requirements.
- [x] T008 Align `labs/customer-lifecycle/level-300/copilot-studio.md` and `labs/customer-lifecycle/level-300/agent-framework.md` with the revised Foundry outcome contract so adjacent phases stay consistent without introducing fixed topology assumptions.
- [x] T009 Update `docs/customer-lifecycle/learner-guide.md` with operational primary and fallback Foundry runbooks, including named-customer spot-check and aggregate artifact validation steps.
- [x] T010 Update `docs/customer-lifecycle/facilitator-guide.md` with scoring rubric gates for FR-016..FR-020, including 3-5 agent compliance, source-derived evidence checks, and failure-mode remediation scoring.
- [x] T011 Refresh `README.md` so the workshop entry flow describes Foundry as architecture-agnostic within the 3-5 agent band and calls out required validation/fallback expectations.

## Phase 3 - Validation and Cleanup
- [x] T012 Update `.specify/specs/customer-lifecycle/traceability.md` with FR-013..FR-020 mappings that reference the revised stage-based contract, guardrail-safe fallback guidance, and Level 300/Level 400 boundary enforcement.
- [x] T013 Rewrite `.specify/specs/customer-lifecycle/validation.md` checklist criteria to verify architecture-agnostic 3-5 compliance, stage handoff evidence, source-derived spot-check + aggregate checks, and fallback-path parity with primary outcomes.
- [x] T014 Execute and document validation walkthroughs in `.specify/specs/customer-lifecycle/validation.md` covering: one named-customer check, one aggregate portfolio check, and three failure scenarios (guardrail blocked, placeholder output, missing fields) with remediation outcomes.
- [x] T015 Run final cross-document parity pass across `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/output-contract.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md`, `README.md`, `.specify/specs/customer-lifecycle/traceability.md`, and `.specify/specs/customer-lifecycle/validation.md` to remove terminology drift and confirm consistent acceptance gates.

## Dependency Notes
- T002 depends on T001.
- T003 depends on T001.
- T004 depends on T001.
- T005 depends on T001, T002, and T003.
- T006 depends on T005.
- T007 depends on T002 and T005.
- T008 depends on T005.
- T009 depends on T005, T006, and T007.
- T010 depends on T005, T006, and T007.
- T011 depends on T005, T009, and T010.
- T012 depends on T005, T006, T007, T008, T009, T010, and T011.
- T013 depends on T012.
- T014 depends on T013.
- T015 depends on T012, T013, and T014.
