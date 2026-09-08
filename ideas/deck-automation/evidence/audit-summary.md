# Stage 1 Evidence Audit Summary — Deck Automation

**Audit Date**: 2026-09-07  
**Audited Target**: `ideas/deck-automation`  
**Audited Artifact**: `ideas/deck-automation/evidence/evidence.jsonl`  
**Total Records Audited**: 88  

---

## 1. Executive Status Overview

| Audit Status | Count | Percentage | Description |
| :--- | :---: | :---: | :--- |
| **VERIFIED** | **52** | 59.1% | Page directly supports all material claims, source identity, and semantic classification. |
| **PARTIALLY_VERIFIED** | **12** | 13.6% | Page supports a core fact, but a material field, amount, recurrence, or attribution is overstated/mismatched. |
| **REJECTED** | **24** | 27.3% | Broken URL (404/DNS), duplicate claim, non-atomic bundle, or unsupported observation. |
| **PENDING** | **0** | 0.0% | No records blocked by tool failure; all available canonical URLs were inspected via browser subagent. |
| **Total** | **88** | 100.0% | Complete raw dataset evaluated. |

---

## 2. Audit Breakdown by Field & Dimension

### 2.1 Status by Semantic Type

| Semantic Type | VERIFIED | PARTIALLY_VERIFIED | REJECTED | Total Raw |
| :--- | :---: | :---: | :---: | :---: |
| **gap** | 10 | 0 | 7 | 17 |
| **market** | 4 | 3 | 1 | 8 |
| **pain** | 7 | 2 | 0 | 9 |
| **reachability** | 0 | 1 | 0 | 1 |
| **risk** | 3 | 0 | 0 | 3 |
| **substitute** | 9 | 0 | 2 | 11 |
| **workflow** | 11 | 3 | 9 | 23 |
| **wtp** | 8 | 3 | 5 | 16 |
| **Total** | **52** | **12** | **24** | **88** |

### 2.2 Status by Source Tier

| Source Tier | VERIFIED | PARTIALLY_VERIFIED | REJECTED | Total |
| :--- | :---: | :---: | :---: | :---: |
| **Tier A** (Official docs, pricing, first-hand reviews, practitioner posts) | 46 | 11 | 21 | 78 |
| **Tier B** (Procurement reports, specialized aggregators, secondary threads) | 6 | 1 | 3 | 10 |
| **Tier C** (Unverified blogs, general SEO) | 0 | 0 | 0 | 0 |
| **Total** | **52** | **12** | **24** | **88** |

### 2.3 Status by Target ICP Attribution

| Target ICP Segment | VERIFIED | PARTIALLY_VERIFIED | REJECTED | Total |
| :--- | :---: | :---: | :---: | :---: |
| **B2B SaaS account executives / sales reps** | 10 | 2 | 5 | 17 |
| **Commercial real-estate (CRE) teams / brokers** | 5 | 2 | 3 | 10 |
| **Boutique consultancies / Management consultants** | 7 | 3 | 2 | 12 |
| **Sales enablement teams / RevOps** | 7 | 1 | 4 | 12 |
| **Marketing & creative agencies** | 4 | 0 | 0 | 4 |
| **IT Managed Service Providers (MSPs)** | 1 | 0 | 0 | 1 |
| **General / Presentation creators / Other** | 18 | 4 | 10 | 32 |
| **Total** | **52** | **12** | **24** | **88** |

### 2.4 Status by Money Signal Classification

| Money Signal | VERIFIED | PARTIALLY_VERIFIED | REJECTED | Total |
| :--- | :---: | :---: | :---: | :---: |
| **employee_time** | 9 | 3 | 0 | 12 |
| **contractor_spend** | 4 | 0 | 1 | 5 |
| **saas_spend** | 3 | 0 | 0 | 3 |
| **dedicated_role** | 1 | 1 | 2 | 4 |
| **actual_purchase** | 1 | 0 | 0 | 1 |
| **stated_wtp** | 1 | 0 | 0 | 1 |
| **competitor_price** | 8 | 4 | 3 | 15 |
| *None / Unspecified* | 25 | 4 | 18 | 47 |
| **Total** | **52** | **12** | **24** | **88** |

---

## 3. Duplicate Analysis and Groupings

### 3.1 Exact Duplicate Claims Rejected
Under evidence audit rules, when multiple raw records capture the exact same user claim, quote, or pricing statement from the same source, one canonical record is retained and duplicates are marked `REJECTED`:

