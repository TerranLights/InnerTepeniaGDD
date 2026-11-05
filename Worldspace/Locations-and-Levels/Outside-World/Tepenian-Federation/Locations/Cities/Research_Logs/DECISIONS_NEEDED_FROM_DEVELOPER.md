# Decisions needed from the developer (running list)

**What this file is.** Every question that needs the developer goes here, written in plain language with the facts, so he can read them all in one sitting later. **Automatic runs (the Mirny repass cron) never stop to ask; they write the question here, continue on the recommended answer, and mark the affected result PROVISIONAL with the decision's number.** When the developer answers, the answer is recorded here, filed as a numbered ruling in `Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`, and the provisional results are confirmed or redone.

**Entry format** (copy this, number the next `DEC-nnn`):

```
### DEC-nnn · OPEN · <date> · <which unit or file raised it>
**The question, in plain words:** <one or two sentences; no internal labels (no Q-74, AQ-17, DR-numbers as the thing being asked)>
**The facts:** <what the sources say, with file and line>
**Options:** A) ... B) ... C) ...
**Recommendation:** <which option and why>
**What is waiting on it / what was done provisionally:** <files, results marked PROVISIONAL (DEC-nnn)>
**Answer (developer):** <blank until he answers>
```

---

## Open since 2026-11-03

### DEC-001 · OPEN · 2026-11-03 · Esperanza
**The question, in plain words:** Part of Esperanza's 1,200,000 people live on the Ulu Peninsula (James Ross Island) as a second site. How many, and how do they get across the water?
**The facts:** The Ulu Peninsula has about 250 km² of ice-free ground and is 74 km from Esperanza Base; the channel is 8–24 km wide, and the ice masks come within 9.4 km at 63.93°S 58.27°W, far south of Hope Bay (`Research_Logs/Esperanza_Extent_Research_2026-11-03.md`). The Tabarin ice alone has room for the whole city (120–171 km² needed of 428 km² of grounded ice).
**Options:** A) a small share (a research and port settlement) · B) about half · C) most of the people, with Hope Bay's head as the harbor and administrative core.
**Recommendation:** none yet; it is a design choice. It is not needed until Esperanza's own run.
**What is waiting on it:** Esperanza's run (Step 0 band and extent), the Ulu Peninsula's description, the road or crossing.
**Answer (developer):**

### DEC-002 · OPEN · 2026-11-03 · Davis
**The question, in plain words:** Is Davis an ice-free oasis, sheltered from the katabatic wind, or a katabatic margin like the scoured coastal cities?
**The facts:** The Davis spec calls it an ice-free oasis (`Specs/Mirny subnet/Davis.md` L107; an authority said it is away from the katabatic wind). `Reference/Real-World/Climate Data/Precipitation_Falls_vs_Lands.md` L163 lists it under the katabatic margin. Numbers in use: 72.8 mm falls, 28 mm stays (38%). As an oasis it would be about 33 mm staying and 40 mm lost (45%).
**Options:** A) leave open (nothing breaks) · B) oasis: change 28 to 33 mm, 38% to 45%, in the spec and the reference · C) katabatic margin: change the spec's label.
**Recommendation:** A, until Davis's pass is tested (the Davis plan, `DR-104`); the finding "no fresh water from the sky" is the same either way.
**Answer (developer):**

### DEC-003 · OPEN · 2026-11-03 · Shirayuki
**The question, in plain words:** Which source folders may ground a finding in a pass? Shirayuki's pass treats two as ratified; the inspiration-picks list and the symbol files fall outside that list.
**The facts:** `Shirayuki/Amendment_Notes_2026-10-30_Manual_Input_Audit.md` section H, item 1 (queue entry `DRQ-12`).
**Recommendation:** decide once for all cities when the first new run needs it (Casey's picks were handled as "reduced standing", `DR-105`).
**Answer (developer):**

### DEC-004 · OPEN · 2026-11-03 · Zhongshan
**The question, in plain words:** May the Zhongshan culture file be corrected so it agrees with the spec and the language rule? Its tier table (L22–24) and its statement that Mandarin is the city's sole public language (L110) differ from the spec table and the Hawaiian-first rule.
**The facts:** `Zhongshan_Opus/Amendment_Notes_2026-10-30_Manual_Input_Audit.md` (SD-3, SD-4). Culture files are written only 05:00–14:59.
**Recommendation:** yes, in a morning window, with the language-line work already planned for Mirny, Temirötkel, Mawson and Santa Luce.
**Answer (developer):**

*(Other open items, not yet written up as questions: the Concordia geothermal flag (A, B or C); the Demilitarized Zone; Troll's faction line (parked). Details are in the handoff, section 7.)*

---

## Raised by the Mirny repass
*(Entries are added by the repass runs, newest last.)*

### DEC-005 · ANSWERED 2026-11-04 (DR-108) · 2026-11-04 · Mirny repass, Idelsk-Uralia piece (U2)
**The question, in plain words:** Idelsk-Uralia's people at Mirny (the founding country's own exiles, 2.14 % of each body): should they be written as one of the four founding exile groups, counted with the others, and NOT as a separate group of people with their own place in Phase 9?
**The facts:** `DR-99` made Idelsk-Uralia also an exile group. Phase 9 never makes a population out of any single stock; the other three exile groups enter through the founding robots and founding humans. Singling out the founder's people would give one stock a category the place does not draw. (`Amendment_Rederivation_PIU_IdelskUralia_2026-11-04.md` AIU-9, AQ-43.)
**Options:** A) a stock inside the founding groups, no population of its own · B) its own Phase 9 population.
**Recommendation:** A. It follows how Phase 9 already treats the other three groups.
**What is waiting on it / what was done provisionally:** Phase 9's own piece (U4). AIU-9 and AIU-10 are written on A and marked PROVISIONAL (DEC-005).
**Answer (developer):** "One stock inside the founding groups (Recommended)": no population of its own in Phase 9.

