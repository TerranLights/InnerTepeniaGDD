# Finished ULM passes: has the data they absorbed changed? (summary, 2026-11-03, evening)

**Question (developer, 2026-11-03):** among the cities already run through the ULM, has any data they absorbed changed so that the results might come out differently, so that the results may need review?

**Answer: yes, for every one of them.** Nothing was re-derived and nothing was edited (no pass file, spec, census or source). Five independent reviewers each read one city's pass against git history at three points in time (when the pass finished, the evening of 2026-10-30 when the earlier input audit wrote its amendment notes, and now). Full reports, one per city, are beside this file: `Drift_Review_Davis_`, `_Mirny_`, `_Shirayuki_`, `_Sinheung_`, `_Zhongshan_2026-11-03.md`. This file adds the Concordia districts, which the reviewers did not cover, and what the reports have in common. Each city was reviewed on its own terms; no city is compared with another here.

## Which passes exist
Six pass folders hold ULM output: Davis (complete), Mirny (run through Step 10, now under amendment), Shirayuki, Sinheung, Zhongshan (Opus, complete) and Zhongshan (Sonnet, a two-phase trial that mostly copies five Opus files). Concordia's 13 districts used the separate district method (section 4 below). No other city has a run.

## 1 · What changed since the passes (causes that touched every finished pass)
1. **The population rework of 2026-11-02** rebuilt every city's composition table: China's row became the Sinian Federation; Russia, Korea and the UK were split or renamed into successor states; dozens of small rows were added; tiers (Primary, Significant, Notable) were relabeled by a new rule; the "founding wave" tag was narrowed to mean the Founding Register's founder.
2. **City populations moved twice more** (the October 28 scenario, then the Esperanza relocation of 2026-11-02), so every census total, retention figure and ratio the passes quote has changed.
3. **The Division of Industry file `16` was recounted on 2026-11-03** with a robot-keyed requirement, so every city's baseline / mandated / free shares moved by a point or two.
4. **The language rule** (Hawaiian dominant everywhere; supporting languages = groups within 12 points of the largest) did not exist when any pass was run.
5. **Rulings and sources rewritten:** the Founding Register and the "founders come only from the Register" law; the station-heritage closure (inherited research, equipment and techniques may cross the founding gap); comparison sentences removed from specs; the spec tables grew, so cited line numbers moved; Robot Universals moved to another repo (text intact).

## 2 · Results by city (counts are the reviewers' own)
| City | Items | N number only | W wording false as written | C conclusion may differ | U cannot tell |
|---|--:|--:|--:|--:|--:|
| Davis | 30 | 11 | 7 | 7 | 5 |
| Mirny | 31 groups | 11 | 8 | 10 | 2 |
| Shirayuki | 26 groups | 8 | 11 | 3 | 4 |
| Sinheung | 32 | 13 | 10 | 5 | 4 |
| Zhongshan (Opus and Sonnet) | 26 | 8 | 6 | 7 | 5 |

**What would most plausibly come out differently (C items), in each city's own terms:**
- **Davis:** Phase 2's arguments that rested on the old 21-origin table (the scale check that said no origin lacks numbers, which is false for the smallest of the 45 rows now; the "origins are where robots were" argument; the seal on comparing nations' figures), Phase 5's "heritage relations structurally excluded", and Phase 8E / Phase 9 language lines. Recommended: re-derive Phase 2 (and Steps −1/1 for the composition part), then Phase 5, Phase 8E and Phase 9 language.
- **Mirny:** Phase 5's founder and null findings (the Idelsk-Uralia exile-group ruling is applied only in Phase 2 so far), Phase 9, the Phase 7 language and tier-arithmetic items, the held Phase 2 and Phase 8 pieces (a one-line language update), Step 5, Step 6, Phase 10. **Two gaps the amendment layer does not know about:** the robot-keyed recount (Phase 7 says robot upkeep is "not in" the formula; it now is; the "free tier is an upper bound" finding turns into a determined number) and the Idelsk-Uralia ruling outside Phase 2. Neither is on the handoff's list of remaining Mirny pieces.
- **Shirayuki:** only three: the "flat Significant tier, no runner-up" shape (gone), the band-crossing argument (Census I is now 11.3% over the one-million line, was 6%), and the Phase 8F language reasoning ("Japan Primary, so the vernacular follows" conflicts with the language rule). The reviewer's view: the pass survives mostly intact because its own rule says no finding rests on a percentage.
- **Sinheung:** Phase 9 B.1/B.2 with the Spine's retention block (the retention gap shrank from +2.46 to +1.47 points), then Phase 2 (A.2, A.4, E.3, F), Phase 8 A.3, Phase 9 C.3. Phase 8's language item waits for how the language rule enters a city pass. Needs a decision first: Band 4 versus Band 5 (Census I now exceeds the edge of Band 4).
- **Zhongshan:** Phase 8 section 8.1 (the composition merge relies on "five Significant entries" and a "twelve-entry tail"), 8.8 (language), the closing axis "The commons had no homeland", QA Gate 4 and the Step 6 cell with it; plus a short re-read of the claim that the inversion lies "in the retention rates themselves".

