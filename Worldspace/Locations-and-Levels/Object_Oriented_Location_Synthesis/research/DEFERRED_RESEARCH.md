# Deferred research: continue later

**Created 2026-10-11 at the developer's direction.** This is the running list of things researched, not found, and parked
**on purpose** to be continued in a later session. It is separate from `SHOPPING_LIST.md`. That file lists sources the
developer might obtain. This one lists searches **an agent should run again** and what to try. Each batch notes which
research file it came from. **Do not delete an item until it is resolved, and say where in the resolving file.**

**On resume:** work these only after the orchestrator review of the completed research files, unless a class needs one
sooner. Use the "search next" leads as written. A route that failed once may still work through a different mirror,
the author's page, an agency NTRS record, or arXiv. Log each route (`_BRIEF.md`).

**Still to add when each agent finishes:** the open threads of `gap_retry_mars_venus_jupiter.md` and
`life_support_lowg_power_structures.md`. (Batches 1–3 are in.)

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

## Batch 4 onward

*(appended as each remaining agent reports: `gap_retry_mars_venus_jupiter.md`, `life_support_lowg_power_structures.md`)*
