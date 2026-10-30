# Russia-split proportions · Unit RS3 · Troll, Santa Luce, Lazar, Concordia (2026-10-29)

**⚠ The First Interwar Period record does not exist yet.** The developer's Russia folders for it (`03 official timeline years`, `04 timeline staging`) are empty (RS1 section 2). **Every figure in this file is a present-day real-world regional figure aggregated to the successor territories (DERIVED), standing in for that unwritten record.** **Nothing here is a ruling or a recommendation.** The successor names are the developer's, exactly as `09 follow-up/subdivisions.csv` gives them; **Idelsk-Uralia and Donska-Kubania are provisional** (RS1 §1.2, conflicting sources) and are marked "(prov.)" wherever they appear.

**Brief:** `Research_Logs/Russia_Split_Proportions_Research_BRIEF_2026-10-29.md` (units RS2 to RS4, and the coordinator's section "Added 2026-10-29 (coordinator, after RS1)"). **Reads:** `Russia_Split_Proportions_RS1_Inventory_and_Method_2026-10-29.md` (RS1), `Russia_Split_Proportions_RS1b_Input_Table_2026-10-29.md` (RS1b), `Russia_Split_Inputs_2026-10-29.csv` (the CSV). Draft arithmetic only: no spec, census or composition file is touched; no other file is edited.

**Labels:** SOURCED (file and line, or URL) · UNVERIFIED · DERIVED · NOT FOUND.

**One location at a time.** Each city's section below stands on its own terms. No section ranks, compares or measures one city against another; the shared material in section 0 is method only.

## PROGRESS
- [x] 1 Troll
- [x] 2 Santa Luce
- [x] 3 Lazar
- [x] 4 Concordia
- [x] FINAL

---

## 0 · Method used (identical for all four cities; method only, no results)

### 0.1 Inputs, defaults and formulas
- **Inputs:** the 91 source units of the CSV (population 2021 census; GRP per head 2024; Gini 2022; S7 solar zone, territory-centroid zone and official zone; recipient at INIT and at C-15), exactly as RS1b built them. **This unit did not redo or change any national input.** All population, GRP and Gini figures are SOURCED secondary in RS1b and DERIVED as Tepenian inputs (RS1b first lines).
- **Coordinator defaults (NOT rulings; brief, "Added 2026-10-29"):** **S1 = V1** (83 pre-war federal subjects) · **S2 = K-out** · **S3 = INIT** · **S4 θ = 10%** · **S5 = solar zones** · **S6 = no wraparound** · **S7 = solar zone of each subject's largest city** · **E = P × y × (1 − G)**. The primary run is V1 · K-out · INIT · solar · S7 · θ 10% · E = P × y2024 × (1 − G2022). V2 uses E = P × y2021 for all units (Ukrainian Gini NOT FOUND, RS1b §3).
- **Check (DERIVED):** this unit's script reproduces RS1b's primary split (a) to two decimals for all 13 successors and every zone profile in RS1b §6.2, total W = 114.09 trillion rubles. Raw output:

```
CHECK vs RS1b 7.1 primary: Russia 41.83, Idelsk-Uralia (prov.) 23.41, Donska-Kubania (prov.) 7.12, Künnarantaiga 8.24, Siberia 16.90, Tuva 0.08, Karelia 0.97, Chechnya 0.29, Dagestan 0.61, Ingushetia 0.06, Kabardino-Balkaria 0.20, Karachay-Cherkessia 0.10, North Ossetia-Alania 0.19
   q Russia {2: 28.8, 3: 71.2}
   q Idelsk-Uralia {3: 57.1, 4: 42.9}
   q Donska-Kubania {3: 100.0}
   q Künnarantaiga {7: 24.9, 8: 6.4, 9: 49.6, 10: 14.5, 11: 3.2, 12: 1.4}
   q Siberia {4: 7.1, 5: 53.6, 6: 39.3}
   q Tuva {6: 100.0}
   q Karelia {2: 100.0}
   q Chechnya {3: 100.0}
   q Dagestan {3: 100.0}
   q Ingushetia {3: 100.0}
   q Kabardino-Balkaria {3: 100.0}
   q Karachay-Cherkessia {3: 100.0}
   q North Ossetia-Alania {3: 100.0}
total W (tn RUB): 114.09
```

- **Formulas (RS1 §5, applied as written):**
  - *E_s = P_s × y_s × (1 − G_s)* per source unit; *W_k = Σ E_s* over the units that go to successor *k*; *q_k(z)* = share of *W_k* in solar zone *z*; meaningful zones *Z_k(θ) = {z : q_k(z) ≥ θ}*.
  - **(a)** *p_k = W_k ÷ Σ_j W_j* (city-independent).
  - **(b)** *d_k = min over z in Z_k(θ) of |z − z_c|*; *I_k = 1 if d_k ≤ 3*; *p_k = W_k × I_k ÷ Σ_j W_j × I_j*. If no successor has *I_k = 1*, (b) is **UNDEFINED** and no fallback is invented (RS1 §5 Step 4).
  - **(b-sub)**, reported beside (b): only the part of *W_k* in units with *|z_s − z_c| ≤ 3* counts (RS1 §5 Step 4).
  - **City zone:** *z_c = round(longitude ÷ 15)* (`UEIC` L28).
- **Counts:** for robots and humans separately, *n_k = floor(total × p_k)*, then the remaining units one each to the largest fractional remainders, ties to the larger *W_k* (largest remainder, Hamilton; RS1 §5 Step 6). Totals are the Census I former-Russia robots and humans from the brief's table (each city's spec). **Census II was not computed** (outside the brief).

### 0.2 The tier readings (informational; tiers are not ruled)
The composition method: nations in a city are ranked by Gini-adjusted effective pool; *"Tier boundaries fall at the largest ratio gaps in each city's specific ranking"* (`UEIC` L17); *"A small-pool nation qualifies for the Notable tier only if distance ≤ 3 … large pools reach anywhere"* (`UEIC` L30–31); distance is the minimum over the zones where *"a meaningful share"* of the pool lives (`UEIC` L43–47). Allocation 8/3/1 shares per Primary/Significant/Notable nation (each city spec's footnote). **SOURCED.**

- **Successor pool:** *Ê_k = 25M × p_k(a)* (`UEIC` L76, pre-war Russia ~25M; RS1 §5 Step 7). Primary values (DERIVED): Russia 10.458M · Idelsk-Uralia (prov.) 5.852M · Siberia 4.226M · Künnarantaiga 2.060M · Donska-Kubania (prov.) 1.781M · Karelia 0.242M · Dagestan 0.153M · Chechnya 0.072M · Kabardino-Balkaria 0.049M · North Ossetia-Alania 0.047M · Karachay-Cherkessia 0.024M · Tuva 0.021M · Ingushetia 0.016M.
- **Comparators:** the city's own tier table (its spec, `Population & Composition`), with each nation's pool from `UEIC` L65–110 (Magna Lombardia ≈18M and Meridia ≈9M, illustrative, from `UEIC` L293–296).
- **Reading A (band placement, used as the main reading):** a successor takes the highest tier whose **smallest member pool in this city's own table** it equals or exceeds. Below the city's smallest Notable pool it is marked **"below floor"**: it can then appear only through the window rule (d ≤ 3), and **no minimum pool is stated anywhere in the method (NOT FOUND)**.
- **Reading A′ (in-window comparators only):** used only where the city's own table visibly orders its tiers by window rather than by pool alone. Comparator zones are DERIVED from the developer's Natural Earth populated-places file (`/tmp/ne_test/ne_10m_populated_places_simple.geojson`, round(lon ÷ 15)), or SOURCED where `UEIC` L57 states them.
- **Reading B (pure ratio-gap rule):** the city's full list with pre-war Russia replaced by the successors, sorted, cut at the two largest ratio gaps. **Restricted to pools at or above the city's smallest Notable pool.** Unrestricted, the successors' micro-pools (0.016 to 0.24M) create the largest ratio gaps at the bottom of the list and push every mid-size nation up a tier (shown in each raw block as "UNRESTRICTED"). Each city's raw block also states whether Reading B reproduces that city's current table; where it does not, Reading B is weak evidence for that city.
- **"Small pool" has no number in the method: NOT FOUND** (RS1 §5 Step 7). So whether an out-of-window successor would appear at all under the large-pool clause cannot be settled here; each city section states which successors this affects.

### 0.3 Scratch files (outside the repo; this session)
Scripts and full raw outputs are in `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/a4f4478c-4c10-4425-b67b-16739b0736bb/scratchpad/rs3/`: `rs3.py` (all arithmetic), `sweep.py` (108-combination sweep), `gen.py` (the tables in this file are generated by it, not retyped), `ne_lookup.py`, raw outputs `out_Troll.txt`, `out_SantaLuce.txt`, `out_Lazar.txt`, `out_Concordia.txt`, `out_sweep.txt`, `knife_blocks.txt`. All run with `python3 -I`.

---

## 1 · Troll

### 1.1 The city's own inputs
- **Position:** ~72°01'S 2°32'E (`UEIC` L276; SOURCED). 2.533 ÷ 15 = 0.169 → **solar zone 0** (DERIVED; 0.331 of a zone, about 5.0°, from the nearest boundary, so not a knife-edge). **Window: −3 … +3.**
- **Russia in Troll's spec:** Significant tier, **9.88%**, Census I **48,477 robots / 48,216 humans** (`Specs/Halley subnet/Troll.md` L21, L33; SOURCED, matches the brief's table).

### 1.2 Which successors lie inside the window
**Membership table (primary: V1 · K-out · INIT · solar zones, S7 · θ = 10%).** Window = solar -3 … +3. W in trillion rubles of Gini-adjusted GRP (RS1b §6.1). DERIVED.

| Successor | W (tn RUB) | Zone profile q(z) | Meaningful zones Z(10%) | Distance d | In window? | In-window part of W (unit level, tn) |
|---|--:|---|---|--:|---|--:|
| Russia | 47.726 | +2: 28.8% · +3: 71.2% | {+2, +3} | 2 | **IN** | 47.726 |
| Idelsk-Uralia (prov.) | 26.704 | +3: 57.1% · +4: 42.9% | {+3, +4} | 3 | **IN** | 15.256 |
| Donska-Kubania (prov.) | 8.125 | +3: 100.0% | {+3} | 3 | **IN** | 8.125 |
| Künnarantaiga | 9.402 | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7, +9, +10} | 7 | out | 0.000 |
| Siberia | 19.284 | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5, +6} | 5 | out | 0.000 |
| Tuva | 0.096 | +6: 100.0% | {+6} | 6 | out | 0.000 |
| Karelia | 1.106 | +2: 100.0% | {+2} | 2 | **IN** | 1.106 |
| Chechnya | 0.327 | +3: 100.0% | {+3} | 3 | **IN** | 0.327 |
| Dagestan | 0.700 | +3: 100.0% | {+3} | 3 | **IN** | 0.700 |
| Ingushetia | 0.072 | +3: 100.0% | {+3} | 3 | **IN** | 0.072 |
| Kabardino-Balkaria | 0.223 | +3: 100.0% | {+3} | 3 | **IN** | 0.223 |
| Karachay-Cherkessia | 0.111 | +3: 100.0% | {+3} | 3 | **IN** | 0.111 |
| North Ossetia-Alania | 0.213 | +3: 100.0% | {+3} | 3 | **IN** | 0.213 |
| **Total** | 114.089 | | | | in-window W = **85.307** | **73.859** |

