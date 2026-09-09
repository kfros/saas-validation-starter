# Evidence Repair Log — raw/skeptic (Baseline 4041943)

- **Track**: `skeptic`
- **Idea**: `multi-brand-content`
- **Scope Baseline**: `MULTIBRAND-OPERATOR-01`
- **Inspection Date**: 2026-09-09
- **Checker Baseline**: `python scripts/check_multibrand_stage1.py skeptic`
- **Summary**: All 14 raw records (`mb-skeptic-001` through `mb-skeptic-014`) were reopened on their original live public pages and directly inspected via the approved browser subagent. No sources were blocked; all 14 targets loaded and were verified in live source context. All material fields (observation, interpretation, source_excerpt, author, role, company_size, icp, recurrence, money fields, source dates, permalinks) were audited and repaired against live source facts. Priority IDs (`mb-skeptic-006`, `mb-skeptic-008`, `mb-skeptic-011`, `mb-skeptic-012`, `mb-skeptic-013`) and remaining rows were rigorously bounded: unsupported owner/operator status and inferred headcounts were removed; synthetic excerpts with ellipses were replaced with verbatim contiguous extracts; short-form video agency friction was separated from static organic production; one practitioner/team's satisfaction was separated from universal market-wide substitute sufficiency; and individual switching decisions were bounded away from market-wide pricing ceilings. All raw records remain in `audit_status: PENDING`.

---

## Checked Records Detail

### mb-skeptic-001
- **Issue**: Source date and observed date were set to baseline date (2026-09-08); interpretation asserted a market-wide "cheap incumbent pricing ceiling" from vendor pricing alone without proven adoption across all tiers.
- **Changed Fields**: `observed_at`, `source_date`, `observation`, `interpretation`.
- **Source URL & Exact Speaker**: `https://www.canva.com/en/pricing/?countryCode=us`, `Canva`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified US pricing: Free tier at $0 (1 Brand Kit, 3 colors); Pro at $18/mo ($180/yr billed annually) for 1 person (5 Brand Kits); Business at $25/person/mo ($250/yr per person billed annually) for teams (100 Brand Kits and approvals).
- **Supported Correction**: Updated inspection date to 2026-09-09; observation explicitly specifies US published pricing and features; interpretation bounded from market-wide pricing ceiling to published incumbent pricing baseline; role/icp/company_size remain null.
- **Unresolved Unknowns**: Proportion of SMM operators subscribing to Pro vs Business vs Free tiers.
- **Status**: DONE.

### mb-skeptic-002
- **Issue**: Observed date was baseline date (2026-09-08); source_excerpt had paraphrased brackets.
- **Changed Fields**: `observed_at`, `source_excerpt`, `observation`, `interpretation`.
- **Source URL & Exact Speaker**: `https://www.canva.com/help/brand-kit/`, `Canva`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified documentation: Free includes 1 Brand Kit (3 colors); Pro includes up to 5 Brand Kits; Business/Teams includes up to 100 Brand Kits; Enterprise supports up to 1,000 Brand Kits; up to 2,000 assets per category.
- **Supported Correction**: Updated observed date; source_excerpt replaced with exact documentation text; observation and interpretation bounded to documented capabilities and multi-brand asset separation within existing design software.
- **Unresolved Unknowns**: Operational overhead of switching between multiple brand kits within large multi-client accounts (>10 brands).
- **Status**: DONE.

### mb-skeptic-003
- **Issue**: Observed date was baseline date; source excerpt was a loose summary rather than exact documentation text.
- **Changed Fields**: `observed_at`, `source_excerpt`, `observation`, `interpretation`.
- **Source URL & Exact Speaker**: `https://www.canva.com/help/bulk-create/`, `Canva`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified documentation: Bulk Create connects tabular data (CSV/XLSX/tables) to template placeholders, generating up to 300 designs/pages; Help Center officially documents: "The Content Planner is not currently compatible with multi-design documents. As a workaround, copy the design you want to schedule into a new single-design and schedule it separately."
- **Supported Correction**: Updated observed date; source_excerpt replaced with exact contiguous verbatim quote regarding Content Planner incompatibility; observation and interpretation accurately document batch generation capabilities and the manual separation required before scheduling.
- **Unresolved Unknowns**: Frequency with which SMM practitioners actually use Bulk Create for multi-client batches vs manual template edits.
- **Status**: DONE.

