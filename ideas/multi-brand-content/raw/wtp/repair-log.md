# WTP Track Repair Log — Baseline 4041943

**Idea:** `multi-brand-content`  
**Scope:** `MULTIBRAND-OPERATOR-01`  
**Baseline:** `4041943510d75728079d02606ade13a6c6d187d4`  
**Track:** `ideas/multi-brand-content/raw/wtp`  
**Date:** 2026-09-09  
**Agent:** `wtp-research`  
**Status:** `PARTIAL` (4/10 inspected & repaired, 6/10 blocked by non-JS tool limitation on client-rendered Reddit comments)

---

## 1. Tool Interruption & Resource Blocker Report

In accordance with Validation Rules 25, 27, 28, and 30:

- **Total records processed:** 10 atomic evidence records (`mb-wtp-001` through `mb-wtp-010`).
- **Records directly inspected & repaired:** 4 records (`mb-wtp-002`, `mb-wtp-004`, `mb-wtp-005`, `mb-wtp-008`).
- **Records blocked by tool limits:** 6 records (`mb-wtp-001`, `mb-wtp-003`, `mb-wtp-006`, `mb-wtp-007`, `mb-wtp-009`, `mb-wtp-010`).
- **Blocked source types:** Dynamic Lit/web-component client-rendered Reddit comment subtrees.
- **Tool / resource failure:**
  1. The `chrome_devtools` MCP server is disabled/disallowed in this environment (`server chrome_devtools is not allowed in this context`).
  2. The available HTTP tool (`read_url_content`) does not execute JavaScript.
  3. Reddit's modern desktop web frontend renders original post titles and bodies in server-side rendered (SSR) HTML, but delivers comment trees dynamically via client-side GraphQL requests.
  4. Consequently, thread OP posts (`mb-wtp-002`, `mb-wtp-004`, `mb-wtp-005`, `mb-wtp-008`) were directly inspectable and verified in live source text, whereas commenter-attributed posts (`mb-wtp-001`, `mb-wtp-003`, `mb-wtp-006`, `mb-wtp-007`, `mb-wtp-009`, `mb-wtp-010`) could not be rendered or verified.
  5. Applying Validation Rule 25 ("Do not attempt to bypass unavailable or rate-limited research tools by building ad-hoc web scrapers..."), Rule 27, and Section A Rule 10 ("If the page cannot be inspected, do not repair from this task list or memory"), commenter-attributed records were preserved in their raw `PENDING` state and logged as `BLOCKED` with unresolved overclaims explicitly documented.

---

## 2. Record-by-Record Repair Audit

### mb-wtp-001
- **Attributed Speaker:** `New-Activity-8659`
- **Source URL:** `https://www.reddit.com/r/canva/comments/1oqdoe9/business_vs_enterprise_for_managing_multiple/`
- **Identified Issue:** Legacy paid-plan statement ($120/yr Canva Teams) does not prove that all 1,000 brand kits are utilized, that the payer matches the target ICP, or that the subscription was purchased specifically for the target multi-brand static post job.
- **Actual Inspection Date / Result:** 2026-09-09 / `BLOCKED`. Author is a commenter in the thread; comment tree is client-side rendered and inaccessible without JavaScript execution.
- **Changed Fields:** None in raw `evidence.jsonl`. Raw record preserved with `audit_status: PENDING`.
- **Corrected Supported Fact / Unresolved Overclaim:** UNRESOLVED OVERCLAIM. Overclaims in previous review (attributing full brand kit utilization and strict ICP membership to a legacy plan holder) cannot be verified from live source text.
- **Remaining Unknowns:** Exact comment text, speaker's current business model, client load, and brand kit utilization.
- **Status:** `BLOCKED`

---