**Reading the table (DERIVED):**
- **Inside (10):** Russia (d = 2, through its +2 units; its +3 units are also in), Idelsk-Uralia (prov.) (d = 3), Donska-Kubania (prov.) (d = 3), Karelia (d = 2), and the six North Caucasus republics (d = 3 each).
- **Outside (3):** Siberia (d = 5; its only +4 unit, Tyumen', is 7.1% of its pool, below θ, and even at θ = 5% Siberia's distance is 4), Künnarantaiga (d = 7), Tuva (d = 6).
- **Eight of the ten inside successors sit at d = 3 exactly, the edge of the window.** Their membership rests on their +3 cities: the nearest +3 cities to the +3/+4 boundary at 52.5°E are Syktyvkar (50.82°E, 1.68° inside) and Samara (50.15°E). Idelsk-Uralia's +3 share is 57.1% of its pool, so no single flip removes it.
- **At unit level (b-sub)** only Idelsk-Uralia loses part of its pool: its +4 units (Bashkortostan, Udmurt, Perm', Sverdlovsk, Chelyabinsk, Kurgan, Orenburg, Nenets; 42.9% of its W) lie at distance 4.

**Knife-edges, shown explicitly (brief; RS1b §4).** Each unit flipped across its nearest zone boundary, one at a time, primary variant. Lines with no effect at all are omitted. The four RS1b-named cases that are V1 units (Moscow, Tula, Blagoveshchensk, Yuzhno-Sakhalinsk) are always shown; the fifth, Donets'k, is a V2-only unit and lies in +2 or +3, both inside this window. 35 units were scanned within 3° of a boundary:

```
-- KNIFE-EDGE scan, Troll (primary variant): every unit whose S7 city lies within 3.0° of a zone boundary, flipped one at a time
   unit                     place                       lon  lon/15   z  ->  margin°  effect on membership / (b)
   Moskva                   Moscow                    37.61   2.507  +3  +2     0.11  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Tula                     Tula                      37.63   2.509  +3  +2     0.13  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Sakha (Yakutia)          Yakutsk                  129.74   8.649  +9  +8     2.24  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 8, 9, 10] d7->7 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Amur                     Blagoveshchensk          127.53   8.502  +9  +8     0.03  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 8, 9, 10] d7->7 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Sakhalin                 Yuzhno Sakhalinsk        142.74   9.516 +10  +9     0.24  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 9] d7->7 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Komi                     Syktyvkar                 50.82   3.388  +3  +4     1.68  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.87 pp (Idelsk-Uralia)
   Nenets                   Naryan Mar                53.06   3.537  +4  +3     0.56  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.37 pp (Idelsk-Uralia)
   Orenburg                 Orenburg                  55.11   3.674  +4  +3     2.61  no membership change | max (b) move 0.00 pp | max (b-sub) move 1.45 pp (Idelsk-Uralia)
   Udmurt                   Izhevsk                   53.23   3.549  +4  +3     0.73  no membership change | max (b) move 0.00 pp | max (b-sub) move 1.02 pp (Idelsk-Uralia)
   Kirov                    Kirov                     49.67   3.311  +3  +4     2.83  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.54 pp (Idelsk-Uralia)
   Samara                   Samara                    50.15   3.343  +3  +4     2.35  no membership change | max (b) move 0.00 pp | max (b-sub) move 2.37 pp (Idelsk-Uralia)
   Krasnodar                Krasnodar                 39.00   2.600  +3  +2     1.50  no membership change | Donska-Kubania Z [3]->[2, 3] d3->2 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Rostov                   Rostov                    39.71   2.647  +3  +2     2.21  no membership change | Donska-Kubania Z [3]->[2, 3] d3->2 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   [scan lines in total: 35]
```

- **Moscow (37.61°E, 0.11° from the +2/+3 boundary) does not decide membership at Troll.** At +3 Russia's profile is +2 28.8% / +3 71.2%; at +2 it would be +2 78.5% / +3 21.5% (RS1b §4). Both zones stay meaningful either way, Russia's distance stays 2, and every Russia unit lies inside the window at unit level (Moscow itself at distance 3 or 2), so neither (b) nor (b-sub) moves. Tula: the same.
- **Blagoveshchensk (0.03°) and Yuzhno-Sakhalinsk (0.24°)** change Künnarantaiga's meaningful zones only; it stays at distance 7, outside.
- **No knife-edge changes membership at Troll.** The largest unit-level move is Samara (+3 → +4): 2.37 points in (b-sub), Idelsk-Uralia.

### 1.3 The division of Troll's Russia share
**Split of the former-Russia share (percent of that share; each column sums to 100).** (a) = W_k ÷ ΣW; (b) = W_k × I_k ÷ Σ W_j × I_j; (b-sub) = in-window part of W_k ÷ Σ in-window parts. DERIVED.

| Successor | (a) | (b) | (b-sub) |
|---|--:|--:|--:|
| Russia | 41.83% | 55.95% | 64.62% |
| Idelsk-Uralia (prov.) | 23.41% | 31.30% | 20.66% |
| Donska-Kubania (prov.) | 7.12% | 9.52% | 11.00% |
| Künnarantaiga | 8.24% | 0.00% | 0.00% |
| Siberia | 16.90% | 0.00% | 0.00% |
| Tuva | 0.08% | 0.00% | 0.00% |
| Karelia | 0.97% | 1.30% | 1.50% |
| Chechnya | 0.29% | 0.38% | 0.44% |
| Dagestan | 0.61% | 0.82% | 0.95% |
| Ingushetia | 0.06% | 0.08% | 0.10% |
| Kabardino-Balkaria | 0.20% | 0.26% | 0.30% |
| Karachay-Cherkessia | 0.10% | 0.13% | 0.15% |
| North Ossetia-Alania | 0.19% | 0.25% | 0.29% |
| **Sum** | 100.00% | 100.00% | 100.00% |

**Worked inputs (DERIVED):** (b) Russia = 47.726 ÷ 85.307 = 55.95%; the in-window total 85.307 = 114.089 − 9.402 (Künnarantaiga) − 19.284 (Siberia) − 0.096 (Tuva). (b-sub) Idelsk-Uralia = 15.256 ÷ 73.859 = 20.66%, where 15.256 is the +3 part of its 26.704 (57.1%). Split (a) is the RS1b city-independent split unchanged.

Raw script output (primary):

```
-- PRIMARY (V1 . K-out . INIT . solar S7 . theta 10% . E = P x y2024 x (1-G2022)); W in trillion RUB
successor                                     W(tn) q(z) %                                   Z(10%)           d  in?    (a)%    (b)%   Wc(tn) (b-sub)%
Russia                                       47.726 +2:28.8 +3:71.2                          [2, 3]           2   IN   41.83   55.95   47.726    64.62
Idelsk-Uralia (prov.)                        26.704 +3:57.1 +4:42.9                          [3, 4]           3   IN   23.41   31.30   15.256    20.66
Donska-Kubania (prov.)                        8.125 +3:100.0                                 [3]              3   IN    7.12    9.52    8.125    11.00
Künnarantaiga                                 9.402 +7:24.9 +8:6.4 +9:49.6 +10:14.5 +11:3.2 +12:1.4 [7, 9, 10]       7  out    8.24    0.00    0.000     0.00
Siberia                                      19.284 +4:7.1 +5:53.6 +6:39.3                   [5, 6]           5  out   16.90    0.00    0.000     0.00
Tuva                                          0.096 +6:100.0                                 [6]              6  out    0.08    0.00    0.000     0.00
Karelia                                       1.106 +2:100.0                                 [2]              2   IN    0.97    1.30    1.106     1.50
Chechnya                                      0.327 +3:100.0                                 [3]              3   IN    0.29    0.38    0.327     0.44
Dagestan                                      0.700 +3:100.0                                 [3]              3   IN    0.61    0.82    0.700     0.95
Ingushetia                                    0.072 +3:100.0                                 [3]              3   IN    0.06    0.08    0.072     0.10
Kabardino-Balkaria                            0.223 +3:100.0                                 [3]              3   IN    0.20    0.26    0.223     0.30
Karachay-Cherkessia                           0.111 +3:100.0                                 [3]              3   IN    0.10    0.13    0.111     0.15
North Ossetia-Alania                          0.213 +3:100.0                                 [3]              3   IN    0.19    0.25    0.213     0.29
TOTAL                                       114.089   in-window W = 85.307 tn ; b-sub in-window W = 73.859 tn

-- COUNTS (a), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Russia                                      41.8327    20279.233   20279    20170.050   20170
Idelsk-Uralia (prov.)                       23.4062    11346.603   11347    11285.513   11286
Donska-Kubania (prov.)                       7.1218     3452.445    3452     3433.857    3434
Künnarantaiga                                8.2407     3994.841    3995     3973.333    3973
Siberia                                     16.9023     8193.733    8194     8149.618    8150
Tuva                                         0.0845       40.945      41       40.724      41
Karelia                                      0.9696      470.041     470      467.510     467
Chechnya                                     0.2868      139.009     139      138.261     138
Dagestan                                     0.6132      297.262     297      295.662     296
Ingushetia                                   0.0629       30.516      30       30.352      30
Kabardino-Balkaria                           0.1950       94.554      95       94.045      94
Karachay-Cherkessia                          0.0975       47.275      47       47.021      47
North Ossetia-Alania                         0.1868       90.544      91       90.056      90
SUM                                                                48477                48216

-- COUNTS (b), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Russia                                      55.9466    27121.233   27121    26975.213   26975
Idelsk-Uralia (prov.)                       31.3031    15174.827   15175    15093.126   15093
Donska-Kubania (prov.)                       9.5246     4617.263    4617     4592.404    4592
Karelia                                      1.2968      628.627     629      625.243     625
Chechnya                                     0.3835      185.909     186      184.908     185
Dagestan                                     0.8201      397.555     398      395.415     395
Ingushetia                                   0.0842       40.812      41       40.592      41
Kabardino-Balkaria                           0.2609      126.456     126      125.775     126
Karachay-Cherkessia                          0.1304       63.225      63       62.885      63
North Ossetia-Alania                         0.2498      121.092     121      120.440     121
SUM                                                                48477                48216

-- COUNTS (b-sub), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Russia                                      64.6182    31324.966   31325    31156.313   31156
Idelsk-Uralia (prov.)                       20.6553    10013.062   10013     9959.152    9959
Donska-Kubania (prov.)                      11.0009     5332.929    5333     5304.217    5304
Karelia                                      1.4977      726.063     726      722.154     722
Chechnya                                     0.4429      214.725     215      213.569     214
Dagestan                                     0.9472      459.175     459      456.703     457
Ingushetia                                   0.0972       47.137      47       46.883      47
Kabardino-Balkaria                           0.3013      146.056     146      145.270     145
Karachay-Cherkessia                          0.1506       73.025      73       72.632      73
North Ossetia-Alania                         0.2885      139.861     140      139.108     139
SUM                                                                48477                48216
```

### 1.4 Draft counts for Troll
**Draft counts, Census I (former-Russia robots 48,477, humans 48,216).** Largest remainder (Hamilton): each successor gets floor(total × p); the units left over go one each to the largest fractional remainders, ties to the larger W. DERIVED.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans | (b-sub) robots | (b-sub) humans |
|---|--:|--:|--:|--:|--:|--:|
| Russia | 20,279 | 20,170 | 27,121 | 26,975 | 31,325 | 31,156 |
| Idelsk-Uralia (prov.) | 11,347 | 11,286 | 15,175 | 15,093 | 10,013 | 9,959 |
| Donska-Kubania (prov.) | 3,452 | 3,434 | 4,617 | 4,592 | 5,333 | 5,304 |
| Künnarantaiga | 3,995 | 3,973 | 0 | 0 | 0 | 0 |
| Siberia | 8,194 | 8,150 | 0 | 0 | 0 | 0 |
| Tuva | 41 | 41 | 0 | 0 | 0 | 0 |
| Karelia | 470 | 467 | 629 | 625 | 726 | 722 |
| Chechnya | 139 | 138 | 186 | 185 | 215 | 214 |
| Dagestan | 297 | 296 | 398 | 395 | 459 | 457 |
| Ingushetia | 30 | 30 | 41 | 41 | 47 | 47 |
| Kabardino-Balkaria | 95 | 94 | 126 | 126 | 146 | 145 |
| Karachay-Cherkessia | 47 | 47 | 63 | 63 | 73 | 73 |
| North Ossetia-Alania | 91 | 90 | 121 | 121 | 140 | 139 |
| **Sum** | **48,477** | **48,216** | **48,477** | **48,216** | **48,477** | **48,216** |

### 1.5 Effective tier of each successor at Troll (informational, not ruled)
**Troll's own table** (`Specs/Halley subnet/Troll.md` L18–22): Primary USA (155M); Significant Germany (46), France (35), UK (32), Russia (25), Brazil (17); Notable Poland (12) down to Latvia and Estonia (0.6). Pools from `UEIC` L65–110. **Floors (DERIVED): Primary 155M · Significant 17M · Notable 0.6M.**

| Successor | Ê (M) | d | Reading A (band) | Reading B (ratio gap, pools ≥ 0.6M) | Note |
|---|--:|--:|---|---|---|
| Russia | 10.458 | 2 | Notable | Notable | below the Significant floor (17M) |
| Idelsk-Uralia (prov.) | 5.852 | 3 | Notable | Notable | |
| Donska-Kubania (prov.) | 1.781 | 3 | Notable | Notable | |
| Karelia | 0.242 | 2 | below floor | below floor | window-eligible (d ≤ 3); below every pool in Troll's table; no minimum stated (NOT FOUND) |
| Six North Caucasus republics | 0.016 to 0.153 | 3 | below floor | below floor | as Karelia |
| Siberia | 4.226 | 5 | Notable by band | Notable | **out of window:** appears only in split (a) and only if 4.2M counts as a "large pool" (cut NOT FOUND) |
| Künnarantaiga | 2.060 | 7 | Notable by band | Notable | out of window: as Siberia |
| Tuva | 0.021 | 6 | below floor | below floor | out of window and below floor: under `UEIC` L30–31 it would not appear at all |

**Raw tier output:**

```
tiers for split (a) presence (all successors):
   Reading B UNRESTRICTED (micro-pools included) top gaps [(3.37, 0), (2.475, 29), (2.138, 31)] -> Russia core would be Significant; shown only to record why B is restricted to pools >= the city's Notable floor

-- TIERS, Troll: floors (all comparators) {'Primary': 155, 'Significant': 17, 'Notable': 0.6}; in-window floors None
   Reading B reproduction check on the city's current list (Russia 25M): pre-war Russia -> Significant; mismatching nations: 2 ['Poland', 'Netherlands']; top ratio gaps [(3.37, 0), (1.667, 7), (1.667, 23)]; 2nd/3rd gap tie: True
   Reading B with successors substituted: top gaps [(3.37, 0), (1.882, 3), (1.667, 7)]; tie: False
   Russia                                     E =  10.4582 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Idelsk-Uralia (prov.)                      E =   5.8515 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Donska-Kubania (prov.)                     E =   1.7805 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Künnarantaiga                              E =   2.0602 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Siberia                                    E =   4.2256 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Tuva                                       E =   0.0211 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Karelia                                    E =   0.2424 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Chechnya                                   E =   0.0717 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Dagestan                                   E =   0.1533 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Ingushetia                                 E =   0.0157 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Kabardino-Balkaria                         E =   0.0488 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Karachay-Cherkessia                        E =   0.0244 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   North Ossetia-Alania                       E =   0.0467 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor

tiers for split (b) presence (in-window successors only):
   Reading B UNRESTRICTED (micro-pools included) top gaps [(3.37, 0), (2.475, 27), (2.138, 29)] -> Russia core would be Significant; shown only to record why B is restricted to pools >= the city's Notable floor

-- TIERS, Troll: floors (all comparators) {'Primary': 155, 'Significant': 17, 'Notable': 0.6}; in-window floors None
   Reading B reproduction check on the city's current list (Russia 25M): pre-war Russia -> Significant; mismatching nations: 2 ['Poland', 'Netherlands']; top ratio gaps [(3.37, 0), (1.667, 7), (1.667, 23)]; 2nd/3rd gap tie: True
   Reading B with successors substituted: top gaps [(3.37, 0), (1.882, 3), (1.667, 7)]; tie: False
   Russia                                     E =  10.4582 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Idelsk-Uralia (prov.)                      E =   5.8515 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Donska-Kubania (prov.)                     E =   1.7805 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Karelia                                    E =   0.2424 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Chechnya                                   E =   0.0717 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Dagestan                                   E =   0.1533 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Ingushetia                                 E =   0.0157 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Kabardino-Balkaria                         E =   0.0488 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Karachay-Cherkessia                        E =   0.0244 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   North Ossetia-Alania                       E =   0.0467 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
```

**Reading the tiers (DERIVED):**
- **No successor reaches Troll's Significant tier under either reading.** The largest, Russia (10.458M), sits below Brazil's 17M, the smallest Significant pool in Troll's table. The pre-war Russia row is Significant at 25M (spec L21).
- **Reading B does not reproduce Troll's current table** (2 mismatches, Poland and Netherlands, and a tie for the second-largest gap). Read it as weak evidence here. With the successors substituted it also moves Brazil from Significant to Notable (the second-largest gap becomes UK 32M → Brazil 17M). That is a side effect on a non-Russian nation, reported only to show how the bare gap rule behaves.
- **Seven of the ten in-window successors fall below the smallest pool in Troll's table.** The method gives them Notable through the window rule, and states no minimum pool.
- **Split (a) and the tier rule disagree for Siberia, Künnarantaiga and Tuva.** Split (a) gives them counts (8,194 + 3,995 + 41 robots); the tier rule admits an out-of-window nation only if its pool is "large", a cut the method does not state.

### 1.6 Sensitivities and NOT FOUND (Troll)
**Sensitivity, split (b), one input changed at a time (percent of the former-Russia share). Bold with ▲/▼ = moves more than 5 points against the primary row; † = this successor's window membership differs from primary; '—' = recipient does not exist in that variant.** DERIVED.

| Variant | Russia | Idelsk-Uralia (prov.) | Donska-Kubania (prov.) | Karelia | Chechnya | Dagestan | Ingushetia | Kabardino-Balkaria | Karachay-Cherkessia | North Ossetia-Alania | Kaliningrad (K-in) | Finland (Rep. of Karelia piece, C-15) | In window |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| primary | 55.95 | 31.30 | 9.52 | 1.30 | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania |
| V1c | 55.42 | 31.01 | 10.37 | 1.28 | 0.38 | 0.81 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| V2 (P × y2021, no Gini) | 59.53 | 27.93 | 9.31 | 1.55 | 0.28 | 0.80 | 0.07 | 0.21 | 0.11 | 0.20 | — | — | as primary |
| K-in | 55.52 | 31.07 | 9.45 | 1.29 | 0.38 | 0.81 | 0.08 | 0.26 | 0.13 | 0.25 | 0.76 † | — | + Kaliningrad (K-in) |
| C-15 | 55.95 | 32.21 | 9.52 | — | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | 0.39 † | + Finland (Rep. of Karelia piece, C-15) − Karelia |
| θ = 5% | 55.95 | 31.30 | 9.52 | 1.30 | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| θ = 25% | 55.95 | 31.30 | 9.52 | 1.30 | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| official zones (S5 alt.) | 55.95 | 31.30 | 9.52 | 1.30 | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| territory centroid (S7 alt.) | 55.95 | 31.30 | 9.52 | 1.30 | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| E = P × y2024 (no Gini) | 57.11 | 30.35 | 9.49 | 1.19 | 0.38 | 0.81 | 0.08 | 0.25 | 0.12 | 0.24 | — | — | as primary |
| E = P only | **39.15 ▼** | **38.57 ▲** | **14.92 ▲** | 1.04 | 1.31 | 2.77 | 0.44 | 0.79 | 0.41 | 0.60 | — | — | as primary |

**Sensitivity, split (b-sub), one input changed at a time (percent of the former-Russia share). Bold with ▲/▼ = moves more than 5 points against the primary row; † = this successor's window membership differs from primary; '—' = recipient does not exist in that variant.** DERIVED.

| Variant | Russia | Idelsk-Uralia (prov.) | Donska-Kubania (prov.) | Karelia | Chechnya | Dagestan | Ingushetia | Kabardino-Balkaria | Karachay-Cherkessia | North Ossetia-Alania | Kaliningrad (K-in) | Finland (Rep. of Karelia piece, C-15) | Nation-level window membership (as in split (b); b-sub counts unit-level parts) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| primary | 64.62 | 20.66 | 11.00 | 1.50 | 0.44 | 0.95 | 0.10 | 0.30 | 0.15 | 0.29 | — | — | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania |
| V1c | 63.92 | 20.43 | 11.96 | 1.48 | 0.44 | 0.94 | 0.10 | 0.30 | 0.15 | 0.29 | — | — | as primary |
| V2 (P × y2021, no Gini) | 67.68 | 18.06 | 10.58 | 1.76 | 0.32 | 0.91 | 0.08 | 0.24 | 0.12 | 0.23 | — | — | as primary |
| K-in | 64.05 | 20.47 | 10.90 | 1.48 | 0.44 | 0.94 | 0.10 | 0.30 | 0.15 | 0.29 | 0.87 | — | + Kaliningrad (K-in) |
| C-15 | 64.62 | 21.70 | 11.00 | — | 0.44 | 0.95 | 0.10 | 0.30 | 0.15 | 0.29 | — | 0.45 | + Finland (Rep. of Karelia piece, C-15) − Karelia |
| θ = 5% | 64.62 | 20.66 | 11.00 | 1.50 | 0.44 | 0.95 | 0.10 | 0.30 | 0.15 | 0.29 | — | — | as primary |
| θ = 25% | 64.62 | 20.66 | 11.00 | 1.50 | 0.44 | 0.95 | 0.10 | 0.30 | 0.15 | 0.29 | — | — | as primary |
| official zones (S5 alt.) | 68.26 | 17.05 | 10.76 | 1.58 | 0.47 | 1.00 | 0.10 | 0.32 | 0.16 | 0.30 | — | — | as primary |
| territory centroid (S7 alt.) | 65.32 | 19.79 | 11.12 | 1.51 | 0.45 | 0.96 | 0.10 | 0.30 | 0.15 | 0.29 | — | — | as primary |
| E = P × y2024 (no Gini) | 65.72 | 19.86 | 10.92 | 1.36 | 0.43 | 0.93 | 0.09 | 0.29 | 0.14 | 0.27 | — | — | as primary |
| E = P only | **46.63 ▼** | **26.84 ▲** | **17.77 ▲** | 1.24 | 1.56 | 3.29 | 0.53 | 0.94 | 0.49 | 0.71 | — | — | as primary |

**Split (a) moves above 5 points (city-independent; RS1b §7):** Russia 41.83 → 31.36 (E = P only); Idelsk-Uralia (prov.) 23.41 → 30.90 (E = P only).

**Cross-product sweep (all 108 combinations of S1 {V1, V1c, V2} × S2 {K-out, K-in} × S3 {INIT, C-15} × zones {solar, centroid, official} × θ {5, 10, 25%}): which successors are in the window.** DERIVED.

| Combinations | In window | Which (listed when 12 or fewer) |
|--:|---|---|
| 27 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania | — |
| 27 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania, Finland (Rep. of Karelia piece, C-15) | — |
| 27 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania, Kaliningrad (K-in) | — |
| 27 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania, Kaliningrad (K-in), Finland (Rep. of Karelia piece, C-15) | — |

**Flags: every proportion that moves more than 5 points (DERIVED):**
- **E = P only** (income dropped; not a coordinator variant, reported because RS1b §7.2 flags it): (a) Russia −10.47, Idelsk-Uralia +7.49; (b) Russia −16.80, Idelsk-Uralia +7.27, Donska-Kubania +5.40; (b-sub) Russia −17.99, Idelsk-Uralia +6.18, Donska-Kubania +6.77.
- **No coordinator alternative (V1c, V2, K-in, C-15, θ 5% or 25%, official zones, territory centroid) moves any successor by more than 5 points at Troll, in (a), (b) or (b-sub).** The largest is V2: (b) Russia +3.58, Idelsk-Uralia −3.37; (b-sub) Russia +3.06. Official zones move (b-sub) Russia +3.64.
- **Window membership of the Russia-split successors never changes at Troll** in any of the 108 combinations. The only membership differences are the two non-successor recipients the variants create: **Kaliningrad (K-in)** at solar +1 (d = 1, 0.69 to 0.76% of the share) and **Finland's Republic-of-Karelia piece (C-15)** at +2 (d = 2, 0.38 to 0.45%), which replaces the Karelia nation.
- **(b) ranges across all 108 combinations** (raw, `out_sweep.txt`): Russia 55.01 to 59.53 · Idelsk-Uralia (prov.) 27.74 to 32.21 · Donska-Kubania (prov.) 9.24 to 10.37 · Karelia 1.28 to 1.55 · each North Caucasus republic under 1%.

**NOT FOUND (Troll):** the meaningful-share threshold θ (the method gives none; 10% is the coordinator default) · the "small pool" cut for the large-pool clause · a minimum pool for Notable · the Gini penalty's functional form (`UEIC` gives none; E = P × y × (1 − G) is the stated convention) · any First Interwar population, GRP or Gini for any successor. Inherited input gaps: RS1b §8.

---

## 2 · Santa Luce

### 2.1 The city's own inputs
- **Position:** ~73°03'S 13°25'W (`UEIC` L288; SOURCED). −13.417 ÷ 15 = −0.894 → **solar zone −1** (DERIVED; 0.394 of a zone, about 5.9°, from the nearest boundary). **Window: −4 … +2.**
- **Russia in Santa Luce's spec:** Significant tier, **9.04%**, Census I **20,229 robots / 19,330 humans** (`Specs/Halley subnet/Santa_Luce.md` L23, L35; SOURCED, matches the brief's table). The composition was rebuilt on 2026-10-29 on the post-war states Magna Lombardia and Meridia (`DR-83`, spec L63); **Russia's 9.04% stands as listed** (brief). This unit splits only that row.

### 2.2 Which successors lie inside the window
**Membership table (primary: V1 · K-out · INIT · solar zones, S7 · θ = 10%).** Window = solar -4 … +2. W in trillion rubles of Gini-adjusted GRP (RS1b §6.1). DERIVED.

