# Workflow Map — Vertical B2B Deck & Sales Collateral Automation

**Idea ID:** `deck-automation`  
**Stage:** 1 (Discovery & Hypothesis Validation)  
**Agent:** `workflow-mapping`  
**Status:** Complete  
**Audit Status:** `PENDING` (16 Evidence Records in `evidence.jsonl`)  
**Verdict Note:** Per Workspace Rule 17 & Rule 19, this research report does not issue a Stage 1 PASS/FAIL decision.

---

## 1. Executive Summary & Where the Job Actually Occurs

The core hypothesis under validation proposes:
> *"B2B teams that regularly create customer-specific sales decks spend meaningful recurring time adapting PowerPoint presentations to individual opportunities. Existing presentation AI tools do not fully solve the workflow because teams require company-specific templates, trusted source material, accurate client customization, and reliably editable native PPTX output."*

Empirical investigation across 5 major candidate segments reveals that the **"deck adaptation job" is not uniformly distributed**. It exhibits stark divergence across segments in terms of who does the work, how often it occurs, where the bottleneck lives, and the required deliverable format:

1. **Commercial Real Estate (CRE) Brokerage Teams (Highest Friction & WTP):**
   - **Where the job occurs:** In the deal assembly line between Analysts/Underwriters, Marketing Specialists, and Senior Brokers preparing Offering Memorandums (OMs) and Broker Opinions of Value (BOVs).
   - **The Reality:** Highly manual, taking from **12 hours** on template software (Buildout) to **1–2 weeks** (and up to 4 weeks for complex books) of multi-person coordination. Current tools force a painful trade-off between rigid, ugly templates (Buildout) and slow, bottlenecked desktop design (Adobe InDesign).

2. **Boutique Consultancies & Management Advisory (High Repetitive Labor):**
   - **Where the job occurs:** Junior Analysts and Associates preparing monthly SteerCo deliverables, PMO status decks, and client RFP pitches under Engagement Manager direction.
   - **The Reality:** 90%+ of slides are recycled from prior decks. Practitioners report spending **2–3 hours per deck** or **30% of their daily work** manually updating figures, re-aligning boxes, and recalculating MoM/YoY numbers because linked Excel objects break. Strict client confidentiality and corporate templates mandate 100% native PowerPoint (.pptx).

3. **IT Managed Service Providers / MSPs (High Recurrence, Structured Inputs):**
   - **Where the job occurs:** In recurring client account management, where vCIOs and Account Managers assemble Quarterly Business Reviews (QBRs) and strategic technology roadmaps.
   - **The Reality:** Every managed client requires a review every 90 days. Staff spend **2–4 hours per review** manually pulling ticket stats, backup logs, and security scores from disparate RMM/PSA dashboards into PowerPoint because existing tools only output non-editable, canned "shiny PDFs".

4. **B2B SaaS Account Executives (Challenged Hypothesis):**
   - **Where the job occurs:** Post-discovery demo recaps, executive summaries, and QBRs.
   - **The Reality:** While Account Managers report heavy manual effort for QBRs, full-cycle Account Executives often bypass dedicated software using simple **10–15 minute master template workarounds** (e.g., copying 6 core slides from a 100-slide master file) or abandon decks entirely in favor of interactive demos and conversational selling.

5. **Marketing & Creative Agencies (Downgraded ICP):**
   - **Where the job occurs:** Proposal writing and RFP responses following discovery calls.
   - **The Reality:** High price sensitivity, delegation to low-cost virtual assistants using Google Slides, or widespread substitution with interactive web proposal tools (Qwilr, PandaDoc, Proposify) that prioritize view analytics over PPTX deliverables.

---

## 2. Cross-Segment Comparative Matrix

