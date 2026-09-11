# Stage 1 Validation Report: Geo Monitoring (v2 Reassessment)

**Idea ID**: `geo-monitoring`  
**Idea Name**: Agency-first GEO / AI-Search Visibility Monitoring  
**Evaluated Scope**: `GEO-AGENCY-01` (Independent SEO agencies with 2–20 staff serving SMB clients on recurring retainers)  
**Evaluation Date**: 2026-09-11  
**Policy Version**: `v2` (Stage 1 SMB Reassessment Policy per `methodology/stage1-policy.json`)  
**Input Snapshot**: `snap-geo-v2-003` (Sealed evidence snapshot; baseline commit `3bf758f`)  
**Verdict**: **INSUFFICIENT EVIDENCE**  
**Stage 2 Authorized**: **No (`false`)**  
**Recommended Next Action**: `REPAIR_RESEARCH`  

---

## 1. Executive Summary & Verdict Decision

This Stage 1 reassessment evaluates the product hypothesis for `geo-monitoring` under Policy v2 (SMB Reassessment Policy). Under Policy v2, numeric gates are calibrated to an SMB-appropriate scale to test admission to limited customer discovery interviews ($\le 8$ interviews), rather than MVP or build approval.

### Verdict: INSUFFICIENT EVIDENCE

Under Policy v2 decision rules:
- **PASS** requires all six gates (G1–G6) to PASS for a coherent declared scope.
- **CONDITIONAL PASS** requires G1 and G5 to PASS with 0 FAIL gates, all material UNKNOWN gates covered by condition objects with `resolution_method: INTERVIEW`, and no material unresolved technical feasibility, API access, or sampling unit economics constraints.
- **FAIL** requires cited verified contradictory evidence against core assumptions.
- **INSUFFICIENT EVIDENCE** occurs when thresholds remain unmet or material assumptions remain unknown without complete market falsification.

In this reassessment of candidate scope `GEO-AGENCY-01`:
1. **G5 (ICP Reachability) PASSES**: Reachability is established with HIGH confidence (2 independent verified records: `geo-workflow-07-butter-marketing-profile` and `geo-workflow-11-reachability-clutch`). Clutch provides a searchable, filtered public discovery channel specifically segmenting 2–9 and 10–49 employee agencies, supported by Butter Marketing (a verified 2–9 employee London agency with 70% service allocation to GEO).
2. **G1 (Concrete Pain) is UNKNOWN (0 in-scope verified signals vs threshold $\ge 5$)**: While 6 Reddit pain records were verified by the Evidence Auditor, every single author lacks explicit source-level proof of agency headcount (2–20 staff), placing all 6 in `UNKNOWN` scope. Under strict repository scope rules, unverified practitioner claims cannot be counted toward in-scope thresholds.
3. **G2 (Recurrence) is UNKNOWN (0 in-scope verified signals vs threshold $\ge$ MEDIUM confidence)**: Reporting cadences observed in unverified practitioner profiles (`Typical-Badger1922`, `Arash-60`, `SORN.AI`) cannot satisfy the gate because the underlying entities lack verified 2–20 staff headcount.
4. **G3 (Revealed Spend / Costly Labor) is UNKNOWN (0 in-scope verified signals vs threshold $\ge 3$)**: Rigorous forensic re-audit eliminated all candidate spend/labor signals. Free tool usage was separated from paid SaaS spend (`Arash-60` normalized to null; `maltelandwehr` normalized to null); vendor marketing arithmetic was disqualified (`Topify / Elsa Ji` reclassified to PARTIALLY_VERIFIED); counterfactual speculation was separated from observed labor (`SORN.AI / Stanislava Smiljanic` reclassified to PARTIALLY_VERIFIED); and Upwork freelance contract was blocked by Cloudflare Turnstile (`PENDING`). Stated WTP is excluded from numeric counts under Policy v2.
5. **G4 (Repeatable Solution Gap) is UNKNOWN (0 in-scope verified signals vs threshold $\ge 3$)**: Qualitative solution gaps (manual prompt checking, Looker Studio data stitching, attribution skepticism) lack in-scope headcount attribution.
6. **G6 (No Killer Substitute) is UNKNOWN**: 7 independent verified context records confirm severe commercial, technical, and legal threats that remain materially unresolved. Low-cost incumbent SEO platforms (SE Ranking at €109–€235/mo with a €59/mo white-label Agency Pack; Semrush at $199–$299/mo) bundle daily AI search tracking into core subscriptions; empirical measurement research demonstrates single prompt checks carry $\pm 0.37$ standard error requiring $n=7$ repeats per prompt; authorized API search calls cost $10–$25 per 1,000 calls creating $14–$35 direct cost per client audit; and OpenAI Terms of Use prohibit programmatic extraction from consumer web interfaces.

