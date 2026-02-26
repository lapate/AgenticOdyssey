---
description: Break a plan into ordered implementation tasks.
---

Create `.specify/specs/<feature-id>/tasks.md` from `plan.md`.

Task generation rules:
1. Start from `.specify/templates/tasks-template.md`.
2. Produce dependency-aware tasks with stable IDs (`T001`, `T002`, ...).
3. Group tasks by phases (foundation, delivery, validation).
4. Include documentation and verification tasks when relevant.
5. Keep tasks concrete and mapped to specific file paths.

If `plan.md` is missing, request `/speckit.plan` first.
