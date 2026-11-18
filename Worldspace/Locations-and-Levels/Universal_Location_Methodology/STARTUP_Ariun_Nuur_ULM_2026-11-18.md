# STARTUP FILE — a full ULM run of ARIUN NUUR (this week, 2026-11-18 to 2026-11-21)

**Written 2026-11-18, at the developer's instruction, by the session that ran Relung Panen. Preparation only: that session does not run
Ariun Nuur.** The developer, 2026-11-18: *"we also have enough time in the week (and resources in the weekly model allotment) to be able to
complete a ULM run on another city as well (and the only other remaining city in the Mirny subnet is Ariun Nuur). So, let's go ahead and
continue with setting up the Pre-Trip, the instant-reference datasheets, and the per-Step/per-Phase schedule for Ariun Nuur today. Once
that's done, I'll check the reading on the weekly model allotment, and then we'll start running."* And: *"During each step and or phase,
keep track of how many tokens actually get used. Keep those numbers recorded in a log file … so that we can get a rough, approximate
average of how much resources the ULM actually needs in order to be able to run on any one particular given city, from beginning to end,
start to finish."* **Kunlun still begins on 2026-11-29; that does not change.**

> **The name.** The city is **Ariun Nuur** (Mongolian **Ариун Нуур**), formerly **Vostok** (`DR-42`, 2026-10-03). **The real Vostok Station,
> Lake Vostok and the city's central scientific district keep the name Vostok.** The pass folder's sheets were built while the generator
> still called the city Vostok; each sheet says so in a note at its head. Read "Vostok" in a sheet as the city only where the note says so.

> **Nothing in this file is Relung Panen's content.** It carries procedure and method lessons only. The session that writes it had Relung
> Panen's whole run in context, which is why **this run belongs to a fresh session** (one city run per fresh session).

---

## 0. What to do first, and the clock

### 0.1 How this run starts
- **A fresh session, given this file by the developer.** Run `date '+%Y-%m-%d %H:%M'`. Then:
  1. **Record the allotment reading** (§0.5) before anything else: the developer gives it when handing over this file. Write it, with the
     time, as the first line of the progress file and of the token log.
  2. Create the morning jobs (§7), report their IDs and next firing, log them, and keep the session open.
  3. **If the clock is inside 05:00–13:59, begin Section 1 at once** (a start on 2026-11-18 itself is expected). Otherwise wait for the
     first job.

### 0.2 The cron prompt (word for word)
> It is a morning window for the Ariun Nuur ULM run. First run `date '+%Y-%m-%d %H:%M'` to confirm the clock is inside the 05:00-14:59 operating
> window (do not start a new piece after 14:00; if outside the window, stop and say so). Then read in full
> `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Ariun_Nuur_ULM_2026-11-18.md`
> and follow it exactly. Read `RUN_PROGRESS_Ariun_Nuur.md` beside it if it exists and resume from the next unfinished piece; otherwise begin
> with Section 1, then Section 2. One piece at a time, each written to file and recorded before the next. Auto mode: do the work and ask
> only what blocks it. No commit, no push, never edit a pass file outside its own run, never compare any city with another, never declare
> anything complete, never start another city. When the window closes, update the progress file and the tracker, and give the developer
> a short plain-language summary of what ran, what is open, and what is next.

### 0.3 The window and the pace
- **Operating hours 05:00–14:59 only** for ULM work. **New units may start until 14:00**; 14:00–14:59 is the wrap-up (§8). A unit begun
  before 14:00 may finish in the wrap-up. If the window closes mid-unit, write a checkpoint into the progress file and stop. The developer's
  decision sessions may run at any hour; ULM work may not.
- **The progress file** is `Universal_Location_Methodology/RUN_PROGRESS_Ariun_Nuur.md` (append only). Create it with the allotment line.
- **Depth over speed (LAW 0).** Three Opus readers on every unit; never fewer readers, rounds or list items.

### 0.4 The web budget (method lessons, measured on the previous run)
- **1,000 web calls per session, shared by every agent.** Check it at every piece boundary with
  `python3 Tools/web_quota_count.py --tasks <this session's tasks folder>` (always pass `--tasks`).
