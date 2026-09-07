# Stage 1 Evidence Audit Summary — Vertical B2B Deck / Sales-Collateral Automation

**Idea ID:** `deck-automation`  
**Audit Date:** 2026-09-06  
**Auditor:** Evidence Auditor Agent  
**Methodology Rules Applied:** `methodology/evidence-schema.json`, `methodology/evidence-standard.md`, `methodology/stage1-gates.md`, `validation-rules.md`  
**Decision Status:** Canonical Audit Completed (No PASS/FAIL Issued)

---

## 1. Executive Summary & Audit Metrics

The Stage 1 evidence audit reviewed **88 raw evidence records** collected across five independent research streams (`market-research`, `pain-mining`, `skeptic-research`, `workflow-mapping`, and `wtp-research`).

Every record was audited for schema conformity, URL validity, source accessibility, factual fidelity, independence of claims, recency, and accurate field attribution.

### Overall Status Breakdown

| Audit Status | Record Count | Percentage | Definition / Disposition |
| :--- | :---: | :---: | :--- |
| **`VERIFIED`** | **66** | **75.0%** | Source inspectable, supports the material observation, accurate attribution, unique independent claim. |
| **`PARTIALLY_VERIFIED`** | **9** | **10.2%** | Core observation supported, but specific fields (e.g. money amount unit errors, vendor ARR, unverified pricing, generic search URL, or low recency) contain defects. |
| **`REJECTED`** | **13** | **14.8%** | Cross-agent duplicates without independent value (7), untraceable root URLs lacking post/article paths (5), or severe money misattribution (1). |
| **Total** | **88** | **100.0%** | **Full raw evidence corpus audited** |

> [!IMPORTANT]
> In strict compliance with Workspace Rule 20 and Stage 1 Gate Methodology, **the Stage 1 Judge may use ONLY the 66 records marked `VERIFIED`**. The 9 `PARTIALLY_VERIFIED` and 13 `REJECTED` records are cataloged here and in `high-impact-review.md` for transparency and human spot-checking, but must not carry Gate thresholds.

---

## 2. Rejection Analysis (13 Records)

The 13 rejected records fall into three distinct failure categories:

### Category A: Cross-Agent Duplicates Without Independent Value (7 records)
Multiple agents inspected the identical source URL, thread, or comment, producing redundant records that repeat the same underlying claim under different record IDs. Counting these would violate Rule 7 ("Do not count duplicated, syndicated, or repeated claims as independent evidence").

1. **`ev-skp-seismic-livedocs`** (skeptic-research)
   * *URL:* `https://developer.seismic.com`
   * *Reason:* Redundant duplicate of `ev-mkt-seismic-livedocs` (`https://seismic.com/product/livedocs/`). Cites a generic developer portal root to document the same LiveDocs PPT plugin capability already verified from the canonical product page.
2. **`ev-skp-highspot-salesforce`** (skeptic-research)
   * *URL:* `https://www.highspot.com`
   * *Reason:* Redundant duplicate of `ev-mkt-highspot-autodocs` (`https://highspot.com/capabilities/content-management/autodocs/`). Cites the root homepage to assert Highspot dynamic templates, which is already verified from the primary AutoDocs capability page.
3. **`ev-skp-m365-copilot-pricing-anchor`** (skeptic-research)
   * *URL:* `https://www.microsoft.com/en-us/microsoft-365/enterprise/copilot-for-microsoft-365`
   * *Reason:* Exact duplicate of `ev-mkt-m365-copilot-pricing`. Both records cite the identical Microsoft pricing page and quote the exact $30/user/month annual add-on price.
4. **`ev-skp-reddit-sales-minimal-decks`** (skeptic-research)
   * *URL:* `https://www.reddit.com/r/sales/comments/148jm0y/presentation_decks/`
   * *Reason:* Composite duplicate conflation. Conflates comments from two distinct commenters (`imfatterthanyou` regarding conversational selling and `elguiri` regarding 10-15 min master template customization) into a single composite observation under one author tag. Both underlying comments are already independently verified in `ev-pain-rep-disdain-for-decks` and `ev-pain-master-template-workaround`.
5. **`ev-wf-saas-am-qbr-hours-editing`** (workflow-mapping)
   * *URL:* `https://www.reddit.com/r/sales/comments/148jm0y/presentation_decks/`
   * *Reason:* Exact duplicate of `ev-pain-sales-qbr-hours-editing`. Same Reddit comment by user `theflatlanderz` reporting hours spent manually editing presentation templates for QBRs.
