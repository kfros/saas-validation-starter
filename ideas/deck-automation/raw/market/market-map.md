# Market Map: B2B Deck & Sales Collateral Automation

## Executive Market Summary

The market surrounding B2B presentation and sales collateral automation is bifurcated into two polar extremes, with distinct capabilities, pricing, and structural limitations:

1. **Horizontal Consumer / Prosumer AI Presentation Generators ($10–$25/user/month):**
   - Products: Gamma, Beautiful.ai, Pitch, Plus AI, Canva Magic Design.
   - Characteristics: Web-first canvas or light add-in, rapid text-to-slide generation, fixed template libraries.
   - Core Gap: They do not reliably adhere to arbitrary corporate PowerPoint master layouts (.potx). Exports to PPTX frequently cause font substitutions, misaligned text boxes, broken layouts, or flattened images. Furthermore, they lack multi-source context synthesis (e.g. merging CRM notes + case studies + deal terms).

2. **Enterprise Sales Enablement Platforms & Template Governance ($40/user/month to $70,000–$180,000+ ACV):**
   - Products: Seismic (LiveDocs), Highspot (AutoDocs), Templafy, UpSlide.
   - Characteristics: Deep native PowerPoint integration, direct Salesforce/Dynamics data merging, strict template locking and marketing compliance workflows.
   - Core Gap: High minimum contract sizes (50–100+ seats), expensive implementation services ($5,000–$50,000), long procurement cycles, and heavy administrative overhead. Completely inaccessible to SMBs, boutique consultancies, agencies, and lean mid-market teams.

3. **Web-Based Interactive Collateral Substitutes ($20–$35/user/month to $275+/month):**
   - Products: Storydoc, Qwilr, PandaDoc.
   - Characteristics: Replaces PowerPoint entirely with trackable, interactive web pages connected to CRM data.
   - Core Gap: **Zero native editable PPTX output.** Unviable for enterprise buyers whose internal procurement, compliance, or executive standards require offline, deliverable .pptx files.

4. **Incumbent AI Suite (Microsoft 365 Copilot):**
   - Pricing: $30/user/month (annual commitment + qualifying M365 license).
   - Capabilities & Limits: Native PPTX, but restricted to referencing a single file at a time (e.g., one Word doc under 24MB) without additional contextual prompting. Cannot synthesize CRM context, case study repositories, and opportunity notes in a single automated pass.

---

## Competitor & Substitute Landscape

| Category | Representative Players | Pricing / Contract Model | PPTX Export Fidelity | Custom Corporate Template (.potx) Support | CRM / Multi-Source Personalization | Target ICP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Horizontal AI Slides** | Gamma, Beautiful.ai, Pitch | $10 – $28 / user / mo | **Medium to Poor**: Text wrapping, font substitution, loss of dynamic rules, card-to-slide reflow | **Proprietary Themes Only**: Requires recreating themes in their web editors; no arbitrary .potx master mapping | **None / Basic**: Prompt-driven or single document upload | Freelancers, startups, non-technical knowledge workers |
| **PowerPoint AI Add-ins** | Plus AI (Plus Docs) | $15 – $25 / user / mo (Enterprise custom) | **High**: Runs inside PPT/Google Slides | **Limited / Beta**: Custom templates restricted to beta or white-glove enterprise setup | **Basic**: Accepts text outlines, documents, or prompts | Individual consultants, small teams |
| **Office Productivity Incumbent** | Microsoft 365 Copilot | $30 / user / mo (annual commitment) | **Native PPTX**: Native Office engine | **Supported with Brand Kit**: Requires enterprise setup and start from template | **Constrained**: Max 1 input file (Word/PDF < 24MB); no prompt customization when file attached | Knowledge workers in M365 ecosystem |
| **Enterprise Enablement (Dynamic Decks)** | Highspot (AutoDocs), Seismic (LiveDocs) | $45 – $65 / user / mo, **$70k – $180k+ annual minimums**, $5k–$50k setup | **Native PPTX**: Direct PPT add-in & server generation | **Complete**: Native PowerPoint template placeholders, marketing lockouts | **Deep**: Automated merge of Salesforce / Dynamics opportunities and custom fields | Large Enterprise (500+ employees), dedicated enablement teams |
| **Document / Template Governance** | Templafy, UpSlide | $40 / user / mo (Templafy Teams) to custom enterprise | **Native PPTX**: Direct PPT add-in | **Complete**: Enforces corporate typography, palettes, dynamic slide libraries | **Moderate**: Pulls CRM data into pre-set placeholders; Excel-to-PPT linking (UpSlide) | Enterprise IT, RevOps, Investment Banking, Consulting |
| **Interactive Web Substitutes** | Storydoc, Qwilr | $20 – $36 / user / mo (Storydoc), $35 – $275+/mo (Qwilr) | **None / Static PDF only**: Explicitly rejects PPTX | **Web Templates Only**: No PPTX template ingestion | **Deep**: Direct Salesforce & HubSpot dynamic variables | B2B sales reps open to sending web links |

