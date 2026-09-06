# Hypothesis setup prompt

The starter pack already contains `ideas/deck-automation/hypothesis.yaml`. Use this prompt for a future idea or to deliberately revise the current hypothesis before research.

```text
Create or revise the Stage 1 hypothesis package for IDEA_PATH.

Read the workspace validation methodology and rules first.

Produce:
- IDEA_PATH/hypothesis.yaml
- IDEA_PATH/research-brief.md
- IDEA_PATH/raw/{market,pain,wtp,workflow,skeptic}/
- IDEA_PATH/evidence/
- IDEA_PATH/output/

The hypothesis must be falsifiable. Explicitly define:
- core proposed job/workflow;
- initial market scope;
- business constraints;
- initial candidate ICPs as hypotheses, not facts;
- core unknowns;
- explicit falsification conditions.

Do not perform market research and do not invent market facts.
If an assumption is supplied by the founder, label it as an assumption rather than evidence.
```
