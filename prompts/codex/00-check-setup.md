# Read-only Codex setup check

Read the repository's `AGENTS.md`,
`.agents/skills/audit-pipeline-repair/SKILL.md`, `CODEX-RUNBOOK.md`, and
`docs/codex/audit-pipeline-repair.md`.

Do not modify files or start the implementation yet. Do not browse or read global
configuration/credentials, Antigravity internals or unrelated projects.

Inspect git status, current branch/HEAD and whether baseline
`241d04317c5ce93ba37982b67c62fc535c7b4727` is in this checkout's history.
Confirm the required local files are present and that the existing checker/tests
can be read. Missing or divergent history should be reported; never reset the
worktree to force a match.

Reply briefly in Russian with the actual repository path, branch/HEAD, worktree
state, instruction/skill files you read, and any blocker. Explain that the next
task is offline engineering and does not verify sources or change market gates.
Do not claim automatic skill discovery or browser availability solely because
a file was readable. If no blocker remains, identify the implementation prompt:
`prompts/codex/10-repair-audit-pipeline.md`.
