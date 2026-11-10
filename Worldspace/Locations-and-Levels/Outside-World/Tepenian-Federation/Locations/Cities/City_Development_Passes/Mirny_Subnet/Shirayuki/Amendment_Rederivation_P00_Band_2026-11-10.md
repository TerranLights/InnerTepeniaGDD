# Shirayuki: amendment re-derivation P00_Band (the population band), 2026-11-10

**Status: PROPOSED.** This is an append-only amendment, kept beside Shirayuki's pass, that re-derives one conclusion
of the pass: the population band. It is the single merged write of three independent readers (A, B and C), each of
whom re-derived the band from the same admitted lines, passed a mechanical check of their reading, and then
cross-checked the other two. Every conclusion here is PROPOSED for the developer's review. **No pass file is edited**,
and nothing here edits the ruling queue, the census or the rulings log. The round record is the file
`Amendment_Rederivation_P00_Band_2026-11-10b_T8_Rounds.md` beside this one. The readers' own files are kept beside the
pass as dot-files: `.t8_xc_P00_Band_readerA.md`, `.t8_xc_P00_Band_readerB.md`, `.t8_xc_P00_Band_readerC.md` (Round 1)
and `.t8_xc_P00_Band_round3_readerA.md`, `.t8_xc_P00_Band_round3_readerB.md`, `.t8_xc_P00_Band_round3_readerC.md`
(Round 3).

**Short names used below.** `Frame` = `00_Frame.md` (the pass's frame file). `note` =
`Amendment_Notes_2026-11-10_Cross_Check.md`. `01` = the methodology's `01_Frame_Typology_and_Inheritance.md`. `census` =
`Official_Population_Census.md`. `LOG` = `DEVELOPER_RULINGS_LOG.md`. `QUEUE` = `Developer_Ruling_Queue.md`. `verdict` =
`.xc_20261110_item_SRY-C02.md` (the first check's verdict on this item). Full paths are in section 8. Reader point
numbers are cited as the readers wrote them, shortened: `A-14` is reader A's point `P00_Band-A-14`, `B-R3-10` is reader
B's Round 3 point `P00_Band-B-R3-10`, and so on. Every quotation below is copied exactly from the single source line
(or the run of lines) cited after it; wording inside a block marked PROPOSED is amendment text and is not a quotation.
Lines that name another location are never quoted here; what they say is given unquoted, by role, with file and line.

## 1 What this piece re-derives

**The item.** `SRY-C02`, the population band, as listed in section F of the cross-check notes: the pass places are
the declaration's band lines, §2 with its readings, §6 item 2 and §10's first limit, and the input it rests on is
"The band ruling; Census I's distance from the line" (note L304).

**The first check's verdict.** "VERDICT: FLIPS" (verdict L2). Its reasoning: an admitted line of the rulings log places
this city in Band 5 on Census I, and the Census I ruling makes Census I govern for every city (verdict L29–L30); the
pass's ground for Band 4, the band Census II sits in, runs the other way from that ruling (verdict L30); and "The
figures on their own would not move the conclusion." (verdict L28). The verdict lists the affected pass sentences at
verdict L39–L52 and seven points a re-derivation must decide, (a) to (g), at verdict L53–L60. All three readers took
that list as the agenda, not as a finding, and re-derived each point from the source lines.

**The pass places re-derived** (all in `Frame`; pass line numbers are as the pass files stand, "unchanged since
2026-10-20" (note L11)):

| Pass place | Lines | What it holds |
|---|---|---|
| The declaration's band lines | L19–L35 (band lines L28–L34) | Band 4, the census pair, the threshold flag |
| §2 and §2a | L150–L204 | The band table, the two-band sentence, what the pass does pending a ruling, readings A, B and C; the three transitions inside one frame |
| §6, what the pass requested | L286–L298 | Item 1, sub-location decomposition; item 2, a ruling on the band crossing |
| §10, what this frame cannot prove | L360–L377 | The first limit, on the band ruling |

**Where each of the first check's points is answered here.**

| Verdict point (verdict L53–L60) | Answered at |
|---|---|
| (a) the band declaration | P00_Band.11 to P00_Band.18, and the proposed lines after P00_Band.18 |
| (b) readings A, B and C | P00_Band.35; the queue entry's status at P00_Band.89 |
| (c) the Band 5 caution and its count | P00_Band.33, P00_Band.34; open question P00_Band.93 |
| (d) §2a's band row and its count of transitions | P00_Band.36 to P00_Band.38; open question P00_Band.92 |
| (e) §6's sub-location sentence | P00_Band.45, P00_Band.46 |
| (f) §6 item 2 and §10's first limit | P00_Band.48, P00_Band.51, P00_Band.52 |
| (g) the current figures | P00_Band.1 to P00_Band.3; the proposed blocks in section 2 |

## 2 The re-derived conclusions

Everything in this section is PROPOSED. The pass is not edited; proposed text is amendment text for the developer.

### 2.0 The inputs now (shared by all four pass places)

- **P00_Band.1. Census I.** The census row for this city's Census I gives 545,891 humans and 566,709 robots, combined
  1,112,600 (census L505). The same row carries the pass's figure as an earlier value (518,822 humans, 541,660 robots,
  1,060,482) and two later adjustments that replaced it, +12,139 humans / +11,778 robots and +14,930 humans / +13,271
  robots, together +52,118; each is recorded on the row as arithmetic and not a migration (census L505; the line names
  other locations, so it is not quoted). Checks: 545,891 + 566,709 = 1,112,600; 518,822 + 12,139 + 14,930 = 545,891;
  541,660 + 11,778 + 13,271 = 566,709; 1,060,482 + 52,118 = 1,112,600.
- **P00_Band.2. Census II.** The census row for Census II gives 319,190 humans and 372,181 robots, combined 691,371
  (census L653). The pass's figure is the row's earlier value (302,512 humans, 352,980 robots, 655,492); two later
  adjustments, +8,108 / +7,739 and +8,570 / +11,462, together +35,879, are each recorded as arithmetic and not a
  migration (census L653; not quoted, for the same reason). Checks: 319,190 + 372,181 = 691,371; 302,512 + 8,108 +
  8,570 = 319,190; 352,980 + 7,739 + 11,462 = 372,181.
- **P00_Band.3. Distance from the line.** "**11.26% above** (112,600); Census II **30.86% below** (308,629)" (note
  L131). On the pass's own figures (Frame L29–L30) the distances were 6.05% above and 344,508 (34.45%) below
  (computed); the pass wrote 6% (Frame L31) and the queue "when the city is 35% below the line" (QUEUE L572), rounded
  forms of the same figures. Both censuses still lie on the sides of the line the pass names.
- **P00_Band.4. The Census I ruling.** Developer, verbatim: "Everything is assumed with Census I, because that's the
  maximum size per city that each city needs to" (LOG L211) "accommodate." (LOG L212). Its heading: "The population
  figure — CENSUS I, corpus-wide" (LOG L214). Its ground: "The rationale is a DESIGN rationale, not a frame
  rationale:" (LOG L216); Census I is "the maximum size each city must" (LOG L216) "be built to accommodate." (LOG
  L217); "A city designed to its smaller figure cannot hold its larger one; the reverse is" (LOG L217) "merely slack."
  (LOG L218). This piece rests the design ground on LOG L216–L218 alone (see section 4, the split on the lines that
  follow a line about another city, and question P00_Band.96).
- **P00_Band.5. The ruling applied to this city.** The rulings log's row at LOG L1713, which is marked as a note and
  not a new ruling, records that the Census I ruling already makes Census I the governing figure for a city's band,
  so this city, at 1,112,600, is Band 5 (described unquoted: the row also names another city, whose clause is not
  used). The cross-check notes agree: "Shirayuki's Census I, 1,112,600, is Band 5" (note L51). The band does not
  depend on that row's being marked as a note: without it, the ruling's own lines still make Census I govern for every
  city (LOG L211, L214), and Census I is 11.26% above the line (note L131) (B-145; the first check's doubt at verdict
  L75 reaches the same).
- **P00_Band.6. The deferral, and what a pass does meanwhile.** The ruling "states two obligations that this ruling
  suspends:" (LOG L230). The obligation at the fifty-thousand threshold, "a location **must** be decomposed into
  sub-locations, each of which gets its own pass" (LOG L234), and the obligation at the million threshold, under which
  "the unit of analysis changes to spread and modes" (LOG L235), are each marked deferred (LOG L234, L235), until all
  38 cities have been through the ULM, CST and RWBEM (LOG L237). The reason: "you cannot write a distribution before
  you know what is being" (LOG L239) "distributed." (LOG L240); decomposing early "would produce 38 sets of invented"
  (LOG L241) "internal structure, each one a fact the later passes would be forced to honor." (LOG L242). "Recorded
  as an override, not as a silent divergence." (LOG L244). The obligations are "suspended, not canceled" and "they
  resume when the gate opens." (LOG L246). Meanwhile a pass writes "base-level fundamental facts" (LOG L248), "what is
  true of the place, its generators, its constraints, its function, its composition" (LOG L249), "declaring Band 5"
  (LOG L249) "where the figure is Band 5, without performing the Band 5 distributional analysis." (LOG L250). "And it
  must say so" (LOG L250), "so a later reader knows the analysis was deferred by ruling rather than missed." (LOG
  L251).
- **P00_Band.7. The bands and thresholds.** The scale band is "The single most consequential declaration" (01 L164).
  A pass declares two numbers, the "population band" and the "extent band" (01 L167); when "they diverge, the
  divergence is characterizing" and "should be written as a finding" (01 L168). Band 4 is "~50,000–1M", with the unit
  "Institutions **plus mandatory internal differentiation**" and the district methodology's assumptions marked "Hold,
  but incomplete" (01 L180). Band 5 is "~1M–50M", with the unit "**Distributions**, not points" and those assumptions
  marked "Mostly fail" (01 L181). "Each threshold is a point where a question that" (01 L186) "was answerable stops
  being answerable in the same form." (01 L187). The lower threshold: "Above roughly fifty thousand," (01 L211);
  "Above this threshold a location **must** be decomposed" (01 L212). The upper: "the location no longer has a
  culture; it has a statistical shape." (01 L218); the later unit of analysis is "what is the spread, where are its
  modes, and what is genuinely" (01 L219) "common to all of it." (01 L220); "A Band 5 pass that reads like a Band 3
  pass has committed the scale error named in" (01 L220), namely "asserting of a large population what is true of a
  small one." (01 L221).
- **P00_Band.8. The queue entry on the band crossing.** Its queue mark is "open" (note L285). "Whether the developer
  treats `DRQ-10` and `DRQ-13` as closed by these" (note L291) "rulings is a question (`DEC-441`)." (note L292); "The
  queue file is not edited by this note." (note L291). The queue text still carries the pass's figures: "sits at
  `1,060,482` at Census I — `6%` above the `~1M` Band 4/5 line" (QUEUE L554) and "when the city is 35% below the line"
  (QUEUE L572). It names the case as "it is a band crossing INSIDE one frame, and the taxonomy has no entry for it."
  (QUEUE L566). It records a standing convention, "all process-derived figures use Census I." (QUEUE L567), and "The
  pass proceeds on A and says so." (QUEUE L575), and says the band will bind "Phase 4 (Ordinary Life), Phase 9
  (Populations) and Gate 11" (QUEUE L576).
- **P00_Band.9. The cross-check's own frame, and the first check.** "No pass file is edited; each mismatch is
  recorded in an amendment note." (note L26); "only items that change are re-derived, using the rulings as they stand"
  (note L36). The section F row gives the input's current value as Band 5 on Census I, 11.26% above the line, with
  the distributional analysis deferred by ruling (note L304). The first check found "VERDICT: FLIPS" (verdict L2) and
  that "The figures on their own would not move the conclusion." (verdict L28).
