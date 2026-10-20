#!/usr/bin/env python3
"""Offline integrity checks for this original reading companion.

This checker validates navigation, source locators and metadata consistency.
It cannot establish scientific correctness or external availability.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/0xHayd3n/hive-swarm-fleet-guide"
PDF = "https://somewhere.systems/research/hive-swarm-fleet.pdf"
REQUIRED = (
    "README.md", "AGENTS.md", "LLMS.txt", "ATTRIBUTION.md", "LICENSE",
    "CONTRIBUTING.md", "CITATION.cff", "VERIFICATION.md", "references/paper.bib",
    "metadata/paper.json", "metadata/claims.json", "metadata/sources.json",
    "metadata/classifications.json", "metadata/results.json",
    "docs/01-motivation-and-audit.md", "docs/02-authority-and-taxonomy.md",
    "docs/03-classification-study.md", "docs/04-simulation-results-and-limits.md",
    "docs/05-context-and-source-audit.md", "docs/06-paper-map.md",
    ".github/workflows/validate.yml", "scripts/validate_citation.py",
)
FORBIDDEN_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".zip"}
SKIP = {".git", "__pycache__", ".venv"}
errors: list[str] = []
counts: Counter[str] = Counter()


def check(ok: bool, context: str) -> None:
    if not ok:
        errors.append(context)


def prose_lines(text: str):
    """Ignore fenced examples when checking prose links and headings."""
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield line
    check(fence is None, "Unclosed fenced block")


def heading_ids(text: str) -> set[str]:
    result = set(re.findall(r'<a\b[^>]*(?:id|name)=[\'"]([^\'"]+)', text))
    repeats: Counter[str] = Counter()
    for line in prose_lines(text):
        heading = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?\s*$", line)
        if not heading:
            continue
        title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading[1])
        title = re.sub(r"<[^>]*>", "", title).lower()
        slug = "".join(c for c in title if c in "_- " or unicodedata.category(c)[0] in "LN").replace(" ", "-")
        result.add(slug if repeats[slug] == 0 else f"{slug}-{repeats[slug]}")
        repeats[slug] += 1
    return result


def markdown_targets(text: str):
    """Recognize inline targets, including balanced parentheses in DOI URLs."""
    for match in re.finditer(r"\]\(", text):
        start = match.end()
        if text[start:start + 1] == "<":
            end = text.find(">", start + 1)
            if end != -1:
                yield text[start + 1:end]
            continue
        depth, cursor = 1, start
        while cursor < len(text) and depth:
            char = text[cursor]
            if char == "\\":
                cursor += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            if depth:
                cursor += 1
        if depth == 0:
            yield text[start:cursor].split(' "', 1)[0].strip()


def url_check(url: str, owner: str, current: Path | None = None) -> None:
    parsed = urlsplit(url)
    if parsed.scheme:
        check(parsed.scheme in {"http", "https", "mailto"}, f"{owner}: unsupported URL {url}")
        counts["external_urls"] += 1
        if url.startswith(PDF) and parsed.fragment:
            page = re.fullmatch(r"page=(\d+)", parsed.fragment)
            check(bool(page) and 1 <= int(page[1]) <= 11, f"{owner}: invalid source PDF page {url}")
            counts["source_page_links"] += 1
        return
    if current is None:
        return
    target = (current.parent / unquote(parsed.path)).resolve() if parsed.path else current
    check(target.is_relative_to(ROOT), f"{owner}: local target escapes repository: {url}")
    check(target.is_file(), f"{owner}: missing local target: {url}")
    counts["local_links"] += 1
    if parsed.fragment and target.is_file() and target.is_relative_to(ROOT):
        check(unquote(parsed.fragment) in heading_ids(target.read_text(encoding="utf-8")), f"{owner}: absent anchor: {url}")


def inspect_value(value, context: str) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"page", "pdf_page", "figure_pdf_page"} and isinstance(child, int):
                check(1 <= child <= 11, f"{context}.{key}: source page outside 1-11")
            if key in {"pdf_pages", "pages"} and isinstance(child, list):
                check(all(type(page) is int and 1 <= page <= 11 for page in child), f"{context}.{key}: source pages must be integers in 1-11")
            inspect_value(child, f"{context}.{key}")
        if isinstance(value.get("page"), int) and str(value.get("url", "")).startswith(PDF):
            check(value["url"] == f"{PDF}#page={value['page']}", f"{context}: source page and URL disagree")
    elif isinstance(value, list):
        ids = [v["id"] for v in value if isinstance(v, dict) and "id" in v]
        check(len(ids) == len(set(ids)), f"{context}: duplicate record IDs")
        for index, child in enumerate(value):
            inspect_value(child, f"{context}[{index}]")
    elif isinstance(value, str):
        check(not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", value), f"{context}: decoded JSON contains a control character")
        if value.startswith(("https://", "http://")):
            url_check(value, context)


for required in REQUIRED:
    path = ROOT / required
    check(path.is_file() and path.stat().st_size > 0, f"Required file absent or empty: {required}")

parsed_json = {}
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or SKIP.intersection(path.relative_to(ROOT).parts):
        continue
    name = path.relative_to(ROOT).as_posix()
    counts["files"] += 1
    check(path.suffix.lower() not in FORBIDDEN_SUFFIXES, f"{name}: source or image/archive assets are excluded")
    check(not any(s in name.lower() for s in ("attachment-extracted", "private-source", "bennington-2026-hive-swarm-fleet.pdf")), f"{name}: source extraction must stay private")
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeError:
        errors.append(f"{name}: expected UTF-8 text")
        continue
    check("\ufffd" not in content, f"{name}: Unicode replacement character")
    check(not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", content), f"{name}: unexpected control bytes")
    if path.suffix == ".md" or path.name == "LLMS.txt":
        visible = "\n".join(prose_lines(content))
        for target in markdown_targets(visible):
            url_check(target, name, path)
    if path.suffix == ".json":
        try:
            parsed_json[name] = json.loads(content)
            inspect_value(parsed_json[name], name)
        except (ValueError, TypeError) as exc:
            errors.append(f"{name}: invalid JSON: {exc}")

try:
    paper = parsed_json["metadata/paper.json"]
    check(paper["page_count"] == 11, "paper.json: page_count must be 11")
    check([a.get("name") for a in paper["authors"]] == ["Justin Bennington"], "paper.json: author credit mismatch")
    check(paper.get("version") == "v1", "paper.json: expected version v1")
    check(paper.get("version_date") == "2026-10-17", "paper.json: expected version date 2026-10-17")
    companion = paper["companion"]
    check(companion["repository_url"] == REPO, "paper.json: unexpected repository URL")
    for flag in ("experiments_run", "implementation_reproduced", "paper_pdf_included"):
        check(companion[flag] is False, f"paper.json: {flag} must be false")
    inventory = paper["source_inventory"]
    expected_inventory = {"numbered_sections": 9, "figures": 5, "tables": 2, "numbered_equations": 0, "appendices": 0, "bibliography_entries": 37}
    check(all(inventory.get(key) == value for key, value in expected_inventory.items()), "paper.json: source inventory differs from the studied 11-page v1")
    provenance = paper["provenance"]
    expected_digest = "b1d36d628a4d9c65ec026fc0533a13f9a8300b29067b5b6d5d99348b03bb943e"
    check(provenance["attachment_public_binary_equality_verified"] is True, "paper.json: exact attachment/public comparison must be recorded")
    check(provenance["attachment_size_bytes"] == 377437, "paper.json: attachment byte count differs")
    check(provenance["attachment_sha256"] == provenance["public_pdf_sha256"] == expected_digest, "paper.json: studied attachment/public PDF digest mismatch")
    check(provenance["visual_pdf_pages_checked"] == list(range(1, 12)), "paper.json: complete visual review pages must remain explicit")
    claims = parsed_json["metadata/claims.json"]["claims"]
    check(bool(claims), "claims.json: empty claim list")
    for claim in claims:
        counts["claims"] += 1
        for field in ("id", "kind", "statement", "scope", "caveat", "sources"):
            check(bool(claim.get(field)), f"Claim {claim.get('id')}: missing {field}")
        for source in claim.get("sources", []):
            check(bool(source.get("section")) and isinstance(source.get("page"), int), f"Claim {claim.get('id')}: incomplete source locator")
    sources = parsed_json["metadata/sources.json"]["sources"]
    check(bool(sources) and all(s.get("id") for s in sources), "sources.json: sources require IDs")
    results = parsed_json["metadata/results.json"]
    check(results["reproduced_by_guide"] is False, "results.json: guide has not reproduced experiments")
    check(results["design"]["seeds_per_condition"] == 200 and results["design"]["reported_total_runs"] == 13800, "results.json: preserve reported seed and total-run counts")
    structure_names = {"HIVE", "HIVE-2", "SWARM-CNP", "SWARM-STEAL", "SWARM-ELECT", "FLEET", "FLEET-LATERAL"}
    check({row["structure"] for row in results["table_2"]["means"]} == structure_names, "results.json: Table 2 must contain the seven reported structures")
    check(len(results["table_2"]["means"]) == 7, "results.json: duplicate Table 2 structures")
    expected_table = {
        "HIVE": [1.18, 2.01, 0.023, 14.0, 28.7],
        "HIVE-2": [1.34, 4.02, 0.026, 14.7, 29.1],
        "SWARM-CNP": [1.41, 30.9, 0.997, 1.43, 76.3],
        "SWARM-STEAL": [1.53, 6.32, 0.995, 1.56, 29.2],
        "SWARM-ELECT": [1.21, 2.02, 0.996, 1.27, 28.7],
        "FLEET": [1.81, 3.06, 0.941, 2.21, 30.7],
        "FLEET-LATERAL": [1.53, 3.28, 0.959, 1.79, 28.3],
    }
    for row in results["table_2"]["means"]:
        actual = [row[field] for field in ("base_sojourn", "messages_per_task", "retention", "sojourn_loss", "makespan")]
        check(actual == expected_table.get(row["structure"]), f"results.json: reported Table 2 values differ for {row['structure']}")
    verdicts = {row["id"]: row["author_verdict"] for row in results["hypotheses"]}
    check(verdicts == {"H1": "holds", "H2": "mixed", "H3": "mixed", "H4": "mixed", "H5": "mixed", "H6": "holds"}, "results.json: preserve H1-H6 author verdicts")
    h3 = next(row for row in results["hypotheses"] if row["id"] == "H3")
    check(h3["reported"]["elected_retention"]["ci_95"] == [0.988, 1.003], "results.json: do not clip the reported elected-retention interval at one")
    classifications = parsed_json["metadata/classifications.json"]
    rows = classifications["classifications"]
    check(len(rows) == 22 and sorted(row["row"] for row in rows) == list(range(1, 23)), "classifications.json: require each source row 1-22 exactly once")
    verdict_counts = dict(Counter(row["initial_verdict"] for row in rows))
    check(verdict_counts == classifications["counts"] == {"agree": 12, "misclassified": 3, "undecidable": 7}, "classifications.json: preserve initial-taxonomy comparison counts 12/3/7")
    bib = (ROOT / "references/paper.bib").read_text(encoding="utf-8")
    check("Bennington, Justin" in bib and "2026" in bib and "v1" in bib, "BibTeX: incomplete paper identity")
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    for token in ("cff-version: 1.2.0", "preferred-citation:", "Bennington", "Justin", "2026-10-17", "v1", REPO):
        check(token in cff, f"CITATION.cff: expected {token!r}")
except (KeyError, TypeError, OSError) as exc:
    errors.append(f"Metadata consistency check could not complete: {exc}")

if errors:
    print("\n".join(f"ERROR: {item}" for item in errors))
    sys.exit(1)
print("PASS: " + ", ".join(f"{key}={value}" for key, value in sorted(counts.items())))
print("Offline scope: required files, UTF-8, local links/anchors, JSON and citation identity, source pages, excluded source assets.")
print("Separate checks cover CFF schema, anonymous access, published bytes and research/source review.")
