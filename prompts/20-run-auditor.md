# Run Evidence Auditor

Browser is not needed for discovery. The Auditor may open only URLs already present in raw evidence for verification.
Invoke `/evidence-audit` and provide:

```text
Audit the already-collected Stage 1 evidence for `ideas/deck-automation`.

Read all evidence under:
- raw/market
- raw/pain
- raw/wtp
- raw/workflow
- raw/skeptic

Hard restriction:
Do NOT conduct new market research.
Do NOT search for replacement or supporting sources.
Do NOT repair weak evidence.
You may open only source URLs already stored in the raw evidence records to verify those records.

Deduplicate by underlying source/claim and `independence_key`.
Apply VERIFIED, PARTIALLY_VERIFIED, or REJECTED strictly according to the Evidence Audit skill.

Write only to:
`ideas/deck-automation/evidence/`

Produce the canonical audited evidence, audit summary, and high-impact human review file.
Do not issue PASS/FAIL.
```
