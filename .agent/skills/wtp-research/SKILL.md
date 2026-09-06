---
name: wtp-research
description: Researches revealed willingness to pay and existing spend around a SaaS workflow using actual subscriptions, labor, contractors, agencies, job roles, and adjacent budgets. Use during Stage 1 validation.
---

# Willingness-to-Pay Research Skill

## Goal

Determine whether money or costly labor already flows toward solving the target job.

## Strong evidence categories

Search for evidence of:

- actual SaaS subscriptions or paid plans used for the job;
- job postings where the role spends meaningful time on the job;
- freelance/contract work bought to produce the output;
- agency/service spend;
- internal teams dedicated to the job;
- tools bought specifically to reduce the work;
- first-hand statements of actual spend.

Competitor pricing is useful context but is not enough by itself.

## Research method

For job and freelance evidence, record what is actually being purchased and whether it maps to the target workflow.

When estimating employee-time cost, record the observable time/workload separately. Do not invent salary or loaded-cost numbers unless sourced.

## Output

Write only to the assigned `raw/wtp` directory:

- `wtp-map.md`;
- `evidence.jsonl`.

Use `money_signal` consistently with the canonical schema.

All records start `audit_status: PENDING`.

## Target

Target up to 10 candidate money records spanning at least 3 distinct money-signal categories when evidence exists.
This is a research target, not a mandatory completion count. Never retry indefinitely, lower evidence quality, or invent alternative scraping infrastructure merely to reach the target.
If tool limits prevent reaching 10, stop with the credible records already collected and report the shortfall and blocker.

Do not issue a PASS/FAIL verdict.
