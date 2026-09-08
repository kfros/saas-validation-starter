# Stage 1 Skeptic Research Case — GEO-AGENCY-01

**Idea:** `geo-monitoring`  
**Scope:** `GEO-AGENCY-01` (Independent SEO agencies with 2–20 staff serving SMB clients on recurring engagements)  
**Evaluation Date:** 2026-09-08  
**Research Track:** Skeptic Research  
**Status:** COMPLETE (Planned discovery search completed)  

---

## 1. Hypothesis and Scope Tested

### 1.1 Hypothesis Tested
> Small independent SEO agencies with recurring SMB client engagements spend meaningful recurring effort checking brand visibility in AI answers and turning inconsistent observations into defensible client reports. They may pay for multi-client monitoring that preserves inspectable answer/source evidence, separates noise from comparable changes, and produces a concise report linked to a concrete agency decision. Existing trackers, SEO suites, and manual checks may already solve this sufficiently; research must test that.

### 1.2 Target Scope Definition (GEO-AGENCY-01)
- **Organization:** Independent boutique SEO agency (2–20 staff) serving SMB clients on recurring retainers ($300–$1,000/mo per client).
- **Buyer:** Agency Owner, Managing Director, or Head of SEO with credit card / software purchasing authority.
- **Operator:** SEO specialist or account manager compiling monthly/quarterly client deliverables.
- **Deliverable:** Inspectable per-client AI visibility, brand citation, and comparative ranking report.
- **Proposed Wedge:** Multi-client monitoring dashboard with noise-aware change detection, citation verification snapshots, and white-label client reporting.

### 1.3 Skeptic Mandate
Test whether this hypothesis is a commercially unviable business by investigating:
1. Direct substitute trackers and incumbent SEO-suite bundling.
2. Low recurrence and the dominance of one-off sales audits over recurring monitoring.
3. Agency margin collapse and client demand for content/authority execution over dashboards.
4. Technical roadblocks: API vs consumer UI divergence, sampling stochasticity (temperature noise), prohibitive web-grounding API costs, and platform Terms of Service / legal scraping barriers.

---

## 2. Substitute Assessment Matrix

For each candidate substitute, we evaluate:
1. **Capability:** Target workflow steps performed.
2. **ICP / Output Fit:** Alignment with SMB SEO agency multi-client needs and client deliverable formats.
3. **Price & Friction:** Sourced vendor pricing, user setup overhead, and seat/project limits.
4. **Adoption & Sufficiency:** Public practitioner adoption or perceived sufficiency.
5. **Key Unknowns:** Unresolved empirical gaps.
6. **Evidence IDs:** Verified or pending records backing each finding.

