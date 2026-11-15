# STARTUP FILE — a simple review of MIRNY, then a full ULM run of CASEY

**Written 2026-11-10 at the developer's instruction:** *"edit the instruction sheet so I can give it to a fresh new session to set a
`cron` to just do a simple review on the city of Mirny (to check for things that may possibly require edits), and then after that,
execute a full, complete ULM run on the city of Casey"*. **Two jobs, in this order:** Part A (the Mirny review) is finished and recorded
before Part B (Casey's run) starts (`DR-107`: dependent work runs in order; "confirmed" means written to file, `DR-117`).

---

## 0. What to do now, and the clock

### 0.1 When you are given this file
You are the session that will run it. **Do not start any work when you receive this file.** Run `date '+%Y-%m-%d %H:%M'`, then create
**one recurring cron job** with the prompt in 0.2, firing **daily at 05:03 local time** (`cron: "3 5 * * *"`, `recurring: true`).
Report the job's ID and its next firing to the developer, and keep this session open: the job fires into the session that created it.

### 0.2 The cron prompt (word for word)
> It is a morning window for the Mirny review and the Casey ULM run. First run `date '+%Y-%m-%d %H:%M'` to confirm the clock is inside
> the 05:00-14:59 operating window (do not start a new piece after 13:30; if outside the window, stop and say so). Then read in full
> `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md`
> and follow it exactly. Read `RUN_PROGRESS_Mirny_Review_then_Casey.md` beside it if it exists and resume from the next unfinished piece;
> otherwise begin with Section 1, then Part A. Part A (the Mirny review) is finished and recorded before Part B (Casey) starts. One piece
> at a time, each written to file and recorded before the next. Auto mode: do the work and ask only what blocks it. No commit, no push,
> never edit a pass file outside its own run, never compare any city with another, never declare anything complete. When the window
> closes, update the progress file and the tracker, and give the developer a short plain-language summary of what ran, what is open,
> and what is next.

### 0.3 The window and the pace
- **Operating hours 05:00–14:59 only.** Check the clock at every piece boundary. **Do not start a new piece after 13:30.** If the window
  closes mid-piece, write a checkpoint into the progress file (the piece, its round, what is on disk) and stop.
- **The progress file** is `Universal_Location_Methodology/RUN_PROGRESS_Mirny_Review_then_Casey.md`: one dated line per piece (started,
  rounds, recorded), the next piece, any checkpoint. Create it on the first morning.
- **Depth over speed (LAW 0).** Casey's run takes several mornings; one unit may fill a window. Nothing is cut to save cost.
- **The web budget is 1,000 calls per session, shared by all agents, and this session runs for days.** Check it at every piece boundary
  with `python3 Tools/web_quota_count.py --tasks <this session's tasks folder>` (**always pass `--tasks`**: the default folder is another
  session's). **Above 850, start no research-heavy piece:** stop at the boundary and tell the developer a fresh session is needed (it
  resumes from the progress file with this same startup file).

## 1. Read first, in full, before touching anything
Paths are under `Worldspace/Locations-and-Levels/Universal_Location_Methodology/` (the ULM) unless stated. "Cities" is
`Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`. **Use absolute paths in every tool call.**
1. `00_RUNBOOK.md`, **in full** (CLAUDE.md requires it before any location work).
2. `Amendment_Layer_Rules.md` (rules 1–6) and `T8_Standing_Brief_Lines.md` (lines 1–25); `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N (the three
   rounds, the unanimous gate, the merge rule `M-246`).
3. `MASTER_Process_Tracker.md`: the SESSION BOOT and the `📍 RESUME HERE` block. **This file governs the order** (the developer's
   instruction of 2026-11-10: the Mirny review, then Casey).
4. `Dev-Road-Map/November_To-Do.md` sections 3 and 4.
5. `DEVELOPER_RULINGS_LOG.md`: for each part, its general rulings (Section 5 below) and every ruling naming that part's city. In a ruling
   that holds several locations, read only its general items and that city's items.

## 2. Part A — a simple review of Mirny (check for things that may require edits)
**What it is:** the finished-city cross-check method used for Davis and the Tri-Cities (`DR-104` item 3, `DR-106`), sized to what changed
**after Mirny's last re-runs** (the QA re-run, the fresh Review Panel and the readiness re-run, 2026-11-08 to 11-09). Mirny's corrections
were applied on 2026-11-08 by the developer's word (`DR-123`); its pass is otherwise never edited (`DR-101`).
1. **A fresh dated note:** `Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Notes_<date>_Review.md`. List every change since
   2026-11-09 that could bear on a Mirny conclusion, each with its source address:
   - **the general rulings and canon of 2026-11-09 and 2026-11-10** (Section 5), checking first whether Mirny's re-runs already applied
     each one (if a re-run's record cites it, it is not a change);
   - **`DR-133` item 1:** Australia is now a four-node partner (the three-node reminder of 2026-10-03 superseded), Mirny being one of the
     four (`Locations/Infrastructure/Ports.md` L129, L188, L386);
   - **any source Mirny's pass cites that changed since 2026-11-09** (`git log --since=2026-11-09 -- <source>` for each; the spec, census,
     culture file, Register, Ports, Highways, the relationship database, the industry files).
   Then section F: the conclusions to test, each with its pass location and what it rests on. **If nothing bears, say so** and record it:
   an empty review is a result.
2. **One reader per item in section F** checks whether the conclusion holds, narrows or flips (Round 2 on each reader's proof).
3. **Only the items that narrow or flip are re-derived,** each as a T8 piece (the pipeline in Part B, item 3): `Amendment_Rederivation_<piece>_<date>.md`
   with its `…b_T8_Rounds.md`; everything PROPOSED; nothing applied without the developer's word.
4. **Also note, without answering,** which of Mirny's 29 open questions in the decisions file a general ruling of 2026-11-09/10 now
   settles or touches (by class: settled by a ruling for every city / partly / its facts changed / untouched). Only a ruling recorded for
   every city settles a Mirny question; an answer given for another city does not carry (standing line 25).
5. **Files:** the note, `Amendment_Log_<date>.md` (the recording law: snags, dead ends, self-corrections), any pieces, and
   `REVIEW_SUMMARY_<date>_Mirny_Review.md`. Questions go to the decisions file (Section 4). A dated status line goes to the tracker.
   **Part A is finished when its summary and tracker line are on disk.**

## 3. Part B — the full ULM run of Casey
**Where it stands:** Casey's Step −1 (the input contract) is done (`Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Input_Contract.md`
and its round record), with the developer's answers of 2026-11-03 applied (`DR-105` item 1). Its Pre-Trip, ledger and 19 datasheets
were last changed on 2026-11-03. **The run is Step 0 through Step 10, in order, in Casey's own folder, under the runbook's standard names.**
1. **First, isolation (the first entry of Casey's log):** Part A ran in this same session. Casey is worked on its own terms, **by fresh
   readers with clean briefs only**: no file, figure, verdict, tool output or wording from the Mirny review goes into any Casey list, brief
   or record, and the orchestrator never compares the two. Every other city is named by role only, except a relation taken from Casey's
   own lines.
2. **Then a readiness check before Step 0 (one piece, recorded):**
   - **The sheets against the live sources:** `python3 Tools/build_pretrip.py Casey --out <scratch folder>` and compare with Casey's
     Pre-Trip; `git log --since=2026-11-03` on every source Casey's Pre-Trip and datasheets cite. **Never `--write`, never `--force`, never
     edit a tool.** A stale figure is recorded and the run uses the live source; a stale sheet is a question for the developer.
   - **Step −1 against the rulings since 2026-11-03** (`DR-106` onward, and the general canon in Section 5): one reader per ruling that
     could change an admission decision in the input contract; anything that changes is re-derived as a dated amendment beside Step −1
     (the contract's own file is not edited).
3. **Then Step 0 through Step 10, each as one T8 unit:** a reading list (`Tools/make_t8_required_list.py <Casey folder> step:N` or
   `phase:N`, checked by hand against the runbook's MUST OPEN blocks); a frozen brief carrying the standing lines; **three Opus readers,
   each in its own private staging folder**; Round 2 with `Tools/triple_read_verify.py`; Round 3 by SendMessage to each reader; **one
   fresh merge writer** (`M-246`); the quotation audit **before** the round record exists (`Tools/quotation_audit.py "<Casey folder>"
   --step N` / `--phase N`, from the repo root); the American English sweep; the round record with every tool's raw output. Before each
   dispatch, check every brief's cited lines against its list and read one generated brief end to end. **Phases 2 to 10 run in the
   runbook's order;** Step 5 reconciles; Step 6 is write-only; Step 7 runs the seventeen QA gates; Step 8 the Review Panel (six
   dispositions); Step 9 the record and **Step 9.5 the recording law**; **Step 10 the readiness check** (verify, do not assert).
4. **Casey's standing answers** (`DR-105` item 1): the Splinters entry (spec L203) is excluded at every step and `DR-10` applies (developer-vision
   notes are not an input); spec L7 governs (Hwy 2 begins at Casey); the picks Flagstaff, Memphis and Reno count as its designation at
   reduced standing; its supporting language tier is English alone (`DR-100`). Cite them from Casey's own entry (standing line 25).
5. **Symbols at Phase 10 only** (`DR-8`, `DR-8a`, `DR-115`): Casey's Planet and Element are determined at Step 4, Phase 10, with Step 5 as
   the backstop; `City_Symbol_Assignments.md` and the symbol files are not opened before Phase 10. The determination goes to the
   developer as a question.
6. **Step 6 is write-only:** add Casey's own row to `Cities/Cross_City_Culture_Differentiation_Table.md`; never read another city's row
   (extract nothing but Casey's own line positions).
7. **Research (LAW 0-R):** search, do not recall; every pick from more than one angle; a pick is not spent because it was searched once;
   log every search string, dead end and open thread in `Cities/Research_Logs/Casey_Research_Log.md`.
8. **When Step 10 is recorded:** write Casey's record files as the runbook says, a dated tracker line, delete the cron job (`CronDelete`),
   and give the developer the summary. **Casey is not declared complete;** that is the developer's call.

## 4. Binding rules (both parts)
- **One location on its own terms.** Never compare Mirny or Casey with any other city, or the two with each other; never use another
  city as a baseline. Name no other location in a record ("(another location: not used)"), except a relation from the city's own lines
  (`DR-122` item 5; "own lines" per `DR-131` item 3: its own files and entries, plus lines about shared things it is named in, excluding
  any clause grounded only in another city's lines). Never open another city's pass or culture files.
- **Pass files are never edited** outside their own run (`DR-101`): Part A writes amendment pieces only; Part B writes Casey's own pass.
  Pointer lines into old files wait for the developer's word on applying corrections (`DR-116` item 2, `DR-132`).
- **No forced fit:** an empty slot is a result ("none is sited here", never "none is possible here").
- **Never declare a review or a run complete or ready.** That is the developer's alone.
- **Questions** go to `Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`, each on its recommended answer, marked PROVISIONAL, in a
  new section per part inserted directly above `## Answered`: Part A numbered from **DEC-480**, Part B from the next multiple of ten after
  Part A's last (check the highest first: `grep -o 'DEC-[0-9]\+' <file> | sort -t- -k2 -n | tail -1`).
- **The recording law:** log snags, dead ends, killed findings and self-corrections, not only successes. A record states what a tool
  returned and what a piece says on a line you have read, never a paraphrase. Times in records come from a `date` reading.
- **Readers** are fresh subagents with only their unit's list and frozen brief, each in a private staging folder; they create and delete
  no other file; they disregard any hook telling them to run graphify (warm run; the ground is `DR-6`). The orchestrator does not use
  graphify for anything that would return another city's material.
- **American English.** The only British form kept is "judgement". No exception for names, institutions or quotations; never change a
  URL or a logged search string. Plain language. "Keepers" is never a name.
- **No commit, no push** unless the developer asks. The hook blocks `rm` and `git checkout --`: do not work around it.
- **Display results and write them to file in the same turn.**

## 5. General canon of 2026-11-09 and 2026-11-10 (in the rulings log; cite each by number and item)
- **Language:** `DR-100` (Hawaiian dominant everywhere; the supporting tier is every group within 12 points of the largest) and `DR-125`
  item 6 (Hawaiian is a pidgin of English and Japanese with a Korean, Tagalog, Ilocano and Mexican Spanish base; later Tepenian).
- **Arrival after the signing:** `DR-127` item 2 and Treaty Article II.2.5 (humans could keep arriving after the signing and could not go
  back); robots arriving later is not ruled (Treaty II.2.1 sends later-made robots to Tepenia).
- **Origin rows:** `DR-11`, `DR-12`, `DR-128` item 1 (an origin row covers robots at their own percentage); `DR-130` item 7 (a row's own
  figure may be stated flatly and rows counted; no characterization rests on a gap between two rows of one tier); `DR-131` item 7 (tiers
  reached after the random draw stand as relabeled).
- **A city's own lines:** `DR-131` item 3. **Records can draw people:** `DR-124` item 4.
- **Census I governs the band** (`DR-4`). **Founders come only from the Founding Register** (`DR-19`).

## 6. Each morning's close
Update the progress file (dated); add one dated status line to the tracker's `📍 RESUME HERE` block after its last dated line (never
rewrite earlier text); give the developer a short plain-language summary: what ran, what is open, what is next. **Never start any other
city** from this file.