### mb-wtp-002
- **Attributed Speaker:** `UniversityWestern346` (Thread OP)
- **Source URL:** `https://www.reddit.com/r/canva/comments/1oqdoe9/business_vs_enterprise_for_managing_multiple/`
- **Identified Issue:** `company_size` contained "5 clients" (client count confused with organizational headcount); `icp` forced `MULTIBRAND-OPERATOR-01`; unexecuted planned purchase treated as confirmed spend.
- **Actual Inspection Date / Result:** 2026-09-09 / `INSPECTED`. OP post body verified verbatim in SSR HTML.
- **Changed Fields:** `observed_at` ("2026-09-09"), `source_excerpt` (verbatim text from OP post), `company_size` (`null`), `icp` (`null`), `role` ("Agency Designer / Freelance Designer"), `money_amount` (30.0), `money_currency` ("USD"), `money_period` ("monthly"), `observation` (clarified evaluation of Canva Business upgrade and $6 pass-through intent), `interpretation` (clarified stated WTP vs revealed spend).
- **Corrected Supported Fact:** Solo agency designer managing 5 client brands with expansion plans is evaluating upgrading from Canva Pro to Canva Business at $30/month for multiple brand kits and controls, intending to pass the subscription cost to clients ($6 each). Shows stated WTP, but purchase has not been executed. Organizational headcount is unknown.
- **Remaining Unknowns:** Whether the upgrade was executed; agency total headcount; whether clients accepted pass-through billing.
- **Status:** `DONE`

---

### mb-wtp-003
- **Attributed Speaker:** `NikiforovAleksandr`
- **Source URL:** `https://www.reddit.com/r/SocialMediaMarketing/comments/ycgaw2/should_i_pay_for_a_clients_later_subscription/`
- **Identified Issue:** $200 for 100 accounts does not establish $2/client/month if billing period is unknown; scheduling spend is adjacent to static production; inferred monthly price and universal WTP ceiling are unsupported.
- **Actual Inspection Date / Result:** 2026-09-09 / `BLOCKED`. Author is a commenter; comment tree is client-side rendered and inaccessible without JavaScript execution.
- **Changed Fields:** None in raw `evidence.jsonl`. Raw record preserved with `audit_status: PENDING`.
- **Corrected Supported Fact / Unresolved Overclaim:** UNRESOLVED OVERCLAIM. Inferred $2/account/month unit economics and generalized market WTP ceiling remain unsupported without inspecting comment text and confirming billing frequency.
- **Remaining Unknowns:** Billing period (monthly, annual, or lifetime), exact tool features utilized, and whether provider is solo or agency.
- **Status:** `BLOCKED`

---

### mb-wtp-004
- **Attributed Speaker:** `Broad_Perspective166` (Thread OP)
- **Source URL:** `https://www.reddit.com/r/SocialMediaMarketing/comments/1m7dkeb/what_platform_do_you_use_for_client_approvals_on/`
- **Identified Issue:** Complaint establishes Planable usage and price dissatisfaction, not confirmed paid spend, dollar amount, or billing period. Money classification and interpretation claiming active spend were unsupported.
- **Actual Inspection Date / Result:** 2026-09-09 / `INSPECTED`. OP post body verified verbatim in SSR HTML.
- **Changed Fields:** `observed_at` ("2026-09-09"), `subtype` ("price_friction"), `source_excerpt` (verbatim text from OP post), `company_size` (`null`), `icp` (`null`), `role` ("Social Media Practitioner"), `money_signal` ("unknown"), `money_amount` (`null`), `money_currency` (`null`), `money_period` (`null`), `recurrence` ("unknown"), `observation` (focused on price friction for Grid view), `interpretation` (clarified absence of confirmed dollar spend).
- **Corrected Supported Fact:** Practitioner uses Planable for social media client approvals and finds it quite good, but seeks alternatives because Planable charges heavily ("charges a bomb") for its Grid view planner, which is the only view needed. Specific paid tier, dollar spend, and billing period are unstated.
- **Remaining Unknowns:** Current Planable tier (Free vs paid Pro/Enterprise), actual spend amount, team headcount, and client count.
- **Status:** `DONE`

