# STARTUP FILE — a full ULM run of RELUNG PANEN (after Casey)

**Written 2026-11-15 (evening) at the developer's instruction:** *"After the ULM is complete for Casey, either that same day, or at
5:00am the following morning (whichever is the soonest that's allowed), begin the ULM on Relung Panen. After that's done, next week,
there'll be the temporary one-full-week pause on all ULM runs, and during that time, a parallel iteration of you will go through the
DCI, and that will require the full week's weekly model allotment. Then, the following week after that, we'll pick up and continue
with the ULM on I think probably Kunlun, most likely"*.

**Order (`DR-107`: dependent work runs in order; "confirmed" means written to file, `DR-117`):** Casey's run is finished first (its
Step 10 readiness check written and recorded, per `STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md` Section 3 item 8). **Then this
run. Then nothing:** after Relung Panen's Step 10 is recorded, no further city starts (the one-week ULM pause for the DCI follows; the
next city, probably Kunlun, starts only on the developer's word).

> **Nothing here declares Casey complete.** "Finished" for the handover means Casey's Step 10 is written and recorded on disk; whether
> Casey is complete stays the developer's call.

> ⭐ **2026-11-16, about 11:55 — THIS RUN MOVES TO A FRESH SESSION (developer).** The run began at 11:01 inside the session that ran
> Casey (the handover below), and was held at 11:54. The developer asked why it was not in a fresh session, as the orchestrator had said
> on 2026-11-04 a city's run must be: **fresh readers do not isolate the run while the orchestrator who writes their lists, briefs and
> merge rules has another city's whole run in context.** The first sign of it is recorded (Relung Panen's run log RL-06: a merge rule
> the orchestrator stated from memory decided a split). **From here the run belongs to a fresh session that has never read Casey's
> pass.** Start at **Section 0.4** below, which comes before everything else in this file.

---

## 0. What to do now, and the clock

### 0.1 How this run starts
- ~~**The usual way: handover inside the Casey session.**~~ *Used on 2026-11-16 at 11:01, then withdrawn by the developer at about
  11:55 (the note above Section 0). Kept as history.*
- **Now: a fresh session.** When you receive this file, run `date '+%Y-%m-%d %H:%M'`. Casey's Step 10 was recorded at 11:00 on
  2026-11-16 (`RUN_PROGRESS_Mirny_Review_then_Casey.md` ends with it); check that line only, **open nothing else of Casey's.** Then:
  1. Create the morning jobs as Section 7 says (one-shot jobs at 05:02, **2026-11-17 to 2026-11-21 only**), report their IDs and next
     firing, log them in the progress file, and keep the session open. (The Casey session's jobs for those mornings were deleted at
     the move.)
  2. **If the clock is inside 05:00–13:59, begin Section 0.4 at once,** under Section 8's standing practice. Otherwise wait for the
     first job.

### 0.2 The cron prompt (word for word)
> It is a morning window for the Relung Panen ULM run. First run `date '+%Y-%m-%d %H:%M'` to confirm the clock is inside the 05:00-14:59
> operating window (do not start a new piece after 14:00; if outside the window, stop and say so). Then read in full
> `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Relung_Panen_ULM_2026-11-15.md`
> and follow it exactly. Read `RUN_PROGRESS_Relung_Panen.md` beside it if it exists and resume from the next unfinished piece; otherwise
> begin with Section 1, then Section 2. One piece at a time, each written to file and recorded before the next. Auto mode: do the work
> and ask only what blocks it. No commit, no push, never edit a pass file outside its own run, never compare any city with another, never
> declare anything complete, never start another city. When the window closes, update the progress file and the tracker, and give the
> developer a short plain-language summary of what ran, what is open, and what is next.

### 0.3 The window and the pace
- **Operating hours 05:00–14:59 only.** Check the clock at every piece boundary. **Do not start a new piece after 13:30.** If the window
  closes mid-piece, write a checkpoint into the progress file and stop.
- **The same-day start:** if Casey's Step 10 is recorded before 13:30, the first piece here (Section 2, item 1) starts that same morning.
  If it is recorded at 13:30 or later, this run starts at the next morning's window. Edits and the developer's decision sessions may
  still run at any hour (`DR-117` item 4); ULM work may not.
- **The progress file** is `Universal_Location_Methodology/RUN_PROGRESS_Relung_Panen.md` (append only; Section 7). Create it with the
  first piece.
- **Depth over speed (LAW 0).** Nothing is cut to save cost. Three Opus readers on every unit (the November setup, 2026-10-21); never
  fewer readers, rounds or list items.
