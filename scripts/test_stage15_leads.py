"""Offline tests for the Stage 1.5 lead-research contract."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "stage15_leads", Path(__file__).with_name("stage15_leads.py")
)
stage15 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stage15)
ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "ideas/multi-brand-content/stage1.5/lead-research/config.json")
                    .read_text(encoding="utf-8"))
STAMP = "2026-09-11T10:00:00+00:00"


class Stage15LeadTests(unittest.TestCase):
    def setUp(self):
        capture = redirect_stdout(StringIO())
        capture.__enter__()
        self.addCleanup(capture.__exit__, None, None, None)
        self.temp = tempfile.TemporaryDirectory(prefix="stage15-leads-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.base = self.root / "ideas/multi-brand-content/stage1.5/lead-research"
        self.base.mkdir(parents=True)
        self.write_json("config.json", CONFIG)
        self.write_text("leads.jsonl", "")
        self.write_text("source-register.jsonl", "")
        self.write_text("lead-research-report.md", "# Synthetic\n\nNo outreach occurred.\n")

    def write_text(self, relative, value):
        (self.base / relative).write_text(value, encoding="utf-8")

    def write_json(self, relative, value):
        self.write_text(relative, json.dumps(value, ensure_ascii=False, indent=2) + "\n")

    def write_jsonl(self, relative, rows):
        self.write_text(relative, "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))

    def source(self, lead_index, source_index, path, kind, supports, outcome="SUCCESS"):
        lead_id = f"mb-lead-{lead_index:03d}"
        base_index = (lead_index - 1) * 4 + source_index
        official = f"https://agency-{lead_index}.example"
        url = f"{official}/{path}" if path else official
        return {
            "schema_version": 1,
            "source_id": f"mb-src-{base_index:04d}",
            "lead_id": lead_id,
            "url": url,
            "source_kind": kind,
            "publisher": f"Agency {lead_index}",
            "retrieved_at": STAMP,
            "retrieval_outcome": outcome,
            "retrieval_tool": "Synthetic browser fixture",
            "locator": "Synthetic visible section" if outcome == "SUCCESS" else None,
            "exact_fragment": "Synthetic source fragment for structural tests only."
            if outcome == "SUCCESS" else None,
            "supports": supports if outcome == "SUCCESS" else [],
            "notes": None,
        }

    def fixture(self, lead_index=1, priority_a=False):
        common = [
            "ACTIVE_BUSINESS", "ENGLISH_SERVICE", "EXTERNAL_SERVICE_PROVIDER",
            "ORGANIC_SOCIAL_MANAGEMENT", "RECURRING_CONTENT_SERVICE",
            "STATIC_OR_CAROUSEL_CONTENT", "MULTIPLE_CLIENT_BRANDS",
        ]
        if priority_a:
            common += ["SMB_CLIENTELE", "OWNER_HANDS_ON_PRODUCTION"]
        sources = [
            self.source(lead_index, 1, "", "OFFICIAL_SITE", common),
            self.source(lead_index, 2, "team-size", "AGENCY_DIRECTORY", ["TEAM_SIZE_2_20"]),
            self.source(lead_index, 3, "about", "OFFICIAL_TEAM", ["OWNER_IDENTITY"]),
            self.source(lead_index, 4, "contact", "OFFICIAL_CONTACT", ["PUBLIC_BUSINESS_CONTACT"]),
        ]
        by_claim = {claim: [] for claim in stage15.CLAIMS}
        qualification = {claim: "UNKNOWN" for claim in stage15.CLAIMS}
        for source in sources:
            for claim in source["supports"]:
                qualification[claim] = "CONFIRMED"
                by_claim[claim].append(source["source_id"])
        unknowns = sorted(claim for claim in CONFIG["screening_unknowns_allowed"]
                          if qualification[claim] == "UNKNOWN")
        lead = {
            "schema_version": 1,
            "lead_id": f"mb-lead-{lead_index:03d}",
            "idea_id": "multi-brand-content",
            "scope_id": "MULTIBRAND-OPERATOR-01",
            "organization_name": f"Agency {lead_index}",
            "organization_key": f"agency-{lead_index}",
            "website_url": f"https://agency-{lead_index}.example",
            "canonical_domain": f"agency-{lead_index}.example",
            "city": "Test City",
            "country": "Testland",
            "working_language": "English",
            "team_size_min": 2,
            "team_size_max": 9,
            "team_size_label": "2-9",
            "owner_name": f"Owner {lead_index}",
            "owner_role": "Founder",
            "qualification": qualification,
            "claim_source_ids": by_claim,
            "contact_channel": "CONTACT_FORM",
            "contact_url": f"https://agency-{lead_index}.example/contact",
            "contact_source_id": sources[3]["source_id"],
            "source_ids": [source["source_id"] for source in sources],
            "screening_unknowns": unknowns,
            "status": "QUALIFIED_FOR_SCREENING",
            "priority": "A" if priority_a else "B",
            "exclusion_reasons": [],
            "duplicate_of": None,
            "notes": "Synthetic lead for checker tests only.",
            "last_verified_at": STAMP,
        }
        return lead, sources

    def save(self, leads, sources):
        self.write_jsonl("leads.jsonl", leads)
        self.write_jsonl("source-register.jsonl", sources)

    def complete_report(self):
        self.write_text(
            "lead-research-report.md",
            "# Synthetic final report\n\n" +
            "This test-only narrative contains no market evidence. " * 20 +
            "\n\nNo outreach occurred.\n",
        )

    def test_empty_checkpoint_and_check(self):
        stage15.checkpoint(self.root, "multi-brand-content")
        _, summary = stage15.check_generated(self.root, "multi-brand-content")
        self.assertEqual(summary["qualified_leads"], 0)
        status = json.loads((self.base / "run-status.json").read_text(encoding="utf-8"))
        self.assertEqual(status["status"], "IN_PROGRESS")

    def test_valid_qualified_lead_and_generated_totals(self):
        lead, sources = self.fixture()
        self.save([lead], sources)
        stage15.checkpoint(self.root, "multi-brand-content")
        _, summary = stage15.check_generated(self.root, "multi-brand-content")
        self.assertEqual(summary["qualified_leads"], 1)
        self.assertEqual(summary["unique_qualified_domains"], 1)
        self.assertEqual(summary["source_records"], 4)
        self.assertIn("mb-lead-001", (self.base / "leads.csv").read_text(encoding="utf-8"))

    def test_final_requires_target_and_real_report(self):
        lead, sources = self.fixture()
        self.save([lead], sources)
        with self.assertRaises(stage15.LeadError):
            stage15.checkpoint(self.root, "multi-brand-content", require_final=True)

    def test_exact_target_seals_and_hashes(self):
        leads, sources = [], []
        for index in range(1, 51):
            lead, source_rows = self.fixture(index)
            leads.append(lead)
            sources.extend(source_rows)
        self.save(leads, sources)
        self.complete_report()
        stage15.seal(self.root, "multi-brand-content", "mb-leads-test-001")
        _, summary = stage15.check_generated(self.root, "multi-brand-content", require_final=True)
        self.assertEqual(summary["qualified_leads"], 50)
        self.assertTrue(summary["ready_for_codex_audit"])

    def test_duplicate_domain_and_name_rejected(self):
        first, first_sources = self.fixture(1)
        second, second_sources = self.fixture(2)
        second["canonical_domain"] = first["canonical_domain"]
        second["website_url"] = first["website_url"]
        self.save([first, second], first_sources + second_sources)
        with self.assertRaises(stage15.LeadError):
            stage15.validate_dataset(self.root, "multi-brand-content")

        second["canonical_domain"] = "agency-2.example"
        second["website_url"] = "https://agency-2.example"
        second["organization_name"] = first["organization_name"]
        second["organization_key"] = first["organization_key"]
        self.save([first, second], first_sources + second_sources)
        with self.assertRaises(stage15.LeadError):
            stage15.validate_dataset(self.root, "multi-brand-content")

    def test_cross_lead_source_binding_rejected(self):
        first, first_sources = self.fixture(1)
        second, second_sources = self.fixture(2)
        first["claim_source_ids"]["TEAM_SIZE_2_20"] = [second_sources[1]["source_id"]]
        self.save([first, second], first_sources + second_sources)
        with self.assertRaises(stage15.LeadError):
            stage15.validate_dataset(self.root, "multi-brand-content")

    def test_blocked_source_cannot_support_claim(self):
        lead, sources = self.fixture()
        sources[1]["retrieval_outcome"] = "BLOCKED"
        sources[1]["locator"] = None
        sources[1]["exact_fragment"] = None
        sources[1]["supports"] = []
        self.save([lead], sources)
        with self.assertRaises(stage15.LeadError):
            stage15.validate_dataset(self.root, "multi-brand-content")

    def test_team_range_and_priority_are_fail_closed(self):
        lead, sources = self.fixture()
        lead["team_size_max"] = 50
        self.save([lead], sources)
        with self.assertRaises(stage15.LeadError):
            stage15.validate_dataset(self.root, "multi-brand-content")

    def test_scope_contradiction_cannot_remain_qualified(self):
        lead, sources = self.fixture()
        lead["qualification"]["SMB_CLIENTELE"] = "CONTRADICTED"
        lead["claim_source_ids"]["SMB_CLIENTELE"] = [sources[0]["source_id"]]
        sources[0]["supports"].append("SMB_CLIENTELE")
        self.save([lead], sources)
        with self.assertRaises(stage15.LeadError):
            stage15.validate_dataset(self.root, "multi-brand-content")

        lead, sources = self.fixture()
        lead["priority"] = "A"
        self.save([lead], sources)
        with self.assertRaises(stage15.LeadError):
            stage15.validate_dataset(self.root, "multi-brand-content")

    def test_contact_url_must_be_inspected_route(self):
        lead, sources = self.fixture()
        lead["contact_url"] = "https://agency-1.example/another-contact"
        self.save([lead], sources)
        with self.assertRaises(stage15.LeadError):
            stage15.validate_dataset(self.root, "multi-brand-content")

    def test_stale_generated_and_snapshot_rejected(self):
        lead, sources = self.fixture()
        self.save([lead], sources)
        stage15.checkpoint(self.root, "multi-brand-content")
        lead["notes"] = "Changed after rendering."
        self.save([lead], sources)
        with self.assertRaises(stage15.LeadError):
            stage15.check_generated(self.root, "multi-brand-content")

    def test_duplicate_json_property_rejected(self):
        self.write_text("leads.jsonl", '{"lead_id":"a","lead_id":"b"}\n')
        with self.assertRaises(stage15.LeadError):
            stage15.validate_dataset(self.root, "multi-brand-content")

    def test_config_cannot_authorize_outreach_or_expand_interview_cap(self):
        config = copy.deepcopy(CONFIG)
        config["outreach_authorized"] = True
        with self.assertRaises(stage15.LeadError):
            stage15.validate_config(config)
        config = copy.deepcopy(CONFIG)
        config["max_counted_conversations"] = 9
        with self.assertRaises(stage15.LeadError):
            stage15.validate_config(config)


if __name__ == "__main__":
    unittest.main()
