# GEO / AI-search monitoring — Stage 1 starting kit

Status: **NOT STARTED / UNVALIDATED**. This directory contains instructions, not evidence.

Start with [RUNBOOK.md](RUNBOOK.md). The research scope is
[hypothesis.yaml](hypothesis.yaml), with one declared ICP: `GEO-AGENCY-01`.
The agency/reporting wedge is a working assumption for human preflight approval.

Read [research-brief.md](research-brief.md) and [research-protocol.md](research-protocol.md).
Use only the launch prompts under [prompts/geo-monitoring](../../prompts/geo-monitoring/).
The root-level older prompts target deck automation; do not use them for this run.

Reuse existing `.agent/skills/` (singular `.agent`) unchanged. Shared methodology,
thresholds, and deck evidence/results are deliberately unchanged. No Stage 2
prospect campaign, outreach, paid subscription, model experiment, or MVP is authorized.

The helper `scripts/check_geo_stage1.py` is read-only and uses Python 3.10+ stdlib.
It enforces every keyword used in the current canonical evidence schema and
rejects unsupported schema keywords instead of silently skipping them. It is not
a general-purpose JSON Schema implementation and does not verify source truth.

Expected output directories are initially empty. Researchers create their own
`evidence.jsonl`, report(s), and `run-status.json`; do not add dummy evidence.

## Files to return after the run

- `output/stage1-report.md`
- `output/scorecard.json`
- `evidence/evidence.jsonl`
- `evidence/high-impact-review.md`

Also retain `evidence/audit-summary.md`, `evidence/scope-map.json`, and all raw
track outputs for reproduction. A Judge decision is reviewed by a human before
any Stage 2 activity; Stage 1 never authorizes product development.