---

### mb-wtp-005
- **Attributed Speaker:** `josh_moworld` (Thread OP)
- **Source URL:** `https://www.reddit.com/r/canva/comments/1g0pcdg/too_little_too_late_lol/`
- **Identified Issue:** Claimed a universal market price ceiling ($500/yr) and cited an Adobe Express deal quote that was not in the original post. `company_size` had inferred headcount.
- **Actual Inspection Date / Result:** 2026-09-09 / `INSPECTED`. OP post body verified verbatim in SSR HTML.
- **Changed Fields:** `observed_at` ("2026-09-09"), `source_excerpt` (verbatim quote, removed bracketed synthetic text), `company_size` (`null`), `icp` (`null`), `role` ("Small Business Operator"), `money_amount` (`null`), `money_currency` (`null`), `money_period` (`null`), `observation` (exact post facts: canceled Canva due to price hike + lag, substituted into existing Adobe Suite bundle with Express), `interpretation` (bounded to individual switching decision, removed universal market price ceiling).
- **Corrected Supported Fact:** Small business operator canceled Canva after a price hike and Chrome browser lag, switching to Adobe Express because they already pay for the Adobe Creative Suite and found Express's generative AI features adequate to replace Canva for their business. Specific subscription costs and seat counts are not stated in the post.
- **Remaining Unknowns:** Exact prior Canva subscription tier/price, Adobe Suite subscription cost, and team headcount.
- **Status:** `DONE`

---

### mb-wtp-006
- **Attributed Speaker:** `whyanalyze`
- **Source URL:** `https://www.reddit.com/r/SocialMediaMarketing/comments/1ixclwe/how_much_to_pay_social_media_manager_contractors/`
- **Identified Issue:** Actual $1,500/mo subcontracting package covered filming, editing, and posting with unallocated static portion; contractor abandonment was an isolated arrangement, not proof that all human subcontracting fails.
- **Actual Inspection Date / Result:** 2026-09-09 / `BLOCKED`. Author is a commenter; comment tree is client-side rendered and inaccessible without JavaScript execution.
- **Changed Fields:** None in raw `evidence.jsonl`. Raw record preserved with `audit_status: PENDING`.
- **Corrected Supported Fact / Unresolved Overclaim:** UNRESOLVED OVERCLAIM. Generalizing one failed contractor arrangement into a global assertion that human subcontracting fails remains unsupported without inspecting full comment context.
- **Remaining Unknowns:** Exact comment text, breakdown of $1,500 between static vs video/filming, and contractor location.
- **Status:** `BLOCKED`

---

### mb-wtp-007
- **Attributed Speaker:** `United_Broccoli_4032`
- **Source URL:** `https://www.reddit.com/r/SocialMediaMarketing/comments/1ixclwe/how_much_to_pay_social_media_manager_contractors/`
- **Identified Issue:** $400–$800 / $20–$40 discussion and $600 example are recommendations and illustrative arithmetic, not author's proven contractor expense; retaining $600 as actual spend was an overclaim.
- **Actual Inspection Date / Result:** 2026-09-09 / `BLOCKED`. Author is a commenter; comment tree is client-side rendered and inaccessible without JavaScript execution.
- **Changed Fields:** None in raw `evidence.jsonl`. Raw record preserved with `audit_status: PENDING`.
- **Corrected Supported Fact / Unresolved Overclaim:** UNRESOLVED OVERCLAIM. Treating illustrative margin math ($600/mo) as confirmed personal contractor spend remains unverified.
- **Remaining Unknowns:** Exact comment text, speaker's personal agency spending, and client retainers.
- **Status:** `BLOCKED`

---

