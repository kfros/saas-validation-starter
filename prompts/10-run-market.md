# Run Market Research

First enable browser access in the Antigravity conversation with `/browser`.
Then invoke `/market-research` and provide:

```text
Run Stage 1 Market Research for `ideas/deck-automation`.

Use the hypothesis and research brief in that directory and follow all workspace validation rules.
Research only the responsibilities assigned to the Market Research skill.

Write only to:
`ideas/deck-automation/raw/market/`

Do not evaluate whether the startup should be pursued.
Do not alter the hypothesis, gates, schema, Rules, Skills, or another agent's output.
Finish only after validating that every JSONL record conforms structurally to the canonical evidence schema and uses `audit_status: PENDING`.
```
