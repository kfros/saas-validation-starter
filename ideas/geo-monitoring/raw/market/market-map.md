# Market Map: Stage 1 Generative Engine Optimization (GEO) Tracking for Agencies

**Scope ID**: GEO-AGENCY-01  
**Target ICP**: Small independent SEO agencies (2–20 staff) serving SMB clients on recurring retainers  
**Core Job**: Recurring brand visibility tracking in AI search answers (ChatGPT, Google AI Overviews, Perplexity, Copilot, Gemini) and defensible, noise-aware client reporting  
**Evaluation Date**: 2026-09-08  
**Research Track**: Market Research (`raw/market/`)  

---

## 1. Executive Summary & Market Landscape

The market for AI-search visibility monitoring—commonly termed **Generative Engine Optimization (GEO)** or **Answer Engine Optimization (AEO)**—has experienced rapid commercial development over the past 12–18 months. As Google AI Overviews roll out globally and standalone AI engines (ChatGPT Search, Perplexity, Gemini, Copilot) capture increasing top-of-funnel query volume, marketing agencies face intense client demand to measure and report on AI search presence (`geo-market-searchengineland-metrics`).

The vendor landscape is currently bifurcated into two major forces, flanked by manual/DIY substitutes:
1. **Dedicated Pure-Play GEO Trackers**: Modern venture-backed platforms purpose-built for AI search monitoring (e.g., **Otterly.ai**, **Peec AI**, **Rankscale**, **Trakkr**, **Profound**). These platforms focus heavily on multi-engine scraping, citation analysis, prompt fanout, and automated agency pitch audits.
2. **Incumbent SEO Suites with Bundled GEO Modules**: Established enterprise and SMB SEO toolkits (e.g., **Semrush**, **SE Ranking**, **Ahrefs**) that have incorporated Google AI Overviews SERP tracking and standalone AI prompt tracking into their existing subscription tiers.
3. **Manual / Spreadsheet & Custom Script Substitutes**: Ad-hoc weekly incognito prompt checks, Google Sheets logging, Looker Studio dashboards, GA4 AI referral tracking, and in-house API scripts.

**Key Finding Regarding the Proposed Wedge**:  
The proposed hypothesis posited that multi-client monitoring, inspectable answer/citation evidence, and branded client reporting might be absent or deficient in existing tools. **Market research decisively contradicts the assumption that multi-client agency workspaces, Looker Studio connectors, or white-labeled client reports are missing from existing tools.** Multiple dedicated trackers (Otterly, Peec AI, Rankscale, Trakkr) and incumbent suites (SE Ranking, Semrush) already provide mature multi-client environments, automated Looker Studio connectors, and white-label client delivery (`geo-market-otterly-pricing`, `geo-market-rankscale-agency`, `geo-market-trakkr-agency`, `geo-market-seranking-agency-pack`). 

However, a genuine structural product gap remains around **reproducibility, stochastic noise modeling, and defensible change review**: almost all existing platforms report discrete, single-point mention counts without explaining LLM sampling variance, non-deterministic drift, or prompt fanout uncertainty (`geo-market-searchengineland-missing`).

---

## 2. Workload & Billing Unit Normalization

To avoid misleading comparisons based on unrelated starting prices (e.g., comparing a solo-freelancer \$20/month plan with an enterprise agency package), this analysis normalizes pricing against a standardized baseline agency workload:

* **Agency Baseline Workload**:
  * **Client Count**: 10 active SMB clients on recurring retainers.
  * **Prompts per Client**: 10–20 core business queries.
  * **Total Tracked Prompts**: 100–200 unique prompts.
  * **Tracking Frequency**: Daily or weekly scheduled monitoring across 3–5 core AI search engines (ChatGPT, Google AI Overviews, Perplexity, Copilot, Gemini).
  * **Reporting Requirement**: White-labeled client reports or dedicated client dashboard links with CSV data export.

### Normalized Pricing & Feature Comparison Table

