# Russia-split proportions · Unit RS4 · Byrd, Palmer City, Contrapunto (2026-10-29)

**Read this first.** The First Interwar Period record does not exist yet (the Russia `03 official timeline years` and `04 timeline staging` folders are empty; RS1 §2). Every figure in this file is a present-day real-world regional figure aggregated to the successor territories (**DERIVED**), standing in for that unwritten record. **Nothing here is a ruling or a recommendation**, and no spec, census or composition file is touched. Successor names are the developer's (`subdivisions.csv`, `09 follow-up`); **Idelsk-Uralia and Donska-Kubania are provisional** (conflicting sources, RS1 §1.2) and are marked "(prov.)" below.

**Brief:** `Research_Logs/Russia_Split_Proportions_Research_BRIEF_2026-10-29.md` (Units RS2 to RS4, and the coordinator's section with defaults S1 to S7). **Inputs used, not redone:** `Russia_Split_Proportions_RS1_Inventory_and_Method_2026-10-29.md` (method, §4 and §5), `Russia_Split_Proportions_RS1b_Input_Table_2026-10-29.md` (pools, zone profiles, split (a)) and `Russia_Split_Inputs_2026-10-29.csv` (91 source units). **Labels:** SOURCED · UNVERIFIED · DERIVED · NOT FOUND.

## PROGRESS
- [x] 1 Byrd
- [x] 2 Palmer City
- [x] 3 Contrapunto
- [x] FINAL

---

## 0 · Method as applied in this file (shared procedure; each city section below stands on its own)

**Coordinator defaults, applied as primary (NOT rulings):** S1 = **V1** (83 pre-war federal subjects) · S2 = **K-out** · S3 = **INIT** · S4 θ = **10%** · S5 = **solar zones** · S6 = **no wraparound** · S7 = **solar zone of each subject's largest city** · pool **E = P × y2024 × (1 − G2022)** (RS1b §0). Sensitivities reported: V1c, V2, K-in, C-15, θ 5% and 25%, official zones, territory-centroid zones, and (beyond the list) wraparound and any θ above zero.

**Composition method (SOURCED, `Upper_Earth_Immigration_Composition.md`, "Methodology" L7–17 and "HOW FACTOR 1 IS MEASURED" L21–63; explanatory L1093–1109):**
- City solar zone = round(longitude ÷ 15) (L28). Distance = |nation zone − city zone| (L29).
- **Clause N (small-pool Notable):** *"A small-pool nation qualifies for the Notable tier only if distance ≤ 3"* (L30–31).
- **Clause L (large pool):** *"Proximity is what gets a small nation into a city's composition at all; large pools reach anywhere"* (L31). **"Large" has no number in the file: NOT FOUND** (RS1 §4.1 item 4, §5 Step 7).
- **Clause G (gateway):** a nation routed through another's gateway takes the gateway's distance (L32–33). No file routes any Russian successor through a gateway: **NOT FOUND**, so not applied.
- **Footprint rule:** distance = the minimum over the zones where a meaningful share of the nation's pool lives (L43–44); Réunion at ~2.5% of France's pool is OUT (L53), so θ sits above 2.5%.
- **Tier rule:** all qualifying nations ranked by effective pool; tier breaks at the largest ratio gaps in that city's ranking (L17, L1107); 8 / 3 / 1 shares per T1 / T2 / T3 nation (L1109).

**Formulas (RS1 §5):**
- Split (a): *p_k = W_k ÷ Σ W_j*. City-independent; recomputed here from the CSV and identical to RS1b §7.1 to two decimals (raw output in 0.2).
- Split (b): *d_k = min over z ∈ Z_k(θ) of |z − z_c|*; *I_k = 1 if d_k ≤ 3*; *p_k^(b) = W_k I_k ÷ Σ W_j I_j*. **If every I_k = 0, (b) is undefined and RS1 §5 Step 4 says: report "no successor in window" and do not invent a fallback.**
- (b-sub): only source units with |z_s − z_c| ≤ 3 count.
- Counts: Hamilton (largest remainder): *n_k = floor(N p_k)*, the leftover units go one each to the largest fractional remainders, ties to the larger W_k (RS1 §5 Step 6).
- Effective pool for tiers: *Ê_k = 25M × p_k^(a)*, 25M being pre-war Russia's pool (`UEIC` L76).

**Tier placement convention used here (DERIVED; stated because the file's rule does not reproduce the cities' own tables).** The strict reading "the two largest ratio gaps are the two tier breaks" was run on each city's own nation list *before* any split, and it does **not** reproduce that city's own tier table in any of the three cases (raw output in each section). So each section reports three things: (i) the admission test (clauses N, L, G); (ii) the strict ratio-gap result, raw, for information; (iii) the tier rule the city's own section or spec actually states, where it states one.

**Real-world search.** None was run. Every gap RS1b lists (Ukrainian Gini, Donetsk/Luhansk GRP after 2013, Ingushetia 2022 GRP, left-bank Kherson population, Rosstat primaries, which Gini measure CEIC carries) changes only split (a), which RS1b already reports, and none can move any successor's zone into a window 5 or more zones away (0.3). The longitude look-ups for the out-of-window evidence in each section use the developer's own Natural Earth 1:10m populated places file (`/tmp/ne_test/ne_10m_populated_places_simple.geojson`, RS1 §1.3): **DERIVED**.

### 0.1 Pools and Ê (primary V1 · K-out · INIT; DERIVED from RS1b)

| Successor | W (tn RUB) | Split (a) | Ê = 25M × p (M) |
|---|--:|--:|--:|
| Russia | 47.726 | 41.83% | 10.458 |
| Idelsk-Uralia (prov.) | 26.704 | 23.41% | 5.852 |
| Siberia | 19.284 | 16.90% | 4.226 |
| Künnarantaiga | 9.402 | 8.24% | 2.060 |
| Donska-Kubania (prov.) | 8.125 | 7.12% | 1.780 |
| Karelia | 1.106 | 0.97% | 0.242 |
| Dagestan | 0.700 | 0.61% | 0.153 |
| Chechnya | 0.327 | 0.29% | 0.072 |
| Kabardino-Balkaria | 0.223 | 0.20% | 0.049 |
| North Ossetia-Alania | 0.213 | 0.19% | 0.047 |
| Karachay-Cherkessia | 0.111 | 0.10% | 0.024 |
| Tuva | 0.096 | 0.08% | 0.021 |
| Ingushetia | 0.072 | 0.06% | 0.016 |
| **Total** | 114.089 | 100% | 25.000 |

### 0.2 Raw output: split (a), every variant (recomputed; `step1.txt`)

```
variant|Russia|Idelsk-Uralia|Donska-Kubania|Künnarantaiga|Siberia|Tuva|Karelia|Chechnya|Dagestan|Ingushetia|Kabardino-Balkaria|Karachay-Cherkessia|North Ossetia-Alania|Kaliningrad (K-in)|Finland (Rep. of Karelia piece, C-15)
V1·K-out·INIT [primary]|41.83|23.41|7.12|8.24|16.90|0.08|0.97|0.29|0.61|0.06|0.20|0.10|0.19|—|—
V1·K-out·C-15 [primary]|41.83|24.09|7.12|8.24|16.90|0.08|—|0.29|0.61|0.06|0.20|0.10|0.19|—|0.29
V1·K-in·INIT [primary]|41.60|23.27|7.08|8.19|16.81|0.08|0.96|0.29|0.61|0.06|0.19|0.10|0.19|0.57|—
V1·K-in·C-15 [primary]|41.60|23.95|7.08|8.19|16.81|0.08|—|0.29|0.61|0.06|0.19|0.10|0.19|0.57|0.29
V1c·K-out·INIT [primary]|41.54|23.24|7.77|8.18|16.78|0.08|0.96|0.28|0.61|0.06|0.19|0.10|0.19|—|—
V1c·K-out·C-15 [primary]|41.54|23.92|7.77|8.18|16.78|0.08|—|0.28|0.61|0.06|0.19|0.10|0.19|—|0.29
V1c·K-in·INIT [primary]|41.31|23.11|7.73|8.14|16.69|0.08|0.96|0.28|0.61|0.06|0.19|0.10|0.18|0.56|—
V1c·K-in·C-15 [primary]|41.31|23.78|7.73|8.14|16.69|0.08|—|0.28|0.61|0.06|0.19|0.10|0.18|0.56|0.29
V2·K-out·INIT [y21]|45.53|21.36|7.12|7.38|16.06|0.07|1.18|0.21|0.61|0.06|0.16|0.08|0.15|—|—
V2·K-out·C-15 [y21]|45.53|22.20|7.12|7.38|16.06|0.07|—|0.21|0.61|0.06|0.16|0.08|0.15|—|0.34
V2·K-in·INIT [y21]|45.29|21.25|7.08|7.34|15.98|0.07|1.18|0.21|0.61|0.06|0.16|0.08|0.15|0.53|—
V2·K-in·C-15 [y21]|45.29|22.09|7.08|7.34|15.98|0.07|—|0.21|0.61|0.06|0.16|0.08|0.15|0.53|0.34
== formula forms (V1·K-out·INIT)
primary|41.83|23.41|7.12|8.24|16.90|0.08|0.97|0.29|0.61|0.06|0.20|0.10|0.19|—|—
noGini24|42.72|22.71|7.10|8.11|17.00|0.08|0.89|0.28|0.60|0.06|0.19|0.09|0.18|—|—
y22G|41.90|22.87|7.22|8.10|17.22|0.08|1.21|0.22|0.63|0.11|0.18|0.10|0.17|—|—
y22|42.80|22.18|7.20|7.98|17.31|0.08|1.10|0.22|0.61|0.10|0.17|0.09|0.16|—|—
y21G|42.61|23.09|6.84|7.86|16.77|0.08|1.36|0.23|0.66|0.06|0.18|0.10|0.17|—|—
y21|43.54|22.40|6.81|7.74|16.85|0.08|1.24|0.23|0.64|0.06|0.17|0.09|0.16|—|—
Ponly|31.36|30.90|11.95|7.20|12.47|0.23|0.84|1.05|2.21|0.35|0.63|0.33|0.48|—|—
```

Moves above 5 points against the primary row (DERIVED from the table above): **only the P-only form** (Russia −10.47, Idelsk-Uralia +7.49). Every scope variant and every income-weighted form stays within 5 points (the largest is V2's Russia, +3.70). The "y22" rows carry the faulty Ingushetia 2022 value RS1b §2.2 flags.

### 0.3 Why the window question has the same shape wherever the city sits west of about −4 (the successors' side only)

The successors' meaningful zones (RS1b §6.2–6.3) run from **+2** (Russia's St. Petersburg side, Karelia, Crimea under V1c) to **+10** (Künnarantaiga: Sakhalin and Magadan), with +11 and +12 entering only below θ = 25% under official zones. Kaliningrad (K-in) sits at **+1**. No successor has a meaningful zone at or west of 0. This is a fact about the successors, stated once; each city section applies it to its own zone.

---

## 1 · Byrd (solar UTC −8; Notable; former Russia share 1.19% = 2,408 robots / 2,361 humans, Census I)

**City zone.** Byrd Station ~119°31′W (SOURCED, `Specs/Byrd subnet/Byrd.md` L49) → −119.517 ÷ 15 = **−7.97 → −8** (DERIVED, `UEIC` L28 rule). **Window: −11 to −5.** Russia's row: Notable, 1.19%, 2,408 robots, 2,361 humans (SOURCED, spec L105; consistent with 1.19% × 202,399 = 2,408.5 and 1.19% × 198,406 = 2,361.0, spec L61, DERIVED).

### 1.1 Which successors lie inside Byrd's window

**None, under the primary or under any variant.** Primary (V1 · K-out · INIT, solar S7, θ = 10%); the wraparound column is the S6 sensitivity (circular distance on a 24-zone dial).

| Successor | Meaningful zones Z(10%) | q(z), solar S7 | d to −8 (no wrap) | d (wrap) | Ê (M) | Clause N (d ≤ 3) | Clause L (large pool) | Verdict |
|---|---|---|--:|--:|--:|---|---|---|
| Russia | +2, +3 | +2: 28.8% · +3: 71.2% | 10 | 10 | 10.458 | fails | see 1.1.1 | **outside** |
| Idelsk-Uralia (prov.) | +3, +4 | +3: 57.1% · +4: 42.9% | 11 | 11 | 5.852 | fails | see 1.1.1 | **outside** |
| Siberia | +5, +6 | +4: 7.1% · +5: 53.6% · +6: 39.3% | 13 | 10 | 4.226 | fails | see 1.1.1 | **outside** |
| Künnarantaiga | +7, +9, +10 | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | 15 | 6 | 2.060 | fails | see 1.1.1 | **outside** |
| Donska-Kubania (prov.) | +3 | +3: 100% | 11 | 11 | 1.780 | fails | see 1.1.1 | **outside** |
| Karelia | +2 | +2: 100% | 10 | 10 | 0.242 | fails | see 1.1.1 | **outside** |
| Dagestan, Chechnya, Kabardino-Balkaria, North Ossetia-Alania, Karachay-Cherkessia, Ingushetia | +3 | +3: 100% | 11 | 11 | 0.016–0.153 | fails | see 1.1.1 | **outside** |
| Tuva | +6 | +6: 100% | 14 | 10 | 0.021 | fails | see 1.1.1 | **outside** |
| Kaliningrad (K-in only; a CIN member, not a Russia-split nation) | +1 | +1: 100% | 9 | 9 | 0.14 (K-in) | fails | see 1.1.1 | **outside** |
| Finland, Republic of Karelia piece (C-15 only) | +2 | +2: 100% | 10 | 10 | 0.07 (C-15) | fails | see 1.1.1 | **outside** |

**The far eastern edge.** Byrd lies east of the date line and Künnarantaiga almost wholly west of it, so the eastern edge is the only part of the old Russia that comes near (and only once wraparound is allowed). Even with wraparound, Künnarantaiga's nearest meaningful zone is +10 (distance 6) at θ = 10%, and +12 (distance **4**) only under official zones at θ = 5% in V2. **The window excludes everything, the far eastern edge included.**

**Raw sweep output (`step2.txt`):**
```
######## Byrd (solar UTC -8); window = -11..-5
  b-sub units within window (primary): NONE
  SWEEP (V1/V1c/V2 x K-out/K-in x INIT/C-15 x solar/centroid/official x theta 5/10/25%/any>0 x wrap no/yes):
  any successor with d<=3: NONE
  minimum distance per successor over the sweep [no-wrap, theta>=5%] / [wrap, theta>=5%] / [wrap, theta any>0]:
   Russia: 10 / 10 / 10
   Idelsk-Uralia: 11 / 11 / 10
   Donska-Kubania: 10 / 10 / 10
   Künnarantaiga: 15 / 4 / 4
   Siberia: 12 / 9 / 9
   Tuva: 14 / 9 / 9
   Karelia: 10 / 10 / 10
   Chechnya: 11 / 11 / 11
   Dagestan: 11 / 11 / 11
   Ingushetia: 11 / 11 / 11
   Kabardino-Balkaria: 11 / 11 / 11
   Karachay-Cherkessia: 11 / 11 / 11
   North Ossetia-Alania: 11 / 11 / 11
   Kaliningrad (K-in): 9 / 9 / 9
   Finland (Rep. of Karelia piece, C-15): 10 / 10 / 10
```

**The one configuration that reaches the window (an edge case, shown honestly).** It needs two departures from the defaults at once: a footprint taken **town by town** instead of S7, and θ at or below about **0.09%**. Chukotka's towns east of 180° (Natural Earth, RS1 scratch `out/places_by_successor.csv`) include three at solar **−11**: Lavrentiya (171.02°W, pop_max 1,242), Uelen (169.81°W, 776) and Enurmino (171.82°W, 297). That is 2,315 of Chukotka's 34,905 NE pop_max (6.63%). Chukotka is 1.394% of Künnarantaiga's pool, so these towns are about **0.0925%** of it (DERIVED; raw: *"-11 town share of Künnarantaiga W if Chukotka's E is split by NE pop_max: 0.0925 %"*). Their distance to −8 is **3**, so under that configuration Künnarantaiga alone would enter, and **(b) would give Künnarantaiga 100% against 8.24% by (a), a gap of 91.76 points.** This configuration contradicts the method's own bound (θ above 2.5%, `UEIC` L53) by a factor of about 27, and NE pop_max is a town proxy, not a population count (RS1 §1.3). **It is reported, not used.**

#### 1.1.1 Clause L at Byrd: what Byrd's own table shows

- **In Byrd's window, by the capital or largest-city zone in NE (DERIVED):** USA (New York −5, Chicago −6, Los Angeles −8), Canada (Ottawa and Toronto −5, Vancouver −8), Mexico (Mexico City −7), Chile (Santiago −5). Byrd's spec lists **42 nations** (L64–68, L76–119), so **38 of them are outside its window.**
- Those 38 include pools far below every "large" reading. Latvia ~0.6M at +2 (distance 10), Uruguay ~0.6M at −4 (distance 4), Lithuania ~1M at +2 (distance 10), and Slovenia ~1M at +1 (distance 9) are all Notable at Byrd (spec L84–119; pools `UEIC` L65–110). **Byrd's own table therefore does not apply clause N to its Notable tier.** What basis admits them is **NOT FOUND**: Byrd has no city section in `UEIC` (only the subnet header, L381–387), and neither the spec (L59–70) nor the census table (`Official_Population_Census.md` L226–232) states one.
- **Consequence, stated both ways.** (i) **By the composition method strictly applied:** every successor is outside the window (clause N fails), and all are far smaller than the 25M pool that Byrd now lists at Notable. Byrd's own table gives no "large" cut, because it admits sub-1M pools at distance 10. So clause L can be neither confirmed nor ruled out from Byrd's material: **status undetermined (NOT FOUND).** (ii) **By what Byrd's own table does in practice:** pools as small as ~0.6M at distance 10 are admitted at Notable. Every successor down to Karelia (0.242M) is the same order of size or larger than the smallest of those, so on that practice they would not be excluded. The six North Caucasus republics and Tuva (0.016–0.153M) sit below anything Byrd now lists.

### 1.2 Division of Byrd's former Russia share

**(a) By pool alone (primary):** Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06% (sum 100%; inputs and formula in §0; source RS1b §6.1 and §7.1).

As shares of **Byrd's whole population** (1.19% × p_k; DERIVED): Russia 0.4978% · Idelsk-Uralia 0.2785% · Siberia 0.2011% · Künnarantaiga 0.0981% · Donska-Kubania 0.0847% · Karelia 0.0115% · Dagestan 0.0073% · Chechnya 0.0034% · Kabardino-Balkaria 0.0023% · North Ossetia-Alania 0.0022% · Karachay-Cherkessia 0.0012% · Tuva 0.0010% · Ingushetia 0.0007%.

**(b) By pool within Byrd's window: UNDEFINED. No successor in window** (every I_k = 0 under every variant in 1.1). **(b-sub): UNDEFINED.** No source unit has |z_s − (−8)| ≤ 3 (raw: *"b-sub units within window (primary): NONE"*). Per RS1 §5 Step 4, no fallback is invented. **So the former Russia share at Byrd can be divided only by (a), and (a) does not depend on where Byrd is.** Window (b) and pool (a) do not "differ" here; (b) simply does not exist. The one configuration that would define it is the edge case in 1.1, which gives 100% Künnarantaiga.

### 1.3 Draft counts (split (a), primary; Hamilton / largest remainder, ties to the larger W)

**Robots, N = 2,408.** The floors sum to 2,402, leaving **6** units; they go to the six largest remainders: Chechnya .905, Dagestan .766, Kabardino-Balkaria .697, Idelsk-Uralia .620, Ingushetia .516, North Ossetia-Alania .498. Next in line and left out: Donska-Kubania .493 and Künnarantaiga .436.
**Humans, N = 2,361.** The floors sum to 2,354, leaving **7** units: Tuva .994, Karelia .893, Chechnya .770, Russia .670, Idelsk-Uralia .619, Kabardino-Balkaria .605, Künnarantaiga .563. Next and left out: Ingushetia .486 and Dagestan .478.

| Successor | p_k | Robots N·p | floor | +1 | **Robots** | Humans N·p | floor | +1 | **Humans** |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.8327% | 1007.3312 | 1007 | 0 | **1,007** | 987.6698 | 987 | 1 | **988** |
| Idelsk-Uralia (prov.) | 23.4062% | 563.6203 | 563 | 1 | **564** | 552.6194 | 552 | 1 | **553** |
| Siberia | 16.9023% | 407.0076 | 407 | 0 | **407** | 399.0636 | 399 | 0 | **399** |
| Künnarantaiga | 8.2407% | 198.4359 | 198 | 0 | **198** | 194.5628 | 194 | 1 | **195** |
| Donska-Kubania (prov.) | 7.1218% | 171.4934 | 171 | 0 | **171** | 168.1462 | 168 | 0 | **168** |
| Karelia | 0.9696% | 23.3483 | 23 | 0 | **23** | 22.8926 | 22 | 1 | **23** |
| Dagestan | 0.6132% | 14.7659 | 14 | 1 | **15** | 14.4777 | 14 | 0 | **14** |
| Chechnya | 0.2868% | 6.9050 | 6 | 1 | **7** | 6.7702 | 6 | 1 | **7** |
| Kabardino-Balkaria | 0.1950% | 4.6968 | 4 | 1 | **5** | 4.6051 | 4 | 1 | **5** |
| North Ossetia-Alania | 0.1868% | 4.4976 | 4 | 1 | **5** | 4.4098 | 4 | 0 | **4** |
| Karachay-Cherkessia | 0.0975% | 2.3483 | 2 | 0 | **2** | 2.3025 | 2 | 0 | **2** |
| Tuva | 0.0845% | 2.0339 | 2 | 0 | **2** | 1.9942 | 1 | 1 | **2** |
| Ingushetia | 0.0629% | 1.5158 | 1 | 1 | **2** | 1.4862 | 1 | 0 | **1** |
| **Total** | 100% | 2408 | 2402 | 6 | **2,408** | 2361 | 2354 | 7 | **2,361** |

**No (b) counts exist** (1.2). Sensitivity, the P-only form (the only form that moves a share more than 5 points), robots / humans: Russia 755 / 740 · Idelsk-Uralia 744 / 730 · Siberia 300 / 294 · Donska-Kubania 288 / 282 · Künnarantaiga 173 / 170 · Dagestan 53 / 52 · Chechnya 25 / 25 · Karelia 20 / 20 · Kabardino-Balkaria 15 / 15 · North Ossetia-Alania 12 / 11 · Ingushetia 9 / 8 · Karachay-Cherkessia 8 / 8 · Tuva 6 / 6 (same rounding rule).

### 1.4 Effective tier at Byrd (informational; nothing is ruled)

- **Under the composition method's admission test: no successor is admitted.** Clause N fails for all (d ≥ 10, or ≥ 4 with wraparound). Clause L is undetermined for all (1.1.1). Clause G is not applicable. **Effective tier: none (outside the window; large-pool status NOT FOUND).**
- **Under the tier rule Byrd's own spec states** (*"Tiers reassigned to match the new ranking by share size — top 2 Primary, next 4 Significant, remainder Notable"*, spec L74): every successor's share is a part of 1.19%, at most 0.4978% (Russia). All of them fall in the remainder: **Notable, if admitted.**
- **Under the strict ratio-gap reading of `UEIC` L17** (raw, `step3.txt`), with Byrd's 42 pools from `UEIC` L65–110 and Russia replaced by the 13 successors' Ê. Pre-split, the two largest gaps fall at USA→Japan (2.385) and Slovenia→Latvia (1.667). That gives T1 China and USA, T3 Latvia and Uruguay, and T2 for everything else, **which does not reproduce Byrd's own table** (USA and Canada Primary). Post-split the breaks fall at USA→Japan (2.385) and **Uruguay→Karelia (2.475)**. That would put Russia, Idelsk-Uralia, Siberia, Künnarantaiga and Donska-Kubania in T2, and Karelia, the six North Caucasus republics and Tuva in T3. Given that the reading fails on Byrd's own pre-split table, **this is recorded and not relied on.**
```
 PRE-SPLIT breaks at: [('USA', 'Japan', 2.385), ('Slovenia', 'Latvia', 1.667)]
 POST-SPLIT breaks at: [('USA', 'Japan', 2.385), ('Uruguay', 'Karelia', 2.475)]
 POST-SPLIT tiers of successors: {'Russia': 2, 'Idelsk-Uralia': 2, 'Donska-Kubania': 2, 'Künnarantaiga': 2, 'Siberia': 2, 'Tuva': 3, 'Karelia': 3, 'Chechnya': 3, 'Dagestan': 3, 'Ingushetia': 3, 'Kabardino-Balkaria': 3, 'Karachay-Cherkessia': 3, 'North Ossetia-Alania': 3}
  Russia 10.458M rank 16/54; above: Poland 12.000 (ratio 1.15); below: Netherlands 10.000
  Idelsk-Uralia 5.852M rank 22/54; above: Sweden 6.000 (ratio 1.03); below: Philippines 5.000
  Siberia 4.226M rank 29/54; above: Romania 4.500 (ratio 1.06); below: Finland 3.300
  Künnarantaiga 2.060M rank 37/54; above: Slovakia 2.200 (ratio 1.07); below: Donska-Kubania 1.780
  Donska-Kubania 1.780M rank 38/54; above: Künnarantaiga 2.060 (ratio 1.16); below: Belarus 1.500
  Karelia 0.242M rank 47/54; above: Uruguay 0.600 (ratio 2.48); below: Dagestan 0.153
```

### 1.5 NOT FOUND and sensitivities at Byrd

**NOT FOUND:** a number for "large pool" (clause L); the basis on which Byrd's table admits its 38 out-of-window nations; any gateway routing for a Russian successor (clause G); every First Interwar figure (all inputs are present-day stand-ins).

**Sensitivities (each against the primary):**

| Input changed | Effect on window membership | Effect on split (a) | > 5 points? |
|---|---|---|---|
| V1c (Crimea and Sevastopol in) | none (Crimea +2: d 10) | Donska-Kubania +0.65 | no |
| V2 (eastern-Ukraine slice in; E = P × y2021) | none | Russia +3.70, Idelsk-Uralia −2.05 | no |
| K-in (Kaliningrad its own row) | none (+1: d 9) | Kaliningrad 0.57; others pro rata | no |
| C-15 (Rep. of Karelia → Finland; Murmansk → Idelsk-Uralia) | none (Finland piece +2: d 10) | Idelsk-Uralia +0.68; Finland piece 0.29; Karelia 0 | no |
| θ = 5% | none (Künnarantaiga gains +8: d 16, or 8 with wrap) | — | no |
| θ = 25% | none | — | no |
| Official zones | none (nearest without wrap: +2 units, d 10; with wrap: Künnarantaiga +11, d 5, and +12 at θ 5% in V2, d 4) | — | no |
| Territory-centroid zones | none | — | no |
| Wraparound (S6 alternative) | none at θ ≥ 5% (closest d = 4) | — | no |
| Town-level footprint **and** θ ≤ 0.09% (edge case, 1.1) | **Künnarantaiga enters (d 3)** | (b) would become 100% Künnarantaiga | **yes, +91.76 for Künnarantaiga under (b)** |
| Pool formula P only | none | **Russia −10.47; Idelsk-Uralia +7.49**; Donska-Kubania +4.83; Siberia −4.43 | **yes (Russia, Idelsk-Uralia)** |
| Any other income-weighted form (no Gini; 2022; 2021) | none | at most Russia +1.71 (y2021, no Gini) | no |
| Moscow, Amur or Sakhalin knife-edge zones (RS1b §4) | none (all far outside −11…−5) | — | no |

---

## 2 · Palmer City (solar UTC −4; Notable; former Russia share 1.20% = 2,009 robots / 1,997 humans, Census I)

**City zone.** Anvers Island, ~64°03′W (SOURCED, `UEIC` L151) → −64.05 ÷ 15 = **−4.27 → −4** (DERIVED). **Window: −7 to −1.** Russia's row: Notable, 1.20%, 2,009 robots, 1,997 humans, Census I (SOURCED, `Specs/Palmer subnet/Palmer_City.md` L92). The Census II figures on the same row (1,381 / 1,647) are outside this brief and are not split here.

**How Russia came to be in Palmer City's table (SOURCED, read before anything else because it decides which rule applies).** Russia is one of the **33 nations added on 2026-07-03**, so that *"every one of the 43 nations in the master Gini-adjusted effective exiles list … now has at least a Notable-tier presence here"*. They were *"assigned population shares via an explicit random-percentage method (0.2%–1.8% of Palmer City's pre-expansion total each), not the standard Gini-weight methodology"* (`UEIC` L153; the list at L160; the spec's own tier table at L64). **So Russia's place in Palmer City rests on that expansion rule, not on the window or large-pool clauses.** Both are reported below.

