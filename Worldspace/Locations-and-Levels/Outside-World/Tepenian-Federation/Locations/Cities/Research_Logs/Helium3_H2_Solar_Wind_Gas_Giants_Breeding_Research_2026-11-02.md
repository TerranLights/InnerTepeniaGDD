# Helium-3 off the Moon: solar wind, gas giants, breeding, the inner system (Unit H2, 2026-11-02)

**Scope.** Research unit H2 of the fusion and helium-3 round (brief: `Fusion_and_Helium3_Research_BRIEF_2026-11-02.md`). It covers six questions: (1) solar-wind helium-3 content, flux, scaling toward the Sun, collection concepts and separation; (2) gas-giant atmospheric mining (the Palaszewski papers and critiques); (3) breeding helium-3 from D-D reactions, tritium decay and fission reactors; (4) any helium-3 link to Mercury, Venus and the inner system; (5) asteroids and comets; (6) the demand side against the supply figures. **Facts only: no recommendation, no design, no ranking.** Labels: **SOURCED** (read at the source in this session, including a PDF read as text on disk), **DERIVED** (my arithmetic on sourced figures, working shown), **UNVERIFIED** (seen only in a search snippet, a secondary page, or inferred), **NOT FOUND** (queries listed in the log). The setting's national figure used for the demand arithmetic is the discussion file's 101.7 GW electric and the Tower's 324 GW net; these are setting figures, not sourced facts.

**Started:** 2026-11-02, about 18:50 (local, MST). **Finished:** 2026-11-02, about 19:15. Web calls used: about 85 (the brief allows about 60 to 80; the overrun went to reading primary PDFs that the fetch tool first returned as binary, which I then read with `pdftotext` in the scratch folder).

## PROGRESS
- [x] Q1 Solar wind: He-3 ratio, flux, scaling, capture area, separation
- [x] Q1 check of the discussion file's 39-54 g/t and 67,000-93,000 km² figures
- [x] Q1 published collection concepts: searched from four angles; **no peer-reviewed engineering concept found** (NOT FOUND, see Q1.6)
- [x] Q2 Gas-giant mining: Palaszewski papers read (2012, 2020, 2024); Daedalus and Icarus read at secondary level; critiques
- [x] Q3 Breeding: D-D, tritium decay, fission and heavy-water reactors (heavy-water yield is UNVERIFIED)
- [x] Q4 Mercury, Venus, inner system
- [x] Q5 Asteroids and comets: **numeric He-3 content NOT FOUND**; qualitative and interplanetary-dust data found
- [x] Q6 Demand side with working
- [x] FINAL section
- [x] Search log

---

## Q1 · Solar wind

### 1.1 The He-3 / He-4 ratio (SOURCED unless marked)
| Value | Source | Status |
|---|---|---|
| **(4.64 ± 0.09) × 10⁻⁴** bulk solar wind, measured in the Genesis diamond-like-carbon-on-silicon target | Heber, Wieler, Baur, Olinger, Friedmann, Burnett, *Geochimica et Cosmochimica Acta* 73(24), 7414-7432, 15 Dec 2009 (Caltech repository record read). The record states the 3He/4He and 4He/20Ne values "are the highest solar wind values measured in exposed natural and artificial targets" | SOURCED (abstract page) |
| **2310 ± 50** average flux ratio of He-4 to He-3 (ISEE-3); "agrees well with Apollo foil measurements"; probably correlated with solar activity | Coplan, Ogilvie, Bochsler, Geiss, 1 Nov 1983, in *Solar Wind Five*, NTRS 19840005043 (page read; the page does not state the direction of the ratio, but 2310 cannot be a 3He/4He value) | SOURCED (abstract page) |
| (4.4 ± 0.4) × 10⁻⁴ (first SWICS/Ulysses result, Bodmer et al. 1995) | search snippet | UNVERIFIED |
| Gloeckler and Geiss 1998 (*Space Science Reviews* 84, 275): fast wind (3.3 ± 0.3) × 10⁻⁴; weighted average (4.08 ± 0.25) × 10⁻⁴ "consistent with the Apollo results"; extrapolated photosphere (3.75 ± 0.27) × 10⁻⁴; local interstellar cloud (2.48 +0.68/-0.62) × 10⁻⁴ | search snippets of the abstract. The abstract page (ADS) returned HTTP 405 and the Springer and Michigan copies redirected or returned 403 | UNVERIFIED |
| Apollo foil (SWC): weighted-average 4He/3He 2350 ± 120; helium flux time-weighted average 1.2 × 10⁷ cm⁻² s⁻¹ | search snippet quoting the Apollo literature; the Apollo 16 report chapter (NTRS 19730013019, Geiss et al., 1972) was read and gives no values | UNVERIFIED |

**Reading.** The ratio is a few × 10⁻⁴ and differs between fast and slow wind and between instruments (3.3 to 4.64 × 10⁻⁴ in the values above). Genesis is the most recent and the one the authors call highest. The fast-versus-slow difference matters for a collector at a given distance: it is the same order as the spread in the helium abundance (below).

### 1.2 Helium abundance, proton density and speed (1 AU and inner)
- **Helium-to-proton number ratio A_He at 1 AU:** Kasper et al. (2007, Wind data 1995-2005) found A_He a "remarkably linear" function of speed that goes to zero at 259 ± 12 km/s, with solar-cycle variation (snippet of the abstract: UNVERIFIED). A later analysis gives a stable 4 to 5% above 426 km/s (arXiv 1906.12273, snippet: UNVERIFIED). Johnson et al. 2025 (*ApJ*, Parker Solar Probe Solar Probe Cup, encounters 1-14; arXiv 2502.19492 read) quote **typical solar-wind A_He of 1 to 5%**, solar-minimum slow wind 1.56% and fast wind 2.86% (Song et al. 2022, as quoted there), photosphere 8.4%; their catalogued helium-rich periods (mean 8.34%, 87% tied to coronal mass ejections) were at 42.8 to 168 solar radii. **SOURCED (that paper).**
- **Proton density and speed at 1 AU:** a model paper uses a time-averaged 5.94 cm⁻³ at 432.4 km/s from OMNI data (arXiv 1509.08685); another uses 7.39 cm⁻³ (IMP-8; astro-ph/0308210). Both are snippet-level (UNVERIFIED). **DERIVED:** proton flux = 5.94 × 4.324 × 10⁷ = 2.6 × 10⁸ cm⁻² s⁻¹; with A_He = 4% the helium flux is 1.0 × 10⁷ cm⁻² s⁻¹.
- **Measured helium flux, 1 AU:** Apollo foil 1.2 × 10⁷ cm⁻² s⁻¹ (snippet, UNVERIFIED); a secondary page on the Genesis data gives 9.72 × 10⁶ (and a ratio of 4.62 × 10⁻⁴) over about 887 days (UNVERIFIED); Becker et al. 2012 from Genesis gold collectors 4He = 1.14 ± 0.04 × 10⁷ cm⁻² s⁻¹ (snippet, UNVERIFIED). The three agree within about 20%.

### 1.3 Helium-3 per tonne of wind (check of the discussion file's "39-54 g per tonne")
**DERIVED.** Wind mass per proton = 1.007 + 4.003 × A_He (atomic mass units); He-3 mass per tonne = A_He × (3He/4He) × 3.016 ÷ that mass.

| A_He | 3He/4He | He-3 per tonne of wind |
|---|---|---|
| 1.56% (slow, solar minimum) | 4.64 × 10⁻⁴ | 20 g |
| 2.86% (fast, solar minimum) | 3.3 × 10⁻⁴ | 25 g |
| 2.86% | 4.64 × 10⁻⁴ | 36 g |
| 4% | 4.08 × 10⁻⁴ | 42 g |
| 4% | 4.64 × 10⁻⁴ | 48 g |
| 5% | 4.64 × 10⁻⁴ | 58 g |

