---
name: evidence-audit
description: Audits already-collected Stage 1 evidence for source support, recency, context, independence, schema compliance, and duplicates. It never performs new market research.
---

# Evidence Audit Skill

## Hard boundary

DO NOT conduct new market research.
DO NOT browse for replacement evidence.
DO NOT improve a weak record with a new source.

You may open an already-recorded URL only to verify the claim in that record.

## Inputs

Read all `evidence.jsonl` files under the target idea's `raw/*` directories plus the canonical methodology/schema.

## Audit each record

Check:

- schema conformity;
- URL exists and is the source actually inspected;
- source supports the observation;
- observation does not overstate the source;
- interpretation is clearly separated;
- current pricing/features are recent enough;
- source tier is appropriate;
- source excerpt/context is not misleading;
- ICP attribution is supported;
- recurrence/money fields are supported;
- independence key is reasonable;
- duplicates/syndicated claims are grouped.

## Statuses

Set exactly one:

- `VERIFIED` — source supports the material observation;
- `PARTIALLY_VERIFIED` — source supports only part; explain;
- `REJECTED` — unsupported, duplicate without independent value, inaccessible in a way that prevents verification, misleading, or invalid.

## Outputs

Write only to the target idea's `evidence` directory:

- `evidence.jsonl` — consolidated records with audit status/reason;
- `audit-summary.md` — counts, rejection reasons, duplicate groups, source-tier distribution;
- `high-impact-review.md` — strongest 10 positive, strongest 10 negative, all VERIFIED money signals, and any disputed/high-impact records for human spot-checking.

The Judge must be able to work from these outputs alone.

Do not issue a PASS/FAIL verdict.
