#!/usr/bin/env python3
"""Independent regression probes for 05de6b6, using only temporary synthetic data.

Run: python reproduce_05de6b6.py --repo /path/to/saas-validation-starter
Expected on 05de6b6: four FAIL results (each exposes an accepted invalid state).
Expected after repair: four PASS results, or an explicit migration if the public
test-fixture/interface contract changes. Never copy these fixtures to real ideas.
"""
from __future__ import annotations

import argparse
import copy
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    sys.path.insert(0, str(repo / "scripts"))
    import audit_review_pipeline as arp
    import test_audit_review_pipeline as pipeline_tests
    import test_check_multibrand_stage1 as checker_tests

    class IndependentRegressionTests(unittest.TestCase):
        def pipeline_fixture(self):
            fixture = pipeline_tests.PipelineTests()
            fixture.setUp()
            self.addCleanup(fixture.doCleanups)
            return fixture

        def render_and_check(self, fixture):
            arp.render_candidate(fixture.root, fixture.review_dir, fixture.output)
            arp.check_candidate(fixture.root, fixture.review_dir, fixture.output)

        def test_quote_cannot_belong_to_a_different_speaker_than_attribution(self):
            fixture = self.pipeline_fixture()
            captures = copy.deepcopy(fixture.captures)
            reviews = copy.deepcopy(fixture.reviews)
            # A genuinely separate source fragment has a different speaker on
            # the same page. The canonical quote exists only in B's fragment.
            wrong_speaker_capture = copy.deepcopy(captures[0])
            wrong_speaker_capture.update(
                capture_id="capture-synthetic-other-speaker",
                local_attempt_id="attempt-synthetic-other-speaker",
                attributed_speaker="Different synthetic speaker",
            )
            captures[0]["fragment"] = "Synthetic speaker A identity and unrelated text only."
            captures[0]["fragment_sha256"] = arp.fragment_fingerprint(captures[0]["fragment"])
            captures.append(wrong_speaker_capture)
            reviews[0]["capture_ids"].append(wrong_speaker_capture["capture_id"])
            quote_claim = next(c for c in reviews[0]["claim_decisions"] if c["field"] == "quote")
            quote_claim.update(capture_id=wrong_speaker_capture["capture_id"],
                               speaker=wrong_speaker_capture["attributed_speaker"])
            fixture.write_bundle(reviews=reviews, captures=captures)
            with self.assertRaises(arp.ReviewError, msg="Wrong-speaker quote retained VERIFIED through strict render/check"):
                self.render_and_check(fixture)

        def test_free_hypothetical_assessment_cannot_verify_actual_saas_spend(self):
            fixture = self.pipeline_fixture()
            reviews = copy.deepcopy(fixture.reviews)
            row = next(r for r in reviews if r["evidence_id"].startswith("mb-wtp-"))
            # Explicit structured contradiction, not a subtle natural-language
            # interpretation: raw saas_spend versus FREE/HYPOTHETICAL review.
            row["money_assessment"].update(payment_status="FREE", transaction_type="HYPOTHETICAL")
            fixture.write_bundle(reviews=reviews)
            with self.assertRaises(arp.ReviewError, msg="FREE/HYPOTHETICAL saas_spend retained VERIFIED through strict render/check"):
                self.render_and_check(fixture)

        def test_judge_cannot_count_explicitly_excluded_evidence(self):
            fixture = checker_tests.WorkflowTests()
            fixture.setUp()
            self.addCleanup(fixture.doCleanups)
            _, audited, _ = fixture.fixture()
            review_dir = fixture.root / "ideas/multi-brand-content/evidence/source-reviews"
            reviews = arp.read_jsonl(review_dir / "reviews.jsonl", "synthetic reviews")
            for review in reviews:
                review["impact_assessment"] = {
                    "eligible_gates": [],
                    "exclusion_reason": "Synthetic explicit exclusion: no gate may count this row.",
                    "unresolved_questions": [],
                }
            arp.write_jsonl(review_dir / "reviews.jsonl", reviews)
            fixture.save_score(fixture.scorecard(audited))
            with self.assertRaises((arp.ReviewError, checker_tests.mb.CheckError),
                                   msg="Judge accepted PASS with all counted evidence explicitly excluded by source reviews"):
                arp.render_candidate(fixture.root, review_dir,
                                     fixture.root / "ideas/multi-brand-content/evidence")
                fixture.checker.judge()

        def test_checkpoint_cannot_reseal_changed_out_of_batch_scope_support(self):
            fixture = self.pipeline_fixture()
            review = copy.deepcopy(fixture.reviews[0])
            support = copy.deepcopy(fixture.records[3])
            review["scope"]["supporting_evidence_ids"] = [support["id"]]
            review["scope_dependency_fingerprint"] = arp.scope_dependency(review, fixture.raw)
            state_dir = fixture.root / "batch"
            arp.prepare_batch(fixture.root, state_dir, [review["evidence_id"]])
            arp.write_jsonl(state_dir / "reviews.jsonl", [review])
            arp.write_jsonl(state_dir / "captures.jsonl", [fixture.captures[0]])
            arp.checkpoint_batch(fixture.root, state_dir)
            support["observation"] += " Synthetic material support change after review."
            arp.write_jsonl(fixture.root / "ideas/multi-brand-content/raw/workflow/evidence.jsonl", [support])
            # Prove the review is stale before checkpoint. The selected raw row
            # itself is unchanged; only its explicit dependency changed.
            raw, locations = arp.load_raw(fixture.root)
            with self.assertRaisesRegex(arp.ReviewError, "stale scope/support dependency"):
                arp.load_review_bundle(state_dir, raw, locations)
            with self.assertRaises(arp.ReviewError, msg="Checkpoint silently refreshed stale support hash and preserved COMPLETE/VERIFIED"):
                arp.checkpoint_batch(fixture.root, state_dir)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(IndependentRegressionTests)
    # Fixture tools are verbose; unittest diagnostics on stderr remain visible.
    with redirect_stdout(io.StringIO()):
        result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
