# Stage 1 Validation Report — Vertical B2B Deck / Sales-Collateral Automation

**Idea ID:** `deck-automation`  
**Evaluation Date:** 2026-09-07  
**Audited Corpus:** 88 total records | **66 VERIFIED** (100% unique `independence_key`s) | 9 PARTIALLY_VERIFIED | 13 REJECTED  
**Governing Methodologies:** `methodology/stage1-gates.md`, `methodology/scoring.md`, `validation-rules.md`

---

## 1. Hypothesis

### Stated Initial Hypothesis
> B2B teams that regularly create customer-specific sales decks spend meaningful recurring time adapting PowerPoint presentations to individual opportunities. Existing presentation AI tools do not fully solve the workflow because teams require company-specific templates, trusted source material, accurate client customization, and reliably editable native PPTX output. A sufficiently painful segment can justify a B2B SaaS price materially above low-cost consumer presentation subscriptions.

### Business & MVP Constraints
- **Target ARPU:** Eventual monthly minimum \$100 USD.
- **Founder Model:** Solo technical founder with coding/research agents.
- **MVP Architectural Scope:** Buildable without developing a full-featured visual presentation canvas editor; native editable PPTX output strongly preferred.
- **Initial Exclusions:** Fortune 500 enterprise procurement-heavy accounts; heavily regulated compliance-intensive workflows.

---

## 2. Executive Verdict

### Final Decision: `CONDITIONAL PASS`

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                                STAGE 1 VERDICT                                   │
│                              CONDITIONAL PASS                                    │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### Strategic Rationale & Explicit Condition
The empirical evidence decisively validates the core pain, recurrence, existing commercial spend, and technical failures of horizontal AI presentation tools. Verified independent pain signals (35 records, 29 from target ICPs) far exceed the G1 threshold. Recurrence is verified across daily, weekly, and per-opportunity cadences (G2). Commercial willingness to pay is demonstrated through active six-figure agency subscriptions (\$180,000/yr Superside), dedicated full-time headcount (\$89,147 in-house presentation designers), and substantial hourly contractor spend (\$45–\$150/hr), across 8 distinct categories (G3). Furthermore, horizontal AI tools (Gamma, Beautiful.ai, Pitch, Microsoft Copilot) exhibit severe, repeatable failures in PPTX export fidelity and corporate master template compliance (G4). Reachability is validated via the APMP directory of 11,000+ corporate proposal managers and active LinkedIn role surfaces (G5).

**However, the initial hypothesis fails Gate 6 under its broad "B2B SaaS Account Executive sales deck" formulation:**
1. **Enterprise Enablement Domination:** Incumbent revenue enablement platforms (**Highspot AutoDocs** [`ev-mkt-highspot-autodocs`], **Seismic LiveDocs** [`ev-mkt-seismic-livedocs`], and **Showpad ACB** [`ev-skp-showpad-acb`]) already provide native, marketing-governed, CRM-to-PPTX dynamic deck assembly for enterprise sales organizations.
2. **Practitioner Workaround Efficiency:** Full-cycle sales practitioners report that disciplined master templates compress individual opportunity customization down to **10–15 minutes** [`ev-pain-master-template-workaround`], capping willingness to pay.
3. **Format Displacement:** Account executives and modern consultative sellers are increasingly moving toward conversational discovery or interactive web collateral (**Storydoc**, **Qwilr**) rather than static pitch decks [`ev-pain-rep-disdain-for-decks`, `ev-skp-storydoc-web-collateral`].

### Mandatory Condition to Proceed to Stage 2:
> **The target ICP must be explicitly redefined away from general B2B SaaS Account Executives to high-volume, mandatory-PPTX collateral segments:**
> 1. **Boutique Strategy & Management Consultancies (5–50 FTEs):** Where presentations are the paid client deliverable, consultants lose ~30% of their workday formatting PowerPoint [`ev-pain-consulting-thirty-percent-time`], corporate clients strictly prohibit web links, and firms routinely pay \$899–\$15,000/month to outsourced design agencies [`ev-wtp-24slides-pricing-models`, `ev-wtp-superside-minimum-annual`].
> 2. **Commercial Real Estate (CRE) Brokerage Teams / Proposal Managers (APMP):** Where multi-page Offering Memorandums (OMs) require combining financial rent rolls into strict layouts, currently creating multi-day bottlenecks for dedicated in-house designers [`ev-wf-cre-designer-indesign-bottleneck`].
>
> **Technical Feasibility Condition:** Stage 2 customer discovery must verify whether a lightweight server-side template-population tool (constrained by python-pptx / OpenXML lack of live font metrics [`ev-skp-openxml-pptx-layout-engine`]) can achieve acceptable visual fidelity without requiring a full visual presentation editor.

