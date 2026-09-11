# Stage 1 v2 SMB Reassessment Runbook

This operational runbook governs the five-conversation sequential reassessment of SMB product hypotheses (`geo-monitoring` and `deck-automation`) against the calibrated `v2` Stage 1 policy.

Each step executes in an **isolated fresh conversation** on the same local git repository (`stage1-v2-setup` branch). Do not merge conversations or skip steps.

---

## Overview of Conversations

| # | Step | Conversation Role | Slash Skills | Target Directory | Primary Checker |
|---|---|---|---|---|---|
| 1 | **Engineering Setup** *(Current)* | Tooling & contracts | None (Engineering) | `scripts/`, `methodology/`, `prompts/` | `python -m unittest discover` |
| 2 | **GEO Source Review** | Auditor / Reviewer | `/browser`, `/evidence-audit` | `ideas/geo-monitoring/reassessment-v2/evidence/` | `python scripts/check_geo_stage1.py audit --policy v2` |
| 3 | **Deck Source Review** | Auditor / Reviewer | `/browser`, `/evidence-audit` | `ideas/deck-automation/reassessment-v2/evidence/` | `python scripts/check_deck_stage1.py audit --policy v2` |
| 4 | **GEO Judge** | Stage 1 Judge | `/stage1-judge` **(NO browser)** | `ideas/geo-monitoring/reassessment-v2/output/` | `python scripts/check_geo_stage1.py judge --policy v2` |
| 5 | **Deck Judge** | Stage 1 Judge | `/stage1-judge` **(NO browser)** | `ideas/deck-automation/reassessment-v2/output/` | `python scripts/check_deck_stage1.py judge --policy v2` |

---

## Step 1: Engineering Setup (Completed)
- **Status**: Complete on branch `stage1-v2-setup`.
- **Deliverables**:
  - `methodology/stage1-policy.json` (canonical v1 and v2 definitions)
  - `methodology/stage1-gates.md` and `methodology/scoring.md`
  - `.agent/skills/stage1-judge/SKILL.md`
  - `scripts/historical_manifest_3bf758f.json`
  - `scripts/stage1_policy.py`, `scripts/check_geo_stage1.py`, `scripts/check_deck_stage1.py`, `scripts/check_multibrand_stage1.py`
  - `scripts/test_stage1_v2_policy.py`
  - `prompts/reassessment-v2/` (all launch prompts and this runbook).
- **Verification**: `python -m unittest discover -s scripts -p "test_*.py"` (128 tests in test suite).

---

## Step 2: GEO Targeted Source Review
- **Conversation Setup**: New conversation. High reasoning. Enable `/browser` and invoke `/evidence-audit`.
- **Launch Action**: Copy and paste the entire prompt from [prompts/reassessment-v2/10-review-geo.md](10-review-geo.md).
- **Write Directory**: `ideas/geo-monitoring/reassessment-v2/evidence/`
- **Supported Terminal Commands**:
  ```bash
  python scripts/seal_v2_snapshot.py --idea geo-monitoring --snapshot-id snap-geo-v2-001
  python scripts/check_geo_stage1.py audit --policy v2
  ```
- **Stopping Rules**:
  - Open public sources in small batches of at most 5 records.
  - On HTTP 429, quota limit, or inaccessible sources: allow at most one ordinary retry. Record inaccessible pages as blocked.
  - After 3 consecutive tool failures, stop discovery work for that run.
  - Finding too little eligible material within the bounded review budget is a legitimate stopping outcome (`INSUFFICIENT EVIDENCE`).
- **Deliverables to Bring Back**:
  - `ideas/geo-monitoring/reassessment-v2/evidence/evidence.jsonl`
  - `ideas/geo-monitoring/reassessment-v2/evidence/scope-map.json`
  - `ideas/geo-monitoring/reassessment-v2/evidence/review-log.jsonl`
  - `ideas/geo-monitoring/reassessment-v2/evidence/audit-summary.md`
  - `ideas/geo-monitoring/reassessment-v2/evidence/high-impact-review.md`
  - `ideas/geo-monitoring/reassessment-v2/evidence/snapshot.json`

---

