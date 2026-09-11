# Stage 1 Gates

The Judge uses only evidence marked `VERIFIED` by the Evidence Auditor.

The purpose of these gates is to decide whether an idea deserves Stage 2 prospect mining and customer discovery interviews.

The repository supports two versioned policies defined in `methodology/stage1-policy.json`:
- **v1 (Baseline Policy)**: historical strict gates used for initial SaaS hypothesis evaluation;
- **v2 (SMB Reassessment Policy)**: calibrated admission policy for SMB hypotheses to customer discovery interviews ($\le 8$ interviews). This is discovery admission, not MVP approval or development authorization.

---

## Gate Thresholds by Policy Version

### G1 — Concrete pain

A "pain signal" must describe an actual workflow problem, cost, delay, error, frustration, or workaround.

- **v1 Threshold**: at least 20 VERIFIED independent concrete pain signals (preferably $\ge 10$ from core target ICP).
- **v2 Threshold**: at least 5 VERIFIED independent examples of experienced concrete pain/workarounds for the assessed scope.

### G2 — Recurrence

The Judge assigns: HIGH, MEDIUM, LOW, or UNKNOWN confidence using observed core job frequency.

- **v1 & v2 Requirement**: PASS requires at least MEDIUM confidence that the core job recurs often enough for a SaaS relationship.

### G3 — Existing spend / WTP

- **v1 Threshold**: at least 5 VERIFIED money signals across at least 2 distinct categories of spend.
- **v2 Threshold**: at least 3 independent VERIFIED examples of actual target-job spending or actually performed costly work. One eligible spend category is sufficient; report full category breakdown.

#### Spend Discipline & Categories
Eligible revealed behavior categories:
- `paid_tool_or_pilot` (actual purchase, paid pilot, SaaS spend);
- `employee_time` (internal labor actually spent on the job);
- `contractor_spend` (outsourced labor);
- `agency_spend` (outsourced agency labor);
- `dedicated_role` (dedicated headcount materially performing the job).

Rules:
- Five competitor pricing pages alone do not satisfy G3.
- `stated_wtp` is preserved separately as context, but does **not** count toward the mandatory revealed/costly-work signals in v2.
- Actually performed costly work qualifies without an invented monetary amount. Never invent dollar figures for unpriced labor.
- Unproven tool use does not equal proof of payment.

### G4 — Repeatable gap in existing solutions

- **v1 Threshold**: at least 10 VERIFIED records showing meaningful workaround, manual cleanup, missing capability, quality failure, or workflow break, clustered around repeatable problems.
- **v2 Threshold**: at least 3 independent VERIFIED examples supporting one coherent, repeated gap/workaround, rather than three unrelated complaints. Report clusters and their member IDs.

### G5 — ICP reachability

Evidence must identify:
- plausible role names;
- plausible company/industry segments;
- where those people can be discovered or contacted (concrete acquisition surface);
- enough public market surface to make Stage 2 prospect mining plausible.

The Judge assigns HIGH / MEDIUM / LOW / UNKNOWN reachability confidence.
- **v1 & v2 Requirement**: PASS requires at least MEDIUM confidence.

### G6 — No killer substitute

The Skeptic and Market research must not reveal an obvious low-friction substitute that already solves the proposed workflow sufficiently well for the target ICP at a price that destroys the planned value proposition.

- A verified low-friction sufficient substitute fails the current wedge.
- A serious direct substitute with material unresolved fit, pricing, or adoption makes G6 UNKNOWN; do not wave it away.
- Absence of research does not make G6 PASS.

---

## Verdict Definitions

### PASS
- **v1**: All six gates PASS for one coherent declared scope.
- **v2**: All six gates PASS within one coherent declared scope.

### CONDITIONAL PASS
- **v1**: No gate fails, five gates PASS, and exactly one material gate-level question remains UNKNOWN and is realistically answerable through interviews. Single condition string required.
- **v2**:
  - G1 and G5 must PASS. No gate may FAIL.
  - Every remaining material UNKNOWN gate must have an explicit condition object covering it.
  - Each condition must specify:
    - `condition_id`: unique identifier;
    - `gate_ids`: list of covered gates;
    - `resolution_method`: must be `INTERVIEW`. (`TECHNICAL_CHECK` and `SOURCE_RESEARCH` are forbidden for CONDITIONAL PASS);
    - `exact_unknown`: precise question to answer;
    - `supporting_evidence_ids`: existing evidence context;
    - `respondent_qualification`: exact interview target profile;
    - `observable_information_to_request`: factual data to gather;
    - `continue_criteria`: what signals validate moving forward;
    - `stop_criteria`: what signals falsify the hypothesis.
  - Resource cap: initial round of at most 8 qualified interviews recorded in `discovery_plan.interview_cap`.
  - Recommended next action: `LIMITED_CUSTOMER_DISCOVERY`. This is NOT permission to build software or contact prospects en masse.
  - Unresolved material technical feasibility, data access, or cost constraints prevent CONDITIONAL PASS and require a preceding `TECHNICAL_CHECK`.

### FAIL
- One or more core assumptions are contradicted strongly by cited VERIFIED evidence for the assessed scope.
- Insufficient records, missing attributes, or tool blocks mean INSUFFICIENT EVIDENCE, not FAIL.

### INSUFFICIENT EVIDENCE
- The research did not produce enough trustworthy evidence to meet thresholds or several material assumptions remain unknown without strong contradiction. Stage 2 is not authorized.

---

## Scope & Anti-Goal

- Do not pool pain from one segment, spend from another, and reachability from a third.
- For Deck automation, candidate ICPs are evaluated individually; pick the most defensible declared candidate or conclude INSUFFICIENT EVIDENCE.
- Do not adjust thresholds after seeing results merely to rescue an attractive idea.
