# Shirayuki: cross-check log, 2026-11-10

**What this is.** The Step 9.5 record (the recording law) for the finished-city cross-check of Shirayuki run on
2026-11-10 under `Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md`.
It logs what happened, including snags, dead ends, killed findings and self-corrections, as they happen. Times are
`date` readings. **Everything this run writes is PROPOSED** (`DR-101`, `DR-102`); no pass file is edited; nothing is
committed. Shirayuki is worked on its own terms: no other city is compared with it, and other locations named by a
source are written as "(another location: not used)" unless the line is a relation taken from Shirayuki's own lines
(`DR-122` item 5).

---

## Entries

**L-01 · 05:03 · Clock and window.** `date '+%Y-%m-%d %H:%M'` returned `2026-11-10 05:03`, inside the 05:00–14:59
window. The one-shot job set at 23:36 the night before fired at 05:03 as scheduled.

**L-02 · 05:03–05:05 · Section 1 reading list, read.** `00_RUNBOOK.md` in full (3,204 lines, five Read calls);
`Amendment_Layer_Rules.md` (63 lines) and `T8_Standing_Brief_Lines.md` (69 lines) in full; the rulings named in
Section 1 item 3; the tracker's SESSION BOOT (L137–L250) and the finished-city block from its heading (L363) through
its "not started" status line (L368); Shirayuki's folder `README.md`, its stale note
`Amendment_Notes_2026-10-30_Manual_Input_Audit.md` (251 lines), `Drift_Review_Shirayuki_2026-11-03.md` in full, the
summary's general part (L1–L16) and its Shirayuki lines (L22, L29, L34, L35, L37, L52, L53, L55–L56); the decisions
file's open entries that name Shirayuki (only `DEC-003`, L36–L40; the grep returned L36–L38); the method model
`Mirny/REPASS_COMPLETE_2026-11-04.md` L1–L24 (the unit table only; its findings sections were not read).

**L-03 · 05:04 · Exposure (self-correction).** One Read call on `DEVELOPER_RULINGS_LOG.md` (offset 1664, 172 lines)
displayed `DR-100` to `DR-118` whole. Section 1 item 3 asked for `DR-103` item 4, `DR-104` item 3 and `DR-105`
item 4's general and Shirayuki clauses only. **What I believed:** a single range read was the efficient way to reach
the named rulings. **Why it was wrong:** it displayed other locations' items the startup file kept out (the other
items of `DR-103`, `DR-104` and `DR-105`, and `DR-108` to `DR-115`, which are rulings about another location).
**What changed:** for every later multi-location ruling the lines naming Shirayuki were located first by line number
(`awk` on the ruling's range, numbers only), and only the heading, the verbatim line and those lines were printed.
Nothing outside the named items is used in any brief, list or record of this run. Nothing from `DR-124` to `DR-128`
was opened.

**L-04 · 05:05 · Exposure (incidental).** A bare `git status --short` printed, among the modified files, the names of
ten untracked dot-files in a closed folder (another location's pass folder: not used). No file there was opened. From
here on `git status` is run only with a path filter.

**L-05 · 05:05 · Blocked step: no Pre-Trip, no datasheets.** `python3 Tools/build_pretrip.py --list` (tool last
committed 2026-11-02; no uncommitted edits) lists 27 cities and then, under "Not built by this generator:", the line
`Shirayuki      its ULM pass is complete (Tri-Cities)`. `python3 Tools/build_datasheets.py Shirayuki --out <scratch>`
(same commit date; no uncommitted edits) stopped with `KeyError: 'Shirayuki'` raised at `build_pretrip.py` line 177
(`c = CITY[key]`) and wrote nothing. Neither tool was edited and `--force` was not used. **Consequence:** every reading
list in this run is built by hand from the amendment note, the pass and the sources the pass cites. Written as a
question in the decisions file (Shirayuki section).

**L-06 · 05:05 · Snag: section letters.** The startup file (Section 2 item 3) and `DR-104` item 3 say one reader per
item "in the note's section F". In the stale 2026-10-30 note the conclusions table is section **G** ("Conclusions that
rest on current inputs and may change on re-derivation"); its section F is source defects. The fresh note places the
conclusions table in section **F** so that the startup file, `DR-104` item 3 and the note agree; source defects move
to section G. Recorded so the next reader of both notes is not misled.

**L-07 · 05:06 · Tool versions.** `triple_read_verify.py` last committed 2026-11-03, no uncommitted edits;
`quotation_audit.py` 2026-11-02, none; `web_quota_count.py` 2026-10-26, none (its default task folder is another
session's; this run passes `--tasks`); `make_t8_required_list.py` 2026-10-21 **with uncommitted edits** (`git status`
lists it as modified). Not used for Shirayuki (no Pre-Trip exists for it to read).

**L-08 · 05:06–05:12 · Every source line the 2026-10-30 note cites, re-read.** Census L422, L424–L428, L502, L505,
L509, L653; spec L23, L35, L41–L48, L54, L56–L67, L99, L108–L111, L157–L158, L188, L203, L221, L321; Register L8–L14,
L36, L61, L90; queue L551–L702; `City_National_Connections.md` L388–L394; `16` L1, L247, L277, L1754–L1769, L3180,
L3580; `09` L78, L126–L146, L216; extent L616, L656–L660; the language reference and CSV; physiology L75, L103, L426;
alias table L10–L15, L105, L107; `Airports.md` L13, L18; `Ports.md` L202, L579, L611; institutes file L97–L109; the
immigration file L559–L570; symbol assignments L117; the walkthrough, ledger and to-do lines; the handoff L25–L47; the
culture file L9, L34, L42, L48, L100, L262, L263 (by pattern only). `git log --since='2026-11-03 22:00'` on each:
the one later commit (`8777bb5f`, 23:03) touches none of Shirayuki's lines (`git show -U0` hunks at other rows).
Results that changed the note: (a) the handoff's language lines moved (the rule is now at L25, the culture-file list
at L46–L47; Shirayuki not listed). (b) The general language rule is cited from `DR-100`, not from `DR-89`: `DR-89` is
an entry recorded for another location (T8 brief line 25). (c) The national-connections file's entry for the
Halley-subnet city (L140–L142) is that city's own line, so under `DR-122` item 5 it is no longer cited for Shirayuki's
tie. (d) Every figure recomputed by command matched the 2026-10-30 note's current-value columns (cluster density is
83,268.5 per km²; the stale note rounds it to 83,269).

**L-09 · 05:09–05:12 · Later-rulings scan (T8 brief line 21), against the pass's own open questions.** The pass's five
queue entries are all still marked open in the queue except `DRQ-14` (closed 2026-10-01). Found: `DR-4` (Census I
governs the band) and `DR-105`'s noted row (Shirayuki Band 5) bear on `DRQ-10`; `DR-105` item 4 ("rock-founded (the
site sets the difficulty coefficient)") bears on `DRQ-13`; `DR-105` item 4 (the rock "divided by Census I share,
stated as arithmetic") bears on `DRQ-11` without naming an allocating authority; nothing found for `DRQ-12`. The pass's
reserved "robot national origin" (Frame §8 item 7; Phase 2 A.3; Phase 9 §B) meets `DR-11` (robots carry a national
origin, learned by immersion; "It is no longer open. They do.", `LOG` L457) and `DR-12` (robot columns ADMITTED-DEMOTED
like the human ones); both were read in full at `LOG` L448–L475 for this reason, outside the startup file's list. The
startup file's quoted general canon (Section 4) bears on Phase 2's arrival modes (items 2 and 4) and on the robot
columns (item 3). `DR-122` item 5 bears on the kinship ties. Result: five new conclusion items (`SRY-C04` to `SRY-C09`,
less the renumbered ones) and one new open item (`SRY-U05`) in the fresh note's section F; 14 items in all.

