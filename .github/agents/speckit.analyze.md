---
description: Analyze consistency across spec, plan, and tasks.
---

Audit `.specify/specs/<feature-id>/spec.md`, `plan.md`, and `tasks.md` for quality and alignment.

Check for:
1. Missing acceptance criteria coverage in plan/tasks.
2. Requirements without matching implementation tasks.
3. Risks not addressed by mitigation or validation steps.
4. Conflicts with `.specify/memory/constitution.md`.

Write findings to `.specify/specs/<feature-id>/analyze.md` with:
- Gaps
- Recommended fixes
- Blocking vs non-blocking issues