**Result:** the discussion file's 39-54 g/t lies inside the 20-58 g/t range, at the upper half. It corresponds to A_He of about 3.5 to 4.5% with the Genesis-era ratio. The low-end values (slow wind at solar minimum, A_He under 2%) are about half to two-fifths of it. Another sourced cross-check: an Olson (NASA, 2021) paper states "Helium-3 nuclei make up approximately 0.002% of the solar wind" (its ref. 7); **DERIVED** here: 0.04 × 4.64 × 10⁻⁴ = 1.9 × 10⁻⁵ = 0.0019% by number. Consistent.

### 1.4 Flux per area and capture area (check of "67,000-93,000 km² at 0.1 AU; 6.7-9.3 million km² at 1 AU for 54 kg/yr")
**DERIVED.** He-3 flux = helium flux × 4.64 × 10⁻⁴; mass = atoms × 3.016 × 1.6605 × 10⁻²⁴ g; 1 km² = 10¹⁰ cm²; 1 year = 3.156 × 10⁷ s. Assumes **100% capture of every He-3 ion crossing the collector plane** (an upper bound).

| Helium flux at 1 AU | He-3 flux (cm⁻² s⁻¹) | He-3 per km² per year | Area for 54 kg/yr at 1 AU | at 0.3 AU | at 0.1 AU |
|---|---|---|---|---|---|
| 9.72 × 10⁶ (Genesis, secondary) | 4,510 | 7.1 mg | 7.6 million km² | 0.68 million | 76,000 km² |
| 1.0 × 10⁷ (OMNI mean, 4%) | 4,770 | 7.5 mg | 7.2 million | 0.65 million | 72,000 |
| 1.14 × 10⁷ (Becker) | 5,290 | 8.4 mg | 6.5 million | 0.58 million | 65,000 |
| 1.2 × 10⁷ (Apollo) | 5,570 | 8.8 mg | 6.1 million | 0.55 million | 61,000 |

(The inner columns use inverse-square scaling of flux with distance from the Sun.) **Result:** the discussion file's 6.7-9.3 million km² at 1 AU and 67,000-93,000 km² at 0.1 AU are reproduced in order of magnitude and are within about 25% of this table at the upper end (the file's 93,000 would need a He-3 flux about a fifth lower than the lowest value here, which a slow-wind or low-A_He case supplies). 54 kg a year at 1 AU needs a capture plane of roughly 6 to 8 million km², a square about 2,500 to 2,800 km on a side (DERIVED). At 0.1 AU the same plane is about 60,000 to 76,000 km², a square about 250 to 280 km on a side (DERIVED).

