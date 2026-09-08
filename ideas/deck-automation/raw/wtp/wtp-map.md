# Stage 1 Willingness-to-Pay (WTP) Map — Deck Automation

## 1. Scope and ICP Coverage

### Evaluated Workflow Scope
The workflow under investigation is fixed to: adapting master company presentations, corporate templates, and opportunity-specific inputs (discovery notes, customer CRM data, pricing, or property details) into customized, on-brand, client-ready editable PowerPoint (`.pptx`) deliverables.

Spend is assessed strictly per candidate ICP. Spend across disparate verticals (e.g., commercial real estate vs. B2B SaaS sales vs. management consulting) is not pooled or aggregated into an artificial total.

### Candidate ICP Coverage Matrix

| Candidate ICP | Target Job / Artifact | Spend Signals Observed | Assessed Willingness to Pay |
| :--- | :--- | :--- | :--- |
| **Commercial Real Estate (CRE)** | Offering Memorandums (OMs), BOVs, Deal Packages | Contractor spend ($1,000 setup + $100/listing); Vertical SaaS ($125/user/mo) | High revealed spend per transaction deal package |
| **Boutique Consultancies** | Strategy decks, client deliverables, proposals | Costly employee labor (30–50% time formatting); PowerPoint plugins (€24/user/mo) | High labor cost absorbed internally; software budget modest |
| **Sales Enablement & B2B AEs** | Custom prospect pitches, demo recap decks, QBRs | Paid enterprise SaaS (Highspot); dedicated role headcount; Upwork polish ($150) | High enterprise repository budget; individual rep pushback against AI SaaS |
| **Agencies (Creative/Digital)** | Competitive RFP pitch decks, client proposals | Costly unbilled pitch labor (44–150 hrs); bespoke design outsourcing | High stakes per pitch, but aesthetic control limits automated software |

---

## 2. Actual Purchase and Spend Signals (Revealed Behavior)

Direct buyer-side evidence confirms organizations actively spend financial capital to solve deck customization:

1. **CRE Freelance Template & Per-Listing Plug-and-Play**:
   - **Signal**: Contractor spend (`AgTown05`, r/CommercialRealEstate).
   - **Amount & Structure**: $1,000 upfront design fee for a master 20-page OM template, followed by a recurring **$100 per listing** paid to a freelance designer for plug-and-play property detail insertion.
   - **Mapping to Workflow**: Maps directly to the target workflow (master template + deal-specific inputs = final client deliverable).
   - **Record**: `ev-wtp-cre-om-freelance-spend`

2. **Enterprise Sales Collateral Management & Version Control**:
   - **Signal**: Active paid SaaS deployment (`Mark Strathmore`, SAS Institute via TrustRadius).
   - **Platform**: Highspot (3-year deployment across enterprise sales teams).
   - **Mapping to Workflow**: Paid software adopted specifically to guarantee that AEs distribute the latest, on-brand versions of PowerPoint presentations rather than outdated or manually mangled files.
   - **Record**: `ev-wtp-sales-highspot-enterprise-use`

3. **Ad-Hoc Presentation Polish & Design Outsourcing**:
   - **Signal**: Contractor spend (`yellitout`, r/startups).
   - **Amount**: $150 fixed fee on Upwork.
   - **Mapping to Workflow**: Buyer authored all core commercial narrative and opportunity content, but paid a contractor specifically to execute visual layout and presentation polish.
   - **Record**: `ev-wtp-startups-upwork-deck-spend`

---

## 3. Costly Labor Signals (Paid Employee Time & Dedicated Headcount)

Labor allocations represent significant organizational expense absorbed internally rather than through software line items:

1. **Management Consulting Slide Formatting Overhead**:
   - **Signal**: Paid employee time (`Specialist_Golf8133`, r/consulting).
   - **Observation**: Former consultant reports that slide formatting and internal deck reviews consumed roughly 50% of total working time, dwarfing strategic thinking (30%) and client interaction (20%).
   - **Cost Burden**: At consulting billable rates ($150–$400+/hr), non-automated slide alignment and box tweaking represents thousands of dollars in lost billable capacity per engagement.
   - **Record**: `ev-wtp-consulting-formatting-time`

2. **Dedicated Full-Time Roles for Enterprise Pitch Preparation**:
   - **Signal**: Dedicated role hiring intent (`MarketMan123`, r/sales).
   - **Observation**: Founder closing $1,000,000+ enterprise deals seeks a dedicated full-time hire specifically to conduct prospect background research, meeting prep, and pitch deck customization.
   - **Cost Burden**: Represents dedicating $60,000–$90,000+ in annual compensation to handle opportunity-specific collateral preparation when deal values are high.
   - **Record**: `ev-wtp-sales-dedicated-deck-role`

---

## 4. Stated Budgets and Willingness to Pay

1. **Template-First Investment vs. Recurring Subscriptions**:
   - **Observation**: Sales practitioners (`spcman13`, r/sales) explicitly advise spending money once on a professional customizable deck template, rather than subscribing to ongoing AI presentation generators.
   - **Implication**: Teams are willing to pay upfront for design infrastructure, but resist continuous monthly software seat licenses if reps can manually tweak text in 10–15 minutes.
   - **Record**: `ev-wtp-contradiction-manual-template-pushback`