## Step 3: Deck Targeted Source Review
- **Conversation Setup**: New conversation. High reasoning. Enable `/browser` and invoke `/evidence-audit`.
- **Launch Action**: Copy and paste the entire prompt from [prompts/reassessment-v2/11-review-deck.md](11-review-deck.md).
- **Write Directory**: `ideas/deck-automation/reassessment-v2/evidence/`
- **Supported Terminal Commands**:
  ```bash
  python scripts/seal_v2_snapshot.py --idea deck-automation --snapshot-id snap-deck-v2-001
  python scripts/check_deck_stage1.py audit --policy v2
  ```
- **Scope Discipline**: Focus review on the single most defensible declared candidate segment (e.g. boutique consultancies or agencies producing client decks). Do not pool across segments.
- **Stopping Rules**: Same tool failure policy (max 1 retry, stop after 3 consecutive failures).
- **Deliverables to Bring Back**:
  - `ideas/deck-automation/reassessment-v2/evidence/evidence.jsonl`
  - `ideas/deck-automation/reassessment-v2/evidence/scope-map.json`
  - `ideas/deck-automation/reassessment-v2/evidence/review-log.jsonl`
  - `ideas/deck-automation/reassessment-v2/evidence/audit-summary.md`
  - `ideas/deck-automation/reassessment-v2/evidence/high-impact-review.md`
  - `ideas/deck-automation/reassessment-v2/evidence/snapshot.json`

---

## Step 4: GEO Stage 1 Judge
- **Conversation Setup**: Fresh conversation. High reasoning. **DO NOT enable `/browser`**. Invoke `/stage1-judge`.
- **Launch Action**: Copy and paste the entire prompt from [prompts/reassessment-v2/20-judge-geo.md](20-judge-geo.md).
- **Write Directory**: `ideas/geo-monitoring/reassessment-v2/output/`
- **Supported Terminal Command**:
  ```bash
  python scripts/check_geo_stage1.py judge --policy v2
  ```
- **Stopping Rules**:
  - The Judge consumes only the audited v2 snapshot; no browsing, web search, or general knowledge.
  - Evaluates G1..G6 against v2 policy thresholds.
  - CONDITIONAL PASS requires G1 and G5 PASS, 0 FAIL, condition objects with `resolution_method: INTERVIEW`, and `discovery_plan.interview_cap` $\le 8$.
  - Unresolved technical blockers (e.g. sampling variance, scraping restrictions) prevent CONDITIONAL PASS.
- **Deliverables to Bring Back**:
  - `ideas/geo-monitoring/reassessment-v2/output/stage1-report.md`
  - `ideas/geo-monitoring/reassessment-v2/output/scorecard.json`

---

## Step 5: Deck Stage 1 Judge
- **Conversation Setup**: Fresh conversation. High reasoning. **DO NOT enable `/browser`**. Invoke `/stage1-judge`.
- **Launch Action**: Copy and paste the entire prompt from [prompts/reassessment-v2/21-judge-deck.md](21-judge-deck.md).
- **Write Directory**: `ideas/deck-automation/reassessment-v2/output/`
- **Supported Terminal Command**:
  ```bash
  python scripts/check_deck_stage1.py judge --policy v2
  ```
- **Scope Discipline**: Candidate ICPs assessed individually without cross-segment pooling.
- **Stopping Rules**: Same hard boundaries as GEO Judge.
- **Deliverables to Bring Back**:
  - `ideas/deck-automation/reassessment-v2/output/stage1-report.md`
  - `ideas/deck-automation/reassessment-v2/output/scorecard.json`

---

## Governance & Interpretation Rules

1. **Structural Check vs Market Truth**: Passing checker commands verifies schema contracts, hash integrity, and count arithmetic. It does NOT verify market desirability or guarantee founder success.
2. **Admission vs Development**: `stage2_authorized: true` and `recommended_next_action: LIMITED_CUSTOMER_DISCOVERY` authorize *only* up to 8 discovery interviews with qualified respondents. They do NOT authorize product engineering, hiring, or mass outbound campaigns.
3. **Immutability of Historical Evidence**: Historical directories (`ideas/*/raw/`, `ideas/*/evidence/`, `ideas/*/output/`) are frozen and checked against `scripts/historical_manifest_3bf758f.json`.
4. **Stopping on Inconclusive Evidence**: A bounded `INSUFFICIENT EVIDENCE` result is valid and expected when evidence remains sparse. Never enter infinite repair loops to force a passing verdict.