### DEC-006 · ANSWERED 2026-11-04 (DR-108) · 2026-11-04 · Mirny repass, Idelsk-Uralia piece (U2)
**The question, in plain words:** How should Mirny's founding be worded in the Frame's "founded" sentence, now that the founding country is also one of four exile groups?
**The facts:** The Frame's form of words (lines 164 to 166) says a Russia-, China- and Australia-founded Tepenian city, which rests on the older ruling `DR-9`. The Register now says founded by Idelsk-Uralia, with four exile groups present, together 23.24 % of a city of 36 stocks with no majority.
**Options:** A) the candidate wording: "an Idelsk-Uralia-founded Tepenian city, settled by exiles from Idelsk-Uralia, Russia, Australia and the Sinian Federation (China), a minority (23.24 %) of a long-run composition of 36 stocks with no majority. People: Tepenian. Local culture: its own." · B) name only the founding country · C) leave the Frame as it is (it is a pass file and is not edited either way).
**Recommendation:** A, as the working wording.
**What is waiting on it / what was done provisionally:** nothing blocks; AIU-16 offers A as a candidate (PROVISIONAL, DEC-006).
**Answer (developer):** "Yes, use that wording (Recommended)": held as the working wording in the amendment layer; the Frame file itself is not edited.

### DEC-007 · ANSWERED 2026-11-04 (DR-114) · 2026-11-04 · Mirny repass, Idelsk-Uralia piece (U2)
**The question, in plain words:** Phase 10 ties Mirny to "Mirny's own Russian-descended community" (a note in the character companion's README). After the population rework old Russia's people sit in thirteen rows, two of them exile groups at Mirny (Russia (core state) and Idelsk-Uralia). Which of them does the tie mean?
**The facts:** `P10` lines 56, 312 and 579 (Q-95; line 546 only says "her tie is TBD, to a stock community"); the census Section E key. The Register's one-to-one mapping (`DR-99`) covers the Register's founder names, not this README word. The README's adjective was written before `DR-46` and `DR-85`. For a robot, "descended" has no kinship referent: robots are fabricated, and a robot's origin is the culture she was immersed in.
**Options:** A) Russia (core state) only · B) Russia (core state) and Idelsk-Uralia · C) all old-Russia rows present at Mirny · D) leave the tie unmapped and unplaced, cited by pointer only.
**Recommendation:** D. Nothing in Phase 10 needs a row, and all three readers of the Phase 10 piece ended there.
**What is waiting on it:** nothing. The Phase 10 piece (U5) is written on D (A10-21).
**Answer (developer):** "Leave it unmapped (Recommended)": the tie to "Mirny's own Russian-descended community" stays unmapped and unplaced, cited by pointer only.

### DEC-008 · ANSWERED 2026-11-04 (DR-108) · 2026-11-04 · Mirny repass, Idelsk-Uralia piece (U2)
**The question, in plain words:** May the Mirny spec's founding lines be corrected to follow the Founding Register (add Idelsk-Uralia as an exile group, and replace the older founders line)?
**The facts:** `DR-99` was applied to the Register, census line 33 and the relationship database, but not to the spec: the founding-population line (L174) and the city-name line (L252) list three exile groups, and L251 still gives the `DR-9` founders (Russia, China and Australia). The Register governs founders (`Founding_Register.md` L8 to L10). This matches the drift found in unit U0.
**Options:** A) correct the three spec lines in a morning window · B) leave the spec as it is.
**Recommendation:** A (three lines; text from the Register).
**What is waiting on it:** nothing. AR-52 of the piece holds the docket.
**Answer (developer):** "Yes, correct the three lines (Recommended)": spec L174, L251 and L252 follow the Founding Register, in a 05:00-14:59 window with each change shown to the developer first (queued in the Weekly To-Do; not yet applied).


### DEC-009 · ANSWERED 2026-11-04 (DR-109) · 2026-11-04 · Mirny repass, robot-term piece (U3)
**The question, in plain words:** In the Division of Industry model the hard site raises the cost of Mirny's human-keyed and shared necessary work (by 43,367 workforce units, 4.10 %), but not the cost of keeping the robot body maintained and supplied (the robot term has no site factor). Is that intended?
**The facts:** the formula in file `16` (`DR-97`, your ruling that the robot term belongs in it) writes the robot term flat: 15.75 per 1,000 robots. The pass elsewhere reads the cold as a cost to a robot's charge. If the term carried the same factor, it would rise by about 2,798 units and Mirny's free tier would fall by 1,679 (to 34.51 %). (`Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md` ART-3, RF-PRT-2, AQ-50.)
**Options:** A) leave the formula as ruled and record the asymmetry · B) give the robot term the site factor.
**Recommendation:** A. It follows your ruling as written and changes no finding.
**What is waiting on it / what was done provisionally:** nothing blocks; the piece is written on A and marked PROVISIONAL (DEC-009).
**Answer (developer):** "Yes, leave it as ruled (Recommended)": the robot term stays flat; the asymmetry is recorded.

