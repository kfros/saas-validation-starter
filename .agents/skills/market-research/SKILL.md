---
name: market-research
description: Maps competitors, substitutes, pricing, positioning, target users, current product capabilities, and market structure for a SaaS validation hypothesis. Use during Stage 1 before customer interviews.
---

# Market Research Skill

## Goal

Produce a factual map of the current market around the selected hypothesis. Do not decide whether the idea is good.

## Required inputs

Read:

- the target idea's `hypothesis.yaml`;
- the target idea's `research-brief.md`;
- `methodology/evidence-standard.md`;
- `methodology/evidence-schema.json`.

## Research questions

Identify:

- direct competitors;
- adjacent competitors;
- substitutes, including bundled/free features in large platforms;
- official pricing;
- target customers and positioning;
- relevant product capabilities;
- export/import formats;
- integrations;
- corporate-template or brand features;
- any complete substitute for the proposed workflow.

For current products, prefer official pages and documentation. Use third-party estimates only when necessary and label them as estimates.

## Output

Write only to the assigned `raw/market` directory.

Create:

- `market-map.md` — concise human-readable market map;
- `evidence.jsonl` — atomic evidence records conforming to the canonical schema.

All raw records must use `audit_status: PENDING`.

## Evidence rules

- Do not use search snippets as evidence.
- Do not infer adoption from mere product existence.
- Do not infer willingness to pay from pricing alone.
- Record contradictory evidence.
- Use `type: substitute` when a tool appears to solve most of the proposed workflow.
- Use a stable `independence_key` for the underlying source/entity/claim.

## Stop condition

Stop when the main competitor/substitute landscape is saturated enough that additional searches produce mostly duplicates, or when at least 15 meaningful market/substitute evidence records have been collected across diverse sources.

Do not produce a PASS/FAIL verdict.