Because G1 does not PASS, CONDITIONAL PASS is strictly prohibited by Policy v2 (`required_pass_gates: ["G1", "G5"]`). Because core assumptions remain unverified without complete falsification, the verdict is **INSUFFICIENT EVIDENCE**. Stage 2 customer discovery is not authorized.

---

## 2. Gate-by-Gate Evaluation Table (Policy v2)

| Gate | Status | Threshold / Rule | Independent Count | Counted Evidence IDs | Confidence | Contradictory IDs | Material Unknowns |
| :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| **G1: Concrete Pain** | **UNKNOWN** | $\ge 5$ independent in-scope VERIFIED concrete pain signals | 0 | *(none)* | LOW | *(none)* | Headcount verification of suffering agencies; SMB client demand for recurring reports vs quarterly audits. |
| **G2: Recurrence** | **UNKNOWN** | $\ge$ MEDIUM confidence in recurrence of core job | 0 | *(none)* | LOW | *(none)* | Whether weekly/monthly reporting is a billable deliverable for 2–20 staff agencies or defensive uncompensated overhead. |
| **G3: Existing Spend / WTP** | **UNKNOWN** | $\ge 3$ independent VERIFIED actual spend/costly labor records ($\ge 1$ category); stated WTP excluded | 0 | *(none)* | LOW | *(none)* | Actual monthly software budget allocated by 2–20 person SEO agencies for standalone GEO monitoring. |
| **G4: Repeatable Gap** | **UNKNOWN** | $\ge 3$ independent VERIFIED gap signals supporting 1 coherent cluster (size $\ge 3$) | 0 | *(none)* | LOW | *(none)* | Whether automated connectors (SE Ranking, Otterly) close the Looker Studio data stitching gap. |
| **G5: ICP Reachability** | **PASS** | $\ge$ MEDIUM confidence; concrete role, segment, and acquisition surface | 2 | `geo-workflow-07-butter-marketing-profile`, `geo-workflow-11-reachability-clutch` | HIGH | *(none)* | Cold outreach response rates and conversion economics for agency owners discovered on Clutch. |
| **G6: No Killer Substitute** | **UNKNOWN** | No low-friction sufficient substitute defeating value proposition; verified context | 7 | `geo-market-otterly-pricing`, `geo-market-semrush-plans`, `geo-market-seranking-plans`, `geo-skeptic-substitute-semrush-ai-tracking`, `geo-skeptic-risk-sampling-noise-variance`, `geo-skeptic-risk-openai-search-pricing`, `geo-skeptic-risk-openai-tos-scraping` | MEDIUM | *(none)* | Commercial fit of bundled suite tracking; unit economics under $n=7$ repeated sampling; compliance under OpenAI ToS. |

---

## 3. Detailed Gate Analyses