### DEC-010 · ANSWERED 2026-11-04 (DR-109) · 2026-11-04 · Mirny repass, robot-term piece (U3)
**The question, in plain words:** Phase 4 uses the phrase "freedom margin" for the share of workforce not spoken for. The Division of Industry file uses it for two different quantities: the residue after the baseline (57.8 % of workforce units at Mirny) and the "elective residue" after both baseline and provision (34.7 %). Which should the phrase name, or should the two get separate names?
**The facts:** `P4` L149 and L351 (Q-43); file `09`, section 3.5. Whether either measures "people able to do work they want" or "a share of a working life" is a separate open question (Q-43).
**Options:** A) separate names: "the free tier (the character budget)" for 34.7 % and "the distinctive tier" for 57.8 % · B) "freedom margin" for 57.8 % only · C) "freedom margin" for 34.7 % only.
**Recommendation:** A.
**What is waiting on it:** Q-43's restatement (ART-10), PROVISIONAL (DEC-010).
**Answer (developer):** "Two separate names (Recommended)": "the free tier (the character budget)" for 34.7 % and "the distinctive tier" for 57.8 %.

### DEC-011 · ANSWERED 2026-11-04 (DR-111) · 2026-11-04 · Mirny repass, Phase 9 piece (U4)
**The question, in plain words:** By your language rule (every group within 12 points of the city's largest is a supporting tier), Mirny's supporting tier comes out as English alone. Do you want that carried?
**The facts:** English is 25.2 to 34.4 % of Mirny's national-origin shares; the next bloc is 15.8 to 16.7 %. At mid-points the gap is about 13.5 points (over 12); at the near ends of the ranges it is 8.5 (under 12). The shares are national-origin shares, not speaker counts, and the nation-to-language mapping is recalled knowledge. The accepted Phase 2 and Phase 8 pieces still say "second slot open for want of a majority", written before the plurality rule. (`Amendment_Rederivation_P9_Populations_2026-11-04.md` A9-20, AQ-59.)
**Options:** A) English alone as the supporting tier, marked as resting on mid-points · B) English and the next bloc, if you want the rule applied at the near ends · C) leave the second slot open.
**Recommendation:** A.
**What is waiting on it / what was done provisionally:** Phase 9's language groups and the typical resident; the piece is written on A and marked PROVISIONAL (DEC-011).
**Answer (developer):** "English and Russian, as a special ruling": Mirny's supporting tier is English and Russian by ruling (a Mirny special case), not by the 12-point arithmetic, which gives English alone (by actual speakers English 32.8 %, Mandarin 16.2 %, Russian 9.4 %). The amendment pieces written on "English alone" (Phase 9, Phase 10, Step 5 and later) need a docket note, not an edit.

### DEC-012 · ANSWERED 2026-11-04 (DR-109) · 2026-11-04 · Mirny repass, Phase 9 piece (U4)
**The question, in plain words:** In 2026-10-21 you ratified three person-shaped additions to Phase 9 (the Aries, Virgo and Capricorn results), worded with "keeper". "Keepers" was the pass author's own coinage, not canon, and the thank-you clause is not established either way. May they be reworded?
**The facts:** Phase 9 line 5 records the additions. The proposed rewording: Aries becomes "whoever is most strategically able to address the hazard goes out, sent by nobody, into the storm that broke the line"; Virgo becomes skilled fine work by the people who maintain the relay, the ring's clearers and the repair trades, without "no thanks when it succeeds"; Capricorn becomes a person who maintains the relay and will not ask the served for a second path. The other four additions (Cancer, Sagittarius, Scorpio, Aquarius) cannot be checked from the files read here.
**Options:** A) reword as proposed · B) leave the ratified wording.
**Recommendation:** A, as a proposal; ratified content changes only on your word.
**What is waiting on it:** Step 5's re-check of the Zodiac-lens additions. The piece is written on A, PROVISIONAL (DEC-012).
**Answer (developer):** "Reword as proposed (Recommended)": Aries, Virgo and Capricorn reworded without "keeper"; a proposal in the amendment layer, ratified wording changes only by this word.

---

### DEC-013 · ANSWERED 2026-11-04 (DR-111) · 2026-11-04 · Mirny repass, Phase 10 piece (U5)
**The question, in plain words:** May the catalog list "a member of the organization that manages and curates the weather protocol" as a candidate role, described by what it does only (no title, office, seat or name)? And does that organization, or the protocol, have a place of its own in the city?
**The facts:** `DR-57` (rulings log L1140): "There's some sort of an organization of people (both robots and humans) who manage and curate the protocol for the weather". The amendment register's draft said "no role or person named"; the personal-name rule bars names, not roles described by function. No admitted line gives the organization a seat.
**Options:** A) a candidate role, no place cataloged · B) a candidate role, and a place exists · C) no role entry.
**Recommendation:** A.
**What is waiting on it / what was done provisionally:** the piece is written on A and marked PROVISIONAL (DEC-013). If B: a new unnamed place-function entry is added, RF-P10-6 is adopted, AR-70 closes, C3-23 gains a setting. If C: C3-23 is struck from A10-8, section 5 row 4 and AQ-65.
**Answer (developer):** "A candidate role, no place (Recommended)": a member of the organization that manages and curates the weather protocol may be cataloged as a candidate role by function only (no title, office, seat or name); no place is cataloged for it.

