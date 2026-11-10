# Zhongshan (Opus): cross-check log, 2026-11-10

**What this is.** The Step 9.5 record (the recording law) for the finished-city cross-check of Zhongshan's Opus pass, run on
2026-11-10 under `Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md`.
It logs what happened, including snags, dead ends, killed findings and self-corrections. Times are `date` readings.
**Everything this run writes is PROPOSED** (`DR-101`, `DR-102`); no pass file is edited; nothing is committed. The
`Zhongshan_Sonnet` trial folder is not opened or touched (`DR-105` item 4; `DR-106`).

---

## Entries

**Z-01 · 06:45 · Isolation, stated first (startup file Section 0.3).** This run follows another city's cross-check in the same
session (another location: not used). **Zhongshan is worked on its own terms, by fresh readers with clean briefs only:** no file,
figure, verdict, tool output, question or wording from that other run goes into any Zhongshan reading list, brief or record, and the
orchestrator never compares the two. Zhongshan's generators and templates are written fresh in their own scratch folder
(`scratchpad/zs/`). Every other city is named by role only, as "(another location: not used)", unless a line is a relation taken from
Zhongshan's own lines (`DR-122` item 5). A fresh session would have been the stronger isolation (startup Section 0.3); this run uses
the permitted one because the clock allowed it.

**Z-02 · 06:45 · Clock and window.** `date` reads 06:44 at the decision point; the window is 05:00–14:59; no new piece starts after
13:30. Web calls so far this session (all agents): "WebSearch: 53 | WebFetch: 87 | TOTAL: 140" (`Tools/web_quota_count.py`).

**Z-03 · 06:56 · Exposures, logged (none used).** (a) Finding the column labels of
`Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md`, a `sed` printed its L28-31, four rows for other locations
(another location: not used). (b) A `grep` of the rulings log for the heading of the `DR-25` row "Records can draw people" also
returned L1886, which lies in the span L1872-1925 holding the end of `DR-123` and the closed rulings `DR-124` to `DR-128`; that
line concerns another location. It is not used, cited or carried into any Zhongshan list, brief or record; the general canon of
those rulings is taken only from `startup` Section 4. (c) `build_pretrip.py --list` prints its city keys (names only). (d)
`queue` L597-600 (`DRQ-11`) carries a sentence about another location's pass; it is kept out of every Zhongshan list.

**Z-04 · 06:56 · The old note's sources re-read.** `git log 8777bb5f..HEAD` and `git diff --stat 8777bb5f` (the commit that wrote the
2026-11-03 note) show no change in: the census, the spec, `09`, `11`, `16`, `Extent`, the Founding Register, the two language
files, the alias table, the relationship database, the inspiration files and both research rounds, the culture file,
`05_Remaining_Cities_Assessment.md`, the shared table, the research log, `Ports`, `Highways`, `Airports`, `Geothermal`, the
transshipment file, or the pass folder (only this log is new). Changed: the rulings log ("1 file changed, 216 insertions(+)", one
hunk at L1715 onward) and the 2026-11-03 run handoff in `Research_Logs/` (its 12-point sentence moved from L28 to L25). The Timeline's
`No_National_Stereotypes.md` has no commit since 2026-10-01. Each cited line was printed and matched (census L502, L643, L554,
L694, L857, L862, L869-871; spec L15, L16, L20-22, L92, L102, L163, L165, L173, L180, L192; `09` L50, L72; `11` L292; `16` L275,
L1917, L1921, L1923, L1925, L1926, L1932, L1934; `Extent` L84, L577, L593, L613, L655; Register L60; language csv L775-780, L790;
reference L36, L77; alias table L11, L12, L102-105, L107; inspiration L103-106; `Ports` L129, L130, L202, L229, L230; relationship
database L488, L495; `Geothermal` L38, L39, L205; `Highways` L60, L292, L349; culture file L22-24, L38, L110). A script recomputed the
composition from `spec` L36-70; it returned: "rows 35 first L 36 last L 70", "sum shares 99.986", "Primary 1 35.830",
"Significant 3 24.100", "Notable 31 40.056", "under2 23 under1 15 under0.1 10", "cum 3 52.83", "cum 10 79.97", "cum 11 82.83",
"lead ratio 3.694 rest 64.17", the four column sums equal to the census, "row shares by pop equal? True", "russian 12 5.685",
"caucasus6 0.292". The rock by Census I share: "14.4545 12.01 8.41 36.136" (km2; % of footprint at 10,000 and 7,000 per km2; % share).
**New since the old note:** the spec's L165 and L180 now read as corrected (`DR-105` item 4), so the pass's quotation at
`01_Inherited` L66-67 and its flag at `02_Spine` L45-50 no longer match the spec (note ZSO-015).

