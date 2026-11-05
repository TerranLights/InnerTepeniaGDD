# Lessons into rules — edits preview (2026-11-04)

> **STATUS: PREVIEW. No rule file in the repo has been changed.** The edits exist only as copies in the scratch
> folder. This document shows every inserted block, the new file in full, and the raw check output. **Nothing is
> applied until the apply script is run, and that script refuses to run if any original has changed since the
> copies were made.**
>
> **Inputs:** the draft `Research_Logs/Lessons_Into_Rules_Draft_2026-11-04.md` (its table, Conflicts and risks,
> and Application plan), and the developer's decisions `DR-116` and `DR-117` (`DEVELOPER_RULINGS_LOG.md`
> L1809–1825), as given row by row for this step.
> **Base commit:** `8777bb5f`. The eight target files had no uncommitted changes when they were copied.

## 1 · Summary

| | |
|---|---|
| **Rows applied** | **43**: every row the draft marks NEEDS RULE TEXT, including the partial ones, except the two struck. |
| **Rows struck** | **M-281** and **OBS-4** (struck by the developer); **OBS-14** (marked "not for the rules"; struck and not logged). |
| **Rows left without rule text, as the draft proposed** | MP-1, MP-2 (tool fixes already in place); MP-4, MP-5, MP-8 to MP-14, MP-16 to MP-19, M-276, M-277, M-299 (already in the rules); MP-6, MP-15, M-255, M-258, M-262, M-265, M-304, OBS-16 (not for the rules); the 24 duplicates, which are covered by the row they duplicate. |
| **Files edited** | 8: `T8_Standing_Brief_Lines.md`, `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md`, `03_The_Phase_Spine.md`, `04_QA_Gates_and_Differentiation.md`, `Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md`, `Mechanical_Extraction_Field_Guide.md`, `00_RUNBOOK.md`, `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` |
| **File created** | 1: `Universal_Location_Methodology/Amendment_Layer_Rules.md` (56 lines), for the amendment-layer rules (`DR-117` item 3). The runbook gets only a one-line pointer to it. |
| **Lines** | **+98 / −17** in the eight edited files (net **+81**; an in-place change counts as one line out and one in), plus **56** in the new file. Per-file counts are in section 4, check (3). |
| **Observation log** | 15 entries appended after M-304, **M-305 to M-319**: the 14 OBS entries other than OBS-4 and OBS-14, and one entry (M-319) that records this methodology change itself. The status line and the pointer stay last. |
| **Checks** | American English sweep: **0 hits** on 155 lines, positive control passed. Layering: **no new location name** in `03`, `04` or the standing lines. No file outside the list was touched. Raw output is in section 4. |

### Where each row went

| Row | File | Where (original line) | Row | File | Where (original line) |
|---|---|---|---|---|---|
| MP-3 | PTR | T5, L448–449 replaced; L451 one phrase | M-282 | SBL | §B, line 17 |
| MP-7 | RB | Step 7, L2927 (first sentence amended) | M-287 | `04`; RB | Gate 0, after L106; Step 9 item 3, after L3007 |
| M-247 | PTR | §6a, L801 in place; box sentence after L795 | M-291 | RB | Step 4 standing reminders, after L2694 |
| M-248 | PTR | §6a, L807 in place | M-300 | SBL | §B, line 18 |
| M-250 | PTR | §N.2 box, after L684 | M-301 | SBL | header, after L5 |
| M-251 | MEFG | after L203 (end of the compliance check) | M-302 | new file | rule 1 |
| M-252 | `03`; RB; PTR | L855; §C.8c L1979; L965 (all in place) | M-303 | new file | rule 4 |
| M-254 | SBL | §A, line 10 | OBS-2 | SBL; RB | after L38; Step 4 table L2711 (clause) |
| M-256 | PTR; RB | after L684; L2713 (clause) | OBS-3 | RB | §9.5, after L3034 |
| M-257 | SBL | §B, line 12 | OBS-5 | new file | rule 3 |
| M-259 | PTR; RB | §N.2 item 2, after L678; L2713 (clause) | OBS-6 | SBL | §B, line 19 |
| M-260 | PTR | Round 2, after L618 | OBS-7 | SBL | §B, line 20 |
| M-264 | SBL | §B, line 13 | OBS-8 | SBL; PTR | quotation-audit row L30 (in place); T6, after L326 |
| M-266 | SBL | §B, line 14 | OBS-9 | `04` | Gate C, after L330 |
| M-267 | RB | Step 5, after L2868 | OBS-11 | RB | Step 9 item 5, after L3015 |
| M-268 | `03` | Phase 10 §B3, after L1171 | OBS-13 | new file | rule 2 |
| M-270 | SBL | §B, line 15 | OBS-15 | SBL | §A, line 11 |
| M-271 | RB | Step 5, after L2877 | R-1 (`DR-107`) | RB | Step 4, after L2724 (between the T8 block and the close-out check) |
| M-272 | RB | Step 6, after L2920 | *(pointer)* | RB | after L3150, before "# Where everything lives" |
| M-273 | RB | Step 6, after L2918 | *(consequential)* | RB | Step 4 table L2709: "the nine lines" corrected (not a draft row; see section 5) |
| M-274 | SBL | §B, line 16 | | | |
| M-275 | QRD | III.2 step 3 (L60–61); III.3 box after L65; Large row L68 | | | |
| M-278 | RB | Step 8, after L2965 | | | |
| M-279 | RB | Step 7, after L2928 | | | |
| M-280 | RB | Step 8, after L2979 | | | |

`SBL` = `T8_Standing_Brief_Lines.md` · `PTR` = `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` · `RB` = `00_RUNBOOK.md` · `QRD` = the differentiation quick reference · `MEFG` = `Mechanical_Extraction_Field_Guide.md`.

### The standing lines: numbers as applied (changed from the draft's numbering; see section 5, item 6)

| Line | Row | Draft's number | Line | Row | Draft's number |
|---|---|---|---|---|---|
| **10** (§A) | M-254 | 10 | **16** (§B) | M-274 | 15 |
| **11** (§A) | OBS-15 | 20 | **17** (§B) | M-282 | 16 |
| **12** (§B) | M-257 (+ M-253, M-261, M-297) | 11 | **18** (§B) | M-300 | 17 |
| **13** (§B) | M-264 (+ M-289) | 12 | **19** (§B) | OBS-6 | 18 |
| **14** (§B) | M-266 | 13 | **20** (§B) | OBS-7 | 19 |
| **15** (§B) | M-270 | 14 | | | |

Lines 1 to 9 keep their numbers.

### The observation entries as numbered

