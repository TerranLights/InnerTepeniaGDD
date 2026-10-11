# Robot body in space and other extreme environments: research file

Created 2026-10-10. Real physics and engineering data only. No figure is from memory; every number below comes from a
page opened in this session (see SEARCH LOG).

## 1. Scope

The physical body of a human-shaped, human-sized machine (skin, clothing, gloves, gel brain waved per H-1 and not
covered here) in vacuum, in thermal extremes, under radiation, in dust, on low-gravity surfaces and over years of
service. Covers thermal, radiation, vacuum materials, power, mechanics, cold, and reliability. Does not consider
flight or any bending of physics.

## 2. SEARCH LOG

(Appended as the work proceeds. Date of all entries: 2026-10-10 unless noted.)

Method note: WebSearch returns summaries only. To get numbers I downloaded the PDF or page itself with curl, converted it
to text with pdftotext, and read the passage. A number taken only from a search summary is marked "search summary only"
and is never given high confidence. Marks: useful / thin / dead (died at query = the query could not find it; died at
sources = it was found but no primary source opened or the source was blocked).

| # | Search string or page (verbatim) | Result | Mark |
|--:|---|---|---|
| 1 | `Robonaut 2 thermal vacuum test thermal control design heat rejection NTRS` | Returned Shuttle and ISS radiator reports, no R2 thermal report | dead (query; R2 thermal vacuum report not indexed under these words) |
| 2 | `NASA Valkyrie humanoid robot power consumption watts actuators thermal` | Led to NTRS 20140011889 and arXiv 1902.00187; no continuous-watt figure in any hit | useful (leads) |
| 3 | Page: nasa.gov r5-fact-sheet.pdf | Image-only photo PDF, no specs | dead (source) |
| 4 | Page: NTRS 20140011889 (Radford, "Valkyrie, NASA's new humanoid", 25 Feb 2014 slides) | 125 kg, 44 DOF, 2 kWh battery, 44 motor controllers | useful |
| 5 | Page: arXiv 1902.00187 (Jorgensen et al., IEEE RA-L 2019) | Valkyrie actuator thermal limits and heating times | useful |
| 6 | `Robonaut 2 "thermal" design ISS external environment heater multilayer insulation actuators power dissipation` | General ISS payload thermal pages; no R2 figures | thin |
| 7 | `Robonaut 2 Systems Design thermal ISS "Robonaut 2" torso thermal radiator power 150 W` | Led to NTRS 20100040493, 20110016467 (wrong doc: Tech Briefs) | thin |
| 8 | `Robonaut 2 design hardware overview NTRS 2011 actuators torque power consumption lessons learned` | Led to NTRS 20100040493, 20140000957, 20120014462 | useful (leads) |
| 9 | Page: NTRS 20140000957 (Ahlstrom et al., R2 on ISS status update and IVA mobility, AIAA) | EVA thermal plan: heat sinking, heaters, fans, beta angle | useful |
| 10 | Page: NTRS 20100040493 (Diftler et al., "Robonaut 2, the first humanoid robot in space") | Draft text with gaps ("need reference"); no thermal or watt figures | thin |
| 11 | `Digit humanoid robot specifications battery capacity runtime power Agility Robotics` | Secondary spec aggregators only (qviro, newequipment) | thin (secondary) |
| 12 | `Tesla Optimus AI Day 2022 power consumption walking watts sitting 2.3 kWh battery` | Press coverage quoting 2.3 kWh, 100 W sitting, 500 W brisk walking | thin (secondary; no Tesla primary opened) |
| 13 | `humanoid robot walking power consumption measured watts cost of transport study Atlas Digit Valkyrie energy` | Cost-of-transport press and a Robotica paper (not opened) | thin |
| 14 | Pages: agilityrobotics.com/solution, tesla.com/AIday, figure.ai | Marketing pages, no specs / redirect stub | dead (source) |
| 15 | Page: bostondynamics.com/products/atlas/ and atlas-spec-sheet.pdf (Jan 2026) | 90 kg, 56 DOF, 4 hr, IP67, -20 to 40 C operating | useful |
| 16 | `Tesla AI Day 2022 transcript Optimus "100 watts" "500 watts" walking brisk battery pack 2.3 kilowatt hours` | Same press, no transcript | thin |
| 17 | `Boston Dynamics electric Atlas specification sheet battery capacity kWh operating temperature` | Confirms battery Wh not published | useful (negative) |
| 18 | `Agility Robotics Digit specifications datasheet operating temperature battery 1.5 kWh payload IP rating` | Secondary only; Agility publishes no temp range or IP in hits | thin |
| 19 | `BAE Systems RAD750 radiation-hardened processor datasheet total ionizing dose krad single event upset` | BAE datasheet URL found; curl and WebFetch both got 403 | thin (datasheet blocked; values from search summary only) |
| 20 | `NASA NEPP commercial off-the-shelf electronics total ionizing dose tolerance krad(Si) typical range radiation hardness assurance guideline` | Led to Sinclair and Dyer SSC13-IV-3 | useful (leads) |
| 21 | Page: Sinclair and Dyer, "Radiation Effects and COTS Parts in SmallSats", SSC13-IV-3, AIAA/USU 2013 | TID classes of COTS, shielding sectoring, tungsten, SEU example | useful |
| 22 | `lithium-ion battery cell radiation tolerance gamma total dose capacity degradation krad study` | Led to Gao et al., The Innovation 2023 (Li metal cells) | useful |
| 23 | Page: Gao et al., "Radiation effects on lithium metal batteries", The Innovation, doi 10.1016/j.xinn.2023.100468 | 20 kGy Co-60: capacity retention after 350 cycles | useful |
| 24 | Page: NASA, "Active Thermal Control System (ATCS) Overview", nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf | ISS radiator capacity, area, mass, ammonia freeze point | useful |
| 25 | Page: Carrillo, Farner and Preston, "ISS Payload Thermal Environments", NASA TFAWS 2015 short course | Passive flux-cube temperatures on ISS vs absorptance/emittance ratio; EVA touch limit | useful |
| 26 | `NASA/TP-2005-212792 Spacecraft Thermal Control Coatings References solar absorptance emittance table` | Led to Kauder (NASA GSFC, Dec 2005) | useful |
| 27 | Page: Kauder, NASA/TP-2005-212792 (NTRS 20070014757) | Absorptance and emittance of coatings. The PDF text layer is a character-shifted font (every code is 29 below the real one); I decoded it with a script and read the tables | useful (decoded text; values read from decoded tables) |
| 28 | `NIST CODATA Stefan-Boltzmann constant value physics.nist.gov constants`; pages physics.nist.gov/cuu/pdf/wallet_2022.pdf and physics.nist.gov/cgi-bin/cuu/Value?sigma | The wallet PDF fetch failed (server returned an HTTP/SSL error page); the Value?sigma page opened | useful (wallet PDF dead at source) |
| 29 | `total solar irradiance 1361 W/m2 NASA SORCE TIM solar constant 1 AU`; pages arXiv 1605.09788 (IAU 2015 Resolution B3), NASA GSFC TSI science page | Nominal TSI 1361 W/m2 | useful |
| 30 | `Valkyrie humanoid robot R5 average power draw standing walking watts battery life measured IHMC` (extended) | No measured watts for Valkyrie in any hit; only battery capacity (1.8 kWh in a secondary) | dead (sources; no continuous-watt figure published in what I could reach) |
| 31 | `Atlas ATLAS humanoid hydraulic power consumption watts standing walking pump energy Boston Dynamics paper` | One secondary quote (about 15 kW for the hydraulic Atlas); no primary | thin (secondary only; not used as a bound) |
| 32 | `Robonaut 2 fact sheet weight 300 pounds power 120 VDC watts nasa.gov facts` | Mass and DOF only | thin |
| 33 | `Radford "Valkyrie: NASA's First Bipedal Humanoid Robot" Journal of Field Robotics 2015 battery thermal liquid cooling` | Paper itself not returned | dead (query or paywall) |
| 34 | `humanoid robot actuator torque density Nm/kg efficiency harmonic drive quasi-direct drive comparison review paper` | Vendor and blog numbers (25 to 39 Nm/kg harmonic, 7 to 28 Nm/kg QDD) | thin (secondary; not used) |
| 35 | Pages: NTRS 20100039862, 20110023122, 20100033240, 20110024047 (Robonaut 2 and Robonaut papers) | 20100033240 states arms use "thermal vacuum rated motors, harmonic drives"; no numeric thermal data in the others | thin |
| 36 | `Robonaut thermal vacuum chamber test arm joint actuator results cold hot temperatures EVA humanoid manipulator` (extended) | A summary claimed R2 arm actuators ran from -25 to 105 C in the JSC chamber; no primary page found | thin (unverified; not used) |
| 37 | `Robonaut 2 batpack EVA thermal design analysis battery torso heat sinking radiate NTRS` (extended) | Confirmed NTRS 20140000957 Batpack text | useful |
| 38 | `Robonaut arm joint actuators tested thermal vacuum chamber "-25" "105" harmonic drive lubricants Johnson Space Center` | No primary for the -25 to 105 C claim | dead (sources) |
| 39 | `harmonic drive gear vacuum lubricant lifetime cold temperature -40 C efficiency torque loss space mechanism study` | Led to ESMATS 2015 Roberts et al. | useful |
| 40 | Page: Roberts, Bridgeman, Jansson, Schulke and Tvaruzka, "The Performance and Life of Fluid-Lubricated Harmonic Drive Gears", ESMATS 2015 (ESTL, Harmonic Drive AG, ESA) | Vacuum life test at +90 C and cold-soak efficiency at -25 C | useful |
| 41 | Page: NASA MSC-TOPS-101 flyer (R2 arm technology) | Confirms brushless motors, harmonic drives, series elastic actuators; no numbers | thin |
| 42 | `NASA outgassing database ASTM E595 TML 1.0 percent CVCM 0.10 percent criteria silicone elastomer values` | Led to GSFC outgassing user guide and a NuSil/Avantor white paper | useful |
| 43 | `NASA RP-1124 Outgassing Data for Selecting Spacecraft Materials TML CVCM WVR table elastomers` | Led to NTRS 19970027853 | useful (leads) |
| 44 | Page: GSFC outgassing database user guide (etd.gsfc.nasa.gov, page carries a funding-lapse notice, content intact) | Test conditions and acceptance limits | useful |
| 45 | Page: NASA RP-1124 Rev 4 (NTRS 19970027853) | Scanned OCR is unreadable garbage | dead (source) |
| 46 | Pages: DTIC ADA303760; JAXA matdb Outgasdoc1 and Outgasdoc2; Wolfram data repository | DTIC returned a maintenance page; JAXA pages describe the method only; Wolfram lists 12859 rows but no per-material values opened | thin / dead (sources) |
| 47 | `Sylgard 184 outgassing NASA TML CVCM WVR values ASTM E595 cured 0.4` and `NASA outgassing data PVC polyurethane foam neoprene TML CVCM fails ASTM E595 materials not recommended for spacecraft use` | No per-material NASA values returned | dead (query; the NASA per-material database is a dynamic site I could not query) |
| 48 | Page: Avantor/NuSil white paper, "Evaluating low and ultra-low outgassing silicones for space applications" | 13 silicones with measured ASTM E595 TML/CVCM | useful (vendor, secondary) |
| 49 | `lunar dust abrasion seals joints Apollo lessons learned Gaier NASA TM-2005-213610 electrostatic adhesion` | Led to Gaier 2005 and Proctor and Dempsey | useful |
| 50 | Page: Gaier, NASA/TM-2005-213610 "The Effects of Lunar Dust on EVA Systems During the Apollo Missions" | Apollo abrasion, seal and radiator dust effects | useful |
| 51 | Page: Proctor and Dempsey, "Survey of Dust Issues for Lunar Seals and the RESOLVE Project" (NTRS 20080003835) | Downloaded; read below only if cited | see rows later |
| 52 | `lunar night survival temperature -170 C radioisotope heater unit Chang'e Yutu rover thermal design survive lunar night paper` | News and ESA pages; no engineering paper | thin |
| 53 | `Mars Exploration Rover thermal design warm electronics box RHU heaters operating temperature -40 C Spirit Opportunity winter survival` | Led to SAE papers (paywalled) and TFAWS05 Tsuyuki (EDL only) | thin |
| 54 | `lithium-ion battery low temperature performance NASA capacity at -20 C -40 C percent of room temperature discharge study` | Led to JPL poster R20129p and NTRS 20000056605 | useful |
| 55 | Pages: JPL R&TD poster R20129p (Smart et al., FY21); NTRS 20000056605 (Huang et al., JPL, Li-ion low-temperature cells) | Cell specific energy at -40 C; cathode capacity vs temperature | useful |
| 56 | `lithium plating charging lithium-ion below 0 C risk NASA Aerospace Battery Workshop charge temperature limit` | Led to NTRS 20100009705 (abstract page only; PDF not downloadable) | thin (abstract only) |
| 57 | `solid-state battery low temperature performance -40 C sulfide oxide polymer electrolyte ionic conductivity review capacity retention` (extended) | Review summaries: polymer cells need 60 to 80 C; no cold-temperature cell data from a primary | thin (not used) |
| 58 | `lithium-ion cell operation in vacuum pouch cylindrical electrolyte evaporation vent thermal runaway heat dissipation vacuum NASA test` | Thermal-runaway and venting summaries; no direct data on cell operation in vacuum | thin |
| 59 | `NASA State-of-the-Art of Small Spacecraft Technology Power chapter lithium-ion specific energy Wh/kg battery table solid-state`; page nasa.gov/wp-content/uploads/2023/05/3.-soa-power-2022.pdf | Cell specific energies, solid-state claims, low-temperature cells | useful |
| 60 | `NASA Mars fact sheet solar irradiance 590 W/m2 ...`; pages nssdc.gsfc.nasa.gov marsfact.html and moonfact.html | Mars 586.2 W/m2, gravity, temperatures; Moon equatorial 95 to 390 K | useful |
| 61 | `Mars surface solar panel power dust storm optical depth Opportunity ...` | News figures (700 to 22 Wh/sol, tau 10.8); NTRS 20190028687 not opened | thin (secondary) |
| 62 | `NASA Human Integration Design Handbook ... glove strength reduction` and `Extravehicular Mobility Unit EMU mass ... glove grip strength loss` | Led to Mesloh et al. NTRS 20100008464 and the EMU data book | useful |
| 63 | Page: Mesloh, England, Benson, Thompson and Rajulu, "The Effects of Extravehicular Activity (EVA) Glove Pressure on Hand Strength" (NTRS 20100008464) | Grip and pinch strength with Phase VI glove at 4.3 psi | useful |
| 64 | Page: NASA HIDH (NASA/SP-2010-3407 Rev 1), grep for EMU mass and glove numbers | 52908 lines of text; only qualitative glove statements found | thin |
| 65 | `Kram Domingo Ferris 1997 ... Froude number lunar Mars gravity` and `Carr Newman "The Apollo Number" ...` | Led to Carr and McGee 2009 PLoS ONE; Kram paper PDF not opened (Neptune 2005 paper opened instead, wrong paper) | useful / thin |
| 66 | Page: Carr and McGee, "The Apollo Number", PLoS ONE 4(8):e6614 (via Europe PMC XML; the PMC page is behind a reCAPTCHA) | Suited lunar walk-run Froude values | useful |
| 67 | Page: NASA EMU LSS/SSA Data Book Rev V (JSC-E-DAA-TN55224, Sept 2017) | Suit component masses, design metabolic loads, water sublimator | useful |
| 68 | `Canadarm2 Dextre lifetime anomalies replaced joint failure ...` and `NASA spacewalk Canadarm2 wrist roll joint replacement June 30 2026 ...` | News coverage (space.com, local TV) of the 2026 wrist-roll replacement and the 2002 one; no CSA/MDA statistics | thin (secondary) |
| 69 | `Curiosity wheel damage aluminum skin holes distance driven design life ...` | Summary quotes (0.75 mm skin; 3 broken grousers = 60% of life); JPL PDF not opened | thin |
| 70 | `NASA Opportunity rover mission complete 2019 ...`; pages science.nasa.gov MER mission, JPL "Six Things to Know About Opportunity", NTRS 20200000214 (abstract only; PDF has no download link) | 90 sols design, sol 5111 last contact, 45.16 km | useful (JPL page) |
| 71 | `Spirit rover wheel stuck ...`; pages JPL "NASA Concludes Attempts to Contact Mars Rover Spirit" (24 May 2011) and Spaceflight Now (24 May 2011) | Spirit's cold-survival failure and wheel failures | useful (JPL) / secondary (Spaceflight Now) |
| 72 | `multilayer insulation effective emittance 0.01 to 0.03 ...` and `Gilmore Spacecraft Thermal Control Handbook ...` | Vendor and student pages; NTRS downloads 404 for 20190025589, 20210008442, 20210004177 | dead (sources for those three) |
| 73 | `TFAWS multilayer insulation short course effective emittance ...` (extended); pages Johnson (NASA GRC) TFAWS "Multilayer Insulation for In-Space Cryogenic Applications" (NTRS 20240010471), TFAWS 2017 PT-07 | MLI heat flux 0.2 to 0.4 W/m2 at 293 K to 78 K, 30 layers, 2e-6 Torr; MLI equations valid only below 1e-4 Torr | useful |
| 74 | `radiation damage threshold polymers Gy dose Kapton PTFE silicone elastomer polyurethane mechanical properties degrade Mrad NASA materials radiation handbook` | Led to NASA CR-1787 (1971) and DTIC handbooks (DTIC returned maintenance pages) | useful (NASA CR-1787) / dead (DTIC, sources) |
| 75 | Page: Hunks and Hunzmun, NASA CR-1787, "Radiation Effects Design Handbook, Section 3: Electrical Insulating Materials and Capacitors", July 1971 (NTRS 19710020300). Scan OCR with spaced letters; numbers read by eye | Damage thresholds of PTFE, silicone rubber, polyurethane | useful (old; units "rads(C)" = carbon-equivalent absorbed dose) |
| 76 | `Juno radiation vault titanium 1 cm thickness dose reduction ...` | News and Scientific American blog only (1 cm Ti vault, factor of 800, 200 kg) | thin (secondary; kept as a lead, not tabled) |
| 77 | `Van Allen belts crossing dose per pass electronics shielding MEO orbit dose rate krad per year aluminum shielding thickness 100 mil` | Led to Carstens and Campola, NASA GSFC, 2022 | useful |
| 78 | Page: Carstens and Campola, "Total Dose Modeling of the Transit Through the Van Allen Belts", NASA GSFC Code 561, LSIC presentation 25 May 2022 (NTRS 20220007131) | TID vs aluminum shield thickness: direct Moon transfer, GTO per revolution, 2 to 10 month spiral | useful (AP-9/AE-9, solid aluminum sphere, silicon target; solar protons not included) |
| 79 | `Jones Jansen "Space Tribology" NASA/TM-2000-209924 ...` and page NTRS 20000057374 | PFPE failure mechanism, MoS2 in humid air, lubricant test results | useful |
| 80 | `cold welding vacuum clean metal surfaces ESA tribology handbook adhesion ...` and page NASA patent US 4,245,768 (NTRS 19810010928) | NASA statement on oxide monolayers, recontamination time vs pressure | useful (patent text; background section) / thin (no ESA handbook opened) |
| 81 | `Kurs Science 2007 Wireless power transfer via strongly coupled magnetic resonances ...`; abstract read through the Europe PMC API (the Science and PubMed pages are behind a CAPTCHA) | 60 W at about 40% over more than 2 m, up to 8 coil radii | useful |
| 82 | `microwave power beaming demonstration distance received power efficiency JAXA 1.8 kW 55 m Caltech MAPLE orbit results` and `Caltech MAPLE in-orbit ...`; page ard.jaxa.jp SSPS ground demonstration | JAXA page has no numbers; Caltech coverage says only that the signal was detected; JAXA 1.8 kW at 55 m is from a news summary | thin (JAXA 1.8 kW/55 m kept as an unverified lead) |
| 83 | `microwave power transmission beam collection efficiency Goubau tau parameter ...` and page Dickinson, JPL, NASA CR-157843, "Microwave Power Transmitting Phased Array Antenna Research Project Summary Report", 1978 (NTRS 19790005092) | Beam efficiency is a function of tau; SPS design tau 1.734; the efficiency curve (Fig. A-5) is a graph, not text | useful (definition and design point); curve values not extractable |
| 84 | `electronics operating at cryogenic temperatures lunar night -180 C extreme environment electronics NASA Glenn ...` and page Patterson, Hammoud and Elbuluk, "Assessment of electronics for cryogenic space exploration missions", Cryogenics 46 (2006) 231-236 | The PDF's minus signs are missing in the text layer, so temperatures cannot be read from it; only qualitative statements used | thin / useful (qualitative) |
| 85 | `legged robot cold weather test Spot Antarctica Arctic -30 C -40 C battery performance actuators problems field trial paper` | Press on Chinese hexapod at Zhongshan (-40 C, insulated battery two hours) and DEEP Robotics tests | thin (secondary; leads) |
| 86 | `Antarctic robot trials rover Cool Robot Nomad Zhongshan battery cold ...` and page Ray, Price, Streeter, Denton and Lever, "The Design of a Mobile Robot for Instrument Network Deployment in Antarctica", ICRA 2005 (Dartmouth Cool Robot) | Antarctic insolation, a 90 kg rover's design temperatures and motor power | useful |
| 87 | `Wensing Wang Seok Otten Lang Kim Proprioceptive Actuator Design in the MIT Cheetah ...` and page IEEE T-RO 33(3):509-522, 2017 (author's proof from MIT) | Motor torque density (27 vs 9 N m/kg) | useful |
| 88 | `Digit Cassie bipedal robot cost of transport measured ...` and page arXiv 2408.15632 (Wow Orin) | Simulated cost of transport for Cassie 0.762 and Unitree H1 0.718; preprint | thin (preprint; simulation) |
| 89 | Page: nasa.gov/technology/r5/ (NASA Valkyrie R5 page) | 300 lb, 6 ft 2 in, 1.8 kWh, about one hour, 44 DOF | useful |
| 90 | `clothing insulation clo definition 0.155 m2 K/W ISO 9920 ...` and page efunda.com clo | Summary only; no primary page opened | dead (sources; clo not used) |
| 91 | `silicone rubber thermal conductivity W/mK Sylgard 184 datasheet 0.27 ...` and page Dow Corning Sylgard 184 data sheet | Data sheet says 0.2 W/m K and a -45 to 200 C service range; the search summary said 0.27 | useful (data sheet) |
| 92 | `flexible thermal management method for high-power chips in humanoid robots` (ScienceDirect S2666998624004988) | WebFetch returned HTTP 403 | dead (sources) |
| 93 | `NASA High Performance Spaceflight Computing HPSC radiation tolerance ...` and page Powell, "High Performance Spaceflight Computing (HPSC) for Lunar and Planetary Missions", LPSC, 12 Mar 2025 (NTRS 20250002070) | 200 kRad TID requirement, RHBD for single events | useful |
| 94 | `Ingenuity helicopter Snapdragon 801 commercial processor radiation ...` | Vendor and press stories; no JPL paper found | dead (query; no primary reached) |
| 95 | Page: Ginosar, "Survey of Processors for Space", DASIA 2012 | RAD750: 250 nm, 133 to 166 MHz, about 300 MIPS, unit price above US$200,000 | useful (secondary survey by a space-processor vendor) |
| 96 | `all-solid-state lithium batteries low-temperature operation review ...` (extended); page Hong et al., Nature Communications 2025, "All-solid-state batteries designed for operation under extreme cold conditions" (open access, via Europe PMC API) | Panasonic 18650 retention at -20 and -40 C; solid-state coin cell at -60 C | useful |
| 97 | `lithium-ion battery cells vacuum environment testing thermal vacuum pouch cell ...` (extended); pages NASA/TM-2009-215751 (NESC Li-ion guidelines), JSC 20793 Rev C (Jan 2014), NTRS 20060020764 (a 3-line stub) | Vacuum and thermal-vacuum qualification requirements; charge and discharge limits for Mars; no data on cell physics in vacuum | useful (requirements) / thin (no cell-in-vacuum data) |
| 98 | Page: Kirchner-Burles et al., "Safety and performance implications of lithium plating induced by sub-zero temperature cycling of lithium-ion batteries", J. Power Sources 660 (2025) 238565 | Reversible plating at -10 C, irreversible at -20 C | useful |
| 99 | `NASA spacewalk Canadarm2 wrist roll joint ...` (extended); pages nasa.gov/blogs/spacestation 29 and 30 June 2026 | Canadarm2 installed 26 Apr 2001, wrist joint replaced 30 Jun 2026 | useful |
| 100 | `Dextre Special Purpose Dexterous Manipulator CSA facts ...` | Wikipedia and news only (15-year design life); NTRS 20100036524 not opened | thin (secondary; lead) |
| 101 | `Robonaut 2 returned to Earth 2018 ...` and page Rogers (NASA JSC), "Robonaut's Return to ISS", POIWG, 24 Apr 2019 (NTRS 20190025367) | Cause of the R2 anomaly | useful |
| 102 | `Curiosity wheel damage ...` page: Graser et al., "Rimmed Wheel Performance on the Mars Science Laboratory Scarecrow Rover" (JPL) | 0.75 mm skin; damage rate; 21.875 km at sol 2633 | useful |
| 103 | `water triple point 273.16 K 611.657 Pa IAPWS NIST value` and page Guildner, Johnson and Jones, J. Res. NBS 80A (1976) via Europe PMC | Vapor pressure of water at the triple point 611.657 Pa | useful |
| 104 | `polydimethylsiloxane PDMS gas permeability ... Merkel 2000` and page PMC3945670 | Europe PMC returned HTTP 500; the 800 Barrer O2 figure exists only in a search summary | dead (sources; not used) |
| 105 | `perfluoropolyether PFPE Krytox grease radiation gamma dose degradation ...` and page S. Mori et al., NASA Technical Paper 2910 (1989), "Degradation and Crosslinking of Perfluoroalkyl Polyethers Under X-Ray Irradiation in Ultrahigh Vacuum" (NTRS 19890011732) | Mechanism only; no dose threshold | thin |
| 106 | `JPL "NASA's COLDArm in Thermal Vacuum Testing"` page (jpl.nasa.gov/images/pia26162) and JPL R&TD poster R21008p (Kennett et al., FY21) | COLDArm tested at -180 C; state-of-the-art mobility actuators need heating to at least -55 C | useful |
| 107 | Page: NASA/JPL "NASA Concludes Attempts to Contact Mars Rover Spirit", 24 May 2011; Spaceflight Now same date | Cold survival failure; -67 F is from the AP/Spaceflight Now report of a NASA statement | useful |
| 108 | `Agility Robotics Digit V4 specifications sheet ...` | Secondary only (automate.org: Digit 5 90 min, 9 min recharge) | thin (secondary; lead) |
| 109 | `NASA Mars fact sheet ...`, Mars TSI search, and Opportunity dust-storm NTRS 20190028687 | The NTRS paper is about dust abrasion on solar cells, not the storm; storm power figures remain press-only | thin / dead (sources) |

Count at the time of writing: 109 numbered log rows (searches and page openings, some rows combine a search with the page it led to). Dead ends:
rows 1, 3, 14 (partly), 28 (partly), 30, 33, 38, 45, 46, 47, 72, 74 (DTIC part), 90, 92, 94, 104, 109 (partly) = 16 dead
or partly dead rows.

## 3. Findings

**How to read the tables.** Full citations (publisher, title, URL, date, type) are in the Source register below; each table
cell cites a key such as S3. "Primary" = space agency, peer-reviewed paper, handbook or dataset, or a manufacturer's own
spec for its own product. Units are as printed in the source; a conversion I made is marked "(conv.)" and uses only an exact
definition (1 Btu/h = 0.29307107 W; 1 lb = 0.45359237 kg). Dose units: 1 Gy = 100 rad; "krad(Si)" is dose to silicon and
"rads(C)" in the 1971 handbook is dose to carbon; they differ by a few percent for the photon spectra involved and I do not
convert between them.

### Source register

| Key | Publisher, title, URL, date | Type |
|---|---|---|
| S1 | NASA JSC (N. Radford), "Valkyrie, NASA's New Humanoid", slides, 25 Feb 2014. https://ntrs.nasa.gov/citations/20140011889 | Primary (agency slides) |
| S2 | NASA, "Valkyrie (R5)" technology page. https://www.nasa.gov/technology/r5/ (read 2026-10-10) | Primary |
| S3 | S. J. Jorgensen, J. Holley, F. Mathis, J. S. Mehling, L. Sentis, "Thermal Recovery of Multi-Limbed Robots with Electric Actuators", IEEE Robotics and Automation Letters, accepted Dec 2018 (arXiv:1902.00187v4, 21 May 2019). https://arxiv.org/abs/1902.00187 | Primary (peer-reviewed; NASA JSC authors) |
| S4 | Boston Dynamics, Atlas product page and spec sheet. https://bostondynamics.com/products/atlas/ and https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf (Jan 2026) | Primary (manufacturer, own product) |
| S5 | T. D. Ahlstrom, M. A. Diftler, R. B. Berka, J. M. Badger, S. Yayathi, A. W. Curtis, C. A. Joyce, "Robonaut 2 on the International Space Station: Status Update and Preparations for IVA Mobility", AIAA, 2013. https://ntrs.nasa.gov/citations/20140000957 | Primary |
| S6 | M. A. Diftler and R. O. Ambrose, "Robonaut: A Robotic Astronaut Assistant", NASA JSC (PDF undated; cites work to 1999, so about 2000). https://ntrs.nasa.gov/citations/20100033240 | Primary |
| S7 | D. Sinclair and J. Dyer, "Radiation Effects and COTS Parts in SmallSats", SSC13-IV-3, 27th AIAA/USU Conference on Small Satellites, 2013. https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Radiation%20Effects%20and%20COTS%20Parts%20in%20SmallSats.pdf | Primary (peer-reviewed conference) |
| S8 | T. A. Carstens and M. J. Campola, NASA GSFC Code 561, "Total Dose Modeling of the Transit Through the Van Allen Belts", LSIC presentation, 25 May 2022. https://ntrs.nasa.gov/citations/20220007131 | Primary (agency presentation) |
| S9 | Y. Gao et al., "Radiation effects on lithium metal batteries", The Innovation, 24 Jun 2023, doi:10.1016/j.xinn.2023.100468. https://ira.lib.polyu.edu.hk/handle/10397/108456 | Primary (peer-reviewed) |
| S10 | C. L. Hunks and D. J. Hunzmun (Battelle) for NASA, "Radiation Effects Design Handbook, Section 3. Electrical Insulating Materials and Capacitors", NASA CR-1787, Jul 1971. https://ntrs.nasa.gov/citations/19710020300 | Primary (agency handbook; old) |
| S11 | W. Powell (NASA STMD), "High Performance Spaceflight Computing (HPSC) for Lunar and Planetary Missions", LPSC, 12 Mar 2025. https://ntrs.nasa.gov/citations/20250002070 | Primary |
| S12 | R. Ginosar (Ramon Chips), "Survey of Processors for Space", DASIA 2012. https://www.ee.technion.ac.il/~ran/papers/SurveySpaceProcessors.DASIA2012.pdf | Secondary (conference survey by a vendor) |
| S13 | S. Mori et al., "Degradation and Crosslinking of Perfluoroalkyl Polyethers Under X-Ray Irradiation in Ultrahigh Vacuum", NASA TP-2910, 1989. https://ntrs.nasa.gov/citations/19890011732 | Primary |
| S14 | L. Kauder, "Spacecraft Thermal Control Coatings References", NASA/TP-2005-212792, Dec 2005. https://ntrs.nasa.gov/citations/20070014757 | Primary (handbook) |
| S15 | L. Carrillo, D. Farner, C. Preston, "ISS Payload Thermal Environments", NASA TFAWS 2015 short course. https://tfaws.nasa.gov/wp-content/uploads/TFAWS2015-SC-ISS-Payload-Thermal-Design.pdf | Primary |
| S16 | NASA, "Active Thermal Control System (ATCS) Overview" (ISS fact sheet, undated). https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf | Primary |
| S17 | NIST, CODATA value: Stefan-Boltzmann constant. https://physics.nist.gov/cgi-bin/cuu/Value?sigma (read 2026-10-10) | Primary (dataset) |
| S18 | IAU 2015 Resolution B3, "Nominal values for selected solar and planetary quantities", arXiv:1605.09788 | Primary (peer-reviewed) |
| S19 | NASA GSFC NSSDC, "Mars Fact Sheet". https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html | Primary (dataset) |
| S20 | NASA GSFC NSSDC, "Moon Fact Sheet". https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html | Primary (dataset) |
| S21 | E. W. Roberts, P. Bridgeman, M. Jansson, M. Schulke, A. Tvaruzka, "The Performance and Life of Fluid-Lubricated Harmonic Drive Gears", ESMATS 2015 (ESTL, Harmonic Drive AG, ESA). https://esrtechnology.com/wp-content/uploads/2026/06/ESMATS-16-2015-Roberts-The-Performance-and-Life-of-Fluid-Lubricated-Harmonic-Drive-Gears.pdf | Primary (peer-reviewed symposium) |
| S22 | W. R. Jones Jr. and M. J. Jansen, "Space Tribology", NASA/TM-2000-209924, Mar 2000. https://ntrs.nasa.gov/citations/20000057374 | Primary |
| S23 | B. L. Sater (NASA), "Method of Cold Welding Using Ion Beam Technology", US Patent 4,245,768, 20 Jan 1981. https://ntrs.nasa.gov/citations/19810010928 | Primary (patent background section) |
| S24 | NASA GSFC, "Outgassing Database User Guide". https://etd.gsfc.nasa.gov/capabilities/outgassing-database/user-guide/ | Primary |
| S25 | NuSil/Avantor white paper, "Evaluating low and ultra-low outgassing silicones for space applications" (undated). https://av.cmd.avantorsciences.com/rq/iddl/evaluating_low_ultra_low_outgassing_silicones_for_space_applications | Secondary (vendor) |
| S26 | J. R. Gaier, "The Effects of Lunar Dust on EVA Systems During the Apollo Missions", NASA/TM-2005-213610, Mar 2005. https://ntrs.nasa.gov/citations/20050160460 | Primary |
| S27 | M. P. Proctor and P. J. Dempsey, "Survey of Dust Issues for Lunar Seals and the RESOLVE Project", NASA GRC slides. https://ntrs.nasa.gov/citations/20080003835 | Primary |
| S28 | P. M. Wensing, A. Wang, S. Seok, D. Otten, J. Lang, S. Kim, "Proprioceptive Actuator Design in the MIT Cheetah", IEEE Transactions on Robotics 33(3):509-522, 2017. https://dspace.mit.edu/handle/1721.1/119863 | Primary (peer-reviewed) |
| S29 | L. Ray, A. Price, A. Streeter, D. Denton, J. Lever, "The Design of a Mobile Robot for Instrument Network Deployment in Antarctica", IEEE ICRA 2005. https://crobots.engineering.dartmouth.edu/papers/Crobots_ICRA2005_A4.pdf | Primary (peer-reviewed) |
| S30 | JPL, R&TD poster R20129p, M. Smart et al., "The Development of Advanced High Voltage, High Specific Energy and High Power Li-ion Cells with Improved Low Temperature Performance", FY21. https://www.jpl.nasa.gov/site/research/media/posters/2021/R20129p.pdf | Primary |
| S31 | JPL, R&TD poster R21008p, A. Kennett et al., "Long Life, High Speed, Heaterless Mobility Actuators", FY21. https://www.jpl.nasa.gov/site/research/media/posters/2021/R21008p.pdf | Primary |
| S32 | NASA JPL, "NASA's COLDArm in Thermal Vacuum Testing", 20 Dec 2023. https://www.jpl.nasa.gov/images/pia26162-nasas-coldarm-in-thermal-vacuum-testing/ | Primary |
| S33 | NASA, "State-of-the-Art of Small Spacecraft Technology", Chapter 3 Power, 2022 edition. https://www.nasa.gov/wp-content/uploads/2023/05/3.-soa-power-2022.pdf | Primary (agency report; compiles manufacturer data) |
| S34 | B. Hong et al., "All-solid-state batteries designed for operation under extreme cold conditions", Nature Communications, 2025, doi:10.1038/s41467-024-55154-5 (PMC11696891) | Primary (peer-reviewed) |
| S35 | C. Kirchner-Burles et al., "Safety and performance implications of lithium plating induced by sub-zero temperature cycling of lithium-ion batteries", Journal of Power Sources 660 (2025) 238565. https://discovery.ucl.ac.uk/id/eprint/10215263/ | Primary (peer-reviewed) |
| S36 | B. McKissock, P. Loyselle, E. Vogel, "Guidelines on Lithium-ion Battery Use in Space Applications", NASA/TM-2009-215751 (NESC-RP-08-75), May 2009. https://ntrs.nasa.gov/citations/20090023862 | Primary |
| S37 | NASA JSC, "Crewed Space Vehicle Battery Safety Requirements", JSC 20793 Rev C, Jan 2014. https://ntrs.nasa.gov/citations/20160003504 | Primary |
| S38 | C.-K. Huang, J. S. Sakamoto, S. Surampudi, J. Wolfenstine, "Li-ion cell development for low temperature applications", JPL (undated, about 2000). https://ntrs.nasa.gov/citations/20000056605 | Primary |
| S39 | A. Kurs et al., "Wireless power transfer via strongly coupled magnetic resonances", Science, 2007 (abstract read via Europe PMC, PMID 17556549) | Primary (peer-reviewed) |
| S40 | R. M. Dickinson (JPL), "Microwave Power Transmitting Phased Array Antenna Research Project Summary Report", NASA CR-157843, 1978. https://ntrs.nasa.gov/citations/19790005092 | Primary |
| S41 | M. Mesloh, S. England, E. Benson, S. Thompson, S. Rajulu (NASA JSC), "The Effects of Extravehicular Activity (EVA) Glove Pressure on Hand Strength", NTRS record 2010. https://ntrs.nasa.gov/citations/20100008464 | Primary |
| S42 | NASA JSC, "EMU LSS/SSA Data Book", Rev V, JSC-E-DAA-TN55224, Sep 2017. https://www.nasa.gov/wp-content/uploads/2017/02/esoc-13_rev._v_emu_hardware_data_book_jsc-e-daa-tn55224.pdf | Primary |
| S43 | C. E. Carr and J. McGee, "The Apollo Number: Space Suits, Self-Support, and the Walk-Run Transition", PLoS ONE 4(8):e6614, 2009 (read via Europe PMC XML) | Primary (peer-reviewed) |
| S44 | R. R. Neptune et al., "Ankle plantar flexor force production is an important determinant of the preferred walk-to-run transition speed", J. Exp. Biol. 208:799-808, 2005 | Primary (peer-reviewed; states the Froude-number fact in its introduction) |
| S45 | NASA, "Human Integration Design Handbook", NASA/SP-2010-3407 Rev 1, 5 Jun 2014. https://www.nasa.gov/sites/default/files/atoms/files/human_integration_design_handbook_revision_1.pdf | Primary (handbook) |
| S46 | NASA JPL, "Six Things to Know About NASA's Opportunity Mars Rover", 13 Feb 2019; "NASA Concludes Attempts to Contact Mars Rover Spirit", 24 May 2011. https://www.jpl.nasa.gov/news/six-things-to-know-about-nasas-opportunity-mars-rover/ ; https://www.jpl.nasa.gov/news/nasa-concludes-attempts-to-contact-mars-rover-spirit/ | Primary |
| S47 | S. Clark, Spaceflight Now, "NASA closes book on Spirit rover's historic mission", 24 May 2011. https://www.spaceflightnow.com/news/n1105/24spirit/index.html | Secondary (quotes a NASA statement) |
| S48 | E. Graser et al. (JPL), "Rimmed Wheel Performance on the Mars Science Laboratory Scarecrow Rover" (about 2020). https://robotics.jpl.nasa.gov/media/documents/Rimmed_Wheel_Performance_on_the_Mars_Science_Laboratory_Scarecrow_Rover.pdf | Primary |
| S49 | NASA, ISS blog posts, 29 and 30 Jun 2026. https://www.nasa.gov/blogs/spacestation/2026/06/30/astronauts-repair-canadarm2-robotic-arm-and-complete-spacewalk/ | Primary |
| S50 | J. Rogers (NASA JSC), "Robonaut's Return to ISS", POIWG, 24 Apr 2019. https://ntrs.nasa.gov/citations/20190025367 | Primary |
| S51 | Dow Corning, "Sylgard 184 Silicone Elastomer" product information (undated). https://www.cnfusers.cornell.edu/sites/default/files/Equipment-Resources/Sylgard_184_data_sheet.pdf | Primary (manufacturer data sheet) |
| S52 | L. A. Guildner, D. P. Johnson, F. E. Jones, "Vapor Pressure of Water at Its Triple Point", J. Res. NBS 80A, 1976 (PMC5293355) | Primary (peer-reviewed) |
| S53 | R. L. Patterson, A. Hammoud, M. Elbuluk, "Assessment of electronics for cryogenic space exploration missions", Cryogenics 46 (2006) 231-236 (NASA Glenn). https://nepp.nasa.gov/files/15442/06_281_Patterson%205%20Elsevier%20Cryogenics%20Journal%20Paper.pdf | Primary (peer-reviewed); minus signs lost in the PDF text layer |
| S54 | W. Johnson (NASA GRC), "Multilayer Insulation for In-Space Cryogenic Applications", TFAWS (NTRS 20240010471), 2024. https://ntrs.nasa.gov/citations/20240010471 | Primary |
| S55 | Wow Orin authors, "Structural Optimization of Lightweight Bipedal Robot via SERL", arXiv:2408.15632 (preprint, Aug 2024) | Secondary (preprint; simulation) |
| S56 | ESA, "Surviving the long dark night of the Moon", 23 Mar 2017. https://www.esa.int/Our_Activities/Space_Engineering_Technology/Surviving_the_long_dark_night_of_the_Moon | Primary (agency feature page) |

### 3.A Thermal

**A1. Published humanoid figures (mass, energy, power, thermal limits).**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Valkyrie (R5) mass, height, DOF, battery | 300 lb (136 kg, conv.); 6 ft 2 in; 44 DOF; battery energy 1.8 kWh, "about an hour" of running | S2 | Primary | S1 gives 125 kg, 44 DOF, 2 kWh (2014 slides, earlier build); see Conflicts | Medium: two NASA sources disagree on mass and energy |
| Valkyrie onboard electronics | 3 Core i7 computers, 1 GPU, 44 motor controllers, 3 IMUs; two Li-ion packs | S1 | Primary | none found | High for the count |
| Valkyrie actuator temperature limits | Actuators "can operate up to 90 C"; operator-set safe limit 70 C; warning zone 75 C; ambient during test 25 C | S3 (Sec. VI-VII, footnote 3) | Primary | none found | High |
| Valkyrie heating rate | Balancing on one leg "heats up the stance leg in less than two minutes" to the warning zone; recovery to below 70 C took about one minute; right-leg actuators cooled in 21 s with contact switching | S3 (Sec. VII) | Primary | none found | High (one robot, one test, ventilated lab air) |
| Valkyrie thermal concern | Torso and leg actuators (motor drivers and cores) "naturally heat up due to the high actuator efforts needed to balance"; operations are postponed until they cool | S3 (Sec. I, III) | Primary | none found | High |
| Valkyrie actuator type | 32 actuated DOF excluding fingers; harmonic-driven series-elastic electric actuators; 3 thermistors per actuator | S3 (Sec. III) | Primary | S1 (44 motor controllers incl. hands) | High |
| Atlas (production electric) | 90 kg; 1.9 m; 56 DOF; battery life 4 hr; IP67; operating temperature -20 to 40 C; battery self-swap; instant payload 50 kg, sustained 30 kg | S4 | Primary (manufacturer) | none found; battery Wh not published | High for what is stated |
| Robonaut 2 EVA thermal approach | Batpack and torso "use fans to help cool electronics"; "main challenge ... will be heat sinking all of the electronics to sufficiently radiate heat to avoid overheating"; heaters for cold; active cooling loops "add complexity and current design concepts do not require them" | S5 (Sec. "Future upgrades for EVA") | Primary | none found | High |
| Robonaut 2 climbing legs thermal test | "some thermal vacuum testing has been performed on the actuators and motors drivers"; legs not certified for EVA | S5 | Primary | S6 says Robonaut 1 arms used "thermal vacuum rated motors" and "other scales have been built for thermal vacuum testing" | Medium: no temperatures or results given |
| Digit, Optimus, Figure power figures | Not obtained from a primary source | none | n/a | n/a | n/a (see Open threads) |
| Human metabolic baseline | Nominal crewmember 474 Btu/h (139 W, conv.); sleeping 300 Btu/h (88 W, conv.) | S45 (Sec. 6.2.3, assumptions for an 82 kg crewmember in a 21 C cabin) | Primary | S42: EMU design loads below | High |
| EMU design heat loads | Average 1000 Btu/h (293 W, conv.) for 7 h; peak 2000 Btu/h (586 W, conv.) for 15 min; 1600 Btu/h for 1 h | S42 (Sec. 1.1) | Primary | S45 | High |
| Human body surface area | 15,300 cm2 (5th-percentile female) to 22,800 cm2 (95th-percentile male); DuBois: area (cm2) = 71.84 x W^0.423 x H^0.723 (W kg, H cm) | S45 (Table 4.6-1, Sec. 4.6.2.2) | Primary | none found | High |

**A2. Radiation physics, surface optical properties, and the environment.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Stefan-Boltzmann constant | 5.670 374 419 x 10^-8 W m^-2 K^-4 | S17 | Primary | search summaries of CODATA 2018/2022 agree | High |
| Solar irradiance at 1 AU | nominal TSI 1361 W m^-2 | S18; S19 and S20 list 1361.0 | Primary | S19, S20 | High |
| Mars solar irradiance (top of atmosphere, mean) | 586.2 W m^-2 | S19 | Primary | none found for surface irradiance | High for the top-of-atmosphere value; surface value not found |
| Mars surface pressure; diurnal temperature | 6.36 mb at mean radius (varies 4.0 to 8.7 mb); Viking 1 site 184 K to 242 K (-89 to -31 C) | S19 | Primary | none found | High |
| Moon equatorial diurnal temperature; sidereal rotation; synodic period | 95 K to 390 K; 655.72 h; 29.53 d | S20 | Primary | S26 and ESA page give "-170 C" lunar night | High |
| Lunar surface pressure at night | 3 x 10^-15 bar | S20 | Primary | none found | High |
| White paint Z93 | solar absorptance 0.16, normal emittance 0.92 | S14 (Table 4.2) | Primary | derived use below | High |
| Black paint Z306 | 0.96 / 0.91 | S14 (Table 4.1) | Primary | none found | High |
| Black Kapton film | 0.93 / 0.85 | S14 (Table 4.9) | Primary | none found | High |
| Beta cloth (EMU outer-layer fabric class), two examples | Beta Cloth/VDA Sheldahl 0.38 / 0.85; Beta Cloth/VDA Chemfab 500 (no silicone) 0.45 / 0.90 | S14 (Table 4.2) | Primary | none found | Medium: I did not find textile data for ordinary clothing |
| Lunar dust on radiators | IR emittance of dust about 0.88 vs 0.83 for the surface; "only 11 percent dust coverage" doubled solar absorptance; 10 psi nitrogen jet for 15 s lowered absorptance only from 0.245 to 0.239 | S26 | Primary | none found | High (ground tests on simulated dust; Apollo flight evidence agrees qualitatively) |
| ISS flux used for payload environments | 216 nmi altitude; mean solar 434.6 Btu/hr-ft2 (1371 W/m2, conv.), albedo 0.27, outgoing longwave 76.4 Btu/hr-ft2 (241 W/m2, conv.) | S15 | Primary | solar value agrees with S18 | High |
| Passive 1 ft cube on ISS ELC-1, no internal power, surface a/e = 0.18/0.84 | Night pass -46 to -51 C; orbit-average -31 to +7 C depending on location | S15 (ELC-1 table) | Primary | none found | Medium: S15 says "for trending purposes only" |
| Same cube, a/e = 0.66/0.74 | Night -46 to -51 C; day pass up to +56 C; orbit average -21 to +39 C | S15 | Primary | | Medium |
| Same cube, a/e = 0.45/0.12 | Day pass up to +155 C; orbit average +9 to +119 C; exceeds the +112.8 C EVA touch limit | S15 | Primary | | Medium |
| ISS orbit timing in S15 | night pass 30 min, day pass 60 min, orbit 90 min | S15 (Sec. 5) | Primary | | High |
| Typical ISS hardware lower limit | -40 C | S15 | Primary | S31 | High |

**A3. Heat rejection hardware and insulation (real figures).**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| ISS Photovoltaic Radiator (PVR) | rejects up to 14 kW; 7 panels; 10.24 ft x 44.62 ft (3.12 m x 13.6 m); mass 1,633 lb (740.7 kg) | S16 | Primary | EEATCS radiator ORU has the same stated dimensions | High |
| ISS External Active Thermal Control System | 35 kW per loop, 70 kW total; ammonia freezing point -107 F (-77 C) | S16 | Primary | none found | High |
| EMU cooling method | Water sublimator: feedwater freezes and sublimates to space; liquid cooling and ventilation garment on the wearer | S42 (Sec. 1.2.1) | Primary | | High |
| MLI heat flux, vacuum | 0.2 to 0.4 W/m2 for the NASA-funded 1970s blankets listed (30 layers, 14.1 layers/cm, 293 K to 78 K, 2e-6 Torr); the cited MLI equation is "only good less than 10^-4 Torr" | S54 | Primary | S54 also lists entries at 2.7 and 5.8 W/m2 for other blanket types | High for vacuum performance |
| MLI in air | "On the launch pad ... a MLI blanket can loosely be modeled as a stagnant gas pocket"; convection removed only in vacuum | S54 | Primary | | High |

**A4. Temperature ranges of materials and components.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Silicone elastomer (Sylgard 184, a representative skin-class material) | service range -45 to 200 C; thermal conductivity 0.2 W/m K; linear CTE 310 ppm/C; Shore A 50; low-temperature behavior "can become more complex" at -55 C | S51 | Primary (manufacturer) | search summaries quoted 0.27 W/m K; not opened | Medium: one product; the fiction's skin material is not specified |
| Li-ion operating range | "Typical Li-Ion batteries have an operating temperature range of -20 C to 60 C" | S33 (Sec. 3.5.3) | Primary | S36: optimum 20 to 40 C | High |
| Li-ion optimum | "between 20 and 40 C" for most Li-ion batteries | S36 | Primary | S33 | High |
| Mars-mission battery qualification | Charge on Mars -10 to 40 C; discharge on Mars -30 to 40 C; cruise -30 to 40 C | S36 (qualification table) | Primary | | High |
| State-of-practice flight cell | InSight-class large-format cells operate -30 C to +35 C; at -40 C deliver 105 Wh/kg at C/5 when charged at room temperature; commercial 18650 cells "negligible capacity at -40 C" | S30 | Primary | S34: Panasonic 18650 | High |
| Commercial 18650 retention in the cold | 66% at -20 C and 5% at -40 C of room-temperature energy at rates below 0.1 C | S34 (introduction, citing a manufacturer curve) | Primary (peer-reviewed paper quoting data) | S30 | Medium |
| Cathode half-cell capacity vs temperature | 100% at +20 C, 70% at -20 C, 60% at -30 C, 46% at -40 C (LiCo0.2Ni0.8O2 half cell) | S38 | Primary (about 2000; chemistry old) | S30 | Medium (old chemistry) |
| Lithium plating on cold cycling | Cells cycled at -10 C show reversible plating; at -20 C plate irreversibly; jelly-roll collapse observed | S35 | Primary | S36 (Mars charge floor -10 C) | High |
| Solid-state (lab) cold operation | All-solid-state coin cells with an amorphous Li3N-TaCl5 electrolyte delivered 143.78 mAh/g at -40 C (rate not stated in the passage I read) and 51.94 mAh/g at -60 C at 18 mA/g (a very slow rate); 83.5% capacity retention at -30 C after 100 cycles | S34 | Primary | no flight or pack-scale data found | Low for any humanoid use: lab coin cells at low rate |
| Solid-state at the high end | Manufacturer-claimed cell values 390 to 560 Wh/kg (Solid Power), 230 to 300 Wh/kg projected (QuantumScape) | S33 (Table 3-7) | Primary (agency compilation of manufacturer claims) | none independent | Low (claims, not flight data) |
| Mobility-actuator cold limit | "the current state of the art actuators require heating to at least -55 C, in flight"; goal of -230 to +125 C without preheating | S31 | Primary | S32 | High |
| Cold-capable arm demonstrated | COLDArm tested in a thermal vacuum chamber reduced to -180 C (-292 F), using bulk metallic glass gears (no wet lubrication or heating), cold motor controllers and a cryogenic six-axis force/torque sensor | S32 | Primary | S31 | High |
| Spacecraft electronics temperature | Spacecraft electronics are normally held near 20 C with radioisotope heaters; COTS bipolar transistors lose current gain and MOSFET gate thresholds rise when cooled; one DC/DC converter's regulation worsens with falling temperature (the minus signs are missing in the PDF text, so the temperatures cannot be quoted) | S53 | Primary | | Medium (qualitative only) |
| Harmonic drive in the cold | At -25 C, efficiency is "appreciably less" than at +90 C because of viscous losses; with MAC grease, cold-soak efficiency started near 20% and fell to about 10% | S21 | Primary | S22 notes liquid-lubricated space mechanisms normally see -10 to -20 C | High |
| Robonaut 2 encoder | Original Mylar optical code disk replaced by a metal disk "that is able to survive a much greater temperature range" | S5 | Primary | | Medium |

**A5. Clothing and skin on a machine (materials constraints).**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Habitat acceptance of non-metals on a robot | "on-orbit off gassing and flammability testing are performed on most non-metallic materials"; R2's Lycra shoulder and elbow covers were replaced by a 100% Nomex stretch material for mobile use because Lycra has undesirable flammability | S5 (Sec. IVA mobility safety) | Primary | S24 (outgassing limits) | High |
| Apollo suit outer layers | Outer layer worn through into the Mylar MLI above the boot after 8 hr of surface activity; cover gloves discarded after two EVAs; zippers, helmet and glove-disconnect seals cleaned and re-lubricated between EVAs | S26; S27 | Primary | | High |

### 3.B Radiation

**B1. Electronics: dose, single events, hardening, shielding.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Commercial (COTS) parts, total ionizing dose | "Most commercial components are radiation tolerant to 5 krad. Many are radiation tolerant to 20 krad or more. Some will fail before 1 krad. Without testing, it is impossible to predict which category a part will fall into." "Provided the lifetime dose is under 30 krad, a solution can probably be realized with commercial parts." | S7 | Primary | none independent found; the figure is a rule of thumb from LEO small-satellite practice | Medium |
| Lot-to-lot variation | Parts made last year may tolerate a dose that this year's lot does not; flight lots must be identical to tested lots | S7 | Primary | | High |
| Radiation-hardened parts, rated dose | "Rated radiation dose of 100 krad to > 1 Mrad"; no single-event latchup | S7 | Primary | S11: NASA's next flight computer requires 200 kRad TID with hardening by design | Medium |
| NASA HPSC computer | 200 kRad total ionizing dose requirement; hardening by design for single-event effects | S11 | Primary | | High |
| Cost and speed penalty of hardened processor | RAD750: 250 nm process, 133 to 166 MHz, about 300 MIPS, unit price above US$200,000 (survey dated 2012) | S12 | Secondary (survey by a space-processor vendor) | | Medium |
| Single-event upset example | A small-satellite supervisor processor with 67,584 RAM bits: expected upset every 4.4 x 10^6 s (52 days) for a proton flux of about 100 /cm2/s behind 0.7 cm aluminum; handled with software error correction | S7 | Primary | | Medium (one device, one orbit) |
| Shielding limit | "shielding has very small marginal benefit beyond about 5 mm (200 mil)" of aluminum for LEO trapped particles; 1 mm tungsten has the mass of 7.1 mm aluminum and stops electrons like 6 mm and protons like 4 mm of aluminum; 5-year dose 10.37 krad with a 2.5 mm aluminum chassis side falls to 2.71 krad with a 1 mm tungsten shell | S7 | Primary | S8 trend (curves flatten beyond about 5 mm) | High |
| Humanoid electronics are distributed | Valkyrie has 44 motor controllers (one per actuator, in the limbs) plus 3 Core i7 computers | S1; S3 (three thermistors and a logic board in each actuator) | Primary | | High |

**B2. Dose behind aluminum shielding for trajectories through the Earth's trapped-radiation belts** (S8: AP-9/AE-9 models, solid aluminum sphere,
silicon target, solar protons not included; units krad(Si); 1 mil = 0.0254 mm). Primary; no independent cross-check found;
confidence high that the numbers are as printed, medium that they transfer to a body of different geometry.

