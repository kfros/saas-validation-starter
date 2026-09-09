# Codex instructions for saas-validation-starter

This repository validates product hypotheses. Market conclusions must be traceable
to source evidence; successful code checks do not validate a market.

## Select the task before acting

- **Engineering/setup:** when asked to build or repair tooling, work on the
  relevant scripts, tests, supporting contracts, documentation and Codex skills.
  Local parsing, rendering and offline tests are part of that task. A research
  launch prompt's terminal/write allowlist governs that research run, not a
  separately requested engineering task. Respect the current task's boundaries.
- **Research/repair:** follow the selected idea's protocol and launch prompt.
  Preserve stable raw IDs and PENDING status. Correct source-dependent fields
  only after inspecting the original source and only within the owned track.
- **Audit:** follow the audit contract. Do not silently repair raw source fields.
  Audit status, reason and independence-key normalization are distinct from
  source repair. An inaccessible source does not receive fresh VERIFIED status.
- **Judge:** use eligible audited evidence and the existing gates. Do not browse,
  backfill evidence or silently broaden the hypothesis to improve a verdict.

Do not advance to another role/stage merely because the current task finished.

## Shared authority and repository map

Read the files relevant to the selected task, especially:

- `methodology/evidence-schema.json`, `evidence-standard.md`, `stage1-gates.md`
  and `scoring.md`: shared evidence and decision rules.
- `ideas/<idea>/hypothesis.yaml`, `research-protocol.md`, `audit-checklist.md`:
  idea-specific scope and execution contract.
- `ideas/<idea>/raw/`: researcher-owned observations, always PENDING.
- `ideas/<idea>/evidence/`: audited consolidation and scope decisions.
- `ideas/<idea>/output/`: Judge outputs; not primary evidence.
- `scripts/`: local deterministic checks and tests.
- `.agent/`: existing Antigravity instructions; preserve this singular path.
- `.agents/skills/` and `prompts/codex/`: Codex workflows and launch tasks.

The methodology is shared across tools. Do not change thresholds, scope, verdict
rules or evidence eligibility unless the user explicitly asks for that change.
Historical reports and repair briefs are leads for inspection, not proof that a
source says something. Do not inherit their VERIFIED labels without the required
review. UNKNOWN, partial coverage and a blocked run are valid outcomes.

## Evidence fidelity

Keep observation separate from interpretation, prices from actual spending, and
speaker identity from inferred buyer authority. Do not merge different speakers'
claims, infer billing periods, convert client counts into headcount, or promote
adjacent work into the target job. Record supported contrary facts too.

Generate repeated metadata and totals from structured canonical data. Review
records must identify the raw ID/version, exact source, attributed speaker and
actually retrieved fragment. A matching quote/hash proves a local relationship,
not that a browser was used or that the interpretation is justified.

Use only authorized tools to inspect original public sources. Do not access
Antigravity's `.gemini/antigravity/brain`, internal browser artifacts or caches.
Do not replace failed research tools with ad-hoc scrapers. Follow the selected
research protocol's retry/partial-run rules. Do not perform outreach unless asked.

## Engineering execution

Inspect the worktree before editing; preserve unrelated user changes. Prefer
tracked Python script files and their documented CLI over repeated multiline
`python -c` quoting experiments. Python is allowed for authorized local processing
and tests; it is not an implicit permission to scrape public sources.

Keep synthetic test records in temporary fixtures, never in idea evidence. Test
material invariants and known failure cases. Report the commands actually run,
their results and remaining limits. A structural success must not be described
as source verification or PASS of a product hypothesis.

Communicate with the user in Russian. Follow the existing artifact language and
schema enums when editing repository files. Keep project-specific configuration
in this repository; do not modify the user's global Codex settings for this task.
