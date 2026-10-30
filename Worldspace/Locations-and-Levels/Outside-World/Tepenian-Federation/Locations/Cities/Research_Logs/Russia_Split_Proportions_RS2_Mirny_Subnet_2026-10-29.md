# Russia-split proportions · Unit RS2 · Davis, Zhongshan, Shirayuki, Sinheung, Mirny, Casey, Relung Panen (2026-10-29)

**⚠ The First Interwar Period record does not exist yet.** The developer's Russia folders for it (`03 official timeline years`, `04 timeline staging`) are empty (RS1 section 2). **Every figure in this file is a present-day real-world regional figure aggregated to the successor nations' territories (DERIVED), standing in for that unwritten record.** **Nothing here is a ruling or a recommendation**; no spec, census or composition file is touched. **The successor names are the developer's** (`09 follow-up/subdivisions.csv`); **Idelsk-Uralia and Donska-Kubania are provisional** (conflicting sources, RS1 §1.2) and are marked "(prov.)" wherever they appear.

## PROGRESS
- [x] 1 Davis
- [x] 2 Zhongshan
- [x] 3 Shirayuki
- [x] 4 Sinheung
- [x] 5 Mirny
- [x] 6 Casey
- [x] 7 Relung Panen
- [x] FINAL

**Brief:** `Research_Logs/Russia_Split_Proportions_Research_BRIEF_2026-10-29.md` (Units RS2 to RS4, and the coordinator's section "Added 2026-10-29 (coordinator, after RS1)"). **Method and successor table:** `Russia_Split_Proportions_RS1_Inventory_and_Method_2026-10-29.md` (cited `RS1`). **Inputs:** `Russia_Split_Proportions_RS1b_Input_Table_2026-10-29.md` (cited `RS1b`) and `Russia_Split_Inputs_2026-10-29.csv` (md5 `9ea0f55b6e5db1e2ff1ba28420f8a39e` when read). **Composition method:** `Upper_Earth_Immigration_Composition.md` (cited `UEIC`), sections "Methodology" (L7–19), "HOW FACTOR 1 IS MEASURED" (L21–63), the pool table (L65–114) and the tier rule (L1105–1109); for each city, only its own section and its own `Specs` tier table.

**Labels:** SOURCED (file and line) · UNVERIFIED · DERIVED · NOT FOUND. **Every percentage and count in this file is DERIVED** (arithmetic on RS1b's DERIVED stand-in inputs).

---

## 0 · The method used (stated once; each city section below applies it to that city alone)

### 0.1 Defaults applied (the coordinator's S1–S7; NOT rulings)
**Primary = V1 · K-out · INIT · θ = 10% · solar zones · no wraparound · each subject at the solar zone of its largest city · E = P × y2024 × (1 − G2022).** Every Russian unit has a Gini (RS1b §3), so the primary form runs without the no-Gini fallback; V2 has no Ukrainian Gini, so V2 uses E = P × y2021 for every unit (RS1b §0). The script reproduces RS1b's primary split (a) and its zone profiles exactly (check run, `check.py`, output: *"V1 primary Russia 41.83 · Idelsk-Uralia (prov.) 23.41 · Donska-Kubania (prov.) 7.12 · Künnarantaiga 8.24 · Siberia 16.90 · …"*, matching RS1b §6.1 and §7.1).

### 0.2 Formulas (RS1 §5, applied without change)
- **City zone (SOURCED rule, `UEIC` L28):** *z_c* = round(longitude ÷ 15). Window = *z_c* − 3 … *z_c* + 3 (`UEIC` L29–31).
- **Effective pool per unit:** *E_s = P_s × y_s × (1 − G_s)*. **Per successor:** *W_k = Σ E_s*. **Zone profile:** *q_k(z) = Σ_{z_s = z} E_s ÷ W_k*. **Meaningful zones:** *Z_k(θ) = {z : q_k(z) ≥ θ}* (the footprint rule, `UEIC` L43–47; RS1 §4.1 item 5).
- **Distance:** *d_k = min over Z_k(θ) of |z − z_c|*; **inside** if *d_k ≤ 3*.
- **(a) by pool alone:** *p_k = W_k ÷ Σ W_j*.
- **(b) by pool within the window:** *p_k = W_k · I_k ÷ Σ W_j · I_j*, with *I_k* = 1 if inside, else 0.
- **(b-sub), reported as a sensitivity:** only the units of each successor that lie within ±3 of the city count: *W_k,c = Σ_{|z_s − z_c| ≤ 3} E_s*, normalized.
- **Counts (largest remainder, Hamilton's method):** for robots and humans separately, *n_k = floor(N × p_k)*; the *N − Σ n_k* units left go one each to the largest fractional remainders, ties to the larger *W_k*. The script asserts that each column sums exactly to *N*.

### 0.3 The tier reading (informational; nothing is ruled)
- **Absolute pool:** *Ê_k = 25M × p_k(a)* (`UEIC` L76: Russia's pool ~25M; RS1 §5 Step 7). The successors' Ê sum to the 25M they replace.
- **The tier rule (SOURCED, `UEIC` L17, L1107):** ranked by pool; breaks at the largest ratio gaps in the city's ranking. **Applied here as follows (DERIVED reading):** the city's existing breaks are kept, and a successor whose Ê falls inside the city's T2|T3 gap (between its smallest Significant pool and its largest Notable pool) goes to the side of the **larger** of the two sub-gaps it creates, which is the same as testing Ê against the geometric mean of the two bounding pools. Above the cut = **T2-sized**; below = **T3-sized**.
- **Proximity (SOURCED, `UEIC` L30–31):** *"A small-pool nation qualifies for the Notable tier only if distance ≤ 3 … large pools reach anywhere."* **"Large" has no number in the file (NOT FOUND); read here as T2-sized.** So: T2-sized → Significant at any distance; T3-sized → Notable if *d ≤ 3*, else absent.
- **Relung Panen only:** computed proximity-first, *"the ±3 window above is applied to EVERY tier here"* (`UEIC` L581–583), so every tier needs *d ≤ 3* there.
- **Smallest pool in the census:** Uruguay, *"~0.6M"*, *"the smallest effective population of any nation in the census"* (`UEIC` L1089). Successors below 0.6M are marked ⚠; whether a floor applies is **NOT FOUND** (`UEIC` L1083–1085 speak of a "floor threshold" without a number).
- **The mechanical alternative** (re-finding the largest gaps over the whole merged ranking) is also printed for each city. It is degenerate: the sub-0.6M successors create ratio gaps larger than any in the city's own ranking, so it places breaks among them. It is reported, not used.
- **The city's pools** are `UEIC` L65–110 values for the nations in that city's tier lists. Where a city's `Specs` table was hand-adjusted, the section says so.

### 0.4 Sensitivities (one at a time against the primary; four combinations added)
V1c · V2 · K-in · C-15 · θ = 5% · θ = 25% · official zones (S5) · territory-centroid zones (S7 alternative) · the three knife-edge cities RS1b §4 lists that can move a zone set (Moscow at +2, Blagoveshchensk/Amur at +8, Yuzhno-Sakhalinsk/Sakhalin at +9) · no Gini (P × y2024) · population only · (b-sub) · combinations: centroid + θ 25%, Moscow at +2 + θ 25%, official + θ 25%, official + θ 5%. **Flag rule:** any share that moves more than 5 percentage points from the primary, and any successor whose window membership flips, is listed. S6 (wraparound) cannot arise under S7: no unit is placed west of the date line (RS1b §6.3, last paragraph), so it is not a sensitivity here.

### 0.5 Searches
**No web search was run by this unit.** Every input is RS1b's; no gap RS1b lists (Ukrainian Gini, Donetsk and Luhansk GRP after 2013, Ingushetia 2022, the left-bank Kherson population, Rosstat primaries, which Gini measure CEIC carries) changes a primary result here, because each touches only a sensitivity (V2, or the 2022 form). **Dead ends: none, because nothing was searched.** Scripts (scratch, not in any repo): `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/a4f4478c-4c10-4425-b67b-16739b0736bb/scratchpad/rs2/core.py`, `…/rs2/cities.py`, `…/rs2/units_table.py`, `…/rs2/check.py`; raw outputs `…/rs2/city_<n>_raw.md`. Python 3.12.3, run with `-I`.

### 0.6 Per-unit effective pools, primary (raw output of `units_table.py`; inputs from RS1b §5.1)

| Unit (`R09` line) | Recipient (INIT) | P (2021) | y 2024 (k RUB) | G 2022 | E_s = P × y × (1 − G) (bn RUB) | Solar S7 | Centroid | Official |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| Belgorod (8) | Russia | 1,540,486 | 1015.794 | 0.368 | 989.0 | +2 | +3 | +3 |
| Bryansk (9) | Russia | 1,169,161 | 636.575 | 0.360 | 476.3 | +2 | +2 | +3 |
| City of St. Petersburg (10) | Russia | 5,601,911 | 2301.327 | 0.402 | 7,709.3 | +2 | +2 | +3 |
| Kaluga (11) | Russia | 1,069,904 | 855.283 | 0.330 | 613.1 | +2 | +2 | +3 |
| Kursk (12) | Russia | 1,082,458 | 788.412 | 0.356 | 549.6 | +2 | +2 | +3 |
| Leningrad (13) | Russia | 2,000,997 | 1174.111 | 0.345 | 1,538.9 | +2 | +2 | +3 |
| Lipetsk (14) | Russia | 1,143,224 | 939.205 | 0.367 | 679.7 | +3 | +3 | +3 |
| Moskovskaya (15) | Russia | 8,524,665 | 1249.020 | 0.372 | 6,686.6 | +3 | +3 | +3 |
| Moskva (16) | Russia | 13,010,112 | 3103.504 | 0.412 | 23,741.6 | +3 | +2 | +3 |
| Novgorod (17) | Russia | 583,387 | 842.000 | 0.340 | 324.2 | +2 | +2 | +3 |
| Orel (18) | Russia | 713,374 | 639.833 | 0.357 | 293.5 | +2 | +2 | +3 |
| Pskov (19) | Russia | 599,084 | 607.585 | 0.344 | 238.8 | +2 | +2 | +3 |
| Ryazan' (20) | Russia | 1,102,810 | 757.419 | 0.349 | 543.8 | +3 | +3 | +3 |
| Smolensk (21) | Russia | 888,421 | 761.465 | 0.365 | 429.6 | +2 | +2 | +3 |
| Tambov (22) | Russia | 982,991 | 609.973 | 0.352 | 388.5 | +3 | +3 | +3 |
| Tula (23) | Russia | 1,501,214 | 891.344 | 0.344 | 877.8 | +3 | +2 | +3 |
| Tver' (24) | Russia | 1,230,171 | 690.823 | 0.329 | 570.2 | +2 | +2 | +3 |
| Voronezh (25) | Russia | 2,308,792 | 757.722 | 0.385 | 1,075.9 | +3 | +3 | +3 |
| Bashkortostan (50) | Idelsk-Uralia (prov.) | 4,091,423 | 739.699 | 0.375 | 1,891.5 | +4 | +4 | +5 |
| Tatarstan (51) | Idelsk-Uralia (prov.) | 4,004,809 | 1361.839 | 0.379 | 3,386.9 | +3 | +3 | +3 |
| Ivanovo (52) | Idelsk-Uralia (prov.) | 927,828 | 557.302 | 0.335 | 343.9 | +3 | +3 | +3 |
| Kostroma (53) | Idelsk-Uralia (prov.) | 580,976 | 711.210 | 0.320 | 281.0 | +3 | +3 | +3 |
| Vladimir (54) | Idelsk-Uralia (prov.) | 1,348,134 | 743.499 | 0.325 | 676.6 | +3 | +3 | +3 |
| Yaroslavl' (55) | Idelsk-Uralia (prov.) | 1,209,811 | 868.435 | 0.350 | 682.9 | +3 | +3 | +3 |
| Arkhangel'sk (56) | Idelsk-Uralia (prov.) | 978,873 | 883.412 | 0.339 | 571.6 | +3 | +3 | +3 |
| Komi (58) | Idelsk-Uralia (prov.) | 737,853 | 1671.788 | 0.353 | 798.1 | +3 | +4 | +3 |
| Nenets (60) | Idelsk-Uralia (prov.) | 41,434 | 14250.822 | 0.419 | 343.1 | +4 | +4 | +3 |
| Vologda (61) | Idelsk-Uralia (prov.) | 1,142,827 | 1081.981 | 0.338 | 818.6 | +3 | +3 | +3 |
| Chelyabinsk (62) | Idelsk-Uralia (prov.) | 3,431,224 | 870.657 | 0.338 | 1,977.7 | +4 | +4 | +5 |
| Kurgan (63) | Idelsk-Uralia (prov.) | 776,661 | 615.394 | 0.337 | 316.9 | +4 | +4 | +5 |
| Orenburg (64) | Idelsk-Uralia (prov.) | 1,862,767 | 1134.336 | 0.348 | 1,377.7 | +4 | +4 | +5 |
| Perm' (65) | Idelsk-Uralia (prov.) | 2,532,405 | 1046.002 | 0.367 | 1,676.8 | +4 | +4 | +5 |
| Sverdlovsk (66) | Idelsk-Uralia (prov.) | 4,268,998 | 1124.324 | 0.395 | 2,903.8 | +4 | +4 | +5 |
| Udmurt (67) | Idelsk-Uralia (prov.) | 1,452,914 | 979.471 | 0.325 | 960.6 | +4 | +4 | +4 |
| Chuvash (68) | Idelsk-Uralia (prov.) | 1,186,909 | 606.492 | 0.336 | 478.0 | +3 | +3 | +3 |
| Kirov (69) | Idelsk-Uralia (prov.) | 1,153,680 | 635.117 | 0.322 | 496.8 | +3 | +3 | +3 |
| Mariy-El (70) | Idelsk-Uralia (prov.) | 677,097 | 530.998 | 0.336 | 238.7 | +3 | +3 | +3 |
| Mordovia (71) | Idelsk-Uralia (prov.) | 783,552 | 625.379 | 0.346 | 320.5 | +3 | +3 | +3 |
| Nizhegorod (72) | Idelsk-Uralia (prov.) | 3,119,115 | 1009.914 | 0.384 | 1,940.4 | +3 | +3 | +3 |
| Penza (73) | Idelsk-Uralia (prov.) | 1,266,348 | 652.090 | 0.343 | 542.5 | +3 | +3 | +3 |
| Samara (74) | Idelsk-Uralia (prov.) | 3,172,925 | 1062.849 | 0.365 | 2,141.4 | +3 | +3 | +4 |
| Saratov (75) | Idelsk-Uralia (prov.) | 2,442,575 | 645.768 | 0.359 | 1,011.1 | +3 | +3 | +4 |
| Ul'yanovsk (76) | Idelsk-Uralia (prov.) | 1,196,745 | 669.092 | 0.342 | 526.9 | +3 | +3 | +4 |
| Krasnodar (77) | Donska-Kubania (prov.) | 5,838,273 | 922.283 | 0.408 | 3,187.6 | +3 | +3 | +3 |
| Adygey (78) | Donska-Kubania (prov.) | 496,934 | 567.832 | 0.404 | 168.2 | +3 | +3 | +3 |
| Rostov (79) | Donska-Kubania (prov.) | 4,200,729 | 746.513 | 0.386 | 1,925.4 | +3 | +3 | +3 |
| Stavropol' (80) | Donska-Kubania (prov.) | 2,907,593 | 553.020 | 0.335 | 1,069.3 | +3 | +3 | +3 |
| Kalmyk (81) | Donska-Kubania (prov.) | 267,133 | 813.187 | 0.313 | 149.2 | +3 | +3 | +3 |
| Astrakhan' (82) | Donska-Kubania (prov.) | 960,142 | 944.947 | 0.335 | 603.3 | +3 | +3 | +4 |
| Volgograd (83) | Donska-Kubania (prov.) | 2,500,781 | 621.115 | 0.342 | 1,022.1 | +3 | +3 | +3 |
| Sakha (Yakutia) (26) | Künnarantaiga | 995,686 | 2520.579 | 0.404 | 1,495.8 | +9 | +9 | +9 |
| Amur (27) | Künnarantaiga | 766,912 | 1365.680 | 0.384 | 645.2 | +9 | +9 | +9 |
| Buryat (28) | Künnarantaiga | 978,588 | 594.962 | 0.355 | 375.5 | +7 | +7 | +8 |
| Chita (29) | Künnarantaiga | 1,004,125 | 923.857 | 0.348 | 604.8 | +8 | +8 | +9 |
| Chukchi Autonomous Okrug (30) | Künnarantaiga | 47,490 | 4678.057 | 0.410 | 131.1 | +12 | +12 | +12 |
| Kamchatka (31) | Künnarantaiga | 291,705 | 1611.201 | 0.362 | 299.9 | +11 | +11 | +12 |
| Khabarovsk (32) | Künnarantaiga | 1,292,944 | 1240.000 | 0.351 | 1,040.5 | +9 | +9 | +10 |
| Maga Buryatdan (33) | Künnarantaiga | 136,085 | 3936.320 | 0.397 | 323.0 | +10 | +10 | +11 |
| Primor'ye (34) | Künnarantaiga | 1,845,165 | 1184.384 | 0.361 | 1,396.5 | +9 | +9 | +10 |
| Sakhalin (35) | Künnarantaiga | 466,609 | 3665.840 | 0.393 | 1,038.3 | +10 | +10 | +11 |
| Yevrey (36) | Künnarantaiga | 150,453 | 786.448 | 0.310 | 81.6 | +9 | +9 | +10 |
| Irkutsk (37) | Künnarantaiga | 2,370,102 | 1284.374 | 0.353 | 1,969.5 | +7 | +7 | +8 |
| Khakass (38) | Siberia | 534,795 | 749.963 | 0.320 | 272.7 | +6 | +6 | +7 |
| Krasnoyarsk (39) | Siberia | 2,856,971 | 1522.495 | 0.379 | 2,701.2 | +6 | +6 | +7 |
| Altay (40) | Siberia | 2,163,693 | 605.547 | 0.353 | 847.7 | +6 | +6 | +7 |
| Gorno-Altay (41) | Siberia | 210,924 | 623.316 | 0.343 | 86.4 | +6 | +6 | +7 |
| Kemerovo (42) | Siberia | 2,600,923 | 716.694 | 0.342 | 1,226.6 | +6 | +6 | +7 |
| Khanty-Mansiy (43) | Siberia | 1,711,480 | 5610.363 | 0.383 | 5,924.4 | +5 | +5 | +5 |
| Novosibirsk (44) | Siberia | 2,797,176 | 966.865 | 0.368 | 1,709.2 | +6 | +5 | +7 |
| Omsk (45) | Siberia | 1,858,798 | 779.599 | 0.366 | 918.7 | +5 | +5 | +6 |
| Tomsk (46) | Siberia | 1,062,666 | 1053.060 | 0.340 | 738.6 | +6 | +6 | +7 |
| Tyumen' (47) | Siberia | 1,601,940 | 1365.511 | 0.373 | 1,371.5 | +4 | +5 | +5 |
| Yamal-Nenets (48) | Siberia | 510,490 | 12196.003 | 0.440 | 3,486.5 | +5 | +5 | +5 |
| Tuva (49) | Tuva | 336,651 | 449.353 | 0.363 | 96.4 | +6 | +6 | +7 |
| Karelia (57) | Karelia | 533,121 | 919.389 | 0.324 | 331.3 | +2 | +2 | +3 |
| Murmansk (59) | Karelia | 667,744 | 1714.106 | 0.323 | 774.9 | +2 | +2 | +3 |
| Chechnya (2) | Chechnya | 1,510,824 | 344.807 | 0.372 | 327.2 | +3 | +3 | +3 |
| Dagestan (3) | Dagestan | 3,182,054 | 348.978 | 0.370 | 699.6 | +3 | +3 | +3 |
| Ingush (4) | Ingushetia | 509,541 | 204.566 | 0.311 | 71.8 | +3 | +3 | +3 |
| Kabardin-Balkar (5) | Kabardino-Balkaria | 904,200 | 381.560 | 0.355 | 222.5 | +3 | +3 | +3 |
| Karachay-Cherkess (6) | Karachay-Cherkessia | 469,865 | 347.711 | 0.319 | 111.3 | +3 | +3 | +3 |
| North Ossetia (7) | North Ossetia-Alania | 687,357 | 473.305 | 0.345 | 213.1 | +3 | +3 | +3 |
| **Total (82 units)** | | 143,669,707 | | | 114,088.7 | | | |

**Where the zones of each successor come from** (S7 city longitudes, CSV column `S7_place_lon_E`, ÷ 15; DERIVED): Siberia's +5 is Surgut (Khanty-Mansiy, 73.43°E → 4.895), Omsk (73.40°E → 4.893) and Noyabrsk (Yamal-Nenets, 75.62°E → 5.041); its +6 is Novosibirsk (5.531), Krasnoyarsk (6.191), Barnaul (5.583), Novokuznetsk (5.807), Tomsk (5.665). Idelsk-Uralia's +4 is Yekaterinburg (60.60°E → 4.040), Chelyabinsk (4.096), Perm (3.750), Ufa (3.736), Orenburg (3.674), Izhevsk (3.549), Kurgan (4.356) and Naryan-Mar (3.537). Künnarantaiga's +7 is Irkutsk (104.25°E → 6.950) and Ulan-Ude (7.175). Russia's +3 is Moscow (37.61°E → **2.507**), Moscow Oblast, Tula (**2.509**), Lipetsk, Ryazan', Tambov and Voronezh.

---

## 1 · Davis (solar UTC +5)

**City inputs (SOURCED):** ~68°35'S 77°58'E (`UEIC` L537); 77.9667°E ÷ 15 = 5.198 → **solar UTC +5** (`UEIC` L28 rule); `UEIC` L28 itself gives *"Davis 77°58'E → +5"*. Window **+2 … +8**. **Former Russia share 5.64%**, tier Significant; **Census I: 34,206 robots, 32,472 humans** (brief L25; the city's `Specs` row, `Specs/Mirny subnet/Davis.md` L37, gives the same figures). **Tier lists:** `UEIC` L541–543 (Primary China; Significant Japan 65M, Germany 46M, UK 32M, South Korea 26M, Russia 25M, Indonesia 16M, Australia 13M; Notable Thailand 8M down to Latvia and Estonia 0.6M). `Specs/Mirny subnet/Davis.md` L20–22 lists the same nations in the same tiers, and `UEIC` L542 records that the two were re-ordered to agree on 2026-09-05.

**Status line, plain:** the First Interwar record does not exist; these are present-day regional figures standing in for it; nothing here is a ruling or a recommendation.

### 1.1 Which successors lie inside Davis's window
**Inside (primary): all thirteen successors** — Russia (d = 2), Idelsk-Uralia (prov.) (d = 1), Donska-Kubania (prov.) (d = 2), Künnarantaiga (d = 2, through its +7 zone: Irkutsk and Ulan-Ude), Siberia (**d = 0**, through its +5 zone: Surgut, Omsk, Noyabrsk), Tuva (d = 1), Karelia (d = 3, at the edge), and the six North Caucasus republics (d = 2). **Outside: none.** Under the variants: **Kaliningrad (K-in) is outside** (solar +1, d = 4; inside under official zones, +2, d = 3); **Finland's Republic-of-Karelia piece (C-15) is inside** (+2, d = 3).

**Relation to the city's own note (SOURCED, then DERIVED):** `UEIC` L542 gives Russia *"**distance 0** from Davis's solar UTC+5 (Yekaterinburg, Perm)"*. On the solar rule the two cities sit in **+4** (Yekaterinburg 60.60°E → 4.040; Perm 56.25°E → 3.750; RS1b CSV), and both now belong to **Idelsk-Uralia (prov.)**, which is therefore at d = 1. Their **official** zone is +5 (RS1b, official column), which is where the note's +5 comes from (the same solar/official mix RS1 §4.2 records). The successor at distance 0 on the solar rule is **Siberia** (Surgut, Omsk, Noyabrsk). Inclusion is unchanged either way.

### 1.2 to 1.5 · Raw script output (`cities.py 1`, pasted unedited)

`CITY 1 Davis: lon 77.9667E / 15 = 5.1978 -> solar UTC +5; window +2 ... +8`

#### WINDOW (primary: V1 · K-out · INIT · solar S7 · θ 10%; θ 5% / 25%, official and centroid shown for membership only)

| Successor | q(z), solar, primary | Z(10%) | d | Inside ±3? | θ 5%: d / in | θ 25%: d / in | official: Z(10%), d / in | centroid: Z(10%), d / in |
|---|---|---|--:|:-:|:-:|:-:|---|---|
| Russia | +2: 28.8% · +3: 71.2% | {+2,+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+2,+3}, 2 / IN |
| Idelsk-Uralia (prov.) | +3: 57.1% · +4: 42.9% | {+3,+4} | 1 | **IN** | 1 / IN | 1 / IN | {+3,+4,+5}, 0 / IN | {+3,+4}, 1 / IN |
| Donska-Kubania (prov.) | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Künnarantaiga | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7,+9,+10} | 2 | **IN** | 2 / IN | 4 / OUT | {+8,+9,+10,+11}, 3 / IN | {+7,+9,+10}, 2 / IN |
| Siberia | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5,+6} | 0 | **IN** | 0 / IN | 0 / IN | {+5,+7}, 0 / IN | {+5,+6}, 0 / IN |
| Tuva | +6: 100.0% | {+6} | 1 | **IN** | 1 / IN | 1 / IN | {+7}, 2 / IN | {+6}, 1 / IN |
| Karelia | +2: 100.0% | {+2} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 2 / IN | {+2}, 3 / IN |
| Chechnya | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Dagestan | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Ingushetia | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Kabardino-Balkaria | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Karachay-Cherkessia | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| North Ossetia-Alania | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Kaliningrad (K-in) *(K-in only)* | +1: 100.0% | {+1} | 4 | **OUT** | same | same | {+2}, 3 / IN | {+1}, 4 / OUT |
| Finland, Rep. of Karelia (C-15) *(C-15 only)* | +2: 100.0% | {+2} | 3 | **IN** | same | same | {+3}, 2 / IN | {+2}, 3 / IN |
| Idelsk-Uralia (prov.) under C-15 *(with Murmansk)* | +2: 2.8% · +3: 55.5% · +4: 41.7% | {+3,+4} | 1 | **IN** | — | — | — | — |

INSIDE (primary): Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Künnarantaiga, Siberia, Tuva, Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania
OUTSIDE (primary): none

#### SPLIT (primary)

Σ W (all) = 114.0887 tn RUB · Σ W (inside window) = 114.0887 tn RUB · Σ W_c (b-sub, units with |z_s − 5| ≤ 3) = 107.6369 tn RUB

| Successor | W_k (tn RUB) | **(a) % = W_k ÷ ΣW** | Inside? | **(b) % = W_k·I ÷ Σ W·I** | W_k,c (tn RUB) | (b-sub) % |
|---|--:|--:|:-:|--:|--:|--:|
| Russia | 47.7264 | 41.83 | IN | 41.83 | 47.7264 | 44.34 |
| Idelsk-Uralia (prov.) | 26.7038 | 23.41 | IN | 23.41 | 26.7038 | 24.81 |
| Donska-Kubania (prov.) | 8.1252 | 7.12 | IN | 7.12 | 8.1252 | 7.55 |
| Künnarantaiga | 9.4017 | 8.24 | IN | 8.24 | 2.9499 | 2.74 |
| Siberia | 19.2836 | 16.90 | IN | 16.90 | 19.2836 | 17.92 |
| Tuva | 0.0964 | 0.08 | IN | 0.08 | 0.0964 | 0.09 |
| Karelia | 1.1062 | 0.97 | IN | 0.97 | 1.1062 | 1.03 |
| Chechnya | 0.3272 | 0.29 | IN | 0.29 | 0.3272 | 0.30 |
| Dagestan | 0.6996 | 0.61 | IN | 0.61 | 0.6996 | 0.65 |
| Ingushetia | 0.0718 | 0.06 | IN | 0.06 | 0.0718 | 0.07 |
| Kabardino-Balkaria | 0.2225 | 0.20 | IN | 0.20 | 0.2225 | 0.21 |
| Karachay-Cherkessia | 0.1113 | 0.10 | IN | 0.10 | 0.1113 | 0.10 |
| North Ossetia-Alania | 0.2131 | 0.19 | IN | 0.19 | 0.2131 | 0.20 |
| **Sum** | 114.0887 | 100.00 | | 100.00 | 107.6369 | 100.00 |

#### COUNTS (largest remainder / Hamilton; ties to larger W_k)

Robots R = 34,206 · Humans H = 32,472. Units left after flooring, given one each to the largest remainders: (a) robots 7, humans 7; (b) robots 7, humans 7.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans |
|---|--:|--:|--:|--:|
| Russia | 14,309 | 13,584 | 14,309 | 13,584 |
| Idelsk-Uralia (prov.) | 8,006 | 7,600 | 8,006 | 7,600 |
| Donska-Kubania (prov.) | 2,436 | 2,313 | 2,436 | 2,313 |
| Künnarantaiga | 2,819 | 2,676 | 2,819 | 2,676 |
| Siberia | 5,782 | 5,489 | 5,782 | 5,489 |
| Tuva | 29 | 27 | 29 | 27 |
| Karelia | 332 | 315 | 332 | 315 |
| Chechnya | 98 | 93 | 98 | 93 |
| Dagestan | 210 | 199 | 210 | 199 |
| Ingushetia | 21 | 20 | 21 | 20 |
| Kabardino-Balkaria | 67 | 63 | 67 | 63 |
| Karachay-Cherkessia | 33 | 32 | 33 | 32 |
| North Ossetia-Alania | 64 | 61 | 64 | 61 |
| **Sum** | 34,206 | 32,472 | 34,206 | 32,472 |

#### TIERS (Ê_k = 25M × (a) share; city T2 floor 13M, T3 top 8M; break at the larger sub-gap ⇔ Ê ≥ √(13×8) = 10.198M is T2-sized)

| Successor | Ê_k (M) | d | Size class | Effective tier (informational) |
|---|--:|--:|---|---|
| Russia | 10.458 | 2 | T2-sized | Significant |
| Idelsk-Uralia (prov.) | 5.852 | 1 | T3-sized | Notable |
| Donska-Kubania (prov.) | 1.780 | 2 | T3-sized | Notable |
| Künnarantaiga | 2.060 | 2 | T3-sized | Notable |
| Siberia | 4.226 | 0 | T3-sized | Notable |
| Tuva | 0.021 | 1 | T3-sized | Notable ⚠ below 0.6M |
| Karelia | 0.242 | 3 | T3-sized | Notable ⚠ below 0.6M |
| Chechnya | 0.072 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Dagestan | 0.153 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Ingushetia | 0.016 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Kabardino-Balkaria | 0.049 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Karachay-Cherkessia | 0.024 | 2 | T3-sized | Notable ⚠ below 0.6M |
| North Ossetia-Alania | 0.047 | 2 | T3-sized | Notable ⚠ below 0.6M |

Mechanical re-finding over the merged ranking, three largest ratio gaps: China 210.00M → Japan 65.000M = 3.23× · Estonia 0.60M → Karelia 0.242M = 2.48× · Dagestan 0.15M → Chechnya 0.072M = 2.14×

#### SENSITIVITY, split (b) (% of the former Russia share; bold = moves more than 5 points from primary; OUT = outside the window)

| Successor | primary | V1c | V2 | K-in | C-15 | θ 5% | θ 25% | official zones | centroid (S7 alt.) | Moscow at +2 | Amur at +8 | Sakhalin at +9 | no Gini (P×y2024) | P only | b-sub (unit level) | combo: centroid + θ 25% | combo: Moscow at +2 + θ 25% | combo: official + θ 25% | combo: official + θ 5% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.83 | 41.83 | 41.83 | 45.59 | 41.83 | 41.83 | 41.83 | 41.83 | 41.83 | 42.72 | **31.36** | 44.34 | 45.59 | 45.59 | 45.59 | 41.83 |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.41 | 24.09 | 23.41 | 25.51 | 23.41 | 23.41 | 23.41 | 23.41 | 23.41 | 22.71 | **30.90** | 24.81 | 25.51 | 25.51 | 25.51 | 23.41 |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.12 | 7.12 | 7.12 | 7.76 | 7.12 | 7.12 | 7.12 | 7.12 | 7.12 | 7.10 | 11.95 | 7.55 | 7.76 | 7.76 | 7.76 | 7.12 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.24 | 8.24 | 8.24 | **OUT** | 8.24 | 8.24 | 8.24 | 8.24 | 8.24 | 8.11 | 7.20 | **2.74** | **OUT** | **OUT** | **OUT** | 8.24 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.90 | 16.90 | 16.90 | 18.42 | 16.90 | 16.90 | 16.90 | 16.90 | 16.90 | 17.00 | 12.47 | 17.92 | 18.42 | 18.42 | 18.42 | 16.90 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.09 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.23 | 0.09 | 0.09 | 0.09 | 0.09 | 0.08 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.97 | — | 0.97 | 1.06 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.89 | 0.84 | 1.03 | 1.06 | 1.06 | 1.06 | 0.97 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.29 | 0.31 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.28 | 1.05 | 0.30 | 0.31 | 0.31 | 0.31 | 0.29 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.67 | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 | 0.65 | 0.67 | 0.67 | 0.67 | 0.61 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.07 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 | 0.07 | 0.07 | 0.07 | 0.07 | 0.06 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.20 | 0.20 | 0.20 | 0.21 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 0.19 | 0.63 | 0.21 | 0.21 | 0.21 | 0.21 | 0.20 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.10 | 0.11 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.09 | 0.33 | 0.10 | 0.11 | 0.11 | 0.11 | 0.10 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.19 | 0.20 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.18 | 0.48 | 0.20 | 0.20 | 0.20 | 0.20 | 0.19 |
| Kaliningrad (K-in) | — | — | — | OUT | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

FLAGS (b), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49); θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); b-sub (unit level): Künnarantaiga 8.24 → 2.74 (-5.50); combo: centroid + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); combo: Moscow at +2 + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); combo: official + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24)
WINDOW FLIPS vs primary: θ 25%: Künnarantaiga IN→OUT; combo: centroid + θ 25%: Künnarantaiga IN→OUT; combo: Moscow at +2 + θ 25%: Künnarantaiga IN→OUT; combo: official + θ 25%: Künnarantaiga IN→OUT