| Shield (Al) | Direct Earth-to-Moon transfer (3 to 6 days typical) | GTO phase 1, per revolution (perigee 188 km, apogee 35,790 km, 10.51 h) | GTO phase 3, per revolution (perigee 33,194 km, 22.85 h) | Spiral, 2 months in belts | Spiral, 10 months in belts |
|---|---|---|---|---|---|
| 1 mil (0.03 mm) | 128 | 283 | 467 | 50,500 | 221,000 |
| 10 mil (0.25 mm) | 16.3 | 37.0 | 34.2 | 6,110 | 24,000 |
| 25 mil (0.63 mm) | 5.76 | 12.5 | 7.43 | 2,090 | 7,280 |
| 50 mil (1.27 mm) | 2.29 | 4.57 | 2.03 | 774 | 2,490 |
| 100 mil (2.54 mm) | 0.559 | 1.04 | 0.391 | 177 | 545 |
| 200 mil (5.08 mm) | 0.0437 | 0.0739 | 0.0254 | 12.5 | 36.1 |
| 300 mil (7.62 mm) | 0.0070 | 0.0126 | 0.0047 | 1.86 | 5.34 |
| 500 mil (12.7 mm) | 0.0013 | 0.0035 | 0.0014 | 0.410 | 1.29 |
| 900 mil (22.9 mm) | 0.0006 | 0.0019 | 0.0007 | 0.203 | 0.648 |

