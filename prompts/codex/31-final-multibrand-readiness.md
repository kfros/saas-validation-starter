# Final Codex readiness review of repaired Multi-brand leads

Run in the Stage 1.5+ ChatGPT/Codex thread after Antigravity has resolved the
independent audit and sealed `mb-leads-v1-002`.

Read both snapshots, Codex findings, Antigravity repair response and the complete
current package. Do not modify Antigravity-owned canonical files and do not send
outreach.

Run:

```bash
python scripts/stage15_leads.py check --idea multi-brand-content --require-final
```

Then:

1. Re-open every changed/new lead and source identified in the repair response.
2. Re-test every qualified official website and public contact route, including
   unchanged leads whose previous check was blocked or materially stale.
3. Recompute duplicates and totals and compare the analytical report with
   `lead-summary.json`.
4. Confirm 50 independently identified qualified organizations remain, every
   hard qualification claim has direct successful support, and no BLOCKER/MAJOR
   finding remains unresolved.
5. Confirm remaining priority-B unknowns are appropriate screening questions and
   have not been presented as facts.

Write only
`ideas/multi-brand-content/stage1.5/lead-research/reviews/final-readiness.md`.
Conclude exactly one of:

- `READY_FOR_BOUNDED_OUTREACH_DESIGN`; or
- `NOT_READY`, with specific open blockers.

Readiness does not authorize sending messages. Outreach copy, channel cadence,
screening, consent and interview logging are a subsequent separately authorized
Stage 1.5 task.