---

## 3. What Users Appear to Be Doing

Across the 66 VERIFIED records, practitioners in collateral-heavy workflows operate in an inefficient, fragmented assembly line:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               CURRENT PRACTITIONER WORKFLOW                            │
├───────────────────┬────────────────────────────┬───────────────────────────────────────┤
│ 1. Data Ingestion │ 2. Narrative / Assembly    │ 3. Formatting & Brand Cleanup         │
│ • CRM Opportunity │ • Copy-pasting CRM data    │ • Manual shape alignment & recoloring │
│ • Rent rolls (CRE)│ • Merging old deck slides  │ • Fixing corrupted master templates   │
│ • Excel models    │ • Drafting bullets in Word │ • Outsourcing overflow to agencies/VAs│
│ • Case studies    │ • Generating raw text (LLM)│ • Re-building broken AI exports       │
└───────────────────┴────────────────────────────┴───────────────────────────────────────┘
```

1. **Manual Copy-Paste from Core Systems:** RevOps leads and sales analysts manually copy opportunity fields (AE name, pain points, dates, metrics) from Salesforce/HubSpot into presentation slides [`ev-pain-revops-sfdc-to-slides-manual-drain`, `ev-pain-dedicated-sales-analyst-deck-role`]. In CRE, capital markets analysts spend 2–3 days gathering rent rolls, underwriting models, and tenant rosters to feed into Offering Memorandums [`ev-wf-cre-assembly-line-redlining`].
2. **Frankenstein Slide Assembly:** Practitioners assemble client decks by stitching together slides from prior client engagements or master slide decks. This frequently corrupts master slide layouts, distorts typography, and creates conflicting color palettes [`ev-pain-pptx-master-slide-corruption`, `ev-pain-consulting-client-theme-rework`].
3. **Manual Formatting Tax:** Management consultants spend up to **30% of their billable workday** manually adjusting slide margins, aligning callout boxes, and recoloring charts to match client brand guidelines [`ev-pain-consulting-thirty-percent-time`].
4. **Delegation and Outsourcing:** To escape formatting labor, firms hire full-time dedicated graphic designers (`$89,147` median salary) [`ev-wtp-ziprecruiter-powerpoint-designer-salary`, `ev-wf-cre-designer-indesign-bottleneck`], retain overseas design agencies at \$899/month (24Slides) to \$15,000/month (Superside) [`ev-wtp-24slides-pricing-models`, `ev-wtp-superside-minimum-annual`], or employ virtual assistants [`ev-wf-agency-proposal-slides-assistant`].
5. **Abandonment of Generic AI Tools:** Practitioners who experiment with modern AI slide generators (Gamma, Beautiful.ai, Pitch, Copilot) universally abandon them for client-facing work due to destroyed layouts upon PPTX export and an inability to enforce corporate brand master files [`ev-pain-gamma-export-corrupted-content`, `ev-gap-beautifulai-export-templates-jeff`].

---

## 4. Pain Clusters

The 35 VERIFIED independent pain signals cluster into four primary pain mechanics:

### Cluster 1: The Formatting & Layout Time Drain (30% Labor Tax)
* **Pervasiveness:** Observed across consulting, CRE, agencies, and MSPs.
* **Evidence:** Management consultants report that approximately 30% of their workday is consumed solely by formatting PowerPoint presentations, adjusting shapes, and aligning boxes [`ev-pain-consulting-thirty-percent-time`]. In CRE, assembling an Offering Memorandum involves 2–3 days of data collation, 12–24 hours of drafting, and multiple rounds of redlining between brokers and marketing coordinators [`ev-wf-cre-assembly-line-redlining`, `ev-wf-cre-marketing-coordinator-role`].
* **Impact:** High-cost billable employees (analysts, consultants, vCIOs) spend valuable hours functioning as amateur graphic layout technicians [`ev-wf-msp-qbr-multi-tool-drain`].

### Cluster 2: Corporate Master Template Corruption & Brand Rework
* **Pervasiveness:** Acute in client-facing consulting and multi-stakeholder corporate sales.
* **Evidence:** Consultants describe spending entire evenings manually combing through 30-page presentations to recolor charts, tables, and icons to adhere to client corporate identity requirements [`ev-pain-consulting-client-theme-rework`]. Merging slides across teams frequently corrupts PowerPoint master layouts, generating duplicate slide masters and scrambled formatting [`ev-pain-pptx-master-slide-corruption`].
* **Impact:** Risk of client embarrassment or brand compliance violations, requiring tedious manual remediation.

### Cluster 3: Data-to-Deck Disconnection & Copy-Paste Bottlenecks
* **Pervasiveness:** Severe in RevOps, MSP QBR prep, and agency RFP responses.
* **Evidence:** RevOps leads report that manually copying CRM opportunity fields into slides for customer handoffs takes up huge amounts of administrative time [`ev-pain-revops-sfdc-to-slides-manual-drain`]. MSPs note that QBR preparation requires vCIOs and engineers to manually compile ticket histories and security metrics because existing tools only produce rigid "shiny PDFs" [`ev-wf-msp-qbr-multi-tool-drain`].
* **Impact:** Administrative drag that slows deal velocity and post-sale onboarding.

### Cluster 4: The "Generate-then-Rebuild" AI Tooling Trap
* **Pervasiveness:** Broad among practitioners attempting to use horizontal AI deck tools.
* **Evidence:** Rather than saving time, using tools like Gamma or Beautiful.ai results in doing **three times more work** than starting in native PowerPoint, because exported files must be completely deconstructed and rebuilt to fix layout distortion and font errors [`ev-gap-beautifulai-export-templates-jeff`, `ev-pain-gamma-export-corrupted-content`].
* **Impact:** Severe disillusionment with generative presentation software across professional service firms.

---

## 5. Recurrence

### Confidence: `HIGH`
The core presentation creation job is deeply embedded and highly recurrent across professional B2B workflows.

| Recurrence Frequency | Verified Records | Example Workflows & Practitioner Roles |
| :--- | :---: | :--- |
| **`per_opportunity`** | **28** | New client sales pitches, CRE Offering Memorandums, agency RFP responses, client handoffs. |
| **`monthly`** | **17** | Monthly client steering committee updates, consulting retainer reports, agency performance reviews. |
| **`daily`** | **6** | Daily deck formatting and slide mechanics by junior strategy and management consultants. |
| **`weekly`** | **5** | Weekly project status decks, PMO governance presentations, enablement collateral assembly. |
| **`quarterly`** | **2** | Account Executive quarterly business reviews (QBRs), MSP vCIO executive reviews. |
| **`per_client` / Other** | **8** | Custom client onboarding roadmaps, ad-hoc investor presentations. |
| **Total** | **66** | **100% of verified corpus exhibits explicit workflow cadence** |

Practitioners in consulting and CRE build presentations on a daily to per-deal basis, satisfying the recurrence requirement for a durable B2B SaaS subscription.

---

## 6. Existing Spend / WTP

### Confidence: `HIGH`
The research establishes massive commercial willingness to pay across **37 VERIFIED records** spanning **8 distinct categories**. The market already expends substantial budgets to solve presentation production:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              VERIFIED COMMERCIAL BUDGETS                               │
├───────────────────────────────┬──────────────────────┬─────────────────────────────────┤
│ Spend Category                │ Documented Spend     │ Verified Example Records        │
├───────────────────────────────┼──────────────────────┼─────────────────────────────────┤
│ Dedicated In-House Roles      │ $89,147 / year       │ ev-wtp-ziprecruiter-salary      │
│ Agency Retainers              │ $899 – $15,000 / mo  │ ev-wtp-superside, 24slides      │
│ Freelance / Contractor Rates  │ $45 – $150 / hour    │ ev-wtp-upwork, reddit-cleanup   │
│ Enterprise Enablement SaaS    │ $70,000 – $180,000/yr│ ev-mkt-highspot-contract-floor  │
│ Incumbent Add-in Software     │ $28.60 / user / mo   │ ev-skp-thinkcell-consulting     │
│ Horizontal Deck Subscriptions │ $10 – $45 / user / mo│ ev-mkt-gamma, beautifulai       │
└───────────────────────────────┴──────────────────────┴─────────────────────────────────┘
```

