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

This bounded Stage 1 v2 audit assesses the smallest decisive subset of evidence required to evaluate policy v2 structural criteria for candidate scope `GEO-AGENCY-01`.

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
- **Audit Decision**: Tool usage and monthly reporting are verified, but canonical field `money_signal` was normalized from `saas_spend` to `null` (traceable in `review-log.jsonl` modifications). Excluded from Gate 3 spend count.

### Lead 2: Vendor Marketing Arithmetic vs. Observed Agency Labor
- **Record**: `geo-wtp-blog-agency-manual-hours`
- **Finding**: Author Elsa Ji is a content marketer at Topify (software vendor). The claimed figure of 250 weekly searches (50 keywords $\times$ 5 engines) is vendor marketing arithmetic quoting Superlines, not internal accounting or observed agency staff time.
- **Audit Decision**: Reclassified from `VERIFIED` to `PARTIALLY_VERIFIED` and `OUT_OF_SCOPE`. Excluded from Gate 3 labor count.

### Lead 3: Counterfactual Statements vs. Actual Performed Work
- **Record**: `geo-workflow-12-manual-workaround-labor`
- **Finding**: Stanislava Smiljanic (SORN.AI) stated: *"It would be very manual, with a ton of print screens and manual research of prompts with VPN, Stanislava says of the alternative."* This represents a counterfactual estimation of what work *would* be required without specialized software, not a record of actual manual hours logged by agency staff.
- **Audit Decision**: Reclassified from `VERIFIED` to `PARTIALLY_VERIFIED`. Excluded from Gate 3 labor count.

### Lead 4: Scope Discipline & Verification (`GEO-AGENCY-01`)
- **Strict Scope Definition**: Independent SEO agencies with 2–20 staff serving SMB clients on recurring retainers. Under repository rules, references to "clients", "our clients", "smaller agency", contracts, or retainers alone do not establish full scope without explicit proof of both 2–20 staff and SMB clients.
- **Verified In-Scope Agencies**:
  - `Butter Marketing` (`geo-workflow-07-butter-marketing-profile`, 2–9 staff verified on Clutch directory)
  - `Clutch Directory Channel` (`geo-workflow-11-reachability-clutch`, public directory filter specifically segmenting 2–9 and 10–49 employee agencies)
- **Reclassified to UNKNOWN Scope (Unverified Headcount or Entity Structure)**:
  - `Typical-Badger1922` (`geo-pain-reddit-typicalbadger-patchwork-stack`): reports small agency operations, but source lacks explicit headcount proof (2–20 staff).
  - `nothabkuuys` (`geo-pain-reddit-nothabkuuys-small-agency-client-anxiety`): mentions smaller agency, but headcount unverified.
  - `jjnasty` (`geo-pain-reddit-jjnasty-losing-game-oneoff-audit`): agency strategist role without agency headcount verification.
  - `erickrealz` (`geo-pain-reddit-erickrealz-agency-attribution-impossibility`): agency SEO specialist role without headcount verification.
  - `ThirdEyesOfTheWorld` (`geo-pain-reddit-thirdeyesoftheworld-bundled-substitute`): agency owner role without headcount verification.
  - `Arash-60` (`geo-pain-reddit-arash60-defensive-monthly-client-reporting`): agency SEO lead role without headcount verification.
  - `What IF Web` (`geo-workflow-01-whatifweb-profile`): cited blog URL confirms studio services, but does not state team size (3–5 staff).
  - `SORN.AI` (`geo-workflow-04-sornai-profile`, `geo-workflow-06-sornai-reporting-cadence`): cited homepage/case study does not state team size (2–10 staff).
  - `maltelandwehr` (`geo-wtp-reddit-peec-usage`): practitioner comment without verified agency headcount.
  - `UK PR Agency` (`geo-wtp-upwork-pr-agency-contract`): retrieval blocked; agency headcount unverified.

### Lead 5: Substitutes and Technical Feasibility Constraints
- **Incumbent Bundles**: SE Ranking (€109–€235/mo + €59/mo white label) and Semrush ($199–$549/mo + $20/mo) bundle daily AI search tracking into core subscriptions.
- **Pure-Play Trackers**: Peec AI (€205–€675/mo) and Otterly.ai (€189/mo + engine add-ons) price multi-client tiers significantly above SMB willingness to pay.
- **Technical & Economic Barriers**:
  - *Sampling Variance*: Non-zero LLM temperature requires $n=7$ repeats per prompt to achieve standard error $<0.10$ (Jay Sim, arXiv:2604.07585). Naive single checks yield 10%–34% noise.
  - *API Unit Economics*: OpenAI Web Search costs $10–$25 per 1,000 calls. Statistically sound checks across 50 prompts $\times$ 7 repeats $\times$ 4 surfaces cost $14–$35 per client audit in raw API fees alone.
  - *Legal Constraints*: OpenAI Terms of Use (updated Jan 16, 2026) explicitly prohibit programmatic output extraction and anti-bot circumvention, making consumer UI scraping legally and technically fragile.
