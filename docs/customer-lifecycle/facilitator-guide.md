# Facilitator Guide: VIP Customer Lifecycle Workshop

## Storyline Alignment
- Business problem: detect early lifecycle decline in high-value customers and act sooner.
- Primary audience: mixed technical levels, business-first framing.
- Baseline scope: Level 300 only; Level 400 is optional enrichment.

## Canonical Level Definitions (Use Verbatim)
- **L100 (foundational orientation):** Understand scenario context, data sources, and shared vocabulary. No pass/fail completion gate.
- **L200 (intermediate):** Learners should demonstrate intermediate tool fluency before baseline grading.
- **L300 (advanced hands-on baseline, WWL-aligned):** Advanced hands-on practice that builds on L100 and L200; this is the required workshop exercise level for completion/pass.
- **L400 (optional complexity):** Extension work that deepens L300 outcomes and is excluded from pass/fail.

## Grading Enforcement (L300-Only)
- Workshop pass/fail is based on **L300 outputs only**.
- L400 content must not be used as a requirement to pass.
- If a learner completes all Level 300 outputs in `labs/customer-lifecycle/level-300/output-contract.md`, mark baseline as pass.
- If any L300 mandatory output is missing, mark baseline as not yet complete.
- Level 300 completion requires build/configure checkpoints in both Copilot Studio and Agent Framework (not conversation-only execution on prebuilt assets).

## Phase Checkpoints (Timeboxed)
| Phase | Target time | Facilitator checkpoint |
|---|---:|---|
| Copilot Studio | <=30 min | Learner built/configured baseline copilot artifacts, then produced at-risk VIP/Gold list with plain-language explanations |
| Foundry | <=60 min | Learner used New Foundry flow (Build -> Data, Build -> Workflows), produced all 4 agent outputs, and enforced `tier='VIP' AND recency_days > 60` plus 2+ risk gate |
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
1. **Portal/auth assumptions verified**
   - New Foundry toggle enabled.
   - No Project API key path used.
2. **Navigation path evidence**
   - Optional project creation path shown: Start building -> Design workflow.
   - Data ingestion performed via Build -> Data.
   - Agent implementation performed via Build -> Workflows.
3. **4-agent completion evidence**
   - Agent 1 output: `agent1_rfm`
   - Agent 2 output: `agent2_tier_health`
   - Agent 3 output: `agent3_vip_recency_alerts` with exact rule text `tier='VIP' AND recency_days > 60`
   - Agent 4 output: `agent4_news_action_eval` with scope/exception handling
4. **Threshold consistency enforcement**
    - Agent 3 threshold evidence field shows 60 days.
    - Rule text in learner output matches `common/customer-lifecycle/risk-rules.md` exactly.

## Foundry Iteration Assessment Rubric (FR-015..FR-019)
1. **Exact artifact-set enforcement (FR-015)**
   - Learner progress checks evaluate exactly four artifacts:
     - `agent1_rfm`
     - `agent2_tier_health`
     - `agent3_vip_recency_alerts`
     - `agent4_news_action_eval`
   - Each artifact includes required evidence fields from `labs/customer-lifecycle/level-300/output-contract.md`.
2. **Exact status-set enforcement (FR-016)**
   - Rubric uses only `complete`, `incomplete`, and `needs rework`.
   - Any other status wording is marked as rubric drift and requires correction.
3. **Iteration loop enforcement (FR-017)**
   - Learner demonstrates: check progress -> detect remaining work -> process remaining work -> iterate.
   - At least one explicit decision point is documented when an artifact is `needs rework`.
4. **Dual stop-condition enforcement (FR-018)**
   - Pass Foundry only when all four required artifacts are `complete`.
   - Pass Foundry only when outputs cover identification, explanation, action, and portfolio summary.
5. **Scope-boundary enforcement (FR-019)**
   - Iteration guidance remains within the existing four-agent Level 300 baseline.
   - No net-new mandatory agent categories are introduced; optional enhancements are routed to Level 400.
