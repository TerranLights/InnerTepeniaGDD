# Unanimous count audit of the conflicting figures (2026-11-03, night)

**Order (developer):** go through each conflicting or ambiguous count one at a time; split off three sub-agents to count from each city's newest data; whatever they come up with unanimously is the count, and the counts must be unanimous.

**Method.** Ten items, run one after another. For each, three independent counters (they never saw each other's work) read the files as they stand on disk, applied the formulas in the sources by program, and returned exact numbers. A count stands only if all three agree on every number. If not, each counter saw the three answers and re-counted (up to three rounds). **Result: all ten items are unanimous; eight in the first round, two (Davis agriculture sizes, Davis polar-night days) in the second.** 36 counters in all. Raw answers, sources and conflicts the counters noted: `Unanimous_Count_Audit_2026-11-03_results.json` (this folder).

## The counts
| # | Item | Unanimous count |
|---|---|---|
| 1 | Davis, current three tiers (file 16 method, Census I 590,668 H / 619,764 R) | workforce 915,098; baseline 383,295 (41.9%); distinctive 531,803; mandated 252,606 (27.6%); free 279,197 (30.5%). The first-pass row's 20.3% / 37.8% is the agriculture-only mandate (186,131). |
| 2 | Davis agriculture | 35% of the distinctive tier = **186,131**; 35% of the whole workforce = **320,284**; difference **134,153** |
| 3 | Sinheung section 17 | workforce 767,363; baseline 321,100 = **41.84%**; distinctive 446,263 (58.2%); fabrication **200,818**; Institute half **11,157** |
| 4 | Russia's successor rows (the 13 names in census L857), rows and share sum | Davis 13 / 6.436; Mirny 13 / 6.817; Shirayuki 13 / 9.101; Sinheung 13 / 6.472; Zhongshan 13 / 5.706 (twelve Russian-language rows 5.685 plus Finland 0.021) |
| 5 | Composition rows (total / Primary / Significant / Notable; share sum) | Davis 45 / 5 / 2 / 38 (100); Mirny 36 / 6 / 11 / 19 (99.98); Shirayuki 38 / 1 / 2 / 35 (99.99); Sinheung 39 / 1 / 3 / 35 (99.99); Zhongshan 35 / 1 / 3 / 31 (99.99) |
| 6 | Census totals and Larsemann sum | Davis 1,210,432 / 817,475; Zhongshan 1,203,607 / 932,895; Sinheung 1,014,533 / 835,341; Shirayuki 1,112,600 / 691,371; the three Larsemann cities 3,330,740 (Census I) and 2,459,607 (Census II); Davis density on 410 km2: 2,952.27 and 1,993.84 per km2 |
| 7 | File 19, Davis | latest run: farm workforce **186,131**, share **44.2%**, reproduced from file 16 and the census |
| 8 | Davis polar night (68°35′S, 2026, Sun's upper limb) | **37** days without sunrise; **54** days without sunset. (The first round split 38 / 37 because two counters used a coarse declination formula; the accurate models give 37.) |
| 9 | Davis spec "about 45% retention" | **38.46%** (28 mm ÷ 72.8 mm) |
| 10 | Zhongshan Pre-Trip addresses | Opus 111 distinct, 110 exist (missing: `Zhongshan_Opus/09.6_Input_Audit.md`); Sonnet 111 distinct, 106 exist (missing five in `Zhongshan_Sonnet/`) |

## What the counts settled, and what was applied
**Applied (stale copies brought to the counted figure; each was a single number in place, no line shifts):**
- `Division_of_Industry/16` Sinheung section 17: baseline share 41.9% became **41.8%**, distinctive share 58.1% became **58.2%**, the sentence's 216,171 became **200,818**, and 12,010 became **11,157**.
- `16` Davis register item 11 prose: 181,808 became **186,131**, the whole-workforce comparison now says 320,284 (noting that file `04` §3 still quotes 306,780 and is not recomputed), and the gap is **134,153**.
- The Davis, Sinheung and both Zhongshan amendment notes carry the counted facts (and the Pre-Trip address entries ZSO-020 and ZSS-019).

**Counted but NOT applied (and why):**
1. **Davis, which pair is "the" split:** the arithmetic is settled (27.6% / 30.5% under the rule behind your ruling; 28.2% / 31.1% is what the same rule gave on the earlier workforce). Which pair to carry is yours; it is open question 1 in the Davis note.
2. **Sinheung, Half B (41.8 / 26.2 / 32.0) versus section 17 (41.8 / 27.6 / 30.5):** the counters confirm section 17's counts. The Half B mandate equals fabrication alone (26.17%); section 17 adds the Institute half. Which definition governs is open question 3 in the Sinheung note.
3. **Davis spec L109 "about 45% retention":** the spec's own numbers give 38.46%. The cause is probably that the 45% belongs to the oasis class of `Precipitation_Falls_vs_Lands.md` while the 28 mm belongs to the katabatic class (the two files disagree on Davis's class). Which number is wrong depends on the class, so it is not changed.
4. **The Extent file** (`Universal_Location_Methodology/Extent_and_Density_Per_City.md`): rows for Davis (L617, L636), Zhongshan (L613), Shirayuki (L616), Sinheung (L620) and the Tri-Cities sum (L593) carry earlier census totals. The table needs a full refresh for every city, not these four rows; the counted census totals above are the inputs.
5. **Culture files:** `Local_Cultures/Mirny_Subnet/Davis.md` L53 says 66–67 days; the count is 37 and 54. Culture writing waits for the window.
6. **Davis polar night, spec "55" versus 54:** the spec says "about 55"; left.
7. **File 19's earlier-run values** (189,548; 44.3%) are the first of two labeled runs; left.
8. **The Pre-Trips' raw verification lines** (for example "105 of 110"): raw tool output, left.
