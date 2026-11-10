# Davis cross-check of 2026-11-09: recording-law log

**What this is.** The Step 9.5 recording law (`00_RUNBOOK.md` L3039-3076) applied to the Davis cross-check: what happened, not only what worked. Entries are written when they happen. They are PROPOSED observations; none is entered in the shared observations log (`DR-116` item 2: the Step 9 and 9.5 updates live in a separate piece file). Each entry has its own prefix, `DVL-`, because the series prefixes (M-, R-, Q-, PA-, RF-, DR-, DEC-) belong to the shared files (`T8_Standing_Brief_Lines.md` line 17).

**Names.** This file names no other city. Another location: not used.

---

## Exposure ledger (what the orchestrating session read beyond Davis's own material)

Written because a later session that runs another city in this same session needs to know what this session has seen. **Nothing below was used in any Davis brief or reader list, and nothing below may enter any later city's brief.**

| # | What was read | Why | Where it sits |
|---|---|---|---|
| E-1 | `MASTER_Process_Tracker.md` L137-232 and L355-405 (the session boot and the resume block) | The startup file's reading list item 4 | L383 is a long dated record of another location's pass; read in full while reading the block; not used |
| E-2 | `Research_Logs/Drift_Review_SUMMARY_Finished_Passes_2026-11-03.md` (56 lines, all finished passes) | The startup file's reading list item 5, "for scope" | It states, for each of the other finished cities, what the 2026-11-03 review expects to change; not used |
| E-3 | `REPASS_COMPLETE_2026-11-04.md` in another location's pass folder (57 lines) | The startup file's reading list item 6, method only | It states that location's findings as well as the method; only the method was taken (the unit shape, the dispositions, the order of checks); not used |
| E-4 | A file-name listing (first 50 names, no content) of that other location's pass folder | To see the shape of a repass's files | Names only |
| E-5 | `STP-06 README` L44-47 (the character draft sited in Davis) | Verifying DV-029 against the live file | L45-47 name another city and quote one of its figures; no use made; the readers' lists stop at L45 |
| E-6 | `git status` and recent commit subjects at session start; the file list of commit `8777bb5f` | The session's start-up context and the change check | Subjects name other locations' work; no content used |
| E-7 | `DEVELOPER_RULINGS_LOG.md` `DR-100` to `DR-123` ranges as listed in the startup file | Reading list item 2 | Rulings; some are about another location; only the general rules are used |

---

## Entries

### DVL-1 · A technique that worked, and what it could not do
The 2026-11-03 note was checked by a read-only script (55 line checks that print OK or DIFF and never print another location's text, plus a recomputation of every derived figure). All 55 passed. **What the script could not see:** text that changed on a line the note did not cite. The three post-note source changes (the census tag sentence, the other location's Register row and relationship line, the character draft README) were found by asking git what changed after the note's commit time (`git log --since`, then `git show --stat` of the one commit), not by the line checks. Lesson: a line check proves cited lines; a commit-bounded diff finds uncited changes. Both were needed.

### DVL-2 · Self-correction (the diaspora file in the reader list)
**What I believed:** the Pre-Trip lists `City_Refugee_District_Affinities.md` as a required input to Phase 2, because the list generator printed it. **Why it was wrong:** I took two grep hits (Pre-Trip L277 and L413) as input rows without reading the ⛔ marker on them, which is the same error the generator makes. **What changed it:** reading both lines in context (L270-282): the Pre-Trip marks the file "RESOLVES TO NOTHING ADMISSIBLE" and its Phase 2 T8 line names five admissible rows that exclude it. The fault is the tool's. Corrected in `Amendment_Notes_2026-11-09_Cross_Check.md` D.1 in the same turn.

### DVL-3 · Tool defect (reader-list generator)
`Tools/make_t8_required_list.py phase:2` writes a path the Pre-Trip row marks ⛔ into the draft list, because it extracts every backticked absolute path from the phase's table rows. Last changed 2026-10-21; no uncommitted edits. Every list in this run was built by hand from the Pre-Trip's own admissible rows, and the file was excluded. The tool is not edited here (DEC-280).

### DVL-4 · The startup file's premise was partly stale for Davis
The startup file says the 2026-10-30 amendment notes are stale after the population rework, the relocation of 2026-11-02 (`DR-90`), the robot term, the language rule and the Register changes. For Davis that is no longer so: the note carrying that file name was rewritten under `DR-102` and committed 2026-11-03 22:34 with every one of those changes in it. Only three source edits and the character README changed after it. The file name still carries 2026-10-30, which is what misleads. The fresh note therefore is a verification plus the delta, not a rewrite.