6. **`ev-wf-saas-ae-master-slide-workaround`** (workflow-mapping)
   * *URL:* `https://www.reddit.com/r/sales/comments/148jm0y/presentation_decks/`
   * *Reason:* Exact duplicate of `ev-pain-master-template-workaround`. Same Reddit comment by user `elguiri` describing a 100-slide master template with 6 mandatory slides taking 10-15 minutes.
7. **`ev-wf-saas-ae-conversational-rejection`** (workflow-mapping)
   * *URL:* `https://www.reddit.com/r/sales/comments/148jm0y/presentation_decks/`
   * *Reason:* Exact duplicate of `ev-pain-rep-disdain-for-decks`. Same Reddit comment by user `imfatterthanyou` arguing that decks do not close deals and prospects ignore them.

### Category B: Inaccessible / Untraceable Root URLs Lacking Post/Article Path (5 records)
These records fail Rule 3 ("Every factual evidence record requires a source URL") and Rule 4 ("Open and inspect the source. Search-result snippets do not count as evidence"). Citing a root homepage or subreddit root prevents independent verification of the claimed quote or fact.

8. **`ev-skp-reddit-consulting-mitochondria`** (skeptic-research)
   * *URL:* `https://www.reddit.com/r/consulting/`
   * *Reason:* Subreddit homepage root without a thread ID or post slug. The quote comparing AI slides to "a fourth-grade presentation on mitochondria" cannot be traced or verified against a specific post.
9. **`ev-skp-reddit-ai-deslop-rebuild`** (skeptic-research)
   * *URL:* `https://www.reddit.com/r/ProductivityApps/`
   * *Reason:* Subreddit homepage root without a thread ID or post slug. Synthesis of the "generate-then-rebuild" cycle is untraceable to a primary post.
10. **`ev-skp-security-nda-soc2-blocker`** (skeptic-research)
    * *URL:* `https://www.forbes.com`
    * *Reason:* Root domain of Forbes without an article path. Claims regarding enterprise bilateral NDAs, SOC 2 Type II, and vendor risk assessments represent unsourced commentary rather than inspected reporting.
11. **`ev-skp-buyer-revops-procurement`** (skeptic-research)
    * *URL:* `https://www.salesforce.com`
    * *Reason:* Root domain of Salesforce without an article, report, or whitepaper slug. Claims regarding RevOps budget ownership and procurement barriers are untraceable.
12. **`ev-skp-agency-freelance-alternative`** (skeptic-research)
    * *URL:* `https://www.upwork.com`
    * *Reason:* Generic marketplace homepage root (`upwork.com`) without a service category slug. (Note: `wtp-research` provided the canonical verified URL `https://www.upwork.com/hire/presentation-designers/` in `ev-wtp-upwork-presentation-designer-hourly`).

### Category C: Misleading Money Attribution & Duplicate (1 record)
13. **`ev-wtp-reddit-revops-six-figure-ceiling`** (wtp-research)
    * *URL:* `https://www.reddit.com/r/revops/comments/1hs7xyp/sfdc_fields_slides_for_customer_facing/`
    * *Reason:* Severe money misattribution. The raw record assigned `money_signal = stated_wtp` with `money_amount = 100000.0 USD/year`. However, the poster explicitly stated: *"Was hoping for something that's not a 6 figure solution since we only need it for 1 use case."* The poster was actively rejecting 6-figure pricing. Furthermore, the underlying Reddit post is already accurately captured as a pain signal in `ev-pain-revops-sfdc-to-slides-manual-drain`.

---

## 3. Partially Verified Records Analysis (9 Records)

The 9 `PARTIALLY_VERIFIED` records contain valid observations, but suffer from specific field inaccuracies, unit errors, or source scope issues:

