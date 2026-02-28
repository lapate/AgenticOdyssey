# Feature Specification: VIP Customer Lifecycle Workshop Scenario

## Summary
Define a workshop-ready, specification-driven learning scenario that helps learners identify and respond to early lifecycle risk in VIP and Gold customers using the provided Zava sales narrative and dataset. This feature matters because the workshop’s core value is teaching practical AI-assisted business decision support—showing who is at risk, why risk is emerging, and what humans should do next—within strict classroom timeboxes and mixed learner skill levels. Foundry requirements should prioritize guardrail-resilient execution and measurable learning outcomes rather than a fixed implementation topology.

## Clarifications
- 2026-02-27: A customer is classified as at-risk only when **two or more** negative lifecycle signals are present.
- 2026-02-27: Portfolio-level minimum outputs must include **tier counts**, **at-risk counts**, and **at-risk percentage by tier**.
- 2026-02-27: The Level 300 baseline must include **at-risk VIP/Gold identification**, a **plain-language explanation**, a **recommended action**, and a **portfolio summary**.
- 2026-02-27: Level 400 scope is **optional complexity enhancements only** and must **not** block Level 300 core learning outcomes.
- 2026-02-28: Foundry guidance must be guardrail-resilient and should avoid depending on full-table chat responses when tenant controls block them.
- 2026-02-28: The specification is intentionally architecture-agnostic; it defines outcomes and constraints, not one required orchestration topology.
- 2026-02-28: The targeted Foundry solution must use at least **3** and no more than **5** agents to demonstrate meaningful multi-agent complexity without overwhelming learners.
- 2026-02-28: Foundry process guidance should focus on explicit validation outcomes and remediation steps; a detailed iteration-cycle script is optional and should only be kept when it adds clear learner value.

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
As an instructor or learner, I want clear definitions of L100, L200, L300, and L400 (including what is core vs optional), so that workshop expectations and learning boundaries are unambiguous.

### Story 8 - Build a Multi-Agent Foundry Workflow
As a technical learner supporting a business SME scenario, I want Foundry to demonstrate a clear multi-agent workflow (3-5 agents) with explicit handoffs, so that I can connect orchestration patterns to business-facing decisions.

### Story 9 - Validate Foundry Outcomes Under Guardrails
As a workshop learner, I want clear validation and fallback guidance when guardrails block interactions, so that I can still demonstrate complete multi-agent outcomes with real data.

