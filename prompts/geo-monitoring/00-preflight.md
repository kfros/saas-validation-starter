# GEO preflight — no research

Fresh conversation; no browser needed. Paste:

```text
Perform read-only setup checks for ideas/geo-monitoring. This is not research.
Read its README.md, RUNBOOK.md, hypothesis.yaml, research-brief.md and research-protocol.md, the existing .agent/rules/validation-rules.md, canonical methodology and the seven existing .agent/skills/*/SKILL.md files.

Do not invoke old root-level deck prompts. Do not modify shared skills or rules, methodology, scripts, deck files, or the hypothesis. Confirm the project root contains .agent/skills (singular .agent). If slash skills are not detected, report that for the human; do not install or rename skills.

The agency/reporting scope is an unvalidated working assumption. Summarize its buyer, job, output, exclusion of content generation, and the $100/agency/month target as an assumption. Verify the human has reviewed that scope before research is launched; do not treat a model's preference as customer evidence.

The sole allowed terminal command is:
python scripts/check_geo_stage1.py preflight

No python -c, inline code, package installation, cache/internal Antigravity access, outside-workspace reads, browser experiments or scraping. If the command fails, report the exact error; do not repair shared files or invent a fallback.

Write only ideas/geo-monitoring/setup/preflight.md. Include: inputs found, scope summary, command/result, missing capabilities or conflicts, and whether setup is ready. No evidence records, gate decision, or auto-launch of research. End after preflight and wait for the human to launch the separate research conversations.
```
