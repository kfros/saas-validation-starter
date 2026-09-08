# GEO Stage 1 Judge

Fresh High-reasoning conversation. **No `/browser`**. Invoke `/stage1-judge`, paste:

```text
Judge Stage 1 for ideas/geo-monitoring and its single declared scope GEO-AGENCY-01.
Read the stage1-judge skill; target hypothesis.yaml, research-brief.md, research-protocol.md; methodology/stage1-gates.md and scoring.md; and target evidence/evidence.jsonl, audit-summary.md, high-impact-review.md, scope-map.json.

Run the audit checker below before judging. On structural/provenance errors stop and return them to the Auditor; do not repair evidence. A checker success is not verification of source truth or scope-link correctness.

No browsing, search, opening URLs, new sources, general-knowledge gap filling, or reading internal Antigravity/cache files. No writes outside ideas/geo-monitoring/output/. Do not alter evidence, scopes, methodology or thresholds.

Only VERIFIED evidence can support gates. G1-G5 counted evidence must be IN_SCOPE in the audited scope-map; inspect the stated linkage, not just the label. Use direct observations rather than treating interpretation as fact. Count one independence key per gate. A concrete experienced workaround can be relevant across gates, never independent twice within a gate. G3 excludes competitor prices, broad SEO/content retainers, uncommitted budgets and stated WTP from revealed counts. Low actual prices are not censored. All G1-G6 rules and exact scorecard fields are in research-protocol.md; keep the canonical numeric thresholds unchanged.

Separate substitute capability, exact-job/ICP fit, price/friction and observed sufficiency. Do not declare monopoly or universal sufficiency from official features. A serious unresolved substitute is UNKNOWN, not automatic FAIL or PASS. Evaluate measurement validity, sampling costs and authorized data access as material uncertainties where evidence warrants; do not hide several technical and commercial unknowns inside one interview question. Lack of data is not proof of lack of a market.

Produce only:
- ideas/geo-monitoring/output/stage1-report.md
- ideas/geo-monitoring/output/scorecard.json

Use the scorecard contract in research-protocol.md (gates object G1..G6, evaluated_scope.scope_id, complete counted/contradictory IDs, unique counts, confidence/unknowns/exclusions, G3 category breakdown, G4 clusters, dimension scores, evidence-backed rationale, candidate-scope assessments). Report INSUFFICIENT EVIDENCE when thresholds are unmet without strong contradiction. FAIL needs strong contradictory evidence, not just sparse research. PASS needs all six gates PASS. CONDITIONAL PASS needs exactly one genuinely interview-answerable UNKNOWN and five PASS; no failed gate. stage2_authorized is the Judge's recommendation, not execution permission. Any other ICP or content-generation product is UNVALIDATED and cannot rescue this run.

For this run the exact terminal allowlist REPLACES older skill commands:
python scripts/check_geo_stage1.py audit
python scripts/check_geo_stage1.py judge

No python -c, inline parsing, shell scripts, package installs or new helper scripts. One repair of your own scorecard structure and one rerun maximum. If checking remains blocked, say so and do not claim a completed validated handoff. End with verdict, main reasons, unknowns, validation result and the four handoff paths. Do not start Stage 2 or development.
```
