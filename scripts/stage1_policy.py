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
import re
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POLICY_FILE = ROOT / "methodology" / "stage1-policy.json"
BASE_COMMIT = "3bf758f"

# Mapping to group equivalent tool signals for category diversity
TOOL_SIGNALS = {"actual_purchase", "paid_pilot", "saas_spend"}


class PolicyError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PolicyError(message)


def load_policy_definitions(policy_file: Path | None = None) -> dict[str, Any]:
    target = policy_file or DEFAULT_POLICY_FILE
    if not target.is_file():
        raise PolicyError(f"missing policy definition file: {target}")
    data = json.loads(target.read_text(encoding="utf-8"))
    return data.get("policy_versions", {})


def compute_sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def resolve_layout(idea_path: Path, policy: str) -> dict[str, Path]:
    """Deterministically resolve directory layout from policy version."""
    require(policy in ("v1", "v2"), f"unknown policy version: {policy!r}")
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
    """Detect and validate policy version with strict fail-closed checks."""
    card_policy = card.get("policy_version")

    if card_policy is not None:
        require(card_policy in ("v1", "v2"), f"unknown scorecard policy_version: {card_policy!r}")

    if layout_name == "legacy":
        if card_policy is None:
            detected = "v1"
        else:
            require(card_policy == "v1", f"legacy layout cannot contain v2 scorecard (found {card_policy})")
            detected = card_policy
        if requested_policy is not None:
            require(requested_policy == "v1", f"cannot run --policy {requested_policy} on legacy layout")
    elif layout_name == "reassessment-v2":
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


