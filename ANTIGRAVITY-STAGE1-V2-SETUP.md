# Antigravity: Stage 1 v2 setup for SMB reassessment

Prepared against `kfros/saas-validation-starter` at `3bf758f` (2026-09-11).
This is an engineering launch task, not a completed migration or a new market verdict.

## Как запустить

1. Открой актуальную рабочую копию `saas-validation-starter` в Antigravity. Используй ветку с последними изменениями пайплайна, а не старую ветку GEO или Deck. Незакоммиченные изменения сначала сохрани обычным для тебя способом.
2. Создай новый разговор для общей инженерной подготовки. Рекомендуемый режим рассуждения — High; это выбор для задачи с несколькими связанными контрактами, а не гарантия качества конкретной модели.
3. На этом шаге не вызывай `/browser`, `/evidence-audit` или `/stage1-judge`: ниже отдельная инженерная задача.
4. Приложи этот файл и отправь: `Выполни инженерную задачу из ANTIGRAVITY-STAGE1-V2-SETUP.md. Подготовь общую методологию v2, проверки и launch prompts. Реальные research, audit и Judge сейчас не запускай.`
5. После завершения сохрани изменения отдельным коммитом. Нужны diff, результат проверок и созданный runbook; сообщение «готово» само по себе не является проверкой миграции.

План после подготовки: отдельный новый разговор для целевой проверки GEO; отдельный — для Deck. Затем отдельный новый Judge-разговор для каждой идеи, чьи входные данные готовы. Итого планируется пять разговоров, включая эту подготовку. Сбои или существенная нехватка данных могут потребовать остановки; завершение за пять запусков не гарантируется. На одной рабочей копии запускай их последовательно.

## Engineering task — execute the instructions below

Implement a versioned Stage 1 decision policy for admitting SMB product hypotheses to prospect mining and customer interviews. The user has chosen Antigravity for the reassessment. Do not perform research, source review, a real Judge run, outreach, or development of a product in this task.

### 1. Inspect the current implementation

Read `AGENTS.md`, `.agent/rules/validation-rules.md`, the relevant `.agent/skills/*/SKILL.md`, shared methodology, the GEO and Multi-brand protocols/checkers, Deck/GEO hypotheses and their existing Judge prompts. Preserve the singular `.agent/` directory used by Antigravity.

Check the actual worktree and commit first. Create an isolated local branch for this task without discarding user changes. Do not reset the project to the preparation commit. If files have advanced, adapt to the current implementation and report material differences.

Known places with coupled v1 rules include:

- `methodology/stage1-gates.md`, `methodology/scoring.md`;
- `.agent/skills/stage1-judge/SKILL.md` and `.agent/rules/validation-rules.md`;
- `prompts/30-run-judge.md`, `prompts/geo-monitoring/30-run-judge.md`;
- `ideas/geo-monitoring/research-protocol.md`;
- `scripts/check_geo_stage1.py`, `scripts/check_multibrand_stage1.py` and their tests;
- the Multi-brand protocol and Judge prompt.

These are leads for inspection, not an instruction to rewrite every listed file. Find other consumers before choosing the smallest coherent implementation.

### 2. Implement one explicit v2 policy

The purpose is Stage 2 interviews, not MVP approval. The following counts are founder operating heuristics, not statistically validated sample sizes or a probability of success. Apply the same versioned policy to all three ideas; do not tune it to their current counts.

For **PASS**:

- G1: at least 5 independent VERIFIED examples of experienced concrete pain/workarounds for the assessed scope.
- G2: at least MEDIUM confidence in recurrence of the core job, using observed frequency.
- G3: at least 3 independent VERIFIED examples of actual target-job spending or actually performed costly work. One eligible spend category is sufficient; report the full category breakdown.
- G4: at least 3 independent VERIFIED examples supporting one coherent, repeated gap/workaround, rather than three unrelated complaints. Report clusters and their member IDs.
- G5: at least MEDIUM confidence that relevant buyers can be found through a concrete acquisition surface. Stage 1 does not require a completed prospect list.
- G6: no evidenced sufficient substitute that defeats the value proposition for this same scope. Material unresolved substitute fit remains UNKNOWN. Absence of research does not make G6 PASS.
- All six gates must PASS within one coherent scope.

For **CONDITIONAL PASS**:

