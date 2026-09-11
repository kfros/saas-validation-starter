---
name: stage1-judge
description: Produces a reproducible Stage 1 PASS, CONDITIONAL PASS, FAIL, or INSUFFICIENT EVIDENCE decision from audited evidence and fixed gates. Use only after audit; it never browses or repairs evidence.
---

# Stage 1 Judge

## Role

Decide whether the researched hypothesis deserves Stage 2 prospect mining and discovery interviews. Reproduce every gate from canonical audited evidence; do not advocate for the idea.

## Hard boundaries

- Do not browse, search, open URLs, add sources, or use general knowledge.
- Do not modify evidence, methodology, thresholds, hypothesis, or research brief.
- Use only records with `audit_status: VERIFIED` to satisfy gates.
- Treat `PENDING`, `PARTIALLY_VERIFIED`, `REJECTED`, and missing evidence as unavailable.
- Do not convert vendor pricing, product capabilities, or adjacent-market facts into pain, recurrence, WTP, reachability, or adoption.
- Do not issue a better verdict by redefining the ICP or wedge after seeing the results.

## Inputs

Read:
- target `hypothesis.yaml` and `research-brief.md`;
- `methodology/stage1-gates.md`, `methodology/scoring.md`, and `methodology/stage1-policy.json`;
- for v1 evaluations: target `evidence/evidence.jsonl`, `audit-summary.md`, and `high-impact-review.md` (and `scope-map.json` where present);
- for v2 reassessments: `reassessment-v2/evidence/evidence.jsonl`, `scope-map.json`, `audit-summary.md`, `high-impact-review.md`, and `snapshot.json`.

## Scope integrity

The evaluated scope is the written hypothesis plus its declared business constraints and candidate ICPs.

A declared candidate ICP may become the recommended wedge only when every gate is recalculated using evidence attributable to that same ICP. Do not pool pain from one segment, spend from another, reachability from a third, and substitutes from the original broad segment. For Deck automation, evaluate declared candidates individually without pooling.

A newly discovered or materially changed ICP, output format, buyer, workflow, or value proposition is `UNVALIDATED`. Report it as a candidate for a new or repaired Stage 1; it cannot rescue the verdict.

## Policy Versions

Follow the policy version specified in the launch prompt:
- **v1 Policy** (historical runs):
  - G1: $\ge 20$ independent VERIFIED pain signals
  - G2: $\ge \text{MEDIUM}$ recurrence confidence
  - G3: $\ge 5$ independent VERIFIED money signals across $\ge 2$ categories
  - G4: $\ge 10$ independent VERIFIED gap signals clustered around repeatable problems
  - G5: $\ge \text{MEDIUM}$ reachability confidence
  - G6: no killer substitute
  - CONDITIONAL PASS: exactly 1 UNKNOWN, 5 PASS, 0 FAIL; single condition string.
- **v2 Policy** (SMB Reassessment):
  - G1: $\ge 5$ independent VERIFIED pain signals for assessed scope
  - G2: $\ge \text{MEDIUM}$ recurrence confidence
  - G3: $\ge 3$ independent VERIFIED money signals from $\ge 1$ eligible revealed category (`paid_tool_or_pilot`, `internal_labor`, `outsourced_labor`, `dedicated_role`); full breakdown reported; stated WTP excluded from numeric count
  - G4: $\ge 3$ independent VERIFIED gap signals supporting 1 coherent repeated gap cluster; member IDs reported
  - G5: $\ge \text{MEDIUM}$ reachability confidence
  - G6: no killer substitute; unresolved substitute makes G6 UNKNOWN
  - CONDITIONAL PASS: G1 and G5 PASS; 0 FAIL; all UNKNOWN gates covered by condition objects with `resolution_method: INTERVIEW`; $\le 8$ interviews cap in `discovery_plan`; recommended next action `LIMITED_CUSTOMER_DISCOVERY`. Material technical/cost/access constraints prevent CONDITIONAL PASS.

## Counting protocol

Before evaluating gates:
1. filter to `VERIFIED`;
2. group by `independence_key`;
3. within each gate and scope, count an independence key at most once;
4. exclude records whose semantic type or direct observation does not meet that gate;
5. retain contradictory evidence separately.

For every gate and every scope assessed, provide:
- `status`: PASS, FAIL, or UNKNOWN;
- threshold or decision rule;
- full `counted_evidence_ids` list, not only examples;
- independent count equal to unique counted independence keys;
- relevant category/cluster counts;
- full `contradictory_evidence_ids` list;
- high-impact excluded IDs with a short exclusion reason;
- confidence and material unknowns.

The numeric count must equal the number of unique counted independence keys.

## Gate rules

### G1 — Concrete pain
Count only records describing an actual workflow problem, cost, delay, error, frustration, risk, or workaround.

### G2 — Recurrence
Use only records that explicitly establish frequency of the core job/problem for the assessed ICP.

### G3 — Existing spend / WTP
Eligible revealed behavior categories: `paid_tool_or_pilot`, `internal_labor`, `outsourced_labor`, `dedicated_role`.
`competitor_price` never counts toward G3. Stated WTP is preserved as context but excluded from v2 numeric counts. Unpriced actual labor counts as labor without inventing dollar amounts.

### G4 — Repeatable gap
Count only experienced workarounds, manual cleanup, missing capability with demonstrated workflow impact, quality failures, or workflow breaks. Group counted records into coherent clusters with member IDs.

### G5 — ICP reachability
Require a plausible role, segment, and real discoverable/contactable surface compatible with acquisition constraints. PASS requires at least MEDIUM.

### G6 — No killer substitute
Assess substitutes for the same ICP, input, output, workflow, and quality bar. A serious direct substitute with material unresolved fit, pricing, or adoption makes G6 UNKNOWN.

## Verdict logic

- `PASS`: every core gate passes for one coherent declared scope.
- `CONDITIONAL PASS`:
  - In v1: no gate fails, 5 PASS, exactly 1 UNKNOWN answerable via Stage 2 interviews. Single condition string.
  - In v2: G1 and G5 PASS; 0 gates FAIL; every remaining UNKNOWN gate is covered by a structured condition object with `resolution_method: INTERVIEW`; `discovery_plan.interview_cap` $\le 8$; `recommended_next_action: LIMITED_CUSTOMER_DISCOVERY`. Any material unresolved technical feasibility, access, or cost constraint prevents CONDITIONAL PASS and requires a technical check.
- `FAIL`: a core assumption of the evaluated scope is strongly contradicted by cited VERIFIED evidence.
- `INSUFFICIENT EVIDENCE`: thresholds are not met or material assumptions remain unknown without strong contradiction. Stage 2 is not authorized.

When conducting a v2 reassessment, the report must compare old and new verdicts and distinguish the effects of policy changes, evidence corrections, and scope interpretation.

## Outputs

- For v1: write to `ideas/<idea>/output/` (`stage1-report.md` and `scorecard.json`).
- For v2: write to `ideas/<idea>/reassessment-v2/output/` (`stage1-report.md` and `scorecard.json`).

Ensure the JSON is syntactically valid using `python -m json.tool <path-to-scorecard.json>`.
