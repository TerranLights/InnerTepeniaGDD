# Nuclear waste and spent fuel: what can be reused, what cannot (Unit R7, 2026-11-02)

**Scope.** Real-world 2020s facts on whether spent nuclear fuel and nuclear waste can be reused, for a fictional cold, isolated, Antarctic nation of about 15 million people that is barred by treaty (the Antarctic Treaty Article V model) from disposing of radioactive waste in its territory, so spent fuel must leave, be stored, or be reused. Facts only. No recommendation, no design, no ranking. Every claim is labeled **SOURCED** (read at the source page or document in this session), **DERIVED** (my arithmetic on sourced figures, working shown), **UNVERIFIED** (seen only in a search snippet, recalled, or inferred) or **NOT FOUND**. Each label also notes how much the source can be trusted where that matters (industry, advocacy, primary regulator). Note on method: the fetch tool reads a page through a small summarizing model, so a "SOURCED" quote is the tool's rendering of the page; PDFs that the tool could not read were converted with `pdftotext` in this unit's scratch folder and read directly (marked "read directly").

**Started:** 2026-11-02 18:12 (shell clock). **Ended:** 2026-11-02 18:25 (shell clock; the clock ran faster than the many tool round trips suggest, so treat the stamps as order markers only).

## PROGRESS
- [x] Q1 Reprocessing, MOX, volume reduction, cost, proliferation, IAEA/NPT
- [x] Q2 Fast reactors, actinide burning, ADS (MYRRHA), how much could be eliminated
- [x] Q3 Isotopes (Am-241, Pu-238, Sr-90, Cs-137, Co-60, Mo-99 and others, Kr-85, tritium) with use, source, scale
- [x] Q4 Heat and power from waste (RTGs, Antarctic RTGs, decay heat); **nuclear batteries and radioisotope heater units were NOT researched (budget); marked NOT FOUND**
- [~] Q5 Irradiation for food and sterilization: dose categories and sources found; **quantitative shelf-life gains and spent-fuel irradiators NOT FOUND**
- [x] Q6 What cannot be reused: volumes, durations, repositories, casks (per-GWe-year volumes only partly found)
- [x] Q7 Antarctic and cold-region relevance (Madrid Protocol Annex III, PM-3A, ice-sheet disposal history, Joint Convention 60 degrees S clause)
- [x] Search log (83 web calls, one over the upper budget; listed at the end)

---

## Q1. Spent fuel reprocessing and recycling

### 1.1 What fraction of spent light-water-reactor fuel is reusable
- **SOURCED (WNA, "Processing of Used Nuclear Fuel"):** "Most of it – about 96% – is uranium," and up to 1% is plutonium; recycling "can save up to 30% of the natural uranium otherwise needed." (World Nuclear Association is an industry body; acceptable as a secondary source per the brief.)
- **SOURCED (Orano, vendor page):** Orano says it recovers "the 96% of re-useable materials (95% uranium and 1% plutonium)," so about 4% is waste. Vendor claim, same split as the WNA.
- **Caveat, UNVERIFIED (one advocacy post seen in a snippet, koebergalert.org):** critics say "96% recyclable" overstates what is done in practice with light-water reactors. The practical limit is real: the recovered uranium is mostly not re-enriched and reused at scale, and plutonium goes into MOX (below). I did not open a source that quantifies how much recovered uranium is actually re-used. **NOT FOUND:** a primary-source figure for the share of recovered reprocessed uranium actually put back in reactors.
- **SOURCED (WNA):** about 28% of the roughly 448,000 tonnes of used fuel discharged from commercial reactors has been reprocessed. **DERIVED:** 0.28 x 448,000 = about 125,000 t reprocessed to date. (A second WNA page gives about 430,000 t discharged worldwide; the two pages disagree and are not reconciled.)
- **SOURCED (Orano):** "40,000 tons of used fuel reprocessed since 1976" at La Hague.

### 1.2 Plant capacity by country (tonnes per year, light-water fuel unless noted)
**SOURCED (WNA, Processing of Used Nuclear Fuel):**

| Country | Plant | Capacity | Status as stated |
|---|---|---|---|
| France | La Hague | 1,700 | operating |
| Russia | Ozersk/Mayak | 400 | operating |
| Japan | Rokkasho | 800 | completion targeted for fiscal 2026 |
| India | four plants (heavy-water reactor fuel) | 260 | operating |
| UK | Magnox plant (1,500 t/yr) | historical | final feed July 2022 |
| UK | THORP (900 t/yr) | historical | reprocessing ended November 2018 |
| China | not covered by that page | NOT FOUND | |

- France, La Hague: UNVERIFIED detail from search snippets of Orano's 2025 report and the French regulator (ASN): two lines (UP2-800 and UP3) with a combined authorized capacity of 1,700 t/yr, each plant individually limited to 1,000 t/yr. Orano page (SOURCED): "an annual production of 1,100 tons until 2022" under the EDF contract.
- Japan, Rokkasho: construction began 1993, first expected done 1997 (UNVERIFIED, search snippet citing reporting); the completion date had been postponed 27 times as of May 2026, with the latest target the end of fiscal 2026 (March 2027) (UNVERIFIED, snippets of Reuters, Jiji and Argus items). A 28th delay was not found but could exist after May 2026.

### 1.3 MOX fuel (plutonium recycled into mixed uranium-plutonium oxide fuel)
**SOURCED (WNA, "Mixed Oxide Fuel"):**
- MOX "provides almost 5% of the new nuclear fuel used today."
- First used in a thermal reactor in 1963, commercial use from the 1980s; over 3,000 t loaded into power reactors since then.
- Orano count: 44 reactors have used MOX since 1972: 22 France, 10 Germany, 5 Japan, 3 Switzerland, 2 Belgium, 1 Netherlands, 1 USA. (Vendor figure.)
- Orano page (SOURCED): "In France, MOX produces 10% of the nuclear electricity." (The WNA page says "about 10% of France's fleet"; the two wordings differ.)
- World MOX fabrication capacity, t/yr: France Marcoule (Melox) 195; Japan Tokai 130; Russia Zheleznogorsk 60; India Tarapur 5; **total 440**. "Only one plant in Europe, in France, currently produces commercial quantities."
- Japan: J-MOX plant (130 t/yr) at Rokkasho "now expected to be completed in fiscal year 2027 after multiple delays." Five Japanese reactors have loaded MOX (Orano). Genkai-3 was first (November 2009) per a snippet (UNVERIFIED).
- Russia: 60 t/yr plant at Zheleznogorsk started 2015, supplies MOX for the BN-800 fast reactor.
- UK: Sellafield MOX Plant downrated from 128 to 40 t/yr; closure decided August 2011.
- USA: Savannah River MOX plant cancelled October 2018 "after costs escalated to an estimated $49 billion to complete."
- Melox output problems, UNVERIFIED (snippet of a Frank von Hippel blog citing Orano data): output fell from 124 t (2016) to 51 t (2021); defective scrap stored at La Hague.
- MOX plutonium content, UNVERIFIED (snippet, Orano): 3 to 12% Pu depending on customer. **DERIVED:** Melox at 195 t/yr x 3 to 12% = 5.9 to 23 t of plutonium per year if run at licensed capacity (a bound, not an observed figure).
- **DERIVED:** La Hague 1,700 t/yr x about 1% plutonium = up to about 17 t Pu per year separated at full capacity, upper bound.

