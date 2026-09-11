#!/usr/bin/env python3
"""Synthetic offline tests for Stage 1 v2 policy, checkers, and immutability manifest.

All synthetic test records live in TemporaryDirectory, never idea outputs.
Verifies structure, arithmetic, boundary conditions, and immutability.
"""
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import tempfile
import unittest
import sys
from collections import Counter
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
        "author_or_entity": f"speaker-{index}",
        "source_excerpt": f"Synthetic test observation {index}.",
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


def make_review_log_item(record: dict, retrieval_outcome: str = "SUCCESS",
                         eligible_gates: list[str] | None = None,
                         blocker: str | None = None,
                         modifications: list[dict] | None = None) -> dict:
    ev_author = record.get("author_or_entity") or record.get("speaker_or_entity") or record.get("independence_key")
    excerpt = record.get("source_excerpt") or record.get("observation") or f"Synthetic test observation."
    return {
        "evidence_id": record["id"],
        "exact_url": record["source_url"],
        "speaker_or_entity": ev_author,
        "independence_key": record.get("independence_key"),
        "locator": "paragraph 1",
        "retrieved_fragment": f"Prefix context. {excerpt} Suffix context." if retrieval_outcome == "SUCCESS" else "",
        "retrieval_outcome": retrieval_outcome,
        "audit_status": record["audit_status"],
        "audit_reason": record["audit_reason"],
        "scope_status": "IN_SCOPE",
        "scope_support": [record["id"]] if record["audit_status"] == "VERIFIED" else [],
        "eligible_gates": eligible_gates or ["G1", "G2", "G3", "G4", "G5", "G6"],
        "blocker": blocker or ("None" if retrieval_outcome == "SUCCESS" else "Synthetic blocker"),
        "modifications": modifications or [],
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
        stage1_policy.Counter(
            "paid_tool_or_pilot" if r["money_signal"] in stage1_policy.TOOL_SIGNALS else r["money_signal"]
            for r in rows[:3]
        )
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
        "discovery_plan": {
            "interview_cap": 8,
            "target_respondent_profile": "Managing Director",
            "review_deadline": "2026-10-01",
            "nonresponse_policy": "Inconclusive.",
        } if verdict in ("PASS", "CONDITIONAL PASS") else None,
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
        """Historical files at 3bf758f must remain 100% byte-for-byte unchanged in canonical Git blobs."""
        self.assertTrue(MANIFEST_FILE.is_file(), f"missing manifest: {MANIFEST_FILE}")
        manifest = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
        manifest_files = manifest.get("files", {})
        manifest_blob_shas = manifest.get("git_blob_shas", {})
        self.assertGreater(len(manifest_files), 50, "manifest must contain historical files")

        # 1. Get canonical Git tree at HEAD for ideas/
        proc = subprocess.run(
            ["git", "ls-tree", "-r", "HEAD", "ideas"],
            cwd=ROOT, capture_output=True, text=True, check=True
        )
        head_blobs = {}
        for line in proc.stdout.splitlines():
            if not line.strip():
                continue
            meta, rel_path = line.split("\t", 1)
            parts = meta.split()
            if len(parts) >= 3 and parts[1] == "blob":
                head_blobs[rel_path] = parts[2]

        mismatches = []
        # 2. Detect changed and deleted files from manifest
        for rel_path, expected_sha256 in manifest_files.items():
            if rel_path not in head_blobs:
                mismatches.append(f"deleted file in historical layout: {rel_path}")
                continue
            head_blob_sha = head_blobs[rel_path]
            expected_blob_sha = manifest_blob_shas.get(rel_path)
            if expected_blob_sha and head_blob_sha != expected_blob_sha:
                mismatches.append(f"git blob changed for {rel_path}: expected {expected_blob_sha}, got {head_blob_sha}")
                continue
            # Canonical blob bytes SHA-256 check
            blob_bytes = subprocess.run(
                ["git", "cat-file", "blob", head_blob_sha],
                cwd=ROOT, capture_output=True, check=True
            ).stdout
            actual_sha256 = hashlib.sha256(blob_bytes).hexdigest()
            if actual_sha256 != expected_sha256:
                mismatches.append(f"blob SHA-256 mismatch for {rel_path}: expected {expected_sha256}, got {actual_sha256}")

        # 3. Detect newly added files in historical raw/evidence/output layouts
        for rel_path in head_blobs:
            parts = rel_path.split("/")
            if len(parts) >= 3 and parts[0] == "ideas" and parts[2] in {"raw", "evidence", "output"}:
                if rel_path not in manifest_files:
                    mismatches.append(f"newly added file in historical layout: {rel_path}")

        # 4. Detect uncommitted changes in working tree for historical layouts
        proc_status = subprocess.run(
            ["git", "status", "--porcelain", "--", "ideas"],
            cwd=ROOT, capture_output=True, text=True, check=True
        )
        for line in proc_status.stdout.splitlines():
            if not line.strip():
                continue
            status = line[:2]
            path = line[3:].strip()
            parts = path.split("/")
            if len(parts) >= 3 and parts[0] == "ideas" and parts[2] in {"raw", "evidence", "output"}:
                mismatches.append(f"uncommitted change in historical file: {path} ({status})")

        self.assertEqual(mismatches, [], f"Historical immutability violated:\n" + "\n".join(mismatches))


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
        self.rev_log = {r["id"]: make_review_log_item(r) for r in self.rows}

    def test_v2_exact_pass_boundary(self):
        card = make_v2_scorecard(self.rows, verdict="PASS")
        stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_v2_g1_fails_below_5(self):
        card = make_v2_scorecard(self.rows, verdict="PASS")
        card["gates"]["G1"]["counted_evidence_ids"] = [self.rows[i]["id"] for i in range(4)]
        card["gates"]["G1"]["independent_count"] = 4
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_v2_g3_passes_with_1_category_and_3_signals(self):
        # All 3 records have saas_spend (paid_tool_or_pilot)
        card = make_v2_scorecard(self.rows, verdict="PASS")
        self.assertEqual(card["gates"]["G3"]["independent_count"], 3)
        self.assertEqual(len(card["gates"]["G3"]["breakdown_by_category"]), 1)
        stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_v2_g3_fails_below_3(self):
        card = make_v2_scorecard(self.rows, verdict="PASS")
        card["gates"]["G3"]["counted_evidence_ids"] = [self.rows[0]["id"], self.rows[1]["id"]]
        card["gates"]["G3"]["independent_count"] = 2
        card["gates"]["G3"]["breakdown_by_category"] = {"paid_tool_or_pilot": 2}
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_v2_g3_stated_wtp_and_competitor_price_rejected_from_counted(self):
        for ms in ("competitor_price", "stated_wtp"):
            with self.subTest(ms=ms):
                bad_rows = copy.deepcopy(self.rows)
                card = make_v2_scorecard(self.rows, verdict="PASS")
                bad_rows[0]["money_signal"] = ms
                card["gates"]["G3"]["breakdown_by_category"] = {ms: 1, "paid_tool_or_pilot": 2}
                records = {r["id"]: r for r in bad_rows}
                rev_log = {r["id"]: make_review_log_item(r) for r in bad_rows}
                with self.assertRaises(stage1_policy.PolicyError):
                    stage1_policy.validate_scorecard_against_policy(card, "v2", records, self.scope, review_log=rev_log)

    def test_v2_g3_unpriced_costly_labor_qualifies(self):
        labor_rows = copy.deepcopy(self.rows)
        labor_rows[0]["money_signal"] = "employee_time"
        labor_rows[0]["money_amount"] = None  # No invented dollar amount
        labor_rows[0]["money_currency"] = None
        records = {r["id"]: r for r in labor_rows}
        rev_log = {r["id"]: make_review_log_item(r) for r in labor_rows}
        card = make_v2_scorecard(labor_rows, verdict="PASS")
        card["gates"]["G3"]["breakdown_by_category"] = {"paid_tool_or_pilot": 2, "employee_time": 1}
        stage1_policy.validate_scorecard_against_policy(card, "v2", records, self.scope, review_log=rev_log)

    def test_v2_g4_requires_coherent_cluster_of_size_at_least_3(self):
        card = make_v2_scorecard(self.rows, verdict="PASS")
        # Split into 3 unrelated complaints (each size 1)
        card["gates"]["G4"]["clusters"] = {
            "unrelated_1": [self.rows[0]["id"]],
            "unrelated_2": [self.rows[1]["id"]],
            "unrelated_3": [self.rows[2]["id"]],
        }
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_deduplication_by_independence_key(self):
        dup_rows = copy.deepcopy(self.rows)
        dup_rows[1]["independence_key"] = dup_rows[0]["independence_key"]
        records = {r["id"]: r for r in dup_rows}
        rev_log = {r["id"]: make_review_log_item(r) for r in dup_rows}
        card = make_v2_scorecard(dup_rows, verdict="PASS")
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", records, self.scope, review_log=rev_log)


class V2ConditionalPassAndDiscoveryPlanTests(unittest.TestCase):
    def setUp(self):
        self.rows = [make_record(i) for i in range(10)]
        self.records = {r["id"]: r for r in self.rows}
        self.scope = {r["id"]: {"scope_status": "IN_SCOPE"} for r in self.rows}
        self.rev_log = {r["id"]: make_review_log_item(r) for r in self.rows}

    def test_valid_conditional_pass_with_interview_conditions(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G2"]["status"] = "UNKNOWN"
        card["gates"]["G3"]["status"] = "UNKNOWN"

        card["discovery_plan"] = {
            "interview_cap": 8,
            "target_respondent_profile": "Managing Director of 2-20 staff agency",
            "review_deadline": "2026-10-01",
            "nonresponse_policy": "Treat recruitment failure as inconclusive.",
        }
        card["conditions"] = [
            {
                "condition_id": "cond-geo-recurrence",
                "gate_ids": ["G2"],
                "resolution_method": "INTERVIEW",
                "exact_unknown": "Is monthly AI answer tracking recurring?",
                "supporting_evidence_ids": [self.rows[0]["id"]],
                "respondent_qualification": "Agency MD",
                "observable_information_to_request": "Frequency and format of client reports.",
                "continue_criteria": "At least 4 of 8 confirm.",
                "stop_criteria": "Fewer than 2 confirm.",
            },
            {
                "condition_id": "cond-geo-wtp",
                "gate_ids": ["G3"],
                "resolution_method": "INTERVIEW",
                "exact_unknown": "Are agencies willing to pay $100+/mo?",
                "supporting_evidence_ids": [self.rows[1]["id"]],
                "respondent_qualification": "Agency owner",
                "observable_information_to_request": "Tool budgets.",
                "continue_criteria": "Target budget identified in >= 3.",
                "stop_criteria": "Refusal to add monitoring line item.",
            },
        ]
        stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_conditional_pass_rejected_if_g1_not_pass(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G1"]["status"] = "UNKNOWN"
        card["conditions"] = [{
            "condition_id": "cond-1", "gate_ids": ["G1"], "resolution_method": "INTERVIEW",
            "exact_unknown": "x", "supporting_evidence_ids": [], "respondent_qualification": "x",
            "observable_information_to_request": "x", "continue_criteria": "x", "stop_criteria": "x",
        }]
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_conditional_pass_rejected_if_g5_not_pass(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G5"]["status"] = "UNKNOWN"
        card["conditions"] = [{
            "condition_id": "cond-5", "gate_ids": ["G5"], "resolution_method": "INTERVIEW",
            "exact_unknown": "x", "supporting_evidence_ids": [], "respondent_qualification": "x",
            "observable_information_to_request": "x", "continue_criteria": "x", "stop_criteria": "x",
        }]
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_conditional_pass_rejected_if_any_gate_fails(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G6"]["status"] = "FAIL"
        card["gates"]["G6"]["contradictory_evidence_ids"] = [self.rows[0]["id"]]
        card["conditions"] = []
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_conditional_pass_rejected_if_resolution_method_is_technical_check(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G6"]["status"] = "UNKNOWN"
        card["conditions"] = [{
            "condition_id": "cond-tech", "gate_ids": ["G6"], "resolution_method": "TECHNICAL_CHECK",
            "exact_unknown": "API access viability", "supporting_evidence_ids": [],
            "respondent_qualification": "Developer", "observable_information_to_request": "API limits",
            "continue_criteria": "API allowed", "stop_criteria": "API prohibited",
        }]
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_conditional_pass_rejected_if_resolution_method_is_source_research(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G6"]["status"] = "UNKNOWN"
        card["conditions"] = [{
            "condition_id": "cond-res", "gate_ids": ["G6"], "resolution_method": "SOURCE_RESEARCH",
            "exact_unknown": "More sources", "supporting_evidence_ids": [],
            "respondent_qualification": "Researcher", "observable_information_to_request": "Sources",
            "continue_criteria": "Found", "stop_criteria": "Not found",
        }]
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_conditional_pass_rejected_if_interview_cap_exceeds_8(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G2"]["status"] = "UNKNOWN"
        card["discovery_plan"]["interview_cap"] = 12
        card["conditions"] = [{
            "condition_id": "cond-2", "gate_ids": ["G2"], "resolution_method": "INTERVIEW",
            "exact_unknown": "x", "supporting_evidence_ids": [], "respondent_qualification": "x",
            "observable_information_to_request": "x", "continue_criteria": "x", "stop_criteria": "x",
        }]
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_conditional_pass_rejected_if_unknown_gate_uncovered(self):
        card = make_v2_scorecard(self.rows, verdict="CONDITIONAL PASS")
        card["gates"]["G2"]["status"] = "UNKNOWN"
        card["gates"]["G3"]["status"] = "UNKNOWN"
        card["conditions"] = [{
            "condition_id": "cond-2", "gate_ids": ["G2"], "resolution_method": "INTERVIEW",
            "exact_unknown": "x", "supporting_evidence_ids": [], "respondent_qualification": "x",
            "observable_information_to_request": "x", "continue_criteria": "x", "stop_criteria": "x",
        }]
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)


class DynamicPolicyOverrideTests(unittest.TestCase):
    def test_validation_reads_supplied_policy_definitions(self):
        """Proof that policy engine dynamically uses supplied definitions without hardcoded thresholds."""
        rows = [make_record(i) for i in range(10)]
        records = {r["id"]: r for r in rows}
        scope = {r["id"]: {"scope_status": "IN_SCOPE"} for r in rows}
        rev_log = {r["id"]: make_review_log_item(r) for r in rows}

        card_5 = make_v2_scorecard(rows[:5], verdict="PASS")
        stage1_policy.validate_scorecard_against_policy(card_5, "v2", records, scope, review_log=rev_log)

        custom_policies = copy.deepcopy(stage1_policy.load_policy_definitions())
        custom_policies["v2"]["gates"]["G1"]["min_independent_count"] = 7

        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(
                card_5, "v2", records, scope, review_log=rev_log, policy_definitions=custom_policies
            )
        self.assertIn("G1: PASS requires >= 7 signals, found 5", str(ctx.exception))

        card_7 = make_v2_scorecard(rows[:7], verdict="PASS")
        card_7["gates"]["G1"]["counted_evidence_ids"] = [r["id"] for r in rows[:7]]
        card_7["gates"]["G1"]["independent_count"] = 7
        stage1_policy.validate_scorecard_against_policy(
            card_7, "v2", records, scope, review_log=rev_log, policy_definitions=custom_policies
        )


class MultiBrandV2Tests(unittest.TestCase):
    def setUp(self):
        self.rows = [make_record(i, idea="multi-brand-content") for i in range(10)]
        self.records = {r["id"]: r for r in self.rows}
        self.scope = {r["id"]: {"scope_status": "IN_SCOPE", "provider_form": "SOLO"} for r in self.rows}
        self.rev_log = {r["id"]: make_review_log_item(r) for r in self.rows}

    def test_multibrand_v2_exact_boundary_pass(self):
        card = make_v2_scorecard(self.rows, idea="multi-brand-content", scope_id="MULTIBRAND-OPERATOR-01", verdict="PASS")
        stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_multibrand_v2_conditional_pass(self):
        card = make_v2_scorecard(self.rows, idea="multi-brand-content", scope_id="MULTIBRAND-OPERATOR-01", verdict="CONDITIONAL PASS")
        card["gates"]["G6"]["status"] = "UNKNOWN"
        card["conditions"] = [{
            "condition_id": "cond-mb-substitute", "gate_ids": ["G6"], "resolution_method": "INTERVIEW",
            "exact_unknown": "Can general schedulers replace dedicated workflow?",
            "supporting_evidence_ids": [self.rows[0]["id"]], "respondent_qualification": "Portfolio operator",
            "observable_information_to_request": "Current scheduling setup.",
            "continue_criteria": "Dedicated tool required by >= 3.", "stop_criteria": "General tools sufficient.",
        }]
        stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)

    def test_multibrand_v2_fails_below_boundary(self):
        card = make_v2_scorecard(self.rows, idea="multi-brand-content", scope_id="MULTIBRAND-OPERATOR-01", verdict="PASS")
        card["gates"]["G1"]["counted_evidence_ids"] = [self.rows[i]["id"] for i in range(4)]
        card["gates"]["G1"]["independent_count"] = 4
        with self.assertRaises(stage1_policy.PolicyError):
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, self.scope, review_log=self.rev_log)


class DeckCandidateScopePoolingTests(unittest.TestCase):
    def setUp(self):
        self.rows = [make_record(i, idea="deck-automation") for i in range(10)]
        self.records = {r["id"]: r for r in self.rows}
        self.rev_log = {r["id"]: make_review_log_item(r) for r in self.rows}

    def test_deck_pooling_across_candidate_scopes_fails(self):
        scope_records = {}
        for i in range(3):
            scope_records[self.rows[i]["id"]] = {
                "scope_status": "IN_SCOPE",
                "candidate_scope": "b2b_saas_account_executives",
            }
        for i in range(3, 5):
            scope_records[self.rows[i]["id"]] = {
                "scope_status": "IN_SCOPE",
                "candidate_scope": "boutique_consultancies",
            }
        for i in range(5, 10):
            scope_records[self.rows[i]["id"]] = {
                "scope_status": "IN_SCOPE",
                "candidate_scope": "b2b_saas_account_executives",
            }

        card = make_v2_scorecard(self.rows, idea="deck-automation", scope_id="b2b_saas_account_executives", verdict="PASS")
        card["gates"]["G1"]["counted_evidence_ids"] = [self.rows[i]["id"] for i in range(5)]
        card["gates"]["G1"]["independent_count"] = 5

        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, scope_records, review_log=self.rev_log)
        self.assertIn("cross-segment pooling forbidden", str(ctx.exception))

    def test_deck_unpooled_single_candidate_scope_passes(self):
        scope_records = {
            r["id"]: {
                "scope_status": "IN_SCOPE",
                "candidate_scope": "b2b_saas_account_executives",
            }
            for r in self.rows
        }
        card = make_v2_scorecard(self.rows, idea="deck-automation", scope_id="b2b_saas_account_executives", verdict="PASS")
        stage1_policy.validate_scorecard_against_policy(card, "v2", self.records, scope_records, review_log=self.rev_log)


class ReviewLogAndSnapshotIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="review-log-test-")
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)

    def test_valid_review_log(self):
        rows = [make_record(i) for i in range(3)]
        items = [make_review_log_item(r) for r in rows]
        log_file = self.dir / "review-log.jsonl"
        log_file.write_text("\n".join(json.dumps(it) for it in items) + "\n", encoding="utf-8")

        entries = stage1_policy.validate_review_log(log_file, evidence_records={r["id"]: r for r in rows})
        self.assertEqual(len(entries), 3)

    def test_review_log_missing_field_fails(self):
        rows = [make_record(0)]
        item = make_review_log_item(rows[0])
        del item["eligible_gates"]
        log_file = self.dir / "review-log.jsonl"
        log_file.write_text(json.dumps(item) + "\n", encoding="utf-8")

        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_review_log(log_file)
        self.assertIn("missing fields in review log row", str(ctx.exception))

    def test_review_log_traceable_modifications_verification(self):
        raw_rows = [make_record(0)]
        ev_rows = copy.deepcopy(raw_rows)
        ev_rows[0]["observation"] = "Modified observation text."

        item_no_mod = make_review_log_item(ev_rows[0], modifications=[])
        log_file = self.dir / "review-log.jsonl"
        log_file.write_text(json.dumps(item_no_mod) + "\n", encoding="utf-8")
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_review_log(
                log_file,
                evidence_records={ev_rows[0]["id"]: ev_rows[0]},
                raw_records={raw_rows[0]["id"]: raw_rows[0]},
            )
        self.assertIn("without traceable entry in review-log modifications", str(ctx.exception))

        item_with_mod = make_review_log_item(
            ev_rows[0],
            modifications=[{
                "field": "observation",
                "before": raw_rows[0]["observation"],
                "after": ev_rows[0]["observation"],
            }],
        )
        log_file.write_text(json.dumps(item_with_mod) + "\n", encoding="utf-8")
        stage1_policy.validate_review_log(
            log_file,
            evidence_records={ev_rows[0]["id"]: ev_rows[0]},
            raw_records={raw_rows[0]["id"]: raw_rows[0]},
        )

    def test_snapshot_hash_mismatch_fails(self):
        rows = [make_record(i) for i in range(2)]
        (self.dir / "evidence.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
        (self.dir / "scope-map.json").write_text("{}", encoding="utf-8")
        (self.dir / "review-log.jsonl").write_text("{}", encoding="utf-8")
        (self.dir / "audit-summary.md").write_text("Audit summary", encoding="utf-8")
        (self.dir / "high-impact-review.md").write_text("High impact", encoding="utf-8")

        snap = {
            "snapshot_id": "snap-001",
            "created_at": "2026-09-11T12:00:00Z",
            "source_baseline_commit": "3bf758f",
            "tooling_commit": "fc2c48a",
            "idea_id": "geo-monitoring",
            "policy_version": "v2",
            "files": {
                "evidence.jsonl": compute_file_sha256(self.dir / "evidence.jsonl"),
                "scope-map.json": compute_file_sha256(self.dir / "scope-map.json"),
                "review-log.jsonl": compute_file_sha256(self.dir / "review-log.jsonl"),
                "audit-summary.md": compute_file_sha256(self.dir / "audit-summary.md"),
                "high-impact-review.md": "corrupted_hash_value_12345",
            },
            "reviewed_evidence_ids": [r["id"] for r in rows],
            "blocked_evidence_ids": [],
            "repaired_evidence_ids": [],
            "unexamined_budget_remaining": "None",
        }
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_v2_snapshot(snap, self.dir)
        self.assertIn("snapshot hash mismatch for high-impact-review.md", str(ctx.exception))

    def test_snapshot_unlinked_id_fails(self):
        rows = [make_record(0)]
        (self.dir / "evidence.jsonl").write_text(json.dumps(rows[0]) + "\n", encoding="utf-8")
        (self.dir / "scope-map.json").write_text("{}", encoding="utf-8")
        (self.dir / "review-log.jsonl").write_text("{}", encoding="utf-8")
        (self.dir / "audit-summary.md").write_text("Audit summary", encoding="utf-8")
        (self.dir / "high-impact-review.md").write_text("High impact", encoding="utf-8")

        snap = {
            "snapshot_id": "snap-001",
            "created_at": "2026-09-11T12:00:00Z",
            "source_baseline_commit": "3bf758f",
            "tooling_commit": "fc2c48a",
            "idea_id": "geo-monitoring",
            "policy_version": "v2",
            "files": {
                "evidence.jsonl": compute_file_sha256(self.dir / "evidence.jsonl"),
                "scope-map.json": compute_file_sha256(self.dir / "scope-map.json"),
                "review-log.jsonl": compute_file_sha256(self.dir / "review-log.jsonl"),
                "audit-summary.md": compute_file_sha256(self.dir / "audit-summary.md"),
                "high-impact-review.md": compute_file_sha256(self.dir / "high-impact-review.md"),
            },
            "reviewed_evidence_ids": ["unlinked-id-999"],
            "blocked_evidence_ids": [],
            "repaired_evidence_ids": [],
            "unexamined_budget_remaining": "None",
        }
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_v2_snapshot(snap, self.dir, evidence_records={rows[0]["id"]: rows[0]})
        self.assertIn("reviewed ID unlinked-id-999 missing from evidence.jsonl", str(ctx.exception))


class GateEligibilityTests(unittest.TestCase):
    def setUp(self):
        self.rows = [make_record(i) for i in range(10)]
        self.records = {r["id"]: r for r in self.rows}
        self.scope = {r["id"]: {"scope_status": "IN_SCOPE"} for r in self.rows}

    def test_unsupported_gate_eligibility_rejected(self):
        rev_log = {
            r["id"]: make_review_log_item(r) for r in self.rows
        }
        rev_log[self.rows[0]["id"]]["eligible_gates"] = ["G1"]
        card = make_v2_scorecard(self.rows, verdict="PASS")
        card["gates"]["G2"]["counted_evidence_ids"] = [self.rows[3]["id"]]
        card["gates"]["G3"]["counted_evidence_ids"] = [self.rows[0]["id"], self.rows[1]["id"], self.rows[2]["id"]]

        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(
                card, "v2", self.records, self.scope, review_log=rev_log
            )
        self.assertIn("is not eligible for G3 in review-log", str(ctx.exception))


class CheckerIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="checker-v2-full-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

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

    def create_v2_bundle(self, idea: str, scope_id: str):
        idea_dir = self.root / "ideas" / idea
        legacy_ev = idea_dir / "evidence"
        v2_ev = idea_dir / "reassessment-v2" / "evidence"
        v2_out = idea_dir / "reassessment-v2" / "output"
        legacy_ev.mkdir(parents=True, exist_ok=True)
        v2_ev.mkdir(parents=True, exist_ok=True)
        v2_out.mkdir(parents=True, exist_ok=True)

        rows = [make_record(i, idea=idea) for i in range(10)]
        for r in rows:
            r["audit_status"] = "VERIFIED"

        (legacy_ev / "evidence.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
        (v2_ev / "evidence.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")

        scope_map = {
            "scope_id": scope_id,
            "records": [
                {
                    "evidence_id": r["id"],
                    "scope_status": "IN_SCOPE",
                    "candidate_scope": scope_id,
                    "provider_form": "SOLO",
                    "supporting_evidence_ids": [r["id"]],
                    "reason": "Synthetic fixture.",
                }
                for r in rows
            ],
        }
        (v2_ev / "scope-map.json").write_text(json.dumps(scope_map, indent=2), encoding="utf-8")
        (v2_ev / "audit-summary.md").write_text("Synthetic audit summary.", encoding="utf-8")
        (v2_ev / "high-impact-review.md").write_text("Synthetic high impact review.", encoding="utf-8")

        log_items = [make_review_log_item(r) for r in rows]
        (v2_ev / "review-log.jsonl").write_text("\n".join(json.dumps(it) for it in log_items) + "\n", encoding="utf-8")

        snap = {
            "snapshot_id": f"snap-{idea}-001",
            "created_at": "2026-09-11T12:00:00Z",
            "source_baseline_commit": "3bf758f",
            "tooling_commit": "fc2c48a",
            "idea_id": idea,
            "policy_version": "v2",
            "files": {
                "evidence.jsonl": compute_file_sha256(v2_ev / "evidence.jsonl"),
                "scope-map.json": compute_file_sha256(v2_ev / "scope-map.json"),
                "review-log.jsonl": compute_file_sha256(v2_ev / "review-log.jsonl"),
                "audit-summary.md": compute_file_sha256(v2_ev / "audit-summary.md"),
                "high-impact-review.md": compute_file_sha256(v2_ev / "high-impact-review.md"),
            },
            "reviewed_evidence_ids": [r["id"] for r in rows],
            "blocked_evidence_ids": [],
            "repaired_evidence_ids": [],
            "unexamined_budget_remaining": "0 remaining",
        }
        (v2_ev / "snapshot.json").write_text(json.dumps(snap, indent=2), encoding="utf-8")

        card = make_v2_scorecard(rows, idea=idea, scope_id=scope_id, verdict="PASS")
        card["input_commit_or_snapshot"] = snap["snapshot_id"]
        (v2_out / "scorecard.json").write_text(json.dumps(card, indent=2), encoding="utf-8")
        (v2_out / "stage1-report.md").write_text("Synthetic stage 1 report.", encoding="utf-8")

    def test_geo_checker_v2(self):
        import check_geo_stage1 as geo_check
        self.create_v2_bundle("geo-monitoring", "GEO-AGENCY-01")
        checker = geo_check.Checker(self.root)
        audited, scope = checker.audit(policy="v2")
        self.assertEqual(len(audited), 10)
        checker.judge(policy="v2")

    def test_deck_checker_v2(self):
        import check_deck_stage1 as deck_check
        self.create_v2_bundle("deck-automation", "boutique_consultancies")
        checker = deck_check.Checker(self.root)
        audited, scope = checker.audit(policy="v2")
        self.assertEqual(len(audited), 10)
        checker.judge(policy="v2")

    def test_multibrand_checker_v2(self):
        import check_multibrand_stage1 as mb_check
        self.create_v2_bundle("multi-brand-content", "MULTIBRAND-OPERATOR-01")
        checker = mb_check.Checker(self.root, policy="v2")
        audited, scope = checker.audit()
        self.assertEqual(len(audited), 10)
        checker.judge()


class AdversarialValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="adversarial-test-")
        self.addCleanup(self.temp.cleanup)
        self.temp_dir = Path(self.temp.name)

    def test_adversarial_wrong_url_rejected(self):
        rec = make_record(0)
        item = make_review_log_item(rec)
        item["exact_url"] = "https://spoofed.attacker.com/fake"
        log_file = self.temp_dir / "review-log.jsonl"
        log_file.write_text(json.dumps(item) + "\n", encoding="utf-8")
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_review_log(log_file, evidence_records={rec["id"]: rec})
        self.assertIn("exact_url mismatch", str(ctx.exception))

    def test_adversarial_wrong_speaker_rejected(self):
        rec = make_record(0)
        item = make_review_log_item(rec)
        item["speaker_or_entity"] = "unattributed-attacker"
        log_file = self.temp_dir / "review-log.jsonl"
        log_file.write_text(json.dumps(item) + "\n", encoding="utf-8")
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_review_log(log_file, evidence_records={rec["id"]: rec})
        self.assertIn("speaker_or_entity mismatch", str(ctx.exception))

    def test_adversarial_wrong_audit_status_rejected(self):
        rec = make_record(0, audit_status="REJECTED")
        item = make_review_log_item(rec)
        item["scope_support"] = [rec["id"]]
        item["audit_status"] = "VERIFIED"  # Spoofed promotion to VERIFIED
        log_file = self.temp_dir / "review-log.jsonl"
        log_file.write_text(json.dumps(item) + "\n", encoding="utf-8")
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_review_log(log_file, evidence_records={rec["id"]: rec})
        self.assertIn("audit_status mismatch", str(ctx.exception))

        # Also test VERIFIED with retrieval_outcome != SUCCESS
        rec_ver = make_record(1, audit_status="VERIFIED")
        item_blocked = make_review_log_item(rec_ver, retrieval_outcome="BLOCKED")
        item_blocked["audit_status"] = "VERIFIED"
        log_file.write_text(json.dumps(item_blocked) + "\n", encoding="utf-8")
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_review_log(log_file, evidence_records={rec_ver["id"]: rec_ver})
        self.assertIn("audit_status VERIFIED requires retrieval_outcome SUCCESS", str(ctx.exception))

    def test_adversarial_wrong_independence_key_rejected(self):
        rec = make_record(0)
        item = make_review_log_item(rec)
        item["independence_key"] = "tampered-independence-key"
        log_file = self.temp_dir / "review-log.jsonl"
        log_file.write_text(json.dumps(item) + "\n", encoding="utf-8")
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_review_log(log_file, evidence_records={rec["id"]: rec})
        self.assertIn("independence_key mismatch", str(ctx.exception))

    def test_adversarial_unlogged_canonical_modification_rejected(self):
        base_rec = make_record(0)
        ev_rec = copy.deepcopy(base_rec)
        ev_rec["money_signal"] = "payroll_spend"  # Unlogged alteration
        item = make_review_log_item(ev_rec, modifications=[])
        log_file = self.temp_dir / "review-log.jsonl"
        log_file.write_text(json.dumps(item) + "\n", encoding="utf-8")
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_review_log(
                log_file,
                evidence_records={ev_rec["id"]: ev_rec},
                baseline_records={base_rec["id"]: base_rec},
            )
        self.assertIn("without traceable entry in review-log modifications", str(ctx.exception))

    def test_adversarial_counted_or_contradictory_id_absent_from_review_log_rejected(self):
        rows = [make_record(i) for i in range(5)]
        records = {r["id"]: r for r in rows}
        scope = {r["id"]: {"scope_status": "IN_SCOPE"} for r in rows}
        card = make_v2_scorecard(rows, verdict="PASS")
        rev_log = {r["id"]: make_review_log_item(r) for r in rows}

        # Case A: counted_evidence_ids has an ID absent from review_log
        del rev_log[rows[0]["id"]]
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(card, "v2", records, scope, review_log=rev_log)
        self.assertIn(f"counted evidence ID {rows[0]['id']} absent from review-log", str(ctx.exception))

        # Restore rev_log
        rev_log = {r["id"]: make_review_log_item(r) for r in rows}

        # Case B: contradictory_evidence_ids has an ID absent from review_log
        card_fail = copy.deepcopy(card)
        card_fail["verdict"] = "FAIL"
        card_fail["stage2_authorized"] = False
        card_fail["recommended_next_action"] = "STOP"
        card_fail["gates"]["G6"]["status"] = "FAIL"
        card_fail["gates"]["G6"]["contradictory_evidence_ids"] = ["ghost-ver-999"]
        records_with_ghost = copy.deepcopy(records)
        records_with_ghost["ghost-ver-999"] = make_record(999, audit_status="VERIFIED")
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(card_fail, "v2", records_with_ghost, scope, review_log=rev_log)
        self.assertIn("contradictory ID ghost-ver-999 absent from review-log", str(ctx.exception))

        # Case C: counted ID has retrieval_outcome != SUCCESS
        rev_log_blocked = copy.deepcopy(rev_log)
        rev_log_blocked[rows[0]["id"]]["retrieval_outcome"] = "BLOCKED"
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(card, "v2", records, scope, review_log=rev_log_blocked)
        self.assertIn("retrieval_outcome is not SUCCESS in review-log", str(ctx.exception))

        # Case D: counted ID has audit_status != VERIFIED
        rev_log_unver = copy.deepcopy(rev_log)
        rev_log_unver[rows[0]["id"]]["audit_status"] = "REJECTED"
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(card, "v2", records, scope, review_log=rev_log_unver)
        self.assertIn("audit_status is not VERIFIED in review-log", str(ctx.exception))

    def test_adversarial_evidence_row_absent_from_snapshot_or_review_log_rejected(self):
        rows = [make_record(i) for i in range(3)]
        evidence_records = {r["id"]: r for r in rows}
        snap_dir = self.temp_dir / "snap_test"
        snap_dir.mkdir(parents=True, exist_ok=True)
        (snap_dir / "evidence.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
        (snap_dir / "scope-map.json").write_text("{}", encoding="utf-8")
        (snap_dir / "review-log.jsonl").write_text("{}", encoding="utf-8")
        (snap_dir / "audit-summary.md").write_text("summary", encoding="utf-8")
        (snap_dir / "high-impact-review.md").write_text("impact", encoding="utf-8")

        # Snapshot and review-log only have rows 0 and 1, but evidence.jsonl has all 3
        snap = {
            "snapshot_id": "snap-test-001",
            "created_at": "2026-09-11T12:00:00Z",
            "source_baseline_commit": "3bf758f",
            "tooling_commit": "fc2c48a",
            "idea_id": "geo-monitoring",
            "policy_version": "v2",
            "files": {
                "evidence.jsonl": compute_file_sha256(snap_dir / "evidence.jsonl"),
                "scope-map.json": compute_file_sha256(snap_dir / "scope-map.json"),
                "review-log.jsonl": compute_file_sha256(snap_dir / "review-log.jsonl"),
                "audit-summary.md": compute_file_sha256(snap_dir / "audit-summary.md"),
                "high-impact-review.md": compute_file_sha256(snap_dir / "high-impact-review.md"),
            },
            "reviewed_evidence_ids": [rows[0]["id"], rows[1]["id"]],
            "blocked_evidence_ids": [],
            "repaired_evidence_ids": [],
            "unexamined_budget_remaining": "0 remaining",
        }
        rev_log_entries = {r["id"]: make_review_log_item(r) for r in rows[:2]}

        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_v2_snapshot(
                snap, snap_dir, evidence_records=evidence_records, review_log_entries=rev_log_entries
            )
        self.assertIn("every evidence.jsonl record must belong to reviewed_evidence_ids or blocked_evidence_ids", str(ctx.exception))

        # Snapshot has all 3 in reviewed_evidence_ids, but review-log only has rows 0 and 1
        snap_all = copy.deepcopy(snap)
        snap_all["reviewed_evidence_ids"] = [r["id"] for r in rows]
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_v2_snapshot(
                snap_all, snap_dir, evidence_records=evidence_records, review_log_entries=rev_log_entries
            )
        self.assertIn(f"reviewed ID {rows[2]['id']} not present in review-log.jsonl", str(ctx.exception))

    def test_adversarial_wrong_snapshot_idea_id_rejected(self):
        snap_dir = self.temp_dir / "snap_idea_test"
        snap_dir.mkdir(parents=True, exist_ok=True)
        (snap_dir / "evidence.jsonl").write_text("", encoding="utf-8")
        (snap_dir / "scope-map.json").write_text("{}", encoding="utf-8")
        (snap_dir / "review-log.jsonl").write_text("{}", encoding="utf-8")
        (snap_dir / "audit-summary.md").write_text("summary", encoding="utf-8")
        (snap_dir / "high-impact-review.md").write_text("impact", encoding="utf-8")

        snap = {
            "snapshot_id": "snap-idea-001",
            "created_at": "2026-09-11T12:00:00Z",
            "source_baseline_commit": "3bf758f",
            "tooling_commit": "fc2c48a",
            "idea_id": "deck-automation",
            "policy_version": "v2",
            "files": {
                "evidence.jsonl": compute_file_sha256(snap_dir / "evidence.jsonl"),
                "scope-map.json": compute_file_sha256(snap_dir / "scope-map.json"),
                "review-log.jsonl": compute_file_sha256(snap_dir / "review-log.jsonl"),
                "audit-summary.md": compute_file_sha256(snap_dir / "audit-summary.md"),
                "high-impact-review.md": compute_file_sha256(snap_dir / "high-impact-review.md"),
            },
            "reviewed_evidence_ids": [],
            "blocked_evidence_ids": [],
            "repaired_evidence_ids": [],
            "unexamined_budget_remaining": "0 remaining",
        }
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_v2_snapshot(snap, snap_dir, expected_idea_id="geo-monitoring")
        self.assertIn("snapshot idea_id mismatch", str(ctx.exception))

    def test_adversarial_missing_or_wrong_scorecard_idea_id_rejected(self):
        rows = [make_record(i) for i in range(5)]
        records = {r["id"]: r for r in rows}
        scope = {r["id"]: {"scope_status": "IN_SCOPE"} for r in rows}
        rev_log = {r["id"]: make_review_log_item(r) for r in rows}
        card = make_v2_scorecard(rows, idea="geo-monitoring", scope_id="GEO-AGENCY-01", verdict="PASS")

        # 1. Missing idea_id
        card_no_idea = copy.deepcopy(card)
        del card_no_idea["idea_id"]
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(card_no_idea, "v2", records, scope, review_log=rev_log)
        self.assertIn("scorecard requires non-empty idea_id", str(ctx.exception))

        # 2. Wrong idea_id against expected_idea_id
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(
                card, "v2", records, scope, review_log=rev_log, expected_idea_id="deck-automation"
            )
        self.assertIn("scorecard idea_id mismatch", str(ctx.exception))

        # 3. Missing evaluated_scope
        card_no_scope = copy.deepcopy(card)
        del card_no_scope["evaluated_scope"]
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(card_no_scope, "v2", records, scope, review_log=rev_log)
        self.assertIn("scorecard requires evaluated_scope object", str(ctx.exception))

        # 4. Wrong scope_id against expected_scope_id
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(
                card, "v2", records, scope, review_log=rev_log, expected_scope_id="WRONG-SCOPE"
            )
        self.assertIn("scorecard evaluated_scope mismatch", str(ctx.exception))

        # 5. Wrong scope_id against allowed_scope_ids
        with self.assertRaises(stage1_policy.PolicyError) as ctx:
            stage1_policy.validate_scorecard_against_policy(
                card, "v2", records, scope, review_log=rev_log,
                allowed_scope_ids=["boutique_consultancies", "b2b_saas_account_executives"]
            )
        self.assertIn("not in declared candidate scopes", str(ctx.exception))

    def test_adversarial_deck_v1_audit_judge_and_raw_mismatch_regression(self):
        import check_deck_stage1 as deck_check

        # 1. Real repository: audit_v1 and judge_v1 must execute without crash
        real_checker = deck_check.Checker(ROOT)
        audited, scope = real_checker.audit(policy="v1")
        self.assertEqual(len(audited), 88, "Deck v1 audit must find 88 canonical records")
        real_checker.judge(policy="v1")
        scorecard = json.loads((ROOT / "ideas" / "deck-automation" / "output" / "scorecard.json").read_text(encoding="utf-8"))
        self.assertEqual(scorecard.get("verdict"), "FAIL", "Deck v1 verdict must be FAIL")

        # 2. In synthetic temp directory, verify duplicate raw ID across tracks is rejected
        temp_root = Path(self.temp_dir) / "deck_dup_test"
        (temp_root / "methodology").mkdir(parents=True, exist_ok=True)
        (temp_root / "methodology" / "evidence-schema.json").write_text(json.dumps(SCHEMA), encoding="utf-8")

        raw_deck = temp_root / "ideas" / "deck-automation" / "raw"
        market_dir = raw_deck / "market"
        pain_dir = raw_deck / "pain"
        market_dir.mkdir(parents=True, exist_ok=True)
        pain_dir.mkdir(parents=True, exist_ok=True)

        dup_rec = make_record(0, idea="deck-automation")
        (market_dir / "evidence.jsonl").write_text(json.dumps(dup_rec) + "\n", encoding="utf-8")
        (pain_dir / "evidence.jsonl").write_text(json.dumps(dup_rec) + "\n", encoding="utf-8")

        mock_checker = deck_check.Checker(temp_root)
        with self.assertRaises((deck_check.CheckError, stage1_policy.PolicyError)) as ctx:
            mock_checker.raw_all()
        self.assertIn("duplicate raw ID across tracks", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
