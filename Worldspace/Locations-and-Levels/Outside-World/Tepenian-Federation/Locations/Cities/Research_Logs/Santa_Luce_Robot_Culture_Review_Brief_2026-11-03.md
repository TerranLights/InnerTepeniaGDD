# Santa Luce's robot-culture sheet: review brief for the developer (2026-11-03)

**What this is.** A plain-language read of `Local_Robot_Culture/Halley_Subnet/Santa_Luce.md` (228 lines, a draft written 2026-11-02, the last of the 36 robot-culture sheets), so you can review it without reading it end to end. **The sheet was not edited.** No web research was done; every check below is against files in the repo. Labels: CHECKED (matched its source), MISMATCH (does not match), DERIVED (my arithmetic).

**Bottom line.**
- The numbers I checked are right, with one exception: the temperature extremes come from a different weather station than the monthly means beside them (section 2).
- The three questions the tracker lists as open were answered by you on 2026-11-02 (`DR-89`) and are already in the sheet. Section 4 says what is still genuinely open.
- The sheet is honest that it is thin on everyday surface culture (food, music, holidays). That is because no culture pass exists yet for the new founding, not because it skipped them.

---

## 1 · What the sheet says, section by section

**Preface and sources.** Santa Luce was held back from the whole run because its old culture files were written around a Finnish-Swedish founding that was replaced. The sheet takes founders only from the Founding Register: Italy's two successor states and the Confederacy of Intermarium Nations (CIN), jointly, with oversight, coordination, management and logistics given to Magna Lombardia. It lists 30 passages from the old files that it refused to use and why (they depend on the superseded founding, on station operators counted as founders, or on stale numbers). Where the new founding left a gap, it says the slot is open instead of filling it. The city is Damaged but partly operational, so the aspect sections describe the living pre-war robot culture in the present tense.

**The one-liner.** A Santa Luce robot belongs to a city of fifty origin groups with no majority, whose coordinating role belongs to a group that is about one resident in sixteen, on a rock that holds still while the ice around it moves. She cannot borrow standing from headcount or heritage, so what she carries is her tenure at one piece of work, through months when the dark and the cold shrink her battery together and the sun returns before the battery does.

**Symbol proposal.** Saturn and Earth (section 3 below).

**Part I, local aspects (ten sections):**
1. **Kinship and mentorship.** The bond between robots is the "threshold watch": in the cold months, how close another robot is to the charge level where she cannot warm herself back up is the most important thing to know about her. Mentorship is the only way into the research sector, because a robot cannot be built to order for a profession. Origin-based clans do not apply here.
2. **Cooperation.** Authority runs by role, not headcount (the coordinating group is 6.25% of the city). Asking another robot's charge level is courtesy, not prying. The Tepenia-wide baseline stands: egalitarian, tilted toward robots.
3. **Locality as identity.** With fifty groups and none above 7.89%, city identity is uncontested. Distinctive trait: "threshold literacy", planning a trip by the number of warm stops it takes.
4. **Generation marks.** Nothing local; Santa Luce is not a Cradle site. It does have fabrication chambers, as every city except Dome Fuji does.
5. **Religion.** None of the six canon robot religions is sited here; the slot is left open (not "impossible").
6. **Consumption.** A glitch-coolant custom (one person stays unglitched until the rest are indoors and warm), and a walking-smoke habit. The glitch-coolant pole is left open. Siligel and robot coffee: nothing asserted.
7. **Sexuality.** Telling her your charge level is the first trust gesture; courtship leans on personal gestures because no community is large enough to supply a default ritual. The sheet itself calls both generic.
8. **Language.** Hawaiian is the civic default; the second-language slot is open because there is no majority. One speech habit: distance spoken in energy cost ("two warm stops"), not kilometers.
9. **Arcanet etiquette.** Nothing derived. One lead: the Hwy 59 "Arcanet Line" ramp.
10. **Surface culture.** The layered glove system (thin inner glove for fine work) and the warmed commons as the robot's "third place". Holidays, music, arts and cuisine are open.