#### SENSITIVITY, split (a) (city-independent; recomputed here)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.60 | 41.83 | 42.72 | **31.36** |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.27 | 24.09 | 22.71 | **30.90** |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.08 | 7.12 | 7.10 | 11.95 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.19 | 8.24 | 8.11 | 7.20 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.81 | 16.90 | 17.00 | 12.47 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.23 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.96 | — | 0.89 | 0.84 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.28 | 1.05 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.19 | 0.20 | 0.19 | 0.63 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.09 | 0.33 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.18 | 0.48 |
| Kaliningrad (K-in) | — | — | — | 0.57 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — |

FLAGS (a), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49)

#### TIER SENSITIVITY (Ê_k in M under each (a) variant; T2-sized cut 10.198M)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 10.46 | 10.39 | 11.38 | 10.40 | 10.46 | 10.68 | **7.84** |
| Idelsk-Uralia (prov.) | 5.85 | 5.81 | 5.34 | 5.82 | 6.02 | 5.68 | 7.72 |
| Donska-Kubania (prov.) | 1.78 | 1.94 | 1.78 | 1.77 | 1.78 | 1.77 | 2.99 |
| Künnarantaiga | 2.06 | 2.05 | 1.85 | 2.05 | 2.06 | 2.03 | 1.80 |
| Siberia | 4.23 | 4.20 | 4.02 | 4.20 | 4.23 | 4.25 | 3.12 |
| Tuva | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.06 |
| Karelia | 0.24 | 0.24 | 0.30 | 0.24 | — | 0.22 | 0.21 |
| Chechnya | 0.07 | 0.07 | 0.05 | 0.07 | 0.07 | 0.07 | 0.26 |
| Dagestan | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.55 |
| Ingushetia | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 | 0.01 | 0.09 |
| Kabardino-Balkaria | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.05 | 0.16 |
| Karachay-Cherkessia | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.08 |
| North Ossetia-Alania | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.04 | 0.12 |
| Kaliningrad (K-in) | — | — | — | 0.14 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.07 | — | — |

### 1.6 Reading the output for Davis (DERIVED; arithmetic only)
- **Split (a) and split (b) coincide here**, because no successor lies outside the window: Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06% (of the former Russia share; sum 100%). In city-share terms (× 5.64%, DERIVED): Russia 2.36% · Idelsk-Uralia (prov.) 1.32% · Siberia 0.95% · Künnarantaiga 0.46% · Donska-Kubania (prov.) 0.40% · the eight smaller successors together 0.14% (each figure rounded).
- **Counts:** the tables above; each column sums exactly to 34,206 robots and 32,472 humans; the rounding rule is largest remainder (§0.2).
- **Effective tier (informational):** **Russia** Ê = 10.458M, **2.5% above** the 10.198M cut that the city's T2|T3 gap (Australia 13M | Thailand 8M) implies → **Significant**, a knife-edge. **Idelsk-Uralia (prov.)** 5.85M, **Siberia** 4.23M, **Künnarantaiga** 2.06M, **Donska-Kubania (prov.)** 1.78M → **Notable** (all inside the window). **Karelia, Dagestan, Chechnya, Kabardino-Balkaria, North Ossetia-Alania, Karachay-Cherkessia, Tuva and Ingushetia** (0.016M to 0.242M) → Notable by the window rule but **every one is below the 0.6M smallest pool the census carries** (`UEIC` L1089); whether they would appear at all is **NOT FOUND**.
- **Sensitivities that move a share by more than 5 points (flagged):**
  - **θ = 25%** (and every combination with it): **Künnarantaiga drops out** (8.24 → 0), because its only zone at or above 25% is +9 (49.6% of its pool; d = 4). The other twelve rise pro rata (Russia 41.83 → 45.59).
  - **(b-sub):** Künnarantaiga **8.24 → 2.74 (−5.50)**: only Irkutsk, Buryatia (+7) and Chita (+8), 31.4% of its pool, lie within ±3; Russia rises to 44.34.
  - **Population only** (no income factor): Russia **41.83 → 31.36 (−10.47)**, Idelsk-Uralia (prov.) **23.41 → 30.90 (+7.49)**; Donska-Kubania +4.83 and Siberia −4.43 stay under the line. This holds for (a) and (b) alike, and it moves Russia's Ê to 7.84M, **below the T2 cut (Significant → Notable)**.
- **Sensitivities that move nothing by more than 5 points:** V1c (largest move Donska-Kubania +0.65), V2 (Russia +3.70), K-in (Kaliningrad is outside, so (b) is unchanged), C-15 (Idelsk-Uralia +0.68; Finland's piece 0.29), θ = 5%, official zones, centroid zones, the three knife-edge cities, no Gini (Russia +0.89).
- **Window membership flips:** Künnarantaiga at θ = 25% (alone and in all three θ-25% combinations). No other.

### 1.7 NOT FOUND for Davis
The First Interwar record itself (every input is a present-day stand-in) · the meaningful-share threshold θ (`UEIC` L46–53 bound it above 2.5% but give no number) · a number for "large pool" (`UEIC` L31) · whether a floor excludes pools below 0.6M · the Gini penalty's functional form (`UEIC` L1057; the form used is RS1's convention).

---

## 2 · Zhongshan (solar UTC +5)

**City inputs (SOURCED):** ~69°22'S 76°22'E (`UEIC` L547); 76.3667°E ÷ 15 = 5.091 → **solar UTC +5** (`UEIC` L28 rule). Window **+2 … +8**. **Former Russia share 5.72%**, tier Significant; **Census I: 34,005 robots, 33,229 humans** (brief L30; the city's `Specs` row, `Specs/Mirny subnet/Zhongshan.md` L36, gives the same figures). **Tier lists:** `UEIC` L551–555 (the pool-rule ranking: Primary China; Significant Japan 65M, Germany 46M, UK 32M, South Korea 26M, Russia 25M, Indonesia 16M, Australia 13M; Notable Thailand 8M down to Latvia and Estonia 0.6M). ⚠ The city's `Specs` table is hand-adjusted (`Specs/Mirny subnet/Zhongshan.md` L20–22): Significant South Korea, Japan, Germany, Russia, Australia; **Indonesia (16M) demoted to Notable**; no UK.

**Status line, plain:** the First Interwar record does not exist; these are present-day regional figures standing in for it; nothing here is a ruling or a recommendation.

### 2.1 Which successors lie inside Zhongshan's window
**Inside (primary): all thirteen successors** — Russia (d = 2), Idelsk-Uralia (prov.) (d = 1), Donska-Kubania (prov.) (d = 2), Künnarantaiga (d = 2, through its +7 zone: Irkutsk and Ulan-Ude), Siberia (**d = 0**, through its +5 zone: Surgut, Omsk, Noyabrsk), Tuva (d = 1), Karelia (d = 3, at the edge), and the six North Caucasus republics (d = 2). **Outside: none.** Under the variants: **Kaliningrad (K-in) is outside** (solar +1, d = 4; inside under official zones, +2, d = 3); **Finland's Republic-of-Karelia piece (C-15) is inside** (+2, d = 3).

### 2.2 to 2.5 · Raw script output (`cities.py 2`, pasted unedited)

`CITY 2 Zhongshan: lon 76.3667E / 15 = 5.0911 -> solar UTC +5; window +2 ... +8`

#### WINDOW (primary: V1 · K-out · INIT · solar S7 · θ 10%; θ 5% / 25%, official and centroid shown for membership only)

| Successor | q(z), solar, primary | Z(10%) | d | Inside ±3? | θ 5%: d / in | θ 25%: d / in | official: Z(10%), d / in | centroid: Z(10%), d / in |
|---|---|---|--:|:-:|:-:|:-:|---|---|
| Russia | +2: 28.8% · +3: 71.2% | {+2,+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+2,+3}, 2 / IN |
| Idelsk-Uralia (prov.) | +3: 57.1% · +4: 42.9% | {+3,+4} | 1 | **IN** | 1 / IN | 1 / IN | {+3,+4,+5}, 0 / IN | {+3,+4}, 1 / IN |
| Donska-Kubania (prov.) | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Künnarantaiga | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7,+9,+10} | 2 | **IN** | 2 / IN | 4 / OUT | {+8,+9,+10,+11}, 3 / IN | {+7,+9,+10}, 2 / IN |
| Siberia | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5,+6} | 0 | **IN** | 0 / IN | 0 / IN | {+5,+7}, 0 / IN | {+5,+6}, 0 / IN |
| Tuva | +6: 100.0% | {+6} | 1 | **IN** | 1 / IN | 1 / IN | {+7}, 2 / IN | {+6}, 1 / IN |
| Karelia | +2: 100.0% | {+2} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 2 / IN | {+2}, 3 / IN |
| Chechnya | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Dagestan | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Ingushetia | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Kabardino-Balkaria | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Karachay-Cherkessia | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| North Ossetia-Alania | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Kaliningrad (K-in) *(K-in only)* | +1: 100.0% | {+1} | 4 | **OUT** | same | same | {+2}, 3 / IN | {+1}, 4 / OUT |
| Finland, Rep. of Karelia (C-15) *(C-15 only)* | +2: 100.0% | {+2} | 3 | **IN** | same | same | {+3}, 2 / IN | {+2}, 3 / IN |
| Idelsk-Uralia (prov.) under C-15 *(with Murmansk)* | +2: 2.8% · +3: 55.5% · +4: 41.7% | {+3,+4} | 1 | **IN** | — | — | — | — |

INSIDE (primary): Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Künnarantaiga, Siberia, Tuva, Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania
OUTSIDE (primary): none

#### SPLIT (primary)

Σ W (all) = 114.0887 tn RUB · Σ W (inside window) = 114.0887 tn RUB · Σ W_c (b-sub, units with |z_s − 5| ≤ 3) = 107.6369 tn RUB

