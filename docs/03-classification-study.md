# Reading the classification study

[Guide home](../README.md) · [Authority definitions](02-authority-and-taxonomy.md) · [Simulation](04-simulation-results-and-limits.md)

The 22 rows in §6 are **Bennington's classifications of documented configurations**. They are not 22 measured production deployments or a benchmark of task quality. The input is documentation, papers, and the author's own source files. The complete evidence table, `CLASSIFICATION.md`, is described but not distributed with the PDF. See [source audit](05-context-and-source-audit.md).

Sources: [§6, PDF pp.5–6](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=5); qualifications in [§9, p.9](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=9).

## What the comparison measures

The initial taxonomy matches the repair for 12 rows, gives a wrong label for 3, and leaves 7 undecidable or contradictory. That is an internal comparison between the author's initial rule and revised rule, applied to the author's selected cases. It does not independently establish that the revised rule captures every organisation.

“Source” in Table 1 means the **initial taxonomy's verdict**, not a bibliographic source column. A cross marks a mismatch; a question mark marks ambiguity. The following is an original reading index of every row, with the author's classifications paraphrased.

| Row | Configuration studied | Author's repaired interpretation | Initial taxonomy outcome | What to inspect |
| --- | --- | --- | --- | --- |
| 1 | Hermes parent with at most four delegated children | One-level hive | Agreement | Children follow the parent's task decisions; their lifetime follows the session. |
| 2 | Persistent cloudsound workstreams with an integrator | Fleet of singleton nodes; acceptance sits with the integrator | Undecidable | Path ownership, acceptance, and launchd restarts perform different jobs. |
| 3 | Four DGX Sparks assigned static roles | Hardware arrangement, without an agent organisation established | Mismatch: fleet | Delegation capacity or machine count does not establish actual authority. |
| 4 | Anthropic research orchestrator and workers | One-level hive | Agreement | Lead agent dispatches research. |
| 5 | Claude Code with subagents | One-level hive | Agreement | Parent/subagent roles in the documented configuration. |
| 6 | AutoGen group conversation | Hive with speaker-selecting manager | Agreement | The chosen speaker policy matters; the label does not cover every AutoGen program. |
| 7 | CAMEL role-play pair | Two-member hive | Agreement | A pair can have binding asymmetric roles. |
| 8 | MetaGPT under its fixed operating procedure | Leaderless swarm | Agreement | The author treats shared procedure as coordination without an original internal commander. |
| 9 | ChatDev fixed conversation chain | Successive two-member hives | Undecidable | A run changes active pair; forcing one static label hides temporal structure. |
| 10 | CrewAI sequential orchestration | Hive whose root is orchestration code | Mismatch: swarm | Scheduling can impose command even without a conversational manager agent. |
| 11 | CrewAI hierarchical process | One-level hive | Agreement | Manager allocates work. |
| 12 | Nested LangGraph supervisors | Hive with at least two command levels | Undecidable | A superior that can bind subordinate allocation yields continuing execution command. |
| 13 | LangGraph swarm with handoffs | Leaderless handoff swarm | Agreement | Control transfer does not imply parallel independent execution. |
| 14 | Agents SDK agents used as tools | One-level hive | Agreement | Calling agent selects the delegated work. |
| 15 | OpenAI Swarm handoffs | Leaderless handoff swarm | Agreement | A handoff transfers control; runtime details remain configuration dependent. |
| 16 | Contract-net allocation | Leaderless swarm | Agreement | Per-task bids and accepted contracts differ from permanent original command. |
| 17 | Hearsay-II | Hive rooted at its scheduler | Mismatch: swarm | A shared blackboard does not remove a scheduler's authority. |
| 18 | Ant colony / ant-colony optimisation | Leaderless swarm | Agreement | Shared environment coordinates activity. |
| 19 | Raft cluster | Elected swarm | Undecidable | The repair filters qualifying revocable leader edges from the command digraph. |
| 20 | PROSA holons | Swarm with an advisory hub | Undecidable | Advice does not bind a subordinate's execution. |
| 21 | Army under detailed command | Hive spanning the command echelons | Undecidable | Doctrine is the evidence, rather than measured field practice. |
| 22 | Army under mission command | Fleet composed of fleets | Undecidable | Intent crosses unit boundaries while subordinate execution remains local. |

The separate [classification index](../metadata/classifications.json) preserves the row numbers, verdict counts, and the boundary of the evidence.

## Three observations and their limits

Bennington observes that the production LLM architectures **in this selection that publish their architecture** are one-level hives; that named swarm frameworks often implement serial handoff; and that his own persistent-agent system is the only fleet among these LLM cases. Read the qualifiers. This does not show that all production LLM systems are hives or that no other fleet exists. The sampling procedure, configuration diversity, and independent raters are not supplied as a systematic population study. [§6, p.6](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=6)

The cloudsound example is useful because one activity would otherwise be misread as another. An integrator accepting a contribution belongs to governance. An agent choosing another agent's next task would be execution command. launchd restarting a process belongs to lifecycle. The same node can also create a local delegated hive without changing the fleet's boundary.

## A useful classification exercise

Choose a specific deployed configuration and a time interval. Record:

1. A decision that each actor can impose on another actor without agreement.
2. Which roles are established and revoked by the members' protocol, including their terms.
3. Who sets each unit's deliverable, budget, acceptance rule, and termination.
4. Who starts and restarts the processes.
5. Which member sets overlap and which nodes are connected.

Only then apply the definitions. Logs of messages alone may not reveal who could refuse a request. A missing observed command is not proof that command authority is absent. These are guide recommendations, not an implemented trace classifier.

## Cases to discuss critically

**Code as commander.** Row 10 roots a hive in orchestration code, while §4 initially takes vertices to be agents. It is sensible to ask how non-agent policy components enter the formal universe. The paper separately allows humans and supervisors in lifecycle control, but does not fully specify this expansion for every execution root.

**Singleton nodes.** Row 2 uses singleton fleet nodes, and §6 says they can root delegated hives. The hive definition speaks of a root with outgoing edges, which a singleton lacks. Record the level and period of analysis; do not silently invent a singleton convention.

**Contract versus command.** A voluntarily accepted task may later create obligations. The repair separates original command from conferred, member-revocable, term-bounded authority. Applying these tests to each contract implementation needs more evidence than the framework name.

**Leader election.** The paper classifies Raft as an elected swarm, not as a claim that Raft has no operational leader. Whether a concrete election protocol satisfies all three filters must be checked, rather than assumed from the word “elected.”

These are interpretive questions raised by applying the definitions, not author-issued corrections. The [source audit](05-context-and-source-audit.md) checks selected accessible primary material and explains why it is not an independent recoding of all 22 cases.

