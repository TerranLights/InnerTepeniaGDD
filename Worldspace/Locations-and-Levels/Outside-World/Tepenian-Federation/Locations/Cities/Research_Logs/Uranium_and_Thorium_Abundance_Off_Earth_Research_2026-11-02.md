# Uranium and thorium abundance off Earth, and whether anyone could mine it (Unit R9, 2026-11-02)

**Started:** 2026-11-02 18:30. **Ended:** 2026-11-02 18:45 (clock read at the end).

**Scope.** Facts only, no recommendation. The question behind the unit: could the reason people go to Mercury and the inner solar system be uranium? This file collects measured and modeled uranium and thorium abundances for Mercury, Venus, the Moon, Mars and meteorites; Earth's ore grades, resources, production, seawater and thorium for scale; the geological processes that concentrate uranium; the arithmetic of mining dilute rock; and launch and solar-power figures for the space-transport side.

**Label rules used.** SOURCED = I read it in the source document or page itself during this session (a downloaded PDF, a fetched page, a database record). DERIVED = my arithmetic on sourced figures, with the working shown. UNVERIFIED = seen only in a search-result summary or snippet, recalled, or inferred. NOT FOUND = looked for, queries listed in the log. Note on the tools: the web-fetch tool summarizes pages through a small model, so a number read from a fetched page is marked SOURCED only where I could also check it in a downloaded document or where the page is the primary publisher; otherwise the fetched-page items carry "(fetched page, summarized)".

**Read first (existing notes, not copied):** `mercury_as_industrial_site.md` (Th 0.155 ± 0.054 ppm, U 90 ± 20 ppb, Nittler et al. 2018 Table 2.1), `mercury_whole_planet_inventory_and_extraction.md`, `venus_as_extraction_site.md`. I did not read the graph index or any city-culture file.

---

## PROGRESS

- [x] Q1 Mercury (GRS K, Th, U; uncertainty; spatial variation; K/Th and K/U; radon caveat; enrichment arguments; bulk-silicate models)
- [x] Q2 Venus (Venera 8, Vega 1 and 2 with uncertainties; Venera 9 and 10 values NOT FOUND; rock types; surface conditions; concentration processes)
- [x] Q3 Moon, Mars, asteroids and meteorites (KREEP Th and U; Mars Th and K; chondrite U and Th table; claims)
- [x] Q4 Earth for scale (crust, ore grades, Red Book totals, production, seawater, phosphate, thorium) — Olympic Dam, Cigar Lake, McArthur River grades only from snippets
- [x] Q5 Concentration processes (partly: the water/oxygen/tectonics dependence is mostly my reading of the deposit-type table, labeled DERIVED/UNVERIFIED)
- [x] Q6 Scale and economics (derived tables; published low-grade studies only partly reached)
- [x] Q7 Space-transport side (escape velocities, delta-v, mass-driver energy, solar flux by distance; Mercury and tether launch studies NOT FOUND)

---

## Q1. Mercury

### 1.1 What the MESSENGER Gamma-Ray Spectrometer measured