**Z-05 · 06:56 · Pass searches for the later rulings (pattern, result).** Robot origin: `robots? (carry|have|had|bring|brought|inherit)
.{0,40}(origin|nation|homeland|culture)|origin.{0,40}robot|DR-11\b|immersion` → no lines; a wider search of four files for lines
with "robot" and origin words found `04_Phase_02` L47 and `04_Phase_08` L132 (item C9). Arrivals: `after the (treaty|signing)|no
(new|further|later) arriv|...` → `04_Phase_02` L221, `04_Phase_08` L889; then `closed system|closed border|refreshed from|only
opened one way|one way|no new arrivals|never refreshed|no correction from` → 17 lines in 6 files (item C10). Records: `station's
(records|logs|archive)|...|translat` → one line, `05_Reconciliation` L456 (a sweep schedule; not a records conclusion): no item.
Rock: `one third|one-third|a third of|13\.33|divid... (oasis|rock)...` → `02_Spine` L216, L279; `04_Phase_07` L230, L475, L620,
L917; `07_QA_Gates` L93 (`04_Phase_08` L325, L885 are about the plurality, not rock) (item C8). `DR-1`'s Spine clause "unsparing
honesty" → 0 lines in the pass folder. `DR-26`'s struck phrases → `05_Reconciliation` L434 records the ruling as applied.
**Self-correction:** the first draft of note section I said `DR-106` to `DR-123` had no Zhongshan item; `DR-106` does (D-7).
Corrected before any reader saw the note.

**Z-06 · 06:56 · Sheets: blocked, as the startup file expected.** Tools last committed 2026-10-30 (`9f6abe9f`); no uncommitted
edits. `build_pretrip.py --list`: exit 0, 32 lines; Zhongshan is not a city key and is not among the three listed under "Not built
by this generator:". `make_t8_required_list.py "<pass folder>" 8`: exit 2, "unknown target '8'. Use step:-1, step:0..3, step:5..10
or phase:2..10." (my target typo). Then `... phase:8`: exit 2, "no T8 block found for phase:8 in the Pre-Trip sheet". The Pre-Trip
has no "T8" string at all (`grep -n -i 'T8'` → nothing). No tool edited; no `--force`. **Every reading list in this run is built
by hand** from the note, the pass and the sources it cites. Question: `DEC-460`.

**Z-07 · 06:56 · The fresh note.** `Amendment_Notes_2026-11-10_Cross_Check.md` written: sections A (standing decisions), B to E
(current facts), F (15 conclusions: C1 to C10, U1 to U5; C8, C9 and C10 are new from `DR-105` item 4, `DR-11` with `DR-128` item 1,
and `DR-127` item 2), G (source defects; SD-5 and SD-6 new), H, I, J (empty until the item round). Step 6 is write-only: the
shared table's Zhongshan rows (L53, L65, L77, L90, L103, L113, L125, L135, L148; headers L48, L60, L72, L85, L98, L108, L120, L130,
L143) were extracted by `scratchpad/zs/tools/own_rows.py`, which prints no other row; a first script that looked for a Zhongshan
column found none ("no table with a Zhongshan column found"; the table has one row per city).

**Z-08 · 07:00 · Exposure, logged (not used).** Looking for the column labels of the language-sets reference, a `sed -n '1,12p'`
printed its L7-10, four rows for other locations. Not used. The labels are at L5; Zhongshan's row is L36.

