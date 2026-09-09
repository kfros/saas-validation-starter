# Multi-Brand Content Production Engine: Stage 1 Evidence Audit Summary

**Idea ID**: `multi-brand-content`  
**Target Scope**: `MULTIBRAND-OPERATOR-01`  
**Baseline**: `4041943510d75728079d02606ade13a6c6d187d4`  
**Date of Audit**: 2026-09-09  
**Auditor**: Evidence Audit Agent (Decisive Live Browser Inspection via Chrome DevTools)  

---

## 1. Executive Summary & Inspection Completeness

This audit represents a fresh consolidation and verification of the current raw dataset following the repair of baseline 4041943. The audit evaluated all 80 raw evidence records collected across five research tracks:
- `market`: 21 records (`mb-market-001` through `mb-market-021`)
- `pain`: 21 records (`mb-pain-001` through `mb-pain-021`)
- `wtp`: 10 records (`mb-wtp-001` through `mb-wtp-010`)
- `workflow`: 14 records (`mb-workflow-001` through `mb-workflow-014`)
- `skeptic`: 14 records (`mb-skeptic-001` through `mb-skeptic-014`)

### Source Inspection Protocol & Completeness
- **Inspection Coverage**: 100% of all 80 records (66 unique source URLs) were directly inspected in a live browser session via Chrome DevTools.
- **Pending Records**: Exactly **0** records are marked `PENDING`. No rate limits, HTTP 429 errors, browser failures, or tool exhaustion events prevented verification.
- **Audit Outcomes**:
  - **VERIFIED**: 65 records (81.25%)
  - **PARTIALLY_VERIFIED**: 9 records (11.25%)
  - **REJECTED**: 6 records (7.5%) — all 6 are dead documentation links returning HTTP 404 (`mb-market-001`, `004`, `005`, `006`, `011`, `012`).
  - **PENDING**: 0 records (0.0%)

### Notice Regarding Historical Output Artifacts
> [!WARNING]
> The existing artifacts in `ideas/multi-brand-content/output/` (`stage1-report.md` and `scorecard.json`) describe baseline `4041943`. They are historical and stale with respect to this repaired dataset. In accordance with `repair-4041943/repair-tasks.md` and workspace rules, this audit does not launch Stage 1 Judge, does not modify `output/`, and does not issue a Stage 1 gate verdict.

---

## 2. Independence Key & Entity Deduplication

To prevent artificial inflation of demand signals, entities appearing multiple times across tracks were normalized to canonical `independence_key` identifiers:
- `vendor-canva`: Canva official documentation and pricing across tracks (`mb-market-001`..`004`, `mb-skeptic-001`..`003`).
- `vendor-planable`: Planable official documentation and pricing across tracks (`mb-market-008`..`010`, `mb-skeptic-004`..`005`).
- `reddit-user-prudent-bad-8786`: Linked practitioner incident (`mb-pain-015` and `mb-skeptic-006` share the same small agency event where an outdated Canva visual was published to a live client account).
- `reddit-user-k_rocker`: Linked practitioner workflow (`mb-pain-011` and `mb-skeptic-013` share the same agency observation regarding Canva template sharing with clients).
- `reddit-user-broad-perspective166`: Linked practitioner workflow (`mb-wtp-004` and `mb-workflow-004` share the same observation regarding Planable usage and workspace pricing friction across 5 clients).
- `meaningfulsocialclub`: Boutique owner-led agency The Meaningful Social Club / Natalie Lasance (`mb-workflow-006`, `007`, `008`).
- `sugarpunchmarketing`: Boutique owner-led agency Sugarpunch Marketing / Shanté Gorman (`mb-workflow-009`, `010`, `011`).
- `blahblahsocial`: Agency Blah Blah Social (`mb-workflow-012`, `013`, `014`).

---

## 3. Dataset Summary

The tables below reflect the audited dataset counts:

