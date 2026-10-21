# November To-Do — preparing to run all the cities in one go

**Created 2026-10-21.** The tracking file and guide for the push to finish **all the city work in November**. The developer upgrades from Max 5x to **Max 20x on October 29, 2026**; between now and then, we create every guiding document (instant-reference datasheets, Pre-Trip files and so on) so that November can power through the cities with as little overhead as possible.

**What this file is:** a checklist and a guide. It holds the plan, the decisions still needed from the developer, and a build log. It does not hold findings. City status lives in `Worldspace/Locations-and-Levels/Universal_Location_Methodology/MASTER_Process_Tracker.md`; datasheet and Pre-Trip status lives in `Datasheet_and_PreTrip_Tracker.md` in the same folder.

**Update rule:** when an item is done, tick it here in the same turn and add a row to the build log at the bottom.

---

## 0 · Dates and ground rules

| Date | What |
|---|---|
| 2026-10-21 (Wed) | This plan written. |
| **Oct 21 to Oct 28** | **Preparation window.** Build the guiding documents; take the developer's decisions. |
| **2026-10-29** | Upgrade to Max 20x. The ULM and the slang-synthesis study restart. |
| **November** | The city run, all cities in one stretch. |

**Rules that bind the preparation** (from the standing laws)
- **Hours.** Preparation items below are bounded source preparation (no derivation about a place), so they may run **at any hour**. Any actual city-pass step, or any edit to a city's culture synthesis, is **in-hours only, 05:00 to 14:59** (wrap-up from 13:59).
- **Law of one location.** A city pass never reads another city. Datasheets are built per city, from that city's own sources, and a datasheet never carries another city's answers.
- **Datasheets answer "what does the source say," never "what does it mean."** No synthesis, no interpretation. `LAW 0` and `LAW 0-R` are untouched.
- **Never read the withheld material** into a datasheet (`City_Megasheets/`, `Local_Cultures/` and `Local_Robot_Culture/` before their turn, reserved questions, the write-only differentiation table).
- **Founders come only from `Founding_Register.md`.** The founders cleanup of 2026-10-13 already brought the specs in line; datasheets must match.
- **Work light on the weekly allotment this week** (the developer reports burning it by Monday afternoon). Prefer scripts over reading everything by hand; keep subagent rounds out until October 29.
- **Commit only when the developer asks.**

---

## 1 · Preparation checklist (October 21 to 28)

*Items marked ⭐ are the most valuable per unit of effort.*