**Z-09 · 07:00 · The Treaty added to the note before any reader saw it.** The Timeline's `Falkland_Treaty_Draft_v1.md` carries
Article II.2.5 (L50), added 2026-11-09 (Timeline commit `23e5226`, "Add Falkland Treaty II.2.5: humans may relocate to Tepenia
after signing"); ZSO-021 and row C10 now cite it with IV.2.3 (L77) and II.2.1 (L46). **The note is frozen from here until the
item round's Round 2 has run** (the readers prove a FULL reading of it): 240 lines, `sha256` `0c1afa724a3a8095`.

**Z-10 · 07:00 · The item round's lists and briefs.** Generators written fresh in `scratchpad/zs/tools/` (`zs_paths.py`,
`zs_items.py`, `zs_check_brief.py`). Each of the 15 items has its own private staging folder `scratchpad/zs/items/<ID>/` with
`required.txt` and `brief.md`; the note is entry 1 of every list (FULL); each path appears once, its spans merged in ascending
order with no overlap, and every span checked to lie inside its file. Entries per list: C1 5, C2 4, C3 4, C4 9, C5 8, C6 7, C7 6,
C8 8, C9 5, C10 8, U1 4, U2 6, U3 5, U4 3, U5 5. **Brief-versus-list check** (`zs_check_brief.py`), first run: 13 briefs
"MISSING: 0"; C5 "citations: 11; OK: 8; MISSING: 3" (my brief text named three lines of the language-sets file right after the
csv's name, so they were read as csv lines; the brief was reworded to name the file, regenerated with `--redo C5`, and rechecked:
"citations: 11; OK: 11; MISSING: 0"); C8 "citations: 11; OK: 7; MISSING: 4": census L505 and L509, cited twice in C8's
orchestrator-verified result, which says they are another location's rows and not on the list (standing line 4) — accepted as
stated. **Positive control:** a copy of C1's brief with "L9999" added returned "citations: 5; OK: 4; MISSING: 1 /
MISSING 04_Phase_08_Making.md 9999-9999". **One brief read end to end** (C10, 103 lines; standing line 24): no placeholder left;
the list, the standing lines (part A, lines 1-6, 10, 11, copied by the generator from the file and asserted by number) and the
output form read as intended.

**Z-11 · 07:12 · Self-correction to Z-06, and one exposure.** Z-06 says the sheet tools had "no uncommitted edits"; I had not run
`git status` on them. Run now, it lists " M .../Tools/make_t8_required_list.py" (13 insertions; file time 2026-11-09 17:25,
before this session; not edited by this run). Its refusal for Zhongshan ("no T8 block found") does not depend on the added lines,
which skip rows marked forbidden. Reading that diff showed a code comment naming a decision number from a section of the decisions
file closed to this run; nothing of that section was opened. Web count, run correctly: `web_quota_count.py --tasks <this
session's tasks folder>` → "WebSearch: 53 | WebFetch: 87 | TOTAL: 140" at 07:01 (a first run without `--tasks` read the tool's
default folder, another session's, and returned "TOTAL: 11004"; not this session's count).

**Z-12 · 07:12 · The item round, returned and checked.** All 15 readers returned between 07:03 and 07:09. Round 2 (`zs_r2_item.sh`:
`triple_read_verify.py <list> <out> <out> <out>`) returned "UNANIMOUS - CLEARED TO WRITE" for all 15, each on its first run.
**Positive control:** C7's output with its second LMID replaced returned "⛔ NOT UNANIMOUS - DO NOT WRITE." (exit 1). Every output
has one PROOF block per list entry (counts 5/5, 4/4, 4/4, 9/9, 8/8, 7/7, 6/6, 8/8, 5/5, 8/8, 4/4, 6/6, 5/5, 3/3, 5/5). Names check:
a list of 56 other-location names and aliases built from the census rows and the alias table, `grep -w -F` over each output's
body (above its PROOF blocks): "none" in all 15; over the QUOTE, LRANGE and LINES fields: nothing; positional fields that carry a
name have EXEMPT lines (C1 1, C4 1, C5 1, C6 2, C7 1, C8 3, U1 2, U2 2, U3 3, U4 1). Verdicts: FLIPS 1 (C10); NARROWS 13; HOLDS 1
(U4); the note's section J gives each verdict line as `grep` returned it. **Two readers broke the no-other-file rule in their own
staging folders:** U1's reader left `check_proof.py` (32 lines; `grep` for open-for-write or `write(` finds nothing; it says it
compared its hand-copied PROOF fields read-only), and C1's reader says it wrote and then deleted a helper script (its output L135);
how the deletion was made is not known from its output. The piece briefs now forbid creating or deleting any file (rule 5).
Filed beside the pass (`cp -n`; `cmp` checked for two): `.xc_20261110_item_<ID>.md`, `_round2.txt`, `_brief.md`,
`_required.txt` for all 15 (60 files). The note's section J was then written by script; the note is now 261 lines, `sha256`
`3f2e1e9400d064c4`, and is frozen from here until the last piece's Round 2.