### mb-skeptic-004
- **Issue**: Observed date was baseline date; interpretation treated published workspace pricing as a firm willingness-to-pay ceiling for all multi-brand review.
- **Changed Fields**: `observed_at`, `source_date`, `observation`, `interpretation`.
- **Source URL & Exact Speaker**: `https://planable.io/pricing/`, `Planable`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified pricing: Basic is $39/workspace/mo ($32.50/mo billed annually, 60 posts, 4 pages, unlimited users, optional approvals); Pro is $59/workspace/mo ($49.17/mo billed annually, 150 posts, 10 pages, unlimited users, Required approvals, team drafts).
- **Supported Correction**: Updated observed date and source date; observation accurately records workspace-based pricing structure with unlimited user seats; interpretation bounded to published competitor benchmark rather than buyer willingness to pay.
- **Unresolved Unknowns**: Actual buyer churn or retention at $39–$59/workspace/mo across small agencies.
- **Status**: DONE.

### mb-skeptic-005
- **Issue**: Observed date was baseline date; interpretation stated that Planable leaves "little room for a standalone review tool" without qualification.
- **Changed Fields**: `observed_at`, `observation`, `interpretation`.
- **Source URL & Exact Speaker**: `https://planable.io/pricing/`, `Planable`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified platform capabilities: isolated workspaces per brand, in-context annotations and comments on mockups, multi-tiered approval chains.
- **Supported Correction**: Updated observed date; observation and interpretation bounded to documented review/approval substitute capabilities without declaring universal market sufficiency.
- **Unresolved Unknowns**: Frequency of client bypass (e.g. clients demanding review via email or WhatsApp instead of using the Planable portal).
- **Status**: DONE.

### mb-skeptic-006
- **Issue**: Explicit priority repair target in Section C. Role was overclaimed as "Agency owner/operator"; company_size held client count ("6 clients"); icp forced "MULTIBRAND-OPERATOR-01" without proof of owner/operator status or SMB clientele; source_excerpt was rewritten with ellipses and merged sentences.
- **Changed Fields**: `role`, `company_size`, `icp`, `independence_key`, `source_excerpt`, `observation`, `interpretation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1vlj75n/published_a_client_post_with_an_old_visual/`, `Prudent-Bad-8786`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified verbatim OP text: "Small agency, 6 clients, everything gets designed in Canva and scheduled about a week out... Thursday the post goes out with the old date on it anyway, because what actually got pushed to the scheduler was the export from the Friday before. Nobody caught it, there was nothing to catch it with. Once it's exported, it's just a PNG sitting in a queue, it has no idea the design behind it moved on."
- **Supported Correction**: Role corrected to "Small agency practitioner / operations"; company_size corrected to "small agency"; client count (6 clients) preserved in observation; icp set to null; source_excerpt replaced with exact contiguous verbatim extract (303 chars); accidental support for static export decoupling failure fully preserved; shared entity key `reddit-user-prudent-bad-8786` aligned with `mb-pain-015`.
- **Unresolved Unknowns**: Agency total headcount; owner identity; client business size/revenue.
- **Status**: DONE.

### mb-skeptic-007
- **Issue**: Source URL was thread URL instead of comment permalink (`jo3h3e8`); company_size was set to "Multiple clients" (client count, not organizational headcount); icp forced "MULTIBRAND-OPERATOR-01" without proof of SMB clientele; excerpt merged sentences with ellipses (`...`).
- **Changed Fields**: `source_url`, `company_size`, `icp`, `source_excerpt`, `observation`, `interpretation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/148zs2w/comment/jo3h3e8/` (resolved comment permalink), `Mannymac2000`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `jo3h3e8`, published 2023-06-14.
- **Supported Correction**: Resolved comment permalink to `jo3h3e8`; company_size set to null (unquantified plural clients in observation); icp set to null; source_excerpt replaced with exact contiguous verbatim text; observation and interpretation bounded to individual freelance practitioner template efficiency rather than universal market sufficiency.
- **Unresolved Unknowns**: Exact client count, client industries, and agency vs solo organizational structure.
- **Status**: DONE.