### 1.4 UK and Russia practice (as far as sourced)
Covered in the table and 1.3: UK reprocessing finished (2018 and 2022) and its MOX plant was closed; Russia reprocesses 400 t/yr at Mayak and runs a 60 t/yr MOX line feeding a fast reactor. **NOT FOUND:** the size of the UK's separated plutonium stockpile from a primary source (a snippet of a WNN viewpoint says about 100 tonnes, UNVERIFIED).

### 1.5 How much waste volume recycling removes
- **SOURCED (Orano):** "Final waste: 5-times less in volume, 10-times less in radiotoxicity."
- **SOURCED (WNA Processing page):** reprocessing reduces the volume of material for high-level waste disposal "to about one-fifth."
- **SOURCED (WNA Radioactive Waste Management page):** reprocessing "significantly reduces the volume of HLW (by about 85%)." This differs from one-fifth (80%) on the other page; both are WNA and not reconciled.
- **SOURCED (WNA):** reprocessed high-level waste decays to the level of the original uranium ore within about 9,000 years, versus about 300,000 years for unreprocessed used fuel (see 6.3).
- Plutonium alone burned does not change long-term hazard much: see 2.4 (factor of about 5).

### 1.6 Cost
- **SOURCED (WNA):** a 2006 Boston Consulting Group study for Areva found that recycling in the USA via the COEX process would be "economically competitive with direct disposal of used fuel," for a 2,500 t/yr plant costing $12 billion to build and $16 billion total capital for all related aspects. (Commissioned by the vendor.)
- **SOURCED (OECD-NEA 2002, read directly):** adding partitioning and transmutation to a fully closed cycle was estimated to add "10-20% to the electricity costs of the once-through fuel cycle" (see 2.4).
- Counter-evidence, SOURCED (WNA): Savannah River MOX plant cancelled at an estimated $49 billion; Rokkasho delayed 27 times.
- **NOT FOUND:** an independent (non-industry, non-advocacy) cost-per-kg comparison of reprocessing versus direct disposal. Not searched beyond the above.

### 1.7 Proliferation concerns, safeguards, and what IAEA/NPT say
- **SOURCED (WNA):** separating plutonium on its own "is described as a potential proliferation risk"; recovering all long-lived actinides together with plutonium (pyroprocessing, co-extraction) "is intended to reduce the risk of plutonium diversion."
- **SOURCED (Joint Convention on the Safety of Spent Fuel Management, 1997, unofficial NUS text read directly):**
  - Article 2(l): "'reprocessing' means a process or operation, the purpose of which is to extract radioactive isotopes from spent fuel for further use."
  - Article 3(1): spent fuel held at reprocessing facilities "is not covered in the scope of this Convention unless the Contracting Party declares reprocessing to be part of spent fuel management."
  - Article 27(3)(iii)-(iv): nothing in the Convention prejudices "the right of a Contracting Party to export its spent fuel for reprocessing" and the right of the receiving party to return the resulting waste to the state of origin.
- **UNVERIFIED (search snippet, not the IAEA text):** IAEA significant quantity for plutonium is 8 kg; timeliness goals are 1 month for unirradiated direct-use material (metal, fresh MOX) and 3 months for irradiated spent fuel. A 2009-era analysis and a critique (both advocacy/academic, via snippets) argue the IAEA could not meet its detection goals at large plutonium bulk-handling facilities (reprocessing and MOX fabrication plants). The IAEA's own glossary page returned 402; INFCIRC/140 (the NPT text) returned 402.
- **UNVERIFIED (snippets):** Rokkasho was designed with a joint safeguards review (1988-1992, with the US, UK, France, West Germany, Japan, IAEA and Euratom); measures include design information verification, interim inventory verification with near-real-time accountancy, and a joint Japan-IAEA on-site laboratory. Japan has published its separated plutonium holdings since 1994 and says it has a "no surplus plutonium" policy.
- **NPT text: NOT FOUND in this session** (UN site redirected then 404; IAEA PDF 402; no alternate host tried because the rule is not to work around blocks). **UNVERIFIED (recalled):** NPT Article IV recognizes the "inalienable right" of parties to peaceful nuclear energy, and Article III requires IAEA safeguards on all source or special fissionable material in all peaceful activities of a non-nuclear-weapon state; the treaty does not name reprocessing. This is recalled, not read.

---

## Q2. Fast reactors and actinide burning

### 2.1 Operating or recent fast reactors
**SOURCED (WNA, "Fast Neutron Reactors," first 100,000 characters read):** "Over 400 reactor-years of experience has been gained in operating them."

| Reactor | Facts as sourced |
|---|---|
| BN-600 (Russia, Beloyarsk 3) | Grid power since 1980, 560 MWe; "said to have the best operating and production record of all Russia's nuclear power units." Blanket replaced with steel reflectors so it can burn military plutonium, starting 2012. |
| BN-800 (Russia, Beloyarsk 4) | 789 MWe (WNN). First 100% power 17 August 2016 (WNN). Full MOX core from September 2022 (WNA). "Can burn up to 3 tonnes of plutonium per year from dismantled weapons, and will test minor actinide recycling." Stated main purpose: "to provide operating experience and technological solutions" for the BN-1200. |
| CEFR (China, experimental) | 65 MWt, 20 MWe. First criticality July 2010; restarted for high-power operation June 2020; reconnected to grid 15 February 2021 (WNN). |
| CFR-600 (China, Xiapu) | Construction began December 2017, unit 2 late 2020; WNA table lists operation from 2023; MOX fuel; breeding ratio given as about 1.1 (WNA) versus a design objective of 1.2 in a search snippet (UNVERIFIED, conflict not resolved). Designed to breed, not primarily burn. Current operating status not confirmed by a dated source (NOT FOUND). Snippet (UNVERIFIED): China stopped its annual voluntary plutonium declarations to the IAEA. |
| PFBR (India, Kalpakkam) | Fuel core loading began March 2024, fuel loading October 2024 after criticality was first expected 2018; blanket designed to breed; not under IAEA safeguards (WNA). |
| Phenix (France) | Operated 1973 to 2009. Planned breeding ratio 1.13, measured about 1.16. About 25 t of its fuel reprocessed and the plutonium recycled, cited as proof of the breeder fuel cycle. |
| Monju (Japan) | Started 1994, shut after a 1995 sodium leak, restarted 2010, closed again; decommissioning confirmed December 2016; fuel removal completed October 2022; 198 MOX assemblies (WNA). Decommissioning plan: 30 years, more than JPY 375 billion (UNVERIFIED, WNN snippet). |
| ASTRID (France) | **NOT FOUND**: the search returned nothing on its cancellation. |

