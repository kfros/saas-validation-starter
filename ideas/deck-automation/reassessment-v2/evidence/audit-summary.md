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
| **Audit Status: REJECTED** | 0 | No records rejected; blocked inspection held as PENDING |
| **Audit Status: PENDING** | 1 | `ev-skp-infosec-procurement-hurdles` (HTTP 502 Bad Gateway; inaccessible source) |

---

## 2. Key Audit Reassessment Findings (Leads 1–4)

### Lead 1: Enterprise/FAANG Evidence Applicability to Boutique Consultancies
- **Records**: `ev-pain-faang-no-deck-workflow`, `ev-skp-infosec-procurement-hurdles`
- **Finding**:
  - `ev-pain-faang-no-deck-workflow`: A FAANG sales practitioner (`-MaximumEffort-`) reports not having built or presented a sales deck in several years. This reflects modern enterprise software AE practices (relying on live platform demos) rather than management consultancies, where presentation decks remain the primary client deliverable. Classified as `OUT_OF_SCOPE` for `boutique_consultancies`.
  - `ev-skp-infosec-procurement-hurdles`: Industry report on 4.2-week enterprise CRM security reviews and SOC 2 audits returned HTTP 502 Bad Gateway. Under policy v2, when inspection is prevented solely by HTTP/tool failure, the record is reclassified as `PENDING`, remaining blocked and ineligible. Furthermore, enterprise CRM security gates govern SaaS integrations into core customer databases, not boutique consulting deliverables where decks are drafted from client interviews and operational data. Classified as `OUT_OF_SCOPE`.
- **Audit Decision**: Enterprise sales deck abandonment and CRM InfoSec procurement barriers do not establish constraints for boutique consultancies delivering advisory presentations.

### Lead 2: Microsoft 365 Copilot Same-Job Sufficiency & Custom Template Fidelity
- **Records**: `ev-skp-m365-copilot-ppt-features`, `ev-skp-m365-copilot-brand-templates`, `ev-skp-m365-copilot-pricing`, `ev-gap-copilot-desktop-custom-template-failure`, `ev-gap-copilot-firmwide-unusable-decks`
- **Finding**:
  - Official Microsoft documentation confirms that Copilot in PowerPoint can generate presentations from referenced Word documents using styles (`ev-skp-m365-copilot-ppt-features`) and ingest corporate `.potx` templates and Brand Kits (`ev-skp-m365-copilot-brand-templates`) at an anchor price of $23.50–$30/user/month (`ev-skp-m365-copilot-pricing`). These records provide substitute context for G6 and are `OUT_OF_SCOPE` for candidate practitioner evidence.
  - Direct practitioner gap evidence reveals substantial capability failures:
    1. PowerPoint desktop users cannot select custom corporate templates when generating decks with Copilot (`ev-gap-copilot-desktop-custom-template-failure`), forcing manual slide-by-slide copy-pasting.
    2. Firmwide enterprise rollouts of Microsoft Copilot result in employees struggling and failing to create usable or decent slide decks (`ev-gap-copilot-firmwide-unusable-decks`).
  - However, neither of these gap reports directly establishes that the speaker or firm belongs to an SMB/boutique consultancy or management advisory firm. Both are reclassified as `UNKNOWN` scope.
- **Audit Decision**: Microsoft 365 Copilot is an established incumbent substitute context for G6, but direct practitioner gap evidence lacks candidate scope attribution for `boutique_consultancies`.

### Lead 3: Recurrence and Discoverable Reachability for Boutique Consultancies
- **Recurrence**:
  - Slide formatting and update frequency are documented across multiple Reddit posts (daily formatting, monthly decks, client theme rework).
  - However, direct captured support that these practitioners belong specifically to SMB/boutique consultancies rather than MBB, Big 4, internal consulting, or corporate FP&A is absent. Under strict candidate discipline, membership in `r/consulting` or generic "client" references do not establish candidate scope. Consequently, in-scope recurrence confidence for `boutique_consultancies` is evaluated as **UNKNOWN**.
- **Reachability**:
  - Record `ev-wf-reachability-apmp-association` documents the Association of Proposal Management Professionals (14,500+ members). However, APMP represents corporate bid, proposal, and RFP managers, not management advisory practices, and was audited as `PARTIALLY_VERIFIED` because association event listings do not establish a contactable prospect surface under the reachability standard.
  - The bounded dataset contains **0 verified reachability channels** specifically targeting boutique consultancies. Reachability remains **UNKNOWN** pending dedicated channel discovery.

