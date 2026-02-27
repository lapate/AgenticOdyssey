# Feature Specification: VIP Customer Lifecycle Workshop Scenario

## Summary
Define a workshop-ready, specification-driven learning scenario that helps learners identify and respond to early lifecycle risk in VIP and Gold customers using the provided Zava sales narrative and dataset. This feature matters because the workshop’s core value is teaching practical AI-assisted business decision support—showing who is at risk, why risk is emerging, and what humans should do next—within strict classroom timeboxes and mixed learner skill levels.

## Clarifications
- 2026-02-27: A customer is classified as at-risk only when **two or more** negative lifecycle signals are present.
- 2026-02-27: Portfolio-level minimum outputs must include **tier counts**, **at-risk counts**, and **at-risk percentage by tier**.
- 2026-02-27: The Level 200 baseline must include **at-risk VIP/Gold identification**, a **plain-language explanation**, a **recommended action**, and a **portfolio summary**.
- 2026-02-27: Level 300 scope is **optional enhancements only** and must **not** affect Level 200 pass/fail.

## User Stories
### Story 1 - Surface At-Risk High-Value Customers
As a sales operations learner, I want to identify VIP and Gold customers with declining engagement signals, so that I can prioritize retention-focused attention before churn occurs.

### Story 2 - Explain Risk in Business Terms
As a business stakeholder learner, I want clear explanations for customer health changes (recency, frequency, spend, margin, and mix), so that I can understand risk drivers without needing deep technical analysis.

### Story 3 - Recommend Practical Next Steps
As an account management learner, I want actionable recommendations tied to customer risk signals, so that I can move from insight to timely outreach and intervention.

### Story 4 - Learn Through Progressive Demo Phases
As a workshop participant, I want the scenario structured across Copilot Studio, Foundry, and Agent Framework phases, so that I can build confidence incrementally and complete core outcomes in class.

### Story 5 - Start Quickly from the Repository Entry Point
As a first-time workshop learner, I want README.md to function primarily as a Getting Started guide with a clear table of contents and top-level demo flow, so that I can understand where to begin and how the parts fit together.

### Story 6 - Follow Click-by-Click Demo Instructions
As a learner with varied tool familiarity, I want explicit step-by-step guidance (where to navigate, what to click, and what to type), especially for the Copilot Studio flow, so that I can complete the exercises without guesswork.

### Story 7 - Understand Learning Levels and Expectations
As an instructor or learner, I want clear definitions of L100, L200, and L300 (including what is required vs optional), so that workshop expectations and pass/fail boundaries are unambiguous.

## Functional Requirements
- [FR-001] The feature must define a lifecycle-monitoring scenario focused on VIP and Gold customer risk in Zava’s sales context.
- [FR-002] The feature must require identification of at-risk behavior using lifecycle signals (such as slowing order frequency, increased time since purchase, and declining spend), and must classify a customer as at-risk only when two or more negative signals are present.
- [FR-003] The feature must require explanation outputs that describe why a customer is considered at risk using understandable business language.
- [FR-004] The feature must require recommended human actions (e.g., retention outreach, account follow-up, pricing/margin review, targeted offers) linked to identified risk.
- [FR-005] The feature must require portfolio-level visibility with, at minimum, tier counts, at-risk counts, and at-risk percentage by tier.
- [FR-006] The feature must define three progressive workshop phases aligned to repository learning flow: conversational insight (Copilot Studio), structured scoring preparation (Foundry), and proactive alert demonstration (Agent Framework).
- [FR-007] The feature must require that all core scenario inputs originate from the provided workshop dataset and narrative, with derived fields explicitly called out as learner-visible transformations.
- [FR-008] The feature must support a Level 200 baseline experience that includes at-risk VIP/Gold identification, plain-language explanation, recommended action, and portfolio summary, with clearly marked Level 300 extensions that are optional and do not affect Level 200 pass/fail.
- [FR-009] The feature must require README.md to function as the workshop entry point by including: (a) a table of contents near the top of the file, and (b) a top-level end-to-end demo flow that lists Copilot Studio, Foundry, and Agent Framework in learning order.
- [FR-010] The feature must require numbered, step-by-step learner instructions for baseline activities that state where to navigate, what to click, and what text to enter; Copilot Studio baseline steps must be fully documented in this format.
- [FR-011] The feature must define learning levels with explicit scope boundaries: L100 = foundational orientation, L200 = required baseline hands-on competency for workshop completion, and **L300 = advanced hands-on practice building on L100 and L200, aligned with Microsoft WWL framing, and optional for pass/fail.**

## Non-Functional Requirements
- [NFR-001] The scenario must be understandable by non-technical learners and business leaders, prioritizing clarity over algorithmic complexity.
- [NFR-002] The scenario must fit workshop delivery constraints: Copilot Studio within 30 minutes, Foundry within 60 minutes, and Agent Framework within 10 minutes.
- [NFR-003] The scenario must be modular and extensible so instructors can add advanced exercises without changing baseline outcomes.
- [NFR-004] The scenario must maintain consistent terminology across phases (customer health, risk signals, tiers, actions) to reduce learner confusion.
- [NFR-005] The scenario must preserve learner safety and confidence by keeping core flows low-friction and avoiding heavy prerequisite setup during class time.
- [NFR-006] Learner-facing documentation must be scannable and orientation-friendly, with predictable sectioning and navigation so participants can recover quickly if they fall behind.

## Acceptance Criteria
- [ ] A learner can describe the business problem as “detect early lifecycle decline in high-value customers and act sooner.”
- [ ] The specification includes at least three user-visible risk signals and explains why each matters to retention outcomes.
- [ ] The specification defines at-risk classification as requiring two or more negative signals.
- [ ] The specification includes recommended actions mapped to identified risk conditions, not just descriptive analytics.
- [ ] The specification defines portfolio minimum outputs as tier counts, at-risk counts, and at-risk percentage by tier.
- [ ] The specification defines all three workshop phases and aligns them to expected learner outcomes and timeboxes.
- [ ] The specification explicitly defines Level 200 baseline outputs (at-risk VIP/Gold identification, plain-language explanation, recommended action, portfolio summary) and marks Level 300 as optional-only.
- [ ] The specification references workshop-relevant source inputs (narrative + Zava sales Excel) and clarifies that derived fields are part of the learning experience.
- [ ] The specification requires README.md to function as a Getting Started guide with a table of contents near the top and a top-level demo flow listing Copilot Studio, Foundry, and Agent Framework in order.
- [ ] The specification requires numbered learner guidance that explicitly includes navigate/click/type instructions for baseline activities, with complete click-by-click coverage for the Copilot Studio baseline flow.
- [ ] The specification explicitly defines L100/L200/L300 and includes the exact L300 advanced-level intent aligned to Microsoft WWL framing.

## Out of Scope
- Building production-grade churn prediction models or real-time enterprise integrations.
- Defining platform-specific implementation steps, code-level architecture, or deployment pipelines.
- Replacing human account ownership decisions with fully autonomous customer intervention.
- Expanding beyond the workshop narrative to unrelated domains, datasets, or non-customer-lifecycle use cases.
