# Validation Checklist and Evidence Record

## FR-015..FR-019 Validation Checklist
| Check | Status | Evidence |
|---|---|---|
| Exact artifact set is defined as only `agent1_rfm`, `agent2_tier_health`, `agent3_vip_recency_alerts`, `agent4_news_action_eval` | Pass | `labs/customer-lifecycle/level-300/foundry.md` (Foundry Progress Checkpoints), `labs/customer-lifecycle/level-300/output-contract.md` (FR-015 Artifact Contract) |
| Exact status set is limited to `complete`, `incomplete`, `needs rework` | Pass | `common/customer-lifecycle/signal-dictionary.md` (Foundry Artifact Status Model), `labs/customer-lifecycle/level-300/foundry.md` (Status Assessment), `docs/customer-lifecycle/learner-guide.md` |
| Iteration loop is explicit: check progress -> detect remaining work -> process remaining work -> iterate | Pass | `labs/customer-lifecycle/level-300/foundry.md` (Learner Iteration Loop), `docs/customer-lifecycle/learner-guide.md`, `README.md` |
| Stop condition is dual: all four artifacts complete + Level 300 outcomes covered | Pass | `labs/customer-lifecycle/level-300/foundry.md` (Stop Condition), `docs/customer-lifecycle/facilitator-guide.md` (Iteration rubric), `README.md` |
| Scope boundary is preserved (no net-new mandatory agent categories) | Pass | `labs/customer-lifecycle/level-300/foundry.md` (Scope-Boundary Guardrail), `labs/customer-lifecycle/level-400/extensions.md` (Isolation and Governance Rules), `.specify/specs/customer-lifecycle/spec.md` (Clarifications) |

## Simulated `needs rework` Iteration Evidence (T015)
Scenario: learner run where Agent 3 output exists but fails threshold evidence checklist.

1. **Initial progress check**
   - `agent1_rfm` = `complete`
   - `agent2_tier_health` = `complete`
   - `agent3_vip_recency_alerts` = `needs rework` (missing `agent3_rule_text`)
   - `agent4_news_action_eval` = `incomplete`
2. **Remaining work detection**
   - Remaining work exists because one artifact is `needs rework` and one is `incomplete`.
3. **Process remaining work**
   - Re-run/fix Agent 3 to include both `vip_recency_threshold_days` (=60) and `agent3_rule_text` (`tier='VIP' AND recency_days > 60`).
   - Complete Agent 4 output with required scope evidence (`news_dataset_name`, `scope_window_months`).
4. **Iteration re-check**
   - `agent1_rfm` = `complete`
   - `agent2_tier_health` = `complete`
   - `agent3_vip_recency_alerts` = `complete`
   - `agent4_news_action_eval` = `complete`
5. **Stop-condition verification**
   - Artifact completeness condition met: all four `complete`.
   - Outcome coverage condition met: identification, explanation, action, and portfolio summary are all present.
   - Loop may stop.

Remediation items: None.