### DEC-014 · ANSWERED 2026-11-04 (DR-111) · 2026-11-04 · Mirny repass, Phase 10 piece (U5)
**The question, in plain words:** Does everyone at Mirny teach the wind to newcomers, children and newly built robots, or do particular people, whom a resident would recognize, do the teaching?
**The facts:** "they teach each other" (rulings log L1115). No admitted line says how the teaching happens.
**Options:** A) keep "a teacher of the wind" as a candidate role, conditional on this answer · B) everyone teaches · C) particular people teach.
**Recommendation:** A until you answer.
**What is waiting on it / what was done provisionally:** the piece is written on A (PROVISIONAL, DEC-014). If B: C3-24 is struck and folds into the typical resident (A10-9) and the new player row. If C: C3-24 loses its condition, AR-73 closes, and whether teaching gives standing stays open (AR-47, AR-63).
**Answer (developer):** "Leave it open for now (Recommended)": "a teacher of the wind" stays a candidate role conditional on the open question whether everyone teaches or particular people do; nothing is built on either reading.

### DEC-015 · ANSWERED 2026-11-04 (DR-115) · 2026-11-04 · Mirny repass, Phase 10 piece (U5)
**The question, in plain words:** Phase 10 still says the Element is "pending by rule" and the Planet is "CONFIRMED, provisionally: Saturn". May that be corrected, as a docket only, to "Element Air accepted; Planet held, Saturn provisional", both provisional until the locations are synthesized? Or is Air final now?
**The facts:** `DR-57` (rulings log L1141, L1151, L1152); the 2026-11-03 stage order (symbols after synthesis). Step 5 states the same stale status (see the Step 5 piece).
**Options:** A) correct the status as a docket only; Air accepted and provisional · B) Air is final now · C) leave Phase 10's wording.
**Recommendation:** A.
**What is waiting on it / what was done provisionally:** written on A (PROVISIONAL, DEC-015). If B: "provisional" is dropped for the Element in A10-17, D10-9, AQ-66 and A10-23. If C: D10-9 and AQ-66 are withdrawn and A10-17 keeps only the corrected facts.
**Answer (developer):** "After Mirny's ULM only; correct the status": Mirny's symbols are determined within Mirny's own ULM pass, not after other cities and not after its CST/RWBEM; the status lines in Phase 10 and Step 5 are corrected, as a proposal, to "Element Air accepted; Planet held, Saturn provisional".

### DEC-016 · ANSWERED 2026-11-04 (DR-111) · 2026-11-04 · Mirny repass, Phase 10 piece (U5)
**The question, in plain words:** Who built Mirny's outer ring, its sheltered core and the relay hardware, and roughly when: the first generation, later residents, or were they inherited with the station?
**The facts:** Phase 10 (L137) says the lasting landmarks are "without exception" made by nobody living at Mirny. Its own L208 lists the builder as not given, and the spec (L172) says the exiles "built on" the station that remained.
**Options:** A) leave them "of unstated making" · B) built by Mirny's people · C) inherited.
**Recommendation:** A (nothing waits on it).
**What is waiting on it / what was done provisionally:** written on A. If B: the "stays" half of the axis gains a second thing made here; A10-1's sort, byproduct 1 (A10-16) and the "shown to be made here" conditionals change. If C: the ring and the core join the "found" class and "without exception" is restored for them (A10-1, section 4, AQ-69).
**Answer (developer):** "Leave it unstated (Recommended)": the ring, the core and the relay hardware stay "of unstated making".

### DEC-020 · ANSWERED 2026-11-04 (DR-113) · 2026-11-04 · Mirny repass, Step 5 piece (U6)
**The question, in plain words:** May Mirny's "strongest finding" be restated for the corrected wind account? In short: the first generation learned the wind alone; what they made became a public knowledge, taught and curated by people of both bodies; its warnings travel on the one relay; and when the relay fails, whoever is most strategically able goes out, uncompelled. Two details inside it: the word "assigned" (for the exiles) stays out of the core of the finding, because it rests on an unratified treaty draft; and "the warnings go dark exactly when they are needed" is a conditional add-on, not part of the core, until the relay's technology and what carries warnings during an outage are ruled.
**The facts:** `DR-56`, `DR-57`, `DR-76`; the Step 5 piece, finding A5-1. The finding's old form depended on "nobody ever taught anyone about the wind".
**Options:** A) adopt the restated form as proposed · B) adopt it with "assigned" back in the core · C) adopt it with "go dark" in the core.
**Recommendation:** A.
**What is waiting on it / what was done provisionally:** the piece is written on A (PROVISIONAL, DEC-020). On B the strongest-finding check must flag the unratified treaty draft as ground. On C the whole finding depends on the relay's technology and on what carries warnings in an outage until both are ruled.
**Answer (developer):** Worked through in four parts. (1) Core idea: "The knowledge the first generation made": the strongest finding is built around the made-and-taught knowledge system (the first generation learned the wind alone and made a public knowledge everyone after is taught, curated by an organization of both bodies); the relay duty is a consequence, not part of the finding. (2) "Assigned": "Keep it out of the core (Recommended)". (3) "The warnings go dark": "A conditional add-on outside the core (Recommended)". (4) No rite after a loss: "Leave it as an empty slot (Recommended)" ("none sited here", never "none possible here").

