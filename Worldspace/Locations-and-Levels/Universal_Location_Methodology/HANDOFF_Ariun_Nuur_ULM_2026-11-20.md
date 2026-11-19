# Ariun Nuur ULM run: handoff to a fresh session (written 2026-11-19, for 2026-11-20 onward)

**For the new session.** You are taking over a ULM run already in progress, in a **fresh session so the web-search quota is new** (1,000 calls
per session, shared by every subagent). The developer asked for this handoff on 2026-11-19 at the second window's close, with the weekly
allotment meter at **35%**.

## ⛔ SCOPE: PICK UP WITH ARIUN NUUR ONLY

**Developer, 2026-11-19:** only Ariun Nuur is picked up now. **The rest of the Mirny subnet's cities (Casey, Mirny, Davis, Kunlun,
Zhongshan, Sinheung, Shirayuki, Relung Panen) are tasks for a couple of weeks from now** — their LAW 0-P catch-up research and their
re-runs. **Do not start, research, schedule or open any of them in this session.** Their state is tracked in
`Reference/Real-World/Inspiration_Place_Research/_LAW_0-P_COVERAGE_TRACKER.md` for when the developer brings them up.

## 1 · Your first job, now: set up the two morning jobs

ULM work runs only **05:00–14:59**; no new unit starts after 14:00 (a unit started before 14:00 may run on). The previous session's jobs have
been **deleted**, so these two are yours to create. Use one-shot crons (`recurring: false`) at exactly these times:

- **2026-11-20 05:02** — cron `2 5 20 11 *` — prompt: **§5 below, verbatim**.
- **2026-11-21 05:02** — cron `2 5 21 11 *` — prompt: **§6 below, verbatim**.

Then tell the developer both job IDs and their next-run times, and stop. **No cron on or after 2026-11-22.** Delete both jobs once Step 10 is
recorded.

## 2 · Read, in this order, before any run work (when a job fires)

1. `STARTUP_Ariun_Nuur_ULM_2026-11-18.md` (this folder): the run's full rule set, the banded files and the reading order. **§9 lists the
   seven banded memory files: never open them. Never open `Reference/Real-World/Vostok_Genetics_Research/`.**
2. **This file.**
3. `RUN_PROGRESS_Ariun_Nuur.md` (this folder): every step, append-only. Read from the 2026-11-19 entries to the end.
4. The project `CLAUDE.md`, **LAW 0-P** (new, 2026-11-19), and the runbook's own LAW 0-P section (`00_RUNBOOK.md`, just above its end pointer).
5. `TOKEN_LOG_Ariun_Nuur.md` (this folder): per-agent token rows and per-unit totals. Keep logging the same way.

## 3 · Where the run stands (2026-11-19, close)

**Recorded (each T8: three Opus readers, Round 2 UNANIMOUS, Round 3 six CONSISTENT, one fresh merge writer; each PROPOSED, never declared
complete):** the readiness check, Steps −1, 0, 1, 2, 3, and Phases 2 to 9. Files in the pass folder
`Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/`
(`00.1_…` to `04_Phase_09_Populations.md`, each with its `0Nb_T8_Rounds_…` or `04b_T8_Rounds_Phase_N.md` record).

**Phase 10 (catalog): three units, all through Round 3; NOT yet merged.**

