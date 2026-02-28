# Level 400 Optional Complexity Extensions

> **L400 Optional Only:** These activities are complexity extensions and are explicitly outside core learning completion requirements.
>
> **Do not gate completion on this file.** Core learning completion is determined by Level 300 only.

## How to Use This File
1. Complete all Level 300 outputs first (`labs/customer-lifecycle/level-300/output-contract.md`).
2. Pick **one** extension candidate to avoid scope creep.
3. Keep baseline outputs unchanged and add extension artifacts separately.
4. Label all deliverables with `Level 400 Optional`.

## Deferred In-Class Scope Cuts (After-Class Intake)
Use this section when classroom time requires scope cuts:
1. Do not delete non-essential items from the learning pathway.
2. Move each deferred non-essential item here as an after-class extension note.
3. Use the template below for every deferred item:

| Deferred item | Source lab/doc | Why deferred in class | After-class owner/date | Status |
|---|---|---|---|---|
| _example: Add trend visual callout cards_ | `labs/customer-lifecycle/level-300/foundry.md` | Timebox overrun during Foundry step 9 | _TBD_ | Planned |

Level 300 required build/configuration steps are not eligible for deferral.

## Product Target Map
| Extension candidate | Primary product focus | Supporting product(s) |
|---|---|---|
| A - Weighted Customer Health Index | Foundry | Copilot Studio, Agent Framework |
| B - Trend Visualization Pack | Foundry | Copilot Studio |
| C - Segment-Specific Threshold Testing | Foundry | Copilot Studio, Agent Framework |
| D - Agent Escalation Workflow | Agent Framework | Foundry |
| E - Offer Recommendation Playbooks | Copilot Studio | Foundry, Agent Framework |
| F - News Scenario Expansion | Foundry | Copilot Studio, Agent Framework |

## Audience and Delivery Lens
- **Primary executor:** technical student building the extension in a hands-on lab context.
- **Primary beneficiary:** Business SME who needs clearer decision support from the extension output.
- **Secondary audience:** facilitator/reviewer validating technical quality and business usefulness.

For every extension candidate, provide two deliverables:
1. **Technical build artifact** (what you configured/built, with reproducible steps or configuration summary).
2. **Business SME readout** (what changed, why it matters, and recommended next action in plain business language).

## Extension Candidate A - Weighted Customer Health Index
### Objective
Create a weighted index to compare against the baseline 2+ signal rule and explain when both methods agree or disagree.

### What to Build
- A configurable weight table for recency, frequency, spend, margin, and mix (weights sum to 100).
- A normalized score per customer (for example 0-100).
- A comparison table with: `risk_status` (baseline), `chi_score` (extension), and `agreement_flag`.

### Expected Output
- Documented weight assumptions and why they were chosen.
- A short interpretation of at least 3 disagreement cases (baseline at-risk vs index non-high-risk, or vice versa).

### Success Criteria
- Baseline classifier remains unchanged.
- The comparison is reproducible and explainable in plain business terms.

## Extension Candidate B - Trend Visualization Pack
### Objective
Visualize risk concentration and movement over time for business readouts.

### What to Build
- Tier-level trend view showing at-risk count over time.
- Tier-level at-risk percentage trend over time.
- Optional callout cards for biggest week-over-week movement.

### Expected Output
- At least 2 visuals with titles, legends, and readable axis labels.
- A 3-5 sentence narrative: "what changed" and "what action should happen next".

### Success Criteria
- Visuals use Level 300 baseline outputs and do not redefine risk rules.
- Narrative connects directly to VIP/Gold retention action planning.

## Extension Candidate C - Segment-Specific Threshold Testing
### Objective
Test whether different tiers should use different negative-signal thresholds while preserving baseline governance.

### What to Build
- A what-if table with candidate threshold policies (example: VIP=2, Gold=2, Silver=3, Bronze=3).
- Impact summary of how many customers change status under each policy.
- Risk note identifying tradeoffs (false positives vs missed risk).

### Expected Output
- Side-by-side comparison between baseline and each threshold policy.
- Recommendation memo that keeps baseline rule as the default for core learning comparisons.

### Success Criteria
- Analysis is clearly marked exploratory (not production policy).
- Baseline Level 300 outputs remain the core source of truth.

## Extension Candidate D - Agent Escalation Workflow
### Objective
Add optional escalation logic for severe deterioration (3+ signals) without enabling autonomous outreach.

### What to Build
- Escalation condition (`negative_signal_count >= 3`) on top of baseline triggers.
- Priority tagging (High/Medium) and routing metadata (owner/manager queue).
- Explain-only escalation message template with reason and next human action.

### Expected Output
- Test run showing at least one escalated record and one non-escalated record.
- Confirmation that no autonomous customer contact is executed.

### Success Criteria
- Escalation is additive and explain-only.
- Level 300 core learning boundary remains unaffected.

## Extension Candidate E - Offer Recommendation Playbooks
### Objective
Map risk patterns to curated offer playbooks with rationale and guardrails.

### What to Build
- A playbook matrix by risk pattern (engagement slowdown, profitability pressure, relationship narrowing, broad deterioration).
- Offer metadata: target condition, expected outcome, and exclusion guardrails.
- Human review step before any outreach recommendation is finalized.

### Expected Output
- At least 4 playbook entries tied to explicit risk patterns.
- Example recommendations for 3 customers with one-line rationale each.

### Success Criteria
- Recommendations are business-safe, human-reviewed, and traceable to signals.
- No change to baseline classification logic.

## Extension Candidate F - News Scenario Expansion
### Objective
Expand the synthetic news model so students can test richer event-behavior correlations beyond the baseline Foundry Agent 4.

### What to Build
- Extend synthetic regional news coverage from 24 months to a denser timeline (for example weekly event cadence where realistic).
- Add multiple event classes (natural disasters, major public events, supply disruptions, policy changes).
- Include fictional company impacts (for example Contoso warehouse disruption) across different regions.
- Add event windows and confidence scoring for action recommendations.

### Expected Output
- Event catalog with reproducible generation rules.
- Correlation table showing pre/post behavior changes by event window (for example 30-day pre vs post).
- Short memo on when external news should override, reinforce, or not change internal lifecycle actions.

### Success Criteria
- Expanded news logic improves decision context without replacing baseline risk logic.
- Recommendations remain explainable for business SMEs and traceable to both internal and external signals.

## Isolation and Governance Rules
- Do not replace baseline `RISK-2PLUS-NEGATIVE-SIGNALS`.
- Keep Level 300 artifacts independently completable.
- Keep extension artifacts in separate sections/files and label them `Level 400 Optional`.
- Do not require any Level 400 outcome for core learning completion.
- Topology variants and advanced orchestration experiments are allowed only as optional extensions and must not redefine Level 300’s architecture-agnostic 3-5 agent contract.
- Every extension submission must include both the technical build artifact and the Business SME readout.