### A. Unit Encoding Errors: Labor Hours Encoded as Dollars (3 records)
In three records, researchers observed manual employee time in hours, but incorrectly recorded the hour count directly into the `money_amount` field with currency `USD`:
* **`ev-pain-consulting-daily-formatting-hours`**: Consultant spends 3 hours/day formatting PowerPoint slides (`employee_time`). Raw record incorrectly stored `money_amount = 3.0 USD/day`.
* **`ev-wf-cre-om-12hr-buildout`**: CRE broker spends 12 hours creating each Offering Memorandum in Buildout (`employee_time`). Raw record incorrectly stored `money_amount = 12.0 USD/per_opportunity`.
* **`ev-wf-consulting-monthly-deck-copy-paste`**: Consultant spends 2 hours/month manually updating 60 figures in a 40-slide deck (`employee_time`). Raw record incorrectly stored `money_amount = 2.0 USD/month`.
* *Audit Disposition:* The underlying manual time drains are fully verified as `employee_time` pain/workflow signals, but `money_amount` cannot be counted as cash spend.

### B. Vendor ARR Encoded as Customer SaaS Spend (1 record)
* **`ev-skp-tome-shutdown-pivot`**: Forbes article verifies that Tome shut down its AI presentation tool on April 30, 2025 and pivoted to Lightfield CRM after annual revenue plateaued at ~$3M. The raw record classified this as `money_signal = saas_spend` with `money_amount = 3000000.0 USD/year`.
* *Audit Disposition:* The shutdown and revenue plateau are verified market facts, but $3M represents vendor ARR across 25 million users, not customer SaaS spend.

### C. Unsupported Pricing on Root Domain (2 records)
* **`ev-skp-matik-salesforce`**: Matik's core capability (generating PPTX/Slides from Salesforce CRM data) is verified on `matik.io`. However, the raw record assigned `money_signal = actual_purchase` with `money_amount = 500.0 USD/year`. Matik does not publish or offer a $500/year tier on its homepage (Matik is custom enterprise pricing); the $500 figure is completely unsupported.
* **`ev-skp-buildout-cre-pricing`**: Buildout's CRE OM generation workflow is verified, but the specific pricing figures ($199/user/month + $275 platform fee) are not published on the root homepage `buildout.com` (which requires booking a demo).

### D. Source Bundling Across Unlinked Tools (1 record)
* **`ev-wtp-vendr-sales-enablement-median-spend`**: The Vendr URL (`https://www.vendr.com/marketplace/highspot`) verifies Highspot median annual contract spend ($60,405/yr). However, the observation also bundled in Seismic spend ($31,950/yr) and r/sales disclosures without providing the corresponding URLs.

### E. Generic Job Directory URL (1 record)
* **`ev-wtp-builtin-unbridled-presentation-designer`**: The job posting details for an Unbridled Presentation Designer ($65,000-$72,000 salary) are specific and detailed, but the URL links to `https://builtin.com/jobs` (search directory root) rather than the permanent posting slug.

### F. Extreme Age / Low Recency (1 record)
* **`ev-pain-head-of-sales-deprecating-decks`**: Reddit post from user reporting that Head of Sales deprecated pitch decks. The observation is supported, but the post date is **March 31, 2019** (over 7 years old), severely compromising recency for current generative AI / SaaS validation.

---

## 4. Deduplication & Independence Key Audit

To satisfy Workspace Rule 24 ("Before claiming a threshold is met, deduplicate by `independence_key`"), all multi-record URLs were audited for shared underlying sources.

### Multi-Record Source URL Resolution