1. **r/sales 148jm0y (theflatlanderz QBR time drain)**:
   - Canonical retained: `ev-pain-sales-qbr-hours-editing` (`VERIFIED`)
   - Duplicate rejected: `ev-wf-saas-am-qbr-hours-editing` (`REJECTED`)
2. **r/sales 148jm0y (elguiri 100-slide master template workaround)**:
   - Canonical retained: `ev-pain-master-template-workaround` (`VERIFIED`)
   - Duplicate rejected: `ev-wf-saas-ae-master-slide-workaround` (`REJECTED`)
3. **r/sales 148jm0y (imfatterthanyou anti-deck sentiment)**:
   - Canonical retained: `ev-pain-rep-disdain-for-decks` (`VERIFIED`)
   - Duplicate rejected: `ev-wf-saas-ae-conversational-rejection` (`REJECTED`)
4. **Buildout Official Pricing ($125/user/month)**:
   - Primary retained: `ev-wtp-cre-buildout-pricing` (`PARTIALLY_VERIFIED` — competitor pricing context)
   - Duplicate rejected: `ev-skp-buildout-pricing` (`REJECTED`)
5. **Plus AI Pricing Tier ($25-$30/user/month)**:
   - Primary retained: `ev-wtp-saas-plusai-pricing` (`PARTIALLY_VERIFIED` — competitor pricing context)
   - Duplicate rejected: `ev-skp-plusai-pricing-tier` (`REJECTED`)

### 3.2 Non-Atomic Bundles Rejected
1. **`ev-skp-cre-practitioner-om-spending`**: Bundled two distinct comments (`AgTown05` fee quote and `SF_Lady` lender evaluation) from `r/CommercialRealEstate/comments/jvoajm/` that were already captured individually in `ev-wtp-cre-om-freelance-spend` and `ev-wtp-contradiction-cre-om-skepticism`. Marked `REJECTED`.
2. **`ev-skp-consulting-slide-formatting-synthesis`**: Bundled quotes and findings from two separate users (`Specialist_Golf8133` and `Maleficent-Drive4056`) in `r/consulting/comments/1seychs/` that were already captured individually in `ev-wtp-consulting-formatting-time` and `ev-pain-llm-thinking-vs-slide-admin`. Marked `REJECTED`.

### 3.3 Multi-Record Independent Canonical URLs
Where multiple records derive from the same canonical URL but represent distinct atomic observations, distinct users, or distinct plans, records are maintained with shared or specific independence keys:
- `https://www.trustpilot.com/review/gamma.app?page=4`: 5 distinct user reviews (`Alexandre Tranchant`, `Jazz`, `Dan Twing`, `Tom Burke`, `Vicky GU`). All 5 `VERIFIED` with unique reviewer keys.
- `https://www.reddit.com/r/consulting/comments/1jv5dwk/`: 3 distinct users (`VisualTrade7019`, `Jumpy_Biscotti3612`, `NoogatAI`).
- `https://www.seismic.com/explainers/the-sales-content-automation-guide/`: 2 distinct aspects (LiveDocs dynamic assembly vs. brand governance restriction). Both `VERIFIED`.

---

## 4. Inaccessible and Blocked Sources (REJECTED)

All 24 rejected records were rejected for verifiable source-side reasons rather than tool limitations:

### 4.1 Broken Official URLs (HTTP 404 / Decommissioned)
- `https://help.gamma.app/en/articles/6908354-exporting-to-powerpoint-or-pdf` (`ev-mkt-gamma-pptx-export`): 404 Not Found.
- `https://support.beautiful.ai/hc/en-us/articles/360037837772-Export-to-PowerPoint` (`ev-mkt-beautifulai-export`): 404 Not Found.
- `https://support.plusdocs.com` (`ev-mkt-plusai-template-gap`): DNS failure (`ERR_NAME_NOT_RESOLVED`).
- `https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8637-94eb3d486a3d` (`ev-mkt-copilot-single-file-limitation`): 404 Not Found.
- `https://pitch.com/features/export-powerpoint` (`ev-mkt-pitch-export-gap`): 404 Not Found.
- `https://storydoc.com/help/export-formats` (`ev-mkt-storydoc-format-barrier`): 404 Not Found.
- `https://www.upslide.net/en/features/powerpoint/` (`ev-mkt-upslide-positioning`): 404 Not Found upon redirect.
- `https://highspot.com/capabilities/content-management/autodocs/` (`ev-mkt-highspot-autodocs`): 404 Not Found.
- `https://seismic.com/product/livedocs/` (`ev-mkt-seismic-livedocs`): 404 Not Found.
- `https://www.canva.com/help/download-save-share-designs/` (`ev-mkt-canva-pptx-breakage`): 404 Not Found.
- `https://venturebeat.com/ai/tome-shuts-down-presentation-tool-pivots-to-lightfield-crm/` (`ev-mkt-tome-market-failure`): 404 Not Found.
- `https://exchange.seismic.com/apps/livedocs-automation` (`ev-skp-seismic-appexchange-pricing`): 404 Not Found.

