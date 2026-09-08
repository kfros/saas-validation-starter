# Resume a stopped GEO conversation

Use in the original track, or in a fresh conversation with the same skill and
original GEO launch prompt. Do not resume an active writer from a second conversation.
For a fresh conversation paste the original stage prompt first, then this block.

```text
Resume only the stage and write directory authorized by the original GEO launch prompt in this conversation. If that prompt is absent or the stage is ambiguous, stop and ask which stage; do not infer ownership from whichever files exist.

Read ideas/geo-monitoring/research-protocol.md and your existing authorized outputs first. Preserve valid records, stable IDs, negative evidence and progress. Recompute actual records; do not trust a stale count. Do not delete the previous conversation, output files or internal artifacts as a recovery strategy. Do not inspect those internal artifacts at all.

If the underlying browser quota/access blocker remains, end partial with next_actions; do not retry into a loop. If tools are restored, resume from recorded unfinished work. Research may reopen original pages; any record whose page was never actually inspected must not be presented as supported evidence. Auditor may reopen only recorded raw URLs; Judge never browses. Do not expand discovery permissions during audit or judge recovery.

No python -c, python stdin, inline code, scraper, cache, .gemini/antigravity/brain, .system_generated or outside-workspace access. Use only the exact checker command(s) in the original launch prompt. On a validation error repair only your owned structural output once and rerun once; otherwise document the blocker and stop. Report what was preserved, added, left unverified and still blocked. Do not alter the scope or thresholds to complete the run.
```
