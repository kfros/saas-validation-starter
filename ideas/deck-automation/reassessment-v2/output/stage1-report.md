# Stage 1 Validation Report: Deck Automation (v2 Reassessment)

**Idea ID**: `deck-automation`  
**Idea Name**: Vertical B2B deck / sales-collateral automation  
**Evaluated Scope**: `boutique_consultancies` (Boutique consultancies and management advisory firms preparing bespoke client presentations)  
**Evaluation Date**: 2026-09-11  
**Policy Version**: `v2` (Stage 1 SMB Reassessment Policy per `methodology/stage1-policy.json`)  
**Input Snapshot**: `snap-deck-v2-002` (Sealed evidence snapshot; baseline commit `3bf758f`)  
**Verdict**: **INSUFFICIENT EVIDENCE**  
**Stage 2 Authorized**: **No (`false`)**  
**Recommended Next Action**: `REPAIR_RESEARCH`  

---

## 1. Executive Summary & Verdict Decision

This Stage 1 reassessment evaluates the product hypothesis for `deck-automation` under Policy v2 (SMB Reassessment Policy). Under Policy v2, numeric gates are calibrated to an SMB-appropriate scale to test admission to limited customer discovery interviews ($\le 8$ interviews), rather than MVP build or commercial deployment.

### Verdict: INSUFFICIENT EVIDENCE

Under canonical Policy v2 decision rules:
- **PASS** requires all six gates (G1–G6) to PASS for a single coherent declared candidate scope.
- **CONDITIONAL PASS** requires G1 and G5 to PASS with 0 FAIL gates, all material UNKNOWN gates covered by structured condition objects with `resolution_method: INTERVIEW`, and no material unresolved technical feasibility, API access, or cost constraints.
- **FAIL** requires strong, verified evidence specifically contradicting a core assumption of the evaluated scope.
- **INSUFFICIENT EVIDENCE** applies when gate thresholds are unmet or material assumptions remain unknown without verified contradiction of the assessed scope.

In this reassessment of candidate scope `boutique_consultancies` against sealed snapshot `snap-deck-v2-002`:

1. **Sealed Snapshot Composition**:
   - **0 IN_SCOPE records**: Out of 24 bounded review records, not a single record provides direct, captured proof that the speaker or organization belongs specifically to an SMB/boutique consultancy or management advisory firm.
   - **0 eligible records for Gates G1–G5**: Because candidate scope discipline strictly prohibits cross-segment pooling and requires direct attribution, all 13 candidate records in consulting and presentation tools are classified as `scope_status: UNKNOWN` and `eligible_gates: []`.
   - **4 substitute-context records for Gate G6**: Four verified records establish incumbent substitute and pricing context for Microsoft 365 Copilot and think-cell.

2. **Decision-Integrity Requirements & Separation of Hypotheses from Findings**:
   - Narrative assertions in `audit-summary.md` and `high-impact-review.md`—specifically that boutique consultancies deliver presentation decks as their core billable product, and that Microsoft Copilot or think-cell leave an unserved workflow gap in bespoke consultancy decks—are **unverified hypotheses**, not established factual findings. They are supported by 0 eligible evidence IDs in `snap-deck-v2-002`.
   - **Absence of direct boutique-consultancy attribution represents missing evidence, not market contradiction**. The fact that anonymous Reddit commentators or generic Trustpilot reviewers do not disclose firm headcount or entity type means their evidence is unestablished for this ICP, not that boutique consultancies do not experience the problem.
   - A **FAIL** verdict requires strong, verified evidence contradicting a core assumption specifically for `boutique_consultancies`. Records originating from enterprise FAANG sales reps (`ev-pain-faang-no-deck-workflow`), sales rep template pushback (`ev-wtp-contradiction-manual-template-pushback`), enterprise CRM security audits (`ev-skp-infosec-procurement-hurdles`), generic presentation users, or vendor pricing cannot independently justify a FAIL verdict for boutique consultancies.
   - Because G1 through G5 fail to reach their required thresholds (all counting 0 against thresholds $\ge 5$, $\ge 3$, etc.) and G6 remains unresolved without strong in-scope contradiction, the verdict is strictly **INSUFFICIENT EVIDENCE** rather than FAIL.