**Z-13 · 07:12 · The pieces, in dependent order (`DR-107`).** Wave 1 (independent of one another): `P02_Arrival` (C10, C6, C9),
`P07_Order` (C7, C8, U1, U3), `P03_Research` (U5). Wave 2, after `P02_Arrival` is merged and checked, because items C2, C4 and
C5 name C10's outcome as a condition, and C9's guard sits inside Phase 8: `P08A_Composition` (C1, C2, C3, C4, U2) and
`P08B_Language` (C5), each with the merged `P02_Arrival` piece on its list. U4 holds: no piece. Wave-1 lists: 15, 19 and 6
entries; the three readers' lists of each piece are identical (`cmp`); the three briefs of each piece differ in 14 lines (title,
reader letter, staging folder, output path, number range). Brief-versus-list check: P02 "citations: 21; OK: 21; MISSING: 0" ×3;
P03 "citations: 1; OK: 1; MISSING: 0" ×3; P07 "citations: 17; OK: 13; MISSING: 4" ×3, the census L505 and L509 of the
orchestrator-verified result, stated there as not on the list (accepted, as in Z-10). One generated brief read end to end
(`P07_Order` reader A, sections 0 to 4): as intended.

**Z-14 · 07:30 · A defect in the note, found by a reader (P07 reader C), confirmed by me.** The note's row U1 (section F) reads
"Zhongshan is a partner in a joint agricultural research project led from another location (seed breeding, phosphorus and soil
recovery)". `rulings log` L1387 lists "agricultural research (as a joint-venture ongoing research project shared with ... Zhongshan),
seed breeding, phosphorus and soil recovery" as separate mandated roles of the other location, and L1421 gives each its own share
(the joint project 4%; seed breeding 3%; phosphorus and soil recovery 6%, "a national role"). So the parenthesis attaches the other
location's own roles to the joint project. **Cause: I carried the wording of the 2026-11-03 note's row U1 without re-reading L1387
against it.** The note is frozen until the wave-1 pieces' Round 2 has run (their readers prove a FULL reading of it); it is corrected
after that, before wave 2 is dispatched, and the correction is logged with the new hash. The P07 merge is told of it through the
reader's own output (union rule).

**Z-15 · 07:35 · Wave 1, Rounds 1 to 3.** Round 1: the nine readers returned between 07:22 and 07:34 (P03 first). Round 2
(`zs_r2_piece.sh`, three readers' files as the three arguments): P03_Research, P02_Arrival and P07_Order each returned
"UNANIMOUS - CLEARED TO WRITE" on the first run; no staging folder holds any file but the brief, the list and the output. P03
Round 3: six cross-verdicts CONSISTENT (`grep` of the three replies: six lines); its merge writer was dispatched at 07:27. P02 and
P07 Round 3 sent at 07:34 (each reader continued by SendMessage, pointed to its own `round3_message.md`). **The note's U1 row
corrected (Z-14)** after the last wave-1 Round 2 had run: one line (section F, L205) rewritten in place, line count unchanged at
261, `sha256` now `79e43941c1a22e78`. Wave 2's readers prove against this version.

**Z-16 · 07:45 · Piece P03_Research merged, checked, recorded.** The merge writer returned at 07:44: the piece
`Amendment_Rederivation_P03_Research_2026-11-10.md`, 506 lines. Checks (`zs_postmerge.py`), run before the record existed:
**snag and fix in my own pre-check:** its first run paired quotation marks across a whole line and reported 9 strings not found, 8
of them spans of text between two separate quotations, and its corpus lacked the merge writer's own list (the merge rule's file); I
rewrote it to pair marks within a paragraph block and to add that list. Rerun: "corpus files: 36; quoted strings (12+ chars,
paired within a block): 72; not found: 1; blocks with an odd quote count (hand-check): 0" — the one is "Merge writer", the piece's
own column label. **Positive control:** a copy with a fabricated quotation appended returned "NOT FOUND (block at L508): the city
keeps three moons above its harbor all winter long". Quotation audit: "INSTRUMENT VALID: YES"; "NOT FOUND in corpus: 11"; triage
"(a) found in the corpus: 5; (b) the piece's own unquoted prose: 6; (c) for hand triage: 0". American English: 0 hits. Names: 0.
Status words: 2, both in L10's statement that nothing calls the pass, the review or the city complete or ready. Round record
written by `zs_record.py` (152 lines); reader files, Round 2 run, Round 3 replies, audit output, merge log and merge brief are
beside the pass as `.t8_xc_P03_Research_*`.

