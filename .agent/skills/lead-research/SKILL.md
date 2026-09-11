---
name: lead-research
description: Builds a source-backed public organization pool for a bounded Stage 1.5 screening scope. Use before outreach; never sends messages, counts interviews or changes a Stage 1 verdict.
---

# Stage 1.5 Lead Research

Read `AGENTS.md`, `methodology/stage1.5-lead-research.md`,
`methodology/stage15-lead-schema.json`, the selected idea's `config.json`,
`hypothesis.yaml`, Stage 1 report and the selected launch prompt.
Before creating the first row, read
[`references/record-shapes.md`](references/record-shapes.md). It is a structural
example only and must never be copied as market data.

## Role boundary

Discover and qualify public business leads. Do not contact anyone, submit forms,
book meetings, follow accounts, collect private contact details, change Stage 1
evidence or claim that a lead validates demand. A qualified lead is only ready
for a separate screening/outreach decision.

Use the browser for public research. Do not use terminal HTTP clients, scrapers,
Antigravity internal files/cache or guessed data. Search snippets are leads only;
open each supporting page. Retry a failed page at most once. After three
consecutive browser/tool failures, checkpoint honestly and stop partial.

## Canonical workflow

1. Read existing `leads.jsonl`, `source-register.jsonl`, generated summary and
   run status before discovering anything. Do not reopen completed leads unless
   resolving a documented conflict.
2. Search broadly across different English-speaking geographies and directory
   surfaces. One organization is one lead. Check official-domain and normalized
   organization duplicates before adding it.
3. Write a source row for every factual claim. Preserve the exact small fragment,
   locator, page URL, actual outcome and retrieval time. Only `SUCCESS` may
   support a confirmed claim.
4. Classify the lead against the hard criteria in `config.json`. Unknown is not
   confirmed. Conflicting headcount, unclear identity, stale/rebranded sites and
   an adjacent paid-ads/video-only service remain `HOLD` or `EXCLUDED`.
5. Store only a public business contact page or company messaging route. Do not
   copy personal emails/phone numbers or guess an address.
6. Keep SMB clientele, hands-on owner work, recurring revision pain, current
   stack, budget authority and WTP explicit for later screening when public
   evidence does not establish them.
7. Update the analytical report with source-backed observations and exclusions.
   Do not hand-edit `leads.csv`, `lead-summary.json` or computed totals.
8. Run the exact checkpoint command in the launch prompt after each bounded
   group. Stop at that conversation's candidate/qualification budget even if the
   50-lead target is not yet reached; a fresh resume conversation continues it.

## Handoff

When the target is reached, seal the package with the tracked script and stop.
Report the snapshot ID, qualified/hold/excluded counts, priority counts,
geographies, unresolved screening fields and blockers. Do not commit/push unless
the launch explicitly authorizes that Git action. Do not start the independent
Codex audit or outreach.