| Substitute | Capability | ICP / Output Fit | Price & Friction | Adoption & Sufficiency | Key Unknowns | Evidence IDs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Ahrefs Brand Radar** | Tracks brand mentions and AI search visibility across 6 platforms (Google AIO, ChatGPT, Gemini, Perplexity, Copilot, AI Mode). 459M search-backed prompt index; free crawler analytics. | High fit for agencies already subscribing to Ahrefs. Branded exports and web analytics integration. | **Zero marginal cost** for custom prompt tracking on paid plans ($129–$199+/mo). AI Visibility Index add-on starts at $199/mo across 459M prompts. | High suite adoption among SEO agencies. Practitioners view it as natural extension of existing stack. | Granular client reporting automation and custom prompt refresh frequency limits. | `geo-skeptic-substitute-ahrefs-brand-radar` |
| **Semrush AI Visibility Toolkit / Semrush One** | Tracks custom prompts across ChatGPT Search, Google AI Mode, Gemini; native Google AIO SERP filters. Captures brand mentions, owned sources, average citation rank, and stored SERP snapshots. | High fit. Includes client-facing branded PDF, Excel, and Google Sheets exports. Bundled in Semrush One tiers (5–40 websites, 50–200 prompts). | Bundled into Semrush One tiers or standalone toolkit (25 prompts). Zero additional procurement hurdle for existing Semrush agency users. | Widespread suite presence. Some practitioners note daily tracking is not as indispensable as core rank tracking (`sammyp99`). | Exact pricing of standalone toolkit outside Semrush One bundles; multi-client white-label customization limits. | `geo-skeptic-substitute-semrush-ai-tracking` |
| **Peec AI** | Dedicated AI search monitoring dashboard across models. Shareable links, Looker Studio templates, scheduled reports, CSV export. | Medium-low fit. Severe client project artificial caps: Essential tier allows only 1 client project; Growth allows 3; Scale allows 10. | **High friction/price:** €205/mo (1 client), €425/mo (3 clients), €675/mo (10 clients). 1 credit = 1 prompt × 1 model × 1 day. | Raised $29M, strong marketing presence, but agency tiers are cost-prohibitive for SMB client retainers. | Agency churn rates and exact adoption of Looker Studio templates. | `geo-skeptic-substitute-peec-pricing` |
| **Profound (tryprofound.com)** | Answer engine insights, citation tracking, sentiment, competitor analysis across ChatGPT, Perplexity, Google AIO. | Low fit for ongoing SMB retainers. Focuses heavily on pre-sales pitch audits rather than ongoing client monitoring. | **Extreme friction/price:** $99/mo base plan includes **zero** permanent client workspaces (only 10 7-day pitch workspaces). Client workspaces cost **$399/mo per client**. | Backed by venture funding; used by enterprise brands. Disliked by small agencies due to per-client price gouging. | Retention rates of agency subscribers beyond initial pitch workspace trials. | `geo-skeptic-substitute-profound-pricing`, `geo-skeptic-risk-clickstream-panel-sourcing` |
| **Otterly.ai** | AI search monitoring across ChatGPT, Google AIO, Perplexity, Copilot. Daily checks, Looker Studio connector, agency pitch workspaces. | Moderate fit. Agency partner requires Standard (€189/mo for 150 prompts) or Premium (€489/mo for 500 prompts). White-labeling offloaded to Looker Studio. | Steep add-ons: Claude support costs +€29 to +€439/mo extra; Gemini costs +€9 to +€149/mo extra; extra 100 prompts cost €99/mo. | Active presence in agency discussions; cited as functional but restrictive prompt caps. | Agency renewal rates after trial periods; stability of Looker Studio connector. | `geo-skeptic-substitute-otterly-pricing` |
| **Rankscale.ai** | Multi-engine brand tracking, white-labeled dashboard links, CSV/Sheets exports, Looker Studio integration. | Moderate fit. Growth plan (€385/mo) supports 50 brand dashboards (~€7.70/client/mo) and 5,500 credits. | Entry Pro is €99/mo (10 brands). Agency Growth is €385/mo. White-labeling available with API. | Emerging direct tracker offering agency-specific dashboard packaging. | User base scale and data accuracy compared to manual searches. | `geo-skeptic-substitute-rankscale-pricing` |
| **Manual Spot-Checks + Spreadsheets** | Manual testing of 10–20 prompts directly in ChatGPT, Perplexity, and Google Search; screenshots pasted into Google Slides/Sheets. | Perfect fit for low-volume SMB clients. Free, zero software procurement, preserves real consumer UI fidelity. | Zero software subscription cost; consumes 1–2 hours of junior SEO staff time per month ($25–$50 labor). | Widely reported on r/SEO and r/agency as the standard agency fallback when software dashboards provide volatile data. | Exact labor hours across different agency sizes; client satisfaction with manual Google Slides decks. | `geo-skeptic-pain-seo-dashboards-vs-manual`, `geo-skeptic-pain-agency-demand-execution` |

---

## 3. Strongest Recurrence Objection: The "One-Off Pitch Audit" Dominance

### 3.1 Empirical Finding
Agencies and clients do not experience AI visibility monitoring as a recurring, high-frequency operational necessity. Instead, demand is heavily concentrated in **one-off pre-sales audits** and **quarterly business review (QBR) talking points**.

