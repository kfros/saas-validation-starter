# Run Evidence Auditor

Use a fresh Local Mode conversation with High reasoning.

1. Enable `/browser` so the Auditor can reopen recorded public URLs.
2. Invoke `/evidence-audit`.
3. Paste the prompt below.

```text
Audit the already-collected Stage 1 evidence for `ideas/deck-automation`.

Read all evidence under:
- `ideas/deck-automation/raw/market/`
- `ideas/deck-automation/raw/pain/`
- `ideas/deck-automation/raw/wtp/`
- `ideas/deck-automation/raw/workflow/`
- `ideas/deck-automation/raw/skeptic/`

Also read the target hypothesis/research brief and the canonical evidence standard, schema, and Stage 1 gates.

Hard restrictions:
- Do not conduct discovery research or search for replacement/supporting sources.
- Open only exact `source_url` values already stored in raw evidence. Open each canonical URL once and use that inspection for all records from it.
- Do not use general knowledge, search snippets, cached content, Antigravity internal files, generated step files, browser cache, terminal HTTP tools, or ad-hoc scrapers as evidence.
- Do not modify methodology, hypothesis, research brief, or raw output.
- Do not weaken or rewrite an unsupported observation merely to mark it VERIFIED.

Audit direct source support, atomicity, observation/interpretation separation, semantic type, ICP attribution, recurrence, money classification and amount, source recency, canonical URL, independence key, and duplicates.

Apply the Evidence Audit distinctions strictly:
- product feature/price is not pain;
- an absent feature without experienced user impact is not a validated gap;
- billing cadence is not workflow recurrence;
- vendor/list/agency pricing is not actual WTP;
- SaaS spend requires actual use/purchase for the job;
- a full salary/retainer cannot be allocated to the job without direct support;
- a role or association homepage alone is not reachability;
- a direct incumbent capability is substitute evidence, not automatic market support.

Set `VERIFIED`, `PARTIALLY_VERIFIED`, or `REJECTED` with a concrete reason. If Antigravity browser/tool failure prevents inspection, preserve the record as `PENDING` with the blocker; never mark it VERIFIED from cached or unopenable material. The Judge must be able to reproduce every potential gate count from the audit outputs alone.

Write only to:
`ideas/deck-automation/evidence/`

Produce:
- `evidence.jsonl`
- `audit-summary.md`
- `high-impact-review.md`

Do not issue PASS/FAIL.

After writing, run only:
- `python scripts/validate_evidence.py ideas/deck-automation/evidence/evidence.jsonl`
- `python scripts/find_duplicates.py ideas/deck-automation/evidence/evidence.jsonl`

Do not use `python -c`, inline `jsonschema`, PowerShell one-liners, or shell parsing. If validation fails, repair only the reported local JSONL problem and rerun the validator once. If it still fails, record the blocker and stop.
```