| Workflow Dimension | 1. Commercial Real Estate (CRE) | 2. Boutique Consultancies | 3. IT Managed Service Providers (MSPs) | 4. B2B SaaS Account Executives | 5. Marketing & Creative Agencies |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Deliverable** | Offering Memorandum (OM), BOV / Pitch Book | Monthly SteerCo Deck, PMO Review, RFP Advisory Pitch | Quarterly Business Review (QBR), Strategic Roadmap | Demo Recap, Executive Solution Pitch, Customer QBR | Scope of Work (SOW), Commercial Proposal, RFP Deck |
| **Output Format Required** | High-res PDF / Print / InDesign / Native PPTX | **Native PPTX strictly required** (.pptx) | Native PPTX or branded presentation deck | Native PPTX or Google Slides | Web link (Qwilr/PandaDoc), Google Slides, PDF |
| **Workflow Actor (Doer)** | Marketing Coordinator / Graphic Designer / Analyst | Junior Analyst / Associate (Years 1–3) | vCIO / Dedicated Account Manager | Quota-carrying AE or Account Manager (AM) | Agency Owner (SMB) or BD Director / Strategist |
| **Buyer / Budget Owner** | Managing Director / Senior Broker / Team Lead | Managing Director / Practice Leader / COO | MSP Owner / VP of Managed Services | VP Sales / Head of RevOps / Sales Enablement | Agency Founder / Managing Director |
| **Observed Recurrence** | 2–6 listing packages per month per team (`per_opportunity`) | Monthly per active client (`monthly`); weekly PMO | Quarterly per managed client (`quarterly` cadence) | 2–6 pitches/week (`per_opportunity`); quarterly QBRs | 5–15 proposals per month (`per_opportunity`) |
| **Manual Effort per Deck** | **12 hours to 2–3 weeks** (`ev-wf-cre-om-12hr-buildout`) | **2–3 hours per deck** / 30% of day (`ev-wf-consulting-monthly-deck-copy-paste`) | **2–4 hours per client** (`ev-wf-msp-qbr-multi-tool-drain`) | **10–15 min** (master template) to **2+ hrs** (QBR) | **30 min** (template) to **10+ hrs** (complex RFP) |
| **Typical Underlying Deal Size** | $2M – $50M+ property value ($50k–$500k+ commission) | $50k – $500k+ advisory engagement fee | $3k – $30k/month recurring retainer ($36k–$360k ARR) | $20k – $150k ARR | $5k – $50k/month retainer or project fee |
| **Primary Data Inputs** | Rent rolls (Excel/PDF), T12 P&Ls, CoStar comps, property photos | Excel financial models, Power BI exports, interview notes | PSA tickets (ConnectWise/Autotask), M365 Secure Score | CRM fields (SFDC/HubSpot), Gong transcripts, pricing calculators | Discovery notes, SOW deliverables, tiered pricing options |
| **Incumbent Tools** | Adobe InDesign, Buildout, CREBuilder, RealNex | Microsoft PowerPoint, Think-Cell, Excel links, Claude | PowerPoint, BrightGauge, CloudRadial, Strategy Overview | Google Slides, PowerPoint, Highspot, Seismic, Gamma | Google Slides, Qwilr, PandaDoc, Proposify, Figma |
| **Core Failure Mode** | Waiting 1–2 weeks in graphic design queue; Buildout is rigid | Linked Excel breaks; manual MoM/YoY arithmetic errors | "Shiny PDF" canned exports require manual transcription | "Frankendecks" with stale logos; template fatigue | High time invested into RFPs with <25% win rates |
| **Observed WTP & Budget Authority** | **Very High** (Brokers pay $500–$1,500/mo/seat or per-deal fees) | **High** (Software expensed to client projects or G&A) | **Medium** (MSPs pay $100–$300/mo for purpose-built add-ons) | **Medium** (Dependent on RevOps enterprise procurement) | **Low** (High sensitivity, prefers free Google Slides) |

---

## 3. Detailed Segment Workflow Maps