**L-10 · 05:13 · Fresh note written.** `Amendment_Notes_2026-11-10_Cross_Check.md`. **Self-correction, same minute:**
its first draft of `SRY-013` quoted the culture file's phrase that names one neighboring city; reworded by role
before any reader saw the note.

**L-11 · 05:14 · Decisions file.** `DEC-440` (no sheets can be built for Shirayuki) and `DEC-441` (whether two queue
questions are closed by later rulings) inserted in a new section "Open since 2026-11-10 (Shirayuki cross-check …)"
directly above `## Answered`, by script, after a backup; `diff` against the backup shows 18 added lines and no other
change. The highest number before insertion was `DEC-435` (`grep -o … | sort | tail -1`).

**L-12 · 05:16 · Self-correction: a standing answer cited from another location's clause.** The note's `D-3` and the
generator's plan result cited `DR-105`'s clause "a re-derivation … uses the rulings as they stand", which `LOG` L1712
records for another location. **What I believed:** the tracker (L365) cites `DR-105` for that rule, so the clause was
the source. **Why it was wrong:** T8 brief line 25 requires the entry that records the words for this location.
**What changed:** `D-3` now cites `DR-104` item 3, `DR-106` items 1 and 3, `DR-105` item 4's own Shirayuki clause
(Shirayuki follows the plan) and the startup file; the plan result was dropped from the briefs (no item test needs it).
**Knock-on snag:** the `D-3` edit added one line to the note, shifting every later note line by one; the generator's
note ranges were re-taken from a fresh `grep -n` before any brief was built.