### Detailed Spend Categories:
1. **Full-Time Headcount (Dedicated Roles — 6 records):**
   * Average salary for a corporate PowerPoint presentation designer in the US is **\$89,147/year** [`ev-wtp-ziprecruiter-powerpoint-designer-salary`].
   * CRE brokerages employ dedicated full-time in-house graphic designers whose sole job is building Offering Memorandums in InDesign [`ev-wf-cre-designer-indesign-bottleneck`].
   * Mid-market firms employ dedicated Marketing Specialists and Sales Enablement Managers whose job specs mandate formatting and translating collateral for senior reps [`ev-wf-cre-marketing-coordinator-role`, `ev-wf-enablement-governance-translation`].
2. **Agency Retainers (3 records):**
   * **Superside:** Creative subscription services (including pitch decks) enforce a strict minimum contract of **\$15,000/month (\$180,000/year)** [`ev-wtp-superside-minimum-annual`].
   * **24Slides:** Dedicated presentation design teams cost **\$899/month** (or \$11/slide pay-as-you-go) [`ev-wtp-24slides-pricing-models`].
   * **PitchWorx:** Monthly presentation design retainers start at **\$699/month** [`ev-wtp-pitchworx-deck-cost-guide`].
3. **Contractor & Freelance Spend (4 records):**
   * Upwork verified median hourly rate for Presentation Designers is **\$45/hour** [`ev-wtp-upwork-presentation-designer-hourly`].
   * Freelance presentation designers quote **\$75 to \$150/hour** for corporate PowerPoint cleanup projects (\$1,125 average fixed-scope project) [`ev-wtp-reddit-powerpoint-cleanup-hourly-rates`].
   * Sales teams hire contract presentation designers for 10–20 hours per month on recurring retainers [`ev-pain-outsourced-deck-freelancer`].
