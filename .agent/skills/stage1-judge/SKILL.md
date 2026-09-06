---
name: stage1-judge
description: Produces the Stage 1 PASS, CONDITIONAL PASS, FAIL, or INSUFFICIENT EVIDENCE decision using only VERIFIED audited evidence and the predefined gates. It is prohibited from doing new research.
---

# Stage 1 Judge Skill

## Hard boundary

DO NOT browse.
DO NOT search the web.
DO NOT add sources.
DO NOT use general knowledge to fill missing facts.
DO NOT use PENDING, PARTIALLY_VERIFIED, or REJECTED evidence when deciding whether gates pass.

Missing evidence is `UNKNOWN`.

## Inputs

Read:

- target `hypothesis.yaml`;
- `methodology/stage1-gates.md`;
- `methodology/scoring.md`;
- target `evidence/evidence.jsonl`;
- target `evidence/audit-summary.md`.

Deduplicate by `independence_key` before counting thresholds.

## Evaluate

Report each gate independently:

- G1 concrete pain;
- G2 recurrence;
- G3 existing spend/WTP;
- G4 repeatable gap;
- G5 ICP reachability;
- G6 killer substitute.

For every gate include:

- result;
- verified independent count where applicable;
- strongest evidence IDs;
- strongest contradictory evidence IDs;
- confidence;
- unknowns.

## Verdict

Use exactly one:

- PASS
- CONDITIONAL PASS
- FAIL
- INSUFFICIENT EVIDENCE

Do not change gate thresholds to rescue the hypothesis.

## Outputs

Write only to the target idea's `output` directory:

- `stage1-report.md`;
- `scorecard.json`.

`stage1-report.md` structure:

1. Hypothesis
2. Executive verdict
3. What users appear to be doing
4. Pain clusters
5. Recurrence
6. Existing spend/WTP
7. Current alternatives
8. Repeatable gaps
9. Candidate ICPs
10. Candidate wedges
11. Strongest disconfirming evidence
12. Unknowns
13. Stage 2 questions
14. Gate scorecard

The report must distinguish evidence-backed conclusions from unresolved hypotheses.