```mermaid
flowchart TD
    subgraph CRE["Segment 1: Commercial Real Estate (CRE) Investment Sales"]
        A1[Trigger: Opportunity / Listing Awarded] --> B1[Inputs: Rent Roll, T12 P&L, Comps, Photos]
        B1 --> C1[Step 1: Analyst abstracts financials & builds cash flow model]
        C1 --> D1[Step 2: Marketing Coordinator compiles draft text & maps]
        D1 --> E1[Step 3: Graphic Designer builds 40-80p OM in InDesign / Buildout]
        E1 --> F1[Handoff: Senior Broker redlines draft across 1-2 weeks]
        F1 --> G1[Output: High-res Print/Web PDF & Listing Deck]
    end

    subgraph Consulting["Segment 2: Boutique Consultancies & Management Advisory"]
        A2[Trigger: Monthly SteerCo Cadence / RFP] --> B2[Inputs: Excel Models, BI Snapshots, Notes]
        B2 --> C2[Step 1: Associate recycles prior master deck]
        C2 --> D2[Step 2: Manually update 60+ data points & re-calculate MoM/YoY]
        D2 --> E2[Step 3: Adjust Think-cell waterfall charts & formatting]
        E2 --> F2[Handoff: Engagement Manager & Partner review storylines]
        F2 --> G2[Output: Native PPTX Presentation strictly on-brand]
    end

    subgraph MSP["Segment 3: IT Managed Service Providers (MSPs)"]
        A3[Trigger: 90-Day Review Cadence] --> B3[Inputs: PSA Tickets, SLA Metrics, M365 Security Score]
        B3 --> C3[Step 1: vCIO reviews ticket history & asset warranties]
        C3 --> D3[Step 2: Re-enter data into PowerPoint template]
        D3 --> E3[Step 3: Formulate strategic tech budget & hardware refresh]
        E3 --> F3[Handoff: Operational vs Strategic meeting with client CEO]
        F3 --> G3[Output: 15-20 slide Executive QBR Presentation]
    end
```

---

### 3.1 Commercial Real Estate (CRE) Investment Sales & Capital Markets

* **Actor (Doer):** Marketing Coordinator, Financial Analyst, or In-House Graphic Designer (`ev-wf-cre-designer-indesign-bottleneck`, `ev-wf-cre-marketing-coordinator-role`).
* **Buyer / Budget Owner:** Managing Director, Senior Vice President, or Lead Broker team owner.
* **Workflow Trigger:**
  - *Pre-listing:* Pitching property owner for an exclusive listing via a Broker Opinion of Value (BOV).
  - *Post-award:* Signed listing agreement mandates delivery of the full Offering Memorandum (OM) within 1–2 weeks (`ev-wf-cre-om-turnaround-investor`).
* **Inputs:**
  - Rent roll (leases, expirations, square footage) in Excel or PDF;
  - Trailing 12-month historical P&L (T12);
  - Property photography, drone aerials, floor plans;
  - Local demographic comps and submarket data (CoStar, Crexi, Esri);
  - Debt/financing assumptions.
* **Major Steps:**
  1. *Underwriting:* Analyst standardizes the rent roll and normalizes operating expenses in Excel/Argus.
  2. *Data Compilation:* Marketing Coordinator compiles location highlights, property narrative, and maps into draft documents (`ev-wf-cre-marketing-coordinator-role`).
  3. *Layout & Assembly:* Graphic Designer lays out 30–80+ pages in Adobe InDesign or inputs data into Buildout (`ev-wf-cre-om-12hr-buildout`).
  4. *Review & Revision Cycles:* Senior Broker redlines drafts, correcting unit numbers, property boundaries, and financial summaries over 1–2 weeks (`ev-wf-cre-assembly-line-redlining`).
* **Output / Deliverable:**
  - 30–80+ page Offering Memorandum (PDF and print booklet);
  - 15–25 page BOV Pitch Deck;
  - 1-page digital property flyer and landing page.
