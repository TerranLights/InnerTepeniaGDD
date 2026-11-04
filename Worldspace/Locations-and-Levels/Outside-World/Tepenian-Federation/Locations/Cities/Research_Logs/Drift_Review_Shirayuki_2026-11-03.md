# Shirayuki: input drift review, 2026-11-03

**What this is.** A read-only check of one finished pass (Shirayuki, run 2026-09-06 to 2026-09-13, last edited 2026-10-01) for input drift: has any data the pass absorbed changed so that its results might come out differently if re-derived? Nothing was re-derived. No pass file, spec, census or source was edited. This file is the only thing written.

**Three points in time used throughout.**
- **Pass** = commit `5c339aee` (completion, 2026-09-06). The pass files themselves did not change after `4a59fab8` (2026-10-01) apart from the added amendment note and README link fixes, so "pass" also describes what the pass files say now.
- **10-30** = commit `c3e31166` (the manual input audit baseline, evening of 2026-10-30).
- **Now** = HEAD `54dda306` (2026-11-03).

**Ruling labels, described once.** `DR-19` founders come only from the Founding Register. `DR-44` the Register's remaining rows ruled (Shirayuki: Japan by the court's allocation, plus geography). `DR-68` 2026-10-28 population scenario (Santa Luce's excess spread over other cities). `DR-85` 2026-11-02 population rework (every country in its latest-period form, China becomes the Sinian Federation and is reduced, tiers relabeled). `DR-88` 2026-11-02 comparison sentences in specs neutralized. `DR-89` 2026-11-02 language rule (Hawaiian dominant, then whoever holds the majority). `DR-90` 2026-11-02 Esperanza cut to 1,200,000 and the difference spread over other cities (the "second population change"). `DR-93` Kazakhstan added to the pool. `DR-94` Manchuria's share reduced. `DR-96`/`DR-97` 2026-11-03: the robot-keyed requirement added to the Division of Industry file 16. `DR-48`/`49`/`50` Hobart and Ushuaia as primary ports, three mainland terminals for bulk freight.

---

## 1 Summary

1. The pass is less exposed to the composition rework than it looks. Its own rule (Phase 2 A.1) says no finding rests on a percentage, and the findings rest on structure (an assigned founding, no shore, a rock/ice split, the Acts). The structural spine, the Phase 3 to 7 reasoning and the whole relation layer re-derive the same way on the evidence read.
2. Every headcount, share and derived ratio in the pass is now wrong a second time. Census I is 1,112,600 (was 1,060,482 at the pass, 1,084,399 on 10-30); Census II is 691,371. Retention is 62.14% combined, 58.47% humans, 65.67% robots (the pass said 61.81 / 58.31 / 65.17).
3. Three places might genuinely come out differently: Phase 2 A.2 and Spine G8 (the "flat Significant tier, no runner-up" shape is gone: now one large group, two near-equal groups at 9.65% and 9.10%, then a drop to 4.49%); Frame section 2 (Census I is now 11.3% over the one-million line, not 6%, which weakens the "treat the excess as margin" reading); Phase 8 F and Phase 9 C.1 (the language reasoning, because Hawaiian is dominant everywhere and Japanese is Shirayuki's supporting language alone).
4. Two statements are false as written beyond numbers: "the percentages are ratios and did not move" (Division of Industry shares moved 40.9/11.8/47.3 to 42.0/11.6/46.4 when the robot-keyed requirement was added), and "retention is immune to the census rebalancing" (it moved again). Also, the open question about the national-connections file (a station-heritage tie the pass set aside) was closed 2026-10-01; the pass still calls it open in ten places. The 10-30 amendment note does not record that.
5. Unchanged and safe: the Founding Register row, climate, extent figures in the extent file, Highways and Airports rows, the Ports section on the Tri-Cities port, symbol assignment (already corrected inside the pass), the robot-religion roster, national holidays, the physiology documents (only an additive ossuary ruling), and the differentiation tables.
6. A source defect found in passing: the spec's own prose still says Japan is 34.71% (lines 35 and 321) while its table says 34.20%.
7. The 10-30 amendment note's "live" figures (SRY-001 to SRY-003, SRY-006, SRY-S02, SRY-S03) are stale again; section 5 lists them.
8. Recommendation: a new dated amendment note covers almost everything. Re-derive only Phase 2 A.2 with Spine G8, Frame section 2, and Phase 8 F with Phase 9 C.1. Totals: C 3, W 11, N 8 groups, U 4 (section 3).

---

## 2 Changed inputs

Values are Shirayuki's own. "Line" is at HEAD unless stated.

| # | Item | At pass (5c339aee) | At 10-30 (c3e31166) | Now (HEAD) | Source line |
|---|---|---|---|---|---|
| 1 | Census I humans / robots / total | 518,822 / 541,660 / 1,060,482 | 530,961 / 553,438 / 1,084,399 | 545,891 / 566,709 / 1,112,600 | `Official_Population_Census.md` L505 (was L495 at pass, L493 on 10-30); spec L41 |
| 2 | Census II humans / robots / total | 302,512 / 352,980 / 655,492 | 310,620 / 360,719 / 671,339 | 319,190 / 372,181 / 691,371 | census L653 (was L616, L620); spec L42 |
| 3 | Retention humans / robots / combined (computed from rows 1 and 2) | 58.31% / 65.17% / 61.81% | 58.50% / 65.18% / 61.91% | 58.47% / 65.67% / 62.14% | computed |
| 4 | Humans / robots gone, people not here | 41.69% / 34.83%, 404,990 | 41.50% / 34.82%, 413,060 | 41.53% / 34.33%, 421,229 | computed |
| 5 | Robot retention minus human retention | +6.86 pp | +6.68 pp | +7.20 pp | computed |
| 6 | Robot share Census I then II | 51.08% then 53.85% | 51.04% then 53.73% | 50.94% then 53.83% | computed |
| 7 | Census I distance over the one-million Band 5 line | 6.0% | 8.4% | 11.3% | computed |
| 8 | Required footprint at 10,000 and 7,000 per km2 | 106.0 to 151.5 km2 | 108.4 to 154.9 km2 | 111.3 to 158.9 km2 | computed |
| 9 | Share of footprint on the shared rock (13.4 km2, cluster share 33.4% unchanged) | rock 8.8 to 12.6%, ice 87.4 to 91.2% | rock 8.6 to 12.4% | rock 8.4 to 12.0%, ice 88.0 to 91.6% | computed; cluster Census I 3,330,740 (was 3,174,386) |
| 10 | Tier of Japan | Primary 36.27% | Primary 36.27% | Primary 34.20% (spec table L62) | spec L62; census L426 |
| 11 | Significant tier | Australia 8.76, Russia 8.61, South Korea 7.89, China 7.18, Germany 4.93 | same | Australia 9.65, Korea 9.10 only | spec L47, L63-64 |
| 12 | Where the old Significant members went | n/a | n/a | Sinian Federation 4.49 (Notable, 4th largest); Germany 3.90; Russia (core state) 3.53 plus Idelsk-Uralia 2.55, Siberia 1.01, Donska-Kubania 0.97, Kunnarantaiga 0.58 and 7 small Caucasus/Siberian rows (about 9.1% if all added); Taiwan 2.86, Manchuria 0.26, Mongolia 0.21, East Turkestan 0.13, Tibet 0.02 as separate rows | spec L65-100 |
| 13 | Number of origins in the table | 17 (1 + 5 + 11) | 17 | 38 (1 + 2 + 35) | spec L62-100 |
| 14 | Division of Industry file 16, Half B row | 890,078 workers (pre-cut); 40.9 / 11.8 / 47.3 % | 818,918; 40.9 / 11.8 / 47.3 | 839,655; 42.0 / 11.6 / 46.4 | `16_Per_City_Three_Tier_Run.md` L277 (was L276, L277) |
| 15 | File 16 section for Shirayuki (counts) | 363,971 / 105,222 / 420,886 (sum 890,079, pre-cut) | same (note SRY-006) | 352,970 / 97,337 / 389,348 (sum 839,655; baseline now includes 8,926 robot-keyed workers) | `16` L1758-1760, L1769 |
| 16 | File 09 row | required 315,192 of 890,079 = 35.4% | 290,137 of 818,919 = 35.4% | 297,848 of 839,655 = 35.5% | `09_Per_City_Baseline_Run.md` L78 |
| 17 | Pass's "25% of workforce" and "20%" test | 25% x 801,070 = 200,270; 20% = 160,210 | 204,730 (note SRY-003) | 209,914 and 167,931 on the pass's own reading (file 16 now counts sectors as shares of the 58.0% distinctive tier: education 97,337) | `04_Phase_07` L38-40 |
| 18 | Founding Register row | did not exist (Register created 2026-10-01 as "Allocation, not geography", unconfirmed) | confirmed, adds geography (zone gap 3) | same text; only its pointer changed (spec L175 to L203) | `Founding_Register.md` L61 |
| 19 | National-connections entry (relation file) | Shirayuki lists Temirotkel (then Sayowa) as a Medium Cultural tie built on a "Bharati-Station-descended founding" | already replaced on 2026-10-01 (commit `67d091af`) | replaced by "Temirotkel, Medium, Infrastructure: Hwy 4"; Utstein tie reworded | `City_National_Connections.md` L388-394 |
| 20 | Status of the station-heritage question the pass called open | open, 5th of five open questions | closed 2026-10-01 | closed (the offending line is gone, tie re-grounded on Highway 4) | `Developer_Ruling_Queue.md` L696 |
| 21 | Language | no language ruling; robot doc "vernacular tracks the dominant local culture" | none | Hawaiian dominant everywhere (later Tepenian); next language is whoever holds the majority; Shirayuki: Japanese 34.2, nothing within 5 or 10 points; supporting tier = groups within 12 points of the largest, so Japanese alone | `Language_Sets_By_City_Reference_2026-11-03.md` L34; `DR-89` |
| 22 | Developer statement that Tepenian is "down at its foundational level core, a Pidgin between English and Japanese" | absent | absent | in `DR-85` verbatim column | `DEVELOPER_RULINGS_LOG.md` L1523-1527 |
| 23 | Spec prose (non-table), every edit | see below | see below | see below | spec |
| 24 | Ports file, Tri-Cities port section 5.6c | unchanged text | unchanged | unchanged (118 lines identical) | `Ports.md` section 5.6c |
| 25 | Ports file, gateway distance table | no Tri-Cities row | row added 2026-10-04 (`DR-48` to `DR-50`) | "4,877 to 4,884 km, Zhongshan, Sinheung, Shirayuki, Tri-Cities Port, long haul, seasonal, shared" | `Ports.md` L202 |
| 26 | Culture file (`Local_Cultures/.../Shirayuki.md`) | read at Step 5 | edited 10-01 | 8 line pairs changed: 36.27 to 34.20; Sejong to Contrapunto; Sayowa contrast sentence replaced; two comparison phrases removed. The nine Step 5 corrections are still not applied (census 1,178,313, "60 days", "shared with Sinheung", Bharati landmark all still present) | culture file L9, L42, L48, L34 |
| 27 | Symbol assignment (Uranus + Fire) | Uranus / Fire | Uranus / Air | Uranus / Air | `City_Symbol_Assignments.md` L117 |
| 28 | Robot physiology doc | no ossuary rulings | ossuary rulings of 2026-09-07 present | same | `Robot_Physiology_and_Cultural_Practices.md` |
| 29 | Upper Earth immigration composition | Shirayuki sole Primary China (starting derivation) | same | same table, plus a 2026-11-02 banner and a "final composition" line (Primary Japan; Significant Australia, Korea; 35 Notable) | `Upper_Earth_Immigration_Composition.md` L559-570 |
| 30 | Inspirational-Influences | Shirayuki picks: Shibuya, Harajuku, Hongdae, Novosibirsk | same | same picks; a new scope note at the top (picks judged on structure, never nationality) | `Inspirational-Influences.md` L113-117 |

**Spec prose edits (item 23), diff excluding table rows, pass to now.** (a) Highway line: "Sayowa Junction" to "Temirotkel Junction" (names only). (b) Significance line: "not an organic real-station inheritance like Sayowa's, but ... one of only two" shortened to "a mechanism Sinheung shares" (comparison removed, `DR-88`). (c) Canon note typo: the real station name corrected from "Shirayuki" to "Bharati". (d) Founding note: "Rather than force an organic real-station-adjacency explanation the way Lazar's resolution used" deleted; "Sejong" to "Contrapunto". (e) Contributing-factor paragraph: Temirotkel now "Sinian-Federation-led (9.73%, largest of five near-equal Primary communities), Japan 2.66%"; Shirayuki "34.71% ... was 36.27%". (f) Census I and II lines: new totals with notes. (g) Zhongshan distance 15 km to 8 km (2026-10-01) in the climate-proxy and oasis lines. (h) Founding-population line: comparison to Sayowa's JARE identity deleted. (i) Working note: contrast with Sayowa deleted. (j) "26 of the 37 are colder" deleted. (k) Ayako Hayashi line: 36.27 to 34.71. (l) New 2026-11-02 rework note and the replaced table. **Unchanged: Annual Climate figures and table, Highway/Access fields, Notable Locations, Economy and Industry, Character and Culture, Open Questions.**

**Source defect found.** The spec table says Japan 34.20% (L62) but its own prose still says 34.71% (L35 and L321; 34.71% was the figure after the first 11-02 pass before Kazakhstan, `DR-93`, and Manchuria, `DR-94`, were applied). The census prose at L422 still says 36.27%. The culture file L9 and the national-connections file (Temirotkel entry) quote 34.20 correctly.

### Five most important raw diff excerpts

**(1) Spec tier table, 10-30 to now** (`git diff c3e31166 HEAD -- Specs/Mirny subnet/Shirayuki.md`)
```
-| Primary | Japan *(founding population — Jeju-do diplomatic allocation; re-tiered 2026-07-06)* |
-| Significant | Australia, Russia, South Korea, China, Germany |
-| Notable | Romania, Vietnam, Ukraine, Belarus, Thailand, New Zealand, Lithuania, South Africa, Bulgaria, Latvia, Estonia |
+| Primary | Japan *(founding population — Jeju-do diplomatic allocation)* |
+| Significant | Australia, Korea |
+| Notable | Sinian Federation, Germany, Russia (core state), Romania, Vietnam, Taiwan, Belarus, New Zealand, Thailand, Idelsk-Uralia, Ukraine, ... (35 rows)
-| Primary | Japan | 36.27% | 200,733 | 192,580 | 130,838 | 112,666 |
+| Primary | Japan ... | 34.20% | 193,839 | 186,718 | 127,306 | 109,181 |
+| Significant | Korea | 9.10% | 51,541 | 49,647 | 33,853 | 29,032 |
+| Notable | Sinian Federation | 4.49% | 25,445 | 24,509 | 16,711 | 14,331 |
```

**(2) Census rows** (`Official_Population_Census.md`)
```
5c339aee L495: | 12 | Shirayuki | Mirny | 518,822 | 541,660 | **1,060,482** |
c3e31166 L493: | 12 | Shirayuki | Mirny | 530,961 | 553,438 | **1,084,399** |
HEAD     L505: | 12 | Shirayuki | Mirny | 545,891 | 566,709 | **1,112,600** | ... DR-90, 2026-11-02: +14,930 H / +13,271 R
HEAD     L653: | 17 | Shirayuki | Mirny | 319,190 | 372,181 | **691,371** | ... DR-90: +8,570 H / +11,462 R
```
Census II humans and robots moved by different amounts (+8,570 vs +11,462), so the ratios moved.

**(3) Division of Industry file 16, Half B row** (`16_Per_City_Three_Tier_Run.md`)
```
5c339aee L276: | Shirayuki | Mirny | 1.25 | 890,078 | 40.9% | 11.8% | 47.3% | C |
c3e31166 L277: | Shirayuki | Mirny | 1.25 | 818,918 | 40.9% | 11.8% | 47.3% | C |
HEAD     L277: | Shirayuki | Mirny | 1.25 | 839,655 | 42.0% | 11.6% | 46.4% | C |
```
The shares moved (not only the counts) because `DR-97` added the robot-keyed baseline term (8,926 workers).

**(4) National-connections file, Shirayuki entry** (`City_National_Connections.md`)
```
5c339aee: - **Sayowa** (Mawson) — Medium, Cultural. Shirayuki's own Bharati-Station-descended founding and Sayowa's own
            JARE heritage are Tepenia's two clearest living Japanese-institutional-heritage civic identities ...
HEAD L393: - **Temirötkel** (Mawson) — Medium, Infrastructure. Hwy 4 runs from the Temirötkel Junction to Shirayuki, the same
            Spur/Junction link that reaches Sinheung alongside it.
```
The pass set the first form aside as a station-heritage breach and left it "open"; the file has been fixed since 2026-10-01.

**(5) Language** (`DR-89` verbatim and the sets table)
```
DR-89: "For all of the locations, the dominant language is always Hawaiian, which later becomes Tepenian.
        The next dominant language after that is whoever holds the majority."
DR-85: the Tepenian language is, "down at its foundational level core, a Pidgin between English and Japanese"
Language_Sets_By_City_Reference L34: | Shirayuki | Japanese 34.2 | none | none |
Pass 04_Phase_08 L206: "Japan is Primary at 36.27%, so the dominant local vernacular follows from that"
```

---

## 3 Dependent findings

Classes: **N** number or label only. **W** wording or identity statement now false as written. **C** conclusion or reasoning step that might come out differently on re-derivation. **U** cannot tell without re-running. Files are in the Shirayuki pass folder.

### C (3)

| ID | Pass file and line | What it says | What changed | Note |
|---|---|---|---|---|
| C1 | `04_Phase_02` L58-71 (A.2); `02_Spine` L132, L123-124 (G8 STRENGTH); `00_Frame` L311 | "The Significant tier is unusually FLAT, 8.76 / 8.61 / 7.89 / 7.18 / 4.93. There is a plurality and no runner-up; four equal middle groups mean no available second pole." Spine adds "genuine breadth, 17 origins". | Significant tier is now two groups, Australia 9.65 and Korea 9.10 (0.55 apart), then a drop to Sinian Federation 4.49 and a 35-row tail. Russia, China, Germany are Notable. Breadth is 38 origins. If the Russian-derived rows are counted together they sum to about 9.1% (the language bloc file gives the Russian language bloc 6.1 to 15.3%), so the answer depends on grouping. | The Act 2 half of the argument ("by Act 2 these are ancestry figures, so no national blocs at all") does not depend on the tiers and stands. The Act 1 half ("no runner-up") was derived from the flat shape and would be rewritten: one 34% group, two near-equal 9% to 10% groups, long tail. The claim "no available second pole" likely survives (3.5 to 1) but is no longer self-evident. |
| C2 | `00_Frame` L28-33 and the Reading A/B/C table (section 2); `00_Frame` L156-186 | Band 4 chosen provisionally; "Census I sits 6% above the line"; Reading A "Census I's excess treated as margin". Flagged `DRQ-10`, open. | Census I is now 1,112,600, 11.3% (112,600 people) over the line. `DRQ-10` is still open (unchanged in the queue). | The provisional choice rested partly on a small excess. At 11% it is a weaker "margin" and the Band 5 obligation for the pre-orbital half presses harder. Likely still written at Band 4 pending the ruling, but the justification sentence would change. |
| C3 | `04_Phase_08` L198-215 (F), L404-411 (F.STOCK); `04_Phase_09` L96 (C.1 Language row) | "Robot vernacular tracks the dominant local culture. Japan is Primary at 36.27%, so the dominant local vernacular follows from that." The keptness vocabulary is a local occupational register carried as vernacular, built from the stock's own material-care vocabulary. | Language is now set as a fact of the place: Hawaiian dominant everywhere, Japanese Shirayuki's supporting language alone (`DR-89`; sets reference). The developer also said the Tepenian language is at its core a pidgin of English and Japanese (`DR-85`). | The dominant-vernacular sentence is false as written (W) and its reasoning (composition tier gives the language) is replaced by an explicit rule. Whether the "keptness register as a Shirayuki marker" still marks a person as from here, when the national language's core is partly Japanese, needs a re-look. The register claim is occupational, not national, so it may stand. |

### W (11)

| ID | Pass file and line | What it says | What changed | Note |
|---|---|---|---|---|
| W1 | `01_Inherited` L95-99; `05_Reconciliation` L177-178 | "The whole retention layer is immune to the census rebalancing"; "the ratios are correct and unchanged". | Not true after `DR-68` and `DR-90`: Census II humans and robots moved by different amounts. Combined retention 61.81 to 62.14; robot retention 65.17 to 65.67; gap 6.86 to 7.20 pp. | The 10-30 note already corrected the `DR-68` instance. This is the second. Direction of every finding that uses the gap is unchanged (humans left harder). |
| W2 | `04_Phase_04` L43-44; `02_Spine` L60, L316-318 | "workforce is a COUNT, so it moved; the percentages are ratios and did not"; "[M-148: ratios hold]". | Shares moved: baseline 40.9 to 42.0, mandated 11.8 to 11.6, free 47.3 to 46.4, distinctive 59.1 to 58.0. Cause: the robot-keyed term (`DR-97`). | False as written. |
| W3 | `04_Phase_02` L40-44 (A table); `02_Spine` L123-124; `00_Frame` L311 | Tier lists and the "Eleven Notable nations, 1.22 to 3.54"; "16 further nations". | Tier lists differ (section 2 rows 10 to 13). | Replace with a dated pointer. |
| W4 | `01_Inherited` L217-219; `02_Spine` L135 (G8 grudging tolerance) | "China is the fifth-largest origin at 7.18%, about 47,000 people; 7.18% of this city descends from the nation the founding refused." | The court's "China" is now the Sinian Federation at 4.49% (fourth largest), 31,042 people at Census II. Its four detached pieces (Manchuria, Mongolia, East Turkestan, Tibet) sum to 0.62% and Taiwan is a separate 2.86%. | The structure (descendants of the refused party live eight kilometers from Zhongshan) stands. Which rows count as "the refused nation" is a choice a re-run would make explicit. |
| W5 | `01_Inherited` L260-282 (A4 vindication) | "Shirayuki held its plurality at 36.27%"; "63.73% of this city is not Japanese by origin"; Australia, Russia, South Korea, China and Germany "are all Significant". | 34.20%; 65.80%; Significant is Australia and Korea. The quoted spec sentence "the diplomatic foresight worked exactly as intended" is unchanged, but its sibling sentence now cites Temirotkel at 9.73% Sinian Federation and 2.66% Japan. | The finding (the verdict is retrodictive and category-shifted across the Act boundary) is unaffected. |
| W6 | `00_Frame` L148; `04_Phase_02` L283; `04_Phase_05` L89-92 and L258; `05_Reconciliation` L346; `07_QA_Gates` L32 and L126; `09_Record` L35 and L99; `10_Readiness_Check` L133 | The station-heritage tie in the national-connections file is "open, queued, canon relationship currently unusable, this pass takes nothing from it". | Closed 2026-10-01; the offending line is gone, the tie re-grounded on Highway 4 (item 20). | **Not in the 10-30 note.** Ten places call it open. The Highway 4 Temirotkel tie is now a usable Medium-Infrastructure relation; Phase 5 5d already covers the same highway fact, so no finding changes. |
| W7 | `02_Spine` L82 | "the margin is an UPPER BOUND, and the correction is largest at robot-majority cities; the character budget is smaller than it looks." | The correction is now applied inside file 16 (`DR-97`): free fell 0.9 points. | Stated as pending; it is now done. |
| W8 | `02_Spine` L74-75 | "TWO BASELINES EXIST IN THE SOURCE: 09 records 35.4%, 16 records 40.9%." | 35.5% and 42.0%. File 09 now explains the difference: the two files agree on the robot term but still differ on B1 (53 in 09, 120.7 in 16), "so the two baselines are not the same quantity". | The pass's choice (use 16) stands and is now documented in the source. |
| W9 | `05_Reconciliation` L172-175 and L333 (Step 5 stale-figure table and docket row 1) | "Current" census column for the culture-file proposals. | "Current" is now stale; culture file still has the pre-cut figures. | Proposal 1 is unapplied; its target figures changed twice. |
| W10 | `02_Spine` L81 | "against a US comparable of about 29% this city carries +11.9 points". | 42.0 minus 29 = +13.0 | Wording only. |
| W11 | `04_Phase_10` L134 | Capricorn yield "40.9%, the ice work". | 42.0% | Wording only. |

### N (9 groups, numbers or labels only)

| ID | Pass file and line | What it says | What changed | Note |
|---|---|---|---|---|
| N1 | `00_Frame` L28-31, L157-159; `01_Inherited` L80-111, L229, L243; `03_Research` L314; `04_Phase_02` L75, L94; `04_Phase_09` L24-25; `07_QA_Gates` L167-175 (pasted scan output); `09.6_Input_Audit` L35 | Census I and II headcounts. | Section 2 rows 1 and 2. | The pasted Gate 11 scan output is a record of the 2026-09-06 run and should not be edited; a dated note beside it is enough. |
| N2 | `01_Inherited` L86-121 (table), `00_Frame` L311, `02_Spine` L125, L133, `03_Research` L163, L234-250, `04_Phase_02` L94, L244, L273, `04_Phase_05` L234, L246-247, `04_Phase_07` L128, `04_Phase_09` L24-25, L108, L202, `04_Phase_10` L288, `04z` L62, L251, `07_QA_Gates` L175 | Retention, departure counts (404,990; 216,310; 188,680), 41.69 / 34.83, +6.86 pp. | Section 2 rows 3 to 5. | Direction of every claim unchanged. |
| N3 | `01_Inherited` L91, L113; `02_Spine` L82, L125; `03_Research` L163, L394; `04_Phase_02` L75-76, L205, L340; `04_Phase_07` L55; `04_Phase_08` L162; `04_Phase_09` L24 | Robot share 51.08 to 53.85, +2.77. "Built rather than born" majority. | 50.94 to 53.83, +2.90. Still a robot majority at Census II. | The arguments need only "majority robot", which holds. |
| N4 | `00_Frame` L36, L40, L305, L366; `01_Inherited` L251, L351, L384; `02_Spine` L47-49, L239-261, L280; `03_Research` L48, L124, L234; `04_Phase_02` L296; `04_Phase_03` L82-83, L207; `04_Phase_04` L48, L61; `04_Phase_06` L58, L77; `04_Phase_07` L61, L113; `04_Phase_08` L252; `04_Phase_09` L288; `04_Phase_10` L76, L224; `04z` L72, L106, L109; `05` L299; `07_QA_Gates` L166-187; `09_Record` L98, L110; `10_Readiness_Check` L255 | Footprint 106 to 152 km2; rock 9 to 13%; ice 87 to 91%; "79,360 per km2, 1.73x Manila". | 111 to 159 km2; rock 8 to 12%; ice 88 to 92%; cluster 3,330,740 on 40 km2 = 83,269 per km2 (about 1.8x the same comparable). | Gate 11 still clears. Per-city density is still forced equal to cluster density by construction (the pass's own tautology note). |
| N5 | `00_Frame` L306; `02_Spine` L60-66, L79, L156-157, L194, L260-264, L278-283; `03_Research` L368; `04_Phase_02` L153; `04_Phase_04` L62, L166; `04_Phase_07` L32; `04_Phase_08` L181; `08_Review_Panel` L57, L205 | 40.9 / 11.8 / 47.3; 890,078 / 801,070; 105,222; 420,886; 363,971; 59.1% distinctive. | Section 2 rows 14 and 15. | The conclusion "free tier is large, mandated tier is one sector (a university)" holds at 46.4% and 11.6%. |
| N6 | `04_Phase_07` L38-40, `07_QA_Gates` L96 | 25% x 801,070 = 200,270; 20% = 160,210; 45% = 360,480. | 209,914; 167,931; 377,845 on the pass's reading. | Pre-existing inconsistency worth noting: the pass uses 105,222 (mandated education, a share of distinctive) in Phase 2 and 03 but 160,210 (20% of whole workforce) in Phase 7 and Phase 10 L223. The "two hundred thousand is not artists" test passes either way. |
| N7 | `02_Spine` L236-253 (Step 2.6 division) | Cluster 3,174,386; 13.4 km2; footprint 106/151; 12.6/8.8% on rock. | Cluster 3,330,740; 13.4 km2; 111/159; 12.0/8.4% on rock. | Gate 11 note above. |
| N8 | `04_Phase_02` L184; `02_Spine` L132; `00_Frame` L311 | "seventeen national origins"; "17 origins"; "16 further nations". | 38 rows. | Folded into W3 and C1. |

### U (4)

| ID | Pass file and line | What it says | What changed | Note |
|---|---|---|---|---|
| U1 | `04_Phase_05` L137-152 (5d.1), L168-198 (5e), L204-209 (section 6) | Supply line unloaded at a neighbor; four-month window; berthing queue; "merger driven by the city that could not walk to the harbor". | The Ports file (section 5.6c) is word-for-word unchanged. New context: Hobart ruled the primary gateway for people and special cargo; three mainland terminals (Perth, Adelaide, Melbourne sites) carry the bulk freight; the Tri-Cities port is "long haul, seasonal, shared" (`DR-48` to `DR-50`, `Ports.md` L202). | Additive. Does not contradict the mechanism. Nothing says the Tri-Cities' freight origin was ever different. |
| U2 | `04_Phase_06` L166-181 (death, ossuaries); `00_Frame` L326 (mortuary question) | Ossuary "is itself a keeping-practice"; mortuary question deferred, do not answer. | 2026-09-07 rulings in the robot physiology doc: a Tepenian ossuary holds robots' metal bones and the bones of the humans who loved them; it is sacred and untouchable; metal persists while calcium reduces. The doc says nothing is adopted and the mortuary question stays deferred. | The pass's refinement is compatible and slightly strengthened. Cannot tell whether a re-run would use it. |
| U3 | `04_Phase_05` L82-87 (wider set) | Princess Elisabeth tie "UNEXPLAINED"; kinship tie to Vostok. | Utstein tie now reads "only Halley subnet city with genuine Japanese demographic presence"; the Utstein spec shows Japan Significant, not Primary. Ariun Nuur (Vostok): Japan is still Primary, now alongside Indonesia (was USA and Japan). | The "Vostok is Japanese-Primary" sentence (`04_Phase_07` L360-361) remains true in letter. Already partly recorded as `SRY-007`. |
| U4 | `04_Phase_08` L318-410 (origin-stock addendum) | Stock is Japanese; "Japan is Primary at 36.27%"; stock is an input, never an output. | Number moved; Japan still the sole Primary; Register still names Japan. Language row (C3) bears on how the stock addendum's "no word named" discipline reads against a pidgin-Japanese national language. | Cannot tell without re-running that addendum. |

**Counts: C 3, W 11, N 8 groups, U 4.** Totals of individual file lines are in the N rows.

**Checked and not affected (stated as results).**
- `04_Phase_03` (surface and texture): rests on climate and the physiology docs, none changed.
- `04_Phase_05` 5a, 5d, 5d.2, 5b, 5c (peers, edge, junction, own eras, parent): the Highways, Airports and Ports section 5.6c lines naming Shirayuki are unchanged apart from renames.
- `04_Phase_07` 7b governance (three facts "none decided by Shirayuki") and the National Institutes addendum: the institutes file's Shirayuki lines are unchanged (names and Esperanza figures only).
- `04_Phase_09` populations (lens, shared exclusion, merger cost to robots, deferral calendar): rest on structure and canon.
- `04_Phase_10` catalog, zodiac, places, events: only the 40.9% and departure counts (W11, N2).
- `06_Differentiation`: Shirayuki's nine cells unchanged; tables only gained columns/rows.
- `08_Review_Panel`: only the 47.3% figure (N5).
- `01_Inherited` A2, A3, A5, A6, A7 and section 5, 6, 6a, 6b: structure and the Acts. Section 6's "only an exodus can re-sort the rock" uses the counts (N2).
- `04z` sections 1, 3, 4: Acts and physical ground; only the footprint percentages (N4).

---

## 4 Checked and unchanged

- **Founding Register row** (L61): same text since 10-30; only the spec pointer line changed. The pass does not cite the Register; `SRY-005` of the 10-30 note still reads correctly.
- **Climate and site facts in the spec**: Annual Climate figures and monthly table, proxy station, precipitation 148.9 mm, polar night and midnight sun, katabatic text. Climate READER file for Shirayuki unchanged since the pass; recomputed-normals file shows zero difference for Shirayuki.
- **Extent figures in `Extent_and_Density_Per_City.md`**: Shirayuki rows (L616, L656-660) and the "MIXED, about 10% rock" band unchanged (the 10-30 note's `SRY-S02` still stands).
- **Highways**: Hwy 4 eastern terminus, the tri-junction with Hwy 110 and Hwy 22: unchanged apart from "Temirotkel Junction". Relationship database highway rows: unchanged apart from names.
- **Airports**: Tri-Cities shared airport and Shirayuki as a listed host: unchanged (the list grew by Relung Panen's two airports).
- **Ports**: section 5.6c (118 lines) identical; the Tri-Cities port is still "constructed" tier.
- **Symbol files**: Uranus / Air assignment already reflects the pass's own Phase 10 correction; Uranus entry text and `Robot_Elementals.md` Air entry unchanged (the Planetary Symbols file gained a Sun entry only).
- **Robot religions** roster (six faiths): no Shirayuki hit then or now. **National holidays**: one phrase removed, no Shirayuki content.
- **Cold physiology doc, Weapons and Tools Philosophy, Division of Industry file 04 row** ("arts/music/fashion 25% plus education 20%"): unchanged.
- **National economy and currency doc**: changed 2026-09-16, but the pass already writes "backing unsettled, not energy-backed" (`04_Phase_04` L246-247).
- **Differentiation tables**: Shirayuki's cells unchanged in both.
- **Vision notes**: names and the 34.20 figure only.
- **Cities in the pass's name set**: renames already recorded as `SRY-004` (Relung Panen, Temirotkel, Utstein, Ariun Nuur). No rename since 10-30 touches a name the pass uses.
- **Rulings log**: entries naming Shirayuki since the pass are `DR-29` (Davis and Shirayuki stay), `DR-44` (Register row), `DR-85`, `DR-90`, `DR-93`, `DR-94` (all population). None changes a structural fact.

---

## 5 Amendment-note figures stale again (`Amendment_Notes_2026-10-30_Manual_Input_Audit.md`)

| Note entry | Says "live" | Now |
|---|---|---|
| SRY-001 table | Census I 530,961 / 553,438 / 1,084,399; Census II 310,620 / 360,719 / 671,339; live rows census L505 and L620 | 545,891 / 566,709 / 1,112,600; 319,190 / 372,181 / 691,371; L505 and L653. "Live since `DR-68`" is now `DR-90` (2026-11-02) |
| SRY-001 "files carrying old value" counts | 6 and 7 files | not recounted; every old count changed again |
| SRY-002 | Retention 61.91 / 58.50 / 65.18; not here 413,060; gone 41.50 / 34.82; gap +6.68 | 62.14 / 58.47 / 65.67; 421,229; 41.53 / 34.33; +7.20 |
| SRY-002 closing remark | "the retention layer ... held for the 10% cut, did not hold for `DR-68`" | holds for neither `DR-68` nor `DR-90` |
| SRY-003 | 8.4% above; 108 to 155 km2; rock 9 to 12%; ice 88 to 91%; workforce 818,919; 09 L78 required 290,137 (35.4%); 25% = 204,730 | 11.3%; 111 to 159 km2; rock 8 to 12%; ice 88 to 92%; workforce 839,655; required 297,848 (35.5%); 25% = 209,914 |
| SRY-006 | file 16 section counts 363,971 / 105,222 / 420,886 "pre-cut", Half B 818,918 and 40.9 / 11.8 / 47.3, at L1754-1760 and L277 | section now 352,970 / 97,337 / 389,348 at L1758-1760, recounted and consistent with Half B 839,655 and 42.0 / 11.6 / 46.4 at L277. The "pre-cut" problem no longer exists; the shares changed |
| SRY-S01 | census L426-428 tier list; "file is 810 lines" | tier list replaced by `DR-85` (Primary Japan; Significant Australia, Korea; 35 Notable); file is 892 lines |
| SRY-S02 | "Live: 1,084,399 needs 108 km2 and 155 km2"; extent L616 and L656 | 1,112,600 needs 111 and 159 km2 |
| SRY-007 | `Airports.md` L18 Mountain Pass row | still L18, still correct |
| SRY-005 | Register L61, spec L203, DR-44 | still correct |
| **Missing from the note** | n/a | The station-heritage question (`DRQ-14`) closed 2026-10-01 (W6); the 2026-10-01 distance change Zhongshan 15 km to 8 km (no pass impact: the pass already says eight); the composition, language and Division of Industry share changes above |

---

## 6 Ranked recommendation

**Re-derive (small, targeted).**
1. `04_Phase_02` A.2 with `02_Spine` G8 STRENGTH (C1): rewrite the tier-shape sentence on the new composition; check whether "no available second pole" still holds for Act 1 and decide how the Russian-derived rows are grouped. The Act 2 argument can stay.
2. `04_Phase_08` F and F.STOCK with `04_Phase_09` C.1 (C3): restate the language from the rule (Hawaiian dominant, Japanese supporting alone) and re-check the keptness-register claim against a national language that has a Japanese core.
3. `00_Frame` section 2 (C2): re-word the provisional Band 4 choice for Census I at 1,112,600; `DRQ-10` is still the open question.

**Dated amendment note only (no finding changes).** Everything in N1 to N8 and W1 to W11: new census rows, retention, robot share, footprint and rock/ice shares, workforce and Division of Industry shares, 17 versus 38 origins, tier lists, "7.18% descends from the refused nation", "36.27%", the "ratios hold" and "immune" sentences, the closure of `DRQ-14`, and the robot-term note. The note should also supersede the 10-30 note's live tables (section 5), and should be written once the ongoing population work is done, since the totals have already moved twice in a week.

**Nothing needed.** Phases 3, 5 (mechanism), 6 (except the optional ossuary note), 7 (except counts), 9, 10 catalog, 06, 08, 05's reconciliation logic, the Register-based claims, climate, symbols, extent, highways, airports, the Ports section on the Tri-Cities port.

**Source files that need fixing before any re-derivation (not pass edits).** The spec prose (L35, L321) says 34.71% where the table says 34.20%. The census prose (L422) still says 36.27%. The culture file still carries the pre-cut census (L9), "shared with Sinheung" (L42, L263), "60 days" (L48) and the Bharati landmark (L34, L100, L262): the Step 5 docket is still entirely unapplied. The runbook still quotes 36.27% and Temirotkel's old shares at L2130-2131. The pass README current-state table is stale (it still shows Phase 9, 04z and Phase 10 as not done, which contradicts `09_Record`).

---

## 7 Commands run and what I could not do

**Commands (all read-only, from the repo root).** `git log --format='%h %ad %s' --date=short <from>..HEAD -- <path>` for the spec, census, Division of Industry files 09 and 16, Founding Register, Ports, Highways, Airports, relationship files, National Institutes file, extent file, symbol folder, robot docs, culture file, vision notes, rulings queue and the pass folder. `git show <commit>:<path>` to write point-in-time copies of the spec, census, files 09 and 16, Ports, Highways, Airports, relationship files, extent file, rulings log, symbol and picks files into the session scratchpad; `diff`, `grep -n`, and `git diff -U0 <from> HEAD -- <path>` on those copies. `git diff --name-only 5c339aee HEAD` (3,216 files) filtered for "shirayuki" to find what to look at. `git ls-files`, `git grep -n` for the language rule. Two small Python calculations for retention, robot share, footprint and workforce. I read in full: README, the 10-30 amendment note, 00_Frame, 01_Inherited, 02_Spine, 09_Record, 09.6_Input_Audit, 04_Phase_02, 04_Phase_05, 05_Reconciliation (all but its last lines), 06_Differentiation, and large parts of 04z, 07, 10, 04_Phase_07, 04_Phase_08 and 04_Phase_09; the others by targeted reading around every hit of the input families (figures, language, relations, symbols, ossuary).

**Could not do or did not do.**
- `09.5_Log.md` (1,051 lines, the process record) was not read line by line. It holds 18 lines with the old figures; as the dated record of the run it should keep them. Phases 3, 4, 6, 8 and 10 were read in the parts where inputs bear on them, not every paragraph.
- No re-derivation was attempted, so every C and U is a judgment about what a re-run might change, not a result.
- The Shirayuki culture file's ethnic-composition claims were not re-reconciled.
- No Pre-Trip file exists for Shirayuki; the input list came from 00_Frame, 01, 02 and 09.6 as instructed. No Shirayuki datasheets were found to check.
- The graphify hook was ignored as instructed.
- **Exposure declaration.** I did not read any other city's pass folder or culture file and drew no comparison. Four incidental exposures: (a) a repo-wide `git grep` for the language rule returned file names (and one line) from other cities' Pre-Trip and datasheet paths; I did not use them. (b) The Language Sets reference table and the relationship and national-connections files list other cities in rows I scrolled past; only Shirayuki's rows are used. (c) I opened one other city's spec (Ariun Nuur) only to check the tier of Japan for the pass's own sentence "Vostok is Japanese-Primary" (relation). (d) The `Upper_Earth_Immigration_Composition.md` and Ports gateway sections list other cities; used only for Shirayuki lines.
