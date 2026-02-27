# Implementation Plan: VIP Customer Lifecycle Workshop Scenario

## Technical Scope
- Target areas (impacted paths):
  - `README.md` — overhaul as workshop Getting Started entry point with top-level flow and TOC.
  - `labs/customer-lifecycle/level-200/` — baseline learner flows and required outputs:
    - `copilot-studio.md` (full click-by-click navigate/click/type guidance),
    - `foundry.md`,
    - `agent-framework.md`,
    - `output-contract.md`.
  - `labs/customer-lifecycle/level-300/extensions.md` — optional advanced practice only, explicitly outside pass/fail.
  - `docs/customer-lifecycle/learner-guide.md` — reinforce numbered learner instructions and recovery guidance.
  - `docs/customer-lifecycle/facilitator-guide.md` — instructor rubric, timing, and L100/L200/L300 boundaries.
  - `common/customer-lifecycle/` — shared logic and language:
    - `signal-dictionary.md`,
    - `risk-rules.md` (2+ negative signals rule),
    - `action-mapping.md`.
  - `.specify/specs/customer-lifecycle/` — maintain spec/plan/task traceability.
- Integration points:
  - `data/Zava Sales Data - FY2024-2026.xlsx` and `narrative.md` as canonical inputs/context.
  - `.specify/memory/constitution.md` constraints: lab-first clarity, minimal disruption, verification required, documentation parity.

## Design Decisions
- Define levels using WWL-aligned boundaries in all learner-facing docs:
  - **L100** = foundational orientation (understand context, tour assets, no completion gate).
  - **L200** = required hands-on baseline for workshop completion/pass (must deliver required outputs).
  - **L300** = advanced hands-on practice that extends L100/L200, optional and excluded from pass/fail.
- Make Copilot Studio baseline fully procedural:
  - Use numbered steps with explicit **navigate to**, **click**, and **type** actions to remove ambiguity for first-time users.
- Treat Level 200 output contract as non-negotiable:
  - Required outputs remain at-risk VIP/Gold identification, plain-language explanation, recommended action, and portfolio summary (tier counts, at-risk counts, at-risk % by tier).
- Keep risk logic rule-based and transparent:
  - At-risk classification remains 2+ negative lifecycle signals to preserve explainability for business learners.

## Risks and Mitigations
- Risk: README overhaul obscures quick start for returning users.
  - Mitigation: keep a concise “fast path” section and stable links to existing lab docs at top-level.
- Risk: Copilot Studio instructions still leave hidden assumptions.
  - Mitigation: enforce a step format checklist (navigate/click/type) and include exact prompt text where typing is required.
- Risk: L100/L200/L300 confusion causes grading disputes.
  - Mitigation: duplicate level definitions and pass/fail boundary table in README + facilitator guide + learner guide.
- Risk: Optional L300 work bleeds into required baseline time.
  - Mitigation: sequence L300 sections after explicit “L200 complete” checkpoint and visually badge as optional.
- Risk: terminology or logic drifts across labs/docs.
  - Mitigation: source shared terms/rules from `common/customer-lifecycle/*` and run parity review before signoff.

## Validation Plan
- [ ] **README getting-started validation**: Confirm `README.md` includes TOC near top, end-to-end flow order (Copilot Studio → Foundry → Agent Framework), and clear first-step onboarding.
- [ ] **Copilot Studio click-path validation**: Execute `labs/customer-lifecycle/level-200/copilot-studio.md` linearly and verify each baseline step explicitly states navigate/click/type with no inferred actions.
- [ ] **L100/L200/L300 boundary validation**: Verify all three definitions match WWL framing verbatim and that only L200 criteria are tied to completion/pass.
- [ ] **Level 200 output validation**: Run baseline flow with workshop dataset and confirm four required outputs are present, including portfolio metrics (tier counts, at-risk counts, at-risk % by tier).
- [ ] **At-risk rule test cases**: Validate examples with 0, 1, 2, and 3+ negative signals; only 2+ may be labeled at-risk.
- [ ] **Timebox rehearsal**: Dry-run baseline sequence to confirm Copilot Studio ≤30 min, Foundry ≤60 min, Agent Framework ≤10 min.
- [ ] **Documentation parity check**: Verify behavior/wording changes in labs are reflected in `README.md`, learner guide, and facilitator guide.

## Rollout Notes
- Deliver in two passes: (1) required L200 + README/doc updates, (2) optional L300 refinements.
- Keep updates additive and backward-compatible with current lab assets.
- Communicate instructor enforcement rule: workshop completion is L200-only; L300 remains optional enrichment.