- G1 and G5 must PASS. No gate may FAIL.
- Remove the v1 requirement that exactly one gate may be UNKNOWN. Every remaining material unknown must have its own explicit condition; do not bundle unrelated questions into one sentence.
- Conditions may concern recurrence, existing spend, experienced gaps, willingness to switch, or actual substitute sufficiency when interviews with the identified buyers can realistically resolve them.
- Each condition must identify its gate(s), available supporting evidence, exact unknown, respondent qualification, observable information to request, and continue/stop criteria. An unsupported “people will probably pay” is not a plan.
- Limit the recommended next step to an initial round of at most 8 qualified interviews. This is a resource cap, not a statistical guarantee or a rule that nonresponse disproves demand. Record a separate review deadline and treat recruitment failure as inconclusive market evidence.
- Material unresolved technical feasibility, authorized data access, or cost constraints that cannot be resolved in buyer interviews prevent CONDITIONAL PASS. Report the specific bounded technical check needed first.
- This is a recommendation for limited discovery only, not permission to contact people automatically or build a product.

For **FAIL**, require strong, cited contradiction of a core assumption for the assessed scope. Too few records, a blocked browser, unavailable sources, or missing scope attributes alone mean **INSUFFICIENT EVIDENCE**, not FAIL. Preserve contrary evidence even when it reduces enthusiasm for an idea.

### 3. Preserve evidence standards and SMB scope

- Keep only VERIFIED, gate-eligible evidence in threshold counts. Deduplicate by independence key within each gate and scope. Count the same organization/speaker once even when the same experience appears through several sources.
- Do not treat use of a tool as proof of payment, hypothetical effort as actual labor, vendor arithmetic as observed customer spending, or a listed subscription price as actual purchase. Actual work can qualify without a sourced dollar amount; never invent its monetary value.
- Unknown buyer authority, company size, or customer segment remains UNKNOWN. Such attributes may be screened when recruiting, but that does not retroactively make a record IN_SCOPE.
- The hypotheses already target SMB or small agencies. Deck already excludes Fortune 500/procurement-heavy enterprise. Do not rewrite scope just to announce this again.
- GEO retains `GEO-AGENCY-01`: independent SEO agencies with 2–20 staff serving SMB clients on recurring engagements. Solo consultants and direct SMB brand owners do not silently join that scope. The proposed billing unit remains an agency account.
- Deck retains its declared candidate segments. Assess them separately; do not pool pain from agencies with spend from real estate and reachability from enterprise sales. Identify the most defensible declared SMB candidate in the preparation for review. Any material reformulation must be labeled a new, UNVALIDATED hypothesis.
- Enterprise evidence may supply context or a technically general constraint if applicability is demonstrated. It cannot by itself establish SMB pain, procurement friction, or a fatal SMB substitute. “Not FAANG” is not a waiver of actual customer requirements.
- Substitute assessments separate capability, actual workflow fit, adoption/sufficiency, price and switching friction. Compare prices on compatible billing units.
- The eventual $100/month ARPU remains a hypothesis. Do not suppress lower observed prices or change the commercial target in this migration.

### 4. Version the implementation and preserve previous results

Keep an explicit, reproducible v1 policy alongside v2. Old reports and evidence must remain byte-for-byte intact. Preserve v1 numeric thresholds and its single-condition verdict behavior when explicitly validating historical outputs.

Use one machine-readable policy source for numeric rules, selected by explicit version in new runs. Avoid divergent numbers hard-coded separately in prompts and checkers. Unknown policy versions must fail validation. Define documented compatibility for legacy scorecards without a version; never interpret them as v2 silently.

The v2 scorecard must record policy version, input commit/snapshot identity, assessed scope, full counted and contradictory IDs, independent counts, relevant exclusions, gate states, conditions, and the recommended next action. Preserve a clear distinction between valid output structure, evidence coverage, market verdict and permission to execute a later stage.

Define one separate v2 run layout and use it consistently in prompts and checker commands. It must preserve historical raw/evidence/output files. A targeted review should create a versioned audited snapshot/review log instead of overwriting the previous run. Shared policy support should cover Deck, GEO and Multi-brand, but do not run or alter current Multi-brand source batches.

Prefer a small extension to existing tooling. Do not build a new generic audit framework or add another mandatory infrastructure-repair stage. Shared changes may be made in methodology, scripts/tests, supporting contracts, Antigravity rules/skills, prompts and runbooks. A research prompt's write/terminal restrictions apply to its research run, not to this explicitly authorized engineering task. Real idea evidence and Judge results remain read-only here.

### 5. Produce bounded reassessment prompts and a runbook