**L-13 · 05:18 · Brief defects found by reading a generated brief end to end (T8 brief line 24).** The first `SRY-C06`
brief cited `LOG` L1711–L1712 and the note's L29–L34 in its results, and neither was in that reader's list (startup
Section 2 item 5). Fixed in the generator: every list now admits each line its brief cites (`LOG` L1711–L1712, L1713,
L1527, L919, L1868 where cited; the note's L29–L34 everywhere). Because several ruling lines hold items for several
locations in one line, a ninth rule was added to every brief: use only the general clauses and the clauses naming
Shirayuki. The plan result was removed from `SRY-C05`. All 14 briefs regenerated; `SRY-C07`'s brief and list read
end to end after regeneration.

**L-14 · 05:19 · Broken instrument, caught by a positive control.** The first script written to check each brief's cited
lines against its list reported "OK" for all 14. A positive control (a copy of one list with the cited ruling lines
removed) also returned "OK": the script's pattern matched no source bracket at all, so every "OK" was an empty check.
Rewritten (`scratchpad/sry/tools/check_brief_vs_list.py`) to print how many cited segments it parsed. Two controls now
fail as they must (`DEVELOPER_RULINGS_LOG.md L1711-1711 not admitted`, `… L1712-1712 not admitted`; and
`Amendment_Notes_2026-11-10_Cross_Check.md L29-34 not admitted`, `02_Spine.md L121-138 not admitted`); the 14 real
folders pass with non-zero counts (1 to 3 source segments and 2 to 12 pass spans each).

**L-15 · 05:20 · Inputs frozen for the item round.** The note (356 lines, `sha256` `eb553bcbde9a00de`) is not edited
until the 14 item readers have returned. Briefs and lists hashed (scratchpad `sry/items/*/`). Each reader has its own
staging folder (T8 brief line 23).

**L-16 · 05:21 · Correction to L-09 (appended, not reworded).** L-09's count reads wrong: the new items are **six**
conclusion items (`SRY-C04` to `SRY-C09`) and **one** open item (`SRY-U05`), beside the seven carried from the
2026-10-30 note (`SRY-C01` to `SRY-C03`, `SRY-U01` to `SRY-U04`): 14 in all.

**L-17 · 05:21 · Item round dispatched.** 14 fresh readers, one per section F item, each given only the path of its own
frozen brief (which names its own list and staging folder). Model: the session's Opus.

**L-18 · 05:27 · Item `SRY-U02` returned: NARROWS.** Reader output 120 lines; manifest 4 of 4. Round 2 (`triple_read_verify.py`
run on the one output three times, saved as `sry/items/SRY-U02/round2_verify.txt`): 12 ✅, 0 ⛔, "UNANIMOUS - CLEARED TO
WRITE". What the reader's file says (its points SRY-U02-24, -29 to -35): the core ("THE QUESTION IS ASKED AND DELIBERATELY
NOT ANSWERED", `04_Phase_06_Meaning.md` L168) holds; the refinement at L179 ("because the national practice already runs in
the same register as the local value") no longer follows as written, citing physiology L77–L78 ("One possibility among
several, not the only disposition."), L84, L96–L98, L114 and L143. Goes to re-derivation.

**L-19 · 05:29 · Item `SRY-C09` returned: NARROWS.** Output 141 lines; manifest 5 of 5; Round 2: 15 ✅, 0 ⛔,
"UNANIMOUS - CLEARED TO WRITE". The file's points SRY-C09-15 to -22: the descendants of the refused party still live here
(spec L65), but the share, headcount, rank ("fifth-largest") and Significant-tier weight of `01_Inherited.md` L217–L218 and
`02_Spine.md` L135 no longer follow; which rows count as the refused party (the successor row alone; with the four pieces
spec L54 names; with Taiwan, which L54 classes as a new pool) is a choice no admitted line makes. **Process snag, recorded
as the reader states it (SRY-C09-28):** "I wrote it after all reads were done, in one session with no interruption, not
entry by entry as the brief asks." The PROOF fields verify, so the reading happened; the log-as-you-go rule was not kept.

**L-20 · 05:29 · Item `SRY-C08` returned: NARROWS.** Output 261 lines; manifest 7 of 7; Round 2: 21 ✅, 0 ⛔,
"UNANIMOUS - CLEARED TO WRITE". Points SRY-C08-12 to -19: the allocation stands and nothing admitted makes the founders
choosers or the allocation appealable; but the added geographic ground (Register L61, L11, L14) removes part of the wording
of `02_Spine.md` L94 (second sentence), L102 ("there is nothing to reach for"), L104, and `01_Inherited.md` L215, and
leaves `04_Phase_02` L107's "opposite direction" to re-check. Open to the reader: what "the rule" at whose edge "zone gap 3"
sits means (no admitted line says).

**L-21 · 05:29 · Item `SRY-C01` returned: NARROWS.** Output 160 lines; manifest 6 of 6; Round 2: 18 ✅, 0 ⛔,
"UNANIMOUS - CLEARED TO WRITE". Points SRY-C01-15 to -22: the Significant tier has two members now (spec L47), so the Act 1
ground "one large group and four equal middle groups" (`04_Phase_02` L64) and "unusually FLAT" (L60) no longer follow; the
Act 2 half (L67–L70) and "none of them the founding one" (L61) hold; whether two co-equal Significant origins make an
available second pole is answered by no admitted line. The reader also notes (SRY-C01-24, -25) that the pass's flatness
reading was itself a within-tier reading that `DR-12` bars, and that the current tier boundary came partly from a random
multiplier (spec L54); neither decided.

**L-22 · 05:30 · Item `SRY-U05` returned: FLIPS.** Output 248 lines; manifest 11 of 11; Round 2: 33 ✅, 0 ⛔,
"UNANIMOUS - CLEARED TO WRITE". Points SRY-U05-14 to -23: layer (A), no station lineage acts as a cause (Frame L142,
L145; queue L698), stands; layer (B), the national tie "set aside entirely" and "currently unusable" with its question
"Raised, not resolved" (`04_Phase_05` L89–L92, L258), is contradicted by queue L696 ("ANSWERED 2026-10-01"), L699 ("The
offending line is gone"), L702 and by Shirayuki's own live entry (`City_National_Connections.md` L393–L394, "Medium,
Infrastructure."). Decide on re-derivation: whether Phase 5's wider set takes the Highway 4 tie and how it sits with §5d.2.

**L-23 · 05:31 · Item `SRY-C05` returned: NARROWS.** Output 138 lines; manifest 7 of 7; Round 2: 21 ✅, 0 ⛔. Points
SRY-C05-17 to -26: B.1's headline (`04_Phase_02` L121) holds for the allocated cohort; B.3's impossibility claims (L139,
L141), L144 ("only once") and the B.4 order (L151–L160) lose part of their ground under the general canon on arrivals after
the signing and on records drawing people; the `G4` "only" lists (Frame L307; Spine L95, L102) are narrower than `DR-26`
(research, equipment, techniques, results); "not people" stands.

**L-24 · 05:31 · Self-correction found by a reader (SRY-C05-31).** The note's `SRY-015` heading says none of that
canon "was in force when the pass ran". **Checked:** the rulings log dates `DR-11` and `DR-12` to the section headed
2026-09-28 (`LOG` L420) and `DR-24`–`DR-26` to 2026-10-01 (L625, L636, L652); the pass ran 2026-09-06 to 2026-09-13
(commit `5c339aee`, 2026-09-06) and its last content edit is `4a59fab8` (2026-10-01 21:48, "apply the audit fixes"), and
the pass cites `DR-24` and `DR-25` (Frame L307; Spine L95). **What changed:** the heading is wrong for five of its rows.
The note is frozen while readers run; the heading is corrected after the item round, with this entry as its record.

**L-25 · 05:31 · Item `SRY-C02` returned: FLIPS.** Output 136 lines; manifest 5 of 5; Round 2: 15 ✅, 0 ⛔. Points
SRY-C02-15 to -23: the band line "4 — URBAN" (Frame L28) and Reading A (L178) are contradicted by `LOG` L1713 (Band 5 on
Census I) and by `DR-4`'s ground (L211, L217–L218); the re-derivation declares Band 5 with the distributional analysis
stated as deferred by ruling (L249–L251) and restates §2, §2a's "Band 5 → Band 4" row (L190), §6 L288 and L292, §10 L364.

**L-26 · 05:31 · Item `SRY-C03` returned: NARROWS.** Output 215 lines; manifest 8 of 8; Round 2: 24 ✅, 0 ⛔. Points
SRY-C03-15 to -26: the speech-marker reasoning (`04_Phase_08` L210–L240, L404–L409) holds; L206's ground (the dominant
vernacular derived from Japan's share) no longer follows under `DR-100` (1); Japanese is the supporting tier alone; Phase 9
L96's wording survives but its reading, inherited from §F, must be restated; how physiology L426 combines with Hawaiian
dominance for robots is answered by no admitted line.

**L-27 · 05:31 · Item `SRY-U01` returned: NARROWS.** Output 130 lines; manifest 4 of 4; Round 2: 12 ✅, 0 ⛔. Points
SRY-U01-13 to -22: the supply line, the four-month window and the berthing queue hold; the merger mechanism of §6 is
labeled "[CANON — Ports.md], not derived here." (`04_Phase_05` L222), and the port section's own SCOPE block calls it
"a PROPOSAL" whose adoption "A culture pass on that" / "cluster should decide" (`Ports.md` L688–L690); adoption is
decided in no admitted line. **A source-status finding, not an input change**; the reader cannot tell whether the SCOPE
block predates the pass (SRY-U01-29).

**L-28 · 05:31 · Item `SRY-U04` returned: HOLDS.** Output 136 lines; manifest 8 of 8; Round 2: 24 ✅, 0 ⛔. Points
SRY-U04-12 to -20: the tier, the founders, the plurality and the precondition are unchanged; the language rule and origin
are consistent with a Japanese stock and with coining no term. Only the figure at `04_Phase_08` L318 differs, recorded in
the note (L157, L315). Not re-derived. The reader's doubts SRY-U04-26 (the "no change" at L404 may need re-reading if
§F is restated) and -29 (Japanese-derived vocabulary also arrives through the national language) are carried to the
`SRY-C03` piece's list of things to decide.

**L-29 · 05:32 · Item `SRY-C04` returned: FLIPS.** Output 186 lines; manifest 8 of 8; Round 2: 24 ✅, 0 ⛔. Points
SRY-C04-13 to -20: the pass's "reserved" status (Frame L331; `04_Phase_02` L90, L355; `04_Phase_09` L60, L336) and its Act 2
answer ("THERE IS NOTHING TO INHERIT.", `04_Phase_02` L86; "vacuous", Frame L331–L332) are contradicted by `LOG` L450,
L457–L459 and the startup file L66; what survives (the table copies the human shares; no date column; WHEN matters for a
robot's culture, runbook L2237–L2238) are inputs, not the conclusion. Open, not to be decided: whether robot columns take
their own percentage; nationality versus residence at departure; whether robots kept arriving.

**L-30 · 05:32 · Item `SRY-C06` returned: NARROWS.** Output 132 lines; manifest 7 of 7; Round 2: 21 ✅, 0 ⛔. Points
SRY-C06-15 to -29: the robot-keyed "UPPER BOUND" hedge (`02_Spine.md` L82) is discharged (`16` L1763); the floor
conditional's "if" is answered by `LOG` L1712 ("the site sets the difficulty coefficient"), but whether the baseline is
still "a FLOOR" turns on the queue's step ② (an on-ice ratio in the model at all), which no admitted line answers; the
ruling's text names the coefficient and is silent on the food term; `04_Phase_04` L47 ("THE GROUND ITSELF") needs a check.

**L-31 · 05:32 · Item `SRY-U03` returned: FLIPS.** Output 159 lines; manifest 7 of 7; Round 2: 21 ✅, 0 ⛔. Points
SRY-U03-12 to -20: the kinship tie's stated ground (the plateau city's tier, `04_Phase_07` L361; `04_Phase_05` L82) is
another city's line under `LOG` L1868 item (5); whether a clause naming Shirayuki inside another subject's row (`Airports.md`
L18; institutes L109) counts as "its own lines" is decided by no admitted line; the "Medium, Demographic" tie the pass
called "UNEXPLAINED in its own source" (`04_Phase_05` L86) has a ground in Shirayuki's own entry
(`City_National_Connections.md` L391–L392): contradicted as stated. **Question for the developer arises** (what counts as
a location's "own lines").

**L-32 · 05:33 · Item `SRY-C07` returned: NARROWS.** Output 186 lines; manifest 10 of 10; Round 2: 30 ✅, 0 ⛔. Points
SRY-C07-14 to -21: "nobody" (provisional assumption 3, Frame L235) still follows and `DRQ-11` stays open as to who divided
the rock; the share's status ("MODELED, not canon", Frame L366–L367; Spine L253–L254) and the readiness limit's ground
(`10_Readiness_Check.md` L255, "`DRQ-11` is open") no longer follow under `LOG` L1712. **Question for the developer
arises** (SRY-C07-23): whether "stated as arithmetic" governs only how the share is presented, or means the rock really is
held in Census I proportions; the second reading sits uneasily with "nobody decided; first-come, then inheritance".

**L-33 · 05:33 · Item round closed: 14 of 14 returned, every Round 2 clean.** Verdicts: **HOLDS** 1 (`SRY-U04`) ·
**NARROWS** 9 (`SRY-C01`, `C03`, `C05`, `C06`, `C07`, `C08`, `C09`, `U01`, `U02`) · **FLIPS** 4 (`SRY-C02`, `C04`,
`U03`, `U05`). Round 2 totals: 291 ✅, 0 ⛔ across the 14 outputs (each run three times on the one output; one reader per
item, so Round 2 here proves the reading happened and nothing about agreement). 13 items go to re-derivation. Process notes:
one reader wrote its reading log at the end (L-19); several readers chose the stricter-or-looser verdict on a stated
tie-break and said so (SRY-C01-23, SRY-C05-33, SRY-C08-25, SRY-C09-24, SRY-U01-31, SRY-C07-25, SRY-U03-21, SRY-C04-28).

**L-34 · 05:33 · Note unfrozen after the item round, corrected, and frozen again.** (1) `SRY-015`'s heading (one line,
L268) now states the dates (rows 1, 2 and 6 predate the pass's last edit of 2026-10-01; the rest is later), per L-24.
(2) Section J (the 14 verdicts, one line each, citing the reader files) appended at L358–L384, so no earlier line moved.
Note now 384 lines, `sha256` `e65fe5aa24132170`; frozen until the T8 merges are written. (3) The 14 item outputs, their
Round 2 runs, briefs and lists copied into the pass folder as `.xc_20261110_item_<ID>*` (56 files; one checked byte for
byte with `cmp`). The item verdict files are read by the piece readers from there.

**L-35 · 05:34 · The 13 items are grouped into seven pieces, by the pass places and inputs they share.** `P00_Band` (`SRY-C02`) ·
`P02A_Composition` (`SRY-C01`, `C09`, `C04`: Phase 2 §A, the Spine's `G8`, the composition table, `DR-11`/`DR-12`) ·
`P02B_Arrival` (`SRY-C05`, `C08`: Phase 2 §B, the Spine's `G4` and §7, `01` A1, the Register) · `PS2_Ground`
(`SRY-C06`, `C07`: the Spine's §2b, §6, §6a, Phase 4 §2a, the rock across the pass) · `P05_Relations` (`SRY-U01`,
`U03`, `U05`: Phase 5 and the Phase 7 addendum) · `P06_Death` (`SRY-U02`) · `P08_Language` (`SRY-C03`, with the two
doubts `SRY-U04` left for it). **Order (`DR-107`):** no piece needs another piece's result; each re-derives from the
current inputs and its own items' verdicts, so the seven run together. Two pieces read one shared section each:
`P02B` and `PS2` both read the Spine's §7 (different claims, 2 and 3); `P02A` and `P06` both read the Frame's §8 (items 7
and 4). The merges keep each piece to its own items. Each piece's "what to decide" line points to the item readers'
own numbered points, not to an orchestrator paraphrase (Amendment_Layer_Rules rule 5).

**L-36 · 05:35 · Briefs checked before dispatch.** 21 briefs (7 pieces × readers A, B, C; identical except reader letter,
private folder and number range: A 1–99, B 101–199, C 201–299). Every brief's cited lines are in its reader's list (the
checker printed non-zero counts for all 21; a positive control with two ranges removed returned `['LOG L1713',
'00_Frame.md L360-377']`). `P08_Language` reader A's brief read end to end; one gap found and fixed (the PROOF format did
not say `LRANGE: FULL` for whole-file entries); all 21 regenerated; `diff` against the brief as read shows only that line.
Web research is permitted in three pieces (`P02A`, `P02B` optional; `P08` recommended), with exact search strings logged.
Web calls so far: 0.

**L-37 · 05:36 · T8 Round 1 dispatched: 21 readers.**

**L-38 · 05:37 · Snag: the subagent limit.** Twenty of the 21 Round 1 readers started; the 21st (`P08_Language`
reader C) was refused by the tool with "Concurrent subagent limit reached. You can run 20 subagents at once. Do not
retry." It is dispatched on the identical brief as soon as a slot frees; nothing about its brief changes. Recorded so the
order of returns is not misread as a difference between readers.

**L-39 · 05:48 · `P08_Language` reader C dispatched** on the identical brief, once `P06_Death` reader C had returned
(270 lines; manifest 5 of 5) and freed a slot. Returns are logged per piece when all three of a piece's readers are in.

**L-40 · 05:52 · `P06_Death`: Round 1 in (readers A 538 lines, B 216, C 270; each manifest 5 of 5); Round 2 run 1:
15 ✅, 0 ⛔, "UNANIMOUS - CLEARED TO WRITE" (saved `sry/pieces/P06_Death/round2_run1.txt`); Round 3 sent to all three by
SendMessage, each continuing with its own context, each given the other two outputs' paths and the six questions (the four
of §N.1, the dispositions section, the recompute section), each replying to its own file.**

**L-41 · 05:55 · Web quota check.** `Tools/web_quota_count.py --tasks <this session's task folder>` (tool last
committed 2026-10-26): "agent transcripts: 36", "WebSearch: 51 | WebFetch: 79 | TOTAL: 130", "largest single agents: [29, 26,
17]", "transcripts mentioning a web quota/rate-limit error: 1" (the transcript of `P02A_Composition` reader C, still
running). What that mention is gets checked against the reader's own research log when it returns.

