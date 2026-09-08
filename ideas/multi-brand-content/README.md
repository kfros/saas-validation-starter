# Multi-brand content production — Stage 1 starting kit

Initial state: NOT STARTED / UNVALIDATED. This kit contains instructions only.
The launch of this run uses the working scope in [hypothesis.yaml](hypothesis.yaml).

Start with [RUNBOOK.md](RUNBOOK.md). Read [research-brief.md](research-brief.md),
[research-protocol.md](research-protocol.md) and [audit-checklist.md](audit-checklist.md).
Use only [prompts/multi-brand-content](../../prompts/multi-brand-content/).

Scope: owner-led external SMM providers doing recurring production and revisions
for multiple SMB client brands. Freelancers and small agencies are included because
of the same owner/operator job, not assumed interchangeable because of their labels.
The Judge must expose differences in workflow, buying behavior and coverage.

Use the seven existing skills under `.agent/skills/` unchanged (singular `.agent`).
Root prompts target deck automation; GEO prompts target GEO. Neither is a launcher
for this idea. Shared methodology and previous evidence remain the historical baseline.

The additional read-only checker is `scripts/check_multibrand_stage1.py`.
It needs Python 3.10+ standard library, with no package installation or network.
It checks the current canonical schema keyword subset and rejects unsupported
future keywords. It does not verify source truth or decide commercial merit.

Output folders start empty. No copied GEO/deck records, dummy evidence or sample
PASS report are included. Research does not authorize outreach, payments, product
development or changes to ChillPup.

Return the commit SHA and these four paths after the run:

- `output/stage1-report.md`
- `output/scorecard.json`
- `evidence/evidence.jsonl`
- `evidence/high-impact-review.md`

Retain the raw files, run statuses, audit-summary.md and scope-map.json alongside
them so the verdict can be reproduced and independently reviewed.
