# Input validation log — the ULM pass folders' sheets, city by city (2026-11)

**Why** (developer, 2026-11-18): *"check to make sure that all the information is valid and correct/accurate"*, then, while the DCI
preparation runs in the parallel session: *"I'd like to spend time double-checking and verifying the ULM-necessary files/sheets for other
cities as well. We'll go one city at a time."*

**The procedure, the same for every city:** back up the pass folder; **three validators** check the Pre-Trip, the position ledger, the
README and the 19 datasheets row by row against their live sources and the rulings since the sheets were built (each recomputing every
derived figure); **a fix writer** re-checks each problem at its source and applies the certain and likely ones in place, line by line (no
line added or removed: other files cite these by line), with a dated note on each corrected figure; **a separate checker** confirms every
change at its source, diffs against the backup, and re-runs `verify_city_sheets.py` and `audit_city_inputs.py`; the rest go to the developer
as questions in `DECISIONS_NEEDED_FROM_DEVELOPER.md`. The working files (reports, backups) stay in the preparing session's scratchpad.

**Also, every time: the shared quick-reference sheets** (developer, 2026-11-18: *"make a note to validate during each double-check to fix
the shared quick-reference sheets, because we're still going one city at a time (just to make sure to be thorough)"*). The validators check
every shared sheet the city's datasheets point to (the Tier U sheets in `Corpus_Reference_Sheets/` and any other sheet several cities
share), the fix writer corrects them under the same rules, and the checker confirms those changes too. A shared sheet corrected for one
city is re-checked, not skipped, on the next: each city's double-check covers the shared sheets it points to as they stand that day.

| City | Date | Problems found | Fixed | Questions | Tools after | Note |
|---|---|--:|--:|---|---|---|
| Ariun Nuur | 2026-11-18 | 111 | 109 | DEC-660 to DEC-666 | verify 20 checks, 0 FAIL; audit 40 tests, 0 GAP | the sheets now use the name Ariun Nuur (`DR-42`); none of 75 composition figures wrong; the verify tool's carried-name check missed the old name in the ledger's title |
| Mawson | 2026-11-18 | 116 | 112 + 6 by the orchestrator | DEC-667, DEC-668 (and DEC-661); all answered in `DR-142` | verify 20 checks, 0 FAIL; audit 40 tests, 0 GAP | the checker found 3 of 120 changes wrong (fixed); 40 datasheet lines cited the spec at a path without its subnet folder (fixed); the fix writer had renumbered a dated developer note in place (restored word for word, the renumbering moved into the correction after it) |
| *Shared sheets (with Mawson)* | 2026-11-18 | 54 | 51 | DEC-669 to DEC-672, answered in `DR-142` | 6 of 6 full-text sheets match their sources | 12 sheets; most full-text sheets had not been re-copied after the 2026-11-04 method edits; the treaty sheet lacked Art. II.2.5 |

**Rule learned 2026-11-18 (Mawson):** a fix writer never rewrites the developer's own dated notes; a correction goes after the note, which keeps its wording.

## Tokens spent on the validation (subagents; the orchestrator's own share is not reported)

| City | Validators | Fix writers | Checkers | Total |
|---|--:|--:|--:|--:|
| Ariun Nuur | 751,043 (A, B, C) + 92,899 memory scan | 314,841 | 275,543 | 1,341,427 + the `DR-142` pass 426,167 (writer 265,548, checker 160,619) = **1,767,594** |
| Mawson, with the shared sheets | 693,972 (A, B, C) + 301,135 (D, shared) | 319,625 + 281,509 | 253,301 + 245,784 | 2,095,326 + the `DR-142` pass 769,846 (method and shared writer 130,009, checker 156,799, correction writer 120,174; Mawson writer 239,101, checker 123,763) = **2,865,172** |

**After the developer's answers (`DR-142`, 2026-11-18):** the method change (substitute 1 deferred to after the pass) was made at its source and in six files in all (`M-404`, `M-405`); the shared sheets got the treaty, Davis-pointer and food-figure items; Mawson's sheets 18 changes (all confirmed); Ariun Nuur's sheets and six source files 53 changes (49 confirmed, 4 fixed after the check). **Rule learned:** a correction to a line about two cities states the basis the line itself used (here the Primary tier, not the founders).

**`DR-142` item 2 corrected the same day** (developer, *"Only 3 and 4"*): the orchestrator had put the option as "substitutes 2 to 4", but substitute 2 reads another location; the checker of the method edits caught it (`M-406`). The corrected rule is now in every copy: 32 line changes in 14 method files, extracts and shared sheets, the full-text sheets and extracts diffed against their sources word for word, no line count changed; the two city Step 7 rows and both startup files corrected by the orchestrator; a final search finds only struck "was" wording. **Left, for a later sweep:** two finished cross-check startup prompts (Davis/Sinheung L30, Shirayuki/Zhongshan L45) still call own earlier states a legal comparison; `S08`'s header and the Pre-Trip template's L173 and L488 give stale runbook line numbers.

**Next city in the validation: Temirotkel** (Mawson subnet), when the developer says to go on.

