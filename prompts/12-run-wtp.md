# Run WTP Research

First enable browser access with `/browser`.
Then invoke `/wtp-research` and provide:

```text
Run Stage 1 revealed willingness-to-pay research for `ideas/deck-automation`.

Prioritize actual spend and costly labor: subscriptions used for the job, employees, contractors, agencies, job postings, freelance projects, and first-hand reports of spend. Competitor pricing alone is context, not sufficient WTP evidence.

Write only to:
`ideas/deck-automation/raw/wtp/`

Do not alter methodology or another agent's output.
Do not infer salary/cost figures without sources.
If browser/web research becomes unavailable because of a rate limit, resource limit, quota error, or repeated tool failure, do not build or use ad-hoc scraping scripts as a fallback.

Preserve the credible evidence already collected, document the blocker, and finish the run as partial. The target record count is not mandatory when research tooling is unavailable.
Do not decide PASS/FAIL.
Finish only after structurally checking JSONL records against the canonical schema. All raw records must remain `PENDING`.
```