## Functional Requirements
- [FR-001] The feature must define a lifecycle-monitoring scenario focused on VIP and Gold customer risk in Zava’s sales context.
- [FR-002] The feature must require identification of at-risk behavior using lifecycle signals (such as slowing order frequency, increased time since purchase, and declining spend), and must classify a customer as at-risk only when two or more negative signals are present.
- [FR-003] The feature must require explanation outputs that describe why a customer is considered at risk using understandable business language.
- [FR-004] The feature must require recommended human actions (e.g., retention outreach, account follow-up, pricing/margin review, targeted offers) linked to identified risk.
- [FR-005] The feature must require portfolio-level visibility with, at minimum, tier counts, at-risk counts, and at-risk percentage by tier.
- [FR-006] The feature must define three progressive workshop phases aligned to repository learning flow: (1) build/configure the Copilot Studio conversational experience and run insight prompts, (2) prepare structured scoring outputs in Foundry, and (3) build/configure the Agent Framework alert workflow and run proactive alert demonstrations.
- [FR-007] The feature must require that all core scenario inputs originate from the provided workshop dataset and narrative (with the explicit exception of the synthetic news input defined in FR-014), and that derived fields are explicitly called out as learner-visible transformations.
- [FR-008] The feature must support a Level 300 baseline experience that includes at-risk VIP/Gold identification, plain-language explanation, recommended action, and portfolio summary, with clearly marked Level 400 extensions that are optional and do not block Level 300 core learning outcomes.
- [FR-009] The feature must require README.md to function as the workshop entry point by including: (a) a table of contents near the top of the file, and (b) a top-level end-to-end demo flow that lists Copilot Studio, Foundry, and Agent Framework in learning order.
- [FR-010] The feature must require numbered, step-by-step learner instructions for baseline activities that state where to navigate, what to click, and what text to enter; Copilot Studio baseline steps must be fully documented in this format.
- [FR-011] The feature must define learning levels with explicit scope boundaries: L100 = foundational orientation, L200 = intermediate hands-on learning, L300 = advanced hands-on baseline for workshop core learning (building on L100 and L200, aligned with Microsoft WWL framing), and L400 = optional complexity extensions that do not block Level 300 core outcomes.
- [FR-012] If classroom time requires scope cuts, non-essential enhancements must be moved to explicit Level 400 after-class extensions; required Level 300 build/configuration steps must remain in-class and must not be removed.
- [FR-013] The Foundry phase must demonstrate an architecture-agnostic multi-agent workflow using **3 to 5 agents** with explicit stage responsibilities and handoffs that collectively produce lifecycle insights and recommended actions.
- [FR-014] The news-based evaluation input must be a synthetic, learner-visible dataset covering the most recent 24 months and include regional events (for example natural disasters and major public events) plus fictional company references (for example Contoso) so students can correlate behavior changes to events.
- [FR-015] The Foundry phase must define learner-visible checkpoints that map each stage in the selected 3-5 agent design to required Level 300 outcomes and required handoff artifact evidence.
- [FR-016] Foundry validation guidance must require source-derived outputs (not example/placeholder output) using at least one named-customer spot-check and one aggregate artifact-level check, both traceable to produced workflow artifacts.
- [FR-017] Foundry guidance must include a concise failure-handling decision path for: (a) guardrail-blocked prompts, (b) generic/placeholder outputs, and (c) missing required fields, including targeted stage rework instructions.
- [FR-018] Foundry completion criteria must require that outputs map to all Level 300 outcomes (identification, explanation, action, portfolio summary), and that validation evidence demonstrates real data progression through stage handoffs.
- [FR-019] Foundry requirements must remain architecture-agnostic: no single fixed orchestration topology is mandatory, provided implementation stays within the 3-5 agent range, preserves required stage outcomes, and includes required validation evidence.
- [FR-020] The Foundry phase must include at least one guardrail-safe fallback interaction pattern (for example artifact-first or scoped prompt sequence) that preserves the same Level 300 outcomes and validation evidence as the primary interaction path when blocked.

## Non-Functional Requirements
- [NFR-001] The scenario must be understandable by non-technical learners and business leaders, prioritizing clarity over algorithmic complexity.
- [NFR-002] The scenario must fit workshop delivery constraints: Copilot Studio within 30 minutes, Foundry within 60 minutes, and Agent Framework within 10 minutes.
- [NFR-003] The scenario must be modular and extensible so instructors can add advanced exercises without changing baseline outcomes.
- [NFR-004] The scenario must maintain consistent terminology across phases (customer health, risk signals, tiers, actions) to reduce learner confusion.
- [NFR-005] The scenario must preserve learner safety and confidence by keeping core flows low-friction and avoiding heavy prerequisite setup during class time.
- [NFR-006] Learner-facing documentation must be scannable and orientation-friendly, with predictable sectioning and navigation so participants can recover quickly if they fall behind.
- [NFR-007] Foundry validation guidance must minimize learner ambiguity by using clear success/failure signals and guardrail-safe next steps that can be followed quickly under workshop time pressure.

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
- [ ] The Foundry phase defines a 3-5 agent workflow with explicit handoffs and clearly mapped responsibilities.
- [ ] The guidance defines synthetic news generation scope as the last 24 months and includes event-to-behavior correlation expectations with fictional company mentions.
- [ ] The specification requires source-derived validation evidence using at least one named-customer spot-check and one aggregate artifact-level check.
- [ ] The specification defines guardrail-safe fallback guidance when primary prompt patterns are blocked.
- [ ] The specification defines Foundry completion in terms of Level 300 outcomes (identification, explanation, action, portfolio summary) and real-data evidence, not a fixed topology.
- [ ] The specification keeps Foundry architecture constraints to a 3-5 agent range without mandating one implementation pattern.

## Out of Scope
- Building production-grade churn prediction models or real-time enterprise integrations.
- Defining platform-specific implementation steps, code-level architecture, or deployment pipelines.
- Replacing human account ownership decisions with fully autonomous customer intervention.
- Expanding beyond the workshop narrative to unrelated domains, datasets, or non-customer-lifecycle use cases.
- Requiring one exact orchestration topology for all tenants or environments.
- Expanding beyond the 3-5 agent complexity band for baseline learning flows.