| Successor | W (tn RUB) | Zone profile q(z) | Meaningful zones Z(10%) | Distance d | In window? | In-window part of W (unit level, tn) |
|---|--:|---|---|--:|---|--:|
| Russia | 47.726 | +2: 28.8% · +3: 71.2% | {+2, +3} | 3 | **IN** | 13.732 |
| Idelsk-Uralia (prov.) | 26.704 | +3: 57.1% · +4: 42.9% | {+3, +4} | 4 | out | 0.000 |
| Donska-Kubania (prov.) | 8.125 | +3: 100.0% | {+3} | 4 | out | 0.000 |
| Künnarantaiga | 9.402 | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7, +9, +10} | 8 | out | 0.000 |
| Siberia | 19.284 | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5, +6} | 6 | out | 0.000 |
| Tuva | 0.096 | +6: 100.0% | {+6} | 7 | out | 0.000 |
| Karelia | 1.106 | +2: 100.0% | {+2} | 3 | **IN** | 1.106 |
| Chechnya | 0.327 | +3: 100.0% | {+3} | 4 | out | 0.000 |
| Dagestan | 0.700 | +3: 100.0% | {+3} | 4 | out | 0.000 |
| Ingushetia | 0.072 | +3: 100.0% | {+3} | 4 | out | 0.000 |
| Kabardino-Balkaria | 0.223 | +3: 100.0% | {+3} | 4 | out | 0.000 |
| Karachay-Cherkessia | 0.111 | +3: 100.0% | {+3} | 4 | out | 0.000 |
| North Ossetia-Alania | 0.213 | +3: 100.0% | {+3} | 4 | out | 0.000 |
| **Total** | 114.089 | | | | in-window W = **48.833** | **14.839** |

**Reading the table (DERIVED):**
- **Inside (2):** **Russia** (d = 3, only through its +2 units, which hold 28.8% of its pool; its +3 units, 71.2%, are at distance 4) and **Karelia** (+2, d = 3).
- **Outside (11):** Idelsk-Uralia (prov.), Donska-Kubania (prov.) and the six North Caucasus republics (all d = 4, one zone past the window's edge), Siberia (d = 6), Tuva (d = 7), Künnarantaiga (d = 8).
- **Both inside successors are at d = 3, the window's edge, and both are in only through their +2 zone.** Russia's membership needs its +2 share (28.8%) to reach θ. At θ = 25% it does, by 3.8 points; at any θ above 28.8% it does not, and (b) becomes **Karelia 100%** (checked at θ = 29%: (b) Karelia 100.00; `combos.py`).
- **At unit level (b-sub)** only Russia's +2 units (St. Petersburg, Leningrad, Novgorod, Pskov, Smolensk, Tver', Kaluga, Bryansk, Orel, Kursk, Belgorod) count: 13.732 of Russia's 47.726. That is why (b-sub) gives Karelia more than (b) does.

**Knife-edges, shown explicitly (brief; RS1b §4).** Each unit flipped across its nearest zone boundary, one at a time, primary variant. Lines with no effect at all are omitted. The four RS1b-named V1 cases are always shown; Donets'k is V2-only. 35 units were scanned within 3° of a boundary:

```
-- KNIFE-EDGE scan, Santa Luce (primary variant): every unit whose S7 city lies within 3.0° of a zone boundary, flipped one at a time
   unit                     place                       lon  lon/15   z  ->  margin°  effect on membership / (b)
   Belgorod                 Belgorod                  36.60   2.440  +2  +3     0.90  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.53 pp (Karelia)
   Kaluga                   Kaluga                    36.27   2.418  +2  +3     1.23  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.32 pp (Russia)
   Kursk                    Kursk                     36.19   2.413  +2  +3     1.31  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.29 pp (Russia)
   Lipetsk                  Lipetsk                   39.64   2.643  +3  +2     2.14  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.33 pp (Karelia)
   Moskovskaya              Noginsk (NE largest; B    38.48   2.565  +3  +2     0.98  no membership change | max (b) move 0.00 pp | max (b-sub) move 2.32 pp (Russia)
   Moskva                   Moscow                    37.61   2.507  +3  +2     0.11  no membership change | max (b) move 0.00 pp | max (b-sub) move 4.59 pp (Russia)
   Orel                     Orel                      36.07   2.405  +2  +3     1.43  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.15 pp (Russia)
   Ryazan'                  Ryazan                    39.72   2.648  +3  +2     2.22  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.26 pp (Russia)
   Tula                     Tula                      37.63   2.509  +3  +2     0.13  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.42 pp (Karelia)
   Tver'                    Tver                      35.89   2.393  +2  +3     1.61  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.30 pp (Russia)
   Voronezh                 Voronezh                  39.27   2.618  +3  +2     1.77  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.50 pp (Karelia)
   Sakha (Yakutia)          Yakutsk                  129.74   8.649  +9  +8     2.24  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 8, 9, 10] d8->8 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Amur                     Blagoveshchensk          127.53   8.502  +9  +8     0.03  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 8, 9, 10] d8->8 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Sakhalin                 Yuzhno Sakhalinsk        142.74   9.516 +10  +9     0.24  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 9] d8->8 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Vladimir                 Vladimir                  40.41   2.694  +3  +2     2.91  no membership change | max (b) move 0.00 pp | max (b-sub) move 4.36 pp (Idelsk-Uralia)
   Yaroslavl'               Yaroslavl                 39.87   2.658  +3  +2     2.37  no membership change | max (b) move 0.00 pp | max (b-sub) move 4.40 pp (Idelsk-Uralia)
   Vologda                  Cherepovets               37.91   2.527  +3  +2     0.41  no membership change | max (b) move 0.00 pp | max (b-sub) move 5.23 pp (Idelsk-Uralia)
   Krasnodar                Krasnodar                 39.00   2.600  +3  +2     1.50  MEMBERSHIP: Donska-Kubania: out->IN | Donska-Kubania Z [3]->[2, 3] d4->3 | max (b) move 14.27 pp | max (b-sub) move 17.68 pp (Donska-Kubania)
   Adygey                   Maykop                    40.12   2.675  +3  +2     2.62  no membership change | max (b) move 0.00 pp | max (b-sub) move 1.12 pp (Donska-Kubania)
   Rostov                   Rostov                    39.71   2.647  +3  +2     2.21  MEMBERSHIP: Donska-Kubania: out->IN | Donska-Kubania Z [3]->[2, 3] d4->3 | max (b) move 14.27 pp | max (b-sub) move 11.49 pp (Donska-Kubania)
   [scan lines in total: 35]
```

- **Moscow (37.61°E, 0.11° from the +2/+3 boundary)** does not change membership: Russia is already inside through +2. It does move (b-sub). At +2 Moscow's 20.8% of the whole V1 pool would fall inside the window at unit level, and Russia's (b-sub) share rises by **4.59 points** (just under the 5-point flag).
- **Vologda (Cherepovets, 37.91°E, 0.41° from the boundary): flagged, more than 5 points in (b-sub).** At +2, Vologda's pool enters the window at unit level for Idelsk-Uralia (prov.). (b-sub) Idelsk-Uralia moves by **5.23 points**, though Idelsk-Uralia's nation-level membership does not change (its +2 share would stay below θ).
- **Krasnodar (39.00°E, 1.50° from the boundary) and Rostov (39.71°E, 2.21°): flagged, membership.** Either one placed at +2 makes +2 a meaningful zone of Donska-Kubania (prov.). That puts it at d = 3, **inside**, and moves (b) by **14.27 points**; (b-sub) by 17.68 (Krasnodar) or 11.49 (Rostov). These are not knife-edges in the 0.35° sense of RS1b. They show that **Donska-Kubania's exclusion at Santa Luce rests on the S7 rule placing each of these two subjects at its largest city.**
- **Blagoveshchensk and Yuzhno-Sakhalinsk** change Künnarantaiga's meaningful zones only; it stays at distance 8.

### 2.3 The division of Santa Luce's Russia share
**Split of the former-Russia share (percent of that share; each column sums to 100).** (a) = W_k ÷ ΣW; (b) = W_k × I_k ÷ Σ W_j × I_j; (b-sub) = in-window part of W_k ÷ Σ in-window parts. DERIVED.

| Successor | (a) | (b) | (b-sub) |
|---|--:|--:|--:|
| Russia | 41.83% | 97.73% | 92.55% |
| Idelsk-Uralia (prov.) | 23.41% | 0.00% | 0.00% |
| Donska-Kubania (prov.) | 7.12% | 0.00% | 0.00% |
| Künnarantaiga | 8.24% | 0.00% | 0.00% |
| Siberia | 16.90% | 0.00% | 0.00% |
| Tuva | 0.08% | 0.00% | 0.00% |
| Karelia | 0.97% | 2.27% | 7.45% |
| Chechnya | 0.29% | 0.00% | 0.00% |
| Dagestan | 0.61% | 0.00% | 0.00% |
| Ingushetia | 0.06% | 0.00% | 0.00% |
| Kabardino-Balkaria | 0.20% | 0.00% | 0.00% |
| Karachay-Cherkessia | 0.10% | 0.00% | 0.00% |
| North Ossetia-Alania | 0.19% | 0.00% | 0.00% |
| **Sum** | 100.00% | 100.00% | 100.00% |

**Worked inputs (DERIVED):** (b) Russia = 47.726 ÷ (47.726 + 1.106) = 47.726 ÷ 48.833 = 97.73%; Karelia = 1.106 ÷ 48.833 = 2.27%. (b-sub) Russia = 13.732 ÷ (13.732 + 1.106) = 92.55%. Split (a) is the RS1b city-independent split unchanged. **Under (a), 57.20% of the Russia share (100 − 41.83 − 0.97: Idelsk-Uralia, Siberia, Künnarantaiga, Donska-Kubania and the rest) goes to successors that are outside Santa Luce's window.**

Raw script output (primary):

```
-- PRIMARY (V1 . K-out . INIT . solar S7 . theta 10% . E = P x y2024 x (1-G2022)); W in trillion RUB
successor                                     W(tn) q(z) %                                   Z(10%)           d  in?    (a)%    (b)%   Wc(tn) (b-sub)%
Russia                                       47.726 +2:28.8 +3:71.2                          [2, 3]           3   IN   41.83   97.73   13.732    92.55
Idelsk-Uralia (prov.)                        26.704 +3:57.1 +4:42.9                          [3, 4]           4  out   23.41    0.00    0.000     0.00
Donska-Kubania (prov.)                        8.125 +3:100.0                                 [3]              4  out    7.12    0.00    0.000     0.00
Künnarantaiga                                 9.402 +7:24.9 +8:6.4 +9:49.6 +10:14.5 +11:3.2 +12:1.4 [7, 9, 10]       8  out    8.24    0.00    0.000     0.00
Siberia                                      19.284 +4:7.1 +5:53.6 +6:39.3                   [5, 6]           6  out   16.90    0.00    0.000     0.00
Tuva                                          0.096 +6:100.0                                 [6]              7  out    0.08    0.00    0.000     0.00
Karelia                                       1.106 +2:100.0                                 [2]              3   IN    0.97    2.27    1.106     7.45
Chechnya                                      0.327 +3:100.0                                 [3]              4  out    0.29    0.00    0.000     0.00
Dagestan                                      0.700 +3:100.0                                 [3]              4  out    0.61    0.00    0.000     0.00
Ingushetia                                    0.072 +3:100.0                                 [3]              4  out    0.06    0.00    0.000     0.00
Kabardino-Balkaria                            0.223 +3:100.0                                 [3]              4  out    0.20    0.00    0.000     0.00
Karachay-Cherkessia                           0.111 +3:100.0                                 [3]              4  out    0.10    0.00    0.000     0.00
North Ossetia-Alania                          0.213 +3:100.0                                 [3]              4  out    0.19    0.00    0.000     0.00
TOTAL                                       114.089   in-window W = 48.833 tn ; b-sub in-window W = 14.839 tn

-- COUNTS (a), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Russia                                      41.8327     8462.335    8462     8086.259    8086
Idelsk-Uralia (prov.)                       23.4062     4734.831    4735     4524.410    4524
Donska-Kubania (prov.)                       7.1218     1440.673    1441     1376.648    1377
Künnarantaiga                                8.2407     1667.010    1667     1592.926    1593
Siberia                                     16.9023     3419.168    3419     3267.217    3267
Tuva                                         0.0845       17.086      17       16.327      16
Karelia                                      0.9696      196.144     196      187.427     187
Chechnya                                     0.2868       58.007      58       55.429      56
Dagestan                                     0.6132      124.045     124      118.532     119
Ingushetia                                   0.0629       12.734      13       12.168      12
Kabardino-Balkaria                           0.1950       39.457      39       37.703      38
Karachay-Cherkessia                          0.0975       19.727      20       18.851      19
North Ossetia-Alania                         0.1868       37.783      38       36.104      36
SUM                                                                20229                19330

-- COUNTS (b), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Russia                                      97.7347    19770.745   19771    18892.111   18892
Karelia                                      2.2653      458.255     458      437.889     438
SUM                                                                20229                19330

-- COUNTS (b-sub), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Russia                                      92.5450    18720.929   18721    17888.949   17889
Karelia                                      7.4550     1508.071    1508     1441.051    1441
SUM                                                                20229                19330
```

### 2.4 Draft counts for Santa Luce
**Draft counts, Census I (former-Russia robots 20,229, humans 19,330).** Largest remainder (Hamilton): each successor gets floor(total × p); the units left over go one each to the largest fractional remainders, ties to the larger W. DERIVED.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans | (b-sub) robots | (b-sub) humans |
|---|--:|--:|--:|--:|--:|--:|
| Russia | 8,462 | 8,086 | 19,771 | 18,892 | 18,721 | 17,889 |
| Idelsk-Uralia (prov.) | 4,735 | 4,524 | 0 | 0 | 0 | 0 |
| Donska-Kubania (prov.) | 1,441 | 1,377 | 0 | 0 | 0 | 0 |
| Künnarantaiga | 1,667 | 1,593 | 0 | 0 | 0 | 0 |
| Siberia | 3,419 | 3,267 | 0 | 0 | 0 | 0 |
| Tuva | 17 | 16 | 0 | 0 | 0 | 0 |
| Karelia | 196 | 187 | 458 | 438 | 1,508 | 1,441 |
| Chechnya | 58 | 56 | 0 | 0 | 0 | 0 |
| Dagestan | 124 | 119 | 0 | 0 | 0 | 0 |
| Ingushetia | 13 | 12 | 0 | 0 | 0 | 0 |
| Kabardino-Balkaria | 39 | 38 | 0 | 0 | 0 | 0 |
| Karachay-Cherkessia | 20 | 19 | 0 | 0 | 0 | 0 |
| North Ossetia-Alania | 38 | 36 | 0 | 0 | 0 | 0 |
| **Sum** | **20,229** | **19,330** | **20,229** | **19,330** | **20,229** | **19,330** |

### 2.5 Effective tier of each successor at Santa Luce (informational, not ruled)
**Santa Luce's own table** (`Specs/Halley subnet/Santa_Luce.md` L20–24): Primary USA (155M); Significant Germany (46), France (35), UK (32), Russia (25), Magna Lombardia (≈18, illustrative), Brazil (17); Notable Meridia (≈9, illustrative), Poland (12), Netherlands (10), Belgium (6.4) … Latvia and Estonia (0.6). Pools from `UEIC` L65–110 and L293–296. **Floors (DERIVED): Primary 155M · Significant 17M (Brazil) · Notable 0.6M.** The illustrative Magna Lombardia and Meridia pools set neither floor, so their provisional status does not affect this reading.

| Successor | Ê (M) | d | Reading A (band) | Reading B (ratio gap, pools ≥ 0.6M) | Note |
|---|--:|--:|---|---|---|
| Russia | 10.458 | 3 | Notable | Notable | below the Significant floor (17M) |
| Karelia | 0.242 | 3 | below floor | below floor | window-eligible (d ≤ 3); below every pool in Santa Luce's table; no minimum stated (NOT FOUND) |
| Idelsk-Uralia (prov.) | 5.852 | 4 | Notable by band | Notable | **out of window:** appears only in split (a), and only if 5.9M counts as a "large pool" (cut NOT FOUND) |
| Siberia | 4.226 | 6 | Notable by band | Notable | out of window: as above |
| Künnarantaiga | 2.060 | 8 | Notable by band | Notable | out of window: as above |
| Donska-Kubania (prov.) | 1.781 | 4 | Notable by band | Notable | out of window: as above |
| Six North Caucasus republics, Tuva | 0.016 to 0.153 | 4 to 7 | below floor | below floor | out of window and below floor: under `UEIC` L30–31 they would not appear at all |

**Raw tier output:**

```
tiers for split (a) presence (all successors):
   Reading B UNRESTRICTED (micro-pools included) top gaps [(3.37, 0), (2.475, 31), (2.138, 33)] -> Russia core would be Significant; shown only to record why B is restricted to pools >= the city's Notable floor

-- TIERS, Santa Luce: floors (all comparators) {'Primary': 155, 'Significant': 17, 'Notable': 0.6}; in-window floors None
   Reading B reproduction check on the city's current list (Russia 25M): pre-war Russia -> Significant; mismatching nations: 14 ['Meridia', 'Poland', 'Netherlands', 'Belgium', 'Sweden', 'Argentina', 'Czech', 'Ukraine', 'Romania', 'Norway', 'Finland', 'Hungary', 'SouthAfrica', 'Slovakia']; top ratio gaps [(3.37, 0), (1.692, 20), (1.667, 25)]; 2nd/3rd gap tie: False
   Reading B with successors substituted: top gaps [(3.37, 0), (1.778, 3), (1.667, 29)]; tie: False
   Russia                                     E =  10.4582 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Idelsk-Uralia (prov.)                      E =   5.8515 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Donska-Kubania (prov.)                     E =   1.7805 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Künnarantaiga                              E =   2.0602 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Siberia                                    E =   4.2256 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Tuva                                       E =   0.0211 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Karelia                                    E =   0.2424 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Chechnya                                   E =   0.0717 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Dagestan                                   E =   0.1533 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Ingushetia                                 E =   0.0157 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Kabardino-Balkaria                         E =   0.0488 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Karachay-Cherkessia                        E =   0.0244 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   North Ossetia-Alania                       E =   0.0467 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor

tiers for split (b) presence (in-window successors only):
   Reading B UNRESTRICTED (micro-pools included) top gaps [(3.37, 0), (2.475, 27), (1.778, 3)] -> Russia core would be Significant; shown only to record why B is restricted to pools >= the city's Notable floor

-- TIERS, Santa Luce: floors (all comparators) {'Primary': 155, 'Significant': 17, 'Notable': 0.6}; in-window floors None
   Reading B reproduction check on the city's current list (Russia 25M): pre-war Russia -> Significant; mismatching nations: 14 ['Meridia', 'Poland', 'Netherlands', 'Belgium', 'Sweden', 'Argentina', 'Czech', 'Ukraine', 'Romania', 'Norway', 'Finland', 'Hungary', 'SouthAfrica', 'Slovakia']; top ratio gaps [(3.37, 0), (1.692, 20), (1.667, 25)]; 2nd/3rd gap tie: False
   Reading B with successors substituted: top gaps [(3.37, 0), (1.778, 3), (1.692, 20)]; tie: False
   Russia                                     E =  10.4582 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Karelia                                    E =   0.2424 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
```

**Reading the tiers (DERIVED):**
- **No successor reaches Santa Luce's Significant tier under either reading.** The largest, Russia (10.458M), sits below Brazil's 17M. The pre-war Russia row is Significant at 25M (spec L23).
- **Reading B does not reproduce Santa Luce's current table** (14 mismatching nations), so it is weak evidence here.
- **Split (a) and the tier rule disagree for eleven successors.** Split (a) assigns Santa Luce counts to every out-of-window successor (for example 4,735 robots to Idelsk-Uralia and 3,419 to Siberia). The tier rule admits an out-of-window nation only if its pool is "large", a cut the method does not state, and excludes the out-of-window micro-pools outright.

