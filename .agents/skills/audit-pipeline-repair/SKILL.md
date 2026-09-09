---
name: audit-pipeline-repair
description: Repair the evidence audit tooling in saas-validation-starter when audit logs, source reviews, JSONL metadata or totals diverge. Use for deterministic rendering, cross-file consistency checks, review provenance and regression tests. This is an engineering workflow, not source research or a Stage 1 verdict.
---

# Audit pipeline repair

Read `AGENTS.md`, `docs/codex/audit-pipeline-repair.md` and the selected launch
prompt. Inspect the current checker, tests, canonical evidence schema and idea
protocol before designing changes.

## Workflow

1. Inspect git status and the task baseline. Reproduce the existing checker gap
   without changing research data. Preserve unrelated changes.
2. Define a small, versioned structured review contract. Bind each review to its
   raw ID and content fingerprint; bind inspected material to an exact source,
   speaker/locator and actual tool result. Keep raw facts, observed source facts
   and reviewer conclusions distinct.
3. Generate repeated ledger metadata from canonical records and structured
   reviews. Do not ask a model to retype URLs, authors, keys, statuses or totals
   into Markdown. Render supported judgments with their supporting references.
4. Extend the checker to compare these relationships and regenerated report
   sections. Reject missing, duplicate, stale, contradictory or fabricated-format
   review inputs. A structurally plausible invented capture remains a semantic
   risk: code cannot establish the external origin of an agent-authored file.
5. Add bounded source-review batch preparation and resumable state. Pending or
   blocked rows must not inherit old VERIFIED status. The engineering run prepares
   this workflow but does not perform live source review.
6. Add meaningful regression tests for the listed failures and document actual
   commands. Preserve the canonical evidence schema and market gates. Do not
   rewrite historical idea data just to make the new strict checks pass.

## Non-negotiable distinctions

- Exact URL consistency is separate from conservative URL normalization for
  counts. Preserve comment IDs, query values and fragments identifying a source.
- Raw source fields are canonical claims, not guaranteed truth. If a retrieved
  author, quote or amount contradicts them, record the discrepancy and route it
  to the raw owner; do not generate a second conflicting "canonical" report.
- Quote containment does not prove the observation, payment, recurrence, target
  scope or causal interpretation. Capture explicit semantic decisions too.
- A reported retrieval failure and an observed contradiction are different.
  Neither can silently become VERIFIED; a blocked page alone is not REJECTED.
- Multiple records on one page may concern different speakers. An independence
  key groups an underlying entity/event; neither a URL nor a row count alone
  establishes independence.

Use temporary test datasets for candidate outputs. The first engineering run must
leave `ideas/` unchanged. Finish with tests, the expected legacy-check failures,
the exact next batch command/prompt and any unimplemented acceptance criteria.