| Entry | Source | Entry | Source |
|---|---|---|---|
| M-305 | OBS-1 (rule: R-1, `DR-107`) | M-313 | OBS-10 (rule: with M-280) |
| M-306 | OBS-2 (premise corrected) | M-314 | OBS-11 |
| M-307 | OBS-3 | M-315 | OBS-12 (settled by `DR-117` item 2) |
| M-308 | OBS-5 (and the draft's R-2) | M-316 | OBS-13 |
| M-309 | OBS-6 | M-317 | OBS-15 |
| M-310 | OBS-7 | M-318 | OBS-16 (logged, not made a rule) |
| M-311 | OBS-8 (and the draft's R-3) | M-319 | this methodology change |
| M-312 | OBS-9 | — | OBS-4 and OBS-14: struck, not logged |

### How to apply, once approved

1. Make sure no city's T8 round is open (the freeze rule, draft Conflict 17).
2. Run `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/883d8609-cb3a-4820-b3cb-6bfce797ee04/scratchpad/apply_rules.sh`. It checks all eight originals and all nine previewed files against their recorded sha256 values, refuses (copying nothing) if any differs or if the new file already exists, and otherwise copies the files in and prints each one. It does not run git.
3. Then `git diff --stat`, the follow-ups in section 8, one commit, and `graphify update .` (batched).

**The unified diffs** are in `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/883d8609-cb3a-4820-b3cb-6bfce797ee04/scratchpad/rules_preview_diffs/` (one per file, plus `ALL_rules_preview.diff`). ⚠ The scratch folder is under `/tmp` and does not survive a reboot. If it is gone, the copies have to be rebuilt; `build_edits.py` in `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/883d8609-cb3a-4820-b3cb-6bfce797ee04/scratchpad/rules_preview_work/` holds every edit as data, and section 2 below holds every inserted text exactly.

**Provenance date.** Every tag reads "Added 2026-11-04". The draft defines `[date]` as the date of application. If this is applied on a later day, the tags would need that date, and the copies and the script's hashes would then have to be rebuilt.

## 2 · Before and after, file by file

Line numbers are the **original's** (before any edit). "Copy L" is where the block sits in the edited copy. The edits were applied bottom-up within each file, so that the original line numbers stayed valid; they are listed here top-down. Every anchor line was asserted by its text before it was touched, and none had drifted from the draft's line numbers. **Context** is the original's target line and the line before it. **Inserted text** is exact.

### 2.1 `T8_Standing_Brief_Lines.md` — 5 edits (lines 40 → 61)

#### `M-301` — inserted after original L5 (copy L6–L7)

Context before (original):

````text
L4: 
L5: Where a line is addressed to the readers it is written in the second person; where it is addressed to the orchestrator it says so.
````

Inserted text, exactly:

````markdown

**Before adding or changing a format line in this file, run `Tools/triple_read_verify.py` on a worked example written to the new line.** Two instruments written on different days can disagree about where a field ends. *(Added 2026-11-04, `M-301`.)*
````

#### `M-254, OBS-15 (lines 10, 11)` — inserted after original L16 (copy L19–L23)

Context before (original):

````text
L15: 5. **Positional PROOF lines that carry a forbidden name.** *If an L1, LMID or LLAST line carries a name this brief forbids (a sign, a symbol, another location, a demonym), copy it exactly as written, because the field is positional, and add on the line below the PROOF block: `EXEMPT: positional line carries a name the brief forbids; not reproduced elsewhere.` Never reproduce the name anywhere else in your output.*
L16: 6. **Excerpted output is labeled.** *When you paste output that is not the whole output, head the block `raw output, excerpted (N lines omitted, reason)`. A block with no such heading is read as complete.*
````

Inserted text, exactly:

````markdown

*Lines 10 and 11, added 2026-11-04, are numbered on from line 9 so that lines 1–9 keep their numbers; both were run through `Tools/triple_read_verify.py` on a worked example first, as the note at the top requires.*

10. **If you stage your output in a plan file, write nothing after the staged block.** *Notes go above it.* *(Added 2026-11-04, `M-254`.)*
11. **In your reading log, write the first few words of each positional line (first, middle, last) beside its number as you reach it, and compare every PROOF field read-only against the source before handing back.** *A list item that wraps onto a second line is where the middle line slips. Never begin a reading-log line with a PROOF field name and a colon (`LRANGE:`, `LINES:`, `L1:`, `LMID:`, `LLAST:`, `QUOTE:`): after a PROOF heading the verifier reads such a line as that field.* *(Added 2026-11-04, `M-317`/OBS-15.)*
````

#### `M-257, M-264, M-266, M-270, M-274, M-282, M-300, OBS-6, OBS-7 (lines 12-20)` — inserted after original L22 (copy L30–L41)

Context before (original):

````text
L21: 8. **Run the DOUBLE-CHECK after the record is final.** *The record grows after a check, so a check run on a draft reports line counts that are already stale (87 lines recorded against 259 on disk at Step 5; 64 against 200 at Step 6). Run the DOUBLE-CHECK scripts last, or state in the block "the record grows after this check."*
L22: 9. **Copy staged reader outputs into the pass folder at the merge, and save every Round 3 reply to a file.** *`DR-27` says reader files archive with the pass. A reader's staged output (plan-file or scratchpad path) is copied into the pass folder at the merge, and each Round 3 reply is written to `.t8_<step>_round3_reader<X>.md` the moment it arrives. A reply that exists only as a chat result is a missing record.*
````

Inserted text, exactly:

````markdown

*Lines 12 to 20, added 2026-11-04, are numbered on so that lines 1–11 keep their numbers.*

12. **An interrupted or refused reader slot (a safeguard flag, a cut-off, a denied write) is re-dispatched on the identical brief and resumes from its own reading log.** *The brief is amended only after a repeat refusal, and only with the developer's OK. Log every attempt with its request id. After a plan-mode event, check that the re-dispatched reader's output file has actually grown before treating it as running. Every brief keeps its §0: create the output file first, log each entry as read, resume from the log.* *(Added 2026-11-04, `M-253`, `M-257`, `M-261`, `M-297`.)*
13. **Before the quotation audit, run a normalized check of every quoted string against the pass's own files and the sources.** *By default the audit excludes the pass's own folder, and even with `--own-pass` it never checks a file against itself or reads a dot-file, so it can miss a misquote of the pass's own text. Rewrite any string not found as unquoted text before the audit runs.* *(Added 2026-11-04, `M-264`, `M-289`.)*
14. **When a merge is written in parts, never type a step-local number by hand.** *Write a named key, and let one script number each series in order of definition, refusing a duplicate or unresolved key. The plan file records the keys each part must define.* *(Added 2026-11-04, `M-266`.)*
15. **Copy the closed set of dispositions from the brief verbatim into every header and column.** *Keep Round 3's verdict words (CONSISTENT / INCONSISTENT) out of disposition columns.* *(Added 2026-11-04, `M-270`.)*
16. **When a step's output rests on the previous step's verdict, its reading list includes that verdict section.** *If it does not, the merge says which flag it closed and on what line.* *(Added 2026-11-04, `M-274`.)*
17. **Never label a within-file item with a prefix the methodology uses for a series (R-, Q-, PA-, RF-, M-, DR-, DEC-).** *Give within-file items their own prefix (for example RC- for refereed conflicts).* *(Added 2026-11-04, `M-282`.)*
18. **A quotation in a brief (an example, a trap, a reminder) is a claim like any verified result and carries a pointer to an admitted line.** *A quotation with no admitted source is removed, or rewritten unquoted, before dispatch.* *(Added 2026-11-04, `M-300`.)*
19. **Generate the brief's results section, and its count, from the list of results** *(the rulings' headings, the verified-results list); never type a count by hand.* *(Added 2026-11-04, `M-309`/OBS-6.)*
20. **Give each piece, and each reader within it, its own disjoint number ranges in the brief before Round 1** *(for example reader A from 1, reader B from 101, reader C from 201); the merge renumbers.* *(Added 2026-11-04, `M-310`/OBS-7, `M-266`.)*
````

#### `OBS-8` — changed in place, original L30 (copy L49)

Context before (original):

````text
L29: |---|---|---|
L30: | Quotation audit | `python3 Tools/quotation_audit.py <pass folder> --step N` (or `--phase N`, `--files GLOB`, `--all`), optionally `--own-pass` | Audits only the step's own files; one selector is required. `--own-pass` lets a quotation of an earlier step of the same pass be found, while a file quoting itself still is not. On Mirny's Phase 7 this lowered the misses from 82 to 10, so the real ones show. |
````

This text in L30:

````markdown
so the real ones show. |
````

became, exactly:

````markdown
so the real ones show. **Run the quotation audit before the step's round record exists:** once the record re-prints the audit's fragments, `--own-pass` lets them validate against themselves. **The audit does not read dot-files,** so quotations of reader outputs and Round 3 replies kept as dot-files are checked by no tool, and each record says so. *(Added 2026-11-04, `M-311`/OBS-8.)* |
````

#### `OBS-2` — inserted after original L38 (copy L58–L59)

Context before (original):

````text
L37: 
L38: **The Step 8 brief template must now ask for the late T5 line** (`T5 - LATE LOVER FACULTY:`), and Phase 6 keeps its `T5 - EARLY LOVER FACULTY:` line.
````

Inserted text, exactly:

````markdown

**A validity line that rests on a tool's built-in self-test says the detector works, not that the pass was checked.** When the tool reports zero rows to audit, the record says "nothing to audit", never "valid". **Above each pasted tool run, give the tool's version or last-change date** (`git log -1 --format=%cs -- <tool>`; write "uncommitted edits" as well if `git status` lists the tool), so the run can be matched to the repairs recorded in the tool's own docstring. *(Added 2026-11-04, `M-306`/OBS-2.)*
````

### 2.2 `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` — 11 edits (lines 1100 → 1110)

#### `OBS-8` — inserted after original L326 (copy L327–L328)

Context before (original):

````text
L325: 
L326: ⭐ **Report `confirmed defects, CELL vs PROSE`.** ***That one ratio is T6/T7's entire experiment.***
````

Inserted text, exactly:

````markdown

⭐ **Run the quotation audit before the step's round record exists:** once the record re-prints the audit's fragments, `--own-pass` lets them validate against themselves. **The audit does not read dot-files,** so quotations of reader outputs and Round 3 replies kept as dot-files are checked by no tool, and each record says so. *(Added 2026-11-04, `M-311`/OBS-8.)*
````

#### `MP-3` — original L448–L449 replaced (copy L450–L450)

Context before (original):

````text
L447: 
L448: **Step 8's real Review Panel already carries a Lover-faculty line by `00f`'s own template — no new marker needed
````

Replaced lines (original):

````markdown
**Step 8's real Review Panel already carries a Lover-faculty line by `00f`'s own template — no new marker needed
there.**
````

with, exactly:

````markdown
**The late marker is a dedicated line in `08_Review_Panel.md`: `T5 - LATE LOVER FACULTY: <verdict>`.** A line that only mentions the Lover faculty is not the marker. The Step 8 record writes the by-hand comparison of the two verdicts (did the early verdict change what any phase between 6 and 8 wrote?), or says it was not done and why. A T5 check deferred to a later step is discharged there and never closed as "not applicable". *(Added 2026-11-04, `M-286`; Mirny Step 8.)*
````

#### `MP-3 (instrument line)` — changed in place, original L451 (copy L452)

Context before (original):

````text
L450: 
L451: ✅ **Instrument:** the same tool. **Extracts the Phase 6 marker and the `08_Review_Panel.md` Lover-faculty line,
````

This text in L451:

````markdown
the `08_Review_Panel.md` Lover-faculty line,
````

became, exactly:

````markdown
the `08_Review_Panel.md` late marker,
````

#### `M-260` — inserted after original L618 (copy L620–L621)

Context before (original):

````text
L617: not proceed on a guess.* **Re-dispatch the failed agent's slot only — do not re-run all three, and do not
L618: silently accept a partial pass.**
````

Inserted text, exactly:

````markdown

⭐ **A single failed PROOF field may be repaired by the reader that wrote it** *(developer ruling 2026-11-04, `DR-117` item 2, settling `M-260`)*. The reader re-checks that field against the source by hand, corrects only that field in its own output, and logs the repair (the field, the value it had, the value it has now, the line it re-read). Where several fields failed, each is repaired the same way, one field at a time. The orchestrator supplies no value and changes nothing else; Round 2 is re-run on the repaired output, and both runs are kept in the round record. **Any other Round 2 failure (a missing PROOF block, or anything that touches the reading itself) follows the rule above: re-dispatch the failed slot.** No piece goes to Round 3 with a failed field unrepaired. *(Added 2026-11-04, `M-260`, `DR-117`; Mirny Phase 10 and the repass.)*
````

#### `M-259` — inserted after original L678 (copy L682–L682)

Context before (original):

````text
L677: > 2. **NO CONTRADICTION → UNION.** A fact only one reader found is written, and credited to its finder in a
L678: >    "found by / confirmed by" table.
````

Inserted text, exactly:

````markdown
>    **A ruling or fact inside every reader's admitted range that only one reader used is a single-reader find, and is written under UNION like a fact only one reader saw.** *(Added 2026-11-04, `M-259`; Mirny Phase 9.)*
````

#### `M-250, M-256` — inserted after original L684 (copy L689–L692)

Context before (original):

````text
L683: > other reader is right · (b) mine is right · (c) a developer question* — so every reader's current view is on
L684: > record for the merge.
````

Inserted text, exactly:

````markdown
>
> **Round 3's prompt also carries a sixth section**, after the fifth: **6 — Recompute any figure a reader derived from a rate or coefficient table, and state its basis (raw coefficient, or adjusted by the location's own factor).** A figure whose basis is not stated is a Round 3 finding. *(Added 2026-11-04, `M-250`; Mirny Phase 7.)*
>
> ⛔ **A vote count is not the merge rule.** A contradiction is decided on content: the reading that claims least and fits the union's findings. **A reader's withdrawal of its own claim is evidence for the narrower reading, never a tie-break.** *(Added 2026-11-04, `M-256`, `M-263`; Mirny Phases 8 and 10.)*
````

#### `M-247 (box sentence)` — inserted after original L795 (copy L804–L805)

Context before (original):

````text
L794: > `§N`. Base for all relative paths in this section:*
L795: > `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/`
````

Inserted text, exactly:

````markdown
>
> ⛔ **A template row is a starting point, never the list.** Before dispatch, every per-step list is re-resolved against that step's own runbook text: its REQUIRED READING box, and every file the step says to run or open. *(Added 2026-11-04, `M-247`, `M-248`; Mirny Steps −1 and 0.)*
````

#### `M-247 (line)` — changed in place, original L801 (copy L811)

Context before (original):

````text
L800: 
L801: > 🧪 `T8` — **Step −1:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step −1", the location's own Specs file})` *(`City_Vision_Notes/` is struck corpus-wide, `00.1a`; never dispatched)* → `triple_read_verify.py` → cross-check → write `00.1_Step_MINUS-1_Input_Contract.md` only on UNANIMOUS.
````

