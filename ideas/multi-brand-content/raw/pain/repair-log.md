# Evidence Repair Log — raw/pain (Baseline 4041943)

- **Track**: `pain`
- **Idea**: `multi-brand-content`
- **Scope Baseline**: `MULTIBRAND-OPERATOR-01`
- **Inspection Date**: 2026-09-09
- **Checker Baseline**: `python scripts/check_multibrand_stage1.py pain`
- **Summary**: All 21 raw records (`mb-pain-001` through `mb-pain-021`) were reopened on their original live public pages via the approved browser subagent. No sources were blocked. All material fields (observation, interpretation, source_excerpt, author, role, company_size, icp, recurrence, money fields, source dates, permalinks) were audited and repaired against live source facts. Unsupported SMB claims and organization-size assertions (including `mb-pain-015`) were removed. Operator pain was preserved regardless of whether buying authority is proven (including `mb-pain-009`). Synthetic quotes and excerpts with ellipses were replaced with verbatim contiguous text or null. Comment permalinks were resolved to exact comment IDs.

---

## Checked Records Detail

### mb-pain-001
- **Issue**: Role was overclaimed as agency operator ("Designer / Agency Operator"); company_size held client count ("~5 clients"); target ICP was assigned without establishing owner-operator status.
- **Changed Fields**: `role`, `company_size`, `icp`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/canva/comments/1oqdoe9/business_vs_enterprise_for_managing_multiple/`, `UniversityWestern346`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified author states: "I am a designer who is working with a marketing agency and I’ve been tasked with figuring out which Canva type is right for us. We have about 5 clients that we manage with more on the way..."
- **Supported Correction**: Role corrected to "Designer working with marketing agency"; company_size set to null (client count is ~5 clients, retained in observation); icp set to null (owner-operator status unestablished); observation aligned with designer role.
- **Unresolved Unknowns**: Exact agency headcount; owner identity; whether the agency principal matches MULTIBRAND-OPERATOR-01.
- **Status**: DONE.

### mb-pain-002
- **Issue**: Provided comment permalink (`n9k45n4`) 404ed; source excerpt contained synthetic ellipses (`...`); company_size conflated headcount and client count ("1 person, 5 clients"); target ICP assigned without explicit SMB proof.
- **Changed Fields**: `source_url`, `company_size`, `icp`, `source_excerpt`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1ueutvu/comment/otqnc0d/` (resolved comment permalink), `Huge_Razzmatazz_985`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified verbatim text and comment ID `otqnc0d`.
- **Supported Correction**: Permalink updated to resolved ID `otqnc0d`; company_size corrected to "1 person"; client count (5 clients) preserved in observation; icp set to null (SMB unproven); excerpt replaced with exact contiguous verbatim text.
- **Unresolved Unknowns**: Revenue band and specific business classifications of the 5 clients.
- **Status**: DONE.

### mb-pain-003
- **Issue**: Assigned to MULTIBRAND-OPERATOR-01 without multi-client agency or SMB evidence; author is a former practitioner now building a SaaS tool; role unrefined.
- **Changed Fields**: `role`, `icp`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1kiemdm/comment/mrla7gn/`, `Recent_Nature_8474`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment text: author used 5 AI tools, spent ~4 hours daily, paid ~$150/mo, and is now building a solution.
- **Supported Correction**: Role corrected to "Former SMM practitioner / SaaS builder"; icp set to null; observation clarifies historical practitioner context.
- **Unresolved Unknowns**: Number of clients and clientele segment in historical practitioner role.
- **Status**: DONE.

### mb-pain-004
- **Issue**: Excerpt merged disconnected paragraphs with synthetic ellipses; role was labeled "Freelance Brand / Web Designer" and company_size "freelancer"; ICP was set to MULTIBRAND-OPERATOR-01 despite web designer advising client rather than external recurring SMM provider.
- **Changed Fields**: `role`, `company_size`, `icp`, `source_excerpt`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/canva/comments/1sc2a5m/found_out_canva_removed_the_styles_menu_mid/`, `DJAYK47`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified post text: author is a web designer who recommended Canva to a client and encountered sudden removal of the styles menu during a live client meeting.
- **Supported Correction**: Role corrected to "Web Designer"; company_size to null; icp to null; source_excerpt replaced with exact contiguous extract; observation updated.
- **Unresolved Unknowns**: Full client roster and recurring social production duties beyond web design handoffs.
- **Status**: DONE.

