# Casey — ULM Step 10 · The readiness check (PROPOSED)

*Step 10 of Casey's warm run (`DR-6`), under runbook Step 10 (L3080–3176). Three readers ran the check independently (A, B, C); each cross-checked the other two in Round 3; a script confirmed each reader's proof of reading in Round 2; this file is the one merge. Round record: `10b_T8_Rounds_Step_10.md`. **VERIFY, DO NOT ASSERT:** every item carries its command and raw output, or the line read; where readers differed on a result, this merge re-ran the read-only command and pasted what it returned. The next pass's subject is **Relung Panen** (startup L1–12; tracker L382). Nothing here is declared complete; the developer declares completion.*

*Merge rule (`M-246`, `M-256`, `M-259`): no contradiction → union, credited; contradiction → the most conservative post-Round-3 view, the split named; for the verdict, the view that reports the blocker. Casey is compared with no other city. Quotation marks stand only around words copied from a file, with file and line.*

## Canon opened

- **By the three readers, each in full at the brief's admitted ranges (21 entries):** the runbook L3080–3176; `Run_Modes_Warm_and_Cold.md`; the auto-loaded memory index (the index only, 141 lines on disk); `06_Worked_Example_Provenance.md`; `STARTUP_Relung_Panen_ULM_2026-11-15.md`; `MASTER_Process_Tracker.md` L361–395; Relung Panen's pass `README.md` and `00.0_Pre-Trip_Inspection.md`; Casey's `Datasheets/Step_10.md`, `README.md`, `05_Reconciliation.md`, `06_Differentiation.md`, `07_QA_Gates.md`, `08_Review_Panel.md`, `09_Record.md`, `09.5_Log.md`, `.t8_10_Step_10_rows_extract_raw.txt`, `04_Phase_06_Meaning.md`, `04_Phase_07_Order.md`, `04_Phase_08_Making.md`, `08b_T8_Rounds_Step_8.md`. Long files in contiguous pages; no entry read in part (A, B, C; Round 2 confirmed by script).
- **Read-only commands the readers ran,** each pasted under its item: `grep -c`, `grep -l`, `grep -n` (line numbers, or lines of Casey's own files), `ls`, `test -e`, `wc -l`, `stat`, `sed -n … | cat -A` for positional fields, and `git log` / `git status --short` / `git diff --numstat` / hunk headers (metadata and counts only). B also printed the runbook's `^# Step` heading lines (line numbers) and ran pattern searches over Casey's own pass files outside the list (Snags).
- **By this merge:** the brief, the three outputs and the three Round 3 replies, in full. To settle results, read-only re-runs (raw output pasted under each item): `git diff --numstat` and hunk headers on the observations file and the rulings log; `git status --short` on the rule files, the tracker and `Tools/`; `git show -U0 --format= 881cbfd1` hunk headers on the runbook and the spine; line numbers only for `casey` in the runbook and the spine; counts of `bunger hills city` in both files now, at `78c3c64f~1` and at `b9b11729`; line numbers only of the alias hits in the memory index; counts over the required reading and Casey's Steps 5–9; `ls` of Relung Panen's folder; `test -e` of the two files the next run creates; `wc -l`, `stat` and two line-total commands over Casey's folder. **Lines printed to settle quotations, all on the list and inside admitted ranges:** runbook L3109–3114, L3151–3160; Run_Modes L57, L60, L91–93; startup L26–28, L33, L78–83, L130, L133–134; Pre-Trip L148, L224, L457; `09` L6, L92; `07` L6, L713; `08` L6, L50, L58; `06` L84; `05` L811; `08b` L235–237; `09.5_Log.md` L43, L60; fixed-string locations in `06`, `08`, `05`, `04_Phase_06`, `04_Phase_07`, `09.5_Log.md`, Casey's README and the Step 10 datasheet.
- **Not opened by anyone:** any other city's pass, culture, spec or personality file; Relung Panen's files beyond its README and Pre-Trip; Casey's culture, robot-culture and personality files; the characters folder; the symbol files; `City_Megasheets/`; the faction files; location content under `Test_Runs/` (the observations file was touched by counts, hunk headers and entry keys only); the memory files behind the index; the decisions file; the spine's text; the runbook outside L3080–3176 (line numbers and hunk headers only). **The differentiation table:** never displayed; three count-only commands touched it (B: two, C: one), recorded under Snags and not used as evidence. No web search. Graphify was not run; every hook notice was disregarded under `DR-6`, which here is compliance, not override.
- **Tiers, as the files record them:** the rulings are tier 1; Casey's pass files are PROPOSED with no canon tier; the datasheets and the Pre-Trip are pre-staged inputs, corrected only after the run (`DR-136` item 9).

## INBOUND HANDOFF SWEEP

*One row per item handed to Step 10 (and the four rows the extract hands to Step 9, plus Step 9's own three at `09` L496–498). Sources: the orchestrator's extract (44 Step 10 rows, 4 Step 9 rows; taken 10:09, before `09_Record.md` existed), `09_Record.md`'s own ten Step 10 rows (L499–508), and the other lines naming Step 10 that the readers found (folded into the row they restate). A wrote 58 rows, B 53, C 53: the difference is grouping only (all three Round 3 replies). Step 10 edits no file, so an owner's item is **carried** with its reason; a check is **discharged** by what the lines and commands show.*

| Key | Source and line | Item handed to Step 10 | Disposition | Found by |
|---|---|---|---|---|
| S10-1 | `04_Phase_05` L616; amendment L99; `06` L238 | Each relation's source; the spec and record revisit list (spec L7's bearings and spur; DB L165, L169; Highways L90, L97, L291; the road-closed day) | **Discharged in part:** spec L7's half is settled by Step 5 (S5-RC-48 to S5-RC-51, `05` L222–225). **Carried to the developer, for the records' owners:** DB L165, L169, Highways L90, L97, L291 and the road-closed day; per-relation source checks need phase files not on the list | A, B, C |
| S10-2 | `04_Phase_05` L617 | `Phase_5.md` datasheet rows | **Carried** (`DR-136` item 9) | A, B, C |
| S10-3 | `04_Phase_06` L398 | `Phase_6.md` datasheet rows; DQ-22 if answered | **DQ-22 answered** by `DR-137` item 4, applied at S5-10 (`05` L291–304); its decisions-file mark (`DEC-532`) **carried to the orchestrator** (B). Datasheet rows **carried** | A, B, C |
| S10-4 | `04_Phase_08` L536 | REQ-33; DQ-10 to be marked closed; amendment L47's check that no base language counts toward the tier | **L47 check discharged**, by reading `04_Phase_08` L454 (A, C) and by command (B: the four supporting-base names appear only at amendment L15, L16, L40, L47 and in P8-37's definition, `04_Phase_08` L445; none names a tier). Marking DQ-10 closed **carried to the orchestrator** | A, B, C; command B |
| S10-5 | `04_Phase_08` L537 | `Phase_8.md` rows; the weapons file's catalog pointer | **Carried** (`DR-136` item 9; gear catalogs gated) | A, B, C |
| S10-6 | `04_Phase_07` L537 | `Phase_7.md` rows; the Megacorps README's heading against its body | **Carried** to the owners | A, B, C |
| S10-7 | `04_Phase_07` L538 | `09` L34–35's legal-rate note; DQ-25 | **Carried:** DQ-25 (`DEC-535`) is the developer's | A, B, C |
| S10-8 | `04_Phase_03` L431; `05` L543 | Spec L98's wind (DQ-35); 219 mm against 225.1 mm snowfall | **Carried:** DQ-35 (`DEC-545`) open; the snowfall pair unreconciled. No finding rests on the wind's exact bearing (`07` L713) | A, B, C |
| S10-9 | `04_Phase_03` L432 | `Phase_3.md` rows | **Carried** (`DR-136` item 9) | A, B, C |
| S10-10 | `04_Phase_10` L476 | The Phase 10 datasheet's L7 coverage claim | **Carried** (`DR-136` item 9) | A, B, C |
| S10-11 | `04_Phase_04` L588 | `Phase_4.md` rows (the stale 38.7%, coverage, out-of-set cites) | **Carried** (`DR-136` item 9) | A, B, C |
| S10-12 | `04_Phase_09` L510; `07` L1281 (part); `09.5_Log.md` L58 (CL-38); `09` L504 (part) | `Phase_9.md` L16's 50.91% | **Carried** to the owner: the figure does not reproduce; 786,985 ÷ 1,547,850 = 50.844% (recomputed by all three in Round 3; raw Census I as `07` L1009 prints it) | A, B, C |
| S10-13 | `04_Phase_09` L511 | DQ-11, answered by `DR-136` item 10, to be marked closed | Reading applied (S5-12, `05` L312–314; S7-E-8, `07` L1139–1144). Mark **carried to the orchestrator** | A, B, C |
| S10-14 | `04_Phase_02` L507 | `Phase_2.md` rows; two polity names possibly one | **Carried** to the owners | A, B, C |
| S10-15 | `04_Phase_02` L508 | The treaty-dependent findings list, to recheck if the draft's standing changes (DQ-12) | **Carried to the developer** as a standing list with DQ-12: no revision of the draft is recorded, so no recheck is triggered now. *Split: A (Round 1) "discharged as standing"; B and C carried; A conceded in Round 3; the conservative form is written* | A, B, C |
| S10-16 | `05` L544; `05` L85, L327, L406 item (9) | Record frictions: rulings L2004 against L2007; P5-3's interims; the datasheet's L18 own-eras line | **Carried** to the owners. Both L2004 and L2007 are lines of the one append after L1996 (S10-48's raw output) (C) | A, B, C |
| S10-17 | `05` L545 | Casey's datasheets and Pre-Trip corrected after the run | **Carried** to the developer (`DR-136` item 9) | A, B, C |
| S10-18 | `05` L546 | A readiness check on stage A's discharge claims (sweep rows 11, 30, 42, 45, 46, 50–57) | **Discharged by reading each pointer** (A, C): row 11 → S5-21 (L410); 30 → S5-20 (L399); 45 → S5-24 (L436); 46 → S5-AM-1 to S5-AM-10 (L106–165); 50 → S5-1 (L237); 51 → S5-25, S5-26 (L469, L486); 52 → S5-18, S5-22 (L389, L416); 53 → S5-23 (L432); 54 complied (L83); 55 the docket (L90–100); 56 → S5-14 (L326); 57 → S5-18 and S5-5 to S5-9. **Row 42 does not land:** S5-20 (L399–402) never mentions the spare, which sits at S5-11 →2 (L310), already erratum S7-E-15 (`07` L1188–1193). B reached the same through Gate 0 (`07` L553). No new defect | A, B, C |
| S10-19 | `05` L891 | The docket S5-PC-1 to S5-PC-19 | **Carried:** each row the developer's (`05` L811) | A, B, C |
| S10-20 | `05` L892; L783 (S5-CK-59); L833 (S5-PC-19) | What grounds the culture file's technical and scientific share | **Carried** to the developer | A, B, C |
| S10-21 | `05` L893 | A readiness check that no finding imports a read-last line as an input | **Discharged by reading:** `06` L84 (A) and `06` L158 (C); `07` L103, row 49; Step 8 cites culture L73, L75 only as that material's own side or an answer not adopted (`08` L126, L144, L153) and refused the `unmet` that leaned on them (`08` L250); `09` cites none as ground; Phases 2–10 predate the opening (C) | A, B, C |
| S10-22 | `06` L235 (S6-16) | Table L27–28 still state the read-before-write loop for cities | **Carried** to the instrument's owner (M-335, proposed) | A, B, C |
| S10-23 | `06` L236 (S6-10) | `04` L526 against runbook L469 and `DR-137` item 10 | **Carried** to the method's owner (M-335). **Single-reader find (B):** runbook L469 is the very line commit `881cbfd1` rewrote (hunk `@@ -469 +469 @@`, re-run at S10-60), so the tension is cited against a line the ruling changed | A, B, C; L469 B |
| S10-24 | `06` L237 | The table's untitled and uninstructed columns; the Pass column; the §10 heading line | **Carried:** DQ-39, DQ-40 open | A, B, C |
| S10-25 | `07` L1281; `07` L554–555 | Lagging status lines and Tier U records (S7-E-16; contract L3; Phase 4's 438-line count; the Step 7 datasheet's splice; 50.91%) | **Carried** to the owners, no edit | A, B, C |
| S10-26 | `07` L1282; `07` L90, L95, L99; `05` L534 | S5-RC-6 (DQ-35), S5-RC-8 and S5-8 (DQ-36), S5-RC-23 with S5-CK-56; check that no later line rests on them | **Check discharged for Steps 7–9 by reading:** "no finding rests on the wind's exact bearing (S5-RC-6), on flight mode counting as rest (S5-RC-8) or on a winter carrier" (`07` L713); "no line places flight mode outdoors or relies on it" (`08` L50); S8-O-15 holds under either answer (`08` L137); `09` rests nothing on them. DQ-35, DQ-36 **carried** | A, B, C |
| S10-27 | `07` L1283; `07` L78 | REQ-32: spec L86, L171, L173, L201 not admitted by part | **Carried:** an admission ruling | A, B, C |
| S10-28 | `07` L1284; `07` L773 | Where waste water and the plant's exhaust land | **Carried:** national topic N1 | A, B, C |
| S10-29 | `07` L1285; `07` L436 | No inheritance class for a site inheritance; runbook §E not on Step 7's list | **Carried** to the method's owner (M-337, M-338) | A, B, C |
| S10-30 | `07` L1286; `07` L56, L321; `09` L505 | Name the negatives' search paths; was the universe repo searched | **Discharged in part:** the run log names the paths (`09.5_Log.md` L49, L51, L53, L60), so the universe repo **was** searched at those paths; Phase 6's receipt names folders, files and command (`04_Phase_06` L21–25, A); Phase 7's names none (`04_Phase_07` L38). **Carried:** `04_Phase_05` L27 and P10-45 (not on the list); REQ-34's search (`07` L958) | A, B, C |
| S10-31 | `07` L1287 | `05` L229's protective figure lacks its raw rate | **Confirmed** at `05` L229 (C); recomputed 6 per 1,000 × D 1.11 × 1,547,850 = 10,308.7 (A, B, C in Round 3), the basis at `07` L1080. **Carried** for the after-run correction | A, B, C |
| S10-32 | `07` L1288; `09` L500 | Every downstream use of S7-E-1 to S7-E-25 takes the corrected reading | **Discharged for Steps 8–9:** "the panel ran on the corrected statements" (`08` L58); `09` cites errata only as records. **One exception carried:** the §7 row already in the city table, current text unread (`09` L64, S9-2; DQ-46). *B's count of the S7-E-12 term in the table is not used (the table is barred)* | A, B, C |
| S10-33 | `08` L260 | The accepted objections' proposed changes | **Carried** for the after-run correction; "never applied" (`08` L6). B: `git status` shows no change to any tracked Casey phase file | A, B, C |
| S10-34 | `08` L261 | `unmet` with its ground; `declined` not counted as self-knowledge; `noted` never later written as characterization | **Discharged by reading:** `08` L250–251; `09` L53–54; `09` writes no `noted` want as characterization | A, B, C |
| S10-35 | `08` L262 | The casting record | **Carried** as a PROPOSED record (`09` L57 points to it) | A, B, C |
| S10-36 | `08` L263 | The Hero's scale question kept open | **Discharged for Step 9** (no line in `09` asserts it); a standing guard downstream | A, B, C |
| S10-37 | `08` L264 | No lapse rule, register or standing for membership; DQ-42 | **Discharged for Step 9**; DQ-42 **carried** | A, B, C |
| S10-38 | `08` L265 | *Owed* stays the pass's analytic word | **Discharged for Step 9** (C searched `09`: no resident is given the word); a standing guard | A, B, C |
| S10-39 | `08` L266; `08` L135 (S8-O-13) | The heat's source and the plants' number and siting | **Carried:** an input gap no admitted line fills | A, B, C |
| S10-40 | `08` L267 | The refusals stay characterizations; the `unmet` unfilled | **Discharged for Step 9**; a standing guard | A, B, C |
| S10-41 | `08` L268 | The panel's readings beside DQ-37, DQ-42, DQ-43, DQ-44 | **Carried** with the questions | A, B, C |
| S10-42 | `08` L269 | DQ-45: no `unmet` rests on a read-last line | **Discharged:** the one `unmet`, S8-O-16, rests on rulings L2003, `DEC-541` (`08` L138, L250). DQ-45 **carried** | A, B, C |
| S10-43 | `08` L259 (Step 9) | Record the panel block | **Discharged at Step 9** (`09` L39–58; S9-9) | A, B, C |
| S10-44 | `06` L228 (Step 9) | Insert Casey's ten rows blind | **Discharged at Step 6**, confirmed at Step 9 from the orchestrator's result (`09` L62); not re-checked (table barred). The commit **carried to the orchestrator**, on the developer's word | A, B, C |
| S10-45 | `06` L229 (Step 9) | The III.0 relations into the table's propagation row | **Carried:** DQ-47 | A, B, C |
| S10-46 | `07` L1280 (Step 9) | Correct Step 6's §7 cell before inserting the row | **Cannot be discharged as written:** the row went in before Step 7 was recorded (`09.5_Log.md` L68–69); DQ-46 **carried** | A, B, C |
| S10-47 | `09` L499 | The T5 falsification check | **Worked here:** S10-70 | A, B, C |
| S10-48 | `09` L501 | The stale-anchor remainder, the rulings log first | **Rulings log discharged by command** (re-run below). **Carried:** the other short-name sources, the twelve unnamed changed files, Steps 5–9 as citing files, the pass's cross-citations | A, B, C |
| S10-49 | `09` L502 | `06`'s table citations at their computed addresses | **Carried** to the orchestrator (table barred) | A, B, C |
| S10-50 | `09` L503 | The 29 Step 10 rows of Steps 5–8 | **Worked here:** S10-16 to S10-42 | A, B, C |
| S10-51 | `09` L504; `09.5_Log.md` L37, L60 | 50.91%; the characters-canon flag in another repository; the research-log index row (DEC-519) | **Carried** to the developer: CL-40 reads "Flag for the developer at Step 10" (`09.5_Log.md` L60); CL-17's row is "Held for the developer's word" (L37) | A, B, C |
| S10-52 | `09` L506 | Rows outside Step 9's list; lines deferring to the close | Rows: worked here (S10-1 to S10-14). Deferral lines: **discharged for Phases 6–8 by reading** (A, C: one hit, `04_Phase_07` L322, a tolerance, not a deferral); B's pattern search over the contract, Frame, Steps 1–3 and Phases 2–10 found only `02_Spine` L360 and `04_Phase_07` L322, both the sea's closing. **Carried** for reading: the files on no list here (pattern search is not reading) | A, B, C |
| S10-53 | `09` L507 (M-347) | Casey's README describes a pass that does not exist yet | **Verified** at README L3–4, L18, L21 (S10-67); **carried** to the owner | A, B, C |
| S10-54 | `09` L508 | M-321 to M-352 stand as proposals; nothing changed by them | **Discharged by command, with a wording to settle** (S10-68): no rule file or `Tools/` change; the entries are written, uncommitted, into the observations file | A, B, C |
| S10-55 | `09` L496–498 (Step 9's own rows) | The tracker line; the L30 propagation write on DQ-47; the commit of the table entry with the record | **Carried to the orchestrator:** no 2026-11-16 Casey status line in the tracker (S10-67); DQ-47 unanswered; nothing committed unasked | B (folded by A, C) |

*Count: 55 rows. Discharged here, in full, in part or for Steps 7–9: 17 (S10-1, S10-4, S10-18, S10-21, S10-26, S10-30, S10-32, S10-34, S10-36, S10-37, S10-38, S10-40, S10-42, S10-48, S10-52, S10-54, and S10-3's DQ-22 half). Discharged at an earlier step or by ruling: 3 (S10-13's reading, S10-43, S10-44). Worked in this file: 3 (S10-47, S10-50, S10-53). Cannot be discharged as written: 1 (S10-46). Every other row and every remainder is carried, each with its reason. No row is refused.*

**S10-48's command, re-run by this merge (raw output, whole):**
```
$ git diff -U0 78c3c64f -- DEVELOPER_RULINGS_LOG.md | grep -o '^@@ [^@]* @@'
@@ -1996,0 +1997,11 @@
$ git diff --numstat 78c3c64f -- DEVELOPER_RULINGS_LOG.md
11	0	Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md
$ wc -l < DEVELOPER_RULINGS_LOG.md
2007
```
Since the base of Steps −1 to Phase 2 (`78c3c64f`) the log only grew after L1996, so no line cited at or before L1996 moved (A, B, C). Since the base of Phases 3–10 (`881cbfd1`) it only grew after L2005: `@@ -2005,0 +2006,2 @@` (A's command, single-reader find, not re-run here). Steps 5–9 were written after the last change, so their L2005–L2007 citations are in the current frame (A).

## §10.1 · The contamination surface, run against the next subject (Relung Panen)

*Relung Panen's run is WARM (Pre-Trip L44). Run_Modes L60: "**the memory blackout · the reader briefs · the pre-contamination review · the pins · skip ranges.** ***None of these is required for a warm run***". Each item is still run and its result written; cold-run-only requirements are marked. Alias set (the brief's): Relung Panen; Bunger Hills City; Bunger Hills; the Bunger Hills oasis; Knox Coast. B and C also counted the Pre-Trip's wider candidate set (L26–38): 0 in every file searched.*

**S10-56 · Item 1, the auto-loaded memory index: three hits, all attribute or status; none states a character, temperament, personality triple or signature phrase. Nothing to fix or band.** *(A, B, C.)* Re-run by this merge, line numbers only (raw output, whole):
```
$ grep -n -i -E 'relung|bunger|knox' MEMORY.md | cut -d: -f1 | tr '\n' ' '; wc -l < MEMORY.md
23 125 140
141
```
- L23: the official name and its confirmation date (attribute). L125: a ruled industry role named by ruling keys, a research status, a held-edits note and a pick count (attribute and status; Run_Modes §3 classes Division-of-Industry figures as attributes, L101–102). L140: run order and a startup pointer (status). *(Classes: A, B, C.)*
- *Cold-run only:* the memory blackout (Run_Modes L60). *Recorded:* the index on disk differs from the copy pushed into the readers' sessions (disk L69–70 and L140 are newer); every scan ran on the disk file (A, B, C).
- **Single-reader find (B):** the memory files behind L23 and L125 name the subject; their bodies were not read (barred), so whether they are attribute-only is not verified. Optional in warm mode; handed forward (S10-73).

**S10-57 · Item 1a, the required reading: one line in `00_RUNBOOK.md` and one in `03_The_Phase_Spine.md` match the alias set, each the subject's former placeholder, Bunger Hills City, by per-alias count; both lines predate Casey's run; `06` has no Relung Panen section, so its check returns clean while they stand. The lines were not read (barred); they are unclassified, unbanded and unmanifested.** *(Hits: A, B, C. The string by per-alias count: B, C. Predating the run: C, confirmed by A and B in Round 3.)* Re-run by this merge (raw output, whole):
```
$ grep -c -i -E 'relung|bunger|knox' 0[0-6]_*.md README.md Disciplines/* | awk -F: '$2>0'
03_The_Phase_Spine.md:1
00_RUNBOOK.md:1
$ for f in 00_RUNBOOK.md 03_The_Phase_Spine.md; do <count 'bunger hills city' now, at 78c3c64f~1, at b9b11729>; done
00_RUNBOOK.md now=1 at_78c3c64f~1=1 at_b9b11729=1
03_The_Phase_Spine.md now=1 at_78c3c64f~1=1 at_b9b11729=1
$ grep -c -i -E 'relung|bunger|knox' 06_Worked_Example_Provenance.md
0
```
- **What the runbook asks of this item:** "**Return line numbers, band or neutralize every hit, and manifest it in" / "`06`.**" (runbook L3111–3112, a sentence that wraps; each line quoted separately). Run_Modes L93 holds in warm mode: "**Check `06` for the subject, and treat any hit as read-last material.**" Neither is done: the readers' brief allowed counts and filenames only (A Snags 5; B Snags 5; C item 1a).
- **A layering question the count raises (A, B, C):** the Pre-Trip quotes the layering law as `01`–`05` naming no location (Pre-Trip L478). The spine's one line is either a non-location use of the string (a path or file name) or a breach. Not decided here.
- **Who returns the line numbers** when the check's readers are barred from the lines is a method gap (A-DQ-3, B Snags 5, C-DQ-201): DQ-48.
- **This item is the verdict's blocker** (see the Verdict).

**S10-58 · Item 1b, the titles the next run must navigate: no file or folder title states a claim about the place.** *(A, B, C.)* Re-run by this merge (raw output, whole):
```
$ ls -A Relung_Panen; ls -A Relung_Panen/Datasheets | wc -l
00.0_Pre-Trip_Inspection.md
00.2_Position_Coverage_Ledger.md
Datasheets
README.md
19
```
Every name is a role or a step or phase number; scaffolding, pre-seeded and allowed (runbook L3145–3147, `M-299`). The research files the Pre-Trip's addendum lists (L398–415) carry topics and real places, not conclusions about the city (A, B); the four airport comparison files naming Casey and another location are withheld by name (Pre-Trip L421) (A, B, C). *Cold-run only:* sanitized paths (runbook L3117–3119).

**S10-59 · Item 1c, this pass's own new prose: one name hit, `09.5_Log.md` L49 (CL-29), the road spur named as Highways names it in a Phase 5 list record; shape (a relation), no claim about the next subject.** *(A, B, C.)* Re-run by this merge (raw output, whole):
```
$ grep -c -i -E 'relung|bunger|knox' 05_Reconciliation.md 06_Differentiation.md 07_QA_Gates.md 08_Review_Panel.md 09_Record.md 09.5_Log.md 08b_T8_Rounds_Step_8.md | awk -F: '$2>0'
09.5_Log.md:1
$ grep -n -i -E 'relung|bunger|knox' 09.5_Log.md | cut -d: -f1
49
```
- **By role (A, B; C conceded in Round 3):** Steps 5–9 name the place as "the spur city" (e.g. `06` L198), relations from Casey's own lines. **Single-reader count (B):** 27 such lines (`05` 3, `06` 2, `07` 10, `08` 9, `09` 3, log 0), which a name grep cannot see.
- **The nearest any line comes to content (A, B):** Step 8 voiced a resident of the spur city as the Neighbor (`08` L103; S8-O-28 to S8-O-30), relation only, characterizing Casey. Not pushed: the startup bars it, "**Never open Casey's pass, culture or vision files during this run.**" (startup L83). The live vector is the orchestrator's own context if one session runs both (B). Handed forward (S10-74).

**S10-60 · Item 2, worked examples added to the methodology: commit `881cbfd1` (2026-11-15) replaced one line in the runbook (L469) and one in the spine (L693), each now naming Casey; `06` gained no row for either; no line added during the run names the next subject; no rule file has an uncommitted change.** *(Lines changed: A, B, C. Coordinates L469, L693: B, confirmed by C in Round 3.)* Re-run by this merge (raw output, whole):
```
$ git show -U0 --format= 881cbfd1 -- 00_RUNBOOK.md 03_The_Phase_Spine.md | grep -o '^@@ [^@]* @@'
@@ -469 +469 @@
@@ -693 +693 @@
$ grep -n -i casey 00_RUNBOOK.md | cut -d: -f1 | tr '\n' ' '; grep -n -i casey 03_The_Phase_Spine.md | cut -d: -f1
9 469 1332 1333 2218
693
$ git status --short -- 00_RUNBOOK.md 03_The_Phase_Spine.md 06_Worked_Example_Provenance.md Tools MASTER_Process_Tracker.md T8_Standing_Brief_Lines.md 04_QA_Gates_and_Differentiation.md; echo "(end status)"
(end status)
$ git log -1 --format='%h %ad' --date=short -- 00_RUNBOOK.md 03_The_Phase_Spine.md
881cbfd1 2026-11-15
```
- The startup names the edit: `DR-137` item 10's amendment of the 5b row (startup L59–60) (A, B, C). `06`'s Casey section (L292–337) has no row for either line (A, B, C). A counted the added lines over `b9b11729`: 2 naming Casey, 0 naming the next subject; C over `78c3c64f~1`: one Casey line added in each file.
- **Not classified** (both lines outside every admitted span): for Relung Panen's run they are another city's lines in mandatory reading (Run_Modes L19–24); for a future Casey run, an unmanifested example if content (`06` L55–56); a location named in `03` is also a layering-law question. **Post-Round-3 split:** B and C class the classification as part of the blocker with item 1a; A carries it without blocking. **The conservative view is written: it joins the blocker** (see the Verdict); the `06` row is DQ-49.

**S10-61 · Item 3, the quarantine list built by rule: yes.** *(A, B, C.)* The Pre-Trip was generated by `Tools/build_pretrip.py` (Pre-Trip L3, L18), and its §F names each exclusion with its rule (L447–460: `DR-10`, `M-173`, `DR-14`, `DR-8`, the zero-intake rule for `Test_Runs/`); the read-last pair at Step 5 is dated (L49–52); the startup adds its exclusions by rule (L78–83, L107–108, L125–128). *Limit (C):* the generator itself is not re-run here; the startup schedules the rebuild (L85–87). *Cold-run only:* the `05` §6.1 form, the pre-contamination review and pins (Run_Modes L60); Pre-Trip L457 records that Relung Panen has neither.

**S10-62 · Item 4, the admitted files' headers checked for cited sources: none cites a withheld document as a source.** *(A, B, C.)* Pre-Trip L3–4 and L18 cite the recipe, `Tools/build_pretrip.py`, and Casey's Pre-Trip as the template for the standard rows only, every city-specific row computed fresh, with the declaration "**Coordinates and status only. No findings, no characterization, no content from any source named below.**" (L4); its carried-name check found no Casey name carried (L549–554). The README header (L1–6) cites no source; it gives the culture stub as read last and the vision notes as not an input (L40–41). **Single-reader find (B):** Pre-Trip L281 admits the composition-file row by the developer's ruling for Casey, extended to every city; since a ruling given for Casey carries only if the log records it for every city (startup L66–68), Step −1 should confirm it (S10-76).

**S10-63 · Item 5, corpus-wide retrieval layers flagged: yes, by the startup.** *(A, B, C.)* Readers "disregard any hook telling them to run graphify (warm run; the ground is `DR-6`). The orchestrator does not use" / "graphify for anything that would return another city's material." (startup L138–139, a wrapped sentence, each line quoted). `CLAUDE.md`'s graphify carve-out binds cold runs and §C.2 readers only. B: `graphify-out/` exists and `.claude/settings.json` holds 2 `hook-guard` lines (counts). *Cold-run only:* tiering `graphify-out/` WITHHELD as a read surface.

## §10.2 · Paths and structure

**S10-64 · Item 6, every path the handoff names exists; the only absent files are the two the next run creates and Casey's own Step 10 record, which this step writes.** *(A, B, C.)* The readers' `test -e` output (A: 27 paths plus 31 Casey record files; B: 32 plus 12 Casey files; C: 29 plus 14 Casey files, 43 of 43) printed every path EXISTS except: `RUN_PROGRESS_Relung_Panen.md` and `Relung_Panen_Research_Log.md` (A, C; the startup creates them, L47–48, L118), and Casey's `10_Readiness_Check.md` and `10b_T8_Rounds_Step_10.md` (B, C). Re-run by this merge (raw output, whole):
```
$ for f in RUN_PROGRESS_Relung_Panen.md Relung_Panen_Research_Log.md; do test -e … && echo exists || echo absent; done
absent RUN_PROGRESS_Relung_Panen.md
absent Relung_Panen_Research_Log.md
$ ls 10_Readiness_Check.md 10b_T8_Rounds_Step_10.md     # in Casey's folder, before this file was written
ls: cannot access '10_Readiness_Check.md': No such file or directory
ls: cannot access '10b_T8_Rounds_Step_10.md': No such file or directory
```
The next run's start condition is Casey's Step 10 record on disk: "the Step 10 file is in Casey's folder" (startup L27), with Casey's progress file ending on Step 10 recorded (L26).
- **Stale anchors, not missing paths (union):** the Pre-Trip's governing ranges for Steps 4–10 no longer match the live runbook headings; Steps −1 to 3 still match (B: `grep -n '^# Step'` gives Step 5 L2760, Step 6 L2897, Step 7 L2936, Step 8 L2978, Step 9 L3006, Step 10 L3080, 3204 lines; confirmed by C's re-run in Round 3); Step 10 is given as "lines 3057–3152" (Pre-Trip L224), 23 and 24 lines off (C's Round 3 arithmetic). The search cap reads "**Web searches: 200 per session, shared by every reader in it.**" (Pre-Trip L148; also L69, L481), where the startup sets 1,000 (L51) (A, single-reader find; confirmed by B's re-run). The startup's readiness piece rebuilds the sheet (L85–87). Handed forward (S10-77).

**S10-65 · Item 7, the next run's output files do not already exist.** *(A, B, C.)* Readers tested every standard output name absent (A: 23 names plus globs; B: 23 names; C: 41 names), no phase file, round record, dot-file or `07_Gate_*` file. Re-run by this merge (raw output, whole):
```
$ ls Relung_Panen | grep -c -E '^(0[1-9]|10|04_|\.t8_)'
0
```
The folder holds pre-seeded scaffolding only, which runbook L3145–3147 allows. **Single-reader find (A):** Relung Panen's README lists `07_Gate_*.md` "one file per gate" (L23) where the Pre-Trip writes `07_QA_Gates.md` (L196); both names tested absent; for the scaffolding's owner (S10-78).

**S10-66 · Item 8, the shared observations file: it sits inside `Test_Runs/`, which the next run takes at zero intake, with one named exception; that exception now delivers Casey's text.** *(Location and exception: A, B, C. The hazard: C, adopted by A and B in Round 3.)* Re-run by this merge (raw output, whole; keys only, no entry text):
```
$ git diff --numstat -- Test_Runs/OBSERVATIONS_and_Methodology_Findings.md
173	0	Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md
$ git diff -U0 -- Test_Runs/OBSERVATIONS_and_Methodology_Findings.md | grep -o '^@@ [^@]* @@'
@@ -8604,0 +8605,173 @@
$ git diff -U0 -- … | grep -o -E '^\+- \*\*M-3[0-9]{2}' | sed 's/^+- \*\*//' | sort -u | tr '\n' ' '
M-321 M-322 M-323 M-324 M-325 M-326 M-327 M-328 M-329 M-330 M-331 M-332 M-333 M-334 M-335 M-336 M-337 M-338 M-339 M-340 M-341 M-342 M-343 M-344 M-345 M-346 M-347 M-348 M-349 M-350 M-351 M-352
$ stat -c '%y' Test_Runs/OBSERVATIONS_and_Methodology_Findings.md
2026-11-16 10:28:24.521508275 -0700
```
- The exception (Pre-Trip L457): "**ZERO INTAKE for the whole pass** *(one exception: Step 9 reads the tail of the" … "file for the next `M-` number — nothing else in the tree).*" Runbook L3151 asks for the file to sit outside every quarantined folder; it does not, and the exception is what holds it open (A, B, C): DQ-51.
- **The hazard (C):** the tail is now Casey's 32 entries, uncommitted. A Relung Panen Step 9 reader who reads the tail would read Casey's wording, against startup L78–83 ("no file, figure, verdict, tool output or" / "wording from Casey's run goes into any Relung Panen list, brief or record", L79–80). **The next key is taken by a number-only command, never by reading the tail** (S10-79). By the keys above the next free key is M-353 (A, B, C), taken at the time.

## §10.3 · Record integrity

**S10-67 · Item 9, Gate 0 outward: nothing in any file read declares Casey, a step or the run complete; several status records lag what the files hold.** *(A, B, C; additions credited.)* Re-run by this merge (raw output, whole):
```
$ wc -l 05_Reconciliation.md 06_Differentiation.md 07_QA_Gates.md 08_Review_Panel.md 09_Record.md 09.5_Log.md README.md
   977 05_Reconciliation.md
   355 06_Differentiation.md
  1393 07_QA_Gates.md
   378 08_Review_Panel.md
   557 09_Record.md
    72 09.5_Log.md
    45 README.md
  3777 total
$ grep -o -E '^- \*\*CL-[0-9]+' 09.5_Log.md | tail -1; grep -c -i 'step 9 recorded' 09.5_Log.md; stat -c '%y' 09.5_Log.md
- **CL-52
0
2026-11-16 10:11:49.984694723 -0700
$ sed -n '361,395p' MASTER_Process_Tracker.md | grep -n '2026-11-16' | cut -d: -f1 | awk '{print $1+360}'
381
```

| Record | What it claims (line) | What the files contain | Result | Found by |
|---|---|---|---|---|
| Casey's Steps 5–9 | Each ends PROPOSED and not complete (`05` L977; `06` L355; `07` L1393; `08` L378; `09` L557) | Line counts as above; Step 7's Gate 0 found no file claiming completion (`07` L551) | **Matches; nothing declared complete** | A, B, C |
| The tracker, L361–395 | Casey's last status line, 2026-11-15, Step 4 written, "**Next:** Step 5 at the next window" (L381); its only 2026-11-16 mention is that line's next cron run | Steps 5–9 written on 2026-11-16 | **Lags, a dated under-claim, not false.** The line for Steps 5–10 is owed at the morning's close (startup §5; `09` L86, L496). *Split: B (Round 1) blocking; B withdrew in Round 3; A, C owed. Not a blocker post-Round 3* | A, B, C |
| The tracker, L388 | Relung Panen among the cities left out of the November run | L382 (2026-11-15) sets Relung Panen next | **Stale beside the live L382**; the developer's text, for its owner | A, B, C |
| Casey's README | "the pass's own output files do not exist yet" (L4, dated 2026-10-30); "eleven" phase files (L18); `07_Gate_*.md` one file per gate (L21) | The pass files exist; nine phase files; one `07_QA_Gates.md` | **Does not match** (M-347); for its owner, no edit | A, B, C |
| Casey's run log | Last entry CL-52 (L72); Steps 5–8 recorded (CL-45, CL-48, CL-49, CL-50) | `09_Record.md` and `09b` exist; no entry records Step 9 (count above: 0) | **Lags:** Step 9's and Step 10's recording entries owed | C (single-reader find; confirmed by A, B) |
| `09` §4's drafted tracker line | ends "Step 10 not run" (L86) | True at its writing | **Matches at its date** | A, B |
| `09` §5 | "**Not one is applied.**" (L92); no pass file, rule file, tracker or table edited by the step (L6) | M-321 to M-352 written into the observations file at 10:28, uncommitted (S10-66); no rule file changed (S10-60) | **A wording to settle:** recorded as entries, applied as rules: none. Who appended them is in no line read (C) | A, B, C |
| Relung Panen's README | No output files yet (L5–6); "Relung Panen is not in the November run" (L38); specs and culture sheets still to be synthesized (L3) | No output exists (S10-65); the run is next (tracker L382) | **L5–6 match; L3 and L38 stale** | A, B (C conceded) |
| Relung Panen's Pre-Trip | Step 10 range L3057–3152 (L224); 200 searches (L148); "12 of 12 cited ranges equal the live range" (L543, B) | Live Step 10 L3080–3176; the startup's 1,000 (L51); Steps 4–10 stale | **Stale anchors and cap** (S10-64) | A, B, C |
| The startup | DEC numbering: "it was `DEC-544` on 2026-11-15, so **DEC-550**" … "unless Casey's Steps 5–10 add more" (L133–134) | Casey's Steps 5–8 filed DEC-545 to DEC-555 (`09.5_Log.md` L65, L68–70); DEC-550 is Casey's (CL-48, L68) | **Holds by its own rule:** the next section starts at DEC-560 or later. *Split on the basis: B gives the highest as DEC-557 from the decisions file, which is on no list; the admitted lines support "DEC-560 or later" (A, C in Round 3); written in that form* | B, C |
| The startup, cron prompt | "do not start a new piece after 13:30" (L33) | L188 says the 14:00 rule replaces the 13:30 in 0.2 and 0.3 | **Stale inside the file;** follow L188 | B (single-reader find; confirmed by A) |
| Casey's Step 10 datasheet | the readiness verdict "cannot exist before Steps 4–9 close" (L39) | Steps 5–9 written | **Matches** | A |
| The startup | "**Nothing here declares Casey complete.**" (L14); "**Never declare a run complete or ready.**" (L130) | — | **Matches** | A, B, C |

*A figure settled by re-run:* B wrote Casey's pass files as 20,686 lines over `0*.md`, the log and the README; C found the glob already includes the log. Re-run (raw output, whole): `ls 0*.md | grep -c '09.5_Log'` → `1`; `cat 0*.md 09.5_Log.md README.md | wc -l` → `20686`; `cat 0*.md README.md | wc -l` → `20614`. **20,614 is the count** (C); no result rests on it. *C's "43 step, phase and round files":* re-run `ls -1 | grep -c -E '^(0[0-9]|10)[^/]*\.md$'` → `43`; without the Pre-Trip and the ledger → `41` (A's Round 3 point: the basis was unstated). Neither changes a result.

**S10-68 · Item 10, findings implemented or only recorded: none of the run's methodology findings is a rule; each waits for the developer's word, so the next pass follows the rules as they stand.** *(A, B, C.)* Evidence: S10-60's status output (no change to the runbook, the spine, `04`, `06`, the standing brief lines, the tracker or `Tools/`; the last commit to the rule files is `881cbfd1`, before Step 5) and S10-66's keys (the entries live only in the observations file, uncommitted). The runbook's own line: "A finding logged in the observations file and" … "absent from the rule it should have changed has not been made — **the next pass follows the rules, not the" / "log.**" (runbook L3158–3160). Equally recorded, not applied: the 25 errata (`07` L6), the docket (`05` L811), the accepted objections' changes (`08` L6).
- **What that means for Relung Panen's run (union):** practiced, not ruled: M-321's hand check of every list (startup L91) and the brief-line check before dispatch (startup L95–96) (A, C). Carried in no startup line read: M-329, M-330, M-332, M-339, M-350, M-351 (A, B, C). Whether any should be ruled before Step −1: DQ-52.

**S10-69 · Item 11, does the handoff state what the next run cannot prove? In part.** *(A, B, C.)*
- **Stated:** nothing declares Casey complete (startup L14); open rulings deferred and non-blocking (L104); `DEC-003` provisional (L109–112); never declare complete or ready (L130); the alias set and every "Names Relung Panen at" row mechanical and unconfirmed (Pre-Trip L38, L583); the census narrative on hold (Pre-Trip L591).
- **Not stated, and true (union):** (1) what a warm run proves: "**nothing about independence — and does not need to.**" (Run_Modes L57, the *Proves* row) (A, B, C); (2) if the run follows Casey's in one session, fresh readers isolate the readers, not the orchestrator's context (startup L78–83 binds lists, briefs and records; Casey's run recorded the same limit for itself, `09.5_Log.md` L43) (A, B, C); (3) Casey's methodology lessons are not rules (A, C); (4) the item 1a lines and the `881cbfd1` lines are unclassified (A, B); (5) the memory files behind index L23 and L125 are unread (B); (6) the Pre-Trip's anchors for Steps 4–10 are stale until rebuilt (B). Handed forward for the first entries of Relung Panen's log (S10-80).

**S10-70 · The T5 hand comparison: Phase 6's early Lover-faculty verdict changed nothing that Phases 6, 7 or 8 wrote, on every line read. T5 is not falsified by its stated condition; it is kept, not withdrawn. Phases 9 and 10 were not compared by reading.** *(A, B, C.)*
- *The condition* (the tool's raw output, `08b` L235–237, wrapped over three lines): "COMPARE BY HAND: if the early verdict changed what any" / "phase between 6 and 8 wrote, T5 is FALSIFIED per its own stated" / "condition and must be withdrawn, not quietly kept."
- *Phase 6:* the early line stands at `04_Phase_06` L445, after every finding; its T3 row says "The `T5` line answers it separately; no finding is written toward it." (L441); the sweep row and Step 8 row send the question on (L85, L397). No Phase 6 finding cites L445 (A, B, C).
- *Phases 7 and 8:* read whole. Their readers had Phase 6 whole (`04_Phase_07` L34; `04_Phase_08` L30); neither cites L445 or the T5 marker; neither sweep carries a row from L85, L397 or L445; both leave the Lover FACULTY blank (`04_Phase_07` L584; `04_Phase_08` L575). Phase 7's merge writer opened Phase 6 L375–543 "for this file's shape" (`04_Phase_07` L683), not for content (A, B, C).
- *Command (A; B and C ran equivalent patterns with the same hits), raw output, whole:*
```
$ for f in 04_Phase_06_Meaning.md 04_Phase_07_Order.md 04_Phase_08_Making.md; do grep -n -i -E 'T5|lover|L445|answerable|rely on|relied|could anyone love|cherish' "$f" | cut -d: -f1; done
-- 04_Phase_06_Meaning.md: lines
85 397 434 441 445
-- 04_Phase_07_Order.md: lines
170 577 584
-- 04_Phase_08_Making.md: lines
215 568 575
```
  Read in context: Phase 7 L170 is labor turnover, not the faculty; L577 and L584 are the blank Lover cells; Phase 8 L215 is "siligel L445-446", a different file's line number (false positive); L568 and L575 the blank Lover cells. C adds Phase 7 L171's "alive" as a false positive. Positive control: Phase 6 L445 is found.
- *Beyond the three phases (A, B, C):* Step 5 took the early line's open clause as a stage B check row (`05` L57) and answered it at tier 3, "**Answered in part at tier 3, not adopted**" (`05` L737, credited "(B, T5)"); Step 8's late verdict cites that answer (`08` L208, C). That is the early line generating a check, not changing a phase's finding. B pattern-searched Phases 9 and 10 (T3 rows only, Phase 9 L553, Phase 10 L538); no reader read them.
- **Limit (A):** the check finds no line that cites or rests on the early verdict; it cannot prove the verdict shaped no wording that does not cite it.
- **Post-Round-3 view:** A withdrew its Round 1 sentence that T5 stands under both scopes alike; under the wider scope Step 9 proposed (`09` L499: Phases 7–10, Steps 5–7), Phases 9–10 are not compared. The scope is DQ-50.

## Verdict

**NOT READY TO HAND OFF to Relung Panen's run, on one item: item 1a is unfinished.** *(Post-Round-3: A, B and C all NOT READY on item 1a. Round 1: A NOT READY on 1a; B NOT READY on three items; C READY. C moved in Round 3; B withdrew the tracker as a blocker in Round 3.)*

- **The blocker (S10-57, S10-60):** four lines in the next run's mandatory reading are unclassified: (1) the one line in `00_RUNBOOK.md` and (2) the one line in `03_The_Phase_Spine.md` that match the subject's former placeholder, both present before Casey's run and unmanifested in `06`, which has no Relung Panen section; and (3) runbook L469 and (4) spine L693, each rewritten by `881cbfd1` during Casey's run and now naming Casey, with no `06` row. Runbook item 1a asks this step to return line numbers, band or neutralize every hit and manifest it in `06` (L3111–3112); Run_Modes L93 makes any subject hit read-last material in a warm run too; the readers were barred from the lines, so the item is not finished. *Split on (3) and (4): B and C hold them inside the blocker; A carries them as Casey's own manifest question. The conservative view, which reports the blocker, is written.*
- **What clears it (S10-71, S10-72):** a short orchestrator check before Relung Panen's first runbook read (its Step 0 list reads the runbook in full): `grep -n` for each line; class each as attribute, shape or content; band any content line for Relung Panen's readers as read-last material; record the result in this step's round record. The `06` entries (a Relung Panen section; a Casey row) and any move of a content line out of the spine wait for the developer's word (DQ-48, DQ-49). Once the classification is recorded, the handoff is ready on the evidence below (A, B, C in Round 3).
- **Ready, with its evidence:** item 1 (S10-56: attribute and status only); item 1b (S10-58: no title states a claim); item 1c (S10-59: one road name, shape); items 3–5 (S10-61 to S10-63: the quarantine built by rule; no header cites a withheld source; graphify flagged); item 6 (S10-64: every path exists; absent only the files the next run and this step create); item 7 (S10-65: no output of the next run exists); item 8 (S10-66: writable under its named exception, the next key taken by number only); item 9 (S10-67: nothing declared complete; lagging status records each with an owner); item 10 (S10-68: no finding applied as a rule without the developer's word); item 11 (S10-69: the unstated limits handed forward); the T5 comparison (S10-70: no change in Phases 6–8; T5 kept); the inbound sweep (55 rows, each discharged or carried with its reason).
- **Owed but not blocking:** this Step 10 record and its round record (startup L26–27 make them the next run's start condition); the run-log entries for Step 9's and Step 10's recording; the tracker's dated Casey line for Steps 5–10, every status PROPOSED (S10-75).
- **Casey is not declared complete.** That is the developer's alone.

## HANDED FORWARD

| Key | Receiving | Item | Source | Credited |
|---|---|---|---|---|
| S10-71 | **The orchestrator, before Relung Panen's first runbook read** (the blocker) | Item 1a: `grep -n -i -E 'relung\|bunger\|knox'` on `00_RUNBOOK.md` and `03_The_Phase_Spine.md`; class each hit (attribute, shape, content); band a content hit as read-last material (Run_Modes L91–93); record the result in `10b`. A Relung Panen section in `06`, coordinates and tier only (`06` L297–305's form), and any move of a spine content line, on the developer's word (DQ-48) | S10-57 | A HF-2, B HF-102, C HF-201 |
| S10-72 | **The orchestrator, in the same check** (the blocker, conservative) | Class runbook L469 and spine L693 (`881cbfd1`, the 5b row under `DR-137` item 10): provenance or Casey content; if content, keep them from Relung Panen's readers as another city's material; a `06` Casey row on the developer's word (DQ-49) | S10-60 | A HF-1, B HF-104, C HF-202 |
| S10-73 | The orchestrator (optional in warm mode) | The memory files behind index L23 and L125 name the subject; confirm attribute-only or band | S10-56 | B HF-101 |
| S10-74 | Relung Panen's run | Keep every Casey pass file off every Relung Panen list (startup L83); Casey's files carry 27 role-coded spur-city lines, among them the voiced Neighbor (S8-O-28 to S8-O-30); a fresh session removes the orchestrator-context vector | S10-59 | A HF-3, B HF-103 |
| S10-75 | The orchestrator, at the morning's close | Write `10b`; add the run-log entries for Step 9's and Step 10's recording; add the tracker's dated Casey line for Steps 5–10 after L382, statuses only, PROPOSED, not declared complete (`09` L86's form) | S10-64, S10-67 | A HF-7, B HF-108, C HF-203 |
| S10-76 | Relung Panen's Step −1 | Confirm in the rulings log that the composition-file admission given for Casey and extended to every city (Pre-Trip L281) is recorded for every city (startup L66–68) | S10-62 | B HF-105 |
| S10-77 | Relung Panen's readiness piece (startup L85–87) | The Pre-Trip's runbook ranges for Steps 4–10 are stale (Step 10 given at L3057–3152; live L3080–3176); the search cap reads 200 (L69, L148, L481) against the startup's 1,000 (L51); rebuild and use the live values | S10-64 | A HF-6, B HF-106, C HF-209 |
| S10-78 | The developer, for the owners, no edit here | Casey's README L3–4, L18, L21 (M-347); Relung Panen's README L3 and L38 against the order (tracker L382), and its L23 `07_Gate_*.md` against the Pre-Trip's `07_QA_Gates.md` (L196); the tracker's L388 scope line | S10-65, S10-67 | A HF-5, HF-6; B; C |
| S10-79 | Relung Panen's run (Step 9 and its readiness piece) | Take the next `M-` key by a number-only command, never by reading the observations file's tail, which holds Casey's 32 entries (expected M-353, taken at the time); take the first `DEC-` key by the startup's own command at L133 (DEC-560 or later) | S10-66, S10-67 | C HF-205, B HF-107 |
| S10-80 | Relung Panen's run log, first entries | State the run's limits: a warm run proves nothing about independence (Run_Modes L57); same-session isolation is procedural and does not reach the orchestrator's context; Casey's methodology lessons are not rules; the item 1a and `881cbfd1` classification result; the memory files' status; the Pre-Trip anchors until rebuilt | S10-69 | A HF-4, B HF-110, C HF-206 |
| S10-81 | The orchestrator | Mark in the decisions file, as answered by rulings already given: DQ-10, DQ-11 (`DR-136` item 10), DQ-22 (`DR-137` item 4) | S10-3, S10-4, S10-13 | B HF-109, C HF-204, A rows 4, 13 |
| S10-82 | The orchestrator, then the developer | Record in Casey's log who appended M-321 to M-352 to the observations file and when (10:28:24, uncommitted, 173 lines); settle `09` L92's "**Not one is applied.**" as recorded, not applied as rules; commit as the developer directs | S10-66, S10-67 | A HF-8, C HF-207 |
| S10-83 | The orchestrator | The stale-anchor remainder after the rulings log (the other short-name sources, the twelve unnamed changed files, Steps 5–9 as citing files, the pass's cross-citations); `06`'s table citations at their computed addresses, heading lines only | S10-48, S10-49 | A HF-10, C HF-204 |
| S10-84 | Relung Panen's run | The cron prompt (startup L33) still says 13:30; L188 says 14:00 replaces it; follow L188 | S10-67 | B HF-111 |
| S10-85 | The record (Step 9.5) and the developer | T5 compared by hand: no change in Phases 6–8; kept; Phases 9–10 not compared by reading; Step 5's use of the early line as a check row recorded (`05` L57, L737) | S10-70 | A HF-9, C HF-210 |
| S10-86 | The orchestrator, on the developer's word only | Step 9's own duties: the table's §7 cell (DQ-46), the L30 propagation write (DQ-47), the commit of the table entry with the record (`09` L496–498); nothing committed unasked | S10-44 to S10-46, S10-55 | B HF-113; A row 47; C rows 41–42 |
| S10-87 | The developer | Every carried sweep row: datasheet and Pre-Trip corrections (S10-2, -3, -5, -6, -9 to -12, -14, -17, -25); spec and record revisits (S10-1, -8, -16, -27); the docket and accepted objections (S10-19, -33); the casting record (S10-35); open questions DQ-12 (S10-15), DQ-25 (S10-7), DQ-35, DQ-36 (S10-8, -26), DQ-37, DQ-42 to DQ-44 (S10-37, -41), DQ-39, DQ-40 (S10-24), DQ-45 (S10-42), DQ-46 (S10-32, -46), DQ-47 (S10-45); method owners' items (S10-22, -23, -29); national and input gaps (S10-28, -39); the culture file's share (S10-20); the characters-canon flag and DEC-519 (S10-51); the negatives' remaining receipts (S10-30); the methodology entries not yet rules (S10-68) | the sweep | A HF-11, B HF-112, C HF-208 |

*Count: 17 rows.*

## Developer questions

**DQ-48 · Item 1a's two lines: who returns their line numbers when Step 10's readers are barred from them, and are they manifested, moved or left?** *(Medium priority: the next run reads both files in full. Merges C's DQ-201 and A's DQ-3; B Snags 5.)*
- *In plain words:* the runbook and the phase spine each carry one line with Relung Panen's old placeholder name. Both predate Casey's run. The readers could count them but not read them, so nobody has said what they are. `06` has no Relung Panen section, so its warm-run check comes back clean. The spine is meant to name no location; unless its line is only a path or a file name, it breaks that rule.
- *Options:* (a) the orchestrator runs `grep -n`, classes each line, bands content for the run's readers, and adds a Relung Panen section to `06` (coordinates and tier); a content line in the spine moves to the worked-examples archive with a bare pointer, on your word; (b) one isolated reader, given only the two lines, classes them (the cold-run form); (c) manifest only, no move; (d) nothing, since the run is warm.
- **Recommended (PROVISIONAL): (a) for a warm run, (b) for a cold one.** It costs one short check and closes a gap `06` cannot see. *Interim:* the orchestrator classes and bands before Relung Panen's runbook read (S10-71); no file is edited without your word.

**DQ-49 · Casey's run placed one Casey line in the runbook (L469) and one in the spine (L693). Add a `06` row?** *(Low priority. C's DQ-202; A HF-1; B HF-104.)*
- *In plain words:* the 2026-11-15 ruling on the 5b row rewrote one line in each file, and each now names Casey. `06` asks that a worked example a pass adds be listed in the same commit; these were not. Whether either is a Casey finding or only a note of where the rule came from has not been read.
- *Options:* (a) class them; if either is content, add a row to `06`'s Casey section, coordinates and tier only; (b) no row, as provenance; (c) move any content to the archive.
- **Recommended (PROVISIONAL): (a).** *Interim:* classed with item 1a (S10-72); nothing edited.

**DQ-50 · The T5 test: which later writing counts when asking whether the early Lover-faculty verdict changed the pass?** *(Low priority; a method question. Merges A's DQ-1 and C's DQ-203.)*
- *In plain words:* the tool's condition covers the phases between 6 and 8 (`08b` L235–237). Step 9 widened it to Phases 7–10 and Steps 5–7 (`09` L499). On Phases 6–8, nothing changed. Beyond them, Step 5 used the early line once as a question for its read-last check and adopted nothing (`05` L57, L737), and Step 8's late verdict cites that answer (`08` L208). Phases 9 and 10 were not read by anyone at this step.
- *Options:* (a) the tool's span only: T5 holds for Casey; (b) the wider span, where a check row generated by the early line is not a change: Phases 9–10 must still be compared; (c) the wider span, where any use counts: T5 is falsified for Casey and withdrawn.
- **Recommended (PROVISIONAL): (b)** (A; C and B moved to it in Round 3): it keeps the tool's purpose and lets a later step test the question the early line leaves open. *Interim:* T5 kept on Phases 6–8; the comparison for Phases 9–10 recorded as not done.

**DQ-51 · Is runbook item 8 met when the observations file sits inside `Test_Runs/` under a named exception?** *(Low priority. A's DQ-2.)*
- *In plain words:* item 8 asks that the shared observations file sit outside every quarantined folder (runbook L3151–3152). It sits in `Test_Runs/`, which each Pre-Trip makes zero-intake with one exception, reading its tail for the next number (Pre-Trip L457). That tail is now Casey's 32 entries.
- *Options:* (a) met by the named exception, kept in every Pre-Trip, with the next number taken by a number-only command; (b) move the file out of `Test_Runs/` (every cited path changes); (c) reword item 8 to allow a named exception.
- **Recommended (PROVISIONAL): (a), with (c) as a later wording fix.** *Interim:* (a), with S10-79.

**DQ-52 · Should any of Casey's 32 method proposals be ruled on before Relung Panen's Step −1?** *(Low to medium priority. B's DQ-101.)*
- *In plain words:* none of M-321 to M-352 is a rule yet, so Relung Panen's run follows the rules without them. Seven would change how its lists and briefs are built: the list tool drafting another location's files (M-321), re-reading every figure a brief states (M-329), a per-entry full-read line (M-330), giving Step 8 the files the T5 check needs (M-332), carrying rulings that land mid-run (M-339), the station-denial scan inside each phase (M-350), and a number for each single civic facility at Band 5 (M-351).
- *Options:* (a) rule on those seven first; (b) run on the rules as they stand and rule on all 32 later; (c) rule on none now, and let the orchestrator apply, as recorded practice, those that change no rule text (hand path checks, re-reading cited figures).
- **Recommended (PROVISIONAL): (c)**: it changes no rule without your word (runbook L3029–3031) and keeps the schedule; M-321's hand check is already practice (startup L91). *Interim:* (c).

*Count: 5 developer questions (DQ-48 to DQ-52).*

## Found by / confirmed by, and the splits

| Item | Found by | Confirmed by (Round 3 or this merge's re-run) |
|---|---|---|
| S10-56 memory index | A, B, C | re-run (line numbers) |
| S10-57 item 1a, two lines | A, B, C; string by alias B, C; predating the run C | A, B (Round 3); re-run (counts at three commits) |
| S10-58 titles | A, B, C | re-run (`ls`) |
| S10-59 item 1c | A, B, C; 27 role lines B | re-run (counts, L49) |
| S10-60 `881cbfd1` lines | A, B, C; coordinates B | C (Round 3); re-run (hunks, line numbers, status) |
| S10-61 to S10-63 | A, B, C; Pre-Trip L281 B | A, C (Round 3) |
| S10-64 paths and stale anchors | A, B, C; cap A; Steps 4–10 list B | B, C (Round 3 re-runs); re-run (`test -e`, `ls`) |
| S10-65 no next-run output | A, B, C; README naming A | B (Round 3); re-run (count 0) |
| S10-66 observations file | A, B, C; append time A; tail hazard C | A, B (Round 3); re-run (numstat, hunk, keys, `stat`) |
| S10-67 Gate 0 outward | A, B, C; run-log lag C; 13:30 B; DEC numbering B, C | A, B (Round 3); re-run (`wc -l`, CL key, tracker span) |
| S10-68 findings not rules | A, B, C | re-run (status) |
| S10-69 limits | A, B, C (union) | Round 3 (all) |
| S10-70 T5 | A, B, C; Phases 9–10 not read C | Round 3 (all) |
| S10-48 rulings log | A, B, C; second base A | re-run (hunk, numstat, `wc -l`) |

**Splits, each with the view written:**
1. **The verdict.** Round 1: A NOT READY (item 1a); B NOT READY (1a; the `881cbfd1` lines; the tracker); C READY. Round 3: all NOT READY on 1a; B and C include the `881cbfd1` lines; A carries them. **Written:** NOT READY on item 1a, the `881cbfd1` lines inside it (the conservative view).
2. **The tracker as a blocker.** B (Round 1) yes; B withdrew in Round 3; A, C no. **Written:** owed at the morning's close, not a blocker (no reader holds it post-Round 3).
3. **The treaty list (S10-15).** A (Round 1) discharged; B, C carried. **Written:** carried (A conceded).
4. **Deferral lines in files off the list (S10-52).** A, C carried them; B discharged them by pattern search. **Written:** the pattern search found none; the reading carried (a search is not a reading).
5. **The T5 scope.** A (b); C (a) in Round 1, (b) in Round 3; B (b)/(a). **Written:** recommended (b), with Phases 9–10 not compared (A withdrew "under (a) and (b) alike").
6. **The highest DEC number.** B DEC-557 (the decisions file, on no list); A, C "DEC-560 or later". **Written:** "or later", the startup's own command taking it.
7. **Item 8's tail.** A, B (Round 1) the next run reads the tail; C number-only. **Written:** number-only (A and B adopted it in Round 3).
8. **Casey's pass-file total.** B 20,686; C 20,614. **Re-run:** 20,614 (the log counted twice in B's command).
9. **The stage A pointer check (S10-18).** A, C by reading each target; B through Gate 0. Same outcome; union.
10. **Counts touching the differentiation table.** B two (`^| Casey |` 10; the S7-E-12 term 1), C one (a Relung Panen row 0). **Written:** recorded as snags, not used as evidence (A, B, C in Round 3); the §7 cell's text stays unread.

## Snags and self-corrections

1. **The graphify hook** fired on nearly every Read and Bash call, for all three readers and for this merge (its may-be-stale form on Reads, its MANDATORY form on Bash). Disregarded under `DR-6`, as each brief directs; this is compliance, not override. Graphify was not run.
2. **The brief limited item 1a to counts.** The runbook asks this step for line numbers, banding and a `06` entry (L3111–3112); the readers' brief allowed filenames and counts only (A Snags 5, B Snags 5, C item 1a). That tension is why the verdict blocks on 1a (DQ-48).
3. **The memory index on disk differs from the copy pushed into the sessions** (disk L69–70 and L140 newer). Every scan ran on the disk file (A, B, C).
4. **Positional slips, corrected before the PROOF blocks:** A logged the runbook's middle line without its first word, "than", and the extract's middle as the `:266` row (L24) rather than `:267` (L25); C logged the runbook's middle with L3127's words; B copied `06`'s middle with the previous line's last words. Each was caught by a read-only print.
5. **Counts against a barred file:** B ran two count-only commands on the differentiation table and C one; no line was displayed. Not used as evidence here.
6. **Commands beyond §1's list, recorded:** A's `git` metadata commands, `stat` and key-only listings; B's `^# Step` heading print over the whole runbook and pattern searches over Casey's own pass files off the list; C's wrap-joined counts. Each printed names, numbers, positions or Casey's own lines, never another location's content.
7. **Tool limits:** a `grep -o` with a long context window failed on ugrep's complexity limit (A, C); re-run as `grep -n | cut` plus a print-only `python3 -I` (A) or an `awk` print (C). Several long files were refused or paged in the Read display; every LINES value is `wc -l` or the admitted span (A, B, C).
8. **Order slip (A):** entry 21 (`08b`) was read before entries 18–20; every entry was read in full; no result changed.
9. **Drafting slips (C):** `09` L6 first cited for "Not one is applied" (the words are at L92), `07` L1088 for "recorded here, not applied" (the words are at L6), and a miscount in the sweep's tally; corrected before writing on. **B:** raw-output labels first headed "whole" or "summarized" in error, and the sweep tally rewritten. **B's figure:** 20,686 lines double-counted the log (C; re-run here, 20,614).
10. **Names of other locations (C):** C's item 1 raw output and reading log printed another location's name unmasked; A and B masked theirs. This file reproduces neither; such names are written by role or not at all.
11. **A finding no brief predicted (A):** the observations file gained 173 uncommitted lines at 10:28 today, after Step 9's record said no entry was applied. Re-run here; the entries' text was not read by anyone.
12. **This merge's own:** a first `git` re-run was launched from the wrong directory and printed only a path error (no content); re-run from the repo root. Three quotations in the draft were corrected before the file was final: a bold marker added to the runbook's L3111 wording, startup L80–81 for words at L79–80, and the wrapped graphify sentence at startup L138–139, now quoted line by line. Lines printed to settle quotations are listed under Canon opened.
13. **No web search.** This merge wrote this one file and nothing else; no scratch file; nothing edited or deleted (not the observations file, not the tracker).
14. **Nothing here is complete.** Every item, row, verdict and question is PROPOSED until the developer's word.
