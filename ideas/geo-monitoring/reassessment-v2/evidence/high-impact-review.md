# High-Impact Evidence Review: Geo Monitoring (v2 Reassessment)

**Idea**: `geo-monitoring`  
**Target Scope**: `GEO-AGENCY-01` (Independent SEO agencies with 2–20 staff serving SMB clients on recurring retainers)  
**Policy Version**: `v2` (SMB Reassessment Policy per `methodology/stage1-policy.json`)  
**Evaluation Date**: 2026-09-11  
**Auditor**: Evidence Auditor  

---

## 1. Deep Review of Money Signals (WTP & Costly Behavior)

Under Policy v2 Gate 3, admission to Stage 2 customer discovery requires at least 3 independent, verified examples of actual target-job spending or actually performed costly labor (`min_independent_count: 3`, `min_categories: 1`). Stated WTP, vendor prices, and unverified estimates are strictly disallowed.

This review details the forensic re-examination of candidate money signals in the bounded dataset.

### Candidate Signal 1: Typical-Badger1922 (Costly Employee Labor)
- **ID**: `geo-pain-reddit-typicalbadger-patchwork-stack`
- **Speaker / Source**: `Typical-Badger1922` on `r/agency`
- **Audit Status**: `VERIFIED` | **Scope**: `UNKNOWN`
- **Signal**: `employee_time`
- **Evidence Review**: The author describes operating a small agency testing stacks and executing recurring manual prompt testing for 20 high-priority client queries weekly per account, stitching disparate outputs into Looker Studio for client reporting. However, the source does not provide explicit proof of agency headcount (2–20 staff). Additionally, the raw claim of "spending hours" was not directly stated by the author and was removed from the canonical observation.
- **Audit Decision**: **EXCLUDED FROM GATE 3**. While internal labor is described, the lack of explicit headcount verification places the record in `UNKNOWN` scope, excluding it from Gate 3 in-scope spend/labor thresholds.

### Candidate Signal 2: Arash-60 (Tool Use vs. Paid Spend)
- **ID**: `geo-pain-reddit-arash60-defensive-monthly-client-reporting`
- **Speaker / Source**: `Arash-60` on `r/seogrowth`
- **Audit Status**: `VERIFIED` | **Scope**: `UNKNOWN`
- **Signal**: Normalized from `saas_spend` to `null`
- **Evidence Review**: Live source inspection of comment `o3bbluh` confirms that Arash-60 uses Guzu.ai to establish client baseline rankings at contract inception and delivers monthly percentage change reports. However, the text contains zero evidence that the agency pays for Guzu.ai (it may be a free tier, trial, or client-provided seat), and the source does not verify agency headcount (2–20 staff). In accordance with Rule 6 (separate observation from interpretation) and the Evidence Standard, tool adoption cannot be promoted to revealed spending without direct proof of payment.
- **Audit Decision**: **EXCLUDED FROM GATE 3**. Canonical field `money_signal` was normalized to `null`, and scope is `UNKNOWN`.

### Candidate Signal 3: Elsa Ji / Topify (Vendor Arithmetic vs. Agency Labor)
- **ID**: `geo-wtp-blog-agency-manual-hours`
- **Speaker / Source**: `Elsa Ji` on `topify.ai/blog`
- **Audit Status**: `PARTIALLY_VERIFIED` | **Scope**: `OUT_OF_SCOPE`
- **Signal**: `employee_time` (disallowed)
- **Evidence Review**: Inspection shows that Elsa Ji is an in-house content marketer at Topify (a software vendor in the AI visibility space). The article claims: *"Tracking a single client across five AI engines already means checking dozens of prompts by hand every week. As Superlines has pointed out, fifty tracked keywords across five engines works out to 250 manual searches weekly for one account alone."* This is vendor promotional arithmetic citing another software vendor (Superlines), not an observed agency timesheet or empirical labor audit.
- **Audit Decision**: **EXCLUDED FROM GATE 3**. Reclassified as `PARTIALLY_VERIFIED` and `OUT_OF_SCOPE`. Vendor marketing arithmetic cannot be credited as revealed buyer willingness to pay.

