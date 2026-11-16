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

---

## 0. What to do now, and the clock

### 0.1 How this run starts
- **The usual way: handover inside the Casey session.** When Casey's Step 10 is recorded, the session follows Casey's startup file
  Section 8 (added 2026-11-15): it replaces Casey's cron job with the job in 0.2 and, if the clock allows (0.3), begins this run the same
  morning.
- **If given to a fresh session instead:** do not start any work when you receive this file. Run `date '+%Y-%m-%d %H:%M'`; confirm on
  disk that Casey's Step 10 record exists (Casey's progress file, `RUN_PROGRESS_Mirny_Review_then_Casey.md`, ends with Step 10 recorded,
  and the Step 10 file is in Casey's folder). **If it does not, stop and tell the developer;** this run never starts before Casey's
  Step 10 is recorded. Otherwise create **one recurring cron job** with the prompt in 0.2, firing daily at 05:03 local time
  (`cron: "3 5 * * *"`, `recurring: true`), report its ID and next firing, and keep the session open.

### 0.2 The cron prompt (word for word)
> It is a morning window for the Relung Panen ULM run. First run `date '+%Y-%m-%d %H:%M'` to confirm the clock is inside the 05:00-14:59
> operating window (do not start a new piece after 13:30; if outside the window, stop and say so). Then read in full
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
1. **First, isolation (the first entry of Relung Panen's research log and Step 9.5 record):** if this run follows Casey's in the same
   session, Relung Panen is worked on its own terms **by fresh readers with clean briefs only**: no file, figure, verdict, tool output or
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
  unless Casey's Steps 5–10 add more).
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

## 7. Keep the cron job alive
- At every morning's close, and at the start of a morning whose last close was missed, run `CronList`. **A recurring job expires 7
  days after it is created. If the job is 6 or more days old, replace it:** create a new recurring job with the 0.2 prompt word for word
  (`cron: "3 5 * * *"`, `recurring: true`), delete the old one with `CronDelete` so only one exists, and log both IDs and the new job's
  creation time.
- **If the job or the session is gone:** the developer gives this file to a fresh session, Section 0.1 sets a new job, and the next
  firing resumes from the progress file. After a usage reset the developer can also resume at once by pasting the 0.2 prompt.
- When Relung Panen's Step 10 is recorded, the job is deleted (Section 2, item 10); log that too.