3. **Stage 2 Customer Discovery Not Authorized**:
   - Stage 2 customer discovery is not authorized (`stage2_authorized: false`).
   - In accordance with Policy v2 governance and decision-integrity instructions, exploratory interviews are not authorized in this scorecard. A separate Stage 1.5 decision regarding potential targeted research repair or primary discovery will be determined after reviewing completed Judge artifacts.

---

## 2. Gate-by-Gate Evaluation Table (Policy v2)

| Gate | Status | Threshold / Rule | Independent Count | Counted Evidence IDs | Confidence | Contradictory IDs | Material Unknowns |
| :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| **G1: Concrete Pain** | **UNKNOWN** | $\ge 5$ independent in-scope VERIFIED concrete pain signals | 0 | *(none)* | LOW | *(none)* | Headcount and firm-type verification of suffering consultants; whether bespoke deck formatting is a billable deliverable or intentional manual craftsmanship. |
| **G2: Recurrence** | **UNKNOWN** | $\ge$ MEDIUM confidence in recurrence of core job from observed frequency | 0 | *(none)* | LOW | *(none)* | Whether bespoke client presentations recur frequently enough in boutique consultancies to justify a recurring SaaS subscription. |
| **G3: Existing Spend / WTP** | **UNKNOWN** | $\ge 3$ independent VERIFIED actual spend/costly labor records ($\ge 1$ category); stated WTP excluded | 0 | *(none)* | LOW | *(none)* | Actual software budget or contractor spend allocated by boutique consultancies for deck creation; preference for software vs junior analyst labor. |
| **G4: Repeatable Gap** | **UNKNOWN** | $\ge 3$ independent VERIFIED gap signals supporting 1 coherent cluster (size $\ge 3$) | 0 | *(none)* | LOW | *(none)* | Whether corporate template fidelity and PPTX export corruption represent acute workflow blockers for boutique consultancies specifically. |
| **G5: ICP Reachability** | **UNKNOWN** | $\ge$ MEDIUM confidence; concrete role, segment, and acquisition surface | 0 | *(none)* | LOW | *(none)* | Identification of a verified, contactable acquisition channel (directory, association, or search filter) matching founder-led outbound. |
| **G6: No Killer Substitute** | **UNKNOWN** | No low-friction sufficient substitute defeating value proposition; verified context | 4 | `ev-skp-m365-copilot-ppt-features`, `ev-skp-m365-copilot-brand-templates`, `ev-skp-m365-copilot-pricing`, `ev-mkt-thinkcell-spend` | MEDIUM | *(none)* | Whether bundled Microsoft Copilot ($23.50–$30/mo) or think-cell ($19.20–$26.90/mo) satisfy the bespoke deck workflow of boutique consultancies. |

---

## 3. Detailed Gate Analyses

### Gate 1: Concrete Pain
- **Status**: `UNKNOWN`
- **Threshold**: $\ge 5$ independent VERIFIED examples of experienced concrete pain/workarounds for assessed scope (`boutique_consultancies`).
- **Independent Count**: 0
- **Counted Evidence IDs**: `[]`
- **Contradictory Evidence IDs**: `[]`
- **High-Impact Excluded Evidence**:
  - `ev-pain-consulting-thirty-percent-time`: Scope UNKNOWN. Management consultant on r/consulting documents spending ~30% of workday formatting slides, but the source provides no explicit confirmation of firm type (boutique/SMB vs MBB/Big 4/internal corporate).
  - `ev-pain-consulting-client-theme-rework`: Scope UNKNOWN. Consultant on r/consulting describes manual slide-by-slide recoloring of a 30-page deck to match client brand themes, but generic client deliverable reference does not establish boutique firm affiliation.
  - `ev-pain-consulting-daily-formatting-hours`: Scope UNKNOWN. Consultant on r/consulting reports spending 3+ hours daily formatting slides per manager review stickies, but firm type and headcount are unstated.
  - `ev-pain-llm-thinking-vs-slide-admin`: Scope UNKNOWN. Knowledge worker on r/consulting observes that LLMs assist with ideation but not slide formatting admin; source does not identify a boutique consultancy practitioner.
  - `ev-pain-faang-no-deck-workflow`: Scope OUT_OF_SCOPE. FAANG enterprise AE describes bypassing sales decks for live platform demos; pertains to enterprise tech sales, not management consultancies, and cannot serve as contradiction for this scope.
