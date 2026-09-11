#!/usr/bin/env python3
"""Stage 1 Policy engine and validation logic for v1 and v2 policies.

Python 3.10+, stdlib only.
Enforces structural, arithmetic, eligibility, and verdict constraints defined in
methodology/stage1-policy.json.
This module checks structure, eligibility relationships, and arithmetic, but does
NOT substitute human semantic audit or Judge review.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
POLICY_FILE = ROOT / "methodology" / "stage1-policy.json"

MONEY_CATEGORIES = {
    "actual_purchase": "paid_tool_or_pilot",
    "paid_pilot": "paid_tool_or_pilot",
    "saas_spend": "paid_tool_or_pilot",
    "employee_time": "employee_time",
    "contractor_spend": "contractor_spend",
    "agency_spend": "agency_spend",
    "dedicated_role": "dedicated_role",
}

VALID_POLICIES = ("v1", "v2")
RESOLUTION_METHODS = ("INTERVIEW", "TECHNICAL_CHECK", "SOURCE_RESEARCH")
RECOMMENDED_ACTIONS = (
    "LIMITED_CUSTOMER_DISCOVERY",
    "STOP",
    "TECHNICAL_CHECK_REQUIRED",
    "REPAIR_RESEARCH",
)


class PolicyError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PolicyError(message)


def load_policy_definitions() -> dict[str, Any]:
    if not POLICY_FILE.is_file():
        raise PolicyError(f"missing policy definition file: {POLICY_FILE}")
    data = json.loads(POLICY_FILE.read_text(encoding="utf-8"))
    return data.get("policy_versions", {})


def compute_sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def resolve_layout(idea_path: Path, policy: str) -> dict[str, Path]:
    """Deterministically resolve directory layout from policy version.

    --policy uniquely determines layout:
      v1 -> legacy layout (ideas/<idea>/evidence, ideas/<idea>/output)
      v2 -> reassessment-v2 layout (ideas/<idea>/reassessment-v2/evidence, output)
    """
    require(policy in VALID_POLICIES, f"unknown policy version: {policy!r}")
    if policy == "v1":
        return {
            "policy": "v1",
            "layout_name": "legacy",
            "evidence_dir": idea_path / "evidence",
            "output_dir": idea_path / "output",
        }
    else:
        v2_root = idea_path / "reassessment-v2"
        return {
            "policy": "v2",
            "layout_name": "reassessment-v2",
            "reassessment_root": v2_root,
            "evidence_dir": v2_root / "evidence",
            "output_dir": v2_root / "output",
        }


def detect_policy_from_scorecard(card: dict[str, Any], requested_policy: str | None, layout_name: str) -> str:
    """Detect and validate policy version with strict fail-closed checks.

    1. Missing policy_version means v1 ONLY in legacy layout.
    2. reassessment-v2 requires explicit v2.
    3. Mismatch between policy, layout, and scorecard fails closed.
    """
    card_policy = card.get("policy_version")

    if card_policy is not None:
        require(card_policy in VALID_POLICIES, f"unknown scorecard policy_version: {card_policy!r}")

    if layout_name == "legacy":
        # Legacy layout can only evaluate v1
        if card_policy is None:
            detected = "v1"
        else:
            require(card_policy == "v1", f"legacy layout cannot contain v2 scorecard (found {card_policy})")
            detected = card_policy
        if requested_policy is not None:
            require(requested_policy == "v1", f"cannot run --policy {requested_policy} on legacy layout")
    elif layout_name == "reassessment-v2":
        # reassessment-v2 layout requires explicit v2
        require(card_policy is not None, "reassessment-v2 layout scorecard requires explicit policy_version: 'v2'")
        require(card_policy == "v2", f"reassessment-v2 layout requires policy_version 'v2', found: {card_policy!r}")
        if requested_policy is not None:
            require(requested_policy == "v2", f"cannot run --policy {requested_policy} on reassessment-v2 layout")
        detected = "v2"
    else:
        raise PolicyError(f"unrecognized layout name: {layout_name}")

    if requested_policy is not None:
        require(detected == requested_policy, f"policy mismatch: requested {requested_policy}, scorecard has {detected}")

    return detected


def validate_v2_conditions(card: dict[str, Any], gates: dict[str, Any], records: dict[str, Any]) -> None:
    """Validate v2 conditions contract for CONDITIONAL PASS."""
    verdict = card["verdict"]
    conditions = card.get("conditions")

    if verdict != "CONDITIONAL PASS":
        require(conditions is None or conditions == [], "conditions must be empty/null unless verdict is CONDITIONAL PASS")
        return

    require(isinstance(conditions, list) and len(conditions) > 0, "CONDITIONAL PASS requires a nonempty conditions list")

    unknown_gates = {name for name, g in gates.items() if g["status"] == "UNKNOWN"}
    covered_gates = set()

    for idx, cond in enumerate(conditions):
        require(isinstance(cond, dict), f"condition[{idx}] must be an object")
        cid = cond.get("condition_id")
        require(isinstance(cid, str) and bool(cid.strip()), f"condition[{idx}]: missing or empty condition_id")

        method = cond.get("resolution_method")
        require(method in RESOLUTION_METHODS, f"{cid}: invalid resolution_method {method!r}")
        # CONDITIONAL PASS allows only questions resolvable via INTERVIEW
        require(
            method == "INTERVIEW",
            f"{cid}: CONDITIONAL PASS allows only resolution_method 'INTERVIEW' (found {method}). "
            f"Technical or source research blockers prevent CONDITIONAL PASS.",
        )

        gate_ids = cond.get("gate_ids")
        require(isinstance(gate_ids, list) and bool(gate_ids), f"{cid}: gate_ids must be a nonempty list")
        for gid in gate_ids:
            require(gid in gates, f"{cid}: references non-existent gate {gid}")
            covered_gates.add(gid)

        for str_field in (
            "exact_unknown",
            "respondent_qualification",
            "observable_information_to_request",
            "continue_criteria",
            "stop_criteria",
        ):
            val = cond.get(str_field)
            require(isinstance(val, str) and bool(val.strip()), f"{cid}: missing or empty {str_field}")

        sup_ids = cond.get("supporting_evidence_ids")
        require(isinstance(sup_ids, list), f"{cid}: supporting_evidence_ids must be a list")
        for sid in sup_ids:
            require(sid in records, f"{cid}: supporting_evidence_id {sid} not in audited evidence")

    # Every UNKNOWN gate must be explicitly covered by conditions
    uncovered = unknown_gates - covered_gates
    require(not uncovered, f"CONDITIONAL PASS has UNKNOWN gates without covering conditions: {uncovered}")


def validate_v2_discovery_plan(card: dict[str, Any]) -> None:
    """Validate v2 discovery_plan and recommended_next_action."""
    verdict = card["verdict"]
    action = card.get("recommended_next_action")
    require(isinstance(action, str) and action in RECOMMENDED_ACTIONS, f"invalid or missing recommended_next_action: {action!r}")

    plan = card.get("discovery_plan")
    if verdict == "CONDITIONAL PASS":
        require(
            action == "LIMITED_CUSTOMER_DISCOVERY",
            f"CONDITIONAL PASS requires recommended_next_action 'LIMITED_CUSTOMER_DISCOVERY', found {action!r}",
        )
        require(isinstance(plan, dict), "CONDITIONAL PASS requires discovery_plan object")
        cap = plan.get("interview_cap")
        require(type(cap) is int and 1 <= cap <= 8, f"discovery_plan.interview_cap must be an integer 1..8, found {cap}")
        for field in ("target_respondent_profile", "review_deadline", "nonresponse_policy"):
            val = plan.get(field)
            require(isinstance(val, str) and bool(val.strip()), f"discovery_plan missing or empty {field}")
    elif verdict == "PASS":
        if plan is not None:
            require(isinstance(plan, dict), "discovery_plan must be object if present")
    else:
        # FAIL or INSUFFICIENT EVIDENCE
        require(
            action != "LIMITED_CUSTOMER_DISCOVERY",
            f"verdict {verdict} cannot have recommended_next_action 'LIMITED_CUSTOMER_DISCOVERY'",
        )


def validate_scorecard_against_policy(
    card: dict[str, Any],
    policy: str,
    records: dict[str, Any],
    scope_records: dict[str, Any] | None,
    allow_unrevealed_stated_wtp: bool = False,
) -> None:
    """Validate scorecard structure, arithmetic, and gate constraints against selected policy."""
    policies = load_policy_definitions()
    p_def = policies.get(policy)
    require(p_def is not None, f"no policy definition found for {policy}")

    verdict = card.get("verdict")
    require(verdict in {"PASS", "CONDITIONAL PASS", "FAIL", "INSUFFICIENT EVIDENCE"}, f"invalid verdict: {verdict!r}")

    gates = card.get("gates")
    require(isinstance(gates, dict) and set(gates) == {f"G{i}" for i in range(1, 7)}, "expected gates G1..G6")

    states = [g.get("status") for g in gates.values()]
    require(all(s in {"PASS", "FAIL", "UNKNOWN"} for s in states), f"invalid gate status in: {states}")

    # Check common gate attributes and count arithmetic
    for name, gate in gates.items():
        require(isinstance(gate, dict), f"{name}: gate must be an object")
        ids = gate.get("counted_evidence_ids")
        require(isinstance(ids, list) and all(isinstance(x, str) for x in ids), f"{name}: invalid counted_evidence_ids")
        require(len(ids) == len(set(ids)), f"{name}: duplicate counted evidence IDs")

        # Every counted ID must be in audited records and VERIFIED
        for x in ids:
            require(x in records, f"{name}: counted evidence ID {x} not in audited records")
            require(records[x].get("audit_status") == "VERIFIED", f"{name}: non-VERIFIED record counted: {x}")

        # Counted IDs must be unique by independence key
        keys = {records[x]["independence_key"] for x in ids}
        require(len(keys) == len(ids), f"{name}: duplicate independence key across counted IDs")
        ind_count = gate.get("independent_count")
        require(type(ind_count) is int and ind_count == len(keys), f"{name}: independent_count mismatch")

        # Scope check: G1..G5 must be IN_SCOPE if scope mapping exists
        if scope_records is not None and name != "G6":
            for x in ids:
                require(
                    scope_records.get(x, {}).get("scope_status") == "IN_SCOPE",
                    f"{name}: counted record {x} is not IN_SCOPE",
                )

        # Gate 3: spend discipline
        if name == "G3":
            for x in ids:
                rec = records[x]
                ms = rec.get("money_signal")
                require(ms in MONEY_CATEGORIES, f"G3: non-revealed money signal {ms!r} on {x}")
            counts = dict(Counter(MONEY_CATEGORIES[records[x]["money_signal"]] for x in ids))
            raw_counts = dict(Counter(records[x]["money_signal"] for x in ids))
            actual_breakdown = gate.get("breakdown_by_category")
            require(actual_breakdown in (counts, raw_counts), "G3: category breakdown mismatch")

        # Gate 4: cluster discipline
        if name == "G4":
            clusters = gate.get("clusters")
            require(isinstance(clusters, dict), "G4: clusters dictionary required")
            covered_ids = set()
            for cname, cids in clusters.items():
                require(isinstance(cids, list) and all(isinstance(i, str) for i in cids), f"G4: invalid cluster {cname}")
                covered_ids.update(cids)
            require(covered_ids == set(ids), "G4: clusters must cover exactly all counted IDs")

    # Policy-specific threshold and verdict rules
    if policy == "v1":
        # v1 thresholds
        if gates["G1"]["status"] == "PASS":
            require(gates["G1"]["independent_count"] >= 20, "G1: v1 PASS requires >= 20 independent signals")
        if gates["G2"]["status"] == "PASS":
            require(gates["G2"]["confidence"] in {"HIGH", "MEDIUM"}, "G2: PASS requires HIGH or MEDIUM confidence")
        if gates["G3"]["status"] == "PASS":
            cat_count = len(gates["G3"].get("breakdown_by_category", {}))
            require(
                gates["G3"]["independent_count"] >= 5 and cat_count >= 2,
                "G3: v1 PASS requires >= 5 signals across >= 2 spend categories",
            )
        if gates["G4"]["status"] == "PASS":
            require(gates["G4"]["independent_count"] >= 10, "G4: v1 PASS requires >= 10 signals")
        if gates["G5"]["status"] == "PASS":
            require(gates["G5"]["confidence"] in {"HIGH", "MEDIUM"}, "G5: PASS requires HIGH or MEDIUM confidence")

        # v1 verdicts
        if verdict == "PASS":
            require(all(s == "PASS" for s in states), "v1 PASS requires all gates PASS")
            require(card.get("condition") is None, "v1 PASS condition must be null")
        elif verdict == "CONDITIONAL PASS":
            require(states.count("UNKNOWN") == 1 and states.count("PASS") == 5, "v1 CONDITIONAL PASS requires 5 PASS and 1 UNKNOWN")
            cond = card.get("condition")
            require(isinstance(cond, str) and bool(cond.strip()), "v1 CONDITIONAL PASS requires single condition string")
        elif verdict == "FAIL":
            require(any(g.get("contradictory_evidence_ids") for g in gates.values()), "FAIL needs cited contradiction, not only missing evidence")
            require(card.get("condition") is None, "v1 condition must be null unless CONDITIONAL PASS")
        else:
            require(card.get("condition") is None, "v1 condition must be null unless CONDITIONAL PASS")

    elif policy == "v2":
        # v2 thresholds
        if gates["G1"]["status"] == "PASS":
            require(gates["G1"]["independent_count"] >= 5, "G1: v2 PASS requires >= 5 independent signals")
        if gates["G2"]["status"] == "PASS":
            require(gates["G2"]["confidence"] in {"HIGH", "MEDIUM"}, "G2: PASS requires HIGH or MEDIUM confidence")
        if gates["G3"]["status"] == "PASS":
            cat_count = len(gates["G3"].get("breakdown_by_category", {}))
            require(
                gates["G3"]["independent_count"] >= 3 and cat_count >= 1,
                "G3: v2 PASS requires >= 3 independent signals from >= 1 category",
            )
        if gates["G4"]["status"] == "PASS":
            require(gates["G4"]["independent_count"] >= 3, "G4: v2 PASS requires >= 3 independent signals")
            clusters = gates["G4"].get("clusters", {})
            # Must support at least one coherent repeated cluster of size >= 3
            require(
                any(len(cids) >= 3 for cids in clusters.values()),
                "G4: v2 PASS requires at least one coherent repeated gap cluster with >= 3 members",
            )
        if gates["G5"]["status"] == "PASS":
            require(gates["G5"]["confidence"] in {"HIGH", "MEDIUM"}, "G5: PASS requires HIGH or MEDIUM confidence")

        # v2 required fields
        require(isinstance(card.get("input_commit_or_snapshot"), str), "v2 requires input_commit_or_snapshot")
        require(bool(card["input_commit_or_snapshot"].strip()), "v2 input_commit_or_snapshot cannot be empty")

        # v2 verdicts
        if verdict == "PASS":
            require(all(s == "PASS" for s in states), "v2 PASS requires all gates PASS")
            validate_v2_discovery_plan(card)
        elif verdict == "CONDITIONAL PASS":
            require(gates["G1"]["status"] == "PASS", "v2 CONDITIONAL PASS requires G1 PASS")
            require(gates["G5"]["status"] == "PASS", "v2 CONDITIONAL PASS requires G5 PASS")
            require("FAIL" not in states, "v2 CONDITIONAL PASS cannot have any FAIL gate")
            validate_v2_conditions(card, gates, records)
            validate_v2_discovery_plan(card)
        elif verdict == "FAIL":
            # Require cited contradiction
            has_contradiction = any(bool(g.get("contradictory_evidence_ids")) for g in gates.values())
            require(has_contradiction, "v2 FAIL requires cited contradiction in contradictory_evidence_ids")
            validate_v2_discovery_plan(card)
        elif verdict == "INSUFFICIENT EVIDENCE":
            validate_v2_discovery_plan(card)

    # Authorization consistency
    require(
        type(card.get("stage2_authorized")) is bool,
        "stage2_authorized must be boolean",
    )
    require(
        card["stage2_authorized"] == (verdict in {"PASS", "CONDITIONAL PASS"}),
        "stage2_authorized must be True for PASS / CONDITIONAL PASS, False otherwise",
    )


def validate_v2_snapshot(snapshot: dict[str, Any], evidence_dir: Path) -> None:
    """Validate v2 review snapshot metadata and hashes."""
    required = {
        "snapshot_id",
        "created_at",
        "base_commit",
        "idea_id",
        "policy_version",
        "files",
        "reviewed_evidence_ids",
        "blocked_evidence_ids",
        "repaired_evidence_ids",
        "unexamined_budget_remaining",
    }
    require(required <= set(snapshot), f"missing snapshot.json fields: {required - set(snapshot)}")
    require(snapshot["policy_version"] == "v2", "snapshot.json must declare policy_version 'v2'")

    files = snapshot["files"]
    require(isinstance(files, dict), "snapshot.json files must be a dict")
    for name in ("evidence.jsonl", "scope-map.json", "review-log.jsonl", "audit-summary.md"):
        require(name in files, f"snapshot files missing {name}")
        file_path = evidence_dir / name
        require(file_path.is_file(), f"snapshot file does not exist: {name}")
        actual_hash = compute_sha256(file_path)
        require(files[name] == actual_hash, f"snapshot hash mismatch for {name}: expected {files[name]}, got {actual_hash}")

    for list_field in ("reviewed_evidence_ids", "blocked_evidence_ids", "repaired_evidence_ids"):
        val = snapshot[list_field]
        require(isinstance(val, list) and all(isinstance(x, str) for x in val), f"snapshot {list_field} must be list of str")
