# Bootstrap prompt

Use this only when recreating the framework from scratch. The supplied starter pack already contains the framework.

```text
Create a reusable Stage 1 evidence-first SaaS validation framework in this workspace.

Do not perform market research yet.

Create:
- methodology/evidence-standard.md
- methodology/evidence-schema.json
- methodology/stage1-gates.md
- methodology/scoring.md
- .agents/rules/validation-rules.md
- workspace Agent Skills under .agents/skills/ for:
  1. market-research
  2. pain-mining
  3. wtp-research
  4. workflow-mapping
  5. skeptic-research
  6. evidence-audit
  7. stage1-judge
- prompts for invoking those roles
- directories for raw evidence, audited evidence and output.

Requirements:
- Facts, observations and interpretations must be separated.
- Every factual evidence record must carry a source URL.
- Search-result snippets are not evidence.
- Unknown must remain UNKNOWN.
- Negative/disconfirming evidence is mandatory.
- Evidence records must have stable independence keys for deduplication.
- The Auditor may verify only already-recorded sources and may not find replacement evidence.
- The Judge may use only VERIFIED evidence and may not browse or add information from general knowledge.
- Gate thresholds must be fixed before results are observed.
- Avoid unnecessary application infrastructure. Use Markdown + JSONL + small validation scripts.

After creating the framework, inspect it for contradictions between Rules, Skills, schema and gates. Fix structural inconsistencies only. Do not begin Stage 1 research.
```
