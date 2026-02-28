# AgenticOdyssey Getting Started

This repository contains a workshop scenario for identifying early lifecycle risk in high-value customers (VIP/Gold) and taking practical retention actions.

## Table of Contents
- [Workshop Demo Flow (Start Here)](#workshop-demo-flow-start-here)
- [First-Time Onboarding](#first-time-onboarding)
- [Returning Learner Fast Path](#returning-learner-fast-path)
- [Learning Levels and Pass/Fail Boundary](#learning-levels-and-passfail-boundary)
- [Level 300 Required Output Checklist](#level-300-required-output-checklist)
- [Direct Links](#direct-links)
- [Spec-Kit Commands (Authoring Flow)](#spec-kit-commands-authoring-flow)

## Workshop Demo Flow (Start Here)
Follow this end-to-end order:
1. **Copilot Studio** (build/configure + conversational insight): build/configure the Level 300 copilot artifacts, then identify at-risk VIP/Gold customers and draft plain-language explanations/actions.
2. **Foundry** (structured scoring + iteration control): use New Foundry navigation (**Build -> Data**, **Build -> Workflows**) to run an architecture-agnostic **3-5 agent** flow that produces required stage artifacts, then iterate with **check progress -> detect remaining work -> process remaining work -> iterate** until required artifacts are `complete` and outcomes cover identification, explanation, action, and portfolio summary. If primary prompts are guardrail-blocked, use the documented guardrail-safe fallback path and validate parity.
3. **Agent Framework** (build/configure + proactive demo): build/configure the Level 300 alert workflow, then generate explain-only alerts for at-risk VIP/Gold customers.

## First-Time Onboarding
1. Open the learner guide: `docs/customer-lifecycle/learner-guide.md`.
2. Run the labs in order:
   1. `labs/customer-lifecycle/level-300/copilot-studio.md`
   2. `labs/customer-lifecycle/level-300/foundry.md`
   3. `labs/customer-lifecycle/level-300/agent-framework.md`
3. Keep `labs/customer-lifecycle/level-300/output-contract.md` open while working; this is the core learning baseline.

## Returning Learner Fast Path
If you have already completed orientation:
1. Go directly to `labs/customer-lifecycle/level-300/copilot-studio.md`.
2. Complete Level 300 outputs per `labs/customer-lifecycle/level-300/output-contract.md`.
3. Use `labs/customer-lifecycle/level-400/extensions.md` only after L300 is complete.

## Learning Levels and Core Learning Boundary
Canonical definitions (aligned with shared docs):
- **L100 (foundational orientation):** Understand scenario context, data sources, and shared vocabulary.
- **L200 (intermediate):** Build practical familiarity with the tools and data shaping approach before the core multi-agent baseline.
- **L300 (advanced hands-on baseline, WWL-aligned):** Advanced hands-on practice that builds on L100 and L200; this is the required workshop baseline for core learning outcomes and multi-agent pattern mastery.
- **L400 (optional complexity):** Extension work that deepens L300 outcomes; enrichment only after the L300 core baseline.

Core learning boundary:
- **Core learning completion requires L300 outcomes.**
- **L400 is optional enrichment and must not block core completion.**
- If in-class scope must be cut, move non-essential items to `labs/customer-lifecycle/level-400/extensions.md` as after-class extensions (do not delete them).

## Level 300 Required Output Checklist
Your Level 300 submission must include:
1. At-risk VIP/Gold identification using the **2+ negative-signal rule**.
2. Plain-language explanation for each at-risk VIP/Gold customer.
3. Recommended human action for each at-risk VIP/Gold customer.
4. Portfolio summary:
   - Tier counts
   - At-risk counts
   - At-risk % by tier

## Direct Links
- Learner guide: `docs/customer-lifecycle/learner-guide.md`
- Facilitator guide: `docs/customer-lifecycle/facilitator-guide.md`
- Signal dictionary: `common/customer-lifecycle/signal-dictionary.md`
- Risk rules: `common/customer-lifecycle/risk-rules.md`
- Level 300 output contract: `labs/customer-lifecycle/level-300/output-contract.md`
- Copilot Studio lab: `labs/customer-lifecycle/level-300/copilot-studio.md`
- Foundry lab: `labs/customer-lifecycle/level-300/foundry.md`
- Agent Framework lab: `labs/customer-lifecycle/level-300/agent-framework.md`
- Optional L400 extensions: `labs/customer-lifecycle/level-400/extensions.md`

## Spec-Kit Commands (Authoring Flow)
Use this flow when creating new features:
1. `/speckit.specify`
2. `/speckit.clarify` (optional)
3. `/speckit.plan`
4. `/speckit.tasks`
5. `/speckit.implement`
