# Multi-brand Stage 1 Judge

Fresh conversation, High. Invoke `/stage1-judge`, **without `/browser`**, then paste:

```text
Judge Stage 1 for ideas/multi-brand-content, single scope MULTIBRAND-OPERATOR-01.
Read stage1-judge SKILL.md; the idea's hypothesis.yaml, research-brief.md, research-protocol.md and audit-checklist.md; methodology/stage1-gates.md and scoring.md; and evidence/evidence.jsonl, scope-map.json, audit-summary.md and high-impact-review.md.

Run the audit checker first. On an error return it to the Auditor; do not edit evidence.
No browsing/search/URLs/new sources, internal Antigravity/cache/outside-workspace reads or general-knowledge gap filling. Write only ideas/multi-brand-content/output/.

Apply the fixed canonical gates and exact scorecard contract from research-protocol.md. Use VERIFIED direct observations. G1–G5 counted and decisive contradictory IDs must be IN_SCOPE; check the identity linkage, not just the label. Count one underlying provider independence key per gate. Every counted ID needs a direct-support reason. Report provider-form coverage and explain whether the same job and buying context hold across SOLO/AGENCY cases. Do not combine unrelated freelancer and agency signals to pass.

G3 counts only eligible revealed behavior/material labor under paid_tool_or_pilot, internal_labor and outsourced_labor. Do not count prices, unawarded budgets, stated intent, free use, hypothetical savings or entire retainers/salaries. Real production labor establishes effort, not proven willingness to buy our software. Apply audit-checklist.md before accepting any decisive classification.

G6 separates current capability, same-job/output fit, effective workload price/switching friction and observed sufficiency. Existing stacks may be sufficient without being one product. Product existence does not prove monopoly; unresolved substitutes are UNKNOWN. Do not infer refusal to pay for internal tools from the absence of a separate client invoice line. Technical, editable-output, cost and buyer questions cannot all be hidden in one interview condition.

Produce only:
- ideas/multi-brand-content/output/stage1-report.md
- ideas/multi-brand-content/output/scorecard.json

Copy dataset_summary exactly from DATASET_SUMMARY printed by the checker. Include all ten canonical integer dimension scores, complete gate IDs/reasons/exclusions, provider_form_breakdown, G3 normalized category breakdown and G4 clusters as specified. Every report count must agree with scorecard and audited data. Summed scores cannot override gates.

PASS: all six gates PASS. CONDITIONAL PASS: five PASS and exactly one genuinely interview-answerable UNKNOWN. FAIL: a failed gate with strong VERIFIED contradiction, not merely missing evidence. Otherwise INSUFFICIENT EVIDENCE when evidence is inadequate. Any materially changed audience/job/output is UNVALIDATED. stage2_authorized is a recommendation for independent human review, not permission to launch outreach or development.

Exact terminal allowlist, replacing older skill commands:
python scripts/check_multibrand_stage1.py audit
python scripts/check_multibrand_stage1.py judge

No python -c, python stdin, inline parsing, helper scripts, packages or shell fallbacks. One repair of your own structural output and one rerun maximum. If still blocked, record the blocker and do not claim a validated completed handoff.

Finish with verdict, decisive reasons, unknowns, actual validation result and the four handoff paths (report, scorecard, audited evidence, high-impact review). Do not start Stage 2 or change ChillPup.
```