def validate_review_log(
    path: Path,
    policy_def: dict[str, Any] | None = None,
    evidence_records: dict[str, Any] | None = None,
    raw_records: dict[str, Any] | None = None,
) -> dict[str, dict[str, Any]]:
    """Validate review-log.jsonl strictly against its contract."""
    if not path.is_file():
        raise PolicyError(f"missing review-log file: {path}")

    text = path.read_text(encoding="utf-8")
    require(bool(text.strip()), f"empty review-log file: {path}")

    policies = policy_def or load_policy_definitions()
    schema = policies.get("v2", {}).get("review_log_schema", {}) if "v2" in policies else policies.get("review_log_schema", {})
    required_fields = set(schema.get("required_fields", [
        "evidence_id", "exact_url", "speaker_or_entity", "locator", "retrieved_fragment",
        "retrieval_outcome", "audit_status", "audit_reason", "scope_status",
        "scope_support", "eligible_gates", "blocker"
    ]))
    allowed_outcomes = set(schema.get("allowed_retrieval_outcomes", ["SUCCESS", "BLOCKED", "NOT_FOUND", "ERROR"]))
    allowed_statuses = set(schema.get("allowed_audit_statuses", ["VERIFIED", "PARTIALLY_VERIFIED", "REJECTED", "PENDING"]))
    allowed_scope = set(schema.get("allowed_scope_statuses", ["IN_SCOPE", "OUT_OF_SCOPE", "UNKNOWN"]))
    allowed_gates = set(schema.get("allowed_gates", ["G1", "G2", "G3", "G4", "G5", "G6"]))

    entries = {}
    for line_no, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        label = f"{path.name}:{line_no}"
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise PolicyError(f"{label}: invalid JSON in review log: {exc}") from exc

        require(isinstance(item, dict), f"{label}: row must be a JSON object")
        missing = required_fields - set(item)
        require(not missing, f"{label}: missing fields in review log row: {missing}")

        eid = item["evidence_id"]
        require(isinstance(eid, str) and bool(eid.strip()), f"{label}: invalid evidence_id")
        require(eid not in entries, f"{label}: duplicate evidence_id in review log: {eid}")

        url = item["exact_url"]
        require(isinstance(url, str), f"{label}: exact_url must be string")
        parts = urlsplit(url)
        require(parts.scheme in {"http", "https"} and bool(parts.hostname), f"{label}: invalid exact_url {url!r}")

        outcome = item["retrieval_outcome"]
        require(outcome in allowed_outcomes, f"{label}: invalid retrieval_outcome: {outcome!r}")
        if outcome in {"BLOCKED", "NOT_FOUND", "ERROR"}:
            require(isinstance(item["blocker"], str) and bool(item["blocker"].strip()),
                    f"{label}: non-empty blocker reason required when retrieval_outcome is {outcome}")

        astatus = item["audit_status"]
        require(astatus in allowed_statuses, f"{label}: invalid audit_status {astatus!r}")
        require(isinstance(item["audit_reason"], str) and bool(item["audit_reason"].strip()),
                f"{label}: non-empty audit_reason required")

        sstatus = item["scope_status"]
        require(sstatus in allowed_scope, f"{label}: invalid scope_status {sstatus!r}")

        ssupport = item["scope_support"]
        require(isinstance(ssupport, list) and all(isinstance(x, str) for x in ssupport),
                f"{label}: scope_support must be list of strings")
        if sstatus == "IN_SCOPE":
            require(bool(ssupport), f"{label}: IN_SCOPE requires non-empty scope_support")

        egates = item["eligible_gates"]
        require(isinstance(egates, list) and all(g in allowed_gates for g in egates),
                f"{label}: eligible_gates must be list of valid gate names (subset of {allowed_gates})")

        # Validate modifications structure if present
        if "modifications" in item:
            mods = item["modifications"]
            require(isinstance(mods, (list, dict)), f"{label}: modifications must be list or dict")
            if isinstance(mods, list):
                for midx, mod in enumerate(mods):
                    require(isinstance(mod, dict), f"{label}: modification #{midx} must be object")
                    require("field" in mod and isinstance(mod["field"], str) and bool(mod["field"].strip()),
                            f"{label}: modification #{midx} missing non-empty field")
                    require("before" in mod and "after" in mod,
                            f"{label}: modification on field {mod.get('field')} requires both 'before' and 'after'")
            elif isinstance(mods, dict):
                for fld, mod in mods.items():
                    require(isinstance(mod, dict), f"{label}: modification for field {fld} must be object")
                    require("before" in mod and "after" in mod,
                            f"{label}: modification on field {fld} requires both 'before' and 'after'")

        # Evidence ID binding
        if evidence_records is not None:
            require(eid in evidence_records, f"{label}: reviewed evidence ID {eid} does not exist in evidence.jsonl")

        # Traceable field modifications check against raw baseline
        if raw_records is not None and evidence_records is not None and eid in raw_records and eid in evidence_records:
            raw_rec = raw_records[eid]
            ev_rec = evidence_records[eid]
            mods = item.get("modifications", [])
            mod_map = {}
            if isinstance(mods, list):
                for m in mods:
                    if isinstance(m, dict) and "field" in m:
                        mod_map[m["field"]] = m
            elif isinstance(mods, dict):
                mod_map = mods

            for fld in set(raw_rec) | set(ev_rec):
                if fld in {"audit_status", "audit_reason"}:
                    continue
                v_raw = raw_rec.get(fld)
                v_ev = ev_rec.get(fld)
                if v_raw != v_ev:
                    require(fld in mod_map,
                            f"{label}: field {fld!r} modified between raw and evidence but has no traceable entry in review log modifications")
                    entry_mod = mod_map[fld]
                    require(entry_mod.get("before") == v_raw,
                            f"{label}: field {fld!r} before value mismatch: expected {v_raw!r}, got {entry_mod.get('before')!r}")
                    require(entry_mod.get("after") == v_ev,
                            f"{label}: field {fld!r} after value mismatch: expected {v_ev!r}, got {entry_mod.get('after')!r}")

        entries[eid] = item

    return entries