### Overall Audit Status Breakdown
| Audit Status | Record Count | Percentage |
| :--- | :--- | :--- |
| **VERIFIED** | 65 | 81.25% |
| **PARTIALLY_VERIFIED** | 9 | 11.25% |
| **REJECTED** | 6 | 7.50% |
| **PENDING** | 0 | 0.00% |
| **Total Records** | **80** | **100.0%** |

```json
DATASET_SUMMARY={"by_audit_status": {"PARTIALLY_VERIFIED": 9, "PENDING": 0, "REJECTED": 6, "VERIFIED": 65}, "by_provider_form": {"AGENCY": {"records": 28, "verified_independence_keys": 17, "verified_records": 25}, "SOLO": {"records": 6, "verified_independence_keys": 5, "verified_records": 5}, "UNKNOWN": {"records": 46, "verified_independence_keys": 26, "verified_records": 35}}, "by_scope": {"IN_SCOPE": {"records": 6, "verified_independence_keys": 2, "verified_records": 6}, "OUT_OF_SCOPE": {"records": 31, "verified_independence_keys": 15, "verified_records": 23}, "UNKNOWN": {"records": 43, "verified_independence_keys": 31, "verified_records": 36}}, "total_records": 80, "verified_independence_keys": 48}
```

### Breakdown by Scope Status (`MULTIBRAND-OPERATOR-01`)
| Scope Status | Total Records | Verified Records | Verified Independence Keys |
| :--- | :--- | :--- | :--- |
| **IN_SCOPE** | 6 | 6 | 2 |
| **OUT_OF_SCOPE** | 31 | 23 | 15 |
| **UNKNOWN** | 43 | 36 | 31 |
| **Total** | **80** | **65** | **48** |

### Breakdown by Provider Form
| Provider Form | Total Records | Verified Records | Verified Independence Keys |
| :--- | :--- | :--- | :--- |
| **AGENCY** | 28 | 25 | 17 |
| **SOLO** | 6 | 5 | 5 |
| **UNKNOWN** | 46 | 35 | 26 |
| **Total** | **80** | **65** | **48** |

---

## 4. Complete URL and Record Inspection Ledger

The complete ledger of all 80 audited records across the five research tracks:

