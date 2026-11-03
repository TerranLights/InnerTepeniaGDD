# Relung Panen, Unit R1 (Power): research on indoor-farm electricity demand, scale, polar precedents, transmission, local wind and solar, and alternatives (2026-11-02)

**Scope.** Real-world facts only, gathered for the Relung Panen open items (stacked indoor hydroponics at the Bunger Hills oasis, a grid line along the road, no conventional port). No recommendation, no design, no ranking. Technology reference is the 2020s with modest extrapolation. Labels: **SOURCED** (read at the source in this session), **DERIVED** (my arithmetic on stated inputs, working shown), **UNVERIFIED** (seen only in a search snippet, recalled, or inferred), **NOT FOUND** (looked for, queries in the log). Figures marked "carried from round 1" were read at the source in the 2026-10-25 files (soil F and soil E) and were not re-opened here. Numbers in quotation marks use the source's own wording where short.

**Started:** 2026-11-02 16:59. **Finished:** 2026-11-02 (time stamped at the end of this file).

**Read first (as the brief required):** `Relung_Panen_Soil_Research_2026-10-25_F_Growing_Without_Soil_Precedents.md`, `Relung_Panen_Soil_Research_2026-10-25_E_Oasis_Ground_Water_and_Light.md`, `Relung_Panen_Oasis_F_Ice_Front_and_Haul_2026-10-29.md`. Round 1 already held: EDEN ISS (2018) at about 205 kWh/kg (plant hardware) and 256 kWh/kg (whole facility), the South Pole chamber at 281 kWh/day, a lighting-only scale-up of 0.7 to 1.6 GW per 100,000 people, the 1956 to 1958 Oasis station climate table, and no energy study or wind-resource number for the oasis.

## PROGRESS

- [x] Q1 Electricity demand of indoor farming (kWh/kg, kWh/m², LED efficacy, split, cold-air effect). Staples and tomatoes are thin (see FINAL).
- [x] Q2 Scale: average megawatts for 100,000 / 750,000 / 1,000,000 people, compared with real farm sizes.
- [x] Q3 Antarctic and polar indoor-growing precedents (EDEN ISS and South Pole done in depth; other stations: power per kg NOT FOUND).
- [x] Q4 Transmission precedents (Arctic and subarctic lines, HVDC, icing failures, costs). Antarctic power line longer than a few kilometers: NOT FOUND.
- [ ] Q5 Local resources: PARTLY done. Wind and solar for the oasis from round-1 station records plus a reanalysis computation done here, and station wind-turbine experience done; a measured wind-resource study for the oasis itself, and wind statistics from the post-2014 automatic stations, are still NOT FOUND, so this item is not ticked.
- [x] Q6 Alternatives as precedents (reactors, geothermal, diesel logistics). Local geothermal heat-flux value and station liters per person NOT FOUND.

---

## 1. Q1: Electricity demand of indoor farming

### 1.1 LED efficacy (µmol of photosynthetic photons per joule of electricity)
- **SOURCED** (Kusuma, Pattison, Bugbee 2020, *Horticulture Research* 7:56, opened this session): "In 2014, the best LED fixtures had an efficacy of 1.7 µmol J−1." Independently tested fixtures now reach "2.5 to 2.8 µmol J−1 for white + red fixtures and 3 µmol J−1 for blue + red fixtures"; typical current values are "2–3 µmol J−1." Calculated (not measured) potential with the best LEDs is 3.4 (white + red) and 4.1 (blue + red) µmol/J; protection against water and humidity cuts these projected limits by about 10%.
- **UNVERIFIED** (search snippets only; the MSU Extension PDFs returned empty): a 2024 MSU update says the Design Lights Consortium horticulture list had a minimum of 1.9 µmol/J, about half of 600+ products at 2.5 or more, and about 6% at 3.0 or more. One DLC listing was reported at 2.71 µmol/J. A rebate-industry blog claims a 2.5 µmol/J minimum since 18 April 2025; this conflicts with the MSU figure and was not checked against DLC.
- **SOURCED** (Lovat, Noor, Milo 2025, below): a light-emitting diode efficiency of "≈50%" is used as the electricity-to-light conversion in their whole-farm estimate, taken from Graamans et al. 2018. Section 2 uses the efficacy figures above in its lighting arithmetic.

### 1.2 Electricity per kg of produce
| Source | Crop / system | Figure | Status |
|---|---|---|---|
| Ceccanti, Bischi, Desideri, Baccioli (Univ. of Pisa), arXiv 2507.18419 | Lettuce, 162 modeled scenarios (Norway/Trondheim, Shanghai, Dubai) | Specific energy consumption **7.8 to 23.8 kWh/kg**; lighting plus the cooling needed to remove its heat is "over 95%" of the total. The paper's introduction cites a literature range of **3.2 to 20 kWh/kg** and, from a review, "around 70%" of total use for lighting and "approximately 28%" for HVACD | SOURCED (preprint; model, not metered) |
| Karpe et al. preprint (round 1, file F) | Lettuce, LCA review of vertical-farm case studies | median **18 kWh/kg** (range 10 to 39); 1,012 kWh per m² of cultivation area per year; 2,225 kWh per m² of floor area per year | carried from round 1 (non-peer-reviewed) |
| Lovat, Noor, Milo 2025, *Plant Physiology* 198(3):kiaf056 | Lettuce; and dry plant matter in general | "equaling 10 kWh of electricity per kg of lettuce" (a commercial farm, citing Martin et al. 2023); **≈250 kWh/kg of dry plant matter**; energy-to-food efficiency of vertical farms about 1% (0.4 to 1.9% over 19 studies), 2% used as optimistic, about 10% as the stated upper bound for the future; maximum for C3 crops in full sunlight about 4% | SOURCED (peer reviewed) |
| Hannah Ritchie, "Vertical farming" (Sustainability by Numbers) | Lettuce | about **12.5 kWh/kg**, plausible 10 to 20, lighting "60% to 80%"; a CEA census average of about 38 kWh/kg; all US lettuce indoors "about 42 TWh/year" (her calculation) | SOURCED (secondary summary) |
| Graamans et al. 2018, *Agricultural Systems* 160:31-43 | Lettuce, plant factory vs greenhouses | purchased electricity per kg **dry** weight: plant factory about 247 kWh; greenhouses about 70 (Netherlands), 111 (UAE), 182 and 211 (Sweden, with and without added lighting) | UNVERIFIED (search-tool abstract text only; the IDEAS abstract page and the full text did not show the numbers) |
| Zabel et al. 2022 (EDEN ISS, Neumayer III, Antarctica) | Salad, vegetables, herbs, 2018 | **≈205 kWh/kg** edible food for the plant-cultivation hardware (55,055 kWh for 268 kg food, 517 kg total biomass); **≈256 kWh/kg** if the common equipment is included (68,516 kWh; DERIVED, 68,516 / 268) | SOURCED, opened in full |
| Giacomelli (Univ. of Arizona), slides, 26 Sept 2012 | South Pole Food Growth Chamber, polyculture, not optimized | "10 – 13 g per kWh" of fresh edible biomass, energy including lighting, environmental control, monitoring and services; "Edible biomass from SPFGC 10 g/kWh vs. 13 g/kWh LGH" (LGH = a prototype lunar greenhouse) | SOURCED. **DERIVED:** 10 g/kWh = **100 kWh/kg**, which matches the round-1 computation (281 kWh/day / 2.8 kg/day = 100) and does not match the 22.8 kWh/kg that Zabel 2022 quotes for the same chamber. The same slide also lists "24 ± 4 g biomass (ww) per kWh" (edible plus non-edible) on a block with 100.3 kWh/day, which appears to belong to the lunar prototype, not the Pole chamber (reading of the slide layout, UNVERIFIED) |