def validate_v2_snapshot(
    snapshot: dict[str, Any],
    evidence_dir: Path,
    review_log_entries: dict[str, Any] | None = None,
    evidence_records: dict[str, Any] | None = None,
) -> None:
    """Validate v2 review snapshot metadata, hashes, and ID bindings."""
    required = {
        "snapshot_id", "created_at", "source_baseline_commit", "tooling_commit",
        "idea_id", "policy_version", "files", "reviewed_evidence_ids",
        "blocked_evidence_ids", "repaired_evidence_ids", "unexamined_budget_remaining",
    }
    missing = required - set(snapshot)
    require(not missing, f"missing snapshot.json fields: {missing}")

    require(snapshot["policy_version"] == "v2", "snapshot.json must declare policy_version 'v2'")
    require(snapshot["source_baseline_commit"] == BASE_COMMIT,
            f"snapshot source_baseline_commit must be {BASE_COMMIT!r}, found: {snapshot.get('source_baseline_commit')!r}")
    require(isinstance(snapshot["tooling_commit"], str) and bool(snapshot["tooling_commit"].strip()),
            "snapshot tooling_commit must be a non-empty string")

    # Date check
    ts_str = snapshot["created_at"]
    try:
        datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
    except ValueError as exc:
        raise PolicyError(f"snapshot created_at is not valid ISO timestamp: {ts_str}") from exc

    files = snapshot["files"]
    require(isinstance(files, dict), "snapshot.json files must be a dict")
    for name in ("evidence.jsonl", "scope-map.json", "review-log.jsonl", "audit-summary.md", "high-impact-review.md"):
        require(name in files, f"snapshot files missing {name}")
        file_path = evidence_dir / name
        require(file_path.is_file(), f"snapshot file does not exist: {name}")
        actual_hash = compute_sha256(file_path)
        require(files[name] == actual_hash, f"snapshot hash mismatch for {name}: expected {files[name]}, got {actual_hash}")

    # Uniqueness and disjointness of ID lists
    for list_field in ("reviewed_evidence_ids", "blocked_evidence_ids", "repaired_evidence_ids"):
        val = snapshot[list_field]
        require(isinstance(val, list) and all(isinstance(x, str) for x in val), f"snapshot {list_field} must be list of str")
        require(len(val) == len(set(val)), f"duplicate IDs inside snapshot {list_field}")

    reviewed_ids = set(snapshot["reviewed_evidence_ids"])
    blocked_ids = set(snapshot["blocked_evidence_ids"])
    repaired_ids = set(snapshot["repaired_evidence_ids"])

    overlap = reviewed_ids & blocked_ids
    require(not overlap, f"reviewed_evidence_ids and blocked_evidence_ids must be disjoint, found overlap: {overlap}")
    require(repaired_ids <= reviewed_ids, f"repaired_evidence_ids must be subset of reviewed_evidence_ids")

    # Bindings with review_log_entries if provided
    if review_log_entries is not None:
        for eid in reviewed_ids:
            require(eid in review_log_entries, f"reviewed ID {eid} not present in review-log.jsonl")
            require(review_log_entries[eid]["retrieval_outcome"] == "SUCCESS",
                    f"reviewed ID {eid} has outcome {review_log_entries[eid]['retrieval_outcome']}, expected SUCCESS")

        for eid in blocked_ids:
            require(eid in review_log_entries, f"blocked ID {eid} not present in review-log.jsonl")
            require(review_log_entries[eid]["retrieval_outcome"] in {"BLOCKED", "NOT_FOUND", "ERROR"},
                    f"blocked ID {eid} has outcome {review_log_entries[eid]['retrieval_outcome']}, expected BLOCKED/NOT_FOUND/ERROR")

        for eid in review_log_entries:
            require(eid in reviewed_ids or eid in blocked_ids,
                    f"review log ID {eid} is neither in reviewed_evidence_ids nor blocked_evidence_ids")

        for eid in repaired_ids:
            rentry = review_log_entries[eid]
            has_mod = bool(rentry.get("modifications")) or rentry.get("repaired") is True or bool(rentry.get("repaired_fields"))
            require(has_mod, f"repaired ID {eid} has no traceable modifications in review-log.jsonl")

    # Bindings with evidence_records if provided
    if evidence_records is not None:
        for eid in reviewed_ids:
            require(eid in evidence_records, f"reviewed ID {eid} missing from evidence.jsonl")
        for eid in blocked_ids:
            if eid in evidence_records:
                require(evidence_records[eid].get("audit_status") != "VERIFIED",
                        f"blocked ID {eid} cannot be marked VERIFIED in evidence.jsonl")


