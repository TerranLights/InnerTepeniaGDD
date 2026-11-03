# Heat unit P2: cogeneration and long-distance heat transport (research, 2026-11-02)

**Started:** 2026-11-02 21:08 (local). **Ended:** 2026-11-02 21:22 (local).

**Scope.** Facts only; no recommendation, no design, no ranking. Seven questions from `Power_Plant_Heat_Research_BRIEF_2026-11-02.md` Unit P2: nuclear district-heating precedents; long-distance hot-water transport; the electricity penalty; polar and permafrost installation; Antarctic uses of plant and generator heat; seasonal storage and demand matching; melting ice for water. Rules 1 to 8 of the Fusion and Helium-3 brief apply. Already sourced in `Tepenia_Nuclear_Power_Logistics_Research_2026-11-02.md` §4.4 (not restated unless improved): Haiyang 23 km line, 83 km network, 12.5 million m2, CNY 4 billion; Qinshan first phase; Bilibino "up to 25 Gcal/h" (UNVERIFIED there); Lomonosov/Pevek 586 GJ/h; Russian pipe lengths NOT FOUND there.

**How the labels are used in this file.** SOURCED = I read the figure in a page, PDF or document fetched in this session (WebFetch returns a small-model summary of the page; two PDFs were saved and read as text with `pdftotext` in my scratch folder, which is marked below). UNVERIFIED = the figure appears only in a web-search result summary, was recalled, or comes from a blog, vendor or encyclopedia page. DERIVED = my arithmetic, working shown. NOT FOUND = looked for, queries in the log. Heat conversions: 1 Gcal = 4.1868 GJ; heat capacity of hot water taken as 4.2 kJ/(kg K) (the value used in the EPRI brief's footnote) unless stated.

## PROGRESS
- [x] Q1 Nuclear district heating precedents (gaps: Loviisa, Bruce, Bohunice MW, Qinshan, Pevek temperatures)
- [x] Q2 Long-distance hot-water transport (gaps: measured pumping power, cost per km at the longest lines)
- [x] Q3 Electricity penalty and temperatures (gap: combined-cycle extraction penalty)
- [x] Q4 Polar and permafrost installation (gap: outage and freeze-up statistics)
- [x] Q5 Antarctic precedents (gaps: Pole heat-recovery kW, Concordia kW)
- [x] Q6 Seasonal storage and demand matching (gap: BTES loss percent, summer share of demand)
- [x] Q7 Heat to water (ice melting)
- [x] FINAL

---

## Q1. Nuclear district-heating precedents

### 1.1 The best single source: EPRI Technical Brief, June 2022 (SOURCED, read as text)
*Current and Past Use of District Energy Using Nuclear Power: A Review of Nuclear District Energy Facilities* (EPRI, Technical Brief, June 2022; PDF fetched and read with `pdftotext`; scratch copy only). It reviews **27 facilities in 11 countries**, and says "in 2019, there was a combined total of 750 reactor years of experience in cogeneration." Its general statements:
- District energy networks "typically require heat within 80-130 C for the supply line ... and 45-70 C for the return line."
- Cycle efficiency 33-37% without extraction; cogeneration "overall thermal efficiency ... could be increased by more than 30%."
- Closest plant-to-network distance about 2 km (Cernavoda, Muhleberg); farthest Kola, "the furthest served town's boundary at 64 km away (the most remote consumer is 72 km away from the NPP)." "It is expected that nuclear heat can be delivered up to 150 km away in the form of hot water at a competitive price" (the brief's own citation [10]).
- All facilities use an independent loop (tertiary loop) so that radiological separation is kept; PWR/PHWR plants take steam from the secondary loop through a heat exchanger.
- Reliability: refueling every 18-24 months stops heat; multi-unit plants stagger outages; single-unit plants use backup (Beznau: oil-fired package boilers). Beznau varies supply temperature with season: "125 C in winter and 80 C in summer."
- Highest operating pressure: Greifswald, 2.86 MPa, 2,600 t/h, 180 C maximum.

### 1.2 Appendix table (SOURCED, EPRI Table A-1; figures as the brief states them)
| Plant (country) | Heat/size as stated | Distance / pipe | Supply / return | Years of operation (heating) |
|---|---|---|---|---|
| Haiyang (China), 2 x AP1000 | "Heat for at least 700,000 m2 of housing" (2019-2021 stage); steam from secondary loop to multistage exchanger on site | municipal pipes (no length given) | N/A | units 2018/2019 to present; district heating 2019 to present |
| Temelin 1, 2 (Czechia) | town Tyn nad Vltavou | 5 km | 153 C / 67 C | 2002/2003 to present |
| Greifswald 1-5 (East Germany) | **260 MWth** | **22 km, 800 mm pipe** | up to 180 C, 2.86 MPa | 1974-1990 |
| Paks 1-4 (Hungary) | town of Paks | 6 km | 130 / 70 C | 1983-1987 start to present |
| Bilibino 1-4 (Russia) | plant and town hot water | 3.5 km to the Bilibino network | 150 / 70 C, 1.81 MPa, 207-309 t/h | unit 1 1974-2019, others to present |
| Cernavoda 1, 2 (Romania) | town about 20,000 inhabitants; 60,500 MWh delivered in 1999; steam 80 t/h | about 2 km | 150 / 70 C | 1996/2007 to present |
| Kozloduy 5-6 (Bulgaria) | **20 MWth** | local network | 150 / 70 C | 1988/1993 to present |
| Balakovo 1-4 (Russia) | "Heat requirement is over 1000 MWth" | 12 km | 130 / 70 C | 1986-1993 start to present |
| Kalinin 1-4 | local area | 4 km main | 130 / 70 C | 1985 to present |
| **Kola 1-4** | nearby areas | **64 km main pipeline** | 130 / 70 C | 1973 to present |
| Kursk 1-4 (RBMK) | local area | 3 km | 130 / 70 C | 1977 to present |
| Leningrad II-1,2 | Sosnovy Bor, "more than 65,000 residents" | 5 km | 80-130 / 45-70 C (generic) | 2018/2021 to present |
| **Novovoronezh 3, 4** | nearby areas | **50 km** | 130 / 70 C | 1972/1973 to present |
| **Novovoronezh II-1,2** | distribution | **55 km** | 80-130 / 45-70 C (generic) | 2017/2019 to present |
| Smolensk 1, 2 (RBMK) | local | 5 km | 130 / 70 C | 1983 to present |
| Beloyarsk | plant site and adjacent living areas | 3-15 km | 130 / 70 C | 1964 to present |
| Agesta (Sweden, PHWR) | suburb Farsta, **55 MWth load** | about 5 km | 78-115 / 55-60 C, 2,400 t/h | 1964-1974 |
| **Beznau 1, 2 (Switzerland)** | Refuna network | **35 km main, 85 km local distribution** | 1.6 MPa, 80-125 C / 50 C | heating started 1983/1984 |
| Gosgen (Switzerland) | 232 GWh_th per year for all heating; 1.8 km steam line to cardboard mill, extended to Niedergosgen and Schonenwerd | | 120 / 70 C (district); process steam 1.2 MPa, 220 C | process steam from 1979, district heating from 1996 |
| Muhleberg (BWR, Switzerland) | 1,700 MWh_th consumed in 2008; 4.4 L/s | 2 km | 125 / 65 C | short-lived (plant 1972-2019) |
| NHR-5 (Tsinghua, China) | 740,000 m2 campus; 152 t/h | | 84 / 56 C | 1989-1992 (three winters), availability >99% |
| Whiteshell SLOWPOKE-3 (Canada) | demonstration | | under 100 C | 1987-1990, ended because of low gas prices |
| Gorky and Voronezh AST-500 (Russia) | **designed for up to 2,300 MW; towns of 350,000-400,000** | | 150 / 70 C, 1.6 MPa | **never operated** |

The EPRI brief gives cost only for plants, not for the heat systems (for example "$815 million (750 million Swiss francs)" for Beznau is the plant).

### 1.3 Other plants named in the brief
- **Beznau (Refuna).** Beyond EPRI: Kavvadias and Quoilin 2018 (Q2) say Beznau "supplies 81 MW of heat through a 31 km main pipeline" (SOURCED, citing a Swiss reference); the EPRI bibliography lists a paper titled "75 MW Heat Extraction from Beznau Nuclear Power Plant" (title SOURCED). Search summaries: a Norwegian encyclopedia says 80 MW can be extracted (UNVERIFIED); 1989 connected capacity 55,000 kW with 1,500 connections in eleven municipalities (INIS abstract, UNVERIFIED); Nuklearforum reports (2012 and 2013) give heat delivered by the two blocks of 188.3 million kWh (2012) and 200.0 million kWh (2013) (UNVERIFIED, snippet); today about 2,600 customers (Swissnuclear, SRF; UNVERIFIED); Axpo plans to close Beznau "um 2030" and Refuna and Axpo plan a wood-fired heating plant at Doettingen as a replacement (SRF, UNVERIFIED). DERIVED: 200 GWh per year / 8,760 h = 22.8 MW average thermal power.
- **Temelin to Ceske Budejovice (a new long line, 2023).** SOURCED (oEnergetice 18 Oct 2023; CEZ press release 22 Oct 2026): two parallel pipes, each **26 km**, outside diameter 80 cm, buried at least 1.3 m; cost **CZK 1.69 billion**; planned **750 TJ per year** for at least 20 years; heat first delivered October 2023; covers about one third of the city's heat. CEZ (22 Oct 2026): **719,000 GJ** delivered in the latest year (October to September), "nearly 2.1 million GJ" in three years, about 2,500 GJ per day, water leaves the plant "just over 100 C". Design parameters from a search summary of the designer's presentation (UNVERIFIED; the presentation URL returned 404): two pipes DN700, 2.5 MPa, nominal flow 2,403 t/h, winter 142/65 C, summer 80/60 C. DERIVED: 2,403 t/h = 667.5 kg/s; x 4.2 kJ/(kg K) x 77 K = **216 MW** design thermal power (matches a reader comment of about 210 MW in the oEnergetice thread, itself unverified); 719,000 GJ/yr = 22.8 MW annual average; 750 TJ / 216 MW = about 965 full-load hours; CZK 1.69 billion / 26 km = CZK 65 million per route-km (for the pair).
- **Temelin to Tyn nad Vltavou.** SOURCED (CEZ 2026): supplied since 1998, "over 5 million GJ in nearly three decades", allowing 22 coal boilers and three large boiler houses to shut. EPRI gives 5 km, 153/67 C.
- **Dukovany to Brno (planned).** SOURCED (oEnergetice): **42 km** through 14 municipalities, estimated **CZK 19 billion**, contractor expected around Q2 2027, nine gas boiler houses to be replaced by 2031, about half of Brno's heat demand eventually; considered in the 1980s and shelved for low gas prices. WNN (20 Aug 2010): Dukovany 5,500 MWth, 1,760 MWe (DERIVED efficiency 32%), "more than 40 km."
- **Mochovce (Slovakia, planned).** SOURCED (oEnergetice/WNN, 20 Jan 2025): hot water to Tlmace (about 4,000 people, about 6 km), implementation 2027, completion early 2028; "Bohunice has had municipal heating schemes operating since 1987."
- **Bohunice (Slovakia).** Search summaries (UNVERIFIED): pipeline to Trnava about 10-15 km (sources disagree), commercial operation 10 December 1987, branch to Leopoldov and Hlohovec, 429 GWh of heat in 2023, a source calls the line unprofitable in the long run. MW: **NOT FOUND**.
- **Paks (Hungary).** EPRI: town 6 km, 130/70 C. Search summary (UNVERIFIED): "district heating license ... only 42 MW of thermal capacity"; a Budapest-Paks pipeline study (about 100 km) is under way (WNN headline SOURCED as a title; details UNVERIFIED).
- **Loviisa (Finland).** No current district-heat delivery found. Kavvadias and Quoilin (SOURCED): Fortum's study for the proposed Loviisa 3 unit found heat "to be transported to the eastern Helsinki, which is about 80 km away, can reach 1 GW" (site about 75 km east of Helsinki); the Loviisa 3 application was refused on 21 April 2010 (search summary, UNVERIFIED).
- **Bruce Energy Centre (Ontario).** Only that it was set up to market surplus steam from the Bruce nuclear site, with a distillery tenant (search summaries, UNVERIFIED). Thermal MW, distance and temperatures: **NOT FOUND**.
- **Haiyang (more).** POWER magazine (SOURCED, article about the 2019-2021 stage): phase 1 700,000 m2 from November 2019; phase 2 adds 4,500,000 m2; 300-400 TJ per year planned (DERIVED average 9.5-12.7 MW); cycle thermal efficiency up 3.25% after phase 2; a 500 MWh storage planned. NEI (26 Nov 2024, SOURCED): "heating capacity ... started at 31.5 MW and now reaches **1,134 MW**", nearly 13 million m2 (DERIVED: 1,134 MW / 13 million m2 = **87 W per m2**), over five winters 9.01 million GJ, 810,000 t of coal saved. WNN (27 Nov 2023, SOURCED): 23 km line, 12.5 million m2, about 400,000 people, 4.56 million GJ to date. Search summaries (UNVERIFIED): a plan for a "900 MW" long-distance cross-region project with a new backbone of about **120 km**, 30 million m2, about 1 million people; cumulative 14.32 million GJ by November 2025 (Chinese source); a conference paper says Haiyang high-pressure-exhaust extraction is 300 t/h and "affects the output of the unit by about 50000" (unit cut off in the snippet), and an AP1000 paper says 1,000 t/h of extraction corresponds to 600 MW of heat. If the 600 MW per 1,000 t/h holds, 300 t/h = 180 MWth (DERIVED); the lost-output unit is unconfirmed.
- **Qinshan.** Search summary (UNVERIFIED): 130 C supply, 70 C return. Pipe length, MW: **NOT FOUND**.
- **Bilibino and Pevek.** Search summaries (UNVERIFIED): Bilibino installed thermal capacity 66 Gcal/h (DERIVED 76.8 MW; matches the "78 MWt" in the earlier file), 49.5 Gcal/h after one unit's shutdown (57.6 MW); the town's only heat source. EPRI (SOURCED): 3.5 km to the Bilibino network, 150/70 C. Akademik Lomonosov 70 MWe and 50 Gcal/h (DERIVED 58 MW) in several reports (UNVERIFIED); earlier file has 586 GJ/h (163 MW) from WNA (SOURCED there). The two figures still do not reconcile.
- **IAEA totals (UNVERIFIED, news summary):** about 43 reactors supply district heat, about 5,000 MWth in total, per-reactor outputs 5-240 MWth; EU nuclear share of district-heating heat 0.17% in 2014.

**What was lost in electricity, per plant:** see Q3 (a measured loss per MWh of heat is NOT FOUND for any named plant; Beznau cumulative lost production is reported but mixed with industrial customers).

---

## Q2. Long-distance hot-water transport

### 2.1 The longest lines
- **Melnik to Prague (Czechia), SOURCED (CEZ press release "30 years", 1995-2025):** two pipes of 1.2 m diameter; **34 km** from Melnik to Treboradice; up to 2.5 MPa; supply 90-140 C by season, return 55-65 C; temperature drop in transit under 1 C over an average 8-hour transit; flow over 2 m/s at full load; "losses ... usually do not exceed 4%"; operation since 1995 (construction from 1988); about 250,000 customers in Prague, Melnik and Neratovice; farthest consumer **74.5 km** from the heating plant; two Vltava crossings and four railway crossings. An earlier search summary gave the Energotrans heat plant maximum 650 MWt (UNVERIFIED). Kavvadias and Quoilin call it "the longest bulk heat transmission distance in Europe", with a line length of 67 km for a direct distance of 32 km, "for a large part above ground" (SOURCED; the 67 km and the 34 km figures differ, possibly because 67 km counts both pipes, 2 x 34 km; this is my inference, UNVERIFIED).
  - DERIVED: 4% / 34 km = **0.12% per km** (if the 4% refers to the whole feeder; the sentence is ambiguous). 34,000 m / (8 x 3,600 s) = 1.2 m/s mean transit speed, against "over 2 m/s" at full flow. Order of magnitude of one pipe at 2 m/s: area pi/4 x 1.2^2 = 1.13 m2; 2.26 m3/s x 950 kg/m3 x 4.2 kJ/(kg K) x 80 K = about 720 MW (taking the nominal diameter as the bore; actual bore is smaller, so this is an upper bound).
- **Temelin to Ceske Budejovice:** 26 km, see Q1.
- **Dukovany to Brno:** 42 km, planned, CZK 19 billion.
- **Kola NPP:** 64 km main pipeline (EPRI, SOURCED); Novovoronezh 50 km and Novovoronezh II 55 km (EPRI). Independent confirmation of the Kola figure: **NOT FOUND** (search summary found only that the plant is about 12 km from Polyarnye Zori and that an Apatity nuclear-heating project was studied in 1998).
- **Tuoketuo to Hohhot (China):** 68.4 km, described as "Asia's longest heat supply pipeline" (SASAC; search summary only, the page itself failed with an SSL error; UNVERIFIED). Taiyuan-Gujiao and other Chinese lines: **NOT FOUND**.
- **Kavvadias and Quoilin 2018, Table 1 (SOURCED; operational in 2016):** heat capacity / length (km) / mean diameter (mm): Linkoping-Mjolby 25 MW / 28 km; Oslo 275 MW / 13 km / 600; Helsinki 490 MW / 20 km / 1,000; Turku 340 MW / 25 km / 800; Tilburg 170 MW / 25 km / 500; Diemen-Almere 260 MW / 8.5 km / 700; **Akranes (Iceland) 60 MW / 62 km / 400**; Sankt Poelten 50 MW / 31 km / 425; Lippendorf-Leipzig 300 MW / 15 km / 800; Mannheim-Speyer 40 MW / 21.2 km / 300; Zolling-Munich airport 150 MW / 28 km / 500; **Nesjavellir-Reykjavik 290 MW / 27 km / 800**; Kozani 137 MW / 16.5 km / 500; Aachen 85 MW / 20 km. (Oradea, Romania: the row prints two numbers, 546 and 86.3, and the text extraction does not show which is the length; not used.) Their reading: "current heat pipelines rarely exceed 30 km in length, with an observed maximum of 60 or 70 km." Other lines they cite: Helsinki Vuosaari about 30 km tunnel; Aarhus 20 km to the center, 45 km to the other end, 130 km total transmission network; Beznau 81 MW over 31 km.
- **Feasibility studies cited by Kavvadias and Quoilin (SOURCED as citations):** a 150 km main line with "losses ... less than 2% of the total transported power" (Safa); Loviisa to eastern Helsinki about 80 km, 1 GW; William Orchard Partners London: **2 GW over 140 km using 2 x 2 m pipes**, delivered-heat cost about 0.0035 EUR per kWh, "Heat loss was 35 MW and the pumping losses 50 MW." DERIVED: 35/2,000 = 1.75% heat loss over 140 km = 0.0125% per km; 50/2,000 = 2.5% pumping (units as the source gives them).
- **POWER magazine (1 March 2022, SOURCED):** "it may be economical to transport hot water as far as 100 miles to cities with heat loads of 1,500 MWth to 2,500 MWth"; "60-inch pipes carry about 2,400 MWth; 40-inch pipes carry about 700 MWth"; supply "up to 400F" has been considered for long transport; "Adding provisions for a 1,500 MWth heat supply to a 1,000 MWe plant will generally increase plant cost by less than 5%"; heat densities below 90 MWth per square mile are generally not economical.

### 2.2 Published limits and the distance formula
Kavvadias and Quoilin (Applied Energy 216, 2018, 452-465; PDF read as text; SOURCED):
- Heat flux: "~0.5 MW/mm2 for a high voltage direct current line vs. ~0.001 MW/mm2 for heat transmission lines."
- "Typical heat distribution losses vary between 4% and 20%, depending mainly on the linear heat density"; electricity transmission and distribution losses average 8.2% worldwide.
- Earlier literature thresholds they list: flat 10 km (UK industry), heat up to 40 km, a linear function with an upper limit of 30 km (Persson), water at 90-175 C over 30 km versus steam over 3-5 km (Ammar), a break-even of 86.5 km for 62 MW assuming 1% of heat lost per km (Kapil, pumping excluded). EU member states' thresholds under Energy Efficiency Directive Art. 14.6: 3 to 20 km (Table 2).
- Their model result: "most literature sources use a common threshold ... in the range of 30-50 km"; their techno-economic model "suggests that longer distances are feasible"; "the maximum delivery distance is proportional to the square root of the amount of heat transmitted" (power-law exponent 0.45 to 0.55). Fitted constant alpha (Table 7), with distance in km = alpha x sqrt(heat in MW): supply 100 C: alpha = 1.0, 3.3, 5.4, 7.5 at heat selling prices 20, 40, 60, 80 EUR/MWh; supply 50 C: 1.21, 2.59, 3.95, 5.29. Model assumptions (their Table): supply 100 C, return 30 C, soil 15 C, insulation conductivity 0.05 W/(m K), capacity factor 40%, lifetime 20 years, discount rate 12%, wholesale electricity 80 EUR/MWh. (The printed equation is garbled in the PDF text; I used the highlights and conclusions, which state the square-root form.)
  - DERIVED maximum feasible distance = alpha x sqrt(MW), taking alpha = 3.3 (40 EUR/MWh) and 7.5 (80 EUR/MWh) at 100 C: 100 MW gives 33 and 75 km; **600 MW gives 81 and 184 km**; **1 GWth (1,000 MW) gives 104 and 237 km**. For 10 GWth the formula gives 330 and 750 km, and for 100 GWth and 600 GWth it gives about 1,000-2,400 km and 2,500-5,800 km. Those last values are far outside any project in the paper (largest cases a few GW) and the paper's fit range is not stated in the text I read; treat anything beyond about 2 GW as an extrapolation of the formula, not a published result. These are European 2018 prices and a 12% discount rate, not Antarctic conditions.
- Pipe cost approximations quoted: 436 EUR/m (Svensson, 30 km), USD 1,460/m (Kapil), 230 EUR/m (Greece), GBP 800/m (UK); "total cost of the welding, construction, and digging was around 3-4 times more than the cost of the pipes"; POWER magazine: underground district-heating piping in the US "typically costs from $800/ft. to $1,500/ft." (DERIVED: USD 2.6 to 4.9 million per km, 1 km = 3,281 ft).
- Cost per km at the longest lines: Temelin line CZK 65 million per route-km (Q1, DERIVED, pair of pipes). Measured pumping power at any named long line: **NOT FOUND** (the Orchard 2 GW case is a design study).

### 2.3 Low-temperature and fifth-generation networks, heat pumps
- Generations (search summaries, UNVERIFIED; the Lund et al. paper itself returned 403): 4th-generation district heating targets supply/return of about 50-55 C / 20-30 C, or "55-60 C in the supply and 25-30 C in the return" from a third-generation 80/40 C; a 2021 paper gives a 60-70 C maximum supply.
- Fifth-generation (ambient-loop) networks: sources differ on the loop temperature (about 10-30 C, or 20-40 C, UNVERIFIED); a vendor blog claims pipework loss "reduced by up to 90%" (vendor claim, no method); a pipe maker's worked example needs a DN200 pipe where a 4th-generation network needs DN100 for the same load, because the temperature difference is small. A 2019 review covers 40 European networks with distributed heat pumps (UNVERIFIED, abstract only). A quantified loss reduction from a peer-reviewed review: **NOT FOUND**.
- Large heat pumps in service (Helen, Helsinki, search summaries, UNVERIFIED): Katri Vala 160 MW heating and 100 MW cooling, over 1,000 GWh per year, 88 C district heat from purified wastewater; Vuosaari about 13 MW heat (about 80% from the power plant's internal cooling circuit, 20% from sea water); Eiranranta about 90 MW planned. Seasonal COP: **NOT FOUND**.

---

## Q3. The electricity penalty and the temperatures involved

- **Definition (SOURCED, Kavvadias and Quoilin):** the power loss factor (PLF) is "the substitution rate between heat and generated power, i.e. the number of electrical kWh made unavailable by the extraction of one thermal kWh"; it is "also referred-to as the inverse of the Z-factor in some publications." They model it as the specific expansion work of the last turbine stage from the saturation pressure at district-heating temperature down to ambient (turbine isentropic efficiency 80%), so it rises with network temperature. "The incremental capital costs of setting up a district heating connection in a conventional extraction/condensing turbine are less than 1% of the total turbine capital costs."
- **Light-water reactors, SOURCED (POWER magazine, 1 March 2022, Oliker):** "The electric power loss is close to 0.2 kWe per kWth extracted" (three-stage extraction to about 300 F = 149 C); two-stage extraction to about 250 F (121 C): "the electrical power loss is about 12% of the thermal extraction"; "the ratio of the electricity lost to the heat-supplied for hot water-based systems can be about 1 kWe per 5 kWth to 10 kWth"; optimum supply about 250 F, peaking boilers to 300 F on the coldest days, return about 160 F (71 C); recommended CHP coefficient for nuclear plants "approximately 0.5-0.6." Multi-point extraction (including the low-pressure crossover) is the most efficient; single-point extraction "substantially less efficient."
- **Other values (UNVERIFIED, search summaries):** a French appraisal (EPJ Nuclear Sci. Technol. 2016; page returned 403) says for a PWR the lost electricity per extracted thermal energy is "around 1/5 for water at 120 C"; a seven-country European cost-benefit study uses about 1/6 for low-pressure-turbine extraction; an economic analysis puts lost output plus pumping at "about 1/4 MWh for each MWh of heat supplied to the DH network"; a 2026 ScienceDirect paper assumes 0.2 MWe per MWth with a maximum extraction cutting output by 150 MWe.
- **DERIVED (applying 0.2 MWe per MWth, the POWER and EPJ value, to the brief's sizes):** 1 GWth extracted costs 0.2 GWe; 10 GWth costs 2 GWe; 100 GWth costs 20 GWe; 600 GWth costs 120 GWe. Reading the plausible band of 0.12 (two-stage, 121 C) to 0.2: 0.12-0.2 GWe per GWth. For scale only: the brief's 324 GW electric net at one-third efficiency has about 648 GWth of reject heat (324 x 2), which is at condenser temperature, not district-heating temperature (next bullet).
- **Plant measurements:** Haiyang cycle thermal efficiency up 3.25% (POWER 2020, SOURCED); the company projects plant thermal efficiency of 55.9% if both units supply 30 million m2 (Chinese source, UNVERIFIED). Beznau: monthly report September 2013 lists lost production due to heat supply to Refuna and two industrial customers: 715 MWh in the month for block 1 and 0 for block 2; cumulative since the start of deliveries 483,172 MWh (block 1) and 53,949 MWh (block 2) (Nuklearforum, search summary, UNVERIFIED). A per-MWh ratio cannot be taken from this because the industrial customers are mixed in and the cumulative heat delivered is not given. Combined cycle: no ratio found. The only related figures are power-to-heat ratios (electricity/heat output) of 0.95 for a combined-cycle with heat recovery, 0.75 for engines, 0.55 for gas turbines with heat recovery, 0.45 for back-pressure steam turbines (Frangopoulos 2012, via a review; UNVERIFIED), and a note that extraction-condensing units' power ratio is hard to define. The power loss for a combined-cycle extraction: **NOT FOUND**.
- **Supply temperatures by network type:** EPRI: 80-130 C supply, 45-70 C return (conventional nuclear district heating). Plant examples: Temelin 142/65 C winter, 80/60 C summer (UNVERIFIED designer data); Melnik-Prague 90-140 / 55-65 C (SOURCED); Beznau 125 C winter, 80 C summer, 50 C return; Bilibino 150/70; Greifswald up to 180 C; NHR-5 84/56 C; SLOWPOKE under 100 C. Low-temperature (4th generation) 50-60 C supply (UNVERIFIED, Q2.3).
- **Condenser temperatures:** nuclear-power.com (UNVERIFIED, reference page): "the lowest feasible condenser pressure is the saturation pressure corresponding to the ambient temperature (e.g., 0.008 MPa ... 41.5 C)" with a typical gap of about 14 C between condenser and ambient temperature; a Cambridge PWR exam question uses a 29 C condenser and treats district heating as a low-grade use (UNVERIFIED). My recollection that 5 kPa saturates near 33 C is UNVERIFIED. Either way, condenser heat is at roughly 30-45 C, below the 45-70 C return temperature that EPRI gives for conventional networks, so it needs either extraction before the condenser (the penalty above) or a heat pump to raise it (COP at polar conditions not researched here).
- **Heat-only reactors** avoid the penalty by not making electricity: AST-500 (150/70 C, 1.6 MPa, 2,300 MW designed), never operated (EPRI); NHR-5 operated three winters.

---

## Q4. Polar and permafrost installation

- **Guidance, SOURCED (J. Paul Guyer 2013 course text adapted from US Unified Facilities Criteria, read as text):** "Utilidors are very expensive and can only be justified for special situations. In most cases individually insulated pipes in a common trench or on a common pile will be more economical." Utilidors range from "a simple insulated conduit to a walk-through passageway," above or below ground. Central heating lines are "more complex": their heat loss is usually enough to protect water and sewer pipes from freezing, but "the utilidor usually has to be much bigger"; the heat source is constant and runs all or most of the year so summer domestic water can exceed 80 F; "Thermal stratification can cause freezing of the lower pipes in large utilidors even when the average air temperature is adequate"; in a small utilidor test a cold-water line "froze and burst ... in spite of the continuous circulation of hot water"; put heat sources near the bottom and insulate domestic water separately.
- **Standard pipe:** pre-insulated bonded pipe for directly buried hot-water networks is standardized as EN 253 (steel service pipe, polyurethane insulation, polyethylene casing) (standard titles from catalog pages, SOURCED as titles).
- **Svalbard (Longyearbyen):** presentation by T. Antle (2026 file, text read): community-wide above-ground district heating, coal-fired CHP 8 MWe / 20 MWth built 1982, coal use ended 2025 (SOURCED). Search summaries (UNVERIFIED): overground pipelines "are gradually being replaced with insulated pipes laid in rock-filled trenches on the permafrost and covered with topsoil"; new buildings on steel piles; permafrost thaw affects infrastructure.
- **Greenland:** same presentation (SOURCED): 16 district heating systems and 23 plants under Nukissiorfiit; heat recovery from diesel generators, oil boilers, electric boilers and waste-to-energy; waste-to-energy CHP at Nuuk and Sisimiut, both 8.2 MWth, Nuuk with a 350 kWe organic Rankine unit; almost all of Sisimiut's heat, 10% of Nuuk's; Nanortalik's supply is diesel generator heat recovery plus oil. A search summary quoting the cost of a meter of district-heating pipe as USD 2,700 and that some municipalities require burial: UNVERIFIED. Pipe layout and heat loss in Nuuk: **NOT FOUND**.
- **Canada, Inuvik:** an early account puts the main utilidor at about $200 per foot and the smaller "utilidette" at about $100 per foot (1960s dollars; search summary of a 1975 paper abstract, UNVERIFIED); about 6,400 m of old utilidor "nearly 65 years old" would cost nearly $80 million to replace (CBC and Yahoo, search summary; the CBC page returned 403; DERIVED: $80 million / 6,400 m = **$12,500 per m**, UNVERIFIED).
- **Yakutsk and Siberia:** heating pipes carried above ground on concrete piles (Irish Times and travel accounts, UNVERIFIED); permafrost thaw under buildings disputed between construction flaws and the heating effect of buildings. Rosstat reportedly said one third of heating networks are in critical condition; a Novosibirsk main that burst in January 2024 had been laid in 1963 and last repaired in 1990 (news summaries, UNVERIFIED). Heat-loss percentages, failures per km and freeze-up outage records for Yakutsk, Norilsk or Magadan: **NOT FOUND** (a Russian-language search would be the next step).
- **Antarctic stations:** McMurdo: new water and sewer runs planned as "heavily insulated, metal-sheathed, hydronic and electrically heat-traced HDPE pipe," some direct bury, some above ground; fuel pipeline supported about 1 m above ground on adjustable supports; a NZ Army News item says stanchions of the Scott Base-McMurdo fuel pipeline "have become disjointed due to the freeze-thaw process" (search summaries, UNVERIFIED). **South Pole (SOURCED, southpolestation.com history page):** the original utilidor was "undersnow tunnels constructed from egg-shaped corrugated metal arch sections," carrying electrical, communications, water and sewer lines between buildings; later tunnels 6 ft wide by 10 ft high cut with a modified Bobcat and snowblower; a 1996-97 CRREL tunnel about 380 ft; a snowdrift loaded the dome and cracked its floor in 1977. Pipe freezing incidents at Antarctic stations and a cost per meter: **NOT FOUND**.
- **Snow cover on pipes:** the drift and burial effects above are the only snow-related facts found (see also P1 for drifting around structures).

---

## Q5. Antarctic precedents for using plant and generator heat

- **PM-3A (McMurdo).** Search summaries (UNVERIFIED): criticality March 1962, power to McMurdo from July 1962, shut down 1972 after a pressure-vessel leak; availability 72%; 438 malfunctions in ten years; supplied about 1.8 MWe (some sources 1.5 MWe), process heat and about 14,000 gallons (53 m3) of fresh water a day; one comparison table lists 9.36 MWth with 1,500 kW net and 11.27 MWth with 1,800 kW net (columns not visible). Thermal rating and heat-use fraction: **NOT FOUND** with certainty. Distilled water 1967-1972 and other uses are SOURCED in the earlier logistics file (AJUS Table 2).
- **McMurdo generators (Contractor magazine, 1 July 2009, SOURCED):** "About one-third (550 kW) goes up the exhaust stacks, one-third is given off by the generators' radiators, and one-third becomes electricity" (the article also states generation of 1,700 kW; the two statements are not consistent unless 1,700 kW is fuel input, as one-third of 1,700 kW is about 567 kW); radiators chosen because "Unlike the stacks, they provide a constant amount of heat"; waste heat was the first stage of heating and alone sufficient from November through January; it heated nine buildings down to 0 F outdoors (expected to reach -20 F after upgrades); primary-secondary water-glycol loops; seawater at 26-28 F warmed to 40 F before desalination; first used in 1981 to boil seawater, later superseded by reverse osmosis that needs far less energy. Xylem case study (search summary, UNVERIFIED): five CAT generators recover jacket and stack heat into hot glycol; backup boilers supplement.
- **Amundsen-Scott South Pole Station.** A visitor's blog (UNVERIFIED): a heat exchanger pulls heat from the engines and a glycol circuit carries it to warm the main station. Rodwell (SOURCED, brr.fyi and a Berkeley Lab page): the water plant sits next to the power plant and generator waste heat reaches the plant's heat exchangers by a glycol loop; recirculated water pumped at about 36 F and returned at about 84 F; backup boilers if plant heat is unavailable; the well is retired when it is about 500 feet deep, after "several years" (details in P1). NREL techno-economic paper (arXiv 2306.13552, SOURCED): example steady load 170 kW needs 124,000 gallons of fuel a year without renewables, at an assumed 12 kWh per gallon marginal fuel economy; the paper does not treat waste-heat recovery. Heat recovered in kW at the Pole: **NOT FOUND**.
- **Halley VI (UK) (Power Engineering trade article, SOURCED):** combined heat and power with exchangers on exhaust and cooling circuits for space heating, hot water and snow melting; exchangers "can reclaim up to 60 percent of all lost heat from the engines"; generator sets "total energy efficiencies of up to 90 percent"; fuel demand estimated 240 m3 per year; winter to -50 C. Exchanger kW and snow quantity not given.
- **Neumayer III (Germany) (search summaries, UNVERIFIED):** a 2009 press release describes a CHP unit giving 160 kW electric and 190 kW thermal (DERIVED heat/electric ratio 1.19); AWI describes four 160 kW diesel generators and a snow melter of up to 8 m3 using generator heat; Structurae/Wikipedia lists snow melting with 25 kW of waste heat; a feasibility study reports 714 t CO2 per year from the CHP plants and recommends power-to-heat for added renewables. Generator counts and ratings differ between sources.
- **Concordia (France/Italy) (search summaries, UNVERIFIED):** heating comes from cogeneration while the power station runs; three diesel generators each at least 150 kW with two working and one as backup (an Italian page says two generators); 12-16 winterers; to -80 C. Total kW and fuel: **NOT FOUND**.
- **Princess Elisabeth (Belgium) (search summaries, UNVERIFIED):** about 70% of electricity from nine wind turbines and about 30% from PV; passive heating plus equipment waste heat; walls about 60 cm; solar-thermal vacuum tubes for hot water, heating and a snow melter supplying 800 L of water per day; summer-only occupancy.
- **Australian stations (AAD page, SOURCED):** cogeneration "can save up to 50% of the station power requirements"; Casey, Davis, Mawson each have four Caterpillar 3306 sets of 125 kW (up to three running) as the cogeneration source; Macquarie Island two sets of 160 kW.
- **Others (UNVERIFIED):** Rothera (UK): all space heating from jacket-water heat of the generators, new sets to add exhaust and charge-air recovery; King Sejong (Korea): generator heat reused for other buildings; Syowa heat recovery since the 1950s-60s and Mizuho coolant heat since 1977 (Japan); Taishan (China): generator heat warms the energy building and station area, 60 kW microgrid (Advances in Polar Science 2021 review text, SOURCED).
- **Efficiency of recovery:** the only quantified splits found are McMurdo's thirds (fuel energy: about one third electricity, one third stacks, one third radiators) and Halley's "up to 60 percent of all lost heat" and "up to 90 percent" total. A measured plant-wide recovery fraction at any station: **NOT FOUND**.
- **A search for per-person station heating energy** (COMNAP, ATCM papers): **NOT FOUND** (the Advances in Polar Science review has none).

---

## Q6. Seasonal storage and demand matching

- **Pit storage, Dronninglund (Denmark), SOURCED where marked / search summaries otherwise:** 60,000 m3 water pit; storage efficiency "above 90%", five-year average 90.1% at a storage cycle of 2.16; capacity 5,280 MWh in one table; measured heat loss 1,392 MWh; lid accounts for 63.5-72.3% of the loss; cost about EUR 2.3 million (38.3 EUR/m3); Vojens (2015) cost 24 EUR/m3; a 2025-era benchmark about 30 EUR/m3 for pits over 100,000 m3; supplies about half the town's heat, around 15,000 MWh per year (all search summaries, UNVERIFIED). DERIVED: 5,280 MWh / 60,000 m3 = 88 kWh per m3, equal to about 76 K of water temperature swing at 1.163 kWh/(m3 K); 1,392 / (2.16 x 5,280) = 12% loss, consistent with 90% efficiency (the loss year is not stated).
- **Borehole storage, Drake Landing (Okotoks, Canada):** 144 boreholes about 37 m deep over about 35 m diameter (about 34,000 m3 of ground); solar fraction 97% in year five against a design goal above 90% (NRCan report title and summary, UNVERIFIED for the numbers); core above 65 C in autumn, about 40 C in spring (Solar Thermal World, UNVERIFIED). Energy stored and loss percent: **NOT FOUND**; the NRCan engineer calls the storage efficiency "fairly low" (qualitative).
- **Storage energy density (DERIVED):** water stores 4.19 kJ/(kg K) x 1,000 kg = 4.19 MJ per m3 per K = 1.163 kWh per m3 per K; a 60 K swing is 70 kWh per m3.
- **Seasonal demand.** An IEA Solar Heating & Cooling publication says "demand for heat is usually around 10 times larger in winter than in summer in Europe" (search summary, UNVERIFIED; the figure is general and not for a polar city). Network practice: supply temperature is lowered in summer (Beznau 125 to 80 C; Temelin 142/65 C winter to 80/60 C summer; Melnik 90-140 C by season). Summer demand is mainly hot water. Quantified summer share of annual demand for a cold-climate city: **NOT FOUND**.
- **What plants do with unusable heat.** EPRI (SOURCED): district-energy demand "would be higher in winter and lower in summer," met by supply-temperature changes; refueling outages timed to low-demand periods or covered by backup boilers; multi-unit plants stagger outages. Swedish and EU studies (search summaries, UNVERIFIED): waste-to-energy CHP plants "run at high loads and work almost continuously" and leave a heat surplus in summer; low summer demand "is a main driver against the increased use of CHP as it strongly influences the economics of a power plant"; CHP capacity is often too small for winter peaks so auxiliary boilers fill the gap. Plants with extraction-condensing turbines return to condensing operation when heat is not drawn (this follows from the PLF definition in Q3; no source page read for the sentence). Haiyang plans 500 MWh of heat storage tanks (POWER, SOURCED). Melnik: ČEZ schedules a week-long summer shutdown of hot water for maintenance (headline SOURCED as a title: "A week without hot water in summer means reliable heat supplies in winter for the right-bank part of Prague").
- Winter load duration curves: a Swedish CHP-sizing study uses them (search summary, UNVERIFIED); the numbers were not retrieved.

---

## Q7. Heat to water (melting ice)

**Inputs.** Specific heat of ice (EngineeringToolbox table, SOURCED): 2.050 kJ/(kg K) at 0 C, 2.000 at -10 C, 1.943 at -20, 1.882 at -30, 1.818 at -40, 1.751 at -50 C. Latent heat of fusion 333.55 kJ/kg (CRC Handbook 62nd ed., per Wikipedia table via search summary, UNVERIFIED at the primary level; the EngineeringToolbox ice page does not give it). Water 4.19 kJ/(kg K) (4.2 assumed, as above).

**DERIVED energy per tonne (= per m3) of water from ice, ending as liquid at 0 C** (sensible heat is the trapezoid integral of the table between the ice temperature and 0 C; working: -10 C: 5 x (2.050+2.027)/2 + 5 x (2.027+2.000)/2 = 20.3 kJ/kg; -30 C: 59.1 kJ/kg; -50 C: 95.5 kJ/kg):
| Ice at | Sensible | + latent 333.55 | Total | kWh per m3 | If heated on to +10 C | to +50 C |
|---|---|---|---|---|---|---|
| -10 C | 20.3 kJ/kg | | 353.8 MJ/t | **98.3** | 109.9 | 156.5 |
| -30 C | 59.1 | | 392.7 MJ/t | **109.1** | 120.7 | 167.3 |
| -50 C | 95.5 | | 429.0 MJ/t | **119.2** | 130.8 | 177.4 |
(+10 C adds 41.9 MJ/t = 11.6 kWh; +50 C adds 209.5 MJ/t = 58.2 kWh.) Latent heat alone is 92.6 kWh per m3.

**Per GWth:** 1 GWth for a year = 8.76 TWh. At -30 C ice to liquid at 0 C: 8.76 x 10^9 kWh / 109.1 kWh/m3 = **80 million m3 of water per GWth-year** (73.5 million m3 from -50 C ice; 89.1 million m3 from -10 C). Multiply by 10, 100 and 600 for the brief's sizes (about 0.8, 8 and 48 billion m3 of water per year at -30 C, ignoring that no one needs that much water). For scale: South Pole winter use "over 4500 liters (1200 gallons)" a day (search summary, UNVERIFIED); 4.5 m3 x 109 kWh = 490 kWh/day = about 20 kW of melt power (DERIVED).

**Published station figures.**
- Summit Station feasibility (US Army CRREL, search summary, UNVERIFIED; the DTIC page returned 403): "basic energy requirement to melt the snow is about 2300 Btu/gal" (DERIVED 0.178 kWh/L = 178 kWh/m3, which is snow starting near 0 C only if the number excludes sensible heat of cold snow; the source does not say); the Rodwell at 4,100-7,000 Btu/gal (DERIVED 0.32-0.54 kWh/L), "1.8 to 3.0 times higher" than melting surface snow.
- SANAE IV (South Africa, search summary of a feasibility study): theoretical minimum to melt snow at 0 C and heat the water to 30 C is about 819 kWh/day for 80 people x 80 L (DERIVED 128 kWh/m3; check: 92.6 + 34.9 = 127.5 kWh/m3, consistent). A practical melter is about half as efficient as the theoretical ideal (CRREL, same summary). Princess Elisabeth solar melter: 800 L per day.
- South Pole Rodwell (brr.fyi, blog, UNVERIFIED as a blog, but the arithmetic checks): "2.44 watt-hours (8.33 BTUs)" per gallon per F (DERIVED 1.16 kWh/m3/K, correct); latent "350 watt-hours" per gallon (DERIVED 92.5 kWh/m3, correct); its quoted raw total "268 618 watt-hours" per gallon from -60 F to 50 F is a typographical artifact (110 F x 2.44 Wh = 268 Wh) and it treats ice with water's heat capacity, overstating the sensible heat. The Rodwell is a recirculation loop: water drawn at about 36 F is reheated to about 84 F with generator heat and returned; one gallon is sent to the station for every two reheated and returned (USAP feature, search summary, UNVERIFIED).
- Other stations: Halley VI melts snow with engine heat; Neumayer III's snow melter (up to 8 m3) uses engine/CHP heat (25 kW waste heat per Structurae); McMurdo uses reverse osmosis on seawater, with waste heat to warm the feed (Q5). Energy per m3 at the stations beyond the above: **NOT FOUND**.

---

## FINAL: what the sources support / do not support / NOT FOUND

**Supported (SOURCED or well-triangulated):**
- Nuclear district heating is a long-running practice: EPRI counts 27 facilities in 11 countries and 750 reactor-years of cogeneration by 2019; typical network temperatures 80-130 C supply and 45-70 C return; typical plant-to-network distances 2-6 km, with long lines at Kola (64 km), Novovoronezh (50 and 55 km) and Beznau (35 km main plus 85 km of local pipe); largest documented stations Greifswald (260 MWth over 22 km, 800 mm) and Haiyang (1,134 MW for about 13 million m2 in 2024, which is about 87 W/m2); heat-only reactors for 2,300 MW were designed but never operated.
- New long lines are being built now: Temelin to Ceske Budejovice (26 km, two pipes, CZK 1.69 billion, 719,000 GJ in the latest year, about 216 MW design thermal by my derivation); Haiyang 23 km (and a 120 km project reported in Chinese sources); Dukovany to Brno planned at 42 km and CZK 19 billion.
- The longest hot-water feeder with good data is Melnik to Prague: 34 km, two 1.2 m pipes, 90-140 C supply, 55-65 C return, 4% loss, 74.5 km to the farthest consumer. A review of lines in operation in 2016 found a maximum of 60-70 km and rarely more than 30 km; a 2018 techno-economic model fits maximum economic distance to alpha x sqrt(MW) with alpha 1-7.5 in the cases computed; design studies exist at 2 GW over 140 km (1.75% heat loss, pumping losses 50 MW as stated).
- The electricity cost of heat extraction from a light-water plant is about 0.12 to 0.2 MWe per MWth for 120-150 C supply temperature; lower supply temperatures reduce it.
- Antarctic precedent is almost entirely diesel-generator heat recovery (McMurdo: thirds; Halley: up to 60% of lost heat), with one nuclear precedent (PM-3A, 1962-1972); heat recovery supplies space heating, snow melting and water.
- Energy to make water from ice: about 98, 109 and 119 kWh per m3 for ice at -10, -30 and -50 C (ending at 0 C liquid), plus about 1.16 kWh per m3 per K above that; field systems reported 2 to 3 times the theoretical figure.

**Not supported / caution:**
- No source supports a heat line, cost, loss or pumping figure at the scale of 10, 100 or 600 GWth; the largest design study found is 2 GW. Extending the distance formula beyond about 2 GW is extrapolation.
- No source gives a nuclear plant heat system in polar conditions with pipes running through ice or firn; all long-line data are European or Chinese, temperate to cold continental.
- Economic distances in the literature are in 2016-2018 European prices and are not transferable to Antarctica.

**NOT FOUND (queries in the log):** thermal MW for Bohunice, Bruce, Qinshan, Beznau (primary Axpo/Refuna document), Pevek (the two figures still conflict); Russian pipe lengths other than EPRI's list (the Sozoniuk NEA presentation returned HTTP 521 again); measured pumping power for any long line; cost per km for the longest lines (except Temelin's derived value); a measured electricity loss per MWh of heat for any named plant; the combined-cycle extraction penalty; heat pump COP at polar temperatures; permafrost and polar district-heating outage or freeze-up statistics; Nuuk pipe layout; kW of heat recovered at the South Pole and Concordia; summer share of annual heat demand; borehole-storage loss percent; a published quantified fifth-generation loss reduction.

**Things worth knowing:** the 2026 Temelin figures (719,000 GJ, 22 Oct 2026) and the Haiyang 2024 figure (1,134 MW) are the newest sourced operating data; the McMurdo article's "1,700 kW" and "one-third" statements do not agree with each other; the Kavvadias and Quoilin Table 1 row for Oradea could not be read from the PDF text.

---

## Search log (every web call; tool, query, result)
Tool legend: S = WebSearch, F = WebFetch. "Dead at" says where a dead end died. PDFs fetched by WebFetch were saved by the tool and read locally with `pdftotext` (in my scratch folder).

1. S "Haiyang nuclear district heating Warm Nuclear No.1 thermal MW supply return temperature 23 km pipeline heat extraction steam AP1000" - partial (no MW or temperatures).
2. S "Beznau nuclear district heating Refuna network km thermal MW households" - hit (figures conflict).
3. S "Prague Melnik district heating pipeline 35 km ... DN1000 supply temperature" - partial (DN1200, 34 km; no supply temperature).
4. S "nuclear cogeneration district heating review IAEA Bohunice Mochovce Temelin Paks Loviisa Bruce Energy Centre heat supplied" - partial (found EPRI review).
5. F EPRI restservice PDF - tool summary unreadable (binary); read locally - hit.
6. F IAEA TECDOC-1056 PDF - dead at source (HTTP 402).
7. F OECD-NEA Schmidiger presentation - dead at source (HTTP 403).
8. S "Bohunice Trnava hot water pipeline nuclear heat km MW ..." - partial.
9. S "Loviisa nuclear district heating Loviisa town MW heat extraction Fortum Finland" - miss for current heat; Loviisa 3 study found.
10. F oenergetice Dukovany-Brno - hit.
11. F WNN Mochovce district heat - hit.
12. F WNN "Czech reactors could supply heat" - hit.
13. S Czech "Temelin Ceske Budejovice horkovod km MW ..." - hit (no MW).
14. S "Bruce Energy Centre Ontario steam supply ..." - miss for MW (died at the sources: no page with figures returned).
15. S "Paks nuclear power plant district heating Paks town MW thermal ..." - partial.
16. S "Bilibino nuclear power plant heat supply Gcal per hour pipeline ..." - partial.
17. F test.oecd-nea.org Sozoniuk - dead at source (HTTP 521).
18. F oenergetice Temelin line cost - hit.
19. F CEZ Temelin three-year press release - hit.
20. F tespo-eng presentation PDF - dead at source (404).
21. S (extended) "longest district heating transmission pipeline in the world km ..." - partial.
22. S "long-distance heat transport district heating maximum economical distance ..." - hit (Kavvadias and Quoilin).
23. F ORBi Kavvadias and Quoilin PDF - read locally - hit.
24. F SASAC Tuoketuo-Hohhot - dead at source (SSL error).
25. F POWER Haiyang AP1000 - partial.
26. F WNN Chinese long-distance nuclear heating begins - hit.
27. S (extended) "Haiyang AP1000 steam extraction heating capacity MW ..." - partial.
28. S Chinese "Haiyang nuclear heating extraction ..." - partial.
29. F e3sconf ESAT 2023 PDF - dead at source (HTTP 403).
30. F NEI Haiyang expands - hit.
31. S (extended) "nuclear power plant district heating loss of electricity per MWh heat extracted Z factor ..." - hit.
32. S "Opportunities for Cogeneration with Nuclear Energy IAEA NP-T-4.1 ..." - partial (no figures).
33. F EPJ-N 2016 full text - dead at source (HTTP 403).
34. F POWER "District Heating Supply from Nuclear Power Plants" - hit.
35. S "fifth generation district heating cooling 5GDHC ..." - partial.
36. S "large heat pumps power plant condenser cooling water ... Helsinki" - partial.
37. S "district heating generations 1G to 4G supply temperature ..." - partial.
38. F core.ac.uk Lund 4GDH PDF - dead at source (HTTP 403).
39. S Czech "Melnik Praha horkovod 35 km DN1200 ... tepelne ztraty" - hit.
40. F CEZ "Teplo z elektrarny Melnik proudi do Prahy uz 30 let" - hit.
41. S "Concordia station Antarctica waste heat generators ... Neumayer III Princess Elisabeth Halley VI" - partial (no Concordia or Neumayer hits; Halley found).
42. F power-eng Bowman Halley VI - hit.
43. S "PM-3A Nukey Poo McMurdo reactor thermal power ..." - partial.
44. S "Neumayer III station Antarctica combined heat and power ..." - hit (sources conflict).
45. S "Amundsen-Scott South Pole Station power plant waste heat recovery ..." - partial.
46. S (extended) "Antarctic research stations energy use review heat recovery ..." - partial.
47. S "Concordia station Dome C energy generators heat recovery ..." - partial.
48. S "Princess Elisabeth Antarctica station zero emission heat ..." - partial.
49. F arXiv 2306.13552 - read locally - partial (fuel and load only).
50. F Advances in Polar Science review PDF - read locally - partial.
51. F Contractor magazine McMurdo waste heat - hit.
52. F antarctica.gov.au power generation - hit.
53. S "utilidor insulated pipe permafrost district heating Siberia Yakutsk Norilsk ..." - partial.
54. S "Nuuk Greenland district heating pre-insulated pipes ..." - miss (died at the query: only generic pipe pages).
55. S "Longyearbyen Svalbard district heating pipes permafrost utilidor ..." - partial.
56. S "Alaska Arctic utilidor design cost per foot ..." - partial.
57. F CED/Guyer utilidors PDF - read locally - hit.
58. F CBC Inuvik utilidor - dead at source (HTTP 403).
59. S "Greenland Arctic district heating network Nuuk Sisimiut Ilulissat heat loss ..." - partial.
60. S "district heating networks Russia heat losses percent pipe network failures ..." - partial (news only).
61. S "McMurdo Station utilidor insulated pipes above ground ..." - partial.
62. F Antle pellet.org presentation - read locally - hit.
63. F southpolestation.com utilidor - hit.
64. S (extended) "seasonal thermal energy storage pit ... Vojens Dronninglund borehole ..." - hit.
65. S "specific heat capacity of ice versus temperature table ..." - partial (pointed to EngineeringToolbox).
66. S "Antarctic station snow melter energy per liter ..." - hit.
67. F engineeringtoolbox ice thermal properties - hit.
68. F DTIC ADA538084 - dead at source (HTTP 403).
69. S "Rodriguez well Rodwell South Pole station water supply ..." - partial.
70. S "latent heat of fusion of ice 333.55 kJ/kg IAPWS NIST value" - partial (no primary).
71. S "district heating summer load share of annual heat demand ..." - partial.
72. S German "Beznau Refuna Axpo Fernwaerme ..." - partial.
73. F brr.fyi South Pole water infrastructure - hit.
74. F glacier.lbl.gov rod_well - hit.
75. S "PWR condenser pressure saturation temperature typical 5 kPa ..." - partial.
76. S "Drake Landing Solar Community borehole thermal energy storage ..." - partial.
77. S "Kola nuclear power plant Polyarnye Zori Apatity heat pipeline 64 km ..." - miss for the 64 km (no confirming source).
78. S "combined cycle CHP district heating extraction condensing steam turbine power loss ..." - miss for the power loss (power-to-heat ratios only).

Total web calls: 78.
