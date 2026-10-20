# Verification and evidence boundaries

Prepared 20 October 2026. This record distinguishes source review, repository checks and experiment reproduction.

## Source review

- Read all 580 extracted lines covering the supplied 11-page attachment, including the complete references and end matter.
- Rendered and visually inspected all 11 actual attachment pages, including five figures, two tables and mathematical definition spans. There are no appendices or numbered equations.
- Compared the attachment with the author's official public PDF: both are 377,437 bytes, SHA-256 `b1d36d628a4d9c65ec026fc0533a13f9a8300b29067b5b6d5d99348b03bb943e`.
- Confirmed title, single author Justin Bennington / Somewhere Systems, cover status Working paper v1 dated 17 October 2026, and CC BY 4.0 on the author page.
- Indexed all 22 Table 1 cases, seven Table 2 rows, H1–H6, five figures, two tables, all sections and 37 bibliography entries. Preserved three mistaken figure references, partial hypothesis outcomes, ratios and rounding distinctions.
- Statically inspected three public framework source files at commit and blob pins, plus selected provider documents; see [source audit](docs/05-context-and-source-audit.md) and [audit notes](metadata/source-audit-notes.json).

## Research limits

The hsf implementation, 13,800 raw runs, preregistration, deviation log and full classification evidence were not obtained. The author page offers them from the author without a direct download. No hsf commands were run; no experiments or figures were reproduced. Registration timing, complete parameter grid and each raw number are not independently verified. No framework deployment was executed or every classification independently recoded. The full bibliography is indexed, not independently audited publication by publication.

## Repository checks

`python scripts/validate_repository.py` validates required files, UTF-8, relative links and anchors, source page ranges, JSON structure and domain invariants, citation identity and excluded source assets.

`python scripts/validate_citation.py --download-schema` validates CITATION.cff against the official CFF 1.2.0 schema, pinned by SHA-256. Offline use is available with `--schema PATH`. The schema validator needs PyYAML and jsonschema; the repository integrity validator uses only the Python standard library. The read-only CI runs both checks.

Publication verification is recorded below after the exact final tree is pushed. Scientific validity and external source permanence are outside these checks.

## Publication record

The repository was published publicly as [0xHayd3n/hive-swarm-fleet-guide](https://github.com/0xHayd3n/hive-swarm-fleet-guide) on 20 October 2026. Duplicate searches for hive, swarm, fleet and Bennington under the owner returned no existing guide; the exact chosen name was also checked before creation.

For initial publication commit `6f6ac63120a95812c25f79ecf3467f4b605204ce`:

- Anonymous GitHub repository API request returned HTTP 200, `private=false`, and default branch `main`; its public branch reference matched the local commit.
- An unauthenticated commit archive contained exactly the 27 expected tracked files. Every published file matched its local committed blob byte-for-byte. The anonymous raw README request also returned HTTP 200 with identical bytes.
- Local integrity checks passed: 27 files, 15 claims, 76 local links, 101 source-page links, classification 12/3/7 counts, all Table 2 values and hypothesis verdicts, author/version/hash identity and source-asset exclusions.
- CITATION.cff passed the official SHA-256-pinned CFF 1.2.0 schema locally and in CI.
- [GitHub Actions run 39429919284](https://github.com/0xHayd3n/hive-swarm-fleet-guide/actions/runs/39429919284) completed successfully, including both validation scripts.

This verification-record update is committed separately. The release procedure repeats anonymous branch/archive/content comparisons and checks CI for the final pushed revision. The final commit is reported with delivery; [current workflow history](https://github.com/0xHayd3n/hive-swarm-fleet-guide/actions/workflows/validate.yml) remains publicly inspectable. No source PDF, original figure, full extracted text, private Library identifier or transfer credential is tracked.