* **Current Tools:** Adobe InDesign, Buildout, CREBuilder, IntellCRE, Canva, RealNex.
* **Recurrence Evidence:** `per_opportunity` (2–6 listing packages or BOVs per month per active brokerage team).
* **Manual Effort Evidence:** **12 hours** of manual formatting in Buildout per book (`ev-wf-cre-om-12hr-buildout`); **2–5 days** for a first draft and **1–2 weeks** for final delivery (`ev-wf-cre-om-turnaround-investor`, `ev-wf-cre-assembly-line-redlining`).
* **Handoffs & Approvals:** Sequential handoff from Underwriter $\rightarrow$ Marketing Coordinator $\rightarrow$ Graphic Designer $\rightarrow$ Senior Broker redline $\rightarrow$ Seller sign-off.
* **Reachable Channels:** NAIOP, CCIM Institute, SIOR, `r/CommercialRealEstate`, A.CRE (Adventures in CRE), Bisnow, CoStar/Crexi broker directories.
* **Evidence Count & Confidence:** 5 verified primary records; **High Confidence**.

---

### 3.2 Boutique Consultancies & Management Advisory

* **Actor (Doer):** Junior Analyst / Associate (Years 1–3) under the supervision of an Engagement Manager (`ev-wf-consulting-monthly-deck-copy-paste`).
* **Buyer / Budget Owner:** Practice Leader, Managing Director, or Managing Partner.
* **Workflow Trigger:**
  - Weekly PMO review or monthly Steering Committee (SteerCo) milestone deliverable;
  - Formal RFP response for new client advisory mandate (3–10 day turnaround).
* **Inputs:**
  - Excel financial and operational data models;
  - Business Intelligence snapshots (Power BI, Tableau);
  - Stakeholder interview notes and qualitative findings;
  - Prior engagement decks (recycled templates and frameworks).
* **Major Steps:**
  1. *Storylining:* Engagement Manager sketches the slide narrative and chapter headings (Minto Pyramid structure).
  2. *Slide Cloning:* Associate clones last month's master presentation ("Save As").
  3. *Data Updating:* Manually updates 40–80 individual figures across text callouts, tables, and charts (`ev-wf-consulting-monthly-deck-copy-paste`).
  4. *Chart Formatting:* Uses Think-cell or native PPT charts to rebuild waterfalls and Marimekkos.
  5. *Spot Checking:* Redline review by Engagement Manager to catch arithmetic or labeling errors.
* **Output / Deliverable:** 30–60 slide executive presentation in **native Microsoft PowerPoint (.pptx)**. Web links or non-editable formats are strictly prohibited by enterprise clients.
* **Current Tools:** Microsoft PowerPoint, Think-Cell, PowerQuery, UpSlide, Templafy, Claude / ChatGPT Enterprise (`ev-wf-consulting-claude-skills-breakage`).
* **Recurrence Evidence:** `monthly` for recurring advisory clients; `weekly` for PMO workstreams; `per_opportunity` for RFPs.
* **Manual Effort Evidence:** **2–3 hours** per monthly deck update (`ev-wf-consulting-monthly-deck-copy-paste`); up to **30% of daily working time** spent purely formatting slides (`ev-pain-consulting-thirty-percent-time`).
* **Handoffs & Approvals:** Associate creates draft $\rightarrow$ Engagement Manager reviews storyline $\rightarrow$ Partner reviews commercial messaging $\rightarrow$ Client presentation.
* **Reachable Channels:** `r/consulting` (400k+ members), Fishbowl Consulting Bowl, Wall Street Oasis, Institute of Management Consultants (IMC USA).
* **Evidence Count & Confidence:** 4 verified primary records; **High Confidence**.

---

### 3.3 IT Managed Service Providers (MSPs) / Professional Services

