"""Offline regression tests for the v1 source-review contract.

All evidence and captures are explicitly synthetic and exist only in temporary
directories. No network access or repository idea output is modified.
"""
from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

import audit_review_pipeline as arp

def synthetic_record(track, index, *, url=None, author=None, money=False, excerpt=None,
                     independence_key=None, kind=None):
    return {
        "id": f"mb-{track}-synthetic-{index}", "idea": arp.IDEA,
        "type": kind or ("wtp" if money else "pain"),
        "observed_at": "2026-09-09", "source_date": None, "source_type": "community_post",
        "source_tier": "A", "source_url": url or f"https://example.test/source/{track}/{index}",
        "source_excerpt": excerpt, "author_or_entity": author,
        "observation": "Synthetic test-only workflow observation with explicit detail.",
        "interpretation": "Synthetic boundary; never market evidence.", "recurrence": "weekly",
        "money_signal": "saas_spend" if money else None,
        "money_amount": 120 if money else None, "money_currency": "USD" if money else None,
        "money_period": "year" if money else None, "polarity": "supports", "strength": 4,
        "independence_key": independence_key or f"synthetic-entity-{track}-{index}",
        "agent": "synthetic-test", "audit_status": "PENDING", "audit_reason": None,
    }


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="audit-review-synthetic-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shared = "https://example.test/shared?page=1&utm_source=test#speaker"
        self.records = [
            synthetic_record("market", 0, url=shared, author="Speaker A", excerpt="Exact synthetic quote A"),
            synthetic_record("pain", 1, url=shared, author="Speaker B", excerpt="Exact synthetic quote B"),
            synthetic_record("wtp", 2, author="Buyer C", money=True, excerpt="Paid 120 USD per year"),
            synthetic_record("workflow", 3, author="Speaker A", kind="substitute",
                             independence_key="synthetic-entity-market-0"),
        ]
        by_track = {track: [] for track in arp.TRACKS}
        for row in self.records:
            by_track[row["id"].split("-")[1]].append(row)
        for track, rows in by_track.items():
            arp.write_jsonl(self.root / f"ideas/{arp.IDEA}/raw/{track}/evidence.jsonl", rows)
        self.raw, self.locations = arp.load_raw(self.root)
        self.review_dir = self.root / "reviews"
        self.output = self.root / "candidate"
        self.captures = []
        self.reviews = []
        for row in self.records:
            rid = row["id"]
            cid = f"capture-{rid}"
            fragment = f"{row.get('source_excerpt') or ''} {row['observation']} {row['interpretation']}"
            capture = {"schema_version": 1, "capture_id": cid,
                "requested_url": row["source_url"], "resolved_url": row["source_url"],
                "locator": f"synthetic locator for {rid}", "attributed_speaker": row.get("author_or_entity"),
                "inspected_at": "2026-09-09T12:00:00+00:00", "retrieval_tool": "synthetic-test-tool",
                "external_result_id": None, "local_attempt_id": f"attempt-{rid}",
                "outcome": "SUCCESS", "fragment": fragment,
                "fragment_sha256": arp.fragment_fingerprint(fragment)}
            claims = []
            for field in sorted(arp.expected_claim_fields(row)):
                claims.append({"field": field, "decision": "SUPPORTED", "reason": "Synthetic explicit support.",
                               "capture_id": cid, "speaker": row.get("author_or_entity"), "material": True})
            review = {"schema_version": 1, "evidence_id": rid,
                "raw_track": rid.split("-")[1], "raw_path": self.locations[rid],
                "raw_fingerprint": arp.fingerprint(row), "scope_dependency_fingerprint": "",
                "reviewed_at": "2026-09-09T12:00:00+00:00", "reviewer_agent": "synthetic-test",
                "state": "COMPLETE", "blocker": None, "capture_ids": [cid],
                "claim_decisions": claims,
                "audit": {"status": "VERIFIED", "reason": "Synthetic explicit review.",
                          "independence_key": row["independence_key"]},
                "scope": {"scope_status": "IN_SCOPE", "provider_form": "SOLO",
                          "supporting_evidence_ids": [rid], "reason": "Synthetic self-bound scope."},
                "money_assessment": ({"payer": "Synthetic payer", "recipient": "Synthetic vendor",
                    "work_bought_or_done": "Synthetic test-only work.", "payment_status": "PAID",
                    "transaction_type": "ACTUAL", "amount_basis": "Synthetic annual statement.",
                    "unresolved_unknowns": []} if row.get("money_signal") is not None else None),
                "impact_assessment": {"eligible_gates": ["G3" if row.get("money_signal") else "G1"],
                                      "exclusion_reason": None, "unresolved_questions": []},
                "substitute_assessment": ({"capability": "Synthetic capability.",
                    "same_job_fit": "Synthetic fit remains bounded.",
                    "price_or_friction": "Synthetic price/friction note.",
                    "observed_sufficiency": "Synthetic sufficiency observation.",
                    "evidence_needed": "Synthetic remaining evidence."}
                    if row.get("type") == "substitute" else None),
                "discrepancies": [], "raw_owner_repairs": []}
            review["scope_dependency_fingerprint"] = arp.scope_dependency(review, self.raw)
            self.captures.append(capture)
            self.reviews.append(review)
        self.write_bundle()
        arp.render_candidate(self.root, self.review_dir, self.output)

    def write_bundle(self, reviews=None, captures=None):
        arp.write_jsonl(self.review_dir / "reviews.jsonl", reviews if reviews is not None else self.reviews)
        arp.write_jsonl(self.review_dir / "captures.jsonl", captures if captures is not None else self.captures)

    def assert_review_error(self):
        with self.assertRaises(arp.ReviewError):
            arp.check_candidate(self.root, self.review_dir, self.output)

    def test_legacy_diagnostic_uses_fixed_synthetic_fixture(self):
        evidence_dir = self.root / f"ideas/{arp.IDEA}/evidence"
        evidence = arp.read_jsonl(self.output / "evidence.jsonl", "synthetic candidate")
        scope = arp.read_json(self.output / "scope-map.json")
        arp.write_jsonl(evidence_dir / "evidence.jsonl", evidence)
        arp.write_json(evidence_dir / "scope-map.json", scope)
        scope_by_id = {row["evidence_id"]: row for row in scope["records"]}
        ledger_rows = []
        for index, row in enumerate(evidence):
            rid = row["id"]
            url = "https://synthetic.invalid/mutated-url" if index == 0 else row["source_url"]
            key = "synthetic-mutated-key" if index == 1 else row["independence_key"]
            entry = scope_by_id[rid]
            ledger_rows.append(f"| `{rid}` | {rid.split('-')[1]} | `{url}` | synthetic | "
                               f"{row['audit_status']} | {entry['scope_status']} | "
                               f"{entry['provider_form']} | {key} |")
        (evidence_dir / "audit-summary.md").write_text(
            "Synthetic legacy fixture claims 5 unique source URLs.\n" + "\n".join(ledger_rows),
            encoding="utf-8")
        result = arp.legacy_diagnostic(self.root)
        self.assertEqual((result["raw_records"], result["exact_url_differences"],
                          result["independence_key_differences"]), (4, 1, 1))
        self.assertEqual((result["audited_distinct_exact_urls"], result["ledger_distinct_exact_urls"],
                          result["narrative_claimed_unique_urls"]), (3, 4, 5))

    def test_two_renders_match_and_raw_is_unchanged(self):
        before = {rid: arp.fingerprint(row) for rid, row in arp.load_raw(self.root)[0].items()}
        second = self.root / "candidate-two"
        arp.render_candidate(self.root, self.review_dir, second)
        for name in ("evidence.jsonl", "scope-map.json", "source-review-manifest.json",
                     "raw-owner-repairs.jsonl", "audit-summary.md", "high-impact-review.md"):
            self.assertEqual((self.output / name).read_bytes(), (second / name).read_bytes())
        after = {rid: arp.fingerprint(row) for rid, row in arp.load_raw(self.root)[0].items()}
        self.assertEqual(before, after)

    def test_documented_render_and_check_cli_shape(self):
        self.assertEqual(arp.main(["--root", str(self.root), "render",
                                  "--reviews", "reviews", "--output", "candidate-cli"]), 0)
        self.assertEqual(arp.main(["--root", str(self.root), "check",
                                  "--reviews", "reviews", "--candidate", "candidate-cli"]), 0)

    def test_ledger_url_author_id_key_status_and_count_mutations_fail(self):
        path = self.output / "audit-summary.md"
        original = path.read_text(encoding="utf-8")
        mutations = [
            (self.records[0]["source_url"], "https://wrong.example.test/"),
            ("Speaker A", "Wrong Speaker"),
            (self.records[0]["id"], "mb-market-mutated"),
            (self.records[0]["independence_key"], "mutated-key"),
            ("VERIFIED", "REJECTED"),
            ('"raw_rows": 4', '"raw_rows": 99'),
        ]
        for old, new in mutations:
            with self.subTest(field=old):
                path.write_text(original.replace(old, new, 1), encoding="utf-8")
                self.assert_review_error()
                path.write_text(original, encoding="utf-8")

    def test_missing_duplicate_and_unknown_reviews_fail(self):
        variants = [self.reviews[:-1], self.reviews + [copy.deepcopy(self.reviews[0])]]
        unknown = copy.deepcopy(self.reviews[0])
        unknown["evidence_id"] = "mb-market-unknown"
        variants.append(self.reviews + [unknown])
        for rows in variants:
            with self.subTest(size=len(rows)):
                self.write_bundle(reviews=rows)
                self.assert_review_error()
        self.write_bundle()

    def test_duplicate_capture_fails(self):
        self.write_bundle(captures=self.captures + [copy.deepcopy(self.captures[0])])
        self.assert_review_error()

    def test_changed_raw_row_invalidates_only_its_review(self):
        rows = [dict(x) for x in self.records if x["id"].startswith("mb-market-")]
        rows[0]["observation"] += " changed"
        arp.write_jsonl(self.root / f"ideas/{arp.IDEA}/raw/market/evidence.jsonl", rows)
        with self.assertRaisesRegex(arp.ReviewError, f"{rows[0]['id']}: stale raw fingerprint"):
            arp.check_candidate(self.root, self.review_dir, self.output)

    def test_changed_scope_dependency_fails(self):
        rows = copy.deepcopy(self.reviews)
        rows[0]["scope"]["reason"] = "Changed dependency without new hash."
        self.write_bundle(reviews=rows)
        with self.assertRaisesRegex(arp.ReviewError, "stale scope/support dependency"):
            arp.check_candidate(self.root, self.review_dir, self.output)

    def test_altered_capture_fragment_fails_hash(self):
        captures = copy.deepcopy(self.captures)
        captures[0]["fragment"] += " altered"
        self.write_bundle(captures=captures)
        with self.assertRaisesRegex(arp.ReviewError, "matching preserved fragment hash"):
            arp.check_candidate(self.root, self.review_dir, self.output)

    def test_unsupported_verified_transition_fails(self):
        rows = copy.deepcopy(self.reviews)
        next(x for x in rows[0]["claim_decisions"] if x["field"] == "observation")["decision"] = "UNKNOWN"
        self.write_bundle(reviews=rows)
        with self.assertRaisesRegex(arp.ReviewError, "unsupported material claim"):
            arp.check_candidate(self.root, self.review_dir, self.output)

    def test_wrong_speaker_and_rewritten_quote_fail(self):
        captures = copy.deepcopy(self.captures)
        rows = copy.deepcopy(self.reviews)
        wrong_speaker_capture = copy.deepcopy(captures[0])
        wrong_speaker_capture.update(capture_id="capture-other-speaker",
                                     local_attempt_id="attempt-other-speaker",
                                     attributed_speaker="Another Speaker")
        captures[0]["fragment"] = "Canonical author identity, without the quoted text."
        captures[0]["fragment_sha256"] = arp.fragment_fingerprint(captures[0]["fragment"])
        captures.append(wrong_speaker_capture)
        rows[0]["capture_ids"].append(wrong_speaker_capture["capture_id"])
        quote = next(x for x in rows[0]["claim_decisions"] if x["field"] == "quote")
        quote.update(capture_id=wrong_speaker_capture["capture_id"], speaker="Another Speaker")
        self.write_bundle(reviews=rows, captures=captures)
        with self.assertRaisesRegex(arp.ReviewError, "quote speaker differs"):
            arp.check_candidate(self.root, self.review_dir, self.output)
        captures = copy.deepcopy(self.captures)
        captures[0]["fragment"] = "A rewritten composite without the canonical excerpt."
        captures[0]["fragment_sha256"] = arp.fragment_fingerprint(captures[0]["fragment"])
        self.write_bundle(reviews=self.reviews, captures=captures)
        with self.assertRaisesRegex(arp.ReviewError, "direct quote not contained"):
            arp.check_candidate(self.root, self.review_dir, self.output)

    def test_money_amount_and_period_decisions_are_mandatory(self):
        money = next(x for x in self.reviews if x["evidence_id"].startswith("mb-wtp-"))
        for field in ("money_amount", "money_period"):
            rows = copy.deepcopy(self.reviews)
            target = next(x for x in rows if x["evidence_id"] == money["evidence_id"])
            target["claim_decisions"] = [x for x in target["claim_decisions"] if x["field"] != field]
            self.write_bundle(reviews=rows)
            with self.subTest(field=field), self.assertRaisesRegex(arp.ReviewError, "missing required claim"):
                arp.check_candidate(self.root, self.review_dir, self.output)

    def test_money_assessment_cannot_contradict_verified_signal(self):
        rows = copy.deepcopy(self.reviews)
        target = next(x for x in rows if x["evidence_id"].startswith("mb-wtp-"))
        target["money_assessment"].update(payment_status="FREE", transaction_type="HYPOTHETICAL")
        self.write_bundle(reviews=rows)
        with self.assertRaisesRegex(arp.ReviewError, "contradictory money assessment"):
            arp.check_candidate(self.root, self.review_dir, self.output)

    def test_nullable_labor_price_context_and_stated_intent_remain_legal(self):
        base = {"money_amount": None}
        cases = [
            ("employee_time", "UNKNOWN", "ACTUAL"),
            ("dedicated_role", "UNKNOWN", "ACTUAL"),
            ("competitor_price", "UNKNOWN", "OFFER"),
            ("stated_wtp", "UNKNOWN", "INTENT"),
        ]
        for signal, payment, transaction in cases:
            assessment = {"payment_status": payment, "transaction_type": transaction,
                          "amount_basis": None}
            with self.subTest(signal=signal):
                self.assertEqual(arp.money_assessment_conflicts(
                    {**base, "money_signal": signal}, assessment), [])

    def test_uninspected_money_blocker_checkpoints_without_invented_raw_repair(self):
        review = copy.deepcopy(self.reviews[2])
        capture = copy.deepcopy(self.captures[2])
        review.update(state="BLOCKED", blocker="Synthetic source quota error; source not inspected.")
        review["audit"].update(status="PENDING", reason=review["blocker"])
        review["scope"].update(scope_status="UNKNOWN", provider_form="UNKNOWN", supporting_evidence_ids=[])
        review["impact_assessment"].update(eligible_gates=[], exclusion_reason=review["blocker"])
        review["money_assessment"].update(
            payer=None, recipient=None, work_bought_or_done=None, amount_basis=None,
            payment_status="UNKNOWN", transaction_type="UNKNOWN",
            unresolved_unknowns=["Synthetic source inaccessible; no observed payment or contradiction."])
        for claim in review["claim_decisions"]:
            claim.update(decision="UNKNOWN", capture_id=None, speaker=None, reason=review["blocker"])
        capture.update(outcome="BLOCKED", fragment=None, fragment_sha256=None,
                       resolved_url=None, locator=None, attributed_speaker=None)
        review["scope_dependency_fingerprint"] = arp.scope_dependency(review, self.raw)
        state_dir = self.root / "uninspected-money-batch"
        arp.prepare_batch(self.root, state_dir, [review["evidence_id"]])
        arp.write_jsonl(state_dir / "reviews.jsonl", [review])
        arp.write_jsonl(state_dir / "captures.jsonl", [capture])
        state = arp.checkpoint_batch(self.root, state_dir)
        self.assertEqual(state["blocked_ids"], [review["evidence_id"]])
        self.assertEqual(state["processed_ids"], [])
        saved = arp.read_jsonl(state_dir / "reviews.jsonl", "blocked review")[0]
        self.assertEqual(saved["audit"]["status"], "PENDING")
        self.assertEqual(saved["discrepancies"], [])
        self.assertEqual(saved["raw_owner_repairs"], [])
        self.assertEqual(arp.load_raw(self.root)[0], self.raw)
        # Successful source access later resumes this same record normally.
        arp.write_jsonl(state_dir / "captures.jsonl", [capture, self.captures[2] | {
            "capture_id": "capture-money-retry", "local_attempt_id": "attempt-money-retry"}])
        resumed = copy.deepcopy(self.reviews[2])
        resumed["capture_ids"] = [capture["capture_id"], "capture-money-retry"]
        for claim in resumed["claim_decisions"]:
            claim["capture_id"] = "capture-money-retry"
        arp.write_jsonl(state_dir / "reviews.jsonl", [resumed])
        state = arp.checkpoint_batch(self.root, state_dir)
        self.assertEqual(state["processed_ids"], [review["evidence_id"]])
        self.assertEqual(state["blocked_ids"], [])

    def test_blocked_money_with_observed_conflict_still_needs_raw_owner_repair(self):
        review = copy.deepcopy(self.reviews[2])
        review.update(state="BLOCKED", blocker="Synthetic remaining inspection blocked.")
        review["audit"].update(status="PENDING", reason=review["blocker"])
        review["money_assessment"].update(payment_status="FREE", transaction_type="HYPOTHETICAL")
        next(c for c in review["claim_decisions"] if c["field"] == "money_type")["decision"] = "CONTRADICTED"
        with self.assertRaisesRegex(arp.ReviewError, "must queue material money_signal repair"):
            arp.validate_review(review, self.raw, self.locations,
                                {c["capture_id"]: c for c in self.captures})

    def test_material_conflict_routes_to_queue_and_blocks_verified(self):
        rows = copy.deepcopy(self.reviews)
        rows[0]["discrepancies"] = [{"field": "author_or_entity", "raw_value": "Speaker A",
            "observed_value": "Speaker X", "material": True, "reason": "Synthetic contradiction."}]
        rows[0]["raw_owner_repairs"] = [{"field": "author_or_entity", "observed_value": "Speaker X",
                                         "reason": "Raw owner must review."}]
        self.write_bundle(reviews=rows)
        with self.assertRaisesRegex(arp.ReviewError, "unresolved material discrepancy"):
            arp.check_candidate(self.root, self.review_dir, self.output)

    def test_shared_page_different_speakers_and_entity_counts_remain_separate(self):
        evidence = arp.read_jsonl(self.output / "evidence.jsonl", "candidate")
        scope = arp.read_json(self.output / "scope-map.json")
        captures = {x["capture_id"]: x for x in self.captures}
        counts = arp.report_counts(evidence, scope, captures)
        self.assertEqual(counts["raw_rows"], 4)
        self.assertEqual(counts["distinct_exact_urls"], 3)
        self.assertEqual(counts["distinct_normalized_url_groups"], 3)
        self.assertEqual(counts["distinct_independence_keys"], 3)
        self.assertEqual(counts["successful_inspections"], 4)

    def test_blocked_batch_checkpoints_and_resumes_without_dropping_ids(self):
        ids = [x["id"] for x in self.records[:3]]
        state_dir = self.root / "batch"
        state = arp.prepare_batch(self.root, state_dir, ids)
        self.assertEqual(state["remaining_ids"], ids)
        manifest = arp.read_json(state_dir / "batch-manifest.json")
        self.assertEqual(manifest["source_groups"][0]["evidence_ids"], ids[:2])
        # A change outside this three-ID batch must not invalidate resumable work.
        unrelated = copy.deepcopy(self.records[3])
        unrelated["observation"] += " unrelated change"
        arp.write_jsonl(self.root / f"ideas/{arp.IDEA}/raw/workflow/evidence.jsonl", [unrelated])
        blocked = copy.deepcopy(self.reviews[1])
        blocked.update(state="BLOCKED", blocker="Synthetic quota blocker.")
        blocked["audit"].update(status="PENDING", reason="Blocked; no fresh verification.")
        arp.write_jsonl(state_dir / "reviews.jsonl", [self.reviews[0], blocked])
        arp.write_jsonl(state_dir / "captures.jsonl", self.captures[:2])
        state = arp.checkpoint_batch(self.root, state_dir)
        self.assertEqual(state["processed_ids"], [ids[0]])
        self.assertEqual(state["blocked_ids"], [ids[1]])
        self.assertEqual(state["remaining_ids"], [ids[2]])
        arp.write_jsonl(state_dir / "reviews.jsonl", self.reviews[:2])
        state = arp.checkpoint_batch(self.root, state_dir)
        self.assertEqual(state["processed_ids"], ids[:2])
        self.assertEqual(state["blocked_ids"], [])
        self.assertEqual(state["remaining_ids"], [ids[2]])
        state2 = arp.prepare_batch(self.root, state_dir, ids)
        self.assertEqual(state2, state)

    def test_checkpoint_cannot_reseal_changed_external_scope_support(self):
        review = copy.deepcopy(self.reviews[0])
        support = copy.deepcopy(self.records[3])
        review["scope"]["supporting_evidence_ids"] = [support["id"]]
        review["scope_dependency_fingerprint"] = arp.scope_dependency(review, self.raw)
        state_dir = self.root / "external-support-batch"
        arp.prepare_batch(self.root, state_dir, [review["evidence_id"]])
        arp.write_jsonl(state_dir / "reviews.jsonl", [review])
        arp.write_jsonl(state_dir / "captures.jsonl", [self.captures[0]])
        arp.checkpoint_batch(self.root, state_dir)
        before_reviews = (state_dir / "reviews.jsonl").read_bytes()
        before_captures = (state_dir / "captures.jsonl").read_bytes()
        support["observation"] += " material change after completed review"
        arp.write_jsonl(self.root / f"ideas/{arp.IDEA}/raw/workflow/evidence.jsonl", [support])
        with self.assertRaisesRegex(arp.ReviewError, "stale scope/support dependency"):
            arp.checkpoint_batch(self.root, state_dir)
        self.assertEqual((state_dir / "reviews.jsonl").read_bytes(), before_reviews)
        self.assertEqual((state_dir / "captures.jsonl").read_bytes(), before_captures)

    def test_tampered_repair_queue_fails(self):
        (self.output / "raw-owner-repairs.jsonl").write_text(
            json.dumps({"schema_version": 1, "evidence_id": self.records[0]["id"],
                        "field": "observation", "observed_value": "invented", "reason": "tampered"}) + "\n",
            encoding="utf-8")
        with self.assertRaisesRegex(arp.ReviewError, "repair queue differs"):
            arp.check_candidate(self.root, self.review_dir, self.output)

    def test_issue_diagnostics_report_missing_and_extra_fields_together(self):
        rid = "mb-wtp-synthetic-2"
        discrepancies = [{"field": "money_currency", "raw_value": "USD",
                          "observed_value": None, "reason": "Synthetic unknown currency."}]
        repairs = [{"field": "money_currency", "action": "Synthetic repair instruction.",
                    "reason": "Synthetic missing support."}]
        with self.assertRaises(arp.ReviewError) as caught:
            arp.validate_review_issue_shapes(rid, discrepancies, repairs)
        message = str(caught.exception)
        self.assertIn(f"{rid}.discrepancies[0]", message)
        self.assertIn("missing=['material']", message)
        self.assertIn(f"{rid}.raw_owner_repairs[0]", message)
        self.assertIn("missing=['observed_value'] unexpected=['action']", message)
        discrepancies[0]["material"] = "true"
        with self.assertRaisesRegex(arp.ReviewError, "material: expected boolean"):
            arp.validate_review_issue_shapes(rid, discrepancies, [])

    def test_issue_schema_declares_the_exact_runtime_shapes(self):
        schema = arp.read_json(Path(__file__).resolve().parents[1] / "methodology/source-review-schema.json")
        for definition, field, expected in (
            ("discrepancy", "discrepancies", arp.DISCREPANCY_FIELDS),
            ("rawOwnerRepair", "raw_owner_repairs", arp.RAW_OWNER_REPAIR_FIELDS),
        ):
            with self.subTest(definition=definition):
                shape = schema["$defs"][definition]
                self.assertEqual(set(shape["required"]), expected)
                self.assertEqual(set(shape["properties"]), expected)
                self.assertIs(shape["additionalProperties"], False)
                self.assertEqual(schema["$defs"]["review"]["properties"][field]["items"],
                                 {"$ref": f"#/$defs/{definition}"})

    def test_repaired_issue_shape_can_checkpoint_without_changing_raw_or_audit_decision(self):
        review = copy.deepcopy(self.reviews[2])
        review["audit"]["status"] = "PARTIALLY_VERIFIED"
        review["scope"].update(scope_status="UNKNOWN", provider_form="UNKNOWN", supporting_evidence_ids=[])
        next(c for c in review["claim_decisions"] if c["field"] == "money_currency")["decision"] = "UNKNOWN"
        review["discrepancies"] = [{"field": "money_currency", "raw_value": "USD",
            "observed_value": "Synthetic currency unknown.", "material": True,
            "reason": "Synthetic currency claim needs review."}]
        review["raw_owner_repairs"] = [{"field": "money_currency",
            "observed_value": "Synthetic currency unknown.",
            "reason": "Synthetic reason. Requested action: confirm currency before raw repair."}]
        state_dir = self.root / "issue-repair-batch"
        arp.prepare_batch(self.root, state_dir, [review["evidence_id"]])
        arp.write_jsonl(state_dir / "reviews.jsonl", [review])
        arp.write_jsonl(state_dir / "captures.jsonl", [self.captures[2]])
        state = arp.checkpoint_batch(self.root, state_dir)
        saved = arp.read_jsonl(state_dir / "reviews.jsonl", "review")[0]
        self.assertEqual(state["processed_ids"], [review["evidence_id"]])
        self.assertEqual(saved["audit"], review["audit"])
        self.assertEqual(saved["raw_owner_repairs"], review["raw_owner_repairs"])
        self.assertEqual(arp.load_raw(self.root)[0], self.raw)


if __name__ == "__main__":
    unittest.main()