| Platform | Category | Relevant Plan & Add-Ons | Normalized Monthly Cost (for 10 Clients) | Multi-Client Isolation | Client Logins / White-Label | Data Export & Connectors | Traceable Evidence ID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Otterly.ai** | Pure-Play GEO | **Standard Plan** (€189/mo) with Agency Partner Program | **€189 / mo** (~$205/mo) | Unlimited Workspaces | Looker Studio white-label reports; no native client portal | CSV, Looker Studio, REST API, MCP | `geo-market-otterly-pricing`, `geo-market-otterly-agency-partner` |
| **Peec AI** | Pure-Play GEO | **Agency Scale Plan** (€675/mo) | **€675 / mo** (~$730/mo) | 7 Client Projects (Extra projects custom) | Unlimited client seats, shareable links, pitch workspaces | CSV, Looker Studio connector, REST API, MCP | `geo-market-peec-agency-plans` |
| **Rankscale** | Pure-Play GEO | **Growth Plan** (€385/mo) | **€385 / mo** (~$415/mo) | 50 Brand Dashboard Slots | Full white-labeling on custom domain, unlimited seats | Google Sheets sync, Looker Studio, CSV, REST API | `geo-market-rankscale-agency` |
| **Trakkr.ai** | Pure-Play GEO | **Scale Plan** (\$500/mo) | **$500 / mo** (\$416.67/mo annual) | 10 Client Brands (50 prompts/client = 500 total) | Dedicated client logins, full white-label custom domain | Google Sheets live sync, Looker Studio, CSV, REST API, MCP | `geo-market-trakkr-agency` |
| **Profound** | Pure-Play GEO | **Agency Growth** (\$99/mo base + \$399/client) | **$4,089 / mo** (Unviable for small agencies) | Dedicated Client Workspaces | 5 agency seats, 10 pitch workspaces; client workspaces | CSV, JSON (no API on Growth; API on Enterprise) | `geo-market-profound-agency-pricing` |
| **SE Ranking** | Incumbent SEO Suite | **Growth Plan** (€235/mo) + **Agency Pack** (€59/mo) | **€294 / mo** (~$318/mo) | 60 Projects (30 base + 30 pack) | 30 Client Seats, full white-label domain (`seo.agency.com`) | Native Looker Studio, custom SMTP email reports, CSV, API | `geo-market-seranking-plans`, `geo-market-seranking-agency-pack` |
| **Semrush** | Incumbent SEO Suite | **Pro+ Plan** (\$299/mo) + **Pro Report** (\$20/mo) | **$319 / mo** | 15 Websites (100 daily prompts) | White-label PDF reports, AI summaries, shareable view links | Looker Studio (Advanced only), CSV, PDF | `geo-market-semrush-plans`, `geo-market-semrush-agency-reporting` |
| **Ahrefs** | Incumbent SEO Suite | **Standard** (\$249/mo) + **Brand Radar Basic** (\$50/mo) | **$299 / mo** | 20 Unverified Projects | 1 team seat; Looker Studio blocked (requires \$449/mo Advanced) | CSV, REST API, MCP (Looker Studio requires \$449/mo) | `geo-market-ahrefs-plans`, `geo-market-ahrefs-brand-radar` |
| **Manual / Sheets** | DIY Substitute | Incognito queries + Google Sheets + GA4 | **$0 SaaS** + ~20–40 hrs/mo staff labor | Unlimited sheets | Manual PDFs / Sheets | Google Sheets, manual Looker Studio | `geo-market-searchengineland-missing` |

---

## 3. Direct Competitors: Pure-Play GEO Trackers

### Otterly.AI
* **Positioning**: Accessible, pure-play AI search visibility monitoring for brands and agencies (`geo-market-surmado-comparison`).
* **Pricing & Billing**:
  * Lite: €29/month (15 prompts, 1 workspace).
  * Standard: €189/month (100 prompts, 150 for Agency Partners, unlimited workspaces, Looker Studio connector).
  * Premium: €489/month (400 prompts, 500 for Agency Partners).
  * Optional engine add-ons: Google AI Mode (€59/mo), Gemini (€59/mo), Claude (€109/mo). Extra prompts: €99/mo per 100 (`geo-market-otterly-pricing`).
* **Agency Capabilities**: Dedicated Agency Partner Program offering pitch workspaces (temporary prospect audits), Looker Studio client report connector, and consolidated single billing (`geo-market-otterly-agency-partner`).
* **Fit for GEO-AGENCY-01**: High feature overlap. Delivers multi-client workspaces and Looker Studio exports at €189/mo, though scaling beyond 150 prompts or adding Claude/Gemini increases monthly cost significantly.

### Peec AI
* **Positioning**: Fast-growing European GEO platform with strong focus on multi-model tracking and GDPR-native hosting (`geo-market-surmado-comparison`).
* **Pricing & Billing**:
  * Brand Plans: Starter (€85/mo, 50 prompts, 1 project), Pro (€205/mo, 150 prompts, 2 projects), Advanced (€425/mo, 350 prompts, 5 projects) (`geo-market-peec-brand-pricing`).
  * Agency Plans (Credit Currency: 1 credit = 1 prompt x 1 model x 1 day): Essential (€205/mo, 1 client project, 10k credits), Growth (€425/mo, 3 client projects, 25k credits), Scale (€675/mo, 7 client projects, 65k credits) (`geo-market-peec-agency-plans`).