### DEC-021 · ANSWERED 2026-11-04 (DR-112) · 2026-11-04 · Mirny repass, Step 5 piece (U6)
**The question, in plain words:** The live local-culture file (rewritten 2026-11-03) still disagrees with the sources in places: the Census II header, the founders note (it omits Idelsk-Uralia as also an exile group), the "smaller communities" list, the "second-language slot left open" line, the retracted light model, the "other five" hub members, and a line about "the station's inherited table". It is also silent on the ruled wind account. The Step 5 piece lists 39 proposed corrections (D-1 to D-39). When should they be applied, and may the file state the wind account (and where)? And should the holidays and the faith line given to a stock by name be held for after the CST, struck, or marked?
**The facts:** the Step 5 piece, section 6 (the docket), rows D-24 to D-39; the culture file belongs to you; nothing was edited. Stage order (2026-11-03): holidays and religion come after the CST.
**Options:** A) hold the whole docket for the post-ULM rewrite, except the high-confidence factual rows (census, founders, members and warnings, light physics); state the wind account in principle (placement yours); mark holidays and faith "held for after the CST" · B) apply everything now · C) apply nothing; keep the docket for later.
**Recommendation:** A.
**What is waiting on it / what was done provisionally:** nothing is applied. On B, later matches against the file become even less independent. On C, a stale census, founders note, language slot and light model stay in a file other work reads.
**Answer (developer):** "Hold most, apply the factual ones (Recommended)": the culture-file docket (D-1 to D-39) is held for the post-ULM rewrite, except the high-confidence factual rows (census, founders, members and warnings, light physics); the file should state the ruled wind account in principle (placement the developer's); holidays and the stock-named faith line are marked "held for after the CST". Nothing is applied yet.

### DEC-060 · ANSWERED 2026-11-04 (DR-107) · 2026-11-04 · Mirny repass, Step 7 piece (U8)
**The question, in plain words:** Step 7 (the 17 QA gates) was run before the wind correction and the population rework. Its scan results are true of the old text. Two things: (a) may the checks that read live sources rather than the pass text be run now, as new labeled blocks beside Step 7's record? These are Gate 11's population arithmetic, Gate C's source and anchor sweep, Gate 5's relation check, Gate P's list and Gate F's Band check. (b) Is the rest of Step 7 re-run once, after all the amendment dockets are applied on your word, or gate by gate as each piece's docket lands?
**The facts:** the Step 7 piece, section 5 (the re-run docket). Gates 0, 3, 4, 6 and I must be re-run after application; Gates 2, 8, 9, 11 and C change now; Gates 1, 5, 7, 10, F, P and G stand with a note.
**Options:** (a) yes / no · (b) once after all dockets are applied / gate by gate.
**Recommendation:** (a) yes; (b) once, after all dockets are applied, and never counting a clash between a file's amendment notice and its unrewritten text as a new finding.
**What is waiting on it / what was done provisionally:** nothing is run. If (a) is no, the stale census anchors and the old Gate 11 arithmetic stay Step 7's only record until the full re-run. If (b) is gate by gate, Gates 0, 3 and C are re-run more than once and each interim run reports a mix of old and new text.
**Answer (developer):** "Live-source checks now, the rest once": the checks that read live sources (population arithmetic, source and anchor sweep, relation check, list and band checks) may run now as separate labeled blocks beside Step 7's record; everything else is re-run once, after the corrections are applied on the developer's word.

### DEC-040 · ANSWERED 2026-11-04 (DR-112) · 2026-11-04 · Mirny repass, Step 6 piece (U7)
**The question, in plain words:** Mirny's row in the cross-city differentiation table was written in nine lines before your rulings, and six of those lines are now stale. The Step 6 datasheet says the table gained a tenth section (the Catalog) and a Phase-axis column on 2026-10-21; no ruling for that change is on our lists. Four things: (a) is ten sections the shape to fill? (b) may the corrected row be adopted, written to the shared table only on your word and in the same commit as your acceptance? (c) in the Order section's Phase-axis cell, repeat "Learned once; those who can, respond." or point to the Meaning section's copy? (d) hold the Catalog line until the Phase 10 piece is settled?
**The facts:** the Step 6 piece, section 4 (the proposed corrected row: 12 cells KEEP, 4 REWORD, 7 RE-DERIVE, plus three Phase-axis cells as CAND); `DR-77`, `DR-79`; the shared table was not opened.
**Options:** (a) yes / nine only · (b) yes / keep the old row · (c) repeat / point · (d) yes / fill now.
**Recommendation:** yes; yes; repeat it; yes.
**What is waiting on it / what was done provisionally:** nothing is written to the table. With nine sections, the new cells drop; keeping the old row leaves six stale lines plus an under-fill; a pointer makes Order depend on Meaning; filling the Catalog line now gets ahead of the Phase 10 piece.
**Answer (developer):** "Adopt it, ten sections, repeat the axis (Recommended)": the corrected row is adopted as a proposal (ten sections filled, the Catalog line held until the Phase 10 piece is settled, the Order cell repeats "Learned once; those who can, respond."); written to the shared table only on the developer's word.

### DEC-041 · PART (a) ANSWERED 2026-11-04 (DR-115); (b) OPEN · 2026-11-04 · Mirny repass, Step 6 piece (U7)
**The question, in plain words:** How should the final cross-city check read two things you ruled? (a) Meaning and Order share one axis ("Learned once; those who can, respond.") by your ruling; should that be treated as your choice, outside the "everything converges, maybe author habit" test? (b) Keep a timing axis in the Observance column now, with its content after the CST, or leave the column empty?
**The facts:** the Step 6 piece, NS-11 and the swap test; `DR-77`, `DR-79`; stage order (holidays after the CST).
**Options:** (a) yes / no · (b) keep the axis / leave empty.
**Recommendation:** (a) yes; (b) keep the axis.
**What is waiting on it / what was done provisionally:** written on the recommendations. If (a) is no, the shared axis counts against the row (higher convergence risk). If (b) is empty, the Meaning section is one cell thinner until after the CST.
**Answer (developer):** (a) "Yes, your deliberate choice (Recommended)": the Meaning and Order shared axis is set outside the "everything converges, maybe author habit" test. (b) keep a timing axis in the Observance column: not asked separately; recommendation stands (keep the axis).

### DEC-042 · DEFERRED 2026-11-04 (DR-112) · 2026-11-04 · Mirny repass, Step 6 piece (U7)
**The question, in plain words:** Who decides who goes out to restore the relay? Can anyone ask a particular person to go without compelling them, or does each person judge alone whether they are the most able? This rides with the Phase 7 piece's request AR-22.
**The facts:** `DR-56` Q-69 (nobody is required; deep guilt on neglect), `DR-76` ("whoever's most strategically able").
**Options:** A) asking exists (who may ask is recorded) · B) each person judges alone · C) answer later.
**Recommendation:** C. The merged Governance cell holds either way.
**What is waiting on it / what was done provisionally:** nothing. If A, the source column records who may ask. If B, AR-22 closes.
**Answer (developer):** "Answer later (Recommended)": who decides who goes out to restore the relay stays open; the merged text holds either way.

