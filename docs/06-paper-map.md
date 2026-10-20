# Complete paper map

[Guide home](../README.md)

This map covers the entire **11-page Working paper v1, 17 October 2026** by **Justin Bennington, Somewhere Systems**. PDF positions and printed pages both run from 1 to 11. The [official PDF](https://somewhere.systems/research/hive-swarm-fleet.pdf) is byte-for-byte identical to the supplied attachment. This guide supplies original explanation, not a replacement copy of the paper.

## Sections and end matter

| Source span | PDF pages | What is there | Guide route |
| --- | --- | --- | --- |
| Title, subtitle, author, affiliation, status, abstract | [1](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=1) | Scope and headline taxonomy/simulation results | [README](../README.md) |
| §1 Introduction and contributions | [1](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=1) | Motivation and testing the author's own initial proposal | [Motivation](01-motivation-and-audit.md) |
| §2 Initial taxonomy | [1–2](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=1) | Original hive, swarm, fleet; four edge cases; governance refinement | [Audit](01-motivation-and-audit.md) |
| §3 Audit | [2](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=2) | D1–D8 and three retained ideas | [Audit](01-motivation-and-audit.md) |
| §4.1 Three relations and a digraph | [2–3](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=2) | Execution, governance, lifecycle, communication; origin and revocation of authority | [Definitions](02-authority-and-taxonomy.md) |
| §4.2 Types | [3](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=3) | Hive, swarm, partition, matrix, four fleet conditions, intervals | [Types](02-authority-and-taxonomy.md) |
| §4.3 Axes and their independence | [3–4](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=3) | Four axes and counterexamples establishing logical separability | [Axes](02-authority-and-taxonomy.md) |
| §5 Related work | [4–5](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=4) | Organisational paradigms, holons, stigmergy, markets, blackboards, temporary leaders, military and LLM systems | [Context and audit](05-context-and-source-audit.md) |
| §6 Classification study | [5–6](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=5) | Table 1, 12/3/7 comparison, selected observations | [Classification](03-classification-study.md) |
| §7.1 Design | [6](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=6) | Seven simulated structures, shared randomness, failures, seeds, uncertainty | [Simulation](04-simulation-results-and-limits.md) |
| §7.2 Results | [6–8](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=6) | Table 2; H1–H6; unregistered latency and burst findings | [Results](04-simulation-results-and-limits.md) |
| §8 Discussion | [8–9](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=8) | Command outage, spare capacity, message expense, lifecycle interpretation | [Results and limits](04-simulation-results-and-limits.md) |
| §9 Limitations and status | [9](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=9) | Model exclusions, classification limitations, logical independence, future trace inference | [Results and limits](04-simulation-results-and-limits.md) |
| Data and code | [10](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=10) | Author-offered hsf package, 13,800 runs, preregistration, deviations and evidence; reproduction commands | [Source audit](05-context-and-source-audit.md) |
| Acknowledgements | [10](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=10) | Author's original taxonomy and AI coding-agent assistance under his direction | [Attribution](../ATTRIBUTION.md) |
| References | [10–11](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=10) | 37 bibliographic entries | [Reference register](../references/reading-list.md) |

There are **no appendices, supplementary pages, numbered equations, or footnotes** in this supplied PDF. Artifacts named by the text are not embedded appendices.

## Figures and tables

| Item | Page | Content and reading caution |
| --- | --- | --- |
| Figure 1 | [4](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=4) | Four authority schematics: depth-2 hive, governed fleet, governed swarm, partition. Black solid execution arrows, orange dashed governance, blue dotted communication. A conceptual diagram, not data. |
| Table 1 | [5](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=5) | All 22 configurations, repaired command locus, lifecycle, and initial-rule verdict. Communication/ownership evidence is deferred to unavailable CLASSIFICATION.md. |
| Table 2 | [6](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=6) | Seven simulation rows; sojourn, messages/task, outage retention, loss-scenario sojourn, and burst makespan. Shared reported base throughput 11.69. |
| Figure 2 | [7](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=7) | Time trace around 150–200 coordinator outage; 2-unit bins, 200-seed means and 95% mean intervals. Hive drains its buffer, then builds and clears backlog. |
| Figure 3a / 3b | [8](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=8) | Dot plots of outage retention and messages/task; the latter uses a log axis. These are not the team-size and latency panels. |
| Figure 4a / 4b | [8](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=8) | Team-size message scaling; sojourn against one-way message latency, log vertical scale. Solid load 0.7, dashed load 0.9. |
| Figure 5 | [9](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=9) | Makespan of a 400-task initial burst with 95% intervals. Contract net's long bar differs from its good outage retention. |

Every figure/table page was visually inspected in the actual attachment. Figures are described, not redistributed or traced.

## Mathematical statements and notation

The paper uses inline and displayed mathematical definitions without equation numbers. This index covers their roles rather than inventing source equation labels.

| Location | Objects / statement | What to keep straight |
| --- | --- | --- |
| §1–2, pp.1–2 | Agent universe A; command relation R; initial H=(c,W,R_H), S=(W,G_S,P), F=(N,U,R_F,α) | These are the audited starting definitions, not the final answer. G_S is the initial swarm coordination graph. |
| §2, p.2 | Original negated universal-command condition; R_F between nodes; α supervision; governed-swarm relation and R-positive-closure exclusion | The weak negated condition allows several permanent roots. The positive closure means indirect reach, not just direct edges. |
| §4.1, pp.2–3 | Time-indexed E_t, G_t, L_t; C_t; unit W subset of A | Execution binds individual work, governance binds a unit's mandate, lifecycle controls process existence, communication indicates a messaging path. |
| §4.1, p.3 | Derived, conferred, member-revocable authority; filtered D_t(W) | An edge is excluded only when conferred, member-revocable **and** term-bounded. Runtime E can contain authority missing from D. |
| §4.2, p.3 | Unique root and reachability; execution transitive closure E_t^+; depth | Hive criterion follows paths. The text also invokes flowgraph domination; cycles and entry conventions are not developed into a complete general graph specification. |
| §4.2, p.3 | Swarm edgelessness over an interval; partition/matrix; fleet | Fleet requires at least two nodes and units, disjoint units, node/unit coverage, execution boundary and connected coordination. |
| §4.3, pp.3–4 | Axis values from D, C, G, L | Counterexamples establish logical separability, not statistical independence. |
| §6, p.6 | E empty between cloudsound nodes | Author's interpretation of that configuration, not absence of all within-node delegation. |
| §7, pp.6–8 | n, δ, σ; rates, load, paired differences, bootstrap CIs; extra-hop comparison 2δ=0.10 | Simulation parameters and descriptive/statistical quantities, not a language-model cost equation. |

## Source discrepancies to retain

The simulation module records the full issues. H2's team-size discussion points to Figure 3a although Figure 4a shows that plot. H5's latency discussion points to Figure 3b although Figure 4b shows it. The burst paragraph points to Figure 4 although Figure 5 plots makespan. The guide identifies the displayed plot while preserving the author's original reference.

Abstract rounding (fleet 0.94 versus Table 2's 0.941; ratio 15.4 versus 15.38; slope 1.95 versus 1.946) is not a contradictory experiment. Confidence intervals for retention ratios can cross 1. A fleet expected to retain 0.6–0.9 instead retains 0.941: the stated hypothesis bound fails in a favourable direction. A tiny nonzero hive message slope still fails the registered zero-containing-interval rule. See [reported results](../metadata/results.json).

