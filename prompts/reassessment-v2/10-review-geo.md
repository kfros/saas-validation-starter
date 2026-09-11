# 10 — GEO Targeted Source Review (v2)

Launch in a **fresh conversation** with **High reasoning**.
Enable `/browser` and invoke `/evidence-audit`.

Paste the prompt below into the conversation:

```text
Perform a bounded Stage 1 v2 source review for ideas/geo-monitoring and its declared scope GEO-AGENCY-01.

Read:
- `ideas/geo-monitoring/hypothesis.yaml`
- `ideas/geo-monitoring/research-brief.md`
- `ideas/geo-monitoring/research-protocol.md`
- `methodology/stage1-policy.json` (policy v2 rules)
- `methodology/stage1-gates.md`
- `methodology/evidence-standard.md`
- `ideas/geo-monitoring/evidence/evidence.jsonl` (historical baseline)
- `ideas/geo-monitoring/evidence/scope-map.json`
- `ideas/geo-monitoring/evidence/high-impact-review.md`

Objective:
Identify the smallest decisive set of positive and contradictory records needed to assess the v2 policy thresholds (G1 >= 5, G2 >= MEDIUM, G3 >= 3, G4 >= 3, G5 >= MEDIUM, G6 no killer substitute). Do not reopen the entire corpus by default. Use a bounded review budget.

Targeted Review Leads (inspect public sources directly):
1. `geo-pain-reddit-arash60-defensive-monthly-client-reporting` — distinguish recurring tool use from proven payment.
2. `geo-wtp-blog-agency-manual-hours` — distinguish vendor marketing arithmetic from observed actual agency labor.
3. `geo-workflow-12-manual-workaround-labor` — distinguish counterfactual labor estimates from work actually performed.
4. Scope verification: confirm independent agency size (2–20 staff serving SMB clients on recurring retainers). Solo consultants and direct SMB brand owners do not silently join GEO-AGENCY-01.
5. Substitutes & technical constraints: reassess SE Ranking, Semrush, Otterly.ai, Peec AI, stochastic sampling costs (n=7), and ToS/scraping risks without assuming previous audit labels are automatically correct.

Inspection Protocol:
- Open original public URLs using browser in small batches of at most 5 records.
- Do not inherit old VERIFIED labels as fresh verification. A matching quote/hash proves local relationship, not that browser retrieval was performed or that interpretation is sound.
- If a source is inaccessible: allow at most one ordinary retry. On HTTP 429 / quota limit / block: record the record as unverified/blocked in snapshot.json. Do not build ad-hoc web scrapers or browser replacements. Stop after 3 consecutive failures.
- Ordinary read-only access to repository files is allowed.

Write ONLY to:
`ideas/geo-monitoring/reassessment-v2/evidence/`

Produce all required snapshot files:
1. `evidence.jsonl`: canonical audited records with direct source quotes and audit reasons.
2. `scope-map.json`: scope attribution mapping for GEO-AGENCY-01 with verified support links.
3. `review-log.jsonl`: line-by-line inspection log of checked URLs, status, timestamps, and findings.
4. `audit-summary.md`: narrative audit summary detailing reviewed vs unexamined records and budget coverage.
5. `high-impact-review.md`: documentation of excluded, unexamined, or contradictory records.
6. `snapshot.json`: generated/sealed machine-readable snapshot manifest via `scripts/seal_v2_snapshot.py`.

Terminal Allowlist:
python scripts/seal_v2_snapshot.py --idea geo-monitoring --snapshot-id snap-geo-v2-001
python scripts/check_geo_stage1.py audit --policy v2

No python -c experiments or helper scripts. When checks pass, report reviewed IDs, unexamined budget, blockers, and stop. Do not proceed to Judge in this conversation.
```