**B3. Batteries and soft materials.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Li-metal cells after 20 kGy of Co-60 gamma (20 kGy = 2 Mrad, conv.) | Capacity retention after 350 cycles at 1 C: NCM811 cell 57.7% (control 76.6%), LFP 69.6% (control 90.9%), LCO 70.3% (control 94.2%). The liquid electrolyte is the largest contributor to the loss, then the cathode material, then the binder | S9 | Primary | none found for Li-ion cells specifically | Medium: lithium-metal cells, gamma only |
| Silicone rubber (wire insulation) | no noticeable degradation of physical properties up to 8.8 x 10^5 rads(C); slight loss of resilience at 8.8 x 10^6; serious deterioration, cracking or crumbling when stressed, at 8.8 x 10^7 and above | S10 | Primary (1971 handbook) | none found | Medium: one product form, old data |
| PTFE (Teflon TFE) | approximate damage threshold 1.7 x 10^4 rads(C); 25 percent damage dose 3.4 x 10^4 rads(C); crumbles at about 10^7 rads. FEP in vacuum kept its elongation to a dose ten times higher than TFE-7 | S10 | Primary | none found | Medium |
| Polyurethane | limited data; two studies (a reactor exposure with gamma 1.4 x 10^6 rads(C), and an electron exposure) found insignificant changes in electrical properties; mechanical data are not given | S10 | Primary | none found | Low |
| Perfluoropolyether (PFPE) lubricants | X-ray irradiation in ultrahigh vacuum causes both degradation and crosslinking; the fluids become tacky; no dose threshold given | S13 | Primary | S22: PFPE contact failure is also driven by surface fluorides (tribochemistry) | Low for a dose number (none found) |