### 2.1 Which successors lie inside Palmer City's window

**None, under the primary or under any variant.** Primary (V1 · K-out · INIT, solar S7, θ = 10%); the wraparound column is the S6 sensitivity.

| Successor | Meaningful zones Z(10%) | q(z), solar S7 | d to −4 (no wrap) | d (wrap) | Ê (M) | Clause N (d ≤ 3) | Clause L (large pool) | Verdict under the composition method |
|---|---|---|--:|--:|--:|---|---|---|
| Russia | +2, +3 | +2: 28.8% · +3: 71.2% | 6 | 6 | 10.458 | fails | fails (2.1.1) | **outside; not admitted** |
| Idelsk-Uralia (prov.) | +3, +4 | +3: 57.1% · +4: 42.9% | 7 | 7 | 5.852 | fails | fails | **outside; not admitted** |
| Siberia | +5, +6 | +4: 7.1% · +5: 53.6% · +6: 39.3% | 9 | 9 | 4.226 | fails | fails | **outside; not admitted** |
| Künnarantaiga | +7, +9, +10 | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | 11 | 10 | 2.060 | fails | fails | **outside; not admitted** |
| Donska-Kubania (prov.) | +3 | +3: 100% | 7 | 7 | 1.780 | fails | fails | **outside; not admitted** |
| Karelia | +2 | +2: 100% | 6 | 6 | 0.242 | fails | fails | **outside; not admitted** |
| Dagestan, Chechnya, Kabardino-Balkaria, North Ossetia-Alania, Karachay-Cherkessia, Ingushetia | +3 | +3: 100% | 7 | 7 | 0.016–0.153 | fails | fails | **outside; not admitted** |
| Tuva | +6 | +6: 100% | 10 | 10 | 0.021 | fails | fails | **outside; not admitted** |
| Kaliningrad (K-in only; a CIN member) | +1 | +1: 100% | 5 | 5 | 0.14 (K-in) | fails | fails | **outside; not admitted** |
| Finland, Republic of Karelia piece (C-15 only) | +2 | +2: 100% | 6 | 6 | 0.07 (C-15) | fails | n/a (Finland is its own master-list row) | **outside** |

