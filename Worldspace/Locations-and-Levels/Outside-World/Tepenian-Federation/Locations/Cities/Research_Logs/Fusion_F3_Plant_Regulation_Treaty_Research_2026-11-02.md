# Fusion F3: plant designs, economics, regulation, treaty status, proliferation (research unit F3, 2026-11-02)

**Started 2026-11-02 18:50 MST. Finished 2026-11-02 19:00 MST (system clock).**
**Scope.** Facts only; no recommendation, design or ranking. Unit F3 of `Fusion_and_Helium3_Research_BRIEF_2026-11-02.md`: published fusion power-plant designs (net and thermal power, efficiency, heat rejection, availability); neutron damage, component lifetime and waste; cost estimates; siting; regulation of fusion versus fission; the Antarctic Treaty and the Madrid Protocol on nuclear power and waste (with the PM-3A precedent); and proliferation through fusion blankets. Labels: **SOURCED** (read at the source in this session), **DERIVED** (my arithmetic on sourced figures, working shown), **UNVERIFIED** (search snippet only, recalled, or inferred), **NOT FOUND** (looked for; queries in the log). Dates are the sources' own. The status date for anything that can change is 2026-11-02.

**Reading note on how documents were read.** Where WebFetch could not read a PDF (compressed binary), the tool saved the file and I extracted its text locally with `pdftotext`; those items are still SOURCED because I read the document's own text. Where WebFetch returned only a summary of a web page, the label says so.

## PROGRESS

- [x] Q1 Published plant designs (EU-DEMO, ARC, STEP, CFEDR, JA-DEMO, ARIES-ACT2 done; K-DEMO UNVERIFIED only; "US pilot-plant studies" other than ARIES-ACT2 not read)
- [x] Q2 Neutron damage, component lifetime, waste (waste classes, volumes, half-life drivers, decay heat; the loss-of-coolant argument is UNVERIFIED)
- [x] Q3 Cost estimates (two harmonized or historic sources read; most primary cost sources blocked)
- [x] Q4 Siting (one 2026 framework paper read; no cold-climate or polar fusion siting study found)
- [x] Q5 Regulation (US, UK, Japan, IAEA covered; EU is NOT FOUND; US final rule not found as of this date)
- [x] Q6 Antarctic Treaty and Madrid Protocol (primary texts quoted; PM-3A history; one 2026 legal white paper read)
- [x] Q7 Proliferation (two primary papers read as abstracts only)
- [x] FINAL section and search log

---

## Q1. Published power-plant designs

### 1.1 Summary table (all figures are the design's own, as published; designs differ in vintage and assumptions)

| Design | Fusion power | Net electric | Thermal-to-electric | Source and date | Label |
|---|---|---|---|---|---|
| **ARC** (MIT, 2015) | 525 MW | 190 MWe (abstract: "~200-250 MWe") | 0.40 at 900 K blanket outlet | Sorbom et al., arXiv:1409.3540v2, 16 Aug 2015; Fusion Eng. Des. 100:378 | SOURCED |
| **EU-DEMO, 2017 baseline** | 1998 MW | 500 MWe | 0.375 | Coleman et al., Nucl. Fusion 65 036039, published 28 Feb 2025, Table 6 | SOURCED |
| **EU-DEMO, 2024 proposal** | 1652 MW | 350 MWe | 0.316 | same paper, Table 6 | SOURCED |
| **STEP** (UK prototype plant) | 1.5-1.8 GW (flat-top) | "at least 100 MW", Q_eng "just above 1.0" | not given in the text I read | arXiv:2403.09460v1 (STEP flat-top operating space), Sections 1.2 and 2.2 | SOURCED |
| **JA-DEMO** (Japan, QST) | 1.4 GW | ~250 MW | about 0.34 DERIVED from a snippet-only 640 MW gross and 1,870 MW "effective heat output" (UNVERIFIED inputs) | Utoh, ISS2025, Nagasaki, 2-4 Dec 2025 (IEEE-CSC newsletter issue 63, Mar 2026) | SOURCED for 1.4 GW and ~250 MW |
| **CFEDR** (China) | 1510 MW (baseline "SAT1 15MA") | not given in what I read | not given | Qin slides, RFPPC2025, 19 May 2025 (IPP Greifswald host) | SOURCED |
| **ARIES-ACT2** (US, conservative) | 2640 MW | sized to "1000 MW electric" | ~44% (DCLL blanket) | Kessel and Poli, PPPL-5007, March 2014 | SOURCED |
| **K-DEMO** (Korea) | ~1,500 MW; R0 6.8 m; net >= 300 MW target | not verified | not verified | search snippets only | UNVERIFIED |

### 1.2 ARC (SOURCED; read in full text locally from the arXiv PDF)
- Table 1: fusion power 525 MW; total thermal power 708 MW; plant thermal efficiency 0.40; total electric power 283 MW; **net electric power 190 MW**; Q_e = 3.0; major radius 3.3 m; plasma semi-minor radius 1.13 m; plasma volume 141 m3; toroidal field 9.2 T; peak on-coil field 23 T; tritium breeding ratio 1.1; fusion power wall loading 2.5 MW/m2.
- Efficiency cases (Section 1): 900 K blanket outlet gives about 40% Brayton efficiency, P_net = 190 MW, Q_e = 3; 1100 K gives about 46%, P_net = 233 MW, Q_e = 3.5; a 1200 K "aggressive" case is also described.
- Quote: "the Q_e of the entire power plant will be lower than this estimate, but requires a full site design, which is beyond the scope of this paper."
- **DERIVED:** heat rejected to the environment at the Table 1 design point = 708 - 283 = **425 MW thermal** (before any plant-wide losses). Net-to-fusion ratio 190/525 = 0.36.
- **No capacity factor or availability figure appears in the paper** (searched the full text for "capacity factor", "availability"; only hits were generic).
- Costing (Section 6): a materials-based estimate, not a plant cost. Quote: "9.2 T ARC has a fifth of the ~$24B price of the 5.3 T ITER (calculated by applying the fabricated component scaling to the ~23,000 tonne ITER)"; ARC about one third of the cost of ARIES-RS (~$14B), which has about four times the electrical output. The balance of plant is excluded ("excluding the balance of plant equipment", Table 11 caption).
- Footprint: the paper does not give a site footprint (search of the text).

### 1.3 EU-DEMO (SOURCED from Coleman et al. 2025, Table 6 and text; Wikipedia as secondary context)
- 2017 baseline: P_fus 1998 MW, P_el,net 500 MWe, R0 8.94 m, A 3.1, eta_th 0.375, pulse 2.0 h. 2024 proposal: P_fus 1652 MW, P_el,net 350 MWe, R0 8.60 m, A 2.8, eta_th 0.316, pulse 2.11 h, confinement margin 0.110.
- Stakeholder requirement quoted from the paper: 300 <= P_el,net <= 500 MWe and pulse >= 2 h.
- The authors say the confinement margin "is tantamount to a reduction of ~150 MWe" at the same geometry (Section 7). A WCLL-blanket versus HCPB-blanket discrepancy is noted in the paper (420 MWe in Section 5.3 versus 485 MWe in Table E.8 for HCPB 2024 at A = 2.8; the paper does not reconcile them).
- **DERIVED:** P_el,net/P_fus = 0.25 (2017) and 0.21 (2024); the paper footnote gives 0.248 for 2017.
- Plant availability and gross thermal power for the 2024 point are not stated in the parts I read (the second half of the page text was read; availability not found there).
- Wikipedia (secondary, UNVERIFIED as to origin): "operation is planned to begin in 2051, per EUROfusion"; an older (1980s NET) concept had 628 MWe net and 2200 MW gross thermal.
- The older 2014 EU materials assessment (Stork et al., arXiv:1408.3546) states a near-term DEMO goal of "~500MW of net electricity generation to the grid" and "a fully-closed tritium fuel cycle" (SOURCED).

