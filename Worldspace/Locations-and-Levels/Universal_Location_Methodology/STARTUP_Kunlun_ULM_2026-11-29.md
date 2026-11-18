# STARTUP FILE — a full ULM run of KUNLUN (week of 2026-11-29)

**Written 2026-11-18, at the developer's instruction, by the session that ran Relung Panen. Preparation only: that session does not run
Kunlun.** The developer, 2026-11-17: *"On the week of November 29th, instead of drafting the remaining "Springboardings" for the remaining
Tepenia-represented countries/cultures/nations, I'd like to postpone those Springboardings for later that week, and begin the week by doing
a full ULM run on the city of Kunlun. This will accomplish a couple things at once: 1.) We'll be able to knock out another ULM city run,
and 2.) We'll see exactly, precisely how much of the weekly model allotment one single, full, complete ULM city run actually takes up (from
start to finish, beginning to end) since nothing else will be running during that time."* And the same evening: *"once that's done, I'll need
you to draft whatever files/sheets/etc are required for Kunlun."*

> **Nothing in this file is Relung Panen's content.** It carries procedure and method lessons only. The session that writes it had Relung
> Panen's whole run in context, which is why **this run belongs to a fresh session** (one city run per fresh session): fresh readers do not
> isolate a run while the orchestrator writing their briefs has another city's run in mind.

---

## 0. What to do first, and the clock

### 0.1 How this run starts
- **A fresh session, given this file by the developer.** Run `date '+%Y-%m-%d %H:%M'`. Then:
  1. **Record the allotment reading** (§0.5) before anything else: ask the developer for the weekly-allotment figure shown at the start,
     and write it as the progress file's first line.
  2. Create the morning jobs (§7), report their IDs and next firing, log them, and keep the session open.
  3. **If the clock is inside 05:00–13:59, begin Section 1 at once.** Otherwise wait for the first job.

### 0.2 The cron prompt (word for word)
> It is a morning window for the Kunlun ULM run. First run `date '+%Y-%m-%d %H:%M'` to confirm the clock is inside the 05:00-14:59 operating
> window (do not start a new piece after 14:00; if outside the window, stop and say so). Then read in full
> `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Kunlun_ULM_2026-11-29.md`
> and follow it exactly. Read `RUN_PROGRESS_Kunlun.md` beside it if it exists and resume from the next unfinished piece; otherwise begin
> with Section 1, then Section 2. One piece at a time, each written to file and recorded before the next. Auto mode: do the work and ask
> only what blocks it. No commit, no push, never edit a pass file outside its own run, never compare any city with another, never declare
> anything complete, never start another city. When the window closes, update the progress file and the tracker, and give the developer
> a short plain-language summary of what ran, what is open, and what is next.

### 0.3 The window and the pace
- **Operating hours 05:00–14:59 only** for ULM work. **New units may start until 14:00**; 14:00–14:59 is the wrap-up (§8). A unit begun
  before 14:00 may finish in the wrap-up. If the window closes mid-unit, write a checkpoint into the progress file and stop. The developer's
  decision sessions may run at any hour; ULM work may not.
- **The progress file** is `Universal_Location_Methodology/RUN_PROGRESS_Kunlun.md` (append only). Create it with the allotment line.
- **Depth over speed (LAW 0).** Three Opus readers on every unit; never fewer readers, rounds or list items.

### 0.4 The web budget (method lessons, measured on the previous run)
- **1,000 web calls per session, shared by every agent.** Check it at every piece boundary with
  `python3 Tools/web_quota_count.py --tasks <this session's tasks folder>` (always pass `--tasks`).
- **The tool's count, not the readers' own counts, is what the limit enforces, and it reads higher** (measured: 643 against about 500
  logged; then +280 for a unit whose readers logged 189). **Set every reader's cap from the tool's remaining count**, with a reserve.
- **Above 850, start no research-heavy piece**: stop at the boundary and tell the developer a fresh session is needed.

