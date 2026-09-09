# Engineering brief: audit consistency and source-review provenance

Baseline: `241d04317c5ce93ba37982b67c62fc535c7b4727`.
Target idea: `ideas/multi-brand-content`.

This brief authorizes an offline tooling repair. It is not new source evidence,
an audit decision, a raw repair or permission to advance to Stage 2.

## Problem to reproduce

The existing `scripts/check_multibrand_stage1.py audit` validates JSONL and scope
relationships but accepts audit Markdown largely by existence. The reviewed
baseline has 80 records. An independent comparison found 59 exact source-URL
differences and 51 independence-key differences between its Markdown ledger and
audited JSONL. The JSONL has 63 distinct exact URLs, the ledger has 65, and its
narrative claims 66. Reproduce the differences from repository files; these
numbers are a baseline diagnostic, not constants for future datasets.

There is also a separate source-fidelity problem. Making reports agree with an
incorrect raw quote would produce consistent but unsupported evidence. Both
problems need a solution; neither is solved by changing model or gate thresholds.

## Read first

- `scripts/check_multibrand_stage1.py` and `scripts/test_check_multibrand_stage1.py`
- `methodology/evidence-schema.json` and `methodology/evidence-standard.md`
- `ideas/multi-brand-content/research-protocol.md` and `audit-checklist.md`
- The current raw JSONL, audited JSONL, scope map and both audit Markdown files
- `ideas/multi-brand-content/repair-4041943/repair-tasks.md` for historical leads

Read existing Judge logic only as needed to preserve strict audit gating. Do not
re-run market research or modify an idea's gates/scope to resolve these defects.

## Allowed changes and preservation

Implement in `scripts/`, relevant tests, `docs/codex/`, `prompts/codex/`,
`.agents/skills/`, and new supporting review-contract files. A new sidecar schema
may live under `methodology/`; do not change `evidence-schema.json`, market
standards, scoring or gates. Update `CODEX-RUNBOOK.md` with actual working commands.

Keep all existing `ideas/` files byte-for-byte unchanged in this engineering run,
including obsolete outputs. Do not alter `.agent/`, global Codex settings or other
ideas' tooling. Temporary fixtures are the place to test rendering and migration.
Preserve and report unrelated pre-existing user edits rather than reverting them.

## Required implementation

### 1. Structured review contract

Use a small versioned JSON/JSONL sidecar; do not expand the canonical evidence
record with improvised fields. Define validation and a documented location for
future per-batch outputs. The precise field names are an implementation choice,
but represent these relationships explicitly:

- Raw ID, raw record fingerprint, and enough file/track identity to locate it.
  Define stable canonical serialization before hashing. Raw changes invalidate
  that row's review, without invalidating unrelated rows unnecessarily.
- Snapshot/manifest fingerprint for the input set and any scope/support records
  on which a review depends. Recompute these when assembling a complete audit.
- Exact requested source URL, actual resolved URL if available, source locator
  (e.g. comment permalink or page heading), and actual attributed speaker.
  Keep unknown fields null; do not generate plausible comment IDs or authors.
- Inspection time, actual retrieval tool, result/attempt identifier if exposed,
  retrieval outcome and locally preserved relevant returned fragment. Hash the
  stored fragment. A tool with no stable result ID must be described honestly,
  not assigned a fabricated external ID. A local capture ID is only a local ID.
- Field/claim-level support decisions referencing that fragment and speaker:
  quote, observation, attribution, money amount/currency/period/type, recurrence,
  role/scope and any material interpretation. Distinguish supported, contradicted,
  unknown and not-applicable, with a reason. Shared captures may support multiple
  IDs only with separate claim and speaker bindings.
- Proposed audit status/reason/key, scope decision/support IDs where applicable,
  unresolved discrepancies and an explicit raw-owner repair queue.

Generated identity/status columns come from canonical raw/consolidated data and
validated review decisions. A capture's observed speaker may disagree with the
raw author; retain that comparison explicitly. Do not "fix" it by overwriting
either field or silently changing the consolidated source fields.

No tool access means no successful inspection claim. A missing capture, unresolved
material contradiction, stale raw version or unreviewed required claim blocks
VERIFIED. A partially supported row can use the canonical PARTIALLY_VERIFIED rules.
Blocked/uninspected rows remain PENDING in a newly assembled candidate audit and
carry a blocker; retain historical decisions as history, not fresh verification.

Store only the source material needed for review with appropriate attribution;
do not archive entire sites or pull internal browser cache files. Local records
and hashes provide traceability, not independent proof a retrieval took place.

### 2. Deterministic generation

Generate the audit ledger and high-impact review from validated structured inputs.
For every displayed row, resolve raw ID, URL, author/entity, status and independence
key from the appropriate canonical data. Compute counts rather than copying prose.
All canonical source fields still must equal raw; only the auditor's three allowed
fields may differ in consolidated evidence.

Choose a documented report layout with generated sections, or generate entire
reports. If free prose is allowed, clearly separate it and do not let it duplicate
machine-owned metadata/totals as if those were authoritative. Material narrative
claims need structured references to reviewed evidence. The checker cannot detect
every unsupported sentence; document that limit rather than declaring it solved.

Generate raw-row counts, audit-status totals, distinct exact URLs, conservatively
normalized URL groups, and distinct independence keys separately. Do not call any
of these "pages opened". Actual attempt counts and distinct successfully inspected
sources must come from inspection records, with clear definitions.

