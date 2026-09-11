# 20 — GEO Stage 1 Judge (v2)

Launch in a **fresh conversation** with **High reasoning**.
**DO NOT enable `/browser`**.
Invoke `/stage1-judge`.

Paste the prompt below into the conversation:

```text
Judge Stage 1 v2 for ideas/geo-monitoring and its declared scope GEO-AGENCY-01.

Read:
- `ideas/geo-monitoring/hypothesis.yaml`
- `ideas/geo-monitoring/research-brief.md`
- `ideas/geo-monitoring/research-protocol.md`
- `methodology/stage1-policy.json` (policy v2)
- `methodology/stage1-gates.md`
- `methodology/scoring.md`
- `ideas/geo-monitoring/reassessment-v2/evidence/evidence.jsonl`
- `ideas/geo-monitoring/reassessment-v2/evidence/scope-map.json`
- `ideas/geo-monitoring/reassessment-v2/evidence/audit-summary.md`
- `ideas/geo-monitoring/reassessment-v2/evidence/high-impact-review.md`
- `ideas/geo-monitoring/reassessment-v2/evidence/snapshot.json`
- `ideas/geo-monitoring/output/scorecard.json` (historical v1 scorecard for retrospective comparison)

Hard Restrictions:
- Do not browse, search, open URLs, add sources, or use general knowledge.
- No writes outside `ideas/geo-monitoring/reassessment-v2/output/`.
- Use only VERIFIED records from the v2 evidence snapshot.
- Treat PARTIALLY_VERIFIED, PENDING, REJECTED, and unreviewed records as unavailable.
- Deduplicate by independence_key within each gate.

Apply Policy v2 Rules:
- G1 (Concrete pain): >= 5 independent VERIFIED signals describing concrete pain/workarounds in GEO-AGENCY-01.
- G2 (Recurrence): >= MEDIUM confidence that core monitoring job recurs (e.g. monthly client reporting).
- G3 (Revealed spend / costly labor): >= 3 independent VERIFIED signals of actual spend or performed costly labor from >= 1 eligible category. Canonical evidence money_signal values are: actual_purchase, paid_pilot, saas_spend, employee_time, contractor_spend, agency_spend, dedicated_role. paid_tool_or_pilot may be described only as a normalized reporting category grouping actual_purchase, paid_pilot, and saas_spend (do not use internal_labor or outsourced_labor). Stated WTP is preserved as context but excluded from this threshold. Report full category breakdown.
- G4 (Repeatable gap): >= 3 independent VERIFIED gap signals supporting one coherent repeated gap cluster. Report cluster member IDs.
- G5 (Reachability): >= MEDIUM confidence that relevant agency buyers can be contacted through a concrete acquisition surface.
- G6 (No killer substitute): no low-friction sufficient substitute that defeats the value proposition. Unresolved substitute fit remains UNKNOWN.

Verdict Logic:
- PASS: all six gates PASS for GEO-AGENCY-01. Requires `discovery_plan` with `interview_cap` <= 8 and `recommended_next_action: LIMITED_CUSTOMER_DISCOVERY`.
- CONDITIONAL PASS: G1 and G5 must PASS; 0 gates FAIL. Every remaining material UNKNOWN gate must have an explicit condition object with `resolution_method: INTERVIEW`. Requires `discovery_plan` with `interview_cap` <= 8 and `recommended_next_action: LIMITED_CUSTOMER_DISCOVERY`. Material unresolved technical feasibility, API access, or sampling unit economics constraints prevent CONDITIONAL PASS and require a preceding TECHNICAL_CHECK.
- FAIL: strong cited contradiction of core assumptions. Insufficient evidence alone is not FAIL.
- INSUFFICIENT EVIDENCE: thresholds unmet or material assumptions remain unknown without strong contradiction.

Retrospective Verdict Comparison:
The report must explicitly compare the historical v1 verdict (INSUFFICIENT EVIDENCE) with the v2 verdict, separating the effects of:
1. Policy threshold changes (e.g. G1 threshold 20 -> 5; G3 threshold 5 -> 3);
2. Evidence corrections or newly checked sources;
3. Scope interpretation.

Produce ONLY:
- `ideas/geo-monitoring/reassessment-v2/output/stage1-report.md`
- `ideas/geo-monitoring/reassessment-v2/output/scorecard.json`

Ensure scorecard.json conforms to the v2 scorecard schema:
- `policy_version`: "v2"
- `input_commit_or_snapshot`: must equal `snapshot.json.snapshot_id` exactly, never `3bf758f`
- `recommended_next_action`: "LIMITED_CUSTOMER_DISCOVERY" | "STOP" | "TECHNICAL_CHECK_REQUIRED" | "REPAIR_RESEARCH"
- `discovery_plan`: object with `interview_cap` <= 8 (required for both PASS and CONDITIONAL PASS)
- `conditions`: list of condition objects with condition_id, gate_ids, resolution_method ("INTERVIEW"), exact_unknown, supporting_evidence_ids, respondent_qualification, observable_information_to_request, continue_criteria, stop_criteria
- complete counted and contradictory evidence IDs, G3 category breakdown, G4 clusters, dimension scores.

Terminal Allowlist:
python scripts/check_geo_stage1.py judge --policy v2

The checker strictly parses JSON and validates all policy contracts. Do not run separate python -m json.tool, ad-hoc scripts, or python -c experiments. One structural repair maximum. Do not start Stage 2 or outreach.
```