- **Substitute Uncertainty**: Whether bundled offerings from SE Ranking, Semrush, or manual workflows are a sufficient substitute for `GEO-AGENCY-01` remains materially unresolved and is left for Stage 1 Judge evaluation.

---

## 3. Potential Gate Eligibility Summary (Input to Stage 1 Judge)

*Note: Per Rules 17–20, the Evidence Auditor does not issue gate verdicts or recommend decisions (PASS, CONDITIONAL PASS, FAIL). The following counts summarize audited records satisfying structural eligibility criteria under Policy v2:*

| Gate | Policy v2 Structural Rule | Audited Eligible Count | Audited In-Scope Records | Notes on Eligibility & Exclusions |
| :--- | :--- | :---: | :--- | :--- |
| **G1: Concrete Pain** | $\ge 5$ independent in-scope VERIFIED records | **0** in-scope | None | 6 pain records verified (`Typical-Badger1922`, `nothabkuuys`, `jjnasty`, `erickrealz`, `ThirdEyesOfTheWorld`, `Arash-60`), but all 6 lack explicit headcount verification and are classified UNKNOWN scope. |
| **G2: Recurrence** | $\ge$ MEDIUM confidence, recurring core job | **0** in-scope | None | Cadence verified in `Typical-Badger1922` (weekly), `Arash-60` (monthly), and `SORN.AI` (weekly), but underlying records have UNKNOWN scope. `ThirdEyesOfTheWorld` recurrence normalized to null. |
| **G3: Existing Spend / WTP** | $\ge 3$ independent VERIFIED spend/labor records | **0** in-scope | None | `Typical-Badger1922` has UNKNOWN scope; `Topify` and `SORN.AI` workaround are PARTIALLY_VERIFIED; `Upwork` is BLOCKED/PENDING; `Peec usage` is UNKNOWN scope and money_signal null; `Arash-60` money_signal null. |
| **G4: Repeatable Gap** | $\ge 3$ independent records, cluster size $\ge 3$ | **0** in-scope (4 out-of-scope/unknown) | None in-scope | If in-scope required: 0. Across the evaluated subset without scope restriction: 4 records qualify under reporting/attribution pain cluster (`Typical-Badger1922`, `nothabkuuys`, `jjnasty`, `erickrealz`). `Arash-60` excluded as tool use lacked paid spend. |
| **G5: ICP Reachability** | $\ge$ MEDIUM confidence, concrete channel | **2** in-scope | `geo-workflow-07-butter-marketing-profile`, `geo-workflow-11-reachability-clutch` | `Clutch Directory Channel` verifies searchable directory with 2–9 and 10–49 employee filters, supported by `Butter Marketing` (2–9 staff verified on Clutch). `What IF Web` and `SORN.AI` profiles are UNKNOWN scope. |
| **G6: No Killer Substitute** | Verified substitute context | **8** context | `geo-market-otterly-pricing`, `geo-market-semrush-plans`, `geo-market-seranking-plans`, `geo-market-seranking-agency-pack`, `geo-skeptic-substitute-semrush-ai-tracking`, `geo-skeptic-risk-sampling-noise-variance`, `geo-skeptic-risk-openai-search-pricing`, `geo-skeptic-risk-openai-tos-scraping` | Comprehensive context verified across incumbent suites, pure-play tools, sampling noise, and API costs/ToS. Commercial substitute fit and sufficiency remain materially unresolved for Judge determination. |

---

## 4. Unexamined Evidence Budget Preserved

The remaining 63 records in `ideas/geo-monitoring/evidence/evidence.jsonl` (commit `3bf758f`) were not modified, deleted, or fabricated. In accordance with Rules 25–31 and bounded reassessment guidelines:
1. No synthetic records were introduced.
2. The unexamined budget remains available if Stage 2 customer discovery requires broader scope exploration.
3. The dataset is sealed and cryptographically verifiable via `snapshot.json`.
