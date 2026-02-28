# Implementation Plan: VIP Customer Lifecycle Workshop Scenario

## Technical Scope
- Target areas (impacted paths):
  - `README.md` (entry-point flow and workshop phase ordering).
  - `labs/customer-lifecycle/level-300/`
    - `foundry.md` (FR-015..FR-019 artifact checkpoints, state model, and iteration loop decisions),
    - `output-contract.md` (required Foundry artifact evidence + Level 300 outcome mapping),
    - `copilot-studio.md` and `agent-framework.md` (baseline alignment and no scope creep from Foundry clarifications).
  - `labs/customer-lifecycle/level-400/extensions.md` (protect optional-only scope boundary).
  - `common/customer-lifecycle/`
    - `risk-rules.md` (VIP recency threshold reference used by artifact #3),
    - `signal-dictionary.md` and `action-mapping.md` (state/artifact vocabulary parity).
  - `docs/customer-lifecycle/`
    - `learner-guide.md` (iteration checklist wording learners execute),
    - `facilitator-guide.md` (assessment rubric for complete/incomplete/needs rework states).
  - `.specify/specs/customer-lifecycle/`
    - `spec.md`, `plan.md`, `tasks.md`, `validation.md`, `traceability.md` (requirements-to-plan traceability and proof).
- Integration points:
  - Canonical internal sources remain `data/Zava Sales Data - FY2024-2026.xlsx` + `narrative.md`.
  - FR-014 exception remains `synthetic_regional_news_24m` (Agent 4 only, 24-month constraint).
  - Foundry iteration integration must preserve existing four-agent chain and avoid net-new mandatory agent categories (FR-019).

## Design Decisions
- Keep the plan implementation-focused on **FR-015 through FR-019** by codifying:
  1. Exactly four required artifacts,
  2. Exactly three allowed progress states (`complete`, `incomplete`, `needs rework`),
  3. One learner-visible loop: progress check -> work detection -> process decision -> repeat.
- Treat Foundry iteration as a **quality/completion overlay** on the existing workflow, not a new architecture. This preserves constitution principles of minimal disruption and lab-first clarity.
- Enforce a two-part stop condition in learner language:
  - all four required artifacts are `complete`, and
  - outputs cover all Level 300 outcomes (identification, explanation, action, portfolio summary).
- Keep Agent 3 threshold evidence explicit and traceable to `common/customer-lifecycle/risk-rules.md` so learners can prove why a VIP alert was triggered.
- Keep all scope changes additive and documentation-symmetric (labs + learner guide + facilitator guide + spec artifacts) to satisfy documentation parity.

## Risks and Mitigations
- Risk: iteration guidance drifts into ambiguous “keep improving” language and breaks FR-016 state consistency.
  - Mitigation: standardize one status table reused across `foundry.md`, learner guide, facilitator guide, and validation artifacts.
- Risk: teams mark artifacts complete without proving checklist criteria.
  - Mitigation: require artifact evidence fields in `output-contract.md` and facilitator rubric checks before status can be marked `complete`.
- Risk: FR-019 scope control is violated by adding mandatory extra agent steps while clarifying iteration.
  - Mitigation: explicitly prohibit new mandatory agent categories in Foundry baseline docs and route enhancements to Level 400.
- Risk: loop termination is applied before Level 300 outcomes are covered.
  - Mitigation: add stop-condition verification step that cross-checks artifact completion against the four required outcomes.

## Validation Plan
- [ ] Confirm `labs/customer-lifecycle/level-300/foundry.md` names exactly four required artifacts and matches FR-015 wording.
- [ ] Confirm artifact states appear exactly as `complete`, `incomplete`, and `needs rework` with definitions matching FR-016.
- [ ] Walk through the published learner loop and verify it explicitly states: check progress -> determine remaining work -> process remaining work -> continue iteration (FR-017).
- [ ] Verify stop-condition text in Foundry guidance requires both artifact completeness and Level 300 outcome coverage (FR-018).
- [ ] Validate `output-contract.md` and facilitator rubric require threshold evidence for Agent 3 (VIP + recency threshold) and evidence for Agent 4 news-based evaluation.
- [ ] Execute a dry run with one intentionally failing artifact to ensure status is set to `needs rework`, remediation path is followed, and loop continues until all artifacts are `complete`.
- [ ] Cross-check `README.md`, learner/facilitator docs, and `.specify/specs/customer-lifecycle/traceability.md` for consistent Foundry iteration terminology and Level 300 vs Level 400 boundaries.

## Rollout Notes
- Apply updates in this order: Foundry lab + output contract -> shared common rules -> learner/facilitator docs -> README and traceability/validation artifacts.
- Keep language workshop-operational (what learners do next) rather than platform-internal implementation detail.
- Communicate one instructor-facing rule: iteration clarifications improve completion quality for the existing four-agent Level 300 baseline and do not introduce new mandatory baseline scope.