4. **Incumbent & Adjacent Software Spend (14 records):**
   * **think-cell:** Consultancies and investment banks universally pay **\$28.60/user/month** billed annually (\$325/year) for slide charting mechanics [`ev-skp-thinkcell-consulting`, `ev-mkt-thinkcell-spend`].
   * **Templafy:** Enterprise template governance and dynamic slide assembly starts at **\$40/user/month** [`ev-mkt-templafy-capabilities`].
   * **Highspot:** Annual enterprise enablement contracts enforce platform minimums of **\$70,000 to \$180,000/year** [`ev-mkt-highspot-contract-floor`].
5. **Employee Billable Time Drains (8 records):**
   * High-earning management consultants losing 30% of their workday to slide formatting represent tens of thousands of dollars in annual lost billable realization per employee [`ev-pain-consulting-thirty-percent-time`].

*Note on Low WTP Segments:* Early-stage startup founders on r/startups explicitly reject paying for presentation software or designers, relying instead on \$30 one-time templates [`ev-wtp-reddit-startups-low-wtp-diy`]. This confirms startups must be excluded from target ICP definitions.

---

## 7. Current Alternatives

The landscape of current alternatives reveals strong polarization between inaccessible high-end suites and dysfunctional low-end tools:

| Solution Category | Key Vendors | Typical Pricing | Core Strengths | Critical Failure / Disqualifying Limitation |
| :--- | :--- | :--- | :--- | :--- |
| **Enterprise Enablement Suites** | Highspot AutoDocs, Seismic LiveDocs, Showpad ACB | \$70,000 – \$180,000+ annual minimums | Native PPTX plugins; dynamic CRM placeholder merging; enterprise governance. | Completely inaccessible to SMB/mid-market; multi-month implementation; 6-figure price floor. |
| **Specialized Incumbent Plugins** | think-cell | \$28.60 / user / mo (billed annually) | Entrenched in top-tier strategy consultancies; automated charting; rock-solid PPTX stability. | Solves only charts and waterfall graphs; does not automate opportunity narrative, text generation, or layout assembly. |
| **Web Proposal / Collateral SaaS** | Storydoc, Qwilr | \$19 – \$35 / user / mo | Interactive web links; embedded analytics; CRM field integration. | **Blocks native editable PPTX export** (Storydoc only exports static PDF; Qwilr is web-only). Rejected by corporate clients and procurement. |
| **Horizontal Generative AI Decks** | Gamma, Beautiful.ai, Pitch | \$10 – \$40 / user / mo | Fast card/web creation; sleek consumer UI; AI copy generation. | **Destroys PPTX export fidelity** (character corruption, broken tables); completely ignores corporate master templates; locks users into proprietary smart templates. |
| **Incumbent Desktop AI** | Microsoft 365 Copilot in PowerPoint | \$30 / user / mo (annual commitment) | Native inside PowerPoint; enterprise security boundaries. | Limited to referencing a single file at a time; desktop app fails to recognize SharePoint corporate templates; generates superficial kindergarten-level output. |
| **Human Design Services** | Superside, 24Slides, Upwork freelancers | \$899 – \$15,000 / mo; \$45 – \$150 / hr | High visual polish; custom template fidelity; zero software bugs. | Turnaround latency (24–72 hours); expensive recurring operational budget; does not scale with deal volume. |

