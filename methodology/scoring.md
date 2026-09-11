# Stage 1 Scorecard

The Stage 1 Judge reports a structured scorecard (`scorecard.json`) alongside `stage1-report.md`. The gate verdict takes precedence over summed scores.

## Scorecard Contracts

### Legacy v1 Contract
Historical scorecards in `ideas/<idea>/output/scorecard.json` use the legacy format:
- `idea_id`: string
- `evaluation_date`: YYYY-MM-DD
- `verdict`: PASS | CONDITIONAL PASS | FAIL | INSUFFICIENT EVIDENCE
- `rationale`: text
- `stage2_authorized`: boolean
- `evaluated_scope`: object
- `gates`: G1..G6 objects
- `condition`: string or null (non-null only for CONDITIONAL PASS)
- `dimension_scores`: dictionary of 0-5 scores
- `scope_integrity_notes`: string list
- `candidate_scope_assessments`: list or object
- `strongest_positive_evidence`, `strongest_negative_evidence`, `top_unknowns`: ID lists

### Reassessment v2 Contract
Version 2 scorecards in `ideas/<idea>/reassessment-v2/output/scorecard.json` require:
- `policy_version`: `"v2"` (mandatory; missing version in v2 layout is an error)
- `input_commit_or_snapshot`: string identifying the base commit (e.g. `3bf758f`) or review snapshot
- `idea_id`: string
- `evaluation_date`: YYYY-MM-DD
- `verdict`: PASS | CONDITIONAL PASS | FAIL | INSUFFICIENT EVIDENCE
- `rationale`: text
- `stage2_authorized`: boolean (true only for PASS or CONDITIONAL PASS)
- `recommended_next_action`: enum:
  - `LIMITED_CUSTOMER_DISCOVERY` (for CONDITIONAL PASS / PASS)
  - `STOP` (for FAIL)
  - `TECHNICAL_CHECK_REQUIRED` (for material technical/access blocker)
  - `REPAIR_RESEARCH` (for data collection gaps)
- `discovery_plan`: object (required for CONDITIONAL PASS):
  - `interview_cap`: integer ($\le 8$)
  - `target_respondent_profile`: string
  - `review_deadline`: string (e.g. `2 weeks` or date)
  - `nonresponse_policy`: string ("Treat recruitment failure as inconclusive market evidence; nonresponse does not disprove demand.")
- `conditions`: list of condition objects (empty or null unless CONDITIONAL PASS):
  - `condition_id`: string (e.g. `cond-geo-wtp-retainer-expansion`)
  - `gate_ids`: list of gate names (e.g. `["G3"]`)
  - `resolution_method`: `INTERVIEW` (`TECHNICAL_CHECK` and `SOURCE_RESEARCH` are invalid for CONDITIONAL PASS)
  - `exact_unknown`: string
  - `supporting_evidence_ids`: list of verified evidence IDs
  - `respondent_qualification`: string
  - `observable_information_to_request`: string
  - `continue_criteria`: string
  - `stop_criteria`: string
- `evaluated_scope`: object with `scope_id` and declared parameters
- `gates`: G1..G6 objects:
  - `status`: PASS | FAIL | UNKNOWN
  - `threshold_or_rule`: string
  - `independent_count`: integer (matching unique counted independence keys)
  - `counted_evidence_ids`: list of strings
  - `contradictory_evidence_ids`: list of strings
  - `high_impact_excluded`: list of objects (`evidence_id`, `reason`)
  - `confidence`: HIGH | MEDIUM | LOW | UNKNOWN
  - `material_unknowns`: list of strings
  - For G3: `breakdown_by_category` (mapping revealed category to count)
  - For G4: `clusters` (dictionary of cluster name to list of counted evidence IDs)
- `dimension_scores`: dictionary of 0-5 integer scores:
  - `pain_strength`, `recurrence_confidence`, `revealed_wtp`, `current_solution_gap`
  - `icp_clarity`, `reachability`, `substitute_risk`, `evidence_quality`
  - `source_diversity`, `overall_confidence`
- `scope_integrity_notes`: list of strings
- `candidate_scope_assessments`: list or dictionary
- `strongest_positive_evidence`, `strongest_negative_evidence`, `top_unknowns`: ID lists

---

## Dimension Scores
Scores are 0-5 integers. Do not manufacture decimal precision. Dimension scores are summary descriptors only and cannot override gate verdicts.