Create ready-to-use files:

- `prompts/reassessment-v2/10-review-geo.md`
- `prompts/reassessment-v2/11-review-deck.md`
- `prompts/reassessment-v2/20-judge-geo.md`
- `prompts/reassessment-v2/21-judge-deck.md`
- `prompts/reassessment-v2/RUNBOOK.md`

The runbook must contain the exact launch message and applicable slash skills for each step, write directories, actual supported checker commands, deliverables, stopping rules, and which files the user should bring back. Do not reference nonexistent helpers or unsupported CLI flags.

Source-review runs use `/browser` and the appropriate audit skill. Judge runs use `/stage1-judge` without browsing, in a separate fresh conversation from the review. Do not claim independence solely from using a different conversation or model.

For each review, first identify the smallest decisive set of positive and contradictory records needed to assess v2. Reopen original public sources in small groups of at most 5. Review every record actually used to carry a new verdict or a decisive contradiction, including any external records needed to establish its scope; do not inherit old VERIFIED labels as fresh verification. Retain unchanged historical material with its historical provenance, but do not present it as newly checked. Avoid reopening the entire corpus by default. Use a bounded review budget, record what remains unexamined, and do not claim comprehensive market coverage from a targeted review. Finding too little eligible material within the budget is a legitimate stopping result.

Bind each review to the raw ID/version, exact source, speaker, retrieved fragment, supported claim, scope and gate eligibility. Generate repeated metadata and totals from structured data. If historical source-dependent fields require repair, downgrade/exclude the affected record and report the needed correction; do not fabricate a repair or automatically launch another repair cycle. A bounded INSUFFICIENT EVIDENCE result is acceptable.

Known review leads, not predetermined audit findings:

- GEO: `geo-pain-reddit-arash60-defensive-monthly-client-reporting` — distinguish recurring tool use from proven payment; `geo-wtp-blog-agency-manual-hours` — distinguish vendor calculations from observed actual labor; `geo-workflow-12-manual-workaround-labor` — distinguish counterfactual labor from work actually performed. Reassess agency scope, recurring decision value, substitutes and authorized measurement/cost uncertainties without assuming previous interpretations are correct.
- Deck: `ev-pain-faang-no-deck-workflow` and `ev-skp-infosec-procurement-hurdles` — inspect applicability to the selected SMB scope. Inspect the Copilot capability, template and pricing records before concluding same-job sufficiency. Reassess recurrence and reachability within each assessed declared segment; absence of enough public records is not strong contradiction.

Browser failures: allow at most one ordinary retry of a failed source/tool operation; no evasion, ad-hoc scraping, internal `.gemini/antigravity/brain` access, cache extraction, or replacement browser scripts. Record inaccessible pages as unverified/blocked, retain credible completed work and stop a repeatedly failing run as partial. A block alone never supplies negative market evidence.

Allow ordinary read-only access to required repository files. Allow documented file-based local validation scripts. Forbid repeated multiline `python -c` experiments. Research prompts must not accidentally forbid reading their own required inputs.

Judge runs consume only the eligible v2 audited snapshot and fixed v2 policy. They do not browse, repair raw records, change scope or thresholds, or run Stage 2. Each report must compare the old and new verdicts and distinguish effects of policy changes, evidence corrections and scope interpretation. Do not pretend this retrospective reassessment was preregistered.

### 6. Verify and stop

Use temporary synthetic fixtures for meaningful policy/checker tests. Cover at least:

- v1 interpretation remains unchanged; v2 selection is explicit;
- PASS at the exact v2 boundary and rejection below it; duplicate keys cannot inflate counts;
- G3 can pass in one category with qualifying actual behavior, but competitor prices and mere unproven tool use do not count as payment;
- unrelated gaps and cross-scope evidence cannot satisfy v2 gates;
- valid interview conditions across multiple UNKNOWN gates; rejection when G1/G5 are not PASS, any gate FAILs, conditions are missing, or an unresolved material technical blocker is misrepresented as interview-answerable;
- structurally valid INSUFFICIENT EVIDENCE can close a partial run without authorizing Stage 2; blocked records remain ineligible;
- historical evidence and output bytes are unchanged.

Run the relevant existing suites and report pre-existing failures separately from regressions. Do not claim a source truth check from synthetic tests. Stop after engineering setup and report: branch/base commit, changed files, actual checks/results, unresolved limitations, and the exact next launch message for GEO. Do not execute that next message yourself.
