# Russia-split proportions: the agent briefs (wave 2; saved 2026-10-29 so an interrupted agent can be re-dispatched)

**Why.** Developer, 2026-10-29 evening (Auto Mode, away): after the first wave, *"dispatch further subsequent subagents to research percentage-proportions for the various nations that have resulted from the Russia-split reorganization based on the data for the First Interwar Period."* In the Tepenian timeline Russia has split into several countries (the developer's map files in `y-files/Map Files/Russia/` and the novel repo's Russia surveys name them, for example Idelsk-Uralia, Künnarantaiga, Donska-Kubania and a Far Eastern composite called Country A). The GDD's composition tables still list one "Russia" in 14 cities. **These units research how each city's Russia share would divide among the successor nations, as DERIVED proportions. They edit no spec, census or composition file, rule nothing and recommend nothing; the reorganization itself is a later, separate job.**

**Units (outputs in this folder):**

| Unit | Task | Output file |
|---|---|---|
| RS1 | Data inventory and method | `Russia_Split_Proportions_RS1_Inventory_and_Method_2026-10-29.md` |
| RS2 | Proportions for Davis, Zhongshan, Shirayuki, Sinheung, Mirny, Casey, Relung Panen | `Russia_Split_Proportions_RS2_Mirny_Subnet_2026-10-29.md` |
| RS3 | Proportions for Troll, Santa Luce, Lazar, Concordia | `Russia_Split_Proportions_RS3_Halley_and_Janbogo_2026-10-29.md` |
| RS4 | Proportions for Byrd, Palmer City, Contrapunto | `Russia_Split_Proportions_RS4_Byrd_and_Palmer_2026-10-29.md` |

RS1 runs first; RS2 to RS4 start only after RS1's progress block is fully ticked, and read its file.

## The 14 cities that list Russia (from each city's spec table; draft shares; Census I counts are robots / humans)
| City | Subnet | Solar UTC | Tier | Share | Robots | Humans |
|---|---|---|---|--:|--:|--:|
| Byrd | Byrd | −8 | Notable | 1.19% | 2,408 | 2,361 |
| Lazar | Halley | +1 | Significant | 4.81% | 58,246 | 56,261 |
| Santa Luce | Halley | −1 | Significant | 9.04% | 20,229 | 19,330 |
| Troll | Halley | 0 | Significant | 9.88% | 48,477 | 48,216 |
| Concordia | Janbogo | +8 | Primary | 9.20% | 48,123 | 47,572 |
| Casey | Mirny | +7 | Significant | 6.13% | 47,415 | 45,713 |
| Davis | Mirny | +5 | Significant | 5.64% | 34,206 | 32,472 |
| Mirny | Mirny | +6 | Significant | 7.22% | 50,379 | 48,987 |
| Relung Panen | Mirny | +7 | Significant | 12.60% | 62,318 | 60,138 |
| Shirayuki | Mirny | +5 | Significant | 8.61% | 47,651 | 45,716 |
| Sinheung | Mirny | +5 | Significant | 6.85% | 34,724 | 32,841 |
| Zhongshan | Mirny | +5 | Significant | 5.72% | 34,005 | 33,229 |
| Contrapunto | Palmer | −4 | Significant | 6.12% | 20,079 | 19,376 |
| Palmer City | Palmer | −4 | Notable | 1.20% | 2,009 | 1,997 |

