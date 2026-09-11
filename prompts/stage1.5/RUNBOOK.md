# Stage 1.5 Lead Research Runbook

This runbook separates lead ownership, independent review and outreach. The
first configured scope is Multi-brand content; GEO and Deck follow only after
this workflow is proven and receive their own locked configs and launch prompts.

## Decision boundary

Stage 1.5 is an explicitly chosen exploratory exception after `INSUFFICIENT
EVIDENCE`. It aims for 5 qualified substantive conversations and stops at 8
counted conversations. Lead research may build a much larger funnel. A lead,
message, response and counted conversation are different units.

No prompt in this kit authorizes outreach.

## Roles and sequence

| Phase | Owner | Session | Output |
|---|---|---|---|
| 1. Broad lead pool | Antigravity | Fresh High conversation per bounded run | 50 source-backed qualified leads plus holds/exclusions |
| 2. Independent audit | Codex in this Stage 1.5+ thread | One logical audit, checkpointed in small batches | Review state, atomic findings, audit report |
| 3. Repair | Antigravity | Fresh High conversation | Corrected/replacement leads, response, new snapshot |
| 4. Final readiness | Codex in this thread | Fresh review turn | Readiness decision; still no outreach |
| 5. Outreach/screen/interview kit | Built only after readiness | Separate authorization | Messages, funnel log and interview protocol |

## Phase 1 — Antigravity lead research

1. Use branch `stage1.5-multibrand-leads` (or its eventual shared successor).
2. Start a fresh Antigravity conversation in High reasoning.
3. Enable `/browser` and invoke `/lead-research`.
4. Paste the full unchanged file
   `prompts/stage1.5/10-multibrand-lead-research.md`.
5. After the agent stops, review its reported diff and commit/push the bounded
   run yourself (or authorize that Git action separately). The research prompt
   itself does not grant a broad terminal/Git write allowance.
6. If `run-status.json.status` is `IN_PROGRESS` or `PARTIAL_BLOCKED`, start a
   fresh conversation and paste the same prompt again. Do not edit the prompt.
7. Repeat until the initial snapshot is sealed and the final checker passes.

Each run adds at most 10 qualified leads or examines at most 20 new candidates.
Therefore 50 qualified leads require at least 5 Antigravity runs; 5–8 is a
reasonable operational expectation, not a quota. Tool blocks or a high exclusion
rate may require more. Existing completed rows are preserved between runs.

Bring the final commit SHA and Antigravity report back to the Stage 1.5+ thread.

## Phase 2 — Codex independent audit

Codex follows `prompts/codex/30-audit-multibrand-leads.md`. Structural checks run
once; live semantic/source review proceeds in small batches while retaining one
audit state. Every qualified lead, decisive hard-claim source and public contact
route must be checked. Codex records findings separately and does not repair the
canonical data.

## Phase 3 — Antigravity repair

After the Codex audit commit is available, start a fresh Antigravity High
conversation with `/browser` and `/lead-research`, then paste
`prompts/stage1.5/20-multibrand-lead-repair.md`. It must resolve or answer every
finding, replace demoted leads when necessary, retain at least 50 qualified
organizations and seal `mb-leads-v1-002`.

## Phase 4 — joint consistency and readiness

Codex follows `prompts/codex/31-final-multibrand-readiness.md`. This is the joint
result: Antigravity has re-opened and repaired its source-owned rows; Codex
independently rechecks changed rows and the final package. Required outcomes:

- no duplicate active organization/domain;
- generated totals equal canonical JSONL;
- all 50 qualified leads have live official websites and public business contact
  routes;
- decisive hard claims are directly supported;
- priority and screening unknowns are honest; and
- no open BLOCKER/MAJOR finding affects the pool.

Only `READY_FOR_BOUNDED_OUTREACH_DESIGN` advances to construction of the next
kit. It does not send or authorize outreach by itself.

## Later idea order

After Multi-brand, repeat the proven workflow in this order:

1. GEO / AI-search visibility monitoring;
2. Vertical B2B deck / sales-collateral automation.

Each idea needs a separate config because its hard public qualification criteria
and screening unknowns differ. Do not reuse Multi-brand claim labels by analogy.