* **Agency Capabilities**: Unlimited client view seats, shareable dashboards, pre-built Looker Studio templates, pitch projects (3 to 7 active, 7-day duration), REST API and MCP server support.
* **Fit for GEO-AGENCY-01**: Strong product capability, but agency project gating is restrictive: tracking 10 clients exceeds the Scale tier (€675/mo), creating price resistance for small agencies.

### Profound (tryprofound.com)
* **Positioning**: Category-leading enterprise platform with automated content agents and extensive CDN log integrations (`geo-market-surmado-comparison`, `geo-market-dageno-comparison`).
* **Pricing & Billing**:
  * Brand Starter: \$99/mo (ChatGPT only, 50 prompts, 1 seat, **no exports**, no API) (`geo-market-profound-brand-pricing`).
  * Brand Growth: \$399/mo (3 engines, 100 prompts, 3 seats, CSV/JSON exports).
  * Agency Growth: \$99/month base platform fee (5 seats, 10 pitch workspaces) + **\$399/month per dedicated client workspace** (`geo-market-profound-agency-pricing`).
* **Agency Capabilities**: 10 pitch workspaces for prospect audits, Profound Sheets, content execution agents.
* **Fit for GEO-AGENCY-01**: **Poor fit / Economically unviable**. At \$399/month per client workspace, a 10-client agency would pay \$4,089/month. Profound explicitly targets upper mid-market and enterprise brands rather than small independent agencies.

### Rankscale (rankscale.ai)
* **Positioning**: Technical GEO platform tracking 17+ AI models with automated "AI Readiness" page audits (`geo-market-surmado-comparison`).
* **Pricing & Billing**:
  * Pro: €99/month (1,200 credits, up to 4,800 answers, 10 dashboard slots) (`geo-market-rankscale-pricing`).
  * Growth: €385/month (€327/mo annual, 5,500 credits, 50 brand dashboard slots, 200 audits) (`geo-market-rankscale-agency`).
  * Credit weights: 0.25 for standard engines (ChatGPT, Google AIO, Gemini, Perplexity), 1.0 for DeepSeek, 2.0 for Claude.
* **Agency Capabilities**: 50 brand dashboard slots, full white-labeling on custom domains, unlimited team seats, direct Google Sheets sync, Looker Studio connector, and REST API (`geo-market-rankscale-agency`).
* **Fit for GEO-AGENCY-01**: Direct substitute. Provides 50 multi-client slots and complete white-labeling for €385/month.

### Trakkr.ai
* **Positioning**: Turnkey agency-first GEO platform with all 8 major AI models included natively with zero engine surcharges (`geo-market-trakkr-agency`).
* **Pricing & Billing**:
  * Growth: \$100/mo (1 brand, 50 prompts, 3 seats, all 8 engines).
  * Scale (Agency Plan): \$500/month (\$416.67/mo annual) for **10 client brands** (50 prompts per brand = 500 total), unlimited seats (`geo-market-trakkr-agency`).
* **Agency Capabilities**: Full white-labeling on custom agency domain, dedicated client logins, Google Sheets live sync, CSV exports, Looker Studio, REST API, and MCP access.
* **Fit for GEO-AGENCY-01**: Direct killer substitute. Flat \$50/client/month cost basis for a 10-client agency, bundling all 8 engines and white-labeled client portals.

---

## 4. Adjacent Competitors: Incumbent SEO Suites

### SE Ranking
* **Product Architecture**: Traditional SMB SEO suite with integrated AI search prompt tracking and competitive GEO research domains (`geo-market-seranking-plans`).
* **Pricing & Packaging**:
  * Core: €109/month (€87.20/mo annual) includes 10 projects and 100 daily AI prompts.
  * Growth: €235/month (€188/mo annual) includes 30 projects, 3 seats, and 250 daily AI prompts.
  * **Agency Pack Add-On**: +€59/month adds 30 projects, 30 client seats, complete custom-domain white-labeling (`seo.agency.com`), and custom SMTP email reporting (`geo-market-seranking-agency-pack`).
  * Dedicated AI Search Add-On: +€63.20/month for 200 prompts across Google AIO, AI Mode, Perplexity, and ChatGPT.
* **Agency Sufficiency**: Very high. For €247–€294/month total, a small agency gets 60 projects, 30 client portal seats, white-label client reporting, traditional SEO rank tracking, and 250 daily AI search prompts.