### 4.2 Expired Job Postings & Wrong Product IDs
- `https://www.linkedin.com/jobs/view/marketing-specialist-at-cushman-wakefield` (`ev-wf-cre-marketing-coordinator-role`): LinkedIn job requisition closed/unresolved.
- `https://spacecrew.com/careers/sales-enablement-manager-spacex-starlink` (`ev-wf-enablement-governance-translation`): 404 Expired posting.
- `https://www.capterra.com/p/150033/think-cell/` (`ev-skp-consulting-thinkcell-standard`): Product ID 150033 on Capterra maps to "Edgagement", not think-cell.

### 4.3 Unsupported / Overstated Forum Comments
- `ev-pain-dedicated-sales-analyst-deck-role`: Brief forum response ("Sales analyst. I'm a business development analyst and do alot of research") does not support full-time dedicated deck creation role or salary spend.
- `ev-pain-sales-enablement-deck-offloading`: Four-word comment ("analyst. And maybe also enablement") cannot support claims of shielding reps from non-selling overhead.

---

## 5. Potential Gate Eligibility Metrics

*(Audit metrics only. No PASS/FAIL decision is declared. The Stage 1 Judge reproduces verdict decisions from VERIFIED records only.)*

### Gate 1: Concrete Pain Signals
- **Threshold Target**: ≥ 20 VERIFIED independent concrete pain signals (≥ 10 from core ICPs).
- **Audit Findings**:
  - **VERIFIED Pain Records**: **7** records.
  - **Unique Independence Keys**: **7** keys.
  - Core ICP Breakdown:
    - B2B SaaS Account Executives / Sales: 2 (`ev-pain-sales-qbr-hours-editing`, `ev-pain-rep-disdain-for-decks`)
    - Management Consultants: 2 (`ev-pain-consulting-thirty-percent-time`, `ev-pain-consulting-client-theme-rework`)
    - Corporate Presentation Creators / Sales Enablement: 1 (`ev-pain-pptx-master-slide-corruption`)
    - RevOps / Sales Operations: 1 (`ev-pain-revops-sfdc-to-slides-manual-drain`)
    - Marketing Agencies: 1 (`ev-wf-agency-rfp-resource-drain`)
  - *Gap to G1 Target*: 7 verified signals vs. 20 target.

### Gate 2: Recurrence
- **Confidence Requirement**: At least MEDIUM confidence that core workflow recurs regularly.
- **Audit Findings**:
  - **VERIFIED Recurring Records**: **49** records (49 unique independence keys).
  - Recurrence breakdown across VERIFIED records:
    - `per_opportunity`: 23 records (deal-by-deal pitch preparation and client proposals)
    - `monthly`: 12 records (monthly leadership/PMO reporting and billing cadences)
    - `daily`: 3 records (daily slide formatting and template production)
    - `weekly`: 3 records (weekly review decks and slide maintenance)
    - `quarterly`: 2 records (recurring QBR deck customization)
    - `per_client`: 2 records (client brand theme alignment)
    - `ad_hoc`: 4 records (situational deck adjustments)
    - `one_time`: 3 records (security reviews, onboarding decks)