- **The web budget is 1,000 calls per session, shared by all agents.** Check it at every piece boundary with
  `python3 Tools/web_quota_count.py --tasks <this session's tasks folder>` (**always pass `--tasks`**). **If this run starts in the
  session that ran Casey, the count already holds Casey's calls.** **Above 850, start no research-heavy piece:** stop at the boundary
  and tell the developer a fresh session is needed (it resumes from the progress file with this same startup file).

### 0.4 Where the run stands at the move, and what the fresh session does first
**Read Section 1 in full first, then this.** Everything below is in Relung Panen's pass folder
(`Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/`) or beside this file; the progress file and the run log (`09.5_Log.md`,
entries RL-01 to RL-06) have the times and agent IDs.

**What exists:**
- **The readiness check before Step −1: written and recorded.** `00.0b_Readiness_Check_2026-11-16.md` (257 lines) and its round record
  `00.0c_T8_Rounds_Readiness.md` (151 lines). Verdict READY FOR STEP −1. Its nine questions are filed as **DEC-564 to DEC-572** in a new
  Relung Panen section of the decisions file (DEC-567 carries an orchestrator note: the held `DR-95`/`DR-96` edits appear to have been
  applied on 2026-11-03, commit `612fdc4c`).
- **Step −1 (the input contract): written, NOT recorded.** Three readers, Round 2 UNANIMOUS, Round 3 all six CONSISTENT, one merge:
  `00.1_Step_MINUS-1_Input_Contract.md` (442 lines). **No close checks, no round record, its developer questions (its DQ-10 to DQ-14) not
  filed.** Its list, briefs, reader outputs, Round 2 output and Round 3 replies are the `.t8_00.1_*` files.