**L-42 · 05:56 · `P00_Band`: Round 1 in (A 264 lines, B 312, C 283; each 7 of 7). Round 2 run 1 FAILED: 18 ✅, 7 ⛔,
"⛔ NOT UNANIMOUS - DO NOT WRITE."** All three readers, on the note entry only: `LINES MISMATCH claimed='106' actual='100'` and
`LMID MISMATCH` (the same claimed line for all three). **Cause: an orchestrator defect, not a reading failure.**
`gen_pieces.py` built every note range as the common part (`1-22,29-34,296-302`) followed by the piece's own ranges, so in
six pieces the range string is not in ascending order, and in two (`P00_Band`, `PS2_Ground`) it overlaps (`29-34` lies inside
`24-61`). `triple_read_verify.py` reads a range as the set of distinct line numbers in ascending order; the brief said
"the ((N+1)//2)-th line counted through the range's lines in order", which the readers took as list order. A script
(line numbers only, no content) shows the six affected entries: `P00_Band` listed 106 / distinct 100; `P02A_Composition`,
`P02B_Arrival`, `P05_Relations`, `P08_Language` out of order (65, 63, 73, 69 lines); `PS2_Ground` listed 125 / distinct 119.
`P06_Death`'s range was ascending and its Round 2 passed. The item round's ranges were all ascending. **What I believed:** a
range string's order did not matter. **Why it was wrong:** the verifier and the readers counted the middle line in different
orders, and the brief did not say which. **What changed:** the repair route of `DR-117` item 2 (the reader repairs its own
failed field, by hand; the orchestrator names the field and supplies no value) is used for each affected piece as its Round 2
runs; the repair request states the verifier's counting rule. Readers still running are not messaged mid-task (`M-93`); their
fields are repaired after they return. **For future generators:** emit every range ascending and without overlaps.