### DVL-5 · Environment: the shell's working directory drifted
`cd` in one Bash call persisted into the next, and the working directory changed several times during the reading. From the first reader dispatch on, every path in every tool call is absolute.

### DVL-6 · Process: the first brief generation had quotations without source pointers
The first generation of the 12 briefs quoted nine pass phrases in the "test in particular" prompts with no pointer to an admitted line (`T8_Standing_Brief_Lines.md` line 18). They were rewritten as unquoted statements with pointers and regenerated before any dispatch. No reader received the first generation (the brief hashes of nine items differ between the two generations; the dispatch prompts carry the second).

### DVL-7 · Environment: the graphify hook
The `PreToolUse` hook printed MANDATORY notices on essentially every call. The orchestrator read named files at named ranges and ran git commands, and did not run graphify (the startup file says using it for orchestration is fine, not required). The readers' prompts carry the `DR-6` line and the briefs carry standing line 3, so disregarding the hook is compliance for them.

### DVL-8 · Clock
Window check at 05:03 and 05:14 on 2026-11-09 (inside 05:00-14:59). No new piece starts after 13:30; wrap-up from 13:59.

### DVL-9 · The 12 item checks: result and what the result is not
All 12 readers returned within about 13 minutes of dispatch (05:14 to 05:27). Verdicts: `FLIPS` 3 (C-1, C-5, U-1), `NARROWS` 9, `STANDS` 0, `CANNOT-TELL` 0; confidence high 6, medium 6. Every PROOF block of every output matched ground truth (mechanical check, `triple_read_verify.py` with the one reader's file in all three slots, a use the tool was not built for; it worked). **What the result is not:** a count of changed findings. The brief's rule sends `NARROWS` to re-derivation by design, so a `NARROWS` can mean one false sentence on a finding whose core stands (for example U-2, U-5, C-7); the readers' own words say which. The first check also found that the original startup expectation (Phase 2, then Phase 5, then the language lines) was incomplete: it did not name the export headcount (U-1), the Step -1 composition region (U-4), the character sweep (U-3) or Step 5 (U-5).

### DVL-10 · Errors in my own briefs, found by the readers
(1) **U-1:** the brief said the pass refuses the export headcount because the denominator is unsettled; the pass says the denominator is not the blocker (04_Phase_07 L104-106, L407). I wrote the brief from the drift review's summary, not from the pass. The reader tested the pass's own ground and said so; the verdict does not depend on my framing. (2) **C-4:** the brief listed "the weights/headcount point" as a ground the pass states; the reader found it at none of the cited lines (it is a ground the ruling keeps, which the pass never states). (3) **C-6:** the brief said the items are in section C of the fresh note; rulings and the 2026-11-03 note call the list "section F" (the fresh note restates F as its section C). (4) **U-5:** the brief's list of Step 5 findings omitted the "no character sited" row; the reader tested it anyway. **Lesson, for the next brief:** state a pass's ground by reading the pass lines, and say "section F (restated as section C of the fresh note)".

### DVL-11 · Reader departures from the brief, all minor, all recorded by the readers
C-6 ran one command that touched spec L4 and L9 (printing only a combined byte count, 272) and loaded source files whole inside verification scripts that printed only OK flags: no struck text was seen. C-2 and C-4 each wrote a helper script in the staging folder (the brief said the output file is the only file written); both are kept as `.t8_check_C2_helper_c2_calc.py` and `.t8_check_C4_helper_c4_spread.py`. U-5 wrote a temporary field list and removed it. U-1 noticed another reader's output file in the shared staging folder and did not open it. **Change made:** the re-derivation pieces use one private staging folder per reader.

### DVL-12 · Stale citations the readers found in the pass (not drift of input; recorded for the docket)
The pass cites `No_National_Stereotypes.md` as 172 lines and by line numbers that are now two lower than the file's (174 lines); it records `02_Spine.md` as 585 lines (584 now); it cites the Davis spec's founding line as L127 (now L151); the Step -1 contract carries both pass-time and current numbers for the spec (L143 and L167; L176 admitted at one place and excluded at another). These belong to the citation-hygiene item (W-6 of the drift review), which no check owns.

### DVL-13 · Character sweep, run by the orchestrator for the P10 piece
`grep -rIl --include=*.md Davis` over the game repo's `Worldspace/Characters/` returned four files, all in one character draft folder (its README and three files under `Personal_Background/`); over the universe repo's `Worldspace/Characters/` it returned zero; `Enneagram_Character_Index.md` (35 lines) has zero Davis hits. Filenames only were listed; to place the hits the orchestrator then printed the matching lines of the three background files, and those lines name another city and quote one of its figures (exposure E-5, extended). Nothing from them is used.

### DVL-14 · Template bug caught by reading a brief before dispatch
The piece brief's output-format heading printed a literal `%s` instead of the piece id. It was found by reading the generated S1 brief end to end before any dispatch, fixed in the generator, and all four briefs were regenerated (so the frozen brief hashes are the second generation). Reading one generated brief before dispatching its twelve readers cost one minute.

### DVL-15 · Verifier hazard noted by a reader (not a failure)
The U-3 reader flagged that a middle line containing the literal token `EXEMPT:` mid-line could be cut short by the verifier's field stop. The verifier passed that block anyway. Recorded as a hazard to watch, with no evidence it fails.

### DVL-16 · Self-correction: I described a piece's contents from a one-line summary
**What I believed:** I could write the P89 record's snag about its developer question and its research from the merge writer's one-line report. **Why it was wrong:** I described the question's reasoning in my own words, and the research as comparables for "how supporting languages work", neither of which I had read. **What changed it:** reading the piece's section 8 and its question 7 after the record was written (the question is a split between routing claims of distinctiveness to the terminal check and taking the peer-free side; the research is on new-dialect formation in new towns). Corrected in the record the same turn. **Rule for the remaining records:** a record states what a tool returned and what the piece says on a line I have read, never my gloss of it.

### DVL-17 · A ruling that settled an open question was missing from two reading lists (found at Round 3 of the Phase 2 piece)
**What happened.** `DR-85`'s not-decided row asks whether China's four pieces and Taiwan decline too; `DR-94` item 4 (LOG L1613) decides it the same day (Manchuria declines; Mongolia, East Turkestan, Tibet and Taiwan do not). The S1 and language-piece reading lists had `DR-85` and not `DR-94`. The first check's reader for the contract item asked the question from `DR-85`; the S1 piece carried it as reserved; the S1 piece's reading was then passed to the Phase 2 and language briefs as an orchestrator-verified result. The Phase 2 piece's list contained `DR-94`, so its readers B and C caught it at Round 3 (XB-139) and the merge recorded it as superseded (docket row AM-P2-D112). The language piece, whose list lacked `DR-94`, built a Mandarin flag on the premise. **Class:** error in my reading-list construction (a later ruling on a question that an included ruling lists as open). **Fix:** `Amendment_Erratum_2026-11-09_DR94_Item4_Four_Rows.md` states the current fact and lists every place; the pieces are left as written. **Lesson, for later lists:** when a list includes a ruling, scan the log for later rulings that answer a question that ruling lists as not decided; the ruling log has a "Not decided" row on most entries and the next entries often settle them.

### DVL-18 · The developer's walkthrough of Davis, first batch of answers (2026-11-09, 17:19, outside the derivation window; answers and one correction, no derivation)
Answers the developer gave in this session. They are not yet entered in the decisions file (to be entered in one batch when the walkthrough ends).
- **Export headcount (DEC-329, 330, 333, 335, 336):** confirmed. 186,131 workers with its formula beside it, the dated 44.2% beside it, "to the rest of the Federation" or "national supply" for the word export. No count of persons until the formula's source file is read.
- **People-fed figure (DEC-331, 332):** not yet. No people-fed number and no difficulty factor chosen.
- **Character draft (DEC-354, 355, 357, 358, 363):** a documentation note, status left to the developer, roster ID only, present-day only.
- **Credit kinship (DEC-368):** hold until Chapter 11 is read and the developer rules. No Chapter 11 piece is queued.
- **Composition bar (DEC-291, 292, 301, 302):** the review's reading is confirmed as it stands.
- **"Records can draw people" (DEC-307):** the developer ruled it a GENERAL mechanism. This differs from the recommendation (specific to the location it names). Davis may use it.
- **Port ruling of 2026-09-16 (DEC-316, 369):** "Vladivostok-style" is the developer's own phrase. "Principal import port" was not the developer's wording. The Davis spec as written can be considered correct, and it is open to further additions on top of what it says (so the route through the two neutral hubs stands as the spec writes it). The verbatim words of the ruling are not stored anywhere found; the developer's answer above is the record.
- **Check-file correction (DEC-366, 367, 373), done on the developer's word:** `Local_Cultures/Mirny_Subnet/Davis.md` lines 45, 47 and 61 were corrected (still 309 lines; `git diff` shows 3 lines changed). Line 45 now states the name as a naming fact only (DR-28 item D2). Line 47 states the founding nation as Australia on the Register's ground of geography and access (the station operator is no longer the stated ground). Line 61 now gives the spec's dates and states both counts ("about 54 to 55 days depending on whether both end dates are counted"); its second sentence, which the pass quotes, is untouched. Line 53 was not touched. No pass file, spec or source file was edited.

### DVL-19 · The walkthrough, second batch: tool fix, rule drafts, pointer-line batch (2026-11-09, evening; edits and decisions may run at any hour, `DR-117` item 4)
- **Developer's answers:** a Davis-built robot's vernacular is Hawaiian (later Tepenian) plus the builders' language (DEC-342, 347 answered yes). Approved: fix the reader-list tool (DEC-280), write the six process lessons into the rules (DEC-281 rows 1 to 6), and make a numeric read spec name its numbering frame (DEC-289). NOT approved: the mandatory character-folder sweep in Phase 10 (DEC-356). The roughly sixty remaining questions: the developer wants to go through them together, not approve them in bulk. The pointer-line batch for Davis: prepare it now.
- **Tool fix (DEC-280), done:** `Tools/make_t8_required_list.py` now skips a Pre-Trip table row whose status cell has the stop sign and says WITHHELD or RESOLVES TO NOTHING ADMISSIBLE, and reports it as a comment. Tested by running the tool on Davis for ten targets before and after: only Phase 2 changed (the forbidden file became a comment, 10 entries to 9); the other nine outputs are byte-identical (diff 0). The tool has no self-test of its own; this before-and-after comparison is the check. A first test command of mine contained a stray `rm`, which the project hook blocked; nothing was deleted and the test was re-run without it. The original is kept in the scratchpad.
- **Rule drafts (DEC-281 rows 1 to 6, DEC-289), NOT applied:** `Research_Logs/Lessons_Into_Rules_Draft_2026-11-09.md`, shown to the developer first as on 2026-11-04. While drafting, one origin note was wrong (I had written a cause for the private-staging lesson from its title); it was corrected from this log's entry before the draft was shown.
- **Pointer-line batch, prepared, NOT applied:** `Amendment_Pointer_Lines_Batch_2026-11-09.md`, built by script from section 4 of the seven pieces: 390 docket rows, of which 321 name a pass file (12 files, plus the record and readiness-check files in the short form), 34 name a source file, 27 name a check file (three of them done today), 4 go only into the amendment note, 1 names a method file and 4 are routing notes.

### DVL-20 · The developer's decisions applied (2026-11-09, 18:44 by the clock reading, after the walkthrough)
On the instruction "apply the decisions I've made": the seven rule rows were applied as drafted (lines 21 to 25 of `T8_Standing_Brief_Lines.md` part B; rules 5 and 6 of `Amendment_Layer_Rules.md`; observation entry `M-320`), with hashes of the three files checked before the edit and the diffs checked after (additions only). One departure from the draft: the numbering-frame rule went to the amendment-layer file, because the rule it extends is written in no rule file and a runbook insertion moves every cited line. `Amendment_Answers_Applied_2026-11-09.md` records where the developer's answers differ from what the pieces proceeded on (four places; one of them, the "records can draw people" ruling, means the station-inheritance finding and its docket row need a re-read before the docket is applied). Not applied, because not decided: the pointer lines, the source fixes, the other 24 check-file corrections, any pass-file edit. The ruling log entries are `DR-124` and `DR-126`.

### DVL-21 · The walkthrough, Phase 2 group (2026-11-09, evening)
The developer answered the establishing country (left open), robots and a row's origin practices (left open, sized on humans), a human exile's origin row ("the origin row applies to both humans and robots"), and gave new canon: humans could continue arriving after the signing and were not allowed back to Upper Earth. The thirteen wording and method questions were left provisional at his word. Recorded as `DR-127` and `DR-128`; `Amendment_Answers_Applied_2026-11-09.md` lists the places in the Phase 2 piece that need a re-read. Nothing in any piece was edited.