**The far eastern edge does not come near Palmer City.** Künnarantaiga's nearest meaningful zone is +7 (distance 11), or +10 with wraparound (distance 10). Even its Chukotka towns at −11 and −12 (Natural Earth) are 7 and 8 zones away. **The nearest point of any successor, town by town, is +2 (distance 6); the nearest pre-war Russian territory of any kind is Kaliningrad at +1 (distance 5).** The window excludes everything.

**Raw sweep output (`step2.txt`):**
```
######## Palmer City (solar UTC -4); window = -7..-1
  b-sub units within window (primary): NONE
  SWEEP (V1/V1c/V2 x K-out/K-in x INIT/C-15 x solar/centroid/official x theta 5/10/25%/any>0 x wrap no/yes):
  any successor with d<=3: NONE
  minimum distance per successor over the sweep [no-wrap, theta>=5%] / [wrap, theta>=5%] / [wrap, theta any>0]:
   Russia: 6 / 6 / 6
   Idelsk-Uralia: 7 / 7 / 6
   Donska-Kubania: 6 / 6 / 6
   Künnarantaiga: 11 / 8 / 8
   Siberia: 8 / 8 / 8
   Tuva: 10 / 10 / 10
   Karelia: 6 / 6 / 6
   Chechnya: 7 / 7 / 7
   Dagestan: 7 / 7 / 7
   Ingushetia: 7 / 7 / 7
   Kabardino-Balkaria: 7 / 7 / 7
   Karachay-Cherkessia: 7 / 7 / 7
   North Ossetia-Alania: 7 / 7 / 7
   Kaliningrad (K-in): 5 / 5 / 5
   Finland (Rep. of Karelia piece, C-15): 6 / 6 / 6
```
Town-level check (Natural Earth places, all successors and Kaliningrad): *"-4 closest NE place (no wrap): Kaliningrad (not in package) Kaliningrad 1 5"*. Excluding Kaliningrad, no successor has any town at a zone below +2.

