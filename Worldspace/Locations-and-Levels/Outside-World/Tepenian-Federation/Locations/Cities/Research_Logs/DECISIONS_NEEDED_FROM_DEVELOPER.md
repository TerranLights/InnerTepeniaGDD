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


### DEC-522 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 3 (DQ-13)
**The question, in plain words:** Can a pass treat the wildlife breeding at a real site today (penguin colonies, nesting petrels, molting seals) as part of that site's physical setting during the frame? (PROVISIONAL)
**The facts:** Physical facts of a real site are admissible, and Step 3 treats every web fact as present-day, standing for the frame only where a later step says so (`03_Research.md` L6). Living populations are not fixed geography, and the frame lies five centuries or more ahead; the island group's penguin numbers grew about sixfold in sixty years on the colony page cited in Casey's research log (Session 2, rows P3B-W4, P3C-W1). Whether the colonies are there decides Casey's only strong outdoor smell, much of its summer sound and color, and its moss ground (`04_Phase_03_Surface_and_Texture.md` L442-449; findings P3-5, P3-14, P3-18, P3-40).
**Options:** (a) Yes, as physical setting: presence carried as a present-day reference, tagged, never a count. (b) Presence only, conditional, until a ruling on how wildlife is carried across the frame; no number is ever asserted. (c) Only the plant ground (moss, alga), which is tied to rock and meltwater; not the animal colonies. (d) No: the site's living ground is unwritten until a ruling.
**Recommendation:** (b), PROVISIONAL (reader B; readers A and C moved to it in Round 3). It claims least and keeps the summer findings available without asserting a population.
**What is waiting on it / what was done provisionally:** Phase 3 runs on (b), recorded as PA-10 (P3-5, P3-14, P3-16, P3-18, P3-26, P3-35, P3-36, P3-40 rest on it).
**Answer (developer):** (b), as recommended: the colonies, nesting birds and seals are written as present, conditionally, until a ruling on how wildlife is carried across the frame; no number is ever asserted. Phase 3 stands as written (PA-10).

### DEC-523 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 3 (DQ-14; a national question)
**The question, in plain words:** National robot canon leaves three things open that Casey's texture turns on: (1) in which direction a robot's hearing is wider than a human's; (2) whether robots feel cold as discomfort or only register it; (3) whether a robot's air sensing amounts to smelling the world. Should these be ruled once for every city? (PROVISIONAL)
**The facts:** The robot-physiology file says robots perceive sound and vibration "across a meaningfully wider range than humans do" (L187) without saying lower, higher or both; it leaves open "whether robots feel cold as discomfort or only register it instrumentally" (L59); and it gives robots air handling with chemical sensors (L297-300) without saying whether they smell. At Casey these decide whether the winter is quiet for the robot majority, the robot majority's whole winter feel, and its share in the one strong outdoor smell (`04_Phase_03_Surface_and_Texture.md` L451-457).
**Options:** Hearing: wider downward (infrasound and vibration), upward (ultrasound), both, or left as written. Cold: discomfort, instrumental only, varying by robot, or left open. Smell: yes, no (only drawn vapors register), or left open.
**Recommendation:** leave all three open until ruled once for every city, PROVISIONAL (readers A and C; B in Round 3). A city's pass should not define national terms. For hearing, the Cymatics reverence file, which the physiology file names as the doctrine built on that fact, may already say; Casey's request REQ-42 asks that it be admitted to a later brief.
**What is waiting on it / what was done provisionally:** Phase 3 writes robot senses only as canon states them, recorded as PA-11 (P3-12, P3-16, P3-19, P3-21 rest on it).
**Answer (developer):** "I think that might actually depend on the robot; it might not be fully uniform". **Orchestrator's reading, to be corrected if wrong:** none of the three (the direction of wider hearing, cold as discomfort or measurement, air sensing as smell) is one fixed fact for every robot; each can vary from robot to robot. A city pass writes robot senses as varying, never as one value for its robots. The developer pointed to the *Streetside Harmonies* notes (`media/Literature/books/CurrentNovelDocs/Streetside Harmonies/`) as a place where robot physiology is already settled (see DEC-526); The notes were read 2026-11-15: they state none of the three (no hearing range, no smell, nothing on whether cold hurts); they only contrast a cold human with a robot who must make heat on purpose, by burning siligel harder (transcribed Chapter 24.md L9, L13-14). The answer stands on the developer's word. **Further answer (developer, 2026-11-15):** "much like patterns in body dimensions, a robot's sensory specifications also derive in part and are partially influenced by needs and requirements of a particular community and location. So, similarly to the way that a society that deals with a lot of heavy labor, robots will more often than not have thicker legs and wider hips, and societies that engage in a lot of agility-necessary activities, robots will be more slender and agile. Similarly, the particular requirements and needs of a particular culture and setting will influence what sorts of sensory specifications a robot will have." **Recorded:** a robot's senses follow the same rule as her build. The existing note is the Build entry, `Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` L424: body type "is not fixed per locality, but statistically weighted by it", tracking local economic and lifestyle character, a "tendency, not absolute rule". Sensory specifications are weighted the same way, by the needs of the community and setting a robot comes from: a tendency, not one fixed sense per city, and not an identity marker in itself. So hearing range, cold sensing and air sensing vary by robot (the first answer) and lean, statistically, toward what her home place needs. **For a city pass:** which way a place's robots' senses lean is that city's own finding, from its own needs, written as a tendency. **Physiology file edited under `DR-137`:** a pointer on the Build entry (L424) and the hearing line (L187), and the rule in the file's end section, "Rulings of 2026-11-15".


### DEC-524 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 4 (DQ-15)
**The question, in plain words:** How far may a city's ULM Phase 4 (Ordinary Life) write everyday life, given that food, music and everyday life belong to the CST, and where does human leisure beyond the shared night belong? (PROVISIONAL)
**The facts:** The spine requires Phase 4 to cover routines, mundane concerns, personal struggles and escapism, and says escapism is explicitly required (spine L585-589). Casey's contract puts food, music and everyday life in the CST and keeps them out of ULM findings (contract L415, RF-6; Frame L404). Canon states no human leisure beyond the shared night (`DR-125` item 3). (`04_Phase_04_Ordinary_Life.md` L597-608.)
**Options:** (a) Structure here, content at the CST: Phase 4 writes what the day is organized around, what it costs, when and where time is free, and whom the rhythm fails; the CST writes what people do in it, and human leisure is written per city at the CST. (b) Structure plus activities in kind (walking, visiting, resting), with no custom, food, music or practice. (c) Phase 4 writes everyday life in full, with RF-6 covering only food and music. (d) Phase 4 is a null in the ULM, and all of ordinary life moves to the CST. For human leisure, separately: (e) stated once nationally, each city writing only its form; (f) left silent nationally.
**Recommendation:** (a), PROVISIONAL (readers A and B; C in Round 3). It satisfies both instruments as written and leaves the leisure definition intact.
**What is waiting on it / what was done provisionally:** Phase 4 is written on (a), recorded as PA-12.
**Answer (developer):** (a), as recommended: Phase 4 writes the structure of the day (what it is organized around, what it costs, when and where time is free, whom the rhythm fails); the CST writes what people do in it, and human leisure is written per city at the CST. Phase 4 stands as written.

### DEC-525 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 4 (DQ-16)
**The question, in plain words:** The industry model counts all robots and half of humans as the workforce (`Division_of_Industry/09_Per_City_Baseline_Run.md` L5). Is that an in-world statement that every robot holds work, or only the model's basis? (PROVISIONAL)
**The facts:** Every reader used the convention; written as a fact about the day, it can be misread as canon. Canon says robots do not work all the time and owes them leisure (robot-physiology file L331-342), and says nothing about every robot holding a job. At Casey it decides whether the robot half has a non-working population of its own (`04_Phase_04_Ordinary_Life.md` L610-614).
**Options:** (a) Model basis only; whether every robot works is unwritten in-world. (b) In-world: every robot holds work, and leisure is the owed part of a working life. (c) In-world for robots, model-only for humans.
**Recommendation:** (a), PROVISIONAL (reader C; A and B in Round 3). It claims least.
**What is waiting on it / what was done provisionally:** Phase 4 runs on (a), recorded as PA-13 (P4-2, P4-28, P4-37).
**Answer (developer):** (a), as recommended: counting every robot as workforce is the industry model's basis only; whether every robot holds work is unwritten in-world.

### DEC-526 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 4 (DQ-17; a national question, low priority)
**The question, in plain words:** Does a robot perceive or experience anything during overnight recharge? (A companion to DEC-523's three questions on robot senses.) (PROVISIONAL)
**The facts:** Canon says robots require overnight recharging (robot-physiology file L334) and that the shared night is a stop for different reasons (L336); it does not say whether a recharging robot is aware, perceives (for example a storm through the walls by vibration) or experiences the hours. At Casey this decides whether the robot half's night is rest like sleep or something else (`04_Phase_04_Ordinary_Life.md` L616-620).
**Options:** (a) Leave it open until ruled once for every city. (b) Aware and perceiving. (c) Not aware, like sleep. (d) Varying by robot.
**Recommendation:** (a), PROVISIONAL (reader A; C in Round 3). A city's pass should not define a national physiological fact.
**What is waiting on it / what was done provisionally:** Nothing about a robot's experience of recharge is written (PA-11).
**Answer (developer):** already answered in the notes for the novel *Streetside Harmonies* (`media/Literature/books/CurrentNovelDocs/Streetside Harmonies/`): "A robot can be in "flight mode", wherein she/he is aware of her/his surroundings, but in much "slower motion". Just as well, while a robot is charging, she/he is "dreaming" during that time." **Recorded:** a charging robot dreams; separately, a robot can be in flight mode, aware of her surroundings in much slower motion. So the robot half's night is not blank: it is dreamed. **The novel notes' own lines** (paths under `Streetside Harmonies/`; the outlines' transcribed chapter tables are `structure/main story/stanza scene and chapter breakdowns/stanza breakdowns (transcribed)/`, read by the orchestrator 2026-11-15): charging is through nodes or a plug, overnight, "C attaches the last charging node | Her arm drops as the nodes begin charging" (Chapter 07.md L23); "V's eyes flicker as usual and she's dreaming" (Chapter 31.md L20); flight mode is a low-energy state, "vaguely akin to "flight mode" or "battery-saving mode" in order to conserve siligel" (`structure/main story/Save the Cat.md` L49), in which "she's still capable of perception and observation, so lying on that bed with absolutely nothing happening nearly drives her insane" (`structure/character arcs/Valerie.md` L198). **The "slower motion" of flight mode is the developer's own word here; the notes do not state it.** **Standing of the source:** the novel is set on Earth in 2149 (`structure/main-ref/timeline.md` L1-5), with one manufacturer's robot; the developer applies these facts to robots generally, and they are recorded on that word.


### DEC-527 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 5 (DQ-18)
**The question, in plain words:** Which way does Hwy 110 run from Casey toward the subnet's hub, and how does it pass the glacier that the Relung Panen spur cannot cross? (PROVISIONAL)
**The facts:** Casey's spec L7 writes Hwy 110 as going northeast toward the hub and the coastal chain; Casey's own entry in the relationship database writes the same neighbor as west via Hwy 110 (`City_Relationship_Database.md` L169); the great circle from Casey's coordinates bears about 260°, west-southwest (computed). The road record says the spur cannot go west because the Denman Glacier crossing is not built (`Highways.md` L278), yet Hwy 110 links Casey to a city beyond that glacier. `DR-105` item 1 settled spec L7 for Hwy 2's origin only (`04_Phase_05_Relation_and_Geometry.md` L625-629).
**Options:** (a) Hwy 110's leg runs west and passes the glacier inland, around its catchment, so the coast west of the oasis has no road. (b) It runs west, and a crossing exists for Hwy 110 but not for the spur. (c) Spec L7's bearings stand, and the road record is revised. (d) Leave all bearings unstated until a map pass.
**Recommendation:** (a), PROVISIONAL (reader A; B and C in Round 3). It fits Casey's own database entry, the spur's line and the physical bearing, and needs no new crossing.
**What is waiting on it / what was done provisionally:** No bearing is asserted beyond the computed great circle, and nothing is said about where the road passes the glacier (P5-4). No spec or record edited.
**Answer (developer):** Not yet answered: "This sounds like something we'll need to review, because the way that I'm seeing it on my map looks different." The developer's map differs from the options as written; the question is held open for a review against that map. No bearing is asserted beyond the computed great circle (P5-4); no spec or record is edited. **Reviewed against the developer's maps, 2026-11-15** (`Reference/Images/Maps/Antarctica_highway_map_by_topology.jpeg`; `Tepenian airport and flight map - highway overlay - with Relung Panen.jpeg`; the traced line `working-stash/data/highway_geometry.csv` L129-145, digitized from the developer's sketch to about ±20 km, `working-stash/CHANGES.md` L42). The orchestrator's reading: (1) from Casey, Hwy 110 runs up the page toward Mirny, which at Casey's position on a pole-centered map is true west, agreeing with Casey's database entry and the computed bearing (about 260°); spec L7's "northeast" most likely describes the line's look on the page, not the ground. (2) Between Mirny and Casey the line leaves the coast and loops inland, to about 68.5°S near 100°E (roughly 200 km south of the shore, where the Denman Glacier comes down), and returns to the coast near 99°E before Mirny: Hwy 110 passes the glacier inland. (3) **Correction to option (a) as worded:** the coast west of Casey is not roadless; the Relung Panen spur runs west from Casey along it to Relung Panen and stops there, because the coastal Denman crossing is not built (`Highways.md` L278). (4) On the sketch the line turns toward Concordia just inland of Casey (the map tooling snaps it onto Casey), and Hwy 2 starts at Casey and runs east along the coast. **Answer (developer):** "That looks right, yes." **Recorded:** (a) as corrected: Hwy 110 runs west from Casey toward Mirny and passes the Denman Glacier inland, about 200 km south of the coast; the coast west of Casey carries the Relung Panen spur only. Spec L7's bearing corrected from "NE" to "W" under `DR-137`; its "SW → Concordia" (true bearing about 160°) was not put to the developer and is not corrected. The developer added: the maps have straight lines in places where they shouldn't, which needs a study of topography rather than vectors; that is for later.

### DEC-528 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 5 (DQ-19)
**The question, in plain words:** The airport list that says Casey has no air access scopes itself to the post-war and present-day setting (`Airports.md` L3), and canon defers when airports exist in the frame (`DR-51`). Does Casey's no-air-access status say anything about Casey at its height? (PROVISIONAL)
**The facts:** Every reader wrote Casey as having no airport. The record's word "keeps" (Casey keeps its no-air-access status) belongs to a decision of 2026-10-29 (`DR-82`) (`04_Phase_05_Relation_and_Geometry.md` L631-635).
**Options:** (a) At the height, air at Casey is unsited and undecided with `DR-51`: written "none sited here". (b) The list holds across the frame: Casey has no airport at its height.
**Recommendation:** (a), PROVISIONAL (reader C; A and B in Round 3). It claims least.
**What is waiting on it / what was done provisionally:** Recorded as PA-14 (P5-7, P5-23, P5-39, P5-44).
**Answer (developer):** (a), as recommended: at Casey's height, air at Casey is unsited and undecided with `DR-51`, written "none sited here", never "no airport".

### DEC-529 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 5 (DQ-20; low priority)
**The question, in plain words:** In which era does the Australian-side intake (`DR-82`: a summer sea gateway and a winter airport, with onward flights to the subnet's hub) apply? (PROVISIONAL)
**The facts:** The intake is why arrivals from abroad pass Casey by (P5-15, P5-18). The port record lists which era it begins in among what is not ruled (`Ports.md` L300). If it begins after Casey's height, those findings describe a later Casey (`04_Phase_05_Relation_and_Geometry.md` L637-641).
**Options:** (a) At Casey's height. (b) Later. (c) Leave open.
**Recommendation:** (c), PROVISIONAL (reader C).
**What is waiting on it / what was done provisionally:** P5-15, P5-18 and P5-46 carry the intake's era as a weak leg; nothing is dated.
**Answer (developer):** (c), as recommended: the era in which the Australian-side intake applies is left open; P5-15, P5-18 and P5-46 keep it as a weak leg, nothing dated.

### DEC-530 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 5 (orchestrator; a methodology question for every city)
**The question, in plain words:** Phase 5's sub-question 5b (the three-way differentiation set) now has no form a city pass can run. Should the spine's text for 5b be amended? (PROVISIONAL)
**The facts:** The sibling form of 5b is withdrawn from every ULM pass (2026-09-06 ruling; `03_The_Phase_Spine.md` L695-708). The spine names the own-eras form (this place at its founding, at its crisis, and now) as the only remaining form (L710-724). `DR-136` item 6 (2026-11-15) rules that no earlier-state or Act 1 against Act 2 comparison runs inside a pass. Casey's Phase 5 therefore recorded 5b as a null with both grounds (`04_Phase_05_Relation_and_Geometry.md` L296-304). The spine was not edited.
**Options:** (a) Amend the spine: 5b is not run in-run; it returns with the histories and the terminal check. (b) Keep the spine as it is and record 5b as a null in each city's Phase 5. (c) Give 5b a new in-run form (to be proposed).
**Recommendation:** (a), PROVISIONAL. It makes the rule visible where a pass reads it (a methodology change goes into the runbook and spine in the same commit, by the project's own rule).
**What is waiting on it / what was done provisionally:** Casey's Phase 5 recorded 5b as a null; later cities would do the same until ruled.
**Answer (developer):** (a), with the reason restated: "I wouldn't necessarily say "banned"; rather, just in the sense that we calculate, synthesize, and derive what a society is like at its peak. That way we can extrapolate how it got there, and then how it later declined. Also, it is additionally possible that a particular location may theoretically have multiple peaks, in which case, what we're doing is synthesizing an overall average, and then we'll work out the details later." **Recorded:** the earlier-states comparison is not forbidden as such; it is out of a pass's order. A pass derives the society at its peak, and the peak is the fixed point from which the road up to it and the decline after it are extrapolated later. **Where a location may have had more than one peak, the pass synthesizes an overall average of its height, and the details of each peak are worked out later.** The spine's 5b heading line and the runbook's 5b row are amended under `DR-137`, as a matter of order, not prohibition.


### DEC-531 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 6 (DQ-21)
**The question, in plain words:** Who handles a robot's death at Casey, where canon sites no faith? Does canon's line that robot death is handled by religion and community rather than by a professional trade (robot-physiology file L174) bind such a city, and may a city's ULM write any of it now? (PROVISIONAL)
**The facts:** That line sits beside a named faith's doctrines (physiology L172-175). At Casey no faith is sited, religion and holidays come after the CST (contract L415, RF-6), and the mortuary question is reserved (RF-13). Casey's own lines say nothing about who handles a death (`04_Phase_06_Meaning.md` L409-413).
**Options:** (a) It binds every city: where no faith is sited, community handles robot death. (b) It describes only places where a faith is present; elsewhere the handler is unwritten. (c) Hold the question until the step after the CST, beside religion. (d) Write its community structure now (who is called, who keeps the memory), never a mechanism or a rite. (e) Leave it with the reserved mortuary question and answer both together.
**Recommendation:** (e), PROVISIONAL (reader B; A moved to it in Round 3; C concurred). The handler and the disposal are parts of one reserved question.
**What is waiting on it / what was done provisionally:** P6-10 states the line as national canon and asserts no handler at Casey.
**Answer (developer):** (e), as recommended: who handles a robot's death at Casey is answered together with the reserved mortuary question (RF-13), both after the CST, beside religion. P6-10 stands as written.

### DEC-532 · ANSWERED IN PART 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 6 (DQ-22; a national question, low priority)
**The question, in plain words:** Can cold kill a robot? Canon defines a robot's death as irreversible damage to the gel brain or the energy-source architecture, with no way of bringing her back online (robot-physiology file L73); the cold file says that past a charge threshold a robot cannot recover on her own. Is a robot caught past that threshold and not reached dead, or only stranded until someone warms and charges her? (PROVISIONAL)
**The facts:** Phase 4 carries the cold file's threshold and calls the death spiral a far edge, not a daily threat, at Casey's temperatures (`04_Phase_04_Ordinary_Life.md` L154, L234). No admitted line settles it (`04_Phase_06_Meaning.md` L415-419).
**Options:** (a) Dead, if nobody reaches her. (b) Not dead: recoverable by others' warmth and charge, so a robot caught in the cold is a rescue, not a death. (c) Leave it open, to be ruled once for every city.
**Recommendation:** (c), PROVISIONAL (reader C; A and B in Round 3). A city's pass should not define national physiology (as with DEC-523 and DEC-526).
**What is waiting on it / what was done provisionally:** No robot death from cold is written; robot death at Casey appears only as canon's incidents (P6-10, P6-14, P6-18).
**Answer (developer):** "to the extent that cold could cause such a degradation in structural integrity of a robot's gel brain and/or energy cell (i.e., heart), yes. We might need to do further research into what sort of science/physics is involved. My leaning is "probably"." **Recorded:** cold kills a robot where it degrades the gel brain or the energy cell (her heart) past recovery, which is canon's definition of death; the developer's leaning is that it probably can. **Still open:** the science of how cold damages a gel brain and an energy cell, and at what point, needs research before any city writes a cold death as a mechanism. Until then a pass may write that a robot left in the cold can die, never how or at what temperature. **Bearing from the *Streetside Harmonies* notes** (Earth, 2149; offered, not ruled): a robot that runs out of siligel slows and has to be carried, "At one point, they do run out, and Craig and Martin need to carry her" (`structure/main story/Save the Cat.md` L49), and comes back slowly when fed, "Takes a few moments {i.e., minutes} to process the substance/material; she gradually becomes more animated" (transcribed Chapter 23.md L20); a robot left inert by an electrical shock is revived by a mechanic over days, "After much trouble, the mechanic revives her." (`structure/character arcs/Valerie.md` L170). So running dry is a rescue, and damage short of irreversible is a repair; death is only where the damage is past recovery, which is where the developer's "probably" sits for cold.


### DEC-533 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 7 (DQ-23; a national question)
**The question, in plain words:** May a city's ULM Phase 7 write the form of its local government at its height (a council, an administration, its holders by role, its succession), when the only line is the founding treaty draft's permission (settlements progress from their founding administration by their own process, II.4; communities may organize local councils, I.4) and no admitted line states the form? (PROVISIONAL)
**The facts:** Nothing admitted says what Casey's government is at its height. Writing one would invent an institution; leaving it blank leaves the phase's order without its formal top (`04_Phase_07_Order.md` L547-551).
**Options:** (a) Write only where decisions fall and who is present when they do, leaving form and holders open. (b) Write a local council at the height for Casey, by role only, as a Proposed finding on the treaty draft. (c) A national ruling, once, on the form of a Tepenian city's government in the Second Interwar, each city then writing only its own form of it.
**Recommendation:** (c) nationally, with (a) as Casey's interim, PROVISIONAL (readers A and B; C in Round 3). A city's pass should not define a national institution.
**What is waiting on it / what was done provisionally:** Casey's Phase 7 runs on (a) (P7-12, P7-13, P7-39).
**Answer (developer):** Casey's interim (a) as recommended, and the national question deferred: "the governmental/justice-oriented sections will need to wait until after the DCI is fully complete, because these cities are populated by people from real cultures. Therefore, we'll need to study and analyze how those real cultures work, and what sorts of new settings they would result in. This includes seeking out and collecting information, studying and analyzing how all these various real cultures consider and understand the concept of justice. Different parts of the Tepenian Federation understand, approach, and handle concepts such as Justice, Law, Law Enforcement, etc. in different ways, depending on where their progenitor cultures come from, and how they understood those concepts. Therefore, it's necessary to measure and understand how those various cultures approach these various concepts, and that will have to wait until the data is in from the DCI." **Recorded:** (1) **No pass writes a city's government form or its justice, law or law enforcement until the DCI is fully complete.** (2) **These are not one national form** (option (c) as worded is set aside): different parts of the Federation understand and handle justice, law and law enforcement differently, according to how their progenitor cultures understood those concepts, and the real cultures' approaches must be studied first, through the DCI. (3) Until then a pass writes only where decisions fall and who is present when they do, form and holders open, as Casey's Phase 7 does. This agrees with the 2026-09-16 ruling that per-area criminal justice is undeveloped corpus-wide. **Further answer (developer, 2026-11-15):** "once the overall data has been established on how each general region understands such concepts as Law, Justice, Law Enforcement, and so on, and once their regional approaches to Law Enforcement, Government, and so on have been established, then that will form the basis of how the entire nation, the entire Tepenian Federation, approaches a national framework of law, government, and justice." **Recorded:** (4) **the order runs from the regions up:** first the DCI's data on how each general region understands law, justice and law enforcement; then each region's approach to law enforcement, government and the rest; and only then, built on those, the Federation's national framework of law, government and justice. No national framework is written before the regional ones.

### DEC-534 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 7 (DQ-24; low priority)
**The question, in plain words:** What form does Casey's winter store take: a city common store, the parent's yearly program, household stores with a common reserve, or left open? (PROVISIONAL)
**The facts:** Every rule about the winter store (who sets its reckoning, who may draw, whether strangers share it, whether the flow is cut first) depends on who holds it, and no admitted line says (`04_Phase_07_Order.md` L553-557). Real sea-supplied places do it both ways.
**Options:** (a) A city common store, kept by Casey's own governing layer. (b) The parent's yearly program, distributed locally. (c) Household stores with a common reserve for those who cannot lay in. (d) Leave it open until Step 5 reads Casey's culture material.
**Recommendation:** (d), PROVISIONAL (reader C; A and B concurred). It claims least, and Step 5 may show what the culture material already writes.
**What is waiting on it / what was done provisionally:** P7-6, P7-7 and P7-28 are written open on it.
**Answer (developer):** (d), as recommended: the form of Casey's winter store is left open until Step 5 reads Casey's culture material. A store kept by a governing layer touches government form, which waits for the DCI (DEC-533's answer).

### DEC-535 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 7 (DQ-25; a national question, low priority)
**The question, in plain words:** The industry model's per-city baseline file explains its legal-and-justice staffing rate by an active three-tier justice system with exile and supervised-labor sentencing (`Division_of_Industry/09_Per_City_Baseline_Run.md` L34-35). Does that reasoning carry any standing as justice canon, given the ruling that per-area criminal justice is undeveloped corpus-wide? (PROVISIONAL)
**The facts:** The line justifies a staffing figure in a folder ruled reliable; a later pass could read it as a ruling that exile is a Tepenian sentence. At Casey, exile in the shut half is, for a robot, permanent injury (`04_Phase_07_Order.md` L559-563).
**Options:** (a) The model's reasoning only, no standing as justice canon. (b) A national canon statement that each area later adapts. (c) Leave it for the national justice design.
**Recommendation:** (a), PROVISIONAL (readers B and C; A concurred). It keeps the 2026-09-16 ruling intact.
**What is waiting on it / what was done provisionally:** P7-36 prices exile only as the model names it and designs nothing.
**Answer (developer):** (a), as recommended: the industry file's justice reasoning has no standing as justice canon. Justice itself waits for the DCI (see DEC-533's answer).

### DEC-536 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 8 (DQ-26; a national question, low priority)
**The question, in plain words:** Robot food in a Tepenian city: is siligel (and coolant) shipped into each city's seasonal stock, or made in each city? And may a city pass write siligel's three proposed classes (a daily meal, a periodic maintenance grade, a rare repair grade) as conditional structure? (PROVISIONAL)
**The facts:** Canon rules only that siligel's first function is energy and its second self-repair, and fixes its form (`Robot_Biology_and_Culture/Siligel_Composition_Research.md` L12-14). Whether it is manufactured or mined is open (L441-444), and the three classes are the research file's proposal, offered for a ruling (L424-428). At Casey both halves matter: whether the robot majority's food has a fill season and a draw-down like the human kitchen, so that a late sea opening is felt first by the robot half; and whether a seven-month closure falls on a maintenance grade the file calls a chokepoint (L322) (`04_Phase_08_Making.md` L550-554).
**Options:** (a) Shipped into each city's stock in the travel season. (b) Made in each city from local feedstock. (c) Both, by kind, once the classes are ruled. (d) A national ruling first on siligel's composition, supply and classes (the file's open items 1 to 3), each city then writing only its access pattern.
**Recommendation:** (d), PROVISIONAL (readers A and B; C in Round 3). A city pass should not settle a national physiology question (the same ground as DEC-523, DEC-526 and DEC-532).
**What is waiting on it / what was done provisionally:** P8-8 and P8-10 write supply and the classes as conditional and as a proposal; nothing in Casey's pass rests on either.
**Answer (developer):** "Siligel needs to be synthesized from raw minerals that are acquired via mining operations, so only a few cities have the geographical proximity to sources (if not exposed rock, then, at the very least, ice that's comparatively subject to melting/drilling in order to reach quarries where those raw materials are found. Once they are, they can be shipped to cities with processing infrastructure (purification, etc) to be able to turn those raw materials into siligel, and those cities with processing infrastructure perhaps may not necessarily be everywhere". **Recorded, a three-link chain:** (1) siligel is synthesized from raw minerals got by mining, so only a few cities lie near sources (exposed rock, or ice thin or workable enough to melt or drill through to the quarries); (2) the raw minerals are shipped to cities with processing infrastructure (purification and so on), which are not necessarily everywhere; (3) the finished siligel then reaches the other cities. This settles the siligel research file's open item on manufactured or mined (`Siligel_Composition_Research.md` L441-444): both, mined and then synthesized. **Not answered:** the three proposed classes (L424-428), and coolant. **Not decided here:** which cities mine or process; that is each city's own question, answered from its own geography, never by a pass assigning it. For a city that neither mines nor processes, siligel is shipped in, so it rides the same supply season as everything else shipped in. **Follow-up, 2026-11-15.** The *Streetside Harmonies* notes show three separate inputs (siligel to eat, coolant to drink, electric charge), siligel burned faster with effort and strain, and a robot making heat on purpose by burning it harder ("V begins overclocking", "burning hotter", transcribed Chapter 24.md L13). Asked whether that is canon, the developer answered: "Anytime any sort of chemical process takes place, the process is either exothermic or endothermic, because it can't be nothing, because that would violate the Law of Conservation of Energy. And the way that I see it in my head, in this particular case, the robot's internal processing of siligel is exothermic." **Recorded:** a robot's processing of siligel releases heat. A robot makes heat by processing siligel, and more heat by processing more, so warmth costs siligel. In a cold place, keeping warm (herself, or someone else) raises a robot's siligel use. **Not separately ruled:** coolant as a drink and electric charge as a separate input, which stand in the novel notes and in the robot-physiology file as far as each states them.

### DEC-537 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 9 (DQ-27; a national question, low priority)
**The question, in plain words:** Canon gives robots a long-life tier (over a thousand years, against 200 to 500 with ordinary upkeep) when a robot has a genuine, ongoing relationship with someone skilled in robot upkeep whom she can "consult and rely on ... regularly, not as a one-off favor" (Robot Universals, ch. 4 L49-53). Does that person have to be reachable in person, or does a relationship held at a distance count? (PROVISIONAL)
**The facts:** At Casey the sea is shut about seven months and no airport is sited. If the relationship must be in person, a Casey robot's long life depends on a maintainer who winters at Casey; if advice at a distance counts, the subnet's network could carry it (`04_Phase_09_Populations.md` L523-526).
**Options:** (a) In person: the tier needs hands on the body. (b) At a distance counts. (c) Both, by kind of upkeep: advice at a distance, repair in person. (d) Leave it open nationally.
**Recommendation:** (d), PROVISIONAL, with (c) as the reading that claims least if a reading is needed (reader A; B and C in Round 3). A city pass should not define national physiology (the same ground as DEC-523, DEC-526, DEC-532 and DEC-536).
**What is waiting on it / what was done provisionally:** P9-7 and P9-9 are written conditional; nothing else rests on them.
**Answer (developer):** "It's not really necessary to be with one specific person, one specific robot mechanic, although it certainly can be. The robot just needs to be able to have access to somebody who understands how to work on robots to achieve those longer lifespans. So theoretically, it is perfectly reasonably possible for a robot to have relationships with multiple knowledgeable engineers, people who are skilled in robot upkeep. It doesn't always have to be with the same person, although it certainly can be." **Recorded:** the long-life tier needs ongoing access to someone who knows how to work on robots, not one particular person; a robot may rely on several skilled engineers over time, or on one. **Orchestrator's reading, to be corrected if wrong:** the question asked was in person or at a distance, and the answer turns on access rather than on one person; at a place shut for part of the year, what counts is whether someone skilled in robot upkeep is reachable there through the shut season, whoever that is.

### DEC-538 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 9 (DQ-28; low priority; may fold into the national robot-ancestry rule)
**The question, in plain words:** `DR-136` item 10 says "a robot built there records the city's own distribution (the spec's copied human proportions)" (rulings L1994). For Casey, does each Casey-built robot carry the city's whole 42-way mixture as her ancestry, or do Casey's robot rows carry the mixture in aggregate, with each robot on one origin row like a human? (PROVISIONAL)
**The facts:** Casey has no majority community, so "a row states the predominant one" (L1994) has nothing to state there. The spec's robot rows copy the human proportions ("Robot figures apply the same proportions as the human population.", spec L74). Readers A and B took the individual reading without noticing the ambiguity; reader C raised it (`04_Phase_09_Populations.md` L528-531).
**Options:** (a) Individual: each Casey-built robot's ancestry is the city's distribution. (b) Aggregate: the rows carry the distribution and each robot has one row. (c) Leave it for the national robot-ancestry rule.
**Recommendation:** (a), PROVISIONAL (reader C; A and B in Round 3). It is the ruling's plain text, and (b) would assign a single origin where the ruling says none predominates.
**What is waiting on it / what was done provisionally:** P9-4 and the axis test's leg 4 are written conditional on (a).
**Answer (developer):** "She certainly can carry the whole mix, but if a robot develops her personality and understanding within the context of a particular ethnic and/or cultural group, then she would be from that particular identity." **Recorded:** (a) holds as the default: a Casey-built robot can carry the city's whole mix as her ancestry. But where a robot develops her personality and understanding inside one particular ethnic or cultural group, she is from that group's identity. So the mix is the default for a robot formed in Casey at large, and a robot formed within one group at Casey belongs to that group. This is the same principle as `DR-136` item 10, applied to the individual robot rather than to a row.

### DEC-539 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 10 (DQ-29; Casey's Planet + Element, `DR-8`, `DR-8a`)
**The question, in plain words:** What are Casey's Planet and Element? (PROVISIONAL)
**The facts:** The assignments file's row for Casey carries Mars, with the element held open for this phase; an earlier draft of the row carried Fire. After reading Casey's own character in Phases 2 to 9, none of the three readers reserved Mars, so by the method's rule (`M-268`) Mars cannot be confirmed here. All three reserved the Asteroid Belt, and all three chose Air. Fire got two opposite readings (one reader against, one for, one reserving it) (`04_Phase_10_Catalog.md` L430, P10-47).
**Options:** Planet: (a) confirm Mars; (b) leave it open, with the Asteroid Belt, the Sun and Earth reserved; (c) the Asteroid Belt; (d) the Sun; (e) Earth. Element: (a) Air; (b) Water; (c) Fire; (d) Earth; (e) leave it pending.
**Recommendation:** Planet (b), open, with the Asteroid Belt as the lead alternative; if it is to be decided now, (c) the Asteroid Belt. Element (a), Air. PROVISIONAL (all three readers).
**What is waiting on it / what was done provisionally:** the planet is open and the element pending until answered; nothing in Phases 2 to 10 rests on either. Step 5 is the backstop.
**Answer (developer):** Planet: "We can go with the Asteroid Belt as settled". **Casey's Planet is the Asteroid Belt.** Element: the developer asked for the arguments for and against both Air and Fire (given in the session of 2026-11-15: Air read as the shelter of shared stillness inside, not as the wind; Fire's best fits were Casey's danger and its winter clock rather than its character), then answered "for Casey's Robot Elemental, I would say Air, yeah." **Casey's Planet + Element: the Asteroid Belt + Air.** The incumbent Mars and the earlier draft's Fire are superseded. `City_Symbol_Assignments.md` updated under `DR-137` (Casey's row, in place).

### DEC-540 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 10 (DQ-30)
**The question, in plain words:** Every name in Casey's catalog is a descriptive English working name (the warm room at the node, and so on). How should the catalog's places and things be named until the national-language naming work? (PROVISIONAL)
**The facts:** The place's own names belong to the national language (AMD-1) and to the developer. Any name or bearing for the coastal-chain highway leg also waits on DEC-527's bearing question (DQ-18).
**Options:** (a) Keep the descriptive English working names as placeholders until the naming work. (b) Leave every place unnamed until then. (c) Name them now in the national language. (d) Use real-world place names from admitted lines.
**Recommendation:** (a), PROVISIONAL (all three readers). Real place names stay coordinates only.
**What is waiting on it / what was done provisionally:** (a).
**Answer (developer):** (a), as recommended: the descriptive English working names are kept as placeholders, each flagged, until the national-language naming work.

### DEC-541 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 10 (DQ-31)
**The question, in plain words:** Two readers independently found, in one inspiration pick, a room at the road's stopping places that holds the belongings and letters of people who are away. A third found a house of small heated rooms near the harbor where people held by the ice spend the winter. Should either become a Casey place? (PROVISIONAL)
**The facts:** The held-things room rests on a search summary only. The berth house rests on a fetched, confirmed source, and the need for a winter's heated berth for the held already stands in Phase 2 (`04_Phase_10_Catalog.md` P10-14, P10-31).
**Options:** (a) Admit the held-things room as a Casey place and role (no lending, cashing or community ownership), leaving whether its keeping is a duty, a trade or a commons for Step 5; keep the berth house a candidate. (b) Keep both as candidates for Step 5's check. (c) Drop the held-things room; keep only the need for berths. (d) Site both now.
**Recommendation:** (a), PROVISIONAL (reader C; A moved to it in Round 3).
**What is waiting on it / what was done provisionally:** both written as conditional until answered.
**Answer (developer):** (a), as recommended: the held-things room at the road's stopping places is admitted as a Casey place and role (no lending, cashing or community ownership); whether its keeping is a duty, a trade or a commons is left for Step 5. The berth house stays a candidate. The Phase 10 file is not edited outside its run; Step 5 carries the change from conditional to admitted.

### DEC-542 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 10 (DQ-32; low priority)
**The question, in plain words:** The catalog lists an ice foot (a shelf of sea ice frozen to the shore) and a tide crack (the break where the moving sea ice meets the fixed ice) as landmarks of Casey's shore. They rest on general polar physics and one example crack, not on any line about Casey's own shore. Keep them? (PROVISIONAL)
**Options:** (a) Admit them as conditional landmarks. (b) Drop them. (c) Hold them for research into the site's shore, without using the real station's records (`DR-19`).
**Recommendation:** (a), PROVISIONAL (reader A), with the crack's width written as one example's.
**What is waiting on it / what was done provisionally:** (a) (`04_Phase_10_Catalog.md` P10-3).
**Answer (developer):** (a), as recommended: the ice foot and the tide crack are kept as conditional landmarks, the crack's width written as one example's.

### DEC-543 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 10 (DQ-33; low priority)
**The question, in plain words:** Should the enclosed links between Casey's raised buildings be catalogued as the places where drifting snow collects? (PROVISIONAL)
**The facts:** Phase 4 kept raised, linked buildings as a comparable only; one search summary says drift collects on the downwind side of such links, and the study that was fetched does not cover them.
**Options:** (a) Leave them conditional. (b) Admit them as where drift collects.
**Recommendation:** (a), PROVISIONAL (reader C).
**What is waiting on it / what was done provisionally:** (a).
**Answer (developer):** (a), as recommended: the enclosed links between raised buildings stay conditional as places where drift collects.

### DEC-544 · ANSWERED 2026-11-15 · 2026-11-15 · Casey ULM run, Phase 10 (DQ-34)
**The question, in plain words:** The Frame forbids any role built from the spec's two placeholder residents, "such as the dispatcher" (`00_Frame.md` L252). Phase 7, separately, writes "a dispatcher counting the last loads" as part of a trade (`04_Phase_07_Order.md` L206). Is the word "dispatcher" barred everywhere, or only when the role comes from the placeholders? (PROVISIONAL)
**Options:** (a) Write the function only (the one counting the last loads), never the title. (b) The title is allowed where it comes from the trade, not from the placeholders.
**Recommendation:** (a), PROVISIONAL, the reading that claims least (all three readers after Round 3).
**What is waiting on it / what was done provisionally:** (a), as written at P10-40.
**Answer (developer):** (a), as recommended: write the function (the one counting the last loads), never the title "dispatcher".

### DEC-545 · OPEN · 2026-11-16 · Casey ULM run, Step 5 (DQ-35; low priority)
**The question, in plain words:** Casey's spec gives a southeasterly katabatic wind at 7-10 m/s (spec L98). Step 3's sourced site record has gales mostly from the east and a mean near 6.9 m/s (S3-18). Both are wind off the ice from the landward side; only the exact bearing and the mean differ, and no phase rests on either.
**Options:** (a) keep spec L98 as written; (b) correct spec L98 to east to southeast with the site mean; (c) write both with their objects (a southeast katabatic as the prevailing flow, gales mostly from the east, the mean as a range with the site's figure inside it), the exact bearing left open until a research session checks the site record; (d) leave it open.
**Recommendation:** (c), PROVISIONAL (readers A and C; B raised none).
**What is waiting on it / what was done provisionally:** nothing in Step 5 depends on the exact bearing; written as (c) (`05_Reconciliation.md`, DQ-35).

### DEC-546 · OPEN · 2026-11-16 · Casey ULM run, Step 5 (DQ-36)
**The question, in plain words:** Flight mode saves siligel and keeps a robot aware, in slow motion; processing siligel gives heat (`DR-137` items 3 and 5). If saving siligel means processing less, flight mode may make a robot colder, so in Casey's cold it could be as dangerous outdoors as resting. Does flight mode lower a robot's own warmth, and does it count as rest?
**Options:** (a) it lowers her warmth and counts as rest: an indoor measure in the cold; (b) it keeps her warmth, or counts as standing awake: safe when dressed; (c) leave it open until the cold-damage research, and write only that flight mode saves siligel.
**Recommendation:** (c), PROVISIONAL (all three readers after Round 3): a city pass should not define national physiology.
**What is waiting on it / what was done provisionally:** flight mode is written only inside heat at Casey (S5-8, conditional on (a)).

### DEC-547 · OPEN · 2026-11-16 · Casey ULM run, Step 5 stage B (DQ-37)
**The question, in plain words:** Casey's culture file names a hospitality economy and lodging that serve travelers fast (culture L83, L109, L171). The pass has a warm night owed to whoever is here, with no named debtor, and a last resort that is neither rented nor refused (P6-2; P10-13). Step 5 finds both true at different scales. How do the two relate? The held-things room and the winter store take their form from the answer. No price may be written either way (`DR-3`).
**Options:** (a) two layers: a public lodging trade for travelers who move on, and beneath it an owed floor of heated rest for whoever is here when the trade cannot serve (the held, a blow, the last resort), no price at either layer; (b) one layer: all heated rest at Casey is owed, and the hospitality economy is work the city does, not a sold service; (c) leave it open for the CST (what the trade looks like) and the DCI (any terms), recording both readings.
**Recommendation:** (a), as structure only, no price, PROVISIONAL (readers B and C; A in Round 3).
**What is waiting on it / what was done provisionally:** written as (c); P6-2 stands either way.

### DEC-548 · OPEN · 2026-11-16 · Casey ULM run, Step 5 stage B (DQ-38)
**The question, in plain words:** Casey's personality read (Feeling, Assertive, Positive Outlook) rests only on a scene from a vision session (`City_Enneagram_Personalities/Mirny_Subnet/Casey.md` L7). Vision material is not an input to any ULM step (`DR-10`), so the read cannot be checked against the pass, and two of its three axes run against the character the pass established. `DR-10` says when vision material is read, not whether this read is kept.
**Options:** (a) keep it as written, outside the ULM, and revisit after the run with the vision notes; (b) re-derive Casey's personality read from the finished pass at the character stage, with the vision notes read beside it then; (c) withdraw it now.
**Recommendation:** (b), PROVISIONAL (reader A; B and C in Round 3).
**What is waiting on it / what was done provisionally:** kept as (a) for now; nothing in the pass rests on it.


### DEC-549 · OPEN · 2026-11-16 · Casey ULM run, Step 6 (DQ-39)
*From `06_Differentiation.md` L244, copied verbatim:*
**DQ-39 · Section 4 of the city differentiation table has a third column with no title. What should it ask?** *Low priority; the instrument's owner.* *Merges S6A-DQ-1, S6B-DQ-101, S6C-DQ-201.*
- *In plain words:* the Phase 4 section's header has a third column with no name (table L85), and no line says what goes in it. Casey's cell there is left empty, with its reason; every later city will meet the same blank.
- *Options:* (a) leave it untitled, and every city writes a null; (b) name it for each axis's weak legs, which every city's peer-free test already writes (C); (c) name it for a second axis from the section's own sentence, such as what ends the day beside what opens it, or whom the day's rhythm fails (A; Phase 4 writes the latter at P4-46); (d) name it for Phase 4's common conditions, its own short list (P4-47) (B); (e) remove the column.
- **Recommended (PROVISIONAL): interim (a), the null as written (all three readers).** The readers split on the title and no lean is taken here: after Round 3, A favors an axis-shaped title, (c), noting that weak legs and common conditions are content; B leans to (b); C leans to (d), since weak legs are a test result, not an answer.

### DEC-550 · OPEN · 2026-11-16 · Casey ULM run, Step 6 (DQ-40)
*From `06_Differentiation.md` L249, copied verbatim:*
**DQ-40 · In the Phase 2 section, is the second column the mode-mix's words again, or what organizes the mix?** *Low priority.* *From S6C-DQ-202.*
- *In plain words:* the section defines its axis as the mode-mix in three or four words (table L58), then gives two columns, the mode-mix and an organizing axis (L60), with no instruction for the second. Casey's row puts the three words in the first and Phase 2's own sorting line (by season and by heat, not by stock) in the second.
- *Options:* (a) as written: the mode-mix, then what sorts it; (b) the three words in both cells; (c) the second cell for the composition condition beside the axis (at Casey, plurality, P2-38's note).
- **Recommended (PROVISIONAL): (a)**, interim (a). All three readers read the column this way independently; C withdrew the question in Round 3 for that reason, and A and B would carry it as low priority (split 19).

### DEC-551 · OPEN · 2026-11-16 · Casey ULM run, Step 6 (DQ-41)
*From `06_Differentiation.md` L254, copied verbatim:*
**DQ-41 · Where does a city's strongest finding, with its legs and the read-last result on its named leg, go in the differentiation instrument?** *Low priority.* *From S6B-DQ-102.*
- *In plain words:* Step 5 asks Step 6 to carry the strongest finding with its legs and the read-last result (`05_Reconciliation` L533, L880), but the table has no column for them. They are written in this file's §5 and §10 grounds and S6-8.
- *Options:* (a) in the pass only, for the terminal check to read; (b) a new column in Section 1, the strongest finding and its weakest leg, for every city, with the runbook changed in the same commit; (c) inside the Shape cell.
- **Recommended (PROVISIONAL): (a)**, interim (a): it keeps cells as axes (runbook L2928) and changes no instrument partway through the corpus; (c) would put content in a cell. B withdrew the question in Round 3, since the grounds discharge Step 5's rows; A and C would carry it (split 19).

### DEC-552 · OPEN · 2026-11-16 · Casey ULM run, Step 7 (DQ-42)
*From `07_QA_Gates.md` L1294, copied verbatim:*
**DQ-42 · When a member of Casey leaves for years and comes back, is she still someone who has wintered?** *(From Gate 9; S7-6.)*
- *In plain words:* at Casey the category that matters more than body or origin is having been held and warmed through a shut half (P9-24); you become a member by wintering (P5-27). The pass writes how that standing is gained, and never whether it can lapse or how it is regained. A young resident who goes away to train in nursing and comes back in a later open season (P4-25 →1) shows the gap.
- *Options:* (a) once wintered, always: the standing never lapses, and a returner is a member on arrival; (b) it lapses after a full shut half away, and a returner is a newcomer until she winters again; (c) it does not lapse but fades in practice: a returner is a member on paper and is taught again by whoever was there last April (as S5-AM-8 →3 writes of newcomers); (d) leave it unwritten until the character work and the CST.
- **Recommended (PROVISIONAL): (c).** It keeps P9-24 as written, claims no rule (no rule can be written before the DCI, `DR-137` item 11), and fits Casey's own lines, where knowledge of the shut half is held by people and taught by wintering (P7-23; S5-AM-8). *Interim:* (d); carried to Step 8's panel first; nothing in the pass rests on either side.
- *From* A (S7A-DQ-1), with B's route-back framing (S7B-103) and C's losing half (S7C-HF-202).

### DEC-553 · OPEN · 2026-11-16 · Casey ULM run, Step 7 (DQ-43)
*From `07_QA_Gates.md` L1300, copied verbatim:*
**DQ-43 · Does the Arcanet carry the state of the roads and the weather between places through the shut half?** *(From Gate 5; S7-E-22; `05` L884, S5-CK-57.)*
- *In plain words:* canon gives the nation its own self-sufficient network for its whole isolated population (`Arcanet.md` L7-8, L16-17), and Casey reaches it through a hub elsewhere (P5-20 →1). The pass writes that in winter, when no traveler comes down the inland road, Casey loses that half of its forecast, and that its winter knowledge of its own roads is borrowed nightly from strangers. If the network carries road and weather reports, travelers are a second channel, not the only one.
- *Options:* (a) yes: road and weather state reach Casey over the network all year, and travelers add what data cannot (the feel of the road, what they saw); (b) no, or only irregularly: in the shut half the road's state still arrives mostly with people; (c) leave it open as a national question, with the corrected wording of S7-E-22 until it is answered.
- **Recommended (PROVISIONAL): (c).** It is a national fact about the network that a city pass should not decide, and the corrected wording holds under either answer. *Interim:* (c).
- *From* C (S7C-DQ-201); A and B concur in Round 3.

### DEC-554 · OPEN · 2026-11-16 · Casey ULM run, Step 7 (DQ-44)
*From `07_QA_Gates.md` L1306, copied verbatim:*
**DQ-44 · Does the rule to write the function, never the title, reach the harbor foreman?** *(From Gate C; low priority.)*
- *In plain words:* `DR-137` item 12 rules on the dispatcher by name: write the function, never the title (rulings L2003). The catalog also writes a harbor foreman choosing in March whose cargo goes into the last open water (P10-40, `04_Phase_10` L339; P10-15 →3, L213; P10-42, L354). That title is not among the placeholder residents the Frame names (Frame L252), and item 11 allows where a decision falls and who is present; a title still suggests an office.
- *Options:* (a) extend the rule: write the one choosing whose cargo goes into the last open water, never the title; (b) keep harbor foreman as a work position, never an office; (c) extend the rule to every role title the pass writes.
- **Recommended (PROVISIONAL): (a)**, the reading that claims least and the form the pass already chose for the dispatcher (DQ-34; S5-16). *Interim:* (a) at Step 8.
- *From* B (S7B-DQ-101); A and C concur in Round 3.

### DEC-555 · OPEN · 2026-11-16 · Casey ULM run, Step 8 (DQ-45)
*From `08_Review_Panel.md` L282, copied verbatim:*
**DQ-45 · Can a line from Casey's own culture material, read last as a check at tier 3, be the line that grounds an `unmet`?** *(Low priority; a method question; from B's S8B-DQ-101.)*
- *In plain words:* an `unmet` refusal needs a line showing that the place itself knowingly protects the thing, and the pass's own wording cannot be that line (runbook L2999). In this panel one refusal was first grounded on the culture file, which Step 5 read last as a check and recorded without adopting (culture L73, L75, as `05` L794, L737 record them). The merge has written that refusal `declined` (S8-O-22), so no disposition here depends on the answer.
- *Options:* (a) yes, at its tier: a read-last line may ground an `unmet`, reported with its standing; (b) no: only admitted inputs or rulings can ground one; (c) yes, only where the read-last line agrees with a refusal the pass already makes on its own grounds, never as the refusal's only ground.
- **Recommended (PROVISIONAL): (b)**, on the rule's own words, an admitted or ruled line (A and C in Round 3). *Interim:* (b); the `unmet` count stays 1.
- *From* B (S8B-DQ-101, which recommended (c) in Round 1 and in Round 3 withdrew it as a question for this run, handing it on as a method note); A would carry it as a question; C finds it acceptable as one and answered by the rule (split 15). Carried as a question so that the merge does not settle a method question itself.

### DEC-556 · OPEN · 2026-11-16 · Casey ULM run, Step 9 (DQ-46)
*From `09_Record.md` L514, copied verbatim:*
**DQ-46 · Casey's Section 7 row in the city table was inserted before Step 7 found its tier name non-canon. Correct the one cell now, or leave it with the erratum recorded?** *(Low priority. S9-2, S9-8; M-324. From S9A-DQ-1, S9B-DQ-101, S9C-DQ-201.)*
- *In plain words:* Step 6 put Casey's ten rows into the shared table at 07:48. At 09:02 Step 7 found that Step 6's Section 7 cell calls English the crossing tier, where canon's term is the supporting tier, used at Casey as a crossing language, and asked for the fix before the row went in (`07_QA_Gates.md` L1170). The row was already in (`09.5_Log.md` L68-69). The Step 6 file is a pass file and is not edited (`DR-101`); no reader has read the row as it now stands in the table.
- *Options:* (a) correct the one cell in Casey's own row by an asserted one-line replacement, at the commit that carries this record, with a second reader, recorded, and the Step 6 file left as written with the erratum beside it; (b) leave the row as inserted, with S7-E-12 as its reading, until the after-run correction (`DR-136` item 9); (c) for later cities, move the insertion after Step 7 (a methodology change that reverses M-298; M-324), and treat Casey under (a) or (b).
- **Recommended (PROVISIONAL): (a), on the developer's word,** since the row is Casey's own, the change touches no other row, and the wrong word would otherwise sit where the terminal check reads (A, C; B first recommended (b) with (c) for the method, and in Round 3 accepted (a)). *Interim:* (b); S7-E-12's reading governs every use of the cell.

### DEC-557 · OPEN · 2026-11-16 · Casey ULM run, Step 9 (DQ-47)
*From `09_Record.md` L519, copied verbatim:*
**DQ-47 · Should Casey's relations to other places go into the table's propagation row, or stay in this record only?** *(Low priority; a method question. S9-3, S9-7; M-325. From S9A-DQ-2, S9B-DQ-102, S9C-DQ-202.)*
- *In plain words:* Step 6 asked for its six relations (the spur city, the subnet, three neighbors, two unrouted ties) to be carried into the table's propagation row, table L30 (`06_Differentiation.md` L229). The runbook's Step 9 asks that they be recorded in the record (L3017). Only Casey's ten rows were written; L30 is as it was. The relations are recorded at S9-5. No reader has read what L30 holds.
- *Options:* (a) write them into table L30 blind, relations only, by role, at the Step 9 commit; (b) keep them in this record only, for the terminal check to collect, and change Step 6's wording; (c) leave it for the terminal differentiation check to decide for all cities at once.
- **Recommended (PROVISIONAL): (b),** the runbook's own wording, and a write to a shared row would be a second blind insertion the inserting step did not make (A, C; B first recommended (a), and in Round 3 accepted (b)). *Interim:* (b).

### DEC-558 · OPEN · 2026-11-16 · Casey ULM run, Step 10 (DQ-48)
*From `10_Readiness_Check.md` L299, copied verbatim:*
**DQ-48 · Item 1a's two lines: who returns their line numbers when Step 10's readers are barred from them, and are they manifested, moved or left?** *(Medium priority: the next run reads both files in full. Merges C's DQ-201 and A's DQ-3; B Snags 5.)*
- *In plain words:* the runbook and the phase spine each carry one line with Relung Panen's old placeholder name. Both predate Casey's run. The readers could count them but not read them, so nobody has said what they are. `06` has no Relung Panen section, so its warm-run check comes back clean. The spine is meant to name no location; unless its line is only a path or a file name, it breaks that rule.
- *Options:* (a) the orchestrator runs `grep -n`, classes each line, bands content for the run's readers, and adds a Relung Panen section to `06` (coordinates and tier); a content line in the spine moves to the worked-examples archive with a bare pointer, on your word; (b) one isolated reader, given only the two lines, classes them (the cold-run form); (c) manifest only, no move; (d) nothing, since the run is warm.
- **Recommended (PROVISIONAL): (a) for a warm run, (b) for a cold one.** It costs one short check and closes a gap `06` cannot see. *Interim:* the orchestrator classes and bands before Relung Panen's runbook read (S10-71); no file is edited without your word.

### DEC-559 · OPEN · 2026-11-16 · Casey ULM run, Step 10 (DQ-49)
*From `10_Readiness_Check.md` L304, copied verbatim:*
**DQ-49 · Casey's run placed one Casey line in the runbook (L469) and one in the spine (L693). Add a `06` row?** *(Low priority. C's DQ-202; A HF-1; B HF-104.)*
- *In plain words:* the 2026-11-15 ruling on the 5b row rewrote one line in each file, and each now names Casey. `06` asks that a worked example a pass adds be listed in the same commit; these were not. Whether either is a Casey finding or only a note of where the rule came from has not been read.
- *Options:* (a) class them; if either is content, add a row to `06`'s Casey section, coordinates and tier only; (b) no row, as provenance; (c) move any content to the archive.
- **Recommended (PROVISIONAL): (a).** *Interim:* classed with item 1a (S10-72); nothing edited.

### DEC-560 · OPEN · 2026-11-16 · Casey ULM run, Step 10 (DQ-50)
*From `10_Readiness_Check.md` L309, copied verbatim:*
**DQ-50 · The T5 test: which later writing counts when asking whether the early Lover-faculty verdict changed the pass?** *(Low priority; a method question. Merges A's DQ-1 and C's DQ-203.)*
- *In plain words:* the tool's condition covers the phases between 6 and 8 (`08b` L235–237). Step 9 widened it to Phases 7–10 and Steps 5–7 (`09` L499). On Phases 6–8, nothing changed. Beyond them, Step 5 used the early line once as a question for its read-last check and adopted nothing (`05` L57, L737), and Step 8's late verdict cites that answer (`08` L208). Phases 9 and 10 were not read by anyone at this step.
- *Options:* (a) the tool's span only: T5 holds for Casey; (b) the wider span, where a check row generated by the early line is not a change: Phases 9–10 must still be compared; (c) the wider span, where any use counts: T5 is falsified for Casey and withdrawn.
- **Recommended (PROVISIONAL): (b)** (A; C and B moved to it in Round 3): it keeps the tool's purpose and lets a later step test the question the early line leaves open. *Interim:* T5 kept on Phases 6–8; the comparison for Phases 9–10 recorded as not done.

### DEC-561 · OPEN · 2026-11-16 · Casey ULM run, Step 10 (DQ-51)
*From `10_Readiness_Check.md` L314, copied verbatim:*
**DQ-51 · Is runbook item 8 met when the observations file sits inside `Test_Runs/` under a named exception?** *(Low priority. A's DQ-2.)*
- *In plain words:* item 8 asks that the shared observations file sit outside every quarantined folder (runbook L3151–3152). It sits in `Test_Runs/`, which each Pre-Trip makes zero-intake with one exception, reading its tail for the next number (Pre-Trip L457). That tail is now Casey's 32 entries.
- *Options:* (a) met by the named exception, kept in every Pre-Trip, with the next number taken by a number-only command; (b) move the file out of `Test_Runs/` (every cited path changes); (c) reword item 8 to allow a named exception.
- **Recommended (PROVISIONAL): (a), with (c) as a later wording fix.** *Interim:* (a), with S10-79.

### DEC-562 · OPEN · 2026-11-16 · Casey ULM run, Step 10 (DQ-52)
*From `10_Readiness_Check.md` L319, copied verbatim:*
**DQ-52 · Should any of Casey's 32 method proposals be ruled on before Relung Panen's Step −1?** *(Low to medium priority. B's DQ-101.)*
- *In plain words:* none of M-321 to M-352 is a rule yet, so Relung Panen's run follows the rules without them. Seven would change how its lists and briefs are built: the list tool drafting another location's files (M-321), re-reading every figure a brief states (M-329), a per-entry full-read line (M-330), giving Step 8 the files the T5 check needs (M-332), carrying rulings that land mid-run (M-339), the station-denial scan inside each phase (M-350), and a number for each single civic facility at Band 5 (M-351).
- *Options:* (a) rule on those seven first; (b) run on the rules as they stand and rule on all 32 later; (c) rule on none now, and let the orchestrator apply, as recorded practice, those that change no rule text (hand path checks, re-reading cited figures).
- **Recommended (PROVISIONAL): (c)**: it changes no rule without your word (runbook L3029–3031) and keeps the schedule; M-321's hand check is already practice (startup L91). *Interim:* (c).

### DEC-563 · OPEN · 2026-11-16 · Casey ULM run, Step 10 item 1a (orchestrator)
**The question, in plain words:** Casey's readiness check found four lines in the required reading that the next run (Relung Panen) reads in full: `00_RUNBOOK.md` L1646 and `03_The_Phase_Spine.md` L483 carry Relung Panen's old placeholder name; `00_RUNBOOK.md` L469 and `03_The_Phase_Spine.md` L693 name Casey (added 2026-11-15 under `DR-137` item 10). The orchestrator classified them (Casey run log CL-55): none carries a conclusion about Relung Panen, so the warm run is not blocked. But L1646 is stale (it says Relung Panen is excluded from the industry run; `DR-71` to `DR-75`, `DR-96` item 5 and `DR-97` gave it its row), L483 is a stale inventory fact (Relung Panen now has an empty concept-art folder), and the spine is a file the layering law says must name no location (L483 and L693 both do; L693's name is my own wording of 2026-11-15).
**Options:** (a) reword the three lines in place: spine L693 drop "from Casey's run" (keep "`DR-137`, 2026-11-15"); spine L483 drop the placeholder clause; runbook L1646 mark the row superseded with the ruling numbers; and add a dated note to `06_Worked_Example_Provenance.md` at its end recording all four lines; (b) only the `06` note, no rewording; (c) leave all as they are.
**Recommendation:** (a), PROVISIONAL; nothing is edited until you say so. Relung Panen's readers are told meanwhile that runbook L1646 is superseded.
**What is waiting on it / what was done provisionally:** the classification is recorded; no methodology file was edited.


## Open since 2026-11-16 (Relung Panen ULM run; every answer below is PROVISIONAL until you give yours)

### DEC-564 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, readiness check (DQ-1)
*From `00.0b_Readiness_Check_2026-11-16.md` L217, copied verbatim:*
- **DQ-1 · `DEC-003` for Relung Panen** (A, B, C). May the inspiration picks, the `Infrastructure/` files and the city-relationship files ground a finding in this pass? **Recommended:** yes, as `DR-136` item 4 answered for one other run; every other folder stays deferred; dependent findings tagged; with the `DEC-003` section's cautions. *(Alternative: settle it once for every city, as `DR-131` item 13 anticipated.)*
- **Answer (2026-11-16, `DR-138`):** Yes, **for every city**: the picks, the `Infrastructure/` files and the city-relationship files may ground findings in every city's pass; other folders stay deferred.

### DEC-565 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, readiness check (DQ-2)
*From `00.0b_Readiness_Check_2026-11-16.md` L218, copied verbatim:*
- **DQ-2 · The treaty draft's standing** (A, B, C). `DR-136` item 11 let one other run's arrival findings "rest on the Falkland Treaty draft's articles at draft standing, each dependent finding tagged [treaty draft] and listed"; that is not recorded for every city, and whether the draft is ever locked is undecided (L1995). **Recommended:** the same for Relung Panen: draft standing, each dependent finding tagged [treaty draft] and listed.
- **Answer (2026-11-16, `DR-138`):** Draft standing, each dependent finding tagged `[treaty draft]` and listed (as recommended).

### DEC-566 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, readiness check (DQ-3)
*From `00.0b_Readiness_Check_2026-11-16.md` L219, copied verbatim:*
- **DQ-3 · The stale sheets** (A, B, C; C's separate "not in the November run" question folded in, as C agreed in Round 3). Lines: Pre-Trip L69, L148, L481 (search cap), L74 (clock), L275 and L281 (Phase 2 rows), L340 and L417 (cold chain; L340 also omits `DR-97`), L419 (airport siting), L584 (port), L587 (founders), L588 (power), and the method ranges in the class (b) table; input status L287, L290, L297; README L38. **Recommended:** no `--write` (it would erase the hand corrections, RC-21) and no in-run edit; Step −1's brief carries the correction list; the run uses the live sources; the sheets are corrected in one pass after the run.
- **Answer (2026-11-16, `DR-138`):** Corrected once, after the run (as recommended).

### DEC-567 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, readiness check (DQ-4)
*From `00.0b_Readiness_Check_2026-11-16.md` L220, copied verbatim:*
- **DQ-4 · The held source edits** (A, B; C agrees in Round 3), only if the `git log` shows `Airports.md`, `Ports.md`, the map notes or the spec's airport, maritime and founding wording unedited since `DR-95`/`DR-96`. **Recommended:** run on the files as they stand; Step −1 lists each conflicting line as superseded by the ruling item that governs it, tagged; the held edits wait for the developer's review; no source file is edited in-run.
- **Orchestrator note, 2026-11-16 (run log RL-05):** the git log re-run with an explicit time shows commit `612fdc4c` (2026-11-03 10:02), *"Apply review files (DR-96): Relung Panen held edits"*, touching the spec, `Airports.md`, `Ports.md` and the input status. The held edits appear to be applied; this question is likely moot. Raw output: `Relung_Panen/.t8_00_git_log_since_1103_0000_raw.txt`.
- **Answer (2026-11-16, `DR-138`):** Closed: settled by the run's own finding (held edits applied 2026-11-03, `612fdc4c`).

### DEC-568 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, readiness check (DQ-5)
*From `00.0b_Readiness_Check_2026-11-16.md` L221, copied verbatim:*
- **DQ-5 · The power figure** (A, C; B records it as a finding), only if Step −1 finds no source line for "about 0.55 GW plus the city". **Recommended:** carry `DR-96` item 4's own words ("about 0.5 GW average" for export food; the plant sized from that share; plant and route open) and cite 0.55 only with its source line.
- **Answer (2026-11-16, `DR-138`):** Closed: settled by the run's own finding (source line spec L260).

### DEC-569 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, readiness check (DQ-6)
*From `00.0b_Readiness_Check_2026-11-16.md` L222, copied verbatim:*
- **DQ-6 · The 71 further candidates** (A; B and C as an orchestrator check first), only if no ruling tiering them is found. **Recommended:** only the 28 tiered picks are admitted picks; the 71 are research material whose admission Step −1 decides; "all 99 picks" on the Step 3 sheet is read as a copy, not a tiering.
- **Answer (2026-11-16, `DR-138`):** Closed: settled by the run's own finding (the 71 tiered 2026-11-03, `48fb475f`).

### DEC-570 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, readiness check (DQ-7)
*From `00.0b_Readiness_Check_2026-11-16.md` L223, copied verbatim:*
- **DQ-7 · Founders' wording** (C). "Indonesia led, Malaysia in support" (Pre-Trip L587) against "Indonesia and Malaysia jointly" (input status L274; startup L101). **Recommended:** the Founding Register row (L65) governs (`DR-19`); Phase 2 reads it and writes its wording only.
- **Answer (2026-11-16, `DR-138`):** Closed: settled by the run's own finding (the Register row L65 governs).

### DEC-571 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, readiness check (DQ-8)
*From `00.0b_Readiness_Check_2026-11-16.md` L224, copied verbatim:*
- **DQ-8 · `DR-125` item 3, "time that is your own"** (raised by C; B wants it filed; A accepts it as a confirmation; C withdrew it in Round 3 — split 3). Worded "so future runs read it one way" but recorded in another city's walkthrough and absent from the startup's Section 4. **Recommended:** carry it as general (standing item 7).
- **Answer (2026-11-16, `DR-138`):** Yes, every city (as recommended).

### DEC-572 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, readiness check (DQ-9)
*From `00.0b_Readiness_Check_2026-11-16.md` L225, copied verbatim:*
- **DQ-9 · `DR-131` item 6, the ice term** (raised by C; A and B in Round 3 file it as a question; C withdrew to "not carried" — split 5). "any ice term is added later as a separate footprint term in a Division of Industry sweep, never inside a city pass" is recorded under another location's item, not for every city; Relung Panen's site has ice cover (input status L259). **Recommended (A's form, the most conservative):** not carried as a rule, but no ice footprint term is written inside this pass until the developer answers.
- **Answer (2026-11-16, `DR-138`):** Yes, every city: no ice footprint term inside any city pass.

### DEC-573 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step −1 (DQ-10)
*From `00.1_Step_MINUS-1_Input_Contract.md` L499, copied verbatim:* The same question as `DEC-564` (the readiness check's DQ-1), restated by Step −1.
- **DQ-10 · `DEC-003` for Relung Panen** (which source folders may ground a finding). Unruled: `DR-131` item 13 (L1949) defers it, "to be settled once for every city when the first new run needs it"; `DR-136` item 4 answered it for one other run only. Options: (a) the 28 tiered inspiration picks, the `Infrastructure/` files and the city-relationship files may ground a finding; every other folder deferred; each dependent finding tagged `[DEC-003 provisional]`; (b) settle `DEC-003` once for every city now; (c) nothing beyond the spec, Register, census and rulings. **Recommended, PROVISIONAL: (a)**, with the readiness check's cautions (L194–198): the 71 candidates excluded until tiered; `Infrastructure/` lines yield to `DR-95`/`DR-96`; the city's own `Research_Logs/` files not covered. (A, B, C; = readiness DQ-1)
- **Answer (2026-11-16, `DR-138`):** Same answer as DEC-564: yes, for every city.

### DEC-574 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step −1 (DQ-11)
*From `00.1_Step_MINUS-1_Input_Contract.md` L500, copied verbatim:*
- **DQ-11 · The band at the threshold.** Census I 1,000,071 against "~1M" (`DR-4` L235); it crossed the line only through `DR-90`'s arithmetic. Options: (a) Band 5 on Census I, the analysis deferred as `DR-4` §4.2 requires; (b) Band 4, treating ~1M as approximate; (c) "at the 4/5 line", both named. **Recommended, PROVISIONAL: (a)** — `DR-4` makes Census I the design figure, and the deferral means little rides on it now. (A, B; C in Round 3)
- **Answer (2026-11-16, `DR-138`):** **At the 4/5 line, both named** (differs from the recommendation).

### DEC-575 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step −1 (DQ-12)
*From `00.1_Step_MINUS-1_Input_Contract.md` L501, copied verbatim:*
- **DQ-12 · Where in the oasis the city stands, for its climate.** Options: (a) the measured −11.2 °C and 4.6 m/s; (b) the central-oasis −9.0 °C and 6.8 m/s; (c) both, stated with their stations, siting open. **Recommended, PROVISIONAL: (c).** Request REQ-4 beside it. (A; B and C as requests)
- **Answer (2026-11-16, `DR-138`):** Both records, each with its station; siting open (as recommended).

### DEC-576 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step −1 (DQ-13)
*From `00.1_Step_MINUS-1_Input_Contract.md` L502, copied verbatim:*
- **DQ-13 · Which composition governs.** Options: (a) the live per-nation table (L57–90; `DR-85`, `DR-93`, `DR-94`), the disagreement recorded, no finding resting on the window method; (b) the developer confirms proximity-first for this city as a standing exception to `DR-19`; (c) recompute under `DR-19`, or review the rows outside the window. **Recommended, PROVISIONAL: (a)**: it changes nothing in-run, and a census recompute waits for the post-ULM census review (`DR-68` L1341). (A, C; B as RF)
- **Answer (2026-11-16, `DR-138`):** The live per-nation table governs (as recommended).

### DEC-577 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step −1 (DQ-14)
*From `00.1_Step_MINUS-1_Input_Contract.md` L503, copied verbatim:*
- **DQ-14 · The founding "why".** `DR-61` L1253 hands it to the pass; `DR-16` (histories after the ULM) and `DR-136` item 6 (the pass captures the height) pull the other way. Options: (a) the pass derives the why as attribute-level reasoning from admitted lines — what the site offered and what the nation needed — `Proposed:`, undated, with no first-wave story; (b) the why waits for the history stage; (c) a dated founding motive. **Recommended, PROVISIONAL: (a)**, because `DR-61` is the later, city-specific ruling; and the why may not rest on national food necessity (SM1-18). (B, C; A's PRODUCED reading is the recommended answer)
- **Answer (2026-11-16, `DR-138`):** **Waits for the history stage; not derived in the pass** (differs from the recommendation).

### DEC-578 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step −1 (DQ-15)
*From `00.1_Step_MINUS-1_Input_Contract.md` L504, copied verbatim:*
- **DQ-15 · Mixed spec lines** (a needed fact and a comparison or stale clause on one line: L124, L144, L146, L158, L204–205, L234, L256, L277–278, L311). Options: (a) DEMOTED, the named clause struck, the struck-clause list carried with the read-spec; (b) excluded whole, the facts requested from their sources (not covered by the provisional `DEC-003` answer). **Recommended, PROVISIONAL: (a)** — (b) loses facts no other admitted line holds, such as the central-oasis wind record and the spur's only length. [Split: B filed this as a question; in Round 3, B offered it as the merge's convention, A kept it a question with this recommendation, and C listed it as B's find to write. The narrower reading, a question answered provisionally, is written.] (B; A, C)
- **Answer (2026-11-16, `DR-138`):** Keep the fact, strike the clause (as recommended).

### DEC-579 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step −1 (DQ-16)
*From `00.1_Step_MINUS-1_Input_Contract.md` L505, copied verbatim:*
- **DQ-16 · How the read-spec folds structural lines.** Options: (a) A's rule: ADMITTED and DEMOTED in; a blank, rule or heading line in only between two admitted content lines; inert content always out; (b) every non-excluded line in; (c) structural lines folded within spans, isolated inert lines out. **Recommended, PROVISIONAL: (a)**, which keeps the stub-file pointers and TBD lines out of later reading lists; the read-spec above uses it. [A marked the method a developer question; B and C adopted A's rule in Round 3.] (A; B, C)
- **Answer (2026-11-16, `DR-138`):** The folding rule as used (as recommended).

### Note · 2026-11-16 · Step −1's updates to DEC-564 to DEC-572
*From `00.1_Step_MINUS-1_Input_Contract.md` L507, copied verbatim (the readiness check's DQ-1 to DQ-9 are DEC-564 to DEC-572):*
**The readiness check's DQ-1 to DQ-9 (its L217–225), carried, with this step's updates:** DQ-1 is DQ-10. DQ-4: the spec part is already applied (SM1-8); only `Airports.md` and `Ports.md` remain (REQ-5). **DQ-5: its condition does not fire** — the 0.55 GW figure's source line is spec L260 (SM1-7). DQ-6: new evidence in the git log (SM1-10; REQ-6). **DQ-7: answered by the Register row itself** (SM1-16). DQ-2, DQ-3, DQ-8 and DQ-9 stand as filed. (A; B and C concur on DQ-5 and DQ-7)

### DEC-580 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 0 (DQ-17)
*From `00_Frame.md` L414–L418, copied verbatim:*
- **DQ-17 · The extent band.** 01 asks for an extent band (L167–170, L563) but defines bands by population only, and no extent scale is on the list.
  - **Options:** (a) state the extent as figures and declare no band number until a scale exists; (b) band the extent by the population its own comfortable capacity holds (3,375,000, spec L120, which falls in Band 5), labeled a reading, with the area beside it; (c) the developer sets a km² scale now.
  - **Recommended, PROVISIONAL: (a), with (b)'s Band 5 recorded beside it as a labeled reading only.** (b) borrows a population scale for an area, and its capacity rests on a 7,500/km² basis not on the list (contract SM1-25). (c) is a method change for every pass.

  *Split named: A recommended (a); B and C recommended (b). In Round 3, B and C each named A's form as the narrower one for the merge, and A accepted Band 5 as a labeled reading.* *(A, B, C)*
- **Answer (2026-11-16, `DR-138`):** Figures only, Band 5 as a labeled reading (as recommended).

### DEC-581 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 0 (DQ-18)
*From `00_Frame.md` L419–L424, copied verbatim:*
- **DQ-18 · The 01 §5.4 per-category declarations at Band 5.** `DR-4` defers the decomposition and the distribution (L234–237), but 01 §5.4 (L541–550) separately requires a Band 4+ pass to label each category.
  - **Options:** (a) no per-category labels: each later phase marks a city-wide statement whose internal variation would matter as deferred by `DR-4` §4.2, and never writes Uniform; (b) full §5.4 labels in every phase, with Patterned only where an admitted line shows the variation; (c) treat §5.4 as suspended with §2.2 and say nothing.
  - **Recommended, PROVISIONAL: (a).** It keeps L550's warning without inventing the internal structure `DR-4` L239–242 says cannot be written before the place is known.
  - **The label wording:** A's wording, "deferred by `DR-4` §4.2" (`.t8_00_Step_0_readerA.md` L347), is written. C's "Delegated — deferred by `DR-4` §4.2" (`.t8_00_Step_0_readerC.md` L347) asserts one of §5.4's three categories, so it claims more.

  *(A, C; B adopts the question in Round 3)*
- **Answer (2026-11-16, `DR-138`):** Written as deferred (as recommended).

### DEC-582 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 0 (DQ-19)
*From `00_Frame.md` L425–L429, copied verbatim:*
- **DQ-19 · The supporting-tier languages.**
  - **Options:** (a) carry the Step 0 datasheet's row (English, Mandarin, Indonesian, Japanese, Korean, Russian, Thai), as `DR-100` item 3 directs, with every language finding tagged to `RF-14`; (b) carry it with Thai held as "at the line, membership provisional" (`.t8_00_Step_0_readerC.md` L350) until the mapping is checked; (c) recount with Malaysia in the Indonesian group, which would add Vietnamese; (d) treat the 12-point rule as inclusive or exclusive for a gap of exactly 12.0; (e) hold the tier open until the mapping is verified (`REQ-21`).
  - **Recommended, PROVISIONAL: (a) with (b)'s flag.** The set stands as the datasheet's, and Thai's membership and Malaysia's group are flagged. Thai's gap is 12.0 on the one-decimal figures and 11.985 only on a reconstructed mapping, so the inclusive question (d) is not settled by arithmetic on the list.

  *Split named: A recommended (a) and held Thai inside on its reconstruction; B recommended (d) inclusive; C recommended (b). In Round 3, B accepted A's arithmetic, and C noted that A's upper bound is a reconstruction.* *(A, B, C)*
- **Answer (2026-11-16, `DR-138`):** **Hold the supporting tier open until the mapping is verified** (differs from the recommendation).

### DEC-583 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 0 (DQ-20)
*From `00_Frame.md` L430–L434, copied verbatim:*
- **DQ-20 · The height and the Acts.** Census I is labeled "Pre-Orbital Era" (spec L20), and the I→II boundary sits at the Act consolidation (~2688; runbook L2294), while `DR-4` gives Census I a design rationale only (L216).
  - **Options:** (a) the height is undated and no Act is chosen; the people are written as Tepenian, with origin as ancestry, in a frame that is mostly Act 2; founders, stock and people are named separately (runbook L2313–2316); and Act-sensitive findings are tagged `[Act unstated]`; (b) date the height to the Census I era, before ~2688, and write it nearer Act 1; (c) write the city across both Acts, side by side.
  - **Recommended, PROVISIONAL: (a).** (b) reads a design figure as a date, and (c) is the in-pass Act comparison `DR-136` item 6 rules out.

  *(A, DQ-4; C, DQ-202 and the tag; B, RF-111, preferring A's form in Round 3)*
- **Answer (2026-11-16, `DR-138`):** **The height in the Census I era, nearer Act 1** (differs from the recommendation).

### DEC-584 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 0 (DQ-21)
*From `00_Frame.md` L435–L439, copied verbatim:*
- **DQ-21 · Does `DR-125` item 4 bind every city?** Item 4 attaches the exile measure to no tier figure, but it is on the contract's not-carried list (L452).
  - **Options:** (a) yes, every city; (b) only the city it was recorded for.
  - **Recommended, PROVISIONAL: (a).** Item 3, which is carried, already excludes reading the free tier as time that is your own, and the canon line (robot physiology L369) is national.

  *(B; A and C name it a developer question in Round 3)*
- **Answer (2026-11-16, `DR-138`):** Yes, every city (as recommended, after a fuller explanation).

### DEC-585 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 1 (DQ-22)
*From `01_Inherited.md` L238, copied verbatim:*
- **DQ-22 · The outdoor belt sited at Bunger Hills** (`18` L30; `DR-96` item 4; S1-34, RF-27). An admitted spec line (L258, indoor growing) and a corroboration-standing line on `DEC-003`'s provisional answer disagree about 88.9% of the rock. Options: (a) carry the belt as reserved and write growing as indoor (spec L258 governs) until `12` and `13` are read and the developer confirms the siting; (b) admit the belt as this city's outdoor growing now, at `DEC-003` provisional standing; (c) hold the belt out of every finding, and rest no finding on either reading of the ground, until `12` and `13` are read at the siting lines (REQ-33); (d) the developer rules where canon's belt lies, or that `18` L30 is a slip. **Recommended, PROVISIONAL: (c), with (d) asked.** Spec L258's words are carried as the admitted line's own, but no finding, figure or spine rests on footprint in surplus or on the belt until the siting is answered. (b) would let a derived siting table set most of the ground. *(Split: see Splits, item 1.)*
- **Answer (2026-11-16, `DR-138`):** Held out of every finding; the developer is not sure yet where the belt lies: read the terraforming and food files at their siting lines first, then bring it back.

### DEC-586 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 1 (DQ-23)
*From `01_Inherited.md` L239, copied verbatim:*
- **DQ-23 · The gulf airports in the melt season** (AS-5; RF-34). Options: (a) record the threshold and the city's own monthly figures side by side, write no closure and no season, tag every summer air finding, and request the data (REQ-32); (b) the developer rules the airports' operating months; (c) the pass derives a closure window from the spec's monthly air means and the real-world threshold, marked `Proposed:`; (d) the developer rules year-round operation as canon-scale fiction, as `DR-96` item 3 does for the haul. **Recommended, PROVISIONAL: (a), with (b) asked.** Air means are not ice-surface temperatures, and the threshold sits in a real-world-basis line of a provisional file; (c) would build a finding on two proxies and make a labeled comparable do a ruling's work. `Airports.md` L21 names melt as a limit, so the season is a research question before it is a ruling.
- **Answer (2026-11-16, `DR-138`):** Research first (as recommended).

### DEC-587 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 1 (DQ-24)
*From `01_Inherited.md` L240, copied verbatim:*
- **DQ-24 · What the exactly-one-door reasoning counts** (`DR-81` L1488; AS-2, AS-3; RF-30). Options: (a) the composition door only, in the ruling's own words: international arrivals overland through Casey, with domestic air passengers a separate path and departures unwritten; (b) every person's way in and out, so the passenger airport carries no arrivals; (c) leave it open. **Recommended, PROVISIONAL: (a)**, because `DR-81` L1488 states the door as composition reasoning, and `Airports.md` L21 links the passenger airport to the national network. The winter arrival's onward route stays a request (REQ-38).
- **Answer (2026-11-16, `DR-138`):** **Left open** (differs from the recommendation).

### DEC-588 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 1 (DQ-25)
*From `01_Inherited.md` L241, copied verbatim:*
- **DQ-25 · Robot ancestry in a city with no majority row** (S1-48; AS-20; RF-32). The general principle (`DR-136` item 10; `DR-137` item 7) is carried; the sentence that handled a no-majority city was recorded for another city and is not carried (contract L435). This city's largest row is 12.86% (spec L59). Options: (a) apply that sentence's form here as this city's own rule (a robot built here records the city's distribution); (b) keep frame PA-11 (the principle and the individual form only) until the national rule is recorded (rulings L1995); (c) answer per community, which needs the sub-locations `DR-4` defers. **Recommended, PROVISIONAL: (b)**: (a) carries another city's answer, and (c) writes structure the deferral forbids.
- **Answer (2026-11-16, `DR-138`):** The principle and its individual form only (as recommended).

### DEC-589 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 2 (DQ-26)
*From `02_Spine.md` L352, copied verbatim:*
- **DQ-26 · G7's standing now that the picks are on the list** (B's DQ-103, C's DQ-202; A agrees). Options: (a) G7 available on `DEC-003`'s provisional answer, used to aim Step 3's research at the deficits, not profiled and not counted in the shape; (b) G7 a counted generator now, at `DEC-003` provisional standing; (c) G7 stays THIN until `DEC-003` is ruled for this city. **Recommended, PROVISIONAL: (a)**: the picks are selection-dependent on the spec's own themes and postdate the climate file (S2-2), and the runbook puts research after the deficit is known (L2566–2567).
- **Answer (2026-11-16, `DR-138`):** **The picks are a full generator for every city** (developer's own words in `DR-138`); Step 2's picks part is re-run as an amendment piece before Step 3.

### DEC-590 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 2 (DQ-27)
*From `02_Spine.md` L353, copied verbatim:*
- **DQ-27 · Which inputs the narrower reading withholds** (B's DQ-101; `02` §4.0 needs two input sets and the brief named none). Options: (a) attribute canon only: withhold every built or ruled particular and institution, and every `[DEC-003 provisional]` and Division of Industry line (set 1); (b) withhold everything at corroboration standing: DEMOTED and ESTIMATED lines, `[DEC-003 provisional]` files, Division of Industry files (set 2); (c) withhold the `[DEC-003 provisional]` and Division of Industry files only (set 3). **Recommended, PROVISIONAL: (a)**, because it is the split `02` §4.0 itself demonstrates (L436–443) and the one in which STANDING COST moves as `02` predicts (B and C, Round 3). Split named: A, its author, recommended in Round 3 that the merge carry the provenance split (b) or (c) as Reading 1 and record (a) as a named further set. Under (b) or (c) the narrower shape is Balanced, the same as the full set's, and phosphorus flips quadrant on (b).
- **Answer (2026-11-16, `DR-138`):** The bare place against the place with its institutions, for every shape reading (as recommended, after a fuller explanation).

### DEC-591 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 2 (DQ-28)
*From `02_Spine.md` L354, copied verbatim:*
- **DQ-28 · Does a robot's recharging draw on the city's electric supply?** (A; B and C adopt.) Rulings L2004 list coolant and electric charge as separate inputs, not separately ruled; the frame records that robots recharge overnight (frame L108). Options: (a) leave it unruled and tag every power-lapse finding robot draw not ruled; (b) rule that robots recharge from the city's electric supply, so power is a standing cost of the robot half as well as of the function; (c) rule that siligel alone powers a robot. **Recommended, PROVISIONAL: (a)**: a national robot-physiology ruling should not be made from one city's pass; (b) would make the city's power the single point of failure for half the population (S2-8's conditional clause).
- **Answer (2026-11-16, `DR-138`):** **Yes, nationally: a robot's charge draws on the electric supply (developer's assumption, conservation of energy), PROVISIONAL pending research.**

### DEC-592 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 2 (DQ-29)
*From `02_Spine.md` L355, copied verbatim:*
- **DQ-29 · Does the Tower-regulated continental grid reach this city at its height?** (A's DQ-2, C's DQ-201; B's RF-101; S2-24, RF-40.) Options: (a) keep `DR-96` item 4's open route, carry the energy file as national context only, write power as a sized requirement whose route is open, and rest nothing on grid connection, tagged `[Act unstated]`; (b) rule a line along the Casey spur into the continental grid while the Tower stands; (c) rule a local plant, off the continental grid. **Recommended, PROVISIONAL: (a)**: `DR-96` left the route open on purpose, the energy file is written about another location in the later era, and the height has no Act; (b) and (c) each set the spine's failure mode and are the developer's.
- **Answer (2026-11-16, `DR-138`):** **Yes, the continental grid reaches the city at its height; the mechanisms need research.** Its fit with the Census I era placement is left to that research.

### DEC-593 · ANSWERED 2026-11-16 (`DR-138`) · 2026-11-16 · Relung Panen ULM run, Step 2 (DQ-30)
*From `02_Spine.md` L356, copied verbatim:*
- **DQ-30 · Animals at the height** (A's DQ-3; C's REQ-203 and RT-210; C in R3 calls option (b) a real choice). The founding brought livestock (`DR-61` L1251); nothing says whether animals are kept at the height. Options: (a) record the silence and research it at Step 3 (RT-13) before anything is written; (b) the developer states whether animals are kept; (c) treat the livestock as part of the founding inventory only, with none at the height. **Recommended, PROVISIONAL: (a)**: (c) would write an absence the list does not state.
- **Answer (2026-11-16, `DR-138`):** Researched at Step 3 (as recommended).

### DEC-594 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 2 amendment (the picks as a generator) (DQ-31)
> **`DR-141`, 2026-11-17:** (a).
*From `02.1_Spine_Amendment_G7.md` L354, copied verbatim:*
- **DQ-31 · How G7 entries that share a root count in the shape.** Options: (a) count every G7 entry, and give distinct facts beside the entries in every quadrant (written here); (b) entries only, so a selection-dependent generator raises the counts; (c) distinct facts only, so a shared-root entry adds nothing; (d) leave G7 out of the shape counts until Step 3 has run. **Recommended, PROVISIONAL: (a):** `DR-138` item 2 makes G7 a full generator; showing both counts keeps a shared root from passing as weight (S2-2's surviving half); the shape is the same under (a), (b), (c) or (d). *(A DQ-1; B DQ-102; C holds the same form.)*

### DEC-595 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 2 amendment (the picks as a generator) (DQ-32)
> **`DR-141`, 2026-11-17:** (a).
*From `02.1_Spine_Amendment_G7.md` L355, copied verbatim:*
- **DQ-32 · G8-S2 while the supporting tier is held** (`DEC-582`). Options: (a) hold the entry out of both counts until the mapping is verified (written here); (b) keep it as Hawaiian dominant only; (c) keep it at DRAFT standing as before. **Recommended, PROVISIONAL: (a):** Hawaiian's dominance is national and the same everywhere (`DR-100` item 1), so without the tier the entry states no property of this place; (c) would rest a counted entry on the held tier. *(A DQ-2; B and C hold it out.)*

### DEC-596 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 2 amendment (the picks as a generator) (DQ-33)
> **`DR-141`, 2026-11-17:** (a): held until the national table gives the re-sized belt here (`DR-140`).
*From `02.1_Spine_Amendment_G7.md` L356, copied verbatim:*
- **DQ-33 · Does footprint in surplus stay held now that `DR-138` holds the outdoor belt?** Step 1's hold (L191) covered either reading of the ground. Options: (a) footprint in surplus stays held until the belt's siting returns, so no finding rests on the room (written here); (b) release it: spec L259 stands as admitted, and only the belt is held; (c) the developer rules the belt's siting now. **Recommended, PROVISIONAL: (a):** the belt's area of about 400 km² sits against an extent of about 450 km² (`18` L30 `[DoI corroboration]`; spec L30), so the surplus cannot be stated while the belt's place is open. *(B DQ-101; C confirmed the reading in Round 3.)*

### DEC-597 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 2 amendment (the picks as a generator) (DQ-34)
> **`DR-141`, 2026-11-17:** (a).
*From `02.1_Spine_Amendment_G7.md` L357, copied verbatim:*
- **DQ-34 · The evidence files' physical-site lines in the narrower reading.** `DR-138` item 6 defines the narrower reading by kind; the spine's set 1 also withheld every `[DEC-003 provisional]` file wholesale. Now that those files are evidence (item 1), their physical-site sentences (the gulf ice's measured thickness, `Airports.md` L21; the sea-ice seasons, `Ports.md` L298) are neither built particulars nor institutions. Options: (a) admit physical-site facts from the evidence files in the bare reading, while every sentence about a built door stays out (written here); (b) keep the spine's wholesale exclusion. **Recommended, PROVISIONAL: (a):** it is the ruling's wording; on this amendment's counts it changes nothing (G2-C4, G5-S4's air door clause and G5-C4 each have a built door as their object), but it governs later steps. *(C DQ-201.)*

### DEC-598 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 3 (research) (DQ-35)
> **`DR-140`, 2026-11-17:** (c) with (a) as the working record; the annual open schedule set by what makes the most in-world sense given the actual climate (research).
*From `03_Research.md` L710, copied verbatim:*
- **DQ-35 · The gulf airports' operating months** (X-4; `DEC-586`; carries Step 1 DQ-23, REQ-32). Research (S3-18 to S3-21): comparable ice runways pause in their warm core and reopen when the ice is back below about −5 °C; this site's air means are November −5.7, December −0.0, January +0.6, February −2.1, March −9.4 °C; the gulf's ice is perennial and about 3 m, used in December and measured in January; dirty ice melts first and the gulf has cryoconite. Options: **(a)** record December to February as the risk window (core about mid-December to late January; late November and early March shoulders) and write no closure, tagging summer air findings meanwhile; **(b)** rule a summer pause in the warmest weeks, perishables then by road; **(c)** wait for the gulf's own record (REQ-69) before ruling; **(d)** rule a pattern rather than dates: the door opens and shuts on the surface each year, kept by clearing and a reflective cap; **(e)** rule year-round operation, by a chipped-ice cap or as canon-scale fiction (as `DR-96` item 3 does for the haul). **Recommended, PROVISIONAL: (c), with (a) as the working record meanwhile, and (d) asked as a second question.** All three readers converged on this in Round 3 (B withdrew its lean toward (b); C widened its months to A's and B's): the site's own surface record is missing and the closest comparable sits 700 m higher on glacier ice.

### DEC-599 · ANSWERED IN PART · 2026-11-17 · Relung Panen ULM run, Step 3 (research) (DQ-36)
> **`DR-140`, 2026-11-17:** (a) then (b) agreed; the national counting rule itself still to be ruled.
*From `03_Research.md` L711, copied verbatim:*
- **DQ-36 · The supporting tier on the verified mapping** (X-3; `DEC-582`; `DR-100` item 3; carries frame DQ-19, REQ-21, amendment DQ-32). The mapping is agreed (S3-55); the tier turns on whether a co-official or widely spoken language counts (S3-56). Options: **(a)** a national rule first: whether a nation's co-official or widely spoken (not national) language counts toward a group; **(b)** Malaysia in one Malay–Indonesian group, the Philippines' English as English's upper bound (mid-points): eight groups, English, Malay–Indonesian, Mandarin, Japanese, Korean, Russian, Thai, Vietnamese (line 4.14–4.25); **(c)** the Philippines fully in English: line 5.64, Vietnamese out; **(d)** the datasheet's set as it stands (English with Malaysia, mid 17.695; line 5.695): Vietnamese out, Thai in only with Patani, recorded as resting on a mapping the sources do not support for Malaysia (English is not Malaysia's official language); **(e)** count each row once under its official language only, a co-official pair split evenly (English 16.14; the same eight as (b)). **Recommended, PROVISIONAL: (a) first, then (b).** All three readers converged on this in Round 3 (A moved to B's (a)-first; C withdrew its (c)-type recommendation). Thai is in under (b) and (e) regardless of Patani. The tier is the developer's.

### DEC-600 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 3 (research) (DQ-37)
> **`DR-140`, 2026-11-17:** (a): the measured figures.
*From `03_Research.md` L712, copied verbatim:*
- **DQ-37 · Algae Lake's figures** (S3-C1, S3-C2). Options: **(a)** drop the superlative (*the oasis's largest freshwater lake*), carry about 17 km (17–18 km), 14.3 km², the 137 m depth as unverified, and the 25 km as the drainage system's total; **(b)** keep the spec's figures as canon-scale fiction for the lake; **(c)** wait for the primary paper (REQ-73). **Recommended, PROVISIONAL: (a).** All three readers' corrections match it.

### DEC-601 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 3 (research) (DQ-38)
> **`DR-140`, 2026-11-17:** (a) with (c).
*From `03_Research.md` L713, copied verbatim:*
- **DQ-38 · The grid and the height** (X-1; `DR-138` item 9; RF-83). Options: **(a)** a continental grid existed before the Tower, steadied by its own plants, and the Tower's regulation arrives later in the era; the city is on the grid at its height, unregulated by the Tower if the height precedes ~2688; **(b)** the grid that reaches the city is the Tower-regulated grid, so the height falls late in the Census I era, at or after ~2688 (revisiting the placement "nearer Act 1", rulings L2014); **(c)** the city's supply is one long line plus standby local generation at its end, era aside; **(d)** the line is built after ~2688 and the city runs on a local plant at its height (conflicts with `DR-138` item 9 unless the height is re-placed); **(e)** leave the fit open. **Recommended, PROVISIONAL: (a) with (c).** All three converged in Round 3: canon's lines tie the Tower to the grid's regulation, not its existence (energy file L107–108; L42 dates nothing), real long lines are kept at their end by standby, and it changes neither ruling; it gives the city's supply a characteristic, a long line on a grid without its later regulator.

### DEC-602 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 3 (research) (DQ-39)
> **`DR-140`, 2026-11-17:** (b) with (d); wild birds at the margins.
*From `03_Research.md` L714, copied verbatim:*
- **DQ-39 · Animals at the height** (X-5; `DEC-593`; carries spine DQ-30). Options, each with its cost on this place's lines: **(a)** none at the height; the founding livestock was a founding inventory only; **(b)** small, warmed, wholly housed animals (poultry, pigs, small ruminants in small numbers) fed from the growing rooms' residues and food waste, their manure to made ground or the nutrient solution, as canon's residue-stream rule allows (`12` L29–31); **(c)** housed ruminants or a prestige dairy on residue and imported fodder, small and costly (pays the haul; no pasture, spec L109); **(d)** insects and land-based fish beside the racks, heated, lit, on the same supply; **(e)** livestock only on the outdoor belt in summer, if the belt is sited here (DQ-40); **(f)** leave open. **Recommended, PROVISIONAL: (b), with (d) as companions.** All three converged in Round 3: every real fully housed high-latitude case shrinks to the smallest-footprint animals; it ties to made ground and the residue rule with the least import; (a) would write an absence the list does not state; (c) carries the cost the real cases dropped. In every option the oasis's wild birds are present at its margins (S3-26).

### DEC-603 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 3 (research) (DQ-40)
> **`DR-140`, 2026-11-17:** (b) with (c); who works it (iii), open, (i) an option.
*From `03_Research.md` L715, copied verbatim:*
- **DQ-40 · Where the outdoor belt lies at this oasis, and who works it** (X-6; `DEC-585`; `12` L259, L303; carries Step 1 DQ-22, REQ-33, spine REQ-46, amendment DQ-33). On canon's figures the belt's ~400 km² is 88.9% of the spec's 450 km² of land and 101.3% of the 395 km² research figure, on ground that also holds the lakes, the dry valleys and a city of 1,000,071. Options: **(a)** the ~400 km² lies on this oasis's rock as written, sharing it with the city (spec L258–259's footprint in surplus would be withdrawn); **(b)** this oasis's allocation is re-sized to what its rock can carry beside the city and its lakes, the remainder redistributed among the regions (a national table edit after the run; `12` L303 already leaves hosting open); **(c)** the remainder is made ground on the ice-free margins or over ice, served from the oasis (`DR-61` L1254: ice is not restricting; canon's terraformed belt is already made ground; no real precedent for made ground over moving ice was found); **(d)** `18` L30's restatement or `12` L259 is a slip, the section undecided until the regions are mapped; **(e)** keep holding. **Who works it:** (i) this city hosts and works the sections at the oasis, the other two served cities taking shares as relations; (ii) each served city works its own sections; (iii) open until the subnet's regional framework (`DR-136` item 3). At canon's national rate about 400 km² would take about 8,000 outdoor workers, seasonal. **Recommended, PROVISIONAL: (b) with (c); who works it stays (iii), open, with (i) an option.** All three moved to (b) with (c) in Round 3: it keeps the belt's distribution (the reason it is safe, `12` L261–265), keeps spec L258's indoor growing and spare ground true, and removes a plausibility exposure (400 km² against 395 km² of ice-free land). **Split on who works it:** A in Round 3 adopted C's (i); C withdrew (i) as a recommendation and kept it as an option; B called (i) a reasonable working answer while noting `12` L303 leaves it open; the narrower reading, which leaves it open, is written. **No finding rests on the belt until this is answered** (Step 1 L191).

### DEC-604 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 3 (research) (DQ-41)
> **`DR-140`, 2026-11-17:** (a), no rate or temperature written.
*From `03_Research.md` L716, copied verbatim:*
- **DQ-41 · A robot's charge on the electric supply** (X-2; `DR-138` item 8). Research found nothing against the conservation-of-energy assumption; every real case draws both the charge and the cold-warming from the plug (S3-53). Options: **(a)** confirm nationally that a robot's charge is electric charge from the supply, and that warming a cold cell to charge it also draws on the supply, with no rate or temperature written; **(b)** confirm the charge only, leaving warming to siligel heat (`DR-137` item 5) unruled (OT-25); **(c)** keep it PROVISIONAL until the coolant/charge relation is ruled (L2004); **(d)** confirm it and add warm charging space as a load in every cold city (a national decision). **Recommended, PROVISIONAL: (a).** All three converged in Round 3 (A moved from confirming the charge only; B, who filed no question, supports (a)); the robot cold file's own three options (L33–37) already price warming as spent energy. (d) is the next decision, and a national one.

### DEC-605 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Step 3 (orchestrator's question)
> **`DR-141`, 2026-11-17:** (a) with (c): a three-researcher supplement on this city's own open threads before Step 5.
- **Research depth now, or targeted follow-ups later?** Step 3's three researchers used 396 of the session's 1,000 web calls (150, 98 and 148 of 250 each) and stopped under their caps by their own choice, to keep room to write; 32 open threads are logged (`03_Research.md` OT-1 to OT-32; six targets named thin). The same session must carry the city to Step 10 across the 11-18 to 11-21 windows, and later phases may not write an inference on the unstated half of a source until research has been asked (runbook L2651–2653). Options: **(a)** keep the remaining calls for targeted questions the phases raise, each logged in the city's research log (the run proceeds this way, run log RL-22); **(b)** run a three-researcher supplement on the open threads now (about 80 calls each), before Phase 2; **(c)** a supplement after Phase 10, on whatever the phases leave open. **Recommended, PROVISIONAL: (a)**, with (c) if calls remain after Phase 10.

### DEC-606 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 2 (composition and arrival) (DQ-42)
> **`DR-140`, 2026-11-17:** (a): left open.
*From `04_Phase_02_Composition_and_Arrival.md` L325, copied verbatim:*
- **DQ-42 · Did robots keep arriving from Upper Earth after the signing?** `[treaty draft]` The draft makes "every robot who may hereafter come into being within such territory" depart for Tepenia (draft L46, II.2.1); `DR-127` records the channel as open in law with no later arrival recorded (rulings L1913); whether robots kept arriving is not decided (L1941). Options: **(a)** leave it open: cite II.2.1 at draft standing as the law of the channel, record no arrival, size none, and write the robot half's recorded channels with that condition; **(b)** rule a continuing stream of robots exiled after the signing (national; it would add a compelled-arrival layer to every city's robot half); **(c)** rule that no robots came into being in Assembly territory after the signing. **Recommended, PROVISIONAL: (a), with the national answer asked of the developer:** it adds the draft's own words to what `DR-127` already records and settles nothing; (b) and (c) are national questions, not this city's. *(A's DQ-2, B's DQ-102 and C's DQ-203, merged; all three converge. C's former option that robots were no longer made on Upper Earth after personhood was withdrawn is withdrawn by C: IV.1.1 withdraws personhood and does not bar manufacture.)*

### DEC-607 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 2 (composition and arrival) (DQ-43)
> **`DR-140`, 2026-11-17:** a new reading: Upper Earth may recognize her as legitimately human, with human rights, and still not as a person (a gray area).
*From `04_Phase_02_Composition_and_Arrival.md` L326, copied verbatim:*
- **DQ-43 · Does a human born in Tepenia stand under the treaty's forfeiture?** `[treaty draft]` The draft ties the loss of Upper Earth personhood and the bar on return to the act of election (IV.2.2–3, II.2.5) and deprives no human of personhood by reason of her own nature (IV.2.1, draft L75); a human born in Tepenia never elected; the draft is silent on her. Options: **(a)** record that the draft is silent: no forfeiture is written for her, and nothing is written about how Upper Earth treats her; **(b)** rule that the forfeiture passes to descendants (a treaty wording change, national); **(c)** rule that Upper Earth recognizes no Tepenian-born human whatever the text says (national); **(d)** leave it until the draft is locked or not (`DR-136`: whether the draft treaty is ever locked is not decided). **Recommended, PROVISIONAL: (a), with (d)'s timing:** it claims least, it is the text as written, and it binds every city, so the national answer is the developer's. *(B's DQ-101; C's REQ-205 withdrawn into it; A holds it)*

### DEC-608 · OPEN · RESEARCH · 2026-11-17 · Relung Panen ULM run, Phase 3 (surface and texture) (DQ-44)
> **`DR-140`, 2026-11-17:** the developer: needs research.
*From `04_Phase_03_Surface_and_Texture.md` L304, copied verbatim:*
- **DQ-44 · Do the export racks stay lit through the shared night?** The export food's load is an average (rulings L1633) and the lit crop has no season (spec L258); canon's shared night stops everyone together (physiology L336–338); robots charge overnight (L334) `[PROV-8]`; real lit growing can cut lights for hours in demand response (research L31). Options: **(a)** leave it unwritten until research gives a photoperiod for canon's model (REQ-104), writing the night as quiet of people, not of power, conditionally; **(b)** rule that the racks are lit around the clock; **(c)** rule a photoperiod whose dark hours fall on the shared night, so the city's light and load drop together at the stop; **(d)** rule a photoperiod set by the supply's hours, apart from the shared night. **Recommended, PROVISIONAL: (a).** The choice sets the city's night sound and light (P3-4, P3-5), whether the robots' charging and the racks' light compete at one hour (RF-78), and part of Phase 4's day; it rests on canon's indoor model, which is national, so the answer should bind every lit city, not this one alone. *(A's DQ-1; B and C agree in Round 3)*

### DEC-609 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 3 (surface and texture) (DQ-45)
> **`DR-140`, 2026-11-17:** glazed; the city is visible. **`DR-141`:** refined: glazed houses screened on winter nights; stacked racks and the seed store windowless; the glow seasonal.
*From `04_Phase_03_Surface_and_Texture.md` L305–L307, copied verbatim:*
- **DQ-45 · Does the light of the lit growing rooms reach the outside: are they built closed or glazed?** All export food is lit indoors (spec L258; `DR-96` item 4), about 0.5 GW of it; no admitted line says whether the rooms are opaque buildings or glazed houses; real lit growing leaks light seen from far away, which curtains reduce and do not end (research L422); light spill matters only where there is dark, here the winter's long nights (S3-42; P3-17). Options: **(a)** opaque, windowless rooms: light kept in, no glow over the city, its winter night lit only by its streets and homes; **(b)** glazed or vented rooms: light leaking at night in the dark half, the city's glow its first sight from far off; **(c)** mixed; **(d)** leave it open until canon's national growing-room form is read at its building lines (REQ-104). **Recommended, PROVISIONAL: (d).** It is a national design fact (every city grows indoors, spec L258); either answer changes the city's night sky, the arrival's first sight and part of its sound, and it should not be set from a texture phase. *(B's DQ-102 and C's DQ-201, merged in C's wording with B's four options, as both now hold; A agrees and sets DQ-44 beside it)*

*Not filed:* whether the oasis's wild birds are a physical fact of the coordinate or held with `DEC-593` (B's DQ-101) is withdrawn by its finder: research DQ-39 already carries the birds (research L714), so it is not a new choice; the birds are reserved (RF-109) (split 18). *Provisional assumptions:* none new in this phase; the series stays at PA-21, and the next file starts at PA-22.

### DEC-610 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 6 (orchestrator's question, before dispatch)
> **`DR-140`, 2026-11-17:** (a), every city.
- **Do a city pass's holidays and faith wait for the stage after the cultural synthesis, for every city?** Your instruction of 2026-11-03 (in the orchestrator's working notes: first work out who these people are, in the cultural synthesis, then what they celebrate and believe) is written in the rulings log only inside two other cities' entries, so a Relung Panen brief cannot cite it there (standing line 25). Phase 6 (Meaning) asks for a belief landscape and two to four observances (`03_The_Phase_Spine.md` L798–832). Options: **(a)** for every city, Phase 6 writes the unnamed load-bearing thing (a stake, a social contract, a debt), the dead (with the reserved mortuary question untouched) and the failure state of the core value, records what national canon already holds (the robot religions roster, the national holidays), and leaves the city's own faith and holidays open, pointed at the stage after the cultural synthesis; **(b)** Phase 6 writes them in full now; **(c)** record it for Relung Panen only. **Recommended, PROVISIONAL: (a)**; Relung Panen's Phase 6 is written on it, and a ruling entry recording it for every city would let later briefs cite it.

### DEC-611 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 8 (orchestrator's question, before dispatch)
> **`DR-140`, 2026-11-17:** (a), every city.
- **Do a city pass's cuisine, music and everyday-life texture wait for the cultural synthesis, for every city?** Your instruction of 2026-11-03 (in the orchestrator's working notes, the same entry as DEC-610's: food, music and everyday life are worked out in the cultural synthesis) is written in the rulings log only inside other cities' entries. Phase 8 (Making) asks for cuisine, music, arts and craft, dress, play and humor, and speech markers (`03_The_Phase_Spine.md` L982–989). Options: **(a)** for every city, Phase 8 writes, for each category, what this place's own conditions supply and demand (function first: what the daily work and the cold require, what the lit food and the made ground allow, what the robot half's sustenance is, from the robot canon), keeps the native and transplanted layers apart as a frame, and records language as the fact of the place it is (`DR-100`; the supporting tier held open, `DEC-582`); the dishes, music, dress styles, games and slang themselves are left open, pointed at the cultural synthesis; **(b)** Phase 8 writes them in full now; **(c)** record it for Relung Panen only. **Recommended, PROVISIONAL: (a)**; Relung Panen's Phase 8 is written on it.

### DEC-612 · OPEN · RESEARCH · 2026-11-17 · Relung Panen ULM run, Phase 4 (ordinary life) (DQ-46)
> **`DR-140`, 2026-11-17:** the developer: needs study, research and design.
*From `04_Phase_04_Ordinary_Life.md` L359, copied verbatim:*
- **DQ-46 · Does the shared stop have a clock hour, and does it hold all year or move with the season?** Canon makes the shared night a stopping time for all (physiology L336–338) and names no hour; here the sky ranges from 2.7 h to about 24 h of light (spec L179–190) and supplies no stop for much of the year (P4-4). Options: **(a)** a stop fixed by the clock all year; **(b)** a stop moved with the season; **(c)** leave the hour unwritten and write only that the stop is made, by schedule, curtain and closing hour (S3-28); **(d)** one national hour, the same everywhere; **(e)** a per-city hour, set at the CST. **Recommended, PROVISIONAL: (c).** `DR-137` item 8 gives the day's structure to the ULM but no line gives the hour; (a) or (b) would set it for this city alone; (d) is a national ruling; (e) is the CST's if the developer wants it. *(B's question and options with C's as (d) and (e), as A, B and C proposed in Round 3; split 10)*

### DEC-613 · OPEN · RESEARCH · 2026-11-17 · Relung Panen ULM run, Phase 4 (ordinary life) (DQ-47)
> **`DR-140`, 2026-11-17:** the developer: needs study, research and design.
*From `04_Phase_04_Ordinary_Life.md` L360–L362, copied verbatim:*
- **DQ-47 · Is anyone awake at the shared night?** Canon has everyone stop together (physiology L336–338); the city's supply, its lit racks (about 0.5 GW for the export alone, `DR-96` item 4), its seed store, warm-chain staging and cooled stores hold set points that run continuously (Phase 3 P3-28), and lit crops are lost within hours to a day in a stoppage (S3-1); the racks' hours are open (Phase 3 DQ-44); no line writes anyone awake and none writes the load unattended (P4-36). Options: **(a)** leave it unwritten and open with Phase 3 DQ-44, tagging every night finding as keepers not written; **(b)** nobody: the continuous loads run unattended through the stop, held by machines, with any failure met at the next day's start (national); **(c)** a small watch or night crew keeps the continuous loads through the stop, its members keeping their own stop at another hour (national; it would add a population with a displaced night to every city, RF-120); **(d)** the stop is staggered for some trades. **Recommended, PROVISIONAL: (a), with the national answer asked.** It binds every city with continuous loads, so it should not be set from one city's pass; this city's continuous load is large enough on its own lines that the question bites here first. *(A's DQ-1 and B's DQ-102 merged, the union of their options; C holds the same recommendation; split 9)*

*Not filed as developer questions:* whether the robot half charges only at the stop (A's DQ-2: withdrawn by its finder, the line itself answering it, "most prominently OVERNIGHT RECHARGING", physiology L334; split 8); what the 0.5 coefficient represents (C's DQ-202: withdrawn by its finder into REQ-127; split 7). **No provisional assumption is issued in this phase;** the series stays at PA-21.

### DEC-614 · OPEN · RESEARCH · 2026-11-17 · Relung Panen ULM run, Phase 6 (meaning) (DQ-48)
> **`DR-140`, 2026-11-17:** the developer: needs research and design.
*From `04_Phase_06_Meaning.md` L352–L354, copied verbatim:*
- **DQ-48 · How does a city pass read a national holiday against its own sky, and does the national reading of Independence Day as the darkest day bind a city whose shortest day still has a sun?** The holidays file reads June 21 as the darkest day (L24–26) and leaves open whether the date was chosen for the solstice and whether every city observes it identically (L160–164); here June 21 has about 2.7 h of daylight under a noon sun under a degree high, and some ground has none for weeks (spec L155, L184; S3-45). Options: **(a)** the national framing stays the national file's open question; each city records its own sky on the day flatly, and any local reading waits for the stage after the cultural synthesis; **(b)** each city's pass may read a national holiday against its own sky as a local inflection, PROPOSED; **(c)** the national question is ruled first (the solstice resonance deliberate, so every city reads June 21 against its own shortest day, or coincidental, so none does) before any city reads the day. **Recommended, PROVISIONAL: (a).** A local reading of a national day is observance, which `DEC-610` already sends to the stage after the cultural synthesis, so (b) asks a method question that ruling answers; and (c) would set every city's reading of its national day from one city's pass, while the national file already holds it open. *(B's P6B-DQ-101 and C's P6C-DQ-201, folded into one question: in Round 3 B withdrew its key for C's and C folded its key into B's, and A, who filed none, asked that if filed they be merged with (a) recommended.)*

**Considered and not filed: made ground in the keeping standard while its siting and use are unwritten** (B's P6B-DQ-102). All three readers hold B's option (a) after Round 3: made ground stands as the standard's scoped, vivid instance and ruled origin (rulings L1252; amendment G7-C2), never as its name or general answer, and no land-use figure or finding about the belt rests on it. B states the question closes in-pass if the standard is not named after made ground, which this merge does not do (P6-2); C would file it only as a pointer under `DEC-585` and amendment DQ-33, whose open part is theirs. **Closed in-pass on (a); the siting question stays where it is already before the developer** (`DEC-585`; amendment DQ-33; REQ-157).

### DEC-615 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 7 (order) (DQ-49)
> **`DR-140`, 2026-11-17:** (a): record the gap, then research.
*From `04_Phase_07_Order.md` L560, copied verbatim:*
- **DQ-49 · The non-thematic export, where the lines hold none.** `03` L895–898 requires an ordinary, emotionally neutral export unrelated to the headline function; every outward flow on this city's lines is food, seed, nutrient recovery or research on its own ground, and the free tier's work is unwritten (P7-8, P7-9). Options: **(a)** record the null with its reason, and ask for the free tier's work and any outbound cargo that is not food (REQ-163); **(b)** the developer names an ordinary export now; **(c)** admit the recovery service as the export (A's original reading); **(d)** admit the reserved know-how candidate, keeping works and surfaces on thawing ground and lake ice, PROPOSED (RF-179); **(e)** read one from a pick, adjusted to the site; **(f)** wait for the industries register and the free tier's work and revisit at Step 5. **Recommended, PROVISIONAL: (a), with (f)'s revisit at Step 5.** (c) fails `03` L895–897's relatedness test (P7-9); (d) would rest an economic finding on a skill no line writes anyone holding; (e) puts a source in the place of a fact; (b) is the developer's to give at any time. *(B, C; A after Round 3: all three recommend (a).)*

### DEC-616 · OPEN · RESEARCH · 2026-11-17 · Relung Panen ULM run, Phase 7 (order) (DQ-50)
> **`DR-140`, 2026-11-17:** the developer: needs research.
*From `04_Phase_07_Order.md` L561, copied verbatim:*
- **DQ-50 · B4 robot sustenance at a city that may not process siligel** (national; `DR-97` item 1 against `DR-137` item 5). The model puts B4 (siligel and coolant, "manufactured, not grown", 3.25 per 1,000 robots) in every city's baseline (`08` L416–427; rulings L1643), while canon has siligel processed only where infrastructure exists and shipped on (rulings L2003), and which cities mine or process is not decided (L2004). Options: **(a)** keep B4 at every city as the model's rate, its local work not written and tagged, until siligel's composition and processing cities are ruled; **(b)** read B4 everywhere as local coolant making plus the handling and storage of shipped siligel, synthesis counted only at processing cities; **(c)** move the siligel half of B4, or all of it, to the processing cities once decided, coolant staying everywhere (a Division of Industry change that moves every city's row); **(d)** site siligel processing at this city (a siting ruling; frame RF-15); **(e)** a national rule for how B4 is read at every city that does not process. **Recommended, PROVISIONAL: (a), with (e) asked.** It changes nothing in this run and treats B4 as Phase 4 treated the own-food term (a national rate applied, never a count); (b), (c) and (e) bind every city; (d) would set a sector from a model line while rulings L2004 holds it undecided. *(A, B, C: all three recommend (a).)*

### DEC-617 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 8 (making) (DQ-51)
> **`DR-140`, 2026-11-17:** neither: **no national music form**; music is regional (the cultural regions now called subnets) and derived after the DCI.
*From `04_Phase_08_Making.md` L435, copied verbatim:*
- **DQ-51 · Robot music: a national form first, or per city?** Robot hearing is national and structurally wider than a human's (physiology L187); which way it is wider leans to the home community's needs (physiology L448; `DR-137` item 2); no file names a robot music; `DEC-611` (PROVISIONAL) sends songs to each city's cultural synthesis. Options: **(a)** a national file of robot music forms before any city writes one; **(b)** each city's cultural synthesis writes its own, with a national request beside it rather than a gate. **Recommended, PROVISIONAL: (a)** *(A's recommendation; C agrees with it on substance and would carry it as a request; B holds (b), split 4)*. A per-city robot music would be written on no canon at all, and nothing robot-musical is written in this city in the meantime; the national request is REQ-196 either way.

### DEC-618 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 8 (making) (DQ-52)
> **`DR-140`, 2026-11-17:** (a): the CST's, not the ULM's.
*From `04_Phase_08_Making.md` L436, copied verbatim:*
- **DQ-52 · Is this city's place on canon's glitch-coolant axis a Phase 8 finding or the cultural synthesis's?** *(B; A and C agree with its recommended answer.)* Canon gives every city with a robot population a local drinking scene on a variety-against-potency axis, where "specific cities can be placed anywhere along it, or between the two poles, as needed" (physiology L285); the frame calls this city's placement "its own later finding" (frame L107) without naming the stage; `DEC-611`'s list names dishes, songs, dress styles, games and slang, not drinks or a drinking scene. Options: **(a)** leave the placement open in the ULM and send it to the cultural synthesis with this phase's function facts (keeping work, coolant through the doors unless B4 rules otherwise, coolant's deep-cold behavior unestablished); **(b)** place it now on the working-class pole, from the city's keeping work (RF-192); **(c)** place it between the poles as its own; **(d)** a national rule for how any city is placed. **Recommended, PROVISIONAL: (a).** A placement is a character of the drinks, which belongs with the synthesis; (b) and (c) would rest a scene on a class reading of work the lines do not give as a class; (d) is national and the developer's (REQ-197). A notes that `DEC-611` with frame L107 already settles (a) to (c), leaving (d) as the only live part; B notes that if `DEC-611` is read as covering drinks the question folds into the open slots without loss.

### DEC-619 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 9 (populations) (DQ-53)
> **`DR-140`, 2026-11-17:** (a).
*From `04_Phase_09_Populations.md` L438, copied verbatim:*
- **DQ-53 · Does the year kept count for more than kind here?** *(B; A and C agree with its recommended answer; B added option (d) in Round 3.)* The lines name the kept year as what makes a person of the place (Phase 5 P5-24; Phase 6 P6-9; Phase 8 P8-60), while kind's relation is the national baseline (physiology L377). Options: **(a)** yes: the year first, the way a person came as where she starts on it; **(b)** no: kind stays the primary division, keeping a secondary note; **(c)** both, co-equal; **(d)** the mode of coming first. **Recommended, PROVISIONAL: (a)**, because kind's relation is national and the year is this place's own; the modes are canon's general sorting (Ch. 14 L35–36) and need sizes no line gives to sort a city. It stays conditional on P5-24's gates. The axis is written on it.

### DEC-620 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 9 (populations) (DQ-54)
> **`DR-140`, 2026-11-17:** (a).
*From `04_Phase_09_Populations.md` L439, copied verbatim:*
- **DQ-54 · May the pass write robot hearing here as leaning toward vibration through solid things (lake ice, rock, the building's frame and the machinery)?** *(A; B's own question, machinery only, folded in as option (c) and withdrawn by B; C agrees.)* Options: **(a)** yes, as a tendency, flagged weaker until the acoustics are researched; **(b)** hold it until REQ-202 is answered; **(c)** the machinery only, dropping the ice. **Recommended, PROVISIONAL: (a).** It is the place's own need on its lines, canon makes the lean a tendency (`DR-137` item 2), and the ice half needs no `[PROV-8]`. P9-12 is written on it.

### DEC-621 · OPEN · RESEARCH · 2026-11-17 · Relung Panen ULM run, Phase 9 (populations) (DQ-55)
> **`DR-140`, 2026-11-17:** the developer: possibly; needs further investigation.
*From `04_Phase_09_Populations.md` L440, copied verbatim:*
- **DQ-55 · May the pass state that the robot half here is mostly built here, on the recorded channels?** *(A; B and C agree.)* The only written robot channel is building (Phase 2 P2-17) and no robot arrival is recorded (rulings L1913, L1941), while the robot channel is open in law. Options: **(a)** yes, conditional, tagged "on the recorded channels"; **(b)** hold until the post-ULM census review sizes builds and arrivals; **(c)** state it as a fact. **Recommended, PROVISIONAL: (a), with the caution that it is canon's general rule applied and never this place's distinction** (Ch. 14 L35–36) *(B's guard)*; not (c), because the channel is open in law. P9-10 is written on it.

### DEC-622 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 10 (catalog) (DQ-56)
> **`DR-139`, 2026-11-17: the Planet is Earth, settled. `DR-140`, 2026-11-17: the Robot Element is Water.** Earth + Water.

*From `04_Phase_10_Catalog.md` L430, copied verbatim:*
- **DQ-56 · Relung Panen's Planet and Robot Element** (`DR-8`, `DR-8a`, `DR-115`). No incumbent pair exists. **Planet: Earth, agreed by all three readers.** **Element: split** (P10-36): readers A and B hold Air (A weakly, with Water its first reserve); reader C holds Water (with Air its near alternative). *Options:* **(a) Earth + Air:** Earth's viability "built from convergence" that "simply hasn't failed yet" (as quoted at reader B L186); Air's shelter held by a stillness it does not control, on the place's own Phase 3 axis "What the stillness keeps" (as quoted at reader A L230), and its membership by sharing the inside, not kind. **(b) Earth + Water:** Water's one path kept open and unfrozen "through that single channel" (as quoted at reader B L187), the culverts before the melt and the one road. **(c) Earth + Earth (the element labeled Contact):** the drains and made ground, ground held only while cold. **(d) Earth + Electricity:** total dependency on the one supply. **(e) Earth now, the Element left open until the developer chooses between (a) and (b).** Reserved planet alternative: Neptune (known by its effect elsewhere). *Against (a):* the stillness is the basin's condition, not what its people do (C). *Against (b):* Water's negative and neutral run opposite to a refreeze that fixes the water where it stands and to a year set by melt and refreeze (B). **⚠ Anchoring risk, plainly:** the rulings-log line L2003, inside every reader's admitted span, carries another location's Planet and Element pair, and the readers report its Element as Air in wording close to the Air readings here; every reader read it before drafting, and no one can show from inside the pass whether it primed or repelled the word. Neither option may be chosen or refused **because of** that other pair; the risk is recorded so the choice is made with it visible, and the convergence check belongs to the terminal differentiation pass. *Recommended, PROVISIONAL:* **(e): Planet Earth; the Element the developer's choice between (a) and (b).** This is the most conservative current view: the three readers agree on Earth and split on the Element after Round 3, a vote is not the merge rule, and each reader's withdrawal (B of Water, C of Air) points in a different direction. *(A P10A-DQ-1; B P10B-DQ-101; C P10C-DQ-201; all three Round 3 replies)*

### DEC-623 · ANSWERED · 2026-11-17 · Relung Panen ULM run, Phase 10 (catalog) (DQ-57)
> **`DR-140`, 2026-11-17:** (a).
*From `04_Phase_10_Catalog.md` L431–L433, copied verbatim:*
- **DQ-57 · How the catalog's unsited places are labeled until siting.** *Options:* **(a) descriptive working labels, flagged as placeholders, with proper names only where an admitted line already gives one** (*the warm charging rooms*, *the seed store*; the airports and the spur by their line-given names); (b) function only, with no working label; (c) the developer names them now; (d) keys only. *Recommended, PROVISIONAL:* **(a).** It lets later steps refer to each place without inventing a name, and the flag keeps the naming the developer's. B recommended (b) and conceded to (a) in Round 3, since all three readers wrote the same descriptive labels in practice; B's concern, that a name cannot be checked against a place with no site, is met by the flag and by keeping proper names out. *(A P10A-DQ-2; B P10B-DQ-102; C P10C-DQ-202)*

*Not carried:* C's DQ-203 (whether to catalog the per-ground sun-return now as a rule with no dates). All three readers already do so (P10-48), so it is not a live choice; C withdrew it in Round 3.

### DEC-624 · OPEN · 2026-11-18 · Relung Panen ULM run, the research supplement (DQ-58)
*From `03.1_Research_Supplement.md` L323, copied verbatim:*
- **DQ-58 · The gulf airports' annual open schedule, given the actual climate** (`DEC-598`; `DR-140` item 8; research DQ-35; T-1). **What the site and its climate say:** the gulf's ice is perennial, fresh, about 3 m in summer and never opens (RS-1); in the one season measured on site, from late January to mid-February, its surface was flat, undecayed and judged fit for heavy wheeled aircraft, but that record began after the warm core (RS-2); the weak layer is a 30 cm porous snow-ice skin with zoned dust pits and tidal cracks at the shores, one zone pit-free and already used by ski aircraft, and little snow to cap or pack it (RS-3, RS-4); ski aircraft fly to the oasis through the whole summer (RS-C6). The central oasis's measured December and January are above freezing in both summers (+1.7, +1.8 °C two-year means), February −2.25, March −5.95 (RS-20); the constructed means are December −0.0, January +0.6, February −2.1 °C, with computed average highs +3.6, +4.2 and +1.3 °C (spec L179–180, L190 `[computed, REQ-52]`) and 71 °C-days above freezing (`Climate.md` L23); the shelf beside it melts first and longest on the oasis's side, about a month a summer and once 44 days, and varies widely between years (RS-5); fresh ice loses reliable strength once candled above about −4.5 °C, and the comparables' criterion for wheeled jets is ice temperature at depth (RS-6; S3-C6); Algae Lake's outlet brings summer water into the gulf (RS-8). Winter limits are light (about 2.7 h in June, spec L155) and storms, whose season is not known (RS-22), not the ice; the sea is shut in winter (`Ports.md` L298). **Options (the union of the readers'):** **(a)** the whole door open all year except a summer pause of about mid-December to late January, longer in a warm summer, set each year by the ice (A's first recommendation, withdrawn by A in Round 3); **(b)** a door split by aircraft and gated by the surface: light aircraft on the pit-free zone in every month; heavy wheeled freighters fly only while the measured ice passes its test (temperature at depth, candling, ponding, the pits), so the cargo door narrows in warm spells, expected about mid-December to late January and wider in a warm summer, with no fixed closure (B and C); **(c)** a fixed summer pause for heavy wheeled flights, about mid-December to late January, perishables then by road (C's option), or one pause for both airports, December to February (B's option); **(d)** a surface rule and no dates: the door is open whenever the ice passes its test (B's option; C's gating); **(e)** open all year with no pause, by canon-scale fiction (B's option) or by capping and patching (A's option: not supported, no snow for a cap and patches weaker than the ice); **(f)** a summer season only, about late October to early March, as real programs run (A's option: rejected on the climate, since the ice is at its best in winter); **(g)** a summer shift to the Apfel blue-ice strip (A's option: against, it stays survey-only, `Airports.md` L21, and the south-east's blue ice melts first); **(h)** record the December–February risk window with no rule (C's option, the current working record); **(i)** wait for the gulf's own multi-year record (all three; REQ-226, REQ-227). **Recommended, PROVISIONAL: (b), with (d) as its rule and (i) as its check.** It is what the site's record and its climate support: the ice never goes, the surface is the limit, and the documented hazard is a warm skin for heavy wheels and the pits, not loss of the door; it keeps the winter door fully open when the sea is shut, keeps the people door open every month, and narrows only the heavy-freight door in warm weeks, which are also the weeks the spur weakens (RF-88). **Split, named:** in Round 3 A and B hold no written closure, the mid-December to late January weeks carried as an expectation; C moved toward B's dated envelope as the expected window of a heavy-freight pause; the narrower reading, an expectation and no fixed closure, is recommended; B's light-and-medium and C's light-only wording for the every-month door are written as light aircraft, the narrower. **Consequence on this place's lines:** in the core weeks perishables wait in the warm chain or go frozen by road (S3-36). The keeper of the ice is not written (`DR-137` item 11; REQ-237).

### DEC-625 · OPEN · 2026-11-18 · Relung Panen ULM run, the research supplement (DQ-59)
*From `03.1_Research_Supplement.md` L324, copied verbatim:*
- **DQ-59 · The ordinary, non-food outbound load** (`DEC-615`; Phase 7 DQ-49, REQ-163; T-2). **Options (the union):** **(a)** the backhaul: scrap metal, broken machines and fittings, spent batteries, used oil, tires, crates and empties, out by the spur and the cargo apron (RS-9); **(b)** a rare specialty stone from the southern charnockite, dressed blocks by road, with crushed stone for the city's own building from the same pits (RS-10; conditional on REQ-233); **(c)** glacier or lake ice or water (RS-11: weak; the lakes are winter water and the cold chain's room is the food's); **(d)** non-food plants from the glazed and lit rooms: young plants, transplants, seedlings, flowers (RS-11: inside the vocation); **(e)** know-how and trained people from the research stake (RS-11: a service); **(f)** collectible issues (RS-11: an authority's act, governance); **(g)** crushed rock (RS-10: fails on the place's own lines); **(h)** none: the gap stays recorded as an absence, the free tier's work unwritten. **Recommended, PROVISIONAL: (a) as the ordinary, neutral outbound load, with (b) left open as the only sold candidate and (h) holding for a sold export until the rock's use is ruled.** The backhaul is ordinary and emotionally neutral on every comparable without inventing a trade, and its first reason, that the waste cannot stay, holds on the place's lines; whether it fills a light leg is unwritten (REQ-232). It is a flow, not a sale: if the developer wants a sold export unrelated to the headline, the stone is the only candidate the rock supports, and it rests on a fact not yet known. **Split, named:** in Round 1 A and B recommended (a) and C recommended (b) with (h); C withdrew its recommendation of the stone in Round 3, and B adopted the stone as conditional; all three now hold this answer.

### DEC-626 · OPEN · 2026-11-18 · Relung Panen ULM run, the research supplement (DQ-60)
*From `03.1_Research_Supplement.md` L325, copied verbatim:*
- **DQ-60 · The measured central-oasis months beside the constructed curve** (T-5; `DEC-575`). **Options:** **(a)** carry the measured 1956–58 months as the central-oasis column beside the constructed, lake-station-anchored column, each with its station `[PA-3]`, siting open; **(b)** replace the constructed column; **(c)** keep only the constructed column. **Recommended, PROVISIONAL: (a)**, which extends `DEC-575`'s both-records rule to the months and changes no figure the run already wrote; carry the two cautions (two years are not a climatology; June as the coldest month rests on two winters). *(B, RSB-DQ-103; supported by A and C in Round 3.)*

### DEC-627 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 5 (reconciliation) (DQ-61)
*From `05_Reconciliation.md` L545, copied verbatim:*
- **DQ-61 · Does the glazed houses' summer sun lower the lit load in canon's power model?** `DR-96` item 4 (rulings L1633) sizes the export food's power as if every indoor crop were lamp-lit, "the 400 km² outdoor belt the only sunlit part", about 0.5 GW; `DR-141` item 1 (L2044) has "glazed houses take the summer's unbroken sun". Options: **(a)** the model stands as a sizing rule: every indoor kilogram counts as lit, the sun through the glass is an unsized summer supplement, no figure moves, and "the only sunlit part" reads as the only sunlit part counted; **(b)** the glazed share's summer sun offsets part of the lit load, a Division of Industry re-run (national), with the stacked racks unchanged; **(c)** the glazed houses grow outside the export model, for the city's own food or for research; **(d)** hold until canon's national growing-room form is read at its building lines (REQ-241). **Recommended, PROVISIONAL: (a), with (d) read later.** It keeps every written figure, matches the ruling's own reasons (heat loss and the glow, not light), and the energy finding claims no magnitude beyond the model's (S5-80); (b) would reopen a ruled figure on an unsized share and move `16` and `18` nationally; (c) adds a function no line writes. *(A and B, the same question; C supports (a) with (d).)*

### DEC-628 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 5 (reconciliation) (DQ-62)
*From `05_Reconciliation.md` L546, copied verbatim:*
- **DQ-62 · Do Phase 9's household lines "a dish" (P9-5, L225) and "an origin feast" (P9-25, L253) stand under `DEC-610` and `DEC-611`?** Options: **(a)** both stand as unnamed function statements about origin forms kept at home; **(b)** both stand, with "an origin feast" read conditionally (*if a household keeps one*), since observances wait for the stage after the cultural synthesis; **(c)** both phrases are withheld until the cultural synthesis. **Recommended, PROVISIONAL: (b).** No dish or feast is named either way; (b) keeps the household finding and makes no observance a fact before its stage; (c) loses a finding that rests on the composition, not on a cuisine. *Split:* B filed it and in Round 3 withdrew it as a question, keeping the lines as a boundary note; A and C hold (b). It is kept so the developer can confirm the conditional reading written at S5-46.

### DEC-629 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 5 (reconciliation) (DQ-63)
*From `05_Reconciliation.md` L547, copied verbatim:*
- **DQ-63 · What does "wild birds at the margins" (`DEC-602` (d)) mean?** The ruling was given before the supplement placed the nesting through the southern hills, 25–155 m (RS-16, RS-C1). Options: **(a)** "margins" means outside the kept city, wild and unhoused; the nests are in the southern hills; **(b)** "margins" means the lake and ice margins, as research L255 and L258 had it before the correction; **(c)** both, with the nesting in the hills and foraging at the city's edges and its food waste (RS-16's skuas). **Recommended, PROVISIONAL: (a), with (c)'s skua clause.** (a) fits the correction and the ruling at once; (b) rests on a corrected line. *Split:* B filed it and in Round 3 withdrew it as not a real choice; A and C hold (a) with (c)'s clause. It is kept because the ruling predates the correction, so what its word means is the developer's to say.

### DEC-630 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 5 (reconciliation) (DQ-64)
*From `05_Reconciliation.md` L548–L550, copied verbatim:*
- **DQ-64 · Phase 8 P8-24 (L214), "music here is household-held and plural", under `DEC-617`.** Options: **(a)** read it as the place's conditions only (households keeping origin forms nearer Act 1), every music claim held for the regional derivation after the DCI; **(b)** withdraw P8-24, keeping only P8-25's sound environment; **(c)** keep it as written. **Recommended, PROVISIONAL: (a).** It keeps what the place's conditions allow (`DEC-611`) and writes nothing about music itself. *(C; A and B hold (a).)*

*Not carried as questions:* C's question on the standby generation (withdrawn in Round 3 as research; REQ-238) and C's question on P9-28's "carries none" (withdrawn in Round 3; answered at S5-42).

### DEC-631 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 5 (reconciliation) (DQ-65)
*From `05_Reconciliation.md` L1013, copied verbatim:*
- **DQ-65 · Does Upper Earth control this city's phosphorus input, as spec L245–247 says?** The spec's own conclusion-shaped line calls the claim load-bearing and an anchor for any pass; contract RF-5 found no source on the list, so the pass writes the dependency (spec L234) and not the control. Options: **(a)** leave the control unwritten and the line held as unsourced (PC-137); the pass stands as written; **(b)** rule the source and who controls it, nationally, and the pass may then write the exposure as a fact at the strength the ruling gives; **(c)** rule that the national recovery role (`DR-75`) means the city is not wholly dependent on an outside source, and the spec line is narrowed. **Recommended, PROVISIONAL: (a), with REQ-248 carried.** It adds nothing the lines do not give; (b) and (c) are national calls, and either would change Phase 7's order entries. *(A filed it; B and C hold it as a real national choice in Round 3. A offered to fold it into contract REQ-2 if one channel were preferred; it is kept, since the other two hold it.)*

### DEC-632 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 5 (reconciliation) (DQ-66)
*From `05_Reconciliation.md` L1014, copied verbatim:*
- **DQ-66 · The development brief's water premise** (L22–31: the water fact as the whole city; the cheapest water in the nation; no ice to melt), against the pass's finding (research S3-31: winter water from deep lakes under ice through heated intakes, on the supply) and its strongest finding, energy (S5-80). Options: **(a)** the pass stands, and the brief's opening is annotated as superseded framing (PC-108); **(b)** the pass stands, and a softer form, *plentiful but drawn through the supply*, goes to the cultural synthesis as a meaning question; **(c)** the developer holds the brief's premise as intended, and the pass's water findings are revisited against it. **Recommended, PROVISIONAL: (a), with (b)'s note.** The pass reached its water findings from admitted figures and research; (c) would rest a spine on a Tier 3 framing whose own figures (the superlative, the deficit) are already superseded. *Split: B filed it and in Round 3 withdrew it as a question (the brief is Tier 3 reasoning, not a ruling, so PC-108 carries it); A and C hold it, C because the brief is the developer's own framing. It is kept, as Part 1 kept DQ-62 and DQ-63 in the same position, so the developer can confirm the reading written at S5-148.*

### DEC-633 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 5 (reconciliation) (DQ-67)
*From `05_Reconciliation.md` L1015, copied verbatim:*
- **DQ-67 · The spec's conclusion-shaped lines L127 ("That tension is the city." … "it is empty because it is sealed.") and L244's "should anchor any pass", against the pass.** The pass's strongest finding is energy (S5-80), and the city's count is census arithmetic. Options: **(a)** leave the lines as written, excluded as conclusions, with a pointer to S5-80 added beside them after the run, an annotation that does not touch the lines (PC-134, PC-136); **(b)** annotate the lines in place as pre-pass readings; **(c)** replace L127 with the pass's finding; **(d)** strike them. **Recommended, PROVISIONAL: (a).** It keeps the author's original framing visible, the way the folder keeps its struck passages, and stops a later reader from taking it as the pass's conclusion; (c) and (d) erase lines the developer may value as a starting image. **L244's "breadbasket" is not in this question:** it is the one factual mismatch (spec L254 states the second agricultural region; `DR-71`) and goes to the docket (PC-135). *(One question, merged: B merged its S5BB-DQ-102 into C's S5BC-DQ-201 in Round 3; C then adopted B's form; A holds the same.)*

### DEC-634 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 6 (differentiate) (DQ-68)
*From `06_Differentiation.md` L196, copied verbatim:*
- **DQ-68 · Substitute 1 at Step 6, against `DR-136` item 6.** III.4 says run substitute 1 without fail (`04` L526); the rulings put earlier states after the pass by order (Phase 5 P5-9 L166; frame S0-9 L55). Options: **(a)** run it in a sequence form only, on facts the pass already writes, nothing new derived; **(b)** record it as not run until the history stage, the undated sequence lines cited; **(c)** run a full earlier-state comparison now. **Recommended, PROVISIONAL: (b).** It claims least against the rulings while keeping the sequence on record (S6-29); (a) is a founding-against-height comparison in form; (c) would write dated history in-run. *(Filed by A, S6A-DQ-1; B and C recommend (b); A's current view, record the sequence and do not run the comparison, is (b) in substance.)*

### DEC-635 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 6 (differentiate) (DQ-69)
*From `06_Differentiation.md` L197, copied verbatim:*
- **DQ-69 · How does a city's symbol pair reach the terminal differentiation check, when the city table has no symbol column?** III.0 was written from a symbol collision a differentiation guide could not see (`04` L459–462). Options: **(a)** add a write-only symbols section to the city table (Planet · Element · provenance note), a method change for every row, earlier rows filled at the terminal check from the registry, the runbook updated in the same commit; **(b)** leave the table as it is, and write an instruction in runbook Step 6, at this run's Step 9, that the terminal check reads `City_Symbol_Assignments.md` beside it; **(c)** a notes line under each row, or a pointer column in section 1, naming the registry row. **Recommended, PROVISIONAL: (b).** It adds no column a write-only row must fill blind, keeps the pair in the file that already owns it (Step 5 PC-86, L457), and closes III.0's gap (`04` L467) by instruction rather than by a second copy that could drift; (a) is the stronger guard and stays the developer's to choose, since it changes every city's row. *(A S6A-DQ-2, B S6B-DQ-101, C S6C-DQ-201; C withdrew its recommendation (a) in Round 3.)*

### DEC-636 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 7 (QA) (DQ-70)
*From `07_QA_Gates.md` L807, copied verbatim:*
- **DQ-70 · What does Gate 7 count: picks or calls?** The gate expects about 70–80% of researched picks to change a finding (`04` L216); this run's logs classify calls (310 of 409 classed calls changed a finding, 75.8%), and its per-pick column states no total; the picks were dispositioned as applies, research aim or does not apply (Q 28, R 47, N 24) and searched under research targets. *Options:* **(a)** count by pick, from Step 3's "Became" column and its supplement and Phase 10 equivalents; **(b)** count by classed call, as the logs do, with a rule that each log separates change from corroboration; **(c)** both, each labeled. *Recommended, PROVISIONAL:* **(c).** The call count is what the logs can give now; the pick count is what the gate's wording asks; showing both keeps either from passing for the other, and (b) alone loses nothing the logs found while leaving the gate's test unrunnable on picks. *(A S7A-DQ-1; B S7B-DQ-101: the same question and the same recommendation, merged; C supports (c).)*

### DEC-637 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 7 (QA) (DQ-71)
*From `07_QA_Gates.md` L808, copied verbatim:*
- **DQ-71 · The "no season" interior claims after the glazed houses** (Phase 8 L119, Phase 10 L113, Phase 10 L262; E7-8 to E7-10). Step 5 read Phase 3 P3-35 and Phase 10 P10-95 as holding "for the windowless racks only; the glazed houses carry the sky's season through the glass" (05 L167), but three lines making the same claim were not given that reading. *Options:* **(a)** amendment notes narrowing each line to the windowless racks, as Step 5 did for the other two; **(b)** read "no season" in those lines as the crop's (no harvest day) and leave them, with the glazed houses' seasonal light noted once at Phase 10; **(c)** hold all five lines until the glazed houses' share is known (REQ-241). *Recommended, PROVISIONAL:* **(a).** It is the reading Step 5 already chose for the same words, and it changes no axis (06 S6-45); (b) leaves the axis rationales saying the interior has no season while P10-50 says the houses are glazed; (c) waits on a figure no finding needs. *(C S7C-DQ-201; A and B support (a) in Round 3.)*

### DEC-638 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 8 (the Review Panel) (DQ-72)
*From `08_Review_Panel.md` L704–L715, copied verbatim:*
- **DQ-72 · The kept year's other side: the returner, the one who leaves before a year ends, and the human past keeping** (Gate 9's fire; RF-260;
  S8-6, S8-17, S8-13; A S8A-DQ-1, B S8B-DQ-101, C S8C-DQ-201, one question). Membership turns on one kept water year (Phase 9 L224; `DEC-619`), and
  the pass writes it for the newcomer only (Step 7 S7-45, S7-46). Does a resident who kept a year, left by the spur for years and returns still
  belong, or must she keep a year again; does someone who leaves before the year ends restart it; and does a human who can no longer keep still
  belong? **Options:** **(a)** a kept year stays kept, for the returner and for the human past keeping, and knowledge of the year is renewed only by
  living it (RF-271) *(C)*; **(b)** a long absence or the end of one's keeping lapses it, and a water year lived again regains it *(A, B, C)*; **(c)**
  a completed year stays kept and an unfinished one restarts *(B)*; **(d)** leave it unwritten until return itself is written (REQ-120) and the
  population history is designed, with AM8-2's open entry applied meanwhile *(A, B)*. **Recommended, PROVISIONAL: (d)**, the view of all three
  readers after Round 3 (C withdrew (a) for it). The return the rule would govern is itself open (REQ-120), the conversion moment is reserved
  (Phase 5 RF-142), and a pass writes the height with no dated history (`DR-136` item 6); (a) to (c) each write a membership rule no line gives.
  *A reading only, not a ground:* the lived year, "not written down" (Phase 9 L267), leans toward (b) *(B)*; P9-4's "having kept a year" and P9-31's
  standing from what one has kept lean toward (a) *(C)*.

### DEC-639 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 8 (the Review Panel) (DQ-73)
*From `08_Review_Panel.md` L716–L732, copied verbatim:*
- **DQ-73 · Method: what counts as "an admitted or ruled line that shows the place knowingly holding the thing" for an `unmet` (runbook L2999;
  `00f` L744–753)?** *(A S8A-DQ-2, B S8B-DQ-102, C S8C-DQ-202: three parts of one question, merged as all three readers propose in Round 3.)* It
  decides this run's `unmet` count, now 1.
  - **(i) Does a ruling that confirms a reading the pass proposed count as a ruled line, or stay the pass's own coinage?** Options: yes, once given;
    no, it stays coinage; only where the ruling's own words state the place's knowing. **Recommended, PROVISIONAL: yes** *(all three)*: the coinage
    bar exists to stop a pass certifying itself, and a developer ruling is not the pass's own voice. *On "no", S8-27 becomes `declined` and the count
    is 0.*
  - **(ii) Does a ruling reach beyond its own words (the kept year ranked above kind, carried to age)?** Options: yes, by the next category its order
    displaces; no, its own words only. **Recommended, PROVISIONAL: its own words only** *(all three after Round 3; A withdrew "yes")*. *On "yes", S8-14
    could be re-counted `unmet`.*
  - **(iii) Does a ruled act with its stated in-world reason suffice, or must the line show the place holding the very thing the objection asks it
    to give up?** Options: **(a)** a ruled act with its stated reason suffices *(B, C)*; **(b)** a ruled line is necessary but not sufficient: it must
    show the place holding the very thing the objection asks it to give up, as a thing it would refuse to surrender *(A)*. **Recommended,
    PROVISIONAL: (b)**, the reading that claims least, on which this file is written (S8-23 `declined`): rulings L2044 states the act's reason as heat
    loss and the dimmed glow as its consequence, so what it shows the place knowingly holding is the heat, not the dimness. *Against it (B, C):* the
    screens are drawn every winter night by the place's own hand for its own reason, which is knowing in the plain sense, and (b) would make `unmet`
    unreachable for any act the lines record without a speaker. *On (a), S8-23 becomes `unmet` and the count is 2.*

### DEC-640 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 9 (the record) (DQ-74)
*From `09_Record.md` L517–L522, copied verbatim:*
- **DQ-74 · Where the ruled convergence rule sits in the runbook.** **(a)** appended to the end of runbook L2620 (Step 3, item 3.4), on the
  same line, with the pointer in the generator method beside `DEC-594`'s counting rule; **(b)** a new item 3.4a on its own line after
  L2620, the numbering frame named in the commit and every later brief's runbook spans recomputed; **(c)** inside LAW 0-R's "In practice"
  line and its full copy in the disciplines file. **Recommended, PROVISIONAL: (a).** It sits where the runbook says how much a source may
  carry, moves no cited line, and keeps a weighting rule out of a law about search depth that is stated in two places. *(A S9A-DQ-1; B
  S9B-DQ-101; C withdrew (b) in Round 3.)*

### DEC-641 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 9 (the record) (DQ-75)
*From `09_Record.md` L523–L526, copied verbatim:*
- **DQ-75 · The two-stage Step 5 seal (MC-2).** **(a)** adopt it as the Step 5 rule whenever the read-last material is checked in a second
  stage, worded as MC-2, appended to L2888; **(b)** keep it as a recorded technique the orchestrator may use; **(c)** do not adopt it.
  **Recommended, PROVISIONAL: (a).** It held in this run, Step 7 relied on it, and the hash written into the file let this step re-check it
  without the copy; its cost is four commands. RF-274's wider reach is not part of the question. *(A S9A-DQ-2; B S9B-DQ-102; C S9C-DQ-201.)*

### DEC-642 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 9 (the record) (DQ-76)
*From `09_Record.md` L527–L531, copied verbatim:*
- **DQ-76 · The selection-dependence sentence (MC-4).** **(a)** the ruling's sentences only, with nothing added; **(b)** add, as a separate
  marked sentence after the ruled text, that places chosen because they match the location's own themes add no weight to a finding drawn from
  those themes (06 L111). **Recommended, PROVISIONAL: (b).** Step 6 found the picks selection-dependent on the spec's own themes, and the
  convergence rule would otherwise count that agreement as independent; either way the sentence stays outside the ruled text. *(C
  S9C-DQ-202; A leans (b) on its merit; B takes no view on adoption and asks only that it stay outside the ruled text.)*

### DEC-643 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 9 (the record) (DQ-77)
*From `09_Record.md` L532–L535, copied verbatim:*
- **DQ-77 · The tool fixes (MC-30).** **(a)** approve fail-loud fixes now: a tool that cannot validate, or whose scope matches nothing, says so
  and exits; **(b)** approve the full fixes now; **(c)** hold every tool change until the city corpus is done. **Recommended, PROVISIONAL:
  (a).** Each failure here was a quiet zero or a plausible line routed around by hand, and a fail-loud fix changes no result a tool reports
  when it works. *(A S9A-DQ-3; supported by B and C in Round 3.)*

### DEC-644 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 9 (the record) (DQ-78)
*From `09_Record.md` L536–L541, copied verbatim:*
- **DQ-78 · Step 6's two wide cells, already in the shared table** (S6-15, S6-24; REQ-268). **(a)** after the run, replace this city's own
  row blind with the two cells narrowed to their axes (backup, assertions, a `diff` showing this row only), the lists kept in Step 6's III.0
  items; **(b)** confirm that a cell may carry a list; **(c)** change the method so the row is inserted at Step 9, after Step 7's cell checks.
  **Recommended, PROVISIONAL: (a), with (c) considered for later runs.** (b) contradicts "One AXIS per cell, never the content." (runbook
  L3016), and (a) fixes this row without reading any other. *(C S9C-DQ-203; A S9A-DQ-4's (b) is the same act; B S9B-RQ-103 gives the same
  routes.)*

### DEC-645 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 9 (the record) (DQ-79)
*From `09_Record.md` L542–L546, copied verbatim:*
- **DQ-79 · Spelling corrections inside an appended log** (REQ-266; `09.5_Log.md` L54). **(a)** an in-place word change, which moves no
  line, with a dated note appended at the log's end; **(b)** corrections only as appended notes, the old spelling left in place; **(c)** quoted
  source text keeps its source spelling. **Recommended, PROVISIONAL: (a).** It keeps the standing American English rule and keeps the log's
  history visible; (b) would leave British forms standing; (c) conflicts with the startup's spelling rule. *(C S9C-DQ-204; A; B withdrew (b)
  in Round 3.)*

### DEC-646 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 9 (the record) (DQ-80)
*From `09_Record.md` L547–L550, copied verbatim:*
- **DQ-80 · What the Step 9 QA block holds.** **(a)** the verdicts, errata and figures by line, the raw outputs pointed to in the QA file by
  line and only Step 9's own scans pasted; **(b)** every raw block pasted again into the record; **(c)** a summary only. **Recommended,
  PROVISIONAL: (a).** It keeps the raw output whole in one place, as the paste rule intends, without a second copy that could drift; (c) is
  what the paste rule forbids. *(B S9B-DQ-103; adopted by A and C in Round 3.)*

### DEC-647 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 10 (the readiness check) (DQ-81)
*From `10_Readiness_Check.md` L609–L613, copied verbatim:*
- **DQ-81 · Where the next subject's run files are drafted.** **(a)** in a fresh session that has never read this pass; **(b)** in this
  session as planned, procedure lines only, with the next run's first step an audit of every inherited line for this pass's material (this
  pass's startup Section 0.4 item 1); **(c)** as planned, with no audit. **Recommended, PROVISIONAL: (b).** It keeps the developer's
  2026-11-17 plan and closes the `M-355` shape with the audit that worked here; (a) costs a session, and (c) repeats the measured failure.
  *(A S10A-DQ-1; B and C concur in Round 3.)*

### DEC-648 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 10 (the readiness check) (DQ-82)
*From `10_Readiness_Check.md` L614–L621, copied verbatim:*
- **DQ-82 · The memory entries that need a band for the next subject** (S10-1). **(a)** band all ten files now, naming the next subject
  immediately after each frontmatter, and decide the three borderline files one by one; **(b)** band the six Group 1 files now, and decide
  Group 2's four with the three borderline files one by one; **(c)** leave them, since the run is warm and conclusion files are read last.
  **Recommended, PROVISIONAL: (a)**, with a rewrite to attributes plus a pointer (`06` L179–183) as time allows, first for the catalog
  line (file 10), which repeats file 6. A pulled entry arrives with no read-last discipline around it, and banding takes minutes. *Split:
  (a) is C's current view; A's Round 3 view and B's would amount to (b), and A's withdrawal from live to borderline on Group 2 is evidence
  for the narrower reading. The stricter judgment is written, and the choice is the developer's.* *(A S10A-DQ-2; B S10B-DQ-101, withdrawn
  in Round 3 in favor of A's; C Round 3 §5.5.)*

### DEC-649 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 10 (the readiness check) (DQ-83)
*From `10_Readiness_Check.md` L622–L625, copied verbatim:*
- **DQ-83 · Tracker L387 carries a Phase 10 result** (S10-12), while the startup forbids rewriting earlier tracker text (startup
  L214–215). **(a)** leave L387 as written, append a dated line noting that it carries a finding, and manifest the coordinate in `06`'s
  section for this city; **(b)** amend L387 in place to remove the result; **(c)** leave it unrecorded. **Recommended, PROVISIONAL: (a).**
  It keeps both rules and gives a future run for this city the coordinate to skip. *(B S10B-DQ-102; A and C concur.)*

### DEC-650 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 10 (the readiness check) (DQ-84)
*From `10_Readiness_Check.md` L626–L630, copied verbatim:*
- **DQ-84 · The proposed method changes and the next run.** **(a)** rule the list-building changes (MC-5, MC-7, MC-8, MC-9, MC-33) before
  the next startup is written, so they are in the rules; **(b)** write them into the next startup as that run's instructions, marked as
  proposals, and rule later; **(c)** hold all of them until after the city corpus. **Recommended, PROVISIONAL: (b).** The next run follows
  its startup and the rules, not the observations file (runbook L3158–3160), so (c) leaves it without them, and (b) carries them without
  deciding their wording early. *(C S10C-DQ-201; A and B concur.)*

### DEC-651 · OPEN · 2026-11-18 · Relung Panen ULM run, Step 10 (the readiness check) (DQ-85)
*From `10_Readiness_Check.md` L631–L636, copied verbatim:*
- **DQ-85 · The pass README's stale status lines** (S10-12). **(a)** the orchestrator updates the status lines in place now, while the run
  is open; **(b)** an amendment note at the README's end after the run; **(c)** leave them until the CST and RWBEM add their files.
  **Recommended, PROVISIONAL: (a).** The run is still open, the lines are status rather than findings, and a README that says no output
  exists is the "status lie" that runbook L3149–3150 names for a pre-seeded folder. *Split: A (S10A-RQ-4) and B (S10B-HF-107) first routed
  it to the after-run session (b), and both moved to (a) in Round 3. A also asked whether `DR-101` covers the README, which is scaffolding,
  so C keeps it as a real choice.* *(C S10C-DQ-202.)*

---

## Open since 2026-11-18 (Ariun Nuur ULM run, preparation: the input validation)

*From the validation of the pass folder's sheets, 2026-11-18 (three validators, a fix writer and a checker; `STARTUP_Ariun_Nuur_ULM_2026-11-18.md` §10). The run itself files its questions after these.*

### DEC-660 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · Ariun Nuur, preparation
- **Step 2's reads of the industry file `16`.** Pre-Trip L133 sends Step 2 to `16` only at L241–248 and the first-pass Half B row L282 (39.0% / 5.7% / 55.3%); the city's own §23 DETERMINED section (L2349–2358: 39.4% / 19.7% / 40.9%) supersedes that row, and the reliability sheet L44 says to quote both and say which governs. Options: (a) add §23 L2349–2358 to Step 2's `16` reads; (b) keep L282 only and read §23 at Phases 4 and 7; (c) replace L282 with §23. **Recommended, PROVISIONAL: (a).**

### DEC-661 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · Ariun Nuur, preparation
- **The web-search cap the sheets state.** Pre-Trip L70, L150 and L442 say 200 per session; the developer's stated budget (2026-11, in memory) is 1,000 per session, shared by every agent; neither figure is in the rulings log or the runbook. Options: (a) 1,000 per session, shared, recorded in the rulings log; (b) keep 200; (c) name no figure and point to the live budget. **Recommended, PROVISIONAL: (a).** The run's startup file already uses 1,000.

### DEC-662 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · Ariun Nuur, preparation
- **Spec L219, the gameplay-reachability bullet.** Step −1 excludes only Open Questions bullet 1; spec L219 ("Can Ariun Nuur be reached in gameplay?", a DLC hook) stays admitted. Options: (a) exclude the whole bullet as DLC and gameplay scoping, like the `DLC:` header and Gameplay Notes; (b) exclude only its DLC and gameplay clauses; (c) admit it. **Recommended, PROVISIONAL: (a);** its one location fact, highway reachability, is already at spec L9.

### DEC-663 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · Ariun Nuur, preparation
- **Step_0 L21, the census L440 tension note.** Its premise (the founding population "primarily Russian exiles") was retired by `DR-35`; the founders are now those at spec L23 and L147, and its path `Specs/Vostok.md` no longer exists. Options: (a) keep the quotation, flagged stale in the source and not an input; (b) drop the row; (c) leave it until the post-ULM census review (`DR-23`). **Recommended, PROVISIONAL: (a).**

### DEC-664 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · Ariun Nuur, preparation
- **Phase 5's FLAGGED rows (sheet L27–37).** `DR-131` item 3 (lines about shared things a city is named in are its own lines), `DR-136` item 3 (the subnet the same) and `DR-138` item 1 (`Infrastructure/` and the relationship files are evidence for every city) make Highways L156–170, Airports L18 and the relationship database's entry L476–484 look citable as this city's own lines. Options: (a) re-dispose them as citable own lines, excluding clauses grounded only in another city's lines (relation legal, comparison barred); (b) keep them flagged. **Recommended, PROVISIONAL: (a).**

### DEC-665 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · Ariun Nuur, preparation
- **Phase 7's food-worker-years and its 3.5×.** "18,774 food-worker-years" (sheet L30, L34) is a deficit headcount, which the sheet's own citation gate bars (reliability sheet L45); "3.5×" is 66,007 ÷ 18,774, and on the live mandate it is 71,444 ÷ 18,774 ≈ 3.8× (`16` L1: its narrative was not rewritten). Options: (a) keep the quotations, the headcount marked not citable and the 3.5× marked stale (≈ 3.8× live); (b) drop both; (c) leave them. **Recommended, PROVISIONAL: (a).**

### DEC-666 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · Ariun Nuur, preparation
- **Errors found in the source files, outside the sheets.** The validation found, without editing them: spec L79 reads "READER station: Ariun Nuur" where the station is Vostok; the census L432 and L440 keep the old name and the retired founding story; `City_Cross_Subnet_Relationships.md` L176 and `City_National_Connections.md` L570 pair the city with "USA + Japan"; `Doll_Representation_Categories.md` L12 gives a Robot Universals path segment that does not match the folder. Options: (a) correct them now, before the run, each recorded; (b) list them as source fixes for after the run; (c) leave them. **Recommended, PROVISIONAL: (b),** the run's own source-fix convention; the run reads the live line and notes the error.

---

## Open since 2026-11-18 (input validation: Mawson, and the shared quick-reference sheets)

*From the validation of Mawson's pass-folder sheets and of the twelve shared quick-reference sheets they point to (`Universal_Location_Methodology/INPUT_VALIDATION_LOG_2026-11.md`). The web-search cap the Mawson sheets also state (Pre-Trip L64, L143, L434: 200 per session) is the same question as `DEC-661`.*

### DEC-667 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · Mawson, preparation
- **The README's file list.** `README.md` L12–26 leaves out `00.1_Step_MINUS-1_Input_Contract.md` and every step's round record (`…b_T8_Rounds_…`), which the Pre-Trip names (L82–83 and each step's "Round record" line). Options: (a) add them (adds lines to the README's table); (b) leave the list as it is. **Recommended, PROVISIONAL: (a).** The same gap likely sits in every city's README.

### DEC-668 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · Mawson, preparation
- **Which Calethina account Phase 10 carries.** `Datasheets/Phase_10.md` L12–14 carries `Formative_History.md` L5 word for word, the older seven-stop account, which itself holds later-era clauses (the wartime reroute, the Tower's later trauma), and excludes the Calethina README L58 and L60 as later-era; but README L58 refines L5, and its Mawson clause (request work at Mawson, commissioned as a general-knowledge host for visitors) falls inside the default scope. Options: (a) carry only L58's Mawson clause, mark L5 as the superseded account and cut its post-war clauses; (b) exclude all three; (c) leave as is. **Recommended, PROVISIONAL: (a).**

### DEC-669 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · shared sheets and method (every city)
- **Differentiation substitute 1, "its own earlier states", against the height rulings.** `04` III.4 (L517–L526) ranks it strongest ("run substitute 1 without fail") and Gate 6 (L167) says to run all four; `DR-136` item 6 and `DR-137` item 10 say no earlier-state comparison runs inside a pass, which captures a place at its height. The two shared sheets copy `04` word for word, so they carry the old instruction. Options: (a) in a pass, run substitutes 2–4 and record substitute 1 as deferred to after the pass, fixed at its source (`04` III.4, Gate 6, runbook L447) in one change and the sheets re-copied; (b) keep substitute 1, limited to the place's own record at its height; (c) leave as is. **Recommended, PROVISIONAL: (a).**

### DEC-670 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · shared sheets (every city)
- **Citing the Falkland Treaty at draft standing.** The treaty sheet L5 says to treat article text as citable working canon; Casey (`DR-136` item 11) and Relung Panen (`DR-138` item 3) were each ruled separately: findings may rest on the draft's articles, each tagged `[treaty draft]` and listed. Options: (a) state that as the practice for every city, on the sheet, pending a general ruling; (b) leave it per city. **Recommended, PROVISIONAL: (a).**

### DEC-671 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · shared sheets (every city)
- **The treaty sheet points into one city's pass file.** Falkland sheet L128: "Full statement: Davis `04_Phase_02…md` §Q.5", so a sheet every city reads sends each run into another city's pass. Options: (a) drop the pointer; the sheet already carries the corrected statement at L115–L127; (b) keep it. **Recommended, PROVISIONAL: (a).** The pass file was not opened.

### DEC-672 · ✅ ANSWERED 2026-11-18 (`DR-142`) · 2026-11-18 · shared sheets (every city)
- **May a city pass cite the national food figures in `19`?** The Division of Industry sheet now carries them (`19` §5, 2026-11-03: export supply 420,833, balance +167,541, +66%, slack 7.4%; +25% and 2.8% without the third exporter), marked "not yet ruled". Options: (a) yes, as national context only, while a city's own export or "feeds N" headcount stays not citable; (b) all citable; (c) none. **Recommended, PROVISIONAL: (a).**

## Open since 2026-11-18 (Ariun Nuur ULM run; every answer below is PROVISIONAL until you give yours)

*Filed by the run itself (`STARTUP_Ariun_Nuur_ULM_2026-11-18.md`). Each entry points to the pass file and question number where its full row sits. None blocks the run: the pass proceeds on the recommended answer.*

*All answered 2026-11-18 (`DR-143`): as recommended, except `DEC-684` (both) and `DEC-682` (widened).*

### DEC-680 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-1)
- **Question.** Is the temporal frame worded *given by standing rule* or "inferred"?
- **Recommended (PROVISIONAL).** *Given by standing rule*: the frame comes from the cited default-scope rule (DS L19–21) plus `DR-137` item 10. Neither wording changes the frame
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-1.

### DEC-681 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-2)
- **Question.** Spec L186 places the geneticist "in the present day", after the frame. Does her breakthrough fall inside this pass's frame, and how is she used?
- **Recommended (PROVISIONAL).** As written: FLAGGED, not an input until her canon entry is read (REQ-5). If her breakthrough is dated before the war, use it only as testimony of what the city can produce at its extreme, never as typical, with no date beyond that and no link to the lake (RF-6)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-2.

### DEC-682 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-3)
- **Question.** The cold-record marker (spec L178): input or output, and may it commemorate the 1983 measurement, which is the real site's history?
- **Recommended (PROVISIONAL).** Its form is PRODUCED at Phase 10, marked Proposed and rooted in the city's own lines (05 L428–429). The city knows the record through inherited station logs (`DR-25`), so marking its own cold is its own practice; it should not commemorate the real station's measurement as the city's own event, and the 1983 measurement may never be the city's identity, core value or founding logic (`DR-28` D2–D3)
- **Answer (developer, 2026-11-18, `DR-143`): as recommended, widened.** *"#2 might be relevant, because it's possible that records may have been found at the station at the time that Tepenians settled the location."* The 1983 measurement is admissible as a record the settlers found at the station (`DR-25`), and the marker may honor it as inherited; per the orchestrator's reading `DR-28` D2–D3 still bind (not identity, core value or founding logic).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-3.

### DEC-683 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-4)
- **Question.** Spec L218's overland cable: admitted by presupposition, or flagged until confirmed?
- **Recommended (PROVISIONAL).** Flagged until its own record (an `Infrastructure/` or relationship file) is read at Step 0; once confirmed, admitted as relation (G5). Whether the cable is intact stays excluded
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-4.

### DEC-684 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-5)
- **Question.** The district name honors past scientists who dedicated, "(and possibly even sacrificed)", their lives (DRL L893). Whose: the real station's, the city's own, or both? And can it ground findings?
- **Recommended (PROVISIONAL).** Until answered, a naming fact only, with no memorial practice derived from it. The ruling's sentence continues "so that Tepenians could have a city of scientific research", which leans toward the city's own scientists but does not settle it. If they are the city's own, it is an act of the city's own that starts with the city and may ground findings (`DR-25`, DRL L646); if they are the real station's, it is a naming fact only (`DR-28` D2, DRL L684) and nothing about identity follows
- **Answer (developer, 2026-11-18, `DR-143`): BOTH.** The name honors the real station's scientists and the city's own. The city's own half may ground findings (`DR-25`); the real station's half is a naming fact only (`DR-28` D2).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-5.

### DEC-685 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-6)
- **Question.** May the pass carry the "two loneliest outposts" label (spec L169)?
- **Recommended (PROVISIONAL).** Carry the joint outpost as a relation; the label stays struck. At most it may be cited as the relationship's recorded name from that relationship's own record (`DR-136` item 2), once read at its step; no characterization rests on "loneliest"
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-6.

### DEC-686 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-7)
- **Question.** Seven spec lines rank the city against others or carry a superlative across places (L10, L68, L70's opening, L93, L127, L179, L217). Strike them?
- **Recommended (PROVISIONAL).** Yes: strike them under the ONE LOCATION law and state the city's own figures flatly (mean −54.8 °C, record low −89.2 °C). Leave the spec unedited, add the lines to its revisit list, and leave any superlative to the terminal differentiation check
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-7.

### DEC-687 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-8)
- **Question.** DS declares itself a DRAFT (L5–6). How much weight do its exclusions carry?
- **Recommended (PROVISIONAL).** Treat it as a working citation map: each exclusion stands on the ruling or standing rule it cites, not on the sheet's authority
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-8.

### DEC-688 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-9)
- **Question.** Spec L147 says the founding community was "necessarily small" because "the environment cannot sustain a large population"; Census I is 441,378 (Band 4). Which governs?
- **Recommended (PROVISIONAL).** Census I governs (`DR-4`, DRL L211–212). Strike "You did not go to Ariun Nuur by accident." as a characterization; strike the reason clause as a stale line written before the census; keep a small, specialized founding wave as a founding condition only. Growth from that wave to the Census I figure through continued arrivals (brief §4 item 5) is no contradiction; it is history, built after the ULM. Add the sentence to the spec's revisit list. Phase 1 treats the hardship of sustaining 441,378 people here as a generator conflict, not as an error to smooth over
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-9.

### DEC-689 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-10)
- **Question.** Spec L30's figure gap: reserve it from adjudication, or request a check?
- **Recommended (PROVISIONAL).** Both, as written here: the table holds the final figures (brief §4 item 1); the gap is reserved from adjudication inside the pass (RF-12) and a mechanical check is requested for Step 2 (REQ-11)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-10.

### DEC-690 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-11)
- **Question.** May the pass read the mechanism and coefficients section of the file spec L95 points to, while its cross-city comparison stays barred?
- **Recommended (PROVISIONAL).** Not by a partial read: a file is admissible only if every section of it is, and the fix is upstream (05 L514–516). Recommended: split the file, mechanism and coefficients in one file the pass may read, the comparison in another left to the terminal check. Until then L95 stays excluded
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-11.

### DEC-691 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-12)
- **Question.** Spec L149, "The name was kept.", is stale against `DR-42`. How is it held?
- **Recommended (PROVISIONAL).** EXCLUDED, as written; add it to the spec's revisit list, read as *the central district keeps the name*
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-12.

### DEC-692 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-13)
- **Question.** DS's exclusion tables leave out spec L149, L153–161 (`Character & Culture`), L220, the gameplay and DLC clauses in L186, and the ranking clauses. Add them?
- **Recommended (PROVISIONAL).** Yes: add a row for each under the rules cited in §3, in a way that moves no cited line (as the sheet already does, on existing rows)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-13.

### DEC-693 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-14)
- **Question.** Spec L171 is excluded whole, but its opening clause states a pre-war fact: the outpost was too remote for its own dedicated power and ran on residual overflow from a continent-wide regulated grid. Readmit that clause?
- **Recommended (PROVISIONAL).** Yes: admit it as a pre-war network and energy fact (G5), through `Airports.md` and the grid file L171 names, read at Step 0 under `DR-138`; keep the post-war remainder and the gameplay detail excluded. Until answered, L171 stays excluded whole, as DS L35 has it
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-14.

### DEC-694 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step −1 (Q-15)
- **Question.** "500+ years of post-exile scientific access" (spec L177, L217) runs to the game's present. What span does the pass use?
- **Recommended (PROVISIONAL).** Not that one. Inside the pass, access runs from the founding to the height, undated (`DR-16`), read as *long access* only; the phrase goes on the spec's revisit list
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md` §6, Q-15.

### DEC-695 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-16)
- **Question.** How should the declaration word the **"Other cities"** line, given RM's template default (L138) against the law of one location?
- **Recommended (PROVISIONAL).** *CLOSED for the whole pass; differentiation is a terminal check on the finished corpus* (01 L512–514), as DL-16 has it; and correct RM's step numbers (REQ-21)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-16.

### DEC-696 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-17)
- **Question.** **Which three generators are the independent set?** (A: G2 · G4 · G8; B: G2 · G5 · G8; C: G2 · G4 · G7)
- **Recommended (PROVISIONAL).** G2 · G5 · G8 provisionally, the only proposal no reader's objection touches (DL-21), noting its shared spec L66; settled only under `02` §5.1 (REQ-16)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-17.

### DEC-697 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-18)
- **Question.** RF-9 bars any robot cold threshold. **May the pass cite the companion box's capacity and materials figures** (RP L12–16), which are not death thresholds?
- **Recommended (PROVISIONAL).** Not as numbers until the developer rules. Cite the costs qualitatively (capacity loss from charging in the cold; reduced capacity; output sag; embrittlement; safer moving than resting) and do not set the city's −54.8 °C mean against any figure. *Alternative (A):* the figures are national material facts, citable once the companion file is read, written as preparation and a gradient, never as a gate or a death threshold
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-18.

### DEC-698 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-19)
- **Question.** **Where does the height sit against the Act boundary?** (A: provisionally Act 2, tagged; B: the Census I period, before ~2688 ±~20, inside or just before the transition; C: undated)
- **Recommended (PROVISIONAL).** Leave the height undated in the pass; record that the governing figure dates to before ~2688 (±~20) (RF-17) and that a population peak is not necessarily the overall height; name the Act on every inheritance call; the developer places the height (REQ-1). *B's proposed form of words for identity, naming the two founding nations with "Tepenian city" (ER L65–66), is kept as population-origin material, DEMOTED, not adopted until the Act is placed*
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-19.

### DEC-699 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-20)
- **Question.** **How is RP L409 held, and should `06`'s subject scan reach non-method files required at Step 0?**
- **Recommended (PROVISIONAL).** Hold L409 as RF-26 has it: the joint staffing as a relation only through spec L169; the expertise characterization not adopted, read at Step 5 as a check, matches tagged `[SELF-ORIGINATED]`; the siting reason excluded; the power clause corroborating Q-14 without settling it; nothing post-war used. And yes, widen the scan (REQ-23); 06 L437 is true as worded, and the request only widens it
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-20.

### DEC-700 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-21)
- **Question.** **Is the national tower's name a forbidden location name** in a reader's or merge writer's text?
- **Recommended (PROVISIONAL).** Yes: a structure is a location type (01 L104), so refer to it by its role, as this file does; positional PROOF lines that carry it are copied and marked EXEMPT
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-21.

### DEC-701 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-22)
- **Question.** With the Band 4 decomposition deferred (RF-3), **how does the pass meet 01 §5.4's per-category declaration?**
- **Recommended (PROVISIONAL).** Delegated (deferred by ruling) where a category cannot be answered at base level; Patterned where base-level facts show an axis; nothing Uniform by default (01 L550), as DL-11 has it
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-22.

### DEC-702 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-23)
- **Question.** **The extent band:** declare it equal to the population band by construction, or leave it undeclared until an independent footprint exists?
- **Recommended (PROVISIONAL).** Declare *4, provisional, by construction (a required area of 44–63 km² at assumed densities, not a measured footprint)*, assert no divergence, and revisit once REQ-14 is met; an undeclared line would hide the step
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-23.

### DEC-703 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-24)
- **Question.** **Is the city `Enclosed`?**
- **Recommended (PROVISIONAL).** Leave the modifier undeclared at Step 0 and settle it at Phase 1 from the spec's physical lines (REQ-22); do not assume enclosure from the cold. If none states an envelope, record it as not stated and open, assuming neither (no forced fit). If enclosed, 01 L131's questions become obligatory, and burial stays bound by RF-14
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-24.

### DEC-704 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-25)
- **Question.** **May DS be corrected** at L5–6 (the stale clause; the pointer spliced into a sentence), L9 (the "3 of 3" count, which omits the registries half), L20 (the label broader than contract CR-16), L25 (the unverified tier; "range mid-points" beside a printed range) and L27–28 (stale at the same point as L5)?
- **Recommended (PROVISIONAL).** Yes, in place, dated, moving no cited line; the sheet stays a demoted draft (contract Q-8); L25's tier waits on REQ-19
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-25.

### DEC-705 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-26)
- **Question.** **Is the absence of a stated power source for the city a gap or a finding?** (contract REQ-6, sharpened)
- **Recommended (PROVISIONAL).** A gap: read `Geothermal_Heating.md` and the grid file at Phase 1 and Phase 5 before writing any energy finding, and assume nothing until then (PV-7)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-26.

### DEC-706 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · Ariun Nuur, Step 0 (Q-27)
- **Question.** **The wording of the "Own culture material read at" line** (RM L139 names the read-order position; the brief names Step 5)
- **Recommended (PROVISIONAL).** *Step 5, as a CHECK (the last position in the Step 0.4 read order, item 6)*, as DL-17 has it, which states where it was actually read, as the template asks
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md` §10, Q-27.

### DEC-707 · ✅ ANSWERED 2026-11-18 (`DR-143`) · 2026-11-18 · methodology maintenance (found on Ariun Nuur, Step 0.2)
- **Question.** The pin on `Disciplines/00b_General_Population_Discipline.md` is stale: the original (`Concordia-City/Districts/Phase_Instructions/00b_General_Population_Discipline.md`) now hashes `f2d0237b06885373` against the pinned `6a08080e1a8da883` (157 lines both), changed once since the pin by commit `e351f6d5` (2026-10-31, one line replaced at L97, inside a worked-instance passage the ULM copy already replaces with a pointer). Re-pin the copy?
- **Recommended (PROVISIONAL).** Yes, as maintenance outside the run: re-pin the copy's header to the new hash after confirming the changed line is one the copy carries only as a pointer. The run uses the copy as read meanwhile.
- **Where:** `RUN_PROGRESS_Ariun_Nuur.md` (held entry AN-05); `Ariun_Nuur/09.5_Log.md` AN-05.

### DEC-708 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 1 (Q-28)
- **Question.** Contract Q-14's adopted answer readmits spec L171's opening clause (the outpost ran on residual overflow from the national grid) through `Airports.md` and the grid file, but the frame carries those reads to Phase 5. **Is the clause inherited material now, or only once those files are read?**
- **Recommended (PROVISIONAL).** Inherited material now, so Step 1 audits it on its own words, as a relation; no finding rests on it until Phase 5 reads both files, and the bar on dating the outpost from it stays
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md` §7c, Q-28.

### DEC-709 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 1 (Q-29)
- **Question.** The Step 1 and 2 datasheet (L39–40) lists the inheritance classification (*Determined* / *Inflected* / *Originated* / *Aggregated*) beside the Gate 9 audit, while the runbook's Step 1 names only the asymmetry check. **Does Step 1 also classify inheritance?**
- **Recommended (PROVISIONAL).** No. Step 1 runs what its own text states; the classification goes to the step or phase whose text names it, each call naming its Act
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md` §7c, Q-29.

### DEC-710 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 1 (Q-30)
- **Question.** Inherited material first opened after Step 1 (the industry run's determined section at Step 2, the picks at Step 3, the network files at Phase 5) misses Gate 9's first run. **Who runs the check on it?**
- **Recommended (PROVISIONAL).** The step that first opens it runs Step 1's asymmetry check on it before writing, and records it; Step 7's run stays for what the pass writes. A method change if adopted (the runbook updated in the same commit). Applied provisionally in this run from Step 2 on
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md` §7c, Q-30.

### DEC-711 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 1 (Q-31)
- **Question.** The national arrival ruling (`DR-127` item 2) writes the human channel both ways (arrive; no return) but gives robots only an arrival channel open in law. **Could a robot who arrived go back?**
- **Recommended (PROVISIONAL).** A national question, outside this pass; until it is answered the pass writes nothing on a robot's return either way
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md` §7c, Q-31.

### DEC-712 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 1 (Q-32)
- **Question.** **May the inherited small, specialized founding wave (`DEC-688`) be read as a filter on who came, and so audited for who was turned away?**
- **Recommended (PROVISIONAL).** Audit it as written: an admission-shaped row whose losing side is not stated, with no criterion for *specialized* supplied; the phases that read the founding and function generators ask the question; nothing is invented before then
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md` §7c, Q-32.

### DEC-713 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 1 (Q-33)
- **Question.** A robot raised within a predominantly X population is reliably X, though not always (`DR-136` item 10); in this city no origin row exceeds 15.97%. **At what scale is *predominantly* read here, and is the other direction written in-run?**
- **Recommended (PROVISIONAL).** At the scale of the community that raised the robot, never at city scale by default; the other direction is left unwritten in-run; no characterization from row figures (`DR-130` item 7)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md` §7c, Q-33.

### DEC-714 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 1 (Q-34)
- **Question.** **Is the city's subnet assignment a membership mechanism for Gate 9?**
- **Recommended (PROVISIONAL).** Yes, for its network mechanics only (what it gives, what it costs, whether it can change), rowed at Phase 5 once the network files are read; the subnet's regional framework stays reserved and nothing is characterized from its nickname
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md` §7c, Q-34.

### DEC-715 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 1 (Q-35)
- **Question.** **The handoff sweep's counting convention:** lines in the file, or the rows of a table a line introduces?
- **Recommended (PROVISIONAL).** Count each distinct line or block that names the step, gate or check as one place, and report the rows discharged inside a block beside it; the substance does not change with the convention
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md` §7c, Q-35.

### DEC-716 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 1 (REQ-24; raised by the orchestrator)
- **Question.** **May the Step 1 and 2 datasheet (`Datasheets/Step_1_and_2.md`) be corrected in place, dated, moving no cited line?** All three readers found: L35 carries spec L149 ("The name was kept") as a naming fact, while the contract excludes it (`DEC-691`); L7's "Nothing below cites them" needs a recheck against L35; L19 carries the record framing without the contract's flag; L34 calls the station's operation "an infrastructure fact", where the contract holds it as a coordinate only; L5–6 carry the same pointer splice as the Step 0 sheet; L6 still says "when Ariun Nuur's own pass actually runs".
- **Recommended (PROVISIONAL).** Yes, in place, dated, moving no cited line, as `DEC-704` did for the Step 0 sheet; the sheet stays a demoted draft (`DEC-687`). Until then the run reads the contract, which governs
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md` §7b, REQ-24.

### DEC-717 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-36)
- **Question.** **Is *Mandated* an in-world allocation of labor, or a model tier only?**
- **Recommended (PROVISIONAL).** A model tier: a share of the workforce count serving national provider roles (16 L132). No in-world mechanism is written in-run; any allocation mechanism waits for the DCI (`DR-137` item 11)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-36 (raised by C (Q-C3); A and B on the same reading).

### DEC-718 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-37)
- **Question.** **The city's heat and power:** (a) does the power file's L16 (only six geothermal cities' heat did not depend on the grid) put this city's heat on the grid by elimination? (b) does L16 hold before about 2688, when the grid came fully online? (c) what powered the city at its height, and before about 2688?
- **Recommended (PROVISIONAL).** (a) No, not as a fact: the line is flagged, the file is a draft, and the layout is not established (L33); keep the source a gap (`DEC-705`). (b) A national question; the city pass writes nothing on its heat before about 2688. (c) Rule it, or let Phase 5 read the grid's layout after Step 3's research (S3-3); in-run nothing is assumed, and every energy finding stands on the physical need
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-37 (raised by A (Q-A5) · B (Q-B104) · C (Q-C4)).

### DEC-719 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-38)
- **Question.** **The primary pick: "CRISPR" (gene editing, as R1 reads it) or "CRISP" (an infrastructure-resilience program, R1 L32)? And were the picks chosen from the city's genetics lines (the struck L167; L186)?**
- **Recommended (PROVISIONAL).** CRISPR, as the pick is spelled and R1 reads it; research CRISP beside it at Step 3 as a second reading only if it was meant; state the picks' basis (REQ-36). Until then, CRISPR's facts support structural forms only (cluster, spin-off, retooling), and any genetics direction rests on G7 alone, PROVISIONAL (RF-43)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-38 (raised by A (Q-A3) · B (Q-B103) · C (Q-C2)).

### DEC-720 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-39)
- **Question.** **The asymmetry-row grain:** one row per finding, as merged (28), or one per source line?
- **Recommended (PROVISIONAL).** One row per finding, as merged; the readers' 16, 19 and 15 recorded; no row conflicts in substance
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-39 (raised by C (Round 3)).

### DEC-721 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-40)
- **Question.** **§23 cites "Canon §15" for Science 65 / Self-sufficiency 25 / Other 10, but the spec has no §15 block. Where is it, and do the figures stand?**
- **Recommended (PROVISIONAL).** Let the percentages stand as citable sector sizes as §23 prints them (DS12 L9), with no base applied to them; locate the block (REQ-39), and add it, or the correct pointer, to the spec's revisit list
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-40 (raised by A (Q-A4) · B (REQ-B102)).

### DEC-722 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-41)
- **Question.** **The selection moves from the provisional G2 · G5 · G8 to G2 · G7 · G8 under `02` §5.1. Confirm?**
- **Recommended (PROVISIONAL).** Yes. §5.1's own sentence names physical constraint, composition and inspiration research as the independent kind; G7 shares no admitted spec line with the other two; G5 shares L66 with G2 and L169 with G3, and its flows are still requested; it is read beside, and run at Phase 5
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-41 (raised by A (Q-A1) · B (Q-B102) · C (Q-C1)).

### DEC-723 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-42)
- **Question.** **May readers name real-world inspiration places (host towns, laboratories) in their output, or are they "another location" under the brief?**
- **Recommended (PROVISIONAL).** Admissible as G7 source citations (source, not specification), never as in-world locations; say so in the next brief. This file refers to them by role
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-42 (raised by C (Q-C6)).

### DEC-724 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-43)
- **Question.** **G8's *no predominant origin at city scale*: a strength (no origin group a newcomer must conform to) or a deficit (*predominantly X* cannot resolve at city scale)?**
- **Recommended (PROVISIONAL).** Write it once, flatly, under DEFICIT, with the strength reading recorded beside; neither reading carries a characterization
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-43 (raised by C (Round 3), on A's, B's and C's placements).

### DEC-725 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-44)
- **Question.** **The comparison table's leading readings, and which GRUDGING TOLERANCE cell is silent** (A: G8; B: G2; C: G7)
- **Recommended (PROVISIONAL).** State each row's leading reading, as here; accept the time reading for GRUDGING TOLERANCE (G8 silent), with the other two readings recorded beside; Step 3 may recheck the row once G8's derived costs are researched
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-44 (raised by B and C (Round 3)).

### DEC-726 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-45)
- **Question.** **The spine sentence:** A's (a user facility whose users stayed, paying twice), B's (nothing here may pause) or C's (only the work that is its purpose can be stopped)?
- **Recommended (PROVISIONAL).** Adopt the merged sentence in §4, PROVISIONAL. B's is not used, because the pick's instruments pause on a schedule, as B accepted for the cost cell
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-45 (raised by A (Round 3)).

### DEC-727 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-46)
- **Question.** **The shape's counting grain, and whether a quadrant's *direction* (the cost quadrant rising with institutions admitted) is reportable as part of a shape**
- **Recommended (PROVISIONAL).** Name the shape by count only (*Balanced* on both sets), never on weight alone; report the rising quadrant beside the name as a note, not as part of it, with each reader's counts kept
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-46 (raised by A (Round 3) · B (Q-B102; Round 3) · C (Q-C7; Round 3)).

### DEC-728 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-47)
- **Question.** **Which inherited material counts as known institutional particulars for `02` §4.0's double reading?**
- **Recommended (PROVISIONAL).** The city's own institutions named in its own lines (the research program L167, the outpost and its power L169–171, the shaft and facilities L177, the archive L179) and the industry model's verdicts about them (Mandated, the forced-importer label, §23's sector sizes); physics, composition and the national physiology stay in the withheld set; C's split stays an extra reading
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-47 (raised by B (Round 3)).

### DEC-729 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-48)
- **Question.** **The address count: does a deficit from a generator beside the three (the lost living institution, G4) enter the count, and is the merged count accepted?**
- **Recommended (PROVISIONAL).** No; record it beside with its earned address (nowhere at all). Accept the merged count: 9 deficits, 8 addresses (in the parent 3, nowhere at all 1, diffuse 4), water unassigned
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-48 (raised by B (Round 3, two points)).

### DEC-730 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-49)
- **Question.** **What does the spec's daylight column mean: a monthly mean, or the day length near mid-month?**
- **Recommended (PROVISIONAL).** State it in L121's column provenance. The values fit the mid-month day length (February 24 h, August 0 h); if a monthly mean is meant, February and August need recomputing; compute both at Step 3 (S3-8)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-49 (raised by A (Q-A6; Round 3) · C (Round 3)).

### DEC-731 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-50)
- **Question.** **Spec L111 calls July the coldest month; the record's August mean is colder. Correct the note?**
- **Recommended (PROVISIONAL).** Yes, at source, dated, citing the record (August −66.9, July −65.9), and keeping July as the month of the record low
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-50 (raised by B (Q-B105)).

### DEC-732 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-51)
- **Question.** **Is Ariun Nuur enclosed? Is *not stated; open* the settlement `DR-143` item 5 meant?**
- **Recommended (PROVISIONAL).** Yes: leave *Enclosed* neither declared nor denied in this pass, and record it as open. If the developer rules it enclosed (or partly), `01` L131's envelope questions become obligatory at that point, with burial still bound by RF-14
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-51 (raised by A (Q-A2) · C (Q-C5)).

### DEC-733 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-52)
- **Question.** **Is §23's mandated headcount (71,444) an export headcount under the citation gate?**
- **Recommended (PROVISIONAL).** Cite the Mandated share as a tier size of the distinctive split, and the count only as §23 prints it beside the determined section; rest no finding on the count
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-52 (raised by B (Q-B101; Round 3) · A (Round 3)).

### DEC-734 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 2 (Q-53)
- **Question.** **The handoff-sweep counting convention** (A 26, B 30, C 52). The same substance as Step 1's Q-35, among `DEC-708` to `DEC-716`, unanswered
- **Recommended (PROVISIONAL).** Answer Q-35 as recommended (each distinct line or block is one place, with the rows discharged reported beside it); this file uses it: 72 places, 71 row labels
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md`, Questions for the developer, Q-53 (raised by A, B and C (Round 3)).

### DEC-735 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-54)
- **Question.** **Which basis does the pass use for the body's altitude:** the standard atmosphere (about 3,900 m; 3,825–4,060 by month) or West's low-latitude equation (about 4,120 m; 3,980–4,280)?
- **Recommended (PROVISIONAL).** State the measured pressure flatly (624.2 hPa; monthly about 612–638), and the standard-atmosphere equivalent beside it as arithmetic, seasonal; give West's only as a second reading with his low-latitude caveat
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-54 (raised by A (Round 3) · B (Q-B104; Round 3) · C (Q-210; Round 3)).

### DEC-736 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-55)
- **Question.** **Does the shaft's life-support (FIND-10) qualify the spine sentence's *only the work that is its purpose can ever be stopped*?**
- **Recommended (PROVISIONAL).** Keep the sentence; add the qualifier at Phase 3 once the shaft's form in the city is known
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-55 (raised by A (Round 3) · B (Q-B103) · C (Round 3)).

### DEC-737 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-56)
- **Question.** **Correct spec L70's lake length (about 250 km) to the published about 230 km?**
- **Recommended (PROVISIONAL).** Yes, at source, dated: *about 230 km long and up to 50 km wide*, citing the altimetry literature
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-56 (raised by C (Q-205) · A (Round 3)).

### DEC-738 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-57)
- **Question.** **The record high at L81:** −14.0 °C (1974) as printed, or −13.6 °C (1957)?
- **Recommended (PROVISIONAL).** Keep −14.0, flagged as conflicted, until the operator's own list is read (REQ-51)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-57 (raised by C (Q-203) · A and B (Round 3)).

### DEC-739 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-58)
- **Question.** **Carry the union of Unrecognized Instrument candidates (UI-1 to UI-7) as PROPOSED for the phases that write the outdoors, the day, the archive and the supply?**
- **Recommended (PROVISIONAL).** Yes, each reserved (RF-53, RF-54, RF-62, RF-63, RF-68 to RF-70), none written as practice
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-58 (raised by C (Q-208; Round 3) · B (Q-B106)).

### DEC-740 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-59)
- **Question.** **Is the real site's stake grid admissible as inherited infrastructure the settlers may have found** (`DR-24`, `DR-25`)?
- **Recommended (PROVISIONAL).** Yes, as physical site infrastructure; whether the city kept or used it is its own and stays reserved (RF-69)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-59 (raised by C (Q-207) · A and B (Round 3)).

### DEC-741 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-60)
- **Question.** **UI-2 (the science's waste heat) and UI-7 (the plant's rejected heat) sit close to the bar on energy findings without a known source (`DEC-705`). Hold them?**
- **Recommended (PROVISIONAL).** Hold both as conditional candidates, written only once Phase 5 knows the source; no energy finding rests on either
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-60 (raised by B (Round 3) · A and C (Round 3)).

### DEC-742 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-61)
- **Question.** **Drop the spec's falls/lands split (L88–90) in favor of the two measured figures** (22 mm precipitation; 22.5 kg m⁻² a year accumulation)?
- **Recommended (PROVISIONAL).** Yes, unless the mechanism file holds a sourced coefficient for this site (REQ-47)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-61 (raised by A (A-Q-3) · C (Round 3)).

### DEC-743 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-62)
- **Question.** **The handoff-sweep counting convention** (A 30, B 46, C 52), the same substance as Step 1's Q-35 (`DEC-715`)
- **Recommended (PROVISIONAL).** Answer `DEC-715` as recommended (each distinct line or block is one place, row labels reported beside it); this file uses it: 64 places, 82 row labels
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-62 (raised by A, B and C (Round 3)).

### DEC-744 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-63)
- **Question.** **Where does the line fall between the real station's site and its life?** May its own sources be used for practice; may its incidents serve as failure-mode comparables; and may facts from accounts of a traverse that starts at another station be used?
- **Recommended (PROVISIONAL).** Site, infrastructure, the kinds of work it does and the physical behavior of its infrastructure are admissible (pressure, accumulation, ice flow, the borehole's behavior, stores, the skiway, crews' measured physiology as a physical fact about the site); crew life, events, incidents and the operator's matters are not; traverse facts from accounts starting at another station are not used, as here
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-63 (raised by A (A-Q-2; Round 3) · B (Q-B102; Round 3) · C (Round 3)).

### DEC-745 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-64)
- **Question.** **Does a URL whose host or path carries another location's name count as naming it?** And may real-world places be named as source citations?
- **Recommended (PROVISIONAL).** No: a URL is a citation kept in its own spelling, and this file's prose never repeats the name. Real-world places as citations stand on `DEC-723`, PROVISIONAL, never as in-world places
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-64 (raised by B (Round 3; Q-B107) · C (Round 3)).

### DEC-746 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-65)
- **Question.** **The primary pick:** CRISPR as spelled, or CRISP? When and on what basis were the picks set?
- **Recommended (PROVISIONAL).** CRISPR as spelled; CRISP recorded as a second reading only (FIND-28); state the picks' date and basis (REQ-53) so RF-43 can be settled
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-65 (raised by A (A-Q-1) · C (Q-206)).

### DEC-747 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-66)
- **Question.** **`DEC-697` bars setting the city's mean against a figure for robots. May the pass set the monthly means beside engineering ratings for outdoor machinery** (grease, steel, hydraulic fluids, turbines)?
- **Recommended (PROVISIONAL).** Yes, for machinery and materials only (spec L126), never for robot bodies, and never as a robot threshold
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-66 (raised by B (Q-B101)).

### DEC-748 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-67)
- **Question.** **Correct the spec's climate block at source** (REQ-48: L115's November note, L111's coldest month, L121's daylight provenance and a provenance line per column, L96–97's start dates)?
- **Recommended (PROVISIONAL).** Yes, at source, dated, citing READER, the box's primary sources and the computed sun; counts unchanged
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-67 (raised by B (Q-B105) · C (Q-201, Q-202, Q-204) · A (A-REQ-2)).

### DEC-749 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Step 3 (Q-68)
- **Question.** **Reader C's call 42 search string named another station. How should the log carry it?**
- **Recommended (PROVISIONAL).** Redacted in the log, recorded as a self-correction, nothing used from it (§3.2); add a reminder line to future research briefs
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md`, Questions for the developer, Q-68 (raised by C (Q-209) · A (Round 3)).

### DEC-750 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-69)
- **Question.** May the founding wave's *assigned* mode rest on the treaty draft's station-assignment article (TD L54, Art. II.3.2), which is not locked canon, with the Register's geography and access as the arrangement's content here?
- **Recommended (PROVISIONAL).** Yes, tagged `[treaty draft]` and listed (`DR-142` item 3), as a national mechanism; the founders themselves stand on the Register, which is canon; no motive is invented, and whether the founders experienced it as a placement or an agreement stays unwritten
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-69 (raised by A (Q-A1), B (Q-B106)).

### DEC-751 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-70)
- **Question.** The draft treats a later human elector as a founding elector for all purposes of the treaty (TD L50, Art. II.2.5), and the assignment clause covers the whole departing population (TD L54, Art. II.3.2). Did later human arrivals choose this city, or were they placed in it?
- **Recommended (PROVISIONAL).** Write *chose Tepenia; the city's part unstated*; settle neither in-run. If the developer rules, the assignment clause most naturally reads as the founding-era allocation (*in the years following* the signing), which would make later arrivals' choice of city their own
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-70 (raised by C (Q-C201); A (REQ-A7)).

### DEC-752 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-71)
- **Question.** Correct the Phase 2 datasheet in place, dated, moving no cited line: L16 (the no-representation verdict, true of the core state only; the stale deferral clause), L19 (the summary's stale tie of exile to the time before the treaty) and L7 (*3 of 3*, which reaches two addresses only through sheets not on the list)?
- **Recommended (PROVISIONAL).** Yes, as REQ-62; the sheet stays a draft citation map (`DEC-687`)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-71 (raised by C (Q-C207); A (REQ-A5); B (REQ-B103)).

### DEC-753 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-72)
- **Question.** Where do requests a phase cannot meet (the language mapping's basis; the census's names section) go: to the orchestrator before Step 5, or to Step 10?
- **Recommended (PROVISIONAL).** Before Step 5, because Phases 8 and 9 may need the language tier sooner; Step 10 lists any still open before any claim of readiness
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-72 (raised by A (Round 3, marked c); B and C (Round 1 routes)).

### DEC-754 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-73)
- **Question.** With no birth and no local making written, does the pass write the born-here mode as a null, or may it write the research's reading that a place people cannot leave keeps its births, aging and deaths (research FIND-25, reserved as RF-64)? The Child and the Elder positions turn on the answer
- **Recommended (PROVISIONAL).** As a null in-run (*none is sited here*, never *none is possible here*); FIND-25's reading stays reserved until the developer or a later phase writes births; the Child and the Elder stay unmarked until then
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-73 (raised by B (Q-B104; Round 3, marked c); A and C (the Child, Round 3, marked c); B (the Elder, Round 3, marked c)).

### DEC-755 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-74)
- **Question.** The draft is silent on a human born in Tepenia entering, or being recognized in, Assembly territory. How is it held?
- **Recommended (PROVISIONAL).** A national question; the pass writes nothing either way
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-74 (raised by A (Q-A4)).

### DEC-756 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-75)
- **Question.** Russia (the core state) is absent from the composition at every tier, not only as a founder. Is that intended, and is the Register's *Not founders* column ever a characterizing absence for this city?
- **Recommended (PROVISIONAL).** Intended as written; record it once as a fact of the Register and the table, draw nothing from it, and never the station as a cause (`DR-19`; NNS L7); confirm at the post-ULM census review
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-75 (raised by B (Q-B105), C (Q-C206; Round 3, marked c)).

### DEC-757 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-76)
- **Question.** Runbook §C.9b constraint 2 (RB L2120–2121) calls whether robots carry a national origin an open reserved question, while `DR-11`, `DR-128` item 1, `DR-136` item 10 and `DR-137` item 7 rule on it. Is the line stale?
- **Recommended (PROVISIONAL).** Yes: the rulings govern, and the line's route (origin reaches a robot through the local community) stands with them; update the line after the run, in a methodology commit, recording what was learned and on which city (REQ-66)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-76 (raised by B (Q-B101), C (Q-C203)).

### DEC-758 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-77)
- **Question.** May a tier sum (Primary 28.36, Significant 69.48, Notable 2.15) be stated under `DR-12` and `DR-130` item 7?
- **Recommended (PROVISIONAL).** Yes, as arithmetic on printed weighting, flatly, with no finding resting on it; findings rest on tier membership and row counts only
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-77 (raised by A (Q-A5)).

### DEC-759 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-78)
- **Question.** The census defines Primary as the tier that shapes the city's primary linguistic and cultural identity (census L36), but here Hawaiian is dominant and English alone supports, and neither Primary row's bloc is in the tier (though Japanese is a primary base of Hawaiian). Which governs, and how is the definition read?
- **Recommended (PROVISIONAL).** `DR-100` governs language; read the tier labels as weighting only (`DR-12`), never as a claim about the language of dealings; add a dated note at the census definitions, and add the definition's linguistic clause to the post-ULM census review
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-78 (raised by A (Q-A6), B (Q-B102), C (Q-C208)).

### DEC-760 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-79)
- **Question.** May the national language's bases be written as structure of the native and transplanted layers (which stocks' tongues are bases, which are not), and may that be expressed as how a resident of a given stock meets the language of dealings?
- **Recommended (PROVISIONAL).** Write the bases and the blocs flatly, one bloc at a time, as composition arithmetic; never as a resident's experience, since a resident's language is never read from her row (`DR-136` item 10); language practice is the CST's
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-79 (raised by C (Round 3, marked c); A (Round 3 objection)).

### DEC-761 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-80)
- **Question.** Is *fled to it* a mode of any human arrival here? The files never frame an arrival as flight; the election's grounds (partnership, parenthood, a life among robots) have the taxonomy's shape of flight but are national
- **Recommended (PROVISIONAL).** No, at city scale: write *not given as such*; keep the national reading as a note only, true of every exile and never this city's distinction; the preamble is not a basis
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-80 (raised by B (Round 3, marked c), C (Round 3, marked c); A (note)).

### DEC-762 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-81)
- **Question.** The robots' founding arrival (a class departure followed by an assignment, with no finding of wrongdoing) fits none of the seven modes. Record it as not fitting and describe it as the articles write it, or fold it into *fled to it*, *sentenced to it* or *assigned*?
- **Recommended (PROVISIONAL).** Record it as what it is, national; fold it into none (the article denies the punitive reading, and *fled* implies a choice); coin no mode, and change the spine's taxonomy only if the developer wants an eighth mode
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-81 (raised by A (Q-A2), C (Q-C202)).

### DEC-763 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-82)
- **Question.** Where did the robot majority come from? Is it mostly built in Tepenia, and as a rule here, on a small founding wave, no recorded later robot arrival from Upper Earth and 284,693 robots at Census I; or does the ruling's *grew by later arrivals* govern?
- **Recommended (PROVISIONAL).** Hold the national rule (fabrication city and home city are, as a rule, the same place) as bearing, PROVISIONAL with frame PV-5, unsized and never this city's distinction; leave the source unrecorded in the pass, stated as such; where built (here, or elsewhere and then moved) stays open until REQ-68 and REQ-61 are met
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-82 (raised by A (Q-A3; Round 3, marked c), B (Q-B103; Round 3, marked c), C (Q-C204)).

### DEC-764 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-83)
- **Question.** The differentiation axis: *assigned specialist wave, arrival-grown* (written), *Assigned specialists, outgrown by arrivals*, *Specialist posting, never rotated*, or a merged form such as *unrotated specialist posting, arrival-grown*? All three pass the peer-free test only in part, the assignment and the missing rotation being national
- **Recommended (PROVISIONAL).** Adopt *assigned specialist wave, arrival-grown*, PROVISIONAL, with the weakness stated; revisit once Phase 3 knows the specialization (RF-29) and Phase 5 the arrival routes (RF-77); the terminal differentiation check reads it later
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-83 (raised by A (Q-A7; Round 3, marked c), B (Q-B107; Round 3, marked c), C (Q-C205; Round 3, marked c)).

### DEC-765 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 2 (Q-84)
- **Question.** Do the treaty's grounds for the founding election (partnership with a robot; children borne or raised in a robot household) cover the Lover (position) and the Parent for this phase, national only?
- **Recommended (PROVISIONAL).** Yes, marked covered, national only and `[treaty draft]`, never as this city's character
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md`, Questions for the developer, Q-84 (raised by C (Round 3, marked c); A and C (covered); B (accepted in Round 3)).

### DEC-766 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-85)
- **Question.** **The concept-art folder was listed by the orchestrator, not by a reader. May the receipt mark it opened-and-empty?**
- **Recommended (PROVISIONAL).** Yes, as *opened, by the orchestrator's listing*, with the listing's date; an orchestrator's listing counts as a look
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-85 (raised by B (Q-B105); A (Round 3)).

### DEC-767 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-86)
- **Question.** **The brief numbers asymmetry rows from 73, while reader ranges number every other series from 101 and 201. Which governs?**
- **Recommended (PROVISIONAL).** The brief's row numbers for asymmetry rows, shared by all readers (as at Phase 2's row 52); reader ranges for every other series
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-86 (raised by B (Q-B107)).

### DEC-768 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-87)
- **Question.** **Spec L68's clause "among the most hostile environments on Earth's surface": a superlative across places to strike, or a general real-world comparable to keep?**
- **Recommended (PROVISIONAL).** Not used as a basis either way (all three readers agree). Add it to the spec's revisit list beside contract Q-7's ranking sentence, for the developer to strike or keep; meanwhile the place's own figures are stated flatly
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-87 (raised by A (Q-A6), B (Q-B104), C (Round 3)).

### DEC-769 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-88)
- **Question.** **May a phase compute sensory physics from constants a reader recalls (the specific heat of air, about 1.005 kJ/kg·K; ice's, about 1.9 kJ/kg·K averaged from a table; the humidity of heated air), or must every such figure come from a cited source?**
- **Recommended (PROVISIONAL).** From a cited source wherever the figure carries a finding (LAW 0-R). A standard constant used only to recompute a figure the research already sourced may stand if the text names it as recalled; the humidity of heated air waits for REQ-75
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-88 (raised by B (Q-B102); C (Round 3, indoor dryness and the 1.005 value)).

### DEC-770 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-89)
- **Question.** **May the supply's sound, and silence as its alarm, stand with no acoustic data?**
- **Recommended (PROVISIONAL).** Not as a finding: as a conditional reserved finding (RF-93) until the supply's audibility is written; research the acoustics (REQ-70) before any practice
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-89 (raised by A (Q-A3); B, C (Round 3)).

### DEC-771 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-90)
- **Question.** **Does a robot who does not breathe have a sense of smell?**
- **Recommended (PROVISIONAL).** A national question. Until it is ruled, the pass writes the smell register as the human minority's on the files as they stand, and never asserts that robots lack smell (RF-94; REQ-73)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-90 (raised by A (Q-A1); B (REQ-B102), C (REQ-C5) as requests).

### DEC-772 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-91)
- **Question.** **May the inherited borehole's fill fluid (kerosene with a densifier) ground a smell for the city's shaft?**
- **Recommended (PROVISIONAL).** Only conditionally, as written: the borehole and its equipment are inherited (`DR-25`; contract CR-29), but whether the city kept the fluid is its own and unwritten; no smell is written as fact until it is (RF-95)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-91 (raised by C (Q-C2); A (RF-A4), B (B116)).

### DEC-773 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-92)
- **Question.** **May the pass write that a lab's once-through air keeps no smell of its own?**
- **Recommended (PROVISIONAL).** Only as a PROPOSED inference, marked as one and conditional on the city's labs following the once-through form; never as a finding of fact
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-92 (raised by A (Round 3)).

### DEC-774 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-93)
- **Question.** **May the pass write that frozen breath marks the human minority outdoors?**
- **Recommended (PROVISIONAL).** Yes, as physics and national canon, flatly, at the record cold only (spec L126); never as a characterization of either body or a basis for any status (RF-96)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-93 (raised by C (Q-C4); narrowed in Round 3 by A).

### DEC-775 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-94)
- **Question.** **Does "Science, almost entirely." (spec L167) describe the city's purpose or the make-up of its day?**
- **Recommended (PROVISIONAL).** Its purpose: the street's texture is survival's and the institutions' is science's; the 65% stays a share of an unstated base (REQ-39); Phase 4 reads it against the ordinary day
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-94 (raised by C (Q-C5)).

### DEC-776 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-95)
- **Question.** **May Phase 3 write that the places that keep things sit apart from the places where people stay?**
- **Recommended (PROVISIONAL).** No: no store siting rule is written as fact before Phase 5 (research RF-60); this phase writes the physics only (FIND-P3-49, FIND-P3-69)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-95 (raised by C (Round 3)).

### DEC-777 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-96)
- **Question.** **Research Q-55's qualifier (*only the work that is its purpose can ever be stopped*, except perhaps the shaft) was to be added at Phase 3 once the shaft's form in the city is known. It is not known. Where does it go?**
- **Recommended (PROVISIONAL).** Keep the spine sentence; carry the qualifier to Phase 10 with REQ-74, written as conditional until the developer gives the shaft's form
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-96 (raised by B (Q-B103)).

### DEC-778 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-97)
- **Question.** **May Phase 3 say what became of the inherited station's build at the height (raised, sunk, built over)?**
- **Recommended (PROVISIONAL).** No; nothing listed says. Write the burial rate and both directions; the developer or Phase 10 settles it (RF-99; REQ-69)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-97 (raised by A (Q-A2); B (REQ-B104), C (REQ-C4) as requests).

### DEC-779 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-98)
- **Question.** **Which Retroactive Mechanism leads?** (F-1 the shimmer is the snowfall; F-2 the lake and the flatness, narrowed; F-3 and F-4 the archive; F-5 the shaft)
- **Recommended (PROVISIONAL).** Keep all five, since none contradicts another. Lead with the archive (F-3 and F-4 together): spec L179 is the plainest *simply true, explained by nothing* in the files, and two readers chose it independently, by different systems. F-1 second, as it carries the axis; F-2 and F-5 as candidates
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-98 (raised by A, B (Round 3)).

### DEC-780 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-99)
- **Question.** **The differentiation axis: *Snow without weather*, *Clear-sky snow, made warmth*, *Silent sky, audible upkeep* or *Silent sky, stoppable purpose*?**
- **Recommended (PROVISIONAL).** *Snow without weather*, PROVISIONAL, with the peer-free answer *in part* and its weakness stated; the terminal differentiation check reads it later
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-99 (raised by A (Q-A5), B (Q-B106), C (Q-C3); all three in Round 3).

### DEC-781 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-100)
- **Question.** **Is the Mentor covered at this phase?**
- **Recommended (PROVISIONAL).** Yes, on FIND-P3-40 (the newcomer's warning must come from someone who already knows) and FIND-P3-52 (the archive's understanding passes person to person), both this phase's own content; B withdrew its objection in Round 3. Until answered, it is not marked
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-100 (raised by A, C (Round 3); B (Round 1)).

### DEC-782 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 3 (Q-101)
- **Question.** **What do the ledger's Lover faculty and Elder need, to be marked covered?** This phase writes what one might love here (the air's glitter, the long light) and a cost rising with years lived, but no listed line defines either term
- **Recommended (PROVISIONAL).** Leave both unmarked until the definitions are on a list; mark a position covered only when the phase's own content reaches a person in that position, not a quality of the place. Record the candidates (FIND-P3-37, FIND-P3-67; FIND-P3-27)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md`, Questions for the developer, Q-101 (raised by A (Q-A4), B (Q-B101), C (Q-C1)).

### DEC-783 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-102)
- **Question.** **May the industry model's FREE share (40.9%) or distinctive share (60.6%) be read as the part of a working life *not spoken for by survival*, as RP reads `09` §3.5 (L364–367)?**
- **Recommended (PROVISIONAL).** Not in-run. `16` counts heads, not hours (L27), and `09` is superseded as a result (`16` L6, L30–32). State §23's shares flatly as the model's headcount shares, every robot plus half the humans; read no free hours, leisure or liberty from them; revisit once `09` §3.5 is read at source (REQ-81)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-102 (raised by A (Q-A1; Round 3 (c)) · B (Q-B101) · C (Q-C202)).

### DEC-784 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-103)
- **Question.** **REQ-9's founding motive is still unwritten after Phases 2 and 4. Leave it to the developer?**
- **Recommended (PROVISIONAL).** Yes. No motive is derived in-run; Phase 2's candidates stay PROPOSED; listed open at Step 10
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-103 (raised by A (Q-A7)).

### DEC-785 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-104)
- **Question.** **Frame RF-20 (robot-only work for safety): carried, answered in part, or not applicable at Phase 4?**
- **Recommended (PROVISIONAL).** Carried, to Phase 9 and Step 7: no admitted line sites any work as robot-only, and the day writes each body's cost, not an allocation (place 42)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-104 (raised by A (Round 3 (c))).

### DEC-786 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-105)
- **Question.** **Do Phase 3 places that reach Phase 4 only *as 5* belong in Block 1 or Block 2 of the sweep?**
- **Recommended (PROVISIONAL).** Block 2, as `DEC-715` already filed stands; they do not name Phase 4 in their own words. This file counts them there (places 79–82)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-105 (raised by C (Round 3 (c))).

### DEC-787 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-106)
- **Question.** **May the cold file's charge-spiral mechanism (recovery impossible alone below some charge level) be used in words beside `DEC-697`?**
- **Recommended (PROVISIONAL).** Yes, in words, as a charge condition and never a temperature, with no figure (row 82; FIND-P4-17)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-106 (raised by A (Q-A4)).

### DEC-788 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-107)
- **Question.** **Is the permanent capacity loss from a cold charge, read as one robot's bad decision, a shadow candidate (SH-13)?**
- **Recommended (PROVISIONAL).** Yes, as a candidate, weaker than textbook because repair is open in the source (cold file L137–138); checked at Step 7
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-107 (raised by A (Round 3 (c)); B concurred).

### DEC-789 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-108)
- **Question.** **Does *every city staffs its own clinicians, always* (institutes L16, as brief §4 item 16 states it) mean, for a city that cannot send students away, staffing by graduates who arrive and stay?**
- **Recommended (PROVISIONAL).** Yes, as the institutes file reads with the plateau problem (L231–233): permanently dependent on graduates arriving when travel is possible; write the dependence as a fact, never a shortage, until Phase 5 reads the road
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-108 (raised by B (Q-B104)).

### DEC-790 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-109)
- **Question.** **DS4 L26–28 says the population-specific days wait for the stage after the cultural synthesis, while this phase's brief asks for each body's and arrival layer's day. Which wording governs?**
- **Recommended (PROVISIONAL).** The brief's, read with `DR-137` item 8: the ULM writes each body's and layer's day as structure (what it is organized around, what it costs, when time is free, whom it fails); what each population does in its day waits. Correct DS4's wording to say so (REQ-83)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-109 (raised by C (Q-C201); B concurred in Round 3).

### DEC-791 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-110)
- **Question.** **The headline test: would *Science, almost entirely* reasonably be someone's entire day, every day, forever?**
- **Recommended (PROVISIONAL).** No, on the files' own figures: the research population's size is not citable and Science's 65% has no stated base; in every reading the phase writes away from the function the same way (FIND-P4-1)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-110 (raised by A (Round 3 (c)); B withdrew its yes).

### DEC-792 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-111)
- **Question.** **The shared night is national canon. With no sky for about 243 days, what sets it here: one national hour, or the city's own clock?**
- **Recommended (PROVISIONAL).** The clock; write neither its hour nor who sets it until ruled (REQ-84; the DCI; RF-105)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-111 (raised by A (Q-A6) · B (Q-B103)).

### DEC-793 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-112)
- **Question.** **How is whoever keeps the life support through the shared night written?**
- **Recommended (PROVISIONAL).** As a function only (keeping heat, water, charge and the shaft running through the stop), never a title (`DR-137` item 12); rosters, numbers and rest rules wait for the DCI and Phase 7. As written here (FIND-P4-8), after Round 3
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-112 (raised by A (Q-A3); B, and C in Round 3).

### DEC-794 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-113)
- **Question.** **May the robot term's split (maintenance about 3,559, sustenance about 925, from `16` L2358's printed coefficients) be cited?**
- **Recommended (PROVISIONAL).** Yes, as baseline load arithmetic with its basis stated (raw coefficients, no city factor); no headcount of a trade and no characterization
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-113 (raised by B (Q-B105)).

### DEC-795 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-114)
- **Question.** **May a phase join two national facts (a robot is safer moving than resting outdoors; a robot who works all the time is virtually guaranteed to go insane) into a city-level tension at this place's light regime, and is the robot who never stops a shadow candidate (SH-16)?**
- **Recommended (PROVISIONAL).** Yes to both, as PROPOSED and in words, with the medical link marked flagged and not ruled (RP L344–348; REQ-91), no rule or illness written, and the shadow checked at Step 7
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-114 (raised by B (Q-B102; Round 3 (c))).

### DEC-796 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-115)
- **Question.** **May the tension between flight mode (saving siligel) and keeping warm be written as a PROPOSED inference?**
- **Recommended (PROVISIONAL).** Yes, marked as an inference, beside the point that flight mode is not rest, with no rate or threshold, and checked at Phase 9 (FIND-P4-29)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-115 (raised by A (Q-A2) · C (Round 3 (c))).

### DEC-797 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-116)
- **Question.** **The differentiation axis: *The warm stop, kept by the clock*?**
- **Recommended (PROVISIONAL).** Adopt it, PROVISIONAL, with the peer-free answer *in part* and its weakness stated; it covers both bodies, where *the warm charge night* narrows it to the robots'; the terminal differentiation check reads it later
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-116 (raised by A (Q-A8; Round 3 (c)) · B (Q-B106; Round 3 (c), recommending A's wording) · C (Q-C203; Round 3 (c))).

### DEC-798 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 4 (Q-117)
- **Question.** **Does this phase's content cover the Neighbor (through rescue by someone near, or through the shared night, both bodies stopping side by side)? The Mentor is covered by all three readers.**
- **Recommended (PROVISIONAL).** Not yet: leave it unmarked at this phase. The shared night describes a time and rescue a need for someone near; neither writes a person as neighbor. Revisit when a phase writes who rests near whom
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md`, Questions for the developer, Q-117 (raised by A (Q-A5; Round 3 (c)) · B (Q-B107; Round 3 (c)) · C (Q-C204; Round 3 (c))).

### DEC-799 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-118)
- **Question.** **The national-connections file lists five outward relations for this city, each naming another location, reasoned from withheld megasheets and other cities' culture conclusions, in a frame after the national tower's completion. Is any of them admissible to a ULM pass, and should the city's section be rebuilt?**
- **Recommended (PROVISIONAL).** No, as the file stands: its method reads conclusions, not attributes. If any relation rests on a shared thing in the city's own lines (a road, an airfield, a shared outpost), re-ground it there and add it to that thing's own record; never drop it, and never read it from the file. Rebuild the section from canon network lines only, after the ULM
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-118 (raised by A, B (C recorded it as put to the developer)).

### DEC-800 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-119)
- **Question.** **The three readers' sweeps counted handoff places at different grains (148, 144 and 155 places; one block or one row per *as H-83* line; Block 1 or Block 2 for a line reaching the phase by reference). Which grain governs?**
- **Recommended (PROVISIONAL).** `DEC-715`'s: one row per distinct line or block, the union of all readers' places; a line reaching Phase 5 only by reference to another row is its own place in Block 2. Followed here: 166 places
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-119 (raised by A, B (each marked (c))).

### DEC-801 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-120)
- **Question.** **Where the readers' handoff discharges differ (for example, the siligel role at frame L252: carried against answered in part; the energy comparables at research L105, L155, L218 and L389: closed as not applicable against answered in part), which is written?**
- **Recommended (PROVISIONAL).** The one that closes less: carried over answered in part over answered; answered in part over closed. Followed here (the siligel role carried; the comparables answered in part, since no finding rests on them but their holding for the developer remains)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-120 (raised by C (marked (c) on both)).

### DEC-802 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-121)
- **Question.** **The national network file's L26 places this city among places with *basically no* network access, on a line cut mid-sentence at the admitted span. Does it describe the city at its height, a post-war state or a gameplay modifier? And does the overland cable to the subnet's hub exist?**
- **Recommended (PROVISIONAL).** Hold L26 FLAGGED and rest nothing on it until its full sentence is read (REQ-98); keep the cable FLAGGED until its record is read (REQ-95). If the near-absence is an altitude condition of the height and the cable exists, the cable is the city's one information link and FIND-P5-9, FIND-P5-27 and FIND-P5-48 narrow to *one cable*; if neither holds, FIND-P5-48's condition is met
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-121 (raised by A, B, C).

### DEC-803 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-122)
- **Question.** **This phase's asymmetry rows are numbered from 102, the brief's shared numbering, while every other series ran in each reader's own range. Which governs?**
- **Recommended (PROVISIONAL).** The brief's shared row numbers for asymmetry rows, as Phase 3's Q-86 recommends; one merged sequence for every other series. Followed here
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-122 (raised by C).

### DEC-804 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-123)
- **Question.** **May a phase rest a finding on a datasheet's restatement of source lines outside its admitted span (the corridor's seasonal closure, altitude, residents and one stopping place, datasheet L33)?**
- **Recommended (PROVISIONAL).** No. Carry it as the sheet's statement, conditional, and read the lines at source before any finding (REQ-97); a datasheet is a citation map whose rows stand on the lines they cite (`DEC-687`)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-123 (raised by A, B, C (A's first answer, PROVISIONAL use, withdrawn in Round 3)).

### DEC-805 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-124)
- **Question.** **The outpost's origin (a gift of means from member cities of the subnet, the city and its partner staffing it) names other locations. Is it admissible as a relation and as the outward half of the relation?**
- **Recommended (PROVISIONAL).** Yes, as the outpost's own record (`DR-131` item 3; `DR-136` item 2), with every giver unnamed, the givers written as inside the city's own subnet (relationship database L49) and not as coastal, and no characterization of any giver
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-124 (raised by C).

### DEC-806 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-125)
- **Question.** **Airports L18 carries the phrase *two loneliest outposts* as what the outpost expressed. May it be cited as the relationship's recorded name under `DEC-685`?**
- **Recommended (PROVISIONAL).** No: it stays struck. The airports file is the outpost's record, not the relationship's own, and the phrase carries a superlative across places
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-125 (raised by C).

### DEC-807 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-126)
- **Question.** **Airports L18 says a moderate share of both plateau populations came up from three cities (members of the Mirny subnet by relationship database L49) to do research. May the pass use that sentence as an arrival route, a population tie, apart from the census-kinship paragraph it sits in?**
- **Recommended (PROVISIONAL).** Yes, flatly, as a relation from a shared thing's own record (`DR-131` item 3; phase spine L636; `DR-138` item 1), PROVISIONAL, unsized and undated; written as from member cities of the city's own subnet, never as coastal; the kinship reasoning stays unused (RF-16), and the diaspora reading is not adopted
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-126 (raised by A, B, C).

### DEC-808 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-127)
- **Question.** **May the Hwy 22 corridor line (relationship database L135, inside another location's entry), read with Highways L156, ground a road from the city to its own subnet's cities?**
- **Recommended (PROVISIONAL).** Only as a PROPOSED route reading, a relation on a shared road, with no distance, travel time or practice; its post-war bypass proposal is not used
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-127 (raised by C (marked (c)); A and B accepted it in Round 3).

### DEC-809 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-128)
- **Question.** **Is the city's only air link the shared airfield on Hwy 37 (Airports L52, L56; datasheet L19)?**
- **Recommended (PROVISIONAL).** Yes, as the files write it; whether the city kept the real site's skiway as an unlisted strip stays reserved (spine RF-41), pending REQ-99
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-128 (raised by B).

### DEC-810 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-129)
- **Question.** **The outpost was *too remote to have its own dedicated power infrastructure*. Does that say the plateau cities had dedicated power, or that the plateau lacked it?**
- **Recommended (PROVISIONAL).** Neither, inside the run; put it with spine Q-37, and write no energy finding until the developer rules or the grid's layout is given (REQ-96)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-129 (raised by C).

### DEC-811 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-130)
- **Question.** **What the city believes about its parent: a null (C), a reading of *alone* against *singly connected* (A), or a new provisional assumption that its working relation is with the nation along Hwy 37 (B)? And in what form is frame PV-8 revised for Gate P?**
- **Recommended (PROVISIONAL).** A null, since no admitted line writes the belief and spec L159 is read only at Step 5; A's and B's readings kept as the files' structure, not as belief, with no new PV. PV-8 revised in A's form, which all three readers now accept: the subnet's member cities supplied people and means, not a route
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-130 (raised by A, B (each marked (c))).

### DEC-812 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-131)
- **Question.** **May the conversion mechanism be written at Phase 5, given that teaching practices are reserved; and is the conversion made by arrival order (C) or by the newcomer's first teaching (A, B)?**
- **Recommended (PROVISIONAL).** Yes, as one mechanism with no practice, ceremony or named moment, PROPOSED, checked by Gate 9 at Step 7: the turn of instruction, made possible by arrival order and marked by her first teaching, with the research and waypoint forms beside it
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-131 (raised by A (marked (c)), B).

### DEC-813 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-132)
- **Question.** **The food dependence: a shadow already held (A), half-named (B), or named only by a model (C)?**
- **Recommended (PROVISIONAL).** Written in C's wording, which B accepts: named only by a model, by nobody in-world; held under spine D-1 and SH-6, with no new shadow number
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-132 (raised by C (marked (c), on the label only)).

### DEC-814 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-133)
- **Question.** **The city's power: a dependency nobody names, so a shadow candidate (A, B), or a gap in the files, not a shadow (C)?**
- **Recommended (PROVISIONAL).** A gap in the files, as written: the source is unwritten, so no in-world awareness can be read either way. Enter it as a shadow only if the developer rules the city's supply (spine Q-37) and the ruling leaves its place on that supply unnamed in-world
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-133 (raised by A, B, C (each marked (c))).

### DEC-815 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-134)
- **Question.** **Does the city mine, process or receive siligel?**
- **Recommended (PROVISIONAL).** Receive, by shipment along Hwy 37, as PV-6 assumes, unless the developer rules that the site's ice or bedrock gives a source; no network line says otherwise
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-134 (raised by A).

### DEC-816 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-135)
- **Question.** **The differentiation axis: *Parented on paper, supplied by the road* (C), *Necessary, and carried by one road* (B), or *One road in, no network: a subnet member reached only by the nation's highway* (A)?**
- **Recommended (PROVISIONAL).** Adopt *Parented on paper, supplied by the road*, PROVISIONAL, with the peer-free answer *in part* and its weakness stated; it claims least, since A's rests on the network line now held FLAGGED; revisit once the road's seasons and the network line are read; the terminal check reads it later
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-135 (raised by A, B, C (each marked (c))).

### DEC-817 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 5 (Q-136)
- **Question.** **Is the Neighbor covered by the partner city's people working beside the city's own at the waypoint?**
- **Recommended (PROVISIONAL).** Yes: it writes people of the next city on the road as colleagues at a shared site, which Phase 4 (Q-117) found missing; the partner city stays unnamed
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md`, Questions for the developer, Q-136 (raised by C).

### DEC-818 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-137)
- **Question.** **Is the load-bearing thing a social contract with a debt inside it, or a debt?**
- **Recommended (PROVISIONAL).** A social contract with a debt inside it, owed forward and never back, with *being needed* as its standard of worth; all three named, none promoted into a creed (reader B's debt reading is the debt inside it)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-137 (raised by A (Q-A3), B (Q-B102), C (Round 3); all three marked (c)).

### DEC-819 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-138)
- **Question.** **The district's honor.** (a) Is *possibly even sacrificed* (contract L52, citing DRL L893) meant literally of the city's own scientists, and is any of them to be named? (b) Does the honor extend to the city's dead in general? (c) May Phase 6 use the city's own half as a debt and a record? (d) Do the real station's record-writers stand as creditors of the city's debt?
- **Recommended (PROVISIONAL).** (a) Not decided in-run: read the clause as the ruling's own wording; write no death of any scientist and name no one (RF-8) until the developer says; the form is Phase 10's. (b) No: it names scientists who gave their working lives to the research. (c) Yes, as a debt and a record, with no rite, no named person and no boundary drawn. (d) No: the station's half stays a naming fact only (`DR-143` item 1), as written here
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-138 (raised by C (REQ-C203, Q-C201), A (Q-A4; Round 3 addendum, marked (c)), B (Round 3, marked (c), the record-writers as creditors)).

### DEC-820 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-139)
- **Question.** **Who handles a robot death in this city,** where national canon names religion and community and no faith is sited?
- **Recommended (PROVISIONAL).** Not in-run: state the national rule only; name no local handler or practice until RF-14 is ruled and the stage after the cultural synthesis reads the physiology lines at source (REQ-105)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-139 (raised by A (Q-A5; Round 3, marked (c)), B (Q-B104), C (Q-C203)).

### DEC-821 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-140)
- **Question.** **Which of the phase spine's four reasons for an absence of the dead applies here?**
- **Recommended (PROVISIONAL).** None chosen in-run; record the fourth (a holder's death thinning the understanding the city exists for, with no signal) as the one candidate the files support, decided with RF-14 at the later stage
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-140 (raised by A (Q-A6), B (Round 3, marked (c)), C (Round 3, marked (c); REQ-C206)).

### DEC-822 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-141)
- **Question.** **Are the keepers of the heat, outside the city's one written honor, a shadow candidate,** or is that reading too far from files that write no honor for anyone but scientists?
- **Recommended (PROVISIONAL).** A candidate, weaker than textbook, checked at Step 7; the spine's own sentence (spine L229) is its basis
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-141 (raised by C (Q-C204), B (Round 3, marked (c))).

### DEC-823 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-142)
- **Question.** **Does the purpose yield first when the two promises compete for the one supply?**
- **Recommended (PROVISIONAL).** Keep it as a PROPOSED inference from spine L224 and spine §4 with Phase 3 FIND-P3-18; write no rule (Phase 7) and no energy source (`DEC-705`); Step 7 checks SH-22
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-142 (raised by B (Round 3, marked (c), on A's finding)).

### DEC-824 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-143)
- **Question.** **The archive's teaching: vertical transmission tied to survival, or copy-the-product drift?**
- **Recommended (PROVISIONAL).** Keep both as PROPOSED readings of different layers: the survival layer as transmission the cold checks (A, B), the archive layer open to the drift reading (C) as the one candidate for the layer the cold does not check; no practice; Step 5 checks them against the city's own files
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-143 (raised by B (Round 3, marked (c)); C (its own FIND-P6-216, reader numbering); A, B (rows)).

### DEC-825 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-144)
- **Question.** **The differentiation axis:** *Taught by paper, owed in person* (C), *Kept by the earlier arrival, owed to the next* (A), or *Owed forward: where to stop* (B)?
- **Recommended (PROVISIONAL).** *Taught by paper, owed in person*, PROVISIONAL, with the peer-free answer *in part* and its weakness stated, *paper* naming the founding's condition and never a creditor; the terminal differentiation check reads it later
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-144 (raised by A (Q-A7; Round 3 recommends C's), B (Q-B105), C (Q-C205); all three marked (c)).

### DEC-826 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-145)
- **Question.** **The Block 2 handoff counts differ by grain (A 22 places, B 20, C 27).** Which count stands?
- **Recommended (PROVISIONAL).** The union, counted by `DEC-715`'s convention, as written here: 30 places in Block 2, 33 in all
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-145 (raised by C (Round 3, marked (c))).

### DEC-827 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-146)
- **Question.** **How does the receipt label `MUST OPEN` addresses checked by the orchestrator, not by a reader?**
- **Recommended (PROVISIONAL).** *Recorded through brief §4 item n, not opened by a reader*, with the check's date, as Phase 3's Q-85 recommends; a reader opens them at the stage after the cultural synthesis if the developer wants them marked opened (REQ-104)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-146 (raised by A (Q-A1, REQ-A1), C (REQ-C202)).

### DEC-828 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-147)
- **Question.** **May the Naming technique take register words from the pass's own earlier outputs, or only from the spec and the rulings?**
- **Recommended (PROVISIONAL).** Yes, as the brief allows the earlier outputs, marking which are canon lines and which pass outputs, and resting the classification on canon lines only
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-147 (raised by A (Q-A2)).

### DEC-829 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-148)
- **Question.** **May the name's gloss (*pure* against *sacred*) enter the Naming technique?**
- **Recommended (PROVISIONAL).** No, as RF-2 has it: record it as the one religious-register word in the city's own name, barred, and build nothing on it until the gloss is settled
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-148 (raised by B (Q-B101); C (RF-C206)).

### DEC-830 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-149)
- **Question.** **Phases 4 and 5 handed counterculture seeds to Phase 6. Does this phase write countercultures, or only name who the load-bearing thing leaves out?**
- **Recommended (PROVISIONAL).** Only name them, as seeds named by what they lack, with real-world mechanisms as mechanism only; no movement, faction, doctrine, leader or counterculture form is written
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-149 (raised by B (Q-B103), C (Q-C206)).

### DEC-831 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 6 (Q-150)
- **Question.** **DS6 L21–23 says Phase 6 records only the checked roster facts; the brief asks also for the non-devotional load-bearing thing, death as a question and the failure state. Which governs?**
- **Recommended (PROVISIONAL).** The brief, read with `DR-140` item 2: faith, holidays and doctrine wait; the contract, the death question and the failure state are written as structure. Correct the sheet's wording, dated, moving no cited line (as Phase 4's Q-109)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md`, Questions for the developer, Q-150 (raised by C (Q-C202); A agreed (Round 3 addendum)).

### DEC-832 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-151)
- **Question.** B (Q-B108); A, B Round 3 (c); C Round 3 (a)
- **Recommended (PROVISIONAL).** **How is a `MUST OPEN` address that the orchestrator checked by name labeled in *Canon opened*** (the theoretical-calculations, staffing, jobs, megacorporations and factions folders), and is the factions folder RECORDED or REFUSED?
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-151 (raised by *Recorded through brief §4 item 17, not opened by a reader*, as Phase 6's Q-146 recommends, the factions folder included; its entry's grounds stay not admitted).

### DEC-833 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-152)
- **Question.** A (Q-A4); C (Q-C209)
- **Recommended (PROVISIONAL).** **The city's genetics research folder is tagged for Phase 7 by the runbook's registry, and the run keeps it closed. Which governs, and what becomes of the tag?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-152 (raised by The run's closure, for this pass (brief §4 item 18); retire the Phase 7 tag in a methodology commit after the run, or move it to the stage the developer names, recording what was learned and on which city; open the folder, if ever, only under its own ruling).

### DEC-834 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-153)
- **Question.** C (Q-C207)
- **Recommended (PROVISIONAL).** **README L103 calls the distinctive tier free for export work; here §23 keeps survival infrastructure inside it as not provider work. Is the distinctive tier the city's spare capacity?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-153 (raised by No: read README L103 as the national method's ceiling; the city's spare capacity is not stated, and nothing is characterized from the ceiling).

### DEC-835 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-154)
- **Question.** A (Q-A7)
- **Recommended (PROVISIONAL).** **Does the Science share include any care work?** The README warns that a *Technical/scientific* share elsewhere included medicine and double-counted care (L206)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-154 (raised by Not decided in-run; no care count is derived from Science; care is written as formed elsewhere (FIND-P7-33)).

### DEC-836 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-155)
- **Question.** A (Q-A1); B (Q-B101); C (Q-C201); A, B, C Round 3 (c); B's Round 3 (c) on band variance
- **Recommended (PROVISIONAL).** **May §23's sector shares be applied to the distinctive tier and the per-sector counts cited** (science ≈142,888, survival infrastructure ≈54,957, other ≈21,983), given that DS7 L7 states the gate's form and that the half-the-science reading (DS7 L29) reproduces §23's printed mandated and FREE counts exactly? This would lift the spine's Q-40 answer, *no base applied*
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-155 (raised by Not in-run: keep the arithmetic as a check, its basis stated; once REQ-120 and REQ-121 confirm §23's lines and the gate at source, cite the counts as the gate allows, as model units (robots plus half the humans), never as people, never as the research population, with the earlier phases' lines left as written and this phase's reading recorded beside them for Step 10).

### DEC-837 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-156)
- **Question.** B (Q-B102); A (Q-A2, its premise half)
- **Recommended (PROVISIONAL).** **DS7 L31's reason for the mandate rests on a closed-population premise that `DR-127` item 2 and `DR-130` item 1 withdrew. Does the 19.7% mandate stand, and may the premise be used?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-156 (raised by The mandate stands as §23 prints it (brief §2); the premise is not used; flag its reason as stale, write no in-world reason, and revisit the share in the post-ULM industry review (SH-27)).

### DEC-838 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-157)
- **Question.** A (Q-A2, its subject half; Round 3 (c)); B (Q-B103); C (Q-C202)
- **Recommended (PROVISIONAL).** **Is the export subject §23's note names for the city canon at its height, from what source, and may it be named in a pass?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-157 (raised by Not in-run: do not name it in the text; write the export as knowledge and research capacity from the program (spec L167; FIND-P7-5); keep the datasheet's quotation as kept (`DR-142` item 12); settle the subject with spine RF-43 once REQ-123 has found its source and the picks' provenance is known).

### DEC-839 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-158)
- **Question.** B (Q-B104); A Round 3 (c) on B's SH-B101 and C's SH-C201
- **Recommended (PROVISIONAL).** **The survival sector sits in FREE (DS7 L33). Is that intended, how is FREE named in a pass, and is the placement a shadow or perceived at source?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-158 (raised by Intended as the model's convention (FREE is the distinctive tier not mandated); always name it *the model's FREE tier*, never free time; keep it a finding (FIND-P7-7), not a shadow, since its own source states it outright; revisit at Step 7's shadow count).

### DEC-840 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-159)
- **Question.** A (Q-A3); B (Q-B105); C (Q-C203)
- **Recommended (PROVISIONAL).** **Is the chamber work at the waypoint the city's non-thematic export, or is the slot a null?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-159 (raised by A null: the chamber work was made off the city's ground with others' means on surplus power and is not emotionally neutral; write the null and its consequence, name nothing for the Other sector, and ask whether anything ordinary leaves the city (REQ-124)).

### DEC-841 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-160)
- **Question.** C (Q-C204)
- **Recommended (PROVISIONAL).** **Is *what is unadministrable* (no rule enforceable by removal; no one able to decide for the archive as a whole; no one written as having first call on the supply, the road or arrivals) a governance finding barred by `DR-137` item 11?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-160 (raised by No: it records where a decision cannot fall or is not written to fall, which is the *where decisions fall* the ruling permits; no authority, form or rule is written).

### DEC-842 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-161)
- **Question.** A Round 3 (c) on its SH-A1; B, C (a)
- **Recommended (PROVISIONAL).** **Is the archive governed by no one a shadow candidate?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-161 (raised by Yes, as SH-29, weaker than textbook; no adverse outcome is written).

### DEC-843 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-162)
- **Question.** A (Q-A8; Round 3 (c) on its SH-A2); B Round 3 (c)
- **Recommended (PROVISIONAL).** **The national shared night is a physiological pattern in its source, and it cannot hold for everyone here. May the pass write *the national pattern, broken here by necessity*, and is that a shadow?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-162 (raised by Yes, as structure (FIND-P7-20), with no rule written for the keepers; hold the shadow question until Step 7, where it can be read beside Phase 4 SH-15).

### DEC-844 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-163)
- **Question.** C Round 3 (c)
- **Recommended (PROVISIONAL).** **May a prohibition rest on the treaty draft's article on certain devices and waste, as the power file reports it (spine row 37)?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-163 (raised by Not until the article is read at source (REQ-126); `DR-142` item 3 admits articles only, and Phase 5 refused this basis).

### DEC-845 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-164)
- **Question.** A (Q-A5); C (Q-C206); A Round 3 (c) on C's judgment
- **Recommended (PROVISIONAL).** **May the phase write the price of exclusion (lethal outside heated space for both bodies; a long road out of the city; no destination for a human beyond the nation) as its sanction-proportionality record, and may it say whether the place could pay that price for any offense?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-164 (raised by Yes to the price, as written (FIND-P7-23): a price only, in words for robots, never a sanction, penalty, offense or practice, undeveloped, not absent (`H42`); no to the second part: no offense is written, so whether the place would pay the price is left unwritten).

### DEC-846 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-165)
- **Question.** B Round 3 (c)
- **Recommended (PROVISIONAL).** **Are the survival rules the explained ones (every arrival is told them) or the ones nobody needs to state (the cold enforces them)?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-165 (raised by Both, as FIND-P7-31 has it: they are told to every arrival, and the cold enforces them; no rule is written).

### DEC-847 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-166)
- **Question.** B (Q-B106); C (Q-C205); A, B, C Round 3 (c)
- **Recommended (PROVISIONAL).** **May 7d name candidate populations and functions that perform what the place cannot, or apply its own rule more literally, while `DR-58` holds factions back, and which candidate, if any, leads?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-166 (raised by Yes, as populations and functions the demand does not fit, PROPOSED, sympathetic and reserved, with no person, faction, name, leader or practice; none leads in-run; check them at Step 5 against the city's own files).

### DEC-848 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-167)
- **Question.** A (Q-A9)
- **Recommended (PROVISIONAL).** **Is the contradiction between groups or inside each person?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-167 (raised by Both, as FIND-P7-42 has it: inside each person for survival; between groups only at being needed, along the research line).

### DEC-849 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-168)
- **Question.** B (Q-B109)
- **Recommended (PROVISIONAL).** **Phase 7's band variance names Bands 1 and 6 only. How is a Band 4 city written?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-168 (raised by As FIND-P7-44: the thin shared layer and its maintenance written as functions, decisions Patterned by where they fall, Delegated by place).

### DEC-850 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 7 (Q-169)
- **Question.** A (Q-A6); B (Q-B107); C (Q-C208); A, B, C Round 3 (c)
- **Recommended (PROVISIONAL).** **The differentiation axis: *An order that cannot send anyone away*, or a wider wording?**
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md`, Questions for the developer, Q-169 (raised by Adopt *An order that cannot send anyone away*, PROVISIONAL, with the peer-free answer *in part* and its weakness stated; keep the other two wordings on record for the terminal differentiation check).

### DEC-851 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-170)
- **Question.** **The `MUST OPEN` address is the whole `Robot_Biology_and_Culture/` folder. Does the physiology file, read whole, satisfy it for a city pass?**
- **Recommended (PROVISIONAL).** Yes, for the rule's purpose (no siligel or coolant claim before reading it); record the folder as opened in part, and list the cold companion, in words only, and the composition research, not canon, for the stage that writes robot food (REQ-127)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-170 (raised by A (Q-A1); B and C by request).

### DEC-852 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-171)
- **Question.** **Labels that differ only as labels.** Gear catalogs were written *not on this list* (A), *refused, by the brief's gate* (B) and *refused, by the brief* (C); slang was written *n/a* (A), *waits* (B) and *refused by ruling* (C). Which labels does the developer want for these two rows?
- **Recommended (PROVISIONAL).** Gear catalogs: *not on this list; none opened or written here*; slang: *waits for the CST (`DR-140` item 2)*: the forms that claim least and fit the brief, as written in *Canon opened* here; recorded where the orchestrator checked them
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-171 (raised by B (Round 3, c: gear catalogs); C (Round 3, c: gear catalogs and slang)).

### DEC-853 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-172)
- **Question.** **The brief holds gear catalogs back until the 38-city corpus is done, and the orchestrator found no canon line gating them. Is the hold a ruling?**
- **Recommended (PROVISIONAL).** Confirm it as a ruling, or name the line that holds it, and add it to the phase spine's `MUST OPEN` block, so later passes inherit it at the point of use and a receipt can cite canon rather than a brief (REQ-128)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-172 (raised by A (Q-A2); B (Q-B103; linked to its Round 3 c)).

### DEC-854 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-173)
- **Question.** **Asymmetry-row grain.** The readers rowed the same first-opened material at different grain (A 11 rows, B 9, C 14), with no conflict of substance. Which grain governs?
- **Recommended (PROVISIONAL).** Union at the finest grain any reader used, as this merge does (16 rows); if the grain question already filed governs, this stands on that question's recommended answer
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-173 (raised by A (Round 3, c, noting it as already filed); B (Round 3, c)).

### DEC-855 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-174)
- **Question.** **The brief numbers asymmetry rows from 171 for all readers, while each reader numbers every other series in its own range. Which governs?**
- **Recommended (PROVISIONAL).** The brief's shared row numbers for asymmetry rows, as Phase 3's Q-86 recommends; reader ranges for every other series
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-174 (raised by B (Q-B105)).

### DEC-856 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-175)
- **Question.** **The phase spine asks what a place cooks, sings, wears, builds, plays and says; `DR-140` items 2–3 defer those forms to the CST. Is Phase 8, for every city, a conditions-only phase until the CST?**
- **Recommended (PROVISIONAL).** Yes: write what the conditions require and allow, function first, in each category, and list every form for the CST at Step 10; note the phase spine's *Asks* line in a methodology commit after the run
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-175 (raised by C (Q-C206)).

### DEC-857 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-176)
- **Question.** **May Phase 8 write that a robot's siligel intake here rises with her cold exposure, in words, with no rate?**
- **Recommended (PROVISIONAL).** Yes, as a condition from RP L489–491 and the place's own temperatures as the spec prints them, never a rate, quantity or threshold (RF-9; `DEC-697`)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-176 (raised by B (Q-B101)).

### DEC-858 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-177)
- **Question.** **Does siligel keep in the cold, as frozen human food does?**
- **Recommended (PROVISIONAL).** A national question; write nothing on siligel stores until ruled (REQ-131)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-177 (raised by C (Q-C203)).

### DEC-859 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-178)
- **Question.** **Coolant's make-up.** The spine puts a robot's coolant on the same melt-and-heat account as drinking and washing (spine L114), while no admitted line states coolant's composition. Is the spine's line a fact about coolant's make-up?
- **Recommended (PROVISIONAL).** Read it as the spine's PROPOSED reading; write coolant as a drink taken at warm stops, and its liquid as a heat bill only conditionally on a water-based formulation, with no figure, until REQ-132 is answered
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-178 (raised by C (Round 3, c; Q-C201); A (Q-A5)).

### DEC-860 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-179)
- **Question.** **Is the city's place on the national glitch-coolant variety-and-potency axis (RP L279–285) a ULM question or the CST's?**
- **Recommended (PROVISIONAL).** The CST's: it is the drinking scene, and placing a city on that axis reads it against other cities; the ULM writes only that the drink is taken at a warm stop
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-179 (raised by B (Q-B102)).

### DEC-861 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-180)
- **Question.** **Language names that are also demonyms:** may a pass write the name of a tongue (for the Japan row, the Korea row, the founders' rows) where the brief bars demonyms?
- **Recommended (PROVISIONAL).** Write language names only for Hawaiian and English, as the brief does; write every other tongue as *the tongue of the X row*; confirm in the next brief (settled so in Round 3 by all three readers)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-180 (raised by C (Q-C202)).

### DEC-862 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-181)
- **Question.** **What marks someone as from here.** The files give two structural lines (Phase 5 FIND-P5-34, FIND-P5-35). Is the mark *having been taught where to stop* (A), *being the one who tells* (B), or both (C)?
- **Recommended (PROVISIONAL).** Write both, as structure only, PROPOSED, as FIND-P8-32 does: knowledge of the warm stop and the turn of instruction; no speech form; accent, dialect, code-switching and slang wait for the CST; Gate 9 at Step 7 asks of whoever never tells
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-181 (raised by B (Round 3, c); A (Q-A3); B (Q-B104)).

### DEC-863 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-182)
- **Question.** **May Phase 8 take the weapons and tools philosophy's categories (ice tools in every household, core drills, coolant-tending tools) as what the place requires of tools, given that the file is cross-media philosophy?**
- **Recommended (PROVISIONAL).** Yes, as national categories in their civilian identity, applied to the city's own conditions, with no item, catalog, weapon or named tool; the war-era and TV material is not used
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-182 (raised by C (Q-C204)).

### DEC-864 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 8 (Q-183)
- **Question.** **The differentiation axis wording:** *Carried in, kept frozen, paid for in heat* (C), *Made in paid heat, kept in free cold* (A), or *Made at the warm stop, from what the road brings* (B)? All three answer the peer-free test *in part*.
- **Recommended (PROVISIONAL).** Adopt *Carried in, kept frozen, paid for in heat*, PROVISIONAL, with the peer-free answer *in part* and its weakness stated, since it carries all three readings' halves (what comes by the road, what the cold keeps, what heat costs); the terminal differentiation check reads it later
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md`, Questions for the developer, Q-183 (raised by A (Round 3, c; Q-A4); B (Round 3, c); C (Round 3, c; Q-C205)).

### DEC-865 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-184)
- **Question.** **Frame PV-4 left the relations baseline's class to the phase that uses it. Is it Determined or Inflected here?** (A and C wrote Inflected; B Determined as the baseline, inflected by physics only)
- **Recommended (PROVISIONAL).** Inflected, in cost only: the baseline's content stays as supplied and is never re-invented; the city's own lines bend it beneath by the place's physics (the skew in cost, one supply, arrival order), never by standing or a social mechanism, which wait for the DCI; confirm once the class definitions are read (REQ-142)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-184 (raised by A (Q-A3) · B (Q-B102; Round 3, marked c) · C (Q-C201; Round 3, marked c)).

### DEC-866 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-185)
- **Question.** **Is there a category here that matters more than kind, and is it the order of arrival, with being needed at the research edge?**
- **Recommended (PROVISIONAL).** Yes, as structure, PROPOSED: arrival order decides who teaches whom and who has become a member; kind decides what each pays; no rank, title or status is written, and Gate 9 at Step 7 checks its losing side
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-185 (raised by A (Q-A2) · B (Q-B101)).

### DEC-867 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-186)
- **Question.** **May the pass declare that the spine's outer-city lens (robot culture anchored in the founding population the Register names) does not hold for this city, because the founders are 7.90% of the stock and no row predominates?**
- **Recommended (PROVISIONAL).** Yes, stated outright, as FIND-P9-1: anchor both kinds in the place's shared constraint, origin carried at the raising community's scale as ancestry, Act open
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-186 (raised by B (Q-B103); C agreed in Round 3).

### DEC-868 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-187)
- **Question.** **The human lens: is the no-return exclusion part of the local anchor, or national context only?**
- **Recommended (PROVISIONAL).** National context only, as FIND-P9-3 writes it: it is true of every human in the nation, so it does not localize
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-187 (raised by B (Round 3, marked c); A and C (C accepting A's reading in Round 3)).

### DEC-869 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-188)
- **Question.** **The physiology file's L448 makes a place's sensory lean that place's own finding, from its own needs. May the pass write this city's lean, or does frame RF-25 hold it reserved?**
- **Recommended (PROVISIONAL).** Keep RF-25 for this pass: list the needs (FIND-P9-17; RF-188), write no lean, and let the developer rule or a later stage derive it once the work's make-up is sized; the candidate *no strong lean* reading stays PROPOSED only
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-188 (raised by A (Q-A1) · C (Q-C203)).

### DEC-870 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-189)
- **Question.** **The Lover (position) and the Parent: does the national founding (partnership with a robot; children raised in a robot household; the nation sorted by whom people loved) cover them at this phase, national only?**
- **Recommended (PROVISIONAL).** Not marked at this phase: the reading is contested here, and Phase 2 already records both covered, national only and `[treaty draft]` (Phase 2 Q-84); nothing new is marked
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-189 (raised by A (Q-A4) · B (Round 3, marked c) · C (accepted A's reading in Round 3)).

### DEC-871 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-190)
- **Question.** **Is a founding-wave robot still present at the height the Elder position, and may the pass write her as a layer?**
- **Recommended (PROVISIONAL).** Not marked and not written as present until the height is placed (`DEC-698`) and the Elder is defined (Phase 6 REQ-107); keep FIND-P9-21 conditional
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-190 (raised by C (Q-C204; Round 3, marked c)).

### DEC-872 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-191)
- **Question.** **May a robot built here be counted, in the order of instruction, as an arrival on the day she comes online?**
- **Recommended (PROVISIONAL).** Yes, as structure, conditional on a chamber (PV-5), PROPOSED: no admitted line gives fabrication the knowledge of where to stop, and the Language Module gives language only (physiology L426); Gate 9 checks it at Step 7
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-191 (raised by C (Q-C205; Round 3, marked c); B's FIND-P9-106 reaches nearby ground).

### DEC-873 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-192)
- **Question.** **The human population renewed only by the road rests on the born-here null. Write it, or reserve it?**
- **Recommended (PROVISIONAL).** Write it as conditional and weaker, as FIND-P9-26, reserved as RF-186; revisit if births are written (Phase 2 Q-73)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-192 (raised by C (Q-C208)).

### DEC-874 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-193)
- **Question.** **May the pass write that, outdoors, the body best suited to go out to a stopped robot is a robot, since a human's whole stay is the cost?**
- **Recommended (PROVISIONAL).** No, not in that form: write the narrower reading of FIND-P9-41, that neither body is self-sufficient outdoors (the robot's charge margin, the human's clock) and that no preference for robot rescuers is written; Step 7 checks it
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-193 (raised by B (Q-B109) · A (Round 3, marked c, near RF-20) · C (Round 3, b)).

### DEC-875 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-194)
- **Question.** **Are the three shadow candidates (SH-35, standing by arrival with no end to arriving; SH-36, the human's night unheard and taught across kinds; SH-37, the human minority held by the road) to be kept?**
- **Recommended (PROVISIONAL).** Keep all three, each weaker than textbook, checked at Step 7 (SH-36 with spine RF-50)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-194 (raised by B (Q-B104) · C (Round 3, marked c)).

### DEC-876 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-195)
- **Question.** **May the doll categories be recorded as *none sited here* for Anthros, Elves and Aliens in a city pass?**
- **Recommended (PROVISIONAL).** Yes, flatly, with the national fact that no character is assigned to any of them; never *none possible here*
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-195 (raised by B (Q-B105)).

### DEC-877 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-196)
- **Question.** **Ch. 14's rule that fabrication and home city are, as a rule, the same place: may a pass cite it as bearing on its robots, unsized?**
- **Recommended (PROVISIONAL).** Yes, as national canon, PROVISIONAL with frame PV-5, unsized, never the city's distinction (as Phase 2 Q-82 recommends)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-196 (raised by B (Q-B106)).

### DEC-878 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-197)
- **Question.** **Does the shared place of rest, where a human's breath is the only breath beside charging robots, cover the Neighbor?**
- **Recommended (PROVISIONAL).** Not yet: it is written conditionally; revisit when a phase writes who rests beside whom (REQ-141)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-197 (raised by B (Q-B107)).

### DEC-879 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-198)
- **Question.** **The datasheet's L15 cites `DR-131` item 2 (a later-era robot's row records her raising community's origin stock as ancestry). May Phase 9 use it?**
- **Recommended (PROVISIONAL).** Not until it is read at source (REQ-136); until then the brief's §4 item 7 governs
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-198 (raised by C (Q-C206)).

### DEC-880 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-199)
- **Question.** **May the outpost's shipped chambers ground a population finding (the city's making entering robots' Gen elsewhere), given RF-18 and RF-26?**
- **Recommended (PROVISIONAL).** Yes, as a relation from spec L169 read with Ch. 14, with no Mark named, no date drawn and no expertise characterized (FIND-P9-14)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-199 (raised by C (Q-C207)).

### DEC-881 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-200)
- **Question.** **The differentiation axis wording: *Ordered by arrival, billed by body* (A), *Kind sets the bill; arrival order sets the place* (B) or *Kind sets the price; arrival sets the place* (C)?**
- **Recommended (PROVISIONAL).** Adopt *Ordered by arrival, billed by body*, PROVISIONAL, with the peer-free answer *in part* and its weakness stated: of the three it claims least, naming arrival as an order every resident moves through rather than a place anyone holds; the substance is the same in all three; the terminal differentiation check reads it later
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-200 (raised by A (Q-A5; Round 3, marked c) · B (Q-B108; Round 3, marked c) · C (Q-C202; Round 3, marked c)).

### DEC-882 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-201)
- **Question.** **The dual tags differ in grain between readers (genuinely emergent findings: A 3, B 9, C 8; several depth tags). Which grain governs?**
- **Recommended (PROVISIONAL).** The tag that claims less, as written in section D, where readers differed on a shared finding (inherited over adapted, adapted over emergent, surface over deep); no shared finding's substance turns on the tag
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-201 (raised by A (Round 3, marked c, against B and against C) · B (Round 3, marked c) · C (Round 3, b, on the human lens's tag)).

### DEC-883 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-202)
- **Question.** **Handoff labels that differ only as labels: Phase 2 L345 (a reason clause), Phase 7 L328 (the parked check), and the sweep's count grain**
- **Recommended (PROVISIONAL).** L345 closed as not applicable, its substance at place 1; L328 not applicable for this phase, the check staying parked, no population sized from it; the count follows `DEC-715` as filed (each line its own place), which stands
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-202 (raised by B (Round 3, marked c, on L345) · A and C (Round 3, marked c, on L328) · C (Round 3, marked c, on the counts)).

### DEC-884 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 9 (Q-203)
- **Question.** **Does a positional PROOF line that carries a person's working name need an EXEMPT line?**
- **Recommended (PROVISIONAL).** No: a person's working name is not a kind the brief forbids (a sign, a symbol, another location, a demonym); an EXEMPT line there is unneeded but harmless, and nothing changes
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md`, Questions for the developer, Q-203 (raised by A (Round 3 addendum, marked c, on C's spec PROOF block)).

### DEC-885 · PROVISIONAL · 2026-11-19 · Ariun Nuur, Phase 10 (raised by the developer's own question)
- **Question.** Phase 10's process B researches the city's *full pick list, prioritizing the lower tiers*. The official list is three picks (`Inspirational-Influences.md` L92–95). A candidate list of 85 drafted rows plus one developer-added row (`Reference/Real-World/Inspiration_Place_Research/candidates/Ariun_Nuur.md`, drafted 2026-10-26 from knowledge, unverified; all 86 rows shown 2026-10-27, no decision recorded except *CRISPR: keep as is*) was never adopted. Should any of the candidates count as picks for this pass's Phase 10 research, or for a later pass?
- **Recommended (PROVISIONAL).** This pass researches the three official picks only (Phase 10 and its research supplement, 2026-11-19); the 86 candidates are reviewed with the developer afterward, and any adopted pick is researched then and reconciled at Step 5 or a later pass.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_brief_04_Phase10R.md` §4 item 1; `RUN_PROGRESS_Ariun_Nuur.md`, 2026-11-19.
- **Status, 2026-11-20 (pointer, not a rewrite):** superseded by **LAW 0-P** (developer, 2026-11-19: *"Codify as a law to incorporate the entire inspiration picks list items into the research."*); the candidate rows are researched in Phase 10R2 (`RUN_PROGRESS_Ariun_Nuur.md`, 2026-11-20). To be filed as `DR-144`.

### DEC-886 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (orchestrator ruling, Round 3)
- **Question.** Phase 10's brief asked for a Planet + Element determination (task item 8, B3) while its standing line 5 lists symbols among the names a reader may not write. May B3 name the Planet and Element members it determines?
- **Recommended (PROVISIONAL).** Yes: B3, and only B3, may name the members it determines (incumbent and alternatives); everywhere else the names stay out, and the merge maps them. The brief's silence on this was the orchestrator's defect.
- **Where:** `RUN_PROGRESS_Ariun_Nuur.md`, 2026-11-19 13:49–14:14; `.t8_Phase10_round3_reader{A,B,C}.md`.

### DEC-887 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R (a PDF read from the fetch tool's saved file)
- **Question.** Phase 10R reader B read four facts (F111–F114) from a PDF that the fetch tool saved locally and B then opened with Read; readers A and C declined that step. Are such facts admissible?
- **Recommended (PROVISIONAL).** Yes, as web-source content: the saved file is the fetched page, not a repository file. Each is marked with its source date (a 2017–18 guide) and tagged as a saved-PDF read.
- **Where:** `RUN_PROGRESS_Ariun_Nuur.md`, 2026-11-19 14:04; `.t8_Phase10R_round3_reader{A,B,C}.md`.

### DEC-888 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 (the candidate research split into three row sub-units)
- **Question.** LAW 0-P requires every candidate row to be researched; the handoff planned one unit of three readers. One reader's context holds about 110 web calls (measured on Phase 10R: about 390,000 tokens per reader at 103–113 calls), and 85 rows need several calls each. May the unit run as three sub-units by rows (1–29, 30–58, 59–85), each a full T8 with three readers (nine readers in all), with a cap of 90 calls each?
- **Recommended (PROVISIONAL).** Yes: each sub-unit keeps the full T8 (three independent readers, Round 2, Round 3, one merge); every row is still read by three readers; the split serves coverage, which is the law's purpose. Row 86 waits (developer, 2026-11-19).
- **Where:** `RUN_PROGRESS_Ariun_Nuur.md`, 2026-11-20; `.t8_brief_04_Phase10R2u{1,2,3}.md`.

### DEC-889 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (the merge in two stages)
- **Question.** The Phase 10 merge's inputs (four units, eighteen reader outputs and their Round 3 replies) are larger than one merge writer can hold. May the merge run in two stages: first one research merge per research unit (Phase 10R; Phase 10R2 sub-units 1–3), each written as a research-log entry; then one catalog merge over Phase 10's and Phase 10C's outputs and the four merged research entries?
- **Recommended (PROVISIONAL).** Yes: every T8 unit still gets one fresh merge writer under the merge rule (M-246), and the catalog writer reads every unit's merged result. A method note goes to the observations log for after the run.
- **Where:** `RUN_PROGRESS_Ariun_Nuur.md`, 2026-11-20 (the merge design entry); `.t8_merge_brief_04_Phase10R.md`.

### DEC-890 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R (research-log Entry 3) (Q2)
- **Question.** **The modules' mapping to sectors.** A 2020 table, seen only in summaries, was read as 434-A/434-B for two sectors (A) and as 434-D/434-E for Sectors 15 and 16 (B).
- **Recommended (PROVISIONAL).** Keep the SOURCED address (Building 434-D) only; carry B's mapping as UNVERIFIED, fitting that address; use no mapping beyond the pick's own sector until a page is read (P10R-T9)
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, research-log Entry 3, Developer questions, Q2 (raised by A (c)).

### DEC-891 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R (research-log Entry 3) (Q3)
- **Question.** **The new complex's floor area at the real site**: more than 3,000 m² (A, the operator's own page, UNVERIFIED) against about 2,000 or 2,500 m² (C, by source, UNVERIFIED).
- **Recommended (PROVISIONAL).** Carry no figure into the catalog until a page is read; keep both with their sources (P10R-T18)
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, research-log Entry 3, Developer questions, Q3 (raised by A (c) · C (c)).

### DEC-892 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R (research-log Entry 3) (Q4)
- **Question.** **Aurora at the real site**: three UNVERIFIED statements in different coordinate systems (A 82; C F-256; B F172), one of which is withheld under point 4.
- **Recommended (PROVISIONAL).** Carry the aurora only as UNVERIFIED and unreconciled; confirm the withholding of B F172 and of C F-256's jointly-stated sentence under point 4; queue a read of a frequency paper (P10R-T17)
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, research-log Entry 3, Developer questions, Q4 (raised by A (c)).

### DEC-893 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R (research-log Entry 3) (Q5)
- **Question.** **The testing lab's end**: C's lead (halted end of 2022, over 650,000 tests) is UNVERIFIED; A and B found no date.
- **Recommended (PROVISIONAL).** Keep it as an UNVERIFIED lead credited to C; a later session reads the page (P10R-T11)
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, research-log Entry 3, Developer questions, Q5 (raised by C (c)).

### DEC-894 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R (research-log Entry 3) (Q6)
- **Question.** **The aluminum plating's attribution** (B F116 against C's read of the same page).
- **Recommended (PROVISIONAL).** Keep the narrower form written (aluminum plating only, UNVERIFIED, both articles cited); drop "quarter-inch" and "in electric rooms" unless a page read restores them
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, research-log Entry 3, Developer questions, Q6 (raised by C (c) · orchestrator (point 3)).

### DEC-895 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R (research-log Entry 3) (Q7)
- **Question.** **OPEN-29: visitor stay "2 to 6" against "1 to 6" months.** Not reached by any reader in this unit.
- **Recommended (PROVISIONAL).** Leave it open for the next research pass; neither figure is carried until it is read (P10R-T7)
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, research-log Entry 3, Developer questions, Q7 (raised by B (c)).

### DEC-896 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R (research-log Entry 3) (Q8)
- **Question.** **The construction-complete date**: A read completion as of 2026-06-09 inside the sector's news item of 2026-07-27; C recorded only the item's date.
- **Recommended (PROVISIONAL).** Keep both dates as written, A's credited to A; it changes nothing in the catalog
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, research-log Entry 3, Developer questions, Q8 (raised by B (c, "only if the date matters")).

### DEC-897 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 1 (Entry 4) (U1-Q1)
- **Question.** **The saved-PDF point.** Several facts are marked SOURCED from PDFs that the fetch tool could not parse and saved to its own tool-results folder, which the reader then viewed page by page with Read (A calls 14, 64, 88; B C11, C41; C calls 8, 29: the underground lab's visitor guides, the borehole fact sheet, the clean-air plan, the laboratory's 2015 tally). Should a PDF viewed this way count as "read on the page fetched" (SOURCED)?
- **Recommended (PROVISIONAL).** **Yes, SOURCED,** PROVISIONAL: the file is the fetched source's own content, the fetch is in the reader's call log, and two readers viewing the same PDF independently confirmed each other's lines at Round 3 (the clean-air plan's winter-crew line; the visitor guide's shower and pressure lines). This entry is written on that basis; if the answer is no, the facts citing those URLs drop to UNVERIFIED.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 4, Developer questions, U1-Q1 (raised by the merge).

### DEC-898 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 1 (Entry 4) (U1-Q2)
- **Question.** **Waiting-topic tags the merge added on its own reading.** Beyond the tags Round 3 named, the merge tagged `WAITS (DCI)` on institutional administration: a laboratory's single-budget rule (U1-F60), no departments and no tenure (U1-F37), funding rules (U1-F57), a data license and fee policy (U1-F8, U1-F9), the vault's ownership (U1-F119), a planning permission (U1-F75), a regional deadline (U1-F258), a drilling team's reorganization (U1-F225), and who runs the tortoise pens (U1-F159). Keep these tags?
- **Recommended (PROVISIONAL).** **Keep them,** PROVISIONAL: the brief sends governance and company-run administration to the DCI, the tags hide nothing (each fact is written in full), and the physical side of each fact stays usable now.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 4, Developer questions, U1-Q2 (raised by the merge).

### DEC-899 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q1)
- **Question.** Row 32: did the new ski area open on 12 or 23 November 1957? (U2-F48)
- **Recommended (PROVISIONAL).** Keep both: 12 November for the first tow's running, 23 November for the area's opening, labeled as such until a third source settles it.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q1 (raised by A; B).

### DEC-900 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q2)
- **Question.** Row 36: how many institutions are in the science city — about 150, 29, or 60 national plus 240 private (by 2000)? (U2-F101)
- **Recommended (PROVISIONAL).** Keep all three, each with its date and scope; they count different things, so no single figure is written.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q2 (raised by A).

### DEC-901 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q3)
- **Question.** Row 37: did the first light-source ring open in 1993 or 1994? (U2-F105)
- **Recommended (PROVISIONAL).** Keep both: 1993 for the center's formation and first operation, 1994 for opening to users.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q3 (raised by A; B).

### DEC-902 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q4)
- **Question.** Row 37: did the first ring carry 22 or 26 beamlines? (U2-F105)
- **Recommended (PROVISIONAL).** Keep both with their sources; neither page gives a date for its count, so treat them as counts from different years until rechecked.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q4 (raised by A; B).

### DEC-903 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q5)
- **Question.** Row 45: is the station's summer population about 160, 180 or at least 200, and are its publications 1,500+ or 2,000+? (U2-F178)
- **Recommended (PROVISIONAL).** Keep all, labeled as different measures (people living in the town, people in residence, researchers) and as counts of different dates.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q5 (raised by A; B).

### DEC-904 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q6)
- **Question.** Row 49: is Oymyakon 30 or about 40 km from Tomtor? (U2-F202)
- **Recommended (PROVISIONAL).** Write 30 km as the working figure (the encyclopedia, read by two readers), with the 2004 article's "about 40 km" as a conflict line; the two may be road and straight-line distances.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q6 (raised by A).

### DEC-905 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q7)
- **Question.** Row 51: did the thermometer cost $700,000 or $750,000? (U2-F223)
- **Recommended (PROVISIONAL).** Keep both with their sources; prefer neither.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q7 (raised by A; B).

### DEC-906 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q8)
- **Question.** Row 52: are the winter minimums about −9 to −10 °C or −3.9 °C? (U2-F234)
- **Recommended (PROVISIONAL).** Keep both, labeled as mean monthly minimum and mean daily minimum, and reread the page's climate table before either figure is used (U2-T25).
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q8 (raised by A; B).

### DEC-907 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q9)
- **Question.** Row 55: were three or five people present for the 1934 gust? (U2-F268)
- **Recommended (PROVISIONAL).** Keep both; the observatory's own anniversary post (five men) is the closer source, but no reader read it on the page.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q9 (raised by A).

### DEC-908 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q10)
- **Question.** Row 56: is the Sphinx at 3,570, 3,571 or 3,580 m? (U2-F269)
- **Recommended (PROVISIONAL).** Keep 3,571 m (read by two readers) and 3,580 m (read by one) as a recorded conflict, noting the foundation's 3,570 m from a summary.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q10 (raised by A; B).

### DEC-909 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 2 (Entry 5) (U2-Q11)
- **Question.** The saved PDFs: three of reader A's fetches returned binary PDFs that the fetch tool saved locally; the readers' brief forbade commands on files, so they were logged as dead at the sources, and other PDFs (the 2026 room guide, the support association's yearbooks, a staff-survey report) were seen only in summaries. May a later research step open such saved or listed PDFs?
- **Recommended (PROVISIONAL).** Yes: let a later research step open a PDF with the Read tool (no other command), log it as a fetch with its call number, and mark a fact SOURCED only when read there; until then these stay dead at the sources (U2-T33).
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 5, Developer questions, U2-Q11 (raised by A (note); merge).

### DEC-910 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 3 (Entry 6) (U3-Q1)
- **Question.** **Period and people adjectives under the no-demonym rule.** Does the rule cover words such as "Roman" (as in "a Roman villa"), "Viking" (the row's own name, used by all three readers) and "American spelling"?
- **Recommended (PROVISIONAL).** A real place's proper name keeps its words as a source name (for example, the Viking Ship Museum). Elsewhere, write the period plainly, by its date, where the source dates it ("a 4th-century villa wing"; a longship built about 1042); where the source gives no date, keep the source's phrase in the fact and flag it. "American spelling" names a spelling convention, not a people, and stays. This merge applies that answer throughout.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 6, Developer questions, U3-Q1 (raised by Reader C, Round 3 (marked (c))).

### DEC-911 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10R2 sub-unit 3 (Entry 6) (U3-Q2)
- **Question.** **Facts read from a PDF that the fetch tool saved and the reader then viewed with Read.** Reader A (call 71, slides 1–8) and reader C (call 68, pages 1–4; call 70, slides 1–12) marked such facts SOURCED (U3-F32, F34, F35, F175). Is a saved copy of a logged fetch a "read on the page fetched," and does its URL count as in the finder's own call record?
- **Recommended (PROVISIONAL).** Yes: keep them SOURCED. The URL is in each finder's own fetch log, the bytes came from that logged fetch, and the readers viewed the saved file as web data, not as a repo file. Mark each such fact "SOURCED (PDF viewed)," as this entry does, so the route stays visible.
- **Where:** `Research_Logs/Ariun_Nuur_Research_Log.md`, Entry 6, Developer questions, U3-Q2 (raised by The orchestrator's Round 3 points (the saved-PDF point)).

### DEC-912 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-204)
- **Question.** **Planet:** keep the incumbent, or choose another member?
- **Recommended (PROVISIONAL).** Leave it open. The leading alternative is the one B3 names first (A, B), with the incumbent and the distributed member beside it: the city's lines describe a place that knows a thing it cannot see and gives that knowledge to whoever does the work, more than a place cut off
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-204.

### DEC-913 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-205)
- **Question.** **Element:** set one now?
- **Recommended (PROVISIONAL).** Leave it open with the three candidates B3 records; if one is wanted now, the member every reader found fits at least in part (A first, B second, C in part), its one-word label left to the file's own review
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-205.

### DEC-914 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-206)
- **Question.** May a phase's B3 name symbol members?
- **Recommended (PROVISIONAL).** Yes, in B3 only, as `DEC-886` already records
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-206.

### DEC-915 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-207)
- **Question.** **The marker's surface part:** A's standing instrument screen, B's raised post, or none (C's register alone)?
- **Recommended (PROVISIONAL).** The shared core as FIND-P10-2 writes it (the found entry kept on paper, attributed as found), with B's raised post as its surface part if you want one: it is rooted in the city's own stake grid and raising chore, where A's screen copies the real site's instrument; or C's register alone, if no surface part is wanted
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-207.

### DEC-916 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-208)
- **Question.** **The axis's wording?**
- **Recommended (PROVISIONAL).** *Kept by the cold, raised by hand* — and nothing that stands stays where it was set
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-208.

### DEC-917 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-209)
- **Question.** **The lake: a landmark or a feature?**
- **Recommended (PROVISIONAL).** A feature that the earlier files call a landmark, until a line uses it for direction
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-209.

### DEC-918 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-210)
- **Question.** **The archive's physical form:** adopt A's two-room body (a cold store that costs nothing, a warm working room that costs heat, a door between)?
- **Recommended (PROVISIONAL).** Not yet: carry the form (REQ-146) and keep A's body reserved (RF-192) as the leading proposal
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-210.

### DEC-919 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-211)
- **Question.** **Visitors:** does someone who comes for a run on the instruments and leaves contradict *those who came have stayed* (Phase 7 FIND-P7-45; Phase 5 L361)?
- **Recommended (PROVISIONAL).** Hold the visitor who leaves reserved (RF-199) until you rule; if admitted, C's reading, that the spine names those who came to live, not those who come for a run
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-211.

### DEC-920 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-212)
- **Question.** **Positions:** who is the Passer-Through and the Elder here, and is a district the Child?
- **Recommended (PROVISIONAL).** Leave all three blank until the ledger's definitions are read (REQ-153) and Q-211 is answered
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-212.

### DEC-921 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-213)
- **Question.** **Where do carried holes go:** Step 10, or Step 5?
- **Recommended (PROVISIONAL).** Step 10 for the developer's holes and the demonym slot; Step 5 only for the symbol backstop, the shaft's qualifier and the person-shaped lens results
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-213.

### DEC-922 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-214)
- **Question.** **Sweep convention:** a pure record (a credit row, a split row, a `Generators used` line) discharged as answered or as not applicable?
- **Recommended (PROVISIONAL).** Not applicable (N), with the place that answers its matter named
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-214.

### DEC-923 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-215)
- **Question.** **The sign-7 prompt** (fairness, harmony): three different results
- **Recommended (PROVISIONAL).** Keep all three as prompts; nothing is assigned
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-215.

### DEC-924 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-216)
- **Question.** **The inherited station:** kept raised by the settlers, or found buried and drifted?
- **Recommended (PROVISIONAL).** B's answer: found partly buried and drifted, which suits the found paper (Phase 3 L274) and the moving of the stores; written only once you confirm
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-216.

### DEC-925 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-217)
- **Question.** **Phase 10C row 84:** may a "furthest from everywhere" marker be researched as a form when the point lies near the city, not at it, and cannot be named?
- **Recommended (PROVISIONAL).** Research it as a source for a marker form only (stage B, under LAW 0-P); no landmark for it is written in the city until you allow one
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-217.

### DEC-926 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-218)
- **Question.** **Phase 10C row 55:** can the museum built around a record serve as a marker form, its record-as-identity care note set aside?
- **Recommended (PROVISIONAL).** Yes, the museum form only, as a lead; the record-as-identity angle stays barred (`DR-28` D2–D3)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-218.

### DEC-927 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-219)
- **Question.** **Phase 10C row 71:** does a relation site outside the city belong in its Phase 10 catalog?
- **Recommended (PROVISIONAL).** No: the outpost is cataloged as a relation (CAT-11), and the row's lead is NO LEAD for the city itself
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-219.

### DEC-928 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-220)
- **Question.** **Phase 10C row 32:** WAITS or NO LEAD?
- **Recommended (PROVISIONAL).** WAITS (games and arts), as the orchestrator recorded
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-220.

### DEC-929 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-221)
- **Question.** **Does the district's honor take a physical form now?**
- **Recommended (PROVISIONAL).** No: a name only, until you name anyone or allow a form (RF-8; Phase 6 Q-138)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-221.

### DEC-930 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-222)
- **Question.** **May Phase 10 coin proper place names?**
- **Recommended (PROVISIONAL).** No: plain working descriptions only; proper names wait for the cultural synthesis and for you
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-222.

### DEC-931 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-223)
- **Question.** **The geneticist:** may her own teaching practice stand as an in-person teaching thread, and will her canon entry be dated so `DEC-681` can be met?
- **Recommended (PROVISIONAL).** Her affiliation only, no institution (RF-200); and please give her era
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-223.

### DEC-932 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-224)
- **Question.** **The elementals file's label count:** it says six labels are under review while seven entries carry the mark
- **Recommended (PROVISIONAL).** Correct the count to seven, or name the six
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-224.

### DEC-933 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-B1-1)
- **Question.** **A copy kept elsewhere.** Three unconnected rows (6, 15, 16) keep or rebuild a living stock from copies held at another site. Does the city keep any copy of its living stock off the plateau?
- **Recommended (PROVISIONAL).** not now. The city's lines give one supply and a city that holds what cannot be moved, so single-site keeping stays the city's condition and its shadow (SH-38); the convergence is recorded as evidence for a later relation, written, if allowed, as what flows and in which direction.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-B1-1.

### DEC-934 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-B1-2)
- **Question.** **CAT-58's wording.** Its title, *lit only by the city's own light*, is not what the site's measured sky shows: a noon twilight every day and a moon up all day for about a week (CAT-B1-5, CAT-B1-6). Amend CAT-58?
- **Recommended (PROVISIONAL).** yes, at Step 5, to *lit by the city's own light, with a faint noon twilight and the moon's week*, spec L96's polar night unchanged.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-B1-2.

### DEC-935 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-B1-3)
- **Question.** **Phase 10C's candidate convergence on written instructions** (rows 12, 54, 75, 76, 79). Row 12's research shows custody passed in person with a written map, not instructions to strangers.
- **Recommended (PROVISIONAL).** row 12 counts toward the in-person handover (convergence 4), not toward written instructions alone; stage B2 tests the other four rows on their own facts.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-B1-3.

### DEC-936 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-B1-4)
- **Question.** **Rows 22, 23 and 24: three places or one root?** All three stand on one ice sheet.
- **Recommended (PROVISIONAL).** count three (no shared operator in the facts), noting the shared ice; nothing in the catalog rests on the count.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-B1-4.

### DEC-937 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-B2-1)
- **Question.** Does the city keep its own outdoor cold readings (an observer, an instrument housing, a register), beyond the inherited 1983 entry?
- **Recommended (PROVISIONAL).** Hold it on Q-207. If you choose a standing screen or C's register, CAT-B2-2 and an observer's role follow as researched forms; if you choose neither, CAT-B2-2 stays a conditional item and no role is written.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-B2-1.

### DEC-938 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-B2-2)
- **Question.** Many rows cap and rotate stays at the hard place (15-day shifts, eight days on and six off, tours of three to six months, stays under about four weeks). Does any role in the city rotate?
- **Recommended (PROVISIONAL).** No: the city's lines say those who came have stayed (Phase 7 FIND-P7-45), so no rotation is cataloged; the outpost's staffing, a relation, stays open.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-B2-2.

### DEC-939 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-B2-3)
- **Question.** Row 84: the research found no marker at the pole and several computed positions for it. Does that change Q-217?
- **Recommended (PROVISIONAL).** No change to Q-217's answer. If a marker is ever allowed, it marks a computed point that moves with the method, so the city is written as *near* it, never *at* it.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-B2-3.

### DEC-940 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Phase 10 (Q-B2-4)
- **Question.** Should a powered or lit display be ruled out of the marker's surface part (Q-207)?
- **Recommended (PROVISIONAL).** Yes: a lit display is one more draw on the one supply, and a dark one becomes the marker's own failure (U2-F225). Keep the found paper indoors as the record, and if a surface part is wanted, make it unpowered.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md`, Q-B2-4.

### DEC-941 · PROVISIONAL · 2026-11-20 · LAW 0-P filing (the RWBEM's ULM copy)
- **Question.** LAW 0-P was written in place into the RWBEM's original (`Worldspace/Locations-and-Levels/Real-World_Basis_Extrapolation_Method.md` L73). Should the ULM's `Disciplines/` copy of the RWBEM carry it too? That copy is not a ULM input (`DR-14`) and may be pinned by other files.
- **Recommended (PROVISIONAL).** Yes, at the next methodology-maintenance session, with its pin re-taken; not during a city run.
- **Where:** `RUN_PROGRESS_Ariun_Nuur.md`, 2026-11-20 (held filings).

### DEC-942 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-225)
- **Question.** The spine sentence (those who came have stayed), research FIND-25, Phase 4 FIND-P4-32's heading and others say or imply that no one leaves the city, while audit RF-30 forecloses asserting that no one left, and Phases 4 and 5 found within-nation arrival channels (RC-39). **Scope these claims to the national scale?**
- **Recommended (PROVISIONAL).** Yes: write could not return to Upper Earth; no departure from the city is written. Tag every finding that needs city-scale staying as resting on an absence (RF-202). The spine sentence's wording goes with the qualifier work, unamended
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-225 (raised by A1·A Q-1; A1·A R3 (c)).

### DEC-943 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-226)
- **Question.** **Does one supply carries both bodies' lives rest on a provisional parental fact,** since the city's heat on the electric supply comes only from a power file that says nothing in it is a ruling?
- **Recommended (PROVISIONAL).** Yes, until the developer rules the city's supply (spine Q-37; Phase 5 REQ-96). Keep a robot's charge on the electric supply as ruled (`DR-140` item 4); hold the city's heat on that supply as the national default, unratified and tagged; the finding stands, tagged, and may not be the strongest; the physical core stands either way
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-226 (raised by A1·A Q-2 · A1·C Q-C204).

### DEC-944 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-227)
- **Question.** Phase 5 L394 calls the research arrivals the first within-nation arrival route written in this pass, after Phase 4 wrote carers sent from the national institutes. **Reword?**
- **Recommended (PROVISIONAL).** Yes, by amendment note: the first within-nation arrival with a named origin and a written motive; the carers' route stays a request (Phase 4 REQ-90)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-227 (raised by A1·A Q-3).

### DEC-945 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-228)
- **Question.** **Read the spine sentence's only the work that is its purpose can ever be stopped as the research's use of its instruments, with the shaft's keeping counted with the heat as work that cannot stop?** (RC-36)
- **Recommended (PROVISIONAL).** Yes, as a qualifier note beside the unamended sentence (FIND-P10-4), conditional on the shaft's form (REQ-145). Phase 6's purpose-yields-first then holds for the research only, and Q-142's shortage reading sets the body's promise against the shaft's upkeep (FIND-S5-2)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-228 (raised by A1·B Q-B101 · A2·A Q-1 · A2·C Q-C201).

### DEC-946 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-229)
- **Question.** **Does spec L167's self-sufficiency the plateau allows mean self-keeping (the survival work) rather than self-supply?** (RC-19)
- **Recommended (PROVISIONAL).** Yes, PROVISIONAL, checked at stage B against the city's own material (REQ-163)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-229 (raised by A1·B Q-B102).

### DEC-947 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-230)
- **Question.** **The generator-vocabulary leaks (T-1 to T-36): correct them in the pass files, or leave the files as written?**
- **Recommended (PROVISIONAL).** Leave the pass files as written (`DR-101`); use the plain rewrites wherever the findings are carried into later text, by an append-only docket (REQ-173); this pass is still PROPOSED, so the developer chooses
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-230 (raised by A1·B Q-B103).

### DEC-948 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-231)
- **Question.** **Is Airports L18 (tagged there as a developer ruling; Phase 5 L288) hard canon,** so that it outranks Phase 2's city-scale null on why anyone came? (RC-41)
- **Recommended (PROVISIONAL).** Yes, for exactly what it states: a moderate, unsized share came up from member cities of the subnet for research. Phase 2's null stands for everyone else; the census-kinship reasoning in the same paragraph stays unused (RF-16)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-231 (raised by A1·C Q-C201; A1·B R3 (c)).

### DEC-949 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-232)
- **Question.** **Is SC-1, in its physical form, the pass's strongest finding?** The A1 readers converge on it; A2's readers nominated SC-4 (B, C) and SC-5 (A)
- **Recommended (PROVISIONAL).** Yes. SC-4 and SC-3 are next and rest on SC-1 or on PROPOSED readings and absences; SC-5 and SC-8 are barred by rule 4. Check SC-1's legs at stage B (REQ-163)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-232 (raised by A1·C Q-C202; A1·A R3, A1·B R3, A2·A R3 (c)).

### DEC-950 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-233)
- **Question.** **Within-phase contradictions (RC-48, RC-52, RC-53, RC-54): record them now as reconciled by narrowing, or hold them for Gate 3 at Step 7?**
- **Recommended (PROVISIONAL).** Record them here as reconciled by narrowing; Gate 3 at Step 7 confirms; any note on a pass file only after the developer's word (REQ-165)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-233 (raised by A1·C Q-C203).

### DEC-951 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-234)
- **Question.** **Read the spine's D-4 (the subnet has no road to it) as no road to its coastal hub?** (RC-56)
- **Recommended (PROVISIONAL).** Yes; the spine's own G5 row says so (L65). Remedies from elsewhere holds for freight; people and means come from member cities by Hwy 37 and, PROPOSED, Hwy 22
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-234 (raised by A2·A Q-2).

### DEC-952 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-235)
- **Question.** **Is a parent location the ledger's Parent position?** (RC-61; catalog L1015)
- **Recommended (PROVISIONAL).** No: the position is a person's. Leave the Parent blank at Phase 10 until REQ-153 reads the ledger's definitions
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-235 (raised by A2·A Q-3; A2·C R3 (c)).

### DEC-953 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-236)
- **Question.** **Genetics (RC-72): hold the catalog's genetics wording narrowed in stage A and carry it to stage B as T2 vision?**
- **Recommended (PROVISIONAL).** Yes. Hold the narrowed wording (REQ-169) and CAT-6 PROVISIONAL with RF-43; stage B reads the vision sentence as a check; if it corroborates, T2 applies: it is not out-reasoned, and the pass finds its mechanism (the primary pick's structural forms; the living-sample cold need). Answer REQ-36, REQ-123 and Q-157 first; the developer may rule the subject canon at any time
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-236 (raised by A2·A Q-4 · A2·B Q-101 · A2·C Q-C204; A2·A R3, A2·B R3 (c)).

### DEC-954 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-237)
- **Question.** **The out-of-frame rows (RC-73 to RC-80): strike or hold?**
- **Recommended (PROVISIONAL).** Hold them OUT OF FRAME, not deleted; re-examine after stage B reads L153–161 and the other lines as a check; any use needs an admitted line or a ruling
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-237 (raised by A2·A Q-5).

### DEC-955 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-238)
- **Question.** **Re-put Q-217 and Q-B2-3 without the excluded premise?** (RC-74)
- **Recommended (PROVISIONAL).** Yes: may a marker form for a computed pole be researched as a source only? No nearness to the city is written
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-238 (raised by A2·B Q-109).

### DEC-956 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-239)
- **Question.** **One amendment piece for all twelve `AM-P9` rows, run as its own three-reader unit, with one pointer line at the end of Phase 9?**
- **Recommended (PROVISIONAL).** Yes (`DR-74`); drafted now as a PROPOSED docket; the pointer applied only with the dockets (`DR-116` item 2) and read by a second reader (rule 4); `AM-P9-10` held on Q-211
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-239 (raised by A2·A Q-6 · A2·B Q-102 · A2·C Q-C205).

### DEC-957 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-240)
- **Question.** **Adopt RC-58's wording for CAT-58 as a docket line?**
- **Recommended (PROVISIONAL).** Yes, with spec L96 unchanged (REQ-170)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-240 (raised by A2·B Q-103).

### DEC-958 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-241)
- **Question.** **Are the spine's method sections (§1 to §7, including the shape report at L251 and the lines at L269 and L293) under the translation discipline?**
- **Recommended (PROVISIONAL).** Exempt in place as Step 2's instrument report, never carried into a later claim in that vocabulary; T-4 (§8e, L368) and T-5 (L520) lie outside the method sections and are hits
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-241 (raised by A2·B Q-104; A1·A R3, A1·B R3 (c); orchestrator's point 8).

### DEC-959 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-242)
- **Question.** **Did the robot majority grow by arrival, by building, or both?** (RC-16)
- **Recommended (PROVISIONAL).** Not in-run. Hold RF-213 and answer it with REQ-68 (a working chamber) after the run
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-242 (raised by A2·B Q-105).

### DEC-960 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-243)
- **Question.** **Add the labels carried to stage B and carried to Step 10 to the brief template for split steps?**
- **Recommended (PROVISIONAL).** Yes, so that no row is forced into discharged or not applicable, and none is dropped
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-243 (raised by A2·B Q-106 · A2·C Q-C203; orchestrator's point 1).

### DEC-961 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-244)
- **Question.** **Narrow CAT-B1-3 to single-custody works** (the shaft's watch, the map of what lies below), withdrawing the choosing as a practice and the clause about the city not letting it lapse, and holding the record-outliving-keeper half? (RC-59)
- **Recommended (PROVISIONAL).** Yes (REQ-172; RF-212), until the phase that reads the archive's succession
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-244 (raised by A2·B Q-107 · A2·C Q-C202; A2·A R3 (c)).

### DEC-962 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-245)
- **Question.** **Do the lens results tagged role (sign 9's research arrival for a term; sign 10's earlier arrival who teaches; sign 10's raisers) count as person-shaped for the Phase 9 amendments?**
- **Recommended (PROVISIONAL).** Not as a class: the catalog's union names twelve. The first two are already in Phase 9 (L245, L340) and need no amendment; the raisers, absent from Phase 9's table (CAT-41; Phase 4 FIND-P4-21), may be added as one further function row if the developer wants them, with `AM-P9-7` already covering the shaft's keeping
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-245 (raised by A2·B Q-108; A2·A R3, A2·B R3, A2·C R3 (c)).

### DEC-963 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-246)
- **Question.** **Frame RF-26's expertise check (DF-6): does stage A's sweep (no finding characterizes the city's scientific expertise as a quality) stand, or does A1·A's candidate list go to the check against the physiology file's L409?**
- **Recommended (PROVISIONAL).** Both: the sweep is recorded, and the candidate list goes to whoever runs the check with L409 on the list (REQ-161); no `[SELF-ORIGINATED]` tag is applied until that comparison is made
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-246 (raised by A1·A R3 (c)).

### DEC-964 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-247)
- **Question.** **Are the research's unbracketed cross-references to spine costs (T-6, T-9) and its deficit-address labels standing as claim subjects (T-10 to T-12) translation hits?**
- **Recommended (PROVISIONAL).** Yes for the labels as subjects (T-10 to T-12); the cross-references are repaired by bracketing only
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-247 (raised by A1·A R3 (c)).

### DEC-965 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-248)
- **Question.** **The skiway against the Airports file (RC-46): canon wins or reconciled?**
- **Recommended (PROVISIONAL).** Canon wins for the city object (the Airports file decides that no airfield is at the city), with the skiway kept as a site fact; the substance is the same either way
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-248 (raised by A1·B R3, A1·C R3 (c)).

### DEC-966 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-249)
- **Question.** **Is research FIND-33 against `DR-19` a contradiction at all?**
- **Recommended (PROVISIONAL).** No: FIND-33 claims no motive and is not counted as the city's own evidence; record only that it grounds no motive (REQ-9 stays open)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-249 (raised by A1·C R3 (c)).

### DEC-967 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-250)
- **Question.** **May a base be applied to §23's shares?** (RC-57; already Q-155)
- **Recommended (PROVISIONAL).** Not until REQ-120, REQ-121 and Q-155 put §23's lines at source; until then the shares are cited as shares and no headcount is derived; Phase 7's reproduction stays a check (RF-151)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-250 (raised by A2·A R3, A2·B R3, A2·C R3 (c)).

### DEC-968 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-251)
- **Question.** **The eight standing-refusal lines naming Step 5 as a check (DF-16): not applicable, or carried to stage B?**
- **Recommended (PROVISIONAL).** Not applicable: they record reading order and hand no check; the checks themselves are carried to stage B
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-251 (raised by A2·B R3, A2·C R3 (c)).

### DEC-969 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-252)
- **Question.** **REQ-129 (DF-28): not applicable in stage A, or carried to stage B and Step 10?**
- **Recommended (PROVISIONAL).** Not applicable in stage A; the orchestrator confirms the basis before stage B uses the tier, and the basis itself rides to Step 10 with REQ-63
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-252 (raised by A2·B R3 (c)).

### DEC-970 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-253)
- **Question.** **Q-213 (DF-34): not applicable as a deferral, or discharged?**
- **Recommended (PROVISIONAL).** Not applicable: a scope statement whose three items are discharged at DF-30 to DF-32; a label only
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-253 (raised by A2·B R3 (c)).

### DEC-971 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-254)
- **Question.** **Is unspeakable, the deficit-address check's word, a translation hit where it stands in a claim about the city (T-11, T-34, T-35, T-36)?**
- **Recommended (PROVISIONAL).** Yes where it stands as a quality of the city in a claim: rewrite as a cost no one has a reason to name; keep the word inside bracketed method notes
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-254 (raised by A2·B R3 (c); orchestrator's point 8).

### DEC-972 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-255)
- **Question.** **The robots' hours (RL-42, RL-43).** The 2026-07-06 vision writes the city's robots as keeping no fixed hours: work to the task's end, then socialize, rest and return. The pass writes the national shared night into the city (Phase 4 FIND-P4-6; Phase 9 FIND-P9-15, FIND-P9-39). **Does the vision govern for the city's robots, the national shared night read as a pattern they do not keep?**
- **Recommended (PROVISIONAL).** **Yes, once `DR-10` is read and shows a reading-order strike** (REQ-187). The vision is upstream and is not out-reasoned, and the pass already holds its mechanism (FIND-P7-20, FIND-P4-5, FIND-P4-8, FIND-P4-10, FIND-P4-28, FIND-P9-19). The national shared night stays the national pattern; here the clock-hour night is the humans' sleep, which the life support's keepers work through, and the robots charge warm, by task, at any hour. Amend by REQ-189; SC-1 is unaffected
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-255 (raised by A-Q-1 · Q-B102 · Q-C201).

### DEC-973 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-256)
- **Question.** **Genetics (RL-30; RC-72; updates Q-236).** With the vision in the city's own file and the primary pick read as a gene-editing technology (spine S3-17), **may the pass write the research program's subject as genetics,** its mechanism the pick, the living-cell cold store and the shaft?
- **Recommended (PROVISIONAL).** **Yes, once `DR-10` shows its strike was a reading-order matter and spine Q-38 is answered as the gene-editing reading** (REQ-187); keep the tag (read out of order), drop the hedge (runbook L2854–2856). The geneticist stays out until her canon entry is read (REQ-188). Until then RF-209 stands
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-256 (raised by A-Q-2 · Q-B101 · Q-C202).

### DEC-974 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-257)
- **Question.** **The research population's extent (RL-43).** Does the vision place most of the robot population in the research?
- **Recommended (PROVISIONAL).** **Not in-run.** Keep the research population one unsized layer; decide after REQ-181, since the 65% figure may be the culture file's own
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-257 (raised by C (Q-C204); A R3 (c)).

### DEC-975 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-258)
- **Question.** **Does the city grow a modest share of human food on the supply** (C L105; RL-32)?
- **Recommended (PROVISIONAL).** **Hold; the developer decides.** If yes: FIND-S5-3 reads supplied in most of its inputs, a modest part grown on the supply; FIND-P8-10 narrows to nothing grown here removes the import; SC-1's physical core is unaffected (FIND-P8-8). RF-204 stands until answered
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-258 (raised by A-Q-3 · Q-B105 · Q-C203).

### DEC-976 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-259)
- **Question.** **Is siligel formulated here, or only received** (C L107; R L168–170; RL-34)?
- **Recommended (PROVISIONAL).** **PV-6 stands (by shipment)** until the developer rules; if formulated here from shipped stock, write it as design, not supply
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-259 (raised by A-Q-4 · Q-B105).

### DEC-977 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-260)
- **Question.** **Do the inherited station records' terms survive as a register of the city's science** (C L88–91; RL-27)?
- **Recommended (PROVISIONAL).** **Not in-run;** spine RF-46 stays. Never inferred from the station's operators and never tied to the founders (`DR-19`, `DR-28` D2, `DR-35`). If the developer wants it, it enters as a fact about inherited records (`DR-25`; `DR-143` item 2); speech practice goes to the CST
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-260 (raised by A-Q-5 · Q-B104 · Q-C206).

### DEC-978 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-261)
- **Question.** **The relay, the game-design line and the geneticist (RL-46, RL-54).** At what tier does the dated game-design statement at C L205 sit, and how does `DEC-681` apply when a read-last line names the held-back figure?
- **Recommended (PROVISIONAL).** **Neither is out of frame;** both are the developer's. Until answered: the pass stays silent on the relay; the figure's role agrees with CAT-76 and nothing more is used. If the developer confirms the relay line and the network line (Q-263), Phase 5 Q-121 answers: no link of its own, and knowledge leaves by the road or through the partner's relay, as a relation, PROVISIONAL
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-261 (raised by A-Q-6; A R3, B R3, C R3 (c)).

### DEC-979 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-262)
- **Question.** **If §23's Canon §15 is the city's own culture file (REQ-181), are §23's shares still citable in the pass?**
- **Recommended (PROVISIONAL).** **Yes, as corroboration only,** tagged `[SELF-ORIGINATED]`; no finding's independence rests on them; SC-1 is unaffected (its model label is basis only)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-262 (raised by A-Q-7).

### DEC-980 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-263)
- **Question.** **Is no functional network reach at extreme altitude, whatever the cable** (C L213; R L200–202), **a ruling?**
- **Recommended (PROVISIONAL).** Until a ruling is found, unratified (`05` §6.3 rule 6). If it is one, RC-35 closes as canon wins, and RC-55's and FIND-P5-48's condition is met
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-263 (raised by Q-B103).

### DEC-981 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-264)
- **Question.** **Hospitality, the working-window etiquette and privacy, and courtship by aligning windows** (RL-21, RL-24, RL-25, RL-64): **which process takes them?**
- **Recommended (PROVISIONAL).** **The CST,** as everyday life (`DR-140` item 2's order), after Q-255 settles the robots' clock, on which three of them rest; never in-run
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-264 (raised by Q-B107 · Q-C205; B R3 (c) on the etiquette).

### DEC-982 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-265)
- **Question.** **The culture file's status, survived (C L8), and its 500-plus-years clauses (C L255, L264): from what vantage do they speak, and do they bear on the pass?**
- **Recommended (PROVISIONAL).** A post-war vantage; no bearing on the height (`DEC-698`); status is the spec's attribute; the clauses stay OUT OF FRAME, and the developer places them
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-265 (raised by Q-B109 · Q-C207).

### DEC-983 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-266)
- **Question.** **Does the robot file's no chamber-making now (R L80, L141) answer REQ-68?**
- **Recommended (PROVISIONAL).** **No.** It rests on the outpost's excluded end and is T3; keep PV-5 provisional; REQ-68 and Q-242 decide
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-266 (raised by Q-B106; A R3 (c)).

### DEC-984 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-267)
- **Question.** **The cold record and the lake research as foundational narrative (C L125–127; RL-38): a waiting topic for the CST, or a sheet conflict under `DR-28` D2–D3?**
- **Recommended (PROVISIONAL).** **Hand it to the CST,** with the bound noted: the marker may honor the measurement as an inherited record (`DR-143` item 2), and `DR-28` D2–D3 bind as the orchestrator reads them. The developer says whether arts and narrative wait for the CST (they are not on `DR-140` item 2's list as the brief gives it)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-267 (raised by A R3 (c); B R3 (a) to C's first reading).

### DEC-985 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-268)
- **Question.** **May a docket row be written against a sheet's feeling claim the pass itself bars** (P L17, rather than visible strain; RL-78; RF-143)?
- **Recommended (PROVISIONAL).** **Not now.** The pass characterizes no feeling; when the sheet is revised after the CST, set FIND-P9-19's cost beside the ethos as a note
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-268 (raised by C R3 (c)).

### DEC-986 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-269)
- **Question.** **Does a relay at a member city on Hwy 37 count as a channel the subnet supplies** (SC-7's leg)?
- **Recommended (PROVISIONAL).** **Not until Q-261 ratifies the relay;** then the leg is touched (information through one member city), not contradicted, and SC-7 stays below SC-1
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-269 (raised by C R3 (c)).

### DEC-987 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-270)
- **Question.** **The three files' founding-legend sections (DK-4, DK-6, DK-7): revisit now or after the run?**
- **Recommended (PROVISIONAL).** **After the run,** as the files' own end notes (C L278; R L279) already mark; nothing in the pass waits on them
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-270 (raised by Q-C208).

### DEC-988 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-271)
- **Question.** **The personality file's three type labels (RL-75): a pass item, or revisit after the run?**
- **Recommended (PROVISIONAL).** **Not a pass item:** a type is a conclusion (`05` §6.1) and the pass assigns none (FIND-P9-12); revisit after the ULM, in light of the pass
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-271 (raised by Q-B108 · Q-C210).

### DEC-989 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-272)
- **Question.** **Accept the named leg's result: leg (i) contradicted in part by tier-3 lines only, so SC-1 stands as the strongest finding?**
- **Recommended (PROVISIONAL).** **Yes** (Q-232 as recommended)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-272 (raised by Q-B110).

### DEC-990 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-273)
- **Question.** **The Phase 9 pointer (DK-22): append now, or with the dockets?**
- **Recommended (PROVISIONAL).** **With the dockets** (`DR-116` item 2), in DK-22's wording, read again by a second reader (rule 4), naming the amendment piece once it exists and any stage-B row the developer adopts against FIND-P9-15, FIND-P9-31 or FIND-P9-39
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-273 (raised by A-Q-8 · Q-C209).

### DEC-991 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 5 (Q-274)
- **Question.** **RC-72, RC-79 and DF-26: discharged as a check, or still open?**
- **Recommended (PROVISIONAL).** **A label only:** RC-72 and RC-79 still open pending `DR-10`, DF-26 in part (its language basis rides to Step 10); the substance is the same in all three outputs
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md`, Questions for the developer, Q-274 (raised by A R3 (c); C R3 (c)).

### DEC-992 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-275)
- **Question.** **Section 1, Shape:** write the standing cost's rise (with the institutions admitted) in the cell, and keep the method's own word *Balanced* in the table?
- **Recommended (PROVISIONAL).** **Keep *Balanced*** (the column asks for the shape name; the table is a method instrument, entry 15 Q-241). **Leave the rise out until Q-46 answers** whether direction is part of the shape; if it is, add it in plain words
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-275 (raised by B R3 (c) · C R3 (c) · A item 6 · Q-105 (B) · Q-C202).

### DEC-993 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-276)
- **Question.** **Section 2:** write the arrival modes Phase 2 tested and found null at city scale (*chose it*, *fled to it*, born here) into the mode-mix cell?
- **Recommended (PROVISIONAL).** **No.** The cell holds the modes the axis names; the nulls stay as Phase 2 wrote them (FIND-P2-18, FIND-P2-20, FIND-P2-22), where the terminal check can read them
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-276 (raised by B R3 (c) · A item 1 (A withdrew in R3)).

### DEC-994 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-277)
- **Question.** **Section 4:** carry the Q-255 caveat inside the cell, and write the finding's gloss beside its head?
- **Recommended (PROVISIONAL).** **Neither, in the cell:** the caveat rides in the source line (orchestrator point 3); the cell changes by the amendment that answers Q-255 (REQ-200). The head claims least; the gloss restates it
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-277 (raised by C R3 (c) · Q-104 (B) · Q-C203; the gloss split).

### DEC-995 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-278)
- **Question.** **Section 5, the unnamed load-bearing thing:** its wording; and is it the debt (Phase 6) whether Phase 6 classes it as a debt or a social contract with a debt inside it (Q-137), rather than the spine's heat no one names?
- **Recommended (PROVISIONAL).** **As written:** the debt by its direction and currency stands under either classification, and the section is Phase 6's; the heat stays section 1's ground. Revise only if the developer rules a contract with no debt
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-278 (raised by A R3 (c) · A item 7 · Q-C205).

### DEC-996 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-279)
- **Question.** **Section 5, Death & the dead:** name who handles a robot death (Phase 9 L430, Q-139, sent past the CST) or burial impossible on the ice in the cell?
- **Recommended (PROVISIONAL).** **No:** the first is a routing note and the second is national; both ride in the source line. Death's forms are not on `DR-140` item 2's list as the brief gives it; the developer may place them
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-279 (raised by C R3 (c) · Q-C207).

### DEC-997 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-280)
- **Question.** **Section 6, Governance:** add a fourth slot, first call on the supply, the road or arrivals written for no one (Phase 7 L1130, Q-160)? And is *where order cannot reach* an admissible governance cell while government waits for the DCI?
- **Recommended (PROVISIONAL).** **No fourth slot:** the axis counts three (L885–893), and whether the fourth is unadministrable or only unwritten is the developer's; **yes, admissible**, with who decides sent on to the DCI
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-280 (raised by A R3 (c) · B R3 (c) · Q-101 (B)).

### DEC-998 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-281)
- **Question.** **Section 6, Counterculture:** write the candidates' shapes, or an axis such as *forbids nothing in writing and charges for everything*, beside *none sited*? Is an empty slot acceptable in a table row?
- **Recommended (PROVISIONAL).** **No candidates; yes, the empty slot:** RF-165 bars any counterculture form before Step 7, the phrase is a tolerances finding (FIND-P7-22), and *none sited* is a result under the no-forced-fit law
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-281 (raised by A R3 (c) · B R3 (c) · Q-106 (B)).

### DEC-999 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-282)
- **Question.** **Section 7, speech marker:** add *never a sound* (Phase 8 L233: speech markers, none sited)?
- **Recommended (PROVISIONAL).** **No:** the cell already names the marker as knowledge; whether any sounded marker exists waits with the slang for the CST
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-282 (raised by A R3 (c) · B R3 (c)).

### DEC-1000 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-283)
- **Question.** **Section 8:** list the spine's three parent-addressed lacks or Step 5's input list (FIND-S5-3)? And insert under a header that asks what the city *refuses*?
- **Recommended (PROVISIONAL).** **Step 5's input list,** which is reconciled; **insert with *no refusal written*,** so the header's word is not read as the city's choice
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-283 (raised by A R3 (c) · A item 3 · Q-102 (B) · Q-C208).

### DEC-1001 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-284)
- **Question.** **Section 9, Lens:** the phase's differentiation axis (FIND-P9-46) or its lens findings (FIND-P9-1 to FIND-P9-4, which Phase 9 L428 names as a separate object)?
- **Recommended (PROVISIONAL).** **The differentiation axis,** as written; the developer may read the column as the lens findings, and the cell would then be replaced
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-284 (raised by A R3 (c) · B R3 (c) · C R3 (c) · Q-C206).

### DEC-1002 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-285)
- **Question.** **Section 9, more than kind:** add a second category, being needed by the archive (FIND-P9-36)?
- **Recommended (PROVISIONAL).** **No, for now:** the archive's cross-kind line is already in the cell; add it only if the developer reads the column as every such category
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-285 (raised by B R3 (c) · C R3 (c)).

### DEC-1003 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-286)
- **Question.** **Section 10:** write Step 5's narrowing (*from decay, not from loss*) into the catalog axis?
- **Recommended (PROVISIONAL).** **No:** the wording is the developer's (Q-208); the narrowing rides in the source line and enters the cell only with the developer's wording
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-286 (raised by A R3 (c) · C R3 (c) · Q-C204).

### DEC-1004 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 6 (Q-287)
- **Question.** **Section 3:** August alone as the seasonal worst point, without the human body's thinnest air (June to August) or a human's first polar night?
- **Recommended (PROVISIONAL).** **Yes, August alone:** one coldest mean is what the source counts; the others are a body's worst points, not the season's
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/06_Differentiation.md`, Questions for the developer, Q-287 (raised by A item 2 · Q-103 (B) · Q-C201; B R3 (a) toward the altitude clause).

### DEC-1005 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-288, Gate 0)
- **Question.** The contract's and frame's question tables (contract L249 Q-3, L251 Q-5; frame L208 "all unanswered") state positions from before `DR-143`.
- **Recommended (PROVISIONAL).** add a dated note at the end of each file, moving no cited line, pointing to the audit's §5 (L154–173); not an erratum, since the lines were true when written.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-288 (raised by B 126).

### DEC-1006 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-289, Gate 1)
- **Question.** Was every row of the candidate list researched (LAW 0-P), not only the official picks at Step 3?
- **Recommended (PROVISIONAL).** record that Phase 10's stage B researched rows 1–85 of the whole pick list, row 86 waiting by your ruling (Gate 7), so LAW 0-P is met at Phase 10 for this pass, while Step 3's own list held the official picks only on the day the law was ruled; confirm it on the LAW 0-P coverage tracker.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-289 (raised by C 219).

### DEC-1007 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-290, Gate 2)
- **Question.** Step 3 has no research target on the robot majority's own needs.
- **Recommended (PROVISIONAL).** at the next research round, add machinery-and-materials targets that bear on the robot body without setting a robot threshold (`DEC-697`; research Q-66), and record that the skew is partly structural.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-290 (raised by B 142).

### DEC-1008 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-291, Gate 4)
- **Question.** Which Q1 finding is weakest under the swap: *Snow without weather* (A), the Phase 2 axis (B) or the spine clause "only the work that is its purpose can ever be stopped" (C)?
- **Recommended (PROVISIONAL).** record all three as the weak set; keep the spine clause as a consequence, not the identity sentence's carrying clause, pending Q-55 and Q-96.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-291.

### DEC-1009 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-292, Gate 6)
- **Question.** Are *the stores* the archive's physical holdings, food stores, or both?
- **Recommended (PROVISIONAL).** split them in the pass: sample and core stores (possibly the archive's physical part, its form unwritten, REQ-79) and food stores (research FIND-37, RF-74); which is which stays open until Phase 10 and your word.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-292 (raised by C 227).

### DEC-1010 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-293, Gate 9)
- **Question.** The losing side of "a condition, not a filter" (P3 FIND-P3-45): a shadow candidate?
- **Recommended (PROVISIONAL).** no new candidate for *being kept*: Phase 7 FIND-P7-36 (L722–736) writes it (she is kept in body and never becomes the teacher); Phase 3 carries one line pointing there. The losing side of *belonging* goes with Q-310.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-293 (raised by A 40; B 144; C 226).

### DEC-1011 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-294, Gate 9)
- **Question.** May frame RF-24 (staffed against settled) close, now that P3 FIND-P3-54 writes it as two registers inside one Settlement?
- **Recommended (PROVISIONAL).** yes: "written as registers; the type stays Settlement; no dual typing", with P3 L254 as the record; reopen only if a later phase finds an institution that controls who is present.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-294 (raised by A 39).

### DEC-1012 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-295, Gate 9)
- **Question.** Restate the shared "no term" once, at a single source: "no term to Upper Earth; departures within the nation unwritten (RF-30)"?
- **Recommended (PROVISIONAL).** yes; correct the source findings (ERR-8 to ERR-16, ERR-48) and let later phases cite the corrected form.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-295 (raised by A 41).

### DEC-1013 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-296, Gate C)
- **Question.** Is "the city's own genetics research folder", tagged for Phase 7 (P3 L27), the folder `06` quarantines for the whole run (frame L23–24; runbook L2074)?
- **Recommended (PROVISIONAL).** the orchestrator confirms by name; if it is, the tag is withdrawn and Phase 7 is checked for any use of the folder (Q2 found the geneticist not an input, `DR-143` item 7, but did not check the folder).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-296 (raised by A 34).

### DEC-1014 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-297, Gates C and F)
- **Question.** Where does the real station's practice fall on research Q-63's line?
- **Recommended (PROVISIONAL).** answer Q-63 as recommended; keep CONV-1's member as access and infrastructure and the borehole's history as inherited record (CR-29); strike FIND-12's greens sentence and FIND-25's winterers clause, which are crew life. No finding's conclusion changes.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-297 (raised by B 140; A's watch item).

### DEC-1015 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-298, Gate C)
- **Question.** When Q-56 (the lake's length) and Q-61 (the falls/lands split) are answered, apply each at once to every line that carries it?
- **Recommended (PROVISIONAL).** yes: spine L62, L107, L110, L133 and contract CR-2, CR-32, CR-33; reword "what falls stays" on the measured figures, which make the argument stronger.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-298 (raised by C 228).

### DEC-1016 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-299, Gate G)
- **Question.** Settle the picks' provenance before Step 8?
- **Recommended (PROVISIONAL).** answer research REQ-53 / Q-65 (spine REQ-36): when and on what basis the three picks were set, and whether they came from the struck genetics line; until then keep G7 counted as independent with the doubt stated, and every genetics direction G7-only and PROVISIONAL (RF-43).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-299 (raised by C 229).

### DEC-1017 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-300, The station-builder scan, all sub-units)
- **Question.** How far does runbook L2944's denial rule reach: a treaty article paraphrased inside a finding (P2 L195); a guard on inference or an operator named only to be set aside (spine L109, L187; P3 L274; P5 L279; P8 L229; P6 L380); a real station's practice carried as the city's (the world clock, P7 L485, P4 L184)?
- **Recommended (PROVISIONAL).** the rule binds inside findings, catalog items, cells and recommended answers: strike the operator clause or write the positive rule ("a coordinate only (`DR-19`)"; "is in no listed line (RF-46)"). Input dispositions, foreclosure columns and canon-opened bookkeeping may keep their prohibitions, and even there need not name the operator. The world clock is site history, and its Gate 3 erratum (ERR-49) stands either way.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-300 (raised by Q1 A 38, B 145, C 225; Q2 A Q-A1, B Q-B101, C 202).

### DEC-1018 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-301, The station-builder scan)
- **Question.** FIND-P2-46: rewrite it flat (A, B) or withdraw it to the post-ULM census review (C)?
- **Recommended (PROVISIONAL).** rewrite it flat (ERR-22): the missing row is the city's own table's fact, and withdrawing it would leave the census review without it; the station appears nowhere in it.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-301.

### DEC-1019 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-302, Gate 0)
- **Question.** P4 L23 counts 5 + 2 + 1 = 8 against DS4's "7 of 7".
- **Recommended (PROVISIONAL).** count addresses: the robot-biology folder is one address read through two files (RP and the cold file); correct L23 with a dated note, moving no cited line.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-302 (raised by C 201).

### DEC-1020 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-303, Gates 1 and 5)
- **Question.** Refuse, waste and the city's discards are unwritten in Phases 4–10, and no line says why.
- **Recommended (PROVISIONAL).** write nothing in-run; record at Step 10 that they are not written and, if a standing content boundary governs them, cite it as the reason; the physics of what sinks under the snow joins REQ-212.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-303 (raised by Q2 A Q-A3; Q3 C's question 203).

### DEC-1021 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-304, Gate 2)
- **Question.** P5 L377, "Every body arrives by Hwy 37": about arrivals only (B), or an overclaim (C)?
- **Recommended (PROVISIONAL).** apply ERR-42; one clause removes the doubt.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-304.

### DEC-1022 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-305, Gate 3)
- **Question.** P6 L338–339, "every death here is a resident's":
- **Recommended (PROVISIONAL).** apply ERR-47 (minor).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-305.

### DEC-1023 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-306, Gate 6)
- **Question.** Which tier holds heat and warm charge: the baseline (P4 L170; P7 L301–302), the survival sector (P7 L370–373), or both by scale?
- **Recommended (PROVISIONAL).** both by scale (every city's floor in the baseline, the extra this cold demands in the survival sector); say so in one clause in FIND-P7-8; derive no split figure in-run.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-306 (raised by A Q-A4).

### DEC-1024 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-307, Gates 6 and I)
- **Question.** Name the one mechanism written as membership, the forward debt, the standard of worth, learning and belonging, and the mark of being from here (P5 FIND-P5-35; P6 FIND-P6-4, FIND-P6-7; P7 FIND-P7-29; P8 FIND-P8-32) once, and class it inflected?
- **Recommended (PROVISIONAL).** yes: one structure seen from five phases, named once at Phase 10 or Step 10, RF-137 the parent with RF-131, RF-160, RF-161 and RF-174 as its aspects; classed inflected from the national mentor and mentee bond (RP L418), with the forward debt and Phase 9 FIND-P9-35 (Q-336).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-307 (raised by A Q-A5; B Q-B104; C 213).

### DEC-1025 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-308, Gate 6)
- **Question.** The shaft's watch: the keepers' function or the research's?
- **Recommended (PROVISIONAL).** follow Phase 4's Q-112: set row (i)'s *who is present* to "the night's keepers, a function (row (l))"; the structure stays the research's, its watch the keepers'.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-308 (raised by C 205).

### DEC-1026 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-309, Gate 9, shadow candidate)
- **Question.** Membership can lapse when someone stops being needed (P5 L413–414).
- **Recommended (PROVISIONAL).** write that whether being needed, once reached, can lapse is not written; carry it to Phase 9 and the DCI; write no status rule; hold it as a shadow candidate until answered.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-309 (raised by A Q-A6).

### DEC-1027 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-310, Gate 9)
- **Question.** Narrow "a condition, never a filter" (P4 L200; P7 L642–646) to being kept?
- **Recommended (PROVISIONAL).** yes, by one clause in FIND-P4-13 and FIND-P7-27: "never a filter for being kept; the same knowledge marks belonging (Phase 5 FIND-P5-35)"; the permanent newcomer (P7 L726) is that filter's written losing side.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-310 (raised by A Q-A7).

### DEC-1028 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-311, Gate 9, shadow candidate)
- **Question.** If the purpose yields first, does the shaft yield?
- **Recommended (PROVISIONAL).** no: the shaft is excepted (ERR-50); the yielding is a pause with a route back for the instruments only, and SH-22 is checked with that exception.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-311 (raised by B Q-B103).

### DEC-1029 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-312, Gate 9, shadow candidate)
- **Question.** What is the point of entry to membership for a robot built here or a human born here?
- **Recommended (PROVISIONAL).** for a robot built here, Phase 9 writes it conditionally (FIND-P9-13, if a chamber stands, PV-5: she comes online as the newest arrival); for a human born here it stays a null; hold it with Q-327 and write no rite or status.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-312 (raised by B Q-B102).

### DEC-1030 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-313, Gate 9)
- **Question.** Once arrivals stop, whoever came last has no one newer, ever (P7 L655).
- **Recommended (PROVISIONAL).** already reserved: Phase 9's SH-35 (L475) writes that if arrivals slow, the last to come stays newest; cite it from Phase 7; no new candidate.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-313 (raised by C 210).

### DEC-1031 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-314, Gate 9)
- **Question.** P7 L894 and P8 L289 dispose of an objection as "refused, `unmet`" before the Review Panel runs.
- **Recommended (PROVISIONAL).** reword to "refused under the peer-free test; its disposition is the Review Panel's (Step 8)"; Step 8 disposes freely.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-314 (raised by C 203).

### DEC-1032 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-315, Gate F)
- **Question.** Does the outpost's power from the national tower's regulated grid (P5 L290) belong to the city's height, the grid being fully online at about 2688 and the height dated before it?
- **Recommended (PROVISIONAL).** hold FIND-P5-14 and its uses (P7 L398–399, L443, L465) as written, with a note that the grid's reach at the height is undated, until you place the height; draw no date (RF-18).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-315 (raised by A Q-A2).

### DEC-1033 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-316, Gate 0)
- **Question.** Rows 31 and 84: taken or not?
- **Recommended (PROVISIONAL).** taken, as extends notes on nulls (their cells and the extends section already say so): 38 taken, 18 not; both rows classed alike (ERR-75). For Gate 7 both are ornament either way.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-316 (raised by A, B; C would move them).

### DEC-1034 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-317, Gate 0)
- **Question.** Phase 10 L1025 marks the Parent position covered on a reading Step 5 holds open.
- **Recommended (PROVISIONAL).** follow Q-235's recommendation: leave the Parent unmarked until answered; the count reads 2.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-317 (raised by B 104).

### DEC-1035 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-318, Gate 2)
- **Question.** The catalog's people lean to the research layer (10 of 21 roles).
- **Recommended (PROVISIONAL).** accept it for this pass as the pick list's effect; note it at Step 10; let the CST, which writes what people do in a day, carry the general population's roles; write no role for them in-run.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-318 (raised by C's question 201).

### DEC-1036 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-319, Gate 2)
- **Question.** Narrow CAT-1's "so the honor is paid daily, not once" (Phase 10 L689–690)?
- **Recommended (PROVISIONAL).** yes, to "the district is where the city's own scientists work"; the honor stays a name only.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-319 (raised by A Q9).

### DEC-1037 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-320, Gate 3)
- **Question.** "No sky edge" against the measured noon twilight, and Phase 4 FIND-P4-40 (L266)?
- **Recommended (PROVISIONAL).** one docket line beside REQ-170: "for about 243 days no sunrise or sunset bounds the day; in the polar night a faint noon twilight marks midday, not when to stop", touching P4 FIND-P4-5, FIND-P4-64 item 1 and Phase 9 FIND-P9-15, FIND-P9-19 by note only; FIND-P4-40 joins RC-58's reading as it stands (A's alternative: amend L266 to "the only light enough to work by is the city's own; the sky holds a faint noon twilight and the moon's week").
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-320 (raised by B Q-B103; A E3).

### DEC-1038 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-321, Gates 3, 4 and 11)
- **Question.** FIND-P10-9, the threshold as "the city's most dangerous ordinary place":
- **Recommended (PROVISIONAL).** narrow it to "the threshold is where a kept thing, and the hands carrying it, are most at risk", since its one research leg is about cryogen transfers.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-321 (raised by B).

### DEC-1039 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-322, Gate 3)
- **Question.** CAT-26's source rests on one reader's off-list read of Phase 7 L578.
- **Recommended (PROVISIONAL).** the orchestrator confirms Phase 7 L578 at source (one line), then ERR-81 is applied; Phase 4 L397 does not carry the claim on any reading.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-322 (raised by A; C (c)).

### DEC-1040 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-323, Gate 4)
- **Question.** The Phase 10 axis's peer-free "Yes": FAIL (A), FLAG (B, C) or PASS; and which finding is weakest (the catalog axis, FIND-P10-9 or FIND-P10-6)?
- **Recommended (PROVISIONAL).** amend both "Yes" answers to "In part" (ERR-85), the practice being shared and the rates the site's; record the three as the weak set; the gate stays FAIL until the amendment is applied.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-323.

### DEC-1041 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-324, Gate 6)
- **Question.** Does the gate reach things and roles named twice, or institutions only; are the lake program and "the genetics program" one; fold CAT-35 into CAT-2, or cross-reference?
- **Recommended (PROVISIONAL).** the gate is about institutions, so the item doubles are bookkeeping: cross-reference a setting and its recurring event (CAT-56/CAT-72; CAT-59/CAT-71), merge the role doubles (CAT-78's second half into CAT-36; CAT-50 into CAT-77) and fold CAT-35 into CAT-2 (ERR-86); treat the lake and genetics programs as one research program by applying REQ-169.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-324 (raised by B Q-B105, Q-B106; A; C).

### DEC-1042 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-325, Gate 7)
- **Question.** The share's definition and base.
- **Recommended (PROVISIONAL).** report the whole-list share (27 of 85 = 31.8%), the PRIMARY-tier share and the official picks (3 of 3) every time, and adjust none; an *extends* note is ornament unless it changes a finding's wording, standing or scope; rows 43 and 45 follow CAT-B2-8's fate (ERR-90); add a changed · ornamented · withheld · omitted column to the pick-incorporation tables so the gate need not class them afterward.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-325 (raised by A Q2; B Q-B101; C's question 206).

### DEC-1043 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-326, Gate 8)
- **Question.** The place-specific standout beside SC-1: SC-4 (A) or SC-3 (B, C)?
- **Recommended (PROVISIONAL).** SC-4, the archive's two signals: it stands on a ratified line (spec L179) and on Phase 9 and 10 findings, while SC-3 rests on PROPOSED readings and absences; record SC-3 beside it, and SC-4's no-signal leg as a contested absence wherever it is cited.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-326 (raised by A Q1; B Q-B107; C's question 207).

### DEC-1044 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-327, Gate 9, shadow candidate)
- **Question.** Membership held by the road or a chamber (A15).
- **Recommended (PROVISIONAL).** yes, reserved beside SH-35 and SH-37, weaker than textbook (no adverse outcome written); no practice.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-327 (raised by A Q4).

### DEC-1045 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-328, Gate 9, shadow candidate)
- **Question.** No written way into the research population for a resident outside it (FIND-P9-36; RF-183).
- **Recommended (PROVISIONAL).** write that how such a resident is first asked is not written; keep RF-183; hold it as a candidate, no rule.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-328 (raised by A 16).

### DEC-1046 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-329, Gate 9, shadow candidate)
- **Question.** A long pause carries the research population across the city's one between-group line (kept, not needed).
- **Recommended (PROVISIONAL).** yes, reserved, conditional on REQ-145 and on FIND-P9-36's line; no rule.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-329 (raised by A Q5).

### DEC-1047 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-330, Gate 9, shadow candidate)
- **Question.** Link Phase 6 SH-25 (the keepers of heat stand in no record) to FIND-P10-1 (the one honor names the scientists) as one candidate?
- **Recommended (PROVISIONAL).** yes, reserved; no honor, roll or practice written.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-330 (raised by A Q6).

### DEC-1048 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-331, Gate 9, shadow candidate)
- **Question.** The clean side's way out is unwritten (CAT-B1-1).
- **Recommended (PROVISIONAL).** reserve it with RF-194 for the DCI, and write its losing side, the one who cannot complete instruction (Phase 7 FIND-P7-36), with it.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-331 (raised by A 19; B).

### DEC-1049 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-332, Gate 9, shadow candidate)
- **Question.** FIND-P10-15's request path: the unanswered sender.
- **Recommended (PROVISIONAL).** yes, weaker than textbook; who decides which requests are answered waits for the DCI, and the unanswered sender is written beside the one who comes in person.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-332 (raised by B Q-B108).

### DEC-1050 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-333, Gate 9, shadow candidate)
- **Question.** The unchosen successor in single custody (FIND-S5-7).
- **Recommended (PROVISIONAL).** yes, weaker than textbook, reserved with RF-212.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-333 (raised by C's question 204).

### DEC-1051 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-334, Gate 11)
- **Question.** C's FAIL on yearly lifting against A's and B's FLAG; and carry the tonnage and the induction-scale question to Step 10?
- **Recommended (PROVISIONAL).** the FAIL stands until ERR-82 is applied; carry the city-scale pricing of raising (about 990,000 to 1,417,500 tonnes of snow a year on the 44–63 km² extent) and the scale question on perpetual induction to Step 10 as pricing and scale notes, not findings; the shared-night plausibility point goes with Q-255.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-334 (raised by A Q7).

### DEC-1052 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-335, Gate C)
- **Question.** Is a dated correction to a shared sheet within Gate C's applied-list rule, or a Gate 0 matter (B)?
- **Recommended (PROVISIONAL).** within it: a statement corrected at one source is corrected wherever it is carried; record the datasheet's L21 under Gate 0 as well; ERR-87 stands either way.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-335.

### DEC-1053 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-336, Gate I)
- **Question.** Reclass Phase 9 FIND-P9-35 (the order of arrival) from genuinely emergent to inflected?
- **Recommended (PROVISIONAL).** yes: it inflects the national mentor bond, cited in the finding itself, and Phase 2's perpetual induction; the substance is unchanged (with Q-307).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-336 (raised by A Q3).

### DEC-1054 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-337, The station-builder scan)
- **Question.** Phase 9 L202, a method bar that names the operator before denying it.
- **Recommended (PROVISIONAL).** rewrite it to the positive rule, "Founders come only from the Founding Register (`DR-19`)."; nothing is lost.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-337 (raised by B Q-B109; A and C hold it as method).

### DEC-1055 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-338, The station-builder scan)
- **Question.** Step 5 DK-3 proposes keeping the culture sheet's sentence that the station operators' nation has no representation in any tier.
- **Recommended (PROVISIONAL).** strike it from the sheet's prose: a census row count needs no mention of whose station it was (`DR-19`; runbook L2944).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-338 (raised by A Q8; C's question 205; B clears it).

### DEC-1056 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 7 (QA gates) (Q-339, Gate 3)
- **Question.** Add to Q-225's scope the other lines that carry city-scale staying (Phase 9 FIND-P9-33's heading L330, Phase 9 L254, Phase 9 L413, Phase 10 Q-B2-2's reason L1916 and Q-211's premise L1208)?
- **Recommended (PROVISIONAL).** yes; each to read "no departure from the city is written" and, for the human, "could not return to Upper Earth"; the same rule as Q1's Gate 9 errata (Q-295).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md`, Questions for the developer, Q-339 (raised by B Q-B104; A A11).

### DEC-1057 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-340)
- **Question.** May a position that cannot be cast be voiced from its edge case? Readers voiced the Child as a conditional human child, a robot built here, or a human born here.
- **Recommended (PROVISIONAL).** no. Record the result (`00f` L757–764). Keep any edge-case voice as data, `noted`, and never let a disposition write a child into the place.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-340 (raised by R1·A A-Q-4; R1·B 131; R1·C 242; R2·A 23; R3·A 19; R3·B Q-B105; R3·C C-Q1; Round 3 (c) in R1, R2 and R3).

### DEC-1058 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-341)
- **Question.** Is a human born here at the height to be written?
- **Recommended (PROVISIONAL).** not in-run. Phase 9's reading and Phase 2 Q-73 and Q-74 govern, and REQ-242 lists what would have to be re-read.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-341 (raised by R2·A 23).

### DEC-1059 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-342)
- **Question.** The Elder's casting.
- **Recommended (PROVISIONAL).** the city's casting is *a holder at the end of her holding*. Where she is a robot of the founding wave, the long life is labeled as national canon and the casting as conditional on `DEC-698`. The oldest keeper of the shaft (CAT-78) is kept as R3·C's costume. The human elder stays uncastable, and the ledger's Elder cells stay blank (REQ-241).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-342 (raised by R1·C 241; R2·B 125; Round 3 (c) at R2·B, R2·C, R3·B, R3·C).

### DEC-1060 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-343)
- **Question.** Can the subnet's coastal hub be cast as a Neighbor? The city names it as its parent (spine D-4; frame PV-8), but no trade or contact is written.
- **Recommended (PROVISIONAL).** cast it only as a relation on paper, able to ask what flows. Its one objection (O-42) is `noted` to Phase 5. That no flow is written confirms spine D-4 and RF-52 from outside either way. Record that one reader found it uncastable. The hub is never named.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-343 (raised by R1·A A-Q-3; R1·B 115; R1·C 213; R2·C 220; Round 3 (c) at R1·A).

### DEC-1061 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-344)
- **Question.** Does `DR-143` L2063 item 1 ground an `unmet` for the honor objection (O-28)?
- **Recommended (PROVISIONAL).** no; `declined`. The ruling shows the honor knowingly placed with the city's scientists. It does not show the keepers knowingly left unnamed, and honoring them would not remove the scientists' honor. *If the developer reads it otherwise:* `unmet` +1, on that line.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-344 (raised by R1·C 216, 240, withdrawn; R2·A 24; R2·B 126; R2·C 232; Round 3 (c) at R2·B).

### DEC-1062 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-345)
- **Question.** Does a passer-through meet the district's name at all (O-40)?
- **Recommended (PROVISIONAL).** no line makes the name visible to someone crossing in a day, so the objection is `declined`. R3·B withdrew its version of it. *If the developer rules that she does:* `DR-143` item 1 grounds an `unmet`, and the count rises by one.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-345 (raised by R1·B 113; R3·B 112, Q-B104; Round 3 (c) at R1·A, R1·B, R3·A, R3·C).

### DEC-1063 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-346)
- **Question.** Does the district's honor stay with the scientists (Phase 6 Q-138 (b)), so that the keepers' absence from it is written as characterization and not as a gap?
- **Recommended (PROVISIONAL).** yes. If the developer widens the honor, re-decide O-28.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-346 (raised by R2·B 126; R2·C 232).

### DEC-1064 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-347)
- **Question.** Does spec L179 show the place knowingly holding an understanding spread across people, so that the Mentor's refusal (O-30) would be `unmet`?
- **Recommended (PROVISIONAL).** no; `declined`. The line is the spec's descriptive voice, not the place's own.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-347 (raised by R1·A A-Q-1).

### DEC-1065 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-348)
- **Question.** Should the spine sentence's first clause (*holds what others come to it for*, L229; Q-45) be narrowed (O-14)?
- **Recommended (PROVISIONAL).** keep the sentence's shape. Read the clause as the purpose's claim. It is written in the world for the research arrivals (Phase 5 L396) and as others coming or sending (FIND-S5-9). Its *send to it* half has one written form only, the Mandated share, which has no in-world form (Phase 5 L450; RF-38). Keep §8e's *Be necessary* conditional on Phase 5's flows (REQ-10; RF-48).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-348 (raised by R1·A A-Q-2; Round 3 (c) at R1·A, R1·C).

### DEC-1066 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-349)
- **Question.** May a later stage write that robots of the founding wave may be living at the height, so that the founding is possibly in living memory?
- **Recommended (PROVISIONAL).** only as conditional, under `DEC-698`. Phase 9 FIND-P9-21 already holds it. It is a role, never a named person, and never a founding-wave standing or privilege (RF-8, RF-27, RF-78).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-349 (raised by R1·B 132; Round 3 (c) at R1·C).

### DEC-1067 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-350)
- **Question.** Should the night's keepers go to the DCI as one carried question: who keeps the heat, water, charge and shaft through the shared night, how many keep it, and when they rest?
- **Recommended (PROVISIONAL).** yes. Fold it into RF-108's handoff, as a function only (`DR-137` item 12), citing FIND-S8-9.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-350 (raised by R1·B 133).

### DEC-1068 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-351, Worth in two tenses (FIND-S8-4).)
- **Question.** Should it enter as a refereed finding, with *the part kept back to stay needed* as a shadow candidate?
- **Recommended (PROVISIONAL).** yes, as structure only, scoped to the research population. Enter it as a shadow candidate weaker than textbook, with no practice or person. When Gate 9 is next run, it asks of the holder who has taught on everything she held.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-351 (raised by R2·B 124; R2·C 231).

### DEC-1069 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-352)
- **Question.** Should Step 7's shadow count weigh FIND-S8-14 as one shadow with six sites?
- **Recommended (PROVISIONAL).** yes, for weight, keeping every site and its number and retiring none. R1·B's further sites stay candidates until Step 7 reads them.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-352 (raised by R2·C 229; Round 3 (c) at R2·B, R2·C).

### DEC-1070 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-353)
- **Question.** May the Lover position be cast on the treaty draft's election ground?
- **Recommended (PROVISIONAL).** yes, for the casting only, tagged `[treaty draft]`. No finding rests on it.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-353 (raised by R1·C 243).

### DEC-1071 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-354)
- **Question.** May the Passer-Through be cast from Hwy 37's through-line (CAT-10 when no through-traffic is written (Phase 2's null; Q-211, Q-212)?
- **Recommended (PROVISIONAL).** yes, as a standpoint for the discoverability check only, never as a population. The ledger cell stays blank until REQ-153.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-354 (raised by R3·A 18; R3·B Q-B102; R3·C C-Q4).

### DEC-1072 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-355, May a position be cast by function)
- **Question.** (the Parent as someone answerable for a dependent who cannot keep herself alive) when its life stage is unwritten?
- **Recommended (PROVISIONAL).** yes, for the panel's run only, recorded as such. The ledger's Parent cell is not marked by it (Q-189, Q-235, REQ-153).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-355 (raised by R3·A 19; R3·B Q-B103; Round 3 (c) at R3·A).

### DEC-1073 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-356)
- **Question.** The door's decision for the untaught (O-12). Should it enter as a strengthening note on Phase 7 FIND-P7-15?
- **Recommended (PROVISIONAL).** yes, as structure only, labeled as resting on the pass's own paraphrase (Phase 6 L193). No line makes it so, and no rule or practice is written. It stays `noted` until ruled.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-356 (raised by R2·C 203; Round 3 (c) at R2·A).

### DEC-1074 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-357)
- **Question.** The Elder's "no way down": `noted` or `declined`?
- **Recommended (PROVISIONAL).** split it. The way down as a departure is `noted` to Phase 5 and the DCI (O-24; a departure is unwritten, not barred). A place or role for whoever can no longer work, or is no longer needed, is `declined` (O-25; FIND-S8-13).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-357 (raised by R1·A 28; R1·B 111; Round 3 (c) at R1·A).

### DEC-1075 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-358)
- **Question.** The late Lover-faculty verdict's wording.
- **Recommended (PROVISIONAL).** *alive, yes; lovable, not yet shown*, with the glimpses written beside it as candidates. It moves one step only when a line writes someone loving the place, or a pleasure taken in a stopped hour.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-358 (raised by Round 3 (c) at R1·B and R1·C; R2·B).

### DEC-1076 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-359)
- **Question.** Should FIND-S8-3 (the store colder than the city's own cold, in the class that cannot stop) be accepted?
- **Recommended (PROVISIONAL).** yes, conditional on the research keeping living stock (RF-209), as a reading beside FIND-S5-2. No pass file is edited.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-359 (raised by R3·C C-Q2).

### DEC-1077 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 8 (Review Panel) (Q-360)
- **Question.** Should the pass's in-phase `unmet` labels be re-labeled `declined` (REQ-239)?
- **Recommended (PROVISIONAL).** yes. They rest on the city's composition, cold, road and archive. Those are facts about the place, not lines showing that it knowingly holds anything. Re-labeling changes no finding's substance.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/08_Review_Panel.md`, Questions for the developer, Q-360 (raised by R2·A 22; R3·A 17; R3·C C-Q3; Round 3 (c) at R3·C).

### DEC-1078 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-361)
- **Question.** Step 9's state in the new tracker lines: "in progress" or "PROPOSED"? (A·R3 (c).)
- **Recommended (PROVISIONAL).** PROPOSED, as written by this merge, because the record exists when the line is applied (orch.).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-361.

### DEC-1079 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-362)
- **Question.** Is `RUN_PROGRESS_Ariun_Nuur.md` a tracker under Step 9 item 3, or the run's resumable log? (A 22, B 145, C 292; A·R3 (c).)
- **Recommended (PROVISIONAL).** the run log (`09.5_Log.md` L4–5 makes it the holding place while a unit's list is frozen). Its closing status line follows item 3's one-line form; per-reader results stay out of that line and are never copied into MASTER.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-362.

### DEC-1080 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-363, A pointer line beside MASTER L391–395?)
- **Question.** L394 reports *Round 2 UNANIMOUS* for units that first failed Round 2; L394–395 carry substance beyond one line; L391's *validated and corrected* is contradicted in part (A 22, C 214; A·R3 and B·R3 (c) on L391).
- **Recommended (PROVISIONAL).** yes, one dated pointer line beside them, naming AN-09, AN-10, AN-14, AN-15 and AN-18 for the first-run failures, AN-21 and ERR-87 for the sheets, and `DR-144` for the law's substance; rewrite nothing.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-363.

### DEC-1081 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-364)
- **Question.** Fold this city's five dated MASTER lines behind one pointer? (A 66.)
- **Recommended (PROVISIONAL).** yes, but only on the developer's word, since it changes existing lines; add the new line first and change nothing else until then.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-364.

### DEC-1082 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-365)
- **Question.** The ledger's Parent *rel.* cell at Phase 10. (A 67, B 146, C 294; B·R3 (c); orch.)
- **Recommended (PROVISIONAL).** leave the Parent unmarked at Phase 10, with a dated note, until Q-235 and Q-317 are answered: a subnet called a parent is not the Parent position.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-365.

### DEC-1083 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-366)
- **Question.** Does the ledger record the late Lover faculty's verdict? (B 147.)
- **Recommended (PROVISIONAL).** no cell; at most a status-note pointer to `08` L877.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-366.

### DEC-1084 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-367)
- **Question.** One ID-only queue for in-run notices about other locations? (B 144, C 293; orch.)
- **Recommended (PROVISIONAL).** yes: one ID-only queue (for example a section of the decisions file), read only at the terminal check; the record lists the IDs and the queue's address, so propagation is recorded now and routed later (REQ-202).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-367.

### DEC-1085 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-368)
- **Question.** Do the panel's redirected charges on shared things (`08` L646–647, L731–732) count as relation items to propagate? (C 207; B·R3 (c).)
- **Recommended (PROVISIONAL).** list them by line in the queue as candidates, not as findings about another location; the terminal check decides.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-368.

### DEC-1086 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-369)
- **Question.** Is Q-175's methodology half (a note in a methodology commit after the run) Step 9 item 4's to discharge? (C 210; C·R3 (c).)
- **Recommended (PROVISIONAL).** no. Step 9 drafts the entry (`M-449`) and hands the change on to the end-of-run methodology commit and the developer; a draft records the point but does not make the change (B·R3; orch.).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-369.

### DEC-1087 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-370)
- **Question.** Does a positional PROOF line that carries a character's working name need the EXEMPT line? (A·R3 (c).)
- **Recommended (PROVISIONAL).** yes, whenever a positional line carries any name the reader would not otherwise reproduce; it costs one line.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-370.

### DEC-1088 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-371)
- **Question.** Is the city's former name, which is also a real station's name, a forbidden name in readers' text? (C·R3 (c), on B 115.)
- **Recommended (PROVISIONAL).** yes outside positional PROOF fields: mask it, as two readers did; the station is a coordinate only.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-371.

### DEC-1089 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-372)
- **Question.** Are a determination's category words forbidden, or only a specific symbol? (C·R3 (c), on B's draft M-432, merged here as `M-433`.)
- **Recommended (PROVISIONAL).** only a specific member is forbidden; a category word names none.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-372.

### DEC-1090 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-373)
- **Question.** Does Step 9 discharge Step 10 deferrals, or only hand them on? (A 64.)
- **Recommended (PROVISIONAL).** only hand them on. Step 9 discharges what is addressed to Step 9 or to the close, and confirms that every Step 10 deferral sits on a Step 10 list.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-373.

### DEC-1091 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-374)
- **Question.** Should a split Review Panel cast its positions once, city-wide, before dispatch (`M-421`)? (A 68, C 219.)
- **Recommended (PROVISIONAL).** yes, for the next city: one casting sheet frozen into every sub-unit's brief, open to readers' objection in Round 1.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-374.

### DEC-1092 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-375)
- **Question.** Reformat the rulings log so each item sits on its own line (`M-424`)? (B 148, C 223.)
- **Recommended (PROVISIONAL).** yes for new rulings; leave old rows as they are, with a note. The log's format is the developer's.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-375.

### DEC-1093 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-376)
- **Question.** Is the national-connections file ever admissible in-run (`M-432`)? (B 149.)
- **Recommended (PROVISIONAL).** no, while its method reads other locations; build in-run inputs from the shared things' own records.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-376.

### DEC-1094 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-377)
- **Question.** Should the ledger's header require the casting's line beside each mark (`M-452`)? (C 242.)
- **Recommended (PROVISIONAL).** yes, from the next city.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-377.

### DEC-1095 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-378)
- **Question.** The Step 9 datasheet's L9 clause (*in the phase file itself, never only in a log*): where is its source? (B 150; C·R3 confirmed.)
- **Recommended (PROVISIONAL).** cite the runbook line, or drop the clause from the corpus-wide sheet (Tier U; the developer's).
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-378.

### DEC-1096 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 9 (Record) (Q-379)
- **Question.** Apply the proposed rule changes (§5) in the methodology commit at the end of the pass? (C 296.)
- **Recommended (PROVISIONAL).** yes, each after the developer confirms it, recording what was learned on this city; none is applied by this step.
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/09_Record.md`, Questions for the developer, Q-379.

### DEC-1097 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 10 (readiness check) (Q-380)
- **Question.** The 48 unbanded memory files that name the next subject. Band them, or record that a warm run does not need it? *Recommended, PROVISIONAL:* before 2026-11-29, a shape-only check of the four with the most hits (scan L39, L37, L43, L83) and of the two whose names carry the subject (scan L39, L46); band any entry that states the place's character, temperament or a signature phrase. For the rest, record that a warm run does not need the memory blackout (runbook L3189). (orch.; A Q4, B 115, C·R3 (a))
- **Recommended (PROVISIONAL).** (see the source)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/10_Readiness_Check.md`, Questions for the developer, Q-380.

### DEC-1098 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 10 (readiness check) (Q-381, Retrieval in a warm run.)
- **Question.** Should the next run carry *"Graphify not used (DR-6)"*, as this run did (entry 7 L121), although warm passes normally use it? *Recommended, PROVISIONAL:* yes, or at least no graph query about its own subject before its culture check, because the own-culture-last rule has no enforcer in a warm run (runbook L3189) and a retrieval layer cannot honor it (L3138). (C 325; (c) in all three Round 3 replies)
- **Recommended (PROVISIONAL).** (see the source)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/10_Readiness_Check.md`, Questions for the developer, Q-381.

### DEC-1099 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 10 (readiness check) (Q-382, `Test_Runs/` under item 8.)
- **Question.** Does a folder barred to readers count as *quarantined* under M-0? *Recommended, PROVISIONAL:* no. The bar is on reading; the orchestrator appends to the observations file without reading its neighbors, which keeps M-0's purpose. No move. (A Q3; (c) in all three Round 3 replies)
- **Recommended (PROVISIONAL).** (see the source)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/10_Readiness_Check.md`, Questions for the developer, Q-382.

### DEC-1100 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 10 (readiness check) (Q-383, The form of the handoff fix.)
- **Question.** A dated pointer line appended to the handoff's §3 (B), a new closing handoff created as its own file (A), or the next handoff carrying this file's cannot-prove section (C)? *Recommended, PROVISIONAL:* the dated pointer line, append only, pointing to RUN_PROGRESS, `09_Record.md` and this file, since it edits no existing text and the window-close summary already points here (orch.). (A·R3 and B·R3 (c))
- **Recommended (PROVISIONAL).** (see the source)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/10_Readiness_Check.md`, Questions for the developer, Q-383.

### DEC-1101 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 10 (readiness check) (Q-384, The helpers' durable home.)
- **Question.** Is `Tools/Orchestrator_Helpers_Ariun_Nuur_2026-11/` their only home, with the handoff pointing nowhere else? *Recommended, PROVISIONAL:* yes; the committed helpers are there (orch.), and this session's new helpers join them at the window close. (C 335; A·R3 (c))
- **Recommended (PROVISIONAL).** (see the source)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/10_Readiness_Check.md`, Questions for the developer, Q-384.

### DEC-1102 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 10 (readiness check) (Q-385, The drafted method changes.)
- **Question.** Which will you confirm or refuse before 2026-11-29, given that the next pass follows the rules, not the log? *Recommended, PROVISIONAL:* decide first on those the next run's own briefs and instruments use: `M-419`, `M-425`, `M-433`, `M-445`, `M-450`, `M-417`, `M-418`, `M-421`, `M-442`, `M-443` and `M-439`; apply what you confirm in one methodology commit with the runbook, with *learned on Ariun Nuur* beside each; leave the rest for the end-of-run methodology commit, and let the next handoff say plainly that none is in force until then. (A Q2, B 124, C 333)
- **Recommended (PROVISIONAL).** (see the source)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/10_Readiness_Check.md`, Questions for the developer, Q-385.

### DEC-1103 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 10 (readiness check) (Q-386, Deferral row 2 (the energy source).)
- **Question.** Does `DEC-705` need anything further, or does the gap stand by ruling? *Recommended, PROVISIONAL:* it stands by ruling; no new question. (C·R3 (c))
- **Recommended (PROVISIONAL).** (see the source)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/10_Readiness_Check.md`, Questions for the developer, Q-386.

### DEC-1104 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 10 (readiness check) (Q-387, When is a listing deferral done?)
- **Question.** *Recommended, PROVISIONAL:* only when the state it conditions on (*still open*, *if still open*, *as carried*) has been re-read at source and the listing written; until then it is handed on with its line, as here. (A·R3 (c))
- **Recommended (PROVISIONAL).** (see the source)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/10_Readiness_Check.md`, Questions for the developer, Q-387.

### DEC-1105 · PROVISIONAL · 2026-11-20 · Ariun Nuur, Step 10 (readiness check) (Q-388)
- **Question.** This run's band notice in the memory index (L5). Retire it when the run ends? *Recommended, PROVISIONAL:* yes, once the run is recorded and committed, asked first, since it is an edit to an existing line. (B 125; C·R3 (a))
- **Recommended (PROVISIONAL).** (see the source)
- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/10_Readiness_Check.md`, Questions for the developer, Q-388.

## Answered
*(Moved here with the date and the ruling number.)*
- 2026-11-18, `DR-142`: DEC-660 to DEC-672 answered in place above (as recommended, except DEC-666: the source errors fixed now).
- 2026-11-15, `DR-137`: Casey's 23 Phase 3-10 questions answered in place above (DEC-522 to DEC-544; DEC-532 in part, the cold-damage science pending research).
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