### DEC-080 · DEFERRED 2026-11-04 (DR-114) · 2026-11-04 · Mirny repass, Step 8 piece (U9)
**The question, in plain words:** In the Review Panel, the only objection the pass refused as "something Mirny knowingly will not do" was that the hub does not ask for a second relay path. That refusal rested on the coined "keepers". Do Mirny's people choose not to ask for a second path, or is nothing ruled either way?
**The facts:** the Step 8 piece, finding on PF-10 (NB-2); no ruling says anyone chooses not to ask.
**Options:** A) no ruling needed now; record the refusal as `declined`, provisional · B) yes, they knowingly do not ask (it returns to `unmet`) · C) they would ask, or a second path exists (the warning half becomes `noted`).
**Recommendation:** A.
**What is waiting on it / what was done provisionally:** written on A (PROVISIONAL, DEC-080; request AR-140). If B, the Lens row keeps its "will not ask" wording and DEC-081 also bears. If C, the characterization changes.
**Answer (developer):** "need to figure that out later": whether Mirny's people knowingly do not ask for a second relay path is open; the refusal stays recorded as "declined", provisional.

### DEC-081 · DEFERRED 2026-11-04 (DR-114) · 2026-11-04 · Mirny repass, Step 8 piece (U9)
**The question, in plain words:** When the panel refuses a rule that would compel someone to go out and restore the relay, is that refusal Mirny's own self-knowledge (`unmet`) or a plain `declined`? The duty is national (Tepenians' sense of community), not Mirny's alone.
**The facts:** the Step 8 piece, Q-136; `DR-56` Q-69, `DR-80`.
**Options:** A) `declined` for both compulsion refusals · B) `unmet` for both · C) `rejected` for both.
**Recommendation:** A (the practice the merge already used).
**What is waiting on it / what was done provisionally:** written on A. The `unmet` count is 0 for now; with B it becomes 2, or 3 if DEC-080 is answered yes.
**Answer (developer):** "haven't figured that out yet": whether the refusals of a rule compelling someone to go out are "unmet" or "declined" is open; recorded as "declined", provisional.

### DEC-082 · ANSWERED 2026-11-04 (DR-115) · 2026-11-04 · Mirny repass, Step 8 piece (U9)
**The question, in plain words:** Should a fresh Review Panel be run once the whole amendment series closes? The corrected city has seats nobody has voiced yet (a teacher of the wind; the curating organization).
**The facts:** the Step 8 piece re-tested only the objections and findings that rested on the retired reading; it did not run a new panel.
**Options:** A) yes, later (after the amendments are applied), not now · B) no; the re-test stands and those seats stay recorded as silences.
**Recommendation:** A.
**What is waiting on it:** nothing.
**Answer (developer):** "Yes, later (Recommended)": a fresh Review Panel is run once the amendments are applied, not now.

