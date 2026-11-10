# Davis: section F checks of 2026-11-09 (one Opus reader per item)

**What this is.** The result of the check the plan asks for (`DR-104` item 3, `DR-106`): for each item in section F of the amendment note, one reader asked whether the pass's conclusion changes on the current inputs. Each reader had only its own frozen brief and a trimmed reading list of Davis's own material, and read in its own session; no reader saw another's output. **Everything here is PROPOSED.** No pass file was edited. The verdicts are the readers' judgments about dependence, not tests; they send an item to re-derivation, they do not settle it.

**Where the detail is.** Each reader's whole output (its reasoning, quotations, the case for and against, and its PROOF blocks) is kept beside this file as `.t8_check_<ID>_reader.md` (for example `.t8_check_C1_reader.md`); the frozen brief and reading list are `.t8_check_<ID>_brief.md` and `.t8_check_<ID>_required.txt`; the input pin is `.t8_check_manifest_2026-11-09.txt`. This file reproduces each reader's decision block unchanged.

**Names.** This file names no other city. Another location: not used.

## Mechanical check of the readers' proof of reading (Round 2 form, one reader per file)

`Tools/triple_read_verify.py` was run on each output with that reader's file in all three slots (the tool is built for three readers; with one, it checks each PROOF field of that one reader against the file on disk). Result for all 12 outputs: every field of every PROOF block matches ground truth, verdict `UNANIMOUS - CLEARED TO WRITE` (read as: every PROOF field matches; the tool's word `UNANIMOUS` here means only that the one reader's file agrees with itself). The 38 pinned input files were re-hashed after the readers finished: none changed.

## Summary

| Item | Verdict | Confidence | Output lines |
|---|---|---|--:|
| C-1 | FLIPS | medium | 227 |
| C-2 | NARROWS | medium | 264 |
| C-3 | NARROWS | high | 209 |
| C-4 | NARROWS | high | 245 |
| C-5 | FLIPS | high | 316 |
| C-6 | NARROWS | medium | 234 |
| C-7 | NARROWS | high | 187 |
| U-1 | FLIPS | medium | 173 |
| U-2 | NARROWS | high | 192 |
| U-3 | NARROWS | medium | 115 |
| U-4 | NARROWS | medium | 142 |
| U-5 | NARROWS | high | 190 |

Totals: FLIPS 3, NARROWS 9, STANDS 0, CANNOT-TELL 0. Confidence: high 6, medium 6, low 0. **No item came back `STANDS`; none came back `CANNOT-TELL`.** `FLIPS` and `NARROWS` both send an item to re-derivation (brief section 4); the readers' bias is toward re-derivation by the brief's own rule, so a `NARROWS` can mean one false sentence, not a changed finding. The piece plan reads each reader's own words, not the label alone.

---

## Item C-1 — FLIPS (medium)

*Reader output: `.t8_check_C1_reader.md`, 227 lines. The decision block, unchanged:*

VERDICT: FLIPS
CONFIDENCE: medium
AFFECTED PASS SENTENCES: P2:L224, P2:L226-228, P2:L231-232, P2:L234, P2:L236-237, P2:L242-244, P2:L244-246, P2:L247-249, P2:L250-251, P2:L254-258, P2:L324-326, P2:L329-332, P2:L342, P2:L344-345, P2:L585-587, P2:L592, P2:L631, P2:L1400, P2:L1598-1599, SPINE:L250, INH:L70
- Same ground, outside the cited locations (listed for routing; not used for the verdict): P2:L301-302 (tier table: "Primary | 1 | China"), P2:L305-306 (inherited 19.04% / 4.93%), P2:L309 ("roughly one person in five"; now about one in ten), P2:L349 ("largest at 19.04%"), P2:L374 (B.0: "classifiable for about 5% of its founding population", which rests on the tag as a route datum), P2:L1438 ("the marker is the only route datum in the whole composition block"), SPINE:L107-108 ("largest at 19.04%"; "the founding population is 4.93%").
- Confidence: high that this item must go to re-derivation (it is not STANDS); medium on FLIPS over NARROWS (see Snags XC1-34).
- Ground for FLIPS: the item bundles two conclusions. (1) The reading of the tag, as an in-world arrival annotation and the only cell that says "when", is contradicted by CENSUS:L33, LOG:L1555 and LOG:L1660. (2) The founding/plurality contrast survives only once restated (founding nation against the Primary tier, with no single nameable plurality), and its host, later-wave and precedence consequences lose the ground they were derived on. On its own, (2) would be NARROWS. The pass pre-declared that losing the in-world arrival reading of the tag means H-2 must be re-run (P2:L254-255, L1400).

WHAT A RE-DERIVATION MUST ASK:
- XC1-25. How does the founded slot read at Davis now that the Register supplies it (Australia, on geography and access; REGISTER:L59)? How is the stock slot written for 45 origins, five of them Primary, when no single plurality may rest on a same-tier gap (DR-104 item 1)?
- XC1-26. With the tag carrying no arrival information, does anything in admitted canon tell any origin's arrival apart from another's? If nothing does, how are A.2's "route datum", A.3's layer call and B.0's "classifiable for about 5%" restated?
- XC1-27. Is the failure of the host/guest model still a finding, and on which ground: weight of numbers (69,475 people, 5.74%, not a majority, outside the Primary tier, stated by headcount per DR-104 item 2), the absence of any recorded order of arrival, or both?
- XC1-28. On what source does "no later wave / no later arrival" now rest, given that the census dates no row? Is it written as an inference, as B.4 does, rather than as a fact, as H-2 L244 does?
- XC1-29. Does "no precedence politics can form" survive when a possible ground of precedence is a Register designation ("establishing country") rather than an order of arrival? Does any source say whether that designation is known or carries standing in-world, asked once for Act 1 and once for Act 2 as fire #3 requires?
- XC1-30. H6 appears closed by CENSUS:L33 and LOG:L1555/L1660. What does the pass record in its place, and what replaces the third doubt (P2:L1598-1599)?
- XC1-31. What is fire #3 (INH:L70) now? A hole with no "between" (no arrival waves, dates, order or mechanism for any of the 45 origins), or still a gap between two terms?
- XC1-32. How is a re-derivation kept from reading the rows the rework added by time-zone window (SPEC:L28, dated) as later arrivals, consistent with A.3's dated-means-authoring test and DR-104 item 2? And how is it kept from reading the Register's basis ("extremely close… comparatively easy access") as an arrival route?
- XC1-33. Does the Register's Davis row record whether the founder nation also sent people (the question DR-99 item 1 settled for another location: not used)? The last cell of REGISTER:L59 is "—", and the column header is outside my admitted range. Does any restated H-2 sentence need that answer? (The composition already shows an Australia row of 69,475 people at Census I.)

NEEDS FROM THE DEVELOPER:
- XC1-D1. Does DR-104 item 1's bar ("no finding rests on a gap between two nations of the same tier") leave cross-tier statements free? For example: "the founding nation's row, 5.74%, sits outside the five Primary rows." **Recommended answer: yes, cross-tier statements are permitted when written as headcounts and grounded on the tier boundary the spec states (SPEC:L78). The bar applies only within a tier.** (DR-12's full text is not in my list, so I cannot confirm this from the source.)
- XC1-D2. Does the "establishing country" designation (LOG:L1660) have any in-world meaning at Davis, such as being known to residents or conferring standing on people of that origin? **Recommended answer: nothing is canon. A re-derivation leaves the slot explicitly open (no forced fit) and restates D5 as "no arrival-based precedence can form; whether the founding designation carries any standing is unstated".**