### 1.5 Scaling toward the Sun
- **Continuity gives r⁻² for the flux** if the wind speed is constant and radial (DERIVED; the figures above). It is a first approximation; the speed is not constant inside about 0.3 AU.
- **Sourced model inside 0.16 AU:** Venzmer and Bothmer (*A&A* 611, A36, 2018; arXiv 1711.07534 abstract read) predict, for the Parker Solar Probe orbit, a proton density of about **214 cm⁻³ and 340 km/s at 0.16 AU** and **2,951 cm⁻³ and 290 km/s at 0.046 AU**. These are **model predictions**, not measurements. **DERIVED:** proton flux 7.3 × 10⁹ cm⁻² s⁻¹ at 0.16 AU and 8.6 × 10¹⁰ at 0.046 AU; the flux falls as r^-1.98 between those two points. At 0.16 AU the model flux is about 62% of the pure r⁻² extrapolation from 1 AU (1.17 × 10¹⁰); applying the model's exponent from 0.16 AU gives about **1.8 × 10¹⁰ cm⁻² s⁻¹ at 0.1 AU against 3.0 × 10¹⁰ for pure r⁻²** (DERIVED, an interpolation). The capture areas at 0.1 AU would then be about 1.6 times larger than in the table: roughly 100,000 to 125,000 km².
- **Helium content near the Sun:** the Parker Solar Probe data (Johnson et al. 2025) say the composition varies strongly there, with no theory that fully explains the range (quoted in the paper's abstract as summarized by the search tool: UNVERIFIED for that phrase; the 8.34% mean and 1-5% "typical" were read in the paper). I did not find a measured **He-3/He-4 ratio** inside 0.3 AU: **NOT FOUND**.
- **Wind speed and ion energy:** a He ion at 400 km/s carries about 3.3 keV (DERIVED: 0.5 × 4 amu × v²).
- **Mercury as a checkpoint:** a Mercury-orbit paper (Weichbold et al. 2025, read) puts the typical proton number flux near Mercury at about 1 × 10⁹ cm⁻² s⁻¹ at 400 km/s (their ref. Sun et al. 2021). The pure r⁻² scaling from 2.6-3 × 10⁸ at 1 AU would give 1.7-2.0 × 10⁹ at 0.387 AU, so the two differ by a factor of about 2 (DERIVED).
- **Thermal limit at the collector (UNVERIFIED, search snippets only):** NASA describes the Parker Solar Probe heat shield as reaching nearly 2,500 °F at closest approach (design figure) while the instruments stay near 85 °F; a later NASA update says there is no front-facing sensor and models suggest about 1,700 °F. The probe's closest approach is about 3.8 million miles (6.1 million km), roughly 0.04 AU. An attempt to read the mission page failed (socket hang up). No published thermal analysis of a **kilometer-scale** collector was found.

### 1.6 Published collection concepts (searched from four angles)
- **Peer-reviewed engineering concept for scooping He-3 from the solar wind with a spacecraft: NOT FOUND** (queries 17, 18, 22, 23, 83 in the log). What exists:
  - **Genesis** (NASA, collected solar wind at the Sun-Earth L1 point, about 850 to 887 days of exposure; collectors were wafers; each pan about 73 cm across, 3,500 cm², per an EO Portal page; the Heber paper says solar-wind noble gases were "quantitatively retained" in the diamond-like-carbon target, abstract page read). It shows **passive collection of solar-wind helium by implantation is real**, but it is a sample-return science mission, not a fuel concept, and I found no He-3 mass yield for it.
  - **A preprint** titled "Comparative Analysis of Helium-3 Extraction Methods: Solar Wind Harvesting versus Lunar Regolith Mining" (ResearchGate; the page returned 403, so **not read**). The search snippet reports a magnetic-lens collector with a collection area of 1.96 × 10¹¹ km², 18.9 kg of He-3 per hour (about 166 t per year), a 3.6-year payback versus more than 15 years for lunar mining, and a placement at the "Mars L1" point (which the search tool flagged as an error). **UNVERIFIED.** **DERIVED check:** 166 t/yr over 1.96 × 10¹¹ km² implies 0.85 mg of He-3 per km² per year, about one-ninth of the 1-AU flux value in §1.4; the area is about 380 times the surface of the Earth. I do not rely on it.
  - A joke-style idea page (Halfbakery "Mine the Sun") and forum threads: not sources.
  - Bussard ram-scoop papers were named in a snippet but are interstellar-propulsion concepts, not read.
- **Why the Moon is called a natural collector (SOURCED, secondary):** Olson (NASA, 2021, read) states the lunar regolith holds He-3 from "over 4 billion years of bombardment from the solar wind." Wisconsin estimates at least a million tonnes in the top 3 m; Apollo 11 sample 10084 averaged 11.8 ppb 3He (range 9.22-17.9). That is the lunar side (unit H1).

### 1.7 Separating He-3 from He-4 (SOURCED from Wittenberg 1993, read; details of terrestrial case)
Wittenberg, *Non-Lunar 3He Resources*, UWFDM-967 (presented 19-21 July 1993, revised July 1994, University of Wisconsin Fusion Technology Institute; full PDF read as text):
- The isotopic separation modeled is a **"superfluid/superleak" stage** that enriches He-3 from 2 × 10⁻⁷ to 10⁻² of the He-4, then **cryogenic distillation** (boiler 2.4 K, condenser 1.6 K, after Wilkes) to **99.9%**.
- Energy: superleak 1.1 × 10³ kWh/kg(³He) of heat; distillation boiler 3 × 10⁴ kWh/kg(³He); "because these separation energies would be rejected at nearly 300 K, each of the latter two values were multiplied by a factor of 10³." The isotopic separation energy for the terrestrial natural-gas case is 3 × 10⁷ kWh/kg(³He), against a D-³He fusion yield of 1.7 × 10⁸ kWh/kg(³He). **For the terrestrial reservoirs the total energy to obtain the He-3 (mostly the cost of extracting helium from methane or air) exceeds the fusion yield** (natural gas 1.23 × 10⁹ kWh/kg; subduction-zone gas about 10⁹; air 9 × 10¹⁰; "Negative" payback in his Table 2).
- The same paper cites Wilkes and Wittenberg (1992), "Isotopic Separation of ³He/⁴He from Solar Wind Gas Evolved from the Lunar Regolith" (SPACE '92), **not read**.
- Search snippets (UNVERIFIED): superleak enrichment about fivefold per pass; heat flush limited to a few percent He-3; cryogenic distillation the usual final step (a 2019 Cernavoda study reports 99.1% distillate purity); patents say commercial-scale distillation of natural helium was impractical. **A separation study starting from a solar-wind-ratio feed (about 4 × 10⁻⁴ He-3 in He-4) was NOT FOUND**; the figures above start at 2 × 10⁻⁷, about 2,000 times more dilute.

---

## Q2 · Gas-giant mining

### 2.1 What the Palaszewski papers say (SOURCED; three papers read as full text)
All by Bryan Palaszewski, NASA Glenn Research Center, "Atmospheric Mining in the Outer Solar System" series (the project acronym is AMOSS). Papers read:
1. **"Resource Capturing, Storage, and Utilization"**, AIAA/ASME/SAE/ASEE Joint Propulsion Conference, Atlanta, 29 July to 1 August 2012 (NTRS 20150006664; date from the NTRS record).
2. **"Aerospacecraft Analysis, Propulsion, and Resource Capturing Implications"**, AIAA Propulsion and Energy Forum (virtual), 24-28 August 2020 (NTRS 20205004479).
3. **"Interplanetary Transfer Vehicles, In-Situ Resource Utilization, and Moon Mining Issues"**, AIAA ASCEND, Las Vegas, 30 July to 1 August 2024 (NTRS 20240007489; record dated acquired 11 June 2024).
Also seen as abstract pages only: 2017 (NTRS 20170008828, AIAA, 10 July 2017) and 2019 (NTRS 20190029288, 19-22 August 2019).

**Inputs (the 2012 paper's Table I, read from the page image):** 3He in 4He = **1.00 × 10⁻⁴** for both planets; 4He in the atmosphere **0.152 (Uranus)** and **0.19 (Neptune)**; so 3He in the atmosphere **1.52 × 10⁻⁵ (Uranus) and 1.90 × 10⁻⁵ (Neptune)**.
- **DERIVED check:** the paper's capture times reproduce these as **mass-style fractions**: 500 kg ÷ (4 kg/s × 95.2 d × 86,400) = 1.52 × 10⁻⁵; 500 kg ÷ (22 kg/s × 13.8 d) = 1.9 × 10⁻⁵; 50 t ÷ (30 kg/s × 1,270 d) = 1.52 × 10⁻⁵ (2020 paper). The tables are mole fractions (He 0.152 times an assumed isotope ratio) but are used as mass fractions with 100% recovery assumed; a mass-fraction correction for 3 amu in a roughly 2.3 amu gas would raise the value by about 30%, in the optimistic direction (DERIVED, my arithmetic; not stated in the papers).
- **The He-3 ratio is an assumption, not a measurement:** Cavalié et al. 2020 (*Space Science Reviews*, arXiv 2004.13987, read as text) state that isotopic measurements in the ice giants "have not yet" been made. Jupiter's measured value is **3He/4He = (1.66 ± 0.05) × 10⁻⁴** (Mahaffy, Donahue, Atreya, Owen, Niemann, *Space Science Reviews* 84, 1998, abstract read), which the authors note is higher than meteoritic gases ((1.5 ± 0.3) × 10⁻⁴). Using 1.66 × 10⁻⁴ for Uranus would give 2.5 × 10⁻⁵ (DERIVED). **No measured 3He/4He for Uranus or Neptune: NOT FOUND.**
- **The helium abundance values are the early Voyager ones:** Cavalié et al. report Uranus He mole fraction 0.152 ± 0.033 (Conrath et al. 1987) and Neptune 0.190 ± 0.032 (Conrath et al. 1991), then revised for nitrogen to about **0.15 for Neptune** (Conrath et al. 1993; ISO 0.149 +0.017/-0.022, Burgdorf et al. 2003). **DERIVED:** with the revised Neptune value and the paper's own 10⁻⁴ ratio, Neptune's He-3 fraction would be 1.5 × 10⁻⁵, not 1.9. A re-analysis with higher methane (Uranus) and nitrogen (Neptune) lowers helium further ("slightly subsolar", He/H about 0.089 and 0.090, error bars large).

**Vehicle and throughput numbers (SOURCED):**
- A 500-kg payload of 3He per trip. Capture rate vs time: 4 kg/s of atmosphere gives 500 kg in 95.2 days (2012); 10 kg/s in 38.1 days; Neptune at 22 kg/s in 13.8 days with a 1,000-t dry-mass vehicle. 2020 paper: 30 kg/s gives 50 t of He-3 in 1,270 days, 120 kg/s in 317 days.
- **Hydrogen and helium-4 by-products:** at 4 kg/s capture, 293,000 kg of hydrogen produced per day; helium-4 about 15-19% of the hydrogen mass (2012).
- **Vehicle:** "aerospacecraft" (ASC) with a closed-cycle gas-core nuclear rocket, Isp 1,800 or 2,500 s, delta-V 20 to 20.5 km/s (flight from the cloud-top altitude to orbit and back); gas-core engines cut vehicle mass 72 to 80% relative to solid-core nuclear thermal rockets (2012). The gas-core engine is a concept never built.
- **Orbit transfer:** a nuclear-electric transfer vehicle of **10 MWe**, alpha 10 to 40 kg/kWe, Isp 5,000 s; Uranus-moon Miranda round trip 229 days at 10 kg/kWe (569 days at 40 kg/kWe); a 200-t lander payload (2020, 2024). Space bases with artificial gravity of 143 to 461 t (2024).
- **Mass of the whole mining architecture:** earlier (Ref. 1 of the 2020 paper): 5,000 t of "He-3 and D" delivered to refuel a nuclear pulse propulsion vehicle, 10,000 ASC flights at 0.5 t of fuel each, **100 ASCs, 118,000-123,000 t** of vehicles over a 10-, 20- or 30-year program (about 12,000 t per year delivered to Uranus for 10 years, 4,000 t per year for 30). Revised (2020, 2024): an ASC carrying 100 t (50 t of it He-3) cuts the architecture to about **22,000 t** (112,000 to 22,000 in 2024); delivery to Uranus or Neptune from Earth with a 200-t launch vehicle takes **nearly 120 launches per year over 10 years or under 30 per year over 40 years** (2024); interplanetary transfer vehicle 2,000 t initial mass delivering 200 t.
- **The "5,000 t" is a combined helium-3 and deuterium fuel load for a propulsion vehicle, not a power-plant fleet.** The papers do not give a He-3 mass per year for electricity supply.
- **Status:** all of this is **paper analysis**; the papers say the key components (gas-core rocket, nuclear-electric vehicle at 10 kg/kWe or better, cryogenic storage at Uranus) are future technologies. No test of any kind exists. Palaszewski himself flags the "complexity of a fissioning plasma gas core rocket" and the haze-layer flight issue as open (2012).

### 2.2 Earlier and parallel studies
- **Project Daedalus** (British Interplanetary Society, 1973-1978; search snippets and Centauri Dreams, read): mine **Jupiter's atmosphere** with 128 factories on fusion-powered balloons over 20 years for about 30,000 t of He-3 (one source: 50,000 t of D-³He propellant in a 54,000-t vehicle). Palaszewski (2012) cites it as the origin and moves the site to Uranus and Neptune.
- **Project Icarus** (Tau Zero Foundation and BIS), as reported by Paul Gilster (*Centauri Dreams*, 28 September 2010; page read) and a Discovery/NBC article (31 May 2011; read): the Icarus fuel team (Adam Crowl, Andreas Hein, Andreas Tziolas) **ruled out Jupiter** (radiation belts) and **Saturn** (radiation; high escape velocity) and chose **Uranus** (double-walled hot-air balloons, single-stage nuclear thermal rocket to return, or tethers). Hein's estimate: a Daedalus-scale probe needs **about 1,500 t of He-3 per year** (15 t/yr if payload mass is cut 100-fold). **Hein's cost threshold:** He-3 must cost **no more than roughly $1 to $10 billion per tonne** to compete with D-T fusion; the article says Hein's own numbers **exceed** it. Stage-two freighter (500 t empty, 114 t fuel out, 70 days to Uranus; return 614 t with 254 t of fuel; 500 t of cargo). Crowl (as reported): about **14,000 t of D-³He mix a year** would supply world energy demand by 2100 at 2.5% annual growth. The Hein and Long paper itself (IAC-10.D4.2.6) is access-restricted: **not read**.
- **Gas-giant He-3 abundance (SOURCED):** Jupiter: Mahaffy et al. 1998, 3He/4He (1.66 ± 0.05) × 10⁻⁴, He/H = 7.85 × 10⁻² (Cavalié et al.). The discussion file's "Jupiter 23 g/t" is not re-derived here (not checked).

### 2.3 Critiques and reservations found
- **Gilster (2010, same page):** a civilization needing this much He-3 "would take centuries to develop" given energy-growth estimates; D-³He has not been demonstrated; Hein's cost numbers exceed the competitive threshold. He suggests strategic uses (planetary defense) might change the cost picture.
- **Bob Parkinson (Icarus consultant), as quoted in the 2011 Discovery article:** extracting He-3 from the Moon "might take more energy … than would be produced by fusing the helium-3 liberated" (a statement about the Moon, not Uranus).
- **Wittenberg (1993)** (SOURCED, read): "the gas-giant planets, Jupiter and Saturn, probably contain millions of tonnes of 3He, but the utilization of such reservoirs may require centuries to develop."
- **Kevin Cannon, "Steelmanning Helium-3," *Planetary Intelligence* (Substack, 6 December 2022; read):** says there are "much richer sources" of He-3 in the outer solar system; calls Palaszewski the only person seriously studying ice-giant mining that he knows of; asks whether the architecture "doesn't violate basic physics." Secondary commentary.
- **Dwayne Day, "The helium-3 incantation" (*The Space Review*, 2015):** described by others as the standard skeptical case (lack of demand); **the article itself was not found** (query 46). UNVERIFIED.
- **A direct, independent energy-balance or cost critique of the Palaszewski architecture was NOT FOUND** (queries 42, 45). The critiques above concern demand, timeline, radiation and escape velocity.

---

## Q3 · Breeding He-3

### 3.1 Tritium decay (SOURCED)
- Tritium half-life **12.3 years**; **about 5.5% decays to He-3 each year** (CRS Report R41419, 6 October 2011, read; Helion's fuel-cycle blog and a Helion webinar report, read). **DERIVED check:** 1 − exp(−ln 2 × 1/12.3) = 5.48%.
- **Mass bookkeeping (DERIVED):** one tritium atom becomes one He-3 atom, so about **1 kg of He-3 per 1 kg of tritium that decays** (both about 3.016 u). Tritium specific activity from the sourced half-life: about 9,640 Ci/g.
- **US supply today:** "approximately 8,000 liters of new helium-3 per year" from the decay of the US tritium stockpile (CRS 2011). **DERIVED:** 1 L at standard conditions = 3.016 ÷ 22.414 = 0.1346 g, so 8,000 L is **about 1.08 kg a year**, implying a tritium inventory of about 20 kg (1.08 ÷ 0.055) if all of it came from decay of a stock. (The CRS text gives no tritium mass.) Stockpile He-3 was 140,000 L (1990), 235,000 L (2001), 50,000 L (2010); Watts Bar and Sequoyah reactor tritium production could add about 25,000 L eventually; stored tritium at Ontario Power Generation could yield about 130,000 L over ten years; Russia exported about 25,000 L a year from 2004 to 2008 and then suspended it. Prices and shortage: unit H1's task.
- **Tritium route cost (Wittenberg 1993, read; 1980s-1993 dollars):** tritium from ICF facilities about $10,000-12,000 per gram, from a fission pile with heavy-water moderator about $100,000/g, from an accelerator about $160,000/g; storage adds about $420 per gram of He-3 over ten half-lives; lowest total about **$10,500 per gram of He-3**; he gives the fuel cost of a 1,000 MWe D-³He plant as **130 mills/kWh(e)** at that price and concludes it "would probably never be competitive." A 1,000 MWe D-³He plant needs about **100 kg of He-3 a year**, "continuously separated from **1.8 tonnes** of ³H," whose storage "would be difficult to license." **DERIVED:** 100 kg ÷ 0.055 = 1.8 t, matching.

### 3.2 D-D fusion (SOURCED reaction data; DERIVED yield)
- Branches (Kulcinski, ISDC 2001, slides read; Wittenberg 1993): **D + D → n (2.45 MeV) + ³He (0.82 MeV) [50%]** and **D + D → p (3.02 MeV) + T (1.01 MeV) [50%]**; so 3.27 MeV and 4.03 MeV, mean **3.65 MeV per event**; neutrons carry 2.45 of 3.27 in the first branch. **DERIVED:** neutrons carry 1.225 of 3.65 MeV on average = **34%** of D-D energy.
- **Helion's account (the company, SOURCED as the company's statement):** Lily Hale, Fuel Cycle Team Manager, "How to engineer a renewable deuterium-helium-3 fusion fuel cycle," Helion blog, **28 March 2025**: about half of D-D fusions yield He-3 directly; the other half yield tritium that decays to He-3 at 5.5% per year; tritium is separated, purified and stored; the system "becomes more self-sufficient" the longer it runs and could reach a balance of production and consumption. The post gives **no quantities, doubling time or fuel per megawatt**. A *Commercial Fusion* article on a Helion webinar (Andrew Proffitt; date not stated in the page) lists three options (a D-D machine run mainly to make He-3; a balanced cycle; hold tritium and let it decay), quotes "5.5% of all that tritium every year will decay," and says the 2.5 MeV D-D neutrons "still require shielding and materials work." No independent confirmation of He-3 breeding at Polaris found; search snippets (UNVERIFIED) say Polaris reported measurable D-T fusion and 150 million °C in February 2026 and D-³He operation is still pending.
- **Yield (DERIVED):** each D-D event ends as one He-3 (directly or after tritium decay). Heat per kg of He-3 made = 6.022 × 10²³ ÷ 3.016 g × 3.65 MeV = **0.0037 GW-yr of D-D heat per kg of He-3**, i.e. about **270 kg of He-3 per GW-yr of D-D fusion heat**, if the product tritium and He-3 are all extracted and none burns in the plasma. **54 kg of He-3 (the burn for 1 GW-yr of D-³He heat) therefore costs about 0.2 GW-yr of D-D heat.** This ignores the bred tritium's decay delay: steady supply of 54 kg/yr by the decay route needs a standing tritium inventory of about 54 ÷ 0.055 = **980 kg** (DERIVED).
- **Semi-catalyzed mode (SOURCED, Wittenberg 1993):** D-D breeder at under 40 keV (optimum 28 keV) feeding a D-³He "satellite" reactor at 80-140 keV (optimum 75 keV); Shuy, Dabiri and Gurol (1986) conceptual tandem-mirror system: a breeder with 3,000 MW of fusion power supplies **12,000 MWe** of satellite reactors at 43.4 mills/kWh (1985). Wittenberg: the breeder "would have the same safety and radioactive waste disposal ratings as a D/T reactor," with tonnes of tritium storage, and needs two licenses. **DERIVED:** 3,000 MW of breeder heat supports 12,000 MWe of satellites, a ratio of about 1 : 4 in electric terms (the source's figures; not re-derived).
- **p + ⁶Li route:** needs several hundred keV; "no viable steady-state burn prospects" (Wittenberg 1993); ⁶Li-⁶Li side reactions make ⁷Be and neutrons.

### 3.3 Fission and heavy-water reactors
- **Heavy-water (CANDU-type) tritium production:** a search snippet gives "1.4-2.0 kCi/MW(e)" per year, about 97% in the moderator (source not identified; the ANS page I fetched for it was the wrong paper). **UNVERIFIED.** **DERIVED from that figure and the 9,640 Ci/g above:** 0.145 to 0.208 g of tritium per MWe-yr, i.e. **0.15 to 0.21 kg of tritium (hence up to the same mass of He-3 once decayed) per GWe-yr.** For 54 kg of He-3 a year this would take about **260 to 370 GWe of heavy-water reactors**, if all moderator tritium were recovered and left to decay (DERIVED). The Darlington Tritium Removal Facility in Ontario recovers tritium from moderator and heat-transport water (SOURCED at the level of an abstract page); a proposed Bruce-area design projected 178 g of tritium a year (snippet, UNVERIFIED).
- **Light-water reactors:** a secondary compilation gives 15-20 kCi per GWe-year and also a conflicting "less than 1 kCi" for the coolant and moderator portion; I could not reconcile them (UNVERIFIED). Release figures in UNSCEAR 2000 (via a Greenpeace report, snippet): heavy-water reactors about 670 TBq per GWe-year released against 21.4 for PWRs (these are releases, not production).
- **Dedicated production:** Watts Bar and Sequoyah irradiate tritium-producing rods (CRS 2011). Wittenberg (1993) concludes "the production of 3He by the decay of tritium produced in a fission or fusion reactor is uneconomical and the tonnes of tritium which must be stored are environmentally unacceptable."
- **Supply for research, per Wittenberg:** separating helium isotopes from commercial helium at **4 to 8 kg a year** plus tritium-stockpile decay could provide **up to 100 kg** for D-³He research and demonstration; "about 150 kg" is the total need through a power-demonstration reactor (his ref. 3).

### 3.4 Cost per kg of bred He-3
- **Only dated estimates found:** about **$10.5 million per kg** (Wittenberg's $10,500 per gram, 1993 dollars, tritium route). Hein's competitive ceiling for propulsion He-3 is $1-10 billion per tonne = **$1,000 to $10,000 per kg** (as reported, 2010). Kulcinski (2001 slides) uses $1 billion per tonne ($1,000/kg) as the price at which He-3 energy equals oil at $7 a barrel. **No current cost estimate of D-D-bred He-3 was found** (NOT FOUND; Helion publishes none in the blog read).
- Terrestrial market prices of existing He-3 (about $2,000 per liter commercial, i.e. about $15 million per kg, per CRS 2011 and snippets) are unit H1's subject; I note only that $2,000/L × (1 ÷ 0.1346 g) = $14.9 million per kg (DERIVED).

---

## Q4 · Mercury, Venus and the inner system

**Plain result: no published engineering proposal for collecting He-3 at Mercury, Venus or in near-Sun orbit was found** (queries 22, 58, 59, 83). The published material is a short list:

1. **Dawson and Livesey, "3He on Venus and Mercury," *Bulletin of the American Physical Society* 31, 1393 (1986)** (cited, **not read**), as summarized in **Wittenberg (1993), read in full:**
   - **Mercury:** "has a larger auroral flux providing **~5.4 kg/yr of 3He**" (Earth about 3 kg/yr); "Dawson suggested, therefore, that Mercury could provide a resource for 3He." But Mercury's atmosphere is very thin, vertical column density 2 × 10¹⁴ cm⁻² (Hartle, Curtis, Thomas 1975, his ref. 7); "if this entire atmosphere were He, it would contain only **360 kg of 3He**." Wittenberg's point is that Mercury, Earth and Mars have geomagnetic fields protecting their surfaces from the solar wind.
   - **Venus:** no magnetosphere, a thick CO₂ atmosphere (about 8 MPa) with a helium pressure of 0.6 MPa. Dawson suggested that the atmosphere could intercept the solar wind and become isotopically solar; "**if this mechanism were demonstrated**, the Venusian atmosphere may contain **2 × 10⁹ tonnes of 3He**." (The 0.6 MPa He pressure is as quoted; I did not check it against Venus atmosphere data. **UNVERIFIED** for the claim itself, and the mechanism is explicitly hypothetical.)
2. **Mercury helium, modern data (SOURCED: Weichbold et al., *JGR Planets* 130, e2024JE008679, accepted 18 February 2025; read as text):** the helium exosphere is a **thermal** population at a dayside surface density of about 1,100 cm⁻³ (surface temperature 615 K), and "the main exospheric He source can be identified as **thermal release and thermal recycling of solar wind implanted He particles**"; Mariner 10 gave 4,500 to 6,000 cm⁻³, BepiColombo PHEBUS 600-1,000 cm⁻³ at the terminator. Solar-wind implantation is modeled at an **average 2.5 × 10²³ He s⁻¹** (Winslow et al. 2012), a primary supply of about **3.3 × 10⁵ He cm⁻² s⁻¹** averaged over the surface; He atoms live only about 10 to tens of days in the exosphere and have been "recycled" after returning to the surface. Solar-wind helium reaches the surface through the polar cusps "when the IMF is in a favorable orientation." **Implication (as stated by the paper's own physics, not a conclusion about mining):** implanted helium on the hot dayside is released thermally, not retained for geologic time. A sporadic non-thermal helium population (150 cm⁻³, 2,700 K) was attributed to meteoroid-impact vaporization.
3. **DERIVED Mercury figures:** at 2.5 × 10²³ He s⁻¹ and a ratio of 4.64 × 10⁻⁴ the **whole planet receives about 18 kg of He-3 a year** (2.5 × 10²³ × 4.64 × 10⁻⁴ × 3.156 × 10⁷ s × 5.0 × 10⁻²⁴ g). The planet's cross-section is 18.7 million km²; with the proton flux of 10⁹ cm⁻² s⁻¹ and A_He 4%, an **unshielded** full disc would intercept about **550 kg of He-3 a year** (DERIVED). Mercury's surface is mostly shielded by its magnetic field; MESSENGER's cusp survey (snippet, UNVERIFIED) reports an average proton precipitation flux of 1.0 × 10⁷ cm⁻² s⁻¹ with peaks of 1.4 × 10⁹ and, during coronal mass ejections, the magnetopause reaching the surface about 30% of the time.
4. **Mercury as a regolith source: NOT FOUND** as a published analysis. One overview page (space-mining.com, a general site) says Mercury's solar wind exposure "could make it a richer source than the Moon" but gives no concentrations (snippet, UNVERIFIED). **No measured He-3 concentration in Mercury's regolith exists (NOT FOUND).**
5. **Venus atmosphere He-3 mining proposal: NOT FOUND.** Forum threads only. NASA's Venus electrolysis concept (EVE) does not involve He-3.
6. **Mercury-based mass driver for He-3, or a tie between He-3 and starlifting: NOT FOUND.**
7. **Solar-wind capture near the Sun** has the flux scaling in §1.4 to §1.5 and the heat-shield data in §1.5 as the only published inputs.
8. **Cosmic and planetary context (Wittenberg 1993):** the cosmic 3He/4He ratio is about 300 ppm; atmospheric 3He on Earth 4,000 t (3He/4He 1.393 × 10⁻⁶), oceans 13 t.

---

## Q5 · Asteroids and comets

- **Measured He-3 concentrations in asteroid regolith or meteorites: NOT FOUND** (queries 67, 68, 70, 71, 72). What was found:
  - **Itokawa (Hayabusa, Nagao et al., *Science* 333, 1128, 26 August 2011; JAXA press release read):** the three grains hold "large amounts of solar helium" at various depths, but with **preferential helium loss** from frictional wear of space-weathered rims; residence time under 8 million years (from ²¹Ne); surface loss of tens of centimeters per million years. No concentrations on the page. A 2023 abstract (snippet) maps solar-wind ⁴He with a peak about 30 nm deep.
  - **Bennu (OSIRIS-REx; Marty et al., *Meteoritics & Planetary Science*, in press; a blog summary dated 8 October 2025 read):** eight particles measured for all stable noble gases; solar wind implantation is a secondary component "mostly identified in the light noble gas (He and Ne)"; maximum solar-wind irradiation duration **≤100,000 years**; noble gas abundances at least twice those of CI meteorites; no He values on the page.
  - **Ryugu (Hayabusa2; Nature Communications, September 2024; snippet):** primordial noble-gas component; no He-3 number.
  - **Gas-rich meteorites and regolith breccias:** solar-derived He and Ne exist; "helium depleted relative to" solar gas-rich meteorites in some lunar-meteorite comparisons (snippet); no He-3 value found.
- **Interplanetary dust (SOURCED, Wittenberg 1993 addendum, read):** magnetic fines collected from deep-sea sediment: **3He/4He = 3.1 × 10⁻⁴**, 4He 7.1 × 10⁻⁵ cm³ STP/g, **3He content 2.2 × 10⁻⁸ cm³/g = 3 × 10⁻¹² g(³He) per g** of particles; IDPs generally above 2 × 10⁻⁴ (about 100 times Earth's atmosphere); inflow 50 to 100 Gg a year of meteoritic and cometary material. **DERIVED:** 3 × 10⁻¹² g/g is **about 0.03% of the lunar mare value** (10 ppb = 10⁻⁸ g/g, Olson 2021).
- **Asteroid He-3 estimates in the literature: NOT FOUND.** The Itokawa result says helium is mobile enough to be lost; Bennu's solar-wind exposure is short. The comets question: no He-3 data found (no query returned any).

---

## Q6 · Demand side, with working

**Constants (DERIVED/SOURCED):** D-³He releases 14.68 MeV (proton) + 3.67 MeV (He-4) = **18.35 MeV** per reaction (Kulcinski 2001, read; Olson 2021 gives the same split). Per kg of He-3: 6.022 × 10²³ ÷ 3.016 × 10⁻³ kg × 18.35 MeV × 1.602 × 10⁻¹³ J/MeV = **5.87 × 10¹⁴ J = 18.6 MW-yr of fusion heat**, so **53.8 kg of He-3 per GW-yr of fusion heat**. This is the discussion file's "54 kg" and it **agrees**; it is a lower bound because D-D side reactions in a D-³He plasma are not counted and no efficiency losses apply to the heat figure. Olson (2021) writes "~19 MWyr/kg of fusion energy"; Kulcinski (2001): "1 tonne of He-3 can produce **10,000 MWe-y** of electrical energy" (**DERIVED:** 10,000 ÷ 18,600 = 54% heat-to-electric, or the equivalent allowance for side reactions and losses; he also claims plant efficiencies above 70%). Wittenberg: about **100 kg a year per 1,000 MWe**; Schmitt (abstract, snippet): about 100 kg runs a 1,000 MWe plant for a year. Olson: 33 kg of He-3 "enough to operate one 400 MW D3He fusion power plant," which is 82 kg per GWe, within the same range.

### 6.1 Published demand estimates (SOURCED unless marked)
| Estimate | Source |
|---|---|
| 13 t/yr for 25% of projected US power (5.16 × 10⁵ MWe-yr over 25 years from 1993). **DERIVED check:** 0.25 × 5.16 × 10⁵ = 1.29 × 10⁵ MWe-yr × 100 kg = 12.9 t | Wittenberg 1993 |
| 40 t of He-3 for the entire US electricity consumption in 2000 | Kulcinski 2001 (slides) |
| about 1,500 t/yr for a Daedalus-scale starship; 15 t/yr at 1/100 payload | Hein, as reported (Centauri Dreams 2010) |
| about 14,000 t/yr of D-³He mix (about 8,400 t of He-3 at 60% He-3 by mass, DERIVED: 3.016 ÷ 5.030) for world demand by 2100 at 2.5% growth; **DERIVED check:** 8,400 t ≈ 156 TW of fusion heat, against about 19 TW today grown 2.5% a year for 75 years (about 119 TW) | Crowl, as reported (Discovery/NBC 2011) |
| 165.2 t could power the 2019 US for a year; "less than five kilograms" current world demand | snippets (techniumscience; gasworld): UNVERIFIED |
| about 150 kg total needed through a power-demonstration reactor | Wittenberg 1993 |

### 6.2 Demand arithmetic for the setting (DERIVED)
- **101.7 GW electric** at 54% (Kulcinski's ratio): 188 GW of heat × 53.8 kg = **10.1 t/yr**; at 70%: **7.8 t/yr**; at 60%: **9.1 t/yr**; at 35%: **15.6 t/yr**. At Kulcinski's 100 kg per GWe-yr: **10.2 t/yr**.
- **324 GW net** (the Tower's figure) at 100 kg per GWe-yr: **32.4 t/yr**.
- **World:** 592 EJ total energy in 2024 (Energy Institute Statistical Review 2025, via a search snippet of a Creamer Media article; the page itself failed to load, so UNVERIFIED; the 2026 edition is reported to give above 600 EJ for 2025): 592 EJ ÷ 3.156 × 10⁷ s = 18.8 TW; × 53.8 kg per GW-yr = **about 1,010 t/yr** if all of it were supplied as D-³He fusion heat (a 600 EJ year would be about 1,020 t). The discussion file's "about 1,030 t/yr" agrees within 2%.

### 6.3 Supply figures from Q1 to Q5 (kg of He-3 per year; DERIVED unless marked)
| Source | He-3 per year | Basis |
|---|---|---|
| US tritium-stockpile decay | about 1.1 kg | CRS 2011: 8,000 L/yr |
| Commercial helium by-product (1993) | 4 to 8 kg (potential); 2-3 kg realizable from US natural gas | Wittenberg 1993 |
| Mercury: whole planet's implanted supply | about 18 kg | 2.5 × 10²³ He/s (Weichbold 2025) × 4.64 × 10⁻⁴ |
| Mercury auroral flux | 5.4 kg | Dawson/Wittenberg 1993 |
| Earth auroral precipitation | about 3 kg | Wittenberg 1993 |
| One lunar M-3 miner | 33 kg (66 kg at 20 ppb) | Olson 2021; 5 million tonnes of regolith; 350 kW; 1,258 t/hr excavated (unit H1's subject) |
| Solar-wind plane, 1 AU | 54 kg needs 6 to 8 million km²; per km² 7 to 9 mg | §1.4 |
| Solar-wind plane, 0.1 AU | 54 kg needs 60,000 to 76,000 km² (about 100,000 to 125,000 with the model-based flux) | §1.4, §1.5 |
| Heavy-water reactors (UNVERIFIED rate) | 0.15 to 0.21 kg per GWe-yr; 260 to 370 GWe for 54 kg | §3.3 |
| D-D breeding | about 270 kg per GW-yr of D-D heat; 54 kg costs about 0.2 GW-yr of D-D heat | §3.2 |
| One Palaszewski ASC trip | 500 kg (2012, 2024); 50 t (2020, large-vehicle case) | §2.1 |

### 6.4 Setting-sized comparisons (DERIVED)
- **10.1 t/yr (101.7 GWe at 54%) from a solar-wind plane** at 1 AU: 10,100 kg ÷ 54 kg × 6 to 8 million km² = **about 1.1 to 1.5 billion km²** at 1 AU; at 0.1 AU **11 to 14 million km²** (pure r⁻², 100% capture); a Mercury-sized cross-section is 18.7 million km². (Each is a capture plane facing the wind, not a mass of structure.)
- **10.1 t/yr from Uranus** at 1.52 × 10⁻⁵ (Palaszewski's fraction) and 100% recovery: 10,170 kg ÷ 1.52 × 10⁻⁵ = 6.7 × 10⁸ kg of gas a year = **about 21 t of atmosphere every second**, against 4 to 120 kg/s per mining vehicle in the papers (so about 180 to 5,300 vehicles operating continuously; DERIVED). In 500-kg trips, 10.1 t a year is about 20 trips per year; the 2020 paper's fleet delivery rate was 500 t/yr of combined He-3 and D over 10 years (DERIVED from 5,000 t), so 10 t of He-3 is 2 to 4% of that program's throughput. (The He-3 share of the 5,000 t is not stated in the paper.)
- **10.1 t/yr from lunar mining** at 33 kg per M-3 miner: about **310 miners** (DERIVED).
- **10.1 t/yr from heavy-water reactors** (0.15-0.21 kg/GWe-yr): about 49,000 to 70,000 GWe (DERIVED, UNVERIFIED rate).
- **10.1 t/yr from D-D breeding:** 10,100 kg × 0.0037 GW-yr per kg = **about 37 GW-yr of D-D heat a year**, an average of about 37 GW of D-D breeder heat running alongside the 188 GW of D-³He heat (equivalently 0.2 × 188 GW; DERIVED, with the §3.2 caveats: all tritium and He-3 extracted, none burned in place).

---

## FINAL

### What the sources support (SOURCED)
- The solar-wind 3He/4He ratio is a few × 10⁻⁴ (Genesis bulk: 4.64 ± 0.09 × 10⁻⁴, 2009; Apollo and Ulysses values 3.3 to 4.4 × 10⁻⁴), and the helium flux at 1 AU is about 1 × 10⁷ cm⁻² s⁻¹. The discussion file's 39-54 g per tonne and its capture areas are reproduced to within the spread of those inputs (§1.3, §1.4).
- Palaszewski's Uranus and Neptune He-3 fractions come from the Voyager helium abundance times an **assumed 10⁻⁴** isotope ratio; Neptune's helium value has since been revised down; no ice-giant He-3 measurement exists; the studies are paper-only sizing with a 500-kg-per-trip payload and architectures of tens of thousands of tonnes.
- Helion's own statement of its fuel cycle (28 March 2025): about half of D-D events yield He-3 directly and half make tritium that decays at 5.5% a year; the company gives no quantities.
- **Mercury:** the only published inner-system He-3 resource statements are Dawson's 1986 suggestion (5.4 kg a year of auroral flux; 360 kg if the whole exosphere were He) and Venus "2 × 10⁹ t if a hypothesized mechanism is demonstrated," both as relayed by Wittenberg. Modern data say Mercury's implanted helium is released thermally and recycled.
- D-³He fusion heat per kg of He-3 is 18.6 MW-yr (53.8 kg per GW-yr): the discussion file's 54 kg is confirmed by an independent derivation and by Olson's 19 MW-yr/kg and Kulcinski's 10,000 MWe-yr per tonne.

### What the sources do not support
- No source I read shows a working solar-wind He-3 collector, an engineered capture concept with a mass or cost, or a separation scheme that starts from solar-wind gas.
- No source ties He-3 mining to Mercury, Venus or near-Sun orbit as a proposal; the Dawson Venus mechanism is "if demonstrated."
- No source gives a measured He-3 concentration for any asteroid, comet, Mercury regolith or Venus atmosphere.
- No source gives a cost for D-D-bred He-3 after 1993.

### NOT FOUND (with where the search died)
- A peer-reviewed or agency-level solar-wind He-3 collector design (died at the sources: only a ResearchGate preprint behind a 403, a joke site, forum threads).
- Measured 3He/4He in the solar wind inside 0.3 AU (died at the query: no paper surfaced).
- Primary pages for Gloeckler and Geiss 1998 (405, redirect, 403) and the Apollo foil flux (the Apollo 16 chapter has no values): the figures above are snippet-level.
- The Hein and Long Icarus gas-planet paper (access-restricted); Dwayne Day's 2015 article (not returned); Wilkes and Wittenberg 1992 solar-wind-gas separation paper (not retrieved).
- A heavy-water-reactor tritium production figure from a primary page (the ANS page returned a different paper; the dspace page returned 503; DNS failure on another host).
- He-3 content of asteroids, comets and gas-rich meteorites (died at the sources and the query).
- A kilometer-scale collector thermal analysis near the Sun; the Parker mission page (socket hang up).
- Ice-giant 3He/4He (not measured).

### Surprises worth noting (facts, not recommendations)
- The Palaszewski papers use an assumed 10⁻⁴ isotope ratio; Jupiter's measured ratio is 1.66 × 10⁻⁴.
- The 5,000-t "fuel" delivered in the 2020 architecture is a He-3-plus-deuterium propulsion load, not a power-plant fuel flow, and the papers give no electricity-scale He-3 rate.
- Mercury's total implanted He-3 supply is about 18 kg a year, less than one lunar M-3 miner's design rate.

---

## Search log
Format: number · tool · query or URL · result · where a dead end died. Times are not recorded per call. "Binary" means the fetch tool returned a PDF as bytes, which I then read with `pdftotext` in the scratch folder (the content was then read in full; counted as a hit).

1. WebSearch · solar wind 3He/4He ratio measured Ulysses SWICS ACE SWIMS helium-3 abundance · hit (snippets)
2. WebSearch · Palaszewski helium-3 mining Uranus Neptune Saturn atmosphere NASA technical report · hit (NTRS list)
3. WebFetch · ui.adsabs.harvard.edu/abs/1998SSRv...84..275G/abstract · HTTP 405 · died at the source
4. WebFetch · ntrs.nasa.gov/citations/20190029288 · hit (abstract only)
5. WebFetch · NTRS 20150006664 PDF · binary, read locally · hit
6. WebFetch · NTRS 20170008828 PDF link · abstract only · partial
7. WebFetch · NTRS 20240007489 citation page · hit
8. WebFetch · NTRS 20205004479 citation page · hit
9. WebFetch · NTRS 20240007489 PDF · binary, read locally · hit
10. WebFetch · NTRS 20205004479 PDF · binary, read locally · hit
11. WebFetch · link.springer.com Gloeckler and Geiss 1998 · redirect to a login host, not followed · died at the source
12. WebFetch · deepblue.lib.umich.edu/items/9ba93056-... · HTTP 403 · died at the source
13. WebFetch · arxiv.org/pdf/astro-ph/9704069 · binary, read locally (Gautier and Morel 1997, protosolar D/H) · partial
14. WebSearch · solar wind helium-3 flux per cm2 per second 3He/4He Apollo solar wind composition experiment foil Geiss 1972 · partial (snippet-level values)
15. WebFetch · NTRS 19840005043 (Coplan et al. 1983) · hit
16. WebSearch · Apollo Solar Wind Composition Experiment helium flux 4He/3He 2350 … · partial
17. WebSearch · collecting helium-3 from the solar wind spacecraft collector concept electrostatic magnetic capture area near Sun fusion fuel · partial; miss for an engineering concept
18. WebSearch · "solar wind" helium-3 harvesting "magnetic" OR "electrostatic" scoop feasibility paper JBIS OR Acta Astronautica · miss for a peer-reviewed concept
19. WebSearch · Wittenberg Kulcinski Santarius solar wind helium-3 mining satellite orbit … · hit (lunar only)
20. WebFetch · researchgate.net/publication/394095079 · HTTP 403 · died at the source
21. WebSearch · exact title of that preprint · miss
22. WebSearch · harvesting solar wind helium-3 in space instead of Moon mining near-Sun orbit collector Mercury concept study · partial (no Mercury study)
23. WebSearch · helium-3 from the solar wind "not economically" OR "impractical" magnetic sail scoop … critique · miss (forums)
24. WebFetch · NTRS 20210022801 (Olson 2021) PDF · binary, read locally · hit
25. WebSearch · solar wind proton flux 1 AU typical density … Kasper 2007 solar cycle · partial
26. WebSearch · Parker Solar Probe heat shield temperature 2,500 F … perihelion · partial (snippets)
27. WebSearch · solar wind mass flux scaling with heliocentric distance r^-2 Parker Solar Probe … · partial
28. WebFetch · arxiv.org/abs/1711.07534 (Venzmer and Bothmer) · hit
29. WebFetch · arxiv.org/html/2502.19492v1 (Johnson et al.) · hit
30. WebSearch · solar wind at 1 AU cm-2 s-1 proton flux average … · partial (snippets)
31. WebSearch · Genesis mission solar wind fluence collected helium … Heber · partial (snippet-level flux)
32. WebFetch · authors.library.caltech.edu/records/g1mba-xbv04 (Heber 2009) · hit
33. WebFetch · research-collection.ethz.ch/handle/20.500.11850/161883 · HTTP 500 · died at the source
34. WebSearch · separating helium-3 from helium-4 methods superfluid heat flush thermal diffusion cryogenic distillation … · partial (snippets)
35. WebSearch · Apollo SWC Geiss Bühler Cerutti Eberhardt Filleux … Apollo 16 preliminary science report · partial
36. WebFetch · NTRS 19730013019 · abstract only, no values · miss for values
37. WebFetch · rlg.fas.org/helium3.pdf · empty · died at the source
38. WebSearch · Galileo probe mass spectrometer Jupiter 3He/4He … Mahaffy 1998 · hit (snippets, later verified by #82)
39. WebSearch · Uranus Neptune atmosphere helium mole fraction Voyager 2 0.152 0.19 … · hit
40. WebFetch · arxiv.org/pdf/2004.13987 (Cavalié et al. 2020) · binary, read locally · hit
41. WebSearch · Project Daedalus helium-3 Jupiter atmosphere mining 30,000 tonnes … · hit (snippets)
42. WebSearch · critique OR feasibility mining helium-3 from gas giants Uranus Neptune Palaszewski … · partial; no energy-balance critique
43. WebFetch · centauri-dreams.org/2010/09/28/project-icarus-finding-the-fuel/ · hit
44. WebFetch · planetaryintel.substack.com/p/steelmanning-helium-3 · hit
45. WebSearch · Hein Tziolas Crowl Project Icarus atmospheric helium 3 mining Uranus … · partial (Hein and Long paper restricted)
46. WebSearch · Dwayne Day "The helium-3 incantation" Space Review · partial (article not returned)
47. WebFetch · centauri-dreams.org/2011/06/01/starship-fuel-from-the-outer-system · 301 redirect (http), not re-fetched · skipped
48. WebFetch · nbcnews.com/news/amp/wbna43232067 · hit
49. WebSearch · Helion Energy helium-3 produced by D-D fusion Polaris breeding … · hit
50. WebSearch · Helion Polaris 2025 2026 D-T fusion first D-He3 announcement … · hit (snippets)
51. WebFetch · helionenergy.com/blog/how-to-engineer-a-renewable-deuterium-helium-3-fusion-fuel-cycle · hit
52. WebFetch · commercial-fusion.com … Helion Proffitt webinar · hit
53. WebSearch · tritium production CANDU reactor kg per year heavy water moderator Darlington … · partial (snippet figure)
54. WebFetch · bvbvf1.bib-bvb.de … Cernavoda He-3 separation · DNS failure · died at the source
55. WebFetch · wx1.ans.org/pubs/journals/fst/a_1818 · wrong paper (Darlington bubbler) · miss
56. WebSearch · helium-3 supply tritium decay US stockpile production 8,000 liters … · hit (snippets)
57. WebFetch · everycrsreport.com … R41419 · hit
58. WebSearch · Mercury helium-3 resource solar wind implanted regolith magnetosphere … · partial
59. WebSearch · Venus atmosphere helium-3 OR "helium 3" mining … · miss for a serious proposal
60. WebFetch · fti.neep.wisc.edu … fdm967.pdf (Wittenberg) · binary, read locally · hit
61. WebSearch · Mercury magnetosphere solar wind plasma precipitation … cusps MESSENGER … · partial
62. WebSearch · Mercury exosphere helium MESSENGER Mariner 10 … · hit
63. WebFetch · repository.tudelft.nl … Hermean helium · SSL error · died at the source
64. WebFetch · eoas.ubc.ca … Winslow 2017 · 301 to a homepage, not followed · died at the source
65. WebFetch · wurz.space.unibe.ch/Weichbold_JGR_2025.pdf · binary, read locally · hit
66. WebFetch · essopenarchive.org … Hermean helium · HTTP 403 · died at the source
67. WebSearch · asteroid regolith solar wind implanted helium-3 concentration Itokawa Ryugu Bennu … · partial
68. WebSearch · helium-3 in asteroids mining estimate NEA … · miss (lunar only)
69. WebFetch · cosmochemistry-papers.com Bennu noble gases · hit (no He values)
70. WebSearch · Nagao 2011 Science Itokawa regolith noble gases … · hit (qualitative)
71. WebSearch · gas-rich meteorites solar wind implanted helium concentration … · miss for numbers
72. WebFetch · global.jaxa.jp/press/2011/08/20110826_hayabusa_e.html · qualitative only · partial
73. WebSearch · Energy Institute Statistical Review 2025 world primary energy 2024 … · partial (snippet)
74. WebSearch · Kulcinski Schmitt helium-3 required per year fusion power world electricity … · partial
75. WebFetch · newsletter.en.creamermedia.com … · DNS failure · died at the source
76. WebFetch · fti.neep.wisc.edu … glk_isdc.pdf (Kulcinski 2001) · binary, read locally · hit
77. WebSearch · tritium produced per GW(e) year PWR CANDU heavy water reactor UNSCEAR … · partial (secondary figures conflict)
78. WebFetch · NTRS 20150006664 citation page · hit (dated 29 July 2012)
79. WebFetch · dspace.zcu.cz … tritium production LWR and HWR · HTTP 503 · died at the source
80. WebSearch · Genesis spacecraft collector arrays total area … · partial (73-cm pan; 850 to 887 days)
81. WebFetch · parkersolarprobe.jhuapl.edu/The-Mission/index.php · socket hang up · died at the source
82. WebFetch · public.websites.umich.edu/~atreya/Articles/1998_Galileo_Probe_Measurements.pdf · binary, read locally · hit (Mahaffy et al. 1998 verified)
83. WebSearch · "solar wind" helium-3 collection spacecraft "collection area" OR "swept area" … · partial (preprint snippet only)
84. WebSearch · "inferred unrecoverable" helium-3 USGS 2022 … · partial

Also: one local read (not a web call) of page 2 of the 2012 Palaszewski PDF rendered to an image, to read Table I; calculations in a scratch script (`calc.py`, scratch folder, not in the repo).
