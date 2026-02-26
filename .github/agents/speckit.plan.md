---
description: Create a technical implementation plan from a spec.
---

Generate `.specify/specs/<feature-id>/plan.md` from the corresponding `spec.md`.

Requirements:
1. Start from `.specify/templates/plan-template.md`.
2. List impacted repository paths (for example `labs/`, `common/`, `docs/`).
3. Document design decisions, risks, and mitigations.
4. Add a validation plan with concrete steps.
5. Keep the plan implementation-focused and consistent with the constitution.

If the feature spec does not exist, request `/speckit.specify` first.
