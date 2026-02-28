# Facilitator Guide: VIP Customer Lifecycle Workshop

## Storyline Alignment
- Business problem: detect early lifecycle decline in high-value customers and act sooner.
- Primary audience: mixed technical levels, business-first framing.
- Baseline scope: Level 300 only; Level 400 is optional enrichment.

## Canonical Level Definitions (Use Verbatim)
- **L100 (foundational orientation):** Understand scenario context, data sources, and shared vocabulary.
- **L200 (intermediate):** Learners should demonstrate intermediate tool fluency before core multi-agent baseline work.
- **L300 (advanced hands-on baseline, WWL-aligned):** Advanced hands-on practice that builds on L100 and L200; this is the required workshop baseline for core learning outcomes and multi-agent pattern mastery.
- **L400 (optional complexity):** Extension work that deepens L300 outcomes and is optional enrichment after L300.

## Learning Outcome Enforcement (L300 Core)
- Workshop core-learning completion is based on **L300 outputs only**.
- L400 content must not be used as a requirement for core completion.
- If a learner completes all Level 300 outputs in `labs/customer-lifecycle/level-300/output-contract.md`, mark core baseline as complete.
- If any L300 mandatory output is missing, mark baseline as not yet complete.
- Level 300 completion requires build/configure checkpoints in both Copilot Studio and Agent Framework (not conversation-only execution on prebuilt assets).

## Phase Checkpoints (Timeboxed)
| Phase | Target time | Facilitator checkpoint |
|---|---:|---|
| Copilot Studio | <=30 min | Learner built/configured baseline copilot artifacts, then produced at-risk VIP/Gold list with plain-language explanations |
| Foundry | <=60 min | Learner used New Foundry flow (Build -> Data, Build -> Workflows), produced required stage outcomes with a 3-5 agent topology, and enforced 2+ risk gate |
| Agent Framework | <=10 min | Learner built/configured alert workflow, then showed explain-only alerts with mapped actions |

## Timing Rubric
- Copilot Studio: **<= 30 minutes**
- Foundry: **<= 60 minutes**
- Agent Framework: **<= 10 minutes**
- If a team overruns, prioritize completion of remaining L300 mandatory outputs before any L400 activity.

## Scope-Cut Policy (FR-012)
- If time pressure requires scope cuts, defer only non-essential items.
- Move each deferred item to `labs/customer-lifecycle/level-400/extensions.md` as an explicitly labeled after-class extension.
- Do **not** delete deferred content from the learning pathway.
- Do **not** remove required Level 300 build/configuration steps from in-class delivery.

## Misclassification Mitigation Prompts
Use these prompts when learners over-classify:
1. "How many negative signals are present for this customer?"
2. "Is the count at least two? If not, should status be watch instead of at-risk?"
3. "Which two concrete signals justify the at-risk label?"

## Portfolio Metric Interpretation Guidance
- Tier counts show portfolio composition.
- At-risk counts identify concentration of intervention workload.
- At-risk % by tier normalizes risk across differently sized tiers.
- Prioritize outreach queue: VIP at-risk first, Gold at-risk second.

## Documentation Parity Notes
- Labs and guides use shared terms: customer health, risk signals, tiers, actions.
- Baseline logic in all phases must match `common/customer-lifecycle/risk-rules.md`.

## Foundry Assessment Rubric (Required Evidence)
1. **3-5 agent compliance**
   - Workflow uses at least 3 and no more than 5 agents.
   - Topology may vary, but required stage outcomes are present.
2. **Portal/auth assumptions verified**
   - New Foundry toggle enabled.
   - No Project API key path used.
3. **Navigation path evidence**
   - Optional project creation path shown: Start building -> Design workflow.
   - Data ingestion performed via Build -> Data.
   - Agent implementation performed via Build -> Workflows.
4. **Stage outcome completion evidence**
   - `agent2-tier-report-{{customer_id}}`
   - `stage3_explain_action`
   - `stage4_portfolio_summary`
   - `stage5_news_enrichment` when enrichment is used
5. **Risk-gate consistency enforcement**
   - At-risk classification enforces `negative_signal_count >= 2`.
   - VIP recency escalation check (`tier='VIP' AND recency_days > 60`) may be implemented in any stage/agent without replacing 2+ gate.

## FR-016..FR-020 Scoring Gates
| Gate | Pass criteria | Fail signal |
|---|---|---|
| FR-016 source-derived validation | Named-customer spot-check and aggregate portfolio check both pass with artifact lineage evidence | Placeholder/generic responses or missing lineage |
| FR-017 failure handling | Learner correctly applies remediation for `guardrail_blocked`, `placeholder_output`, and `missing_required_fields` | No clear remediation path or wrong rework target |
| FR-018 completion criteria | Identification, explanation, action, and portfolio summary all present and mapped to stage artifacts | One or more Level 300 outcomes missing |
| FR-019 architecture agnostic | No fixed topology mandated; submission remains within 3-5 agents and delivers required stages | Requires one topology or falls outside 3-5 |
| FR-020 fallback parity | At least one guardrail-safe fallback path yields same outcomes/evidence as primary path | Fallback path produces partial/non-equivalent outputs |

## Foundry Remediation Scoring
Use this scoring lens during walkthroughs:
- **Pass with confidence:** failure detected, correct remediation applied, recheck passed.
- **Pass with coaching:** failure detected but remediation needed facilitator hint.
- **Not yet pass:** remediation skipped, incomplete, or did not restore required evidence.
## Foundry Iteration Assessment Rubric (FR-015..FR-020)
1. **Required stage-set enforcement (FR-015)**
   - Learner progress checks evaluate required stage artifacts from `output-contract.md`.
   - Stage 5 is required only when enrichment is used.
   - Each artifact includes required evidence fields.
2. **Exact status-set enforcement (FR-016)**
   - Rubric uses only `complete`, `incomplete`, and `needs rework`.
   - Any other status wording is marked as rubric drift and requires correction.
3. **Iteration loop enforcement (FR-017)**
   - Learner demonstrates: check progress -> detect remaining work -> process remaining work -> iterate.
   - At least one explicit decision point is documented when an artifact is `needs rework`.
4. **Dual stop-condition enforcement (FR-018)**
   - Pass Foundry only when required artifacts are `complete`.
   - Pass Foundry only when outputs cover identification, explanation, action, and portfolio summary.
5. **Scope-boundary enforcement (FR-019)**
   - Submission remains within a 3-5 agent topology and is outcome-driven.
   - Optional enhancements are routed to Level 400.
6. **Fallback-path parity enforcement (FR-020)**
   - Learner demonstrates at least one fallback path when primary prompt flow is blocked.
   - Fallback output parity is confirmed against primary-path Level 300 outcomes.
