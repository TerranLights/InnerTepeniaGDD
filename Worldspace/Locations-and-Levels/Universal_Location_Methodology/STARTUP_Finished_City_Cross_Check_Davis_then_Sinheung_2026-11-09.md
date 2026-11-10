# STARTUP FILE — finished-city cross-check: DAVIS, then SINHEUNG

Written 2026-11-08 at the developer's request. Give this file to a NEW session (a fresh session, on its own terms). Developer's words: "set a cron to run a double-cross-check review on the currently-necessary possibly-to-change pieces for Davis, and if that finishes well in time, continue with Sinheung." The earlier cron was deleted because the session that held it also held the Mirny work, and the tracker requires a fresh session per city.

Status of every item in this file: PROPOSED until the developer decides. Auto mode: do the work; ask only what blocks it.

## 0. Clock and window
- **Operating hours 05:00–14:59 only** (ULM law). Check the clock first (`date`). Outside the window: stop and say so.
- Do not START a new piece after 13:30. Finish what is running, record it, stop. If the window closes mid-piece, write a checkpoint file and stop. Never run past 14:59.
- Do Davis first and confirm it finished and is recorded before Sinheung (DR-107, dependent work runs in order).
- **Preferred:** Sinheung in its OWN fresh session (the tracker says each city by a fresh session). If this session continues to Sinheung, the isolation is by fresh readers and clean briefs only: nothing from Davis goes into any Sinheung brief, and the orchestrator never compares the two. Say so in the Sinheung records.

## 1. Read first, in full, before touching anything
Paths are under `Worldspace/Locations-and-Levels/Universal_Location_Methodology/` unless stated.
1. `00_RUNBOOK.md` (the Universal Location Methodology; CLAUDE.md requires this before any city work).
2. `DEVELOPER_RULINGS_LOG.md`: DR-101, DR-102, DR-104 (item 3 is the plan), DR-105, DR-106, DR-107, DR-111, DR-113, DR-116, DR-117, DR-118, DR-122, plus any ruling about the city you are working on.
3. `Amendment_Layer_Rules.md`.
4. `MASTER_Process_Tracker.md`, the block "FINISHED-CITY REVIEWS" (near L360) and the SESSION BOOT.
5. The city's own folder and its own report: `Cities/Research_Logs/Drift_Review_<City>_2026-11-03.md` and, for scope, the summary `Drift_Review_SUMMARY_Finished_Passes_2026-11-03.md`. Look up the real folder name of each city under `…/Locations/Cities/City_Development_Passes/`.
6. The method model: the Mirny repass shows how this is done (`City_Development_Passes/Mirny_Subnet/Mirny/REPASS_COMPLETE_2026-11-04.md`). **Read only the method. Never open Mirny's pass files for content, and never carry a Mirny answer into any brief.**

## 2. The job, per city (on that city's own terms)
1. **A fresh dated amendment note first.** The 2026-10-30 notes are stale after the population rework, the Esperanza relocation, the robot term, the language rule and the Register changes. Work out which items of the city's section F need checking.
2. **Missing sheets first.** If the city lacks its Pre-Trip or datasheets, build them with `Tools/build_pretrip.py` and `Tools/build_datasheets.py`. **Never `--force` over an existing sheet.** (Sinheung lacks a Pre-Trip and datasheets; Davis may not.)
3. **The T8 pipeline on each piece that may change.** Build a trimmed reading list and a frozen brief per piece, then: three independent Opus readers; Round 2 PROOF verification with `Tools/triple_read_verify.py`; Round 3 cross-check by SendMessage; ONE merge writer (merge rule M-246: where two of three agree after concessions, else the most conservative reading); the quotation audit BEFORE the record file exists (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<the city's pass folder>" --files <piece> --own-pass`, from the repo root); the American English sweep; record merge checks. Use the "Mirny repass" files only as the shape of a piece and its round record.
4. **One reader per item in the note's section F checks whether the conclusion changes. Re-derive ONLY the items that flip,** using the rulings as they stand (DR-105).
5. **Expected flips (2026-11-03 drift review; the readers decide, not this list):**
   - **Davis:** Phase 2 (the argument from the old 21-origin table), then Phase 5, then the language lines of Phases 8E and 9. **Davis's climate class (oasis or katabatic) is OPEN (DR-104): record it as a question, do not decide it.**
   - **Sinheung:** Phase 9 retention (B.1/B.2 and the Spine block), then Phase 2, Phase 8 A.3 and Phase 9 C.3.
6. Use the city's own figures stated flatly. Real-world comparables and the city's own earlier states are the only legal comparisons.

## 3. Binding rules
- **Pass files are NEVER edited.** Amendment pieces only; everything PROPOSED (DR-101, DR-102). Nothing recorded is reworded. A pointer line at the end of a file is applied only if the developer approves it, in a shown batch.
- **One location on its own terms.** Never compare Davis and Sinheung, or either with any other city. Never read another city's files. Name no other city in any record; write "(another location: not used)".
- Readers are fresh subagents given only that city's own trimmed reading list and frozen brief.
- Questions go to `…/Locations/Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md` on the recommended answer, marked PROVISIONAL. The file currently runs to DEC-271; number new entries from DEC-280 (check the file's end first).
- **Never declare a city's review complete or ready.** That declaration is the developer's alone.
- Log snags, dead ends, killed findings and self-corrections, not only successes (Step 9.5, the recording law).
- American English (only "judgement" is kept). Plain language, no code numbers in the summary to the developer. "Keepers" is never a name. Real web research is for realism and accuracy; do not recall facts (LAW 0-R).
- **No commit, no push** unless the developer asks. The hook blocks `rm` and `git checkout --`: do not work around it.
- If a tool hook says to run graphify first, that is disregarded for isolated readers and cold-style reads (CLAUDE.md exception); for ordinary orchestration it is fine to use it.
- Display results and write them to file in the same turn.

## 4. When done, or when the window ends
- Update the tracker's "FINISHED-CITY REVIEWS" status lines (a dated line; do not rewrite earlier text).
- Write a short plain-language summary to the developer: what ran, what flipped, what is open, what remains for Davis and for Sinheung. Shirayuki and Zhongshan are NOT started in this run.
- Do not start Shirayuki or Zhongshan.