- **P00_Band.10. No datasheet place.** No Pre-Trip or datasheet file exists for this city, the tools that build them
  do not build it, and every reading list of the cross-check is built by hand (note L29–L33, described unquoted
  because L32 names another location). No datasheet line exists to receive a pointer from this piece.

### 2.1 The declaration's band lines (Frame L19–L35; the band lines are L28–L34)

**As the pass states it.** "4 — URBAN, at the top of the band" (Frame L28), listing Census II first, 655,492
(302,512 H / 352,980 R), then Census I, 1,060,482 (518,822 H / 541,660 R) (Frame L29–L30); "THE FRAME CROSSES THE
4→5 THRESHOLD. Census I sits 6% ABOVE the" (Frame L31) "~1M line; Census II sits well inside Band 4." (Frame L32);
"FLAGGED — DRQ-10, open. Written at Band 4, with Band 5's" (Frame L33) "obligation treated as live for the
pre-orbital half." (Frame L34).

**The inputs it now rests on.** P00_Band.1 to P00_Band.8.

**The PROPOSED conclusion.**

- **P00_Band.11. The band is 5, Regional, on Census I, set by ruling and not provisional.** The figure that sets a
  city's band is Census I, "corpus-wide" (LOG L214), because it is the size the city must be built to hold (LOG
  L211–L212, L216–L218). This city's Census I is 1,112,600 (census L505), inside Band 5's range, "~1M–50M" (01 L181),
  and the ruling as applied to this city places it in Band 5 (LOG L1713). The band no longer waits on a ruling: the
  ruling sets it, not this pass.
- **P00_Band.12. The count that decides the band is the combined count of humans and robots.** 1,112,600 is the
  row's combined total (census L505), it is the figure the rulings log applies (LOG L1713), and the pass's own table
  banded the combined row (Frame L159–L160). A Band 4 reading on humans alone (545,891) is killed (P00_Band.55).
- **P00_Band.13. Its place in the band.** 112,600 above the line that opens Band 5 (note L131; 01 L181), near the
  band's floor. "at the top of the band" (Frame L28) described a place in Band 4 and does not carry over.
- **P00_Band.14. The flip comes from the ruling, not from the new figures.** The pass's own Census I, 1,060,482, was
  already above the line (Frame L31, L160), and the first check found that the figures alone would not move the
  conclusion (verdict L28). The changes since the pass are the two later adjustments on each census row, each recorded
  as arithmetic and not a migration (census L505, L653; P00_Band.1, P00_Band.2). So no in-world event is implied by the
  change of band or of figure, and none is to be narrated. (The sentence on those rows saying that nobody left the
  city belongs to an earlier adjustment, the one that produced the pass's own figures; see P00_Band.79.)
- **P00_Band.15. The declaration carries the deferral in its own lines.** A pass declares Band 5 "without performing
  the Band 5 distributional analysis." (LOG L250), and "And it must say so" (LOG L250), "so a later reader knows the
  analysis was deferred by ruling rather than missed." (LOG L251). The sub-location decomposition is deferred on the
  same terms (LOG L234, L237). Both are suspended, not canceled (LOG L246). The pass's lines say something else: the
  band is flagged open and an obligation is "treated as live" (Frame L34).
- **P00_Band.16. The declaration names the ruling and leaves the queue entry's status open.** The queue mark is still
  "open" (note L285), and whether these rulings close it is the developer's question (note L291–L292; question
  P00_Band.89). The declaration does not call the queue entry closed.
- **P00_Band.17. Census I is listed first, as the governing figure.** The pass listed Census II first (Frame
  L29–L30).
- **P00_Band.18. Census II is stated as a figure with its distance below the line, not as a second band.** 691,371,
  30.86% below the line (census L653; note L131). Whether any band wording stands beside it is the developer's
  question (P00_Band.91); the merged text below gives none, as the reading that claims least.

  Proposed declaration lines (merged amendment text, PROPOSED; the pass itself is not edited):

  ```
  **Population band:** 5 — REGIONAL, near the floor of the band, set by Census I            [PROPOSED]
                       Census I   (Pre-Orbital)   1,112,600   (545,891 H / 566,709 R)   the governing figure
                       Census II  (Orbital Era)     691,371   (319,190 H / 372,181 R)
                       Census I sits 112,600 (11.26%) above the ~1M line; Census II sits
                       308,629 (30.86%) below it. The band is set by Census I, the size the
                       city must be built to hold, and holds for the whole frame; it does not
                       change at ~2688 [Census I ruling: LOG L211, L214, L216-L218; applied to
                       this city at LOG L1713].
                       ⏸️ DEFERRED BY RULING, NOT MISSED: the Band 5 distributional analysis and
                       the sub-location decomposition wait until all 38 cities have been through
                       the ULM, CST and RWBEM; suspended, not canceled [LOG L234-L246]. In the
                       meantime the ruling asks a pass to write base-level facts, what is true of
                       the place [LOG L248-L251].
                       The queue entry on the band crossing is still marked open; whether these
                       rulings close it is a developer question [note L285, L291-L292].
  ```

- **P00_Band.19. Second and third order.** The scale band is "The single most consequential declaration" (01 L164),
  so every later phase that reads the band now reads Band 5 with its analysis deferred, not Band 4. Because the band
  is a design figure and not an era's snapshot (LOG L216), it does not move with the Act: it holds in Act 1 and Act 2
  alike, and no cultural claim in these lines turns on the Act.

**What survives unchanged.**

- **P00_Band.20.** The two figures' sides of the line, Census I above and Census II below (Frame L31–L32; note
  L131). The labels Pre-Orbital and Orbital Era on the two censuses (Frame L29–L30). The practice of declaring both
  figures with their human and robot split (Frame L29–L30), with new numbers. The words "THE FRAME CROSSES THE 4→5
  THRESHOLD" (Frame L31) survive only as a statement about the two figures; as a statement about the band they do not,
  because the band is set once. The Type and Location lines (Frame L22–L26) are not touched by this piece.

**Downstream pass places (pointer or docket note only; no edit).**

- **P00_Band.21.** Inside the frame: §2 (Frame L153–L180), §2a's census row and its count (Frame L190, L200), §6
  items 1 and 2 (Frame L288, L292) and §10's first limit (Frame L364), each re-derived below. Outside the admitted
  lines (named only): the Phase 4 (Ordinary Life) and Phase 9 (Populations) material and Gate 11, which the queue says
  the band binds (QUEUE L576; docket notes at P00_Band.41); the pass's process record, `09.5_Log.md` (Frame L376);
  the next piece, `01_Inherited.md` (Frame L375), if it carries the band. Not pass places, but carrying the pass's
  figures: the queue text (QUEUE L554, L572), a pointer only, since the note does not edit the queue (note L291); and
  the note's queue row and section F row (note L285, L304). The extent band: no admitted line of the declaration
  (Frame L19–L35) shows the pass's extent band, so whether the move to Band 5 opens a divergence between the two bands
  is a lookup for the item that owns the extent row (question P00_Band.95). No datasheet exists to receive a pointer
  (P00_Band.10).

### 2.2 §2 and §2a, the population band and the three transitions (Frame L150–L204)

**As the pass states it.** The heading: "the frame crosses a threshold, and this needs a ruling" (Frame L153). The
table gives Census I combined 1,060,482 and Census II combined 655,492 (Frame L159), banded 5 — Regional, "6% over the
~1M line", and 4 — Urban (Frame L160). "So this city is Band 5" (Frame L162) "for the pre-orbital portion of its own
declared frame and Band 4 for the rest." (Frame L163). Why it is not a rounding question: "That is a different kind
of writing, not a bigger version of the same writing." (Frame L168). Pending the ruling, the pass writes at Band 4,
"the band Census II sits in cleanly, and whose obligations are a superset of what Band 5" (Frame L172) "needs at this
margin." (Frame L173), and "KEEPS BAND 5's OBLIGATION LIVE for the pre-orbital half:" (Frame L173), no claim of the
form "people here do X" (Frame L174) "that would be false of two hundred thousand of them." (Frame L174). Readings: A,
the "provisional choice", "Census I's excess treated as margin." (Frame L178); B, "Written as a distribution." with
the caveat "arguably wrong for the orbital half" (Frame L179); C, "Declared crossing, two states", in which "the
crossing becomes a finding rather than an awkwardness" (Frame L180). §2a is headed "THREE STRUCTURAL TRANSITIONS SIT
INSIDE ONE FRAME" (Frame L182) and lists "| **Band 5 → Band 4** *(Census I → II)* | **~2688** | **scale** |" (Frame
L190) beside the Act 1 → Act 2 row at about 2688 (Frame L189) and the civic row, in the ~2780s, in which the city
becomes a constituent of a unified three-city whole (Frame L191; both rows described unquoted because each names a
place or structure). "THE FRAME STANDS AS ONE" (Frame L193); "But rule 1 binds: the mixture may not be UNDECLARED."
(Frame L197); "And the three transitions are not a problem — they are the OWN-ERAS INSTRUMENT." (Frame L198); "Two of
the three cluster at `~2688`; the third follows." (Frame L200).

**The inputs it now rests on.** P00_Band.1 to P00_Band.8, chiefly the Census I ruling (P00_Band.4, P00_Band.5), the
deferral (P00_Band.6) and the thresholds (P00_Band.7).

**The PROPOSED conclusion: §2.**

- **P00_Band.22. The heading.** The band no longer waits on a ruling: the Census I ruling sets it (LOG L214), and the
  rulings log applies it to this city (LOG L1713). What is still open is the queue entry's status (note L285,
  L291–L292).
- **P00_Band.23. The table.** It takes the current figures (census L505, L653) and the current distances (note
  L131); Census I sets the one band for the city; Census II is a figure, not a second band (P00_Band.18; its cell's
  wording is question P00_Band.91).
- **P00_Band.24. The two-band sentence (Frame L162–L163) becomes one band and two figures.** The census boundary
  still sits at about 2688 (Frame L162). The population figure falls across it from 1,112,600 to 691,371, a fall of
  421,229, which is 37.86% of Census I (computed from census L505, L653; on the pass's own figures the fall was
  404,990, 38.19%). The band does not change, because it is set once, by the size the city must be built to hold (LOG
  L211–L212, L216–L217).

  Proposed §2 heading, table and sentence (merged amendment text, PROPOSED; the pass itself is not edited):

  ```
  2 · POPULATION BAND — Band 5 on Census I, set by ruling; the census pair lies across the ~1M line;
      the Band 5 analysis is deferred by ruling                                              [PROPOSED]

  |                      | Census I (Pre-Orbital), sets the band | Census II (Orbital)                            |
  |----------------------|---------------------------------------|------------------------------------------------|
  | Humans               | 545,891                               | 319,190                                        |
  | Robots               | 566,709                               | 372,181                                        |
  | Combined             | 1,112,600                             | 691,371                                        |
  | Against the ~1M line | 11.26% above (112,600)                | 30.86% below (308,629)                         |
  | Band                 | 5 — Regional, for the whole frame     | not a second band; the band is set by Census I |

  The Second Interwar runs 2564–2812; the Census I→II boundary sits at ~2688. This city is Band 5 for its
  whole declared frame. Its population figure falls at ~2688 from 1,112,600 to 691,371; that is a change of
  figure inside one band, not a change of band.
  ```

- **P00_Band.25. The gap the queue names does not arise for this city's band.** The queue framed the case as "it is
  a band crossing INSIDE one frame, and the taxonomy has no entry for it." (QUEUE L566). With the band set on Census I
  "corpus-wide" (LOG L214), this city's band does not cross inside its frame. Whether the queue entry is therefore
  closed is not decided here (note L291–L292; question P00_Band.89).
