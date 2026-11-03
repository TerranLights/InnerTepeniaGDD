# Nuclear waste and byproducts in the construction and operation of low-Earth-orbit infrastructure: research (Unit R8, 2026-11-02)

**Started 2026-11-02 18:17. Finished 2026-11-02 18:38.**

**Scope.** The developer asked whether nuclear waste can be used toward building orbital infrastructure in low Earth orbit (LEO). This file collects real-world facts on seven questions: shielding physics and materials; depleted uranium and other heavy byproducts as mass; isotope power; fission reactors in space; law and safety; launching waste to space; and other uses in orbital construction. **Facts only. No recommendation, no design, no ranking.** Labels: **SOURCED** (read at the source in this session, by fetched page or by OCR/text extraction of the fetched document), **DERIVED** (my arithmetic on sourced figures, working shown), **UNVERIFIED** (seen only in a search-result summary, a mirror or secondary site, or recalled), **NOT FOUND** (looked for, queries in the log). Background files read for orientation only: `Theoretical-Calculations/Orbital_Infrastructure_Mass_Budget.md` (line 33: shielding is the largest mass driver, about 5 to 10 t/m2; line 36: about 7 million tonnes total for the ~0.5 km2 floor-area case) and the novel repo's `leo_and_orbital_habitats.md` (section C2: 4.5 t/m2 versus 10 t/m2 versus a modeled minimum near 20 to 40 g/cm2). Nothing was copied from them.

**Method note on tools.** WebFetch returned unreadable raw bytes for scanned NASA reports. Those PDFs were then saved locally and read with `pdftotext` / `tesseract` OCR (scratch folder only; nothing written to the repo except this file). OCR text is noisy; figures read from OCR are flagged where a digit could be wrong. Two documents (NTRS 19820017396 and the 1980 DOE EIS chapter) were obtained this way; NTRS 19820017396 was downloaded with `curl` from the same NTRS URL after WebFetch hit its size limit (this was a size limit, not a refusal or block).

## PROGRESS

- [x] Q1 Shielding physics and materials
- [x] Q2 Depleted uranium and heavy byproducts as mass
- [x] Q3 Isotope power
- [x] Q4 Fission reactors in space
- [x] Q5 Law and safety
- [x] Q6 Launching waste to space; radioactive debris
- [x] Q7 Other orbital-construction uses (mostly NOT FOUND)
- [x] FINAL section
- [x] Search log

---

## Q1. Shielding physics and materials

### 1.1 Hydrogen-rich versus aluminum versus lead for galactic cosmic rays (GCR)

**SOURCED. NASA Technical Paper 3473, "Performance Study of Galactic Cosmic Ray Shield Materials," Kim, Wilson, Thibeault, Nealy, Badavi, Kiefer, NASA Langley, November 1994** (NTRS 19950010497; OCR of the fetched PDF).
- Stopping physics: "Materials with the most electrons per unit mass, the least mean excitation energy, and the least tight binding corrections make the best energy absorbers. Thus, liquid hydrogen is a favored material and lead is less efficient as an energy absorber."
- LET (linear energy transfer) transmission: "liquid hydrogen being the most efficient and lead the least efficient" at attenuating the highest-LET components. The "pivotal LET" (where attenuation of a species equals its production in nuclear events) is "less than 1 keV/um for liquid hydrogen," rises to "40 to 50 keV/um for lead," and sits at a few keV/um for aluminum.
- A direct mass-for-mass comparison: the iron flux, which in free space "accounts for nearly 30 percent of the cell transformations," "is reduced by several orders of magnitude in the 30 g/cm2 liquid hydrogen shield compared with a reduction factor of only 3 behind an equivalent mass of lead shielding." In the liquid hydrogen shield all components are attenuated; "in the lead shield, the light ions tend to increase as the heavier ions slowly attenuate. In addition, the neutron, hydrogen ions, and helium ions are greatly enhanced over their free-space values, partly because of the secondary production from the target nuclei."
- Summary statement: "performance indices up to a factor of 20" for biological protection at constant shield mass with changing composition; "the unique role of hydrogenous materials used as high-performance shields is clear." The paper also states the uncertainty in nuclear cross sections "will not allow an accurate evaluation of risk reduction."
- Caveat: a 1994 model on a cell-transformation endpoint, not a dose-equivalent standard.

**SOURCED. Norman et al. (NASA Langley), "Early Results from the Advanced Radiation Protection Thick GCR Shielding Project," 2017** (NTRS 20170005580; text extracted from the PDF). "Preliminary results of space radiation models indicate that a minimum in the dose equivalent versus aluminum shielding thickness may exist in the 20-30 g/cm2 region. For greater shield thickness, dose equivalent increases due to secondary neutron and light particle production." "The polyethylene results do not show the increase in dose." In the paper's updated runs the minimum for aluminum "has shifted closer to 20 g/cm2." Polyethylene "has a large [hydrogen content] ... minimizing the buildup of light" secondaries. Modeled for the 1977 solar-minimum GCR environment. First laboratory measurements were at the NASA Space Radiation Laboratory (neutrons and light ions between thick aluminum targets).

**SOURCED (summary only, from search results, then not opened in full): polyethylene as NASA's reference shielding material** in accelerator tests (OSTI 918614); the Lunar Reconnaissance Orbiter CRaTER instrument measured reduced dose behind tissue-equivalent plastic. **UNVERIFIED** (snippet): an arXiv 2024 HZETRN/OLTARIS paper (2411.18083) reports metal hydrides below polyethylene and aluminum over 5 to 15 g/cm2.

### 1.2 Where high-Z materials appear in the literature, and what they do

**SOURCED. Atwell, Rojdev, Aghara, Sriprisan, "Mitigating the Effects of the Space Radiation Environment: A Novel Approach of Using Graded-Z Materials," 2013** (NTRS 20140002469; text extracted).
- Graded-Z means a high-Z layer (usually tantalum, also tungsten) between low-Z layers. It is "commonly used in satellite" electronics shielding and "reduce[s] electron penetration over 60%" compared with a single material of the same mass. The paper quotes a prior study: for protons "the optimal shield would consist of a single, low-Z material layer."
- In the paper's own GCR runs, tantalum or tungsten (6.3 and 7.3 g/cm2 layers) plus 5 g/cm2 of high-density polyethylene gave "some slight dose reductions" versus polyethylene alone in a GCR environment; the combination "was actually detrimental with an SPE [solar particle event] environment when compared with a single layer of HDPE." At very large thickness (water 100 to 300 g/cm2) "the results were comparable."
- "Secondary particles, namely neutrons, are produced as the primary particles penetrate a spacecraft"; the authors propose boron, lithium or beryllium dopants to absorb them.

**SOURCED (from search-result summaries of sources not opened):** a Berkeley Lab overview states dose falls with thickness but "the contribution to the dose and dose equivalent from secondary neutrons also increases"; another source reports that behind thick shielding (20 g/cm2 or more) "up to 80-90% of the total dose equivalent" comes from light secondary fragments and neutrons. Both **UNVERIFIED** (not opened).

**NOT FOUND:** a direct numerical neutron-yield comparison for lead or tungsten versus aluminum under GCR (the TP-3473 qualitative result above is the closest). Tungsten did not appear in neutron-yield results for the queries run.

### 1.3 Where high-Z is the standard answer: reactor gamma shadow shields

**SOURCED. Banjac and Heger, "Mass Optimization Studies of Gamma Shield Materials for Space Nuclear Reactors," Nuclear Technology 108(1), 126-136, 1994** (abstract fetched at ans.org). Reference reactor: nuclear-electric, 10^16 gamma/s source term, dimensions from the Russian TOPAZ-II; seven candidate materials; target 5.0 mrem/h at the shield outer surface; gamma energies 0.5, 1.0, 2.0 MeV. "Depleted uranium gives the lowest mass requirement at all three energies, with a mass index of 1.0"; tungsten and lead have indices of roughly 1.2 to 1.7 and "could substitute for depleted uranium in lower-power reactors."
**UNVERIFIED** (snippet): a 1969 NASA Lewis report (NTRS 19690026439) recommended lithium hydride for neutrons and depleted uranium for gamma on a space power reactor.
**SOURCED** (figure labels and text in the Kilopower papers, see Q4): Kilopower uses lithium hydride neutron shielding and "Lithium Hydride/Tungsten Shielding" in the LANL description. In the NASA/LANL KRUSTY paper the flight-concept figure labels "Lithium Hydride Shielding."
**UNVERIFIED** (snippet): shields can be 20 to 50% of a space reactor system's mass.