#### 2.1.1 Clause L at Palmer City: what Palmer City's own table shows

- **In the window, by the capital or largest-city zone in NE (DERIVED):** USA (New York −5, Chicago and Houston −6), Canada (Ottawa and Toronto −5), Mexico (−7), Brazil (Rio de Janeiro −3, Manaus −4), Argentina (Buenos Aires −4), Chile (Santiago −5), Uruguay (Montevideo −4).
- **The ten nations placed by the standard method** (`UEIC` L155–159; spec L60–64, before the expansion rows) admit three pools from outside the window: **Germany ~46M** (Berlin +1, distance 5), **France ~35M** (Paris 0, distance 4) and **UK ~32M** (London 0, distance 4). The standard method did **not** admit Italy ~27M (+1, distance 5), South Korea ~26M (+8), **Russia ~25M** (+2/+3, distance 6), Spain ~20M (0, distance 4) or anything smaller. All of these entered only through the 2026-07-03 expansion. Japan ~65M and China ~210M were also left out before the expansion. That does not fit any single pool cut, and the city's section gives no reason: **NOT FOUND.**
- **So the standard method's own large-pool cut at Palmer City lies between about 27M and 32M** for the European pools (DERIVED from the table, not stated in it). **Every successor, at most 10.458M, fails clause L by that evidence**, as Russia's own 25M already did before the expansion.
- **Under the expansion rule:** the rule names *"the 43 nations in the master … list"* (`UEIC` L153). The successors are not on that list; the list is pre-war by `DR-23` (RS1 §2). **Whether that rule would extend to the successors after a split is not stated anywhere: NOT FOUND.** It is a design question, and nothing here answers it. Under the expansion, each nation was given its own random draw. A split divides Russia's single draw; the rule does not say how to handle a later split of one of its nations: **NOT FOUND.**

### 2.2 Division of Palmer City's former Russia share

**(a) By pool alone (primary):** Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06% (sum 100%; §0; RS1b §6.1, §7.1).

As shares of **Palmer City's whole population** (1.20% × p_k; DERIVED): Russia 0.5020% · Idelsk-Uralia 0.2809% · Siberia 0.2028% · Künnarantaiga 0.0989% · Donska-Kubania 0.0855% · Karelia 0.0116% · Dagestan 0.0074% · Chechnya 0.0034% · Kabardino-Balkaria 0.0023% · North Ossetia-Alania 0.0022% · Karachay-Cherkessia 0.0012% · Tuva 0.0010% · Ingushetia 0.0008%.

**(b) By pool within Palmer City's window: UNDEFINED. No successor in window** under any variant, at any θ, with or without wraparound, and even town by town (2.1). **(b-sub): UNDEFINED** (no source unit within ±3 of −4). No fallback is invented (RS1 §5 Step 4). **The former Russia share at Palmer City can be divided only by (a).** (a) is the same for any city, because it carries no proximity term.

### 2.3 Draft counts (split (a), primary; Hamilton / largest remainder, ties to the larger W)

