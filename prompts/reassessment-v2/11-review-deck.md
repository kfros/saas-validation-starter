# 11 — Deck Targeted Source Review (v2)

Launch in a **fresh conversation** with **High reasoning**.
Enable `/browser` and invoke `/evidence-audit`.

Paste the prompt below into the conversation:

```text
Perform a bounded Stage 1 v2 source review for ideas/deck-automation.

Read:
- `ideas/deck-automation/hypothesis.yaml`
- `ideas/deck-automation/research-brief.md`
- `methodology/stage1-policy.json` (policy v2 rules)
- `methodology/stage1-gates.md`
- `methodology/evidence-standard.md`
- `ideas/deck-automation/evidence/evidence.jsonl` (historical baseline)
- `ideas/deck-automation/evidence/audit-summary.md`
- `ideas/deck-automation/evidence/high-impact-review.md`

Objective:
Identify the smallest decisive set of positive and contradictory records needed to assess the v2 policy thresholds (G1 >= 5, G2 >= MEDIUM, G3 >= 3, G4 >= 3, G5 >= MEDIUM, G6 no killer substitute).

Scope Discipline:
Deck retains its declared candidate segments:
- B2B SaaS account executives
- sales enablement teams
- boutique consultancies
- agencies producing client decks
- professional-services firms
- commercial real-estate teams
Assess candidate segments individually. Do not pool pain from agencies with spend from real estate and reachability from enterprise sales. Focus the review on the single declared SMB candidate with the most defensible existing coverage (e.g. boutique consultancies or agencies producing client decks) or conclude INSUFFICIENT EVIDENCE.

Targeted Review Leads (inspect public sources directly):
1. `ev-pain-faang-no-deck-workflow` and `ev-skp-infosec-procurement-hurdles`: inspect applicability to the selected SMB scope. Enterprise/FAANG evidence does not automatically establish SMB constraints.
2. Microsoft 365 Copilot records (`ev-skp-m365-copilot-ppt-features`, `ev-skp-m365-copilot-brand-templates`, `ev-skp-m365-copilot-pricing`): inspect actual custom corporate template capability and output quality before concluding same-job sufficiency.
3. Reassess core recurrence and discoverable reachability for the chosen SMB candidate segment. Absence of enough public forum posts is not strong contradiction.
4. Stated WTP vs costly labor: preserve stated WTP as context, but verify actual employee/contractor labor spent adapting decks for G3.

Inspection Protocol:
- Open original public URLs in small batches of at most 5 records.
- Do not inherit old audit statuses without re-review.
- On HTTP 429, quota exhaustion, or inaccessible sources: allow at most one ordinary retry. Record inaccessible pages as blocked. Stop after 3 consecutive failures. No ad-hoc web scrapers.
- Ordinary read-only access to repository files is allowed.

Write ONLY to:
`ideas/deck-automation/reassessment-v2/evidence/`

Produce all required snapshot files:
1. `evidence.jsonl`: canonical audited records with direct quotes and audit reasons.
2. `scope-map.json`: scope attribution mapping for the assessed candidate segment.
3. `review-log.jsonl`: line-by-line inspection log of checked URLs, timestamps, and findings.
4. `audit-summary.md`: narrative audit summary detailing reviewed vs unexamined records.
5. `high-impact-review.md`: documentation of excluded, unexamined, or contradictory records.
6. `snapshot.json`: generated/sealed machine-readable snapshot manifest via `scripts/seal_v2_snapshot.py`.

Terminal Allowlist:
python scripts/seal_v2_snapshot.py --idea deck-automation --snapshot-id snap-deck-v2-001
python scripts/check_deck_stage1.py audit --policy v2

No python -c experiments or helper scripts. When checks pass, report reviewed IDs, unexamined budget, blockers, and stop. Do not proceed to Judge in this conversation.
```