**Part II, five combined findings.**
- *Conventions win by being no one's:* with no majority, the shared ground is the cold and the charge threshold. (Explains why the whole sheet leans on cold physiology.)
- *The sun returns before the battery does:* polar night ends about Aug 2 but the coldest month is August and October is still colder than any month of the light half, so for a robot the seasons are "small" and "smaller", not "warm" and "cold".
- *A role without a node, held by a group without a majority:* coordination and logistics, but no port, no airfield, and a mid-corridor position on Hwy 7. Competence replaces heritage as the route in, and long robot lifespans mean the same individuals can hold a founding-era role for the whole period.
- *The long-baseline observer:* a fixed rock to measure against plus lifespans longer than any program means a robot can keep one observation line for two or three centuries.
- *"Community-scaled" is true for robots sooner than for humans* (your lifespan bridge, accepted 2026-11-02).
- *The present-day layer:* what survived the war is TBD; the threshold watch and the keeper are the customs most likely to persist.

**Part III.** Candidates raised but not resolved: a dark-season and sun-return observance, a warmed commons, a Cymatics link (the physics is unsourced), mortuary practice on bedrock, the Hwy 59 ramp, and the Italian–CIN dynamic (your ruling: partly mixed spaces, generally separate neighborhoods; the sheet derives nothing further).

**Swap test (closing check).** The sheet's own verdict is "partial". Three findings pass cleanly (the role without a node; conventions by being no one's; the sun-before-battery gap). Three are kept with a stated weakness. Nine are generic to any cold interior city. It says this plainly.

---

## 2 · Spot-checks against sources (17 checks)

