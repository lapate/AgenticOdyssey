# Tasks: customer-lifecycle

## Phase 1 - Foundation
- [x] T001 Document the canonical VIP recency threshold value and the explicit Agent 3 rule (`tier='VIP' AND recency > <threshold>`) in `common/customer-lifecycle/risk-rules.md`.
- [x] T002 Align shared terminology in `common/customer-lifecycle/signal-dictionary.md` with the Foundry 4-agent flow (Agent 1 RFM, Agent 2 tier+health, Agent 3 thresholded VIP alert, Agent 4 news-based action evaluation).
- [x] T003 Update `labs/customer-lifecycle/level-300/output-contract.md` to require handoff outputs for each Foundry agent, including the recency-threshold evidence field used by Agent 3.
- [x] T004 Define synthetic news dataset scope and exception criteria in `common/customer-lifecycle/action-mapping.md` and `common/customer-lifecycle/signal-dictionary.md` (dataset name `synthetic_regional_news_24m`, last-24-month window, regional events, fictional-company references, invalid/out-of-window row handling).

## Phase 2 - Feature Delivery
- [x] T005 Revise `labs/customer-lifecycle/level-300/foundry.md` with explicit New Foundry navigation assumptions (New Foundry enabled) and the no Project API key authentication path.
- [x] T006 Implement end-to-end Foundry Build -> Data workflow steps in `labs/customer-lifecycle/level-300/foundry.md`, including loading canonical workbook inputs plus synthetic news input with exception handling branches.
- [x] T007 Implement Foundry Build -> Workflows steps in `labs/customer-lifecycle/level-300/foundry.md` for the full 4-agent chain and explicit inter-agent handoff mapping.
- [x] T008 Add explicit Agent 4 synthetic-news processing instructions in `labs/customer-lifecycle/level-300/foundry.md` for scope enforcement (24 months only) and exception paths (missing region, non-fictional company, malformed date, stale record).
- [x] T009 Mirror New Foundry navigation/auth assumptions and Build -> Data / Build -> Workflows expectations in `docs/customer-lifecycle/learner-guide.md`.
- [x] T010 Mirror the same Foundry assumptions, checkpoints, and assessment rubric in `docs/customer-lifecycle/facilitator-guide.md`, including enforcement of the documented recency threshold and 4-agent completion evidence.

## Phase 3 - Validation and Cleanup
- [x] T011 Add validation checklist items to `.specify/specs/customer-lifecycle/validation.md` for New Foundry toggle, no Project API key path, and presence of Build -> Data plus Build -> Workflows steps in `labs/customer-lifecycle/level-300/foundry.md`.
- [x] T012 Execute and record validation in `.specify/specs/customer-lifecycle/validation.md` that all four Foundry agents are documented with correct sequencing and that Agent 3 uses the same recency threshold text as `common/customer-lifecycle/risk-rules.md`.
- [x] T013 Execute and record synthetic-news validation in `.specify/specs/customer-lifecycle/validation.md` against `labs/customer-lifecycle/level-300/foundry.md` and `common/customer-lifecycle/*` for dataset scope and exception handling coverage.
- [x] T014 Reconcile cross-doc consistency in `README.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md`, and `.specify/specs/customer-lifecycle/traceability.md` so Foundry navigation assumptions and workflow checks are traceable end-to-end.

## Backlog (Placeholder Only)
- [ ] B001 Revisit how workshop markdown definitions are consumed in lab flows (for example lifecycle definitions and output checklist) so future definition shifts can be handled with less manual rewrite.

## Dependency Notes
- T002 depends on T001.
- T003 depends on T001 and T002.
- T004 depends on T002.
- T005 depends on T001.
- T006 depends on T004 and T005.
- T007 depends on T003 and T005.
- T008 depends on T004, T006, and T007.
- T009 depends on T005, T006, and T007.
- T010 depends on T005, T007, and T009.
- T011 depends on T006 and T007.
- T012 depends on T001, T007, and T011.
- T013 depends on T004, T008, and T011.
- T014 depends on T009, T010, T012, and T013.
