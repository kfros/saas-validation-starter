# Stage 1 Evidence Audit Summary: Geo Monitoring (v2 Reassessment)

**Idea**: `geo-monitoring`  
**Target Scope**: `GEO-AGENCY-01` (Independent SEO agencies with 2–20 staff serving SMB clients on recurring retainers)  
**Policy Version**: `v2` (SMB Reassessment Policy per `methodology/stage1-policy.json`)  
**Audit Mode**: Bounded Source Review & Reassessment  
**Baseline Reference**: Git commit `3bf758f` (`ideas/geo-monitoring/evidence/evidence.jsonl`)  
**Evaluation Date**: 2026-09-11  
**Audit Role**: Evidence Auditor  

---

## 1. Executive Summary & Status Breakdown

This bounded Stage 1 v2 audit assesses the smallest decisive subset of evidence required to evaluate the v2 policy thresholds (G1 $\ge 5$, G2 $\ge$ MEDIUM, G3 $\ge 3$, G4 $\ge 3$, G5 $\ge$ MEDIUM, G6 no killer substitute) for candidate scope `GEO-AGENCY-01`.

Rather than reopening all 87 baseline records or performing redundant web crawling, this audit evaluated 24 high-impact records across positive, contradictory, and scope-defining categories, preserving 63 records in the unexamined baseline budget.

| Metric | Count | Details |
| :--- | :---: | :--- |
| **Total Baseline Records** | 87 | Preserved at commit `3bf758f` |
| **Audited Bounded Subset** | 24 | Decisive set evaluated in this reassessment |
| **Unexamined Budget Preserved** | 63 | Retained for targeted Stage 2 customer discovery |
| **Retrieval SUCCESS** | 23 | Exact public sources retrieved and verified |
| **Retrieval BLOCKED** | 1 | `geo-wtp-upwork-pr-agency-contract` (Cloudflare Turnstile 403) |
| **Audit Status: VERIFIED** | 20 | Fully verified against source and schema |
| **Audit Status: PARTIALLY_VERIFIED** | 3 | Vendor arithmetic, counterfactual claims, tier mismatches |
| **Audit Status: PENDING** | 1 | Preserved blocked record (Upwork) |
| **Audit Status: REJECTED** | 0 | (0 in this decisive subset; historical rejection preserved in baseline) |

---

## 2. Key Audit Reassessment Findings (Leads 1–5)

### Lead 1: Separating Tool Use from Paid Software Spend
- **Record**: `geo-pain-reddit-arash60-defensive-monthly-client-reporting`
- **Finding**: Practitioner `Arash-60` (Agency SEO Lead) describes using Guzu.ai to establish client baseline rankings across ChatGPT, Gemini, and Perplexity for monthly SEO reports. However, the source provides no evidence of a paid subscription or corporate software expenditure (could be free tier or client-provided).
- **Audit Decision**: Tool usage and monthly reporting pain are verified for G1 and G2. Canonical field `money_signal` was normalized from `saas_spend` to `null` (traceable in `review-log.jsonl` modifications). Excluded from Gate 3 spend count.

### Lead 2: Vendor Marketing Arithmetic vs. Observed Agency Labor
- **Record**: `geo-wtp-blog-agency-manual-hours`
- **Finding**: Author Elsa Ji is a content marketer at Topify (software vendor). The claimed figure of 250 weekly searches (50 keywords $\times$ 5 engines) is vendor marketing arithmetic quoting Superlines, not internal accounting or observed agency staff time.
- **Audit Decision**: Reclassified from `VERIFIED` to `PARTIALLY_VERIFIED` and `OUT_OF_SCOPE`. Excluded from Gate 3 labor count.

### Lead 3: Counterfactual Statements vs. Actual Performed Work
- **Record**: `geo-workflow-12-manual-workaround-labor`
- **Finding**: Stanislava Smiljanic (SORN.AI) stated: *"It would be very manual, with a ton of print screens and manual research of prompts with VPN, Stanislava says of the alternative."* This represents a counterfactual estimation of what work *would* be required without specialized software, not a record of actual manual hours logged by agency staff.
- **Audit Decision**: Reclassified from `VERIFIED` to `PARTIALLY_VERIFIED`. Excluded from Gate 3 labor count.

### Lead 4: Scope Verification (`GEO-AGENCY-01`)
- **Verified In-Scope Agencies (2–20 staff)**:
  - `Typical-Badger1922` (`geo-pain-reddit-typicalbadger-patchwork-stack`)
  - `nothabkuuys` (`geo-pain-reddit-nothabkuuys-small-agency-client-anxiety`)
  - `jjnasty` (`geo-pain-reddit-jjnasty-losing-game-oneoff-audit`)
  - `erickrealz` (`geo-pain-reddit-erickrealz-agency-attribution-impossibility`)
  - `ThirdEyesOfTheWorld` (`geo-pain-reddit-thirdeyesoftheworld-bundled-substitute`)
  - `Arash-60` (`geo-pain-reddit-arash60-defensive-monthly-client-reporting`)
  - `What IF Web` (`geo-workflow-01-whatifweb-profile`, 3–5 staff)
  - `SORN.AI` (`geo-workflow-04-sornai-profile`, `geo-workflow-06-sornai-reporting-cadence`, 2–10 staff)
  - `Butter Marketing` (`geo-workflow-07-butter-marketing-profile`, 2–9 staff)
  - `Clutch Directory Channel` (`geo-workflow-11-reachability-clutch`, directory filter for 2–9 / 10–49 staff)