| Successor | W_k (tn RUB) | **(a) % = W_k ÷ ΣW** | Inside? | **(b) % = W_k·I ÷ Σ W·I** | W_k,c (tn RUB) | (b-sub) % |
|---|--:|--:|:-:|--:|--:|--:|
| Russia | 47.7264 | 41.83 | IN | 41.83 | 47.7264 | 44.34 |
| Idelsk-Uralia (prov.) | 26.7038 | 23.41 | IN | 23.41 | 26.7038 | 24.81 |
| Donska-Kubania (prov.) | 8.1252 | 7.12 | IN | 7.12 | 8.1252 | 7.55 |
| Künnarantaiga | 9.4017 | 8.24 | IN | 8.24 | 2.9499 | 2.74 |
| Siberia | 19.2836 | 16.90 | IN | 16.90 | 19.2836 | 17.92 |
| Tuva | 0.0964 | 0.08 | IN | 0.08 | 0.0964 | 0.09 |
| Karelia | 1.1062 | 0.97 | IN | 0.97 | 1.1062 | 1.03 |
| Chechnya | 0.3272 | 0.29 | IN | 0.29 | 0.3272 | 0.30 |
| Dagestan | 0.6996 | 0.61 | IN | 0.61 | 0.6996 | 0.65 |
| Ingushetia | 0.0718 | 0.06 | IN | 0.06 | 0.0718 | 0.07 |
| Kabardino-Balkaria | 0.2225 | 0.20 | IN | 0.20 | 0.2225 | 0.21 |
| Karachay-Cherkessia | 0.1113 | 0.10 | IN | 0.10 | 0.1113 | 0.10 |
| North Ossetia-Alania | 0.2131 | 0.19 | IN | 0.19 | 0.2131 | 0.20 |
| **Sum** | 114.0887 | 100.00 | | 100.00 | 107.6369 | 100.00 |

#### COUNTS (largest remainder / Hamilton; ties to larger W_k)

Robots R = 34,005 · Humans H = 33,229. Units left after flooring, given one each to the largest remainders: (a) robots 6, humans 6; (b) robots 6, humans 6.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans |
|---|--:|--:|--:|--:|
| Russia | 14,225 | 13,901 | 14,225 | 13,901 |
| Idelsk-Uralia (prov.) | 7,959 | 7,778 | 7,959 | 7,778 |
| Donska-Kubania (prov.) | 2,422 | 2,367 | 2,422 | 2,367 |
| Künnarantaiga | 2,802 | 2,738 | 2,802 | 2,738 |
| Siberia | 5,748 | 5,616 | 5,748 | 5,616 |
| Tuva | 29 | 28 | 29 | 28 |
| Karelia | 330 | 322 | 330 | 322 |
| Chechnya | 97 | 95 | 97 | 95 |
| Dagestan | 209 | 204 | 209 | 204 |
| Ingushetia | 21 | 21 | 21 | 21 |
| Kabardino-Balkaria | 66 | 65 | 66 | 65 |
| Karachay-Cherkessia | 33 | 32 | 33 | 32 |
| North Ossetia-Alania | 64 | 62 | 64 | 62 |
| **Sum** | 34,005 | 33,229 | 34,005 | 33,229 |

#### TIERS (Ê_k = 25M × (a) share; city T2 floor 13M, T3 top 8M; break at the larger sub-gap ⇔ Ê ≥ √(13×8) = 10.198M is T2-sized)

| Successor | Ê_k (M) | d | Size class | Effective tier (informational) |
|---|--:|--:|---|---|
| Russia | 10.458 | 2 | T2-sized | Significant |
| Idelsk-Uralia (prov.) | 5.852 | 1 | T3-sized | Notable |
| Donska-Kubania (prov.) | 1.780 | 2 | T3-sized | Notable |
| Künnarantaiga | 2.060 | 2 | T3-sized | Notable |
| Siberia | 4.226 | 0 | T3-sized | Notable |
| Tuva | 0.021 | 1 | T3-sized | Notable ⚠ below 0.6M |
| Karelia | 0.242 | 3 | T3-sized | Notable ⚠ below 0.6M |
| Chechnya | 0.072 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Dagestan | 0.153 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Ingushetia | 0.016 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Kabardino-Balkaria | 0.049 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Karachay-Cherkessia | 0.024 | 2 | T3-sized | Notable ⚠ below 0.6M |
| North Ossetia-Alania | 0.047 | 2 | T3-sized | Notable ⚠ below 0.6M |

Mechanical re-finding over the merged ranking, three largest ratio gaps: China 210.00M → Japan 65.000M = 3.23× · Estonia 0.60M → Karelia 0.242M = 2.48× · Dagestan 0.15M → Chechnya 0.072M = 2.14×

#### SENSITIVITY, split (b) (% of the former Russia share; bold = moves more than 5 points from primary; OUT = outside the window)

| Successor | primary | V1c | V2 | K-in | C-15 | θ 5% | θ 25% | official zones | centroid (S7 alt.) | Moscow at +2 | Amur at +8 | Sakhalin at +9 | no Gini (P×y2024) | P only | b-sub (unit level) | combo: centroid + θ 25% | combo: Moscow at +2 + θ 25% | combo: official + θ 25% | combo: official + θ 5% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.83 | 41.83 | 41.83 | 45.59 | 41.83 | 41.83 | 41.83 | 41.83 | 41.83 | 42.72 | **31.36** | 44.34 | 45.59 | 45.59 | 45.59 | 41.83 |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.41 | 24.09 | 23.41 | 25.51 | 23.41 | 23.41 | 23.41 | 23.41 | 23.41 | 22.71 | **30.90** | 24.81 | 25.51 | 25.51 | 25.51 | 23.41 |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.12 | 7.12 | 7.12 | 7.76 | 7.12 | 7.12 | 7.12 | 7.12 | 7.12 | 7.10 | 11.95 | 7.55 | 7.76 | 7.76 | 7.76 | 7.12 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.24 | 8.24 | 8.24 | **OUT** | 8.24 | 8.24 | 8.24 | 8.24 | 8.24 | 8.11 | 7.20 | **2.74** | **OUT** | **OUT** | **OUT** | 8.24 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.90 | 16.90 | 16.90 | 18.42 | 16.90 | 16.90 | 16.90 | 16.90 | 16.90 | 17.00 | 12.47 | 17.92 | 18.42 | 18.42 | 18.42 | 16.90 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.09 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.23 | 0.09 | 0.09 | 0.09 | 0.09 | 0.08 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.97 | — | 0.97 | 1.06 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.89 | 0.84 | 1.03 | 1.06 | 1.06 | 1.06 | 0.97 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.29 | 0.31 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.28 | 1.05 | 0.30 | 0.31 | 0.31 | 0.31 | 0.29 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.67 | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 | 0.65 | 0.67 | 0.67 | 0.67 | 0.61 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.07 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 | 0.07 | 0.07 | 0.07 | 0.07 | 0.06 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.20 | 0.20 | 0.20 | 0.21 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 0.19 | 0.63 | 0.21 | 0.21 | 0.21 | 0.21 | 0.20 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.10 | 0.11 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.09 | 0.33 | 0.10 | 0.11 | 0.11 | 0.11 | 0.10 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.19 | 0.20 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.18 | 0.48 | 0.20 | 0.20 | 0.20 | 0.20 | 0.19 |
| Kaliningrad (K-in) | — | — | — | OUT | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

FLAGS (b), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49); θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); b-sub (unit level): Künnarantaiga 8.24 → 2.74 (-5.50); combo: centroid + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); combo: Moscow at +2 + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); combo: official + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24)
WINDOW FLIPS vs primary: θ 25%: Künnarantaiga IN→OUT; combo: centroid + θ 25%: Künnarantaiga IN→OUT; combo: Moscow at +2 + θ 25%: Künnarantaiga IN→OUT; combo: official + θ 25%: Künnarantaiga IN→OUT

#### SENSITIVITY, split (a) (city-independent; recomputed here)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.60 | 41.83 | 42.72 | **31.36** |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.27 | 24.09 | 22.71 | **30.90** |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.08 | 7.12 | 7.10 | 11.95 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.19 | 8.24 | 8.11 | 7.20 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.81 | 16.90 | 17.00 | 12.47 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.23 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.96 | — | 0.89 | 0.84 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.28 | 1.05 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.19 | 0.20 | 0.19 | 0.63 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.09 | 0.33 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.18 | 0.48 |
| Kaliningrad (K-in) | — | — | — | 0.57 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — |

FLAGS (a), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49)

#### TIER SENSITIVITY (Ê_k in M under each (a) variant; T2-sized cut 10.198M)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 10.46 | 10.39 | 11.38 | 10.40 | 10.46 | 10.68 | **7.84** |
| Idelsk-Uralia (prov.) | 5.85 | 5.81 | 5.34 | 5.82 | 6.02 | 5.68 | 7.72 |
| Donska-Kubania (prov.) | 1.78 | 1.94 | 1.78 | 1.77 | 1.78 | 1.77 | 2.99 |
| Künnarantaiga | 2.06 | 2.05 | 1.85 | 2.05 | 2.06 | 2.03 | 1.80 |
| Siberia | 4.23 | 4.20 | 4.02 | 4.20 | 4.23 | 4.25 | 3.12 |
| Tuva | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.06 |
| Karelia | 0.24 | 0.24 | 0.30 | 0.24 | — | 0.22 | 0.21 |
| Chechnya | 0.07 | 0.07 | 0.05 | 0.07 | 0.07 | 0.07 | 0.26 |
| Dagestan | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.55 |
| Ingushetia | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 | 0.01 | 0.09 |
| Kabardino-Balkaria | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.05 | 0.16 |
| Karachay-Cherkessia | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.08 |
| North Ossetia-Alania | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.04 | 0.12 |
| Kaliningrad (K-in) | — | — | — | 0.14 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.07 | — | — |

### 2.6 Reading the output for Zhongshan (DERIVED; arithmetic only)
- **Split (a) and split (b) coincide here**, because no successor lies outside the window: Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06% (of the former Russia share; sum 100%). In city-share terms (× 5.72%, DERIVED): Russia 2.39% · Idelsk-Uralia (prov.) 1.34% · Siberia 0.97% · Künnarantaiga 0.47% · Donska-Kubania (prov.) 0.41% · the eight smaller successors together 0.14% (each figure rounded).
- **Counts:** the tables above; each column sums exactly to 34,005 robots and 33,229 humans; the rounding rule is largest remainder (§0.2).
- **Effective tier (informational):** **Russia** Ê = 10.458M, **2.5% above** the 10.198M cut that the city's T2|T3 gap (Australia 13M | Thailand 8M) implies → **Significant**, a knife-edge. **Idelsk-Uralia (prov.)** 5.85M, **Siberia** 4.23M, **Künnarantaiga** 2.06M, **Donska-Kubania (prov.)** 1.78M → **Notable** (all inside the window). **Karelia, Dagestan, Chechnya, Kabardino-Balkaria, North Ossetia-Alania, Karachay-Cherkessia, Tuva and Ingushetia** (0.016M to 0.242M) → Notable by the window rule but **every one is below the 0.6M smallest pool the census carries** (`UEIC` L1089); whether they would appear at all is **NOT FOUND**. ⚠ **Under the city's own `Specs` tier lists the reading changes:** there Indonesia (16M) sits in Notable while Australia (13M) sits in Significant, so the Specs boundary is not a pool boundary, and a 10.46M Russia falls inside the Specs table's Notable pool range (16M down to 0.6M) → **Notable** under that reading. Which list the tier rule should be read against is not settled by any file (NOT FOUND).
- **Sensitivities that move a share by more than 5 points (flagged):**
  - **θ = 25%** (and every combination with it): **Künnarantaiga drops out** (8.24 → 0), because its only zone at or above 25% is +9 (49.6% of its pool; d = 4). The other twelve rise pro rata (Russia 41.83 → 45.59).
  - **(b-sub):** Künnarantaiga **8.24 → 2.74 (−5.50)**: only Irkutsk, Buryatia (+7) and Chita (+8), 31.4% of its pool, lie within ±3; Russia rises to 44.34.
  - **Population only** (no income factor): Russia **41.83 → 31.36 (−10.47)**, Idelsk-Uralia (prov.) **23.41 → 30.90 (+7.49)**; Donska-Kubania +4.83 and Siberia −4.43 stay under the line. This holds for (a) and (b) alike, and it moves Russia's Ê to 7.84M, **below the T2 cut (Significant → Notable)**.
- **Sensitivities that move nothing by more than 5 points:** V1c (largest move Donska-Kubania +0.65), V2 (Russia +3.70), K-in (Kaliningrad is outside, so (b) is unchanged), C-15 (Idelsk-Uralia +0.68; Finland's piece 0.29), θ = 5%, official zones, centroid zones, the three knife-edge cities, no Gini (Russia +0.89).
- **Window membership flips:** Künnarantaiga at θ = 25% (alone and in all three θ-25% combinations). No other.

### 2.7 NOT FOUND for Zhongshan
The First Interwar record itself (every input is a present-day stand-in) · the meaningful-share threshold θ (`UEIC` L46–53 bound it above 2.5% but give no number) · a number for "large pool" (`UEIC` L31) · whether a floor excludes pools below 0.6M · the Gini penalty's functional form (`UEIC` L1057; the form used is RS1's convention). · which tier list (the `UEIC` pool ranking or the hand-adjusted `Specs` table) governs a successor's tier here.

---

## 3 · Shirayuki (solar UTC +5)

**City inputs (SOURCED):** ~69°24'S 76°11'E (`UEIC` L507); 76.1833°E ÷ 15 = 5.079 → **solar UTC +5** (`UEIC` L28 rule). Window **+2 … +8**. **Former Russia share 8.61%**, tier Significant; **Census I: 47,651 robots, 45,716 humans** (brief L28; the city's `Specs` row, `Specs/Mirny subnet/Shirayuki.md` L60, gives the same figures). **Tier lists:** `UEIC` L511–515 (the pool-rule ranking: Primary China; Significant Japan 65M, Germany 46M, UK 32M, South Korea 26M, Russia 25M, Indonesia 16M, Australia 13M; Notable Thailand 8M down to Latvia and Estonia 0.6M). ⚠ The city's `Specs` table is hand-adjusted (`Specs/Mirny subnet/Shirayuki.md` L44–48): Primary Japan; Significant Australia, Russia, South Korea, China, Germany; no UK or Indonesia; Notable Romania down to Estonia. Its Significant floor (Australia 13M) and Notable top (Thailand 8M) are the same pools as in the `UEIC` ranking, so the cut is the same under either list.

**Status line, plain:** the First Interwar record does not exist; these are present-day regional figures standing in for it; nothing here is a ruling or a recommendation.

### 3.1 Which successors lie inside Shirayuki's window
**Inside (primary): all thirteen successors** — Russia (d = 2), Idelsk-Uralia (prov.) (d = 1), Donska-Kubania (prov.) (d = 2), Künnarantaiga (d = 2, through its +7 zone: Irkutsk and Ulan-Ude), Siberia (**d = 0**, through its +5 zone: Surgut, Omsk, Noyabrsk), Tuva (d = 1), Karelia (d = 3, at the edge), and the six North Caucasus republics (d = 2). **Outside: none.** Under the variants: **Kaliningrad (K-in) is outside** (solar +1, d = 4; inside under official zones, +2, d = 3); **Finland's Republic-of-Karelia piece (C-15) is inside** (+2, d = 3).

### 3.2 to 3.5 · Raw script output (`cities.py 3`, pasted unedited)

`CITY 3 Shirayuki: lon 76.1833E / 15 = 5.0789 -> solar UTC +5; window +2 ... +8`

#### WINDOW (primary: V1 · K-out · INIT · solar S7 · θ 10%; θ 5% / 25%, official and centroid shown for membership only)

| Successor | q(z), solar, primary | Z(10%) | d | Inside ±3? | θ 5%: d / in | θ 25%: d / in | official: Z(10%), d / in | centroid: Z(10%), d / in |
|---|---|---|--:|:-:|:-:|:-:|---|---|
| Russia | +2: 28.8% · +3: 71.2% | {+2,+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+2,+3}, 2 / IN |
| Idelsk-Uralia (prov.) | +3: 57.1% · +4: 42.9% | {+3,+4} | 1 | **IN** | 1 / IN | 1 / IN | {+3,+4,+5}, 0 / IN | {+3,+4}, 1 / IN |
| Donska-Kubania (prov.) | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Künnarantaiga | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7,+9,+10} | 2 | **IN** | 2 / IN | 4 / OUT | {+8,+9,+10,+11}, 3 / IN | {+7,+9,+10}, 2 / IN |
| Siberia | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5,+6} | 0 | **IN** | 0 / IN | 0 / IN | {+5,+7}, 0 / IN | {+5,+6}, 0 / IN |
| Tuva | +6: 100.0% | {+6} | 1 | **IN** | 1 / IN | 1 / IN | {+7}, 2 / IN | {+6}, 1 / IN |
| Karelia | +2: 100.0% | {+2} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 2 / IN | {+2}, 3 / IN |
| Chechnya | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Dagestan | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Ingushetia | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Kabardino-Balkaria | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Karachay-Cherkessia | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| North Ossetia-Alania | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Kaliningrad (K-in) *(K-in only)* | +1: 100.0% | {+1} | 4 | **OUT** | same | same | {+2}, 3 / IN | {+1}, 4 / OUT |
| Finland, Rep. of Karelia (C-15) *(C-15 only)* | +2: 100.0% | {+2} | 3 | **IN** | same | same | {+3}, 2 / IN | {+2}, 3 / IN |
| Idelsk-Uralia (prov.) under C-15 *(with Murmansk)* | +2: 2.8% · +3: 55.5% · +4: 41.7% | {+3,+4} | 1 | **IN** | — | — | — | — |

INSIDE (primary): Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Künnarantaiga, Siberia, Tuva, Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania
OUTSIDE (primary): none

#### SPLIT (primary)

Σ W (all) = 114.0887 tn RUB · Σ W (inside window) = 114.0887 tn RUB · Σ W_c (b-sub, units with |z_s − 5| ≤ 3) = 107.6369 tn RUB

| Successor | W_k (tn RUB) | **(a) % = W_k ÷ ΣW** | Inside? | **(b) % = W_k·I ÷ Σ W·I** | W_k,c (tn RUB) | (b-sub) % |
|---|--:|--:|:-:|--:|--:|--:|
| Russia | 47.7264 | 41.83 | IN | 41.83 | 47.7264 | 44.34 |
| Idelsk-Uralia (prov.) | 26.7038 | 23.41 | IN | 23.41 | 26.7038 | 24.81 |
| Donska-Kubania (prov.) | 8.1252 | 7.12 | IN | 7.12 | 8.1252 | 7.55 |
| Künnarantaiga | 9.4017 | 8.24 | IN | 8.24 | 2.9499 | 2.74 |
| Siberia | 19.2836 | 16.90 | IN | 16.90 | 19.2836 | 17.92 |
| Tuva | 0.0964 | 0.08 | IN | 0.08 | 0.0964 | 0.09 |
| Karelia | 1.1062 | 0.97 | IN | 0.97 | 1.1062 | 1.03 |
| Chechnya | 0.3272 | 0.29 | IN | 0.29 | 0.3272 | 0.30 |
| Dagestan | 0.6996 | 0.61 | IN | 0.61 | 0.6996 | 0.65 |
| Ingushetia | 0.0718 | 0.06 | IN | 0.06 | 0.0718 | 0.07 |
| Kabardino-Balkaria | 0.2225 | 0.20 | IN | 0.20 | 0.2225 | 0.21 |
| Karachay-Cherkessia | 0.1113 | 0.10 | IN | 0.10 | 0.1113 | 0.10 |
| North Ossetia-Alania | 0.2131 | 0.19 | IN | 0.19 | 0.2131 | 0.20 |
| **Sum** | 114.0887 | 100.00 | | 100.00 | 107.6369 | 100.00 |

#### COUNTS (largest remainder / Hamilton; ties to larger W_k)

Robots R = 47,651 · Humans H = 45,716. Units left after flooring, given one each to the largest remainders: (a) robots 6, humans 5; (b) robots 6, humans 5.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans |
|---|--:|--:|--:|--:|
| Russia | 19,934 | 19,124 | 19,934 | 19,124 |
| Idelsk-Uralia (prov.) | 11,153 | 10,700 | 11,153 | 10,700 |
| Donska-Kubania (prov.) | 3,394 | 3,256 | 3,394 | 3,256 |
| Künnarantaiga | 3,927 | 3,767 | 3,927 | 3,767 |
| Siberia | 8,054 | 7,727 | 8,054 | 7,727 |
| Tuva | 40 | 39 | 40 | 39 |
| Karelia | 462 | 443 | 462 | 443 |
| Chechnya | 137 | 131 | 137 | 131 |
| Dagestan | 292 | 280 | 292 | 280 |
| Ingushetia | 30 | 29 | 30 | 29 |
| Kabardino-Balkaria | 93 | 89 | 93 | 89 |
| Karachay-Cherkessia | 46 | 45 | 46 | 45 |
| North Ossetia-Alania | 89 | 86 | 89 | 86 |
| **Sum** | 47,651 | 45,716 | 47,651 | 45,716 |

#### TIERS (Ê_k = 25M × (a) share; city T2 floor 13M, T3 top 8M; break at the larger sub-gap ⇔ Ê ≥ √(13×8) = 10.198M is T2-sized)

| Successor | Ê_k (M) | d | Size class | Effective tier (informational) |
|---|--:|--:|---|---|
| Russia | 10.458 | 2 | T2-sized | Significant |
| Idelsk-Uralia (prov.) | 5.852 | 1 | T3-sized | Notable |
| Donska-Kubania (prov.) | 1.780 | 2 | T3-sized | Notable |
| Künnarantaiga | 2.060 | 2 | T3-sized | Notable |
| Siberia | 4.226 | 0 | T3-sized | Notable |
| Tuva | 0.021 | 1 | T3-sized | Notable ⚠ below 0.6M |
| Karelia | 0.242 | 3 | T3-sized | Notable ⚠ below 0.6M |
| Chechnya | 0.072 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Dagestan | 0.153 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Ingushetia | 0.016 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Kabardino-Balkaria | 0.049 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Karachay-Cherkessia | 0.024 | 2 | T3-sized | Notable ⚠ below 0.6M |
| North Ossetia-Alania | 0.047 | 2 | T3-sized | Notable ⚠ below 0.6M |

Mechanical re-finding over the merged ranking, three largest ratio gaps: China 210.00M → Japan 65.000M = 3.23× · Estonia 0.60M → Karelia 0.242M = 2.48× · Dagestan 0.15M → Chechnya 0.072M = 2.14×

#### SENSITIVITY, split (b) (% of the former Russia share; bold = moves more than 5 points from primary; OUT = outside the window)