### Gate 1: Concrete Pain
- **Status**: `UNKNOWN`
- **Threshold**: $\ge 5$ independent VERIFIED examples of experienced concrete pain/workarounds for assessed scope (`GEO-AGENCY-01`).
- **Independent Count**: 0
- **Counted Evidence IDs**: `[]`
- **Contradictory Evidence IDs**: `[]`
- **High-Impact Excluded Evidence**:
  - `geo-pain-reddit-typicalbadger-patchwork-stack`: Scope UNKNOWN. Small agency operator describes running manual prompt checks across 20 queries weekly per client and stitching data into Looker Studio, but cited thread provides no explicit headcount verification (2–20 staff).
  - `geo-pain-reddit-nothabkuuys-small-agency-client-anxiety`: Scope UNKNOWN. Small agency owner describes severe client expectation friction across Google AIO, ChatGPT, and Claude, but headcount (2–20 staff) is unverified.
  - `geo-pain-reddit-jjnasty-losing-game-oneoff-audit`: Scope UNKNOWN. Strategist warns against recurring retainers due to unprovable ROI, but agency headcount is unverified.
  - `geo-pain-reddit-erickrealz-agency-attribution-impossibility`: Scope UNKNOWN. Practitioner reports attribution impossibility in AI search, but agency headcount is unverified.
  - `geo-pain-reddit-thirdeyesoftheworld-bundled-substitute`: Scope UNKNOWN. Agency owner bundles AI checks into existing SEO retainers, but headcount is unverified.
  - `geo-pain-reddit-arash60-defensive-monthly-client-reporting`: Scope UNKNOWN. Agency lead reports monthly client reporting with Guzu.ai, but headcount is unverified.
  - `geo-wtp-blog-agency-manual-hours`: Status PARTIALLY_VERIFIED and OUT_OF_SCOPE. Vendor promotional calculation quoting Superlines arithmetic, not observed agency staff hours.
- **Analysis**:
  While qualitative pain regarding AI search visibility volatility, client expectation management, and reporting rework is richly documented across agency communities, not a single record satisfies both `VERIFIED` audit status and verified `GEO-AGENCY-01` scope. Headcount discipline prevents treating general practitioner commentary as verified evidence for 2–20 employee agencies. Threshold $\ge 5$ is unmet.

### Gate 2: Recurrence
- **Status**: `UNKNOWN`
- **Threshold**: $\ge$ MEDIUM confidence that core monitoring job recurs (e.g. monthly client reporting).
- **Independent Count**: 0
- **Counted Evidence IDs**: `[]`
- **Contradictory Evidence IDs**: `[]`
- **High-Impact Excluded Evidence**:
  - `geo-workflow-06-sornai-reporting-cadence`: Scope UNKNOWN. Weekly reporting cadence confirmed on case study, but underlying agency profile lacks explicit headcount verification.
  - `geo-pain-reddit-typicalbadger-patchwork-stack`: Scope UNKNOWN. Weekly prompt checking cadence observed, but agency headcount is unverified.
  - `geo-pain-reddit-arash60-defensive-monthly-client-reporting`: Scope UNKNOWN. Monthly reporting cadence observed, but agency headcount is unverified.
- **Analysis**:
  Recurrence is established for informal practitioners and unverified entities, but zero in-scope records verify recurring cadence for the target 2–20 staff agency ICP.

### Gate 3: Existing Spend / WTP
- **Status**: `UNKNOWN`
- **Threshold**: $\ge 3$ independent VERIFIED examples of actual target-job spending or actually performed costly work from $\ge 1$ eligible category; stated WTP excluded from numeric count.
- **Independent Count**: 0
- **Counted Evidence IDs**: `[]`
- **Contradictory Evidence IDs**: `[]`
- **Breakdown by Category**: `{}`
- **High-Impact Excluded Evidence**:
  - `geo-pain-reddit-typicalbadger-patchwork-stack`: Scope UNKNOWN. Unpriced employee labor described, but agency headcount is unverified.
  - `geo-pain-reddit-arash60-defensive-monthly-client-reporting`: Scope UNKNOWN and money_signal normalized to null. Tool usage (Guzu.ai) observed without proof of paid subscription.
  - `geo-wtp-reddit-peec-usage`: Status PARTIALLY_VERIFIED and scope UNKNOWN. Peec AI usage reported without proof of paid subscription or verified agency headcount.
  - `geo-workflow-12-manual-workaround-labor`: Status PARTIALLY_VERIFIED and scope UNKNOWN. Counterfactual statement ("It would be very manual...") rather than audited performed labor; headcount unverified.
  - `geo-wtp-blog-agency-manual-hours`: Status PARTIALLY_VERIFIED and OUT_OF_SCOPE. Vendor promotional arithmetic, not observed agency payroll.
  - `geo-wtp-upwork-pr-agency-contract`: Status PENDING and scope UNKNOWN. Upwork posting blocked by Cloudflare Turnstile; stated WTP excluded from numeric count by policy v2.
