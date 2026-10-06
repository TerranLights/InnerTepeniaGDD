# Mirny — Step 4 · Phase 7 · T8 round record

**Pass:** Mirny · ULM · Step 4, Phase 7 (Order) · 2026-10-06.
- **Clock checks:** 07:09, 07:22, 07:27, 07:29, 07:58, 08:01, 08:04, 08:07, 08:26 (merge drafted).
- **Boot:** 07:09–07:25 (runbook read in full; tracker; Mirny's progress row; spine Phase 7 spec and mechanics; Pre-Trip §D–§M; `Datasheets/Phase_7.md`; the Mirny README; the handoff sweep for the brief).
- **Round 1:** dispatched 07:27; reader A finished ~07:58 (31 min, 150 tool uses), C ~08:01 (34 min, 169), B ~08:04 (38 min, 168).
- **Round 2:** 08:04.
- **Round 3:** sent about 08:07; the three replies arrived within about five minutes.
- **Merge:** written 08:07–08:26. Phase 7 was started before 13:59, so it finishes inside the window.

**Files:**
- **Written:** `04_Phase_07_Order.md` (705 lines).
- **Required list:** `.t8_required_04_Phase7.txt` (58 entries, 9,316 admitted lines, about 930 KB; ranges on 26 of them).
- **Reader outputs:** written by the readers directly to the session scratchpad (plan mode did not block the writes) and archived with the pass (`DR-27`) as `.t8_Phase7_readerA.md` (1,147 lines), `…B.md` (1,059), `…C.md` (1,142). Not canon, not an input.
- **Brief:** one identical brief to all three readers (master copy archived as `.t8_Phase7_brief.md`).

## Round 0 — the required-reading list
- **Sources:** the Phase 7 `MUST OPEN` block (`03_The_Phase_Spine.md` L843–882), the Pre-Trip's resolved Phase 7 table (`PTI` L348–365) and the runbook's §C.8c row 7.
- **Added beyond the spine's block** (each because Phase 7's four components cannot be written without it):
  - the Falkland Treaty draft and scaffold (the only written governance skeleton: Arts. I.3, I.4, II.4, III.1);
  - `DRQ-02` (hybrid highway maintenance authority) and `DRQ-06` (no job closed to either body), `Highways.md`, `Ports.md`, `Arcanet.md`;
  - `Laws_of_Robotics.md` and Robot Universals chapters 1, 7, 9, 11, 12, 13, 14, 16 (a robot-majority city: `RB` §C.10 binds every phase);
  - `Robot_Physiology_and_Cultural_Practices.md` and `Robot_Cold_Physiology.md` in full;
  - `DEVELOPER_RULINGS_LOG.md` ranges for `DR-3`, `DR-4`, `DR-9`…`DR-19`, `DR-24`…`DR-26`, `DR-28`, `DR-31`/`DR-32`, `DR-46`/`DR-47`;
  - `Division_of_Industry` `00`, `08`, `09`, `10`, `16` at ranges (Mirny's §20 is `16` L2105–2173).
- **Trimmed:** SOC to its table of contents; `Airports.md` dropped (no Phase 7 handoff touches it); the merge-provenance sections of Phases 2, 4, 5, 6 dropped (process records, not findings). The first draft of the list was 1,001 KB; the admitted list is 932 KB, about 30 % above Phase 6's 708 KB.
- **Orchestrator-verified results (recorded, not dispatched):** the four `Factions/` files naming Mirny (found by `grep -l`; closed by the law of one location and the frame; contents read by no one); the PDFs (not T8-verifiable); SOC; `Airports.md`; `Megacorps/`.
- **The brief named fourteen traps**, including: the Half B / §20 figures (R-24); the §20 Notes; the Technical/scientific cause; the superseded `01`; `DS7`'s stale anchors; the citation gate; currency; the compact; invented practices; reserved items; the treaty's status stamps; `City_Logistics`' scope; no T5 line.
- **No reader failed or was re-dispatched.** All three finished inside 38 minutes.

## Round 1 — what each reader wrote
| Reader | Axis | Distinctive contributions |
|---|---|---|
| A (1,147 lines) | "Mandated work, unruled wind" | the three-question test (trigger / assignee / check); the freedom-margin arithmetic (25.1 % smaller; the site's price 11.59 % of the §20 free tier); the unadministrable table incl. the hub's hidden maintenance decision; the candidate-sanction rows "a handoff, not a penalty"; a 14-row downstream table |
| B (1,059 lines) | "Claims without an arbiter" | the three scales (point / region / above) tied to `FTD` III.1; the Sweep's five absences as a coverage gap; the prohibition table; "blame has no executioner and no appeal"; the LAW G null; a 21-row downstream table |
| C (1,142 lines) | "Tiered work, positional calls" | **both staffing bases** and the formula reproduction (157,468.9 + 261,096.3 = 418,565.2); the coefficient gap; the robot-keyed lower bound on the free tier; the fast/slow × empowered/answerable grid; three sources of legitimacy; a 26-row downstream table |
**All three reached the same findings under different names:** 23.6 % governs and the 11.8 % was the Arcanet sector alone; R-12 not chosen; a chamber is the national default and Mirny is not named; the non-thematic export is a null; "mandated" is a need-test; no admitted line makes anyone compellable into the storm; the wind call is unadministrable and every instrument gives a loss a second answerer; no local prohibition has an author; no sanction is writable and blame is the one that exists; the dissent sits inside each person.

## Round 2 — `triple_read_verify.py`, raw output (header and verdict lines; the 174 passing "all fields match ground truth" lines and the 58 file headers are counted, not repeated)
```
required files: 58
agents: agent1, agent2, agent3
=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
EXIT=0
174
```
*(Before the real run, each reader's proofs were checked alone by the verifier with that reader in all three slots: A, C — UNANIMOUS. Reader B was checked in the real three-way run.)*

## Round 3 — peer cross-check (reply-only, via `SendMessage`)
| Reader | vs | Verdict | One-sentence reason |
|---|---|---|---|
| A | B | **CONSISTENT** | the same material read; two quotations cross lines, a few [D] items run firm, PA-44's "order of arrival" and a "foreman" row invent practice — all demotable |
| A | C | **CONSISTENT** | the chamber loop contradicts `RP` L409 and spec L176; "lethal in effect" overstates; everything else tagged |
| B | A | **CONSISTENT** | the faults are small: "two independent files", `MED` L89 as corroboration, "must outlive", the keepers' leverage |
| B | C | **CONSISTENT** | four [D] stretches (the chamber chain, the record's Register entry, "lethal", "assigned from outside") need correction |
| C | A | **CONSISTENT** | every quotation verbatim (226 checked); an off-by-one citation and three overreaching [D] statements |
| C | B | **CONSISTENT** | every quotation verbatim (272 checked); one mischaracterized source and several [D] items stated too firmly |
**6 / 6 CONSISTENT → gate met.**

**Dispositions (merge; the three readers conceded to one another on almost every point):**
- **Axis:** B's "Claims without an arbiter" (A and C conceded; B conceded A's wind clause as a sub-axis: calls by position).
- **Staffing:** both bases shown; C's difficulty-adjusted figures are the model's own accounting (checked by all three at `DOI8` §7.1 and `D16` L127–128).
- **Chamber chain:** `P5` P5-15's wording only; "nearly every city" and "the loop closed" withdrawn by C; the loop is RF-4.
- **Harbor watch:** conditional (free or baseline); B withdrew the unconditional placement.
- **Seeds:** asking keeper kept as a seed; book-followers reserved; A withdrew the keepers' "structural leverage" from the body.
- **Framing:** the three scales lead; four sources of right; the fast/slow grid is the second-order structure.
- **Treaty:** only the four named articles plus one [DRAFT] row; I.2, IV.3, V.1 rows dropped; VI.1–VI.3 demoted.
- **C's P7-3 third order:** cut to two checkable points (the wind has no Register industry; the record has no named tier).
- **Strikes** (Snag 13 of the phase file): the number "two persons", the ratios, "order of arrival", "foreman", "capacity", "assigned from outside", "must outlive", the household-language line, the heat finding, "lethal in effect", the 57,001 figure, the 47,469 attribution, and the cross-line quotations.

## Merge (§N.2 as amended, `M-246`)
- **Credits (single-reader finds kept, by finder):**
  - **A:** the 0.5 weight is not a vote (P7-1); the freedom-margin arithmetic (P7-2); the three-question test (P7-14); the hub's hidden maintenance decision (P7-14 row 12); CAND-1…CAND-6; the "handoff, not a penalty" sanction reading (P7-38).
  - **B:** the Sweep as a coverage gap (P7-11); the three scales (P7-13); the prohibition table (P7-21); "no executioner and no appeal" (P7-39); the LAW G null (P7-3); S7 as book-followers (RF-7); the `FTS` L49 reading of the subnets.
  - **C:** both staffing bases and the coefficient gap (P7-9); the free-tier lower bound (P7-9); the fast/slow grid (P7-20); the sources of legitimacy (P7-13); the harbor watch's call as RF-8; the `Q-65` finding that §20's Industrial basis cell cites the barred vision note.
  - **All three:** the R-24 resolution and its downstream table (27 rows, the union; every line verified).
- **Quotation pre-check by script:** 269 distinct quotations tested against the 58 admitted sources.
  - **243 verbatim.** 26 are not source quotations: the orchestrator's own axis labels, the phrases struck in Snag 13–14, a hook line, and three fragments from the Phase 4 and 5 merge-provenance tables (outside the readers' admitted ranges; verified directly by `grep`).
  - **Line anchors:** 133 quotation-and-citation pairs checked; 103 sit at the cited line, and the other 30 were heuristic artifacts (the cite following a quotation belonged to the next phrase on the line); each phrase was separately confirmed.
  - **SOC:** all 15 codes in the file exist in `SOC_Table_of_Contents.md`.
  - **0 real misses after fixes.**

## Snags in this round (the recording law)
- **Two readers displayed non-admitted lines** inside contiguous reads (spec L4, L9, L59, L84, L99; `Ports.md` L537). None was used; both readers said so. *Observation:* a range of many small spans (the spec's contract spans) invites a whole-file read; the displayed lines are the exposure.
- **C extracted its PROOF lines by script** after reading each file, "for exactness". Round 2 cannot tell the difference: the proof passes either way. C also read every file with the Read tool (recorded in its Snag 12), so reading happened; but a script-extracted proof no longer *proves* reading. **Recorded as `M-249`: the brief template should say the PROOF fields are copied from the reader's own reading, never produced by a script (awaits your OK).**
- **The deciding fact was found by a peer, not by the author.** Two readers' staffing rows (A4, A5) used the raw national coefficient; the third applied Mirny's difficulty. All three agreed in Round 3 that the third was right. *Recorded as `M-250`:* a number a reader computes from a coefficient table is exactly the kind of claim Round 3 should recompute.
- **Two registry findings** came out of the reading and are docketed, not fixed: `Datasheets/Phase_7.md`'s stale anchors into `16` and its vision-note row (`M-251`), and the superseded `01` still on the spine's MUST-OPEN list (`M-252`).
- **The list was heavy** (932 KB; about 30 % above Phase 6). All three readers finished; none ran out of context.
- **Plan mode was turned off by the developer at 07:29 and back on at about 07:35**, with the readers running. The required list was copied into the pass folder in that window; the readers wrote to the scratchpad throughout.
- **Hook notices** to run graphify arrived in every session on essentially every tool call; nothing was run (`DR-6`).

## Post-write checks — raw output, pasted unedited

**Triage (by hand, as each tool asks):**
- **Quotation audit.** It audits the whole pass folder with the pass's own files excluded from its corpus, so quotations of the pass's own earlier files and connective prose between adjacent quotations show as misses by design. Of the 82 lines it lists for `04_Phase_07_Order.md`: (a) phrases quoted from the pass's own files (`02_Spine`, `03_Research`, Phases 2–6 — e.g. the `RES` and `SPN` lines on the wind, the `P4` and `P5` lines on the stop and the relay); (b) the cells of the 27-row downstream-effects table, which quote the earlier Mirny files on purpose; (c) connective prose captured between two adjacent quotations (receipt and sweep rows, the Snag 13 and 14 lists). The pre-write script check (269 distinct quotations against the 58 admitted sources, including the admitted ranges of the pass files) found every real source quotation verbatim; the 26 it did not find are the orchestrator's own labels and the phrases struck in Snag 13–14. **0 real misses.**
- **Handoff audit:** *INSTRUMENT VALID: NO*, as at Phases 5 and 6 (its detector found no outbound "HANDED FORWARD" blocks, so it cannot discriminate). It reports Phase 7's sweep as FORMAL with 39 table rows; the 38 inbound rows are enumerated in the phase file.
- **Phase discipline:** T4 present in 6 / 6 phase files (Phase 7's marker names substantive shed items, read by hand). T5's early marker is present (Phase 6); its late marker waits for Step 8. The Position-Coverage Ledger shows the Ruler and Mentor cells blank at P7: bookkeeping only, nothing was written toward them (`00f` Rule 3).

### quotation_audit.py
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 5128   chars: 48,538,957

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 563
NOT FOUND in corpus: 311
  of those, in TABLE CELLS : 76
  of those, in PROSE       : 235

  [00.1_Step_MINUS-1_Input_Contract.md:15]           is now present, by ruling (hard canon, rb l2786): the founders were exiles from russia, china and australia. the spec's
  [00.1_Step_MINUS-1_Input_Contract.md:15]           (l150 chars 702-716) is consistent with the ruling as one of three stocks
  [00.1_Step_MINUS-1_Input_Contract.md:296]  [CELL]  daylight value) 1-63 and 114-144 3-0 (r3); 64-113 held (c dem a, b adm)
  [00.1_Step_MINUS-1_Input_Contract.md:296]  [CELL]  is computed from latitude (l126), independent of the note
  [00.1_Step_MINUS-1_Input_Contract.md:325]  [CELL]  ) is grammatically tied to the contested head. 125-240 uses the operator's
  [00.1_Step_MINUS-1_Input_Contract.md:389]  [CELL]  g6 deferred corpus-wide - do not report it as a gap
  [00_Frame.md:32]           i need you to ask me before changing anything
  [00_Frame.md:122]           ( 01 l113-119), and no admitted in-frame fact gives mirny
  [00_Frame.md:179]           its own census total, 32,026,600 ( cen l540; tl l327
  [00_Frame.md:277]  [CELL]  (l108); ossuaries are sacred and untouchable (l122-137); the mortuary question
  [00_Frame.md:330]  [CELL]  round 2 unanimous (15 / 15) round 3 all six consistent
  [00_Frame.md:331]  [CELL]  coverage: mirny.md 1-230, no gaps, no overlaps
  [00_Frame.md:336]  [CELL]  mirny's own frame declaration has not been written
  [00_Frame.md:338]  [CELL]  ( ext l542) ext l615; arithmetic holds for mirny. internal count mismatch
  [00_Frame.md:345]  [CELL]  an rwbem step; under the 2026-09-29 ruling the ulm's own step 3.7 creates it docket. l3-4
  [00_Frame.md:346]  [CELL]  all cells blank - mirny's ulm pass has not yet reached phase 2
  [00_Frame.md:348]  [CELL]  undetermined: whether the planetary split brain falls inside the frame
  [00_Frame.md:349]  [CELL]  if post-war, the whole frame has cross-subnet links through the hub
  [00_Frame.md:395]  [CELL]  as the settled name; deriving meaning from the word or from the demoted
  [00_Frame.md:498]           whr l69, l122: the tower's destruction in the war is
  [00_Frame.md:502]           closes the two-pass risk does not arise l483-484's
  [00_Frame.md:507]           as in-frame g6 material; cen l592 names this one (
  [00_Frame.md:523]           tl l348-349), not the grand-timeline act ( rb l2256-2259). (c; a and b withdrew
  [00_Frame.md:524]           ) the two act-1 windows end within 5 years of each other, but tl also places
  [00_Frame.md:526]           2564 founding census i ( 2671-2676); no year; act open
  [00_Frame.md:562]           substitute under your cst/rwbem ruling. 01 l500 routes it
  [03_Research.md:33]           the sky tells the truth in a language nobody at the founding had learned
  [03_Research.md:85]           well known to greenlanders, but not well studied by scientists
  [04_Phase_02_Composition_and_Arrival.md:78]           half of it could, and that half is marked as national
  [04_Phase_02_Composition_and_Arrival.md:174]           ( rp l67) and die in incidents ( rp l103-107); the gel brain's data
  [04_Phase_02_Composition_and_Arrival.md:184]  [CELL]  placement follows the robots' (ii.3.2). the rotation clock is inverted: no one leaves (iv.2.3). later work postings: cannot be rea
  [04_Phase_02_Composition_and_Arrival.md:185]  [CELL]  (l19). the only text for humans seeking refuge is the preamble's
  [04_Phase_02_Composition_and_Arrival.md:185]  [CELL]  (l23), a register (l134, l138). not shown, not ruled out. fits, at the federation level, not at mirny. war since 2563 (l19), perso
  [04_Phase_02_Composition_and_Arrival.md:185]  [CELL]  is scaffold-tier ( ftr l17), never treaty text ( ftd l134). gratitude and resentment in one population: gratitude has an admitted 
  [04_Phase_02_Composition_and_Arrival.md:185]  [CELL]  rp l360); resentment is only implied (v.2, l89: assistance is not
  [04_Phase_02_Composition_and_Arrival.md:186]  [CELL]  in tepenia ( rp l397); act 2 makes origin
  [04_Phase_02_Composition_and_Arrival.md:188]  [CELL]  none compelled (ii.2.4). the echo is permanence (iv.2.3), but in assembly territory, not at mirny. does not fit as a sentence: ii.
  [04_Phase_02_Composition_and_Arrival.md:210]           recognizing it would give mirny its first loss with someone to answer for it
  [04_Phase_02_Composition_and_Arrival.md:293]  [CELL]  mirny trusts what is written and what is relayed
  [04_Phase_02_Composition_and_Arrival.md:407]           the place as sinister, a trap, or secretly awful
  [04_Phase_02_Composition_and_Arrival.md:504]           definition (australia only) meant to constrain the order of the founding stocks, or only to mark a nation that preceded larger com
  [04_Phase_02_Composition_and_Arrival.md:515]           l393 (so frm 's con l387/l388/l393 cites are off by two). cen l4, l33, l36 and the treaty, nns , rp (other) and spine anchors held
  [04_Phase_02_Composition_and_Arrival.md:547]  [CELL]  is the weight model, not a datum; 8/3/1 not on any admitted census line
  [04_Phase_03_Surface_and_Texture.md:141]           tells the truth in a language nobody at the founding had learned
  [04_Phase_03_Surface_and_Texture.md:168]           adm l142 . the warm months are not the safe months: december and january average highs are above freezing ( 0.4, 1.1 c) with
  [04_Phase_03_Surface_and_Texture.md:197]           (l13), capacity falls to 50-60 % by -20 c, and a robot is safer moving than resting (l15-16). exposure is
  [04_Phase_03_Surface_and_Texture.md:222]           the entry is the first designed thing a visitor meets
  [04_Phase_03_Surface_and_Texture.md:449]           ) stands. not adopted: the research says the katabatic dies 8-15 km offshore and that the ice is not beyond the cyclones
  [04_Phase_03_Surface_and_Texture.md:487]           (no admitted line says the air is dry) passages along the wind as
  [04_Phase_03_Surface_and_Texture.md:487]           the visitor's picture arrives through the relay
  [04_Phase_03_Surface_and_Texture.md:487]           (kept only as a conditional) the reading of
  [04_Phase_03_Surface_and_Texture.md:487]           as the typical resident's time budget hwy 110's position relative to the settlement
  [04_Phase_03_Surface_and_Texture.md:487]           (kept corr only) fine hand-work in the lit weeks and coarse in winter (kept d , not a finding) the solar-geometry finding (reserve
  [04_Phase_03_Surface_and_Texture.md:506]           in p3-1 should read 29 lit days (found by phase 4 reader b; the canon midnight-sun span is about 29 days, and the other uses in th
  [04_Phase_04_Ordinary_Life.md:74]           conflicts with phase 3 b.0, exposure is a gradient, never a gate)
  [04_Phase_04_Ordinary_Life.md:80]           subnet hub; quarrying; processing construction materials; manufacturing infrastructure-maintenance machinery; the near-exclusive r
  [04_Phase_04_Ordinary_Life.md:103]           (l334); the human's is the ordinary one and no file states it. the gloss that follows in rp (the polar night falls on a population
  [04_Phase_04_Ordinary_Life.md:138]           so the midnight sun and the 2.4-hour june change nothing about the plate or the recharge; the one sun-using tier
  [04_Phase_04_Ordinary_Life.md:144]           mirny carries its losses as weather, as personal carelessness, or as quiet under-reporting
  [04_Phase_04_Ordinary_Life.md:149]           leisure is a condition of remaining sane; overwork is
  [04_Phase_04_Ordinary_Life.md:151]           a household or community that included a robot
  [04_Phase_04_Ordinary_Life.md:242]           no dusk ends the day in the one season that permits outdoor work
  [04_Phase_04_Ordinary_Life.md:242]           is the spine's reading, not an admitted line, and strains rp 's gradient (outdoor work is permitted by preparation in every month)
  [04_Phase_04_Ordinary_Life.md:246]           corrected 2026-10-03 to the prudent default (the cold file lists three options); residual unsoftened phrases remain in p3 : e's
  [04_Phase_04_Ordinary_Life.md:360]           (an assumption that a gust front travels at the mean wind) the free share
  [04_Phase_04_Ordinary_Life.md:360]           as a care figure and replacement-per-year figures smoking as a plume that exists only in still air, a lee dug out for a pleasure k
  [04_Phase_04_Ordinary_Life.md:360]           morning and evening attach to the rest, not the sun
  [04_Phase_05_Relation_and_Geometry.md:46]           air 's present-day framing as a frame and air l61's tally) crd l324's real station (gps) crd l330's founders ( dr-9 , superseded b
  [04_Phase_05_Relation_and_Geometry.md:46]           (comparison) cnc l116-118 / l283-285, l194-196 / l269-270, l286-288 / l478-479 (comparisons; one clause survives, 5e) the withheld
  [04_Phase_05_Relation_and_Geometry.md:46]           and every per-nation figure ( dr-12 ) air l18's chamber-city count (a count-ranking; only
  [04_Phase_05_Relation_and_Geometry.md:48]           ) mortuary content ( rv-4 ) the official name ( rv-1
  [04_Phase_05_Relation_and_Geometry.md:53]  [CELL]  when the relay fails, how long does the subnet stay cut off, and who restores contact
  [04_Phase_05_Relation_and_Geometry.md:57]  [CELL]  verified, not supported: hwy l204 makes concordia
  [04_Phase_05_Relation_and_Geometry.md:88]           adm l176 ); everything mirny receives from beyond the continent arrives through a sea that
  [04_Phase_05_Relation_and_Geometry.md:88]           adm l57 , whose break-up varies over 83 days and freeze-up over 48 ( res 3 corr ), and where
  [04_Phase_05_Relation_and_Geometry.md:88]           adm l143 . and one wind sits on both sides of the ledger: it shuts the inward window and degrades the outward relay
  [04_Phase_05_Relation_and_Geometry.md:89]           mislabels a relay that carries signal both ways
  [04_Phase_05_Relation_and_Geometry.md:105]           a russia-, china- and australia-founded tepenian city
  [04_Phase_05_Relation_and_Geometry.md:105]           is a question, not a choice made here (q-46). (4) dr-47 : the subnet's colloquial name
  [04_Phase_05_Relation_and_Geometry.md:105]           now has an in-world basis, partly superseding dr-13 's
  [04_Phase_05_Relation_and_Geometry.md:108]           internal relay routing (l184 chars 487-549) and road and infrastructure supply (l174 chars 272-623)
  [04_Phase_05_Relation_and_Geometry.md:138]           a pause at the hub is a pause for every node, so maintenance is done live or deferred
  [04_Phase_05_Relation_and_Geometry.md:139]           (iii.1) is the eight other members whose contact mirny carries - so a request for redundancy would run from the server to the serv
  [04_Phase_05_Relation_and_Geometry.md:147]           predates dr-46 / dr-47 , and states no ground for
  [04_Phase_05_Relation_and_Geometry.md:147]           the reading on which both of its examples are non-matching is the real station's nationality, a gps premise ( nns ; dr-19 ) - so n
  [04_Phase_05_Relation_and_Geometry.md:153]           cites a file outside this set, and tl l76 and l492 now mark the arcanet's place under shape d
  [04_Phase_05_Relation_and_Geometry.md:159]           stands ; shape d only marks where a second channel could be written (rf-4; q-47). whether that chain's practice carries any stock'
  [04_Phase_05_Relation_and_Geometry.md:164]           a place chosen by no one has no chooser to answer for its costs
  [04_Phase_05_Relation_and_Geometry.md:177]  [CELL]  ( crd l330 - the hedge carried); australia staging out of hobart/fremantle as
  [04_Phase_05_Relation_and_Geometry.md:187]           ( geo l98); geo 's heading for the six
  [04_Phase_05_Relation_and_Geometry.md:196]           are willing to do business with tepenia at all
  [04_Phase_05_Relation_and_Geometry.md:196]           anti-robot sentiment that drove the falkland treaty exile in the first place, is unresolved
  [04_Phase_05_Relation_and_Geometry.md:202]           ): res 4 records three ways storms attack a radio relay - static from blowing snow, rime icing (
  [04_Phase_05_Relation_and_Geometry.md:202]           high-latitude radio blackouts lasting hours to days
  [04_Phase_05_Relation_and_Geometry.md:202]           no admitted line turns degradation into an outage duration. tl 's chain availability estimate (
  [04_Phase_05_Relation_and_Geometry.md:203]           name is withheld-source and not an input). the hardware is at mirny adm l184 , so restoration falls to people at mirny, of whateve
  [04_Phase_05_Relation_and_Geometry.md:205]           at mirny the storm that breaks the relay also stops people walking
  [04_Phase_05_Relation_and_Geometry.md:210]           and its whole-network scope go beyond the spec (
  [04_Phase_05_Relation_and_Geometry.md:232]           those who fail without it include the adult arrival of either body , who learned the wind by neither descent nor a teacher
  [04_Phase_05_Relation_and_Geometry.md:242]  [CELL]  ( crd l330, hedged); or an intra-tepenian coastal freighter ( twr l955, a design calculation) from the start: at the treaty
  [04_Phase_05_Relation_and_Geometry.md:242]  [CELL]  ( dr-50 ) - so mirny's founders, in both bodies, arrived by sea d on ind , by
  [04_Phase_05_Relation_and_Geometry.md:242]  [CELL]  (ii.2.1 draft ); only in the unschedulable window and not while katabatic events close the harbor. which tepenian ports receive pe
  [04_Phase_05_Relation_and_Geometry.md:247]  [CELL]  ); prt 3d; dr-50 whether the transfer role continues into the second interwar period is open ( prt l278) - count of stocks, not pe
  [04_Phase_05_Relation_and_Geometry.md:247]  [CELL]  (which ueic l565's own remark applies to thailand, vietnam, the philippines and malaysia) - ten of fourteen fall in a named span; 
  [04_Phase_05_Relation_and_Geometry.md:262]           ). 2nd. the road is administered mostly from the center, but
  [04_Phase_05_Relation_and_Geometry.md:263]           adm 361-383 ; hwy l204 says concordia is
  [04_Phase_05_Relation_and_Geometry.md:263]           crd l28 records the 2026-07-06 correction; crd l158 (casey's entry) still reads
  [04_Phase_05_Relation_and_Geometry.md:263]           the spec's phrase matches the pre-correction wording; the frame's feature list (
  [04_Phase_05_Relation_and_Geometry.md:266]           (l366), which for a robot also answers the recharge default ( p4 p4-1); and the departure is decided by the wind, so
  [04_Phase_05_Relation_and_Geometry.md:273]           mirny can always be reached by signal and only sometimes in person
  [04_Phase_05_Relation_and_Geometry.md:279]  [CELL]  a misjudged crossing is carried as the person's own
  [04_Phase_05_Relation_and_Geometry.md:295]           no forced fit ( prt l363). recorded as d
  [04_Phase_05_Relation_and_Geometry.md:295]           leans constructed in its seasonal-offload sense; the deciding fact - whether any rock at mirny shelters a berth - is unstated (r-5
  [04_Phase_05_Relation_and_Geometry.md:308]  [CELL]  are the materials' destination adm l174 none written none written not stated / crd l158 names mirny only as
  [04_Phase_05_Relation_and_Geometry.md:319]           ( crd l329; hwy l199). supply: all three receive australian freighter shipments on one coastal supply line - casey
  [04_Phase_05_Relation_and_Geometry.md:320]           ) are heritage-grounded ( dr-19 ), traced to a withheld source ( ccsr l125, l129; cnc l25-27) and post-war-framed . not an input. 
  [04_Phase_05_Relation_and_Geometry.md:320]           adm l184 . a shared founding stock - australia an exile group at mirny ( reg l57) and the founder of the other two by dr-47 's cou
  [04_Phase_05_Relation_and_Geometry.md:320]           never as a reason for shared culture, and never as identity in act 2 ; nns l93-97's divergence operator works on that stock at eac
  [04_Phase_05_Relation_and_Geometry.md:327]           harbor traffic is of goods and observers, not of returning residents
  [04_Phase_05_Relation_and_Geometry.md:328]           ( dr-48 ); trade stands on geography ( twr ), the exile group on dr-46
  [04_Phase_05_Relation_and_Geometry.md:358]           a second own-eras axis - before and after the subnet's arcanet connection - waits with it, and on r-11's dates
  [04_Phase_05_Relation_and_Geometry.md:533]           rows, corrected (docket, never applied): row 10's
  [04_Phase_05_Relation_and_Geometry.md:533]           ( crd l328 says it of mirny and l180 of davis; not used as a measure) row 12 drops crd l330's
  [04_Phase_05_Relation_and_Geometry.md:533]           row 14 quotes the old member name row 15's
  [04_Phase_05_Relation_and_Geometry.md:533]           is a count-ranking over a post-war list row 16 cites prt l221, l572, l628 (l221 is a quote-marker line in 3c; l572 and l628 are ou
  [04_Phase_05_Relation_and_Geometry.md:534]           is weaker than the frame recorded (b). the frame's window
  [04_Phase_05_Relation_and_Geometry.md:534]           ), which cites a withheld full extrapolation outside this set, and on a b-story reading that tl l492 and l76 now mark superseded (
  [04_Phase_05_Relation_and_Geometry.md:534]           ); tl l514-519 adds that local hub construction and the national buildout
  [04_Phase_05_Relation_and_Geometry.md:535]           mirny vs reg l57 and dr-47 (q-52); (vii) tl 's order puts the subnet-by-subnet connection before hwy 22 reaches the pole, while th
  [04_Phase_05_Relation_and_Geometry.md:535]           and the junctions index ( hwy l271-286) lists none (r-58); (xi) crd l328 and l180 both
  [04_Phase_05_Relation_and_Geometry.md:535]           neither load-bearing; (xiii) cnc 's header (the tower's completion connecting all six subnets
  [04_Phase_05_Relation_and_Geometry.md:535]           ) vs tl 's gradual connection - consistent as read; (xiv) geo l90-92 points to the empty power file, so its claim that it
  [04_Phase_05_Relation_and_Geometry.md:539]           at any hour the residents awake are the standing exception
  [04_Phase_05_Relation_and_Geometry.md:539]           (it lies in another subnet) the hwy l30 analogy applied to the relay (withdrawn)
  [04_Phase_05_Relation_and_Geometry.md:539]           (narrowed to chambers made at sinheung) the harbor watch as first contact (to rf-16)
  [04_Phase_05_Relation_and_Geometry.md:539]           (now offered); in b - dr-21 read as a national supply (struck) the 11.8 % mandate as a parent requirement (demoted to context)
  [04_Phase_05_Relation_and_Geometry.md:539]           for a robot from upper earth (corrected to federation residence with placement by assignment) davis as
  [04_Phase_05_Relation_and_Geometry.md:539]           principal import port (it is tepenia's indian-ocean-sector port) sinheung placed
  [04_Phase_05_Relation_and_Geometry.md:539]           (it lies on hwy 4, short of the tri-junction)
  [04_Phase_05_Relation_and_Geometry.md:539]           in the body (to rf-2) p5-21's personhood sentence (made conditional on australia's assembly membership)
  [04_Phase_05_Relation_and_Geometry.md:539]           of crd l55 (softened); in c - the stone's route stated as adm (l176 gives the destination only) the early relay as
  [04_Phase_05_Relation_and_Geometry.md:539]           the overland reach to two members passes outside the subnet
  [04_Phase_05_Relation_and_Geometry.md:539]           ) composite quotations in handoff rows 18-20 (table cells joined inside quotation marks)
  [04_Phase_05_Relation_and_Geometry.md:539]           for crd l55 and the geographic-ground claim (withdrawn)
  [04_Phase_05_Relation_and_Geometry.md:541]           as an institution a mirny-davis port ranking
  [04_Phase_05_Relation_and_Geometry.md:541]           as a mirny product the sinian federation exiled mirny's founders (the treaty exiles robots as a class) mirny far enough from the n
  [04_Phase_05_Relation_and_Geometry.md:543]           attested on the road, unattested at the place
  [04_Phase_05_Relation_and_Geometry.md:543]           now defined by tpl l6 frm a.5's form of words and a.6's
  [04_Phase_05_Relation_and_Geometry.md:553]  [CELL]  one wind on both sides b (name), c (content, third-order clause) a and c conceded to b's name; b offered c's; c's
  [04_Phase_06_Meaning.md:14]           occurs 0 times in all six ) nh full icb0 , icb1 , icb3 , icb4 , icb7 , icb8 , icb9 (all full; 0 mirny mentions ; research only
  [04_Phase_06_Meaning.md:18]           three independent grounds, each sufficient (all three readers): (1) its only source is a path into background-lore/
  [04_Phase_06_Meaning.md:18]           /course of events/ - a vignette, never an input (developer ruling); (2)
  [04_Phase_06_Meaning.md:18]           is the retracted symmetric light model - the admitted spec gives
  [04_Phase_06_Meaning.md:41]  [CELL]  an observance of the open water could only be called on the day
  [04_Phase_06_Meaning.md:45]  [CELL]  the record is the only witness, and it can't name what it left out
  [04_Phase_06_Meaning.md:57]           the record is the only witness, and it can't name what it left out
  [04_Phase_06_Meaning.md:57]           ( spn l103 corr ). the person answers for crossings decided on cues that are honest and unread ( res l30 corr ), so a loss is
  [04_Phase_06_Meaning.md:58]           a; it names the compact's blind side, kept as p6-4
  [04_Phase_06_Meaning.md:65]           admitted-demoted; dr-28 : no meaning may be built on it ) l176 owed (an edit-history note, demoted) l142 must (inside the excluded
  [04_Phase_06_Meaning.md:69]           the record is the only witness, and it can't name what it left out
  [04_Phase_06_Meaning.md:69]           so mirny trusts what is written and what is relayed
  [04_Phase_06_Meaning.md:69]           the one cost that gives no failure signal when it lapses
  [04_Phase_06_Meaning.md:69]           each injury is read as the injured person's carelessness
  [04_Phase_06_Meaning.md:69]           a misjudged crossing is carried as the person's own
  [04_Phase_06_Meaning.md:69]           living witnesses to the arrival are robots; the heirs are humans born here
  [04_Phase_06_Meaning.md:85]           the book has the numbers and the wind has the say - if you went out, the call was yours
  [04_Phase_06_Meaning.md:87]           ( spn l137). it is not a creed - nothing is venerated, no invisible force is invoked
  [04_Phase_06_Meaning.md:90]           nothing says a born-here human reads the cue better than a built-here robot, or the reverse
  [04_Phase_06_Meaning.md:93]           ( res l30); (d) had residents chosen the site , a chooser would answer for its costs - at mirny there is
  [04_Phase_06_Meaning.md:93]           ( p2 l207). the conjunction does not travel; delete-the-name: survives. (c's shorter form
  [04_Phase_06_Meaning.md:96]           ( res l94). 2nd. so the only party in any crossing who can be wrong, on the files, is the reader; a loss is
  [04_Phase_06_Meaning.md:96]           the struggle is not fear of the wind but the privacy of the loss
  [04_Phase_06_Meaning.md:97]           the person best at surviving the wind has the least standing in the record
  [04_Phase_06_Meaning.md:97]           membership at mirny is conferred by exposure, not by welcome
  [04_Phase_06_Meaning.md:100]           the one cost that gives no failure signal when it lapses
  [04_Phase_06_Meaning.md:100]           the people who keep the relay up are invisible exactly while they succeed
  [04_Phase_06_Meaning.md:100]           no event teaches anyone at mirny that the warmth is delivered from elsewhere
  [04_Phase_06_Meaning.md:100]           so when a long-lived robot is lost the recollection goes with her
  [04_Phase_06_Meaning.md:104]           preserved journals, logs and orientation manuals (dr-7 yes)
  [04_Phase_06_Meaning.md:104]           ( con l387) - so it predates the founding and holds none of it. the persons who do
  [04_Phase_06_Meaning.md:104]           but a long-lived robot is a person to ask, not an archive
  [04_Phase_06_Meaning.md:106]           nobody who lives at mirny chose it; the one party the files name as founding it stands outside the country
  [04_Phase_06_Meaning.md:106]           ( p2 l258). the reading of the wind is one thing at mirny that nobody handed anyone
  [04_Phase_06_Meaning.md:106]           ( p4 l174) - and the compact's private clause protects it (b
  [04_Phase_06_Meaning.md:106]           in round 3). act 1: living human founders and founding robots are both witnesses; act 2: the first-person founding is a robot's
  [04_Phase_06_Meaning.md:110]           mirny is the one place in the subnet that knows what has happened, and it cannot tell anyone
  [04_Phase_06_Meaning.md:114]           the chambers made at sinheung are built from material mirny near-exclusively supplies
  [04_Phase_06_Meaning.md:114]           mirny's relation to the robot half of its own population is material and upstream, not cultural
  [04_Phase_06_Meaning.md:134]           the person who misjudged and the person who was lucky had the same cue
  [04_Phase_06_Meaning.md:137]           ( nns l106). what the thin layer shows d : three of four items are national or physical; what is mirny's own is how a shared condi
  [04_Phase_06_Meaning.md:143]  [CELL]  the hours that belong to nobody are hours nobody else has free
  [04_Phase_06_Meaning.md:157]           no in-frame disaster, discovery, migration or crime in the admitted set
  [04_Phase_06_Meaning.md:157]           is false for the human half : 665,901 humans at census i and a senescence that
  [04_Phase_06_Meaning.md:157]           mirny has human dead in every year of the frame d; no rate, no number (a). the others cannot be read; naming one would be the
  [04_Phase_06_Meaning.md:172]           so mirny trusts what is written and what is relayed
  [04_Phase_06_Meaning.md:175]           ( res l76; conditional - the relay's technology is not canon)
  [04_Phase_06_Meaning.md:175]           ( res l99); the record carries thresholds, not judgment. physical floor
  [04_Phase_06_Meaning.md:178]           ( spn l98) under-reporting at the hub ( spn l137) maintenance
  [04_Phase_06_Meaning.md:178]           ( spn 3 g5) staying in, interior-bound stretches
  [04_Phase_06_Meaning.md:178]           the one role that already makes live calls on wind
  [04_Phase_06_Meaning.md:178]           as weather, as personal carelessness, or as quiet
  [04_Phase_06_Meaning.md:182]           with no one intending it; res 's real-world case says the cure for a lost technique
  [04_Phase_06_Meaning.md:183]           a place chosen by no one has no chooser to answer for its costs
  [04_Phase_06_Meaning.md:188]           recognizing it would give mirny its first loss with someone to answer for it
  [04_Phase_06_Meaning.md:198]           a trained reader's judgment published as a marker and reset daily
  [04_Phase_06_Meaning.md:201]           the only things in the year that can be known in advance to the day are light-dated
  [04_Phase_06_Meaning.md:201]           no darkness beyond civil twilight for about 80 days (nov 11 jan 30)
  [04_Phase_06_Meaning.md:202]           an observance of them is a culture, not a necessity
  [04_Phase_06_Meaning.md:207]           break-up varies over 83 days, freeze-up over 48
  [04_Phase_06_Meaning.md:207]           the one role that already makes live calls on wind
  [04_Phase_06_Meaning.md:207]           an observance of the open water could only be called on the day
  [04_Phase_06_Meaning.md:342]           ) b's cand-obs-4 afternoon stop and residents
  [04_Phase_06_Meaning.md:342]           the warning (the warning stays unread) b's p6-12 assigning the fourth reason (to rf) b's
  [04_Phase_06_Meaning.md:342]           read as cloud (it is a precipitation figure) c's duty row resting on a hook proposal ( p5 l409) c's noon gathering facing north (i
  [04_Phase_07_Order.md:55]  [CELL]  rests on the retracted symmetric light model (the admitted spec spans give no polar night and about 29 days of midnight sun; frm d
  [04_Phase_07_Order.md:55]  [CELL]  come from a developer-vision note ( dr-10 : never an input; layout and amenity reserved); (c) the rename flag and the
  [04_Phase_07_Order.md:55]  [CELL]  name legend are rv-1 (name), dr-32 (namesake) and dr-19 / dr-25 (station lineage); (d) chain 2's
  [04_Phase_07_Order.md:55]  [CELL]  framing are developer-vision wording ( dr-10 ) - the chain itself stands on spec l174 chars 272-623. extension: the 20 lines that 
  [04_Phase_07_Order.md:57]  [CELL]  outputs) doir l49 and d16 l68-70 stamp 01 , 03 , 07 superseded (
  [04_Phase_07_Order.md:75]  [CELL]  re-date before any relation is written ( frm l227) d p7-7 (relation only; the chamber role is
  [04_Phase_07_Order.md:80]  [CELL]  later work postings: cannot be read (phase 7)
  [04_Phase_07_Order.md:92]  [CELL]  how a person moves between tiers is phase 7's
  [04_Phase_07_Order.md:108]  [CELL]  who would build one is phase 7's and is in no file
  [04_Phase_07_Order.md:123]           its wind half restates p4 q-42 and p6 p6-18, and mandated is the model's accounting term
  [04_Phase_07_Order.md:161]           (l2105), inside the section titled the roster pass
  [04_Phase_07_Order.md:161]           (l445), placed after the 37-row first-pass table (l241). (2) it names the omission itself
  [04_Phase_07_Order.md:161]           (l2126). (3) it records a developer ruling (c, 2026-09-02
  [04_Phase_07_Order.md:173]  [CELL]  the one role that already makes live calls on wind
  [04_Phase_07_Order.md:194]           d16 's own statement, not independently confirmed ind ; med l89 says what sinheung takes in (
  [04_Phase_07_Order.md:198]           the chambers made at sinheung are built from material mirny near-exclusively supplies
  [04_Phase_07_Order.md:242]           ( doi9 ), just nationally rather than locally, and the standard given is that
  [04_Phase_07_Order.md:262]  [CELL]  because the treaty structured them that way scaffold the other reading of pa-1 ; dr-17 rules
  [04_Phase_07_Order.md:281]           at every settlement; none is described for mirny. populations were assigned to stations by arrangements
  [04_Phase_07_Order.md:285]           ( hwy l27); the localized tier operates because its conditions
  [04_Phase_07_Order.md:298]  [CELL]  work in the wind and emergencies have no stay option
  [04_Phase_07_Order.md:299]  [CELL]  admits the hub can't hold alone under-reporting
  [04_Phase_07_Order.md:305]           not an early warning - no lead time is demonstrated - on a channel
  [04_Phase_07_Order.md:305]           ( res l30); whether a storm can be seen coming is not demonstrated at this coast ( res l34-36). storms last
  [04_Phase_07_Order.md:305]           no admitted file gives a public wind report, flag, alarm or scale
  [04_Phase_07_Order.md:317]           is the one place in the subnet that knows what has happened, and it cannot tell anyone
  [04_Phase_07_Order.md:317]           falls to people at mirny, of whatever institution
  [04_Phase_07_Order.md:317]           the storm that breaks the relay also stops people walking
  [04_Phase_07_Order.md:319]           ( cp l37; p4 p4-7) - volunteering prices differently by body. the compact meets its failure here: a culture that will not ritualiz
  [04_Phase_07_Order.md:319]           also loses its channel ( p5 p5-5: the parent
  [04_Phase_07_Order.md:323]           the one role that already makes live calls on wind
  [04_Phase_07_Order.md:334]  [CELL]  a misjudged crossing is carried as the person's own
  [04_Phase_07_Order.md:335]  [CELL]  the person best at surviving the wind has the least standing
  [04_Phase_07_Order.md:342]  [CELL]  with a mandatory randomized remainder robots themselves, post-exile (
  [04_Phase_07_Order.md:346]           (a hazard statement, spec l131); the harbor's closure (the wind, spec l143); the road's go/no-go (an authority to call, not a ban)
  [04_Phase_07_Order.md:349]           ( rp l69), and the two professions turn over for different reasons
  [04_Phase_07_Order.md:349]           no age-grade system, ru9 ), so succession at mirny runs on notice and choice , never on rank, seniority or descent. succession of 
  [04_Phase_07_Order.md:352]           ( p4 l149.) a rule overriding a person's own want to work would cut against law 1 , and the one admitted guard is medical, not reg
  [04_Phase_07_Order.md:352]           can come is a relationship: a mentor/mentee bond is
  [04_Phase_07_Order.md:355]           so the cost is a choice remade after every storm
  [04_Phase_07_Order.md:355]           it is the half of the wind that can be written down
  [04_Phase_07_Order.md:389]           ( p2 l225). two groups hold partial readings and each learned by doing - the quarry crews upwind (a report from inside the storm, 
  [04_Phase_07_Order.md:390]           it is the half of the wind that can be written down
  [04_Phase_07_Order.md:390]           ( res l125). not writable: the reading in the moment (how much loose snow lies upwind, how many days since snowfall, which of thre
  [04_Phase_07_Order.md:396]           when a long-lived robot is lost the recollection goes with her
  [04_Phase_07_Order.md:402]           a household or community that included a robot
  [04_Phase_07_Order.md:410]           work in the wind and emergencies have no stay option
  [04_Phase_07_Order.md:438]  [CELL]  has a written half (the record, the relay that
  [04_Phase_07_Order.md:450]           tendency - those who treat the record's thresholds as the only authority and are insulated from blame because
  [04_Phase_07_Order.md:453]           ( spn l143) - and the address of the big one is
  [04_Phase_07_Order.md:455]           ( spn l68) - is a leverage the compact's own grammar is against using (
  [04_Phase_07_Order.md:458]           the struggle is not fear of the wind but the privacy of the loss
  [04_Phase_07_Order.md:472]           ( spec l131); for a robot, charging below freezing is one of
  [04_Phase_07_Order.md:472]           ( cp l30-37) - spend reserve to warm the cells, charge 10-20 times slower and exposed throughout, or take
  [04_Phase_07_Order.md:472]           ( cp l63). outside waiting beside a road is
  [04_Phase_07_Order.md:490]           each injury is read as the injured person's carelessness
  [04_Phase_07_Order.md:650]           ). its own admitted lines (l1-80) carry no stamp - only
  [04_Phase_07_Order.md:651]           l2152-2158). its sweep citation (l23-26) is l24-28; its
  [04_Phase_07_Order.md:656]           which is in no admitted file; p5 p5-15 wrote the route
  [04_Phase_07_Order.md:662]           l35-36; d16 maritime l2155 l2156; half b's c source is
  [04_Phase_07_Order.md:662]           (a headcount beyond the division of industry's) the logic without the number; the 44.4 / 4.7 / 6.7 ratios and
  [04_Phase_07_Order.md:662]           the first authority was assigned from outside
  [04_Phase_07_Order.md:662]           (a death-class exposure cost for a human; three bad options and a permanent scar for a robot)
  [04_Phase_07_Order.md:662]           third order ( conditional); the 57,001 human-keyed non-food figure (it included c5 mortuary; 56,602 is used); the heat finding (a 
  [04_Phase_07_Order.md:662]           attribution to c6/c7/c8/d4 ( the coefficient gap only); treaty rows i.2, iv.3, v.1 and the vi.1-vi.3 finding ( one draft row and r
  [04_Phase_07_Order.md:673]  [CELL]  national mandate: 11.8 % of the workforce ( 16 l275) - its link to the stone is not stated
  [04_Phase_07_Order.md:674]  [CELL]  a national mandate of 11.8 % in the division of industry run
  [04_Phase_07_Order.md:675]  [CELL]  phase 7 (arrangements and any later postings; the 11.8 % mandate, r-24; r-13's lookup)
  [04_Phase_07_Order.md:676]  [CELL]  the 11.8 % mandate's link to the stone is not stated (r-24)
  [04_Phase_07_Order.md:677]  [CELL]  the parked mirny question: 11.8 % vs 23.6 %, a later item
  [04_Phase_07_Order.md:678]  [CELL]  the figure is used as the row states it; not resolved
  [04_Phase_07_Order.md:680]  [CELL]  the free tier can contain the headline function
  [04_Phase_07_Order.md:680]  [CELL]  which tier holds the quarry, the relay, the ring and the harbor watch is not stated
  [04_Phase_07_Order.md:681]  [CELL]  baseline 41.1 % mandated 11.8 % 52.9 %
  [04_Phase_07_Order.md:683]  [CELL]  row 41.1 11.8 47.1 100.0 ; baseline mandated 52.9 %
  [04_Phase_07_Order.md:684]  [CELL]  41.1 % and 11.8 % are averages over workforce units
  [04_Phase_07_Order.md:684]  [CELL]  how a person moves between tiers is phase 7's
  [04_Phase_07_Order.md:686]  [CELL]  an elective share under 47.1 % with the site's price charged to it
  [04_Phase_07_Order.md:690]  [CELL]  the hours spoken for: 52.9 % baseline plus mandated
  [04_Phase_07_Order.md:691]  [CELL]  has an unstated object and a parked base (r-24; fq-12)
  [04_Phase_07_Order.md:693]  [CELL]  dr-21 supply and the 11.8 % requirement struck
  [04_Phase_07_Order.md:694]  [CELL]  an elective share with the site's price charged to it
  [04b_T8_Rounds_Phase_2.md:101]           annotation vs dr-9 (iii) the treaty's status (iv) the arrival-mode verdicts (v) the
  [04b_T8_Rounds_Phase_2.md:115]           the notable tier's nations are southeast asian
  [04b_T8_Rounds_Phase_2.md:116]           as the treaty's ties (the quote includes a means ground the treaty lacks) c's
  [04b_T8_Rounds_Phase_2.md:116]           (rests partly on a personhood withdrawal that applies to robots, not humans; iv.2.1) b's
  [04b_T8_Rounds_Phase_2.md:116]           listed as a tier property (it is a property of the weight model) a's
  [04b_T8_Rounds_Phase_2.md:116]           for human fled (stronger than the files allow) a's
  [04b_T8_Rounds_Phase_2.md:123]  [CELL]  draft-tier is the safe outcome; substance confirmed, wording draft (b accepted the tiering split from a and c) conf / draft
  [04b_T8_Rounds_Phase_3.md:128]  [CELL]  with a sheltered core is admitted; closure, solidity, arcs, roofing are conditional d pa-15; q-38
  [04b_T8_Rounds_Phase_4.md:129]  [CELL]  no invented practice, no time budget; one over-reach noted: the axis word
  [04b_T8_Rounds_Phase_4.md:137]           recharge against a three-option cold table; three invented practices (a smoking plume, kinship by wind, near-miss retelling); a ti
  [04b_T8_Rounds_Phase_4.md:137]           a derived bias toward staying in) and real defects in already-written files: p3 l140's
  [04b_T8_Rounds_Phase_4.md:137]           (reader b, a unit slip that three phases of readers had passed), p3 's residual unsoftened recharge phrases after my first repair 
  [04b_T8_Rounds_Phase_4.md:137]           label (the m-151 trap, c2), and ds4 's header calling the row's percentages
  [04b_T8_Rounds_Phase_5.md:75]  [CELL]  a and c conceded to b, while b offered c's wording. a's objection that
  [04b_T8_Rounds_Phase_7.md:35]  [CELL]  the three scales (point / region / above) tied to ftd iii.1; the sweep's five absences as a coverage gap; the prohibition table

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

### handoff_audit.py
```
pass audited : Mirny
phase files  : 6

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  POSITIVE (detector must find a formal block): phases 2, 3, 4, 5, 6, 7
  NEGATIVE (detector must find nothing)       : phases none
  INSTRUMENT VALID: NO - detector never discriminated; DO NOT TRUST THESE VERDICTS

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      3 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      4 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      5 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      6 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      7 |        0 | FORMAL   |   39 | n/a - nothing addressed to it

TOTAL outbound handoff rows: 0
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 0

=== outbound rows, per target, for hand reconciliation ===
```

### phase_discipline_check.py
```
pass audited : Mirny

=== T3 - POSITION-COVERAGE LEDGER ===
  phases in header: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Child              filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Lover (position)   filled=1  blank=8   blank at: P2, P3, P5, P6, P7, P8, P9, P10
  The Parent             filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Ruler              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Elder              filled=1  blank=8   blank at: P3, P4, P5, P6, P7, P8, P9, P10
  The Mentor             filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Passer-Through     filled=1  blank=8   blank at: P2, P4, P5, P6, P7, P8, P9, P10
  The Neighbor           filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10

  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).

=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the axis had no use for the Chose it attract/repel analysis at Mirny, the Inherited it and
  [04_Phase_03_Surface_and_Texture.md]  T4 present: this phase's axis had no use for smell (no admitted input), interiors and building fabric 
  [04_Phase_04_Ordinary_Life.md]  T4 present: this phase's axis had no use for dwellings and amenity layout, a shift roster, an intracit
  [04_Phase_05_Relation_and_Geometry.md]  T4 present: this phase's axis had no use for rivalry (none recorded), 5b's sibling form, the per-natio
  [04_Phase_06_Meaning.md]  T4 present: this phase's axis had no use for the roster's denominational strongholds, aesthetics, nume
  [04_Phase_07_Order.md]  T4 present: this phase's axis had no use for the Federation's own form of government above the region,

  6/6 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 6 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: Alive in its conditions and its two bodies — a working coast that keeps nine places talking without being thanked, where people stop together, own their own calls, and get a sunset with no night after it and an open sea nobody can promise — and lovable by someone who wants to be trusted with their own reading; but what its people laugh at and do with their own hours is still the largest empty slot, so for now the love is for how the place holds its conditions more than for any custom it is known to keep (an early, provisional verdict; it must not steer Phases 7–8, or it is falsified and withdrawn).
  LATE marker absent (08_Review_Panel.md missing or has no Lover-faculty line yet)

  T5 not fully applied this pass (one or both markers absent).
```