The counts are small, so every step is shown. **Robots, N = 2,009.** The floors sum to **2,002**, leaving **7** units. They go, one each, to the seven largest fractional remainders: Karachay-Cherkessia .9592, Kabardino-Balkaria .9185, Chechnya .7609, North Ossetia-Alania .7523, Tuva .6969, Siberia .5674, Künnarantaiga .5555. The first two left out are Karelia .4796 and Russia .4187.
**Humans, N = 1,997.** The floors sum to **1,990**, leaving **7** units: Karachay-Cherkessia .9475, Kabardino-Balkaria .8951, North Ossetia-Alania .7299, Chechnya .7264, Tuva .6867, Künnarantaiga .5667, Siberia .5391. The first two left out are Idelsk-Uralia .4210 and Russia .3988. There are no exact ties, so the tie rule is not invoked.

| Successor | p_k | Robots N·p | floor | +1 | **Robots** | Humans N·p | floor | +1 | **Humans** |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.8327% | 840.4187 | 840 | 0 | **840** | 835.3988 | 835 | 0 | **835** |
| Idelsk-Uralia (prov.) | 23.4062% | 470.2297 | 470 | 0 | **470** | 467.4210 | 467 | 0 | **467** |
| Siberia | 16.9023% | 339.5674 | 339 | 1 | **340** | 337.5391 | 337 | 1 | **338** |
| Künnarantaiga | 8.2407% | 165.5555 | 165 | 1 | **166** | 164.5667 | 164 | 1 | **165** |
| Donska-Kubania (prov.) | 7.1218% | 143.0774 | 143 | 0 | **143** | 142.2228 | 142 | 0 | **142** |
| Karelia | 0.9696% | 19.4796 | 19 | 0 | **19** | 19.3632 | 19 | 0 | **19** |
| Dagestan | 0.6132% | 12.3192 | 12 | 0 | **12** | 12.2456 | 12 | 0 | **12** |
| Chechnya | 0.2868% | 5.7609 | 5 | 1 | **6** | 5.7264 | 5 | 1 | **6** |
| Kabardino-Balkaria | 0.1950% | 3.9185 | 3 | 1 | **4** | 3.8951 | 3 | 1 | **4** |
| North Ossetia-Alania | 0.1868% | 3.7523 | 3 | 1 | **4** | 3.7299 | 3 | 1 | **4** |
| Karachay-Cherkessia | 0.0975% | 1.9592 | 1 | 1 | **2** | 1.9475 | 1 | 1 | **2** |
| Tuva | 0.0845% | 1.6969 | 1 | 1 | **2** | 1.6867 | 1 | 1 | **2** |
| Ingushetia | 0.0629% | 1.2646 | 1 | 0 | **1** | 1.2571 | 1 | 0 | **1** |
| **Total** | 100% | 2009 | 2002 | 7 | **2,009** | 1997 | 1990 | 7 | **1,997** |

**Rounding effects at this scale (DERIVED).** Every successor gets at least 1 robot and 1 human. The relative rounding error is largest for the smallest pieces: Ingushetia 1.26 → 1 (−21%), Tuva 1.70 → 2 (+18%), Karachay-Cherkessia 1.96 → 2 (+2%). For the five largest successors it is under 0.3%. With seven leftover units on each side and twelve or more candidates, the remainders, not the shares, decide the bottom of the table. **No (b) counts exist** (2.2). Sensitivity, the P-only form, robots / humans: Russia 630 / 626 · Idelsk-Uralia 621 / 617 · Siberia 250 / 249 · Donska-Kubania 240 / 239 · Künnarantaiga 145 / 144 · Dagestan 44 / 44 · Chechnya 21 / 21 · Karelia 17 / 17 · Kabardino-Balkaria 13 / 13 · North Ossetia-Alania 10 / 9 · Ingushetia 7 / 7 · Karachay-Cherkessia 6 / 6 · Tuva 5 / 5 (same rounding rule).

### 2.4 Effective tier at Palmer City (informational; nothing is ruled)

- **Under the composition method's admission test: no successor is admitted** (clause N fails, d ≥ 6; clause L fails against the city's own 27–32M evidence; clause G not applicable). **Effective tier: none.**
- **Under the 2026-07-03 expansion rule, if it were carried over to the successors (an open question, 2.1.1):** all 33 expansion nations sit at **Notable** regardless of pool, Japan's ~65M included (`UEIC` L160; spec L64). On that rule, any successor present would be **Notable**.
- **If the standard method's band edges at Palmer City were used** (T2 floor Brazil ~17M, T3 ceiling Argentina ~6M, `UEIC` L158–159), with the T2/T3 break re-placed at the largest ratio between those two once successors are inserted (§0 convention): Russia's Ê of 10.458M splits that gap into 17 ÷ 10.458 = **1.626** and 10.458 ÷ 6 = **1.743**. The larger ratio is below Russia, so **Russia would sit on the Significant side**, and every other successor (5.852M and below) on the Notable side. Under V2 (Ê 11.384M: 1.493 against 1.897) and K-in (10.399M: 1.635 against 1.733) this holds. **Under the P-only form it flips:** Russia 7.840M and Idelsk-Uralia 7.724M give ratios 2.168, 1.015, 1.287, the break stays directly under Brazil, and **both are Notable.** This applies only if a successor were admitted by the standard method, which by 2.1.1 none is.
```
V1·K-out·INIT [primary] … between Brazil 17M and Argentina 6M: [('Brazil', 'Russia', 1.626), ('Russia', 'Argentina', 1.743)] -> break after Russia ; T2-side successors: ['Russia']
V2·K-out·INIT [y21]     … [('Brazil', 'Russia', 1.493), ('Russia', 'Argentina', 1.897)] -> break after Russia ; T2-side successors: ['Russia']
V1·K-in·INIT [primary]  … [('Brazil', 'Russia', 1.635), ('Russia', 'Argentina', 1.733)] -> break after Russia ; T2-side successors: ['Russia']
V1·K-out·INIT [Ponly]   … [('Brazil', 'Russia', 2.168), ('Russia', 'Idelsk-Uralia', 1.015), ('Idelsk-Uralia', 'Argentina', 1.287)] -> break after Brazil ; T2-side successors: []
```
- **The strict ratio-gap reading** over all 43 pools (raw, `step3.txt`): pre-split, the two largest gaps fall at USA→Japan (2.385) and Slovenia→Uruguay (1.667). That gives T1 China and USA, **which does not reproduce Palmer City's own table** (USA sole Primary). Post-split: USA→Japan and Estonia→Karelia (2.475), so Russia, Idelsk-Uralia, Siberia, Künnarantaiga and Donska-Kubania would be T2 and the rest T3. **Recorded, not relied on.**
```
 PRE-SPLIT breaks at: [('USA', 'Japan', 2.385), ('Slovenia', 'Uruguay', 1.667)]
 POST-SPLIT breaks at: [('USA', 'Japan', 2.385), ('Estonia', 'Karelia', 2.475)]
  Russia 10.458M rank 16/55; above: Poland 12.000 (ratio 1.15); below: Netherlands 10.000
  Idelsk-Uralia 5.852M rank 22/55; above: Argentina 6.000 (ratio 1.03); below: Czech Republic 5.000
  Siberia 4.226M rank 29/55; above: Romania 4.500 (ratio 1.06); below: Norway 3.300
  Künnarantaiga 2.060M rank 37/55; above: Slovakia 2.200 (ratio 1.07); below: Donska-Kubania 1.780
  Donska-Kubania 1.780M rank 38/55; above: Künnarantaiga 2.060 (ratio 1.16); below: Belarus 1.500
  Karelia 0.242M rank 48/55; above: Estonia 0.600 (ratio 2.48); below: Dagestan 0.153
```
- **C-15 note:** under C-15, the Republic of Karelia's piece (0.29% of the former Russia share) would go to Finland, which already has its own Notable row at Palmer City (spec L117). Whether it would merge into that row is not stated: **NOT FOUND.**

### 2.5 NOT FOUND and sensitivities at Palmer City

**NOT FOUND:** a number for "large pool"; why Japan and China were not admitted before the expansion; whether the 2026-07-03 expansion rule extends to successor nations, and how it treats a later split of one of its draws; gateway routing for any successor; every First Interwar figure.

| Input changed | Effect on window membership | Effect on split (a) | Effect on tier band (2.4, if admitted) | > 5 points? |
|---|---|---|---|---|
| V1c | none (Crimea +2: d 6) | Donska-Kubania +0.65 | none | no |
| V2 | none (Ukrainian units +2/+3: d ≥ 6) | Russia +3.70, Idelsk-Uralia −2.05 | none | no |
| K-in | none (Kaliningrad +1: d 5) | Kaliningrad 0.57; others pro rata | none | no |
| C-15 | none (Finland piece +2: d 6) | Idelsk-Uralia +0.68; Finland piece 0.29 | see 2.4 C-15 note | no |
| θ = 5% / 25% | none (at 5%, Siberia gains +4: d 8) | — | — | no |
| Official zones | none (nearest +2, d 6) | — | — | no |
| Territory-centroid zones | none | — | — | no |
| Wraparound | none (closest d 6; Künnarantaiga 8) | — | — | no |
| Town-level footprint, any θ | none (nearest successor town +2, d 6) | — | — | no |
| Pool formula P only | none | **Russia −10.47; Idelsk-Uralia +7.49**; Donska-Kubania +4.83; Siberia −4.43 | Russia moves from the Significant side to Notable | **yes (Russia, Idelsk-Uralia)** |
| Other income-weighted forms | none | at most Russia +1.71 | none | no |
| Moscow, Amur or Sakhalin knife-edge zones | none | — | — | no |

