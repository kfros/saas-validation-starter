# Stage 1 Evidence Audit Summary: Geo Monitoring

**Idea**: `geo-monitoring`  
**Target Scope**: `GEO-AGENCY-01` (Independent SEO agencies with 2–20 staff serving SMB clients on recurring retainers)  
**Evaluation Date**: 2026-09-08  
**Audit Status**: COMPLETE  

---

## 1. Executive Summary & Status Breakdown

All 86 raw evidence records collected across the 5 discovery tracks (`market`, `pain`, `wtp`, `workflow`, `skeptic`) were audited against public source URLs, repository evidence schemas, and semantic definitions.

| Track | Total Raw | VERIFIED | PARTIALLY_VERIFIED | REJECTED | PENDING |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Market** (`raw/market`) | 18 | 17 | 1 | 0 | 0 |
| **Pain** (`raw/pain`) | 25 | 24 | 1 | 0 | 0 |
| **WTP** (`raw/wtp`) | 10 | 6 | 2 | 0 | 1 |
| **Workflow** (`raw/workflow`) | 15 | 14 | 0 | 1 | 0 |
| **Skeptic** (`raw/skeptic`) | 18 | 16 | 2 | 0 | 0 |
| **Total** | **86** | **78** | **6** | **1** | **1** |

---

## 2. Non-Verified Records & Blockers

### Rejected Records (1)
- **`geo-workflow-14-semrush-substitute-gap`** (`agencydashboard.io`):
  - *Reason*: Inspection revealed the cited excerpt does not exist anywhere on the target page. The page provides a general discussion of generative engine optimization without mentioning Semrush pricing ($139–$499/mo) or specific conversational AI gaps claimed in the raw observation. Status: `REJECTED`.

### Partially Verified Records (6)
- **`geo-market-peec-agency-plans`** (`peec.ai/pricing-agencies`):
  - *Reason*: Base pricing and credits verified (€205/mo Essential, €425/mo Growth, €675/mo Scale). However, the comparison table allocates 2 and 5 client projects respectively (while cards recommend for 3–10 and 11–25+ clients), conflicting with the raw claim of 3 and 7 projects.
- **`geo-pain-reddit-consistentsally-api-consumer-discrepancy`** (`reddit.com/r/SEO/comments/1ltwzlt/comment/n1tu5jt/`):
  - *Reason*: Verbatim quote by `Consistent_Sally_11` verified within thread `1ltwzlt` (comment `nuvs0wi`), but raw permalink pointed to comment `n1tu5jt` (authored by `SEOPub`).
- **`geo-wtp-pricing-peec-agency`** (`peec.ai/pricing-agencies`):
  - *Reason*: Plan features verified, but official pricing is listed in EUR (€205/mo Essential, €425/mo Growth, €675/mo Scale) rather than USD ($245/$495/$795), and comparison table specifies 1, 2, and 5 projects.
- **`geo-wtp-pricing-otterly-standard`** (`otterly.ai/pricing`):
  - *Reason*: Standard plan features confirmed, but official pricing is EUR (€189/mo) rather than USD ($189/mo).
- **`geo-skeptic-substitute-peec-pricing`** (`peec.ai/pricing-agencies`):
  - *Reason*: Official tier pricing and credit definitions confirmed, but comparison table allocates 5 client projects on Scale rather than 10 as stated in the raw record.
- **`geo-skeptic-pain-seo-dashboards-vs-manual`** (`reddit.com/r/SEO/comments/1l8dous/are_ai_visibility_tools_actually_helpful/`):
  - *Reason*: Core observation confirmed in comments by `stevebrownlie`, but raw excerpt combined sentences from two separate commenters (`stevebrownlie` and `cinematic_unicorn`).

### Blocked / Pending Records (1)
- **`geo-wtp-upwork-pr-agency-contract`** (`upwork.com/freelance-jobs/apply/...`):
  - *Reason*: Inspection blocked by Cloudflare Turnstile challenge on Upwork. In compliance with Rule 25 and Rule 27, no automated scraping bypass or workaround was attempted. Preserved with status `PENDING` (must not be counted by Judge).

---

## 3. Breakdown by Source Tier, Type & Money Signal

