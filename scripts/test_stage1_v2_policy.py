#!/usr/bin/env python3
"""Synthetic offline tests for Stage 1 v2 policy, checkers, and immutability manifest.

All synthetic test records live in TemporaryDirectory, never idea outputs.
Verifies structure, arithmetic, boundary conditions, and immutability.
"""
from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
import sys
from datetime import date
from pathlib import Path

SCRIPTS_DIR = str(Path(__file__).resolve().parent)
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)
import stage1_policy

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_FILE = ROOT / "scripts" / "historical_manifest_3bf758f.json"
SCHEMA = json.loads((ROOT / "methodology/evidence-schema.json").read_text(encoding="utf-8"))


def compute_file_sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def make_record(index: int = 0, idea: str = "geo-monitoring", money_signal: str = "saas_spend",
                audit_status: str = "VERIFIED", polarity: str = "supports",
                key: str | None = None, money_amount: float | None = 100.0) -> dict:
    return {
        "id": f"{idea}-test-{index}",
        "idea": idea,
        "type": "pain",
        "observed_at": date.today().isoformat(),
        "source_date": None,
        "source_type": "community_post",
        "source_tier": "A",
        "source_url": f"https://example.com/fixture/{index}",
        "observation": f"Synthetic test observation {index}.",
        "interpretation": f"Synthetic fixture {index}.",
        "polarity": polarity,
        "strength": 3,
        "independence_key": key or f"speaker-{index}",
        "agent": "market-research",
        "money_signal": money_signal,
        "money_amount": money_amount,
        "money_currency": "USD" if money_amount else None,
        "money_period": "month" if money_amount else None,
        "audit_status": audit_status,
        "audit_reason": "Synthetic fixture check.",
    }


def make_v2_scorecard(rows: list[dict], idea: str = "geo-monitoring", scope_id: str = "GEO-AGENCY-01",
                      verdict: str = "PASS") -> dict:
    ids = [r["id"] for r in rows]
    gates = {}
    for name in ("G1", "G2", "G3", "G4", "G5", "G6"):
        if name == "G1":
            chosen = ids[:5]
        elif name == "G3":
            chosen = ids[:3]
        elif name == "G4":
            chosen = ids[:3]
        else:
            chosen = ids[:1]
        gates[name] = {
            "status": "PASS",
            "threshold_or_rule": f"Synthetic v2 rule for {name}.",
            "independent_count": len(chosen),
            "counted_evidence_ids": chosen,
            "contradictory_evidence_ids": [],
            "high_impact_excluded": [],
            "confidence": "HIGH" if name in ("G2", "G5") else "MEDIUM",
            "material_unknowns": [],
        }

    gates["G3"]["breakdown_by_category"] = dict(
        stage1_policy.Counter(stage1_policy.MONEY_CATEGORIES[r["money_signal"]] for r in rows[:3])
    )
    gates["G4"]["clusters"] = {"core_gap_cluster": ids[:3]}

    card = {
        "policy_version": "v2",
        "input_commit_or_snapshot": "3bf758f",
        "idea_id": idea,
        "evaluation_date": date.today().isoformat(),
        "verdict": verdict,
        "rationale": "Synthetic fixture evaluation.",
        "stage2_authorized": verdict in ("PASS", "CONDITIONAL PASS"),
        "recommended_next_action": "LIMITED_CUSTOMER_DISCOVERY" if verdict in ("PASS", "CONDITIONAL PASS") else "STOP",
        "evaluated_scope": {"scope_id": scope_id},
        "gates": gates,
        "conditions": None,
        "discovery_plan": None,
        "dimension_scores": {"pain_strength": 4},
        "scope_integrity_notes": ["Synthetic test notes."],
        "candidate_scope_assessments": [],
        "strongest_positive_evidence": ids[:2],
        "strongest_negative_evidence": [],
        "top_unknowns": [],
    }
    return card


class HistoricalImmutabilityTests(unittest.TestCase):
    def test_historical_files_match_manifest_hashes(self):
        """Historical files at 3bf758f must remain 100% byte-for-byte unchanged."""
        self.assertTrue(MANIFEST_FILE.is_file(), f"missing manifest: {MANIFEST_FILE}")
        manifest_data = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
        files = manifest_data.get("files", {})
        self.assertGreater(len(files), 50, "manifest must contain historical files")

        mismatches = []
        for rel_path, expected_hash in files.items():
            full_path = ROOT / rel_path
            if not full_path.is_file():
                mismatches.append(f"missing file: {rel_path}")
                continue
            actual_hash = compute_file_sha256(full_path)
            if actual_hash != expected_hash:
                mismatches.append(f"hash mismatch for {rel_path}: expected {expected_hash}, got {actual_hash}")

        self.assertEqual(mismatches, [], f"Historical immutability violated: {mismatches}")


class PolicyEngineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="stage1-v2-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_policy_definitions_loaded(self):
        defs = stage1_policy.load_policy_definitions()
        self.assertIn("v1", defs)
        self.assertIn("v2", defs)
        self.assertEqual(defs["v2"]["gates"]["G1"]["min_independent_count"], 5)
        self.assertEqual(defs["v2"]["gates"]["G3"]["min_independent_count"], 3)
        self.assertEqual(defs["v2"]["gates"]["G4"]["min_independent_count"], 3)

    def test_deterministic_layout_resolution(self):
        idea_dir = self.root / "ideas" / "geo-monitoring"
        l_v1 = stage1_policy.resolve_layout(idea_dir, "v1")
        self.assertEqual(l_v1["layout_name"], "legacy")
        self.assertEqual(l_v1["evidence_dir"], idea_dir / "evidence")

        l_v2 = stage1_policy.resolve_layout(idea_dir, "v2")
        self.assertEqual(l_v2["layout_name"], "reassessment-v2")
        self.assertEqual(l_v2["evidence_dir"], idea_dir / "reassessment-v2" / "evidence")

        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.resolve_layout(idea_dir, "v3")

    def test_policy_detection_and_mismatch(self):
        # 1. Missing policy_version in legacy layout defaults to v1
        detected = stage1_policy.detect_policy_from_scorecard({}, None, "legacy")
        self.assertEqual(detected, "v1")

        # 2. Missing policy_version in reassessment-v2 layout fails closed
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.detect_policy_from_scorecard({}, None, "reassessment-v2")

        # 3. v1 scorecard in reassessment-v2 layout fails closed
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.detect_policy_from_scorecard({"policy_version": "v1"}, None, "reassessment-v2")

        # 4. v2 scorecard in legacy layout fails closed
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.detect_policy_from_scorecard({"policy_version": "v2"}, None, "legacy")

        # 5. Unknown policy version fails
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.detect_policy_from_scorecard({"policy_version": "v99"}, None, "reassessment-v2")


class V2ThresholdAndBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.rows = [make_record(i) for i in range(10)]
        self.records = {r["id"]: r for r in self.rows}
        self.scope = {r["id"]: {"scope_status": "IN_SCOPE"} for r in self.rows}

    def test_v2_exact_pass_boundary(self):
        card = make_v2_scorecard(self.rows, verdict="PASS")
        stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope)

    def test_v2_g1_fails_below_5(self):
        card = make_v2_scorecard(self.rows, verdict="PASS")
        card["gates"]["G1"]["counted_evidence_ids"] = [self.rows[i]["id"] for i in range(4)]
        card["gates"]["G1"]["independent_count"] = 4
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope)

    def test_v2_g3_passes_with_1_category_and_3_signals(self):
        # All 3 records have saas_spend (paid_tool_or_pilot)
        card = make_v2_scorecard(self.rows, verdict="PASS")
        self.assertEqual(card["gates"]["G3"]["independent_count"], 3)
        self.assertEqual(len(card["gates"]["G3"]["breakdown_by_category"]), 1)
        stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope)

    def test_v2_g3_fails_below_3(self):
        card = make_v2_scorecard(self.rows, verdict="PASS")
        card["gates"]["G3"]["counted_evidence_ids"] = [self.rows[0]["id"], self.rows[1]["id"]]
        card["gates"]["G3"]["independent_count"] = 2
        card["gates"]["G3"]["breakdown_by_category"] = {"paid_tool_or_pilot": 2}
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope)

    def test_v2_g3_stated_wtp_and_competitor_price_rejected_from_counted(self):
        for ms in ("competitor_price", "stated_wtp"):
            with self.subTest(ms=ms):
                bad_rows = copy.deepcopy(self.rows)
                card = make_v2_scorecard(self.rows, verdict="PASS")
                bad_rows[0]["money_signal"] = ms
                card["gates"]["G3"]["breakdown_by_category"] = {ms: 1, "paid_tool_or_pilot": 2}
                records = {r["id"]: r for r in bad_rows}
                with self.assertRaises(stage1_policy.PolicyError):
                    stage1_policy.validate_scorecard_against_policy(card, "v2", records, self.scope)

    def test_v2_g3_unpriced_costly_labor_qualifies(self):
        labor_rows = copy.deepcopy(self.rows)
        labor_rows[0]["money_signal"] = "employee_time"
        labor_rows[0]["money_amount"] = None  # No invented dollar amount
        labor_rows[0]["money_currency"] = None
        records = {r["id"]: r for r in labor_rows}
        card = make_v2_scorecard(labor_rows, verdict="PASS")
        card["gates"]["G3"]["breakdown_by_category"] = {"paid_tool_or_pilot": 2, "employee_time": 1}
        stage1_policy.validate_scorecard_against_policy(card, "v2", records, self.scope)

    def test_v2_g4_requires_coherent_cluster_of_size_at_least_3(self):
        card = make_v2_scorecard(self.rows, verdict="PASS")
        # Split into 3 unrelated complaints (each size 1)
        card["gates"]["G4"]["clusters"] = {
            "unrelated_1": [self.rows[0]["id"]],
            "unrelated_2": [self.rows[1]["id"]],
            "unrelated_3": [self.rows[2]["id"]],
        }
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope)

    def test_deduplication_by_independence_key(self):
        dup_rows = copy.deepcopy(self.rows)
        dup_rows[1]["independence_key"] = dup_rows[0]["independence_key"]
        records = {r["id"]: r for r in dup_rows}
        card = make_v2_scorecard(dup_rows, verdict="PASS")
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", records, self.scope)