def validate_v2_discovery_plan(card: dict[str, Any], p_def: dict[str, Any]) -> None:
    """Validate v2 discovery_plan and recommended_next_action against policy."""
    verdict = card["verdict"]
    action = card.get("recommended_next_action")
    allowed_actions = ("LIMITED_CUSTOMER_DISCOVERY", "STOP", "TECHNICAL_CHECK_REQUIRED", "REPAIR_RESEARCH")
    require(isinstance(action, str) and action in allowed_actions, f"invalid or missing recommended_next_action: {action!r}")

    plan = card.get("discovery_plan")
    max_cap = p_def.get("discovery_plan", {}).get("max_interviews", 8)
    expected_action = p_def.get("discovery_plan", {}).get("recommended_next_action", "LIMITED_CUSTOMER_DISCOVERY")

    if verdict in ("PASS", "CONDITIONAL PASS"):
        require(
            action == expected_action,
            f"{verdict} requires recommended_next_action {expected_action!r}, found {action!r}",
        )
        require(isinstance(plan, dict), f"{verdict} requires discovery_plan object")
        cap = plan.get("interview_cap")
        require(type(cap) is int and 1 <= cap <= max_cap,
                f"discovery_plan.interview_cap must be an integer 1..{max_cap}, found {cap}")
        for field in ("target_respondent_profile", "review_deadline", "nonresponse_policy"):
            val = plan.get(field)
            require(isinstance(val, str) and bool(val.strip()), f"discovery_plan missing or empty {field}")
    else:
        require(
            action != expected_action,
            f"verdict {verdict} cannot have recommended_next_action {expected_action!r}",
        )


def validate_v2_conditions(
    card: dict[str, Any],
    gates: dict[str, Any],
    records: dict[str, Any],
    p_def: dict[str, Any],
    review_log: dict[str, Any] | None = None,
) -> None:
    """Validate v2 conditions contract for CONDITIONAL PASS."""
    verdict = card["verdict"]
    conditions = card.get("conditions")

    if verdict != "CONDITIONAL PASS":
        require(conditions is None or conditions == [], "conditions must be empty/null unless verdict is CONDITIONAL PASS")
        return

    require(isinstance(conditions, list) and len(conditions) > 0, "CONDITIONAL PASS requires a nonempty conditions list")

    unknown_gates = {name for name, g in gates.items() if g["status"] == "UNKNOWN"}
    require(bool(unknown_gates), "CONDITIONAL PASS requires at least one UNKNOWN gate")
    covered_gates = set()
    condition_ids = []

    c_schema = p_def.get("condition_schema", {})
    req_fields = set(c_schema.get("required_fields", [
        "condition_id", "gate_ids", "resolution_method", "exact_unknown",
        "supporting_evidence_ids", "respondent_qualification",
        "observable_information_to_request", "continue_criteria", "stop_criteria"
    ]))
    allowed_methods = set(c_schema.get("allowed_resolution_methods", ["INTERVIEW", "TECHNICAL_CHECK", "SOURCE_RESEARCH"]))
    v_rules = p_def.get("verdict_rules", {}).get("CONDITIONAL_PASS", {})
    allowed_conditional_methods = set(v_rules.get("allowed_resolution_methods", ["INTERVIEW"]))

    for idx, cond in enumerate(conditions):
        require(isinstance(cond, dict), f"condition[{idx}] must be an object")
        missing = req_fields - set(cond)
        require(not missing, f"condition[{idx}] missing fields: {missing}")

        cid = cond["condition_id"]
        require(isinstance(cid, str) and bool(cid.strip()), f"condition[{idx}]: invalid condition_id")
        condition_ids.append(cid)

        method = cond["resolution_method"]
        require(method in allowed_methods, f"{cid}: invalid resolution_method {method!r}")
        require(method in allowed_conditional_methods,
                f"{cid}: CONDITIONAL PASS allows only {allowed_conditional_methods} (found {method}). "
                f"Technical or source research blockers prevent CONDITIONAL PASS.")

        gate_ids = cond["gate_ids"]
        require(isinstance(gate_ids, list) and bool(gate_ids), f"{cid}: gate_ids must be a nonempty list")
        for gid in gate_ids:
            require(gid in gates, f"{cid}: references non-existent gate {gid}")
            # Every condition may reference only UNKNOWN gates
            require(gates[gid]["status"] == "UNKNOWN",
                    f"{cid}: condition references gate {gid} which has status {gates[gid]['status']}, "
                    f"conditions may reference ONLY UNKNOWN gates")
            covered_gates.add(gid)

        for str_field in ("exact_unknown", "respondent_qualification", "observable_information_to_request",
                          "continue_criteria", "stop_criteria"):
            val = cond[str_field]
            require(isinstance(val, str) and bool(val.strip()), f"{cid}: missing or empty {str_field}")

        sup_ids = cond["supporting_evidence_ids"]
        require(isinstance(sup_ids, list), f"{cid}: supporting_evidence_ids must be a list")
        for sid in sup_ids:
            require(sid in records, f"{cid}: supporting_evidence_id {sid} not in audited evidence")
            require(records[sid]["audit_status"] == "VERIFIED", f"{cid}: supporting_evidence_id {sid} is not VERIFIED")
            # If review log is available, check gate eligibility
            if review_log and sid in review_log:
                eligible = review_log[sid].get("eligible_gates", [])
                require(any(gid in eligible for gid in gate_ids),
                        f"{cid}: supporting ID {sid} is not eligible for referenced gates {gate_ids}")

    # Condition IDs must be unique
    require(len(condition_ids) == len(set(condition_ids)), f"condition IDs must be unique: {condition_ids}")

    # Every UNKNOWN gate must be explicitly covered by conditions
    uncovered = unknown_gates - covered_gates
    require(not uncovered, f"CONDITIONAL PASS has UNKNOWN gates without covering conditions: {uncovered}")