- **Analysis**:
  Gate 3 underwent complete forensic re-auditing. Tool adoption was separated from paid software spend; vendor marketing arithmetic was disqualified; counterfactual statements were separated from performed labor; and blocked records were kept PENDING. Zero records satisfy in-scope revealed spend or performed costly labor.

### Gate 4: Repeatable Solution Gap
- **Status**: `UNKNOWN`
- **Threshold**: $\ge 3$ independent VERIFIED examples supporting one coherent, repeated gap/workaround cluster with $\ge 3$ members.
- **Independent Count**: 0
- **Counted Evidence IDs**: `[]`
- **Contradictory Evidence IDs**: `[]`
- **Clusters**: `{}`
- **High-Impact Excluded Evidence**:
  - `geo-pain-reddit-typicalbadger-patchwork-stack`: Scope UNKNOWN. Manual prompt testing and Looker Studio stitching verified, but agency headcount unverified.
  - `geo-pain-reddit-nothabkuuys-small-agency-client-anxiety`: Scope UNKNOWN. Client expectation gap verified, but agency headcount unverified.
  - `geo-pain-reddit-jjnasty-losing-game-oneoff-audit`: Scope UNKNOWN. Tracking gap making recurring retainers a "losing game" verified, but agency headcount unverified.
  - `geo-pain-reddit-erickrealz-agency-attribution-impossibility`: Scope UNKNOWN. Attribution gap verified, but agency headcount unverified.
- **Analysis**:
  Across the broader dataset, 4 qualitative records describe a coherent problem cluster around manual prompt testing, attribution failure, and Looker Studio reporting compilation. However, because all 4 records lack verified agency headcount, in-scope count is 0.

### Gate 5: ICP Reachability
- **Status**: `PASS`
- **Threshold**: $\ge$ MEDIUM confidence that relevant buyers can be found through a concrete acquisition surface.
- **Independent Count**: 2
- **Counted Evidence IDs**:
  - `geo-workflow-07-butter-marketing-profile` (independence_key: `butter-marketing-profile`): Verified London agency on Clutch with 2–9 employees dedicating 70% of its service offering to Generative Engine Optimization.
  - `geo-workflow-11-reachability-clutch` (independence_key: `clutch-seo-directory-channel`): Verified public B2B directory providing searchable filters specifically segmenting 2–9 and 10–49 employee agencies, verified client reviews, and direct agency website/founder links.
- **Contradictory Evidence IDs**: `[]`
- **High-Impact Excluded Evidence**:
  - `geo-workflow-01-whatifweb-profile`: Scope UNKNOWN. Studio profile confirmed on blog, but cited source does not verify team size (2–20 staff).
  - `geo-workflow-04-sornai-profile`: Scope UNKNOWN. Agency profile confirmed on homepage, but cited source does not verify team size (2–20 staff).
- **Confidence**: `HIGH`
- **Analysis**:
  Clutch provides an explicit, scalable acquisition channel matching the founder's preferred outbound model. Search filters isolate agencies with 2–9 employees specializing in SEO/GEO, directly verifiable against verified profiles like Butter Marketing. Gate 5 PASSES with HIGH confidence.

### Gate 6: No Killer Substitute
- **Status**: `UNKNOWN`
- **Threshold**: No low-friction sufficient substitute that defeats the value proposition. Requires verified substitute assessment context.
- **Independent Count**: 7 (deduplicated by independence key)
- **Counted Evidence IDs**:
  - `geo-market-otterly-pricing` (independence_key: `otterly-ai-pricing`): Standard plan €189/mo with Looker Studio connector and multi-workspace support, but modular add-on fees (€59/mo Gemini, €109/mo Claude) create high software costs.
  - `geo-market-semrush-plans` (independence_key: `semrush-pricing`): Starter ($199/mo) and Pro+ ($299/mo) bundle 50–100 daily AI prompts across 5–15 websites with branded exports.
  - `geo-market-seranking-plans` (independence_key: `seranking-pricing`): Core (€109/mo) and Growth (€235/mo) bundle 100–250 daily AI search prompts across 10–30 client projects.
  - `geo-skeptic-substitute-semrush-ai-tracking` (independence_key: `semrush-kb-1503-ai-toolkit`): AI Visibility Toolkit bundles multi-engine prompt tracking into Semrush One plans with branded exports.
  - `geo-skeptic-risk-sampling-noise-variance` (independence_key: `sim-sampling-noise-variance`): Empirical research (arXiv:2604.07585) shows single checks carry $\pm 0.37$ standard error, requiring $n=7$ repeats per prompt to achieve statistical validity.
  - `geo-skeptic-risk-openai-search-pricing` (independence_key: `openai-api-pricing`): Official Web Search tool costs $10–$25 per 1,000 calls, resulting in $14–$35 direct API costs per client audit under required sampling.
  - `geo-skeptic-risk-openai-tos-scraping` (independence_key: `openai-terms-of-use`): Terms of Use explicitly prohibit programmatic output extraction and circumventing protective measures.