| Successor | primary | V1c | V2 | K-in | C-15 | θ 5% | θ 25% | official zones | centroid (S7 alt.) | Moscow at +2 | Amur at +8 | Sakhalin at +9 | no Gini (P×y2024) | P only | b-sub (unit level) | combo: centroid + θ 25% | combo: Moscow at +2 + θ 25% | combo: official + θ 25% | combo: official + θ 5% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.83 | 41.83 | 41.83 | 45.59 | 41.83 | 41.83 | 41.83 | 41.83 | 41.83 | 42.72 | **31.36** | 44.34 | 45.59 | 45.59 | 45.59 | 41.83 |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.41 | 24.09 | 23.41 | 25.51 | 23.41 | 23.41 | 23.41 | 23.41 | 23.41 | 22.71 | **30.90** | 24.81 | 25.51 | 25.51 | 25.51 | 23.41 |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.12 | 7.12 | 7.12 | 7.76 | 7.12 | 7.12 | 7.12 | 7.12 | 7.12 | 7.10 | 11.95 | 7.55 | 7.76 | 7.76 | 7.76 | 7.12 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.24 | 8.24 | 8.24 | **OUT** | 8.24 | 8.24 | 8.24 | 8.24 | 8.24 | 8.11 | 7.20 | **2.74** | **OUT** | **OUT** | **OUT** | 8.24 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.90 | 16.90 | 16.90 | 18.42 | 16.90 | 16.90 | 16.90 | 16.90 | 16.90 | 17.00 | 12.47 | 17.92 | 18.42 | 18.42 | 18.42 | 16.90 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.09 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.23 | 0.09 | 0.09 | 0.09 | 0.09 | 0.08 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.97 | — | 0.97 | 1.06 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.89 | 0.84 | 1.03 | 1.06 | 1.06 | 1.06 | 0.97 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.29 | 0.31 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.28 | 1.05 | 0.30 | 0.31 | 0.31 | 0.31 | 0.29 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.67 | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 | 0.65 | 0.67 | 0.67 | 0.67 | 0.61 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.07 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 | 0.07 | 0.07 | 0.07 | 0.07 | 0.06 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.20 | 0.20 | 0.20 | 0.21 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 0.19 | 0.63 | 0.21 | 0.21 | 0.21 | 0.21 | 0.20 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.10 | 0.11 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.09 | 0.33 | 0.10 | 0.11 | 0.11 | 0.11 | 0.10 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.19 | 0.20 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.18 | 0.48 | 0.20 | 0.20 | 0.20 | 0.20 | 0.19 |
| Kaliningrad (K-in) | — | — | — | OUT | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

FLAGS (b), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49); θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); b-sub (unit level): Künnarantaiga 8.24 → 2.74 (-5.50); combo: centroid + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); combo: Moscow at +2 + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); combo: official + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24)
WINDOW FLIPS vs primary: θ 25%: Künnarantaiga IN→OUT; combo: centroid + θ 25%: Künnarantaiga IN→OUT; combo: Moscow at +2 + θ 25%: Künnarantaiga IN→OUT; combo: official + θ 25%: Künnarantaiga IN→OUT

#### SENSITIVITY, split (a) (city-independent; recomputed here)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.60 | 41.83 | 42.72 | **31.36** |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.27 | 24.09 | 22.71 | **30.90** |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.08 | 7.12 | 7.10 | 11.95 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.19 | 8.24 | 8.11 | 7.20 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.81 | 16.90 | 17.00 | 12.47 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.23 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.96 | — | 0.89 | 0.84 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.28 | 1.05 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.19 | 0.20 | 0.19 | 0.63 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.09 | 0.33 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.18 | 0.48 |
| Kaliningrad (K-in) | — | — | — | 0.57 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — |

FLAGS (a), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49)

#### TIER SENSITIVITY (Ê_k in M under each (a) variant; T2-sized cut 10.198M)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 10.46 | 10.39 | 11.38 | 10.40 | 10.46 | 10.68 | **7.84** |
| Idelsk-Uralia (prov.) | 5.85 | 5.81 | 5.34 | 5.82 | 6.02 | 5.68 | 7.72 |
| Donska-Kubania (prov.) | 1.78 | 1.94 | 1.78 | 1.77 | 1.78 | 1.77 | 2.99 |
| Künnarantaiga | 2.06 | 2.05 | 1.85 | 2.05 | 2.06 | 2.03 | 1.80 |
| Siberia | 4.23 | 4.20 | 4.02 | 4.20 | 4.23 | 4.25 | 3.12 |
| Tuva | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.06 |
| Karelia | 0.24 | 0.24 | 0.30 | 0.24 | — | 0.22 | 0.21 |
| Chechnya | 0.07 | 0.07 | 0.05 | 0.07 | 0.07 | 0.07 | 0.26 |
| Dagestan | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.55 |
| Ingushetia | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 | 0.01 | 0.09 |
| Kabardino-Balkaria | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.05 | 0.16 |
| Karachay-Cherkessia | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.08 |
| North Ossetia-Alania | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.04 | 0.12 |
| Kaliningrad (K-in) | — | — | — | 0.14 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.07 | — | — |

### 3.6 Reading the output for Shirayuki (DERIVED; arithmetic only)
- **Split (a) and split (b) coincide here**, because no successor lies outside the window: Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06% (of the former Russia share; sum 100%). In city-share terms (× 8.61%, DERIVED): Russia 3.60% · Idelsk-Uralia (prov.) 2.02% · Siberia 1.46% · Künnarantaiga 0.71% · Donska-Kubania (prov.) 0.61% · the eight smaller successors together 0.21% (each figure rounded).
- **Counts:** the tables above; each column sums exactly to 47,651 robots and 45,716 humans; the rounding rule is largest remainder (§0.2).
- **Effective tier (informational):** **Russia** Ê = 10.458M, **2.5% above** the 10.198M cut that the city's T2|T3 gap (Australia 13M | Thailand 8M) implies → **Significant**, a knife-edge. **Idelsk-Uralia (prov.)** 5.85M, **Siberia** 4.23M, **Künnarantaiga** 2.06M, **Donska-Kubania (prov.)** 1.78M → **Notable** (all inside the window). **Karelia, Dagestan, Chechnya, Kabardino-Balkaria, North Ossetia-Alania, Karachay-Cherkessia, Tuva and Ingushetia** (0.016M to 0.242M) → Notable by the window rule but **every one is below the 0.6M smallest pool the census carries** (`UEIC` L1089); whether they would appear at all is **NOT FOUND**.
- **Sensitivities that move a share by more than 5 points (flagged):**
  - **θ = 25%** (and every combination with it): **Künnarantaiga drops out** (8.24 → 0), because its only zone at or above 25% is +9 (49.6% of its pool; d = 4). The other twelve rise pro rata (Russia 41.83 → 45.59).
  - **(b-sub):** Künnarantaiga **8.24 → 2.74 (−5.50)**: only Irkutsk, Buryatia (+7) and Chita (+8), 31.4% of its pool, lie within ±3; Russia rises to 44.34.
  - **Population only** (no income factor): Russia **41.83 → 31.36 (−10.47)**, Idelsk-Uralia (prov.) **23.41 → 30.90 (+7.49)**; Donska-Kubania +4.83 and Siberia −4.43 stay under the line. This holds for (a) and (b) alike, and it moves Russia's Ê to 7.84M, **below the T2 cut (Significant → Notable)**.
- **Sensitivities that move nothing by more than 5 points:** V1c (largest move Donska-Kubania +0.65), V2 (Russia +3.70), K-in (Kaliningrad is outside, so (b) is unchanged), C-15 (Idelsk-Uralia +0.68; Finland's piece 0.29), θ = 5%, official zones, centroid zones, the three knife-edge cities, no Gini (Russia +0.89).
- **Window membership flips:** Künnarantaiga at θ = 25% (alone and in all three θ-25% combinations). No other.

### 3.7 NOT FOUND for Shirayuki
The First Interwar record itself (every input is a present-day stand-in) · the meaningful-share threshold θ (`UEIC` L46–53 bound it above 2.5% but give no number) · a number for "large pool" (`UEIC` L31) · whether a floor excludes pools below 0.6M · the Gini penalty's functional form (`UEIC` L1057; the form used is RS1's convention).

---

## 4 · Sinheung (solar UTC +5)

**City inputs (SOURCED):** ~69°22'S 76°22'E (`Specs/Mirny subnet/Sinheung.md` L3; `UEIC` L497 gives no coordinates); 76.3667°E ÷ 15 = 5.091 → **solar UTC +5** (`UEIC` L28 rule). Window **+2 … +8**. **Former Russia share 6.85%**, tier Significant; **Census I: 34,724 robots, 32,841 humans** (brief L29; the city's `Specs` row, `Specs/Mirny subnet/Sinheung.md` L92, gives the same figures). **Tier lists:** `UEIC` L499–503 (the raw pool ranking, which the section itself calls *"a record of the pre-correction baseline, not … current guidance"*, L497: Primary China; Significant Japan 65M, Germany 46M, UK 32M, South Korea 26M, Russia 25M, Indonesia 16M, Australia 13M; Notable Thailand 8M down to Latvia and Estonia 0.6M). **Authoritative per `UEIC` L497:** `Specs/Mirny subnet/Sinheung.md` L74–78, hand-adjusted 2026-07-06: Primary South Korea; Significant China, Japan, Germany, Russia, Indonesia, Australia; Notable Thailand, Estonia, Hungary, Lithuania, Malaysia, Vietnam, Philippines, Bulgaria, Latvia, South Africa. Its Significant floor (Australia 13M) and Notable top (Thailand 8M) are the same pools as in the raw ranking, so the cut is the same under either list. The Specs history (L112, L116) records that Russia's share was cut by 3.0 points by hand (9.85% → 6.85%); the split below divides the 6.85% that stands.

**Status line, plain:** the First Interwar record does not exist; these are present-day regional figures standing in for it; nothing here is a ruling or a recommendation.

### 4.1 Which successors lie inside Sinheung's window
**Inside (primary): all thirteen successors** — Russia (d = 2), Idelsk-Uralia (prov.) (d = 1), Donska-Kubania (prov.) (d = 2), Künnarantaiga (d = 2, through its +7 zone: Irkutsk and Ulan-Ude), Siberia (**d = 0**, through its +5 zone: Surgut, Omsk, Noyabrsk), Tuva (d = 1), Karelia (d = 3, at the edge), and the six North Caucasus republics (d = 2). **Outside: none.** Under the variants: **Kaliningrad (K-in) is outside** (solar +1, d = 4; inside under official zones, +2, d = 3); **Finland's Republic-of-Karelia piece (C-15) is inside** (+2, d = 3).

### 4.2 to 4.5 · Raw script output (`cities.py 4`, pasted unedited)

`CITY 4 Sinheung: lon 76.3667E / 15 = 5.0911 -> solar UTC +5; window +2 ... +8`

#### WINDOW (primary: V1 · K-out · INIT · solar S7 · θ 10%; θ 5% / 25%, official and centroid shown for membership only)

| Successor | q(z), solar, primary | Z(10%) | d | Inside ±3? | θ 5%: d / in | θ 25%: d / in | official: Z(10%), d / in | centroid: Z(10%), d / in |
|---|---|---|--:|:-:|:-:|:-:|---|---|
| Russia | +2: 28.8% · +3: 71.2% | {+2,+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+2,+3}, 2 / IN |
| Idelsk-Uralia (prov.) | +3: 57.1% · +4: 42.9% | {+3,+4} | 1 | **IN** | 1 / IN | 1 / IN | {+3,+4,+5}, 0 / IN | {+3,+4}, 1 / IN |
| Donska-Kubania (prov.) | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Künnarantaiga | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7,+9,+10} | 2 | **IN** | 2 / IN | 4 / OUT | {+8,+9,+10,+11}, 3 / IN | {+7,+9,+10}, 2 / IN |
| Siberia | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5,+6} | 0 | **IN** | 0 / IN | 0 / IN | {+5,+7}, 0 / IN | {+5,+6}, 0 / IN |
| Tuva | +6: 100.0% | {+6} | 1 | **IN** | 1 / IN | 1 / IN | {+7}, 2 / IN | {+6}, 1 / IN |
| Karelia | +2: 100.0% | {+2} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 2 / IN | {+2}, 3 / IN |
| Chechnya | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Dagestan | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Ingushetia | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Kabardino-Balkaria | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Karachay-Cherkessia | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| North Ossetia-Alania | +3: 100.0% | {+3} | 2 | **IN** | 2 / IN | 2 / IN | {+3}, 2 / IN | {+3}, 2 / IN |
| Kaliningrad (K-in) *(K-in only)* | +1: 100.0% | {+1} | 4 | **OUT** | same | same | {+2}, 3 / IN | {+1}, 4 / OUT |
| Finland, Rep. of Karelia (C-15) *(C-15 only)* | +2: 100.0% | {+2} | 3 | **IN** | same | same | {+3}, 2 / IN | {+2}, 3 / IN |
| Idelsk-Uralia (prov.) under C-15 *(with Murmansk)* | +2: 2.8% · +3: 55.5% · +4: 41.7% | {+3,+4} | 1 | **IN** | — | — | — | — |

INSIDE (primary): Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Künnarantaiga, Siberia, Tuva, Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania
OUTSIDE (primary): none

#### SPLIT (primary)

Σ W (all) = 114.0887 tn RUB · Σ W (inside window) = 114.0887 tn RUB · Σ W_c (b-sub, units with |z_s − 5| ≤ 3) = 107.6369 tn RUB

| Successor | W_k (tn RUB) | **(a) % = W_k ÷ ΣW** | Inside? | **(b) % = W_k·I ÷ Σ W·I** | W_k,c (tn RUB) | (b-sub) % |
|---|--:|--:|:-:|--:|--:|--:|
| Russia | 47.7264 | 41.83 | IN | 41.83 | 47.7264 | 44.34 |
| Idelsk-Uralia (prov.) | 26.7038 | 23.41 | IN | 23.41 | 26.7038 | 24.81 |
| Donska-Kubania (prov.) | 8.1252 | 7.12 | IN | 7.12 | 8.1252 | 7.55 |
| Künnarantaiga | 9.4017 | 8.24 | IN | 8.24 | 2.9499 | 2.74 |
| Siberia | 19.2836 | 16.90 | IN | 16.90 | 19.2836 | 17.92 |
| Tuva | 0.0964 | 0.08 | IN | 0.08 | 0.0964 | 0.09 |
| Karelia | 1.1062 | 0.97 | IN | 0.97 | 1.1062 | 1.03 |
| Chechnya | 0.3272 | 0.29 | IN | 0.29 | 0.3272 | 0.30 |
| Dagestan | 0.6996 | 0.61 | IN | 0.61 | 0.6996 | 0.65 |
| Ingushetia | 0.0718 | 0.06 | IN | 0.06 | 0.0718 | 0.07 |
| Kabardino-Balkaria | 0.2225 | 0.20 | IN | 0.20 | 0.2225 | 0.21 |
| Karachay-Cherkessia | 0.1113 | 0.10 | IN | 0.10 | 0.1113 | 0.10 |
| North Ossetia-Alania | 0.2131 | 0.19 | IN | 0.19 | 0.2131 | 0.20 |
| **Sum** | 114.0887 | 100.00 | | 100.00 | 107.6369 | 100.00 |

#### COUNTS (largest remainder / Hamilton; ties to larger W_k)

Robots R = 34,724 · Humans H = 32,841. Units left after flooring, given one each to the largest remainders: (a) robots 9, humans 6; (b) robots 9, humans 6.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans |
|---|--:|--:|--:|--:|
| Russia | 14,526 | 13,738 | 14,526 | 13,738 |
| Idelsk-Uralia (prov.) | 8,127 | 7,687 | 8,127 | 7,687 |
| Donska-Kubania (prov.) | 2,473 | 2,339 | 2,473 | 2,339 |
| Künnarantaiga | 2,861 | 2,706 | 2,861 | 2,706 |
| Siberia | 5,869 | 5,551 | 5,869 | 5,551 |
| Tuva | 29 | 28 | 29 | 28 |
| Karelia | 337 | 319 | 337 | 319 |
| Chechnya | 100 | 94 | 100 | 94 |
| Dagestan | 213 | 201 | 213 | 201 |
| Ingushetia | 22 | 21 | 22 | 21 |
| Kabardino-Balkaria | 68 | 64 | 68 | 64 |
| Karachay-Cherkessia | 34 | 32 | 34 | 32 |
| North Ossetia-Alania | 65 | 61 | 65 | 61 |
| **Sum** | 34,724 | 32,841 | 34,724 | 32,841 |

#### TIERS (Ê_k = 25M × (a) share; city T2 floor 13M, T3 top 8M; break at the larger sub-gap ⇔ Ê ≥ √(13×8) = 10.198M is T2-sized)

| Successor | Ê_k (M) | d | Size class | Effective tier (informational) |
|---|--:|--:|---|---|
| Russia | 10.458 | 2 | T2-sized | Significant |
| Idelsk-Uralia (prov.) | 5.852 | 1 | T3-sized | Notable |
| Donska-Kubania (prov.) | 1.780 | 2 | T3-sized | Notable |
| Künnarantaiga | 2.060 | 2 | T3-sized | Notable |
| Siberia | 4.226 | 0 | T3-sized | Notable |
| Tuva | 0.021 | 1 | T3-sized | Notable ⚠ below 0.6M |
| Karelia | 0.242 | 3 | T3-sized | Notable ⚠ below 0.6M |
| Chechnya | 0.072 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Dagestan | 0.153 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Ingushetia | 0.016 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Kabardino-Balkaria | 0.049 | 2 | T3-sized | Notable ⚠ below 0.6M |
| Karachay-Cherkessia | 0.024 | 2 | T3-sized | Notable ⚠ below 0.6M |
| North Ossetia-Alania | 0.047 | 2 | T3-sized | Notable ⚠ below 0.6M |

Mechanical re-finding over the merged ranking, three largest ratio gaps: China 210.00M → Japan 65.000M = 3.23× · Estonia 0.60M → Karelia 0.242M = 2.48× · Dagestan 0.15M → Chechnya 0.072M = 2.14×

#### SENSITIVITY, split (b) (% of the former Russia share; bold = moves more than 5 points from primary; OUT = outside the window)

| Successor | primary | V1c | V2 | K-in | C-15 | θ 5% | θ 25% | official zones | centroid (S7 alt.) | Moscow at +2 | Amur at +8 | Sakhalin at +9 | no Gini (P×y2024) | P only | b-sub (unit level) | combo: centroid + θ 25% | combo: Moscow at +2 + θ 25% | combo: official + θ 25% | combo: official + θ 5% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.83 | 41.83 | 41.83 | 45.59 | 41.83 | 41.83 | 41.83 | 41.83 | 41.83 | 42.72 | **31.36** | 44.34 | 45.59 | 45.59 | 45.59 | 41.83 |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.41 | 24.09 | 23.41 | 25.51 | 23.41 | 23.41 | 23.41 | 23.41 | 23.41 | 22.71 | **30.90** | 24.81 | 25.51 | 25.51 | 25.51 | 23.41 |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.12 | 7.12 | 7.12 | 7.76 | 7.12 | 7.12 | 7.12 | 7.12 | 7.12 | 7.10 | 11.95 | 7.55 | 7.76 | 7.76 | 7.76 | 7.12 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.24 | 8.24 | 8.24 | **OUT** | 8.24 | 8.24 | 8.24 | 8.24 | 8.24 | 8.11 | 7.20 | **2.74** | **OUT** | **OUT** | **OUT** | 8.24 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.90 | 16.90 | 16.90 | 18.42 | 16.90 | 16.90 | 16.90 | 16.90 | 16.90 | 17.00 | 12.47 | 17.92 | 18.42 | 18.42 | 18.42 | 16.90 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.09 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 | 0.23 | 0.09 | 0.09 | 0.09 | 0.09 | 0.08 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.97 | — | 0.97 | 1.06 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.89 | 0.84 | 1.03 | 1.06 | 1.06 | 1.06 | 0.97 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.29 | 0.31 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.28 | 1.05 | 0.30 | 0.31 | 0.31 | 0.31 | 0.29 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.67 | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 | 0.65 | 0.67 | 0.67 | 0.67 | 0.61 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.07 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 | 0.07 | 0.07 | 0.07 | 0.07 | 0.06 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.20 | 0.20 | 0.20 | 0.21 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 0.19 | 0.63 | 0.21 | 0.21 | 0.21 | 0.21 | 0.20 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.10 | 0.11 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.09 | 0.33 | 0.10 | 0.11 | 0.11 | 0.11 | 0.10 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.19 | 0.20 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.18 | 0.48 | 0.20 | 0.20 | 0.20 | 0.20 | 0.19 |
| Kaliningrad (K-in) | — | — | — | OUT | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

FLAGS (b), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49); θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); b-sub (unit level): Künnarantaiga 8.24 → 2.74 (-5.50); combo: centroid + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); combo: Moscow at +2 + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24); combo: official + θ 25%: Künnarantaiga 8.24 → 0.00 (-8.24)
WINDOW FLIPS vs primary: θ 25%: Künnarantaiga IN→OUT; combo: centroid + θ 25%: Künnarantaiga IN→OUT; combo: Moscow at +2 + θ 25%: Künnarantaiga IN→OUT; combo: official + θ 25%: Künnarantaiga IN→OUT

#### SENSITIVITY, split (a) (city-independent; recomputed here)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.60 | 41.83 | 42.72 | **31.36** |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.27 | 24.09 | 22.71 | **30.90** |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.08 | 7.12 | 7.10 | 11.95 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.19 | 8.24 | 8.11 | 7.20 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.81 | 16.90 | 17.00 | 12.47 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.23 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.96 | — | 0.89 | 0.84 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.28 | 1.05 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.19 | 0.20 | 0.19 | 0.63 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.09 | 0.33 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.18 | 0.48 |
| Kaliningrad (K-in) | — | — | — | 0.57 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — |

FLAGS (a), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49)