- **Analysis**:
  While acute formatting friction is documented on r/consulting (spending 30% of workdays or 3+ hours daily tweaking slides), zero records establish that the speakers belong to boutique consultancies or management advisory firms. Headcount and entity discipline prevent treating general consulting chatter as verified evidence for boutique consultancies. Absence of attribution is missing evidence, not contradiction. Threshold ($\ge 5$) is unmet.

### Gate 2: Recurrence
- **Status**: `UNKNOWN`
- **Threshold**: $\ge$ MEDIUM confidence that the core job recurs with sufficient frequency for a B2B SaaS subscription.
- **Independent Count**: 0
- **Counted Evidence IDs**: `[]`
- **Contradictory Evidence IDs**: `[]`
- **High-Impact Excluded Evidence**:
  - `ev-pain-consulting-thirty-percent-time`: Scope UNKNOWN. Daily slide formatting cadence observed, but target scope attribution is unverified.
  - `ev-pain-consulting-daily-formatting-hours`: Scope UNKNOWN. Daily 3+ hours formatting cadence observed, but firm size/type is unstated.
  - `ev-wf-consulting-monthly-deck-copy-paste`: Scope OUT_OF_SCOPE. Monthly 40-slide reporting deck describes internal corporate FP&A / CFO reporting, not bespoke client deliverables by a boutique consultancy.
  - `ev-wf-consulting-claude-skills-breakage`: Scope UNKNOWN. Recurring PMO/SteerCo deck assembly observed, but consultancy firm type/size is unstated.
- **Analysis**:
  Recurrence is documented for generic management consulting analysts and corporate reporting teams, but zero in-scope records verify recurring cadence for the target boutique consultancy ICP. Gate 2 remains UNKNOWN.

### Gate 3: Existing Spend / WTP
- **Status**: `UNKNOWN`
- **Threshold**: $\ge 3$ independent VERIFIED examples of actual target-job spending or actually performed costly work from $\ge 1$ eligible category; stated WTP excluded from numeric count.
- **Independent Count**: 0
- **Counted Evidence IDs**: `[]`
- **Contradictory Evidence IDs**: `[]`
- **Breakdown by Category**: `{}`
- **High-Impact Excluded Evidence**:
  - `ev-wtp-consulting-formatting-time`: Scope UNKNOWN. Consultant estimates 50% working time spent on formatting and reviews, but firm size and type are unverified.
  - `ev-pain-consulting-thirty-percent-time`: Scope UNKNOWN. 30% workday formatting labor described, but firm affiliation is unverified.
  - `ev-pain-consulting-daily-formatting-hours`: Scope UNKNOWN. 3 hours daily formatting labor described, but firm affiliation is unverified.
  - `ev-mkt-thinkcell-spend`: Scope OUT_OF_SCOPE. Vendr procurement benchmark reflects `competitor_price`, explicitly disallowed for G3 under Policy v2; preserved as substitute context for G6.
  - `ev-wtp-consulting-thinkcell-pricing`: Scope OUT_OF_SCOPE and PARTIALLY_VERIFIED. Vendor list price (23.90 EUR/mo Suite) reflects competitor pricing context, not buyer-side spend.
  - `ev-wtp-contradiction-manual-template-pushback`: Scope OUT_OF_SCOPE. Sales practitioner template pushback pertains to enterprise sales rather than boutique consultancies.
  - `ev-pain-outsourced-deck-freelancer`: Scope OUT_OF_SCOPE. Freelance designer hired by sales reps, not boutique consultancies.