---

## Detailed Competitor Breakdown

### 1. Gamma (gamma.app)
- **Positioning**: AI-first workspace for presentations, documents, and web pages using cards rather than traditional 16:9 slides.
- **Pricing**: Free ($0, 400 credits); Plus ($10/user/mo monthly, $8 annual); Pro ($20/user/mo monthly, $15 annual); Business ($40/seat/mo billed annually).
- **Capabilities & Gaps**: Supports exporting to PPTX on all plans (with watermark on Free). Tables export as editable objects. However, because content is authored in flexible fluid web cards, exporting to PowerPoint introduces layout drift, element stacking issues, and font substitutions. Does not support uploading a client's .potx template to auto-populate master slide layouts.

### 2. Beautiful.ai (beautiful.ai)
- **Positioning**: Presentation software using smart slide layouts that adapt dynamically as users type.
- **Pricing**: Pro ($12/user/mo billed annually at $144, or $45 monthly); Team ($40/user/mo billed annually); Enterprise (custom quote).
- **Capabilities & Gaps**: PPTX export is available on Pro/Team plans and produces editable shapes/text. However, Beautiful.ai's proprietary layout constraints do not transfer to PowerPoint. When opened in PowerPoint, slides lose dynamic repositioning rules and custom animations. Corporate templates must be configured inside Beautiful.ai's platform rather than importing native .potx files.

### 3. Plus AI / Plus Docs (plusdocs.com)
- **Positioning**: AI presentation maker that works directly as an add-in for Microsoft PowerPoint and Google Slides.
- **Pricing**: Basic ($15/user/mo); Pro ($25/user/mo or $20 annual); Enterprise (custom pricing).
- **Capabilities & Gaps**: Operates inside PowerPoint, avoiding export conversion bugs. However, custom template support is in beta (primarily Google Slides) and only handles simple text/image designs; complex enterprise templates require custom white-glove setup. Lacks CRM pipeline connectors or multi-document contextual grounding.

### 4. Microsoft 365 Copilot for PowerPoint
- **Positioning**: Built-in AI assistant for Microsoft 365 productivity suite.
- **Pricing**: $30/user/month (annual commitment, required prerequisite base license like Business Standard/Premium or E3/E5).
- **Capabilities & Gaps**: Can build presentations from natural language prompts or an uploaded reference Word document (up to 24MB). While it can use organization templates via Brand Kits, it possesses rigid limitations: it can only ingest one reference file at a time, does not allow additional contextual prompt guidance when a file is referenced, and frequently produces generic text bullets requiring manual redesign.

### 5. Storydoc (storydoc.com) — *Key Workflow Substitute*
- **Positioning**: Interactive web-based sales deck and proposal software designed to replace static PowerPoint presentations.
- **Pricing**: Starter ($19.80/mo annual); Pro ($36/mo annual); Team (custom quote for 5+ seats).
- **Capabilities & Gaps**: Directly integrates with Salesforce and HubSpot to dynamically generate client-specific presentations with embedded ROI calculators, videos, and real-time viewing analytics. **Fatal Gap for Hypothesis**: Storydoc cannot export to native editable PPTX (offers only hosted web links or static PDF downloads). If an enterprise client or procurement workflow mandates editable PPTX, Storydoc is disqualified.

### 6. Highspot AutoDocs & Seismic LiveDocs — *Enterprise Substitutes*
- **Positioning**: Market leaders in Enterprise Sales Enablement.
- **Capabilities**: Both platforms allow revenue operations to create PowerPoint templates with dynamic placeholders and business rules. A seller selects an opportunity in Salesforce, and the system automatically generates a customized PPTX deck pulling relevant case studies, product modules, and client data.
- **Pricing & Barrier**:
  - Highspot: Estimated $45–$65/user/month with typical annual contracts of $70,000 to $180,000+ and $5,000–$50,000 implementation fees. Minimum 50+ seats.
  - Seismic: Estimated $500–$650/user/year with annual contracts of $50,000 to $250,000+.
  - Barrier: Completely unreachable for SMBs, boutique consultancies, agencies, and small mid-market sales teams.