This text in L801:

````markdown
T8_PROMPT{files: 00_RUNBOOK.md §"Step −1", the location's own Specs file})`
````

became, exactly:

````markdown
T8_PROMPT{files: 00_RUNBOOK.md §"Step −1" + 05_The_Input_Contract.md in full (its §7 pre-flight is what the step runs first) + the location's own Specs file + DEVELOPER_RULINGS_LOG.md where the contract's classification needs a ruling})`
````

#### `M-247 (line, tag)` — changed in place, original L801 (copy L811)

Context before (original):

````text
L800: 
L801: > 🧪 `T8` — **Step −1:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step −1", the location's own Specs file})` *(`City_Vision_Notes/` is struck corpus-wide, `00.1a`; never dispatched)* → `triple_read_verify.py` → cross-check → write `00.1_Step_MINUS-1_Input_Contract.md` only on UNANIMOUS.
````

This text in L801:

````markdown
write `00.1_Step_MINUS-1_Input_Contract.md` only on UNANIMOUS.
````

became, exactly:

````markdown
write `00.1_Step_MINUS-1_Input_Contract.md` only on UNANIMOUS. *(Changed 2026-11-04, `M-247`; Mirny Step −1.)*
````

#### `M-248` — changed in place, original L807 (copy L817)

Context before (original):

````text
L806: 
L807: > 🧪 `T8` — **Step 0:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step 0" + §6b Phase-0 row-set below + C.1's two Step-0 boxes})` → `triple_read_verify.py` → cross-check → write `00_Frame.md` only on UNANIMOUS.
````

This text in L807:

````markdown
T8_PROMPT{files: 00_RUNBOOK.md §"Step 0" + §6b Phase-0 row-set below + C.1's two Step-0 boxes})` → `triple_read_verify.py` → cross-check → write `00_Frame.md` only on UNANIMOUS.
````

became, exactly:

````markdown
T8_PROMPT{files: FIRST the 06_Worked_Example_Provenance.md subject check (before Step 0.2) · 00_RUNBOOK.md §"Step 0" · 01_Frame_Typology_and_Inheritance.md whole · Run_Modes_Warm_and_Cold.md whole · Robot_Physiology_and_Cultural_Practices.md whole (§C.10) · §6b's Phase-0 row-set · C.1's two Step-0 boxes})` → `triple_read_verify.py` → cross-check → write `00_Frame.md` only on UNANIMOUS. *The disciplines (`00b`, `00d`, `00f`) are read by the orchestrator at 0.2.* *(Added 2026-11-04, `M-248`; Mirny Step 0.)*
````

#### `M-252` — changed in place, original L965 (copy L975)

Context before (original):

````text
L964: | **7** | Division_of_Industry_Sweep §4.4 | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry_Sweep_2026-08-31.md` | `MAPPED` |
L965: | **7** | `01_Burden_Scoring_Model` / `08_Volume_Based…` | *(same Division_of_Industry/ directory)* | `MAPPED` |
````

This text in L965:

````markdown
| *(same Division_of_Industry/ directory)* | `MAPPED` |
````

became, exactly:

````markdown
| *(same Division_of_Industry/ directory)* | `MAPPED` · **`01_Burden_Scoring_Model.md` — SUPERSEDED by its own folder README (L49): opened for the record of why the method changed; cite no figure from it.** *(Added 2026-11-04, `M-252`.)* |
````

### 2.3 `03_The_Phase_Spine.md` — 2 edits (lines 1200 → 1201)

#### `M-252` — original L855 replaced (copy L855–L855)

Context before (original):

````text
L854: >   `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry_Sweep_2026-08-31.md`
L855: > - Inputs — `01_Burden_Scoring_Model.md`
````

Replaced lines (original):

````markdown
> - Inputs — `01_Burden_Scoring_Model.md`
````

with, exactly:

````markdown
> - **`01_Burden_Scoring_Model.md` — SUPERSEDED by its own folder README (L49): opened for the record of why the method changed; cite no figure from it.** *(Added 2026-11-04, `M-252`.)*
````

#### `M-268` — inserted after original L1171 (copy L1172–L1172)

Context before (original):

````text
L1170:   reconciliation pass surfaces a genuine contradiction between this determination and an earlier phase, it is
L1171:   revised there like any other finding.
````

Inserted text, exactly:

````markdown
  **When confirming, list the incumbent (the value the files already carry, and any value an earlier draft carries) beside the determination's own reserved alternatives.** If the incumbent is not among them, the honest value is open, not confirmed. The Step 5 backstop applies the same test. *(Added 2026-11-04, `M-268`.)*
````

### 2.4 `04_QA_Gates_and_Differentiation.md` — 2 edits (lines 928 → 931)

#### `M-287 (04 half)` — inserted after original L106 (copy L107–L108)

Context before (original):

````text
L105: check the target, never the claim.** And when a phase is added to this methodology, **every location already
L106: marked complete reverts to incomplete for that phase.**
````

Inserted text, exactly:

````markdown

**Gate 0 outward also reads a tracker's scope words (*unattended*, *in the developer's absence*, *complete*) and its forward references (*Step N to confirm*) against the files, not only its completion marks.** *(Added 2026-11-04, `M-287`.)*
````

#### `OBS-9` — inserted after original L330 (copy L333–L333)

Context before (original):

````text
L329:   > the real figure was ~60 days, and swapping the number in would have left a weak claim. **The actual
L330:   > constraint — nothing grows on that continent in any season — was both true and stronger.**
````

Inserted text, exactly:

````markdown
- **When a ruling changes a fact, check its "applied" list against every file that states the fact, at once.** A ruling applied to some sources and not others is recorded as a Gate C failure, with the files that lag. *(Added 2026-11-04, `M-312`/OBS-9.)*
````

### 2.5 `Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md` — 3 edits (lines 95 → 98)

#### `M-275 (III.2 step 3)` — original L60–L61 replaced (copy L60–L61)

Context before (original):

````text
L59:    look identical.
L60: 3. **Name the axis the category answers on**, in bold, and confirm no completed sibling already uses it —
````

Replaced lines (original):

````markdown
3. **Name the axis the category answers on**, in bold, and confirm no completed sibling already uses it —
   *"different content is not differentiation; a different question is."*
````

with, exactly:

````markdown
3. **Name the axis the category answers on**, in bold. ⏸️ *Confirming that no completed sibling already uses it
   is TERMINAL-ONLY, like steps 1–2.* *"Different content is not differentiation; a different question is."* *(Re-extracted from `04` III.2 step 3, 2026-11-04, `M-275`.)*
````

#### `M-275 (III.3 box)` — inserted after original L65 (copy L66–L68)

Context before (original):

````text
L64: ## III.3 — Sibling sets of different sizes
L65: 
````

Inserted text, exactly:

````markdown
> ⏸️ **TERMINAL-ONLY for a ULM / CST / RWBEM pass** (the 2026-09-06 ruling above). In-run, every location takes
> the III.4 path. *(Re-extracted from `04` III.3, 2026-11-04, `M-275`.)*

````

#### `M-275 (III.3 Large row)` — original L68 replaced (copy L71–L71)

Context before (original):

````text
L67: |---|---|
L68: | Large (20+) | Full table; check the most recently written first — collisions cluster there |
````

Replaced lines (original):

````markdown
| Large (20+) | Full table; check the most recently written first — collisions cluster there |
````

with, exactly:

````markdown
| Large (20+) | Full table, with all columns present. |
````

### 2.6 `Mechanical_Extraction_Field_Guide.md` — 1 edit (lines 505 → 507)

#### `M-251` — inserted after original L203 (copy L204–L205)

Context before (original):

````text
L202: instruction, not a conclusion.
L203: 
````

Inserted text, exactly:

````markdown
⛔ **A row that quotes another file's quotation of an excluded input (a developer-vision note, a vignette) is refused like the input itself, whatever heading it sits under.** Before a datasheet is used as a step's input, its line anchors are re-located with `Tools/remap_line_citations.py`. *(Added 2026-11-04, `M-251`; Mirny Phases 6–7.)*

````

### 2.7 `00_RUNBOOK.md` — 19 edits (lines 3179 → 3204)

#### `M-252` — changed in place, original L1979 (copy L1979)

Context before (original):

