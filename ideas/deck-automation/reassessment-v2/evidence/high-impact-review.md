# High-Impact Evidence Review: Deck Automation (v2 Reassessment)

**Idea**: `deck-automation`
**Target Scope**: `boutique_consultancies` (Boutique consultancies and management advisory firms preparing bespoke client presentations)
**Policy Version**: `v2` (SMB Reassessment Policy per `methodology/stage1-policy.json`)
**Evaluation Date**: 2026-09-11
**Auditor**: Evidence Auditor

---

## 1. Deep Review of Money Signals (WTP & Costly Behavior)

Under Policy v2 Gate 3, admission to Stage 2 customer discovery requires at least 3 independent, verified examples of actual target-job spending or actually performed costly labor (`min_independent_count: 3`, `min_categories: 1`). Stated WTP, vendor list prices, and unverified estimates are strictly disallowed. Furthermore, competitor software prices (`competitor_price`) are explicitly disqualified under Policy v2 from serving as Gate 3 evidence, and candidate labor records qualify only when the target candidate scope is independently established.

This review details the forensic re-examination of candidate money signals in the bounded dataset.

### Candidate Signal 1: Specialist_Golf8133 (Consultant Labor)
- **ID**: `ev-wtp-consulting-formatting-time`
- **Speaker / Source**: `Specialist_Golf8133` on `r/consulting`
- **Audit Status**: `VERIFIED` | **Scope**: `UNKNOWN`
- **Signal**: `employee_time`
- **Evidence Review**: Former management consultant estimates spending 50% of working time on slide formatting and internal review cycles. Cites administrative formatting burden as a primary reason for leaving consulting.
- **Audit Decision**: **INELIGIBLE FOR GATE 3**. While the comment documents costly formatting labor, firm size and firm type are not stated in the source. Under candidate discipline, membership in `r/consulting` does not directly establish affiliation with an SMB/boutique consultancy. Labor cannot qualify for G3 when target scope is unestablished.

### Candidate Signal 2: Ancient_Wave_8245 (Recurring Internal Reporting Deck)
- **ID**: `ev-wf-consulting-monthly-deck-copy-paste`
- **Speaker / Source**: `Ancient_Wave_8245` on `r/consulting`
- **Audit Status**: `VERIFIED` | **Scope**: `OUT_OF_SCOPE`
- **Signal**: `employee_time` (repaired)
- **Evidence Review**: Practitioner reports spending approximately 2 hours every month manually updating 60 data points across a 40-slide recurring presentation for internal corporate leadership and CFO, calculating MoM and YoY metrics by hand due to BI export limitations. Erroneous baseline price fields were repaired to null.
- **Audit Decision**: **INELIGIBLE FOR GATE 3**. The deck is an internal corporate finance / FP&A reporting deliverable for executive management, not a bespoke client advisory deliverable produced by a boutique consultancy.

### Candidate Signal 3: Vendr think-cell Procurement Benchmark (Marketplace Pricing Benchmark)
- **ID**: `ev-mkt-thinkcell-spend`
- **Speaker / Source**: `Vendr` (Procurement Benchmark)
- **Audit Status**: `VERIFIED` | **Scope**: `OUT_OF_SCOPE`
- **Signal**: `competitor_price` (benchmark spend tiers)
- **Evidence Review**: Procurement transaction data from Vendr indicates volume tier pricing ($19.20 to $26.90/user/month; $260 to $325/yr) for think-cell licenses.
- **Audit Decision**: **DISQUALIFIED FOR GATE 3; PRESERVED AS G6 SUBSTITUTE CONTEXT**. The signal type is `competitor_price`, which Policy v2 explicitly disallows for Gate 3. In addition, the Vendr marketplace benchmark reflects aggregated multi-tier vendor pricing rather than documented spend specifically by boutique consultancies. Retained as verified incumbent substitute context for Gate 6.

### Candidate Signal 4: Reddit Consultant / 30% Workday Formatting (Consultant Labor)
- **ID**: `ev-pain-consulting-thirty-percent-time`
- **Speaker / Source**: `Reddit Consultant` (`Jumpy_Biscotti3612`) on `r/consulting`
- **Audit Status**: `VERIFIED` | **Scope**: `UNKNOWN`
- **Signal**: `employee_time`
- **Evidence Review**: Anonymous Reddit user states: *"I spend 30% or so of my day formatting PowerPoints 🥲 You gotta kinda learn how to get quick at it, learning shortcuts etc. but yeah it’s a pain the ass."*
- **Audit Decision**: **INELIGIBLE FOR GATE 3**. The post does not disclose firm size or firm type. Subreddit membership alone cannot substitute for direct captured evidence of an SMB/boutique consultancy practice.