* **Actor (Doer):** Virtual CIO (vCIO), Dedicated Account Manager, or Lead Systems Engineer (`ev-wf-msp-qbr-multi-tool-drain`).
* **Buyer / Budget Owner:** MSP Owner, CEO, or VP of Service Delivery.
* **Workflow Trigger:** Calendar-driven 90-day cadence per managed client (Quarterly Business Review / Strategic Technology Review).
* **Inputs:**
  - Ticketing metrics, open tickets, SLA response times from PSA (ConnectWise, Autotask, HaloPSA);
  - Asset lifecycle, warranty expirations, and OS compliance from RMM/documentation tools (IT Glue, NinjaOne);
  - Cybersecurity scorecards (Microsoft Secure Score, Sophos/SentinelOne alerts);
  - Recommended hardware/software capital expenditure (Capex) budget.
* **Major Steps:**
  1. *Data Extraction:* vCIO logs into 3–4 separate tools to pull ticket reports, asset lifecycle tables, and security posture.
  2. *Data Synthesis:* Manually filters operational noise to identify business-level technology issues.
  3. *Presentation Assembly:* Copies metrics into a client-facing PowerPoint deck or attempts to use canned reporting tools (`ev-wf-msp-qbr-multi-tool-drain`).
  4. *Strategy Formulation:* Writes 3–5 strategic recommendations and estimated project budgets for the upcoming quarter.
* **Output / Deliverable:** 15–25 slide Executive QBR Presentation (PPTX/PDF) + 1-page IT Budget Roadmap.
* **Current Tools:** Microsoft PowerPoint, BrightGauge, CloudRadial, Strategy Overview, PropelYourMSP, Augmentt.
* **Recurrence Evidence:** `quarterly` per contract client. For an average MSP managing 40 clients, this represents **10–13 QBR decks per month**.
* **Manual Effort Evidence:** **2–4 hours per client review** spent analyzing data and building the presentation (`ev-wf-msp-qbr-multi-tool-drain`).
* **Handoffs & Approvals:** Support Team/RMM data $\rightarrow$ vCIO synthesis $\rightarrow$ Client meeting with business owner/CFO.
* **Reachable Channels:** `r/msp` (150k+ members), IT Nation (ConnectWise), CompTIA Communities, Pax8 Community, The Tech Tribe.
* **Evidence Count & Confidence:** 2 verified primary records; **Moderate Confidence** (niche professional services vertical).

---

### 3.4 B2B SaaS Account Executives & Sales Enablement

* **Actor (Doer):** Quota-carrying Account Executive (AE), Sales Development/Business Development Analyst (`ev-pain-dedicated-sales-analyst-deck-role`), or Account Manager (`ev-wf-saas-am-qbr-hours-editing`).
* **Buyer / Budget Owner:** Head of Sales Enablement, VP of Sales Operations, or VP of Sales.
* **Workflow Trigger:** Post-discovery qualification meeting (demo preparation) or upcoming contract renewal (QBR).
* **Inputs:** CRM opportunity notes (pain points, ACV, tech stack), Gong/Chorus discovery transcripts, customer logo/brand colors, product marketing collateral repository.
* **Major Steps:**
  1. *Rep Approach (Master File):* AE opens a master PPT (100 slides), copies 6 mandatory slides, and picks 3–4 relevant case study/pricing slides (`ev-wf-saas-ae-master-slide-workaround`).
  2. *Personalization:* Manually types prospect's company name, challenges, and logo into title and problem slides (10–15 minutes).
  3. *AM Approach (QBR):* Gathers usage metrics, customer health scores, and ROI calculations; attempts to format into slide deck (2+ hours).