**Z-17 · 07:57 · Piece P02_Arrival merged, checked, recorded; wave 2 dispatched.** The merge writer returned at 07:47: the piece, 844
lines. Checks: pre-check "corpus files: 40; quoted strings (12+ chars, paired within a block): 248; not found: 5; blocks with an odd
quote count (hand-check): 0"; audit "INSTRUMENT VALID: YES", "NOT FOUND in corpus: 28", triage "(a) 8; (b) 9; (c) for hand triage:
11"; American English 0; names 0; status words 0. **Hand triage, read at each line:** the 5 pre-check strings are the piece's own
proposed wording in plain quotation marks (it puts source quotations in italic quotation marks); of the 11 class (c) fragments, ten
are the piece's prose between two adjacent quotations and one (L558) is its proposed restatement. No misquotation found. Record:
215 lines. **Wave 2 generated** (`P08A_Composition` 17 entries, `P08B_Language` 10; each list carries the merged
`P02_Arrival` piece whole; three lists identical per piece; briefs differ in 14 lines; brief-versus-list "MISSING: 0" for all six).
**Snag, fixed before dispatch:** the generator's template does not say what an earlier piece on the list is; a sentence was added to
all six briefs, and that sentence first carried an unsourced quotation ("permanently unavailable"), against standing line 18; it was
rewritten unquoted, and the six briefs rechecked ("MISSING: 0"). Six readers dispatched at 07:57.

**Z-18 · 08:00 · Piece P07_Order merged, checked, recorded.** The merge writer returned at 07:59: the piece, 839 lines. Checks:
pre-check "corpus files: 45; quoted strings (12+ chars, paired within a block): 175; not found: 11; blocks with an odd quote count
(hand-check): 0"; audit "INSTRUMENT VALID: YES", "NOT FOUND in corpus: 14", triage "(a) 2; (b) 6; (c) for hand triage: 6";
American English 0; names 0; status words 0. **Hand triage, read at each line:** the 11 pre-check strings are proposed replacement
wording written after the pass address each would replace; class (c): four connective spans, two proposed texts. No misquotation
found. The piece states the U1 correction of Z-14 without proposing a further change to the note. Record written.

**Z-19 · 08:22 · Wave 2, Rounds 1 to 3.** P08B_Language: readers returned 08:12 to 08:14; Round 2 "UNANIMOUS - CLEARED TO WRITE"
(first run); Round 3 sent 08:15, six cross-verdicts CONSISTENT (two `grep` lines in each reply); merge writer dispatched 08:19.
P08A_Composition: readers returned 08:18 to 08:22; Round 2 "UNANIMOUS - CLEARED TO WRITE" (first run); Round 3 sent 08:22. No staging
folder holds any file but the brief, the list and the output. The note was unchanged through the last Round 2 (`sha256` `79e43941c1a22e78`,
as at Z-15); it is no longer frozen.

**Z-20 · 08:37 · Piece P08B_Language merged, checked, recorded.** The merge writer returned at 08:29: the piece, 783 lines. Checks:
pre-check "corpus files: 38; quoted strings (12+ chars, paired within a block): 184; not found: 1; blocks with an odd quote count
(hand-check): 0"; audit "INSTRUMENT VALID: YES", "NOT FOUND in corpus: 18", triage "(a) 4; (b) 7; (c) for hand triage: 7";
American English 0; names 0; status words 0. **Hand triage, read at each line:** six connective spans; L557 is the piece's label for a
disputed reading. No misquotation found. P08A Round 3: six cross-verdicts CONSISTENT; its merge writer dispatched at 08:27.

