# Simulation results and limits

The simulation isolates scheduling and failure handling in a deliberately simple service system. It does **not** run language models. Justin Bennington reports two hypotheses as holding and four as mixed; the elected dispatcher looks attractive under the tested conditions, but those results do not establish that an elected LLM team is generally more reliable. This module explains the reported experiment rather than reproducing it. Source: §7, PDF pp.6-8; §9, p.9; Data and code, p.10. See the [complete paper map](06-paper-map.md).

## What was held fixed

The base case contains 16 workers. Their speeds are lognormal, with median 1 and sigma 0.3. Work arrives as a Poisson stream at 0.7 of total capacity; task work is exponentially distributed with mean 1. Runs last 400 simulated time units and discard the first 50. A one-way message takes `delta = 0.05` in the base case. These units have no calibrated conversion into seconds, tokens, or money. (§7.1 and Table 2, p.6.)

Workers also fail at rate 0.002, stay unavailable for 20 time units, and cause lost work to return to ingress after a detection timeout of 5. Common random numbers provide the same arrivals, speeds, and failures for each structure at a given seed. The author reports 200 seeds per condition, means with 95% bootstrap confidence intervals over seeds, and paired comparisons. This pairing makes structural comparisons less sensitive to different random workloads; it does not broaden the model's coverage to real reasoning failures. (§7.1, p.6.)

For coordinator loss, an affected coordinator-like component fails at time 150 and is restarted at 200. The text names the hive coordinator, elected leader, and fleet node 0. A structure without such a component instead loses one random worker for that interval. Consequently, these are failures appropriate to the implemented structures, rather than equal removals of identical functions. (§7.1, p.6.)

## What the seven structures implement

| Structure | Scheduling rule in the simulation | What to watch |
| --- | --- | --- |
| HIVE | One dispatcher, with at most two outstanding tasks per worker | Buffered work masks the beginning of an outage; the dispatch window can limit capacity when messages are slow. |
| HIVE-2 | A root and four sub-coordinators; the root still determines routing | Added hierarchy adds message legs without removing the root's command role. |
| SWARM-CNP | Contract-net allocation with a manager for each task | Announcements, bids, and awards cost messages; concurrent bids can be stale. |
| SWARM-STEAL | Workers obtain work through leaderless stealing | Idle polling can become expensive at low load and low message latency. |
| SWARM-ELECT | A dispatcher whose authority is elected in a Raft-style scheme | Election can replace the failed dispatcher while retaining economical dispatch. |
| FLEET | Four local hives of four workers; a governor routes deliverables in proportion to reported node capacity | Local allocation continues independently, but rerouting depends on capacity reports and spare capacity. |
| FLEET-LATERAL | The fleet additionally permits nodes to take one another's backlog | Lateral exchange reduces the cost of coarse routing in this implementation. |

These descriptions are the author's implementations in §7.1, p.6, not unique implementations of the proposed taxonomy. In particular, a different dispatch window, bidding protocol, election implementation, or capacity-report period could change the comparison.

## Reading the metrics

**Sojourn** measures the time a task spends in the system, so waiting and service both matter. **Messages per task** counts coordination messages; it does not measure their length or the computation needed to produce them. **Retention** is throughput during the outage divided by throughput during the preceding 50 time units. **Sojourn under loss** covers the coordinator-loss scenario. **Makespan** is the time needed to finish a separate burst of 400 tasks already present at time zero. These quantities answer different questions. (Table 2, p.6.)

The table below reorganizes the seven reported Table 2 rows for comparison. Time values are simulated units. The paper reports steady-state throughput of **11.69 for every structure in this base case**. The table's values are means; most intervals are said to be in a separate `results/hypotheses.md`, rather than printed in Table 2.

| Structure | Base sojourn | Messages/task | Outage retention | Sojourn under loss | Burst makespan |
| --- | ---: | ---: | ---: | ---: | ---: |
| HIVE | 1.18 | 2.01 | 0.023 | 14.0 | 28.7 |
| HIVE-2 | 1.34 | 4.02 | 0.026 | 14.7 | 29.1 |
| SWARM-CNP | 1.41 | 30.9 | 0.997 | 1.43 | 76.3 |
| SWARM-STEAL | 1.53 | 6.32 | 0.995 | 1.56 | 29.2 |
| SWARM-ELECT | 1.21 | 2.02 | 0.996 | 1.27 | 28.7 |
| FLEET | 1.81 | 3.06 | 0.941 | 2.21 | 30.7 |
| FLEET-LATERAL | 1.53 | 3.28 | 0.959 | 1.79 | 28.3 |

Below saturation, arrivals can determine completions even when one structure wastes more coordination work. Equal base throughput therefore does not show equal maximum capacity or equal response time. The hive's base sojourn is low, but its outage sojourn is much larger; the burst experiment also gives a very different view of contract net from the steady arrival stream. (§7.2, pp.6-8.)

## Hypotheses: keep the author's mixed verdicts