### 3.2 Evidence & Practitioner Quotes
- **Vendor Structure Reflects Demand Reality:** Both Profound and Peec AI have built their agency tiers explicitly around temporary "Pitch Workspaces" (Profound gives 10 temporary 7-day workspaces for $99/mo; Peec gives 3–7 7-day pitch projects). Vendors themselves recognize agencies want to run a quick audit to close a new client, not pay ongoing monthly seat/workspace fees (`geo-skeptic-substitute-profound-pricing`, `geo-skeptic-substitute-peec-pricing`).
- **Practitioner Consensus on Cadence:** On `r/agency`, agency owners explicitly advise against monthly monitoring deliverables:
  > *"Don't create a separate line item (yet). If you start charging separately for 'AI optimization,' you're now on the hook to prove ROI on something with almost no reliable tracking... package a quarterly 'AI Visibility Audit' as an add-on or a QBR talking point... The people selling 'AIO packages' right now are mostly repackaging content strategy."* (`geo-skeptic-pain-agency-demand-execution`, `geo-skeptic-pain-agency-lack-reliable-tracking`).
- **Low Decision Value of Daily/Weekly Fluctuation:** AI search answer generation is stochastic. Trackers report wild visibility swings (+30% one week, -40% the next) due to prompt phrasing variations and model temperature. Showing volatile daily graphs to SMB clients creates client panic and billing disputes rather than actionable recurring agency workflows (`geo-skeptic-pain-seo-prompt-fantasy-roi`, `geo-skeptic-pain-seo-dashboards-vs-manual`).

---

## 4. Strongest Willingness-to-Pay (WTP) Objection: The Agency Margin Squeeze

### 4.1 Empirical Retainer Economics
- Verified agency pricing for SMB GEO services (e.g., Butter Marketing) reveals client retainers of **$399/month** for dedicated GEO (monthly prompt testing, schema markup, 1 citation/backlink, monthly report) and **$699/month** for combined GEO + SEO (8 articles, 3 backlinks, on-page optimization) (`geo-skeptic-market-butter-agency-pricing`).
- SMB agencies typically operate on gross margins of 50%–70% to cover labor, overhead, and core tool subscriptions.

### 4.2 Software Cost vs Retainer Math
1. **Profound:** Charges $99/mo base + $399/month *per client workspace*. A $399/mo software cost on a $399/mo client retainer represents **100% software cost (0% agency margin)** (`geo-skeptic-substitute-profound-pricing`).
2. **Peec AI:** Scale plan costs €675/mo (~$730/mo) for 10 client projects, or ~$73/client/mo. On a $399 retainer, software consumes ~18.3% of top-line revenue just for tracking, before content writing, backlinks, or labor (`geo-skeptic-substitute-peec-pricing`).
3. **Incumbent Squeeze:** Agencies already spend $200–$500/mo on Ahrefs or Semrush. When Ahrefs includes custom prompt tracking for free and Semrush bundles prompt tracking into Semrush One plans, spending an incremental $100–$300/mo on a dedicated tracker is rejected by agency owners (`geo-skeptic-substitute-ahrefs-brand-radar`, `geo-skeptic-substitute-semrush-ai-tracking`).
4. **Client Demand is for Content Execution, Not Dashboards:** SMB clients pay agencies to *fix* visibility through tangible deliverables: writing blog posts, digital PR, publishing YouTube/LinkedIn content, and building structured data. A monitoring tool produces no content, leaving the agency to bear both the monitoring cost and the execution labor (`geo-skeptic-pain-agency-demand-execution`, `geo-skeptic-pain-agency-lack-reliable-tracking`).

---

## 5. Strongest Adoption and Procurement Blocker: Incumbent SEO Suites

### 5.1 The "Good Enough" Bundled Moat
Small agencies fiercely resist tool sprawl. A specialized point solution must offer an order-of-magnitude improvement over existing suites to justify a separate recurring subscription.
- **Ahrefs Brand Radar:** Ahrefs has integrated custom prompt tracking across Google AIO, ChatGPT, Gemini, Perplexity, Copilot, and AI Mode directly into standard subscriptions at **no extra charge**. Furthermore, Ahrefs queries a pre-computed database of 459 million search-backed prompts for $199/month, offering scale that no startup can match (`geo-skeptic-substitute-ahrefs-brand-radar`).
- **Semrush AI Visibility Toolkit:** Semrush has bundled multi-model prompt tracking (ChatGPT Search, AI Mode, Gemini) with brand mention counts, owned source breakdowns, citation placement, and stored SERP verification snapshots directly into Semrush One subscriptions (`geo-skeptic-substitute-semrush-ai-tracking`).
- **The Outcome:** Agency operators who already manage client SEO inside Semrush or Ahrefs have zero incentive to log into a separate tool or pay another monthly invoice.