### Candidate Signal 5: VisualTrade7019 / 3 Hours Daily Formatting (Consultant Labor)
- **ID**: `ev-pain-consulting-daily-formatting-hours`
- **Speaker / Source**: `Reddit Consultant` (`VisualTrade7019`) on `r/consulting`
- **Audit Status**: `VERIFIED` | **Scope**: `UNKNOWN`
- **Signal**: `employee_time` (repaired)
- **Evidence Review**: Consultant reports spending at least 3 hours daily making formatting adjustments to PowerPoint decks based on manager review stickies and placeholders. Erroneous baseline price fields were repaired to null.
- **Audit Decision**: **INELIGIBLE FOR GATE 3**. Firm type and organization size are unstated. Scope remains `UNKNOWN`; ineligible for G3.

### Candidate Signal 6: Nasrullah / Storydoc Paid Subscription (Actual Purchase)
- **ID**: `ev-gap-storydoc-no-pptx-export-nasrullah`
- **Speaker / Source**: `Nasrullah` on `Trustpilot`
- **Audit Status**: `VERIFIED` | **Scope**: `UNKNOWN`
- **Signal**: `actual_purchase`
- **Evidence Review**: Paying subscriber subscribed to Storydoc AI pitch deck generator for a 1-month plan specifically expecting PowerPoint export, but demanded a refund when the platform provided only an unusable multi-slide PDF.
- **Audit Decision**: **INELIGIBLE FOR GATE 3**. Pertains to an individual pitch deck creator whose professional firm context is unstated (`UNKNOWN` scope).

### Excluded Money Signals
1. **`ev-wtp-consulting-thinkcell-pricing`** (`PARTIALLY_VERIFIED` | `OUT_OF_SCOPE`): Official think-cell list price (23.90 EUR/user/mo). Vendor list pricing does not establish buyer-side revealed willingness to pay.
2. **`ev-skp-m365-copilot-pricing`** (`VERIFIED` | `OUT_OF_SCOPE`): Microsoft 365 Copilot pricing ($30/user/mo). Incumbent substitute pricing context for G6.
3. **`ev-wtp-contradiction-manual-template-pushback`** (`VERIFIED` | `OUT_OF_SCOPE`): Sales practitioner advising one-time master template purchase. Stated WTP and pertains to enterprise sales reps.
4. **`ev-pain-outsourced-deck-freelancer`** (`VERIFIED` | `OUT_OF_SCOPE`): Sales clients hiring freelancer for 10–20 hrs/mo. Pertains to B2B sales reps rather than boutique consultancies.

### Summary of Gate 3 Eligibility
- **Counted In-Scope Labor/Spend Records**: **0** records eligible.
- **Threshold Target**: $\ge 3$ independent records under Policy v2.
- **Audit Conclusion**: Threshold is not met (0 eligible records). All candidate labor records lack direct boutique consultancy attribution (`UNKNOWN` or `OUT_OF_SCOPE`), and `ev-mkt-thinkcell-spend` is disallowed by Policy v2 due to `competitor_price` signal type and unestablished scope.

---

## 2. Solution Gap Clusters (Template Compliance & Export Fidelity)

Policy v2 Gate 4 requires at least 3 independent records clustering around repeatable solution gaps within the evaluated candidate scope. While the bounded review identified 7 verified records documenting real technical and workflow shortcomings across modern presentation tools, **0 records have direct captured support for boutique consultancies** (all 7 reclassified to `UNKNOWN` scope). Consequently, in-scope Gate 4 eligible count is **0**.

For diagnostic reference, the documented failure clusters comprise:

### Cluster 1: Corporate Template Compliance & Layout Preservation (3 Records, Scope: UNKNOWN)
1. **`ev-gap-copilot-desktop-custom-template-failure`** (`Warm-Pirate5356` | `r/powerpoint`): PowerPoint desktop Copilot fails to display or apply custom corporate SharePoint templates during presentation creation, forcing users to generate default slides and manually paste them into corporate templates.
2. **`ev-pain-gamma-ignores-corporate-templates`** (`Jazz` | `Trustpilot`): Presentation designer reports Gamma completely disregards uploaded PowerPoint templates despite explicit preservation instructions, generating off-brand, visually cluttered slides.
3. **`ev-pain-pptx-master-slide-corruption`** (`FauxDemure` | `r/powerpoint`): Presentation specialist confirms pasting slides between decks creates duplicate master slides, breaks layout names, and prevents presentations from inheriting template updates.

