# Feature Specification: VIP Customer Lifecycle Workshop Scenario

## Summary
Define a workshop-ready, specification-driven learning scenario that helps learners identify and respond to early lifecycle risk in VIP and Gold customers using the provided Zava sales narrative and dataset. This feature matters because the workshop’s core value is teaching practical AI-assisted business decision support—showing who is at risk, why risk is emerging, and what humans should do next—within strict classroom timeboxes and mixed learner skill levels. The scenario must also support Foundry iteration loops so learners can check progress, decide whether additional work is required, process remaining work, and continue until baseline outputs are complete.

## Clarifications
- 2026-02-27: A customer is classified as at-risk only when **two or more** negative lifecycle signals are present.
- 2026-02-27: Portfolio-level minimum outputs must include **tier counts**, **at-risk counts**, and **at-risk percentage by tier**.
- 2026-02-27: The Level 300 baseline must include **at-risk VIP/Gold identification**, a **plain-language explanation**, a **recommended action**, and a **portfolio summary**.
- 2026-02-27: Level 400 scope is **optional complexity enhancements only** and must **not** affect Level 300 pass/fail.
- 2026-02-28: Foundry baseline flow must explicitly include an iteration cycle of **check progress -> detect remaining work -> process remaining work -> iterate** until required outputs satisfy the Level 300 checklist.
- 2026-02-28: Required Foundry artifacts for iteration completion are exactly four: **RFM output**, **tier/health output**, **VIP recency alert output with documented threshold evidence**, and **news-based short-term action evaluation output**.
- 2026-02-28: Foundry progress states are defined as **complete** (artifact exists and passes checklist criteria), **incomplete** (artifact missing or not yet run), and **needs rework** (artifact exists but fails one or more checklist criteria).
- 2026-02-28: Foundry iteration stops only when **all four required artifacts are complete** and outputs map to Level 300 outcomes: **identification, explanation, action, and portfolio summary**.
- 2026-02-28: Foundry iteration guidance must preserve the existing four-agent Level 300 baseline and must not introduce net-new mandatory agent categories.

## User Stories
### Story 1 - Surface At-Risk High-Value Customers
As a sales operations learner, I want to identify VIP and Gold customers with declining engagement signals, so that I can prioritize retention-focused attention before churn occurs.

### Story 2 - Explain Risk in Business Terms
As a business stakeholder learner, I want clear explanations for customer health changes (recency, frequency, spend, margin, and mix), so that I can understand risk drivers without needing deep technical analysis.

### Story 3 - Recommend Practical Next Steps
As an account management learner, I want actionable recommendations tied to customer risk signals, so that I can move from insight to timely outreach and intervention.

### Story 4 - Learn Through Progressive Demo Phases
As a workshop participant, I want the scenario structured across Copilot Studio, Foundry, and Agent Framework phases, so that I can build confidence incrementally, explicitly build/configure the agent experience, and complete core outcomes in class.

### Story 5 - Start Quickly from the Repository Entry Point
As a first-time workshop learner, I want README.md to function primarily as a Getting Started guide with a clear table of contents and top-level demo flow, so that I can understand where to begin and how the parts fit together.

### Story 6 - Follow Click-by-Click Demo Instructions
As a learner with varied tool familiarity, I want explicit step-by-step guidance (where to navigate, what to click, and what to type), especially for the Copilot Studio flow, so that I can complete the exercises without guesswork.

### Story 7 - Understand Learning Levels and Expectations
As an instructor or learner, I want clear definitions of L100, L200, L300, and L400 (including what is required vs optional), so that workshop expectations and pass/fail boundaries are unambiguous.

### Story 8 - Build a Multi-Agent Foundry Workflow
As a technical learner supporting a business SME scenario, I want Foundry to demonstrate a clear four-agent workflow (RFM, tier/health, VIP recency alert, and news-based action evaluation), so that I can connect data engineering steps to business-facing decisions.

### Story 9 - Iterate Foundry Work Until Baseline Is Complete
As a workshop learner, I want explicit checkpoints that tell me whether work remains in the Foundry flow and what to do next, so that I can confidently continue iterating without leaving required Level 300 outputs incomplete.

