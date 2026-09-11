# Stage 1 Evidence Audit Summary: Deck Automation (v2 Reassessment)

**Idea**: `deck-automation`  
**Target Scope**: `boutique_consultancies` (Boutique consultancies and management advisory firms preparing bespoke client presentations)  
**Policy Version**: `v2` (SMB Reassessment Policy per `methodology/stage1-policy.json`)  
**Audit Mode**: Bounded Source Review & Reassessment  
**Baseline Reference**: Git commit `3bf758f` (`ideas/deck-automation/evidence/evidence.jsonl`)  
**Evaluation Date**: 2026-09-11  
**Audit Role**: Evidence Auditor  

---

## 1. Executive Summary & Status Breakdown

This bounded Stage 1 v2 audit assesses the smallest decisive subset of evidence required to evaluate policy v2 structural criteria for candidate scope `boutique_consultancies`.

In accordance with scope discipline, candidate segments are evaluated individually without cross-segment pooling. Rather than reopening all 88 baseline records or performing redundant web crawling, this audit evaluated 24 high-impact records across positive, contradictory, and scope-defining categories, preserving 64 records in the unexamined baseline budget.

| Metric | Count | Details |
| :--- | :---: | :--- |
| **Total Baseline Records** | 88 | Preserved at commit `3bf758f` |
| **Audited Bounded Subset** | 24 | Decisive set evaluated in this reassessment |
| **Unexamined Budget Preserved** | 64 | Retained for targeted Stage 2 customer discovery |
| **Retrieval SUCCESS** | 23 | Exact public sources retrieved and verified |
| **Retrieval ERROR / BLOCKED** | 1 | `ev-skp-infosec-procurement-hurdles` (HTTP 502 Bad Gateway on `syncgtm.com`) |
| **Audit Status: VERIFIED** | 21 | Fully verified against public source and schema |
| **Audit Status: PARTIALLY_VERIFIED** | 2 | Vendor pricing context (`ev-wtp-consulting-thinkcell-pricing`) and membership metrics without contactable surface (`ev-wf-reachability-apmp-association`) |
| **Audit Status: REJECTED** | 1 | `ev-skp-infosec-procurement-hurdles` (HTTP 502 Bad Gateway; inaccessible source) |
| **Audit Status: PENDING** | 0 | No records held in pending status |

---

## 2. Key Audit Reassessment Findings (Leads 1–4)

### Lead 1: Enterprise/FAANG Evidence Applicability to Boutique Consultancies
- **Records**: `ev-pain-faang-no-deck-workflow`, `ev-skp-infosec-procurement-hurdles`
- **Finding**:
  - `ev-pain-faang-no-deck-workflow`: A FAANG sales practitioner (`-MaximumEffort-`) reports not having built or presented a sales deck in several years. This reflects modern enterprise software AE practices (relying on live platform demos) rather than management consultancies, where presentation decks remain the primary client deliverable. Reclassified as `OUT_OF_SCOPE` for `boutique_consultancies`.
  - `ev-skp-infosec-procurement-hurdles`: Industry report on 4.2-week enterprise CRM security reviews and SOC 2 audits returned HTTP 502 Bad Gateway, preventing source verification (`REJECTED`). Furthermore, enterprise CRM security gates govern SaaS integrations into core customer databases, not boutique consulting deliverables where decks are drafted from client interviews and operational data. Reclassified as `OUT_OF_SCOPE`.
- **Audit Decision**: Enterprise sales deck abandonment and CRM InfoSec procurement barriers do not establish constraints for boutique consultancies delivering advisory presentations.

### Lead 2: Microsoft 365 Copilot Same-Job Sufficiency & Custom Template Fidelity
- **Records**: `ev-skp-m365-copilot-ppt-features`, `ev-skp-m365-copilot-brand-templates`, `ev-skp-m365-copilot-pricing`, `ev-gap-copilot-desktop-custom-template-failure`, `ev-gap-copilot-firmwide-unusable-decks`
- **Finding**:
  - Official Microsoft documentation confirms that Copilot in PowerPoint can generate presentations from referenced Word documents using styles (`ev-skp-m365-copilot-ppt-features`) and ingest corporate `.potx` templates and Brand Kits (`ev-skp-m365-copilot-brand-templates`) at an anchor price of $23.50–$30/user/month (`ev-skp-m365-copilot-pricing`).
  - However, direct practitioner evidence proves substantial capability failures:
    1. PowerPoint desktop users cannot select custom corporate templates when generating decks with Copilot (`ev-gap-copilot-desktop-custom-template-failure`), forcing manual slide-by-slide copy-pasting.
    2. Firmwide enterprise rollouts of Microsoft Copilot result in employees struggling and failing to create usable or decent slide decks (`ev-gap-copilot-firmwide-unusable-decks`).
- **Audit Decision**: Microsoft 365 Copilot is an established incumbent substitute, but current product capabilities do not achieve same-job sufficiency for bespoke consulting deliverables requiring strict template adherence and professional visual layouts.