**Answers to tests (a) to (d).**
- (a) The core contrast survives only in restated form: the founding nation (Australia, 5.74%) is not among the five Primary origins (46.39% together). "Two different communities" survives as founder nation against the bulk of the stock. It does not survive as founder community against one plurality community, because the first is no longer arrival-defined and the second is no longer nameable.
- (b) No longer following from the sources: in H-2, "founding-wave community … 4.93%", "Primary-tier community … 19.04%", "plurality-Chinese", "that form has one slot … no correct single instantiation", "too small to host" stated as absolute, "no later stocks because there was no later arrival", "arriving all at once and never being followed", and the precedence mechanism's scope. In H6, the binary itself (in-world content or authoring note) and the A.3 ground for its answer ("undated, and it names a mechanism"; "the only arrival annotation"). The question is now answered by ruling, on neither branch.
- (c) The tag licenses nothing about route, timing, order or waves (CENSUS:L33; LOG:L1555; LOG:L1660). It licenses one statement: Australia is the nation named as Davis's founder in the Register, on geography and access (REGISTER:L59; NNS:L9). Under REGISTER:L8-10, a pass should cite the Register for that, not the tag.
- (d) The share (5.74%, 69,475 people at Census I) supports "not a majority, and outside the Primary tier", so it cannot host by weight of numbers. It does not support "too small" in absolute terms. It has no bearing on "no later wave follows", which no input in my list supports. It supports the absence of majority-based and arrival-based precedence, but not "no precedence politics can form" as a universal, because the designation-based ground is unaddressed.

---

## Item C-2 — NARROWS (medium)

*Reader output: `.t8_check_C2_reader.md`, 264 lines. The decision block, unchanged:*

VERDICT: NARROWS
CONFIDENCE: medium
AFFECTED PASS SENTENCES: 04_Phase_02:948, 04_Phase_02:949, 04_Phase_02:949-950, 04_Phase_02:951, 04_Phase_02:955, 04_Phase_02:957-958, 04_Phase_02:960, 04_Phase_02:963, 04_Phase_02:972, 04_Phase_02:975, 04_Phase_02:1014, 04_Phase_02:1448, 04_Phase_02:1482. What is wrong at each:
- 04_Phase_02:948 (≈220,543 is false; current 126,123)
- 04_Phase_02:949 (≈57,105 is false; current 69,475)
- 04_Phase_02:949-950 ("Not one of the 21 lacks numbers…": the count is wrong and the claim is ungrounded for the ten rows of 152 to 1,162)
- 04_Phase_02:951 (the model-output caveat is superseded by `DR-104` item 1; this line is one past the cited range but inside C.2)
- 04_Phase_02:955 ("21 substantial communities": the count is wrong; "substantial" is ungrounded for the small rows)
- 04_Phase_02:957-958 ("sustained internally at full strength": ungrounded for the small rows)
- 04_Phase_02:960 ("twenty-one communities")
- 04_Phase_02:963 ("twenty-one-fold, fully staffed, carried at full scale": false as a universal over 45 rows)
- 04_Phase_02:972 ("Stock: twenty-one": the count is wrong, and the rows are not one-stock-per-row; see XC2-15)
- 04_Phase_02:975 ("acts identically on all twenty-one stocks": the count is wrong; true of the mechanism, not of its yield)
- 04_Phase_02:1014 ("21 origins": the count only; "organize nothing" stands)
- 04_Phase_02:1448 (≈220,543 is false; the kill stands on 126,123)
- 04_Phase_02:1482 ("the 21 origins": the count is wrong, and the item now bears directly on whether the small rows can carry assembling forms)

WHAT A RE-DERIVATION MUST ASK: nine questions, (a) to (i).
- (a) For each of the 45 rows, by its own headcount at both censuses, with no cutoff: does it carry the forms that need people to assemble (a liturgy, a street, a kitchen, a conversation), and does it carry its practices from one generation to the next or only the portable and household ones?
- (b) What do real-world comparables say about the size a small minority or diaspora community inside a large city needs to sustain such forms? This needs web research; no recalled figure may stand in for it.
- (c) Does the killed draft survive in a narrowed scope for rows below that size, and how does that meet C.4's lapse mechanism ("a second person who would notice")?
- (d) What is the unit of an origin practice? Which practices are shared across rows from one split country (carriers pooled), which belong to one row alone (its headcount only), and which regional practice-sets sit inside one merged row (the Sinian Federation's nine states and two cities; Korea's two halves)?
- (e) For each successor row, what is the stock: the people of the in-world latest-period unit, as Census Section E says, rather than the real-world nation of the same name (the Finland and Hungary rows in particular)?
- (f) Do a row's robots carry its origin practices (hole `H2`)? If not, is the carrier count for some practices the human headcount alone (74 to 567 for the ten smallest rows at Census I; 57 to 435 at Census II)?
- (g) Does spatial co-location decide whether a row of a few hundred people has "a street", and is that deferral still in force?
- (h) With what size qualifier is "fully staffed, carried at full scale" true, and should "acts identically" become "acts by one mechanism, with a yield set by each row's own headcount"?
- (i) Does the national-language line at LOG:1527 (the Tepenian language is "at its foundational level core, a Pidgin between English and Japanese") bear on PASS:959-960's claim that the civic layer "cannot be inherited from any stock"? It is national context, so it is never a differentiator, but the C.3 wording should be checked against it.

NEEDS FROM THE DEVELOPER: three questions, (1) to (3), each with a recommended answer.
- (1) Does the pass's `DR-4` bar on distributional results still apply to Phase 2, now that `DR-104` says Phase 2 reasons by headcount with no cutoff? Concretely, may a re-derivation qualify the two-layer conclusion by naming rows by their own headcounts ("rows of a few hundred people")? **Recommended answer: yes.** Reading each row's own headcount flatly against a researched threshold is reasoning by headcount, not a spread, a mode or a gap between nations. Keep the bar on spread, mode and spatial claims until it is lifted.
- (2) For a successor row, is the origin stock the in-world unit's people or the real-world nation named? **Recommended answer: the in-world unit's people, read through Census Section E.** The real-world culture of that territory serves as the comparable, with the divergence operator applied, and never the name alone.
- (3) May rows from one split country be pooled when sizing the carriers of a practice they share? **Recommended answer: yes, as an aggregation inside Davis's own table.** It is not a ranking or a gap between nations. Each row's own distinct practices are still sized on that row alone.

---

## Item C-3 — NARROWS (high)

*Reader output: `.t8_check_C3_reader.md`, 209 lines. The decision block, unchanged:*

VERDICT: NARROWS
CONFIDENCE: high
AFFECTED PASS SENTENCES:
- `04_Phase_02_Composition_and_Arrival.md:1071-1072`: "Davis's 21 origins are not a sample of humanity. They are a sample of *where robots were*." The count is false (45). The sample claim survives only once restated as territorial labels.
- `:1073-1074`: "The composition of Davis is a fossil record of the pre-exile global distribution of robot manufacture, employment and residence." Misstated in two ways. Membership is placed partly by time-zone window. Sizes come from headcount splits, income-estimated pools and random multipliers, and the robot column copies human proportions (SPEC L78). "Global" and "manufacture, employment" are unsourced. It survives at most as membership.
- `:1075-1076`: "FIRE #11 FORBIDS IT." The conclusion stands; the stated ground is superseded (SPEC L78; LOG L1703 items 1-2). It needs re-grounding on SPEC L78.
- `:1079`: "Davis's block lists 21." False: the block lists 45 (SPEC L20-22; Census L394-396).
- `:1077-1078` (needs a qualifier, not false): "presence in Tepenia's origin set is downstream of having had a robot population" should say it is read by ground, not by the latest-period label's polity.
- `:1067` and `:1069-1070` (pre-existing, not caused by the changed input): "and therefore no human ones either" and "Tepenia's entire origin stock is, by construction, the origin stock of the robot-holding world" hold only if a human's origin row records residence at departure. II.2.3 (Treaty L48) ties the human to the robot population, not to their own place.

