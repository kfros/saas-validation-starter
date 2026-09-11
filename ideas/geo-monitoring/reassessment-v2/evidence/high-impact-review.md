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
- **Audit Status**: `VERIFIED` | **Scope**: `IN_SCOPE` (`GEO-AGENCY-01`)
- **Signal**: `employee_time`
- **Evidence Review**: The author explicitly operates a small multi-client agency. They report "burning months on manual testing" across tools and executing recurring manual prompt testing for 20 high-priority client queries weekly per account because automated tools miss citations. They subsequently spend hours stitching disparate outputs into Looker Studio for monthly reporting.
- **Audit Decision**: **ELIGIBLE FOR GATE 3**. This is first-hand evidence of repeated, costly internal agency labor dedicated to the exact target job (weekly prompt verification and monthly client deliverable generation).

### Candidate Signal 2: Arash-60 (Tool Use vs. Paid Spend)
- **ID**: `geo-pain-reddit-arash60-defensive-monthly-client-reporting`
- **Speaker / Source**: `Arash-60` on `r/seogrowth`
- **Audit Status**: `VERIFIED` | **Scope**: `IN_SCOPE` (`GEO-AGENCY-01`)
- **Signal**: Normalized from `saas_spend` to `null`
- **Evidence Review**: Live source inspection of comment `o3bbluh` confirms that Arash-60 uses Guzu.ai to establish client baseline rankings at contract inception and delivers monthly percentage change reports. However, the text contains zero evidence that the agency pays for Guzu.ai (it may be a free tier, trial, or client-provided seat). In accordance with Rule 6 (separate observation from interpretation) and the Evidence Standard, tool adoption cannot be promoted to revealed spending without direct proof of payment.
- **Audit Decision**: **EXCLUDED FROM GATE 3**. Eligible for G1 (pain) and G2 (monthly recurrence), but canonical field `money_signal` is normalized to `null`.

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
- **Audit Status**: `PARTIALLY_VERIFIED` | **Scope**: `IN_SCOPE`
- **Signal**: `employee_time` (disallowed)
- **Evidence Review**: Stanislava Smiljanic is an in-scope agency co-founder (SORN.AI, 2–10 staff). However, her quote states: *"Without a specialized tool, tracking prompts would be very manual, with a ton of print screens and manual research of prompts with VPN, Stanislava says of the alternative."* The phrasing explicitly describes a hypothetical alternative ("would be very manual..."), not a verified record of hours actually logged or payroll spent performing manual checks.
- **Audit Decision**: **EXCLUDED FROM GATE 3**. Reclassified as `PARTIALLY_VERIFIED`. Counterfactual descriptions of what work *would* be needed in the absence of tools cannot substitute for observed labor expenditure.

### Candidate Signal 5: maltelandwehr / Peec AI User (Unverified Scope)
- **ID**: `geo-wtp-reddit-peec-usage`
- **Speaker / Source**: `maltelandwehr` on `r/SEO`
- **Audit Status**: `VERIFIED` | **Scope**: `UNKNOWN`
- **Signal**: `saas_spend`
- **Evidence Review**: The author explicitly confirms paying for and using Peec AI for visibility reporting and content optimization. However, their organizational identity, agency affiliation, and team size cannot be verified against the 2–20 employee threshold of `GEO-AGENCY-01`.
- **Audit Decision**: **EXCLUDED FROM GATE 3**. Under strict scope integrity rules, evidence from practitioners whose team size or business model is UNKNOWN cannot be pooled into the candidate ICP count.

### Candidate Signal 6: UK PR Agency Upwork Contract (Access Blocked)
- **ID**: `geo-wtp-upwork-pr-agency-contract`
- **Speaker / Source**: `UK PR Agency` on `upwork.com`
- **Audit Status**: `PENDING` | **Scope**: `UNKNOWN`
- **Signal**: `stated_wtp`
- **Evidence Review**: Retrieval was blocked by Cloudflare Turnstile anti-bot protection (HTTP 403). Under repository rules 25–27, automated scraping workarounds are prohibited.
- **Audit Decision**: **EXCLUDED FROM GATE 3**. Retained as `PENDING` and cannot be counted toward any threshold.

### Summary of Gate 3 Eligibility
- **Counted Independent Signals**: **1** (`geo-pain-reddit-typicalbadger-patchwork-stack`, `Typical-Badger1922`)
- **Policy v2 Threshold**: $\ge 3$ independent signals
- **Audit Outcome**: **GATE 3 STATUS IS UNKNOWN**.
- **Implication**: This shortfall does not cause a FAIL verdict under v2 policy. Instead, it fulfills the exact condition for `CONDITIONAL PASS`, where unverified willingness to pay is designated as an explicit interview topic to be resolved during limited customer discovery ($n \le 8$ interviews).

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

---

## 3. Strongest Positive Evidence (ICP & Workflow Coherence)

The bounded dataset establishes strong evidence for problem existence and operational workflow:

1. **Direct Agency Pain & Client Anxiety**:
   - `nothabkuuys` (`geo-pain-reddit-nothabkuuys-small-agency-client-anxiety`): Small agency owner describes intense friction managing SMB client expectations across Google AIO, ChatGPT, and Claude, and confusion over billing models.
   - `Typical-Badger1922` (`geo-pain-reddit-typicalbadger-patchwork-stack`): Documents weekly prompt checking routines and the necessity of stitching data into Looker Studio to demonstrate trendlines to clients.
2. **Verified Boutique Agency Workflow Profiles**:
   - `What IF Web` (`geo-workflow-01-whatifweb-profile`, 3–5 staff): Confirms client traffic erosion triggers AI optimization audits; prompts are modeled from sales conversations; deliverables focus on citability and directory presence.
   - `SORN.AI` (`geo-workflow-04-sornai-profile`, `geo-workflow-06-sornai-reporting-cadence`, 2–10 staff): Delivers weekly AI visibility reports using Brand Visibility Index quadrant charts comparing clients against 4 competitors.
   - `Butter Marketing` (`geo-workflow-07-butter-marketing-profile`, 2–9 staff): Verified London agency on Clutch dedicating 70% of operations to Generative Engine Optimization.
3. **Targeted Acquisition Channel**:
   - `Clutch Directory` (`geo-workflow-11-reachability-clutch`): Provides verified public directory filters specifically segmenting independent agencies by headcount (2–9 and 10–49 employees) and service line (GEO / SEO).

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

## 5. Decision Architecture for Stage 1 Judge

Under Policy v2, this evidence structure provides a coherent, grounded basis for decision-making:
- **G1 (Concrete Pain)**: 6 independent verified in-scope records $\rightarrow$ **PASS**.
- **G2 (Recurrence)**: Weekly and monthly client reporting cadences $\rightarrow$ **PASS**.
- **G3 (Existing Spend / WTP)**: 1 verified labor record vs. 3 required $\rightarrow$ **UNKNOWN**.
- **G4 (Repeatable Gap)**: Clustered around `client_reporting_rework_under_volatility` $\rightarrow$ **PASS**.
- **G5 (ICP Reachability)**: Clutch directory filter $\rightarrow$ **PASS**.
- **G6 (No Killer Substitute)**: Verified context; no killer substitute $\rightarrow$ **PASS**.

This distribution matches the exact prerequisites for **`CONDITIONAL PASS`** under v2 policy:
- G1 and G5 pass;
- No gate fails;
- The single UNKNOWN gate (G3) can be addressed via limited customer discovery interviews ($n \le 8$), structured specifically to verify whether agency buyers will pay $\ge \$100$/mo for automated reporting or will continue relying on bundled suite add-ons and manual spot-checks.
