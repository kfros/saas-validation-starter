# Resume the control batch after structural recovery

Read `AGENTS.md`, `.agents/skills/source-review-batch/SKILL.md`,
`docs/codex/source-review-contract.md`, `docs/codex/control-recovery-249030f.md`,
`methodology/source-review-schema.json`, and the target idea's `hypothesis.yaml`,
`research-protocol.md`, and `audit-checklist.md`.

## Exact task boundaries

This prompt replaces the initial control-batch launch for this recovery only.
Two batches are already prepared. Write only inside:

- `work/source-review/control-01-scope-recheck/`: new review of `mb-pain-001`.
- `work/source-review/control-01/`: remaining `mb-wtp-005`, `mb-wtp-008`, `mb-wtp-009`.

Read each manifest/state before acting. Preserve every completed review/capture
in the original batch exactly; in particular do not rewrite completed pain or
WTP-001, remove fingerprint guards, or re-prepare/reset a batch. The separate
pain review is a revision requiring later resolution, never a sixth evidence row.

As a narrow override of the old protocol, read-only `Get-Content -LiteralPath
<path>` is allowed for the instruction/contract files named above, this launch
prompt and the manifest/state/captures/reviews in these two directories. Prefer
an available file-reading tool. No other paths, shell expressions/pipelines,
network access through the terminal or additional terminal commands are allowed
apart from the two exact checkpoints below. This overrides only local input
reading, batch output paths and checkpoint commands; retain the public-source,
no-new-discovery, retry and partial-run restrictions.

Use only original public URLs in the manifests with an authorized public-source
retrieval tool. No terminal scraping, internal brain/cache files, fabricated tool
IDs, conversation-only findings promoted to captures, outreach or raw edits.

## Work sequence

1. Inspect `mb-pain-001` in the separate scope-recheck batch. Reopen the original
   page. For each scope requirement state what the source establishes and what
   remains unknown: external service, multiple unrelated brands, recurring static
   production/revision, owner-led hands-on work, SMB clientele. A designer/agency
   label and five clients do not establish the remaining attributes. Recheck the
   scope and gate eligibility independently from the useful broad pain observation.
   Never infer recurring production from a per-client permissions setup question.
2. Finish only the three remaining WTP IDs in the original batch. Previous prose
   about their findings is a lead; no retained captures for them were present in
   249030f. Inspect and preserve each source fragment and speaker now. Focus on
   direct quote fidelity, amount/period/transaction, role and scope. Distinguish
   statics counts from hours, task times from invented monthly totals, and an
   offer/list price from an actual purchase.
3. Checkpoint after each completed or blocked record using the applicable command.

```powershell
& 'C:\Users\acer\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/audit_review_pipeline.py checkpoint-batch --state-dir work/source-review/control-01-scope-recheck
```

```powershell
& 'C:\Users\acer\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/audit_review_pipeline.py checkpoint-batch --state-dir work/source-review/control-01
```

Before writing any issues, use the exact nested definitions in the sidecar schema:
discrepancies need `field`, `raw_value`, `observed_value`, boolean `material`,
`reason`; raw-owner repairs need `field`, `observed_value`, `reason`. Put the
requested action in `reason`, not an extra `action` key. Unknown stays unknown.
Use the full diagnostic to repair all listed structural issues in the permitted
repair attempt. Do not infer a replacement observed value merely to satisfy shape.

If tools fail, preserve a truthful BLOCKED/PENDING record and stop as required by
the protocol. Uninspected monetary rows can keep all money facts null and all
money decisions UNKNOWN without an invented discrepancy. One structural repair
and one rerun remain the limit; if still failing, preserve the files and error.

Finish with separate processed/blocked/remaining lists for both batches, source
inspection results, known discrepancies and raw-owner actions. Stop after these
four reviews. No final rendering, canonical consolidation, raw repair or Judge.
