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

Publication checks pending the initial public push. This line is replaced with verified outcomes before completion.
