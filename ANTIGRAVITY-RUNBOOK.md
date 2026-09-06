# Antigravity Runbook — Stage 1 SaaS Validation

This runbook assumes Google Antigravity 2.0 and the included `saas-validation-starter` folder.

## 0. Prepare the folder

Unpack the starter pack into a normal local directory. Prefer initializing it as a Git repository so changes are easy to inspect and revert.

Example:

```bash
cd saas-validation-starter
git init
git add .
git commit -m "Bootstrap SaaS validation pipeline"
```

## 1. Create the Antigravity Project

1. Open Antigravity.
2. Select **New Project**.
3. Choose **Add Folder** and select the `saas-validation-starter` root.
4. Create the project.

Antigravity indexes workspace skills from `.agents/skills/<skill-name>/SKILL.md`.
Workspace rules live under `.agents/rules`.

## 2. Configure safety for this research project

Recommended project-level settings:

- **Outside / non-workspace file access:** Deny / Off.
- **Terminal Sandbox:** Enabled where supported.
- **Terminal command execution:** Proceed in Sandbox, or Request Review if you prefer maximum manual control.
- Do not use Always Proceed outside a sandbox for this task.

Research needs web/browser access, but it does not need arbitrary access to the rest of the machine.

## 3. Make the workspace Rule Always On

Open the Agent panel's **...** menu -> **Customizations** -> **Rules**.
Confirm the workspace rule in `.agents/rules/validation-rules.md` is visible.
Set it to **Always On**.

This is important. Do not rely only on the launch prompt to enforce evidence discipline.

## 4. Confirm Skills are detected

Start a conversation and type `/` in the input.
You should see workspace skills such as:

- `/market-research`
- `/pain-mining`
- `/wtp-research`
- `/workflow-mapping`
- `/skeptic-research`
- `/evidence-audit`
- `/stage1-judge`

If they do not appear:

- confirm the Project root is the folder containing `.agents`;
- confirm each skill is exactly `.agents/skills/<name>/SKILL.md`;
- reopen/reload the Project if needed.

## 5. Human pre-flight: inspect the hypothesis

Open:

`ideas/deck-automation/hypothesis.yaml`

Check the founder assumptions and market scope before research starts.
Do not edit the gates after research starts merely because results are disappointing.

The included default scope is:

- global English-speaking B2B;
- SMB/mid-market first;
- no Fortune 500 / procurement-heavy enterprise as initial ICP;
- eventual ARPU plausibly >= $100/month;
- remote founder-led sales / self-service preferred;
- no heavy compliance dependency for initial adoption;
- constrained MVP buildable by a solo technical founder plus agents.

Commit any deliberate changes before starting the five research conversations.

## 6. Start five research conversations in parallel

Use **Local Mode** for all five.

Why Local Mode here: all five agents need to contribute to the same active repository, and this starter pack gives each one a distinct write directory, so there should be no file collision. New Worktree Mode gives stronger isolation but then you must merge five worktrees before auditing.

Create five separate conversations:

### Conversation A — Market

1. Type `/browser` and enable browser access when prompted.
2. Invoke `/market-research`.
3. Paste the body from `prompts/10-run-market.md`.
4. Confirm it writes only to `raw/market`.

### Conversation B — Pain

1. `/browser`
2. `/pain-mining`
3. Paste `prompts/11-run-pain.md` body.

### Conversation C — WTP

1. `/browser`
2. `/wtp-research`
3. Paste `prompts/12-run-wtp.md` body.

### Conversation D — Workflow / ICP

1. `/browser`
2. `/workflow-mapping`
3. Paste `prompts/13-run-workflow.md` body.

### Conversation E — Skeptic

1. `/browser`
2. `/skeptic-research`
3. Paste `prompts/14-run-skeptic.md` body.

Allow Chrome debugging/browser permission when Antigravity requests it.

Do not run the Auditor until all five agents have finished writing their outputs.

## 7. Mechanical pre-check

From the repository root run:

```bash
python scripts/validate_evidence.py ideas/deck-automation/raw
python scripts/find_duplicates.py ideas/deck-automation/raw
```

The first command should end with `OK`.
The second is informational: repeated URLs/independence keys are not automatically errors, but the Auditor needs to see them.

If validation fails, ask only the responsible research conversation to repair its structural output. Do not ask another agent to rewrite it.

## 8. Run the Evidence Auditor

Create a fresh conversation after the five research agents finish.

Do not ask it to do discovery research.
Invoke `/evidence-audit` and paste the body of `prompts/20-run-auditor.md`.

If Antigravity needs to open already-recorded URLs for verification, allow that. The Auditor is forbidden from finding replacement sources.

Expected outputs:

- `ideas/deck-automation/evidence/evidence.jsonl`
- `ideas/deck-automation/evidence/audit-summary.md`
- `ideas/deck-automation/evidence/high-impact-review.md`

## 9. Human spot-check

This is the main human job in Stage 1.

Open `evidence/high-impact-review.md`.
Check the original source for:

- strongest 10 supporting records;
- strongest 10 contradictory records;
- every VERIFIED money/WTP record;
- any disputed record that materially affects a gate.

You do not need to reread every source in the dataset.

If you find a material audit error, correct the evidence/audit status before the Judge runs and record why.

## 10. Run the Judge

Create a new conversation.

**Do not use `/browser`.**

Invoke `/stage1-judge` and paste the body of `prompts/30-run-judge.md`.

Expected outputs:

- `ideas/deck-automation/output/stage1-report.md`
- `ideas/deck-automation/output/scorecard.json`

The final verdict must be exactly:

- PASS
- CONDITIONAL PASS
- FAIL
- INSUFFICIENT EVIDENCE

## 11. Independent review

Bring these three files into the independent review step:

- `output/stage1-report.md`
- `output/scorecard.json`
- `evidence/evidence.jsonl`

Also keep `evidence/high-impact-review.md` handy.

The independent reviewer should challenge the Judge's counting, evidence interpretation, candidate ICP, and proposed wedge before Stage 2 begins.

## 12. Commit the result

After the decision:

```bash
git add .
git commit -m "Complete Stage 1 validation for deck automation"
```

This freezes the evidence and thresholds that produced the decision.

## 13. Reusing the pipeline for another idea

Copy the idea directory structure, create a new `hypothesis.yaml` + `research-brief.md`, then reuse the same Skills and launch prompts with the path changed.

Do not create new methodology for every idea. The point is to compare ideas under the same evidence standard.