````text
L1978: | **6** | **P** ⚠ **`Factions/Robot_Religions/` — check before inventing a belief.** ⭐⭐ **THE ROSTER IS OPEN AND IS EXPECTED TO GROW** *(developer ruling, 2026-09-06: **"I am open to the possibility — in fact, the likelihood — that there will be more robot religions, so don't force any community/society into a religion where it doesn't already naturally fit"**)*. ⛔ **So a roster `grep` returning ZERO for a location is a RESULT, not a gap to fill** — *write "no faith sited here," leave the slot explicitly open, and never let it read as "no faith possible." `03` §Phase 6 B carries the universal form* · `National_Holidays.md` ⚠ *(its own scope note warns that most cities' `Local_Cultures/` files already hold scattered festival material — **which is `Step 0.4` item-6 READ-LAST**, so any observance a pass proposes is a CANDIDATE pending Step 5 reconciliation)* · ⭐ **`Reference/Real-World/Ice-Cold_Buddhism_Research/` (§C.9, 7 files — metaphysics, machine ethics, Zen aesthetics, vocabulary)** ⚠ *the faith's name is a placeholder* · **`The_True_Believer_` / `The_Meme_Machine_Extraction.md` (§C.9)** · **the deferred mortuary question — do not answer it** |
L1979: | **7** | ⭐⭐ **`Division_of_Industry/` — THE PRIMARY SOURCE FOR 7a, and the strongest `G3` supply in the project (§C.6).** Read its README/status header for carve-outs FIRST; figures from `16` Half B; gaps from `Division_of_Industry_Sweep_2026-08-31.md` §4.4; inputs `01_Burden_Scoring_Model.md`, `08_Volume_Based_Requirement_Reference.md`, `National_Medical_and_Care_Institutes.md`, `Theoretical-Calculations/` · ⭐ **`Reference/Real-World/Industry_Staffing_and_Productivity/` and `jobs_professions_and_fields/` (SOC) — both §C.9; SOC tier-marking is ADDITIVE, never a replacement** · **P** `National_Economy_and_Currency.md`, `City_Logistics.md`, `Factions/`, criminal-justice canon · **U** `Megacorps/` |
````

This text in L1979:

````markdown
inputs `01_Burden_Scoring_Model.md`, `08_Volume_Based_Requirement_Reference.md`,
````

became, exactly:

````markdown
inputs `01_Burden_Scoring_Model.md` (**SUPERSEDED by its own folder README (L49): opened for the record of why the method changed; cite no figure from it** — *added 2026-11-04, `M-252`*), `08_Volume_Based_Requirement_Reference.md`,
````

#### `M-291` — inserted after original L2694 (copy L2695–L2695)

Context before (original):

````text
L2693: - **Phase 5 is mandatory and is written mid-spine specifically so it cannot be dropped.**
L2694: - **Push every finding to a physical or behavioral expression.** The violation is usually the gameplay.
````

Inserted text, exactly:

````markdown
- **When a phase parks a figure ("as the row states it"), it lists the figure's downstream uses at that time,** so a later correction reaches a list, not a search. *(Added 2026-11-04, `M-291`; Mirny Phases 4 and 7.)*
````

#### `Consequential: line count in the SBL row (not a draft row)` — changed in place, original L2709 (copy L2710)

Context before (original):

````text
L2708: > | ⭐⭐ **`T8` — three-subagent read consensus** | **`Tools/triple_read_verify.py`.** *Three independent readers per step/phase, each emitting a `PROOF:` block; mechanical ground-truth check; then agent-to-agent cross-check. **Write only on UNANIMOUS.*** **23 commands are written into the template — 12 steps, 11 phases** *(Step 4 routes to its phases rather than dispatching)* |
L2709: > | ⭐ **`T8_Standing_Brief_Lines.md`** *(2026-10-21)* | **The nine lines every three-reader brief and its record must carry** (PROOF fields by hand, admitted spans, the one graphify ground, source pointers, forbidden names in positional lines, excerpted-output labels, generated entry ranges, DOUBLE-CHECK last, saved Round 3 replies), plus the post-write check commands as the tools now work |
````

This text in L2709:

````markdown
**The nine lines every three-reader brief and its record must carry** (PROOF fields by hand,
````

became, exactly:

````markdown
**The standing lines every three-reader brief and its record must carry** (lines 1–9 since 2026-10-21: PROOF fields by hand,
````

#### `Consequential: line count in the SBL row (not a draft row)` — changed in place, original L2709 (copy L2710)

Context before (original):

````text
L2708: > | ⭐⭐ **`T8` — three-subagent read consensus** | **`Tools/triple_read_verify.py`.** *Three independent readers per step/phase, each emitting a `PROOF:` block; mechanical ground-truth check; then agent-to-agent cross-check. **Write only on UNANIMOUS.*** **23 commands are written into the template — 12 steps, 11 phases** *(Step 4 routes to its phases rather than dispatching)* |
L2709: > | ⭐ **`T8_Standing_Brief_Lines.md`** *(2026-10-21)* | **The nine lines every three-reader brief and its record must carry** (PROOF fields by hand, admitted spans, the one graphify ground, source pointers, forbidden names in positional lines, excerpted-output labels, generated entry ranges, DOUBLE-CHECK last, saved Round 3 replies), plus the post-write check commands as the tools now work |
````

This text in L2709:

````markdown
DOUBLE-CHECK last, saved Round 3 replies), plus
````

became, exactly:

````markdown
DOUBLE-CHECK last, saved Round 3 replies; lines 10–20 added 2026-11-04), plus
````

#### `OBS-2 (clause)` — changed in place, original L2711 (copy L2712)

Context before (original):

````text
L2710: | **Part V** — `Tools/quotation_audit.py` | Record `confirmed defects, CELL vs PROSE` at every phase close. ⭐ *(2026-10-21: `--step N` / `--phase N` / `--files` / `--all` required; `--own-pass` optional.)* |
L2711: > | **Part V.2** — `Tools/handoff_audit.py` | Record `phases with rows addressed to them and NO enumeration` |
````

This text in L2711:

````markdown
Record `phases with rows addressed to them and NO enumeration` |
````

became, exactly:

````markdown
Record `phases with rows addressed to them and NO enumeration`. ⚠ *A YES that rests on the tool's built-in self-test says the detector works, not that the pass was checked; with zero rows to audit, record "nothing to audit", never "valid"* (`T8_Standing_Brief_Lines.md` §C; added 2026-11-04, `M-306`/OBS-2) |
````

#### `M-256, M-259 (clause)` — changed in place, original L2713 (copy L2714)

Context before (original):

````text
L2712: > | **`Tools/phase_discipline_check.py`** | `T3` ledger · `T4` shed marker · `T5` early Lover-faculty smoke test |
L2713: > | ⭐ **The `T8` WRITE is a MERGE, not a pick** *(developer, 2026-09-28, `M-246`)* | **Contradiction → the most conservative current view, split named in the row** *(population-origin material → DEMOTED, never EXCLUDED — §C.9c, "a pass that refuses all ethnic material")*. **No contradiction → UNION: every single-reader find is written and credited to its finder.** Full statement: `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 |
````

This text in L2713:

````markdown
**No contradiction → UNION: every single-reader find is written and credited to its finder.** Full statement:
````

became, exactly:

````markdown
**No contradiction → UNION: every single-reader find is written and credited to its finder.** *(2026-11-04, `M-256`, `M-259`:)* **A vote count is not the merge rule; a reader's withdrawal of its own claim is evidence for the narrower reading, never a tie-break; a ruling inside every reader's admitted range that only one reader used is a single-reader find.** Full statement:
````

#### `R-1 (DR-107)` — inserted after original L2724 (copy L2726–L2731)

Context before (original):

````text
L2723: > measurements already taken.*
L2724: 
````

Inserted text, exactly:

````markdown
> ### ⛔⛔ DEPENDENT WORK RUNS IN ORDER. ***Developer ruling, 2026-11-04 (`DR-107`); "confirmed" defined by `DR-117`.***
>
> > **Developer, verbatim:** *"If there's anything that needs the results from a previous thing in order to run, don't run the next thing until the previous thing is confirmed."*
>
> **A step, phase or piece that needs another's result does not start until that result is complete and confirmed. "Confirmed" means the previous unit's result is written to file; the next unit may then start** — *it does not wait for the developer's review, which comes at the end of the day (`DR-117`).* Work that does not depend on other work may run together; the three readers of one unit are not dependent work. Any change to a planned order is written into the queue or tracker, with its reason, at the time. *(Added 2026-11-04, `DR-107`, `DR-117`, `M-305`/OBS-1; Mirny repass.)*

````

#### `M-267` — inserted after original L2868 (copy L2876–L2877)

Context before (original):

````text
L2867: > ⭐⭐ **And the pass's own finding STAYS AT FULL STRENGTH in the pass's files.** ***Nothing derived is discarded
L2868: > to make room for an older answer.***
````

Inserted text, exactly:

````markdown
>
> ⛔ **A row whose only stated ground is material excluded at every step (a vignette, a vision note, a test run) is OUT OF FRAME, never culture-only and never both-are-true.** A reader who reconciles it anyway is a Round 3 finding. *(Added 2026-11-04, `M-267`; Mirny Step 5.)*
````

#### `M-271` — inserted after original L2877 (copy L2887–L2888)

Context before (original):

````text
L2876: > strong one arrives — **because you do not know which finding is strongest until the pass is nearly done.**
L2877: > Stated at declaration time it is advice; **stated here it is checkable.**
````

Inserted text, exactly:

````markdown
>
> **End the strongest-finding paragraph by naming the one leg that a later-read file (this location's own culture material, read last) could contradict, before that file is opened; then check it when it is.** A leg that rests on an absence is named as such. *(Added 2026-11-04, `M-271`; Mirny Step 5.)*
````

#### `M-273` — inserted after original L2918 (copy L2930–L2930)

Context before (original):

````text
L2917: > ⛔ **CELLS HOLD THE AXIS, NEVER THE CONTENT.** *"Different content is not differentiation; a different
L2918: > question is."*
````

Inserted text, exactly:

````markdown
> ✅ **Check each cell against the source's own count and slots, not against a reader's reading of them, and keep the narrowest cell.** *(Added 2026-11-04, `M-273`; Mirny Step 6.)*
````

#### `M-272` — inserted after original L2920 (copy L2933–L2934)

Context before (original):

````text
L2919: > ⚠ **The table is FILLED DURING synthesis, not before it.** ***It is not a prerequisite and its emptiness is
L2920: > not a gap*** — it contributes nothing to the first city and everything to the thirty-seventh.
````

Inserted text, exactly:

````markdown
>
> ⭐ **Write the row blind:** back the table up, find the insertion point by its first-column label, assert that label and the column count before inserting, and compare with the backup afterward (only the inserted lines may differ). Print headings and column counts only, never another row's first cell. *(Added 2026-11-04, `M-272`; Mirny Step 6.)*
````

#### `MP-7` — changed in place, original L2927 (copy L2941)

Context before (original):

````text
L2926: 
L2927: **Paste raw scan output. Verify the instrument before trusting any zero. Report what Gate 11 cleared as well as
````

This text in L2927:

````markdown
**Paste raw scan output. Verify
````

became, exactly:

````markdown
**Paste raw scan output, whole; or, where it is long, save the whole output to a file beside the record and head the pasted part *raw output, excerpted (N lines omitted, reason)*.** A block with no such heading is read as complete. Cutting another location's lines under the law of one location is a labeled excerpt, not a summary. *(Added 2026-11-04, `M-285`; Mirny Phases 5–10.)* **Verify
````

#### `M-279` — inserted after original L2928 (copy L2943–L2944)

Context before (original):

````text
L2927: **Paste raw scan output. Verify the instrument before trusting any zero. Report what Gate 11 cleared as well as
L2928: what it flagged.**
````

Inserted text, exactly:

````markdown

**The station-builder scan looks for denials as well as assertions.** A sentence saying the builder does *not* explain a form is the same violation as one saying it does (`DR-19`; `No_National_Stereotypes.md`; `Corpus_Reference_Sheets/No_National_Stereotypes_Quick_Reference.md` L76–78). Read every hit in context. *(Added 2026-11-04, `M-279`; Mirny Step 7.)*
````

#### `M-278` — inserted after original L2965 (copy L2982–L2983)

Context before (original):

````text
L2964: `Disciplines/00f_Review_Panel.md` *(the ULM copy)*, carried unchanged; only the casting changes. Six Flat Archetypes plus the mandatory
L2965: **Passer-Through** and **Neighbor**; the **Lover faculty's question every time.**
````

Inserted text, exactly:

````markdown

**Step 7's errata enter the Review Panel's brief as facts, each with its source line, and the panel runs on the corrected statements.** *(Added 2026-11-04, `M-278`; Mirny Steps 7–8.)*
````

#### `M-280` — inserted after original L2979 (copy L2998–L2999)

Context before (original):

````text
L2978: 
L2979: **If yes, it is `unmet`, and the refusal is written as characterization rather than as a gap to close.**
````

Inserted text, exactly:

````markdown

**The peer-free test decides *whether* to refuse. Whether a refusal is `unmet` or `declined` is decided by `00f`'s self-knowledge test (`Disciplines/00f_Review_Panel.md` L744–753).** An `unmet` must name an admitted or ruled line that shows the place knowingly holding the thing; the pass's own coinage cannot be that line. A refusal grounded only in national canon is `declined`. Report the `unmet` count with its grounds, never as a measure of the place. *(Added 2026-11-04, `M-280`, `M-313`/OBS-10; Mirny Step 8.)*
````

#### `M-287 (RB half)` — inserted after original L3007 (copy L3028–L3028)

Context before (original):

````text
L3006:    > **The finding itself goes to `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` and nowhere else.**
L3007:    > **If you have written more than ~3 lines into a tracker, you are writing in the wrong file.**
````

Inserted text, exactly:

````markdown
   > **Before the record is committed, check the tracker's lines for this location: one line plus a pointer each, no finding in them.** *(Added 2026-11-04, `M-287`.)*
````

#### `OBS-11` — inserted after original L3015 (copy L3037–L3037)

Context before (original):

````text
L3014:    against the file as it now stands, because edits shift lines.** Record what moved. This step discharges any
L3015:    phase's "sweep at the close" deferral; a deferral that no step names is a hole.
````

Inserted text, exactly:

````markdown
   **A deferral that names any step, not only the close, reaches that step's brief as a line to discharge.** That step may close it as "not applicable" only by stating why the deferred check no longer applies. *(Added 2026-11-04, `M-314`/OBS-11; Mirny Phase 6 to Step 8.)*
````

#### `OBS-3` — inserted after original L3034 (copy L3057–L3057)

Context before (original):

````text
L3033: - **Killed findings** — an attractive result destroyed by its own evidence. ***The most valuable entries in the
L3034:   file.*** Run 1's best moment was a finding killed by its own arithmetic; Run 3's was the same.
````

Inserted text, exactly:

````markdown
  - **Class each killed finding as *killed by evidence* or *killed for want of an admitted line*; only the second may be revived by a later ruling or source.** A kill stays in the record. When a ruling later settles it, add a status pointer beside the record, never a rewrite. *(Added 2026-11-04, `M-307`/OBS-3; Mirny repass.)*
````

#### `Amendment-layer pointer (M-302, M-303, OBS-5, OBS-13)` — inserted after original L3150 (copy L3174–L3175)

Context before (original):

````text
L3149: > produced a confident, coherent, contaminated result — precisely the failure the protocol exists to prevent.**
L3150: 
````

Inserted text, exactly:

````markdown
📎 **The amendment-layer rules (amending a pass after it is written: append-only amendment pieces, notices and pointer lines, scoping registers, dockets) live in a separate file beside this runbook: `Amendment_Layer_Rules.md`.** *(Developer ruling 2026-11-04, `DR-117` item 3.)*

````

### 2.8 `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` — 1 edit (lines 8586 → 8602)

#### `OBS entries M-305 to M-318, and M-319 (this change)` — inserted after original L8582 (copy L8583–L8598)

Context before (original):

````text
L8581: - **M-303 · An in-place amendment of a heading's body can leave the same physical line stating the premise, and a second pass found it** (Mirny amendment Piece 2, Phase 7, 2026-10-29). The 2026-10-13 in-place corrections of P7-26 and P7-27 fixed the clauses the developer named, yet all three readers found that L391 (P7-26's third order) and L396 (P7-27) still said the outcome is the examiner, that no qualification exists, that the unlearned are "visible only when hurt", and treated a taught reading as a mere candidate; one reader also found the 7c scope line (L380) and the heading (L382). Phase 7 also still carried "the one handoff that always drops", the phrase Phase 6 had withdrawn (L354). **Lesson:** an in-place amendment must be followed by a read of the whole finding, not only of the sentence amended; amendment notices need a second reader. *(Mirny; 9.5 kind: a correction that did not hold.)*
L8582: - **M-304 · The two Piece 1 fixes and a trimmed list took a three-reader round from about 35 minutes plus a repair to one clean pass** (Mirny amendment Piece 2, 2026-10-29). Piece 1 (38 entries, about 7,830 lines per reader) needed a same-reader repair after Round 2; Piece 2 (16 entries, about 3,490 lines) passed Round 2 unanimously on the first run, all readers finishing within about 35 minutes. Causes recorded: the brief carried no unverified quotation (M-300) and put a blank line before `EXEMPT:` (M-301); the trimmed list admitted earlier phases only at the cited findings (`DR-74`). The trimming cost nothing visible in quality: the three readers still found about 60 uncovered places in Phase 7 and a falsifier in Phase 5 (M1), outside the list, via a cited line. **Lesson:** the trimmed-list approach for amendment work is supported by one measured case; the November city runs are unaffected (`DR-74`). *(Mirny; 9.5 kind: a technique that worked, and why.)*
````

Inserted text, exactly:

````markdown

- **M-305 · A one-at-a-time repass ran its later units in parallel, on the orchestrator's judgement, and each dependent piece declared its predecessors "not inputs"** (Mirny repass, 2026-11-04; proposed as OBS-1 in `Amendment_Rederivation_ST9_RecordLog_2026-11-04.md` §5). The order was "Go one step, one phase at a time." and "One unit per firing."; after the developer said to continue through all the steps and to go until 3 pm, the orchestrator ran U5 to U9 (and later U10, U11) in parallel to finish inside the window; the developer did not specifically instruct it (the cause is on no file and comes from the orchestrator's account). No finding was contaminated (each held its dependents "pending" and read the others' section 0 for a cross-reference note only), but Steps 6 to 8 never took the re-derived Step 5 or Phase 10 as input, one piece appeared mid-merge of another, and the reconciliation is an open request no step carries. **Lesson:** dependent work runs in order (`DR-107`): a unit that needs another's result does not start until that result is written to file (`DR-117` item 1). The piece's softer alternative (schedule a fold-in and run beside the input) is not adopted, because `DR-107` forbids it. Write the reason for any change of order into the queue at the time. *(Mirny; 9.5 kind: a problem, and a departure from a stated order. Extends M-278. Rule: `00_RUNBOOK.md` Step 4, "DEPENDENT WORK RUNS IN ORDER", added 2026-11-04. Whether units U5 to U11 are redone or folded in is still undecided, `DR-107`.)*
- **M-306 · Three tools changed their verdicts between the pass and the repass, and the new YES of one is a self-test** (Mirny repass U0, 2026-11-04; OBS-2, same file). `handoff_audit.py` went from NO on ten checks to "INSTRUMENT VALID: YES" on its built-in controls, with 0 outbound rows for the pass; the founders script became scoped by `--city`; the T5 check found a dedicated marker absent. **Correction to the piece's premise:** the piece wrote that the verdicts changed "with no recorded repair". The repairs are recorded in each tool's docstring (`Tools/handoff_audit.py` L26–30, `Tools/phase_discipline_check.py` L41–46, `Tools/check_founders_against_register.py` L15–21), in `T8_Standing_Brief_Lines.md` §C, and in the rulings log (`DEVELOPER_RULINGS_LOG.md` L1169, the 2026-10-21 handoff decisions 8 and 13); none of those lines was on the piece's reading list. What was stale is the Log's "never repaired" line, not the repair's record. **Lesson:** a validity that rests on a tool's own built-in self-test says the detector works, not that the pass was checked; with zero rows to audit the record says "nothing to audit". Paste each tool's version or last-change date with its output, so a run can be matched to the repair its docstring records. *(Mirny; 9.5 kind: a tooling obstacle, and a reading-list blind spot. Extends M-284. Rule: `T8_Standing_Brief_Lines.md` §C and the handoff-audit row of `00_RUNBOOK.md` Step 4, added 2026-11-04.)*
- **M-307 · Five killed findings were later answered by ruling, one of them in part** (Mirny Step 9 addendum, 2026-11-04; OBS-3, same file). Each was killed correctly on the lines then admitted. **Lesson:** class each kill as *killed by evidence* or *killed for want of an admitted line*; only the second can be revived; keep kills as records and add a status pointer when a ruling settles one; never read the Log as having falsified them. *(Mirny; 9.5 kind: killed findings. Extends the runbook §9.5 class "killed findings". Rule: `00_RUNBOOK.md` §9.5, added 2026-11-04.)*
- **M-308 · A notice at the head of a file is an edit that moves every anchor below it** (Mirny, the 2026-10-13 notices; OBS-5, same file). The measured shifts match one notice per file (+2), more for Phase 7 (+5); the cause is consistent, not proved. The 2026-10-13 notice reached Phases 2 to 10 and Steps 5 to 8 only; the record and readiness steps were left out. **Lesson:** put notices and pointers at the end of a file, only where a ruling permits the edit at all (`DR-101`; `DR-116` item 2), and include the record and readiness steps in any notice sweep. *(Mirny; 9.5 kind: an edit's side effect. Rule: `Amendment_Layer_Rules.md` rule 3, added 2026-11-04.)*
- **M-309 · The brief's result count was wrong in seven repass briefs in one day** (Mirny repass U2 to U9, 2026-11-04; OBS-6, same file). Five said "eight results" over ten, two over nine; readers caught each. **Lesson:** generate the results section and its count from the list of results, as M-294 asked for the entry map. *(Mirny; 9.5 kind: a recurrence of M-283 and M-294. Rule: `T8_Standing_Brief_Lines.md` line 19, added 2026-11-04.)*
- **M-310 · Reader number collisions in every piece that let readers number** (amendment layer and repass of 2026-11-04, eight pieces and the Steps 9/9.5 piece, 2026-11-04; OBS-7, same file). Each merge needed a mapping table; the queue's rows for U10 and U11 were the first to give a piece its series, and the three readers of the Steps 9/9.5 piece still collided inside it. **Lesson:** give each reader its own disjoint ranges in the brief, not only each piece. *(Mirny; 9.5 kind: a recurrence. Extends M-266, M-282. Rule: `T8_Standing_Brief_Lines.md` line 20, added 2026-11-04.)*
- **M-311 · The quotation audit cannot see where the readers' outputs are kept, and it validates against its own pass's other files once a record exists** (Mirny repass, 2026-11-04; OBS-8, same file). Keeping reader outputs and Round 3 replies as dot-files (the fix for M-296) put them outside the audit's corpus: `--own-pass` reads `*.md` in the folder, which does not match a dot-file (`Tools/quotation_audit.py` L161–175), so quotations of them are checked only by the merge itself. The second half was measured on the Phase 10 amendment piece: 37 misses before its round record existed against 5 after (`Amendment_Rederivation_P10_Catalog_2026-11-04b_T8_Rounds.md` L389). **Lesson:** when a record practice changes, re-check which instruments read the new location; run the audit before the record file exists, and say in each record which quotations no tool checked. A dot-file mode for the audit stays a tool option, not applied. *(Mirny; 9.5 kind: a tooling obstacle. Extends M-264, M-289, M-296. Rule: `T8_Standing_Brief_Lines.md` §C and `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` T6, added 2026-11-04.)*
- **M-312 · A ruling applied to some sources and not others becomes every later piece's snag** (Mirny, `DR-99`, 2026-11-04; OBS-9, same file). The Register, the census tag line and the relationship entry follow `DR-99`; the spec does not; four pieces logged the same disagreement. **Lesson:** a ruling's "applied" list is checked against every file that states the fact, at once (a Gate C item). *(Mirny; 9.5 kind: a problem. Rule: `04` Gate C, added 2026-11-04. The Mirny case itself is already known, `DR-108` item 4.)*
- **M-313 · The pass's only `unmet` rested on the author's coinage** (Mirny Step 8, re-tested, 2026-11-04; OBS-10, same file). The panel's self-knowledge reading took the pass's retired premise for the place's; the panel cannot test plausibility, and none of its positions caught the error; the developer did. **Lesson:** an `unmet` must name an admitted or ruled line that shows the place knowingly holding the thing; a coinage cannot be that line; a count is reported with its grounds, never as a measure of a place. *(Mirny; 9.5 kind: self-audit error. Extends M-280. Rule: `00_RUNBOOK.md` Step 8, added 2026-11-04 with M-280. Mirny's single `unmet` becoming `declined` stays a proposal; `DR-114` keeps two refusals "declined, provisional".)*
- **M-314 · A deferral reached its named step and was closed there as "not applicable"** (Mirny Phase 6 piece to Step 8 piece, 2026-11-04; OBS-11, same file). T5 was left "not re-run" and "flagged for Step 8, AQ-4"; the Step 8 re-test closed with "T5: not applicable to Step 8". **Lesson:** a deferral that names a step must reach that step's brief as a line to discharge. *(Mirny; 9.5 kind: a problem. Extends M-291, M-286. Rule: `00_RUNBOOK.md` Step 9 item 5 and `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` T5, added 2026-11-04.)*
- **M-315 · The rule for a single-field Round 2 failure changed between pieces** (amendment layer and repass of 2026-11-04, 2026-11-04; OBS-12, same file). P06 and P08 repaired before Round 3; Step 5 proceeded with the failure logged; Step 10 repaired the one field and re-ran. **Lesson:** state in the brief what a single-field failure requires. **Settled by `DR-117` item 2 (2026-11-04):** a reader may repair a single failed PROOF field in its own output (re-check, correct that field only, log it). Under that rule the same-reader repairs of M-260 and of the P06, P08 and Step 10 pieces comply; the Step 5 piece, which went on with one field unrepaired, does not. *(Mirny; 9.5 kind: a contradiction between practices. Extends M-260. Rule: `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.1 Round 2, added 2026-11-04.)*
- **M-316 · A single-reader pointer register under-reached at every step it covered** (amendment layer, Phase 6 to Step 8, 2026-11-04; OBS-13, same file). **Lesson:** a draft register is where to look, never what to budget a piece by; replace each section when its piece is verified, in the same unit. *(Mirny; 9.5 kind: self-audit error. Extends the reconciliation note's "a floor, not a ceiling", and M-302. Rule: `Amendment_Layer_Rules.md` rule 2, added 2026-11-04.)*
- **M-317 · Positional PROOF slips recur, and one line caught every reader** (amendment layer and repass of 2026-11-04, 2026-11-04; OBS-15, same file). All three readers of the Steps 9/9.5 piece, and a Step 10 reader the same morning, first copied the Founding Register's middle line one off, where a list item wraps onto a second line. **Lesson:** in a reading log, write the first words of a positional line beside its number; keep the read-only comparison before handback in every brief. **Found while writing the rule (2026-11-04, under M-301):** a worked example run through `Tools/triple_read_verify.py` showed that a reading-log line beginning `LMID:` after a PROOF heading overwrites that field (`LMID MISMATCH`), so the new standing line also forbids beginning a log line with a field name and a colon. *(Mirny; 9.5 kind: a recurrence, and a tool interaction found in testing. Rule: `T8_Standing_Brief_Lines.md` line 11, added 2026-11-04.)*
- **M-318 · A repo pointer spliced mid-sentence in two datasheets** (Mirny Step 8 and Step 9 datasheets, L5, 2026-11-04; OBS-16, same file). A note meant to sit where "no cited line moves" landed inside a sentence near the top. **Lesson:** check every datasheet's first lines once after a pointer insertion; the note states an intention its own placement breaks. **Not made a rule:** a one-off placement defect of the 2026-10-29 pointer sweep; fix the affected sheets on the developer's word, and check `Tools/build_datasheets.py` (three pointer strings) for the same placement. *(Mirny; 9.5 kind: an edit's side effect; a docket item.)*
- **M-319 · The Mirny lessons were written into the rules** (2026-11-04; methodology change under `DR-116` item 4 and `DR-117`). Source: `Research_Logs/Lessons_Into_Rules_Draft_2026-11-04.md` (96 lessons: MP-1 to MP-19, M-247 to M-304, OBS-1 to OBS-16, and three repass lessons), from the Mirny ULM pass of 2026-10-12 and the Mirny repass of 2026-11-04. **Applied:** 43 rows of rule text, every row the draft marked NEEDS RULE TEXT except M-281 and OBS-4, which the developer struck; OBS-14 (marked not for the rules) was struck too and is not logged. Files changed: `T8_Standing_Brief_Lines.md` (lines 10 to 20 and three notes), `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md`, `03_The_Phase_Spine.md`, `04_QA_Gates_and_Differentiation.md`, `Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md`, `Mechanical_Extraction_Field_Guide.md`, `00_RUNBOOK.md`, and this log (M-305 to M-319); new file `Amendment_Layer_Rules.md`. **The developer's decisions that shaped the text:** "confirmed" in the dependency rule means written to file (`DR-117` item 1); a reader may repair a single failed PROOF field in its own output (`DR-117` item 2); the amendment-layer rules live in a separate file (`DR-117` item 3); rule-file edits may run at any hour (`DR-117` item 4); `unmet` against `declined` follows `00f`'s self-knowledge test. **What was learned in doing it:** (1) a lesson's premise is checked before its rule is written: OBS-2 said three tools changed "with no recorded repair", and the repairs are in each tool's docstring (M-306); (2) the new M-301 rule caught a defect in a new standing line before it shipped (M-317); (3) the draft's own repass labels R-1 to R-3 reused the R- prefix that M-282 now forbids for within-file items, so the rules cite `DR-107`, M-308 and M-311 instead (R-1 is `DR-107`; R-2 is OBS-5, now M-308; R-3 is OBS-8, now M-311); (4) every runbook insertion moves lines that Pre-Trips, datasheets, the `Stepwise_Execution/` extracts, the quick references and `T8_Standard_Entries.json` cite; re-locating them is a listed follow-up, not part of this change. **Stale status line, recorded here and not edited:** the status line below this block says MP-1 to MP-19 were "none applied"; groups A to C were ruled and applied on 2026-10-21 (`DEVELOPER_RULINGS_LOG.md` L1169). *(Mirny; 9.5 kind: a methodology change, recorded per Step 9 item 4.)*
````

## 3 · The new file, in full: `Universal_Location_Methodology/Amendment_Layer_Rules.md`

Created only as a copy in the scratch folder. The runbook's one-line pointer to it is in 2.7 (the row headed "Amendment-layer pointer").

````markdown
# Amendment-layer rules — amending a pass after it is written

> **Created 2026-11-04 at the developer's direction:** the amendment-layer rules live in a separate file beside
> the runbook, not in a new runbook section (`DR-117` item 3, `DEVELOPER_RULINGS_LOG.md`). **`00_RUNBOOK.md`
> carries a one-line pointer to this file just before its "# Where everything lives" table.** The rules below
> come from the lessons of the amendment layer and repass of 2026-11-04 (`Research_Logs/Lessons_Into_Rules_Draft_2026-11-04.md`,
> approved row by row on 2026-11-04; the change itself is recorded as `M-319` in
> `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`).

## What this file governs

**The amendment layer: everything written about a pass after the pass itself is written.** That is:

- **Amendment pieces** — a re-derivation of one phase or step, written as a new file appended beside the pass,
  never a rewrite of it.
- **Amendment notes and notices** — what is true now, where a pass's text no longer matches its sources.
- **Pointer lines** — a line in an existing file that sends its reader to an amendment.
- **Registers** — the lists that scope which findings an amendment has to re-derive.
- **Dockets** — proposed corrections, held for the developer's word.

## The standing rulings this file sits inside

**These are rulings, not new rules; they are stated here so that no amendment work has to reconstruct them.**

| Ruling | What it says | Where |
|---|---|---|
| `DR-101` | **A finished pass's files are never edited.** Changes in its sources are recorded in its amendment note. | `DEVELOPER_RULINGS_LOG.md` L1673–1679 |
| `DR-102` | **Nothing already recorded is reworded to carry its own history.** An amendment note states the current fact with its source address, not what the text used to say; the history stays in git and in the drift reviews; entry IDs stay stable, because other files cite them. | L1681–1687 |
| `DR-74` | **Each amendment piece runs with three readers and the usual rounds**, and its output is appended beside the pass, never a rewrite. Pieces after the first may use trimmed reading lists; that trimming applies to amendment pieces only, never to the city runs. | L1404–1410 |
| `DR-116` item 2 | **A pointer line at the end of an old file is a pass-file edit:** it is applied only when the dockets are applied, and `DR-101` is to be reconciled then. | L1814 |

## The rules

### 1 · A scoping register is itself a derivation

**A register that scopes a re-derivation is itself a derivation:** it gets the same three-reader check before any
piece is planned from it, and its "by citation" rows count as unread rows. *(Added 2026-11-04, `M-302`; Mirny
amendment layer.)*

### 2 · A draft register is where to look, never a budget

**A draft register is where to look, never what to budget a piece by.** Each register section is replaced by the
verified piece's result in the same unit that verifies it. *(Added 2026-11-04, `M-316`/OBS-13; amendment
layer.)*

### 3 · Notices and pointers go at the END of a file

**Notices and pointers added to an existing file go at the END of the file, never the head, so no cited line
moves**, and only where a ruling permits the edit at all (`DR-101`; `DR-116` item 2). A notice sweep includes the
record and readiness-check files. *(Added 2026-11-04, `M-308`/OBS-5; amendment layer.)*

### 4 · A notice or pointer line gets a second reader

**A notice or pointer line written into an existing pass file is read by a second reader before it is committed,**
against the whole finding it touches, not only the sentence it names. Such a line is written only where a ruling
permits the edit at all (rule 3). *(Added 2026-11-04, `M-303`; amendment layer.)*
````

## 4 · Raw check output (pasted, not summarized)

**How the location-name list for the layering check was built:** 86 names, one per line, in `locnames.txt` (scratch). They are every city spec name under `Cities/Specs/` (38 cities, with spaces for underscores), common real-world aliases (McMurdo, Jang Bogo, Zucchelli, Vostok and others), the 13 district folder names (the zodiac signs), and the nation and region names that appear in canon. The check compares each file before and after the edit; the counts that are already there belong to the unedited files and are not this change's to fix.

### 4.1 American English sweep (1), layering by name (2), lines per file (3): `run_checks.py`

````text
=== (1) AMERICAN ENGLISH SWEEP (full-word patterns; only 'judgement' kept) ===
POSITIVE CONTROL line: The colour was organised in the centre; the row was labelled grey; a judgement stays; synthesis and emphasis are fine nouns.
POSITIVE CONTROL hits: ['colour', 'organised', 'centre', 'labelled', 'grey']
POSITIVE CONTROL: PASS (found exactly the 5 planted British forms; 'judgement' kept; 'synthesis'/'emphasis' nouns not flagged)
T8_Standing_Brief_Lines.md                                                  inserted lines scanned:   22  hits: 0 
PRE-TRIP_INSPECTION_RECIPE_TRIAL.md                                         inserted lines scanned:   17  hits: 0 
03_The_Phase_Spine.md                                                       inserted lines scanned:    2  hits: 0 
04_QA_Gates_and_Differentiation.md                                          inserted lines scanned:    3  hits: 0 
Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md       inserted lines scanned:    6  hits: 0 
Mechanical_Extraction_Field_Guide.md                                        inserted lines scanned:    2  hits: 0 
00_RUNBOOK.md                                                               inserted lines scanned:   30  hits: 0 
Test_Runs/OBSERVATIONS_and_Methodology_Findings.md                          inserted lines scanned:   16  hits: 0 
Amendment_Layer_Rules.md                                                    new-file lines scanned:   57  hits: 0 
TOTAL lines scanned: 155

=== (2) LAYERING CHECK: location names in edited 03, 04 and SBL, original vs copy (case-sensitive, whole word) ===
name list: 86 names (locnames.txt)
-- 03_The_Phase_Spine.md
   names present (name, original count, copy count, count inside inserted lines): [('Davis', 2, 2, 0), ('Mirny', 1, 1, 0), ('Sinheung', 1, 1, 0)]
   NEW names not in the unedited file: none
   names whose count increased: none
-- 04_QA_Gates_and_Differentiation.md
   names present (name, original count, copy count, count inside inserted lines): [('Davis', 2, 2, 0), ('Sinheung', 1, 1, 0), ('Zhongshan', 11, 11, 0)]
   NEW names not in the unedited file: none
   names whose count increased: none
-- T8_Standing_Brief_Lines.md
   names present (name, original count, copy count, count inside inserted lines): [('Casey', 1, 1, 0), ('Mirny', 4, 4, 1)]
   NEW names not in the unedited file: none
   names whose count increased: none

=== (3) LINES PER FILE (from difflib, original vs copy) ===
file                                                                            orig     copy   +lines   -lines
T8_Standing_Brief_Lines.md                                                        40       61       22        1
PRE-TRIP_INSPECTION_RECIPE_TRIAL.md                                             1100     1110       17        7
03_The_Phase_Spine.md                                                           1200     1201        2        1
04_QA_Gates_and_Differentiation.md                                               928      931        3        0
Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md             95       98        6        3
Mechanical_Extraction_Field_Guide.md                                             505      507        2        0
00_RUNBOOK.md                                                                   3179     3204       30        5
Test_Runs/OBSERVATIONS_and_Methodology_Findings.md                              8586     8602       16        0
Amendment_Layer_Rules.md (NEW)                                                     -       56       56        0
````

### 4.2 The runbook's own layering command (RB L259 form), unedited against edited, and Step 10 item 1c for the next subject

````text
$ (cd originals/<ULM> && grep -c -F -f locnames.txt 03_*.md 04_*.md T8_Standing_Brief_Lines.md)   # UNEDITED
T8_Standing_Brief_Lines.md:4
04_QA_Gates_and_Differentiation.md:14
03_The_Phase_Spine.md:4
$ (cd rules_preview/<ULM> && grep -c -F -f locnames.txt 03_*.md 04_*.md T8_Standing_Brief_Lines.md)   # EDITED COPY
T8_Standing_Brief_Lines.md:4
03_The_Phase_Spine.md:4
04_QA_Gates_and_Differentiation.md:14
$ grep -c "Casey" <inserted (+) lines of every diff>   # Step 10 item 1c, next subject
0
````

### 4.3 Nothing outside the list was touched (4); run before this preview document was written

````text
$ sha256sum -c original_sha256.txt   # repo originals vs the hashes recorded when the copies were made
Worldspace/Locations-and-Levels/Universal_Location_Methodology/T8_Standing_Brief_Lines.md: OK
Worldspace/Locations-and-Levels/Universal_Location_Methodology/PRE-TRIP_INSPECTION_RECIPE_TRIAL.md: OK
Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md: OK
Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md: OK
Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md: OK
Worldspace/Locations-and-Levels/Universal_Location_Methodology/Mechanical_Extraction_Field_Guide.md: OK
Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md: OK
Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md: OK
$ find . -newer original_sha256.txt -type f -not -path "./.git/*"   # repo files modified after the copies were made
(end of list)
$ git status --porcelain -- <the 8 targets> <ULM>/Amendment_Layer_Rules.md
(end of status)
$ git status --porcelain --untracked-files=no   # whole repo, tracked changes (same six as at session start)
 M Dev-Road-Map/Weekly_To-Do_-_Current.md
 M Game-Mechanics/Perks/Regular_Perks_-_Level-Up.md
 M Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/DR-56_Amendment_Register_2026-10-13.md
 M Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/ULM_Runs_Casey_Then_Mirny_Handoff_2026-11-03.md
 M Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md
 M Worldspace/Locations-and-Levels/Universal_Location_Methodology/MASTER_Process_Tracker.md
$ (cd scratchpad/rules_preview && find . -type f | sort)   # the only files written as copies
./Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md
./Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md
./Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md
./Worldspace/Locations-and-Levels/Universal_Location_Methodology/Amendment_Layer_Rules.md
./Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md
./Worldspace/Locations-and-Levels/Universal_Location_Methodology/Mechanical_Extraction_Field_Guide.md
./Worldspace/Locations-and-Levels/Universal_Location_Methodology/PRE-TRIP_INSPECTION_RECIPE_TRIAL.md
./Worldspace/Locations-and-Levels/Universal_Location_Methodology/T8_Standing_Brief_Lines.md
./Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md
$ bash -n apply_rules.sh
syntax OK (script NOT run)
````

### 4.4 M-301 applied to the new reader lines 10 and 11: a worked example through the verifier

Agent 1 follows lines 10 and 11. Agent 2 writes notes directly after its staged block, which line 10 forbids. Agent 3 writes a reading-log line that begins `LMID:`, which line 11 now forbids.

````text
$ ls m301_test; cat agentA.md agentB.md agentC.md   # worked example (scratch)
----- agentA.md
### PROOF: /tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/883d8609-cb3a-4820-b3cb-6bfce797ee04/scratchpad/rules_preview_work/m301_test/source.md
LRANGE: FULL
LINES: 12
L1: # Worked example source
LMID: The middle line is this one.
LLAST: Last line of the file.
QUOTE: A load-bearing sentence sits here.

READING LOG
- line 1 (first): "# Worked example"
- line 6 (middle): "The middle line"
- line 12 (last): "Last line of"
----- agentB.md
### PROOF: /tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/883d8609-cb3a-4820-b3cb-6bfce797ee04/scratchpad/rules_preview_work/m301_test/source.md
LRANGE: FULL
LINES: 12
L1: # Worked example source
LMID: The middle line is this one.
LLAST: Last line of the file.
QUOTE: A load-bearing sentence sits here.
STAGED OUTPUT ENDS
working notes the reader kept after the marker
----- agentC.md
### PROOF: /tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/883d8609-cb3a-4820-b3cb-6bfce797ee04/scratchpad/rules_preview_work/m301_test/source.md
LRANGE: FULL
LINES: 12
L1: # Worked example source
LMID: The middle line is this one.
LLAST: Last line of the file.
QUOTE: A load-bearing sentence sits here.

READING LOG
LMID: 6 - The middle line (first words)
$ python3 Tools/triple_read_verify.py required.txt agentA.md agentB.md agentC.md
required files: 1
agents: agent1, agent2, agent3

=== /tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/883d8609-cb3a-4820-b3cb-6bfce797ee04/scratchpad/rules_preview_work/m301_test/source.md ===
  agent1   ✅ all fields match ground truth
  agent2   ⛔ QUOTE NOT IN ADMISSIBLE RANGE  (not found anywhere in this file - fabricated, sha1:aa7247821191)
  agent3   ⛔ LMID  MISMATCH  claimed='6 - The middle line (first words)'  actual='The middle line is this one.'

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
````

## 5 · What was changed from the draft's text, and why

**Changes made because of your decisions**

1. **M-260 (PTR, after L618), rewritten under `DR-117` item 2 (decision 3).** The text now states the allowance: a single failed PROOF field may be repaired by the reader that wrote it (re-check that field, correct only that field, log the repair). The draft's precondition ("when every failed field is a PROOF transcription field ... and the reading log and the body are intact") was dropped. Its closing "A QUOTE not found ... re-dispatches the slot fresh" was replaced by "any other Round 2 failure (a missing PROOF block, or anything that touches the reading itself) follows the rule above: re-dispatch the failed slot". So the text does not call a field repair a fresh-slot matter. **Two readings to confirm (section 6, a).**
2. **R-1 (RB Step 4), under `DR-117` item 1 (decision 2).** Added: **"Confirmed" means the previous unit's result is written to file; the next unit may then start**, followed by "it does not wait for the developer's review, which comes at the end of the day (`DR-117`)". It contains no text saying the developer reviews first. OBS-1's softer form (schedule a fold-in, then run beside the input) is not carried (decision 8). The rule is formatted as a runbook box with your verbatim sentence from `DR-107`.
3. **Amendment-layer rules: a separate file (decision 4).** M-302, OBS-13, OBS-5 and M-303 are rules 1 to 4 of `Amendment_Layer_Rules.md`, with registers first and notices second. OBS-4 is struck. The runbook gets one pointer line after L3150, just before the `---` and "# Where everything lives".
4. **M-303 (new file, rule 4)** gained one sentence: "Such a line is written only where a ruling permits the edit at all (rule 3)", which carries decision 6 (Conflict 4) into M-303 as well as OBS-5. No pointer line is added to any pass file by this change.
5. **OBS-2 (decision 9).** The rule reads "give the tool's version or last-change date", "so the run can be matched to the repairs recorded in the tool's own docstring". Nothing in it says a repair was unrecorded. Its log entry (M-306) corrects the piece's premise and cites the three docstrings, `SBL` §C and `DRL` L1169.

**Changes made for correctness or fit, in the draft's spirit (strike any you do not want)**

6. **Standing-line numbers.** The draft numbered line 10 (§A), 11–19 (§B) and 20 (§A). Markdown numbers a list from its first item, so "10, 20" in §A would display as "10, 11" while the raw text says 20. As applied: §A gets **10, 11**, §B gets **12–20** (table in section 1). A one-line italic note heads each new block ("numbered on so that lines 1–9 keep their numbers"). The note also starts a new list, so the numbers display as written. Lines 1–9 are unchanged.
7. **OBS-15 (line 11) gained one sentence**, found by applying M-301 to the line itself: *"Never begin a reading-log line with a PROOF field name and a colon (...): after a PROOF heading the verifier reads such a line as that field."* In the worked example (raw output in section 4), a reading-log line `LMID: 6 - ...` written after the PROOF block overwrote the field, and the verifier reported `LMID MISMATCH`. The same example confirmed that line 10 (M-254) is still needed: notes written directly after the staged block failed the QUOTE.
8. **M-264 (line 13): the reason was corrected; the rule is unchanged.** The draft said "The audit excludes the pass's own folder, so it cannot catch a misquote of an earlier step". Since 2026-10-21, `--own-pass` does find quotations of an earlier step (`SBL` L30). The text now reads: *"By default the audit excludes the pass's own folder, and even with `--own-pass` it never checks a file against itself or reads a dot-file, so it can miss a misquote of the pass's own text."*
9. **OBS-2 placement.** The draft said "SBL §C, after L31". L31 is a table row, and a paragraph there would split the table, so the text went after the paragraph that follows the table (after L38). The rule also gained "(write "uncommitted edits" as well if `git status` lists the tool)", because `git log` alone gives a stale date for a tool that has been edited but not committed.
10. **OBS-8 in SBL** was appended to the quotation-audit row's last cell (L30, in place) rather than added as a new line. The draft named the row, and an in-place edit moves no line.
11. **Tags.** `[date]` became 2026-11-04. Every OBS tag also carries its new log number (for example `M-306`/OBS-2). The draft's labels R-2 and R-3 were dropped from tags because they use the R- prefix that the new line 17 (M-282) forbids, and they collide with the Step 10 R-series (R-177, R-183). R-1 is cited as `DR-107`. M-319 records the mapping (R-1 = `DR-107`, R-2 = OBS-5 = M-308, R-3 = OBS-8 = M-311).
12. **MP-3 (PTR T5).** The draft said "replace L448–453". Only L448–449 were replaced; that is the sentence "no new marker needed there", which contradicts the tool. The Instrument paragraph (L451–453) was kept, with one phrase changed ("the `08_Review_Panel.md` Lover-faculty line" became "the `08_Review_Panel.md` late marker"). That paragraph explains that the tool prints both verdicts for a human to compare, which is why the Step 8 record must carry the comparison.
13. **M-248 (PTR L807)** keeps "C.1's two Step-0 boxes" at the end of the new list. The draft's replacement dropped it, but the row's aim was to add the missing files, not to remove one. The draft's sentence about the disciplines follows the command in italics.
14. **M-247 (PTR L801)** was changed in place and given a short tag, "(Changed 2026-11-04, `M-247`; Mirny Step −1.)". The draft gave a tag only for the box sentence.
15. **M-252** has three different line shapes. In `03` L855 the draft's text became the list item, and its path line (L856) was kept. In RB L1979 (a table cell) the SUPERSEDED clause sits in parentheses after the file name, inside the "inputs" list. In PTR L965 (a table row) it was appended to the Tier cell. All three are in place, so no line moves.
16. **M-250** gained a lead-in, "Round 3's prompt also carries a sixth section, after the fifth:". It sits inside the §N.2 box, where the fifth section is described (L682–684). The prompt's code block (L632–643) was not touched: the draft did not target it, and the fifth section is not in it either.
17. **The RB clauses for M-256/M-259 (L2713) and OBS-2 (L2711).** The draft named "one clause" for each but gave no text. Both were written from the rows' own texts.
18. **M-279** gained the pointer `Corpus_Reference_Sheets/No_National_Stereotypes_Quick_Reference.md` L76–78. That is where the draft's status column locates the "defensive note" wording, and the lines were checked.
19. **M-287, RB half:** the tag is "*(Added 2026-11-04, `M-287`.)*". The draft gave no run for this half.
20. **M-275 (QRD).** Step 3 keeps the "Different content is not differentiation" quotation, which `04` L491–492 also carries. The tags read "Re-extracted from `04` ...".
21. **M-251 (MEFG)** went after the compliance check's last paragraph (after L203, before the `---` at L204). Inserting after L205, as the draft's span suggests, would put it under RULE 2's separator.
22. **Consequential, not a draft row: RB L2709.** It said "**The nine lines** every three-reader brief and its record must carry". After this change that count is false, so it now reads "**The standing lines** ... (lines 1–9 since 2026-10-21: ...; lines 10–20 added 2026-11-04)". It is separable; strike it if unwanted.
23. **Observation entries** are written in the log's latest form (bullets, like M-300 to M-304). They were written from the text of ST9 §5 (L578–593), not from the draft's one-line summaries, and each ends with where its rule now lives. Two figures carried from the draft were checked at their sources before use: 37 to 5 (`Amendment_Rederivation_P10_Catalog_2026-11-04b_T8_Rounds.md` L389) and the Step 5 piece's one unrepaired field (ST9 L251, "116 of 117 ... not repaired").

## 6 · Flags for your decision (nothing below blocks the apply)

- **a. M-260, two readings.** (1) `SBL` line 1 counts QUOTE among the PROOF fields, so under `DR-117` a single failed QUOTE may now be repaired by the same reader; the draft had excluded QUOTE. (2) "Where several fields failed, each is repaired the same way, one field at a time" is my reading of "a single failed PROOF field". It follows the precedent `DR-117` cites ("as happened in several pieces"; M-260 repaired 10 fields). Narrow either one if that was not meant.
- **b. OBS-16 is logged (M-318).** Your instruction for the log excluded only OBS-4 and OBS-14. Decision 1 strikes rows "marked not for the rules (OBS-14)", and the draft marks OBS-16 that way too. It is logged as an observation and flagged "not made a rule". If it should not be logged, delete M-318 and renumber M-319 to M-318.
- **c. RB L2979 ("If yes, it is `unmet`") is left as written,** as the draft proposed (decision 6). The new paragraph right after it qualifies it. A later rewording of L2979 itself would remove the tension.
- **d. PTR L718–720** says "the UNANIMOUS output is DISPLAYED to the developer before being treated as final". It was not edited. Under `DR-117` this reads as the end-of-day display, not a gate on the next unit, and R-1 now says so. Align the wording later if you want.
- **e. The new file's tags name Mirny** ("amendment layer"), as the draft's tags did. The Layering Law table (RB L223–228) does not list this file. If it should count as universal like `01`–`05`, strip the location from its four tags.
- **f. Line 12 (M-257)** keeps "only with the developer's OK" for amending a brief after a repeat refusal. Under `DR-117`'s daytime mode, that slot waits for the end-of-day review. The text is kept as approved.
- **g. Already in `SBL` and not touched:** L3 and L20 name Mirny, and L30 names "Mirny's Phase 7" (draft Conflict 7).

## 7 · What was not done

**Not done, by design or by instruction**
- No repo file was edited. No git command was run other than read-only status and `rev-parse`. `graphify` was not used. The apply script was not run.
- **The rulings log** (`DEVELOPER_RULINGS_LOG.md`) was not edited. The row-by-row approvals, which `DR-117` lists as "Not decided", still need filing (draft plan, step 7).
- **The Derivation Mechanisms copies** were not touched. They are to be refreshed after the commit, with the refresh recorded in that repo's `SYNC_RECORD.md` (its ULM row is L34), and that repo's commit needs your OK.
- **The M-252 tool inputs** (`Tools/pretrip_template_casey_2026-09-30.md` L330, `Tools/build_datasheets.py` L780–781) were not touched. They are outside the file list.

**Checks the draft lists for after application, not run here**
- **Step 10 item 10:** re-open each target and confirm every approved row landed. This preview's diffs show it on the copies; repeat it on the repo after apply.
- **The pins (RB §C.4):** check whether a `Pre-Contamination_Reviews/` file pins any edited file, and re-tag only those.
- **`Tools/phase_discipline_check.py` on Mirny's folder and on a test copy (for MP-3):** not run, because it reads a pass folder.
- **`Tools/triple_read_verify.py` on worked examples (M-301):** run for the new reader lines 10 and 11, which are the only new lines that touch the reader-output format. Lines 12–20 and the §C notes are orchestrator procedure, not PROOF-format lines, so they were not run through the verifier.

**Could not do**
- Nothing was blocked. The draft's note that the QRD's "re-read 2026-10-30" stamp (L5) over-claims has no proposed text, so L5 was left as it is.

## 8 · To-do: citations of runbook lines that go stale when this is applied (draft plan, step 8; not done)

**Shift in the runbook** (original line → line in the copy): §C.8c and everything above Step 4's standing reminders, **no shift** · Step 5 L2753 → L2760 (**+7**) · Step 6 L2886 → L2897 (**+11**) · Step 7 L2922 → L2936 (**+14**) · Step 8 L2962 → L2978 (**+16**) · Step 9 L2986 → L3006 (**+20**) · §9.5 L3017 → L3039 (**+22**) · Step 10 L3057 → L3080 (**+23**) · "# Where everything lives" L3153 → L3178 (**+25**). Inside Step 4, lines move by +1 after L2694 and by +7 after L2724.

1. **`Stepwise_Execution/01_Spine/S06`–`S12`.** Their "Origin: ... lines N–M" stamps cite runbook lines. Re-extract them from the edited runbook.
2. **`Corpus_Reference_Sheets/`: the Step 9 and Step 10 quick references.** Refresh them, since Step 9 moves +20 and Step 10 +23.
3. **This change's own QRD** still cites the old runbook lines. At its L4, `§"Step 6" (L2886–L2921)` becomes **L2897–L2935**. At its L96 (L93 before this change), `L2917–L2918` becomes **L2928–L2929** and `L2919–L2920` becomes **L2931–L2932**.
4. **`MEFG` L388 (the Step 9 datasheet description).** Refresh it for OBS-11: a deferral that names any step now reaches that step's brief.
5. **`T8_Standard_Entries.json`.** Run `Tools/build_t8_standard_entries.py <pass folder> <git ref>` to re-locate the standard spans.
6. **Pre-Trips (Casey and the 26 pre-seeded cities) and their datasheets.** Run `Tools/remap_line_citations.py <Pre-Trips and datasheets> --base 8777bb5f`, report first, and use `--apply` on your word.
7. **Stale by design, not to be edited:** Mirny's records (`DR-101`), and the observation log's historical entries (for example `OBSL` L8343, which cites RB L2963).
8. **Not affected:** citations of standing lines by number ("line 4", "line 5"), since lines 1–9 keep their numbers, and every runbook citation above L2694 (for example PTR L675's §C.2 L1221–1241).
