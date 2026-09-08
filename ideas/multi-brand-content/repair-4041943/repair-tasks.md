# Evidence repair tasks — baseline 4041943

Baseline: 4041943510d75728079d02606ade13a6c6d187d4.
This file records an independent review and instructions for a bounded repair.
It is not primary evidence, a new audit, a new scope or a Stage 1 verdict.
Reopen original public pages before changing a source-dependent fact.

This pass repairs source fidelity and finishes Workflow. The current hypothesis,
scope-map contract, gates and checker remain the evaluation baseline. A later
methodology revision may separately change admission to interviews; it is not part
of this repair. No improved verdict or IN_SCOPE count is promised.

## Shared repair requirements

1. Preserve all existing raw IDs, including a source that is still blocked or
   ultimately unsuitable. Raw records remain PENDING. Do not delete/reseed files.
2. A researcher may correct their own source fields after reopening the page.
   The Auditor may change only audit_status, audit_reason and independence_key.
3. Check observation, interpretation, source_excerpt, author, role, company_size,
   icp, recurrence, money fields and source dates together. Fix dependent claims
   in the owned Markdown reports; a corrected JSONL with an old inflated report
   is an incomplete repair.
4. source_excerpt is an exact short extract from the attributed speaker, or null.
   Do not present a rewritten list, summary, arithmetic or merged comments as a
   quotation. Put paraphrases in observation. Preserve comment identity in URLs.
5. Unknown payment is not zero payment; unknown price/period/currency remains null
   or the existing schema's appropriate unknown value. Never calculate a monthly
   price from a purchase whose billing period is unknown.
6. company_size is organizational size, not number of client accounts. A known
   small agency can stay "small agency"; unknown size stays null. Client counts
   may appear in the supported observation. Do not infer employee/owner identity.
7. icp: MULTIBRAND-OPERATOR-01 is not justified merely because the run studies it.
   Use a source-supported broader role/segment or null when full membership is
   unknown. Separate profile records can later support explicit same-entity
   linkage in scope-map; they do not silently amend the original source.
8. Retain supported pain and contrary facts. This is not a search for a PASS.
9. Every repair conversation writes repair-log.md in its own raw directory:
   ID; issue; changed fields; source URL and attributed speaker; actual inspection
   date/result; corrected supported fact; remaining unknown; DONE or BLOCKED.
   Include unchanged-but-checked records and new IDs. Logs are accountability,
   never substitutes for original public source verification.
10. If the page cannot be inspected, do not repair from this task list or memory.
    Preserve the existing PENDING raw row, mark the task BLOCKED in repair-log.md
    and explain the unresolved overclaim. Auditor must not carry its old VERIFIED
    status forward blindly.
11. Record any newly discovered material error in the owned track's log and
    correct it only from its reopened source. No global refactor or new discovery
    outside the explicit task. All writers finish before audit begins.

## A — WTP owner: review all ten existing WTP records

Priority source URLs and review findings:

| IDs | Review finding / required action |
| --- | --- |
| mb-wtp-009 | The source gives task-level timing, not a stated 25–45+ monthly hours/client total. Its excerpt in raw is a constructed summary. Remove unsupported monthly totals and "1+ hour per carousel"; use the exact timing distinctions the source makes. Check whether solo-owner, client count, payment and monthly recurrence are actually established; do not infer them from the thread title. |
| mb-wtp-010 | The source recommends Canva for client work and mentions a free version. This does not establish the speaker's actual free-plan use, avoidance of paid tools, retention or refusal to pay. Remove the unsupported behavioral/WTP conclusion and free_tier_retention subtype. Record only supported advice/capability context; no current legal conclusion from an old forum reply. |
| mb-wtp-004 | The recorded complaint establishes Planable use and price dissatisfaction, not paid use or a billing period. Repair money classification and the interpretation claiming active spending. Keep the useful price-friction observation if supported. |
| mb-wtp-007 | The $400–$800 / $20–$40 discussion and $600 example are recommendations/illustrative arithmetic, not the author's proven contractor expense. Do not retain $600 as actual spend. Preserve the supported advisory context without treating it as personal stated WTP or an awarded budget. |
| mb-wtp-006 | Actual $1,500/month subcontracting is supported in the reviewed thread, alongside later abandonment. The package also includes filming, editing and posting. Preserve that full scope and its unknown static-production allocation. Do not generalize one failed arrangement into "human subcontracting fails." |
| mb-wtp-008 | company_size contains "5 accounts" and subtype claims owner_operator_time while the record describes an agency content operator. Separate clients from team size; confirm actual role. Preserve the mixture of static/reels/shooting labor and avoid attributing all effort to static production. |
| mb-wtp-001 | A legacy paid-plan statement is not proof that all available brand kits are used, that the payer matches the target ICP, or that the plan is bought specifically for our exact job. Preserve the stated historical payment and qualify job/scope mapping. |
| mb-wtp-003 | $200 for 100 accounts does not establish $2/client/month if billing period is unknown. Scheduling spend is adjacent to static production. Remove the inferred monthly price and any universal WTP ceiling. |
| mb-wtp-002, mb-wtp-005 | Recheck identity, scope and interpretation alongside the other rows. Planned purchase remains intent; one person's switching choice does not establish a universal market price ceiling. |

