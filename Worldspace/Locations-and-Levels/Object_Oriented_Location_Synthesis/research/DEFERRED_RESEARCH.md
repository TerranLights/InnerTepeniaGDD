# Deferred research: continue later

**Created 2026-10-11 at the developer's direction.** This is the running list of things researched, not found, and parked
**on purpose** to be continued in a later session. It is separate from `SHOPPING_LIST.md`. That file lists sources the
developer might obtain. This one lists searches **an agent should run again** and what to try. Each batch notes which
research file it came from. **Do not delete an item until it is resolved, and say where in the resolving file.**

**On resume:** work these only after the orchestrator review of the completed research files, unless a class needs one
sooner. Use the "search next" leads as written. A route that failed once may still work through a different mirror,
the author's page, an agency NTRS record, or arXiv. Log each route (`_BRIEF.md`).

**All five second-tranche agents have reported; Batches 1–5 are entered.** Later searches go in Batch 6 onward.

---

## Batch 1: from `gap_retry_leo_human_machines_power.md` (418 lines; ~45 searches; ~95 documents opened; ~14 dead routes)

### Routes that failed (the pages exist; the tool could not read them)

| Source | Failure | Try next |
|---|---|---|
| **SpaceX pages** and the **Falcon user's guide** | return a JavaScript shell or a 404 | the PDF user's guide from a mirror; an independent analyst such as a government or university study |
| **Springer ISS-RAD papers** (Life Sciences in Space Research, 2023, Parts 1–3) | paywalled; three routes tried (publisher, Europe PMC, PubMed); abstracts only | author preprint copies; the NASA SRAG WRMISS 2025 slides (read; few numbers) |
| **Cucinotta 2008** (BioOne) | Incapsula wall; NTRS 20080026203 has a different abstract and no PDF | author copies; NASA-hosted version |
| **ORNL Pu-238 page** | 403 | NASA RPS program documents; National Academies radioisotope reviews |
| **MDPI paper** (4058) | blocked | a repository copy |
| **ResearchGate** "Impact of Solar Activity Cycles on ISS Orbital Decay: A Two-Decade TLE-Based Analysis (2005-2025)" | not opened; the arXiv route failed | the arXiv listing again; Space-Track TLE history for catalog number 25544 |

### Facts still not found