### Semrush
* **Product Architecture**: Flagship SEO suite offering "SEO + AI Search" unified tiers (`geo-market-semrush-plans`).
* **Pricing & Packaging**:
  * Starter: \$199/month (5 websites, 50 daily AI prompts).
  * Pro+: \$299/month (15 websites, 100 daily AI prompts).
  * Advanced: \$549/month (40 websites, 200 daily AI prompts).
  * Agency Reporting: **Pro Report add-on** for \$20/month provides full white-label branding, AI summaries, and shareable client links (`geo-market-semrush-agency-reporting`).
* **Agency Sufficiency**: Moderate to high. Small agencies already subscribed to Semrush can monitor 15 client domains and generate white-label client reports for \$319/month without adding a new software vendor.

### Ahrefs
* **Product Architecture**: Traditional SEO suite with Brand Radar AI exploration and prompt tracking (`geo-market-ahrefs-plans`, `geo-market-ahrefs-brand-radar`).
* **Pricing & Packaging**:
  * Standard: \$249/month (20 unverified client projects, 10 daily AI prompts).
  * Brand Radar Add-on: \$50 to \$250/month for +2,500 to +25,000 monthly checks (`geo-market-ahrefs-brand-radar`).
* **Agency Sufficiency**: Low to moderate for GEO. Ahrefs caps native prompt tracking at 10–20 daily queries and restricts Looker Studio connectors to the \$449/month Advanced plan.

---

## 5. Substitutes: Manual Checks, Spreadsheets & In-House Scripts

### The Manual Spreadsheet Baseline
* **Workflow**: Account managers manually type client prompts into incognito browser sessions once a week across ChatGPT, Perplexity, and Gemini, copying citations and brand mentions into Google Sheets or Excel (`geo-market-searchengineland-missing`).
* **Cost**: \$0 in software fees, but consumes an estimated 20–40 hours per month of agency employee labor across a 10-client roster.
* **Structural Limitations**:
  1. *Stochastic Sampling Variance*: LLMs generate responses probabilistically; a single manual query represents a single seed that cannot measure true visibility.
  2. *Personalization & Geo-Bias*: Manual testing is skewed by local IP, browser fingerprint, and session history.
  3. *Unscalable Query Volume*: Tracking 10 clients x 10 prompts x 4 engines = 400 queries per cycle.
  4. *Query Fanout Blindness*: Manual checks see only generated output text, not the background web searches executed by the LLM.

### Custom In-House Scripts & APIs
* **Workflow**: Technical agency staff write Python or Playwright scripts calling OpenAI, Anthropic, or Perplexity APIs, piping JSON outputs into BigQuery/Supabase and Looker Studio.
* **Cost**: \$50–\$200/month in API tokens, but high ongoing developer maintenance due to scraping blocks and LLM interface changes.

---

## 6. Evaluation Against the Proposed GEO-AGENCY-01 Wedge

The hypothesis in `hypothesis.yaml` proposed that small independent SEO agencies need:
1. *Multi-client monitoring*: **Already solved** by Otterly (€189/mo), Rankscale (€385/mo), Trakkr (\$500/mo), and SE Ranking (€294/mo).
2. *Inspectable answer/source evidence*: **Already solved** by all direct trackers, which display cited domains, URLs, and source categories.
3. *Usable client exports & reports*: **Already solved** via native Google Looker Studio connectors, Google Sheets live sync, and white-label custom domain portals.
4. *Noise-aware change review & reproducibility notes*: **UNSOLVED / GENUINE MARKET GAP**. Current trackers present visibility scores as deterministic facts, despite heavy LLM answer volatility, prompt fanout divergence, and sampling instability (`geo-market-searchengineland-missing`).

### Competitive Summary for Stage 1 Review
* **Direct Trackers Available**: Yes (5+ mature pure-play vendors).
* **Affordable Agency Tiers Available**: Yes (Otterly Standard at €189/mo, Rankscale Growth at €385/mo, Trakkr Scale at \$500/mo, SE Ranking Agency Pack at €294/mo).
* **Enterprise-Priced Outliers**: Profound (\$4,000+/mo for 10 clients) is cost-prohibitive for small agencies, but mid-market competitors aggressively serve this exact segment.
* **Differentiating Opportunity**: A monitoring tool competing purely on "we track AI search and generate client reports" will face fierce, established competition. Differentiation must lie strictly in **statistical noise reduction, confidence intervals, reproducible query sampling, and defensible agency decision workflows**.