Original pages already present in raw:

- mb-wtp-001/002: https://www.reddit.com/r/canva/comments/1oqdoe9/business_vs_enterprise_for_managing_multiple/
- mb-wtp-003: https://www.reddit.com/r/SocialMediaMarketing/comments/ycgaw2/should_i_pay_for_a_clients_later_subscription/
- mb-wtp-004: https://www.reddit.com/r/SocialMediaMarketing/comments/1m7dkeb/what_platform_do_you_use_for_client_approvals_on/
- mb-wtp-005: https://www.reddit.com/r/canva/comments/1g0pcdg/too_little_too_late_lol/
- mb-wtp-006/007: https://www.reddit.com/r/SocialMediaMarketing/comments/1ixclwe/how_much_to_pay_social_media_manager_contractors/
- mb-wtp-008: https://www.reddit.com/r/SocialMediaMarketing/comments/1hlh20d/am_i_handling_too_many_accounts/
- mb-wtp-009: https://www.reddit.com/r/SocialMediaMarketing/comments/14zvgln/how_long_does_it_take_for_you_to_make_30_days/
- mb-wtp-010: https://www.reddit.com/r/SocialMediaMarketing/comments/kti4jk/is_it_legal_to_use_canva_as_part_of_your_social/

These are pointers, not preapproved replacements or guaranteed available pages.
Use exact comment permalinks only when obtained from the original public page.

## B — Pain owner: correct mb-pain-015; check material attribution across own track

mb-pain-015: original post states "Small agency, 6 clients." It reports an actual
outdated PNG publication after a Canva edit. It does not explicitly establish
SMB clientele or hands-on ownership. Remove unsupported SMB attribution and the
company_size value "6 SMB clients". Keep the actual version/handoff failure.

Source:
https://www.reddit.com/r/SocialMediaMarketing/comments/1vlj75n/published_a_client_post_with_an_old_visual/

mb-pain-009: preserve the small-agency employee's actual monthly production and
formatting/revision problems. The evidence need not be deleted because buyer
authority is unknown. Do not relabel an employee as owner to make scope pass.

Source:
https://www.reddit.com/r/SocialMediaMarketing/comments/1lx80ha/how_do_you_deliver_monthly_social_media_posts_to/

Recheck the remaining existing pain rows for the same unsupported icp/role/size
upgrades and for advice promoted into experience. No new pain collection or quota.
Only change source-dependent fields after inspecting their original pages. Exact
broad facts can remain with unknown target-scope membership.

## C — Skeptic owner: repair attribution and bound conclusions

mb-skeptic-006 uses the same agency event as mb-pain-015. Remove unsupported
"owner/operator" status and any headcount inferred from six clients. Replace the
rewritten source_excerpt with an exact short extract or null. Keep the real
incident and its shared underlying entity key.

mb-skeptic-011: the cited discussion concerns a short-form agency. Its comment
describes client-side friction and Trello use; it does not by itself falsify
static content production for every owner-led SMM provider. Preserve the source
context and limited mapping instead of a universal bottleneck conclusion.

mb-skeptic-012/013: actual collaborative-link/shared-template satisfaction is
useful contrary evidence. Do not upgrade one team's preference into "low market
desire", a universal format requirement or complete substitute sufficiency.

