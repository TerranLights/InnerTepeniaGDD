# Research: Asteroid Belt, Jovian System, Saturnian System, and Deep Interplanetary Transit

Date of research: 2026-10-06. Brief followed: `_BRIEF.md`. No figure is from memory; each table row cites a page opened this session.

## 1. Scope

The main Asteroid Belt (mass, spacing, classes, rotation, gravity, light, temperature, delta-v, light delay, radiation); the Jovian system (radiation belts, Galilean moons, magnetosphere, tides, irradiance, transfer, orbit regimes); the Saturnian system (rings, Titan, Enceladus, radiation, transfer); deep transit (cosmic-ray and solar-particle dose, propulsion, thermal rejection, transfer energy); power scaling and nuclear options; a short interstellar-precursor note.

## 2. SEARCH LOG

(Appended as work proceeds. Format: date, query or URL, rating, notes.)

All entries dated 2026-10-06. "WebFetch" returns a small-model summary of the page, not the raw page; where a number matters it is cross-checked or the raw text was read via a local download (marked "raw").

| # | Query or page | Rating | Notes |
|---|---|---|---|
| 1 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html | useful | Jupiter bulk, orbit, irradiance 50.26 W/m2 (WebFetch summary) |
| 2 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturnfact.html | useful | Saturn bulk and orbit |
| 3 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/galileanfact_table.html | useful | Galilean moons table (summary lists "mean temperature"; treat temperatures as low confidence until cross-checked) |
| 4 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/satusatfact.html | dead | 404, died at the URL guess, not at the sources |
| 5 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturniansatfact.html | useful | Titan and Enceladus bulk and orbit |
| 6 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/asteroidfact.html | useful | Total asteroid mass, Ceres/Pallas/Vesta masses |
| 7 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/titanfact.html | dead | 404, died at the URL guess |
| 8 | Query: asteroid belt total mass fraction of Moon mass Ceres Vesta Pallas Hygiea share of mass | useful | Led to arXiv:2603.17561 and the Lucy page |
| 9 | Page: https://arxiv.org/pdf/2603.17561 (raw, via local pdftotext) | useful | Menichella, Mar 2026 preprint; belt mass, Pitjeva and Pitjev 2018 |
| 10 | Page: https://en.wikipedia.org/wiki/Asteroid_belt | thin | Secondary; used only for leads (Kirkwood gaps, dust temperature range). First 100,000 characters read |
| 11 | Query: NASA science asteroid belt facts "mostly empty" distance between asteroids spacecraft | useful | Led to Lucy and Astronomy.com |
| 12 | Query: asteroid belt number density asteroids larger than 1 km 1 million NEOWISE Hubble size frequency distribution main belt | thin | Mostly NEO-focused results; gave 0.7 to 1.2 million range lead |
| 13 | Page: https://www.astronomy.com/science/how-do-spacecraft-avoid-collisions-in-the-asteroid-belt/ | thin | Secondary (planetarium staff, Dec 23, 2024); matches Lucy page |
| 14 | Page: https://lucy.swri.edu/MainBeltDensity.html via WebFetch | dead | TLS certificate error, died at the tool; recovered with curl -k (see 15) |
| 15 | Page: same URL, raw text via curl -k into the scratchpad | useful | Lucy mission team (SwRI), Jul 30, 2025. Mass, count, volume, spacing, "far less densely packed than films" |
| 16 | Query: Bottke Jedicke ... debiased main belt size distribution ... | dead | Died at the query: I put a remembered figure in it and results returned NEO papers; no figure from it is used |
| 17 | Query: DeMeo Carry 2013 "Solar System evolution from compositional mapping of the asteroid belt" C-complex S-complex mass fraction ... | useful | Found the Nature 2014 paper (arXiv:1408.2787); year correction 2014 not 2013 |
| 18 | Page: https://arxiv.org/pdf/1408.2787 (raw via pdftotext) | thin | Mass-weighted taxonomy by zone only in figures; text gives qualitative statements and the C-type inner-belt percentages; no single belt-wide C/S/M mass split |
| 19 | Query: M-type asteroid 16 Psyche density metal content ... | useful | Leads to NASA Psyche pages |
| 20 | Page: https://science.nasa.gov/solar-system/asteroids/16-psyche/ | thin | NASA: 30 to 60 percent metal by volume; rotation just over 4 hours; page has no density or gravity |
| 21 | Query: carbonaceous chondrite water content weight percent CI CM ... | useful | Led to Garenne et al. 2014 and Beck et al. 2021 |
| 22 | Page: https://www.isterre.fr/IMG/pdf/46_2014gca.pdf (raw) | useful | Garenne et al. 2014, GCA 137:93; CI about 20, CM about 9 wt% water (cited), TGA of 26 CMs |
| 23 | Page: https://arxiv.org/pdf/2011.00279 (raw) | useful | Beck et al. "Water abundance at the surface of C-complex main-belt asteroids": 4.5 wt% volume-average (Ceres excluded), uncertainty 4 wt% (90 percent) |
| 24 | Query: Lewis "Mining the Sky" OR Kargel metallic asteroids ... | thin | Mostly popular summaries; lead to How Many Ore-Bearing Asteroids (arXiv:1312.4450) not read |
| 25 | JPL SBDB API, physical parameters for asteroids 1, 2, 4, 10, 16, 243, 253, 433 (https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=N&phys-par=1), raw JSON | useful | Primary dataset: diameter, GM, density, rotation period, albedo, spectral type with source refs |
| 26 | Page: https://science.nasa.gov/dwarf-planets/ceres/facts/ | thin | NASA says Ceres is 25 percent of belt mass; conflicts with 39 percent (see Conflicts) |
| 27 | Query: asteroid rotation period spin barrier 2.2 hours rubble pile fast rotators distribution Pravec Harris | useful | Secondary summary of Pravec and Harris 2000; critical period 3.3 h / sqrt(density) |
| 28 | Query: Ceres Dawn gravity field Park 2016 Nature ... | thin | Confirms paper identity; numbers taken from JPL SBDB (row 25) instead |
| 29 | Pages: NSSDCA fact sheets for Sun, Mars, Earth | useful | Sun: luminosity 382.8e24 W; Earth irradiance 1361.0 W/m2; Mars 586.2 W/m2; Mars orbit; Earth orbital speed |
| 30 | Page: https://ssd.jpl.nasa.gov/astro_par.html | useful | GM of Sun, Earth, Moon, Mars system, Jupiter system, Saturn system; AU; c (DE440) |
| 31 | Query: Hohmann transfer Earth to Jupiter transfer time years delta-v ... | thin | Leads only; Wikipedia and a lecture table |
| 32 | Query: NASA JPL Basics of Space Flight interplanetary Hohmann ... | dead | Died at the sources: no JPL page returned; Earth-Mars 259 days from a secondary page, not used |
| 33 | Page: https://ocw.tudelft.nl/.../AE2104-Orbital-Mechanics-Slides_11_12.pdf | dead | Died at the tool: image-only PDF |
| 34 | Page: https://fti.neep.wisc.edu/.../lecture29.pdf (raw) | useful | Santarius, University of Wisconsin lecture, Apr 2, 2004; Hohmann table Earth to belt, Jupiter, Saturn; moon escape speeds |
| 35 | Query: Galilean moons surface radiation dose rate rem per day ... | thin | Secondary summaries only |
| 36 | Query: Juno radiation vault titanium total ionizing dose ... | thin | Popular and trade pages; 1 cm Ti, about 200 kg; leads only |
| 37 | Query: ntrs.nasa.gov Europa Clipper radiation environment total ionizing dose requirement ... (extended) | useful | Andersen et al. 2020, Space Weather: 150 krad(Si) design basis, 300 krad parts; Wiley page returned 403 (dead at the source) |
| 38 | Pages: Wiley 10.1029/2019SW002340; Springer 10.1007/s11214-025-01139-9; NTRS 20205004139 | dead | 403, login redirect, and an unrelated regulator test report respectively; died at the sources |
| 39 | Query: Cooper et al. 2001 Energetic ion and electron irradiation of the icy Galilean satellites ... | useful | Identifies Icarus 149:133; NTRS annual report 20000120581 read raw but yielded no dose figures (thin) |
| 40 | Page: https://lasp.colorado.edu/mop/files/2015/08/jupiter_ch20-1.pdf (raw) | useful | Johnson et al. chapter 20 in the Jupiter book (2004): Table 20.1 energy fluxes at each Galilean moon; 60 gigarad figure |
| 41 | Page: https://arxiv.org/pdf/1706.05356 | dead | Not relevant; no Europa dose in it (died at the query, a bad guess from a search snippet) |
| 42 | Query: Europa surface radiation dose rate Sv per day ... (extended) | useful | Secondary: 5.4 Sv/day (about 540 rem/day); leads to Paranicas 2007 and Nordheim 2019 |
| 43 | Query: Europa Lander Study 2016 Report radiation ... | useful | 2.3 Mrad or 540 rem/day, 150 krad(Si) vault requirement (secondary summary) |
| 44 | Pages: NTRS 20190027385 (raw); NTRS 20190029432 (image PDF); exordo ASEC 2017 abstract | thin | 8.5 mm Al vault, about 72 kg (abstract); the NTRS PDFs held no dose-rate figure |
| 45 | Query: Nordheim Hand Paranicas 2019 GCR bombardment of Europa's surface ... | thin | Identified paper; no numbers returned |
| 46 | Query: Juno radiation monitoring investigation total ionizing dose ... Becker 2017 (extended) | thin | Identified Becker et al. 2017 (Space Sci Rev 213:507); Springer and Wiley copies not retrievable (HTML wall, died at the sources) |
| 47 | Page: https://sci.esa.int/documents/33960/35865/1567260128466-JUICE_Red_Book_i1.0.pdf (raw) | useful | ESA JUICE Definition Study Report, Sep 2014: 50 krad per equipment, 46 W/m2 worst-case solar, Europa fluxes >20 times Ganymede, JOI about 900 m/s |
| 48 | Query: ESA JUICE radiation environment total ionising dose ... (extended) | useful | Led to EUCASS paper and ESA page |
| 49 | Page: https://www.eucass.eu/doi/EUCASS2022-7148.pdf (raw) | useful | Sarri, Witasse, Cavel 2022: 85 m2 array gives under 1 kW at Jupiter end of life, over 25 percent array degradation in 4 years, 50 krad, solar constant about 27 times lower than Earth |
| 50 | Page: https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Jupiter_s_radiation_belts_and_how_to_survive_them (06/04/2023) | thin | Qualitative: under 4 years at Jupiter equals 20 years of geostationary; lethal dose on Europa in hours |
| 51 | Query: Jupiter total ionizing dose rate versus orbital radius ... GIRE (extended) | useful | Led to arXiv white paper (Galileo 30 to 40 krad per crossing) |
| 52 | Page: https://arxiv.org/pdf/1908.02339 (raw) | useful | White paper for ESA Voyage 2050 (preprint, 2019): Galileo 30 to 40 krad per belt crossing behind 2.2 g/cm2 Al; electrons above 50 MeV in inner belts |
| 53 | Page: https://arxiv.org/pdf/2006.14682 (raw) | useful | Roussos and Kollmann (AGU book chapter preprint, 2020): Saturn versus Jupiter belts |
| 54 | Page: https://link.springer.com/article/10.1007/s10686-021-09801-0 | dead | Redirect to an authentication endpoint, not followed; same content found as the arXiv white paper (row 52) |
| 55 | Query: Fieseler ... radiation effects on Galileo spacecraft systems ... | thin | Identified IEEE Trans Nucl Sci 49:2739 (2002); paper itself not opened. Dose figure via the arXiv white paper |
| 56 | Query: Juno radiation dose Io torus ... krad ... Mrad ... (NASA domains) | thin | JPL article of Jun 16, 2016: vault reduces exposure about 800 times, 172 kg |
| 57 | Page: https://www.jpl.nasa.gov/news/nasas-juno-spacecraft-to-risk-jupiters-fireworks-for-science/ | useful | Jun 16, 2016: 800 times reduction, almost 400 lb vault, 37 close approaches, 20 months |
| 58 | Pages: IOPscience 10.3847/2041-8213/ab3661 (Nordheim et al. 2019) | thin | Summarized by WebFetch only; summary line "a few Gy per second at shallowest depths" looks implausible and is NOT used. GCR peak dose 6.3e-10 Gy/s at 0.92 m and a 14 GV cutoff recorded as low confidence |
| 59 | Pages: Wiley Paranicas 2007 GRL; Wiley Bagenal and Dols 2020; ResearchGate Paranicas 2009 chapter; ADS 2007GeoRL abstract; europa.nasa.gov Lander report PDF | dead | All died at the sources (403, 405, HTML wall, 404). The 5.4 Sv/day Europa surface dose therefore rests on secondary summaries only |
| 60 | Query: Europa Lander Study 2016 Report ... radiation (3 variants) | thin | Secondary: 540 rem/day (5.4 Sv/day), 150 krad(Si) lander electronics, 8.5 mm Al vault about 72 kg |
| 61 | Pages: NASA Science Europa facts, Juno ice-shell news, Ganymede facts, Callisto facts, Io facts; ESA JUICE Callisto page | useful | Moon figures (ice shell, ocean, orbit, temperature, Io torus mass loading) |
| 62 | NASA Science URLs under /jupiter/moons/<name>/facts/ and /jupiter-moons/<name>/<name>-facts/ | dead | Several 404s; died at the URL guess. Correct pattern is /jupiter/jupiter-moons/<name>/facts/ |
| 63 | Query: Io heat flow tidal heating Juno ... | thin | Secondary news: 1 to 3 W/m2 background heat flow, about 100 TW; primary Nature paper (Park et al. 2024) not opened |
| 64 | Page: https://eos.org/research-spotlights/two-moons-and-a-magnetosphere | thin | AGU Eos research spotlight on Bagenal and Dols 2020: about 1 ton/s ionized |
| 65 | Query: HOPE Callisto surface base ... Troutman | useful | Led to the NASA Langley HOPE slides |
| 66 | Page: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20030063128.pdf (and the api path) | dead | Died at the tool (HTML / 404). Same slides read via a mirror (row 67) |
| 67 | Page: https://eltamiz.com/files/HOPE.pdf (raw) | useful | Troutman and Bethke, NASA Langley, Feb 3, 2003 (STAIF-2003); mirror of the NTRS item, not the NTRS copy itself |
| 68 | Query: Iess 2019 Science ... ring mass | useful | Found paper and open copies |
| 69 | Page: https://www.weizmann.ac.il/.../Iess-etal-2019.pdf (raw) | useful | Ring mass (1.54 +/- 0.49) e19 kg, 0.41 Mimas mass, 10^7 to 10^8 yr age. (The first PDS-atmospheres copy of the paper failed to download: dead at the file path) |
| 70 | Page: https://arxiv.org/pdf/0912.3017 (raw) | useful | Charnoz et al. chapter 17, Saturn After Cassini-Huygens (2009 preprint): rings mainly pure water ice, little contamination |
| 71 | Page: https://science.nasa.gov/mission/cassini/science/rings/ | useful | Rings about 10 m thick; lowest recorded A-ring temperature -230 C; particle sizes micron to mountain-size |
| 72 | Query: Cuzzi 2010 "An evolving view of Saturn's dynamic rings" ... 95% | thin | Paper identified; the 95 percent figure did NOT appear and is not used. Died at the sources (paywall) |
| 73 | Query: Titan surface pressure 1.5 bar ... | useful | Led to arXiv reviews |
| 74 | Pages: arXiv 1702.08611 (Horst 2017, raw); arXiv 2410.04595 (Zhang 2024, raw) | useful | Titan: 94 K, about 1.5 bar, 95 percent N2, gravity 1.35 m/s2, winds under 1 m/s at surface |
| 75 | Query: Titan surface radiation dose GCR atmosphere shielding ... Gronoff | thin | Qualitative: atmosphere stops trapped particles, GCR is the dominant source at the surface; Gronoff et al. 2011 not opened. Column mass derived myself (see Derived figures) |
| 76 | Query: Enceladus plume mass flux kg/s ... | thin | About 200 kg/s (UVIS summary, secondary); jets over 1000 m/s; primary Hansen et al. not opened |
| 77 | Query: Enceladus south polar heat output ... Howett; Thomas 2016; Waite 2017 | useful | 15.8 GW (JPL 2011, fetched); ocean about 45 km, ice shell about 20 km (secondary, from the Thomas 2016 abstract) |
| 78 | Pages: JPL "Cassini finds Enceladus is a powerhouse"; NASA 2015 global-ocean release; NTRS Nixon chapter 6 (image PDF) | thin | 15.8 GW confirmed on the JPL page; the NASA release gave no ocean numbers; chapter unreadable by WebFetch |
| 79 | Query: Zeitlin 2013 ... MSL RAD in transit to Mars | useful | 1.8 mSv/day GCR dose equivalent in cruise; SwRI release fetched (2013-05-30) |
| 80 | Page: https://www.nasa.gov/wp-content/uploads/2023/03/radiation-protection-technical-brief-ochmo.pdf (raw) | useful | NASA-STD-3001 Rev B: 600 mSv career, 250 mSv per SPE, shelter shielding; Rev E Dec 27, 2022 |
| 81 | Query: galactic cosmic ray radial gradient heliosphere ... (extended) | thin | About 3 percent/AU (protons, inner heliosphere) and 1.5 to 2.5 percent/AU at high energy (Pioneer 10 abstracts, secondary summaries); not opened in full |
| 82 | Query: NASA nuclear thermal propulsion specific impulse ... NERVA ... | useful | Led to NTRS 20190033337 |
| 83 | Page: https://ntrs.nasa.gov/api/citations/20190033337/downloads/20190033337.pdf (raw) | useful | NASA MSFC overview slides (Wilkerson, 2019): NERVA 825 to 875 s; NTP 25 to 250 klbf, 800 to 1000 s; ion NEP 2000 to 8000 s |
| 84 | Page: NEXT-C fact sheet (www1.grc.nasa.gov) (raw) | useful | NEXT: 25 to 235 mN, 4220 s max, 0.6 to 7.4 kW |
| 85 | Query: Dawn spacecraft NSTAR ... | useful | NSTAR 19 to 92 mN, 1900 to 3100 s at 0.5 to 2.3 kW; Dawn about 11 km/s delta-v, 425 kg xenon, array over 10 kW (JPL/NASA press and NTRS titles; the Dawn press kit itself not opened) |
| 86 | Queries: Kilopower KRUSTY ...; MMRTG ... | useful | KRUSTY 1.5 to 5 kWt, 28 hours; MMRTG about 110 We, 2000 Wt, 45 kg, 6 percent BOL efficiency (search summaries of NASA fact sheets) |
| 87 | Page: https://ntrs.nasa.gov/api/citations/20200001569/downloads/20200001569.pdf (raw) | thin | Kilopower higher-power paper; no usable mass or radiator figures found |
| 88 | Page: https://ntrs.nasa.gov/api/citations/20220004670/downloads/40%20kW%20Deployable%20FSP%20Paper_FINAL.pdf (raw) | useful | Oleson et al., NASA GRC: 40 kWe lunar fission surface power, 10,046 kg with margin, 18.1 percent efficiency, 126.4 kW waste heat, 133.4 m2 radiator at 395 K |
| 89 | Page: https://ntrs.nasa.gov/api/citations/20190031807/downloads/20190031807.pdf (raw) | useful | NIAC Phase II Final Report, Thomas, Paluszek, Cohen, May 2019: Direct Fusion Drive 1 MW and 10 MW point designs, mission table |
| 90 | Queries: solar sail NEA Scout ...; VASIMR VX-200 ... | useful | NEA Scout 86 m2 sail; VX-200: 200 kW, 5000 s, 5.7 N, 72 percent |
| 91 | Pages: https://ntrs.nasa.gov/api/citations/20170001499/downloads/20170001499.pdf (raw); https://www.adastrarocket.com/technical-papers-archives/Gar_AIAA-2011.pdf (raw) | useful | NEA Scout 86 m2 confirmed; Bering et al. AIAA-2011-1071 confirmed 5.7 N, 5000 s, 72 percent (a company-affiliated paper: treat as vendor-adjacent) |
| 92 | Queries: Lubin "A Roadmap to Interstellar Flight" ...; Project Daedalus final report ... | useful | Lubin found; Daedalus found only through secondary pages |
| 93 | Page: https://arxiv.org/pdf/1604.01356 (raw) | useful | Lubin, v8 dated Jan 21, 2022: Voyager 1 17 km/s, kinetic energy formula, 0.3c about 1 Mt TNT/kg, DE-STAR 4 50 to 70 GW |
| 94 | Page: https://en.wikipedia.org/wiki/Project_Daedalus | thin | Secondary only; gave 0.12c, 50 years, 54,000 t. No link to the original JBIS 1978 report; not opened |
| 95 | Query: Bond Martin "Project Daedalus" Final Report ... pdf full text (extended) | dead | Died at the sources: the 1978 report is not online in an openable form (ADS record and CD-ROM only) |
| 96 | Page: https://arxiv.org/pdf/1307.2424 (raw) | useful | DeMeo and Carry 2013 (Icarus 226): Table 5 mass by taxonomic class, Table 6 zones |
| 97 | Page: https://arxiv.org/pdf/1109.4096 (raw) | thin | Masiero et al. 2011 NEOWISE main belt (preprint): size-frequency slopes -2.5 observed, -3.5 theoretical; kink at 15 to 25 km. Number of objects over 1 km not found here |
| 98 | Pages: https://arxiv.org/pdf/2303.05099 (raw); https://arxiv.org/pdf/1903.11876 (raw) | useful | Rotation: most periods 2.2 to 20 h; about 1,600 of 32,249 below 2.2 h (as of 2022); critical period about 2.1 h at 2.5 g/cm3 |
| 99 | Page: https://arxiv.org/abs/1908.01868 | dead | Wrong arXiv id guessed by me (it is an unrelated paper); died at the query, not at the sources |
| 100 | Page: PDS targIO.PLASMA.TORUS.cat | useful | Io torus zones in Jupiter radii, composition, density over 3000 per cm3, about 1 eV inner torus (PDS catalog text via WebFetch) |
| 101 | Query: Cassini Saturn orbit insertion burn delta-v 626 m/s ... | useful | SOI 626 m/s, 96 minutes; VVEJGA, about 6.7 years |
| 102 | Pages: DESCANSO Cassini navigation (raw), NASA Cassini fact sheet (raw) | useful | SOI delta-v 626 m/s in a JPL DESCANSO article; cruise nearly seven years |
| 103 | Pages: NIST CODATA 2022 values for c, sigma, G, standard gravity, eV to J | useful | Exact or defined constants used in derived figures |
| 104 | Query: Juno solar arrays 60 m2 18,698 cells 14 kW at Earth 500 W at Jupiter ... | useful | JPL, Jan 13, 2016: more than 60 m2, about 14 kW at Earth distance, 500 W at Jupiter |
| 105 | Page: https://www.jpl.nasa.gov/news/nasas-juno-spacecraft-breaks-solar-power-distance-record/ | useful | 793 million km from the Sun at record; maximum 832 million km; 500 W; 25 times less |
| 106 | Query: Cassini three RTGs 633 watts ... ; page: NASA Cassini RTG page | thin | Page lists RTG count and RHUs only. The 882 W beginning-of-mission figure is from a search summary of a NASA page and is medium confidence |
| 107 | Query: Callisto surface radiation dose 0.01 rem per day ... (extended) | thin | Same secondary 0.01 rem per day figure; no primary reached |
| 108 | Query: solar energetic particle radial dependence ... (extended) | useful | Peak-flux exponent between -3.7 and -2, fluence between -2.7 and -1.4 (Cao et al. 2025 via the ESA Solar Orbiter nugget), but all data inside 1 AU |
| 109 | Page: https://www.cosmos.esa.int/web/solar-orbiter/-/science-nugget-radial-dependence-of-solar-energetic-particle-peak-fluxes-and-fluences | useful | Confirms the exponents and the 0.05 to 1.01 AU data range |
| 110 | Local computation (Python, scratchpad) of Hohmann transfers, irradiance, delays, gravity, rocket equation, radiators | useful | Inputs only from rows above; results in section 5 |