---

## 6. Strongest Technical & MVP Blocker: Sampling Noise, API Divergence & Legal Barriers

### 6.1 Sampling Noise & The n=7 Statistical Imperative
- **Empirical Variance:** Peer-reviewed and measurement industry studies (Univ. of St. Gallen, arXiv:2604.07585; arXiv:2601.21339) demonstrate that LLM answer generation varies **10% to 34% from sampling alone** on identical prompts due to non-zero model temperature (`geo-skeptic-risk-sampling-noise-variance`).
- **Standard Error of Single Check:** A single prompt check carries an unacceptable **standard error of ±0.37**. Achieving basic statistical stability (standard error < 0.10) requires a minimum sample size of **n = 7 repeated queries per prompt per surface** (`geo-skeptic-risk-sampling-noise-variance`).
- **The Economic Trap:** Any tool that runs single-shot queries delivers random noise ("astrology"). But running 7 repeats across 50 client prompts and 4 engines requires **1,400 grounded model calls per client audit**, making infrastructure costs explode.

### 6.2 The UI vs API Dilemma
- **Vendor Technical Admission:** Profound's Head of Engineering publicly acknowledged that querying official LLM APIs produces radically different results from what users see in consumer browser interfaces (ChatGPT Search, Perplexity, Google AI Overviews). Consumer UIs use multi-stage dynamic query fanout, personalized session context, and real-time retrieval routing that static API calls miss (`geo-skeptic-risk-api-vs-consumer-divergence`).
- **The Catch-22:**
  - If a startup uses official APIs: The data does not match what the client sees on their laptop, leading to client disputes and cancellations (`geo-skeptic-pain-seo-dashboards-vs-manual`, `geo-skeptic-risk-api-vs-consumer-divergence`).
  - If a startup scrapes consumer UIs: It directly violates OpenAI's Terms of Use (Updated Jan 2026), which prohibit programmatic extraction and safety mitigation bypass (`geo-skeptic-risk-openai-tos-scraping`), triggering Cloudflare Turnstile blocks, IP bans, and permanent platform shutdown.

### 6.3 Third-Party Clickstream Panel Dependence
- Even venture-funded trackers like Profound do not possess proprietary search volume data. They purchase clickstream panels from browser extension brokers (e.g., Datos). These panels only capture the initial prompt query string, leaving conversational follow-ups and true user query distributions estimated or synthesized via LLMs (`geo-skeptic-risk-clickstream-panel-sourcing`, `geo-skeptic-pain-seo-prompt-fantasy-roi`). A solo technical founder cannot credibly license or maintain multi-million-dollar clickstream datasets.

---

## 7. Workload Economics Worksheet (Research-Brief Specification)

Below is the sourced-or-unknown scenario analysis specified in `ideas/geo-monitoring/research-brief.md`.

### 7.1 Scenario Formula
$$\text{observations/month} = \text{clients} \times \frac{\text{prompts}}{\text{client}} \times \text{surfaces} \times \text{locale\_variants} \times \text{repetitions} \times \frac{\text{checks}}{\text{month}}$$

### 7.2 Sourced Unit Cost Parameters
From official documentation gathered in this research:
1. **OpenAI Web Search Tool:** $10.00 / 1,000 search calls + token costs (~$15.00/1k total) (`geo-skeptic-risk-openai-search-pricing`).
2. **Google Gemini Search Grounding:** $14.00 / 1,000 prompts (Gemini 3) to $35.00 / 1,000 prompts (Gemini 2.5) + tokens (~$16.00 – $38.00/1k total) (`geo-skeptic-risk-gemini-grounding-pricing`).
3. **Perplexity Sonar API:** $5.00 – $14.00 / 1,000 requests + tokens (~$8.00 – $18.00/1k total) (`geo-skeptic-risk-perplexity-api-pricing`).
4. **Blended Average API Cost per Grounded Observation:** **$16.00 per 1,000 observations** ($0.016 / observation).
5. **Retry Overhead:** 5% on transient network/API timeouts.
6. **Parsing, Snapshot Storage & Embedding Overhead:** Estimated at $1.50 per 1,000 observations.
7. **Total Operating COGS per 1,000 Observations:** **$18.30** ($0.0183 / observation).

