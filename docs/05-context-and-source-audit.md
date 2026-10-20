# Context and source audit

[Back to the reading guide](../README.md)

The taxonomy is an argument about authority. Its connection to existing organisational ideas and its simulation results are useful, but they answer different questions. This module separates the paper's intellectual context, the primary sources inspected for this guide, and the evidence still needed.

## Where the proposal sits

In [§5, PDF pp.4-5](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=4), Justin Bennington relates the repaired categories to older work:

| Research tradition | What it helps a reader notice | Caution |
| --- | --- | --- |
| Organisational paradigms: Horling and Lesser | Hierarchies, federations, markets and matrix organisations already form a broad design space. | The contribution claimed here is an authority-graph test, not the invention of organisational diversity. |
| Holons and holonic manufacturing: Koestler; Van Brussel and colleagues; Fischer and colleagues; Giret and Botti | A unit can exercise local autonomy while participating in a larger organisation. Advisory staff need not command operational units. | A nested diagram alone does not establish where execution authority ends. |
| Stigmergy and swarm intelligence: Grassé; Theraulaz and Bonabeau; Bonabeau, Dorigo and Theraulaz; Dorigo, Maniezzo and Colorni | Agents can coordinate through a shared environment. | A common medium can still be a single infrastructure dependency. |
| Markets and blackboards: Smith; Erman and colleagues; Lesser and Corkill | A task contract, a shared board, and a scheduler are distinct mechanisms. | A blackboard does not automatically make its surrounding system leaderless. |
| Temporary leaders: Lamport; Ongaro and Ousterhout | Leadership can be conferred and removable through a protocol. | The author's elected-swarm classification is a taxonomy choice; an election protocol does not eliminate every failure mode. |
| Military command: Army doctrine; Alberts and Hayes | Mandates and local allocation can be separated across echelons. | The military rows use doctrine, not observations of actual operations. |

The LLM literature in §5 includes conversation frameworks, software teams, collaboration graphs, communication surveys, topology learning and failure analysis. These works supply context for the author's distinctions. The paper's claim that earlier classifications do not separate all three authority relations should be read as its literature assessment, rather than an independently exhaustive review by this guide.

## Exact source provenance

The source studied is the user-supplied **Working paper v1, 17 October 2026**, by **Justin Bennington, Somewhere Systems, New York, NY**, with 11 PDF pages. The entire attachment was read.