### 1.4 STEP (UK)
- SOURCED (arXiv:2403.09460v1): fusion power "aims for a range of 1.5 - 1.8 GW" in flat-top; "net steady-state electric power output of at least 100 MW"; Q_eng "just above 1.0"; Q_sci recommended limit >~ 11; R_geo = 3.6 m; minor radius 2.0 m; aspect ratio 1.8; elongation 2.8; B_geo = 3.2 T; flat-top plasma current about 20 MA (agreed limit 25 MA, scans at 23 MA). The text gave no number for heat-to-electricity efficiency.
- **DERIVED:** net/fusion = 100/1,800 = 0.056 to 100/1,500 = 0.067 (an unusually low ratio, consistent with Q_eng just above 1).
- Wikipedia (secondary, summarizing STEP Fusion and UKAEA pages retrieved 23 Jan 2026): operation 2040; Phase 2 (detailed design) 2025-2032; Phase 3 (construction and commissioning) 2032-2040; site the former West Burton A coal-fired station, Nottinghamshire; GBP 2.5 billion additional investment announced in 2025 "not a total project cost". UNVERIFIED beyond the aggregator; search snippets from STEP Fusion and gov.uk agree on West Burton and the 2040 target.
- The IAEA FEC 2025 STEP slides (Wilson) and manuscript returned HTTP 403 (died at the source).

### 1.5 JA-DEMO and CFEDR
- JA-DEMO (SOURCED, Utoh, ISS2025): R_p/a_p 8.5 m / 2.4 m; aspect ratio 3.5; fusion output 1.4 GW; net electric ~250 MW; plasma current 12.3 MA; B_T on axis 6.0 T; B_max ~14 T. The same deck gives a three-phase ITER-size path: Phase I fusion 500-540 MW with P_net about 0-11 MWe; Phase III P_net > 0 "(~100 MW)" with a table value of 107 MWe net, 342 MW gross, 917 MW fusion. Timeline in the deck: Cabinet Office "demonstration of power generation in the 2030s".
- JA-DEMO snippet-only figures (UNVERIFIED, from a search-result excerpt of the Takenaga IAEA FEC 2025 paper; the paper itself was 403): fusion 1,500 MW, effective heat output 1,870 MW, gross electric 640 MW, on-site use 390 MW, net 250 MW, availability target 70%. **DERIVED from those snippet inputs:** recirculating share 390/640 = 0.61 of gross; gross/heat = 640/1,870 = 0.34.
- CFEDR (SOURCED, Qin slides, 19 May 2025): baseline R0 7.8 m, a 2.5 m, B0 6.3 T, P_fus 1510 MW, beta_n 2.56. Stage goals on the slide: "I: DEMO validation, Q>10, CW, 1-2GW, >20 dpa"; "II: Q>30, steady state, TBR>1, >2-3GW, >50 dpa". CFETR engineering design "completed": Phase I Q=10, 400 s, 500 MW; Phase II Q=5, 3000 s, 350 MW. CRAFT construction launched 2019; its commissioning "will be finished at the end of 2025". No CFEDR net electric figure in what I read.

### 1.6 ARIES-ACT2 (US, SOURCED, PPPL-5007, March 2014)
- Conservative physics and conservative technology; aspect ratio 4.0; Dual Coolant Lead-Lithium blanket and He-cooled tungsten divertor; "thermal conversion efficiency of ~ 44%"; auxiliary systems 32 MW; operating points "cost determined and filtered to provide 1000 MW electric power operating points"; fusion power of 2640 MW. **DERIVED check:** 2,640 MW / (17.6 MeV x 1.602e-13 J/MeV) = 9.36e20 reactions per second; the report states 9.38e20.
- A 2024 arXiv study of fusion plant value (arXiv:2405.01514v2, SOURCED) quotes availability figures from earlier studies: DEMO-related studies "roughly 75%"; ARIES-CS "roughly 85%"; US fission fleet "about 90%"; and its own conclusion that designs "were previously assumed to reach about 80% availability".

### 1.7 Availability, capacity factor and replacement downtime
- EU DEMO planning (Stork et al. 2014, SOURCED): target machine availabilities "30% for Phase I and 50% for Phase II".
- From arXiv:2405.01514v2 (SOURCED, as it cites others): Nagy 2009, about 70 days to replace divertors after 2 full-power years; Crofts 2014, about 8 months for blanket and divertor replacement after 4 full-power years, falling from 22 months with one remote-handling system to 3.2 months with eight.
- Mulder, Melese and Lopes Cardozo, Nucl. Fusion 61:046032 (2021), "Plant efficiency: a sensitivity analysis of the capacity factor for fusion power plants with high recirculated power": SOURCED as to title and abstract only; it argues designs need a low recirculated-power fraction and links poor plant efficiency to "high recirculated power combined with a low capacity factor". Numbers not read.

### 1.8 Footprint, heat rejection and cooling water
- No fusion-plant site footprint (hectares) found in any source I could read. **NOT FOUND.**
- Heat rejection is the thermal power minus the electric output. ARC DERIVED: 425 MW thermal. **DERIVED, assumptions stated:** if all 425 MW were rejected to once-through water with a heat capacity of 4,186 J/kg/K, the flow would be 425e6 / (4,186 x 10 K) = 10.2 m3/s for a 10 K rise, or 20.3 m3/s for a 5 K rise. This is plain heat-balance arithmetic, not a published fusion requirement.
- UNVERIFIED (search snippet of a 2008 ITER cooling-tower paper): cooling-tower system designed to reject up to 450 MW, four towers, for 350 MW of fusion power. Not read.
- The 2026 siting paper (Q4) lists "access to abundant cooling water" among fusion siting needs but gives no volume.
- **Cold-climate effect on efficiency: NOT FOUND for fusion.** A snippet from an IPP Greifswald FAQ states that higher coolant temperature raises conversion efficiency (UNVERIFIED, snippet); this is a statement about the hot side.

### 1.9 Scale arithmetic against the setting (DERIVED)
Plants of each published net electric size needed for the setting's 101.7 GW national electricity and 324 GW tower net figure, with no capacity-factor adjustment: 

| Design net output | Plants for 101.7 GW | Plants for 324 GW |
|---|---|---|
| ARC 190 MWe | 535 | 1,705 |
| EU-DEMO 2024 350 MWe | 291 | 926 |
| EU-DEMO 2017 500 MWe | 204 | 648 |
| JA-DEMO ~250 MWe | 407 | 1,296 |
| STEP 100 MWe | 1,017 | 3,240 |
| ARIES-ACT2 1,000 MWe | 102 | 324 |

