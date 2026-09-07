---
name: evidence-audit
description: Audits already-collected Stage 1 evidence for direct source support, semantic classification, scope attribution, independence, and schema compliance. Use after research; never use it to discover or replace evidence.
---

# Evidence Audit

## Role

Turn raw `PENDING` records into a canonical audited dataset. Verify what each recorded URL actually establishes; do not improve the research or decide the Stage 1 verdict.

## Hard boundaries

- Do not search for new or replacement sources.
- Open only a `source_url` already present in a raw record. Open each canonical URL once and apply that inspection to its records.
- Do not use general knowledge, search snippets, cached browser content, Antigravity internal files, or paths outside the repository as evidence.
- Do not use terminal commands, scripts, HTTP clients, or ad-hoc scrapers to retrieve web content.
- Do not change methodology, hypothesis, research brief, or raw agent output.
- Do not rewrite an unsupported observation into a weaker claim merely to mark it `VERIFIED`.
- Do not issue PASS, CONDITIONAL PASS, FAIL, or INSUFFICIENT EVIDENCE.

## Inputs

Read:

- the target `hypothesis.yaml` and `research-brief.md`;
- `methodology/evidence-standard.md`, `methodology/evidence-schema.json`, and `methodology/stage1-gates.md`;
- every target `raw/*/evidence.jsonl` file.

## Audit protocol

Audit every record in this order.

### 1. Structure and source identity

Confirm that the record is valid JSON, conforms to the canonical schema, is atomic, points to the exact inspected public page, and identifies the real author/entity and date when available. A directory root, search page, unrelated documentation page, or changed page that no longer contains the claim does not verify it.

### 2. Direct support

The page must directly support every material part of `observation`, including numbers, units, dates, role, ICP, workflow, recurrence, amount, currency, and period. Do not derive a median from a range, convert time into currency, allocate an entire salary to one task, or combine facts from several URLs into one record.

`interpretation` may explain relevance but may not add facts. Unsupported interpretation does not become evidence.

### 3. Semantic classification

Apply these distinctions strictly:

- `pain`: an experienced workflow problem, cost, delay, error, frustration, risk, or workaround. A product feature, product limitation, price, market statistic, or job description alone is not pain.
- `gap`: an observed missing capability, failed output, manual cleanup, or workflow break experienced in the target job. A feature comparison or an absent feature on a pricing page alone is not a validated customer gap.
- `recurrence`: explicit frequency of the core job or problem. Billing cadence, subscription term, publication cadence, or the fact that a workflow could recur is not recurrence.
- `reachability`: evidence of a specific target role/segment plus a real discoverable or contactable surface. A role label, association homepage, or claimed member count alone is insufficient.
- `substitute`: evidence that an alternative performs material parts of the same job. Current incumbent capability normally contradicts the proposed wedge or is neutral; it is not supporting evidence merely because a market exists.
- `wtp`: money or costly labor demonstrably committed to the same or a closely mapped job.

For WTP and Gate 3:

- Eligible signals may include an actual purchase or paid pilot; first-hand actual SaaS use for the job; actual employee time spent on the job; an actual contractor/agency engagement or buyer budget; or a dedicated role whose duties materially include the job.
- A vendor's own price, agency rate card, marketplace average, salary aggregator, broad creative retainer, or competitor contract benchmark is `competitor_price` context unless a buyer-side source establishes purchase or use.
- A job posting supports `dedicated_role` only when the target job is a material duty. Its full salary is not spend on the target job unless the source establishes that allocation.
- A posted freelance budget without evidence of award or purchase is stated/budget intent, not actual contractor spend.
- `saas_spend` requires evidence of actual use or purchase for the target job; a pricing page alone does not qualify.

### 4. Scope attribution

Assign a record to an ICP only when the source identifies that role or segment. Do not relabel generic presentation users, enterprise teams, agencies, consultants, proposal teams, or CRE teams as one another. If the narrow ICP is not supported, keep it unknown or reject the material attribution.

### 5. Independence and duplicates

Canonicalize URLs by removing tracking parameters and fragments. Group the same person/company and underlying claim under one `independence_key`, including reposts and syndicated pages.

- Exact duplicate claim: retain one canonical record and reject the duplicate.
- Same source with genuinely different atomic observations: records may remain, but use the same independence key where they are not independent.
- A Judge may count an independence key at most once per gate.

## Audit statuses

Set one status and a concrete `audit_reason`:

- `VERIFIED`: the opened page directly supports all material fields and the semantic classification.
- `PARTIALLY_VERIFIED`: the page supports a useful core fact but a material field, scope attribution, amount, recurrence, or classification is overstated. It cannot satisfy a gate.
- `REJECTED`: unsupported, misleading, non-atomic beyond repair, duplicate without independent value, wrong URL, or invalid.
- `PENDING`: use only when browser/tool failure prevents inspection. State the blocker; the Judge must ignore it.

An inaccessible page is not VERIFIED. Distinguish a source failure from an Antigravity quota/tool failure in `audit_reason`.

## Outputs

Write only to the target idea's `evidence` directory:

- `evidence.jsonl`: all consolidated records with status and audit reason;
- `audit-summary.md`: status counts by type, source tier, ICP, and money signal; duplicate groups; blocked records; and counts potentially eligible for each gate without declaring a gate result;
- `high-impact-review.md`: every VERIFIED or PARTIALLY_VERIFIED money record, the strongest positive and contradictory records, all substitute candidates, and every record whose inclusion could change a gate.

The outputs must let the Judge reproduce every count without browsing.

## Mechanical checks

After writing the canonical JSONL, run only:

```bash
python scripts/validate_evidence.py <idea-path>/evidence/evidence.jsonl
python scripts/find_duplicates.py <idea-path>/evidence/evidence.jsonl
```

Do not use `python -c`, PowerShell one-liners, `jsonschema` snippets, or Antigravity cache inspection. If validation fails, repair only the reported local JSONL problem and rerun the validator once. If it still fails, record the blocker and stop.
