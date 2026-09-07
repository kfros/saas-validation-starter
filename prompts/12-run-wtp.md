# Run WTP Research

Use a fresh Local Mode conversation. High reasoning is recommended.

1. Enable `/browser`.
2. Invoke `/wtp-research`.
3. Paste the prompt below.

```text
Run Stage 1 revealed willingness-to-pay research for `ideas/deck-automation`.

Read before researching:
- `ideas/deck-automation/hypothesis.yaml`
- `ideas/deck-automation/research-brief.md`
- `methodology/evidence-standard.md`
- `methodology/evidence-schema.json`
- `methodology/stage1-gates.md`

Keep the written job and declared candidate ICPs fixed. Assess spend for each ICP separately. Do not combine money from agencies, consultancies, CRE, proposal teams, and B2B SaaS sales unless the source actually applies to the same assessed scope.

Prioritize buyer-side actual purchases, paid pilots, actual contractor/agency engagements, explicit buyer budgets, paid employee time materially spent on the job, dedicated roles, and first-hand actual use of paid SaaS for this job.

Competitor pricing, vendor/agency rate cards, marketplace averages, salary aggregators, broad creative retainers, vendor revenue, and unawarded listings are context—not revealed WTP. Do not count them as actual spend. Never encode hours as currency or allocate an entire salary/retainer to deck work without direct source support.

Use only original public pages opened through the browser. Search snippets are leads only. Every record must be atomic and must separate observation from interpretation. Do not infer buyer, ICP, adoption, recurrence, amount, currency, period, or purchase.

Write only to:
`ideas/deck-automation/raw/wtp/`

Produce:
- `evidence.jsonl`
- `wtp-map.md`

All raw records must remain `audit_status: PENDING`. Do not decide any gate or PASS/FAIL verdict.

Tool restrictions:
- Do not access Antigravity internal files, generated step files, browser cache, or paths outside the repository.
- Do not retrieve or parse web content using terminal, Python, PowerShell, curl, or an ad-hoc scraper.
- Do not run `python -c`, inline `jsonschema`, or shell parsing.
- If browser research fails, retry the failed research action at most once. After 3 consecutive research-tool failures, preserve credible records, document the blocker and missing spend categories in `wtp-map.md`, and finish partial.

When the files are complete, run exactly this mechanical check from the repository root:
`python scripts/validate_evidence.py ideas/deck-automation/raw/wtp/evidence.jsonl`

If it fails, repair only the reported JSONL problem and run that same command once more. If it still fails, document the structural blocker and stop. The target record count is not mandatory.
```
