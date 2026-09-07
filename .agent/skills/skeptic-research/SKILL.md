---
name: skeptic-research
description: Tries to falsify a Stage 1 SaaS hypothesis by testing direct substitutes, weak frequency or WTP, adoption blockers, bundling, and technical constraints for the stated ICP. Use as the adversarial research track, not to invent a better wedge.
---

# Skeptic Research

## Mission

Test whether the hypothesis as written is a bad business. Look for evidence that the job is already solved, too infrequent, too cheap, too risky, or too difficult to adopt.

Do not rescue the hypothesis while researching.

## Scope lock

Read the target hypothesis, research brief, evidence standard, schema, and gates before browsing. Evaluate the stated job, business constraints, and each declared candidate ICP separately.

If evidence suggests a new ICP or wedge, record it only as an unvalidated follow-up hypothesis. Do not transfer evidence from the failed scope or declare the new scope viable.

## Falsification targets

Search specifically for:

- complete and near-complete substitutes for the same job and ICP;
- incumbent features, add-ins, templates, services, and manual workflows that make the pain cheap to tolerate;
- cheap/free bundling and low switching friction;
- actual low frequency, short completion time, or abandonment of the workflow;
- users satisfied with current tools or returning to manual work after trying automation;
- low spend, rejected prices, weak purchase authority, or no budget owner;
- privacy, security, procurement, data-access, integration, and change-management blockers;
- fidelity, accuracy, editable-output, template, and review requirements that defeat automation;
- technical complexity incompatible with the stated MVP/founder constraints;
- failed or discontinued products when the reason is observable.

## Substitute assessment

For every serious substitute, distinguish four separate facts:

1. capability: which target workflow steps it performs;
2. fit: whether it serves the same ICP, input, required output, and quality bar;
3. friction/economics: price, procurement, setup, and switching cost actually supported by sources;
4. adoption/sufficiency: evidence that target users use it or find it sufficient.

A vendor page can verify current capability or published price; it does not prove adoption, satisfaction, pain, or buyer spend. A user complaint can verify a problem; it does not prove the vendor lacks every workaround.

Classify a substitute record as `contradicts` when it materially performs the proposed job for the target ICP. Do not label it supportive merely because its existence suggests a market. If decisive fit, price, or adoption remains unknown, report the threat as unresolved rather than dismissing it.

A potential killer substitute is one that appears to solve the core job sufficiently for the target ICP with low enough friction/economics to undermine the planned value proposition. The Judge, not this skill, decides Gate 6.

## Evidence discipline

- Open original public pages; search-result snippets are leads only.
- Use one atomic factual observation per record.
- Keep observation separate from interpretation.
- Do not invent a product weakness, user dissatisfaction, price, adoption level, or technical limitation.
- Do not treat an old or unrelated failure as evidence about the current product without explaining the mismatch.
- Attribute evidence only to the ICP shown by the source.
- Use mostly `contradicts` or `neutral` polarity. Record accidental support honestly.
- Keep every raw record `audit_status: PENDING`.

## Outputs

Write only to the assigned `raw/skeptic` directory:

- `evidence.jsonl`;
- `skeptic-case.md` containing:
  1. hypothesis and scope tested;
  2. substitute matrix with capability, ICP/output fit, price/friction, adoption evidence, unknowns, and evidence IDs;
  3. strongest recurrence objection;
  4. strongest WTP objection;
  5. strongest adoption/procurement blocker;
  6. strongest technical/MVP blocker;
  7. evidence sufficient to rebut each objection;
  8. candidate new scopes discovered, explicitly marked `UNVALIDATED`; and
  9. research shortfall and tooling blockers.

Do not issue the official Stage 1 verdict.

## Tool and stopping policy

Use the browser for public research. Do not retrieve web content through terminal, Python, PowerShell, curl, internal Antigravity files, browser cache, or ad-hoc scrapers.

Retry a failed research action at most once. After 3 consecutive research-tool failures, preserve the credible records, document the blocker, and finish partial.

Validate the finished file only with:

```bash
python scripts/validate_evidence.py <idea-path>/raw/skeptic/evidence.jsonl
```

Do not use `python -c`, inline `jsonschema`, or shell parsing. If validation fails, repair only the reported JSONL problem and rerun once. If it still fails, document the structural blocker and stop.