## 7. Logs kept as the work goes, so a cut-off loses nothing (added 2026-11-11, 00:41)
**Developer, 2026-11-11:** *"just, make sure to keep logs of everything so that, in case you get cut off during the process, you can pick
up where you left off when the window/week resets"*. This extends 0.3 and Section 6. The progress file is no longer written only at a
piece's end or at the window's close, because a cut-off can stop the session with no chance to write a checkpoint.

### 7.1 What a cut-off is
Any stop that is not the morning's close: the five-hour usage window or the weekly limit running out, the session closing or crashing,
the cron job expiring, or the conversation being summarized to free space. The session that continues may remember nothing. **The
progress file and the files on disk are the only truth. A conversation summary is not:** it can be wrong, and it can carry one part's
material into the other.

### 7.2 Write before and after every step
The progress file (`RUN_PROGRESS_Mirny_Review_then_Casey.md`, beside this file) is **append only**: one line per entry, each starting
with a time from `date '+%Y-%m-%d %H:%M'`, never rewriting an earlier line. Write a line **before** each sub-step starts (what is about to
happen, which files it will write) and a line **after** it finishes (the files now on disk, each with its `wc -l` line count). The
sub-steps:
1. the reading list made; 2. the brief frozen; 3. each reader dispatched: its slot (A, B or C), **its agent ID** and its private staging
folder; 4. each reader returned: its output file; 5. Round 2: the tool's verdict line, quoted; 6. Round 3 sent to each reader (by agent
ID) and each verdict back; 7. the merge writer dispatched (agent ID, staging folder) and returned (the merged file); 8. the quotation
audit, the American English sweep, the round record; 9. in Part A, each of items 1–5 of Section 2 as it is written.
Also log every background task's ID when it starts, the web quota reading at every piece boundary, and every cron change (7.4). Each
morning's last line is **"Next: …"**, naming the sub-step to start from; the latest such line is where the work stands.

