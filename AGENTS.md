# Instructions for reading and maintaining this guide

This is an independent guide to Justin Bennington's **Hive, Swarm, Fleet**, Working paper **v1, 17 October 2026**, Somewhere Systems. Read [README.md](README.md), [paper metadata](metadata/paper.json), and the [paper map](docs/06-paper-map.md) first.

## Source hierarchy

Use the supplied attachment/public PDF with SHA-256 `b1d36d628a4d9c65ec026fc0533a13f9a8300b29067b5b6d5d99348b03bb943e` as primary. [Official source](https://somewhere.systems/research/hive-swarm-fleet.pdf). Its one-based PDF pages equal printed pages 1–11. Attribute the research to **Justin Bennington**, not the guide maintainer or AI assistant.

The author page identifies the version and paper license. The guide's pinned code inspections are present-day snapshots, not the unreleased hsf package or necessarily the versions behind the paper. The [reference register](references/reading-list.md) identifies all 37 source bibliography entries; it does not certify independent reading of each one.

## Evidence discipline

- Separate **proposed definitions**, **logical counterexamples**, **author classifications**, **reported simulation**, **cited background**, and **guide interpretation**.
- E is execution, G governance, L lifecycle, C communication. The filtered D graph differs from E. Qualifying leader authority requires conferred, member-revocable **and** term-bounded conditions.
- Hive/fleet labels describe authority at a stated level and interval. Do not infer command from message routing, hardware count, a product name, or absent observed messages.
- Do not generalise 22 documentation-based cases into every deployment of a framework.
- Do not turn simulated retention into reliability probabilities or measured LLM robustness. The model excludes reasoning errors and deliberation cost.
- H1/H6 hold as reported; H2–H5 are mixed. Preserve unexpected results, reported precision, failed bounds, and the SWARM-ELECT CI upper bound 1.003.
- Preserve figure-reference discrepancies: H2→printed Fig.3a/displayed Fig.4a; H5→printed Fig.3b/displayed Fig.4b; burst→printed Fig.4/displayed Fig.5.
- hsf, raw runs, preregistration/deviations and full classification evidence were not obtained. Never say experiments reproduced, registration verified, or full code/data audited unless that work is later actually completed and documented.
- Treat novel graph questions, singleton conventions and code-as-root concerns as guide interpretation, not author errata.

## Navigation

[Audit](docs/01-motivation-and-audit.md) · [Definitions](docs/02-authority-and-taxonomy.md) · [Classification](docs/03-classification-study.md) · [Simulation](docs/04-simulation-results-and-limits.md) · [Source audit](docs/05-context-and-source-audit.md) · [Complete map](docs/06-paper-map.md).

Machine indexes: [claims](metadata/claims.json), [results](metadata/results.json), [classifications](metadata/classifications.json), [sources](metadata/sources.json). Each is an explanatory index, not a substitute for the source.

## Editing and verification

Keep all factual changes source-linked by section and page; update the human module and affected metadata together. New interpretation must be labelled. Do not add the source PDF, full extracted paper, original figure images, credentials, private Library transfer metadata, or local scratch files. Preserve author credit and license boundaries. Do not overwrite a later paper version into the v1 guide without explicitly revising its scope.

Run `python scripts/validate_repository.py` after changes. Validate CITATION.cff against the official CFF 1.2.0 schema when editing it. Record checks and their limits in [VERIFICATION.md](VERIFICATION.md). These instructions authorize ordinary local maintenance; external publication follows the user's actual task authorization.

