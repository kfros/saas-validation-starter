# Multi-Brand Content Production Engine: Stage 1 Evidence Audit Summary

**Idea ID**: `multi-brand-content`  
**Target Scope**: `MULTIBRAND-OPERATOR-01`  
**Date of Audit**: 2026-09-08  
**Auditor**: Evidence Audit Agent (via Antigravity Browser Verification)  

---

## 1. Executive Summary & Inspection Completeness

This audit examined all 71 raw evidence records collected across five research tracks (`market`: 21, `pain`: 21, `wtp`: 10, `workflow`: 5, `skeptic`: 14).

- **Source Inspection Completeness**: 100% of the 57 unique source URLs were inspected in a live browser session.
- **Pending Records**: 0 records are marked `PENDING`. No tool exhaustion, rate limits, or network failures blocked source verification.
- **Audit Outcomes**:
  - **VERIFIED**: 60 records (84.5%)
  - **PARTIALLY_VERIFIED**: 5 records (7.0%)
  - **REJECTED**: 6 records (8.5%)
  - **PENDING**: 0 records (0.0%)
- **Unique Verified Independence Keys**: 49 independent sources/entities.

---

## 2. Dataset Summary (Checker Exact Representation)

The following table and JSON structure reflect the exact counts computed by `scripts/check_multibrand_stage1.py audit`:

### Overall Audit Status Breakdown
| Audit Status | Record Count | Percentage |
| :--- | :--- | :--- |
| **VERIFIED** | 60 | 84.5% |
| **PARTIALLY_VERIFIED** | 5 | 7.0% |
| **REJECTED** | 6 | 8.5% |
| **PENDING** | 0 | 0.0% |
| **Total Records** | **71** | **100.0%** |
| **Verified Independence Keys** | **49** | — |

### Breakdown by Scope Status (`MULTIBRAND-OPERATOR-01`)
| Scope Status | Total Records | Verified Records | Verified Independence Keys |
| :--- | :--- | :--- | :--- |
| **IN_SCOPE** | 0 | 0 | 0 |
| **OUT_OF_SCOPE** | 30 | 22 | 14 |
| **UNKNOWN** | 41 | 38 | 35 |
| **Total** | **71** | **60** | **49** |

### Breakdown by Provider Form
| Provider Form | Total Records | Verified Records | Verified Independence Keys |
| :--- | :--- | :--- | :--- |
| **SOLO** | 6 | 6 | 6 |
| **AGENCY** | 20 | 19 | 16 |
| **UNKNOWN** | 45 | 35 | 27 |
| **Total** | **71** | **60** | **49** |

### Canonical DATASET_SUMMARY JSON
```json
{
  "by_audit_status": {
    "PARTIALLY_VERIFIED": 5,
    "PENDING": 0,
    "REJECTED": 6,
    "VERIFIED": 60
  },
  "by_provider_form": {
    "AGENCY": {
      "records": 20,
      "verified_independence_keys": 16,
      "verified_records": 19
    },
    "SOLO": {
      "records": 6,
      "verified_independence_keys": 6,
      "verified_records": 6
    },
    "UNKNOWN": {
      "records": 45,
      "verified_independence_keys": 27,
      "verified_records": 35
    }
  },
  "by_scope": {
    "IN_SCOPE": {
      "records": 0,
      "verified_independence_keys": 0,
      "verified_records": 0
    },
    "OUT_OF_SCOPE": {
      "records": 30,
      "verified_independence_keys": 14,
      "verified_records": 22
    },
    "UNKNOWN": {
      "records": 41,
      "verified_independence_keys": 35,
      "verified_records": 38
    }
  },
  "total_records": 71,
  "verified_independence_keys": 49
}
```

---

## 3. Detailed Audit Findings & Categorization

### Rejected Records (6 Records)
All 6 rejected records failed due to broken URLs returning HTTP 404 Not Found during live browser inspection without valid redirects:
1. `mb-market-001`: Canva Help (`https://www.canva.com/help/use-brand-kit/`) — HTTP 404.
2. `mb-market-004`: Canva Help (`https://www.canva.com/help/request-approval/`) — HTTP 404.
3. `mb-market-005`: Adobe Help (`https://helpx.adobe.com/express/using/brand-kits.html`) — HTTP 404.
4. `mb-market-006`: Adobe Help (`https://helpx.adobe.com/express/using/bulk-create.html`) — HTTP 404.
5. `mb-market-011`: Kontentino (`https://www.kontentino.com/features/collaboration/`) — HTTP 404.
6. `mb-market-012`: Kontentino (`https://www.kontentino.com/features/approvals/`) — HTTP 404.

### Partially Verified Records (5 Records)
These records contain verified core facts but overclaim material elements, use outdated pricing, or blur usage into paid spend:
1. `mb-market-002`: Canva Bulk Create documentation verifies 300-row CSV generation and detached outputs; however, vendor documentation is published capability, not an experienced customer gap.
2. `mb-market-003`: Canva Pricing page confirms pricing structure, but the raw observation recorded superseded legacy numbers ($15/mo Pro, $100/seat Teams); current pricing is $18/mo Pro and $25/user/mo Business.
3. `mb-wtp-004`: Planable user complains about Grid view pricing; establishes tool usage but no actual payment tier, transaction amount, or paid spend is established.
4. `mb-wtp-007`: Practitioner discusses standard subcontracting rate benchmarks ($400–$800/mo flat fee) and target agency margins; presents a hypothetical margin rule-of-thumb rather than an actual completed spend transaction.
5. `mb-workflow-004`: Duplicate source URL and observation of `mb-wtp-004` (Planable Grid view pricing complaint); lacks verified paid spend.

