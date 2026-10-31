# Fort McMurdo — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (246 lines), the whole Pre-Trip (566 lines; the standard text compared line for line with Dumont d'Urville's and, through it, Denison's, and only the differing lines re-read), all 19 datasheets, the pass README and coverage ledger; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `FM-…`). Pass folder: `City_Development_Passes/Janbogo_Subnet/Fort_McMurdo/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run. Fort McMurdo's population did not change in the 2026-10-28 scenario or the 2026-09-05 extent ruling ("population UNCHANGED"), so every census, `09` and `16` number in the sheets is current.

**Verdict.** **Nothing blocks a run.** This is the cleanest city so far on numbers: the retention, the `09` and `16` rows, the per-nation table and the Census I/II sums all check. What is left: **(1)** the Pre-Trip is the builder version that still says the datasheets are "not yet built" in three places (all 19 exist); **(2)** the pass README's spec pointer is dead (flat pre-reorg path); **(3)** `Step_1_and_2` cites the COMNAP catalogue at pages 55 and 81 — the city's own entry is on **page 82**; **(4)** two sheet rows copy the spec's coldest-month and record-extreme lines, which the monthly table overrides; **(5)** the usual line shifts (the `16` list and the Ports, Airports and RelDB lines), the Precipitation row L159 missing from the Pre-Trip, and no extent rows in any sheet; **(6)** source: the spec's polar-night length is 116 days in one place and 118 in two others, and the Census II robots column is one short.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Janbogo subnet/Fort_McMurdo.md` (246 lines; `Step_-1` says 247, the builder's convention). Later-era headings **L209** (Connection to Concordia), **L217** (Current Status), **L227** (Legacy) = the Step −1 list; `## Notable Locations` **L191**, `## Notable Figures` **L202**; spec L3–9, L15–16, L18–38, L42–44, L48–73, L74–156, L86, L90–95, L99–102, L109–111, L159, L161, L167–180, L181, L204–205 land on what the sheets say | ✅ |
| Census Section A heading **L270**, entry L272–276 (tier table L274–276); Census I row **L507**; Census II row **L627** (both tagged "island cap") | ✅ unchanged |
| Census I **222,190 H / 223,120 R / 445,310**; Census II **173,548 H / 164,621 R / 338,169** — all sheets agree with the live rows; retention by hand: 338,169 ÷ 445,310 = **75.94%**, 173,548 ÷ 222,190 = **78.11%**, 164,621 ÷ 223,120 = **73.78%** (humans retain more than robots here; spread 4.33 pp toward humans) — `Step_0` and `Phase_2` right | ✅ |
| Extent file rows **L63** (the naive snapshot: Ross Island entire, 2,460 km², 181/km², "rural"), **L509** (DECLARED 2026-09-05: 55 and 45 km² → 8,097 and 8,578/km²; populations unchanged) and the other lines L14, L20, L25, L76, L697 | ✅ unchanged |
| `09` row **L69** (header L52): D 1.25 · humans 222,190 · residents 445,310 · required **119,774** · workforce **334,215** · **35.8%** (119,774 ÷ 334,215 = 35.84%); `16` Half B row **L250** (header L247): D 1.25 · workforce **334,215** (= 223,120 + 0.5 × 222,190) · base 41.5 · MAND 35.1 · FREE 23.4 (sum 100.0) · src C; `11`: no row, as the sheet says | ✅ |
| `READER/Fort_McMurdo.md` (16 lines; "READER station: McMurdo"; annual −16.2): the twelve monthly means equal the spec's Mean column; the sheets' L4–L8 cites land | ✅ |
| Stations L36, L45, L48, L69 (the four airstrips; the Country column is the builder, infrastructure only); Founding Register row **L69** (founders: miners, then clerics, bureaucrats and logistics coordinators from all over Tepenia; `DR-20`, `DR-21`; "Not founders: American") and L91, L94 — the Pre-Trip's §J already names them; Robot Physiology L409; Holidays L29, L164; Topics L310, L312; Sweep L95 and row L156; Theoretical L965, L984, L1036; Factions: `PostWar_Refugee` L109, L111, L113, `Second_Interwar` L157, L159, L163, `Hometown-based_Faction_Possibilities` L46; Geothermal L9, L23, L31, L154 | ✅ |
| Zero-hit claims re-run: Robot Religions (6 files), Meme Machine, True Believer, NMCI, Energy grid, Weapons, Weapon_Item_Catalog, National Economy, Ice-Cold folder (7 files), jobs folder (4 `.md`), `06_Worked_Example_Provenance.md` (431 lines, 0 hits), Arcanet (27 lines), `11` city row; `Test_Runs` tree: 1 file (`OBSERVATIONS_and_Methodology_Findings.md`); timeline repo `Worldspace/Characters/`: 587 `.md` files, 2 name the city (Calethina `README.md` L58, L60; `Formative_History.md` L5); `Robot_Universals` (timeline repo; 33 files, 1 hit: `24_Worked_Example_Arcanet_Etiquette/README.md` L28); universe-repo `Worldspace/Locations/`: 4 `.md` files, README L18 and L29 name it | ✅ |
| Pass README: local culture ✓, vision notes ✓, research log (does not exist yet) ✓, picks file ✓; every Pre-Trip source path exists; megasheet folder 7 entries; concept-art folder `.gitkeep` only | ✅ (the spec pointer: **A-03**) |
| `Step_3` picks: heading **L58**, picks **L59–61** (Zug [PRIMARY], Calgary, Geneva) — the Janbogo-subnet section sits before the Relung Panen insert, so XS-15 does not apply; `Step_6` section header lines L44, L56, L68, L80, L93, L106, L116, L128, L138, L153 all equal the live headings, and section 1 carries the Subnet column; `Step_9` carries item 5 | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). Highways L231 → **L232**. Airports L48, 52 → **L51, 55**. Ports L199, 240, 244, 246, 264 same; L519, 551, 713, 736, 756 → **L542, 574, 736, 759, 779**. CrossSub L181, 183, 185, 188–189, 205 same; L238 → **L239**. RelDB L30, 50, 105 same; L116, 219–220, 249, 405–407, 504, 520–521, 528 → **L127, 230–231, 260, 416–418, 515, 531–532, 539** (the city's entry is L230–L237). NatConn L101–102, 149, 249, 296–297 same; L414, 416, 421, 462–463, 578 → **L419, 421, 426, 467–468, 583**. `09` L69 same. `16`: row **L250** same, L137 same; the other 29 entries L327, 334, 1149, 1202, 1232, 1387, 1582, 2930, 2962, 2969, 2975–2976, 2978, 2985, 2989, 3003, 3051, 3053–3054, 3056, 3061, 3065, 3069, 3074, 3077, 3079, 3087, 3558, 3567 → **L330, 337, 1154, 1207, 1237, 1392, 1587, 2935, 2967, 2974, 2980–2981, 2983, 2990, 2994, 3008, 3056, 3058–3059, 3061, 3066, 3070, 3074, 3079, 3082, 3084, 3092, 3563, 3572**. Add `Precipitation_Falls_vs_Lands.md` **L159** (the city's row). Unchanged: census, extent, Stations, Holidays, Topics, Robot Physiology, Register. | live greps | Re-read each list live (SH-012) |
| **A-02** | WRONG | **"Datasheets not yet built" in three places** (2026-10-21 builder text): §C intro ("**not yet built** — November item N-5"), §I `DATASHEET-NOT-YET-BUILT(N-5)=20` (with `RESOLVE=118`), and a §J row. All 19 files exist. | `Datasheets/` | Reword all three |
| **A-03** | STALE | **Pass README spec pointer is dead:** `../../../Specs/Fort_McMurdo.md` (pre-reorg flat path); the file is `Specs/Janbogo subnet/Fort_McMurdo.md`. The other pointers resolve. | `ls` | Re-point (deferred README sweep) |
| **A-04** | NOTE | **Alias set** is the mechanical draft (McMurdo Station · Ross Island · Ross Sea) and never says Scott is a different place on the same island and the same peninsula (as Denison's and Dumont d'Urville's do for their neighbors). Found in shared files and not listed: **Hut Point** (Holidays L29–31 and L163–164), **Winter Quarters Bay** (Ports L542–543), **Mount Erebus**, **McMurdo Sound**, the **Dry Valleys**, **Cape Evans** and **Cape Royds** (spec L191–198). | grep | Confirm; add |
| **A-05** | NOTE | **Geothermal.** `Infrastructure/Geothermal_Heating.md` names the city (L9, L23, L31, L154, L196) and the spec's terrain finding rests on it (L21–28: "one of the six geothermal cities … their ground is bare"). The Pre-Trip's §J keeps the file out of every phase list (the runbook's registry names it, the per-phase table does not); `Phase_5` carries L9, L23, L31, L154 and omits L196 (a source URL). | spec L21–28 | DECIDE whether Phase 3 should read it for the six geothermal cities |
| **A-06** | NOTE | **Characters.** The timeline repo's tree (the one the Pre-Trip names) has 2 hits, both Calethina. The **GDD** `Worldspace/Characters/` tree names the city in more: Calethina's `Founding_Construction_Chain_UNMARKED.md` and `…_Play-by-Play.md`, `Personal_Questline_Summary.md`, `Questlines/Substrate_Transfer_and_Embodiment_Design.md`, `README.md`; `Dolls/Doll_Questline_Directory.md`; `Methodology/04_Story_Material.md`; the quick-capture seed `00d_…txt`. The spec's own L223 "unmarked background lore" paragraph is the same chain (Cradle / player-origin lore: ambient only, never a quest). | grep | Register; keep out of the pass inputs |
| **A-07** | NOTE | Picks are in `Step_3` but not in the Pre-Trip; no inspiration-research output exists yet (`Reference/Real-World/Inspiration_Place_Research/inputs/Fort_McMurdo.md` and `candidates/Fort_McMurdo.md` are there). | live | none |
| **A-08** | NOTE | Shared items SH-001 … SH-007, SH-010, SH-011 (composition file, extent snapshot). | live | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ · G3 `16` Half B ✅ · G4 Register row ✅ (named in §J, cited in the sheets) · G5 `Access type: SPUR` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ in `Step_3` · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ not in the sheets (**D-05**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals (222,190 + 223,120 = 445,310; 173,548 + 164,621 = 338,169); the 15 per-nation shares sum to **100.01%** (rounding); Census I robots **223,120**, Census I humans **222,190** and Census II humans **173,548** sum exactly; tier lists equal the table (2 / 5 / 8) and equal the census Section A entry; monthly means average **−16.24 °C** (stated −16.2); in every month Avg High > Mean > Avg Low and **Avg Low > Rec Low**; monthly precipitation sums to **213 mm** (stated 213); falls 213 − lands 81 = lost **132** (81 ÷ 213 = 38.0%); polar night Apr 26 → Aug 19 = **116 days**, midnight sun Oct 24 → Feb 19 = **119 days** (both recomputed from the physics at 77°51′S: polar night needs a solar declination of about +13°, midnight sun about −11.3°, which fit the stated dates); density 445,310 ÷ 55 = **8,097/km²** inside the 7,000–10,000 band.

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **Coldest month and record extremes contradict the monthly table.** L92 "coldest months (July/August) avg −28 °C; warmest month (January) avg −3 °C": the table's July and August means are **−24.9 / −25.2** (−28.4 and −29.5 are the Avg Low column), and the warmest mean is December (**−2.6**, January −2.7). L93 "record low ~−54 °C; record high ~+8 °C (rare summer peak)": the table's Rec columns give **−50.6 (Jul)** and **+10.8 (Dec)**. `Step_1_and_2` carries both lines. | spec L92–93 vs L117–128 |
| **S-02** | WRONG | **Polar-night length is 116 days at L108 and 118 at L141 and L148.** The dates (L108) give 116. L141 also compares the length with Janbogo's ("roughly six weeks longer"). | spec L108, L141, L148 |
| **S-03** | NOTE | **The Census II robots column sums to 164,620** (35,700 + 31,837 + 17,262 + 16,009 + 14,956 + 8,064 + 7,024 + 5,830 + 5,747 + 5,449 + 5,274 + 3,168 + 2,993 + 2,695 + 2,612), one short of the stated 164,621. A rounding residual of the de-stacking. | spec L16, L54–68 |
| **S-04** | STALE | Peer-relative statements, none carried by the sheets: L8 "Census II rank ~24th of ~30 cities" (the census row is numbered 23; the corpus is 38 cities now), L105 "13 of the 37 Tepenian cities are colder", L107 "full 37-city comparison", L141 (Janbogo), L82 (Scott, a neighbor — relation). | spec |
| **S-05** | NOTE | The monthly Daylight column shows Feb **24** and Aug **0**, while the stated ends are Feb 19 (midnight sun) and Aug 19 (polar night) — month averages should be slightly under 24 and above 0. | spec L117–128, L108–109 |
| **S-06** | NOTE | L15–16 and the census rows L507, L627 still tag the city "(island cap)", while the L18 block declares a 55 km² extent (8,097/km²) on Hut Point Peninsula and leaves the population unchanged. Dumont d'Urville's island-cap label was removed on the same date for a similar reason; this one stays. | spec L15–19; census L507, L627 |
| **S-07** | NOTE | L223 holds the Cradle / player-origin chain (a "discoverable-only" paragraph inside Current Status); later-era section, correctly outside the pass. Founding L161 and the Register agree. | spec L223 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings, census, header fields; **D-06** (247) |
| `Step_0` | ✅ census, retention (hand-checked); ❌ **D-05** (extent) |
| `Step_1_and_2` | ✅ climate rows, READER rows, Stations, `16` row, Register; ❌ **D-01** (COMNAP), **D-02** (rows 19–20), **D-05** |
| `Step_3` | ✅ picks L58–61 |
| `Step_5`, `Step_6`, `Step_7`, `Step_8`, `Step_9` | ✅ |
| `Step_10` | ❌ **D-04** (430 → 431) |
| `Phase_2` | ✅ census, retention, Register; duplicate rows **D-07** |
| `Phase_3` | ✅ spec ranges |
| `Phase_4` | ✅ `09` L52 / L69, `16` L250 |
| `Phase_5` | ❌ **D-03** (lines) |
| `Phase_6` | NOTE **D-08** |
| `Phase_7` | ❌ **D-03** (`16` list); NOTE **D-09** |
| `Phase_8` | ✅ (0-hit term counts confirmed against the spec) |
| `Phase_9` | ✅ robot share 50.10% (223,120 ÷ 445,310 = 50.103%), `Robot_Universals` hit |
| `Phase_10` | ✅ 587 files, 2 hits, spec L202–205; NOTE **A-06** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | WRONG | `Step_1_and_2` · COMNAP row | "pages **55, 81**". The catalogue's own entry for McMurdo Station is on **page 82** (heading "MCMURDO"; "built on the bare volcanic rock of Hut Point"); the index row is on **page 8** ("McMurdo 77°50′53″S 166°40′06″E"). Page 55 is Scott Base's entry (it names both bases), page 81 is another station's distance sentence, page 6 the generic environmental-domain list. | Replace with 8 and 82 (note 55 as the neighbor's entry) |
| **D-02** | WRONG | `Step_1_and_2` · temperature-range and record-extreme rows | Copy spec L92–93 (−28 / −3; −54 / +8). The table gives: July mean −24.9, August −25.2, warmest mean December −2.6; Rec Low **−50.6 (Jul)**, Rec High **+10.8 (Dec)**. | Replace from the table; note S-01 |
| **D-03** | STALE | `Phase_5`; `Phase_7` | Highways **L231 → L232**; Airports **L48, L52 → L51, L55**; Ports **L519 → L542, L551 → L574, L713 → L736, L736 → L759, L756 → L779**; RelDB entry **L219–L231 → L230–L242** and entry lines **L220–L226 → L231–L237**; CrossSub **L238 → L239**; NatConn **L414, L416, L421, L462–463, L578 → L419, L421, L426, L467–468, L583**. `Phase_7`'s `16` "30 line(s)" list: the +3 / +5 shifts of A-01. | Re-point |
| **D-04** | STALE | `Step_10` | "`06_Worked_Example_Provenance.md` (430 lines)" — **431** (zero hits re-run). | Re-count (SH-009) |
| **D-05** | GAP | `Step_0`, `Step_1_and_2` | No extent rows: spec **L18–38** (declared ~55 km², 8,097/km², rock kept bare by geothermal heat, Hut Point Peninsula 104–157 km² shared with Scott, populations unchanged) and the extent file's **L63** (snapshot: 445,310 on Ross Island's 2,460 km², 181/km²), **L509** (the declaration: 55 and 45 km² → 8,097 and 8,578/km²). `Step_0` says the extent band is "not included here". The Pre-Trip's `Step 0` read list names all of them. | Add, labelled the 2026-09-05 snapshot (SH-011) |
| **D-06** | STALE | counts | "247 lines" spec (246), "293-line" Meme Machine (292), "378-line" True Believer (377), "246-line" NMCI (245), "74-line" Weapons (73), "36-line" Enneagram Index (35), "28-line" Arcanet (27), "146-line" Energy (145) — builder convention, SH-009. | per SH-009 |
| **D-07** | NOTE | `Phase_2` | Rows 4–5 and 6–7 are exact duplicates (the "(founding wave) — no date" rows). | Delete the duplicates |
| **D-08** | NOTE | `Phase_6` · Holidays rows | The two quotes stop mid-sentence. The established observance is L29–31 ("Hut Point remembrance in Scott and Fort McMurdo — residents lay candles, flowers, and personal tokens at Hut Point, Scott's most sacred civic location …"); L163–164 is one open question. | Re-point to L29–31 and L163–164 |
| **D-09** | NOTE | `Phase_7` · Factions box | The box says `City_Origin_Factions_Second_Interwar.md` is "an explicitly comparative grouping — do not open". This city has its own single-city section there (**L157–165**, "Cities: Fort McMurdo") alongside the comparative groupings; the sheet treats both alike. | DECIDE (whether the single-city section may be read) |

### 2d. DECIDE items (collected)
1. **S-01 / S-02** Approve source edits in the spec: L92–93 from the table; the polar-night length (116 vs 118).
2. **A-05** Whether `Geothermal_Heating.md` is a named input for the six geothermal cities.
3. **D-09** Whether this city's own faction section may be read in the pass.
4. **S-06** Whether the "(island cap)" label stays beside a declared 55 km² extent.