- **Two orchestrator findings to carry:** RL-03 (the readiness list left out rulings from `DR-98` on; five, `DR-105`, `DR-114`, `DR-115`,
  `DR-117` and `DR-121`, were added to Step −1's rulings spans after a name search that cannot prove the rest carry nothing general);
  RL-05 (the first git-log check gave a date with no time and missed three commits; the corrected run is
  `.t8_00_git_log_since_1103_0000_raw.txt`, meant for Step 0's list).
- **Nothing else.** Steps 0 to 10 are not started. The old session drafted Step 0 and Step 1 materials in its own scratch folder:
  **do not look for them or use them.**

**What the fresh session does first, in order (`DR-107`), each step written to the run log before the next:**
1. **Audit the inherited orchestrator work for Casey material.** Read, end to end, every brief and merge brief the old session wrote
   (`.t8_00_readiness_brief_A.md`, `.t8_00_readiness_merge_brief.md`, `.t8_00.1_Step_MINUS-1_brief_A.md`,
   `.t8_00.1_Step_MINUS-1_merge_brief.md`; briefs B and C differ from A only in reader letter and paths) and both reading lists. **Look for
   anything that came from Casey's run** (a finding, figure, verdict, wording or rule stated from memory), as opposed to Relung Panen's own
   lines, the rulings log, and the method files. The old session found these mentions of Casey, and judged them legal: "never open Casey's
   files"; rulings named by number (`DEC-003` was ruled for Casey only, `DR-136` item 4); and one method note from Casey's Step 10, that
   the runbook's §C.6 row for Relung Panen's old placeholder (L1646) is superseded (`DEC-563`). **Check that judgment yourself.** If you
   find Casey material that could have shaped a result, re-run that unit from a brief you write.
2. **Settle Step −1's split 1** (RL-06; the merge file's own split 1 and Snags). The old session's merge brief said: *"Population-origin
   material is DEMOTED, never excluded (runbook §C.9c)."* That was stated from memory; §C.9c was not on the merge writer's list. Under it,
   the merge demoted spec L39–42, L45–51 and L94–98, which all three readers had excluded. **Read runbook §C.9 (b–e) yourself.** If the
   wording was right, keep the merge. If it was wrong or broader than §C.9c, write your own merge brief and run a fresh merge writer;
   first keep the old file with `mv` to `00.1_Step_MINUS-1_Input_Contract_merge1_superseded.md` (never delete; the hook blocks
   overwrites), and record both.
3. **Close Step −1:** the quotation pre-check and `Tools/quotation_audit.py --own-pass`, the American English sweep, the round record
   `00.1b_T8_Rounds_Step_MINUS-1.md` with every tool's raw output pasted whole, and its developer questions filed from **DEC-573**.
   Write your own scripts for these; the old session's were in its scratch folder.
4. **Then Step 0, and on through Step 10,** as Section 2 item 3 says, building every list and brief yourself.

## 1. Read first, in full, before touching anything
Paths are under `Worldspace/Locations-and-Levels/Universal_Location_Methodology/` (the ULM) unless stated. "Cities" is
`Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`. **Use absolute paths in every tool call.**
1. `00_RUNBOOK.md`, **in full** (CLAUDE.md requires it before any location work). **Re-read it even if Casey's run read it**: Casey's
   rulings amended it (`DR-137` item 10, the 5b row).
2. `Amendment_Layer_Rules.md` (rules 1–6) and `T8_Standing_Brief_Lines.md` (lines 1–25); `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N (the three
   rounds, the unanimous gate, the merge rule `M-246`).
3. `MASTER_Process_Tracker.md`: the SESSION BOOT and the `📍 RESUME HERE` block.
4. `Dev-Road-Map/November_To-Do.md` (at the repo root, not under the ULM) sections 3 and 4.
5. `DEVELOPER_RULINGS_LOG.md`: the general rulings in Section 5 below, and **every ruling naming Relung Panen or its former placeholder
   names** (Bunger Hills City, Bunger Hills; renamed under `DR-39`). In a ruling that holds several locations, read only its general items
   and Relung Panen's items. **A ruling or answer given for Casey or any other city does not carry here** (standing line 25), unless the
   log records it for every city.
6. `Cities/Relung_Panen/ULM_Input_Status.md`, **the block at its end** (the current state of the inputs, 2026-11-02), and Relung Panen's
   pass README, `Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/README.md`.

## 2. The run
**Where it stands:** Relung Panen's pass folder (`Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/`) holds the Pre-Trip, the
Position-Coverage ledger and 19 datasheets (inputs, not output; last changed 2026-11-03, `a2b55eb4`; the Step 3 sheet copies all 99
picks, `63277e9b`). **No pass file exists yet: the run is Step −1 through Step 10, in order, in that folder, under the runbook's
standard names** (the README's table lists them). Checked 2026-11-15 by tool: `audit_city_inputs.py --city Relung_Panen` 40 tests,
0 gaps, 3 notes; `verify_city_sheets.py Relung_Panen` 20 checks, 0 FAIL, 2 NOTE (the city key is `Relung_Panen`, case as written).
1. **First, isolation (the first entry of Relung Panen's research log and Step 9.5 record):** *since 2026-11-16 ~11:55 the run has its
   own session (the note above Section 0); the session never opens Casey's pass, Casey's run log or the Casey session's transcript or
   scratch folder.* In any session, Relung Panen is worked on its own terms **by fresh readers with clean briefs only**: no file, figure, verdict, tool output or
   wording from Casey's run goes into any Relung Panen list, brief or record, and the orchestrator never compares the two. **Casey is
   named in Relung Panen's own lines** (the road spur from Hwy 110, Casey's port for bulk goods, a possible grid line from Casey): those
   are relations, taken only from Relung Panen's own lines and from the shared things' own records (`DR-122` item 5, `DR-131` item 3,
   `DR-136` item 2), never from Casey's pass. **Never open Casey's pass, culture or vision files during this run.**
2. **Then a readiness check before Step −1 (one piece, recorded):**
   - **The sheets against the live sources:** `python3 Tools/build_pretrip.py Relung_Panen --out <scratch folder>` and compare with the
     Pre-Trip; `git log --since=2026-11-03` on every source the Pre-Trip and datasheets cite. **Never `--write`, never `--force`, never
     edit a tool.** A stale figure is recorded and the run uses the live source; a stale sheet is a question for the developer.
   - **The rulings since 2026-11-03** (`DR-98` to the latest): note each general item and each Relung Panen item the Step −1 readers must
     carry (cite by number and item).
3. **Then Step −1 (the input contract), Step 0 (with Step 0.5's deferred list) and Steps 1 to 10, each as one T8 unit:** a reading list
   (`Tools/make_t8_required_list.py <Relung Panen folder> step:N` or `phase:N`, checked by hand against the runbook's MUST OPEN blocks); a
   frozen brief carrying the standing lines; **three Opus readers, each in its own private staging folder**; Round 2 with
   `Tools/triple_read_verify.py`; Round 3 by SendMessage to each reader; **one fresh merge writer** (`M-246`); the quotation audit
   **before** the round record exists (`Tools/quotation_audit.py "<Relung Panen folder>" --step N` / `--phase N`, from the repo root); the
   American English sweep; the round record with every tool's raw output. Before each dispatch, check every brief's cited lines against
   its list and read one generated brief end to end. **Phases 2 to 10 run in the runbook's order;** Step 5 reconciles (its two-stage
   set-up, the strongest-finding leg named before the city's own culture files are opened, `M-271`); Step 6 is write-only; Step 7 runs
   the seventeen QA gates; Step 8 the Review Panel (six dispositions); Step 9 the record and **Step 9.5 the recording law**; **Step 10
   the readiness check** (verify, do not assert).
4. **Relung Panen's own rulings** are in the log (Section 1, item 5). Those already known: the name (`DR-39`); founders Indonesia and
   Malaysia jointly (`DR-34`, Founding Register); settled shortly after the 2564 signing (`DR-61`); population and density (`DR-68`,
   `DR-85`, `DR-90`, `DR-93`); the industry row (`DR-71` to `DR-75`, `DR-96` item 5, `DR-97`); the airports, the winter intake and the
   sea gateway (`DR-81`, `DR-82`, `DR-95`, `DR-96` items 1, 2 and 6); no berth of its own, bulk by road through Casey's port (`DR-96`
   item 3); power sized, plant and route open (`DR-96` item 4). **The open items go on Step 0.5's deferred list; they do not block**
   (the input status file's 2026-10-26 section: open rulings are listed at the head of the pass, and `DR-16`: no founding history is
   built in-run).
5. **Not inputs:** the vision notes (`DR-10`); the megasheets (withheld); the city's own culture stubs are read last, at Step 5, as a
   check, never as an input. The Pre-Trip (L417–L431) classifies the other files in `Cities/Relung_Panen/`; follow it and Step −1.
6. **Which source folders may ground a finding (`DEC-003`):** `DR-136` item 4 made the inspiration picks, the `Infrastructure/` files
   and the city-relationship files usable **for Casey only**; `DEC-003` stays deferred for every other city. **If the developer has not
   ruled on it for Relung Panen before Step −1, file it as a question on its recommended answer (the same as Casey's), PROVISIONAL, and
   proceed on that answer, tagging each dependent finding.**
7. **Symbols at Phase 10 only** (`DR-8`, `DR-8a`, `DR-115`): `City_Symbol_Assignments.md` and the symbol files are not opened before
   Phase 10. The determination goes to the developer as a question.
8. **Step 6 is write-only:** add Relung Panen's own row to `Cities/Cross_City_Culture_Differentiation_Table.md`; never read another
   city's row.
9. **Research (LAW 0-R):** search, do not recall; every pick from more than one angle; a pick is not spent because it was searched once.
   The research log is `Cities/Research_Logs/Relung_Panen_Research_Log.md` (it does not exist yet; the run creates it). The many dated
   Relung Panen research files already in `Research_Logs/` are earlier input research; Step −1 decides how each is admitted.
10. **When Step 10 is recorded:** write the record files as the runbook says, a dated tracker line, **delete the cron job**
    (`CronDelete`), and give the developer the summary. **Relung Panen is not declared complete;** that is the developer's call. **Start
    no other city:** the one-week ULM pause for the DCI follows, and the next run (probably Kunlun) waits for the developer.

## 3. Binding rules
- **One location on its own terms.** Never compare Relung Panen with any other city or use one as a baseline. Name no other location in
  a record ("(another location: not used)"), except a relation from the city's own lines (`DR-122` item 5; "own lines" per `DR-131`
  item 3, and the subnet as a shared thing per `DR-136` item 3). Never open another city's pass or culture files.
- **Pass files are never edited** outside their own run (`DR-101`).
- **No forced fit:** an empty slot is a result ("none is sited here", never "none is possible here").
- **Never declare a run complete or ready.** That is the developer's alone.
- **Questions** go to `Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`, each on its recommended answer, marked PROVISIONAL, in a
  new section for Relung Panen inserted directly above `## Answered`, numbered from the next multiple of ten after the highest number in
  the file (check first: `grep -o 'DEC-[0-9]\+' <file> | sort -t- -k2 -n | tail -1`; it was `DEC-544` on 2026-11-15, so **DEC-550**
  unless Casey's Steps 5–10 add more). *Update 2026-11-16: the Relung Panen section exists (heading "Open since 2026-11-16 (Relung Panen
  ULM run …)", DEC-564 to DEC-572); add to it, continuing from **DEC-573**.*
- **The recording law:** log snags, dead ends, killed findings and self-corrections, not only successes. A record states what a tool
  returned and what a piece says on a line you have read, never a paraphrase. Times in records come from a `date` reading.
- **Readers** are fresh subagents with only their unit's list and frozen brief, each in a private staging folder; they create and delete
  no other file; they disregard any hook telling them to run graphify (warm run; the ground is `DR-6`). The orchestrator does not use
  graphify for anything that would return another city's material.
- **American English.** The only British form kept is "judgement". No exception for names, institutions or quotations; never change a
  URL or a logged search string. Plain language. "Keepers" is never a name.
- **No commit, no push** unless the developer asks. The hook blocks `rm` and `git checkout --`: do not work around it.
- **Display results and write them to file in the same turn.**

## 4. General canon to carry (in the rulings log; cite each by number and item)
- **Language:** `DR-100` (Hawaiian dominant everywhere; the supporting tier is every group within 12 points of the largest; the city's
  own row is in its `Step_0` datasheet) and `DR-125` item 6, national by `DR-136` item 1. Languages outside the supporting tier: not yet
  stated nationally (`DR-136` item 8); ask only what lies outside the tier at Relung Panen.
- **Arrival after the signing:** `DR-127` item 2 and Treaty Article II.2.5.
- **Origin rows:** `DR-11`, `DR-12`, `DR-128` item 1, `DR-130` item 7, `DR-131` item 7. **Robot ancestry:** `DR-136` item 10 (its general
  sentences) and `DR-137` item 7.
- **A city's own lines:** `DR-131` item 3, `DR-136` items 2 and 3. **Records can draw people:** `DR-124` item 4.
- **A pass captures a place at its height:** `DR-136` item 6; `DR-137` item 10 (the peak first; an overall average where there were
  several peaks).
- **Government and justice wait for the DCI:** `DR-137` item 11. No pass writes a city's government form or its justice, law or law
  enforcement; it writes only where decisions fall and who is present.
- **The day's structure, the workforce convention, "dispatcher":** `DR-137` items 8, 9 and 12.
- **Robots:** `DR-137` items 2 to 6 (senses lean to place, a charging robot dreams and flight mode, cold death settled in part, siligel
  mined then processed and exothermic, the long-life tier); full wording at the end of
  `Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md`.
- **Census I governs the band** (`DR-4`). **Founders come only from the Founding Register** (`DR-19`).

## 5. Each morning's close
Update the progress file (dated); add one dated status line to the tracker's `📍 RESUME HERE` block after its last dated line (never
rewrite earlier text); give the developer a short plain-language summary: what ran, what is open, what is next. **Never start any other
city** from this file.