**L-43 · 05:58 · `P00_Band`: the three field repairs returned ("repaired: LINES, LMID"); `diff` against the pre-repair
copies shows, for each reader, only those two fields changed plus two "Round 2 repair:" lines in its reading log. Round 2
run 2: 21 ✅, 0 ⛔, "UNANIMOUS - CLEARED TO WRITE" (run 1 and run 2 both kept). Round 3 sent to all three.**

**L-44 · 05:58 · `P06_Death`: Round 3 in; all six cross-verdicts CONSISTENT** (reader A on B and C: "CONSISTENT." at its
R3-9, R3-26; reader B: "Reader A: CONSISTENT." R3-8, "Reader C: CONSISTENT." R3-23; reader C: "Reader A: CONSISTENT." R3-9,
"Reader B: CONSISTENT." R3-28). Reader outputs, Round 3 replies and the Round 2 run copied into the pass folder as
`.t8_xc_P06_Death_*`. **The one merge writer dispatched** (fresh; not a reader). Its brief was read end to end before dispatch;
one defect fixed first (rule 7 named "section 4's table" for the found-by table, which is section 3; `diff` shows only that
line). Output: `Amendment_Rederivation_P06_Death_2026-11-10.md`, new.

**L-45 · 06:01 · `P02B_Arrival`: Round 1 in (A 804 lines, B 403, C 367; each 11 of 11). Round 2 run 1: 30 ✅, 4 ⛔,
"⛔ NOT UNANIMOUS - DO NOT WRITE."** The failures are the note entry's `LMID` for all three readers (the same claimed line),
as the L-42 range check predicted for this piece (out of order, no overlap). Repair requests (`DR-117` item 2) sent to all
three for `LMID` only; pre-repair copies kept for the diff.

