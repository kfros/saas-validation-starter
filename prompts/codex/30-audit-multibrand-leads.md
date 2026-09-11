# Independent Codex audit of the Multi-brand Stage 1.5 lead package

Use this in the existing Stage 1.5+ ChatGPT/Codex thread after the user provides
the commit containing sealed snapshot `mb-leads-v1-001`.

## Boundary

Audit the Antigravity-owned package. Do not modify `leads.jsonl`,
`source-register.jsonl`, `lead-research-report.md`, generated files, config or
snapshot. Do not send outreach, submit contact forms or book calls. Write only
reviewer artifacts under:

`ideas/multi-brand-content/stage1.5/lead-research/reviews/`

Read `AGENTS.md`, `methodology/stage1.5-lead-research.md`, the lead schema,
config, sealed snapshot and all package files. First run:

```bash
python scripts/stage15_leads.py check --idea multi-brand-content --require-final
```

The command is structural only. Independently inspect public pages with web
research; do not use terminal HTTP clients or Antigravity internal/cache files.

## Required audit coverage

1. Recompute organization-name/domain duplicates and all dataset/report totals.
2. Review every qualified lead. Re-open its official website, public business
   contact route and each decisive source used for hard qualification claims.
3. Check that exact fragments support the recorded claim without role,
   headcount, client, recurrence or service inference. Resolve source conflicts
   conservatively; an `11-50` range does not prove `<=20`.
4. Confirm that the organization is an active external agency, not software,
   in-house, inactive/rebranded, paid-ads-only or video-only; that the public
   owner identity is real; and that work for multiple client brands is shown.
5. Check every priority-A classification specifically for direct SMB-client and
   hands-on owner support. Unknown is acceptable for priority B but must remain a
   screening unknown.
6. Test all qualified public contact URLs without submitting anything. A page
   that loads but has no contact surface does not pass.
7. Review all report-cited holds, exclusions and analytical claims. Do not need
   to re-open an unmentioned excluded lead unless it affects a duplicate, total
   or claimed pattern.

Work in batches small enough to preserve reliable source attribution. Maintain:

- `codex-audit-state.json` — snapshot ID, reviewed qualified lead IDs, remaining
  IDs, blocked IDs and last checkpoint time;
- `codex-findings.jsonl` — one atomic finding with fields `finding_id`,
  `severity` (`BLOCKER`, `MAJOR`, `MINOR`, `NOTE`), `category` (`IDENTITY`,
  `DUPLICATE`, `SCOPE`, `SOURCE_SUPPORT`, `LINK`, `CONTACT`, `TOTAL`, `REPORT`),
  nullable `lead_id`, nullable `source_id`, exact `url`, `finding`,
  `required_action`, and `status: OPEN`;
- `codex-audit.md` — coverage, structural result, live-link result, findings,
  report accuracy and a clear `REPAIR_REQUIRED` or `READY_FOR_REPAIR_HANDOFF`
  conclusion.

Do not declare outreach-ready while any qualified lead has an unreviewed or
blocked decisive source/contact route. Commit only reviewer artifacts, report
the commit SHA and stop. Canonical repairs belong to Antigravity.