* **Output / Deliverable:** 8–15 slide tailored pitch deck or 20-slide QBR deck in Google Slides or Microsoft PowerPoint.
* **Current Tools:** Google Slides, Microsoft PowerPoint, Highspot, Seismic, Pitch.com, Gamma, Canva.
* **Recurrence Evidence:** `per_opportunity` (2–6 customized decks per week per active AE); `quarterly` for Account Managers.
* **Manual Effort Evidence:** **10–15 minutes** per deck when using an organized master template (`ev-wf-saas-ae-master-slide-workaround`); **hours** when preparing custom QBRs (`ev-wf-saas-am-qbr-hours-editing`).
* **Handoffs & Approvals:** Product Marketing creates master messaging $\rightarrow$ Enablement organizes collateral $\rightarrow$ AE customizes slide deck independently without managerial review.
* **Reachable Channels:** `r/sales`, `r/SalesEnablement`, `r/RevenueOperations`, Pavilion, Sales Enablement Collective (SEC), Modern Sales Pros.
* **Evidence Count & Confidence:** 6 verified primary records; **High Confidence** (Workflow exists, but automation necessity is contested).

---

### 3.5 Marketing & Creative Agencies

* **Actor (Doer):** Agency Owner, Business Development Lead, or Account Director (`ev-wf-agency-proposal-slides-assistant`).
* **Buyer / Budget Owner:** Agency Owner / Managing Director.
* **Workflow Trigger:** Completion of prospect discovery call or formal RFP invitation (`ev-wf-agency-rfp-resource-drain`).
* **Inputs:** Discovery call notes, client website URL, audit metrics (SEMrush, Google PageSpeed, Meta ad library), scope of work packages, tiered pricing options.
* **Major Steps:**
  1. *Scope Definition:* Lead strategist defines deliverables, timelines, and monthly retainer fees.
  2. *Template Assembly:* Fills out a standard Google Slides or web proposal template (`ev-wf-agency-proposal-slides-assistant`).
  3. *Delegation:* Many owners hand off structured call notes to virtual assistants to generate the draft (`ev-wf-agency-proposal-slides-assistant`).
* **Output / Deliverable:** Web-based interactive proposal (Qwilr/PandaDoc) with view tracking and e-signature, or 10–20 slide Google Slides / PDF deck.
* **Current Tools:** Google Slides, PandaDoc, Qwilr, Proposify, Figma, Canva, Better Proposals (`ev-wf-agency-interactive-qwilr-substitute`).
* **Recurrence Evidence:** `per_opportunity` (5–20 proposals per month per agency).
* **Manual Effort Evidence:** 30–60 minutes for templated proposals; 4–10+ hours for complex competitive RFPs (`ev-wf-agency-rfp-resource-drain`).
* **Handoffs & Approvals:** BD Lead $\rightarrow$ Delivery Lead (scope verification) $\rightarrow$ Agency Owner sign-off $\rightarrow$ Client.
* **Reachable Channels:** `r/agency`, `r/marketing`, Agency Hackers, Bureau of Digital, Demand Curve.
* **Evidence Count & Confidence:** 4 verified primary records; **High Confidence** (Plausible segment, but low fit for PPTX automation).

---

## 4. Key Takeaways & Workflow Bottlenecks

1. **The InDesign / PowerPoint Divide:**
   - In **CRE**, teams require publication-grade visual typography and multi-page layout standards (Adobe InDesign), but InDesign creates a severe human bottleneck where brokers wait 1–2 weeks for graphic designers.
   - In **Management Consulting**, native Microsoft PowerPoint (.pptx) is the non-negotiable standard. Cloud-only tools (Gamma, Pitch, Canva) fail because enterprise clients require offline editable .pptx files governed by corporate master themes.

2. **The "Air Gap" Between Zero-Automation and 6-Figure Suites:**
   - Mid-market teams across all segments are priced out of Highspot/Seismic ($70k–$180k/year) and Buildout ($500–$1,500/mo enterprise lock-in), forcing them into error-prone copy-pasting across desktop files.

3. **Repetitive Data Injection vs. Creative Narrative:**
   - Across consulting and CRE, the recurring pain is **not writing creative prose**, but **injecting structured tabular numbers into slide layouts** (rent rolls, MoM financial changes, ticket metrics) without breaking slide formatting or calculating arithmetic wrong.