---

### 7.3 Scenario Models

#### Scenario A: Low (Minimal Ad-Hoc / Single Monthly Check, Single Repetition)
*Assumptions:* Agency runs 1 check per month for 5 SMB clients, 15 prompts each, across 2 surfaces (ChatGPT, Google AIO), 1 locale, 1 repetition (n=1, accepting ±0.37 standard error).
- **Parameters:**
  - Clients: 5
  - Prompts/client: 15
  - Surfaces: 2
  - Locales: 1
  - Repetitions: 1 (single check)
  - Checks/month: 1
- **Observations/Month:** $5 \times 15 \times 2 \times 1 \times 1 \times 1 = \mathbf{150 \text{ observations/month}}$
- **Direct API & Supplier Cost:** $150 \times \$0.0183 = \mathbf{\$2.75 / \text{month}}$
- **Analysis:** Financially trivial, but statistically invalid (standard error ±0.37). Delivers volatile "astrology" data that leads to client churn.

---

#### Scenario B: Base (Statistically Valid Weekly Monitoring for 10 Clients)
*Assumptions:* Standard boutique agency monitoring 10 clients, 25 prompts each, across 3 surfaces (ChatGPT, Google AIO, Perplexity), 1 locale, with statistical validity ($n = 7$ repetitions per St. Gallen benchmark), checked weekly (4 times/month).
- **Parameters:**
  - Clients: 10
  - Prompts/client: 25
  - Surfaces: 3
  - Locales: 1
  - Repetitions: 7 ($n=7$ required to achieve $\text{SE} < 0.10$)
  - Checks/month: 4 (weekly)
- **Observations/Month:** $10 \times 25 \times 3 \times 1 \times 7 \times 4 = \mathbf{21,000 \text{ observations/month}}$
- **Cost Breakdown:**
  - ChatGPT Search (7,000 calls @ $15/1k): $105.00
  - Google Gemini Grounding (7,000 calls @ $16/1k): $112.00
  - Perplexity Sonar (7,000 calls @ $8/1k): $56.00
  - Subtotal Raw API: $273.00
  - 5% Retry Overhead: $13.65
  - Snapshot Storage, DB & Ingestion: $25.00
  - **Total Monthly COGS:** $\mathbf{\$311.65 / \text{month}}$
- **Comparison to Buyer WTP:**
  - Target agency ARPU hypothesis: **$100.00 / agency / month**.
  - **Gross Margin:** $\$100.00 - \$311.65 = \mathbf{-\$211.65 / \text{month} \quad (-211\% \text{ Gross Margin})}$.
  - Even if billed per client at $15/client/month ($150 total for 10 clients), the SaaS still loses $161.65/month on direct infrastructure alone.
  - To achieve a standard 70% SaaS gross margin, the founder would need to charge **$1,038 / month** for 10 clients (~$104 / client / month). SMB agencies charging $399/mo retainers will not pay $104/mo per client for software.

---

#### Scenario C: High (Daily Multi-Locale Tracking at Agency Scale)
*Assumptions:* Growing agency with 20 clients, 50 prompts each, across 4 surfaces, 2 locales (US, UK), $n=7$ repetitions, tracked daily (30 days/month).
- **Parameters:**
  - Clients: 20
  - Prompts/client: 50
  - Surfaces: 4
  - Locales: 2
  - Repetitions: 7
  - Checks/month: 30 (daily)
- **Observations/Month:** $20 \times 50 \times 4 \times 2 \times 7 \times 30 = \mathbf{1,680,000 \text{ observations/month}}$
- **Total Monthly COGS:** $1,680,000 \times \$0.0183 = \mathbf{\$30,744 / \text{month}}$
- **Analysis:** Multi-client daily tracking at statistical validity is completely economically prohibitive for any small B2B SaaS without proprietary search engine infrastructure or discounted bulk agreements.

---

