# Review the five-ID control batch

Use `AGENTS.md`, `.agents/skills/source-review-batch/SKILL.md`,
`ideas/multi-brand-content/research-protocol.md`,
`ideas/multi-brand-content/audit-checklist.md`, and
`docs/codex/source-review-contract.md`.

## Narrow operational override

For this prepared source-review workflow, this prompt overrides exactly two
operational clauses of the older idea protocol:

1. Write only batch artifacts under `work/source-review/control-01/`, not the
   final `ideas/multi-brand-content/evidence/` outputs.
2. Terminal use is limited to the exact `checkpoint-batch` command below and
   read-only local input inspection via `Get-Content -LiteralPath <path>`.
   Approved paths are `AGENTS.md`, `.agents/skills/source-review-batch/SKILL.md`,
   `docs/codex/source-review-contract.md`, `methodology/source-review-schema.json`,
   this launch prompt, the target idea's `hypothesis.yaml`, `research-protocol.md`
   and `audit-checklist.md`, and the prepared batch manifest/state/captures/reviews.
   Prefer a local file-reading tool when available. No shell expressions,
   pipelines, network reads or other paths are authorized by this read exception.
   The human runs `prepare-batch` before the review. Do not run the old phase
   checker during this batch.

Every other protocol restriction remains in force: known exact URLs only,
authorized public browser/retrieval tools, no terminal research/scraping, no new
search/discovery, no outreach, one permitted quota retry, and partial checkpoint
on repeated failure. This override does not authorize edits to raw evidence,
final audit outputs, source-review tooling, market gates or Judge outputs.

The human first prepares exactly these known IDs:

```powershell
& 'C:\Users\acer\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/audit_review_pipeline.py prepare-batch --state-dir work/source-review/control-01 --ids mb-pain-001 mb-wtp-001 mb-wtp-005 mb-wtp-008 mb-wtp-009
```

Read `work/source-review/control-01/batch-manifest.json`. Inspect only its exact
source URLs with an authorized public-source browser/retrieval tool. Do not treat
the following as facts: they are regression questions to resolve from the actual
source.

- `mb-pain-001`: whether the historical ledger pointed to a different discussion.
- `mb-wtp-001`: exact $120/$300 statements, speaker and periods.
- `mb-wtp-005`: each Adobe/Affinity price, purchase versus offer, speaker, period.
- `mb-wtp-008`: canonical versus observed author and the alleged 30+ hours/week.
- `mb-wtp-009`: canonical versus observed author and task-level timing without a
  constructed monthly total.

Write valid v1 `captures.jsonl` and `reviews.jsonl` in that state directory.
Read the exact issue-object definitions and example in the contract before
writing `discrepancies` or `raw_owner_repairs`. The repair array needs
`field`, `observed_value`, `reason`; requested actions go in `reason`, never an
extra `action` field. The discrepancy array also needs `raw_value` and the
boolean `material`. Use the diagnostic's full path/missing/unexpected-key list.
Use each manifest row's generated `raw_record`, `raw_fingerprint` and
`required_claim_fields`; do not invent fragments, authors, result IDs or
successful outcomes. Material source/raw differences must be represented both as
discrepancies and raw-owner repair actions. The checkpoint command seals only
deterministic raw/dependency/fragment hashes after confirming that the selected
raw snapshot is unchanged; it never supplies semantic decisions or capture text.

Checkpoint after each completed or blocked record:

```powershell
& 'C:\Users\acer\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/audit_review_pipeline.py checkpoint-batch --state-dir work/source-review/control-01
```

If interrupted, read `batch-state.json` and resume only its blocked/remaining IDs;
never discard completed rows. A repeated quota/resource failure ends the batch
PARTIAL after one permitted retry. Do not run final audit rendering or Judge.