---

## 3 · Contrapunto (solar UTC −4; Significant; former Russia share 6.12% = 20,079 robots / 19,376 humans, Census I)

**City zone.** King George Island, ~58°47′W (SOURCED, `UEIC` L222; `Specs/Palmer subnet/Contrapunto.md` L5) → −58.783 ÷ 15 = **−3.92 → −4** (DERIVED). **Window: −7 to −1.** Russia's row: Significant, 6.12%, 20,079 robots, 19,376 humans, Census I (SOURCED, spec L57). The spec notes that its row sums may be off by a handful from the census totals (L63), so the brief's counts are used as given.

**How Russia is admitted at Contrapunto (SOURCED).** It is Significant among *"Large effective pools 17–46M; South Korea and Russia sit at Significant — Gini-adjusted composite places them behind the larger European/Mexican pools"* (`UEIC` L227). Russia is at least 6 zones from −4 (0.3), so **its admission rests on clause L ("large pools reach anywhere"), with Russia counted as one ~25M pool.**

### 3.1 Which successors lie inside Contrapunto's window

**None, under the primary or under any variant.** Primary (V1 · K-out · INIT, solar S7, θ = 10%); the wraparound column is the S6 sensitivity.

| Successor | Meaningful zones Z(10%) | q(z), solar S7 | d to −4 (no wrap) | d (wrap) | Ê (M) | Clause N (d ≤ 3) | Clause L (large pool) | Verdict under the composition method |
|---|---|---|--:|--:|--:|---|---|---|
| Russia | +2, +3 | +2: 28.8% · +3: 71.2% | 6 | 6 | 10.458 | fails | fails (3.1.1) | **outside; not admitted** |
| Idelsk-Uralia (prov.) | +3, +4 | +3: 57.1% · +4: 42.9% | 7 | 7 | 5.852 | fails | fails | **outside; not admitted** |
| Siberia | +5, +6 | +4: 7.1% · +5: 53.6% · +6: 39.3% | 9 | 9 | 4.226 | fails | fails | **outside; not admitted** |
| Künnarantaiga | +7, +9, +10 | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | 11 | 10 | 2.060 | fails | fails | **outside; not admitted** |
| Donska-Kubania (prov.) | +3 | +3: 100% | 7 | 7 | 1.780 | fails | fails | **outside; not admitted** |
| Karelia | +2 | +2: 100% | 6 | 6 | 0.242 | fails | fails | **outside; not admitted** |
| Dagestan, Chechnya, Kabardino-Balkaria, North Ossetia-Alania, Karachay-Cherkessia, Ingushetia | +3 | +3: 100% | 7 | 7 | 0.016–0.153 | fails | fails | **outside; not admitted** |
| Tuva | +6 | +6: 100% | 10 | 10 | 0.021 | fails | fails | **outside; not admitted** |
| Kaliningrad (K-in only; a CIN member) | +1 | +1: 100% | 5 | 5 | 0.14 (K-in) | fails | fails | **outside; not admitted** |
| Finland, Republic of Karelia piece (C-15 only) | +2 | +2: 100% | 6 | 6 | 0.07 (C-15) | fails | Finland not in Contrapunto's table | **outside** |

**The far eastern edge does not come near Contrapunto.** Künnarantaiga's nearest meaningful zone is +7 (distance 11), or +10 with wraparound (distance 10). Its Chukotka towns at −11 and −12 are 7 and 8 zones away. **The nearest successor town is at +2 (distance 6); Kaliningrad, at +1 (distance 5), is the nearest pre-war Russian territory.** The window excludes everything.

**Raw sweep output (`step2.txt`):**
```
######## Contrapunto (solar UTC -4); window = -7..-1
  b-sub units within window (primary): NONE
  SWEEP (V1/V1c/V2 x K-out/K-in x INIT/C-15 x solar/centroid/official x theta 5/10/25%/any>0 x wrap no/yes):
  any successor with d<=3: NONE
  minimum distance per successor over the sweep [no-wrap, theta>=5%] / [wrap, theta>=5%] / [wrap, theta any>0]:
   Russia: 6 / 6 / 6
   Idelsk-Uralia: 7 / 7 / 6
   Donska-Kubania: 6 / 6 / 6
   Künnarantaiga: 11 / 8 / 8
   Siberia: 8 / 8 / 8
   Tuva: 10 / 10 / 10
   Karelia: 6 / 6 / 6
   Chechnya: 7 / 7 / 7
   Dagestan: 7 / 7 / 7
   Ingushetia: 7 / 7 / 7
   Kabardino-Balkaria: 7 / 7 / 7
   Karachay-Cherkessia: 7 / 7 / 7
   North Ossetia-Alania: 7 / 7 / 7
   Kaliningrad (K-in): 5 / 5 / 5
   Finland (Rep. of Karelia piece, C-15): 6 / 6 / 6
```

#### 3.1.1 Clause L at Contrapunto: what Contrapunto's own table shows

- **In the window, by the capital or largest-city zone in NE (DERIVED):** USA (−5/−6), Mexico (−7), Brazil (−3/−4), Argentina (−4), Chile (−5), Uruguay (−4).
- **Admitted from outside the window** (spec L36–40, L50–58; pools `UEIC` L65–110): Germany ~46M (+1, distance 5), France ~35M (0, distance 4), UK ~32M (0, distance 4), Italy ~27M (+1, distance 5), South Korea ~26M (+8, distance 12) and **Russia ~25M** (+2/+3, distance 6). **The smallest of these is Russia's own 25M.**
- **Not admitted from outside the window:** Spain ~20M (0, distance 4), Poland ~12M, the Netherlands ~10M and all smaller European pools; also Japan ~65M (+9) and China ~210M (+8), which the spec removed on 2026-07-13 (L46). The reason for China's removal and Japan's absence is not given in the city's section: **NOT FOUND.**
- **So the table's own clause-L cut for the European pools lies between about 20M (Spain, out) and 25M (Russia, in)** (DERIVED from the table, not stated in it). **Every successor, at most 10.458M, falls below it.**
- **Consequence, stated flatly (not a recommendation).** Russia stands in Contrapunto's table as one large pool reaching from 6 zones away. Once split, **no successor meets clause L or clause N on the city's own evidence.** Under the composition method strictly applied, the 6.12% would have no admitting clause for any successor. The task's division by (a) below therefore divides the existing count as the brief asks. It is not a finding that the method would still place these people at Contrapunto. Whether the share stays, as one inherited block or otherwise, is a later decision this unit does not make.

### 3.2 Division of Contrapunto's former Russia share

**(a) By pool alone (primary):** Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06% (sum 100%; §0; RS1b §6.1, §7.1).

As shares of **Contrapunto's whole population** (6.12% × p_k; DERIVED): Russia 2.5602% · Idelsk-Uralia 1.4325% · Siberia 1.0344% · Künnarantaiga 0.5043% · Donska-Kubania 0.4359% · Karelia 0.0593% · Dagestan 0.0375% · Chechnya 0.0175% · Kabardino-Balkaria 0.0119% · North Ossetia-Alania 0.0114% · Karachay-Cherkessia 0.0060% · Tuva 0.0052% · Ingushetia 0.0039%.

**(b) By pool within Contrapunto's window: UNDEFINED. No successor in window** under any variant, at any θ, with or without wraparound, and town by town (3.1). **(b-sub): UNDEFINED.** No fallback is invented (RS1 §5 Step 4). **Only (a) divides the share.**

### 3.3 Draft counts (split (a), primary; Hamilton / largest remainder, ties to the larger W)

**Robots, N = 20,079.** The floors sum to **20,071**, leaving **8** units: Donska-Kubania .9903, Tuva .9592, Siberia .8150, Idelsk-Uralia .7222, Karelia .6891, Künnarantaiga .6489, Ingushetia .6395, Russia .5858. The first two left out are Karachay-Cherkessia .5811 and Chechnya .5770.
**Humans, N = 19,376.** The floors sum to **19,368**, leaving **8** units: Siberia .9917, Donska-Kubania .9239, Karachay-Cherkessia .8956, Karelia .8728, Dagestan .8140, Kabardino-Balkaria .7928, Künnarantaiga .7168, Chechnya .5611. The first two left out are Russia .5020 and Tuva .3655. There are no exact ties.