**Z-21 · 08:51 · Piece P08A_Composition merged, checked, recorded.** The merge writer returned at 08:51: the piece, 1,159 lines. Checks:
pre-check "corpus files: 43; quoted strings (12+ chars, paired within a block): 226; not found: 7; blocks with an odd quote count
(hand-check): 0"; audit "INSTRUMENT VALID: YES", "NOT FOUND in corpus: 22", triage "(a) 7; (b) 8; (c) for hand triage: 7"; American
English 0; names 0; status words 0. **Hand triage, read at each line:** the 7 pre-check strings are proposed wording or readers'
phrasings named in section 5 and section 6; class (c): seven connective spans. No misquotation found. All five pieces are now merged,
checked and recorded.

**Z-22 · 08:53 · Questions, summary, tracker; the run stops here.** `DEC-460` to `DEC-473` written in a new section of
`Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md` directly above `## Answered` (highest number before: `DEC-451`; next
multiple of ten: 460); a check of the new section returned no other-location name, no British spelling and no status word. The note's
section J gained J.2, the five pieces with line counts and `sha256` (by script). `REVIEW_SUMMARY_2026-11-10_Zhongshan_Cross_Check.md`
written. The tracker's FINISHED-CITY REVIEWS block got one dated status line, inserted after the last dated line (found by line number
only; no earlier text rewritten). Web calls for the whole session: "WebSearch: 137 | WebFetch: 92 | TOTAL: 229". Not done, as the
startup file says: no commit, no push, no pass file edited, no other run started, the review not declared complete or ready.

**Z-23 · 08:54 · Self-correction: three names of other locations in my own records.** A final sweep of this run's log, note and summary
(`grep -w -F` against the 56-name list) returned two hits in the log and one in the note (the hit lines are not reproduced here, because each is another location's name). Each was my wording, not a tool's
output: Z-04 named a handoff file by two locations' names, Z-22 named the run the startup file says not to start, and the note's
ZSO-016 row quoted a ruling line that names another location. Each was rewritten in place on its own line (no line moved): the handoff
is now "the 2026-11-03 run handoff in `Research_Logs/`", Z-22 says "no other run started", and the note says "Zhongshan is exempt,
with one other location (not used)". Rerun of the sweep: see below. The rerun returned no hit in the log, the note or the summary.

**Z-24 · 10:50 · The developer's answers (walk-through at 10:05 to 10:50).** All fifteen questions answered (`DEC-460` to `DEC-473` and
the Element question of `DR-1`); fourteen took the recommended option; one differs: freight, "All three routes". Recorded as `DR-130`
in the rulings log and as ANSWERED in the decisions file (with `DEC-004`). **To apply:** the order piece's import wording (U3) is
revisited for the three routes; the culture file's three corrections; pointer lines into the pass files, with a second reader.

