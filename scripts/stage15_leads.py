#!/usr/bin/env python3
"""Offline Stage 1.5 lead dataset validator, renderer and snapshot sealer.

This script never retrieves a URL and never sends outreach. Passing it proves
local structure and cross-file consistency, not that a public source is true or
currently reachable.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


SCHEMA_VERSION = 1
CLAIMS = (
    "ACTIVE_BUSINESS",
    "ENGLISH_SERVICE",
    "EXTERNAL_SERVICE_PROVIDER",
    "TEAM_SIZE_2_20",
    "OWNER_IDENTITY",
    "ORGANIC_SOCIAL_MANAGEMENT",
    "RECURRING_CONTENT_SERVICE",
    "STATIC_OR_CAROUSEL_CONTENT",
    "MULTIPLE_CLIENT_BRANDS",
    "PUBLIC_BUSINESS_CONTACT",
    "SMB_CLIENTELE",
    "OWNER_HANDS_ON_PRODUCTION",
    "RECURRING_REVISION_PAIN",
    "CURRENT_TOOL_STACK",
    "BUDGET_AUTHORITY",
    "WILLINGNESS_TO_PAY",
)
CLAIM_STATUSES = {"CONFIRMED", "UNKNOWN", "CONTRADICTED"}
LEAD_STATUSES = {"QUALIFIED_FOR_SCREENING", "HOLD", "EXCLUDED"}
PRIORITIES = {"A", "B", "C", "NONE"}
CONTACT_CHANNELS = {
    "CONTACT_FORM", "BOOKING_PAGE", "BUSINESS_EMAIL_PAGE", "COMPANY_LINKEDIN", "NONE"
}
SOURCE_KINDS = {
    "OFFICIAL_SITE", "OFFICIAL_CONTACT", "OFFICIAL_TEAM", "OFFICIAL_PORTFOLIO",
    "LINKEDIN_COMPANY", "LINKEDIN_FOUNDER", "AGENCY_DIRECTORY", "COMPANY_REGISTRY",
    "OTHER_PUBLIC_PAGE",
}
RETRIEVAL_OUTCOMES = {"SUCCESS", "BLOCKED", "NOT_FOUND", "ERROR"}
SEARCH_HOSTS = {
    "google.com", "www.google.com", "bing.com", "www.bing.com", "search.yahoo.com",
    "duckduckgo.com", "www.duckduckgo.com",
}
DIRECTORY_HOSTS = {
    "linkedin.com", "www.linkedin.com", "clutch.co", "www.clutch.co", "sortlist.com",
    "www.sortlist.com", "designrush.com", "www.designrush.com", "themanifest.com",
    "www.themanifest.com", "facebook.com", "www.facebook.com", "instagram.com",
    "www.instagram.com",
}
TRACKING_KEYS = {"gclid", "fbclid", "msclkid"}
LEGAL_SUFFIXES = {
    "agency", "co", "company", "corp", "corporation", "gmbh", "inc", "incorporated",
    "limited", "llc", "ltd", "plc", "pty",
}
LEAD_FIELDS = {
    "schema_version", "lead_id", "idea_id", "scope_id", "organization_name",
    "organization_key", "website_url", "canonical_domain", "city", "country",
    "working_language", "team_size_min", "team_size_max", "team_size_label",
    "owner_name", "owner_role", "qualification", "claim_source_ids", "contact_channel",
    "contact_url", "contact_source_id", "source_ids", "screening_unknowns", "status",
    "priority", "exclusion_reasons", "duplicate_of", "notes", "last_verified_at",
}
SOURCE_FIELDS = {
    "schema_version", "source_id", "lead_id", "url", "source_kind", "publisher",
    "retrieved_at", "retrieval_outcome", "retrieval_tool", "locator", "exact_fragment",
    "supports", "notes",
}
RUN_STATUS_FIELDS = {
    "schema_version", "idea_id", "scope_id", "phase", "status",
    "target_qualified_leads", "total_leads", "qualified_leads", "hold_leads",
    "excluded_leads", "priority_counts", "source_records", "blockers", "notes",
    "lead_summary_sha256",
}
CSV_FIELDS = (
    "lead_id", "organization_name", "website_url", "canonical_domain", "city", "country",
    "team_size_label", "owner_name", "owner_role", "contact_channel", "contact_url",
    "status", "priority", "screening_unknowns", "source_ids", "notes",
)


class LeadError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise LeadError(message)


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value, f"duplicate JSON property: {key}")
        value[key] = item
    return value


def parse_json(text):
    def reject_constant(value):
        raise LeadError(f"non-finite JSON value: {value}")
    return json.loads(text, object_pairs_hook=unique_object, parse_constant=reject_constant)


def canonical_json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def sha256_file(path):
    return sha256_bytes(Path(path).read_bytes())


def read_json(path):
    path = Path(path)
    require(path.is_file(), f"missing JSON file: {path}")
    try:
        value = parse_json(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError, LeadError) as exc:
        raise LeadError(f"invalid JSON {path}: {exc}") from exc
    require(isinstance(value, dict), f"JSON object required: {path}")
    return value


def read_jsonl(path, label):
    path = Path(path)
    require(path.is_file(), f"missing {label}: {path}")
    rows = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = parse_json(line)
        except (json.JSONDecodeError, LeadError) as exc:
            raise LeadError(f"{label}:{line_number}: {exc}") from exc
        require(isinstance(row, dict), f"{label}:{line_number}: object required")
        rows.append(row)
    return rows


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate_timestamp(value, label):
    require(nonempty(value), f"{label}: timestamp required")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise LeadError(f"{label}: invalid ISO timestamp {value!r}") from exc
    require(parsed.tzinfo is not None, f"{label}: timezone required")
    return parsed


def normalized_url(url):
    require(nonempty(url), "nonempty URL required")
    parts = urlsplit(url)
    require(parts.scheme.lower() in {"http", "https"} and parts.hostname and not parts.username,
            f"public HTTP(S) URL required: {url!r}")
    query = [
        (key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if not key.lower().startswith("utm_") and key.lower() not in TRACKING_KEYS
    ]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"),
                       urlencode(sorted(query)), parts.fragment))


def hostname(url):
    return (urlsplit(normalized_url(url)).hostname or "").lower().removeprefix("www.")


def normalize_organization_name(name):
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii").lower()
    tokens = re.findall(r"[a-z0-9]+", text)
    while len(tokens) > 1 and tokens[-1] in LEGAL_SUFFIXES:
        tokens.pop()
    return "-".join(tokens)


def validate_config(config):
    required = {
        "schema_version", "idea_id", "scope_id", "working_language", "geography",
        "target_qualified_leads", "target_substantive_conversations",
        "max_counted_conversations", "max_new_qualified_per_research_run",
        "max_candidates_examined_per_research_run", "required_confirmed_claims",
        "screening_unknowns_allowed", "screening_disqualifying_contradictions",
        "priority_a_requires", "hard_exclusions", "outreach_authorized",
    }
    require(set(config) == required,
            f"config fields differ: missing={sorted(required - set(config))}, "
            f"unexpected={sorted(set(config) - required)}")
    require(config["schema_version"] == SCHEMA_VERSION, "unsupported config schema_version")
    require(nonempty(config["idea_id"]) and nonempty(config["scope_id"]), "idea/scope required")
    require(config["working_language"] == "English", "this run must use English leads")
    for field in ("target_qualified_leads", "target_substantive_conversations",
                  "max_counted_conversations", "max_new_qualified_per_research_run",
                  "max_candidates_examined_per_research_run"):
        require(type(config[field]) is int and config[field] > 0, f"positive integer required: {field}")
    require(config["target_substantive_conversations"] == 5,
            "Stage 1.5 substantive-conversation target must be 5")
    require(config["max_counted_conversations"] == 8,
            "Stage 1.5 counted-conversation cap must be 8")
    for field in ("required_confirmed_claims", "screening_unknowns_allowed",
                  "screening_disqualifying_contradictions", "priority_a_requires"):
        values = config[field]
        require(isinstance(values, list) and len(values) == len(set(values)),
                f"unique array required: {field}")
        require(set(values) <= set(CLAIMS), f"unknown claim in {field}")
    require(set(config["priority_a_requires"]) <= set(config["screening_unknowns_allowed"]),
            "priority-A claims must be screening claims")
    require(set(config["screening_disqualifying_contradictions"])
            <= set(config["screening_unknowns_allowed"]),
            "disqualifying contradictions must be screening claims")
    require(isinstance(config["hard_exclusions"], list) and config["hard_exclusions"],
            "hard_exclusions required")
    require(config["outreach_authorized"] is False, "lead research must not authorize outreach")


def validate_source(row, config):
    sid = row.get("source_id", "<missing-source-id>")
    require(set(row) == SOURCE_FIELDS,
            f"{sid}: source fields differ: missing={sorted(SOURCE_FIELDS - set(row))}, "
            f"unexpected={sorted(set(row) - SOURCE_FIELDS)}")
    require(row["schema_version"] == SCHEMA_VERSION, f"{sid}: unsupported schema_version")
    require(re.fullmatch(r"mb-src-[0-9]{4}", sid or ""), f"{sid}: invalid source_id")
    require(re.fullmatch(r"mb-lead-[0-9]{3}", row["lead_id"] or ""),
            f"{sid}: invalid lead_id")
    normalized_url(row["url"])
    require(urlsplit(row["url"]).hostname.lower() not in SEARCH_HOSTS,
            f"{sid}: search-result URL cannot be evidence")
    require(row["source_kind"] in SOURCE_KINDS, f"{sid}: invalid source_kind")
    require(nonempty(row["publisher"]), f"{sid}: publisher required")
    validate_timestamp(row["retrieved_at"], sid)
    require(row["retrieval_outcome"] in RETRIEVAL_OUTCOMES, f"{sid}: invalid outcome")
    require(nonempty(row["retrieval_tool"]), f"{sid}: retrieval_tool required")
    forbidden = ("curl", "wget", "requests", "httpx", "scraper", "terminal")
    require(not any(term in row["retrieval_tool"].lower() for term in forbidden),
            f"{sid}: forbidden retrieval tool description")
    supports = row["supports"]
    require(isinstance(supports, list) and len(supports) == len(set(supports)),
            f"{sid}: supports must be a unique array")
    require(set(supports) <= set(CLAIMS), f"{sid}: unknown supports claim")
    if row["retrieval_outcome"] == "SUCCESS":
        require(nonempty(row["locator"]), f"{sid}: SUCCESS requires locator")
        require(nonempty(row["exact_fragment"]), f"{sid}: SUCCESS requires exact_fragment")
        require(len(row["exact_fragment"]) <= 1200, f"{sid}: exact_fragment exceeds 1200 chars")
        require(supports, f"{sid}: successful source must support at least one recorded claim")
    else:
        require(row["exact_fragment"] is None, f"{sid}: unsuccessful source cannot carry fragment")
        require(not supports, f"{sid}: unsuccessful source cannot support qualification")
    require(row["notes"] is None or nonempty(row["notes"]), f"{sid}: invalid notes")


def validate_lead_shape(row, config):
    lid = row.get("lead_id", "<missing-lead-id>")
    require(set(row) == LEAD_FIELDS,
            f"{lid}: lead fields differ: missing={sorted(LEAD_FIELDS - set(row))}, "
            f"unexpected={sorted(set(row) - LEAD_FIELDS)}")
    require(row["schema_version"] == SCHEMA_VERSION, f"{lid}: unsupported schema_version")
    require(re.fullmatch(r"mb-lead-[0-9]{3}", lid or ""), f"{lid}: invalid lead_id")
    require(row["idea_id"] == config["idea_id"], f"{lid}: wrong idea_id")
    require(row["scope_id"] == config["scope_id"], f"{lid}: wrong scope_id")
    require(nonempty(row["organization_name"]), f"{lid}: organization_name required")
    expected_key = normalize_organization_name(row["organization_name"])
    require(row["organization_key"] == expected_key,
            f"{lid}: organization_key must be {expected_key!r}")
    normalized_url(row["website_url"])
    require(re.fullmatch(r"[a-z0-9.-]+", row["canonical_domain"] or ""),
            f"{lid}: invalid canonical_domain")
    site_host = hostname(row["website_url"])
    domain = row["canonical_domain"].lower().removeprefix("www.")
    require(site_host == domain or site_host.endswith("." + domain),
            f"{lid}: website host does not match canonical_domain")
    require(row["city"] is None or nonempty(row["city"]), f"{lid}: invalid city")
    require(row["country"] is None or nonempty(row["country"]), f"{lid}: invalid country")
    require(row["working_language"] in {"English", "UNKNOWN"}, f"{lid}: invalid language")
    for field in ("team_size_min", "team_size_max"):
        require(row[field] is None or (type(row[field]) is int and row[field] > 0),
                f"{lid}: invalid {field}")
    if row["team_size_min"] is not None and row["team_size_max"] is not None:
        require(row["team_size_min"] <= row["team_size_max"], f"{lid}: reversed team range")
    require(row["team_size_label"] is None or nonempty(row["team_size_label"]),
            f"{lid}: invalid team_size_label")
    for field in ("owner_name", "owner_role", "notes"):
        require(row[field] is None or nonempty(row[field]), f"{lid}: invalid {field}")
    qualification = row["qualification"]
    claim_sources = row["claim_source_ids"]
    require(isinstance(qualification, dict) and set(qualification) == set(CLAIMS),
            f"{lid}: qualification must contain every canonical claim exactly once")
    require(set(qualification.values()) <= CLAIM_STATUSES, f"{lid}: invalid claim status")
    require(isinstance(claim_sources, dict) and set(claim_sources) == set(CLAIMS),
            f"{lid}: claim_source_ids must contain every canonical claim exactly once")
    for claim, source_ids in claim_sources.items():
        require(isinstance(source_ids, list) and len(source_ids) == len(set(source_ids)),
                f"{lid}.{claim}: source IDs must be unique array")
        require(all(re.fullmatch(r"mb-src-[0-9]{4}", value or "") for value in source_ids),
                f"{lid}.{claim}: invalid source ID")
        if qualification[claim] == "UNKNOWN":
            require(not source_ids, f"{lid}.{claim}: UNKNOWN cannot cite a supporting source")
        else:
            require(source_ids, f"{lid}.{claim}: {qualification[claim]} requires source")
    require(row["contact_channel"] in CONTACT_CHANNELS, f"{lid}: invalid contact channel")
    if row["contact_channel"] == "NONE":
        require(row["contact_url"] is None and row["contact_source_id"] is None,
                f"{lid}: NONE contact cannot carry a route")
    else:
        normalized_url(row["contact_url"])
        require(re.fullmatch(r"mb-src-[0-9]{4}", row["contact_source_id"] or ""),
                f"{lid}: contact_source_id required")
    require(isinstance(row["source_ids"], list) and len(row["source_ids"]) == len(set(row["source_ids"])),
            f"{lid}: source_ids must be unique array")
    require(all(re.fullmatch(r"mb-src-[0-9]{4}", value or "") for value in row["source_ids"]),
            f"{lid}: invalid source_ids")
    require(isinstance(row["screening_unknowns"], list)
            and len(row["screening_unknowns"]) == len(set(row["screening_unknowns"])),
            f"{lid}: screening_unknowns must be unique array")
    expected_unknowns = sorted(
        claim for claim in config["screening_unknowns_allowed"]
        if qualification[claim] == "UNKNOWN"
    )
    require(sorted(row["screening_unknowns"]) == expected_unknowns,
            f"{lid}: screening_unknowns must equal unresolved allowed claims")
    require(row["status"] in LEAD_STATUSES, f"{lid}: invalid status")
    require(row["priority"] in PRIORITIES, f"{lid}: invalid priority")
    require(isinstance(row["exclusion_reasons"], list)
            and len(row["exclusion_reasons"]) == len(set(row["exclusion_reasons"])),
            f"{lid}: exclusion_reasons must be unique array")
    require(all(nonempty(value) for value in row["exclusion_reasons"]),
            f"{lid}: invalid exclusion reason")
    require(row["duplicate_of"] is None or re.fullmatch(r"mb-lead-[0-9]{3}", row["duplicate_of"]),
            f"{lid}: invalid duplicate_of")
    validate_timestamp(row["last_verified_at"], lid)


def validate_dataset(root, idea, require_final=False):
    base = Path(root) / "ideas" / idea / "stage1.5" / "lead-research"
    config = read_json(base / "config.json")
    validate_config(config)
    require(config["idea_id"] == idea, "--idea does not match config idea_id")
    leads = read_jsonl(base / "leads.jsonl", "leads.jsonl")
    sources = read_jsonl(base / "source-register.jsonl", "source-register.jsonl")

    source_by_id = {}
    sources_by_lead = {}
    seen_source_pages = set()
    for source in sources:
        validate_source(source, config)
        sid = source["source_id"]
        require(sid not in source_by_id, f"duplicate source_id: {sid}")
        source_by_id[sid] = source
        sources_by_lead.setdefault(source["lead_id"], []).append(source)
        page_key = (source["lead_id"], normalized_url(source["url"]))
        require(page_key not in seen_source_pages,
                f"duplicate source page for {source['lead_id']}: {source['url']}")
        seen_source_pages.add(page_key)

    lead_by_id = {}
    active_domains = {}
    active_names = {}
    for lead in leads:
        validate_lead_shape(lead, config)
        lid = lead["lead_id"]
        require(lid not in lead_by_id, f"duplicate lead_id: {lid}")
        lead_by_id[lid] = lead
        owned_sources = sources_by_lead.get(lid, [])
        owned_ids = {source["source_id"] for source in owned_sources}
        require(set(lead["source_ids"]) == owned_ids,
                f"{lid}: source_ids must equal all source-register rows for this lead")
        require(owned_sources, f"{lid}: at least one source row required")
        latest = max(validate_timestamp(source["retrieved_at"], source["source_id"])
                     for source in owned_sources)
        actual_latest = validate_timestamp(lead["last_verified_at"], lid)
        require(actual_latest == latest, f"{lid}: last_verified_at must equal latest source retrieval")

        for claim, source_ids in lead["claim_source_ids"].items():
            for sid in source_ids:
                require(sid in source_by_id, f"{lid}.{claim}: unknown source {sid}")
                source = source_by_id[sid]
                require(source["lead_id"] == lid, f"{lid}.{claim}: cross-lead source {sid}")
                require(source["retrieval_outcome"] == "SUCCESS",
                        f"{lid}.{claim}: non-success source {sid}")
                require(claim in source["supports"], f"{lid}.{claim}: {sid} lacks supports binding")

        status = lead["status"]
        required_claims = config["required_confirmed_claims"]
        if status == "QUALIFIED_FOR_SCREENING":
            missing = [claim for claim in required_claims
                       if lead["qualification"][claim] != "CONFIRMED"]
            require(not missing, f"{lid}: qualified lead has unconfirmed hard claims: {missing}")
            require(lead["working_language"] == "English", f"{lid}: qualified lead must be English")
            require(nonempty(lead["country"]), f"{lid}: qualified lead needs country")
            require(lead["team_size_min"] is not None and lead["team_size_max"] is not None
                    and 2 <= lead["team_size_min"] <= lead["team_size_max"] <= 20,
                    f"{lid}: qualified team range must be wholly within 2..20")
            require(nonempty(lead["owner_name"]) and nonempty(lead["owner_role"]),
                    f"{lid}: qualified lead needs public owner identity")
            require(lead["contact_channel"] != "NONE", f"{lid}: qualified lead needs contact route")
            require(lead["canonical_domain"] not in DIRECTORY_HOSTS,
                    f"{lid}: qualified lead needs an official website, not a directory profile")
            require(not lead["exclusion_reasons"] and lead["duplicate_of"] is None,
                    f"{lid}: qualified lead cannot be excluded/duplicate")
            contradicted_scope = [
                claim for claim in config["screening_disqualifying_contradictions"]
                if lead["qualification"][claim] == "CONTRADICTED"
            ]
            require(not contradicted_scope,
                    f"{lid}: qualified lead has contradicted scope claims: {contradicted_scope}")
            a_ready = all(lead["qualification"][claim] == "CONFIRMED"
                          for claim in config["priority_a_requires"])
            require(lead["priority"] == ("A" if a_ready else "B"),
                    f"{lid}: priority must be derived from priority-A claims")
        elif status == "HOLD":
            require(lead["priority"] == "C", f"{lid}: HOLD priority must be C")
            require(lead["exclusion_reasons"], f"{lid}: HOLD needs concrete reason")
            require(lead["duplicate_of"] is None, f"{lid}: HOLD cannot be duplicate_of")
        else:
            require(lead["priority"] == "NONE", f"{lid}: EXCLUDED priority must be NONE")
            require(lead["exclusion_reasons"], f"{lid}: EXCLUDED needs reason")

        if lead["contact_source_id"] is not None:
            sid = lead["contact_source_id"]
            require(sid in source_by_id and source_by_id[sid]["lead_id"] == lid,
                    f"{lid}: contact source must belong to lead")
            source = source_by_id[sid]
            require(source["retrieval_outcome"] == "SUCCESS"
                    and "PUBLIC_BUSINESS_CONTACT" in source["supports"],
                    f"{lid}: contact source must successfully support contact route")
            require(normalized_url(lead["contact_url"]) == normalized_url(source["url"]),
                    f"{lid}: contact URL must equal its inspected source URL")

        if status != "EXCLUDED":
            domain = lead["canonical_domain"]
            key = lead["organization_key"]
            require(domain not in active_domains,
                    f"duplicate active canonical_domain: {active_domains.get(domain)} and {lid}")
            require(key not in active_names,
                    f"duplicate active organization key: {active_names.get(key)} and {lid}")
            active_domains[domain] = lid
            active_names[key] = lid

    for sid, source in source_by_id.items():
        require(source["lead_id"] in lead_by_id, f"{sid}: orphan source lead_id")
    for lead in leads:
        if lead["duplicate_of"] is not None:
            require(lead["status"] == "EXCLUDED" and "DUPLICATE" in lead["exclusion_reasons"],
                    f"{lead['lead_id']}: duplicate_of requires EXCLUDED + DUPLICATE")
            require(lead["duplicate_of"] in lead_by_id, f"{lead['lead_id']}: unknown duplicate target")
            require(lead_by_id[lead["duplicate_of"]]["status"] != "EXCLUDED",
                    f"{lead['lead_id']}: duplicate target must be retained")

    qualified_count = sum(row["status"] == "QUALIFIED_FOR_SCREENING" for row in leads)
    if require_final:
        require(qualified_count >= config["target_qualified_leads"],
                f"qualified lead target not reached: {qualified_count}/{config['target_qualified_leads']}")
        report_path = base / "lead-research-report.md"
        require(report_path.is_file(), f"missing analytical report: {report_path}")
        report = report_path.read_text(encoding="utf-8")
        require(len(report.strip()) >= 600 and "NOT_STARTED" not in report,
                "analytical report is still a placeholder")
        require("No outreach" in report or "no outreach" in report,
                "report must explicitly state that no outreach occurred")

    return base, config, leads, sources


def make_csv(leads):
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for lead in sorted(leads, key=lambda row: row["lead_id"]):
        writer.writerow({
            "lead_id": lead["lead_id"],
            "organization_name": lead["organization_name"],
            "website_url": lead["website_url"],
            "canonical_domain": lead["canonical_domain"],
            "city": lead["city"] or "",
            "country": lead["country"] or "",
            "team_size_label": lead["team_size_label"] or "",
            "owner_name": lead["owner_name"] or "",
            "owner_role": lead["owner_role"] or "",
            "contact_channel": lead["contact_channel"],
            "contact_url": lead["contact_url"] or "",
            "status": lead["status"],
            "priority": lead["priority"],
            "screening_unknowns": ";".join(sorted(lead["screening_unknowns"])),
            "source_ids": ";".join(sorted(lead["source_ids"])),
            "notes": lead["notes"] or "",
        })
    return output.getvalue().encode("utf-8")


def make_summary(config, leads, sources):
    status_counts = Counter(row["status"] for row in leads)
    qualified = [row for row in leads if row["status"] == "QUALIFIED_FOR_SCREENING"]
    source_outcomes = Counter(row["retrieval_outcome"] for row in sources)
    return {
        "schema_version": SCHEMA_VERSION,
        "idea_id": config["idea_id"],
        "scope_id": config["scope_id"],
        "target_qualified_leads": config["target_qualified_leads"],
        "total_leads": len(leads),
        "status_counts": dict(sorted(status_counts.items())),
        "qualified_leads": len(qualified),
        "priority_counts": dict(sorted(Counter(row["priority"] for row in qualified).items())),
        "country_counts": dict(sorted(Counter(row["country"] for row in qualified).items())),
        "contact_channel_counts": dict(sorted(Counter(row["contact_channel"] for row in qualified).items())),
        "screening_unknown_counts": dict(sorted(Counter(
            claim for row in qualified for claim in row["screening_unknowns"]
        ).items())),
        "source_records": len(sources),
        "source_outcome_counts": dict(sorted(source_outcomes.items())),
        "source_kind_counts": dict(sorted(Counter(row["source_kind"] for row in sources).items())),
        "unique_qualified_domains": len({row["canonical_domain"] for row in qualified}),
        "ready_for_codex_audit": len(qualified) >= config["target_qualified_leads"],
        "outreach_authorized": False,
    }


def write_bytes(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def expected_status(config, summary, base):
    existing = {}
    status_path = base / "run-status.json"
    if status_path.is_file():
        existing = read_json(status_path)
        require(set(existing) == RUN_STATUS_FIELDS,
                f"run-status fields differ: {sorted(set(existing) ^ RUN_STATUS_FIELDS)}")
        require(isinstance(existing["blockers"], list)
                and all(nonempty(value) for value in existing["blockers"]),
                "run-status blockers must be nonempty strings")
        require(existing["notes"] is None or nonempty(existing["notes"]),
                "invalid run-status notes")
    blockers = existing.get("blockers", [])
    if summary["ready_for_codex_audit"]:
        status = "READY_FOR_CODEX_AUDIT"
    elif blockers:
        status = "PARTIAL_BLOCKED"
    else:
        status = "IN_PROGRESS"
    summary_bytes = canonical_json_bytes(summary)
    return {
        "schema_version": SCHEMA_VERSION,
        "idea_id": config["idea_id"],
        "scope_id": config["scope_id"],
        "phase": "LEAD_RESEARCH",
        "status": status,
        "target_qualified_leads": config["target_qualified_leads"],
        "total_leads": summary["total_leads"],
        "qualified_leads": summary["qualified_leads"],
        "hold_leads": summary["status_counts"].get("HOLD", 0),
        "excluded_leads": summary["status_counts"].get("EXCLUDED", 0),
        "priority_counts": summary["priority_counts"],
        "source_records": summary["source_records"],
        "blockers": blockers,
        "notes": existing.get("notes"),
        "lead_summary_sha256": sha256_bytes(summary_bytes),
    }


def checkpoint(root, idea, require_final=False):
    base, config, leads, sources = validate_dataset(root, idea, require_final=require_final)
    csv_bytes = make_csv(leads)
    summary = make_summary(config, leads, sources)
    summary_bytes = canonical_json_bytes(summary)
    status = expected_status(config, summary, base)
    write_bytes(base / "leads.csv", csv_bytes)
    write_bytes(base / "lead-summary.json", summary_bytes)
    write_bytes(base / "run-status.json", canonical_json_bytes(status))
    return base, config, leads, sources, summary, status


def check_generated(root, idea, require_final=False):
    base, config, leads, sources = validate_dataset(root, idea, require_final=require_final)
    expected_csv = make_csv(leads)
    expected_summary = make_summary(config, leads, sources)
    expected_summary_bytes = canonical_json_bytes(expected_summary)
    require((base / "leads.csv").is_file()
            and (base / "leads.csv").read_bytes() == expected_csv,
            "leads.csv is missing or stale; run checkpoint")
    require((base / "lead-summary.json").is_file()
            and (base / "lead-summary.json").read_bytes() == expected_summary_bytes,
            "lead-summary.json is missing or stale; run checkpoint")
    expected_run = expected_status(config, expected_summary, base)
    actual_run = read_json(base / "run-status.json")
    require(actual_run == expected_run, "run-status.json is stale or inconsistent")
    if require_final:
        snapshot_path = base / "snapshot.json"
        require(snapshot_path.is_file(), "final check requires snapshot.json")
        snapshot = read_json(snapshot_path)
        required_snapshot = {
            "schema_version", "snapshot_id", "idea_id", "scope_id", "sealed_at",
            "qualified_leads", "files",
        }
        require(set(snapshot) == required_snapshot, "snapshot fields differ from contract")
        require(snapshot["schema_version"] == SCHEMA_VERSION, "snapshot schema mismatch")
        require(snapshot["idea_id"] == config["idea_id"] and snapshot["scope_id"] == config["scope_id"],
                "snapshot identity mismatch")
        validate_timestamp(snapshot["sealed_at"], "snapshot")
        require(snapshot["qualified_leads"] == expected_summary["qualified_leads"],
                "snapshot qualified total mismatch")
        expected_files = {
            "config.json", "leads.jsonl", "source-register.jsonl", "lead-research-report.md",
            "leads.csv", "lead-summary.json", "run-status.json",
        }
        require(set(snapshot["files"]) == expected_files, "snapshot file set mismatch")
        for filename, expected_hash in snapshot["files"].items():
            require(re.fullmatch(r"[0-9a-f]{64}", expected_hash or ""),
                    f"snapshot invalid hash for {filename}")
            require(sha256_file(base / filename) == expected_hash,
                    f"snapshot hash mismatch: {filename}")
    return base, expected_summary


def seal(root, idea, snapshot_id):
    require(re.fullmatch(r"[a-z0-9][a-z0-9._-]{5,80}", snapshot_id or ""),
            "invalid snapshot ID")
    base, config, _, _, summary, _ = checkpoint(root, idea, require_final=True)
    files = [
        "config.json", "leads.jsonl", "source-register.jsonl", "lead-research-report.md",
        "leads.csv", "lead-summary.json", "run-status.json",
    ]
    snapshot = {
        "schema_version": SCHEMA_VERSION,
        "snapshot_id": snapshot_id,
        "idea_id": config["idea_id"],
        "scope_id": config["scope_id"],
        "sealed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "qualified_leads": summary["qualified_leads"],
        "files": {filename: sha256_file(base / filename) for filename in files},
    }
    write_bytes(base / "snapshot.json", canonical_json_bytes(snapshot))
    return base, summary


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("checkpoint", "check", "seal"))
    parser.add_argument("--idea", required=True)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--require-final", action="store_true")
    parser.add_argument("--snapshot-id")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        if args.command == "checkpoint":
            require(not args.snapshot_id, "checkpoint does not accept --snapshot-id")
            base, _, _, _, summary, status = checkpoint(args.root, args.idea,
                                                        require_final=args.require_final)
            print(f"OK: checkpointed {base}")
            print(json.dumps({"total": summary["total_leads"],
                              "qualified": summary["qualified_leads"],
                              "status": status["status"]}, sort_keys=True))
        elif args.command == "check":
            require(not args.snapshot_id, "check does not accept --snapshot-id")
            _, summary = check_generated(args.root, args.idea, require_final=args.require_final)
            print("OK: Stage 1.5 lead package is structurally consistent")
            print(json.dumps({"total": summary["total_leads"],
                              "qualified": summary["qualified_leads"],
                              "ready_for_codex_audit": summary["ready_for_codex_audit"]},
                             sort_keys=True))
            print("NOTE: this does not verify live sources or authorize outreach")
        else:
            require(args.snapshot_id, "seal requires --snapshot-id")
            base, summary = seal(args.root, args.idea, args.snapshot_id)
            print(f"OK: sealed {args.snapshot_id} in {base / 'snapshot.json'}")
            print(json.dumps({"qualified": summary["qualified_leads"]}, sort_keys=True))
    except (LeadError, OSError, UnicodeError) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