## 3 · Things found that are not drift (existing defects and loose ends)
- **Every 10-30 amendment note is stale again** (population, retention, workforce, shares, line numbers). One dated amendment note per city, written after the population work settles, would cover all the N and W items. The reviewers recommend waiting, since totals have moved twice in a week.
- **Spec defect, Shirayuki** *(I checked this one)*: spec L35 and L321 say Japan 34.71% (and "was 36.27%"), while the spec's own table (L62) says 34.20%.
- **Davis:** the amendment note's air-access item is mis-framed (`Airports.md` already said Davis had no airport at pass time, so the Phase 5 claim was a pass misreading, not drift). The `16` prose still says agriculture 181,808 where the recomputed table says 186,131.
- **Station-heritage question (`DRQ-14`)**: closed 2026-10-01 per the Shirayuki reviewer, but the Shirayuki pass still calls it open in nine files. I confirmed a closure is recorded in `ULM_Run_Progress.md`; I have not read it.
- **Sinheung and Zhongshan notes:** errors in the amendment notes themselves (e.g., Zhongshan Sonnet's note says it has no industry figures, but its Spine carries them).
- **Mirny:** the 2026-11-03 note's "22 of 100" founders figure and "second slot open" are stale; the language rule exists only in the handoff, not in the rulings log.

## 4 · Concordia's 13 districts (checked by me, not by the reviewers; approximate)
- **Concordia's own composition changed the same way** (its Primary tier was China, Japan, South Korea, Russia, Indonesia and Australia; it is now Korea, Japan, Australia and Indonesia, with the Sinian Federation, Russia (core state) and others Significant), and its Census I rose from 1,015,947 (pass) through 1,039,863 to 1,068,065.
- **The district diaspora weights depend on every city's population.** `District_Refugee_Diaspora_Composition.md` weights each city's Census I by its top-3 district picks (3 / 2 / 1). Every city's Census I has changed. My recompute does **not** reproduce the file's stated percentages exactly (the file says Esperanza 24.6% of Cancer; my reconstruction gives about 27% at the file's date), so treat my numbers as approximate. **The direction is firm:** after the Esperanza relocation (1,200,000), Esperanza falls from the largest diaspora source of the Cancer district to about third (Mawson, Zukelli, then Esperanza), and the sources of other districts shift by a point or two. The Cancer district's description (Esperanza as the dominant outer-city source, its Caregiver-Teacher Halls) is the clearest place to re-check.
- Not done: whether the district `Full_Extrapolation` files themselves rest on Concordia's composition or only on these weights. A district-by-district review would be a separate job, using the district runbook.

## 5 · Decisions that wait for you (plain language)
1. **Davis, which split governs:** the 2026-09-16 ruling (mandate 28.2%, free 31.1%), or the recounted figures (27.6% / 30.5%) that the new robot-keyed recount produced from the same ruling?
2. **Davis, the seal on comparing nations' figures:** it was grounded on the old randomization of equal shares, which no longer exists. Does the seal stay?
3. **Davis, tiny origin rows:** do 21 rows under 1% (the smallest, Tuva, about 150 people) count as origin communities?
4. **Sinheung, Band 4 or Band 5:** Census I now exceeds the edge of Band 4 while Census II sits inside it.
5. **Sinheung, station-heritage rulings:** do they change what the pass treated as inadmissible?
6. **Language rule in a finished pass:** how does it enter a pass that never mentioned Hawaiian (Sinheung, Shirayuki, Zhongshan, Davis)? A dated amendment note, or re-derivation of the language sections?
7. **Whether to re-derive or only annotate:** the reviewers' lines are in each report's section 6. Short version: Davis Phase 2 and Mirny Phases 5, 7, 9 are the most likely to need real re-derivation; Shirayuki needs three small items; Sinheung and Zhongshan need targeted pieces; everything else is a dated note.

## 6 · Limits
The reviewers did not read every pass file line by line (Mirny's pass is about 25,000 lines; several 100 KB-plus logs were searched, not read). Their C and U classes are judgments about dependence, not tests. The Timeline repo's own history, the Zhongshan datasheets and methodology-file changes since the passes were not assessed. The district part above is my own approximate recompute.