## 6. Logs, cut-offs and resuming
Casey's startup file Section 7 (7.1 to 7.3) applies here word for word, with these names: the progress file is
`RUN_PROGRESS_Relung_Panen.md`; the recording-law log is Relung Panen's Step 9.5 record; the research log is
`Relung_Panen_Research_Log.md`. **A progress line records what happened, never what was found. No reader is ever given the progress
file.** Reading Casey's startup file for its Section 7 procedure is allowed; it holds no Casey findings.

## 7. The morning jobs (start time 05:02, exactly)
- **Developer, 2026-11-16: *"I wanted it to start at 5:02am."*** A recurring job runs late by a fixed offset of up to 30 minutes, so
  this run uses **one-shot jobs, one per morning at 05:02** (`cron: "2 5 <day> <month> *"`, `recurring: false`, the 0.2 prompt word for
  word). Create them for the next seven mornings at the handover, and log every ID and its day in the progress file.
- At every morning's close, run `CronList`. **If fewer than three mornings remain scheduled, add the next seven the same way.**
  One-shot jobs do not expire, so there is nothing else to renew. Only this run's jobs may exist; Casey's are deleted at the handover.
- ⛔ **No job on or after 2026-11-22 until the developer says the DCI week is over** (developer, 2026-11-16: the windows from the
  22nd on are cancelled for the DCI lead-sheets). If this run is still going on 2026-11-21, it stops at that window's close with a
  checkpoint and resumes after the pause, on the developer's word.
- **If the job or the session is gone:** the developer gives this file to a fresh session, Section 0.1 sets a new job, and the next
  firing resumes from the progress file. After a usage reset the developer can also resume at once by pasting the 0.2 prompt.
- When Relung Panen's Step 10 is recorded, every remaining job is deleted (Section 2, item 10); log that too.

## 8. Standing practice (added 2026-11-16, developer)
*"During the productive hours (5:00am to 3:00pm, with the wrap-up beginning at 2:00pm), once one Step/Phase is complete, any and all questions and/or decisions that you need from me, just log in the questions decisions file, and then continue with the next Step/Phase."* **Never stop between units to report or wait;** questions go to the decisions file on their recommended answer, PROVISIONAL. **New units may start until 14:00** (this replaces the 13:30 in 0.2 and 0.3); 14:00–14:59 is the wrap-up. Pre-build the next units' lists and briefs, prepare the next unit while readers run, and report one short line per finished step.