---

## 8. Repeatable Gaps

Across 18 VERIFIED gap records, evidence converges on three structural, repeatable technical gaps:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             REPEATABLE TECHNICAL GAPS                                  │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ 1. Export Fidelity Breakdown              │ 2. Corporate Template Non-Compliance       │
│ • Gamma: character glitches, missing text │ • Gamma: completely disregards master PPTX │
│ • Beautiful.ai: export locks custom edits │ • Beautiful.ai: rigid proprietary layouts  │
│ • Storydoc: strictly prohibits PPTX export│ • Copilot: desktop bug blocks SharePoint   │
│ • Canva: converts tables to static shapes │   corporate templates                      │
├───────────────────────────────────────────┴────────────────────────────────────────────┤
│ 3. Multi-Input Context Blindness                                                       │
│ • Microsoft Copilot limited to 1 file (<24MB); cannot combine CRM data + case studies  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

1. **PPTX Export Fidelity Corruption:**
   * Gamma exports to PowerPoint drop sections, replace characters with unreadable symbols, and scramble visual layouts [`ev-pain-gamma-export-corrupted-content`].
   * Canva converts editable tables and groupings into misaligned static shapes when exported to PPTX [`ev-mkt-canva-pptx-breakage`].
   * Storydoc permanently blocks editable PPTX export, causing paying business customers to churn in frustration [`ev-mkt-storydoc-format-barrier`, `ev-gap-storydoc-no-pptx-export-nasrullah`].
   * Beautiful.ai prevents exporting custom slides outside its rigid smart templates, forcing users to do 3x more manual work in PowerPoint [`ev-gap-beautifulai-export-templates-jeff`].
2. **Corporate Master Template Non-Compliance:**
   * Horizontal AI presentation generators completely disregard uploaded PowerPoint master templates, outputting cluttered slides that violate corporate brand standards [`ev-pain-gamma-ignores-corporate-templates`].
   * Microsoft Copilot in the desktop PowerPoint application frequently fails to access corporate templates stored in SharePoint, generating generic default templates instead [`ev-gap-copilot-desktop-custom-template-failure`].
3. **Multi-Input Context Ingestion Limits:**
   * Microsoft's official documentation confirms that PowerPoint Copilot can reference only a single file at a time (under 24MB), and cannot accept additional prompt context in the same instruction [`ev-mkt-copilot-single-file-limitation`]. It cannot synthesize opportunity notes, call transcripts, and case studies into a coherent tailored deck.

---