WHAT A RE-DERIVATION MUST ASK:
1. With all 45 rows as origins and no cutoff (DR-104 item 2), what exactly is the unit of "origin" in E.1? Is it a 2564 polity, a latest-period territorial label (Census L841), or a place of residence at departure?
2. Does the membership inference attach to the ground or to the polity? Does the argument still hold for split labels (Tibet, Tuva, Patani and the others), merged labels (Mongolia), and labels that carry a former parent's people (Finland, Hungary)?
3. Since some places are folded into other rows (Hong Kong and Macau into the Sinian Federation; North Korea and Jeju-do into Korea; China's pieces into the Sinian Federation outside their windows), what, if anything, may E.1 say about any absence?
4. Given that membership at Davis is partly placed by time-zone window and that sizes come from headcount splits, income-estimated pools and random multipliers, what is left of the third order? Is it a windowed membership record, or should it be dropped?
5. With the robot column defined as the human proportions (SPEC L78) and tiers defined from final shares, what ground now carries the refusal to read rows or tiers as robot density?
6. For human exiles, does the step from "no robots" to "no human exiles" hold under II.2.3, given that no ground in II.2.3 is tied to the human's own place? Should it be stated as conditional?
7. Does "manufacture, employment and residence" have a source beyond II.2.1's residence and coming-into-being?

NEEDS FROM THE DEVELOPER:
- **XC3-15 · What does a human exile's origin row record: nationality, or the place they lived before departure?** Recommended answer: no new ruling now. Let the re-derivation state the human half of E.1 as conditional ("holds if origin means residence at departure"), since the treaty's human grounds (II.2.3) are ties to the robot population and not to a place.
- **XC3-16 · Should origin rows be read in-world as latest-period territorial labels rather than as 2564 polities?** Recommended answer: yes, as Census L841 already says for the tables. The treaty argument runs on ground (II.2.1 is territorial), and the exclusion criterion is defined by having no robots, so the answer does not depend on where the atlas's latest period falls relative to 2564.

---

## Item C-4 — NARROWS (high)

*Reader output: `.t8_check_C4_reader.md`, 245 lines. The decision block, unchanged:*

VERDICT: NARROWS
CONFIDENCE: high
AFFECTED PASS SENTENCES: `01_Inherited.md:87-88`; `01_Inherited.md:274`; `04_Phase_02_Composition_and_Arrival.md:50`; `04_Phase_02_Composition_and_Arrival.md:318`; `04_Phase_02_Composition_and_Arrival.md:319` (conditional, the word "share-weighted" only); `04_Phase_02_Composition_and_Arrival.md:320`; `04_Phase_02_Composition_and_Arrival.md:324`; `02_Spine.md:116` (conditional, "share-weighted" only); `02_Spine.md:117` (first sentence only)

**What is wrong in each:**
- **`01_Inherited.md:87-88`.**
  - The ground is false for 43 of 45 rows (L1703). "de-stacking" names a table that SPEC L28 says was replaced.
  - "Corroborated twice independently" corroborates that withdrawn ground.
  - The scope "No two nations' figures... at any precision, in either direction" is wider than the bar the ruling records.
- **`01_Inherited.md:274`.** "the de-stacked per-nation ordering" names the old table. The instruction survives for orderings within a tier.
- **`04_Phase_02:50`.**
  - "guard 2 make per-nation comparison inadmissible at any precision" rests on the withdrawn ground and has too wide a scope.
  - "deliberately not used" runs against `DR-12`'s ADMITTED-DEMOTED, "readable" disposition (L474) and against `DR-104(2)`.
  - The fire #2 half of the sentence stands.
- **`04_Phase_02:318`.** Same ground and scope defects as `01:87-88`. "any two of the 21" is also a stale count: there are 45 rows, all of them origins (`DR-104(2)`).
- **`04_Phase_02:319`.** The core ("identical across both censuses BY CONSTRUCTION"; which communities left is unanswerable; the absence is an artifact) stands. Only "share-weighted" is uncertain against SPEC L78.
- **`04_Phase_02:320`.** "0.009 pp" is false. The current spread is 0.79 to 1.33 pp across 45 rows and 0.024 to 0.047 pp across rows at 1% or more. The rest of the line stands.
- **`04_Phase_02:324`.**
  - "19.04% and 4.93%" are not the current figures.
  - "a sole-occupant tier's own share, not an ordering" is false: the Primary tier has five rows, and naming the largest is a same-tier ordering that the draw can reverse.
  - "safe under all six" therefore fails for the first figure.
  - The second figure's "in-world annotation" leg cannot be told from my list (CENSUS L33).
- **`02_Spine.md:116`.** It stands, apart from the "share-weighted" uncertainty.
- **`02_Spine.md:117`, first sentence.** "No two nations' figures may be compared at any precision, in either direction" is wider than the kept bar. Its stated ground here, construction identity, supports only a ban on comparing how many of each nation left. The second sentence (`02_Spine.md:117-118`, "an artifact, not a finding") stands.

**Noted outside the cited lines, not counted here.** These rest on the same inputs and probably belong to other items:
- `04_Phase_02:236`'s plurality clause names a row that is no longer the largest, and naming the largest is now barred.
- `04_Phase_02:305`'s 19.04% and 4.93% are stale.
- `04_Phase_02:317` and `01_Inherited.md:78`: the "production weight" premise is reversed by SPEC L78.
- `04_Phase_02:948-951`'s scale check ("Not one of the 21 lacks numbers for a liturgy, a street, a kitchen or a conversation") meets rows of 152 to 240 people.
- `04_Phase_02:1360-1361`: "~0.009 pp" is stale.

WHAT A RE-DERIVATION MUST ASK:
1. What bar does Davis now carry, stated on its kept ground (weights for derivation, headcounts in the world) rather than on randomization?
2. Which bar is it: the developer's recorded bar (same-tier gaps) or the pass's all-pairs bar? (See XC4-Q1.)
3. For each per-nation statement Phase 2 makes, which of these does it rest on: a same-tier gap, tier membership, the city totals, or one row's own headcount? Which of these are legal?
4. Which orderings change when the Sinian Federation's and Manchuria's draws change? In particular, can any statement name Davis's largest origin, given that the top two rows share a tier and one of them is randomized?
5. What can be said about the largest share without naming its nation? Examples: no majority; about one person in ten.
6. How does "reason by headcount, with no cutoff" (`DR-104(2)`) sit beside the seal? What use of a row's headcount is not a comparison between two nations?
7. What is the current rounding spread, row by row? Below what row size is it large enough to be mistaken for a real difference in who left? How should the guard be worded so no reader takes it as one?
8. Is "share-weighted" still the right description of the construction now that the 8/3/1 weights no longer produce the figures? What sentence should replace it?
9. What figure replaces 4.93%? Does the founding-wave row's level standing with Indonesia, in the same tier, bar any statement that sets the two against each other?

NEEDS FROM THE DEVELOPER:
- **XC4-Q1 · Which bar was kept?**
  - `DR-104(1)` records the kept bar as `DR-12`'s: "no finding rests on a gap between two nations of the same tier". The pass's bar is wider: "No two nations' figures may be compared, at any precision, in either direction" (`01_Inherited.md:87`; `02_Spine.md:117`; `04_Phase_02:318`). When you chose "Keep the bar, re-ground it", was the bar kept the recorded one or the pass's wider one?
  - **Recommended answer: the recorded text governs.** Barred: a gap between two same-tier nations, including which of the top two rows is larger, and the founding-wave row against Indonesia. Also barred, separately and by construction (fire #2): any difference between nations in who left. Allowed: contrasts across tiers at the precision of the tier, and any single row's own headcount, stated flatly, as `DR-104(2)` directs.

---

## Item C-5 — FLIPS (high)

*Reader output: `.t8_check_C5_reader.md`, 316 lines. The decision block, unchanged:*

VERDICT: FLIPS
CONFIDENCE: high
AFFECTED PASS SENTENCES:
- Row C-5 (heritage relations):
  - 04_Phase_05:35. Both disqualifications as stated: the current Davis line no longer cites the withheld file, and the namesake thread never grounded the tie (`DR-32`). "Neither recorded" is too broad.
  - 04_Phase_05:36. "Same withheld root"; "A structural exclusion, not a search gap. No admissible independent route exists; searching harder will not surface one."; "escalate for a ruling on partial Megasheet declassification", which is moot for the Register-and-map basis.
  - 04_Phase_05:72-73. "Three are disqualified at the source ... The three that survive are all scientific, and canon writes each as a prospect".
  - 04_Phase_05:79. The quotation is not in Davis's current line, CONN:314-315.
  - 04_Phase_05:103-105. "the flagged material removes the heritage relations entirely".
  - 04_Phase_05:114. "And any heritage relation admissible to this pass", listed under "What does NOT flow".
  - 04_Phase_05:303-304. "in any form — withheld-Megasheet root AND reserved-person territory, two independent disqualifications".
  - 04_Phase_05:305-306. "same withheld root, checked and confirmed to have no independent route".
  - 04_Phase_05:330 (H31). "A structural exclusion, not a search gap. Requires re-derivation or a ruling on partial declassification".
  - 04_Phase_05:346. "the heritage relations are structurally excluded, not missing".
  - 04_Phase_05:383-385. "removed for cause, and the removal is structural rather than evidentiary — the material may be perfectly true and simply unavailable to a pass run under these rules".
  - 04_Phase_05:359 (§10 item 5). "a third source was ACTIVELY SEARCHED FOR and does not exist". The Register and `DR-32` are now that independent source.
  - 04_Phase_05:26-27. Stale line citations: CONN's Davis section is now L303-315, and XSUB's entries are now L123-131.
- Outside row C-5 (port and air inputs in my list; reported for routing, not counted in this verdict):
  - 04_Phase_05:202. The quoted port text is not in PORTS:559, and "Roughly five months open, seven shut" is contradicted by "year-round, icebreaker-dependent".
  - 04_Phase_05:23 and 04_Phase_05:203. "Davis holds a confirmed airport marker", contradicted by AIR:50 and AIR:56.
  - 04_Phase_05:269. "by road and air"; the air part is contradicted by AIR:50.
  - 04_Phase_05:275-277, 04_Phase_05:309 and 04_Phase_05:329 (H30). PORTS:559 now states an import port with inbound raw materials, so "It does not state that the port exists for imports" is false.
  - 04_Phase_05:332 (H33). Its nearest candidate is now partly answered by PORTS:559.
  - 04_Phase_05:345. "the airport" listed as a nameable feature.
  - 04_Phase_05:22. The quoted port text is not in PORTS:559. The tier's own definition is outside my range, so I cannot tell whether that part still holds.
WHAT A RE-DERIVATION MUST ASK:
- XC5-27. For each of Davis's six lines at CONN:303-315, what is the stated basis now? Does any of them still lean on the station, its operator, a namesake, a subnet nickname, or the withheld file?
- XC5-28. For each heritage tie, does Davis's own line state a relation (a mechanism, a dependency, a direction or a flow), or only a shared founder? What survives the one-sentence test once the partner's name is deleted?
- XC5-29. Should a tie that stands on the Register and the map (`DR-32`) be recorded as a relation whose content is a hole, or as a demoted population-origin finding (brief rule 4)? Either way, exclusion is not an option. Which treatment fits each of the three lines, given that CONN:308 rests on presence ("among the exile groups present"), not on founding?
- XC5-30. What, if anything, do Davis's own lines say flows along Hwy 110 between Davis and its two direct highway neighbors? Does a heritage tie change 5a's flow table, or only its "does NOT flow" row?
- XC5-31. How are canon's grades ("Strong", "Medium") and type labels recorded without turning them into a ranking of Davis?
- XC5-32. Which parts of XSUB:123-131 stay out (the withheld description, the post-frame severance and survival), and does anything there survive on the Register-and-map basis alone?
- XC5-33. Does H31 close, and does a new hole replace it (for example, what passes along the heritage ties)? How should the headline count at PH5:72-73 and the second doubt at PH5:383-386 be restated?
- XC5-34. Is the freighter note at RELDB:193 a Davis relation (an inbound flow from the founding nation as an Upper-Earth supplier)? How does it square with PORTS:559's transshipment route, and with 5a's inflow row, H30 and H33?
- XC5-35. Does CONN's file-level sourcing statement (outside this check's range) still say it builds on the withheld file? If so, does the Davis section stand anyway on REG:59, HWY:199 and `DR-32`?
- XC5-36. Does the third scientific line (CONN:314-315), once its ranking is stripped, still carry any relation? Is the headline "largely unwritten" (PH5:83) still the right statement on the corrected count?
- XC5-37. Does any heritage tie bear on 5d (who arrives by road, the meaning of "outsider")? Or must that stay out unless a Davis line states it?
NEEDS FROM THE DEVELOPER:
- XC5-38. Is a shared founding nation, stated in Davis's own relation line and confirmed by `DR-19`, a relation for a single-location run, or only a population-origin fact? Recommended answer: record it as a tie whose basis is the Register and Hwy 110 (`DR-32`), state no sameness or similarity, mark what flows along it as an open hole, and treat it as demoted, never excluded.
- XC5-39. May CONN's grades ("Strong", "Medium") be carried into the pass? Recommended answer: carry them only as canon's own wording about the tie, attributed to the source, and never as a ranking of Davis.
- XC5-40. Do the port and air contradictions in 5d (PH5:202, PH5:203 and related lines) belong to another item in section C? Recommended answer: yes, route them to the port and air items. If no such item exists, open one, because AIR:50/56 and PORTS:559 contradict the pass outright.
- XC5-41. RELDB:193 (staging via Hobart/Fremantle) and PORTS:559 (transshipment via the French Southern and Antarctic Lands and Heard Island and McDonald Islands) disagree on the inbound route. Which governs? Recommended answer: PORTS:559, which carries a developer ruling, governs. Flag RELDB:193 for a source correction, and have the re-derivation record the conflict without choosing.
- XC5-42. Does XSUB:123-131, whose Davis entries still cite the withheld file for the tie's character, need a source fix? Recommended answer: flag it for the source-fix list, and do not edit it in the re-derivation. No declassification ruling is needed, because the Register and `DR-32` already give the basis.

---

## Item C-6 — NARROWS (medium)

*Reader output: `.t8_check_C6_reader.md`, 234 lines. The decision block, unchanged:*

VERDICT: NARROWS
CONFIDENCE: medium
AFFECTED PASS SENTENCES:
- **XC6-23. At the cited locations:**
  - 04_Phase_08_Making.md:247: "21-fold" is out of date (45 rows, DR-104 (2)). As the premise of the language section, "a thin, procedural civic layer" is also unsourced, because a ruled common language now sits over the composition too.
  - 04_Phase_08_Making.md:248: the city-level half of the deferral is superseded by DR-100. Only the community-level half stands, and its ground is now DR-100 (5), not DR-4.
  - 04_Phase_08_Making.md:250: "it is not an accent" is unsourced on the current inputs.
  - 04_Phase_08_Making.md:255: the negative half, "NOT HOW THEY PRONOUNCE IT", is unsourced. The positive half stands.
  - 04_Phase_08_Making.md:256: "not a dialect" is unsourced.
  - 04_Phase_08_Making.md:259: the exclusive "the one Davis marker" is unsourced.
  - 04_Phase_08_Making.md:320: "21" is out of date, and H48 is half-answered by DR-100.
  - 04_Phase_09_Populations.md:92: the Module delivers a vernacular, and the dominant language is Hawaiian. The claim-register is not what the Module delivers.
- **XC6-24. Outside the cited locations, not counted toward the verdict, for the re-derivation's attention:**
  - 04_Phase_06_Meaning.md:203: "the only thing the whole city does the same way" now competes with a shared dominant language.
  - 04_Phase_08_Making.md:292: the list of shared items leaves out the ruled common language.
  - Bare "21" counts at 04_Phase_06_Meaning.md:204, 04_Phase_08_Making.md:294, 04_Phase_09_Populations.md:77 and :96.

**XC6-25. What the language rule now lets those sentences say (PROPOSED, not applied):**
- **E.1 (L247-248):** "Hawaiian (later Tepenian) is the dominant language at Davis, as it is everywhere (DR-100 (1)). Davis's supporting tier is English, Mandarin, Japanese and German. These are languages in which business, social talk and general dealings can be done, and which people can be assumed to follow (DR-100 (2)-(3); Language_Blocs L922-L926). What each of the 45 origin communities speaks among itself is not written. The tier is computed from origin shares, not speaker counts, and the nation-to-language mapping is unverified (DR-100 (5))."
- **E.2 (L250-259):** keep "what marks someone as from Davis is how they make a claim", and add "in whichever of its languages they make it". Drop "not an accent", "not how they pronounce it", "not a dialect" and "the one marker", or hold them as open questions pending research.
- **Phase 9 L92:** "The Module tracks the dominant local culture and the community who had her built. A Davis-born robot's vernacular is Hawaiian, plus her building community's language where that differs (developer to confirm). The claim-register is something she shares with every resident by living here, in whichever language she speaks."
- **H48 (L320):** "Answered at city level by DR-100: Hawaiian is dominant; English, Mandarin, Japanese and German are supporting. Still open: what each of the 45 origin communities speaks among itself."

WHAT A RE-DERIVATION MUST ASK:
- **XC6-26.** At Davis, is DR-100's dominant language (Hawaiian, later Tepenian) the "dominant local culture" that the Language Module tracks?
- **XC6-27.** What language does the community that has a Davis robot built use, when that community is a local robot community (physiology L424)? Is the answer written anywhere admissible?
- **XC6-28.** Does a Davis robot acquire the claim-register through the Module, or by living in the city? Can Phase 9 L92 say both a language and a register without merging them?
- **XC6-29.** What does each of the 45 origin communities speak among itself? Can admitted canon answer that at all, given DR-100 (5), or does it stay an open hole on that ground?
- **XC6-30.** Does the answer to XC6-29 differ between the Act 1 and Act 2 parts of the 2564–2812 frame (No_National_Stereotypes.md L112)? Is the pass's "Davis is Act 2" framing (04_Phase_09_Populations.md:76) right for language?
- **XC6-31.** Within the frame, is the dominant language named Hawaiian throughout, or Tepenian for part of it?
- **XC6-32.** Given the supporting tier, what can §E say about code-switching, meaning which languages a Davis exchange can move between, without claiming that this sets Davis apart?
- **XC6-33.** Is there a Davis accent, contact feature or loan vocabulary in its Hawaiian or its supporting languages? This needs real web research before any claim. The research question is: what do real-world populations of many origins who share a common language show about accent, substrate features and code-switching? The divergence method's inputs (separation, environment, struggles, goals, habits) would then be applied from Davis's own data.
- **XC6-34.** Restated as a register carried across Hawaiian and the four supporting languages, is "show me the entry" independent of language? And can any of its exclusions ("not an accent", "not a dialect", "the one marker") be sourced, or must they go?
- **XC6-35.** Does German's place in the tier hold once the Austro-Bavaria-to-German mapping is checked? DR-100 (5) calls that mapping unverified, and without it German falls below the cutoff.
- **XC6-36.** Does a dominant language spoken by the whole city change Phase 6's "only thing the whole city does the same way" (04_Phase_06_Meaning.md:203) and Phase 8 §G's list of shared items (04_Phase_08_Making.md:292)?

NEEDS FROM THE DEVELOPER:
- **XC6-37.** Under the Language Module rule, is a Davis-born robot's vernacular Hawaiian, plus the language of whoever had her built? **Recommended answer: yes.** DR-100 (1) says Hawaiian is dominant "everywhere", and physiology L426 ties what the Module delivers to the language of the dominant local culture. Leave the builders' language open wherever the building community is not specified.
- **XC6-38.** Should H48's community-level half (what each origin community speaks among itself) stay an open hole, now on the ground of DR-100 (5) instead of DR-4? **Recommended answer: yes.** Do not work out home languages from origin shares; DR-100 (5) says those shares are not speaker counts.
- **XC6-39.** German's place in Davis's supporting tier depends on counting Austro-Bavaria (1.39) as German-speaking, a mapping DR-100 (5) calls unverified. Should the re-derivation carry the four-member tier as ruled and note that dependency in the amendment note? **Recommended answer: yes.** Carry English, Mandarin, Japanese and German as ruled, since the rulings as they stand govern, and record the German dependency as a flag without reopening DR-100.

---

## Item C-7 — NARROWS (high)

*Reader output: `.t8_check_C7_reader.md`, 187 lines. The decision block, unchanged:*

VERDICT: NARROWS
CONFIDENCE: high
AFFECTED PASS SENTENCES:

*At the cited locations:*
- **02_Spine.md:107**: "21 origins, largest at 19.04%" and "13 nations at Notable tier" are false (45 rows; 10.42% ceiling; 38 Notable rows). The inference "⇒ nothing load-bearing can be tacit" stands.
- **04_Phase_02:349-350**: quotes the same stale ground as the basis of A.4.
- **04_Phase_02:357-358**: "A 21-origin city can be non-tacit without being factional": the count is false.
- **04_Phase_02:354-355**: "maximally visible" is ungrounded for the smallest rows. Its scope needs restating; it is not shown false.
- **04_Phase_02:470-471**: "With no majority, a tacit norm has no carrier" is misstated in scope; it holds as "no majority origin". This gap existed before the change.

*Outside the cited locations, carrying the same input or the same conclusion:*
- **04_Phase_02:309**: "at roughly one person in five" is false; it is now about one in ten.
- **04_Phase_02:305-306**: "plurality share **19.04%**" is stale.
- **04_Phase_02:324-325**: "The first is a sole-occupant tier's own share, not an ordering." is false.
- **04_Phase_02:226-227**: "The Primary-tier community sits at an inherited 19.04%." is false.
- **04_Phase_02:236**: "plurality-Chinese" is false. Naming any plurality now also rests on a gap between two same-tier rows, which DR-104 item (1) bars.
- **04_Phase_02:948-950**: "≈220,543" is stale, and "Not one of the 21 lacks numbers..." is stale and may be false for the smallest rows.
- **04_Phase_02:955** "21 substantial communities", **04_Phase_02:961** (restates the C-7 conclusion as "the arithmetic"), and **04_Phase_02:963** "twenty-one-fold, fully staffed, carried at full scale".

*Stale counts elsewhere that do not affect the verdict:* 04_Phase_02:67, 297-303, 318, 329, 485, 592, 859-860, 972, 975, 1014, 1071, 1079, 1397, 1482, 1492. 02_Spine.md:37 is a dated record of a Round 3 correction and should be left as it is.

WHAT A RE-DERIVATION MUST ASK:
1. Should P1 be stated as a per-row ceiling ("no origin exceeds 10.42%", or 126,123 people at Census I) instead of as "the largest origin"? Naming the largest now rests on a 0.70-point gap between two Primary rows, which DR-104 item (1) bars, and one of those rows was set by a random draw (SPEC L28).
2. With no single-row tier left, what replaces the safe-use ground at 04:324-325? Does a ceiling pass all six A.2 limits as DR-104 item (1) restates them?
3. Should C1 be limited to "no majority *origin*"? SPEC L15-16 show a majority population type at each census. Can a population-type majority carry a tacit norm? This needs sources outside this item.
4. Can a tacit norm be carried by anything other than a majority origin? Candidates include a set of rows sharing one medium (the successor mapping is in census Section E), a minority placed in institutions (hole H8), the inherited record, or the work calendar. Does any such set reach a majority?
5. Reasoning by headcount with no cutoff: for rows of a few hundred people, does "explicit" mean seen, or only "explicit when stated"? Do the C.2 kill and C.3's "fully staffed" still hold? Research question: what headcount sustains a gathering practice in a city of about 1.2 million?
6. This point was already there before the change: is "FORCED BY THE ALLOCATION CRITERION" (04:469) an overstatement? The capacity criterion allows a no-majority composition, but the composition itself comes from the census.

NEEDS FROM THE DEVELOPER:
1. Four uncited places (04:305-311, 04:324-325, H-2 at 04:226-241, and C.2/C.3 at 04:939-965) rest on the same row. If no other section-C item owns them, should C-7's re-derivation take them? **Recommended:** yes for A.1 (04:309) and A.2 (04:324-325), because they are the stated ground for the figure this conclusion uses. Leave H-2 and C.2/C.3 to the item that owns them, and give them to C-7 only if none does.
2. Should the one-word scope fix at 04:470-471 ("no majority *origin*") go into this re-derivation, even though it existed before the change? **Recommended:** yes for the wording, since the sentence is at a cited location and is misstated on the current inputs. Log the substantive question (can a population-type majority carry a tacit norm) as an open hole rather than answering it in C-7.

---

## Item U-1 — FLIPS (medium)

*Reader output: `.t8_check_U1_reader.md`, 173 lines. The decision block, unchanged:*

VERDICT: FLIPS
CONFIDENCE: medium
AFFECTED PASS SENTENCES: At the cited locations: 04_Phase_07_Order.md:110 (181,808; now 186,131) · 04:112 (NOT WRITABLE, three live values; contradicted) · 04:114 ("will not resolve inside this pass"; resolved by the national file and by file 16's own baseline) · 04:118-120 (table: row 1 withdrawn, row 2 double-books against file 16's baseline, row 3 is the national files' reading; all values on the pass-time population) · 04:122-123 (the ~2× spread as "the honest reason"; ungrounded) · 04:130-132 (quotes file 16's gap as 124,972; file 16 now says 134,153, 320,284 against 186,131) · 04:407 (H39: 181,808, and "three live values spanning ~2×"; contradicted) · 05_Reconciliation.md:102 ("mandate 28.2% / free 31.1%"; file 16 now carries 27.6% / 30.5% by developer instruction). Outside the cited locations, the same refusal or the same stale figures, listed for the re-derivation and not counted in the verdict: 04:48 (every export magnitude "Gated by `DRQ-09`") · 04:388-389 (§F: no export headcount; sector 181,808) · 04:32 (09 L79 row: 876,515, 35.3%; now 915,098, 35.4%) · 04:87 (876,515) · 04:91 (181,808) · 04:99 (28.2% / 31.1%).
WHAT A RE-DERIVATION MUST ASK: (1) What does convention B (DR-73) say about own need? Does it count an exporter's whole distinctive-tier agriculture sector as export because the baseline already staffs the city's own food? Are conventions A and C of file 17 live alternatives or only records? (2) Does file 16's own formula text confirm that its baseline carries Davis's human food term at 120.7 (89,117 workers on the current population), so that subtracting own need again double-books? (3) Which run governs Davis's export headcount: the latest (186,131; 44.2%, 19:62, 19:81)? What is that run's national export-supply total, so the 44.2% can be checked? (4) Was "feeds about 1,309,000 beyond itself" (19:44) restated for the latest run, what is its people-per-worker conversion, and does it survive Finding 3's units objection (file 10)? (5) With the denominator still unsettled nationally (19:50), how is the whole-workforce alternative (320,284, 16:2092) carried beside a stated 186,131 without becoming a second headline? (6) Does H39 close, or does it narrow to the national denominator question? Does §F (04:388-389) then state the headcount? (7) Do A.2b's two grounds stand as written once the quoted gap is updated? Is "feeds any fraction of the country" statable at all, given the current national population is not in this item's inputs? (8) Does a stated export headcount alter anything that Phase 7 feeds to Phase 8, Phase 10 or Step 5 (04:417-426)?
NEEDS FROM THE DEVELOPER: (a) Only if DR-73's text does not settle it: is convention B the governing answer to Davis's own-need question, so that the pass may state its export headcount as its whole distinctive-tier agriculture sector (186,131 on the latest run, 44.2% of national export supply)? **Recommended answer:** yes. State 186,131 on file 16's convention and the 44.2% share. Carry 320,284 only as the open national denominator caveat (Register item 11). Retire the 53 and 120.7 rows as superseded, the first withdrawn and the second double-booking file 16's baseline. (b) Should the pass carry the "feeds about 1,309,000 people beyond itself" figure? **Recommended answer:** not yet. Carry the worker headcount and the share. Hold the people figure until the latest run's value and its conversion are checked against Finding 3; keep refusing "a third of the country".

---

## Item U-2 — NARROWS (high)

*Reader output: `.t8_check_U2_reader.md`, 192 lines. The decision block, unchanged:*

VERDICT: NARROWS
CONFIDENCE: high
AFFECTED PASS SENTENCES:
- Within the cited locations:
  - 02_Spine.md:94: strength cell names only "a documentary inheritance" and grounds all of it on "its subject did not change". The scope must include the inherited infrastructure (a Davis fact) and the admissible DR-26 classes. The stationary ground covers only the written half.
  - 04_Phase_02_Composition_and_Arrival.md:708: heading "OCCUPIED FOR RECORDS".
  - 04_Phase_02_Composition_and_Arrival.md:713: a two-row table with no row for infrastructure, equipment, research or techniques.
  - 04_Phase_02_Composition_and_Arrival.md:728: "A LIBRARY": the "not a soul" half stands; the "library" half is too narrow.
  - 04_Phase_02_Composition_and_Arrival.md:730-732: "a description of the ground with nobody attached to it", as the whole delivery. The "none of its account-holders" half stands.
  - 04_Phase_02_Composition_and_Arrival.md:733-737: the selection filter is stated as occupancy rather than person-to-person transmission, and "brings none" is extended to an inheritance that includes maintained infrastructure.
  - 04_Phase_02_Composition_and_Arrival.md:739-740: "the thing that was here first is a document".
  - 04_Phase_02_Composition_and_Arrival.md:742-743: "The only inherited thing was the one class of thing that confers nothing". This is false as an inventory; the conclusion survives on the corrected ground.
- Knock-on, outside the cited range (same claim, listed for the re-derivation, not used for the verdict):
  - 04_Phase_02_Composition_and_Arrival.md:632-633: "What was here first at Davis is a document".
  - 04_Phase_02_Composition_and_Arrival.md:846: "Inherited a RECORD instead".
  - 04_Phase_02_Composition_and_Arrival.md:1451: "the mode's product inverted into a record".
  - 02_Spine.md:140, conditional: the STRENGTH row "something this place was given or built and need not renew" fails for G4 if a maintained material inheritance enters G4's strength cell.
  - 02_Spine.md:438, exposed: "its METHOD is its own" must place DR-26's "carry it on as its own" category.
WHAT A RE-DERIVATION MUST ASK:
- XU2-23. Which inheritable classes does Davis's own canon state as having crossed (infrastructure: stated; journals, logs, orientation manuals: stated), and which are admissible but unstated at Davis (manifests, maps, research data and results, ongoing datasets, equipment, techniques beyond those written into the manuals)?
- XU2-24. For each class that crossed, what explains why it still works on arrival: the stationarity of the subject (written records, written techniques, datasets) or maintenance across the operator chain (infrastructure, any equipment)?
- XU2-25. Does G4 need a second strength item (a material inheritance) and a second standing cost (upkeep of inherited plant)? If so, what is its relation to Davis's own D6, "cannot make its own plant" (02_Spine.md:125, :251)?
- XU2-26. Is the in-world selection filter at the gap occupancy, or person-to-person transmission (DR-25)? What does 04_Phase_02:733-737 say once restated on that filter?
- XU2-27. Does any inherited class confer anything on Davis (capability, an obligation, a claim, a draw), and can any of them carry precedence or legitimacy?
- XU2-28. Is any part of Davis's serial observation an inherited dataset or technique that the city took up and "carr[ied] on as its own" (DR-26)? If so, where does the line fall between it and the practical mastery the spec credits to the exiles, and is the wording DR-26 log:663 requires being followed?
- XU2-29. If instruments crossed with the logs, does the record's continued usefulness rest partly on instrument continuity as well as on the stationarity of the subject?
- XU2-30. Does No_National_Stereotypes.md:23's first source (skilled exiles' own pre-exile institutional backgrounds) bear on the spec's word "independently" at Davis, or does Davis.md:151 close it?
NEEDS FROM THE DEVELOPER:
- XU2-31. Did Davis's inheritance include equipment, research data and results, or ongoing datasets beyond the journals, logs and orientation manuals the spec names? *Recommended answer:* state only what is already canon: the infrastructure (Davis.md:151) and the documentary record, with the techniques written into it per No_National_Stereotypes.md:21. Record equipment and datasets as admissible and unstated, an open slot, unless the developer wants to state them. Do not invent them in the re-derivation.
- XU2-32. Is DR-25's "Records can draw people" row (log:648) a general mechanism any city's records can carry, or a ruling about the one location it names? *Recommended answer:* treat it as specific to that location, and do not apply it at Davis without a Davis-specific ruling. This keeps the one-location law intact and avoids carrying another location's answer across.