#### TIER SENSITIVITY (Ê_k in M under each (a) variant; T2-sized cut 10.198M)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 10.46 | 10.39 | 11.38 | 10.40 | 10.46 | 10.68 | **7.84** |
| Idelsk-Uralia (prov.) | 5.85 | 5.81 | 5.34 | 5.82 | 6.02 | 5.68 | 7.72 |
| Donska-Kubania (prov.) | 1.78 | 1.94 | 1.78 | 1.77 | 1.78 | 1.77 | 2.99 |
| Künnarantaiga | 2.06 | 2.05 | 1.85 | 2.05 | 2.06 | 2.03 | 1.80 |
| Siberia | 4.23 | 4.20 | 4.02 | 4.20 | 4.23 | 4.25 | 3.12 |
| Tuva | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.06 |
| Karelia | 0.24 | 0.24 | 0.30 | 0.24 | — | 0.22 | 0.21 |
| Chechnya | 0.07 | 0.07 | 0.05 | 0.07 | 0.07 | 0.07 | 0.26 |
| Dagestan | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.55 |
| Ingushetia | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 | 0.01 | 0.09 |
| Kabardino-Balkaria | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.05 | 0.16 |
| Karachay-Cherkessia | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.08 |
| North Ossetia-Alania | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.04 | 0.12 |
| Kaliningrad (K-in) | — | — | — | 0.14 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.07 | — | — |

### 4.6 Reading the output for Sinheung (DERIVED; arithmetic only)
- **Split (a) and split (b) coincide here**, because no successor lies outside the window: Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06% (of the former Russia share; sum 100%). In city-share terms (× 6.85%, DERIVED): Russia 2.87% · Idelsk-Uralia (prov.) 1.60% · Siberia 1.16% · Künnarantaiga 0.56% · Donska-Kubania (prov.) 0.49% · the eight smaller successors together 0.17% (each figure rounded).
- **Counts:** the tables above; each column sums exactly to 34,724 robots and 32,841 humans; the rounding rule is largest remainder (§0.2).
- **Effective tier (informational):** **Russia** Ê = 10.458M, **2.5% above** the 10.198M cut that the city's T2|T3 gap (Australia 13M | Thailand 8M) implies → **Significant**, a knife-edge. **Idelsk-Uralia (prov.)** 5.85M, **Siberia** 4.23M, **Künnarantaiga** 2.06M, **Donska-Kubania (prov.)** 1.78M → **Notable** (all inside the window). **Karelia, Dagestan, Chechnya, Kabardino-Balkaria, North Ossetia-Alania, Karachay-Cherkessia, Tuva and Ingushetia** (0.016M to 0.242M) → Notable by the window rule but **every one is below the 0.6M smallest pool the census carries** (`UEIC` L1089); whether they would appear at all is **NOT FOUND**.
- **Sensitivities that move a share by more than 5 points (flagged):**
  - **θ = 25%** (and every combination with it): **Künnarantaiga drops out** (8.24 → 0), because its only zone at or above 25% is +9 (49.6% of its pool; d = 4). The other twelve rise pro rata (Russia 41.83 → 45.59).
  - **(b-sub):** Künnarantaiga **8.24 → 2.74 (−5.50)**: only Irkutsk, Buryatia (+7) and Chita (+8), 31.4% of its pool, lie within ±3; Russia rises to 44.34.
  - **Population only** (no income factor): Russia **41.83 → 31.36 (−10.47)**, Idelsk-Uralia (prov.) **23.41 → 30.90 (+7.49)**; Donska-Kubania +4.83 and Siberia −4.43 stay under the line. This holds for (a) and (b) alike, and it moves Russia's Ê to 7.84M, **below the T2 cut (Significant → Notable)**.
- **Sensitivities that move nothing by more than 5 points:** V1c (largest move Donska-Kubania +0.65), V2 (Russia +3.70), K-in (Kaliningrad is outside, so (b) is unchanged), C-15 (Idelsk-Uralia +0.68; Finland's piece 0.29), θ = 5%, official zones, centroid zones, the three knife-edge cities, no Gini (Russia +0.89).
- **Window membership flips:** Künnarantaiga at θ = 25% (alone and in all three θ-25% combinations). No other.

### 4.7 NOT FOUND for Sinheung
The First Interwar record itself (every input is a present-day stand-in) · the meaningful-share threshold θ (`UEIC` L46–53 bound it above 2.5% but give no number) · a number for "large pool" (`UEIC` L31) · whether a floor excludes pools below 0.6M · the Gini penalty's functional form (`UEIC` L1057; the form used is RS1's convention).

---

## 5 · Mirny (solar UTC +6)

**City inputs (SOURCED):** ~66°33'S 93°01'E (`UEIC` L559); 93.0167°E ÷ 15 = 6.201 → **solar UTC +6** (`UEIC` L28 rule; `UEIC` L28 itself gives *"Mirny 93°01'E → +6"*). Window **+3 … +9**. **Former Russia share 7.22%**, tier Significant; **Census I: 50,379 robots, 48,987 humans** (brief L26; the city's `Specs` row, `Specs/Mirny subnet/Mirny.md` L36, gives the same figures). **Tier lists:** `UEIC` L563–565 (Primary China; Significant Japan 65M, UK 32M, South Korea 26M, Russia 25M, Indonesia 16M, Australia 13M; Notable Thailand 8M, Vietnam, Philippines, Malaysia 5M, South Africa 3M, New Zealand 2.6M, Belarus 1.5M). `Specs/Mirny subnet/Mirny.md` L20–22 lists the same nations in the same tiers.

**Status line, plain:** the First Interwar record does not exist; these are present-day regional figures standing in for it; nothing here is a ruling or a recommendation.

### 5.1 Which successors lie inside Mirny's window
**Inside (primary): twelve successors.** Siberia (**d = 0**, its +6 zone: Novosibirsk, Krasnoyarsk, Barnaul, Novokuznetsk, Tomsk) · Tuva (**d = 0**, Kyzyl) · Künnarantaiga (d = 1, its +7 zone: Irkutsk, Ulan-Ude) · Idelsk-Uralia (prov.) (d = 2, its +4 zone: Yekaterinburg, Chelyabinsk, Perm, Ufa and others) · **at the edge, d = 3:** Russia (through its +3 zone: Moscow, Moscow Oblast, Tula, Lipetsk, Ryazan', Tambov, Voronezh; 71.2% of its pool), Donska-Kubania (prov.), and the six North Caucasus republics.
**Outside: Karelia** (+2 only; d = 4). Under the variants: **Kaliningrad (K-in) is outside** (d = 5 solar; d = 4 official); **Finland's Republic-of-Karelia piece (C-15) is outside** (+2, d = 4), but inside under official zones (+3, d = 3).

**Relation to the city's own note (SOURCED):** `UEIC` L565 already places the edge here: *"Belarus (UTC+3, distance=3) just qualifies; Romania/Ukraine outside ±3 window."* The successors at +3 sit on that same edge.

**Why Russia's place in this window is the input to watch (DERIVED):** Russia is inside only through its +3 zone, and that zone rests mostly on **Moscow at 37.61°E = 2.507 zones**, 0.007 of a zone (0.11°) above the +2/+3 line (RS1b §4). At θ = 10% Russia stays inside even if Moscow is moved to +2 (its +3 share is then 21.5%, still above 10%). **At θ = 25% it does not**: with Moscow at +2, or with territory-centroid zones, Russia's +3 share falls to 21.5% or 21.7%, its only meaningful zone becomes +2, d = 4, and it leaves the window. θ = 25% alone, with Moscow at +3, keeps it inside (+2 28.8%, +3 71.2%).

### 5.2 to 5.5 · Raw script output (`cities.py 5`, pasted unedited)

`CITY 5 Mirny: lon 93.0167E / 15 = 6.2011 -> solar UTC +6; window +3 ... +9`

#### WINDOW (primary: V1 · K-out · INIT · solar S7 · θ 10%; θ 5% / 25%, official and centroid shown for membership only)

| Successor | q(z), solar, primary | Z(10%) | d | Inside ±3? | θ 5%: d / in | θ 25%: d / in | official: Z(10%), d / in | centroid: Z(10%), d / in |
|---|---|---|--:|:-:|:-:|:-:|---|---|
| Russia | +2: 28.8% · +3: 71.2% | {+2,+3} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 3 / IN | {+2,+3}, 3 / IN |
| Idelsk-Uralia (prov.) | +3: 57.1% · +4: 42.9% | {+3,+4} | 2 | **IN** | 2 / IN | 2 / IN | {+3,+4,+5}, 1 / IN | {+3,+4}, 2 / IN |
| Donska-Kubania (prov.) | +3: 100.0% | {+3} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 3 / IN | {+3}, 3 / IN |
| Künnarantaiga | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7,+9,+10} | 1 | **IN** | 1 / IN | 3 / IN | {+8,+9,+10,+11}, 2 / IN | {+7,+9,+10}, 1 / IN |
| Siberia | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5,+6} | 0 | **IN** | 0 / IN | 0 / IN | {+5,+7}, 1 / IN | {+5,+6}, 0 / IN |
| Tuva | +6: 100.0% | {+6} | 0 | **IN** | 0 / IN | 0 / IN | {+7}, 1 / IN | {+6}, 0 / IN |
| Karelia | +2: 100.0% | {+2} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 3 / IN | {+2}, 4 / OUT |
| Chechnya | +3: 100.0% | {+3} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 3 / IN | {+3}, 3 / IN |
| Dagestan | +3: 100.0% | {+3} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 3 / IN | {+3}, 3 / IN |
| Ingushetia | +3: 100.0% | {+3} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 3 / IN | {+3}, 3 / IN |
| Kabardino-Balkaria | +3: 100.0% | {+3} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 3 / IN | {+3}, 3 / IN |
| Karachay-Cherkessia | +3: 100.0% | {+3} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 3 / IN | {+3}, 3 / IN |
| North Ossetia-Alania | +3: 100.0% | {+3} | 3 | **IN** | 3 / IN | 3 / IN | {+3}, 3 / IN | {+3}, 3 / IN |
| Kaliningrad (K-in) *(K-in only)* | +1: 100.0% | {+1} | 5 | **OUT** | same | same | {+2}, 4 / OUT | {+1}, 5 / OUT |
| Finland, Rep. of Karelia (C-15) *(C-15 only)* | +2: 100.0% | {+2} | 4 | **OUT** | same | same | {+3}, 3 / IN | {+2}, 4 / OUT |
| Idelsk-Uralia (prov.) under C-15 *(with Murmansk)* | +2: 2.8% · +3: 55.5% · +4: 41.7% | {+3,+4} | 2 | **IN** | — | — | — | — |

INSIDE (primary): Russia, Idelsk-Uralia (prov.), Donska-Kubania (prov.), Künnarantaiga, Siberia, Tuva, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania
OUTSIDE (primary): Karelia

#### SPLIT (primary)

Σ W (all) = 114.0887 tn RUB · Σ W (inside window) = 112.9825 tn RUB · Σ W_c (b-sub, units with |z_s − 6| ≤ 3) = 97.4578 tn RUB

| Successor | W_k (tn RUB) | **(a) % = W_k ÷ ΣW** | Inside? | **(b) % = W_k·I ÷ Σ W·I** | W_k,c (tn RUB) | (b-sub) % |
|---|--:|--:|:-:|--:|--:|--:|
| Russia | 47.7264 | 41.83 | IN | 42.24 | 33.9939 | 34.88 |
| Idelsk-Uralia (prov.) | 26.7038 | 23.41 | IN | 23.64 | 26.7038 | 27.40 |
| Donska-Kubania (prov.) | 8.1252 | 7.12 | IN | 7.19 | 8.1252 | 8.34 |
| Künnarantaiga | 9.4017 | 8.24 | IN | 8.32 | 7.6095 | 7.81 |
| Siberia | 19.2836 | 16.90 | IN | 17.07 | 19.2836 | 19.79 |
| Tuva | 0.0964 | 0.08 | IN | 0.09 | 0.0964 | 0.10 |
| Karelia | 1.1062 | 0.97 | OUT | 0.00 | 0.0000 | 0.00 |
| Chechnya | 0.3272 | 0.29 | IN | 0.29 | 0.3272 | 0.34 |
| Dagestan | 0.6996 | 0.61 | IN | 0.62 | 0.6996 | 0.72 |
| Ingushetia | 0.0718 | 0.06 | IN | 0.06 | 0.0718 | 0.07 |
| Kabardino-Balkaria | 0.2225 | 0.20 | IN | 0.20 | 0.2225 | 0.23 |
| Karachay-Cherkessia | 0.1113 | 0.10 | IN | 0.10 | 0.1113 | 0.11 |
| North Ossetia-Alania | 0.2131 | 0.19 | IN | 0.19 | 0.2131 | 0.22 |
| **Sum** | 114.0887 | 100.00 | | 100.00 | 97.4578 | 100.00 |

#### COUNTS (largest remainder / Hamilton; ties to larger W_k)

Robots R = 50,379 · Humans H = 48,987. Units left after flooring, given one each to the largest remainders: (a) robots 7, humans 9; (b) robots 5, humans 5.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans |
|---|--:|--:|--:|--:|
| Russia | 21,075 | 20,493 | 21,281 | 20,693 |
| Idelsk-Uralia (prov.) | 11,792 | 11,466 | 11,907 | 11,578 |
| Donska-Kubania (prov.) | 3,588 | 3,489 | 3,623 | 3,523 |
| Künnarantaiga | 4,152 | 4,037 | 4,192 | 4,077 |
| Siberia | 8,515 | 8,280 | 8,599 | 8,361 |
| Tuva | 43 | 41 | 43 | 42 |
| Karelia | 488 | 475 | 0 | 0 |
| Chechnya | 144 | 140 | 146 | 142 |
| Dagestan | 309 | 300 | 312 | 303 |
| Ingushetia | 32 | 31 | 32 | 31 |
| Kabardino-Balkaria | 98 | 96 | 99 | 97 |
| Karachay-Cherkessia | 49 | 48 | 50 | 48 |
| North Ossetia-Alania | 94 | 91 | 95 | 92 |
| **Sum** | 50,379 | 48,987 | 50,379 | 48,987 |

#### TIERS (Ê_k = 25M × (a) share; city T2 floor 13M, T3 top 8M; break at the larger sub-gap ⇔ Ê ≥ √(13×8) = 10.198M is T2-sized)

| Successor | Ê_k (M) | d | Size class | Effective tier (informational) |
|---|--:|--:|---|---|
| Russia | 10.458 | 3 | T2-sized | Significant |
| Idelsk-Uralia (prov.) | 5.852 | 2 | T3-sized | Notable |
| Donska-Kubania (prov.) | 1.780 | 3 | T3-sized | Notable |
| Künnarantaiga | 2.060 | 1 | T3-sized | Notable |
| Siberia | 4.226 | 0 | T3-sized | Notable |
| Tuva | 0.021 | 0 | T3-sized | Notable ⚠ below 0.6M |
| Karelia | 0.242 | 4 | T3-sized | absent (small pool, d > 3) |
| Chechnya | 0.072 | 3 | T3-sized | Notable ⚠ below 0.6M |
| Dagestan | 0.153 | 3 | T3-sized | Notable ⚠ below 0.6M |
| Ingushetia | 0.016 | 3 | T3-sized | Notable ⚠ below 0.6M |
| Kabardino-Balkaria | 0.049 | 3 | T3-sized | Notable ⚠ below 0.6M |
| Karachay-Cherkessia | 0.024 | 3 | T3-sized | Notable ⚠ below 0.6M |
| North Ossetia-Alania | 0.047 | 3 | T3-sized | Notable ⚠ below 0.6M |

Mechanical re-finding over the merged ranking, three largest ratio gaps: Belarus 1.50M → Dagestan 0.153M = 9.78× · China 210.00M → Japan 65.000M = 3.23× · Dagestan 0.15M → Chechnya 0.072M = 2.14×

#### SENSITIVITY, split (b) (% of the former Russia share; bold = moves more than 5 points from primary; OUT = outside the window)

| Successor | primary | V1c | V2 | K-in | C-15 | θ 5% | θ 25% | official zones | centroid (S7 alt.) | Moscow at +2 | Amur at +8 | Sakhalin at +9 | no Gini (P×y2024) | P only | b-sub (unit level) | combo: centroid + θ 25% | combo: Moscow at +2 + θ 25% | combo: official + θ 25% | combo: official + θ 5% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Russia | 42.24 | 41.94 | 46.08 | 42.24 | 41.95 | 42.24 | 42.24 | 41.83 | 42.24 | 42.24 | 42.24 | 42.24 | 43.11 | **31.62** | **34.88** | **OUT** | **OUT** | 41.83 | 41.83 |
| Idelsk-Uralia (prov.) | 23.64 | 23.47 | 21.62 | 23.64 | 24.16 | 23.64 | 23.64 | 23.41 | 23.64 | 23.64 | 23.64 | 23.64 | 22.91 | **31.16** | 27.40 | **40.92** | **40.92** | 23.41 | 23.41 |
| Donska-Kubania (prov.) | 7.19 | 7.85 | 7.21 | 7.19 | 7.14 | 7.19 | 7.19 | 7.12 | 7.19 | 7.19 | 7.19 | 7.19 | 7.16 | 12.05 | 8.34 | **12.45** | **12.45** | 7.12 | 7.12 |
| Künnarantaiga | 8.32 | 8.26 | 7.47 | 8.32 | 8.26 | 8.32 | 8.32 | 8.24 | 8.32 | 8.32 | 8.32 | 8.32 | 8.18 | 7.26 | 7.81 | **14.41** | **14.41** | 8.24 | 8.24 |
| Siberia | 17.07 | 16.95 | 16.26 | 17.07 | 16.95 | 17.07 | 17.07 | 16.90 | 17.07 | 17.07 | 17.07 | 17.07 | 17.15 | 12.57 | 19.79 | **29.55** | **29.55** | 16.90 | 16.90 |
| Tuva | 0.09 | 0.08 | 0.07 | 0.09 | 0.08 | 0.09 | 0.09 | 0.08 | 0.09 | 0.09 | 0.09 | 0.09 | 0.08 | 0.24 | 0.10 | 0.15 | 0.15 | 0.08 | 0.08 |
| Karelia | OUT | OUT | OUT | OUT | — | OUT | OUT | 0.97 | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | 0.97 | 0.97 |
| Chechnya | 0.29 | 0.29 | 0.22 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 1.06 | 0.34 | 0.50 | 0.50 | 0.29 | 0.29 |
| Dagestan | 0.62 | 0.61 | 0.62 | 0.62 | 0.61 | 0.62 | 0.62 | 0.61 | 0.62 | 0.62 | 0.62 | 0.62 | 0.61 | 2.23 | 0.72 | 1.07 | 1.07 | 0.61 | 0.61 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.36 | 0.07 | 0.11 | 0.11 | 0.06 | 0.06 |
| Kabardino-Balkaria | 0.20 | 0.20 | 0.17 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 0.19 | 0.63 | 0.23 | 0.34 | 0.34 | 0.20 | 0.20 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.09 | 0.33 | 0.11 | 0.17 | 0.17 | 0.10 | 0.10 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.19 | 0.18 | 0.48 | 0.22 | 0.33 | 0.33 | 0.19 | 0.19 |
| Kaliningrad (K-in) | — | — | — | OUT | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | OUT | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

FLAGS (b), |Δ| > 5 points: P only: Russia 42.24 → 31.62 (-10.62); b-sub (unit level): Russia 42.24 → 34.88 (-7.36); combo: centroid + θ 25%: Russia 42.24 → 0.00 (-42.24); combo: Moscow at +2 + θ 25%: Russia 42.24 → 0.00 (-42.24); P only: Idelsk-Uralia (prov.) 23.64 → 31.16 (+7.52); combo: centroid + θ 25%: Idelsk-Uralia (prov.) 23.64 → 40.92 (+17.29); combo: Moscow at +2 + θ 25%: Idelsk-Uralia (prov.) 23.64 → 40.92 (+17.29); combo: centroid + θ 25%: Donska-Kubania (prov.) 7.19 → 12.45 (+5.26); combo: Moscow at +2 + θ 25%: Donska-Kubania (prov.) 7.19 → 12.45 (+5.26); combo: centroid + θ 25%: Künnarantaiga 8.32 → 14.41 (+6.09); combo: Moscow at +2 + θ 25%: Künnarantaiga 8.32 → 14.41 (+6.09); combo: centroid + θ 25%: Siberia 17.07 → 29.55 (+12.48); combo: Moscow at +2 + θ 25%: Siberia 17.07 → 29.55 (+12.48)
WINDOW FLIPS vs primary: official zones: Karelia OUT→IN; combo: centroid + θ 25%: Russia IN→OUT; combo: Moscow at +2 + θ 25%: Russia IN→OUT; combo: official + θ 25%: Karelia OUT→IN; combo: official + θ 5%: Karelia OUT→IN

#### SENSITIVITY, split (a) (city-independent; recomputed here)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.60 | 41.83 | 42.72 | **31.36** |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.27 | 24.09 | 22.71 | **30.90** |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.08 | 7.12 | 7.10 | 11.95 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.19 | 8.24 | 8.11 | 7.20 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.81 | 16.90 | 17.00 | 12.47 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.23 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.96 | — | 0.89 | 0.84 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.28 | 1.05 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.19 | 0.20 | 0.19 | 0.63 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.09 | 0.33 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.18 | 0.48 |
| Kaliningrad (K-in) | — | — | — | 0.57 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — |

FLAGS (a), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49)

#### TIER SENSITIVITY (Ê_k in M under each (a) variant; T2-sized cut 10.198M)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 10.46 | 10.39 | 11.38 | 10.40 | 10.46 | 10.68 | **7.84** |
| Idelsk-Uralia (prov.) | 5.85 | 5.81 | 5.34 | 5.82 | 6.02 | 5.68 | 7.72 |
| Donska-Kubania (prov.) | 1.78 | 1.94 | 1.78 | 1.77 | 1.78 | 1.77 | 2.99 |
| Künnarantaiga | 2.06 | 2.05 | 1.85 | 2.05 | 2.06 | 2.03 | 1.80 |
| Siberia | 4.23 | 4.20 | 4.02 | 4.20 | 4.23 | 4.25 | 3.12 |
| Tuva | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.06 |
| Karelia | 0.24 | 0.24 | 0.30 | 0.24 | — | 0.22 | 0.21 |
| Chechnya | 0.07 | 0.07 | 0.05 | 0.07 | 0.07 | 0.07 | 0.26 |
| Dagestan | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.55 |
| Ingushetia | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 | 0.01 | 0.09 |
| Kabardino-Balkaria | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.05 | 0.16 |
| Karachay-Cherkessia | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.08 |
| North Ossetia-Alania | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.04 | 0.12 |
| Kaliningrad (K-in) | — | — | — | 0.14 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.07 | — | — |