| # | Item | Search next |
|--:|---|---|
| 1 | **ISS reboost propellant per year** from a NASA or ESA primary (only a 1995 plan of 8–11 t/yr for the Russian segment, and per-burn data) | NASA ISS Program Office "Trajectory Operations" papers; Progress M propellant manifest tables; *Orbital Debris Quarterly News* altitude histories |
| 2 | **ISS monthly altitude decay** from a NASA primary (tool summaries gave 100 m/day and 2–4 km/month; not used) | Space-Track TLE history; JSC or ESA conference papers on ISS drag |
| 3 | **ISS eclipses per year**; longest sunlit periods (only "no eclipse above about 70° beta, one week twice a year", and 30–35 min eclipse per 90–92 min orbit) | NTRS 20250002029 (found, not opened); JSC "ISS beta angle" thermal documents |
| 4 | **Current ISS altitude** (2026) | NASA mission pages |
| 5 | **TDRS Ku-band ISS round-trip latency** (SNUG and test data used instead) | NASA SCaN documents |
| 6 | **Dose at 600 km vs 400 km** | ESA SPENVIS / ECSS-E-ST-10-04C tables; NASA/TP-2009-215779; Wu et al. 2011 (NTRS 20110015964, abstract only); STS-31 and STS-61 dose reports; Badhwar 2002 |
| 7 | **Solar Cycle 25 effect on crew dose**, quantified | beyond the ISS-RAD slides: none found |
| 8 | **The "80 / 160 mSv" claim.** Not traced to a NASA document. NASA's own figures found: **40–90 mSv** and **72 mSv** per six months. | settle against NASA primaries before any class cites a crew dose |
| 9 | **ORDEM 3.0 numeric fluxes** by size and altitude (numbers live in software and figures) | NASA/TP-20220002309 (ORDEM 3.1 verification; found, not opened); ODQN issues; Hypervelocity Impact Symposium flux tables |
| 10 | **ISS shield ballistic-limit equations and critical diameters** (only a 1 cm statement) | Christiansen (NASA JSC), "Design and performance equations for advanced meteoroid and debris shields" (NTRS); ISS document SSP 30425 |
| 11 | **Atomic oxygen at 600 km**, its solar-cycle swing, ISS ram fluence per year | a NASA primary |
| 12 | **Orbital lifetime of very large structures** (ISS ballistic coefficient was not derived because drag area and drag coefficient were not sourced) | NASA debris-office lifetime tools |
| 13 | **Modern commercial-part TID values** (only 1996 JSC classes) | NASA Goddard RADHOME / NEPP compendia (NTRS 20220010348; found, not opened); NESC COTS assessment (Majewicz, Chen); ISO 21980:2020 |
| 14 | **Typical single-event rates** beyond the 1996 per-class numbers | as above |
| 15 | **ESTL actuator data** beyond the SOT paper and the Harmonic Drive paper | ESTL's own site; NTRS 19750006982 (sputtered MoS₂ bearing endurance; seen in a summary, not opened) |
| 16 | **NASA HRP evidence reports** (cardiovascular, vestibular, SANS, immune) as primaries. The two NTRS numbers given (20150006969, 20160001745) are a panel report and a process deck. | NTRS: the "Evidence Report: Risk of Cardiovascular Adaptations Contributing to Adverse Mission Performance", and the SANS and immune reports. The plasma-volume 10–15% figure is secondary. |
| 17 | **Launch cost per kg, 2024–2026** for Falcon Heavy, Starship, Neutron, New Glenn; any government analysis | not found; SpaceX pages unreadable |
| 18 | **ISS array wing dimensions** from NASA (Lockheed numbers seen only in a summary); a 2026 power-degradation figure (only 2003 P6 data) | NASA ISS pages |
| 19 | **Propulsion and nuclear:** X3 Hall thruster (NTRS 20190001137; PEPL X3 pages); NTRS 20190029289; NTRS 20040161476 (a bibliography; the 2004 papers behind it were not opened); NASA TA-3 space power roadmap radiator numbers; Pu-238 supply and production, 2024–2026 | NASA RPS program; National Academies reviews |
| 20 | **Mars round trip:** the "Folta 2012" item resolved to a two-page abstract plus a 2005 paper. A separate 2012 full paper was not found. Bailey et al. 2013 table columns could not be aligned by year in the extracted text. | the AIAA copy, doi `10.2514/6.2013-5507` |

### Found and not opened (listed for a follow-up)

arXiv 2609.24534 (FACSAT-2 re-entry, solar cycle 25) · Frontiers `fspas.2026.1797886` · the JAXA Kibo shield page
(`iss.jaxa.jp/iss/kibo/develop_status_09_e.html`) · NASA OIG IG-22-003 PDF · GAO-17-673.

---

## Batch 2: from `robot_body_in_space.md` (751 lines; ~80 search strings; 109 log rows; 17 dead or partly dead)

### Not opened at a primary source