---

## Item U-3 — NARROWS (medium)

*Reader output: `.t8_check_U3_reader.md`, 115 lines. The decision block, unchanged:*

VERDICT: NARROWS
CONFIDENCE: medium
AFFECTED PASS SENTENCES: `04_Phase_10_Catalog.md:499` (heading "zero, verified": false as written on the current project records, and it claims more verification than was done) · `:502` ("No figures, placeholder or otherwise, beyond §E's roles.": ungrounded, because it rested on a sweep that never opened the project's character folder, where a placeholder-named figure is sited in Davis) · `:329-330` ("§F.3's zero is not a gap in this pass's research, it is a consequence of the spine": false as written, since part of the zero was a gap in the sweep's scope) · `:327` ("records Davis's notable figures as ⛔ zero, verified — empirically": carries over the same overclaim). Scope only, not false: `:501` ("Character canon returns nothing for Davis" is true for canon as scoped at `:30`, but the sentence does not state its scope where it grounds `:499`). Not affected: `:502-503` (the hedge), `:563`, `:9-10` (the sweep did run).
WHAT A RE-DERIVATION MUST ASK: (1) Does the city template's §31 "notable figures" include developer-sourced character drafts sited in the city, or only canon figures? (2) Which character sources does Davis's sweep cover? Does it include the project's own character folders as well as the universe repo's character canon and the Enneagram index, and does the receipt name every folder opened? (3) Do the universe repo's character canon and the current Enneagram index still return nothing for Davis, with every "Davis" hit checked in context (`:599`)? (4) Are any other drafts in the project's character folders sited in Davis? (5) Does the README's "present day" fall inside the pass's frame, the Second Interwar 2564-2812 (`:3`)? (6) If the draft is recorded, how is it named without a proper name? By folder ID? (7) Does Disanalogy B have to be restated to cover commemorated figures only, given that §F.3's empty cell was partly a sweep gap? (8) Does §E need any change, or does the draft's sourced role sit inside an existing role without forcing a fit? (9) Does §L need a handoff row from Davis's finished pass to character work, and is the direction recorded as city to character only?
NEEDS FROM THE DEVELOPER: (XU3-N1) Does a character draft sited in Davis count as a §31 notable figure in Davis's Phase 10? *Recommended:* not as a canon entry, but as a recorded documentation note. §F.3 would then read "zero in canon (two sources run); one developer-sourced draft is sited here (STP-06; label not official; not canon)", so the catalog neither adopts the draft nor hides it. (XU3-N2) Should Davis's re-derived sweep name and include the project's own character folders? *Recommended:* yes, with every folder listed in the receipt and every hit checked in context. (XU3-N3) Which way does the dependency run between Davis's pass and the STP-06 draft? *Recommended:* from the city to the character only. Davis's finished catalog is an input to her Enneagram-adjusted fields under the Enneagram-first law, nothing in the README flows back into Davis's culture, composition or relation, and §L records that row.

