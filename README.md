# AgenticOdyssey Getting Started

This repository contains a workshop scenario for identifying early lifecycle risk in high-value customers (VIP/Gold) and taking practical retention actions.

## Table of Contents
- [Workshop Demo Flow (Start Here)](#workshop-demo-flow-start-here)
- [First-Time Onboarding](#first-time-onboarding)
- [Returning Learner Fast Path](#returning-learner-fast-path)
- [Learning Levels and Pass/Fail Boundary](#learning-levels-and-passfail-boundary)
- [Level 200 Required Output Checklist](#level-200-required-output-checklist)
- [Direct Links](#direct-links)
- [Spec-Kit Commands (Authoring Flow)](#spec-kit-commands-authoring-flow)

## Workshop Demo Flow (Start Here)
Follow this end-to-end order:
1. **Copilot Studio** (conversational insight): identify at-risk VIP/Gold customers and draft plain-language explanations/actions.
2. **Foundry** (structured scoring): calculate lifecycle signals and enforce the 2+ negative-signal rule.
3. **Agent Framework** (proactive demo): generate explain-only alerts for at-risk VIP/Gold customers.

## First-Time Onboarding
1. Open the learner guide: `docs/customer-lifecycle/learner-guide.md`.
2. Run the labs in order:
   1. `labs/customer-lifecycle/level-200/copilot-studio.md`
   2. `labs/customer-lifecycle/level-200/foundry.md`
   3. `labs/customer-lifecycle/level-200/agent-framework.md`
3. Keep `labs/customer-lifecycle/level-200/output-contract.md` open while working; this is the grading baseline.

## Returning Learner Fast Path
If you have already completed orientation:
1. Go directly to `labs/customer-lifecycle/level-200/copilot-studio.md`.
2. Complete Level 200 outputs per `labs/customer-lifecycle/level-200/output-contract.md`.
3. Use `labs/customer-lifecycle/level-300/extensions.md` only after L200 is complete.

## Learning Levels and Pass/Fail Boundary
Canonical definitions (aligned with shared docs):
- **L100 (foundational orientation):** Understand scenario context, data sources, and shared vocabulary. No pass/fail completion gate.
- **L200 (required baseline hands-on competency):** Deliver the required workshop outputs for completion/pass.
- **L300 (advanced hands-on practice, WWL-aligned):** Advanced hands-on practice that builds on L100 and L200; optional enrichment and excluded from pass/fail.

Pass/fail boundary:
- **Pass requires L200 completion.**
- **L300 is optional and must not affect pass/fail.**

## Level 200 Required Output Checklist
Your Level 200 submission must include:
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
- Level 200 output contract: `labs/customer-lifecycle/level-200/output-contract.md`
- Copilot Studio lab: `labs/customer-lifecycle/level-200/copilot-studio.md`
- Foundry lab: `labs/customer-lifecycle/level-200/foundry.md`
- Agent Framework lab: `labs/customer-lifecycle/level-200/agent-framework.md`
- Optional L300 extensions: `labs/customer-lifecycle/level-300/extensions.md`

## Spec-Kit Commands (Authoring Flow)
Use this flow when creating new features:
1. `/speckit.specify`
2. `/speckit.clarify` (optional)
3. `/speckit.plan`
4. `/speckit.tasks`
5. `/speckit.implement`
