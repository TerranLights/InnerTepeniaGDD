# Token log — the ULM run of Kunlun

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

## Allotment-meter readings (the developer's)
| Date and time | Reading | Note |
|---|---|---|

## Per notification
| Date and time | Unit | Role (reader A/B/C · Round 3 · repair · addendum · merge · helper) | Agent ID | subagent_tokens (cumulative) | Delta | Tool uses | Duration (min) |
|---|---|---|---|--:|--:|--:|--:|

## Per unit (filled when each unit is recorded)
| Unit | Readers | Round 3, repairs, addenda | Merge | Helpers | Unit total | Web calls |
|---|--:|--:|--:|--:|--:|--:|

## The run's totals (filled at Step 10)
| Measure | Value |
|---|---|
| Subagent tokens, all units | |
| Allotment at start · at end · used | |
| Orchestrator share (meter used minus subagent sum, approximate) | |
| Web calls (readers' counts · the tool's count) | |
