---
description: Draft a feature specification from natural language.
---

Create a new feature specification in `.specify/specs/<feature-id>/spec.md`.

Instructions:
1. Derive `<feature-id>` from the current branch name; strip common prefixes like `feature/`, `chore/`, `optional/`.
2. If the folder exists, update `spec.md`; otherwise create it from `.specify/templates/spec-template.md`.
3. Focus on **what** and **why** (not implementation details).
4. Include user stories, functional/non-functional requirements, acceptance criteria, and out-of-scope items.
5. Tailor requirements to this workshop repository structure and learner experience.

Return the created/updated file path and a short summary.