### 2.2 What is demonstrated versus experimental (from sources)
- **Demonstrated:** commercial-scale electricity from fast reactors (BN-600 since 1980); closing a plutonium cycle with Phenix fuel; burning weapons plutonium as MOX (BN-600 hybrid core from 2012, BN-800 full MOX core 2022); fast reactors can burn long-lived actinides because fission cross sections are higher in a fast spectrum (WNA, Chang 2014 table).
- **Planned or experimental:** minor actinide recycling in the BN-800 ("will test," so not yet demonstrated in the page); metal fuel in the CFR-600 later; pyroprocessing waste "projected" to need 300 years but "these technologies are not yet operational" (WNA).
- **NOT FOUND:** measured minor-actinide burning figures from any operating fast reactor.

### 2.3 Accelerator-driven transmutation: MYRRHA
- **SOURCED (IN2P3 sheet "Myrrha 2025," read directly):** hybrid research reactor at Mol, Belgium; "Status: project under construction, supported by the Belgian Nuclear Research Centre (SCK CEN)." Maximum power 100 MWth; 600 MeV proton linac 400 m long, 2.4 MW continuous beam; total estimated cost "EUR 2 to 3Bn"; phase 1 is called MINERVA, to test the redundancy approach for beam reliability (no more than 3 interruptions of more than 3 s per quarter). Timeline graphic in the sheet shows 2036 for the full ADS.
- **SOURCED but dated (WNN, October 2013):** 57 MWt design; mission includes "transmutation of long-lived radionuclides" and medical radioisotopes; then expected "in service in 2024-25." This differs from the 100 MWth of the 2025 sheet and the 2036 date; the schedule has slipped about 12 years.
- **UNVERIFIED (snippets):** Belgian government approved construction/operation to 2038 in 2018 with EUR 558 million for 2019-2038; MINERVA is 100 MeV, 4 mA with radioisotope and fusion-materials target stations; construction start planned Q1 2025 (not confirmed).
- No operating accelerator-driven transmutation system exists in the sources. **NOT FOUND:** confirmation that MYRRHA construction actually began.

### 2.4 How much long-lived waste could be eliminated (OECD-NEA 2002, "Accelerator-driven Systems (ADS) and Fast Reactors (FR) in Advanced Nuclear Fuel Cycles," read directly)
- Goal stated: "a reduction in the HLW radiotoxicity by a factor of at least one hundred is desirable."
- "Fuel cycles with multiple recycling of the fuel and very low fuel losses are required to achieve the desired hundred-fold radiotoxicity reduction."
- With fully closed cycles these strategies "can achieve a more than hundred-fold reduction in the long-term waste radiotoxicity," assuming 0.1% losses for all actinides ("as already achieved for uranium and plutonium, though an ambitious target for the other actinides"), multiple recycling and high burn-ups. Fast reactors and ADS give "no distinct differences" in potential.
- "Plutonium burning alone ... reduces the long-term waste radiotoxicity by only a factor of about five."
- Recycling americium and curium in target pins is "about a factor of two less effective" than a closed cycle.
- P&T "is estimated to add a relatively modest 10-20% to the electricity costs."
- Time scale: the goal "can be achieved only if it is introduced with the intention of using it for at least a century."
- Caveat: this is a 2002 study; the figures are model results, not operating data.

---

## Q3. Isotopes from waste and spent fuel with real uses

