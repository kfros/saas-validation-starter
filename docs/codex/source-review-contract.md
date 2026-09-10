# Source-review contract and migration boundary

`scripts/audit_review_pipeline.py` implements version 1 of the sidecar contract
described by `methodology/source-review-schema.json`. It is an offline provenance
and consistency tool. It never opens a URL, and a green result cannot prove that
a locally written fragment originated from the named retrieval tool.

## Layout

A review directory contains `captures.jsonl` and `reviews.jsonl`. Captures retain
only a relevant returned fragment plus exact requested/resolved URLs, locator,
attributed speaker, recorded inspection time, honest tool/result identifiers and
a fragment hash. Reviews bind one known raw ID to its canonical fingerprint,
capture IDs, field-level decisions, audit/scope proposals, money/impact/substitute
assessments, discrepancies and the raw-owner repair queue.

### Exact issue objects

Read the `$defs.discrepancy` and `$defs.rawOwnerRepair` definitions in the sidecar
schema before writing issues. Each object permits only these keys:

| Array | Required keys |
| --- | --- |
| `discrepancies` | `field`, `raw_value`, `observed_value`, `material`, `reason` |
| `raw_owner_repairs` | `field`, `observed_value`, `reason` |

`material` is a JSON boolean, not a string. Keep exact raw values where the issue
names a raw field. `observed_value` records the supported observation or explicit
unknown; it is not a command to execute. Put the requested action in `reason`.
Do not introduce an `action` key or substitute an action for an observed value.
The checker now reports the ID, array index, missing keys and unexpected keys for
all malformed issue objects together. It neither fills missing observations nor
accepts unknown keys to make a checkpoint pass. Empty arrays remain valid when
there is no source/raw discrepancy, including an uninspected blocked source.

Synthetic shape example only; never copy its facts into a real record:

```json
{
  "discrepancies": [{"field": "money_currency", "raw_value": "USD", "observed_value": null, "material": true, "reason": "Synthetic example: currency was not established."}],
  "raw_owner_repairs": [{"field": "money_currency", "observed_value": null, "reason": "Synthetic example: source lacks currency support; the raw owner should leave it unknown until verified."}]
}
```

Canonical JSON serialization is UTF-8 JSON with sorted keys, no insignificant
spaces and `ensure_ascii=false`. Raw fingerprints use that serialization. Fragment
hashes normalize Unicode to NFKC and line endings to LF. Direct quote containment
additionally collapses whitespace; no fuzzy, composite or semantic matching is
accepted.

The scope dependency hash covers the exact scope proposal and current raw
fingerprints of its support IDs. A raw row change invalidates that row's review;
a changed support row invalidates only reviews depending on it. A complete
candidate manifest is regenerated at assembly time and fingerprints the current
raw snapshot, review set, capture set, evidence and scope map.

`prepare-batch` embeds generated raw records and required claim-field names for at
most five selected IDs, plus shared exact-URL groups that retain every separate
raw ID/speaker binding. `checkpoint-batch` first verifies that selected-ID
snapshot, then seals only raw/path, dependency and fragment hashes. It never fills
an outcome, fragment, speaker, claim decision, audit decision or scope decision.
Changes to raw IDs outside the batch do not invalidate its resumable state.

## Status boundary

`VERIFIED` requires a successful capture, all material required claims supported
(or genuinely not applicable), exact quote containment, matching speaker when a
canonical author exists, and no unresolved material discrepancy. Monetary rows
must decide type, amount, currency and period explicitly; nullable raw amounts can
be marked not applicable but cannot be silently invented. `PARTIALLY_VERIFIED`
requires both supported and contradicted/unknown material. A blocked/uninspected
row remains `PENDING`; retrieval failure alone cannot create `REJECTED`.

For VERIFIED rows, the quote claim and supported observation/money claims must be
bound through their own capture and locator to the canonical author/entity. A
separate capture proving an author's name cannot authorize a quote attributed to
another speaker. Distinct speakers on the same page remain separate raw IDs with
separate claim bindings. A future legitimate quoted-speaker relationship needs an
explicit versioned representation; until then it cannot receive VERIFIED.

Every money row separately records payer, recipient, work bought/done,
paid/free/unknown, actual/intent/hypothetical, amount basis and unresolved
unknowns. Every substitute row separately records capability, same-job fit,
price/friction, observed sufficiency and evidence still needed. Gate eligibility
or a concrete exclusion is structured rather than inferred by the renderer.
Actual purchase/pilot/SaaS/contractor/agency spend requires PAID+ACTUAL;
employee time and dedicated roles require ACTUAL but may have UNKNOWN payment or
amount; stated WTP remains INTENT/HYPOTHETICAL with UNKNOWN payment; competitor
pricing is UNKNOWN payment plus OFFER. A conflicting assessment must contradict
or leave unknown the money-type claim and queue a material `money_signal` action
for the raw owner; it cannot remain VERIFIED.

An uninspected BLOCKED/PENDING money row may keep payment and transaction UNKNOWN,
all money fact fields null, and all money claim decisions UNKNOWN. That absence of
knowledge is not a material source/raw contradiction and does not require a
fabricated money_signal discrepancy or raw-owner repair. Keep its blocker and
unresolved questions instead. Observed conflicts still require the normal repair
queue; this exception cannot authorize VERIFIED.

`render --allow-incomplete` creates a checkpoint candidate in which missing rows
are PENDING and scope UNKNOWN. Only a complete strict render/check can enter the
ordinary `audit` and therefore `judge` path. The checker compares both Markdown
reports and the repair queue byte-for-byte with deterministic regeneration.
Judge may count or cite a contradiction only when the review's
`impact_assessment.eligible_gates` includes that gate; an explicit review
exclusion cannot be silently ignored by the scorecard.

Checkpoint validates completed review/capture fingerprints and their current
support dependencies before sealing any new or previously blocked row. Derived
values are prepared in memory and files are written only after the entire bundle
passes. A changed external support row therefore requires a new review instead
of receiving an automatically refreshed dependency hash.

## Migration

The historical audit has no structured source reviews and is intentionally not
grandfathered. Run `legacy-diagnostic` to inspect its report/JSONL drift. Do not
copy old VERIFIED labels, prose or claimed browser activity into sidecars. Review
known raw IDs in batches of at most five, checkpoint blocked work, assemble a
temporary candidate, then replace evidence artifacts only in a separately
authorized audit/migration task. Raw-owner corrections are queued, not applied by
the auditor. Market gates and `methodology/evidence-schema.json` remain unchanged.