- [x] **N-1 ⭐ · Recount the Datasheet and Pre-Trip Tracker.** *(Done 2026-10-21: totals unchanged; Mirny's row and three notes updated.)* It was last counted on 2026-09-30; re-count from the live folders and fix the rows. *(Cheap, no research.)*
- [ ] **N-2 ⭐ · Check which existing datasheets the founders cleanup made stale.** The founders cleanup rewrote founding lines in 20 specs and corrected culture sheets; datasheets quoting the old founding lines (Cape Adare, Zukelli, Dumont d'Urville, Denison, Casey, Kunlun, Vostok, Mirny, Davis) must be re-checked. Spec line numbers did not move, so citations still resolve; the values may not match. Use `Tools/check_founders_against_register.py` plus a manual look.
- [ ] **N-3 ⭐ · Build the reader-list generator.** Generate the `.t8_required_<step or phase>.txt` lists by copying each city's Pre-Trip rows verbatim, so Round 0 of every step stops being hand-built. *(Identified as the cheapest win on 2026-09-15.)*
- [ ] **N-4 · Build the Pre-Trip sheets and position-coverage ledgers for every city that lacks them.** Recipe: `PRE-TRIP_INSPECTION_RECIPE.md`. Have them: Casey, Davis, Denison, Dumont d'Urville, Kunlun, Mirny, Vostok, Zhongshan (both trial folders). **Missing** (see list in section 4): Cape Adare and Zukelli need Pre-Trip sheets; the other cities need everything.
- [ ] **N-5 · Build the 19-file datasheet set for every city that lacks one,** subnet by subnet, in the run's geographic order (section 3). Recipe: `Mechanical_Extraction_Field_Guide.md`. Datasheets are DRAFT until the developer wants a fresh three-reader check.
- [ ] **N-6 · Finish the eBook-to-city mapping,** checked by contents, not titles (the old title-based mapping was measured wrong three times). Queued 2026-09-15; the completed tally was not found. Check `Book_Extraction_Index.md` and `Book_TOC_Master_Reference.md` first so nothing already mined is mined twice. Output: which book serves which city's research step.
- [ ] **N-7 · Casey: stage a fresh warm run.** Casey is the next city. The earlier cold run was a test; production is warm. Verify its datasheets and Pre-Trip sheet are current after the founders cleanup, and that its folder and `README.md` are ready.
- [ ] **N-8 · Estimate the cost per city and set the standard reader setup.** Mirny's Steps 5 to 10 hit the five-hour limit on Max 5x. Estimate cost per step on Max 20x and decide the standard number of readers, rounds and list sizes, so one month fits. *(Needs the developer's decision, see section 2.)*
- [x] **N-9 · Review Mirny's lessons and fold the accepted ones into the runbook.** *(Done 2026-10-21 for the 19 proposals: groups A to C approved and implemented, the per-line hash and the cross-reference item set aside. The remaining Mirny handoff decisions are still being taken; see D-1.)* The pass recorded 16 new observations and 19 methodology proposals; none is applied. The developer reviews which become rules; accepted ones go into `00_RUNBOOK.md` and the Spine in the same commit.
- [ ] **N-10 · Add any new corpus-wide reference sheets that November will need.** Candidates (propose, then build only those the developer approves): founders and rename quick reference; the social-contract and symbol-layer terms; the Modern Hawaiian language canon note; the fixed rosters not yet in `Corpus_Reference_Sheets/`. Check the Field Guide's Tier U list against what exists.
- [ ] **N-11 · Mirny leftovers to schedule, not do.** The amendment re-derivation after the Social Contract rulings; the Planet symbol assignment; the cap-starved research on the unresearched stock repertoires (queued for Max 20x). Record them in the November run order so they are not lost.
- [ ] **N-12 · Update `MASTER_Process_Tracker.md`** so its `RESUME HERE` block names the first November city and the first piece, and its SESSION BOOT is current.

---

## 2 · Decisions needed from the developer

| # | Decision | Needed by | Notes |
|---|---|---|---|
| D-1 | ~~Which of Mirny's 19 methodology proposals become rules~~ **Decided 2026-10-21** | | Groups A to C approved; two set aside. Remaining Mirny handoff decisions (ledger, Phase 9 amendments, the 23-row docket and so on) continue. |
| D-2 | New names for **Dumont d'Urville** and **Zukelli**, in line with their founders; whether to audit other foreign-named cities (Mawson, Neumayer, Rothera, Signy, Scott and others) | before their runs, ideally before datasheets are built | Dome Fuji stays "The Temple" until the language exists. Byrd keeps its name. The rename sweep for the held files runs after the Mirny pass. |
| D-3 | Founders for **Sejong, Juan Carlos, Sayowa** (still TBD in the register) | before those cities' datasheets | |
| D-4 | The standard reader setup and budget per city | before N-8 | |
| D-5 | Whether the 38th-city placeholder is still "Bunger Hills City" or has become Relung Panen, and whether it runs in November | before N-4/N-5 for it | Tracker lists `{{Bunger Hills City}}` as saved for later; Relung Panen has its own dossier |
| D-6 | Confirm the run order and that Concordia stays excluded | before N-5 | Concordia's districts use the district methodology |
| D-7 | When the CST and RWBEM passes run relative to the ULM | before November | Standing plan: ULM on all cities first, then CST and RWBEM |
| D-8 | Whether the reference sheets in N-10 are wanted | before building them | |

---

## 3 · The November run plan (draft)

- **Mode: warm** for every city (cold runs are tests only).
- **Order: geographic, by subnet,** finishing one subnet before starting the next; Peninsula, then east around the coast, then the Ross Sea, West Antarctica, and the Pole. **Casey is first** (Mirny subnet). Not alphabetical.
- **One piece at a time.** Display the result, write it to file in the same turn, take the developer's clarifications, then run the next piece. "Painfully slow" is the design.
- **Pace:** roughly one city per day is the expectation, but a city taking longer is fine. One step should not take eight hours. Attack overhead, never depth.
- **After the ULM on all cities:** the CST and RWBEM passes, then the terminal differentiation check. Factions are created after all of that, together with the developer.
- **Run alongside, from October 29:** the slang-synthesis study and the Tepenian Hawaiian research, in their own repos.
- **Mirny's own leftovers** (N-11) are scheduled into the run, not forgotten.

---

## 4 · Cities and what each still needs

*(Counts taken 2026-10-21 from the tracker and folders. Re-count with N-1 before relying on them.)*

**Have a full datasheet set (9):** Cape Adare, Casey, Davis, Denison, Dumont d'Urville, Kunlun, Mirny, Vostok, Zukelli.
**Have a Pre-Trip sheet:** Casey, Davis, Denison, Dumont d'Urville, Kunlun, Mirny, Vostok, Zhongshan (both trial folders).
**Need a Pre-Trip sheet only:** Cape Adare, Zukelli.

**Need everything (datasheets, Pre-Trip sheet, ledger):**
- **Amundsen Station:** Amundsen Station
- **Byrd subnet:** Byrd
- **Halley subnet:** Abowasa, Belgrano, Halley, Lazar, Neumayer, Princess Elisabeth, Sanay, Troll
- **Janbogo subnet:** Fort McMurdo, Janbogo, Scott *(Concordia excluded: its districts use the district methodology)*
- **Mawson subnet:** Dome Fuji, Mawson, Sayowa
- **Mirny subnet:** Shirayuki, Sinheung, Zhongshan *(the ULM is already done for these three without the artifacts; decide whether to build them)*, the 38th-city placeholder (see D-5)
- **Palmer subnet:** Esperanza, Juan Carlos, Marambio, Palmer City, Port Lockroy, Rothera, Sejong, Signy

---

## 5 · Build log

| Date | Event |
|---|---|
| 2026-10-21 | File created from the survey of existing artifacts; plan and decisions listed. |
| 2026-10-21 | N-1 done: the Datasheet and Pre-Trip Tracker recounted. |
| 2026-10-21 | Mirny handoff decisions 4 to 7 done (agreed): culture-sheet corrections wait for the post-ULM rewrite; vision material stays out of frame; vignette-grounded robot findings withdrawn or re-grounded at the rewrite; the sector shares retagged on Phase 7. |
| 2026-10-21 | Mirny handoff decisions 1 and 2 done: the Position-Coverage ledger marked for Phases 8 to 10 (developer confirmed); the three firm Phase 9 amendments ratified (notice added to Phase 9). Rulings recorded as `DR-58`. |
| 2026-10-21 | Mirny handoff decision 13 done: groups A to C of the 19 proposals implemented. Tools repaired (`handoff_audit.py`, `phase_discipline_check.py`, `quotation_audit.py`); new file `Universal_Location_Methodology/T8_Standing_Brief_Lines.md`; runbook Step 9 items 2, 3, 5 and the T8 table rows; spine Phase 6 must-open list; Field Guide Step 9 note. |
| 2026-10-21 | Mirny handoff decision 8 done: `Tools/check_founders_against_register.py` now honors `--city` (own files plus shared files only; other cities' files and withheld material skipped and counted; developer approved). Developer's reminder: scanning and reading every city-related file in the whole repo belongs in the preparation phase, so a pass can read the reference files directly. |