**L-46 · 06:04 · `P00_Band`: Round 3 in; all six cross-verdicts CONSISTENT** (A: R3-4 on B, R3-9 on C; B: R3-9 on A, R3-26
on C; C: R3-8 on A, R3-23 on B). **Merge writer dispatched.** Its brief differs from the `P06_Death` merge brief (read end to end)
only in the piece name, items and places (`diff` after substituting the names).

**L-47 · 06:04 · `P02B_Arrival`: the three `LMID` repairs returned; each `diff` shows only that field plus one repair
line. Round 2 run 2: 33 ✅, 0 ⛔, "UNANIMOUS - CLEARED TO WRITE". Round 3 sent to all three.**

**L-48 · 06:04 · `PS2_Ground`: Round 1 in (A 331 lines, B 674, C 437; each 15 of 15). Round 2 run 1: 42 ✅, 7 ⛔: the note
entry's `LINES` (claimed by all three; the verifier printed the claimed value as "[REDACTED - found at L201, outside the
admissible range, …]", because the claimed number's text also occurs on note L201) and `LMID`, as L-42 predicted. Repairs
returned ("repaired: LINES, LMID"); each `diff` shows only those two fields plus repair lines (reader A also added one blank
line in its log). Round 2 run 2: 45 ✅, 0 ⛔, "UNANIMOUS - CLEARED TO WRITE". Round 3 sent to all three.**

