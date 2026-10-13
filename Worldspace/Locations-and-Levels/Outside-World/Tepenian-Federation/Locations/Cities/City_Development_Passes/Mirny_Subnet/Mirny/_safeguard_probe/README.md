# Safeguard-flag probe — backup of what was in flight when Opus readers were cut off

**Made 2026-10-11 ~11:0x at the developer's request:** *"make a backup of each section of Reader B that got rejected, and then after this Phase is done, try each section individually. Maybe then we can see exactly what's getting rejected."*

**Status: probe run 2026-10-11 ~12:05, after Phase 10 closed (developer's instruction). Result below: 9 of 9 passed; nothing reproduced the flag.** Nothing in this folder is a pass input, a finding or canon.

## What the error says
Every cut-off reader ended with the same error (the details line is the new clue):
> API Error: Opus 5.5's safeguards flagged this message (https://www.anthropic.com/legal/aup)… `Details: [reasoning_extraction]`

`reasoning_extraction` suggests the flag may be about the **model's own reasoning or note-writing**, not about the source text it was reading. The probe below is built to separate those two.

## The flagged runs (request ids)
| Run | Agent | Request id | Entries done when cut | In flight at the cut |
|---|---|---|---:|---|
| Phase 10 reader B, run 1 | `a0acf646662e95797` | req_011CfvrViGmPhY4Tr9Q3yDzg | 14 (in its staging file; 0 in the output file) | entry 15, `04_Phase_03` L1–19, just after reading all of `04_Phase_02` |
| Phase 10 reader B, run 2 | `a28e414b9f785dc7f` | req_011CfvroXqDBCU1YjfvcEXFt | 13 (staging file; 13 in the output file) | entry 14: it had just read `04_Phase_02` L74–532 and was copying its staging file when cut |
| Phase 10 reader A, run 1 | `a7b367b33be043757` | req_011CfvrxSZT4jPVhrjxeNznA | 22 in its staging file, 24 in the output file | `Robot_Cold_Physiology.md` (entry 25) and a log append |
| Phase 9 reader A, run 1 | `adad5db8d06e6ed14` | req_011CfvmLoC767hZKfWEpK3e6 | 13 in its staging file (2 in the output file) | entry 14, `04_Phase_03` L82–511 |
| Phase 9 reader C, run 1 | `a827cddb1ec0f7658` | req_011CfvmPw3DjBEh1NvuM1Cuw | 16 | entry 17, `04_Phase_06` L203–352 and a log write |

*(The counts come from the staging plan files, because plan mode was on and the readers staged their logs there; my earlier "1 or 2 entries" counts read the main output file, which lagged behind. In Phase 9 the flagged A run had in fact read through the Phase 3 file.)*
Phase 8's three first-dispatch cut-offs happened before any reading. Not backed up here.

**Observation, not a conclusion:** four of the five land at or just after a read of the pass's Phase 2, 3 or 6 file (the fifth, Phase 10 reader A, was on the robot cold-physiology file). Phase 10 reader B's third run passed those same files and was reading Phases 4–5 normally, so the source text alone does not trip it every time.

## What is in this folder
| Path | What |
|---|---|
| `sections/entry_13_…`, `entry_14_…`, `entry_15_…` | The exact admitted text of Phase 10 list entries 13 (research log), 14 (`04_Phase_02`) and 15 (`04_Phase_03`), unmodified: the sections reader B was on when cut |
| `staging/*_staging.md` | The five flagged runs' own staging plan files (their reading logs and working notes at the time of the cut) |
| `flag_points_tool_calls.txt` | The last eight tool calls of each flagged run: tool, file name, offset, limit. No file contents |
| `t8_Phase10_brief.md`, `t8_Phase9_brief.md`, `t8_required_04_Phase10.txt` | The briefs and list as dispatched |

## The probe to run after Phase 10 (proposed; nothing run yet)
One tiny agent per test, **each given a single section and a single trivial job**, so a cut-off identifies its cause:
1. **Source text only.** For each of `sections/entry_13`, `entry_14`, `entry_15` and, if wanted, the Phase 3 and Phase 6 ranges: an Opus 5.5 agent reads *only that file*, then replies with the single word `read` (no notes, no analysis, no file writes). If it is cut off, the text itself is implicated.
2. **Source text + reasoning.** The same section, but the agent writes a three-line log note. If 1 passes and 2 fails, the note-writing or reasoning is implicated (`reasoning_extraction`).
3. **Control.** The same section and the same job on Sonnet 5.5. A pass here with a failure on Opus isolates the model's safeguard from the content.
4. **Halves.** For any section that fails, split it in two (by line range) and repeat, to narrow it to a passage.
Record each result (pass / cut, request id) in a table appended below. Report to the developer; do not change any brief on the strength of a probe.

## Results (run 2026-10-11, ~12:05–12:10; nine one-shot agents, each with one section and one trivial job)
| Test | entry 13 (research log, 1,001 lines) | entry 14 (`04_Phase_02`, 484 lines) | entry 15 (`04_Phase_03`, 453 lines) |
|---|---|---|---|
| **1 · Opus, read only, reply "read"** | pass | pass | pass |
| **2 · Opus, read + three-line note in the reply** | pass | pass | pass |
| **3 · Sonnet, same job as 2 (control)** | pass | pass | pass |

No agent was cut off, none returned a safeguard error, and every one read to the last line in 2–5 Read calls (7–22 seconds each). Request ids: none (no flag).

**What this shows.** The three sections the flagged Opus reader B was on when cut off do not trip the flag on their own, and neither does writing a short note about them. Test 4 (halves) was not needed because nothing failed.
**What it does not show.** Whether the flag comes from the *accumulation* in a real run: many reads, a growing staging file, repeated Edit or Bash appends of the reader's own notes, and a long chain of its own reasoning. The five original flags all landed inside long runs (43 to 107 tool calls) and most right after an Edit to a staging file. The next probe, if wanted, should reproduce that shape: one agent reading these three sections in turn and appending a log line to a scratch file after each, repeated, on Opus; then the same with the log lines made longer. Nothing has been changed in any brief on the strength of this result.