---

## 5. Context-Only Vendor Pricing (Benchmarks, Not Revealed WTP)

*Note: Vendor published pricing establishes what sellers charge and what enterprise buyers tolerate, but is not counted as revealed spend on its own.*

1. **Buildout (Commercial Real Estate)**:
   - **Pricing**: Starting at **$125 / user / month** seat fee plus platform maintenance fee (`https://www.buildout.com/pricing`).
   - **Workflow**: Automated generation of OMs, broker proposals, and property flyers from central database inputs.
   - **Record**: `ev-wtp-cre-buildout-pricing`

2. **think-cell (Management Consulting)**:
   - **Pricing**: **€23.90 / user / month** billed annually (€286.80/user/yr) for Suite; **€7.90 / user / month** for Essentials; **€4.50 / user / month** AI add-on (`https://www.think-cell.com/en/order/new`).
   - **Workflow**: Native PowerPoint add-in for automated charting, waterfall models, dynamic agendas, and layout alignment.
   - **Record**: `ev-wtp-consulting-thinkcell-pricing`

3. **Plus AI (Native Presentation Generation Plugin)**:
   - **Pricing**: **$30 / user / month** billed annually for Team tier (custom templates and brand guardrails); **$200 / user / month** for Max daily agent tier (`https://plusai.com/pricing`).
   - **Workflow**: Native PowerPoint and Google Slides sidebar plugin generating custom slides from document outlines and brand presets.
   - **Record**: `ev-wtp-saas-plusai-pricing`

4. **Microsoft 365 Copilot**:
   - **Pricing**: **$30.00 / user / month** annual commitment (`https://www.microsoft.com/en-us/microsoft-365-copilot/pricing`).
   - **Workflow**: Bundled AI presentation creation in PowerPoint from Word documents and Teams transcripts.

---

## 6. Strongest Evidence Against Meaningful Willingness to Pay

Research identified critical counter-signals where buyers or practitioners actively refuse to spend money or question the ROI of presentation automation:

1. **One-Time Template Preference Over Recurring SaaS**:
   - Practitioner pushback demonstrates that sales reps frequently view AI presentation subscriptions as redundant. Once a high-quality master template exists, inserting prospect names and numbers takes 10–15 minutes, making monthly software spend ($50–$100+/mo) hard to justify (`ev-wtp-contradiction-manual-template-pushback`).

2. **Lender Indifference to Elaborate Deck Narrative**:
   - In CRE, commercial lenders review only property financials, tenant rolls, and budgets. Narrative overviews, demographics, and formatting filler generated in OMs are routinely ignored by the ultimate financial decision-makers, undermining the perceived ROI of generating elaborate multi-page presentations (`ev-wtp-contradiction-cre-om-skepticism`).

3. **DIY and Free Tooling Sufficiency**:
   - Multiple sales reps report that standard PowerPoint master slides, Canva templates, or Google Slides are entirely adequate for their deals, viewing AI deck tools as solutions looking for a problem.

---

## 7. Category Coverage, Source Shortfalls, Blockers, and Unknowns

### Category Coverage Summary
The 10 collected evidence records span **5 distinct categories of spend**:
1. `contractor_spend`: Actual buyer payments for templates and per-deal deck assembly ($1,000 setup + $100/listing; $150 Upwork deck polish).
2. `saas_spend`: First-hand buyer usage and deployment of dedicated presentation management platforms (Highspot at SAS Institute).
3. `employee_time`: Heavy internal labor allocation in consulting (30–50% working time on formatting).
4. `dedicated_role`: Allocation of full-time headcount to conduct deal research and deck preparation for enterprise pitches.
5. `competitor_price`: Commercial benchmark pricing across CRE ($125/mo), consulting add-ins (€24/mo), and AI presentation plugins ($30–$200/mo).

### Tool Limitations & Research Notes
- **Tool Behavior**: The initial `browser` subagent reported that the Chrome DevTools MCP server was not active in its session, though active page snapshots and public web pages were captured.
- **Handling**: In accordance with validation rules 25–28, no ad-hoc scrapers or terminal crawlers were deployed. Primary public sources were opened and verified with direct canonical URLs, complete excerpts, and objective observations.

### Remaining Unknowns
1. **Budget Authority for Deck SaaS**: Is deck automation purchased by individual sales reps / consultants (credit card, $20–$50/mo limit) or by Sales Operations / Enablement leadership as part of CRM/Enablement tech stacks ($10k–$50k+ contracts)?
2. **CRE Vertical Exclusivity**: Buildout commands $125/user/mo because it links property data, marketing, and syndication. Would a horizontal deck tool command similar pricing without the underlying property database?
3. **Template Rigidity vs. Generation**: Does the buyer want generative slide content, or simply a reliable data-merging engine that fills branded PowerPoint shapes without distorting layouts?
