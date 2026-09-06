# Evidence Standard

## 1. Evidence is atomic

One evidence record should support one main factual observation. Split unrelated facts into separate records.

## 2. Observation and interpretation are different fields

**Observation** describes what the source actually establishes.

**Interpretation** states what that observation might mean for the hypothesis.

Do not smuggle interpretation into the observation.

Bad:
> Sales teams desperately need automated deck generation and will pay $500/month.

Better:
> The respondent reports spending approximately three hours per week manually adapting customer-facing PowerPoint decks.

Interpretation:
> This suggests recurring manual effort that may support an automation product.

## 3. Source requirements

Every factual evidence record requires:

- a URL;
- date observed;
- source type;
- source tier;
- enough context to understand what was observed.

Search-result snippets do not count. Open the source.

## 4. Source tiers

### Tier A — strong / primary

Examples:

- official product pricing or documentation;
- first-hand user reviews;
- first-hand practitioner posts or interviews;
- actual job postings;
- actual freelance project listings;
- company statements about its own workflow or product.

### Tier B — useful secondary

Examples:

- reputable interviews;
- credible industry research;
- strong specialist publications;
- expert/community summaries with transparent sourcing.

### Tier C — lead only

Examples:

- affiliate comparisons;
- generic SEO blogs;
- revenue-estimate aggregators;
- unsourced market-size pages;
- reposts.

Tier C may help discover better sources. It must not carry a PASS decision by itself.

## 5. First-hand pain

A strong independent pain signal normally has:

- a unique person or company;
- a specific workflow or situation;
- a concrete problem;
- a traceable source.

Do not count the same person repeating the same complaint as multiple independent signals.

## 6. Willingness-to-pay hierarchy

From strongest to weakest:

1. Actual purchase / paid pilot / recurring spend.
2. Existing company budget for the same job.
3. Paid employee or contractor time dedicated to the job.
4. Paid SaaS subscription solving part of the job.
5. Published competitor price with credible adoption evidence.
6. Stated willingness to pay.
7. Hypothetical "I would pay" comments.

Stage 1 should prioritize revealed behavior over stated intent.

## 7. Recurrence evidence

Record actual recurrence when available:

- per opportunity;
- per client;
- daily;
- weekly;
- monthly;
- quarterly;
- ad hoc.

Do not infer weekly frequency simply because a workflow could happen weekly.

## 8. Negative evidence is mandatory

Agents must record evidence that weakens the hypothesis, including:

- complete substitutes;
- low frequency;
- low switching intent;
- security/privacy blockers;
- low willingness to pay;
- user satisfaction with manual workflow;
- high implementation cost;
- incumbent bundling;
- platform risk.

## 9. Quotes and excerpts

Use short excerpts only when they materially preserve meaning. Prefer paraphrase.

Do not store long copyrighted passages. Keep non-Reddit excerpts short.

## 10. Independent-source counting

Use `independence_key` to identify evidence that should not be counted independently.

Examples:

- same user, same complaint -> same key;
- same company pricing page repeated in several articles -> same underlying key;
- syndicated press release -> one underlying key.

## 11. Unknown is valid

If a source does not establish frequency, money, geography, role, or company size, leave that field null/unknown.