### 2.6 Sensitivities and NOT FOUND (Santa Luce)
**Sensitivity, split (b), one input changed at a time (percent of the former-Russia share). Bold with ▲/▼ = moves more than 5 points against the primary row; † = this successor's window membership differs from primary; '—' = recipient does not exist in that variant.** DERIVED.

| Variant | Russia | Karelia | Kaliningrad (K-in) | Finland (Rep. of Karelia piece, C-15) | In window |
|---|--:|--:|--:|--:|---|
| primary | 97.73 | 2.27 | — | — | Russia, Karelia |
| V1c | 97.73 | 2.27 | — | — | as primary |
| V2 (P × y2021, no Gini) | 97.46 | 2.54 | — | — | as primary |
| K-in | 96.45 | 2.24 | 1.32 † | — | + Kaliningrad (K-in) |
| C-15 | 99.31 | — | — | 0.69 † | + Finland (Rep. of Karelia piece, C-15) − Karelia |
| θ = 5% | 97.73 | 2.27 | — | — | as primary |
| θ = 25% | 97.73 | 2.27 | — | — | as primary |
| official zones (S5 alt.) | — | — | — | — | **no successor in window: (b) UNDEFINED** |
| territory centroid (S7 alt.) | 97.73 | 2.27 | — | — | as primary |
| E = P × y2024 (no Gini) | 97.97 | 2.03 | — | — | as primary |
| E = P only | 97.40 | 2.60 | — | — | as primary |

**Sensitivity, split (b-sub), one input changed at a time (percent of the former-Russia share). Bold with ▲/▼ = moves more than 5 points against the primary row; † = this successor's window membership differs from primary; '—' = recipient does not exist in that variant.** DERIVED.

| Variant | Russia | Idelsk-Uralia (prov.) | Donska-Kubania (prov.) | Karelia | Kaliningrad (K-in) | Finland (Rep. of Karelia piece, C-15) | Nation-level window membership (as in split (b); b-sub counts unit-level parts) |
|---|--:|--:|--:|--:|--:|--:|---|
| primary | 92.55 | 0.00 | 0.00 | 7.45 | — | — | Russia, Karelia |
| V1c | 87.79 | 0.00 | **5.13 ▲** | 7.07 | — | — | as primary |
| V2 (P × y2021, no Gini) | 89.07 | 0.00 | 3.78 | 7.15 | — | — | as primary |
| K-in | 88.65 | 0.00 | 0.00 | 7.14 | 4.21 | — | + Kaliningrad (K-in) |
| C-15 | 92.55 | **5.22 ▲** | 0.00 | — | — | 2.23 | + Finland (Rep. of Karelia piece, C-15) − Karelia |
| θ = 5% | 92.55 | 0.00 | 0.00 | 7.45 | — | — | as primary |
| θ = 25% | 92.55 | 0.00 | 0.00 | 7.45 | — | — | as primary |
| official zones (S5 alt.) | — | — | — | — | — | — | **no successor in window: (b) UNDEFINED** |
| territory centroid (S7 alt.) | 97.12 | 0.00 | 0.00 | 2.88 | — | — | as primary |
| E = P × y2024 (no Gini) | 93.13 | 0.00 | 0.00 | 6.87 | — | — | as primary |
| E = P only | 93.21 | 0.00 | 0.00 | 6.79 | — | — | as primary |

**Split (a) moves above 5 points (city-independent; RS1b §7):** Russia 41.83 → 31.36 (E = P only); Idelsk-Uralia (prov.) 23.41 → 30.90 (E = P only).

**Cross-product sweep (all 108 combinations of S1 {V1, V1c, V2} × S2 {K-out, K-in} × S3 {INIT, C-15} × zones {solar, centroid, official} × θ {5, 10, 25%}): which successors are in the window.** DERIVED.

| Combinations | In window | Which (listed when 12 or fewer) |
|--:|---|---|
| 16 | Kaliningrad (K-in) | — |
| 14 | Russia, Karelia | — |
| 14 | Russia, Finland (Rep. of Karelia piece, C-15) | — |
| 14 | Russia, Karelia, Kaliningrad (K-in) | — |
| 14 | Russia, Kaliningrad (K-in), Finland (Rep. of Karelia piece, C-15) | — |
| 4 | Russia, Donska-Kubania (prov.), Karelia | V1c · K-out · INIT · solar · θ 5%; V1c · K-out · INIT · centroid · θ 5%; V2 · K-out · INIT · solar · θ 5%; V2 · K-out · INIT · centroid · θ 5% |
| 4 | Russia, Donska-Kubania (prov.), Finland (Rep. of Karelia piece, C-15) | V1c · K-out · C-15 · solar · θ 5%; V1c · K-out · C-15 · centroid · θ 5%; V2 · K-out · C-15 · solar · θ 5%; V2 · K-out · C-15 · centroid · θ 5% |
| 4 | Russia, Donska-Kubania (prov.), Karelia, Kaliningrad (K-in) | V1c · K-in · INIT · solar · θ 5%; V1c · K-in · INIT · centroid · θ 5%; V2 · K-in · INIT · solar · θ 5%; V2 · K-in · INIT · centroid · θ 5% |
| 4 | Russia, Donska-Kubania (prov.), Kaliningrad (K-in), Finland (Rep. of Karelia piece, C-15) | V1c · K-in · C-15 · solar · θ 5%; V1c · K-in · C-15 · centroid · θ 5%; V2 · K-in · C-15 · solar · θ 5%; V2 · K-in · C-15 · centroid · θ 5% |
| 2 | Russia | V2 · K-out · INIT · official · θ 5%; V2 · K-out · C-15 · official · θ 5% |
| 2 | Russia, Kaliningrad (K-in) | V2 · K-in · INIT · official · θ 5%; V2 · K-in · C-15 · official · θ 5% |
| 16 | **none: (b) UNDEFINED** | V1 · K-out · INIT · official · θ 5%; V1 · K-out · INIT · official · θ 10%; V1 · K-out · INIT · official · θ 25%; V1 · K-out · C-15 · official · θ 5%; V1 · K-out · C-15 · official · θ 10%; V1 · K-out · C-15 · official · θ 25%; V1c · K-out · INIT · official · θ 5%; V1c · K-out · INIT · official · θ 10%; V1c · K-out · INIT · official · θ 25%; V1c · K-out · C-15 · official · θ 5%; V1c · K-out · C-15 · official · θ 10%; V1c · K-out · C-15 · official · θ 25%; V2 · K-out · INIT · official · θ 10%; V2 · K-out · INIT · official · θ 25%; V2 · K-out · C-15 · official · θ 10%; V2 · K-out · C-15 · official · θ 25% |

**Combined cases the sweep surfaced, computed in full** (`combos.py`; raw):

```
Santa Luce | V1c K-out INIT solar θ0.05: (b) Russia 82.63, Karelia 1.92, Donska-Kubania 15.46 || (b-sub) Russia 87.79, Karelia 7.07, Donska-Kubania 5.13
      counts (b) robots {'Russia': 16715, 'Karelia': 387, 'Donska-Kubania': 3127} humans {'Russia': 15972, 'Karelia': 370, 'Donska-Kubania': 2988}
Santa Luce | V2 K-out INIT solar θ0.05: (b) Russia 84.58, Karelia 2.20, Donska-Kubania 13.22 || (b-sub) Russia 89.07, Karelia 7.15, Donska-Kubania 3.78
      counts (b) robots {'Russia': 17109, 'Karelia': 445, 'Donska-Kubania': 2675} humans {'Russia': 16348, 'Karelia': 426, 'Donska-Kubania': 2556}
Santa Luce | V1 K-in INIT official θ0.10: (b) Kaliningrad (K-in) 100.00 || (b-sub) Kaliningrad (K-in) 100.00
      counts (b) robots {'Kaliningrad (K-in)': 20229} humans {'Kaliningrad (K-in)': 19330}
Santa Luce | V2 K-out INIT official θ0.05: (b) Russia 100.00 || (b-sub) Russia 100.00
      counts (b) robots {'Russia': 20229} humans {'Russia': 19330}
Santa Luce | V1 K-out INIT solar θ0.29: (b) Karelia 100.00 || (b-sub) Russia 92.55, Karelia 7.45
      counts (b) robots {'Karelia': 20229} humans {'Karelia': 19330}
Santa Luce | V1c K-in C15 solar θ0.05: (b) Russia 82.80, Finland (Rep. of Karelia piece, C-15) 0.57, Donska-Kubania 15.49, Kaliningrad (K-in) 1.13 || (b-sub) Russia 84.28, Idelsk-Uralia 4.76, Finland (Rep. of Karelia piece, C-15) 2.03, Donska-Kubania 4.93, Kaliningrad (K-in) 4.00
      counts (b) robots {'Russia': 16751, 'Finland (Rep. of Karelia piece, C-15)': 116, 'Donska-Kubania': 3133, 'Kaliningrad (K-in)': 229} humans {'Russia': 16006, 'Finland (Rep. of Karelia piece, C-15)': 111, 'Donska-Kubania': 2994, 'Kaliningrad (K-in)': 219}
Santa Luce | V2 K-in C15 centroid θ0.05: (b) Russia 85.06, Finland (Rep. of Karelia piece, C-15) 0.64, Donska-Kubania 13.30, Kaliningrad (K-in) 1.00 || (b-sub) Russia 93.95, Idelsk-Uralia 2.17, Finland (Rep. of Karelia piece, C-15) 0.88, Donska-Kubania 1.62, Kaliningrad (K-in) 1.38
      counts (b) robots {'Russia': 17207, 'Finland (Rep. of Karelia piece, C-15)': 129, 'Donska-Kubania': 2691, 'Kaliningrad (K-in)': 202} humans {'Russia': 16443, 'Finland (Rep. of Karelia piece, C-15)': 124, 'Donska-Kubania': 2571, 'Kaliningrad (K-in)': 192}
```

**Flags: every proportion that moves more than 5 points, or whose window membership changes (DERIVED):**
- **Official zones (S5 alternative): (b) is UNDEFINED at Santa Luce.** Under official zones every successor's nearest zone is +3 or more (Russia, Karelia, Donska-Kubania and the republics all +3), at distance 4, so **no successor is in the window**. Then Santa Luce's Russia share exists only under the large-pool clause, and split (a) is the only split (RS1 §5 Step 4). This holds in 16 of the 108 combinations, every official-zone combination except those noted next.
- **K-in with official zones: Kaliningrad 100%.** Kaliningrad's official zone (+2) is at distance 3, so it becomes the **only** in-window recipient. Kaliningrad is not a Russia-split nation: it is a CIN member (RS1 §1.2). This holds in 16 combinations.
- **V2 with official zones at θ = 5%: Russia 100%.** The eastern-Ukraine slice keeps Ukraine's legal UTC+2 (RS1b §4), 8.8% of V2 Russia's pool, which clears θ = 5% but not 10%.
- **V1c or V2 with θ = 5%: Donska-Kubania (prov.) enters, 13.2 to 15.7% in (b).** Crimea and Sevastopol (solar +2) are 9.0% (V1c) or 8.8% (V2) of its pool, below θ = 10% and above 5%. Russia then falls by 13.2 to 15.1 points. 16 combinations.
- **θ above 28.8%:** Russia leaves; (b) = Karelia 100%. Not among the coordinator's sweep values (5, 10, 25%); stated because 25% clears it by only 3.8 points.
- **C-15:** Karelia (nation) is replaced by Finland's Republic-of-Karelia piece (0.69% in (b)), and Russia rises to 99.31%. In (b-sub), Murmansk (+2, now Idelsk-Uralia's) brings **Idelsk-Uralia (prov.) in at 5.22 points (flag)**.
- **V1c, (b-sub): Donska-Kubania (prov.) +5.13 (flag)**, through Crimea and Sevastopol at unit level.
- **Territory centroid:** no change in (b); (b-sub) Karelia −4.57 (under the flag).
- **E = P only** moves no in-window proportion by more than 5 points here (Russia −0.33 in (b)), because the two in-window successors move together. In (a) it moves Russia −10.47 and Idelsk-Uralia +7.49 (RS1b §7.2).
- **(b) ranges across all defined combinations** (raw, `out_sweep.txt`): Russia 0.00 to 100.00 · Donska-Kubania (prov.) 0.00 to 15.67 · Karelia 0.00 to 2.54 · Kaliningrad (K-in) 0.98 to 100.00 · Finland's piece 0.00 to 0.75.

**NOT FOUND (Santa Luce):** the meaningful-share threshold θ (decisive here for Russia above 28.8% and for Donska-Kubania below 9.0%) · whether solar or official zones are meant for a nation's footprint (decisive here: official zones leave (b) undefined; RS1 §4.2 notes the source mixes them) · the "small pool" cut · a minimum pool for Notable · the Gini penalty's functional form · any First Interwar population, GRP or Gini for any successor. Inherited input gaps: RS1b §8.

---

## 3 · Lazar

### 3.1 The city's own inputs
- **Position:** ~70°46'S 11°44'E (`UEIC` L324; SOURCED). 11.733 ÷ 15 = 0.782 → **solar zone +1** (DERIVED; 0.282 of a zone, about 4.2°, from the nearest boundary). **Window: −2 … +4.**
- **Russia in Lazar's spec:** Significant tier, **4.81%**, Census I **58,246 robots / 56,261 humans** (`Specs/Halley subnet/Lazar.md` L42, L57; SOURCED, matches the brief's table).
- `DR-34` names *"Russia (the core state) and the CIN"* as Lazar's founders (spec L161). Founders are not composition (RS1 §3.5), so nothing below uses it.

### 3.2 Which successors lie inside the window
**Membership table (primary: V1 · K-out · INIT · solar zones, S7 · θ = 10%).** Window = solar -2 … +4. W in trillion rubles of Gini-adjusted GRP (RS1b §6.1). DERIVED.

| Successor | W (tn RUB) | Zone profile q(z) | Meaningful zones Z(10%) | Distance d | In window? | In-window part of W (unit level, tn) |
|---|--:|---|---|--:|---|--:|
| Russia | 47.726 | +2: 28.8% · +3: 71.2% | {+2, +3} | 1 | **IN** | 47.726 |
| Idelsk-Uralia (prov.) | 26.704 | +3: 57.1% · +4: 42.9% | {+3, +4} | 2 | **IN** | 26.704 |
| Donska-Kubania (prov.) | 8.125 | +3: 100.0% | {+3} | 2 | **IN** | 8.125 |
| Künnarantaiga | 9.402 | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7, +9, +10} | 6 | out | 0.000 |
| Siberia | 19.284 | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5, +6} | 4 | out | 1.372 |
| Tuva | 0.096 | +6: 100.0% | {+6} | 5 | out | 0.000 |
| Karelia | 1.106 | +2: 100.0% | {+2} | 1 | **IN** | 1.106 |
| Chechnya | 0.327 | +3: 100.0% | {+3} | 2 | **IN** | 0.327 |
| Dagestan | 0.700 | +3: 100.0% | {+3} | 2 | **IN** | 0.700 |
| Ingushetia | 0.072 | +3: 100.0% | {+3} | 2 | **IN** | 0.072 |
| Kabardino-Balkaria | 0.223 | +3: 100.0% | {+3} | 2 | **IN** | 0.223 |
| Karachay-Cherkessia | 0.111 | +3: 100.0% | {+3} | 2 | **IN** | 0.111 |
| North Ossetia-Alania | 0.213 | +3: 100.0% | {+3} | 2 | **IN** | 0.213 |
| **Total** | 114.089 | | | | in-window W = **85.307** | **86.679** |