### 5.6 Reading the output for Mirny (DERIVED; arithmetic only)
- **Split (a)** (pool alone; Karelia's slice included although it is outside): Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06%.
- **Split (b)** (pool within the window; Karelia's 0.97 points spread pro rata over the other twelve): Russia **42.24%** · Idelsk-Uralia (prov.) **23.64%** · Siberia **17.07%** · Künnarantaiga **8.32%** · Donska-Kubania (prov.) **7.19%** · Dagestan 0.62% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.09% · Ingushetia 0.06% · Karelia 0. In city-share terms (× 7.22%, each rounded): Russia 3.05% · Idelsk-Uralia (prov.) 1.71% · Siberia 1.23% · Künnarantaiga 0.60% · Donska-Kubania (prov.) 0.52% · the seven smaller successors together about 0.11%.
- **Counts:** the tables above; every column sums exactly to 50,379 robots and 48,987 humans (largest remainder, §0.2). Under (b) Karelia receives 0.
- **Effective tier (informational):** **Russia** Ê = 10.458M, **2.5% above** the 10.198M cut implied by the city's T2|T3 gap (Australia 13M | Thailand 8M) → **Significant**, a knife-edge (inside the window at d = 3 in any case). **Idelsk-Uralia (prov.)** 5.85M, **Siberia** 4.23M, **Künnarantaiga** 2.06M, **Donska-Kubania (prov.)** 1.78M → **Notable**. **Dagestan, Chechnya, Kabardino-Balkaria, North Ossetia-Alania, Karachay-Cherkessia, Tuva, Ingushetia** (0.016M to 0.153M) → Notable by the window rule, all **below the 0.6M smallest pool the census carries** (`UEIC` L1089). **Karelia** (0.242M, d = 4) → **absent** (a small pool outside the window).
- **Sensitivities that move a share by more than 5 points (flagged):**
  - **Moscow at +2 with θ = 25%**, and **centroid zones with θ = 25%** (identical results): **Russia leaves the window (42.24 → 0)**; Idelsk-Uralia (prov.) **40.92 (+17.29)**, Siberia **29.55 (+12.48)**, Künnarantaiga **14.41 (+6.09)**, Donska-Kubania (prov.) **12.45 (+5.26)**. This is the largest single sensitivity in this city.
  - **(b-sub):** Russia **42.24 → 34.88 (−7.36)**: only its +3 units (71.2% of its pool) lie within ±3; St. Petersburg, Leningrad Oblast and the other +2 units drop out. Idelsk-Uralia rises to 27.40, Siberia to 19.79.
  - **Population only:** Russia **−10.62** (to 31.62), Idelsk-Uralia (prov.) **+7.52** (to 31.16), in (b); (a) moves the same way (−10.47, +7.49). Russia's Ê falls to 7.84M, **below the T2 cut (Significant → Notable)**.
- **Sensitivities that move nothing by more than 5 points:** V1c, V2 (Russia +3.84 in (b)), K-in, C-15, θ = 5%, θ = 25% alone, official zones, centroid zones alone, Moscow at +2 alone, Amur at +8, Sakhalin at +9, no Gini.
- **Window membership flips:** Karelia OUT → IN under official zones (θ 5%, 10% or 25%), worth 0.97 points; Russia IN → OUT under the two θ-25% combinations above.

### 5.7 NOT FOUND for Mirny
The First Interwar record itself · the threshold θ (decisive here only in combination with Moscow's zone or the centroid rule) · a number for "large pool" (`UEIC` L31) · whether a floor excludes pools below 0.6M · the Gini penalty's functional form (`UEIC` L1057).

---

## 6 · Casey (solar UTC +7)

**City inputs (SOURCED):** ~66°17'S 110°32'E (`UEIC` L569); 110.5333°E ÷ 15 = 7.369 → **solar UTC +7** (`UEIC` L28 rule; `UEIC` L28 itself gives *"Casey 110°32'E → +7"*). Window **+4 … +10**. **Former Russia share 6.13%**, tier Significant; **Census I: 47,415 robots, 45,713 humans** (brief L24; the city's `Specs` row, `Specs/Mirny subnet/Casey.md` L36, gives the same figures). **Tier lists:** `UEIC` L573–575 (Primary China 210M, USA 155M; Significant Japan 65M, France 35M, South Korea 26M, Russia 25M, Indonesia 16M, Australia 13M; Notable Thailand 8M, Vietnam, Philippines, Malaysia 5M, New Zealand 2.6M). `Specs/Mirny subnet/Casey.md` L19–21 lists the same nations in the same tiers.

**Status line, plain:** the First Interwar record does not exist; these are present-day regional figures standing in for it; nothing here is a ruling or a recommendation.

### 6.1 Which successors lie inside Casey's window
**Inside (primary): four successors.** Künnarantaiga (**d = 0**, its +7 zone: Irkutsk, Ulan-Ude; 24.9% of its pool) · Siberia (d = 1, its +6 zone) · Tuva (d = 1) · **Idelsk-Uralia (prov.) at the edge, d = 3**, through its +4 zone (Yekaterinburg, Chelyabinsk, Perm, Ufa, Orenburg, Izhevsk, Kurgan, Naryan-Mar; 42.9% of its pool).
**Outside: nine successors.** Russia (+2 and +3; d = 4), Donska-Kubania (prov.) (+3; d = 4), Karelia (+2; d = 5), Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania (+3; d = 4). Under the variants: Kaliningrad (K-in) and Finland's Republic-of-Karelia piece (C-15) are outside under every zone rule. **Together the outside successors hold 51.37% of the pool** (split (a) below).

**Robustness of the four memberships (DERIVED):** Idelsk-Uralia's +4 share is 42.9%, so it stays inside for any θ up to that; none of the cities that set its +4 zone lies within RS1b's 0.35° knife-edge distance of a zone line (nearest: Izhevsk 53.23°E = 3.549 and Naryan-Mar 53.06°E = 3.537, about 0.7° from the +3/+4 line). Künnarantaiga stays inside at θ = 25% through +9 (d = 2). Under official zones every one of the four is still inside, and Russia (+3 official) is still outside.

### 6.2 to 6.5 · Raw script output (`cities.py 6`, pasted unedited)

`CITY 6 Casey: lon 110.5333E / 15 = 7.3689 -> solar UTC +7; window +4 ... +10`

#### WINDOW (primary: V1 · K-out · INIT · solar S7 · θ 10%; θ 5% / 25%, official and centroid shown for membership only)

| Successor | q(z), solar, primary | Z(10%) | d | Inside ±3? | θ 5%: d / in | θ 25%: d / in | official: Z(10%), d / in | centroid: Z(10%), d / in |
|---|---|---|--:|:-:|:-:|:-:|---|---|
| Russia | +2: 28.8% · +3: 71.2% | {+2,+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+2,+3}, 4 / OUT |
| Idelsk-Uralia (prov.) | +3: 57.1% · +4: 42.9% | {+3,+4} | 3 | **IN** | 3 / IN | 3 / IN | {+3,+4,+5}, 2 / IN | {+3,+4}, 3 / IN |
| Donska-Kubania (prov.) | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Künnarantaiga | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7,+9,+10} | 0 | **IN** | 0 / IN | 2 / IN | {+8,+9,+10,+11}, 1 / IN | {+7,+9,+10}, 0 / IN |
| Siberia | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5,+6} | 1 | **IN** | 1 / IN | 1 / IN | {+5,+7}, 0 / IN | {+5,+6}, 1 / IN |
| Tuva | +6: 100.0% | {+6} | 1 | **IN** | 1 / IN | 1 / IN | {+7}, 0 / IN | {+6}, 1 / IN |
| Karelia | +2: 100.0% | {+2} | 5 | **OUT** | 5 / OUT | 5 / OUT | {+3}, 4 / OUT | {+2}, 5 / OUT |
| Chechnya | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Dagestan | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Ingushetia | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Kabardino-Balkaria | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Karachay-Cherkessia | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| North Ossetia-Alania | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Kaliningrad (K-in) *(K-in only)* | +1: 100.0% | {+1} | 6 | **OUT** | same | same | {+2}, 5 / OUT | {+1}, 6 / OUT |
| Finland, Rep. of Karelia (C-15) *(C-15 only)* | +2: 100.0% | {+2} | 5 | **OUT** | same | same | {+3}, 4 / OUT | {+2}, 5 / OUT |
| Idelsk-Uralia (prov.) under C-15 *(with Murmansk)* | +2: 2.8% · +3: 55.5% · +4: 41.7% | {+3,+4} | 3 | **IN** | — | — | — | — |

INSIDE (primary): Idelsk-Uralia (prov.), Künnarantaiga, Siberia, Tuva
OUTSIDE (primary): Russia, Donska-Kubania (prov.), Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania

#### SPLIT (primary)

Σ W (all) = 114.0887 tn RUB · Σ W (inside window) = 55.4855 tn RUB · Σ W_c (b-sub, units with |z_s − 7| ≤ 3) = 39.7987 tn RUB

| Successor | W_k (tn RUB) | **(a) % = W_k ÷ ΣW** | Inside? | **(b) % = W_k·I ÷ Σ W·I** | W_k,c (tn RUB) | (b-sub) % |
|---|--:|--:|:-:|--:|--:|--:|
| Russia | 47.7264 | 41.83 | OUT | 0.00 | 0.0000 | 0.00 |
| Idelsk-Uralia (prov.) | 26.7038 | 23.41 | IN | 48.13 | 11.4480 | 28.76 |
| Donska-Kubania (prov.) | 8.1252 | 7.12 | OUT | 0.00 | 0.0000 | 0.00 |
| Künnarantaiga | 9.4017 | 8.24 | IN | 16.94 | 8.9708 | 22.54 |
| Siberia | 19.2836 | 16.90 | IN | 34.75 | 19.2836 | 48.45 |
| Tuva | 0.0964 | 0.08 | IN | 0.17 | 0.0964 | 0.24 |
| Karelia | 1.1062 | 0.97 | OUT | 0.00 | 0.0000 | 0.00 |
| Chechnya | 0.3272 | 0.29 | OUT | 0.00 | 0.0000 | 0.00 |
| Dagestan | 0.6996 | 0.61 | OUT | 0.00 | 0.0000 | 0.00 |
| Ingushetia | 0.0718 | 0.06 | OUT | 0.00 | 0.0000 | 0.00 |
| Kabardino-Balkaria | 0.2225 | 0.20 | OUT | 0.00 | 0.0000 | 0.00 |
| Karachay-Cherkessia | 0.1113 | 0.10 | OUT | 0.00 | 0.0000 | 0.00 |
| North Ossetia-Alania | 0.2131 | 0.19 | OUT | 0.00 | 0.0000 | 0.00 |
| **Sum** | 114.0887 | 100.00 | | 100.00 | 39.7987 | 100.00 |

#### COUNTS (largest remainder / Hamilton; ties to larger W_k)

Robots R = 47,415 · Humans H = 45,713. Units left after flooring, given one each to the largest remainders: (a) robots 7, humans 6; (b) robots 2, humans 2.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans |
|---|--:|--:|--:|--:|
| Russia | 19,835 | 19,123 | 0 | 0 |
| Idelsk-Uralia (prov.) | 11,098 | 10,700 | 22,820 | 22,001 |
| Donska-Kubania (prov.) | 3,377 | 3,256 | 0 | 0 |
| Künnarantaiga | 3,907 | 3,767 | 8,034 | 7,746 |
| Siberia | 8,014 | 7,726 | 16,479 | 15,887 |
| Tuva | 40 | 39 | 82 | 79 |
| Karelia | 460 | 443 | 0 | 0 |
| Chechnya | 136 | 131 | 0 | 0 |
| Dagestan | 291 | 280 | 0 | 0 |
| Ingushetia | 30 | 29 | 0 | 0 |
| Kabardino-Balkaria | 92 | 89 | 0 | 0 |
| Karachay-Cherkessia | 46 | 45 | 0 | 0 |
| North Ossetia-Alania | 89 | 85 | 0 | 0 |
| **Sum** | 47,415 | 45,713 | 47,415 | 45,713 |

#### TIERS (Ê_k = 25M × (a) share; city T2 floor 13M, T3 top 8M; break at the larger sub-gap ⇔ Ê ≥ √(13×8) = 10.198M is T2-sized)

| Successor | Ê_k (M) | d | Size class | Effective tier (informational) |
|---|--:|--:|---|---|
| Russia | 10.458 | 4 | T2-sized | Significant (by the large-pool clause; outside the window) |
| Idelsk-Uralia (prov.) | 5.852 | 3 | T3-sized | Notable |
| Donska-Kubania (prov.) | 1.780 | 4 | T3-sized | absent (small pool, d > 3) |
| Künnarantaiga | 2.060 | 0 | T3-sized | Notable |
| Siberia | 4.226 | 1 | T3-sized | Notable |
| Tuva | 0.021 | 1 | T3-sized | Notable ⚠ below 0.6M |
| Karelia | 0.242 | 5 | T3-sized | absent (small pool, d > 3) |
| Chechnya | 0.072 | 4 | T3-sized | absent (small pool, d > 3) |
| Dagestan | 0.153 | 4 | T3-sized | absent (small pool, d > 3) |
| Ingushetia | 0.016 | 4 | T3-sized | absent (small pool, d > 3) |
| Kabardino-Balkaria | 0.049 | 4 | T3-sized | absent (small pool, d > 3) |
| Karachay-Cherkessia | 0.024 | 4 | T3-sized | absent (small pool, d > 3) |
| North Ossetia-Alania | 0.047 | 4 | T3-sized | absent (small pool, d > 3) |

Mechanical re-finding over the merged ranking, three largest ratio gaps: Künnarantaiga 2.06M → Tuva 0.021M = 97.57× · USA 155.00M → Japan 65.000M = 2.38× · Japan 65.00M → France 35.000M = 1.86×

#### SENSITIVITY, split (b) (% of the former Russia share; bold = moves more than 5 points from primary; OUT = outside the window)

| Successor | primary | V1c | V2 | K-in | C-15 | θ 5% | θ 25% | official zones | centroid (S7 alt.) | Moscow at +2 | Amur at +8 | Sakhalin at +9 | no Gini (P×y2024) | P only | b-sub (unit level) | combo: centroid + θ 25% | combo: Moscow at +2 + θ 25% | combo: official + θ 25% | combo: official + θ 5% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Russia | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Idelsk-Uralia (prov.) | 48.13 | 48.13 | 47.60 | 48.13 | 48.84 | 48.13 | 48.13 | 48.13 | 48.13 | 48.13 | 48.13 | 48.13 | 47.40 | **60.82** | **28.76** | 48.13 | 48.13 | 48.13 | **41.98** |
| Donska-Kubania (prov.) | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | **12.77** |
| Künnarantaiga | 16.94 | 16.94 | 16.45 | 16.94 | 16.71 | 16.94 | 16.94 | 16.94 | 16.94 | 16.94 | 16.94 | 16.94 | 16.93 | 14.18 | **22.54** | 16.94 | 16.94 | 16.94 | 14.78 |
| Siberia | 34.75 | 34.75 | 35.79 | 34.75 | 34.28 | 34.75 | 34.75 | 34.75 | 34.75 | 34.75 | 34.75 | 34.75 | 35.49 | **24.54** | **48.45** | 34.75 | 34.75 | 34.75 | 30.32 |
| Tuva | 0.17 | 0.17 | 0.16 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.46 | 0.24 | 0.17 | 0.17 | 0.17 | 0.15 |
| Karelia | OUT | OUT | OUT | OUT | — | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Chechnya | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Dagestan | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Ingushetia | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Kabardino-Balkaria | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Karachay-Cherkessia | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| North Ossetia-Alania | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Kaliningrad (K-in) | — | — | — | OUT | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | OUT | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

FLAGS (b), |Δ| > 5 points: P only: Idelsk-Uralia (prov.) 48.13 → 60.82 (+12.69); b-sub (unit level): Idelsk-Uralia (prov.) 48.13 → 28.76 (-19.36); combo: official + θ 5%: Idelsk-Uralia (prov.) 48.13 → 41.98 (-6.15); combo: official + θ 5%: Donska-Kubania (prov.) 0.00 → 12.77 (+12.77); b-sub (unit level): Künnarantaiga 16.94 → 22.54 (+5.60); P only: Siberia 34.75 → 24.54 (-10.21); b-sub (unit level): Siberia 34.75 → 48.45 (+13.70)
WINDOW FLIPS vs primary: combo: official + θ 5%: Donska-Kubania (prov.) OUT→IN

#### SENSITIVITY, split (a) (city-independent; recomputed here)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.60 | 41.83 | 42.72 | **31.36** |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.27 | 24.09 | 22.71 | **30.90** |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.08 | 7.12 | 7.10 | 11.95 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.19 | 8.24 | 8.11 | 7.20 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.81 | 16.90 | 17.00 | 12.47 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.23 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.96 | — | 0.89 | 0.84 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.28 | 1.05 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.19 | 0.20 | 0.19 | 0.63 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.09 | 0.33 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.18 | 0.48 |
| Kaliningrad (K-in) | — | — | — | 0.57 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — |

FLAGS (a), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49)

#### TIER SENSITIVITY (Ê_k in M under each (a) variant; T2-sized cut 10.198M)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 10.46 | 10.39 | 11.38 | 10.40 | 10.46 | 10.68 | **7.84** |
| Idelsk-Uralia (prov.) | 5.85 | 5.81 | 5.34 | 5.82 | 6.02 | 5.68 | 7.72 |
| Donska-Kubania (prov.) | 1.78 | 1.94 | 1.78 | 1.77 | 1.78 | 1.77 | 2.99 |
| Künnarantaiga | 2.06 | 2.05 | 1.85 | 2.05 | 2.06 | 2.03 | 1.80 |
| Siberia | 4.23 | 4.20 | 4.02 | 4.20 | 4.23 | 4.25 | 3.12 |
| Tuva | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.06 |
| Karelia | 0.24 | 0.24 | 0.30 | 0.24 | — | 0.22 | 0.21 |
| Chechnya | 0.07 | 0.07 | 0.05 | 0.07 | 0.07 | 0.07 | 0.26 |
| Dagestan | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.55 |
| Ingushetia | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 | 0.01 | 0.09 |
| Kabardino-Balkaria | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.05 | 0.16 |
| Karachay-Cherkessia | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.08 |
| North Ossetia-Alania | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.04 | 0.12 |
| Kaliningrad (K-in) | — | — | — | 0.14 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.07 | — | — |

### 6.6 Reading the output for Casey (DERIVED; arithmetic only)
- **Split (a)** (pool alone, window-blind): Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06%. **51.37% of this goes to successors outside the window.**
- **Split (b)** (pool within the window): Idelsk-Uralia (prov.) **48.13%** · Siberia **34.75%** · Künnarantaiga **16.94%** · Tuva **0.17%**; the nine outside successors 0. In city-share terms (× 6.13%, each rounded): Idelsk-Uralia (prov.) 2.95% · Siberia 2.13% · Künnarantaiga 1.04% · Tuva 0.01%.
- **The two splits differ by more than 5 points for five successors** (Russia −41.83, Idelsk-Uralia +24.72, Siberia +17.85, Künnarantaiga +8.70, Donska-Kubania −7.12, from (a) to (b)). Which of the two the method calls for is the window question itself, and it is not ruled.
- **Counts:** the tables above; every column sums exactly to 47,415 robots and 45,713 humans (largest remainder, §0.2).
- **Effective tier (informational):** **Russia** Ê = 10.458M, **2.5% above** the 10.198M cut implied by the city's T2|T3 gap (Australia 13M | Thailand 8M), so it is T2-sized and, under the large-pool clause (`UEIC` L31), **Significant although outside the window**, a knife-edge on two counts (the cut, and the unnumbered meaning of "large"). ⚠ **This does not match split (b)**, which gives it nothing because it is outside: the tier rule admits a large pool from anywhere, while (b) admits only the window. **Idelsk-Uralia (prov.)** 5.85M (d = 3), **Siberia** 4.23M, **Künnarantaiga** 2.06M → **Notable**. **Tuva** 0.021M → Notable by the window rule, ⚠ below the 0.6M smallest pool the census carries (`UEIC` L1089). **Donska-Kubania (prov.), Karelia and the six North Caucasus republics** → **absent** (small pools outside the window).
- **Sensitivities that move a share by more than 5 points in (b) (flagged):**
  - **(b-sub):** Idelsk-Uralia (prov.) **48.13 → 28.76 (−19.36)**, because only its +4 units (42.9% of its pool) count; Siberia **34.75 → 48.45 (+13.70)**; Künnarantaiga **16.94 → 22.54 (+5.60)** (its +7 to +10 units count, its +11 and +12 do not).
  - **Population only:** Idelsk-Uralia (prov.) **+12.69** (to 60.82), Siberia **−10.21** (to 24.54).
  - **Official zones with θ = 5%:** **Donska-Kubania (prov.) enters the window** (its Astrakhan' unit is official +4, 7.4% of its pool, d = 3) at **12.77%**; Idelsk-Uralia falls **−6.15** (to 41.98).
- **Sensitivities that move nothing by more than 5 points in (b):** V1c, V2 (Siberia +1.04), K-in, C-15 (Idelsk-Uralia +0.71), θ = 5%, θ = 25%, official zones at θ = 10% or 25%, centroid zones, the three knife-edge cities, no Gini.
- **Split (a) sensitivities** are city-independent (population only is the one over 5 points: Russia −10.47, Idelsk-Uralia +7.49); under population only, Russia's Ê falls to 7.84M, T3-sized, and it would then be **absent** here (a small pool, d = 4).
- **Window membership flips:** Donska-Kubania (prov.) OUT → IN under official zones with θ = 5%. No other.

### 6.7 NOT FOUND for Casey
The First Interwar record itself · whether the composition method divides a former share by (a) or by (b) where the two diverge this far (no file says) · a number for "large pool" (`UEIC` L31), which decides whether Russia is Significant or absent here · the threshold θ · whether a floor excludes pools below 0.6M · the Gini penalty's functional form (`UEIC` L1057).

---

## 7 · Relung Panen (solar UTC +7)

**City inputs (SOURCED):** ~66°17'S 100°47'E (`UEIC` L579); 100.7833°E ÷ 15 = 6.719 → **solar UTC +7**; `UEIC` L594: *"Solar UTC +7 (100.78 ÷ 15 = 6.72) … Window: UTC+4 … +10."* **Former Russia share 12.60%** (today's figure), tier Significant; **Census I: 62,318 robots, 60,138 humans** (brief L27; `UEIC` L617 and the city's `Specs` row, `Specs/Mirny subnet/Relung_Panen.md` L58, give the same figures). **Tier lists:** `UEIC` L596–600 (Primary China 210M, d = 1; Significant Russia 25M d = 0, Indonesia 16M d = 0, Japan 65M d = 2, South Korea 26M d = 2, Australia 13M d = 1; Notable Thailand 8M, Vietnam 5M, Malaysia 5M, Philippines 5M, New Zealand 2.6M via the Hobart gateway). `Specs/Mirny subnet/Relung_Panen.md` L35–37 lists the same nations in the same tiers.

**How this city's composition is computed (SOURCED):** *"Computed PROXIMITY-FIRST at the developer's direction … so the ±3 window above is applied to EVERY tier here, not only to Notable"* (`UEIC` L581–583); its Significant tier is *"ORDERED BY PROXIMITY, NOT POOL"* (`UEIC` L607). `UEIC` L592 (update 2026-10-29) records that the new airports and the Australian seasonal intake leave the question of the city's single door *"not ruled"* and that *"The proximity-first computation above is not re-run."* This file applies the computation as it stands.

**Status line, plain:** the First Interwar record does not exist; these are present-day regional figures standing in for it; nothing here is a ruling or a recommendation.

### 7.1 Which successors lie inside Relung Panen's window
**Inside (primary): four successors.** Künnarantaiga (**d = 0**, its +7 zone: Irkutsk 104.25°E → 6.950, Ulan-Ude 107.62°E → 7.175; 24.9% of its pool) · Siberia (d = 1, its +6 zone) · Tuva (d = 1, Kyzyl) · **Idelsk-Uralia (prov.) at the edge, d = 3**, through its +4 zone (Yekaterinburg, Chelyabinsk, Perm, Ufa, Orenburg, Izhevsk, Kurgan, Naryan-Mar; 42.9% of its pool).
**Outside: nine successors.** Russia (+2 and +3; d = 4), Donska-Kubania (prov.) (+3; d = 4), Karelia (+2; d = 5), and the six North Caucasus republics (+3; d = 4). Kaliningrad (K-in) and Finland's Republic-of-Karelia piece (C-15) are outside under every zone rule. **Together the outside successors hold 51.37% of the pool.**

**Relation to the city's own note (SOURCED, then DERIVED):** `UEIC` L599: *"Russia enters by SIBERIA, not by Moscow — Novosibirsk and Krasnoyarsk sit on this exact meridian."* On the solar rule Novosibirsk (82.96°E → 5.531) and Krasnoyarsk (92.86°E → 6.191) are **+6**, so Siberia sits at **d = 1**; their official zone is +7 (RS1b official column), which is where "this exact meridian" comes from (the solar/official mix RS1 §4.2 records). On the solar rule the successor on this city's meridian is **Künnarantaiga**, through Irkutsk Oblast and Buryatia. Siberia is inside either way. **The successor the note does not cover is Russia itself (the core state): its people are at +2 and +3, d = 4, outside.**

**Robustness (DERIVED):** Idelsk-Uralia's +4 share (42.9%) keeps it inside for any θ up to that, and none of its +4 cities lies within RS1b's 0.35° knife-edge distance of a zone line (nearest: Izhevsk 3.549, Naryan-Mar 3.537, about 0.7°). Künnarantaiga stays inside at θ = 25% through +9 (d = 2). Under official zones the four stay inside and Russia (+3) stays outside.

### 7.2 to 7.5 · Raw script output (`cities.py 7`, pasted unedited)

`CITY 7 Relung Panen: lon 100.7833E / 15 = 6.7189 -> solar UTC +7; window +4 ... +10`

#### WINDOW (primary: V1 · K-out · INIT · solar S7 · θ 10%; θ 5% / 25%, official and centroid shown for membership only)

| Successor | q(z), solar, primary | Z(10%) | d | Inside ±3? | θ 5%: d / in | θ 25%: d / in | official: Z(10%), d / in | centroid: Z(10%), d / in |
|---|---|---|--:|:-:|:-:|:-:|---|---|
| Russia | +2: 28.8% · +3: 71.2% | {+2,+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+2,+3}, 4 / OUT |
| Idelsk-Uralia (prov.) | +3: 57.1% · +4: 42.9% | {+3,+4} | 3 | **IN** | 3 / IN | 3 / IN | {+3,+4,+5}, 2 / IN | {+3,+4}, 3 / IN |
| Donska-Kubania (prov.) | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Künnarantaiga | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7,+9,+10} | 0 | **IN** | 0 / IN | 2 / IN | {+8,+9,+10,+11}, 1 / IN | {+7,+9,+10}, 0 / IN |
| Siberia | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+5,+6} | 1 | **IN** | 1 / IN | 1 / IN | {+5,+7}, 0 / IN | {+5,+6}, 1 / IN |
| Tuva | +6: 100.0% | {+6} | 1 | **IN** | 1 / IN | 1 / IN | {+7}, 0 / IN | {+6}, 1 / IN |
| Karelia | +2: 100.0% | {+2} | 5 | **OUT** | 5 / OUT | 5 / OUT | {+3}, 4 / OUT | {+2}, 5 / OUT |
| Chechnya | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Dagestan | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Ingushetia | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Kabardino-Balkaria | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Karachay-Cherkessia | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| North Ossetia-Alania | +3: 100.0% | {+3} | 4 | **OUT** | 4 / OUT | 4 / OUT | {+3}, 4 / OUT | {+3}, 4 / OUT |
| Kaliningrad (K-in) *(K-in only)* | +1: 100.0% | {+1} | 6 | **OUT** | same | same | {+2}, 5 / OUT | {+1}, 6 / OUT |
| Finland, Rep. of Karelia (C-15) *(C-15 only)* | +2: 100.0% | {+2} | 5 | **OUT** | same | same | {+3}, 4 / OUT | {+2}, 5 / OUT |
| Idelsk-Uralia (prov.) under C-15 *(with Murmansk)* | +2: 2.8% · +3: 55.5% · +4: 41.7% | {+3,+4} | 3 | **IN** | — | — | — | — |