### 1.4 Aluminum, regolith, water: what the background notes already hold, plus new regolith data

The background notes carry the per-square-meter figures (SP-413 4.5 t/m2; Kalpana One 4.5 to 10 t/m2); those were not re-researched.
**UNVERIFIED** (search snippets): a DLR/Matthiä and Berger 2024 *Space Weather* Geant4 study finds that for GCR on the lunar surface adding regolith "did not reduce the absorbed dose significantly" (about 180 g/cm2 of regolith gives about 200 mSv/yr, "about 25% below" unshielded), while for solar particle events more than 10 g/cm2 of regolith gives a safety factor of two. A NASA presentation (NTRS 20250006713) says dose-depth curves beyond about 100 g/cm2 are poorly constrained.
**DERIVED (thickness equivalents for 4.5 t/m2 = 450 g/cm2):** depleted uranium at 19.1 g/cm3 is 450/19.1 = 23.6 cm; lead at about 11.3 g/cm3 is about 40 cm; water at 1.0 g/cm3 is 4.5 m. (This is geometry only; it says nothing about GCR dose, for which see 1.1 and 1.2.)

### 1.5 Any proposal that uses nuclear waste, vitrified waste, or depleted uranium as spacecraft or habitat shielding?

- **Depleted uranium as spacecraft or habitat GCR shielding: NOT FOUND.** A query for it returned only terrestrial and reactor-shield uses (1.3). One secondary summary says metals like lead or depleted uranium "provide the most protection" but are heavy (**UNVERIFIED**; Universe Today snippet).
- **Vitrified high-level waste or spent fuel as habitat shielding: NOT FOUND.** The closest items: a 2019 JBIS paper (R. J. Soilleux, "Orbital Civil Engineering: Waste silicates reformed into radiation-shielded pressure hulls") proposes anhydrous glass from metal-extraction waste silicates (not nuclear waste) as shielding, about half the thickness of water-based shielding, for an "O'Neill Island 1" class habitat, buildable in ten years (**UNVERIFIED**; shop page snippet, paper not opened). A 2024 Chornobyl-institute preprint asks whether cemented and vitrified radioactive waste could be a raw source of compounds for spacecraft devices and materials (**UNVERIFIED**; snippet). Terrestrial patents describe glass and concrete waste shielding in storage containers only.
- **Radiation from the waste itself:** no source retrieved discusses the habitat dose from using radioactive waste as shielding. The 1980-82 space-disposal designs instead wrapped the waste in a **separate radiation shield** (stainless steel core, spherical shield; lead iodide poured into the metal shield in one variant) so that the waste payload stays below dose limits (OCR of NTRS 19820017396, sections 2.2 and 2.4). **SOURCED.**

---

## Q2. Depleted uranium (DU) and other heavy byproducts as mass

**SOURCED/UNVERIFIED mix; each marked.**

- **Availability.**
  - **UNVERIFIED** (WNA-authored chapter by Kidd, via search snippet): "World stock is about 1.3 million tonnes," with ">50,000 tonnes" added each year, mainly in the US, Europe and Russia.
  - **UNVERIFIED** (2001 Nuclear Energy Agency estimate cited by the National Academies, via snippet): about 1.2 million tonnes worldwide.
  - **SOURCED** (OSTI 885886, DUF6 Materials Use Roadmap, abstract): about 500,000 metric tons of surplus DU in the US Department of Energy inventory: 470,500 MT as DUF6 at Paducah, Portsmouth and Oak Ridge (with 225,000 MT of chemically combined fluorine and 74,000 MT of steel in the cylinders) and about 27,860 MT in other forms.
  - **SOURCED** (World Nuclear News, "Heads up on new tails partnership"): the DOE's gaseous diffusion operations "produced nearly 700,000 tonnes of tails over more than fifty years"; most tails sit "in storage at enrichment plants around the world"; a joint venture (CATUP) plans to re-enrich some DOE tails at Urenco USA.
  - **SOURCED** (WISE Uranium, dhap991): about 560,000 t in the US by 1993; France planned 199,900 t at Bessines; "for every tonne of enriched product, about 7 tonnes of depleted uranium"; and "none of the civilian uses of depleted uranium has brought an appreciable decrease" of stockpiles.
  - **UNVERIFIED** (snippet): a DOE audit questioned plans to dispose of 551,000 tonnes of DU from the deconversion project as waste at an estimated $428 million. Over 70,000 tonnes had been converted (2010 onward).
  - The World Nuclear Association's own depleted-uranium page returned 404 at the guessed URL; not read.
- **Real uses as mass.** **SOURCED** (WISE; and summaries of an NRC document, which returned 403 so was not read directly): counterweights in aircraft (the first 550 Boeing 747s, per WISE), ballast and stabilizers in ships, balance weights for drilling tools, radiation shielding in transport casks and radiography/therapy equipment. **UNVERIFIED** (via the unreadable NRC document snippet): aircraft DU counterweights range 0.23 to 77 kg each (NUREG-1717 as cited by WISE); density 19.1 g/cm3, 68.4% denser than lead.
- **DU as balance mass or counterweight for rotating structures, tethers or space elevators: NOT FOUND in any serious source.** Two queries returned only generic counterweight literature (captured asteroids, lunar dust, debris collection; tether counterweights 1,000 to 2,000 times payload mass in one educational source, **UNVERIFIED**) and one speculative Halfbakery entry proposing a lead-coated DU counterweight (not an engineering source).
- **DERIVED scale comparison using the setting's own budget figure** (background file line 36, about 7 million tonnes for the 0.5 km2 case): 1.2 to 1.3 million tonnes of world DU would be about 17 to 19% of 7 million tonnes (1.2/7 = 0.171; 1.3/7 = 0.186). No source ties DU to that purpose.
- **Radioactivity of DU:** **SOURCED** (WISE via NUREG-1717 cite): the passenger and flight crew dose attributed to aircraft DU counterweights is less than 0.001 of their cosmic-radiation dose. Unused U-235 fuel "is not radioactive" to speak of (Primack et al. 1989, SOURCED); DU is weakly radioactive alpha emitter material (general knowledge, **UNVERIFIED** here).
- **Other heavy byproducts as mass:** not researched beyond DU. Lead, tungsten, and mine tailings are not nuclear byproducts and were not searched.

---

## Q3. Isotope power for orbital infrastructure

### 3.1 Plutonium-238

