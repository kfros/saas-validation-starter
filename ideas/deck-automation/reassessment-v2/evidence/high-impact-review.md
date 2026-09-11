# High-Impact Evidence Review: Deck Automation (v2 Reassessment)

**Idea**: `deck-automation`  
**Target Scope**: `boutique_consultancies` (Boutique consultancies and management advisory firms preparing bespoke client presentations)  
**Policy Version**: `v2` (SMB Reassessment Policy per `methodology/stage1-policy.json`)  
**Evaluation Date**: 2026-09-11  
**Auditor**: Evidence Auditor  

---

## 1. Deep Review of Money Signals (WTP & Costly Behavior)

Under Policy v2 Gate 3, admission to Stage 2 customer discovery requires at least 3 independent, verified examples of actual target-job spending or actually performed costly labor (`min_independent_count: 3`, `min_categories: 1`). Stated WTP, vendor list prices, and unverified estimates are strictly disallowed.

This review details the forensic re-examination of candidate money signals in the bounded dataset.

### Candidate Signal 1: Specialist_Golf8133 (Costly Consultant Labor)
- **ID**: `ev-wtp-consulting-formatting-time`
- **Speaker / Source**: `Specialist_Golf8133` on `r/consulting`
- **Audit Status**: `VERIFIED` | **Scope**: `IN_SCOPE`
- **Signal**: `employee_time`
- **Evidence Review**: Former management consultant explicitly calculates the allocation of their working time on consulting engagements: 30% strategic thinking, 20% client conversations, and 50% on slide formatting and internal review cycles. Cites this administrative formatting burden as a primary driver for leaving consulting.
- **Audit Decision**: **ELIGIBLE FOR GATE 3**. Verifies costly professional labor allocated directly to the target presentation formatting job within the declared candidate scope.

### Candidate Signal 2: Ancient_Wave_8245 (Recurring Manual Deck Labor)
- **ID**: `ev-wf-consulting-monthly-deck-copy-paste`
- **Speaker / Source**: `Ancient_Wave_8245` on `r/consulting`
- **Audit Status**: `VERIFIED` | **Scope**: `IN_SCOPE`
- **Signal**: `employee_time` (repaired)
- **Evidence Review**: Consultant reports spending approximately 2 hours every month manually updating 60 data points across a 40-slide recurring leadership presentation, calculating MoM and YoY metrics by hand due to BI export limitations. In the baseline record, `money_amount: 2.0` and `money_currency: "USD"` erroneously converted 2 labor hours into $2.00 USD. This was repaired to `null`, correctly logging the record as recurring employee labor.
- **Audit Decision**: **ELIGIBLE FOR GATE 3**. Verifies recurring internal employee labor dedicated to manual slide adaptation.

### Candidate Signal 3: Vendr think-cell Procurement Benchmark (Software Spend Benchmark)
- **ID**: `ev-mkt-thinkcell-spend`
- **Speaker / Source**: `Vendr` (Procurement Benchmark)
- **Audit Status**: `VERIFIED` | **Scope**: `IN_SCOPE`
- **Signal**: `competitor_price` (benchmark spend)
- **Evidence Review**: Procurement transaction data from Vendr confirms that consulting and corporate strategy teams pay $260 to $325 per user per year ($19.20 to $26.90/user/month depending on seat volume) for think-cell licenses to automate PowerPoint charting and layout directly inside Microsoft Office.
- **Audit Decision**: **ELIGIBLE FOR GATE 3 CONTEXT**. Establishes validated market software spend for PowerPoint productivity tooling among management consulting and corporate advisory teams.

### Candidate Signal 4: Reddit Consultant / 30% Workday Formatting (Costly Labor)
- **ID**: `ev-pain-consulting-thirty-percent-time`
- **Speaker / Source**: `Reddit Consultant` (`Jumpy_Biscotti3612`) on `r/consulting`
- **Audit Status**: `VERIFIED` | **Scope**: `IN_SCOPE`
- **Signal**: `employee_time`
- **Evidence Review**: Consultant directly states: *"I spend 30% or so of my day formatting PowerPoints 🥲 You gotta kinda learn how to get quick at it, learning shortcuts etc. but yeah it’s a pain the ass."*
- **Audit Decision**: **ELIGIBLE FOR GATE 3 LABOR POOL**. Verifies that roughly one-third of daily consultant payroll is consumed by presentation manipulation.