INSIDE (primary): Idelsk-Uralia (prov.), Künnarantaiga, Siberia, Tuva
OUTSIDE (primary): Russia, Donska-Kubania (prov.), Karelia, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania

#### SPLIT (primary)

Σ W (all) = 114.0887 tn RUB · Σ W (inside window) = 55.4855 tn RUB · Σ W_c (b-sub, units with |z_s − 7| ≤ 3) = 39.7987 tn RUB

| Successor | W_k (tn RUB) | **(a) % = W_k ÷ ΣW** | Inside? | **(b) % = W_k·I ÷ Σ W·I** | W_k,c (tn RUB) | (b-sub) % |
|---|--:|--:|:-:|--:|--:|--:|
| Russia | 47.7264 | 41.83 | OUT | 0.00 | 0.0000 | 0.00 |
| Idelsk-Uralia (prov.) | 26.7038 | 23.41 | IN | 48.13 | 11.4480 | 28.76 |
| Donska-Kubania (prov.) | 8.1252 | 7.12 | OUT | 0.00 | 0.0000 | 0.00 |
| Künnarantaiga | 9.4017 | 8.24 | IN | 16.94 | 8.9708 | 22.54 |
| Siberia | 19.2836 | 16.90 | IN | 34.75 | 19.2836 | 48.45 |
| Tuva | 0.0964 | 0.08 | IN | 0.17 | 0.0964 | 0.24 |
| Karelia | 1.1062 | 0.97 | OUT | 0.00 | 0.0000 | 0.00 |
| Chechnya | 0.3272 | 0.29 | OUT | 0.00 | 0.0000 | 0.00 |
| Dagestan | 0.6996 | 0.61 | OUT | 0.00 | 0.0000 | 0.00 |
| Ingushetia | 0.0718 | 0.06 | OUT | 0.00 | 0.0000 | 0.00 |
| Kabardino-Balkaria | 0.2225 | 0.20 | OUT | 0.00 | 0.0000 | 0.00 |
| Karachay-Cherkessia | 0.1113 | 0.10 | OUT | 0.00 | 0.0000 | 0.00 |
| North Ossetia-Alania | 0.2131 | 0.19 | OUT | 0.00 | 0.0000 | 0.00 |
| **Sum** | 114.0887 | 100.00 | | 100.00 | 39.7987 | 100.00 |

#### COUNTS (largest remainder / Hamilton; ties to larger W_k)

Robots R = 62,318 · Humans H = 60,138. Units left after flooring, given one each to the largest remainders: (a) robots 5, humans 8; (b) robots 1, humans 2.

| Successor | (a) robots | (a) humans | (b) robots | (b) humans |
|---|--:|--:|--:|--:|
| Russia | 26,069 | 25,157 | 0 | 0 |
| Idelsk-Uralia (prov.) | 14,586 | 14,076 | 29,992 | 28,943 |
| Donska-Kubania (prov.) | 4,438 | 4,283 | 0 | 0 |
| Künnarantaiga | 5,136 | 4,956 | 10,560 | 10,190 |
| Siberia | 10,533 | 10,165 | 21,658 | 20,901 |
| Tuva | 53 | 51 | 108 | 104 |
| Karelia | 604 | 583 | 0 | 0 |
| Chechnya | 179 | 172 | 0 | 0 |
| Dagestan | 382 | 369 | 0 | 0 |
| Ingushetia | 39 | 38 | 0 | 0 |
| Kabardino-Balkaria | 122 | 117 | 0 | 0 |
| Karachay-Cherkessia | 61 | 59 | 0 | 0 |
| North Ossetia-Alania | 116 | 112 | 0 | 0 |
| **Sum** | 62,318 | 60,138 | 62,318 | 60,138 |

#### TIERS (Ê_k = 25M × (a) share; city T2 floor 13M, T3 top 8M; break at the larger sub-gap ⇔ Ê ≥ √(13×8) = 10.198M is T2-sized)

| Successor | Ê_k (M) | d | Size class | Effective tier (informational) |
|---|--:|--:|---|---|
| Russia | 10.458 | 4 | T2-sized | absent (outside window; proximity-first: every tier needs d ≤ 3) |
| Idelsk-Uralia (prov.) | 5.852 | 3 | T3-sized | Notable |
| Donska-Kubania (prov.) | 1.780 | 4 | T3-sized | absent (outside window; proximity-first: every tier needs d ≤ 3) |
| Künnarantaiga | 2.060 | 0 | T3-sized | Notable |
| Siberia | 4.226 | 1 | T3-sized | Notable |
| Tuva | 0.021 | 1 | T3-sized | Notable ⚠ below 0.6M |
| Karelia | 0.242 | 5 | T3-sized | absent (outside window; proximity-first: every tier needs d ≤ 3) |
| Chechnya | 0.072 | 4 | T3-sized | absent (outside window; proximity-first: every tier needs d ≤ 3) |
| Dagestan | 0.153 | 4 | T3-sized | absent (outside window; proximity-first: every tier needs d ≤ 3) |
| Ingushetia | 0.016 | 4 | T3-sized | absent (outside window; proximity-first: every tier needs d ≤ 3) |
| Kabardino-Balkaria | 0.049 | 4 | T3-sized | absent (outside window; proximity-first: every tier needs d ≤ 3) |
| Karachay-Cherkessia | 0.024 | 4 | T3-sized | absent (outside window; proximity-first: every tier needs d ≤ 3) |
| North Ossetia-Alania | 0.047 | 4 | T3-sized | absent (outside window; proximity-first: every tier needs d ≤ 3) |

Mechanical re-finding over the merged ranking, three largest ratio gaps: Künnarantaiga 2.06M → Tuva 0.021M = 97.57× · China 210.00M → Japan 65.000M = 3.23× · Japan 65.00M → South Korea 26.000M = 2.50×

#### SENSITIVITY, split (b) (% of the former Russia share; bold = moves more than 5 points from primary; OUT = outside the window)

| Successor | primary | V1c | V2 | K-in | C-15 | θ 5% | θ 25% | official zones | centroid (S7 alt.) | Moscow at +2 | Amur at +8 | Sakhalin at +9 | no Gini (P×y2024) | P only | b-sub (unit level) | combo: centroid + θ 25% | combo: Moscow at +2 + θ 25% | combo: official + θ 25% | combo: official + θ 5% |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Russia | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Idelsk-Uralia (prov.) | 48.13 | 48.13 | 47.60 | 48.13 | 48.84 | 48.13 | 48.13 | 48.13 | 48.13 | 48.13 | 48.13 | 48.13 | 47.40 | **60.82** | **28.76** | 48.13 | 48.13 | 48.13 | **41.98** |
| Donska-Kubania (prov.) | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | **12.77** |
| Künnarantaiga | 16.94 | 16.94 | 16.45 | 16.94 | 16.71 | 16.94 | 16.94 | 16.94 | 16.94 | 16.94 | 16.94 | 16.94 | 16.93 | 14.18 | **22.54** | 16.94 | 16.94 | 16.94 | 14.78 |
| Siberia | 34.75 | 34.75 | 35.79 | 34.75 | 34.28 | 34.75 | 34.75 | 34.75 | 34.75 | 34.75 | 34.75 | 34.75 | 35.49 | **24.54** | **48.45** | 34.75 | 34.75 | 34.75 | 30.32 |
| Tuva | 0.17 | 0.17 | 0.16 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.17 | 0.46 | 0.24 | 0.17 | 0.17 | 0.17 | 0.15 |
| Karelia | OUT | OUT | OUT | OUT | — | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Chechnya | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Dagestan | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Ingushetia | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Kabardino-Balkaria | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Karachay-Cherkessia | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| North Ossetia-Alania | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT | OUT |
| Kaliningrad (K-in) | — | — | — | OUT | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | OUT | — | — | — | — | — | — | — | — | — | — | — | — | — | — |

FLAGS (b), |Δ| > 5 points: P only: Idelsk-Uralia (prov.) 48.13 → 60.82 (+12.69); b-sub (unit level): Idelsk-Uralia (prov.) 48.13 → 28.76 (-19.36); combo: official + θ 5%: Idelsk-Uralia (prov.) 48.13 → 41.98 (-6.15); combo: official + θ 5%: Donska-Kubania (prov.) 0.00 → 12.77 (+12.77); b-sub (unit level): Künnarantaiga 16.94 → 22.54 (+5.60); P only: Siberia 34.75 → 24.54 (-10.21); b-sub (unit level): Siberia 34.75 → 48.45 (+13.70)
WINDOW FLIPS vs primary: combo: official + θ 5%: Donska-Kubania (prov.) OUT→IN

#### SENSITIVITY, split (a) (city-independent; recomputed here)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 41.83 | 41.54 | 45.53 | 41.60 | 41.83 | 42.72 | **31.36** |
| Idelsk-Uralia (prov.) | 23.41 | 23.24 | 21.36 | 23.27 | 24.09 | 22.71 | **30.90** |
| Donska-Kubania (prov.) | 7.12 | 7.77 | 7.12 | 7.08 | 7.12 | 7.10 | 11.95 |
| Künnarantaiga | 8.24 | 8.18 | 7.38 | 8.19 | 8.24 | 8.11 | 7.20 |
| Siberia | 16.90 | 16.78 | 16.06 | 16.81 | 16.90 | 17.00 | 12.47 |
| Tuva | 0.08 | 0.08 | 0.07 | 0.08 | 0.08 | 0.08 | 0.23 |
| Karelia | 0.97 | 0.96 | 1.18 | 0.96 | — | 0.89 | 0.84 |
| Chechnya | 0.29 | 0.28 | 0.21 | 0.29 | 0.29 | 0.28 | 1.05 |
| Dagestan | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 | 0.60 | 2.21 |
| Ingushetia | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.35 |
| Kabardino-Balkaria | 0.20 | 0.19 | 0.16 | 0.19 | 0.20 | 0.19 | 0.63 |
| Karachay-Cherkessia | 0.10 | 0.10 | 0.08 | 0.10 | 0.10 | 0.09 | 0.33 |
| North Ossetia-Alania | 0.19 | 0.19 | 0.15 | 0.19 | 0.19 | 0.18 | 0.48 |
| Kaliningrad (K-in) | — | — | — | 0.57 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.29 | — | — |

FLAGS (a), |Δ| > 5 points: P only: Russia 41.83 → 31.36 (-10.47); P only: Idelsk-Uralia (prov.) 23.41 → 30.90 (+7.49)

#### TIER SENSITIVITY (Ê_k in M under each (a) variant; T2-sized cut 10.198M)

| Successor | primary | V1c | V2 | K-in | C-15 | no Gini (P×y2024) | P only |
|---|--:|--:|--:|--:|--:|--:|--:|
| Russia | 10.46 | 10.39 | 11.38 | 10.40 | 10.46 | 10.68 | **7.84** |
| Idelsk-Uralia (prov.) | 5.85 | 5.81 | 5.34 | 5.82 | 6.02 | 5.68 | 7.72 |
| Donska-Kubania (prov.) | 1.78 | 1.94 | 1.78 | 1.77 | 1.78 | 1.77 | 2.99 |
| Künnarantaiga | 2.06 | 2.05 | 1.85 | 2.05 | 2.06 | 2.03 | 1.80 |
| Siberia | 4.23 | 4.20 | 4.02 | 4.20 | 4.23 | 4.25 | 3.12 |
| Tuva | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.06 |
| Karelia | 0.24 | 0.24 | 0.30 | 0.24 | — | 0.22 | 0.21 |
| Chechnya | 0.07 | 0.07 | 0.05 | 0.07 | 0.07 | 0.07 | 0.26 |
| Dagestan | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.15 | 0.55 |
| Ingushetia | 0.02 | 0.02 | 0.01 | 0.02 | 0.02 | 0.01 | 0.09 |
| Kabardino-Balkaria | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.05 | 0.16 |
| Karachay-Cherkessia | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 | 0.08 |
| North Ossetia-Alania | 0.05 | 0.05 | 0.04 | 0.05 | 0.05 | 0.04 | 0.12 |
| Kaliningrad (K-in) | — | — | — | 0.14 | — | — | — |
| Finland, Rep. of Karelia (C-15) | — | — | — | — | 0.07 | — | — |