- **P00_Band.26. Physical expression: the design figure and the Orbital-era census.** The ruling's ground is
  physical: Census I is "the maximum size each city must" (LOG L216) "be built to accommodate." (LOG L217). In the
  Orbital era the census records 691,371 (census L653): 421,229 fewer people than the design figure, 37.86% of it;
  Census II is 62.14% of Census I (computed). The ruling's own word for a city holding less than it was designed for
  is "merely slack." (LOG L218). The footprint the note computes, "**111.26 to 158.94 km²**" (note L133), is Census
  I's: 1,112,600 ÷ 10,000 = 111.26 and 1,112,600 ÷ 7,000 = 158.94 (computed); it belongs to another item and is cited
  only as resting on the same figure. No admitted line dates when the built city reaches the design size within a
  frame that opens in 2564 (Frame L162), so this conclusion states the slack against the declared design figure and
  makes no claim about the physical build at any date (the split is in section 4).
- **P00_Band.27. The slack is a scale fact, not a cultural one.** It lies on the Orbital side of about 2688, where the
  pass also places its Act boundary (Frame L162; the Act row at Frame L189). Nothing cultural is drawn from it here.
- **P00_Band.28. What the slack is on the ground, and where it sits, is not stated.** No admitted line says whether
  the unused capacity stands empty, idle or put to other use, where it sits (on rock or on ice), or who carries its
  upkeep. Placing it now would be the invented "internal structure" the ruling defers (LOG L241–L242), so it waits
  for the decomposition. It is declared as a limit in §10 (P00_Band.52); how the frame states the slack is question
  P00_Band.94.
- **P00_Band.29. No admitted line gives a cause for the fall between the two censuses.** The census rows' notes that
  the changes were arithmetic, or an authoring adjustment, and not a migration (census L505, L653) concern the changes
  made to each figure, not the gap between Census I and Census II; they are evidence neither way. No cause is
  supplied.
- **P00_Band.30. The not-a-rounding-question reasoning survives, on a wider margin.** Census I is 11.26% above the line (note
  L131) where the pass had 6% (Frame L31), the city's own earlier state. The pass's quotation of the threshold (Frame
  L167–L168) matches the methodology (01 L218). What changes: the "different kind of writing" (Frame L168) is now
  suspended by ruling (LOG L235, L246), not avoided by the pass's choice; it describes the writing the deferred
  analysis will owe.
- **P00_Band.31. What the pass does under the ruling.** In place of "the band Census II sits in cleanly" (Frame
  L172): the pass declares Band 5, performs neither the distributional analysis nor the decomposition (LOG L234–L235),
  and says so (LOG L250–L251). The ruling asks a pass, in the meantime, to write "base-level fundamental facts" (LOG
  L248), "what is true of the place, its generators, its constraints, its function, its composition" (LOG L249). The
  amendment states this as the ruling's instruction. It does not state that the pass body already meets it: the
  ordinary-life and populations phases and the scale gate are outside every reader's admitted lines, so whether they
  meet it is a docket check (P00_Band.41).
- **P00_Band.32. The superset ground no longer carries.** The pass wrote at Band 4 because its obligations "are a
  superset of what Band 5" (Frame L172) "needs at this margin." (Frame L173). Both obligations it compares, the
  decomposition that marks Band 4 and the distribution that marks Band 5, are now deferred (LOG L234–L235), so nothing
  is left between them to be a superset of. And the ruling's direction is the larger figure, "A city designed to its
  smaller figure cannot hold its larger one" (LOG L217), where the pass chose the band the smaller figure sits in
  (Frame L172).
- **P00_Band.33. The caution survives as a guard, over the whole frame and both Acts, not as a live Band 5
  obligation.**
  1. The obligation the pass kept "LIVE" (Frame L173) is the one at the million threshold, now deferred (LOG L235)
     and "suspended, not canceled" (LOG L246). It cannot stand as a live obligation.
  2. What the pass wrote under it is narrower, a negative guard: no claim of the form "people here do X" (Frame L174)
     that is false of a large part of the city.
  3. That guard is the scale error the methodology names, "asserting of a large population what is true of a small
     one." (01 L221). It also follows from the ruling's level for the meantime, "what is true of the place" (LOG
     L249): a claim false of a large part of the people is not true of the place.
  4. The ruling suspends exactly two obligations (LOG L230, L234–L235). In the admitted lines it names neither the
     scale error nor its gate, so whether the guard is suspended with them is not stated in words; the guard's survival
     rests on the reasoning in steps 2 and 3 and is offered as such.
  5. Reach: the pass's "pre-orbital half" limit (Frame L173) rested on a band split by census. The band is no longer
     split, since "Everything is assumed with Census I" (LOG L211), so the guard covers the whole frame: Act 1 and Act
     2, pre-orbital and Orbital.

  Its count and its wording are question P00_Band.93. Recommended wording (amendment text, PROPOSED, provisional on
  that question):

  ```
  WRITES BASE-LEVEL FACTS, across the whole frame and both Acts [LOG L248-L249]: no claim of the form
  "people here do X" unless it is true of the place, and nothing asserted of the city's people as a whole
  that is true only of part of them [01 L220-L221]. This is a guard against the scale error, not the
  suspended Band 5 obligation; the Band 5 analysis itself is deferred by ruling [LOG L235-L237].
  ```

- **P00_Band.34. The count "two hundred thousand" has no admitted derivation.** No admitted line says how the figure
  in "that would be false of two hundred thousand of them." (Frame L174) was reached. It is 17.98% of the current
  Census I and was 18.86% of the pass's (computed). It is not recomputed or rescaled here (P00_Band.59).
- **P00_Band.35. Readings A, B and C.** The readings table stays in the pass as the record of the question as it
  stood before the ruling; it governs nothing, and the amendment states each reading's standing beneath it:
  - **A, Band 4 throughout: superseded.** The rulings log places the city in Band 5 (LOG L1713), and A's ground,
    "Census I's excess treated as margin." (Frame L178), runs against the ruling's design ground (LOG L216–L218).
  - **B, Band 5 throughout: its band stands, its manner is deferred.** Its band is the ruled band (LOG L211, L1713);
    its manner, "Written as a distribution." (Frame L179), is the analysis the ruling defers (LOG L235). Its caveat,
    "arguably wrong for the orbital half" (Frame L179), is answered as to the band by the design ground (LOG L216);
    as to the writing, it belongs to the deferred analysis (LOG L235).
  - **C, "Declared crossing, two states" (Frame L180): its two band states fall.** One band is set for the whole
    frame (LOG L211, L214, L1713). What C was for, the city's own eras as an axis, survives on the stated population
    figures (P00_Band.40); how far Census II may be used for that is question P00_Band.90.

**The PROPOSED conclusion: §2a.**

- **P00_Band.36. The census row is no longer a band transition; it stays declared, as a change of population
  figure.** The band is 5 on both sides of about 2688 (LOG L211, L1713), so "Band 5 → Band 4" (Frame L190) does not
  hold. The population figure still changes at that date (census L505, L653; Frame L162), and the frame's own rule is
  "But rule 1 binds: the mixture may not be UNDECLARED." (Frame L197), so the row stays. "Two of the three cluster at
  `~2688`; the third follows." (Frame L200) survives as a statement about three dated changes. How the heading names
  and counts them is question P00_Band.92.

  Proposed row (amendment text, PROPOSED):

  ```
  | Census I → Census II (1,112,600 → 691,371; the band stays 5, set by Census I) | ~2688 | scale (the population figure, not the band) |
  ```

- **P00_Band.37. The kind of writing the band calls for does not change at about 2688.** The band is set once, on
  Census I, "corpus-wide" (LOG L214), with "Everything is assumed with Census I" (LOG L211); nothing at the census
  boundary changes the form of a question in the sense of 01 L186–L187. Whether the deferred analysis, when the gate
  opens, writes the two eras differently stays with the deferral (LOG L246) and with question P00_Band.90.
- **P00_Band.38. The frame still stands as one, and its case is simpler.** Its test turned on the Act boundary being
  "a consolidation, not a line crossed" (Frame L194) and on the war being the frame's terminus (Frame L196); the band
  row was not part of that test. One band is now declared for the whole frame, so this piece removes a band mixture
  rather than adding a straddle. Nothing in the admitted lines says the frame fails.
- **P00_Band.39. The band no longer adds a reason to split the pre-orbital half off (reader C's inference, not a
  statement of the pass).** The question "Whether a dedicated ACT-1 pass is separately warranted is a developer
  question — flagged, not assumed." (Frame L201) survives unchanged. The pass does not give the band as a reason for
  that question in any admitted line; the point is C's inference from the band's now being the same on both sides.
- **P00_Band.40. The own-eras instrument survives, on the two remaining transitions and the stated census pair.** It
  loses the band as one of its axes (Frame L198–L200). The pair, 1,112,600 before about 2688 and 691,371 after, is
  stated canon (census L505, L653); no process-derived figure rests on Census II (QUEUE L567; LOG L211). Whether
  Census II may be used in an own-eras description is question P00_Band.90.

**Second and third order, for §2 and §2a.**

- **P00_Band.41. Docket notes for the places the queue says the band binds** (Phase 4 (Ordinary Life), Phase 9
  (Populations) and Gate 11, QUEUE L576; their files and lines are not in any reader's admitted lines). Checks, not
  edits:
  1. Check Orbital-era sentences, and any claim of the form "people here do X" (Frame L174), against the guard,
     which now reaches the whole frame rather than the pre-orbital half (P00_Band.33).
  2. Check that process-derived figures use Census I, as the ruling (LOG L211) and the queue's standing convention
     (QUEUE L567) require.
  3. Test the scale error, which the methodology places in that gate (01 L220–L221), against Band 5, not Band 4.
  4. Check any sentence written to Band 4's unit (01 L180), or that leaned on the district methodology's assumptions
     because at Band 4 they "Hold, but incomplete" (01 L180), where Band 5's row reads "Mostly fail" (01 L181).
  5. Check whether the pass body writes at the level the ruling asks for in the meantime (LOG L248–L249; P00_Band.31).
- **P00_Band.42. Why the guard matters now (reader A's inference, not the ruling's words).** The ruling names the
  danger of early decomposition as "a fact the later passes would be forced to honor" (LOG L242). By the same
  mechanism, a universal claim about the city's people written now would be inherited by the later analysis as a
  fact. When the gate opens the city is owed the decomposition and the distribution, "what is the spread, where are
  its modes, and what is genuinely" (01 L219) "common to all of it." (01 L220); the base-level facts written now are
  what that later distribution will be a distribution of.

**What survives unchanged.**

- **P00_Band.43.** The Census I→II boundary at about 2688 (Frame L162). The not-a-rounding-question reasoning and its
  quotation (Frame L165–L168). The pass's choice to keep a caution against universal claims, now wider (P00_Band.33).
  The readings table as the record of the question (Frame L176–L180). The Act row and the civic row of §2a (Frame
  L189, L191). The frame-as-one test (Frame L193–L197). The question at Frame L201.

**Downstream pass places (pointer or docket note only; no edit).**

- **P00_Band.44.** The declaration (Frame L28–L34), §6 items 1 and 2 (Frame L288, L292) and §10's first limit (Frame
  L364) point to §2. Frame L190 feeds L200 (L200 survives; a pointer only). The queue's options table (QUEUE
  L569–L573) repeats the three readings on the pass's figures, and the queue's question (QUEUE L554) and option B
  (QUEUE L572) carry them: pointers only, since the note does not edit the queue (note L291). Phase 4, Phase 9 and
  Gate 11 (QUEUE L576): the docket notes at P00_Band.41. Any later file that cites the three transitions or the
  own-eras axis (not in any admitted line). The pass's process record, `09.5_Log.md` (Frame L376), whose content is
  not admitted.

### 2.3 §6, what the pass requested (Frame L286–L298)