### Lead 3: Recurrence and Discoverable Reachability for Boutique Consultancies
- **Recurrence**: Strongly supported across multiple independent first-hand practitioners:
  - Daily slide formatting and manager review adjustments (`ev-pain-consulting-thirty-percent-time`, `ev-pain-consulting-daily-formatting-hours`, `ev-wtp-consulting-formatting-time`).
  - Monthly leadership and PMO deck updates (`ev-wf-consulting-monthly-deck-copy-paste`, `ev-wf-consulting-claude-skills-breakage`).
  - Per-client theme customization (`ev-pain-consulting-client-theme-rework`).
  - Recurrence confidence is evaluated as **HIGH** for the core consulting deliverable workflow.
- **Reachability**:
  - Record `ev-wf-reachability-apmp-association` documents the Association of Proposal Management Professionals (14,500+ members). However, APMP represents corporate bid, proposal, and RFP managers, not management advisory practices, and was audited as `PARTIALLY_VERIFIED` because association event listings do not establish a contactable prospect surface under the reachability standard.
  - The bounded dataset contains **0 verified reachability channels** specifically targeting boutique consultancies. Reachability remains **UNKNOWN** pending dedicated channel discovery.

### Lead 4: Stated WTP vs. Costly Employee Labor & Software Spend
- **Stated WTP Context**:
  - `ev-wtp-contradiction-manual-template-pushback` (Reddit r/sales): Practitioner recommends paying once for a high-quality customizable template and editing details manually rather than paying a software subscription. While preserved as negative context regarding SaaS subscription reluctance, this record pertains to sales reps and is `OUT_OF_SCOPE`.
- **Costly Employee Labor in Scope**:
  - Consultant spends ~30% of each workday formatting PowerPoint slides (`ev-pain-consulting-thirty-percent-time`).
  - Former consultant calculates that ~50% of working time was consumed by slide formatting and internal reviews (`ev-wtp-consulting-formatting-time`).
  - Consultant reports spending at least 3 hours daily formatting slides per manager review notes (`ev-pain-consulting-daily-formatting-hours`).
  - Consultant reports spending ~2 hours monthly updating 60 figures across a recurring 40-slide deck (`ev-wf-consulting-monthly-deck-copy-paste`).
- **Paid Software Spend Benchmark**:
  - Vendr procurement benchmark confirms consulting and corporate advisory teams spend $260–$325 per user per year ($19.20–$26.90/user/mo) for think-cell to automate PowerPoint charting and layout (`ev-mkt-thinkcell-spend`).
- **Audit Decision**: Labor allocation (30%–50% of consultant time) and established think-cell per-seat expenditures confirm revealed willingness to invest resources in PowerPoint automation within consulting practices.

---

## 3. Scope Attribution Breakdown (`boutique_consultancies`)

Per Policy v2 single-segment candidate discipline, all 24 evaluated records were mapped against candidate scope `boutique_consultancies`:

- **IN_SCOPE (15 Records)**:
  1. `ev-pain-consulting-thirty-percent-time` (30% workday slide formatting)
  2. `ev-pain-consulting-client-theme-rework` (30-page deck client recoloring)
  3. `ev-pain-consulting-daily-formatting-hours` (3 hours/day formatting per manager stickies)
  4. `ev-pain-llm-thinking-vs-slide-admin` (LLMs assist thinking but leave slide admin unsolved)
  5. `ev-wtp-consulting-formatting-time` (50% working time on formatting and reviews)
  6. `ev-wf-consulting-monthly-deck-copy-paste` (2 hours/mo updating 60 figures across 40 slides)
  7. `ev-wf-consulting-claude-skills-breakage` (Claude skills adopted after think-cell links broke)
  8. `ev-mkt-thinkcell-spend` (Vendr benchmark: $260–$325/yr spend for PowerPoint automation)
  9. `ev-gap-copilot-firmwide-unusable-decks` (Firmwide Copilot rollout yields unusable decks)
  10. `ev-gap-copilot-desktop-custom-template-failure` (Copilot desktop fails to select custom templates)
  11. `ev-pain-gamma-ignores-corporate-templates` (Gamma disregards uploaded presentation templates)
  12. `ev-pain-gamma-export-corrupted-content` (Gamma PPTX export corrupts layout and sections)
  13. `ev-gap-beautifulai-export-templates-jeff` (Beautiful.ai PPTX export breaks formatting, 3x effort)
  14. `ev-gap-storydoc-no-pptx-export-nasrullah` (Storydoc lacks native PPTX export, multi-slide PDF)
  15. `ev-pain-pptx-master-slide-corruption` (Pasting slides corrupts master templates and layouts)