| Unit | What it is | Outputs (archived in the pass folder) | State |
|---|---|---|---|
| **Phase 10** | the phase itself (29-entry list; symbols opened only for B3) | `.t8_Phase10_reader{A,B,C}.md`, `.t8_Phase10_round3_reader{A,B,C}.md`, `.t8_Phase10_round2_run{1,2}.txt` | Round 3 first gave three INCONSISTENT on rule grounds; A and B then repaired (A: the Planet left **open**; B: struck 500-year basis removed, two siting claims removed, REQ-77 and REQ-106 carried); Round 2 re-run UNANIMOUS; re-verdicts **six CONSISTENT** — **Round 3 CLOSED** (2026-11-19). Two notes for the merge in `RUN_PROGRESS`. |
| **Phase 10R** | research supplement on the three official picks (the Phase 10 readers' context ran out) | `.t8_Phase10R_reader{A,B,C}.md` (233 facts, 326 web calls), `.t8_Phase10R_round3_reader{A,B,C}.md` | six CONSISTENT |
| **Phase 10C** | reading check of all 85 candidate rows, no web (the developer's choice) | `.t8_Phase10C_reader{A,B,C}.md`, `.t8_Phase10C_round3_reader{A,B,C}.md` | six CONSISTENT |

**Not yet written:** the Phase 10 merge (`04_Phase_10_Catalog.md`), the candidate-research unit, Steps 5 to 10.

## 4 · What happened on 2026-11-19 that you must carry

- ⛔⛔ **LAW 0-P (developer):** every item on a location's inspiration-picks list is researched and incorporated — the official picks **and
  every candidate row** (`Reference/Real-World/Inspiration_Place_Research/candidates/<City>.md`), any tier. Tiers set order and weight, never
  scope. In the project `CLAUDE.md`, the runbook (own section) and memory. **Still to file (11-20, after Phase 10 is recorded):** `DR-144` in
  `DEVELOPER_RULINGS_LOG.md` with the developer's words; in-place copies in `00_RUNBOOK.md` Step 3, `03_The_Phase_Spine.md` Phase 10 process B,
  `Cities/Research_Logs/README.md`, and `Real-World_Basis_Extrapolation_Method.md`. **The runbook copy is a standing law: no city or run named**
  (developer: *"It's just a standing Law. Period."*).
- **The developer's decision:** *"keep going, add the candidate research unit tomorrow at 05:02."* Ariun Nuur continues; the rest of the Mirny
  subnet (developer: a couple of weeks from now; scope theirs) is **not** this session's work, and is tracked in
  `Reference/Real-World/Inspiration_Place_Research/_LAW_0-P_COVERAGE_TRACKER.md`.
- **Orchestrator rulings, PROVISIONAL, to be filed as questions (next number `DEC-886`):** (1) Phase 10's B3 may name the Planet and Element
  members it determines; names elsewhere are mapped by the merge. (2) Phase 10R reader B's four facts (F111–F114) read from a PDF the fetch
  tool saved locally: admissible as web-source content, marked by source date (a 2017–18 guide); readers A and C refused that step.
- **Settled points for the Phase 10 merge** are in `RUN_PROGRESS_Ariun_Nuur.md` (entries from 13:49 to the close) and in the nine Round 3
  replies: e.g. the platform's 2026 summer program was cancelled (C's read page wins over a stale listing); the polymer platform moved off
  campus; Phase 10C's rows 32 and 42 WAIT; row 55's record-as-identity angle is barred (`DR-28` D2–D3).
- **Method notes for after the run** (logged): a phase cannot read 29 entries and research in one context; `triple_read_verify.py`
  normalizes emphasis marks (the orchestrator's `exact_fields.py` closes that gap); Round 3 on long outputs can exhaust reader context;
  `handoff_audit.py` resets at every heading; `Tools/web_quota_count.py` read 0 for the old session although calls were made (check it in the
  new session; meanwhile log readers' own counts).
- **Next numbers:** Phase 10 merge continues rows from 205, RF-189, SH-38, REQ-144, Q-204; findings `FIND-P10-1` on. Decisions from `DEC-886`.

## 4a · Helper scripts

Copied to `Tools/Orchestrator_Helpers_Ariun_Nuur_2026-11/` (this folder): `checks.py` (quotation pre-check, AmE sweep, other-location name
scan, tower-name count), `exact_fields.py` (exact L1/LLAST check), `make_phase_brief.py` + `phase_parts.py` + `spec_phase10.py` +
`build_phase10.sh` (brief builder), `record_phase.py` + `rec_phase9.json` (round-record writer, with an example spec), `file_decs.py` (files a
unit's questions), and the Round 3 and merge templates. ⚠ **Each script hard-codes the old session's scratchpad path** (`/tmp/claude-1000/…/
9d90e9d3-…/scratchpad/t8/`): copy them into your own scratchpad and change that path before use. The old scratchpad may still exist on disk
but is not yours; read the archived copies in the pass folder instead.

## 5 · The 2026-11-20 05:02 job prompt (create verbatim)

> It is a morning window for the Ariun Nuur ULM run (2026-11-20), in a fresh session. First run `date '+%Y-%m-%d %H:%M'` and log every time
> from it. ULM work only 05:00–14:59; no new unit starts after 14:00 (a unit started before 14:00 may run on).
>
> READ FIRST, in order: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/HANDOFF_Ariun_Nuur_ULM_2026-11-20.md`;
> `STARTUP_Ariun_Nuur_ULM_2026-11-18.md`; `RUN_PROGRESS_Ariun_Nuur.md` from its 2026-11-19 entries; the project `CLAUDE.md` LAW 0-P; the memory
> file `feedback_inspiration_picks_core_tiers_check_all.md`.
>
> THE DAY'S ORDER (DR-107: each step only after the one before is recorded):
> 1. **Candidate research unit (Phase 10R2), under LAW 0-P — the developer's instruction: "keep going, add the candidate research unit
>    tomorrow at 05:02."** Research EVERY row of `Reference/Real-World/Inspiration_Place_Research/candidates/Ariun_Nuur.md` (admit L1–120 and
>    L122–161; L121 names another location; row 86, solo road-travel music, is an orchestrator fact and WAITS for the CST, `DR-140` item 2).
>    Real-world facts only, SOURCED/UNVERIFIED with URLs, search logs verbatim, dead ends logged; no other Antarctic station researched or
>    named; the real station's site only, never its operator. Order by tier and by Phase 10C's leads and treasures (`.t8_Phase10C_reader*.md`
>    and `.t8_Phase10C_round3_reader*.md` in the pass folder), but EVERY row is researched. Three fresh Opus readers, full T8. Give each
>    reader a SHORT reading list so its context goes to research (the pick list, the candidate list at its spans, the research-log README,
>    this city's research log, the two inspiration-place files, `DR-143`). Budget first: the session has 1,000 web calls shared; set each
>    reader's cap so the unit fits and leave room below 850; if the rows cannot all be covered, ask the developer before cutting any row.
> 2. **Phase 10 merge:** confirm Phase 10's Round 3 closed six CONSISTENT (see `RUN_PROGRESS`); if not, put it to the developer before
>    merging. Then one fresh Opus merge writer over ALL inputs — Phase 10's outputs and Round 3 replies (A's and B's repaired versions are the
>    archived `.t8_Phase10_reader{A,B}.md`), Phase 10R's, Phase 10C's and Phase 10R2's — writing `04_Phase_10_Catalog.md`. Then the quotation
>    pre-check, `Tools/quotation_audit.py --own-pass`, the AmE sweep, `Tools/handoff_audit.py`, `Tools/phase_discipline_check.py`, the position
>    ledger (`00.2_Position_Coverage_Ledger.md`, column P10), questions as PROVISIONAL DECs from `DEC-886`, `04b_T8_Rounds_Phase_10.md`, a
>    `09.5_Log.md` entry, and token totals.
> 3. **File the held items** once Phase 10 is recorded: `DR-144` (LAW 0-P, the developer's words) in `DEVELOPER_RULINGS_LOG.md`; LAW 0-P in
>    `00_RUNBOOK.md` Step 3, the spine's Phase 10 process B, `Cities/Research_Logs/README.md`, `Real-World_Basis_Extrapolation_Method.md`
>    (no city or run named in the method files); the four method notes in `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`; update
>    `_LAW_0-P_COVERAGE_TRACKER.md`'s Ariun Nuur row.
> 4. Then **Step 5** (two stages with a seal) if time allows before 14:00.
>
> STANDING RULES (binding): T8 per unit (three Opus readers in private staging folders; Round 2 `Tools/triple_read_verify.py` must print
> UNANIMOUS, plus the exact-field check from `Tools/Orchestrator_Helpers_Ariun_Nuur_2026-11/exact_fields.py`; a failed field is repaired by
> its own reader, first version kept; Round 3 by SendMessage to the same readers, six verdicts CONSISTENT; one fresh merge writer, M-246; raw
> tool output pasted whole). Log tokens per notification in `TOKEN_LOG_Ariun_Nuur.md`. No commit, no push. Never compare Ariun Nuur with any
> other city; never open another city's files or sibling folders in `City_Development_Passes/Mirny_Subnet/`; never open the banded memory
> files (STARTUP §9) or `Reference/Real-World/Vostok_Genetics_Research/`. Never declare anything complete; never start another city.
> Questions to `Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md` as PROVISIONAL on the recommended answer. Freeze every listed file
> during a unit. American English (only "judgement"). Graphify not used (DR-6). The national tower by role only; no demonyms; treaty
> articles only; government and justice wait for the DCI; faith, holidays, dishes, music, dress, games, slang and drinking wait for the CST;
> no robot cold numbers. Never `rm` (the hook blocks it; move to the scratchpad). Always `cd` to the right folder before appending to a log.
> Keep going between steps; do not stop to report.
>
> AT THE WINDOW CLOSE: update `RUN_PROGRESS_Ariun_Nuur.md` and a status line in the `📍 RESUME HERE` block of `MASTER_Process_Tracker.md`,
> ask the developer for an allotment reading, and give a plain-language summary.

## 6 · The 2026-11-21 05:02 job prompt (create verbatim)

> It is a morning window for the Ariun Nuur ULM run (2026-11-21). First run `date '+%Y-%m-%d %H:%M'` and log every time from it. ULM work
> only 05:00–14:59; no new unit starts after 14:00.
>
> READ FIRST: `HANDOFF_Ariun_Nuur_ULM_2026-11-20.md` and `RUN_PROGRESS_Ariun_Nuur.md` from the last window's entries (both in
> `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`). Finish anything the 11-20 window left open first (DR-107), then
> continue in order: **Step 5** (reconciliation and the close pass, two stages with a seal; fold in the Zodiac Lens person-shaped results as
> amendments to Phase 9; the Planet + Element backstop), **Step 6** (differentiation, written blind, WRITE-ONLY), **Step 7** (QA gates),
> **Step 8** (Review Panel, with the late T5 marker), **Step 9** (record), **Step 10** (the readiness check). Each step per the runbook and
> T8. At **Step 10 recorded**: delete both morning jobs, ask the developer for the closing allotment reading, and copy the per-unit totals
> into `ULM_Token_Measurements.md`. If time runs out, record where the run stopped and ask the developer how to continue; there is no cron
> on or after 2026-11-22.
>
> STANDING RULES: as in the 11-20 job (`HANDOFF_Ariun_Nuur_ULM_2026-11-20.md` §5), unchanged.
>
> AT THE WINDOW CLOSE: update `RUN_PROGRESS_Ariun_Nuur.md` and the `📍 RESUME HERE` status line, ask the developer for an allotment reading,
> and give a plain-language summary.
