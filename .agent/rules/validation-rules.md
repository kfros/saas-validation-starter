---
trigger: always_on
description: Project Validation Workspace Rules
---

# SaaS Validation Workspace Rule

Apply this rule to all Stage 1 validation work in this workspace.

1. Never invent a fact, number, quote, URL, company, price, role, feature, or user statement.
2. `UNKNOWN` is a valid and often correct result.
3. Every factual evidence record requires a source URL.
4. Open and inspect the source. Search-result snippets do not count as evidence.
5. Prefer primary and first-hand sources over secondary summaries.
6. Separate `observation` from `interpretation`.
7. Do not count duplicated, syndicated, or repeated claims as independent evidence.
8. For current product features and pricing, prioritize recent official sources.
9. Do not optimize research toward PASS. Contradictory evidence is mandatory.
10. Do not silently convert absence of evidence into evidence of absence.
11. Revealed willingness to pay is stronger than hypothetical willingness to pay.
12. Do not assert market-size or revenue figures without a traceable methodology/source. Label estimates as estimates.
13. Every evidence record must conform to `methodology/evidence-schema.json`.
14. Read and obey `methodology/evidence-standard.md`.
15. Read and obey `methodology/stage1-gates.md` when evaluating Stage 1.
16. Keep excerpts short. Prefer paraphrase over copying source text.
17. Research agents may not issue the final Stage 1 verdict.
18. Evidence Auditor may not conduct new research or repair weak evidence with new sources.
19. Stage 1 Judge may not browse, search, add sources, or use general knowledge to fill evidence gaps.
20. Stage 1 Judge may use only evidence whose `audit_status` is `VERIFIED`.
21. Do not modify another parallel research agent's output directory.
22. Preserve negative evidence even when it weakens the proposed product.
23. Keep outputs machine-readable where a schema is defined.
24. Before claiming a threshold is met, deduplicate by `independence_key`.
## Tool failure and resource exhaustion policy

25. Do not attempt to bypass unavailable or rate-limited research tools by building ad-hoc web scrapers, search-engine scrapers, browser replacements, or HTTP crawling scripts.
26. Python and terminal tools may be used for local data processing, validation, deduplication, and file generation. They must not be used as a replacement for the browser or web research tools unless the research skill explicitly requires it.
27. On HTTP 429, resource-limit, quota-limit, or equivalent browser/tool exhaustion:
* do not retry the same operation more than once;
* do not repeatedly switch between alternative scraping approaches;
* preserve all evidence already collected;
* record the blocker in the agent's output;
* complete the run with the evidence available so far.
28. After 3 consecutive research-tool failures, stop discovery work for that run. Do not attempt further workaround chains.
29. Minimum evidence targets are targets, not completion requirements. Never weaken evidence standards or enter a retry loop merely to reach a numeric target.
30. If a research run is prevented from reaching its target because of tool/resource limits, explicitly report:
* records collected;
* records still needed to reach the target;
* blocked source types;
* the tool/resource failure that caused the interruption.
31. A partially completed, well-sourced dataset is preferable to an artificially completed or workaround-generated dataset.