Working: 101.7 GW / plant GWe, and 324 GW / plant GWe. These are first-of-a-kind or demonstration designs; no source I read gives a mature commercial-fleet net size.

---

## Q2. Neutron damage, component lifetime and waste

### 2.1 Replacement intervals and damage rates
- **IAEA-led waste review** (Gonzalez de Vicente et al., Nucl. Fusion 62 (2022) 085001, published 30 May 2022; SOURCED): "The FW/blanket and divertor are expected to be replaced every 5-10 years, depending on the neutron wall loading and operational schedule." (Section 1.)
- **EU assessment of materials for a near-term DEMO** (Stork et al., arXiv:1408.3546, 2014; SOURCED, read locally): starter blanket first wall "capable of withstanding >=2MW.yr.m-2 fusion neutron fluence (~20 dpa in the front-wall steel)"; Phase II >= 50 dpa steel damage; "a level of 15dpa/fpy corresponds to >= 1.33 full power years of operation in Phase I"; first-wall steel damage scaled to a 1.8 GWth concept "~ 12 dpa/fpy"; transmutation helium "~12 appm/dpa"; divertor figures "~3 dpa/fpy"; divertor structures "feasible engineering structures to last for 2 fpy in operation unless erosion is significantly enhanced"; ITER-grade 316L vacuum vessel assumed over a 30 fpy lifetime. These are 2014 planning assumptions, not measurements.
- **ARC** (SOURCED): Table 9 damage in one full-power year: inner vacuum vessel 44 dpa with 280 He ppm; outer vessel 26 dpa with 140 He ppm; blanket tank 0.14 dpa; support column 3.0 dpa. Quotes: ferritic-steel irradiation lifetime "estimated at 150-200 DPA"; the vacuum vessel (Inconel 718) is expected to "survive for at least 6-12 months"; the blanket tank "would need replaced after only two years" because rewelding becomes problematic near 1 He appm; magnets reach the Nb3Sn-based fluence limit of 3x10^18 neutrons/cm2 after "9 Full-Power Years" with a TiH2 shield, described by the authors as "likely insufficient for a dedicated, commercial-scale power plant" and extendable by a small increase in size.
- **Solid material mass in the vessel (ARC):** "85 metric tons (~11 m3) of solid material compared to over 2000 metric tons in ITER", and a claim that the liquid blanket "can reduce the amount of solid radioactive waste by a factor of ~20".

### 2.2 Waste classes, volumes, half-lives (SOURCED, Gonzalez de Vicente et al. 2022)
- Abstract: "Fusion waste is significantly different to fission NPP waste, i.e. the quantity of fusion waste is much larger. However, it mostly comprises low-level waste (LLW) and intermediate level waste (ILW). Notably, the waste does not contain many long-lived isotopes, mainly tritium and other activation isotopes but no-transuranic elements." "Fusion power should be able to avoid creating high-level waste, while the volume of fusion ILW and LLW will be significant, both in terms of pure volume and volume per unit of electricity produced."
- Long-lived contributors named: isotopes from niobium, molybdenum, nickel, carbon, nitrogen, copper and aluminum and impurities (K, Co, Ag), which "might preclude disposal in LLW repositories".
- Volumes: "DEMO may produce as much as 10 000 t of solid waste from in-vessel components alone [16], compared to around only 2000 t from ESFR [15] plus an estimated 300 t of spent fuel ... resulting in ~2500 t of waste (HLW, ILW)" (ESFR = the European sodium-cooled fast reactor). The authors read this as "a significantly greater waste burden from fusion in comparison to fission reactors developed on the same timescales" but say the fission waste is "much longer-lived actinide waste". The review's Figure 3 compares power-core volumes only, "not the lifetime waste generation".
- Clearance: "all in-vessel components are not clearable as their clearance indices (CIs) exceed the limit of unity by a wide margin even after a period of 100 years"; the main contributor at 100 years for reduced-activation steel is Nb-94 (from niobium impurity). The biological shield and some magnet constituents are clearable, "representing ~65% of the total volume of ARIES-ACT2 radioactive materials".
- Recycling: "all fusion components could be recycled in less than a year with advanced RH equipment" (a design-study claim). Tritium decay storage before disposal: "up to 50 years" or "very long (about 100 years)" depending on initial tritium activity.
- Decay heat: the review lists "lower decay heat to be removed" among the differences from fission (SOURCED as a statement; no decay-heat number read).
- Regulatory status of waste standards: "In the absence of official standards and guidelines for nuclear fusion plants, fusion designers adopted, as far as possible, well-established standards for fission-based nuclear power plants."
- **DERIVED comparison caution:** the 10,000 t versus 2,500 t figures compare DEMO in-vessel solids with ESFR structural waste plus spent fuel; they are not per-GWh figures, and the review itself says a per-unit-electricity comparison is what matters. I found no per-plant-year or per-GWh figure. **NOT FOUND:** activated waste volume per plant-year.
- Search snippets (UNVERIFIED, not read): ARIES-era studies expect most plants to generate Class A or C low-level waste under US rules if materials are chosen carefully; a 2006 comparison suggested fusion radiotoxicity indices become comparable with fission's after 100 to 500 years, 4 to 5 orders of magnitude lower. These were not confirmed.

### 2.3 Decay heat and the loss-of-coolant argument
- UNVERIFIED (search snippets only): the SEAFP study (Andritsos and Zucchetti, 1997-1998) concluded decay heat can be removed passively even in a total loss-of-coolant case; ARIES-ACT safety analysis (Humrickhouse and Merrill, 2015) found secondary confinement not challenged and passive removal possible; ARIES-RS authors (Mogahed et al.) concluded a passive afterheat removal system is needed. An EU-DEMO note says hydrogen from steam reacting with hot plasma-facing materials remains a hazard under study. I did not open any of these. The only SOURCED statement on decay heat is the IAEA-led review's "lower decay heat" line above, and ARC's statement that its blanket tank, not its vacuum vessel, is the primary nuclear safety barrier ("both the activated vessel and the tritium-containing FLiBe inside of it would still be contained").

---

## Q3. Cost estimates