- **Contradictory Evidence IDs**: `[]`
- **High-Impact Excluded Evidence**:
  - `geo-market-seranking-agency-pack`: Excluded from counted IDs due to duplicate independence key (`seranking-pricing`) with `geo-market-seranking-plans`. Preserved as supporting pricing context (€59/mo add-on for white-labeling, 30 client seats, Looker Studio).
  - `geo-market-peec-agency-plans`: Status PARTIALLY_VERIFIED due to project allocation discrepancy between pricing cards and comparison table.
- **Confidence**: `MEDIUM`
- **Analysis**:
  Gate 6 cannot PASS because incumbent SEO platforms (SE Ranking, Semrush) bundle AI tracking at negligible incremental cost, while pure-play monitoring tools face crippling unit economics ($14–$35/client in raw API search fees) under mandatory $n=7$ repeated sampling. Conversely, Gate 6 cannot FAIL because practitioner evidence indicates incumbent suite tracking is superficial and lacks white-label multi-client client reporting clarity. Commercial substitute sufficiency remains unresolved, leaving G6 `UNKNOWN`.

---

## 4. Scope Integrity & Excluded Profiles

Candidate scope `GEO-AGENCY-01` is strictly defined in `hypothesis.yaml`:
> "Small independent SEO agencies with 2–20 staff serving SMB clients on recurring retainers."

Under repository validation rules, references to "clients", "our clients", "smaller agency", contracts, or retainers alone do not prove scope without explicit evidence verifying both team size (2–20 staff) and SMB client focus.

In accordance with the launch protocol, the following profile records were evaluated as **excluded context only**:
1. **`geo-workflow-01-whatifweb-profile`**:
   The What IF Web blog confirms a boutique digital studio in Christchurch, New Zealand, serving SaaS and SMB clients and partnering with Otterly.ai. However, the cited source does not state employee count (3–5 staff). Classified as `scope_status: UNKNOWN` and excluded from counted totals.
2. **`geo-workflow-04-sornai-profile`**:
   The SORN.AI homepage confirms an independent boutique AI SEO agency serving SaaS, eCommerce, and legal clients. However, the cited source does not verify team headcount (2–10 staff). Classified as `scope_status: UNKNOWN` and excluded from counted totals.
3. **`geo-workflow-06-sornai-reporting-cadence`**:
   The Otterly case study confirms weekly client reporting driven by AI citation volatility and Brand Visibility Index quadrant graphs. However, because the underlying agency entity lacks verified headcount, this record is classified as `scope_status: UNKNOWN` and excluded from counted totals.
4. **`geo-workflow-12-manual-workaround-labor`**:
   Stanislava Smiljanic's quote (*“It would be very manual, with a ton of print screens and manual research of prompts with VPN”*) represents a counterfactual estimation of an alternative workflow, not observed or audited manual hours logged by staff. Classified as `audit_status: PARTIALLY_VERIFIED` and `scope_status: UNKNOWN`.

Only two records in the bounded dataset satisfied full in-scope criteria:
- `geo-workflow-07-butter-marketing-profile`: Verified on Clutch directory with 2–9 employees in London, allocating 70% of service focus to Generative Engine Optimization.
- `geo-workflow-11-reachability-clutch`: Verified public B2B directory providing searchable filters specifically segmenting 2–9 and 10–49 employee agencies.

