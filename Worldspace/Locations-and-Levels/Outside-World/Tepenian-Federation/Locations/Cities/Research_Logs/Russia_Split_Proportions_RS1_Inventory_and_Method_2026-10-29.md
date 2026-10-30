# Russia-split proportions · Unit RS1 · Data inventory and method (2026-10-29)

**Brief:** `Research_Logs/Russia_Split_Proportions_Research_BRIEF_2026-10-29.md` (Unit RS1). Draft research only: nothing here is a ruling, a design or a recommendation, and no other file is edited.

**Labels used on every claim:** SOURCED (file and line, or URL) · UNVERIFIED · DERIVED · NOT FOUND.

## PROGRESS
- [x] 1 Successor nations as the developer's files define them
- [x] 2 What the First Interwar Period data states
- [x] 3 The other Russia sources
- [x] 4 The composition method to apply, and per-successor inputs found / NOT FOUND
- [x] 5 Derivation procedure for RS2 to RS4 (method only)
- [x] FINAL

**Abbreviations for the files cited** (all read in full or in the cited ranges this session):
- `MAP` = `/home/kuroskalacs/Documents/Doll-Fi/media/y-files/Map Files/`
- `TRK` = `MAP/Russia/PROGRESS TRACKER - Read This First.md`
- `R09` = `MAP/Russia/02 reorganization/09 follow-up/` (`subdivisions.csv` cited as `R09/sub` with **file line numbers**; line 1 is the header, so line n is data row n−1)
- `R01D` = `MAP/Russia/02 reorganization/01 follow-up/Russia - Reorganization Decisions (round 1).md`
- `R01K` = `MAP/Russia/02 reorganization/01 follow-up/Russia - Karelia, Murmansk and Finland (pending future decision).md`
- `EUI` = `MAP/Europe/02 reorganization/04 follow-up - final map INIT 2083/README - Europe INIT 2083 map.md`
- `EUB` = `MAP/Europe/02 reorganization/03 follow-up - determining Western Europe/Eastern Ukraine - Candidate Border Lines (working).md` (byte-identical to the 01 and 02 follow-up copies, md5 `027a43c5…`)
- `ATL` = `MAP/x Full Earth/z-full-world-atlas/` (`README.md`; `data/regions/russia/README.md` cited as `ATL/ru`)
- `NOV` = `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/`
- `SURV` = `NOV/extractions/Russia - Federal Fractures and the Far Eastern Question (survey).md`
- `NAMES` = `NOV/extractions/Russia - Candidate Names for Countries A, C and D (research).md`
- `TLR` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`
- `PWN` = GDD `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Post-War_Nations_Founder_Reference.md`
- `UEIC` = GDD `…/Locations/Cities/Upper_Earth_Immigration_Composition.md`
- `DRL` = GDD `Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`
- `NE` = Natural Earth 1:10m (the developer's own map pipeline data): admin-1 subset at `ATL/data/regions/russia/cache/ne-admin1-russia-ukraine-subset.geojson`; populated places at `/tmp/ne_test/ne_10m_populated_places_simple.geojson` (`TRK` L253 names `/tmp/ne_test` as the established pipeline).

---

## 1 · The successor nations as the developer's files define them

### 1.1 Which folder and file is authoritative

- **`02 reorganization/09 follow-up/` is the current authoritative state** for all six maps and the data: *"09 is now the current authoritative folder for all six maps"* (`TRK` L15) and *"✅ CURRENT AUTHORITATIVE STATE for ALL SIX maps, as of 2026-09-30 … Work FROM this folder now"* (`TRK` L72–76). **SOURCED.**
- ⚠ `TRK` L129 still heads its nation table *"`04 follow-up/subdivisions.csv` is the source of truth"*; that heading is older than the 2026-09-30 updates at L8–15, which name 09. The 04 file has 82 rows and lacks Crimea, Sevastopol and the eastern-Ukraine slice (row counts below). **SOURCED (the two lines); the reading that L129 is stale is DERIVED.**
- `02 reorganization/10 follow-up/` and `11 follow-up/` exist and are **empty** (directory listing, 2026-10-29). **SOURCED (listing).**
- `03 official timeline years/` and `04 timeline staging/` (with its subfolders `DISTILLED - ready for Timeline repo/` and `Place_Name/`) are **empty** for Russia (directory listing). **SOURCED (listing).** So the brief's items 1 and 2 cannot draw on them.
- `R09/README.md` L19 still says *"82 rows, 13 nations"*; the file now has 90 data rows (the atlas notes the same stale header: `ATL/ru` L6). **SOURCED.**

**The `x Full Earth/Russia/` copy versus `R09` (checked by md5, 2026-10-29):**

| File | Same as `R09`? |
|---|---|
| `subdivisions.csv` | **identical** (md5 `4ed710cb749105ff92c40bd120b143b9` both) |
| `spheres.csv`, `CHANGES.md`, `README.md`, `cyrillic_names.py`, `render_map_russia_full.py` | identical |
| `russia_full_map.svg` | identical |
| `russia_full_map.png`, `russia_west_map.png`, `russia_reference_map.png`, `russia_woodard_map.png` | **differ.** The Full Earth PNGs are dated 2026-09-27 (pre-Crimea renders); the `R09` PNGs are dated 2026-09-30. **`R09` is newer and authoritative.** `ATL/ru` L30 records the same: *"The reference PNG on disk (dated 09-27) predates the slice."* |

**SOURCED (md5 and listing); the difference matters only for the images, not for any data used here.**

**Every copy of `subdivisions.csv` was checked for population data** (rows / non-empty `population` cells): `01 initial generations` 83/0 · `01 follow-up` reorganized 83/0 and FINAL 82/0 · `02`–`07` follow-up 82/0 each · `08` 84/0 · `09` 90/0 · `x Full Earth/Russia` 90/0 · archive copies 82–84/0 · novel-repo `NOV/nations/russia-map-data/subdivisions.csv` 83/0. **The population column is blank in every row of every copy. SOURCED (count run on each file).** `R09/CHANGES.md` L70 confirms it is deliberate: *"population data for the new subdivisions (blank, like every other subdivision)."*

### 1.2 The successor table (state of `R09`, the 13 nations of the package)

Footprint columns are **DERIVED** by this unit from the developer's own Natural Earth data (method in 1.3). "Urban share by zone" is the share of the summed Natural Earth `pop_max` of all NE populated places that fall inside the nation's units: **a proxy for where people live, not a population count.** Per-unit and per-place tables are in the scratch files listed in 1.3.

| Nation (exact spelling) | Name status | Units (`R09/sub` file lines) | Capital | Population in `subdivisions.csv` | Territory solar zones (DERIVED) | Urban share by solar zone (DERIVED, NE proxy) | When it exists (SOURCED) |
|---|---|---|---|---|---|---|---|
| **Russia** | Not provisional (the core state; `DRL` L789: *"'Russia' is the core state, not the old whole"*) | 24: L8–25 (18 core: Belgorod, Bryansk, City of St. Petersburg, Kaluga, Kursk, Leningrad, Lipetsk, Moskovskaya, Moskva, Novgorod, Orel, Pskov, Ryazan', Smolensk, Tambov, Tula, Tver', Voronezh) + L86–91 (6 ex-Ukrainian: Luhans'k, Donets'k, Kharkiv, Dnipropetrovs'k, Zaporizhzhya, Kherson *left bank only*) | Moscow (`TRK` L133) | **NOT FOUND** (blank, all 24 rows) | lon 26.9°E–43.2°E → **+2 to +3** | +2: 43.9% · +3: 56.1% (90 places). ⚠ Moscow itself is at 37.61°E = 2.507 zones, rounding to **+3 by 0.007 of a zone** | At the start of 2083 (`EUI` L14, L18); the eastern-Ukraine slice is drawn from INIT on (`EUI` L13–14) |
| **Idelsk-Uralia** | ⚠ **Provisional (conflicting).** `TRK` L134: *"✅ named 2026-09-27"*. But `R09/sub` L50 note: *"Name not yet decided — placeholder 'Idelsk-Uralia'"*; `ATL/README.md` L28 and `ATL/ru` L39: *"Idelsk-Uralia and Donska-Kubania names are still placeholders per the package"*. **Marked provisional here** | 25: L50–56, L58, L60–76 (Bashkortostan, Tatarstan, Ivanovo, Kostroma, Vladimir, Yaroslavl', Arkhangel'sk, Komi, Nenets, Vologda, Chelyabinsk, Kurgan, Orenburg, Perm', Sverdlovsk, Udmurt, Chuvash, Kirov, Mariy-El, Mordovia, Nizhegorod, Penza, Samara, Saratov, Ul'yanovsk). **+ Murmansk at the C-15 stage** (`EUI` L40; `ATL/ru` L17 counts 26) | Nizhny Novgorod (`TRK` L134) | **NOT FOUND** | lon 34.7°E–69.0°E → **+2 to +5** (Arkhangel'sk's Arctic islands reach +5) | +3: 57.7% · +4: 42.3% (156 places) | From INIT 2083 (`EUI` L14) |
| **Donska-Kubania** | ⚠ **Provisional (conflicting)**, same three sources as Idelsk-Uralia (`TRK` L135 "✅ named"; `R09/sub` L81 "placeholder"; `ATL/README.md` L28) | 9: L77–85 (Krasnodar, Adygey, Rostov, Stavropol', Kalmyk, Astrakhan', Volgograd, **Crimea** and **Sevastopol** as an *Autonomous Zone*, L84–85; Sevastopol's inclusion is *"assumed … OPEN"*, L85) | Rostov-on-Don (`TRK` L135) | **NOT FOUND** | lon 32.5°E–49.3°E → **+2 to +3** | +2: 12.8% (Crimea, Sevastopol) · +3: 87.2% (48 places) | From INIT 2083, with Crimea an Autonomous Zone (`EUI` L14) |
| **Künnarantaiga** (formerly "Country A") | Not provisional: *"✅ named 2026-09-27"* (`TRK` L136; `R09/sub` L26). The ASCII form "Kunnarantaiga" is the map's primary line (`TRK` L199–201) | 12: L26–37 (Sakha (Yakutia), Amur, Buryat, Chita, Chukchi Autonomous Okrug, Kamchatka, Khabarovsk, Maga Buryatdan [= Magadan, L33], Primor'ye, Sakhalin (with the Kurils), Yevrey, Irkutsk) | Vladivostok (`TRK` L136) | **NOT FOUND** | lon 95.7°E to 169.0°W (Chukotka crosses the antimeridian) → **+6 to +12, and −11 to −12** | +7: 32.3% (Irkutsk Oblast, Buryatia) · +8: 11.9% · +9: 45.5% · +10: 6.7% · +11: 3.3% · +12: 0.2% · −12/−11: 0.1% (172 places) | Not dated in the files; the map is undated (`PWN` L19) |
| **Siberia** | Not provisional (`TRK` L137; `R01D` L19–21) | 11: L38–48 (Khakass, Krasnoyarsk, Altay, Gorno-Altay, Kemerovo, Khanty-Mansiy, Novosibirsk, Omsk, Tomsk, Tyumen', Yamal-Nenets) | Novosibirsk (`TRK` L137) | **NOT FOUND** | lon 59.2°E–113.9°E → **+4 to +8** | +4: 6.3% · +5: 29.6% · +6: 63.5% · +7: 0.6% (105 places) | Undated (`PWN` L19) |
| **Tuva** | Not provisional (`TRK` L138) | 1: L49 | Kyzyl (`TRK` L138) | **NOT FOUND** | lon 88.7°E–99.2°E → **+6 to +7** | +6: 100% (2 places) | Undated |
| **Karelia** | Name not provisional (*"Named 'Karelia' (author-confirmed, no longer a placeholder)"*, `R09/sub` L57). **The nation itself is a "semi-stable proto-country"** (`R09/sub` L57; `R01K` L15–18) | 2: L57 (Karelia), L59 (Murmansk) | **Not set** (`TRK` L139, L175–176) | **NOT FOUND** | lon 28.4°E–41.4°E → **+2 to +3** | +2: 100% (15 places) | **Exists at INIT 2083 and on maps B to C-14; gone by C-15**, where the Republic of Karelia is part of Finland and Murmansk part of Idelsk-Uralia (`EUI` L18, L40). *"Open: when"* (`EUI` L42). `ATL/ru` L11 builds the atlas on the C-15 state, in which *"that nation does not exist."* |
| **Chechnya** | Not provisional | 1: L2 | Grozny (`TRK` L143) | **NOT FOUND** | +3 | +3: 100% | From INIT 2083 (`EUI` L14) |
| **Dagestan** | Not provisional | 1: L3 | Makhachkala (`TRK` L145) | **NOT FOUND** | +3 | +3: 100% | From INIT 2083 |
| **Ingushetia** | Not provisional | 1: L4 | Magas (`TRK` L144) | **NOT FOUND** | +3 | +3: 100% | From INIT 2083 |
| **Kabardino-Balkaria** | Not provisional (`[P]` removed, `R09/sub` L5) | 1: L5 | Nalchik (`TRK` L147) | **NOT FOUND** | +3 | +3: 100% | From INIT 2083 |
| **Karachay-Cherkessia** | Not provisional (`[P]` removed, `R09/sub` L6) | 1: L6 | Cherkessk (`TRK` L148) | **NOT FOUND** | +3 | +3: 100% | From INIT 2083 |
| **North Ossetia-Alania** | Not provisional (`[P]` removed, `R09/sub` L7) | 1: L7 | Vladikavkaz (`TRK` L146) | **NOT FOUND** | +3 | +3: 100% | From INIT 2083 |

**Not a successor in the Russia package, but part of the pre-war Russian Federation:** **Kaliningrad**. *"Removed from Russia's nation list entirely"* (`TRK` L149; `R01D` L57–60); not in `subdivisions.csv` (`ATL/ru` L33); a member of the Confederacy of Intermarium Nations, joining at map C-01 *"Lithuania and Kaliningrad join"* (`EUI` L13, L31). Solar zone **+1** (NE places, DERIVED). **SOURCED except the zone.**

**Capitals of the North Caucasus republics, Tuva and Siberia are SOURCED from `TRK` L137–148.** The capitals of Russia, Idelsk-Uralia, Donska-Kubania and Künnarantaiga are SOURCED from `TRK` L133–136 and L227–230 (*"Every named nation on the map now has a settled capital except Karelia"*). Crimea Autonomous Zone capital: not decided (`R09/sub` L84; `ATL/ru` L39).

### 1.3 How the footprint columns were computed (DERIVED; scratch, not part of any repo)

- **Territory zones:** for each `R09/sub` unit, the matching Natural Earth admin-1 polygon (name join, the same join the atlas build uses, `ATL/data/regions/russia/build_russia.py` L36–37). Longitude extent and an approximate area-weighted centroid were taken; **solar zone = round(longitude ÷ 15)**, the rule in `UEIC` L28 and `PWN` L9. All 90 package names matched an NE unit; Kaliningrad and one unnamed NE islet are the only NE Russia units with no package nation (the atlas drops the same islet, `ATL/ru` L38). ⚠ The NE Kherson unit is the whole oblast, not the left bank only; at zone resolution this changes nothing (both banks lie in +2). Output: `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/a4f4478c-4c10-4425-b67b-16739b0736bb/scratchpad/out/unit_zones.csv`.
- **Urban share by zone:** every NE populated place in Russia or Ukraine was assigned to a unit by point-in-polygon, then `pop_max` was summed by nation and by the place's own solar zone. Output: `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/a4f4478c-4c10-4425-b67b-16739b0736bb/scratchpad/out/places_by_successor.csv`. **Limits, stated flatly:** NE `pop_max` is a city or metro estimate of mixed vintage, rural people are missing, and some small places carry placeholder values (10, 0). It shows *where the towns are*, not a census. **It is not a population input and must not be used as one.**
- **The urban-proxy share of each nation in the summed total** (DERIVED, NE `pop_max`, 89.4M in all): Russia 36.7% · Idelsk-Uralia 29.9% · Siberia 12.3% · Donska-Kubania 9.8% · Künnarantaiga 7.4% · Karelia 1.1% · Dagestan 0.9% · Kaliningrad 0.6% · North Ossetia-Alania 0.5% · Kabardino-Balkaria 0.3% · Chechnya 0.3% · Karachay-Cherkessia 0.1% · Tuva 0.1% · Ingushetia 0.1%. **Given only so RS2–RS4 can sanity-check census-based results; not an input.** It badly undercounts the republics, whose people are largely rural (e.g., Chechnya counts only Grozny, 226,100).
- The Natural Earth scripts used the system Python with the stock `json` module; the developer's `/tmp/mapvenv` geopandas install is broken on disk (its package folders are missing files) and was not repaired.

### 1.4 Populations the developer's files DO state (not in `subdivisions.csv`)

| Unit | Figure | Basis | Source |
|---|---|---|---|
| Donets'k | about 4.83M | Ukraine 2001 census | `EUB` L105 |
| Dnipropetrovs'k | about 3.56M | 2001 census | `EUB` L106 |
| Kharkiv | about 2.90M | 2001 census | `EUB` L107 |
| Luhans'k | about 2.54M | 2001 census | `EUB` L108 |
| Zaporizhzhya | about 1.93M | 2001 census | `EUB` L109 |
| Kherson, left bank | *"roughly 0.4 M (⚠️ an area-weighted guess)"* | 2001 census, area-weighted | `EUB` L110 |
| Mainland slice total | *"about 16 million"* | 2001 | `EUB` L111 |
| Crimea and Sevastopol | about 2.4M (L78: Crimea ~2.02M, Sevastopol ~0.38M) | 2001 | `EUB` L78, L112 |
| Primorsky Krai | 1.85M | real-world, year not stated | `SURV` L98 |
| Khabarovsk Krai | 1.29M | real-world, year not stated | `SURV` L98 |
| Jewish AO (Yevrey) | 150,453 (2021 census); est. 145,802 (2024) | real-world | `SURV` L99 |
| Sakhalin Oblast | 466,609 (2021 census) | real-world | `SURV` L129 |
| Tuva | 336,651 (2021 census) | real-world | `SURV` L151 |
| Moscow / St. Petersburg | 13.0M / 5.6M | real-world, year not stated | `SURV` L53 |
| Kaliningrad | *"489,359 people, 2020"* | real-world | `SURV` L309. ⚠ **UNVERIFIED and probably the city, not the oblast** (the oblast is roughly twice that by recall; recall is not evidence, so this is flagged, not corrected) |

**All SOURCED to the file and line given; none is a Tepenian-era population.** They are present-day (2001 or 2020s) real-world baselines. No file gives any population for any successor at any in-world date.

---

## 2 · What the First Interwar Period data states (2083 to 2564)

**The two folders the brief names hold nothing:** `MAP/Russia/03 official timeline years/` and `MAP/Russia/04 timeline staging/` (and both its subfolders) are **empty**. **SOURCED (listing).** Everything below comes from other files; each is quoted or paraphrased with its line, and nothing is extrapolated.

| # | Statement | Date or stage given | Source |
|---|---|---|---|
| F1 | *"a global nuclear war permanently reshaped the world on September 26, 2083 — countries collapsed, borders were redrawn, the pre-war geopolitical order was destroyed."* | 26 Sept 2083 | `TLR/Timeline Eras/1 The First Interwar Period/Timeline.md` L89–91 |
| F2 | The First Interwar timeline's confirmed successor roster (Set-Up, ~June 2088 to ~July 2131) names **no Russian successor** (it lists Korea, the Sinian Federation, Hawaii and the North American states). | 2088–2131 span | same file L123–136 |
| F3 | Europe's starting map shows, among "The East (10)": *"Russia (core, with the eastern-Ukraine slice), Idelsk-Uralia, Donska-Kubania (Crimea an Autonomous Zone), Karelia (with Murmansk, as the proto-country), and the North Caucasus republics …"* | **"Europe at the outset of 2083"** | `EUI` L3, L14 |
| F4 | *"Karelia and Murmansk are still the proto-country, not yet part of Finland; Murmansk later joins Idelsk-Uralia."* | INIT | `EUI` L18 |
| F5 | **C-15** *"also shows Karelia (the Republic) as part of Finland and Murmansk Oblast as part of Idelsk-Uralia"* (author: *"by the very end … Karelia is definitely part of Finland"*). **"Open: when"**; and for the series, *"No years are implied."* | Undated, after INIT | `EUI` L24, L40, L42 |
| F6 | The Russia map series' year: *"none (matches Europe INIT 2083)"*; *"So outside East Asia, whether these borders still stand in 2564 is not established."* | — | `PWN` L19, L27 |
| F7 | The Confederacy of Intermarium Nations: *"founded ~2108–2118 (research estimate only)"*; Kaliningrad joins at C-01. | ~2108–2118 (estimate) | `PWN` L18; `EUI` L31 |
| F8 | Karelia plan, undated: Stage 1 split into a *"semi-stable proto-country"*; Stage 2 merge with Finland; Stage 3 the ethnic-Russian population is *"'encouraged' to leave"* and relocates *"primarily into Country C's own northern territory (… Arkhangelsk, Komi, Nenets, Vologda), with some also relocating into the old Volga Republic and/or Tatarstan territory"* (Country C = Idelsk-Uralia). | Undated; *"Timing/sequencing … isn't specified"* (L48) | `R01K` L15–38, L48–51 |
| F9 | Tuva: *"an economic trade agreement with Mongolia"* (a canon fact, not a border change). | Undated | `R01D` L23–25; `R09/sub` L49 |
| F10 | Russia's own later-stage maps: *"Not built yet: … any maps for the Russian, West Asian or other regions' own progressions."* | — | `EUI` L42 |
| F11 | *"Stage 2 (material survey) has never been done for Russia."* | — | `TRK` L115–117, L231–233 |

**Not First Interwar, but bearing on the borders and found while looking (SOURCED, quoted only):**
- **Timeline canon, end of the Second Interwar Period:** the doll Lyuba Baranova was *"Built not long before the Long Night War, in East Intermaria (formerly West Russia)"* (`TLR/Worldspace/Characters/Dolls/Lyuba _Lyubochka_ Baranova [Люба _Любочка_ Баранова]/Personal_Background/Timeline.md` L13; README L6, L44). The novel repo's Europe intake records the open question: *"when and how the bloc takes in former West Russian territory is not yet known (OPEN)"* (`NOV/nations/Europe - GDD hand-over intake (Santa Luce, the two Italys, the CIN; 2026-10-23).md` L31–32, L51, L59). **No file says which successor (Russia, Karelia, Idelsk-Uralia …) "West Russia" means.**
- `DRL` L609–621 (`DR-23`; quotes at L618 and L621): the census and composition *"may stay built on pre-war nations (… Russia …) until the CST"*, and *"No census or composition edits … until all 38 cities have finished the ULM."*

**NOT FOUND, for every successor at any First Interwar date:** population, population change, GDP or income, inequality, migration figures (other than F8's direction), unions or splits beyond F3–F5 and F8, and any date after 2083 at which any Russian successor's border changes (F5 is the only change, and it is undated).

---

## 3 · The other Russia sources

**3.1 `SURV` (the Stage 1 survey, 2026-09-27, 343 lines).** A real-world frameworks survey, not an in-world history. What it supplies:
- Method: tiered ethnic identity, not Woodard's settlement doctrine (L19–25, L61–89).
- **The economic finding the split rests on:** *"only five of Russia's ~85 federal subjects produced over 70% of federal budget revenue — the oil/gas okrugs Khanty-Mansi and Yamalo-Nenets, Moscow, St. Petersburg, and Tatarstan. 72 of 85 subjects are net recipients"*; per-head GRP spread *"richest region (oil-producing Nenets AO) … poorest (Ingushetia) is 62-to-1"* (L27–33, 2019 data). Mapped to the successors (DERIVED from `R09/sub`): Khanty-Mansiy and Yamal-Nenets → **Siberia**; Moscow and St. Petersburg → **Russia**; Tatarstan → **Idelsk-Uralia**; Nenets → **Idelsk-Uralia**; Ingushetia → **Ingushetia**. **This concentration is what will move a GDP-weighted split; see 4.4.**
- Sakha produces *"~98% of Russia's diamonds"* (L266–268; also `R09/sub` L26).
- Present-day populations listed in 1.4. Ethnic-Russian shares by republic (L189–203), with a flagged Tuva discrepancy (10.1% vs 20%, L205–207).
- **Its own open items** (L304–324): the Rosstat twelve economic regions not pulled in; no material-base (Stage 2) survey.
- ⚠ Its header (L4–7) predates the map package (*"No map-data package exists yet"*) and its recommendations (Far Eastern state, Buryatia open) were then decided by the developer in round 1 (`R01D` L13–17). **Read it as background evidence, not as the current state.**

**3.2 `NAMES` (candidate names, 2026-09-27, 248 lines).** A menu, *"not a recommendation"* (L6–7). Territory checked against `02 follow-up` (L4–5), so it predates Karelia's split, Crimea and the Ukrainian slice (e.g., Country D listed as 7 subdivisions, L165). Outcome recorded elsewhere: Idel-Ural → **Idelsk-Uralia**, Don-Kuban → **Donska-Kubania** (`TRK` L110). Useful facts for this task: Rosstat's real economic regions do not match the successors (L136–145, L227–235: the real *Volga Economic Region* spans both Idelsk-Uralia and Donska-Kubania). **No population, GDP or Gini data.** SOURCED.

**3.3 `NOV/nations/russia-map-data/`.** `TRK` L77–80: *"mirrors the ORIGINAL 20-nation state only."* ⚠ **Internal mismatch:** its `README.md` (L14–46) describes the round-1 12-nation reorganization ("Country A/C/D", names not yet decided), while its `subdivisions.csv` carries the original 20 nations (83 rows: Russia 22, The Volga Republic 11, The Russian Far East 10, Western Siberia 9, … Kaliningrad 1; counted this session). Population blank (0 of 83). **Neither matches `R09`; do not use it for the split.** SOURCED.

**3.4 `PWN` (GDD, derived 2026-10-01).** How post-war nations are summarized in the GDD: *"working summary, not canon … the map files are the authority"* (L5–7); method *"solar time zone = round(longitude ÷ 15). Spans are estimates"* (L9). Russian successors by zone: Russia core +2…+3, Donska-Kubania, Karelia and the North Caucasus republics (+3) in the +2…+3 row (L39); Idelsk-Uralia +2…+5 (L40); Siberia +4…+8 and Tuva in +6…+7 (L41); Künnarantaiga +6…+12 (L44) with Chukotka at −11 (L33). *"Russia: split into 13 states"* (L52). **These spans agree with this unit's DERIVED territory zones in 1.2.** `PWN` counts Karelia as one of the 13, i.e. the INIT state, not C-15.

**3.5 Related rulings (context only; founders are not composition).** `DRL` L779 (`DR-34`): Lazar's founders are *"Russia (the core state) and the CIN"*. `DRL` L787–789 and L800–804 (`DR-35`): Vostok/Ariun Nuur is founded by **Künnarantaiga and Mongolia**; *"Wherever a pool or a founder says 'Russia', read the core state unless a successor is named. Consequence for later: `DR-9` names Russia for Mirny in pre-war terms; the CST recast will need a successor state."* **SOURCED.** These rule founders only; the composition tables are pre-war by `DR-23`.

---

## 4 · The composition method to apply, and which inputs exist

### 4.1 The method, restated plainly (all SOURCED to `UEIC`)

1. **Three factors** (L9–15): proximity; population; and *"GDP per capita × Gini inequality penalty (robot-ownership proxy)"*. Their product for a nation is its **Gini-adjusted effective population** ("effective pool", L1059).
2. **The Gini penalty's functional form is not stated.** The file says only that it *"reduces the robot-eligible fraction proportionally to inequality"* (L1057). **The exact formula: NOT FOUND** (searched the GDD for an explicit expression; none exists outside the industry formulas, which are unrelated).
3. **Russia's whole pool is "~25M"**, *"Medium GDP, high Gini — significant reduction"* (L76); *"moderate GDP per capita and high inequality (Gini ~0.37)"* (L1071). Close pools are ordered only approximately (L114). This 25M is the pool of **pre-war Russia** (`DRL` L618, `DR-23`).
4. **Proximity** (L21–33): city solar zone = round(longitude ÷ 15) (L28); distance = |nation zone − city zone| (L29); **a small pool reaches the Notable tier only if distance ≤ 3** (L30–31); large pools *"reach anywhere"* (L31); a nation routed through another's gateway takes the gateway's distance (L32–33). The window is *"a proxy for logistics, not a hard physical limit"* (L1101).
5. **Footprint rule** (L35–47): *"distance = the MINIMUM over the zones where a meaningful share of the nation's exile-eligible pool actually lives"*, with "meaningful share" the guard against scoring territory instead of people. The file's examples bound it but give no number: Réunion at *"~2.5% of France's effective pool"* is OUT (L53); Russia's Siberian belt, *"a large minority of its whole pool"*, is IN (L51). **The threshold: NOT FOUND as a number; the examples put it above 2.5%.**
6. **Tiers** (L17, L1107–1109): all qualifying nations in a city are ranked by effective pool; tier breaks fall at the largest ratio gaps in that city's ranking; allocation is **8 shares per T1 nation, 3 per T2, 1 per T3**.
7. **Exile rate** 2% of the effective pool (L1119–1123), with a ×0.65 revision applied globally to earlier figures (L1123). Not needed for a within-Russia split, because a split divides an existing count.

### 4.2 A method problem found in the source (stated flatly; not resolved here)

`UEIC` L38–41 scores Russia's footprint as *"ELEVEN time zones, +2 to +12 … Novosibirsk …, Krasnoyarsk …, Tomsk, Kemerovo and Barnaul all sit at UTC+7"*, and the Relung Panen row says *"Russia enters by SIBERIA … Novosibirsk and Krasnoyarsk sit on this exact meridian"* (L599). **Those are Russia's official (legal) zones, not solar zones.** On the file's own solar rule (L28), using the Natural Earth coordinates in the developer's pipeline (**DERIVED**): Novosibirsk 82.96°E → 5.53 → **+6**; Krasnoyarsk 92.86°E → 6.19 → **+6**; Tomsk 84.98°E → **+6**; Kemerovo 86.09°E → **+6**; Barnaul 83.75°E → **+6**; Omsk 73.40°E → **+5**. The solar **+7** urban population of the old Russia lies in **Irkutsk Oblast and Buryatia, which are Künnarantaiga's** (Irkutsk 104.25°E → 6.95 → +7), not Siberia's (Siberia's +7 share is 0.6% of its urban proxy, 1.2). That Russia's legal zones are UTC+2…+12 and that Novosibirsk keeps UTC+7 is **UNVERIFIED (recall)**; the solar figures are DERIVED from file data. **Consequence for RS2–RS4:** the nation-side zone must be stated as solar or official for each successor; the brief and `PWN` L9 use solar.

### 4.3 Inputs per successor: what the developer's files give, and what is NOT FOUND

| Successor | Population | GDP (GRP) per head | Gini | Zone footprint (territory) | Zone footprint (where people live) |
|---|---|---|---|---|---|
| Russia (core + slice) | **NOT FOUND** for the 18 core units. The 6 Ukrainian units: 2001 census, `EUB` L105–111 (Kherson left bank a guess). Moscow 13.0M, St. Petersburg 5.6M real-world (`SURV` L53) | **NOT FOUND** | **NOT FOUND** | `PWN` L39 (+2…+3, estimate); DERIVED 1.2 | DERIVED proxy only (1.2) |
| Idelsk-Uralia | **NOT FOUND** | **NOT FOUND** | **NOT FOUND** | `PWN` L40 (+2…+5); DERIVED | DERIVED proxy only |
| Donska-Kubania | **NOT FOUND**, except Crimea and Sevastopol, 2001 (`EUB` L78, L112) | **NOT FOUND** | **NOT FOUND** | `PWN` L39; DERIVED | DERIVED proxy only |
| Künnarantaiga | **NOT FOUND**, except real-world Primorsky, Khabarovsk, Jewish AO, Sakhalin (`SURV` L98–99, L129) | **NOT FOUND** | **NOT FOUND** | `PWN` L44, L33 (+6…+12, −11); DERIVED | DERIVED proxy only |
| Siberia | **NOT FOUND** | **NOT FOUND** (only that Khanty-Mansi and Yamal-Nenets are 2 of 5 donor regions, `SURV` L27–30) | **NOT FOUND** | `PWN` L41 (+4…+8); DERIVED | DERIVED proxy only |
| Tuva | Real-world 336,651 (2021) (`SURV` L151) | **NOT FOUND** | **NOT FOUND** | `PWN` L41; DERIVED | DERIVED proxy only |
| Karelia | **NOT FOUND** | **NOT FOUND** | **NOT FOUND** | `PWN` L39; DERIVED | DERIVED proxy only |
| Six North Caucasus republics | **NOT FOUND** | **NOT FOUND** (Ingushetia is the poorest, `SURV` L31–32) | **NOT FOUND** | `PWN` L39 (+3); DERIVED | DERIVED proxy only |
| Kaliningrad (CIN; pre-war Russia) | `SURV` L309, ⚠ UNVERIFIED (see 1.4) | **NOT FOUND** | **NOT FOUND** | DERIVED (+1) | — |

**Where real-world regional data could fill the gaps (every fill is DERIVED and must carry its year):**
- **Population by federal subject, 2021 census:** Rosstat's own tables are **unreachable from this environment** (every rosstat.gov.ru host fails TLS verification; recorded by EO3, `Relung_Panen_Ethnic_Origin_EO3_Oceania_and_Siberia_2026-10-29.md` L336 and log R1). EO3 used secondary transcriptions (Wikipedia and a mirror, EO3 L334–348) for its 23 belt subjects. RS2–RS4 need all 83 pre-war subjects (plus Crimea and Sevastopol in variant V2 below).
- **GRP per head by subject:** ru.wikipedia, *Список субъектов Российской Федерации по валовому продукту на душу населения*, which reproduces the Rosstat series *"Валовый региональный продукт на душу населения по субъектам Российской Федерации в 1998—2024 гг."*, revision `oldid=152668547` (EO3 L363; not reopened here). Caveat recorded there: GRP is booked where value added is registered, which overstates head-office regions and the two oil-and-gas okrugs (EO3 L394). **An alternative income input** is Rosstat's money income per head by subject (closer to "who could buy a robot"); it was not searched.
- **Gini by subject:** Rosstat publishes *"Коэффициент Джини (индекс концентрации доходов) в целом по России и по субъектам Российской Федерации"* in its *Неравенство и бедность* section (https://www.rosstat.gov.ru/folder/13723; search result only, **the page did not open in results and the host is TLS-blocked here**). Regional Rosstat offices publish single values, e.g. 2021 (preliminary) Tuva **0.364**, Khakassia **0.330**, Krasnoyarsk Krai **0.385** (24.rosstat.gov.ru PDFs; **search snippet only, UNVERIFIED**). **No Wikipedia list by subject was found.** This is the hardest gap.
- **The six ex-Ukrainian units:** population is in `EUB` (2001). GRP per head by oblast: the State Statistics Service of Ukraine and en.wikipedia *List of regions of Ukraine by GDP* (https://en.wikipedia.org/wiki/List_of_regions_of_Ukraine_by_GDP; found, **not opened**). Pre-2014 years avoid the war's distortion. Gini by oblast: **NOT FOUND (not searched).**

### 4.4 Choices the method leaves open (inputs to state, not rulings)

The developer's files do not settle these; each changes the split, so RS2–RS4 must state which variant each result uses.

- **S1 · What "Russia" is being split.** By `DR-23` the composition's "Russia" is pre-war Russia (`DRL` L618), and pre-war Ukraine has its own row (`UEIC` L96, ~5M). So:
  - **V1** (pre-war territory): the 83 federal subjects excluding Crimea and Sevastopol; the eastern-Ukraine slice is **not** in the pool (it belonged to pre-war Ukraine).
  - **V1c**: V1 plus Crimea and Sevastopol (Natural Earth carries them as Russian admin-1 units, `R09/sub` L84–85; their pre-war status is not stated in any file).
  - **V2** (the successors' own territory): V1c plus the six Ukrainian units.
- **S2 · Kaliningrad.** Part of pre-war Russia but a CIN member, not a Russia-split nation (`TRK` L149; `EUI` L31). Either it receives its slice as its own row (**K-in**) or it is left out and the rest renormalized (**K-out**). Its zone (+1) puts it outside every East Antarctic window, so it matters only for method (a) and for the Atlantic and Peninsula cities.
- **S3 · Which Karelia state.** **INIT** (Karelia = Karelia + Murmansk) or **C-15** (Republic of Karelia → Finland, Murmansk → Idelsk-Uralia). Under C-15 the Karelia Republic's slice goes to a non-Russian successor (Finland). The date of the change is open (`EUI` L42).
- **S4 · The meaningful-share threshold θ** (4.1 item 5): not given; bounded below by 2.5%.
- **S5 · Solar or official nation zones** (4.2).
- **S6 · Wraparound.** Whether a distance can be taken around the date line (e.g., Chukotka at −11/−12 against a city at −8). `UEIC` gives no rule; its only cross-date-line example is the gateway case (L32–33). Under any θ above 0.1%, Chukotka is not a meaningful share of Künnarantaiga (1.2: 0.1% of its urban proxy), so this matters only if θ is set very low.
- **S7 · Where each subject's people are.** Large subjects span several zones (Arkhangel'sk +2…+5, Sakha +7…+11, Krasnoyarsk +5…+8, 1.2). Assigning a subject to its territory centroid's zone is a territory proxy; assigning it to its main city's zone, or splitting it by its towns, is closer to the footprint rule.

---

## 5 · Derivation procedure for RS2 to RS4 (method only; no results)

**Notation.** *s* = a source unit (a pre-war federal subject, or one of the variant units in S1); *k* = a recipient successor (the 13 package nations, plus Kaliningrad under K-in, plus Finland's Karelia piece under C-15); *c* = a city; *R_c*, *H_c* = the city's former-Russia robots and humans (the brief's table).

**Inputs per source unit *s*:** population *P_s*; GRP per head *y_s*; Gini *G_s*; the solar zone *z_s* where its people live (S7); its recipient *k(s)* from `R09/sub` (under S3's C-15 variant, Karelia → Finland and Murmansk → Idelsk-Uralia). Use **one year for all units** wherever possible and state it.

**Step 1 · Effective pool per source unit.** Because `UEIC` gives no functional form (4.1 item 2), state the form used. The plain reading of L15 and L1057 (pool rises with income per head and falls with inequality) gives:

  *E_s = P_s × y_s × (1 − G_s)*  … (DERIVED convention)

National constants cancel in a within-Russia split, so no scale factor is needed. Note that *P_s × y_s* is simply the unit's total GRP, so *E_s* = total GRP × (1 − Gini). **Sensitivities to report beside it:** (i) *E_s = P_s × y_s* (no Gini); (ii) *E_s = P_s* (population only). If any unit lacks *G_s*, use (i) for all units rather than mixing forms, and say so.

**Step 2 · Pool per successor.** *W_k = Σ_{s: k(s)=k} E_s*. **Zone profile of *k*:** *q_k(z) = Σ_{s: k(s)=k, z_s=z} E_s ÷ W_k*. **Meaningful zones:** *Z_k(θ) = { z : q_k(z) ≥ θ }* (S4).

**Step 3 · Split (a), by effective pool alone:**

  *p_k^(a) = W_k ÷ Σ_j W_j*  (sum over all recipients in the chosen variant; sums to 100%)

Needs: *P_s*, *y_s*, *G_s* and the variant choices S1–S3. Does not need zones.

**Step 4 · Split (b), by effective pool within the city's proximity window.** For city *c* at solar zone *z_c*:

  *d_{k,c} = min over z ∈ Z_k(θ) of |z − z_c|*  (circular distance only if S6 allows it)
  *I_{k,c} = 1 if d_{k,c} ≤ 3, else 0*
  *p_{k,c}^(b) = W_k × I_{k,c} ÷ Σ_j W_j × I_{j,c}*

Needs everything in (a) plus *z_s*, θ and S5–S6. **If no recipient has *I_{k,c} = 1***, (b) is **undefined** for that city: the city's Russia share then exists only under the large-pool clause (4.1 item 4), and (a) is the only split. Report "no successor in window"; do not invent a fallback.
**Sub-variant (b-sub), reported beside (b):** count only the part of each successor's pool that lives inside the window, *W_{k,c} = Σ_{s: k(s)=k, |z_s − z_c| ≤ 3} E_s*, then normalize. This follows the footprint rule at unit level rather than nation level.

**Step 5 · Sensitivity sweep.** Recompute (b) at θ = 5%, 10% and 25%, and (a) and (b) under each S1 variant, K-in/K-out and INIT/C-15. Flag every successor whose share moves by more than 5 percentage points, or whose window membership flips, with the input that moved it (brief, RS2–RS4 item 5).

**Step 6 · Draft counts** (RS2–RS4 item 3). For robots and humans separately: *n_k = floor(R_c × p_k)*; give the remaining *R_c − Σ n_k* units one each to the largest fractional remainders (Hamilton's method; ties to the larger *W_k*). Counts are integers and sum exactly to *R_c* (and to *H_c*).

**Step 7 · Effective tier (informational, not ruled).** Absolute pool *Ê_k = 25M × p_k^(a)* (`UEIC` L76, scaled by the same variant). Insert *Ê_k* into that city's own ranking of other nations' pools (`UEIC` L65–110 and the city's own section), re-find the largest ratio gaps (L17, L1107), and apply the Notable rule (*d* ≤ 3 for a small pool, L30–31). "Small pool" has no number in the file (**NOT FOUND**), so state the cut used.

**What each formula needs, in one line:** (a) needs *P, y, G* and S1–S3. (b) and (b-sub) need those plus *z_s*, θ, S5 and S6. Counts need *p* and the brief's counts. Tiers need *Ê_k* and each city's ranking.

---

## Search log (exact strings; per LAW 0-R)

| # | String | Tool | Result |
|---|---|---|---|
| G1 | `коэффициент Джини по субъектам Российской Федерации 2021 таблица Росстат` | WebSearch | No all-subject table. Rosstat section https://www.rosstat.gov.ru/folder/13723 and https://rosstat.gov.ru/folder/313/document/282523 (a sixth Gini measure from 2021); single 2021 values for Tuva, Khakassia and Krasnoyarsk in 24.rosstat.gov.ru PDFs (snippet only). Rosstat hosts are TLS-blocked here (EO3 R1), so not opened. **Dead at the source.** |
| G2 | `список субъектов Российской Федерации по коэффициенту Джини википедия` | WebSearch | No Wikipedia list; academic papers (economicsjournal.spbu.ru; emjume.elpub.ru, 2017 Gini by region) not opened. **Open thread:** an academic or compendium table may carry all subjects. |
| G3 | `gross regional product per capita Ukraine by oblast 2013 Donetsk Luhansk Kharkiv Dnipropetrovsk Zaporizhzhia` | WebSearch | https://en.wikipedia.org/wiki/List_of_regions_of_Ukraine_by_GDP and Ukrstat named as sources; no 2013 values in snippets. Not opened (a named source is enough for RS1). |
| L1 | Population column in all 15 `subdivisions*.csv` copies | local count | 0 filled in every copy. |
| L2 | `grep` for an explicit Gini formula across the GDD | local | None. |
| L3 | Russia successor names across the novel repo, timeline repo and map files | local `grep -l` | Hits listed in sections 1–3; the timeline repo has no successor name, only "East Intermaria (formerly West Russia)". |

---

## FINAL · Summary (facts and method only; no design, no ruling, no recommendation)

**Successors (`R09`, 90 units):** Russia (24 units, Moscow, +2…+3) · Idelsk-Uralia (25; Nizhny Novgorod; +2…+5; **name provisional by conflicting sources**; gains Murmansk at C-15) · Donska-Kubania (9 incl. the Crimea Autonomous Zone; Rostov-on-Don; +2…+3; **name provisional by conflicting sources**) · Künnarantaiga (12; Vladivostok; +6…+12 and −11) · Siberia (11; Novosibirsk; +4…+8) · Tuva (Kyzyl; +6…+7) · Karelia (2; capital not set; +2…+3; a proto-country gone by C-15) · Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania (+3). Kaliningrad: pre-war Russia, now a CIN member (+1). **Population: NOT FOUND in any copy of `subdivisions.csv`.**

**First Interwar facts:** the Russia `03` and `04` folders are empty. Stated: the 2083 war and border redrawing; the INIT 2083 state; the undated C-15 change (Karelia → Finland, Murmansk → Idelsk-Uralia, timing open); the CIN ~2108–2118 (estimate); the undated Karelia population transfer into Idelsk-Uralia's north and Volga lands; the Tuva–Mongolia trade agreement. No population, GDP or Gini for any successor at any in-world date. Second Interwar canon names "East Intermaria (formerly West Russia)", extent open.

**Method:** effective pool = population × GRP per head × (1 − Gini) as a stated convention (the file gives no form); split (a) by pool; split (b) by pool among successors whose meaningful zones lie within ±3 of the city; (b-sub) at unit level; Hamilton rounding; tiers informational.

**Input gaps:** subject populations (Rosstat TLS-blocked; secondary sources exist); GRP per head (ru.wikipedia Rosstat series); **Gini by subject (no reachable all-subject table found)**; the Ukrainian units' GRP and Gini; θ; solar versus official zones (the source mixes them for Russia, 4.2); and the scope variants S1–S3.

**What is left:** RS2–RS4 (not started by this unit). Open threads: an all-subject Gini table (G2); the Kaliningrad population figure in `SURV` L309; money income per head as an alternative input.
