# Heat, unit P3: food production and housing heat demand (2026-11-02)

**Scope.** Real-world facts for the question "what could plant reject heat do for food and housing, and how much heat do those uses need." Covers indoor-farm and greenhouse heat budgets, waste-heat greenhouse precedents, aquaculture on power-plant heat, livestock, insects and soil heating, housing heat demand in extreme cold, scale checks per gigawatt of heat (GWth), and published food mass per person for orbit. No recommendation, no design, no ranking. Technology reference is the 2020s. Labels: **SOURCED** (read at the source page or document in this session), **DERIVED** (my arithmetic on stated inputs, working shown), **UNVERIFIED** (seen only in a search snippet or summary, recalled, or inferred), **NOT FOUND** (looked for; queries in the log). "Carried from R1" means read at the source in `Relung_Panen_R1_Power_Research_2026-11-02.md` (which I read in full for this unit) and not re-opened here. The search tool returns summaries, so many figures below are UNVERIFIED snippets; the ones I opened as primary documents are marked SOURCED.

**Started:** 2026-11-02 21:08. **Finished:** see the stamp at the end of the FINAL section. (Clock note: the shell clock ran faster than the session's call count suggests; the stamps are the shell's.)

**Read first (as the brief required):** `Relung_Panen_R1_Power_Research_2026-11-02.md` (all of it) and `Cities/Division_of_Industry/13_National_Balance_Under_the_Ruling.md` lines 440 to 520. Facts taken from the repo, not re-researched: the national staple tier is 1,180 km² of growing area and 10.37 Mt/yr; electricity for it is 944 GW at EDEN ISS's measured 256 kWh/kg, 47.4 GW at 40 kWh/kg and 11.8 GW at 10 kWh/kg, against a national grid of 101.7 GW (file 13, section 11). Canon food rate: 0.66 t per human per year (brief).

## PROGRESS

- [x] Q1 Heat budget of indoor farms and greenhouses (splits, lamp heat, cold-air envelope load). Alaska annual greenhouse energy: NOT FOUND.
- [x] Q2 Waste-heat greenhouse precedents (Bruce, Netherlands, Iceland, Kamchatka, Nordic, Siberian, nuclear). Heat per m² for most named cases NOT FOUND; partly filled.
- [x] Q3 Aquaculture on power-plant heat (Tihange, Japan, Korea, Browns Ferry-era US, RAS energy). Regulator stance: NOT FOUND.
- [x] Q4 Livestock, poultry, insects, soil heating (poultry and pig numbers found; crickets and field-scale soil heating NOT FOUND).
- [ ] Q5 Housing heat demand in extreme cold: PARTLY done. Fairbanks and Greenland (Sisimiut) found; Yakutsk, Norilsk, Nuuk, Longyearbyen, Iqaluit, Alert kWh/m² and per-person figures NOT FOUND; Antarctic per-person heat NOT FOUND. Not ticked.
- [x] Q6 Scale checks (derived, working shown).
- [x] Q7 Food mass per person for orbit and launch cost; SP-413 agriculture area: primary NOT FOUND.

---

## 1. Q1: Heat budget of indoor farms and greenhouses