---

## 5. Retrospective Verdict Comparison (v1 vs v2)

| Dimension | Historical v1 Evaluation | Reassessment v2 Evaluation | Primary Driver of Difference |
| :--- | :---: | :---: | :--- |
| **G1: Concrete Pain** | UNKNOWN (5 signals, threshold $\ge 20$) | **UNKNOWN (0 signals, threshold $\ge 5$)** | Scope discipline: 5 baseline signals lacked verified headcount (2–20 staff). |
| **G2: Recurrence** | PASS (4 signals, conf: MEDIUM) | **UNKNOWN (0 signals, conf: LOW)** | Scope discipline: cadences observed in SORN.AI, Arash-60, and Typical-Badger lacked verified headcount. |
| **G3: Existing Spend / WTP** | UNKNOWN (4 signals, threshold $\ge 5$) | **UNKNOWN (0 signals, threshold $\ge 3$)** | Evidence forensic review: tool use normalized from spend; vendor arithmetic & counterfactuals disqualified. |
| **G4: Repeatable Gap** | UNKNOWN (5 signals, threshold $\ge 10$) | **UNKNOWN (0 signals, threshold $\ge 3$)** | Scope discipline: gap signals lacked verified headcount attribution. |
| **G5: Reachability** | PASS (5 signals, conf: HIGH) | **PASS (2 signals, conf: HIGH)** | Maintained: Clutch channel and Butter Marketing verified 2–9 staff agency reachability. |
| **G6: No Killer Substitute** | UNKNOWN (6 signals, conf: MEDIUM) | **UNKNOWN (7 signals, conf: MEDIUM)** | Maintained: incumbent bundling, sampling noise ($n=7$), API costs, and OpenAI ToS remain unresolved. |
| **Overall Verdict** | **INSUFFICIENT EVIDENCE** | **INSUFFICIENT EVIDENCE** | Unchanged verdict, but driven by rigorous evidence forensics rather than arbitrary numeric quotas. |
| **Stage 2 Authorized** | False | False | Unchanged. |

### Decomposition of Reassessment Effects

The comparison separates the effects into three distinct categories:

#### 1. Effect of Policy Threshold Changes
Under Policy v2, numeric admission thresholds were lowered to reflect the operational reality of SMB discovery (G1: $20 \to 5$; G3: $5 \to 3$; G4: $10 \to 3$). If historical v1 evidence classifications had remained intact, the idea would have met G1 (5 signals), G3 (4 signals), and G4 (5 signals), qualifying for CONDITIONAL PASS. However, Policy v2 is not a license to dilute evidence standards; it couples lower thresholds with tighter evidence fidelity.

#### 2. Effect of Evidence Corrections & Forensic Review (Leads 1–5)
Rigorous re-inspection of primary sources against canonical evidence rules disqualified candidate signals that had been improperly credited in historical runs:
- **Lead 1 (Tool Use vs Paid Spend)**: `Arash-60` reported using Guzu.ai to establish client baseline rankings. However, the source contained zero proof of payment. `money_signal` was normalized from `saas_spend` to `null`.
- **Lead 2 (Vendor Arithmetic vs Agency Labor)**: `Topify / Elsa Ji` claimed tracking 50 keywords across 5 engines required 250 weekly manual searches. Source inspection revealed this was promotional arithmetic citing another software vendor (Superlines), not audited agency timesheets. Reclassified to `PARTIALLY_VERIFIED` and `OUT_OF_SCOPE`.
- **Lead 3 (Counterfactual vs Performed Labor)**: `SORN.AI / Stanislava Smiljanic` stated tracking *would* be manual with print screens and VPN. This counterfactual speculation was reclassified to `PARTIALLY_VERIFIED`.
- **Lead 4 (Unproven Peec AI Spend)**: `maltelandwehr` confirmed Peec AI usage, but source did not establish paid subscription. Normalized to `null` spend.
- **Lead 5 (Blocked Upwork Contract)**: `UK PR Agency` was blocked by Cloudflare Turnstile (`PENDING`), and stated WTP is excluded from Policy v2 numeric counts.