### Gate 3: Existing Spend / WTP
- **Threshold Target**: ≥ 5 VERIFIED money signals across ≥ 2 distinct spend categories (excluding competitor pricing pages alone).
- **Audit Findings**:
  - **VERIFIED Buyer/Actual Money Records**: **19** records (19 unique independence keys).
  - **Distinct Spend Categories Represented**: **6 categories**:
    1. `contractor_spend` (4 signals): `ev-wtp-cre-om-freelance-spend` ($100/listing + $1,000 template), `ev-wtp-startups-upwork-deck-spend` ($150 on Upwork), `ev-pain-outsourced-deck-freelancer` (10-20 hrs/mo), `ev-wf-agency-proposal-slides-assistant`.
    2. `saas_spend` (3 signals): `ev-wtp-sales-highspot-enterprise-use` (3-year SAS Institute deployment), `ev-gap-copilot-firmwide-unusable-decks` (firmwide Microsoft Copilot rollout), `ev-wf-agency-interactive-qwilr-substitute` (Qwilr deployment).
    3. `employee_time` (9 signals): `ev-pain-sales-qbr-hours-editing`, `ev-pain-consulting-thirty-percent-time` (30% workday), `ev-pain-consulting-client-theme-rework`, `ev-gap-beautifulai-export-templates-jeff` (3x time), `ev-pain-revops-sfdc-to-slides-manual-drain`, `ev-wtp-consulting-formatting-time` (50% time), `ev-wf-cre-assembly-line-redlining`, `ev-wf-agency-rfp-resource-drain`, `ev-wf-msp-qbr-multi-tool-drain`.
    4. `dedicated_role` (1 signal): `ev-wf-cre-designer-indesign-bottleneck` (full-time in-house InDesign OM designer).
    5. `actual_purchase` (1 signal): `ev-gap-storydoc-no-pptx-export-nasrullah` (1-month paid subscription for pitch deck).
    6. `stated_wtp` (1 signal): `ev-wtp-contradiction-manual-template-pushback` (preference to pay once for master template).
  - *Competitor Price Context (VERIFIED)*: 8 records (`ev-mkt-plusai-pricing`, `ev-mkt-m365-copilot-pricing`, `ev-mkt-highspot-contract-floor`, `ev-mkt-thinkcell-spend`, `ev-skp-highspot-pricing-procurement`, `ev-skp-m365-copilot-pricing`, `ev-mkt-qwilr-pricing-substitute`, `ev-mkt-templafy-capabilities`).

### Gate 4: Repeatable Gap in Existing Solutions
- **Threshold Target**: ≥ 10 VERIFIED records clustering around repeatable solution gaps.
- **Audit Findings**:
  - **VERIFIED Gap Records**: **10** records (10 unique independence keys).
  - Identifiable Gap Clusters:
    1. *PPTX Export Fidelity & Content Corruption* (4 records): `ev-pain-gamma-export-corrupted-content`, `ev-gap-beautifulai-export-templates-jeff`, `ev-gap-storydoc-no-pptx-export-nasrullah`, `ev-pain-gamma-import-dropped-data`.
    2. *Template Non-Compliance & Inability to Enforce Brand Kits* (3 records): `ev-pain-gamma-ignores-corporate-templates`, `ev-gap-copilot-desktop-custom-template-failure`, `ev-pain-gamma-rigid-layout-distortion`.
    3. *Low AI Output Quality & Instruction Deviation* (2 records): `ev-gap-copilot-firmwide-unusable-decks`, `ev-gap-pitch-ai-ignores-structure-layout`.
    4. *Administrative Formatting Disconnect* (1 record): `ev-pain-llm-thinking-vs-slide-admin`.

### Gate 5: ICP Reachability
- **Threshold Target**: Identifiable roles, company segments, and discoverable/contactable market surface.
- **Audit Findings**:
  - **VERIFIED Reachability Records**: **0** records.
  - *Note*: `ev-wf-reachability-apmp-association` was downgraded to `PARTIALLY_VERIFIED` because an association event page and membership count alone does not provide a contactable prospect surface under the reachability standard.

### Gate 6: Killer Substitute Analysis
- **Threshold Target**: No low-friction substitute that solves the workflow at a price that destroys planned value proposition.
- **Audit Findings**:
  - **VERIFIED Substitute Records**: **9** records (9 unique independence keys).
  - Major Direct & Adjacent Substitutes Verified:
    1. *Microsoft 365 Copilot* (`ev-skp-m365-copilot-ppt-features`, `ev-skp-m365-copilot-brand-templates`, `ev-skp-m365-copilot-pricing`): Directly bundled in PowerPoint at $23.50–$30/user/mo, generates decks from Word docs, and learns .potx templates/Brand Kits.
    2. *Highspot AutoDocs & Seismic LiveDocs* (`ev-skp-seismic-livedocs-automation`, `ev-skp-highspot-pricing-procurement`): Solve end-to-end dynamic template population from Salesforce/Dynamics in mid-market and enterprise ($45–$65/user/mo per seat, $60k median contract).
    3. *Buildout Showcase* (`ev-skp-buildout-cre-suite`): Solves automated OM and proposal creation from property data for 50,000+ CRE brokers at $125/user/mo.
    4. *Web Proposal Platforms (Qwilr, Storydoc)* (`ev-mkt-storydoc-substitute`, `ev-mkt-qwilr-pricing-substitute`, `ev-wf-agency-interactive-qwilr-substitute`): Replace PowerPoint entirely with dynamic, tracked web links.
