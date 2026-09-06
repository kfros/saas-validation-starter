# Prompt order

For the included deck-automation hypothesis:

1. Do **not** run `00-bootstrap-framework.md`; the framework already exists.
2. Review/edit `ideas/deck-automation/hypothesis.yaml` if needed.
3. Run prompts 10–14 in five separate Antigravity conversations in parallel.
4. Run `scripts/validate_evidence.py` and `scripts/find_duplicates.py` locally as a mechanical pre-check.
5. Run prompt 20 (Auditor) after all five research agents finish.
6. Human spot-check `evidence/high-impact-review.md` against the original URLs.
7. Run prompt 30 (Judge) only after the audit is complete.

`01-create-hypothesis.md` is for future ideas or deliberate pre-research changes.
