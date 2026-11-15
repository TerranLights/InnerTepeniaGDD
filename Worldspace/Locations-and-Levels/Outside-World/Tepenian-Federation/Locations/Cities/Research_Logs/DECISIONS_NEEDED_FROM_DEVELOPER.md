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

### DEC-003 · OPEN (deferred 2026-11-10, DR-131) · 2026-11-03 · Shirayuki
**The question, in plain words:** Which source folders may ground a finding in a pass? Shirayuki's pass treats two as ratified; the inspiration-picks list and the symbol files fall outside that list.
**The facts:** `Shirayuki/Amendment_Notes_2026-10-30_Manual_Input_Audit.md` section H, item 1 (queue entry `DRQ-12`).
**Recommendation:** decide once for all cities when the first new run needs it (Casey's picks were handled as "reduced standing", `DR-105`).
**Answer (developer):** "Decide for all cities later (Recommended)": deferred; settled once for every city when the first new run needs it.

### DEC-004 · ANSWERED 2026-11-10 (DR-130) · 2026-11-03 · Zhongshan
**The question, in plain words:** May the Zhongshan culture file be corrected so it agrees with the spec and the language rule? Its tier table (L22–24) and its statement that Mandarin is the city's sole public language (L110) differ from the spec table and the Hawaiian-first rule.
**The facts:** `Zhongshan_Opus/Amendment_Notes_2026-10-30_Manual_Input_Audit.md` (SD-3, SD-4). Culture files are written only 05:00–14:59.
**Recommendation:** yes, in a morning window, with the language-line work already planned for Mirny, Temirötkel, Mawson and Santa Luce.
**Answer (developer):** "Yes, correct all three (Recommended)" (given at DEC-470, 2026-11-10): the tier table and the sole-public-language line are corrected, with the founding-wave tag on Australia.

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

### DEC-140 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Steps -1 to 3 piece (U12)
**The question, in plain words:** May the five early Mirny step files (the input contract, the Frame, Inherited, the Spine and Research) each get one pointer line at their very end? They still read as current, with nothing to say that their wind, composition and founders lines were updated elsewhere.
**The facts:** the Steps -1 to 3 piece (`Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md`), AS12-52 holds the exact text. `DR-101` says pass files are never edited; `DR-116` allowed this kind of end-of-file pointer only for Steps 9 and 9.5. A notice at the top would shift every cited line in all five files.
**Options:** A) yes, one line at the end of each file, applied only when the dockets are applied · B) no, leave the files untouched.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. If B, the files keep reading as current, which is how the gap was missed.
**Answer (developer):** Yes, all four (Recommended): one pointer line at the end of each file, applied only when the dockets are applied (same answer for DEC-140, 160, 180, 203).

### DEC-141 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Steps -1 to 3 piece (U12)
**The question, in plain words:** Two datasheets print wrong arithmetic (the retention spread is printed 1.89 and should be 1.26; the extent rows print 137.5 and 196.5 km2 and should be 140.35 and 200.51), and four other rows predate rulings (language, founders, the census attribution, the spec length). Correct them in place, or keep corrections beside them?
**The facts:** the Steps -1 to 3 piece, section 2 and the docket. The datasheets are derived sheets, not pass files.
**Options:** A) correct in place, showing each change to you first, as with the culture file's factual rows (`DR-112`) · B) keep the sheets and put corrections beside them.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. If B, the sheets keep printing figures that do not follow from their own inputs.
**Answer (developer):** Correct in place, show first (Recommended): same answer for DEC-141, 163, 182.

### DEC-142 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Steps -1 to 3 piece (U12)
**The question, in plain words:** When does the real-world research on Mirny's weather signs run? `DR-76` asked for it ("we'll need to look into actual real-world research"); it has not run. Step 3's web search stopped at a 200-search cap, Idelsk-Uralia's forms were never researched, and 33 of the 36 stocks are unresearched.
**The facts:** the Steps -1 to 3 piece (research section) and the open stocks research already listed as not in the repass queue.
**Options:** A) a dedicated research session in the 05:00-14:59 window, before Mirny's symbols unit and before the readiness check is re-run · B) after the stocks research · C) leave the slots open.
**Recommendation:** A.
**What is waiting on it:** nothing is researched yet. If B or C, the signs stay an open slot in Phases 3, 8 and 10.
**Answer (developer):** Dedicated session soon (Recommended): a research session on Mirny's weather signs in the 05:00-14:59 window, before the readiness check is re-run.

### DEC-160 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Phase 3 piece (U13)
**The question, in plain words:** May Phase 3 (the surface and texture file) get one pointer line at its very end, like the five early step files (DEC-140)? It still reads as current, with nothing to say that its wind, composition and founders lines were updated elsewhere.
**The facts:** the Phase 3 piece (`Amendment_Rederivation_ST13_Phase3_2026-11-05.md`), section 7.4. `DR-101` says pass files are never edited; a notice at the top would shift every cited line.
**Options:** A) yes, one line at the end, applied only when the dockets are applied, under the same answer as DEC-140 · B) no, leave the file untouched.
**Recommendation:** A, decided together with DEC-140.
**What is waiting on it:** nothing is edited. If B, the file keeps reading as current.
**Answer (developer):** Yes, all four (Recommended): see DEC-140.

### DEC-161 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Phase 3 piece (U13)
**The question, in plain words:** Phase 3 says the ring "has keepers". May that be read as "the ring's clearers": a role either body may hold, never an organization? (Reader B offers a form with no label at all.)
**The facts:** the Phase 3 piece, section 7.4 (the piece uses "the ring's clearers"; both forms are shown). "Keepers" is never a name.
**Options:** A) "the ring's clearers" · B) no label, describe the work only.
**Recommendation:** A.
**What is waiting on it:** nothing is edited; the wording in Phase 3's addendum is provisional.
**Answer (developer):** No label, describe the work (reader B's form): Phase 3's "keepers" line is described by the work done, with no role label and no name.

### DEC-162 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Phase 3 piece (U13)
**The question, in plain words:** Phase 3 uses "the warning" for two different things: the weather warning on the relay and the wind's own first physical sign. Which word goes to which?
**The facts:** the Phase 3 piece, section 7.4 and the term note (readers A, B and C all found the clash at L333 to L417).
**Options:** A) "the warning" means the weather warning on the relay and the wind's physical onset is "the first sign" · B) keep both uses and let context decide.
**Recommendation:** A.
**What is waiting on it:** nothing is edited; the addendum carries both forms until you decide.
**Answer (developer):** Keep both uses: "the warning" stays for both the weather warning on the relay and the wind's own first sign; context decides. (The addendum carries both forms.)

### DEC-163 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Phase 3 piece (U13)
**The question, in plain words:** Phase 3's datasheet has no wind, precipitation or record-extreme rows. May those rows be added after the spec figures are re-keyed (request AR-220)?
**The facts:** the Phase 3 piece, section 7.4 and AR-220; the datasheet is a derived sheet, not a pass file. It rides on DEC-141 (corrected in place or kept beside).
**Options:** A) add them, showing you the rows first · B) leave the datasheet as is.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):** Correct in place, show first (Recommended): see DEC-141.

### DEC-180 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Phases 4 and 5 piece (U14)
**The question, in plain words:** May Phase 4 and Phase 5 each get one pointer line at their very end, like the early step files (DEC-140) and Phase 3 (DEC-160)? They still read as current, with nothing to say that their wind, composition and founders lines were updated elsewhere.
**The facts:** the Phases 4 and 5 piece (`Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md`), the decisions section. `DR-101` says pass files are never edited; a notice at the top would shift every cited line.
**Options:** A) yes, one line at the end of each, applied only when the dockets are applied, under the same answer as DEC-140 and DEC-160 · B) no, leave the files untouched.
**Recommendation:** A, decided together with DEC-140 and DEC-160.
**What is waiting on it:** nothing is edited. If B, the files keep reading as current.
**Answer (developer):** Yes, all four (Recommended): see DEC-140.

### DEC-181 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Phases 4 and 5 piece (U14)
**The question, in plain words:** Phase 4's Band 5 lists four common items. The readers disagree on whether the taught wind knowledge and the relayed warnings make a fifth. Keep four and record those two as Mirny's own?
**The facts:** the Phases 4 and 5 piece, the decisions section (P4 L238). Two of three readers hold four; one holds a fifth common item.
**Options:** A) keep four common items; record the taught knowledge and the relayed warnings as what is Mirny's own · B) add a fifth common item.
**Recommendation:** A (the reading that changes less).
**What is waiting on it:** nothing is edited; the addendum text is provisional.
**Answer (developer):** Keep four (Recommended): the taught wind knowledge and the relayed warnings are recorded as Mirny's own, not as a fifth common item.

### DEC-182 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Phases 4 and 5 piece (U14)
**The question, in plain words:** The Phase 4 and Phase 5 datasheets have no live tier, language or wind-account rows. May those rows be added after the source figures are re-keyed, as for Phase 3 (DEC-163)?
**The facts:** the Phases 4 and 5 piece, the decisions section. The datasheets are derived sheets, not pass files. Corrected in place or kept beside rides on DEC-141.
**Options:** A) add them, showing you the rows first · B) leave the datasheets as they are.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):** Correct in place, show first (Recommended): see DEC-141.

### DEC-183 · ANSWERED 2026-11-08 (DR-122) · 2026-11-05 · Mirny finish run, Phases 4 and 5 piece (U14)
**The question, in plain words:** Some admitted lines in the reading lists name other locations while carrying Mirny's own relation (a road-access section in the highways file, the subnet member list in the relationship database, a ports legend). Should a single location's run take a relation only from the location's own lines, and the lists be re-keyed to them?
**The facts:** the Phases 4 and 5 piece, the decisions section and the list-defect note: several non-spec spans were never re-keyed and now hold other places' text. No finding uses them; they are recorded as a list defect.
**Options:** A) yes: keep lines that name other locations out of a single location's run; take a relation only from the location's own lines; re-key the lists · B) no, leave the lists.
**Recommendation:** A (it follows the one-location law).
**What is waiting on it:** nothing is edited; the related requests stay open.
**Answer (developer):** Yes (Recommended): a single location's run takes a relation only from that location's own lines; the lists are re-keyed.


### DEC-200 · ANSWERED 2026-11-08 (DR-122) · 2026-11-08 · Mirny finish run, symbols piece (U16) · THE PLANET (HELD, blocks "complete")
**The question, in plain words:** Which Planet should be Mirny's? Three readers, each working alone and each writing down what the place is before opening any symbol file, ranked all eleven Planets the same way: Neptune first, Uranus second, the Sun third. Saturn, the old provisional pick, is not confirmed once the corrected wind account is applied. The evidence cannot cleanly separate Neptune from Uranus.
**The facts:** the symbols piece (`Amendment_Rederivation_ST16_Symbols_2026-11-05.md`), sections 4, 5 and 10.4 (decision 1); the Planet is yours (`DR-115`).
**Options:** A) Neptune, provisional · B) Uranus, provisional · C) the Sun, provisional · D) keep the Planet held.
**Recommendation:** A, PROVISIONAL (confidence low to moderate), with Uranus reserved in case the strongest finding is worded around the single founding learning; Saturn recorded as not confirmed. What decides between Neptune and Uranus is your own wording of the strongest finding (DEC-020): openness favors Neptune, the one founding learning favors Uranus.
**What is waiting on it:** nothing is edited. While the Planet is held, Mirny cannot be called complete (`DR-115`). If B or C, the Element-and-Planet pair and the panel notes change; if D, Mirny stays not complete.
**Answer (developer):** Neptune (Recommended): Mirny's Planet is Neptune, provisional, decided inside Mirny's own ULM; Uranus reserved; Saturn recorded as not confirmed. The Planet hold is lifted.

### DEC-201 · ANSWERED 2026-11-08 (DR-122) · 2026-11-08 · Mirny finish run, symbols piece (U16)
**The question, in plain words:** After the re-test on the corrected wind account, may Air be recorded as Mirny's Element, confirmed, with its one-word label still provisional?
**The facts:** the symbols piece, section 3 and 10.4 (decision 2). All three readers keep Air; the old wind premise appears in the October reasons but carries none of them. Wood is the runner-up and covers only the made half. Earth, rebuilt, was tested and does not fit.
**Options:** A) keep Air, confirmed on re-test, label provisional · B) keep Air exactly as now (provisional) · C) reopen the Element.
**Recommendation:** A, PROVISIONAL (confidence moderate to high). Wood stays reserved.
**What is waiting on it:** nothing is edited; a revisit after the CST rides with DEC-015.
**Answer (developer):** Keep Air, confirmed (Recommended): Air confirmed on the corrected account, its one-word label still provisional; Wood reserved.

### DEC-202 · ANSWERED 2026-11-08 (DR-122) · 2026-11-08 · Mirny finish run, symbols piece (U16)
**The question, in plain words:** The record says "Saturn stays provisional"; the re-test says Saturn is not confirmed. May the status line say both, and may the Planet cell in the registry show only that the Planet is held (no pick in it), while the Element cell reads Air?
**The facts:** the symbols piece, section 7 and 10.4 (decision 3).
**Options:** A) yes · B) leave the cells as they are until DEC-200 is answered.
**Recommendation:** A.
**What is waiting on it:** nothing is edited; the cell texts were inferred because no reader opened Mirny's registry row (a second reader is owed).
**Answer (developer):** Yes (Recommended): Saturn recorded as provisional and not confirmed on re-test; the Planet cell shows the hold only, the Element cell reads Air. (The cell texts stay proposals; a second reader checks Mirny's registry row before anything is applied.)

### DEC-203 · ANSWERED 2026-11-08 (DR-122) · 2026-11-08 · Mirny finish run, symbols piece (U16)
**The question, in plain words:** May the eleven end-of-file marks that point from the October Phase 10 and Step 5 texts to the new symbols piece be added, only when the other corrections are applied, each read by a second reader first?
**The facts:** the symbols piece, sections 8 and 10.4 (decision 4). Pass files are never edited (`DR-101`); a pointer is an edit. It rides with the earlier pointer questions (DEC-140, DEC-160, DEC-180).
**Options:** A) yes, as end-of-file pointers, applied together with the other dockets · B) no.
**Recommendation:** A, decided together with those earlier ones.
**What is waiting on it:** nothing is edited; if B, the October texts keep reading as current.
**Answer (developer):** Yes (Recommended): the Phase 10 and Step 5 marks go in as end-of-file pointers, applied together with the other dockets, each read by a second reader first.

### DEC-204 · ANSWERED 2026-11-08 (DR-122) · 2026-11-08 · Mirny finish run, symbols piece (U16)
**The question, in plain words:** If Mirny's two symbols both read the wind (Air, and Neptune or Uranus), is that acceptable as the place's own defining fact, with a record line naming what the pair leaves unread, and with the fresh Review Panel testing the pair? One reader called the pair tensioned; two called it reinforcing; the piece carries "reinforcing" because it claims less.
**The facts:** the symbols piece, section 5 and 10.4 (decision 5).
**Options:** A) accept the doubling, with the record line and the panel test · B) look for a Planet that reads one half only (this would be the narrow-object error for the whole city).
**Recommendation:** A, PROVISIONAL.
**What is waiting on it:** nothing is edited.
**Answer (developer):** Accept (Recommended): the pair reads the wind as the place's own defining fact, with a record line naming what the pair leaves unread; the fresh Review Panel tests the pair and its class.


### DEC-220 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** The Step 1 and 2 datasheet row that says the spec still lags the Founding Register is now wrong: the spec's founding line was corrected today. Correct that row in place, shown to you first?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) yes, correct it in place, shown first (as DR-122 item 3) · B) leave it and rely on the new piece.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. The row keeps contradicting the corrected spec.
**Answer (developer):**

### DEC-221 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** Open question Q-123 is answered by an earlier ruling (DR-28 D4: the Installation is not assigned), but four pass lines still write it as held. Close it and mark those lines as answered?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) yes, close Q-123 and mark Phase 9 L18 and L82, Phase 10 L16 and Step 6 L265 as answered · B) leave them.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. Four lines keep reading as open.
**Answer (developer):**

### DEC-222 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** Phase 2's L3 still says whether the weather warnings ride the relay is undecided (decided 2026-10-29, DR-76). Step 7 and Step 6 already have a docket row for the same sentence. Give Phase 2's L3 the same row?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) yes · B) no.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. Phase 2 is the only copy of that sentence with no row.
**Answer (developer):**

### DEC-223 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** The amendment layer's own notes (the answers note, the amendment register, the Phase 8 piece, the Phase 6 piece) have not caught up with the rulings on founders, language, the strongest finding, symbols and today's applications. Add one dated end line to each, each read by a second reader first?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) one dated end line on each of the four · B) the answers note only · C) none.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. The notes keep stating the older state.
**Answer (developer):**

### DEC-224 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** Phase 2, Phases 6 to 9 and Step 6 have no end-of-file pointer (your ruling DR-122 named ten files; eleven were applied, and these six were not among them). Give each one pointer, under the same answer as the others, applied with the dockets and read by a second reader first?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) yes, one pointer each · B) no; the pieces stand alone.
**Recommendation:** A, decided together with DEC-140.
**What is waiting on it:** nothing is edited. Those files keep reading as current to anyone who does not know the pieces exist.
**Answer (developer):**

### DEC-225 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** Several pass files cite spec lines in the old 230-line numbering, and Step 7's anchors drifted 2 to 5 lines. Run the line-reference sweep now that the corrections are applied (DR-107 item 3), carrying the offsets by docket at line grain for the eleven files, never by editing the body text?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) yes, run the sweep · B) later.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. The cited lines keep pointing a few lines off.
**Answer (developer):**

### DEC-226 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** Eight of the new pointer lines say "(Act 1)" for the first generation, while the Frame keeps the founders' Act open. Keep the Act open as the Frame ruled, and read "(Act 1)" in the pointers as the founding era until the founding is dated (open request AR-14)?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) keep the Act open; read "(Act 1)" as the founding era · B) the first generation is Act 1 by definition.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. The pointers and the Frame would say different things.
**Answer (developer):**

### DEC-227 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** The Step 6 docket's proposed mark D6-40 is stale against the symbol decisions (DR-122, DR-115) before it is ever applied. Bring its text up to date before the Step 6 docket is applied?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) yes · B) leave it.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. A stale mark would be applied.
**Answer (developer):**

### DEC-228 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** Phase 2's L283 says the native layer is "the only layer ... met without translation". Mark it to be read beside DR-100's common civic tongue, as the Phase 8 piece already does for Phase 8's copy?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) yes · B) leave it.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. The line reads as if the dominant language were unmet.
**Answer (developer):**

### DEC-229 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** Two bookkeeping updates: the Step 5 piece's LC-39 tag, and the Register row's sources cell and the spec line's dated note. Apply them with the next docket application, each shown first (the Register's status column stays yours alone)?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) yes · B) no.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. Two small citations stay stale.
**Answer (developer):**

### DEC-230 · OPEN · 2026-11-08 · Mirny finish run, Step 7 QA re-run piece (ST7b)
**The question, in plain words:** Where the Step 7 re-run is recorded: append the new labeled blocks after Step 7's last line (L2027) and mark nothing inside the October raw section or on its gate-result lines?
**The facts:** the Step 7 re-run piece (`Amendment_Rederivation_ST7b_QAGates_Rerun_2026-11-09.md`), section 9.
**Options:** A) yes · B) mark inside Step 7.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. Step 7's October record is never reworded (DR-102).
**Answer (developer):**


### DEC-240 · OPEN · 2026-11-08 · Mirny finish run, fresh Review Panel
**The question, in plain words:** The duty to go out and restore the relay, seen from inside lives. Eight of the nine panel seats found the same weakness from eight corners: the partner left at the door, a parent with a child in sole care, an elder in decline, someone who wants a person to tell, a student who learns the guilt with the skill, readiness nobody marks, the served end outside, and guilt that presses one way. What should the record carry?
**The facts:** the fresh Review Panel piece (`Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md`), the decisions section.
**Options:** A) carry the cases as characterization and rule nothing now · B) also answer whether guilt reaches someone kept from going by the storm, by decline or by never having learned, and whether a dependent in one's sole care counts for 'most strategically able' · C) rule a release, or a non-compelling way to ask or to tell.
**Recommendation:** A now; B when convenient, because it is a ruling for you (the duty and the guilt are ruled; guilt is not a sanction; who goes out is deferred, DEC-042).
**What is waiting on it:** nothing is edited; the record carries the cases as characterization.
**Answer (developer):**

### DEC-241 · OPEN · 2026-11-08 · Mirny finish run, fresh Review Panel
**The question, in plain words:** Confirm that the first generation's makers, the people who do the city's unseen work, and the city's built face stay unmarked: no day, monument, honor or landmark, the slots left open as 'none sited here'?
**The facts:** the fresh Review Panel piece (`Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md`), the decisions section.
**Options:** A) confirm, with the question of marking the first generation left open for after the CST · B) open it now · C) leave it to the holidays work.
**Recommendation:** A.
**What is waiting on it:** nothing is edited; the refusals are written as characterization.
**Answer (developer):**

### DEC-242 · OPEN · 2026-11-08 · Mirny finish run, fresh Review Panel
**The question, in plain words:** Mirny's work serves claims outside the city (the roads and the chamber chain) and no arbiter is admitted. Keep 'no arbiter; the split is made by whoever is at the haul; the shortfall arrives late and cannot be traced back' as Mirny's character, or name an arbiter?
**The facts:** the fresh Review Panel piece (`Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md`), the decisions section.
**Options:** A) keep it as character · B) name an arbiter.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-243 · OPEN · 2026-11-08 · Mirny finish run, fresh Review Panel
**The question, in plain words:** The warnings' reach: do the protocol and its warnings serve the whole subnet or Mirny only (AR-16), and does a warning reach a visitor (AR-1)? Two earlier pieces pre-decide AR-16 in opposite directions.
**The facts:** the fresh Review Panel piece (`Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md`), the decisions section.
**Options:** A) leave both open; apply only the conditional marks and the datasheet wording fix, shown first · B) rule AR-16 now.
**Recommendation:** A. The warning's form waits on the weather-signs research.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-244 · OPEN · 2026-11-08 · Mirny finish run, fresh Review Panel
**The question, in plain words:** A stranger's stop: the panel's refusal stands while it is unread whether Mirny is a road node. Keep the refusal, or research it with the highways?
**The facts:** the fresh Review Panel piece (`Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md`), the decisions section.
**Options:** A) keep the declined characterization now, research later · B) research now.
**Recommendation:** A now and B later.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-245 · OPEN · 2026-11-08 · Mirny finish run, fresh Review Panel
**The question, in plain words:** PROVISIONAL. The panel's proof of reading failed on the first run: all nine seats had 3 to 8 proof fields wrong (47 in all), mostly middle-line counts across multi-range spans and blank last lines. Each seat re-read and repaired only its own fields, with no values supplied, and the second run was unanimous in all three groups. Your ruling DR-117 allows repair of a single field. Accept this wider repair as the panel's proof of reading?
**The facts:** the fresh Review Panel piece (`Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md`), the decisions section.
**Options:** A) accept, logged as a deviation · B) re-dispatch fresh seats · C) accept, and state the counting convention in the brief or in DR-117 (the middle line counted within the admitted lines across spans; a blank last line written as an empty field).
**Recommendation:** A, with C.
**What is waiting on it:** nothing is edited; the panel record is PROVISIONAL until you answer.
**Answer (developer):**


### DEC-260 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** Today's Step 10 run came before the weather-signs research you ordered ahead of it, so it is only an interim run. Record it as interim, and run Step 10 once more, whole and last, after the research and the open decisions?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes, interim, one more whole run last · B) interim, with the final run narrowed to items 9, 10, 11 · C) this was the one run; the rest closes on your word.
**Recommendation:** A.
**What is waiting on it:** nothing is edited. Until then the condition 'Step 10 run last' is not met.
**Answer (developer):**

### DEC-261 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** Three decisions are deferred, not answered: DEC-042 (who decides who goes out), DEC-080 and DEC-081 (panel seats). Carry them as not answered until you decide each, and list any you keep deferred at close as 'deferred by ruling', as the lived middle is?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes · B) answer them now.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-262 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** Every piece from the repass and the finish run still reads PROPOSED; no ruling accepts any as a whole. Give each piece you accept one dated acceptance line at its end, read by a second reader first?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes, per piece you accept · B) accept them all by one ruling.
**Recommendation:** A.
**What is waiting on it:** nothing is edited; until then each stays PROPOSED.
**Answer (developer):**

### DEC-263 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** Step 7's gates 5, 7, 8, 9, 10, 11, P and G were not re-run on the applied text, and gates 0, 3 and C still fail in part. Re-run those eight before the final Step 10 run, and rule the three partial failures through the Step 7 re-run's docket?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes · B) only the three partial failures.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-264 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** Before any commit: the name scan covered only the 24 new files. Extend it to every surface written since 2026-10-13 (hidden working files and applied rows included, with a positive control), and keep the 2026-11-03 note's one content-class line out of any other place's reading by a docket mark, never by rewording it?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes · B) no.
**Recommendation:** A. Nothing has been committed or pushed since the finish run began.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-265 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** Count the symbols condition as met, recorded as Air (confirmed, label provisional) and Neptune (provisional)?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes · B) not until the provisional labels are lifted.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-266 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** U15 (the in-order fold-in of Steps 5 to 8) is held. Keep it held, and say before the final Step 10 run whether Mirny's completion waits on it?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) keep held and say before the final run · B) run it before the final run.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-267 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** The new name: confirm it is not a readiness condition for Mirny's pass (runs continue under 'Mirny'; the rename sweep comes after the pass, DR-110)?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes, not a condition · B) it is a condition.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-268 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** Set a date for the weather-signs research session (05:00-14:59 window) and keep the stocks research on the readiness list, the founding nation's forms first?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes · B) move the stocks research to a later stage.
**Recommendation:** A.
**What is waiting on it:** nothing is edited; the research has no date yet.
**Answer (developer):**

### DEC-269 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** Add the Step 10 re-run's marks (15 docket rows) as dated notes and end-of-file lines, each read by a second reader first, and bring the amendment register level by its dated end line before the final run?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes · B) no.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-270 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** Apply the Step 9 and 9.5 end-of-file pointers and the late Lover-faculty (T5) pointer in the Review Panel file with the next docket application, each read by a second reader first? (This also lets the phase-check tool see the panel's late marker.)
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes · B) no.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

### DEC-271 · OPEN · 2026-11-08 · Mirny finish run, Step 10 readiness re-run piece (ST10b)
**The question, in plain words:** Name the file that closes Mirny's pass as its handoff, give it the 'what this cannot prove' block, run items 6 and 11 on it in the final Step 10 run, and note the three not-found paths beside the October handoff without rewording it?
**The facts:** the Step 10 readiness re-run piece (`Amendment_Rederivation_ST10b_ReadinessRerun_2026-11-08.md`), section 9.
**Options:** A) yes · B) no.
**Recommendation:** A.
**What is waiting on it:** nothing is edited.
**Answer (developer):**

## Open since 2026-11-09 (Davis cross-check; every answer below is PROVISIONAL until you give yours)

*Written by the finished-city cross-check of Davis on 2026-11-09. Each entry is a question from one of the seven amendment pieces (or from the run itself), stated on the recommended answer, which the piece already proceeds on. Nothing is applied and no pass file is edited. The two questions the earlier pieces asked about four composition rows are not entered because `DR-94` item 4 already answers them (see the erratum `Amendment_Erratum_2026-11-09_DR94_Item4_Four_Rows.md`).*

### DEC-280 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the reader-list tool
**The question, in plain words:** The tool that drafts each phase's reading list writes into the Phase 2 list a file that the city's own Pre-Trip marks as forbidden (the file that maps cities to Concordia districts). May the tool be fixed to skip table rows the Pre-Trip marks with the forbidden sign, and to use the rows of the Pre-Trip's own T8 line?
**The facts:** `Tools/make_t8_required_list.py phase:2` (last changed 2026-10-21) extracts every backticked absolute path in the phase's table rows and does not read the marker; Davis's Pre-Trip row (`00.0_Pre-Trip_Inspection.md` L277) says the file "resolves to nothing admissible" and its Phase 2 T8 line names five admissible rows that do not include it. Found while writing the fresh Davis amendment note (`Amendment_Notes_2026-11-09_Cross_Check.md`, section D, item 1). Every list in this review was hand-trimmed and the file was never read.
**Options:** A) yes, fix the tool and re-run its self-test · B) no, leave it and hand-trim every Phase 2 list.
**Recommendation:** A. The tool is mechanical and a repair may run at any hour (`DR-117` item 4).
**What is waiting on it / what was done provisionally:** nothing is edited; every other city's Phase 2 list built with the tool would carry the same file until it is fixed.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved (A) and done: the reader-list tool skips Pre-Trip rows marked forbidden and reports them as comments; checked on Davis before and after (only Phase 2 changed, 10 entries to 9).

### DEC-281 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, lessons for the rules
**The question, in plain words:** May the process lessons of this run be written into the rules and tools, row by row, as the Mirny lessons were?
**The facts:** The run's log (`Amendment_Log_2026-11-09.md`) records them: (1) when a reading list includes a ruling, scan the ruling log for a later ruling that answers a question the included ruling lists as not decided (the four composition rows, entry DVL-17); (2) state a pass's ground by reading the pass lines, never from a summary of it (DVL-10); (3) give each reader its own private staging folder (DVL-11); (4) generate one brief and read it end to end before dispatching its readers (DVL-14); (5) in briefs, cite the developer's verbatim answer (`LOG` L1711) for "the rulings as they stand govern", not item (4) of `DR-105`, which records it against another location (the Phase 10 piece's record); (6) a record states what a tool returned and what the piece says on a line the orchestrator has read, never its own paraphrase (DVL-16); (7) the helper scripts of this run (a key-numbering script, a post-merge check, a flagged-quote checker, the brief generators) are written against Davis's paths and would have to be made general before any other city uses them.
**Options:** A) approve rows 1 to 6 now, and general versions of the scripts later · B) approve only some rows · C) none.
**Recommendation:** A. Row 7 is a build task, not a rule.
**What is waiting on it / what was done provisionally:** nothing is edited; the run followed the lessons from the point each was found.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved (A) for rows 1 to 6 (row 7 is a build task); the wording is drafted in Research_Logs/Lessons_Into_Rules_Draft_2026-11-09.md and is applied only on the developer's word on the wording. NOT applied.