### Verified Records (60 Records)
All 60 verified records directly substantiate every material claim, number, and semantic classification without rewriting or embellishment.

---

## 4. Scope Attribution & Boundary Analysis (`MULTIBRAND-OPERATOR-01`)

The operational definition of `MULTIBRAND-OPERATOR-01` requires five concurrent conditions:
1. External social-media content service (not in-house).
2. Multiple unrelated client brands.
3. Recurring static social-content production and revision work.
4. Owner-led provider with hands-on production or revision role.
5. SMB clientele explicitly established in source text or identity-linked evidence.

### Findings on Scope:
- **`OUT_OF_SCOPE` (30 Records)**:
  - 28 Software Vendor Records: Product documentation and pricing for Canva, Adobe, Planable, Kontentino, SocialPilot, Buffer, Predis.ai, Ocoya, Abyssale, Bannerbear, PostFlow (`mb-workflow-005`), and Juicer (`mb-skeptic-014`).
  - 2 Explicitly Excluded Practitioners: `mb-wtp-005` (single-brand small business owner) and `mb-pain-017` (in-house marketing professional for a single organization).
- **`UNKNOWN` (41 Records)**:
  - All remaining practitioner records. While many describe managing multiple clients (e.g. `UniversityWestern346` with 5 clients, `Prudent-Bad-8786` with 6 clients, `Huge_Razzmatazz_985` with 5 clients), none explicitly establish that their clients are SMBs alongside hands-on owner-operator status.
  - In adherence to Rule 1 ("Never invent a fact..."), Rule 2 ("`UNKNOWN` is a valid and often correct result"), and Rule 17 ("Never fabricate SMB focus, ownership or buyer authority"), these records must remain `UNKNOWN` rather than being upgraded to `IN_SCOPE`.
- **`IN_SCOPE` (0 Records)**:
  - No record meets all five strict criteria with explicit verified evidence.

---

## 5. Duplicate Groups & Independence Key Normalizations

Several raw records shared underlying entities, commercial sources, or authors. These have been normalized to canonical independence keys:
1. `vendor-canva`: Canva official documentation and pricing across tracks (`mb-market-001`..`004`, `mb-skeptic-001`..`003`).
2. `vendor-planable`: Planable official documentation and pricing (`mb-market-008`..`010`, `mb-skeptic-004`..`005`).
3. `vendor-adobe`: Adobe official documentation and pricing (`mb-market-005`..`007`).
4. `vendor-kontentino`: Kontentino official documentation and pricing (`mb-market-011`..`013`).
5. `vendor-socialpilot`: SocialPilot official documentation and pricing (`mb-market-014`..`015`).
6. `vendor-predis`: Predis.ai official documentation and pricing (`mb-market-017`..`018`).
7. `reddit-user-universitywestern346`: `mb-pain-001` and `mb-wtp-002` (same practitioner managing ~5 clients in Canva).
8. `reddit-user-prudent-bad-8786`: `mb-pain-015` and `mb-skeptic-006` (same small agency operator experiencing Canva-scheduler desynchronization).
9. `reddit-user-k-rocker`: `mb-pain-011` and `mb-skeptic-013` (same agency practitioner using shared Canva document).
10. `reddit-user-broad-perspective166`: `mb-wtp-004` and `mb-workflow-004` (same author and observation regarding Planable Grid view pricing).

---

## 6. Gate Eligibility Context for Stage 1 Judge

*Note: In accordance with Rule 17, the Auditor does not issue gate verdicts. The following observations summarize eligibility conditions for the Judge:*

- **Gates 1–5 (Pain, Recurrence, WTP, Gap, Reachability)**:
  - Canonical gate rules require counted supporting evidence to be `VERIFIED` and `IN_SCOPE`.
  - Because 0 records are currently established as `IN_SCOPE` for `MULTIBRAND-OPERATOR-01` (41 records are `UNKNOWN`), the Judge will need to assess whether the lack of explicit SMB / owner-operator evidence prevents Gates 1–5 from passing, or whether scope ambiguity requires an `INSUFFICIENT EVIDENCE` verdict or candidate scope reassessment.
- **Gate 3 (WTP)**:
  - Revealed spend signals were verified for outsourced contractor spend (`mb-wtp-006`: $1,500/mo), legacy multi-tenant SaaS (`mb-wtp-001`: $120/yr, `mb-wtp-003`: $200 for 100 accounts), and heavy internal labor (`mb-wtp-008`, `mb-wtp-009`: 25–45+ hrs/mo/client). However, all exist under `UNKNOWN` scope.
- **Gate 6 (Substitute Risk)**:
  - Evaluates incumbent substitutes across market and practitioner sources. Incumbents (Canva Pro/Business, Planable, Adobe Express) provide substantial, low-cost coverage of brand asset isolation, batch generation, and client review workflows. Contradictory evidence (`mb-pain-002`, `mb-pain-011`, `mb-skeptic-007`, `mb-skeptic-008`, `mb-wtp-010`) shows strong observed sufficiency of existing manual and template workflows.