On **20 October 2026**, the [author's paper page](https://somewhere.systems/research/hive-swarm-fleet) and [official public PDF](https://somewhere.systems/research/hive-swarm-fleet.pdf) were located. The downloaded public PDF and the Library attachment are byte-identical:

- Size: **377,437 bytes**.
- SHA-256: `b1d36d628a4d9c65ec026fc0533a13f9a8300b29067b5b6d5d99348b03bb943e`.

Public PDF page links therefore point to the same bytes as the studied attachment. The public URL is not version-addressed; use the date, working-paper version and hash to detect later replacement. The author's landing page states **CC BY 4.0**. This guide links to the paper and publishes original explanatory material; it does not redistribute the PDF or the paper's figures.

## What could be audited

The audit below is a **static reading of accessible source and documentation**, completed on 20 October 2026. It is a limited check of mechanisms relevant to selected Table 1 rows. No framework was installed or executed, no deployed system was instrumented, and none of the paper's experiments was reproduced.

| Source inspected | Observation relevant to the paper | What remains unproved |
| --- | --- | --- |
| [OpenAI Swarm core.py, commit 6af0b4c](https://github.com/openai/swarm/blob/6af0b4caf37dca4526dfd98e9fbd8ce36e7eeb22/swarm/core.py) | The run loop holds one active agent, obtains its completion, handles tools, and replaces the active agent when a tool result supplies another agent. This supports the handoff description used for Table 1 row 15. | It does not demonstrate parallel leaderless execution, crash resilience, or a universal classification of applications built with Swarm. Its [README](https://github.com/openai/swarm) now directs production users to the Agents SDK. |
| [LangGraph Swarm swarm.py, commit 5442a15](https://github.com/langchain-ai/langgraph-swarm-py/blob/5442a15cdd0ed210589148900c9960c24c489d04/langgraph_swarm/swarm.py) | The graph stores an active-agent field, routes entry to that agent, and obtains destinations from handoff tools. This is consistent with row 13's handoff mechanism. | The file does not establish the authority semantics of every custom tool, agent or surrounding application. |
| [LangGraph Supervisor supervisor.py, commit 88859b3](https://github.com/langchain-ai/langgraph-supervisor-py/blob/88859b34017ac3569bbd4a3092c7e77593a0a960/langgraph_supervisor/supervisor.py) | A supervisor is added at entry, receives agent outputs, and has handoff tools to managed agents. Its [README](https://github.com/langchain-ai/langgraph-supervisor-py) also demonstrates supervisors managing compiled teams. This supports the central and nested delegation patterns underlying row 12. | Control-flow edges alone do not settle whether a particular application treats a request as binding execution command or as governance of an autonomous unit. |
| [CrewAI process documentation, v1.15.28](https://docs.crewai.com/v1.15.28/en/concepts/processes) | The sequential process follows a predefined task order; the hierarchical process uses a manager for allocation and review. These descriptions support the operational distinction discussed around rows 10-11. | They do not independently establish an authority graph for every deployment or prove the author's proposed classifications. |
| [Anthropic's research-system account](https://www.anthropic.com/engineering/multi-agent-research-system) | The account describes a lead agent decomposing a query, assigning subtasks and synthesising subagent results. That is compatible with the orchestrator-worker pattern used for row 4. | This is the provider's architectural account, not an independent audit of its production behaviour or an evaluation of the present taxonomy. |

The pinned code commits are **inspection snapshots**, not a claim that the paper used those commits. Documentation can change. The paper cites `langchain-ai/langgraph-supervisor`; that URL redirected to `langchain-ai/langgraph-supervisor-py` during this audit. The direct connector could not fetch the old name, while the redirected public repository and its source were readable.

## Code, data and pre-registration limits

[Data and code, PDF p.10](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=10) describes an `hsf` package, results from **13,800 simulation runs**, a pre-registration, deviation log, classification evidence and initial definitions. It names commands for experiments and analysis. Naming those commands is not enough to run them without the package and its inputs.

The author page says the supporting package and records are available **from the author**. It supplies no direct package, dataset, pre-registration or classification-evidence download link. Four GitHub repository searches, scoped to `somewheresy` and `somewheresystems` with `hsf` and `hive`, returned no matches. This search result does not prove that no public copy exists elsewhere.

Consequently, this guide could not independently:

- Inspect the `hsf` classifier, simulator, tests, seed grid or analysis implementation.
- Verify that the pre-registration commit preceded the full run, or inspect the six clarifications and process slip in the deviation log.
- Recompute confidence intervals, reconcile totals from per-run records, or trace rounded table entries to raw data.
- Inspect `CLASSIFICATION.md`, the author's cloudsound source files, or the archived starting conversation.

The report that pre-registration preceded the grid, and the reported simulation results, are **the author's statements**. The guide preserves their stated status while marking the supporting records unavailable to this audit. We did not contact the author.

## How to use the classifications responsibly

Table 1 is the author's application of his repaired definitions to selected configurations. A framework can support several architectures. A product name, a communication graph or a library's default example is not a measurement of every deployment made with it.

A defensible new classification needs a stated unit boundary and time interval; evidence for who can bind an individual's task allocation; evidence for who sets unit mandates; the origin and removal rules for temporary authority; and lifecycle dependencies. It should also record shared infrastructure separately. An outage of a shared database, message board or model service can defeat a system with no permanent command root.

The paper itself limits the classification to documentation and, for military examples, doctrine ([§9, p.9](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=9)). The 12/3/7 agreement split compares the author's initial and repaired taxonomies. It is not an accuracy score against independently labelled ground truth.

## What a stronger follow-up would test

The following are **guide proposals**, not experiments reported by Bennington:

1. Release the exact classifier inputs, full simulation grid, seeds, code version and registration history; rerun the published commands before assessing replication.
2. Vary the failure being compared: a single ordinary worker, the command component, a shared service, and correlated failures. Report failed capacity as well as organisational role.
3. Test fleet re-routing both with spare capacity and near saturation. The paper's favourable four-node result depends on remaining capacity being sufficient.
4. Replace abstract service times with measured LLM work, including coordinator deliberation, token sizes, reasoning mistakes, mandate misunderstandings, verification and task quality.
5. Check whether traces plus permission and protocol specifications can recover authority relations. A message trace alone usually cannot tell whether a recipient could refuse.

These steps would connect the taxonomy to observable behaviour without treating the current model's throughput ratios as guarantees for real agent teams.