- **Analysis**:
  Under Policy v2 Gate 3 rules, competitor software prices (`competitor_price`) are disqualified from serving as spend signals, and candidate labor records qualify only when the target candidate scope is independently established. Because candidate consultant labor records lack verified boutique consultancy scope, eligible in-scope count is 0. Threshold ($\ge 3$) is unmet.

### Gate 4: Repeatable Solution Gap
- **Status**: `UNKNOWN`
- **Threshold**: $\ge 3$ independent VERIFIED examples supporting one coherent, repeated gap/workaround cluster with $\ge 3$ members.
- **Independent Count**: 0
- **Counted Evidence IDs**: `[]`
- **Contradictory Evidence IDs**: `[]`
- **Clusters**: `{}`
- **High-Impact Excluded Evidence**:
  - `ev-gap-copilot-desktop-custom-template-failure`: Scope UNKNOWN. Desktop Copilot custom template failure verified, but speaker firm affiliation is unstated.
  - `ev-pain-gamma-ignores-corporate-templates`: Scope UNKNOWN. Gamma template disregard verified, but author is generic presentation designer.
  - `ev-pain-pptx-master-slide-corruption`: Scope UNKNOWN. Duplicate master slide corruption verified, but author is generic corporate template specialist.
  - `ev-pain-gamma-export-corrupted-content`: Scope UNKNOWN. PPTX export layout breakage verified, but user firm affiliation is unstated.
  - `ev-gap-beautifulai-export-templates-jeff`: Scope UNKNOWN. Beautiful.ai export formatting breakage verified, but firm affiliation is unstated.
  - `ev-gap-storydoc-no-pptx-export-nasrullah`: Scope UNKNOWN. Storydoc lack of PPTX download verified, but speaker is individual pitch deck creator.
  - `ev-gap-copilot-firmwide-unusable-decks`: Scope UNKNOWN. Firmwide Copilot unusable decks verified, but generic enterprise corporate setting.
- **Analysis**:
  Seven verified records document genuine technical and workflow shortcomings across AI and presentation software (template non-compliance, layout distortion, export corruption). However, zero records possess direct attribution to boutique consultancies. In-scope count is 0. Threshold ($\ge 3$) is unmet.

### Gate 5: ICP Reachability
- **Status**: `UNKNOWN`
- **Threshold**: $\ge$ MEDIUM confidence that relevant buyers can be found through a concrete acquisition surface.
- **Independent Count**: 0
- **Counted Evidence IDs**: `[]`
- **Contradictory Evidence IDs**: `[]`
- **High-Impact Excluded Evidence**:
  - `ev-wf-reachability-apmp-association`: Status PARTIALLY_VERIFIED and Scope OUT_OF_SCOPE. Association of Proposal Management Professionals (APMP) represents corporate bid, proposal, and RFP managers, not boutique management consultancies, and an association homepage does not constitute a contactable prospect surface.
  - `ev-skp-infosec-procurement-hurdles`: Status PENDING and Scope OUT_OF_SCOPE. Inaccessible source (HTTP 502 Bad Gateway); pertains to enterprise CRM integrations rather than boutique consultancies.
- **Analysis**:
  The bounded dataset contains 0 verified reachability channels specifically targeting boutique consultancies. Confidence is LOW; Gate 5 remains UNKNOWN.

### Gate 6: No Killer Substitute
- **Status**: `UNKNOWN`
- **Threshold**: No evidenced sufficient substitute defeating the value proposition for the assessed scope. Requires verified substitute assessment context.
- **Independent Count**: 4 (deduplicated by independence key)
- **Counted Evidence IDs**:
  - `ev-skp-m365-copilot-ppt-features` (independence_key: `msft-copilot-ppt-docs`): Official Microsoft documentation confirms Copilot in PowerPoint generates presentations from referenced Word documents using styles and headings.
  - `ev-skp-m365-copilot-brand-templates` (independence_key: `msft-copilot-brand-kit-docs`): Official Microsoft documentation confirms Copilot in PowerPoint supports corporate `.potx` presentation templates and Brand Kits.
  - `ev-skp-m365-copilot-pricing` (independence_key: `msft-copilot-pricing-official`): Official Microsoft pricing page confirms Copilot is priced as an add-on at $23.50–$30/user/month.
  - `ev-mkt-thinkcell-spend` (independence_key: `thinkcell-powerpoint-annual-spend`): Vendr procurement marketplace benchmark confirms think-cell volume tier pricing at $19.20–$26.90/user/month ($260–$325/yr) for PowerPoint chart automation.