## Functional Requirements
- [FR-001] The feature must define a lifecycle-monitoring scenario focused on VIP and Gold customer risk in Zava’s sales context.
- [FR-002] The feature must require identification of at-risk behavior using lifecycle signals (such as slowing order frequency, increased time since purchase, and declining spend), and must classify a customer as at-risk only when two or more negative signals are present.
- [FR-003] The feature must require explanation outputs that describe why a customer is considered at risk using understandable business language.
- [FR-004] The feature must require recommended human actions (e.g., retention outreach, account follow-up, pricing/margin review, targeted offers) linked to identified risk.
- [FR-005] The feature must require portfolio-level visibility with, at minimum, tier counts, at-risk counts, and at-risk percentage by tier.
- [FR-006] The feature must define three progressive workshop phases aligned to repository learning flow: (1) build/configure the Copilot Studio conversational experience and run insight prompts, (2) prepare structured scoring outputs in Foundry, and (3) build/configure the Agent Framework alert workflow and run proactive alert demonstrations.
- [FR-007] The feature must require that all core scenario inputs originate from the provided workshop dataset and narrative (with the explicit exception of the synthetic news input defined in FR-014), and that derived fields are explicitly called out as learner-visible transformations.
- [FR-008] The feature must support a Level 300 baseline experience that includes at-risk VIP/Gold identification, plain-language explanation, recommended action, and portfolio summary, with clearly marked Level 400 extensions that are optional and do not affect Level 300 pass/fail.
- [FR-009] The feature must require README.md to function as the workshop entry point by including: (a) a table of contents near the top of the file, and (b) a top-level end-to-end demo flow that lists Copilot Studio, Foundry, and Agent Framework in learning order.
- [FR-010] The feature must require numbered, step-by-step learner instructions for baseline activities that state where to navigate, what to click, and what text to enter; Copilot Studio baseline steps must be fully documented in this format.
- [FR-011] The feature must define learning levels with explicit scope boundaries: L100 = foundational orientation, L200 = intermediate hands-on learning, L300 = advanced hands-on baseline for workshop completion (building on L100 and L200, aligned with Microsoft WWL framing), and L400 = optional complexity extensions that do not affect Level 300 pass/fail.
- [FR-012] If classroom time requires scope cuts, non-essential enhancements must be moved to explicit Level 400 after-class extensions; required Level 300 build/configuration steps must remain in-class and must not be removed.
- [FR-013] The Foundry phase must demonstrate a four-agent workflow with explicit agent responsibilities: (1) compute RFM, (2) compute tiers and simple health indicators, (3) apply a simple rule `VIP + recency above a documented threshold -> alert` (with that threshold explicitly stated in learner-facing guidance), and (4) run news-based short-term action evaluation that augments internal lifecycle signals.
- [FR-014] The news-based evaluation input must be a synthetic, learner-visible dataset covering the most recent 24 months and include regional events (for example natural disasters and major public events) plus fictional company references (for example Contoso) so students can correlate behavior changes to events.
- [FR-015] The Foundry phase must define learner-visible progress checkpoints for exactly four required artifacts: (1) RFM output, (2) tier/health output, (3) VIP recency alert output with documented threshold evidence, and (4) news-based short-term action evaluation output.
- [FR-016] The Foundry phase must use only these progress states for each required artifact: **complete** (artifact exists and passes checklist criteria), **incomplete** (artifact missing or not yet run), and **needs rework** (artifact exists but fails one or more checklist criteria).
- [FR-017] The feature must define an explicit Foundry iteration decision flow in learner terms: check progress, determine whether work remains, decide to process remaining work when present, and repeat until all four required artifacts are marked complete.
- [FR-018] The Foundry iteration stop condition must require both: (a) all four required artifacts are marked complete, and (b) the resulting outputs map to all Level 300 Foundry outcomes (identification, explanation, action, portfolio summary).
- [FR-019] Foundry iteration requirements must preserve current scope boundaries by improving completion and quality of the existing four-agent scenario, without introducing new mandatory agent types or expanding baseline platform scope.