### 7.6 Reading the output for Relung Panen (DERIVED; arithmetic only)
- **Split (a)** (pool alone, window-blind): Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06%. **51.37% of this goes to successors outside the window**, which this city's proximity-first rule does not admit to any tier.
- **Split (b)** (pool within the window): Idelsk-Uralia (prov.) **48.13%** · Siberia **34.75%** · Künnarantaiga **16.94%** · Tuva **0.17%**; the nine outside successors 0. In city-share terms (× 12.60%, each rounded): Idelsk-Uralia (prov.) 6.06% · Siberia 4.38% · Künnarantaiga 2.13% · Tuva 0.02%.
- **(b) is the split that matches this city's own rule**, since every tier here needs d ≤ 3 (`UEIC` L581–583). (a) is reported because the brief asks for both.
- **The two splits differ by more than 5 points for five successors** (from (a) to (b): Russia −41.83, Idelsk-Uralia +24.72, Siberia +17.85, Künnarantaiga +8.70, Donska-Kubania −7.12).
- **Counts:** the tables above; every column sums exactly to 62,318 robots and 60,138 humans (largest remainder, §0.2).
- **Effective tier (informational):** under the proximity-first rule, **Russia (the core state), Donska-Kubania (prov.), Karelia and the six North Caucasus republics are absent** (outside the window). **Idelsk-Uralia (prov.)** 5.85M (d = 3), **Siberia** 4.23M (d = 1), **Künnarantaiga** 2.06M (**d = 0**) → **Notable** by pool (each below the 10.198M cut implied by the T2|T3 pools Australia 13M | Thailand 8M). **Tuva** 0.021M (d = 1) → Notable by the window rule, ⚠ below the 0.6M smallest pool the census carries (`UEIC` L1089). ⚠ **This city orders its Significant tier by proximity, not pool** (`UEIC` L607–610: a 16M pool at d = 0 outranks a 65M pool at d = 2), but **no formula for that ordering is written down**: the section gives its final shares as a table (`UEIC` L612–627), with China's share reduced by developer ruling (`UEIC` L598). So whether Künnarantaiga at d = 0 (2.06M) or Idelsk-Uralia at d = 3 (5.85M) would rank higher here is **NOT FOUND**; the tier given above is the pool reading only.
- **Sensitivities that move a share by more than 5 points in (b) (flagged):**
  - **(b-sub):** Idelsk-Uralia (prov.) **48.13 → 28.76 (−19.36)** (only its +4 units, 42.9% of its pool, count); Siberia **34.75 → 48.45 (+13.70)**; Künnarantaiga **16.94 → 22.54 (+5.60)** (its +11 and +12 units drop out).
  - **Population only:** Idelsk-Uralia (prov.) **+12.69** (to 60.82), Siberia **−10.21** (to 24.54).
  - **Official zones with θ = 5%:** **Donska-Kubania (prov.) enters** (Astrakhan', official +4, 7.4% of its pool, d = 3) at **12.77%**; Idelsk-Uralia **−6.15** (to 41.98).
- **Sensitivities that move nothing by more than 5 points in (b):** V1c, V2 (Siberia +1.04), K-in, C-15 (Idelsk-Uralia +0.71), θ = 5%, θ = 25%, official zones at θ = 10% or 25%, centroid zones, the three knife-edge cities, no Gini.
- **Split (a) sensitivities** are city-independent (population only is the one over 5 points: Russia −10.47, Idelsk-Uralia +7.49).
- **Window membership flips:** Donska-Kubania (prov.) OUT → IN under official zones with θ = 5%. No other.

### 7.7 NOT FOUND for Relung Panen
The First Interwar record itself · a written rule for ordering this city's tiers by proximity (the section gives only the resulting shares) · whether the city's single-door premise survives the 2026-10-29 airport rulings (`UEIC` L592: *"not ruled"*), which is what makes (b) the matching split here · the threshold θ · whether a floor excludes pools below 0.6M · the Gini penalty's functional form (`UEIC` L1057).

---

## FINAL

**Plainly, again:** the First Interwar Period record does not exist yet; every figure here is a present-day real-world regional figure aggregated to the successors' territories (DERIVED) standing in for it; **nothing here is a ruling or a recommendation**; the successor names are the developer's, and Idelsk-Uralia and Donska-Kubania are provisional. No spec, census or composition file was edited; nothing was committed.

### F0 · Method used (full statement in §0)
Primary variant **V1 · K-out · INIT · θ = 10% · solar zones · no wraparound · largest-city zone per subject · E = P × y2024 × (1 − G2022)** (the coordinator's defaults S1–S7, not rulings). **(a)** = W_k ÷ ΣW. **(b)** = the same over the successors whose meaningful zones (q ≥ θ) come within ±3 of the city's solar zone. Counts by largest remainder (Hamilton), each column summing exactly to the city's former-Russia robots and humans. Tiers informational: Ê = 25M × (a) share, placed against the city's own T2|T3 gap (the side of the larger sub-gap), with the Notable tier closed to small pools beyond d = 3 (every tier, at Relung Panen). Sensitivities: V1c, V2, K-in, C-15, θ 5% and 25%, official zones, centroid zones, three knife-edge cities, no Gini, population only, (b-sub), and four combinations. No web search was run.

### F1–F7 · One table per city (each stands on its own; DERIVED)

**F1 · Davis** (solar +5; former Russia share 5.64%; Census I 34,206 robots, 32,472 humans)

| Successor | d | Window | (a) % | (b) % | (a) robots | (a) humans | (b) robots | (b) humans | Tier (informational) |
|---|--:|:-:|--:|--:|--:|--:|--:|--:|---|
| Russia | 2 | IN | 41.83 | 41.83 | 14,309 | 13,584 | 14,309 | 13,584 | Significant |
| Idelsk-Uralia (prov.) | 1 | IN | 23.41 | 23.41 | 8,006 | 7,600 | 8,006 | 7,600 | Notable |
| Donska-Kubania (prov.) | 2 | IN | 7.12 | 7.12 | 2,436 | 2,313 | 2,436 | 2,313 | Notable |
| Künnarantaiga | 2 | IN | 8.24 | 8.24 | 2,819 | 2,676 | 2,819 | 2,676 | Notable |
| Siberia | 0 | IN | 16.90 | 16.90 | 5,782 | 5,489 | 5,782 | 5,489 | Notable |
| Tuva | 1 | IN | 0.08 | 0.08 | 29 | 27 | 29 | 27 | Notable ⚠ <0.6M |
| Karelia | 3 | IN | 0.97 | 0.97 | 332 | 315 | 332 | 315 | Notable ⚠ <0.6M |
| Chechnya | 2 | IN | 0.29 | 0.29 | 98 | 93 | 98 | 93 | Notable ⚠ <0.6M |
| Dagestan | 2 | IN | 0.61 | 0.61 | 210 | 199 | 210 | 199 | Notable ⚠ <0.6M |
| Ingushetia | 2 | IN | 0.06 | 0.06 | 21 | 20 | 21 | 20 | Notable ⚠ <0.6M |
| Kabardino-Balkaria | 2 | IN | 0.20 | 0.20 | 67 | 63 | 67 | 63 | Notable ⚠ <0.6M |
| Karachay-Cherkessia | 2 | IN | 0.10 | 0.10 | 33 | 32 | 33 | 32 | Notable ⚠ <0.6M |
| North Ossetia-Alania | 2 | IN | 0.19 | 0.19 | 64 | 61 | 64 | 61 | Notable ⚠ <0.6M |
| **Sum** | | | 100.00 | 100.00 | 34,206 | 32,472 | 34,206 | 32,472 | |

**F2 · Zhongshan** (solar +5; former Russia share 5.72%; Census I 34,005 robots, 33,229 humans)

| Successor | d | Window | (a) % | (b) % | (a) robots | (a) humans | (b) robots | (b) humans | Tier (informational) |
|---|--:|:-:|--:|--:|--:|--:|--:|--:|---|
| Russia | 2 | IN | 41.83 | 41.83 | 14,225 | 13,901 | 14,225 | 13,901 | Significant (Notable if read against the hand-adjusted `Specs` list, §2.6) |
| Idelsk-Uralia (prov.) | 1 | IN | 23.41 | 23.41 | 7,959 | 7,778 | 7,959 | 7,778 | Notable |
| Donska-Kubania (prov.) | 2 | IN | 7.12 | 7.12 | 2,422 | 2,367 | 2,422 | 2,367 | Notable |
| Künnarantaiga | 2 | IN | 8.24 | 8.24 | 2,802 | 2,738 | 2,802 | 2,738 | Notable |
| Siberia | 0 | IN | 16.90 | 16.90 | 5,748 | 5,616 | 5,748 | 5,616 | Notable |
| Tuva | 1 | IN | 0.08 | 0.08 | 29 | 28 | 29 | 28 | Notable ⚠ <0.6M |
| Karelia | 3 | IN | 0.97 | 0.97 | 330 | 322 | 330 | 322 | Notable ⚠ <0.6M |
| Chechnya | 2 | IN | 0.29 | 0.29 | 97 | 95 | 97 | 95 | Notable ⚠ <0.6M |
| Dagestan | 2 | IN | 0.61 | 0.61 | 209 | 204 | 209 | 204 | Notable ⚠ <0.6M |
| Ingushetia | 2 | IN | 0.06 | 0.06 | 21 | 21 | 21 | 21 | Notable ⚠ <0.6M |
| Kabardino-Balkaria | 2 | IN | 0.20 | 0.20 | 66 | 65 | 66 | 65 | Notable ⚠ <0.6M |
| Karachay-Cherkessia | 2 | IN | 0.10 | 0.10 | 33 | 32 | 33 | 32 | Notable ⚠ <0.6M |
| North Ossetia-Alania | 2 | IN | 0.19 | 0.19 | 64 | 62 | 64 | 62 | Notable ⚠ <0.6M |
| **Sum** | | | 100.00 | 100.00 | 34,005 | 33,229 | 34,005 | 33,229 | |

**F3 · Shirayuki** (solar +5; former Russia share 8.61%; Census I 47,651 robots, 45,716 humans)

| Successor | d | Window | (a) % | (b) % | (a) robots | (a) humans | (b) robots | (b) humans | Tier (informational) |
|---|--:|:-:|--:|--:|--:|--:|--:|--:|---|
| Russia | 2 | IN | 41.83 | 41.83 | 19,934 | 19,124 | 19,934 | 19,124 | Significant |
| Idelsk-Uralia (prov.) | 1 | IN | 23.41 | 23.41 | 11,153 | 10,700 | 11,153 | 10,700 | Notable |
| Donska-Kubania (prov.) | 2 | IN | 7.12 | 7.12 | 3,394 | 3,256 | 3,394 | 3,256 | Notable |
| Künnarantaiga | 2 | IN | 8.24 | 8.24 | 3,927 | 3,767 | 3,927 | 3,767 | Notable |
| Siberia | 0 | IN | 16.90 | 16.90 | 8,054 | 7,727 | 8,054 | 7,727 | Notable |
| Tuva | 1 | IN | 0.08 | 0.08 | 40 | 39 | 40 | 39 | Notable ⚠ <0.6M |
| Karelia | 3 | IN | 0.97 | 0.97 | 462 | 443 | 462 | 443 | Notable ⚠ <0.6M |
| Chechnya | 2 | IN | 0.29 | 0.29 | 137 | 131 | 137 | 131 | Notable ⚠ <0.6M |
| Dagestan | 2 | IN | 0.61 | 0.61 | 292 | 280 | 292 | 280 | Notable ⚠ <0.6M |
| Ingushetia | 2 | IN | 0.06 | 0.06 | 30 | 29 | 30 | 29 | Notable ⚠ <0.6M |
| Kabardino-Balkaria | 2 | IN | 0.20 | 0.20 | 93 | 89 | 93 | 89 | Notable ⚠ <0.6M |
| Karachay-Cherkessia | 2 | IN | 0.10 | 0.10 | 46 | 45 | 46 | 45 | Notable ⚠ <0.6M |
| North Ossetia-Alania | 2 | IN | 0.19 | 0.19 | 89 | 86 | 89 | 86 | Notable ⚠ <0.6M |
| **Sum** | | | 100.00 | 100.00 | 47,651 | 45,716 | 47,651 | 45,716 | |

**F4 · Sinheung** (solar +5; former Russia share 6.85%; Census I 34,724 robots, 32,841 humans)

| Successor | d | Window | (a) % | (b) % | (a) robots | (a) humans | (b) robots | (b) humans | Tier (informational) |
|---|--:|:-:|--:|--:|--:|--:|--:|--:|---|
| Russia | 2 | IN | 41.83 | 41.83 | 14,526 | 13,738 | 14,526 | 13,738 | Significant |
| Idelsk-Uralia (prov.) | 1 | IN | 23.41 | 23.41 | 8,127 | 7,687 | 8,127 | 7,687 | Notable |
| Donska-Kubania (prov.) | 2 | IN | 7.12 | 7.12 | 2,473 | 2,339 | 2,473 | 2,339 | Notable |
| Künnarantaiga | 2 | IN | 8.24 | 8.24 | 2,861 | 2,706 | 2,861 | 2,706 | Notable |
| Siberia | 0 | IN | 16.90 | 16.90 | 5,869 | 5,551 | 5,869 | 5,551 | Notable |
| Tuva | 1 | IN | 0.08 | 0.08 | 29 | 28 | 29 | 28 | Notable ⚠ <0.6M |
| Karelia | 3 | IN | 0.97 | 0.97 | 337 | 319 | 337 | 319 | Notable ⚠ <0.6M |
| Chechnya | 2 | IN | 0.29 | 0.29 | 100 | 94 | 100 | 94 | Notable ⚠ <0.6M |
| Dagestan | 2 | IN | 0.61 | 0.61 | 213 | 201 | 213 | 201 | Notable ⚠ <0.6M |
| Ingushetia | 2 | IN | 0.06 | 0.06 | 22 | 21 | 22 | 21 | Notable ⚠ <0.6M |
| Kabardino-Balkaria | 2 | IN | 0.20 | 0.20 | 68 | 64 | 68 | 64 | Notable ⚠ <0.6M |
| Karachay-Cherkessia | 2 | IN | 0.10 | 0.10 | 34 | 32 | 34 | 32 | Notable ⚠ <0.6M |
| North Ossetia-Alania | 2 | IN | 0.19 | 0.19 | 65 | 61 | 65 | 61 | Notable ⚠ <0.6M |
| **Sum** | | | 100.00 | 100.00 | 34,724 | 32,841 | 34,724 | 32,841 | |

**F5 · Mirny** (solar +6; former Russia share 7.22%; Census I 50,379 robots, 48,987 humans)

| Successor | d | Window | (a) % | (b) % | (a) robots | (a) humans | (b) robots | (b) humans | Tier (informational) |
|---|--:|:-:|--:|--:|--:|--:|--:|--:|---|
| Russia | 3 | IN | 41.83 | 42.24 | 21,075 | 20,493 | 21,281 | 20,693 | Significant |
| Idelsk-Uralia (prov.) | 2 | IN | 23.41 | 23.64 | 11,792 | 11,466 | 11,907 | 11,578 | Notable |
| Donska-Kubania (prov.) | 3 | IN | 7.12 | 7.19 | 3,588 | 3,489 | 3,623 | 3,523 | Notable |
| Künnarantaiga | 1 | IN | 8.24 | 8.32 | 4,152 | 4,037 | 4,192 | 4,077 | Notable |
| Siberia | 0 | IN | 16.90 | 17.07 | 8,515 | 8,280 | 8,599 | 8,361 | Notable |
| Tuva | 0 | IN | 0.08 | 0.09 | 43 | 41 | 43 | 42 | Notable ⚠ <0.6M |
| Karelia | 4 | OUT | 0.97 | 0.00 | 488 | 475 | 0 | 0 | absent |
| Chechnya | 3 | IN | 0.29 | 0.29 | 144 | 140 | 146 | 142 | Notable ⚠ <0.6M |
| Dagestan | 3 | IN | 0.61 | 0.62 | 309 | 300 | 312 | 303 | Notable ⚠ <0.6M |
| Ingushetia | 3 | IN | 0.06 | 0.06 | 32 | 31 | 32 | 31 | Notable ⚠ <0.6M |
| Kabardino-Balkaria | 3 | IN | 0.20 | 0.20 | 98 | 96 | 99 | 97 | Notable ⚠ <0.6M |
| Karachay-Cherkessia | 3 | IN | 0.10 | 0.10 | 49 | 48 | 50 | 48 | Notable ⚠ <0.6M |
| North Ossetia-Alania | 3 | IN | 0.19 | 0.19 | 94 | 91 | 95 | 92 | Notable ⚠ <0.6M |
| **Sum** | | | 100.00 | 100.00 | 50,379 | 48,987 | 50,379 | 48,987 | |

**F6 · Casey** (solar +7; former Russia share 6.13%; Census I 47,415 robots, 45,713 humans)

| Successor | d | Window | (a) % | (b) % | (a) robots | (a) humans | (b) robots | (b) humans | Tier (informational) |
|---|--:|:-:|--:|--:|--:|--:|--:|--:|---|
| Russia | 4 | OUT | 41.83 | 0.00 | 19,835 | 19,123 | 0 | 0 | Significant (large-pool clause) |
| Idelsk-Uralia (prov.) | 3 | IN | 23.41 | 48.13 | 11,098 | 10,700 | 22,820 | 22,001 | Notable |
| Donska-Kubania (prov.) | 4 | OUT | 7.12 | 0.00 | 3,377 | 3,256 | 0 | 0 | absent |
| Künnarantaiga | 0 | IN | 8.24 | 16.94 | 3,907 | 3,767 | 8,034 | 7,746 | Notable |
| Siberia | 1 | IN | 16.90 | 34.75 | 8,014 | 7,726 | 16,479 | 15,887 | Notable |
| Tuva | 1 | IN | 0.08 | 0.17 | 40 | 39 | 82 | 79 | Notable ⚠ <0.6M |
| Karelia | 5 | OUT | 0.97 | 0.00 | 460 | 443 | 0 | 0 | absent |
| Chechnya | 4 | OUT | 0.29 | 0.00 | 136 | 131 | 0 | 0 | absent |
| Dagestan | 4 | OUT | 0.61 | 0.00 | 291 | 280 | 0 | 0 | absent |
| Ingushetia | 4 | OUT | 0.06 | 0.00 | 30 | 29 | 0 | 0 | absent |
| Kabardino-Balkaria | 4 | OUT | 0.20 | 0.00 | 92 | 89 | 0 | 0 | absent |
| Karachay-Cherkessia | 4 | OUT | 0.10 | 0.00 | 46 | 45 | 0 | 0 | absent |
| North Ossetia-Alania | 4 | OUT | 0.19 | 0.00 | 89 | 85 | 0 | 0 | absent |
| **Sum** | | | 100.00 | 100.00 | 47,415 | 45,713 | 47,415 | 45,713 | |

**F7 · Relung Panen** (solar +7; former Russia share 12.60%; Census I 62,318 robots, 60,138 humans)

| Successor | d | Window | (a) % | (b) % | (a) robots | (a) humans | (b) robots | (b) humans | Tier (informational) |
|---|--:|:-:|--:|--:|--:|--:|--:|--:|---|
| Russia | 4 | OUT | 41.83 | 0.00 | 26,069 | 25,157 | 0 | 0 | absent |
| Idelsk-Uralia (prov.) | 3 | IN | 23.41 | 48.13 | 14,586 | 14,076 | 29,992 | 28,943 | Notable |
| Donska-Kubania (prov.) | 4 | OUT | 7.12 | 0.00 | 4,438 | 4,283 | 0 | 0 | absent |
| Künnarantaiga | 0 | IN | 8.24 | 16.94 | 5,136 | 4,956 | 10,560 | 10,190 | Notable |
| Siberia | 1 | IN | 16.90 | 34.75 | 10,533 | 10,165 | 21,658 | 20,901 | Notable |
| Tuva | 1 | IN | 0.08 | 0.17 | 53 | 51 | 108 | 104 | Notable ⚠ <0.6M |
| Karelia | 5 | OUT | 0.97 | 0.00 | 604 | 583 | 0 | 0 | absent |
| Chechnya | 4 | OUT | 0.29 | 0.00 | 179 | 172 | 0 | 0 | absent |
| Dagestan | 4 | OUT | 0.61 | 0.00 | 382 | 369 | 0 | 0 | absent |
| Ingushetia | 4 | OUT | 0.06 | 0.00 | 39 | 38 | 0 | 0 | absent |
| Kabardino-Balkaria | 4 | OUT | 0.20 | 0.00 | 122 | 117 | 0 | 0 | absent |
| Karachay-Cherkessia | 4 | OUT | 0.10 | 0.00 | 61 | 59 | 0 | 0 | absent |
| North Ossetia-Alania | 4 | OUT | 0.19 | 0.00 | 116 | 112 | 0 | 0 | absent |
| **Sum** | | | 100.00 | 100.00 | 62,318 | 60,138 | 62,318 | 60,138 | |

### F8 · Flags, city by city (moves of more than 5 points, and window flips; each city on its own terms, no city compared with another)
- **Davis (+5):** all thirteen successors inside, so (a) = (b). Over 5 points: **θ = 25%** removes Künnarantaiga (8.24 → 0); **(b-sub)** cuts it to 2.74; **population only** moves Russia −10.47 and Idelsk-Uralia +7.49 and drops Russia's tier from Significant to Notable. Russia's Significant tier is a knife-edge (Ê 10.46M against a 10.20M cut).
- **Zhongshan (+5):** all thirteen successors inside, so (a) = (b). Over 5 points: **θ = 25%** removes Künnarantaiga (8.24 → 0); **(b-sub)** cuts it to 2.74; **population only** moves Russia −10.47 and Idelsk-Uralia +7.49 and drops Russia's tier from Significant to Notable. Russia's Significant tier is a knife-edge (Ê 10.46M against a 10.20M cut). Read against the city's hand-adjusted `Specs` list, Russia would be Notable instead.
- **Shirayuki (+5):** all thirteen successors inside, so (a) = (b). Over 5 points: **θ = 25%** removes Künnarantaiga (8.24 → 0); **(b-sub)** cuts it to 2.74; **population only** moves Russia −10.47 and Idelsk-Uralia +7.49 and drops Russia's tier from Significant to Notable. Russia's Significant tier is a knife-edge (Ê 10.46M against a 10.20M cut).
- **Sinheung (+5):** all thirteen successors inside, so (a) = (b). Over 5 points: **θ = 25%** removes Künnarantaiga (8.24 → 0); **(b-sub)** cuts it to 2.74; **population only** moves Russia −10.47 and Idelsk-Uralia +7.49 and drops Russia's tier from Significant to Notable. Russia's Significant tier is a knife-edge (Ê 10.46M against a 10.20M cut).
- **Mirny (+6):** Karelia outside; Russia, Donska-Kubania and the six republics at the edge (d = 3). **Moscow at +2 with θ = 25%**, or **centroid zones with θ = 25%**, take Russia out (42.24 → 0; Idelsk-Uralia +17.29, Siberia +12.48, Künnarantaiga +6.09, Donska-Kubania +5.26). **(b-sub)** Russia −7.36; **population only** Russia −10.62, Idelsk-Uralia +7.52. Official zones bring Karelia in (0.97 points).
- **Casey (+7):** only Idelsk-Uralia (d = 3), Künnarantaiga (d = 0), Siberia (d = 1) and Tuva inside; **(a) and (b) differ by up to 41.83 points**. In (b): **(b-sub)** Idelsk-Uralia −19.36, Siberia +13.70, Künnarantaiga +5.60; **population only** Idelsk-Uralia +12.69, Siberia −10.21; **official zones with θ = 5%** bring Donska-Kubania in at 12.77. **Tier mismatch:** Russia (the core state) is T2-sized and so Significant by the large-pool clause, but gets 0 in (b).
- **Relung Panen (+7, proximity-first):** Idelsk-Uralia (d = 3), Künnarantaiga (d = 0), Siberia (d = 1) and Tuva inside; (b) is the split that matches the city's own rule, which places Russia (the core state), Donska-Kubania, Karelia and the six republics in no tier; **(a) and (b) differ by up to 41.83 points**. In (b): **(b-sub)** Idelsk-Uralia −19.36, Siberia +13.70, Künnarantaiga +5.60; **population only** Idelsk-Uralia +12.69, Siberia −10.21; **official zones with θ = 5%** bring Donska-Kubania in at 12.77.

### F9 · NOT FOUND (unit-wide)
- **The First Interwar record** for every successor: population, income, inequality, borders over time (RS1 §2). Everything here stands in for it.
- **The meaningful-share threshold θ** (`UEIC` L46–53 bound it only from below, above 2.5%). It decides Künnarantaiga's place at the +5 cities and, with Moscow's zone, Russia's place at Mirny.
- **A number for "large pool"** (`UEIC` L31). It decides whether Russia (the core state) is Significant or absent at Casey.
- **A floor** below which a pool does not appear (`UEIC` L1083–1085 mention one with no number); seven or eight successors per city fall below the census's smallest pool (0.6M, `UEIC` L1089).
- **The Gini penalty's functional form** (`UEIC` L1057); (1 − G) is RS1's convention.
- **Whether a former share divides by (a) or (b)** where the window cuts successors out (at Mirny, Karelia's 0.97 points; at Casey, 51.37%; at Relung Panen, 51.37%). No file says.
- **Which tier list governs** where a city's `Specs` table was hand-adjusted (Zhongshan; also Shirayuki and Sinheung, where the cut happens to be unchanged).
- **A rule for ordering tiers by proximity** at Relung Panen (only the resulting shares are written).
- **The gaps RS1b lists** (Ukrainian Gini; Donetsk and Luhansk GRP after 2013; the correct 2022 Ingushetia GRP; a sourced left-bank Kherson population; Rosstat primaries; which Gini measure CEIC carries). They touch only the V2 and 2022-form sensitivities here, so none was searched.

### F10 · What is left
RS3 and RS4 (other cities; not this unit). For these seven cities: the developer's choices on θ, "large pool", (a) versus (b), the tier list to read against, and the defaults S1–S7; then the reorganization itself, which is a separate job.