**L-49 · 06:05 · `P02A_Composition`: Round 1 in (A 288 lines, B 330, C 570; each 13 of 13). Round 2 run 1: 36 ✅, 4 ⛔:
the note entry's `LMID`, all three readers (claimed blank: the list-order middle line, note L300, is blank), as L-42 predicted.
`LMID` repairs requested; pre-repair copies kept.** The web-quota flag of L-41 (one transcript "mentioning a web quota/rate-limit
error", this piece's reader C): reader C's own research log (section 6) records no refused or limited call; a pattern search of
that section for rate, limit, quota, 429, blocked, fail and error matched only ordinary words in quoted source abstracts. Recorded
as most likely page text matched by the counter, not a refused call; not verified further (the counter prints counts only).

**L-50 · 06:06 · `P02A_Composition`: the three `LMID` repairs returned; each `diff` shows only that field plus one repair
line. Round 2 run 2: 39 ✅, 0 ⛔, "UNANIMOUS - CLEARED TO WRITE". Round 3 sent to all three.**

**L-51 · 06:07 · `P02B_Arrival`: Round 3 in; all six cross-verdicts CONSISTENT** (A: R3-4 on B, R3-10 on C; B: R3-4 on A,
R3-10 on C; C: R3-8 on A, R3-16 on B; C's R3-16 names "two departures" in B, a disposition difference for the merge to decide on
content). Files copied as `.t8_xc_P02B_Arrival_*`. **Merge writer dispatched.**

**L-52 · 06:07 · `P05_Relations`: Round 1 in (A 356 lines, B 473, C 415; each 18 of 18). Round 2 run 1: 51 ✅, 4 ⛔: the note
entry's `LMID`, all three readers (claimed blank), as L-42 predicted. `LMID` repairs requested; pre-repair copies kept.**

**L-53 · 06:09 · `P05_Relations`: the three `LMID` repairs returned; each `diff` shows only that field plus one repair
line. Round 2 run 2: 54 ✅, 0 ⛔, "UNANIMOUS - CLEARED TO WRITE". Round 3 sent to all three.** `PS2_Ground` Round 3: readers A and
C in (A: R3-4 on B, R3-17 on C; C: R3-4 on A, R3-10 on B; all CONSISTENT); reader B pending.

**L-54 · 06:09 · `PS2_Ground`: Round 3 complete; all six cross-verdicts CONSISTENT** (B: R3-4 on A, noting "one line count"
discrepancy; R3-10 on C). Files copied as `.t8_xc_PS2_Ground_*`. **Merge writer dispatched.**

**L-55 · 06:10 · `P02A_Composition`: Round 3 complete; all six cross-verdicts CONSISTENT** (A: R3-9 on B, R3-26 on C; B:
R3-4 on A, R3-10 on C; C: R3-5 on A, R3-11 on B). Files copied as `.t8_xc_P02A_Composition_*`. **Merge writer dispatched.**

**L-56 · 06:11 · `P08_Language`: Round 1 in (A 255 lines, B 747, C 311; each 10 of 10). Round 2 run 1: 27 ✅, 4 ⛔: the note
entry's `LMID`, all three readers, as L-42 predicted. `LMID` repairs requested; pre-repair copies kept.**

**L-57 · 06:12 · `P08_Language`: the three `LMID` repairs returned; each `diff` shows only that field plus one repair
line. Round 2 run 2: 30 ✅, 0 ⛔, "UNANIMOUS - CLEARED TO WRITE". Round 3 sent to all three.** Round 2 across the seven pieces:
one piece passed on run 1 (`P06_Death`, the one whose note range was ascending); six failed run 1 on the note entry only, as
L-42 predicted, and all six passed run 2 after same-reader field repairs.

**L-58 · 06:13 · `P05_Relations`: Round 3 complete; all six cross-verdicts CONSISTENT** (A: R3-4 on B, R3-18 on C; B: R3-4 on A,
R3-17 on C; C: R3-4 on A, R3-10 on B; C names "two contradictions" in A as disposition differences for the merge). Files copied as
`.t8_xc_P05_Relations_*`. **Merge writer dispatched.**

**L-59 · 06:16 · `P08_Language`: Round 3 complete; all six cross-verdicts CONSISTENT** (A: R3-4 on B, R3-8 on C; B: R3-11 on A,
R3-28 on C; C: R3-5 on A, R3-18 on B). Files copied as `.t8_xc_P08_Language_*`. **Merge writer dispatched.** All seven pieces have
now cleared Round 2 and Round 3; 42 cross-verdicts, all CONSISTENT.

**L-60 · 06:20 · `P06_Death`: merge returned and checked; record written.** Merge writer's return: "Section 3: 70 rows. written
(union) 36, written (conservative) 10, demoted 0, question 11, not written 13." Piece: 349 lines. Checks: (1) my pre-check first
crashed (`FileNotFoundError` on a path split at the space in "Inner Tepenia", a bug in `postmerge.sh`'s argument passing; fixed
with an `@list` argument; the control still flags the invented quotation); rerun: 293 quoted strings, 284 found, 9 not found, all 9
connective prose between adjacent quotations. (2) `quotation_audit.py --own-pass`: "INSTRUMENT VALID: YES", 137 fragments, "NOT FOUND
in corpus: 53" (1 in table cells, 52 in prose). (2b) triage script: 6 found in the readers' and item files (dot-files the audit cannot
read), 44 the piece's own unquoted prose, 3 left for hand triage; the three lines (L198, L315, L323) read in full: each is prose between
quotations. Confirmed defects: 0. (3) American English: 0 hits. (4) other locations' names: 0; status words: 0. Record
`Amendment_Rederivation_P06_Death_2026-11-10b_T8_Rounds.md` written by script after the checks. **Self-correction:** its Round 3 block
showed 4 of 6 verdict lines (pattern too narrow); a correction carrying reader A's two lines was appended at the record's end, and the
generator now refuses a record without exactly six.