## 9. Candidate ICPs

Based on verified workflow structures, existing spend, and substitute risk, candidate segments rank as follows:

### 1. Boutique Strategy & Management Consultancies (5–50 FTEs) — `TIER 1 (RECOMMENDED)`
* **Profile:** Strategy, operations, and IT boutique consulting practices.
* **Workflow:** Every client engagement requires bespoke steering committee decks, deliverables, and recap presentations.
* **Pain & Spend:** Consultants spend 30% of their workday formatting PowerPoint [`ev-pain-consulting-thirty-percent-time`]; pay \$28.60/user/mo for think-cell [`ev-skp-thinkcell-consulting`]; pay \$899–\$15,000/mo to 24Slides/Superside [`ev-wtp-24slides-pricing-models`, `ev-wtp-superside-minimum-annual`].
* **Substitute Barrier:** Enterprise suites (Seismic/Highspot) are irrelevant; web links (Storydoc) are strictly banned by corporate clients; native editable PPTX is the mandatory currency of business.

### 2. Commercial Real Estate (CRE) Brokerage Teams & Analysts — `TIER 1 (RECOMMENDED)`
* **Profile:** Commercial brokerage teams, capital markets analysts, investment sales brokers.
* **Workflow:** Regularly produce 30–50 page Offering Memorandums (OMs) combining rent rolls, property financials, and neighborhood demographics.
* **Pain & Spend:** Coordinators spend 12–24 hours compiling data; firms hire dedicated graphic designers (\$89k salary) solely for InDesign OMs [`ev-wf-cre-designer-indesign-bottleneck`, `ev-wf-cre-marketing-coordinator-role`].
* **Substitute Barrier:** Highspot/Seismic do not operate in CRE; Buildout requires extensive manual data cleanup [`ev-wf-cre-assembly-line-redlining`].

### 3. Mid-Market RFP & Proposal Teams (APMP Members) — `TIER 2`
* **Profile:** Dedicated bid, proposal, and tender managers responding to commercial and public RFPs.
* **Workflow:** Assembling multi-stakeholder capability decks and pitch collateral under tight deadlines.
* **Pain & Spend:** 20–40 hours per RFP proposal deck [`ev-wf-agency-rfp-resource-drain`]; highly reachable via APMP (11,000+ members) [`ev-wf-reachability-apmp-association`].
* **Risk:** RFPs frequently center on complex Word/Excel documents rather than pure presentations.

### 4. B2B SaaS Account Executives — `DISQUALIFIED AS INITIAL WEDGE`
* **Profile:** Mid-market and enterprise B2B SaaS quota-carrying reps.
* **Falsification:** Enterprise enablement suites (Highspot, Seismic, Showpad) already dominate; disciplined master templates take only 10–15 minutes [`ev-pain-master-template-workaround`]; top reps question the utility of decks entirely in favor of conversational selling [`ev-pain-rep-disdain-for-decks`, `ev-pain-faang-no-deck-workflow`].

---

## 10. Candidate Wedges

To operate within solo-founder constraints and avoid building a full presentation canvas editor, two viable product wedges emerge:

### Wedge A: Consulting Client Theme & Data Injector (Desktop Add-In or CLI)
* **Value Proposition:** Automatically transforms analysis (Excel models, interview transcripts, bullet notes) into client-branded PowerPoint slides matching the consultancy's exact master layout, without corrupting fonts or shape coordinates.
* **MVP Scope:** A native PowerPoint VSTO/Web add-in or Python-based CLI that maps structured tables and bullet hierarchies into predefined shape placeholders in an existing `.pptx` master. Avoids arbitrary layout generation.
* **Pricing Anchor:** \$99 – \$199 / user / month (anchored against think-cell at \$29/mo and 24Slides at \$899/mo).

### Wedge B: CRE Offering Memorandum (OM) Automated Builder
* **Value Proposition:** Ingests property financial spreadsheets (rent rolls, unit mixes, debt assumptions) and generates a standardized, ready-to-refine 30-page PowerPoint Offering Memorandum.
* **MVP Scope:** Server-side templating engine that populates a firm's master OM PowerPoint deck with dynamic financial tables, lease comp summaries, and property stat callouts.
* **Pricing Anchor:** \$250 – \$500 / brokerage team / month (anchored against dedicated graphic designer salary of \$89k/year).