| # | Claim in the sheet | Source | Result |
|---|---|---|---|
| 1 | Twelve monthly mean temperatures, Jan −5.2 to Aug −21.9 to Dec −5.5 °C | `Climate Data/READER/Aboa.md` (Kärkäs 2004, Table 2) | CHECKED, all twelve match |
| 2 | Annual mean about −15 °C | same | CHECKED: the twelve values sum to −180.1, mean −15.0 |
| 3 | Five months (May to Sept) between −19.0 and −21.9 | same | CHECKED |
| 4 | Polar night about May 12 to Aug 2 (83 days); midnight sun about Nov 8 to Feb 5 (90 days) | the city's spec | CHECKED against the spec. My own rough geometric check at the station's latitude gives about 89 days for each (May 8 to Aug 4; Nov 7 to Feb 3); the spec's 83 and 90 are within what air refraction accounts for. I did not independently verify the exact dates. |
| 5 | Census I: 228,766 humans, 237,052 robots, 465,818 combined; Census II: 140,994 / 137,861 / 278,855 | spec, after `DR-90` | CHECKED |
| 6 | Robots 50.89% of Census I and 49.44% of Census II (humans 50.56%) | DERIVED from row 5 | CHECKED |
| 7 | Fifty origin groups: 4 Primary, 31 Significant, 15 Notable; largest 7.89% | spec composition table | CHECKED (counted the rows) |
| 8 | Brazil 7.89%, UK 7.44%, Magna Lombardia 6.25%, CSA 5.40% | spec table | CHECKED |
| 9 | Magna Lombardia 14,835 robots | spec table | CHECKED (6.26% of 237,052; the table's rounding) |
| 10 | Magna Lombardia plus Meridia is 8.34% | DERIVED from the table | CHECKED (6.25 + 2.09) |
| 11 | The 13 rows that match the CIN accession list sum to 27.79% | DERIVED from the table | CHECKED (Latvia through Poland) |
| 12 | Hwy 7 order; Hwy 59 ramp between Halley and Santa Luce; Neumayer connector between Santa Luce and Sanay | `Highways.md` | CHECKED |
| 13 | Santa Luce "served, not host" (air via Troll or Belgrano); landlocked | `Airports.md`, `Ports.md` | CHECKED |
| 14 | Saturn is held by Mirny, Scott and Zhongshan (Metal); Santa Luce is excluded from the symbol file | `City_Symbol_Assignments.md` | CHECKED (Saturn used 3 times) |
| 15 | Sector split: Technical 25%, Marine 15%, Commercial 15% | old `Local_Cultures` file, section 15 | CHECKED for those three (I did not re-read the other three sectors) |
| 16 | Juneau Icefield Research Program: mass-balance data since 1946, longest-running icefield program in North America; students assessed before glacier work | Santa Luce research log C01 R1 | CHECKED |
| 17 | Gibraltar: 79% call themselves Gibraltarian (2012 census) | same log | CHECKED |

**MISMATCH found (the sheet's description of its own climate source).** The sheet's climate paragraph gives "record low −45.4 °C (June); record highs above freezing only in Nov to Mar (+0.3 to +4.1)" right after the Aboa monthly means, as if all of it were Aboa. It is not:
- The −45.4 °C low and +4.1 °C high come from the spec's record-extremes line, which cites a different weather station (an automated station about 10 km away and 117 m lower, 1998–2014).
- Aboa's own recorded extremes (Kärkäs 2004) are a low of −42.0 °C (12 May 1995) and a high of +9.7 °C (4 Jan 1991). Aboa recorded above-freezing maxima in October (+0.5), November (+3.2), December (+9.1), January (+9.7) and February (+5.9), and March topped out at −0.3, so "Nov to Mar" does not match Aboa either.
- This does not change any finding: the sheet's arguments rest on the monthly means, which are Aboa's own and are all below freezing. It is a labeling problem: two stations are blended without saying so.
- Related: the spec's own older "Mean" column (annual about −23 °C, coldest month −36 °C) differs from the measured Aboa record by up to 16.6 °C. The sheet correctly uses the measured record and declines the older column.

**Proposed fix (not applied):** relabel the extremes as "from the nearby automated station" and add Aboa's own recorded extremes beside them.

---

## 3 · The symbol proposals (Category E)

Both are proposals; the real determination is in Phase 10 of the ULM pass, which has not run for this city.

- **Solar Symbol: Saturn** (core idea "Mystery": rings made of fragments, beauty built from pieces, not needing to be whole).
  - Reasoning: fifty origin groups, none dominant, so the city is assembled from fragments without a central mass; it has never been a node (no port, no airfield); it is not a Concordia connection point. The sheet also notes the negative reading, held together by something other than shared mass.
  - Rejected: Neptune (already the most-used planet symbol and flagged for over-use), the Asteroid Belt (closest alternative, but created for Rothera's literal decentralization, and Santa Luce has a centralized coordination mandate), and Jupiter, Mercury and Uranus (held by neighbors Sanay and Lazar, Halley and Utstein).
  - Note: Saturn would be Santa Luce's, Mirny's, Scott's and Zhongshan's. The shared symbol file records Saturn as used three times today.
- **Robo-Element: Earth** (core idea "Contact": strength is in the touching between parts, not in any one part).
  - Reasoning: with no majority group, the city's strength is relational, passed from group to group. The element's negative reading (looks permanent, held by a condition nobody checked) fits an aggregate social ground.
  - **The sheet's own honest limit:** the Earth entry is about soil that can lose strength, and Santa Luce's physical ground is bedrock, the opposite. The pick rests on the social reading only.
  - Note for you: the shared file shows Earth already used by six cities (tied with Water as the most-used element). The sheet does not mention this; it is the kind of cross-city fact the terminal differentiation check handles.

---

## 4 · The open questions, as concrete choices

The tracker's list of ten open questions is out of date; most were answered in `DR-89` (2026-11-02) and are already in the sheet. Where each stands:

| Question | Status | Where |
|---|---|---|
| Working language | **Settled:** Hawaiian is the civic default; the second slot is whoever holds the majority; Santa Luce has none, so the slot stays open | `DR-89`; sheet section 8 |
| Which CIN states supplied the CIN share | **Settled:** all member states, each in proportion to its population (so the 13 rows totaling 27.79% are the CIN stock) | `DR-89` |
| Which census governs robot-vs-human majority | **Settled:** Census II (humans lead 50.56% to 49.44%) | `DR-89`; sheet section 2 |
| The old file's 102 and 104 day polar night and midnight sun vs the spec's 83 and 90 | **Settled:** the spec governs; the old file's numbers are excluded | sheet exclusion list |
| "Small and community-scaled" at 465,818 people | **Settled:** your lifespan bridge | `DR-89` |
| Italian–CIN coexistence | **Settled:** partly mixed spaces, generally separate neighborhoods; the sheet derives nothing further | `DR-89`; Part III |
| Fabrication chamber | **Settled:** every city except Dome Fuji | `DR-89` |

**Still genuinely open (your call, each with my recommendation):**
1. **A supporting-tier language for Santa Luce?** Today you ruled English and Spanish as Contrapunto's supporting tier beside Hawaiian. Santa Luce has no majority. If you want a tier here: summing the English-speaking rows gives about 23.8% (UK 7.44, CSA 5.40, Appalachia 3.46, New England 2.83, Cascadia 2.52, Midwest Republic 1.08, Colorado 0.81, Northern Ireland 0.21, Alaska 0.033; DERIVED, rows chosen by me), Portuguese about 8.8% (Brazil and Amazonia), Italian 8.3% (Magna Lombardia plus Meridia). *Recommendation:* leave the slot open until the culture pass, since that pass should decide from the actual communities.
2. **Troll's sheet repeats the old "Competence Without Commentary" faction line for Santa Luce.** You deferred this to the evening work and the factions work. *Recommendation:* keep it deferred; it needs the factions pass.
3. **The four old inspiration picks** were restored to Primary but their written reasons are the superseded ones. *Recommendation:* re-reason them (or replace them) in the Santa Luce culture pass, using the two research logs already done.
4. **Row 76, the Tromsø-style dark-season festival** you added on 2026-10-27, is still "developer to confirm". The sheet's sun-before-battery finding would support a two-part observance. *Recommendation:* confirm it as a candidate and leave naming for the culture pass.
5. **Open slots:** holidays, demonym, glitch-coolant pole, war damage, music, arts, cuisine, religion. *Recommendation:* all stay open; none can be derived without the culture pass for Magna Lombardia, Meridia and the CIN states.
6. **The symbol pair** (Saturn and Earth). *Recommendation:* accept as proposals only; Phase 10 decides.

---

## 5 · What is stale after today's changes

- **The sheet itself is current.** It already carries the post-`DR-85` shares and the `DR-90` populations. The ruling rows from today (`DR-96`, `DR-97`) do not touch it. The sheet cites the Division of Industry file's Half B and section 4 "for the citable workforce figures only", but quotes none of them, so today's recount (including Santa Luce's own recount, with its "held at current value" heading kept) leaves nothing to update here.
- **The tracker's entry on this sheet (S.0k) is stale, not the sheet.** It still says robots lead Census I at 51.14%, quotes 437,614 people and lists ten open questions that `DR-89` mostly answered. I would correct that entry. I haven't.
- **Troll's sheet** still repeats the old faction line (above).
- **Two things the sheet cannot yet use:** the research on Magna Lombardia, Meridia and the CIN states (none exists), and a rewritten culture file for the new founding (the old one is mostly excluded).

---

## 6 · Things that look wrong or generic

- **The climate-extremes blend** (section 2): a real labeling error.
- **Generic findings.** The sheet's own swap test admits nine findings would transplant to any cold interior city: the threshold watch, charge-state courtesy, threshold literacy, the keeper, the walking smoke, telling her your charge, distance spoken in cost, the glove trade-off and the warmed commons. They are all true to canon and to the city's cold, but none is specific to this place. The two sexuality findings are described by the sheet itself as weak on locality.
- **Inferred, not sourced.** The walking smoke, the speech habit and the glove trade-off are inferences from canon with no direct source; the sheet says so.
- **Deep-heavy, surface-light.** Almost no everyday texture (food, music, holidays) because the inputs for it do not exist yet. That is correct behavior for a draft, but it is not yet a place somebody could live in; it is a frame that the culture pass has to fill.
- **Earth's soil-versus-bedrock limit** (section 3) is stated by the sheet itself and deserves your decision rather than a quiet acceptance.
- **Finland and Sweden are present** in the composition table (Sweden 1.61%, Finland 1.35%, both Significant). That is fine: they are population, not founders. The sheet keeps them out of the founding story and the Register excludes them as founders.
