# Implementation Plan: VIP Customer Lifecycle Workshop Scenario

## Technical Scope
- Target areas:
  - `labs/` — create/update workshop lab flow artifacts for the three phases (Copilot Studio, Foundry, Agent Framework) with a Level 200 baseline and clearly separated optional Level 300 extensions.
  - `common/` — add shared definitions for lifecycle signals, at-risk rule logic (2+ negative signals), and recommendation mapping so terminology and logic remain consistent across phases.
  - `docs/` — update facilitator/learner-facing guidance to reflect scenario goals, timeboxes, expected outputs, and how to interpret portfolio-level metrics.
  - `data/` — reference the provided Zava dataset as the only scenario input source and document learner-visible derived fields used for scoring/explanations.
  - `.specify/specs/customer-lifecycle/` — keep spec-to-plan traceability and ensure implementation artifacts map back to FR/NFR and acceptance criteria.
- Integration points:
  - `narrative.md` for business context alignment and consistent storyline language.
  - `data/Zava Sales Data - FY2024-2026.xlsx` as source data for all baseline outputs.
  - Constitution constraints in `.specify/memory/constitution.md` (lab-first clarity, minimal disruption, documentation parity, explicit validation).

## Design Decisions
- Use a rule-based baseline classifier instead of predictive modeling:
  - Rationale: FR-002 explicitly defines at-risk as two or more negative lifecycle signals, and workshop constraints prioritize clarity for non-technical learners (NFR-001) over model complexity.
- Standardize a shared “signal dictionary” across all phases:
  - Rationale: A single definition set for recency, frequency, spend, margin, and mix supports NFR-004 terminology consistency and prevents phase drift.
- Enforce a strict Level 200/Level 300 boundary in content structure:
  - Rationale: FR-008 requires Level 300 to be optional-only and not impact Level 200 pass/fail; implementation will physically separate baseline vs extension tasks/prompts.
- Implement portfolio summary as a mandatory output contract:
  - Rationale: Clarifications require tier counts, at-risk counts, and at-risk percentage by tier; defining this as a contract ensures comparable learner outcomes and easier facilitator review.
- Keep changes additive to existing workshop assets:
  - Rationale: Aligns with constitution “minimal disruption” and reduces risk to existing runnable workshop flow.

## Risks and Mitigations
- Risk: Learners misclassify customers by applying only one negative signal.
  - Mitigation: Add explicit gating checks and examples that require confirmation of at least two negative signals before any at-risk label is shown.
- Risk: Inconsistent wording across phases confuses business audiences.
  - Mitigation: Reuse shared glossary text from `common/` and perform cross-phase terminology review before finalizing labs/docs.
- Risk: Scope creep from optional enhancements consumes core class time.
  - Mitigation: Timebox Level 200 deliverables first; mark Level 300 tasks as optional and sequenced after baseline completion checkpoints.
- Risk: Data transformation steps become opaque to non-technical learners.
  - Mitigation: Document each derived field in plain language alongside source columns and business interpretation, keeping transformations learner-visible.
- Risk: Documentation and lab behavior diverge after updates.
  - Mitigation: Include documentation parity checks in validation to verify every behavior/output change in labs is reflected in docs.

## Validation Plan
- [ ] **Spec-to-plan traceability check**: Verify each FR-001..FR-008 and NFR-001..NFR-005 is mapped to at least one planned implementation artifact in `labs/`, `common/`, or `docs/`.
- [ ] **Baseline output verification (Level 200)**: Run through the scenario with the provided dataset and confirm outputs include:
  - at-risk VIP/Gold identification,
  - plain-language explanation for each at-risk customer,
  - recommended human action per at-risk customer,
  - portfolio summary with tier counts, at-risk counts, and at-risk percentage by tier.
- [ ] **At-risk rule verification**: Validate sample customers where 0, 1, 2, and 3+ negative signals are present to confirm only 2+ are classified at-risk.
- [ ] **Phase timebox rehearsal**: Dry-run workshop flow to confirm Copilot Studio ≤30 min, Foundry ≤60 min, Agent Framework ≤10 min for baseline completion.
- [ ] **Terminology consistency review**: Check that “customer health,” “risk signals,” “tiers,” and “actions” are used consistently across lab instructions and documentation.
- [ ] **Optional extension isolation check**: Confirm Level 300 enhancements are clearly labeled optional and no Level 200 pass/fail rubric depends on Level 300 outputs.
- [ ] **Documentation parity check**: Confirm updated docs describe any changed/added lab behavior, expected learner outputs, and facilitator interpretation guidance.

## Rollout Notes
- Roll out in two increments: (1) Level 200 baseline assets and docs, then (2) optional Level 300 enhancement assets.
- Preserve backward compatibility for existing workshop delivery by introducing new lifecycle content as additive modules rather than replacing prior materials.
- Communicate to instructors that baseline completion criteria are fixed to the clarified outputs and 2+ signal rule, with optional extensions positioned for advanced cohorts only.
