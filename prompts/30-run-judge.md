# Run Stage 1 Judge

Use a fresh Local Mode conversation with High reasoning. Do not enable `/browser`.

1. Invoke `/stage1-judge`.
2. Paste the prompt below.

```text
Judge Stage 1 for `ideas/deck-automation` using only audited evidence in its `evidence` directory.

Read:
- `ideas/deck-automation/hypothesis.yaml`
- `ideas/deck-automation/research-brief.md`
- `methodology/stage1-gates.md`
- `methodology/scoring.md`
- `ideas/deck-automation/evidence/evidence.jsonl`
- `ideas/deck-automation/evidence/audit-summary.md`
- `ideas/deck-automation/evidence/high-impact-review.md`

Hard restrictions:
- Do not browse, search, open URLs, add sources, or use general knowledge.
- Do not change evidence, methodology, thresholds, hypothesis, or research brief.
- Use only `audit_status: VERIFIED` records to satisfy gates.
- Treat PARTIALLY_VERIFIED, PENDING, REJECTED, and missing evidence as unavailable.
- Deduplicate by `independence_key` within each gate and assessed scope.
- Do not convert product features, competitor pricing, generic workflow, or adjacent-market facts into pain, recurrence, WTP, reachability, or adoption.

Evaluate the written hypothesis and each declared candidate ICP without pooling unrelated segments. A candidate ICP may be recommended only if all six gates are recalculated on evidence attributable to that same ICP. Any materially new ICP, buyer, output, workflow, or wedge is `UNVALIDATED` and cannot rescue the verdict.

For every gate include:
- PASS, FAIL, or UNKNOWN;
- threshold/decision rule;
- complete `counted_evidence_ids`, not only strongest examples;
- count equal to unique counted independence keys;
- category/cluster breakdown where applicable;
- complete contradictory evidence IDs;
- high-impact excluded IDs and reasons;
- confidence and material unknowns.

Gate discipline:
- G1 counts only experienced concrete pain/workaround.
- G2 uses only explicit recurrence of the core job/problem.
- G3 never counts `competitor_price`; vendor/agency rate cards, marketplace averages, salary aggregates, broad retainers, vendor revenue, and incidental job duties do not qualify as revealed WTP.
- G4 counts only experienced repeatable gaps/workarounds with workflow impact and coherent clusters.
- G5 requires role + segment + a real discoverable/contactable surface compatible with acquisition constraints.
- G6 evaluates direct substitutes for the same ICP/input/output/workflow; a serious unresolved substitute makes G6 UNKNOWN, not PASS.

Use exactly one final verdict:
- PASS only when every gate passes for one coherent declared scope;
- CONDITIONAL PASS only when no gate fails and exactly one material gate-level question remains UNKNOWN and is realistically answerable in Stage 2;
- FAIL when a core assumption is strongly contradicted;
- INSUFFICIENT EVIDENCE when thresholds are unmet or several material assumptions remain unknown.

A failed broad scope plus an under-evidenced narrower candidate is not CONDITIONAL PASS. Explicitly state whether Stage 2 is authorized.

Write only to:
`ideas/deck-automation/output/`

Produce:
- `stage1-report.md`
- `scorecard.json`

The scorecard must contain reproducible counted ID lists, scope-integrity notes, candidate-scope assessments, `stage2_authorized`, and at most one explicit condition.

Validate JSON syntax only with:
`python -m json.tool ideas/deck-automation/output/scorecard.json`

Do not use `python -c` or inline parsing. If validation fails, repair the JSON and run that same command once more.
```
