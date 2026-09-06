# Run Stage 1 Judge

Do NOT enable browser access for this conversation.
Invoke `/stage1-judge` and provide:

```text
Judge Stage 1 for `ideas/deck-automation` using only VERIFIED evidence in its audited evidence directory.

Hard restrictions:
- Do not browse.
- Do not search.
- Do not add sources.
- Do not use general knowledge to fill gaps.
- Do not use PARTIALLY_VERIFIED, PENDING, or REJECTED evidence to satisfy gates.
- Deduplicate by `independence_key` before counting thresholds.
- Do not modify the predefined gate thresholds.
- Missing evidence must remain UNKNOWN.

Write only to:
`ideas/deck-automation/output/`

Produce:
- stage1-report.md
- scorecard.json

Use exactly one final verdict:
PASS, CONDITIONAL PASS, FAIL, or INSUFFICIENT EVIDENCE.
```
