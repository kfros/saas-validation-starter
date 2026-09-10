# Control batch recovery after 249030f

This is an engineering recovery note, not source evidence or a Stage 1 verdict.
Original commit: `249030f83e9e53b0ce663513c40bd100d4ec5ec2`.

## What the commit actually retained

- Two reviews: completed `mb-pain-001` and uncheckpointed `mb-wtp-001`.
- Three source fragments, all attributed to one Reddit URL and the same external
  result ID, `turn0view0`. They represent separate speakers/fragments; their count
  does not establish three independent page retrievals.
- No captures/reviews for `mb-wtp-005`, `mb-wtp-008`, or `mb-wtp-009`. Findings in
  the conversation are leads to reopen, not substitutes for those missing files.

## Mechanical recovery performed

The old schema allowed arbitrary objects in two issue arrays while the Python
checker required exact keys. In the retained WTP review, all four repair objects
used `action` instead of `observed_value`. The latter is now copied from the
matching already-recorded discrepancy. The original action text is preserved
in `reason`; no new source-dependent claim is introduced.

The existing WTP decision remains PARTIALLY_VERIFIED. Running checkpoint fills
its deterministic hashes and records it as processed. Processed means a review
was checkpointed; it does not mean the evidence is VERIFIED or gate-eligible.

After recovery, `control-01` has:

- processed: `mb-pain-001`, `mb-wtp-001`;
- remaining: `mb-wtp-005`, `mb-wtp-008`, `mb-wtp-009`;
- blocked: none.

The completed pain review and its capture fingerprints were preserved. All raw
records, source fragments, speakers, tool/result IDs and inspection dates were
preserved. Only the WTP issue structure and derived checkpoint data changed.
No original page was newly inspected by this engineering recovery.

## Content concern requiring a fresh scope review

The existing pain review promotes a designer working with an agency and about
five clients to full `IN_SCOPE`. Its saved fragment does not establish hands-on
ownership, SMB clientele or recurring static production/revision as required by
the fixed `MULTIBRAND-OPERATOR-01` hypothesis. A real permissions/setup problem
can remain useful while full scope and target-job recurrence are UNKNOWN.

Do not edit the sealed review or its fingerprint map to force a change. A separate
empty one-ID batch is prepared at `work/source-review/control-01-scope-recheck/`.
Its new review is a revision for `mb-pain-001`, not an additional independent
signal. Reopen the original source; use the scope requirements without filling
missing facts from the thread topic. Keep broad role support separate from full
scope membership and per-client setup separate from repeated production work.

`mb-wtp-001` already acknowledges missing role, target-job use and recurrence.
Its saved `interpretation=SUPPORTED` still deserves a later content check because
the canonical interpretation asserts WTP for multi-brand asset separation.
This mechanical recovery does not endorse that overreach, certify the other
captured claims, or turn its PARTIALLY_VERIFIED row into admissible G3 evidence.

## Resume

Use `prompts/codex/21-resume-control-batch.md`. Both manifests already exist;
there is no need to prepare or reset either batch again. First review the single
pain revision, then finish only the three remaining WTP IDs in the original
batch. No raw repair, final audit assembly or Judge is part of this run.

If retrieval fails, preserve the honest partial state. If the permitted structural
repair still fails, preserve the files and exact error without repeatedly issuing
the same command. The explicit local `Get-Content -LiteralPath` read exception
replaces the overly restrictive read boundary for these inputs only.

At a later authorized assembly, select at most one accepted current review per
raw ID. Never concatenate the old pain review and its revision into duplicate
evidence, add their counts together, or select a VERIFIED version just because
it produces a better outcome. A blocked revision leaves the concern unresolved.
