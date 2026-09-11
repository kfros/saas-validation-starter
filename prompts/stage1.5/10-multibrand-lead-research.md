# Multi-brand Stage 1.5 lead research — start or resume one bounded run

Invoke `/browser` and `/lead-research` in a fresh Antigravity conversation using
High reasoning. This prompt is resumable and must be reused unchanged for each
subsequent bounded run until the canonical summary reaches 50 qualified leads.

## Read first

- `AGENTS.md`
- `.agent/skills/lead-research/SKILL.md`
- `methodology/stage1.5-lead-research.md`
- `methodology/stage15-lead-schema.json`
- `ideas/multi-brand-content/hypothesis.yaml`
- `ideas/multi-brand-content/output/stage1-report.md`
- `ideas/multi-brand-content/stage1.5/lead-research/config.json`
- every existing file under
  `ideas/multi-brand-content/stage1.5/lead-research/`, excluding `reviews/`

The Stage 1 report explains unknowns but is not proof about a lead. The locked
research target is global English-language, owner-led agencies with 2–20 people
that provide recurring organic static social content for multiple client brands.

## Resume and deduplicate

Inspect the generated summary and run status before searching. Preserve every
valid existing lead/source ID and continue from the next unused numeric IDs.
Never restart or replace the dataset. Before adding a candidate, compare its
normalized official domain and organization name against all existing leads,
including holds and exclusions.

## Bounded research budget for this conversation

Inspect at most 20 new candidate organizations and add at most 10 newly
`QUALIFIED_FOR_SCREENING` leads. Stop when either limit is reached. A future
fresh conversation will reuse this same prompt and continue.

Search broadly across English-speaking geographies and more than one discovery
surface. Do not impose a country quota, but do not fill the dataset from a single
directory page or one city merely because it is convenient.

For each candidate:

1. Open the official website and the actual supporting pages. Search snippets do
   not count.
2. Confirm or leave unknown every canonical claim. One public source may support
   several claims when its exact fragment truly does so.
3. For a qualified lead, public sources must confirm all hard claims in
   `config.json`, including a wholly supported 2–20 team range, named
   founder/owner, recurring organic social-content service, static/graphic or
   carousel work, multiple client brands and a public business contact route.
4. Directory-only organizations, conflicting `11-50`/larger headcount,
   paid-ads-only, video-only, SaaS vendors, inactive/rebranded businesses and
   ambiguous identities are not qualified. Record an honest `HOLD` or
   `EXCLUDED` row with a concrete reason.
5. Do not infer SMB clientele or a hands-on owner role. Those can remain
   screening unknowns. Priority A requires direct support for both; otherwise a
   qualified lead is priority B.
6. Store contact URLs only. Do not copy personal emails/phone numbers, guess an
   email, enter a login wall or contact the organization.

Maintain only these researcher-owned canonical files:

- `leads.jsonl`
- `source-register.jsonl`
- `lead-research-report.md`

The analytical report must distinguish confirmed public facts from screening
unknowns, cite material claims by lead ID and source ID, summarize exclusions
and geography/source coverage, and state explicitly that no outreach occurred.
Do not hand-edit generated CSV, summary, computed status fields or snapshot.
When a run is blocked, you may edit only `blockers` and `notes` in
`run-status.json` before rerunning checkpoint; the script owns all other fields.

## Write and terminal boundary

Write only under:

`ideas/multi-brand-content/stage1.5/lead-research/`

Do not alter `config.json`, methodology, scripts, Stage 1 evidence/output or
reviewer-owned files under `reviews/`.

After each group of at most five finalized candidates, run only:

```powershell
python scripts/stage15_leads.py checkpoint --idea multi-brand-content
```

You may then run the read-only consistency check:

```powershell
python scripts/stage15_leads.py check --idea multi-brand-content
```

No `python -c`, terminal web retrieval or helper scripts.

If the generated summary reaches at least 50 `QUALIFIED_FOR_SCREENING` leads,
finish the report and seal the initial package using only:

```powershell
python scripts/stage15_leads.py seal --idea multi-brand-content --snapshot-id mb-leads-v1-001
python scripts/stage15_leads.py check --idea multi-brand-content --require-final
```

If it remains below 50, checkpoint and stop partial without sealing. Report this
run's examined/qualified IDs, cumulative totals, browser blockers and next
starting IDs. Do not start Codex review, screening, outreach or interviews.
