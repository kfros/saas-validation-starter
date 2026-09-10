# Review or resume one prepared source-review batch

## Bind this launch

The user supplies one concrete repository-relative `BATCH_DIR`, for example
`work/source-review/wtp-02`. It must name an already prepared directory under
`work/source-review/`, without `..`, a wildcard or a shell expression. This is a
literal prompt parameter, not a PowerShell variable. Substitute that exact path
for `<BATCH_DIR>` in the command below before executing it.

Review only this batch, with at most five known raw IDs. If the path or required
manifest/state is missing, report the missing preparation and stop. Do not choose
a different batch, prepare/reset this one, or begin another batch automatically.

## Read the contract and saved progress

Read these repository files:

- `AGENTS.md`
- `.agents/skills/source-review-batch/SKILL.md`
- `docs/codex/source-review-contract.md`
- `methodology/source-review-schema.json`
- `methodology/evidence-schema.json`
- `ideas/multi-brand-content/hypothesis.yaml`
- `ideas/multi-brand-content/research-protocol.md`
- `ideas/multi-brand-content/audit-checklist.md`
- This launch prompt.
- The selected directory's `batch-manifest.json`, `batch-state.json`,
  `captures.jsonl` and `reviews.jsonl`.

Use the manifest's generated raw records, fingerprints, required claim fields,
canonical authors/entities and exact URL groups. Their content is the claim to
test, not source proof. Existing reports and historical VERIFIED labels do not
establish what a source says.

Preserve every checkpointed completed review and its captures exactly. Resume
only blocked/remaining IDs from the saved state. If the entire batch is already
processed, report that fact and finish without reopening or rewriting it. A new
semantic review of a completed ID belongs in a separately prepared revision
batch; do not edit the sealed review to make this run pass.

## Narrow operational override

For this launch, the bound `BATCH_DIR` and the bound checkpoint command below
explicitly replace the old protocol's Auditor write-directory and terminal
allowlist. They do not change source standards, scope, market gates or roles.

- Write only `captures.jsonl`, `reviews.jsonl` and checkpoint-managed
  `batch-state.json` inside the selected directory. Keep its manifest unchanged.
- Local file-reading tools may read the inputs listed above. In the terminal,
  allow only read-only `Get-Content -LiteralPath <path>` for those exact inputs
  and the bound checkpoint command below. No additional shell expressions,
  pipelines or terminal commands. The checkpoint may read canonical raw and its
  dependencies internally; that does not authorize terminal research.
- Open only exact public source URLs listed in the manifest through an
  authorized browser/public-source retrieval tool. Inspect the relevant post and
  speaker's comments; record any actual redirect. No discovery/search, terminal
  HTTP clients, scrapers, Antigravity brain/cache, outreach or invented captures.
- No raw edits, final evidence writes, rendering, consolidation, Judge, tool or
  skill changes in this run. Do not run the old phase checker.

## Source review

1. Inspect each unfinished ID against its exact original public source. A shared
   URL may serve several IDs, but preserve each speaker and raw-ID binding. Save
   the actual small relevant returned fragments and locators, honest timestamps,
   tool/result IDs when exposed, and unique local attempt IDs. Unknown tool
   metadata stays null; a locally invented ID is never an external result ID.
2. Use the v1 schema to decide every required claim at its original strength:
   quote, author, observation, interpretation, recurrence, money and role/scope.
   Bind decisions to the capture and actual speaker. An accurate paraphrase may
   support an observation but cannot pass exact quote containment. Absence of
   evidence is UNKNOWN; distinguish it from a direct contradiction or an excerpt
   that is absent from the inspected source. Neither can receive VERIFIED when
   material and unresolved.
3. For monetary evidence, separate firsthand spending/use, paid labor, adoption,
   intention and advertised prices. A firsthand spending report does not require
   an invoice or an exact amount to be evidence. Conversely, signup alone does
   not establish a charged amount. Preserve supported ownership/use/switching
   facts even when payment, currency or amount is unknown. Do not invent an
   hourly rate, payment period, monthly total or units for output counts.
4. Assess all five scope requirements from `hypothesis.yaml`. Separate the
   speaker's role, the provider's characteristics and buying authority. Employee
   testimony can establish paid labor without establishing owner-led provider
   fit; an agency label cannot establish all scope requirements. Unknown fit is
   not proof of exclusion. Preserve supported contrary facts too.
5. Fill money/impact/substitute assessments as required by the schema and record
   a concrete gate exclusion when appropriate. `substitute_assessment` is null
   for non-substitute rows. Do not promote an interpretation or gate eligibility
   merely because a checkpoint accepts its structure.
6. Record material raw/source discrepancies and raw-owner actions without
   changing raw. Exact nested keys:
   - discrepancy: `field`, `raw_value`, `observed_value`, boolean `material`,
     `reason`;
   - raw-owner repair: `field`, `observed_value`, `reason`.
   Put the requested action in `reason`, never an extra `action` key. Keep the
   actual raw value and supported observation/unknown distinct. A summarized
   observed value is not automatically a replacement exact quote.
7. Checkpoint after each completed or blocked record using the command below.

```powershell
& 'C:\Users\acer\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/audit_review_pipeline.py checkpoint-batch --state-dir <BATCH_DIR>
```

For `BATCH_DIR = work/source-review/wtp-02`, the only checkpoint is:

```powershell
& 'C:\Users\acer\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/audit_review_pipeline.py checkpoint-batch --state-dir work/source-review/wtp-02
```

The example does not authorize touching `wtp-02` when another directory is bound.
If this runtime is unavailable, report the blocker; do not change runtime paths
or repair infrastructure inside the research run.

## Stop and resume honestly

For quota/resource exhaustion, make at most one permitted retry. If it repeats,
checkpoint truthful BLOCKED/PENDING state and stop PARTIAL. Stop after three
consecutive tool failures. Uninspected monetary rows may keep money facts null,
payment/transaction UNKNOWN and money decisions UNKNOWN; lack of access does not
justify an invented discrepancy or REJECTED status.

On a checkpoint structural failure, read the full diagnostic and make at most
one structural repair to unfinished records, then one rerun. Never invent facts
or change completed reviews/fingerprint guards to satisfy it. If it still fails,
preserve the sidecars and report the exact error; the failed record is unsealed.

Finish with the selected directory, checkpoint result, processed/blocked/remaining
IDs, source links, material discrepancies and raw-owner actions. Say explicitly
that batch completion is not full-audit completion or a market verdict. Stop
after this batch. Do not automatically run Judge or require every row to become
VERIFIED.