class V2ConditionalPassAndDiscoveryPlanTests(unittest.TestCase):
    def setUp(self):
        self.rows = [make_record(i) for i in range(10)]
        self.records = {r["id"]: r for r in self.rows}
        self.scope = {r["id"]: {"scope_status": "IN_SCOPE"} for r in self.rows}

    def test_valid_conditional_pass_with_interview_conditions(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        # G2 and G3 are UNKNOWN
        card["gates"]["G2"]["status"] = "UNKNOWN"
        card["gates"]["G3"]["status"] = "UNKNOWN"

        card["discovery_plan"] = {
            "interview_cap": 8,
            "target_respondent_profile": "Managing Director of 2-20 staff SEO agency",
            "review_deadline": "2026-10-01",
            "nonresponse_policy": "Treat recruitment failure as inconclusive market evidence.",
        }
        card["conditions"] = [
            {
                "condition_id": "cond-geo-recurrence",
                "gate_ids": ["G2"],
                "resolution_method": "INTERVIEW",
                "exact_unknown": "Is monthly AI answer tracking an actual recurring client deliverable?",
                "supporting_evidence_ids": [self.rows[0]["id"]],
                "respondent_qualification": "SEO Agency MD or Head of SEO",
                "observable_information_to_request": "Frequency and format of recent client AI search reports.",
                "continue_criteria": "At least 4 of 8 agencies confirm recurring monthly deliverables.",
                "stop_criteria": "Fewer than 2 agencies report recurring deliverable需求.",
            },
            {
                "condition_id": "cond-geo-wtp",
                "gate_ids": ["G3"],
                "resolution_method": "INTERVIEW",
                "exact_unknown": "Are agencies willing to pay $100+/mo separately for monitoring?",
                "supporting_evidence_ids": [self.rows[1]["id"]],
                "respondent_qualification": "Agency owner with budget authority",
                "observable_information_to_request": "Current software tool subscriptions and budget line items.",
                "continue_criteria": "Target budget identified in >= 3 interviews.",
                "stop_criteria": "Strict refusal to add dedicated monitoring line item across interviews.",
            },
        ]
        stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope)

    def test_conditional_pass_rejected_if_g1_not_pass(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G1"]["status"] = "UNKNOWN"
        card["discovery_plan"] = {"interview_cap": 8, "target_respondent_profile": "x", "review_deadline": "x", "nonresponse_policy": "x"}
        card["conditions"] = [{
            "condition_id": "cond-1", "gate_ids": ["G1"], "resolution_method": "INTERVIEW",
            "exact_unknown": "x", "supporting_evidence_ids": [], "respondent_qualification": "x",
            "observable_information_to_request": "x", "continue_criteria": "x", "stop_criteria": "x",
        }]
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope)

    def test_conditional_pass_rejected_if_any_gate_fails(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G6"]["status"] = "FAIL"
        card["discovery_plan"] = {"interview_cap": 8, "target_respondent_profile": "x", "review_deadline": "x", "nonresponse_policy": "x"}
        card["conditions"] = []
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope)

    def test_conditional_pass_rejected_if_resolution_method_is_technical_check(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G6"]["status"] = "UNKNOWN"
        card["discovery_plan"] = {"interview_cap": 8, "target_respondent_profile": "x", "review_deadline": "x", "nonresponse_policy": "x"}
        card["conditions"] = [{
            "condition_id": "cond-tech", "gate_ids": ["G6"], "resolution_method": "TECHNICAL_CHECK",
            "exact_unknown": "API access viability", "supporting_evidence_ids": [],
            "respondent_qualification": "Developer", "observable_information_to_request": "API limits",
            "continue_criteria": "API allowed", "stop_criteria": "API prohibited",
        }]
        # Technical blockers cannot be disguised as buyer interviews for CONDITIONAL PASS
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope)

    def test_conditional_pass_rejected_if_interview_cap_exceeds_8(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G2"]["status"] = "UNKNOWN"
        card["discovery_plan"] = {"interview_cap": 12, "target_respondent_profile": "x", "review_deadline": "x", "nonresponse_policy": "x"}
        card["conditions"] = [{
            "condition_id": "cond-2", "gate_ids": ["G2"], "resolution_method": "INTERVIEW",
            "exact_unknown": "x", "supporting_evidence_ids": [], "respondent_qualification": "x",
            "observable_information_to_request": "x", "continue_criteria": "x", "stop_criteria": "x",
        }]
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope)