| Source URL | Raw Records | Action / Resolution | Independent VERIFIED Records Retained |
| :--- | :---: | :--- | :--- |
| `reddit.com/r/sales/comments/148jm0y/` | 8 | 4 distinct commenters in thread (`theflatlanderz`, `imfatterthanyou`, `elguiri`, `1discostu`). Redundant duplicates in workflow and skeptic rejected. | **4 unique records** (`ev-pain-sales-qbr-hours-editing`, `ev-pain-rep-disdain-for-decks`, `ev-pain-master-template-workaround`, `ev-pain-outsourced-deck-freelancer`) |
| `trustpilot.com/review/gamma.app?page=4` | 5 | 5 distinct verified users (`Alexandre Tranchant`, `Jazz`, `Dan Twing`, `Tom Burke`, `Vicky GU`) reviewing different functional failures. | **5 unique records** (all retained with unique author keys) |
| `reddit.com/r/consulting/comments/1jv5dwk/` | 3 | 2 distinct commenters (`Reddit Consultant`, `NoogatAI`). One record has unit error (`PARTIALLY_VERIFIED`). | **2 VERIFIED records** (`ev-pain-consulting-thirty-percent-time`, `ev-pain-consulting-client-theme-rework`) |
| `reddit.com/r/sales/comments/13tcscl/` | 2 | 2 distinct commenters (`No-Lab4815` on analyst role, `artfuldawdg3r` on enablement offloading). | **2 unique records** (both retained) |
| `reddit.com/r/CommercialRealEstate/comments/1tmr2n7/` | 2 | 2 distinct commenters (`New_England_CRE` broker vs `Yoncen` InDesign designer). Broker has unit error. | **1 VERIFIED record** (`ev-wf-cre-designer-indesign-bottleneck`) |
| `reddit.com/r/CommercialRealEstate/comments/1gg6all/` | 2 | 2 distinct commenters (`TerdFerguson2112` investor vs `Meatonthebone23` capital markets analyst). | **2 unique records** (both retained) |
| `reddit.com/r/consulting/comments/1vt8k9n/` | 2 | 2 distinct commenters (`Ancient_Wave_8245` analyst vs `sqenchlift444` PMO). Analyst has unit error. | **1 VERIFIED record** (`ev-wf-consulting-claude-skills-breakage`) |
| `reddit.com/r/agency/comments/1fukogp/` | 2 | 2 distinct commenters (`really_evan` VA workflow vs `Sleep-Charming` Qwilr substitute). | **2 unique records** (both retained) |
| `microsoft.com/.../copilot-for-microsoft-365` | 2 | Exact duplicate pricing records. Skeptic duplicate rejected. | **1 VERIFIED record** (`ev-mkt-m365-copilot-pricing`) |
| `vendr.com/marketplace/highspot` | 2 | Market pricing verified. WTP record bundled Seismic without URL (`PARTIALLY_VERIFIED`). | **1 VERIFIED record** (`ev-mkt-highspot-contract-floor`) |
| `reddit.com/r/revops/comments/1hs7xyp/` | 2 | Pain verified. WTP record had $100k misattribution and was rejected. | **1 VERIFIED record** (`ev-pain-revops-sfdc-to-slides-manual-drain`) |

> [!NOTE]
> Following the audit, **the 66 VERIFIED records map to exactly 66 unique `independence_key` values**. There are zero duplicate independence keys in the canonical dataset.

---

## 5. Source Tier & Distribution Breakdown

### Verified Evidence by Source Tier

```
Tier A (Primary / Direct Source):  62 records (93.9%)
Tier B (Reputable Secondary):        4 records ( 6.1%)
Tier C (Lead / Unsupported):         0 records ( 0.0%)
Total VERIFIED:                    66 records
```

*All 66 VERIFIED records are supported by Tier A primary sources (official pricing pages, documentation, first-hand practitioner posts, verified user reviews, active job postings) or reputable Tier B intelligence (Vendr procurement data, VentureBeat reporting, ZipRecruiter benchmark).*

### Verified Evidence by Collecting Agent

| Agent | Raw Records | VERIFIED | PARTIALLY_VERIFIED | REJECTED | Verification Rate |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`market-research`** | 21 | **21** | 0 | 0 | 100.0% |
| **`pain-mining`** | 25 | **23** | 2 | 0 | 92.0% |
| **`skeptic-research`** | 16 | **4** | 4 | 8 | 25.0% |
| **`workflow-mapping`** | 16 | **11** | 2 | 3 | 68.8% |
| **`wtp-research`** | 10 | **7** | 1 | 2 | 70.0% |
| **Total** | **88** | **66** | **9** | **13** | **75.0%** |

*Note on `skeptic-research`: The lower verification rate (25.0%) was driven by the use of generic root URLs (e.g. `forbes.com`, `salesforce.com`, `reddit.com/r/consulting/`) and cross-agent duplication of records already captured in market and pain mining.*

### Verified Evidence by Record Type

| Record Type | VERIFIED Count | Primary Insights Established |
| :--- | :---: | :--- |
| **`gap`** | 18 | PPTX export fidelity breakdowns, corporate template overrides, desktop Copilot failures, python-pptx layout constraints. |
| **`workflow`** | 11 | Multi-stage collateral assembly line, QBR prep, RFP burdens, InDesign specialist bottleneck. |
| **`wtp`** | 9 | Agency retainers ($899-$15k/mo), freelance rates ($35-$150/hr), full-time designer salaries ($89k). |
| **`market`** | 8 | Competitor pricing tiers ($10-$40/mo), think-cell spend ($260-$325/yr), Highspot contract floor ($70k+). |
| **`pain`** | 8 | Formatting time drain (30% of day), recoloring rework, template corruption, sales deck skepticism. |
| **`substitute`** | 9 | Enterprise enablement suites (Seismic, Showpad, Highspot), web proposals (Storydoc, Qwilr), think-cell. |
| **`risk`** | 2 | Tome presentation shutdown ($81M raised, 25M users, $3M ARR plateau), third-party Google security block. |
| **`reachability`** | 1 | APMP association directory covering 11,000+ corporate bid and presentation managers globally. |
| **Total** | **66** | |