### mb-wtp-008
- **Attributed Speaker:** `Still_Feedback1176` (Thread OP)
- **Source URL:** `https://www.reddit.com/r/SocialMediaMarketing/comments/1hlh20d/am_i_handling_too_many_accounts/`
- **Identified Issue:** `company_size` contained "5 accounts"; subtype claimed `owner_operator_time` while operator is an agency employee (fresher); money fields were misconfigured (`money_amount: 5.0`, `money_currency: "accounts"`); all effort was attributed to static production, ignoring photography, videography, reels, and stories.
- **Actual Inspection Date / Result:** 2026-09-09 / `INSPECTED`. Full post body verified verbatim via LD+JSON schema in SSR HTML.
- **Changed Fields:** `observed_at` ("2026-09-09"), `subtype` ("in_house_labor"), `source_excerpt` (verbatim text from post), `company_size` (`null`), `icp` (`null`), `role` ("Agency Social Media Operator (Fresher)"), `money_signal` ("employee_time"), `money_amount` (`null`), `money_currency` (`null`), `money_period` (`null`), `observation` (accurate scope: 5 client accounts, end-to-end execution including camera recording, design, copy, scheduling, daily reels/stories), `interpretation` (recognized in-house labor allocation, unquantified compensation, multi-discipline scope, and employee status).
- **Corrected Supported Fact:** Entry-level agency social media manager manages 5 client accounts across different industries as a single operator, handling video recording with a professional camera, graphic design, copywriting, and post scheduling. Low compensation relative to workload is reported, but salary is unquantified. Workload spans multiple disciplines beyond static graphics.
- **Remaining Unknowns:** Agency headcount, operator's exact compensation, client retainers, and proportion of time spent specifically on static graphics vs video/reels/shooting.
- **Status:** `DONE`

---

### mb-wtp-009
- **Attributed Speaker:** `Safe-Tell-7072`
- **Source URL:** `https://www.reddit.com/r/SocialMediaMarketing/comments/14zvgln/how_long_does_it_take_for_you_to_make_30_days/`
- **Identified Issue:** Source gave task-level timing, not a stated 25–45+ monthly hours/client total; excerpt in raw was a constructed summary; monthly totals and 1+ hour per carousel unsupported; solo-owner, client count, payment, and recurrence unverified.
- **Actual Inspection Date / Result:** 2026-09-09 / `BLOCKED`. Author is a commenter; comment tree is client-side rendered and inaccessible without JavaScript execution.
- **Changed Fields:** None in raw `evidence.jsonl`. Raw record preserved with `audit_status: PENDING`.
- **Corrected Supported Fact / Unresolved Overclaim:** UNRESOLVED OVERCLAIM. Aggregated monthly footprint (25–45+ hours per client) and constructed summary excerpt remain unverified against raw comment text.
- **Remaining Unknowns:** Exact comment text, speaker's business structure, client count, and whether task times apply to every post or select deliverables.
- **Status:** `BLOCKED`

---

### mb-wtp-010
- **Attributed Speaker:** `Kasia-K`
- **Source URL:** `https://www.reddit.com/r/SocialMediaMarketing/comments/1kti4jk/is_it_legal_to_use_canva_as_part_of_your_social/`
- **Identified Issue:** Source recommends Canva for client work and mentions a free version; does not establish speaker's actual free-plan use, avoidance of paid tools, retention, or refusal to pay. Behavioral/WTP conclusion and free_tier_retention subtype unsupported.
- **Actual Inspection Date / Result:** 2026-09-09 / `BLOCKED`. Author is a commenter; comment tree is client-side rendered and inaccessible without JavaScript execution.
- **Changed Fields:** None in raw `evidence.jsonl`. Raw record preserved with `audit_status: PENDING`.
- **Corrected Supported Fact / Unresolved Overclaim:** UNRESOLVED OVERCLAIM. Inferred free-tier retention and avoidance of paid tools remain unsupported without inspecting comment text.
- **Remaining Unknowns:** Exact comment text, speaker's personal tool subscription status, and commercial practices.
- **Status:** `BLOCKED`