## Non-Functional Requirements
- [NFR-001] The scenario must be understandable by non-technical learners and business leaders, prioritizing clarity over algorithmic complexity.
- [NFR-002] The scenario must fit workshop delivery constraints: Copilot Studio within 30 minutes, Foundry within 60 minutes, and Agent Framework within 10 minutes.
- [NFR-003] The scenario must be modular and extensible so instructors can add advanced exercises without changing baseline outcomes.
- [NFR-004] The scenario must maintain consistent terminology across phases (customer health, risk signals, tiers, actions) to reduce learner confusion.
- [NFR-005] The scenario must preserve learner safety and confidence by keeping core flows low-friction and avoiding heavy prerequisite setup during class time.
- [NFR-006] Learner-facing documentation must be scannable and orientation-friendly, with predictable sectioning and navigation so participants can recover quickly if they fall behind.
- [NFR-007] Foundry iteration guidance must minimize learner ambiguity by using clear completion states and next-step decisions that can be followed quickly under workshop time pressure.

## Acceptance Criteria
- [ ] A learner can describe the business problem as “detect early lifecycle decline in high-value customers and act sooner.”
- [ ] The specification includes at least three user-visible risk signals and explains why each matters to retention outcomes.
- [ ] The specification defines at-risk classification as requiring two or more negative signals.
- [ ] The specification includes recommended actions mapped to identified risk conditions, not just descriptive analytics.
- [ ] The specification defines portfolio minimum outputs as tier counts, at-risk counts, and at-risk percentage by tier.
- [ ] The specification defines all three workshop phases and aligns them to expected learner outcomes and timeboxes.
- [ ] The specification explicitly defines Level 300 baseline outputs (at-risk VIP/Gold identification, plain-language explanation, recommended action, portfolio summary) and marks Level 400 as optional-only.
- [ ] The specification references workshop-relevant source inputs (narrative + Zava sales Excel) and clarifies that derived fields are part of the learning experience.
- [ ] The specification requires README.md to function as a Getting Started guide with a table of contents near the top and a top-level demo flow listing Copilot Studio, Foundry, and Agent Framework in order.
- [ ] The specification requires numbered learner guidance that explicitly includes navigate/click/type instructions for baseline activities, with complete click-by-click coverage for the Copilot Studio baseline flow.
- [ ] The specification explicitly defines L100/L200/L300/L400, including L300 as the advanced baseline aligned to Microsoft WWL framing and L400 as optional complexity.
- [ ] The specification explicitly requires learners to build/configure the Copilot Studio and Agent Framework experiences as part of the Level 300 baseline, not only run conversations on prebuilt assets.
- [ ] The specification states that any time-constrained scope cuts are moved to Level 400 after-class extensions rather than deleted from the learning pathway.
- [ ] The Foundry phase defines exactly four required iteration artifacts: RFM output, tier/health output, VIP recency alert output with documented threshold evidence, and news-based short-term action evaluation output.
- [ ] The guidance defines synthetic news generation scope as the last 24 months and includes event-to-behavior correlation expectations with fictional company mentions.
- [ ] The specification defines artifact status values exactly as: complete (artifact exists and passes checklist criteria), incomplete (artifact missing or not yet run), and needs rework (artifact exists but fails one or more checklist criteria).
- [ ] The specification defines a Foundry progress-check loop that explicitly covers: check progress, detect remaining work, process it, and continue iterating until all four required artifacts are marked complete.
- [ ] The specification defines the Foundry stop condition as both: all four required artifacts are complete, and outputs map to all Level 300 Foundry outcomes (identification, explanation, action, portfolio summary).
- [ ] The specification keeps Foundry iteration within existing Level 300 boundaries and does not make new agent categories mandatory.

## Out of Scope
- Building production-grade churn prediction models or real-time enterprise integrations.
- Defining platform-specific implementation steps, code-level architecture, or deployment pipelines.
- Replacing human account ownership decisions with fully autonomous customer intervention.
- Expanding beyond the workshop narrative to unrelated domains, datasets, or non-customer-lifecycle use cases.
- Reframing Foundry iteration as a platform re-architecture effort, or requiring net-new mandatory workflow components beyond the established four-agent baseline.
