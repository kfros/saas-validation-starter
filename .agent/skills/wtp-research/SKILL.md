---
name: wtp-research
description: Researches revealed willingness to pay and costly labor for a specific Stage 1 job and ICP. Use to distinguish actual purchases, budgets, labor, and tool use from vendor pricing or hypothetical interest.
---

# Willingness-to-Pay Research

## Goal

Determine whether buyers already commit money or costly labor to the target job, who pays, what is purchased, and how closely that spend maps to the proposed workflow.

## Scope lock

Before browsing, read the target `hypothesis.yaml`, `research-brief.md`, canonical evidence standard, schema, and gates. Research the stated job and candidate ICPs; do not silently redefine the product or pool unrelated segments.

Adjacent spend may be recorded as `neutral`, but label the mapping gap explicitly.

## Evidence hierarchy

Prioritize, in order:

1. Buyer-side first-hand evidence of an actual purchase, renewal, paid pilot, invoice, or recurring spend for the job.
2. An actual contractor, freelancer, or agency engagement, or an explicit buyer budget for the job.
3. Paid employee time or a dedicated role materially performing the job.
4. First-hand evidence that a paid SaaS product is actually used for the job.
5. Stated budget or willingness to pay.
6. Vendor/competitor pricing as context only.

Search across multiple categories when credible evidence exists. Do not manufacture category diversity.

## What does not establish revealed WTP

Do not treat any of the following as actual spend without buyer-side purchase/use evidence:

- a competitor pricing page;
- an agency or freelancer rate card;
- a marketplace's typical rate or salary aggregator;
- vendor revenue, funding, customer count, or market-size estimate;
- a broad creative-services subscription that merely includes presentations;
- a job posting where deck work is incidental;
- a freelance listing that was posted but not shown as awarded or purchased;
- a hypothetical savings calculation or `would pay` statement;
- hours of work encoded as dollars.

These may be useful context records with low strength and the appropriate `money_signal`; they cannot by themselves satisfy Gate 3.

## Record requirements

Each record must be atomic and directly supported by one opened original public page. Record:

- payer/buyer or employing organization when known;
- target ICP and role only when the source supports them;
- exact job/output being purchased or performed;
- whether the signal is actual behavior, budget intent, stated WTP, or vendor price;
- amount, currency, and period only when explicitly stated;
- recurrence only when it describes the target job;
- the gap between the purchased work and proposed workflow;
- a short factual observation separated from interpretation.

Classification rules:

- Use `actual_purchase` or `paid_pilot` only for explicit buyer-side behavior.
- Use `contractor_spend` or `agency_spend` only for an actual engagement/spend or a clearly identified buyer budget; otherwise use `stated_wtp` or `competitor_price` as appropriate.
- Use `employee_time` when a practitioner/source establishes actual paid time on the job. Leave currency and amount null unless the monetary cost is sourced.
- Use `dedicated_role` only when the target job is a material duty. Do not allocate the full salary to the job without evidence.
- Use `saas_spend` only when paid use for the target job is established. A pricing page is `competitor_price`.
- Vendor pricing and substitute capability should normally be `neutral` or `contradicts`, not automatic support for the proposed product.

All raw records must keep `audit_status: PENDING`.

## Research quality

Prefer original buyer/practitioner statements, actual job postings, actual project listings, procurement records tied to use, and official pages for price context. Open every source; search-result snippets are leads only.

Do not infer missing salary, loaded cost, adoption, purchase, contract value, or buyer authority. `UNKNOWN` is valid.

## Outputs

Write only to the assigned `raw/wtp` directory:

- `evidence.jsonl`;
- `wtp-map.md` containing:
  1. scope and ICP coverage;
  2. actual purchase/spend signals;
  3. costly-labor signals;
  4. stated budgets/WTP;
  5. context-only vendor pricing;
  6. strongest evidence against meaningful WTP;
  7. category coverage, source shortfall, blockers, and unknowns.

Target up to 10 credible candidate records across at least 3 categories when the public evidence supports them. This is not a quota and is never a reason to lower standards.

Do not decide a gate or final verdict.

## Tool and stopping policy

Use the browser for public research. Do not retrieve web content through terminal, Python, PowerShell, curl, internal Antigravity files, browser cache, or ad-hoc scrapers.

After a rate limit, quota/resource error, or repeated browser failure, retry the failed research action at most once. After 3 consecutive research-tool failures, preserve the records collected, document the blocker and missing categories in `wtp-map.md`, and finish partial.

Validate the finished file only with:

```bash
python scripts/validate_evidence.py <idea-path>/raw/wtp/evidence.jsonl
```

Do not use `python -c`, inline `jsonschema`, or shell parsing. If validation fails, repair only the reported JSONL problem and rerun once. If it still fails, document the structural blocker and stop.