**L-61 · 06:24 · `P00_Band`: merge returned and checked; record written.** Return: "Section 3 rows: 94 total — written (union)
64 · written (conservative) 5 · demoted 0 · question 8 · not written 17". Piece: 1,079 lines. Pre-check: 157 quoted strings, 127 found,
30 not found (all connective prose between quotations wrapping across lines). Audit: "NOT FOUND in corpus: 13"; triage 6 (a), 2 (b),
5 (c); the five read in full, all prose. Confirmed defects: 0. American English 0; names 0; status words 0. Record
`Amendment_Rederivation_P00_Band_2026-11-10b_T8_Rounds.md` written (the Round 3 block's count check passed at six).

**L-62 · 06:30 · `P02B_Arrival`: merge returned and checked; record written.** Return: "Section 3 rows (98 in total): 58 written
(union), 10 written (conservative), 2 demoted, 16 question, 12 not written." Piece: 1,285 lines. Pre-check: 172 quoted, 155 found, 17
not found (prose between wrapped quotations, and the record's own filename). Audit: "NOT FOUND in corpus: 9"; triage 3 (a), 0 (b), 6
(c), all read: prose or the filename. Confirmed defects: 0. American English: 4 hits, none a defect (three "realism", a pattern false
positive; one "defence" in a source domain name). **Snag in my sweep pattern:** `realis[a-z]*` matches the American "realism";
narrowed for later pieces to `realis(e|ed|es|ing|ation)`. Names 0; status words 0. Record written (six verdict lines).

**L-63 · 06:32 · `PS2_Ground`: merge returned and checked; record written.** Return: "Section 3, 123 rows: written (union) 78 ·
written (conservative) 20 · demoted 0 · question 11 · not written 14". Piece: 1,060 lines. Pre-check: 185 quoted, 185 found. Audit:
"NOT FOUND in corpus: 3"; triage 0 (a), 3 (b), 0 (c). Confirmed defects: 0. American English 0; names 0; status words 0. Record written.

**L-64 · 06:34 · `P02A_Composition`: merge returned and checked; record written.** Return: "Section 3: 97 rows — written (union)
76 · written (conservative) 12 · demoted 4 · question 3 · not written 2". Piece: 497 lines. Pre-check: 222 quoted, 218 found, 4 not found
(prose; the record's filename). Audit: "NOT FOUND in corpus: 32"; triage 17 (a), 13 (b), 2 (c), both read: the filename and a table
cell's prose. Confirmed defects: 0. American English 0; names 2 (the subnet folder in the spec path); status words 0. Record written.
**The quota flag (L-41, L-49) settled as far as the logs allow:** readers A's and C's research logs contain no rate-limit, 429 or refusal
entry; a search of reader A's log for "quota" matched only inside "quotation". The counter's flag is most likely that same word; it
prints counts only, so this is an inference, not a verification.

**L-65 · 06:40 · `P05_Relations`: merge returned and checked; record written.** Return: "wc -l: 1329"; "Section 3 rows by
disposition (102 rows): written (union) 62 · written (conservative) 12 · demoted 3 · question 14 · not written 11". Pre-check: 216 quoted,
196 found, 20 not found (prose between wrapped quotations). Audit: "NOT FOUND in corpus: 7"; triage 0 (a), 4 (b), 3 (c), all read: prose.
Confirmed defects: 0. American English: one hit, "judgment" at L298 in the writer's own prose; corrected to the kept spelling
"judgement" (one-word `sed`, `diff` shows only L298; the pre-fix copy kept in scratch); checks rerun on the corrected file: 0 hits.
Names 0; status words 0. Record written.

**L-66 · 06:42 · `P08_Language`: merge returned and checked; record written. All seven pieces now merged, checked and recorded.**
Return: "Line count (wc -l): 1153"; "Section 3 rows by disposition (84 rows): written (union) 52; written (conservative) 13; demoted 1;
question 14; not written 4." Pre-check: 217 quoted, 198 found, 19 not found (connective prose). Audit: "NOT FOUND in corpus: 15"; triage
8 (a), 6 (b), 1 (c): L651 quotes reader C's own words (its file L56); my triage missed it because it did not strip the audit's "[CELL]"
prefix. Confirmed defects: 0. American English 0; names 0; status words 0. **Totals across the seven pieces:** 6,750 lines; found-by rows
668 (written by union 426, by the conservative rule 82, demoted 10, put as questions 77, not written 73); confirmed quotation defects 0;
one spelling corrected (L-65).

**L-67 · 06:42 · Correction to L-66 (appended).** The seven pieces total **6,752** lines (349 + 1,079 + 1,285 + 1,060 + 497 + 1,329 +
1,153, summed by command), not 6,750: L-66's figure was written before the sum was run. The row totals in L-66 match the command's sums.

**L-68 · 06:44 · Questions written.** `DEC-442` to `DEC-451` inserted in the Shirayuki section above `## Answered` (78 lines added,
0 removed, by `diff` against a backup). The pieces' sections 6 hold 88 questions; nine standalone entries carry the ones that bear beyond
one sentence (several of them general: `DEC-443` own lines, `DEC-447` drawn tiers), and `DEC-451` takes the rest as a batch on their
recommended answers. **Snag:** a script that tried to list each piece's questions by pattern printed number-only rows for two pieces
(bullet styles differ between merge writers); the questions were then read by a plain line pattern and, for the standalone ones, in full.

**L-69 · 06:44 · Summary written:** `REVIEW_SUMMARY_2026-11-10_Shirayuki_Cross_Check.md` (this folder). **Tracker:** one dated
status line inserted after the finished-city block's last dated status line (tracker L374; the earlier dated lines were located by line
number only and not read; `diff` shows one added line). Shirayuki's note, log, summary and tracker line are written to file: finished
and recorded in the sense of `DR-107` / `DR-117` item 1. **Not declared complete or ready.**

**L-70 · 06:44 · Section 0.3 applied.** `date` reads 06:44, before 11:00, so Zhongshan may start in this session. It runs
with fresh readers and clean briefs only: no Shirayuki file, figure, verdict, tool output or wording goes into any Zhongshan list or
brief, and Zhongshan's generators are written fresh in their own scratch folder. Web calls so far this session: see the quota check in
Zhongshan's log. Nothing committed.

**L-71 · 11:12 · The developer's answers (walk-through, 2026-11-10).** All thirteen questions answered (`DEC-440` to `DEC-451`, and
the older `DEC-003`, deferred for every city). Every answer took the recommended option (the sheets question took the entry's own
recommendation, to extend the tools). Recorded as `DR-131` in the rulings log and as ANSWERED in the decisions file. No piece differs
from its recommendation, so none is revisited. **To apply:** the queue entries `DRQ-10` and `DRQ-13` (closed) and `DRQ-11` (split);
the tool extension in a maintenance session; pointer lines into the pass files, with a second reader.

**L-72 · 11:18 · Applying the answers.** The queue headings of `DRQ-10` and `DRQ-13` marked answered and `DRQ-11` narrowed and split,
in place (`Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md`; no line moved). Pointer lines drafted, not applied:
`Pointer_Lines_DRAFT_2026-11-10.md` in this folder, one line per numbered pass file (21), for the developer's approval and a second
reader. The tool extension waits for a maintenance session.

**L-73 · 11:45 · Pointer lines checked, then held (`DR-132`).** A fresh second reader checked the 21 drafted lines: "12 OK, 10 FLAG"
(nine lines listed pieces that only name the file as a place for a later note; one pass file, `04z_Post-Ruling_Enrichment_Review.md`,
had no line, because my draft's file pattern skipped it). Its output is beside the pass as `.ptr_check_2026-11-10.md`. The developer
chose the two-part wording, the checker's closing clause, and then to **hold** the lines until the corrections are applied
(`DR-116` item 2). `Pointer_Lines_DRAFT_2026-11-10.md` was rebuilt by script on those answers: 22 lines, marked HELD. Nothing is
appended to any pass file.

**L-74 · 13:14 · A source changed after this review.** `DR-133` (2026-11-10, raised on another location's review: not used here) made the
Larsemann cluster's shared Nella Fjord port a fourth Australian receiving node: `Ports.md` L129, L188, L202 and L386 were edited in
place. Shirayuki's note and pieces cite `Ports.md` as it read before; the next review of Shirayuki takes the current lines.