## 8. Evidence Sufficient to Rebut Each Skeptic Objection

To overturn this skeptic case and justify a Stage 2 progression for `GEO-AGENCY-01`, future research or customer discovery would need to provide verified evidence for the following:

1. **Rebutting the Recurrence Objection:**
   - Document at least 5 independent boutique agencies that routinely deliver weekly or monthly AI search reports to SMB clients as a contractual retainer deliverable, with evidence of client retention exceeding 6 months.
2. **Rebutting the WTP / Margin Objection:**
   - Prove that agencies can successfully pass through a $100–$250/mo monitoring software fee to SMB clients, or demonstrate that agencies achieve measurable labor savings exceeding $300/month by replacing manual checks with software.
3. **Rebutting the Incumbent Suite Objection:**
   - Identify a critical, non-negotiable agency workflow gap in Ahrefs Brand Radar and Semrush AI Visibility Toolkit (e.g., specific white-label client approval workflows or deterministic citation verification) that suite vendors cannot easily copy.
4. **Rebutting the Statistical / Cost Objection:**
   - Provide a mathematically verified sampling methodology that achieves acceptable statistical confidence ($\text{SE} < 0.10$) with $n \le 2$ calls, reducing base COGS below $30/month for 10 clients.
5. **Rebutting the Legal / Platform Risk:**
   - Obtain formal, published commercial developer terms from OpenAI permitting automated recurring queries of consumer ChatGPT Search without risking account termination.

---

## 9. Candidate New Scopes Discovered (Explicitly Marked UNVALIDATED)

During discovery, three adjacent product and ICP directions emerged. Per protocol, these are **UNVALIDATED** and cannot rescue `GEO-AGENCY-01`:

1. **Scope Candidate: UNVALIDATED-GEO-PRE-SALES-AUDIT**
   - *Concept:* A pay-per-report or low-tier subscription tool ($49–$99/mo) designed purely for **pre-sales pitch audits**. Agencies run a high-fidelity snapshot of a prospect's AI visibility gaps to include in sales proposals to close new retainer clients.
   - *Rationale:* Aligns with current agency behavior (using Profound/Peec pitch workspaces) without requiring ongoing monthly client monitoring.
2. **Scope Candidate: UNVALIDATED-GEO-CONTENT-REMEDIATION**
   - *Concept:* An automated execution tool that scans AI citations, detects missing client brand mentions in top-cited URLs (e.g., Reddit threads, listicles, review roundups), and generates automated outreach/content actions (e.g., MentionBird / Byword models).
   - *Rationale:* Aligns with client willingness to pay for *fixing* visibility and creating content rather than watching graphs.
3. **Scope Candidate: UNVALIDATED-ENTERPRISE-BRAND-PR-MONITORING**
   - *Concept:* Enterprise brand reputation monitoring for in-house corporate communications and PR teams tracking brand sentiment, hallucination, and executive mentions across LLMs.
   - *Rationale:* Enterprise buyers have budgets ($1,000–$5,000/mo) that comfortably absorb $300+ API observation COGS.

---

## 10. Research Shortfall and Tooling Blockers

1. **Tool Capacity / Rate Limits:**
   - During parent agent execution, the `search_web` tool returned HTTP 503 `MODEL_CAPACITY_EXHAUSTED` for `gemini-3.1-flash-lite`, and `read_url_content` was blocked by Cloudflare (HTTP 403) on certain vendor sites (e.g. OpenAI).
   - Per protocol, research was conducted via the dedicated `browser` subagent utilizing Chrome DevTools MCP navigation (`mcp_chrome_devtools_navigate_page`) to inspect primary vendor pricing pages, knowledge bases, legal policies, and practitioner forums.
2. **Missing Coverage / Unknowns:**
   - Exact churn rates of direct trackers (Otterly, Peec, Profound) could not be verified from public financial records (privately held companies).
   - Exact client-facing white-label customization options inside Semrush One's newest AI Visibility Toolkit remain partially unknown.
3. **Protocol Adherence:**
   - All 18 raw records are initialized with `audit_status: PENDING`.
   - All records use the stable prefix `geo-skeptic-`.
   - No Stage 1 gate verdict is issued in this report.
