# GEO Stage 1 — workflow

Fresh conversation. Invoke `/browser` and `/workflow-mapping`, then paste the block below.

```text
Run Stage 1 workflow research for ideas/geo-monitoring, scope GEO-AGENCY-01.

Before researching, read:
- .agent/skills/workflow-mapping/SKILL.md
- ideas/geo-monitoring/hypothesis.yaml
- ideas/geo-monitoring/research-brief.md
- ideas/geo-monitoring/research-protocol.md
- ideas/geo-monitoring/source-leads.md
- methodology/evidence-standard.md
- methodology/evidence-schema.json
- methodology/stage1-gates.md
Inspect existing files in your own raw/workflow/ directory. Preserve valid records and IDs; avoid duplicate underlying claims. Do not read another research track's output during discovery.

Map GEO-AGENCY-01 only: actual operator, budget owner, trigger, inputs, observation surface, review steps, client deliverable, action after the report, recurrence and current alternatives. Research reachability explicitly: original public agency/team/contact or directory entries linking to identifiable matching agencies and a legitimate discovery/contact route. Include 3-5 illustrative examples if available; this is a coverage guide, not a gate or a full Stage 2 lead list. Do not contact anyone, harvest personal emails, or infer authority/size from job titles. Where useful, create separate atomic company-profile records for later explicit same-entity scope linkage. Other ICPs stay OUT_OF_SCOPE/UNVALIDATED leads. No Stage 1 verdict.

Write only to ideas/geo-monitoring/raw/workflow/:
- evidence.jsonl
- workflow-map.md and icp-candidates.md
- run-status.json following research-protocol.md
All raw records remain PENDING. Use stable geo-workflow- ID prefixes and idea geo-monitoring. Do not seed evidence from the hypothesis or lead list. No sample records; an actually empty run has an empty JSONL plus an honest report.

Use approved browser/web tools to open original public pages. No terminal web retrieval, scraping, internal Antigravity files, .gemini/antigravity/brain, .system_generated, browser cache or outside-workspace files. No python -c, python stdin, inline code, ad-hoc scripts, package installs, signups, payments, outreach or live model probes.
On quota/resource exhaustion stop and finish partial; otherwise retry a transient failed action at most once, and stop after three consecutive tool failures. Stop at saturation or the 45-minute research budget; never chase a numeric quota. Checkpoint each small batch.

For this run the exact terminal allowlist below REPLACES older example commands in the skill. Use workspace file tools for edits. Do not modify scripts, methodology, hypothesis, shared skills or any other output directory.
Allowed command from repository root:
python scripts/check_geo_stage1.py workflow

Write run-status.json with validation NOT_RUN before checking; set it to PASS or FAIL from the actual result. One structural repair and one rerun maximum. On missing tool, permission denial or repeated validation failure preserve output, document the blocker and end partial without fallback commands. Report counts, scope coverage, blockers, validation result and next unfinished task. Do not decide PASS/FAIL or begin Stage 2.
```