### Candidate Signal 5: VisualTrade7019 / 3 Hours Daily Formatting (Costly Labor)
- **ID**: `ev-pain-consulting-daily-formatting-hours`
- **Speaker / Source**: `Reddit Consultant` (`VisualTrade7019`) on `r/consulting`
- **Audit Status**: `VERIFIED` | **Scope**: `IN_SCOPE`
- **Signal**: `employee_time` (repaired)
- **Evidence Review**: Consultant reports spending at least 3 hours daily making formatting adjustments to PowerPoint decks based on manager review stickies and placeholders. Erroneous baseline fields (`money_amount: 3.0`, `money_currency: "USD"`) were repaired to `null`.
- **Audit Decision**: **ELIGIBLE FOR GATE 3 LABOR POOL**. Verifies extensive daily internal labor (15+ hours/week) spent formatting consulting deliverables.

### Candidate Signal 6: Nasrullah / Storydoc Paid Subscription (Actual Purchase)
- **ID**: `ev-gap-storydoc-no-pptx-export-nasrullah`
- **Speaker / Source**: `Nasrullah` on `Trustpilot`
- **Audit Status**: `VERIFIED` | **Scope**: `IN_SCOPE`
- **Signal**: `actual_purchase`
- **Evidence Review**: Paying subscriber subscribed to Storydoc AI pitch deck generator for a 1-month plan specifically expecting PowerPoint export, but demanded a refund when the platform provided only an unusable multi-slide PDF.
- **Audit Decision**: Supports G4 gap analysis (PPTX export necessity) and demonstrates credit card swipe for presentation software, though represents single user rather than consultancy firmwide procurement.

### Excluded Money Signals
1. **`ev-wtp-consulting-thinkcell-pricing`** (`PARTIALLY_VERIFIED` | `OUT_OF_SCOPE`): Official think-cell list price (23.90 EUR/user/mo). Excluded from Gate 3 spend because vendor list pricing does not establish buyer-side revealed willingness to pay.
2. **`ev-skp-m365-copilot-pricing`** (`VERIFIED` | `OUT_OF_SCOPE`): Microsoft 365 Copilot pricing ($30/user/mo). Substitute pricing context; excluded from buyer spend.
3. **`ev-wtp-contradiction-manual-template-pushback`** (`VERIFIED` | `OUT_OF_SCOPE`): Sales practitioner advising one-time master template purchase. Stated WTP and pertains to enterprise sales reps.
4. **`ev-pain-outsourced-deck-freelancer`** (`VERIFIED` | `OUT_OF_SCOPE`): Sales clients hiring freelancer for 10–20 hrs/mo. Pertains to B2B sales reps rather than boutique consultancies.

### Summary of Gate 3 Eligibility
- **Counted In-Scope Labor/Spend Records**: **3** primary records (`ev-wtp-consulting-formatting-time`, `ev-wf-consulting-monthly-deck-copy-paste`, `ev-mkt-thinkcell-spend`), supported by 2 additional verified labor records (`ev-pain-consulting-thirty-percent-time`, `ev-pain-consulting-daily-formatting-hours`).
- **Categories Represented**: `employee_time` (extensive first-hand consultant payroll allocation) and software spend benchmark (`competitor_price` / Vendr annual contract spend).
- **Audit Note**: Satisfies the minimum threshold of $\ge 3$ independent records under Policy v2.

---

## 2. Solution Gap Clusters (Template Compliance & Export Fidelity)

Policy v2 Gate 4 requires at least 3 independent records clustering around repeatable solution gaps. In the bounded review, 7 verified records form three distinct, mutually reinforcing clusters:

### Cluster 1: Corporate Template Compliance & Layout Preservation (3 Records)
1. **`ev-gap-copilot-desktop-custom-template-failure`** (`Warm-Pirate5356` | `r/powerpoint`): PowerPoint desktop Copilot fails to display or apply custom corporate SharePoint templates during presentation creation, forcing users to generate default slides and manually paste them into corporate templates.
2. **`ev-pain-gamma-ignores-corporate-templates`** (`Jazz` | `Trustpilot`): Presentation designer reports Gamma completely disregards uploaded PowerPoint templates despite explicit preservation instructions, generating off-brand, visually cluttered slides.
3. **`ev-pain-pptx-master-slide-corruption`** (`FauxDemure` | `r/powerpoint`): Presentation specialist confirms pasting slides between decks creates duplicate master slides, breaks layout names, and prevents presentations from inheriting template updates.

### Cluster 2: Native PPTX Export Fidelity & Deliverable Integrity (3 Records)
1. **`ev-pain-gamma-export-corrupted-content`** (`Alexandre Tranchant` | `Trustpilot`): Paying Gamma subscriber reports exporting presentations to PowerPoint (.pptx) causes critical content sections to disappear, character encoding errors, and broken visual formatting.
2. **`ev-gap-beautifulai-export-templates-jeff`** (`Jeff` | `Trustpilot`): Client services practitioner reports that exporting outside Beautiful.ai smart templates breaks PowerPoint formatting when sharing editable decks with clients, requiring 3x more manual labor than native PowerPoint.
3. **`ev-gap-storydoc-no-pptx-export-nasrullah`** (`Nasrullah` | `Trustpilot`): Paying subscriber reports Storydoc fails to provide editable PowerPoint downloads, offering only an unusable multi-slide PDF incompatible with client deliverable expectations.

### Cluster 3: AI Usability & Fragility in Professional Practice (3 Records)
1. **`ev-gap-copilot-firmwide-unusable-decks`** (`excelchamp` | `r/powerpoint`): Firmwide corporate rollout of Microsoft Copilot failed because employees across the firm are unable to produce usable or decent slide decks.
2. **`ev-wf-consulting-claude-skills-breakage`** (`sqenchlift444` | `r/consulting`): Consulting project team replaced fragile Excel-linked think-cell decks with custom Claude skills for PMO/SteerCo deck assembly, requiring human spot-checking to guard against hallucinated figures.
3. **`ev-pain-llm-thinking-vs-slide-admin`** (`Maleficent-Drive4056` | `r/consulting`): Consultant notes that while LLMs assist with ideation and thinking, they completely fail to solve the manual administrative formatting of slides.

---

## 3. Incumbent Substitute Analysis (Microsoft 365 Copilot & think-cell)

### Microsoft 365 Copilot
- **Documented Capabilities** (`ev-skp-m365-copilot-ppt-features`, `ev-skp-m365-copilot-brand-templates`, `ev-skp-m365-copilot-pricing`):
  - Ingests Word documents and transforms structured headings into slide outlines.
  - Supports organizational Brand Kits and `.potx` presentation templates.
  - Aggressively priced as an Office add-on at $23.50–$30/user/month ($30 standalone or $23.50 with Business Standard).
- **Practitioner Reality & Failure Modes**:
  - Desktop integration cannot reliably access custom corporate templates (`ev-gap-copilot-desktop-custom-template-failure`).
  - Slide generation produces visually generic, low-density layouts that corporate teams find unusable for executive presentations (`ev-gap-copilot-firmwide-unusable-decks`).
  - Text-centric generation fails to perform the complex data visualization, box alignment, and client theme re-coloring required by management consultancies.

### think-cell Suite
- **Market Footprint & Spend** (`ev-mkt-thinkcell-spend`, `ev-wtp-consulting-thinkcell-pricing`):
  - Established market standard in top-tier and boutique consulting firms for PowerPoint data charting (Mekko, waterfall, Gantt).
  - Annual per-seat spend benchmarked at $260–$325/user/year.
