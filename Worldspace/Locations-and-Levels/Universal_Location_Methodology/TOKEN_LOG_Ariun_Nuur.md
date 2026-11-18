# Token log — the ULM run of Ariun Nuur

**Why this file exists** (developer, 2026-11-18): *"During each step and or phase, keep track of how many tokens actually get used. Keep those
numbers recorded in a log file, and then we'll use that as a reference to measure how much resources each step, each phase of the ULM
actually requires. We'll do this for both Kunlun and Ariun Nuur so that we can get a rough, approximate average of how much resources the
ULM actually needs in order to be able to run on any one particular given city, from beginning to end, start to finish."*

## How to record (the orchestrator, during the run)
- **Every agent's tokens come from its task notification:** the `subagent_tokens` figure, with `tool_uses` and `duration_ms`.
- **The figure is cumulative per agent.** A reader resumed for Round 3, a repair or an addendum reports its running total each time. Record
  each notification as it arrives, and compute the **delta** (this notification minus that agent's previous one). The unit's cost is the sum of
  every agent's **last** figure.
- **One row per notification**, in the table below, written when the notification arrives (not reconstructed later).
- **A unit's total line** when the unit is recorded: readers, Round 3, repairs and addenda, the merge writer, and any helper agent.
- **The orchestrator's own tokens are not reported per unit** by any tool. They are captured by the **allotment-meter readings** the developer
  gives: at the start, at the end, and (if the developer is present) at each morning close. Record each reading with its time.
- **Web calls** per unit, from the readers' own counts and from `Tools/web_quota_count.py` (which reads higher).

## Preparation, 2026-11-18 (by the session that ran Relung Panen; **not part of the run's measurement**)
| Agent | Task | subagent_tokens | Tool uses | Duration (min) |
|---|---|--:|--:|--:|
| validator A | the Pre-Trip, ledger, README, Steps −1 to 3 sheets | 275,693 | 75 | 13.0 |
| validator B | the Phase 2 to 6 sheets | 185,660 | 54 | 8.0 |
| validator C | the Phase 7 to 10 and Step 5 to 10 sheets | 196,791 | 78 | 10.9 |
| memory scan | memory and required reading, by shape | 92,899 | 18 | 3.1 |
| fix writer | applying the corrections | 314,841 | 59 | 14.6 |
| checker | verifying the corrections | 275,543 | 79 | 12.6 |
| **Preparation, subagents in all** | | **1,341,427** | | |

## Allotment-meter readings (the developer's)
| Date and time | Reading | Note |
|---|---|---|
| 2026-11-18 13:16 | **12%** | the start of the run; given by the developer with the handover of the startup file |
| 2026-11-18 14:01 | **13%** | after the readiness check and Step −1 (Step −1's subagents: 914,005 tokens); given by the developer |
| 2026-11-18 15:42 | **14%** | the first day's close, after Step 0 (Step 0's subagents: 1,246,877 tokens; day total 2,160,882); given by the developer |

## Per notification
| Date and time | Unit | Role (reader A/B/C · Round 3 · repair · addendum · merge · helper) | Agent ID | subagent_tokens (cumulative) | Delta | Tool uses | Duration (min) |
|---|---|---|---|--:|--:|--:|--:|
| 2026-11-18 13:34 | Step −1 | reader B | a4f16872c4e1e396b | 170,621 | 170,621 | 42 | 9.1 |
| 2026-11-18 13:35 | Step −1 | reader C | ae8de1fc7b5ce0842 | 171,488 | 171,488 | 42 | 9.7 |
| 2026-11-18 13:37 | Step −1 | reader A | a098665c856e2f16e | 188,874 | 188,874 | 44 | 12.0 |
| 2026-11-18 13:39 | Step −1 | Round 3, reader C | ae8de1fc7b5ce0842 | 218,681 | 47,193 | 3 | 1.4 |
| 2026-11-18 13:40 | Step −1 | Round 3, reader B | a4f16872c4e1e396b | 222,028 | 51,407 | 3 | 2.0 |
| 2026-11-18 13:40 | Step −1 | Round 3, reader A | a098665c856e2f16e | 237,879 | 49,005 | 3 | 2.1 |
| 2026-11-18 13:54 | Step −1 | merge | a5be549d0b010f72b | 235,417 | 235,417 | 20 | 12.5 |
| 2026-11-18 14:14 | Step 0 | reader A | aa3736c660d86e995 | 248,957 | 248,957 | 35 | 10.3 |
| 2026-11-18 14:14 | Step 0 | reader B | a6dd3497d646e97b8 | 249,550 | 249,550 | 32 | 10.8 |
| 2026-11-18 14:17 | Step 0 | reader C | ac704552f301ca3e5 | 278,346 | 278,346 | 106 | 13.4 |
| 2026-11-18 14:20 | Step 0 | Round 3, reader B | a6dd3497d646e97b8 | 313,656 | 64,106 | 3 | 1.8 |
| 2026-11-18 14:20 | Step 0 | Round 3, reader A | aa3736c660d86e995 | 314,754 | 65,797 | 4 | 1.9 |
| 2026-11-18 14:20 | Step 0 | Round 3, reader C | ac704552f301ca3e5 | 341,505 | 63,159 | 4 | 2.0 |
| 2026-11-18 14:33 | Step 0 | merge | a9a2aca37c405fda7 | 276,962 | 276,962 | 27 | 10.4 |

## Per unit (filled when each unit is recorded)
| Unit | Readers | Round 3, repairs, addenda | Merge | Helpers | Unit total | Web calls |
|---|--:|--:|--:|--:|--:|--:|
| Readiness check before Step −1 | 0 | 0 | 0 | 0 | **0** (orchestrator only; no subagent) | 0 (tool: 0) |
| Step −1 (input contract) | 530,983 | 147,605 | 235,417 | 0 | **914,005** | 0 (tool: 0) |
| Step 0 (frame; Phase 0) | 776,853 | 193,062 | 276,962 | 0 | **1,246,877** | 0 (tool: 0) |

## The run's totals (filled at Step 10)
| Measure | Value |
|---|---|
| Subagent tokens, all units | |
| Allotment at start · at end · used | |
| Orchestrator share (meter used minus subagent sum, approximate) | |
| Web calls (readers' counts · the tool's count) | |
