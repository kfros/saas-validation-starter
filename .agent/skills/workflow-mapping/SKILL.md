---
name: workflow-mapping
description: Maps candidate ICPs, workflow triggers, inputs, outputs, recurrence, current tools, actors, buyers, and reachable channels for a SaaS hypothesis. Use during Stage 1 validation.
---

# Workflow / ICP Mapping Skill

## Goal

Determine where the proposed job actually occurs and which segments appear most promising for Stage 2 interviews.

## For each plausible segment, map

- role/person doing the work;
- buyer/budget owner when observable;
- trigger that starts the workflow;
- inputs;
- major steps;
- output/deliverable;
- current tools;
- recurrence evidence;
- manual effort evidence;
- handoffs/approvals;
- reachable discovery channels;
- evidence count and confidence.

## Important

Do not treat an imagined persona as evidence.

A plausible segment may be listed as a hypothesis, but all claims about its real workflow must be supported by evidence records.

Do not invent workflow frequency. Use `unknown` when not established.

## Output

Write only to the assigned `raw/workflow` directory:

- `workflow-map.md`;
- `icp-candidates.md`;
- `evidence.jsonl`.

All records start `audit_status: PENDING`.

## Reachability

Identify where Stage 2 could discover prospects, such as:

- LinkedIn role/company filters;
- industry directories;
- communities;
- agency directories;
- public company lists;
- conference/member directories.

Do not collect the full Stage 2 prospect list yet.

Do not issue a Stage 1 verdict.