**As the pass states it.** The section is "emitted rather than invented" (Frame L286). Item 1: "SUB-LOCATION
DECOMPOSITION." and "Band 4 makes it mandatory." (Frame L288); "No sub-locations exist in admissible" (Frame L288)
"canon." (Frame L289); the spec's vision-session notes are not read as an input (Frame L289–L290); "The hole has a
known SHAPE: the" (Frame L290) "internal axis is ROCK vs ICE, and it is physical rather than chosen." (Frame L291).
Item 2: "A RULING ON THE BAND CROSSING" (Frame L292), pointing to §2's readings A, B and C. Item 3, the
rock-allocation mechanism (Frame L293–L296), belongs to other items.

**The inputs it now rests on.** The lower threshold (P00_Band.7: 01 L211–L212); its deferral and the reason for
waiting (P00_Band.6: LOG L234, L237, L241–L242, L246); the band as applied to this city (P00_Band.5); the queue mark
and the closure question (P00_Band.8).

**The PROPOSED conclusion.**

- **P00_Band.45. Item 1: the obligation stands on the fifty-thousand threshold, not on Band 4, and it is deferred.**
  1. The decomposition obligation comes from the lower threshold: "Above roughly fifty thousand," (01 L211); "Above
     this threshold a location **must** be decomposed" (01 L212). It is tied to that line, not to Band 4.
  2. Census I, the governing figure, is 1,112,600 (census L505), above that threshold at Band 5 as it was at Band 4.
     Census II, 691,371 (census L653), is above it too; that is support only, since Census I governs (LOG L211).
  3. The ruling defers the obligation (LOG L234) until all 38 cities have been through the three methods (LOG L237),
     suspended, not canceled (LOG L246), because decomposing early "would produce 38 sets of invented" (LOG L241)
     "internal structure, each one a fact the later passes would be forced to honor." (LOG L242). So the obligation
     changes from mandatory now to deferred by ruling; only the stated ground (Band 4) and the timing change.
- **P00_Band.46. What survives inside item 1.** No sub-locations exist in admissible canon (Frame L288–L289), and no
  admitted line contradicts it. The spec's vision-session notes stay out of the inputs (Frame L289–L290). The hole's
  known shape, rock against ice, physical rather than chosen (Frame L290–L291), is a constraint of the site, the kind
  of base-level fact a pass writes meanwhile, which includes "its constraints" (LOG L249). Naming a physical axis does
  not decompose the city into sub-locations or invent internal structure (LOG L241–L242), so it is kept, recorded for
  when the gate opens. How much of the site is rock, and the axis's footing, belong to the rock items, not to this
  piece.

  Proposed item 1 (amendment text, PROPOSED):

  ```
  1. SUB-LOCATION DECOMPOSITION. Required above roughly fifty thousand, which Census I's 1,112,600 exceeds
     (Census II's 691,371 does too) [01 §2.2, threshold 3→4]. DEFERRED BY RULING until all 38 cities have
     been through the ULM, CST and RWBEM; suspended, not canceled [LOG L234-L246]. Not performed here;
     deferred, not missed. No sub-locations exist in admissible canon, and none is invented here. The
     spec's vision-session notes are not read as an input. The hole's known shape, rock against ice, is
     physical rather than chosen, and is recorded for when the gate opens.
  ```

- **P00_Band.47. Second and third order.** The REQUESTED list now carries two items deferred by ruling, the
  decomposition and the distributional analysis, so a later reader finds them there when the gate opens (LOG L246,
  L251). When it opens, the decomposition and the distribution resume together on Census I's figure (LOG L211,
  L246); the spread will then be a spread over a city whose internal axis is physical (Frame L291), and the Orbital-era
  slack (P00_Band.26) sits somewhere on that axis. Where it sits is the decomposition's to find, not this pass's.
- **P00_Band.48. Item 2: the band is answered by ruling; the queue entry's status is with the developer.** The band
  is set by the Census I ruling (LOG L214) as applied to this city (LOG L1713), so nothing about which band remains
  to request. The queue mark is still "open" (note L285), and whether these rulings close it is the developer's
  question (note L291–L292; question P00_Band.89). The readings item 2 names are retired as in P00_Band.35. Whether
  item 2 should also request, for when the gate opens, how the two census states are to be written is part of question
  P00_Band.89.

  Proposed item 2 (amendment text, PROPOSED):

  ```
  2. THE BAND: answered by ruling, Band 5 on Census I [LOG L214; LOG L1713]. The Band 5 analysis is deferred
     by ruling [LOG L234-L246]. Whether the queue entry on the band crossing is closed is with the developer
     [note L285, L291-L292].
  ```

- **P00_Band.49. Item 3 is untouched, and the rock line it quotes is not read as a fact about this city.** The line
  "the 10% on rock is the only ground that never has to be rebuilt" (Frame L295) is the pass's quotation, inside its
  rock-allocation item (Frame L293–L296), of the extent file's general statement about a city "in a `~90%`-ice"
  (Frame L294) setting. Whether it describes this city belongs to the rock items: the note records "Shirayuki is
  rock-founded" (note L56) and gives the city's rock share of its footprint as "rock **8.41% to 12.01%**" (note
  L136). Nothing in this piece rests on that line.

**What survives unchanged.** Item 1 as a request, and the section's stance, "emitted rather than invented" (Frame
L286); the absence of sub-locations in admissible canon; the refusal to read the vision-session notes as input; the
rock-against-ice shape as a physical fact (all in P00_Band.46); item 3 (P00_Band.49).

**Downstream pass places (pointer or docket note only; no edit).**

- **P00_Band.50.** The section F row names only L292 from §6 (note L304); this piece adds L288, because its stated
  ground is Band 4 (the first check did the same, verdict L50, L77). §10's limits on the band and on the rock
  assumption (Frame L364–L365), which point to the same queue entries. The queue entry itself (QUEUE L551–L577). Any
  later phase that refers to sub-locations (not in any admitted line).

### 2.4 §10, what this frame cannot prove (Frame L360–L377)

**As the pass states it.** The section's premise: "a run whose limits are undeclared will be over-read." (Frame
L362). The first limit: "It cannot prove the band ruling." and "§2 is provisional." (Frame L364).

**The inputs it now rests on.** The ruling that sets the band (P00_Band.4, P00_Band.5); the deferral and the duty to
say so (P00_Band.6); the closure question (P00_Band.8); the slack the ruling's ground implies (P00_Band.26 to
P00_Band.28).

**The PROPOSED conclusion.**

- **P00_Band.51. The first limit becomes the declared deferral.** The band is no longer this frame's to prove: the
  ruling sets it (LOG L214, L1713). The limit the frame now has is the one the ruling makes it declare, "And it must
  say so" (LOG L250), "so a later reader knows the analysis was deferred by ruling rather than missed." (LOG L251).
  That is the discipline of the section's own premise (Frame L362), so the deferral belongs here as well as in the
  declaration; it also matches the ruling's own "Recorded as an override, not as a silent divergence." (LOG L244).
  Second order: a reader who meets Band 5 in the declaration and finds no distribution in the pass is told why here;
  without the line, the absence reads as a miss, which is the over-reading the premise warns against.
- **P00_Band.52. Two limits are added.** The frame cannot say whether the queue entry on the band crossing is closed
  (note L285, L291–L292). And it cannot say what the Orbital-era slack between the design figure and Census II
  (421,229; P00_Band.26) is on the ground, or where it sits: no admitted line describes it (P00_Band.28), and placing
  it would be the internal structure the ruling defers (LOG L241–L242).

  Proposed limits, in place of Frame L364 (amendment text, PROPOSED):

  ```
  - ⛔ It does not perform the Band 5 distributional analysis or the sub-location decomposition. Both are
    deferred by ruling until all 38 cities have been through the ULM, CST and RWBEM; suspended, not
    canceled [LOG L234-L246]; deferred, not missed [LOG L250-L251]. The band itself, 5 on Census I, is
    set by ruling [LOG L214; LOG L1713] and is not provisional.
  - ⛔ It cannot say whether the queue entry on the band crossing is closed [note L285, L291-L292].
  - ⛔ It cannot say what the Orbital-era slack between the design figure and Census II (421,229) is on
    the ground, or where it sits: no admitted line describes it, and placing it is internal structure
    the ruling defers [LOG L241-L242].
  ```

**What survives unchanged.**

- **P00_Band.53.** The section's premise (Frame L362). The limits that follow (Frame L365–L371), which this piece
  does not test. One of them, the per-city rock apportionment (Frame L366–L367), rests on a population share that has
  moved with the census; the note now gives "Shirayuki's part of the ~40 km² rock" as 13.36 km² on the Census I share
  (note L135). That belongs to the rock items.

**Downstream pass places (pointer or docket note only; no edit).**

- **P00_Band.54.** None beyond the pass's own §2 and §6, to which this limit points, the queue entry (QUEUE L551),
  the note's section F row (note L304), and the pass's process record, `09.5_Log.md` (Frame L376), whose content is
  not admitted.

## 3 Found by / confirmed by

One row per finding: every numbered point in sections 2, 5 and 6, except the two corrections made by the merge itself
(P00_Band.87, P00_Band.88), which are not findings. **Found by** gives the Round 1 point (or, where the finding first
appears in Round 3, the Round 3 point). **Confirmed by** gives independent finds by the other readers or the Round 3
point that confirmed, narrowed or corrected it. All six Round 3 verdicts on the other readers were CONSISTENT
(`A-R3-4`, `A-R3-9`, `B-R3-9`, `B-R3-26`, `C-R3-8`, `C-R3-23`).