| # | Item | Search next |
|--:|---|---|
| 1 | **Digit, Optimus and Figure power and heat figures.** Agility and Figure publish no specifications. Tesla's AI Day 2022 figures reached the agent only through press (2.3 kWh, ~100 W sitting, ~500 W brisk walking; Digit ~1 kWh; Digit 5 ~90 min run and 9 min recharge). Unverified. | Tesla AI Day 2022 transcript or video; Agility's 2025–2026 datasheet; an independent teardown with measured watts |
| 2 | **Valkyrie continuous power draw in watts** | Radford et al., J. Field Robotics 2015; IHMC Valkyrie papers (energy per step); NASA ER4 technical memoranda |
| 3 | **Robonaut 2 thermal-vacuum test data** (only qualitative statements; a summary quoted "-25 °C to 105 °C" for two joint actuators; unverified) | NTRS: Ambrose and Berka, "Thermal Management in Hyper-Redundant Space Manipulators" (SPIE 1993); R2 joint qualification reports |
| 4 | **Humanoid heat fraction** (share of electrical power that becomes heat; energy conservation was used instead) | a measured power-balance paper on Valkyrie, TALOS, Atlas or Digit |
| 5 | **Li-ion and solid-state cell behavior in vacuum** (swelling, venting, electrolyte loss; only qualification requirements found; NTRS 20060020764 was a stub) | NASA battery workshop papers on pouch cells in thermal vacuum |
| 6 | **Hardened-processor datasheets.** BAE RAD750 datasheet: HTTP 403 (curl and WebFetch). A summary quoted 200 krad (rad-tolerant), 1 Mrad (rad-hard), latch-up-immune SEU rate below 1.6e-10 errors/bit-day; unverified. | vendor datasheet through a mirror; NASA NEPP compendia |
| 7 | **NASA per-material outgassing values** (outgassing.nasa.gov is dynamic; NASA RP-1124 Rev 4 was an unreadable scan). No TML/CVCM for skin silicone, PVC, polyurethane foam or fabrics. | JAXA matdb.jaxa.jp data lists; a library scan of RP-1124 |
| 8 | **Textile and skin solar absorptance and emittance** (Kauder lists coatings and Beta cloth only) | ECSS or NASA tables for Nomex, Kevlar and silicone elastomers |
| 9 | **Mars surface solar irradiance and dust loss** (press: Opportunity fell from ~700 Wh/sol to 22 Wh/sol in the 2018 storm at optical depth 10.8; unverified). Overlaps Batch 3's Mars retry. | Lorenz et al.; JPL MER power reports |
| 10 | **Soft-skin permeation and blistering in vacuum** (a summary quoted PDMS O₂ permeability of 800 Barrer; unverified, not used) | Merkel et al., J. Polym. Sci. B 38:415–434 |
| 11 | **PFPE lubricant radiation threshold** (mechanism only) | ESTL or Krytox radiation-stability data |
| 12 | **Convective cooling in the Mars atmosphere** (6.36 mb CO₂) for a warm body | not searched |
| 13 | **Dextre service history and design life** (Wikipedia and news only: 15-year design life) | CSA / NASA primaries; tabulate |
| 14 | **Perseverance, ISS CMG and other long-duration machine reliability data** | not searched beyond the machines covered |
| 15 | **Cold-weld experiments beyond the NASA patent; ESA tribology handbook values** | ESA tribology handbook |
| 16 | **Lunar and Mars regolith wear rates on robot joints and seals** in controlled tests (S27 reviews seals; its test data not extracted) | Proctor and Dempsey, re-read for the test tables |
| 17 | **Antarctic humanoid or legged-robot trials** (press: a Chinese hexapod run at -40 °C with an insulated battery for two hours; an Arctic quadruped traverse; no paper opened) | trial papers; Arctic/Antarctic legged-robot field reports |

### Routes that failed

BAE RAD750 datasheet (403) · NASA outgassing database (dynamic) · NASA RP-1124 Rev 4 (unreadable scan) · Merstallinger et al.
(RADHARD 2024; 404) · DTIC radiation handbooks (maintenance page) · NTRS 20060020764 (a stub).

### Found and not read (or only skimmed)

