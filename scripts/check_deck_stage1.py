#!/usr/bin/env python3
"""Read-only Deck checks. Python 3.10+, stdlib, no network or subprocess calls.

Enforces schema contracts, single-segment candidate discipline, and policy rules
for deck-automation Stage 1 validation.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

SCRIPTS_DIR = str(Path(__file__).resolve().parent)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)
import stage1_policy

IDEA = "deck-automation"
TRACKS = ("market", "pain", "wtp", "workflow", "skeptic")
SKILLS = ("market-research", "pain-mining", "wtp-research", "workflow-mapping",
          "skeptic-research", "evidence-audit", "stage1-judge")
KEYWORDS = {"$schema", "$id", "title", "description", "type", "additionalProperties",
            "required", "properties", "enum", "minLength", "maxLength", "minimum", "maximum", "format"}

CANDIDATE_ICPS = (
    "b2b_saas_account_executives",
    "sales_enablement_teams",
    "boutique_consultancies",
    "agencies_producing_client_decks",
    "professional_services_firms",
    "commercial_real_estate_teams",
)


def normalize_candidate(name: str) -> str:
    return re.sub(r"[-\s]+", "_", name.strip().lower())


class CheckError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise CheckError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON property: {key}")
        result[key] = value
    return result


def bad_constant(value):
    raise CheckError(f"non-finite JSON number: {value}")


def parse_json(text):
    return json.loads(text, object_pairs_hook=unique_object, parse_constant=bad_constant)


def load_json(path):
    return parse_json(path.read_text(encoding="utf-8"))


def is_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def check_schema_contract(schema):
    require(isinstance(schema, dict), "schema node must be object")
    require(not (set(schema) - KEYWORDS), f"unsupported schema keywords: {set(schema) - KEYWORDS}")
    kinds = schema.get("type", [])
    kinds = kinds if isinstance(kinds, list) else [kinds]
    require(all(k in {"object", "string", "integer", "number", "null", "boolean"} for k in kinds),
            f"unsupported schema types: {kinds}")
    require("format" not in schema or schema["format"] == "date", "unsupported schema format")
    require("additionalProperties" not in schema or isinstance(schema["additionalProperties"], bool),
            "unsupported additionalProperties schema")
    for child in schema.get("properties", {}).values():
        check_schema_contract(child)


def matches_type(value, kind):
    return {"object": isinstance(value, dict), "string": isinstance(value, str),
            "integer": type(value) is int,
            "number": type(value) in (int, float) and math.isfinite(value),
            "null": value is None, "boolean": type(value) is bool}[kind]


def validate_value(value, schema, where="record"):
    kinds = schema.get("type", [])
    kinds = kinds if isinstance(kinds, list) else [kinds]
    require(not kinds or any(matches_type(value, k) for k in kinds), f"{where}: expected {kinds}")
    if "enum" in schema:
        require(any(type(value) is type(x) and value == x for x in schema["enum"]),
                f"{where}: invalid enum value {value!r}")
    if isinstance(value, dict):
        require(not (set(schema.get("required", [])) - set(value)), f"{where}: missing required fields")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            require(not (set(value) - set(props)), f"{where}: additional fields {set(value) - set(props)}")
        for key, item in value.items():
            if key in props:
                validate_value(item, props[key], f"{where}.{key}")
    if isinstance(value, str):
        require(len(value) >= schema.get("minLength", 0), f"{where}: too short")
        require(len(value) <= schema.get("maxLength", len(value)), f"{where}: too long")
        if schema.get("format") == "date":
            require(is_date(value), f"{where}: invalid date")
    if type(value) in (int, float):
        require(math.isfinite(value), f"{where}: non-finite number")
        require(value >= schema.get("minimum", value), f"{where}: below minimum")
        require(value <= schema.get("maximum", value), f"{where}: above maximum")


def normalized_url(url):
    parts = urlsplit(url)
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
             if not k.lower().startswith("utm_") and k.lower() not in {"gclid", "fbclid"}]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"),
                       urlencode(sorted(query)), parts.fragment))


class Checker:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.idea = self.root / "ideas" / IDEA
        self.schema = load_json(self.path("methodology/evidence-schema.json"))
        check_schema_contract(self.schema)
        require(self.schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema",
                "unexpected evidence schema dialect")

    def path(self, relative):
        path = (self.root / relative).resolve()
        require(path.is_relative_to(self.root), f"path escapes workspace: {relative}")
        return path

    def file(self, relative, nonempty=True):
        path = self.path(relative)
        require(path.is_file(), f"missing file: {relative}")
        if nonempty:
            require(bool(path.read_text(encoding="utf-8").strip()), f"empty file: {relative}")
        return path

    def preflight(self):
        for name in ("hypothesis.yaml", "research-brief.md"):
            self.file(f"ideas/{IDEA}/{name}")
        for name in ("evidence-standard.md", "stage1-gates.md", "scoring.md", "stage1-policy.json"):
            self.file(f"methodology/{name}")
        self.file(".agent/rules/validation-rules.md")
        for skill in SKILLS:
            self.file(f".agent/skills/{skill}/SKILL.md")
        for folder in [f"raw/{t}" for t in TRACKS] + ["evidence", "output"]:
            require(self.path(f"ideas/{IDEA}/{folder}").is_dir(), f"missing directory: {folder}")
        print("Preflight files/schema ready for Deck. No evidence or market validation implied.")

    def records(self, relative):
        records, seen = [], set()
        path = self.file(relative, nonempty=False)
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            label = f"{relative}:{number}"
            try:
                rec = parse_json(line)
                validate_value(rec, self.schema, label)
                require(rec["idea"] == IDEA, f"{label}: wrong idea")
                require(rec["id"] not in seen, f"{label}: duplicate ID {rec['id']}")
                url = urlsplit(rec["source_url"])
                require(url.scheme in {"http", "https"} and bool(url.hostname) and not url.username,
                        f"{label}: expected public HTTP(S) URL without credentials")
                require(date.fromisoformat(rec["observed_at"]) <= date.today(), f"{label}: future observed_at")
            except (ValueError, TypeError, KeyError) as exc:
                raise CheckError(f"{label}: {exc}") from exc
            seen.add(rec["id"])
            records.append(rec)
        return records

    def audit(self, policy=None):
        if policy == "v2":
            return self.audit_v2()
        return self.audit_v1()

    def audit_v1(self):
        raw = {r["id"]: r for r in self.raw_all()}
        base = f"ideas/{IDEA}/evidence"
        records = self.records(f"{base}/evidence.jsonl")
        audited = {r["id"]: r for r in records}
        require(set(raw) == set(audited), "audit/raw ID set mismatch: missing or invented evidence")
        for rid, rec in audited.items():
            require(isinstance(rec.get("audit_reason"), str) and bool(rec["audit_reason"].strip()),
                    f"{rid}: audit reason required")
        for name in ("audit-summary.md", "high-impact-review.md"):
            self.file(f"{base}/{name}")
        print(f"Audit structure (v1): {dict(Counter(r['audit_status'] for r in records))}")
        return audited, None

    def audit_v2(self):
        base = f"ideas/{IDEA}/reassessment-v2/evidence"
        ev_dir = self.path(base)
        require(ev_dir.is_dir(), f"missing v2 evidence directory: {base}")

        self.file(f"{base}/audit-summary.md")
        self.file(f"{base}/high-impact-review.md")

        records = self.records(f"{base}/evidence.jsonl")
        audited = {r["id"]: r for r in records}
        for rid, rec in audited.items():
            require(isinstance(rec.get("audit_reason"), str) and bool(rec["audit_reason"].strip()),
                    f"{rid}: audit reason required")

        # review-log validation
        rev_path = self.file(f"{base}/review-log.jsonl")
        review_log_entries = stage1_policy.validate_review_log(rev_path, evidence_records=audited)

        snap_path = self.file(f"{base}/snapshot.json")
        snap = load_json(snap_path)
        try:
            stage1_policy.validate_v2_snapshot(snap, ev_dir, review_log_entries=review_log_entries, evidence_records=audited)
        except stage1_policy.PolicyError as exc:
            raise CheckError(f"v2 snapshot error: {exc}") from exc

        # scope-map in v2 for Deck
        scope_path = self.file(f"{base}/scope-map.json")
        mapping = load_json(scope_path)
        require(isinstance(mapping, dict), "scope-map must be object")
        entries = mapping.get("records", [])
        require(isinstance(entries, list), "scope-map records must be list")
        by_id = {}
        for entry in entries:
            require(isinstance(entry, dict), "scope entry must be object")
            rid = entry.get("evidence_id")
            require(isinstance(rid, str) and rid in audited and rid not in by_id, f"invalid/duplicate evidence_id in scope-map: {rid}")
            require(entry.get("scope_status") in {"IN_SCOPE", "OUT_OF_SCOPE", "UNKNOWN"}, f"{rid}: invalid scope_status")
            cand = entry.get("candidate_scope") or entry.get("candidate_icp")
            require(cand and normalize_candidate(cand) in CANDIDATE_ICPS,
                    f"{rid}: candidate scope {cand!r} must be one of {CANDIDATE_ICPS}")
            entry["candidate_scope"] = normalize_candidate(cand)
            require(isinstance(entry.get("reason"), str) and bool(entry["reason"].strip()), f"{rid}: scope reason required")
            support = entry.get("supporting_evidence_ids")
            require(isinstance(support, list), f"{rid}: scope support list required")
            for sid in support:
                require(isinstance(sid, str) and sid in audited and audited[sid]["audit_status"] == "VERIFIED",
                        f"{rid}: scope support ID {sid} must be VERIFIED")
            if entry["scope_status"] == "IN_SCOPE":
                require(bool(support), f"{rid}: IN_SCOPE without evidence support")
            by_id[rid] = entry

        require(set(by_id) == set(audited), "scope map must cover every audited record")
        print(f"Audit structure (v2): {dict(Counter(r['audit_status'] for r in records))}")
        return audited, by_id

    def judge(self, policy=None):
        if policy == "v2":
            return self.judge_v2()
        return self.judge_v1()

    def judge_v1(self):
        records, scope = self.audit_v1()
        base = f"ideas/{IDEA}/output"
        self.file(f"{base}/stage1-report.md")
        card = load_json(self.file(f"{base}/scorecard.json"))
        require(isinstance(card, dict), "scorecard must be object")

        try:
            detected_policy = stage1_policy.detect_policy_from_scorecard(card, requested_policy="v1", layout_name="legacy")
            stage1_policy.validate_scorecard_against_policy(card, detected_policy, records, scope)
        except stage1_policy.PolicyError as exc:
            raise CheckError(f"Judge policy check failed: {exc}") from exc

        cand_assessments = card.get("candidate_scope_assessments")
        if isinstance(cand_assessments, dict):
            for cand_id, assessment in cand_assessments.items():
                require(isinstance(assessment, dict), f"candidate assessment {cand_id} must be object")
        elif isinstance(cand_assessments, list):
            for item in cand_assessments:
                require(isinstance(item, dict), "candidate assessment list item must be object")

        verdict = card["verdict"]
        print(f"Judge arithmetic/structure valid (v1): {verdict}; human semantic review remains required")

    def judge_v2(self):
        records, scope = self.audit_v2()
        base = f"ideas/{IDEA}/reassessment-v2/output"
        self.file(f"{base}/stage1-report.md")
        card = load_json(self.file(f"{base}/scorecard.json"))
        require(isinstance(card, dict), "scorecard must be object")

        # Deck single-segment discipline: evaluated scope must be one of the 6 declared candidates
        eval_scope = card.get("evaluated_scope", {}).get("scope_id")
        require(eval_scope and normalize_candidate(eval_scope) in CANDIDATE_ICPS,
                f"evaluated scope {eval_scope!r} must be one of declared candidates: {CANDIDATE_ICPS}")
        norm_eval = normalize_candidate(eval_scope)

        # Enforce no pooling across candidate scopes for counted IDs in G1..G5
        gates = card.get("gates", {})
        for gname in ("G1", "G2", "G3", "G4", "G5"):
            if gname in gates:
                for eid in gates[gname].get("counted_evidence_ids", []):
                    rec_scope = scope[eid]
                    require(rec_scope["scope_status"] == "IN_SCOPE",
                            f"{gname}: counted evidence {eid} is not IN_SCOPE")
                    rec_cand = rec_scope.get("candidate_scope")
                    require(rec_cand == norm_eval,
                            f"{gname}: record {eid} candidate scope {rec_cand!r} does not match evaluated scope {eval_scope!r} (cross-segment pooling forbidden)")

        rev_log_path = self.path(f"ideas/{IDEA}/reassessment-v2/evidence/review-log.jsonl")
        review_log = stage1_policy.validate_review_log(rev_log_path, evidence_records=records)
        snap = load_json(self.file(f"ideas/{IDEA}/reassessment-v2/evidence/snapshot.json"))

        try:
            detected_policy = stage1_policy.detect_policy_from_scorecard(card, requested_policy="v2", layout_name="reassessment-v2")
            stage1_policy.validate_scorecard_against_policy(
                card, detected_policy, records, scope,
                review_log=review_log, expected_snapshot_id=snap["snapshot_id"],
            )
        except stage1_policy.PolicyError as exc:
            raise CheckError(f"Judge policy check failed: {exc}") from exc

        # Candidate scope assessments discipline
        cand_assessments = card.get("candidate_scope_assessments")
        if isinstance(cand_assessments, dict):
            for cand_id, assessment in cand_assessments.items():
                require(isinstance(assessment, dict), f"candidate assessment {cand_id} must be object")
        elif isinstance(cand_assessments, list):
            for item in cand_assessments:
                require(isinstance(item, dict), "candidate assessment list item must be object")

        verdict = card["verdict"]
        print(f"Judge arithmetic/structure valid (v2): {verdict}; human semantic review remains required")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("preflight", "audit", "judge"))
    parser.add_argument("--policy", choices=("v1", "v2"), default="v1",
                        help="Policy version (default: v1).")
    args = parser.parse_args()
    try:
        checker = Checker(Path(__file__).resolve().parents[1])
        if args.phase in ("audit", "judge"):
            getattr(checker, args.phase)(policy=args.policy)
        else:
            getattr(checker, args.phase)()
        print("OK: requested structural checks passed. This is not a market PASS.")
        return 0
    except (CheckError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
