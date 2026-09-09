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

Every money row separately records payer, recipient, work bought/done,
paid/free/unknown, actual/intent/hypothetical, amount basis and unresolved
unknowns. Every substitute row separately records capability, same-job fit,
price/friction, observed sufficiency and evidence still needed. Gate eligibility
or a concrete exclusion is structured rather than inferred by the renderer.

`render --allow-incomplete` creates a checkpoint candidate in which missing rows
are PENDING and scope UNKNOWN. Only a complete strict render/check can enter the
ordinary `audit` and therefore `judge` path. The checker compares both Markdown
reports and the repair queue byte-for-byte with deterministic regeneration.

## Migration

The historical audit has no structured source reviews and is intentionally not
grandfathered. Run `legacy-diagnostic` to inspect its report/JSONL drift. Do not
copy old VERIFIED labels, prose or claimed browser activity into sidecars. Review
known raw IDs in batches of at most five, checkpoint blocked work, assemble a
temporary candidate, then replace evidence artifacts only in a separately
authorized audit/migration task. Raw-owner corrections are queued, not applied by
the auditor. Market gates and `methodology/evidence-schema.json` remain unchanged.