def validate_scorecard_against_policy(
    card: dict[str, Any],
    policy: str,
    records: dict[str, Any],
    scope_records: dict[str, Any] | None = None,
    review_log: dict[str, Any] | None = None,
    policy_definitions: dict[str, Any] | None = None,
    expected_snapshot_id: str | None = None,
) -> None:
    """Validate scorecard strictly against supplied policy definitions without hardcoded constants."""
    policies = policy_definitions or load_policy_definitions()
    p_def = policies.get(policy)
    require(p_def is not None, f"no policy definition found for {policy}")

    verdict = card.get("verdict")
    require(verdict in {"PASS", "CONDITIONAL PASS", "FAIL", "INSUFFICIENT EVIDENCE"}, f"invalid verdict: {verdict!r}")

    gates = card.get("gates")
    require(isinstance(gates, dict) and set(gates) == {f"G{i}" for i in range(1, 7)}, "expected gates G1..G6")

    states = [g.get("status") for g in gates.values()]
    require(all(s in {"PASS", "FAIL", "UNKNOWN"} for s in states), f"invalid gate status in: {states}")

    # Bind input_commit_or_snapshot for v2
    if policy == "v2":
        snap_ref = card.get("input_commit_or_snapshot")
        require(isinstance(snap_ref, str) and bool(snap_ref.strip()), "v2 scorecard requires input_commit_or_snapshot")
        if expected_snapshot_id is not None:
            require(snap_ref == expected_snapshot_id,
                    f"input_commit_or_snapshot mismatch: expected {expected_snapshot_id!r}, found {snap_ref!r}")

    # Validate individual gates
    for name, gate in gates.items():
        g_def = p_def.get("gates", {}).get(name, {})
        require(isinstance(gate, dict), f"{name}: gate must be an object")

        # FAIL gate check: every FAIL gate requires eligible contradictory evidence
        if gate["status"] == "FAIL":
            contra = gate.get("contradictory_evidence_ids", [])
            require(isinstance(contra, list) and bool(contra), f"{name}: FAIL gate requires cited contradictory_evidence_ids")
            for cid in contra:
                require(cid in records and records[cid].get("audit_status") == "VERIFIED",
                        f"{name}: contradictory ID {cid} not in records or not VERIFIED")
                if scope_records and name != "G6":
                    require(scope_records.get(cid, {}).get("scope_status") == "IN_SCOPE",
                            f"{name}: contradictory evidence {cid} is not IN_SCOPE")
                if review_log and cid in review_log:
                    require(name in review_log[cid].get("eligible_gates", []),
                            f"{name}: contradictory ID {cid} is not eligible for {name}")

        ids = gate.get("counted_evidence_ids")
        require(isinstance(ids, list) and all(isinstance(x, str) for x in ids), f"{name}: invalid counted_evidence_ids")
        require(len(ids) == len(set(ids)), f"{name}: duplicate counted evidence IDs")

        for x in ids:
            require(x in records, f"{name}: counted evidence ID {x} not in audited records")
            require(records[x].get("audit_status") == "VERIFIED", f"{name}: non-VERIFIED record counted: {x}")
            if review_log and x in review_log:
                require(name in review_log[x].get("eligible_gates", []),
                        f"{name}: counted record {x} is not eligible for {name} in review-log")

        keys = {records[x]["independence_key"] for x in ids}
        require(len(keys) == len(ids), f"{name}: duplicate independence key across counted IDs")
        ind_count = gate.get("independent_count")
        require(type(ind_count) is int and ind_count == len(keys), f"{name}: independent_count mismatch")

        # Scope integrity: G1..G5 must be IN_SCOPE and match evaluated candidate scope
        if scope_records is not None and name != "G6":
            eval_scope = card.get("evaluated_scope", {}).get("scope_id")
            for x in ids:
                rec_scope = scope_records.get(x, {})
                require(rec_scope.get("scope_status") == "IN_SCOPE",
                        f"{name}: counted record {x} is not IN_SCOPE")
                cand = rec_scope.get("candidate_scope") or rec_scope.get("candidate_icp")
                if cand and eval_scope:
                    norm_cand = re.sub(r"[-\s]+", "_", str(cand).strip().lower())
                    norm_eval = re.sub(r"[-\s]+", "_", str(eval_scope).strip().lower())
                    require(norm_cand == norm_eval,
                            f"{name}: record {x} candidate scope {cand!r} does not match evaluated scope {eval_scope!r} (cross-segment pooling forbidden)")

        # G2 / G5 requirements
        if gate["status"] == "PASS" and g_def.get("requires_counted_evidence"):
            require(bool(ids), f"{name}: PASS requires counted evidence")
            allowed_conf = g_def.get("allowed_confidences", ["HIGH", "MEDIUM"])
            require(gate.get("confidence") in allowed_conf,
                    f"{name}: PASS requires confidence in {allowed_conf}, found {gate.get('confidence')!r}")

        # G6 requirement
        if gate["status"] == "PASS" and g_def.get("requires_verified_context"):
            require(bool(ids), "G6: PASS requires VERIFIED eligible substitute assessment context")

        # Gate 3: spend discipline
        if name == "G3":
            allowed_signals = set(g_def.get("allowed_money_signals", [
                "actual_purchase", "paid_pilot", "saas_spend", "employee_time",
                "contractor_spend", "agency_spend", "dedicated_role"
            ]))
            disallowed_signals = set(g_def.get("disallowed_money_signals", [
                "stated_wtp", "competitor_price", "unknown"
            ]))
            for x in ids:
                rec = records[x]
                ms = rec.get("money_signal")
                require(ms in allowed_signals, f"G3: money_signal {ms!r} on {x} is not in allowed signals: {allowed_signals}")
                require(ms not in disallowed_signals, f"G3: disallowed money_signal {ms!r} counted on {x}")

            raw_counts = dict(Counter(records[x]["money_signal"] for x in ids))
            # Normalized counts grouping tool signals under paid_tool_or_pilot
            norm_counts = dict(Counter(
                "paid_tool_or_pilot" if records[x]["money_signal"] in TOOL_SIGNALS else records[x]["money_signal"]
                for x in ids
            ))
            actual_breakdown = gate.get("breakdown_by_category")
            require(actual_breakdown in (raw_counts, norm_counts), f"G3: breakdown_by_category mismatch")

            if gate["status"] == "PASS":
                min_count = g_def["min_independent_count"]
                min_cats = g_def.get("min_categories", 1)
                require(ind_count >= min_count, f"G3: PASS requires >= {min_count} signals, found {ind_count}")
                # Distinct categories counted via normalized categories
                require(len(norm_counts) >= min_cats, f"G3: PASS requires >= {min_cats} distinct categories, found {len(norm_counts)}")

        # Gate 4: cluster discipline
        if name == "G4":
            clusters = gate.get("clusters")
            require(isinstance(clusters, dict), "G4: clusters dictionary required")
            covered_ids = set()
            for cname, cids in clusters.items():
                require(isinstance(cids, list) and all(isinstance(i, str) for i in cids), f"G4: invalid cluster {cname}")
                covered_ids.update(cids)
            require(covered_ids == set(ids), "G4: clusters must cover exactly all counted IDs")

            if gate["status"] == "PASS":
                min_count = g_def["min_independent_count"]
                require(ind_count >= min_count, f"G4: PASS requires >= {min_count} signals, found {ind_count}")
                min_cluster_size = g_def.get("min_cluster_size", 1)
                require(any(len(cids) >= min_cluster_size for cids in clusters.values()),
                        f"G4: PASS requires at least one cluster with >= {min_cluster_size} members")

        # G1 check
        if name == "G1" and gate["status"] == "PASS":
            min_count = g_def["min_independent_count"]
            require(ind_count >= min_count, f"G1: PASS requires >= {min_count} signals, found {ind_count}")

    if expected_snapshot_id is not None:
        snap_field = card.get("input_commit_or_snapshot")
        require(snap_field in (expected_snapshot_id, BASE_COMMIT),
                f"scorecard input_commit_or_snapshot {snap_field!r} does not match expected snapshot ID {expected_snapshot_id!r}")

    # Verdict rules from policy definition
    v_rules = p_def.get("verdict_rules", {})
    if verdict == "PASS":
        pass_rules = v_rules.get("PASS", {})
        if pass_rules.get("all_gates_pass", True):
            require(all(s == "PASS" for s in states), "PASS verdict requires all gates to be PASS")
        if pass_rules.get("condition_allowed") is False:
            require(card.get("condition") is None, "PASS condition must be null")
        if pass_rules.get("requires_discovery_plan"):
            validate_v2_discovery_plan(card, p_def)
    elif verdict == "CONDITIONAL PASS":
        cp_rules = v_rules.get("CONDITIONAL_PASS", {})
        req_pass = cp_rules.get("required_pass_gates")
        if isinstance(req_pass, list):
            for gname in req_pass:
                require(gates[gname]["status"] == "PASS", f"CONDITIONAL PASS requires {gname} to be PASS")
        elif isinstance(req_pass, int):
            require(states.count("PASS") == req_pass, f"CONDITIONAL PASS requires exactly {req_pass} PASS gates")

        max_fail = cp_rules.get("max_fail_gates", 0)
        require(states.count("FAIL") <= max_fail, f"CONDITIONAL PASS requires <= {max_fail} FAIL gates")

        allowed_unknown = cp_rules.get("allowed_unknown_gates")
        if allowed_unknown is not None:
            require(states.count("UNKNOWN") == allowed_unknown, f"CONDITIONAL PASS requires exactly {allowed_unknown} UNKNOWN gate(s)")
        elif cp_rules.get("requires_unknown_gate", True):
            require("UNKNOWN" in states, "CONDITIONAL PASS requires at least one UNKNOWN gate")

        cond_type = cp_rules.get("condition_type")
        if cond_type == "single_string":
            cond = card.get("condition")
            require(isinstance(cond, str) and bool(cond.strip()), "CONDITIONAL PASS requires condition string")
        elif cp_rules.get("all_unknown_gates_must_be_covered"):
            validate_v2_conditions(card, gates, records, p_def, review_log)

        if cp_rules.get("requires_discovery_plan"):
            validate_v2_discovery_plan(card, p_def)
    elif verdict == "FAIL":
        fail_rules = v_rules.get("FAIL", {})
        if fail_rules.get("requires_fail_gate", False):
            require("FAIL" in states, "FAIL verdict requires at least one FAIL gate")
        if fail_rules.get("requires_cited_contradiction", True):
            contra_exists = any(bool(g.get("contradictory_evidence_ids")) for g in gates.values())
            require(contra_exists, "FAIL verdict requires cited contradictory evidence")
        if policy == "v1":
            require(card.get("condition") is None, "v1 condition must be null unless CONDITIONAL PASS")
        elif policy == "v2" and fail_rules.get("requires_discovery_plan"):
            validate_v2_discovery_plan(card, p_def)
    elif verdict == "INSUFFICIENT EVIDENCE":
        ie_rules = v_rules.get("INSUFFICIENT_EVIDENCE", {})
        if ie_rules.get("requires_unknown_gate", True):
            require("UNKNOWN" in states, "INSUFFICIENT EVIDENCE requires at least one UNKNOWN gate")
        max_fail = ie_rules.get("max_fail_gates", 0)
        require(states.count("FAIL") <= max_fail, f"INSUFFICIENT EVIDENCE cannot have any FAIL gate")
        if policy == "v1":
            require(card.get("condition") is None, "v1 condition must be null unless CONDITIONAL PASS")
        elif policy == "v2" and ie_rules.get("requires_discovery_plan"):
            validate_v2_discovery_plan(card, p_def)

    # Authorization check
    require(type(card.get("stage2_authorized")) is bool, "stage2_authorized must be boolean")
    require(
        card["stage2_authorized"] == (verdict in {"PASS", "CONDITIONAL PASS"}),
        "stage2_authorized must be True for PASS / CONDITIONAL PASS, False otherwise",
    )
