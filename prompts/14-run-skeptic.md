# Run Skeptic Research

Use a fresh Local Mode conversation. High reasoning is recommended.

1. Enable `/browser`.
2. Invoke `/skeptic-research`.
3. Paste the prompt below.

```text
Try to falsify the Stage 1 hypothesis in `ideas/deck-automation`.

Read before researching:
- `ideas/deck-automation/hypothesis.yaml`
- `ideas/deck-automation/research-brief.md`
- `methodology/evidence-standard.md`
- `methodology/evidence-schema.json`
- `methodology/stage1-gates.md`

Test the written job, business constraints, and every declared candidate ICP separately. Do not rescue the hypothesis or silently redefine its ICP, output, buyer, or workflow. A newly discovered wedge may be listed only as `UNVALIDATED`; it cannot inherit evidence or a positive verdict.

Actively search for complete and near-complete substitutes, cheap bundled/manual workflows, low recurrence, low completion time, weak actual spend, users satisfied with existing solutions, failed automation attempts, low switching intent, procurement/security/data blockers, output-fidelity constraints, and technical complexity incompatible with the stated MVP.

For every serious substitute, distinguish:
1. capability for the target workflow;
2. same-ICP/input/output fit;
3. supported price, setup, procurement, and switching friction;
4. actual adoption or sufficiency evidence.

A vendor page proves only the current capability or published price it explicitly states. It does not prove adoption, satisfaction, pain, or buyer spend. Classify a substitute that materially performs the proposed job as `contradicts` or `neutral`, not `supports` merely because a market exists. Leave unresolved threats unresolved.

Use only original public pages opened through the browser. Search snippets are leads only. Do not invent weaknesses, prices, adoption, or technical limitations.

Write only to:
`ideas/deck-automation/raw/skeptic/`

Produce:
- `evidence.jsonl`
- `skeptic-case.md`, including the substitute matrix and evidence needed to rebut each major objection.

All raw records must remain `audit_status: PENDING`. Do not issue the official Stage 1 verdict.

Tool restrictions:
- Do not access Antigravity internal files, generated step files, browser cache, or paths outside the repository.
- Do not retrieve or parse web content using terminal, Python, PowerShell, curl, or an ad-hoc scraper.
- Do not run `python -c`, inline `jsonschema`, or shell parsing.
- Retry a failed research action at most once. After 3 consecutive research-tool failures, preserve credible records, document the blocker, and finish partial.

When the files are complete, run exactly this mechanical check from the repository root:
`python scripts/validate_evidence.py ideas/deck-automation/raw/skeptic/evidence.jsonl`

If it fails, repair only the reported JSONL problem and run that same command once more. If it still fails, document the structural blocker and stop.
```
