---
name: source-review-batch
description: Review one prepared batch of at most five known multi-brand-content raw IDs against their exact original public URLs, producing v1 captures, reviews, repair-queue decisions, and resumable checkpoints. Use only after audit pipeline preparation; never for discovery or Judge work.
---

# Source-review batch

Read `AGENTS.md`, `ideas/multi-brand-content/research-protocol.md`,
`ideas/multi-brand-content/audit-checklist.md`,
`docs/codex/source-review-contract.md`, the selected launch prompt, and the
prepared `batch-manifest.json` before acting.

Review only the IDs and exact URLs in the manifest. Use an authorized browser or
public-source retrieval tool; do not use terminal HTTP clients, scrapers,
Antigravity internals/caches, replacement searches, outreach, or newly discovered
IDs. A historical report or repair brief is a lead, never source evidence.

For every actual attempt, append an honest v1 capture to `captures.jsonl`: exact
requested URL, actual resolved URL if known, locator, attributed speaker, recorded
timestamp, real tool name/result ID if exposed, local attempt ID, outcome, the
small relevant returned fragment and its hash. Unknowns stay null. A local ID is
not an external result ID.

Create one v1 review per raw ID with its manifest raw fingerprint and explicit
claim decisions. Keep canonical raw facts, observed source facts and audit
conclusions separate. Decide quote, observation, attribution, money fields,
recurrence, role/scope and material interpretation at their stated strength.
Exact quote containment allows only NFKC, line-ending and whitespace
normalization—not fuzzy/composite paraphrases. Bind every decision to the actual
capture and speaker.

For every money row complete `money_assessment`: payer, recipient, work,
paid/free/unknown, actual/intent/hypothetical, amount basis and unknowns. Complete
`impact_assessment` with eligible gates or an exclusion. For every substitute row
separate capability, same-job fit, price/friction, observed sufficiency and the
evidence still needed; do not collapse product existence into sufficiency.

A material disagreement goes into `discrepancies` and `raw_owner_repairs`; do not
rewrite raw. Missing access, stale raw, an unreviewed material claim or unresolved
contradiction cannot become VERIFIED. Retrieval failure alone is not REJECTED.
Blocked rows are PENDING with a concrete blocker; historical VERIFIED is never
carried forward.

After each useful record, update the batch files and run the exact checkpoint
command from the launch prompt. Preserve processed, blocked and remaining IDs.
On quota/resource exhaustion, make at most one permitted retry, checkpoint and
stop PARTIAL if it repeats. Stop after three consecutive tool failures. Do not
fan out more than the prepared five IDs.

Finish with processed/blocked/remaining IDs, discrepancies and raw-owner actions.
Do not render a final complete audit, run Judge, change market gates or claim that
local hashes prove external provenance.