### 1.3 Staple crops indoors (potatoes, wheat, rice)
- **Wheat, lighting only, from a measured experiment** (round 1, file F, Asseng et al. 2020 *PNAS*): 14 t/ha per harvest, 5 harvests per year, 1,400 µmol/m²/s for 20 h/day; computed at 2.7 µmol/J then as about 10.4 kWh/m²/day, about **540 kWh/kg grain** for lighting alone (carried from round 1; an optimistic bound, excludes climate control).
- **SOURCED** (Lovat et al. 2025): about 250 kWh per kg of dry plant matter at 2% efficiency; at 1% the same logic gives about twice that and at 10% about one fifth (DERIVED by proportion). The paper does not give separate figures for wheat, rice, potato or soybean. "Wheat is close to one-half" harvest index; lettuce "close to 1."
- **UNVERIFIED** (search snippets of an MDPI review, *Sustainability* 17(7):3259, which returned 403, citing Kobayashi et al.): potatoes "at least 62 kWh/kg," wheat "at least 435 kWh/kg," lettuce 7 kWh/kg.
- **UNVERIFIED** (a Substack post, "decodingtech"): wheat about 113 kWh/kg (85 for the minimum energy of photosynthesis plus 28 for climate control), wheat's own energy content 4.23 kWh/kg.
- **SOURCED** (Ritchie's page, quoting Pattison et al. 2018, *Nature* 563:493): lighting alone would cost about 100 times the market price of wheat or rice at $0.10/kWh. The *Nature* paper itself is paywalled and was not read. Ceccanti et al. say that "even with 100% efficient LED systems, the cultivation of staple crops like rice and wheat in vertical farms remains economically unfeasible," citing that line of work.
- **Rice: NOT FOUND** (no indoor kWh/kg located).
- **Tomatoes indoors under fully artificial light: NOT FOUND** as kWh/kg (a pilot cherry-tomato study in Athens gives per-plant yields and energy differences only). Nearest figures, both greenhouses with LED lighting: Tromsø year-round about 9.2 kWh/kg (round 1, DERIVED from Naseer et al. 2022 inputs); all Finnish greenhouses about 17.8 kWh/kg (round 1).

### 1.4 Energy per m² of growing area
- **EDEN ISS, 2018 (SOURCED):** 5,481 kWh per m² of cultivation area over 286 days; 19.2 kWh/m²/day (DERIVED check: 5,481 / 286 = 19.2); of that, illumination 5.7 kWh/m²/day. Stand-alone container, partly resistive heating.
- **South Pole chamber (SOURCED, Zabel 2022):** 12.8 kWh/m²/day total, 9.5 kWh/m²/day for lighting (high-pressure sodium lamps).
- **Manitoba pilot vertical farm (SOURCED, University of Manitoba thesis abstract):** 517.2 to 773 kWh per m² per year of floor area measured, against 850 to 1,150 reported in the literature for other regions.
- **Karpe median:** 1,012 kWh/m² of cultivation area per year, lettuce (carried from round 1).
- **Greenhouses for comparison (round 1):** all Finnish greenhouses about 480 kWh/m²/year, all energy; Tromsø year-round tomatoes 1,006 kWh/m² of electricity plus 166 of gas.

### 1.5 How demand splits
- **EDEN ISS 2018 (SOURCED, Zabel 2022 Table 2):** atmosphere management (temperature, humidity, CO₂, air flow, dehumidifier) 23,040 kWh = **33%**; illumination 19,033 kWh = **28%**; common equipment (room heaters, water boiler, room lights) 13,461 kWh = **20%**; thermal control (removes heat, supplies cooling fluid to the dehumidifier) 7,551 kWh = **11%**; control and data handling 4,268 kWh = **6%**; nutrient delivery (eight high-pressure mist pumps) 1,163 kWh = **2%**. Average power 11.23 kW during the 17-hour photoperiod, 8.21 kW in the 7-hour dark period.
- **Manitoba pilot (SOURCED):** lighting 46 to 75% of total energy, HVAC 22 to 52%.
- **Ceccanti et al. (SOURCED):** lighting and the cooling to remove its heat together exceed 95% of consumption in insulated scenarios. Higher light intensity raises cooling load (180% and 360% more when intensity goes from 100 to 250 and 400 µmol/m²/s) and lowers dehumidification load (67% and 77% less) because the cooling coil itself removes moisture.
- **A US industry source (SOURCED, Canary Media quoting a former Plenty energy manager):** lighting about 70% of a vertical farm's electricity.
- **Pumping:** 2% in EDEN ISS (mist pumps); no other measured pumping share found.

### 1.6 Effect of cold outdoor air on cooling versus heating
- **EDEN ISS (SOURCED):** in mid-May one of two roof "free cooler" fans failed; the other was shut down June to September "because the low temperatures of the Antarctic environment were enough to cool the cooling fluid without the need for forced convection by the fans." Without that shutdown demand in June to October would have been "around 900 kWh per month higher." Demand still rose June to October "most likely associated with the dropping temperatures during the winter months and the corresponding need for additional electrical heating"; the room heaters in the common equipment rose steadily from May to October. Zabel also writes that the share of demand caused by the Antarctic environment "cannot clearly be determined" (round 1 quote).
- **Manitoba pilot (SOURCED):** winter operation used less energy than fall "because the facility did not need cooling"; the model predicted lighting well and heating less well.
- **Ceccanti et al. (SOURCED):** in an insulated farm, the same plant held at the same indoor setpoints used 2.55% (Shanghai) and 5.66% (Dubai) more specific energy than in Trondheim, "primarily due to... the cooling load [being] the second largest energy demand," with chiller efficiency better in cold air. Raising the indoor setpoint from 20 to 28 °C raised heating demand 50% in the cold climate. Removing insulation raised specific energy by 40 to 70% at low light intensity in the cold climate, and by up to 5% less at high intensity (heat losses offset cooling).
- **Result in short (DERIVED from the three sources):** cold outdoor air replaces compressor cooling with free cooling and lets heat from the lamps warm the interior; the penalty is resistive or heat-pump heating in the dark period and for the building shell, which in the one Antarctic measurement was 20% of the total.

---

## 2. Q2: Scale, average megawatts for N people

### 2.1 Inputs
- Food energy: 2,500 kcal/person/day (the basis used by NASA's Wheeler for the 50 m² per person figure; carried from round 1). 2,500 kcal = 10.47 MJ = **2.908 kWh/day** (DERIVED, 2,500 × 4.1868 kJ / 3,600).
- Crop area per person: **50 m²** for dietary calories under electric light (Wheeler, NASA, carried from round 1: "about 50 m2 would be required for dietary calories (2500 kcal person-1 d-1)").
- Per-person food mass is not a published single number in the sources opened. DERIVED for wheat only, assuming 3,400 kcal/kg of grain (recalled, **UNVERIFIED**): 268 kg grain per person per year (2,500 × 365 / 3,400). The Our World in Data/FAO per-person supply pages did not return a figure (see log).

### 2.2 Computed average power
Working (all DERIVED): average kW per person × N. Per-person values are in the second column. Round-1 Section 2.2.8 covered lighting only; the rows below add routes from this session.

| Basis (per person) | kW avg per person | 100,000 | 750,000 | 1,000,000 |
|---|---|---|---|---|
| A. Efficiency route, Lovat et al. 2025: 2.908 kWh food energy per day ÷ η ÷ 24 h, η = 10% (their stated future upper bound) | 1.21 | 121 MW | 909 MW | 1,211 MW |
| A. η = 2% (their "optimistic" current value) | 6.06 | 606 MW | 4,543 MW | 6,057 MW |
| A. η = 1% (their measured central value) | 12.1 | 1,211 MW | 9,086 MW | 12,115 MW |
| B. 50 m² × 3.4 to 7.4 kWh/m²/day, lighting only, from LED efficacy and PPFD (round 1) | 7.1 to 15.4 | 708 to 1,542 MW | 5,312 to 11,562 MW | 7,083 to 15,417 MW |
| C. 50 m² × 12.8 kWh/m²/day (South Pole chamber, whole facility, salad crops) | 26.7 | 2,667 MW | 20,000 MW | 26,667 MW |
| D. 50 m² × 19.2 kWh/m²/day (EDEN ISS, whole facility, salad crops, Antarctic container) | 40.0 | 4,000 MW | 30,000 MW | 40,000 MW |
| E. 50 m² × 1,012 kWh/m²/year (Karpe median, lettuce) | 5.8 | 578 MW | 4,332 MW | 5,776 MW |
| F. 250 kWh/kg dry matter × 0.625 kg dry matter/day (2,500 kcal at an assumed 4 kcal/g) | 6.51 | 651 MW | 4,883 MW | 6,510 MW |
| G. Wheat, lighting only, Asseng measured yield: 268 kg grain/year ÷ 7 kg/m²/year per layer = 38.3 m² × 10.4 kWh/m²/day (assumes 3,400 kcal/kg) | 16.6 | 1,661 MW | 12,461 MW | 16,614 MW |
| H. Wheat at 435 kWh/kg (UNVERIFIED snippet) × 0.735 kg/day | 13.3 | 1,333 MW | 9,995 MW | 13,327 MW |
| I. Potato at 62 kWh/kg (UNVERIFIED snippet) × 3.25 kg/day (assumes 770 kcal/kg, recalled) | 8.4 | 839 MW | 6,291 MW | 8,387 MW |

Annual energy at 1,000,000 people runs from 10.6 TWh/year (row A at 10%) to 350 TWh/year (row D). Rows A to B cluster at roughly **6 to 16 kW per person** (about 0.6 to 1.5 GW per 100,000 people; about 5 to 12 GW per 750,000 to 1,000,000 people) for staple-calorie diets under current LED technology; rows C and D, which rest on salad crops in Antarctic test rigs, are higher because those rigs are small and include heating and other overhead.

**Caveats that change the figures (facts, not advice):** (i) Row A's efficiency definition is Lovat's; the paper's text read here does not say whether climate control is inside it. (ii) Rows B, G, H, I are lighting-only or crop-only and leave out harvest, processing, storage and any animal protein. (iii) Rows C and D include a heated, stand-alone, very small facility; large buildings have a smaller envelope-to-volume ratio. (iv) The calorie-per-kg values for wheat and potato are recalled and UNVERIFIED.

### 2.3 Check against real vertical-farm sizes
- **Bustanica (Emirates Crop One, Dubai), SOURCED (NZ Herald):** "a three-level Bustanica, which has a floor area of 3ha"; "27 rooms that are 550sqm and are stacked six shelves high"; "about three tonnes of green vegetables are being harvested each day." Energy: the article says "it is energy-hungry" and gives no figure; a search summary said the company declined to disclose energy use (UNVERIFIED). **DERIVED:** 3 t/day = 1,095 t/year; at 10 to 20 kWh/kg that is 11 to 22 GWh/year, or **1.25 to 2.5 MW** average. The measured load is **NOT FOUND**.
- **Nordic Harvest (Taastrup, Denmark), UNVERIFIED (news reports):** about 7,000 m² total building, "almost 1,000 tonnes annually" at full capacity, power purchased with wind certificates; no consumption published. DERIVED at 10 to 20 kWh/kg: 1.1 to 2.3 MW average.
- **Jones Food Company, UK, UNVERIFIED (news reports):** a Lydney, Gloucestershire site described as 148,000 sq ft of growing space, projected 1,000 t/year at announcement, 550 t/year in a later report; no megawatt figure published.
- **Plenty (Richmond, Virginia), SOURCED (Greater Richmond Partnership page):** the state development agency asked for sites of "at least 25 acres with 15+ megawatts of power" (a site-search request, not a stated load); the campus is "Designed to grow more than 4 million pounds annually" of strawberries. DERIVED, only to show scale: if all 15 MW were used continuously, 15 MW × 8,760 h = 131 GWh over 1.81 million kg is about 72 kWh/kg; the actual load was not published.
- **Fifth Season (Pittsburgh), SOURCED (Canary Media):** a 1.75 MW microgrid (160 kW solar, 200 kW batteries, 1.2 MW natural-gas generator) "doesn't supply the site's total electricity needs"; total load not stated.
- **Largest-farm claims:** Guinness lists AeroFarms' Newark farm as largest by growing capacity, about 907,000 kg (2 million lb) of greens per year (UNVERIFIED, snippet). Bustanica is reported as largest by floor area.
- **Comparison (DERIVED):** one million people on row A at 2% (6.06 GW) is about 2,400 to 4,800 times Bustanica's estimated 1.25 to 2.5 MW; the same row exceeds the 4.8 GW average implied by Ritchie's 42 TWh/year for all US lettuce grown indoors (42,000 GWh / 8,760 h = 4.79 GW).
- **Antarctic yardsticks:** McMurdo's whole electrical load is about 15 GWh/year (NREL/Meridian slides, SOURCED), an average of 1.7 MW (DERIVED). The Australian program's electricity use per person is reported as 46,100 to 51,390 kWh per year, 5.3 to 5.9 kW average (UNVERIFIED, a search summary of the State of Environment report; the report pages returned errors). 

### 2.4 Is this real anywhere, or only a calculation?
- **What the sources say (SOURCED):** Ritchie: vertical farms are unlikely to supply calories "in any meaningful way," meaning more than a few percent. Lovat et al.: electricity at about 250 kWh/kg of dry matter costs about $10/kg at 4 cents/kWh, "not competitive with" bulk cereals. Ceccanti et al.: staples remain "economically unfeasible" even with 100% efficient LEDs (citing other work). Bamsey et al. 2015 and the EDEN ISS and Pole data (round 1): operating Antarctic indoor farms serve crews of 10 to 50 with salad-scale output (EDEN ISS 315 kg in 2021, about 110 g per crew member per day).
- **Closed-system test beds that fed people (round 1, SOURCED there):** BIOS-3, 63 m² of growing area, about 400 kW, three crew, 50 to 70% of the diet, up to 180 days; Lunar Palace 1, 55% of food regenerated, 105 days; Biosphere 2 (sunlit, soil), 2,000 m² for eight people, about 80% of nutrition for two years.
- **Hundreds of thousands of people fed entirely this way:** **NOT FOUND** in any source opened. The largest operating farms found harvest on the order of 1,000 t/year of leafy greens (Bustanica, Nordic Harvest, Jones), which is an order of magnitude below the food mass of a city (at 268 kg of grain per person per year, 1,000 t is the grain for about 3,700 people; DERIVED on the recalled caloric density).

---

## 3. Q3: Antarctic and polar indoor-growing precedents

### 3.1 EDEN ISS (Neumayer III, 70°S), SOURCED (Zabel et al. 2022 opened in full; yields from round 1)
- Two 20-foot containers, 12.5 m² of cultivation area, 42 fluid-cooled LED fixtures, aeroponic mist roots, 400 m from the station, power by cable from the station grid. The station's diesel combined heat-and-power plants: four units of up to 150 kW electric each (up to three running), waste heat warms the station, a wind turbine adds up to 30 kW.
- 2018: 68,516 kWh from February to November (286 days) = 9.98 kW average (DERIVED, 68,516 / (286 × 24)); 268 kg edible food; 205 kWh/kg (hardware) or 256 kWh/kg (all); 17-hour photoperiod; 19.2 kWh/m²/day. 2019: 106.5 kg (June to November). 2021: 315 kg in 319 days; 0.99 kg/day. Crew time 3 to 4 hours per day in 2018; 6.31 crew-hours per kg in 2019 (all round 1).
- The paper states "no legumes and no grains" were grown.

### 3.2 South Pole Food Growth Chamber, SOURCED (Giacomelli slides; round 1)
- About 22.7 m² of cultivation area, high-pressure sodium lamps, 281 kWh/day, 2.8 kg edible per day (2006), 12.8 kWh/m²/day, about 100 kWh/kg edible (10 g/kWh). The slide gives labor of "35.9 min day-1" for the prototype lunar greenhouse block (not stated for the Pole chamber).
- Search summary only (UNVERIFIED): a plant growth room "listed at 12 kW of lighting." Anything newer than 2013 (a replacement chamber, 2023 to 2024 data): **NOT FOUND**.

### 3.3 Other Antarctic stations
- McMurdo (hydroponics 1989 to 2011), Casey, Davis, Mawson, Great Wall (8.5 kW maximum electrical load, planned 60 kg/month), Zhongshan, King Sejong (more than 1 kg/day), Syowa, Vostok (multi-level "panoponics," cucumbers 100 kg/m² etc.): yields from round 1; **power per kg NOT FOUND** for all of them (searched again this session for Zhongshan, Great Wall, Maitri, Bharati: nothing new).
- A search snippet attributing "12.8 kWh/m²" and "22.77 m²" to Vostok actually carries the South Pole chamber's numbers; treat as a misattribution (UNVERIFIED reading).

### 3.4 Arctic and subarctic
- Svalbard (Polar Permaculture), Greenland (Nuuk "Greenlandic Greenhouse"; Narsaq sheep farms), Kotzebue (Arctic Greens), Inuvik, Gjoa Haven (Naurvik: three then five retrofitted shipping containers on wind and solar, "about three-quarters powered by renewable electricity even during the Arctic night"): existence and renewables share found; **kWh and kg NOT FOUND** for each (searched again for Naurvik and Nuuk). Nuuk's grid is hydropower from Buksefjord: 255 GWh in 2020 (UNVERIFIED snippet). Greenland imports about 3,600 t of vegetables a year for about 56,000 people (UNVERIFIED, Norden nominee page snippet).
- Yakutsk (Sayuri), Friðheimar, Icelandic growers, Finland, Tromsø: round 1.

---

## 4. Q4: Transmission precedents

### 4.1 Longest and most relevant lines in cold regions
| Line | Facts | Status |
|---|---|---|
| **Labrador-Island Link** (Labrador to Newfoundland, HVDC) | **1,100 km, 900 MW**, commissioned 14 April 2023 after "nine years of planning, delays and billions in cost overruns." Voltage not stated on the page read | SOURCED (Renewable Energy World) |
| Labrador-Island Link, cold-weather record | In a search summary of CBC and N.L. Hydro items (the CBC pages returned 403 and the Hydro page an SSL error, so UNVERIFIED): rime ice damaged 8 towers in southern Labrador in January 2021 and more in February 2021; failures in winter 2022-23 attributed to conductor "galloping" with a $28 million, four-year fix, with about 9,000 pieces of equipment to be installed on 161 spans; ice "three inches thick in places" damaged 11 towers in a later event with no power interruption | UNVERIFIED |
| **Bipole III** (Manitoba, HVDC) | 1,384 km, two 2,000 MW converter stations, in service 2018, final cost about C$4.6 to 5.0 billion depending on the source | UNVERIFIED (trade-press and policy snippets disagree; T&D World and CCPA pages not opened) |
| **Alaska Intertie** (Willow to Healy) | 170 miles, "345 kilovolt" construction, operated at 138 kV, built mid-1980s, $124 million of state appropriations; no outage data on the page | SOURCED (Alaska Energy Authority) |
| **Pevek to Bilibino, Chukotka** | Replacement of a 1960 wooden-pole 110 kV line; two single-circuit 110 kV lines totaling 986.9 km (first stage 490.59 km, commissioning 2023 in the government decree; 2018 article said "almost 491 km," commissioning 2020, "about 18.42 billion rubles, including VAT") | SOURCED for the cost and length in the 19 January 2018 East Russia article; the 986.9 km total and the decree figures are UNVERIFIED (search snippets) |
| Bilibino to Peschanka (for the Baimsky mine) | 110 kV overhead line, built 2020; length not stated | SOURCED (partial) |
| **Kivalliq Hydro-Fibre Link** (Manitoba to Nunavut, proposed) | 1,200 km high-voltage line to Arviat, Whale Cove, Rankin Inlet, Chesterfield Inlet, Baker Lake and two mines; estimate C$1.2 billion (2019) rising to C$3.2 billion (reported June 2025); work started 2018, completion estimated 2032; route over continuous permafrost per a study summary. Not built | SOURCED (Nunatsiaq News) for length, cost, dates; permafrost line UNVERIFIED |
| Norway: Balsfjord-Skaidi-Hammerfest 420 kV | Standard steel portal towers, prefabricated foundations; project pages only | UNVERIFIED (search summaries); design ice loads **NOT FOUND** |
| Iceland (Landsnet) | December 2019 storm in northern Iceland: "40 towers failed," estimated outage cost $40 million; a tower on a main line from the largest hydropower plant collapsed on 17 December 2019 from a defect "possibly worsened by line galloping"; sensors that harvest line power ran at −30 °C with 99.9% uptime | SOURCED (POWER magazine) |

### 4.2 Voltage, AC versus DC at 300 to 400 km
- **SOURCED** (Wikipedia HVDC article, first 100,000 characters): break-even distance between AC and DC "perhaps 600–800 km" for overhead lines and "about 50 km" for submarine cables; HVDC losses "quoted at 3.5% per 1,000 km," against 6.7% for AC at the same voltage. **DERIVED:** at 3.5% per 1,000 km, 300 to 400 km loses 1.05 to 1.4% in the line, before converter-station losses (not found).
- **SOURCED** (Stantec/Areva/PDC report for Alberta, 2009): overhead HVAC "provide[s] a good balance from a cost and technical perspective"; HVDC has "lower overall cost compared to a HVAC transmission system for longer transmission distances"; converter stations are the high-cost item. Costs there are relative only, for 50, 100, 300 and 600 km at 500 kV.
- Real HVDC lines in cold regions (Bipole III, Labrador-Island Link) are 1,100 to 1,400 km and 900 to 2,000 MW. A 300 to 400 km Antarctic line has **no** precedent in these sources.
- A search summary (UNVERIFIED) of a hackaday comment thread said a very long line to the South Pole would need DC; the article itself says nothing about a power line.

### 4.3 Ice loading, blizzard and icing failures
- **SOURCED** (Wikipedia, 1998 North American ice storm, temperate-subarctic, for the failure mode): "Over 1,000 transmission towers collapsed in cascading failures"; about 35,000 wooden poles also fell; some outages lasted "an entire month"; Quebec damage about C$2 billion. The 1998 ice thickness figure was not on the page read.
- **SOURCED** (POWER magazine, Noyabrsk grids, northern West Siberia, above 60°N): frost heave is "the most serious" cause of damage to northern overhead lines; heaving pushed piles up "up to 20 inches per season"; engineering fix: metal cruciform piles approved for 35 to 220 kV lines. A 1992 to 2000 study blamed tower failures on a combination of damp soil, permafrost degradation, frost heave and wind load.
- **UNVERIFIED** (search snippets): in winter 2013-14 two 420 kV lines in southern Norway were damaged by ice loads above design values, with observed loads "four to five times the design value" at one location; Iceland has measured test-span icing since 1972; more than 60% of lines in the Sakha (Yakutia) power system are worn (e-koncept.ru abstract).
- **Failure rates per 100 km-year for icing or blizzard on Arctic lines: NOT FOUND** (IEC 60826, CIGRE sources surfaced only as titles; no rates).

### 4.4 Cable-laying on ice, and any power line or cable longer than a few kilometers on Antarctic ice
- **NOT FOUND.** Queries on Antarctic and Greenland ice-sheet power cables returned only: an IceCube/UMD trencher for power and data cables in ice (short), Concordia low-temperature power cables (no length), a Computerworld story of a National Science Foundation study of a nearly 2,000 km data cable across the Pole route (UNVERIFIED, data not power), and subsea Arctic cable proposals.
- Known short runs: EDEN ISS power by cable over 400 m (round 1 and Zabel); the Ross Island wind turbines connect McMurdo and Scott Base, 3 km apart by road (search snippet, UNVERIFIED). The NSF shared McMurdo–Scott Base utility corridor carries "fuel, water and electrical lines" (Army News snippet, UNVERIFIED).

### 4.5 Typical cost per km (derived from the above; mixed currencies and years)
- Pevek-Bilibino, 110 kV, about 491 km, 18.42 billion rubles (2018 estimate, incl. VAT): **about 37.5 million rubles/km** (DERIVED).
- Bipole III, ±500 kV HVDC with two converter stations: C$4.6 to 5.04 billion / 1,384 km = **C$3.3 to 3.6 million/km** (DERIVED; includes converter stations).
- Kivalliq link (estimate, 1,200 km): C$1.2 to 3.2 billion = **C$1.0 to 2.7 million/km** (DERIVED).
- Alaska Intertie: $124 million / 170 miles = **$0.73 million/mile (about $0.45 million/km)**, mid-1980s dollars (DERIVED).
- Search snippets, UNVERIFIED: a 2002 Alaska utility memo, "at least $400,000 per mile"; an engineering blog, overhead HVDC "about $1–2.5M per km" with no source.
- Cost per km for a line **in Antarctic conditions: NOT FOUND**.

---

## 5. Q5: Local resources at the Bunger Hills

### 5.1 Records that exist (what was found, not what was obtained)
- Oasis station, 1956 to 1958 (round 1): mean wind 6.8 m/s; days with wind ≥15 m/s: 122 a year; maximum 56 m/s; calms 39% of observations; mean winter wind 2 to 3 times lower than at nearby ice-sheet stations; the main katabatic flow "miss[es] the elevated oasis or pass[es] above" (Gregorczuk 1980). White Smoke Lake AWS, 19 months 1992 to 1993: mean 4.6 m/s, peak 32 m/s (carried from round 1; a search result this session repeated the 4.6 m/s from Doran et al. 1996).
- Automated stations: Russian Vaisala MAWS410 "Oazis" at 66°16.465′S, 100°44.773′E, 42 m, in service 9 January 2014 (round 1); an Australian station near Edgeworth David Base; Bureau of Meteorology station ID 300061 at 12 m height listing "no observations in the last 72 hours" (UNVERIFIED snippet); a temporary Casey-deployed AWS (post, no statistics). **No wind statistics from the post-2014 stations were obtained.** Energy study for the oasis: **NOT FOUND** (retried). Wind-resource number for the oasis: **NOT FOUND** from measurements.

### 5.2 Reanalysis computed here (DERIVED; treat as indicative only)
- **Method.** ERA5 hourly data via the Open-Meteo archive API, grid point reported by the service as 66.25°S, 100.75°E, elevation 41 m (essentially the Russian automatic station's position and height), 1 January 2015 to 31 December 2021 (7 years, 61,368 hours; 2022 to 2024 requests timed out). Fields: 10 m wind, 100 m wind, downward shortwave radiation, 2 m temperature. Scripts and raw files are in the unit's scratch folder, not in the repository.
- **Why caution.** The grid cell is about 28 km across and mixes ice, shelf and rock. Its 7-year mean temperature is −12.6 °C, colder than the oasis station record (−9.0 °C, 1956 to 1958) and close to the White Smoke Lake figure (−11.2 °C). Its calm fraction (hours below 3 m/s at 10 m: 17%) is far below the oasis station's 39% calms. So the wind numbers probably describe the surrounding slopes and shelf better than the sheltered oasis floor.
- **Wind (ERA5):** annual mean 6.99 m/s at 10 m and 9.50 m/s at 100 m (year-to-year at 100 m: 8.87 to 10.0 m/s). Monthly mean at 10 m: Jan 5.0, Feb 6.2, Mar 6.3, Apr 7.1, May 7.3, Jun 8.1, Jul 8.7, Aug 9.3, Sep 7.6, Oct 6.8, Nov 6.2, Dec 5.2 m/s. Winter (June to August) is windiest at both heights (100 m: Jun 10.9, Jul 11.9, Aug 12.7 m/s; Jan 6.9, Dec 7.2 m/s). Hours with 100 m wind at or above 25 m/s (the usual turbine cut-out): 5.3% of all hours over the 7 years; by month the most are in August (669 hours in 7 years, about 96 hours per August) and the fewest in January (20 hours in 7 years).
- **Generic turbine capacity factor (DERIVED, cubic power curve between cut-in and rated, cut-out 25 m/s, no icing or cold derating):** 36.5% with cut-in 3 / rated 12 / cut-out 25 m/s; 32.9% for a 330 kW-class curve (3 / 13 / 25); 30.8% with a 20 m/s cut-out. Monthly (3/12/25): 28% in January, 32% in December, 38 to 42% May to August. Hours with 100 m wind below 3 m/s: 17.4%; the longest run was 63 hours; runs of 24 hours or more occurred 63 times in 7 years (about 9 a year); 4 runs of 48 hours or more. Daily capacity factor: 5th percentile 0.006, 10th 0.019, median 0.29, 90th 0.85.
- **Solar (ERA5 downward shortwave, kWh per m² of horizontal surface):** monthly means, 2015 to 2021: Jan 253.5, Feb 158.8, Mar 96.6, Apr 33.2, May 5.7, Jun 0.2, Jul 2.3, Aug 19.7, Sep 66.2, Oct 149.0, Nov 224.7, Dec 273.3; annual **1,283 kWh/m²** (4,620 MJ/m²; yearly values 1,232 to 1,318). Compare the observed record carried from round 1 (Gregorczuk 1980, 1956 to 1958): global radiation 3,735 MJ/m² per year = 1,038 kWh/m², December 779 MJ/m² (216 kWh/m²), January 716 (199), June 0, July 4 (1.1). The reanalysis is **about 24% above the observed annual total** and about 25 to 30% above in December and January. Observed day length: 24 h in December, 2 h 32 min in June (round 1). The two sources agree that June and July have effectively no sun and December and January carry 20 to 21% of the year each.
- **Albedo (round 1, observed):** 16 to 22% in summer, over 50% in winter, annual 30% (Gregorczuk 1980). Peak global radiation under clear sky at highest sun about 907 W/m² (round 1).

### 5.3 Snow and ice albedo effects on photovoltaics
- **SOURCED** (Casey, AAD/Masdar 30 kW array, 105 panels, switched on March 2019, about 10% of the station's annual electricity demand): mounted vertically on the north wall of the "green store" because "the wall of the building gets more sunshine than the roof of the building" at low sun angles; a wind deflector along one side reduces blizzard loads. The page gives no measured yield and does not mention snow albedo.
- **UNVERIFIED** (search snippets): a Sandia study in Vermont found bifacial modules produced about 14% more than monofacial and up to about 40% more in winter; a University of Alaska study found vertical east-west bifacial modules produced about the same annual energy as latitude-tilt south-facing bifacial ones; Sandia modeling found vertical bifacial gains rise with latitude and snow duration. **No measurement from an Antarctic oasis or ice-sheet site was found.**

### 5.4 Wind-turbine experience at Antarctic stations
- **Ross Island Wind Farm (McMurdo and Scott Base), SOURCED** (NREL/Meridian slides, 2012): three Enercon E33 turbines, 330 kW each, on Crater Hill, average wind 7.9 m/s, **37 to 40% capacity factor, about 3.5 GWh/year** against a combined McMurdo electrical load of about 15 GWh/year; 6.8 GWh total production from January 2010 to February 2012; "average ~95% availability, some months ~25% (ice, cold)"; about 22% of the combined stations' electrical energy planned; the diesel offset is quoted as "~270,000 gal/yr" on one slide and as 11% of generating fuel on another. A separate search summary gives 463,000 L/year (UNVERIFIED); the two do not reconcile in the sources read (270,000 gal is about 1.02 million L). DERIVED check: 3.5 GWh / (0.99 MW × 8,760 h) = 40.4%.
- **Mawson (Australia), SOURCED** (AAD, 4 July 2014): two Enercon E-30 turbines of 300 kW each, installed 2003, 30 m towers; **17,010 MWh cumulative output** and "about 5 million liters" of diesel saved; wind penetration (wind power as a share of diesel power) "usually between 55–60% for the year," 81% in April 2014; "best between 16 and 25 m/s"; one diesel generator always runs for frequency control. **DERIVED** capacity factor, 17,010 MWh over 600 kW × 8,760 h × 11.0 to 11.5 years (installation date approximate): **28 to 29%**. Mawson's yearly diesel need was given as 450,000 liters in 2014, the year a ship could not reach Horseshoe Harbour.
- **Neumayer III (SOURCED, Zabel 2022):** a wind turbine "up to 30 kW" beside four 150 kW diesel plants.
- **Casey and Davis (UNVERIFIED, a search summary of a 1998 University of Tasmania thesis):** low wind resource at Casey and Davis, high at Mawson; modeled fuel reductions of 24% and 30% with 100 kW and 50 kW turbines; a 10 kW turbine tested at Casey.
- **Princess Elisabeth (Belgium), UNVERIFIED and conflicting:** reported as 8 or 9 small turbines (6 kW each; total 54 kW peak) plus about 284 solar panels and 192 lead-acid batteries; a Guinness entry gives implausible units. Capacity factor: **NOT FOUND**. Mario Zucchelli and Concordia wind or solar: **NOT FOUND**.
- Turbine collapse at Mawson reported (reneweconomy title only; not read).

---

## 6. Q6: Alternatives, as precedents only

### 6.1 Small reactors at remote polar sites
- **PM-3A, McMurdo (SOURCED in part, Wikipedia):** 1.75 MW electric plus heating and desalination; critical 3 March 1962 (another source in the search says 4 March); shut down September 1972 "after problems including a fire and coolant leakage"; contaminated soil around the tanks was removed to Port Hueneme; program-wide (all the Army reactors, not PM-3A alone), the Atomic Energy Commission phased out its support in 1966 after military research funding was cut during the Vietnam War, and the costs were hard to justify. In search summaries (UNVERIFIED): power available only 72% of the time and more than 400 malfunctions; a cracked containment vessel. Fuel-oil saved, decommissioning cost, crew size: **NOT FOUND**. The Polar Record paper "Atomic energy for Antarctica: the rise and fall of Nukey Poo" (Cambridge) returned 403.
- **PM-2A, Camp Century (Greenland ice sheet) (SOURCED, Wikipedia):** 2 MW electric, critical 3 October 1960, powered the camp for three years, shut down 1963 to 1964.
- **Akademik Lomonosov, Pevek, Chukotka (UNVERIFIED, search snippets):** two KLT-40S reactors of 35 MW electric each (70 MW), connected to the isolated Chaun-Bilibino grid in December 2019, to replace Bilibino NPP and the Chaunskaya thermal plant. **Bilibino NPP** reported at 45 MW capacity (UNVERIFIED). Baimsky mine link: no nuclear connection found.
- **Current microreactor and small-reactor programs, SOURCED** (ANS, 14 November 2025): Radiant Kaleidos 1 MWe helium-cooled, 60 days of full power in 2026 at Idaho National Laboratory; Antares MARK-0 500 kWt, aiming for criticality before 4 July 2026; Valar Ward 250 100 kWt; Oklo Aurora-INL 75 MWe, ground broken September 2025; Aalo-X 10 MWe. The article reports **no** reactor in the DOE Reactor Pilot Program at criticality as of its date. **UNVERIFIED** (search snippets after that date): Antares' Mark-0 reached criticality at INL, the first private company under the program; Oklo's status by 4 July 2026 unknown; the US Army's Project Pele 1.5 MW core in fabrication, possible power "as soon as 2028." None is operating at a polar site in these sources.

### 6.2 Geothermal
- **Local heat-flux value for the Bunger Hills: NOT FOUND** (Martos et al. 2017, An et al. 2015, Shapiro and Ritzwoller 2004 exist as gridded models; no cell value read).
- **UNVERIFIED** (EGU blog snippet): an East Antarctic average of 48 mW/m² with a standard deviation of 13.6 (Goodge 2017); models differ by 10 mW/m² or more and disagree strongly in the Wilkes Subglacial Basin region. **DERIVED:** 0.048 W/m² × 450 km² = 21.6 MW of natural thermal flow across the whole 450 km², low-grade and diffuse. No hot spring, fumarole or volcanic feature near the oasis was found in any source opened (absence not demonstrated; only the heat-flux query was run).

### 6.3 Fuel logistics for diesel generation in East Antarctica
- **Australian program total (UNVERIFIED, search summary of the State of the Environment report):** 6.4 to 7.1 megaliters of fuel a year across all operations (ships and aircraft included), 2015-16 to 2019-20; a fixed headcount of 144 equivalent full-time expeditioners is used for per-person figures in the same reports. **DERIVED, on those unverified inputs:** 44,000 to 49,000 liters per expeditioner per year, all operations. Station-only liters per person: **NOT FOUND**.
- **Mawson (SOURCED):** need of 450,000 L for the year (2014); wind saved about 5 million L over 11 years; "over 200,000 liters" a year at typical penetration.
- **McMurdo (SOURCED, NREL slides):** electrical load about 15 GWh/year; the wind turbines offset about 270,000 gallons a year "NOT including offset waste heat"; generators averaged about 53% loading; one generator alone in 25.6% of 2011 hours.
- **South Pole (SOURCED, Hackaday):** three Caterpillar 3512B generators each derated to 750 kW; fuel delivered by LC-130 at about 1.33 kg of fuel per kg delivered or by the traverse (about 1,600 km, about 40 days) at about 0.56 kg per kg (round-1 traverse figure: whole train ≈66 L/km). Annual fuel use not stated.
- **Neumayer III (SOURCED):** one resupply pumped 270,000 L Arctic diesel and 60,000 L aviation fuel across the shelf edge (round 1).
- Special Antarctic Blend is the diesel-like fuel used at Australian stations (search summary, UNVERIFIED).

---

## FINAL: what the sources support, do not support, and NOT FOUND

### What the sources support
1. **Electricity per kg for leafy greens in lit vertical farms is 10 to 20 kWh/kg in most sources** (modeled range 7.8 to 23.8; literature cited 3.2 to 20; a census average near 38). Lighting is 46 to 75% (about 70% in several sources) and HVAC or dehumidification 22 to 52%. The best fixtures tested are 2.5 to 3.0 µmol/J; theoretical limits for current LEDs are 3.4 to 4.1.
2. **Measured Antarctic indoor farms use far more per kg:** EDEN ISS 205 to 256 kWh/kg, the South Pole chamber about 100 kWh/kg, with 20% of EDEN ISS electricity going to room heaters and heat-related equipment and 33% to atmosphere management.
3. **Cold outdoor air:** free cooling removes compressor use in winter (EDEN ISS shut off its cooler fans for four months); the penalty is heating in the dark period and building heat loss. In a modeled insulated farm, warm-climate sites (Shanghai, Dubai) used 2.6 to 5.7% more specific energy than the cold-climate site (Trondheim).
4. **Staple crops under lamps are 10 to 40 times more energy-intensive per kg than lettuce** (potatoes at least 62, wheat at least 435 kWh/kg in one unverified review; 250 kWh/kg dry matter at 2% efficiency in a peer-reviewed estimate) and the sources conclude they are not economic at current electricity prices.
5. **For feeding N people entirely from lit indoor farming, the computed average power is about 6 to 16 kW per person:** about 0.6 to 1.5 GW per 100,000 people, 4.5 to 11.6 GW per 750,000, 6 to 15.4 GW per 1,000,000 (rows A, B), with the low end 1.2 kW per person (0.12 / 0.9 / 1.2 GW) if efficiency reached the 10% upper bound and salad-crop Antarctic benchmarks giving 27 to 40 kW per person. For scale, the largest operating vertical farms harvest about 1,000 t/year and draw an estimated 1 to 2.5 MW.
6. **Long transmission is real in subarctic Canada and Chukotka** (1,100 to 1,400 km HVDC; 110 kV over about 490 km of Chukotka; costs from about C$1 to 3.6 million per km), and icing, galloping and permafrost heave are documented causes of failure (Labrador-Island Link, Iceland, Norway, Siberia).
7. **Station wind turbines work in Antarctica** at capacity factors of 37 to 40% (Ross Island, measured) and about 28 to 29% (Mawson, derived), with some months of 25% availability from ice and cold. Reanalysis for the oasis' grid cell suggests 7.0 m/s at 10 m and about 31 to 37% for a generic turbine; the oasis floor itself has more calms.
8. **Solar at 66°S is strongly seasonal:** 2 months of essentially zero sun and about 40% of the year's energy in December and January (observed and reanalysis agree on the shape; the reanalysis total is about 24% above the observed 1956 to 1958 total).
9. **Reactors at polar sites have precedent only as early military units** (PM-3A 1.75 MW, PM-2A 2 MW at Camp Century) and a Russian floating plant (2 × 35 MW at Pevek); current microreactors are in demonstration at Idaho and none has a polar deployment in the sources.

### What the sources do not support
- Any example of hundreds of thousands of people, or any city, fed entirely from indoor hydroponics. The largest operations are leafy-green farms.
- Any measured energy, wind-resource or solar-resource study for the Bunger Hills oasis after 1958 (the 1992 to 1993 White Smoke Lake record is short and on a colder, atypical lake site).
- Any power line or cable longer than a few kilometers on Antarctic ice; any HVDC or HVAC line in an ice-sheet setting.
- Any published failure rate (per 100 km per year) for icing or blizzard on Arctic lines.

### NOT FOUND (collected)
Measured electrical load of Bustanica, Nordic Harvest, Jones Food Company or any large vertical farm; indoor kWh/kg for rice and tomatoes; the full text of Pattison et al. 2018, Graamans et al. 2018 and the MDPI/Kobayashi staple-crop figures; power per kg for Zhongshan, Great Wall, McMurdo, Casey, Davis, Mawson, Svalbard and Greenland farms; a power line above a few kilometers on Antarctic ice; Antarctic cost per km; icing failure rates; post-2014 Bunger Hills station wind statistics; a local geothermal heat-flux value; PM-3A availability, oil saved, cost; station diesel liters per person; the AAD State of the Environment pages; Casey and Davis wind-resource thesis details; Princess Elisabeth capacity factor.

### Pages that failed and were not worked around
msu.edu LED PDFs (empty); mdpi.com (403); cris.unibo.it (403); jukuri.luke.fi (bot wall); repository.tudelft.nl (SSL error); cbc.ca and amp.cbc.ca (403); nlhydro.com (SSL error); cambridge.org Polar Record (403); apps.dtic.mil (HTML interstitial); nrel.gov (no connection, DNS failure); soe.dcceew.gov.au and agriculture.gov.au (socket hang up); data.aad.gov.au (403); Open-Meteo requests for 2022 to 2024 (timed out, stopped). No search was refused by the search tool; no STOP note was needed.

**Ended:** 2026-11-02 17:23:48.

---

## Search log

Format: number, tool, exact query or URL, result (hit / partial / miss), and for a miss where it died. A "hit" means the source or answer was read; "partial" means a snippet or incomplete answer.

- 1 WebSearch "vertical farm electricity consumption kWh per kg lettuce lighting HVAC dehumidification share of energy" | hit (snippets: Manitoba, arXiv 2603.15806, 2507.18419, NREL)
- 2 WebSearch "LED horticulture fixture efficacy µmol/J 2025 highest efficacy DLC qualified product list" | partial (no top figure; MSU Runkle: DLC min 1.9, ~6% >=3.0 per snippet)
- 3 WebFetch canr.msu.edu 2024-01 Update on LED efficacy.pdf | miss (empty content returned; died at fetch)
- 4 WebFetch mspace.lib.umanitoba.ca item ac54c125 | hit (abstract only)
- 5 WebFetch canr.msu.edu LED efficacy.pdf | miss (empty)
- 6 WebFetch arxiv.org/pdf/2507.18419v1.pdf | hit via saved PDF + pdftotext (Ceccanti et al.)
- 7 WebSearch "largest vertical farm in the world Bustanica Dubai Crop One annual production kg megawatt power" | partial (size, output; no MW)
- 8 WebSearch "Nordic Harvest Taastrup vertical farm 7,000 m2 power consumption MW wind turbines tonnes per year" | partial (no MW)
- 9 WebSearch "vertical farm "megawatts" electricity demand facility grid connection lettuce plant factory hectare" | partial
- 10 WebSearch "Jones Food Company Lincolnshire vertical farm 5,000 m2 electricity MW renewable power tonnes basil per year" | partial (no MW)
- 11 WebFetch canarymedia.com vertical farms microgrid | hit (lighting ~70%; Fifth Season 1.75 MW microgrid, partial)
- 12 WebFetch sustainabilitybynumbers.com/p/vertical-farming | redirect; 13 WebFetch hannahritchie.substack.com/p/vertical-farming | hit
- 14 WebSearch "Kozai plant factory electricity use efficiency kWh per kg fresh weight lettuce 2023 energy consumption review photon cost staple crops rice wheat economically unfeasible" | partial
- 15 WebFetch par.nsf.gov/servlets/purl/10206750 | miss (one-page unrelated PDF)
- 16 WebFetch mdpi.com/2071-1050/17/7/3259 | miss (403, died at source)
- 17 WebSearch "indoor vertical farming staple crops wheat rice potato electricity kWh per kg dry grain lighting energy requirement calories energy return" | partial (snippets: potato >=62, wheat >=435 kWh/kg per MDPI review citing Kobayashi; UNVERIFIED)
- 18 WebSearch "Pattison Tsao Brainard Bugbee 2018 Nature "LEDs for photons, physiology and food" cost of lighting wheat rice" | partial (paywalled)
- 19 WebFetch ncbi PMC12225668 | redirect; 20 WebFetch pmc.ncbi.nlm.nih.gov/articles/PMC12225668 | hit (Lovat, Noor, Milo 2025)
- 21 WebSearch "Graamans 2018 "Plant factories versus greenhouses: Comparison of resource use efficiency" electricity kWh per kg dry weight lettuce Sweden" | partial (abstract numbers in snippet only: 247 PF; 70 NL; 111 UAE; 182/211 Sweden = UNVERIFIED)
- 22 WebSearch "tomato indoor vertical farming LED electricity kWh per kg fruit energy use fully artificial light tomatoes study" | partial/miss (no tomato kWh/kg)
- 23 WebFetch ideas.repec.org Graamans | partial (abstract without numbers; full text ScienceDirect subscriber only)
- 24 WebFetch jukuri.luke.fi luke-luobio_49_2015.pdf | miss (Anubis bot-wall; not worked around)
- 25 WebFetch repository.tudelft.nl Graamans | miss (SSL error WRONG_VERSION_NUMBER)
- 26 WebFetch cris.unibo.it Orsini 2020 | miss (403)
- 27 WebSearch "Plenty Richmond Virginia vertical farm Dominion Energy megawatts power load substation" | partial (site criterion 15+ MW)
- 28 WebSearch "Bustanica Emirates Crop One Dubai electricity consumption solar MW kWh vertical farm 330,000 square feet energy use" | partial (no energy figure published)
- 29 WebFetch grpva.com Plenty success story | hit (15+ MW site request, 120 acres, 4 M lb/yr)
- 30 WebFetch nzherald Bustanica | hit (3 t/day, 3 ha floor area, 27 rooms 550 sqm x 6 shelves; energy "hungry", no figure)
- 31 curl elib.dlr.de Zabel 2022 pdf + pdftotext | hit (read in full)
- 32 WebSearch "Antarctic station greenhouse hydroponic power consumption kW kg vegetables per year Zhongshan Great Wall Maitri Bharati" | partial
- 33 WebSearch "South Pole Station food growth chamber 2023 2024 new greenhouse hydroponic NSF output kg per week power" | partial (no recent; Giacomelli slides lead)
- 34 curl frc.ri.cmu.edu GIACOMELLI.pdf | hit (SPFGC 10-13 g/kWh edible)
- 35 WebSearch "Naurvik Gjoa Haven hydroponic container farm electricity use kWh per week kg produce solar wind diesel" | partial (no kWh/kg)
- 36 WebSearch "Nuuk Greenland hydroponic farm "Green Greenland" OR "Greenlandic Greenhouse" electricity hydropower kWh vegetables tonnes per year" | partial/miss for farm numbers
- 37 WebSearch "longest power line Antarctica cable station power cable length km buried ice McMurdo Scott Base power cable" | miss
- 38 WebSearch "transmission line ice loading permafrost Yakutia 220 kV line length km Siberia Arctic overhead line icing failures" | partial
- 39 WebSearch "Antarctic station "overhead" OR "underground" high voltage power cable km to remote facility airfield wind farm Mawson Casey Davis Scott Base 11 kV" | miss
- 40 WebFetch powermag.com frost heaving | hit
- 41 WebFetch en.wikipedia Bipole_III | miss (404)
- 42 WebFetch en.wikipedia North_American_ice_storm_of_1998 | hit
- 43 WebSearch "Kivalliq Hydro-Fibre Link transmission line Manitoba Nunavut cost billion km permafrost study" | partial
- 44 WebSearch "Alaska Railbelt Intertie 345 kV Anchorage Fairbanks miles cost per mile transmission line Arctic Alaska cost" | partial
- 45 WebFetch nunatsiaq Kivalliq $3.2B | hit
- 46 WebFetch akenergyauthority.org Alaska Intertie | hit
- 47 WebSearch "HVDC overhead line unit cost per km 500 kV 2 GW million USD per km DC transmission cost benchmark 2023 report" | partial
- 48 curl open.alberta.ca Stantec 2009 summary | hit but relative costs only
- 49 WebSearch "Manitoba Hydro Bipole III transmission project 1,384 km 500 kV HVDC final cost billion in service 2018" | partial
- 50 WebSearch "Labrador-Island Link HVDC 1,100 km ±350 kV ice icing galloping conductor cold weather outage Newfoundland 2021 2022 issues" | partial
- 51 WebFetch cbc.ca/1.6989056 | miss (403, died at source)
- 52 WebFetch renewableenergyworld LIL | hit (partial)
- 53 WebFetch amp.cbc.ca lite story | miss (403)
- 54 WebFetch nlhydro.com/?p=61559 | miss (SSL error)
- 55 WebFetch hackaday.com Making Electricity At The South Pole | hit (article does not discuss a power line; 1,600 km is the fuel traverse)
- 56 WebSearch "power cable laid on ice sheet snow trench cable plow Greenland Summit Station OR Antarctica long electrical cable kilometers research station experience" | partial (no power-cable record found; snippets about data cable studies)
- 57 curl apps.dtic.mil ADA121109.pdf | miss (an HTML interstitial came back instead of the PDF; not worked around)
- 58 WebSearch "Ross Island wind farm Antarctica capacity factor three Enercon E33 turbines kWh per year diesel savings Antarctica New Zealand report" | hit (snippets, led to NREL slides)
- 59 WebSearch "Mawson station wind turbines two 300 kW capacity factor wind power percentage diesel saving Australian Antarctic Division" | hit
- 60 curl sundowner.colorado.edu PTC_2012_Roberts.pdf (NREL/Meridian Ross Island slides) | hit (read)
- 61 WebFetch antarctica.gov.au "This week at Mawson 4 July 2014" | hit
- 62 Open-Meteo archive API (ERA5), curl, 2015-2021 hourly, point 66.28S 100.78E (snapped to 66.25S 100.75E, 41 m) | hit for 7 years; 2022-2024 requests hung/rate-limited and were stopped, so 7 years used
- 63 WebSearch "Bunger Hills automatic weather station wind speed annual mean Oasis Russian AWS Vaisala data wind rose" | partial (no AWS wind statistics)
- 64 WebSearch "Australian Antarctic Division Casey station renewable energy wind turbine solar capacity fuel use per year litres Casey Davis Mawson energy strategy" | partial
- 65 curl nrel.gov/docs/fy24osti/89240.pdf | miss (no connection); 66 WebFetch same URL | miss (DNS ENOTFOUND)
- 67 WebFetch onestepoffthegrid.com.au Casey 30 kW vertical solar | hit
- 68 WebSearch "PM-3A McMurdo nuclear power plant 1962 1972 1.8 MW electric output fuel oil savings problems shut down cost decommissioning" | partial
- 69 WebSearch "microreactor demonstration status 2026 Project Pele Eielson Oklo Aurora Alaska remote microreactor first criticality DOE reactor pilot program July 2026" | partial
- 70 WebFetch cambridge.org Polar Record "Nukey Poo" core-reader | miss (403, died at source)
- 71 WebFetch ans.org article-7543 Reactor Pilot Program update | hit
- 72 WebFetch en.wikipedia.org/wiki/PM-3A | hit (partial; no availability or oil-saved figure)
- 73 WebSearch "Akademik Lomonosov floating nuclear power plant Pevek 70 MW electrical operating since 2020 Bilibino NPP Chukotka output Baimsky" | partial
- 74 WebSearch "Davis Casey Mawson station annual diesel fuel consumption litres per year AAF "litres" Antarctic Division station fuel use summer winter population" | partial
- 75 WebSearch "Antarctic research station fuel consumption per person per year liters COMNAP energy use stations comparison kWh per person" | partial
- 76-77 WebFetch soe.dcceew.gov.au human-environment (two tries) | miss (socket hang up, died at source)
- 78 WebFetch data.aad.gov.au soe_id=57 | miss (403)
- 79 WebFetch agriculture.gov.au 2015-16-environmental-indicators.pdf | miss (socket hang up)
- 80 WebSearch "geothermal heat flux East Antarctica Wilkes Land Knox Coast mW/m2 map Martos 2017 Shapiro Ritzwoller heat flux Bunger Hills" | partial (no local value)
- 81 WebSearch "Norway Finnmark Arctic 420 kV transmission line Skaidi Hammerfest ice loading wind icing line design Statnett outages Arctic conditions" | partial
- 82 WebSearch "atmospheric icing overhead transmission lines Nordic outage statistics ice load design kg/m rime 50-year return period Iceland Norway CIGRE failures per 100 km" | partial
- 83 WebSearch "Landsnet Iceland Byggðalína 132 kV ring line icing outages Sprengisandur highland transmission line ice storm failure" | partial
- 84 WebFetch powermag.com Landsnet and Laki Power | hit
- 85 WebSearch "Yakutia Arctic power line 110 kV Tiksi OR Chokurdakh OR Zyryanka length km permafrost foundations cost rubles per km Yakutskenergo Nizhny Kuranakh" | miss (query returned nothing on target)
- 86 WebSearch (Russian) "ЛЭП 110 кВ Арктика Якутия протяженность км вечная мерзлота стоимость строительства млрд рублей Тикси Усть-Куйга" | partial (led to Pevek-Bilibino)
- 87 WebSearch (Russian) "Чаун-Билибинский энергоузел ЛЭП 110 кВ Билибино Певек протяженность км гололедные нагрузки аварии обледенение проводов Чукотка" | partial
- 88 WebFetch eastrussia.ru Pevek-Bilibino 18.42 bn | hit
- 89 WebFetch eastrussia.ru Baimsky GOK line | partial (110 kV; no length)
- 90 WebFetch en.wikipedia High-voltage_direct_current | hit (first 100,000 of 156,090 characters)
- 91 WebSearch "Princess Elisabeth Antarctica station wind turbines solar panels zero emission energy production kWh capacity factor Mario Zucchelli wind turbine Concordia solar" | partial (sources conflict)
- 92 WebSearch "bifacial photovoltaic snow albedo vertical array high latitude polar performance measured yield gain winter Antarctica OR Svalbard OR Greenland" | partial (no polar measurement)
- 93 WebFetch pmc.ncbi.nlm.nih.gov PMC7105460 (Kusuma 2020) first try | miss (tool error); 94 second try | hit
- 95 WebSearch "Our World in Data daily supply of calories per person kcal world average food supply kilograms per person per year FAO food balance" | miss (no figure returned)

Notes on the log: items 7-10 and others marked partial relied on search-tool summaries that I then tried to confirm by opening sources; where the open failed, the claim is UNVERIFIED in the body. The reanalysis step (item 62) was run by script in the unit scratch folder (not in the repository): `analyze.py`, `extra.py`, `calc.py` and the raw ERA5 JSON files. The shell hook that blocks `rm` stopped one cleanup command; nothing was deleted.

**Unit R1 ended 2026-11-02 17:23:48.**