---

## 11. Strongest Disconfirming Evidence

The audit uncovered significant disconfirming evidence that directly challenges the original hypothesis:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             STRONGEST DISCONFIRMING SIGNALS                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. ev-mkt-highspot-autodocs / ev-mkt-seismic-livedocs: Enterprise enablement platforms │
│    already solve dynamic template deck assembly from CRM data.                         │
│ 2. ev-pain-master-template-workaround: Disciplined master PowerPoint templates compress│
│    sales customization to 10-15 minutes, capping willingness to pay for AEs.           │
│ 3. ev-pain-rep-disdain-for-decks / ev-pain-faang-no-deck-workflow: Reps report decks do │
│    not close deals, and FAANG reps operate without decks for years.                    │
│ 4. ev-skp-openxml-pptx-layout-engine: python-pptx lacks font metrics and live layout   │
│    calculation; dynamic text overflow causes layout clipping without complex engines.  │
│ 5. ev-skp-thinkcell-consulting: Entrenched $28.60/user/mo pricing anchor in consulting.│
│ 6. ev-mkt-tome-market-failure: Horizontal AI deck tool raised $81M, stalled at $3M ARR │
│    across 20M users, and shut down presentation tool in April 2025.                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

1. **Enterprise Incumbents Solve CRM-to-PPTX:** Highspot AutoDocs [`ev-mkt-highspot-autodocs`], Seismic LiveDocs [`ev-mkt-seismic-livedocs`], and Showpad ACB [`ev-skp-showpad-acb`] prove that CRM-driven presentation automation is an established enterprise feature, not an unserved white space.
2. **The 10–15 Minute Master Template Workaround:** Sales leaders report that providing reps with a well-structured 10-slide master PowerPoint with explicit placeholder prompts reduces deal customization to only 10–15 minutes [`ev-pain-master-template-workaround`].
3. **Conversational Sales Pushback:** Senior B2B reps actively argue that slide decks disengage buyers and fail to close deals, with enterprise FAANG reps reporting going years without presenting a deck [`ev-pain-rep-disdain-for-decks`, `ev-pain-faang-no-deck-workflow`].
4. **The OpenXML Server-Side Layout Trap:** Official documentation for `python-pptx` confirms that server-side OpenXML generation lacks font metrics and live layout rendering [`ev-skp-openxml-pptx-layout-engine`]. If dynamic text overflows a fixed text frame, PowerPoint only resolves line wraps upon file opening, resulting in text clipping. Solving this cleanly without a rendering engine is a serious technical risk for a solo founder.
5. **Entrenched Pricing Anchor (think-cell):** Consulting firms pay \$28.60/user/month for think-cell [`ev-skp-thinkcell-consulting`], establishing a psychological price ceiling for internal PowerPoint utilities unless tied directly to billable hour savings.
6. **Horizontal Presentation Market Failure (Tome):** Tome raised \$81M, reached 20M+ users, but shut down its presentation tool on April 30, 2025 after ARR plateaued at ~$3M [`ev-mkt-tome-market-failure`]. Consumer/prosumer deck generation lacks sustainable enterprise monetization.

---

## 12. Unknowns

In strict compliance with Workspace Rule 2, the following missing items remain **`UNKNOWN`** and cannot be assumed:

1. **Server-Side Rendering Feasibility:** `UNKNOWN` whether a solo founder can achieve acceptable text autofit and shape wrapping across diverse corporate templates using OpenXML without building a headless Chromium / PowerPoint rendering pipeline.
2. **Boutique Consulting Discretionary Card Spend:** `UNKNOWN` whether engagement managers in 10–50 person boutique consultancies possess individual credit card authority (\$100–\$300/mo) or whether all software requires managing partner consensus.
3. **Template Variance vs. Standardization:** `UNKNOWN` what percentage of slides in boutique consultancy client deliverables follow standard structured layouts versus bespoke ad-hoc visualizations.
4. **Displacement of Human Design Retainers:** `UNKNOWN` whether firms spending \$899–\$15,000/month on human design agencies (24Slides/Superside) will trust an automated tool to produce final, client-facing decks without human review.

