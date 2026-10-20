# 1. Why repair the vocabulary?

Justin Bennington's *Hive, Swarm, Fleet* begins by testing his own earlier definitions. The target is a vocabulary problem with practical consequences: an architecture name can suggest resilience, autonomy, or scalability without specifying who can actually bind another agent's work. The paper's repair is a proposal for making those claims inspectable. It is not a finding that these three words exhaust every possible organisation. [§§1-2, PDF pp.1-2](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=1)

This module and the [authority module](02-authority-and-taxonomy.md) explain Working paper v1, dated 17 October 2026. The research and taxonomy are Bennington's, Somewhere Systems; the examples and explanations here are an independent reading companion.

## A useful starting question

Imagine five agents working in one repository. Their messages all pass through the same service. That fact does not establish whether the service dispatches their tasks, merely carries messages, accepts their final work, or restarts crashed processes. Those are different powers. To classify the system, inspect what decisions are binding, who grants that authority, and how it can be withdrawn.

This is why counting machines, counting possible delegation tools, or drawing a communication graph cannot by itself identify a fleet or a swarm. The paper preserves an insight from the initial taxonomy: giving a unit a goal can differ from allocating work to its members. The repair makes that distinction explicit and adds lifecycle control. [§3 D5-D8 and §4.1, PDF pp.2-3](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=2)

## What the initial definitions attempted

The initial hive had a coordinator and delegated workers. Its swarm condition excluded a member with exclusive, persistent command over every other member. Its fleet collected at least two command-capable nodes supervising hives or swarms. Additional prose allowed both temporary swarm leaders and a supreme commander above a fleet. [§2, PDF pp.1-2](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=1)

These definitions look plausible on familiar cases. A single dispatcher is easy to call a hive; a peer protocol is easy to call a swarm. The audit asks what happens when the quantifiers, boundary cases, and kinds of authority disagree.

## Eight defects and the corresponding repairs

The defect labels below are the paper's. The explanations are original summaries. [§3, PDF p.2](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=2)

| Defect | Why the initial test fails | What the repair changes |
| --- | --- | --- |
| **D1: the swarm exclusion is too weak** | If two permanent dispatchers each command a separate subgroup, neither commands everyone. The original negative condition therefore permits substantial permanent command. Even a dispatcher commanding all but one member slips through. | Test the retained authority graph, not just whether one universal commander exists. Name multiple disjoint roots a **partition**, and overlapping original command a **matrix**. |
| **D2: persistence and exclusivity have no operational test** | A leader elected for a term can issue binding decisions while remaining replaceable by the members. The prose calls it a swarm, while the original formula can imply a hive. | Track how authority originates and whether it is member-revocable and term-bounded. Remove edges meeting all three qualifying conditions from the graph used for command-locus classification. |
| **D3: a deep hive and a fleet overlap** | An apex above several commanders can satisfy both the unique-root hive rule and the fleet-with-supreme-commander exception. | Ask whether the apex's execution command crosses the node boundary. Governance over units permits a fleet; execution command reaching the descendants yields a deep hive. |
| **D4: fleet membership and coordination are underspecified** | Empty inter-node relations permit unrelated units to form a nominal fleet; shared units and multiple supervisors blur joint governance with conflicting command. | Require disjoint units, at least two nodes and units, coverage of nodes and units, connected coordination, and limits on execution command across units. Distinguish joint governance from matrix command. |
| **D5: capability substitutes for exercised authority** | Merely having a delegation tool or an inference server does not establish an organisational relation. | Classify actual binding relations over agents and units. A collection of hardware is not automatically an agent organisation. |
| **D6: one relation carries three powers** | Task dispatch, mandate setting, and process restart may belong to different actors. | Separate execution command **E**, governance **G**, and lifecycle **L**. |
| **D7: topology and independence are unclear** | A hierarchy of authority does not determine which agents can communicate. Unspecified axes cannot substantiate an independence claim. | Give four axes explicit values and show counterexamples that vary one while holding the others fixed. This establishes logical separability, not statistical independence. |
| **D8: absence of a commander becomes a resilience claim** | A leaderless organisation can still rely on one shared board. Hearsay-II additionally had a scheduler, according to the author's classification. | Keep command relations separate from communication infrastructure and lifecycle. Removing a command bottleneck does not remove every failure bottleneck. |

### Preserve the D1 wording tension

The audit's D1 paragraph calls its counterexamples hives in a broad rhetorical sense. The final definitions instead call the several-root, disjoint-reach case a **partition**, and Figure 1d depicts two disjoint hives under one label. Treat the paragraph as an argument that permanent command escaped the old swarm test, not as the final type assignment. The guide preserves this tension rather than quietly changing either passage. [§3 D1, PDF p.2](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=2); [§4.2, PDF p.3](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=3); [Figure 1d, PDF p.4](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=4)

## What survives the audit

Bennington explicitly retains three commitments: governance can differ from execution command, units can compose recursively, and the presence of a leader alone should not settle the type. The repair therefore changes the test rather than simply reversing the original labels. A fleet node can command a local hive while being governed from above; a swarm can elect a dispatcher without granting irrevocable authority. [§3, PDF p.2](https://somewhere.systems/research/hive-swarm-fleet.pdf#page=2)

Recursive composition also makes the observation boundary essential. The local unit and the collection of units can have different descriptions. Calling a component a hive does not determine whether the larger organisation is a deep hive, a fleet, or a partition.

## How to read the rest of the paper

The paper supports different kinds of statements in different ways:

1. **A formal proposal:** §§3-4 repair definitions and construct counterexamples. Evaluate consistency, scope, and applicability.
2. **An author classification:** §6 applies the proposal to 22 documented systems. Evaluate the selected configurations and authority evidence. Agreement with the repaired definition is not agreement with an independent ground truth.
3. **A simulated comparison:** §7 reports service-time and message models under controlled conditions. Evaluate assumptions and metrics before translating results to real LLM teams.
4. **An engineering interpretation:** §§8-9 connect results to persistent agents and production practice while listing limitations. Evaluate what additional measurements would be needed.

The [simulation module](04-simulation-results-and-limits.md) keeps the reported performance numbers separate from real-world robustness. The [source audit](05-context-and-source-audit.md) records which implementation and evidence artifacts could actually be inspected.

## Questions for a reading group

- Which observable event would show that a message is an instruction the recipient must obey, rather than a request it can decline?
- Can members revoke their leader using their own protocol, or can only an external owner replace it?
- If a shared service crashes, which relation describes its normal role, and which separate dependency explains the outage?
- Would the same actors receive a different classification if the unit boundary or observation interval changed?
- What would make a classification reproducible by a second reader: an authority diagram, source-code paths, protocol traces, or all three?

Continue with [2. Authority and taxonomy](02-authority-and-taxonomy.md). Use the [complete paper map](06-paper-map.md) to return to the source.