### 3.C Vacuum and materials

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Outgassing screening test | 398 K (125 C) for 24 h in vacuum; acceptance limits total mass loss (TML) at most 1.0 percent and collected volatile condensable material (CVCM) at most 0.10 percent; water vapor regained measured after 24 h at 25 C, 50 percent RH | S24 | Primary | S25 states the same limits | High |
| Silicones that pass | 13 NuSil silicones: TML 0.02 to 0.52 percent and CVCM 0.00 to 0.09 percent (e.g., one 2-part dimethyl: 0.02 / 0.00; a 1-part oxime coating: 0.52 / 0.09); an "ultra-low outgassing" tier demands TML at most 0.1 and CVCM at most 0.01 | S25 | Secondary (vendor) | S24 limits | Medium: selected space-grade grades; ordinary skin-grade silicone was not found in the database I could open |
| Habitat materials rule | Non-metallic materials on R2 undergo offgassing and flammability testing; new materials not in the JSC database must be tested | S5 | Primary | | High |
| Cold welding | "As little as one or two monolayers of metallic oxides effectively interrupt or prevent metallic bonding." A surface cleaned at one atmosphere is recontaminated by a monolayer in less than 10^-8 s; at 10^-6 torr the recontamination time is a few seconds and rises as pressure falls | S23 | Primary (NASA patent background) | none found; no ESA handbook opened | Medium |
| Harmonic drive life in high vacuum, fluid lubricated | 160:1 gear, rated 40 N m, tested at 4 N m output, 50 rpm input, +90 C: PFPE-lubricated efficiency 80 to 90 percent over the first 5 million input revolutions, 50 to 70 percent afterward, 40 percent at about 11 million, test stopped near 12 million input revolutions (about 75,000 output revolutions); post-test inspection found metal transfer at the flexspline/wave-generator interface ("lubrication having become ineffective"). MAC-grease unit: about 80 percent for about 12 million input revolutions, then low | S21 | Primary | S22: PFPE liquid lubricants in boundary contact fail by an autocatalytic fluoride reaction, abruptly | High for this test; medium for transfer to other gears |
| Other lubricants | In an ESTL linear ball-screw test the two PFPE lubricants "failed rapidly"; Braycote 601 grease with ion-plated lead and sputtered MoS2 reached the 2 million cycle requirement | S22 | Primary | | Medium |
| MoS2 dry lubricant and air | friction below 0.01 in ultrahigh vacuum, 0.01 to 0.04 in normal vacuum with long life; in humid air about 0.15 and "very limited life" | S22 | Primary | S31 (dry-lubricated gearing for -230 to +125 C is an open development goal) | High |
| Liquid-lubricated space mechanisms, temperature | "do not involve wide temperature ranges"; -10 to -20 C sometimes encountered | S22 | Primary | S21 (-25 C cold soaks) | High |
| Lunar dust, abrasion | Apollo 12: suits more worn after 8 hr of surface activity than training suits after 100 hr, worn through the outer layer into the Mylar insulation; Apollo 17 cover gloves discarded after two EVAs; surface times were 21 to 75 hr per mission | S26 | Primary | | High |
| Lunar dust, seals | Apollo 12 suit leak rate 0.15 psi/min after the first EVA and 0.25 psi/min after the second, against a 0.30 psi/min limit; all environmental and gas sample seals failed because of dust; 4 of 12 sample containers leaked because of dust or equipment on seals | S26; S27 | Primary | | High |
| Lunar dust, thermal | LRV batteries exceeded operating temperature limits on Apollo 16 and 17 because dust could not be brushed off; magnetometer temperatures about 68 F higher than expected on Apollo 12 | S26 | Primary | | High |
| Suit seal practice | Wrist bearings and rotational connectors had fabric covers against dust; glove-disconnect seals were cleaned and re-lubricated with Krytox between EVAs | S27 | Primary | | High |
| Triple point of water | vapor pressure 611.657 Pa +/- 0.010 Pa (99 percent limits) | S52 | Primary | S19: Mars mean surface pressure 6.36 mb (636 Pa) | High |
| Battery vacuum qualification | Batteries in pressurized volumes: vacuum exposure at about 0.1 psi for at least 6 h; batteries in unpressurized volumes: thermal-vacuum cycles at 1 x 10^-5 Torr; eight thermal cycles with first and last under vacuum | S37; S36 | Primary | | High |