- **Original result (Peplowski et al. 2011, Science 333, 1850-1852).** Northern-hemisphere averages: K 1150 ± 220 ppm, Th 220 ± 60 ppb, U 90 ± 20 ppb. UNVERIFIED (abstract text as quoted in search results from the Smithsonian and Arizona repositories; the full paper pages returned HTTP 403). The same numbers are quoted in the Icarus paper of Pirotte et al. 2023 (SOURCED, downloaded PDF): "220 ± 60 ppb Th and 90 ± 20 ppb U (Peplowski et al., 2011)". The conference version (EPSC-DPS 2011-1170, SOURCED, downloaded) used only the first 30 days of orbital data covering "about half of the northern hemisphere" and summed low-altitude spectra with a total acquisition time of 3,300 s (measurements below 2,000 km altitude; the orbit is highly elliptical and near-polar, so GRS coverage is "restricted to regions in the northern hemisphere").
- **Later compilation (Nittler, Chabot, Grove, Peplowski, "The Chemical Composition of Mercury," chapter 2 of *Mercury: The View after MESSENGER*, 2018; arXiv 1712.02187, SOURCED, downloaded and read).** "The GRS has also provided measurements of the absolute concentrations of the naturally radioactive elements Th and U, which have mean northern hemisphere averages of 155±54 and 90±20 ppb, respectively." Table 2.1 of that chapter: K 1288 ± 234 ppm (average), range 240-2500 ppm; Th 0.155 ± 0.054 ppm; U 90 ± 20 ppb; K/Th 8000 ± 3200.
- **Discrepancy to note.** The 2011 Th value (220 ± 60 ppb) and the 2018 chapter value (155 ± 54 ppb) differ, and the K averages differ (1150 versus 1288 ppm), so K/Th is 5200 ± 1800 in the 2011-2012 papers and 8000 ± 3200 in the chapter. I did not find the paper that explains the revision (NOT FOUND; see log). Both sets of uncertainties overlap at about 1 sigma for Th (220 - 155 = 65, versus combined sigma of about 81 ppb, DERIVED).
- **Th/U.** The chapter says "Mercury's Th/U ratio of about 2" (SOURCED); 155/90 = 1.7 and 220/90 = 2.4 (DERIVED). Pirotte et al. 2023 give surface Th/U = 2.5 ± 0.9 (SOURCED, downloaded PDF).
- **Gamma-ray instrument limits.** The chapter states that Th and U "have larger statistical errors and are more susceptible to systematic uncertainties than the major elements," and that the germanium cooler failed about 14 months into orbit (UNVERIFIED, from a search summary of the chapter; the table's uncertainties are SOURCED).

### 1.2 Spatial variation

- **Coverage:** northern hemisphere only (SOURCED, EPSC abstract). No southern-hemisphere Th or U map exists in what I found (NOT FOUND for any global Th or U map).
- **Potassium varies; thorium shows little variation.** Peplowski et al. 2012 (JGR Planets 117, E00L04, doi 10.1029/2012JE004141), UNVERIFIED (abstract text only, via search results; the ADS page returned HTTP 405): K ranges "from 300 to 2400 ppm"; "the lack of a significant variation in the measured Th abundances suggests that there may be considerable variability in the K/Th abundance ratio over the mapped regions"; regions included the northern smooth plains and the plains inside the Caloris basin; K correlates with surface-temperature models, suggesting a temperature-related process controls surface K and supplies the exosphere. The chapter's K range 240-2500 ppm (SOURCED) matches.
- **Northern smooth plains.** The chapter (SOURCED): the northern smooth plains are "generally collocated with the highest K concentrations found on the planet," and the authors compare this to lunar maria and KREEP, adding "Although a KREEP-like material has not been identified on Mercury, the concentration of incompatible elements (K, Cl) in the northern terrane raises the possibility that regions with concentrated abundances of heat-producing radioactive elements such as K may have been a factor in powering Mercury's flood volcanism."
- **Enriched regions of U or Th (hollows, high-Mg region, volcanic plains):** NOT FOUND. No source I reached reports a mapped region with elevated U or Th. The chapter discusses hollows only as volatile-loss features (S- and C-bearing volatiles), not as uranium or thorium sites (SOURCED). Regional terrane statements for the high-Mg region are about Mg, Ca, S, Fe, Al, not U or Th.

### 1.3 K/Th, K/U and what they imply for volatiles

- Chapter (SOURCED): "MESSENGER revealed that Mercury's K/Th ratio is the highest observed in the inner solar system (Figure 2.3a), comparable to that of Mars and significantly higher than that for the volatile-depleted Moon." It "rules out many pre-MESSENGER theories for Mercury's formation, which predicted a near complete loss of volatiles." The chapter adds Cl/K similar to carbonaceous chondrites and Mars.
- The 2011 conference abstract (SOURCED): chondritic melting models appear to predict higher Th (~1 ppm) than observed.
- **Counter-interpretation: surface ratios may not be bulk ratios.** Habermann et al. (LPSC 2016 abstract, NASA NTRS 20160003144, SOURCED, downloaded) give surface K/U = 12,800 ± 4,300 and K/Th = 5,200 ± 1,800 (from Peplowski 2011) and calculate, for a sulfide layer at the base of the mantle and fO2 of IW-6.3 to IW-2.6, bulk-planet minimum K/U of 600 and K/Th of 2,003. Their conclusion: the elevated surface ratios "should not be interpreted as an enrichment of Mercury in volatile elements. Instead, they suggest low U- and Th-contents in the mantle and crust due to their early sequestration in Mercury's core and sulfide layer." They also say the presence of radioactive elements in the core "may have acted as major sources of energy."
- Pirotte et al. 2023 (Icarus 405, 115699; SOURCED, downloaded) reach a different conclusion: "U, K and especially Th are principally concentrated in the BSM and did not partition into the core because they are not siderophile elements," U is chalcophile at very low oxygen fugacity (an FeS layer would take up U), and "surface K/Th and K/U ratios are respectively 2-4 times and 3-6 times lower than expected for initial K/Th and K/U ratios similar to enstatite chondrites, implying that the planet suffered an important volatile loss." So the same data are read as high volatiles (2011), core sequestration (Habermann) or volatile loss (Pirotte). All are published positions.
- McCubbin et al. 2012 (cited in the chapter, SOURCED as a citation): the high K/Th "may not be a reflection of its volatile content, but instead the result of sequestration of Th within Mercury's core." Malavergne et al. 2010 (cited, SOURCED as a citation; abstract via search): U could be an important heat-producing element in the core, Th and K would not enter the core. The chapter's rebuttal: Th/U of about 2 "is inconsistent with suggestions that U fractionated into Mercury's core."

### 1.4 The radon-transport caveat

- Chapter (SOURCED): "it has been suggested that the GRS-measured U concentrations may be overestimated as a consequence of radon transport and diffusion within Mercury's regolith (Meslin and Déprez, 2012), as U gamma rays originate from a number of U-decay products, including radon."
- I could not reach Meslin and Déprez 2012 itself (title as given in the chapter's reference list: "Radon exhalation as a possible explanation to the low Th/U ratio of Mercury's surface"; three searches did not surface it; NOT FOUND at source). Whether the overestimate is large is therefore not known from this session. If U is overestimated, the real Th/U would be higher than about 2 (DERIVED, direction only).

### 1.5 Arguments about uranium enrichment processes on Mercury

- No published argument that Mercury has uranium ore-grade concentrations: NOT FOUND (queries logged).
- Published processes that move U on Mercury: (a) partitioning into a sulfide (FeS) layer or core at very low oxygen fugacity (Malavergne 2010; Habermann; Pirotte) which would lower mantle U; (b) enrichment in the crust by partial melting; Pirotte et al. model lavas of "~180-400 ppb Th and ~35-115 ppb U" after crust formation, matching the surface measurement (SOURCED); (c) temperature-dependent redistribution of K (not U) near the surface.

### 1.6 Bulk-silicate-Mercury model values

- Pirotte et al. 2023 (SOURCED): for bulk-planet inputs of 9 ppb U (average of EH enstatite chondrites; Javoy and Kaminski 2014) and 30 ppb Th, the bulk silicate Mercury (BSM) U is "~35 ppb in the absence of an FeS layer," "~33 ppb at the least reducing oxygen fugacity conditions (IW-3, 100-km thick FeS layer) to as low as ~23 ppb under the most reducing conditions (IW-6...)". BSM Th "~110 ppb for an FeS layer 100 km thick under the most reducing conditions or up to ~121 ppb in the absence of an FeS layer." They also state "the majority of HPE are concentrated in Mercury's thin silicate part" if no FeS layer formed.
- Existing project note also uses Knibbe et al. 2025 shell values (Th 50 ppb, U-238 27.8 ppb); I did not re-verify them.

---

## Q2. Venus

### 2.1 Lander gamma-ray results (K, U, Th)

| Lander | K | U | Th | Status |
|---|---|---|---|---|
| Venera 8 (1972) | K2O 4.0 ± 1.2 wt% | 2.2 ± 0.7 ppm | 6.5 ± 2.2 ppm | SOURCED (Icarus 2019 abstract, fetched via the cosmochemistry-papers page and cross-checked in a search summary; Shellnutt 2019, Icarus 321, 50-61). |
| Venera 9 (1975) | not found | not found | not found | NOT FOUND for the numbers. SOURCED qualitatively: Treiman's 2009 EGU abstract says Venera 9 has "a non-chondritic U/Th abundance ratio" and a K/Th ratio about half that of Earth's mantle (UNVERIFIED for the half, from a Treiman 2022 abstract snippet). |
| Venera 10 (1975) | not found | not found | not found | NOT FOUND. A 1976 Soviet abstract reports the soils at the Venera 9 and 10 sites have natural radioactive element contents "close to terrestrial basalts" (UNVERIFIED, snippet of ADS 1976KosIs..14..704S; the ADS page could not be fetched). A secondary page (GlobalSecurity) gives 0.3% K, 0.0002% Th, 0.0001% U without saying which site: UNVERIFIED and not reconciled. |
| Vega 1 (1985) | 0.45 ± 0.22 % | 0.64 ± 0.47 ppm (0.64 ± 0.47 × 10^-4 %) | 1.5 ± 1.2 ppm | SOURCED (Surkov et al. 1987, JGR 92, abstract text read in the EarthRef record; the plus-minus signs were encoded as a replacement character, and the uncertainties are read from the positions of those characters). |
| Vega 2 (1985) | 0.40 ± 0.20 % | 0.68 ± 0.39 ppm | 2.0 ± 1.0 ppm | SOURCED (same). |

- A recalled set of Venera 9 and 10 numbers (K about 0.47% and 0.30%, U about 0.60 and 0.46 ppm, Th about 3.65 and 0.70 ppm) came to mind during the work. UNVERIFIED and not confirmed at any source; two searches targeting them failed. Do not use them without a primary check.
- One encyclopedia article (EBSCO Research Starters) gives Venera 8 as "about 200 ppm" uranium and "650 ppm" thorium. That conflicts with the 2.2 and 6.5 ppm abstract values by a factor of about 100, and the abstract is the primary source. Treat the EBSCO numbers as a units error (DERIVED judgment).
- Quality statement (Treiman 2009 EGU abstract, SOURCED, downloaded): "Their analyses for K, U, and Th (by gamma rays) are imprecise, except for one (Venera 8) with extremely high K contents (~4% K2O) and one (Venera 9) with a non-chondritic U/Th abundance ratio." Also: "the Venera and VEGA landers sampled only materials from the Venus lowlands," none from tesserae, shield volcanoes or Ishtar Terra.

### 2.2 What rock types they match

- Vega 1 and 2: "similar to that of basic rocks (tholeitic basalts and gabbros) of the earth's crust"; the same conclusion for Vega 2 from XRF (SOURCED, EarthRef record of the abstract).
- Venera 9 and 10: basalt-like (UNVERIFIED, snippets).
- Venera 8: the high Th, U and K matched a diorite/granodiorite calculated bulk composition; Shellnutt (2019) argued it could be a fragment of crust resembling a terrestrial greenstone belt, modeled by fractional crystallization of a hydrous, oxidizing parent (SOURCED for the abstract's statements as fetched; the model description is from the same abstract in a search summary).
- A 2017 review states Venera 8 data are "high enough to suggest granitic rocks but would also be consistent with highly alkaline basaltic lavas" (UNVERIFIED, search summary).

### 2.3 Later reanalysis and bulk values

- A heat-flow paper (arXiv 2401.06558; 2024; UNVERIFIED, search summary) uses 0.4 µW per cubic meter average radioactive heat production from Venera and Vega data. A paper estimating bulk Venus U and Th of "18-29 ppb and 64-94 ppb" with K of 100-300 ppm appeared in a search summary and could not be traced to its source: UNVERIFIED, treat as unconfirmed.
- Sampled sites are all lowland basalt-like surfaces; Treiman notes tesserae may be older crust and Ishtar Terra may be granitic, both unsampled (SOURCED).

### 2.4 Surface conditions bearing on mining

- NASA NSSDC Venus fact sheet (fetched, summarized): surface pressure 92 bar; mean surface temperature 737 K (464 °C); mean gravity 8.87 m/s²; escape velocity 10.36 km/s; solar irradiance at Venus 2601.3 W/m².
- Cloud-top conditions (about 50-65 km altitude): temperature and pressure not retrieved in this session: NOT FOUND. A NASA ASCEND-2024 sample-return concept uses a balloon at about the 60 km level, rising to about 65 km (UNVERIFIED, snippet).
- Lander lifetimes at the surface: Treiman's abstract says current concepts are "severely limited durations at Venus' surface before they succumb to its high temperature" (SOURCED, 2009).

### 2.5 Uranium concentration processes on Venus

- NOT FOUND. No study of uranium concentration processes on Venus was found in two queries. What was found: Treiman (2022 abstract, snippet) argues U is mobile in aqueous fluids as uranyl while Th is not, so U/Th is a possible test for past water, and the Venera 9 non-chondritic U/Th is "consistent with" some such history (UNVERIFIED, wording from a search summary). A heat-flow paper notes that producing felsic rocks without water "typically requires extreme igneous fractionation" (UNVERIFIED, snippet).

---

## Q3. Moon, Mars, asteroids and meteorites

### 3.1 Moon

- **Procellarum KREEP Terrane (PKT), Lunar Prospector Th.** Jolliff, Gillis and Haskin (1999 workshop abstract, NASA NTRS 20000040504, fetched, summarized, consistent with other snippets): the PKT crustal section is about 12% of the Moon's crust and about 1.2% of the whole Moon but "may hold up to 40% of the Moon's total Th budget, depending on assumptions." The strongest hotspot covers the Fra Mauro Formation and parts of the Alpes Formation, "with Th near 12-13 ppm, consistent with Apollo 14 soils." Mean Th of volcanic-resurfaced and rugged terrain about 5.5 ppm. Apollo 14 mafic impact-melt breccias "reach about 30 ppm Th and average about 18 ppm"; Apollo 14 soils about 13 ppm. Apollo 12 breccia 12013 evolved lithologies 17-50 ppm, a KREEP basalt soil fragment about 50 ppm. Data resolution 5 degrees per pixel, so peaks are smeared.
- **Kaguya.** A 2016 JpGU abstract (UNVERIFIED, snippet) reports high-Th craters in the PKT (Aristarchus, Aristillus, Mairan) of about 7-12 ppm Th against 3-5 ppm in their surroundings. A 2013 JpGU abstract (UNVERIFIED) argues the new Th model for the PKT is about 50% lower than earlier estimates. PKT covers about 16% of the lunar surface (USGS Fact Sheet 2025-3049, SOURCED, downloaded) and the PKT maximum is near 13 ppm Th (UNVERIFIED, a 2023 paper in a snippet).
- **Uranium, global map.** Yamashita et al. 2010 (Geophys. Res. Lett. 37, L10201): first global lunar U map from the Kaguya gamma-ray spectrometer. Average U about 0.3 ppm, maximum about 2 ppm, average Th about 1.2 ppm (abstract values, UNVERIFIED from a search summary; the maximum is confirmed in the Crawford review below). Crawford (2015, "Lunar Resources: A Review," arXiv 1410.6865, SOURCED, downloaded): U scales with Th, "with a U/Th ratio of approximately 0.27 (Korotev, 1998)"; the Kaguya map "revealed a maximum surficial U abundance of about 2 ppm in the highest Th-bearing areas of the PKT south of the Imbrium basin" at a spatial resolution of 130 km. "For comparison, the urKREEP concentration of U is about 5 ppm (Warren and Wasson, 1979), and some small individual Apollo samples of highly evolved lithologies (i.e. quartz monzodiorites and felsites) are known with U concentrations in the range 10-20 ppm. However, even the latter concentrations are well below what would currently be considered a low grade U ore on Earth (>100 ppm; WNA, 2012)."
- A Lunar Sample Compendium entry for an Apollo 14 sample (14311) lists a clast U of 1.12 ppm (INAA) (UNVERIFIED, snippet). A NASA catalog lists Apollo 15 KREEP basalt 15386 at about 3-4 ppm U and about 10-15 ppm Th (UNVERIFIED, snippet).
- **Th/U in lunar samples:** about 3.8 ± 0.2 in a 1974 abstract (UNVERIFIED, snippet), consistent with U/Th 0.27 (1/0.27 = 3.7, DERIVED).
- **Bulk-Moon and mantle values:** 0.039 ppm U and 0.15 ppm Th for the average lunar mantle from pyroclastic glasses (UNVERIFIED, USGS publication summary); about 80 ppb U for the whole Moon in a 1974 model (UNVERIFIED).
- **Claims about lunar uranium deposits.** Press coverage in 2008-2010 ("Uranium found on the Moon," "Uranium boom on the Moon?") framed Kaguya detection as a possible resource; the follow-up coverage and the paper's maps showed "The concentrations are very far from being of commercial levels" and less than in many granites on Earth (UNVERIFIED, snippets from World Nuclear News, Space.com, Gizmodo). Status: no deposit above Earth low-grade ore has been identified on the Moon in what I found. One press piece said most uranium "should be near the Moon's core" because it is dense; that contradicts the sourced KREEP picture (U and Th concentrated in the last residual liquid and the crust), and I treat it as an error in the press piece (DERIVED judgment).
- **Thorium and REE value of KREEP:** USGS Fact Sheet 2025-3049 (SOURCED): KREEP is mapped by Th; PKT covers about 16% of the surface; "elevated thorium concentrations are mostly in a ring around the Imbrium basin"; Th concentrations correlate with REEs. One study suggests "locations with Th concentration twelve times what was estimated for KREEP from just the orbital data (Hagerty and others, 2006)."

### 3.2 Mars

- Taylor et al. 2006 (JGR 111, E03S10, "Bulk composition and early differentiation of Mars"), abstract text as quoted in a search summary (UNVERIFIED): average surface Th 0.6 ppm (range 0.2 to 1 ppm); K 2000 to 6000 ppm; average K/Th about 5300; if surface Th equals crustal Th the crust cannot be thicker than about 118 km. Boynton et al. 2007 (JGR 112, E12S99): K and Th follow similar patterns, depleted over young volcanic deposits (UNVERIFIED, abstract summary).
- **Uranium on Mars:** no direct orbital measurement exists (the Odyssey GRS maps K, Th, Fe, Si, Cl, H, not U in what I found). DERIVED estimate: with Th 0.6 ppm and an assumed Th/U of 4.0 (the lunar value is 3.7-3.8; the Mars value was not found, so this is an assumption), U is about 0.15 ppm (range 0.12 to 0.17 for Th/U 3.5 to 5, DERIVED).
- Martian meteorite NWA 11115 has K/Th 2987 ± 810 and Th/U about 4.09 (UNVERIFIED, snippet). A bulk-silicate-Mars U-Pb ratio (mu about 3) is not an abundance. A bulk silicate Mars U of 16 ppb and Th of 56 ppb (a recalled model) was not confirmed: NOT FOUND.

### 3.3 Chondritic meteorites (SOURCED, Lodders 2021, Space Science Reviews 217:44, Table 1, ppm by mass; downloaded and read)

| Group | Th (ppm) | U (ppm) | Th/U (DERIVED) |
|---|---|---|---|
| CI | 0.0298 (±0.0030) | 0.00816 (±0.00106) | 3.65 |
| CM | 0.042 | 0.011 | 3.8 |
| CV | 0.059 | 0.016 | 3.7 |
| CO | 0.046 | 0.014 | 3.3 |
| CK | 0.059 | 0.014 | 4.2 |
| CR | 0.041 | 0.012 | 3.4 |
| H | 0.040 | 0.013 | 3.1 |
| L | 0.04 | 0.013 | 3.1 |
| LL | 0.046 | 0.013 | 3.5 |
| EH | 0.029 | 0.0095 | 3.1 |
| EL | 0.031 | 0.008 | 3.9 |

So chondritic U is 8 to 16 ppb and Th is 30 to 60 ppb. Measured individual meteorites: an H5 chondrite, Th about 35.8 ppb and U about 14.9 ppb; achondrites U 18 to 190 ppb and Th 56 to 663 ppb (UNVERIFIED, snippets). A 1955 estimate for stony meteorites was 0.1 ppm U and 0.5 ppm Th (UNVERIFIED; superseded by the table above).

### 3.4 Asteroids

- No asteroid U or Th has been measured by remote sensing in what I found; asteroid abundances are inferred from the meteorite analogs above (DERIVED from the table; the analog assignment per asteroid type is a standard approach but I did not retrieve a source mapping types to groups).
- Claims of uranium-rich asteroids: NOT FOUND (two queries). A discussion-forum post (not a source) argued that U in asteroids is too dilute to mine and would need to be raised by "a factor of ~100 or so."
- Metal-rich asteroids: iron-meteorite metal is siderophile-element rich; uranium is lithophile and is not expected in the metal (this is general geochemistry; no source retrieved this session, UNVERIFIED).

---

## Q4. Earth for scale

### 4.1 Crustal abundance (U and Th)

- Dye (2010) crust model table, built on Rudnick and Gao 2003 and seismic crust layers (arXiv 1005.4465, SOURCED, downloaded): **bulk continental crust** U 1.17 ± 0.30 µg/g and Th 4.97 ± 0.66 µg/g (Th/U 4.3 ± 1.2); **upper crust** U 2.70 ± 0.57 and Th 10.5 ± 1.1; middle crust U 1.30, Th 6.50; lower crust U 0.20, Th 1.20; oceanic crust U 0.10, Th 0.22. Bulk silicate Earth U 8.2 ppb, Th 29 ppb (the same paper).
- The figure "about 2.7 ppm" for continental crust in the brief is the **upper-crust** value in this table. WNA's table lists "continental crust (average) 2.8 ppm" and granite 3-5 ppm, sedimentary rock 2-3 ppm, seawater 0.003 ppm (fetched page, summarized). The bulk-crust value in the Dye table is 1.17 ppm. These differ by a factor of about 2.3; both are published conventions (DERIVED comparison).
- Total crustal uranium (DERIVED): 2.79 × 10^25 g × 1.17 × 10^-6 = 3.3 × 10^13 tonnes.

### 4.2 Ore grades by deposit type

- WNA, *Geology of Uranium Deposits* (fetched page, summarized): sandstone 0.05-0.35% U; paleo-quartz-pebble conglomerate 0.01% (Witwatersrand) to 0.15% (Elliot Lake); phosphate 0.005-0.015% U; Proterozoic unconformity "some ore around 20% uranium" (Saskatchewan); polymetallic iron-oxide breccia complex 0.07 to 0.035% as written on the page (likely a transcription oddity).
- WNA, *Uranium Mining Overview* (fetched page, summarized): most supporting deposits have "average grades in excess of 0.10% of uranium"; some Canadian mines "up to 20% U"; some mines operate down to about 0.02% U; heap leaching ore usually below 0.1% U; Canadian mills are designed for up to 26% U; by-product uranium (with copper, gold, phosphate) may be a tenth the concentration of primary orebodies.
- WNA Table 1 (fetched): very high-grade (Canada) 20% U (200,000 ppm), high-grade 2% (20,000 ppm), low-grade 0.1% (1,000 ppm), very low-grade (Namibia) 0.01% (100 ppm).
- Specific mines (secondary, search snippets, UNVERIFIED): Cigar Lake average reserve grade 14.5-14.7% U3O8 (Cameco, Dec 2019), about 18% in an Orano description; McArthur River 6.89% U3O8 (Cameco reserves, Dec 2020), 7% in an Orano description; Olympic Dam 10.1 billion tonnes at 0.78% Cu and **0.25 kg U per tonne** (250 ppm U3O8; 2015 resource), reserves 484 million tonnes at 1.95% Cu and 0.59 kg/t U; Rössing 0.028% U3O8, Ranger 0.234%, Trekkopje 0.00126% (a calcrete deposit; from a conference paper snippet). Olympic Dam's uranium is a by-product of copper.
- IAEA UDEPO deposit counts (end-2017; UNVERIFIED, snippet): 951 sandstone deposits holding about 4.83 million tU; 114 Proterozoic unconformity deposits holding about 1.55 million tU; for polymetallic iron-oxide breccia complex deposits, 80% of the resource is Olympic Dam.

### 4.3 Resources, production and demand (Red Book, "Uranium: Resources, Production and Demand," OECD-NEA and IAEA)

- **Edition 2026** (data as of 1 Jan 2025), as quoted on the WNA page (fetched, summarized; the Red Book itself was not opened): identified resources at <$130/kg U 5,864,500 tU (Australia 1,701,600; Kazakhstan 827,500; Canada 551,700; Russia 471,700; Namibia 392,800); at <$260/kg U 8.105 million tU; rock phosphate 34,600 tU (<$130) and 42,300 tU (<$260); cumulative production 1945-2024 3,299,714 tU; power reactors "just over 400 GWe" need "nearly 69,000 tU per year"; fuel consumption **160 tU per GWe per year** (189 t U3O8) at 0.25% tails assay, 175 tU (206 t U3O8) in the 2012 report.
- **Edition 2024** (data as of 1 Jan 2023; snippets, UNVERIFIED): identified recoverable resources 7,934,500 tU at $40-260/kgU (Australia 28%, Kazakhstan 14%, Canada 10%; Olympic Dam about 17% of the world); 438 reactors, 394 GWe, requiring about 59,000 tU a year.
- **Production** (WNA, fetched, summarized): world mine production in tU: 2020 47,731; 2021 47,805; 2022 49,614; 2023 54,433; 2024 60,213. In-situ leach 55% of 2024 production. Largest 2024 mines: McArthur River/Key Lake 7,808 tU; Cigar Lake 6,501; Husab 4,437; Rössing 2,205; Olympic Dam 2,693.
- DERIVED cross-check: 69,000 tU / ~400 GWe = about 172 tU/GWe-year, consistent with the 160 figure. Identified resources (8.1 Mt) at 60,000 tU/yr correspond to 135 years of 2024 production (DERIVED, simple division; the Red Book makes no such statement in what I read).

### 4.4 Uranium in seawater

- Concentration about 3.3 ppb; total dissolved about 4.5 billion tonnes (ORNL report, UNVERIFIED snippet). DERIVED check: 1.4 × 10^21 kg of ocean water × 3.3 × 10^-9 = 4.6 × 10^9 tonnes. WNA lists seawater at 0.003 ppm (fetched).
- Extraction research state (UNVERIFIED, search summaries of ORNL, PNNL, JAEA, Schneider and Sachde, and a 2024 Nanoscale review): amidoxime polymer adsorbents reach about 3 mg U per gram of adsorbent after 8 weeks in PNNL marine tests (3.3 mg/g max reported); ORNL adsorbent updated cost about $610/kg U; Schneider and Gill (2014) $606/kg with a 95% interval of $420-1,000; Schneider and Sachde (2013) $1,230/kg (95% interval $1,030-1,430) for 2 kg U per tonne adsorbent and 6 reuses, falling to $299/kg at 6 kg/t and 20 reuses; a 2024 review "current cost estimates being $600 per kg per U"; Lindner and Schneider (2015) $400-1,000/kg. A newsletter claimed a Chinese pilot reaching "$150/kg" (secondary; UNVERIFIED). I did not retrieve a current uranium spot price (NOT FOUND this session).
- DERIVED water throughput: at 3.3 µg/L and 100% capture, 1 tU needs 3.0 × 10^11 L (3.0 × 10^8 m³); 160 tU (one GWe-year) needs 4.9 × 10^10 m³; 20,000 tU needs 6.1 × 10^12 m³ (6.06 × 10^12 m³ = about 6,060 km³ of seawater a year, DERIVED).

### 4.5 Phosphate uranium

- Red Book 2026 as quoted on WNA (fetched): rock phosphate resources 34,600 tU at <$130/kg and 42,300 tU at <$260/kg. WNA geology page: phosphate deposits 0.005-0.015% U (50-150 ppm).

### 4.6 Thorium on Earth

- USGS Mineral Commodity Summaries, Thorium, February 2026 (SOURCED, downloaded): the primary source is monazite; in 2025 "thorium was not separated or recovered by any domestic facility" (United States); "worldwide identified thorium resources were an estimated 6.4 million tons of thorium" (WNA 2017); India 850,000 tons, Brazil 630,000, Australia and the United States 600,000 each; "Without demand for the rare earths, monazite likely would not be recovered for its thorium content"; imports of thorium compounds valued at $118,000 in 2025; unit values $26-29/kg (France, import). Reserves figure is not given in the 2026 text I extracted.
- Crustal Th 4.97 ppm bulk, 10.5 ppm upper crust (Dye table, SOURCED).

---

## Q5. Concentration processes

### 5.1 What the sources say about how uranium concentrates on Earth

- **Magmatic differentiation:** U and Th are incompatible and go into the last melts. WNA's table lists intrusive (alaskite, granite, pegmatite, monzonite) and granite-related vein deposits (fetched page). In the Moon, urKREEP is the "final KREEP-rich residual magma ocean liquid... rich in Th and U" (UNVERIFIED, snippet) with about 5 ppm U (Crawford, SOURCED). This process needs a magma body, not water, oxygen or plate tectonics. Evidence on Mercury: lava models of 35-115 ppb U from partial melts of a ~9-35 ppb source (Pirotte, SOURCED), i.e., enrichment by a factor of about 3 for U; no ore-grade value.
- **Hydrothermal:** vein, volcanic-related, metasomatite (Na or K), polymetallic iron-oxide breccia (water-magma interaction), collapse-breccia pipes (WNA table). These need circulating fluid (usually water).
- **Sedimentary and redox:** U(VI) (uranyl, carbonate complexes) is mobile in oxidized water; U(IV) minerals are far less soluble; precipitation at a reduction front (roll-front sandstone, unconformity) concentrates it (UNVERIFIED, from search summaries of several mineralogy papers; one paper reports U mobile under reducing conditions in acidic brines). WNA: sandstone deposits "precipitated under reducing conditions"; surficial deposits by deep weathering in semi-arid to arid climate and valley-fill and playa deposition; lignite/coal and black shale by adsorption onto organic matter; phosphate by uranium in fine-grained apatite.
- **Detrital:** paleo-quartz-pebble conglomerates (Witwatersrand, Elliot Lake) by "fluvial transport of uraninite in an anoxic atmosphere" (WNA, fetched). That is a process that used liquid water flow but not oxygen.

### 5.2 Which need water, oxygen, plate tectonics (DERIVED reading of the above, not a published statement)

- Needs liquid water: hydrothermal types, sandstone and unconformity types, surficial, detrital placer types, phosphate and black-shale adsorption types. Needs oxygen (oxidized fluids to carry U(VI)): sandstone, unconformity, surficial types, in the standard model. Needs neither: magmatic differentiation. The sources I read do not make a statement about plate tectonics as a requirement; the only link is that the continental crust, which carries most crustal U, came from repeated melting (UNVERIFIED inference).
- Largest deposit class by tonnage (UDEPO snippet): sandstone, then unconformity: both water-and-redox types. The world's highest-grade ore (Athabasca unconformity) is a water-and-redox type.

### 5.3 Is any of this plausible on a dry, airless or very hot body?

- Magmatic enrichment is the one process with direct non-Earth evidence: lunar KREEP (up to 5 ppm urKREEP; 10-20 ppm in tiny felsite samples; 2 ppm maximum in the 130 km Kaguya map). Mercury's northern smooth plains show K enrichment, but no equivalent KREEP-like U or Th concentration has been identified (Nittler chapter, SOURCED).
- Hydrothermal and redox processes on Venus, Mars or Mercury: no source found describing uranium concentration by them (NOT FOUND). Mars has had liquid water (K-Th GRS patterns discussed as water-related in a 2009 review, UNVERIFIED snippet), but no Martian U ore or enrichment study was found.
- Meteorite evidence: no meteorite U concentration above the chondrite table's 8-16 ppb is a "deposit"; individual achondrites reach 190 ppb (UNVERIFIED).

---

## Q6. Scale and economics of mining dilute rock (DERIVED, working shown)

**Inputs (SOURCED unless noted):** fuel use 160 tU per GWe-year (Red Book via WNA); world material extraction about 106 billion tonnes in 2020 (UNEP International Resource Panel, Global Resources Outlook 2024; UNVERIFIED, search summaries of the press release; "from 30 billion tonnes in 1970," projected 160 billion tonnes by 2060); target scenarios: 1 GWe-year (160 tU) and 20,000 tU a year.

**Method:** rock per tonne U = 1,000,000 / grade in ppm (100% recovery; real recovery is lower, so these are minima). Rock for 160 tU = 160 × that; for 20,000 tU = 20,000 × that. Ratio to world extraction = rock / 106 Gt.

| Material (U grade) | t rock per t U | Gt rock per GWe-year | Gt rock for 20,000 tU | x world annual extraction (106 Gt) |
|---|---|---|---|---|
| Mercury GRS surface (0.090 ppm) | 1.1 × 10^7 | 1.8 | 222 | 2.1 |
| Mercury BSM model, 35 ppb | 2.9 × 10^7 | 4.6 | 571 | 5.4 |
| Mercury BSM model, 23 ppb | 4.3 × 10^7 | 7.0 | 870 | 8.2 |
| Mercury bulk planet, 9 ppb | 1.1 × 10^8 | 17.8 | 2,222 | 21 |
| Venus Vega 2 (0.68 ppm) | 1.5 × 10^6 | 0.24 | 29 | 0.28 |
| Venus Vega 1 (0.64 ppm) | 1.6 × 10^6 | 0.25 | 31 | 0.29 |
| Venus Venera 8 (2.2 ppm, one outlier) | 4.5 × 10^5 | 0.073 | 9.1 | 0.086 |
| Moon average (0.3 ppm) | 3.3 × 10^6 | 0.53 | 67 | 0.63 |
| Moon maximum in Kaguya map (2 ppm) | 5.0 × 10^5 | 0.080 | 10 | 0.094 |
| urKREEP (5 ppm) | 2.0 × 10^5 | 0.032 | 4.0 | 0.038 |
| Apollo felsite (10-20 ppm) | 1.0-0.5 × 10^5 | 0.016-0.008 | 2.0-1.0 | 0.019-0.009 |
| Mars (0.15 ppm, assumed Th/U 4) | 6.7 × 10^6 | 1.1 | 133 | 1.3 |
| CI chondrite (8.16 ppb) | 1.2 × 10^8 | 19.6 | 2,451 | 23 |
| H, L, LL chondrite (13 ppb) | 7.7 × 10^7 | 12.3 | 1,538 | 14.5 |
| Earth bulk crust (1.17 ppm) | 8.5 × 10^5 | 0.14 | 17 | 0.16 |
| Earth upper crust (2.7 ppm) | 3.7 × 10^5 | 0.059 | 7.4 | 0.070 |
| Granite (4 ppm) | 2.5 × 10^5 | 0.040 | 5.0 | 0.047 |
| Very low-grade ore (0.01% U) | 1.0 × 10^4 | 0.0016 | 0.20 | 0.0019 |
| Low-grade ore (0.02% U) | 5,000 | 0.0008 | 0.10 | 0.00094 |
| Olympic Dam (250 ppm U3O8 = 212 ppm U) | 4,700 | 0.00075 | 0.094 | 0.00089 |
| Low-grade ore (0.1% U) | 1,000 | 0.00016 | 0.020 | 0.00019 |
| High-grade ore (2% U) | 50 | 8 × 10^-6 | 0.001 | 9 × 10^-6 |
| Very high-grade ore (20% U) | 5 | 8 × 10^-7 | 0.0001 | 9 × 10^-7 |
| Seawater (3.3 µg/L) | 3.0 × 10^8 t of water | 4.9 × 10^10 m³ water | 6.1 × 10^12 m³ water | (water, not rock) |

(Mercury's 0.090 ppm entries use the possibly radon-overestimated GRS value; if the true surface U is lower, the rock needed is higher in proportion.)

**Energy the uranium yields (DERIVED):** one GWe-year = 10^9 W × 3.156 × 10^7 s = 3.156 × 10^16 J (8.77 TWh) of electricity. At 160 tU per GWe-year, each tonne of natural U yields 1.97 × 10^14 J(e) = 54.8 GWh(e) = 197 TJ(e), in a light-water-reactor, once-through cycle. For scale, complete fission of all U-235 and U-238 in a tonne would be much higher (theoretical, 200 MeV per fission: 8.2 × 10^10 J per gram of U-235, so 5.8 × 10^14 J of heat per tonne of natural U counting only its 0.711% U-235, DERIVED); the 197 TJ(e) figure is what today's reactor fleet gets as electricity.

**Break-even energy per tonne of rock:** electricity yield per tonne of U divided by rock per tonne of U (before any energy for enrichment, fuel fabrication, transport, or the mine's own plant):

| Grade | Break-even (MJ electric per tonne rock) | kWh(e) per tonne rock |
|---|---|---|
| Mercury 0.090 ppm | 17.8 | 4.9 |
| Mars 0.15 ppm | 29.6 | 8.2 |
| Moon average 0.3 ppm | 59 | 16.4 |
| Vega 2, 0.68 ppm | 134 | 37 |
| Moon maximum 2 ppm | 394 | 110 |
| Earth upper crust 2.7 ppm | 533 | 148 |
| urKREEP 5 ppm | 986 | 274 |
| 0.02% ore | 39,450 | 11,000 |
| CI chondrite 8.16 ppb | 1.6 | 0.45 |

**Comparison with the energy to crush and grind (search summaries, UNVERIFIED):** milling electricity is typically 10-40 kWh per tonne of ore (up to 60 kWh/t in some mining sources); a rule of thumb of 20 kWh/t for an integrated crushing-grinding plant; crushing and grinding of non-ferrous ores uses about 0.43% of global electricity (87 TWh a year). Reading the tables together (DERIVED comparison, not a conclusion): at 0.090 ppm the break-even of 4.9 kWh(e)/t is below the 10-60 kWh/t milling range quoted, at 0.3 ppm the 16 kWh(e)/t is inside that range, at 2 ppm the 110 kWh(e)/t is above it. This compares electricity yield with grinding electricity only; mining (excavation, hauling), chemical extraction, tailings handling and the enrichment of natural uranium to reactor fuel are not included, and uranium is not fully recovered in practice. Milling energy depends on the rock's hardness; none of these were measured for the Moon, Mercury or Venus.

**Published studies of low-grade uranium and the "energy cliff":** A paper at an IAEA conference (Strupczewski, "2S05") rebuts a claim attributed to Storm van Leeuwen that no net energy is possible below an ore grade of about 0.02-0.01% U3O8, and uses Ranger, Rössing and Trekkopje examples (UNVERIFIED, search summary only; the page returned HTTP 402). Mudd's work finds mining energy and water inputs are inversely related to ore grade (UNVERIFIED, snippet). A University of Texas thesis (Tavrides, 2010) says mining of lower-grade uranium deposits is likely to be less energy-intensive than earlier investigators concluded (UNVERIFIED, snippet). I did not reach the coefficients of any of these. Mining at crustal-average or lower grade (1-3 ppm) as a primary uranium source: NOT FOUND (no published operating or planned case).

**Seawater as a low-grade analog:** see 4.4; published costs of about $300-1,230/kg U (UNVERIFIED snippets) for a resource at 3.3 µg/L.

---

## Q7. Space-transport side

### 7.1 Escape velocity and surface gravity (NASA NSSDC fact sheets, fetched, summarized)

| Body | Escape velocity (km/s) | Surface gravity (m/s²) | Solar irradiance (W/m²) |
|---|---|---|---|
| Mercury | 4.3 | 3.70 | 9,082.7 (mean) |
| Venus | 10.36 | 8.87 | 2,601.3 |
| Earth | 11.186 | 9.820 | 1,361.0 |
| Moon | 2.38 | 1.62 | 1,361.0 |
| Mars | 5.03 | 3.73 | 586.2 (mean) |

Mercury surface temperature: 590-725 K on the sunward side per the fact sheet (the fact sheet also gives an average of 440 K); perihelion 46.0 million km, aphelion 69.8 million km.

### 7.2 Delta-v figures (secondary)

- Wikipedia "Delta-v budget" (fetched, summarized; table values without inline citation for the planetary Hohmann rows): from Earth orbit, Hohmann transfer Mercury 7.5 km/s to enter the transfer orbit, 5.5 km/s from LEO, 13.3 km/s exiting LEO (3.5 months); Venus 2.5 and 3.5 km/s (4.8 months); Mars 2.9 and 3.6 km/s (8.5 months). These reach the planet's orbital distance, not orbit or surface. Moon surface to LEO 2.74 km/s; to Earth escape 2.80 km/s; low lunar orbit from Earth escape 1.40 km/s. Near-Earth asteroid: Earth escape to closest NEO 0.8-2.0 km/s; one-way LEO to NEO from 3.8 km/s; return as low as 0.06 km/s with aerocapture (cited there to JPL pages). Treat as UNVERIFIED at the primary level.
- **Venus:** the Venus Life Finder study (arXiv 2112.05153; UNVERIFIED, snippet) budgets 8.78 km/s for ascent from the upper atmosphere to a 300 km Venus orbit, with 0.10 km/s for rendezvous and 3.66 km/s for capture. A Valentian abstract says a rocket must fire above about 55 km altitude because of drag and that surface-to-orbit delta-v is "close to the Earth case" (UNVERIFIED, snippet). The vacuum escape velocity at the Venus surface is 10.36 km/s (SOURCED); the surface case with atmosphere and 92 bar pressure: no source found for a surface-launch delta-v (NOT FOUND).
- **Mercury:** surface-to-orbit and surface-to-Earth-transfer delta-v: NOT FOUND in a mission study. DERIVED lower bound: the escape velocity of 4.3 km/s, then the heliocentric Hohmann leg to Earth's distance (Wikipedia table: 7.5 km/s between Earth and Mercury transfer orbits at the Earth end; the Mercury-end departure velocity relative to Mercury was not retrieved). A Mercury ejecta paper (arXiv 0801.4038) says material must leave at roughly twice the escape speed to exit the system (UNVERIFIED, snippet).

### 7.3 Mass-driver and tether launch

- Launch kinetic energy at escape speed (DERIVED, E = 1/2 v²): Moon 2.83 MJ/kg; Mercury 9.24 MJ/kg; Mars 12.7 MJ/kg; Venus 53.7 MJ/kg (vacuum, no atmosphere; not applicable on the surface); Earth 62.6 MJ/kg. A lunar wiki gives 2.4 MJ/kg for a mass driver against about 110 MJ/kg for an oxygen-aluminum rocket (UNVERIFIED, snippet; the 2.4 MJ/kg figure is lower than the 2.83 MJ/kg escape energy, so it likely refers to a lower exit speed).
- **Scale against the fuel (DERIVED):** launching 20,000 tU a year at Mercury escape speed takes 20,000,000 kg × 9.24 MJ/kg = 1.85 × 10^14 J = 51 GWh a year, which is 4.7 × 10^-5 of the electricity that uranium yields (20,000 × 1.97 × 10^14 J = 3.9 × 10^18 J). From the Moon: 16 GWh, 1.4 × 10^-5 of the yield. This counts launching only the extracted uranium; launching the rock would be 10^5 to 10^7 times more mass (table in Q6).
- NASA's 1970s space-settlement study (SP-428 summary, nss.org, fetched, summarized): about 2.4 million tons of lunar material delivered to a manufacturing facility over a 10-year program; cost per kg delivered, Table 3: asteroidal $25.2 (with RDT&E) or $10.8 (excluded) without a LEO station; $28.4 or $11.5 with; lunar $23.8 or $15.4. These are 1970s dollars and a mass-driver concept; no mass driver has been built at launch scale (UNVERIFIED, snippet of a commercial summary). Modern mass-driver cost-per-kg studies: NOT FOUND in reviewed sources; several web pages give figures under $10/kg (marginal electricity only) or hardware masses of hundreds to thousands of tonnes (UNVERIFIED, advocacy pages; not citable).
- Tether (skyhook) launch costs from Mercury, Venus, the Moon or an asteroid: NOT FOUND.

### 7.4 Solar flux by distance and nuclear versus solar

- Solar irradiance (SOURCED from the fact sheets: Mercury 9,082.7; Venus 2,601.3; Earth 1,361.0; Mars 586.2 W/m²). DERIVED by inverse square from 1,361 W/m² at 1 AU: Mercury at perihelion 14,400 and at aphelion 6,250; **Jupiter (5.2026 AU) 50.3 W/m² (3.7% of Earth)**; **Saturn (9.5549 AU) 14.9 W/m² (1.1%)**; main belt at 2.77 AU 177 W/m².
- Cross-checks (UNVERIFIED, snippets): a NASA technical paper says Jupiter probes see "3.4 to 4.1 percent of Earth's solar intensity"; Juno's arrays produce about 400-500 W at Jupiter versus about 12-14 kW at Earth, and need about 30 times the area for the same power at Jupiter; Saturn sunlight is "about 90 times weaker than at Earth" and Cassini used radioisotope power.
- Array area for 1 GWe at 20% efficiency (DERIVED; ignores storage, night and degradation): Mercury mean 0.55 km²; Earth 3.7 km²; Mars 8.5 km²; Jupiter 99 km²; Saturn 336 km².
- Where nuclear becomes necessary: Juno shows solar power at Jupiter is workable with very large arrays for a few hundred watts; at Saturn the only mission-class precedent found (Cassini) is nuclear. This is as far as the sources I reached go; for a settlement, the area scaling above is the only quantitative statement I can offer, and the point at which nuclear is necessary rather than merely smaller depends on a power-demand and mass-per-kW choice that no source here makes.

---

## FINAL

**What the sources support**
- Mercury's northern hemisphere surface has about 90 ± 20 ppb U and 155-220 ppb Th, with Th/U about 2 and K/Th among the highest in the inner solar system; K varies (240-2500 ppm) and is highest in the northern smooth plains, Th shows little variation; U may be overestimated through radon transport. Modeled bulk-silicate-Mercury U is about 23-35 ppb.
- Venus lander data are imprecise basalt-like values (Vega 1 and 2: U 0.64 and 0.68 ppm, Th 1.5 and 2.0 ppm, uncertainties about 60-70% on U) with one high-K, high-U, high-Th outlier (Venera 8: U 2.2 ppm, Th 6.5 ppm, K2O 4 wt%) at a surface of 737 K and 92 bar.
- The Moon's best-measured enrichment is KREEP: Kaguya U maximum about 2 ppm (130 km resolution), urKREEP about 5 ppm, tiny Apollo samples 10-20 ppm, all below what is considered low-grade ore on Earth (above 100 ppm). Chondrites hold 8-16 ppb U.
- Earth's mined ore is 100 ppm to 20% U; the world used about 60,000 tU in 2024 and 160 tU per GWe-year; identified resources are about 8 million tU; seawater holds about 4.5 billion tonnes of U at 3.3 ppb, with published extraction costs of roughly $300-1,200/kg U in research estimates.
- At the grades found off Earth, 20,000 tU a year of rock would be 1 to 2,500 billion tonnes (Q6 table); at Mercury's surface grade it is about twice the world's annual material extraction, at urKREEP grade about 4% of it. Break-even electricity yield per tonne of rock at Mercury's grade (5 kWh) is below published grinding energy (10-60 kWh per tonne).
- Launch energy for the uranium itself is small relative to its yield (about 10^-5 to 10^-4); the rock mass dominates.

**What the sources do not support**
- No source reports a uranium ore-grade concentration, a uranium-rich asteroid or a mineable lunar deposit. No source describes uranium concentration by water or redox processes on Mercury, Venus or the Moon.

**NOT FOUND**
- Global Mercury Th or U maps; the explanation for the Th revision from 220 to 155 ppb; Meslin and Déprez 2012 itself; Venera 9 and 10 numbers; Venus cloud-top conditions; direct Mars U; mass-driver or tether launch cost studies from Mercury or Venus; Mercury surface-to-Earth delta-v study; a current uranium spot price; Olympic Dam, Cigar Lake and McArthur River grades at the operator's own pages; Mudd and Tavrides regression coefficients.

---

## Search log (tool, exact query or URL, result)

Tools: WS = WebSearch (standard unless stated); WF = WebFetch; CURL = direct download to the scratchpad folder (used for PDFs, opened with pdftotext; no block was bypassed). "Hit" = useful; "Partial"; "Miss". Dead-end type given where relevant.

**Mercury**
1. WS "MESSENGER Gamma-Ray Spectrometer Mercury potassium thorium uranium abundances Peplowski" — hit (abstract numbers).
2. WF https://core.ac.uk/download/161445502.pdf — miss: HTTP 403 (died at source).
3. WF https://repository.si.edu/items/dcb77953-0598-4663-852c-7276c77d65fa — miss: HTTP 403 (source).
4. WS "Mercury thorium uranium MESSENGER GRS revised Th 155 ppb radon transport uranium overestimated Peplowski 2014 Nittler" — partial (no revision found).
5. WF https://meetingorganizer.copernicus.org/EPSC-DPS2011/EPSC-DPS2011-1170.pdf — partial: binary returned, saved and read with pdftotext (hit).
6. WS "Mercury "K/U" ratio MESSENGER Th U surface radon Earth Venus Mars K/Th 5000 volatile" — hit (Habermann, Pirotte leads).
7. WF https://ntrs.nasa.gov/api/citations/20160003144/downloads/20160003144.pdf — binary, saved and read (hit: Habermann abstract).
8. WF Pirotte et al. 2023 PDF at orbi.uliege.be — binary, saved and read (hit).
9. WS "Nittler Chabot Grove Peplowski "The Chemical Composition of Mercury" chapter..." — hit (arXiv 1712.02187).
10. CURL https://arxiv.org/pdf/1712.02187 — hit (full chapter).
11. WS "Peplowski MESSENGER GRS Mercury thorium abundance 0.155 ppm uranium northern smooth plains Th map variation" — partial.
12. WS "Meslin Déprez 2012 Radon exhalation as a possible explanation to the low Th/U ratio of Mercury's surface" — miss (paper not indexed; died at query/index).
13. WS "Peplowski 2012 "Variations in the abundances of potassium and thorium on the surface of Mercury" Caloris northern smooth plains results" — partial (abstract only).
14. WF https://ui.adsabs.harvard.edu/abs/2012JGRE..117.0L04P/abstract — miss: HTTP 405 (source).
15. WS "Mercury uranium radon regolith Th/U ratio gamma-ray "Meslin" Mercury surface planetary space science 2012" — miss for the paper; confirmed the chapter's citation.
16. WS "Mercury core uranium Malavergne 2010 metal-silicate partitioning U Th heat producing elements reduced conditions Mercury sulfide layer enrichment mantle bulk U ppb" — partial.
17. WS "Mercury surface mass driver OR tether launch to Mercury orbit material export solar power Mercury 9 kW/m2 industrial mining study Mercury delta-v surface to Earth transfer" — miss for Mercury-specific studies (died at sources: none exist in results).

**Venus**
18. WS "Venera 8 9 10 Vega 1 2 gamma-ray spectrometer Venus surface K U Th results ppm Surkov" — hit (Vega, Venera 8).
19. WS "Venus surface composition K U Th Venera Vega gamma ray table Kargel Lunar Planetary Institute Venus II "Th" "U" ppm" — partial.
20. WF https://cosmochemistry-papers.com/2018/11/07/the-curious-case-of-the-rock-at-venera-8/ — hit (Venera 8 abstract).
21. WF https://aminer.org/pub/53e9b1d7b7602d9703c6d062/... — miss (no abstract; source).
22. WF https://link.springer.com/content/pdf/10.1007/BF00142398.pdf — miss: redirected to an authentication page (paywall); not followed.
23. WF https://www.ebsco.com/research-starters/earth-and-atmospheric-sciences/venuss-surface-experiments — partial (numbers conflict with primary; judged a units error).
24. WS "Surkov 1987 "Uranium, thorium, and potassium in the Venusian rocks at the landing sites of Vega 1 and 2" Journal of Geophysical Research 92 E537" — hit.
25. WS "Venus landers radioactive elements table Venera 8 9 10 Vega 1 2 K% U ppm Th ppm heat production..." — partial.
26. CURL arXiv 1703.10961 and NTRS 19930005109 (Venus review; abstract-quality text) — partial; no table.
27. CURL EGU2009-6536.pdf (Treiman) — hit; CURL NTRS 20220007325 (Treiman abstract) — partial; CURL EarthRef ERR/37056 — hit (Vega abstract with uncertainties).
28. WS "Venera 9 Venera 10 gamma spectrometer potassium 0.47% uranium thorium Th 3.65 U 0.60 Venera 10 K 0.30 Th 0.70 ppm" — miss (died at sources).
29. WS (extended) "Venera 10 landing site basalt "U" "Th" "K" gamma spectrometer GS-12V 0.46 0.70 0.30 Venera 9 0.60 3.65 0.47 radioactivity of surface rocks" — miss for numbers (ADS 1976KosIs abstract indexed but not fetchable).
30. WS "Treiman "curious case of the rock at Venera 8" Icarus 2019 Th U K2O alkaline syenite greenstone" — hit; corrected author to Shellnutt.
31. WS "Venus uranium thorium concentration processes crust enrichment Venus tesserae granitic felsic evolved magmas heat production Venus radiogenic heat K U Th lander data bulk Venus U 18-29 ppb" — partial/miss for processes (query/source).
32. WF https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html — hit.
33. WS "Venus surface to orbit ascent delta-v km/s high temperature 92 bar; Venus cloud-top 50 km altitude ascent to orbit delta-v balloon launch Landis" — weak.
34. WS "Venus surface sample return ascent vehicle delta-v to Venus orbit km/s Venus balloon launch 55 km "delta-v" Venus Intrepid OR "Venus Surface Sample Return"" — partial (8.78 km/s snippet).

**Moon, Mars, meteorites, asteroids**
35. WS "Procellarum KREEP Terrane thorium concentration ppm Lunar Prospector Kaguya gamma-ray spectrometer Th U map Jolliff" — hit.
36. WS "lunar KREEP basalt uranium ppm Apollo 14 high-K KREEP U Th concentration sample urKREEP uranium 1.0 ppm" — partial.
37. WF https://ntrs.nasa.gov/citations/20000040504 — hit; WF https://ntrs.nasa.gov/citations/20000040494 — hit.
38. WS "lunar Th/U ratio 3.7 KREEP U concentration ppm bulk Moon U 20 ppb crust average thorium 0.9 ppm Warren Wasson" — hit (Crawford lead, Th/U).
39. WS "Lunar Sample Compendium 14321 uranium ppm thorium ppm KREEP impact melt breccia Apollo 14 U concentration" — partial/miss for 14321 (not fetched).
40. CURL arXiv 1410.6865 (Crawford) — hit; CURL USGS FS 2025-3049 — hit.
41. WS "Yamashita 2010 "Uranium on the Moon: Global distribution and U/Th ratio" Kaguya abstract" — hit (abstract summary).
42. WS "uranium deposit on the Moon claim OR uranium-rich asteroid claim fact check Moon uranium mining helium-3 thorium lunar nuclear fuel resource ppm too low" — partial (Moon claims; no asteroid claims).
43. WS "asteroid mining uranium thorium concentration asteroids meteorite analog Th U ppb "uranium" asteroid resources review Lewis Metal-rich" — partial (no asteroid review; a forum post only).
44. WS "Mars Odyssey GRS global surface Th K Fe abundances Taylor 2006 Th 0.7 ppm K 3000 ppm Hahn crust average Mars uranium" — partial.
45. WS "Martian meteorites uranium ppm nakhlite shergottite Mars crust U Th heat producing elements Mars bulk silicate U 16 ppb Mars Th 56 ppb" — partial/miss for the recalled model values.
46. WS "Taylor et al. 2006 "Bulk composition and early differentiation of Mars" Th K Mars Odyssey GRS surface average Th ppm K ppm" — hit (abstract).
47. WS "Boynton 2007 Concentration of H, Si, Cl, K, Fe, and Th in the low- and mid-latitude regions of Mars Th 0.6 ppm abstract" — partial.
48. WS "CI chondrite uranium abundance ppb thorium ppb Lodders 2021 Palme Jones O'Neill solar system abundances U 7.8 Th 29" — partial; led to the Lodders paper.
49. CURL https://par.nsf.gov/servlets/purl/10642789 (Lodders 2021) — hit (Table 1).
50. WS "ordinary chondrite uranium thorium concentration ppb H L LL chondrites Th 40 ppb U 12 ppb Wasson Kallemeyn compositions of chondrites" — partial (superseded by Lodders).
51. WF Moon, Mars, Earth NSSDC fact sheets (3 fetches) and Mercury fact sheet — hit.

**Earth**
52. WS "Uranium 2024 Resources, Production and Demand Red Book identified resources tonnes U world uranium production 2022 requirements 2023" — hit (snippets).
53. WF https://world-nuclear.org/information-library/nuclear-fuel-cycle/uranium-resources/supply-of-uranium — hit (Red Book 2026 figures as quoted).
54. WS ""Uranium 2026" Red Book NEA IAEA identified resources 1 January 2025 production 2024 tonnes uranium reactor requirements" — partial (existence of the 2026 edition; no headline figures from the OECD-NEA release).
55. WF https://world-nuclear.org/information-library/nuclear-fuel-cycle/mining-of-uranium/world-uranium-mining-production — hit.
56. WF https://world-nuclear.org/information-library/nuclear-fuel-cycle/mining-of-uranium/uranium-mining-overview — hit.
57. WS "Olympic Dam uranium grade U3O8 ppm 0.023% Cigar Lake average grade 17% U3O8 McArthur River grade 2023 reserves" — partial.
58. WS "Olympic Dam resource grade U3O8 kg/t "Olympic Dam" 0.025% U3O8 copper 0.7% uranium by-product BHP resource statement" — hit (snippets).
59. WS "IAEA uranium deposit types classification unconformity-related sandstone-hosted grade % U range tonnes IOCG typical grade" — partial.
60. WF https://world-nuclear.org/information-library/nuclear-fuel-cycle/uranium-resources/geology-of-uranium-deposits — hit.
61. WS "uranium from seawater concentration 3.3 ppb 4.5 billion tonnes adsorbent cost per kg U ORNL PNNL amidoxime review 2023" — hit (snippets).
62. WS "uranium extraction from seawater techno-economic cost $/kg U 2024 review state of the art pilot Kuo PNNL Nature Sustainability adsorbent capacity" — partial.
63. WS "thorium crustal abundance 9.6 ppm USGS Mineral Commodity Summaries thorium reserves monazite world reserves tonnes India Brazil Australia" — partial; CURL USGS MCS 2026 thorium PDF — hit.
64. WS "Rudnick Gao 2003 composition of the continental crust bulk crust U 1.3 ppm Th 5.6 ppm upper crust U 2.7 Th 10.5" — partial; CURL https://www.geol.umd.edu/~rudnick/PDF/Rudnick_Gao_Treatise.pdf — miss: returned a 12,655-byte HTML page, not the PDF (source block; not retried); WF arXiv 1005.4465 — hit (binary, saved, crust table).

**Concentration, scale, transport**
65. WS "uranium mobility U(VI) uranyl soluble oxidizing fluids U(IV) uraninite reduced precipitate redox front concentration factor ore deposit formation requires oxygen water Great Oxidation" — partial (no oxygen-requirement source).
66. WS "UNEP International Resource Panel Global Resources Outlook 2024 global material extraction billion tonnes per year 100 Gt 2020 biomass fossil fuels metal ores nonmetallic minerals" — hit (summaries; report PDF not opened).
67. WS "Mudd uranium mining energy intensity ore grade relationship GJ per tonne U3O8 low grade ore sustainability uranium mining milling Olympic Dam Rossing energy use" — partial.
68. WF Strupczewski IAEA paper — miss: HTTP 402 (paywall at source).
69. WS "comminution energy consumption kWh per tonne ore grinding mining sector share of global electricity 3% Ballantyne Powell benchmarking comminution energy" — partial (ranges).
70. WF https://en.wikipedia.org/wiki/Delta-v_budget — hit (secondary).
71. WS "lunar mass driver electromagnetic launcher Moon surface to Earth orbit cost per kg study NASA space tether launch from Moon Mercury mass driver feasibility" — partial.
72. WF https://space.nss.org/settlement/nasa/spaceres/IV-2apa.html — redirected (301, same site); WF https://nss.org/settlement/nasa/spaceres/IV-2apa.html — hit (cost table).
73. WS "Juno solar-powered Jupiter 5 AU solar flux 50 W/m2 solar arrays power output at Jupiter versus Earth; Saturn solar power insufficient RTG Cassini" — hit (snippets).

Total web calls: about 86 (tools above, counting each search, fetch and download). Scripts: one local Python 3 run (isolated mode) for the Q6 and Q7 arithmetic; one local pdftotext batch. Nothing written outside this file except scratch files in the session scratchpad.