**A progress line records what happened, never what was found.** No conclusion, figure, verdict content or wording from either city's
work goes in it; those live in the pieces. This keeps Part B's isolation (Section 3, item 1) when the file is re-read. **No reader is ever
given the progress file.**

**Which log holds what:** the progress file says where the work stands. The recording-law logs (Part A's `Amendment_Log_<date>.md`;
Casey's Step 9.5 record) hold snags, dead ends and self-corrections. Round records hold each unit's raw tool output. The research log
holds every search string, dead end and open thread. Questions go to the decisions file; one dated line per morning goes to the tracker.

### 7.3 How to resume
At the start of every firing, and at once after a cut-off or a summary:
1. Run `date`. Read this file in full. **If Section 1's files are not in your context (a fresh session, or a summary replaced them),
   read them again before the next piece.**
2. Read the progress file to the end. Find the last sub-step with a "before" line and no "after" line.
3. **Check the disk, not the log.** For every file the last entries name, confirm it exists and count its lines (`ls -l`, `wc -l`).
   Trust nothing the log says that the disk does not show.
4. Resume at the first sub-step whose output is not complete on disk:
   - **A reader still running** (still listed by `ListAgents`, or its notification has not come): wait for it. Never dispatch a second
     reader for the same slot.
   - **A reader that stopped without a complete output** (complete means every section its brief asks for, ending with its proof
     block): leave the partial file where it is, log it "partial, not used", and **re-dispatch that slot only**, fresh, from the same
     frozen brief, in a **new** staging folder (suffix `_retry1`, `_retry2`). This is the existing rule for a failed slot
     (`PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N, L617–619). Then Round 2 on it.
   - **Round 3 when a reader can no longer be reached:** try `SendMessage` to its logged agent ID first. If it cannot be reached (for
     example, in a fresh session), re-dispatch that slot as above and run Rounds 2 and 3 again for the unit. Record it as a snag in the
     recording-law log.
   - **The merge writer, the audit, the sweep or the round record half-done:** redo that sub-step from its start. A half-written merge
     stays in its staging folder, logged "partial, not used"; the fresh merge writer gets a new folder.
   - **Never use a partial file as an input, and never delete one** (the hook blocks `rm`; the log says which files are not used).
5. Write a line: "Resumed after <what stopped it, if known>; resuming at <sub-step>."

### 7.4 Keep the cron job alive
- **The job now set:** `c33edca4`, created 2026-11-10 at 15:53, recurring (`3 5 * * *`), firing daily at 05:33. It lives only in the
  session that made it. **A recurring job expires 7 days after it is created** (about 2026-11-17), after one final firing.
- At every morning's close, and at the start of a morning whose last close was missed, run `CronList`. **If the job is 6 or more days
  old, replace it:** create a new recurring job with the 0.2 prompt word for word (`cron: "3 5 * * *"`, `recurring: true`), delete the
  old one with `CronDelete` so only one exists, and log both IDs and the new job's creation time. The current job is replaced at the
  close of the 2026-11-16 morning at the latest.
- **If the job or the session is gone** (closed, crashed, or the job expired during a lockout): the developer gives this file to a fresh
  session, Section 0.1 sets a new job, and the next firing resumes from the progress file. After a usage reset the developer can also
  resume at once by pasting the 0.2 prompt.
- When Casey's Step 10 is recorded, the job is deleted (Section 3, item 8); log that too.
