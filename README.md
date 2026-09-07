# SaaS Validation — Stage 1 Research Pipeline

This repository is a reusable evidence-first pipeline for validating niche SaaS ideas before product development.

The first configured hypothesis is **Vertical B2B deck / sales-collateral automation**.

## Stage 1 objective

Stage 1 does not prove product-market fit. It decides whether an idea deserves direct customer validation.

It tests five questions:

1. Is there a concrete recurring pain?
2. Does the workflow recur often enough to support a SaaS product?
3. Are customers already spending money or meaningful employee time on it?
4. Do current alternatives leave a repeatable gap?
5. Is the likely ICP reachable without enterprise-scale distribution?

## Architecture

Five research agents run independently and in parallel:

- `market-research`
- `pain-mining`
- `wtp-research`
- `workflow-mapping`
- `skeptic-research`

Then two agents run sequentially:

- `evidence-audit`
- `stage1-judge`

Only audited VERIFIED evidence may influence the Stage 1 verdict.

## Canonical directories

```text
methodology/                    Methodology, evidence schema and gates
.agent/rules/                   Antigravity workspace rules
.agent/skills/                  Antigravity Agent Skills
ideas/deck-automation/          First validation target
  raw/                          Independent agent outputs
  evidence/                     Audited canonical evidence
  output/                       Final Stage 1 report and scorecard
prompts/                        Copy/paste launch prompts
scripts/                        Local validators and duplicate checks
```

## Operating assumptions for the first hypothesis

These are defaults, not discovered facts. Edit `ideas/deck-automation/hypothesis.yaml` before research if they are wrong.

- Global English-speaking B2B market.
- Initial focus on SMB and mid-market companies rather than Fortune 500 procurement-heavy enterprise.
- Product should support remote founder-led sales or self-service acquisition.
- Target eventual ARPU should plausibly be at least USD 100/month.
- Avoid products whose initial adoption depends on heavy regulatory/compliance work.
- MVP should be buildable by a solo technical founder with coding agents.

## Running Stage 1 in Antigravity

See `ANTIGRAVITY-RUNBOOK.md`.

## Important principle

A missing fact remains `UNKNOWN`. Agents must not convert plausible assumptions into evidence.