### 3.D Power

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Li-ion cell specific energy, 18650 | 112 (Canon BP-930s), 182 (Molicel ICR18650H), 191 (LG ICR18650 B3), 243 (Panasonic NCR18650B), 260 (LG MJ1) Wh/kg; "latest cells have all exceeded 240 Wh/kg" | S33 (Table 3-4) | Primary (agency compilation of manufacturer data) | | High at cell level; pack level is lower and not found |
| Li-ion 21700 | 262 and 264 Wh/kg | S33 | Primary | | High |
| Solid-state cells | Manufacturer values 390 to 560 Wh/kg (Solid Power) and projected 230 to 300 Wh/kg (QuantumScape); not flight-proven | S33 (Table 3-7) | Primary compilation of claims | S34 (cold, lab only) | Low |
| Fuel cells | A hydrogen-peroxide fuel cell reached over 1000 Wh/kg but "cannot be recharged on orbit"; regenerative fuel cells "currently being researched"; fuel cells are "primarily being proposed for small spacecraft propulsion systems rather than for power sub-systems" | S33 (Sec. 3.3.4) | Primary | none found for a human-sized machine | Medium |
| Space solar cell efficiency | triple-junction cells over 32 percent; terrestrial silicon about 20 percent; 38 percent laboratory multi-junction | S33 | Primary | S29 used 20 percent cells | High |
| Humanoid battery energies | Valkyrie 1.8 kWh (S2) or 2 kWh (S1); Robonaut 2 Batpack about 5.79 kWh from 300 Boston Power Swing 5300 cells (24, 48, 96 V buses); Atlas 4 hr, Wh not published (S4) | S1; S2; S5; S4 | Primary | | Medium (Valkyrie sources disagree) |
| Efficiency of a wheeled 90 kg Antarctic robot | estimated 90 W average and 180 W at 0.8 m/s (resistance coefficient 0.25); target power budget about 250 W; gearboxes 90 percent efficient, 100:1, lubricated for -50 C | S29 | Primary | not a humanoid | Medium (estimate) |
| Simulated cost of transport | Cassie 0.762, Unitree H1 0.718, Wow Orin 0.407 (COT = P/(m g v), P = joint power; simulation with one training algorithm) | S55 | Secondary (preprint) | | Low |
| Antarctic solar flux | South Pole summer horizontal 200 to 500 W/m2; with elevation adjustment 800 to 1200 W/m2; November to February average about 1000 W/m2 at about 20 degrees sun elevation; diffuse 50 to 100 W/m2; efficiency rises as temperature falls | S29 | Primary | | Medium |
| Cold charging limit | Mars-mission charge range -10 to 40 C (S36); irreversible plating at -20 C (S35) | S36; S35 | Primary | | High |
| Magnetic-resonance wireless power | 60 W transferred at about 40 percent efficiency over more than 2 m, up to 8 times the coil radius | S39 | Primary | none found for a moving, human-sized receiver | High for the experiment |
| Microwave beaming, design parameter | Beam efficiency depends on tau = sqrt(A_t A_r)/(wavelength x distance); the SPS design point was tau = 1.734; the efficiency curve is a figure in the report (not extractable) | S40 | Primary | JAXA 1.8 kW at 55 m is in news summaries only | Medium |

