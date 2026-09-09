# Review the five-ID control batch

Use `AGENTS.md`, `.agents/skills/source-review-batch/SKILL.md`,
`ideas/multi-brand-content/research-protocol.md`,
`ideas/multi-brand-content/audit-checklist.md`, and
`docs/codex/source-review-contract.md`.

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
