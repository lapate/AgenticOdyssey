---
description: Clarify ambiguities in a feature specification.
---

Review `.specify/specs/<feature-id>/spec.md` and identify unclear or missing requirements.

Workflow:
1. Ask targeted clarification questions where ambiguity blocks planning.
2. Capture resolved answers in a `## Clarifications` section in the same `spec.md`.
3. Rewrite ambiguous requirements into explicit, testable statements.
4. Do not introduce implementation details not requested by the user.

If `spec.md` is missing, instruct to run `/speckit.specify` first.