### Candidate Signal 4: Stanislava Smiljanic / SORN.AI (Counterfactual vs. Performed Labor)
- **ID**: `geo-workflow-12-manual-workaround-labor`
- **Speaker / Source**: `Stanislava Smiljanic` on `otterly.ai/blog/geo-case-study-sornai/`
- **Audit Status**: `PARTIALLY_VERIFIED` | **Scope**: `UNKNOWN`
- **Signal**: `employee_time` (disallowed)
- **Evidence Review**: Stanislava Smiljanic is an agency co-founder at SORN.AI. However, her quote states: *“It would be very manual, with a ton of print screens and manual research of prompts with VPN,” Stanislava says of the alternative.* The phrasing explicitly describes a hypothetical alternative ("would be very manual..."), not a verified record of hours actually logged or payroll spent performing manual checks. Additionally, the underlying agency profile (`geo-workflow-04-sornai-profile`) lacks explicit headcount verification, placing the record in `UNKNOWN` scope.
- **Audit Decision**: **EXCLUDED FROM GATE 3**. Reclassified as `PARTIALLY_VERIFIED` and `UNKNOWN` scope. Counterfactual descriptions of what work *would* be needed in the absence of tools cannot substitute for observed labor expenditure.

### Candidate Signal 5: maltelandwehr / Peec AI User (Unverified Scope & Spend)
- **ID**: `geo-wtp-reddit-peec-usage`
- **Speaker / Source**: `maltelandwehr` on `r/SEO`
- **Audit Status**: `PARTIALLY_VERIFIED` | **Scope**: `UNKNOWN`
- **Signal**: Normalized from `saas_spend` to `null`
- **Evidence Review**: The author confirms using Peec AI for visibility reporting and content optimization ("I use Peec AI"). However, the comment does not establish paid subscription or revealed willingness to pay, and their organizational identity and agency headcount cannot be verified against `GEO-AGENCY-01`.
- **Audit Decision**: **EXCLUDED FROM GATE 3**. Reclassified as `PARTIALLY_VERIFIED`; `interpretation`, `recurrence`, `money_signal`, and `money_period` normalized, and scope is `UNKNOWN`.

### Candidate Signal 6: UK PR Agency Upwork Contract (Access Blocked)
- **ID**: `geo-wtp-upwork-pr-agency-contract`
- **Speaker / Source**: `UK PR Agency` on `upwork.com`
- **Audit Status**: `PENDING` | **Scope**: `UNKNOWN`
- **Signal**: `stated_wtp`
- **Evidence Review**: Retrieval was blocked by Cloudflare Turnstile anti-bot protection (HTTP 403). Under repository rules 25–27, automated scraping workarounds are prohibited.
- **Audit Decision**: **EXCLUDED FROM GATE 3**. Retained as `PENDING` and cannot be counted toward any threshold.

### Summary of Gate 3 Eligibility
- **Counted In-Scope Signals**: **0**
- **Excluded Candidates**: 6 candidate records reviewed and excluded (1 due to unverified scope, 2 normalized due to lack of payment proof, 2 due to partially verified/counterfactual claims, 1 blocked).
- **Audit Note**: No candidate record satisfies both verified revealed spend/labor and verified `GEO-AGENCY-01` scope. Gate 3 status determination is reserved for the Stage 1 Judge.

---

## 2. Competitor Pricing & Commercial Substitute Landscape

Vendor rate cards establish market pricing benchmarks, though they do not represent buyer willingness to pay:

1. **SE Ranking Agency Bundles** (`geo-market-seranking-plans`, `geo-market-seranking-agency-pack`):
   - Core (€109/mo) and Growth (€235/mo) bundle daily tracking for 100–250 AI prompts across 10–30 client projects.
   - The Agency Pack add-on (€59/mo) provides custom domain white-labeling (`seo.agency.com`), 30 client seats, Looker Studio integration, and automated scheduled reporting.
   - *Impact*: Establishes an incumbent ceiling of ~€294/month for a 30-client agency (~€10/client/mo).
2. **Semrush Incumbent Suite** (`geo-market-semrush-plans`, `geo-skeptic-substitute-semrush-ai-tracking`):
   - Bundles Google AI Overview tracking and the AI Visibility Toolkit (ChatGPT, Google AI Mode, Gemini) into core tiers ($199–$549/mo) with branded PDF exports and a $20/mo Pro Report white-label add-on.
   - *Impact*: High inertia; existing agency subscribers resist paying $100+/mo for a standalone monitoring tool when traditional suites bundle AI tracking.
3. **Pure-Play AI Trackers** (`geo-market-otterly-pricing`, `geo-market-peec-agency-plans`):
   - Otterly.ai Standard costs €189/mo for 100 prompts (150 for agency partners), but charges heavy add-on surcharges for Claude (€109/mo) and Gemini (€59/mo).
   - Peec AI agency plans range from €205/mo (1 client) to €675/mo (5–7 client projects).
   - *Impact*: Multi-client pure-play tools are priced for funded mid-market agencies, leaving small independent agencies (2–20 staff) underserved.
4. **Substitute Uncertainty**:
   - Whether bundled incumbent suites (SE Ranking, Semrush) or manual spot-check routines provide a sufficient, adequate substitute for `GEO-AGENCY-01` remains materially unresolved in the evidence and is reserved for Stage 1 Judge evaluation.