**Z-25 · 11:18 · Applying the answers (the developer chose all four follow-ups at 11:12).** (1) **Imports re-derivation**
`P07B_Imports` (item U3, after "All three routes"): three readers dispatched at 11:15 on identical 8-entry lists (the note, the U3
item output, the merged order piece, the U3 pass and source spans, `DR-130` L1935-1941); brief-versus-list "MISSING: 0" ×3.
**Snag, fixed before dispatch:** the brief's added paragraph cited `DR-130` "L1938"; the line holding the quoted text is L1940
(`sed` and `grep -o` returned it there); corrected in all three briefs. (2) **The queue** (`Developer_Ruling_Queue.md`): the
headings of `DRQ-10` and `DRQ-13` marked answered and `DRQ-11` marked narrowed and split, each on its own heading line ("1 file
changed, 3 insertions(+), 3 deletions(-)"; no line moved). (3) **The culture file** (`Cities/Local_Cultures/Mirny_Subnet/Zhongshan.md`):
L22-24 (the tier table, to the spec's L20-22), L38 (the founding-wave sentence) and L110 (the language line) rewritten in place with
dated correction notes ("1 file changed, 5 insertions(+), 5 deletions(-)"; no line moved). (4) **Pointer lines drafted**, not applied:
`Pointer_Lines_DRAFT_2026-11-10.md` in this folder, one line per numbered pass file (23), for the developer's approval and a second
reader.

**Z-26 · 11:52 · The imports piece merged, checked, recorded; pointer lines.** `P07B_Imports`: Round 2 "UNANIMOUS - CLEARED TO WRITE";
Round 3, six cross-verdicts CONSISTENT; merge writer returned at 11:46: 661 lines. Checks: pre-check "not found: 0"; audit
"INSTRUMENT VALID: YES", "NOT FOUND in corpus: 5", triage "(c) for hand triage: 1" (L153, connective prose); American English 0; names
0; status words 0. Record written (158 lines); the note's J.2 table gained its row. Its five new questions became `DEC-474`.
**Pointer lines:** the developer chose to hold them until the corrections are applied (`DR-132`), with the two-part wording and the
checker's closing clause. `Pointer_Lines_DRAFT_2026-11-10.md` was rebuilt in that form (23 lines, with `P07B_Imports` on the Phase 5
and Phase 7 rows), and a fresh second reader was dispatched at 11:52 to sort each listed piece into its part and to look for files
with no row.

**Z-27 · 12:04 · Pointer lines checked, then held (`DR-132`).** The second reader returned "OK: 13 · FLAG: 10": four listed pieces only
cite the file as a source (removed), six only name it as a place for a later note (moved to that part), and four were missing (the
imports piece on the Spine; three name-only entries). It also found that three files (`06`, `09.5`, `10`) end inside a blockquote,
so a blank line before the pointer is required there. Its output is beside the pass as `.ptr_check_2026-11-10.md`.
`Pointer_Lines_DRAFT_2026-11-10.md` rebuilt by script on its sorting: 23 lines, marked HELD until the corrections are applied.
Nothing is appended to any pass file.

**Z-28 · 13:14 · The follow-ups (`DEC-474`) answered and applied (`DR-133`).** Answers: add the cluster to Australia's receiving
nodes, then, told of the 2026-10-03 three-node reminder, "Four nodes; supersede 10-03"; the coastal line by highway for certain, the sea
leg to be researched; the cargo split and the further terminals left open; both lines extended. **Source edits, in place, no line
moved:** `Ports.md` L129 (the cluster added; "four-node"), L188 (the 2026-10-03 reminder marked superseded in part; its text kept),
L202 (the cluster's row: canon node; Zhongshan's three routes), L386 (the node-tier row); `City_Relationship_Database.md` L495
(Zhongshan's routes). `git diff --stat`: "2 files changed, 5 insertions(+), 5 deletions(-)". **Research dispatched** (13:14) on the
sea leg: real-world sea ice and shipping off the Larsemann Hills, year-round or seasonal. **Imports revisited again:**
`P07C_Imports` (U3; the earlier imports piece and `DR-133` on the list; Ports spans widened to L186-190 and L382-386), three readers
dispatched at 13:15, briefs "MISSING: 0" ×3; one unsourced quotation in the generated preface rewritten unquoted before dispatch.

**Z-29 · 14:04 · Research, the sea-leg answer, and the second imports revisit recorded.** The research reader returned at 13:41: 475 lines,
77 numbered sources, a 130-entry search log; filed as `Cities/Research_Logs/Zhongshan_Sea_Access_Research_2026-11-10.md` with a header
naming the developer's question (spelling check: 5 hits, all institution names or a false match, kept). The developer chose "Seasonal, as
in reality (Recommended)": `DR-134`; `Ports.md` L202 and `City_Relationship_Database.md` L495 updated in place from "under research".
`P07C_Imports`: Round 2 "UNANIMOUS - CLEARED TO WRITE"; Round 3, six cross-verdicts CONSISTENT; merge writer returned at 13:52, 810
lines; checks: pre-check "not found: 0"; audit "INSTRUMENT VALID: YES", "NOT FOUND in corpus: 11", "(c) for hand triage: 3" (two
connective spans, one table cell of the piece's own wording); American English 0; names 0; status words 0. Record written (160 lines).
The note's J.2 gained its row and a dated current-fact line for `DR-133` and `DR-134`. Tracker status line added. The window closes at
14:59; no new piece was started after 13:30.
