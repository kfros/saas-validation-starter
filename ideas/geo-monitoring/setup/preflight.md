# Preflight Setup Check — GEO Monitoring (Stage 1)

**Date**: 2026-09-08  
**Idea ID**: `geo-monitoring`  
**Status**: SETUP READY (No research initiated; no evidence or market validation implied)

---

## 1. Inputs Found and Verified

All required configuration, protocol, methodology, and skill files were located and read directly:

### Target Idea Configuration (`ideas/geo-monitoring/`)
- `README.md` — Status unvalidated; run guidance and return deliverables defined.
- `RUNBOOK.md` — Step-by-step operating instructions for preflight, research tracks A–E, auditor, and judge.
- `hypothesis.yaml` — Idea metadata (`geo-monitoring`), scope `GEO-AGENCY-01`, core job, constraints, falsification criteria, and core unknowns.
- `research-brief.md` — Track questions, non-advocacy mandate, and GEO-specific traps (prompt sampling, API vs UI, mentions vs referrals).
- `research-protocol.md` — Execution contract, sandbox/tool boundaries, atomic record rules, checkpoint commands, and audit/judge contracts.
- `source-leads.md` — Unvalidated initial discovery leads.

### Workspace Rules and Methodology
- `.agent/rules/validation-rules.md` — 31 rules governing evidence standards, tool limits, isolation, and anti-hallucination policies.
- `methodology/evidence-schema.json` — Strict JSON schema for evidence records.
- `methodology/evidence-standard.md` — Atomicity, observation vs. interpretation, source tiers (A/B/C), WTP hierarchy, recurrence, and negative evidence mandates.
- `methodology/stage1-gates.md` — Quantitative and qualitative thresholds for G1 through G6.
- `methodology/scoring.md` — Scorecard format and dimension scoring (0–5 integer scale).

### Shared Skills (`.agent/skills/` — singular `.agent`)
The workspace root contains the canonical `.agent/skills` directory. All seven skills are present and detected:
1. `evidence-audit` (`.agent/skills/evidence-audit/SKILL.md`)
2. `market-research` (`.agent/skills/market-research/SKILL.md`)
3. `pain-mining` (`.agent/skills/pain-mining/SKILL.md`)
4. `skeptic-research` (`.agent/skills/skeptic-research/SKILL.md`)
5. `stage1-judge` (`.agent/skills/stage1-judge/SKILL.md`)
6. `workflow-mapping` (`.agent/skills/workflow-mapping/SKILL.md`)
7. `wtp-research` (`.agent/skills/wtp-research/SKILL.md`)

---

## 2. Working Assumption & Scope Summary (`GEO-AGENCY-01`)

> [!WARNING]
> **UNVALIDATED WORKING ASSUMPTION**: The target scope defined below is a working hypothesis selected for testing, not an empirical market finding or customer truth. A model's preference or convenience is not customer evidence. The human operator must review and confirm this scope before launching any research conversation.

- **Primary ICP / Target Organization**: Independent SEO agency with 2–20 staff serving SMB clients on recurring engagements, delivering English deliverables (geography: English-serving agencies; do not infer country from language).
- **Target Buyer**: Owner, agency managing director, or head of SEO with purchasing authority.
- **Operator**: SEO specialist or account manager tasked with recurring client reporting.
- **Core Job**:
  - *Trigger*: Recurring monthly/periodic client review or suspected material visibility fluctuation.
  - *Inputs*: Client brand/domain, named competitors, agreed prompt set, specified search/answer surfaces, locale context.
  - *Workflow*: Capture observations across surfaces -> inspect citations/mentions -> filter noise/sampling variance -> generate report tied to actionable client advice.
- **Proposed Output**: Inspectable, defensible per-client visibility/change report (exact format is an unknown).
- **Proposed Wedge**: Evidence-backed recurring client reporting with noise-aware change review. Differentiation is unvalidated and not assumed unique.
- **Explicit Scope Exclusions**:
  - Autonomous SEO/GEO content generation or automated publishing.
  - In-house enterprise marketing teams or procurement-heavy buyers.
  - Direct-to-SMB brand-owner tools.
  - Solo freelancers/consultants automatically pooled as agency peers.
  - Traditional rank tracking / social listening lacking AI answer workflows.
  - Guaranteed rankings, referrals, citations, or traffic uplift.
- **Target Economics Assumption**: Target eventual ARPU of \$100/agency/month minimum on an agency account billing model. This is an internal founder viability hurdle, **not** evidenced willingness to pay.

---

## 3. Terminal Preflight Command and Execution Result

Sole authorized command executed from project root:
```bash
python scripts/check_geo_stage1.py preflight
```

**Execution Result**:
- Exit code: `0`
- Output:
```text
Preflight files/schema ready. No evidence or market validation implied.
OK: requested structural checks passed. This is not a market PASS.
```

---

## 4. Missing Capabilities and Conflicts

- **Slash Skills Detection**: Verified. The 7 core validation skills in `.agent/skills/` are recognized by Antigravity and available for slash invocation (`/market-research`, `/pain-mining`, `/wtp-research`, `/workflow-mapping`, `/skeptic-research`, `/evidence-audit`, `/stage1-judge`).
- **Path and Tool Conflicts**: None. The directory structure conforms strictly to the single `.agent` convention. Older root-level deck prompts under `prompts/10-run-market.md` etc. remain intact for deck automation and were NOT touched or invoked; GEO-specific prompts under `prompts/geo-monitoring/` are designated for this run.
- **Shared Code/Rules Integrity**: Preserved without modification. No rules, skills, methodology files, scripts, or hypothesis files were altered.

---

## 5. Setup Readiness Verdict

**SETUP IS READY.**

The environment, files, and schemas are structurally sound. Preflight completion does **not** constitute research, market validation, or evidence collection.

### Next Steps (Human Action Required)
Do not auto-launch research in this conversation. The human operator should review the scope assumptions above and launch dedicated research conversations according to [RUNBOOK.md](../RUNBOOK.md):
1. **Track A (Market)**: New conversation with `/browser` + `/market-research`, using `prompts/geo-monitoring/10-run-market.md`
2. **Track B (Pain)**: New conversation with `/browser` + `/pain-mining`, using `prompts/geo-monitoring/11-run-pain.md`
3. **Track C (WTP)**: New conversation with `/browser` + `/wtp-research`, using `prompts/geo-monitoring/12-run-wtp.md`
4. **Track D (Workflow)**: New conversation with `/browser` + `/workflow-mapping`, using `prompts/geo-monitoring/13-run-workflow.md`
5. **Track E (Skeptic)**: New conversation with `/browser` + `/skeptic-research`, using `prompts/geo-monitoring/14-run-skeptic.md`