- **Harmonized review, 2026** (SOURCED as to the abstract on arXiv; numbers from the EmergentMind summary of the same paper, UNVERIFIED against the paper's PDF): Böhnlein, Böse, von Hirschhausen, Kemfert and Wimmers, "Too cheap to meter? A stochastic analysis of projected future fusion costs", arXiv:2606.26536, submitted 25 June 2026. Abstract summary: mean LCOE for mature technologies of "roughly 110 to 144 USD/MWh", learning rates above 30%; the authors call these projections optimistic compared with other literature and with fission. EmergentMind adds: 590 records from 56 sources, constant 2018 USD; MCF mature mean $114.6/MWh, ICF $110.3, MIF $143.9; median first-of-a-kind MCF $206.7/MWh; reducing WACC from 7% to 3% lowers LCOE by about 19-38%. No overnight capital cost figures in what I read.
- **National Academies, "Bringing Fusion to the U.S. Grid" (2021):** SOURCED from the introduction chapter: the pilot plant is aimed at electricity "at the lowest possible capital cost" and is "not meant to demonstrate the economic viability of the commercial plant"; no cost-of-electricity target in the chapter I read. UNVERIFIED (a slide-deck snippet): "A fusion pilot plant should have a generating power >50 MWe and total overnight construction cost <5-6 B$"; recommendation to produce net electricity in a pilot plant in the 2035-2040 timeframe.
- **EU PPCS (2005), cost of electricity** (UNVERIFIED; search snippet of an IAEA conference paper; the full paper returned HTTP 402): Model A 5-9, Model B 5-9 (another summary says 4-8), Model C 4-7, Model D 3-5 eurocents/kWh.
- **ARC materials-based figures:** see Q1.2 (about one fifth of an applied-scaling ITER cost of about $24B; no balance of plant).
- **Not read or not found:** IEA, UK government and EPRI capital-cost-per-kWe estimates; ARIES-ACT2 cost of electricity; the EUROfusion "Economic Viability of Fusion" document (TLS certificate error). A snippet-only secondary blog (Prime Movers Lab, 2020) gave 150 MW plants at an average of $1.3B (2016 USD); this is UNVERIFIED and I do not carry its derived per-kWe figure forward. A snippet states an MIT thesis estimated LCOE between $140 and $550/MWh (UNVERIFIED).
- **NOT FOUND:** a primary, dated, assumption-stated capital cost per kWe for any of the Q1 designs.

---

## Q4. Siting

- **SOURCED** (Abdussami, Daley, Hoelzle and Verma, "A Framework for Evaluating the Siting of Fusion Power: Case Study on the Retired Coal Sites in the United States", arXiv:2606.01344v1, metadata dated 2 June 2026; read locally): fusion siting needs listed as "high electrical interconnection capacity, precision cooling, and minimal seismic interference"; also "stable seismic and geological conditions, access to abundant cooling water, availability of skilled technical labor, and proximity to existing" infrastructure; the paper's multi-criteria model includes a Safe Shutdown Earthquake sub-criterion, a 100-year flood sub-criterion, open waters and wetlands, population distance, slope; one passage says a site "above 0.3g" does not benefit from the earthquake sub-criterion. It states that fission siting "primarily designed around managing risks from high-level radioactive waste, large exclusion zones, and continuous fuel-cycle logistics ... concerns that are minimal or absent in fusion systems", and that fusion has "far smaller offsite radiological risk profiles and greater siting flexibility". Siting for ITER in Spain (Medrano et al.) considered "land, geological characteristics, freshwater supply, sanitary and industrial sewage, heat sink, electrical power supply, and transport and shipping".
- Siting by regulation: the NRC proposed rule (Q5.1) requires an applicant to evaluate whether the maximum offsite dose could exceed 1 rem and, only if so, to provide an offsite emergency plan; no exclusion-zone size is set in the summary I read.
- **NOT FOUND:** any cold-climate, polar or Antarctic fusion siting study; any coastal-rock or ice-sheet siting criterion for fusion; any published fusion plant land area. (Queries in log.) Search-snippet items only (UNVERIFIED): a University of Khartoum study of 92 locations found tropical ambient temperature exceeds polar by 26 C for conventional thermal plants; this is not about fusion.

---

## Q5. Regulation: how fusion differs from fission

### 5.1 United States
- **SOURCED** (Federal Register Vol. 91, No. 38, 26 February 2026, pp. 9476-9498, "Regulatory Framework for Fusion Machines", docket NRC-2023-0071, RIN 3150-AL00, proposed rule; read through the first 100,000 characters via the page summary): the **ADVANCE Act of 2024 (Public Law 118-67)** amended the Atomic Energy Act so that material made radioactive by a fusion machine is **byproduct material under section 11e.(3)(B)**; the rule treats fusion machines as a subset of particle accelerators; the Commission chose the byproduct-material approach (its Option 2) over a utilization-facility approach under Part 53. Comments were due 27 May 2026. New definitions go into 10 CFR 20.1003 and 30.4. The rule is "not intended for speculative fusion technologies" and "not intended to address the licensing of a standard fusion machine design or the approval of mass production".
- **Tritium (SOURCED):** reporting uses existing thresholds under 10 CFR 30.55(c) and 20.2201; tritium used or produced by fusion machines "is not considered a risk-significant radionuclide under part 37".
- **Activated components (SOURCED):** activation products not listed in Appendix A to Part 37 may need extra security, decided case by case through license conditions or orders.
- **Waste (SOURCED):** a proposed change to 10 CFR 20.2008(a) would allow certain fusion machine waste to go to LLW disposal facilities, either if it matches a 10 CFR 61.7 waste class description or if it goes to a site with a completed site-specific intrusion assessment (inadvertent-intruder dose no more than 0.5 rem per year); the 10 CFR 61.55 classification tables are not revised.
- **Emergency planning (SOURCED):** the maximum offsite dose test above (1 rem).
- **Status on 2026-11-02:** I found no final rule. Search results (UNVERIFIED as a negative) show the proposed stage, an NRC plan to publish a final rule in "fall 2026", a unified-agenda target of October 2026, and the statutory deadline of 31 December 2027 under NEIMA. The NRC rulemaking-status page itself returned HTTP 403.
- Search-snippet only: a law-firm note titled "The Nuclear Regulatory Commission unanimously votes to separate fusion energy regulation from nuclear fission" (a 2023 Commission decision; date UNVERIFIED); a K&L Gates note dated 19 Aug 2026 that Tennessee established a state fusion framework (UNVERIFIED, not opened).

### 5.2 United Kingdom
- **SOURCED** (legislation.gov.uk, Energy Act 2023 section 156): new Nuclear Installations Act 1965 subsection (2A): "Subsection (1) does not apply to a fusion energy facility." The definition (2B): a site "used for the purpose of installing or operating any plant designed or adapted for the production of electrical energy or heat by fusion, and not also used for the purpose of installing or operating a nuclear reactor." The page has no tritium provision. Commencement 10 September 2024 (snippet, UNVERIFIED).
- UNVERIFIED (search snippets of government guidance): fusion is regulated mainly by the Health and Safety Executive and the Environment Agency, not the Office for Nuclear Regulation; ionising radiation for fusion energy is "not currently a justified practice" in the UK; a justification application was submitted 15 December 2025 by UKIFS (since renamed UK Fusion Energy); a proposed fusion National Policy Statement is in consultation.

### 5.3 Japan
- UNVERIFIED (snippets of a law-firm bulletin and Cabinet Office slides): no comprehensive fusion statute; a Cabinet Office task force's draft position (NRA slides, November 2025) is that fusion devices with risks comparable to existing ones fall under the Radioisotope Act for now; regulatory-issue compilation by end of the fiscal year; the UK-Japan-Canada "Agile Nations" group (October 2023) recommended proportionate, technology-independent regulation.

### 5.4 EU
- **NOT FOUND:** the legal status of fusion under the Euratom Treaty and the EU nuclear safety directive. Snippets only (UNVERIFIED): a May 2026 EPRS briefing says the Commission is expected to publish a fusion strategy in 2026; a July 2026 open letter still called it upcoming and asked for a fusion-specific regulation distinct from fission; the 2026-2027 Euratom Work Programme (March 2026) gives EUR 222 million to fusion. The EPRS page itself returned 404 on fetch.

### 5.5 IAEA
- UNVERIFIED (snippets of IAEA pages and a Nov 2025 Vienna session; the IAEA page returned HTTP 402): there are no fusion-specific IAEA safety standards; the Agency said in 2023 it aims to begin developing them "later this decade"; a Safety Report Series volume "Safety and Regulation Considerations for Fusion Facilities" is in preparation; a session abstract states "up to now, no country has such higher-level fusion specific regulatory requirements". The one IAEA-authored paper I did read (the 2022 waste review) says designers use fission standards in the absence of fusion standards.

---

## Q6. The Antarctic Treaty and the Madrid Protocol

**Brief's citation note.** The brief asks for "Article 1(c) of the Antarctic Treaty". Article I of the Antarctic Treaty has paragraphs 1 and 2 only, with no lettered sub-paragraph (c). The provisions that matter for nuclear matters are **Article I** (peaceful purposes) and **Article V** (nuclear explosions and radioactive waste). Both are quoted in full below. (Article IV(1)(c), on recognition of claims, is a separate provision not about nuclear matters.)

### 6.1 Antarctic Treaty, verbatim (SOURCED; official text, documents.ats.aq/recatt/att005_e.pdf)
**Article I**
> "1. Antarctica shall be used for peaceful purposes only. There shall be prohibited, inter alia, any measures of a military nature, such as the establishment of military bases and fortifications, the carrying out of military maneuvers, as well as the testing of any type of weapons.
> 2. The present Treaty shall not prevent the use of military personnel or equipment for scientific research or for any other peaceful purpose."

**Article V**
> "1. Any nuclear explosions in Antarctica and the disposal there of radioactive waste material shall be prohibited.
> 2. In the event of the conclusion of international agreements concerning the use of nuclear energy, including nuclear explosions and the disposal of radioactive waste material, to which all of the Contracting Parties whose representatives are entitled to participate in the meetings provided for under Article IX are parties, the rules established under such agreements shall apply in Antarctica."

**Article VI (area):** "The provisions of the present Treaty shall apply to the area south of 60 deg South Latitude, including all ice shelves ..."

### 6.2 Protocol on Environmental Protection (Madrid Protocol), verbatim (SOURCED; official text, documents.ats.aq/recatt/Att006_e.pdf; the Annex from Att010_e.pdf)
**Article 2:** "The Parties commit themselves to the comprehensive protection of the Antarctic environment and dependent and associated ecosystems and hereby designate Antarctica as a natural reserve, devoted to peace and science."

**Article 3(1):** "The protection of the Antarctic environment and dependent and associated ecosystems and the intrinsic value of Antarctica, including its wilderness and aesthetic values and its value as an area for the conduct of scientific research, in particular research essential to understanding the global environment, shall be fundamental considerations in the planning and conduct of all activities in the Antarctic Treaty area."

**Article 3(2)(b)** requires activities to be planned and conducted "so as to avoid: (i) adverse effects on climate or weather patterns; (ii) significant adverse effects on air or water quality; (iii) significant changes in the atmospheric, terrestrial (including aquatic), glacial or marine environments; ... or (vi) degradation of, or substantial risk to, areas of biological, scientific, historic, aesthetic or wilderness significance". Article 3(2)(c)(vi) lists "whether there exists the capacity to respond promptly and effectively to accidents, particularly those with potential environmental effects".

**Article 7 (mining):** "Any activity relating to mineral resources, other than scientific research, shall be prohibited."

**Article 8(1)-(3):** proposed activities are subject to Annex I prior assessment "according to whether those activities are identified as having: (a) less than a minor or transitory impact; (b) a minor or transitory impact; or (c) more than a minor or transitory impact", and the procedures "shall apply to any change in an activity ... from the addition of an activity, the decommissioning of a facility, or otherwise."

**Article 25(2):** "If, after the expiration of 50 years from the date of entry into force of this Protocol, any of the Antarctic Treaty Consultative Parties so requests ... a conference shall be held as soon as practicable to review the operation of this Protocol." (Entry into force: 1998 per the Kobe white paper, so the earliest review request falls in 2048, DERIVED 1998 + 50.) Article 8(5)(a): the Article 7 prohibition "shall continue unless there is in force a binding legal regime on Antarctic mineral resource activities".

**Annex III (Waste Disposal and Waste Management), Article 2(1):** "The following wastes, if generated after entry into force of this Annex, shall be removed from the Antarctic Treaty area by the generator of such wastes: (a) radio-active materials; (b) electrical batteries; (c) fuel, both liquid and solid; ..." **Annex III Article 1(4):** "Wastes removed from the Antarctic Treaty area shall, to the maximum extent practicable, be returned to the country from which the activities generating the waste were organized or to any other country in which arrangements have been made for the disposal of such wastes in accordance with relevant international agreements." **Article 1(5):** past and present waste disposal sites and abandoned work sites "shall be cleaned up by the generator of such wastes and the user of such sites", except where removal would cause greater harm or concerns a historic site. Annex III applies to activities for which advance notice is required under Article VII(5) of the Treaty, "including associated logistic support activities".

The Protocol text contains **no use of the words "nuclear" or "reactor"** (search of the saved Protocol text for "nuclear" found no match in the Protocol; the only hits in the Treaty file were Article V). The word "radio-active materials" appears in Annex III Article 2(1)(a).

### 6.3 How the literature reads these for power reactors
- **SOURCED, McGee and Shibata, "Beyond Article V: Nuclear Use and Environmental Assessment in Antarctica", Antarctic Governance White Paper Series No. 1, May 2026** (Kobe University PCRC; authors from the University of Tasmania and Kobe University): "The Antarctic Treaty's Article V prohibits nuclear explosions and radioactive waste disposal in Antarctica, but is silent on controlled nuclear technologies - reactors, nuclear-powered vessels, and radioisotope devices." "Controlled nuclear reactions - including use of nuclear reactors ... - do not constitute 'nuclear explosions' and are therefore not prohibited by the Treaty. This was confirmed in practice between 1962-72, when the US operated a small nuclear reactor at McMurdo Station." Also: the Protocol "has never been systematically applied to nuclear-related activities involving controlled nuclear reactions" because the McMurdo reactor was decommissioned in 1972 and the Protocol entered into force in 1998; the authors propose a consensus text presuming that reactors, nuclear-powered vessels or radioisotope devices require at least an Initial or Comprehensive Environmental Evaluation under Annex I. They state that the 1997 Joint Convention "prohibit[s] shipment of spent fuel or radioactive waste to the area below 60 degrees South Latitude and also for 'storage'" (their citation: Joint Convention 1997, Article 27(2); I did not read the Convention itself). They note a 2020 Russian plan to use the nuclear icebreaker Sevmorput for Vostok Station, aborted for mechanical reasons, with no public record of an environmental assessment. Their reading is an academic proposal, not an ATCM decision.
- **SOURCED primary negotiating record:** U.S. State Department, Foreign Relations of the United States 1958-60, vol. II, document 324, memorandum by Herman Phleger to Livingston Merchant, 28 November 1959: the Heads of Delegations "agreed" that the Article V text "contained no prohibition whatever of the peaceful use of nuclear material in Antarctica other than for explosions" (quotation as returned by the page summary; the sentence structure was relayed in the tool's paraphrase around the quote). The same record notes the only change from earlier text was that radioactive waste produced in Antarctica would have to be disposed of elsewhere than in Antarctica.
- **Effect of the text on fusion (DERIVED from the quoted texts; not a legal opinion and not stated in any source I read):** Article V bans "nuclear explosions" and "disposal there of radioactive waste material". Annex III Article 2(1)(a) requires removal of "radio-active materials" generated by covered activities. None of the sources I read addresses fusion plants specifically. **NOT FOUND:** any ATCM working paper, Information Paper or scholarly article that analyzes a fusion plant, as distinct from a fission reactor, in Antarctica.
- **Setting-relevant observation (DERIVED from the above, not a source claim):** the 2564-2812 Tepenian setting is far beyond the Protocol's own earliest review window (2048); the sources say nothing about what treaty regime would exist then.

### 6.4 PM-3A precedent
- **SOURCED** (Hanne E. F. Nielsen, "Remembering Antarctica's nuclear past with 'Nukey Poo'", phys.org / The Conversation, 23 July 2018; read in full): "Between 1961 and 1972 McMurdo Station was home to Antarctica's first and only portable nuclear reactor, known as PM-3A, or 'Nukey Poo.'" It "began producing power for the McMurdo station in 1962, and was refuelled for the first time in 1964." The plant "required a 25-man team"; chloride stress corrosion concern after "wet insulation" was found in a routine inspection; "Both costs and environmental impacts conspired to close the plant in September 1972." The cleanup "saw 12,000 tonnes of contaminated rock removed and shipped back to the USA through nuclear-free New Zealand" and "required the development of new standards for soil contamination levels". The site is a Historic Site and Monument under the Antarctic Treaty System; "all that physically remains ... is a missing hillside and a plaque."
- **SOURCED but secondary** (Wikipedia, PM-3A page summary): criticality 3 March 1962; shutdown September 1972; output 1.75 MW electric plus heating and desalination; "a multitude of problems, including a fire and coolant leakage"; radioactive soil around the tanks taken to Port Hueneme Naval Base, California, "incorporated into asphalt pavement" (no quantity); plant cut into pieces and shipped to the US for burial. Search snippets (UNVERIFIED): first criticality 4 March 1962 per one source; power available 72% of the time with more than 400 reactor malfunctions; 14,000 gallons of desalinated water a day. A 2024 Polar Record article by Nielsen ("Atomic energy for Antarctica: the rise and fall of Nukey Poo") exists (title seen in search results); it returned HTTP 403 and was not read. The McGee and Shibata white paper cites it for the 1962-72 period.
- The shutdown date and operating years are given as 1961-72 (Nielsen 2018), 1962-72 (McGee and Shibata 2026) and "1961 and 1979" (a Cambridge snippet, UNVERIFIED). The 1972 shutdown agrees across the three SOURCED items.

---

## Q7. Proliferation

- **SOURCED (abstract only), Ball, Peterson, Kemp and Ferry, "Assessing the Risk of Proliferation via Fissile Material Breeding in ARC-class Fusion Power Plants", arXiv:2404.12451 (submitted 18 April 2024, revised 5 June 2024, submitted to Nuclear Fusion):** the authors argue fusion plants with neutron source rates above 10^20 n/s could pose a "breakout" risk; with an OpenMC model of an ARC-class blanket they report that "a significant quantity of fissile material can be bred in less than six months" of full-power operation for initial fertile inventories of 5 to 50 metric tons of U-238 or Th-232; Li-6 enrichment substantially reduces the breeding rate, which they suggest as a proliferation-resistance measure. The abstract gives no plutonium or U-233 masses; the isotope produced is not stated there.
- **SOURCED (abstract only), Glaser and Goldston, "Proliferation Risks of Magnetic Fusion Energy: Clandestine Production, Covert Production and Breakout", Nucl. Fusion 52 (2012) 043004 (PPPL-4745):** three categories of risk: clandestine production in an undeclared facility, covert production in a declared facility, and breakout ("in which a state begins production of fissile material without concealing the effort"). Main finding: the risk "can be much lower than the equivalent risk from fission systems, if the fusion system is designed to accommodate appropriate safeguards."
- UNVERIFIED (press and search snippets about the same Glaser and Goldston work): a fusion system able to make weapons material within a couple of years could not be built clandestinely; a plant would draw at least some 40 MW, whereas first-generation centrifuge plants making material for one weapon a year need less than 0.5 MW; covert production in a declared plant would be easy for inspectors to detect; minimum breakout time to any weapon-usable material 1 to 2 months. A companion paper, PPPL-4794 (Goldston and Glaser, 2012), concludes safeguards are required (snippet).
- UNVERIFIED (search snippets): a 2026 RSIS commentary says the IAEA's first World Fusion Outlook (2023) summarized that a fusion system does not use or produce fissile materials and "is therefore not subject to IAEA safeguards"; an arXiv paper (2608.12963) on fusion-neutron production of alpha-emitting isotopes argues IAEA full-scope safeguards can apply to blankets intentionally breeding special nuclear material. Neither was read; the second arXiv number looks unusual and needs checking before any citation.
- **NOT FOUND:** a published IAEA safeguards proposal text for fusion plants; detailed fusion-fission hybrid design papers (LIFE or similar); plutonium or U-233 breeding rates in kg per year per GW from the Ball et al. full text. The IAEA waste review also notes the plant's beryllium and lead can be tritiated, and that "toxic materials, such as beryllium and lead" are present (SOURCED, Section 4); this is not a proliferation statement.

---

## FINAL

### What the sources support (SOURCED unless marked)
1. Published fusion plant designs span a wide range of net output: ARC 190 MWe from 525 MW fusion; EU-DEMO 350 MWe (2024 proposal, down from 500 MWe in the 2017 baseline) from 1,652 MW (down from 1,998 MW); STEP at least 100 MWe from 1.5-1.8 GW with Q_eng just above 1; JA-DEMO ~250 MWe from 1.4 GW; CFEDR baseline 1,510 MW; ARIES-ACT2 1,000 MWe from 2,640 MW. Net-to-fusion ratios from 0.06 to 0.36 (DERIVED). The trend in the one design with two vintages (EU-DEMO) is downward after adding physics margins.
2. No design I read gives a mature commercial-fleet plant; all are demonstration or pilot plants. Net electricity from any fusion plant has not been demonstrated (this brief's F1 covers status).
3. Thermal-to-electric efficiency in the designs: 0.316 to 0.44; ARC 0.40 (0.46 with hotter materials). Availability assumptions in the literature run 30% (early EU DEMO phase) to about 75-85% (mature-plant studies).
4. Components that face the 14 MeV neutron flux are expected to be replaced every 5 to 10 years (IAEA-led review) or, in DEMO planning, every 1.3 to 2 full-power years for the early blanket and divertor; the ARC vessel is designed to be swapped as a unit.
5. Fusion waste is much larger in volume than fission waste, "mostly" low and intermediate level, with "no-transuranic elements", with in-vessel components not clearable even after 100 years, and with tritium decay storage of up to 50 to about 100 years before disposal in some cases.
6. In the US the proposed rule treats fusion machines as byproduct-material (accelerator-like) facilities, not reactors; in the UK a 2023 Act removes fusion energy facilities from nuclear site licensing. No country has higher-level fusion-specific safety requirements per a late-2025 IAEA session abstract (UNVERIFIED snippet).
7. Antarctic Treaty Article V bans nuclear explosions and radioactive waste disposal; the Protocol's Annex III requires removal of radio-active materials; neither text mentions reactors. The 2026 white paper and the 1959 negotiating record both read Article V as not prohibiting peaceful non-explosive nuclear use; PM-3A operated 1962-72 and its cleanup shipped about 12,000 tonnes of contaminated rock out.
8. A fusion blanket could breed fissile material if fertile material (5-50 t) were deliberately added; with no fertile material added the risk is described as low and manageable with safeguards.

### What the sources do not support
- No source I read says fusion would be allowed or banned in Antarctica; the legal reading above is the sources' reading of Article V for fission reactors, applied here by me as DERIVED.
- No source states a fusion plant needs no emergency planning; the US proposed rule instead sets a 1 rem maximum-offsite-dose test for requiring an offsite plan.
- The discussion file's "roughly 400 MWe per plant (current commercial designs)" is not supported by any design read here: published pilot or demonstration net outputs are 100 to 500 MWe, except ARIES-ACT2's 1,000 MWe sizing. The discussion file's claim that fusion waste is "shorter-lived than fission waste" is supported with a caveat: the sources support "no transuranics and few long-lived isotopes" but also "much larger volume" and Nb-94 keeping steel non-clearable beyond 100 years.

### NOT FOUND (queries in the log)
- Fusion plant site footprint (hectares); fusion-specific cooling water volumes; any cold-climate or polar fusion siting or efficiency study; coastal-rock or ice-sheet criteria.
- Primary capital cost per kWe for any design; IEA, UK government or EPRI estimates.
- EU legal status of fusion (Euratom, safety directive); any ATCM paper or article on fusion (as opposed to fission) in Antarctica.
- Activated waste volume per plant-year or per GWh; decay heat figures.
- K-DEMO and CFEDR net electric figures from a read source; a published IAEA safeguards proposal for fusion plants; breeding rates (kg per GW-year) from Ball et al.
- Could not be read (blocked, died at the source): IAEA STEP papers (403), Takenaga JA-DEMO papers (403), NRC rulemaking-status page (403), IAEA PPCS paper (402), IAEA page node 187088 (402), Polar Record Nielsen 2024 (403), Nature K-DEMO paper (redirect to a sign-in page, not followed), EUROfusion Economic Viability PDF (TLS certificate error), PMC article (bot page), UKAEA waste slide deck from Wisconsin (file exceeded the 10 MB fetch limit).

---

## SEARCH LOG

Tool names: WS = WebSearch, WF = WebFetch. Result: hit, partial, miss. For misses, where it died is stated. "(local)" means WebFetch could not summarize the PDF, saved it, and I read its text with `pdftotext` in the scratch folder.

1. WS "EU-DEMO design parameters net electric power fusion power thermal power 2024 status" - partial (snippets; led to Coleman 2025).
2. WS "STEP Fusion UK Spherical Tokamak for Energy Production 100 MW net electricity West Burton 2040 status" - partial (program news, no design numbers).
3. WS "ARC fusion power plant design Sorbom 2015 200 MWe fusion power 525 MW capacity factor" - partial (capacity factor not in snippets).
4. WF arxiv.org/pdf/1409.3540 (ARC) - hit (local).
5. WF en.wikipedia.org/wiki/DEMOnstration_Power_Plant - hit (secondary).
6. WS "Coleman 2025 Nuclear Fusion EU-DEMO PROCESS design space net electric power 2017 baseline 2037 MW fusion power 1998 MW" - partial (identified paper).
7. WS "STEP spherical tokamak 1.8 GW fusion power 100 MW net electric prototype powerplant design parameters 2025 UKIFS" - partial.
8. WS "CFETR CFEDR China Fusion Engineering Demo Reactor parameters fusion power net electric 2035 design" - partial (led to IPP slides).
9. WF conferences.iaea.org/event/392/papers/35846/files/13486-Wilson_Manuscript_PWF.pdf - miss, HTTP 403 (died at the source).
10. WF doi.org/10.1088/1741-4326/ada6d9 - redirect to iopscience (followed in call 12).
11. WF ipp.mpg.de/5533652/RFPPC2025-05-19_I-05_Chengming_Qin.pdf - hit (local).
12. WF iopscience.iop.org/article/10.1088/1741-4326/ada6d9 - hit.
13. WF same URL, offset 100000 - hit (Table 6).
14. WF en.wikipedia.org/wiki/Spherical_Tokamak_for_Energy_Production - hit (secondary).
15. WS "STEP prototype powerplant "net electricity" MW fusion power spherical tokamak design IAEA FEC 2025 Wilson paper parameters major radius 3.6 m" - partial.
16. WF arxiv.org/html/2403.09460v1 - hit (first 100,000 characters).
17. WF conferences.iaea.org/event/392/contributions/35846/attachments/19824/36231/IAEA_FEC_25.pdf - miss, HTTP 403 (source).
18. WS "JA-DEMO design Japan fusion DEMO net electric output 200 MW 1.5 GW fusion power Tobita parameters" - partial (snippets of Takenaga and Utoh).
19. WS "K-DEMO Korea fusion demonstration reactor design parameters fusion power net electricity major radius 6.8 m" - partial (snippets only).
20. WS "ARIES-ACT2 power plant study fusion power net electric 1000 MWe availability cost of electricity" - partial.
21. WF conferences.iaea.org/event/392/contributions/35844/attachments/19822/36191/Takenaga.pdf - miss, HTTP 403 (source).
22. WF collaborators.euro-fusion.org/wp-content/uploads/2023/05/EconomicViabilityOfFusion.pdf - miss, TLS "unable to verify the first certificate" (source).
23. WF arxiv.org/html/2405.01514v2 - hit (availability figures; no LCOE).
24. WF conferences.iaea.org/.../Takenaga_PWF.pdf - miss, HTTP 403 (source).
25. WF snf.ieeecsc.org/files/ieeecsc/slides/utoh-presentation.pdf - hit (local).
26. WS "Bringing Fusion to the U.S. Grid National Academies 2021 fusion pilot plant cost of electricity capital cost target" - partial.
27. WF nationalacademies.org/read/25991/chapter/3 - partial (introduction only).
28. WS "levelized cost of electricity fusion power plant published estimate $/MWh overnight capital cost $/kWe techno-economic assessment Bustreo OR Lindley OR Schwartz" - partial (named authors not found).
29. WS "Fusion Industry Association 2025 global fusion industry report total investment billion public funding" - hit but out of scope for F3 (belongs to F1); no figures carried into this file.
30. WF emergentmind.com/papers/2606.26536 - hit (secondary summary).
31. WF pmc.ncbi.nlm.nih.gov/articles/PMC7658748 - miss (bot-verification page; died at the source).
32. WF arxiv.org/abs/2606.26536 - hit (abstract summary).
33. WS "EUROfusion DEMO cost of electricity estimate PPCS 2005 "cost of electricity" fusion Europe eurocents per kWh Model A to D" - partial (PPCS ranges in snippets).
34. WF www-pub.iaea.org/mtcd/publications/pdf/p1250-cd/papers/cd-i.pdf - miss, HTTP 402 (paywall).
35. WF arxiv.org/abs/2103.12451 - hit (abstract only).
36. WS "fusion power plant radioactive waste volume per year activated steel recycling clearance 100 years EU DEMO waste classification low level intermediate Gilbert" - partial (led to UKAEA-CCFE-PR2239).
37. WF scientific-publications.ukaea.uk/wp-content/uploads/UKAEA-CCFE-PR2239.PDF - hit (local; the IAEA-led waste review preprint, matching Nucl. Fusion 62 085001).
38. WF fti.neep.wisc.edu/.../aries/TALKS/lae_radwaste0308.pdf - miss, "maxContentLength size of 10485760 exceeded" (file too large for the tool).
39. WS "EU DEMO EUROFER first wall damage limit 20 dpa blanket segment replacement full power years divertor replacement interval 2 fpy" - partial (led to arXiv:1408.3546).
40. WS "fusion power plant loss of coolant accident decay heat passive safety no evacuation plan needed SEAFP safety fusion inherent" - partial (snippets only; "no evacuation plan" claim not found).
41. WF arxiv.org/pdf/1408.3546 - hit (local).
42. WS "fusion power plant cooling water consumption heat rejection cooling towers seawater siting requirements study footprint hectares" - partial (footprint and water volumes not found).
43. WS "NRC final rule fusion machines byproduct material framework 10 CFR Part 30 2025 2026 published Federal Register" - hit (proposed rule 26 Feb 2026).
44. WF govinfo.gov/content/pkg/FR-2026-02-26/html/2026-03865.htm - hit (first 100,000 of 168,363 characters).
45. WF arxiv.org/pdf/2606.01344 - hit (local).
46. WS "NRC fusion machines final rule approved Commission October 2026" - partial (no final rule found).
47. WS "UK fusion regulation Energy Act 2023 fusion energy facility not nuclear site licence Environment Agency HSE "fusion energy facilities" definition tritium" - partial.
48. WS "Japan fusion regulation 2025 radioisotope act not reactor regulation law fusion Cabinet Office safety framework; EU fusion regulatory approach Euratom 2025 commission fusion strategy" - partial for Japan, miss for EU (two topics in one query was a mistake; EU re-queried in call 71).
49. WF nrc.gov/materials/fusion/rulemaking-status.html - miss, HTTP 403 (source).
50. WF legislation.gov.uk/ukpga/2023/52/section/156 - hit.
51. WS "IAEA fusion regulation safety standards "fusion" IAEA Safety Standards applicability fusion facilities 2025 World Fusion Outlook regulatory" - partial.
52. WF ww2.nrc.gov/materials/fusion/rulemaking-status - miss, HTTP 403 (source).
53. WF iaea.org/node/187088 - miss, HTTP 402 (paywall).
54. WF ats.aq/e/antarctictreaty.html - partial (summary page; linked to full text).
55. WF ats.aq/e/protocol.html - partial (summary page; linked to full text).
56. WF documents.ats.aq/recatt/att005_e.pdf - hit (local; treaty text).
57. WF documents.ats.aq/recatt/Att006_e.pdf - hit (local; Protocol text).
58. WF ats.aq/documents/recatt/Att010_e.pdf - redirect to documents.ats.aq (followed).
59. WF documents.ats.aq/recatt/Att010_e.pdf - hit (local; Annex III).
60. WS "PM-3A nuclear power plant McMurdo Station 1962 criticality 1972 shutdown decommissioning contaminated soil removal 1979 Nukey Poo" - partial (the "1979" in my query was a guess and is not supported).
61. WS "nuclear power in Antarctica Madrid Protocol Antarctic Treaty Article V nuclear reactors legality scholarly article environmental impact assessment nuclear power station Antarctic" - hit (led to the Kobe white paper and FRUS).
62. WF cambridge.org/core/product/A35009D4403A289EF51E5F61EE54CFF4/core-reader (Nielsen 2024) - miss, HTTP 403 (source).
63. WF history.state.gov/historicaldocuments/frus1958-60v02/d324 - hit.
64. WF en.wikipedia.org/wiki/PM-3A - hit (secondary).
65. WF phys.org/news/2018-07-antarctica-nuclear-nukey-poo.pdf - hit (local; Nielsen 2018).
66. WS "fusion proliferation risk plutonium production fusion blanket breeding safeguards IAEA fusion hybrid 2023 2024 paper "fusion" "proliferation" 10 tonnes" - partial (the "10 tonnes" figure is not supported).
67. WS "Glaser Goldston 2012 "Proliferation risks of magnetic fusion energy: clandestine production, covert production and breakout" Nuclear Fusion" - hit.
68. WF arxiv.org/abs/2404.12451 - hit (abstract only).
69. WF bp-pub.pppl.gov/pub_report/2012/PPPL-4745-abs.html - hit (abstract).
70. WS "fusion power plant Arctic OR polar OR cold climate siting study cooling efficiency low ambient temperature Carnot heat sink fusion" - miss (no fusion study exists in results; died at the sources).
71. WS "European Commission fusion regulation Euratom treaty fusion facilities not covered nuclear safety directive EU fusion strategy 2026" - partial (policy background only).
72. WF nature.com/articles/s41598-022-12389-w - not followed: the server redirected to an authentication endpoint (idp.nature.com); logged as a block and not worked around.
73. WF epthinktank.eu/2026/05/18/nuclear-fusion-state-of-play/ - redirect to eprs.europarl.europa.eu (followed in call 74).
74. WF eprs.europarl.europa.eu/2026/05/18/nuclear-fusion-state-of-play/ - miss, HTTP 404 (source).
75. WF bp-pub.pppl.gov/pub_report/2014/PPPL-5007.pdf - hit (local).
76. WF research.kobe-u.ac.jp/gsics-pcrc/core-to-core/pdf/2026/antarctic_governance_whitepaper01.pdf - hit (local, non-layout extraction for column order).

Total: 76 web calls (WS 29, including call 29 which was out of scope; WF 47). No search tool refusal occurred. No files outside this one output file were written in the repo; downloads and extracted text are in the session scratch folder.

**Self-corrections.** (a) My first reading of the ARC cooling arithmetic printed kg/s where m3/s was meant; corrected to 10.2 and 20.3 m3/s (1 kg of water is about 1 liter). (b) The search summary for call 60 echoed my guess of a "1979 decommissioning"; no source supports it, and the Cambridge snippet's "1961 and 1979" is likely a heritage-site date range (UNVERIFIED). (c) The brief's "Article 1(c)" does not exist in the Treaty's Article I; noted in Q6 instead of inventing a quotation.
