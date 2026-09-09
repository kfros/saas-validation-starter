# Implement the audit infrastructure repair

Use `AGENTS.md`, `.agents/skills/audit-pipeline-repair/SKILL.md` and
`docs/codex/audit-pipeline-repair.md` as the task instructions. Read the actual
repository files, not summaries from another conversation.

Carry out the engineering brief to completion: reproduce the consistency gap,
implement the structured review contract, deterministic report generation,
integrated strict checks, regression tests, and resumable small-batch preparation.
Create the source-review skill/launch prompt against the implemented interface,
and update `CODEX-RUNBOOK.md` with tested commands and the migration boundary.

This task authorizes relevant local scripts/tests/supporting-contract/docs/skill
edits described in the brief. Use Python script files and normal test commands
for local processing. No live source research, terminal scraping, browser/cache
workarounds, global configuration changes, outreach or market gate changes.
Preserve `.agent/` and all `ideas/` files byte-for-byte; test candidate outputs in
temporary directories. Do not fabricate successful source-review captures for
real IDs to satisfy a new check. Mark synthetic fixtures explicitly.

Inspect the worktree first and preserve unrelated changes. Do not discard/reset
files, switch away from the user's branch, or merge/push changes as a side effect.
If a boundary blocks part of the task, complete the independent allowed work and
explain the specific blocker. Do not stop at a plan when implementation can proceed.

Finish in Russian with what changed, meaningful test results, expected failures
on the unchanged legacy audit, remaining limitations, and the exact command and
launch prompt for the five-ID control batch. Do not run that source-review batch
or Judge in this conversation. Engineering success is not evidence verification.