### Polarity of Verified Evidence

* **`supports`**: 44 records (66.7%) — Validates pain, manual formatting labor, export bugs in existing AI tools, and willingness to pay for slide design services.
* **`contradicts`**: 15 records (22.7%) — Establishes severe incumbent substitutes (Seismic, Highspot, Showpad), conversational sales pushback against decks, master template workarounds (10-15 min), and python-pptx rendering hurdles.
* **`neutral`**: 7 records (10.6%) — Baseline pricing benchmarks and feature mappings (Gamma, Beautiful.ai, Pitch, Copilot, Templafy, Qwilr).

---

## 6. Pre-Judge Gate Audit Checklist

The table below previews the verified evidentiary foundation available for the Stage 1 Judge under `methodology/stage1-gates.md`:

| Stage 1 Gate | Required Threshold | VERIFIED Audit Foundation | Preliminary Data Status |
| :--- | :--- | :--- | :--- |
| **G1: Concrete Pain** | ≥20 VERIFIED independent concrete pain signals (≥10 from plausible ICPs) | **26 verified records** reporting actual workflow problems, formatting drains, template corruption, export failures, and delays across Consultancies, CRE, Agencies, MSPs, and RevOps. | Threshold numerically exceeded with strong ICP attribution. |
| **G2: Recurrence** | At least MEDIUM confidence that core job recurs frequently enough for SaaS | Verified signals document **quarterly QBRs** (`ev-pain-sales-qbr-hours-editing`), **weekly PMO/client decks** (`ev-pain-pptx-master-slide-corruption`), **daily formatting** (`ev-pain-consulting-thirty-percent-time`), and **per-opportunity pitches** (`ev-wf-cre-om-turnaround-investor`). | High/Medium confidence supported. |
| **G3: Existing Spend / WTP** | ≥5 VERIFIED money signals from ≥2 distinct spend categories | **37 VERIFIED money signals** across **7 distinct categories**: Agency Spend (3), Contractor Spend (4), Dedicated Roles (6), Competitor Pricing (11), SaaS Spend (3), Employee Time (8), Stated WTP / Templates (1), Actual Purchase (1). | Threshold overwhelmingly met; multiple verified commercial spend categories. |
| **G4: Repeatable Gap** | ≥10 VERIFIED records showing repeatable workaround, manual cleanup, or tool failure | **18 VERIFIED gap records** clustering tightly around two repeatable technical failures: (1) Export fidelity/layout distortion in AI deck tools, and (2) Inability to respect corporate PowerPoint master templates. | Highly cohesive wedge validated. |
| **G5: Reachability** | Plausible roles, company segments, and reachable channels (≥MEDIUM confidence) | Verified roles: Proposal Managers, Sales Enablement Managers, CRE Marketing Specialists, BD Analysts. Verified channel: **APMP (11,000+ members)**. | Sufficient surface for Stage 2 prospect mining. |
| **G6: No Killer Substitute** | No low-friction substitute solving workflow sufficiently well at price destroying value prop | **CRITICAL SKEPTIC FINDING**: Highspot AutoDocs, Seismic LiveDocs, and Showpad ACB solve CRM-to-PPTX generation natively. However, they are locked behind $70k-$180k enterprise floors, leaving SMB/mid-market unserved. | Key strategic tension for Judge evaluation. |

---

## 7. Compliance Attestation

1. The Auditor did not conduct new market research or browse the web for replacement sources (Rules 18, 25).
2. All 13 rejected records and 9 partially verified records were flagged strictly according to the Evidence Standard (Rules 1-7, 13-14).
3. The canonical dataset `ideas/deck-automation/evidence/evidence.jsonl` contains exactly 88 records and passes `methodology/evidence-schema.json` with zero errors.
4. No PASS/FAIL verdict has been issued (Rule 17, SKILL.md).