| Successor | p_k | Robots N·p | floor | +1 | **Robots** | Humans N·p | floor | +1 | **Humans** |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.8327% | 8399.5858 | 8399 | 1 | **8,400** | 8105.5020 | 8105 | 0 | **8,105** |
| Idelsk-Uralia (prov.) | 23.4062% | 4699.7222 | 4699 | 1 | **4,700** | 4535.1770 | 4535 | 0 | **4,535** |
| Siberia | 16.9023% | 3393.8150 | 3393 | 1 | **3,394** | 3274.9917 | 3274 | 1 | **3,275** |
| Künnarantaiga | 8.2407% | 1654.6489 | 1654 | 1 | **1,655** | 1596.7168 | 1596 | 1 | **1,597** |
| Donska-Kubania (prov.) | 7.1218% | 1429.9903 | 1429 | 1 | **1,430** | 1379.9239 | 1379 | 1 | **1,380** |
| Karelia | 0.9696% | 194.6891 | 194 | 1 | **195** | 187.8728 | 187 | 1 | **188** |
| Dagestan | 0.6132% | 123.1248 | 123 | 0 | **123** | 118.8140 | 118 | 1 | **119** |
| Chechnya | 0.2868% | 57.5770 | 57 | 0 | **57** | 55.5611 | 55 | 1 | **56** |
| Kabardino-Balkaria | 0.1950% | 39.1640 | 39 | 0 | **39** | 37.7928 | 37 | 1 | **38** |
| North Ossetia-Alania | 0.1868% | 37.5029 | 37 | 0 | **37** | 36.1898 | 36 | 0 | **36** |
| Karachay-Cherkessia | 0.0975% | 19.5811 | 19 | 0 | **19** | 18.8956 | 18 | 1 | **19** |
| Tuva | 0.0845% | 16.9592 | 16 | 1 | **17** | 16.3655 | 16 | 0 | **16** |
| Ingushetia | 0.0629% | 12.6395 | 12 | 1 | **13** | 12.1970 | 12 | 0 | **12** |
| **Total** | 100% | 20079 | 20071 | 8 | **20,079** | 19376 | 19368 | 8 | **19,376** |

**No (b) counts exist** (3.2). Sensitivity, the P-only form, robots / humans: Russia 6,296 / 6,076 · Idelsk-Uralia 6,204 / 5,986 · Siberia 2,503 / 2,416 · Donska-Kubania 2,400 / 2,316 · Künnarantaiga 1,446 / 1,395 · Dagestan 445 / 429 · Chechnya 211 / 204 · Karelia 168 / 162 · Kabardino-Balkaria 126 / 122 · North Ossetia-Alania 96 / 93 · Ingushetia 71 / 69 · Karachay-Cherkessia 66 / 63 · Tuva 47 / 45 (same rounding rule).

### 3.4 Effective tier at Contrapunto (informational; nothing is ruled)

- **Under the composition method's admission test: no successor is admitted** (clause N fails, d ≥ 6; clause L fails against the city's own 20–25M evidence; clause G not applicable). **Effective tier: none.**
- **If admitted, using Contrapunto's own band edges** (T2 floor Brazil ~17M, T3 ceiling Argentina ~6M, spec L36–40 and `UEIC` L227–228), with the T2/T3 break re-placed at the largest ratio between them (§0 convention): Russia's Ê of 10.458M splits the gap into 17 ÷ 10.458 = **1.626** and 10.458 ÷ 6 = **1.743**, so **Russia would sit on the Significant side.** Idelsk-Uralia (5.852M), Siberia (4.226M), Künnarantaiga (2.060M) and Donska-Kubania (1.780M) sit inside the Notable band beside Argentina, Chile and Uruguay. Karelia (0.242M), the six North Caucasus republics and Tuva sit below Uruguay's ~0.6M, the lowest pool in the city's table, so they would be **Notable** as the lowest tier. This holds under V2 and K-in. **Under P-only it flips:** Russia (7.840M) and Idelsk-Uralia (7.724M) both fall on the Notable side (ratios 2.168, 1.015, 1.287; raw output identical in form to `step4.txt`).
- **Allocation note (DERIVED, not computed).** The tier rule allocates 8 / 3 / 1 shares per T1 / T2 / T3 nation (`UEIC` L1109). If the tiers were re-run with successors as separate nations, that rule would change the total Russian-successor share of Contrapunto rather than divide 6.12%. **This unit divides the existing count only, as the brief asks**, and does not re-run the allocation.
- **The strict ratio-gap reading** (raw, `step3.txt`): pre-split, the two largest gaps fall at USA→Germany (3.37) and Chile→Uruguay (3.833). That gives T3 = Uruguay only, **which does not reproduce Contrapunto's own table** (T3 = Argentina, Chile, Uruguay). Post-split: USA→Germany and Donska-Kubania→Uruguay (2.967). **Recorded, not relied on.**
```
 PRE-SPLIT breaks at: [('USA', 'Germany', 3.37), ('Chile', 'Uruguay', 3.833)]
 POST-SPLIT breaks at: [('USA', 'Germany', 3.37), ('Donska-Kubania', 'Uruguay', 2.967)]
 POST-SPLIT T1= ['USA']  T2= ['Germany', 'France', 'UK', 'Italy', 'South Korea', 'Mexico', 'Brazil', 'Russia', 'Argentina', 'Idelsk-Uralia', 'Siberia', 'Chile', 'Künnarantaiga', 'Donska-Kubania']
  Russia 10.458M rank 9/24; above: Brazil 17.000 (ratio 1.63); below: Argentina 6.000
  Idelsk-Uralia 5.852M rank 11/24; above: Argentina 6.000 (ratio 1.03); below: Siberia 4.226
  Siberia 4.226M rank 12/24; above: Idelsk-Uralia 5.852 (ratio 1.38); below: Chile 2.300
  Künnarantaiga 2.060M rank 14/24; above: Chile 2.300 (ratio 1.12); below: Donska-Kubania 1.780
  Donska-Kubania 1.780M rank 15/24; above: Künnarantaiga 2.060 (ratio 1.16); below: Uruguay 0.600
  Karelia 0.242M rank 17/24; above: Uruguay 0.600 (ratio 2.48); below: Dagestan 0.153
```
- **C-15 note:** under C-15 the Republic of Karelia's piece (0.29%) goes to Finland, which has no row at Contrapunto (spec L48–61). How that piece would be listed is **NOT FOUND**.

### 3.5 NOT FOUND and sensitivities at Contrapunto

**NOT FOUND:** a number for "large pool"; why China was removed and Japan is absent; gateway routing for any successor; how a C-15 Finland piece would be listed; every First Interwar figure.

| Input changed | Effect on window membership | Effect on split (a) | Effect on tier band (3.4, if admitted) | > 5 points? |
|---|---|---|---|---|
| V1c | none (Crimea +2: d 6) | Donska-Kubania +0.65 | none | no |
| V2 | none (d ≥ 6) | Russia +3.70, Idelsk-Uralia −2.05 | none | no |
| K-in | none (Kaliningrad +1: d 5) | Kaliningrad 0.57; others pro rata | none | no |
| C-15 | none (Finland piece +2: d 6) | Idelsk-Uralia +0.68; Finland piece 0.29 | see C-15 note | no |
| θ = 5% / 25% | none | — | — | no |
| Official zones | none (nearest +2, d 6) | — | — | no |
| Territory-centroid zones | none | — | — | no |
| Wraparound | none (closest d 6; Künnarantaiga 8) | — | — | no |
| Town-level footprint, any θ | none (nearest successor town +2, d 6) | — | — | no |
| Pool formula P only | none | **Russia −10.47; Idelsk-Uralia +7.49**; Donska-Kubania +4.83; Siberia −4.43 | Russia moves from the Significant side to Notable | **yes (Russia, Idelsk-Uralia)** |
| Other income-weighted forms | none | at most Russia +1.71 | none | no |
| Moscow, Amur or Sakhalin knife-edge zones | none | — | — | no |

---

## FINAL

**Reminder:** draft arithmetic only. The First Interwar record does not exist; every input is a present-day real-world regional figure aggregated to successor territories (DERIVED). Nothing here is a ruling or a recommendation, and no spec, census or composition file was edited.

### Per-city tables (each city on its own terms)

**Byrd (−8; window −11…−5; Notable 1.19%).**