### Lead 4: Stated WTP vs. Costly Employee Labor & Software Spend
- **Stated WTP Context**:
  - `ev-wtp-contradiction-manual-template-pushback` (Reddit r/sales): Practitioner recommends paying once for a high-quality customizable template and editing details manually rather than paying a software subscription. Pertains to sales reps and is `OUT_OF_SCOPE`.
- **Candidate Labor Records**:
  - Formatting labor estimates (30%–50% of time, 3 hours daily, 2 hours monthly) are documented in `ev-pain-consulting-thirty-percent-time`, `ev-pain-consulting-daily-formatting-hours`, `ev-wtp-consulting-formatting-time`, and `ev-wf-consulting-monthly-deck-copy-paste`.
  - However, actual performed labor qualifies for G3 only when the target scope is independently established. Because these sources do not establish that the practitioners work in SMB/boutique consultancies (and `ev-wf-consulting-monthly-deck-copy-paste` describes an internal corporate leadership deck), their scope is `UNKNOWN` or `OUT_OF_SCOPE`, making them ineligible for G3.
- **Competitor Price Context (think-cell)**:
  - Vendr benchmark data (`ev-mkt-thinkcell-spend`) documents think-cell per-seat pricing ($19.20–$26.90/user/mo). Its money signal is `competitor_price`, which Policy v2 explicitly disallows for G3, and the Vendr fragment does not establish spend by boutique consultancies. Removed from G3 eligibility; preserved as substitute context for G6.
- **Audit Decision**: 0 in-scope spend or costly labor records qualify for Gate 3 under Policy v2 for `boutique_consultancies`.

---

## 3. Scope Attribution Breakdown (`boutique_consultancies`)

Per Policy v2 single-segment candidate discipline, all 24 evaluated records were mapped against candidate scope `boutique_consultancies`:

- **IN_SCOPE (0 Records)**:
  None. Under strict candidate discipline, IN_SCOPE attribution requires direct captured support that the speaker or organization belongs to an SMB/boutique consultancy or management-advisory firm and performs the relevant client-deck workflow. None of the evaluated records meet this standard directly.

- **UNKNOWN (13 Records)**:
  1. `ev-pain-consulting-thirty-percent-time` (30% workday slide formatting; membership in r/consulting does not establish SMB/boutique firm type or size)
  2. `ev-pain-consulting-client-theme-rework` (30-page deck client recoloring; generic client deliverable reference does not establish boutique firm affiliation)
  3. `ev-pain-consulting-daily-formatting-hours` (3 hours/day formatting per manager stickies; firm type/size unstated)
  4. `ev-pain-llm-thinking-vs-slide-admin` (LLM ideation vs slide admin; general knowledge worker observation on r/consulting)
  5. `ev-wtp-consulting-formatting-time` (50% working time on formatting/reviews; unstated firm size/type)
  6. `ev-wf-consulting-claude-skills-breakage` (Claude skills for PMO/SteerCo decks; firm type/size unstated)
  7. `ev-gap-copilot-firmwide-unusable-decks` (Firmwide Copilot rollout yields unusable decks; generic corporate setting on r/powerpoint)
  8. `ev-gap-copilot-desktop-custom-template-failure` (Copilot desktop custom template failure; generic business user on r/powerpoint)
  9. `ev-pain-gamma-ignores-corporate-templates` (Gamma disregards presentation templates; generic designer on Trustpilot)
  10. `ev-pain-gamma-export-corrupted-content` (Gamma PPTX export corrupts layout; generic business user on Trustpilot)
  11. `ev-gap-beautifulai-export-templates-jeff` (Beautiful.ai export breaks formatting; generic client services user on Trustpilot)
  12. `ev-gap-storydoc-no-pptx-export-nasrullah` (Storydoc lacks native PPTX export; pitch deck creator on Trustpilot)
  13. `ev-pain-pptx-master-slide-corruption` (Pasting slides corrupts master templates; corporate template specialist on r/powerpoint)

