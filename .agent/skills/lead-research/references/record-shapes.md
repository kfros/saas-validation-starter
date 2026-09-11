# Stage 1.5 record shapes

These synthetic examples show the complete v1 shape. Replace every value after
opening actual public sources. Never leave `example.com`, the synthetic fragment
or an unsupported `CONFIRMED` value in idea data.

## Source row

```json
{"schema_version":1,"source_id":"mb-src-0001","lead_id":"mb-lead-001","url":"https://agency.example/services","source_kind":"OFFICIAL_SITE","publisher":"Example Agency","retrieved_at":"2026-09-11T10:00:00+00:00","retrieval_outcome":"SUCCESS","retrieval_tool":"Antigravity Browser Agent","locator":"Organic social section","exact_fragment":"Exact small fragment actually visible on the opened page.","supports":["ACTIVE_BUSINESS","ENGLISH_SERVICE","EXTERNAL_SERVICE_PROVIDER","ORGANIC_SOCIAL_MANAGEMENT","RECURRING_CONTENT_SERVICE","STATIC_OR_CAROUSEL_CONTENT"],"notes":null}
```

A blocked row has `retrieval_outcome: "BLOCKED"`, `exact_fragment: null` and
`supports: []`. It cannot support a confirmed lead claim.

## Lead row

Every object in `qualification` and `claim_source_ids` contains all 16 canonical
claim names, even when the status is `UNKNOWN` and the source list is empty.

```json
{"schema_version":1,"lead_id":"mb-lead-001","idea_id":"multi-brand-content","scope_id":"MULTIBRAND-OPERATOR-01","organization_name":"Example Agency","organization_key":"example","website_url":"https://agency.example","canonical_domain":"agency.example","city":"Example City","country":"Example Country","working_language":"English","team_size_min":2,"team_size_max":9,"team_size_label":"2-9","owner_name":"Example Founder","owner_role":"Founder","qualification":{"ACTIVE_BUSINESS":"CONFIRMED","ENGLISH_SERVICE":"CONFIRMED","EXTERNAL_SERVICE_PROVIDER":"CONFIRMED","TEAM_SIZE_2_20":"CONFIRMED","OWNER_IDENTITY":"CONFIRMED","ORGANIC_SOCIAL_MANAGEMENT":"CONFIRMED","RECURRING_CONTENT_SERVICE":"CONFIRMED","STATIC_OR_CAROUSEL_CONTENT":"CONFIRMED","MULTIPLE_CLIENT_BRANDS":"CONFIRMED","PUBLIC_BUSINESS_CONTACT":"CONFIRMED","SMB_CLIENTELE":"UNKNOWN","OWNER_HANDS_ON_PRODUCTION":"UNKNOWN","RECURRING_REVISION_PAIN":"UNKNOWN","CURRENT_TOOL_STACK":"UNKNOWN","BUDGET_AUTHORITY":"UNKNOWN","WILLINGNESS_TO_PAY":"UNKNOWN"},"claim_source_ids":{"ACTIVE_BUSINESS":["mb-src-0001"],"ENGLISH_SERVICE":["mb-src-0001"],"EXTERNAL_SERVICE_PROVIDER":["mb-src-0001"],"TEAM_SIZE_2_20":["mb-src-0002"],"OWNER_IDENTITY":["mb-src-0003"],"ORGANIC_SOCIAL_MANAGEMENT":["mb-src-0001"],"RECURRING_CONTENT_SERVICE":["mb-src-0001"],"STATIC_OR_CAROUSEL_CONTENT":["mb-src-0001"],"MULTIPLE_CLIENT_BRANDS":["mb-src-0004"],"PUBLIC_BUSINESS_CONTACT":["mb-src-0005"],"SMB_CLIENTELE":[],"OWNER_HANDS_ON_PRODUCTION":[],"RECURRING_REVISION_PAIN":[],"CURRENT_TOOL_STACK":[],"BUDGET_AUTHORITY":[],"WILLINGNESS_TO_PAY":[]},"contact_channel":"CONTACT_FORM","contact_url":"https://agency.example/contact","contact_source_id":"mb-src-0005","source_ids":["mb-src-0001","mb-src-0002","mb-src-0003","mb-src-0004","mb-src-0005"],"screening_unknowns":["BUDGET_AUTHORITY","CURRENT_TOOL_STACK","OWNER_HANDS_ON_PRODUCTION","RECURRING_REVISION_PAIN","SMB_CLIENTELE","WILLINGNESS_TO_PAY"],"status":"QUALIFIED_FOR_SCREENING","priority":"B","exclusion_reasons":[],"duplicate_of":null,"notes":"State only source-backed or explicitly unresolved details.","last_verified_at":"2026-09-11T10:00:00+00:00"}
```

For `HOLD`, use priority `C` and at least one concrete reason in
`exclusion_reasons`. For `EXCLUDED`, use priority `NONE`. An excluded duplicate
also needs reason `DUPLICATE` and a valid retained `duplicate_of` lead ID.