### Source Tier Breakdown (Audited Records)
- **Tier A** (Official docs, pricing, first-hand practitioner reports): 68 records (61 VERIFIED, 5 PARTIALLY_VERIFIED, 1 PENDING, 1 REJECTED)
- **Tier B** (Industry press, practitioner blogs, verified directories): 11 records (11 VERIFIED)
- **Tier C** (Unverified secondary discussions, editorial commentary): 7 records (6 VERIFIED, 1 PARTIALLY_VERIFIED)

### Scope Classification (`GEO-AGENCY-01`)
- **IN_SCOPE**: 22 records
  - *Verified Agency Profiles & Deliverables*: What IF Web (3 records), SORN.AI (5 records), Butter Marketing (3 records), Embarque (2 records), Clutch Directory Channel (1 record).
  - *Verified Agency Operators*: Typical-Badger1922, nothabkuuys, jjnasty (2 records), erickrealz, ThirdEyesOfTheWorld, Arash-60, Elsa Ji / Topify, MAN0L2.
- **OUT_OF_SCOPE**: 36 records (Vendor pricing pages, tool documentation, enterprise consultancy articles, software founders).
- **UNKNOWN**: 28 records (Unverified solo practitioners, anonymous forum participants where team size/retainer model is not established).

### Money Signal Breakdown
- `competitor_price`: 24 records (Vendor pricing context; not buyer purchase signals)
- `employee_time`: 7 records (Directly observed labor spend: Typical-Badger1922, trustmeimnotnotlying, SuccessfulCoyote1800, jwipez, tachichuchi, Elsa Ji, SORN.AI)
- `saas_spend`: 6 records (maltelandwehr, Next-Calligrapher381, sammyp99, Diligent-Macaroon566, atlas-node-219, Terrybrt, Arash-60, Vegetable_Arm_9480)
- `agency_spend`: 1 record (Butter Marketing retainer rate card)
- `stated_wtp`: 1 record (Upwork PR agency contract - PENDING)
- `null`: 47 records

---

## 4. Deduplication & Independence Key Normalization

Duplicate claims across different tracks were identified and assigned canonical `independence_key` values so that the Stage 1 Judge does not count multiple observations from the same entity/source toward gate thresholds:

1. **`otterly-ai-pricing`**: Consolidated across `geo-market-otterly-pricing`, `geo-market-otterly-agency-partner`, `geo-wtp-pricing-otterly-standard`, `geo-workflow-15-otterly-looker-studio-connector`, and `geo-skeptic-substitute-otterly-pricing`.
2. **`peec-ai-pricing`**: Consolidated across `geo-market-peec-brand-pricing`, `geo-market-peec-agency-plans`, `geo-wtp-pricing-peec-agency`, `geo-workflow-13-peec-agency-substitute`, and `geo-skeptic-substitute-peec-pricing`.
3. **`profound-pricing`**: Consolidated across `geo-market-profound-brand-pricing`, `geo-market-profound-agency-pricing`, and `geo-skeptic-substitute-profound-pricing`.
4. **`rankscale-pricing`**: Consolidated across `geo-market-rankscale-pricing`, `geo-market-rankscale-agency`, and `geo-skeptic-substitute-rankscale-pricing`.
5. **`semrush-pricing`**: Consolidated across `geo-market-semrush-plans` and `geo-market-semrush-agency-reporting`.
6. **`seranking-pricing`**: Consolidated across `geo-market-seranking-plans` and `geo-market-seranking-agency-pack`.
7. **`ahrefs-pricing`**: Consolidated across `geo-market-ahrefs-plans`, `geo-market-ahrefs-brand-radar`, and `geo-skeptic-substitute-ahrefs-brand-radar`.
8. **`whatifweb-agency-profile`**: Consolidated across `geo-workflow-01-whatifweb-profile`, `geo-workflow-02-whatifweb-workflow`, and `geo-workflow-03-whatifweb-deliverable`.
9. **`sornai-agency-profile`**: Consolidated across `geo-workflow-04-sornai-profile`, `geo-workflow-05-sornai-workflow`, `geo-workflow-06-sornai-reporting-cadence`, and `geo-workflow-12-manual-workaround-labor`.
10. **`butter-marketing-profile`**: Consolidated across `geo-workflow-07-butter-marketing-profile`, `geo-workflow-08-butter-marketing-offer`, and `geo-skeptic-market-butter-agency-pricing`.
11. **`embarque-agency-profile`**: Consolidated across `geo-workflow-09-embarque-profile` and `geo-workflow-10-embarque-deliverable`.
12. **`reddit-jjnasty-no-roi-oneoff-audit`**: Consolidated across `geo-pain-reddit-jjnasty-losing-game-oneoff-audit` and `geo-skeptic-pain-agency-demand-execution`.
13. **`reddit-consistentsally-api-consumer-discrepancy`**: Consolidated across `geo-pain-reddit-consistentsally-api-consumer-discrepancy` and `geo-skeptic-pain-seo-prompt-fantasy-roi`.
14. **`reddit-middlesmell1031-otterly-false-competitors-peec`**: Consolidated across `geo-pain-reddit-middlesmell-otterly-hallucinated-competitors` and `geo-wtp-reddit-peec-agency-vat-checkout`.
15. **`reddit-vegetablearm9480-tool-abandonment-inability-to-act`**: Consolidated across `geo-pain-reddit-vegetablearm-tool-abandonment-no-action` and `geo-wtp-reddit-churn-no-actionability`.