### DEC-120 · ANSWERED 2026-11-04 (DR-108, DR-115) · 2026-11-04 · Mirny repass, Step 10 piece (U11)
**The question, in plain words:** What does "complete" have to mean for Mirny's ULM pass? (a) Must the lived middle (what Mirny's people, robots and humans, do with their own hours) be written inside the ULM, or may the ULM close with it explicitly left to the CST, as your stage order suggests? (b) Does the held Planet still block calling the ULM complete, or is it a later-stage item?
**The facts:** the Step 10 piece, section 4; Step 10's review notice (2026-10-21) said the pass is not complete because the lived middle is unwritten, the wind re-derivation and the cap-starved research are scheduled, and the Planet is held.
**Options:** (a) inside the ULM / left to the CST, recorded as "deferred" · (b) blocks / later-stage.
**Recommendation:** (a) yours alone; until you answer it stays on the readiness list, and if you defer it the record says "deferred", never "done". (b) carry the Planet as held, not cleared.
**What is waiting on it:** nothing is declared complete. Otherwise Mirny cannot close until the everyday life is written, or it waits on symbol work your order puts after synthesis.
**Answer (developer):** (a) "Hand it to the CST" (DR-108): the ULM may close with the everyday-life texture explicitly handed to the CST. (b) "It still blocks": the held Planet blocks calling Mirny's ULM pass complete, so the Planet must be decided within the ULM.

### DEC-121 · ANSWERED 2026-11-04 (DR-116) · 2026-11-04 · Mirny repass, Step 10 piece (U11)
**The question, in plain words:** When is Step 10 run again, and what did "the cold half of 10" mean? (a) May the checks that read today's files run now as labeled blocks (the name scan of the repass's new prose, the methodology git and name scan, the handoff path check, the existence half of Gate 0 outward, the reading of the rule files for item 10)? (b) Is the whole Step 10 re-run once, last, after the decisions, the dockets, the Step 7 re-run, a fresh panel if wanted, and the Step 9 piece? (c) Item 10 has no written cold half: what did it mean?
**The facts:** the Step 10 piece, section 5 (the re-run docket); items 1c, 6, 9 and 11 must be re-run, items 2 and 10 change.
**Options:** (a) yes / no · (b) once, last / check by check · (c) your definition.
**Recommendation:** (a) yes; (b) yes; (c) until you say, treat all of item 10 as live.
**What is waiting on it:** the name scan of the new prose has to run before anything from the repass is committed anyway. Running Step 10 check by check gives interim results that mix old and new text.
**Answer (developer):** (a) yes and (b) yes by DR-107; (c) "Treat all of item 10 as live (Recommended)": until the developer says otherwise no part of Step 10 item 10 is parked as cold-run-only.

### DEC-122 · ANSWERED 2026-11-04 (DR-118) · 2026-11-04 · Mirny repass, Step 10 piece (U11)
**The question, in plain words:** Which lessons from the Mirny runs go into the methodology rules? (Step 10's R-183, open since 2026-10-13; you said "that's something we need to review".)
**The facts:** `M-299` is in the runbook; three tools now behave as MP-1 to MP-3 asked; six proposals exist only as brief lines; the repass added more lessons of the same kind (see the Step 9/9.5 piece when it lands).
**Options:** A) review them as one batch with this evidence; record MP-1 to MP-3 as visible in tool behavior, not yet in a rule · B) put them in the rules now · C) leave as they are.
**Recommendation:** A.
**What is waiting on it:** nothing. Otherwise item 10 keeps firing.
**Answer (developer):** Applied: 43 of the 45 rows (M-281 and OBS-4 struck; OBS-14 not for the rules) written into the rules; amendment-layer rules in the new file Amendment_Layer_Rules.md; observation entries M-305 to M-319 appended. Not committed.

### DEC-100 · ANSWERED 2026-11-04 (DR-107) · 2026-11-04 · Mirny repass, Steps 9 and 9.5 piece (U10)
**The question, in plain words:** Should the repass be extended to the files no piece covered? No piece re-checked Steps -1 to 3, Phase 3, or the wind lines of Phases 4 and 5. Some of those files still state the old "nobody taught the wind" reading with no notice: the spine's deficits 5 and 7, Step 2's profile, two lines of Phase 3, Phase 4's axis and wind clauses, and two Phase 5 lines that use the coinage. Steps -1, 0, 1 and 3 have not been checked at all.
**The facts:** the Steps 9/9.5 piece, AS9-16 and the Record addendum (AS9-23).
**Options:** A) yes: add units, run them after the open decisions are answered, and finish them before the readiness check is re-run · B) no · C) only the files that still state the old reading.
**Recommendation:** A.
**What is waiting on it:** nothing is changed. Otherwise the early files keep the retired reading and the amendment layer cannot be called complete.
**Answer (developer):** "Yes, extend it (Recommended)": units for Steps -1 to 3, Phase 3 and the wind lines of Phases 4 and 5, run after the other open decisions are answered and finished before the readiness check is re-run. Queued as U12 to U14 in the repass queue (not started).