### DEC-282 · OPEN · 2026-11-09 · Davis cross-check, the Step -1 input contract piece (S1)
**The question, in plain words:** How are the changed lines L109, L167 and L113 carried until they are classified?
**The facts:** The question is entry AM-S1-Q1 in section 5 of the Step -1 input contract piece (S1) (`Amendment_Rederivation_S1_Step_Minus1_Composition_Region_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** carry L109 and L167 in the 161-line read spec with their use held: L167 grounds G3 only conditionally, and L109 grounds nothing. L113 stays struck. Dispatch a small three-reader piece (DR-74) with L109, L167 and L86 in span and a classification-only read of L113, as R-2 was read (classification only, never content; 00.1a L227). The strict 159-line alternative [C] would remove G3's only ground without evidence that the new text is inadmissible, so it is not recommended. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** G3's verified status; R-7; the banner (AM-S1-F12); the LRANGE for later pieces.
**Answer (developer):**

### DEC-283 · OPEN · 2026-11-09 · Davis cross-check, the Step -1 input contract piece (S1)
**The question, in plain words:** The census read spec
**The facts:** The question is entry AM-S1-Q2 in section 5 of the Step -1 input contract piece (S1) (`Amendment_Rederivation_S1_Step_Minus1_Composition_Region_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** adopt `33,390-396,506,650` (10 lines) after the orchestrator confirms that L506 and L650 are Davis's Census I and II rows and that L397-L398 lie outside Davis's block (classification only). Optional [C; A supports it]: admit Section E's name key (L843-L874, L877-L878) so that latest-period names can be read, with L881's founder clause and L883 not used and L884 DO-NOT-FOLLOW. B left the optional part as a developer question without a recommended answer. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** every PROOF block over the census in later pieces.
**Answer (developer):**

### DEC-284 · OPEN · 2026-11-09 · Davis cross-check, the Step -1 input contract piece (S1)
**The question, in plain words:** How the mixed numbering in 00.1 and 00.1a is recorded, since DR-101 forbids fixing it in place
**The facts:** The question is entry AM-S1-Q3 in section 5 of the Step -1 input contract piece (S1) (`Amendment_Rederivation_S1_Step_Minus1_Composition_Region_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** a numbering key in the amendment note, giving each spec citation's numbering (pass-time or current) and its current line, with the pass files never edited (DR-101, DR-102) [A, B, C]. Check the other Davis pass files for the same split [B, C] (AM-S1-R8). Separately, a methodology docket item: the citation-remap tool must remap a file's spec citations all or none, and must not run over finished pass folders without a ruling [A]. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** any reader who follows a citation in 00.1 or 00.1a; docket application.
**Answer (developer):**

### DEC-285 · OPEN · 2026-11-09 · Davis cross-check, the Step -1 input contract piece (S1)
**The question, in plain words:** Is the DR-68 redistribution arithmetic, as DR-90's is, and which ruling applied it to the census?
**The facts:** The question is entry AM-S1-Q4 in section 5 of the Step -1 input contract piece (S1) (`Amendment_Rederivation_S1_Step_Minus1_Composition_Region_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, arithmetic and not an in-world inflow (PROVISIONAL), because DR-90 (LOG L1575) names DR-68's scenario as its own method and calls that method arithmetic. Cite the ruling that applied the census edit (probably DR-69). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-S1-F7 moving from conditional to firm; the qualifier at 00.1 L108-L112; whether any later finding may treat the 23,917 people of that step as arrivals [C]; the SPEC L15 source row.
**Answer (developer):**

### DEC-286 · OPEN · 2026-11-09 · Davis cross-check, the Step -1 input contract piece (S1)
**The question, in plain words:** Is current SPEC L8's shared-heritage clause a restated founding claim?
**The facts:** The question is entry AM-S1-Q6 in section 5 of the Step -1 input contract piece (S1) (`Amendment_Rederivation_S1_Step_Minus1_Composition_Region_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** this pass does not use the clause (another location: not used). The developer checks it against those locations' Register rows at the terminal differentiation stage. Davis's own reading is Australia, REGISTER L59. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** nothing in S1.
**Answer (developer):**

### DEC-287 · OPEN · 2026-11-09 · Davis cross-check, the Step -1 input contract piece (S1)
**The question, in plain words:** Should current L180, L201 and L206-L260 be classified?
**The facts:** The question is entry AM-S1-Q7 in section 5 of the Step -1 input contract piece (S1) (`Amendment_Rederivation_S1_Step_Minus1_Composition_Region_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** record them as not admitted, never classified and not read. Adjudicate them line by line only if a later phase needs them (00.1a L191-L193's rule), never cut or admitted as a range. Have the orchestrator confirm from git that L206-L260 were appended after L181 (AM-S1-R5). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** §4.3's statement; the banner; MAP L4's caveat.
**Answer (developer):**

### DEC-288 · OPEN · 2026-11-09 · Davis cross-check, the Step -1 input contract piece (S1)
**The question, in plain words:** Is the founding-wave roster at current L86 still "legal relation"?
**The facts:** The question is entry AM-S1-Q8 in section 5 of the Step -1 input contract piece (S1) (`Amendment_Rederivation_S1_Step_Minus1_Composition_Region_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** until a reader admitted to L86 classifies it, its roster grounds nothing beyond the Register founder (REGISTER L59). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the L86 row of the strike table (AM-S1-R1).
**Answer (developer):**

### DEC-289 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Step -1 input contract piece (S1)
**The question, in plain words:** Should the M-224 rule require a numeric read spec to name its numbering frame?
**The facts:** The question is entry AM-S1-Q9 in section 5 of the Step -1 input contract piece (S1) (`Amendment_Rederivation_S1_Step_Minus1_Composition_Region_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes; a numeric read spec names the commit or the line count it was computed against [C; A endorsed it in Round 3]. This is a methodology change, and the developer decides it. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** every later contract's read spec (AM-S1-N1).
**Answer (developer):** Answered 2026-11-09 (DR-124): approved (A): a numeric read spec names the commit or line count it was computed against; drafted as row 7 of the same draft. NOT applied.

### DEC-290 · OPEN · 2026-11-09 · Davis cross-check, the Step -1 input contract piece (S1)
**The question, in plain words:** The PROOF EXEMPT line for positional lines carrying the parent subnet's name or a cluster comparison
**The facts:** The question is entry AM-S1-Q10 in section 5 of the Step -1 input contract piece (S1) (`Amendment_Rederivation_S1_Step_Minus1_Composition_Region_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** keep the EXEMPT line, and either amend the standing line to allow the name in file paths or rule that the parent subnet, a Tier 0 input, is not a forbidden name. Use EXEMPT for UEIC L598, because it also carries the cluster comparison. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the PROOF format of later pieces.
**Answer (developer):**

### DEC-291 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Which bar did "Keep the bar, re-ground it" keep?
**The facts:** The question is entry AM-P2-Q1 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** the recorded text governs (LOG L472, L1703). Barred: a gap between two same-tier rows, including which of the top two rows is larger, and the founder's row against Indonesia's. Barred separately, by construction: any difference between rows in who left (SPEC L78). Free: tiers, totals and one row's own headcount, stated flatly. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-F1, AM-P2-F4, AM-P2-F6, AM-P2-F10; the docket rows AM-P2-D7, AM-P2-D17, AM-P2-D27 and AM-P2-D45. Under the wider bar, the clause that the founder's row sits outside the Primary tier and the pooled sets would have to go; no other finding changes (C).
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed as recommended (the review's reading of the bar stands).

### DEC-292 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Are cross-tier statements allowed at tier precision?
**The facts:** The question is entry AM-P2-Q2 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, when written as headcounts and grounded on the tier boundary the spec states (SPEC L78). LOG L472, "The tiers and the city totals are the information.", supports it directly (B). The bar applies only within a tier. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the surviving contrast of AM-P2-F6; the supporting ground of AM-P2-F10; the tier-boundary point of AM-P2-F4.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed as recommended (the review's reading of the bar stands).

### DEC-293 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Should `DR-104` item 1's narrowing of the randomized ground note that the draws also set the refill rows' figures?
**The facts:** The question is entry AM-P2-Q3 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, as a note, with no new bar. The within-tier order of the refill rows is already barred, and the identity of the largest row is set by the draw. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-N13; AM-P2-F4.
**Answer (developer):**

### DEC-294 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Is the ceiling stated at its exact figure, or at about one in ten?
**The facts:** The question is entry AM-P2-Q4 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** about one in ten, with 10.42% at the stated draw in parentheses. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the wording of AM-P2-F4 and AM-P2-D44.
**Answer (developer):**

### DEC-295 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** May a re-derivation use SPEC L28's draw range as a limit, to show that the order of the top two rows is an artifact?
**The facts:** The question is entry AM-P2-Q5 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, as a limit only (S1 L24-25), with the crossover labeled approximate. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the second reason in AM-P2-F4. The bar alone already forbids naming the row.
**Answer (developer):**

### DEC-296 · ANSWERED 2026-11-09 (DR-127) · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** What is the in-world role of Davis's "establishing country", and does it carry standing, in Act 1 and in Act 2?
**The facts:** The question is entry AM-P2-Q6 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** nothing is canon. Leave the slot explicitly open (none is sited here). Write Australia-founded (the Register), with no role attached. Record the two readings of AM-P2-N6 as seeds without choosing between them. No treaty slot may be read as an arrival route. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the second sentence of the restated D5 (AM-P2-F12); the third doubt's replacement (AM-P2-F8); the founded-slot wording (AM-P2-F5).
**Answer (developer):** Answered 2026-11-09 (DR-127): leave it open (A): write "Australia-founded" as the Register records it, with no role attached and the slot marked "none is sited here"; the two readings stay as seeds.

### DEC-297 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** What does the last cell of REGISTER L59 ("—") record, and did the establishing country also send people?
**The facts:** The question is entry AM-P2-Q7 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no ruling is needed now. Add the Register's table-header line to the next piece's reading list (AM-P2-R1). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** only a sentence that would say the founding nation sent the first people, and no such sentence is proposed.
**Answer (developer):**

### DEC-298 · ANSWERED 2026-11-09 (DR-127) · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Did robots come into being on Assembly territory after 2564 and arrive in Tepenia under II.2.1?
**The facts:** The question is entry AM-P2-Q8 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no ruling now. Write: no later arrival is recorded; the robot channel is open in law, and the human channel closed at signing. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-F11; AM-P2-N5; the Act 2 route at AM-P2-D73.
**Answer (developer):** Answered 2026-11-09 (DR-127): NEW CANON, developer verbatim: "humans could continue arriving into Tepenia after the signing. They just weren't allowed back to Upper Earth if they did". This replaces the recommendation's clause "the human channel closed at signing". (The treaty's article II.2.3 fixes who may accompany the robot population without being prevented, namely humans who had settled among robots before the signing; it does not bar later human arrival.) The robot half of the question, whether robots kept coming into being and arriving after 2564, was not answered and stays as recorded: the robot channel is open in law (II.2.1) and no later arrival is recorded.

### DEC-299 · ANSWERED 2026-11-09 (DR-127) · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Are a row's robots counted carriers of its origin practices, and is a robot made in Tepenia assigned a national origin at all?
**The facts:** The question is entry AM-P2-Q9 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). A recommends no: treat the robot columns as weights (SPEC L78), and count a practice's carriers as the row's humans plus an unstated share of founding-era robots. C recommends leaving `H2` open, sizing carriers on the human count, with the total as a conditional upper figure. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** leave `H2` open; size carriers on the human count; show the total only as a conditional upper figure. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the total columns of AM-P2-F15; AM-P2-F19; AM-P2-F21.
**Answer (developer):** Answered 2026-11-09 (DR-127): leave it open (A): practices are sized on the row's human count, the total including robots is shown only as a conditional upper figure, and whether a robot made in Tepenia has a national origin stays open.

### DEC-300 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Can a population-type majority (robots at CI, humans at CII), or the season's calendar, carry a Davis-wide tacit norm?
**The facts:** The question is entry AM-P2-Q10 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** record it as an open hole and route it to Phase 9. Narrow the pass's wording to no majority origin now. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the extension in AM-P2-F13; AM-P2-N21.
**Answer (developer):**

### DEC-301 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Is `DR-4`'s spatial deferral still in force for Phase 2 after `DR-104` item 2?
**The facts:** The question is entry AM-P2-Q11 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. Reading each row's own headcount flatly against a researched threshold is reasoning by headcount, not a spread, a mode or a gap between nations. Keep the bar on spread, mode and spatial claims until it is lifted (K). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-F20; AM-P2-R6; `DR-4`'s full text (AM-P2-R2).
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed as recommended (the review's reading of the bar stands).

### DEC-302 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Does `DR-4`'s bar on distributional results cover a city-wide composition statistic, such as the chance that two residents share an origin row?
**The facts:** The question is entry AM-P2-Q12 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes; keep it barred until `DR-4` lifts. Each row's own headcount read against an external threshold stays legal. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** a possible sharpening of C's out-marriage point in AM-P2-F16, held as a seed meanwhile.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed as recommended (the review's reading of the bar stands).

### DEC-303 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Is a successor row's stock the in-world unit's people, and which territories did the atlas move to Davis's successor rows?
**The facts:** The question is entry AM-P2-Q13 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, the in-world unit's people, read through Census Section E, with the real-world territory as the comparable and the divergence operator applied, never the name alone. Supply the atlas rows, or allow a later piece to read them (AM-P2-R4). Meanwhile write the stock as the people of the territory that passed from the old Russia (or the old Romania). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-F18; AM-P2-F22.
**Answer (developer):**

### DEC-304 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** May rows of one split country be pooled when sizing the carriers of a practice they share?
**The facts:** The question is entry AM-P2-Q14 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, as an aggregation inside Davis's own table. It is not a ranking or a gap between nations. Each row's own distinct practices are still sized on that row alone. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-F17; AM-P2-F13; AM-P2-F15.
**Answer (developer):**

### DEC-305 · ANSWERED 2026-11-09 (DR-128) · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** What does a human exile's origin row record: nationality, or residence at departure?
**The facts:** The question is entry AM-P2-Q15 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no new ruling now. State E.1's human half as conditional: it holds if origin means residence at departure. The treaty's human grounds (II.2.3) are ties to the robot population, not to a place. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-F24.
**Answer (developer):** Answered 2026-11-09 (DR-128): developer verbatim: "the 'origin' row applies to both humans and robots, just at whatever percent makes sense for them". So an origin row covers humans and robots alike, each at its own percentage. The question of nationality or residence at departure was not addressed; the human half of the exile statement stays conditional on "residence at departure" as the recommendation wrote it.

### DEC-306 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Are origin rows read in-world as latest-period territorial labels rather than as 2564 polities?
**The facts:** The question is entry AM-P2-Q16 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, as CENSUS L841 already says for the tables. TREATY L15 shows two row names that also existed as 2564 polities in the draft. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-F18; AM-P2-F22.
**Answer (developer):**

### DEC-307 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Is `DR-25`'s "Records can draw people" row a general mechanism, or a ruling about the one location it names?
**The facts:** The question is entry AM-P2-Q17 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** treat it as specific to that location, and do not apply it at Davis without a Davis-specific ruling. This keeps the one-location law and carries no other location's answer across. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-F27.
**Answer (developer):** Answered 2026-11-09 (DR-124): GENERAL mechanism (B, differs from the recommendation): the row is a general mechanism and Davis may use it.

### DEC-308 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Do `DR-94` item 4 (LOG L1613) and orchestrator result 9 conflict?
**The facts:** The question is entry AM-P2-Q18 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** `DR-94` item 4 governs, as the later ruling. Re-check S1 L40-41 before any finding uses the exact shares of the four rows; meanwhile none does. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-N17; the table notes of AM-P2-F15; AM-P2-D112.
**Answer (developer):**

### DEC-309 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Should treaty-derived findings carry "in the treaty's current draft"?
**The facts:** The question is entry AM-P2-Q19 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). B recommends the qualifier on each treaty-derived finding, and C called B's recommendation right. A recommends stating it once, in the amendment's head, rather than on every line. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** once, in the amendment's head. The treaty stays the mandated canon target (SPINE03 L410-411). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-N16; the treaty-derived parts of AM-P2-F9, AM-P2-F11 and AM-P2-F22; AM-P2-D52.
**Answer (developer):**

### DEC-310 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** Does G4 gain the inherited plant as a strength and its upkeep as a standing cost, and did the inheritance include more than the spec names?
**The facts:** The question is entry AM-P2-Q20 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, conditionally, docketed to a Step 2 piece. State only what is already canon: the infrastructure (SPEC L151) and the documentary record, with the techniques written into it (NNS L21). Record equipment, research data and results, and ongoing datasets as admissible and unstated, an open slot, unless the developer wants to state them. Do not invent them. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-F26; AM-P2-F25; AM-P2-D12.
**Answer (developer):**

### DEC-311 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** May the real station's present-day capacity stand as a comparable for the inherited plant's scale?
**The facts:** The question is entry AM-P2-Q21 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). A: keep it as a labeled comparable (about 90 to 100 people in summer, about 20 in winter), as an infrastructure fact `DR-24` allows, used for nothing about founders. B: leave it out, since a present-day figure says nothing about an in-world plant after five more centuries of rotating maintenance. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** leave it out of any pass wording; keep it in the research log only. The plant's size in 2564 stays unstated. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the scale caution in AM-P2-F26.
**Answer (developer):**

### DEC-312 · OPEN · 2026-11-09 · Davis cross-check, the Phase 2 piece (P2)
**The question, in plain words:** May a re-derivation rely on SCAFFOLD's note that the allocation mechanism outlived the founding decade?
**The facts:** The question is entry AM-P2-Q22 in section 5 of the Phase 2 piece (P2) (`Amendment_Rederivation_P2_Composition_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no. Rest the open-endedness on II.3.2's own text ("in the years following this Treaty's signing"), which suffices. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** nothing; recorded so that the line is not reached for.
**Answer (developer):**

### DEC-313 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Is a shared founding nation in Davis's own line a relation, or only a population-origin fact? (question XC5-38)
**The facts:** The question is entry AM-P5-Q1 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** adopt the first check's answer. Record it as a tie whose basis is the Register and, where a line states it, Hwy 110 (`DR-32`). State no sameness or similarity. Mark what passes along it as an open hole. Demote the Davis half to a population-origin fact, and never exclude it. Add one thing (B, C): the CONN:308 line is recorded as road adjacency plus a named link, not as a shared-founder tie. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F4, AM-P5-F5, AM-P5-F6 and AM-P5-F9, and the wording of the docket rows for PH5:35, PH5:36, PH5:72-73, PH5:303-306 and PH5:383-386.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-314 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** May canon's grades and type labels be carried into the pass? (question XC5-39)
**The facts:** The question is entry AM-P5-Q2 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, but only as canon's own attributed wording on each line. Never sort or compare them, give them no meaning until the grade legend is read, and never use one as evidence of what flows. The same treatment applies to PORTS:559's "principal". (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F7.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-315 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Do the port and air contradictions belong to another item? (question XC5-40)
**The facts:** The question is entry AM-P5-Q3 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** within Phase 5, no. The readers' brief puts the arrival types and the air-access statement in P5, so P5 owns every Phase 5 statement about the port and air. Statements outside Phase 5 go to their own pieces: Phase 4's "road and air", SPINE L555, the spine's figures, and any air statement in `03_Research.md` or Phase 10. Open an item for any that has none. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows AM-P5-D53, AM-P5-D54, AM-P5-D51 and AM-P5-D52.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-316 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** RELDB:193 or PORTS:559 on the inbound route, and how far does the 2026-09-16 ruling reach? (question XC5-41)
**The facts:** The question is entry AM-P5-Q4 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). the first check recommended that PORTS:559 governs because it carries a developer ruling. In Round 3, C withdrew its claim that the route itself is ruled. B had noted that the ruling's parenthesis sits on the import designation, not on the transshipment sentence. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** PORTS:559 governs, PROVISIONALLY. Record the difference without choosing, and put RELDB:193 on the source-fix list. Do not adopt the founding nation as a named supplier. The developer is also asked to say whether the 2026-09-16 ruling covers PORTS:559's route sentence, or only the designation it is attached to. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F14, the in-row of AM-P5-F13, and the docket row AM-P5-D58.
**Answer (developer):** Answered 2026-11-09 (DR-124): the Davis spec as written is correct and open to further additions; "Vladivostok-style" is the developer's phrase and "principal import port" was not his wording; the older relationship-database line that conflicts with the spec's route goes on the source-fix list (not edited).

### DEC-317 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Does XSUB:123-131 need a source fix? (question XC5-42)
**The facts:** The question is entry AM-P5-Q5 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. Flag it for the source-fix list, and do not edit it here. No declassification ruling is needed, because the Register and `DR-32` already give the basis. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-D59.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-318 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Should CONN:308 be recorded as a founding tie at all?
**The facts:** The question is entry AM-P5-Q6 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no. Record a direct-neighbor tie on Hwy 110 plus a named link whose content is undescribed, with canon's label attributed. Do not use the presence clause, which describes another location's composition. Davis's own population-origin fact (REG:59) stays recorded and demoted, so no population-origin finding about Davis is excluded. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F6.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-319 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Does the CONN:304 tie exist, given SPEC L8's "not paired with"?
**The facts:** The question is entry AM-P5-Q7 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** `DR-19` and `DR-32` govern. Record a seed tie on the Register (Australia among both places' founders), with no route stated and nothing said about what passes along it. Read SPEC L8's parenthesis as a statement about subnet membership, and put SPEC L8 and SPEC L153 on the source-fix list. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F4, and the docket rows AM-P5-D6, AM-P5-D32 and AM-P5-D61.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-320 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Are CONN's scientific prospect lines admissible inputs under PSPINE L636?
**The facts:** The question is entry AM-P5-Q8 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** carry them only as canon's attributed prospects (seed), gated on full connectivity, unless the developer rules that an exchange of records counts as trade. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F11, AM-P5-N10, and the wording of the restated count at AM-P5-F9.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-321 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Does CONN:311's "once full connectivity exists" name an in-world condition inside the frame?
**The facts:** The question is entry AM-P5-Q9 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** keep the correction at PH5:355 (an undeveloped prospect). Record the dating question as a seed and characterize nothing. Until the question is answered, no date is inferred. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-N11, and the Phase 6 feed.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-322 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Is the Federation-paid icebreaker channel a parent supply to Davis for 5c, or a national asset sited at Davis?
**The facts:** The question is entry AM-P5-Q10 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** record it as a Federation-paid service sited at Davis that keeps the nation's import port open. That is firm on the text. Do not say it serves Davis's own needs. It fills part of `PA-6` in that scope only, and the provisional-assumption protocol keeps the rest. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F19, and the docket rows AM-P5-D18 and AM-P5-D50.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-323 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Does the port's designation re-open the spine's "Davis was assigned both of its vocations"?
**The facts:** The question is entry AM-P5-Q11 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** record the port as a national function sited at Davis, not as a third vocation of its people. Route any re-test of SPINE L430 and SPINE L436 to the piece that holds Step 2. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F19.
**Answer (developer):** Answered 2026-11-09 (DR-124): differently from the recommendation: the port is part of (though not the entirety of) the local identity. Any re-test of the spine's "both vocations" claim goes to the piece that holds Step 2.

### DEC-324 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Does anyone from beyond Tepenia come ashore at Davis, and who crews the leg from the hubs?
**The facts:** The question is entry AM-P5-Q12 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** leave it as a hole. Write no sea arrival of persons until a line states one. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F17, AM-P5-F18, AM-P5-N5, and Phase 9's outsider question.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-325 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Should Phase 5's axis be replaced, and if so with what?
**The facts:** The question is entry AM-P5-Q13 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** record legs 1 and 2 as killed and leg 3 as standing, and adopt no replacement in the amendment. If the developer wants a replacement, C's is the candidate that A (after withdrawing its own) and C support, and the one that keeps leg 3. Attach B's caution to it: the port is one sector, not the city. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F22, and the docket row AM-P5-D8.
**Answer (developer):** Answered 2026-11-09 (DR-124): the port is one sector, not the whole city; food research and food production are a substantial portion of the city's activity, and the port is in addition to that, not replacing it. Phase 5's central argument is worded on this reading when the amendment is applied.

### DEC-326 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Is CONN:308's Relay Vaults link among "the relay questions" that LOG L1869 lists as not decided?
**The facts:** The question is entry AM-P5-Q14 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** treat the link's content as a hole until those questions are decided. Line L1869 does not say what the questions are. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F6 and AM-P5-R2.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-327 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Should a later round read CONN's header and method lines?
**The facts:** The question is entry AM-P5-Q15 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, as a single span read. Until then the founding-nation ties stand on REG, `DR-19` and `DR-32`. The provenance of the scientific lines, and of canon's grades and labels, stays conditional. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P5-F2.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-328 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 5 piece (P5)
**The question, in plain words:** Does the one-location rule reach real-world territories and Upper-Earth ports named as route points?
**The facts:** The question is entry AM-P5-Q16 in section 5 of the Phase 5 piece (P5) (`Amendment_Rederivation_P5_Relations_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** name them only inside quotations and in research questions. This merge follows that practice PROVISIONALLY. The two Upper-Earth staging ports in RELDB:193 are not named at all. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** wording only. No finding depends on it.
**Answer (developer):** Answered 2026-11-09 (DR-124): approved as recommended (the developer: "Everything else looks fine").

### DEC-329 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Is the national files' arithmetic under `DR-73` the governing answer to Davis's own need?
**The facts:** The question is entry AM-P7-Q1 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. State 186,131 (on the workforce formula, Census I) as the export headcount. Retire the 53 row (withdrawn) and the 120.7 row (it double-books the baseline). No new rule is needed; this is a confirmation only (C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** P7 A.2 L112–123, §F L388–389 and §G L407.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed: Davis's export headcount is 186,131 workers (Census I) with its formula beside it and the dated 44.2% beside it as a flow into a national total; "export" only with "to the rest of the Federation" or "national supply"; no count of persons until the formula's source file is read.

### DEC-330 · OPEN · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Should 320,284 be carried beside 186,131 as an open denominator caveat?
**The facts:** The question is entry AM-P7-Q2 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The first check (`K`) recommended carrying 320,284 "only as the open national denominator caveat (Register item 11)". `K` had no admitted line for `DR-73`. A, B and C each recommend against it, on `DR-73` L1399. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no. Carry 320,284, if at all, as one line that names it the superseded convention's figure (file 16 L2092), inside A.2b's refusal. Never carry it as a caveat on the headcount. Annotate the register (AM-P7-Q9). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** A.2b L130–132, §F, the §A.1 and §A.2 boxes, and receipt L29.
**Answer (developer):**

### DEC-331 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Should the pass carry a people-fed figure?
**The facts:** The question is entry AM-P7-Q3 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** not yet. Carry the worker headcount and the dated share. No people figure and no people fraction enters the pass until two things are settled: the conversion (AM-P7-Q4) and the national human total (AM-P7-R2). If one is ever written, it is a capacity, with both bases stated: "could feed", never "feeds". Keep refusing the third-of-the-country headline. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** A.2b L127–135, and §F's second clause.
**Answer (developer):** Answered 2026-11-09 (DR-124): not yet (A): no people-fed figure.

### DEC-332 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Which difficulty converts a Davis farm worker into people fed?
**The facts:** The question is entry AM-P7-Q4 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Davis's own D (1.25), giving 6.628 people per worker and about 1,233,677 beyond its own humans. Reason: the food term's D is the growing site's, and 1.25 is the rate Davis's own baseline uses. Keep the files' 1.20 for national slack accounting. If a figure is ever carried, give the files' value (1,285,080) beside it (A). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** any people-fed sentence; where the conversion is filed (AM-P7-Q12); file 13 §15, if the answer is 1.20 (AM-P7-R3).
**Answer (developer):** Answered 2026-11-09 (DR-124): not yet: no difficulty factor chosen and no people-fed figure.

### DEC-333 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Should the 44.2% be stated beside the headcount?
**The facts:** The question is entry AM-P7-Q5 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, dated and labeled as 44.2% of the national export-supply headcount, file 19 §5, 2026-11-03. It is secondary to the headcount. It is written as a flow into a national total, never as a rank, and never as a share of the nation's food. The share moves with the national pool and the headcount does not, so the date belongs to the share (A). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** §F and L111.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed: Davis's export headcount is 186,131 workers (Census I) with its formula beside it and the dated 44.2% beside it as a flow into a national total; "export" only with "to the rest of the Federation" or "national supply"; no count of persons until the formula's source file is read.

### DEC-334 · OPEN · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Is the README food-layer carve-out (L8–11) still binding on figures drawn from file 16 §19 and file 19 §5?
**The facts:** The question is entry AM-P7-Q6 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** its named scope (file 04, 05, file 09 and the README's "First results") does not reach those files. Treat it as not blocking the headcount. Keep it binding on the figures it names. Keep Finding 3 binding on any people-fed figure. Check the README after L12 first (AM-P7-R7; C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** P7 receipt L29 and Q.3 L453–457.
**Answer (developer):**

### DEC-335 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Which word should the amendment use for Davis's outward food flow?
**The facts:** The question is entry AM-P7-Q7 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** keep "export" only with "to the rest of the Federation" attached, or write "national supply"; P7 A.4 L163 already rules out food leaving Tepenia. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** §F and A.2.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed: Davis's export headcount is 186,131 workers (Census I) with its formula beside it and the dated 44.2% beside it as a flow into a national total; "export" only with "to the rest of the Federation" or "national supply"; no count of persons until the formula's source file is read.

### DEC-336 · OPEN · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Should the amendment stop naming "Option B" by letter?
**The facts:** The question is entry AM-P7-Q8 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. Name the mandate composition and the distinctive-tier convention (`DR-73`) by their content. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the §A.1 and §A.2 amendment wording.
**Answer (developer):**

### DEC-337 · OPEN · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Should file 16's Register item 11 be annotated with `DR-73`?
**The facts:** The question is entry AM-P7-Q9 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, at the next docket application. It is a source edit, and it blocks nothing in Davis. A and C put the same pointer in their dockets, and C also points at file 16 L2095 and file 19 L50. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** nothing in this piece.
**Answer (developer):**

### DEC-338 · OPEN · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Should §A.5's "SUBSTITUTABLE" and "backfillable" be qualified?
**The facts:** The question is entry AM-P7-Q10 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, with conditional wording (supplemented, not substituted), after the canon source has been read (AM-P7-R1). That the national balance is smaller than Davis's supply line is carried as a seed only. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the §A.5 qualifier (AM-P7-D20); a reading of `National_Medical_and_Care_Institutes.md` L23–25; 05 L104, which `K` reported carries §A.5 as unaffected, and for which no reader proposed a row.
**Answer (developer):**

### DEC-339 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Does the workforce formula count persons, or weighted worker units?
**The facts:** The question is entry AM-P7-Q11 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). A read the count as worker units, on file 17 L18, so the number of persons in the sector would lie between 186,131 and 372,262. A first rated this firm; under the weakest-strength line it is now conditional. B adopted A's reading. C, in Round 3, read file 16 L27 as a participation count (half of humans work, and the count is of working persons). C recommended persons. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** until file 09 §5 is read (AM-P7-R5), carry every count with its formula beside it, and state no count of persons and no share of residents. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the wording of every amended sentence that carries 186,131; whether a share of residents can ever be stated (AM-P7-N2).
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed: Davis's export headcount is 186,131 workers (Census I) with its formula beside it and the dated 44.2% beside it as a flow into a national total; "export" only with "to the rest of the Federation" or "national supply"; no count of persons until the formula's source file is read.

### DEC-340 · OPEN · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** Is the open people-fed conversion filed as H39's residue, or as a new hole?
**The facts:** The question is entry AM-P7-Q12 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). B writes H39 as closed for the headcount and still open for any people-fed conversion. A and C close H39 and hold the conversion as a different, narrower question, unnumbered, for the developer to number. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** A and C's form. It gives H39 no subject beyond the one P7 L407 states (C's ground). The conversion stays open in this amendment, unnumbered (AM-P7-R9), and the developer numbers any successor hole. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the wording of the H39 row (AM-P7-D26).
**Answer (developer):**

### DEC-341 · OPEN · 2026-11-09 · Davis cross-check, the Phase 7 piece (P7)
**The question, in plain words:** May a path in a reader's reading log carry a forbidden name?
**The facts:** The question is entry AM-P7-Q13 in section 5 of the Phase 7 piece (P7) (`Amendment_Rederivation_P7_Export_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** withhold the name in the reading log, as C did. The PROOF header carries the full path in any case, so nothing is lost, and the log reproduces no forbidden name. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** future briefs only; nothing in Davis.
**Answer (developer):**

### DEC-342 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** Is a Davis-built robot's vernacular Hawaiian, plus the language of whoever had her built? (the first check's XC6-37)
**The facts:** The question is entry AM-P89-Q1 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes (PROVISIONAL). DR-100 item (1) makes Hawaiian dominant everywhere, and PHYS L426 ties the Module's delivery to the language of the dominant local culture and of the builders. Leave the builders' language open wherever the building community is not specified. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** The P9 L92 row (AM-P89-D20); AM-P89-F5; AM-P89-F6; AM-P89-F7.
**Answer (developer):** Answered 2026-11-09 (DR-124): yes: a Davis-built robot's vernacular is Hawaiian (later Tepenian) plus the builders' language, left open wherever the building community is not specified; "local" means the city; no origin language is written as delivered by the Module itself; robots are not written as lacking the supporting-tier languages; any Davis accent is marked not written.

### DEC-343 · OPEN · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** Should H48's group half stay open, now on DR-100 item (5) instead of DR-4? (XC6-38)
**The facts:** The question is entry AM-P89-Q2 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes (PROVISIONAL). Do not work out home languages from origin shares. The hole reads the 45 origin rows, not communities: whether a row forms a speech community is itself unwritten (A, B; C withdrew its wording). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** The H48 split (AM-P89-D16).
**Answer (developer):**

### DEC-344 · OPEN · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** Carry English, Mandarin, Japanese and German as ruled, with German's dependency flagged? (XC6-39)
**The facts:** The question is entry AM-P89-Q3 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes (PROVISIONAL). Record the margins (+0.530 with Austro-Bavaria, −0.860 without) and the real-world check (Standard German as the written, media and education language of Bavaria and Austria) in the flag. The flag names the mapping, not the ruling (A). DR-100 is not reopened. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** The amendment-note line (AM-P89-D32).
**Answer (developer):**

### DEC-345 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** Within 2564–2812, when does Hawaiian become Tepenian, and is that a renaming or a successor language?
**The facts:** The question is entry AM-P89-Q4 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Write Hawaiian (later Tepenian), undated, in Davis's amendment, mirroring DR-100. Settle the timing in the national-language canon, not at Davis (A). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P89-F4; every naming of the dominant language in the amendment.
**Answer (developer):** Answered 2026-11-09 (DR-124): yes: a Davis-built robot's vernacular is Hawaiian (later Tepenian) plus the builders' language, left open wherever the building community is not specified; "local" means the city; no origin language is written as delivered by the Module itself; robots are not written as lacking the supporting-tier languages; any Davis accent is marked not written.

### DEC-346 · OPEN · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** Does DR-12's first ground (LOG L1703 item (1)) bar a pass sentence that relies on the tier boundary between two origins of the same tier (Japan in, Korea out)?
**The facts:** The question is entry AM-P89-Q5 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** The tier stands as DR-100's output. No pass finding may rest on a particular origin's being outside it: state the tier and stop. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P89-N1.
**Answer (developer):**

### DEC-347 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** In PHYS L426, is the "local" of the dominant local culture the city?
**The facts:** The question is entry AM-P89-Q6 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, the city (PROVISIONAL), consistent with PHYS L217. At Davis the Module's first input is then Hawaiian, and any origin language arrives only through the builders' half. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P89-F5; AM-P89-N3.
**Answer (developer):** Answered 2026-11-09 (DR-124): yes: a Davis-built robot's vernacular is Hawaiian (later Tepenian) plus the builders' language, left open wherever the building community is not specified; "local" means the city; no origin language is written as delivered by the Module itself; robots are not written as lacking the supporting-tier languages; any Davis accent is marked not written.

### DEC-348 · OPEN · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** How should a city pass answer the spine's what-marks-someone-as-from-here (ULM03 L988-L989) under the rule of one location on its own terms?
**The facts:** The question is entry AM-P89-Q7 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). B keeps, as firm: "What marks someone as from Davis, as far as Davis's own lines go, is how they make a claim: they reach for the dated entry." A routes any claim of distinctiveness to the terminal differentiation check (A XA-10 (d), XA-29). C's proposed wording ("includes how they make a claim") is already peer-free, and C accepted A's question in Round 3. K adds that saying the four-language set marks someone as from Davis would mean comparing it with sets elsewhere, which belongs to the terminal check (K XC6-20)... The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Answer it peer-free, by stating the speech habits a person from here carries (AM-P89-F10 (a)). Send any reading of it as setting Davis apart, including whether a pronunciation would set a speaker apart, to the terminal differentiation check. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** The P8 L255 wording (AM-P89-D9).
**Answer (developer):**

### DEC-349 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** Does the Language Module deliver any supporting-tier language? Does it deliver a local form of the dominant language or a national standard?
**The facts:** The question is entry AM-P89-Q8 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Leave both open. Do not write robots as lacking the supporting languages; a pass may state only the Module's two named inputs (A). Mark any Davis accent as not written until ruled (B). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P89-N4; AM-P89-N6; AM-P89-F9.
**Answer (developer):** Answered 2026-11-09 (DR-124): yes: a Davis-built robot's vernacular is Hawaiian (later Tepenian) plus the builders' language, left open wherever the building community is not specified; "local" means the city; no origin language is written as delivered by the Module itself; robots are not written as lacking the supporting-tier languages; any Davis accent is marked not written.

### DEC-350 · OPEN · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** Does the supporting tier hold across the whole frame, both Acts, or does it thin in the Act 2 part?
**The facts:** The question is entry AM-P89-Q9 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Carry it across the frame as ruled: DR-100 gives no date, and the shares are "identical between censuses" (SPEC L78). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** The §E switching sentence (AM-P89-D12).
**Answer (developer):**

### DEC-351 · OPEN · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** In what language or languages is Davis's record kept, inherited and current?
**The facts:** The question is entry AM-P89-Q10 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Leave it open as a new hole; never infer it from the real-world station's operator (DR-19). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P89-N14; any later pass that uses show me the entry in a scene.
**Answer (developer):**

### DEC-352 · OPEN · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** Should the amendment note record that the tier's membership depends on the English bloc's range as well as on Austro-Bavaria?
**The facts:** The question is entry AM-P89-Q11 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, as a flag only (PROVISIONAL). The ruled convention is applied, not changed. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P89-N9; AM-P89-D33.
**Answer (developer):**

### DEC-353 · OPEN · 2026-11-09 · Davis cross-check, the language piece for Phases 8 and 9 (P89)
**The question, in plain words:** Should Phase 8 §E.2's exclusions be struck in the docket, and a new hole opened for Davis speech features?
**The facts:** The question is entry AM-P89-Q13 in section 5 of the language piece for Phases 8 and 9 (P89) (`Amendment_Rederivation_P89_Language_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes (PROVISIONAL). The exclusions go (AM-P89-K4, AM-P89-K5, AM-P89-K6, AM-P89-K7); the new hole is at AM-P89-D13. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P89-F9; AM-P89-F10.
**Answer (developer):**

### DEC-354 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 10 piece (P10)
**The question, in plain words:** Does a developer-sourced character draft sited in Davis count as a §31 notable figure in Davis's Second Interwar catalog, when its only dated residence there is the post-frame present day?
**The facts:** The question is entry AM-P10-Q1 in section 5 of the Phase 10 piece (P10) (`Amendment_Rederivation_P10_Character_Draft_2026-11-09.md`). All three readers recommend this. It agrees in substance with the first check's recommended answer, with two narrowings: drop that answer's "not canon", and add the frame date (AM-P10-K12). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no, not as an entry. Record it as a documentation note in §F.3, with: the roster ID; the present-day date, after the frame; her status, recorded and not adopted. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P10-D10, AM-P10-D12, AM-P10-D6, AM-P10-D7.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed as recommended: a documentation note, not a notable-figure entry; roster ID only, "not yet named"; status wording "developer-sourced character draft, in development; its siting is developer-sourced; its status is the developer's to state"; present-day residence only; dependency city to character only.

### DEC-355 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 10 piece (P10)
**The question, in plain words:** What should the catalog call the draft's status?
**The facts:** The question is entry AM-P10-Q2 in section 5 of the Phase 10 piece (P10) (`Amendment_Rederivation_P10_Character_Draft_2026-11-09.md`). This is A's wording, which claims least. B's (a character in development; name to be chosen; siting developer-sourced) and C's (a character draft, not a §31 entry) are equivalent. All three refuse "not canon" (B, Round 3). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** neither "canon" nor "not canon". Use: *developer-sourced character draft, in development; its siting is developer-sourced; its status is the developer's to state.*. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the wording of AM-P10-D12.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed as recommended: a documentation note, not a notable-figure entry; roster ID only, "not yet named"; status wording "developer-sourced character draft, in development; its siting is developer-sourced; its status is the developer's to state"; present-day residence only; dependency city to character only.

### DEC-356 · OPEN · 2026-11-09 · Davis cross-check, the Phase 10 piece (P10)
**The question, in plain words:** Is the project repo's own `Worldspace/Characters/` a mandatory Phase 10 sweep target alongside the two MUST OPEN sources, and is the sweep run by the location's canon epithets as well as its name?
**The facts:** The question is entry AM-P10-Q3 in section 5 of the Phase 10 piece (P10) (`Amendment_Rederivation_P10_Character_Draft_2026-11-09.md`). A, B and C all recommend yes, and the first check's second recommended answer agrees. The epithet half is B's, and A and C accepted it at Round 3. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, on both counts. The receipt names every folder searched, with its result. The search is case-insensitive and covers every text file type. Every hit is checked in context. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P10-D3, AM-P10-D17 and AM-P10-D19; the method row AM-P10-D24, which is a methodology change, made with the runbook in the same commit.
**Answer (developer):** Not selected on 2026-11-09 (the developer approved items (1) to (3) only); left open, no rule written.

### DEC-357 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 10 piece (P10)
**The question, in plain words:** How does Davis's catalog refer to the draft?
**The facts:** The question is entry AM-P10-Q4 in section 5 of the Phase 10 piece (P10) (`Amendment_Rederivation_P10_Character_Draft_2026-11-09.md`). A: the roster ID "STP-06", stated as not yet named, with the folder path only as a file address. B: the roster ID alone, with "name to be chosen". C: the folder ID plus the folder path, with the label allowed only inside a quotation of README L11 that carries its status. At Round 3, A sent the point to the developer, noting that the full path carries the descriptors in its last segment. B called the difference not real. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** the roster ID only in the catalog's prose, with "not yet named"; the folder path only in a source citation; the working label and the folder's descriptors never in the catalog. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P10-D12, AM-P10-D3.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed as recommended: a documentation note, not a notable-figure entry; roster ID only, "not yet named"; status wording "developer-sourced character draft, in development; its siting is developer-sourced; its status is the developer's to state"; present-day residence only; dependency city to character only.

### DEC-358 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 10 piece (P10)
**The question, in plain words:** Did her Davis residence begin inside the frame, before 2812?
**The facts:** The question is entry AM-P10-Q5 in section 5 of the Phase 10 piece (P10) (`Amendment_Rederivation_P10_Character_Draft_2026-11-09.md`). B and C hold it open as a reserved finding rather than a question (AM-P10-R2). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** treat it as present-day only until a line says otherwise (A). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P10-D12, and whether the answer to AM-P10-Q1 changes.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed as recommended: a documentation note, not a notable-figure entry; roster ID only, "not yet named"; status wording "developer-sourced character draft, in development; its siting is developer-sourced; its status is the developer's to state"; present-day residence only; dependency city to character only.

### DEC-359 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Phase 10 piece (P10)
**The question, in plain words:** Does the dependency between Davis's finished pass and the STP-06 draft run from the city to the character only?
**The facts:** The question is entry AM-P10-Q6 in section 5 of the Phase 10 piece (P10) (`Amendment_Rederivation_P10_Character_Draft_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. This is already the observed direction (README L22–25 and L45; DR-105 item 5). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P10-D18.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed as recommended: a documentation note, not a notable-figure entry; roster ID only, "not yet named"; status wording "developer-sourced character draft, in development; its siting is developer-sourced; its status is the developer's to state"; present-day residence only; dependency city to character only.

### DEC-360 · OPEN · 2026-11-09 · Davis cross-check, the Phase 10 piece (P10)
**The question, in plain words:** Does the new §L row cover STP-06 only, or STP-06 and any later character sited in Davis?
**The facts:** The question is entry AM-P10-Q7 in section 5 of the Phase 10 piece (P10) (`Amendment_Rederivation_P10_Character_Draft_2026-11-09.md`). B's row covers later characters as well. A's and C's rows cover STP-06 only. A and C both sent the scope to the developer at Round 3. B did not withdraw its wider scope. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** STP-06 only, until the sweep rule at AM-P10-Q3 is settled (A). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the heading of AM-P10-D18.
**Answer (developer):**

### DEC-361 · OPEN · 2026-11-09 · Davis cross-check, the Phase 10 piece (P10)
**The question, in plain words:** Is Disanalogy B's cartographer sentence kept, now that B is narrowed?
**The facts:** The question is entry AM-P10-Q8 in section 5 of the Phase 10 piece (P10) (`Amendment_Rederivation_P10_Character_Draft_2026-11-09.md`). A reads the sentence as contested inside the spine: the environment "can be learned from written observation because it is STATIONARY" (`02_Spine.md` L164), and the record "documents the terrain" (L262, as A quotes it). B and C keep the cartographer argument for the observation method. All three sent the point to the developer at Round 3. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** drop the cartography claim from the restated B, which needs only the serial obligation with no completion moment. B and C both lean this way. Whether `02_Spine.md` L431 ("a landscape no document could describe") itself needs amending is routed to the piece that owns the spine (C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P10-D6, AM-P10-K13.
**Answer (developer):**

### DEC-362 · OPEN · 2026-11-09 · Davis cross-check, the Phase 10 piece (P10)
**The question, in plain words:** Does the B3 (Planet + Element) determination for Davis belong to this Phase 10 amendment, or to a separate unit?
**The facts:** The question is entry AM-P10-Q9 in section 5 of the Phase 10 piece (P10) (`Amendment_Rederivation_P10_Character_Draft_2026-11-09.md`). B: it belongs to the Phase 10 amendment, as a piece of its own. A: it is owed, outside this piece, and routed to whoever is cleared to open the three symbol files. C: a developer question, leaning to A's routing, because this piece's scope is notable figures. The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** a separate unit outside P10, with the three symbol files in its list. Following B's sequencing, run it after the earlier phases' amendments are verified, because B3 reads the location's own Phases 1–9 first (`03` L1166). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P10-D20, AM-P10-D22.
**Answer (developer):**

### DEC-363 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** The character draft (XU5-35, refined): Does the character draft sited in Davis (roster ID STP-06) count as a character sited for Phase 10's zero?
**The facts:** The question is entry AM-S5-Q1 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no, inside the frame. Record the merged wording in AM-S5-F20: no canon character sited in Davis inside the frame; one developer-sourced draft sited there after the frame (about 2822 to 2827); whether it counts was put to the developer and not answered (LOG L1704). Drop XU5-35's clause "whose README cites the pre-rework composition" (AM-S5-N4). Keep the label neutral: A, B and K call the draft unratified, while C keeps to what LOG L1704 records; the neutral wording is the narrower. *Waiting:* 05:131, 05:146, Phase 10 §F.3. Disposition: `confirmed by all three` (the recommendation); `conflict resolved to the narrower reading` (the label). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):** Answered 2026-11-09 (DR-124): confirmed as recommended: a documentation note, not a notable-figure entry; roster ID only, "not yet named"; status wording "developer-sourced character draft, in development; its siting is developer-sourced; its status is the developer's to state"; present-day residence only; dependency city to character only.

### DEC-364 · OPEN · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** The composition row (XU5-36): Should Step 5 carry the check files' composition conflict as its own reconciliation row, with the spec governing, the correction outside the pass, and a new hole?
**The facts:** The question is entry AM-S5-Q2 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, in the text of AM-S5-F26. State that no Step 5 finding rests on the stale text; record the correction as not decided (LOG L1529, L1616), not as needed; record DR-85's coverage of the two files as conditional on the list it cites; number the hole when the amendment is applied. *Waiting:* Step 5 §2 and §8; whether the check files are corrected now or kept as they are under DR-85. Disposition: `confirmed by all three`. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):**

### DEC-365 · OPEN · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** Re-tagging §1 (XU5-37, refined): Should §1's amendment be kept and re-tagged, with an independent ground sought?
**The facts:** The question is entry AM-S5-Q3 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. Keep the finding. Tag LC §4 as *a conclusion read last as a check; corroboration only (INPUT L629-631)*, not as self-originated, because column 3 is for migrated canon (INPUT L492-494, L596-597) and LC is the prior culture-pass file itself. Record SPEC L141 as the tier 1 ground of the physical leg, and open research AM-S5-R1 for the timing leg. As the first check noted, this is a pre-existing issue, and the developer may prefer to treat it apart from the U-5 items (K). *Waiting:* 05:33, 05:49-54, 05:198-202; the strength of Phase 6 §A.2's amendment. Disposition: `confirmed by all three`. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):**

### DEC-366 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** LC §4's light-cycle dates: Does DR-103's condition, "If the number of days for polar night is just a plain numerical value, then we can do it now." (LOG L1693), cover LC L61's dates and "roughly two months"? The ruling named L53 only.
**The facts:** The question is entry AM-S5-Q4 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. Correct L61 to the spec's dates, with the counting convention stated, outside the pass. Until then `H61` stays open for §4 only. *Waiting:* `H61`'s status. Disposition: `found by two` (B, C); A withdrew its direct docket row in favor of this question in Round 3. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):** Answered 2026-11-09 (DR-124): done on the developer's word ("go ahead and correct the three lines (61, 45, 47)"): L45, L47 and L61 of the Davis culture sheet were corrected (309 lines before and after); both day counts are stated in L61.

### DEC-367 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** The counting convention: Should the 54-against-55 midnight-sun difference be recorded with its convention, and where? Split: A recommends stating both counts in the amendment record (*about 54 to 55 days: the spec counts both ends of its span, 55; DR-103's count at 68°35′S, 54*) and changing neither file; C recommends a short note beside SPEC L99-100 and L138 that the spans count both end dates; B accepted both as additions.
**The facts:** The question is entry AM-S5-Q5 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** state both counts in the amendment record and change neither file. *Waiting:* the wording of `H61` for §3. Disposition: `conflict sent to the developer`. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):** Answered 2026-11-09 (DR-124): done on the developer's word ("go ahead and correct the three lines (61, 45, 47)"): L45, L47 and L61 of the Davis culture sheet were corrected (309 lines before and after); both day counts are stated in L61.

### DEC-368 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** Credit kinship: (a) Is the credit-kinship row out of frame as a convergence, because T16's only stated ground for the norm is a founding-era decision with no admitted line? (b) May the mechanism still be carried at proposal strength through RC L98-100's fit with robot biology canon (Ch.11)? (c) What, if anything, is done to T16 L2103-2105?
**The facts:** The question is entry AM-S5-Q6 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** (a) yes (A, B, C). (b) The readers split: A reads RC L98-100 as a fit, not a ground; C reads it as a second stated ground that keeps the mechanism in frame at RC's level, at proposal strength; B cannot test it, since Ch.11 is in no list. Recommended, the narrower: do not carry the mechanism through RC L98-100 until Ch.11 is read and the developer rules; Phase 7 §C.1 stands only on a derivation of its own. (c) The readers split: A would drop the incident clause; C would add a provenance clause and mark the incident clause as non-canon; B would leave T16 unedited and record the note's provenance in the amendment. Recommended, the narrower: B's. *Waiting:* 05:125, 05:205-206, Phase 7 §C.1 (AM-S5-R3). Disposition: `conflict sent to the developer`. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):** Answered 2026-11-09 (DR-124): hold (A): the row is out of frame as a convergence; the mechanism is not carried through the robot-biology canon (Chapter 11) until Chapter 11 is read and the developer rules; the old note's text stays unedited and the amendment records its provenance.

### DEC-369 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** The real-world port comparison at LC L164: Was it part of the 2026-09-16 port ruling? Split: A recommends treating it as not part of the ruling until the developer confirms; B recommends using it neither way until the ruling's verbatim text is read; C flags it for confirmation.
**The facts:** The question is entry AM-S5-Q7 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** B's; it is used neither way until the ruling text is read (AM-S5-R8). 05:147's withdrawal of the history-file wish stands either way. *Waiting:* the docket row for LC L164. Disposition: `conflict sent to the developer`. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):** Answered 2026-11-09 (DR-124): the Davis spec as written is correct and open to further additions; "Vladivostok-style" is the developer's phrase and "principal import port" was not his wording; the older relationship-database line that conflicts with the spec's route goes on the source-fix list (not edited).

### DEC-370 · OPEN · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** Glitch-coolant against tier 2: Accept the narrowed reading of 05:127, that no named drinking-culture institution is recorded, because tier 2 (SPEC L167) places most non-work time in bars, eateries and social establishments?
**The facts:** The question is entry AM-S5-Q8 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, PROVISIONAL on S1's hold on SPEC L167. *Waiting:* 05:127; the tag on Phase 8 §A.4; T16 L2084. Disposition: `found by two` (A, B); C withdrew "stands" in Round 3. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):**

### DEC-371 · OPEN · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** The headline: Should the narrowed wording of AM-S5-F3 be adopted for Phase 6 §A.2's amended text?
**The facts:** The question is entry AM-S5-Q9 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. *Waiting:* Phase 6 §A.2's amended text. Disposition: `found by one` (B). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):**

### DEC-372 · OPEN · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** `H65`: Is the PORTS L559 sentence "this coast is not the only place the Federation pays for one" enough to record the channel's payer, with the base and operator left open?
**The facts:** The question is entry AM-S5-Q10 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. *Waiting:* the `H65` row; P5's items 5c and 5e. Disposition: `found by one` (B). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):**

### DEC-373 · ANSWERED 2026-11-09 (DR-124) · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** The check-file sentences behind `H62`: Should LC L45 and L47 be corrected now, and under which ruling?
**The facts:** The question is entry AM-S5-Q11 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, under DR-19 (the operator is never a reason) and the namesake rule (05:161-163), as a check-file correction outside the pass. *Waiting:* `H62`. Disposition: `found by one` (C); A accepted it in Round 3. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):** Answered 2026-11-09 (DR-124): done on the developer's word ("go ahead and correct the three lines (61, 45, 47)"): L45, L47 and L61 of the Davis culture sheet were corrected (309 lines before and after); both day counts are stated in L61.

### DEC-374 · OPEN · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** Robot departures (question only, from U-5 item 8): Were robot departures between the censuses selective by generation or mark?
**The facts:** The question is entry AM-S5-Q12 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** leave it unanswered. The Gen/Mark null stands, and no default is written. *Waiting:* nothing in Step 5. Disposition: `found by one` (C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):**

### DEC-375 · OPEN · 2026-11-09 · Davis cross-check, the Step 5 piece (S5)
**The question, in plain words:** A methodology observation: When a Step 5 re-sourcing makes the later-read file a leg's own ground, should that leg be named as grounded in the check file itself, and an independent ground sought (AM-S5-N14)?
**The facts:** The question is entry AM-S5-Q13 in section 5 of the Step 5 piece (S5) (`Amendment_Rederivation_S5_Reconciliation_2026-11-09.md`). The sources and the readers' reasoning are in that piece's findings and merge record (section 9).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. No rule is changed by this piece. *Waiting:* the runbook's Step 5 text, at the developer's direction. Disposition: `found by one` (B). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the docket rows of the piece that cite this entry; nothing is edited.
**Answer (developer):**


## Open since 2026-11-09 (Sinheung cross-check; every answer below is PROVISIONAL until you give yours)

*Written by the finished-city cross-check of Sinheung on 2026-11-09. Each entry is a question from one of the six amendment pieces (or from the run itself), stated on the recommended answer, which the piece already proceeds on. Nothing is applied and no pass file is edited. The entries are cut from section 5 of each piece by script; the reasoning, the sources and the readers' splits are in the piece named in each entry.*

### DEC-376 · OPEN · 2026-11-09 · Sinheung cross-check, the sheet builders
**The question, in plain words:** The startup file says a finished city that lacks its Pre-Trip and datasheets gets them built first with the two builder tools. Both tools refuse Sinheung. May the tools be given Sinheung's entry (its row in their city tables) so the sheets can be built for the next pass, or is a hand-built reading list for each piece the rule for finished cities?
**The facts:** `Tools/build_pretrip.py Sinheung --write` and `--out` print "unknown city key 'Sinheung'"; `Tools/build_datasheets.py Sinheung --out` stops with `KeyError: 'Sinheung'`; `build_pretrip.py --list` puts the city under "Not built by this generator: its ULM pass is complete (Tri-Cities)" (the tool's own table, line 144). Nothing was written, no tool was edited, and `--force` was not used. Found while writing the fresh Sinheung amendment note (`Amendment_Notes_2026-11-09_Cross_Check.md`, entry SNH-020).
**Options:** A) leave the tools as they are; finished cities' reading lists are built by hand from the note and the pass, as in this run · B) add Sinheung to both tools' tables (a mechanical repair that may run at any hour, `DR-117` item 4) and build its Pre-Trip and datasheets, then re-run nothing already recorded.
**Recommendation:** A for this run (it changes nothing already recorded and every list here was hand-trimmed from the city's own files); B only if a later full re-pass of this city is wanted. PROVISIONAL: this run proceeds on A.
**What is waiting on it / what was done provisionally:** nothing is edited; no Pre-Trip or datasheet exists as an input to any piece in this run.
**Answer (developer):**

### DEC-377 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Which convention scores a nation's distance from a city: its legal zones, or its solar zone at its population centers?
**The facts:** The question is entry AM-P2-Q1 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The Register gives Korea a gap of 3 (REG L62; LOG L930); legal time gives 4; the composition file scores cities by solar longitude (COMP L30) and nations by legal zones in its own worked example (COMP L38-42); LOG L540 calls the window "the ±3 solar-UTC window". The readers' answers differ: A recommends that the Register's stated gap govern founders, that UTC+9 stay only as a labeled legal-time fact, and that the composition file state its reckoning for nations; B recommends solar at the population centers, ... Waiting on it: the wording of P2 A.4 (AM-P2-D12), the outer-edge list, P2 section F's first item (AM-P2-D21), AM-P2-Q14 and AM-P2-D68. Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** the Register's figure governs every founding sentence; this piece changes no Notable admission; the composition file states which convention it uses for nations, and the choice between legal and solar is the developer's. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the wording of P2 A.4 (AM-P2-D12), the outer-edge list, P2 section F's first item (AM-P2-D21), AM-P2-Q14 and AM-P2-D68. Disposition: conflict sent to the developer.
**Answer (developer):** Answered 2026-11-09 (DR-125): the Register's figure governs every founding sentence; which convention the composition file uses to score a nation's distance (legal or solar zones) is left open (A).

### DEC-378 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** What is the ruled cluster called?
**The facts:** The question is entry AM-P2-Q2 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The readers' answers differ: A keeps the ruled label (LOG L1712) and states the members every time ("the East Asian cluster as ruled (Korea, Japan, the Sinian Federation)"), accepting the three Jeju-do parties as a gloss after Round 3; B names it by its members ("the Korea–Japan–Sinian Federation cluster") and keeps "East Asian cluster" only as the ruling's recorded label; C names it by its members or as "the Jeju-do parties". All three drop the pass's word "core". Waiting on it: every docket row that names the cluster. Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** keep the ruled label and state the members every time; drop "core"; "the Jeju-do parties" may stand beside it as a conditional gloss (AM-P2-N10). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** every docket row that names the cluster. Disposition: conflict sent to the developer.
**Answer (developer):** Answered 2026-11-09 (DR-125): keep the ruled label "East Asian cluster" AND list the members individually each time (Korea, Japan, the Sinian Federation); the pass's word "core" is dropped. The developer: "both A.) keep the 'East-Asian cluster' designation, and also, B.) list them individually as members".

### DEC-379 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** May a pass pool the thirteen Russian-named rows back into "Russia" for a distance argument?
**The facts:** The question is entry AM-P2-Q3 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no, not as one nation. Name each row by its current name and zone; a pool needs a stated reason and is labeled as the thirteen Russian-named rows (6.47%), separate origins, never as "Russia". All three readers adopt the first check's recommended answer. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-D15 (deleted on this answer).
**Answer (developer):**

### DEC-380 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Where do Taiwan and Manchuria, Mongolia, East Turkestan and Tibet go?
**The facts:** The question is entry AM-P2-Q4 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** unpooled, as separate origins; not added to the ruled cluster; no finding on their decimals. No reader found a local ground for patterning them, which the first check's recommended answer had allowed (B). All three agree. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the P2 A.2 text (AM-P2-D5, AM-P2-D6).
**Answer (developer):**

### DEC-381 · ANSWERED 2026-11-09 (DR-128) · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Does DR-12's caution extend to a cross-tier pooled sum whose side of 50% depends on the membership chosen?
**The facts:** The question is entry AM-P2-Q5 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, as a working rule: state 47.85% as arithmetic of the ruled cluster, a plurality, and let no in-world claim about imposing or a bloc rest on which side of 50% a pooled share falls; nor let any claim of "can impose" or "cannot impose" rest on a share (B's extension). Added grounds: the ruled figure contains two random draws (A); the side flips on one 2.86-point Notable row (C); the research band for dominance starts at 45% (B). All three agree. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-D7, AM-P2-D9, AM-P2-D35, AM-P2-D52.
**Answer (developer):** Answered 2026-11-09 (DR-128): yes, as a working rule (A): state 47.85% as arithmetic of the ruled cluster, a plurality, and rest no in-world claim of imposing or of a bloc on which side of 50% a pooled share falls.

### DEC-382 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Does "practical reach" (NNS L9) need a measure for this city?
**The facts:** The question is entry AM-P2-Q6 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no new measure now; cite only the Register's ground for the founding; record practical reach as unmeasured, not as impossible; keep Sinheung's own access lines as context (AM-P2-N6). All three agree. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** nothing blocks; any later founding or arrival-route finding.
**Answer (developer):**

### DEC-383 · ANSWERED 2026-11-09 (DR-128) · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Should the bloc verdict be stated as conditional on DRQ-11 (the rock allocation)?
**The facts:** The question is entry AM-P2-Q7 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes; the rock is the one scarce good the admitted lines name, and an origin-keyed allocation of it would be the classic bloc mechanism (A; B and C name the same seam). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-D29, AM-P2-D31, AM-P2-D40.
**Answer (developer):** Answered 2026-11-09 (DR-128): yes (A): the "no bloc" verdict is stated as conditional on the rock allocation, which is the one open seam.

### DEC-384 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Should the two mid-pools survive as anything?
**The facts:** The question is entry AM-P2-Q8 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** only as descriptive labels for rows where a sentence needs them ("Southeast Asian-origin rows"; "Baltic, Hungarian and Bulgarian-origin rows"), with no finding on a pooled share and no claim of shared practice beyond what research gives each member (A); B and C hold them as candidate readings only, which is the same limit. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-D49, AM-P2-D52, AM-P2-D53.
**Answer (developer):**

### DEC-385 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** How is a documented real-world practice projected onto a stock that left in 2564?
**The facts:** The question is entry AM-P2-Q9 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** as seed, labeled "real-world proxy", for some households of the stock, then the divergence operator on this place's own inputs (A; C's household-share qualifier; B agrees). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** every practice line in P8 A.3 (AM-P2-D49).
**Answer (developer):**

### DEC-386 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Is Phase 8 A.3 a claim about the human population only?
**The facts:** The question is entry AM-P2-Q10 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes; record the robot half's relation to food preservation as an open slot (none is sited here), and do not keep P8 L159's storage parallel (A, B and C; A withdrew its reading of L159 as an existing relation). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the A.3 scope line and AM-P2-D51.
**Answer (developer):**

### DEC-387 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Should Phase 2's composition be re-stated at Band 5, as a shape and its modes?
**The facts:** The question is entry AM-P2-Q11 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes, within this amendment, using AM-P2-F2 item 1: tier sums stated as arithmetic, with no claim that the Notable tail outweighs the founder (A; B and C wrote to Band 5). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-D5, AM-P2-D6.
**Answer (developer):**

### DEC-388 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Should Phase 8's named starting stock follow the tiers, with the shared thing widened to preservation in the broad sense?
**The facts:** The question is entry AM-P2-Q12 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes: Korea, then Japan, Germany and the Sinian Federation; the ruled cluster as the one ruled pool; the mid-pools only as candidate readings; preservation, not fermentation, as the shared category (B, C, and the first check's recommended answer, which B widens). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-D45, AM-P2-D49, AM-P2-D55.
**Answer (developer):**

### DEC-389 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Should Japanese-derived process words be treated as national vocabulary, not as local origin markers?
**The facts:** The question is entry AM-P2-Q13 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes (B; A and C as findings). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-D53.
**Answer (developer):**

### DEC-390 · ANSWERED 2026-11-09 (DR-128) · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** Does the ±3 window re-test rows created by splitting a large-pool country (Austro-Bavaria and West Papua, at distance 4 by legal zone)?
**The facts:** The question is entry AM-P2-Q14 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no; a successor row carries its parent's admission by headcount (CENSUS L841: "A country that split is written as its successor states, each taking its share of the old country's people"), and a note records the distance (B, C). B's first form of the question also asked about a newly added share within a row (Austria); B withdrew that half in Round 3, because no admitted line puts an Austria share in this city's row (AM-P2-N13). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the outer-edge list; P2 section F.
**Answer (developer):** Answered 2026-11-09 (DR-128): carry the parent's admission (A): a successor row keeps its parent's admission by headcount, and a note records the distance.

### DEC-391 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** What replaces "a singularly Korean city"?
**The facts:** The question is entry AM-P2-Q15 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** "a Korea-founded Tepenian city", with "singularly" used only of the founding (SPEC L9; NNS L136-139; ROBOT L229-230) (C; B; A adopted it in Round 3). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-D36, AM-P2-D38, AM-P2-D61, AM-P2-D63.
**Answer (developer):**

### DEC-392 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phase 2 chain piece (P2)
**The question, in plain words:** May real-world comparables that involve South Asian-origin populations be used as evidence?
**The facts:** The question is entry AM-P2-Q16 in section 5 of the Phase 2 chain piece (P2) (`Amendment_Rederivation_P2_Composition_Chain_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Several do: Mauritius (Hindus about 47.8%; C); Varshney's Indian cities (B, C); Suriname's Hindustani parties (C); and the Indian share listed in Malaysia's 1957 census (B). The project carries a standing rule: "No South Asian population, anywhere in Tepenia" (P2 L176). A raised this for the developer; B flagged its own case in its snags; no reader proposed a ruling.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** keep them as labeled real-world evidence pending a ruling; none places any population in Tepenia, and nothing in this piece rests on them alone (each conclusion they support is also supported by another comparable: Posner's group-size work, the Ruhr, Hawaii, Singapore or the Kazakh SSR). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P2-F2 item 4 and AM-P2-F3 item 3.
**Answer (developer):** Answered 2026-11-09 (DR-125): keep the comparables as labeled real-world evidence (A); none places any population in Tepenia and nothing rests on them alone.

### DEC-393 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 9 retention piece (P9)
**The question, in plain words:** Is Sinheung's Census I → II retention gap to be read as an in-world outcome of the orbital exit, or only as arithmetic of the census?
**The facts:** The question is entry AM-P9-Q1 in section 5 of the Phase 9 retention piece (P9) (`Amendment_Rederivation_P9_Retention_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. A ruling in the lists settles this for another location only (LOG L1711-1712; another location: not used). No admitted ruling names this city. Disposition: confirmed by all three (K also asked it).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Read the current rows as the city's in-world figures: the steps that produced them are authoring, but their results are the census of record, and CENSUS L22-23 frames Census II as post-orbital-migration. State the direction flatly (robots 81.62%, humans 83.09%). Attach no cause sized to the gap. Keep B.1 only as an unsized candidate reason, and B.2 only as a demoted, unnoticed structural fit, not a reason. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P9-D3 to AM-P9-D8, AM-P9-D11, AM-P9-D17 to AM-P9-D25, AM-P9-D28 to AM-P9-D31, AM-P9-D34, AM-P9-D35.
**Answer (developer):**

### DEC-394 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phase 9 retention piece (P9)
**The question, in plain words:** Is Census I → II read, by convention, as migration only, or as net change?
**The facts:** The question is entry AM-P9-Q2 in section 5 of the Phase 9 retention piece (P9) (`Amendment_Rederivation_P9_Retention_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Split named. A recommends keeping the migration convention (Step 2 rule 2 as the Spine cites it; CENSUS L22-23) and stating it in the amendment as a convention, so that "Nobody died" and the gap are not read as observed quantities. B recommends reading the rows as net, writing "remained in the count", and glossing "not loss" as not war loss; B would accept A's labeled convention as an alternative. C takes A's disposition and rejects the war-loss gloss, which reinterprets a rule whose text was in no reader's list. Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** State the counts as net (firm), and keep the migration reading only as a labeled convention, not as an observed count. Write "remained in the count" where a figure is given. Do not gloss the rule's "not loss". (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P9-D5, AM-P9-D6, AM-P9-D18, AM-P9-D23; the strength of AM-P9-N1.
**Answer (developer):** Answered 2026-11-09 (DR-125): net counts ("remained in the count"); the migration reading is kept only as a labeled convention; the rule's "not loss" is not glossed (A).

### DEC-395 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 9 retention piece (P9)
**The question, in plain words:** B.2 needs residents to register the pairing of their line's history with the city's work, and C.4 rules that the pairing is not noticed. Where is that tension resolved?
**The facts:** The question is entry AM-P9-Q3 in section 5 of the Phase 9 retention piece (P9) (`Amendment_Rederivation_P9_Retention_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: confirmed by all three (after Round 3; A withdrew its earlier answer, an unarticulated fit kept as a candidate).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** This piece records B.2 as a demoted seed, described as unnoticed (consistent with C.4), and makes no change to C.4. The piece that owns C.4 checks the conjunction, without elapsed-time reasoning (AM-P9-N13). If that piece finds the conjunction noticed, B.2 could return as a candidate reason (B's limit). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P9-D28, AM-P9-D35.
**Answer (developer):**

### DEC-396 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 9 retention piece (P9)
**The question, in plain words:** Split catalog row 3, and which inheritance tag does 3a carry?
**The facts:** The question is entry AM-P9-Q4 in section 5 of the Phase 9 retention piece (P9) (`Amendment_Rederivation_P9_Retention_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Recommended answer. Split. 3a is the place fact, tagged Adapted (canon facts, local consequence), matching the pass's own row 4, with depth Deep. 3b is the candidate reason, tagged Genuinely emergent, with depth Surface. Keeping "Genuinely emergent" for 3a is defensible if the developer reads the combination as the pass's own synthesis (B, C). Disposition: confirmed by all three (after Round 3).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Split. 3a is the place fact, tagged Adapted (canon facts, local consequence), matching the pass's own row 4, with depth Deep. 3b is the candidate reason, tagged Genuinely emergent, with depth Surface. Keeping "Genuinely emergent" for 3a is defensible if the developer reads the combination as the pass's own synthesis (B, C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P9-D34, AM-P9-D36, AM-P9-D38.
**Answer (developer):**

### DEC-397 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 9 retention piece (P9)
**The question, in plain words:** Should the amendment call H − R the "gap" rather than the "spread"?
**The facts:** The question is entry AM-P9-Q5 in section 5 of the Phase 9 retention piece (P9) (`Amendment_Rederivation_P9_Retention_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: found by two (A, C; K also noted it).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Yes, "gap", in the amendment only. Nothing already recorded is reworded (DR-102). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P9-D3, AM-P9-D17, AM-P9-D34.
**Answer (developer):**

### DEC-398 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 9 retention piece (P9)
**The question, in plain words:** Which measure does "a third of a working life is unclaimed" refer to?
**The facts:** The question is entry AM-P9-Q6 in section 5 of the Phase 9 retention piece (P9) (`Amendment_Rederivation_P9_Retention_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Split named. K and C in Round 1 read it as approximating the free share; C withdrew its wording in Round 3. A and B hold the measure unnamed. Disposition: conflict resolved to the narrower reading.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Name the measure from its source (D16 L1838-L1840; AM-P9-R3), or drop the figure. If it is the free share in the city's own determination, write 30.532%, about three-tenths, with its base stated only once the source says what it is a share of. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P9-D31.
**Answer (developer):**

### DEC-399 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 9 retention piece (P9)
**The question, in plain words:** Should the amendment record the physiology candidate (AM-P9-N2)?
**The facts:** The question is entry AM-P9-Q7 in section 5 of the Phase 9 retention piece (P9) (`Amendment_Rederivation_P9_Retention_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: found by one (C).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Yes, as one sentence marked "national baseline, not a finding of this city", conditional on orbital-tier canon (AM-P9-R4). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the amended wording of Spine L116-119.
**Answer (developer):**

### DEC-400 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** Is D16's free tier ever to be read as residents' leisure or time of their own?
**The facts:** The question is entry AM-P4-Q1 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: K (C-5's question), and answered by A, B and C. Disposition: confirmed by all three. Raised by: K (C-5's question), and answered by A, B and C. Disposition: confirmed by all three.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** no. Read it only as work that neither survival nor the national mandate claims: a headcount of workers in the city's chosen sectors (D16 L27, L1840, L1897-1904). Drop "of life" (P4 L202) and "of a working life" (P4 L52, L94 and L130; P8 L30; P9 L190-191). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P4-D28, AM-P4-D33, AM-P4-D42, AM-P4-D47 and AM-P4-D51.
**Answer (developer):**

### DEC-401 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** Keep "time that is your own" (P4 L193), re-cited to canon and scoped to robots, or drop it?
**The facts:** The question is entry AM-P4-Q2 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: K (C-5's recommended answer); A, B and C. Disposition: conflict sent to the developer. Raised by: K (C-5's recommended answer); A, B and C. Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** drop the phrase as written. If the developer prefers to keep it, keep it only in the scoped form above, cited to canon and never to the free tier. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P4-D41 and AM-P4-D42.
**Answer (developer):** Answered 2026-11-09 (DR-125): the phrase is kept and DEFINED, so that future runs read it one way. The developer: "specify what it actually means, in clear terms, so that future runs don't misinterpret it", then "Yes, write it exactly so". Definition: "time that is your own" means canon's leisure and nothing else. (1) For robots, leisure is a fact of life and is owed to nobody: hours that belong to nobody, so that a robot's freedom is real rather than granted, and a condition of staying sane. (2) For everyone, human and robot, there is the shared night, when all stop at the same time for different reasons. It does NOT mean the free tier (the 30.5% headcount of workers in work the city chose), it does NOT mean any share of a person's life is free, and it says nothing about human leisure beyond the night, which canon does not state.

### DEC-402 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** Which measure does canon's line "measures the thing the exile was for" belong to under the three-tier model?
**The facts:** The question is entry AM-P4-Q3 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: A, B and C. Disposition: conflict sent to the developer. Raised by: A, B and C. Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** hold the line out of the free-tier sentences, and attach it to no tier figure until the developer rules. B's and C's mapping to the 58.2% share is the alternative. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P4-D33, AM-P4-D44, and AM-P4-R9.
**Answer (developer):** Answered 2026-11-09 (DR-125): attach the line to no tier figure until the developer rules (A); the mapping to the 58.2% share stays recorded as the alternative.

### DEC-403 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** Where does the Band 5 deferral statement go?
**The facts:** The question is entry AM-P4-Q4 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: K (U-1's question); answered by A, B and C. Disposition: conflict resolved to the narrower reading. Raised by: K (U-1's question); answered by A, B and C. Disposition: conflict resolved to the narrower reading.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** the statement of AM-P4-F11 goes in full in this amendment. Each pass file that states the band gets an end-of-file pointer only, never a header pointer (AM-P4-N7). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** every band row of the docket, from AM-P4-D1 to AM-P4-D20.
**Answer (developer):**

### DEC-404 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** Should the spec's DR-68 and DR-90 parentheticals carry a label, and in whose words?
**The facts:** The question is entry AM-P4-Q5 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: K (U-1's question); answered by A, B and C. Disposition: conflict sent to the developer. Raised by: K (U-1's question); answered by A, B and C. Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** the census's own words. They add no new label, and they keep the word relocation from being read as an arrival. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P4-D52 and AM-P4-D53.
**Answer (developer):** Answered 2026-11-09 (DR-125): a new label, "arithmetic redistribution" (this differs from the recommendation, which was the census's own words).

### DEC-405 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** Does Band 5 carry its own density for the area need?
**The facts:** The question is entry AM-P4-Q6 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: A and C as a question; B as a reserved request. Disposition: confirmed by all three. Raised by: A and C as a question; B as a reserved request. Disposition: confirmed by all three.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** use the refreshed table as ruled (DR-103 item 4): about 101–145 km² at 10,000 and 7,000 per km², until a Band 5 density is stated. - The finding that the footprint lies mostly off the rock holds at any density below about 25,000 per km² (C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P4-D38 and AM-P4-D4.
**Answer (developer):**

### DEC-406 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** Does DR-105 item 4 answer DRQ-11?
**The facts:** The question is entry AM-P4-Q7 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: A; B and C hold it answered in method. Disposition: conflict resolved to the narrower reading. Raised by: A; B and C hold it answered in method. Disposition: conflict resolved to the narrower reading.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** DR-105 item 4 settles the division method: Census I share, as arithmetic. - Whether it is the whole of DRQ-11 waits on DRQ-11's own text. - This city's figure is computed where the three cities' Census I figures sit, not in this single-location piece. - Which side people live on is deferred by DR-4. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P4-D40, AM-P4-D45 and AM-P4-D9.
**Answer (developer):**

### DEC-407 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** Is D16's roster complete, so that its standing provisional rule no longer applies to §17?
**The facts:** The question is entry AM-P4-Q8 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: A and B. Disposition: found by two. Raised by: A and B. Disposition: found by two.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** label the split determined (D16 §17; DR-103 item 2), citing D16's standing caveats once (L466-467, L45-46, L1891-1895), rather than calling it provisional on the old ground. If the developer declares the roster complete, drop the roster caveat. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P4-D25, AM-P4-D33, AM-P4-D44 and AM-P4-D47.
**Answer (developer):**

### DEC-408 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** At Band 5, is what is genuinely common to all base-level work, or part of the deferred analysis?
**The facts:** The question is entry AM-P4-Q9 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: B and C; A in Round 3. Disposition: conflict resolved to the narrower reading. Raised by: B and C; A in Round 3. Disposition: conflict resolved to the narrower reading.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** - Statements true for everyone by mechanism stand as base-level facts, and are marked base-level: the shared night, the melt, the thin-glove climate, the road. - They are not presented as the performed Band 5 common list. - The spread, the modes and the complete common-to-all list belong to the deferred analysis. - Majority or modal claims are marked as deferred-distribution points. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P4-D59, AM-P4-D60 and AM-P4-D49.
**Answer (developer):**

### DEC-409 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** Does DR-4's interim clause also cover a pass's reliance on the other district-derived assumptions?
**The facts:** The question is entry AM-P4-Q10 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: B; with A's and C's readings. Disposition: conflict sent to the developer. Raised by: B; with A's and C's readings. Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** DR-4's words cover only the two §2.2 obligations. Until the developer rules, the amendment states the deferral, marks the point statements, and claims no further cover. A sector standing in for the city is a 00b error at any band whatever the answer. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P4-F15 and AM-P4-R7.
**Answer (developer):** Answered 2026-11-09 (DR-125): only the two named obligations (A): the amendment states the deferral, marks point statements as point statements, and claims no further cover.

### DEC-410 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 4 and Frame piece (P4)
**The question, in plain words:** Should the spine's Phase 4 must-open list point to the city's own D16 determination, not to Half B and D09 §3.5?
**The facts:** The question is entry AM-P4-Q11 in section 5 of the Phase 4 and Frame piece (P4) (`Amendment_Rederivation_P4_Free_Share_and_Band_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by: B. Disposition: found by one. A and C adopted it in Round 3. Raised by: B. Disposition: found by one. A and C adopted it in Round 3.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** yes. Word it as the city's own determination where one exists, else Half B, and mark D09 §3.5 superseded as a result. As a methodology change, the runbook changes in the same commit. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P4-D58, and the next city pass's Phase 4.
**Answer (developer):**

### DEC-411 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 8 language piece (P8)
**The question, in plain words:** In the Second Interwar frame, is the dominant language written as Hawaiian or as Tepenian, and from what year does Tepenian apply?
**The facts:** The question is entry AM-P8-Q1 in section 5 of the Phase 8 language piece (P8) (`Amendment_Rederivation_P8_Language_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: confirmed by all three.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Write Hawaiian (later Tepenian), exactly as DR-100 (1) words it (LOG L1669), and leave the year open until it is ruled. Do not tie the change to Act 2 by inference (B). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the wording of the proposed F.0 and F.1; AM-P8-F6; AM-P8-N13.
**Answer (developer):**

### DEC-412 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 8 language piece (P8)
**The question, in plain words:** Does the language rule enter this city's 8f only through the re-derivation?
**The facts:** The question is entry AM-P8-Q2 in section 5 of the Phase 8 language piece (P8) (`Amendment_Rederivation_P8_Language_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. LOG L1670 lists "how the rule enters a finished pass" under not applied yet (K). Disposition: found by two (A, C; B did not raise it).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Yes: only in the amendment piece appended beside the pass, under LOG L1711 ("Yes: a re-derivation uses the rulings as they stand") and DR-101. The finished pass is not edited. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** how the proposed F.0, F.1 and F.2 are filed.
**Answer (developer):**

### DEC-413 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 8 language piece (P8)
**The question, in plain words:** Does a supporting-tier language count as an identity marker under the Act 2 law, or only as a working language?
**The facts:** The question is entry AM-P8-Q3 in section 5 of the Phase 8 language piece (P8) (`Amendment_Rederivation_P8_Language_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: confirmed by all three.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Only as a working language. Any mark of locality is derived from the city's own data, not assumed from the tier. The city's own figures support this answer: at most 16.08% of residents can follow Korean by human Korean descent, and robots have no genetic descent (AM-P8-N18); inside the city, following Korean marks nobody, because it is assumed of everyone (AM-P8-F5). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the identity sentences of the proposed F.1; AM-P8-F5.
**Answer (developer):**

### DEC-414 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phase 8 language piece (P8)
**The question, in plain words:** Does a robot built here receive Korean through the Language Module, through community life, or both?
**The facts:** The question is entry AM-P8-Q4 in section 5 of the Phase 8 language piece (P8) (`Amendment_Rederivation_P8_Language_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question in full. RP L426 says robot vernacular "tracks the dominant local culture and the community who had her built", with the mechanism not yet determined. Under DR-100, the dominant local culture carries the dominant language (AM-P8-F9). In a city with a supporting tier, does the Module also deliver the supporting-tier language (here Korean), or is that left to community life? Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** A's and B's: leave the mechanism open; robots built here follow Korean as the city's people do, and the amendment says nothing about the channel. C's reading of what a building community may add is recorded as one possibility for the developer to rule on. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P8-F9; the robot clause of the proposed F.0; AM-P8-F8 (the newly online robot); AM-P8-N13; AM-P8-N14; AM-P8-N19.
**Answer (developer):** Answered 2026-11-09 (DR-125): leave the mechanism open (A): robots built here follow Korean as the city's people do, and the amendment says nothing about the channel.

### DEC-415 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 8 language piece (P8)
**The question, in plain words:** Does DR-100 (2)'s "people can be assumed to follow" cover robots exactly as humans?
**The facts:** The question is entry AM-P8-Q5 in section 5 of the Phase 8 language piece (P8) (`Amendment_Rederivation_P8_Language_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: found by one (C; A and B reasoned the same way inside their findings, and B adopted C's citation in Round 3).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Yes. The ruling says people; NNS L76 counts robots among the "People (whether human or robot)" who develop new cultures (C); and RP L191 applies the culture and identity rulings to robots "exactly as to humans" (A). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P8-F5; AM-P8-F9; the proposed F.0.
**Answer (developer):**

### DEC-416 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phase 8 language piece (P8)
**The question, in plain words:** Is the Hawaiian of the Falkland Treaty the same language later called Tepenian, whose core DR-85 describes as a pidgin between English and Japanese, or does one description supersede the other?
**The facts:** The question is entry AM-P8-Q6 in section 5 of the Phase 8 language piece (P8) (`Amendment_Rederivation_P8_Language_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** A's: leave it open. All three agree on the working caution, which holds until it is ruled: no word of Japanese or English origin in this city is credited to its own Japan or English-mapped rows as a local survival without checking that it is not national vocabulary. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P8-N5; the caution in AM-P8-F13; AM-P8-F6.
**Answer (developer):** Answered 2026-11-09 (DR-125): NEW CANON, developer verbatim: "'Hawaiian' is a Pidgin between a primary base of English and Japanese, with a supporting base of Korean, Tagalog, Ilocano, and Mexican Spanish. Later in the future, further influence from a wide variety of languages) resulted in Hawaiian later becoming Tepenian". So Hawaiian and Tepenian are one language over time. Consequence for the pieces (the reviewer's reading, not the developer's words): the national-vocabulary caution covers words of English and Japanese origin and of the supporting bases (Korean, Tagalog, Ilocano, Mexican Spanish).

### DEC-417 · OPEN · 2026-11-09 · Sinheung cross-check, the Phase 8 language piece (P8)
**The question, in plain words:** Should 8f carry an explicit open slot for switching between the dominant language and Korean?
**The facts:** The question is entry AM-P8-Q7 in section 5 of the Phase 8 language piece (P8) (`Amendment_Rederivation_P8_Language_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: found by one (B).
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Yes. Write it as having no data, with none sited here, until a speaker count or the deferred Band 5 spread exists, and fill nothing by invention. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P8-N4; AM-P8-D21.
**Answer (developer):**

### DEC-418 · OPEN · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** Does Resettled require a predecessor population?
**The facts:** The question is entry AM-P3-Q1 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question. Does the Resettled modifier (01 §1.1) require a prior population, or can a prior staffed installation's plant and paper satisfy it? Asked by A and C; B named it as a need. Disposition: confirmed by all three.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** It requires a prior population. Documents and equipment belong to the type's inherited plant. The readers word "population" in three ways: - A: people who lived there as a home; - C: a population whose ways reach the second; - B: a predecessor population whose relation to the newcomers can be written. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P3-F5, AM-P3-F6, AM-P3-D6 and AM-P3-D7, and whether AM-P3-F4 moves from conditional to firm.
**Answer (developer):**

### DEC-419 · OPEN · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** Does DR-25 admit an inherited institution?
**The facts:** The question is entry AM-P3-Q2 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question. LOG L639 (DR-25) says "inherited [xyz] institution/tradition/etc" citations are fine, apart from the tradition wording. Does that admit an inherited institution from a station in general, or only approve that wording in the files the ruling names? K's question. A, B and C concur with K's answer. Disposition: confirmed by all three.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Only the latter (K; A, B, C). - Read "institution" there as inherited infrastructure or records, referred to in an institution's terms. - Institutional continuity stays barred (NNS L15, L156 item 6, L170). - The ruling's own sentence scopes it to named files (LOG L640-641, L647). One of those files, the DoI README, restates the inheritable set with no institution in it (K). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P3-F12 (what stays), and the rows that strike "institutional" wording (AM-P3-D31, AM-P3-D43).
**Answer (developer):**

### DEC-420 · OPEN · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** May unspecified prior occupancy bear on who the city is?
**The facts:** The question is entry AM-P3-Q3 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question. May an unspecified prior occupancy of the plant ("this ground was someone's before ours") bear on the city's self-understanding, as distinct from the operator nation? K's question. A, B and C concur with K's answer. Disposition: confirmed by all three.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** No. - NNS L15: "The rotation's only job is explaining functional infrastructure across the gap". The operator is never a reason for identity (LOG L632). - The bar cannot rest on NNS L7's swap test, which does not reach an unnamed predecessor (B). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P3-F8, AM-P3-D41 and AM-P3-D42.
**Answer (developer):**

### DEC-421 · OPEN · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** Record the closed items as resolved upstream?
**The facts:** The question is entry AM-P3-Q4 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question. Should the Frame's docketed "deep institutional roots" phrase be recorded as resolved upstream by spec L211, without editing the pass? And should the same treatment cover the Frame's Gate 0 defect (spec L4) and Recon L181-182 (spec L4, L211; sheet §2 L34)? K's question, widened by A, B and C. Disposition: confirmed by all three.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Yes to both, as current facts with their addresses (DR-102). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P3-D9, AM-P3-D12 and AM-P3-D32.
**Answer (developer):**

### DEC-422 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** What replaces spec L213's "against" clause?
**The facts:** The question is entry AM-P3-Q5 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question. In spec L213, does "against Russia's purely physical, non-diplomatic presence at the original station" mean the builder's long-past construction, or a presence at the time of the court? What wording replaces it? Asked by A, B and C. Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Strike the "against" clause and add nothing. Leave the Register's basis (the allocation, plus geography) as it stands. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P3-D35, and the Register's source citation (Register L62).
**Answer (developer):** Answered 2026-11-09 (DR-125): strike the clause and add nothing (A); the Register's basis stands; the spec's clause goes on the source-fix list and is not edited.

### DEC-423 · OPEN · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** Should "Russia was not a party to the Jeju-do court at all." stay?
**The facts:** The question is entry AM-P3-Q6 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question. Spec L211 ends with this sentence, Frame L200 repeats it, and sheet §2 L34 carries a variant. Should it stay? Asked by C; B gave the same treatment for Frame L200; A adopted it in Round 3. Disposition: found by two.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** - It may stay in the spec, as the developer's record. - Do not carry it into any characterization (identity, politics, psychology), because there it gives the operator a role by negation (C). - Frame L200 is not needed by any finding (B). - The ground is LOG L632. NNS L170 is not used; see AM-P3-N5. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P3-D11 and AM-P3-D40.
**Answer (developer):**

### DEC-424 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** May real-world plant facts stand as what the exiles inherited in 2564?
**The facts:** The question is entry AM-P3-Q7 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question. May the amendment treat the real-world plant facts (1988 to 2022/23) as what the exiles inherited in 2564, or state only the admitted categories? Asked by A and C, with different answers. Disposition: conflict sent to the developer.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** State only the categories, and use the real-world facts as comparables. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P3-F2, AM-P3-F3, AM-P3-N3, the four seeds, and any scale claim about the plant.
**Answer (developer):** Answered 2026-11-09 (DR-125): categories only; the real-world plant facts are used as comparables (A).

### DEC-425 · OPEN · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** Should this amendment site any uptake of the station's material?
**The facts:** The question is entry AM-P3-Q8 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question. Should this amendment site any of the station's records, research, equipment or techniques as taken up by the city (DR-26)? Asked by B. Disposition: found by one.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** No, not in this amendment. - Leave the slot open: none is sited here. - Carry the seeds to the later finished-city review, where a phase can test them against its own research. - Take the moving-ice seed first, because it touches the spine's heaviest standing cost (B). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P3-F2, AM-P3-K17 and AM-P3-D23.
**Answer (developer):**

### DEC-426 · OPEN · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** How should a later piece treat the sheet's §31 placeholder figure?
**The facts:** The question is entry AM-P3-Q9 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Raised by A, B and C, with split readings. Disposition: conflict resolved to the narrower reading.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Not as evidence: the sheet is Tier 3. Treat it as a pointer only, for whichever piece owns Phase 10's figures, to check two things: - whether the pass's Phase 10 catalog already carries it (Recon L145 says of the second figure, "the pass had carried only one"); - whether it reads as plant uptake (admissible) or as continuity. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** the uptake slot (AM-P3-K17).
**Answer (developer):**

### DEC-427 · OPEN · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** Re-declare G7, and widen the Phase 1 canon list?
**The facts:** The question is entry AM-P3-Q10 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question. For amendment pieces, should G7 be re-declared as a plant input (infrastructure, records, research, equipment, techniques; the operator excluded)? And should the method's Phase 1 canon list (03 L337, and its runbook mirror §C.8c) carry the full DR-24 to DR-26 set? Asked by C; A and B adopted the 03 L337 point in Round 3. Disposition: found by one.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Yes to both (C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P3-D15, AM-P3-D37 and AM-P3-N1.
**Answer (developer):**

### DEC-428 · OPEN · 2026-11-09 · Sinheung cross-check, the Frame and Step 5 piece (P3)
**The question, in plain words:** Re-file the method gap as methodology?
**The facts:** The question is entry AM-P3-Q11 in section 5 of the Frame and Step 5 piece (P3) (`Amendment_Rederivation_P3_Station_Lineage_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. The question. Should the Frame's modifier-set gap be re-filed as a methodology item, "inheritance without personhood" (plant and papers cross, people do not), rather than as a Sinheung finding? And should the modifier set get a term for it? Asked by B and C; A adopted it in Round 3. Disposition: found by two.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** - Re-file it as a methodology question for whoever next edits 01 §1.1. - Add no new modifier (NO FORCED FIT). - Record it as a standing note under the type, because the rule makes it the ordinary condition (C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** AM-P3-F6 and AM-P3-D7.
**Answer (developer):**

### DEC-429 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phases 5 and 7 piece (P7)
**The question, in plain words:** Is the neutral transshipment arrangement in force during the Second Interwar, from when, and by the pass's "now" of the ~2780s?
**The facts:** The question is entry AM-P7-Q1 in section 5 of the Phases 5 and 7 piece (P7) (`Amendment_Rederivation_P7_Raw_Materials_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: confirmed by all three (A, B, C). K drafted the question and made it conditional on the hub file being silent; the file says outright that the era is open ("This file assumes nothing ...
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** In force within the default Second Interwar frame by the ~2780s, with the start date left open (A, B, C) and post-war survival left open (C). The developer should also say whether it begins before or after the cluster's legal merger (Phase 5 L92), because that decides whether it bears on the forcing function in AM-P7-F7 (C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** . AM-P7-F2, AM-P7-F3, AM-P7-F4, AM-P7-F5, AM-P7-F6, AM-P7-F7, AM-P7-F11, AM-P7-F12, AM-P7-F13, AM-P7-F14, and every docket row marked PROVISIONAL.
**Answer (developer):** Answered 2026-11-09 (DR-125): in force by the 2780s within the default Second Interwar frame; its start date and its survival after the war are left open (A). The developer did not say whether it begins before or after the legal merger of the cluster; that part stays open.

### DEC-430 · ANSWERED 2026-11-09 (DR-125) · 2026-11-09 · Sinheung cross-check, the Phases 5 and 7 piece (P7)
**The question, in plain words:** Does the cluster's share land directly at Nella Fjord, or at another beneficiary's harbor and then by road?
**The facts:** The question is entry AM-P7-Q2 in section 5 of the Phases 5 and 7 piece (P7) (`Amendment_Rederivation_P7_Raw_Materials_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: found by two (A, B); confirmed by C, whose Round 3 withdrawal keeps the direct landing as the recommended reading.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Directly at Nella Fjord, in its one window and through its queue. It is the cluster's only listed sea access (Ports.md L560) and its one defensible cut (Phase 5 L62), and the cluster is a beneficiary in its own right (Ports.md L130; hub file L60) (A, B, C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** . AM-P7-F7; the "meets first" entry in AM-P7-F4; AM-P7-N1, AM-P7-N6, AM-P7-N4; AM-P7-D5, AM-P7-D10, AM-P7-D11.
**Answer (developer):** Answered 2026-11-09 (DR-125): directly at the fjord, in its one window and through its queue; conditional until the arrangement's form is ruled (A).

### DEC-431 · OPEN · 2026-11-09 · Sinheung cross-check, the Phases 5 and 7 piece (P7)
**The question, in plain words:** What does this city draw through the channel (H66)?
**The facts:** The question is entry AM-P7-Q3 in section 5 of the Phases 5 and 7 piece (P7) (`Amendment_Rederivation_P7_Raw_Materials_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: confirmed by all three.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Keep the national manifest unruled (H66; hub file L51-52), and carry the real-world list in AM-P7-F3 as research (seed), not as canon (A, B). When H66 is ruled, the developer may consider that list alongside the file's own candidates (C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** . Whether the L110 wording names categories or stays generic (A) (AM-P7-D20); the strength of AM-P7-F3 and AM-P7-N2.
**Answer (developer):**

### DEC-432 · OPEN · 2026-11-09 · Sinheung cross-check, the Phases 5 and 7 piece (P7)
**The question, in plain words:** Does anything leave Tepenia through the hubs in exchange, does any of it come from this city, and how is the inflow paid for?
**The facts:** The question is entry AM-P7-Q4 in section 5 of the Phases 5 and 7 piece (P7) (`Amendment_Rederivation_P7_Raw_Materials_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: confirmed by all three.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Leave it open nationally ("What flows each way" is an open question in the hub file, L129); the city pass writes the hub channel as inbound only (A, B, C). Record payment as open: the arrangement's form (L127), the flows (L129) and the currency's backing (Phase 7 L159-166) are unsettled (A). Do not route this city's domestic exports abroad to fill the slot (C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** . AM-P7-F8; AM-P7-D21.
**Answer (developer):**

### DEC-433 · OPEN · 2026-11-09 · Sinheung cross-check, the Phases 5 and 7 piece (P7)
**The question, in plain words:** Do foreign vessels or crews enter Nella Fjord, or does cargo change hulls at the hub?
**The facts:** The question is entry AM-P7-Q5 in section 5 of the Phases 5 and 7 piece (P7) (`Amendment_Rederivation_P7_Raw_Materials_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: found by one (B); confirmed by C.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Leave it open. The arrival table gains no people row, and nothing is invented (B). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** . AM-P7-F4, AM-P7-N9, AM-P7-N7.
**Answer (developer):**

### DEC-434 · OPEN · 2026-11-09 · Sinheung cross-check, the Phases 5 and 7 piece (P7)
**The question, in plain words:** National: how does the no-bilateral condition sit beside DR-19's record of the same mainland power's central role in founding other cities, and beside a gateway structure that names it a partner?
**The facts:** The question is entry AM-P7-Q6 in section 5 of the Phases 5 and 7 piece (P7) (`Amendment_Rederivation_P7_Raw_Materials_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: conflict sent to the developer. A offers a substantive working answer; B and C flag the question without one.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Decide it nationally. This piece decides nothing on it and writes nothing for this city from it. A's working answer is offered for the developer's decision only: treat the no-bilateral condition as a state-level relationship, later than founding, which would also help date AM-P7-Q1. (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** . The start date in AM-P7-Q1; the scope of AM-P7-K11; AM-P7-N12.
**Answer (developer):** Developer, 2026-11-09: "we'll likely need to look at this in detail". Left open for a detailed discussion; Sinheung writes nothing from it meanwhile.

### DEC-435 · OPEN · 2026-11-09 · Sinheung cross-check, the Phases 5 and 7 piece (P7)
**The question, in plain words:** Does the "(principal)" mark at Ports.md L130 limit this cluster's share, given the ruling's "equally"?
**The facts:** The question is entry AM-P7-Q7 in section 5 of the Phases 5 and 7 piece (P7) (`Amendment_Rederivation_P7_Raw_Materials_2026-11-09.md`); its reasoning, the sources and the readers' split are in that piece's findings and merge record. Disposition: found by two (A, C); confirmed by B.
**Options:** A) the recommended answer below · B) a different answer, in your words.
**Recommendation:** Follow the ruling's own words ("could all equally benefit", hub file L15; "all four benefit equally, per the ruling", L54). Read "principal" as recording where the question was raised (L59), not as a ranking of landings (A, B, C). (PROVISIONAL: the piece proceeds on this until you answer).
**What is waiting on it / what was done provisionally:** . Nothing in this piece, since no quantity is stated (DRQ-09); the direct-landing reading in AM-P7-F2 leans on it (C). Low priority. See AM-P7-N11.
**Answer (developer):**

## Open since 2026-11-10 (Shirayuki cross-check; every answer below is PROVISIONAL until you give yours)

### DEC-440 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (sheets)
**The question, in plain words:** Shirayuki has no Pre-Trip sheet and no datasheets, and the tools that build them refuse it because its pass is finished. Should the tools be extended to build them for Shirayuki, or should finished cities keep hand-built reading lists?
**The facts:** `Tools/build_pretrip.py --list` lists Shirayuki under "Not built by this generator: its ULM pass is complete (Tri-Cities)"; `Tools/build_datasheets.py Shirayuki` stops with `KeyError: 'Shirayuki'` (both run 2026-11-10 05:05; neither tool edited, `--force` not used). The to-do to create them stands (`Dev-Road-Map/Weekly_To-Do_-_Current.md` L73, L80). This cross-check built every reading list by hand (`City_Development_Passes/Mirny_Subnet/Shirayuki/Amendment_Log_2026-11-10.md`, L-05).
**Options:** A) extend the two tools to build sheets for a finished city, as reference inputs only (the pass stays unedited) · B) keep hand-built lists for finished-city reviews and build sheets only for new runs · C) build Shirayuki's sheets by hand once.
**Recommendation:** A, in a maintenance session (tool edits run at any hour, `DR-117` item 4): the sheets would give later reviews a checked list instead of a hand-built one.
**What is waiting on it / what was done provisionally:** nothing is blocked; this cross-check ran on hand-built lists (PROVISIONAL, DEC-440).
**Answer (developer):** "Extend the tools (entry's recommendation)": the two builders are extended to make reference sheets for a finished city (the pass stays unedited), in a maintenance session.

### DEC-441 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (two queue questions)
**The question, in plain words:** Two questions Shirayuki's pass left open look answered by later rulings. Are they closed? (1) Which population band the city is written at, when its first census is above one million and its second below. (2) Whether the industry model's difficulty figure should account for most of the city standing on ice, when the site itself is rock.
**The facts:** (1) Queue entry `DRQ-10` (`Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md` L551) is still marked open; `DR-4` (2026-09-13) makes the first census govern the band, with the larger-city analysis deferred until all 38 cities finish all three methods, and `DR-105`'s noted row records Shirayuki (1,112,600) as Band 5. (2) Queue entry `DRQ-13` (L656) is still marked open; `DR-105` item 4 rules "Shirayuki is rock-founded (the site sets the difficulty coefficient)". Detail: `Shirayuki/Amendment_Notes_2026-11-10_Cross_Check.md` `SRY-016`.
**Options:** A) both closed by those rulings; mark the queue entries answered · B) the band closed, the difficulty question left open · C) both left open.
**Recommendation:** A: the rulings answer the exact questions the entries ask, and the cross-check re-derives the affected findings on that reading.
**What is waiting on it / what was done provisionally:** the cross-check items `SRY-C02` and `SRY-C06` are tested on reading A (PROVISIONAL, DEC-441). The queue file is not edited.
**Answer (developer):** "Both closed (Recommended)": the band question is closed by DR-4 (Shirayuki is Band 5 on Census I) and the difficulty question by DR-105 item 4 (the rock site sets the coefficient); the queue entries DRQ-10 and DRQ-13 are marked answered.

### DEC-442 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (what the robot origin rows mean)
**The question, in plain words:** The pass held "do robots have a national origin?" as an open question; your ruling says they do (learned by immersion after coming online), and your note of 2026-11-09 says an origin row covers robots too, "just at whatever percent makes sense for them". So: for a robot who came online in the later era, what does her origin row record; should the robot columns keep copying the human shares; and are the rows a weighting or a headcount for robots?
**The facts:** `DEVELOPER_RULINGS_LOG.md` `DR-11` (L450, L457–L459) and `DR-12` (L472–L474); the startup file Section 4 item 3. Shirayuki's spec gives every row the same share of robots as of humans. Full options: `Shirayuki/Amendment_Rederivation_P02A_Composition_2026-11-10.md` section 6, points .154, .155, .156 (with .157 and .159, which ask whether robots arrived with the founders or kept arriving after the signing).
**Options:** see the piece. **Recommendation:** (1) a later-era robot's row records the origin stock of the community she came online in, standing as ancestry, as for a human of the same era; (2) keep the copied shares for now (no finding rests on a robot row differing from a human row), then make one rule for every city once the arrival questions are answered; (3) the rows are a weighting for derivation and a headcount in-world.
**What is waiting on it / what was done provisionally:** the re-derivation of the pass's robot-origin reasoning (PROVISIONAL, DEC-442).
**Answer (developer):** "Ancestry; copied shares stand (Recommended)": a later-era robot's row records the origin stock of the community she came online in, as ancestry; the copied shares stand for now, with one rule for every city later; rows are weighting for derivation and a headcount in-world.

### DEC-443 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (which lines are "a city's own lines")
**The question, in plain words:** Your ruling of 2026-11-08 says a single city's run takes a relation only from its own lines. Which lines count as Shirayuki's own: only its own files and its own entries in shared files; also lines about things it shares and is named in (its port, airport, road, the cluster), excluding any clause that rests only on another city's lines; or every line that names it?
**The facts:** `DR-122` item 5 (`DEVELOPER_RULINGS_LOG.md` L1868) is one sentence and defines no term. The three readings, and which of the pass's ties and port facts each would keep, are tabled at `Shirayuki/Amendment_Rederivation_P05_Relations_2026-11-10.md` section 6, point .124. A related question on lines that follow another city's line: `Amendment_Rederivation_P00_Band_2026-11-10.md` point .96.
**Options:** A) own files and own entries only · B) A plus shared facilities and clauses whose subject is Shirayuki, excluding clauses grounded only in another city's lines · C) any line naming Shirayuki.
**Recommendation:** B. It is the only reading that keeps the port's summer window and berthing order, which the port file offers to any city of the cluster, while keeping out ties whose only ground is another city's census tier.
**What is waiting on it / what was done provisionally:** the re-derived relation layer of Phase 5 and the Phase 7 addendum (PROVISIONAL, DEC-443). The question is general, so the answer would bind every city's run.
**Answer (developer):** "Own files + shared things it's in (Recommended)": for every city: a city's own lines are its own files and entries, plus lines about shared things it is named in (its port, airport, road, cluster), excluding any clause grounded only in another city's lines.

### DEC-444 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (the harbor and the merger)
**The question, in plain words:** Shirayuki's pass says, as canon, that the merger of the three Larsemann Hills cities was driven by the city that could not reach the harbor. The port file itself calls that mechanism "a PROPOSAL" and says a culture pass on the cluster should decide whether to adopt it. Is it adopted? And may Shirayuki's own single-city pass adopt it for the cluster?
**The facts:** `Locations/Infrastructure/Ports.md` L688–L690 (the scope block); L629–L630 (your remark of 2026-09-05 calling the port "a pretty strong supporting in-world factor"); L639 (canon gives the merger's cause as "none given."). Pass: `04_Phase_05_Relation_and_Geometry.md` L222. Full options: `Amendment_Rederivation_P05_Relations_2026-11-10.md` points .125 and .126.
**Options:** adopted by your remark · adopted by the file-wide canon label · not adopted until a cluster pass or a ruling adopts it · you rule now · rejected.
**Recommendation:** not adopted until a cluster pass or a ruling adopts it (you can rule at any time); meanwhile Shirayuki's pass cites it as a proposal, and a single city's pass does not adopt it for the cluster.
**What is waiting on it / what was done provisionally:** the re-derived Phase 5 sections 6 and 6a (PROVISIONAL, DEC-444).
**Answer (developer):** "Not yet; cite as a proposal (Recommended)": the harbor-merger mechanism is not adopted until a cluster pass or a ruling adopts it; Shirayuki's pass cites it as a proposal.

### DEC-445 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (the oasis rock: what "stated as arithmetic" means)
**The question, in plain words:** You ruled that the Larsemann Hills' ~40 km² of rock is "divided by Census I share, stated as arithmetic". Does that only say how the figure is presented, or that the rock really is held in those shares? And does the open question "who divided the rock, or did nobody?" now split in two: who divided it among the three cities, and who holds the rock inside Shirayuki?
**The facts:** `DR-105` item 4 (`DEVELOPER_RULINGS_LOG.md` L1711–L1712). Queue entry `DRQ-11` (`Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md` L579–L612) is still marked open. The pass's provisional answer is "nobody" (`00_Frame.md` L235). Full options: `Amendment_Rederivation_PS2_Ground_2026-11-10.md` point .117; the item reader's question at `.xc_20261110_item_SRY-C07.md` (its point SRY-C07-23).
**Options:** leave the entry as it is · treat it as closed · narrow it to who decided · narrow it and split it into the three-city division and the holding inside Shirayuki.
**Recommendation:** narrow and split it. The ruling speaks of the three cities; the extent file's canon support ("hierarchy without anyone designing one") speaks of the inside of one city, so the two layers can take different answers without contradiction. "Stated as arithmetic" is read, provisionally, as presentation only.
**What is waiting on it / what was done provisionally:** the rock passages of the re-derived Frame, Spine, Phase 7 and readiness check (PROVISIONAL, DEC-445).
**Answer (developer):** "Narrow and split it (Recommended)": "stated as arithmetic" is presentation only; the open question splits into who divided the rock among the three cities and who holds the rock inside Shirayuki; the pass's provisional "nobody" stays for the inside.

### DEC-446 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (the difficulty model and the ice)
**The question, in plain words:** You ruled that Shirayuki's site (rock) sets its difficulty coefficient. But about 88 to 92% of the city stands on ice that has to be kept usable. Should that ice work count somewhere in the industry model? Four linked points: does an on-ice share belong in the model at all; does the site also set the food term; should the robot upkeep term carry the site's coefficient; and what does the coefficient 1.25 actually price for a rock-founded site?
**The facts:** `DR-105` item 4 (`DEVELOPER_RULINGS_LOG.md` L1712); `Division_of_Industry/16_Per_City_Three_Tier_Run.md` L1758 ("D=1.25, GROWER — Larsemann Hills, rock-founded, food term 100%"). The ice accumulation and flow at the site are unmeasured (`04_Phase_04_Ordinary_Life.md` L63–L65). Full options: `Amendment_Rederivation_PS2_Ground_2026-11-10.md` points .113, .115, .121, .123.
**Options:** see the piece.
**Recommendation:** measure the ice work first, then decide (if a term is added, add it as a separate footprint term and leave the coefficient site-set, run as a Division of Industry sweep, never inside a city pass); confirm in one line that the site label also sets the food term; refer the robot term's coefficient to Division of Industry as a model question; look up what 1.25 prices before the final wording of Phase 4 L47.
**What is waiting on it / what was done provisionally:** the re-derived free-tier and ground wording (PROVISIONAL, DEC-446). Overlaps `DEC-441` (whether the old queue entry on this is closed).
**Answer (developer):** "Measure the ice first (Recommended)": the site's ice is researched first; any ice term is added later as a separate footprint term in a Division of Industry sweep, never inside a city pass; the site label also sets the food term; the robot term's coefficient goes to Division of Industry; what 1.25 prices is looked up before Phase 4's final wording.

### DEC-447 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (tiers set after a random draw)
**The question, in plain words:** In the 2026-11-02 population rework, one origin's share was multiplied by a random factor (0.55 to 0.65) and the tiers were then relabeled. Your ruling says the tiers are "the information". Does a tier boundary that came out of a random draw carry that standing? And what value divides Significant from Notable?
**The facts:** `DR-12` (`DEVELOPER_RULINGS_LOG.md` L472–L475); spec `Specs/Mirny subnet/Shirayuki.md` L54. In Shirayuki the drawn row (the Sinian Federation, 4.49%) sits just below the Significant tier. Full options: `Amendment_Rederivation_P02A_Composition_2026-11-10.md` point .150.
**Options:** the tiers stand as relabeled · a tier reached through a random draw is provisional · re-run the draw across its range and accept a tier only if it is stable.
**Recommendation:** the tiers stand as relabeled; otherwise every tier near a boundary becomes uncertain and tiers stop being the information. Please also state the dividing value.
**What is waiting on it / what was done provisionally:** the re-derived tier-shape and refused-party passages (PROVISIONAL, DEC-447). The question is general.
**Answer (developer):** "Tiers stand as relabeled (Recommended)": for every city: tiers reached after the random draw stand as relabeled; the dividing rule stays the composition file's own (no row at 4.5% or more is Notable).

### DEC-448 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (later arrivals and the station's records)
**The question, in plain words:** Your note of 2026-11-09 says humans could keep arriving after the treaty was signed, and that a station's records can draw people. Did anyone who arrived after the signing settle in Shirayuki in its founding years? And did the station's records draw anyone here?
**The facts:** the startup file Section 4 items 2 and 4; `DR-25` and `DR-26` (`DEVELOPER_RULINGS_LOG.md` L634–L663). No admitted line about Shirayuki records either. Full options: `Amendment_Rederivation_P02B_Arrival_2026-11-10.md` points .100 and .103.
**Options:** see the piece.
**Recommendation:** none is sited here, and both slots stay open ("none is sited here", never "none is possible here"); the pass's founding-era headline is restated so it holds whatever is chosen later; if a draw from the records is ever sited, it runs through what the records hold, never through who wrote them.
**What is waiting on it / what was done provisionally:** the re-derived arrival-mode passages (PROVISIONAL, DEC-448).
**Answer (developer):** "None sited; both open (Recommended)": neither later arrivals nor a draw by the station's records is sited at Shirayuki; both slots stay open ("none is sited here"); the founding-era headline is restated to hold whatever is chosen later.

### DEC-449 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (Band 5: the second census, the guard, the slack)
**The question, in plain words:** Shirayuki is now Band 5 on its first census (your ruling that the first census governs). Three follow-ons: may the second census (691,371) still be used to describe the later era; does the pass's caution against writing "people here do X" stay, over the whole frame and without the old "two hundred thousand" count; and how is the gap between the two censuses (421,229 people the city was built for and did not hold later) stated?
**The facts:** `DR-4` (`DEVELOPER_RULINGS_LOG.md` L211–L251, "Everything is assumed with Census I"; the larger-city analysis deferred and "suspended, not canceled"); census L505, L653. Full options: `Amendment_Rederivation_P00_Band_2026-11-10.md` points .90, .93, .94 (and .89, which is `DEC-441`'s band half).
**Options:** see the piece.
**Recommendation:** the second census is stated as canon in the later-era description only, never as the base of a derived figure; the caution stays over the whole frame with no head-count; the gap is stated as figures only, with a limit saying where it sits on the ground waits for the deferred analysis.
**What is waiting on it / what was done provisionally:** the re-derived Frame band passages (PROVISIONAL, DEC-449).
**Answer (developer):** "Accept the three readings (Recommended)": Census II is canon in the later-era description only, never the base of a derived figure; the caution against "people here do X" stays over the whole frame with no headcount; the gap is stated as figures only.

### DEC-450 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (the language rule in Shirayuki's finished pass)
**The question, in plain words:** Shirayuki's pass derived its everyday language from Japan being its largest origin group. Under your language rule, Hawaiian (later Tepenian) is dominant everywhere, and Japanese is Shirayuki's supporting language (the only group within 12 points of the largest). The piece re-derives the language section on that basis. Do you accept these readings: this amendment is how the rule enters Shirayuki's finished pass; the national language is written "Hawaiian (later Tepenian)" until you date the change; the Japanese supporting tier holds in both Acts (as ancestry in the later one); Shirayuki's robots speak the dominant language and, as residents, can be assumed to follow Japanese; the city's "keptness" register is held in the dominant language, with no word named; and who builds Shirayuki's robots stays an open slot?
**The facts:** `DR-100` (`DEVELOPER_RULINGS_LOG.md` L1664–L1671); your note of 2026-11-09 on the language's origin (startup file Section 4 item 1); `DR-85` (L1527); `DR-105` item 4 and `DR-104` item 3 (Shirayuki follows the plan in which "the language rule enters through the note"); `Robot_Physiology_and_Cultural_Practices.md` L426. Full options: `Amendment_Rederivation_P08_Language_2026-11-10.md` section 6, points .101 to .108 (and .102: the rule goes into the note now and into a culture file only after you accept it).
**Recommendation:** accept each reading as listed.
**What is waiting on it / what was done provisionally:** the re-derived Phase 8 section F and Phase 9's language row (PROVISIONAL, DEC-450).
**Answer (developer):** "Accept each reading (Recommended)": the amendment is how the rule enters the finished pass; "Hawaiian (later Tepenian)" until the change is dated; the Japanese supporting tier holds in both Acts (as ancestry in Act 2); robots speak the dominant language and can be assumed to follow Japanese; the "keptness" register lives in the dominant language with no word named; who builds the robots stays open.

### DEC-451 · ANSWERED 2026-11-10 (DR-131) · 2026-11-10 · Shirayuki cross-check (the smaller choices, taken on their recommended answers)
**The question, in plain words:** The seven amendment pieces put 88 questions in their sections 6. The ones that bear beyond a sentence are `DEC-441` to `DEC-450`. The rest are wording and placement choices inside one piece (for example how a restated sentence reads, where a pointer goes, whether a figure is shown). Each was written on its recommended answer, marked PROVISIONAL. Do you accept them as a batch, or want to go through any?
**The facts:** sections 6 of the seven pieces in `City_Development_Passes/Mirny_Subnet/Shirayuki/`: `Amendment_Rederivation_P00_Band_2026-11-10.md` (.89 to .96; 8 questions), `…_P02A_Composition_…` (.150 to .164; 15), `…_P02B_Arrival_…` (.100 to .115; 16), `…_PS2_Ground_…` (.113 to .123; 11), `…_P05_Relations_…` (.124 to .136; 13), `…_P06_Death_…` (.109 to .119; 11; none touches the deferred mortuary question itself), `…_P08_Language_…` (.101 to .114; 14).
**Options:** A) accept the remaining choices as a batch · B) go through them piece by piece · C) accept some pieces, review others.
**Recommendation:** A, after `DEC-441` to `DEC-450` are answered (some smaller choices follow from them).
**What is waiting on it / what was done provisionally:** every piece's section 6 (PROVISIONAL, DEC-451).
**Answer (developer):** "Accept as a batch (Recommended)": the 88 smaller choices in the seven pieces' sections 6 are accepted; pointer lines into the pass files follow, for approval with a second reader.

## Open since 2026-11-10 (Zhongshan cross-check; every answer below is PROVISIONAL until you give yours)

*From the cross-check of Zhongshan's Opus pass, 2026-11-10. Files: `Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md` (the
note), `Amendment_Log_2026-11-10.md` (the log), the five pieces `Amendment_Rederivation_<piece>_2026-11-10.md` and the summary
`REVIEW_SUMMARY_2026-11-10_Zhongshan_Cross_Check.md`, all in `Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/`. Each
recommendation is the assistant's, PROVISIONAL; nothing is applied to a pass file.*

### DEC-460 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** The two sheet builders cannot make Zhongshan's sheets. The Pre-Trip builder has no Zhongshan entry,
and the reading-list builder finds no reading-list block in Zhongshan's Pre-Trip. Should they be extended to Zhongshan, or should
finished-city reviews keep building their reading lists by hand?
**The facts:** log Z-06 (the tools' own outputs), Z-11 (the reading-list tool carries uncommitted edits dated 2026-11-09, not made by
this run). Every list in this review was built by hand and checked against its brief (Z-10, Z-13, Z-17).
**Options:** A) hand-built lists for finished-city reviews · B) extend the builders to Zhongshan (a change to the tools, made only at
your word).
**Recommendation (PROVISIONAL):** A for this review; B before Zhongshan's own pass is ever run again.
**What is waiting on it:** nothing in this review.
**Answer (developer):** "Hand lists now, extend later (Recommended)": finished-city reviews keep hand-built lists; the builders are extended to Zhongshan before its own pass is run again.

### DEC-461 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** The pass says nobody came to Zhongshan from outside after 2564, so every origin culture there is "a
closed system". The Treaty now lets humans move to Tepenia at any time after the signing (they can never go back), and it sends to
Tepenia every robot who comes into being in Upper Earth territory later. Did people keep arriving in Zhongshan, how many, and when?
**The facts:** Treaty Article II.2.5 (added 2026-11-09), II.2.1, IV.2.3 (note ZSO-021); your general canon of 2026-11-09 (startup
file Section 4). The first check found this conclusion FLIPS (note section J). `Amendment_Rederivation_P02_Arrival_2026-11-10.md`
keeps "the door only opened one way" (no one who came could go back) and drops "no new arrivals" and "a closed system"; its
Questions 74 to 78 and 82 set out the parts: the human stream (a trickle, a steady flow or waves), robots who came online in Upper
Earth later, visitors who never elected, goods and recordings under the Treaty's trade clause, and the census's statement that the
national total was conserved.
**Options:** A) leave the size of any later stream open, as the piece's wording does · B) give it a size now (a trickle; a steady
flow; waves at named periods) · C) rule that in practice almost nobody came to Zhongshan, keeping the pass's reading with a new ground.
**Recommendation (PROVISIONAL):** A. Canon gives permission and no figure; the census cannot show arrivals, so any size would be
invented. Decide B or C when the population history is designed.
**What is waiting on it:** the proposed wording in the P02 piece, and the clauses in the composition and language pieces that rest on
it (a source "permanently unavailable", a "closed border").
**Answer (developer):** "Leave the size open (Recommended)": keep "the door only opened one way" (no one could go back); drop "no new arrivals" and "a closed system"; no size is stated for the later inflow until the population history is designed.

### DEC-462 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** Zhongshan went from more robots than humans (Census I) to more humans than robots (Census II). The
pass reads this as robots leaving through the orbital exit at a higher rate than humans. You ruled that Zhongshan's retention rates are
arithmetic of the census. May the pass keep that reading, labeled as a reading of the arithmetic, or must it say only that the robot
count fell further than the human count?
**The facts:** note ZSO-011 and D-6; `census` L502 and L643 (two later additions marked "Arithmetic, NOT a migration"); the P02 piece,
item C6 (NARROWS) and its Questions 78 to 80 (whether the 22.49% not in Census II all went to orbit, or partly moved on the surface).
**Options:** A) keep the reading, labeled as a reading of the census arithmetic · B) state only the two counts.
**Recommendation (PROVISIONAL):** A, as the piece proposes: the crossing stands as a headcount fact, and the rate reading is labeled.
**What is waiting on it:** the P02 piece's restatements of Phase 2, Phase 5 and Phase 9 lines.
**Answer (developer):** "Keep it, labeled (Recommended)": the crossing stands as a headcount fact; the higher robot departure rate is kept, labeled as a reading of the census arithmetic.

### DEC-463 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** Zhongshan's composition table gives robots exactly the human share in every origin row. The pass
therefore treated the robot figures as a method copied across, with no standing of their own. Robots now carry a national origin, and
an origin row covers robots "at whatever percent makes sense for them". Do the copied robot figures stand as Zhongshan's robots' own,
or will they be set separately?
**The facts:** note ZSO-022 (`DR-11`, `DR-12`, general canon of 2026-11-09); the P02 piece, item C9 (NARROWS: the robot columns regain
equal standing; the pass's guard against robot-versus-human findings holds on a new ground) and its Questions 75, 81 and 82.
**Options:** A) the copied figures stand as the robots' own weighting · B) set robot percentages separately (for example, founding
robots who came online in Upper Earth carrying their own figures).
**Recommendation (PROVISIONAL):** A until robot percentages are set for any city; if B is chosen, the guard is run again.
**What is waiting on it:** the P02 piece's restatement of the pass's two robot-figure lines.
**Answer (developer):** "Copied figures stand (Recommended)": the copied shares are Zhongshan's robots' own weighting until robot percentages are set for any city.

### DEC-464 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** You chose "Divide by Census I share, labeled as arithmetic" for the oasis rock: Zhongshan's figures
now carry 14.45 km² of the roughly 40 km². Does that only set the amount on paper, or does it also answer the open question of who, in
the world, divided the rock (or whether anyone did)?
**The facts:** note ZSO-013 and SD-6; the queue's open question at `Developer_Ruling_Queue.md` L579-583 (options A nobody decided, B an
authority, C the same court that placed the cities); `Amendment_Rederivation_P07_Order_2026-11-10.md`, item C8 (NARROWS) and its
Questions 67 to 71. The share has already moved with re-authored census rows alone (36.27% on the pass's figures, 36.14% now), which an
in-world holding could not do.
**Options:** A) arithmetic only; the in-world question stays open · B) it is also the in-world answer, under option A, B or C of the
queue.
**Recommendation (PROVISIONAL):** A, and record the ruling in the queue entry as answering how the rock divides, while who divided it
stays open (the piece's Question 68). Also open, smaller: whether the rock is one core or scattered pieces, and whether the 40 km²
includes the oasis's lakes (Questions 70, 71).
**What is waiting on it:** the P07 piece's restatements of Gate 11, Phase 7 and the Spine lines.
**Answer (developer):** "Paper amount only (Recommended)": the Census I division sets the amount each city's figures carry (14.45 km² for Zhongshan) as authoring arithmetic; who divided the rock in the world, or whether anyone did, stays open (the queue's DRQ-11, second half).

### DEC-465 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** Zhongshan is a partner in a joint agricultural research project. What is its part: where is that
work booked in its workforce, where is it done, and does it need anything only this site has?
**The facts:** `DR-72` L1386-1387, `DR-75` L1421, `DR-105` item 4 (note row U1, corrected in this run: seed breeding and phosphorus and
soil recovery are another location's own roles, not the project's; log Z-14); the P07 piece, item U1 (NARROWS) and its Questions 72
to 76.
**Options:** for booking: A) inside the technical and scientific mandate (137,200) · B) in that sector's free quarter (45,733) · C) a
separate mandated share (above 41,308 workers it would take the free tier below your 38% floor).
**Recommendation (PROVISIONAL):** confirm the part is agricultural research only, and choose A or B; leave where it is done open until
the project is designed.
**What is waiting on it:** the P07 piece's restatements of the Phase 7 lines on what the city supplies.
**Answer (developer):** "Free quarter of tech sector (Recommended)": Zhongshan's part is agricultural research only, booked in the technical and scientific sector's free part (45,733 workers); the 137,200 mandated workers are unchanged.

### DEC-466 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** How does Zhongshan's inbound freight arrive: only through the neutral transshipment route, which
`Ports.md` now names the city's cluster on, also by direct sailing from the two staging ports in its own relationship entry, or along
the subnet's coastal supply line?
**The facts:** `Ports` L130 (ruling of 2026-09-16, after the pass was committed); `City_Relationship_Database.md` L495; the P07 piece,
item U3 (NARROWS) and its Questions 77 and 78 (whether the block of further terminals at `Ports` L224-228 is canon).
**Options:** A) transshipment only · B) transshipment plus direct sailing · C) all three.
**Recommendation (PROVISIONAL):** B, the reading that keeps both live lines true; but it is a design choice.
**What is waiting on it:** the P07 piece's restatements of the Phase 5 and Phase 7 import lines.
**Answer (developer):** "All three routes": freight reaches Zhongshan through the neutral transshipment hubs, by direct sailing from the staging ports, and onward along the subnet's coastal supply line. Differs from the recommendation: the order piece's import wording is revisited.

### DEC-467 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** Two later research rounds on Zhongshan's three inspiration picks exist (2026-10-26), each ending with
open threads. Are they admitted as material for a re-derivation of Zhongshan, and should their open threads be searched?
**The facts:** note row U5; `Amendment_Rederivation_P03_Research_2026-11-10.md` (NARROWS: the picks stand; the pass's "genuinely
covered" no longer describes the record) and its Questions 39 to 47, including whether a real-world pick counts as "another location"
under the own-terms rule (the piece does not name the picks).
**Options:** A) admit them, and record them for a later fusion run · B) admit them and run the fusion question now · C) do not admit
them.
**Recommendation (PROVISIONAL):** A: record them, carry their open threads forward, and leave the fusion run for Zhongshan's next pass.
**What is waiting on it:** the P03 piece's restatement of Step 3.
**Answer (developer):** "Admit, use at next pass (Recommended)": the two research rounds are admitted material; their open threads are carried forward; the fusion step runs at Zhongshan's next full pass.

### DEC-468 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** Zhongshan's composition table now has 35 rows (one Primary, three Significant, 31 Notable) where the
pass read eighteen nations, five Significant and a tight tail of twelve. The pass's reading of the roster (a plurality that cannot
impose, a few named parties that bargain, a diffuse remainder), its closing axis "The commons had no homeland", its QA gate on the
weakest finding, and its list of groups that could pool all narrow. Do you accept the restated readings, which rest on the tiers and
their totals rather than on single rows?
**The facts:** note ZSO-016; `Amendment_Rederivation_P08A_Composition_2026-11-10.md` (items C1 to C4 and U2, all NARROWS) and its
Questions 102 to 112. Among them: what ground the Siberia, Finland, Tuva and Künnarantaiga rows cover for the polar-climate test; whether
"separate origins" also means separate conduct, which decides whether the twelve Russian-named rows can be tested as one group; and
whether the refusal to pool the East Asian rows may still rest on a file about another location.
**Options:** A) accept the tier-based restatements as proposed · B) keep per-row readings where the rows are in different tiers only.
**Recommendation (PROVISIONAL):** A. The axis and the gate hold on the tier totals; only their grounds and counts change.
**What is waiting on it:** the piece's restatements of Phase 8 section 8.1, the closing axis, Gate 4, the Step 6 output, and the
Zhongshan cells of the shared table (write-only).
**Answer (developer):** "Accept as proposed (Recommended)": the composition piece's tier-based restatements are accepted; the closing axis and the weakest-finding gate stand on tier totals.

### DEC-469 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** The pass never named a language: it treated the dominant language as something the Federation
supplies and the city's common speech as built locally, with "no source at all". Under your rule, Hawaiian is dominant and Mandarin is
Zhongshan's only supporting tier, and Hawaiian's own base languages include English, Japanese, Korean and Tagalog, all four among Zhongshan's own language rows
(`Language_Blocs_By_City_2026-11-03.csv` L775-806). Do you accept the restated language section, which names both languages and keeps the speech marker (two
branches of one stock, meeting here) heard at least in the city's Mandarin?
**The facts:** note ZSO-018 (`DR-100`; your general canon of 2026-11-09); `Amendment_Rederivation_P08B_Language_2026-11-10.md` (item C5,
NARROWS) and its Questions 69 to 79: where the marker is heard; when Hawaiian becomes Tepenian and whether Zhongshan's Mandarin feeds
it; how a robot's speech is set after she comes online; which census sets the robot share; and whether the marker is one local speech in
layers or two side by side.
**Options:** A) accept as proposed · B) accept, and also place the marker in local Hawaiian · C) keep the pass's unnamed layers.
**Recommendation (PROVISIONAL):** A; B can follow once Hawaiian's Zhongshan usage is designed.
**What is waiting on it:** the piece's restatements of Phase 8 section 8.8, two Frame lines, a Phase 5 line and the shared-table language
cell; the culture file's language line (`DEC-470`).
**Answer (developer):** "Accept as proposed (Recommended)": Hawaiian dominant and Mandarin the sole supporting tier, both named; the two-branch speech marker is kept in Zhongshan's Mandarin; the pass's "no source at all" common speech is dropped.

### DEC-470 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** Zhongshan's culture file still disagrees with the spec and the language rule in three places: its tier
table (China Primary, five Significant, twelve Notable), its statement that Mandarin is the city's sole public language, and its "founding
wave" tag on Australia. May all three be corrected in a morning window?
**The facts:** note section G, SD-3, SD-4 and SD-5 (new: the tag on Australia at L23 and L38, against the spec's tag on the Sinian
Federation only, `DR-88` and the Founding Register). `DEC-004` (2026-11-03) asks the first two and is still open.
**Recommendation (PROVISIONAL):** yes, answered together with `DEC-004`, after `DEC-468` and `DEC-469`.
**What is waiting on it:** the culture file only.
**Answer (developer):** "Yes, correct all three (Recommended)": the culture file's tier table, its sole-public-language line and the founding-wave tag on Australia are corrected to the spec, the language rule and the Founding Register in a morning window. Also answers DEC-004.

### DEC-471 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · general (raised on Zhongshan)
**The question, in plain words:** You ruled that per-nation shares are weighting and that "no finding may rest on a within-tier
difference". How far does that reach? For example: may a finding count how many rows fall under 2%, name which rows are the smallest,
or compare two Notable rows; or may it speak only of tiers and their totals?
**The facts:** `DR-12` (`rulings log` L463-475); raised independently by the first check (items C1, C2) and by two pieces (composition,
Question 102; language, Question 79). The pieces wrote the stricter, tier-level reading where the readers differed.
**Options:** A) tiers and totals only; no per-row count, rank or comparison inside a tier · B) per-row figures may be stated flatly, but
no characterization may rest on a gap between two rows of one tier.
**Recommendation (PROVISIONAL):** B, which keeps each row's own headcount stated flatly (your words: "Stating a figure as a population
in-fiction is fine") while barring the gap.
**What is waiting on it:** the wording of the composition and language pieces where they chose the stricter form.
**Answer (developer):** "Rows stated flatly, no gaps (Recommended)": for every city: a row's own figure may be stated flatly and counts of rows are allowed, but no characterization may rest on a gap between two rows of one tier.

### DEC-472 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** The pass says the other 31 cities have no geothermal heat. The conclusion about Zhongshan holds (its
heat is delivered over the grid and can be cut), but the count is 32 on today's list and could change again with the open geothermal
flag. Should the pass's figure be noted as 32 now, or restated without counting other cities?
**The facts:** note row U4 (the first check: HOLDS); `Geothermal_Heating.md` L38-39, L203-217 (options A to C, none applied); the item
output `.xc_20261110_item_U4.md`, Questions U4-Q1 to U4-Q3 (including whether the national grid file of 2026-11-02 places a generation
center near Zhongshan).
**Options:** A) note 32 now · B) restate as a relation with no count ("Zhongshan has no heat source of its own; its heat arrives as a
national service, delivered and interruptible").
**Recommendation (PROVISIONAL):** B: it cannot be moved by the flag's outcome.
**What is waiting on it:** a dated note only.
**Answer (developer):** "Restate with no count (Recommended)": the line becomes a relation with no count of other cities: Zhongshan has no heat source of its own; its heat arrives as a national service, delivered and interruptible.

### DEC-473 · ANSWERED 2026-11-10 (DR-130) · 2026-11-10 · Zhongshan
**The question, in plain words:** The five pieces made 109 smaller choices of wording and scope (each piece's section 6: arrival 21,
research 13, order 18, composition 29, language 28), and asked a few smaller questions not raised above (for example, whether "shares
held" in the industry file means the sector shares, order piece Question 66; how the research rounds' dropped threads are carried,
research piece Questions 41 to 46). Accept them as a batch, or walk through them?
**The facts:** the five pieces, sections 6 and 7; each choice names the readers who made it.
**Recommendation (PROVISIONAL):** accept as a batch, except any you mark; then the pointer lines into the pass files are drafted for your
approval with a second reader (`DR-101`, `DR-116` item 2).
**What is waiting on it:** the pointer lines into the pass files.
**Answer (developer):** "Accept as a batch (Recommended)": the 109 smaller choices in the five pieces' sections 6 are accepted; pointer lines into the pass files follow, for approval with a second reader.

### DEC-474 · ANSWERED 2026-11-10 (DR-133) · 2026-11-10 · Zhongshan
**The question, in plain words:** After your answer that Zhongshan's freight comes by all three routes, the imports re-derivation asks
five follow-ups. (1) The Ports file's list of the main partner's receiving harbors does not include Zhongshan's cluster. Should it, now
that freighters sail there directly, or does "receiving node" mean a formal designation the cluster lacks? (2) Does the subnet's coastal
supply line reach Zhongshan by sea (into the same seasonal harbor), by the coastal highway, or both? (3) What decides whether a cargo
comes by direct sailing or through the neutral hubs? (4) Is the block of further terminals in the Ports file canon, and does any of them
send freight here? (5) May the Ports file's Zhongshan row and its relationship entry be extended to name the three routes?
**The facts:** `DR-130` item 6; `Amendment_Rederivation_P07B_Imports_2026-11-10.md` (U3 still NARROWS; its Questions 47 to 51);
`Ports` L129, L130, L202, L224-230; `City_Relationship_Database.md` L493, L495.
**Recommendation (PROVISIONAL):** (5) yes, at your word, as a source edit; (1) leave the list as it is, so "not a designated receiving
node" stands as a table fact; (2) both, sea in season and the highway all year (a design call; it decides whether any freight arrives
outside the harbor's season); (3) and (4) leave open until the subnet's logistics are designed.
**What is waiting on it:** nothing in the piece's proposed wording; only the source extensions in (5).
**Answer (developer):** (1) "Add the cluster", then "Four nodes; supersede 10-03": Australia is a four-node partner with the cluster's Nella Fjord harbor; (2) "Definitely highway, for sure. Whether by sea is also year-round, or seasonal, needs to be researched"; (3) "Leave open for now (Recommended)"; (4) "Leave open (Recommended)"; (5) "Yes, extend both (Recommended)".

*Older, still open, unchanged by this run: `DEC-004` (with `DEC-470`); the question in `DR-1` (L134) whether Zhongshan keeps Metal as
its Element (the Spine clause that ruling named no longer appears in the pass; note H.2).*

---

## Open since 2026-11-11 (Mirny review; every answer below is PROVISIONAL until you give yours)

*Raised by the review of Mirny on 2026-11-11 (`Mirny/Amendment_Notes_2026-11-11_Review.md`; summary `Mirny/REVIEW_SUMMARY_2026-11-11_Mirny_Review.md`). Nothing below is applied; every result that rests on an answer is marked PROVISIONAL in its piece.*

### DEC-480 · OPEN · 2026-11-11 · Mirny review, piece ARR (ARR-QD-1)
**The question, in plain words:** When a human chooses to move to Tepenia after the treaty date, under the treaty's new paragraph that lets any human elect to take up residence in the Federation at any time, is she assigned to a station the way the founders were, or does she choose where in Tepenia to live? This is national canon, raised from one city's review (PROVISIONAL).
**The facts:** The new paragraph, treaty draft (`TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md`) L50, Article II.2.5: "5. Any human person who has not made the election described in paragraph 3 of this Article may, at any time after the effective date of this Treaty, freely elect to take up residence within the Federation of Tepenia, the Federation's existence not being limited to the population described in this Article"; the elector "shall for all purposes of this Treaty be treated as a person who has made the election described in paragraph 3." Ruled canon at `DEVELOPER_RULINGS_LOG.md` L1913 (`DR-127` item 2). **For assignment:** II.3.2 settles "The population departing under Article II.2" at installations, "each population being assigned to a station" (treaty L54), and "for all purposes" (L50) carries the elector into that population on a literal reading. **Against it:** II.3.2 speaks of installations "presently found" and of arrangements concluded "in the years following this Treaty's signing" (L54); assignment's purpose is "the orderly and humane distribution of the exiled population" (L55); II.2.5 says "the Federation's existence not being limited to the population described in this Article" (L50); II.4 lets a settlement progress "by its own governance" "without requiring further leave of the Assembly Powers" (L57). Phase 2 (`04_Phase_02_Composition_and_Arrival.md`) L148–149 gives arrival two levels, "into the Federation (the treaty) and into Mirny (the station assignment)"; for a later elector the second level is not stated to be assignment. The F-1 item check could not read II.3.2; all three readers have it, and it does not settle the question (piece §1, correction (b)). For Mirny the answer decides whether a later human there was sent or came by choice, and so whether Phase 2's "Nobody chose the site; the place does not know what it attracts because it did not attract." (L341, E5) holds past the founding, whether Mirny can draw anyone from Upper Earth at all (ARR-5), and whether a partner who stayed when her robot was compelled to leave could follow to her robot's station (ARR-3).
**Options:** (A) Assigned, on the literal reading of "for all purposes"; E5's "did not attract" then extends to later electors. (B) She chooses; II.3.2 is the founding-era allocation only; Mirny's attractors (the hub, quarry and chamber-supply functions; inherited records under the "records can draw people" ruling; a partner) then matter for her. (C) Assigned during the founding-era arrangements, and placed by the Federation's own law afterward (II.4, treaty L57: settlements progress "by its own governance"); the both-are-true candidate. (D) Leave it open; Mirny's lines carry both branches (ARR-6).
**Recommendation:** (D), PROVISIONAL. The question is national and was raised from one city's review; either answer moves every city's later-arrival reading. If the developer rules, the ruling should be recorded for every city, and (C) is the candidate that keeps both readings true.
**What is waiting on it / what was done provisionally:** Carried as an open slot with both readings written (ARR-6). Resting on it: ARR-6; ARR-3's third order (whether a follower could reach her partner's station); ARR-5's later half (whether anyone chose Mirny); docket rows ARR-DK-1 ("where placement lets them choose"), ARR-DK-2 (Phase 2 L148–149), ARR-DK-8 (Phase 2 L168–169), ARR-DK-11 (Phase 2 L341) and ARR-DK-13 (Phase 2 L494, "how she was placed"). Merges the readers' ARR-Q1, ARR-Q101 and ARR-Q201 and the F-1 item check's IQ-101. Related in the same piece: DEC-481, DEC-482.
**Answer (developer):**

### DEC-481 · OPEN · 2026-11-11 · Mirny review, piece ARR (ARR-QD-2)
**The question, in plain words:** Where may a human make that election to move to Tepenia: anywhere, including on Tepenian soil, or only in Assembly Power territory before she departs? For Mirny it decides whether an Upper Earth visitor held at Mirny through a winter by the ice could choose to stay (PROVISIONAL).
**The facts:** Treaty draft L50 names a time ("at any time after the effective date of this Treaty") and no place. Phase 5 (`04_Phase_05_Relation_and_Geometry.md`) L258's first sentence, "A human from Upper Earth arriving after the treaty date has **no written route to membership**", is superseded by L50 (ARR-DK-17). Phase 5 L282, the ice's hold (M2): "an Upper Earth person — the one the ice does hold — has no legal route to membership (P5-19). **The ice holds mostly those it cannot convert**"; its premise falls with L258, and whether its conclusion flips or survives turns on where an election may be made. Phase 5 L261: "**So a sea visitor's arrival date belongs to the ice and the wind, not to the visitor or the host;**". The new paragraph names no conveyance, where II.2.1 names the Assembly Powers' "schedule" and "means of conveyance" (treaty L46 against L50), so the ice bears on an elector only if she comes by sea (ARR-2). No admitted line shows any Upper Earth person wintering at Mirny or electing there; "**whether crews come ashore is not stated**" (Phase 5 L250, R-64). Under either answer the "Outside legally" cell stays "**empty in the admitted set**" (Phase 5 L238).
**Options:** (A) Anywhere, including inside Tepenia: a visitor at Mirny's edge could elect and stay. (B) Only before departure, in Assembly Power territory. (C) Leave it open, recording that the text names no place, and carry M2 in two branches.
**Recommendation:** (C), PROVISIONAL. (A) is the literal reading, but no admitted line shows any Upper Earth person wintering at Mirny (R-64) or electing there, and choosing either answer would set national canon from one city's review.
**What is waiting on it / what was done provisionally:** ARR-2's third order, carried in two branches: if an election may be made inside Tepenia, the ice may hold those the law now lets convert themselves, at the cost of their legal elsewhere; if only before departure, Phase 5 L282 survives in substance. Docket rows ARR-DK-17 (Phase 5 L258) and ARR-DK-18 (Phase 5 L282; high for the premise, medium for the branch wording); ARR-1's open slot. Merges the readers' ARR-Q2, ARR-Q102 and ARR-Q202 and the F-1 item check's IQ-102. Related in the same piece: DEC-480.
**Answer (developer):**

### DEC-482 · OPEN · 2026-11-11 · Mirny review, piece ARR (ARR-QD-3)
**The question, in plain words:** Did any human who moved to Tepenia after the treaty settle at Mirny and live there into Act 2? The national half of the older question is now answered by the treaty; only Mirny's half remains (PROVISIONAL).
**The facts:** The older question, Phase 9 (`04_Phase_09_Populations.md`) L501 (Q-86), rests on "The treaty text gives humans no admission channel after June 21, 2564 (`FTD` II.2.3)"; that premise is superseded by treaty L50 and `DEVELOPER_RULINGS_LOG.md` L1913, and its Mirny half ("or did later human arrivals reach it?") stays open. The human clock: "By about 2614 the human founders are elderly or dead while the founding robots are still active" (Phase 9 L303); [CALC] 2614 − 2564 = 50 years. Phase 9 L304: "**Act 2:** with the human founders gone, and no human channel after the treaty in the treaty's own text (R-17), **the remembering side is robots**". Phase 9 L508 (PA-59): "No post-treaty human admission from Upper Earth is assumed, and none is denied". The later-airport ruling stays "**DEFERRED ON PURPOSE.**" (`DEVELOPER_RULINGS_LOG.md` L1027). No later elector at Mirny is recorded. The piece splits the memory line into two objects: (a) the founding held first-hand, in Act 2 by the founding robots only, on the human clock; (b) the memory of an elsewhere, in Act 2 certainly by the founding robots and possibly by both bodies (ARR-4).
**Options:** (a) Leave it unread at Mirny: in Act 2 the founding is held first-hand by the founding robots, and an elsewhere certainly by them and possibly by any later arrival of either body; no share, count or date. (b) Yes, some did (no count): the Act 2 memory line runs through both bodies, and the Act 2 halves of Phase 9 L193, L199, L207, L301, L304 and `Amendment_Rederivation_P9_Populations_2026-11-04.md` L109, L165 reverse. (c) None did: the robots-only reading for an elsewhere stands as a Mirny fact on a ruling, which needs its own ground, since the treaty permits arrival.
**Recommendation:** (a), PROVISIONAL. Canon gives a "could", not a recorded arrival; an empty slot is a result: none is sited here, not none possible here.
**What is waiting on it / what was done provisionally:** Written as (a): ARR-4 (the memory line in Act 2, "certain in the robot half, possible in both bodies", with its proposed Act-column wording) and ARR-1's conditional third order. Docket rows written on "unread at Mirny": ARR-DK-20, ARR-DK-23 to ARR-DK-34, ARR-DK-37 and ARR-DK-38. Merges the readers' ARR-Q3, ARR-Q103 and ARR-Q203 and the F-2 item check's IQ-201. Related in the same piece: DEC-480.
**Answer (developer):**

### DEC-483 · OPEN · 2026-11-11 · Mirny review, piece ARR (ARR-QD-4)
**The question, in plain words:** The developer has ruled that "records can draw people" is a general mechanism, and Mirny holds records inherited with its station. Does Mirny use that mechanism as a way later arrivals came to the city (PROVISIONAL)?
**The facts:** `DEVELOPER_RULINGS_LOG.md` L1886 (`DR-124` item 4): "**(4) Records can draw people** (the station-inheritance ruling's row) is a GENERAL mechanism"; the rest of the line names another city as one that "may use" it and records that this "differs from the review's recommendation that it is specific to the location it names"; the words "for every city" are not on the line, so every Mirny change resting on it is held at medium confidence. Only the mechanism carries: a station can hand down its "**records, logs, journals, manifests, maps**" (L645), never "A **tradition**: that passes person to person, and no one carried it across the gap" (L646); none of the generalized row's place, languages, analogy or outcome carries (L648). Mirny holds inherited records: Phase 2 L62 ("Inherited station infrastructure and records"), L72's "the inherited record and no living teacher", L337 ("Records, not people, came with the place."). Phase 2 L72 calls the hub, quarry and chamber-supply functions (G3) "the only admitted attractor for any later arrival"; Phase 2 L61: "**Not adopted as a mode:** no admitted file says anyone arrived for the hub" (the reserve RF-7). No Mirny line gives the records' language or any reader; the real station at the site is a coordinate only (`DR-19`); Mirny's record is read as shared without translation at the founding (`06_Differentiation.md` L71); Phase 2 L498 (R-21): "*Instead:* none named."
**Options:** (A) Admissible and reserved beside RF-7 (arrivals explained by hub work): adopted only when a Mirny line states the language or content of its inherited records and that someone came to read them. (B) Adopt it now as a later-arrival finding. (C) Record it as not used at Mirny.
**Recommendation:** (A), PROVISIONAL. (B) would be a forced fit: no Mirny line gives the records' language or any reader, `DR-19` bars reading the language off the real station, and Mirny's record is read as shared without translation at the founding (`06` L71). (C) would turn "none is sited here" into "none is possible here". If the developer reads `DR-124` item 4 as another city's only, G3's "only" (Phase 2 L72) stands and this question falls away.
**What is waiting on it / what was done provisionally:** ARR-5's records half (G3's "only" falls; three conditional readings of a records draw, each medium, none adopted); docket rows ARR-DK-1 (its records clause, medium) and ARR-DK-39 (the object of its scope note). If the ruling is read as another city's only, ARR-5's records half falls and ARR-DK-1's records clause and ARR-DK-39's scope note lose their object (piece §6). Option (B) of DEC-484 waits on this answer. Merges the readers' ARR-Q4, ARR-Q104 and ARR-Q204 and the F-16 item check's IQ-1601.
**Answer (developer):**

### DEC-484 · OPEN · 2026-11-11 · Mirny review, piece ARR (ARR-QD-5)
**The question, in plain words:** An earlier reconciliation struck a culture-file line that drew people to Mirny by "the old station" and its name. Now that records can draw people, should that strike carry a note saying it struck the station and the name as meaning, not the records as things (PROVISIONAL)?
**The facts:** The strike, `Amendment_Rederivation_S5_Reconciliation_2026-11-04.md` L448 (D-2): "the station-and-name draw (and at `LC:97` the draw by stock ties, R-96)". Its object, S5 L154: "`LC:97` keeps a draw by "the old station, the sloop's name" and by stock ties"; "A kept name is "a naming fact only" (`NNS` L160)". The strike never rested on a closed human channel, so the new human route does not reopen it. The records ruling concerns records as things (`DEVELOPER_RULINGS_LOG.md` L645, L648), and L646 still bars any inherited draw by tradition. Treaty draft L55 corroborates the strike at the founding only: assignment does not require a population to "share the national origin of the Power that formerly maintained it"; it says nothing about later draws. The strike's stock-ties half (R-96) stands. The readers split on whether to ask this at all: two moved to a docket row only, one to a separate question because option (B) would touch the developer's own culture file; it is written as a question, the form that decides least.
**Options:** (A) A scope note: the strike's object is a draw by the station and the name as meaning (history and heritage weight); records as things are a different object and stay admissible (the text of ARR-DK-39). (B) Re-ground the culture file's "the old station" draw (`LC:97`) as a records draw instead of striking it. (C) Keep the label with no scope note.
**Recommendation:** (A), PROVISIONAL. The strike's grounds ("a naming fact only", `NNS` L160 via S5 L154; treaty L55 at the founding) do not reach records as things. (B) would rest a culture line on a mechanism that is empty at Mirny, so at most it waits on ARR-QD-4 (DEC-483). (C) leaves a later reader free to read the records mechanism as struck.
**What is waiting on it / what was done provisionally:** Docket row ARR-DK-39 (S5 L448; its text is option (A)); ARR-5's check of the strike ("Both are true, on two objects"). Option (B) waits on DEC-483. Merges the readers' ARR-Q5, ARR-Q105 and ARR-D232.
**Answer (developer):**

### DEC-485 · OPEN · 2026-11-11 · Mirny review, piece LANG (LANG-QD-1)
**The question, in plain words:** Phase 2 says the place's conditions are "the only layer" every resident meets "without translation", and that at the founding the shared medium was the site, the record and the relay. Canon now gives Mirny a defined civic tongue, shared from the founding on; how should those two lines read beside it (PROVISIONAL)?
**The facts:** Phase 2 (`04_Phase_02_Composition_and_Arrival.md`) L283: "These are **the only layer every resident, in either body and from any stock, meets without translation.**" L284: "shared medium was **site, record and relay, not a culture**; whatever is common must be built on them." The national language, `DEVELOPER_RULINGS_LOG.md` L1895 (`DR-125` item 6): "Hawaiian is a pidgin with a primary base of English and Japanese and a supporting base of Korean, Tagalog, Ilocano and Mexican Spanish; later, influence from a wide variety of languages made Hawaiian become Tepenian (so they are one language over time)." L1669 (`DR-100` item 1): Hawaiian (later Tepenian) "is the dominant language everywhere". `Amendment_Rederivation_P08_Making_2026-11-03.md` L269: "**Hawaiian is the de-facto national language, and at Mirny it is the dominant, civic language for both bodies from the founding on.**" (the human half ruled, P08 L297; the robot half a derivation conditional on AR-40, P08 L301). The pass names a resident who does not yet have the civic tongue, "before she has the dominant language" (`Amendment_Rederivation_P9_Populations_2026-11-04.md` L175, conditional on AR-45), so L283's strict "only" survives; what fails is its silence and, read with L284, its implication that residents share no other medium. L284's "whatever is common must be built on them" holds for what is common and Mirny's own (P08 L307: "What is Mirny's in speech is the conditions vocabulary of its own wind"), by referent, not by word. The relay and the record are met as things while what each carries is in a language (P08 L278, L296, L310; LANG-2). The earlier open decision DEC-228 asks whether to mark the line at all ("Whether to mark the line is still the question.", review note L122); this question asks what a mark would say and does not answer DEC-228.
**Options:** A. Scope it. L283, proposed wording: *the only native layer, and the only layer every resident, in either body and from any stock, meets with no language between her and it*, with one sentence naming the civic tongue beside it as a second common layer, national and not native. L284: the founding medium gains the civic tongue as national speech, and "whatever is common must be built on them" is scoped to what is common and Mirny's own. The relay and the record are named as met as things, their content in a language (LANG-DK-3). B. Strike "only": Mirny has two common layers met without translation (all three readers: this overstates; a resident who arrives without the civic tongue does not meet it without translation, P9 L175). C. Mark only: leave the wording and add a marker beside L283 pointing to `DR-100` and `DR-125` item 6 (leaves L284's founding list silent on the civic tongue).
**Recommendation:** A, PROVISIONAL. It keeps what Phase 2 built from the place (the conditions); it states the second layer that the pass's later layer already names (P08 L304) and keeps it national, not native (P08 L307); it sits inside C.2's own frame ("**C.2 What the place's own conditions make native**", Phase 2 L275); it holds in both Acts; and it survives either reading of "every resident". All three readers recommend A. Two readers proposed a fourth option, leaving the line unmarked (DEC-228 answered no) so that one answer settles both; the merge keeps the two questions separate because that claims less. If the developer prefers to settle both at once, answering DEC-228 by leaving the line unmarked makes this question fall away.
**What is waiting on it / what was done provisionally:** LANG-1 and LANG-2; docket rows LANG-DK-1 (wording PROVISIONAL on this question and on DEC-228), LANG-DK-2 and LANG-DK-3. Merges the readers' LANG-Q1, LANG-Q101 and LANG-Q201; overlaps the F-3 item check's IQ-301 and replaces nothing in it. See also DEC-228 (open before this review).
**Answer (developer):**

### DEC-486 · OPEN · 2026-11-11 · Mirny review, piece LANG (LANG-QD-2)
**The question, in plain words:** A catalog caution says an English authoring label could be mistaken for an in-world English name because English is Mirny's supporting tier; English is now one of two supporting-tier languages and also a named base of the civic tongue. What should the caution give as its reason (PROVISIONAL)?
**The facts:** The caution, `Amendment_Rederivation_P10_Catalog_2026-11-04.md` L394: "With English Mirny's supporting tier, an English authoring label in this catalog could be read as an attested in-world English name." Its rule clause stands: "Every label stays an authoring label for an admitted referent, in English, **never attested speech** (the Phase 8 piece, L316), and never a place name." The tier: the developer, `DEVELOPER_RULINGS_LOG.md` L1768, *"English and Russian, as a special ruling"*; recorded at L1769 (`DR-111`, 2026-11-04, names Mirny). The base: L1894–1895 (`DR-125` item 6), "a primary base of English and Japanese". The rule: `Amendment_Rederivation_P08_Making_2026-11-03.md` L316, "*Every label is an authoring label for an admitted referent, in English, **never attested speech**, and must never become a place name. No word is coined in any language.*"; P10 L393: "the catalog coins no word in any language"; P10 L395 (R-118): "*which language a name is in (the dominant, the supporting tier or another) is part of the developer's naming*". The developer's words say English is a "primary base"; they do not say what a base supplies, and no claim is made that the civic tongue contains English words. The sentence at L1895 labeled "Reviewer's reading, not the developer's words" is not canon and is not used.
**Options:** (a) `DR-111` only: English is one of Mirny's two supporting-tier languages; the civic-tongue route is not named. (b) Both routes, the second worded as a hazard of reading: English is one of Mirny's two supporting-tier languages (`DR-111`), and canon names it a primary base of the civic tongue (`DR-125` item 6), so an English label "could be read" as attested speech in either, with no claim about what a base supplies; the rule (P08 L316) and R-118 (P10 L395) answer both. (c) Drop the ground and keep the rule unconditioned, as P08 L316 states it.
**Recommendation:** (b), PROVISIONAL. It rests on the ruling's words (rulings log L1769) and the developer's words (L1894), not on the reading labeled non-canon at L1895; it names the wider and costlier route that (a) leaves out; (c) would drop the reason a later reader needs for keeping each label's status attached; and the rule's text stays unchanged. All three readers recommend (b), in the hazard-of-reading wording.
**What is waiting on it / what was done provisionally:** LANG-3; docket row LANG-DK-4 (wording PROVISIONAL on this question). Under option C of DEC-487, LANG-DK-4 keeps only its `DR-111` route. Merges the readers' LANG-Q2, LANG-Q102 and LANG-Q202; overlaps the F-5 item check's IQ-501.
**Answer (developer):**

### DEC-487 · OPEN · 2026-11-11 · Mirny review, piece LANG (LANG-QD-3)
**The question, in plain words:** The developer's definition of the national language (a pidgin of named base languages, one language with Tepenian over time) was recorded during another city's walkthrough and does not say "for every city"; is it recorded for every city? Low priority: a confirmation (PROVISIONAL).
**The facts:** The definition, `DEVELOPER_RULINGS_LOG.md` L1895 (`DR-125` item 6), sits inside another city's walkthrough (heading at L1890) and does not say "for every city" in words. Its object is the national language itself, which `DR-100` item 1 (L1669) already makes general ("the dominant language everywhere"); one language cannot be a pidgin of named bases in one city and not in another. The review note classes it for every city (L16, L22) and leaves item 6 out of the other-city list (L71). Two sentences of L1895 are not used: the one on how a robot built in another city gets its language (city-specific) and the one labeled "Reviewer's reading, not the developer's words". Both LANG items (Phase 2's "met without translation" and the catalog caution on English labels) rest on this reading for their halves that come from the definition.
**Options:** A. Yes, national canon for every city, and say so in words in the log (a clause or a cross-reference), so that standing line 25's venue test (only a ruling recorded for every city, or one naming Mirny, moves a Mirny conclusion) reads it the same way next time. B. Yes, with no words added. C. Not yet general; Mirny's lines wait for a general record. (Under C, F-3 and F-5 lose their halves that rest on the definition: LANG-DK-1, LANG-DK-2 and LANG-DK-11 fall, and LANG-DK-4 keeps only its `DR-111` route. LANG-DK-3 and LANG-DK-5 to LANG-DK-10 do not rest on it and stand.)
**Recommendation:** A, PROVISIONAL. Carried as a question by two readers; the third would keep it as a one-line confirmation and drop it if the orchestrator holds the review note's section A classification as settled.
**What is waiting on it / what was done provisionally:** The definition's halves of LANG-1 and LANG-3; docket rows LANG-DK-1, LANG-DK-2 and LANG-DK-11, and LANG-DK-4's civic-tongue route. Merges reader B's LANG-Q103 (A and C had it in Limits in Round 1).
**Answer (developer):**

### DEC-488 · OPEN · 2026-11-11 · Mirny review, piece COMP (COMP-QD-1)
**The question, in plain words:** Mirny's origin table gives every row a robot figure, filled at the human proportions; now that the developer has ruled each body is in a row "at its own percentage", how should Mirny's lines read those robot figures? (PROVISIONAL)
**The facts:** The ruling, `DEVELOPER_RULINGS_LOG.md` L1922 (`DR-128` item 1): "**(1) An origin row applies to both humans and robots, each at its own percentage.**"; "This settles in part the "does a robot made in Tepenia have a national origin" point left open in `DR-127` item (3): robots are in the origin rows. Whether a row's robots carry its origin practices is still the earlier answer (practices are sized on the human count; the total with robots is a conditional upper figure)." The developer's words (L1921): *"just at whatever percent makes sense for them"*. Item (1) carries no "for every city" words of its own (unlike `DR-130` item 7 at L1940), and the developer's words were given on a human exile's origin row; the review note classes it for every city (L25, L71–L72). The spec (`Specs/Mirny subnet/Mirny.md`) L69: "Robot figures apply the same proportions as the human population." Spec L30 heads separate robot columns, and every admitted row carries a robot count (for example spec L32, 97,555). `DR-11` L459: the robot columns "are **not** demoted on a "reserved question" ground. They carry the same standing as the human columns"; `DR-12` L474: admitted-demoted "for humans and robots alike". [CALC] Over the 17 admitted rows a row's robot share and human share at Census I differ by at most 0.0004 points (United Kingdom: 97,555 / 710,578 = 13.7290 % against 95,135 / 692,971 = 13.7286 %). The rulings log records "the robot percentages" as not decided (L1941, a record of an open matter, not a ruling). The F-7 item check (DEC-501) records the chamber question as answered before this review (`Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` L702: "an array of fabrication chambers stands at Mirny, so robots are built here"); this piece lists which communities at Mirny have robots built and immersed as open (COMP-1).
**Options:** (a) Keep the spec's robot figures as the robots' own, labeled. They stand with the human column's standing (`DR-11` L459), equal to the human share by construction. The pass lines that speak of "both bodies" take notes, not rewording (COMP-DK-1 to COMP-DK-9). Practices are sized on the human count. Nothing rests on the bodies' shares being the same or different. Robot percentages set on the robots' own grounds wait for a rule for every city, which is not yet made (review note L73; the rulings log records "the robot percentages" as not decided, L1941). (b) Read every row share as a human share only. The robots' per-row percentage is treated as "not stated at Mirny" until a rule sets it, and the "of each body" and "identical in both bodies" lines are reworded. This is the F-6 item check's recommendation (its IQ-601 (b)). (c) Set Mirny's robot percentages now, on the robots' own grounds: who brought robots at the founding, which communities had robots built and immersed, and any later arrival. No admitted line gives those inputs (R-13 open), it would edit the spec and the census, and it needs a rule for every city that does not yet exist. (d) Read `DR-128` item 1 as another city's answer only. F-6 then holds unchanged. The item's own text carries no "for every city" words; the review note classes it for every city (L25).
**Recommendation:** (a), PROVISIONAL. The spec states robot figures, `DR-11` L459 says the robot columns "are **not** demoted" and carry "the same standing as the human columns", and canon outranks the pass. "Its own percentage" does not say "a different percentage". (b) does exactly that demotion: it reads stated canon figures as unstated. (c) needs inputs no admitted line reads, and a rule not yet made. (d) is possible on the item's wording, but it goes against the note's classification and the log's layout; it is listed so the developer can close it, not recommended. A ruling recorded for another city reached a reading like (a) there; it does not carry, which is why Mirny needs its own answer. (a) and (b) give the same guard (nothing rests on the sameness or on a difference); they differ on one point: under (a) Mirny may state flatly, as a headcount, that a row holds a given number of robots (for example 97,555 in the United Kingdom row at Census I, spec L32); under (b) it may not.
**What is waiting on it / what was done provisionally:** COMP-1 (the robot half of each origin row) and COMP-3; docket rows COMP-DK-1 to COMP-DK-9. Under (d), F-6 holds unchanged and COMP-1 moves no Mirny line (COMP-1's precondition). Merges the readers' COMP-Q1, COMP-Q101 and COMP-Q201 (all three recommend (a)); answers in place of the F-6 item check's IQ-601. See also DEC-501 (the F-7 item check asks how a robot who came online at Mirny is placed in an origin row, on the same ruling).
**Answer (developer):**

### DEC-489 · OPEN · 2026-11-11 · Mirny review, piece COMP (COMP-QD-2)
**The question, in plain words:** Mirny's two largest origin rows, United Kingdom 13.73 % and Korea 13.71 %, are 0.02 points apart inside the Primary tier, and the developer has ruled for every city that no characterization may rest on a gap between two rows of one tier. May any Mirny line (pass, spec candidate or in-world speech) name one of them "the largest"? (PROVISIONAL)
**The facts:** Spec (`Specs/Mirny subnet/Mirny.md`) L20: "| Primary | United Kingdom, Korea, Indonesia, Sinian Federation, Japan, Australia |"; L32: "| Primary | United Kingdom | 13.73% | 97,555 | 95,135 | 72,536 | 71,942 |"; L33: "| Primary | Korea | 13.71% | 97,439 | 95,023 | 72,449 | 71,855 |". [CALC] Printed gap 13.73 − 13.71 = 0.02 points; from the counts at Census I, 192,690 against 192,462 of 1,403,549, which is 13.7288 % against 13.7125 %, a gap of 0.0162 points (228 people). The ruling, `DEVELOPER_RULINGS_LOG.md` L1940 (`DR-130` item 7): "**(7) The tier rule, for every city (`DR-12`'s reach):** a row's own figure may be stated flatly and rows may be counted; no characterization may rest on a gap between two rows of one tier."; the developer's selection (L1939): *"Rows stated flatly, no gaps (Recommended)"*. L472: "those differences were randomized for realism and carry no meaning"; L473: "The census *is* a headcount. Stating a figure as a population in-fiction is fine; **deriving a characterization from a within-tier gap is not**". Spec L28: "random 0.55 to 0.65". Lines that name the largest row: `Amendment_Rederivation_P2c_Composition_2026-11-03.md` L15, "The largest share is 13.73 % (United Kingdom; Korea 13.71 %)."; and the held spec candidate at `Application_Batch_3_CultureFile_and_Spec_2026-11-08.md` L624, "the largest the United Kingdom at 13.73 %" (held, not applied: L622, "**Needs the developer's word first (spec).**"). The census defines Primary in the singular: "**Primary** — Dominant national community; shapes the city's primary linguistic and cultural identity" (`Official_Population_Census.md` L36); P2c L222 recommends reading it as "a tier label: the six largest communities jointly, none shaping the city's linguistic and cultural identity alone", an open question the developer has not answered (P2c L259). [CALC] "The top two" would rest on Korea 13.71 % against Indonesia 12.03 % (spec L33, L34), also a within-tier gap. The readers' swap test (exchange two rows' figures; a sentence that still reads true does not rest on the gap) is a working test, not a ruling.
**Options:** (a) Yes, as an in-world headcount fact (rulings log L473), marked so that nothing rests on it. P2c L15 and the held Batch 3 L624 candidate keep "the largest the United Kingdom". (b) No. State the bound ("no row is above 13.73 %"), the count (six Primary rows; zero of 36 at a majority) and each row's own figure flatly, and read the Primary tier jointly. In-world, a row's count may be quoted, but the order is never used as a characterization. A sentence rests on a within-tier gap if it fails the swap test (COMP-2). (c) Name the two top rows together, each with its figure, and call neither the largest. As framed, this fails the ruling too: setting those two apart from the other four Primaries rests on 13.71 against 12.03 (spec L33, L34), a gap inside the Primary tier.
**Recommendation:** (b), PROVISIONAL. It uses only the two forms the ruling permits, and the swap test makes it checkable line by line. It matches the developer's own selection, *"Rows stated flatly, no gaps (Recommended)"* (L1939). It keeps the census's singular Primary definition ("Dominant national community", census L36) from attaching to one row on 0.0162 points. It agrees with P2c's own recommendation for how Primary is read (P2c L222) and with the F-8 item check's IQ-801. If (b) is chosen, COMP-DK-10 and COMP-DK-12 apply, the latter before the held candidate goes forward under AR-208.
**What is waiting on it / what was done provisionally:** COMP-2 (naming the largest row) and COMP-3; docket rows COMP-DK-10 (P2c L15) and COMP-DK-12 (Batch 3 L624, both clauses, before the held candidate goes to the developer under AR-208). Merges the readers' COMP-Q2, COMP-Q102 and COMP-Q202 (all three recommend (b)). See also DEC-502 (the F-9 item check asks whether the drawn-tiers ruling answers in part the same open question of how "Primary" is read at Mirny).
**Answer (developer):**

### DEC-490 · OPEN · 2026-11-11 · Mirny review, piece OWN (OWN-QD-1)
**The question, in plain words:** The highway file's clause "The Denman Glacier crossing is not built; there is no western link to Mirny." sits in a section about another subnet member's spur road; does it count as one of Mirny's own lines? (PROVISIONAL)
**The facts:** The every-city definition, `DEVELOPER_RULINGS_LOG.md` L1949 (`DR-131` item 3): "**(3) A city's own lines, for every city (`DR-122` item 5):** its own files and entries, plus lines about shared things it is named in (its port, airport, road, cluster), excluding any clause grounded only in another city's lines." The clause (`Infrastructure/Highways.md` L278) names Mirny and is about what reaches Mirny by road, so it meets the inclusion half. The paragraph it sits in opens with "`[CGRM 2026-09-01 · Path 6 · developer ruling]`", but the section's stated source is another city's spec field, "which quotes the ruling" (Highways L281), and the same paragraph restates the admitted route line (L199) in an editor's words, so the tag does not by itself show that every clause under it is the ruling's own. Two tests decide it: the exclusion half of L1949, and the rule that only a ruling recorded for every city, or one naming Mirny, moves a Mirny conclusion (brief §3; standing line 25). No Mirny reader has read the ruling's own record (CGRM 2026-09-01, Path 6). Caution kept by all three readers: read with its subject, the clause says the spur member has no road westward to Mirny; it does not say that Mirny has no road to its west, which Highways L199 and `City_Relationship_Database.md` L340 contradict. Without the clause, the pass's null row at Phase 5 (`04_Phase_05_Relation_and_Geometry.md`) L463 on that member's road access stays open on the Mirny side.
**Options:** A) Admit it. The tag shows a ground beyond the other city's spec, so the clause is not grounded *only* in another city's lines. The null at Phase 5 L463 closes for the Mirny side (no direct road), and the review panel's Neighbor seat gains the line. B) Withhold it. If the ruling of 2026-09-01 was made for the other city, it does not carry, and the clause then rests only on that city's line. The null stays "present in the read set, withheld", now on the ruling's exclusion ground. C) Check first, then A or B. The orchestrator, not a reader, reads the ruling at its own record, and no reader opens the member's spec. If the ruling's own words name Mirny, or carry the clause, A follows, on two grounds: L1949, and a ruling that names Mirny. Otherwise B follows. If the ruling's only record is the spur member's spec field, the developer says whether the orchestrator may read that one field.
**Recommendation:** C, then A or B as the ruling's own text decides, PROVISIONAL. All three readers converged on this in Round 3. The deciding fact is what the ruling itself says, and no Mirny reader has read it.
**What is waiting on it / what was done provisionally:** OWN-1's admitted clause, its first order ("no direct road joins Mirny and the spur member") and the closing of Phase 5 L463's second row; OWN-2's case for the spur member (its count of one member with no direct link); docket rows OWN-DK-1, OWN-DK-11, OWN-DK-13, OWN-DK-14, OWN-DK-15 and OWN-DK-19, each with the Mirny-side clause pending. Merges the F-10 item check's IQ-1001 and the readers' OWN-Q1, OWN-Q101 and OWN-Q201.
**Answer (developer):**

### DEC-491 · OPEN · 2026-11-11 · Mirny review, piece OWN (OWN-QD-2)
**The question, in plain words:** Do the spur road's junction lines in the highway file ("joining Hwy 110 at Casey"; "junction with Hwy 110") count as lines about Mirny's own road? (PROVISIONAL)
**The facts:** `Infrastructure/Highways.md` L274 (the route, "joining Hwy 110 at Casey") and L276 (the endpoints, "junction with Hwy 110") are about the spur, a road Mirny is not named in, and the section's stated source is another city's spec (L281). The ruling puts "named in" on the shared thing (`DEVELOPER_RULINGS_LOG.md` L1949: "lines about shared things it is named in (its port, airport, road, cluster)"), and Hwy 110 names Mirny (Highways L199: "**Route:** Zhongshan → Davis → Mirny → Casey → Concordia"), so the reading choice is real. Delete the names from L274 or L276 and no claim about Mirny survives. The readers split on whether to ask: one resolved it without the developer, and one moved to that view in Round 3; two kept it asked, and it is written as asked because the merge does not settle a reading of the ruling on its own authority.
**Options:** A) No. They are about the spur, a road Mirny is not named in, and their stated source is another city's spec (L281). They stay out, and how overland traffic between the spur member and Mirny runs stays an open slot. B) Yes. Any line about a junction on Hwy 110 is a line about Mirny's road.
**Recommendation:** A, PROVISIONAL. All three readers and the item check agree. Under B, "its road" would take in every junction along Hwy 110, including other places' own access, which is what the exclusion half keeps out. Delete the names from L274 or L276, and no claim about Mirny survives.
**What is waiting on it / what was done provisionally:** OWN-1's second order (which direction, and where the spur member joins, are member-side clauses and are not used) and its open slot (how overland traffic between the spur member and Mirny runs: not on Mirny's lines under the recommended answer). Merges the F-10 item check's IQ-1002 and the readers' OWN-Q105 and OWN-Q202.
**Answer (developer):**

### DEC-492 · OPEN · 2026-11-11 · Mirny review, piece OWN (OWN-QD-3)
**The question, in plain words:** The developer's every-city definition of a city's own lines includes lines about shared things the city is named in, giving the examples "its port, airport, road, cluster"; is an Arcanet subnet one of those shared things? For Mirny it decides whether the subnet's member list, and so the hub's member count, is one of Mirny's own lines (PROVISIONAL).
**The facts:** `DEVELOPER_RULINGS_LOG.md` L1949 (`DR-131` item 3), as quoted in DEC-490; the developer's selection, L1948: *"Own files + shared things it's in (Recommended)"*, with no list attached. The subnet row, `City_Relationship_Database.md` L49: Mirny is in its Subnet and Hub cells and is the first member listed; nine places are listed, [CALC] 9 − 1 = 8 other members. L42: "Six subnets, each named after its hub city. **Official names** are the hub city names — used in Arcanet documentation, government records, and signage." Mirny's own entry: "**Arcanet subnet:** Mirny ("Australian") — **hub city**" (L338). The culture file (`Local_Cultures/Mirny_Subnet/Mirny.md`) sites the subnet's relay hardware at Mirny (L279) and names five members, "the other five Mirny subnet cities" (L235). On 2026-11-08 the count was set aside because its only source was "a line that names other places" (`Application_Batch_3_CultureFile_and_Spec_2026-11-08.md` L620), while Mirny's pass already used the count: Phase 5 L308 "**The eight other members**"; `Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md` L637 "nine members' contact". Decision 4 of the 2026-11-05 piece listed this row among "Lines that name other locations but carry Mirny's own relation" (`Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` L842); that DEC-183 answered decision 4, and what its "Yes (Recommended)" (rulings log L1867) accepted, are inferred, not read.
**Options:** (a) Yes. The subnet row (`City_Relationship_Database.md` L49) is one of Mirny's own lines. The hub's member count can be proposed (F-11 flips), and the pass's existing counts (Phase 5 L308; ST8b L637) stand on an admitted line. The reasons: the developer's selection has no list (L1948); the subnet carries Mirny's name as its *official* name (L42), the strongest sense of "named in"; Mirny is the Hub cell and the first member listed (L49), and Mirny's own entry calls it the "**hub city**" (L338); a subnet is a group of places sharing one piece of infrastructure, the same kind of thing as the listed "cluster"; Mirny's own culture file sites the subnet's physical relay hardware at Mirny (L279); decision 4 had already listed this row among "Lines that name other locations but carry Mirny's own relation" (ST14 L842). (b) No. The parenthesis is a closed list, so L49 stays outside, F-11 holds as Batch 3 L620 wrote it, and the culture file keeps "five". The pass's counts at Phase 5 L308 and ST8b L426 and L637 then need notes. The reasons: the parenthesis does not name a subnet; decision 4 named this row explicitly, and the answer of 2026-11-08 was "Yes (Recommended)" (L1867), so the earlier answer may have covered this exact line. (That DEC-183 is decision 4, and what its "Yes" accepted, are inferred, not read.)
**Recommendation:** (a), PROVISIONAL. All three readers agree. The later ruling is recorded for every city, defines the very term, and cites `DR-122` item 5 by number.
**What is waiting on it / what was done provisionally:** OWN-3 (the hub's member count); the count of eight in OWN-1 and OWN-2; the reserved nickname note OWN-RS-1; docket rows OWN-DK-3, OWN-DK-21, OWN-DK-22, OWN-DK-24, OWN-DK-25, OWN-DK-27 and OWN-DK-28. DEC-493 applies only under (a), and option (d) of DEC-494 needs (a). Merges the F-11 item check's IQ-1101 and the readers' OWN-Q2, OWN-Q102 and OWN-Q203.
**Answer (developer):**

### DEC-493 · OPEN · 2026-11-11 · Mirny review, piece OWN (OWN-QD-4)
**The question, in plain words:** If the subnet counts as one of Mirny's shared things, how should the culture file's member text be corrected, where it names "the other five Mirny subnet cities" but the subnet table lists eight others? (PROVISIONAL)
**The facts:** `Local_Cultures/Mirny_Subnet/Mirny.md` L235: "the other five Mirny subnet cities", with the correction note "Corrected 2026-07-04"; L279, the relay-hardware landmark, carries the same five (pointer D-36); docket D-6 proposed the factual row first. `City_Relationship_Database.md` L49 lists nine places, Mirny first; [CALC] 9 − 1 = 8 others; 8 − 5 = 3 not named in the culture file: the two L49 marks "latter two joined 2026-07-05" and the one marked "added 2026-10-21" (5 + 2 + 1 = 8). These are authoring dates, not in-world dates; no admitted line gives an in-world era in which the subnet had five other members, so "five" is a stale count with no in-world meaning. `Application_Batch_3_CultureFile_and_Spec_2026-11-08.md` L616: "the hub routes eight other members, not five; keep the single point of failure". `DEVELOPER_RULINGS_LOG.md` L1778 (`DR-112` item 1) excepts "the high-confidence factual rows" from the hold, and DEC-021 permits the members row (Batch 3 L620); "the date any correction is applied" is not decided (L1779).
**Options:** (A) Count and names. Name all eight other members as `City_Relationship_Database.md` L49 gives them, without the row's parenthetical reasons, and make "the other five" read "the other eight". This keeps the file's own form: each name is a relation (that member is routed through Mirny), not a measure. (B) Count and a pointer. Write "the other eight cities of the Mirny subnet (`City_Relationship_Database.md` §2)", drop the names from L235, and let L279 point the same way. The five names went stale because the culture file kept its own copy of a list whose home is the database row, and a pointer keeps one copy. (C) Hold it for the post-ULM rewrite with the 39 held corrections (`DR-112` item 1). This contradicts the permission already given for factual rows (DEC-021; rulings log L1778). *Not offered:* the count corrected with the five names kept, which leaves a list that reads as complete and contradicts its own count.
**Recommendation:** (A), PROVISIONAL. Two readers recommend it, and the third withdrew its (B) in Round 3 ("the post-ULM rewrite can change form"). The single-copy argument stands as the reason for option (B). Whichever is chosen, the date of applying it stays the developer's (rulings log L1779).
**What is waiting on it / what was done provisionally:** Docket rows OWN-DK-27 (culture file L235) and OWN-DK-28 (L279), both conditional on DEC-492 and on this question; OWN-3's "Changes". Applies only if DEC-492 is answered (a). Merges the readers' OWN-Q3, OWN-Q103 and OWN-Q204.
**Answer (developer):**

### DEC-494 · OPEN · 2026-11-11 · Mirny review, piece OWN (OWN-QD-5)
**The question, in plain words:** Phase 5 grounded Mirny's tie with its two road neighbors partly on supply, "three receiving points on one coastal supply line", and the "three" now falls because the other two receivers rest only on the neighbors' own entries. What happens to that supply ground of the tie? (PROVISIONAL)
**The facts:** Phase 5 (`04_Phase_05_Relation_and_Geometry.md`) L322, ground (2): "(2) **supply**, three receiving points on one coastal supply line [IND, lookup file];". Phase 5 L321: "all three receive Australian freighter shipments on one coastal supply line", with the two neighbors' receiving clauses taken from their own entries (`City_Relationship_Database.md` L159, L182), which the every-city definition's exclusion half removes ("excluding any clause grounded only in another city's lines", `DEVELOPER_RULINGS_LOG.md` L1949). No line Mirny may use puts either neighbor back as a receiver: `DR-133` item 1 (L1967), a ruling that names Mirny, lists Mirny as one of Australia's receiving nodes and neither road neighbor; that shows no line read places them as receivers, not that they receive nothing. Mirny's own entry calls the line "the Mirny/Mawson subnet coastal supply line" (`City_Relationship_Database.md` L341), and the subnet table lists those two hub names as two separate subnets (L48, L49). The tie's other grounds stand: (1) the route (L340; `Infrastructure/Highways.md` L199) and (3) the relay hardware. The 2026-11-05 piece reports that the shared connections file grounds the two ties "on the Register, on Hwy 110 and on the relay hardware" (`Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` L341), a supporting reason only, since the pass marks that file "**Not an input.**" (Phase 5 L322). Phase 5's tie already holds its "cultural" half without admissible content (R-60).
**Options:** (a) Withdraw (2) from the tie's grounds, and add a null row: "Whether the two road neighbors receive on the coastal supply line | **Not stated on Mirny's lines** | their own entries carry it; excluded by `DR-131` item 3". The tie stands on (1) the route and (3) the relay hardware. (b) Keep a narrowed (2) as Mirny's own supply role on the line, without placing the neighbors on it. Under this option the ground no longer connects to *those two* neighbors. (c) Hold (2) without admissible content, as the tie already does for its "cultural" half (R-60), until a Mirny line or a ruling places the neighbors on the line. (This was the F-12 item check's recommendation.) (d) Re-ground (2) on subnet membership: both neighbors are members of the subnet whose line Mirny likely receives first. This needs DEC-492 answered (a). (Proposed in Round 1 and withdrawn in Round 3: it rested on a paraphrase of the line's name as Mirny's subnet's line.)
**Recommendation:** (a), PROVISIONAL. All three readers recommend it after Round 3. The null table is the pass's own place for "not stated"; the shared connections file grounds the two ties "on the Register, on Hwy 110 and on the relay hardware", not on supply (ST14 L341; a supporting reason only, since the pass marks that file "**Not an input.**", Phase 5 L322); (d) would be a forced fit, because membership is not a supply tie and the line's name joins two subnets; and a null row keeps "not stated here" from reading as "not so".
**What is waiting on it / what was done provisionally:** OWN-5 (the tie with the two road neighbors after "three" falls); docket row OWN-DK-7 (Phase 5 L322; its disposition follows this answer). Merges the F-12 item check's IQ-1202 and the readers' OWN-Q4, OWN-Q104 and OWN-Q205. Related in the same piece: DEC-492, DEC-495.
**Answer (developer):**

### DEC-495 · OPEN · 2026-11-11 · Mirny review, piece OWN (OWN-QD-6)
**The question, in plain words:** What does "the Mirny/Mawson subnet coastal supply line", named in Mirny's own relationship-database entry, cover? Low priority: you may simply know (PROVISIONAL).
**The facts:** `City_Relationship_Database.md` L341: "**Hub port for Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) — as the subnet hub, likely the primary receiving point for the Mirny/Mawson subnet coastal supply line". After the narrowing in DEC-494, Mirny's own entry is the line's only ground. The line's name joins two subnet hubs' names, and the subnet table lists them as two separate subnets (L48, L49; L42: "Six subnets, each named after its hub city."). "Primary" presupposes at least one other receiving point; which places the line serves besides Mirny, in which subnet or subnets, and where goods go after Mirny, are named on no Mirny line. The F-12 item check paraphrased the line as "the subnet's line"; that paraphrase is corrected. `DR-133` item 2 (`DEVELOPER_RULINGS_LOG.md` L1967) speaks of "The subnet's coastal supply line" but is recorded for another city (review note L75) and does not carry.
**Options:** A) One coastal line serving the coasts of both subnets, with Mirny likely its primary receiving point. B) A joint label for Mirny's own subnet's line, of whatever origin. C) Leave it open. Quote the line by its own name, never paraphrase it as "the subnet's" line, and record which subnet or subnets it serves as unstated.
**Recommendation:** C, PROVISIONAL, until a ruling recorded for every city, or one naming Mirny, says what the line covers. A ruling recorded for another city does not settle it (`DR-133` item 2; review note L75).
**What is waiting on it / what was done provisionally:** OWN-4's open slot (the line's other receiving points, what its two-part name covers, where goods go after Mirny) and its wording rule (quote the line by its own name). Merges reader A's OWN-Q5, reader C's open slot and reader B's Round 3 view (the question is optional; record the slot). Related in the same piece: DEC-494.
**Answer (developer):**

### DEC-496 · OPEN · 2026-11-11 · Mirny review, piece FREE (FREE-QD-1)
**The question, in plain words:** An open question asked whether Mirny's free tier (the character budget, 34.7 % of its workforce units) measures the share of people able to do work they want, or the share of a working life not spoken for by survival. Now that "time that is your own" is defined as canon's leisure only, never the free tier and never a free share of anyone's life, what is left of that question? (PROVISIONAL)
**The facts:** The question, Phase 4 (`04_Phase_04_Ordinary_Life.md`) L351: "**Q-43.** Does the freedom margin (47.1 %) measure the share of people able to do work they want (`D09` L126–127) or the share of a working life not spoken for by survival (`RP` L364–371)?"; L149: "**is a developer reading** (Q-43)". The figure was replaced before the cut-off: 34.7 %, determined (`Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md` ART-2, L83–L85); "the question of meaning stays open" (PRT L156). The ruling, `DEVELOPER_RULINGS_LOG.md` L1895 (`DR-125` item 3): "it means canon's leisure and nothing else … it does NOT mean any share of a person's life is free, and it says nothing about human leisure beyond the night, which canon does not state." Mirny's two names, L1751 (`DR-109` item 3): "the free tier (the character budget)" for 34.7 % and "the distinctive tier" for 57.8 % of Mirny's workforce units. Live figures (PRT L9, L85): workforce 1,057,064 units; baseline 446,228 (42.2 %); distinctive 610,836 (57.8 %); mandated 244,334 (23.1 %); free 366,502 (34.7 %); [CALC] 1,057,064 − 446,228 = 610,836; 610,836 − 244,334 = 366,502. The second reading's source, `Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` L365–366 ("half to three-quarters of a Tepenian working life is not spoken for by survival"), takes it from the Division of Industry's margin, the residue after the baseline (`Division_of_Industry/09_Per_City_Baseline_Run.md` L131), which that file qualifies: "**"Not baseline" is not quite "wanted."**" (L137); "That labor is mandated too, just nationally rather than locally." (L138–139); "The truly elective residue is what remains after both." (L139–140). So "not spoken for by survival" is the distinctive tier, and the robot file's "**Both are free.**" (L369–371) is what the ruling excludes. [CALC] Units do not convert to persons: robot units are 710,578 ÷ 1,057,063.5 = 67.22 % of workforce units while robots are 710,578 ÷ 1,403,549 = 50.63 % of residents, and who staffs any tier is "a free design variable" (`04_Phase_07_Order.md` L155).
**Options:** A. Unchanged: both limbs stay open as written. (The state of the record until the developer answers.) B. Narrowed only (the F-13 item check's IQ-1301 (B)): the second limb stays a possible meaning of the free tier, read only as work whose reason is not survival, never as a share of a life that is free. C. Sorted, then one question left: the second limb leaves the free tier and is recorded as the distinctive tier's definition only (57.8 %, the residue after the baseline, with no "free" or "own" reading); at the model's level the free tier (the character budget, 34.7 %) is the elective residue, work whose reason is the holder's want, an average of workforce units; Q-43 then asks only whether the free tier is read in-world at the city's scale alone (the four sectors section 20 leaves unmandated) or also at a person's scale (a share of people doing work they want, `D09` L128–129), which would also need a staffing split no admitted line gives. *Not offered:* reading the ruling's parenthetical as a general definition of the free tier; it carries another city's figure and unit and does not carry (standing line 25).
**Recommendation:** C, PROVISIONAL. All three readers. By its own source the second limb is the residue after the baseline, which `DR-109` item 3 already names apart; B would keep that tier's definition under the free tier's name, and the narrowed limb holds for the free tier only because it holds for the whole distinctive tier. C leaves the person scale to the developer.
**What is waiting on it / what was done provisionally:** FREE-1 (what the free tier measures; its sorting cannot be relied on until this is answered); FREE-3's person-scale tie of wanted work to the free tier; docket rows FREE-DK-1 (restatement PROVISIONAL on this question), FREE-DK-2, FREE-DK-4 (any reading in persons waits on it), FREE-DK-25 and FREE-DK-26. Merges the readers' FREE-Q1, FREE-Q101 and FREE-Q201 and the F-13 item check's IQ-1301.
**Answer (developer):**

### DEC-497 · OPEN · 2026-11-11 · Mirny review, piece FREE (FREE-QD-2)
**The question, in plain words:** Phase 6 said Mirny's site price comes out of the same pool as the leisure the nation reads as proof that leaving worked, and that "work as devotion" and "leisure as proof" meet in that pool; with leisure now ruled separate from the free tier, the pool is gone. What should stand in place of that finding and its story seed? (PROVISIONAL)
**The facts:** Phase 6 (`04_Phase_06_Meaning.md`) L119, second order: "*2nd [D].* At Mirny the wind's price is drawn from the same pool, so part of what the nation reads as the proof that leaving worked is spent keeping the wind out (conditional)."; third order: "**two standards of worth touch here — leisure as proof, work as devotion** (seed S3)". Phase 6 L146 (S3): "two standards of worth in one pool"; Phase 7 (`04_Phase_07_Order.md`) L458: "the free-tier worker holds two standards in one pool (`P6` S3)". The pool was the free tier in workforce units (Phase 7 L167). The proof: "It is the material proof that leaving worked." (`Robot_Physiology_and_Cultural_Practices.md` L360). The ruling (`DEVELOPER_RULINGS_LOG.md` L1895) puts canon's leisure outside every tier, so a price charged to the free tier spends none of the proof. The site's price is charged in the model under a 40/60 convention, and "no admitted line says the Federation reckons anything in this way" (`Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md` L104). What the site does reach is when the shared stop can be cued and where and how leisure is spent: midnight sun "about Dec 8 → Jan 5" and "no night for ~29 days" (Phase 4 L122, L160; [CALC] 24 + 5 = 29); "**A stop that is shared and is not the sky's night.**" (Phase 4 L233); "**a retreat to quiet is not written**" and the glove cost outdoors (Phase 4 L160); "**A night place held above freezing, as the default for both bodies**" (Phase 4 L234). The seed can rest elsewhere: "**Wanted work carries no external stop.**" (Phase 4 L151), kept with no number (PRT L41).
**Options:** A. Retire: strike P6-8's second and third orders and retire S3; keep the national canon only. B. Strike and re-locate: strike the second order without restating it (the docket note, FREE-DK-13, gives the reason); move the third order and S3 to the stop, inside a robot whose work is her own want, robot half only (FREE-3); re-ground "at Mirny's own values" on the stop's conditions and the site's bounds on leisure's shape (FREE-2). C. As B, and restate the second order in FREE-2's terms: the site's price is charged in the model to Mirny's work, never to canon's leisure, and the site reaches leisure only in its shape and in where and when the stop is held. D. Hold P6-8 and S3 until Q-43 is answered and R-45 and the CST supply leisure content.
**Recommendation:** B, PROVISIONAL. S3 rests on Phase 4 L151, kept with no figure, and does not wait on Q-43 or a tier, so D waits on what S3 no longer depends on; A drops the Mirny content all three readers found (the stop's conditions and Phase 4's bounds on leisure's shape). Two readers re-derive Mirny's half in place, and one offers no restatement of the second order; B is recommended because it claims less, with C offered for a developer who wants the re-derived sentence in the line. One reader would ask only about S3 and treat P6-8 as a docket choice; it is written as one question on both, because asking claims less than deciding.
**What is waiting on it / what was done provisionally:** FREE-2 and FREE-3 (the re-located seed cannot be relied on until this is answered); docket rows FREE-DK-12, FREE-DK-14 and FREE-DK-17 (each PROVISIONAL on this question), and FREE-DK-20 and FREE-DK-21, which carry the re-located seed into Phase 7. FREE-DK-13 (the strike of the second order) is recommended at high confidence under B and C alike. Merges the readers' FREE-Q103, FREE-Q203 and FREE-D5 (a docket proposal, offered here as C).
**Answer (developer):**

### DEC-498 · OPEN · 2026-11-11 · Mirny review, piece FREE (FREE-QD-3)
**The question, in plain words:** The ruling gives humans one stated portion of time that is their own, the shared night, but Mirny has about 29 days a year with no night, and an open question already asks whether the daily stop holds then as a rule both bodies keep or by coincidence. Does the ruling bear on that question? (PROVISIONAL)
**The facts:** `DEVELOPER_RULINGS_LOG.md` L1895 (`DR-125` item 3): "For everyone, human and robot, there is the shared night, when all stop at the same time for different reasons"; it "says nothing about human leisure beyond the night, which canon does not state." Phase 4 (`04_Phase_04_Ordinary_Life.md`) L122: "the span of midnight sun, about Dec 8 → Jan 5"; L160: "no night for ~29 days"; [CALC] Dec 8–31 inclusive is 24 days, plus Jan 1–5 is 5: 29. L233: "1. **A stop that is shared and is not the sky's night.**" The open question is Q-41 (Phase 4 L349); meanwhile PA-18 holds: "The shared stop is a daily recurrence at which both bodies are indoors." (Phase 4 L354). That the ruling's "shared night" is Mirny's stop is Phase 4 L233's reading held by PA-18, not a ruling. The readers split on whether to ask: one would drop the question because its recommended answer is the docket note itself; two keep it, because option C is a real alternative a docket note cannot offer.
**Options:** A. No: Q-41 stands as written. B. Annotate Q-41 (FREE-DK-11): its answer now also decides whether a human at Mirny has any stated time of her own through the days without night; its first half (a rule the two bodies keep, or a coincidence of dusk) stays open. C. The ruling answers Q-41's first half at Mirny: since it gives everyone the shared night and the sky gives none for those days, the stop must be a rule the two bodies keep; only what keeps it stays open.
**Recommendation:** B, PROVISIONAL. The ruling defines a phrase and was not given against a sky without night, so reading a ruling about Mirny's sky into it would be forced. Phase 4 already writes the stop as "not the sky's night" (L233), and Q-41's own note, "P4-1 stands under either answer", stays true. What changes is what the answer moves.
**What is waiting on it / what was done provisionally:** Docket row FREE-DK-11 (the annotation to Q-41 at Phase 4 L349); FREE-4's conditional third order (were Q-41 answered against a rule, Mirny's humans would have, in those weeks, no time canon calls their own) and FREE-2's conditional third order. Merges reader B's FREE-Q102 and readers A's and C's Round 3 rows.
**Answer (developer):**

### DEC-499 · OPEN · 2026-11-11 · Mirny review, piece FREE (FREE-QD-4)
**The question, in plain words:** Phase 7 had a clause about "the year the Federation asked for hours back", and the later amendment that replaced those Phase 7 lines restated them without the clause and never said whether it meant to drop it. Is the clause dropped, standing, or to be restored? (PROVISIONAL)
**The facts:** Phase 7 (`04_Phase_07_Order.md`) L168: "at Mirny the pool it would draw on is a quarter smaller than Phase 4 wrote", with the clause "The "year the Federation asked for hours back" (`DOI10`, corroboration only) is a national object". The replacement, `Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md` ART-4: its scope line "replaces … the P7-2 table and argument (L158 to L168)" (L109); its restatement, "**exactly a quarter smaller than Half B's row** … Stated only within the live set" (L123); snag 12, ""than Phase 4 wrote" dropped from the quarter claim" (L223); it restates the line's last clause on one sector figure (L125) and does not restate the Federation clause. [CALC] 0.6 ÷ 0.8 = 0.75; 366,502 ÷ 488,668.8 = 0.7500. The ruling (`DEVELOPER_RULINGS_LOG.md` L1895, `DR-125` item 3): if the clause is kept, it is a claim on work, never on anyone's own hours ("workforce units per resident; not an hours claim", PRT L114). Canon's leisure is "Owed to nobody" (`Robot_Physiology_and_Cultural_Practices.md` L356–357), set against a past in which it was "contingent, personal, and revocable" (L353–354). `DOI10` is corroboration only and was read by no reader.
**Options:** A. Not in the live text: record that ART-4 does not restate it; if it ever returns, it is a claim on work only, never on anyone's own hours (`DR-125` item 3). B. Standing under ART-4's silence, read as a claim on work in the free tier only. C. Restore it in labor terms after `DOI10` is read (a national call on Mirny's work comes out of the distinctive tier and, under the 40/60 convention, partly out of the character budget).
**Recommendation:** A, PROVISIONAL. All three readers. `DOI10` is corroboration only and was read by no reader; restoring a clause about an unread object would rest a Mirny line on a source no reader of this piece has seen. Until it is answered, FREE-DK-18 covers both A and B.
**What is waiting on it / what was done provisionally:** FREE-6 (the pool a national call would draw on: work, never time); docket row FREE-DK-18 (Phase 7 L168), written to cover both A and B. Merges reader A's FREE-Q3, reader B's snag 1 and FREE-D118, and reader C's FREE-D213.
**Answer (developer):**

### DEC-500 · OPEN · 2026-11-11 · Mirny review, piece NODE (NODE-QD-1)
**The question, in plain words:** Australia is now a four-node supply partner and Mirny is one of its receiving nodes; when the note on Phase 5's sea-supply row (and on the 2026-11-05 geometry re-test) states the current nodes, should it name the other nodes, give only the count, or drop the count? (PROVISIONAL)
**The facts:** `DEVELOPER_RULINGS_LOG.md` L1967 (`DR-133` item 1): "Australia is a **four-node** partner" and "The developer reminder of 2026-10-03 recorded in `Ports.md` ("a THREE-NODE partner") is superseded."; the developer's words (L1966): *"Four nodes; supersede 10-03"*. The ruling is recorded among another city's freight follow-ups but item 1 names Mirny. `Locations/Infrastructure/Ports.md` L129: "✅ four-node *(three-node until 2026-11-10)*"; L188: "SUPERSEDED IN PART 2026-11-10 (`DR-133`): Australia is now a FOUR-node partner"; L386, Mirny's receiving-node row: "✅ Australia-partner receiving nodes | ⚠ tier not established". Phase 5 (`04_Phase_05_Relation_and_Geometry.md`) L179 quotes the node list and "three-node" as Ports L129 read before 2026-11-10; `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` L662 carries the same "three-node" qualifier. The change brings onto Mirny's line a node the pass never named; Ports L129 and L386 name that node on lines that also name Mirny, so they count as Mirny's own lines under `DR-131` item 3 (review note L27); the fourth node's own lines stay unread (review note L47–L48). No admitted line divides calls or cargo among the nodes, so the count sizes nothing at Mirny (NODE-1).
**Options:** Option 1. Quote Ports L129 whole, with all four names and "four-node", in the note and in the finding. Option 2. Quote Ports L129 whole as the cited source, and write the finding about Mirny with no other name: "Mirny is one of Australia's four receiving nodes, ✅." Option 3. Give the count and Mirny's membership with no other name anywhere, and cite "four-node" at Ports L129 by its address. Option 4. Drop the count, and state only Mirny's direct membership and its tier ("not established", Ports L386).
**Recommendation:** Option 3, PROVISIONAL. All four options are legal under `DR-131` item 3, and all three readers accept a finding that names no other place. Option 3 claims least. The address L129 already says which four, the other names carry nothing that flows to or from Mirny, and the citation stays exact. Option 2 is the close alternative; it answers the concern that "four" without its four cannot be checked. Option 1 adds other places' names to Mirny's finding, and option 4 drops a canon fact that Mirny lives with. In Round 3 two readers moved to option 2 and one to option 3; option 3 is written because it is the narrowest current view and fits the name-free finding. A vote count does not settle it, and the choice is the developer's.
**What is waiting on it / what was done provisionally:** The proposed addendum for Phase 5 L179 and the 2026-11-05 re-test (written in option 3's wording; under option 2 its source citation also quotes Ports L129 whole); docket rows NODE-DK-1 (Phase 5 L179) and NODE-DK-4 (ST14 L662); NODE-1's finding. Merges the readers' NODE-Q1, NODE-Q101 and NODE-Q201; the F-15 item check's IQ-1501 recommended option 1.
**Answer (developer):**

### DEC-501 · OPEN · 2026-11-11 · Mirny review, piece F-7 item check (IQ-701)
**The question, in plain words:** The developer ruled that robots are in the origin rows, each body at its own percentage, without saying which row a robot who came online at Mirny is counted in. How is such a robot placed in an origin row? (PROVISIONAL)
**The facts:** The ruling, `DEVELOPER_RULINGS_LOG.md` L1922 (`DR-128` item 1): "**(1) An origin row applies to both humans and robots, each at its own percentage.**"; "This settles in part the "does a robot made in Tepenia have a national origin" point left open in `DR-127` item (3): robots are in the origin rows."; and the review note (L25): "Whether a row records nationality or residence at departure is not addressed", so a row's basis has no departure to read for her. The provisional assumption it bears on, Phase 2 (`04_Phase_02_Composition_and_Arrival.md`) L512: "**PA-14.** Robots built at Mirny, if any, have a learned origin from Mirny's own cultures. *Overturned by:* R-13 or a ruling." Its grounds: `DR-11` (rulings log L458): "**Learned, not built in:** a robot absorbs the cultures she is immersed in while her consciousness develops after coming online — as humans do, **without a childhood or adolescence**"; `Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` L426: "**Robot vernacular language tracks the dominant local culture and the community who had her built — robot, human, or both**". R-13 (whether chambers stand at Mirny) was answered before this review: "R-13 is answered: an array of fabrication chambers stands at Mirny, so robots are built here and come online as adults" (`Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` L702). The every-city rule for robot rows is not yet made (review note L73). The F-7 check's verdict is HOLDS: the ruling agrees with PA-14 (one property, origin, with two effects: on the individual robot, learned by immersion; on the table, counted in a row at the robot side's own percentage).
**Options:** (A) Keep PA-14's reading as Mirny's provisional assumption: her row follows the communities she is immersed in and the one that had her built (`DR-11` L458; robot physiology file L426); Mirny's robot-side percentages stay unstated until set. (B) Keep PA-14 as written but mark its row placement open until the every-city robot-row rule is made (that rule is not yet made; review note L73).
**Recommendation:** (A), with (B)'s marker, PROVISIONAL. PA-14 stays as written (its "if any" read through AS14-51, the 2026-11-05 answer on chambers), `DR-128` item 1 is noted beside it as partial ground, and no robot-side percentage is proposed for Mirny here.
**What is waiting on it / what was done provisionally:** Under either option PA-14 (Phase 2 L512) stays as written; its carrying lines, Phase 4 (`04_Phase_04_Ordinary_Life.md`) L176 and `Amendment_Rederivation_P2c_Composition_2026-11-03.md` L169 (N-1), hold. No docket row; no robot-side percentage proposed. See also DEC-488 (the COMP piece asks how Mirny's lines read the robot figures in the origin rows, on the same ruling).
**Answer (developer):**

### DEC-502 · OPEN · 2026-11-11 · Mirny review, piece F-9 item check (IQ-901)
**The question, in plain words:** The developer ruled, for every city, that tiers reached after the random draw stand as relabeled. Does that answer in part the open question of how "Primary" is read at Mirny, where the census defines Primary in the singular and Mirny has six Primary rows? (PROVISIONAL)
**The facts:** The ruling, `DEVELOPER_RULINGS_LOG.md` L1949 (`DR-131` item 7): "**(7) Drawn tiers, for every city:** tiers reached after the random draw stand as relabeled; the dividing rule stays the composition file's own (no row at 4.5% or more is Notable)."; the developer's selection (L1948): *"Tiers stand as relabeled (Recommended)"*; heading (L1944) in part "DRAWN TIERS STAND (ALL CITIES)". The census, `Official_Population_Census.md` L36: "**Primary** — Dominant national community; shapes the city's primary linguistic and cultural identity". The open question, `Amendment_Rederivation_P2c_Composition_2026-11-03.md` L222: "**AQ-23 · How is "Primary" read at Mirny?** The census defines it in the singular (Dominant national community); Mirny has six. **Recommendation:** a tier label: the six largest communities jointly, none shaping the city's linguistic and cultural identity alone."; it stays open (P2c L259: "AQ-20, AQ-22 to AQ-26 stay open"). Mirny's table: "Thirty-six stocks: **6 Primary, 11 Significant, 19 Notable**" (P2c L15). No Mirny line names a draw or relabeling of tiers (review note L108). [CALC] No Notable row at Mirny can be above 2.71 % (5.247 − 2.537 = 2.710), so every one is below 4.5 % and no Mirny label is put in question. The review note's section G found that no ruling of these two days settles any Mirny question "in whole or in part" (L117). Recorded by the check, not caused by the ruling: P2c L192's null row states the joint reading as if adopted, while L259 keeps the question open. The check's verdict is HOLDS.
**Options:** (A) No. The ruling fixes which rows carry the Primary label. How the census's singular definition is read across six rows ("jointly, none alone") is untouched, so the question stays open as asked. (B) Yes, in part. The ruling confirms the "tier label" reading, and only the "jointly, none … alone" half stays open.
**Recommendation:** (A), PROVISIONAL. The ruling's text concerns labels and the Notable dividing rule. It says nothing about the meaning attached to the Primary label. The review note's section G found no ruling of these two days settles any Mirny question "in whole or in part" (L117), and (A) keeps that consistent.
**What is waiting on it / what was done provisionally:** Nothing applied; no docket row. The F-9 check holds both lines it tested, P2c L222 (the open question and its recommendation) and `Amendment_Rederivation_PIU_IdelskUralia_2026-11-04.md` L126; under either option the "jointly, none alone" reading stays the developer's choice. See also DEC-489 (the COMP piece asks whether any Mirny line may name one Primary row "the largest", which bears on the same open question).
**Answer (developer):**

---

## Open since 2026-11-11 (Casey ULM run; every answer below is PROVISIONAL until you give yours)

*Casey's own questions from its warm run of 2026-11-11, in the order they arose. Casey's files are in `City_Development_Passes/Mirny_Subnet/Casey/`. Until you answer, each runs on its recommended answer, as the "What is waiting on it" line says.*

### DEC-510 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Step −1 amendment (AMD-Q1)
**The question, in plain words:** The new definition of the national language (Hawaiian, which becomes Tepenian) was recorded during another city's cross-check. Does it apply to every city, Casey included? (PROVISIONAL)
**The facts:** `00.1_Step_MINUS-1_Amendment_2026-11-11.md` L228: the definition is `DR-125` item 6, first sentence; "It was recorded during another city's cross-check and is not marked for every city in words, as `DR-131` items 3 and 7 are (L1949)." All three readers read it as national, because it defines the one language that `DR-100` item 1 makes dominant everywhere. A Casey amendment may move a Casey decision only on a ruling recorded for every city or naming Casey.
**Options:** (a) Yes: it is national canon by its subject, and the amendment's two language decisions (AMD-1, AMD-2) apply to Casey. (b) No: Casey's contract keeps its language lines (§5 L375 and L377) as written until a ruling marks the definition national.
**Recommendation:** (a), PROVISIONAL (all three readers).
**What is waiting on it / what was done provisionally:** AMD-1 and AMD-2 run as written in Casey's run.
**Answer (developer):** "(a) Yes, national (Recommended)": the language definition (`DR-125` item 6) applies to every city, Casey included; AMD-1 and AMD-2 stand.

### DEC-511 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Step −1 amendment (AMD-Q2)
**The question, in plain words:** When other places' finished passes open at Step 6, may a line in one of them bring a relation into Casey's run, if the line is about a shared thing Casey is named in? (PROVISIONAL)
**The facts:** `DR-131` item 3 admits "lines about shared things it is named in" (rulings log L1949), but does not say where such a line may sit (amendment L233).
**Options:** (a) Directly, as the ruling's letter allows. (b) As corroboration only: the shared thing's own file supplies the relation, and the other pass's line at most corroborates it. (c) As a pointer only: the line points to the shared thing's own record, and the relation is taken from that record, at Casey's lines in it. (d) Not at all: other passes supply nothing in-run, not even pointers.
**Recommendation:** (c), PROVISIONAL (all three readers after their cross-check). It admits the same content as (a) without resting a finding on another location's derivation, and it keeps a connection that only another pass would reveal, which (d) would lose.
**What is waiting on it / what was done provisionally:** AMD-3 runs on (c).
**Answer (developer):** "(c) Pointer only (Recommended)": a line in another pass may only point to the shared thing's own record; the relation is taken from that record at Casey's lines in it. AMD-3 stands.

### DEC-512 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Step −1 amendment (AMD-Q3)
**The question, in plain words:** Does Casey's parent subnet count as a shared thing Casey is in, so that lines about the subnet count as Casey's own lines? (PROVISIONAL)
**The facts:** The ruling's recorded list is "(its port, airport, road, cluster)" (rulings log L1949); your selection was "Own files + shared things it's in (Recommended)" (L1948), which is broader than the list. Casey is in the subnet (spec L5), and one of Casey's open requests (REQ-13) asks about its status in the subnet. No cluster is named for Casey in the readers' material (amendment L240).
**Options:** (a) Yes: the list gives examples. Lines about the subnet count as Casey's lines, less any clause grounded only in another city's lines; the subnet's regional framework stays reserved, and the nickname stays a name only (`DR-13`). (b) Only if a subnet is a cluster in the ruling's sense. (c) No: the list is the full set, and for the subnet only Casey's own entries count. (d) Leave it open until Phase 5 meets such a line.
**Recommendation:** (a), PROVISIONAL (all three readers). A subnet is shared by its members as plainly as a road is, and the clause exclusion keeps other members' lines out.
**What is waiting on it / what was done provisionally:** AMD-6 runs on Casey's own entries only until you answer.
**Answer (developer):** "(a) Yes (Recommended)": the parent subnet counts as a shared thing Casey is in; its lines count as Casey's own, less any clause grounded only in another city's lines; the subnet's regional framework stays reserved and the nickname stays a name only. AMD-6 widens accordingly.

### DEC-513 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Step −1 amendment (AMD-Q4)
**The question, in plain words:** The open question of which source folders may ground a finding (`DEC-003`) is deferred "to be settled once for every city when the first new run needs it". Casey's run is a new run. When must it be settled for Casey? (PROVISIONAL)
**The facts:** `DR-131` item 13 (rulings log L1949) defers `DEC-003`. The amendment's decisions on shared files (AMD-4 to AMD-7) settle which lines of those files Casey may use, and assume the folders stay admitted as the contract records them: `Division_of_Industry/` by your answer to Casey's DQ-3 (contract L484), and `Infrastructure/` and the relationship files as Phase 5 must-open sources (contract L307, L317, L500), which rests on the Pre-Trip sheet and on a request (R-5) not yet confirmed (amendment L247).
**Options:** (a) Settle it before the first Casey step that grounds a finding on a shared folder not already answered for Casey; that falls at Phase 5 at the latest. (b) Run Casey on the contract's existing admissions, and bring `DEC-003` at the first Casey step that needs a folder neither the ratified roots nor a Casey ruling admits. (c) Settle it now.
**Recommendation:** (a), PROVISIONAL. The readers split: one recommended (b), because the folders are already admitted; the written answer is (a), because it treats your DQ-3 answer as settled for that folder, does not treat the Pre-Trip's Phase 5 admission as a settled answer, and holds no step before Phase 5.
**What is waiting on it / what was done provisionally:** Nothing is held before Phase 5. Phase 5's set-up checks this entry first.
**Answer (developer):** "we can use the inspiration-picks" (the picks may ground findings), and "Yes, confirm both" (the `Infrastructure/` files and the city-relationship files are confirmed as usable evidence for Casey, so Phase 5 needs no further question on them). Still deferred for every other city and folder: `DEC-003` itself.

### DEC-514 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Step −1 amendment (AMD-Q5)
**The question, in plain words:** A reviewer's reading, recorded beside the new language definition, says the national-vocabulary caution covers words of English and Japanese origin. English is also Casey's supporting language. Does that caution reach Casey's work? (low priority; a national question) (PROVISIONAL)
**The facts:** Rulings log L1895: "Reviewer's reading, not the developer's words: the national-vocabulary caution therefore covers words of English and Japanese origin and of the supporting bases." English is a primary base of the national language and Casey's supporting tier is English alone (`DR-100`), so a word of English origin at Casey may be national vocabulary rather than anything of Casey's own. The caution's own text is in no reader's material (amendment L253).
**Options:** (a) Adopt the reading as stated, for every city. (b) Leave it unadopted until you have the caution's text in front of you and rule on it; Casey's naming runs under the existing rules. (c) Adopt it for Casey alone.
**Recommendation:** (b), PROVISIONAL. It claims least: a national rule should not be adopted through one city's amendment, and no reader has read the caution itself. One reader first recommended (a).
**What is waiting on it / what was done provisionally:** AMD-1 records the caution as not a rule and not applied.
**Answer (developer):** The developer never said anything cautioning English- or Japanese-derived words; the "reviewer's reading" recorded beside `DR-125` is not his. **Option (b): left unadopted.** Casey's naming runs under the existing rules.

### DEC-515 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Step 0 (DQ-8)
**The question, in plain words:** One of the comparison substitutes a single-city run may use is "the location's own earlier states" (Casey then against Casey later). Founding dates and histories are deferred until after the ULM (`DR-16`). Does that substitute run in Casey's pass, and in what form? (PROVISIONAL)
**The facts:** Casey's contract §8 (L441), which you accepted, runs "Act 1 against Act 2 within the frame" as its first substitute; `Run_Modes_Warm_and_Cold.md` L126 lists "the location's own earlier states" as "(deferred with the histories, `DR-16`)"; `01_Frame_Typology_and_Inheritance.md` L470–471 calls it "The strongest substitute, usually available, and the one to reach for first." (`00_Frame.md` L623–630).
**Options:** (a) No: deferred entirely with the histories; the in-run substitutes are real-world comparables and the generator-conflict method only. (b) Yes, narrowly: an undated two-state contrast, Act 1 against Act 2, resting on national canon about the Acts applied to what Casey's admitted lines already state, with no Casey dates, no events and no census pair. (c) Yes, in full: three states, or Casey events in each era, or the census pair; not runnable while the founding date stays reserved and `DR-16` stands.
**Recommendation:** (b), PROVISIONAL (all three readers). It keeps the strongest instrument that needs no other city without touching the deferred histories.
**What is waiting on it / what was done provisionally:** Casey's phases run on (b), with no dated Casey history.
**Answer (developer):** "I would say Option (A), yes": option (a), no earlier-state comparison in the pass. The developer's reason: each location is identified at its height, so that how it got there and how it declined can be worked out afterward. Casey runs with no dated Casey history and no Act 1 against Act 2 contrast. (Option (a) reads "No: deferred entirely with the histories"; asked whether that was his meaning, he answered "essentially, yes". Recorded as `DR-136` item 6.)

### DEC-516 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Step 0 (DQ-9)
**The question, in plain words:** One line in the relationship database (its L170) is about Casey's port and a freight link with its founder nation. It touches an open national question (how a "no direct relationship" condition sits beside the Register's record of Australia's role). Until that is decided, how does Casey's run treat the line? (PROVISIONAL)
**The facts:** The open national question, as the amendment records it (L222): "The national question of how the no-direct-relationship condition sits beside the Register's record of Australia's role stays open for a detailed discussion." (`DR-125` item 9). The condition's own wording is in no reader's material. Casey's port status (REQ-7) can still be answered at Phase 5 from Casey's own lines in `Ports.md` (AMD-5) without this line (`00_Frame.md` L632–641).
**Options:** (a) Admit the whole line at Phase 5 as Casey's own line about its port, marked as resting on an unratified file, never as a founder tie. (b) Admit the port's existence at Phase 5, and hold the freight link until the national question is decided. (c) Treat the line as a pointer: the port fact comes from `Ports.md`; the line at most corroborates, and its freight clause is held. (d) Hold all of it out of every finding until the national question is decided, or until the condition's own text is admitted to a Casey brief. (e) Exclude it.
**Recommendation:** (d), PROVISIONAL. It claims least and decides nothing nationally; the readers split across (b), (c) and (d) before settling on (d) as the narrowest view.
**What is waiting on it / what was done provisionally:** The line is held at (d). Phase 5 is several steps away.
**Answer (developer):** "(d) Hold it out of every finding (Recommended)": the relationship-database line at L170 stays out of every finding until the national question is decided or the condition's own text is admitted to a Casey brief.

### DEC-517 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Step 1 (DQ-10)
**The question, in plain words:** Casey's supporting language is English alone. What standing do the languages outside a city's supporting tier have in-world? That is a national term, and one city's pass should not define it. (PROVISIONAL)
**The facts:** `DR-100` (rulings log L1668) item (2) says what a supporting tier is: "a language that is not dominant but widely enough understood that business, social talk and general dealings can be done in it and people can be assumed to follow". **The orchestrator's reading (not a reader's finding):** the ruling says nothing of the languages outside the tier. Casey's question was written to go to you only if the ruling is silent (`01_Inherited.md` L365, with request REQ-33, which also asks that the ruling's text be put in the brief of the phase that writes the language of the place; that still happens). So it goes to you narrowed to that half.
**Options:** (a) A national definition: you state what standing languages outside the tier have, and each city writes only its own form of it. (b) Per city: each city's pass writes it for itself. (c) A design label only: the tier makes no in-world difference beyond `DR-100` item (2), and community languages are written as part of the general population.
**Recommendation:** (a), PROVISIONAL. (b) would let each city's pass define one national term its own way; (c) is possible, but it would itself be a ruling.
**What is waiting on it / what was done provisionally:** Casey's phases ask only what lies outside the tier at Casey; nothing defines the tier's outside.
**Answer (developer):** "(a) National definition (Recommended)": the developer will state the standing of languages outside a city's supporting tier once, nationally; each city then writes only its own form. Not yet stated; Casey runs provisionally and asks only what lies outside the tier at Casey.

### DEC-518 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, the sheets (CL-12, CL-19)
**The question, in plain words:** Two of Casey's draft datasheets and its Pre-Trip sheet carry stale line numbers or material the contract keeps out. The run reads the live sources and keeps those rows out of every reading list. Should the sheets be corrected now, after the run, or left? (PROVISIONAL)
**The facts:** `Datasheets/Step_1_and_2.md`: the row at L30 quotes a conclusion the contract excludes (spec L108–109); the row at L34 carries the reserved founding date and an excluded clause about the station's operator (Casey log CL-12). `Datasheets/Phase_2.md`: L18 describes the composition file's pool table, which its own L639 calls "the derivation before the rework"; L19 cites the rule list at L26–L33 (now L28–35); L24 names the real station's operator (a coordinate only, `DR-19`, `DR-24`); L25 quotes spec L173, outside the admitted spans. `00.0_Pre-Trip_Inspection.md` L272 still names the pool table L633–L637 and the old rule-list lines (Casey log CL-19). Casey's contract already asks for datasheet corrections (REQ-14).
**Options:** (a) Correct the sheets after Casey's run, in one pass, with the run's own findings in hand. (b) Correct them now, mid-run. (c) Leave them; they are drafts and the run never relies on them.
**Recommendation:** (a), PROVISIONAL. Changing a sheet mid-run would change an input while later phases are still being briefed; one correction at the end keeps every brief's inputs fixed.
**What is waiting on it / what was done provisionally:** Nothing waits; the rows are kept out of every list and the live sources are read.
**Answer (developer):** "(a) After Casey's run (Recommended)": the sheets are corrected in one pass at the end of the run.

### DEC-519 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Step 3 (CL-17)
**The question, in plain words:** Casey now has a research log (`Research_Logs/Casey_Research_Log.md`, new today). The log folder's README keeps an index of logs and has no row for it. May a one-line Casey row be added? (PROVISIONAL)
**The facts:** `Research_Logs/README.md` L122–129 is the index; L131–135 record that the index is already incomplete, "Raised rather than swept". The Step 3 merge was told not to edit the README.
**Options:** (a) Add Casey's row at the end of Casey's run, with the log's final counts. (b) Add it now. (c) Leave the index as it is.
**Recommendation:** (a), PROVISIONAL. The log may gain later sessions in this run; one row written at the end states its real counts. The other missing rows stay a separate task.
**What is waiting on it / what was done provisionally:** Nothing; the log exists and is named in Casey's Step 3 files.
**Answer (developer):** "(a) At the end of Casey's run (Recommended)": one row with the log's final counts.

### DEC-520 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Phase 2 (DQ-11)
**The question, in plain words:** A ruling recorded at another city's cross-check says a later-era robot's origin row records the community she came online in, as ancestry. Does that reach Casey, and for which robots? (PROVISIONAL)
**The facts:** `DR-131` item 2 (rulings log L1949): "a later-era robot's row records the origin stock of the community she came online in, as ancestry; the copied shares stand for now, with one rule for every city later". It is not marked for every city. The runbook holds whether robots carry a national origin at all as an open reserved question (runbook L2120-2121). Casey's robot half also holds robots exiled from Upper Earth, whose origin comes from immersion there (`DR-11`, as Casey's contract L337 carries it). No community holds a majority at Casey, so a robot built by a community of several origins is a real case the item does not cover (`04_Phase_02_Composition_and_Arrival.md`, DQ-11).
**Options:** (a) It reaches every city for robots built in Tepenia; an exile-era robot's row records the place of her immersion, so one row carries two meanings; the mixed-community case waits for the national rule. (b) Not yet: until the one rule for every city is recorded, Casey's robot rows stay the copied human proportions (spec L74), no ancestry is stated for any robot built at Casey, and exile-era robots stand on `DR-11`. (c) It reaches every city, and every robot row is ancestry, exile-era robots included. (d) It reaches every city, and a robot whose building community is mixed records the city's own distribution as her ancestry.
**Recommendation:** (b) as Casey's interim, PROVISIONAL, with (a)'s first clause offered as the start of the national rule and the mixed-community case added to it. It claims least. The readers split in their first round and settled on (b) in the cross-check.
**What is waiting on it / what was done provisionally:** Phase 2's findings P2-5, P2-29 and P2-31 are written on (b).
**Answer (developer):** "A combination of a, b, & d". **Orchestrator's reading, to be corrected if wrong:** a robot built in Tepenia has a row recording the ancestry of the community she came online in (a); an exile-era robot stands on `DR-11` (place of immersion); where her building community is mixed, as at Casey where no community holds a majority, her row records the city's own distribution (d), which is the copied human proportions of the spec (b); no other ancestry is stated for Casey's robots until the national rule is recorded. **Confirmed by the developer 2026-11-15:** "basically, pretty much. If a robot develops her/his culture within a predominantly `[X]` population, then that robot can reliably be considered `[X]`. There may not consistently be times when this is the case, and people (both robots and humans alike) make draw their influences from multiple cultures, depending on the situation." Recorded as `DR-136` item 10. Phase 2's P2-5, P2-29 and P2-31 were written on (b) and give the same figures.

### DEC-521 · ANSWERED 2026-11-15 · 2026-11-11 · Casey ULM run, Phase 2 (DQ-12; low priority)
**The question, in plain words:** The founding treaty file that Phase 2 opened calls itself a draft, "Not locked canon". May Casey's arrival findings rest on its articles? (PROVISIONAL)
**The facts:** The spine names the treaty as the founding instrument to open (spine L410-411). The file opened, `TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md`, says of itself "first full draft, 2026-07-08. Not locked canon." (its L3); its Article II.2.5 was added on 2026-11-09 (its L138). Most of Phase 2's section on arrival modes rests on its articles; the dependent findings are listed in Phase 2's last HANDED FORWARD row (Step 10).
**Options:** (a) Yes, at draft standing, with each dependent finding tagged and listed so a later revision reaches a list. (b) Only the articles the draft's own notes record as confirmed or as added at the developer's direction. (c) None until the treaty is locked.
**Recommendation:** (a), PROVISIONAL. It is the instrument the method requires opening, and the tag and the list keep every dependent finding reachable. One reader raised the question and later judged the tag and list enough; the other two judged the choice real, so it is asked rather than assumed.
**What is waiting on it / what was done provisionally:** Phase 2 runs on (a); its treaty-dependent findings carry the tag [treaty draft].
**Answer (developer):** "(a) Yes, at draft standing (Recommended)": the arrival findings may rest on the treaty's articles, each dependent finding tagged [treaty draft] and listed.

---

## Answered
*(Moved here with the date and the ruling number.)*
- 2026-11-09, `DR-125`: 14 of the 60 Sinheung questions answered in place above (DEC-377, 378, 392, 394, 401, 402, 404, 409, 414, 416, 422, 424, 429, 430); DEC-434 was discussed and left open for a detailed look; the other 45 stay open and PROVISIONAL for a later review.
- 2026-11-09, `DR-128`: Davis DEC-305 and Sinheung DEC-381, 383, 390 answered in place above.
- 2026-11-09, `DR-127`: three more Davis questions answered in place above (DEC-296, 298, 299); DEC-298 carries new canon about human arrival after the signing; the other 13 Phase 2 questions put to the developer were left PROVISIONAL at his word.
- 2026-11-09, `DR-124`: 45 of the 96 Davis questions answered in place above (DEC-280, 281, 289, 291, 292, 301, 302, 307, 313 to 329, 331 to 333, 335, 339, 342, 345, 347, 349, 354, 355, 357 to 359, 363, 366 to 369, 373); the other 51 stay open and PROVISIONAL for a later review (DEC-356 was left out of the approved rows).
- 2026-11-09, `DR-94` item 4: the Davis pieces' questions about the four composition rows (the Step -1 piece's fifth question and the language piece's twelfth) are answered by the existing ruling and are not entered as open; see `Amendment_Erratum_2026-11-09_DR94_Item4_Four_Rows.md`.
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