class CheckerV2IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="checker-v2-integration-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

        # Write schema and policy
        (self.root / "methodology").mkdir(parents=True, exist_ok=True)
        (self.root / "methodology" / "evidence-schema.json").write_text(json.dumps(SCHEMA), encoding="utf-8")
        (self.root / "methodology" / "stage1-policy.json").write_text(
            (ROOT / "methodology" / "stage1-policy.json").read_text(encoding="utf-8"), encoding="utf-8"
        )
        (self.root / "methodology" / "evidence-standard.md").write_text("Standard", encoding="utf-8")
        (self.root / "methodology" / "stage1-gates.md").write_text("Gates", encoding="utf-8")
        (self.root / "methodology" / "scoring.md").write_text("Scoring", encoding="utf-8")

        (self.root / ".agent" / "rules").mkdir(parents=True, exist_ok=True)
        (self.root / ".agent" / "rules" / "validation-rules.md").write_text("Rules", encoding="utf-8")

        for skill in ("market-research", "pain-mining", "wtp-research", "workflow-mapping",
                      "skeptic-research", "evidence-audit", "stage1-judge"):
            p = self.root / ".agent" / "skills" / skill
            p.mkdir(parents=True, exist_ok=True)
            (p / "SKILL.md").write_text(f"---\nname: {skill}\n---", encoding="utf-8")

    def build_geo_v2_fixture(self):
        idea_dir = self.root / "ideas" / "geo-monitoring"
        v2_ev = idea_dir / "reassessment-v2" / "evidence"
        v2_out = idea_dir / "reassessment-v2" / "output"
        v2_ev.mkdir(parents=True, exist_ok=True)
        v2_out.mkdir(parents=True, exist_ok=True)

        rows = [make_record(i, idea="geo-monitoring") for i in range(10)]
        for r in rows:
            r["audit_status"] = "VERIFIED"

        ev_text = "\n".join(json.dumps(r) for r in rows) + "\n"
        (v2_ev / "evidence.jsonl").write_text(ev_text, encoding="utf-8")

        scope_map = {
            "scope_id": "GEO-AGENCY-01",
            "records": [
                {
                    "evidence_id": r["id"],
                    "scope_status": "IN_SCOPE",
                    "supporting_evidence_ids": [r["id"]],
                    "reason": "Synthetic fixture.",
                }
                for r in rows
            ],
        }
        (v2_ev / "scope-map.json").write_text(json.dumps(scope_map, indent=2), encoding="utf-8")
        (v2_ev / "audit-summary.md").write_text("Synthetic audit summary.", encoding="utf-8")
        (v2_ev / "review-log.jsonl").write_text("Synthetic review log.\n", encoding="utf-8")

        snap = {
            "snapshot_id": "snap-geo-001",
            "created_at": "2026-09-11T12:00:00Z",
            "base_commit": "3bf758f",
            "idea_id": "geo-monitoring",
            "policy_version": "v2",
            "files": {
                "evidence.jsonl": compute_file_sha256(v2_ev / "evidence.jsonl"),
                "scope-map.json": compute_file_sha256(v2_ev / "scope-map.json"),
                "review-log.jsonl": compute_file_sha256(v2_ev / "review-log.jsonl"),
                "audit-summary.md": compute_file_sha256(v2_ev / "audit-summary.md"),
            },
            "reviewed_evidence_ids": [r["id"] for r in rows],
            "blocked_evidence_ids": [],
            "repaired_evidence_ids": [],
            "unexamined_budget_remaining": "0 remaining",
        }
        (v2_ev / "snapshot.json").write_text(json.dumps(snap, indent=2), encoding="utf-8")

        card = make_v2_scorecard(rows, idea="geo-monitoring", scope_id="GEO-AGENCY-01", verdict="PASS")
        (v2_out / "scorecard.json").write_text(json.dumps(card, indent=2), encoding="utf-8")
        (v2_out / "stage1-report.md").write_text("Synthetic stage 1 report.", encoding="utf-8")

    def test_geo_checker_v2_audit_and_judge(self):
        import check_geo_stage1 as geo_check

        self.build_geo_v2_fixture()
        checker = geo_check.Checker(self.root)
        audited, scope = checker.audit(policy="v2")
        self.assertEqual(len(audited), 10)
        checker.judge(policy="v2")

    def test_deck_checker_v2_audit_and_judge(self):
        import check_deck_stage1 as deck_check

        idea_dir = self.root / "ideas" / "deck-automation"
        v2_ev = idea_dir / "reassessment-v2" / "evidence"
        v2_out = idea_dir / "reassessment-v2" / "output"
        v2_ev.mkdir(parents=True, exist_ok=True)
        v2_out.mkdir(parents=True, exist_ok=True)

        rows = [make_record(i, idea="deck-automation") for i in range(10)]
        for r in rows:
            r["audit_status"] = "VERIFIED"

        (v2_ev / "evidence.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
        scope_map = {
            "scope_id": "boutique_consultancies",
            "records": [
                {"evidence_id": r["id"], "scope_status": "IN_SCOPE", "supporting_evidence_ids": [r["id"]], "reason": "Test"}
                for r in rows
            ],
        }
        (v2_ev / "scope-map.json").write_text(json.dumps(scope_map, indent=2), encoding="utf-8")
        (v2_ev / "audit-summary.md").write_text("Synthetic audit summary.", encoding="utf-8")
        (v2_ev / "review-log.jsonl").write_text("Synthetic review log.\n", encoding="utf-8")

        snap = {
            "snapshot_id": "snap-deck-001",
            "created_at": "2026-09-11T12:00:00Z",
            "base_commit": "3bf758f",
            "idea_id": "deck-automation",
            "policy_version": "v2",
            "files": {
                "evidence.jsonl": compute_file_sha256(v2_ev / "evidence.jsonl"),
                "scope-map.json": compute_file_sha256(v2_ev / "scope-map.json"),
                "review-log.jsonl": compute_file_sha256(v2_ev / "review-log.jsonl"),
                "audit-summary.md": compute_file_sha256(v2_ev / "audit-summary.md"),
            },
            "reviewed_evidence_ids": [r["id"] for r in rows],
            "blocked_evidence_ids": [],
            "repaired_evidence_ids": [],
            "unexamined_budget_remaining": "0 remaining",
        }
        (v2_ev / "snapshot.json").write_text(json.dumps(snap, indent=2), encoding="utf-8")

        card = make_v2_scorecard(rows, idea="deck-automation", scope_id="boutique_consultancies", verdict="PASS")
        (v2_out / "scorecard.json").write_text(json.dumps(card, indent=2), encoding="utf-8")
        (v2_out / "stage1-report.md").write_text("Synthetic stage 1 report.", encoding="utf-8")

        checker = deck_check.Checker(self.root)
        checker.audit(policy="v2")
        checker.judge(policy="v2")


if __name__ == "__main__":
    unittest.main()