**Reading the table (DERIVED):**
- **Inside (10):** Russia (d = 1, through +2; its +3 units are at d = 2), Karelia (d = 1), Idelsk-Uralia (prov.) (d = 2 through +3; its +4 units at d = 3 are also inside), Donska-Kubania (prov.) (d = 2), and the six North Caucasus republics (d = 2 each).
- **Outside (3):** **Siberia (d = 4)**, Tuva (d = 5), Künnarantaiga (d = 6).
- **Siberia is the edge case at Lazar.** One Siberian unit, Tyumen' (city of Tyumen, 65.53°E, solar +4), lies at distance 3, inside the window. It holds 1.372 of Siberia's 19.284 trillion, **7.11%** of its pool. At θ = 10% that is not a meaningful share, so Siberia is outside in (b). It still counts at unit level in (b-sub) (**1.58%** of Lazar's Russia share). At θ = 5% Siberia is inside in (b), with its **whole** pool (see 3.6).
- Every other inside successor is inside with all of its pool at unit level, so (b) and (b-sub) differ here only through Siberia.

**Knife-edges, shown explicitly (brief; RS1b §4).** Each unit flipped across its nearest zone boundary, one at a time, primary variant. Lines with no effect at all are omitted. The four RS1b-named V1 cases are always shown; Donets'k is V2-only, at +2 or +3, inside either way. 35 units were scanned within 3° of a boundary:

```
-- KNIFE-EDGE scan, Lazar (primary variant): every unit whose S7 city lies within 3.0° of a zone boundary, flipped one at a time
   unit                     place                       lon  lon/15   z  ->  margin°  effect on membership / (b)
   Moskva                   Moscow                    37.61   2.507  +3  +2     0.11  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Tula                     Tula                      37.63   2.509  +3  +2     0.13  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Sakha (Yakutia)          Yakutsk                  129.74   8.649  +9  +8     2.24  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 8, 9, 10] d6->6 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Amur                     Blagoveshchensk          127.53   8.502  +9  +8     0.03  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 8, 9, 10] d6->6 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Sakhalin                 Yuzhno Sakhalinsk        142.74   9.516 +10  +9     0.24  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 9] d6->6 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Tyumen'                  Tyumen                    65.53   4.369  +4  +5     1.97  no membership change | max (b) move 0.00 pp | max (b-sub) move 1.58 pp (Siberia)
   Kurgan                   Kurgan                    65.34   4.356  +4  +5     2.16  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.25 pp (Idelsk-Uralia)
   Krasnodar                Krasnodar                 39.00   2.600  +3  +2     1.50  no membership change | Donska-Kubania Z [3]->[2, 3] d2->1 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Rostov                   Rostov                    39.71   2.647  +3  +2     2.21  no membership change | Donska-Kubania Z [3]->[2, 3] d2->1 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   [scan lines in total: 35]
```

- **Moscow (37.61°E, 0.11° from the +2/+3 boundary) does not decide membership at Lazar.** At +3 Russia's profile is +2 28.8% / +3 71.2%; at +2 it would be +2 78.5% / +3 21.5% (RS1b §4). Both zones stay meaningful, Russia's distance stays 1, and every Russia unit lies inside the window at unit level either way (Moscow itself at distance 2 or 1), so neither (b) nor (b-sub) moves. Tula: the same.
- **Blagoveshchensk (0.03°) and Yuzhno-Sakhalinsk (0.24°)** change Künnarantaiga's meaningful zones only; it stays at distance 6.
- **Tyumen (65.53°E, 1.97° from the +4/+5 boundary)** is the only flip that touches Siberia. At +5, Siberia loses its only in-window unit, and (b-sub) Siberia falls from 1.58% to 0. Under the territory-centroid alternative Tyumen' already sits at +5 (RS1b §4), which is why the centroid row has no Siberia at all.
- **No single flip changes membership at Lazar.**

### 3.3 The division of Lazar's Russia share
**Split of the former-Russia share (percent of that share; each column sums to 100).** (a) = W_k ÷ ΣW; (b) = W_k × I_k ÷ Σ W_j × I_j; (b-sub) = in-window part of W_k ÷ Σ in-window parts. DERIVED.

| Successor | (a) | (b) | (b-sub) |
|---|--:|--:|--:|
| Russia | 41.83% | 55.95% | 55.06% |
| Idelsk-Uralia (prov.) | 23.41% | 31.30% | 30.81% |
| Donska-Kubania (prov.) | 7.12% | 9.52% | 9.37% |
| Künnarantaiga | 8.24% | 0.00% | 0.00% |
| Siberia | 16.90% | 0.00% | 1.58% |
| Tuva | 0.08% | 0.00% | 0.00% |
| Karelia | 0.97% | 1.30% | 1.28% |
| Chechnya | 0.29% | 0.38% | 0.38% |
| Dagestan | 0.61% | 0.82% | 0.81% |
| Ingushetia | 0.06% | 0.08% | 0.08% |
| Kabardino-Balkaria | 0.20% | 0.26% | 0.26% |
| Karachay-Cherkessia | 0.10% | 0.13% | 0.13% |
| North Ossetia-Alania | 0.19% | 0.25% | 0.25% |
| **Sum** | 100.00% | 100.00% | 100.00% |

**Worked inputs (DERIVED):** (b) Russia = 47.726 ÷ 85.307 = 55.95%; the in-window total 85.307 = 114.089 − 9.402 (Künnarantaiga) − 19.284 (Siberia) − 0.096 (Tuva). (b-sub) adds Tyumen's 1.372 to the in-window total: 86.679; Siberia = 1.372 ÷ 86.679 = 1.58%. Split (a) is the RS1b city-independent split unchanged.

Raw script output (primary):

```
-- PRIMARY (V1 . K-out . INIT . solar S7 . theta 10% . E = P x y2024 x (1-G2022)); W in trillion RUB
successor                                     W(tn) q(z) %                                   Z(10%)           d  in?    (a)%    (b)%   Wc(tn) (b-sub)%
Russia                                       47.726 +2:28.8 +3:71.2                          [2, 3]           1   IN   41.83   55.95   47.726    55.06
Idelsk-Uralia (prov.)                        26.704 +3:57.1 +4:42.9                          [3, 4]           2   IN   23.41   31.30   26.704    30.81
Donska-Kubania (prov.)                        8.125 +3:100.0                                 [3]              2   IN    7.12    9.52    8.125     9.37
Künnarantaiga                                 9.402 +7:24.9 +8:6.4 +9:49.6 +10:14.5 +11:3.2 +12:1.4 [7, 9, 10]       6  out    8.24    0.00    0.000     0.00
Siberia                                      19.284 +4:7.1 +5:53.6 +6:39.3                   [5, 6]           4  out   16.90    0.00    1.372     1.58
Tuva                                          0.096 +6:100.0                                 [6]              5  out    0.08    0.00    0.000     0.00
Karelia                                       1.106 +2:100.0                                 [2]              1   IN    0.97    1.30    1.106     1.28
Chechnya                                      0.327 +3:100.0                                 [3]              2   IN    0.29    0.38    0.327     0.38
Dagestan                                      0.700 +3:100.0                                 [3]              2   IN    0.61    0.82    0.700     0.81
Ingushetia                                    0.072 +3:100.0                                 [3]              2   IN    0.06    0.08    0.072     0.08
Kabardino-Balkaria                            0.223 +3:100.0                                 [3]              2   IN    0.20    0.26    0.223     0.26
Karachay-Cherkessia                           0.111 +3:100.0                                 [3]              2   IN    0.10    0.13    0.111     0.13
North Ossetia-Alania                          0.213 +3:100.0                                 [3]              2   IN    0.19    0.25    0.213     0.25
TOTAL                                       114.089   in-window W = 85.307 tn ; b-sub in-window W = 86.679 tn

-- COUNTS (a), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Russia                                      41.8327    24365.869   24366    23535.490   23535
Idelsk-Uralia (prov.)                       23.4062    13633.150   13633    13168.538   13169
Donska-Kubania (prov.)                       7.1218     4148.175    4148     4006.807    4007
Künnarantaiga                                8.2407     4799.875    4800     4636.297    4636
Siberia                                     16.9023     9844.920    9845     9509.409    9509
Tuva                                         0.0845       49.196      49       47.520      48
Karelia                                      0.9696      564.762     565      545.516     546
Chechnya                                     0.2868      167.022     167      161.330     161
Dagestan                                     0.6132      357.166     357      344.994     345
Ingushetia                                   0.0629       36.665      37       35.416      35
Kabardino-Balkaria                           0.1950      113.608     113      109.737     110
Karachay-Cherkessia                          0.0975       56.802      57       54.866      55
North Ossetia-Alania                         0.1868      108.790     109      105.082     105
SUM                                                                58246                56261

-- COUNTS (b), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Russia                                      55.9466    32586.657   32587    31476.117   31476
Idelsk-Uralia (prov.)                       31.3031    18232.832   18233    17611.464   17611
Donska-Kubania (prov.)                       9.5246     5547.726    5548     5358.662    5359
Karelia                                      1.2968      755.307     755      729.567     730
Chechnya                                     0.3835      223.373     223      215.761     216
Dagestan                                     0.8201      477.670     478      461.391     461
Ingushetia                                   0.0842       49.036      49       47.365      47
Kabardino-Balkaria                           0.2609      151.939     152      146.761     147
Karachay-Cherkessia                          0.1304       75.966      76       73.377      73
North Ossetia-Alania                         0.2498      145.494     145      140.536     141
SUM                                                                58246                56261

-- COUNTS (b-sub), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Russia                                      55.0613    32071.028   32071    30978.060   30978
Idelsk-Uralia (prov.)                       30.8078    17944.328   17944    17332.793   17333
Donska-Kubania (prov.)                       9.3739     5459.943    5460     5273.870    5274
Siberia                                      1.5823      921.645     922      890.235     890
Karelia                                      1.2762      743.356     743      718.023     718
Chechnya                                     0.3774      219.839     220      212.347     212
Dagestan                                     0.8071      470.111     470      454.090     454
Ingushetia                                   0.0829       48.260      48       46.615      47
Kabardino-Balkaria                           0.2567      149.535     150      144.438     145
Karachay-Cherkessia                          0.1284       74.764      75       72.216      72
North Ossetia-Alania                         0.2458      143.192     143      138.312     138
SUM                                                                58246                56261
```

### 3.4 Draft counts for Lazar
**Draft counts, Census I (former-Russia robots 58,246, humans 56,261).** Largest remainder (Hamilton): each successor gets floor(total × p); the units left over go one each to the largest fractional remainders, ties to the larger W. DERIVED.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans | (b-sub) robots | (b-sub) humans |
|---|--:|--:|--:|--:|--:|--:|
| Russia | 24,366 | 23,535 | 32,587 | 31,476 | 32,071 | 30,978 |
| Idelsk-Uralia (prov.) | 13,633 | 13,169 | 18,233 | 17,611 | 17,944 | 17,333 |
| Donska-Kubania (prov.) | 4,148 | 4,007 | 5,548 | 5,359 | 5,460 | 5,274 |
| Künnarantaiga | 4,800 | 4,636 | 0 | 0 | 0 | 0 |
| Siberia | 9,845 | 9,509 | 0 | 0 | 922 | 890 |
| Tuva | 49 | 48 | 0 | 0 | 0 | 0 |
| Karelia | 565 | 546 | 755 | 730 | 743 | 718 |
| Chechnya | 167 | 161 | 223 | 216 | 220 | 212 |
| Dagestan | 357 | 345 | 478 | 461 | 470 | 454 |
| Ingushetia | 37 | 35 | 49 | 47 | 48 | 47 |
| Kabardino-Balkaria | 113 | 110 | 152 | 147 | 150 | 145 |
| Karachay-Cherkessia | 57 | 55 | 76 | 73 | 75 | 72 |
| North Ossetia-Alania | 109 | 105 | 145 | 141 | 143 | 138 |
| **Sum** | **58,246** | **56,261** | **58,246** | **56,261** | **58,246** | **56,261** |

### 3.5 Effective tier of each successor at Lazar (informational, not ruled)
**Lazar's own table** (`Specs/Halley subnet/Lazar.md` L39–43): Primary USA (155M); Significant Germany (46), France (35), UK (32), Russia (25), Brazil (17); Notable Poland (12), Netherlands (10), Argentina (6) … Latvia and Estonia (0.6). Pools from `UEIC` L65–110. **Floors (DERIVED): Primary 155M · Significant 17M · Notable 0.6M.**

| Successor | Ê (M) | d | Reading A (band) | Reading B (ratio gap, pools ≥ 0.6M) | Note |
|---|--:|--:|---|---|---|
| Russia | 10.458 | 1 | Notable | Notable | below the Significant floor (17M) |
| Idelsk-Uralia (prov.) | 5.852 | 2 | Notable | Notable | |
| Donska-Kubania (prov.) | 1.781 | 2 | Notable | Notable | |
| Karelia | 0.242 | 1 | below floor | below floor | window-eligible (d ≤ 3); below every pool in Lazar's table; no minimum stated (NOT FOUND) |
| Six North Caucasus republics | 0.016 to 0.153 | 2 | below floor | below floor | as Karelia |
| Siberia | 4.226 | 4 (3 at θ = 5%) | Notable by band | Notable | **out of window at θ = 10%:** appears in split (a) only if 4.2M counts as a "large pool" (cut NOT FOUND); inside and Notable at θ = 5% |
| Künnarantaiga | 2.060 | 6 | Notable by band | Notable | out of window: as Siberia at θ = 10% |
| Tuva | 0.021 | 5 | below floor | below floor | out of window and below floor: under `UEIC` L30–31 it would not appear at all |

**Raw tier output:**

```
tiers for split (a) presence (all successors):
   Reading B UNRESTRICTED (micro-pools included) top gaps [(3.37, 0), (2.475, 28), (2.138, 30)] -> Russia core would be Significant; shown only to record why B is restricted to pools >= the city's Notable floor

-- TIERS, Lazar: floors (all comparators) {'Primary': 155, 'Significant': 17, 'Notable': 0.6}; in-window floors None
   Reading B reproduction check on the city's current list (Russia 25M): pre-war Russia -> Significant; mismatching nations: 2 ['Poland', 'Netherlands']; top ratio gaps [(3.37, 0), (1.667, 7), (1.667, 22)]; 2nd/3rd gap tie: True
   Reading B with successors substituted: top gaps [(3.37, 0), (1.882, 3), (1.667, 7)]; tie: False
   Russia                                     E =  10.4582 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Idelsk-Uralia (prov.)                      E =   5.8515 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Donska-Kubania (prov.)                     E =   1.7805 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Künnarantaiga                              E =   2.0602 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Siberia                                    E =   4.2256 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Tuva                                       E =   0.0211 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Karelia                                    E =   0.2424 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Chechnya                                   E =   0.0717 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Dagestan                                   E =   0.1533 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Ingushetia                                 E =   0.0157 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Kabardino-Balkaria                         E =   0.0488 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Karachay-Cherkessia                        E =   0.0244 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   North Ossetia-Alania                       E =   0.0467 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor

tiers for split (b) presence (in-window successors only):
   Reading B UNRESTRICTED (micro-pools included) top gaps [(3.37, 0), (2.475, 26), (2.138, 28)] -> Russia core would be Significant; shown only to record why B is restricted to pools >= the city's Notable floor

-- TIERS, Lazar: floors (all comparators) {'Primary': 155, 'Significant': 17, 'Notable': 0.6}; in-window floors None
   Reading B reproduction check on the city's current list (Russia 25M): pre-war Russia -> Significant; mismatching nations: 2 ['Poland', 'Netherlands']; top ratio gaps [(3.37, 0), (1.667, 7), (1.667, 22)]; 2nd/3rd gap tie: True
   Reading B with successors substituted: top gaps [(3.37, 0), (1.882, 3), (1.667, 7)]; tie: False
   Russia                                     E =  10.4582 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Idelsk-Uralia (prov.)                      E =   5.8515 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Donska-Kubania (prov.)                     E =   1.7805 M   A(all comparators) = Notable      A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = Notable
   Karelia                                    E =   0.2424 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Chechnya                                   E =   0.0717 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Dagestan                                   E =   0.1533 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Ingushetia                                 E =   0.0157 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Kabardino-Balkaria                         E =   0.0488 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   Karachay-Cherkessia                        E =   0.0244 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
   North Ossetia-Alania                       E =   0.0467 M   A(all comparators) = below floor  A'(in-window comparators) = —            B(ratio gap, pools >= Notable floor) = below floor
```

**Reading the tiers (DERIVED):**
- **No successor reaches Lazar's Significant tier under either reading.** The largest, Russia (10.458M), sits below Brazil's 17M, the smallest Significant pool in Lazar's table. The pre-war Russia row is Significant at 25M (spec L42).
- **Reading B does not reproduce Lazar's current table** (2 mismatches, Poland and Netherlands, and a tie for the second-largest gap). Read it as weak evidence here. With the successors substituted, it also moves Brazil from Significant to Notable (the gap UK 32M → Brazil 17M becomes the second-largest). That is a side effect on a non-Russian nation, shown only to record how the bare gap rule behaves.
- **Seven of the ten in-window successors fall below the smallest pool in Lazar's table.** The method gives them Notable through the window rule, and states no minimum pool.

### 3.6 Sensitivities and NOT FOUND (Lazar)
**Sensitivity, split (b), one input changed at a time (percent of the former-Russia share). Bold with ▲/▼ = moves more than 5 points against the primary row; † = this successor's window membership differs from primary; '—' = recipient does not exist in that variant.** DERIVED.

| Variant | Russia | Idelsk-Uralia (prov.) | Donska-Kubania (prov.) | Siberia | Karelia | Chechnya | Dagestan | Ingushetia | Kabardino-Balkaria | Karachay-Cherkessia | North Ossetia-Alania | Kaliningrad (K-in) | Finland (Rep. of Karelia piece, C-15) | In window |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| primary | 55.95 | 31.30 | 9.52 | 0.00 | 1.30 | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania |
| V1c | 55.42 | 31.01 | 10.37 | 0.00 | 1.28 | 0.38 | 0.81 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| V2 (P × y2021, no Gini) | 59.53 | 27.93 | 9.31 | 0.00 | 1.55 | 0.28 | 0.80 | 0.07 | 0.21 | 0.11 | 0.20 | — | — | as primary |
| K-in | 55.52 | 31.07 | 9.45 | 0.00 | 1.29 | 0.38 | 0.81 | 0.08 | 0.26 | 0.13 | 0.25 | 0.76 † | — | + Kaliningrad (K-in) |
| C-15 | 55.95 | 32.21 | 9.52 | 0.00 | — | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | 0.39 † | + Finland (Rep. of Karelia piece, C-15) − Karelia |
| θ = 5% | **45.63 ▼** | **25.53 ▼** | 7.77 | **18.44 ▲** † | 1.06 | 0.31 | 0.67 | 0.07 | 0.21 | 0.11 | 0.20 | — | — | + Siberia |
| θ = 25% | 55.95 | 31.30 | 9.52 | 0.00 | 1.30 | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| official zones (S5 alt.) | 55.95 | 31.30 | 9.52 | 0.00 | 1.30 | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| territory centroid (S7 alt.) | 55.95 | 31.30 | 9.52 | 0.00 | 1.30 | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| E = P × y2024 (no Gini) | 57.11 | 30.35 | 9.49 | 0.00 | 1.19 | 0.38 | 0.81 | 0.08 | 0.25 | 0.12 | 0.24 | — | — | as primary |
| E = P only | **39.15 ▼** | **38.57 ▲** | **14.92 ▲** | 0.00 | 1.04 | 1.31 | 2.77 | 0.44 | 0.79 | 0.41 | 0.60 | — | — | as primary |

**Sensitivity, split (b-sub), one input changed at a time (percent of the former-Russia share). Bold with ▲/▼ = moves more than 5 points against the primary row; † = this successor's window membership differs from primary; '—' = recipient does not exist in that variant.** DERIVED.

| Variant | Russia | Idelsk-Uralia (prov.) | Donska-Kubania (prov.) | Siberia | Karelia | Chechnya | Dagestan | Ingushetia | Kabardino-Balkaria | Karachay-Cherkessia | North Ossetia-Alania | Kaliningrad (K-in) | Finland (Rep. of Karelia piece, C-15) | Nation-level window membership (as in split (b); b-sub counts unit-level parts) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| primary | 55.06 | 30.81 | 9.37 | 1.58 | 1.28 | 0.38 | 0.81 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania |
| V1c | 54.56 | 30.53 | 10.21 | 1.57 | 1.26 | 0.37 | 0.80 | 0.08 | 0.25 | 0.13 | 0.24 | — | — | as primary |
| V2 (P × y2021, no Gini) | 58.60 | 27.49 | 9.16 | 1.57 | 1.53 | 0.28 | 0.79 | 0.07 | 0.21 | 0.11 | 0.20 | — | — | as primary |
| K-in | 54.65 | 30.58 | 9.30 | 1.57 | 1.27 | 0.37 | 0.80 | 0.08 | 0.25 | 0.13 | 0.24 | 0.75 | — | + Kaliningrad (K-in) |
| C-15 | 55.06 | 31.70 | 9.37 | 1.58 | — | 0.38 | 0.81 | 0.08 | 0.26 | 0.13 | 0.25 | — | 0.38 | + Finland (Rep. of Karelia piece, C-15) − Karelia |
| θ = 5% | 55.06 | 30.81 | 9.37 | 1.58 | 1.28 | 0.38 | 0.81 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | + Siberia |
| θ = 25% | 55.06 | 30.81 | 9.37 | 1.58 | 1.28 | 0.38 | 0.81 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| official zones (S5 alt.) | **63.50 ▲** | **22.03 ▼** | 10.81 | 0.00 | 1.47 | 0.44 | 0.93 | 0.10 | 0.30 | 0.15 | 0.28 | — | — | as primary |
| territory centroid (S7 alt.) | 55.95 | 31.30 | 9.52 | 0.00 | 1.30 | 0.38 | 0.82 | 0.08 | 0.26 | 0.13 | 0.25 | — | — | as primary |
| E = P × y2024 (no Gini) | 56.22 | 29.88 | 9.34 | 1.56 | 1.17 | 0.37 | 0.79 | 0.07 | 0.25 | 0.12 | 0.23 | — | — | as primary |
| E = P only | **38.61 ▼** | **38.04 ▲** | **14.72 ▲** | 1.37 | 1.03 | 1.29 | 2.73 | 0.44 | 0.77 | 0.40 | 0.59 | — | — | as primary |

**Split (a) moves above 5 points (city-independent; RS1b §7):** Russia 41.83 → 31.36 (E = P only); Idelsk-Uralia (prov.) 23.41 → 30.90 (E = P only).

**Cross-product sweep (all 108 combinations of S1 {V1, V1c, V2} × S2 {K-out, K-in} × S3 {INIT, C-15} × zones {solar, centroid, official} × θ {5, 10, 25%}): which successors are in the window.** DERIVED.

| Combinations | In window | Which (listed when 12 or fewer) |
|--:|---|---|
| 24 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania | — |
| 24 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania, Finland (Rep. of Karelia piece, C-15) | — |
| 24 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania, Kaliningrad (K-in) | — |
| 24 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania, Kaliningrad (K-in), Finland (Rep. of Karelia piece, C-15) | — |
| 3 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Siberia, Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania | V1 · K-out · INIT · solar · θ 5%; V1c · K-out · INIT · solar · θ 5%; V2 · K-out · INIT · solar · θ 5% |
| 3 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Siberia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania, Finland (Rep. of Karelia piece, C-15) | V1 · K-out · C-15 · solar · θ 5%; V1c · K-out · C-15 · solar · θ 5%; V2 · K-out · C-15 · solar · θ 5% |
| 3 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Siberia, Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania, Kaliningrad (K-in) | V1 · K-in · INIT · solar · θ 5%; V1c · K-in · INIT · solar · θ 5%; V2 · K-in · INIT · solar · θ 5% |
| 3 | Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Siberia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania, Kaliningrad (K-in), Finland (Rep. of Karelia piece, C-15) | V1 · K-in · C-15 · solar · θ 5%; V1c · K-in · C-15 · solar · θ 5%; V2 · K-in · C-15 · solar · θ 5% |

**The θ = 5% case and its neighbors, computed in full** (`combos.py`; raw):

```
Lazar | V1 K-out INIT solar θ0.05: (b) Chechnya 0.31, Dagestan 0.67, Ingushetia 0.07, Kabardino-Balkaria 0.21, Karachay-Cherkessia 0.11, North Ossetia-Alania 0.20, Russia 45.63, Siberia 18.44, Idelsk-Uralia 25.53, Karelia 1.06, Donska-Kubania 7.77 || (b-sub) Chechnya 0.38, Dagestan 0.81, Ingushetia 0.08, Kabardino-Balkaria 0.26, Karachay-Cherkessia 0.13, North Ossetia-Alania 0.25, Russia 55.06, Siberia 1.58, Idelsk-Uralia 30.81, Karelia 1.28, Donska-Kubania 9.37
      counts (b) robots {'Chechnya': 182, 'Dagestan': 390, 'Ingushetia': 40, 'Kabardino-Balkaria': 124, 'Karachay-Cherkessia': 62, 'North Ossetia-Alania': 119, 'Russia': 26578, 'Siberia': 10739, 'Idelsk-Uralia': 14871, 'Karelia': 616, 'Donska-Kubania': 4525} humans {'Chechnya': 176, 'Dagestan': 376, 'Ingushetia': 39, 'Kabardino-Balkaria': 120, 'Karachay-Cherkessia': 60, 'North Ossetia-Alania': 114, 'Russia': 25673, 'Siberia': 10373, 'Idelsk-Uralia': 14364, 'Karelia': 595, 'Donska-Kubania': 4371}
Lazar | V1 K-out INIT centroid θ0.05: (b) Chechnya 0.38, Dagestan 0.82, Ingushetia 0.08, Kabardino-Balkaria 0.26, Karachay-Cherkessia 0.13, North Ossetia-Alania 0.25, Russia 55.95, Idelsk-Uralia 31.30, Karelia 1.30, Donska-Kubania 9.52 || (b-sub) Chechnya 0.38, Dagestan 0.82, Ingushetia 0.08, Kabardino-Balkaria 0.26, Karachay-Cherkessia 0.13, North Ossetia-Alania 0.25, Russia 55.95, Idelsk-Uralia 31.30, Karelia 1.30, Donska-Kubania 9.52
      counts (b) robots {'Chechnya': 223, 'Dagestan': 478, 'Ingushetia': 49, 'Kabardino-Balkaria': 152, 'Karachay-Cherkessia': 76, 'North Ossetia-Alania': 145, 'Russia': 32587, 'Idelsk-Uralia': 18233, 'Karelia': 755, 'Donska-Kubania': 5548} humans {'Chechnya': 216, 'Dagestan': 461, 'Ingushetia': 47, 'Kabardino-Balkaria': 147, 'Karachay-Cherkessia': 73, 'North Ossetia-Alania': 141, 'Russia': 31476, 'Idelsk-Uralia': 17611, 'Karelia': 730, 'Donska-Kubania': 5359}
Lazar | V1 K-out INIT official θ0.10: (b) Chechnya 0.38, Dagestan 0.82, Ingushetia 0.08, Kabardino-Balkaria 0.26, Karachay-Cherkessia 0.13, North Ossetia-Alania 0.25, Russia 55.95, Idelsk-Uralia 31.30, Karelia 1.30, Donska-Kubania 9.52 || (b-sub) Chechnya 0.44, Dagestan 0.93, Ingushetia 0.10, Kabardino-Balkaria 0.30, Karachay-Cherkessia 0.15, North Ossetia-Alania 0.28, Russia 63.50, Idelsk-Uralia 22.03, Karelia 1.47, Donska-Kubania 10.81
      counts (b) robots {'Chechnya': 223, 'Dagestan': 478, 'Ingushetia': 49, 'Kabardino-Balkaria': 152, 'Karachay-Cherkessia': 76, 'North Ossetia-Alania': 145, 'Russia': 32587, 'Idelsk-Uralia': 18233, 'Karelia': 755, 'Donska-Kubania': 5548} humans {'Chechnya': 216, 'Dagestan': 461, 'Ingushetia': 47, 'Kabardino-Balkaria': 147, 'Karachay-Cherkessia': 73, 'North Ossetia-Alania': 141, 'Russia': 31476, 'Idelsk-Uralia': 17611, 'Karelia': 730, 'Donska-Kubania': 5359}
Lazar | V2 K-in C15 solar θ0.05: (b) Chechnya 0.23, Dagestan 0.66, Ingushetia 0.06, Kabardino-Balkaria 0.18, Karachay-Cherkessia 0.09, North Ossetia-Alania 0.16, Russia 48.92, Siberia 17.26, Idelsk-Uralia 23.85, Finland (Rep. of Karelia piece, C-15) 0.37, Donska-Kubania 7.65, Kaliningrad (K-in) 0.57 || (b-sub) Chechnya 0.27, Dagestan 0.78, Ingushetia 0.07, Kabardino-Balkaria 0.21, Karachay-Cherkessia 0.11, North Ossetia-Alania 0.19, Russia 58.20, Siberia 1.55, Idelsk-Uralia 28.38, Finland (Rep. of Karelia piece, C-15) 0.44, Donska-Kubania 9.10, Kaliningrad (K-in) 0.68
      counts (b) robots {'Chechnya': 135, 'Dagestan': 384, 'Ingushetia': 35, 'Kabardino-Balkaria': 103, 'Karachay-Cherkessia': 52, 'North Ossetia-Alania': 95, 'Russia': 28494, 'Siberia': 10051, 'Idelsk-Uralia': 13894, 'Finland (Rep. of Karelia piece, C-15)': 214, 'Donska-Kubania': 4455, 'Kaliningrad (K-in)': 334} humans {'Chechnya': 130, 'Dagestan': 371, 'Ingushetia': 33, 'Kabardino-Balkaria': 99, 'Karachay-Cherkessia': 51, 'North Ossetia-Alania': 92, 'Russia': 27523, 'Siberia': 9709, 'Idelsk-Uralia': 13421, 'Finland (Rep. of Karelia piece, C-15)': 207, 'Donska-Kubania': 4303, 'Kaliningrad (K-in)': 322}
```

**Flags: every proportion that moves more than 5 points, or whose window membership changes (DERIVED):**
- **θ = 5% with solar zones: Siberia enters (b) at 18.44%, membership flag.** Its +4 share (7.11%, Tyumen' alone) clears 5%, and split (b) then admits **all** of Siberia's pool, the 92.9% at +5 and +6 included, because (b) works at nation level. Russia falls **−10.32** (55.95 → 45.63) and Idelsk-Uralia (prov.) **−5.77** (31.30 → 25.53). (b-sub) is unchanged (Siberia 1.58%), because it counts only Tyumen'. **The gap between (b) and (b-sub) for Siberia at θ = 5% (18.44 against 1.58) is the clearest case at Lazar of the footprint rule's "meaningful share" deciding a result.** It holds in 12 of the 108 combinations: solar zones and θ = 5% under every S1, S2 and S3. It does not hold under the territory centroid (Tyumen' at +5) or official zones (Siberia at {+5, +7}).
- **Official zones, (b-sub): Russia +8.44 (55.06 → 63.50) and Idelsk-Uralia (prov.) −8.78 (30.81 → 22.03).** Under official zones Idelsk-Uralia's Ural and Bashkir units sit at UTC+5 (RS1b §4: 38.0% of its pool), at distance 4 from Lazar, so they drop out at unit level. Siberia's Tyumen' (official +5) drops out too. Nation-level (b) does not move.
- **E = P only:** (b) Russia −16.80, Idelsk-Uralia +7.27, Donska-Kubania +5.40; (b-sub) Russia −16.45, Idelsk-Uralia +7.23, Donska-Kubania +5.35; (a) Russia −10.47, Idelsk-Uralia +7.49.
- **No other coordinator alternative (V1c, V2, K-in, C-15, θ 25%, territory centroid) moves any successor by more than 5 points at Lazar.** The largest is V2: (b) Russia +3.58, Idelsk-Uralia −3.37. K-in adds Kaliningrad (solar +1, d = 0) at 0.57 to 0.76%. C-15 replaces Karelia with Finland's Republic-of-Karelia piece (0.31 to 0.45%).
- **(b) ranges across all 108 combinations** (raw, `out_sweep.txt`): Russia 45.01 to 59.53 · Idelsk-Uralia (prov.) 22.95 to 32.21 · Siberia 0.00 to 18.44 · Donska-Kubania (prov.) 7.65 to 10.37 · Karelia 1.04 to 1.55 · each North Caucasus republic under 1%.

**NOT FOUND (Lazar):** the meaningful-share threshold θ (decisive here: Siberia's 7.11% at +4 sits between the 5% and 10% sweep values) · the "small pool" cut · a minimum pool for Notable · the Gini penalty's functional form · any First Interwar population, GRP or Gini for any successor. Inherited input gaps: RS1b §8.

---

## 4 · Concordia

### 4.1 The city's own inputs
- **Position:** ~75°06'S 123°20'E (`Specs/Janbogo subnet/Concordia.md` L3; SOURCED). 123.333 ÷ 15 = 8.222 → **solar zone +8** (DERIVED; 0.278 of a zone, about 4.2°, from the nearest boundary). **Window: +5 … +11.**
- **Russia in Concordia's spec:** **Primary** tier, **9.20%**, Census I **48,123 robots / 47,572 humans** (spec L19, L33; SOURCED, matches the brief's table).
- **`Upper_Earth_Immigration_Composition.md` has no Concordia section** (searched for "Concordia": no match). Concordia's tier table is therefore taken from its spec only (L17–21).

### 4.2 Which successors lie inside the window
**Membership table (primary: V1 · K-out · INIT · solar zones, S7 · θ = 10%).** Window = solar +5 … +11. W in trillion rubles of Gini-adjusted GRP (RS1b §6.1). DERIVED.

| Successor | W (tn RUB) | Zone profile q(z) | Meaningful zones Z(10%) | Distance d | In window? | In-window part of W (unit level, tn) |
|---|--:|---|---|--:|---|--:|
| Russia | 47.726 | +2: 28.8% · +3: 71.2% | {+2, +3} | 5 | out | 0.000 |
| Idelsk-Uralia (prov.) | 26.704 | +3: 57.1% · +4: 42.9% | {+3, +4} | 4 | out | 0.000 |
| Donska-Kubania (prov.) | 8.125 | +3: 100.0% | {+3} | 5 | out | 0.000 |
| Künnarantaiga | 9.402 | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7, +9, +10} | 1 | **IN** | 9.271 |
| Siberia | 19.284 | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5, +6} | 2 | **IN** | 17.912 |
| Tuva | 0.096 | +6: 100.0% | {+6} | 2 | **IN** | 0.096 |
| Karelia | 1.106 | +2: 100.0% | {+2} | 6 | out | 0.000 |
| Chechnya | 0.327 | +3: 100.0% | {+3} | 5 | out | 0.000 |
| Dagestan | 0.700 | +3: 100.0% | {+3} | 5 | out | 0.000 |
| Ingushetia | 0.072 | +3: 100.0% | {+3} | 5 | out | 0.000 |
| Kabardino-Balkaria | 0.223 | +3: 100.0% | {+3} | 5 | out | 0.000 |
| Karachay-Cherkessia | 0.111 | +3: 100.0% | {+3} | 5 | out | 0.000 |
| North Ossetia-Alania | 0.213 | +3: 100.0% | {+3} | 5 | out | 0.000 |
| **Total** | 114.089 | | | | in-window W = **28.782** | **27.279** |

**Reading the table (DERIVED):**
- **Inside (3):** **Künnarantaiga** (d = 1, through +7 (Irkutsk, Buryatia) and +9; its +8 units, Chita alone at S7, hold 6.4%, below θ), **Siberia** (d = 2 through +6; its +5 units are also inside, at d = 3), **Tuva** (+6, d = 2).
- **Outside (10):** Idelsk-Uralia (prov.) (d = 4, through its +4 Ural and Bashkir units), Russia (d = 5), Donska-Kubania (prov.) and the six North Caucasus republics (d = 5), Karelia (d = 6).
- **The window's western edge, +5, is the line that matters at Concordia.** Siberia's +5 units (Khanty-Mansiy, Yamal-Nenets, Omsk) sit exactly at d = 3. No Idelsk-Uralia unit reaches +5 under solar zones: its easternmost S7 city is Kurgan (65.34°E, 2.16° short of the +4/+5 boundary at 67.5°E), and even Kurgan at +5 would be only 1.19% of Idelsk-Uralia's pool (DERIVED: 776,661 × 615.394 × (1 − 0.337) = 0.317 trillion of 26.704).
- **At unit level (b-sub)** only two units fall away: Chukotka (+12, d = 4, 1.4% of Künnarantaiga) and Tyumen' (+4, d = 4, 7.1% of Siberia).

**Knife-edges, shown explicitly (the brief asks for them at Concordia in particular; RS1b §4).** Each unit flipped across its nearest zone boundary, one at a time, primary variant. Lines with no effect at all are omitted. The four RS1b-named V1 cases are always shown. 35 units were scanned within 3° of a boundary:

```
-- KNIFE-EDGE scan, Concordia (primary variant): every unit whose S7 city lies within 3.0° of a zone boundary, flipped one at a time
   unit                     place                       lon  lon/15   z  ->  margin°  effect on membership / (b)
   Moskva                   Moscow                    37.61   2.507  +3  +2     0.11  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Tula                     Tula                      37.63   2.509  +3  +2     0.13  no membership change | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Sakha (Yakutia)          Yakutsk                  129.74   8.649  +9  +8     2.24  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 8, 9, 10] d1->0 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Amur                     Blagoveshchensk          127.53   8.502  +9  +8     0.03  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 8, 9, 10] d1->0 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Sakhalin                 Yuzhno Sakhalinsk        142.74   9.516 +10  +9     0.24  no membership change | Künnarantaiga Z [7, 9, 10]->[7, 9] d1->1 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Tyumen'                  Tyumen                    65.53   4.369  +4  +5     1.97  no membership change | max (b) move 0.00 pp | max (b-sub) move 1.64 pp (Siberia)
   Kurgan                   Kurgan                    65.34   4.356  +4  +5     2.16  no membership change | max (b) move 0.00 pp | max (b-sub) move 1.15 pp (Idelsk-Uralia)
   Krasnodar                Krasnodar                 39.00   2.600  +3  +2     1.50  no membership change | Donska-Kubania Z [3]->[2, 3] d5->5 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   Rostov                   Rostov                    39.71   2.647  +3  +2     2.21  no membership change | Donska-Kubania Z [3]->[2, 3] d5->5 | max (b) move 0.00 pp | max (b-sub) move 0.00 pp
   [scan lines in total: 35]
```

| RS1b knife-edge | Longitude, margin | At its S7 zone | If it fell the other way | Decides membership at Concordia? |
|---|---|---|---|---|
| **Blagoveshchensk** (Amur) | 127.53°E, 0.03° east of the +8/+9 boundary | +9: Künnarantaiga +8 share 6.4%, below θ; d = 1 (through +7 and +9) | +8: Künnarantaiga +8 share 13.3% (RS1b §4), a meaningful zone; d = 0 | **No.** Künnarantaiga is inside either way; (b) and (b-sub) do not move, because both +8 and +9 lie inside the window |
| **Yuzhno-Sakhalinsk** (Sakhalin) | 142.74°E, 0.24° east of the +9/+10 boundary | +10: Künnarantaiga Z = {+7, +9, +10} | +9: +10 falls to 3.4% (RS1b §4), Z = {+7, +9} | **No.** d stays 1; +9 and +10 both lie inside the window |
| **Moscow** (Moskva) | 37.61°E, 0.11° east of the +2/+3 boundary | +3: Russia's profile +2 28.8% / +3 71.2%; d = 5 | +2: profile +2 78.5% / +3 21.5% (RS1b §4); +3 still meaningful, d stays 5 | **No.** Russia's easternmost territory is at 43.2°E (RS1 §1.2), solar +3 at most, so no zone assignment of any Russia unit can bring it within 3 of +8 |
| **Tula** | 37.63°E, 0.13° | +3 | +2 | **No** (as Moscow) |

**What does decide membership at Concordia is not a knife-edge but the zone convention (S5), set out in 4.6:** under official zones the Ural and Bashkir units of Idelsk-Uralia (prov.) sit at UTC+5, and Idelsk-Uralia enters the window.

### 4.3 The division of Concordia's Russia share
**Split of the former-Russia share (percent of that share; each column sums to 100).** (a) = W_k ÷ ΣW; (b) = W_k × I_k ÷ Σ W_j × I_j; (b-sub) = in-window part of W_k ÷ Σ in-window parts. DERIVED.

| Successor | (a) | (b) | (b-sub) |
|---|--:|--:|--:|
| Russia | 41.83% | 0.00% | 0.00% |
| Idelsk-Uralia (prov.) | 23.41% | 0.00% | 0.00% |
| Donska-Kubania (prov.) | 7.12% | 0.00% | 0.00% |
| Künnarantaiga | 8.24% | 32.67% | 33.98% |
| Siberia | 16.90% | 67.00% | 65.66% |
| Tuva | 0.08% | 0.33% | 0.35% |
| Karelia | 0.97% | 0.00% | 0.00% |
| Chechnya | 0.29% | 0.00% | 0.00% |
| Dagestan | 0.61% | 0.00% | 0.00% |
| Ingushetia | 0.06% | 0.00% | 0.00% |
| Kabardino-Balkaria | 0.20% | 0.00% | 0.00% |
| Karachay-Cherkessia | 0.10% | 0.00% | 0.00% |
| North Ossetia-Alania | 0.19% | 0.00% | 0.00% |
| **Sum** | 100.00% | 100.00% | 100.00% |

**Worked inputs (DERIVED):** in-window total = 9.402 (Künnarantaiga) + 19.284 (Siberia) + 0.096 (Tuva) = 28.782; (b) Siberia = 19.284 ÷ 28.782 = 67.00%; Künnarantaiga = 9.402 ÷ 28.782 = 32.67%; Tuva = 0.096 ÷ 28.782 = 0.33%. (b-sub): Künnarantaiga 9.271 (without Chukotka) and Siberia 17.912 (without Tyumen'), total 27.279. **Under (a), 74.77% of the share** (100 − 8.24 Künnarantaiga − 16.90 Siberia − 0.08 Tuva, unrounded: Russia, Idelsk-Uralia, Donska-Kubania, Karelia and the six republics) **goes to successors outside Concordia's window.** Split (a) is the RS1b city-independent split unchanged.

Raw script output (primary):

```
-- PRIMARY (V1 . K-out . INIT . solar S7 . theta 10% . E = P x y2024 x (1-G2022)); W in trillion RUB
successor                                     W(tn) q(z) %                                   Z(10%)           d  in?    (a)%    (b)%   Wc(tn) (b-sub)%
Russia                                       47.726 +2:28.8 +3:71.2                          [2, 3]           5  out   41.83    0.00    0.000     0.00
Idelsk-Uralia (prov.)                        26.704 +3:57.1 +4:42.9                          [3, 4]           4  out   23.41    0.00    0.000     0.00
Donska-Kubania (prov.)                        8.125 +3:100.0                                 [3]              5  out    7.12    0.00    0.000     0.00
Künnarantaiga                                 9.402 +7:24.9 +8:6.4 +9:49.6 +10:14.5 +11:3.2 +12:1.4 [7, 9, 10]       1   IN    8.24   32.67    9.271    33.98
Siberia                                      19.284 +4:7.1 +5:53.6 +6:39.3                   [5, 6]           2   IN   16.90   67.00   17.912    65.66
Tuva                                          0.096 +6:100.0                                 [6]              2   IN    0.08    0.33    0.096     0.35
Karelia                                       1.106 +2:100.0                                 [2]              6  out    0.97    0.00    0.000     0.00
Chechnya                                      0.327 +3:100.0                                 [3]              5  out    0.29    0.00    0.000     0.00
Dagestan                                      0.700 +3:100.0                                 [3]              5  out    0.61    0.00    0.000     0.00
Ingushetia                                    0.072 +3:100.0                                 [3]              5  out    0.06    0.00    0.000     0.00
Kabardino-Balkaria                            0.223 +3:100.0                                 [3]              5  out    0.20    0.00    0.000     0.00
Karachay-Cherkessia                           0.111 +3:100.0                                 [3]              5  out    0.10    0.00    0.000     0.00
North Ossetia-Alania                          0.213 +3:100.0                                 [3]              5  out    0.19    0.00    0.000     0.00
TOTAL                                       114.089   in-window W = 28.782 tn ; b-sub in-window W = 27.279 tn

-- COUNTS (a), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Russia                                      41.8327    20131.145   20131    19900.647   19901
Idelsk-Uralia (prov.)                       23.4062    11263.745   11264    11134.777   11135
Donska-Kubania (prov.)                       7.1218     3427.234    3427     3387.992    3388
Künnarantaiga                                8.2407     3965.669    3966     3920.263    3920
Siberia                                     16.9023     8133.899    8134     8040.767    8041
Tuva                                         0.0845       40.646      41       40.181      40
Karelia                                      0.9696      466.608     466      461.266     461
Chechnya                                     0.2868      137.994     138      136.414     136
Dagestan                                     0.6132      295.091     295      291.712     292
Ingushetia                                   0.0629       30.293      30       29.946      30
Kabardino-Balkaria                           0.1950       93.864      94       92.789      93
Karachay-Cherkessia                          0.0975       46.930      47       46.392      46
North Ossetia-Alania                         0.1868       89.882      90       88.853      89
SUM                                                                48123                47572

-- COUNTS (b), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Künnarantaiga                               32.6656    15719.648   15720    15539.661   15540
Siberia                                     66.9996    32242.234   32242    31873.066   31873
Tuva                                         0.3348      161.118     161      159.273     159
SUM                                                                48123                47572

-- COUNTS (b-sub), Hamilton (largest remainder; ties to larger W)
successor                                       p %  robot quota  robots  human quota  humans
Künnarantaiga                               33.9844    16354.307   16354    16167.053   16167
Siberia                                     65.6624    31598.701   31599    31236.901   31237
Tuva                                         0.3532      169.993     170      168.046     168
SUM                                                                48123                47572
```

### 4.4 Draft counts for Concordia
**Draft counts, Census I (former-Russia robots 48,123, humans 47,572).** Largest remainder (Hamilton): each successor gets floor(total × p); the units left over go one each to the largest fractional remainders, ties to the larger W. DERIVED.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans | (b-sub) robots | (b-sub) humans |
|---|--:|--:|--:|--:|--:|--:|
| Russia | 20,131 | 19,901 | 0 | 0 | 0 | 0 |
| Idelsk-Uralia (prov.) | 11,264 | 11,135 | 0 | 0 | 0 | 0 |
| Donska-Kubania (prov.) | 3,427 | 3,388 | 0 | 0 | 0 | 0 |
| Künnarantaiga | 3,966 | 3,920 | 15,720 | 15,540 | 16,354 | 16,167 |
| Siberia | 8,134 | 8,041 | 32,242 | 31,873 | 31,599 | 31,237 |
| Tuva | 41 | 40 | 161 | 159 | 170 | 168 |
| Karelia | 466 | 461 | 0 | 0 | 0 | 0 |
| Chechnya | 138 | 136 | 0 | 0 | 0 | 0 |
| Dagestan | 295 | 292 | 0 | 0 | 0 | 0 |
| Ingushetia | 30 | 30 | 0 | 0 | 0 | 0 |
| Kabardino-Balkaria | 94 | 93 | 0 | 0 | 0 | 0 |
| Karachay-Cherkessia | 47 | 46 | 0 | 0 | 0 | 0 |
| North Ossetia-Alania | 90 | 89 | 0 | 0 | 0 | 0 |
| **Sum** | **48,123** | **47,572** | **48,123** | **47,572** | **48,123** | **47,572** |

### 4.5 Effective tier of each successor at Concordia (informational, not ruled)
**Concordia's own table** (`Specs/Janbogo subnet/Concordia.md` L17–21), with pools from `UEIC` L65–110: **Primary** China (210M), Japan (65), South Korea (26), Russia (25), Indonesia (16), Australia (13) · **Significant** USA (155), Thailand (8), Vietnam (5), Philippines (5), Malaysia (5), New Zealand (2.6), Belarus (1.5) · **Notable** Germany (46), France (35), UK (32), Italy (27), Canada (20), Spain (20), Mexico (18), Poland (12) … Latvia and Estonia (0.6).

**Concordia's table is not ordered by pool alone.** USA (155M) is Significant below Australia (13M, Primary), and Germany (46M) is Notable. The pattern follows the window. Every Primary member lies inside the window (by capital or main city, DERIVED from the NE file: China +8 (Beijing 7.76, Shanghai 8.10; also `UEIC` L57), Japan +9 (Tokyo 9.32), South Korea +8 (Seoul 8.47), Indonesia +7 (Jakarta 7.12; `UEIC` L57), Australia +8 (Perth 7.72; `UEIC` L57)). Every Notable member lies outside it (capitals at +2 or less, or in the Americas: distance 6 to 15, DERIVED, `ne_eu.py`). So **Reading A′ (in-window comparators only) is the main reading at Concordia**, and Reading A and B are shown beside it.

- **In-window comparators (DERIVED):** Primary China, Japan, South Korea, Indonesia, Australia (floor **13M**); Significant Thailand (+7, Bangkok 6.70), Vietnam (+7), Philippines (+8, Manila 8.07), Malaysia (+7, Kuala Lumpur 6.78), and New Zealand **only through the gateway exception** (Wellington and Auckland 11.65 → +12, d = 4; `UEIC` L32–33 places New Zealand *"across the Mirny subnet 'via Hobart'"*, Hobart 9.82 → +10, d = 2). **Whether that gateway applies at Concordia (Janbogo subnet) is not stated: NOT FOUND.** In-window Significant floor: **2.6M with New Zealand, 5M without.** In-window Notable members: **none**. Out of window: USA (Washington −5, d = 13) and Belarus (Minsk +2, d = 6), both Significant.
- **Floors, all comparators (DERIVED):** Primary 13M · Significant 1.5M (Belarus) · Notable 0.6M.

| Successor | Ê (M) | d | Reading A′ (in-window comparators) | Reading A (all comparators) | Reading B (ratio gap, pools ≥ 0.6M) | Note |
|---|--:|--:|---|---|---|---|
| Siberia | 4.226 | 2 | **Significant** if New Zealand counts through the gateway (≥ 2.6M); **Notable** (window rule) if not (< 5M) | Significant | Significant | in window |
| Künnarantaiga | 2.060 | 1 | **Notable** (window rule; below 2.6M). The raw block prints "below floor": below the in-window Significant floor, with no in-window Notable comparator to band against | Significant | Significant | in window |
| Tuva | 0.021 | 2 | Notable (window rule) | below floor | below floor | in window; below every pool in Concordia's table; no minimum stated (NOT FOUND) |
| Russia | 10.458 | 5 | — (out of window) | Significant | Significant | appears only in split (a). Concordia's own table holds out-of-window nations in Significant (USA, Belarus) and Notable (down to 0.6M), so at this city the d ≤ 3 condition does not visibly exclude a pool of this size |
| Idelsk-Uralia (prov.) | 5.852 | 4 (3 under official zones) | — (out); **Significant** under official zones | Significant | Significant | in window under official zones only |
| Donska-Kubania (prov.) | 1.781 | 5 | — (out) | Significant | Significant | as Russia |
| Karelia, six North Caucasus republics | 0.016 to 0.242 | 5 to 6 | — (out) | below floor | below floor | out of window and below the 0.6M floor |

**Raw tier output** (Reading A′ column computed with New Zealand counted in window):

```
tiers for split (a) presence (all successors):
   Reading B UNRESTRICTED (micro-pools included) top gaps [(2.475, 41), (2.385, 1), (2.138, 43)] -> Russia core would be Significant; shown only to record why B is restricted to pools >= the city's Notable floor

-- TIERS, Concordia: floors (all comparators) {'Primary': 13, 'Significant': 1.5, 'Notable': 0.6}; in-window floors {'Primary': 13, 'Significant': 2.6, 'Notable': None}
   Reading B reproduction check on the city's current list (Russia 25M): pre-war Russia -> Significant; mismatching nations: 28 ['Japan', 'SouthKorea', 'Indonesia', 'Australia', 'USA', 'Germany', 'France', 'UK', 'Italy', 'Canada', 'Spain', 'Mexico', 'Poland', 'Netherlands', 'Belgium', 'Sweden', 'Czech', 'Ukraine', 'Romania', 'Norway', 'Finland', 'Hungary', 'Slovakia', 'Croatia', 'Bulgaria', 'Serbia', 'Lithuania', 'Slovenia']; top ratio gaps [(2.385, 1), (1.667, 35), (1.467, 29)]; 2nd/3rd gap tie: False
   Reading B with successors substituted: top gaps [(2.385, 1), (1.667, 39), (1.413, 2)]; tie: False
   Russia                                     E =  10.4582 M   A(all comparators) = Significant  A'(in-window comparators) = Significant  B(ratio gap, pools >= Notable floor) = Significant
   Idelsk-Uralia (prov.)                      E =   5.8515 M   A(all comparators) = Significant  A'(in-window comparators) = Significant  B(ratio gap, pools >= Notable floor) = Significant
   Donska-Kubania (prov.)                     E =   1.7805 M   A(all comparators) = Significant  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = Significant
   Künnarantaiga                              E =   2.0602 M   A(all comparators) = Significant  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = Significant
   Siberia                                    E =   4.2256 M   A(all comparators) = Significant  A'(in-window comparators) = Significant  B(ratio gap, pools >= Notable floor) = Significant
   Tuva                                       E =   0.0211 M   A(all comparators) = below floor  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = below floor
   Karelia                                    E =   0.2424 M   A(all comparators) = below floor  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = below floor
   Chechnya                                   E =   0.0717 M   A(all comparators) = below floor  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = below floor
   Dagestan                                   E =   0.1533 M   A(all comparators) = below floor  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = below floor
   Ingushetia                                 E =   0.0157 M   A(all comparators) = below floor  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = below floor
   Kabardino-Balkaria                         E =   0.0488 M   A(all comparators) = below floor  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = below floor
   Karachay-Cherkessia                        E =   0.0244 M   A(all comparators) = below floor  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = below floor
   North Ossetia-Alania                       E =   0.0467 M   A(all comparators) = below floor  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = below floor

tiers for split (b) presence (in-window successors only):
   Reading B UNRESTRICTED (micro-pools included) top gaps [(28.415, 38), (2.385, 1), (1.667, 36)] -> Russia core would be —; shown only to record why B is restricted to pools >= the city's Notable floor

-- TIERS, Concordia: floors (all comparators) {'Primary': 13, 'Significant': 1.5, 'Notable': 0.6}; in-window floors {'Primary': 13, 'Significant': 2.6, 'Notable': None}
   Reading B reproduction check on the city's current list (Russia 25M): pre-war Russia -> Significant; mismatching nations: 28 ['Japan', 'SouthKorea', 'Indonesia', 'Australia', 'USA', 'Germany', 'France', 'UK', 'Italy', 'Canada', 'Spain', 'Mexico', 'Poland', 'Netherlands', 'Belgium', 'Sweden', 'Czech', 'Ukraine', 'Romania', 'Norway', 'Finland', 'Hungary', 'Slovakia', 'Croatia', 'Bulgaria', 'Serbia', 'Lithuania', 'Slovenia']; top ratio gaps [(2.385, 1), (1.667, 35), (1.467, 29)]; 2nd/3rd gap tie: False
   Reading B with successors substituted: top gaps [(2.385, 1), (1.667, 36), (1.413, 2)]; tie: False
   Künnarantaiga                              E =   2.0602 M   A(all comparators) = Significant  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = Significant
   Siberia                                    E =   4.2256 M   A(all comparators) = Significant  A'(in-window comparators) = Significant  B(ratio gap, pools >= Notable floor) = Significant
   Tuva                                       E =   0.0211 M   A(all comparators) = below floor  A'(in-window comparators) = below floor  B(ratio gap, pools >= Notable floor) = below floor
```

**Reading the tiers (DERIVED):**
- **No successor reaches Concordia's Primary floor (13M, Australia) under any reading.** The pre-war Russia row is Primary at 25M (spec L19); the largest successor, Russia (10.458M), is outside the window, and the largest in-window successor, Siberia, is 4.226M. **Under the method's tier rule, the former Primary-tier Russia share at Concordia would sit, after the split, in Significant or Notable successors only.** This is informational, not ruled.
- **Reading B does not reproduce Concordia's current table** (28 of 37 nations mismatch), because the table follows the window rather than the bare pool ranking. Reading B carries little weight here.
- **The New Zealand gateway question decides Siberia's tier** (Significant or Notable) under Reading A′. That question is about a non-Russian nation and is NOT FOUND in the method; it is reported, not resolved.

### 4.6 Sensitivities and NOT FOUND (Concordia)
**Sensitivity, split (b), one input changed at a time (percent of the former-Russia share). Bold with ▲/▼ = moves more than 5 points against the primary row; † = this successor's window membership differs from primary; '—' = recipient does not exist in that variant.** DERIVED.

| Variant | Idelsk-Uralia (prov.) | Künnarantaiga | Siberia | Tuva | In window |
|---|--:|--:|--:|--:|---|
| primary | 0.00 | 32.67 | 67.00 | 0.33 | Künnarantaiga, Siberia, Tuva |
| V1c | 0.00 | 32.67 | 67.00 | 0.33 | as primary |
| V2 (P × y2021, no Gini) | 0.00 | 31.39 | 68.30 | 0.31 | as primary |
| K-in | 0.00 | 32.67 | 67.00 | 0.33 | as primary |
| C-15 | 0.00 | 32.67 | 67.00 | 0.33 | as primary |
| θ = 5% | 0.00 | 32.67 | 67.00 | 0.33 | as primary |
| θ = 25% | 0.00 | 32.67 | 67.00 | 0.33 | as primary |
| official zones (S5 alt.) | **48.13 ▲** † | **16.94 ▼** | **34.75 ▼** | 0.17 | + Idelsk-Uralia (prov.) |
| territory centroid (S7 alt.) | 0.00 | 32.67 | 67.00 | 0.33 | as primary |
| E = P × y2024 (no Gini) | 0.00 | 32.20 | 67.48 | 0.33 | as primary |
| E = P only | 0.00 | 36.18 | 62.64 | 1.18 | as primary |

**Sensitivity, split (b-sub), one input changed at a time (percent of the former-Russia share). Bold with ▲/▼ = moves more than 5 points against the primary row; † = this successor's window membership differs from primary; '—' = recipient does not exist in that variant.** DERIVED.

| Variant | Idelsk-Uralia (prov.) | Künnarantaiga | Siberia | Tuva | Nation-level window membership (as in split (b); b-sub counts unit-level parts) |
|---|--:|--:|--:|--:|---|
| primary | 0.00 | 33.98 | 65.66 | 0.35 | Künnarantaiga, Siberia, Tuva |
| V1c | 0.00 | 33.98 | 65.66 | 0.35 | as primary |
| V2 (P × y2021, no Gini) | 0.00 | 32.78 | 66.89 | 0.32 | as primary |
| K-in | 0.00 | 33.98 | 65.66 | 0.35 | as primary |
| C-15 | 0.00 | 33.98 | 65.66 | 0.35 | as primary |
| θ = 5% | 0.00 | 33.98 | 65.66 | 0.35 | as primary |
| θ = 25% | 0.00 | 33.98 | 65.66 | 0.35 | as primary |
| official zones (S5 alt.) | **26.35 ▲** | **23.30 ▼** | **50.09 ▼** | 0.25 | + Idelsk-Uralia (prov.) |
| territory centroid (S7 alt.) | 0.00 | 32.36 | 67.31 | 0.34 | as primary |
| E = P × y2024 (no Gini) | 0.00 | 33.45 | 66.20 | 0.34 | as primary |
| E = P only | 0.00 | 38.22 | **60.53 ▼** | 1.25 | as primary |

**Split (a) moves above 5 points (city-independent; RS1b §7):** Russia 41.83 → 31.36 (E = P only); Idelsk-Uralia (prov.) 23.41 → 30.90 (E = P only).

**Cross-product sweep (all 108 combinations of S1 {V1, V1c, V2} × S2 {K-out, K-in} × S3 {INIT, C-15} × zones {solar, centroid, official} × θ {5, 10, 25%}): which successors are in the window.** DERIVED.

| Combinations | In window | Which (listed when 12 or fewer) |
|--:|---|---|
| 72 | Künnarantaiga, Siberia, Tuva | — |
| 36 | Idelsk-Uralia (prov.), Künnarantaiga, Siberia, Tuva | — |

**Flags: every proportion that moves more than 5 points, or whose window membership changes (DERIVED):**
- **Official zones (S5 alternative): Idelsk-Uralia (prov.) enters the window, membership flag, at 48.13% of the share in (b).** Under official zones its Ural and Bashkir units (Sverdlovsk, Chelyabinsk, Kurgan, Orenburg, Perm', Bashkortostan) are UTC+5, 38.0% of its pool (RS1b §6.3), at distance 3. (b) becomes Idelsk-Uralia **48.13 (+48.13)** · Siberia **34.75 (−32.25)** · Künnarantaiga **16.94 (−15.73)** · Tuva 0.17. (b-sub) becomes Idelsk-Uralia **26.35 (+26.35)** · Siberia **50.09 (−15.57)** · Künnarantaiga **23.30 (−10.68)** · Tuva 0.25. **This holds in all 36 official-zone combinations of the sweep** and in none of the other 72.
- **The method's own source used official zones for Russia.** `UEIC` L38–41 (and the Relung Panen row it cites) scores Russia's footprint with *"Novosibirsk … Krasnoyarsk … at UTC+7"*, which are legal zones, not solar ones (RS1 §4.2, flagged there, not resolved). So the official-zone result is not a remote alternative at Concordia: it is the convention the footprint rule was first written in. **Which convention applies is a developer choice (S5), and at Concordia it decides whether Idelsk-Uralia is in the window at all.**
- **E = P only:** (b-sub) Siberia **−5.13** (65.66 → 60.53), flag; (b) Siberia −4.36 and Künnarantaiga +3.51 (under the flag); (a) Russia −10.47 and Idelsk-Uralia +7.49 (RS1b §7.2).
- **No other alternative (V1c, V2, K-in, C-15, θ 5% or 25%, territory centroid) moves any successor by more than 5 points at Concordia, or changes membership.** V1c, K-in and C-15 add, move or remove pools that are all outside this window, so (b) is unchanged under them. V2 moves (b) Siberia +1.30. θ changes Künnarantaiga's meaningful zones (at 5% it gains +8, d = 0; at 25% only +9 remains, d = 1) but never its membership.
- **(b) ranges across all 108 combinations** (raw, `out_sweep.txt`): Siberia 34.28 to 68.30 · Künnarantaiga 16.15 to 32.67 · Idelsk-Uralia (prov.) 0.00 to 48.84 · Tuva 0.16 to 0.33.

**Draft counts under official zones** (the one alternative that changes membership here; DERIVED, same rounding rule):

| Successor (official zones) | Z(10%) | d | (b) | (b) robots | (b) humans | (b-sub) | (b-sub) robots | (b-sub) humans |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| Idelsk-Uralia (prov.) | {+3, +4, +5} | 3 | 48.13% | 23,160 | 22,895 | 26.35% | 12,682 | 12,536 |
| Künnarantaiga | {+8, +9, +10, +11} | 0 | 16.94% | 8,154 | 8,061 | 23.30% | 11,214 | 11,086 |
| Siberia | {+5, +7} | 1 | 34.75% | 16,725 | 16,533 | 50.09% | 24,107 | 23,831 |
| Tuva | {+7} | 1 | 0.17% | 84 | 83 | 0.25% | 120 | 119 |
| **Sum** | | | 100.00% | **48,123** | **47,572** | 100.00% | **48,123** | **47,572** |

**NOT FOUND (Concordia):** a Concordia section in `Upper_Earth_Immigration_Composition.md` (none exists; the spec's table is the only tier source) · whether solar or official zones are meant for a nation's footprint (**decisive here**) · whether the New Zealand gateway (`UEIC` L32–33) applies at Concordia (decides Siberia's tier under Reading A′) · the meaningful-share threshold θ · the "small pool" cut · a minimum pool for Notable · the Gini penalty's functional form · any First Interwar population, GRP or Gini for any successor. Inherited input gaps: RS1b §8.

---

## FINAL

**Draft arithmetic only. Nothing here is a ruling or a recommendation; no spec, census or composition file was touched.** Every figure is a present-day real-world regional figure aggregated to the successors (DERIVED), standing in for the First Interwar record, which does not exist yet. Idelsk-Uralia and Donska-Kubania are provisional names.

### F.1 One table per city (primary: V1 · K-out · INIT · solar · S7 · θ 10% · E = P × y2024 × (1 − G2022))
(a) = by pool alone; (b) = by pool within the window (nation level); (b-sub) = the in-window part of each pool (unit level). Counts are Census I, largest remainder; the (a) and (b-sub) counts are in each city's §n.4. The tier reading is informational (§0.2): Reading A, or A′ at Concordia.

**Troll** (solar +0; window -3 … +3; former Russia 48,477 robots / 48,216 humans; full tables §1.3 to §1.4)

| Successor | d | Window | (a) | (b) | (b) robots | (b) humans | (b-sub) | Tier reading (in window) |
|---|--:|---|--:|--:|--:|--:|--:|---|
| Russia | 2 | IN | 41.83% | 55.95% | 27,121 | 26,975 | 64.62% | Notable |
| Idelsk-Uralia (prov.) | 3 | IN | 23.41% | 31.30% | 15,175 | 15,093 | 20.66% | Notable |
| Donska-Kubania (prov.) | 3 | IN | 7.12% | 9.52% | 4,617 | 4,592 | 11.00% | Notable |
| Künnarantaiga | 7 | out | 8.24% | 0.00% | 0 | 0 | 0.00% | — |
| Siberia | 5 | out | 16.90% | 0.00% | 0 | 0 | 0.00% | — |
| Tuva | 6 | out | 0.08% | 0.00% | 0 | 0 | 0.00% | — |
| Karelia | 2 | IN | 0.97% | 1.30% | 629 | 625 | 1.50% | below floor; Notable by window rule only (no minimum stated) |
| Chechnya | 3 | IN | 0.29% | 0.38% | 186 | 185 | 0.44% | below floor; Notable by window rule only (no minimum stated) |
| Dagestan | 3 | IN | 0.61% | 0.82% | 398 | 395 | 0.95% | below floor; Notable by window rule only (no minimum stated) |
| Ingushetia | 3 | IN | 0.06% | 0.08% | 41 | 41 | 0.10% | below floor; Notable by window rule only (no minimum stated) |
| Kabardino-Balkaria | 3 | IN | 0.20% | 0.26% | 126 | 126 | 0.30% | below floor; Notable by window rule only (no minimum stated) |
| Karachay-Cherkessia | 3 | IN | 0.10% | 0.13% | 63 | 63 | 0.15% | below floor; Notable by window rule only (no minimum stated) |
| North Ossetia-Alania | 3 | IN | 0.19% | 0.25% | 121 | 121 | 0.29% | below floor; Notable by window rule only (no minimum stated) |
| **Sum** | | | 100.00% | 100.00% | **48,477** | **48,216** | 100.00% | |

**Santa Luce** (solar -1; window -4 … +2; former Russia 20,229 robots / 19,330 humans; full tables §2.3 to §2.4)

| Successor | d | Window | (a) | (b) | (b) robots | (b) humans | (b-sub) | Tier reading (in window) |
|---|--:|---|--:|--:|--:|--:|--:|---|
| Russia | 3 | IN | 41.83% | 97.73% | 19,771 | 18,892 | 92.55% | Notable |
| Idelsk-Uralia (prov.) | 4 | out | 23.41% | 0.00% | 0 | 0 | 0.00% | — |
| Donska-Kubania (prov.) | 4 | out | 7.12% | 0.00% | 0 | 0 | 0.00% | — |
| Künnarantaiga | 8 | out | 8.24% | 0.00% | 0 | 0 | 0.00% | — |
| Siberia | 6 | out | 16.90% | 0.00% | 0 | 0 | 0.00% | — |
| Tuva | 7 | out | 0.08% | 0.00% | 0 | 0 | 0.00% | — |
| Karelia | 3 | IN | 0.97% | 2.27% | 458 | 438 | 7.45% | below floor; Notable by window rule only (no minimum stated) |
| Chechnya | 4 | out | 0.29% | 0.00% | 0 | 0 | 0.00% | — |
| Dagestan | 4 | out | 0.61% | 0.00% | 0 | 0 | 0.00% | — |
| Ingushetia | 4 | out | 0.06% | 0.00% | 0 | 0 | 0.00% | — |
| Kabardino-Balkaria | 4 | out | 0.20% | 0.00% | 0 | 0 | 0.00% | — |
| Karachay-Cherkessia | 4 | out | 0.10% | 0.00% | 0 | 0 | 0.00% | — |
| North Ossetia-Alania | 4 | out | 0.19% | 0.00% | 0 | 0 | 0.00% | — |
| **Sum** | | | 100.00% | 100.00% | **20,229** | **19,330** | 100.00% | |

**Lazar** (solar +1; window -2 … +4; former Russia 58,246 robots / 56,261 humans; full tables §3.3 to §3.4)

| Successor | d | Window | (a) | (b) | (b) robots | (b) humans | (b-sub) | Tier reading (in window) |
|---|--:|---|--:|--:|--:|--:|--:|---|
| Russia | 1 | IN | 41.83% | 55.95% | 32,587 | 31,476 | 55.06% | Notable |
| Idelsk-Uralia (prov.) | 2 | IN | 23.41% | 31.30% | 18,233 | 17,611 | 30.81% | Notable |
| Donska-Kubania (prov.) | 2 | IN | 7.12% | 9.52% | 5,548 | 5,359 | 9.37% | Notable |
| Künnarantaiga | 6 | out | 8.24% | 0.00% | 0 | 0 | 0.00% | — |
| Siberia | 4 | out | 16.90% | 0.00% | 0 | 0 | 1.58% | — |
| Tuva | 5 | out | 0.08% | 0.00% | 0 | 0 | 0.00% | — |
| Karelia | 1 | IN | 0.97% | 1.30% | 755 | 730 | 1.28% | below floor; Notable by window rule only (no minimum stated) |
| Chechnya | 2 | IN | 0.29% | 0.38% | 223 | 216 | 0.38% | below floor; Notable by window rule only (no minimum stated) |
| Dagestan | 2 | IN | 0.61% | 0.82% | 478 | 461 | 0.81% | below floor; Notable by window rule only (no minimum stated) |
| Ingushetia | 2 | IN | 0.06% | 0.08% | 49 | 47 | 0.08% | below floor; Notable by window rule only (no minimum stated) |
| Kabardino-Balkaria | 2 | IN | 0.20% | 0.26% | 152 | 147 | 0.26% | below floor; Notable by window rule only (no minimum stated) |
| Karachay-Cherkessia | 2 | IN | 0.10% | 0.13% | 76 | 73 | 0.13% | below floor; Notable by window rule only (no minimum stated) |
| North Ossetia-Alania | 2 | IN | 0.19% | 0.25% | 145 | 141 | 0.25% | below floor; Notable by window rule only (no minimum stated) |
| **Sum** | | | 100.00% | 100.00% | **58,246** | **56,261** | 100.00% | |

**Concordia** (solar +8; window +5 … +11; former Russia 48,123 robots / 47,572 humans; full tables §4.3 to §4.4)

| Successor | d | Window | (a) | (b) | (b) robots | (b) humans | (b-sub) | Tier reading (in window) |
|---|--:|---|--:|--:|--:|--:|--:|---|
| Russia | 5 | out | 41.83% | 0.00% | 0 | 0 | 0.00% | — |
| Idelsk-Uralia (prov.) | 4 | out | 23.41% | 0.00% | 0 | 0 | 0.00% | — |
| Donska-Kubania (prov.) | 5 | out | 7.12% | 0.00% | 0 | 0 | 0.00% | — |
| Künnarantaiga | 1 | IN | 8.24% | 32.67% | 15,720 | 15,540 | 33.98% | Notable |
| Siberia | 2 | IN | 16.90% | 67.00% | 32,242 | 31,873 | 65.66% | Significant (with NZ gateway) / Notable (without) |
| Tuva | 2 | IN | 0.08% | 0.33% | 161 | 159 | 0.35% | Notable (window rule, below floor) |
| Karelia | 6 | out | 0.97% | 0.00% | 0 | 0 | 0.00% | — |
| Chechnya | 5 | out | 0.29% | 0.00% | 0 | 0 | 0.00% | — |
| Dagestan | 5 | out | 0.61% | 0.00% | 0 | 0 | 0.00% | — |
| Ingushetia | 5 | out | 0.06% | 0.00% | 0 | 0 | 0.00% | — |
| Kabardino-Balkaria | 5 | out | 0.20% | 0.00% | 0 | 0 | 0.00% | — |
| Karachay-Cherkessia | 5 | out | 0.10% | 0.00% | 0 | 0 | 0.00% | — |
| North Ossetia-Alania | 5 | out | 0.19% | 0.00% | 0 | 0 | 0.00% | — |
| **Sum** | | | 100.00% | 100.00% | **48,123** | **47,572** | 100.00% | |

### F.2 What decides each city's result (one city at a time; DERIVED)
- **Troll.** Membership never changes for any Russia-split successor, in any of the 108 combinations or under any single-unit flip. The only proportion moving more than 5 points is the income-free form (E = P only). The named knife-edges (Moscow, Tula, Blagoveshchensk, Yuzhno-Sakhalinsk) do not decide anything here.
- **Santa Luce.** The window holds only Russia and Karelia, both at its edge (d = 3), both only through their +2 zone. **Decisive inputs:** **official zones leave (b) UNDEFINED** (no successor in window; 16 combinations), and with K-in they leave **Kaliningrad 100%** (16 combinations). **θ = 5% with V1c or V2 brings Donska-Kubania in** (13.2 to 15.7%; 16 combinations). θ above 28.8% leaves Karelia alone. The S7 placement of Krasnodar (1.50° from the boundary) or Rostov (2.21°) alone decides Donska-Kubania's exclusion (14.27-point move if either falls to +2). Cherepovets (Vologda, 0.41°) moves (b-sub) 5.23 points.
- **Lazar.** **θ is decisive for Siberia:** its only in-window unit, Tyumen', is 7.11% of its pool. At θ = 5% Siberia enters (b) with its whole pool (18.44%; Russia −10.32, Idelsk-Uralia −5.77), while (b-sub) gives it 1.58%. **Official zones move (b-sub)** by more than 5 points (Russia +8.44, Idelsk-Uralia −8.78). Moscow does not decide anything here.
- **Concordia.** **The zone convention (S5) is decisive:** under official zones Idelsk-Uralia (prov.) enters at 48.13% of the share in (b) (all 36 official-zone combinations), Siberia falls 32.25 points and Künnarantaiga 15.73. The method's own source wrote Russia's footprint in official zones (`UEIC` L38–41; RS1 §4.2). **None of the RS1b knife-edges (Blagoveshchensk, Yuzhno-Sakhalinsk, Moscow, Tula) decides membership at Concordia**; the table in §4.2 shows each. Russia's pre-war Primary row there has no successor reaching the Primary floor (13M) under any reading. Whether New Zealand's gateway applies at Concordia decides Siberia's tier (Significant or Notable) under Reading A′.

### F.3 Method used
RS1 §5 as written, with the coordinator defaults S1 to S7 (§0.1). Inputs are RS1b's CSV, unchanged; the script reproduces RS1b's split (a) and zone profiles exactly. (a) = W_k ÷ ΣW; (b) = W_k × I_k ÷ Σ W_j × I_j, with I_k = 1 when the minimum distance over meaningful zones is ≤ 3; (b-sub) at unit level; counts by largest remainder (Hamilton), ties to larger W. Tier readings A, A′ and B as defined in §0.2. Sensitivities: each coordinator alternative one at a time, plus the full 108-combination sweep, plus the single-unit knife-edge scan (35 units within 3° of a boundary), plus the income-free and Gini-free forms. Flag threshold: more than 5 points.

### F.4 NOT FOUND (all four cities)
- **Method choices no source settles** (each named where it is decisive above): the meaningful-share threshold θ · solar or official zones for a nation's footprint (S5) · the "small pool" cut for the large-pool clause · a minimum pool for the Notable tier · the Gini penalty's functional form · whether the New Zealand gateway (`UEIC` L32–33) applies at Concordia.
- **A Concordia section in `Upper_Earth_Immigration_Composition.md`:** none exists; Concordia's spec table was used.
- **First Interwar data:** no population, GRP or Gini for any successor at any in-world date (RS1 §2).
- **Inherited input gaps (RS1b §8):** Ukrainian-unit Gini; Donetsk and Luhansk GRP per head after 2013; any Ukrainian GRP after 2021; Ingushetia's correct 2022 GRP; a statistical left-bank Kherson population; Rosstat primaries (TLS-blocked); which Gini measure CEIC carries.
- **Not computed (outside the brief):** Census II counts.

### F.5 Search and retrieval log (per LAW 0-R)
| # | What | Tool | Result |
|---|---|---|---|
| W0 | **No web search was run.** The brief allows search only to fill a gap RS1b lists. None of those gaps feeds the primary form for these four cities: the Ukrainian Gini, the Donetsk/Luhansk GRP and Kherson affect V2 only; Ingushetia's 2022 GRP affects a form not used here; the CEIC-measure question moves (1 − G) by under 1.5% per unit (RS1b §3). The unknowns that are decisive here (θ, S5, the small-pool cut, the New Zealand gateway) are method choices no search can settle. **Not a dead end: a scope decision, stated so it can be challenged.** | — | — |
| L1 | `grep -n "Concordia"` in `Upper_Earth_Immigration_Composition.md` | local | No match: the file has no Concordia section. Dead at the source; the spec's table was used. |
| L2 | City specs: `Specs/Halley subnet/Troll.md` L1–70, `Santa_Luce.md` L1–75, `Lazar.md` L1–90, `Specs/Janbogo subnet/Concordia.md` L1–85 (headers and the Population & Composition sections) | Read | Read in full for those ranges. Only each city's own coordinates, Russia row and tier table were used (one-location rule). |
| L3 | `UEIC` sections Methodology (L7–19), HOW FACTOR 1 IS MEASURED (L21–127), and the city sections Troll L276–286, Santa Luce L288–298, Lazar L324–366 | Read | Read in full. |
| L4 | `/tmp/ne_test/ne_10m_populated_places_simple.geojson` (the developer's NE pipeline file): longitudes of Beijing, Shanghai, Tokyo, Seoul, Busan, Jakarta, Perth, Sydney, Melbourne, Hobart, Bangkok, Hanoi, Ho Chi Minh City, Manila, Kuala Lumpur, Wellington, Auckland, Minsk, Moscow, Blagoveshchensk, Yuzhno-Sakhalinsk, Yekaterinburg, Omsk, Izhevsk, Orenburg, and the capitals of Concordia's other nations | `ne_lookup.py`, `ne_eu.py` | Read; used only for Concordia's tier reading (§4.5). ⚠ Seoul is 0.03 of a zone from the +8/+9 boundary (8.467); either way it is inside Concordia's window. |

### F.6 What is left
- Developer choices that would settle the results flagged above: θ, S5 (solar or official), the small-pool cut, and, for Concordia, the New Zealand gateway. **This unit makes no recommendation on any of them.**
- Census II counts, if wanted (same method, different totals).
- The reorganization itself (editing composition tables) is a later, separate job under `DR-23`; nothing here touches it.

---