### mb-pain-005
- **Issue**: Provided comment permalink (`n9lbz3p`) 404ed; source date was listed as 2026-06-25 instead of actual 2026-06-29; advice was presented as personal operational incident; company_size held "agency" and icp held target scope without proof.
- **Changed Fields**: `source_url`, `source_date`, `role`, `company_size`, `icp`, `observation`, `interpretation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1ueutvu/comment/ouf4wov/` (resolved comment permalink), `ayecl`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `ouf4wov`, published 2026-06-29.
- **Supported Correction**: Resolved permalink to `ouf4wov`; corrected source_date to 2026-06-29; role to "Agency practitioner / consultant"; company_size to null; icp to null; observation and interpretation explicitly framed as advisory estimation guidance rather than personal firm audit.
- **Unresolved Unknowns**: Author's specific agency affiliation, ownership status, and client roster.
- **Status**: DONE.

### mb-pain-006
- **Issue**: Source URL was thread URL instead of comment permalink; author firmographics (role, company_size, icp) were unevidenced.
- **Changed Fields**: `source_url`, `role`, `company_size`, `icp`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/canva/comments/1rk9bj6/comment/o8kv01e/` (resolved comment permalink), `nataliakalinska`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `o8kv01e`.
- **Supported Correction**: Resolved comment permalink; role corrected to "Content creator"; company_size and icp set to null; observation updated to remove unevidenced professional SMM assumptions.
- **Unresolved Unknowns**: Author's professional agency affiliation, client count, and organization size.
- **Status**: DONE.

### mb-pain-007
- **Issue**: Excerpt contained a synthetic sentence not present in the post ("Was trying to create in bulk. I'll have to manually edit the names of each and every location in different csv files"); company_size ("freelancer") and icp ("MULTIBRAND-OPERATOR-01") were unevidenced.
- **Changed Fields**: `company_size`, `icp`, `source_excerpt`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/canva/comments/yo0m6r/bulk_create_with_two_lines/`, `consy_man786`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified post text: author has a project requiring bulk creation across two text layers and Canva collapses them into one line.
- **Supported Correction**: Removed synthetic quote and replaced with verbatim post text; company_size and icp set to null; observation accurately describes multi-line layer merging in Canva.
- **Unresolved Unknowns**: Organization size, whether user performs multi-brand client work.
- **Status**: DONE.

### mb-pain-008
- **Issue**: company_size held "agency / consultant" without headcount proof; icp was set to target scope without proof of owner/operator status or recurring organic content delivery.
- **Changed Fields**: `role`, `company_size`, `icp`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/mzutga/comment/gw3ipmq/`, `dvdmcn`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment text: author ran Facebook ads and experienced cross-client image contamination in a carousel.
- **Supported Correction**: Role refined to "Social Media Marketer"; company_size to null (multiple clients preserved in observation); icp to null.
- **Unresolved Unknowns**: Headcount, firm ownership, and proportion of organic vs paid ad work.
- **Status**: DONE.

### mb-pain-009
- **Issue**: Excerpt merged sentences with synthetic ellipsis; icp was set to MULTIBRAND-OPERATOR-01 despite author explicitly being an employee graphic designer at a small agency without buying authority.
- **Changed Fields**: `icp`, `source_excerpt`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1lx80ha/how_do_you_deliver_monthly_social_media_posts_to/`, `Ok-Guitar4196`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified post text: author is a graphic designer at a small agency making monthly batch social content across platforms (FB, IG, LI, X).
- **Supported Correction**: Per section B, preserved genuine operator pain of small-agency designer while setting icp to null (no owner/buyer authority); company_size "small agency" preserved; excerpt replaced with exact contiguous text without ellipsis; observation refined.
- **Unresolved Unknowns**: Exact agency headcount and specific client types.
- **Status**: DONE.