| Isotope | Use | Source (spent fuel or separate?) | Scale |
|---|---|---|---|
| Am-241 | Smoke detectors, backscatter gauges, fill-height detectors, coal-ash measurement (WNA, SOURCED). Space power candidate (ESA). | Grows in from decay of Pu-241 in separated plutonium; "produced as nuclear waste and is nearly isotopically pure" (Wikipedia RTG page, SOURCED). UK NNL separates it from civil plutonium (AMPPEX process) (snippet, UNVERIFIED). Half-life 432 y (WNA). | Amount per smoke detector **NOT FOUND** in this session (not read). Power density about one quarter of Pu-238; prototypes 2-2.2 W/kg expected, tests gave 1.3-1.9 W/kg (SOURCED). UK civil plutonium stockpile about 100 t (UNVERIFIED snippet). |
| Pu-238 | Radioisotope power for spacecraft: MMRTG about 110 We, GPHS-RTG 300 We, MHW-RTG 160 We (SOURCED, Wikipedia). | Not recovered from spent fuel directly: made by irradiating Np-237 targets in the HFIR (Oak Ridge) and Advanced Test Reactor (Idaho), then chemical separation (ORNL paper, read directly). Np-237 is a minor actinide in spent fuel (UNVERIFIED inference; the paper says the nation's separated Np-237 is stored at INL). Last Savannah River production 1988. | Initial ORNL demonstration 350 g PuO2. Goal: average 1.5 kg/yr, "anticipated to be complete by 2026" (SOURCED, ORNL). US made no more than 50 g in total 2013-2018 (SOURCED, Wikipedia). Heat 0.57 W/g (SOURCED). **DERIVED:** 1.5 kg x 0.57 W/g = about 855 W thermal per year of production. |
| Sr-90 | Heat source for Soviet terrestrial RTGs (Beta-M and others); Sr-90 yields about 0.95 W/g as pure metal, usually used as titanate; heavy shielding (Wikipedia RTG, SOURCED). | Fission product of spent fuel and high-level waste (UNVERIFIED general knowledge; the Hanford capsules below are the documented example). | Beta-M: 1,480 TBq, "some 280 grams," 250 W thermal, 10 W electric (Wikipedia Beta-M, SOURCED). **DERIVED:** 1,480 TBq / 3.7e10 Bq per Ci = 40,000 Ci; 10 W / 250 W = 4% conversion efficiency. |
| Cs-137 | Blood irradiators, low-intensity gamma sterilization, level and density gauges, soil-erosion tracer (WNA, SOURCED); food irradiation gamma source (snippet). | Fission product separated from high-level waste: Hanford Waste Encapsulation and Storage Facility made cesium chloride and strontium fluoride capsules 1968-1985; 1,335 cesium and 601 strontium capsules remain in a pool (2018 Federal Register, snippet, UNVERIFIED; ANS: "nearly 2,000 ... capsules," SOURCED). | Capsule curie totals **NOT FOUND**. NNSA had replaced 50 CsCl blood irradiators and Congress targeted elimination of all by 2027 (snippet, UNVERIFIED). Most Category 1-2 sources use Co-60, Cs-137 or Ir-192; about 2,000 US licensees hold them (NRC fact sheet, read directly). |
| Co-60 | "Widely used for gamma sterilization, industrial radiography, density, and fill height switches" (WNA). | **Not a fission product**: made by irradiating Co-59 in reactors; "has mostly come from Candu power reactors by irradiation of Co-59 in special rods for up to three years" (WNA). Nordion says about half of world supply comes from Ontario CANDUs (snippet, UNVERIFIED). | Supply in curies per year **NOT FOUND**. Cumulative "more than 500 million curies" shipped by CANDU partners (Scribd-hosted paper, weak, UNVERIFIED). |
| Mo-99 (decays to Tc-99m) | Medical imaging; Tc-99m is about 80% of nuclear medicine procedures; over 50 million procedures per year (WNA). | **Fission product, but not harvested from power-reactor spent fuel**: made mostly by fission of U-235 targets in research reactors then chemically processed; neutron activation of Mo-98 is a lower-activity route (WNA). About 95% of supply comes from the reactors in the NEA's Table 2 (NEA No. 7743, October 2025, read directly). | Demand 23,000 six-day TBq per year in 2012, about 18,500 since; about 333 six-day TBq per week in mid-2017 (WNA). **DERIVED check:** 333 x 52 = 17,300 per year, consistent with 18,500. |
| I-131 | Medical. | Fission product recovered during Mo-99 processing; also made separately from tellurium oxide at Leningrad NPP (WNA). | 2.6-3.0 TBq per week supplied to one Russian institute (WNA). |
| Sr-89, Lu-177 | Medical. | Sr-89 listed as a fission product; Lu-177 by activation of Lu-176 or Yb-176 (WNA). | Not found. |
| Kr-85 | "Used for industrial gauging" (WNA); atmospheric-dispersion tracer. | Fission gas released at reprocessing; La Hague released 1.8e17 Bq in 1994 (snippet from an advocacy-leaning source, UNVERIFIED). **DERIVED:** 1.8e17 / 3.7e10 = about 4.9 million Ci. Half-life about 10.7-10.8 y. | Whether it is captured and sold: **NOT FOUND**. |
| Tritium | Tracer; groundwater dating (WNA); fusion experiments (JET used tritium from Darlington, snippet). | Byproduct of heavy-water (CANDU) reactors, removed by Ontario Power Generation's Darlington Tritium Removal Facility, first tritium mid-1988; sales approved 1989, export needs a permit (snippets, UNVERIFIED). Not mainly a spent-fuel product. | Kilograms **NOT FOUND**. |
| Others | Np-237 (Pu-238 feedstock above), Cm-244 and Am-243 as actinide targets (no source read), iridium-192 (activation, not waste). | | |

Note on sorting "from spent fuel" versus "made separately": Sr-90, Cs-137, Kr-85 and I-131 are fission products that can be recovered from irradiated fuel or high-level waste; Co-60, Lu-177 and Pu-238 are deliberately made in reactors; Am-241 grows in separated plutonium; Mo-99 is a fission product made in dedicated targets. Only some of these are actually harvested from spent fuel today; the sources read here document Hanford's Cs/Sr capsules and UK americium separation as the recovery examples.

---

## Q4. Heat and power from waste

### 4.1 RTGs, power levels, fuels
- SOURCED (Wikipedia, RTG): Pu-238 has 0.54-0.57 W/g and "has become the most widely used fuel for RTGs"; Sr-90 about 0.95 W/g, "the Soviet Union used it in terrestrial RTGs." Space RTG electrical outputs: SNAP-19 40.3 W, SNAP-27 73 W, MMRTG about 110 W, MHW-RTG 160 W, GPHS-RTG 300 W.
- Soviet terrestrial: "the Soviet Union built 1,007 RTGs to power uncrewed lighthouses and beacons on its Arctic coast by the late 1980s," largely unmaintained after 1991; decommissioning began 1996; "by 2021, all RTGs had been removed" (Wikipedia, SOURCED, secondary). Conflicts: the Beta-M page says only 482 recovered before 2014 and "dozens or hundreds" may remain unaccounted; Bellona (snippet) reports Russia said it had almost entirely rid itself of more than 1,000 sources by 2015. Not reconciled. Orphaned-source accident, December 2001, Lia, Georgia: three residents burned with acute radiation symptoms (Wikipedia Beta-M).
- Beta-M life: initially 10 years, extendable 5-10 years (Wikipedia Beta-M).

### 4.2 RTGs in Antarctica itself
- **SOURCED (US DOE final report, OSTI 1631097, April 2017):** the Soviet Antarctic Expedition used RTGs from the mid-1970s to power automated geophysical and meteorological stations in remote regions; "the remaining four unsecured RTGs" held Sr-90 with "a combined total activity of 80,000 curies"; one was deep in the interior and had become buried in the ice; on 18 May 2015 the research vessel *Akademik Fedorov* delivered RTGs from Antarctica to St. Petersburg; funding and technical oversight by the US DOE with the Russian Antarctic Expedition and Rosatom subsidiaries. The work fulfilled the Madrid Protocol requirement to remove unused radioactive material (snippet, UNVERIFIED). **DERIVED:** 80,000 Ci / 4 = about 20,000 Ci each, half a Beta-M's 40,000 Ci (the units differ in type, unknown).
- **SOURCED (Isoflex, citing a *Stuff* investigation):** "more than 45 small radioactive electricity generators" in Antarctica between 1961 and 2015, Sr-90, depleted-uranium shielding, "enough to run a simple weather station for 10 years or more."
- **UNVERIFIED (snippet):** a SNAP-7C 10 W Sr-90 generator in a US Navy weather station delivered to Antarctica December 1961. Location **NOT FOUND**.
- No RTG at McMurdo or the South Pole was found in the search (UNVERIFIED negative). The PM-3A reactor at McMurdo is separate (Q7).
- **NOT FOUND:** national programs other than the Soviet/Russian, US Navy and New Zealand-linked items above.

### 4.3 Decay heat as a resource
- Vitrified canister heat, UNVERIFIED (snippets): about 1.5-2 kW per canister at vitrification, about 500 W after 60 years (Andra); a German cask (CASTOR HAW) holds 28 canisters with a maximum 45 kW, about 1.6 kW each (GNS). WNA (SOURCED): "Each cask has up to 45 kW heat load"; HLW is defined by heat above 2 kW per cubic meter.
- Proposals to use it: a 2024 *Energies* study models extracting heat from HLW in a repository with an organic Rankine cycle and heat pump; the snippet gives "approximately 108 kWe per HLW canister 30 years after emplacement" plus 81 kWth for heating (UNVERIFIED). **Flag:** that is far above the roughly 1-2 kW thermal of a single canister quoted above, so the snippet's unit or basis (perhaps per many canisters) is probably misstated. A student study from the University of Michigan estimated dry-cask outlet air of 36-65 degrees C for a greenhouse (UNVERIFIED).
- **NOT FOUND:** any built or operating project using vitrified waste or dry-cask heat for district heating, greenhouses or power.

### 4.4 Radioisotope heater units and nuclear batteries
**NOT FOUND (not searched; budget):** radioisotope heater unit (RHU) power levels and Pu-238 content; betavoltaic and other "nuclear battery" products. Only the RTG/heat-source facts above were read.

---

## Q5. Irradiation uses relevant to cold chains and food

- **Sources, UNVERIFIED (snippets of Britannica and lecture materials):** the two common gamma sources are Co-60 and Cs-137; electron beams are a third option with limited penetration, "suitable only for foods of relatively shallow depth." Electron beams and X-ray machines use no radioisotope.
- **Doses, UNVERIFIED (snippets):** low dose (up to 1 kGy) for sprout inhibition, delayed ripening, insect control; potatoes and onions about 0.03-0.15 kGy (one source) or 0.06-0.2 kGy (Wikipedia); medium doses 1-10 kGy for pathogens such as Salmonella. A 1980 FAO/IAEA/WHO committee declared an average dose of 10 kGy safe; a 1997 group said foods irradiated at any dose are safe and no upper limit is needed.
- **Volume, UNVERIFIED (Wikipedia via snippet, no primary citation):** permitted in over 60 countries; about 500,000 t of food processed annually worldwide.
- **Sterilization, SOURCED (WNA):** Co-60 "widely used for gamma sterilization"; Cs-137 "for low-intensity gamma sterilization." Share of single-use medical goods sterilized by gamma: **NOT FOUND**.
- Co-60 supply: from CANDU reactor adjuster rods, about three years of irradiation per rod (WNA; snippet); Darlington Unit 1 producing Co-60 as of January 2025 and Argentina's Embalse refurbished to continue production for about 30 years (snippets, UNVERIFIED).
- **Spent-fuel-based irradiators: NOT FOUND.** No source read documents a spent-fuel irradiator in use. Cs-137 capsules from Hanford are the documented fission-product source (Q3), and they are held as waste, not sold as irradiator sources, per the sources read.
- **Shelf-life gains for produce and grain (quantified): NOT FOUND.** Only the dose categories and "sprout inhibition" and "delayed ripening" purposes were found. The IAEA food-irradiation page returned 402.

---

## Q6. What cannot be reused

### 6.1 Volumes
- **SOURCED (WNA):** "HLW accounts for just 3% of the volume, but 95% of the total radioactivity of produced waste"; ILW about 7% of volume and 4% of radioactivity; LLW about 90% of volume and 1% of radioactivity.
- **SOURCED (WNA, citing IAEA 2022, solid waste in storage):** HLW 29,000 m3; ILW 2,740,000 m3; LLW 1,471,000 m3; VLLW 2,918,000 m3.
- **UNVERIFIED (snippets):** France (Andra) about 1.76 million m3 of all radioactive waste at end of 2021; an older (end-2010) Andra chart said HLW is 96% of radioactivity and 0.2% of volume; an older Andra figure of 2 kg of radioactive waste per inhabitant per year (2009 edition).
- **Per gigawatt-year in cubic meters: NOT FOUND from a primary source.** Pieces available:
  - Spent fuel mass: about 25-30 t per 1,000 MWe-year (one snippet) or about 20 t (another) (UNVERIFIED, general web sources).
  - Vitrified waste after recycling: "only about three cubic meters per year" per reactor (Wikipedia "High-level waste" via snippet, UNVERIFIED), with decay heat about the same as the unreprocessed fuel. A CSD-V canister holds 150 liters (2004 COGEMA paper, snippet). **DERIVED:** 3 m3 / 0.15 m3 = about 20 canisters per reactor-year.
  - WNA gives the Western European vitrification capacity as "2500 canisters (1000 t) a year," canister about 1.3 m high, Sellafield "over 6000 canisters" produced (SOURCED). The "1000 t" unit is ambiguous (probably glass mass), so this cannot be reconciled to the 3 m3 figure from the pages read.
  - Direct disposal volume of unreprocessed fuel, in cubic meters: **NOT FOUND**.

### 6.2 Dry-cask interim storage
- **SOURCED (WNA):** fuel is cooled under water at least five years first; US dry storage since 1986; at least one-third of US used fuel is in dry casks; "As of the end of 2019, 3203 casks had been loaded at 72 interim spent fuel storage installations (ISFSIs) in the USA"; cask heat load up to 45 kW; the page gives a 100-year design life only for Holtec's HI-STORM MIC cask and "no general service life for dry casks."
- **UNVERIFIED (snippets of US Federal Register and NRC items):** the NRC's standard initial approval is 20 years with renewals; several cask designs were renewed for 40 years in 2023-2024 (FuelSolutions, NAC-UMS, NAC-MPC). Worldwide cask count: **NOT FOUND**.
- Cold-climate storage: **UNVERIFIED (snippet):** at Bilibino (Chukotka, permafrost), spent fuel moved from pools to dry storage after two pools were drained; the operator argues permafrost could suit disposal, but with no proof it stays stable for a million years (operator advocacy). The NRC found ambient temperature, wind and elevation change a ventilated cask's thermal performance (snippet). **NOT FOUND:** any cold-region-specific licensing standard for casks.

### 6.3 How long the activity lasts
- **SOURCED (WNA):** reprocessed HLW decays to the level of the original ore within 9,000 years versus 300,000 years for unreprocessed waste; heat and radioactivity fall by over 99% after about 40-50 years of storage; pyroprocessing waste projected 300 years but not operational.
- **SOURCED (ANS, Aug 2026):** Finland's regulator evaluated safety "over at least 100,000 years and up to 1 million years."

### 6.4 Final disposal concepts and status
- **Onkalo, Finland:** SOURCED (ANS, 10 August 2026): regulator STUK found "no obstacle to granting the facility an operating licence"; Posiva's goal is operational readiness by the end of 2026; design is an iron-copper canister, bentonite buffer and clay backfill; fuel from Loviisa and Olkiluoto. SOURCED (WNA, as fetched): operating licence granted October 2026, the first for a civil used-fuel deep geological repository; disposal not started until STUK confirms readiness; depth about 400 m. UNVERIFIED (search snippets): licence date 22 October 2026, runs to end-2070, cap of 6,500 tU. The ANS and WNA pages are consistent in time order (the ANS item predates the grant).
- **Sweden, Forsmark (KBS-3, about 500 m):** construction licence approved January 2022; surface works began January 2025; commissioning listed for the 2030s (WNA).
- **France, Cigeo:** licence application January 2023; ASNR favorable opinion December 2025; public inquiry May-July 2026 with a favorable opinion with two reservations in August 2026; commissioning listed for 2050 (WNA as fetched).
- **USA:** no HLW repository; WIPP takes transuranic waste (WNA).
- **Deep boreholes (WNA):** concepts in Denmark, Sweden, Switzerland, USA; none implemented; Sweden, Finland and the USA abandoned them largely on economic grounds; borehole to about 5,000 m with waste in the lower 2,000 m; Malaysia's effort halted September 2023 when rock broke away during liner installation; Ghana's licence still awaiting a security evaluation at end-2023.
- **Sub-seabed (WNA):** "has not been implemented anywhere and is not permitted by international agreements."
- **Heat limit of a repository (UNVERIFIED, Andra snippet):** Cigeo's design keeps the clay below 90 degrees C; a vitrified package gives off about 500 W after 60 years of interim storage.

---

## Q7. Antarctic and cold-region relevance

### 7.1 Treaty and Protocol text
- **Antarctic Treaty Article V:** UNVERIFIED (search snippets of several copies, matching): "Any nuclear explosions in Antarctica and the disposal there of radioactive waste material shall be prohibited." The full treaty text was not opened (NTI page returned 403).
- **Madrid Protocol, Annex III, Article 2(1) (SOURCED, read directly from the Secretariat PDF):** "The following wastes, if generated after entry into force of this Annex, shall be removed from the Antarctic Treaty area by the generator of such wastes: (a) radio-active materials; (b) electrical batteries; (c) fuel, both liquid and solid; ..." Article 1(4): "Wastes removed from the Antarctic Treaty area shall, to the maximum extent practicable, be returned to the country from which the activities generating the waste were organized or to any other country in which arrangements have been made for the disposal of such wastes in accordance with relevant international agreements." Article 1(3): "Waste storage, disposal and removal ... as well as recycling and source reduction, shall be essential considerations in the planning and conduct of activities." Article 1(5): past waste sites to be cleaned up unless removal would cause greater adverse environmental impact.
- **Joint Convention Article 27(2) (SOURCED, unofficial NUS text read directly):** "A Contracting Party shall not license the shipment of its spent fuel or radioactive waste to a destination south of latitude 60 degrees South for storage or disposal." (This restricts shipments into the area from Contracting Parties; it does not itself address material leaving.)

### 7.2 PM-3A at McMurdo
- **SOURCED (Atomic Insights, a pro-nuclear blog quoting a Navy history):** the Naval Facilities Engineering Command read the Antarctic Treaty as requiring complete removal of the plant, buildings and possibly contaminated soil; leaving the plant locked in place "was not considered an option"; work "declared complete in February, 1979"; the pressure vessel held "approximately 40,000 curies" and the rest of the plant about 5 curies; "More than 14,000 metric tons of soil was bulk packed on board ships," "less than 200 tons of which was considered radioactive for transportation purposes"; shipped to Port Hueneme, California, and later spread and paved as a parking lot; action level set at 10 picocuries per gram (against a US transport limit of 2,000), taken from a Soviet soil rule; dose estimate below 15 millirem per year, more probably about 6.
- UNVERIFIED (snippets): plant shut down September 1972 after a coolant leak; site released in May 1979 (a second source says February 1979); initial criticality 4 March 1962. Output in MW: **NOT FOUND**. Disposal destination of the pressure vessel: **NOT FOUND**.

### 7.3 Ice-sheet disposal proposals of the 1960s-70s
- **SOURCED (WNA):** the USA investigated ice-sheet disposal for heat-generating waste; "Since 1980 there has been no significant consideration of this option"; countries that signed the 1959 Antarctic Treaty, or committed to managing waste within their borders, rejected it; never implemented.
- **UNVERIFIED (snippets of the Journal of Glaciology and a newspaper):** B. Philberth proposed from the 1950s-60s placing reactor fission products on the ice of Antarctica or Greenland (containers near the surface, melting slowly down); Zeller, Angino and Saunders (1973, *Bulletin of the Atomic Scientists*) proposed an Antarctic ice-cap repository with containers melting to bedrock; critics argued bottom-lying containers could make the ice slide over its bed; Zeller was to present to SCAR in Cambridge in September 1974; K. Philberth, *Journal of Glaciology* 19(81), 1977, argued disposal in a small area (about 100 km2) on an ice divide, with retrievability and containment if the ice surged, and said the deposit would not affect ice-sheet stability. A 1990 *Polar Record* editorial (snippet) says the latest Treaty meeting accepted all major SCAR waste-disposal recommendations, reversing earlier practice of disposing waste in ice and at sea.
- **NOT FOUND:** the content of SCAR's 1974-75 resolution; the Antarctic Treaty Consultative Meeting recommendations of the 1970s; any single document stating why the ice-sheet idea was rejected beyond Treaty Article V. The Cambridge PDF pages returned 403; the openpolar page failed on a certificate error; none was bypassed.

---

# FINAL

## What the sources support
- About 96% of a light-water reactor's spent fuel by mass is uranium (about 95%) and plutonium (about 1%) that is chemically recoverable; reprocessing is commercial only in France, Russia and (historically) the UK, with Japan's Rokkasho not yet complete after 27 delays. MOX supplies about 5% of the world's new reactor fuel; 44 reactors have used it, 22 in France.
- Recycling cuts final high-level waste volume to about one-fifth (Orano, WNA; one WNA page says about 85%) and shortens the time to reach ore-level radiotoxicity from about 300,000 years to about 9,000 years (WNA). Plutonium recycling alone cuts long-term radiotoxicity only about five-fold (NEA 2002); a 100-fold cut needs multiple recycling with fast reactors or accelerator-driven systems at 0.1% losses and a century-scale commitment. Fast reactors operate commercially (BN-600, BN-800); minor-actinide burning and accelerator-driven transmutation remain at the test or construction stage (MYRRHA planned for 2036).
- Useful isotopes: Am-241 (smoke detectors; space power research), Co-60 (made in CANDU reactors, not a waste product), Cs-137 and Sr-90 (recovered fission products, held at Hanford as waste capsules; Sr-90 powered Soviet RTGs at 10 W electric per unit), Pu-238 (made by irradiating Np-237 at about 1.5 kg/yr target), Mo-99 and I-131 (fission products from research-reactor targets).
- Antarctic precedent: Madrid Protocol Annex III requires radioactive materials generated after entry into force to be removed from the Treaty area and returned to the country of origin or to a country with disposal arrangements; PM-3A was removed completely (14,000+ t of soil shipped); Soviet Sr-90 RTGs were removed in 2015 with US funding; the Joint Convention bars licensing shipments to south of 60 degrees S for storage or disposal.
- Remaining waste needs a repository: only Finland's Onkalo has a licence (October 2026), not yet receiving fuel; Sweden and France are in licensing or early construction; deep boreholes have not been implemented anywhere.

## What the sources do not support
- That all spent fuel is "reusable": the 96% is a recoverable-mass figure; reuse in practice is limited by plant capacity, MOX capacity (440 t/yr worldwide), and the one-time-or-few-times recycling in light-water reactors.
- That minor-actinide transmutation is demonstrated at commercial scale. That the ice-sheet idea has any current standing (none since 1980 per WNA).
- A heat or power product from vitrified waste: only modeling and student studies were found.

## NOT FOUND (queries logged below)
NPT Article IV/III text; IAEA safeguards glossary and timeliness goals from the IAEA itself; independent reprocessing cost comparison; share of recovered uranium actually reused; amount of Am-241 per smoke detector; Co-60 curies per year; tritium kilograms; Kr-85 capture or sale; capsule curies at Hanford; RHU and nuclear-battery facts (not searched); quantified shelf-life gains for irradiated produce or grain; spent-fuel irradiators; per-GWe-year waste volumes in cubic meters from a primary source; worldwide dry-cask count; cold-climate cask licensing; SCAR 1974-75 resolution and ATCM 1970s recommendations; ASTRID cancellation; CFR-600 current status; MYRRHA construction start; PM-3A MW output and pressure-vessel disposal site.

## Source conflicts noted
WNA pages: used-fuel discharged 448,000 t vs 430,000 t; HLW volume reduction one-fifth vs 85%. Orano says MOX makes 10% of French nuclear electricity, WNA says 10% of the French fleet. CFR-600 breeding ratio 1.1 (WNA) vs 1.2 (snippet). MYRRHA 57 MWt (2013) vs 100 MWth (2025). Soviet RTG recovery: all removed by 2021 (Wikipedia RTG page) vs 482 recovered and hundreds possibly missing (Beta-M page).

---

# SEARCH LOG (tool, exact query or URL, result, where a dead end died)

WS = WebSearch, WF = WebFetch. "Source" = the page itself failed; "query" = the search returned nothing useful. Total 83 calls (one to three over the 60-80 budget; the last were needed to read primary PDFs).

1. WS "World Nuclear Association processing of used nuclear fuel recycling 96% reusable" - partial (secondary pages; WNA page not returned).
2. WS "MOX fuel reactors worldwide number France Japan IAEA" - partial (Orano counts; no IAEA source).
3. WS "Orano La Hague recycling capacity 1,700 tonnes per year plutonium MOX Melox" - hit (snippets).
4. WF world-nuclear.org .../fuel-recycling/processing-of-used-nuclear-fuel - hit.
5. WF world-nuclear.org .../fuel-recycling/mixed-oxide-fuel-mox - hit.
6. WF world-nuclear.org .../nuclear-wastes/radioactive-waste-management - hit (no per-GWe-year figures).
7. WF world-nuclear.org .../nuclear-wastes/nuclear-waste-management - dead end at source (404).
8. WF world-nuclear.org .../nuclear-wastes/storage-and-disposal-of-radioactive-wastes - hit.
9. WF world-nuclear.org .../fuel-recycling/fast-neutron-reactors - dead end at source (404).
10. WS "World Nuclear Association fast neutron reactors BN-800 BN-600 CFR-600 status" - partial.
11. WS "Onkalo operating licence granted Finland spent fuel disposal Posiva 2026" - hit (snippets).
12. WS "Rokkasho reprocessing plant completion delayed 27th time fiscal 2026" - hit (snippets).
13. WF ans.org/news/2026-08-10/article-8280/onkalo-snf-repository-passes-safety-assessment/ - hit.
14. WF world-nuclear-news.org/articles/russian-fast-reactor-reaches-full-power - hit.
15. WF iaea.org/topics/spent-fuel-management/reprocessing - dead end at source (402).
16. WS "CFR-600 Xiapu fast reactor operation status plutonium breeding 2025" - partial.
17. WS "MYRRHA accelerator driven system status 2025 construction MINERVA SCK CEN transmutation" - partial.
18. WS "OECD NEA Accelerator-driven Systems and Fast Reactors in Advanced Nuclear Fuel Cycles transmutation minor actinides report" - hit.
19. WF world-nuclear-news.org/articles/chinese-fast-reactor-begins-high-power-operation - hit (it concerns CEFR).
20. WF world-nuclear-news.org/articles/myrrha-accelerates-towards-realisation - hit but 2013.
21. WF oecd-nea.org/jcms/pl_33830 - dead end at source (403).
22. WF atrium.in2p3.fr .../Myrrha_2025_EN.pdf - tool could not read; read directly with pdftotext - hit.
23. WF git2.oecd-nea.org/... (NEA ADS/FR PDF) - dead end at source (DNS failure, ENOTFOUND).
24. WS "Monju fast reactor decommissioning status Phenix shutdown 2009 ASTRID cancelled 2019 lessons" - partial (Monju only; Phenix/ASTRID dead end at query).
25. WF world-nuclear.org .../current-and-future-generation/fast-neutron-reactors - hit (first 100,000 of 125,391 characters read).
26. WF conference.sns.gov .../Accelerator-driven Systems (ADS) and Fast Reactors (FR)... .pdf - tool could not read; read directly with pdftotext - hit (NEA 2002 report).
27. WF world-nuclear.org .../radioisotopes-research/radioisotopes-in-medicine - hit.
28. WF world-nuclear.org .../radioisotopes-research/non-medical-applications-of-radioisotopes - dead end at source (404).
29. WF world-nuclear.org .../radioisotopes-research/radioisotopes-in-industry - hit.
30. WS "plutonium-238 production Oak Ridge HFIR neptunium-237 irradiation 1.5 kg per year goal NASA RTG" - hit.
31. WS "Soviet strontium-90 radioisotope thermoelectric generators lighthouses Arctic number orphaned IAEA Beta-M" - partial (no IAEA source).
32. WS "americium-241 radioisotope power ESA RTG europium UK National Nuclear Laboratory americium extraction from plutonium stockpile" - hit (snippets).
33. WF world-nuclear.org .../transport/nuclear-power-in-space - dead end at source (404).
34. WF en.wikipedia.org/wiki/Beta-M - hit.
35. WS "radioisotope thermoelectric generator Antarctica used McMurdo OR Mount Erebus OR "South Pole" OR Soviet RTG Antarctic station" - hit (no US-station RTG found).
36. WF osti.gov/biblio/1631097 - hit.
37. WF isoflex.com/news/965-radioactive-generators-powered-antarctic-science - hit.
38. WF world-nuclear.org .../non-medical-applications-of-nuclear-technologies - dead end at source (404).
39. WF en.wikipedia.org/wiki/Radioisotope_thermoelectric_generator - hit (first 100,000 of 172,897 characters read; no Antarctica mention in that part).
40. WF osti.gov/servlets/purl/1766431 - tool could not read; read directly with pdftotext - hit (ORNL Pu-238 process paper).
41. WF iaea.org/topics/food-irradiation - dead end at source (402).
42. WF documents.ats.aq/recatt/Att006_e.pdf - tool could not read the PDF; saved but not used (document identity unconfirmed).
43. WS "Antarctic Treaty 1959 Article V "disposal of radioactive waste material shall be prohibited" text" - hit (snippets; text not opened).
44. WS "PM-3A McMurdo nuclear power plant decommissioning radioactive waste shipped 1979 soil removed 438 barrels" - partial ("438 barrels" not supported; 438 was malfunctions).
45. WF ats.aq/e/protocol.html - partial (links only).
46. WF atomicinsights.com/how-clean-clean-blasting-out-frozen-soil/ - hit.
47. WF iaea.org/sites/default/files/infcirc546.pdf - dead end at source (402).
48. WF ats.aq/documents/recatt/Att010_e.pdf - redirect to documents.ats.aq (followed in call 51).
49. WS "Madrid Protocol Annex III Article 2 "radioactive materials" "shall be removed from the Antarctic Treaty area by the generator"" - hit (snippets).
50. WS "Joint Convention on the Safety of Spent Fuel Management Article 27 "south of latitude 60 degrees South" transboundary movement" - hit (snippets).
51. WF documents.ats.aq/recatt/Att010_e.pdf - tool could not read; read directly with pdftotext - hit (Annex III text).
52. WF cil.nus.edu.sg/.../1997-Joint-Convention-... .pdf - tool could not read; read directly with pdftotext - hit.
53. WS "Antarctic ice sheet nuclear waste disposal proposal 1970s Zeller Philberth self-burial ice sheet SCAR rejected" - partial.
54. WS "NRC dry cask storage certificate of compliance 40 years renewal 20 years ISFSI number of casks Nuclear Energy Institute 2024" - partial (no cask count).
55. WS "NPT Article IV reprocessing right IAEA safeguards plutonium separation non-nuclear-weapon state Japan Rokkasho safeguards approach" - partial (no NPT text).
56. WF cambridge.org/core/journals/journal-of-glaciology/article/disposal-of-radioactive-waste-in-ice-sheets/4BF2EA... - dead end at source (403).
57. WF un.org/disarmament/wmd/nuclear/npt/text - redirect to disarmament.unoda.org.
58. WF iaea.org/sites/default/files/iaea_safeguards_glossary.pdf - dead end at source (402).
59. WF disarmament.unoda.org/wmd/nuclear/npt/text - dead end at source (404).
60. WF cambridge.org/core/services/aop-cambridge-core/content/view/4BF2EA.../the-disposal-of-radioactive-waste-in-ice-sheets.pdf - dead end at source (403).
61. WS "IAEA significant quantity 8 kg plutonium timely detection goal reprocessing plant safeguards separated plutonium" - hit (secondary).
62. WF iaea.org/.../infcircs/1970/infcirc140.pdf - dead end at source (402).
63. WF openpolar.no/Record/crcambridgeupr:10.1017%2Fs0022143000031440 - dead end at source (certificate verification error).
64. WS "Antarctic Treaty Consultative Meeting 1975 OR 1977 recommendation radioactive waste disposal ice sheet Philberth SCAR conclusion not suitable "ice sheet" repository history" - partial (resolution content dead end at query and sources).
65. WF cambridge.org/.../disposal_of_radioactive_waste_in_ice_sheets.pdf - dead end at source (403).
66. WF nti.org/learn/treaties-and-regimes/antarctic-treaty/ - dead end at source (403).
67. WF world-nuclear.org .../radioactive-waste-management (second prompt on volumes) - hit (confirms no per-GWe-year volume; gives 85% reduction).
68. WS "Andra French inventory radioactive waste volume per inhabitant 2 kg per year per capita HLW cubic meters 2022 essential" - partial.
69. WS "spent fuel 20-25 tonnes per GWe year 1000 MWe reactor annual discharge cubic meters once-through versus recycling high-level waste volume" - partial.
70. WS "vitrified high-level waste decay heat kW per canister La Hague CSD-V cooling 50 years storage temperature" - partial.
71. WS "food irradiation IAEA FAO WHO cobalt-60 electron beam shelf life fruit potatoes onions sprouting dose 1 kGy volume irradiated tonnes worldwide" - partial.
72. WS "National Academies "Radiation Source Use and Replacement" cesium-137 chloride blood irradiators replace x-ray cobalt-60 supply Canada Russia" - partial.
73. WS "Hanford cesium strontium capsules WESF 1,936 capsules Cs-137 Sr-90 curies vitrification disposal decision DOE" - partial (curies not found).
74. WF nrc.gov/security/nas-facts-sheet.pdf - tool could not read; read directly with pdftotext - hit (fact sheet only).
75. WF ans.org/news/tag-waste management/step-1643722532 - partial (login wall).
76. WS "tritium production CANDU heavy water detritiation Darlington tritium removal facility kilograms tritium inventory Ontario sales" - partial (kilograms not found).
77. WS "krypton-85 reprocessing plants release curies half-life 10.76 years industrial use capture La Hague" - partial.
78. WS "dry cask storage spent fuel cold climate Canada OR Russia OR Finland OR Sweden permafrost Antarctic interim storage nuclear station cask Arctic" - partial.
79. WS "IAEA cobalt-60 production Candu adjuster rods annual supply million curies sterilization Nordion Bruce Power Mo-99 supply reactors 2025" - partial (no IAEA supply figures).
80. WF orano.group/en/the-expertise/recycling/expertise - hit.
81. WS "use of vitrified high-level radioactive waste decay heat as heat source district heating OR greenhouse OR "waste heat" proposal feasibility study" - partial (no built project).
82. WS "OECD NEA Mo-99 supply reactors worldwide 2025 six reactors produce 95% of supply HFR Petten BR2 SAFARI OPAL NRU" - hit (snippets).
83. WF oecd-nea.org/upload/docs/application/pdf/2025-10/7743_medical_radioisotopes_supply_rev.pdf - tool could not read; read directly with pdftotext - hit (95% of Mo-99 from Table 2 reactors).

Unsearched by budget or by oversight (so "NOT FOUND" for these means not looked for): radioisotope heater units, nuclear batteries (betavoltaics), Am-241 per smoke detector, Russian/Chinese reprocessing detail beyond the WNA table, Hanford capsule curies by a second angle, and a second-angle search on food-irradiation shelf-life data.

Local scratch (not in the repo): `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/886bca9e-5882-4ef6-bb9a-fa7f86df3ba8/scratchpad/r7/` holds the pdftotext conversions.