### 1.1 Where the energy goes (splits)
| Source | System | Split | Status |
|---|---|---|---|
| Zabel et al. 2022, EDEN ISS (Antarctica, 2018) | Two containers, 12.5 m² cultivation area | atmosphere management 33%, illumination 28%, common equipment (room heaters, water boiler, room lights) 20%, thermal control 11%, control and data 6%, nutrient delivery 2%; 68,516 kWh over 286 days | carried from R1 (opened in full there) |
| Manitoba pilot (thesis abstract) | Vertical farm | lighting 46 to 75%, HVAC 22 to 52% | carried from R1 |
| Ceccanti et al., arXiv 2507.18419 | Modeled lettuce, 162 cases | lighting plus the cooling to remove its heat "over 95%" | carried from R1 |
| Ceccanti et al., arXiv 2603.15806 (Univ. of Pisa, opened this session, text extracted) | Modeled 3-tier container farm, Dubai | "energy use is dominated by lighting and cooling, with lighting slightly higher than cooling, while heating, dehumidification, and post-heating represent minor contributions"; "Owing to the insulated envelope, heating demand is largely confined to the dark period and remains low"; dehumidification limited because "the chiller operates and simultaneously removes both lighting waste heat and water vapor" | SOURCED (preprint, a model, a hot climate) |
| Same paper, citing a comparison of plant factory and Dutch greenhouse (Graamans et al. 2018) | Lettuce | Dutch greenhouse about 2,100 MJ per kg dry biomass total, "Solar radiation provides the largest share of the total energy input (76%), while heating and cooling each accounted for about 12%"; purchased electricity about 70 kWh per kg dry biomass; plant factory "about 33% less total energy input, but about 253% more electricity (247 vs 70 kWh e per kg dry biomass), with artificial lighting accounting for around 90% of the electrical load" | SOURCED as quoted inside the Pisa paper (the Graamans paper itself was not opened; R1 also lists it as UNVERIFIED) |
| Montreal modeling group (Monfet), 2024 and 2025 | Controlled-environment agriculture, high density | lighting "55%" to "80%" of electricity (search summary); HVAC energy is "required to dissipate the heat generated by electric lighting and crop transpiration" | UNVERIFIED (snippet) |
| Cornell CEA group (Harbick, Albright, Mattson), conference slides "Energy consumption in controlled environments", about 2016 (opened this session) | Plant factory vs greenhouse, US climates | "In plant factories/vertical farms, internal loads dominate"; "In greenhouses, external loads often dominate"; "3 to 12x lighting energy used in plant factory vs greenhouse, depending on location"; "1.5 to 5x total energy used in plant factory vs greenhouse (contiguous U.S.)"; "Moving away from equator favors plant factory; Crossover somewhere in Alaska/Canada"; the slide listing "Sensible applications" names "Research, Space, South pole" with "Heating costs >>> elec. cost" | SOURCED (slides; the crossover remark is the authors' summary of their earlier work, not re-derived here) |

### 1.2 How much heat the lamps themselves release
- **SOURCED** (Cornell slides): a worked case at "1.7 mol/J @ 17 mol/m²/d -> 117 W/m²" of lighting power, evapotranspiration "ET = 67 W/m²", leaving "net sensible heat: 50 W/m²" and "net latent heat: 67 W/m²". **DERIVED check:** 17 mol/m²/d ÷ 1.7 µmol/J = 10.0 MJ/m²/d = 115.7 W/m², which matches the slide's 117 W/m² and shows the slide treats all lamp electricity as heat inside the room (sensible plus latent through the water the plants evaporate). The slide also says a plant factory has a sensible-heavy load when "Light power > 2x ET power" and a latent-heavy load, needing reheat, when "Light power < 2x ET power".
- **SOURCED** (Lovat, Noor, Milo 2025, carried from R1): energy-to-food efficiency of vertical farms is about 1% (0.4 to 1.9% over 19 studies). **DERIVED:** if only 0.4 to 1.9% of the electricity ends as chemical energy in food, 98.1 to 99.6% of it ends as heat in the building. Not a published heat fraction; my reading of that efficiency.
- **UNVERIFIED** (grower guides in search snippets): "about 50% of the electrical input power is converted into light output. Leaving the remaining 50% being converted into heat"; another guide takes "essentially all LED power ends up as heat" in a sealed building. These conflict only in how they define "heat" (heat at the fixture versus heat after the light is absorbed). The first counts the radiated light separately; the room still receives it as heat when it is absorbed by leaves, trays and walls.
- **DERIVED, LED efficacy to radiated fraction:** Kusuma et al. 2020 (carried from R1): best fixtures 2.5 to 3.0 µmol/J. If a joule of 400 to 700 nm radiation carries about 4.56 µmol (the conversion factor the Pisa paper adopts for PAR, line "conversion factor of 4.56 μmol J-1"), 2.8 µmol/J means 2.8 / 4.56 = about 61% of electricity leaves the fixture as photosynthetic radiation and about 39% as heat at the fixture. The radiated 61% is absorbed in the room as well.
- **Result for the plant-heat question (DERIVED):** a lit indoor farm is a heat source. Its heat release is about its electrical input (EDEN ISS: 68,516 kWh over 6,864 h = 9.98 kW average, carried from R1). Applied to the repo's national staple tier (file 13): 11.8 GW at 10 kWh/kg means about 11.7 GW of heat released inside the farms (11.8 GW × 0.99), 47.4 GW at 40 kWh/kg, 944 GW at 256 kWh/kg. Heat from outside would be needed only for the building shell and the dark period.

### 1.3 When farms need extra heat or cooling
- **EDEN ISS (carried from R1, Zabel 2022):** in winter the free-cooling fans were not needed June to September; demand still rose June to October "most likely associated with the dropping temperatures during the winter months and the corresponding need for additional electrical heating"; the common equipment (room heaters etc.) used 13,461 kWh in 286 days = 1.96 kW average (DERIVED: 13,461 / 6,864 h), 20% of the total.
- **Ceccanti 2507.18419 (carried from R1):** removing insulation raised specific energy 40 to 70% at low light intensity in a cold climate; raising the setpoint from 20 to 28 °C raised heating demand 50% there.
- **Pisa model (above):** insulated container farm, heating "largely confined to the dark period."

### 1.4 Cold outside air on the envelope: greenhouses and farms, by region (heat per m² of floor)
| Place / source | Figure | Status |
|---|---|---|
| Europe, Energies 2023 review (MDPI 16(19):6788) | greenhouse heating need "250 to 430 kWh/m²/y" at 40 to 50°N; "430 to 650 kWh/m²/y" at 50 to 60°N; Estonia, Finland, Lithuania, Latvia "over 444"; latitude "the most significant factor" | UNVERIFIED (search summary of the abstract) |
| Magallanes, Chile (sub-Antarctic, modeled tomato greenhouse) | 7,813 MJ/m²/yr = **2,170 kWh/m²/yr** (DERIVED: 7,813 / 3.6); ventilation and infiltration 45.8% of loss | UNVERIFIED (snippet; a model, one case) |
| Netherlands, Greenhouse Horticulture Key Figures 2026 (Glastuinbouw Nederland, opened) | total glass 10,637 ha; specialist greenhouse area 8,490 ha (vegetables 4,799, cut flowers 1,731, pot and bedding plants 1,903, fruit 57); natural gas "Crop heating: 1.97 billion m³", "Supplying electricity to the national grid: 0.97 billion m³", total 2.94 billion m³; geothermal heat to 237 growers on 1,746 ha, 7.1 PJ; "Around 15% of the energy greenhouse growers use comes from renewable sources" | SOURCED (the sheet does not date each figure; some graphics are labeled 1990, 2017, 2020) |
| **Derived Dutch heat per m²** | 1.97e9 m³ × 31.65 MJ/m³ (calorific value recalled, UNVERIFIED) = 62.4 PJ = 17.3 TWh; over 8,490 ha (84.9 km²) = **204 kWh/m²/yr = 23.3 W/m² average**, fuel basis; includes unheated area and combined-heat-and-power gas whose electricity is sold, so not heat delivered | DERIVED |
| Finland, all greenhouses (round 1, carried from R1) | about 480 kWh/m²/yr all energy | carried from R1 |
| Tromsø year-round tomatoes (round 1, DERIVED from Naseer et al. 2022 in R1) | 1,006 kWh/m² electricity plus 166 kWh/m² gas | carried from R1; the paper (Agricultural Systems 198:103391) was not opened this session; a search showed its abstract: heat pump and year-round production cut fossil fuel use |
| Alaska (UAF Cooperative Extension, search summary) | design example: 69,120 Btu/h for a 12 × 16 ft (192 ft²) greenhouse, single layer, −30 °F design = 360 Btu/h/ft² = **1,136 W/m² peak** (DERIVED: 360 × 3.1546 W/m² per Btu/h/ft²); "greenhouse heating requirement doubles as wind speed goes from 0 to 15 miles per hour"; "Greenhouses in Alaska are often operated seasonally because of the high energy costs" | UNVERIFIED (snippet); annual Alaska year-round greenhouse kWh/m²: **NOT FOUND** |
| Iceland geothermal greenhouses | Annual kWh/m²: **NOT FOUND**. A low-reliability page claims 1.5 to 2 kWh/m²/yr (geothermal) vs 15 to 20 (conventional), which is implausible next to the figures above and was not traced to a primary source; treat as unreliable | UNVERIFIED, doubtful |
| Canada, Siberia | Manitoba pilot vertical farm 517 to 773 kWh/m²/yr floor area (carried from R1); Yakutsk Sayuri: annual heat per m² **NOT FOUND** | |

### 1.5 Indoor farm shell load, cold climate
Published vertical-farm shell heat loads (W/m² of floor) for Alaska, Iceland, Canada or Siberia: **NOT FOUND**. Nearest are EDEN ISS (1.96 kW of common equipment for two containers), the Manitoba totals and the Pisa dark-period statement above.

---

## 2. Q2: Waste-heat greenhouse precedents

### 2.1 Bruce Energy Centre (Tiverton, Ontario)
- **SOURCED** (Ontario Legislature committee transcript, Kincardine hearing, 30 October 1997, first 100,000 of 159,432 characters read): the Centre "was founded about 13 years" before the hearing (about 1984); tenants named: Commercial Alcohols (pilot ethanol plant), Canadian Agra Corp (invested 1989, alfalfa dehydration plant 1990), Integrated Energy Development Corp, which "developed a greenhouse at BEC meant to act as an end-of-line condenser," and, not at the hearing, St Lawrence Technologies, BI-AX International (polypropylene film) and Bruce Agra Foods; "Hydro has a contractual commitment to provide steam at a rolling price 10 years in advance that is cost-based"; in March 1992 Hydro refused a long-term steam contract for the ethanol plant; in mid-1993 rural electricity rates were applied; the speaker states the Bruce development ran at about 25% thermal efficiency and that "up to 240,000 barrels of oil per day" of heat went to Lake Huron (a witness's statement, not checked). The Centre has "900 acres" plus "about 4,000 acres."
- **NOT FOUND:** greenhouse area, heat delivered per m², crops, yields, years of operation, or whether the greenhouse still exists (two searches). The steam here is process steam from CANDU units, a different heat grade from condenser water.

### 2.2 Other nuclear plant heat, greenhouses
- **France (SOURCED abstract, OSTI 5027502, Nuclear Technology paper, 1978):** a CEA, EDF and Ministry of Agriculture program "begun in 1972" used plant heat for farming. Greenhouses were heated by "water at about 30 °C (303 K)" circulated through "double-wall plastic mulch" on the soil, "used successfully for a few years on several hectares," with heat pumps added when needed; tomatoes, cucumbers, flowers and strawberries "did very well." Outdoor soil heating by buried pipes at Cadarache (near an experimental pressurized-water reactor) gave "excellent" earlier and larger yields for asparagus, strawberries and potatoes. Eels "grew about four times faster over one year."
- **Browns Ferry, Alabama (SOURCED abstract, OSTI 6272979, Tennessee Valley Authority report, August 1980):** a 25,000 ft² (2,323 m², DERIVED: 25,000 × 0.0929) experimental greenhouse in three sections, two on condenser cooling water and one conventional; supply 3,000 gal/min (three 125-hp pumps) through about 2,000 ft of 12-in. pipe; built November 1978, first tomatoes planted 10 January 1979. "Low winter temperatures lowered tomato yield and quality in the two CCW sections, which averaged 13.0 lb/plant, compared with 15.4 lb/plant in the conventionally heated zone" (a 15.6% drop, DERIVED). The cooling water "sometimes fell to 52°F, 18°F below the predicted 70°F minimum"; greenhouse air stayed "within 10° to 12°F of the incoming water temperature." Ornamentals "have more potential than vegetables." Heat-exchange systems "need higher capital investment and more electricity than conventional greenhouse heating."
- **Exelon / University of Illinois (UNVERIFIED, search snippet):** a study of using lost nuclear-plant heat for greenhouses and biofuel; a proposal, not a measured result.
- **Tricastin (France):** no specific greenhouse figure found (**NOT FOUND**; a search showed only general claims).
- **Fusion plant heat for greenhouses:** **NOT FOUND**, no source.

### 2.3 Netherlands
- **CHP and OCAP (SOURCED, factsheet opened, undated, about 2018):** OCAP supplies "about 500,000 tons of CO₂ per year to approximately 600 greenhouse companies" representing "some 2,500 hectares," from Shell Botlek hydrogen production and the Alco bioethanol plant; savings "about 140 million cubic metres of natural gas a year." **OCAP carries CO₂, not heat.** Dutch residual-heat and geothermal use: see 1.4.
- Westland CHP heat per m² for one farm: **NOT FOUND** (only the sector sums above).

### 2.4 Iceland, Kamchatka
- **Iceland:** geothermal greenhouse heating "since 1924" (UNVERIFIED snippet); Friðheimar 4,200 m² of tomatoes with 600 to 700 t/yr stated for a cucumber site of 3,800 m² (snippets conflict); winter assimilation lighting is used. Hectare totals, heat per m²: **NOT FOUND**.
- **Kamchatka (UNVERIFIED, Hortidaily 2014 to 2017):** a regional program aimed for greenhouse output "up to 2,000 tons a year" and "up to 30 hectares" against about 90 t then; a 4.8 ha project near Petropavlovsk dropped hot-spring heating "because of high economic and environmental costs." Whether targets were met: **NOT FOUND**. Heat per m²: **NOT FOUND**.

### 2.5 Nordic industrial heat
- **Sweden, Frövi (SOURCED, Selected Group page and BillerudKorsnäs release, both opened):** "at least 100,000 m²" (10 ha) of greenhouse heated by surplus heat from the neighboring pulp mill, tomatoes, "over 8,000 tonnes of tomatoes every year" (DERIVED: **80 kg/m²/yr**), about 10% of Sweden's tomato consumption, 9,936 lights; the mill release (27 Oct 2021) describes a 20-hectare industrial estate with Sweden's largest tomato greenhouse. **Heat delivered (MW, GWh) and temperature: NOT FOUND in either page.**
- **Norway, SINTEF HighEFF case (SOURCED, page opened):** "100 GWh of surplus heat for the production of 1809 t tomatoes per year," "5 % of the total Norwegian tomato consumption" for low-temperature aluminum-plant heat. **DERIVED: 100 GWh / 1,809 t = 55 kWh of heat per kg of tomatoes.** The page gives neither temperature nor area. A second SINTEF pre-project studies data-center heat for a tomato greenhouse at Hemnes (UNVERIFIED, snippet).
- **Unreconciled (DERIVED):** 55 kWh/kg × 80 kg/m²/yr (Frövi) = 4,400 kWh/m²/yr, about 7 to 10 times the 430 to 650 kWh/m² regional range of 1.4. At 430 to 650 kWh/m² the SINTEF figure implies only 7.8 to 11.8 kg/m²/yr of tomatoes. The sources do not say which yield the SINTEF case assumes, so the two cannot be reconciled from what was read.

### 2.6 Siberia, Kazakhstan
- **Sayuri, Yakutsk (SOURCED, MWM/Caterpillar reference sheet, October 2021):** pilot greenhouse of 1,000 m² December 2016; "By 2020, the greenhouse area was expanded to 3.2 ha"; planned 2021 output "some 1,250 t of cucumbers and about 230 t of tomatoes" (DERIVED: 1,480 t / 32,000 m² = 46 kg/m²/yr if all from 3.2 ha); on-site gas cogeneration: two 1-MW Cat gensets plus one MWM TCG 2020 V20 of 2,000 kW electric and **2,005 kW thermal** (electrical efficiency 43.5%, thermal 43.6%, total 87.1%), go-live August 2020; "temperatures of 60 °C below zero" in the first winter; energy costs "almost halved" against the local grid. **The total heat to the 3.2 ha and the heat per m² are not stated.** Also gives ground temperatures "from -50 to +50 °C."
- **Petropavlovsk, Kazakhstan (SOURCED, Hortidaily 8 Nov 2024):** 3.7 ha cucumber greenhouse heated by steam from the city's thermal power plant, target 3,000 t/yr (DERIVED: 81 kg/m²/yr), 10,742 lamps in winter. Heat quantity: NOT FOUND.
- **Norilsk (UNVERIFIED snippet):** a Nornickel "Polar Greenhouse Complex" set up March 2018, plan of 1,000 t/yr of vegetables; heat source **NOT FOUND**.

### 2.7 What limits waste-heat greenhouses (as stated)
Browns Ferry: water temperature, because greenhouse air stays within 10 to 12 °F of the water; capital and electricity for exchangers. Norway: "Heating accounts for roughly 40% of greenhouse operating costs" (UNVERIFIED snippet). Bruce: a steam price negotiated as a contract.

---

## 3. Q3: Aquaculture with power-plant heat

### 3.1 Cases
- **Tihange, Belgium (nuclear unit 870 MW on the Meuse).** SOURCED (Mélard, Philippart, Ruwet 1981 report, University of Liège page, opened): pilot farm built in 1980 by a private company; warm water "27-31 °C" above 21 °C for nine months (March to November), below 15 °C in winter, handled "with a closed storage circuit and conventional heating"; optimal tilapia growth 25 to 30 °C; **12 t in 1981**, goal 50 t/yr; "90-100 m³ of warm water (27-31 °C) per kg of tilapia"; about 0.5 kg per m³ of tank per day; market fish 300 to 350 g in 8 to 9 months from egg, all-male stock. UNVERIFIED (search summaries of other papers): the commercial farm Piscimeuse began in 1984, drew effluent at 1,800 m³/h, produced 136 t in 1986; 85 m³ per kg in one 1981 paper; early analyses found heavy metals and radionuclides in the fish "below the level permitted by law." **DERIVED check:** 1,800 m³/h × 8,760 h = 15.8 Mm³/yr ÷ 136,000 kg = 116 m³/kg, the same order as 85 to 100.
- **Japan (SOURCED abstract, INIS record of K. Mori, August 1983):** "Since 1963, research and development on aquaculture using this warm water has been carried out at some twenty power plants, seven nuclear and thirteen thermal, some of which are now in the commercial stage." Production figures: **NOT FOUND**. An older 1976 snippet lists sea bream, abalone, flatfish, prawn, eel at Tokai (UNVERIFIED).
- **Korea (UNVERIFIED, Asia Economy press reports, 2023 to 2025):** utility sites raise olive flounder and abalone in warm discharge water and release fry to the sea each year (Gori since 2000, Wolsong since 1999, Hanul 2026: 30,000 flounder and 20,000 abalone). These are utility press releases; yields and economics **NOT FOUND**.
- **Eskom, South Africa; Konin, Poland; Cherepovets, Russia; Ukraine (UNVERIFIED snippets):** catfish and tilapia studies in cooling water; carp, then sturgeon, at Konin on thermal-plant water since its founding; a caviar farm using the Cherepovets thermal station's cooling-system water on the Suda River; a 2024 Ukrainian paper on a sturgeon farm using energy-facility discharge. No yield per m³ or heat per kg in any snippet.
- **US (UNVERIFIED snippet):** tilapia in heated effluents, fingerlings reared in winter when open-cycle nuclear condenser water is 15 to 20 °C; a Utah catfish and tilapia study of coal-plant water; Tennessee Valley work. Numbers beyond that: **NOT FOUND**.

### 3.2 Heat needed per kg of fish
- No source stated heat per kg of fish at a power plant. Figures found are for recirculating systems (RAS): Norway smolt 5.1 to 12.8 kWh/kg on-site energy (mean 8.8) and grow-out "between 6 and 10 kWh per kilo live-weight" (UNVERIFIED snippet of a Norwegian study); modeled 15-week salmon grow-out 9.59 kWh/kg with "at least one-third" for thermal needs of freshwater; a 25-dataset review (2010 to 2024): freshwater systems 7.49 kWh/kg, saltwater 14.53; a Romanian source puts heating or cooling water at "40 ÷ 60% of the total energy" depending on winter (all UNVERIFIED snippets). Tilapia RAS in a PV study: 7.35 to 8.44 kWh/kg (UNVERIFIED, share for heating unknown).
- **DERIVED, illustrative:** thermal share 40 to 60% of 6 to 10 kWh/kg = 2.4 to 6 kWh of heat per kg, a rough bracket from weak inputs.
- **Flow-through (once-through) view (DERIVED):** at 90 to 100 m³/kg and a cooling-water temperature rise of 10 K (assumed, UNVERIFIED) each kg of fish needs 90 × 4.18 MJ/K/m³ × 10 K / 3.6 = 1,045 kWh of heat in the water flow, almost all of which leaves again; the heat actually consumed is far smaller. Not a published figure.

### 3.3 Yield per m³ and limits
- Tihange: 0.5 kg per m³ of tank per day in the 1981 abstract, which is a growth rate (11 g per m³ of water flowing per hour is the page's figure). Standing yield per m³ in a power-plant system: **NOT FOUND**.
- **Limits stated:** winter water below 15 °C needed supplementary heat; output depends on how many months the discharge stays above about 21 °C (Tihange) or 15 to 20 °C (Tennessee Valley); the 1974 Canadian review called for research on biological limits and year-round production.
- **Regulators' stance on nuclear plant effluent for fish farming:** **NOT FOUND** (two searches). Only context: Japan's tritium biological half-life "less than two days in fish" claim from a seafood trade outlet (UNVERIFIED) and the early Tihange compliance statement above. The Fukushima water release shows stakeholder opposition to nuclear effluent (UNVERIFIED snippet), which is not a statement about aquaculture.

---

## 4. Q4: Livestock, poultry, insects, soil

### 4.1 Poultry
- **SOURCED** (Finnish broiler house case study, *Agricultural and Food Science* 24(1), 2015, abstract opened): southern Finland, six flocks a year of 26,000 birds; heating "averaging 1.3 kWh kg⁻¹ of carcass weight"; electricity "0.08 kWh kg⁻¹"; heating highest in the cold period. Another table in the same paper (UNVERIFIED snippet) lists a Swedish house at 0.701 kWh/kg and theoretical values 0.75 (Helsinki) and 0.95 (Jyväskylä).
- **UNVERIFIED** (Government of Alberta factsheet in a search summary): "2279 Gigajoules (GJ) for a 50,000 head broiler operation," natural gas space heating. **DERIVED:** 2,279 GJ × 277.8 kWh/GJ = 633,000 kWh ÷ 50,000 = 12.7 kWh per bird per year; if the operation runs six flocks (the Finnish pattern, an assumption), 2.1 kWh per bird per flock.

### 4.2 Pigs
- **UNVERIFIED** (Alberta Agriculture and Prairie Swine Centre in search summaries): "608 GJ" of space-heating gas for a 500-sow farrow-to-wean operation (about 95% of the farm's gas). **DERIVED:** 608 / 500 = 1.216 GJ = **338 kWh of heat per sow per year**. Heat lamps "1,279 kWh per crate per year" versus efficient heat pads "383 kWh"; heat recovery cut gas use "about 70%," radiant heaters "about 40%." Irish audits: total farm energy 18 to 45 kWh per pig produced (mean 28), all uses.

### 4.3 Insects
- **UNVERIFIED** (Öko-Institut deck, search summary; the PDF returned 403): black soldier fly breeding at "28 to 30 °C," about 60% humidity, about 30-day cycle; a mass balance of "about 161 kWh of electricity and 3,404 kWh of heat per tonne of input" (input, not larvae). A German article: a five-chamber plant needs about 30,000 kWh of electricity and 240,000 kWh of heat per year, output not given. Larval metabolic heat varies with age and mass (a thesis, snippet).
- **Crickets, mealworms (heat per kg): NOT FOUND.**

### 4.4 Soil warming with pipes
- **UNVERIFIED** (extension guides and thesis snippets): hot-water root-zone systems run around 100 °F (38 °C); root-zone heat "will provide less than 25% of the total greenhouse heat needs on the coldest night"; a McGill thesis reports about 30% of the heat recovered from a soil heat-exchanger system went to a tomato crop; an Iraqi journal paper models power-plant waste heat in buried pipes at 20, 30 and 50 °C (results not read). The French 30 °C mulch and Cadarache outdoor soil heating are in 2.2.
- **Field-scale heat flux for warming open-field soil (W/m²): NOT FOUND.**

---

## 5. Q5: Heating demand of housing in extreme cold

### 5.1 Figures found
| Place | Figure | Status |
|---|---|---|
| **Fairbanks, Alaska** (Alaska Housing Finance Corporation, 2014 Alaska Housing Assessment, Fairbanks North Star Borough profile, opened) | Average home **1,844 ft²** (171.3 m²); overall row: annual energy use **247** million Btu, of which **space heating 188**, hot water 26, appliances 31; "143" kBtu/ft²/yr overall; the profile text says the home "uses 143,000 BTUs of energy per square foot annually, 4% more than the statewide average of 137,000"; heating index 7.7 Btu/ft²/HDD; climate zone "Zone 8 (12,600 - 16,800 HDD)". Newest homes (2005 or later): space heating 123 million Btu | SOURCED |
| Fairbanks, derived | space heating 188 million Btu × 0.293071 = 55.1 MWh per home per year = 6.3 kW average per home; ÷ 171.3 m² = **322 kWh/m²/yr**; total energy 143 kBtu/ft² × 3.1546 = 451 kWh/m². (The 143 kBtu/ft² × 1,844 ft² = 264 million Btu does not match the 247 in the same table, a difference the profile does not explain.) | DERIVED |
| **Sisimiut, Greenland (66.6°N)** (Vladyková and Rode 2011, 9th Nordic Symposium on Building Physics, opened) | heating degree hours (base 16 °C) 146.3 kKh/a (DERIVED: ÷ 24 = **6,096 K·days**), monthly mean −14.0 to 6.3 °C; Greenland building regulations (2006) maximum **185 kWh/m²/yr** for heating north of the Arctic Circle; "typical house is 230 kWh/(m²·a) (GBR, 2006)", dormitory Apisseq designed at **150**, a low-energy house targeted 80 | SOURCED |
| Sisimiut low-energy house, measured | "varied over the past 5 years from 139 to 150 kWh/(m²·a)", 90 in 2010; Greenland semi-detached houses 214 to 383 kWh/m² | UNVERIFIED (snippets) |
| **Iqaluit** | heating degree days "9540 °C" for 2016 (a demonstration house study); Pond Inlet "12,000 HDD" | UNVERIFIED (snippet) |
| **Yakutsk** | "average temperature in January -38 °C"; heating period "256 days with an average daily temperature of -21.2 °C" (**DERIVED:** with an 18 °C indoor base, (18 + 21.2) × 256 = about 10,000 K·days; base assumed); housing stock panel 30.6%, wood 29.2%. Heat per m²: **NOT FOUND** | UNVERIFIED |
| **Norilsk** | Nornickel energy report: combined heat-and-power plants "4,129 Gcal/h" plus boilers "511 Gcal/h" capacity (DERIVED: 4,640 Gcal/h × 1.163 MW per Gcal/h = **5,396 MW** of heat capacity, which serves the city and industry); per-person or per-m² heat: **NOT FOUND** | UNVERIFIED (snippet) |
| **Longyearbyen** | coal heat and power plant "11 MW electricity and 20 MW thermal"; population "about 1,750" in one presentation and "nearly 2,500" in a Barents Observer article; plant's last day October 19, 2023 (SOURCED, article opened); heat "about 75 percent" of the town's energy need once the mine closes (UNVERIFIED). **DERIVED:** 20 MWth ÷ 1,750 to 2,500 people = 8.0 to 11.4 kW of heat capacity per person, a capacity ratio including mine and commercial loads, not residential demand | partly SOURCED |
| **Nuuk** | district heating uses waste-incineration heat, electricity from the Buksefjord hydropower plant 56 km away; kWh per m² or per person: **NOT FOUND** | UNVERIFIED |
| **Alert** | **NOT FOUND**; only Nunavut totals (Iqaluit over 60 million liters a year for about 7,200 people, UNVERIFIED) | |
| **Antarctic stations per person** | Australian program electricity per person 46,100 to 51,390 kWh/yr (5.3 to 5.9 kW average), total fuel 6.4 to 7.1 ML/yr over all operations (UNVERIFIED, search summary; the report page failed to load); a Spanish study: Deception Island station living wing used 103.5 kWh/m² in 28 days (3.7 kWh/m²/day, UNVERIFIED); Concordia heat from cogeneration; Wasa station "does not require the use of additional heating" through generator heat recovery (UNVERIFIED). Per-person heat: **NOT FOUND** | |

### 5.2 Design temperatures
Fairbanks and Alaska: the AHFC zone is stated as HDD, a design minimum was not in what was read (UAF's −30 °F is a greenhouse example). Yakutsk January mean −38 °C (above). Russian code values (SP 131.13330, SP 50.13330) for Yakutsk and Norilsk: **NOT FOUND** (one search in Russian returned the structure of the standards only).

### 5.3 Heat pumps at very low outdoor temperature (all secondary reports, UNVERIFIED)
Oak Ridge field data in Alaska: "COP of 2 at -25 °C and 1.8 at -35 °C"; a Finnish field test of cold-climate models: at −30 °C COP "between 1.5 and 2" (Mitsubishi) and "between 1 and 1.5" (Toshiba); NRCan, Ottawa-area test house: "COP ranged from an average of 1.5 at -21.1 °C ... to 3.0 at +4.9 °C"; Minnesota field tests: "COPs between 1 and 2" below −12 °C; a review: near −30 °C heat pumps still ran about 1.5 times as efficient as oil or gas heating. The NREL field validation (OSTI 1973090, abstract opened) measured capacity and COP every 5 seconds at Northwest US sites but its COP values were not in the abstract. Defrost lowers COP near 0 °C.

### 5.4 Per-person heat, with the assumption stated
Floor area per person was not found in these sources; I assume **30 and 40 m² per person** (UNVERIFIED assumption, shown so it can be replaced). Space heating only (domestic hot water is separate; Fairbanks hot water 26 million Btu/home/yr = 7.6 MWh).
| Load, kWh/m²/yr | Source | per person at 30 m² | at 40 m² | average kW per person (30 / 40 m²) |
|---|---|---|---|---|
| 150 | Apisseq dormitory design | 4,500 kWh | 6,000 kWh | 0.51 / 0.68 |
| 185 | Greenland code maximum | 5,550 | 7,400 | 0.63 / 0.84 |
| 230 | Greenland "typical house" | 6,900 | 9,200 | 0.79 / 1.05 |
| 322 | Fairbanks measured-class average | 9,660 | 12,880 | 1.10 / 1.47 |
Fairbanks per home (not per person): 55.1 MWh/yr = 6.3 kW average per home.

---

## 6. Q6: Scale checks (all DERIVED, working shown)

Conversion: 1 kWh/m²/yr ÷ 8,760 h = 0.1142 W/m². 1 GWth for a year = 8.76 TWh of heat. Reject heat reference from the brief: about 2 GW of heat per GW of electricity; 324 GW net for the Tower plants (brief says about 600 GWth) and about 190 GW for the national grid.

### 6.1 Greenhouse area per GWth (heat load → area)
| Heat load | W/m² | km² per 1 GWth | km² per 10 GWth | km² per 100 GWth | km² per 600 GWth | Heat for the national growing area, 1,180 km² |
|---|---|---|---|---|---|---|
| 204 kWh/m²/yr (Dutch, fuel basis) | 23.3 | 42.9 | 429 | 4,290 | 25,800 | 27.5 GW |
| 430 (50 to 60°N low) | 49.1 | 20.4 | 204 | 2,040 | 12,200 | 57.9 GW |
| 650 (50 to 60°N high) | 74.2 | 13.5 | 135 | 1,350 | 8,090 | 87.6 GW |
| 2,170 (Magallanes model) | 247.7 | 4.0 | 40 | 404 | 2,420 | 292 GW |
Working: km² = 1e9 W ÷ (W/m²) ÷ 1e6. Example: 1e9 / 49.1 = 2.04e7 m² = 20.4 km² (2,040 ha). Peak Alaska design load (1,136 W/m²) would be about 0.9 km² per GWth at the single coldest hour.
- **Share of 600 GWth (DERIVED):** heating all 1,180 km² of national growing area as greenhouse: 27.5 / 600 = 4.6%; 57.9 / 600 = 9.7%; 87.6 / 600 = 14.6%; 292 / 600 = 48.7%. Note the repo's staple tier is indoor stacked farming, not greenhouse; for lit indoor farms see 1.2 (the lamps provide the heat; shell loss only).
- **Stacked layers:** for N layers, heated floor area falls to 1/N of the cultivation area, but lamp heat rises (EDEN ISS 800 W per m² of cultivation area, 19.2 kWh/m²/day).

### 6.2 People housed per GWth
From 5.4, 0.51 to 1.47 kW per person: **0.68 to 1.96 million persons per GWth** (1e9 W ÷ 510 W = 1.96 million; 1e9 ÷ 1,470 = 0.68 million), before distribution loss and hot water. For an illustrative 50 million people (the setting says tens of millions): 25.7 GW (150 kWh/m², 30 m²) to 73.5 GW (322 kWh/m², 40 m²). That is 4.3 to 12.3% of 600 GWth, or 13 to 39% of a 190 GWth national-grid plant. Per 1 million people: 0.51 to 1.47 GW.

### 6.3 Fish per GWth
1 GWth = 8.76 TWh/yr. At 2.4 to 6 kWh of heat per kg (a rough bracket from weak inputs, see 3.2): 8.76e9 kWh ÷ 6 = 1.46 Mt/yr to ÷ 2.4 = 3.65 Mt/yr of fish. This depends entirely on the 40 to 60% heating share and 6 to 10 kWh/kg RAS energy, both UNVERIFIED. Tomatoes at 55 kWh/kg (SINTEF): 8.76e9 ÷ 55 = 159 Mkg = **158,500 t/yr per GWth** (also = 100 GWh : 1,809 t scaled by 87.6); at 80 kg/m² (Frövi) that is 2.0 km² of greenhouse, versus 13.5 to 42.9 km² in 6.1 for the area-based loads, the unreconciled gap noted in 2.5.

### 6.4 Livestock heat per GWth
Broilers at 1.3 kWh/kg carcass (Finland): 8.76e9 ÷ 1.3 = 6.7 Mt carcass per year per GWth (heating only, Finnish climate). Pigs at 338 kWh per sow per year (Alberta): 8.76e9 ÷ 338 = 25.9 million sow-places per GWth.

### 6.5 Fraction of heat that stays with indoor-farm lamps
11.8 GW of farm electricity at 10 kWh/kg becomes about 11.7 GW of heat inside the buildings (1.2). For comparison, 6.1 shows the same area as a greenhouse would need 27.5 to 87.6 GW from outside.

### 6.6 Orbit food in heat terms (illustrative)
100,000 people in orbit × 0.66 t/yr = 66,000 t/yr. At the SINTEF tomato figure (55 kWh/kg): 66e6 kg × 55 = 3.63 TWh = **0.41 GWth** (0.07% of 600 GWth). At the fish bracket 2.4 to 6 kWh/kg: 0.02 to 0.05 GWth.

---

## 7. Q7: Food for orbit

### 7.1 Published per-person food mass (NASA)
- **SOURCED** (Frontiers in Space Technologies, DOI 10.3389/frspt.2024.1461389, published 15 January 2025, opened): "The required food mass ranges from 1.830 to 2.390 kg/CM-d, depending on the study"; "food mass excluding packaging estimated at 1.510 kg/CM-d"; packaged food supplied from Earth "2.161 kg/CM-d" plus food kits "0.055 kg/CM-d"; observed ISS food usage from October 2017 through February 2020 (882 days, average crew about 5.269) "2.77 kg/crew member per day"; food was "21% of the overall delivery mass"; "cargo transportation costs approximately $20,000 per kilogram," citing NASA (2018). (CM-d = crew member-day.)
- **SOURCED** (NASA, ASCEND 2023 logistics presentation, extracted): food packaging 0.40 kg/CM-d; dry mass as shipped 0.98 (non-EVA days) and 1.26 (EVA days); total packaged food 2.36 and 2.91; "BOBs" 0.03; total as shipped **2.39 (non-EVA) and 2.94 (EVA)** kg/CM-d; a table gives as-shipped mass by food hydration (50% hydration, 2.36 kg).
- **SOURCED** (Ewert and Stromgren, ICES-2019-126, NASA JSC, opened): the BVAD (Life Support Baseline Values and Assumptions Document), Table 4-53, "gives an average food supply planning value of 2.39 kg of individually packaged food delivered per person per day on the International Space Station"; "0.43 kg was subtracted for the packaging mass and then 0.20 kg (10%) was subtracted to account for food packages that are not opened and consumed" (DERIVED: 2.39 − 0.43 − 0.20 = **1.76 kg** of food consumed). It also assumes 0.2 kg of prepared food wasted per day.
- **UNVERIFIED** (NASA 2013 presentation in a search summary): "~3000 kcal/person/day + current primary packaging at a mass of 1.83 kg/crewmember/day." The kcal basis of the 2.39 kg figure is not stated in what was read.

### 7.2 Comparison with canon 0.66 t per human per year
Canon: 660 kg ÷ 365 = **1.808 kg/day** (DERIVED).
| NASA basis | kg/day | kg/year (× 365) | Canon 0.66 t is |
|---|---|---|---|
| 3,000 kcal with primary packaging (2013) | 1.83 | 668 | 1.2% lower |
| Food consumed after removing packaging and unopened food (Ewert and Stromgren) | 1.76 | 642 | 2.7% higher |
| Food excluding packaging (Frontiers) | 1.51 | 551 | 19.7% higher |
| BVAD packaged as shipped | 2.39 | 872 | 24.3% lower |
| Observed ISS use 2017 to 2020 | 2.77 | 1,011 | 34.7% lower |
Working: canon ÷ NASA annual mass − 1.

### 7.3 Earth-to-orbit cost and mass
- **SOURCED** as cited in the Frontiers paper: "approximately $20,000 per kilogram" (NASA, 2018, for ISS-type cargo). **DERIVED:** 872 kg/yr × $20,000 = $17.4 million per person-year; at the canon 660 kg, $13.2 million.
- **UNVERIFIED** (search snippets, aggregator sites; SpaceX's own page not retrieved): Falcon 9 list price $67 million (2022), $70 million (2025), $74 million (2026) for up to about 22,800 kg to low Earth orbit (22,000 kg on another sheet), about $3,000 to $3,250 per kg (DERIVED: $70M ÷ 22,800 = $3,070; $74M ÷ 22,800 = $3,245). At $3,070/kg, 660 kg/yr = $2.0 million per person-year (DERIVED). Prices to a settlement above low orbit were not found.
- **Published study of Earth-to-orbit food supply cost or mass beyond these:** **NOT FOUND.**

### 7.4 Space-habitat agriculture area
- SP-413 (NASA Space Settlements: A Design Study, 1977, Stanford torus, 10,000 people): the original agriculture chapter was not reached. **UNVERIFIED** (one secondary summary in a search result): "Agricultural sections: 20 m² per person." Other secondary figures conflicted widely (a forum post 150 to 200 m² per person). The NSS page opened has no area figure. **Primary NOT FOUND.** A 2023 arXiv paper (2302.12353) says NASA's studies assumed 15 m tall conventional farm space and re-estimates with short stacked shelves (UNVERIFIED snippet; per-person or whole-station basis unclear).
- For comparison from R1 (carried): NASA's Wheeler, about 50 m² of crop area per person for dietary calories under electric light.

---

## FINAL: what the sources support, do not support, and NOT FOUND

### What the sources support
1. **A lit indoor farm turns almost all its electricity into heat inside the building**: Cornell slides treat 117 W/m² of lamp power as 50 W/m² sensible plus 67 W/m² latent; lighting-to-food efficiency is about 1% (0.4 to 1.9%). In EDEN ISS (Antarctic) room heaters and similar equipment were 20% of use and cooling fans were off for four months. A stacked farm needs outside heat only for the shell and the dark period; Cornell's authors place the crossover at which plant factories beat greenhouses "somewhere in Alaska/Canada."
2. **Greenhouse heat loads**: about 204 kWh/m²/yr as fuel in the Netherlands (derived from 1.97e9 m³ over 8,490 ha); 430 to 650 kWh/m² at 50 to 60°N (snippet); about 2,170 kWh/m² for a modeled sub-Antarctic greenhouse. At 13.5 to 42.9 km² per GWth for the first three, 1 GWth is a few thousand hectares of greenhouse.
3. **Waste-heat greenhouses exist at modest scale**: Frövi, Sweden, 10 ha of tomatoes at about 80 kg/m²/yr on mill heat; Petropavlovsk, Kazakhstan, 3.7 ha on city power-plant steam; Sayuri, Yakutsk, 3.2 ha on gas cogeneration (2 MW thermal per large engine); France ran 30 °C water through soil mulch on several hectares of plant-heated land in the 1970s; Browns Ferry (US, 1979) grew tomatoes on condenser water and lost about 16% of yield to cold-water winter months. No fusion-plant case exists in the sources.
4. **Aquaculture on power-plant water**: Tihange tilapia needed 90 to 100 m³ of warm water per kg and supplementary heat when the water fell below 15 °C; Japan had research at about 20 plants by 1983 (seven nuclear).
5. **Poultry and pig heat**: Finnish broilers 1.3 kWh/kg carcass; Alberta sows about 338 kWh each per year.
6. **Housing heat**: Fairbanks measured about 322 kWh/m²/yr for space heating (188 million Btu per 1,844 ft² home); Greenland code maximum 185 and typical 230 kWh/m²/yr; at 30 to 40 m² per person that is 0.5 to 1.5 kW per person, or 0.7 to 2.0 million people per GWth.
7. **Food mass for orbit**: NASA planning values run 1.5 to 2.9 kg/person/day; the canon 0.66 t/yr (1.81 kg/day) matches the 1.83 kg (3,000 kcal with primary packaging) and 1.76 kg (consumed food) values within 3%, and is 24 to 35% below the ISS shipped and observed values.
8. **Launch cost to orbit**: about $20,000/kg (NASA 2018, as cited in a 2025 paper) for ISS-type cargo; roughly $3,000/kg at Falcon 9 list prices (aggregator snippets).

### What the sources do not support
- Any measured heat per m² for Bruce, Frövi, Sayuri, Petropavlovsk, Iceland or Kamchatka.
- That the Norwegian SINTEF tomato figure (55 kWh/kg) agrees with area-based greenhouse loads (they differ by about 7 to 10 times at the stated yield).
- Any use of fusion plant heat for farms, or any aquaculture-specific regulator statement about nuclear effluent.

### NOT FOUND (collected)
Annual Alaska/Iceland/Siberian greenhouse kWh/m²; vertical-farm shell loads in cold climates; Bruce Energy Centre greenhouse area, heat and years; Tricastin greenhouse figures; heat per m² and yields for Iceland, Kamchatka and Frövi (MW or GWh); heat per kg of fish at a power plant; standing yield per m³ in power-plant fish systems; Korean and Japanese production numbers; regulators' stance on nuclear effluent for fish farming; cricket and mealworm heating; field-scale soil-warming W/m²; Yakutsk, Norilsk, Nuuk, Iqaluit, Alert residential kWh/m² and per person; Russian code design temperatures; Antarctic station heat per person; floor area per person; SP-413 agriculture chapter and a primary per-person area; any dedicated study of Earth-to-orbit food supply; fusion or nuclear heat for housing (belongs to unit P2).

### Pages that failed and were not worked around
hub.ifdc.org (timeouts, twice); ntnu.no/bridge (404); s-vfu.ru (SSL error); e3s-conferences.org (403); soe.dcceew.gov.au (socket hang up); ccacoalition.org (403); nature.com Kusuma 2020 (redirect to a login host); electricityforum.com (page held a different article); pellet.org Arctic district heating slides (PDF fetched but not text-extracted; not read). No search was refused by the search tool; no STOP note was needed.

**Ended:** 2026-11-02 21:20 (shell clock).

---

## Search log

Format: number, tool, exact query or URL, result (hit = read at the source; partial = snippet or incomplete; miss), and where a miss died. WebSearch used "standard" mode throughout.

1. WebSearch "vertical farm energy balance lighting heat released into room cooling load dehumidification share of electricity" | partial (Montreal group, arXiv leads)
2. WebSearch "greenhouse heating energy demand cold climate Alaska Iceland kWh per m2 per year heating share of energy" | partial (Energies 2023, Magallanes)
3. WebSearch "Bruce Energy Centre Ontario greenhouse waste steam nuclear Bruce Power heat greenhouses hectares" | partial (1997 transcript lead)
4. WebSearch "Bruce Energy Centre history Tiverton Ontario Hydro steam greenhouse ethanol plant nuclear process steam 1980s" | partial
5. WebSearch "OCAP CO2 Netherlands greenhouses residual CO2 pipeline hectares Shell Pernis heat greenhouses" | hit (CO2 only)
6. WebSearch "Netherlands greenhouse horticulture heat demand 2022 energy use PJ per hectare CHP share Statistics Netherlands" | partial
7. WebSearch "Iceland geothermal greenhouses area hectares energy use heat per m2 tomatoes cucumbers lighting Orkustofnun" | partial (low-reliability numbers)
8. WebFetch glastuinbouwnederland.nl Key_Figures_Greenhouse_Horticulture_Sector_2026.pdf | hit via saved PDF and pdftotext
9. WebFetch hortidaily.com/article/9680843 | partial (percentages only)
10. WebFetch tomatoworld.nl OCAP factsheet PDF | hit via pdftotext
11. WebSearch "Tricastin nuclear plant waste heat greenhouse Pierrelatte tomatoes hectares EDF serres chaleur fatale" | partial (French program leads)
12. WebSearch "greenhouse heated by nuclear power plant waste heat condenser cooling water greenhouse experiment tomatoes IAEA" | hit (Browns Ferry, OSTI)
13. WebSearch "Kamchatka geothermal greenhouses Paratunka heat vegetable production hectares" | partial
14. WebSearch "industrial waste heat greenhouse Norway Finland tomato greenhouse low temperature heat supplied by factory MW hectares" | partial (SINTEF, Frövi)
15. WebFetch osti.gov/biblio/5027502 | hit
16. WebFetch osti.gov/biblio/6272979 | hit
17. WebFetch sintef.no HighEFF utilizing low temperature surplus heat | hit
18. WebFetch selectedgroup.dk Frövi | partial (no heat figure)
19. WebFetch billerud.com press release 2021 | partial
20. WebSearch "aquaculture power plant thermal effluent tilapia shrimp heated discharge water fish farm yield kg per m3 review" | partial
21. WebSearch "recirculating aquaculture system energy use heating kWh per kg fish salmon tilapia sturgeon cold climate" | partial
22. WebSearch "Korea Japan power plant warm water discharge fish farming flounder eel nuclear plant thermal effluent aquaculture utilization" | partial
23. WebFetch hub.ifdc.org/handle/20.500.14297/2059 | miss (timeout)
24. WebFetch inis.iaea.org/records/5krpc-sjv97 | hit (abstract)
25. WebFetch ntnu.no/bridge/node/22667 | miss (404)
26. WebSearch "tilapia nuclear plant heated effluent Tihange Belgium fish farm Tihange tonnes per year cooling water" | hit (partial numbers)
27. WebFetch popups.lib.uliege.be/2984-0317/index.php?id=670 | hit
28. WebFetch hub.ifdc.org/items/23ded0d4-... | miss (timeout)
29. WebSearch "heat demand poultry broiler house cold climate kWh per bird propane Canada Alberta heating energy broiler barn" | partial
30. WebSearch "pig barn heating energy per sow per year farrowing room heat demand cold climate kWh per pig place Canada" | partial
31. WebSearch "Yakutsk Norilsk heating degree days design temperature heat consumption per m2 per year residential kWh/m2 district heating Siberia" | partial
32. WebSearch "Greenland Nuuk Longyearbyen Iqaluit Alert residential space heating energy kWh per m2 per year heating degree days" | partial
33. WebSearch "Fairbanks Alaska home heating energy use per household MMBtu per year heating degree days 14,000 energy per square foot" | partial (led to AHFC)
34. WebSearch "air-source heat pump coefficient of performance at -30 C -25 C field measurements cold climate heat pump Alaska Yukon Nordic" | partial
35. WebFetch backend.orbit.dtu.dk (Vladyková and Rode 2011) | hit via pdftotext
36. WebFetch s-vfu.ru Slobodchikov_2020 | miss (SSL error)
37. WebFetch e3s-conferences.org esr2021_04004 | miss (403)
38. WebFetch osti.gov/biblio/1973090 | partial (abstract, no COP values)
39. WebSearch "NASA Baseline Values and Assumptions Document food mass per crew member per day kg dry food packaging calories 2500 kcal" | hit
40. WebSearch "ISS resupply food mass per astronaut per day kg including packaging cost of launching food to orbit per kilogram" | hit
41. WebSearch "space habitat O'Neill cylinder food production area per person agricultural land per person study Stanford torus 1975 NASA SP-413 agriculture" | partial
42. WebFetch frontiersin.org/articles/10.3389/frspt.2024.1461389/full | hit
43. WebFetch ntrs.nasa.gov ASCEND2023 logistics PDF | hit via pdftotext
44. WebFetch ntrs.nasa.gov/api/citations/20190027563 (Ewert and Stromgren) | hit via pdftotext
45. WebSearch "Antarctic station energy use per person per year kWh heating share fuel liters per person station McMurdo Halley Neumayer Concordia heating demand kW" | partial
46. WebSearch "Longyearbyen district heating coal power plant heat demand MW population energy per capita Svalbard heat consumption" | partial
47. WebSearch "Norilsk heat supply Gcal per year thermal energy consumption per capita Norilsk Nickel heating network Taimyr" | partial
48. WebSearch "Nuuk district heating waste heat incineration hydropower heat demand GWh per year Nuuk heating oil Greenland household heating energy" | partial
49. WebFetch soe.dcceew.gov.au human-environment | miss (socket hang up)
50. WebFetch thebarentsobserver.com Longyearbyen plant | hit
51. WebFetch pellet.org Arctic district heating slides PDF | miss (binary, not extracted)
52. WebSearch "Konakovo power station sturgeon farm warm water cooling Russia aquaculture thermal power plant sturgeon cage" | partial
53. WebSearch "insect farming energy heating requirement black soldier fly larvae rearing temperature 27 C kWh per kg cricket farm heating energy use" | partial
54. WebSearch "soil heating buried pipes warm water root zone heating greenhouse W/m2 required soil warming field crops waste heat power plant cooling water irrigation" | partial
55. WebSearch "Siberia Yakutia Norilsk greenhouse heating winter energy greenhouse complex vegetables heated by thermal power plant hectares tonnes" | partial
56. WebFetch mwm.net Sayuri reference sheet | hit via pdftotext
57. WebFetch hortidaily.com/article/9676177 | hit
58. WebFetch ccacoalition.org Oeko-Institut Black Soldier Flies | miss (403)
59. WebSearch "Naseer Tromsø greenhouse tomato year-round LED energy use kWh per m2 heating electricity Norway Arctic greenhouse study" | partial (abstract only)
60. WebSearch "Alaska greenhouse heating fuel use winter Fairbanks greenhouse energy BTU per square foot year-round production study" | partial
61. WebSearch "plant factory LED lighting heat load fraction of electrical input converted to heat sensible latent heat transpiration cooling load per m2 vertical farm heat recovery heat pump" | partial
62. WebFetch nature.com/articles/s41438-020-0283-7 | miss (login redirect)
63. WebFetch controlledenvironments.org Kale Harbick | hit via pdftotext
64. WebFetch arxiv.org/pdf/2603.15806 | hit via pdftotext
65. WebSearch "нормативный удельный расход тепловой энергии на отопление жилых зданий Якутск кВт·ч/м2 в год градусо-сутки отопительного периода СП 50.13330" | miss (standards' structure only; died at the query/sources)
66. WebSearch "Concordia station Halley VI Princess Elisabeth heating power kW generator waste heat recovery energy consumption per person winter station Antarctica" | partial
67. WebSearch "nuclear power plant thermal discharge aquaculture regulatory acceptance tritium radioactivity fish farm cooling water consumer perception regulator" | miss for the aquaculture angle (context only)
68. WebSearch "Bruce Energy Centre Tiverton greenhouse Bruce Power steam Energy Centre tenants Ontario Hydro heat sold to alfalfa dehydration ethanol greenhouse history ended" | miss (died at sources)
69. WebFetch electricityforum.com planwillhelpcentercutcosts | miss (different article)
70. WebFetch ola.org committee transcript 1997-oct-30 | hit (first 100,000 of 159,432 characters)
71. WebSearch "NASA SP-413 Space Settlements design study agriculture area per person food production 1975 chapter agriculture Stanford torus crop area" | partial
72. WebFetch nss.org/stanford-torus-space-settlement | miss (no area data)
73. WebFetch journal.fi/afs/article/view/48012 | hit (abstract)
74. WebSearch "Falcon 9 price per kilogram to low Earth orbit SpaceX capacity page 22,800 kg standard launch price 2025" | partial (aggregators)
75. WebSearch "tilapia recirculating aquaculture heating requirement kWh per kg fish water temperature 28 C cold climate energy for heating water RAS heat loss building" | miss for heating kWh/kg
76. WebSearch "Alert Nunavut Canadian Forces Station Alert fuel consumption litres per year population heating energy per person 82 N" | miss (Alert specific)
77. WebFetch ahfc.us/download_file/view/9034/796 (Fairbanks North Star Borough, 2014 Alaska Housing Assessment) | hit via pdftotext