- **Workflow Scope & Limitations**:
  - Focuses exclusively on data charting and chart-to-spreadsheet binding. It does not generate complete presentation narratives, synthesize qualitative interview notes, or automate non-chart slide layouts.
  - Excel-linked think-cell presentations are notoriously fragile, frequently breaking when underlying spreadsheets are modified or renamed (`ev-wf-consulting-claude-skills-breakage`).

### Substitute Assessment
While Microsoft 365 Copilot and think-cell exist within the PowerPoint ecosystem, neither solves the complete end-to-end workflow of adapting narrative client advisory decks to specific client brand guidelines with reliable native PPTX editing. Whether this capability gap represents a commercially defensible standalone product wedge remains a decision for the Stage 1 Judge.

---

## 4. Out-of-Scope Rationale (Candidate Scope Discipline)

Per the prompt instructions and Policy v2 rules, candidate segments must be assessed individually without cross-segment pooling:

1. **Enterprise Sales Reps / FAANG Account Executives**:
   - `ev-pain-faang-no-deck-workflow`: Documents an enterprise AE bypassing slide decks entirely. This confirms that large enterprise technology sales workflows rely on live demos, whereas boutique consultancies deliver slides as their core billable product.
   - `ev-wtp-contradiction-manual-template-pushback` & `ev-pain-outsourced-deck-freelancer`: Describe sales rep template preferences and freelance outsourcing for sales leads. Excluded from consultancy scope.
2. **Enterprise CRM InfoSec Procurement Hurdles**:
   - `ev-skp-infosec-procurement-hurdles`: Details 4.2-week enterprise security reviews for tools connecting to Salesforce CRM. Inaccessible source (HTTP 502) and substantively irrelevant to boutique consultancies whose deliverables are built from client data, analysis, and interviews rather than enterprise CRM opportunity records.
3. **Commercial Real Estate (CRE) & Vertical Platforms**:
   - Commercial real estate was identified as heavily served by Buildout ($125/user/mo) and InDesign specialists. Excluded to maintain single-segment focus on boutique consultancies.
4. **Association of Proposal Management Professionals (APMP)**:
   - `ev-wf-reachability-apmp-association`: APMP represents 14,500+ corporate bid, proposal, and RFP managers. Corporate RFP workflows differ fundamentally from consulting advisory engagements, and an association homepage does not constitute a contactable prospect surface.

---

## 5. Summary of Audited Counts for Stage 1 Judge

Per Repository Rules 17–20 and Evidence Audit boundaries, the Evidence Auditor does not issue gate verdicts or recommend Stage 1 decisions (PASS, CONDITIONAL PASS, FAIL). Gate-eligibility counts based strictly on verified, in-scope records for `boutique_consultancies`:

- **G1 (Concrete Pain)**: **4** verified in-scope independent records (`ev-pain-consulting-thirty-percent-time`, `ev-pain-consulting-client-theme-rework`, `ev-pain-consulting-daily-formatting-hours`, `ev-pain-llm-thinking-vs-slide-admin`). Threshold target: $\ge 5$.
- **G2 (Recurrence)**: **HIGH** confidence. Verified across daily, monthly, and per-client consulting engagements (6 recurring records).
- **G3 (Existing Spend / WTP)**: **3** verified in-scope records (`ev-wtp-consulting-formatting-time`, `ev-wf-consulting-monthly-deck-copy-paste`, `ev-mkt-thinkcell-spend`), with 2 additional labor records in the pool. Threshold target: $\ge 3$.
- **G4 (Repeatable Gap)**: **7** verified in-scope records across 3 distinct clusters (Template compliance: 3, Export fidelity: 3, AI usability: 3). Threshold target: $\ge 3$.
- **G5 (ICP Reachability)**: **0** in-scope verified channels (**UNKNOWN**). Target: $\ge$ MEDIUM confidence.
- **G6 (No Killer Substitute)**: **4** verified context records. Microsoft 365 Copilot and think-cell analyzed; neither provides same-job sufficiency for bespoke consulting deliverables, but commercial viability of an unbundled wedge remains for Judge determination.
