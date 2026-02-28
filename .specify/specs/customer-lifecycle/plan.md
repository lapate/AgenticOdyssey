# Implementation Plan: VIP Customer Lifecycle Workshop Scenario

## Technical Scope
- Target areas (impacted paths):
  - `labs/customer-lifecycle/level-300/`
    - `foundry.md` (replace fixed 4-agent baseline language with architecture-agnostic 3-5 agent guidance, explicit handoffs, and guardrail-safe fallback paths),
    - `output-contract.md` (recast artifact contract from fixed agent names to required stage outcomes and evidence),
    - `copilot-studio.md` and `agent-framework.md` (confirm Level 300 outputs stay aligned after Foundry wording changes).
  - `labs/customer-lifecycle/level-400/extensions.md` (move optional topology variants and advanced orchestration experiments here only).
  - `common/customer-lifecycle/`
    - `risk-rules.md` (retain canonical 2+ signal gate and any threshold rules used as evidence),
    - `action-mapping.md` and `signal-dictionary.md` (standardize vocabulary for stage responsibilities, handoffs, validation statuses, and fallback terms).
  - `docs/customer-lifecycle/`
    - `learner-guide.md` (operational runbook for primary + fallback Foundry interaction patterns),
    - `facilitator-guide.md` (scoring rubric for FR-016..FR-020 success/failure checks under classroom guardrails).
  - `README.md` (entry-point summary must describe Foundry as 3-5 agent architecture-agnostic flow with concrete validation/fallback expectations).
  - `.specify/specs/customer-lifecycle/`
    - `plan.md`, `tasks.md`, `traceability.md`, `validation.md` (align implementation tracking and proof with revised FR-013..FR-020).
- Integration points:
  - Core source inputs remain `data/Zava Sales Data - FY2024-2026.xlsx` + `narrative.md`.
  - FR-014 exception remains synthetic learner-visible news input (`synthetic_regional_news_24m`, 24-month scope, regional events, fictional companies).
  - Foundry execution must produce source-derived outputs even when chat-based/table-wide prompts are blocked by tenant guardrails.

## Design Decisions
- Use a **stage-based contract** instead of fixed agent identities:
  1. Ingest/score stage,
  2. Risk classification stage (2+ negative signals),
  3. Explanation/action stage,
  4. Portfolio summary stage,
  5. Optional enrichment stage.
  Implementations may merge/split stages as long as total agents remain **3-5** and all Level 300 outcomes are produced.
- Define explicit handoff artifacts between stages (table/output schema + required fields) so learners can verify real-data progression independent of topology.
- Make validation evidence mandatory at two levels (FR-016):
  - one named-customer spot-check (source row lineage),
  - one aggregate portfolio check (tier counts, at-risk counts, at-risk % by tier).
- Standardize a concise failure-handling decision tree (FR-017, FR-020):
  - guardrail blocked -> run guardrail-safe fallback interaction pattern,
  - generic/placeholder output -> re-run with source-only constraints,
  - missing required fields -> mark `needs rework` and remediate targeted stage.
- Keep all changes additive and cross-documented (labs + docs + spec artifacts) to satisfy constitution principles for minimal disruption, verification, and documentation parity.

## Risks and Mitigations
- Risk: architecture-agnostic wording becomes too vague, leading to inconsistent learner implementations.
  - Mitigation: require a fixed stage-to-outcome checklist and explicit handoff evidence regardless of chosen 3-5 agent topology.
- Risk: teams drift below/above the 3-5 agent range while experimenting.
  - Mitigation: add a hard validation gate in Foundry instructions and facilitator rubric: submissions outside 3-5 are incomplete for Level 300.
- Risk: tenant guardrails block primary prompts and learners stall.
  - Mitigation: publish at least one pre-approved fallback pattern (artifact-first or scoped prompt sequence) that preserves identical Level 300 outcomes.
- Risk: outputs pass superficially but are generic/placeholder rather than source-derived.
  - Mitigation: require named-customer and aggregate evidence checks before marking completion; fail fast on placeholder indicators.
- Risk: optional enhancements leak into core flow and break timeboxes.
  - Mitigation: enforce L300/L400 boundary in all guides; route topology experiments and advanced agent roles to `level-400/extensions.md`.

## Validation Plan
- [ ] Verify `labs/customer-lifecycle/level-300/foundry.md` explicitly allows **3-5 agents** and does not mandate one orchestration topology (FR-013, FR-019).
- [ ] Verify Foundry guidance includes a learner-visible stage map with responsibilities, handoffs, and checkpoint evidence tied to Level 300 outcomes (FR-015, FR-018).
- [ ] Verify synthetic news requirements remain explicit: last 24 months, regional events, fictional company mentions, and learner-visible dataset usage (FR-014).
- [ ] Execute a named-customer spot-check path (for example `Contoso, Ltd.`): confirm identification, explanation, and recommended action fields are source-derived (FR-016, FR-018).
- [ ] Execute an aggregate artifact check: confirm tier counts, at-risk counts, and at-risk % by tier match produced workflow outputs (FR-005, FR-016, FR-018).
- [ ] Simulate each failure mode in documentation walkthrough: (a) guardrail-blocked prompt, (b) placeholder/generic output, (c) missing required fields; confirm remediation steps are concise and actionable (FR-017).
- [ ] Validate at least one documented guardrail-safe fallback interaction pattern reaches the same Level 300 outputs as the primary path (FR-020).
- [ ] Cross-check `README.md`, learner/facilitator guides, and `.specify/specs/customer-lifecycle/traceability.md` for terminology parity and L300-vs-L400 scope boundaries.

## Rollout Notes
- Implementation order: update Foundry lab + output contract first, then shared vocabulary/rules, then learner/facilitator guides, then README and spec traceability/validation artifacts.
- Keep learner instructions click-by-click and operational; avoid platform-internal architecture prescriptions that conflict with FR-019.
- Instructor communication note: acceptable submissions may vary in topology, but all must stay within 3-5 agents, pass guardrail-safe validation/fallback checks, and produce complete Level 300 outcomes from real data.