| ID | Track | Source URL | Actual Inspection Finding | Audit Status | Scope Status | Provider Form | Independence Key |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `mb-market-001` | market | `https://www.canva.com/help/article/brand-kit/` | HTTP 404 Not Found (dead URL) | REJECTED | OUT_OF_SCOPE | UNKNOWN | vendor-canva |
| `mb-market-002` | market | `https://www.canva.com/help/magic-switch/` | Live docs; batch resize exists, but brand kit multi-tenant isolation overclaimed | PARTIALLY_VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-canva |
| `mb-market-003` | market | `https://www.canva.com/pricing/` | Live pricing; Teams $100/yr for 3 seats, enterprise brand controls separate | PARTIALLY_VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-canva |
| `mb-market-004` | market | `https://www.canva.com/help/article/brand-controls/` | HTTP 404 Not Found (dead URL) | REJECTED | OUT_OF_SCOPE | UNKNOWN | vendor-canva |
| `mb-market-005` | market | `https://www.adobe.com/express/features/brand-kit` | HTTP 404 Not Found (dead URL) | REJECTED | OUT_OF_SCOPE | UNKNOWN | vendor-adobe |
| `mb-market-006` | market | `https://www.adobe.com/express/pricing` | HTTP 404 Not Found (dead URL) | REJECTED | OUT_OF_SCOPE | UNKNOWN | vendor-adobe |
| `mb-market-007` | market | `https://www.kontentino.com/pricing/` | Live pricing; Starter €49/mo (3 users/10 profiles), Pro €99/mo | VERIFIED | OUT_OF_SCOPE | UNKNOWN | mb-market-007 |
| `mb-market-008` | market | `https://planable.io/features/multi-brand/` | Live docs; multi-workspace client brand separation documented | VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-planable |
| `mb-market-009` | market | `https://planable.io/features/approvals/` | Live docs; multi-tier client approval workflow documented | VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-planable |
| `mb-market-010` | market | `https://planable.io/pricing/` | Live pricing; Basic $33/workspace/mo, Pro $67/workspace/mo | VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-planable |
| `mb-market-011` | market | `https://buffer.com/features/multi-account` | HTTP 404 Not Found (dead URL) | REJECTED | OUT_OF_SCOPE | UNKNOWN | vendor-buffer |
| `mb-market-012` | market | `https://buffer.com/features/drafts-approvals` | HTTP 404 Not Found (dead URL) | REJECTED | OUT_OF_SCOPE | UNKNOWN | vendor-buffer |
| `mb-market-013` | market | `https://buffer.com/pricing` | Live pricing; Essentials $6/channel/mo, Team $12/channel/mo | VERIFIED | OUT_OF_SCOPE | UNKNOWN | mb-market-013 |
| `mb-market-014` | market | `https://buffer.com/resources/social-media-approval-workflow/` | Live blog guide; draft review workflows for social agencies documented | VERIFIED | OUT_OF_SCOPE | UNKNOWN | mb-market-014 |
| `mb-market-015` | market | `https://predis.ai/pricing/` | Live pricing; Solo $29/mo, Starter $49/mo (2 brands), Agency $119/mo (7 brands) | VERIFIED | OUT_OF_SCOPE | UNKNOWN | mb-market-015 |
| `mb-market-016` | market | `https://predis.ai/features/ecommerce-social-media/` | Live docs; automated catalog-to-social post generation documented | VERIFIED | OUT_OF_SCOPE | UNKNOWN | mb-market-016 |
| `mb-market-017` | market | `https://www.abyssale.com/features/dynamic-templates` | Live docs; dynamic template generation via spreadsheet/API documented | VERIFIED | OUT_OF_SCOPE | UNKNOWN | mb-market-017 |
| `mb-market-018` | market | `https://www.abyssale.com/features/batch-generation` | Live docs; batch graphic generation from structured data documented | VERIFIED | OUT_OF_SCOPE | UNKNOWN | mb-market-018 |
| `mb-market-019` | market | `https://www.abyssale.com/pricing` | Live pricing; Essential €39/mo, Advanced €79/mo (5 templates), Pro €199/mo | VERIFIED | OUT_OF_SCOPE | UNKNOWN | mb-market-019 |
| `mb-market-020` | market | `https://www.bannerbear.com/features/template-editor/` | Live docs; automated image generation via API/integrations documented | VERIFIED | OUT_OF_SCOPE | UNKNOWN | mb-market-020 |
| `mb-market-021` | market | `https://www.bannerbear.com/pricing/` | Live pricing; Automate $49/mo (1,000 credits), Scale $149/mo | VERIFIED | OUT_OF_SCOPE | UNKNOWN | mb-market-021 |
| `mb-pain-001` | pain | `https://www.reddit.com/r/marketing/comments/1iws6g1/managing_12_social_media_accounts_across_3/` | Live post; 12 accounts across 3 agency clients, brand asset drift verified | VERIFIED | UNKNOWN | AGENCY | reddit-marketing-001 |
| `mb-pain-002` | pain | `https://www.reddit.com/r/freelance/comments/1h8c9xy/how_do_you_handle_client_revisions_on_social/` | Live post; solo freelancer batch revision friction verified | VERIFIED | UNKNOWN | SOLO | reddit-freelance-001 |
| `mb-pain-003` | pain | `https://www.reddit.com/r/socialmedia/comments/1gyh511/canva_brand_kit_mess_with_multiple_clients/` | Live post; multi-client brand kit confusion in Canva verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-socialmedia-001 |
| `mb-pain-004` | pain | `https://www.reddit.com/r/web_design/comments/1fp881m/client_keeps_asking_for_asset_variations/` | Live post; solo web designer graphic updates across clients verified | VERIFIED | OUT_OF_SCOPE | SOLO | reddit-web-design-001 |
| `mb-pain-005` | pain | `https://www.reddit.com/r/agency/comments/1fq6i4a/client_review_bottleneck_is_killing_our_margins/` | Live post; agency review bottleneck and Canva export mismatches verified | VERIFIED | UNKNOWN | AGENCY | reddit-agency-001 |
| `mb-pain-006` | pain | `https://www.reddit.com/r/socialmedia/comments/1f4kmh9/client_asset_organization_nightmare/` | Live post; asset disorganization and missing fonts across 5 brands verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-socialmedia-002 |
| `mb-pain-007` | pain | `https://www.reddit.com/r/freelance/comments/1ex73w1/how_do_you_keep_brand_assets_organized_for/` | Live post; template propagation delays across 4 accounts verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-freelance-002 |
| `mb-pain-008` | pain | `https://www.reddit.com/r/socialmedia/comments/1edsp2o/client_approval_process_is_broken/` | Live post; multi-client approval delays in spreadsheets verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-socialmedia-003 |
| `mb-pain-009` | pain | `https://www.reddit.com/r/SocialMediaMarketing/comments/1lx80ha/how_do_you_deliver_monthly_social_media_posts_to/` | Live post; Ok-Guitar4196 small agency employee monthly batch delivery verified | VERIFIED | UNKNOWN | AGENCY | reddit-smm-okguitar4196 |
| `mb-pain-010` | pain | `https://www.reddit.com/r/freelance/comments/1dkx3i8/carousel_reformatting_is_eating_my_weekends/` | Live post; solo freelancer carousel reformatting across 3 clients verified | VERIFIED | UNKNOWN | SOLO | reddit-freelance-003 |
| `mb-pain-011` | pain | `https://www.reddit.com/r/SocialMediaMarketing/comments/1djv7k5/how_do_you_handle_client_design_templates/` | Live post; k_rocker agency Canva template sharing verified | VERIFIED | UNKNOWN | AGENCY | reddit-user-k_rocker |
| `mb-pain-012` | pain | `https://www.reddit.com/r/agency/comments/1d4lwhk/brand_consistency_across_multiple_retainer_clients/` | Live post; agency brand asset drift across client retainers verified | VERIFIED | UNKNOWN | AGENCY | reddit-agency-002 |
| `mb-pain-013` | pain | `https://www.reddit.com/r/socialmedia/comments/1cqsm73/accidental_wrong_brand_post_nightmare/` | Live post; accidental cross-posting / wrong asset upload verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-socialmedia-004 |
| `mb-pain-014` | pain | `https://www.reddit.com/r/freelance/comments/1c6s0r7/propagating_client_logo_updates_across_a_whole/` | Live post; client logo revision propagation across static batch verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-freelance-004 |
| `mb-pain-015` | pain | `https://www.reddit.com/r/SocialMediaMarketing/comments/1vlj75n/published_a_client_post_with_an_old_visual/` | Live post; Prudent-Bad-8786 small agency 6 clients published outdated PNG verified | VERIFIED | UNKNOWN | AGENCY | reddit-user-prudent-bad-8786 |
| `mb-pain-016` | pain | `https://www.reddit.com/r/agency/comments/1buhx69/review_latency_on_carousel_posts_is_out_of_control/` | Live post; agency review latency on carousel drafts across 10 clients verified | VERIFIED | UNKNOWN | AGENCY | reddit-agency-003 |
| `mb-pain-017` | pain | `https://www.reddit.com/r/nonprofit/comments/1beo7c5/managing_social_assets_for_5_internal_programs/` | Live post; in-house nonprofit communications staff internal program assets | VERIFIED | OUT_OF_SCOPE | UNKNOWN | reddit-nonprofit-001 |
| `mb-pain-018` | pain | `https://www.reddit.com/r/agency/comments/1avd07m/asset_collection_from_clients_is_the_worst_part/` | Live post; agency multi-client asset collection bottlenecks verified | VERIFIED | UNKNOWN | AGENCY | reddit-agency-004 |
| `mb-pain-019` | pain | `https://www.reddit.com/r/socialmedia/comments/1ag6c1h/static_banner_revision_hell/` | Live post; revision cycles for static banners across 4 clients verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-socialmedia-005 |
| `mb-pain-020` | pain | `https://www.reddit.com/r/freelance/comments/197cqlu/exporting_and_renaming_assets_for_5_clients/` | Live post; manual export and asset renaming across 5 clients verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-freelance-005 |
| `mb-pain-021` | pain | `https://www.reddit.com/r/agency/comments/18z7g9t/client_approval_of_static_grids_taking_2_weeks/` | Live post; agency client approval delay on static grids verified | VERIFIED | UNKNOWN | AGENCY | reddit-agency-005 |
| `mb-wtp-001` | wtp | `https://www.reddit.com/r/canva/comments/1oqdoe9/business_vs_enterprise_for_managing_multiple/` | Live post; New-Activity-8659 paying $300/yr Canva Teams legacy, refused Enterprise | PARTIALLY_VERIFIED | UNKNOWN | UNKNOWN | reddit-smm-001 |
| `mb-wtp-002` | wtp | `https://www.reddit.com/r/canva/comments/1oqdoe9/business_vs_enterprise_for_managing_multiple/` | Live post; agency designer intent to pass Canva Business fees to clients | PARTIALLY_VERIFIED | UNKNOWN | AGENCY | reddit-smm-002 |
| `mb-wtp-003` | wtp | `https://www.reddit.com/r/SocialMediaMarketing/comments/ycgaw2/should_i_pay_for_a_clients_later_subscription/` | Live post; NikiforovAleksandr $200 Postmypost 100 accounts, period unstated | PARTIALLY_VERIFIED | UNKNOWN | UNKNOWN | reddit-smm-003 |
| `mb-wtp-004` | wtp | `https://www.reddit.com/r/SocialMediaMarketing/comments/1m7dkeb/what_platform_do_you_use_for_client_approvals_on/` | Live post; Broad_Perspective166 Planable 5 clients, price friction verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-user-broad-perspective166 |
| `mb-wtp-005` | wtp | `https://www.reddit.com/r/canva/comments/1g0pcdg/too_little_too_late_lol/` | Live post; josh_moworld single-brand business paid $100/yr Express + $150 Affinity | VERIFIED | OUT_OF_SCOPE | SOLO | reddit-user-josh_moworld |
| `mb-wtp-006` | wtp | `https://www.reddit.com/r/SocialMediaMarketing/comments/1ixclwe/how_much_to_pay_social_media_manager_contractors/` | Live post; Internal_Heat_8471 paid contractor $1,500/mo, bundled scope | PARTIALLY_VERIFIED | UNKNOWN | AGENCY | reddit-smm-004 |
| `mb-wtp-007` | wtp | `https://www.reddit.com/r/SocialMediaMarketing/comments/1ixclwe/how_much_to_pay_social_media_manager_contractors/` | Live post; Social_Savvy_Pro advisory rate guidance $400-$800/mo contractor | PARTIALLY_VERIFIED | UNKNOWN | AGENCY | reddit-smm-007 |
| `mb-wtp-008` | wtp | `https://www.reddit.com/r/SocialMediaMarketing/comments/1hlh20d/am_i_handling_too_many_accounts/` | Live post; Marketing_Maven_99 agency employee 30+ hrs/wk on 5 accounts | VERIFIED | UNKNOWN | AGENCY | reddit-smm-005 |
| `mb-wtp-009` | wtp | `https://www.reddit.com/r/SocialMediaMarketing/comments/14zvgln/how_long_does_it_take_for_you_to_make_30_days/` | Live post; Creative_Solo_88 spends 8-10 hrs/client batch, monthly total unstated | PARTIALLY_VERIFIED | UNKNOWN | SOLO | reddit-smm-006 |
| `mb-wtp-010` | wtp | `https://www.reddit.com/r/SocialMediaMarketing/comments/kti4jk/is_it_legal_to_use_canva_as_part_of_your_social/` | Live post; advisory forum comment regarding Canva Free for client work | PARTIALLY_VERIFIED | UNKNOWN | UNKNOWN | reddit-smm-010 |
| `mb-workflow-001` | workflow | `https://www.reddit.com/r/SocialMediaMarketing/comments/1m7dkeb/what_platform_do_you_use_for_client_approvals_on/` | Live post; agency practitioner using Planable for multi-client approvals | VERIFIED | UNKNOWN | AGENCY | reddit-workflow-001 |
| `mb-workflow-002` | workflow | `https://www.reddit.com/r/SocialMediaMarketing/comments/1m7dkeb/what_platform_do_you_use_for_client_approvals_on/` | Live post; practitioner using Google Drive/Sheets for client approval flow | VERIFIED | UNKNOWN | UNKNOWN | reddit-workflow-002 |
| `mb-workflow-003` | workflow | `https://www.reddit.com/r/SocialMediaMarketing/comments/1m7dkeb/what_platform_do_you_use_for_client_approvals_on/` | Live post; agency practitioner using Notion client portals for approval | VERIFIED | UNKNOWN | AGENCY | reddit-workflow-003 |
| `mb-workflow-004` | workflow | `https://www.reddit.com/r/SocialMediaMarketing/comments/1m7dkeb/what_platform_do_you_use_for_client_approvals_on/` | Live post; Broad_Perspective166 Planable workflow across 5 clients verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-user-broad-perspective166 |
| `mb-workflow-005` | workflow | `https://postflow.io/` | Live product landing page; social approval software vendor | VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-postflow |
| `mb-workflow-006` | workflow | `https://www.themeaningfulsocialclub.com/services` | Live site; TMSC monthly social retainers for lifestyle SMB brands verified | VERIFIED | IN_SCOPE | AGENCY | meaningfulsocialclub |
| `mb-workflow-007` | workflow | `https://www.themeaningfulsocialclub.com/about` | Live site; Natalie Lasance founder/creative director hands-on role verified | VERIFIED | IN_SCOPE | AGENCY | meaningfulsocialclub |
| `mb-workflow-008` | workflow | `https://www.themeaningfulsocialclub.com/contact` | Live site; direct agency booking and client inquiry channel verified | VERIFIED | IN_SCOPE | AGENCY | meaningfulsocialclub |
| `mb-workflow-009` | workflow | `https://www.sugarpunchmarketing.com/services` | Live site; Sugarpunch monthly static/carousel retainers for SMBs verified | VERIFIED | IN_SCOPE | AGENCY | sugarpunchmarketing |
| `mb-workflow-010` | workflow | `https://www.sugarpunchmarketing.com/about` | Live site; Shanté Gorman owner hands-on creative lead verified | VERIFIED | IN_SCOPE | AGENCY | sugarpunchmarketing |
| `mb-workflow-011` | workflow | `https://www.sugarpunchmarketing.com/contact` | Live site; direct retainer onboarding and inquiry form verified | VERIFIED | IN_SCOPE | AGENCY | sugarpunchmarketing |
| `mb-workflow-012` | workflow | `https://blahblahsocial.com/services` | Live site; social media agency multi-client management packages verified | VERIFIED | UNKNOWN | AGENCY | blahblahsocial |
| `mb-workflow-013` | workflow | `https://blahblahsocial.com/about` | Live site; agency team profile without explicit founder hands-on production | VERIFIED | UNKNOWN | AGENCY | blahblahsocial |
| `mb-workflow-014` | workflow | `https://blahblahsocial.com/contact` | Live site; agency direct inquiry form verified | VERIFIED | UNKNOWN | AGENCY | blahblahsocial |
| `mb-skeptic-001` | skeptic | `https://www.canva.com/help/brand-kit/` | Live docs; Canva Brand Kit management capabilities verified | VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-canva |
| `mb-skeptic-002` | skeptic | `https://www.canva.com/help/share-templates/` | Live docs; Canva shared template link collaboration verified | VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-canva |
| `mb-skeptic-003` | skeptic | `https://www.canva.com/help/magic-switch/` | Live docs; Magic Switch batch reformat capabilities verified | VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-canva |
| `mb-skeptic-004` | skeptic | `https://planable.io/features/workspaces/` | Live docs; Planable multi-workspace setup and workspace costs verified | VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-planable |
| `mb-skeptic-005` | skeptic | `https://planable.io/features/approvals/` | Live docs; Planable approval workflows and audit trails verified | VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-planable |
| `mb-skeptic-006` | skeptic | `https://www.reddit.com/r/SocialMediaMarketing/comments/1vlj75n/published_a_client_post_with_an_old_visual/` | Live post; Prudent-Bad-8786 small agency 6 clients versioning error verified | VERIFIED | UNKNOWN | AGENCY | reddit-user-prudent-bad-8786 |
| `mb-skeptic-007` | skeptic | `https://www.reddit.com/r/freelance/comments/1h8c9xy/how_do_you_handle_client_revisions_on_social/` | Live post; solo practitioner finds Canva Pro completely adequate verified | VERIFIED | UNKNOWN | SOLO | reddit-skeptic-001 |
| `mb-skeptic-008` | skeptic | `https://www.reddit.com/r/SocialMediaMarketing/comments/1b3u2i9/does_anyone_actually_spend_most_of_their_time/` | Live post; Unable-Connection-58 40% time spent communicating/chasing verified | VERIFIED | UNKNOWN | AGENCY | reddit-skeptic-002 |
| `mb-skeptic-009` | skeptic | `https://www.reddit.com/r/socialmedia/comments/1ag6c1h/static_banner_revision_hell/` | Live post; Carey251 prefers native Figma/Canva workflows over tools verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-skeptic-003 |
| `mb-skeptic-010` | skeptic | `https://www.reddit.com/r/agency/comments/18z7g9t/client_approval_of_static_grids_taking_2_weeks/` | Live post; practitioner client resistance to new portal login verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-skeptic-004 |
| `mb-skeptic-011` | skeptic | `https://www.reddit.com/r/SocialMediaMarketing/comments/1m7dkeb/what_platform_do_you_use_for_client_approvals_on/` | Live post; TheGentleAnimal client-side review latency true bottleneck verified | VERIFIED | UNKNOWN | AGENCY | reddit-skeptic-005 |
| `mb-skeptic-012` | skeptic | `https://www.reddit.com/r/SocialMediaMarketing/comments/1m7dkeb/what_platform_do_you_use_for_client_approvals_on/` | Live post; unmethodicals Canva template links sufficient with clients verified | VERIFIED | UNKNOWN | UNKNOWN | reddit-skeptic-006 |
| `mb-skeptic-013` | skeptic | `https://www.reddit.com/r/SocialMediaMarketing/comments/1djv7k5/how_do_you_handle_client_design_templates/` | Live post; k_rocker agency Canva template links sufficient verified | VERIFIED | UNKNOWN | AGENCY | reddit-user-k_rocker |
| `mb-skeptic-014` | skeptic | `https://juicer.io/blog/social-media-workflow-bottlenecks/` | Live blog; JuicerSocial vendor blog on social workflow bottlenecks | VERIFIED | OUT_OF_SCOPE | UNKNOWN | vendor-juicersocial |

---
*End of Audit Summary.*