- **Contradictory Evidence IDs**: `[]`
- **Breakdown by Category**:
  - `Bundled Incumbent Office AI`: `ev-skp-m365-copilot-ppt-features`, `ev-skp-m365-copilot-brand-templates`, `ev-skp-m365-copilot-pricing`
  - `PowerPoint Chart Automation`: `ev-mkt-thinkcell-spend`
- **High-Impact Excluded Evidence**:
  - `ev-wtp-consulting-thinkcell-pricing`: Status PARTIALLY_VERIFIED and OUT_OF_SCOPE. Vendor list price (23.90 EUR/mo Suite); preserved as supporting pricing context.
  - `ev-wf-consulting-claude-skills-breakage`: Scope UNKNOWN. Describes using Claude skills for PMO/SteerCo decks due to fragile think-cell links, but firm type/size is unverified.
- **Confidence**: `MEDIUM`
- **Analysis**:
  Gate 6 cannot PASS because Microsoft 365 Copilot directly targets presentation generation and corporate templates at an aggressive incumbent price ($23.50–$30/mo) well below the founder's $100/mo target ARPU, while think-cell is entrenched for chart automation.
  Conversely, Gate 6 cannot FAIL because narrative claims that Copilot or think-cell are sufficient or insufficient for boutique consultancies are unverified hypotheses: the dataset lacks direct in-scope practitioner evidence testing these tools against boutique consultancy client deliverables. Because substitute sufficiency remains materially unresolved, Gate 6 is evaluated as `UNKNOWN`.

---

## 4. Scope Integrity & Forensic Review

Candidate scope `boutique_consultancies` is defined in `hypothesis.yaml`:
> "Boutique consultancies and management advisory firms preparing bespoke client presentations."

Under single-segment candidate discipline:
1. **Candidate Scope Independence**: Candidate segments must be evaluated individually without cross-segment pooling. Pain from enterprise sales reps, spend from commercial real estate, reachability from bid managers, and software gaps from horizontal tool reviews cannot be aggregated to manufacture a passing verdict for boutique consultancies.
2. **Strict Headcount & Entity Attribution**: References to "consulting", "clients", "manager notes", or participation in `r/consulting` do not establish affiliation with an SMB/boutique consultancy as opposed to MBB (McKinsey, BCG, Bain), Big 4 (Deloitte, PwC, EY, KPMG), or internal corporate strategy teams.
3. **Absence of Evidence is Not Contradiction**: The absence of verified in-scope records is a data availability gap, not empirical proof that boutique consultancies do not make decks or do not experience pain.
4. **Out-of-Scope Evidence Cannot Justify FAIL**: Enterprise software AE evidence (FAANG reps abandoning decks for live software demos) and sales rep master template preferences pertain strictly to B2B SaaS sales workflows, where interactive product demos replace narrative slide decks. These records cannot be transposed to management consulting, where narrative slide decks remain a primary client deliverable.

---

## 5. Retrospective Verdict Comparison (v1 vs v2)

