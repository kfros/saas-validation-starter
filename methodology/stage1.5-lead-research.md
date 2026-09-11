# Stage 1.5 Lead Research Contract

Stage 1.5 is a bounded exploratory bridge for hypotheses whose Stage 1 verdict
is `INSUFFICIENT EVIDENCE`, but which the founder has explicitly chosen to test
through direct conversations. It is not a relaxed Stage 1 PASS and does not
authorize product development, mass outreach or a launch.

## Funnel and counting units

Keep these units separate:

1. **Researched candidate** — an organization inspected during public lead
   research. It may be qualified, held or excluded.
2. **Qualified for screening** — the public record establishes all hard lead
   criteria and a public business contact route. This is a lead, not a validated
   respondent.
3. **Contacted candidate** — outreach was actually sent in a separately
   authorized task.
4. **Qualified respondent** — screening answers establish the complete target
   scope, including the facts that public research intentionally leaves unknown.
5. **Counted substantive conversation** — a qualified respondent gives an
   answer about the actual workflow, pain, substitute, spend or decision process.

The Stage 1.5 target is **5 counted substantive conversations**. Stop at a hard
cap of **8 counted conversations** and make a decision. The candidate and
outreach pools may be much larger. No-response, a bare refusal, trolling,
off-topic text and a wrong-ICP reply do not count. A substantive negative answer
from a qualified respondent does count.

## Lead-research boundary

Lead research is public business research only. It may collect public company
names, founder/owner names and roles, source URLs and public business contact
routes. Do not collect private contact details, guessed emails, personal phone
numbers, data behind login walls or sensitive personal data. Do not send a
message, submit a form, book a call or otherwise interact with a candidate.

Search snippets are discovery leads, never support. Open the public page and
record the exact relevant fragment. Prefer official company pages for services,
portfolio, activity and contact routes; use a public company directory or
professional profile when it is the best available source for team size or
founder identity. A directory range such as `2-10` may establish the configured
team range; a conflicting `11-50` range does not establish `<=20`.

## Canonical artifacts

Each idea keeps its lead work under:

`ideas/<idea>/stage1.5/lead-research/`

- `config.json` — locked scope, target and qualification policy.
- `leads.jsonl` — canonical organization-level lead dataset.
- `source-register.jsonl` — source-level retrieval ledger and exact fragments.
- `lead-research-report.md` — analytical narrative. Its totals must agree with
  generated structured output.
- `leads.csv` — generated operational view; never edit it by hand.
- `lead-summary.json` — generated counts and source coverage.
- `run-status.json` — generated checkpoint state plus honest blockers/notes.
- `snapshot.json` — hashes of a complete package sealed for independent audit.
- `reviews/` — reviewer-owned findings and repair responses.

`leads.jsonl` and `source-register.jsonl` are canonical. Repeated fields and
totals in CSV, status and summaries are generated from them. A passing local
checker proves structural consistency, not that a public page says what the
agent recorded.

## Organization identity and deduplication

One lead equals one independent organization, not one office, founder, employee
or directory listing. Deduplicate on the normalized official domain and on a
case/punctuation-insensitive organization key. Preserve an excluded duplicate
only when it points to the retained `duplicate_of` lead. Rebrands, acquisitions
and parent/subsidiary relationships remain `HOLD` until independence is clear.

## Multi-brand public qualification

For the first run (`MULTIBRAND-OPERATOR-01`), a lead counts toward the 50-lead
research target only when opened public sources confirm all of the following:

- active English-language external service provider;
- owner/founder identity and an agency team of 2–20;
- organic social-media management;
- recurring content-production service;
- static post, graphic or carousel work (not video-only or paid-ads-only);
- work for multiple client brands; and
- a public business contact route.

Public research does **not** silently infer SMB clientele, the owner's hands-on
production/revision role, recurring revision pain, current stack, buying
authority or WTP. Those may remain explicit screening unknowns. Direct evidence
that the organization does not serve SMBs or that its owner is not materially
involved makes it ineligible for this scope; a negative view of the pain or WTP
does not, because disconfirming respondents are valuable. A priority-A lead
additionally has direct public support for both SMB clientele and the owner's
hands-on production/review role; other qualified leads are priority B.

## Source binding

Every confirmed lead claim must reference at least one successful
`source-register.jsonl` row for the same lead whose `supports` list names that
claim. A blocked, missing or errored page cannot support qualification. A
contact route must link to the public page where the form, booking route,
business email route or company messaging surface is actually available.

## Roles and handoff

The lead researcher owns the canonical dataset, source register and analytical
report. The independent reviewer writes findings under `reviews/` and does not
repair those canonical files. The researcher then responds to findings and
creates a new sealed snapshot. Final readiness requires:

- deterministic schema, binding, deduplication and total checks;
- independent semantic review of qualification and report claims;
- successful live re-opening of every qualified lead's official site and public
  contact route, plus the source pages used for decisive hard claims;
- no open blocker affecting a qualified lead; and
- an explicit statement that readiness means **ready for bounded outreach**, not
  that outreach has occurred or that the hypothesis passed.
