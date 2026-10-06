# Mirny — Step 4 · Phase 6 · T8 round record

**Pass:** Mirny · ULM · Step 4, Phase 6 (Meaning) · 2026-10-05.
- **Clock checks:** 12:31, 12:33, 13:03, 13:06, 14:11, 14:29, 14:31.
- **Round 1:** dispatched about 12:34.
- **Round 2:** 13:06.
- **Round 3:** sent about 13:10; the replies arrived across the usage-limit pause.
- **Merge:** written 14:11–14:31. Phase 6 was started before 13:59, so it is finished inside the window.

**Files:**
- **Written:** `04_Phase_06_Meaning.md`.
- **Required list:** `.t8_required_04_Phase6.txt` (34 entries, 6,655 admitted lines; `00_Frame.md` and `04_Phase_03` admitted at ranges).
- **Reader outputs:** staged in the readers' own plan files, because plan mode was active when they finished. Not canon, not an input; they archive with the pass (`DR-27`).
  - `~/.claude/plans/linked-growing-tarjan-agent-a5ea3ce5e152a7aca.md` (A, 756 lines)
  - `…-a27dfe6b5af1394c8.md` (B, 740 lines)
  - `…-af9ad85a22e49e3ca.md` (C, 725 lines)

## Round 0 — the required-reading list
- **Sources:** the Phase 6 `MUST OPEN` block (`03_The_Phase_Spine.md` L757–775) and the runbook's §C.8c row 6.
  - The §C.8c row adds `The_True_Believer_Extraction.md` and `The_Meme_Machine_Extraction.md`, which the spine's block omits.
  - Also added: the Pre-Trip's T5 rule (L518–526); `DR-8`, `DR-25`, `DR-26`; Robot Physiology's death and leisure ranges (L71–190, L329–374).
- **Orchestrator-verified empties:** four of six roster folders.
- **The brief named ten traps**, including:
  - the `National_Holidays.md` Mirny entry: a vignette source, post-war framing and the retracted light model;
  - `RV-4`;
  - observances as candidates;
  - no forced faith in either direction.
- **Reader C's first dispatch got no classifier verdict and was re-sent once, as-is.**

## Round 2 — `triple_read_verify.py`, raw output (header and verdict lines; the 102 passing "all fields match ground truth" lines and the 34 file headers are counted, not repeated)
```
required files: 34
agents: agent1, agent2, agent3
=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
EXIT=0
102
```

## Round 3 — peer cross-check (reply-only, via `SendMessage`)
| Reader | vs | Verdict | One-sentence reason |
|---|---|---|---|
| A | B | **CONSISTENT** | grounds check out; one overclaim to soften ("only" → "one") |
| A | C | **CONSISTENT** | nothing fatal; four demotions (L150 beyond the permitted phrases, a hook used as a premise, an invented gathering, "for minutes") |
| B | A | **CONSISTENT** | two removable slips: the Christmas date, and the calm's "nothing to read" |
| B | C | **CONSISTENT** | re-grounding and demotions only, no contradiction |
| C | A | **CONSISTENT** | the calm overclaim and a stop-timing slip; no reservation breached |
| C | B | **CONSISTENT** | one overclaim about what residents know, and one stop-timing slip |

**6 / 6 CONSISTENT → gate met.**

**Dispositions (merge; details in the phase file's Snags 5–6):**
- **Axis:** B's "The medium holds; the person answers". A and C conceded.
- **Name sentence:** B's, scoped to the keepers for its relay clause, with A's as the alternate.
- **The calm:** reserved, RF-15.
- **The treaty day:** relation plus RF-12 (crossed concessions, so the conservative reading).
- **Not mourned properly:** a null; C's cases go to RF-11.
- **Borrowed Form:** fires at §D as the compact's dissent, as [D] not adopted; in §E it is resemblance only.
- **The refusal:** a union of all three readers' mechanisms.
- **L150:** narrowed to `CON` L387 and `NNS` L21.

## Merge (§N.2 as amended, `M-246`)
- **Quotation pre-check by script:** 128 italic quotations against the 34 sources.
  - One regex artifact: the `ICB0` quote, confirmed separately.
  - Two italicized copies of a struck reader phrase, changed to plain quotation marks.
  - **0 real misses.**

## Snags in this round (the recording law)
- **Plan mode during Round 1.** Plan mode was active when the readers finished, so all three staged their outputs in plan files, and the verifier read them there.
- **The usage-limit pause.** The developer's usage limit was reached during Round 3.
  - The checkpoint was saved in the session plan file.
  - The merge resumed at 14:11, inside the window.
- **Hook notices** to run graphify arrived in all sessions; nothing was run (`DR-6`).

## Post-write checks — raw output, pasted unedited

**Triage (by hand, as each tool asks):**
- **Quotation audit.** It audits the whole pass folder, with the pass itself excluded from its corpus. So quotations of the pass's own files and connective prose between adjacent quotations show as misses by design. The pre-write check above found every italic quotation in the Phase 6 file verbatim in its sources.
- **Handoff audit:** *INSTRUMENT VALID: NO*, as at Phase 5. The inbound sweep is enumerated in the phase file instead.
- **Phase discipline:** T4 present in 5 / 5 phase files. T5's early marker is now present (Phase 6); its late marker waits for Step 8.

### quotation_audit.py
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 5041   chars: 41,977,284

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 425
NOT FOUND in corpus: 228
  of those, in TABLE CELLS : 41
  of those, in PROSE       : 187

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

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

### handoff_audit.py
```
pass audited : Mirny
phase files  : 5

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  POSITIVE (detector must find a formal block): phases 2, 3, 4, 5, 6
  NEGATIVE (detector must find nothing)       : phases none
  INSTRUMENT VALID: NO - detector never discriminated; DO NOT TRUST THESE VERDICTS

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      3 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      4 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      5 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      6 |        0 | FORMAL   |    0 | n/a - nothing addressed to it

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

  5/5 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 5 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: Alive in its conditions and its two bodies — a working coast that keeps nine places talking without being thanked, where people stop together, own their own calls, and get a sunset with no night after it and an open sea nobody can promise — and lovable by someone who wants to be trusted with their own reading; but what its people laugh at and do with their own hours is still the largest empty slot, so for now the love is for how the place holds its conditions more than for any custom it is known to keep (an early, provisional verdict; it must not steer Phases 7–8, or it is falsified and withdrawn).
  LATE marker absent (08_Review_Panel.md missing or has no Lover-faculty line yet)

  T5 not fully applied this pass (one or both markers absent).

```