### mb-skeptic-008
- **Issue**: Explicit priority repair target in Section C. Independent spot-check failed to reopen page; source_date was listed as 2026-02-15 instead of actual 2026-04-14; role was listed as "Agency marketer" without proving agency ownership; icp was set to MULTIBRAND-OPERATOR-01 without SMB proof; source_excerpt merged disconnected sentences with ellipsis; interpretation claimed global "high risk of client churn and engagement drop" leading practitioners to abandon automated generators.
- **Changed Fields**: `source_date`, `role`, `company_size`, `icp`, `source_excerpt`, `observation`, `interpretation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1sl3obg/is_anyone_feeling_the_ai_slop_burnout_how_im/`, `Unable-Connection-58`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Page loaded successfully (not blocked, not removed). OP author `Unable-Connection-58` published post on 2026-04-14: "I’ve been in marketing for 6 years... I almost lost a client last month because we automated everything. Our efficiency was up 40%, but engagement tanked. People were just scrolling past the perfection."
- **Supported Correction**: Verified page is accessible; corrected source_date to 2026-04-14; role set to "Marketing practitioner / agency operator"; company_size and icp set to null; source_excerpt replaced with exact contiguous verbatim text (159 chars); observation confirms 40% efficiency boost alongside client dissatisfaction and engagement collapse; interpretation bounded to practitioner risk rather than universal market abandonment.
- **Unresolved Unknowns**: Exact firm size, headcount, specific AI tools deployed, and client market segments.
- **Status**: DONE.

### mb-skeptic-009
- **Issue**: Source URL was thread URL instead of comment permalink (`og4p5bj`); source date was 2026-02-15 instead of 2026-04-14; excerpt inverted sentence order and merged with ellipsis (`...`); observation and interpretation omitted author's balancing context that prompt labor was still preferable to physical photoshoots.
- **Changed Fields**: `source_url`, `source_date`, `source_excerpt`, `observation`, `interpretation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1sl3obg/is_anyone_else_feeling_the_ai_slop_burnout_how_im/og4p5bj/` (resolved comment permalink), `Carey251`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `og4p5bj`, published 2026-04-14.
- **Supported Correction**: Resolved comment permalink to `og4p5bj`; corrected source_date to 2026-04-14; source_excerpt replaced with exact contiguous verbatim text (485 chars); observation and interpretation updated to reflect both the multi-hour prompt iteration burden for static visuals and the author's rationale comparing it favorably to live shoot costs.
- **Unresolved Unknowns**: Client count, agency affiliation, and specific AI image tools evaluated.
- **Status**: DONE.

### mb-skeptic-010
- **Issue**: Source URL was thread URL instead of comment permalink (`nkez6lb`); source date was 2025-10-18 instead of 2025-10-20; observation and interpretation generalized video scriptwriting rework into social media copy and layout rework without separating medium formats.
- **Changed Fields**: `source_url`, `source_date`, `role`, `source_excerpt`, `observation`, `interpretation`, `strength`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1oamrin/comment/nkez6lb/` (resolved comment permalink), `JoshOlufemii`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `nkez6lb`, published 2025-10-20.
- **Supported Correction**: Resolved comment permalink to `nkez6lb`; corrected source_date to 2025-10-20; role refined to "Video creator / content marketer"; source_excerpt replaced with exact contiguous verbatim quote; observation and interpretation explicitly bound the editing time penalty to long-form video scripting and creative storytelling, separating it from short static social posts; strength adjusted from 3 to 2.
- **Unresolved Unknowns**: Practitioner's volume of static social graphics compared to video production.
- **Status**: DONE.

### mb-skeptic-011
- **Issue**: Explicit priority repair target in Section C. Source URL was thread URL instead of comment permalink (`nq73sfk`); source date was 2025-11-20 instead of 2025-11-22; role was listed as "Agency operator" and company_size as "Agency with multiple clients"; icp forced "MULTIBRAND-OPERATOR-01"; observation and interpretation framed short-form video agency bottlenecks as a universal falsification point for all SMM production without acknowledging the short-form context.
- **Changed Fields**: `source_url`, `source_date`, `role`, `company_size`, `icp`, `source_excerpt`, `observation`, `interpretation`, `strength`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1p2zj55/comment/nq73sfk/` (resolved comment permalink), `TheGentleAnimal`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `nq73sfk`, published 2025-11-22.
- **Supported Correction**: Resolved comment permalink to `nq73sfk`; corrected source_date to 2025-11-22; role corrected to "Short-form agency operator"; company_size and icp set to null; source_excerpt replaced with exact contiguous text (388 chars); observation and interpretation explicitly identify that this operational friction occurs in a short-form video agency managing reels/shorts revisions on Trello Kanban, bounding the client-side bottleneck observation; strength adjusted from 4 to 3.
- **Unresolved Unknowns**: Exact agency headcount and whether the agency also handles static organic social posts.
- **Status**: DONE.