## Unit RS1 · Data inventory and method (files first; web only to fill named gaps)
1. **The successor nations as the developer's files define them.** Start with `y-files/Map Files/Russia/PROGRESS TRACKER - Read This First.md`, then the folder it names as current (the latest numbered follow-up under `02 reorganization/`, its `README.md`, `CHANGES.md`, `subdivisions.csv`, `spheres.csv`), `03 official timeline years/` and `04 timeline staging/`, and the matching `x Full Earth/Russia/` copy. For each successor nation: name (and whether provisional), the subdivisions it holds, its capital if stated, **population from `subdivisions.csv` (cite file and row)**, its time-zone footprint, and the date or staging year at which it exists. If two copies of a file disagree, say which is newer and use the authoritative one; report the difference.
2. **What the First Interwar Period data states** (2083 to 2564; the folders `03 official timeline years` and `04 timeline staging` and any notes in them): populations, borders, unions, splits and economic facts for each successor over time. Quote only what is stated, with file and line; never extrapolate.
3. **The other Russia sources:** the novel repo's `worldbuilding/extractions/Russia - Federal Fractures and the Far Eastern Question (survey).md`, `Russia - Candidate Names for Countries A, C and D (research).md` and `worldbuilding/nations/russia-map-data/`; the GDD's `Post-War_Nations_Founder_Reference.md` (Cities folder) for how post-war nations are summarized there.
4. **The composition method to apply** (stated in the GDD's `Upper_Earth_Immigration_Composition.md`, "Methodology" and "HOW FACTOR 1 IS MEASURED"): effective pool = population × GDP per head with a Gini penalty; proximity = distance in solar UTC, taken as the minimum over the zones where a meaningful share of a nation's pool lives; large pools reach anywhere; a small pool qualifies for the Notable tier only if its distance is at most 3. Restate it plainly and list, **per successor nation, which inputs the developer's files give and which are NOT FOUND** (GDP per head and Gini by subdivision are not in the map files; say where real-world regional data could fill them, for example Russian regional gross product per head, and label any such fill DERIVED).
5. **A derivation procedure for RS2 to RS4** (method only, no results): how a city's Russia share divides among the successors, computed two ways: (a) by effective pool alone; (b) by effective pool restricted by the proximity window of that city. State every formula and which inputs each needs.
FINAL: the successor table, the First Interwar facts found, the method, the input gaps. No design, no ruling, no recommendation.

## Units RS2 to RS4 · the proportions
For each city assigned to your unit (read RS1's file first, in full; read the Santa Luce, Relung Panen and other cities' sections of the GDD composition file ONLY for the city's own tier table; do not compare cities):
1. **Which successors lie inside the city's proximity window** (by solar UTC and the footprint rule) and which are outside it.
2. **The division of the city's Russia share among the successors,** (a) by pool alone and (b) by pool within the window, as percentages that sum to 100% of the former Russia share, with every input, formula and source shown. **Real-world regional data** (population, regional gross product per head, income inequality) may fill the gaps RS1 listed: search for it, cite it, label it DERIVED, and note its date.
3. **The resulting draft counts** for the city (the former Russia robots and humans split by those percentages, integer counts that sum exactly to the original counts; show the rounding rule).
4. **The effective tier** each successor would hold in that city under the composition method's tier rule (informational; the tier assignments are not ruled).
5. **NOT FOUND and sensitivities:** which input, if changed, moves a proportion by more than five percentage points.
FINAL per unit: a table per city, the method used, the NOT FOUND list. **Draft arithmetic only: nothing here is a ruling and no specification file is touched.**

## Agent rules (full text as sent)
Research FULLY and by the book: there is no speed credit; a recalled fact is a guess; open and read primary files and pages rather than snippets; a wrong fact is worse than a missing one; mark every claim SOURCED (with file and line, or URL), UNVERIFIED, DERIVED or NOT FOUND; log exact search strings and dead ends. Create the output file FIRST with a PROGRESS block (one `- [ ] <n> <item>` line per item or per city, plus `- [ ] FINAL`); tick an item only when its section is fully written; if the file exists, resume. Names of successor nations are exactly as the developer's files give them; a provisional name is marked provisional. Never invent a border, a population or a name. American English. Do not edit any file but your own output file; do not commit; do not spawn sub-agents; scratch files in your scratchpad. If a search tool says the budget is used up or a search is refused, STOP: write a STOP note giving exactly where you stopped and do not work around it. Final reply under 300 words: boxes ticked, key findings, what is left.

---
## ➕ Added 2026-10-29 (coordinator, after RS1): the shared input step and the defaults for the open choices

**What RS1 found (`Russia_Split_Proportions_RS1_Inventory_and_Method_2026-10-29.md`):** the developer's Russia files give **no population, GRP or Gini for any successor**; the First Interwar folders (`03 official timeline years`, `04 timeline staging`) are **empty**, so *"based on the data for the First Interwar Period"* cannot be met from the files: **the First Interwar record does not exist yet** (the developer recorded it as a future folder). **Every number in this wave is therefore a present-day real-world regional figure aggregated to the successors' territories (DERIVED), standing in for the unwritten record, and each file must say so in its first lines.**

**New unit RS1b · the shared input table (runs before RS2 to RS4).** Output `Russia_Split_Proportions_RS1b_Input_Table_2026-10-29.md` plus the machine-readable `Russia_Split_Inputs_2026-10-29.csv` (this folder). For each source unit in RS1's successor table (the 83 pre-war federal subjects, Crimea and Sevastopol, and the six eastern-Ukraine units): population (one year for all, 2021 census where possible), GRP per head (one year for all, the latest year common to all), Gini (Rosstat's regional table if reachable; otherwise NOT FOUND with the fallback below), the solar zone where its people live (S7 rule below), and its recipient successor from `subdivisions.csv` (`09 follow-up`). Then, per successor: pool W, zone profile q(z), and the **city-independent split (a)** among successors under each variant. RS1 section 4.3 lists the sources to try (ru.wikipedia's regional-GRP list, Rosstat tables if reachable, the Ukrainian oblast data in `EUB`). Rosstat hosts fail certificate checks here: do not bypass.
RS2 to RS4 then **read RS1 and RS1b, and do only the city-specific work** (windows, split (b), counts, tiers, sensitivity).

**Coordinator defaults for RS1's open choices (NOT rulings; every result file states them and reports the alternatives as sensitivities):**
- **S1** primary variant **V1** (the 83 pre-war federal subjects, excluding Crimea, Sevastopol and the eastern-Ukraine units); report V1c and V2 beside it.
- **S2** primary **K-out** (Kaliningrad is not a Russia-split nation); report K-in.
- **S3** primary **INIT** (the only dated state: the start of 2083); report C-15.
- **S4** threshold θ = **10%**; sweep 5% and 25% (RS1 step 5).
- **S5** primary **solar zones** (the composition method's own rule); report official zones.
- **S6** **no wraparound** across the date line.
- **S7** assign each subject to the solar zone of its largest city; report the territory-centroid alternative for subjects that span zones.
- **Effective pool** *E = P × y × (1 − G)*; if Gini is missing for any unit use *E = P × y* for all units and say so.