NTRS 20200000214 (Opportunity End of Mission Report; abstract only, no PDF) · NTRS 20100009705 (JPL safe charge rates and
lithium plating; abstract only) · JPL FY21 R&TD poster R22020p · NASA Glenn "SiGe" low-temperature electronics pages · NASA
NEPP "Careful COTS" guidance · NASA TM-2009-215751 (read for qualification tables and vacuum text only) · Caltech SSPD-1 /
MAPLE papers · JAXA microwave transmission papers · Daryabeigi et al., NTRS 20060019134 (high-temperature MLI; downloaded,
not read) · NASA CR-1787 sections beyond those cited.

---

## Batch 3: from `moon_lagrange_and_comparables.md` (443 lines; ~64 searches; ~75 pages opened; 10 dead ends, 7 at the sources)

### Routes that failed

DTIC (403; reports AD0609888, AD0488532, AD0678427, ADA389253) · bas.ac.uk pages (Halley closure) · the ASCE Mir-repair paper ·
Carrer 2024 full text (abstract only) · the Lunar Sourcebook (not open online).

### Part 1 (physics): not found

| # | Item | Search next |
|--:|---|---|
| 1 | **Peak-illumination polar sites and "eternal light" figures** (not searched) | LRO LOLA/LROC illumination maps (Mazarico et al. 2011; Speyerer and Robinson 2013) |
| 2 | **Paige et al. 2010 (Diviner polar temperatures)** and **Williams et al. 2017** (only quoted through reviews) | the papers themselves |
| 3 | **Colaprete et al. 2010; Strycker et al. 2013; Spudis et al. 2010 and 2013; Mini-SAR; Lunar Prospector neutron and H data** (abstracts and reviews used) | full texts |
| 4 | **Apollo Lunar Sourcebook** (Heiken, Vaniman, French 1991): bulk soil oxide table (so oxygen wt% is quoted, not derived), respirable dust size, electrostatic charging, radiation chapter | a library copy; this is also a shopping-list candidate |
| 5 | **Dust toxicology primaries** (only the Gaier "under 5 microns" quote) | Wallace / Linnarsson / Park papers |
| 6 | **Lunar seismicity and meteoroid flux at the Moon** (not researched) | bears on lava-tube and surface design |
| 7 | **Lava tubes**: Sauro et al. 2020 (Earth-Science Reviews); Carrer et al. 2024; Chappaz et al. 2017 (GRAIL). Sizes beyond abstracts not found. | overlaps the Mars lava-tube retry |
| 8 | **Lunar mass driver**: no primary report of Mass Driver One or Two results; O'Neill's *The High Frontier* and SP-428; Kolm / Snow papers; SP-413 Appendices 5G, 5H and L | |
| 9 | **Economics**: Jones et al. (2018?), Charania and DePascuale, Bennett et al., Kornuta et al. 2019 (REACH); a dated 2024–2026 launch cost table | |
| 10 | **Lagrange points**: Earth-Moon L4/L5 as mission orbits (none flown); Kordylewski clouds; a primary on Earth-Moon L1/L2 halo thermal and radiation; Queqiao orbit parameters; ARTEMIS stationkeeping (Folta et al.); Gaia and JWST actuals; SOHO annual propellant; Sun-Earth L4/L5 (STEREO) environment; dose equivalent at L2 | |
| 11 | **Cislunar radiation** (Orion / Artemis I dosimetry) | NASA primaries |
| 12 | **Artemis II** (a flight on 1–11 April 2026 is reported in secondary pages; no NASA primary opened; no figures used); **Gateway status** (contested in 2025–2026 news; orbit physics stands regardless) | NASA primaries |
| 13 | **DRO station-keeping** (only "0 m/s" in Whitley and Martinez 2016, a qualitative table entry) | DRO long-term stability studies |

### Part 2 (mechanism comparables): not found