| Point | Finding | Found by | Confirmed by | Disposition |
|---|---|---|---|---|
| P00_Band.1 | Census I and its earlier value | A (`A-1`), B (`B-101`), C (`C-201`) | all three; adjustment totals `B-R3-1`, `C-R3-1`, `C-R3-37` | written (union) |
| P00_Band.2 | Census II and its earlier value | A (`A-2`), B (`B-102`), C (`C-202`) | all three; `B-R3-1`, `C-R3-37` | written (union) |
| P00_Band.3 | Distance from the line; the pass-era distances | A (`A-3`), B (`B-103`), C (`C-204`, current figures) | `A-R3-1`, `C-R3-37` | written (union) |
| P00_Band.4 | The Census I ruling and its design ground, resting on LOG L216–L218 | A (`A-4`), B (`B-104`), C (`C-205`) | all three; footing narrowed `B-R3-11` | written (conservative) |
| P00_Band.5 | The ruling applied to this city; not weakened by the row's marking | A (`A-5`), B (`B-105`, `B-145`), C (`C-206`) | all three; verdict L75 | written (union) |
| P00_Band.6 | The deferral; what a pass does meanwhile | A (`A-6`), B (`B-106`), C (`C-209`, `C-210`) | all three; `C-R3-1`, `C-R3-16` | written (union) |
| P00_Band.7 | The bands and thresholds | A (`A-7`), B (`B-107`), C (`C-207`, `C-208`) | all three; `B-R3-2`, `C-R3-4`, `A-R3-6`, `B-R3-21` | written (union) |
| P00_Band.8 | The queue entry, its mark, its text | A (`A-8`), B (`B-108`), C (`C-211`) | all three; `B-R3-3` | written (union) |
| P00_Band.9 | The cross-check's frame; the first check | A (`A-9`, `A-10`), B (`B-109`), C (`C-213`, `C-214`) | `B-R3-4`, `A-R3-7`, `B-R3-20` | written (union) |
| P00_Band.10 | No datasheet place | A (`A-11`), B (`B-110`) | not contradicted | written (union) |
| P00_Band.11 | Band 5 on Census I, by ruling, not provisional | A (`A-14`), B (`B-113`), C (`C-217`) | all three | written (union) |
| P00_Band.12 | The combined count decides the band | A (`A-14` step 3), B (`B-113` step 3) | `C-R3-15` | written (union) |
| P00_Band.13 | Near the floor of Band 5 | A (`A-14` step 4), B (`B-113` step 2), C (`C-217`) | all three | written (union) |
| P00_Band.14 | The flip comes from the ruling; no in-world event | A (`A-14` step 5), C (`C-217` step 7, as corrected) | `B-R3-18`; correction `B-R3-24` | written (union) |
| P00_Band.15 | The declaration carries the deferral | A (`A-14` steps 6–7), B (`B-113` step 5), C (`C-217` step 5) | all three | written (union) |
| P00_Band.16 | The ruling named; the queue entry's status left open | A (`A-14` step 8), B (`B-113` step 6), C (`C-245`) | all three | written (union) |
| P00_Band.17 | Census I listed first | C (`C-217`) | A and B list it first in their proposed lines (`A-14`, `B-113`) | written (union) |
| P00_Band.18 | Census II a figure, not a second band | A (`A-52`), B (`B-113` step 4), C (`C-217` step 6, `C-223`) | all three; its wording is P00_Band.91 | written (union) |
| P00_Band.19 | The most consequential declaration; the band does not move with the Act | A (`A-14`, second and third order) | `B-R3-2`, `C-R3-4`; `B-122` step 4 | written (union) |
| P00_Band.20 | What survives in the declaration | A (`A-15`), B (`B-115`), C (`C-219`) | all three | written (union) |
| P00_Band.21 | Downstream of the declaration | A (`A-16`), B (`B-116`), C (`C-220`) | all three | written (union) |
| P00_Band.22 | §2's heading | A (`A-19` step 1), B (`B-119`), C (`C-223`) | all three | written (union) |
| P00_Band.23 | §2's table | A (`A-19` step 2), B (`B-119`), C (`C-223`) | all three | written (union) |
| P00_Band.24 | One band, two figures; the fall of 421,229 | A (`A-19` step 3), B (`B-119`, `B-124`), C (`C-224`) | `C-R3-37` | written (union) |
| P00_Band.25 | The queue's named gap does not arise for this city's band | C (`C-224`), A (`A-50`, its ground) | `B-R3-13` | written (union) |
| P00_Band.26 | The design figure and the Orbital-era census; the slack | A (`A-19` step 4), B (`B-114`), C (`C-218`) | narrowed `C-R3-6`, `C-R3-14` | written (conservative) |
| P00_Band.27 | The slack is a scale fact on the Orbital side | B (`B-114`), C (`C-218`), A (`A-14` third order) | not contradicted | written (union) |
| P00_Band.28 | What and where the slack is: not stated, deferred | A (`A-45`), B (`B-148`), C (`C-218`, `C-252`) | `A-R3-10` d, `B-R3-27` | written (union) |
| P00_Band.29 | No admitted cause for the fall | A (`A-44`), B (`B-148`), C (`C-244`) | all three | written (union) |
| P00_Band.30 | Not a rounding question, on a wider margin | A (`A-19` step 5), B (`B-120`), C (`C-225`) | all three | written (union) |
| P00_Band.31 | What the pass does under the ruling, as instruction | A (`A-19` step 6), B (`B-121`), C (`C-226`) | wording `A-R3-8`; hedge `B-114` | written (conservative) |
| P00_Band.32 | The superset ground no longer carries | A (`A-19` step 6), B (`B-121`, `B-140`), C (`C-226`) | `C-R3-13`, `C-R3-30` | written (union) |
| P00_Band.33 | The caution survives as a guard, whole frame | A (`A-19` step 7, `A-41`), B (`B-122`), C (`C-227`) | all three; `A-R3-5` f, `B-R3-31` | written (union) |
| P00_Band.34 | The count has no admitted derivation | A (`A-19` step 7), B (`B-122` step 5), C (`C-227`) | `A-R3-17`, `C-R3-37` | written (union) |
| P00_Band.35 | Readings A, B and C | A (`A-19` step 8), B (`B-123`), C (`C-228`) | `A-R3-5` f, `B-R3-17` | written (union) |
| P00_Band.36 | §2a's census row restated, kept declared | A (`A-24` step 1), B (`B-124`), C (`C-229`) | all three; heading is P00_Band.92 | written (union) |
| P00_Band.37 | The kind of writing the band calls for does not change at ~2688 | A (`A-24` step 2), C (`C-229`, `C-R3-26`) | B left it to the deferred analysis (`B-124`) | written (conservative) |
| P00_Band.38 | The frame still stands as one | A (`A-24` step 4), B (`B-124`), C (`C-229`) | `B-R3-5`, `C-R3-3` | written (union) |
| P00_Band.39 | No band reason left to split off the pre-orbital half (C's inference) | C (`C-229`) | marked as inference `B-R3-23` | written (union) |
| P00_Band.40 | The own-eras instrument survives on the figures | A (`A-24` step 5), B (`B-123`), C (`C-228`) | all three; Census II use is P00_Band.90 | written (union) |
| P00_Band.41 | Docket notes for Phase 4, Phase 9 and Gate 11 | A (`A-19` second order), B (`B-126`), C (`C-220`) | `A-R3-10` f, `B-R3-30` | written (union) |
| P00_Band.42 | Why the guard matters now (A's inference) | A (`A-19` third order) | `B-R3-18` | written (union) |
| P00_Band.43 | What survives in §2 and §2a | A (`A-20`, `A-25`), B (`B-125`), C (`C-230`) | all three | written (union) |
| P00_Band.44 | Downstream of §2 and §2a | A (`A-21`, `A-26`), B (`B-126`), C (`C-231`) | all three | written (union) |
| P00_Band.45 | §6 item 1 stands on the fifty-thousand threshold, deferred | A (`A-29` steps 1–2), B (`B-129`), C (`C-234`) | all three; `A-R3-10` i | written (union) |
| P00_Band.46 | What survives in item 1; the rock-against-ice shape as a constraint | A (`A-29` step 3), B (`B-129` step 4), C (`C-234`, `C-236`) | all three | written (union) |
| P00_Band.47 | Second and third order of §6 | B (`B-129` step 5), C (`C-234`) | not contradicted | written (union) |
| P00_Band.48 | §6 item 2 answered; the queue entry's status open | A (`A-29` step 4), B (`B-130`), C (`C-235`) | all three; B's added request is in P00_Band.89 | written (union) |
| P00_Band.49 | Item 3 untouched; the rock line not read as a fact about this city | A (`A-29` step 5), B (`B-131`), C (`C-232`) | rock line `A-R3-8`, `B-R3-25` | written (conservative) |
| P00_Band.50 | Downstream of §6 | A (`A-31`), B (`B-132`), C (`C-237`) | all three | written (union) |
| P00_Band.51 | §10's first limit becomes the declared deferral | A (`A-34`), B (`B-135`), C (`C-240`) | all three | written (union) |
| P00_Band.52 | Two added limits in §10 | A (`A-34`) | `C-R3-12`, `B-R3-16`; ground added `A-R3-14` | written (union) |
| P00_Band.53 | What survives in §10 | A (`A-35`), B (`B-136`), C (`C-241`) | all three | written (union) |
| P00_Band.54 | Downstream of §10 | A (`A-36`), B (`B-137`), C (`C-242`) | all three | written (union) |
| P00_Band.55 | A Band 4 on humans alone | A (`A-38`), B (`B-141`) | `C-R3-15`, `C-R3-31` | not written (killed by evidence: the band is set on the combined count) |
| P00_Band.56 | The new figures as the cause of the flip | A (`A-39`) | verdict L28; `B-R3-18`; `C-R3-32` | not written (killed by evidence: the pass's own Census I was already above the line) |
| P00_Band.57 | 11.26% as inside the threshold's approximation | B (`B-142`) | not contradicted | not written (killed by evidence: the pass refused 6% as rounding, and the log names the band) |
| P00_Band.58 | Two band states under Reading C | B (`B-143`), C (`C-246`), A (`A-19` step 8) | all three | not written (killed by evidence: one band for the whole frame) |
| P00_Band.59 | Recomputing or rescaling the count | B (`B-122` step 5, `B-146`), C (`C-243`) | `A-R3-17`, `B-R3-30`, `C-R3-37` | not written (killed for want of an admitted line) |
| P00_Band.60 | An Orbital-era density on the Census I footprint | A (`A-43`) | not contradicted | not written (killed for want of an admitted line) |
| P00_Band.61 | Footprint, rock figures and coefficients: other items; raw basis | A (`A-R3-15`, `A-R3-16`), B (`B-R3-32` to `B-R3-35`), C (`C-R3-35`, `C-R3-36`) | each other | written (union) |
| P00_Band.62 | Two sources in no list | C (`C-250`) | verdict L64, L68 | written (union) |
| P00_Band.63 | Whether the ruling was in force when the pass was written | C (`C-251`) | verdict L79 | written (union) |
| P00_Band.64 | The queue's length-of-halves framing not used | A (`A-47`) | not contradicted | written (union) |
| P00_Band.65 | Self-correction: the flip does not remove the decomposition | A (`A-40`), B (`B-144`), C (`C-248`) | all three | written (union) |
| P00_Band.66 | Self-correction: the guard is not deferred with the analysis | A (`A-41`) | `C-227` step 4, `A-R3-7` | written (union) |
| P00_Band.67 | Self-correction: the §2 heading's words | A (`A-42`) | not contradicted | written (union) |
| P00_Band.68 | Self-check: the row's marking does not weaken the band | B (`B-145`) | verdict L75 | written (union) |
| P00_Band.69 | Self-correction: the census row restored | C (`C-247`) | not contradicted | written (union) |
| P00_Band.70 | Self-check: the pass-era rounding | B (`B-149`) | `A-3`, `C-R3-37` | written (union) |
| P00_Band.71 | A's two transitions of kind | A (`A-24` step 3, `A-53`) | withdrawn `A-R3-11` | not written (withdrawn by its finder in Round 3; the heading is question P00_Band.92) |
| P00_Band.72 | A's no own-era use for Census II | A (`A-52`) | narrowed `A-R3-12`; tension `B-R3-8` | not written (narrowed by its finder; question P00_Band.90) |
| P00_Band.73 | A's extent band out of scope | A (`A-48`) | narrowed `A-R3-13` | not written (narrowed to a docket check; question P00_Band.95) |
| P00_Band.74 | B's Band 4 range wording and its use of LOG L220 | B (`B-113`, `B-119`) | withdrawn `B-R3-10`, `B-R3-28`; `A-R3-3` | not written (withdrawn by its finder; question P00_Band.91) |
| P00_Band.75 | B's support from LOG L224–L225 | B (`B-104`, `B-123`) | withdrawn `B-R3-11`; `A-46` | not written (withdrawn by its finder; the ground rests on LOG L216–L218) |
| P00_Band.76 | B's research thread on the slack, now | B (`B-155`) | withdrawn `B-R3-27` | not written (withdrawn by its finder; kept as an option in question P00_Band.94) |
| P00_Band.77 | C's margin sentence | C (`C-219`) | withdrawn `C-R3-32` | not written (withdrawn by its finder; no admitted line shows the margin alone would move the pass) |
| P00_Band.78 | C's count of three kept as transitions | C (`C-229`) | narrowed `C-R3-9`, `C-R3-33` | not written (narrowed by its finder; question P00_Band.92) |
| P00_Band.79 | C's attribution of the census rows' sentence that nobody left the city | C (`C-217` step 7) | corrected `B-R3-24` | not written (misattributed; P00_Band.14 carries the corrected form) |
| P00_Band.80 | Two claims that asserted more than an admitted line shows | A (`A-19` step 4), C (`C-217`, proposed lines) | `C-R3-6`, `C-R3-14`; `A-R3-8` | not written (narrower forms at P00_Band.26 and P00_Band.31) |
| P00_Band.81 | C's placing of the rock line in this city | C (`C-218`) | corrected `A-R3-8`, `B-R3-25` | not written (the line is a general quotation; P00_Band.49) |
| P00_Band.82 | C's Act 1 point marked as inference | B (`B-R3-23`) | not contradicted | written (union) |
| P00_Band.83 | The first check's line addresses | C (`C-R3-22`) | not contradicted | written (union) |
| P00_Band.84 | The count of the note's admitted lines, repaired | A, B, C (reading logs; `C-253`) | Round 2 repair by all three | written (union) |
| P00_Band.85 | Whole-file loads by comparison scripts | A (reading log), B (`B-R3-7`) | not contradicted | written (union) |
| P00_Band.86 | The note's line count, 356 against 384 | A (`A-R3-2`) | not contradicted | written (union) |
| P00_Band.89 | Is the queue entry on the band crossing closed? | A (`A-50`), B (`B-151`, `B-130`), C (`C-254`) | marked (c) `A-R3-5` c, `B-R3-13`, `B-R3-29`, `C-R3-24`, `C-R3-27` | question |
| P00_Band.90 | May Census II describe the Orbital era? | C (`C-257`), B (`B-123`), A (`A-52`, narrowed) | marked (c) `B-R3-14`, `C-R3-10` | question |
| P00_Band.91 | What band wording stands beside Census II? | A (`A-52`), B (`B-113`), C (`C-223`) | marked (c) `A-R3-5` b, `A-R3-10` c, `C-R3-25` | question |
| P00_Band.92 | How §2a's heading names and counts the changes | A (`A-53`), B (`B-124`), C (`C-229`) | marked (c) `B-R3-12`, `C-R3-9` | question |
| P00_Band.93 | The guard's count and words | A (`A-51`), B (`B-152`, `B-153`), C (`C-255`) | marked (c) `A-R3-10` h, `C-R3-11` | question |
| P00_Band.94 | How the frame states the Orbital-era slack | C (`C-256`), B (`B-155`), A (`A-34`, `A-45`) | marked (c) `A-R3-5` e, `C-R3-28` | question |
| P00_Band.95 | Does the extent band still match? | B (`B-147`, `B-154`) | `A-R3-13`, `C-R3-29` | question |
| P00_Band.96 | Lines that follow a line about another city | A (`A-46`) | marked (c) `A-R3-5` g; `C-R3-7` | question |

## 4 Splits and how each was merged

All three readers reached the same band (5, on Census I, by ruling), the same deferral, the same ground for the
decomposition and the same guard in substance. The splits below are about footing, wording and reach. Each is merged
on content, choosing the reading that claims least and fits the union's findings; a reader's withdrawal of its own
claim counts as evidence for the narrower reading, not as a vote. Where readers marked the difference as a developer
question (their option (c)), it is also written in section 6.

**No origin or ethnicity material arose in this piece**, so the named exception (demote, never exclude) was not
needed, and no row is demoted.

**Split on P00_Band.4: the footing of the design ground** (question P00_Band.96).
- A, post-Round 3: did not use LOG L222–L226, because they follow a line about another city (`A-46`); calls B's use a
  rule-application question for the developer (`A-R3-5` g).
- B, post-Round 3: had used LOG L224–L225 for the point that the ruling answers what the city must be built to hold,
  not which snapshot the frame describes, and LOG L220's form for Census II; withdrew both, resting the point on LOG
  L216–L218 alone (`B-R3-10`, `B-R3-11`).
- C, post-Round 3: used LOG L226; holds that LOG L222–L226 name no city and are general, so a general mechanism may be
  taken from them, while agreeing A's restraint costs nothing (`C-R3-7`).
- **Merged:** the design ground rests on LOG L216–L218 alone, which all three accept and which carries the same point.
  Nothing in this piece rests on LOG L220 or L222–L226. The general rule for such lines goes to the developer.

**Split on P00_Band.18 and P00_Band.23: band wording beside Census II** (question P00_Band.91).
- A: no band label; "a band label beside it would read as a second band" (A's Round 1 file, L181); marked (c)
  (`A-R3-5` b, `A-R3-10` c), and warned that C's wording, read alone, could place 691,371 in Band 5 (`A-R3-8`).
- B: first wrote "in Band 4's range; a figure, not a second band" (B's Round 1 file, L44); withdrew it, holding A right
  and C right (`B-R3-10`, `B-R3-28`).
- C: "the same band; Census II is not a second declaration" (C's Round 1 file, L101); marked (c), low stakes
  (`C-R3-25`).
- **Merged:** all three say Census II is not a second band, and that is written (P00_Band.18). The merged text gives
  no band word beside the figure, only its distance below the line and the note that it is not a second band, as in
  the proposed table at P00_Band.24: the reading that claims least. The choice of words is the developer's.

**Split on P00_Band.26: whether the city is physically built to the design figure across the whole frame.**
- A: "So the city is built for 1,112,600 across the whole frame" (A's Round 1 file, L80); not answered in Round 3,
  since A's cross-check was written without C's.
- B: the built fabric is sized to 1,112,600 (`B-114`); no Round 3 comment on the point.
- C: the ruling fixes the design figure, and no admitted line dates when the built city reaches that size inside a
  frame that opens in 2564; A's phrase holds for the band as a declared design figure, not demonstrably for the
  physical build (`C-R3-6`, `C-R3-14`).
- **Merged:** the slack is stated against the declared design figure; no claim is made about the physical build at any
  date. This claims least, and every figure the union uses (421,229; 37.86%; 62.14%) survives unchanged under it.

**Split on P00_Band.31: whether the amendment may say the pass writes base-level facts.**
- C's proposed declaration lines said the pass writes base-level facts (`C-217`). A: that asserts more than any reader
  checked, since the ordinary-life and populations phases and the scale gate are outside every admitted line
  (`A-R3-8`). B had hedged the same point (`B-114`). C did not answer (its cross-check was written without A's).
- **Merged:** the amendment states what the ruling asks a pass to write meanwhile, as instruction, and turns the
  question of whether the pass body meets it into a docket check (P00_Band.41 item 5).

**Split on P00_Band.37: whether the fall across the line changes the kind of writing.**
- B left whether a fall across the ~1M line changes the kind of writing, in the sense of the upper threshold, to the
  deferred analysis (`B-124`). C: the band, and so the kind of writing it calls for, is fixed for the whole frame
  (`C-R3-21`, `C-R3-26`). A: with the band unchanged, nothing at the census boundary changes the form of a question
  (`A-24` step 2; A withdrew only the counting conclusion it drew from this, `A-R3-11`).
- **Merged:** both halves are kept, because they answer different things. The kind of writing *the band* calls for
  does not change at about 2688 (all three hold the band is set once). Whether the deferred analysis writes the two
  eras differently stays with the deferral and with question P00_Band.90, which is what B's open end protects.

**Split on P00_Band.49: the rock line at Frame L294–L295.**
- C placed "the 10% on rock is the only ground that never has to be rebuilt" (Frame L295) in this city (`C-218`); B
  used the same line for its slack question (`B-155`). A and B: the pass is quoting the extent file's general statement
  about a mostly-ice city, and whether it describes this city belongs to the rock items, since the note records this
  city as rock-founded (`A-R3-8`, `B-R3-25`; B applies the caution to itself).
- **Merged:** the line is not read as a fact about this city, and nothing in this piece rests on it.

**Split on question P00_Band.89: whether the queue entry is closed, and whether §6 item 2 adds a request.**
- A: closed in full; keeps that recommendation, and holds that no admitted line asks the deferred analysis to write
  two census states (`A-50`, `A-R3-5` c).
- B: answered in its band half, with how the two census states are written carried into the deferred analysis and
  added to §6 item 2 (`B-151`, `B-130`); in Round 3 calls C's split into two questions the cleaner form and would merge
  into it (`B-R3-13`, `B-R3-29`).
- C: closed, with the Census II matter asked on its own (`C-254`, `C-257`); B's added request stands or falls with the
  closure question (`C-R3-24`, `C-R3-27`).
- **Merged (provisional, in section 6):** closed as to the band, with the one matter left over asked separately, as
  question P00_Band.90. All three agree the band is answered; separating the leftover matter claims less than adding a
  request to the deferred analysis, which no admitted line makes. §6 item 2's proposed text adds no request.

**Split on question P00_Band.90: whether Census II may describe the Orbital era.**
- A first allowed no use beyond stating the figure (`A-52`), then narrowed to C's view: Census II may be stated in the
  own-eras description, with no derived figure resting on it (`A-R3-12`), resolving the tension B found in A's own
  file (`B-R3-8`).
- B and C: stated canon in the own-eras description, never the base of a process-derived figure (`B-123`, `C-257`);
  both marked the matter (c) (`B-R3-14`, `C-R3-10`).
- **Merged (provisional):** the view all three now hold, recommended in section 6.

**Split on question P00_Band.92: how §2a's heading names and counts the three dated changes.**
- A: first counted two transitions of kind plus one declared change of population figure (`A-24` step 3); withdrew it
  (`A-R3-11`), holding that §2a classes rows
  by what changes and the population's scale still changes (`A-R3-5` a). A now keeps three, with the census row
  relabeled.
- B: three kept (`B-124`); in Round 3 marked it (c), finding support for A's first reading in 01 L187 (`B-R3-12`).
- C: three kept (`C-229`); in Round 3 narrowed to "three dated changes stay declared" (C's Round 3 file, L29), with
  whether the heading still calls the census row a structural transition left as wording for the developer
  (`C-R3-9`, `C-R3-33`).
- **Merged:** the readers crossed over in Round 3, each conceding part of the other's view. All three hold that the row
  stays declared and that L200 survives (written at P00_Band.36). The heading's wording is recommended, provisionally,
  as three dated changes, without calling the census row a structural transition or denying it is one.

**Split on question P00_Band.93: the guard's words.**
- A words it after the scale error (01 L221); C after the ruling's level (LOG L249); B after the ruling's base-level
  facts, "what is true of the place" (LOG L249) (`A-51`, `C-255`, `B-122`). All three drop the count and extend the guard to the
  whole frame. A and C marked the wording (c) (`A-R3-10` h, `C-R3-11`); C notes the two forms can stand together.
- **Merged:** the recommended wording at P00_Band.33 uses both forms; the choice is the developer's.

**Split on question P00_Band.94: the Orbital-era slack.**
- B first recommended raising it now as a research and design thread for the rock and ice items (`B-155`), then
  withdrew that recommendation and adopted A's §10 limit and C's deferral ground (`B-R3-16`, `B-R3-27`).
- A: a declared limit; adopts C's ground that placing the slack would be invented internal structure (`A-34`,
  `A-R3-10` d); marked B's thread (c) (`A-R3-5` e).
- C: figures only, where and how deferred with the decomposition (`C-256`); marked B's thread (c), noting that a thread
  that researches without placing anything would not breach the deferral (`C-R3-28`).
- **Merged (provisional):** figures plus the §10 limit, with where and how deferred. B's withdrawal is evidence for this
  narrower reading; the research thread stays in section 6 as an option, since two readers asked the developer.

**Resolved without a remaining split (recorded for the record).**
- The extent band (question P00_Band.95): A first called it out of scope (`A-48`), then narrowed it to a docket check
  (`A-R3-13`); B held its question right (`B-R3-15`); C adopted B's recommendation (`C-R3-29`). Kept as a question
  because B posed it to the developer; the readers agree on the recommendation.
- The superset ground (P00_Band.32): C's added reason, that the margin had grown, was withdrawn by C (`C-R3-32`);
  C adopted A's and B's reason (`C-R3-13`, `C-R3-30`).
- Reading B's caveat (P00_Band.35): A held it met by the design ground, B held it a matter for the deferred analysis;
  B found no conflict, the band half answered and the writing half deferred (`B-R3-17`).

## 5 Killed findings, dead ends, self-corrections, and any quotation or line the merge corrected

### 5.1 Killed findings (with what killed each)

- **P00_Band.55. A Band 4 on humans alone: killed by evidence.** Humans alone at Census I are 545,891 (census L505),
  inside Band 4's range, "~50,000–1M" (01 L180). The pass bands the combined row (Frame L159–L160), the rulings log
  applies the ruling to the combined 1,112,600 (LOG L1713), and no admitted line separates humans from robots for the
  band (`A-38`, `B-141`; C, which had not raised it, accepts the kill, `C-R3-15`).
- **P00_Band.56. The new figures as the cause of the flip: killed by evidence.** The pass's own Census I was already
  above the line (Frame L31, L160), the later adjustments are arithmetic (census L505), and the first check found "The
  figures on their own would not move the conclusion." (verdict L28). The flip comes from the ruling (`A-39`).
- **P00_Band.57. Treating 11.26% as inside the threshold's approximation: killed by evidence.** The thresholds are approximate, "Above
  roughly a million," (01 L218), but the pass itself refused to treat its 6% as rounding (Frame L165–L168), and the
  rulings log names the band for this figure (LOG L1713) (`B-142`).
- **P00_Band.58. Two band states under Reading C: killed by evidence.** One band is set for the whole frame (LOG
  L211, L214, L1713). Narrowed rather than killed as to C's own-eras use, which survives on the figures (P00_Band.40)
  (`B-143`, `C-246`, `A-19` step 8).
- **P00_Band.59. Recomputing or rescaling the count of two hundred thousand (Frame L174): killed for want of an admitted line.** B scaled it
  by the ratio of the two Census I figures to 209,829 and did not adopt it (`B-122` step 5, `B-146`). C found two
  routes to a number near it on the pass's figures, about a fifth of its Census I (1,060,482 × 0.2 = 212,096) or about
  half its fall between the censuses ((1,060,482 − 655,492) ÷ 2 = 202,495), and no admitted line says which, if
  either, the pass used (`C-243`). All three figures were recomputed and match (`A-R3-17`, `C-R3-37`).
- **P00_Band.60. An Orbital-era density on the Census I footprint: killed for want of an admitted line.** No admitted
  line says the built footprint stays the same across the census boundary, and the footprint belongs to another item
  (`A-43`).

### 5.2 Dead ends

- **P00_Band.61. The footprint, the rock figures and the coefficients belong to other items, on a raw basis.** The
  footprint, "**111.26 to 158.94 km²**" (note L133), is Census I divided by the raw densities 10,000 and 7,000 per km²
  named on that row, with no site factor applied; the source of the two densities is in no admitted line, since the
  row is marked only "computed" (note L133). The city's part of the shared rock, 13.36 km² (note L135), is the raw
  Census I share of about 40 km²; the rock share of the footprint, "rock **8.41% to 12.01%**" (note L136), follows
  from those two and inherits the densities' unstated basis. The site's difficulty coefficient, "D = 1.25," (note
  L56), is applied to none of these and to no figure in this piece; no reader applied the note's workforce rates either
  (`A-R3-15`, `A-R3-16`, `B-R3-32` to `B-R3-35`, `C-R3-35`, `C-R3-36`). No band conclusion rests on any of them.
- **P00_Band.62. Two sources were in no reader's list.** The methodology's own-eras section, and the source of the
  queue's convention that "all process-derived figures use Census I." (QUEUE L567). The own-eras instrument is used
  here only through the pass's own quotation of it (Frame L198–L200) (`C-250`; the first check names both as missing,
  verdict L64, L68).
- **P00_Band.63. Whether the Census I ruling was in force when the pass was written** is not in the admitted lines,
  and it does not matter to a re-derivation against the inputs as they stand (note L36) (`C-251`; verdict L79).
- **P00_Band.64. The queue's framing of the two halves by their length in years** (QUEUE L555–L556) was not used: a
  span of years is not a reason for anything in this piece (`A-47`). QUEUE L555 names a structure by its full name and
  is not quoted.

### 5.3 Self-corrections (Round 1)

- **P00_Band.65. That the flip removes the decomposition.** All three readers first read "Band 4 makes it mandatory."
  (Frame L288) as losing its obligation along with its ground. B had first taken the first check's "its Band 4 ground
  is gone" (verdict L58) as the conclusion. Each corrected it: the obligation comes from the fifty-thousand threshold
  (01 L211–L212), which this city exceeds, and the ruling defers it (LOG L234) (`A-40`, `B-144`, `C-248`).
- **P00_Band.66. That the guard is deferred with the analysis.** Considered by A and not adopted: the ruling suspends
  two obligations (LOG L230, L234–L235), and the scale-error sentence (01 L220–L221) names an error, not something to
  perform; no admitted line says in words that the guard survives (`A-41`; P00_Band.33 step 4).
- **P00_Band.67. The §2 heading's "the frame crosses a threshold".** A first kept it (Frame L153), since the figures
  lie on both sides of the line; corrected: the figures cross the line, the band does not (`A-42`).
- **P00_Band.68. Whether the log row's marking as a note weakens the band.** Checked by B: it does not (`B-145`;
  P00_Band.5).
- **P00_Band.69. §2a reduced to two transitions.** C first dropped the census row, then restored it, relabeled,
  because the population figure still changes at about 2688 by 421,229 (`C-247`).
- **P00_Band.70. The pass-era rounding.** The pass's 6% (Frame L31) was 6.05% on its own figure, and the queue's "35%
  below" (QUEUE L572) was 34.45% on the pass's Census II; neither changes anything (`B-149`; P00_Band.3).

### 5.4 Withdrawals and narrowings in Round 3

Additions one reader adopted from another in Round 3 (`A-R3-14`, `B-R3-16`, `B-R3-30`, `C-R3-12`, `C-R3-13`,
`C-R3-29`, `C-R3-34`) are written into the findings they joined (P00_Band.32, P00_Band.41, P00_Band.52, P00_Band.55,
P00_Band.95).

- **P00_Band.71. A withdrew its count of two transitions of kind** (`A-24` step 3) and its recommended heading
  (`A-53`), holding that §2a classes its rows by what changes and that the population's scale still changes at about
  2688 (`A-R3-5` a, `A-R3-11`). The heading is question P00_Band.92.
- **P00_Band.72. A narrowed its view of Census II** (`A-52`: the figure stated, no own-era use) to: Census II may be
  stated in the own-eras description, with no derived figure resting on it, its band wording left open (`A-R3-12`).
  This resolved a tension B found between A's step 5 at `A-24` and `A-52` (`B-R3-8`). The matter is question
  P00_Band.90.
- **P00_Band.73. A narrowed the extent band** from out of scope (`A-48`) to a docket check for the item that owns the
  extent row (`A-R3-13`). Question P00_Band.95.
- **P00_Band.74. B withdrew its Census II wording**, that the figure is in Band 4's range (`B-113`, `B-119`), and its
  use of the ruling's worked example for that form, a line about another city (LOG L220) (`B-R3-10`, `B-R3-28`).
  Question P00_Band.91.
- **P00_Band.75. B dropped LOG L224–L225 as support** for the point that the ruling answers what the city must be
  built to hold, resting it on LOG L216–L218 alone (`B-R3-11`). Question P00_Band.96.
- **P00_Band.76. B withdrew its recommendation to open a research and design thread on the slack now** (`B-155`),
  adopting the deferral ground (LOG L237, L241–L242) and A's §10 limit (`B-R3-16`, `B-R3-27`). Question P00_Band.94.
- **P00_Band.77. C withdrew the last sentence of `C-219`**, that the pass's own route had lost its footing because the
  margin had grown from 6% to 11.26%: no admitted line shows that this alone would have moved the pass's choice
  (`C-R3-32`; verdict L28).
- **P00_Band.78. C narrowed "the count of three stays"** (C's Round 1 file, L120; `C-229`) to three dated changes declared, with the heading's
  wording left to the developer (`C-R3-9`, `C-R3-33`). Question P00_Band.92.

### 5.5 Corrections one reader made to another's claim (Round 3)

- **P00_Band.79. A misattributed sentence (`B-R3-24`).** `C-217` step 7 cited the census rows' sentence that nobody
  left the city as describing the changes since the pass. On both rows that sentence belongs to the −10% authoring
  adjustment of 2026-09-05, the change that produced the pass's own figures (1,178,313 × 0.9 = 1,060,481.7, the pass's
  1,060,482, B's arithmetic on census L505; the merge checked the Census II row the same way: 728,324 × 0.9 =
  655,491.6, the pass's 655,492, census L653). The changes since the pass are the two later entries on each row, each
  recorded as arithmetic and not a migration. C's own `C-203` states this correctly, and C's conclusion (no in-world
  event to narrate) holds on the later entries' wording. P00_Band.14 is written in the corrected form.
- **P00_Band.80. Two claims that asserted more than an admitted line shows.** A's "So the city is built for 1,112,600
  across the whole frame" (A's Round 1 file, L80): no admitted line dates when the built city reaches that size inside
  a frame that opens in 2564 (`C-R3-6`, `C-R3-14`). C's proposed declaration sentence that the pass writes base-level
  facts (`C-217`): the pass body is outside every admitted line (`A-R3-8`). Neither finder answered in Round 3, since
  each cross-check was written without the other's. Both are written in narrower form, at P00_Band.26 and P00_Band.31.
- **P00_Band.81. The rock line's attribution (`A-R3-8`, `B-R3-25`).** `C-218` placed "the 10% on rock is the only
  ground that never has to be rebuilt" (Frame L295) "in this city" (C's Round 1 file, L69); the pass is quoting the extent file's general
  statement about a mostly-ice city (Frame L294). B applied the same caution to its own use of the line (`B-155`).
  Written in narrower form at P00_Band.49.
- **P00_Band.82. An inference marked as one (`B-R3-23`).** `C-229` said the band no longer adds a reason to split the
  pre-orbital half off; no admitted line has the pass give the band as a reason for the question at Frame L201. Written
  at P00_Band.39 as C's inference.
- **P00_Band.83. Line addresses for the first check (`C-R3-22`).** B cited the verdict's affected sentences as L40–L52
  and its points as L54–L60; the list headings are at L39 and L53. This file uses verdict L39–L52 and L53–L60.

### 5.6 Procedural snags

- **P00_Band.84. The count of the note's admitted lines.** The note's range lists lines 29–34 and then 24–61, so
  29–34 lie inside 24–61. All three readers first counted through the spans in the order given, 106 lines with the
  middle at file line 41; after the mechanical check each repaired the count to 100 distinct lines with the middle at
  file line 51 (the Round 2 repair lines in each reader's reading log; `C-253` had recorded both counts). The first
  count's middle line carries names this piece may not reproduce, and it is not reproduced.
- **P00_Band.85. Whole-file loads.** The readers' comparison scripts and line counts loaded each listed file whole in
  order to index the listed lines; only lines inside listed spans were printed, compared or used (A's reading log;
  `B-R3-7`).
- **P00_Band.86. The note's length.** The first check counted the note at 356 lines (verdict L91); B and C count 384.
  Not material: every admitted span of the note ends at or before L304 (`A-R3-2`).

### 5.7 Corrections made by this merge (not findings; no row in section 3)

- **P00_Band.87. Quotations from lines that name another location are given unquoted.** The readers quoted from
  census L505 and L653 (the combined figures, the earlier values, and the notes that the changes were arithmetic and
  not a migration, or that nobody left the city), from LOG L1713 (its general clause, this city's clause and its
  marking as a note), and, in B's case, from LOG L224–L226. Census L505, L653 and LOG L1713 each name other locations,
  so their content is given here unquoted, by role, with file and line (P00_Band.1, P00_Band.2, P00_Band.5,
  P00_Band.14, P00_Band.29). LOG L224–L226 name no location but are not used (P00_Band.4, question P00_Band.96).
  Likewise the note's lines on the missing datasheets (note L29–L33, of which L32 names another location) and the
  pass's Act and civic rows (Frame L189, L191) are described unquoted. Every reader quotation this file uses was
  checked against its source line; none differs, apart from the misattribution at P00_Band.79.
- **P00_Band.88. An over-wide read by the merge writer.** To check note L281–L294 and L304, one Read displayed lines
  281 to 304, which includes two lines outside the listed spans: L295 (blank) and L303 (another item's row in section
  F). Neither is used here.

## 6 Open questions for the developer

Every recommended answer below is **PROVISIONAL**. None decides a question a ruling leaves open; each is the merge's
best reading of the readers' post-Round 3 views, for the developer to accept, change or refuse.

- **P00_Band.89. Is the queue entry on the band crossing closed by the Census I ruling?** (note L285, L291–L292;
  `A-50`, `B-151`, `B-130`, `C-254`; marked (c) by `A-R3-5` c, `B-R3-13`, `B-R3-29`, `C-R3-24`, `C-R3-27`.)
  - (a) Closed in full: answered by the Census I ruling, "corpus-wide" (LOG L214), as applied to this city (LOG
    L1713). The queue keeps its text as the record of the question and gains the answer's address, which shows its
    figures (QUEUE L554, L572) to be historical. (A's recommendation; C's option (a).)
  - (b) Closed as to the band, with the one matter left over, whether and how Census II may describe the Orbital era,
    asked on its own (question P00_Band.90) rather than kept inside the queue entry. (C's split, which B calls the
    cleaner form; close to A's own option (C).)
  - (c) Answered in its band half, with how the two census states are written carried into the deferred
    distributional analysis and added to §6 item 2 as a request for when the gate opens. (B's Round 1
    recommendation.)
  - (d) Left open until the gate opens.
  - **Recommended (PROVISIONAL): (b).** All three readers agree the ruling answers the band, so no band crosses inside
    this frame (P00_Band.25). The queue's option C is about writing, "declare the CROSSING; write two states" (QUEUE
    L573), and that matter is real; but no admitted line asks the deferred analysis to write two census states
    (`A-R3-5` c), so asking it separately claims less than (c) and keeps the queue's answer as narrow as the ruling.
    Under any option, the queue text's earlier figures get a note, not an edit (note L291).
- **P00_Band.90. May Census II be used to describe the Orbital era?** (LOG L211; QUEUE L567; Frame L180,
  L198–L200; `A-52` narrowed by `A-R3-12`, `B-123`, `C-257`; marked (c) by `B-R3-14`, `C-R3-10`.)
  - (a) Yes, as stated canon in the own-eras description only (1,112,600 before about 2688, 691,371 after), never as
    the base of a process-derived figure.
  - (b) Stated as a figure only, with no own-era description. (A's Round 1 view, since narrowed.)
  - (c) No: "Everything is assumed with Census I" (LOG L211) excludes it.
  - (d) Yes, including derived figures for the Orbital era.
  - **Recommended (PROVISIONAL): (a).** After A's narrowing, all three readers hold it. The Census II figure is canon
    (census L653). The standing convention, "all process-derived figures use Census I." (QUEUE L567), bars derived
    figures built on Census II, not the statement of the figure; (d) would break it.
- **P00_Band.91. What band wording, if any, stands beside Census II?** (Frame L29, L159–L160; `A-52`, `B-113`
  (withdrawn), `C-223`; marked (c) by `A-R3-5` b, `A-R3-10` c, `C-R3-25`.)
  - (a) None: the figure and its distance below the line, with the note that it is not a second band. (A; B after
    Round 3.)
  - (b) A note that the figure lies in Band 4's numeric range, marked as not a band declaration. (B's Round 1 wording,
    withdrawn; A's own option (B).)
  - (c) "the same band; Census II is not a second declaration" (C's Round 1 file, L101).
  - **Recommended (PROVISIONAL): (a).** It claims least: the distance below the line already says where the figure
    sits (`B-R3-10`). (b) took its form from a line about another city (LOG L220). (c) is true of the city's declared
    band, but read alone it could be taken as placing 691,371 in Band 5, whose range begins at about a million
    (`A-R3-8`; 01 L180–L181).
- **P00_Band.92. How does §2a's heading name and count the three dated changes?** (Frame L182, L190, L200; `A-53`
  (withdrawn), `B-124`, `C-229`; marked (c) by `B-R3-12`, `C-R3-9`.)
  - (a) Keep "THREE STRUCTURAL TRANSITIONS SIT INSIDE ONE FRAME" (Frame L182), with the census row relabeled as a
    change of population figure, kind "scale". (A after Round 3; B's Round 1 view.)
  - (b) Two transitions of kind and one declared change of population figure. (A's Round 1 view, withdrawn.)
  - (c) Three dated changes, all declared, without calling the census row a structural transition. (C after Round 3.)
  - **Recommended (PROVISIONAL): (c).** All three readers agree the row stays declared and L200 survives
    (P00_Band.36). Whether the census row is a transition of kind divides them: nothing at the census boundary
    changes the form of a question (01 L186–L187), which supports not calling it one (`B-R3-12`, `C-R3-9`), while
    §2a's table classes its rows by what changes, and the population's scale does change (`A-R3-5` a). (c) asserts
    neither; A's withdrawal of the narrower count is evidence against asserting that count too.
- **P00_Band.93. The guard: does it stay, and with what reach, count and words?** (Frame L173–L174; 01 L220–L221;
  LOG L235, L246, L248–L249; `A-51`, `B-152`, `B-153`, `C-255`; wording marked (c) by `A-R3-10` h, `C-R3-11`.)
  - (a) Keep it over the whole frame and both Acts, with no head-count, in words that name both the error and the
    level at which it is avoided: the wording at P00_Band.33.
  - (b) Keep the pass's wording and "two hundred thousand" (Frame L174), extended to the whole frame.
  - (c) Restate the count as a share of Census I (17.98%) or rescale it (209,829).
  - (d) Keep it for the pre-orbital half only, as written (Frame L173).
  - (e) Treat it as suspended with the distribution.
  - **Recommended (PROVISIONAL): (a).** All three readers drop the count and extend the guard to the whole frame. The
    count has no admitted derivation (P00_Band.34), and a share-of-population cutoff begins to measure spread, which
    is the analysis the ruling defers (`B-152`; LOG L235). (e) would let text be written that the resumed analysis
    must undo, since the obligation is "suspended, not canceled" (LOG L246). A's form names the error (01 L221) and
    C's names the level (LOG L249); the two can stand together (`C-R3-11`).
- **P00_Band.94. How does the frame state the Orbital-era slack?** (LOG L216–L218, L241–L242; census L505, L653;
  `C-256`, `B-155` (withdrawn), `A-34`, `A-45`; the research thread marked (c) by `A-R3-5` e, `C-R3-28`.)
  - (a) As figures only: the design figure, 1,112,600; the Orbital-era census, 691,371; the difference, 421,229
    (37.86% of the design figure). A §10 limit says what the slack is on the ground and where it sits are not known,
    and both wait for the decomposition.
  - (b) As (a), and also open a research thread now that studies the slack's physical form without placing anything
    in the city.
  - (c) Say nothing: read the ruling as fixing an authoring figure only, with no claim about the city after about
    2688.
  - (d) Decide now where the slack sits.
  - **Recommended (PROVISIONAL): (a).** All three readers hold it after Round 3, and B withdrew the first form of (b).
    (d) would be the invented "internal structure" the ruling defers (LOG L241–L242). (b) would not by itself breach
    the deferral (`C-R3-28`), but no admitted line asks for it, and where the slack sits belongs to the decomposition,
    deferred until all 38 cities have been through the three methods (LOG L237).
- **P00_Band.95. Does the frame's extent band still match its population band?** (01 L167–L168; Frame L19–L35;
  `B-147`, `B-154`; `A-R3-13`, `C-R3-29`.)
  - (a) The item that owns the extent row looks up the frame's extent declaration against Band 5 now.
  - (b) Leave it to the deferred analysis.
  - **Recommended (PROVISIONAL): (a).** A divergence between the two bands "is characterizing" and "should be written
    as a finding" (01 L168); a change of population band is when the match needs looking at, and the check is a
    lookup, not an analysis. All three readers agree after Round 3.
- **P00_Band.96. May a sentence that names no location, on lines that follow a line about another city, be used?**
  (LOG L220, L222–L226; `A-46`; `B-104`, `B-113` (both withdrawn in `B-R3-10`, `B-R3-11`); `C-205`, `C-R3-7`;
  marked (c) by `A-R3-5` g.)
  - (a) Not used: rest the design ground on LOG L216–L218 alone, and take no form from LOG L220. (A; B after Round
    3.)
  - (b) Usable for a general mechanism, when the line itself names no location. (C: LOG L222–L226 name no city, and
    their last clause is general.)
  - **Recommended (PROVISIONAL): (a) for this piece**, since nothing in it rests on those lines and LOG L216–L218 carry
    the same point (C agrees that A's restraint costs nothing, `C-R3-7`). The general rule for such lines is the
    developer's.

## 7 Research the readers used

**None.** No reader ran a web search; each logged that no web research was done (A's, B's and C's Round 1 files,
section 6). This
piece rests on rulings, canon files and the pass. Arithmetic only, on figures from the admitted lines: A with
`python3 -I`, B with `bc`, C with one local command (row sums, distances from the line, the fall between the censuses
and its shares, the footprint quotients, the count's shares and candidate derivations). The merge rechecked every
figure it writes with `python3 -I`; all match.

## 8 Sources

**Read by all three readers in Round 1** (the same seven entries; ranges as listed, by Read offset and limit):

| File (full path) | Lines |
|---|---|
| `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md` | 1–22, 29–34, 296–302, 24–61, 127–144, 281–294, 304 (100 distinct lines; 29–34 lie inside 24–61) |
| `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/00_Frame.md` | 19–35, 150–204, 286–298, 360–377 |
| `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md` | 162–230 |
| `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md` | 505, 653 |
| `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md` | 203–252, 1713 |
| `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md` | 551–577 |
| `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/.xc_20261110_item_SRY-C02.md` | whole file (136 lines) |

Read-only checks the readers logged inside those spans: `01` L196 and L230 (both blank; A, B, C); `Frame` L184 and
L377 and `verdict` L1, L68 and L136 (B; A checked the verdict's end). Round 2 repairs re-read note L51 (A, B, C) and
note L24 and L61 (C). Line counts by `wc -l` (B, C): note 384, `Frame` 377, `01` 590, census 892, LOG 1933, QUEUE
902, `verdict` 136. The readers' comparison scripts and line counts loaded each listed file whole to index the listed
lines; only listed lines were printed, compared or used (P00_Band.85).

**Read by the readers in Round 3:** each read the other two readers' Round 1 files in full, and nothing else (B
counts A's at 266 lines and C's at 285).

**The first check** (whose verdict file is the seventh entry above) read the same note spans without the repeated
29–34, the same `Frame` spans, census L505 and L653, LOG L203–L252 and L1713, and QUEUE L551–L577 (verdict
L83–L92).

**Read by the merge writer:**
- The brief and its two lists (`merge_inputs.txt`, `required.txt`), in the staging folder
  `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/f899d4fe-04ee-4884-94c4-71b538f8f45f/scratchpad/sry/pieces/P00_Band/M/`.
- In full: the three Round 1 files, the three Round 3 files and the verdict file, all in
  `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Shirayuki/`:
  `.t8_xc_P00_Band_readerA.md`, `.t8_xc_P00_Band_readerB.md`, `.t8_xc_P00_Band_readerC.md`,
  `.t8_xc_P00_Band_round3_readerA.md`, `.t8_xc_P00_Band_round3_readerB.md`, `.t8_xc_P00_Band_round3_readerC.md`,
  `.xc_20261110_item_SRY-C02.md`.
- To check quotations and figures: `Frame` L19–L35, L150–L204, L286–L298, L360–L377; LOG L203–L252 and L1713; `01`
  L162–L230; QUEUE L551–L577; census L505 and L653; note L1–L22, L24–L61, L127–L144 and L281–L304. The last read
  displayed note L295 and L303, which lie outside the listed spans; neither is used (P00_Band.88).
- Nothing else was opened.
