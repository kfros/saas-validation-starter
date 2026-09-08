# Workflow Map: GEO-AGENCY-01 (Small Independent SEO Agencies)

## 1. Executive Summary & Scope

* **Idea**: `geo-monitoring` (Agency-first GEO / AI-search visibility monitoring)
* **Target Scope**: `GEO-AGENCY-01`
* **Definition**: Independent SEO agencies with 2–20 staff serving SMB clients on recurring retainer engagements.
* **Evaluation Context**: Stage 1 Workflow Research (pre-interview mapping). Raw evidence status is `PENDING`. No Stage 1 verdict is rendered in this document.

---

## 2. Core Workflow Anatomy

### 2.1 Operator vs. Budget Owner

* **Actual Operator**: 
  * **Boutique Agency Co-founder / Technical Lead**: In micro-teams (2–5 staff), founders handle prompt curation, technical crawl checks, and report building directly (e.g. Isaac Farrow at What IF Web [`geo-workflow-01-whatifweb-profile`](#), [`geo-workflow-02-whatifweb-workflow`](#)).
  * **Dedicated SEO / GEO Strategist**: In slightly larger independent agencies (5–20 staff), a specialized SEO/GEO strategist or senior technical SEO performs prompt modeling, entity checks, and dashboard setup (e.g. Stanislava Smiljanic at SORN.AI [`geo-workflow-05-sornai-workflow`](#)).
* **Budget Owner**:
  * Agency Owner, Managing Director, or Head of SEO with discretionary tool budget authority (e.g. Eri Georgiev at SORN.AI [`geo-workflow-05-sornai-workflow`](#)).
  * In micro-agencies, the operator and budget owner are often the same individual (the founder/managing partner).

### 2.2 Triggers (Starting the Workflow)

1. **Client Retention / Traffic Erosion Inquiries**: SMB and SaaS clients notice traffic softening even while holding top traditional SERP rankings, caused by Google AI Overviews intercepting search clicks ([`geo-workflow-02-whatifweb-workflow`](#)).
2. **Scheduled Retainer Reporting Cycle**: Monthly or weekly contractual reporting deliverables requiring visibility updates to justify retainers ([`geo-workflow-03-whatifweb-deliverable`](#), [`geo-workflow-06-sornai-reporting-cadence`](#)).
3. **Pre-Sales Prospect Audits ("Pitch Projects")**: Agencies use prompt visibility and citation gap audits during prospect pitches to prove absence in AI search and close new client retainers ([`geo-workflow-05-sornai-workflow`](#), [`geo-workflow-13-peec-agency-substitute`](#)).

### 2.3 Inputs

* **Client Entity Context**: Core brand domain, brand names, product lines, and 3–5 explicit direct competitors.
* **Curated Prompt Sets**: Rather than high-volume static keywords, agencies build 15–25 natural language buyer queries derived collaboratively from client sales conversations, customer surveys, and GSC queries ([`geo-workflow-02-whatifweb-workflow`](#)). Prompts span 4 functional buckets: category-defining, comparison ("Brand A vs Brand B"), problem-solving ("how to fix X"), and branded sentiment.
* **Target Engine Surfaces**: Google AI Overviews (primary SERP surface), ChatGPT (leading conversational assistant), Perplexity (research engine), Gemini, Microsoft Copilot, and Claude ([`geo-workflow-02-whatifweb-workflow`](#), [`geo-workflow-10-embarque-deliverable`](#)).

### 2.4 Observation Surface & Measurement

* **Prompt Execution**: Running prompts systematically across designated surfaces and locales.
* **Data Capture Fields**:
  * Brand mention frequency (present vs. absent).
  * Domain citation / source attribution (is the client URL linked as a source?).
  * Competitor citation share (which competing domains took citations).
  * Answer rank / position within multi-source AI answers.

### 2.5 Review & Quality Assurance Steps

1. **Crawlability & Server Access Verification**: Checking `robots.txt` and server logs to verify AI crawlers (GPTBot, PerplexityBot, ClaudeBot) are not blocked by server firewalls or CMS settings ([`geo-workflow-02-whatifweb-workflow`](#), [`geo-workflow-05-sornai-workflow`](#)).
2. **Entity Consistency Audit**: Verifying that LLMs resolve the brand as a coherent entity across major public knowledge bases and directories (e.g. Clutch, Crunchbase, Wikipedia) ([`geo-workflow-03-whatifweb-deliverable`](#), [`geo-workflow-05-sornai-workflow`](#)).
3. **Citation & Hallucination Filtering**: Manually reviewing whether cited URLs exist and accurately reflect client offerings versus hallucinated attributions ([`geo-workflow-02-whatifweb-workflow`](#)).
4. **On-Page Answer Structure Check**: Checking whether client landing pages contain concise, inverted-pyramid prompt answers, question-based H2s, and HTML tables rather than CSS grids or images ([`geo-workflow-02-whatifweb-workflow`](#), [`geo-workflow-05-sornai-workflow`](#)).

### 2.6 Client Deliverable

* **Deliverable Formats**:
  * **Branded Looker Studio Dashboards**: Cloned or connected dashboards displaying automated citation trends alongside GA4/GSC organic data ([`geo-workflow-15-otterly-looker-studio-connector`](#), [`geo-workflow-13-peec-agency-substitute`](#)).
  * **Competitive Visibility Quadrants / Pitch Decks**: Visual competitor benchmarking graphs (e.g. Brand Visibility Index quadrant charts) comparing the client to 4 named competitors ([`geo-workflow-06-sornai-reporting-cadence`](#)).
  * **One-off AI Search Health Check Reports**: Initial baseline audit documents evaluating citability, crawler access, and citation gaps ([`geo-workflow-03-whatifweb-deliverable`](#), [`geo-workflow-10-embarque-deliverable`](#)).
* **Value Framing ("Citability Over Traffic")**: Boutique agencies explicitly frame deliverables around **Citability** and **Share of Voice** across target prompt sets, deliberately avoiding traffic or revenue guarantees due to zero-click AI answer dynamics ([`geo-workflow-03-whatifweb-deliverable`](#)).

### 2.7 Actions Taken After the Report

1. **Technical Remediation**: Unblocking AI user agents in `robots.txt`, cleaning reference CMS sitemaps, and fixing server response codes ([`geo-workflow-02-whatifweb-workflow`](#)).
2. **Structured Data Implementation**: Writing and injecting custom JSON-LD schema (FAQ, Organization, Product, Author) to feed structured entity facts to LLMs ([`geo-workflow-05-sornai-workflow`](#), [`geo-workflow-06-sornai-reporting-cadence`](#), [`geo-workflow-08-butter-marketing-offer`](#)).
3. **Prompt-Led Content Inversion**: Updating existing landing pages so answers appear directly in the first paragraph, and structuring data into clean HTML tables ([`geo-workflow-05-sornai-workflow`](#)).
4. **Off-Page Directory & Citation Seeding**: Aligning entity data on high-authority directories (e.g. Clutch profiles) and earning mentions in trusted third-party listicles and community forums (Reddit) that LLMs heavily cite ([`geo-workflow-03-whatifweb-deliverable`](#), [`geo-workflow-06-sornai-reporting-cadence`](#)).

### 2.8 Recurrence & Cadence

* **Monthly Retainer Cadence**: Standard agency billing and reporting cadence for recurring client management ([`geo-workflow-03-whatifweb-deliverable`](#), [`geo-workflow-08-butter-marketing-offer`](#), [`geo-workflow-10-embarque-deliverable`](#)).
* **Weekly Monitoring Cadence**: Adopted by specialized AI SEO agencies due to rapid algorithmic fluctuations in LLM citations, allowing faster competitive counter-measures ([`geo-workflow-06-sornai-reporting-cadence`](#)).
* **Ad-Hoc Pre-Sales Audits**: Conducted on-demand during agency pitch processes to win new retainers ([`geo-workflow-05-sornai-workflow`](#), [`geo-workflow-13-peec-agency-substitute`](#)).

---

## 3. Current Alternatives & Tooling Landscape

| Alternative | Cost Tier | Role in Workflow | Agency Limitation / Friction |
| :--- | :--- | :--- | :--- |
| **Manual Spreadsheets + VPN + Screenshots** | $0 SaaS / High Labor | Operator manually enters prompts via VPN/incognito, takes screenshots, and tabulates citations ([`geo-workflow-12-manual-workaround-labor`](#)). | Unsustainable beyond 1–2 clients; zero historical tracking; cannot capture non-deterministic output variance; high billable labor burn. |
| **Otterly.ai** | Tiered SMB / Agency | Specialized prompt tracking across ChatGPT, Perplexity, Gemini, Copilot, AI Overviews; provides Looker Studio connector ([`geo-workflow-15-otterly-looker-studio-connector`](#)). | Focused solely on citation tracking; lacks integrated project task management or automated remediation scripts. |
| **Peec AI** | €175–€575/mo | Agency-oriented platform with "Pitch Projects", Looker Studio cloned templates, and multi-client workspace management ([`geo-workflow-13-peec-agency-substitute`](#)). | Direct commercial substitute for multi-client agency monitoring; entry barrier at €365/mo for small rosters. |
| **Traditional SEO Suites (Semrush, Ahrefs)** | $139–$499/mo | Tracks Google AI Overviews appearing in traditional Google SERPs ([`geo-workflow-14-semrush-substitute-gap`](#)). | **Critical Gap**: Blind to conversational chatbot engines (ChatGPT, Perplexity, Claude), forcing agencies to maintain secondary tools. |

---

## 4. Reachability & Stage 2 Discovery Strategy

### 4.1 Discovery Channels

1. **B2B Agency Directories (Clutch.co)**:
   * Public directory filtering allows isolating agencies by team size (2–9 and 10–49 employees), service line ("Generative Engine Optimization", "SEO"), and verified client reviews detailing reporting practices ([`geo-workflow-11-reachability-clutch`](#)).
2. **Direct Booking / Contact Surfaces**:
   * Independent agencies publicly expose owner/strategist booking routes (e.g. HubSpot/Calendly meeting schedulers, contact forms) directly on their websites for prospect and partner discovery ([`geo-workflow-01-whatifweb-profile`](#), [`geo-workflow-04-sornai-profile`](#), [`geo-workflow-08-butter-marketing-offer`](#), [`geo-workflow-10-embarque-deliverable`](#)).
3. **LinkedIn Advanced Search**:
   * Filter: Company Headcount (2–10, 11–50) + Industry ("Advertising Services", "Marketing Services") + Title ("Founder", "Managing Director", "Head of SEO", "SEO Strategist").

### 4.2 Illustrative Matching Agencies (Coverage Sample)

The following 4 independent agencies provide empirical coverage proof for `GEO-AGENCY-01`:

1. **What IF Web** (Christchurch, New Zealand)
   * Team Size: 3–5 staff.
   * Model: Boutique creative studio offering AI Search Health Checks and ongoing citability retainers using Otterly.ai.
   * Key People: Isaac Farrow (Co-founder / Developer).
   * Verifiable Linkage: [`geo-workflow-01-whatifweb-profile`](#), [`geo-workflow-02-whatifweb-workflow`](#), [`geo-workflow-03-whatifweb-deliverable`](#).
2. **SORN.AI** (Europe / Remote)
   * Team Size: 2–10 staff.
   * Model: Dedicated AI SEO agency offering weekly GEO visibility reporting and entity optimization.
   * Key People: Eri Georgiev (Co-founder), Stanislava Smiljanic (SEO & GEO Strategist).
   * Verifiable Linkage: [`geo-workflow-04-sornai-profile`](#), [`geo-workflow-05-sornai-workflow`](#), [`geo-workflow-06-sornai-reporting-cadence`](#).
3. **Butter Marketing** (London, UK)
   * Team Size: 2–9 employees (verified on Clutch).
   * Model: Packages standalone recurring GEO retainers ($399/mo) and combined GEO+SEO retainers ($699/mo).
   * Key People: Agency Management / Founder.
   * Verifiable Linkage: [`geo-workflow-07-butter-marketing-profile`](#), [`geo-workflow-08-butter-marketing-offer`](#).
4. **Embarque** (London, UK / Remote)
   * Team Size: 10–49 employees (~12–20 core staff on Clutch).
   * Model: SEO agency for high-growth SaaS SMBs offering multi-model AI citation audits and dedicated tracking dashboards.
   * Key People: Julian Song (Founder) / Agency Strategists.
   * Verifiable Linkage: [`geo-workflow-09-embarque-profile`](#), [`geo-workflow-10-embarque-deliverable`](#).

---

## 5. Evidence Reference Index

| Evidence ID | Type | Entity / Source | Core Finding |
| :--- | :--- | :--- | :--- |
| `geo-workflow-01-whatifweb-profile` | workflow | What IF Web | Boutique studio profile (3–5 staff, NZ, SMB/tech clients). |
| `geo-workflow-02-whatifweb-workflow` | workflow | What IF Web | Workflow triggers, sales-derived prompt sets, Otterly tracking. |
| `geo-workflow-03-whatifweb-deliverable` | workflow | What IF Web | Retainer deliverable framed as citability; post-report entity actions. |
| `geo-workflow-04-sornai-profile` | workflow | SORN.AI | Independent AI SEO agency profile (2–10 staff, remote). |
| `geo-workflow-05-sornai-workflow` | workflow | SORN.AI | SEO strategist operator, pitch audit trigger, entity/table review. |
| `geo-workflow-06-sornai-reporting-cadence` | recurrence | SORN.AI | Weekly reporting cadence, competitor quadrant graphs, schema actions. |
| `geo-workflow-07-butter-marketing-profile` | workflow | Butter Marketing | Clutch-verified agency profile (2–9 staff, 70% GEO focus). |
| `geo-workflow-08-butter-marketing-offer` | wtp | Butter Marketing | Standalone monthly recurring GEO retainer packaging ($399–$699/mo). |
| `geo-workflow-09-embarque-profile` | workflow | Embarque | Clutch-verified agency profile (10–49 staff, SaaS/SMB focus). |
| `geo-workflow-10-embarque-deliverable` | workflow | Embarque | Multi-model citation audits and dedicated client tracking dashboards. |
| `geo-workflow-11-reachability-clutch` | reachability | Clutch Directory | Public directory discovery channel with team size and service filters. |
| `geo-workflow-12-manual-workaround-labor` | substitute | SORN.AI / Strategist | Manual workaround friction (VPN + screenshots) driving tool adoption. |
| `geo-workflow-13-peec-agency-substitute` | substitute | Peec AI | Commercial multi-client agency substitute (€175–€575/mo). |
| `geo-workflow-14-semrush-substitute-gap` | substitute | AgencyDashboard | Incumbent SEO suite gap (tracks SERP AIO, blind to conversational LLMs). |
| `geo-workflow-15-otterly-looker-studio-connector` | workflow | Otterly.ai | Looker Studio connector as primary client reporting mechanism. |