| # | Item | Search next |
|--:|---|---|
| 14 | **Antarctic**: COMNAP Antarctic Station Catalog (PDF not opened); Concordia / Dome C winter-over logistics (IPEV/PNRA/ESA); the NSF 2016 evacuation release; the Vostok 1982 fire in a primary; Stonehouse 1953 "Fire precautions at Antarctic Stations" (*Polar Record*); NSF/USAP incident statistics; McMurdo and Pole winter populations by year; per-person mass flows (the Panel's Figure 1 is a graph) | |
| 15 | **Submarines**: atmospheric-equipment redundancy (SUBSAFE is hull integrity); NRL submarine atmosphere papers; the NRC 1988 report cited by NRC 2007; oxygen consumption per person; emergency backup (oxygen candles, LiOH) in a primary; a primary for "food is the limit" | |
| 16 | **ISS**: ORU counts and failure rates from the NASA Logistics and Maintenance database; actual annual cargo up-mass. **The OIG crew-time shares (13% maintenance) conflict with delivered research hours**: that 13% is a planning share, not a measured fraction. | NASA ECTM validation (NTRS 20220013436, 20150009469); later OIG reports (2017–2018) |
| 17 | **Mir**: the claim that repair reached 50% of cosmonaut work | the blocked ASCE paper |
| 18 | **Biosphere 2**: Silverstone and Nelson 1996 full text | |
| 19 | **Analog habitats** (HI-SEAS, Mars-500, MDRS): no maintenance-time data searched | |

### Found and not read

NTRS 20220011365 · NTRS 20220019129 · NTRS 20230010822 and 20230010792 · ISSFD 2024 paper 20-13 · the Polito DRO thesis ·
NTRS 20210026714 (Deitrick, regolith size) · arXiv 2408.05823 (review of lunar construction) · arXiv 2602.03829 (open database
of regolith properties).

---

## Batch 4: from `life_support_lowg_power_structures.md` (591 lines; 45 searches; ~50 document groups opened; 2 searches wholly dead, 6 more dead on the figure sought; 6 page-level dead ends)

### Not opened

BVAD Revision 2 (only Rev 1 found) · the Lunar Sourcebook · MMPDS and CMH-17 · NCRP and ICRP fetal-dose figures (search-summary
numbers only; not used) · the ESA 3D-printing study PDF (the nebula.esa.int URL returned HTML) · the BIS paper "Docking with
Rotating Space Systems".

### Not found

| # | Item | Search next |
|--:|---|---|
| 1 | **BVAD Revision 2**, and **NASA-STD-3001 Vol. 1–2** (CO₂ and O₂ limits). Table 4-99 (growing area by diet) has misaligned columns; per-crop yields not used. | NTRS "Baseline Values and Assumptions Document Rev 2"; Wheeler / Hall / Ruminsky diet studies |
| 2 | **Closed-ecology full texts**: Lunar Palace 365 (peer-reviewed; only the bioRxiv preprint read); Salisbury, Gitelson and Lisovsky 1997 (*BioScience* 47(9):575); Gitelson, Lisovsky and MacElroy 2003; Lunar Palace 1 (105-day); MELiSSA whole-loop numbers; Severinghaus et al. 1994 (Biosphere 2) | |
| 3 | **Modern LED efficacy and crop yield per kWh** (BVAD's 1.6–10 g/kWh predates LEDs) | |
| 4 | **ISS ECLSS**: oxygen generation power and mass; a primary table of total ECLSS power and mass per crew member | |
| 5 | **Low-pressure (<57 kPa) human tolerance**, the original Norcross 2013 report; **fire in partial gravity** (only the 1 g Test 1 method paper read) | |
| 6 | **Fetal dose limits**: NCRP / ICRP figures (summaries quoted 5 mSv per pregnancy and 0.5 mSv per month; unverified); ICRP Publication 84 | |
| 7 | **Reproductive hazards in space**: Mishra and Luderer 2019 (*Nat Rev Endocrinol*); the 2020 Chinese mouse-embryo space experiment (Lei et al., *Natl Sci Rev*); Ronca and Alberts 2000 | |
| 8 | **NASA HRP evidence reports** (SANS, muscle, bone, cardiovascular); countermeasures (lower-body negative pressure, fluid loading) | overlaps Batch 1 item 16 |
| 9 | **Rotational gravity in humans since 1994?**; short-radius centrifuge studies in orbit; **partial-gravity primate or large-mammal data** (none found); plants at Mars gravity (abstract only); animal and plant fertility at partial gravity | |
| 10 | **Radiator areal mass** (kg/m²) and measured heat rejection per m² (summaries quoted 1.5–3.6 kg/m²; not used) | SAE and NASA primaries |
| 11 | **Kilopower** (KRUSTY) reports; orbital-habitat nuclear studies; Brayton vs Stirling at 100 kWe–MWe; reactor shielding for a habitat | |
| 12 | **Solar**: iROSA dimensions; decades-long array degradation at 1 AU; battery or regenerative fuel cell mass for eclipses. **SP-413's radiator area (4.9×10⁵ m²)** could not be reconciled with a blackbody calculation (K9). | |
| 13 | **Structures**: MMPDS / CMH-17 allowables (composites here are manufacturer typical values); NASA SP-8007 shell buckling; fatigue of pressure-cycled and spinning shells; TransHab burst factor and Kevlar / Vectran allowables; BEAM leak rate and pressure; Bigelow B330 numbers | |
| 14 | **MMOD**: ORDEM 3.0 numeric fluxes vs size at 400 km and beyond LEO; Grün 1985 flux; SSP-30425; Christiansen's Whipple rear-wall equations (OCR-damaged) | overlaps Batch 1 items 9–10 |
| 15 | **Docking to a rotating hub**: Hall's AIAA 99-4524; SP-413 appendices A, F, G, I, K, M; NASA SP-8024; any rotating-station momentum budget; artificial-gravity.com PDFs AIAA-2015-4613 and AIAA-2017-5140 | |
| 16 | **Regolith and ISRU**: the Lunar Sourcebook (density, composition, specific heat at high temperature; the sintering heat floor was not computed); Cesaretti 2014; strength of full-scale printed structures; thermal cycling of sintered regolith; peer-reviewed confirmation of the 2024 molten-regolith electrolysis run and the 311 kW figure; MMPACT reports; Mars regolith processing (perchlorate removal) and sulfur concrete | overlaps Batch 3 item 4 |

### Found and not read

Jensen arXiv:2408.00155 (abstract only) · NTRS 20170005618, 20160009739, 20200003267 (headers only) · NTRS 20240011694
(skimmed) · NASA TN D-5772 (header) · Frontiers in Physiology AGBRESA protocol (PMC9492851; abstract only).

---

## Batch 5: from `gap_retry_mars_venus_jupiter.md` (516 lines; 101 numbered log rows; 18 dead at the sources, 1 at the query)

### Routes that failed

Springer bot wall (Martinez 2017; the 2025 Space Science Reviews cave review) · Crossref (no abstract) · CDC / ATSDR (403 on both
hosts) · OU and UCL repositories (403) for Dartnell · eight routes for Seiff 1985 · NSSDC IDs for Venera 13 (guessed; errors) ·
JPL Magellan conjunction pages (403) · NTRS 20210007725, 20220000754 and 20210002012 (records with no file).

### Not closed

| # | Item | Search next |
|--:|---|---|
| 1 | **Measured Mars temperature by latitude and season** (Martinez 2017; Viking IRTM, Kieffer 1977; Pathfinder, REMS, TWINS, MEDA). Mars Climate Database v6.2 **model output** was substituted and is labeled as a model. | Europe PMC for open-access REMS and MEDA papers; the PDS atmospheres node for REMS reduced data |
| 2 | **Mars solar irradiance under dust beyond the Viking sites** (the tables are for VL1 and VL2 only) | |
| 3 | **Lava tubes**: measured roof thickness (none exists); Cushing 2012 and 2015; the 2025 cave review; Rostel et al. 2020 numbers | a third route for each |
| 4 | **Perchlorate**: the ATSDR toxicological profile; NRC 2005; inhalation toxicity of perchlorate dust (EPA: no value); lunar and Martian dust inhalation studies (not searched) | |
| 5 | **Dundas et al. 2018 full text** and the eight sites' latitudes; the SWIM maps (data products) | |
| 6 | **Dust storms**: SL19's table S1 (properties of each global storm); Montabone and Forget 2018; **a count after 2018** (no later event documented in anything opened; no claim made about 2019–2026) | |
| 7 | **Launch windows for crewed or cargo missions** (the BURKE dates are 2010 mission-design minima, not NASA announcements) | mission-specific plans |
| 8 | **MARIE dose equivalent in mSv/day** (Zeitlin; Cleghorn); Mars-orbit habitat dose at a specific shielding mass in g/cm²; Zeitlin 2013 and Hassler 2014 supplement | |
| 9 | **Partial gravity**: human bed-rest or centrifuge studies at 0.38 g (none found); bone results of the MARS mouse missions | |
| 10 | **Venus VIRA tables** (Seiff 1985): no web table found | NASA PDS archives for the Pioneer Venus probes; the NSSDC "Venus Atmosphere" listing; a library request for *Advances in Space Research* vol. 5 no. 11; Venus-GRAM outputs |
| 11 | **Venera 13 from a Soviet or NASA SP primary** (Ksanfomaliti et al. 1983) | |
| 12 | **Dartnell et al. 2015 full paper**; Nordheim et al. 2015 (ionization of Venus) | |
| 13 | **Birch 1991 (JBIS 44:157)**: obtained from no route (Fogg 1995 and Wikipedia are secondary) | |
| 14 | **Europa surface dose** in absorbed-dose units: Paranicas 2002 / 2007 / 2009; Nordheim 2016 / 2017 (*Nature Astronomy*); Europa Clipper radiation requirements | |
| 15 | **Callisto and Ganymede human-unit dose** (Cooper 2001 full text); **Juno measured radiation** (Becker et al.); **Galileo** (Fieseler 2002 full text) | |
| 16 | **Saturn versus Jupiter in common units** (numeric); Cassini MIMI datasets (PDS); Titan surface dose | |
| 17 | **Enceladus**: Hansen et al. 2020 full text. **Io**: Veeder et al. 2012 and 2004; Davies et al. final version | |

### Found and not read

Limaye et al. 2018 (*Space Sci. Rev.* 214) · arXiv:2603.22602 · arXiv:2605.09052 · Putzig et al. handbook chapter · Hansen et al.
UVIS plume paper (*Icarus* 2020).

---

## Status of the second tranche

All five agents have reported; Batches 1–5 are in. New searches belong in a Batch 6 and later.


---

## Batch 6: from `waste_heat_utilization.md` (441 lines; 52 searches; 11 dead ends)

**Routes that failed:** NSF 1992 power-upgrade page (404) · NREL and Antarctic Sun (host not resolved) · PNAS site (403; PMC copy used) ·
KIST (firewall) · maritime.edu (403) · ADS Ewert 1989 (405).

| # | Item | Search next |
|--:|---|---|
| 1 | **Absorption chillers and membrane distillation on low-grade (40–60 °C) heat.** No primary opened; the one absorption concept read regenerates at up to 120 °C. | ASHRAE or DOE/ORNL absorption chiller fact sheets; membrane-distillation reviews; Ewert 1989, *J. Spacecraft and Rockets* 26:303 (title seen in a snippet only) |
| 2 | **Kerrebrock's three-quarters rule** (derived, not sourced) | a space-power textbook (Angelo and Buden); Ewert 1989 |
| 3 | **Polar-station heat recovery and ship / submarine heat reuse**, from primaries | NSF Office of Polar Programs environmental assessments for South Pole; Naval Ships' Technical Manual chapters on distilling plants |
| 4 | **Fission surface power / Kilopower waste-heat reuse** for water or habitat heat | NASA FSP user interface requirements; Artemis base architecture papers; 1-ACT / NASA papers on Kilopower heat pipes and high-temperature water heat pipes |
| 5 | **Energy per kg for molten regolith electrolysis**; carbothermal in flight-like form | Sibille et al. 2024 TFAWS; NTRS 20110008524; NTRS 20205007780 |
| 6 | **Regolith ice-mining thermal energy** (NIAC Aqua Factorem; the search-summary numbers 800 kW and 2.4 kW are not used) | the opsjournal paper; NIAC pages |
| 7 | **Heat of reaction of ilmenite hydrogen reduction** (only 294,000 J/kg, from an unopened reference) | compute from formation enthalpies of FeTiO₃ and TiO₂ |
| 8 | **ASRG hot-end and cold-end temperatures** (only system efficiencies read) | |
| 9 | **ISS cabin-level heat flows** (kW for the cabin air condensing heat exchanger; total internal heat collected); **measured ISS radiator temperatures and rejection** (not design capacity) | NTRS 20130000766; ICES 2024 ISS ECLSS presentation |
| 10 | **Commercial humanoid thermal designs** (Digit, Optimus, Figure, Atlas electric) | patents; IEEE thermal papers on humanoid actuator cooling; the KIST cold-plate paper (firewalled) |
| 11 | **Orbital-habitat reactor waste heat** (no orbital study found; the sibling file also found none) | |
| 12 | **Mars heat-pump studies; 2020s Artemis heat-pump hardware** (only 1990s–2010s items) | |

**Found and not read:** IAPWS-95 · Mainstream Engineering heat pump SBIR news · NTRS 20110008524 and 20130012503 · TFAWS 2024 ID-04 ·
NTRS 20210026557 · Meier APM details · EPFL graph pages on thermochemical cycles · JAXA repository thermal control hits.

---

## Proposed research topics

| # | Topic | Raised | Notes |
|--:|---|---|---|
| P1 | **DONE 2026-10-11** (`research/waste_heat_utilization.md`; open threads in Batch 6). **Waste-heat utilization in a vacuum habitat.** Can a station use the heat it must reject to drive other processes (heat pumps to raise radiator temperature, thermoelectric and organic Rankine conversion, endothermic chemistry, distillation and drying, thermochemical processes)? What the second law and real systems allow at low temperatures. | developer, 2026-10-11 | The developer asked Grok about this "several months ago" and believes the answer was pasted into a file. **Searched on 2026-10-11 and not found:** the only Grok conversation on orbital infrastructure (`to-be-integrated/Conversation with Grok - theoretical logistics for orbital infrastructure.rtf`; an identical copy is in CurrentNovelDocs) is the mass-budget discussion and has no heat content. Treat any Grok answer as an unverified lead; re-source from primary literature. Ask the developer to point to the file or re-paste it. |
| P2 | **Heat batteries (thermal energy storage) for stations in orbit** around the Sun, Moon, Mars, Jupiter and Saturn: eclipse and shade statistics per body, storage figures for the Jovian and Saturnian cases, comparison with oversizing batteries or radiators; the heliocentric case (no planetary eclipse). | developer, 2026-10-11 | Synthesis in `waste_heat_utilization.md` §10.2. The file's storage cases are lunar night and ISS-class eclipse only. |
| P3 | **Thermal environment and heat use at Earth-Moon and Sun-Earth L4/L5 ("grav-locked" stations):** eclipse and Sun-angle statistics from orbital mechanics (calculate, arithmetic shown); radiator and heat-pump sizing for a stated power; which heat uses apply when there is little or no eclipse; what JWST at L2 shows. | developer, 2026-10-11; **for 2026-10-12** | §10.3 of the waste-heat file frames the questions. Results become parameters of an "Orbital habitat at a Lagrange point" class (not yet written). |