### mb-skeptic-012
- **Issue**: Explicit priority repair target in Section C. Source URL was thread URL instead of comment permalink (`ktmp16l`); role was listed as "Social media marketer", company_size as "Multiple clients", and icp forced "MULTIBRAND-OPERATOR-01"; interpretation upgraded one practitioner's workflow preference into "low market desire for standalone static content packages."
- **Changed Fields**: `source_url`, `role`, `company_size`, `icp`, `source_excerpt`, `observation`, `interpretation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1b847vd/comment/ktmp16l/` (resolved comment permalink), `unmethodicals`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `ktmp16l`, published 2024-03-06.
- **Supported Correction**: Resolved comment permalink to `ktmp16l`; role set to "Social media practitioner"; company_size and icp set to null; source_excerpt replaced with exact contiguous text (190 chars); observation accurately documents preference for view-only Canva links over file storage/calendars; interpretation bounded to firsthand practitioner satisfaction without claiming a universal market-wide rejection of exports.
- **Unresolved Unknowns**: Client count, agency vs freelance status, and whether clients ever require native editable handoffs.
- **Status**: DONE.

### mb-skeptic-013
- **Issue**: Explicit priority repair target in Section C. Source URL was thread URL instead of comment permalink (`n2su5nh`); source date was 2025-07-10 instead of 2025-07-12; company_size held "Agency team" and icp held "MULTIBRAND-OPERATOR-01"; interpretation upgraded one agency team's workflow into an assertion of complete substitute sufficiency for all operators.
- **Changed Fields**: `source_url`, `source_date`, `role`, `company_size`, `icp`, `source_excerpt`, `observation`, `interpretation`, `strength`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1lx80ha/comment/n2su5nh/` (resolved comment permalink), `k_rocker`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `n2su5nh`, published 2025-07-12. Matches `mb-pain-011`.
- **Supported Correction**: Resolved comment permalink to `n2su5nh`; corrected source_date to 2025-07-12; company_size and icp set to null; source_excerpt replaced with exact contiguous text (302 chars); observation documents shared Canva canvas collaboration across copywriters, designers, and clients; interpretation bounded to firsthand team satisfaction with an incumbent tool, removing claims of universal substitute sufficiency; strength adjusted from 4 to 3.
- **Unresolved Unknowns**: Headcount, specific client industries, and failure rates when client changes occur post-approval.
- **Status**: DONE.

### mb-skeptic-014
- **Issue**: Source date was listed as 2026-08-11 instead of actual comment date 2026-08-13; observed date was baseline date.
- **Changed Fields**: `source_date`, `observed_at`, `observation`, `interpretation`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1vlj75n/published_a_client_post_with_an_old_visual/`, `JuicerSocial`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment timestamp: 2026-08-13. Verbatim comment text verified.
- **Supported Correction**: Corrected source_date to 2026-08-13; updated observed_at to 2026-09-09; observation and interpretation precisely document the architectural decoupling between static PNG exports and downstream scheduling queues as a structural version-control vulnerability.
- **Unresolved Unknowns**: Feasibility and API support for automated queue cache invalidation across third-party social scheduling platforms.
- **Status**: DONE.

---

## Summary of Changes
- **Total Checked IDs**: 14
- **Changed Records**: 14 (all 14 updated with audited observed dates, verified source dates, exact contiguous excerpts or null, corrected roles, bounded interpretations, and schema-valid nulls for unproven company_size and icp fields)
- **Unchanged Records**: 0
- **Blocked Records**: 0 (all 14 sources successfully reopened on live public pages via browser subagent; zero tool blockers encountered)
- **Resolved Permalinks**:
  - `mb-skeptic-007`: `https://www.reddit.com/r/SocialMediaMarketing/comments/148zs2w/comment/jo3h3e8/`
  - `mb-skeptic-009`: `https://www.reddit.com/r/SocialMediaMarketing/comments/1sl3obg/is_anyone_else_feeling_the_ai_slop_burnout_how_im/og4p5bj/`
  - `mb-skeptic-010`: `https://www.reddit.com/r/SocialMediaMarketing/comments/1oamrin/comment/nkez6lb/`
  - `mb-skeptic-011`: `https://www.reddit.com/r/SocialMediaMarketing/comments/1p2zj55/comment/nq73sfk/`
  - `mb-skeptic-012`: `https://www.reddit.com/r/SocialMediaMarketing/comments/1b847vd/comment/ktmp16l/`
  - `mb-skeptic-013`: `https://www.reddit.com/r/SocialMediaMarketing/comments/1lx80ha/comment/n2su5nh/`
- **Scope Baseline Audit Conclusion**: 0 of the 14 raw records have primary source proof satisfying all criteria of `MULTIBRAND-OPERATOR-01` (external provider, multiple unrelated clients, recurring static content, owner/operator with hands-on production role, and explicit SMB clientele). All `icp` values have been set to `null` to prevent unevidenced scope upgrades upstream of Auditor and Judge.