- **Scope Discipline**: Solo consultants, individual website owners, and anonymous Reddit users without verified agency headcount (`maltelandwehr`, `trustmeimnotnotlying`, `tachichuchi`, `billhartzer`) are classified as `UNKNOWN` scope and strictly excluded from G1–G5 thresholds.

### Lead 5: Substitutes and Technical Feasibility Constraints
- **Incumbent Bundles**: SE Ranking (€109–€235/mo + €59/mo white label) and Semrush ($199–$549/mo + $20/mo) bundle daily AI search tracking into core subscriptions.
- **Pure-Play Trackers**: Peec AI (€205–€675/mo) and Otterly.ai (€189/mo + engine add-ons) price multi-client tiers significantly above SMB willingness to pay.
- **Technical & Economic Barriers**:
  - *Sampling Variance*: Non-zero LLM temperature requires $n=7$ repeats per prompt to achieve standard error $<0.10$ (Jay Sim, arXiv:2604.07585). Naive single checks yield 10%–34% noise.
  - *API Unit Economics*: OpenAI Web Search costs $10–$25 per 1,000 calls. Statistically sound checks across 50 prompts $\times$ 7 repeats $\times$ 4 surfaces cost $14–$35 per client audit in raw API fees alone.
  - *Legal Constraints*: OpenAI Terms of Use (updated Jan 16, 2026) explicitly prohibit programmatic output extraction and anti-bot circumvention, making consumer UI scraping legally and technically fragile.

---

## 3. Potential Gate Eligibility Summary (Input to Stage 1 Judge)

*Note: Per Rules 17–19, the Evidence Auditor does not issue gate verdicts. The following counts summarize audited records satisfying structural eligibility criteria under Policy v2:*

| Gate | Policy v2 Requirement | Audited Eligible Count | Status Indication | Key Eligible Evidence IDs |
| :--- | :--- | :---: | :---: | :--- |
| **G1: Concrete Pain** | $\ge 5$ independent in-scope VERIFIED records | **6** | PASS | `geo-pain-reddit-typicalbadger-patchwork-stack`, `geo-pain-reddit-nothabkuuys-small-agency-client-anxiety`, `geo-pain-reddit-jjnasty-losing-game-oneoff-audit`, `geo-pain-reddit-erickrealz-agency-attribution-impossibility`, `geo-pain-reddit-thirdeyesoftheworld-bundled-substitute`, `geo-pain-reddit-arash60-defensive-monthly-client-reporting` |
| **G2: Recurrence** | $\ge$ MEDIUM confidence, recurring core job | **4** (HIGH) | PASS | `geo-pain-reddit-typicalbadger-patchwork-stack` (weekly), `geo-pain-reddit-arash60-defensive-monthly-client-reporting` (monthly), `geo-workflow-06-sornai-reporting-cadence` (weekly), `geo-pain-reddit-thirdeyesoftheworld-bundled-substitute` (monthly) |
| **G3: Existing Spend / WTP** | $\ge 3$ independent VERIFIED spend/labor records | **1** | UNKNOWN | Counted: `geo-pain-reddit-typicalbadger-patchwork-stack` (`employee_time`). Excluded: `geo-wtp-blog-agency-manual-hours` (PARTIALLY_VERIFIED), `geo-workflow-12-manual-workaround-labor` (PARTIALLY_VERIFIED), `geo-wtp-upwork-pr-agency-contract` (BLOCKED), `geo-wtp-reddit-peec-usage` (UNKNOWN scope), `geo-pain-reddit-arash60-defensive-monthly-client-reporting` (money_signal null) |
| **G4: Repeatable Gap** | $\ge 3$ independent records, cluster size $\ge 3$ | **5** (Cluster: 5) | PASS | Cluster `client_reporting_rework_under_volatility`: `geo-pain-reddit-typicalbadger-patchwork-stack`, `geo-pain-reddit-arash60-defensive-monthly-client-reporting`, `geo-pain-reddit-nothabkuuys-small-agency-client-anxiety`, `geo-pain-reddit-erickrealz-agency-attribution-impossibility`, `geo-pain-reddit-jjnasty-losing-game-oneoff-audit` |
| **G5: ICP Reachability** | $\ge$ MEDIUM confidence, concrete channel | **4** (HIGH) | PASS | `geo-workflow-11-reachability-clutch` (searchable directory with 2–9 and 10–49 employee filters), supported by profiles `geo-workflow-01-whatifweb-profile`, `geo-workflow-04-sornai-profile`, `geo-workflow-07-butter-marketing-profile` |
| **G6: No Killer Substitute** | Verified substitute context, no killer | **8** context | PASS | Verified context across SE Ranking, Semrush, Otterly, Peec, OpenAI pricing/ToS, and sampling variance. No single killer substitute, but significant bundling and margin constraints |

---

## 4. Unexamined Evidence Budget Preserved

The remaining 63 records in `ideas/geo-monitoring/evidence/evidence.jsonl` (commit `3bf758f`) were not modified, deleted, or fabricated. In accordance with Rules 25–31 and bounded reassessment guidelines:
1. No synthetic records were introduced.
2. The unexamined budget remains available if Stage 2 customer discovery requires broader scope exploration.
3. The dataset is sealed and cryptographically verifiable via `snapshot.json`.