### Cluster 2: Native PPTX Export Fidelity & Deliverable Integrity (3 Records, Scope: UNKNOWN)
1. **`ev-pain-gamma-export-corrupted-content`** (`Alexandre Tranchant` | `Trustpilot`): Paying Gamma subscriber reports exporting presentations to PowerPoint (.pptx) causes critical content sections to disappear, character encoding errors, and broken visual formatting.
2. **`ev-gap-beautifulai-export-templates-jeff`** (`Jeff` | `Trustpilot`): Client services practitioner reports that exporting outside Beautiful.ai smart templates breaks PowerPoint formatting when sharing editable decks with clients, requiring 3x more manual labor than native PowerPoint.
3. **`ev-gap-storydoc-no-pptx-export-nasrullah`** (`Nasrullah` | `Trustpilot`): Paying subscriber reports Storydoc fails to provide editable PowerPoint downloads, offering only an unusable multi-slide PDF incompatible with client deliverable expectations.

### Cluster 3: AI Usability & Fragility in Professional Practice (3 Records, Scope: UNKNOWN)
1. **`ev-gap-copilot-firmwide-unusable-decks`** (`excelchamp` | `r/powerpoint`): Firmwide corporate rollout of Microsoft Copilot failed because employees across the firm are unable to produce usable or decent slide decks.
2. **`ev-wf-consulting-claude-skills-breakage`** (`sqenchlift444` | `r/consulting`): Project team replaced fragile Excel-linked think-cell decks with custom Claude skills for PMO/SteerCo deck assembly, requiring human spot-checking to guard against hallucinated figures.
3. **`ev-pain-llm-thinking-vs-slide-admin`** (`Maleficent-Drive4056` | `r/consulting`): Consultant notes that while LLMs assist with ideation and thinking, they fail to solve the manual administrative formatting of slides.

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
  - Established market standard in consulting for PowerPoint data charting (Mekko, waterfall, Gantt).
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
   - `ev-skp-infosec-procurement-hurdles`: Details 4.2-week enterprise security reviews for tools connecting to Salesforce CRM. Inaccessible source (HTTP 502 Bad Gateway; held as `PENDING`) and substantively irrelevant to boutique consultancies whose deliverables are built from client data, analysis, and interviews rather than enterprise CRM opportunity records.
3. **Internal Corporate FP&A / Finance Reporting**:
   - `ev-wf-consulting-monthly-deck-copy-paste`: Describes a recurring monthly 40-slide reporting deck for internal executive leadership and CFO with BI exports. Represents corporate FP&A reporting rather than bespoke client deliverables by a boutique consultancy.
4. **Incumbent Pricing & Marketplace Benchmarks**:
   - `ev-skp-m365-copilot-pricing`, `ev-wtp-consulting-thinkcell-pricing`, and `ev-mkt-thinkcell-spend`: Vendor list pricing and third-party marketplace pricing benchmarks provide market context for G6 substitutes, but do not qualify as buyer-side evidence for boutique consultancies.
5. **Commercial Real Estate (CRE) & Vertical Platforms**:
   - Commercial real estate was identified as heavily served by Buildout ($125/user/mo) and InDesign specialists. Excluded to maintain single-segment focus on boutique consultancies.
6. **Association of Proposal Management Professionals (APMP)**:
   - `ev-wf-reachability-apmp-association`: APMP represents 14,500+ corporate bid, proposal, and RFP managers. Corporate RFP workflows differ fundamentally from consulting advisory engagements, and an association homepage does not constitute a contactable prospect surface.

---

## 5. Summary of Audited Counts for Stage 1 Judge

Per Repository Rules 17–20 and Evidence Audit boundaries, the Evidence Auditor does not issue gate verdicts or recommend Stage 1 decisions (PASS, CONDITIONAL PASS, FAIL). Gate-eligibility counts based strictly on verified, in-scope records for `boutique_consultancies`:

- **G1 (Concrete Pain)**: **0** verified in-scope independent records (4 candidate records reclassified to `UNKNOWN`). Threshold target: $\ge 5$.
- **G2 (Recurrence)**: **0** (UNKNOWN) confidence. Candidate recurring records lack direct boutique consultancy attribution.
- **G3 (Existing Spend / WTP)**: **0** verified in-scope records. `ev-mkt-thinkcell-spend` disqualified under Policy v2 (`competitor_price` signal, boutique scope unestablished; kept for G6 context); candidate labor records lack target scope attribution (`UNKNOWN` / `OUT_OF_SCOPE`). Threshold target: $\ge 3$.
- **G4 (Repeatable Gap)**: **0** verified in-scope records (7 verified gap records reclassified to `UNKNOWN` scope). Threshold target: $\ge 3$.
- **G5 (ICP Reachability)**: **0** in-scope verified channels (**UNKNOWN**). Target: $\ge$ MEDIUM confidence.
- **G6 (No Killer Substitute)**: **4** verified context records (`ev-skp-m365-copilot-ppt-features`, `ev-skp-m365-copilot-brand-templates`, `ev-skp-m365-copilot-pricing`, `ev-mkt-thinkcell-spend`). Microsoft 365 Copilot and think-cell analyzed; neither provides same-job sufficiency for bespoke consulting deliverables, but commercial viability of an unbundled wedge remains for Judge determination.