---

## 5. Potential Gate Eligibility Counts (Audit Input to Judge)

*Note: Per rule 17 and Rule 18, Evidence Auditor does not issue gate verdicts. The following counts reflect audited records meeting structural eligibility criteria for Stage 1 Judge review.*

- **Gate 1 (Market / Problem Reality: 20 independent records required)**:
  - Total VERIFIED in-scope records: 22 records across 12 unique independence keys.
  - Total VERIFIED all-scope records: 78 records across 49 unique independence keys.
  - *Integrity Note*: If strict `IN_SCOPE` attribution is required by the Judge, unique in-scope keys equal 12.
- **Gate 2 (Workflow & Trigger: 1 verified ICP workflow map required)**:
  - 4 complete agency profiles verified (`whatifweb-agency-profile`, `sornai-agency-profile`, `butter-marketing-profile`, `embarque-agency-profile`) with documented triggers, review cycles, and deliverables.
- **Gate 3 (Willingness to Pay / Costly Behavior: 5 signals across 2 categories required)**:
  - In-Scope Verified Revealed Signals:
    1. `employee_time`: `geo-pain-reddit-typicalbadger-patchwork-stack` (20 prompts/client weekly).
    2. `employee_time`: `geo-wtp-blog-agency-manual-hours` (250 manual searches weekly per account).
    3. `employee_time`: `geo-workflow-12-manual-workaround-labor` (Stanislava Smiljanic / SORN.AI manual VPN & print screens).
    4. `saas_spend`: `geo-pain-reddit-arash60-defensive-monthly-client-reporting` (Guzu.ai baseline tracking).
  - Out-of-Scope / Unknown Verified Revealed Signals:
    5. `saas_spend`: `geo-wtp-reddit-peec-usage` (`maltelandwehr` - unknown size).
    6. `saas_spend`: `geo-wtp-reddit-multitool-portfolio` (`Next-Calligrapher381` - unknown size).
    7. `employee_time`: `geo-pain-reddit-trustmeimnotnotlying-weekly-spreadsheet` (weekly spreadsheet - unknown size).
    8. `employee_time`: `geo-pain-reddit-successfulcoyote-manual-screenshot-workflow` (20 min/mo manual searches - unknown size).
    9. `employee_time`: `geo-pain-reddit-jwipez-custom-crawler-model-update-breakage` (custom crawler effort - unknown size).
- **Gate 4 (Pain Severity & Recurring Frustration: 10 independent records across 2 clusters required)**:
  - Verified pain records: 24 records.
  - In-scope verified pain records: 7 records (`Typical-Badger1922`, `nothabkuuys`, `jjnasty`, `erickrealz`, `ThirdEyesOfTheWorld`, `Arash-60`, `MAN0L2`).
- **Gate 5 (Reachability: 1 verified scalable channel with >100 reachable targets)**:
  - `geo-workflow-11-reachability-clutch`: Clutch directory with filters specifically targeting 2–9 and 10–49 employee SEO agencies offering GEO/AEO services.
- **Gate 6 (Technical Feasibility & Unit Economics)**:
  - Empirical research and official API documentation confirm heavy stochastic variance (Jay Sim: n=7 repeats required), high API search costs (OpenAI $10–$25/1k, Gemini $14–$35/1k, Perplexity $5–$14/1k), and explicit ToS prohibitions against consumer interface scraping (OpenAI Terms of Use).
