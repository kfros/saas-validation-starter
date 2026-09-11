# Multi-brand Stage 1.5 lead repair after independent Codex audit

Invoke `/browser` and `/lead-research` in a fresh Antigravity conversation using
High reasoning. Run this only after Codex has written a complete audit under:

`ideas/multi-brand-content/stage1.5/lead-research/reviews/`

Read the same contracts and inputs as
`prompts/stage1.5/10-multibrand-lead-research.md`, plus every Codex audit state,
finding and report in `reviews/`.

## Task

Resolve every open BLOCKER or MAJOR finding against the original public pages.
For each finding, either:

- correct the canonical lead/source row with directly supported facts;
- demote the lead to `HOLD` or `EXCLUDED`; or
- preserve the row and give source-backed reasons that the finding is not a
  defect.

If a demotion reduces the qualified pool below 50, research replacements using
the unchanged qualification contract. Do not lower criteria or keep a broken
lead to preserve the total. Preserve stable IDs; a replacement gets a new ID.
Do not edit Codex-owned findings or claim they are closed yourself.

Update `lead-research-report.md` and create:

`ideas/multi-brand-content/stage1.5/lead-research/reviews/antigravity-repair-response.md`

Map every finding ID to the exact changed lead/source IDs or to the reason for
disagreement. State that no outreach occurred.

Write only in the Stage 1.5 lead-research directory. Do not modify methodology,
scripts, config, Stage 1 files or Codex-owned audit artifacts.

After each bounded repair group run only:

```powershell
python scripts/stage15_leads.py checkpoint --idea multi-brand-content
python scripts/stage15_leads.py check --idea multi-brand-content
```

When all repair work is complete and 50 qualified leads remain, seal a new
snapshot and validate it:

```powershell
python scripts/stage15_leads.py seal --idea multi-brand-content --snapshot-id mb-leads-v1-002
python scripts/stage15_leads.py check --idea multi-brand-content --require-final
```

No `python -c`, terminal web retrieval, outreach, screening or interviews. Stop
after reporting the new snapshot, changed IDs, replacement IDs, unresolved
findings and structural-check result.