---

## Item U-4 — NARROWS (medium)

*Reader output: `.t8_check_U4_reader.md`, 142 lines. The decision block, unchanged:*

VERDICT: NARROWS
CONFIDENCE: medium
AFFECTED PASS SENTENCES: In the cited locations: 00.1:L244 (lists L21 as a PARTIAL strike, but the clause is no longer at L21) · 00.1:L267 (the L21 strike row: its clause is gone, and "tier + figures at L27, L37" now lands on a blank line and on Indonesia's row, while Australia is at SPEC:L21 and L38) · 00.1:L223 and L238 (the read spec and "= 137 lines" are in pass-time numbering; the region they admit is now 24 lines longer; unverifiable past L81) · 00.1:L225 ("**137 lines.**" is stale, and "contains ZERO struck lines" is unverified on the current file) · 00.1:L226 and L228 (the LRANGE value and "(137)" as the PROOF LINES value are stale) · 00.1:L241-243 (the bound and additions are in pass-time numbering; "L176 (premise only)" collides with L286) · 00.1:L286 (in current numbering beside a pass-time spec; at least one of L243 and L286 is false about L176, and I cannot tell which without reading past L81) · 00.1:L248 (census lines "496,613"; per orchestrator result 3 the rows are now at L506 and L650; not checked by me) · 00.1a:L232 ("181 lines with 135 admissible"; the file is 260 lines by wc -l) · numbering only, outside the region: 00.1:L277-279 ("L143", which 00.1:L303 and L341 call L167), 00.1a:L152 ("L1–134 ∪ {L143}"), and 00.1a:L73 against L75 and L83 (L143 and L167 used for the same line). Outside the cited locations, given for routing only and not judged here: 00.1:L64-65 and L70-71 (pass-time census values and census lines L496/L613), L129 (G8 at "L30–52"), L164 ("100.00%"), L168-171 (retention figures), and L179-182 (use limit grounded on L54 and L28, contradicted by SPEC:L78, SPEC:L28 and DR-104(1)).
WHAT A RE-DERIVATION MUST ASK: (XU4-29) Read line by line, does each line of current SPEC:L13-81 pass 05 §6.1 first and the §6.3 ratification check second? That includes the 24 or more rows and the new notes that the original classification never saw. (XU4-30) Is the L21 PARTIAL strike retired for lack of a target, and does anything at current L21 or L38 need a strike, given DR-88's meaning of the "(founding wave)" tag? (XU4-31) Are SPEC:L28 and SPEC:L78 provenance and scope notes, admitted and binding as limits under 05's Scoped property, rather than G8 content? And are L28's process numbers (pool percentages, multipliers, seeds) marked as not usable as shares? (XU4-32) Is L28's clause "the share every city in its time-zone window receives" read but not used, as an implicit normal like the pass's L117 strike, or is it a legal statement of method? (XU4-33) Are L28's two pointers, to the scratch folder and to git commit `593510ab`, DO-NOT-FOLLOW, as L91 was? (XU4-34) Are the revision parentheticals at SPEC:L15-16 read-but-not-used process notes? These hold superseded values, the DR-68 note and the DR-90 note, which names another location. And is the relocation they record an in-world flow into Davis, which would be relation and possibly G4 or G8 material, or an authoring redistribution? Answering this needs DR-68 and DR-90, which are not in this list. (XU4-35) What is the read spec on the current file, computed and verified mechanically under M-224, and what are its count and LRANGE? Does the +24 shift hold past the table, given that the file is 260 lines and not 205? Which of 00.1:L243 and L286 is right about L176? (XU4-36) Where are the census rows now, and what do lines 392-398 now hold? (XU4-37) Under DR-104(1) and (2), what is the region's use spec (reason by headcount, no cutoff, no finding on a gap within a tier, randomization in two rows only), and does any of §3.3's limit survive? (XU4-38) Does the region meet 05's Stable property while DR-85's question on the four pieces and Taiwan stays open for rows Davis carries?
NEEDS FROM THE DEVELOPER: (XU4-39) The contract's VALID banner says "Nothing below rests on a single reader's claim" (00.1:L11). Must the re-derived classification of the composition region be run under the same three-reader protocol, or may it be single-reader with the banner amended to say so? **Recommended:** three readers for this region only. It is 69 lines, so the cost is small, and the banner stays true. If you choose single-reader, mark the re-derived part as single-reader in the amendment note. (XU4-40) Is Davis's composition block now settled, or may the Mongolia, Tibet, East Turkestan and Taiwan rows still change under DR-85's open question (LOG:L1529)? **Recommended:** take the current block as the input, mark those four rows as open, and rely on DR-104(1)'s bar on findings that rest on a gap within a tier, so that no finding depends on their exact shares.

---

## Item U-5 — NARROWS (high)

*Reader output: `.t8_check_U5_reader.md`, 190 lines. The decision block, unchanged:*

VERDICT: NARROWS
CONFIDENCE: high
AFFECTED PASS SENTENCES:
- `05_Reconciliation.md:64`: attributes "polar night and midnight sun each running roughly 66-67 days" to §3 and §4. The current §3 (LC:53) reads ~37 and ~54 days. §4 (LC:61) still gives the old span, but by dates and "roughly two months", not in these words.
- `05_Reconciliation.md:69`: "`Local_Cultures` §3 and §4 need correction". §3's polar night is corrected. §4 remains, and §3's midnight sun differs by one day, which looks like a counting convention.
- `05_Reconciliation.md:185` (`H61`): "§3/§4 carry a 66–67 day polar night against `Specs`' 37". False for §3, true for §4. H61 is now half closed.
- `05_Reconciliation.md:131` and `05_Reconciliation.md:146`: "No character sited … verified zero" and "Phase 10 §F.3's zero STANDS as written" meet LOG:1704's character draft sited in Davis. They must be qualified as the canon zero against an unratified draft.
- `05_Reconciliation.md:164-165`: "The Australian founding itself stands on geography (`DR-29`, `Founding_Register.md`)". The Register's row is grounded on geography and access under `DR-19` (orchestrator line 5). I cannot tell what `DR-29` says (it is not in my list), so this is provisional.
- An omission, not a sentence: Step 5's record has no entry for the check files' composition conflict with tier 1 (XU5-25).
- Pre-existing problems, not caused by any change in the row. They are listed so they are not lost; they do not drive the verdict.
  - 05:15: the "Provisional … not asserted canon" self-declaration is attributed to both files, but only the robot file carries it (RC:3-4).
  - 05:54: "rests on admissible canon" contradicts 05:15, and section 1 is not tagged as self-originated under 05:116-121.
  - 05:205: "Seven convergences survive on canon sources", but two of the seven are tagged corroboration (05:125, 05:127), and the tier 3 sources are not canon by 05:15.
WHAT A RE-DERIVATION MUST ASK:
1. What do the check file's §3 and §4 now each say about polar night and midnight sun, and what does the spec's current climate line say, with its counting convention? Is `H61` closed for §3 and open for §4?
2. Does any Step 5 finding rest on any composition-derived sentence in either check file (LC:9, 24-37, 77, 104, 107, 119, 173, 186, 193's stated ground, 199; RC:25, 79)? If so, does it survive re-keying to the 45-row table by headcount, with no ground in a within-tier gap?
3. How does Step 5 record the composition conflict? Should it be a reconciliation row like 2.1, with Specs governing, the correction placed in the check file outside the pass, and a hole opened? Does the record cite DR-85's "not edited" status?
4. Does the language rule that enters through the note (DR-104 item 3) bear on LC:104's "Mandarin (Primary tier)"? Does any Step 5 finding use §8 beyond the §8c idiom?
5. Does an unratified character draft sited in Davis falsify "No character sited" or Phase 10 §F.3's zero? Was the draft made before or after the pass, and does its README's earlier composition matter?
6. Which ruling grounds the Australian founding on geography and access: `DR-19`, `DR-29`, or both? Should 05:165 say "geography and access"?
7. Have LC:45 and LC:47 been corrected? (Not as of 2026-11-09.) Should `H62`'s entry say the correction is still pending?
8. Does the robot file's Census II human majority still hold on current figures? (Yes at Census II; at Census I robots are the majority.) Does the gap between human and robot retention bear on the Gen/Mark null? (Question only.)
9. Is section 1's re-sourcing onto a tier 3 check file compatible with reading check files only as a check (`05` §6.1; Step 0.4 item 6)? Must section 1 be tagged as self-originated corroboration, and does the multi-calendar property have an independent ground in tier 1 text or in real-world research? The research question would be whether the Vestfold Hills' lakes freeze, thaw and open on different schedules.
10. Does the open oasis-or-katabatic-margin question (DR-104 item 4) reach section 1 or the lakes convergence (05:128), given that the check file states oasis as fact (LC:43, LC:160)?
NEEDS FROM THE DEVELOPER:
- XU5-35. Does an unratified character draft sited in Davis count as "a character sited" for Phase 10's zero? **Recommended (PROPOSED):** no. Record the zero as "no canon character sited; one unratified draft exists (DR-104, not answered), whose README cites the pre-rework composition", so the sentence is true either way.
- XU5-36. Should the re-derived Step 5 carry the check files' composition conflict as its own reconciliation row, with Specs governing, the correction placed in the check file outside the pass, and a new hole number assigned at re-derivation? **Recommended (PROPOSED):** yes, on the model of 2.1 and `H61`. State that no Step 5 finding rests on the stale text, and that composition-derived content in the check files is population-origin material: demoted, never excluded, and re-keyed to all 45 rows by headcount (DR-104 item 2).
- XU5-37. Should section 1's amendment be kept but re-tagged as self-originated corroboration (tier 3), with an independent ground sought? **Recommended (PROPOSED):** yes. Keep the finding, correct 05:54's "canon" to "tier 3, admissible, corroboration", and open the research question named in re-derivation question 9. This is a pre-existing issue, so the developer may prefer to leave it out of the U-5 re-derivation.

---