### 3.E Mechanical

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Motor torque density (rotor-stator, no gearbox) | custom MIT Cheetah motor saturation torque density about 27 N m/kg versus 9 N m/kg for a catalog frameless motor (Emoteq HT-5001); catalog torque density scales roughly as gap radius^0.8 | S28 | Primary | | High |
| Gear efficiency, new | harmonic drive 80 to 90 percent in vacuum at +90 C; 100:1 planetary 90 percent | S21; S29 | Primary | | High |
| Walk-run transition | in normal and reduced gravity humans switch gait at a Froude number (v^2/(g L)) of about 0.5; suited Apollo lunar gait events gave Fr* = 0.358 +/- 0.057 (Apollo number Ap* = 0.684 +/- 0.102); unsuited transition expected near 0.9 in lunar gravity | S44; S43 | Primary | | Medium (human data; a machine's gait is not bound by it, but dynamic similarity is) |
| Surface gravity | Moon 1.62 m/s2; Mars 3.73 m/s2 (mean) | S20; S19 | Primary | | High |
| Microgravity translation | R2 translates on IVA handrails and seat tracks, which "have load and moment limits that R2 must remain below"; the climbing legs have no electromagnetic brakes, so joint motors hold position | S5 | Primary | | High |
| EVA suit mass | Enhanced suit assembly with two arms and two gloves 143.73 lb (65.2 kg, conv.); life-support subsystem 196.7 lb (89.2 kg, conv.), with PLSS 101.4 lb; operating 4.3 psid | S42 (Sec. 1.5.3, Fig. 1.10) | Primary | | High |
| Pressurized glove strength | Phase VI glove at 4.3 psi, 8 subjects: grip 58 percent of bare-hand without the thermal micrometeoroid garment, 46 percent with it (66 and 55 percent unpressurized); lateral pinch 83 to 86 percent; the garment adds stiffness | S41 | Primary | S45 (gloves reduce tactility even unpressurized) | High (small sample) |

### 3.F Cold (additional rows; see also 3.A4)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Lunar night | temperatures "dip below -170 C"; the equatorial range is 95 K to 390 K | S56; S20 | Primary | S26 | High |
| Mars rover thermal design | The rovers' Warm Electronics Box (batteries, computer) must stay within -40 to +40 C; gold-painted insulated walls, silica aerogel, thermostat and heaters, and a heat-rejection system protect it from a daily temperature swing of 113 C | S29 (description of the Mars rovers) | Primary (secondary description of MER) | S19 (diurnal range) | Medium |
| Spirit, loss of survival heat | "With inadequate energy to run its survival heaters, the rover likely experienced colder internal temperatures last year than in any of its prior six years on Mars. Many critical components and connections would have been susceptible to damage from the cold." Reported internal temperature likely about -67 F | S46 (quote); S47 (the -67 F figure) | Primary / secondary | | High for the loss mechanism; medium for the number |
| Antarctic design point | A 90 kg robot designed for -40 C ambient (South Pole summer average -20 to -40 C), with an insulated cold-room test of the drive train | S29 | Primary | S31 | Medium |
| Insulation in vacuum | MLI: 0.2 to 0.4 W/m2 at 293 K to 78 K (30 layers, 2e-6 Torr) | S54 | Primary | | High |

### 3.G Fatigue and lifetime

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Opportunity | Prime mission 90 days; worked more than 14 years; drove 28.06 mi (45.16 km); the right-front wheel drew more current than the others so engineers drove backward to extend its life; last contact sol 5111 (10 Jun 2018) in a dust storm | S46 (JPL 2019) | Primary | NTRS 20200000214 abstract (not downloadable) | High |
| Spirit | Landed Jan 2004 for a 3-month mission; last contact 22 Mar 2010; 4.8 mi driven; two of six wheels stopped rotating and the rover stalled in a sand pit in May 2009; NASA ended contact attempts 25 May 2011 | S46 (dates, mission); S47 (wheels, sand pit, distance) | Primary / secondary | | Medium |
| Curiosity wheels | Aluminum wheel skin 0.75 mm thick; on Sol 490, 4.6 km into the prime mission, "an unexpectedly high rate of damage" was seen; as of Sol 2555 (14 Oct 2019) two broken grousers on the left middle wheel and one on the right middle; 21.875 km by Sol 2633 (1 Jan 2020) | S48 | Primary | | High |
| Canadarm2 | installed 26 Apr 2001; on 27 May 2026 the arm "drew elevated motor current and did not move as expected"; a wrist joint was replaced on 30 Jun 2026 in a 7 h 20 min spacewalk; "designed with replaceable components" | S49 | Primary | an earlier wrist-roll replacement in 2002 is in news only | High |
| Robonaut 2 | On ISS from 2011; returned Feb 2018; cause of the failure was a missing return wire for the computer-chassis power, so current used an undersized path and a backpack connector overheated and opened; the fault was in the original design and only appeared when higher-power processors were added; six crew members, 10 sessions of troubleshooting; "very difficult to repair on-orbit" | S50 | Primary | | High |
| Dextre | design life and service history | not obtained from a primary source | n/a | | n/a (see Open threads) |
| Fluid-lubricated gear life | about 75,000 output revolutions in vacuum at 10 percent of rated torque before efficiency fell to 40 percent | S21 | Primary | | High for the test |
