---
name: pain-mining
description: Finds first-hand evidence of concrete recurring user pain, manual workarounds, failures, delays, and frustration related to a SaaS hypothesis. Use during Stage 1 validation.
---

# Pain Mining Skill

## Goal

Find first-hand evidence of real workflow pain. Optimize for specificity and independence, not volume.

## Required inputs

Read the target idea hypothesis/research brief and the workspace evidence methodology/schema.

## Preferred sources

Prioritize:

- Reddit;
- G2/Capterra/App Store/marketplace reviews;
- practitioner community posts;
- LinkedIn posts from practitioners;
- vendor support/community threads;
- public interviews describing actual work.

SEO articles and vendor marketing claims are weak evidence unless they lead to primary evidence.

## What counts as strong pain

Look for:

- manual repetitive steps;
- rework;
- quality failures;
- export/import problems;
- outdated/inconsistent assets;
- delays or bottlenecks;
- expensive specialist involvement;
- errors or risk;
- frustration with current alternatives;
- abandoned tools and reasons for abandonment.

## Output

Write only to the assigned `raw/pain` directory:

- `pain-clusters.md`;
- `evidence.jsonl`.

Cluster evidence after collecting it, but preserve each independent atomic evidence item.

All records start with `audit_status: PENDING`.

## Minimum target

Attempt to collect at least 25 candidate pain records so the Auditor can reject weak/duplicate items while still allowing the Stage 1 G1 target to be tested.

Do not manufacture volume. If fewer credible records exist, report that as a finding.

## Special rule

A product review complaining about an irrelevant feature does not count merely because it is negative. The pain must relate to the investigated workflow.

Do not issue a Stage 1 verdict.