#### 3. Effect of Scope Interpretation & Headcount Discipline
The decisive difference between v1 and v2 is strict enforcement of candidate scope `GEO-AGENCY-01`. While v1 loosely pooled comments from "smaller agencies" and "our clients", v2 enforces Rule 1: an agency cannot be claimed as having 2–20 staff unless the cited source explicitly verifies that headcount. Consequently, 6 Reddit pain records and 3 agency profile records were classified as `scope_status: UNKNOWN`, reducing counted in-scope signals for G1, G2, G3, and G4 to zero.

---

## 6. Commercial, Technical, and Legal Risk Synthesis

The 7 verified Gate 6 context records document formidable structural barriers:

1. **Incumbent Suite Bundling**:
   - SE Ranking (`geo-market-seranking-plans`, `geo-market-seranking-agency-pack`) includes daily tracking for 100–250 AI prompts across 10–30 client projects for €109–€235/mo. An Agency Pack add-on (€59/mo) provides white-label client portals, custom SMTP reports, and Looker Studio integration.
   - Semrush (`geo-market-semrush-plans`, `geo-skeptic-substitute-semrush-ai-tracking`) bundles multi-engine prompt tracking into core SEO tiers ($199–$549/mo) with branded exports.
   - *Impact*: Small agencies operating on $399–$699/mo client retainers resist paying $100+/mo for a standalone monitoring tool when traditional suites bundle AI tracking.

2. **Statistical Sampling Variance ($n=7$)**:
   - Academic research (`geo-skeptic-risk-sampling-noise-variance`, arXiv:2604.07585) proves single prompt checks have a standard error of $\pm 0.37$ due to non-zero LLM sampling temperature. Single spot-checks exhibit 10%–34% random variance.
   - Reducing standard error below 0.10 requires at least $n=7$ repeated queries per prompt per surface.
   - *Impact*: A naive single-check tool produces misleading noise; a statistically defensible tool must multiply API query volume by 7x.

3. **API Infrastructure Unit Economics**:
   - Official OpenAI Web Search API calls (`geo-skeptic-risk-openai-search-pricing`) cost $10–$25 per 1,000 requests.
   - Tracking 50 prompts $\times$ 7 repeats across 4 engines equals 1,400 API search calls per client audit ($14–$35 in raw supplier costs).
   - For an agency tracking 5 clients, raw API costs reach $70–$175/month, completely eliminating gross margin at a $100/mo ARPU.

4. **Platform Terms of Use & Legal Restrictions**:
   - OpenAI Terms of Use (`geo-skeptic-risk-openai-tos-scraping`, updated Jan 16, 2026) explicitly prohibit programmatic output extraction and circumventing safety/rate limits.
   - Scraping consumer ChatGPT interfaces exposes monitoring tools to IP blocks, Cloudflare Turnstile challenges, and legal liability.

---

## 7. Strategic Recommendations & Next Actions

### Recommended Next Action: `REPAIR_RESEARCH`
Stage 2 customer discovery is **not authorized** (`stage2_authorized: false`). The hypothesis remains unvalidated due to evidence collection gaps and unverified scope attribution.

If the founder decides to pursue `geo-monitoring` further, the following research repair steps are required before re-submitting to Stage 1 Judge:

1. **Verify Headcount for Identified Practitioner Entities**:
   Conduct targeted OSINT or public registry checks (Companies House, LinkedIn, Clutch) to verify team size (2–20 staff) for `What IF Web`, `SORN.AI`, `Typical-Badger1922`, and `Arash-60`. If headcount is proven, link the profile records in `scope-map.json` to elevate candidate pain signals from `UNKNOWN` to `IN_SCOPE`.
2. **Obtain Primary First-Hand Evidence of Paid Tool Spend**:
   Identify verified instances where independent agencies pay for standalone AI visibility tools (e.g. Peec AI, Otterly.ai, Guzu.ai) out of agency overhead, rather than utilizing free trials or bundling checks into core SEO suites.
3. **Conduct Preceding Technical Check on Sampling Economics**:
   Formulate a technical feasibility study resolving the contradiction between $n=7$ sampling variance requirements, official API search pricing ($10–$25/1k calls), and the founder's target $100/mo ARPU constraint.