mb-skeptic-008: the page could not be reopened in the independent spot-check.
That failure alone is not proof the source is false. Reopen it, verify the exact
speaker, quoted 40% figure and causal/agency claims; if still blocked, log BLOCKED
and do not claim a fresh verification.

Check all own existing skeptic rows for icp/role/size attribution, source_excerpt
fidelity and inferred market-wide price ceilings. Keep current official capability
separate from paid adoption and sufficient quality. No new substitute discovery
in this repair conversation.

## D — Workflow owner: repair the partial report and finish missing coverage

Baseline: raw/workflow/run-status.json says PARTIAL because search/browser tools
failed. All five existing rows use one Reddit thread:
https://www.reddit.com/r/SocialMediaMarketing/comments/1m7dkeb/what_platform_do_you_use_for_client_approvals_on/

Recheck each speaker separately. Determine firsthand operator use versus a seller's
recommendation. Repair mb-workflow-004's paid-use implication just as the WTP owner
repairs mb-wtp-004; preserve the independent ownership of both raw files.

Remove unsupported "typical" client ranges (3–8, 8–25), 1–5/2–5 employee assumptions,
buyer behavior, native-editable-output conclusions and HIGH reachability claims.
Do not merely re-label an invented table as "research findings." Proposed questions
may be retained in a clearly marked hypotheses section.

Then resume the missing source families:

- Original public service/portfolio pages showing actual external social-content work.
- Team/about/founder workflow pages and named practitioner process descriptions.
- Public contact/directory surfaces for plausible buyer discovery.
- Explicit recurrence and editable/review/handoff requirements from firsthand sources.

Investigate a small illustrative set of providers, aiming for 3–5 only if the
sources support it. This is a search guide, not a quota or proof of market size.
Record every scope attribute separately as SUPPORTED / UNKNOWN / CONTRADICTED
with evidence IDs in the Markdown coverage matrix. Preserve the canonical
scope-map schema for the Auditor; do not invent new JSONL fields.

New provider profiles may support reachability for themselves. They cannot supply
missing size/ownership/SMB facts for an unrelated anonymous Reddit author.
Use same-entity linkage only when explicitly established by public self-identification.
Do not attempt to deanonymize practitioners.

Keep each new atomic profile/workflow/reachability fact in a raw record with its
own original source_url. Append stable mb-workflow- IDs; never renumber existing IDs.
Preserve one entity independence key across that provider's profile records.

A legitimate public business contact surface is enough for reachability evidence;
no outreach, personal-email harvesting, account creation or full Stage 2 list.
If tools still fail, preserve PARTIAL and state the exact missing research.

## E — Auditor: fresh consolidation and priority source verification

Use current raw after all four writers finish. Prioritize:

1. Every changed/new record in repair-log.md and all BLOCKED tasks.
2. Every WTP row; every other monetary row and old PARTIALLY_VERIFIED money claim.
3. mb-pain-009/015, mb-skeptic-006/008/011/012/013 and linked duplicates.
4. New Workflow sources, scope support links and declared reachability.
5. All official/practitioner sources used for decisive substitute claims.

Inspect all consolidated records for semantic/provenance integrity. Reopen the
remaining originals too before claiming a complete fresh audit: the baseline
Auditor let material overclaims through, so old VERIFIED labels and source excerpts
are not sufficient evidence for carrying status forward without checking.

Record reinspection date/status per record or URL-to-ID group. A quota/budget/tool
interruption yields PARTIAL with uninspected rows PENDING and no declaration of
complete source verification. Do not use old snippets/cache/internal artifacts.

If a market source is unavailable or the exact URL is wrong, the Auditor records
the appropriate unsupported/blocked result and a precise follow-up for Market;
the Auditor never discovers replacement URLs or silently repairs raw.

## What completion means

Repair completion means source-faithful current raw, an honest Workflow coverage
report/status and a newly checked audited dataset with reproducible counts.
Zero or few IN_SCOPE records remain possible under the unchanged scope contract.
No one may rewrite facts or relax scope merely to avoid UNKNOWN.

The existing output/stage1-report.md and scorecard.json describe baseline 4041943.
After raw/audit changes they are historical and stale for the current dataset.
Do not refresh or cite them as current in this pass; no Judge launch is included.