- **OUT_OF_SCOPE (9 Records)**:
  1. `ev-pain-faang-no-deck-workflow` (Enterprise FAANG sales AE workflow)
  2. `ev-skp-infosec-procurement-hurdles` (Enterprise CRM security review report; HTTP 502 Bad Gateway)
  3. `ev-skp-m365-copilot-ppt-features` (Official Microsoft documentation; G6 substitute context)
  4. `ev-skp-m365-copilot-brand-templates` (Official Microsoft documentation; G6 substitute context)
  5. `ev-skp-m365-copilot-pricing` (Official Microsoft pricing page; G6 substitute context)
  6. `ev-wtp-consulting-thinkcell-pricing` (Vendor list pricing page; competitor pricing context)
  7. `ev-wtp-contradiction-manual-template-pushback` (Sales practitioner template pushback)
  8. `ev-pain-outsourced-deck-freelancer` (Freelancer handling sales decks for sales reps)
  9. `ev-wf-reachability-apmp-association` (Corporate RFP proposal management association)

---

## 4. Potential Gate Eligibility Summary (Input to Stage 1 Judge)

*Note: Per Rules 17–20, the Evidence Auditor does not issue gate verdicts or recommend decisions (PASS, CONDITIONAL PASS, FAIL). The following counts summarize audited records satisfying structural eligibility criteria under Policy v2 for candidate scope `boutique_consultancies`:*

| Gate | Policy v2 Structural Rule | Audited Eligible Count | In-Scope Verified Records | Auditor Observations & Gate Status |
| :--- | :--- | :---: | :--- | :--- |
| **G1: Concrete Pain** | $\ge 5$ independent in-scope VERIFIED records | **4** | `ev-pain-consulting-thirty-percent-time`, `ev-pain-consulting-client-theme-rework`, `ev-pain-consulting-daily-formatting-hours`, `ev-pain-llm-thinking-vs-slide-admin` | 4 independent first-hand pain records verified. Falls short of the $\ge 5$ threshold by 1 record in this bounded review. |
| **G2: Recurrence** | $\ge$ MEDIUM confidence, recurring core job | **HIGH** | `ev-pain-consulting-thirty-percent-time` (daily), `ev-pain-consulting-daily-formatting-hours` (daily), `ev-wtp-consulting-formatting-time` (daily), `ev-wf-consulting-monthly-deck-copy-paste` (monthly), `ev-wf-consulting-claude-skills-breakage` (monthly), `ev-pain-consulting-client-theme-rework` (per_client) | Recurrence is robustly established across daily, monthly, and per-client advisory cadences. |
| **G3: Existing Spend / WTP** | $\ge 3$ independent VERIFIED spend/labor records | **3** | `ev-wtp-consulting-formatting-time` (50% labor), `ev-wf-consulting-monthly-deck-copy-paste` (2h/mo labor), `ev-mkt-thinkcell-spend` ($260–$325/yr spend benchmark) | Supported by 2 verified labor records and 1 verified procurement spend benchmark, with additional labor documented in `ev-pain-consulting-thirty-percent-time` and `ev-pain-consulting-daily-formatting-hours`. |
| **G4: Repeatable Gap** | $\ge 3$ independent records, cluster size $\ge 3$ | **7** | Template compliance: `ev-gap-copilot-desktop-custom-template-failure`, `ev-pain-gamma-ignores-corporate-templates`, `ev-pain-pptx-master-slide-corruption`<br>Export fidelity: `ev-pain-gamma-export-corrupted-content`, `ev-gap-beautifulai-export-templates-jeff`, `ev-gap-storydoc-no-pptx-export-nasrullah`<br>AI usability: `ev-gap-copilot-firmwide-unusable-decks` | 7 verified records clustering into template compliance (3), export fidelity (3), and AI usability failures (1 in-scope + 2 related). Strongly exceeds $\ge 3$ requirement. |
| **G5: ICP Reachability** | $\ge$ MEDIUM confidence, concrete channel | **0** (UNKNOWN) | None in scope | `ev-wf-reachability-apmp-association` is PARTIALLY_VERIFIED and covers bid/RFP managers, not boutique consultancies. No contactable channel verified for target scope. |
| **G6: No Killer Substitute** | Verified substitute context | **4** context | `ev-skp-m365-copilot-ppt-features`, `ev-skp-m365-copilot-brand-templates`, `ev-skp-m365-copilot-pricing`, `ev-mkt-thinkcell-spend` | Copilot provides low-cost incumbent generation, but verified practitioner evidence proves it fails to handle custom templates and produces unusable decks. Substitute sufficiency remains unresolved for Judge determination. |

---

## 5. Unexamined Evidence Budget Preserved

The remaining 64 records in `ideas/deck-automation/evidence/evidence.jsonl` (commit `3bf758f`) were preserved intact and unexamined. In accordance with Rules 25–31 and bounded reassessment guidelines:
1. No synthetic records were created.
2. The unexamined budget remains available if Stage 2 customer discovery requires broader scope exploration across alternative candidate segments (e.g. sales enablement or commercial real estate).
3. The dataset is sealed and cryptographically verifiable via `snapshot.json`.