---

## 3. Strongest Positive Evidence (ICP & Workflow Coherence)

The bounded dataset establishes qualitative evidence for problem existence and operational workflow, while scope discipline distinguishes verified headcount from unverified practitioners:

1. **Direct Agency Pain & Client Anxiety (Unverified Headcount / UNKNOWN Scope)**:
   - `nothabkuuys` (`geo-pain-reddit-nothabkuuys-small-agency-client-anxiety`): Small agency owner describes intense friction managing SMB client expectations across Google AIO, ChatGPT, and Claude, and confusion over billing models.
   - `Typical-Badger1922` (`geo-pain-reddit-typicalbadger-patchwork-stack`): Documents weekly prompt checking routines and stitching data into Looker Studio to demonstrate trendlines to clients.
2. **Verified In-Scope Boutique Agency & Channel**:
   - `Butter Marketing` (`geo-workflow-07-butter-marketing-profile`, 2–9 staff): Verified London agency on Clutch dedicating 70% of operations to Generative Engine Optimization.
   - `Clutch Directory Channel` (`geo-workflow-11-reachability-clutch`): Provides verified public directory filters specifically segmenting independent agencies by headcount (2–9 and 10–49 employees) and service line (GEO / SEO).
3. **Workflow Profiles with Unverified Headcount (UNKNOWN Scope)**:
   - `What IF Web` (`geo-workflow-01-whatifweb-profile`): Blog confirms agency services and Otterly partnership, but does not verify team size (3–5 staff).
   - `SORN.AI` (`geo-workflow-04-sornai-profile`, `geo-workflow-06-sornai-reporting-cadence`, `geo-workflow-12-manual-workaround-labor`): Homepage and Otterly case study confirm weekly client reporting cadence, but do not verify team size (2–10 staff).

---

## 4. Strongest Negative & Technical Risk Evidence

1. **Buyer Resistance to Standalone Recurring Line Items**:
   - `jjnasty` (`geo-pain-reddit-jjnasty-losing-game-oneoff-audit`): Emphatically advises against recurring retainers for AI optimization because proving ROI without reliable tracking is a "losing game." Recommends low-lift quarterly audits instead.
   - `ThirdEyesOfTheWorld` (`geo-pain-reddit-thirdeyesoftheworld-bundled-substitute`): Labels separate GEO monitoring fees as "snake oil" and bundles AI referral monitoring directly into existing SEO retainers.
2. **Technical Feasibility & Unit Economics Hurdles**:
   - `Jay Sim / CiteAngle` (`geo-skeptic-risk-sampling-noise-variance`): Empirical research (arXiv:2604.07585) proves single prompt checks have a standard error of $\pm 0.37$ due to non-zero sampling temperature. Reliable measurement requires $n=7$ repeated queries per prompt per surface.
   - `OpenAI Web Search Pricing` (`geo-skeptic-risk-openai-search-pricing`): Authorized search API calls cost $10–$25 per 1,000 requests. Running 50 queries $\times$ 7 repeats across 4 surfaces results in 1,400 calls ($14–$35) per client audit in raw API costs alone, challenging a $100/mo price point.
   - `OpenAI Terms of Use` (`geo-skeptic-risk-openai-tos-scraping`): Section 2 explicitly prohibits programmatic extraction and anti-bot circumvention, preventing compliant tools from scraping consumer web interfaces.

---

## 5. Summary of Audited Counts for Stage 1 Judge

Per Repository Rules 17–20 and Evidence Audit boundaries, the Evidence Auditor does not issue gate verdicts or recommend Stage 1 decisions (PASS, CONDITIONAL PASS, FAIL). Gate-eligibility counts based strictly on verified, in-scope records:
- **G1 (Concrete Pain)**: 0 in-scope verified records (6 pain records reviewed, all classified UNKNOWN scope due to unverified agency headcount).
- **G2 (Recurrence)**: 0 in-scope verified records (cadences observed in Typical-Badger1922, Arash-60, and SORN.AI, but underlying records have UNKNOWN scope).
- **G3 (Existing Spend / WTP)**: 0 in-scope verified spend/labor records.
- **G4 (Repeatable Gap)**: 0 in-scope verified records (4 out-of-scope/unknown records in qualitative reporting/attribution cluster).
- **G5 (ICP Reachability)**: 2 in-scope verified records (`geo-workflow-07-butter-marketing-profile`, `geo-workflow-11-reachability-clutch`).
- **G6 (No Killer Substitute)**: 8 verified context records. Fit, sufficiency, and defensibility of incumbent bundles and manual workarounds remain materially unresolved for Judge determination.