- **OUT_OF_SCOPE (11 Records)**:
  1. `ev-pain-faang-no-deck-workflow` (Enterprise FAANG sales AE workflow)
  2. `ev-skp-infosec-procurement-hurdles` (Enterprise CRM security review report; HTTP 502 Bad Gateway / PENDING)
  3. `ev-skp-m365-copilot-ppt-features` (Official Microsoft documentation; G6 substitute context)
  4. `ev-skp-m365-copilot-brand-templates` (Official Microsoft documentation; G6 substitute context)
  5. `ev-skp-m365-copilot-pricing` (Official Microsoft pricing page; G6 substitute context)
  6. `ev-wtp-consulting-thinkcell-pricing` (Vendor list pricing page; competitor pricing context)
  7. `ev-mkt-thinkcell-spend` (Vendr marketplace benchmark; competitor_price signal disallowed for G3; G6 substitute context)
  8. `ev-wf-consulting-monthly-deck-copy-paste` (Recurring monthly 40-slide internal corporate leadership/CFO reporting deck with BI data; internal FP&A)
  9. `ev-wtp-contradiction-manual-template-pushback` (Sales practitioner template pushback)
  10. `ev-pain-outsourced-deck-freelancer` (Freelance presentation designer handling sales decks for sales reps)
  11. `ev-wf-reachability-apmp-association` (Corporate RFP proposal management association)

---

## 4. Potential Gate Eligibility Summary (Input to Stage 1 Judge)

*Note: Per Rules 17–20, the Evidence Auditor does not issue gate verdicts or recommend decisions (PASS, CONDITIONAL PASS, FAIL). The following counts summarize audited records satisfying structural eligibility criteria under Policy v2 for candidate scope `boutique_consultancies`:*

| Gate | Policy v2 Structural Rule | Audited Eligible Count | In-Scope Verified Records | Auditor Observations & Gate Status |
| :--- | :--- | :---: | :--- | :--- |
| **G1: Concrete Pain** | $\ge 5$ independent in-scope VERIFIED records | **0** | None | 0 verified records provide direct captured support for boutique consultancies (4 candidate records reclassified to UNKNOWN). Threshold ($\ge 5$) not met. |
| **G2: Recurrence** | $\ge$ MEDIUM confidence, recurring core job | **0** (UNKNOWN) | None | In-scope recurrence confidence is UNKNOWN because candidates lack direct boutique consultancy attribution. |
| **G3: Existing Spend / WTP** | $\ge 3$ independent VERIFIED spend/labor records | **0** | None | `ev-mkt-thinkcell-spend` disqualified under Policy v2 (competitor_price signal, boutique scope unestablished; kept for G6). Candidate labor records lack target scope attribution (UNKNOWN / OUT_OF_SCOPE). Threshold ($\ge 3$) not met. |
| **G4: Repeatable Gap** | $\ge 3$ independent records, cluster size $\ge 3$ | **0** | None | While 7 verified records document repeatable product gaps in horizontal/AI presentation tools, 0 have direct boutique consultancy attribution (all UNKNOWN). |
| **G5: ICP Reachability** | $\ge$ MEDIUM confidence, concrete channel | **0** (UNKNOWN) | None | `ev-wf-reachability-apmp-association` is PARTIALLY_VERIFIED and covers bid/RFP managers (OUT_OF_SCOPE). 0 contactable channels verified for boutique consultancies. |
| **G6: No Killer Substitute** | Verified substitute context | **4** context | `ev-skp-m365-copilot-ppt-features`, `ev-skp-m365-copilot-brand-templates`, `ev-skp-m365-copilot-pricing`, `ev-mkt-thinkcell-spend` | 4 verified records establish incumbent substitute and pricing context (Microsoft 365 Copilot capabilities/pricing and think-cell spend benchmark). Substitute sufficiency remains for Judge determination. |

---

## 5. Unexamined Evidence Budget Preserved

The remaining 64 records in `ideas/deck-automation/evidence/evidence.jsonl` (commit `3bf758f`) were preserved intact and unexamined. In accordance with Rules 25–31 and bounded reassessment guidelines:
1. No synthetic records were created.
2. The unexamined budget remains available if Stage 2 customer discovery requires broader scope exploration across alternative candidate segments (e.g. sales enablement or commercial real estate).
3. The dataset is sealed and cryptographically verifiable via `snapshot.json`.