### mb-pain-010
- **Issue**: icp was set to MULTIBRAND-OPERATOR-01 without explicit proof of SMB clientele; recurrence and labor preserved.
- **Changed Fields**: `icp`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1sa5r9a/solo_social_managers_how_tf_are_you_staying/`, `GiraffeDelicious5649`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified post text: solo SMM managing multiple ongoing clients wastes hours across 20+ folders and transfers assets between phone, PC, and Canva.
- **Supported Correction**: Role ("Solo Social Media Manager") and company_size ("solo") preserved; icp set to null (client segment SMB unproven); observation accurately describes media folder sprawl and cross-device upload friction.
- **Unresolved Unknowns**: Exact client count and client revenue/segment.
- **Status**: DONE.

### mb-pain-011
- **Issue**: Provided comment permalink (`n2mhn74`) 404ed; actual comment ID was `n2su5nh`; source date was 2025-07-11 instead of 2025-07-12; role ("Agency Operator"), company_size ("agency"), and icp ("MULTIBRAND-OPERATOR-01") were unevidenced.
- **Changed Fields**: `source_url`, `source_date`, `role`, `company_size`, `icp`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1lx80ha/comment/n2su5nh/` (resolved comment permalink), `k_rocker`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `n2su5nh`, published 2025-07-12.
- **Supported Correction**: Resolved comment permalink to `n2su5nh`; corrected source_date to 2025-07-12; role to "Agency practitioner"; company_size and icp to null; observation accurately describes shared Canva canvas collaboration.
- **Unresolved Unknowns**: Firm size, client roster, and author's ownership status.
- **Status**: DONE.

### mb-pain-012
- **Issue**: Role was overclaimed as "Agency Team Operator", company_size held "agency team", and icp held target scope without proof of agency ownership or SMB clientele.
- **Changed Fields**: `role`, `company_size`, `icp`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1o7es1o/comment/nocl8p3/`, `Commercial_Carob_977`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment text: team starts with Google Doc briefs but chat spreads to WhatsApp/Slack/Gmail, leading to Briefmatic adoption.
- **Supported Correction**: Role refined to "Agency team practitioner"; company_size and icp set to null; observation accurately reflects adoption of Briefmatic to manage feedback sprawl across channels.
- **Unresolved Unknowns**: Agency headcount and client types.
- **Status**: DONE.

### mb-pain-013
- **Issue**: Excerpt merged paragraphs with synthetic ellipsis; role ("SMM Content Practitioner"), company_size ("freelancer / specialist"), and icp were unevidenced.
- **Changed Fields**: `role`, `company_size`, `icp`, `source_excerpt`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1pirk74/comment/o1zv78c/`, `maddiecoder`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment text: author tests marketing/AI tools for work; finds Jasper/Copy.ai homogeneous; relies on Canva + manual tweaking + spreadsheets.
- **Supported Correction**: Role corrected to "Marketing tool evaluator / content practitioner"; company_size and icp set to null; excerpt replaced with exact contiguous text; observation updated.
- **Unresolved Unknowns**: Organization type and client roster.
- **Status**: DONE.