### DEC-101 · ANSWERED 2026-11-04 (DR-107) · 2026-11-04 · Mirny repass, Steps 9 and 9.5 piece (U10)
**The question, in plain words:** Units U5 to U11 ran at the same time, not one after another as the queue said (the assistant did this under your instruction to continue through all the steps and to finish by 3 pm; you did not ask for parallel running). Do you accept that, and how should future repasses run?
**The facts:** the Steps 9/9.5 piece, AS9-24 (C'.1), marked as the orchestrator's account; the pieces cross-reference each other after the fact.
**Options:** A) accept it, schedule one in-order read of the corrected Steps 5 to 8 (a fold-in) before the readiness check, and in future run a unit only after the units it depends on · B) redo the Step 6 to Step 8 pieces in order · C) accept it with no fold-in.
**Recommendation:** A.
**What is waiting on it:** nothing. On B, the Step 6 to 8 pieces are redone; on C, the cross-references stay the only link between those pieces.
**Answer (developer):** Standing rule, verbatim: "If there's anything that needs the results from a previous thing in order to run, don't run the next thing until the previous thing is confirmed. So if [B] requires [A] to be able to run and [A] is not complete, then finish [A] first and then start doing [B]." Applies from now on; whether to redo Steps 5 to 8 in order (the fold-in) was not yet asked.

### DEC-102 · ANSWERED 2026-11-04 (DR-107) · 2026-11-04 · Mirny repass, Steps 9 and 9.5 piece (U10)
**The question, in plain words:** When does the line-reference sweep (Step 9's fifth action: checking every cited line number) run?
**The facts:** the Steps 9/9.5 piece; the sweep has not been run; line numbers have drifted by 2 to 5 lines in about eight places.
**Options:** A) once, after the dockets are applied, together with Step 7's re-run · B) now, and again later · C) not at all.
**Recommendation:** A.
**What is waiting on it:** nothing. If it runs now it must be run again later; if it is left, every line-number citation stays unchecked.
**Answer (developer):** Once, after the corrections are applied, together with Step 7's re-run ("the rest once"). The live-source half may run now.

### DEC-103 · ANSWERED 2026-11-04 (DR-116) · 2026-11-04 · Mirny repass, Steps 9 and 9.5 piece (U10)
**The question, in plain words:** Where do the Step 9 and 9.5 updates live? The old Record and Log keep stale counts and statuses (for example "one unmet", "Steps -1 to 8 complete"); records are never reworded.
**The facts:** the Steps 9/9.5 piece, AS9-23 (Record addendum) and AS9-24 (Log addendum), written as separate text.
**Options:** A) keep them in the separate piece file, plus one line at the very end of each old file pointing to it (no cited line moves) · B) the separate piece file only · C) a new Record and Log file for the repass.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. Otherwise the old counts and tool statuses keep reading as current.
**Answer (developer):** "Separate file plus a pointer line (Recommended)": the Step 9 and 9.5 updates live in the separate piece file, plus one pointer line at the very end of each old file (no cited line moves). The pointer lines are edits to pass files, which `DR-101` says are never edited: not applied; to be confirmed when the dockets are applied.

### DEC-104 · ANSWERED 2026-11-04 (DR-116) · 2026-11-04 · Mirny repass, Steps 9 and 9.5 piece (U10)
**The question, in plain words:** Is the Lover-faculty late check (the pass's T5 check, never run) still owed, or retired?
**The facts:** the Steps 9/9.5 piece; the Step 8 piece's DEC-082 already asks about a fresh Review Panel.
**Options:** A) owed, done together with the fresh panel · B) compare by hand now against the old panel · C) retire T5 by ruling.
**Recommendation:** A.
**What is waiting on it:** nothing.
**Answer (developer):** "Owed, done with the fresh panel (Recommended)": the Lover-faculty late check is run together with the fresh Review Panel (DR-115).


## Answered
*(Moved here with the date and the ruling number.)*
- 2026-11-04, `DR-118`: DEC-122 answered in place above.
- 2026-11-04, `DR-117`: DEC-122 answered in place above.
- 2026-11-04, `DR-116`: DEC-121, DEC-103, DEC-104, DEC-122 answered in place above.
- 2026-11-04, `DR-115`: DEC-015, DEC-041, DEC-082, DEC-120 answered in place above.
- 2026-11-04, `DR-114`: DEC-080, DEC-081, DEC-007, DEC-015 answered in place above.
- 2026-11-04, `DR-113`: DEC-020 answered in place above.
- 2026-11-04, `DR-112`: DEC-021, DEC-040, DEC-042 answered in place above.
- 2026-11-04, `DR-111`: DEC-011, DEC-013, DEC-014, DEC-016 answered in place above.
- 2026-11-04, `DR-107`: DEC-100, DEC-101, DEC-060, DEC-102 answered in place above; DEC-121 (a) and (b) answered, (c) open.
- 2026-11-04, `DR-108`: DEC-005, DEC-006, DEC-008 answered in place above; DEC-120 (a) answered, (b) open.
- 2026-11-04, `DR-109`: DEC-012, DEC-009, DEC-010 answered in place above; DEC-011 questioned by the developer, still open.
