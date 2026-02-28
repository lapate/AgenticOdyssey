# Traceability Matrix: Customer Lifecycle Feature

## FR Mapping
| Requirement | Implementation mapping |
|---|---|
| FR-001 lifecycle scenario for VIP/Gold risk | `labs/customer-lifecycle/level-300/copilot-studio.md`, `labs/customer-lifecycle/level-300/foundry.md`, `docs/customer-lifecycle/learner-guide.md` |
| FR-002 2+ negative signal at-risk classification | `common/customer-lifecycle/risk-rules.md`, `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/output-contract.md` |
| FR-003 business-language explanations | `labs/customer-lifecycle/level-300/copilot-studio.md`, `labs/customer-lifecycle/level-300/agent-framework.md`, `docs/customer-lifecycle/learner-guide.md` |
| FR-004 recommended human actions | `common/customer-lifecycle/action-mapping.md`, `labs/customer-lifecycle/level-300/agent-framework.md`, `labs/customer-lifecycle/level-300/output-contract.md` |
| FR-005 portfolio minimum outputs | `labs/customer-lifecycle/level-300/output-contract.md`, `labs/customer-lifecycle/level-300/foundry.md`, `docs/customer-lifecycle/facilitator-guide.md` |
| FR-006 three progressive phases with build/config steps | `labs/customer-lifecycle/level-300/copilot-studio.md`, `labs/customer-lifecycle/level-300/foundry.md` (New Foundry, Build -> Data, Build -> Workflows), `labs/customer-lifecycle/level-300/agent-framework.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md` |
| FR-007 canonical inputs + learner-visible derived fields | `data/customer-lifecycle/derived-fields.md`, `labs/customer-lifecycle/level-300/copilot-studio.md`, `labs/customer-lifecycle/level-300/foundry.md` |
| FR-008 Level 300 baseline + isolated Level 400 optional | `labs/customer-lifecycle/level-300/output-contract.md`, `labs/customer-lifecycle/level-400/extensions.md`, `README.md`, `docs/customer-lifecycle/learner-guide.md` |
| FR-009 README as entry point with TOC + top-level flow | `README.md` |
| FR-010 numbered navigate/click/type baseline guidance | `labs/customer-lifecycle/level-300/copilot-studio.md`, `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/agent-framework.md` |
| FR-011 explicit L100/L200/L300/L400 boundaries | `README.md`, `common/customer-lifecycle/signal-dictionary.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md` |
| FR-012 scope cuts deferred to Level 400 (not deleted) | `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md`, `labs/customer-lifecycle/level-400/extensions.md` |
| FR-013 Foundry architecture-agnostic 3-5 agent workflow with explicit stage responsibilities/handoffs | `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/output-contract.md`, `common/customer-lifecycle/signal-dictionary.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md` |
| FR-014 synthetic news input scope (24 months + regional events + fictional companies) | `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/output-contract.md`, `common/customer-lifecycle/signal-dictionary.md`, `common/customer-lifecycle/action-mapping.md`, `labs/customer-lifecycle/level-400/extensions.md` |
| FR-015 learner-visible stage checkpoints + required handoff evidence | `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/output-contract.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md` |
| FR-016 source-derived validation with named-customer + aggregate checks and canonical status set | `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/output-contract.md`, `common/customer-lifecycle/signal-dictionary.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md` |
| FR-017 failure-handling path for blocked prompts, placeholder output, and missing fields | `labs/customer-lifecycle/level-300/foundry.md`, `common/customer-lifecycle/risk-rules.md`, `common/customer-lifecycle/signal-dictionary.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md` |
| FR-018 completion based on Level 300 outcomes plus real-data handoff evidence | `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/output-contract.md`, `common/customer-lifecycle/action-mapping.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md`, `README.md` |
| FR-019 architecture-agnostic constraints maintained within 3-5 agents and L300/L400 boundary | `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/output-contract.md`, `labs/customer-lifecycle/level-400/extensions.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md`, `.specify/specs/customer-lifecycle/spec.md` |
| FR-020 guardrail-safe fallback interaction pattern with parity to primary outcomes | `labs/customer-lifecycle/level-300/foundry.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md`, `.specify/specs/customer-lifecycle/spec.md` |

## NFR Mapping
| Requirement | Implementation mapping |
|---|---|
| NFR-001 non-technical clarity | `common/customer-lifecycle/signal-dictionary.md`, `docs/customer-lifecycle/learner-guide.md` |
| NFR-002 workshop timeboxes | `labs/customer-lifecycle/level-300/copilot-studio.md`, `labs/customer-lifecycle/level-300/foundry.md`, `labs/customer-lifecycle/level-300/agent-framework.md`, `docs/customer-lifecycle/facilitator-guide.md` |
| NFR-003 modular extensibility | `labs/customer-lifecycle/level-400/extensions.md`, `common/customer-lifecycle/action-mapping.md` |
| NFR-004 consistent terminology | `common/customer-lifecycle/signal-dictionary.md`, `docs/customer-lifecycle/facilitator-guide.md`, `docs/customer-lifecycle/learner-guide.md` |
| NFR-005 low-friction learner safety | `labs/customer-lifecycle/level-300/*.md`, `docs/customer-lifecycle/learner-guide.md` |
| NFR-006 scannable orientation-friendly docs | `README.md`, `docs/customer-lifecycle/learner-guide.md`, `docs/customer-lifecycle/facilitator-guide.md` |