### 7. UpSlide (upslide.net) & Templafy (templafy.com)
- **Positioning**: Enterprise template governance and productivity add-ins for Microsoft 365.
- **Pricing**: Templafy Teams at $40/user/month; UpSlide and Templafy Enterprise require custom quotes (several hundred dollars per seat/year).
- **Capabilities**: Directly manage slide libraries in PowerPoint, enforce brand guidelines, automate table of contents, and link Excel financial models to PowerPoint charts.
- **Gaps**: Focused on manual assembly from pre-approved modular slides and financial table updates rather than end-to-end AI synthesis from opportunity notes.

### 8. Tome (tome.app) — *Market Failure / Cautionary Indicator*
- **Market Trajectory**: Originally raised tens of millions and amassed 20 million users as a viral consumer AI presentation generator.
- **Outcome**: Officially discontinued its presentation product on April 30, 2025, deleted user presentations, and pivoted the company to Lightfield (an AI CRM) due to low monetization and enterprise retention.
- **Implication**: Confirms that broad, horizontal text-to-slide generation without deep workflow integration and enterprise formatting fidelity suffers from severe commoditization and churn.

---

## Contradictory Evidence & Falsification Check (Skill Requirement)

In compliance with workspace rules requiring the preservation of negative and contradictory evidence:

1. **Enterprise Workflow is Already Solved:**
   - For Fortune 500 and large enterprise revenue teams, the exact proposed workflow (CRM data + master template -> automated personalized PPTX deck) is already completely solved by Highspot AutoDocs and Seismic LiveDocs. Any attempt by the hypothesis to target large enterprise sales teams will run directly into entrenched incumbents.

2. **Web-Native Collateral Adoption (The "PPTX is Dead" Trend):**
   - Storydoc, Qwilr, and PandaDoc demonstrate that a subset of modern B2B sales teams are deliberately abandoning PowerPoint in favor of interactive web links with integrated tracking, video, and e-signatures. If target ICPs prefer trackable web links over PPTX, the core value proposition of editable PPTX output is undermined.

3. **Incumbent Pricing Ceiling:**
   - Microsoft 365 Copilot ($30/user/mo), Google Workspace Gemini ($20–$30/user/mo), Gamma ($10–$20/user/mo), and Beautiful.ai ($12–$40/user/mo) establish strong market expectation that generic presentation AI costs between $10 and $40 per user per month. Justifying a price materially above $100/month requires proving massive, measurable time savings or agency replacement value.

---

## Identified Market Gap (The Wedge)

The market research reveals a clear, structural gap:

```
Low-End: Horizontal AI Tools ($10-$25/mo)
  [Gamma, Beautiful.ai, Pitch, Canva]
  - Fast, but wrong format (web-first)
  - Broken PPTX exports, missing master .potx support
  - No CRM / deal context integration
           │
           ▼
  ==============================================
  THE UNADDRESSED WEDGE:
  SMB & Mid-Market Vertical Sales Deck Automation
  - Native editable PPTX output (.pptx)
  - Ingestion of company master templates (.potx)
  - Multi-source context synthesis (CRM + notes + case studies)
  - Self-serve or low-touch onboarding ($100–$300/mo team price)
  ==============================================
           ▲
           │
High-End: Enterprise Enablement ($70k-$180k+/yr ACV)
  [Highspot AutoDocs, Seismic LiveDocs, Templafy]
  - Native PPTX + Salesforce integration
  - Requires 50-100+ seats, dedicated admins, $5k-$50k setup
  - Inaccessible to SMBs, consultancies, and agencies
```

### Key Technical & Functional Requirements Identified by Market Research:
1. **Native PowerPoint Master Support:** Any viable solution in this wedge must ingest an existing corporate `.potx` or master deck, extract its slide layouts, placeholders, and font/color schemes, and populate them directly without cross-platform translation artifacts.
2. **Multi-Source Context Synthesis:** Unlike Copilot (limited to 1 Word file without prompt guidance), the workflow requires combining CRM opportunity notes, transcript excerpts, and approved proof points.
3. **Editable Native PPTX Deliverable:** Delivering web links (like Storydoc) disqualifies the solution for enterprise buyers with strict offline/security mandates; output must be 100% editable native `.pptx`.