| Dimension | Historical v1 Evaluation | Reassessment v2 Evaluation | Primary Driver of Difference |
| :--- | :---: | :---: | :--- |
| **Target Scope** | B2B SaaS Account Executives / Broad | **`boutique_consultancies`** | Focused single-segment candidate evaluation without cross-segment pooling. |
| **G1: Concrete Pain** | FAIL (6 signals, threshold $\ge 20$) | **UNKNOWN (0 signals, threshold $\ge 5$)** | Scope discipline: candidate consulting records lack verified boutique firm status; FAANG AE record is OUT_OF_SCOPE. |
| **G2: Recurrence** | FAIL (15 signals, conf: LOW) | **UNKNOWN (0 signals, conf: LOW)** | Scope discipline: recurrence observed in consulting threads lacks verified boutique consultancy scope. |
| **G3: Existing Spend / WTP** | PASS (16 signals, threshold $\ge 5$) | **UNKNOWN (0 signals, threshold $\ge 3$)** | Policy & forensic review: think-cell spend disqualified under Policy v2 (`competitor_price`); candidate labor unverified. |
| **G4: Repeatable Gap** | PASS (10 signals, threshold $\ge 10$) | **UNKNOWN (0 signals, threshold $\ge 3$)** | Scope discipline: 7 verified tool gaps lack in-scope boutique consultancy attribution. |
| **G5: Reachability** | FAIL (0 signals, conf: LOW) | **UNKNOWN (0 signals, conf: LOW)** | Maintained: 0 verified acquisition channels for boutique consultancies (APMP is OUT_OF_SCOPE). |
| **G6: No Killer Substitute** | FAIL (9 signals, conf: HIGH) | **UNKNOWN (4 signals, conf: MEDIUM)** | Policy v2 discipline: substitute sufficiency for boutique consultancies is an unresolved hypothesis, not a proven contradiction. |
| **Overall Verdict** | **FAIL** | **INSUFFICIENT EVIDENCE** | Elimination of cross-scope contradiction; absence of in-scope evidence mandates INSUFFICIENT EVIDENCE rather than FAIL. |
| **Stage 2 Authorized** | False | False | Unchanged. |

### Decomposition of Reassessment Effects

1. **Effect of Policy Threshold Changes**:
   Under Policy v2, numeric admission thresholds were lowered (G1: $20 \to 5$; G3: $5 \to 3$; G4: $10 \to 3$) to reflect SMB discovery realities. However, lower numeric thresholds cannot compensate for 0 in-scope records.
2. **Effect of Evidence Corrections & Forensic Review (Leads 1–4)**:
   - Erroneous currency values on labor records (`ev-pain-consulting-daily-formatting-hours`, `ev-wf-consulting-monthly-deck-copy-paste`) were repaired from currency ($3, $2) to null, properly classifying them as unpriced `employee_time`.
   - `ev-mkt-thinkcell-spend` was disqualified from Gate 3 because its money signal is `competitor_price` (disallowed under Policy v2) and its marketplace benchmark reflects aggregated corporate procurement rather than boutique consultancy spend. It is preserved strictly as substitute context for G6.
   - `ev-skp-infosec-procurement-hurdles` returned HTTP 502 Bad Gateway during re-inspection and was classified as `PENDING`, preventing fresh verification.
3. **Effect of Single-Segment Scope Discipline**:
   In historical v1, disparate evidence from sales reps, real estate brokers, agencies, and consultants was pooled into a single scorecard. Under Policy v2, `boutique_consultancies` is assessed strictly on its own merits. The 24 reviewed records yield 0 IN_SCOPE records (13 UNKNOWN, 11 OUT_OF_SCOPE).
4. **Decision-Integrity Rationale (FAIL vs. INSUFFICIENT EVIDENCE)**:
   In historical v1, the broad hypothesis received a FAIL verdict because its primary target ICP (B2B SaaS account executives) was directly contradicted by sales reps abandoning decks for live software demos. For `boutique_consultancies`, however, no such contradiction exists in the evidence. The statements asserting that consultancies do not need automation, or that Copilot already solves their workflow, are unverified. Under Policy v2, absence of evidence is not contradiction; the correct verdict is **INSUFFICIENT EVIDENCE**.

---

## 6. Next Steps & Stage 1.5 Governance

- **Stage 2 Status**: Not authorized (`stage2_authorized: false`).
- **Recommended Next Action**: `REPAIR_RESEARCH`.
- **Preserved Baseline Budget**: 64 baseline records in `ideas/deck-automation/evidence/evidence.jsonl` (at commit `3bf758f`) remain unexamined.
- **Stage 1.5 Governance**: Any decision to authorize customer discovery interviews, conduct targeted research repair, or explore alternative candidate segments (such as sales enablement or commercial real estate) will be made separately by leadership after reviewing these Stage 1 artifacts.
