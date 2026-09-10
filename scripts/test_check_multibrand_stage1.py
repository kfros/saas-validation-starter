"""Offline tests; synthetic records live only in TemporaryDirectory, never idea outputs.

Human/developer command: python -m unittest discover -s scripts -p test_check_multibrand_stage1.py
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

SPEC = importlib.util.spec_from_file_location("multibrand_checker", Path(__file__).with_name("check_multibrand_stage1.py"))
mb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mb)
import audit_review_pipeline as arp
ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "methodology/evidence-schema.json").read_text(encoding="utf-8"))


def record(index=0):
    return {"id": f"mb-market-test-{index}", "idea": mb.IDEA, "type": "pain",
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
        mb.check_schema_contract(SCHEMA)
        mb.validate_value(record(), SCHEMA)

    def test_rejects_unsupported_future_keyword(self):
        schema = copy.deepcopy(SCHEMA)
        schema["properties"]["id"]["pattern"] = "x"
        with self.assertRaises(mb.CheckError):
            mb.check_schema_contract(schema)

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
                with self.assertRaises(mb.CheckError):
                    mb.validate_value(value, SCHEMA)

    def test_missing_required_and_nonobject(self):
        value = record()
        del value["source_url"]
        for invalid in (value, [], None):
            with self.subTest(invalid=invalid), self.assertRaises(mb.CheckError):
                mb.validate_value(invalid, SCHEMA)

    def test_null_fields(self):
        value = record()
        for field, rule in SCHEMA["properties"].items():
            if isinstance(rule.get("type"), list) and "null" in rule["type"]:
                value[field] = None
        mb.validate_value(value, SCHEMA)

    def test_duplicate_properties_and_nonfinite(self):
        for text in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}'):
            with self.subTest(text=text), self.assertRaises(mb.CheckError):
                mb.parse_json(text)

    def test_url_identity_preserved(self):
        self.assertEqual(mb.normalized_url("https://example.com/r?ref=review1&utm_source=a#comment1"),
                         "https://example.com/r?ref=review1#comment1")


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        capture = redirect_stdout(StringIO())
        capture.__enter__()
        self.addCleanup(capture.__exit__, None, None, None)
        self.temp = tempfile.TemporaryDirectory(prefix="mb-stage1-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("methodology/evidence-schema.json", SCHEMA)
        self.checker = mb.Checker(self.root)

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content if isinstance(content, str) else json.dumps(content), encoding="utf-8")

    def fixture(self, count=20):
        raw = [record(i) for i in range(count)]
        for track in mb.TRACKS:
            rows = raw if track == "market" else []
            base = f"ideas/{mb.IDEA}/raw/{track}"
            self.write(f"{base}/evidence.jsonl", "\n".join(json.dumps(r) for r in rows))
            for report in mb.REPORTS[track]:
                self.write(f"{base}/{report}", "Synthetic report for checker tests only.")
            self.write(f"{base}/run-status.json", {"track": track, "status": "COMPLETE",
                       "validation": "PASS", "records": len(rows), "blockers": [], "next_actions": []})
        raw_by_id, locations = arp.load_raw(self.root)
        captures, reviews = [], []
        for r in raw:
            cid = f"capture-{r['id']}"
            fragment = "Synthetic test-only returned fragment."
            captures.append({"schema_version": 1, "capture_id": cid,
                "requested_url": r["source_url"], "resolved_url": r["source_url"],
                "locator": "synthetic fixture paragraph", "attributed_speaker": None,
                "inspected_at": "2026-09-09T10:00:00+00:00", "retrieval_tool": "synthetic-test-tool",
                "external_result_id": None, "local_attempt_id": f"attempt-{r['id']}",
                "outcome": "SUCCESS", "fragment": fragment,
                "fragment_sha256": arp.fragment_fingerprint(fragment)})
            claims = []
            for field in sorted(arp.expected_claim_fields(r)):
                decision = "NOT_APPLICABLE" if field in {"money_amount", "money_currency", "money_period"} else "SUPPORTED"
                claims.append({"field": field, "decision": decision,
                    "reason": "Synthetic explicit claim decision.", "capture_id": cid,
                    "speaker": None, "material": True})
            review = {"schema_version": 1, "evidence_id": r["id"], "raw_track": "market",
                "raw_path": locations[r["id"]], "raw_fingerprint": arp.fingerprint(r),
                "scope_dependency_fingerprint": "", "reviewed_at": "2026-09-09T10:00:00+00:00",
                "reviewer_agent": "synthetic-test", "state": "COMPLETE", "blocker": None,
                "capture_ids": [cid], "claim_decisions": claims,
                "audit": {"status": "VERIFIED", "reason": "Synthetic checker test.",
                          "independence_key": r["independence_key"]},
                "scope": {"scope_status": "IN_SCOPE", "provider_form": "SOLO",
                          "supporting_evidence_ids": [r["id"]], "reason": "Synthetic scope test only."},
                "money_assessment": {"payer": "Synthetic payer", "recipient": "Synthetic recipient",
                    "work_bought_or_done": "Synthetic test-only work.",
                    "payment_status": "PAID" if r["money_signal"] == "saas_spend" else "UNKNOWN",
                    "transaction_type": "ACTUAL", "amount_basis": None,
                    "unresolved_unknowns": ["Synthetic amount is intentionally unknown."]},
                "impact_assessment": {"eligible_gates": [f"G{i}" for i in range(1, 7)], "exclusion_reason": None,
                                      "unresolved_questions": []},
                "substitute_assessment": None,
                "discrepancies": [], "raw_owner_repairs": []}
            review["scope_dependency_fingerprint"] = arp.scope_dependency(review, raw_by_id)
            reviews.append(review)
        review_dir = self.root / "ideas/multi-brand-content/evidence/source-reviews"
        arp.write_jsonl(review_dir / "captures.jsonl", captures)
        arp.write_jsonl(review_dir / "reviews.jsonl", reviews)
        arp.render_candidate(self.root, review_dir,
                             self.root / "ideas/multi-brand-content/evidence")
        audited = arp.read_jsonl(self.root / "ideas/multi-brand-content/evidence/evidence.jsonl", "test evidence")
        scope = arp.read_json(self.root / "ideas/multi-brand-content/evidence/scope-map.json")
        return raw, audited, scope

    def sync_review_bundle(self):
        raw_by_id, locations = arp.load_raw(self.root)
        review_dir = self.root / "ideas/multi-brand-content/evidence/source-reviews"
        reviews = arp.read_jsonl(review_dir / "reviews.jsonl", "test reviews")
        for review in reviews:
            rid = review["evidence_id"]
            review["raw_path"] = locations[rid]
            review["raw_fingerprint"] = arp.fingerprint(raw_by_id[rid])
            review["scope_dependency_fingerprint"] = arp.scope_dependency(review, raw_by_id)
        arp.write_jsonl(review_dir / "reviews.jsonl", reviews)
        arp.render_candidate(self.root, review_dir,
                             self.root / "ideas/multi-brand-content/evidence")
        return reviews

    def write_audit(self, rows):
        self.write("ideas/multi-brand-content/evidence/evidence.jsonl", "\n".join(json.dumps(r) for r in rows))

    def scorecard(self, rows):
        ids = [r["id"] for r in rows]
        gates = {}
        for name in ("G1", "G2", "G3", "G4", "G5", "G6"):
            chosen = ids if name == "G1" else ids[:5] if name == "G3" else ids[:10] if name == "G4" else ids[:1]
            gates[name] = {"status": "PASS", "threshold_or_rule": "Synthetic gate fixture.",
                           "independent_count": len(chosen), "counted_evidence_ids": chosen,
                           "contradictory_evidence_ids": [], "high_impact_excluded": [],
                           "counted_evidence_reasons": {rid: "Synthetic direct-support reason." for rid in chosen},
                           "provider_form_breakdown": {"SOLO": len(chosen), "AGENCY": 0, "UNKNOWN": 0},
                           "confidence": "HIGH", "material_unknowns": []}
        gates["G3"]["breakdown_by_category"] = dict(mb.Counter(mb.MONEY_CATEGORIES[r["money_signal"]] for r in rows[:5]))
        gates["G4"]["clusters"] = {"synthetic": ids[:10]}
        return {"idea_id": mb.IDEA, "evaluation_date": date.today().isoformat(), "verdict": "PASS",
                "rationale": "Synthetic checker fixture only.", "stage2_authorized": True,
                "evaluated_scope": {"scope_id": mb.SCOPE}, "gates": gates, "condition": None,
                "dataset_summary": mb.dataset_summary({r["id"]: r for r in rows},
                    {r["id"]: {"scope_status": "IN_SCOPE", "provider_form": "SOLO"} for r in rows}),
                "dimension_scores": {name: 3 for name in mb.DIMENSIONS}, "scope_integrity_notes": [],
                "candidate_scope_assessments": [], "strongest_positive_evidence": [],
                "strongest_negative_evidence": [], "top_unknowns": []}

    def save_score(self, card):
        self.write("ideas/multi-brand-content/output/scorecard.json", card)
        self.write("ideas/multi-brand-content/output/stage1-report.md", "Synthetic test report.")

    def test_missing_outputs_fail(self):
        with self.assertRaises(mb.CheckError):
            self.checker.raw_all()

    def test_zero_record_run_is_not_market_pass(self):
        self.fixture(0)
        self.assertEqual(self.checker.raw_all(), [])
        self.checker.audit()

    def test_full_pipeline_structure(self):
        _, audited, _ = self.fixture()
        self.save_score(self.scorecard(audited))
        self.checker.judge()

    def test_judge_rejects_source_review_gate_exclusion(self):
        _, audited, _ = self.fixture()
        review_dir = self.root / "ideas/multi-brand-content/evidence/source-reviews"
        reviews = arp.read_jsonl(review_dir / "reviews.jsonl", "synthetic reviews")
        for review in reviews:
            review["impact_assessment"] = {"eligible_gates": [],
                "exclusion_reason": "Synthetic explicit exclusion from every gate.",
                "unresolved_questions": []}
        arp.write_jsonl(review_dir / "reviews.jsonl", reviews)
        arp.render_candidate(self.root, review_dir,
                             self.root / "ideas/multi-brand-content/evidence")
        self.save_score(self.scorecard(audited))
        with self.assertRaisesRegex(mb.CheckError, "excluded or not eligible"):
            self.checker.judge()

    def test_raw_not_pending(self):
        raw, _, _ = self.fixture()
        raw[0]["audit_status"] = "VERIFIED"
        self.write("ideas/multi-brand-content/raw/market/evidence.jsonl", "\n".join(json.dumps(r) for r in raw))
        with self.assertRaises(mb.CheckError):
            self.checker.raw_all()

    def test_duplicate_ids(self):
        self.fixture()
        self.write("ideas/multi-brand-content/raw/market/evidence.jsonl", json.dumps(record()) + "\n" + json.dumps(record()))
        with self.assertRaises(mb.CheckError):
            self.checker.track("market")

    def test_audit_cannot_drop_or_rewrite(self):
        _, audited, _ = self.fixture()
        self.write_audit(audited[:-1])
        with self.assertRaises(mb.CheckError):
            self.checker.audit()
        audited[0]["observation"] = "Unsupported rewritten observation for this test."
        self.write_audit(audited)
        with self.assertRaises(mb.CheckError):
            self.checker.audit()

    def test_scope_requires_verified_support(self):
        _, _, scope = self.fixture()
        scope["records"][0]["supporting_evidence_ids"] = []
        self.write("ideas/multi-brand-content/evidence/scope-map.json", scope)
        with self.assertRaises(mb.CheckError):
            self.checker.audit()

    def test_count_and_threshold_enforcement(self):
        _, audited, _ = self.fixture()
        card = self.scorecard(audited)
        card["gates"]["G1"]["independent_count"] = 99
        self.save_score(card)
        with self.assertRaises(mb.CheckError):
            self.checker.judge()
        card["gates"]["G1"]["counted_evidence_ids"] = [audited[0]["id"]]
        card["gates"]["G1"]["independent_count"] = 1
        self.save_score(card)
        with self.assertRaises(mb.CheckError):
            self.checker.judge()

    def test_unknown_scope_cannot_satisfy_gate(self):
        _, audited, scope = self.fixture()
        self.save_score(self.scorecard(audited))
        scope["records"][0]["scope_status"] = "UNKNOWN"
        self.write("ideas/multi-brand-content/evidence/scope-map.json", scope)
        with self.assertRaises(mb.CheckError):
            self.checker.judge()

    def test_verdict_consistency(self):
        _, audited, _ = self.fixture()
        card = self.scorecard(audited)
        card["verdict"] = "CONDITIONAL PASS"
        card["condition"] = "Synthetic question."
        for name in ("G2", "G5"):
            card["gates"][name]["status"] = "UNKNOWN"
        self.save_score(card)
        with self.assertRaises(mb.CheckError):
            self.checker.judge()
        card["gates"]["G5"]["status"] = "PASS"
        self.save_score(card)
        self.checker.judge()

    def test_auditor_can_normalize_keys_but_judge_cannot_double_count(self):
        _, audited, _ = self.fixture()
        review_dir = self.root / "ideas/multi-brand-content/evidence/source-reviews"
        reviews = arp.read_jsonl(review_dir / "reviews.jsonl", "test reviews")
        reviews[1]["audit"]["independence_key"] = reviews[0]["audit"]["independence_key"]
        arp.write_jsonl(review_dir / "reviews.jsonl", reviews)
        arp.render_candidate(self.root, review_dir,
                             self.root / "ideas/multi-brand-content/evidence")
        self.checker.audit()
        self.save_score(self.scorecard(audited))
        with self.assertRaises(mb.CheckError):
            self.checker.judge()

    def test_price_and_stated_intent_cannot_satisfy_wtp(self):
        for money_signal in ("competitor_price", "stated_wtp"):
            with self.subTest(money_signal=money_signal):
                raw, audited, _ = self.fixture()
                raw[0]["money_signal"] = money_signal
                self.write("ideas/multi-brand-content/raw/market/evidence.jsonl", "\n".join(json.dumps(r) for r in raw))
                review_dir = self.root / "ideas/multi-brand-content/evidence/source-reviews"
                reviews = arp.read_jsonl(review_dir / "reviews.jsonl", "synthetic reviews")
                reviews[0]["money_assessment"].update(
                    payment_status="UNKNOWN",
                    transaction_type="OFFER" if money_signal == "competitor_price" else "INTENT")
                arp.write_jsonl(review_dir / "reviews.jsonl", reviews)
                card = self.scorecard([record(i) for i in range(20)])
                self.sync_review_bundle()
                self.save_score(card)
                with self.assertRaises(mb.CheckError):
                    self.checker.judge()

    def test_partial_audit_nonverified_cannot_carry_gate(self):
        _, audited, _ = self.fixture()
        card = self.scorecard(audited)
        review_dir = self.root / "ideas/multi-brand-content/evidence/source-reviews"
        reviews = arp.read_jsonl(review_dir / "reviews.jsonl", "test reviews")
        reviews[0]["audit"]["status"] = "PARTIALLY_VERIFIED"
        reviews[0]["claim_decisions"][0]["decision"] = "UNKNOWN"
        reviews[0]["scope"].update(scope_status="UNKNOWN", supporting_evidence_ids=[])
        raw_by_id, _ = arp.load_raw(self.root)
        reviews[0]["scope_dependency_fingerprint"] = arp.scope_dependency(reviews[0], raw_by_id)
        arp.write_jsonl(review_dir / "reviews.jsonl", reviews)
        arp.render_candidate(self.root, review_dir,
                             self.root / "ideas/multi-brand-content/evidence")
        self.checker.audit()
        self.save_score(card)
        with self.assertRaises(mb.CheckError):
            self.checker.judge()

    def test_fail_requires_contradiction(self):
        _, audited, _ = self.fixture()
        card = self.scorecard(audited)
        card["verdict"] = "FAIL"
        card["stage2_authorized"] = False
        card["gates"]["G6"]["status"] = "FAIL"
        self.save_score(card)
        with self.assertRaises(mb.CheckError):
            self.checker.judge()

    def test_missing_scope_entry(self):
        _, _, scope = self.fixture()
        scope["records"].pop()
        self.write("ideas/multi-brand-content/evidence/scope-map.json", scope)
        with self.assertRaises(mb.CheckError):
            self.checker.audit()

    def test_partial_track_with_no_evidence(self):
        self.fixture(0)
        self.write("ideas/multi-brand-content/raw/wtp/run-status.json", {"track": "wtp", "status": "PARTIAL",
                   "validation": "PASS", "records": 0, "blockers": ["Synthetic quota failure"],
                   "next_actions": ["Resume after tool restoration"]})
        self.checker.raw_all()

    def test_outside_workspace_path_denied(self):
        with self.assertRaises(mb.CheckError):
            self.checker.path("../outside/example")

    def test_summary_counts_rows_and_entities_separately(self):
        _, rows, mapping = self.fixture(4)
        rows[1]["independence_key"] = rows[0]["independence_key"]
        rows[2]["audit_status"] = "PARTIALLY_VERIFIED"
        mapping["records"][2]["scope_status"] = "UNKNOWN"
        mapping["records"][3]["scope_status"] = "OUT_OF_SCOPE"
        mapping["records"][3]["provider_form"] = "AGENCY"
        actual = mb.dataset_summary({r["id"]: r for r in rows},
                                    {r["evidence_id"]: r for r in mapping["records"]})
        self.assertEqual(actual["total_records"], 4)
        self.assertEqual(actual["verified_independence_keys"], 2)
        self.assertEqual(actual["by_audit_status"]["VERIFIED"], 3)
        self.assertEqual(actual["by_audit_status"]["PENDING"], 0)
        self.assertEqual(actual["by_scope"]["IN_SCOPE"],
                         {"records": 2, "verified_records": 2, "verified_independence_keys": 1})
        self.assertEqual(actual["by_scope"]["UNKNOWN"]["verified_records"], 0)
        self.assertEqual(actual["by_provider_form"]["AGENCY"]["verified_records"], 1)

    def test_wrong_summary_rejected(self):
        _, rows, _ = self.fixture()
        card = self.scorecard(rows)
        card["dataset_summary"]["verified_independence_keys"] = 49
        self.save_score(card)
        with self.assertRaisesRegex(mb.CheckError, "dataset summary"):
            self.checker.judge()

    def test_missing_counted_reason_rejected(self):
        _, rows, _ = self.fixture()
        card = self.scorecard(rows)
        card["gates"]["G1"]["counted_evidence_reasons"].pop(rows[0]["id"])
        self.save_score(card)
        with self.assertRaisesRegex(mb.CheckError, "direct-support reason"):
            self.checker.judge()

    def test_wrong_provider_form_breakdown_rejected(self):
        _, rows, _ = self.fixture()
        card = self.scorecard(rows)
        card["gates"]["G3"]["provider_form_breakdown"] = {"SOLO": 0, "AGENCY": 5, "UNKNOWN": 0}
        self.save_score(card)
        with self.assertRaisesRegex(mb.CheckError, "provider form counts"):
            self.checker.judge()

    def test_labor_labels_do_not_manufacture_spend_diversity(self):
        raw, rows, _ = self.fixture()
        for index, row in enumerate(raw):
            row["money_signal"] = "employee_time" if index % 2 else "dedicated_role"
            rows[index]["money_signal"] = row["money_signal"]
        self.write("ideas/multi-brand-content/raw/market/evidence.jsonl",
                   "\n".join(json.dumps(r) for r in raw))
        self.sync_review_bundle()
        self.save_score(self.scorecard(rows))
        with self.assertRaisesRegex(mb.CheckError, "2 categories"):
            self.checker.judge()

    def test_unknown_buyer_cannot_decisively_falsify_scope(self):
        _, rows, _ = self.fixture(21)
        review_dir = self.root / "ideas/multi-brand-content/evidence/source-reviews"
        reviews = arp.read_jsonl(review_dir / "reviews.jsonl", "test reviews")
        reviews[-1]["scope"].update(scope_status="UNKNOWN", supporting_evidence_ids=[])
        raw_by_id, _ = arp.load_raw(self.root)
        reviews[-1]["scope_dependency_fingerprint"] = arp.scope_dependency(reviews[-1], raw_by_id)
        arp.write_jsonl(review_dir / "reviews.jsonl", reviews)
        arp.render_candidate(self.root, review_dir,
                             self.root / "ideas/multi-brand-content/evidence")
        mapping = arp.read_json(self.root / "ideas/multi-brand-content/evidence/scope-map.json")
        unknown_id = reviews[-1]["evidence_id"]
        counted_rows = [row for row in rows if row["id"] != unknown_id]
        card = self.scorecard(counted_rows)
        card["dataset_summary"] = mb.dataset_summary({r["id"]: r for r in rows},
                                    {r["evidence_id"]: r for r in mapping["records"]})
        card["gates"]["G1"]["contradictory_evidence_ids"] = [unknown_id]
        self.save_score(card)
        with self.assertRaisesRegex(mb.CheckError, "decisive contradiction"):
            self.checker.judge()

    def test_cannot_claim_insufficient_with_all_gates_passing(self):
        _, rows, _ = self.fixture()
        card = self.scorecard(rows)
        card["verdict"] = "INSUFFICIENT EVIDENCE"
        card["stage2_authorized"] = False
        self.save_score(card)
        with self.assertRaisesRegex(mb.CheckError, "insufficient verdict"):
            self.checker.judge()

    def test_empty_partial_research_can_finish_insufficient(self):
        _, rows, _ = self.fixture(0)
        card = self.scorecard(rows)
        card.update(verdict="INSUFFICIENT EVIDENCE", stage2_authorized=False)
        for gate in card["gates"].values():
            gate.update(status="UNKNOWN", confidence="UNKNOWN", material_unknowns=["Synthetic missing evidence."])
        self.save_score(card)
        self.checker.judge()

    def test_pass_cannot_be_transferred_to_new_scope(self):
        _, rows, _ = self.fixture()
        card = self.scorecard(rows)
        card["candidate_scope_assessments"] = [
            {"scope_id": "SYNTHETIC-ADJACENT", "status": "PASS", "reason": "Synthetic invalid rescue."}]
        self.save_score(card)
        with self.assertRaisesRegex(mb.CheckError, "UNVALIDATED"):
            self.checker.judge()

    def test_scorecard_exclusion_cannot_invent_record(self):
        _, rows, _ = self.fixture()
        card = self.scorecard(rows)
        card["gates"]["G1"]["high_impact_excluded"] = [
            {"evidence_id": "mb-pain-not-collected", "reason": "Synthetic invalid ID."}]
        self.save_score(card)
        with self.assertRaisesRegex(mb.CheckError, "existing evidence_id"):
            self.checker.judge()


if __name__ == "__main__":
    unittest.main()