### mb-pain-014
- **Issue**: Author manages content/ads for a single client ("my client"); company_size ("freelancer / agency") and icp ("MULTIBRAND-OPERATOR-01") were unevidenced.
- **Changed Fields**: `role`, `company_size`, `icp`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1m0gx6l/client_want_me_to_use_ai_to_reduce_cost/`, `PopularReception6422`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified post text: author's client wants them to use AI to reduce costs, but ChatGPT repeatedly produces generic off-brand copy.
- **Supported Correction**: Role refined to "Social media marketer / ad manager"; company_size and icp set to null; observation accurately reflects single-client AI cost reduction and brand amnesia pain.
- **Unresolved Unknowns**: Client count beyond the one mentioned; organization form.
- **Status**: DONE.

### mb-pain-015
- **Issue**: Explicit repair target in Section B. company_size was "6 SMB clients" (client count conflated with company size; SMB unevidenced); role claimed "Small Agency Operator"; icp claimed MULTIBRAND-OPERATOR-01 without proof of owner/operator status or SMB clientele; observation claimed "6 SMB clients".
- **Changed Fields**: `role`, `company_size`, `icp`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1vlj75n/published_a_client_post_with_an_old_visual/`, `Prudent-Bad-8786`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified post text: "Small agency, 6 clients, everything gets designed in Canva and scheduled about a week out...". Designer fixed date in Canva, but scheduler held Friday's PNG export and published wrong date.
- **Supported Correction**: Removed unsupported SMB attribution; company_size corrected to "small agency"; client count (6 clients) preserved in observation; role adjusted to "Small agency practitioner / operations"; icp set to null; genuine Canva revision desync / PNG scheduler failure fully preserved.
- **Unresolved Unknowns**: Exact agency headcount, owner identity, and client business size/revenue.
- **Status**: DONE.

### mb-pain-016
- **Issue**: Source URL was thread URL instead of comment permalink; author was listed as post author when author was a commenter (`khj8mjo`); company_size ("agency") and icp ("MULTIBRAND-OPERATOR-01") were unevidenced.
- **Changed Fields**: `source_url`, `role`, `company_size`, `icp`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/graphic_design/comments/194g5un/comment/khj8mjo/` (resolved comment permalink), `Luaanebonvoy311`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `khj8mjo`.
- **Supported Correction**: Resolved comment permalink; role corrected to "Design agency employee"; company_size and icp set to null; observation clarifies client price sensitivity and Canva template satisfaction.
- **Unresolved Unknowns**: Employer headcount and client market segments beyond tight-budget businesses.
- **Status**: DONE.

### mb-pain-017
- **Issue**: Critical scope mismatch! Author is an in-house marketing professional at a nonprofit scheduling posts for their own organization to tag donors/partners, but raw recorded role as "Marketing Professional", company_size as "multi-channel operator", industry as "marketing_services", and icp as "MULTIBRAND-OPERATOR-01" (which is explicitly excluded by the hypothesis).
- **Changed Fields**: `role`, `company`, `company_size`, `industry`, `icp`, `observation`, `interpretation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1hs150n/planable_crossposting_issues/`, `Capital-Act-5704`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified post text: "I am a marketing professional at a nonprofit who uses Planable as a content scheduler... cannot easily tag donors and partners when I post across FB, Insta, and LinkedIn..."
- **Supported Correction**: Role corrected to "Nonprofit marketing professional"; company to "nonprofit"; company_size to null; industry to "nonprofit"; icp to null (explicitly in-house nonprofit marketing); observation and interpretation updated to reflect in-house nonprofit context.
- **Unresolved Unknowns**: Nonprofit organization size and team structure.
- **Status**: DONE.

### mb-pain-018
- **Issue**: company_size held "agency" and icp held MULTIBRAND-OPERATOR-01 without headcount, ownership, or SMB proof.
- **Changed Fields**: `role`, `company_size`, `icp`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/graphic_design/comments/1aylev1/comment/krvpcjs/`, `FdINI`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment text: agency creative received scanned PDF in Word doc through several stakeholders, remade logo.
- **Supported Correction**: Role refined to "Design agency practitioner"; company_size and icp set to null; degraded asset observation and verbatim quote preserved.
- **Unresolved Unknowns**: Organization headcount, agency ownership, and client size.
- **Status**: DONE.

