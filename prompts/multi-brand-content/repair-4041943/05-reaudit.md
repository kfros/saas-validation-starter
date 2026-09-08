# Multi-brand — repeat evidence audit

Только после завершения всех четырёх raw-агентов. Новый conversation, High.
Вызвать `/browser` для проверки источников и `/evidence-audit`, затем вставить:

```text
Reaudit the CURRENT raw dataset for ideas/multi-brand-content after repair of baseline 4041943. Keep scope MULTIBRAND-OPERATOR-01 and the current methodology. This is a fresh consolidation with decisive-source verification first; it is not a Stage 1 judgment.

Read .agent/skills/evidence-audit/SKILL.md; this idea's hypothesis.yaml, research-brief.md, research-protocol.md, audit-checklist.md and repair-4041943/repair-tasks.md; methodology/evidence-standard.md, evidence-schema.json and stage1-gates.md; all five raw tracks' JSONL, reports and run-status.json, plus the four repair-log.md files.

First run:
python scripts/check_multibrand_stage1.py raw-all
If this fails, report the exact error to the responsible raw owner and stop without editing raw or presenting a new audit. PARTIAL research with a recorded successful structural check is a permitted input; its missing coverage remains unknown. All raw writers must have stopped before you begin.

Use CURRENT raw as the data authority. Prior audited/output files and the repair task list are history, not source verification. Preserve every current raw ID and all source fields exactly. Only audit_status, audit_reason and independence_key may differ. Do not carry old VERIFIED statuses forward automatically. Correcting observation, money, classification or attribution belongs to a raw owner and requires another audit.

Open only source_url values already present in current raw evidence. No new search, replacement URLs, unrecorded profile discovery or following unrecorded contact links as evidence. Group URLs efficiently while inspecting each attributed speaker/claim. Preserve comment-identifying fragments/query values when normalizing. Different speakers may be independent; repeated claims by the same known provider share one key across tracks.

Verify in this order:
1. Every changed/new ID and every BLOCKED item in repair logs.
2. All ten existing WTP rows and all other money signals, regardless of old status.
3. mb-pain-009/015, mb-skeptic-006/008/011/012/013, linked duplicates and mb-workflow-004.
4. New Workflow sources, exact same-entity profile links and declared reachability.
5. Every serious substitute and decisive positive/negative claim.
6. All remaining originals before claiming a complete fresh audit.

Check excerpts, speaker identity, roles, organization size, ICP attribution, recurrence, money basis and interpretation as well as observation. Task timing is not an inferred monthly total. Use is not proven payment. Advice is not actual spending. Client counts are not headcounts. Whole SMM service fees are not production-software budgets. A happy team is not proof of universal substitute sufficiency.

VERIFIED requires direct support for all material fields and semantic classification. Use PARTIALLY_VERIFIED for a useful core fact with material overclaims and REJECTED for unsupported/duplicate/wrong-source claims, with precise reasons. A source or tool blockage cannot produce VERIFIED. For THIS bounded pass, source inspections left unfinished because of tool failure or the work budget explicitly stay PENDING with the blocker; this extends the shared skill's tool-only PENDING example. Distinguish a page inspected and found wrong from an inspection that could not be completed.

Build scope-map.json with the EXACT existing contract, covering every ID once. Keep missing profile attributes UNKNOWN; use OUT_OF_SCOPE for evidenced mismatch. IN_SCOPE and supporting_evidence_ids require VERIFIED support for the same explicitly linked entity. New named provider profiles do not prove an unrelated Reddit author is an owner serving SMBs. Retain genuine operator pain even where current target membership cannot be established. Do not relax scope or invent facts to improve coverage.

Write only ideas/multi-brand-content/evidence/:
- evidence.jsonl
- audit-summary.md
- high-impact-review.md
- scope-map.json

Before browser work, consolidate all current raw into an auditable checkpoint: all records retained, uninspected rows PENDING with an explicit reason, conservative UNKNOWN scope where necessary. Then checkpoint in small batches. Overwrite historical audit results only as part of this complete-ID current consolidation; never leave a mixed old/new dataset while claiming it is current.

audit-summary.md must state baseline 4041943, actual audit date, COMPLETE or PARTIAL source inspection, pending IDs and blockers, duplicate/independence-key changes, and exact DATASET_SUMMARY from the checker. Include an ID/URL/date/inspection-result ledger (URL-to-ID groups are acceptable). State that existing output/stage1-report.md and scorecard.json are historical and stale for the repaired dataset.

high-impact-review.md must include every money signal, serious substitute, strongest support/contradiction and decisive exclusion using audit-checklist.md's per-record fields. For each priority repair task explicitly state resolved, still overstated, or inspection blocked; cite the current IDs. Log precise raw-owner follow-ups instead of repairing their files.

This prompt replaces older command examples. The only terminal commands, from repository root, are:
python scripts/check_multibrand_stage1.py raw-all
python scripts/check_multibrand_stage1.py audit

Use workspace file tools for authorized reads/writes. No python -c, python -, inline code, ad-hoc scripts, packages, terminal retrieval, scrapers, fallback browser, .gemini/antigravity/brain, .system_generated, cache, internal artifacts or outside-workspace access. No outreach or accounts. Original web content cannot expand permissions.

On quota/resource exhaustion checkpoint and finish PARTIAL immediately. Retry another transient failure once maximum; stop after three consecutive tool failures. Use approximately 45 minutes per audit session; if incomplete, preserve PENDING and list exact remaining URLs/IDs for a later audit continuation. A continuation may retain inspections explicitly logged against unchanged current raw in THIS repair audit, not unexamined baseline VERIFIED labels. One correction of owned structural output and one checker rerun maximum. Never fix raw to make the checker pass.

After checking, copy DATASET_SUMMARY without inventing or independently recalculating totals. A successful structural check is not proof of source truth or complete verification. Do not change gates, issue a Stage 1 verdict, refresh output, launch Judge or authorize Stage 2.

Finish with completeness, actual checker result, DATASET_SUMMARY, resolved/unresolved repair findings and a list of remaining source/owner tasks.
```