| Successor | In window? | (a) % | (b) % | Robots | Humans | Tier (method / Byrd's own share-rank rule) |
|---|---|--:|---|--:|--:|---|
| Russia | no (d 10) | 41.83 | undefined | 1,007 | 988 | not admitted / Notable |
| Idelsk-Uralia (prov.) | no (d 11) | 23.41 | undefined | 564 | 553 | not admitted / Notable |
| Siberia | no (d 13) | 16.90 | undefined | 407 | 399 | not admitted / Notable |
| Künnarantaiga | no (d 15; 6 with wrap) | 8.24 | undefined | 198 | 195 | not admitted / Notable |
| Donska-Kubania (prov.) | no (d 11) | 7.12 | undefined | 171 | 168 | not admitted / Notable |
| Karelia | no (d 10) | 0.97 | undefined | 23 | 23 | not admitted / Notable |
| Dagestan | no (d 11) | 0.61 | undefined | 15 | 14 | not admitted / Notable |
| Chechnya | no (d 11) | 0.29 | undefined | 7 | 7 | not admitted / Notable |
| Kabardino-Balkaria | no (d 11) | 0.20 | undefined | 5 | 5 | not admitted / Notable |
| North Ossetia-Alania | no (d 11) | 0.19 | undefined | 5 | 4 | not admitted / Notable |
| Karachay-Cherkessia | no (d 11) | 0.10 | undefined | 2 | 2 | not admitted / Notable |
| Tuva | no (d 14) | 0.08 | undefined | 2 | 2 | not admitted / Notable |
| Ingushetia | no (d 11) | 0.06 | undefined | 2 | 1 | not admitted / Notable |
| **Total** | | 100 | | **2,408** | **2,361** | |

Clause L at Byrd is undetermined, since Byrd's own table admits ~0.6M pools at distance 10 on an unstated basis. Edge case: a town-level footprint with θ ≤ 0.09% admits Künnarantaiga alone (d 3), and (b) would then be 100% Künnarantaiga.

**Palmer City (−4; window −7…−1; Notable 1.20%; Russia present through the 2026-07-03 expansion, not the standard method).**

| Successor | In window? | (a) % | (b) % | Robots | Humans | Tier (method / expansion rule if extended / standard bands if admitted) |
|---|---|--:|---|--:|--:|---|
| Russia | no (d 6) | 41.83 | undefined | 840 | 835 | none / Notable / Significant side (Notable under P-only) |
| Idelsk-Uralia (prov.) | no (d 7) | 23.41 | undefined | 470 | 467 | none / Notable / Notable |
| Siberia | no (d 9) | 16.90 | undefined | 340 | 338 | none / Notable / Notable |
| Künnarantaiga | no (d 11) | 8.24 | undefined | 166 | 165 | none / Notable / Notable |
| Donska-Kubania (prov.) | no (d 7) | 7.12 | undefined | 143 | 142 | none / Notable / Notable |
| Karelia | no (d 6) | 0.97 | undefined | 19 | 19 | none / Notable / Notable |
| Dagestan | no (d 7) | 0.61 | undefined | 12 | 12 | none / Notable / Notable |
| Chechnya | no (d 7) | 0.29 | undefined | 6 | 6 | none / Notable / Notable |
| Kabardino-Balkaria | no (d 7) | 0.20 | undefined | 4 | 4 | none / Notable / Notable |
| North Ossetia-Alania | no (d 7) | 0.19 | undefined | 4 | 4 | none / Notable / Notable |
| Karachay-Cherkessia | no (d 7) | 0.10 | undefined | 2 | 2 | none / Notable / Notable |
| Tuva | no (d 10) | 0.08 | undefined | 2 | 2 | none / Notable / Notable |
| Ingushetia | no (d 7) | 0.06 | undefined | 1 | 1 | none / Notable / Notable |
| **Total** | | 100 | | **2,009** | **1,997** | |

**Contrapunto (−4; window −7…−1; Significant 6.12%; Russia admitted as one ~25M large pool).**

| Successor | In window? | (a) % | (b) % | Robots | Humans | Tier (method / city's own bands if admitted) |
|---|---|--:|---|--:|--:|---|
| Russia | no (d 6) | 41.83 | undefined | 8,400 | 8,105 | none / Significant side (Notable under P-only) |
| Idelsk-Uralia (prov.) | no (d 7) | 23.41 | undefined | 4,700 | 4,535 | none / Notable |
| Siberia | no (d 9) | 16.90 | undefined | 3,394 | 3,275 | none / Notable |
| Künnarantaiga | no (d 11) | 8.24 | undefined | 1,655 | 1,597 | none / Notable |
| Donska-Kubania (prov.) | no (d 7) | 7.12 | undefined | 1,430 | 1,380 | none / Notable |
| Karelia | no (d 6) | 0.97 | undefined | 195 | 188 | none / Notable |
| Dagestan | no (d 7) | 0.61 | undefined | 123 | 119 | none / Notable |
| Chechnya | no (d 7) | 0.29 | undefined | 57 | 56 | none / Notable |
| Kabardino-Balkaria | no (d 7) | 0.20 | undefined | 39 | 38 | none / Notable |
| North Ossetia-Alania | no (d 7) | 0.19 | undefined | 37 | 36 | none / Notable |
| Karachay-Cherkessia | no (d 7) | 0.10 | undefined | 19 | 19 | none / Notable |
| Tuva | no (d 10) | 0.08 | undefined | 17 | 16 | none / Notable |
| Ingushetia | no (d 7) | 0.06 | undefined | 13 | 12 | none / Notable |
| **Total** | | 100 | | **20,079** | **19,376** | |

On the city's own evidence, no successor meets clause L (its cut sits between about 20M and 25M) or clause N (d ≥ 6). Under the strict method, the 6.12% has no admitting clause after a split.

### Method used (one paragraph)
Split (a) = W_k ÷ ΣW, with W = Σ P × y2024 × (1 − G2022) over each successor's 2021-census subjects (RS1b), recomputed from the CSV and matching RS1b to two decimals. Split (b) applies the ±3 solar-zone window to each successor's meaningful zones (θ = 10%, S7 zones, no wraparound). It is **undefined for all three cities under every variant tried** (S1 × S2 × S3 × zone basis × θ ∈ {5, 10, 25%, any > 0} × wraparound), and (b-sub) is likewise empty. Counts use Hamilton's largest-remainder rule, ties to the larger W (none occurred), and sum exactly. Tiers are informational: the admission test (clauses N, L, G of `UEIC` L30–33), plus the tier rule each city's own section or spec states; the strict two-largest-ratio-gap reading of `UEIC` L17 is recorded raw but does not reproduce any of the three cities' own pre-split tables.

### NOT FOUND (all three sections together)
- A numeric threshold for "large pool" (clause L), and for "small pool" (clause N).
- Any gateway routing for a Russian successor (clause G).
- Byrd: the basis on which its table admits 38 out-of-window nations, sub-1M pools included; Byrd has no city section in `UEIC`.
- Palmer City: why Japan and China were left out before the 2026-07-03 expansion; whether that expansion's "every master-list nation" rule extends to successor nations; how it treats a later split of one nation's random draw.
- Contrapunto: why China was removed (2026-07-13) and Japan is absent; how a C-15 Finland piece would be listed.
- Every First Interwar figure. RS1b's own NOT FOUND list (Ukrainian Gini, Donetsk/Luhansk GRP after 2013, Ingushetia 2022 GRP, left-bank Kherson population, Rosstat primaries, which Gini measure CEIC carries) affects split (a) only and cannot affect any window here.

### Sensitivities that move a proportion by more than 5 points (all three cities)
- **Pool formula P only** (no income term): Russia −10.47 and Idelsk-Uralia +7.49 points in (a). At Palmer City's and Contrapunto's standard bands it also moves Russia from the Significant side to Notable.
- **Byrd only, the town-level footprint at θ ≤ 0.09%:** Künnarantaiga would hold 100% under (b) against 8.24% under (a).
- **Nothing else:** V1c, V2, K-in, C-15, θ 5% and 25%, official zones, territory centroids, wraparound, and the Moscow, Amur and Sakhalin knife-edges move no proportion by more than 5 points (the largest is V2's Russia, +3.70) and flip no window membership.

### Search and retrieval log (per LAW 0-R)
| # | What | Tool | Result |
|---|---|---|---|
| — | Web search | — | **None run.** No RS1b-listed gap can change any result here (see §0); the brief allows search only to fill those gaps. |
| L1 | `UEIC` L1–130, L143–167, L222–233, L381–388, L1047–1126 | Read | Method, Palmer City and Contrapunto sections, Byrd subnet header (Byrd has no city section) |
| L2 | `Specs/Byrd subnet/Byrd.md` L1–125; `Specs/Palmer subnet/Palmer_City.md` L40–129; `Specs/Palmer subnet/Contrapunto.md` L1–80 | Read | Each city's own tier table and Russia row |
| L3 | `Official_Population_Census.md` L220–239 (Byrd entry), L700–720 | Read | Byrd's pre-re-tiering table; no admission basis stated (dead end) |
| L4 | NE populated places (`/tmp/ne_test/…simple.geojson`): capitals and large cities | local script | Nation zones for the out-of-window evidence (DERIVED) |
| L5 | RS1 scratch `out/places_by_successor.csv`: Chukotka and Kamchatka towns; nearest town to each city zone | local script | The Byrd edge case; the nearest successor town to −4 is +2 |

**Scratch scripts and raw outputs** (not repo files): `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/a4f4478c-4c10-4425-b67b-16739b0736bb/scratchpad/rs4/` holds `rs4.py` (shared functions), `step1_splits.py` → `step1.txt`, `step2_windows.py` → `step2.txt`, `step3_counts_tiers.py` → `step3.txt`, `step4_band.py` → `step4.txt`, `step5_primary_table.py` → `step5.txt`, and `step6.txt` (shares of each city). All were run with `python3 -I`.

**What is left:** none of this unit's assigned work. Open for the developer, by name and not by recommendation: whether a split Russia keeps its place at each of the three cities, and on what basis, given that no successor is admitted by the composition method at any of them; whether Palmer City's expansion rule extends to successors; a number for "large pool".