### 0.5 The measurement (the developer's second purpose)
- **Nothing else runs during this run**, the DCI session included; if anything else is running, say so to the developer at once.
- **At the start and at the end,** ask the developer for the weekly-allotment reading and record both in the progress file, with the time.
- **The token log is `Universal_Location_Methodology/TOKEN_LOG_Kunlun.md`** (developer, 2026-11-18: *"During each step and or phase,
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
4. `DEVELOPER_RULINGS_LOG.md`: **the general rulings** (§4 below) **and every ruling naming Kunlun** (two name it in their headings,
  `DR-85` and `DR-94`; find the rest by a name search that prints line numbers only, then read those rulings). **In a ruling that holds
  several locations, read only its general items and Kunlun's items.** A ruling given for another city does not carry here unless the
  log records it for every city. **The rulings `DR-136` to `DR-141` hold two other cities' own items; read only their general items**
  (§4), and cut those rulings' other-location lines out of every reader's span.
5. Kunlun's pass folder, `Cities/City_Development_Passes/Mirny_Subnet/Kunlun/`: its `README.md` and `00.0_Pre-Trip_Inspection.md`. **It
  holds scaffolding only** (the Pre-Trip, the position ledger, the README and 19 datasheets; checked 2026-11-18 by name). There is **no**
  `Cities/Kunlun/` input-status folder.

## 2. The run
1. **Isolation first** (the first entry of Kunlun's research log and its run log): the session never opens another city's pass, culture,
   spec, personality or vision files. ⚠ **Kunlun's pass folder sits in the same subnet folder as two finished passes** (Casey's and Relung
   Panen's, under `City_Development_Passes/Mirny_Subnet/`): **never list, search or open those folders**, and never use a glob that reaches
   them. A relation from Kunlun's own lines (a road, a port, the subnet) is legal, taken only from Kunlun's lines and the shared things' own
   records (`DR-122` item 5, `DR-131` item 3, `DR-136` items 2–3).
2. **The memory bands** (the previous run's readiness check, 2026-11-18): thirteen memory files carry lines about Kunlun of a
   characterization, significance or vision-session shape, banded on 2026-11-18 with a line naming Kunlun. **Never open them during this
   run:** they are listed in this file's §9, and a line at the head of the memory index points there; copy the list into
   `RUN_PROGRESS_Kunlun.md`'s first lines when the run starts. The two Kunlun lines in the auto-loaded `MEMORY.md` index are attribute-only.
3. **Then a readiness check before Step −1** (one unit, recorded): **the sheets against the live sources**: `python3 Tools/build_pretrip.py
   Kunlun --out <scratch folder>` and compare with the Pre-Trip; `git log` on every source the Pre-Trip and datasheets cite. **Kunlun's
   Pre-Trip (2026-11-02) and datasheets (2026-10-30) predate every ruling from `DR-98` on:** list each later ruling's general items and
   Kunlun items that the Step −1 readers must carry. Never `--write`, never `--force`, never edit a tool. A stale figure is recorded and the
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
6. **Kunlun's own rulings** are in the log (§1 item 4). Open items go on Step 0.5's deferred list; they do not block.
7. **Not inputs:** the vision notes (`DR-10`, never an input and never a check); the megasheets (withheld); the city's own culture,
   robot-culture and personality files are read last, at Step 5's stage B, as a check, never as an input; the neo-race catalog, if one
   exists, is not an input at any step.
8. **Which source folders may ground a finding:** the inspiration picks, the `Infrastructure/` files and the city-relationship files, **for
   every city** (`DR-138` item 1); the picks are a full generator for every city (`DR-138` item 2).
9. **Symbols at Phase 10 only** (`DR-8`, `DR-8a`, `DR-115`): the symbol files are not opened before Phase 10, and their spans are chosen
   only after Phase 9 is recorded. **Cut every other city's pair out of every reader's span**, the rulings log's included: the previous run
   found another city's pair inside a general rulings span, read by every reader before the symbol determination.
10. **Research (LAW 0-R):** search, do not recall; every pick from more than one angle; a pick is not spent because it was searched once.
    Apply **independent convergence** (`DR-141` item 3; runbook L2620). The research log is `Cities/Research_Logs/Kunlun_Research_Log.md`
    (created by the run).
11. **When Step 10 is recorded:** the record files, a dated tracker line, **delete the cron jobs** (`CronDelete`), **the closing allotment
    reading and the token totals** (§0.5), and the developer's summary. **Kunlun is not declared complete;** that is the developer's call.
    **Start no other city.**

## 3. Binding rules
- **One location on its own terms.** Never compare Kunlun with any other city or use one as a baseline. Name no other location in a record
  ("(another location: not used)"), except a relation from the city's own lines.
- **Pass files are never edited** outside their own run (`DR-101`).
- **No forced fit:** an empty slot is a result ("none is sited here", never "none is possible here").
- **Never declare a run complete or ready.**
- **Questions** go to `Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`, each on its recommended answer, marked PROVISIONAL, in a new
  section for Kunlun inserted directly above `## Answered`, numbered from the next multiple of ten after the highest number in the file
  (check first: `grep -o 'DEC-[0-9]\+' <file> | sort -t- -k2 -n | tail -1`; it was **DEC-672** on 2026-11-18; another run may file more before this one starts, so always check).
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
The progress file records what happened, never what was found; **no reader is ever given it.** The recording-law log is Kunlun's
`09.5_Log.md`. A session cut off mid-unit resumes from the progress file and the readers' staging folders.

## 7. The morning jobs (05:02, one-shot)
- One-shot jobs, one per morning at 05:02 (`cron: "2 5 <day> <month> *"`, `recurring: false`, the §0.2 prompt word for word), **from
  2026-11-29 for seven mornings**, unless the developer gives other dates. Log every ID and its day.
- At every morning's close, run `CronList`; if fewer than three remain and the run is still going, ask the developer before adding more
  (the rest of that week belongs to the springboardings).
- When Step 10 is recorded, every remaining job is deleted.

## 8. Standing practice (developer, 2026-11-16)
*"During the productive hours (5:00am to 3:00pm, with the wrap-up beginning at 2:00pm), once one Step/Phase is complete, any and all
questions and/or decisions that you need from me, just log in the questions decisions file, and then continue with the next Step/Phase."*
**Never stop between units to report or wait;** questions go to the decisions file on their recommended answer, PROVISIONAL. Pre-build the
next units' lists and briefs while readers run, and report one short line per finished step.

## 9. The banded memory files (names only; never open them during this run)
In the memory folder (`/home/kuroskalacs/.claude/projects/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/memory/`), each carrying a line `CONTAMINATION BAND — KUNLUN` under its header (2026-11-18). From the previous run's readiness check (`Relung_Panen/10_Readiness_Check.md`, its memory list): the first six on all three readers' evidence; the next four on the stricter judgment; the last three left there for the developer and banded anyway, as the cautious reading.

1. `project_city_vision_notes.md`
2. `project_interwar_factions_expansion.md`
3. `project_dome_fuji_megasheet_pilot.md`
4. `project_byrd_dlc_enrichment_possibilities.md`
5. `project_kunlun_vostok_dlc_connection.md`
6. `project_kunlun_domefuji_population.md`
7. `project_sayowa_recheck_shirayuki_crossref.md`
8. `project_robot_religions_status.md`
9. `project_dlc_city_base_attributes_rollout.md`
10. `memory_unindexed_catalog.md`
11. `project_ice_cold_buddhism_research.md`
12. `project_larsemann_hills_demographic_rework.md`
13. `feedback_city_vision_notes_process.md`

**The previous check could not classify 29 lines** (prints refused by the permission system); a second classification is its REQ-289. A memory file that names Kunlun but is not listed here was classified attribute-only.