---

## 13. Stage 2 Questions

During Stage 2 prospect discovery and customer validation interviews, researchers must ask:

1. **Time Breakdown:** *"When your team adapts a presentation for a client engagement or pitch, exactly how many hours are spent drafting content and narrative versus mechanical slide formatting, shape alignment, and recoloring?"*
2. **Current Toolchain & Breakage:** *"Walk me through the exact software chain you use to build client decks today (PowerPoint, think-cell, InDesign, Google Slides). What breaks when you try to export, merge templates, or share editable files with clients?"*
3. **Generative AI Evaluation:** *"Have you tried tools like Gamma, Beautiful.ai, Pitch, or Copilot? Exactly why did they fail to make it into your live client workflow?"*
4. **Layout Tolerance & Automation Boundary:** *"If a software tool could automatically populate your firm's PowerPoint template from your Excel models or notes, but required you to do minor final text polish in native PowerPoint, would that save enough time to be worth \$150–\$300/seat/month?"*
5. **Budget Authority:** *"Who in your organization has the budget authority to approve a \$2,000–\$5,000 annual software expense for slide automation? Is it an individual project expense, a practice lead decision, or firm-wide IT?"*

---

## 14. Gate Scorecard

All metrics reflect strictly **VERIFIED** evidence deduplicated by `independence_key`.

| Gate | Name | Required Threshold | Verified Metric | Result | Confidence |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **G1** | **Concrete Pain** | ≥20 VERIFIED independent signals (≥10 from plausible ICPs) | **35 independent records** (29 from target ICPs: Consulting, CRE, RevOps, Agencies, MSPs) | **PASS** | `HIGH` |
| **G2** | **Recurrence** | At least MEDIUM confidence of SaaS recurrence | **66 verified records** with explicit recurrence (28 per-opportunity, 17 monthly, 6 daily, 5 weekly) | **PASS** | `HIGH` |
| **G3** | **Existing Spend / WTP** | ≥5 VERIFIED money signals from ≥2 distinct spend categories | **37 verified records across 8 distinct categories** (Agency, Dedicated Role, Contractor, SaaS, Competitor Price, Employee Time, Actual Purchase, Stated WTP) | **PASS** | `HIGH` |
| **G4** | **Repeatable Gap** | ≥10 VERIFIED records clustered around repeatable gaps | **18 verified records** clustered in (1) PPTX export fidelity destruction, (2) corporate template non-compliance, (3) multi-input context limits | **PASS** | `HIGH` |
| **G5** | **ICP Reachability** | Plausible roles, company segments, reachable channels (≥MEDIUM confidence) | **42 verified practitioner roles**; direct channel via **APMP (11,000+ members)** and LinkedIn role clusters | **PASS** | `MEDIUM` |
| **G6** | **No Killer Substitute** | No low-friction substitute solving workflow at value-destroying price | **FAILED for B2B SaaS AEs** (Highspot, Seismic, 10-min template workarounds, Storydoc). **CONDITIONAL PASS for Boutique Consultancies and CRE OMs** where 6-figure enterprise suites are absent and native PPTX is mandatory. | **CONDITIONAL PASS** | `MEDIUM` |

### Dimension Scores (0–5 Integer Scale)

```json
{
  "pain_strength": 5,
  "recurrence_confidence": 5,
  "revealed_wtp": 5,
  "current_solution_gap": 5,
  "icp_clarity": 4,
  "reachability": 4,
  "substitute_risk": 2,
  "evidence_quality": 5,
  "source_diversity": 4,
  "overall_confidence": 4
}
```

---

### Final Operational Instruction for Stage 2
Proceed to Stage 2 Prospect Mining and Customer Interviews **ONLY** after updating `hypothesis.yaml` to narrow the target ICP from general B2B sales teams to **Boutique Strategy Consultancies** and/or **Commercial Real Estate Brokerage Teams**. Focus initial outreach interviews on validating the OpenXML layout automation boundary and identifying the exact economic buyer.
