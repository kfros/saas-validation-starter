#!/usr/bin/env python3
"""Read-only GEO checks. Python 3.10+, stdlib, no network or subprocess calls.

Enforces the keyword subset used by the repository's current evidence schema.
Fails closed if that schema introduces unsupported keywords; not a general JSON
Schema engine. Structural success never verifies source truth or business fit.
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

IDEA = "geo-monitoring"
SCOPE = "GEO-AGENCY-01"
TRACKS = ("market", "pain", "wtp", "workflow", "skeptic")
REPORTS = {"market": ["market-map.md"], "pain": ["pain-clusters.md"],
           "wtp": ["wtp-map.md"], "workflow": ["workflow-map.md", "icp-candidates.md"],
           "skeptic": ["skeptic-case.md"]}
SKILLS = ("market-research", "pain-mining", "wtp-research", "workflow-mapping",
          "skeptic-research", "evidence-audit", "stage1-judge")
KEYWORDS = {"$schema", "$id", "title", "description", "type", "additionalProperties",
            "required", "properties", "enum", "minLength", "maxLength", "minimum", "maximum", "format"}
MONEY_CATEGORIES = {"actual_purchase": "paid_tool_or_pilot", "paid_pilot": "paid_tool_or_pilot",
                    "saas_spend": "paid_tool_or_pilot", "employee_time": "employee_time",
                    "contractor_spend": "contractor_spend", "agency_spend": "agency_spend",
                    "dedicated_role": "dedicated_role"}


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


def duplicate_warnings(records):
    for field in ("source_url", "independence_key"):
        groups = defaultdict(list)
        for record in records:
            key = normalized_url(record[field]) if field == "source_url" else record[field]
            groups[key].append(record["id"])
        for ids in groups.values():
            if len(ids) > 1:
                print(f"WARNING repeated {field}: {', '.join(ids)} (audit; not auto-delete)")


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
        for name in ("README.md", "RUNBOOK.md", "hypothesis.yaml", "research-brief.md",
                     "research-protocol.md", "source-leads.md"):
            self.file(f"ideas/{IDEA}/{name}")
        for name in ("evidence-standard.md", "stage1-gates.md", "scoring.md", "stage1-policy.json"):
            self.file(f"methodology/{name}")
        self.file(".agent/rules/validation-rules.md")
        for skill in SKILLS:
            self.file(f".agent/skills/{skill}/SKILL.md")
        for name in ("00-preflight", "10-run-market", "11-run-pain", "12-run-wtp",
                     "13-run-workflow", "14-run-skeptic", "20-run-auditor", "30-run-judge", "90-resume"):
            self.file(f"prompts/{IDEA}/{name}.md")
        for folder in [f"raw/{t}" for t in TRACKS] + ["evidence", "output", "setup"]:
            require(self.path(f"ideas/{IDEA}/{folder}").is_dir(), f"missing directory: {folder}")
        print("Preflight files/schema ready. No evidence or market validation implied.")

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

    def track(self, track, checkpoint=False):
        base = f"ideas/{IDEA}/raw/{track}"
        records = self.records(f"{base}/evidence.jsonl")
        for record in records:
            require(record["id"].startswith(f"geo-{track}-"), f"wrong track ID: {record['id']}")
            require(record["audit_status"] == "PENDING", f"raw not PENDING: {record['id']}")
        for name in REPORTS[track]:
            self.file(f"{base}/{name}")
        status = load_json(self.file(f"{base}/run-status.json"))
        require(isinstance(status, dict), f"{track}: status must be object")
        require(status.get("track") == track, f"{track}: wrong status track")
        require(status.get("status") in {"COMPLETE", "PARTIAL"}, f"{track}: invalid run status")
        require(type(status.get("records")) is int and status["records"] == len(records),
                f"{track}: inaccurate record count")
        require(status.get("validation") in {"NOT_RUN", "PASS", "FAIL"}, f"{track}: invalid validation status")
        for field in ("blockers", "next_actions"):
            require(isinstance(status.get(field), list) and all(isinstance(x, str) for x in status[field]),
                    f"{track}: {field} must be a string list")
        if checkpoint:
            require(status["validation"] == "PASS", f"{track}: validation not recorded as PASS")
        if status["status"] == "PARTIAL":
            require(bool(status["blockers"] or status["next_actions"]), f"{track}: explain PARTIAL")
            print(f"WARNING {track}: PARTIAL research; missing coverage must remain unknown")
        print(f"{track}: {len(records)} raw records structurally valid")
        return records

    def raw_all(self):
        records = [rec for track in TRACKS for rec in self.track(track, checkpoint=True)]
        require(len({r["id"] for r in records}) == len(records), "duplicate raw IDs across tracks")
        duplicate_warnings(records)
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
                    f"{rid}: audit reason required (including PENDING)")
            strip = lambda r: {k: v for k, v in r.items() if k not in {"audit_status", "audit_reason", "independence_key"}}
            require(strip(raw[rid]) == strip(rec), f"{rid}: source fields changed; audit stale or observation rewritten")
        for name in ("audit-summary.md", "high-impact-review.md"):
            self.file(f"{base}/{name}")
        mapping = load_json(self.file(f"{base}/scope-map.json"))
        require(isinstance(mapping, dict) and mapping.get("scope_id") == SCOPE, "wrong audit scope")
        entries = mapping.get("records")
        require(isinstance(entries, list), "scope-map.records must be list")
        by_id = {}
        for entry in entries:
            require(isinstance(entry, dict), "scope entry must be object")
            rid = entry.get("evidence_id")
            require(isinstance(rid, str) and rid in audited and rid not in by_id, "invalid/duplicate scope-map ID")
            require(entry.get("scope_status") in {"IN_SCOPE", "OUT_OF_SCOPE", "UNKNOWN"}, f"{rid}: scope status invalid")
            require(isinstance(entry.get("reason"), str) and bool(entry["reason"].strip()), f"{rid}: scope reason required")
            support = entry.get("supporting_evidence_ids")
            require(isinstance(support, list), f"{rid}: scope support list required")
            for source_id in support:
                require(isinstance(source_id, str) and source_id in audited and
                        audited[source_id]["audit_status"] == "VERIFIED", f"{rid}: scope support must be VERIFIED")
            if entry["scope_status"] == "IN_SCOPE":
                require(bool(support), f"{rid}: IN_SCOPE without evidence support")
            by_id[rid] = entry
        require(set(by_id) == set(audited), "scope map must cover every audited record")
        print(f"Audit structure: {dict(Counter(r['audit_status'] for r in records))}")
        return audited, by_id

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

        # scope-map validation first
        mapping = load_json(self.file(f"{base}/scope-map.json"))
        require(isinstance(mapping, dict) and mapping.get("scope_id") == SCOPE, "wrong audit scope")
        entries = mapping.get("records")
        require(isinstance(entries, list), "scope-map.records must be list")
        by_id = {}
        for entry in entries:
            require(isinstance(entry, dict), "scope entry must be object")
            rid = entry.get("evidence_id")
            require(isinstance(rid, str) and rid in audited and rid not in by_id, "invalid/duplicate scope-map ID")
            require(entry.get("scope_status") in {"IN_SCOPE", "OUT_OF_SCOPE", "UNKNOWN"}, f"{rid}: scope status invalid")
            require(isinstance(entry.get("reason"), str) and bool(entry["reason"].strip()), f"{rid}: scope reason required")
            support = entry.get("supporting_evidence_ids")
            require(isinstance(support, list), f"{rid}: scope support list required")
            for source_id in support:
                require(isinstance(source_id, str) and source_id in audited and
                        audited[source_id]["audit_status"] == "VERIFIED", f"{rid}: scope support must be VERIFIED")
            if entry["scope_status"] == "IN_SCOPE":
                require(bool(support), f"{rid}: IN_SCOPE without evidence support")
            by_id[rid] = entry
        require(set(by_id) == set(audited), "scope map must cover every audited record")

        # review-log validation
        baseline_records = stage1_policy.load_historical_baseline_evidence(IDEA, self.root)
        rev_path = self.file(f"{base}/review-log.jsonl")
        review_log_entries = stage1_policy.validate_review_log(
            rev_path,
            evidence_records=audited,
            scope_records=by_id,
            baseline_records=baseline_records,
        )

        # Check snapshot metadata
        snap_path = self.file(f"{base}/snapshot.json")
        snap = load_json(snap_path)
        try:
            stage1_policy.validate_v2_snapshot(
                snap,
                ev_dir,
                review_log_entries=review_log_entries,
                evidence_records=audited,
                expected_idea_id=IDEA,
            )
        except stage1_policy.PolicyError as exc:
            raise CheckError(f"v2 snapshot error: {exc}") from exc

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
        required = {"idea_id", "evaluation_date", "verdict", "rationale", "stage2_authorized",
                    "evaluated_scope", "gates", "condition", "dimension_scores", "scope_integrity_notes",
                    "candidate_scope_assessments", "strongest_positive_evidence", "strongest_negative_evidence", "top_unknowns"}
        require(required <= set(card), f"missing scorecard fields: {required - set(card)}")
        require(card["idea_id"] == IDEA, "wrong scorecard idea")
        require(is_date(card["evaluation_date"]), "invalid evaluation date")
        require(isinstance(card["evaluated_scope"], dict) and card["evaluated_scope"].get("scope_id") == SCOPE,
                "wrong evaluated scope")
        require(isinstance(card["rationale"], str) and bool(card["rationale"].strip()), "rationale required")
        gates = card["gates"]
        require(isinstance(gates, dict) and set(gates) == {f"G{i}" for i in range(1, 7)}, "expected G1..G6")
        verdict = card["verdict"]
        require(verdict in {"PASS", "CONDITIONAL PASS", "FAIL", "INSUFFICIENT EVIDENCE"}, "invalid verdict")
        for name, gate in gates.items():
            require(isinstance(gate, dict), f"{name}: gate must be object")
            fields = {"status", "threshold_or_rule", "independent_count", "counted_evidence_ids",
                      "contradictory_evidence_ids", "high_impact_excluded", "confidence", "material_unknowns"}
            require(fields <= set(gate), f"{name}: missing gate fields")
            require(gate["status"] in {"PASS", "FAIL", "UNKNOWN"}, f"{name}: invalid gate status")
            require(gate["confidence"] in {"HIGH", "MEDIUM", "LOW", "UNKNOWN"}, f"{name}: invalid confidence")
            for field in ("counted_evidence_ids", "contradictory_evidence_ids"):
                ids = gate[field]
                require(isinstance(ids, list) and all(isinstance(x, str) for x in ids), f"{name}: invalid ID list")
                require(len(ids) == len(set(ids)), f"{name}: repeated IDs")
                require(all(x in records and records[x]["audit_status"] == "VERIFIED" for x in ids),
                        f"{name}: unknown or non-VERIFIED evidence counted/cited as contradiction")
            ids = gate["counted_evidence_ids"]
            keys = {records[x]["independence_key"] for x in ids}
            require(len(keys) == len(ids), f"{name}: repeated independence key")
            require(type(gate["independent_count"]) is int and gate["independent_count"] == len(keys),
                    f"{name}: independent count mismatch")
            if name != "G6":
                require(all(scope[x]["scope_status"] == "IN_SCOPE" for x in ids), f"{name}: out-of-scope/unknown buyer evidence")
            if name == "G3":
                require(all(records[x].get("money_signal") in MONEY_CATEGORIES for x in ids), "G3: non-revealed money signal")
                counts = dict(Counter(MONEY_CATEGORIES[records[x]["money_signal"]] for x in ids))
                require(gate.get("breakdown_by_category") == counts, "G3: category breakdown mismatch")
                if gate["status"] == "PASS":
                    require(len(keys) >= 5 and len(counts) >= 2, "G3: PASS below 5 signals / 2 categories")
            if name == "G4":
                clusters = gate.get("clusters")
                require(isinstance(clusters, dict) and all(isinstance(v, list) and all(isinstance(x, str) for x in v)
                        for v in clusters.values()), "G4: clusters required")
                require({x for v in clusters.values() for x in v} == set(ids), "G4: clusters must cover exactly counted IDs")
            if gate["status"] == "PASS":
                if name in {"G1", "G4"}:
                    require(len(keys) >= {"G1": 20, "G4": 10}[name], f"{name}: PASS below numeric threshold")
                if name in {"G2", "G5"}:
                    require(bool(ids) and gate["confidence"] in {"HIGH", "MEDIUM"}, f"{name}: PASS lacks evidence/confidence")
        states = [g["status"] for g in gates.values()]
        if verdict == "PASS":
            require(all(s == "PASS" for s in states), "PASS requires all gates PASS")
        if verdict == "CONDITIONAL PASS":
            require(states.count("UNKNOWN") == 1 and states.count("PASS") == 5, "conditional requires one UNKNOWN / five PASS")
            require(isinstance(card["condition"], str) and bool(card["condition"].strip()), "conditional requires a condition")
        else:
            require(card["condition"] is None, "condition must be null unless conditional")
        if verdict == "FAIL":
            require(any(g["contradictory_evidence_ids"] for g in gates.values()), "FAIL needs cited contradiction, not only missing evidence")
        require(type(card["stage2_authorized"]) is bool and
                card["stage2_authorized"] == (verdict in {"PASS", "CONDITIONAL PASS"}), "stage2_authorized inconsistent")
        require(isinstance(card["dimension_scores"], dict) and bool(card["dimension_scores"]), "dimension scores required")
        require(all(type(v) is int and 0 <= v <= 5 for v in card["dimension_scores"].values()), "dimension scores must be integers 0..5")
        print(f"Judge arithmetic/structure valid: {verdict}; human semantic review remains required")

    def judge_v2(self):
        records, scope = self.audit_v2()
        base = f"ideas/{IDEA}/reassessment-v2/output"
        self.file(f"{base}/stage1-report.md")
        card = load_json(self.file(f"{base}/scorecard.json"))
        require(isinstance(card, dict), "scorecard must be object")

        baseline_records = stage1_policy.load_historical_baseline_evidence(IDEA, self.root)
        rev_log_path = self.path(f"ideas/{IDEA}/reassessment-v2/evidence/review-log.jsonl")
        review_log = stage1_policy.validate_review_log(
            rev_log_path,
            evidence_records=records,
            scope_records=scope,
            baseline_records=baseline_records,
        )
        snap = load_json(self.file(f"ideas/{IDEA}/reassessment-v2/evidence/snapshot.json"))

        try:
            detected_policy = stage1_policy.detect_policy_from_scorecard(card, requested_policy="v2", layout_name="reassessment-v2")
            stage1_policy.validate_scorecard_against_policy(
                card,
                detected_policy,
                records,
                scope,
                review_log=review_log,
                expected_snapshot_id=snap["snapshot_id"],
                expected_idea_id=IDEA,
                expected_scope_id=SCOPE,
            )
        except stage1_policy.PolicyError as exc:
            raise CheckError(f"Judge policy check failed: {exc}") from exc

        verdict = card["verdict"]
        print(f"Judge arithmetic/structure valid (v2): {verdict}; human semantic review remains required")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("preflight", *TRACKS, "raw-all", "audit", "judge"))
    parser.add_argument("--policy", choices=("v1", "v2"), default="v1",
                        help="Policy version (default: v1).")
    args = parser.parse_args()
    try:
        checker = Checker(Path(__file__).resolve().parents[1])
        if args.phase in TRACKS:
            duplicate_warnings(checker.track(args.phase))
        elif args.phase in ("audit", "judge"):
            getattr(checker, args.phase)(policy=args.policy)
        else:
            getattr(checker, args.phase.replace("-", "_"))()
        print("OK: requested structural checks passed. This is not a market PASS.")
        return 0
    except (CheckError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