- **The tool's count, not the readers' own counts, is what the limit enforces, and it reads higher** (measured: 643 against about 500
  logged; then +280 for a unit whose readers logged 189). **Set every reader's cap from the tool's remaining count**, with a reserve.
- **Above 850, start no research-heavy piece**: stop at the boundary and tell the developer a fresh session is needed.

### 0.5 The measurement (the developer's second purpose)
- **Nothing else runs during this run**, the DCI session included; if anything else is running, say so to the developer at once.
- ⭐ **The developer reads the allotment meter before this session starts and tells it the reading.** Record it, with the time, as the
  first line of the progress file and of the token log, before anything else.
- **At the end,** ask the developer for the closing reading and record it the same way; at each morning's close, ask for a reading too if
  the developer is present.
- **The token log is `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`** (developer, 2026-11-18: *"During each step and or phase,
  keep track of how many tokens actually get used. Keep those numbers recorded in a log file"*). **Follow its "How to record" section
  exactly:** one row per task notification as it arrives (each agent's `subagent_tokens` is cumulative, so record the delta too), a total
  line per unit, the developer's allotment readings with their times, and the run's totals at Step 10. The progress file's line for each
  unit also carries the unit's total. At the close, copy the per-unit totals into `ULM_Token_Measurements.md`.
- The figure is the developer's; this file states no estimate.

## 1. Read first, in full, before touching anything
Paths are under `Worldspace/Locations-and-Levels/Universal_Location_Methodology/` (the ULM) unless stated; "Cities" is
`Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`. **Use absolute paths in every tool call.**
1. `00_RUNBOOK.md`, **in full** (CLAUDE.md requires it). It changed on 2026-11-18: `DR-141` item 3, independent convergence, is at Step 3
   item 3.4 (L2620), with a pointer in `02_Generators_Capability_and_Symbols.md` (L254).
2. `Amendment_Layer_Rules.md`; `T8_Standing_Brief_Lines.md` (lines 1–25); `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N (the three rounds, the
   unanimous gate, the merge rule `M-246`).
3. `MASTER_Process_Tracker.md`: the SESSION BOOT and the `📍 RESUME HERE` block (its last lines name the schedule).
4. `DEVELOPER_RULINGS_LOG.md`: **the general rulings** (§4 below) **and every ruling naming Ariun Nuur or Vostok** (`DR-42`, L892, the
  rename, names it in its heading; find the rest by a name search that prints line numbers only, then read those rulings). **In a ruling
  that holds several locations, read only its general items and Ariun Nuur's items.** A ruling given for another city does not carry here unless the
  log records it for every city. **The rulings `DR-136` to `DR-141` hold two other cities' own items; read only their general items**
  (§4), and cut those rulings' other-location lines out of every reader's span.
5. Ariun Nuur's pass folder, `Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/`: its `README.md` and `00.0_Pre-Trip_Inspection.md`.
  **It holds scaffolding only** (the Pre-Trip, the position ledger, the README and 19 datasheets, last built 2026-11-02/03). There is **no**
  `Cities/Ariun_Nuur/` input-status folder.
6. **The input validation of 2026-11-18** (§10): what was checked, what was corrected, and what is left for the developer.

## 2. The run
1. **Isolation first** (the first entry of Ariun Nuur's research log and its run log): the session never opens another city's pass,
   culture, spec, personality or vision files. ⚠ **Ariun Nuur's pass folder sits in a subnet folder holding several other cities' passes**
   (`City_Development_Passes/Mirny_Subnet/`): **never list, search or open those folders**, and never use a glob that reaches them. A
   relation from Ariun Nuur's own lines (a road, a port, the subnet) is legal, taken only from Ariun Nuur's lines and the shared things' own
   records (`DR-122` item 5, `DR-131` item 3, `DR-136` items 2–3).
2. **The memory bands:** see §9 (a readiness scan for this city, 2026-11-18). **Never open a banded file during this run.** Copy §9's list
   into the progress file's first lines when the run starts.
3. **Then a readiness check before Step −1** (one unit, recorded): **the sheets against the live sources**: `python3 Tools/build_pretrip.py
   Ariun_Nuur --out <scratch folder>` and compare with the Pre-Trip (the generator now builds a leaner layout; the pass folder's richer
   sheets are kept); `git log` on every source the Pre-Trip and datasheets cite. **Start from §10's validation report**, which already checked
   every row against its live source and the rulings since 2026-11-03: carry its open items to Step −1, and list each later ruling's general
   items and Ariun Nuur items that the Step −1 readers must carry. Never `--write`, never `--force`, never edit a tool. A stale figure is recorded and the
   run uses the live source; a stale sheet is a question for the developer.
4. **Then Step −1, Step 0 (with Step 0.5's deferred list) and Steps 1 to 10, each as one T8 unit**: a reading list (built by hand against
   the runbook's MUST OPEN blocks); a frozen brief carrying the standing lines; **three Opus readers, each in its own private staging
   folder**; Round 2 with `Tools/triple_read_verify.py`; Round 3 by SendMessage to each reader; **one fresh merge writer** (`M-246`); the
   quotation pre-check and `Tools/quotation_audit.py --own-pass` before the round record; the American English sweep; the round record with
   every tool's raw output pasted whole. Phases 2 to 10 run in the runbook's order; Step 6 is write-only; Step 7 runs the seventeen gates;
   Step 8 the Review Panel (six dispositions); Step 9 the record and 9.5 the recording law; Step 10 the readiness check.
5. **Method lessons from the previous run, to apply** (procedure, not content):
   - **A Round 3 INCONSISTENT verdict:** confirm the point at source, ask the reader to check and repair its own output (keep the first
     version as `…_prerepair.md`), re-run Round 2, and ask the objecting reader for an addendum. Never write without all six CONSISTENT.
   - **Step 5 in two stages, with a seal:** stage A with no read-last material, ending with the named leg; seal it by sha256 and a byte
     copy; re-check before stage B's Round 2; stage B's merge into a separate file, appended by the orchestrator; `cmp` the head after.
     (Applied on the previous run; its adoption into the runbook awaits the developer, `DEC-641`.)
   - **Step 6's row is written blind** (runbook L2934): back up the table, insert by script asserting headers and column counts, `diff`
     against the backup. **The Subnet cell may name the subnet**: it is a shared thing the city's own lines give.
   - **The record script's verdict capture** takes the first two verdict lines per reader (summary lines and headings miscount).
   - **Keep every orchestrator command to the one action it records.** The hooks block `rm` and `mv` onto existing files, and a stray
     file shuffle blocks the whole command.
   - **Freeze every file on a unit's list while it runs**, the run log included: hold run-log entries in the progress file meanwhile.
   - **A brief's naming rule** ("never name another location") should carve out the location's own subnet.
6. **Ariun Nuur's own rulings** are in the log (§1 item 4). Open items go on Step 0.5's deferred list; they do not block.
7. **Not inputs:** the vision notes (`DR-10`, never an input and never a check); the megasheets (withheld); the city's own culture,
   robot-culture and personality files are read last, at Step 5's stage B, as a check, never as an input; the neo-race catalog, if one
   exists, is not an input at any step.
8. **Which source folders may ground a finding:** the inspiration picks, the `Infrastructure/` files and the city-relationship files, **for
   every city** (`DR-138` item 1); the picks are a full generator for every city (`DR-138` item 2).
9. **Symbols at Phase 10 only** (`DR-8`, `DR-8a`, `DR-115`): the symbol files are not opened before Phase 10, and their spans are chosen
   only after Phase 9 is recorded. **Cut every other city's pair out of every reader's span**, the rulings log's included: the previous run
   found another city's pair inside a general rulings span, read by every reader before the symbol determination.
10. **Research (LAW 0-R):** search, do not recall; every pick from more than one angle; a pick is not spent because it was searched once.
    Apply **independent convergence** (`DR-141` item 3; runbook L2620). The research log is `Cities/Research_Logs/Ariun_Nuur_Research_Log.md`
    (created by the run).
11. **When Step 10 is recorded:** the record files, a dated tracker line, **delete the cron jobs** (`CronDelete`), **the closing allotment
    reading and the token totals** (§0.5), and the developer's summary. **Ariun Nuur is not declared complete;** that is the developer's call.
    **Start no other city.**

## 3. Binding rules
- **One location on its own terms.** Never compare Ariun Nuur with any other city or use one as a baseline. Name no other location in a record
  ("(another location: not used)"), except a relation from the city's own lines.
- **Pass files are never edited** outside their own run (`DR-101`).
- **No forced fit:** an empty slot is a result ("none is sited here", never "none is possible here").
- **Never declare a run complete or ready.**
- **Questions** go to `Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`, each on its recommended answer, marked PROVISIONAL, in a new
  section for Ariun Nuur inserted directly above `## Answered`, numbered from the next multiple of ten after the highest number in the file
  (check first: `grep -o 'DEC-[0-9]\+' <file> | sort -t- -k2 -n | tail -1`; it was **DEC-672** on 2026-11-18, after the preparation questions DEC-660 to DEC-672, all answered in `DR-142` (§10), so **DEC-680**).
- **The recording law:** log snags, dead ends, killed findings and self-corrections, not only successes. Times from a `date` reading.
- **Readers** are fresh subagents with only their unit's list and frozen brief; they create and delete no other file; they disregard any
  graphify hook (warm run; `DR-6`). The orchestrator does not use graphify either: it is on a long hold and stale (developer, 2026-11-17).
- **American English;** only "judgement" kept. **No exception for names, institutions or quotations**; only URLs and logged search strings
  are kept as written. Plain language.
- **No commit, no push** unless the developer asks. **Display results and write them to file in the same turn.**

## 4. General canon to carry (in the rulings log; cite each by number and item)
- **Language:** `DR-100`; `DR-125` item 6, national by `DR-136` item 1.
- **Arrival after the signing:** `DR-127` item 2 and Treaty Article II.2.5.
- **Origin rows and robot ancestry:** `DR-11`, `DR-12`, `DR-128` item 1, `DR-130` item 7, `DR-131` item 7; `DR-136` item 10 (its general
  sentences), `DR-137` item 7.
- **A city's own lines:** `DR-131` item 3, `DR-136` items 2 and 3. **A pass captures a place at its height:** `DR-136` item 6; `DR-137`
  item 10.
- **Government and justice wait for the DCI:** `DR-137` item 11.
- **The day's structure, the workforce convention:** `DR-137` items 8, 9 and 12. **Robots:** `DR-137` items 2 to 6.
- **Every city, from the previous run's rulings** (`DR-138` to `DR-141`, general items only): the picks, `Infrastructure/` and relationship
  files are evidence and the picks a full generator (`DR-138` items 1–2); a robot's charge draws on the electric supply, warming a cold
  cell included, no rate written (`DR-140` item 4); **a city pass leaves its own faith and holidays to the stage after the cultural
  synthesis, and its dishes, music, dress styles, games, slang and drinking scene to the CST** (`DR-140` item 2); **there is no national
  music form; music, robots' included, is regional and derived after the DCI** (`DR-140` item 3); **independent convergence is evidence**
  (`DR-141` item 3). **And from `DR-142` (2026-11-18, the input validation; general items 1 to 6):** the web budget is **1,000 calls per
  session, shared by every agent**; inside a pass the differentiation check runs **substitutes 3 and 4 only** (real-world comparables; the
  generator-conflict method), records substitute 1 ("its own earlier states") as **deferred to after the pass**, and never runs
  substitute 2, which reads another location; findings may rest on the **Falkland Treaty draft's articles, each tagged
  `[treaty draft]`** and listed; `19`'s national food figures are citable **as national context only**.
- **Census I governs the band** (`DR-4`). **Founders come only from the Founding Register** (`DR-19`); the founders check runs with the
  register's spelling of the name.

## 5. Each morning's close
Update the progress file (dated, with the units' token counts); add one dated status line to the tracker's `📍 RESUME HERE` block after its
last dated line (one line plus a pointer; never rewrite earlier text); give the developer a short plain-language summary.

## 6. Logs, cut-offs and resuming
The progress file records what happened, never what was found; **no reader is ever given it.** The recording-law log is Ariun Nuur's
`09.5_Log.md`. A session cut off mid-unit resumes from the progress file and the readers' staging folders.

## 7. The morning jobs (05:02, one-shot)
- One-shot jobs, one per morning at 05:02 (`cron: "2 5 <day> <month> *"`, `recurring: false`, the §0.2 prompt word for word), **for
  2026-11-19, 2026-11-20 and 2026-11-21 only.** Log every ID and its day.
- ⛔ **No job on or after 2026-11-22** (the DCI week; developer, 2026-11-16). **Kunlun begins on 2026-11-29 in its own session, with nothing
  else running** (its measurement). If this run is not finished at the 2026-11-21 close: write a checkpoint, and **ask the developer**
  whether it resumes after Kunlun's run or another time; never run alongside Kunlun.
- When Step 10 is recorded, every remaining job is deleted.

## 8. Standing practice (developer, 2026-11-16)
*"During the productive hours (5:00am to 3:00pm, with the wrap-up beginning at 2:00pm), once one Step/Phase is complete, any and all
questions and/or decisions that you need from me, just log in the questions decisions file, and then continue with the next Step/Phase."*
**Never stop between units to report or wait;** questions go to the decisions file on their recommended answer, PROVISIONAL. Pre-build the
next units' lists and briefs while readers run, and report one short line per finished step.

## 9. The banded memory files (names only; never open them during this run)
In the memory folder (`/home/kuroskalacs/.claude/projects/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/memory/`), each carrying a line `CONTAMINATION BAND — ARIUN NUUR (formerly Vostok)` under its header (2026-11-18). From a shape-only scan of the memory folder for "Ariun", "Ариун" and "Vostok" (59 files with real hits, 204 lines; 5 lines were the unrelated real city Vladivostok): **seven** carry characterization, significance or vision-session lines about this city; 52 are attribute-only. The auto-loaded `MEMORY.md` index is attribute-only, but two of its link labels point at banded files: do not follow them.

1. `project_city_vision_notes.md`
2. `project_kunlun_vostok_dlc_connection.md`
3. `project_cryptograph_helix_bioinformatics_connection.md`
4. `project_byrd_extrapolation_in_progress.md`
5. `project_refugee_affinity_verification_pass.md`
6. `project_vostok_redistribution_retcon.md`
7. `project_charlene_vostok_geneticist.md`

**The required reading:** three runbook lines name this city (L1958 and L2073, attribute only; **L2074, borderline**: read the rule, skip that line's example, and do not open the folder it names). Recorded in `06_Worked_Example_Provenance.md` (its Ariun Nuur section). No other ULM method file names it.

## 10. The input validation of 2026-11-18
At the developer's instruction (*"check to make sure that all the information is valid and correct/accurate"*), the pass folder's
Pre-Trip, position ledger, README and 19 datasheets were checked **row by row against their live sources and the rulings since 2026-11-03**,
before this run, by the session that prepared it:
- **Three validators** (the Pre-Trip, ledger, README and Steps −1 to 3; Phases 2 to 6; Phases 7 to 10 and Steps 5 to 10) found **111
  problems**: 10 wrong figures, 25 stale after a ruling, 24 moved line ranges, 8 broken citations, 15 stale names (the sheets called the
  city Vostok), 31 others. **None of the 75 composition figures was wrong.**
- **A fix writer** re-checked each at its source and applied **100** (263 line edits in 22 files, **no line count changed**: other files cite
  these by line); **a separate checker** confirmed **262 of 263** edits at their sources, found none wrong and none unlisted, and found one
  clause unclear (fixed). The orchestrator then applied **nine more** in place: the items `DR-140` item 2 already settles for every city
  (Phase 4's population-specific days, Phase 6's doctrine question, Phase 6's must-open rows, Step 6's culture cells), the README's Step 7
  file name, a Step −1 comparison with other cities, a withheld Phase 7 row whose two phrases may come from this city's own read-last
  material, the unclear clause and a note's section list.
- **The sheets now use the name Ariun Nuur**, keeping "Vostok" only for the real station, Lake Vostok and the central scientific district
  (`DR-42`); each sheet's line 3 says so.
- **Tools after the fixes:** `verify_city_sheets.py Ariun_Nuur`: 20 checks, 0 FAIL, 2 NOTE; `audit_city_inputs.py --city Ariun_Nuur`: tests
  40, GAP 0, note 3. **A blind spot found:** the verify tool's "carried names" check did not see the old name in the ledger's title.
- **The developer answered all of them the same day** (`DR-142`, 2026-11-18; `DEC-660` to `DEC-672`), and the answers are applied:
  Step 2 reads `16` §23 beside the first-pass row (§23 governs); spec L219's bullet is excluded whole; Step_0's census quotation is kept,
  flagged stale; Phase 5's flagged rows are this city's own citable lines; Phase 7's headcount is marked not citable and its 3.5× stale
  (≈ 3.8× live); **the source errors were corrected at their sources before the run** (the spec's station line, two census lines, two
  relationship-file lines, the Doll categories path); the README lists the input contract and the round records. **A second fix writer
  applied these (53 changes); a separate checker confirmed 49, found 3 wrong (a path changed inside a quotation; two notes giving
  the founders where the Primary tier was meant) and 1 self-contradicting row; the orchestrator fixed all four at their sources, plus two
  citation ranges, and both tools still pass (`dr142_ariun_checked.md` in the scratchpad).** Nothing
  is left open from the preparation.
- **The shared quick-reference sheets** were validated too, with Mawson's double-check (54 problems, 51 fixed and checked; the six
  full-text sheets re-copied from their sources and matching them): `INPUT_VALIDATION_LOG_2026-11.md`.
- **The working files** (outside the repository, in the preparing session's scratchpad): the three validation reports, the change report,
  the checker's report, and two backups of the folder (before the fixes and before the last nine edits): `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/e35a4021-07fc-4998-b0b3-3b1c8e253713/scratchpad/ariun/`.

## 11. The per-Step and per-Phase schedule
**A plan, not a target:** LAW 0 governs, and a unit is never cut to keep to it. It is sized from the pace of the previous ULM run, measured
in its progress file: about 30 to 45 minutes per unit for the short steps, 60 to 90 for the research step and for Step 5's two stages, and a
full window for Phases 2 to 10.

| Window | Units, in order | Notes |
|---|---|---|
| **2026-11-18** (from the start, until 14:00) | the readiness check before Step −1 · **Step −1** (the input contract) · Step 0 if time allows | §2 item 3; the input validation (§10) is its starting point |
| **2026-11-19** | Step 0 (if not done) · **Step 1** · **Step 2** (the picks a full generator from the start, `DR-138` item 2, so no later amendment is needed) · **Step 3** (research; the web cap per reader set from the tool's remaining count, §0.4) | Step 3 is the run's heaviest web user |
| **2026-11-20** | **Phases 2 to 10**, in the runbook's order (Phase 10's symbol spans chosen only after Phase 9 is recorded) | a full window |
| **2026-11-21** | **Step 5** (two stages, sealed) · **Step 6** (write-only, blind) · **Step 7** (the seventeen gates) · **Step 8** (the Review Panel) · **Step 9** (the record; apply its ruled changes) · **Step 10** (the readiness check) | delete the jobs when Step 10 is recorded; take the closing allotment reading |

**If a window runs short,** the unit in progress checkpoints and the schedule moves one unit later; never compress a unit. **If the run
reaches the 2026-11-21 close unfinished,** see §7.

**Per unit, one token-log total** (§0.5): the schedule's real durations and token counts are what the developer's measurement is for.