### mb-pain-019
- **Issue**: company_size held "freelancer / solo" and icp held MULTIBRAND-OPERATOR-01 without source basis.
- **Changed Fields**: `role`, `company_size`, `icp`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1w7wee3/comment/p7yha5i/`, `Summer_Macaroon`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment text: author rejected AI tools because fixing bad outputs took more time than manual creation.
- **Supported Correction**: Role refined to "Social media content practitioner"; company_size and icp set to null; AI editorial overhead contradiction preserved.
- **Unresolved Unknowns**: Organization size, employment vs freelance status, and client count.
- **Status**: DONE.

### mb-pain-020
- **Issue**: company_size held "solo / creator" and icp held MULTIBRAND-OPERATOR-01 without source basis.
- **Changed Fields**: `role`, `company_size`, `icp`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1tkbwzm/comment/onac80v/`, `heymae13`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment text: author experiences preview window aspect ratio mismatch vs live platform cropping.
- **Supported Correction**: Role refined to "Social media practitioner / publisher"; company_size and icp set to null; preview aspect ratio mismatch pain preserved.
- **Unresolved Unknowns**: Organization size, client count, and operational scope.
- **Status**: DONE.

### mb-pain-021
- **Issue**: Source URL was thread URL instead of comment permalink (`oui105w`); source date was 2026-07-02 instead of 2026-06-29; role ("Agency SMM Practitioner"), company_size ("agency"), and icp ("MULTIBRAND-OPERATOR-01") were unevidenced advisory assumptions.
- **Changed Fields**: `source_url`, `source_date`, `role`, `company_size`, `icp`, `observation`, `observed_at`.
- **Source URL & Exact Speaker**: `https://www.reddit.com/r/SocialMediaMarketing/comments/1uheu6p/comment/oui105w/` (resolved comment permalink), `Dry-College4773`.
- **Actual Inspection Date / Result**: 2026-09-09 / Live public page inspected via browser subagent. Verified comment ID `oui105w`, published 2026-06-29.
- **Supported Correction**: Resolved comment permalink; corrected source_date to 2026-06-29; role to "SMM practitioner / consultant"; company_size and icp to null; observation accurately records onboarding and revision limit guidance.
- **Unresolved Unknowns**: Author's specific agency affiliation, role, and client roster.
- **Status**: DONE.

---

## Summary of Changes
- **Total Checked IDs**: 21
- **Changed Records**: 21 (all 21 updated with audited observed_at, exact source fields, corrected comment permalinks, accurate roles, and removed unproven company_size/icp assertions)
- **Unchanged Records**: 0
- **Blocked Records**: 0 (all sources successfully reopened on live public pages)
- **Resolved Permalinks**:
  - `mb-pain-002`: `https://www.reddit.com/r/SocialMediaMarketing/comments/1ueutvu/comment/otqnc0d/`
  - `mb-pain-005`: `https://www.reddit.com/r/SocialMediaMarketing/comments/1ueutvu/comment/ouf4wov/`
  - `mb-pain-006`: `https://www.reddit.com/r/canva/comments/1rk9bj6/comment/o8kv01e/`
  - `mb-pain-011`: `https://www.reddit.com/r/SocialMediaMarketing/comments/1lx80ha/comment/n2su5nh/`
  - `mb-pain-016`: `https://www.reddit.com/r/graphic_design/comments/194g5un/comment/khj8mjo/`
  - `mb-pain-021`: `https://www.reddit.com/r/SocialMediaMarketing/comments/1uheu6p/comment/oui105w/`
- **Scope Baseline Audit Conclusion**: 0 of the 21 raw records had primary source proof meeting all requirements of `MULTIBRAND-OPERATOR-01` (external provider, plural client work, recurring static content, owner-operator with hands-on role, and explicit SMB clientele). All `icp` values have been corrected to null to prevent unevidenced scope upgrades upstream of Auditor/Judge.