- **SOURCED** (ORNL, "Making fuel for exploring space," 8 Sep 2015): "Our objective is to stand up the capability to make 1.5 kilograms of plutonium oxide annually"; output then "a few grams, or maybe tens of grams"; about 450 targets per year at full production; feedstock neptunium-237 oxide, "originally produced at Savannah River and now stored at Idaho National Laboratory," pressed with aluminum into pellets (typically 52 per target), irradiated in HFIR at Oak Ridge or the Advanced Test Reactor at Idaho, then chemically separated in hot cells.
- **SOURCED** (DOE, 18 Jul 2023): 0.5 kg of heat-source plutonium oxide shipped Oak Ridge to Los Alamos, "the largest shipment of new heat source plutonium oxide since DOE restarted domestic plutonium-238 production over a decade ago"; DOE "remains on track to meet an 'average production target of 1.5 kilograms per year of heat source plutonium oxide by 2026.'"
- **UNVERIFIED** (snippets): ORNL capable of about 700 g/yr at HFIR; Savannah River produced about 300 kg of Pu-238 between 1959 and 1988; NASA funding about $15 million per year for the restart; a November 2025 aggregator article repeats the 1.5 kg/yr target. **NOT FOUND:** a 2025-2026 DOE statement confirming the 1.5 kg/yr rate has been reached.
- **Power per unit (UNVERIFIED: search-result text from nasa.gov and energy.gov pages, none opened):** the Multi-Mission RTG (MMRTG) holds about 4.8 kg of plutonium dioxide in eight General Purpose Heat Source modules, gives about 2,000 Wthermal (a NASA table lists 1,975) and about 110 We at launch, masses about 45 kg, degrades 3.5 to 4.8% per year (NASA RPS reference book). The 156 Wth/kg GPHS figure just below is SOURCED from Bell et al.
- **Specific thermal power** (SOURCED, Bell et al. NETS 2026, Table 1-1): the Pu-238 General Purpose Heat Source gives 250 Wth at 1.60 kg = 156 Wth/kg, half-life 87.7 years. The WNN viewpoint gives 560 W/kg for Pu-238 (SOURCED, WNN).
- **Is it extracted from spent fuel?** The route is neptunium-237, which is itself a byproduct recovered from irradiated fuel/targets (**SOURCED** ORNL 2015 for the stockpile origin at Savannah River). **UNVERIFIED** (snippet of Savannah River fact sheets): H Canyon recovered Np-237 from aluminum-clad enriched-uranium fuel tubes, finished processing neptunium solutions in 2006 to 2008 and this was "the last neptunium inventory in the United States"; the Np went to Idaho for conversion to targets. **NOT FOUND:** a source giving the Np-237 inventory in kilograms, or the Pu-238 share of commercial spent fuel.
- **DERIVED scale illustrations** (my arithmetic):
  - MMRTG thermal density: 2,000 Wth / 4.8 kg = 417 Wth per kg of PuO2.
  - The 1.5 kg/yr rate then corresponds to about 1.5 × 417 = 625 Wth of new heat source per year; at MMRTG conversion (110/2,000 = 5.5%) that is about 34 We per year of production.
  - One megawatt electric at 5.5% would need 1,000,000/0.055 = 18.2 MWth, or 18.2e6/417 = about 43,600 kg (about 44 tonnes) of PuO2, about 29,000 years at 1.5 kg/yr. (No source proposes MWe-scale radioisotope power in orbit; the arithmetic only shows scale.)

### 3.2 Americium-241 (ESA / University of Leicester / UK National Nuclear Laboratory)

- **SOURCED** (Bell et al., "Americium-Fuelled Radioisotope Stirling Generator Elegant Breadboard," NETS 2026, Univ. of Leicester and NASA Glenn):
  - Am-241 is "the fuel of choice in European Radioisotope Power Systems"; Pu-238 "is not readily available to ESA, with its production process being highly regulated and expensive."
  - European Large Heat Source (ELHS): 200 Wth from "~2 kg of 241Am fuel," mass 6.85 kg, 1,836 cm3, specific power 29 Wth/kg, half-life 432.2 years (versus the Pu-238 GPHS: 250 Wth, 1.60 kg, 156 Wth/kg, 87.7 years).
  - Am radioisotope heater unit: 3 Wth. RTGs "usually have a conversion efficiency at system level around 5-7%."
  - A four-ELHS design gives 800 Wth feeding six Stirling converters; a half-scale technology demonstrator (two ELHS, three converters, electrically heated) was tested at NASA Glenn in early 2025.
  - Programs: ESA's ENDURE; UK Space Agency support; spin-out Perpetual Atomics.
- **DERIVED:** 200 Wth / 2 kg = 100 Wth per kg of Am-241 fuel (close to the 115 W/kg pure-isotope figure below). The whole heat source is 29 Wth/kg, and the Pu-238 GPHS is 156 Wth/kg: 156/29 = 5.4 times higher per kilogram of finished heat source. Fuel-only and module-level figures should not be mixed.
- **SOURCED** (World Nuclear News viewpoint, "Can americium replace plutonium in space missions?", opened this session): Am-241 about 115 W/kg versus 560 W/kg for Pu-238; half-life 432 versus 88 years; Am-241 oxide "about $1,500 per gram"; Am-241 emits far more gamma than Pu-238; the Sellafield MOX plant could not use plutonium separated more than six years earlier because Am-241 exceeded 3%; for Curiosity "15-20 kg of Am-241 would be needed, versus 4.8 kg of Pu-238"; ESA contracted the UK NNL to recover Am-241 from civil plutonium and was "seeking only a few grams for now."
- **UNVERIFIED** (search snippets): about 250 kg of civilian plutonium per 10 kg of Am-241; Pu-241 (10 to 14% of civil Pu, half-life 14 years) decays into Am-241 so stocks gain Am as they age; UK civil plutonium stock "about 100 tonnes" at Sellafield; a Leicester 10 We RTG prototype and a design up to 50 We; a £19 million UK Space Agency-funded laboratory at Sellafield for Am separation; military plutonium is unsuitable (little Pu-241). **NOT FOUND:** a current production rate for Am-241 in kilograms per year.
- **Derived from sourced figures:** because Am-241 comes from plutonium stored from reprocessing, it is a byproduct of reprocessed civil spent fuel (SOURCED basis: NNL "chemical extraction from the UK's civil plutonium stocks," snippet **UNVERIFIED**).

### 3.3 Strontium-90 and polonium-210

- **Strontium-90 (Soviet Beta-M terrestrial RTGs). UNVERIFIED** (mirror/secondary sources only): half-life 28.8 to 29.1 years (IAEA conference abstract snippet gives 29.1); a Beta-M unit about 250 Wthermal from about 280 g of Sr-90 (1,480 TBq); a tungsten shield is shown around the strontium core; Sr-90 emits beta with no gamma, daughter Yttrium-90 also beta (so bremsstrahlung shielding is needed); up to about 1,000 such RTGs still exist, mostly in Russia; they power lighthouses and beacons; produced at Narva, Estonia. **DERIVED:** 250 Wth/280 g = 0.89 W/g (my division; the snippet did not state it). No source retrieved describes a Sr-90 RTG for space; one secondary source describes it as a ground-based choice.
- **Polonium-210. UNVERIFIED** (snippets): half-life 138.4 days; Lunokhod 1 used a polonium-210 radioisotope heater to keep the rover warm through the lunar night; about 140 W of heat per gram. **NOT FOUND:** a production rate in kilograms per year (one combined query; no production source returned). Polonium-210 is produced by neutron irradiation of bismuth-209 (general knowledge, **UNVERIFIED**; not a spent-fuel byproduct extraction).

### 3.4 Radiation, thermal and cost limits

- Conversion efficiency 5 to 7% for thermoelectrics (SOURCED, Bell et al.), hence most heat is waste heat that must be dumped; dynamic (Stirling) conversion is intended to improve this (SOURCED, Bell et al.).
- Am-241 gamma emission and the need for heavier shielding: SOURCED (WNN), no figure given.
- Cost: Am-241 oxide about $1,500 per gram (SOURCED WNN). **NOT FOUND:** a current Pu-238 price per gram from a primary source.
- Small platforms: Am-RHU 3 Wth for keeping spacecraft electronics warm (SOURCED, Bell et al.). Electrical output per unit is on the order of 10 to 110 We (Am prototype 10 We **UNVERIFIED**; MMRTG 110 We per NASA text above).

---

## Q4. Fission reactors in space

### 4.1 Flown units

