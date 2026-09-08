"""Offline tests; synthetic records live only in TemporaryDirectory, never idea outputs.

Human/developer command: python -m unittest discover -s scripts -p test_check_geo_stage1.py
"""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from datetime import date
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("geo_checker", Path(__file__).with_name("check_geo_stage1.py"))
geo = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(geo)
ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "methodology/evidence-schema.json").read_text(encoding="utf-8"))


def record(index=0):
    return {"id": f"geo-market-test-{index}", "idea": geo.IDEA, "type": "pain",
            "observed_at": date.today().isoformat(), "source_date": None,
            "source_type": "community_post", "source_tier": "A",
            "source_url": f"https://example.com/synthetic-fixture/{index}",
            "observation": "Synthetic test-only observation, not market evidence.",
            "interpretation": "Synthetic fixture only.", "polarity": "supports", "strength": 3,
            "independence_key": f"synthetic-speaker-{index}", "agent": "market-research",
            "money_signal": "employee_time" if index % 2 else "saas_spend",
            "audit_status": "PENDING"}


class SchemaTests(unittest.TestCase):
    def test_current_schema_fully_supported(self):
        geo.check_schema_contract(SCHEMA)
        geo.validate_value(record(), SCHEMA)

    def test_rejects_unsupported_future_keyword(self):
        schema = copy.deepcopy(SCHEMA)
        schema["properties"]["id"]["pattern"] = "x"
        with self.assertRaises(geo.CheckError):
            geo.check_schema_contract(schema)

    def test_all_canonical_constraints(self):
        changes = [
            {"id": "a"}, {"idea": "x"}, {"type": "bad"}, {"observed_at": "2026-02-30"},
            {"source_date": "yesterday"}, {"source_type": "bad"}, {"source_tier": "D"},
            {"source_url": "x"}, {"source_excerpt": "x" * 501}, {"company": 123},
            {"observation": "short"}, {"interpretation": "x"}, {"recurrence": "yearly"},
            {"money_signal": "salary_guess"}, {"money_amount": -1}, {"money_amount": True},
            {"money_currency": 20}, {"polarity": "positive"}, {"strength": True},
            {"strength": 0}, {"strength": 6}, {"independence_key": "x"},
            {"agent": "x"}, {"audit_status": "PASS"}, {"audit_reason": False}, {"invented": 1},
        ]
        for delta in changes:
            with self.subTest(delta=delta):
                value = record()
                value.update(delta)
                with self.assertRaises(geo.CheckError):
                    geo.validate_value(value, SCHEMA)

    def test_missing_required_and_nonobject(self):
        value = record()
        del value["source_url"]
        for invalid in (value, [], None):
            with self.subTest(invalid=invalid), self.assertRaises(geo.CheckError):
                geo.validate_value(invalid, SCHEMA)

    def test_null_fields(self):
        value = record()
        for field, rule in SCHEMA["properties"].items():
            if isinstance(rule.get("type"), list) and "null" in rule["type"]:
                value[field] = None
        geo.validate_value(value, SCHEMA)

    def test_duplicate_properties_and_nonfinite(self):
        for text in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}'):
            with self.subTest(text=text), self.assertRaises(geo.CheckError):
                geo.parse_json(text)

    def test_url_identity_preserved(self):
        self.assertEqual(geo.normalized_url("https://example.com/r?ref=review1&utm_source=a#comment1"),
                         "https://example.com/r?ref=review1#comment1")


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        capture = redirect_stdout(StringIO())
        capture.__enter__()
        self.addCleanup(capture.__exit__, None, None, None)
        self.temp = tempfile.TemporaryDirectory(prefix="geo-stage1-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("methodology/evidence-schema.json", SCHEMA)
        self.checker = geo.Checker(self.root)

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content if isinstance(content, str) else json.dumps(content), encoding="utf-8")

    def fixture(self, count=20):
        raw = [record(i) for i in range(count)]
        for track in geo.TRACKS:
            rows = raw if track == "market" else []
            base = f"ideas/{geo.IDEA}/raw/{track}"
            self.write(f"{base}/evidence.jsonl", "\n".join(json.dumps(r) for r in rows))
            for report in geo.REPORTS[track]:
                self.write(f"{base}/{report}", "Synthetic report for checker tests only.")
            self.write(f"{base}/run-status.json", {"track": track, "status": "COMPLETE",
                       "validation": "PASS", "records": len(rows), "blockers": [], "next_actions": []})
        audited = [{**r, "audit_status": "VERIFIED", "audit_reason": "Synthetic checker test."} for r in raw]
        self.write_audit(audited)
        scope = {"scope_id": geo.SCOPE, "records": [{"evidence_id": r["id"], "scope_status": "IN_SCOPE",
                 "supporting_evidence_ids": [r["id"]], "reason": "Synthetic scope test only."} for r in audited]}
        self.write("ideas/geo-monitoring/evidence/scope-map.json", scope)
        for name in ("audit-summary.md", "high-impact-review.md"):
            self.write(f"ideas/geo-monitoring/evidence/{name}", "Synthetic test report.")
        return raw, audited, scope

    def write_audit(self, rows):
        self.write("ideas/geo-monitoring/evidence/evidence.jsonl", "\n".join(json.dumps(r) for r in rows))

    def scorecard(self, rows):
        ids = [r["id"] for r in rows]
        gates = {}
        for name in ("G1", "G2", "G3", "G4", "G5", "G6"):
            chosen = ids if name == "G1" else ids[:5] if name == "G3" else ids[:10] if name == "G4" else ids[:1]
            gates[name] = {"status": "PASS", "threshold_or_rule": "Synthetic gate fixture.",
                           "independent_count": len(chosen), "counted_evidence_ids": chosen,
                           "contradictory_evidence_ids": [], "high_impact_excluded": [],
                           "confidence": "HIGH", "material_unknowns": []}
        gates["G3"]["breakdown_by_category"] = dict(geo.Counter(geo.MONEY_CATEGORIES[r["money_signal"]] for r in rows[:5]))
        gates["G4"]["clusters"] = {"synthetic": ids[:10]}
        return {"idea_id": geo.IDEA, "evaluation_date": date.today().isoformat(), "verdict": "PASS",
                "rationale": "Synthetic checker fixture only.", "stage2_authorized": True,
                "evaluated_scope": {"scope_id": geo.SCOPE}, "gates": gates, "condition": None,
                "dimension_scores": {"pain_strength": 3}, "scope_integrity_notes": [],
                "candidate_scope_assessments": [], "strongest_positive_evidence": [],
                "strongest_negative_evidence": [], "top_unknowns": []}

    def save_score(self, card):
        self.write("ideas/geo-monitoring/output/scorecard.json", card)
        self.write("ideas/geo-monitoring/output/stage1-report.md", "Synthetic test report.")

    def test_missing_outputs_fail(self):
        with self.assertRaises(geo.CheckError):
            self.checker.raw_all()

    def test_zero_record_run_is_not_market_pass(self):
        self.fixture(0)
        self.assertEqual(self.checker.raw_all(), [])
        self.checker.audit()

    def test_full_pipeline_structure(self):
        _, audited, _ = self.fixture()
        self.save_score(self.scorecard(audited))
        self.checker.judge()

    def test_raw_not_pending(self):
        raw, _, _ = self.fixture()
        raw[0]["audit_status"] = "VERIFIED"
        self.write("ideas/geo-monitoring/raw/market/evidence.jsonl", "\n".join(json.dumps(r) for r in raw))
        with self.assertRaises(geo.CheckError):
            self.checker.raw_all()

    def test_duplicate_ids(self):
        self.fixture()
        self.write("ideas/geo-monitoring/raw/market/evidence.jsonl", json.dumps(record()) + "\n" + json.dumps(record()))
        with self.assertRaises(geo.CheckError):
            self.checker.track("market")

    def test_audit_cannot_drop_or_rewrite(self):
        _, audited, _ = self.fixture()
        self.write_audit(audited[:-1])
        with self.assertRaises(geo.CheckError):
            self.checker.audit()
        audited[0]["observation"] = "Unsupported rewritten observation for this test."
        self.write_audit(audited)
        with self.assertRaises(geo.CheckError):
            self.checker.audit()

    def test_scope_requires_verified_support(self):
        _, _, scope = self.fixture()
        scope["records"][0]["supporting_evidence_ids"] = []
        self.write("ideas/geo-monitoring/evidence/scope-map.json", scope)
        with self.assertRaises(geo.CheckError):
            self.checker.audit()

    def test_count_and_threshold_enforcement(self):
        _, audited, _ = self.fixture()
        card = self.scorecard(audited)
        card["gates"]["G1"]["independent_count"] = 99
        self.save_score(card)
        with self.assertRaises(geo.CheckError):
            self.checker.judge()
        card["gates"]["G1"]["counted_evidence_ids"] = [audited[0]["id"]]
        card["gates"]["G1"]["independent_count"] = 1
        self.save_score(card)
        with self.assertRaises(geo.CheckError):
            self.checker.judge()

    def test_unknown_scope_cannot_satisfy_gate(self):
        _, audited, scope = self.fixture()
        self.save_score(self.scorecard(audited))
        scope["records"][0]["scope_status"] = "UNKNOWN"
        self.write("ideas/geo-monitoring/evidence/scope-map.json", scope)
        with self.assertRaises(geo.CheckError):
            self.checker.judge()

    def test_verdict_consistency(self):
        _, audited, _ = self.fixture()
        card = self.scorecard(audited)
        card["verdict"] = "CONDITIONAL PASS"
        card["condition"] = "Synthetic question."
        for name in ("G2", "G5"):
            card["gates"][name]["status"] = "UNKNOWN"
        self.save_score(card)
        with self.assertRaises(geo.CheckError):
            self.checker.judge()
        card["gates"]["G5"]["status"] = "PASS"
        self.save_score(card)
        self.checker.judge()

    def test_auditor_can_normalize_keys_but_judge_cannot_double_count(self):
        _, audited, _ = self.fixture()
        audited[1]["independence_key"] = audited[0]["independence_key"]
        self.write_audit(audited)
        self.checker.audit()
        self.save_score(self.scorecard(audited))
        with self.assertRaises(geo.CheckError):
            self.checker.judge()

    def test_price_and_stated_intent_cannot_satisfy_wtp(self):
        for money_signal in ("competitor_price", "stated_wtp"):
            with self.subTest(money_signal=money_signal):
                raw, audited, _ = self.fixture()
                raw[0]["money_signal"] = money_signal
                audited[0]["money_signal"] = money_signal
                self.write("ideas/geo-monitoring/raw/market/evidence.jsonl", "\n".join(json.dumps(r) for r in raw))
                card = self.scorecard([record(i) for i in range(20)])
                self.write_audit(audited)
                self.save_score(card)
                with self.assertRaises(geo.CheckError):
                    self.checker.judge()

    def test_partial_audit_nonverified_cannot_carry_gate(self):
        _, audited, scope = self.fixture()
        card = self.scorecard(audited)
        audited[0]["audit_status"] = "PENDING"
        scope["records"][0]["scope_status"] = "UNKNOWN"
        scope["records"][0]["supporting_evidence_ids"] = []
        self.write_audit(audited)
        self.write("ideas/geo-monitoring/evidence/scope-map.json", scope)
        self.checker.audit()
        self.save_score(card)
        with self.assertRaises(geo.CheckError):
            self.checker.judge()

    def test_fail_requires_contradiction(self):
        _, audited, _ = self.fixture()
        card = self.scorecard(audited)
        card["verdict"] = "FAIL"
        card["stage2_authorized"] = False
        card["gates"]["G6"]["status"] = "FAIL"
        self.save_score(card)
        with self.assertRaises(geo.CheckError):
            self.checker.judge()

    def test_missing_scope_entry(self):
        _, _, scope = self.fixture()
        scope["records"].pop()
        self.write("ideas/geo-monitoring/evidence/scope-map.json", scope)
        with self.assertRaises(geo.CheckError):
            self.checker.audit()

    def test_partial_track_with_no_evidence(self):
        self.fixture(0)
        self.write("ideas/geo-monitoring/raw/wtp/run-status.json", {"track": "wtp", "status": "PARTIAL",
                   "validation": "PASS", "records": 0, "blockers": ["Synthetic quota failure"],
                   "next_actions": ["Resume after tool restoration"]})
        self.checker.raw_all()

    def test_outside_workspace_symlink_denied(self):
        (self.root / "escape").symlink_to(self.root.parent, target_is_directory=True)
        with self.assertRaises(geo.CheckError):
            self.checker.path("escape/example")


if __name__ == "__main__":
    unittest.main()
