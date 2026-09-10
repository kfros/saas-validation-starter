#!/usr/bin/env python3
"""Offline source-review contract, renderer, checker, and batch state tooling.

This module never retrieves a URL.  It validates locally preserved review
fragments and relationships; a passing check is not proof that a retrieval
actually happened or that a market claim is true.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

IDEA = "multi-brand-content"
SCOPE = "MULTIBRAND-OPERATOR-01"
TRACKS = ("market", "pain", "wtp", "workflow", "skeptic")
VERSION = 1
AUDIT_STATUSES = ("VERIFIED", "PARTIALLY_VERIFIED", "REJECTED", "PENDING")
SCOPE_STATUSES = ("IN_SCOPE", "OUT_OF_SCOPE", "UNKNOWN")
PROVIDER_FORMS = ("SOLO", "AGENCY", "UNKNOWN")
DECISIONS = ("SUPPORTED", "CONTRADICTED", "UNKNOWN", "NOT_APPLICABLE")
CAPTURE_OUTCOMES = ("SUCCESS", "BLOCKED", "NOT_FOUND", "ERROR")
REVIEW_STATES = ("COMPLETE", "BLOCKED")
CLAIM_FIELDS = {
    "quote", "observation", "attribution", "money_amount", "money_currency",
    "money_period", "money_type", "recurrence", "role_scope", "interpretation",
}
CONTROL_IDS = ("mb-pain-001", "mb-wtp-001", "mb-wtp-005", "mb-wtp-008", "mb-wtp-009")


class ReviewError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ReviewError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON property: {key}")
        result[key] = value
    return result


def parse_json(text):
    def bad_constant(value):
        raise ReviewError(f"non-finite JSON number: {value}")
    return json.loads(text, object_pairs_hook=unique_object, parse_constant=bad_constant)


def canonical_bytes(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def fingerprint(value):
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def normalized_fragment(value):
    value = unicodedata.normalize("NFKC", value).replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"\s+", " ", value).strip()


def fragment_fingerprint(value):
    return hashlib.sha256(unicodedata.normalize("NFKC", value)
                          .replace("\r\n", "\n").replace("\r", "\n")
                          .encode("utf-8")).hexdigest()


def normalized_url(url):
    parts = urlsplit(url)
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
             if not k.lower().startswith("utm_") and k.lower() not in {"gclid", "fbclid"}]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"),
                       urlencode(sorted(query)), parts.fragment))


def read_json(path):
    return parse_json(Path(path).read_text(encoding="utf-8"))


def read_jsonl(path, label):
    path = Path(path)
    require(path.is_file(), f"missing {label}: {path}")
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = parse_json(line)
        except (json.JSONDecodeError, ReviewError) as exc:
            raise ReviewError(f"{label}:{number}: {exc}") from exc
        require(isinstance(value, dict), f"{label}:{number}: object required")
        rows.append(value)
    return rows


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True,
                              separators=(",", ":")) + "\n" for row in rows)
    path.write_text(text, encoding="utf-8")


def safe_path(root, value):
    root = Path(root).resolve()
    path = (root / value).resolve()
    require(path.is_relative_to(root), f"path escapes workspace: {value}")
    return path


def load_raw(root):
    root = Path(root).resolve()
    records = {}
    locations = {}
    for track in TRACKS:
        rel = f"ideas/{IDEA}/raw/{track}/evidence.jsonl"
        for row in read_jsonl(safe_path(root, rel), rel):
            rid = row.get("id")
            require(isinstance(rid, str) and rid.startswith(f"mb-{track}-"),
                    f"{rel}: invalid track ID {rid!r}")
            require(rid not in records, f"duplicate raw ID: {rid}")
            require(row.get("audit_status") == "PENDING", f"{rid}: raw audit_status must be PENDING")
            records[rid] = row
            locations[rid] = rel
    return records, locations


def raw_snapshot(raw, locations, ids=None):
    ids = sorted(raw) if ids is None else list(ids)
    return fingerprint([{"evidence_id": rid, "raw_path": locations[rid],
                         "raw_fingerprint": fingerprint(raw[rid])}
                        for rid in ids])


def index_unique(rows, field, label):
    result = {}
    for row in rows:
        key = row.get(field)
        require(isinstance(key, str) and key, f"{label}: nonempty {field} required")
        require(key not in result, f"duplicate {label} {field}: {key}")
        result[key] = row
    return result


def nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def iso_datetime(value):
    require(nonempty_string(value), "inspection/review timestamp required")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ReviewError(f"invalid ISO timestamp: {value}") from exc
    require(parsed.tzinfo is not None, f"timestamp must include timezone: {value}")


def validate_capture(capture):
    allowed = {"schema_version", "capture_id", "requested_url", "resolved_url", "locator",
               "attributed_speaker", "inspected_at", "retrieval_tool", "external_result_id",
               "local_attempt_id", "outcome", "fragment", "fragment_sha256"}
    require(set(capture) == allowed, f"{capture.get('capture_id')}: capture fields differ from contract")
    require(capture["schema_version"] == VERSION, "unsupported capture schema_version")
    cid = capture["capture_id"]
    require(nonempty_string(cid) and re.fullmatch(r"capture-[A-Za-z0-9._-]+", cid),
            f"invalid capture_id: {cid!r}")
    require(nonempty_string(capture["requested_url"]), f"{cid}: requested_url required")
    parsed = urlsplit(capture["requested_url"])
    require(parsed.scheme in {"http", "https"} and parsed.hostname and not parsed.username,
            f"{cid}: public HTTP(S) requested_url required")
    for field in ("resolved_url", "locator", "attributed_speaker", "external_result_id"):
        require(capture[field] is None or nonempty_string(capture[field]), f"{cid}: invalid {field}")
    if capture["resolved_url"] is not None:
        resolved = urlsplit(capture["resolved_url"])
        require(resolved.scheme in {"http", "https"} and resolved.hostname and not resolved.username,
                f"{cid}: public HTTP(S) resolved_url required")
    iso_datetime(capture["inspected_at"])
    require(nonempty_string(capture["retrieval_tool"]), f"{cid}: retrieval_tool required")
    forbidden = ("curl", "wget", "requests", "httpx", "terminal scraper")
    require(not any(x in capture["retrieval_tool"].lower() for x in forbidden),
            f"{cid}: retrieval_tool reports a forbidden terminal/scraper route")
    require(nonempty_string(capture["local_attempt_id"]), f"{cid}: local_attempt_id required")
    require(capture["outcome"] in CAPTURE_OUTCOMES, f"{cid}: invalid outcome")
    fragment = capture["fragment"]
    require(fragment is None or nonempty_string(fragment), f"{cid}: fragment must be null or nonempty")
    require(capture["fragment_sha256"] is None or
            re.fullmatch(r"[0-9a-f]{64}", capture["fragment_sha256"] or ""),
            f"{cid}: invalid fragment_sha256")
    if capture["outcome"] == "SUCCESS":
        require(fragment is not None and capture["fragment_sha256"] == fragment_fingerprint(fragment),
                f"{cid}: SUCCESS needs matching preserved fragment hash")
        require(nonempty_string(capture["locator"]), f"{cid}: SUCCESS needs source locator")
    else:
        require(fragment is None and capture["fragment_sha256"] is None,
                f"{cid}: unsuccessful retrieval cannot carry a supporting fragment")


def expected_claim_fields(raw):
    fields = {"observation", "interpretation", "role_scope"}
    fields.add("quote" if raw.get("source_excerpt") is not None else "attribution")
    if raw.get("author_or_entity") is not None:
        fields.add("attribution")
    if raw.get("recurrence") is not None:
        fields.add("recurrence")
    if raw.get("money_signal") is not None:
        fields.update({"money_amount", "money_currency", "money_period", "money_type"})
    return fields


def scope_dependency(review, raw):
    support = review["scope"]["supporting_evidence_ids"]
    return fingerprint({
        "scope": review["scope"],
        "support_raw_fingerprints": {rid: fingerprint(raw[rid]) for rid in sorted(support)},
    })


def money_assessment_conflicts(raw_row, assessment):
    """Return explicit contract conflicts without interpreting source prose."""
    signal = raw_row.get("money_signal")
    if signal is None:
        return []
    allowed = {
        "actual_purchase": ({"PAID"}, {"ACTUAL"}),
        "paid_pilot": ({"PAID"}, {"ACTUAL"}),
        "saas_spend": ({"PAID"}, {"ACTUAL"}),
        "contractor_spend": ({"PAID"}, {"ACTUAL"}),
        "agency_spend": ({"PAID"}, {"ACTUAL"}),
        # Actual labor/recruitment can be supported without a known salary or
        # cash payment to the operator; do not turn UNKNOWN pay into rejection.
        "employee_time": ({"PAID", "UNKNOWN"}, {"ACTUAL"}),
        "dedicated_role": ({"PAID", "UNKNOWN"}, {"ACTUAL"}),
        # These remain context/intent and are not promoted into revealed spend.
        "stated_wtp": ({"UNKNOWN"}, {"INTENT", "HYPOTHETICAL"}),
        "competitor_price": ({"UNKNOWN"}, {"OFFER"}),
        "unknown": ({"UNKNOWN"}, {"UNKNOWN"}),
    }
    payment_allowed, transaction_allowed = allowed[signal]
    conflicts = []
    if assessment["payment_status"] not in payment_allowed:
        conflicts.append(f"money_signal={signal} incompatible with payment_status={assessment['payment_status']}")
    if assessment["transaction_type"] not in transaction_allowed:
        conflicts.append(f"money_signal={signal} incompatible with transaction_type={assessment['transaction_type']}")
    if (raw_row.get("money_amount") is not None and signal not in {"competitor_price"} and
            not nonempty_string(assessment["amount_basis"])):
        conflicts.append("canonical money_amount requires an explicit amount_basis")
    return conflicts


def validate_review(review, raw, locations, captures):
    allowed = {"schema_version", "evidence_id", "raw_track", "raw_path", "raw_fingerprint",
               "scope_dependency_fingerprint", "reviewed_at", "reviewer_agent", "state", "blocker",
               "capture_ids", "claim_decisions", "audit", "scope", "discrepancies", "raw_owner_repairs"}
    allowed.update({"money_assessment", "impact_assessment", "substitute_assessment"})
    rid = review.get("evidence_id")
    require(set(review) == allowed, f"{rid}: review fields differ from contract")
    require(review["schema_version"] == VERSION, f"{rid}: unsupported review schema_version")
    require(rid in raw, f"unknown review evidence_id: {rid}")
    expected_track = rid.split("-")[1]
    require(review["raw_track"] == expected_track and review["raw_path"] == locations[rid],
            f"{rid}: raw track/path mismatch")
    require(review["raw_fingerprint"] == fingerprint(raw[rid]), f"{rid}: stale raw fingerprint")
    iso_datetime(review["reviewed_at"])
    require(nonempty_string(review["reviewer_agent"]), f"{rid}: reviewer_agent required")
    require(review["state"] in REVIEW_STATES, f"{rid}: invalid review state")
    require(review["blocker"] is None or nonempty_string(review["blocker"]), f"{rid}: invalid blocker")
    capture_ids = review["capture_ids"]
    require(isinstance(capture_ids, list) and len(capture_ids) == len(set(capture_ids)) and
            all(cid in captures for cid in capture_ids), f"{rid}: invalid capture references")
    require(all(captures[cid]["requested_url"] == raw[rid]["source_url"] for cid in capture_ids),
            f"{rid}: capture requested_url differs from canonical exact source_url")
    audit = review["audit"]
    require(isinstance(audit, dict) and set(audit) == {"status", "reason", "independence_key"},
            f"{rid}: invalid audit proposal")
    require(audit["status"] in AUDIT_STATUSES and nonempty_string(audit["reason"]) and
            nonempty_string(audit["independence_key"]), f"{rid}: incomplete audit proposal")
    scope = review["scope"]
    require(isinstance(scope, dict) and set(scope) == {"scope_status", "provider_form",
            "supporting_evidence_ids", "reason"}, f"{rid}: invalid scope proposal")
    require(scope["scope_status"] in SCOPE_STATUSES and scope["provider_form"] in PROVIDER_FORMS and
            nonempty_string(scope["reason"]), f"{rid}: incomplete scope proposal")
    support = scope["supporting_evidence_ids"]
    require(isinstance(support, list) and len(support) == len(set(support)) and
            all(x in raw for x in support), f"{rid}: invalid scope supporting IDs")
    require(review["scope_dependency_fingerprint"] == scope_dependency(review, raw),
            f"{rid}: stale scope/support dependency fingerprint")
    if scope["scope_status"] == "IN_SCOPE":
        require(bool(support), f"{rid}: IN_SCOPE requires supporting evidence IDs")
    money = review["money_assessment"]
    if raw[rid].get("money_signal") is None:
        require(money is None, f"{rid}: non-money row must have null money_assessment")
    else:
        money_fields = {"payer", "recipient", "work_bought_or_done", "payment_status",
                        "transaction_type", "amount_basis", "unresolved_unknowns"}
        require(isinstance(money, dict) and set(money) == money_fields,
                f"{rid}: money_assessment fields differ from contract")
        for field in ("payer", "recipient", "work_bought_or_done", "amount_basis"):
            require(money[field] is None or nonempty_string(money[field]), f"{rid}: invalid money {field}")
        require(money["payment_status"] in {"PAID", "FREE", "UNKNOWN"} and
                money["transaction_type"] in {"ACTUAL", "INTENT", "HYPOTHETICAL", "OFFER", "UNKNOWN"},
                f"{rid}: invalid money payment/transaction classification")
        require(isinstance(money["unresolved_unknowns"], list) and
                all(nonempty_string(x) for x in money["unresolved_unknowns"]),
                f"{rid}: money unresolved_unknowns must be string list")
    impact = review["impact_assessment"]
    require(isinstance(impact, dict) and set(impact) ==
            {"eligible_gates", "exclusion_reason", "unresolved_questions"},
            f"{rid}: invalid impact_assessment")
    require(isinstance(impact["eligible_gates"], list) and
            len(impact["eligible_gates"]) == len(set(impact["eligible_gates"])) and
            all(re.fullmatch(r"G[1-6]", x or "") for x in impact["eligible_gates"]),
            f"{rid}: invalid eligible_gates")
    require(impact["exclusion_reason"] is None or nonempty_string(impact["exclusion_reason"]),
            f"{rid}: invalid exclusion_reason")
    require(isinstance(impact["unresolved_questions"], list) and
            all(nonempty_string(x) for x in impact["unresolved_questions"]),
            f"{rid}: unresolved_questions must be string list")
    require(bool(impact["eligible_gates"]) != (impact["exclusion_reason"] is not None),
            f"{rid}: state exactly one of gate eligibility or exclusion")
    substitute = review["substitute_assessment"]
    if raw[rid].get("type") == "substitute":
        fields = {"capability", "same_job_fit", "price_or_friction", "observed_sufficiency", "evidence_needed"}
        require(isinstance(substitute, dict) and set(substitute) == fields and
                all(value is None or nonempty_string(value) for value in substitute.values()),
                f"{rid}: substitute assessment must separate capability/fit/friction/sufficiency/evidence")
    else:
        require(substitute is None, f"{rid}: non-substitute row must have null substitute_assessment")
    claims = review["claim_decisions"]
    require(isinstance(claims, list), f"{rid}: claim_decisions must be list")
    claim_by_field = {}
    for claim in claims:
        require(isinstance(claim, dict) and set(claim) ==
                {"field", "decision", "reason", "capture_id", "speaker", "material"},
                f"{rid}: invalid claim decision shape")
        field = claim["field"]
        require(field in CLAIM_FIELDS and field not in claim_by_field, f"{rid}: duplicate/invalid claim {field}")
        require(claim["decision"] in DECISIONS and nonempty_string(claim["reason"]) and
                type(claim["material"]) is bool, f"{rid}.{field}: incomplete claim decision")
        cid = claim["capture_id"]
        require(cid is None or cid in capture_ids, f"{rid}.{field}: invalid claim capture")
        require(claim["speaker"] is None or nonempty_string(claim["speaker"]),
                f"{rid}.{field}: invalid speaker")
        if claim["decision"] in {"SUPPORTED", "CONTRADICTED"}:
            require(cid is not None and captures[cid]["outcome"] == "SUCCESS",
                    f"{rid}.{field}: decision needs a successful capture")
            require(claim["speaker"] == captures[cid]["attributed_speaker"],
                    f"{rid}.{field}: speaker differs from capture attribution")
        claim_by_field[field] = claim
    require(expected_claim_fields(raw[rid]) <= set(claim_by_field),
            f"{rid}: missing required claim decisions {expected_claim_fields(raw[rid]) - set(claim_by_field)}")
    discrepancies = review["discrepancies"]
    repairs = review["raw_owner_repairs"]
    require(isinstance(discrepancies, list) and isinstance(repairs, list),
            f"{rid}: discrepancies/repair queue must be lists")
    discrepancy_fields = set()
    for item in discrepancies:
        require(isinstance(item, dict) and set(item) ==
                {"field", "raw_value", "observed_value", "material", "reason"} and
                nonempty_string(item["field"]) and type(item["material"]) is bool and
                nonempty_string(item["reason"]), f"{rid}: invalid discrepancy")
        discrepancy_fields.add(item["field"])
    repair_fields = set()
    for item in repairs:
        require(isinstance(item, dict) and set(item) == {"field", "observed_value", "reason"} and
                nonempty_string(item["field"]) and nonempty_string(item["reason"]),
                f"{rid}: invalid raw-owner repair")
        repair_fields.add(item["field"])
    material_discrepancies = {x["field"] for x in discrepancies if x["material"]}
    require(material_discrepancies <= repair_fields,
            f"{rid}: material discrepancies missing from raw-owner repair queue")
    money_conflicts = money_assessment_conflicts(raw[rid], money) if money is not None else []
    # A failed inspection supplies no observed transaction classification.
    # UNKNOWN is a blocker, not evidence contradicting the raw money signal.
    # Keep the exception narrow: no asserted money facts or supported/contradicted
    # money claims, and only a BLOCKED/PENDING review. Actual conflicts still
    # require a raw-owner action; VERIFIED continues to reject money_conflicts.
    uninspected_money = (
        money is not None and review["state"] == "BLOCKED" and audit["status"] == "PENDING"
        and money["payment_status"] == "UNKNOWN" and money["transaction_type"] == "UNKNOWN"
        and all(money[field] is None for field in
                ("payer", "recipient", "work_bought_or_done", "amount_basis"))
        and all(claim_by_field[field]["decision"] == "UNKNOWN" for field in
                ("money_type", "money_amount", "money_currency", "money_period"))
    )
    if money_conflicts and not uninspected_money:
        require(claim_by_field["money_type"]["decision"] in {"CONTRADICTED", "UNKNOWN"},
                f"{rid}: contradictory money assessment requires non-supported money_type decision")
        require("money_signal" in material_discrepancies and "money_signal" in repair_fields,
                f"{rid}: contradictory money assessment must queue material money_signal repair")
    if review["state"] == "BLOCKED":
        require(review["blocker"] is not None and audit["status"] == "PENDING",
                f"{rid}: BLOCKED review must remain PENDING with blocker")
    else:
        require(review["blocker"] is None, f"{rid}: COMPLETE review cannot carry blocker")
    successful = [captures[cid] for cid in capture_ids if captures[cid]["outcome"] == "SUCCESS"]
    material = [c for c in claims if c["material"]]
    if audit["status"] == "VERIFIED":
        require(review["state"] == "COMPLETE" and successful,
                f"{rid}: VERIFIED requires completed successful inspection")
        require(material and all(c["decision"] in {"SUPPORTED", "NOT_APPLICABLE"} for c in material),
                f"{rid}: VERIFIED has unsupported material claim")
        require(not material_discrepancies, f"{rid}: VERIFIED has unresolved material discrepancy")
        for field in expected_claim_fields(raw[rid]):
            claim = claim_by_field[field]
            raw_field = {"money_type": "money_signal"}.get(field, field)
            nullable_money = field in {"money_amount", "money_currency", "money_period"}
            expected = "NOT_APPLICABLE" if nullable_money and raw[rid].get(raw_field) is None else "SUPPORTED"
            require(claim["decision"] == expected,
                    f"{rid}.{field}: VERIFIED requires {expected}, got {claim['decision']}")
        author = raw[rid].get("author_or_entity")
        if author is not None:
            attribution = claim_by_field["attribution"]
            require(attribution["speaker"] == author,
                    f"{rid}: VERIFIED speaker does not match canonical author_or_entity")
        excerpt = raw[rid].get("source_excerpt")
        if excerpt is not None:
            quote_claim = claim_by_field["quote"]
            if author is not None:
                require(quote_claim["speaker"] == author,
                        f"{rid}: VERIFIED quote speaker differs from canonical author_or_entity")
            quote_capture = captures[quote_claim["capture_id"]]
            require(normalized_fragment(excerpt) in normalized_fragment(quote_capture["fragment"]),
                    f"{rid}: direct quote not contained in its supporting fragment")
        if author is not None:
            for field in {"observation", "money_amount", "money_currency", "money_period", "money_type"}:
                claim = claim_by_field.get(field)
                if claim is not None and claim["decision"] == "SUPPORTED":
                    require(claim["speaker"] == author,
                            f"{rid}.{field}: VERIFIED claim speaker differs from canonical author_or_entity")
        require(not money_conflicts,
                f"{rid}: contradictory money assessment: {'; '.join(money_conflicts)}")
    if audit["status"] == "PARTIALLY_VERIFIED":
        require(review["state"] == "COMPLETE" and successful and
                any(c["decision"] == "SUPPORTED" for c in material) and
                any(c["decision"] in {"CONTRADICTED", "UNKNOWN"} for c in material),
                f"{rid}: PARTIALLY_VERIFIED needs supported and unresolved/contradicted material")
    if audit["status"] == "REJECTED":
        require(review["state"] == "COMPLETE" and any(c["decision"] == "CONTRADICTED" for c in material),
                f"{rid}: retrieval failure alone cannot produce REJECTED")
    if audit["status"] == "PENDING":
        require(review["state"] == "BLOCKED", f"{rid}: fresh PENDING requires blocked review state")


def validate_review_bundle_rows(capture_rows, review_rows, raw, locations):
    """Validate an in-memory bundle without mutating its source files."""
    captures = index_unique(capture_rows, "capture_id", "capture")
    for capture in captures.values():
        validate_capture(capture)
    reviews = index_unique(review_rows, "evidence_id", "review")
    for review in reviews.values():
        validate_review(review, raw, locations, captures)
    attempt_ids = [x["local_attempt_id"] for x in captures.values()]
    require(len(attempt_ids) == len(set(attempt_ids)), "duplicate local_attempt_id in captures")
    referenced = {cid for review in reviews.values() for cid in review["capture_ids"]}
    require(set(captures) == referenced, "orphan or missing capture relative to review references")
    return reviews, captures


def load_review_bundle(review_dir, raw, locations):
    review_dir = Path(review_dir)
    capture_rows = read_jsonl(review_dir / "captures.jsonl", "captures")
    review_rows = read_jsonl(review_dir / "reviews.jsonl", "reviews")
    return validate_review_bundle_rows(capture_rows, review_rows, raw, locations)


def audit_row(raw_row, review):
    row = dict(raw_row)
    if review is None:
        row.update(audit_status="PENDING", audit_reason="No current structured source review.")
    else:
        row["audit_status"] = review["audit"]["status"]
        row["audit_reason"] = review["audit"]["reason"]
        row["independence_key"] = review["audit"]["independence_key"]
    return row


def scope_row(rid, review):
    if review is None:
        return {"evidence_id": rid, "scope_status": "UNKNOWN", "provider_form": "UNKNOWN",
                "supporting_evidence_ids": [], "reason": "No current structured source review."}
    return {"evidence_id": rid, **review["scope"]}


def candidate_data(raw, reviews):
    evidence = [audit_row(raw[rid], reviews.get(rid)) for rid in sorted(raw)]
    scope = {"scope_id": SCOPE, "records": [scope_row(rid, reviews.get(rid)) for rid in sorted(raw)]}
    return evidence, scope


def validate_cross_relationships(raw, reviews, evidence, scope):
    audited = {row["id"]: row for row in evidence}
    require(len(audited) == len(evidence) and set(audited) == set(raw),
            "candidate evidence coverage differs from raw IDs")
    scope_by_id = index_unique(scope.get("records", []), "evidence_id", "scope record")
    require(scope.get("scope_id") == SCOPE and set(scope_by_id) == set(raw),
            "candidate scope map coverage/scope_id mismatch")
    for rid, raw_row in raw.items():
        candidate = audited[rid]
        protected = lambda row: {k: v for k, v in row.items()
                                 if k not in {"audit_status", "audit_reason", "independence_key"}}
        require(protected(candidate) == protected(raw_row), f"{rid}: protected raw fields changed")
        review = reviews.get(rid)
        require(candidate == audit_row(raw_row, review), f"{rid}: review/consolidation audit fields disagree")
        require(scope_by_id[rid] == scope_row(rid, review), f"{rid}: review/consolidation scope fields disagree")
        for support_id in scope_by_id[rid]["supporting_evidence_ids"]:
            require(audited[support_id]["audit_status"] == "VERIFIED",
                    f"{rid}: scope support {support_id} is not VERIFIED")
            require(audited[support_id]["independence_key"] == candidate["independence_key"],
                    f"{rid}: scope support {support_id} has different normalized independence key")


def report_counts(evidence, scope, captures):
    by_scope = Counter(x["scope_status"] for x in scope["records"])
    by_form = Counter(x["provider_form"] for x in scope["records"])
    exact = {x["source_url"] for x in evidence}
    normalized = {normalized_url(x["source_url"]) for x in evidence}
    successful = [x for x in captures.values() if x["outcome"] == "SUCCESS"]
    successful_sources = {x["resolved_url"] or x["requested_url"] for x in successful}
    return {
        "raw_rows": len(evidence),
        "audit_status": {x: sum(r["audit_status"] == x for r in evidence) for x in AUDIT_STATUSES},
        "scope_status": {x: by_scope[x] for x in SCOPE_STATUSES},
        "provider_form": {x: by_form[x] for x in PROVIDER_FORMS},
        "distinct_exact_urls": len(exact),
        "distinct_normalized_url_groups": len(normalized),
        "distinct_independence_keys": len({x["independence_key"] for x in evidence}),
        "retrieval_attempts": len(captures),
        "successful_inspections": len(successful),
        "distinct_successfully_inspected_sources": len(successful_sources),
    }


def md(value):
    if value is None:
        return "—"
    return str(value).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def render_audit_summary(evidence, scope, reviews, captures, manifest):
    scope_by_id = {x["evidence_id"]: x for x in scope["records"]}
    counts = report_counts(evidence, scope, captures)
    lines = [
        "# Generated Stage 1 evidence audit ledger", "",
        "> Machine-owned report. Regenerate it from canonical raw records and validated source-review sidecars.",
        "> Structural consistency does not prove external retrieval, semantic truth, or market fit.", "",
        f"- Contract version: `{VERSION}`",
        f"- Idea: `{IDEA}`",
        f"- Scope: `{SCOPE}`",
        f"- Assembled from recorded reviews at: `{manifest['assembled_at']}`", "",
        "## Machine-owned totals", "", "```json",
        json.dumps(counts, ensure_ascii=False, sort_keys=True, indent=2), "```", "",
        "## Evidence ledger", "",
        "| ID | Track | Exact source URL | Author/entity | Audit status | Scope | Provider form | Independence key | Review state | Capture IDs |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in sorted(evidence, key=lambda x: x["id"]):
        rid = row["id"]
        review = reviews.get(rid)
        lines.append("| " + " | ".join(md(x) for x in (
            rid, rid.split("-")[1], row["source_url"], row.get("author_or_entity"),
            row["audit_status"], scope_by_id[rid]["scope_status"], scope_by_id[rid]["provider_form"],
            row["independence_key"], review["state"] if review else "MISSING",
            ", ".join(review["capture_ids"]) if review else "—")) + " |")
    lines += ["", "## Provenance boundary", "",
              "Counts of rows, URLs, normalized URL groups, entity keys, attempts, and successful inspections are distinct.",
              "The checker validates hashes and exact relationships in local files; it cannot prove that an agent-authored capture originated externally.", ""]
    return "\n".join(lines)


def high_impact(row):
    return (row.get("money_signal") is not None or row.get("type") in {"substitute", "risk"} or
            row.get("strength", 0) >= 4 or row.get("polarity") == "contradicts" or
            row.get("audit_status") in {"PARTIALLY_VERIFIED", "REJECTED"})


def render_high_impact(evidence, scope, reviews, captures, manifest):
    scope_by_id = {x["evidence_id"]: x for x in scope["records"]}
    lines = ["# Generated high-impact source review", "",
             "> Machine-owned report. Material narrative is limited to canonical observations and structured review decisions.",
             "> It is not a gate verdict and does not authorize Stage 2.", "",
             f"- Contract version: `{VERSION}`",
             f"- Assembled from recorded reviews at: `{manifest['assembled_at']}`", ""]
    for row in sorted((x for x in evidence if high_impact(x)), key=lambda x: x["id"]):
        rid = row["id"]
        review = reviews.get(rid)
        entry = scope_by_id[rid]
        lines += [f"## `{rid}`", "", f"- Exact source URL: {row['source_url']}",
                  f"- Canonical author/entity: {md(row.get('author_or_entity'))}",
                  f"- Audit status: `{row['audit_status']}` — {row['audit_reason']}",
                  f"- Scope/provider: `{entry['scope_status']}` / `{entry['provider_form']}`; support: {', '.join(entry['supporting_evidence_ids']) or 'none'}",
                  f"- Directly recorded observation: {row['observation']}",
                  f"- Interpretation boundary: {row['interpretation']}"]
        if row.get("money_signal") is not None:
            lines.append(f"- Canonical money fields: type=`{row['money_signal']}`; amount={md(row.get('money_amount'))}; currency={md(row.get('money_currency'))}; period={md(row.get('money_period'))}")
        if review is None:
            lines += ["- Review state: `MISSING`; no inspection is claimed.", ""]
            continue
        lines.append(f"- Review state: `{review['state']}`; reviewed_at=`{review['reviewed_at']}`; blocker={md(review['blocker'])}")
        impact = review["impact_assessment"]
        lines.append(f"- Gate eligibility: {', '.join(impact['eligible_gates']) or 'none'}; exclusion={md(impact['exclusion_reason'])}; unresolved={'; '.join(impact['unresolved_questions']) or 'none'}")
        if review["money_assessment"] is not None:
            money = review["money_assessment"]
            lines.append("- Monetary assessment: " + "; ".join([
                f"payer={md(money['payer'])}", f"recipient={md(money['recipient'])}",
                f"work={md(money['work_bought_or_done'])}", f"payment={money['payment_status']}",
                f"transaction={money['transaction_type']}", f"amount_basis={md(money['amount_basis'])}",
                f"unknowns={'; '.join(money['unresolved_unknowns']) or 'none'}"]))
        if review["substitute_assessment"] is not None:
            substitute = review["substitute_assessment"]
            lines.append("- Substitute assessment: " + "; ".join(
                f"{key}={md(substitute[key])}" for key in
                ("capability", "same_job_fit", "price_or_friction", "observed_sufficiency", "evidence_needed")))
        for cid in review["capture_ids"]:
            capture = captures[cid]
            lines.append(f"- Capture `{cid}`: outcome=`{capture['outcome']}`; locator={md(capture['locator'])}; speaker={md(capture['attributed_speaker'])}; tool={capture['retrieval_tool']}; external_result_id={md(capture['external_result_id'])}")
        for claim in review["claim_decisions"]:
            lines.append(f"- Claim `{claim['field']}`: `{claim['decision']}`; material={str(claim['material']).lower()}; {claim['reason']}")
        if review["discrepancies"]:
            lines.append("- Unresolved discrepancies: " + "; ".join(f"{x['field']}: {x['reason']}" for x in review["discrepancies"]))
        if review["raw_owner_repairs"]:
            lines.append("- Raw-owner queue: " + "; ".join(f"{x['field']}: {x['reason']}" for x in review["raw_owner_repairs"]))
        lines.append("")
    return "\n".join(lines)


def repair_rows(reviews):
    rows = []
    for rid in sorted(reviews):
        for item in reviews[rid]["raw_owner_repairs"]:
            rows.append({"schema_version": VERSION, "evidence_id": rid, **item})
    return rows


def build_manifest(raw, locations, evidence, scope, reviews, captures):
    timestamps = sorted(review["reviewed_at"] for review in reviews.values())
    return {
        "schema_version": VERSION,
        "idea_id": IDEA,
        "scope_id": SCOPE,
        "assembled_at": timestamps[-1] if timestamps else None,
        "raw_snapshot_sha256": raw_snapshot(raw, locations),
        "evidence_sha256": fingerprint(evidence),
        "scope_map_sha256": fingerprint(scope),
        "reviews_sha256": fingerprint([reviews[x] for x in sorted(reviews)]),
        "captures_sha256": fingerprint([captures[x] for x in sorted(captures)]),
    }


def render_candidate(root, review_dir, output_dir, allow_incomplete=False):
    root = Path(root).resolve()
    output_dir = Path(output_dir).resolve()
    require(output_dir.is_relative_to(root) or "tmp" in {p.lower() for p in output_dir.parts},
            f"output directory is outside workspace/temp: {output_dir}")
    raw, locations = load_raw(root)
    reviews, captures = load_review_bundle(review_dir, raw, locations)
    unknown_missing = set(raw) - set(reviews)
    if not allow_incomplete:
        require(not unknown_missing, f"missing reviews: {', '.join(sorted(unknown_missing))}")
        require(all(x["state"] == "COMPLETE" for x in reviews.values()),
                "strict render requires COMPLETE review coverage; blocked rows need checkpoint mode")
    evidence, scope = candidate_data(raw, reviews)
    validate_cross_relationships(raw, reviews, evidence, scope)
    manifest = build_manifest(raw, locations, evidence, scope, reviews, captures)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(output_dir / "evidence.jsonl", evidence)
    write_json(output_dir / "scope-map.json", scope)
    write_json(output_dir / "source-review-manifest.json", manifest)
    write_jsonl(output_dir / "raw-owner-repairs.jsonl", repair_rows(reviews))
    (output_dir / "audit-summary.md").write_text(
        render_audit_summary(evidence, scope, reviews, captures, manifest), encoding="utf-8")
    (output_dir / "high-impact-review.md").write_text(
        render_high_impact(evidence, scope, reviews, captures, manifest), encoding="utf-8")
    return manifest


def check_candidate(root, review_dir, candidate_dir, allow_incomplete=False, include_reviews=False):
    root = Path(root).resolve()
    candidate_dir = Path(candidate_dir).resolve()
    raw, locations = load_raw(root)
    reviews, captures = load_review_bundle(review_dir, raw, locations)
    if not allow_incomplete:
        require(set(reviews) == set(raw), f"strict review coverage mismatch; missing {sorted(set(raw)-set(reviews))}")
        require(all(x["state"] == "COMPLETE" for x in reviews.values()),
                "strict review coverage contains blocked/incomplete rows")
    evidence = read_jsonl(candidate_dir / "evidence.jsonl", "candidate evidence")
    scope = read_json(candidate_dir / "scope-map.json")
    validate_cross_relationships(raw, reviews, evidence, scope)
    manifest = build_manifest(raw, locations, evidence, scope, reviews, captures)
    require(read_json(candidate_dir / "source-review-manifest.json") == manifest,
            "source-review manifest is stale or inconsistent")
    require(read_jsonl(candidate_dir / "raw-owner-repairs.jsonl", "raw-owner repair queue") == repair_rows(reviews),
            "raw-owner repair queue differs from structured reviews")
    expected_reports = {
        "audit-summary.md": render_audit_summary(evidence, scope, reviews, captures, manifest),
        "high-impact-review.md": render_high_impact(evidence, scope, reviews, captures, manifest),
    }
    for name, expected in expected_reports.items():
        path = candidate_dir / name
        require(path.is_file(), f"missing generated report: {name}")
        require(path.read_text(encoding="utf-8") == expected,
                f"{name}: checked-in report differs from deterministic render")
    label = "CHECKPOINT/INCOMPLETE" if allow_incomplete else "STRICT/COMPLETE"
    print(f"SOURCE_REVIEW={label}; rows={len(raw)} reviews={len(reviews)}. Structural provenance only.")
    result = (evidence, {x["evidence_id"]: x for x in scope["records"]})
    return (*result, reviews) if include_reviews else result


def parse_legacy_ledger(path):
    rows = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\|\s*`?mb-(?:market|pain|wtp|workflow|skeptic)-", line):
            continue
        cells = [x.strip().strip("`") for x in line.strip().strip("|").split("|")]
        if len(cells) < 8:
            continue
        rid = cells[0]
        require(rid not in rows, f"legacy ledger duplicate ID: {rid}")
        rows[rid] = {"track": cells[1], "source_url": cells[2], "status": cells[4],
                     "scope": cells[5], "provider_form": cells[6], "independence_key": cells[7]}
    return rows


def legacy_diagnostic(root, show_details=False):
    root = Path(root).resolve()
    raw, _ = load_raw(root)
    evidence = index_unique(read_jsonl(root / f"ideas/{IDEA}/evidence/evidence.jsonl", "legacy evidence"), "id", "evidence")
    scope_obj = read_json(root / f"ideas/{IDEA}/evidence/scope-map.json")
    scope = index_unique(scope_obj.get("records", []), "evidence_id", "scope")
    ledger_path = root / f"ideas/{IDEA}/evidence/audit-summary.md"
    ledger = parse_legacy_ledger(ledger_path)
    common = set(evidence) & set(ledger)
    comparisons = {
        "source_url": {rid: (evidence[rid]["source_url"], ledger[rid]["source_url"]) for rid in common},
        "independence_key": {rid: (evidence[rid]["independence_key"], ledger[rid]["independence_key"]) for rid in common},
        "audit_status": {rid: (evidence[rid]["audit_status"], ledger[rid]["status"]) for rid in common},
        "scope_status": {rid: (scope[rid]["scope_status"], ledger[rid]["scope"]) for rid in common if rid in scope},
        "provider_form": {rid: (scope[rid]["provider_form"], ledger[rid]["provider_form"]) for rid in common if rid in scope},
    }
    result = {
        "raw_records": len(raw), "audited_records": len(evidence), "ledger_records": len(ledger),
        "missing_ledger_ids": sorted(set(evidence) - set(ledger)),
        "extra_ledger_ids": sorted(set(ledger) - set(evidence)),
        "exact_url_differences": sum(ledger[x]["source_url"] != evidence[x]["source_url"] for x in common),
        "independence_key_differences": sum(ledger[x]["independence_key"] != evidence[x]["independence_key"] for x in common),
        "audit_status_differences": sum(ledger[x]["status"] != evidence[x]["audit_status"] for x in common),
        "scope_status_differences": sum(ledger[x]["scope"] != scope[x]["scope_status"] for x in common if x in scope),
        "provider_form_differences": sum(ledger[x]["provider_form"] != scope[x]["provider_form"] for x in common if x in scope),
        "audited_distinct_exact_urls": len({x["source_url"] for x in evidence.values()}),
        "ledger_distinct_exact_urls": len({x["source_url"] for x in ledger.values()}),
    }
    prose = ledger_path.read_text(encoding="utf-8")
    match = re.search(r"(\d+)\s+unique source URLs", prose)
    result["narrative_claimed_unique_urls"] = int(match.group(1)) if match else None
    if show_details:
        for field, values in comparisons.items():
            for rid in sorted(values):
                expected, actual = values[rid]
                if expected != actual:
                    print(f"LEGACY_DIFFERENCE id={rid} field={field} expected={expected!r} actual={actual!r}")
    print("LEGACY_DIAGNOSTIC=" + json.dumps(result, ensure_ascii=False, sort_keys=True))
    print("Legacy diagnostic is read-only and not admission-ready source verification.")
    return result


def prepare_batch(root, state_dir, ids):
    root = Path(root).resolve()
    state_dir = Path(state_dir).resolve()
    raw, locations = load_raw(root)
    require(1 <= len(ids) <= 5 and len(ids) == len(set(ids)), "batch must contain 1..5 unique IDs")
    require(all(x in raw for x in ids), f"batch contains unknown IDs: {sorted(set(ids)-set(raw))}")
    state_path = state_dir / "batch-state.json"
    if state_path.exists():
        state = read_json(state_path)
        require(state.get("ids") == ids, "existing batch has different IDs/order")
    else:
        state = {"schema_version": VERSION, "idea_id": IDEA, "ids": ids,
                 "batch_snapshot_sha256": raw_snapshot(raw, locations, ids),
                 "processed_ids": [], "blocked_ids": [], "remaining_ids": list(ids),
                 "completed_review_fingerprints": {}, "completed_capture_fingerprints": {}}
    state_dir.mkdir(parents=True, exist_ok=True)
    write_json(state_path, state)
    manifest = {"schema_version": VERSION, "idea_id": IDEA,
                "batch_snapshot_sha256": raw_snapshot(raw, locations, ids),
                "source_groups": [{"exact_source_url": url,
                                   "evidence_ids": [rid for rid in ids if raw[rid]["source_url"] == url]}
                                  for url in dict.fromkeys(raw[rid]["source_url"] for rid in ids)],
                "records": [{"evidence_id": rid, "raw_track": rid.split("-")[1],
                             "raw_path": locations[rid], "raw_fingerprint": fingerprint(raw[rid]),
                             "exact_source_url": raw[rid]["source_url"],
                             "canonical_author_or_entity": raw[rid].get("author_or_entity"),
                             "required_claim_fields": sorted(expected_claim_fields(raw[rid])),
                             "raw_record": raw[rid]}
                            for rid in ids]}
    write_json(state_dir / "batch-manifest.json", manifest)
    for name in ("captures.jsonl", "reviews.jsonl"):
        path = state_dir / name
        if not path.exists():
            path.write_text("", encoding="utf-8")
    print(f"BATCH prepared: {state_path}; remaining={state['remaining_ids']}")
    return state


def checkpoint_batch(root, state_dir):
    root = Path(root).resolve()
    state_dir = Path(state_dir).resolve()
    state = read_json(state_dir / "batch-state.json")
    ids = state.get("ids")
    require(isinstance(ids, list) and 1 <= len(ids) <= 5, "invalid batch state IDs")
    raw, locations = load_raw(root)
    require(state.get("batch_snapshot_sha256") == raw_snapshot(raw, locations, ids),
            "batch raw snapshot changed; prepare a new batch/check fingerprints")
    captures_rows = read_jsonl(state_dir / "captures.jsonl", "captures")
    reviews_rows = read_jsonl(state_dir / "reviews.jsonl", "reviews")
    original_captures = index_unique(captures_rows, "capture_id", "capture")
    original_reviews = index_unique(reviews_rows, "evidence_id", "review")
    processed_before = set(state.get("processed_ids", []))
    stored_reviews = state.get("completed_review_fingerprints", {})
    stored_captures = state.get("completed_capture_fingerprints", {})
    require(isinstance(stored_reviews, dict) and isinstance(stored_captures, dict),
            "invalid completed fingerprint maps in batch state")
    protected_capture_ids = set()
    # Completed reviews are checked exactly as stored before any derived value
    # can be filled. A changed external support row therefore remains stale.
    for rid in processed_before:
        require(rid in original_reviews, f"processed review disappeared: {rid}")
        review = original_reviews[rid]
        if rid in stored_reviews:
            require(fingerprint(review) == stored_reviews[rid],
                    f"{rid}: completed review changed; create an explicit new review")
        for cid in review.get("capture_ids", []):
            require(cid in original_captures, f"{rid}: completed capture disappeared: {cid}")
            if cid in stored_captures:
                require(fingerprint(original_captures[cid]) == stored_captures[cid],
                        f"{cid}: completed capture changed; create an explicit new attempt")
            validate_capture(original_captures[cid])
            protected_capture_ids.add(cid)
        validate_review(review, raw, locations, original_captures)

    sealed_captures = copy.deepcopy(captures_rows)
    sealed_reviews = copy.deepcopy(reviews_rows)
    # Seal only new/previously blocked records, and only in memory until the
    # whole candidate bundle validates. Semantic fields are never supplied.
    for capture in sealed_captures:
        if capture.get("capture_id") in protected_capture_ids:
            continue
        if capture.get("outcome") == "SUCCESS" and isinstance(capture.get("fragment"), str):
            capture["fragment_sha256"] = fragment_fingerprint(capture["fragment"])
        elif capture.get("outcome") in {"BLOCKED", "NOT_FOUND", "ERROR"}:
            capture["fragment_sha256"] = None
    for review in sealed_reviews:
        rid = review.get("evidence_id")
        require(rid in ids, f"batch review contains unknown/out-of-batch ID: {rid}")
        if rid in processed_before:
            continue
        review["raw_track"] = rid.split("-")[1]
        review["raw_path"] = locations[rid]
        review["raw_fingerprint"] = fingerprint(raw[rid])
        if isinstance(review.get("scope"), dict) and isinstance(review["scope"].get("supporting_evidence_ids"), list):
            review["scope_dependency_fingerprint"] = scope_dependency(review, raw)
    reviews, captures = validate_review_bundle_rows(sealed_captures, sealed_reviews, raw, locations)
    require(set(reviews) <= set(ids), "batch reviews contain IDs outside this batch")
    processed = [rid for rid in ids if rid in reviews and reviews[rid]["state"] == "COMPLETE"]
    blocked = [rid for rid in ids if rid in reviews and reviews[rid]["state"] == "BLOCKED"]
    remaining = [rid for rid in ids if rid not in reviews]
    completed_capture_ids = {cid for rid in processed for cid in reviews[rid]["capture_ids"]}
    state.update(processed_ids=processed, blocked_ids=blocked, remaining_ids=remaining,
                 completed_review_fingerprints={rid: fingerprint(reviews[rid]) for rid in processed},
                 completed_capture_fingerprints={cid: fingerprint(captures[cid])
                                                 for cid in sorted(completed_capture_ids)})
    write_jsonl(state_dir / "captures.jsonl", sealed_captures)
    write_jsonl(state_dir / "reviews.jsonl", sealed_reviews)
    write_json(state_dir / "batch-state.json", state)
    print(f"BATCH checkpoint: processed={processed}; blocked={blocked}; remaining={remaining}")
    return state


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("legacy-diagnostic")
    render = sub.add_parser("render")
    render.add_argument("--reviews", required=True)
    render.add_argument("--output", required=True)
    render.add_argument("--allow-incomplete", action="store_true")
    check = sub.add_parser("check")
    check.add_argument("--reviews", required=True)
    check.add_argument("--candidate", required=True)
    check.add_argument("--allow-incomplete", action="store_true")
    prepare = sub.add_parser("prepare-batch")
    prepare.add_argument("--state-dir", required=True)
    prepare.add_argument("--ids", nargs="+", required=True)
    checkpoint = sub.add_parser("checkpoint-batch")
    checkpoint.add_argument("--state-dir", required=True)
    args = parser.parse_args(argv)
    try:
        root = Path(args.root)
        if args.command == "legacy-diagnostic":
            legacy_diagnostic(root, show_details=True)
        elif args.command == "render":
            render_candidate(root, safe_path(root, args.reviews), safe_path(root, args.output), args.allow_incomplete)
        elif args.command == "check":
            check_candidate(root, safe_path(root, args.reviews), safe_path(root, args.candidate), args.allow_incomplete)
        elif args.command == "prepare-batch":
            prepare_batch(root, safe_path(root, args.state_dir), args.ids)
        elif args.command == "checkpoint-batch":
            checkpoint_batch(root, safe_path(root, args.state_dir))
        print("OK: offline audit tooling completed. No source or market verification implied.")
        return 0
    except (ReviewError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