- **SNAP-10A (US, 3 Apr 1965). SOURCED** (DOE Energy Technology Engineering Center SNAP overview): objective minimum 500 We, "more than 600 watts" produced shortly after launch; enriched uranium fuel, zirconium hydride moderator, liquid NaK coolant; "Following 43 days of successful operation" it shut down after a high-voltage failure in the Agena's electrical system; "500-nautical-mile orbit" and "The reactor remains in polar orbit today." Primack et al. 1989 (SOURCED) say "500 watts electric" and "1,300-kilometer orbit." **DERIVED conflict:** 500 nautical miles is 926 km (500 × 1.852), not 1,300 km; the two SOURCED values disagree and are not reconciled here. **UNVERIFIED:** expected orbital lifetime about 4,000 years (Wikipedia mirrors); a 2008 paper (Stokely and Stansbery) reports a debris cloud near 1,300 km tied to the SNAPSHOT/Agena with 50 additional cataloged pieces since 1979 (snippet).
- **Soviet RORSAT reactors (BES-5 / "Buk"). SOURCED** (Primack et al., *Science & Global Security* 1, 59-82, 1989): "at least 33" RORSAT reactors launched, "at least one" not reaching orbit; RORSATs fly at about 250 km because radar effectiveness falls off as R^-4 so a compact reactor replaces large solar panels; when finished the reactor is "supposed to be boosted to a 'nuclear safe' disposal orbit at approximately 950 kilometers"; the Cosmos 1900 reactor "apparently contained about 30 kilograms of highly enriched uranium-235, producing about 75 kilowatts of thermal power and perhaps 5 kilowatts electric"; Soviet thermionic in-core reactors in Cosmos 1818 and 1867 (1987) in 800 km orbits produced "about 10 kilowatts electric." **UNVERIFIED** (Wikipedia mirrors): BES-5 3 kWe from 100 kWth; 30 kg or more of over-90% enriched uranium-235; 31+ missions; TOPAZ fuel mass 12 kg and "5 kW for 3-5 years" for the first TOPAZ reactor.
- **SP-100 (planned, not flown). SOURCED** (Primack et al.): "2.5 megawatts [thermal]... for seven years"; "approximately 200 kilograms of highly enriched uranium-235, 40 times the 'formula quantity'..."

### 4.2 Ground-tested: Kilopower / KRUSTY

- **SOURCED** (Gibson, Poston et al., "KRUSTY Nuclear Ground Test Results and Lessons Learned," NASA Glenn/Los Alamos, NTRS 20180005435): Kilopower is "a fission reactor that could be scaled from 1 to 10 kWe"; the test at the Nevada National Security Site was completed 21 Mar 2018, "the first space reactor test completed for fission power systems in over 50 years"; objective: 4 kWt at 800 degrees C; core of highly enriched uranium (HEU) with sodium heat pipes, beryllium oxide reflectors, boron carbide control rod, lithium hydride shielding; 1 kWe design uses 8 Stirling engines of 125 W; the test used two 80 W Sunpower engines; a full-power facility run of about "28 hour[s]."
- **SOURCED** (LANL white paper "Comparison of LEU and HEU Fuel for the Kilopower Reactor," Oct 2018, from the fetched PDF): "The critical mass of HEU (93% enriched) is ~52 kg, the critical mass of LEU (20% enriched) is over 400 kgs"; "A LEU Kilopower will be 600 to 800 kg heavier than an HEU system. On a percentage basis, a 1-kWe space and lander system has a 200% increase in mass. For 10-kWe space system, the increase is 70%. For a 10-kWe Mars surface system, the increase is 40%"; a 1 kWe Moon-lander system under 700 kg with "fuel and reflectors weigh[ing] just over 100kg using HEU," versus 700 kg for fuel and reflectors alone in an LEU version; LEU would need to be down-blended from HEU; "required infrastructure to make 10's of kg's quantities of [alternative] fuels... does not exist"; HEU-versus-LEU cost difference estimated "less than 70 million dollars."
- **UNVERIFIED** (snippet, student thesis): Kilopower core mass 28 to 44 kg; gross mass about 400 kg for 1 to 3 kW and 1,500 kg for 3 to 10 kW surface systems. NASA 10 kWe analysis: the core generates roughly 43 kWt (snippet).

### 4.3 Fuel enrichment policy and whether reprocessed fuel could be used

- **SOURCED** (Physics Today, 23 Dec 2020, on Space Policy Directive-6, 16 Dec 2020): HEU use "should be limited to applications for which the mission would not be viable" with other fuels; NASA "now plans to use only low-enriched uranium (LEU) for its lunar and Martian surface reactors"; an Idaho National Laboratory study found HALEU (just below 20%) reactors "about 25% heavier than the HEU-fueled Kilopower design." Pu-238 radioisotope systems are not covered by the proliferation concern.
- **UNVERIFIED** (snippets from outlets of mixed quality): NASA and DOE signed an agreement in January 2026 to develop, fuel and ready a lunar surface reactor for launch by 2030; a draft solicitation "explicitly requires" HALEU; a 2022 solicitation sought 40 kWe for 10 years; "Lunar Reactor-1" concept 20 kWe for five years with HALEU; a 2025 Argonne study found a HALEU nuclear-thermal core only about 9% heavier than HEU (19.5% U-235); INL Oct 2025 core and reflector masses 1.9 to 2.7 t (HALEU) versus 0.9 to 2.0 t (HEU) for 300 MWt cores. DRACO's fuel: **NOT FOUND**.
- **Recycled or reprocessed uranium as space reactor fuel: NOT FOUND.** Two queries (reprocessed/recycled uranium, U-236 impurity) returned nothing on this. Both documented routes to space-reactor fuel (HEU or HALEU) are enriched uranium; the LANL paper notes LEU "would have to be down-blended from HEU."
- **Interaction with the UN Principles (see Q5):** Principle 3 as fetched reads "Nuclear reactors shall use only highly enriched uranium 235 as fuel" (SOURCED, hrlibrary.umn.edu page summary), while NASA's 2020 policy shifts to LEU. **NOT FOUND:** commentary reconciling the two.

### 4.4 Power levels and shield mass summary (all sourced above)
SNAP-10A about 0.5 to 0.6 kWe; RORSAT (BES-5) a few kWe (Cosmos 1900: about 5 kWe from 75 kWt); Soviet thermionic 10 kWe; Kilopower 1 to 10 kWe, KRUSTY test 4 kWt; SP-100 design 2.5 MWt. Shield mass: 20 to 50% of system (UNVERIFIED); gamma shield DU/W/Pb mass index 1.0 versus 1.2 to 1.7 (SOURCED, Banjac and Heger); Moon-lander 1 kWe: total system under 700 kg, reactor fuel plus reflectors just over 100 kg (SOURCED, LANL). **NOT FOUND:** a flown or tested reactor above about 10 kWe in the West; no source retrieved shows MWe-class space reactor hardware.

---

## Q5. Law and safety

- **Outer Space Treaty (1967), as summarized by pages fetched** (NASA history site reproduction; the UNOOSA URL returned 404): **Article IV**: parties may not place "nuclear weapons or any other kinds of weapons of mass destruction" in orbit, on celestial bodies, or elsewhere in space; the Moon and celestial bodies are used "exclusively for peaceful purposes." **Article VI**: states bear "international responsibility for national activities in outer space," including private ones, which need authorization and supervision. **Article VII**: a launching state or one whose territory/facility is used is liable for damage to other states or their nationals on Earth, in air space or in outer space. **Article IX**: parties must avoid "harmful contamination" of space and Earth's environment and consult before potentially harmful activities. The fetch tool paraphrased these (125-character quote limit), so the paraphrase is SOURCED but not verbatim.
- **Reactors and RTGs versus waste:** Article IV, as retrieved, concerns weapons, not reactors or radioisotope power; neither Article IV nor Article IX, as retrieved, mentions radioactive waste disposal. **NOT FOUND:** a binding instrument that explicitly bans or permits disposal of nuclear waste in space. **UNVERIFIED** (snippets): a 1992 Congressional Research Service paper says space law gives only the general Article IX contamination guidance; Dusek, "Lost in Space?", 22 Wm. & Mary Envtl. L. & Pol'y Rev. 181 (1997), and Schafer (1988) examine the legality of space waste disposal (texts not retrieved); London Convention applicability: NOT FOUND.
- **UN "Principles Relevant to the Use of Nuclear Power Sources in Outer Space," General Assembly resolution 47/68, adopted 14 December 1992, 85th plenary meeting** (SOURCED, hrlibrary.umn.edu text, via fetch summary):
  - Scope: nuclear power sources that "generate electric power on board space objects for non-propulsive purposes."
  - Principle 3: missions "shall be restricted to those space missions which cannot be operated by non-nuclear energy sources in a reasonable way."
  - Reactors: "Nuclear reactors shall use only highly enriched uranium 235 as fuel"; allowed on interplanetary missions, in sufficiently high orbits, or in low Earth orbit if moved to a sufficiently high orbit afterwards; the high-orbit criterion is that fission products decay substantially before return and collision risk is minimal.
  - Radioisotope generators: allowed on interplanetary missions or in Earth orbit if later stored in a high orbit; containment must withstand re-entry heat and forces.
  - Principle 9: launching states are "internationally liable for damage caused by such space objects or their component parts"; compensation includes "search, recovery, and clean-up" costs.
