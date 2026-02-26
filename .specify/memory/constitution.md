# AgenticOdyssey Spec Constitution

## Purpose
This repository uses Spec-Driven Development to keep workshop changes predictable, reviewable, and reproducible.

## Core Principles
1. **Lab-first clarity**: Specs must clearly identify which lab(s) are impacted and what learner outcome changes.
2. **Notebook safety**: Changes to notebooks must preserve runnable order and avoid hidden dependencies.
3. **Minimal disruption**: Prefer additive, backward-compatible changes to existing workshop content.
4. **Verification required**: Every implementation plan must include practical validation steps.
5. **Documentation parity**: Any behavior change in labs must be reflected in repository documentation.

## Quality Gates
- A feature spec must define user stories and measurable acceptance criteria.
- A plan must identify impacted paths before implementation starts.
- Tasks must be independently testable and ordered by dependency.
- Work is incomplete until validation is documented.

## Repository Context
- Primary delivery artifacts are workshop docs and notebooks under `labs/`.
- Shared guidance is kept in `common/`.
- Screenshots and handout assets are under `docs/screenshots/`.