The same inputs must produce the same output; use recorded timestamps rather
than wall-clock render times. Rendering must not change raw facts, promote audit
statuses on its own, or authorize Stage 2.

### 3. Consistency checker and integration

Extend the existing checker rather than leaving an optional validator that normal
`audit` / `judge` execution can bypass. A read-only diagnostic or checkpoint mode
may accept an incomplete run, but label it incomplete and never admission-ready.

The strict audit path must check:

- Schema validity, duplicate JSON keys/IDs, coverage of the current input IDs,
  review references, raw fingerprints, support dependencies and capture hashes.
- Raw/consolidated equality for protected fields; review/consolidation agreement
  on allowed audit fields; scope/support integrity and normalized-key consistency.
- Regenerated ledger/report data versus checked-in data, including exact URLs,
  authors, IDs, keys, statuses and all machine-owned totals.
- Source fragments and attributed locators supporting direct quotes. Document
  any whitespace/Unicode normalization; do not permit fuzzy or semantic matching
  to pass rewritten/composite quotes as verbatim. Nullable excerpts remain legal:
  their underlying observation still needs an inspected supporting fragment.
- Review completeness and legal status transitions. A renderer cannot bootstrap
  VERIFIED from the old Markdown or from an agent's unbacked "checked" assertion.

Diagnostics should name the raw ID, field and expected/actual relationship and
return nonzero for strict failures. Keep structural readiness, source-review
completion and market verdict distinct in CLI messages and documentation.

The unmodified 241d043 audit should fail the new strict contract because it lacks
the required review provenance and has inconsistent reports. That failure is an
expected diagnostic, not permission to silently manufacture missing reviews.
Historical diagnostic mode may explain legacy inconsistencies without requiring
the sidecar, but cannot pass the legacy data to Judge as a fresh completed audit.

### 4. Small source-review batches, prepared but not executed here

Implement batch preparation/resume and create a narrow
`.agents/skills/source-review-batch/SKILL.md` plus launch prompt after the contract
and commands work. Use the existing public-source research policy. Do not assume
that Antigravity's `/browser` exists in Codex or install a browser/MCP integration.

The initial control batch contains exactly five raw IDs:

| Raw ID | Regression to investigate from original source in the later review |
| --- | --- |
| mb-pain-001 | Ledger points to a different Reddit discussion than the canonical Canva source. |
| mb-wtp-001 | Historical review found a $120/year statement; high-impact prose claimed $300/year. Reopen and attribute it; do not treat this brief as replacement evidence. |
| mb-wtp-005 | The repaired raw quote and high-impact narrative disagree with the previously inspected switching discussion. Check each Adobe/Affinity price, purchase versus offer, speaker and billing period separately. |
| mb-wtp-008 | Canonical author is Still_Feedback1176; high-impact prose substitutes Marketing_Maven_99 and adds a 30+ hours/week claim. |
| mb-wtp-009 | Canonical author is Safe-Tell-7072; high-impact prose substitutes Creative_Solo_88 and an 8–10 hour batch estimate. Check original task-level timings, without inventing a monthly total. |

This is an error-control sample, not a representative market sample. Author and
price corrections above are review leads, not automatically verified facts.
Another purely mechanical regression is `mb-market-007`: canonical Adobe pricing
was labeled as Kontentino in the reports. Derive the original URLs from JSONL.

Prepare work in batches of at most five raw IDs, grouping shared sources when
helpful while preserving per-speaker records. Each batch must checkpoint processed,
blocked and remaining IDs. Do not fan out dozens of browser sessions. On a hard
resource/quota error use at most one permitted retry; on repeated tool failure
stop and persist partial progress. No terminal scraping, internal brain access,
invented snippets or obligation to reach a target count.

Only review known IDs in this workflow. If a source fact requires repair, produce
the raw-owner queue; audit must not silently rewrite it. A later authorized raw
repair invalidates that row's fingerprint and requires review again. Complete
the control batch before deciding whether to review the remaining records.

### 5. Meaningful tests and delivery

Use offline temporary fixtures, clearly synthetic, and test at least:

1. Mutating a ledger URL, author, ID, key, status or count produces a diagnostic.
2. A missing/duplicate review, unknown raw ID, changed raw row, changed dependency,
   altered capture or unsupported VERIFIED transition fails strict validation.
3. A quote from another speaker, a rewritten/composite quote, a missing amount or
   period in structured money support, and an unresolved material field conflict
   cannot become VERIFIED merely because Markdown was regenerated. Test the
   explicit support contract; do not pretend regex alone detects semantic truth.
4. Shared page/different speakers, multiple rows from one entity and same URL
   across tracks produce correct separate counts, without auto-deleting evidence.
5. Blocked/partial batches resume without dropping IDs, carrying stale VERIFIED
   labels or overwriting unrelated reviews. Complete strict coverage is required
   before the ordinary Judge path can accept the new audit.
6. Two renders of identical inputs match, and applying a render does not mutate
   raw files. Old market thresholds and verdict/eligibility tests still hold.

Adapt old synthetic tests to the stricter contract; do not keep a success fixture
that consists only of invented Markdown and VERIFIED JSONL without review inputs.
If an old test's expectation changes, explain which new invariant requires it.

Deliver implementation, tests, a short migration note and actual commands for:
baseline diagnostics, rendering/checking a temporary candidate, preparing the
five-ID control batch, and resuming after a blocked inspection. State which tests
ran and which legacy strict failures are expected. Run no source review or Judge
verdict in this engineering task. Do not claim the dataset has been repaired.