- **Liability Convention (1972) and Cosmos 954** (SOURCED, JAXA space-law page): Cosmos 954 re-entered on 24 January 1978 at about 11:53 GMT north of the Queen Charlotte Islands, debris in the Northwest Territories, Alberta and Saskatchewan; Canada's claim: C$6,041,174.70; protocol signed in Moscow 2 April 1981: C$3,000,000.00 "in full and final settlement." Canada based its claim on the Convention's Article II (absolute liability for damage on Earth's surface) and argued hazardous radioactive debris was "damage to property" and that absolute liability for nuclear space activities had become a general principle of international law, citing OST Article VII. **UNVERIFIED** (snippets): Operation Morning Light recovered about 65 kg of debris from a 600 km path over a search area above 124,000 km2; Canada's first-phase costs C$12.0 million, C$4.4 million included in the claim; one law-review source says the claim was in US dollars (currency conflict not resolved).
- **IAEA/UN safety framework: UNVERIFIED** (the direct PDF at unoosa.org returned 404; snippet summaries only): "Safety Framework for Nuclear Power Source Applications in Outer Space," developed jointly by the UN COPUOS Scientific and Technical Subcommittee's working group and the IAEA, adopted by the Subcommittee at its 46th session in February 2009; applies to radioisotope power systems (RTGs, heater units) and reactor systems for power and propulsion; generic, goal-based; the working group's 2023 review recommended possible enhancements to technical content and scope. Its text on waste disposal: **NOT FOUND** (document not opened).

---

## Q6. Launching waste to space; radioactive material already in orbit

### 6.1 The 1970s-80s NASA/DOE studies

- **SOURCED. "Study of extraterrestrial disposal of radioactive wastes. Part 1: Space transportation and destination considerations," R. L. Thompson, J. R. Ramler, S. M. Stevenson, NASA Lewis, 1 April 1974** (NTRS 19740014663; OCR of the scanned PDF):
  - "The currently planned Space Shuttle was found to be more cost-effective than current expendable launch vehicles by about a factor of 2"; the shuttle needs a third stage (reusable tug or expendable Centaur).
  - Destinations judged best candidates: high Earth orbits (between geostationary and lunar altitude), solar orbits (such as a 0.90 AU circular orbit), or direct injection to solar system escape. Earth orbits and solar orbits have "uncertainties regarding orbit stability and waste package integrity for times of the order of a million years." High Earth orbit "cannot now be considered a permanent disposal site... should only be considered a temporary storage site."
  - Delta-v: direct solar system escape from a 185 km Earth parking orbit: 8.75 km/s; about 20 years to reach Pluto's mean distance; "over a million years" to the nearest stars. Escape "requires two or three space tugs in tandem" and the system cost "is about four times higher than for the high Earth orbit or solar orbit destinations." Direct solar impact "requires an extremely high delta-v... far beyond the capability of current or planned launch systems... considered impractical"; a Jupiter swing-by route reduces the requirement to near escape level but "the launch opportunity is limited to perhaps 40 days once every 13 months."
  - Failure concern: all destinations beyond Earth have an "abort gap" during the departure burn; if propulsion fails "at or beyond Earth-escape velocity, the waste package will be left in an unplanned solar orbit," with "a high probability of eventually reencountering the Earth."
  - Costs: shuttle cost per kilogram "of the order of one-half" that of expendables; one configuration at "$1,750 per kilogram ($800 per lb)" (1974 dollars). Destinations like the Moon, planets and asteroids were not studied; stated arguments against them: landing failure contamination, scientific interest, future value, limited launch opportunities, high retropropulsion delta-v.
- **SOURCED. DOE Final Environmental Impact Statement on commercial waste, 1980 (DOE/EIS-0046F), chapter 1 text via OCR, section 1.4.8 "Space Disposal Concept," and the May 1981 Record of Decision:**
  - Reference concept: high-level waste in a ceramic-metal matrix, flight containers, "a solar orbit, where it would be expected to remain for at least one million [years]."
  - "once the waste is placed in orbit its potential for environmental impacts and human health effects is judged to be nonexistent. However, the risk of launch pad accidents and low earth orbit failures have not been determined."
  - "The space disposal option appears feasible for selected long-lived waste fractions or radionuclides such as iodine-129 [and technetium-99], or even for the total amount of reprocessed high-level waste that will be produced. Space disposal of unreprocessed fuel rods and other high volume wastes does not appear economically feasible or practical because of the large number of flights involved."
  - Decision: "While not a viable alternative for the disposal of all high-level wastes, the Department has concluded that space disposal may be profitably studied for its application to special disposal concerns, e.g., more remote isolation of long lived and environmentally mobile radionuclides such as Tc-99 and I-129." The proposed action "does not preclude" selective space disposal. The primary program was mined geologic repositories.
- **SOURCED. Battelle/NASA "Preliminary Risk Assessment for Nuclear Waste Disposal in Space," Rice, Denning, Friedlander, February 1982** (NTRS 19820017396 executive summary, OCR): three conclusions: (1) "Preliminary estimates of space disposal risk are low, even with the estimated uncertainty bounds"; (2) "If calculated MGR [mined geologic repository] release risks remain low... and the EPA requirements continue to be met, then no additional space disposal study effort is warranted"; (3) "If risks perceived by the public are significant in the acceptance of mined geologic repositories, then consideration of space disposal as an MGR complement is warranted." Its model counted "only single-point failures for space transportation booster systems (Space Shuttle)"; reference concept 750 missions. Launch-failure probability table: **NOT FOUND** (table present but numbers not legible in OCR).
- **SOURCED. NASA-DOE follow-on, "Space Systems for the Disposal of Nuclear Waste, Follow-on Study, Vol. 1 Executive Summary" (NASA-CR-161991, 1982; Boeing, June 1981 to February 1982; OCR) and "Analysis of Space Systems Study... Vol. 2" (NASA-CR-161888, 1981; abstract):**
  - Destination: 0.85 AU heliocentric orbit; the reference waste was the cermet high-level waste mix "with 95% of the cesium and strontium removed"; "the only one of the three [waste mixes] that showed the potential for long-term risk reductions when compared to mined geologic repository."
  - Waste-generation basis: "a 4480-MTHM/year rate of high-level waste generation." Reference cermet mission: "approximately 27,000t over 10 years" to LEO (OCR digits; read as 27,000 t); technetium plus iodine "approximately 2,000t over 10 years." Cermet billet packing efficiency "slightly under 75%" raises flights by 20%. Life-cycle cost figures read from OCR charts: cermet program savings about $4 billion with the best launch pairing; the low-rate technetium/iodine case about $1 billion with the existing shuttle. (Chart values noisy; the 1980 cost per kilogram: **NOT FOUND**.)
  - Vol. 2 abstract: no concept "significantly cheaper than the reference concept."
  - Program status in 1982: "sustaining-level assessment" meant to "maintain a low level of research activity... to provide a baseline for future development should a decision be made to increase the emphasis."
- **UNVERIFIED** (UK CoRWM/NNC 2004 report, via snippet only; the document itself returned HTML): shuttle launch cost $100 to $500 million; about 5,000 kg radioactive waste in a 45,000 kg payload; about 910 launches for predicted high-level waste. A 1974 Nuclear Technology paper favored space disposal of transuranics only; a forum recollection of "1 in 10,000" catastrophic failure is not a verified figure.
- **Space Studies Institute paper (Coopersmith, "Disposal of High-Level Nuclear Waste in Space," SSI Space Manufacturing 12, 1999; SOURCED, extracted text):** proposes ground-based launchers (electromagnetic launchers, mass drivers "fueled by lunar material," gas guns, laser propulsion) because most of the system mass stays on the ground; "What could engineers develop if asked to launch 10,000 tons annually?"; low-speed propulsion (solar sails, electric rockets, mass drivers) would suit non-urgent disposal; destinations include solar orbits inside Venus's orbit, Earth-Moon libration points, lunar landings, outside the solar system; reasons given for why it has not been adopted: "Two major public concerns will dominate future discussions -- safety and cost"; key safety demonstrations would be required (exploding a launch vehicle with a mock cargo, a re-entry capsule test). Satellite launch cost then $2,000 to $10,000 per pound. It states NASA Lewis concluded feasibility in 1974 and the AIAA Space Systems Technical Committee endorsed it in 1981.
- **UNVERIFIED** (snippet, abstract only): Rossetti and Smith, JBIS 2025: about £2,460/kg on Falcon Heavy and £520/kg on Starship; about 75 and 25 launches per year for global high-level waste; destination Jupiter. Full paper unavailable (UCL page returned 403).
- **What a cheap one-directional launcher would change:** no source retrieved models a mass driver or space-elevator launch of waste with costs. The nearest sourced statements are Coopersmith's argument above (tonnage demand as a market for cheap launch; ground-based launchers keep most mass on the ground) and the 1974/1980-82 results that the delta-v to solar escape (8.75 km/s from LEO) and the abort gap are the drivers of cost and risk. **DERIVED from the sourced Earth-orbit-to-escape figure:** a launcher that places mass in LEO cheaply still leaves roughly 8.75 km/s to be supplied by the waste package's own stages for solar escape (the 1974 figure, 185 km parking orbit). The delta-v to place waste in a (lower-energy) high Earth orbit was not sourced here as a number.

### 6.2 Radioactive material already in orbit, and its persistence

- **RORSAT reactors and sodium-potassium (NaK) coolant. SOURCED** (NASA ORDEM2010 modeling slides, NTRS 20100006950, text extracted; and Primack et al. 1989):
  - 16 RORSATs ejected their fuel cores at end of mission, releasing liquid NaK coolant that formed droplets; "One out of the 16 RORSATs failed to reach the normal disposal orbit region of 900-1000 km and was placed in a lower orbit (~700 km altitude)."
  - The droplets are conducting spheres giving highly polarized radar returns, nearly circular orbits at about 65 degrees inclination, altitude below about 1,000 km; model populations are derived from Haystack radar data; the NASA NaK module treats droplets of size 5.5 mm and larger. The slides' own text dates the Cosmos 954 re-entry "in 1980"; other sources (JAXA, Primack) say 24 January 1978, so the slide has an error.
  - Disposal-orbit persistence: "re-entry will not normally occur for several hundred years, by which time most of the radioactivity will have decayed" (Primack et al.).
  - **UNVERIFIED** (snippets): ESA MASTER-2005 estimate about 45,000 droplets in orbit in May 2005, droplets up to about 5.5 cm (the ORDEM slides use a 5.5 mm size threshold; the two differ and are not reconciled); an AMOS 2023 poster says the original count was roughly a million droplets, most decayed by the 1990s; a 1999 study (Rossi and Anselmo) found NaK droplets cannot catastrophically fragment large targets.
  - **Note:** the NaK is coolant, not fuel; the radioactive fuel cores were boosted to the higher orbit. A reactor that ran (neutron activation of coolant) can make coolant slightly radioactive: no source retrieved quantifies this.
- **Cosmos 954 / 1402 / 1900. SOURCED** (Primack et al. 1989): Cosmos 954 re-entered 24 January 1978 "spreading radioactive debris over northern Canada"; after the reactor boost system on Cosmos 1402 failed, "a new system was used to eject the fuel core, which disintegrated in the upper atmosphere over the South Atlantic Ocean on 7 February 1983"; Cosmos 1900 lost radio contact April 1988, an automatic backup boosted the reactor to a high orbit on 30 September 1988 "shortly before the satellite's expected re-entry"; "Counting Cosmos 954, 1402, and 1900, as well as the one or two RORSAT launch failures, the accident rate for RORSATs is about 15 percent." Also: the accumulation of long-lived fission products "is approximately proportional to its thermal power level multiplied by its operating lifetime."
- **SNAP-10A in orbit:** see 4.1.
- **Persistence of other orbits:** **UNVERIFIED** (snippet): a tracking page lists Cosmos 402 (1971) still in orbit at 990 km with a BES-5 reactor.
- **NOT FOUND:** a measured activity (becquerels) for the NaK droplets or for reactors in the 900 to 1,000 km disposal orbits.

---

## Q7. Other orbital-construction uses

- **Food sterilization by irradiation: SOURCED in principle, but on the ground.** Search results (inverse.com; a NASA food page; FDA dispensation) say NASA astronauts eat foods irradiated to sterility and that Apollo 12 through 17 carried irradiated bread, shelf-stable at room temperature, and that NASA has FDA dispensation to irradiate to commercial sterility. All **UNVERIFIED** (snippets; not opened). The sources describe irradiation done before launch, not in orbit. **NOT FOUND:** radiation sterilization (gamma or electron-beam) carried out on an orbital platform.
- **Space-based isotope production: UNVERIFIED** (patent US20220367077A1, Google Patents / Justia snippet): a proposal for a space-borne charging station using a reactor or other neutron source to activate material on client spacecraft, so spacecraft launch without radioactive material; described as a patent proposal, not a demonstrated system.
- **Thermal management:** radioisotope heater units keep electronics warm (Am-RHU 3 Wth, SOURCED, Bell et al.; Lunokhod Po-210 heater, UNVERIFIED snippet). Waste heat from radioisotope generators can be circulated by a pumped fluid loop (SOURCED, Bell et al.: "The Am-RTG can also dissipate heat throughout a spacecraft by using its integrated pumped-fluid loop system").
- **Power for in-orbit industry:** no source retrieved on reactor power for an orbital factory (one combined query, nothing returned). The Primack et al. paper (1989) considers reactors for military satellites and SDI. **NOT FOUND** for industry.
- **Other:** the Coopersmith paper (Q6) proposes that waste disposal demand could finance a cheap launch system, the only source retrieved that links nuclear waste to space infrastructure; it concerns launch cost, not building material.

---

## FINAL

**What the sources support (SOURCED):**
- Hydrogen-rich materials are better GCR shields per unit mass than aluminum, and lead is the least efficient material in the 1994 NASA comparison: behind 30 g/cm2 of lead the iron flux falls by a factor of 3, versus several orders of magnitude behind the same mass of liquid hydrogen, and lead raises neutron, proton and helium fluxes through target fragmentation (TP-3473). Aluminum shows a modeled dose minimum near 20 to 30 g/cm2 with a rise for thicker shields from secondary neutrons; polyethylene does not (Norman et al. 2017). Tantalum/tungsten layers help against trapped electrons and gave slight GCR gains with 5 g/cm2 polyethylene but were detrimental in a solar-event case (Atwell et al. 2013).
- High-Z (depleted uranium, tungsten, lead) is the mass-optimal choice for gamma shadow shields at reactors: DU index 1.0, W and Pb 1.2 to 1.7 (Banjac and Heger 1994); Kilopower uses lithium hydride plus tungsten.
- Depleted uranium stock: about 1.2 to 1.3 million tonnes worldwide (snippet level); about 500,000 to 700,000 tonnes in the US (OSTI roadmap; WNN); real uses are small (counterweights, ballast, shielding).
- Isotope power: Pu-238 production is on the order of a kilogram per year (target 1.5 kg PuO2/yr, DOE 2023); Am-241 heat source 200 Wth from about 2 kg at 29 Wth/kg of the heat source, from civil plutonium stocks; conversion efficiency 5 to 7%.
- Reactors: SNAP-10A (over 600 We, 43 days), RORSATs (about 5 kWe class, about 30 kg HEU), KRUSTY (4 kWt, HEU, 2018); all flown or tested units burned enriched uranium, and the 1992 UN Principles say reactors "shall use only highly enriched uranium 235." LEU adds 600 to 800 kg (70% at 10 kWe) to a Kilopower unit.
- Law: OST Article IV bars nuclear weapons/WMD in orbit; Articles VI, VII and IX govern responsibility, liability and contamination; UN Principles 47/68 limit reactors to interplanetary or sufficiently high orbits and make launching states liable; Cosmos 954 produced the only Liability Convention claim (C$6.04 million claimed, C$3 million paid, 1981).
- Space disposal of waste: studied 1973 to 1982 by NASA/DOE; best destinations were high Earth orbit (temporary), 0.85 to 0.9 AU solar orbit, or solar escape (8.75 km/s from LEO; about four times the system cost); the 1980 DOE EIS found it feasible for long-lived fractions (Tc-99, I-129) or reprocessed high-level waste but "not economically feasible or practical" for unreprocessed fuel because of the number of flights; the 1982 risk study found risk "low" and concluded no additional effort is warranted if repository risks stay low.

**What the sources do not support / have nothing on:**
- No source proposes depleted uranium, vitrified waste or spent fuel as habitat or spacecraft shielding, or DU as counterweight for rotating structures or tethers (only one speculative Halfbakery entry).
- No source shows that reprocessed or recycled uranium fuel has been used or studied for space reactors.
- No source models a mass driver or space elevator for waste with a cost per kilogram.

**NOT FOUND (queries in the log):** Am-241 production rate (kg/yr); Pu-238 price; Np-237 inventory in kg; Po-210 production rate; 1982 launch-failure probabilities (numbers illegible in OCR); the 1980 study's cost per kilogram; the IAEA Safety Framework's own text on waste; any legal text addressing waste disposal in space specifically; activity of NaK droplets; radiation sterilization in orbit; reactor power for orbital industry; DRACO fuel; the UNOOSA-hosted treaty and principles pages (404).

**Surprises.** (1) The mass-optimal gamma shield for a space reactor is depleted uranium, a waste-stream material, but in the cosmic-ray comparison lead, the same class of material, was the worst shield per unit mass. (2) The UN 1992 Principles require HEU for reactors while NASA's 2020 policy moves to LEU. (3) The 1980 DOE EIS ruled out unreprocessed fuel because of flight count, and still left selective space disposal of Tc-99 and I-129 open. (4) Two sourced figures for SNAP-10A's orbit disagree: 500 nautical miles (926 km) in the DOE page and 1,300 km in Primack et al. 1989.

---

## Search log

Tool names: WS = WebSearch (standard mode), WF = WebFetch, SH = shell (local extraction of already-downloaded or curl-fetched PDFs; no search). "Died at the source" means the query worked but the document could not be read; "died at the query" means results did not contain it. Approximate web-call count: 41 searches and 43 fetches/downloads (about 84, slightly above the brief's 60 to 80 guideline to finish the legal and risk threads).

| # | Tool | Exact query or URL | Result |
|---|------|--------------------|--------|
| 1 | WS | galactic cosmic ray shielding effectiveness per unit mass polyethylene aluminum hydrogen-rich materials NASA | Partial: qualitative; no per-mass numbers |
| 2 | WS | high-Z shielding lead tungsten secondary neutron production galactic cosmic rays increases dose spacecraft | Partial: mechanism supported; tungsten absent |
| 3 | WS | depleted uranium spacecraft shielding proposal radiation shield space | Partial: reactor shield uses only; no spacecraft proposal |
| 4 | WS | space disposal of nuclear waste NASA DOE study 1970s solar system escape shuttle risk cost per kilogram | Hit: NTRS reports |
| 5 | WF | ntrs.nasa.gov/api/citations/19740014663/downloads/19740014663.pdf | Died at the source (scanned image PDF); recovered via local OCR |
| 6 | WF | ntrs.nasa.gov/api/citations/19820017397/downloads/19820017397.pdf | Died at the source (size limit 10 MB) |
| 7 | WF | ntrs.nasa.gov/citations/19740014663 | Hit (abstract) |
| 8 | WF | ntrs.nasa.gov/citations/19820004016 | Hit (abstract of NASA-CR-161888 Vol. 2) |
| 9 | WS | why space disposal of nuclear waste rejected DOE 1981 Shuttle Challenger cost launch failure reprocessing waste only fraction actinides | Partial |
| 10 | WF | ntrs.nasa.gov/api/citations/19820014142/downloads/19820014142.pdf | Hit after OCR (NASA-CR-161991 executive summary) |
| 11 | WS | DOE Final Environmental Impact Statement Management of Commercially Generated Radioactive Waste 1980 space disposal alternative dismissed reasons | Hit: located FEIS and ROD |
| 12 | WF | laka.org/docu/boeken/pdf/6-01-5-59-04.pdf | Died at the source (returned a catalogue HTML page; also confirmed by `curl`, 45 KB HTML) |
| 13 | WF | curie.pnnl.gov/.../doe_repository_rod_plus_eis_ch1_1981s.pdf | Died at the source (scanned); recovered via OCR (section 1.4.8, ROD) |
| 14 | WS | space disposal nuclear waste "launch" failure rate Shuttle Challenger 1986 ended NASA DOE study high-level waste Pu-239 actinides removal "space disposal" | Partial; no Challenger link found |
| 15 | WS | Wilson Nealy shielding material aluminum lead polyethylene GCR dose equivalent per g/cm2 HZETRN comparison NTRS | Hit: located TP-3473 |
| 16 | WF | ntrs.nasa.gov/citations/20140002469 | Hit (abstract) |
| 17 | WF | ntrs.nasa.gov/api/citations/19950010497/downloads/19950010497.pdf | Died at the source (scanned); recovered via OCR (TP-3473) |
| 18 | WF | ntrs.nasa.gov/api/citations/20170005580/downloads/20170005580.pdf | Died at the source (compressed streams); recovered via local text extraction |
| 19 | WF | wx1.ans.org/pubs/journals/nt/a_35048 | Hit (Banjac and Heger abstract) |
| 20 | WS | depleted uranium stockpile tonnes worldwide enrichment tails inventory DUF6 United States 700,000 tonnes | Hit |
| 21 | WS | depleted uranium uses counterweight ballast aircraft keel yacht radiation shielding density 19.1 g/cm3 World Nuclear Association | Partial |
| 22 | WF | world-nuclear.org/.../depleted-uranium | Died at the source (404) |
| 23 | WF | nrc.gov/docs/ML2006/ML20062J141.pdf | Died at the source (403) |
| 24 | WS | World Nuclear Association "Uranium and Depleted Uranium" stockpile tonnes tails uses | Partial: snippets only |
| 25 | WF | osti.gov/biblio/885886 | Hit (abstract) |
| 26 | WF | wise-uranium.org/dhap991.html | Hit |
| 27 | WF | world-nuclear-news.org/articles/heads-up-on-new-tails-partnership | Hit |
| 28 | WS | tether counterweight mass depleted uranium OR "dense material" ballast space tether OR rotating space station balance mass proposal | Miss: died at the sources (no DU proposal exists in results) |
| 29 | WS | "depleted uranium" "space elevator" OR "orbital tether" OR "space station" counterweight OR "radiation shield" OR "ballast" | Miss for serious sources; one Halfbakery entry |
| 30 | WS | NASA plutonium-238 production rate ORNL 1.5 kilograms per year goal neptunium-237 target irradiation HFIR 2024 | Hit |
| 31 | WS | ESA americium-241 radioisotope thermoelectric generator Leicester power output watts per kg recovered from civil plutonium reprocessing | Hit |
| 32 | WF | ntrs.nasa.gov/api/citations/20260002867/downloads/Bell_CP_10393-Am-RSG_NETS2026_20260002867.pdf | Died at the source (compressed); recovered via local text extraction |
| 33 | WF | ornl.gov/news/making-fuel-exploring-space | Hit (first 100,000 of 238,916 characters read) |
| 34 | WS | strontium-90 RTG Beta-M lighthouse Soviet power watts half-life 29 years heat 0.46 W/g space unsuitable; polonium-210 Lunokhod heater half-life 138 days | Partial: Wikipedia-derived |
| 35 | WS | UK civil plutonium stockpile 140 tonnes americium-241 ingrowth kilograms available for space power National Nuclear Laboratory Sellafield | Partial |
| 36 | WF | world-nuclear-news.org/articles/can-americium-replace-plutonium-in-space-missions | Hit |
| 37 | WF | unoosa.org/pdf/pres/stsc2015/tech-15E.pdf | Died at the source (404) |
| 38 | WF | rps.nasa.gov/power/radioisotope-power-systems/ | Redirect (301) |
| 39 | WF | science.nasa.gov/planetary-science/programs/radioisotope-power-systems/ | Partial (no figures) |
| 40 | WS | DOE Pu-238 production 2025 ORNL Savannah River kilograms per year milestone plutonium-238 supply NASA Dragonfly | Partial; the snippet's "early 2025" shipment date was wrong (DOE page: 18 Jul 2023) |
| 41 | WF | energy.gov/node/4831221 | Hit |
| 42 | WS | MMRTG multi-mission radioisotope thermoelectric generator 110 watts electrical ... NASA fact sheet (allowed domains nasa.gov, energy.gov, etc.) | Hit (snippet level; pages not opened) |
| 43 | WS | SNAP-10A reactor 1965 orbit 590 kg 43 kWt 500 We HEU ... BES-5 TOPAZ 5 kWt 3 kWe 30 kg U-235 | Partial: mirrors; my query's figures were wrong (43 is days) |
| 44 | WF | energy.gov/etec/system-nuclear-auxiliary-power-snap-overview | Hit |
| 45 | WS | Kilopower KRUSTY test 2018 1 kWe 4 kg uranium-235 HEU U-8Mo core 28 hours results NASA Los Alamos | Hit: located papers |
| 46 | WF | ntrs.nasa.gov/api/citations/20180005435/downloads/20180005435.pdf | Died at the source; recovered via local text extraction |
| 47 | WS | NASA fission surface power 40 kWe lunar reactor 2030 HALEU Directive 2025 100 kWe industry proposals ... | Partial: aggregators |
| 48 | WS | space nuclear reactor fuel HALEU versus HEU low-enriched uranium cermet nuclear thermal propulsion DRACO fuel enrichment 19.75% analysis | Partial; DRACO fuel NOT FOUND |
| 49 | WS | Kilopower reactor core HEU U-235 mass kg 10 kWe 1500 kg total mass shield lithium hydride tungsten gamma shield mass | Partial |
| 50 | WF | osti.gov/servlets/purl/1477618 | Died at the source (compressed); recovered via local text extraction (LANL LEU/HEU white paper) |
| 51 | WF | ntrs.nasa.gov/api/citations/20180005553/downloads/20180005553.pdf | Died at the source (size limit) |
| 52 | WF | unoosa.org/oosa/en/ourwork/spacelaw/principles/nps-principles.html | Died at the source (404) |
| 53 | WF | unoosa.org/oosa/en/ourwork/spacelaw/treaties/outerspacetreaty.html | Died at the source (404) |
| 54 | WS | Principles Relevant to the Use of Nuclear Power Sources in Outer Space General Assembly resolution 47/68 text Principle 3 nuclear reactors sufficiently high orbit | Hit: located hrlibrary page |
| 55 | WS | Outer Space Treaty 1967 Article IV text "nuclear weapons or any other kinds of weapons of mass destruction" "celestial bodies" unoosa.org | Hit: NASA history copy |
| 56 | WF | hrlibrary.umn.edu/resolutions/47/68GA1992.html | Hit (paraphrase, 125-character quote limit) |
| 57 | WF | nasa.gov/history/SP-4225/documentation/cooperation/treaty.htm | Hit (paraphrase) |
| 58 | WS | Safety Framework for Nuclear Power Source Applications in Outer Space 2009 IAEA UN COPUOS joint report scope reactors radioisotope | Partial |
| 59 | WF | unoosa.org/pdf/publications/iaea-nps-sfrmwrkE.pdf | Died at the source (404) |
| 60 | WS | Cosmos 954 Canada claim Liability Convention 1978 C$6 million settlement 1981 C$3 million Operation Morning Light recovered radioactive debris | Hit |
| 61 | WF | jaxa.jp/library/space_law/chapter_3/3-2-2-1_e.html | Hit |
| 62 | WS | NaK droplets RORSAT reactor coolant leaked debris cloud orbital debris population 70,000 particles 1 to 6 cm ORDEM NASA Orbital Debris Quarterly News | Partial; my 70,000 figure not confirmed |
| 63 | WS | RORSAT reactor cores boosted to disposal orbit 950 km altitude 600 years Cosmos 1402 reentry 1983 core Atlantic Ocean Soviet nuclear reactor satellites in orbit number of reactors | Hit (600 years not supported; "several hundred years") |
| 64 | WF | ntrs.nasa.gov/api/citations/20100006950/downloads/20100006950.pdf | Died at the source; recovered via local text extraction |
| 65 | WF | scienceandglobalsecurity.org/archive/sgs01primack.pdf | Partial; recovered via local text extraction (Primack et al. 1989) |
| 66 | WS | vitrified high-level waste glass OR spent nuclear fuel as radiation shielding material for spacecraft or space habitat proposal | Miss for nuclear waste; related Soilleux (silicates) |
| 67 | WS | lunar mass driver launch nuclear waste disposal in space cheap launch cost per kg analysis Starship 2020s feasibility reprocessing actinides | Partial |
| 68 | WF | nss.org/.../Space-Manufacturing-conference-12-111-Disposal-Of-High-Level-Nuclear-Waste-In-Space.pdf | Died at the source (binary); recovered via local text extraction |
| 69 | WF | discovery.ucl.ac.uk/id/eprint/10219285 | Died at the source (403) |
| 70 | WS | neptunium-237 recovered from spent nuclear fuel reprocessing Pu-238 source Np-237 inventory kilograms Savannah River H-Canyon; plutonium-238 content in spent fuel percent | Partial; inventory NOT FOUND |
| 71 | WS | space nuclear reactor fuel reprocessed OR recycled uranium impurities U-236 feasibility; lunar fission surface power fuel enrichment LEU HALEU decision 2026 | Partial; recycled-fuel part NOT FOUND (query-level miss) |
| 72 | WF | inl.gov/fsp/ | Died at the source (403) |
| 73 | WF | physicstoday.aip.org/news/no-bomb-grade-uranium-in-space-says-white-house | Hit |
| 74 | WF | ntrs.nasa.gov/api/citations/20140002469/downloads/20140002469.pdf | Died at the source; recovered via local text extraction |
| 75 | WS | lunar regolith shielding galactic cosmic rays dose reduction g/cm2 compared water polyethylene aluminum habitat 3 meters regolith NASA study | Partial |
| 76 | WS | strontium-90 radioisotope thermoelectric generators Soviet Union Russia IAEA number of RTGs specific thermal power W/g half-life 28.8 years bremsstrahlung shielding | Partial |
| 77 | WS | in-space manufacturing radioactive isotope source OR "radiation sterilization" OR "gamma irradiation" orbital platform OR space station industry nuclear byproduct use | Miss (query level) except patent |
| 78 | WS | SNAP-10A fragmentation debris 1979 2008 Agena NaK orbit 1300 km reactor remains orbital debris events NASA Orbital Debris Quarterly News | Partial |
| 79 | WS | NASA food irradiation astronauts sterilized meals radiation sterilization space food; space station power generator reactor industrial park orbital factory nuclear power study | Partial (food half only) |
| 80 | WS | Rice Denning Battelle "Space Disposal of Nuclear Waste" risk assessment launch failure probability shuttle abort dose NASA CR 1982 ntrs | Hit: located NTRS 19820017396/7 |
| 81 | SH | curl of ntrs.nasa.gov/api/citations/19820017396/downloads/19820017396.pdf, then pdftotext/tesseract | Hit after OCR (size limit on WF, not a block) |
| 82 | WS | legal status disposal of nuclear waste in outer space Outer Space Treaty Article IX harmful contamination London Convention space law obstacle | Partial: London Convention NOT FOUND |

Notes on the log: items 5, 6, 12, 13, 17, 18, 32, 46, 50, 64, 68, 74 were scanned or compressed PDFs that the fetch summarizer could not read; where the PDF was saved by the tool, it was read locally with `pdftotext` or `tesseract` (not a workaround of any block). Item 12's PDF address returned HTML; no further attempt was made. No refusals by the search tool occurred.