| Hypothesis | Author's verdict | Reported result and interpretation |
| --- | --- | --- |
| H1: message cost without a throughput gain | Holds | Contract net uses 15.38 times the hive's messages/task, 95% CI [15.35, 15.40]. Relative throughput difference is 0.0000 [-0.0001, 0.0001]. This concerns the tested below-saturation condition, not every arrival rate. (§7.2, p.6.) |
| H2: scaling of message cost with team size | Mixed | Contract-net slope is 1.946 [1.944, 1.948] additional messages/task per added agent; reported endpoints are 7.5 at 4 agents and 62.0 at 32. Hive slope is -0.00013 [-0.00015, -0.00011]. The hive change is tiny, yet its interval excludes zero, so it fails the registered rule requiring an interval containing zero. The author's explanation is amortization of failure-related messages. (pp.6-7.) |
| H3: retention bounds under outage | Mixed | HIVE retains 0.023 [0.022, 0.024]; SWARM-ELECT 0.996 [0.988, 1.003]; FLEET 0.941 [0.933, 0.950]. Four of five bounds hold. Fleet retention exceeds its predicted range [0.6, 0.9], because rerouting and spare capacity preserve more throughput than expected. A favorable surprise still fails that registered bound. (p.7.) |
| H4: recovery after failure | Mixed | Elected-swarm recovery is 0.69 [0.55, 0.84] time units, below the registered limit of 10. Hive throughput recovers immediately after restart, reported as 0.0, failing a requirement that recovery be positive. This recovery metric misses the accumulated queue: hive outage sojourn is 14.0 [13.8, 14.2], and the backlog takes about 150 units to clear. (p.7 and Figure 2.) |
| H5: coordination latency | Mixed | At one-way latency 0.5, contract-net sojourn exceeds hive sojourn by 1.20 [1.02, 1.37], as registered. Work stealing fails the predicted comparison at load 0.3: it is 0.024 faster than the hive and 1.62 faster than contract net. (p.7.) |
| H6: additional hive depth | Holds | HIVE-2 and HIVE have relative throughput difference 0.0000 [-0.0001, 0.0001]; HIVE-2 sojourn is 0.168 [0.166, 0.169] longer. At base latency, two extra one-way legs alone give 0.10; delayed next dispatch adds to that cost. (p.8.) |

An interval extending above 1 for retention is not a probability greater than 100%. Retention is a ratio of two measured throughput windows, and its bootstrap interval can cross 1. The guide preserves the reported [0.988, 1.003] interval.

## Two findings outside the registered hypotheses

At load 0.9 and one-way latency 0.5, the hive's sojourn rises to **40.7** and throughput drops to **12.37**, while contract net reaches **15.02** throughput. The proposed mechanism is specific: the hive allows only two outstanding tasks per worker, so a completion report and subsequent assignment can leave a worker waiting. Contract-net workers queue locally. This is an implementation-sensitive capacity bottleneck, not a theorem that centralized command must be slower. The same discussion reports work-stealing message cost ranging from 141.9/task at load 0.3 and latency 0.01 to 1.3/task at load 0.9 and latency 0.5, because frequent idle polling is expensive. (§7.2, p.7; latency plot is Figure 4b, p.8.)

For the 400-task burst, contract net takes **76.3 [73.3, 79.3]** units versus **28.7** for the hive, about **2.7 times** as long. Every simultaneous auction uses current finish-time bids, so many awards converge on the same apparently fastest worker before its other awards are reflected in bids. The experiment exposes an allocation problem under stale concurrent information. It does not show that all contract-net variants share this makespan. (§7.2, p.8; Figure 5, p.9.)

## Numbers, references, and unresolved source details

The v1 text contains three figure-reference mismatches. Preserve them when discussing the source rather than silently renumbering it:

| Passage in v1 | Printed reference | Figure whose caption describes that quantity |
| --- | --- | --- |
| H2, team-size message scaling, p.6 | Figure 3a | Figure 4a, p.8 |
| H5, latency and high-load saturation, p.7 | Figure 3b | Figure 4b, p.8 |
| Unregistered burst allocation, p.8 | Figure 4 | Figure 5, p.9 |

The abstract's fleet retention 0.94 [0.93, 0.95] is a rounded presentation of H3's 0.941 [0.933, 0.950]. Its contract-net cost of 15.4 and slope of 1.95 likewise round the more precise H1 and H2 values. Table 2 rounds the means, so recomputing a ratio or difference from that table need not exactly reproduce a separately estimated paired comparison. We retain both precisions without inventing a correction.

The discussion's statement that hive outage costs backlog rather than lost throughput should be read with its recovery assumptions: outage-window throughput is very low, and work can catch up after restart. It does not mean the hive maintains throughput during the outage. (§8, p.9, against Table 2 and H3.)

Data and code on p.10 reports **13,800 runs** in total. Seven structures times 200 seeds gives 1,400 runs for one complete set of conditions, not the whole grid; the attachment does not enumerate enough grid details to reconstruct that total independently. It is not appropriate to label this a contradiction or infer missing conditions. The paper also says hypotheses were committed before the grid, that six implementation clarifications followed one smoke run per structure, and that one process slip was logged. Those are author reports, not independently verified preregistration history. See the [source audit](05-context-and-source-audit.md) for available-artifact limits.

## What would support a stronger engineering conclusion

The paper itself names the principal limits: service-time agents do not misunderstand goals or reason incorrectly; a coordinator's deliberation has no modeled cost; messages have no modeled length; failure is mainly loss and restart; and classifications are inferred from documentation. Fleet rerouting also relies on spare capacity: the author notes that above load 0.75 the remaining three nodes cannot absorb the full lost node. (§9, p.9.)

To evaluate a real LLM deployment, retain the authority distinctions but measure additional outcomes: correctness, task verification, correlated bad plans, context and token cost, failed handoffs, completion latency, and behavior under an actual capacity shortage. Vary dispatch buffering, election delay, auction reservations, and reporting periods before attributing an effect to the organizational type alone. These are this guide's proposed follow-up checks, not experiments reported by Bennington.

For agent use, [results.json](../metadata/results.json) records the table, printed intervals, hypothesis status, and caveats. It is a structured reading aid derived from the attachment, not raw data or an independent result set.
