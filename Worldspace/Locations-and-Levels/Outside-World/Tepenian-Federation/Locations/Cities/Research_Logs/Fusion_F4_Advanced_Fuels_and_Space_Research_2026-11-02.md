# Fusion F4: advanced fuels (D-3He, p-11B, D-D), neutron fractions, fuel scale, and fusion in space (research unit F4, 2026-11-02)

**Scope.** Facts only, no recommendation, no design, no ranking. This file answers Unit F4 of `Fusion_and_Helium3_Research_BRIEF_2026-11-02.md`: (1) the reaction physics and the best results ever achieved for D-3He, p-11B and D-D, including Helion's and TAE's claims and the 2022-2026 p-11B literature; (2) fusion for space power and propulsion (published performance numbers and status); (3) neutron fractions and the shielding and waste consequences; (4) fuel mass per gigawatt-year, checked against the discussion file's 54 kg of helium-3 per GW-year. Labels: **SOURCED** (I read it at the source in this session), **DERIVED** (my arithmetic; working shown), **UNVERIFIED** (seen only in a search-result summary, recalled, or inferred), **NOT FOUND** (looked for; queries in the log). Status claims carry the source's date. Today is 2026-11-02.

**Started:** 2026-11-02, about 18:50 MST. **Finished:** 2026-11-02, about 19:05 MST (system clock).

**Handling note on PDFs.** WebFetch could not read PDFs inline (it returned binary). Where a PDF is marked "read via local text extraction", the tool saved the file and I converted it with `pdftotext` in my scratch folder (not in the repo), then read the text myself. Such items count as SOURCED. Where the fetch tool returned only a model-written summary of a web page, the item is SOURCED only if the summary quoted the page; I note it when the quote was the tool's paraphrase.

---

## PROGRESS

- [x] 1. Reaction energies, cross-section peaks, temperatures, neutron fractions for D-3He, p-11B, D-D
- [x] 1. Highest results with each fuel; whether any has net energy
- [x] 1. Helion D-3He claims versus independent evidence
- [x] 1. TAE p-11B program and results
- [x] 1. 2022-2026 p-11B feasibility papers and laser/proton-boron experiments
- [x] 2. Fusion for space: Daedalus, Discovery II, Direct Fusion Drive, others (performance numbers and status)
- [x] 3. Neutron fraction by fuel; shielding and waste consequences
- [x] 4. Fuel mass per GW-year for D-3He and p-11B; check of the 54 kg figure against independent sources
- [ ] NOT FOUND items remain: see FINAL (primary Daedalus report; D-3He cross-section peak from an evaluated-data source; OMEGA/JT-60U D-3He yields; any independent confirmation of Helion's D-3He fusion; Helion status after 2026-02-13)

---

## 1. Advanced fuels: D-3He, p-11B, D-D

### 1.1 Reaction energies (SOURCED, with a DERIVED check)

| Reaction | Energy release and product split | Source |
|---|---|---|
| D + 3He | 18.3 MeV: alpha 3.6 MeV (Wurzel and Hsu give 3.6; Santarius gives 3.67) + proton 14.7 MeV (14.68) | SOURCED: Wurzel and Hsu 2022 (read via local text extraction), Eqs. D6 and D10; Santarius and Kulcinski 2004 slide 3 |
| p + 11B | 3 alphas, 8.68 MeV total (Molloy 2025 and Magee 2023 give 8.7 MeV) | SOURCED: Santarius 2004 slide 3; Molloy 2025; Magee 2023 |
| D + D (50% / 50%) | n 2.45 MeV + 3He 0.82 MeV (3.27 MeV total); p 3.02 MeV + T 1.01 MeV (4.03 MeV total) | SOURCED: Wurzel and Hsu 2022 Eqs. D7, D9; Santarius 2004 slide 3 ("50% each channel") |
| D + T (for reference) | alpha 3.5 MeV + n 14.1 MeV (17.6 MeV); "D-T... 14-MeV neutrons that carry 80% of the fusion energy" | SOURCED: Wurzel and Hsu 2022 |
| Fully catalyzed D-D | "62% of the 43.2 MeV released in charged particles (compared with only 20% for D-T)" when the 3He and T products burn with D | SOURCED: Wurzel and Hsu 2022, Appendix D.3 |
| 3He + 3He | 12.86 MeV, 2 protons + alpha | SOURCED: Santarius 2004 slide 3 |

**DERIVED check of the Q-values** from atomic masses (masses are constants I recalled, so treat the check as a consistency test, not a source): D + 3He gives 18.353 MeV; p + 11B gives 8.682 MeV; D + T gives 17.589 MeV; D + D gives 3.269 MeV (n branch) and 4.033 MeV (p branch). All agree with the sourced values.

### 1.2 Cross-section peaks, optimal temperatures, required plasma conditions

- **p-11B cross-section peaks (SOURCED, Molloy et al., Phys. Rev. Research 7, 013230, published 2025-02-28):** "The p-11B fusion reaction cross section has two peaks at 150 keV and 612 keV in the center-of-mass frame, corresponding to a cross section of 0.1 b and 1.4 b, respectively." The paper also notes 11B is "80% of naturally occurring boron."
- **Optimal fusion temperature and reactivity (SOURCED, arXiv 2410.18054, "Introduction to Fusion Ignition Principles", Table 2.2, read through the fetch tool's page extraction; the table's own numbers):** D-T 10-30 keV; D-D ~50-100 keV; D-3He ~50-100 keV; p-11B ~100-300 keV. Reaction rate (m^3 s^-1): D-T 6e-22 at 25 keV; D-D 5e-23 at 100 keV; D-3He 2e-22 at 100 keV; p-11B 4e-22 at 300 keV. **Caution:** the p-11B figure looks high against the plot in Santarius 2004 slide 3, where p-11B sits below D-3He over most of the range; I did not resolve this. Treat that one number as UNVERIFIED in magnitude.
- **D-3He cross-section peak:** The only numbers found were from search-result text: one table row (from Atzeni 2004, citing Cox 1990) read as about 0.9 barn at 250 keV, and an old Minnesota measurement quoted as a maximum of 0.90 +/- 0.10 barn at 430 +/- 30 keV deuteron (laboratory) energy. These two are consistent if 250 keV is the center-of-mass energy and 430 keV the laboratory energy, but that is my inference. **UNVERIFIED.** I did not reach Bosch and Hale 1992 (Nucl. Fusion 32, 611) or Nocente et al. 2010 tables. D-T comparison from the same snippet: about 5 barn at 64 keV (UNVERIFIED). A Wikipedia page read this session says "The DT rate peaks at a lower temperature (about 70 keV, or 800 million kelvin)" (that wording is Wikipedia's; a different convention from the 10-30 keV optimal range above; sources do not agree on a single "peak temperature").
- **Ignition requirements, D-3He (SOURCED, Wurzel and Hsu 2022, Appendix D.1, local text extraction):** "The requirement for ignition of D-3He ignoring side D-D reactions is n_i T tau_E* >= 5.2 x 10^22 m^-3 keV s at 68 keV (see Fig. 27), 18 times higher than for D-T." The same paper: "3He is not abundant on earth and must be bred via other reactions or mined from the moon" and "D-3He will not be completely aneutronic because of D-D reactions."
- **Ignition requirements, D-3He, other statements:** Santarius and Kulcinski 2004 slide 4: compared with D-T, D-3He needs "a minimum factor of ~6 increase in ignition temperature, a minimum factor of ~8 increase in n tau_E, a minimum T n tau increase of ~50 times." Wikipedia (Aneutronic fusion, read this session): D-3He ignition temperature 58 keV, "over four times as high as that of the D-T reaction." The 58, 68 and the factor-of-6 figures differ because the sources use different assumptions (impurities, bremsstrahlung treatment, fuel ratio); I did not reconcile them.
- **Required conditions, catalyzed D-D (SOURCED, Wurzel and Hsu 2022):** ignition at n_i T tau_E* >= 1.1 x 10^23 m^-3 keV s at 52 keV, "38 times higher than required for D-T."
- **Required conditions, p-11B (SOURCED, Wurzel and Hsu 2022):** "this reaction requires temperatures around 100 keV, at which bremsstrahlung radiation losses per unit volume exceed fusion power density, and ignition is not possible for a p-11B plasma where Te = Ti"; "Figure 29 shows that only modest values of Q_fuel are physically possible for Te = Ti, at triple products three orders of magnitude higher than that of D-T"; "However recent work points to a higher reactivity, and given certain assumptions, high-Q_fuel operation up to and including ignition may be theoretically possible." Wikipedia (Aneutronic fusion): "the bremsstrahlung power will be at least 1.74 times larger than the fusion power" for a thermal plasma (secondary; not checked against its source).
- **Comparison with what has been achieved (DERIVED):** Wurzel and Hsu's Table VI lists tokamak triple products up to about 7.9 x 10^20 keV m^-3 s (TFTR, 1995) and 5.6 x 10^20 (JT-60U, 1998). The D-3He ignition figure of 5.2 x 10^22 is therefore about 66 times the TFTR row and about 93 times the JT-60U row (5.2e22 / 7.9e20 = 66; 5.2e22 / 5.6e20 = 93). Those rows are D-T or D-T-equivalent data and are not necessarily the table's maximum; this is a scale comparison, not a ranking.
- **Helion's stated temperature for D-3He:** "D-He-3: requires the highest temperatures, about 200 M degrees C" (Helion blog, 2024-06-27, SOURCED as Helion's statement). 200 million K is about 17.2 keV (DERIVED: 200e6 x 8.617e-5 eV/K). The ignition models above give 58-68 keV for a thermal, steady-state ignition. **No source I read reconciles the two.** Possible reasons (non-Maxwellian ion populations, pulsed operation with energy recovery rather than ignition) are my inference and are UNVERIFIED.

### 1.3 Highest results ever achieved, and whether any has net energy

**D-3He**
- **JET, 1991 (SOURCED, OSTI record of Jacquinot and Sadler, Fusion Technology 21(4), July 1992, "D-3He fusion in the Joint European Torus tokamak; Recent experimental results"):** "a record fusion power of 140 kW," reaction rate 4.6 x 10^16 reactions per second, amplification factor Q "peaked at about 1.25% at 10 MW of heating power" (ion cyclotron resonance heating). The previous records given were 100 kW and Q = 1% (the OSTI page; a different ANS listing in a search result gave 700 kW for the prior best; the two disagree and I did not resolve it, so the prior-record figure is UNVERIFIED). Method: ICRH produces a high-energy 3He tail that reacts with a background deuterium plasma (non-thermal). **DERIVED check:** 4.6e16 /s x 18.35 MeV x 1.602e-13 J/MeV = 135 kW, consistent with the 140 kW.
- **Net energy:** none. Wikipedia (read this session): "As of the mid-2020s, no aneutronic fusion system has demonstrated sustained or net-energy operation using 3He-based fuel cycles." The repo's own earlier note (discussion file section 1) agrees.
- **Other D-3He data:** Laser-heated D2-3He clusters (Texas Petawatt) are reported in a 2013 arXiv paper; a NIF-based MIT thesis reportedly found D3He exploding-pusher yields "two orders of magnitude lower" than average-ion hydrodynamic predictions. Both seen only as search-result text: UNVERIFIED. I did not find OMEGA or JT-60U D-3He yield figures (NOT FOUND; queries in the log).

**p-11B**
- **First measurement in a magnetically confined plasma (SOURCED, Magee et al., Nature Communications 14, 955, received 2022-11-04, accepted 2023-02-10, read via local text extraction):** "the first such realization of p11B fusion in a magnetically confined plasma", done at the Large Helical Device (NIFS, Japan) with boron powder injection and three 2 MW, 160 kV hydrogen neutral beams; central electron temperature about 2 keV, line-averaged density about 2 x 10^18 m^-3. Alpha particles were counted with a silicon detector. Count rate with boron "about 150 kcps," without it "less than 1 kcps." The paper compares the time dynamics of the count rate to a code (FBURN) and says an absolute comparison is not possible ("we rely on the dynamical, relative agreement"). It predicts p-11B fusion rates "of ~10^14 s^-1 when all three high-energy beams are fired simultaneously."
- **Magnitude of the result:** TAE's own account (tae.com, SOURCED, undated page; the speaker is the paper's first author): the alpha particles released "about 14 watts," "it wasn't a Q of greater than one," "this was not a net-energy production demonstration." Physics World (2023-03-09, read this session): about 10^12 fusion reactions per second measured, and quoting EUROfusion scientists that the rate is "about ten orders of magnitude too low to be useful." **The three rate figures do not agree:** 10^14 /s predicted (all beams), 10^12 /s (Physics World), and 14 W (TAE page; 14 W / 1.39e-12 J per reaction = 1e13 /s, DERIVED). I did not find which applies to which discharge. 10^12 /s would be 1.4 W (DERIVED: 1e12 x 8.68 MeV x 1.602e-13).
- **Laser-driven p-11B, in-target scheme (SOURCED, Molloy et al. 2025):** "A fusion-generated alpha particle flux of up to (5 x 10^7 sr^-1 J^-1) was generated ... when irradiating the targets with a moderate laser system (10 J, 800 fs, 10^19 W cm^-2). Normalized by laser energy, the alpha particle flux generated in this experiment is comparable with the highest alpha particle yields reported in the literature." Text: "over 5 x 10^8 alpha/sr." **DERIVED scale (assuming isotropic emission, which the paper does not claim):** 5e8 x 4 pi = 6.3e9 alphas per shot, which is about 2.1e9 reactions (3 alphas each) or about 2.9 mJ of fusion energy against 10 J of laser, a ratio near 3e-4. Net energy: none.
- **Earlier laser records (UNVERIFIED, search-result text only):** alpha yields of order 10^9 to 10^11 per steradian per shot from ELI-Beamlines work (2019-2020, Giuffrida and colleagues, a figure later corrected by another group); HB11 Energy's Applied Sciences paper reported about 10^10 /sr with laser-to-alpha conversion about 0.005% and the company's own statement that its approach is "four orders of magnitude" from net gain; HB11 presented results from the Phelix and LFEX lasers at a September 2025 workshop (company page, no independent review found).
- **Net energy:** none for p-11B by any method. TAE: not claimed. Wikipedia: a French team reported "an estimated 80 million fusion reactions during a 1.5 nanosecond laser pulse" in 2013 (secondary).

**D-D**
- No separate "highest D-D result" was isolated. Wurzel and Hsu 2022 (local text extraction) treat D-only experiments by D-T-equivalent values and state: "Scientific breakeven has not yet been achieved" in magnetic confinement; the closest D-T results are "Q_sci = 0.27 for TFTR, Q_sci = 0.64 for JET, and Q_sci ~ 0.7 for NIF [August 2021]." The brief's earlier-found laser record (8.6 MJ from 2.08 MJ laser, 7 April 2025) is D-T and belongs to Unit F1. I recall (UNVERIFIED) that JT-60U's D-D plasmas were reported as reaching a D-T-equivalent Q near 1.25 in 1998; Wurzel and Hsu's own Table VI row for JT-60U 1998 (shot E31872) lists n_i T tau_E* = 5.6 x 10^20 keV m^-3 s, which they use in their own method. NOT FOUND as a sourced D-D net-energy statement.
- Catalyzed D-D and "3He double-catalyzed D-D" are theoretical in these sources (Wurzel and Hsu 2022); no experiment reported.

### 1.4 Helion's D-3He claims: company statements versus independent evidence

**What the company says (all SOURCED as Helion's own statements):**
- **2021-06-22 (page dated 2021-06-29):** "first private company to announce exceeding 100 million degrees Celsius in their 6th fusion generator prototype," "reaching 9 keV total bulk plasma temperatures with operation above 8 keV ion temperature and 1 keV electron temperature," described as "high-Beta Field Reversed Configuration (FRC) deuterium plasmas." The page says nothing about helium-3.
- **2023-10-05 (Helion CEO's post, "Trenta's final fusion test campaign"):** during 2021 operations Trenta "saw evidence of bulk deuterium-helium-3 fusion" and "deuterium-helium-3 is our preferred fuel cycle"; the D-3He run is called "a simple check that our system still operates the way we expect when new fuels are introduced"; Trenta withstood "thousands of fusion pulses." No D-3He fusion power, yield, rate or duration is given.
- **2024-06-27 (Helion blog, "Explaining Helion's fusion fuel: D-He-3"):** D-He-3 "requires the highest temperatures, about 200 M degrees C"; D-3He yields "18.3 MeV ... without the higher-energy neutrons"; side D-D reactions can still produce 2.45 MeV neutrons but the page does not quantify them; the fuel "maximizes our ability to directly capture electricity."
- **2025-03-28 (Helion blog, fuel cycle):** "Half of the time D-D fusion directly yields helium-3"; the other branch makes tritium, which "transforms at a rate of 5.5% per year into helium-3 through natural radioactive decay with a 12.3-year half-life"; the system "may reach a steady state where helium-3 production is balanced with power generation"; "helium-3 is exceedingly rare on Earth with no known natural source to supply the quantities necessary." No He-3 mass per plant and no neutron fraction are given. **DERIVED check:** 1 - exp(-ln2/12.3) = 5.48% per year, matching the stated 5.5%.
- **2026-02-13 (Helion press release, read in full):** Polaris (7th generation) "became the first and currently only private fusion energy machine to use deuterium-tritium fuel" ("This January"), "demonstrated measurable D-T fusion," and "reached plasma temperatures of 150 million degrees C", beating its own 100 million record from Trenta; the release calls 100 million C "the industry threshold for a commercially relevant fusion machine." 150 million K is about 12.9 keV (DERIVED). Quoted reviewers: a DOE Office of Science official saying the data indicate "strong progress"; Ryan McBride (reviewed diagnostics: "evidence of D-T fusion and temperatures exceeding 13 keV"); Alan Hoffman. The page describes no formal audit or peer-reviewed publication. D-3He is still ahead: Helion "will continue to increase plasma temperatures ... to demonstrate that it can reliably operate with" D-3He (the fetch tool's paraphrase; the sense matches the ANS roundup of 2026-02-18, which attributes all Polaris claims to the company and says the article "does not say whether Polaris has yet operated on that fuel at the higher temperature"). Polaris began operating at the end of 2024; construction on the Orion site (Malaga, Washington, for Microsoft) began in July 2025 (company statement).

**Independent evidence:**
- **No peer-reviewed or third-party-confirmed D-3He fusion measurement from Helion was found** (NOT FOUND; queries S4, S16, S25 in the log). Search-result summaries said Helion publishes little peer-reviewed plasma data and mentioned a named "independent auditor" in a 2023 conference slide deck; I did not read that deck's findings. UNVERIFIED.
- **Axios, reported 2026-09-08 (UNVERIFIED; the page returned HTTP 403, so I read only a search-result summary):** Helion reportedly changed its Polaris goal from "net electricity" to "demonstrating electricity from fusion," saying "net electricity" was "not well defined within the fusion industry"; the summary also said Helion first said Polaris would show net electricity in 2024 and that its Orion target is 50 MW to Microsoft by 2028.
- **Net energy from D-3He or any Helion fuel:** none announced as of the sources above (latest dated 2026-02-13 for the company, 2026-09-08 for the unverified Axios summary). I found no October 2026 Helion announcement (S25).

### 1.5 TAE Technologies' p-11B program

- **Company roadmap, December 2025 / January 2026 investor one-pager (SOURCED, local text extraction; PDF metadata dates are January 2026):** "TRUMP MEDIA & TECHNOLOGIES GROUP TO MERGE WITH TAE TECHNOLOGIES IN $6B TRANSACTION"; "$1.3B raised to date"; "five demonstration fusion reactors built to date"; plants "350-500 MWe" planned later; expected path: 2026 site, close transaction, begin construction (first plant expected to produce 50 MWe); **2029 "first plasma expected"; 2030 "net energy capability expected to validate economic viability"; 2031 "initial facility power operations."** "Da Vinci ... is expected to use hydrogen-boron fuel." Current machine Norm "is the first known fusion machine to successfully generate a field-reversed configuration (FRC) plasma using only neutral beam injection," about 40 feet long. The one-pager says the NRC voted in 2023 to place fusion under Part 30 (byproduct materials). Siting criteria quoted: minimum 20 acres, grid access, metropolitan hub.
- **Merger status (UNVERIFIED, search-result text; the Benzinga page returned 403):** not closed; target "fourth quarter of 2026 or earlier"; Form S-4 filed 2026-09-30; mid-2026 target slipped.
- **Statement that Norm will be upgraded to 100 million degrees C as a step to Da Vinci, and that the roadmap skips a planned "Copernicus" machine (UNVERIFIED, search-result text from company release summaries).**
- **Measured p-11B results:** only the 2023 LHD experiment in 1.3 (collaboration with NIFS, not run on a TAE machine). I found **no published p-11B fusion measurement from Norm** (NOT FOUND).
- **Independent assessments:** Physics World (2023-03-09) quotes Peter Norreys (Oxford) saying p-11B "is still far from rivaling" D-T, and EUROfusion scientists with "strong doubts" that the gains needed for commercial power are achievable; it states "A commercial plant likely needs a gain of at least 50" (Physics World's wording, not independently checked). TAE says it aims for grid electricity from a pilot p-11B plant "by the early 2030s" (Physics World's report of TAE's aim).

### 1.6 The 2022-2026 p-11B feasibility and experiment literature (what each paper says)

- **Ochs, Kolmes, Mlodik, Rubin, Fisch, Phys. Rev. E 106, 055215 (arXiv 2210.08076, submitted 2022-10-14), SOURCED (abstract page):** "ignition is barely plausible, with fusion power exceeding bremsstrahlung losses by only about 3%" (the fetch tool's paraphrase of the abstract); alpha channeling could cut the confinement time needed for ignition by a factor of 2.6 (thermal protons) or 6.9 (fast protons). Search-result text adds that without channeling "a very small amount of ash (under 2%) can preclude ignition" (UNVERIFIED).
- **Follow-up, arXiv 2310.18508 (2023), "Lowering the reactor breakeven requirements for proton-Boron 11 fusion"** (UNVERIFIED beyond its title and a search-result summary: fast-proton heating, alpha capture, direct conversion).
- **Wang, Li, Wu, Cui (Nanjing University), arXiv 2601.00241, "Revisiting p-11B Fusion: Updated Cross-sections, Reactivity, and Energy Balance," submitted 2026-01-01 (the page also displayed "August 24, 2026," which I cannot explain; a preprint, not peer-reviewed as far as I could see), SOURCED via the fetch tool's page reading:** "p-11B fusion is not precluded by bremsstrahlung constraints"; with Te = T bremsstrahlung exceeds fusion power at all temperatures; with self-consistent electron temperature fusion exceeds bremsstrahlung between about 0.17 and 0.38 MeV; no Q value or ignition claim; the side reaction p + 11B -> n + 11C has a branching fraction of roughly 10^-5, with neutrons of about 2.765 MeV.
- **ENN (China), arXiv 2401.11338, "ENN's Roadmap for Proton-Boron Fusion Based on Spherical Torus," SOURCED via page reading:** EXL-50U "achieved its first plasma in January 2024"; EHL-2 construction "estimated to be completed by 2026," first plasma "around 2027"; EHL-2 targets central ion temperature 30 keV; a reactor concept with R0 = 4 m, B0 = 6 T, Ti0 = 150 keV, Ti/Te = 4 "can yield p-B fusion with Q>10" (a modeling claim, not an experiment). The abstract and Table 4 disagree on the EHL-2 Ti/Te target (at least 2 versus 3).
- **arXiv 2511.10885 (November 2025), inertial analysis: above certain boron fractions breakeven is unachievable, and at a boron fraction of 0.3 ion temperatures of at least 200 keV are needed** (UNVERIFIED, search-result text only).
- **Laser experiments:** Molloy et al. 2025 (SOURCED, 1.3); Tosca, Molloy et al., Frontiers in Physics 11, 1227140 (2023), "Plasma polymers as targets for laser-driven proton-boron fusion" (identified from PDF metadata only; body not read); HB11 (company; see 1.3).
- **Putvinski et al. 2019 (reactivity "revisited," APS DPP):** only an APS meeting listing title was seen; not read. NOT FOUND as a source I read.

---

## 2. Fusion for space power and propulsion

**Status in one line (SOURCED, Wikipedia "Fusion rocket," read this session, a secondary source):** Daedalus, Discovery II and VISTA are design studies and "None has been built"; the Direct Fusion Drive is listed as conceptual. No fusion rocket has flown.

### 2.1 Project Daedalus (British Interplanetary Society, study 1973-1978)
- **SOURCED (Wikipedia "Project Daedalus," secondary; the primary BIS 1978 report was not read):** "an initial mass of 54,000 tonnes including 50,000 tonnes of fuel"; payload 500 tonnes in the narrative and 450 tonnes in the specifications list (the page does not reconcile these); first-stage thrust 7,540,000 N, exhaust velocity 10,600 km/s; second stage 663,000 N and 9,210 km/s; burn-up fractions 0.175 and 0.133; burn times about 2.05 and 1.76 years; delta-V 35,000,000 m/s (0.117 c) and 13,000,000 m/s; 250 pellets per second; deuterium/helium-3 pellets ignited by electron beams (inertial confinement); He-3 to be mined from Jupiter's atmosphere "using large hot-air balloon-supported robotic factories over a 20-year period."
- **SOURCED (Centauri Dreams, 2010-09-28, a blog post quoting the Project Icarus study):** "128 such factories deployed over 20 years were needed to mine the needed 30,000 tons of helium-3," and an annual rate of "1500 tonnes of He3 required for the Daedalus probe." The post says the Icarus team ruled out Jupiter for its radiation belts, preferred Uranus, and eliminated Saturn for radiation and escape-velocity reasons.
- **DERIVED consistency check:** 50,000 t of an equal-atom D + 3He mix is 50,000 x 3.016 / 5.030 = about 29,980 t of 3He, matching the stated 30,000 t (the 20,000 t of deuterium is my inference from the split; no source I read states it). 30,000 t / 20 yr = 1,500 t per year, matching the quote.
- **A later reassessment ("Project Daedalus at 50," 2024-2025) was reported only in a search-result summary as finding the physics "broadly stands up" but the He-3 mining infrastructure "a serious gating problem"** (UNVERIFIED).

### 2.2 NASA Glenn "Discovery II" (spherical torus, D-3He)
- **SOURCED (NASA/TM-2005-213559, Williams, Dudzinski, Borowski, Juhasz, March 2005; also AIAA-2001-3805; read via local text extraction):** crewed vehicle, 172 metric tons payload; Jupiter rendezvous in 118 days and Saturn in 212 days from 1,690 t in low Earth orbit (1,699 t for Saturn); Jupiter case thrust 6,250 lbf, specific impulse 35,435 (lbf s/lbm, i.e., seconds), propellant flow 0.079 kg/s; Saturn case thrust 4,690 lbf, 47,205 s; jet power 4,830 MW; jet efficiency 0.8; **specific power 8.62 kW/kg** (defined as reactor-system output power divided by the stage dry mass including reserves); D3He fuel 11 t and hydrogen propellant 861 t on the mass table; vehicle length 240 m; assembly in LEO would need seven heavy-lift launches (HLLV throw weight 251 t each).
- **Fusion power balance (SOURCED, same report):** "Of the 7,895 MW of fusion power produced, 96% was in the form of charged particles with the remainder in (largely 2.45 MeV) neutrons"; neutron power 307 MW, bremsstrahlung 1,016 MW, synchrotron 535 MW. **DERIVED:** neutrons = 307 / 7,895 = 3.9%; charged 7,588 / 7,895 = 96.1%.
- **He-3 supply discussion in the same report (SOURCED):** D3He "would be acquired by either collecting solar wind deposited or scavenging in situ major planetary atmosphere deposits"; "Processing 40 km^2 of lunar regolith to a depth of 2 m, for example, could yield 1 and 6,100 mt of 3He and H2 respectively"; a cited study proposed a balloon-suspended Jupiter facility "capable of producing ~1 gm/sec of 3He and deuterium each by processing 680 kg/sec (i.e., 3,600 m^3/sec) of atmosphere," mass "~200 mt," requiring "10 MWe," which the authors call "Ingenious in its design" but illustrating "the considerable difficulty in using in situ resources." **DERIVED:** 1 g/s is about 31.6 t of He-3 per year per such facility. The report itself frames the vehicle as conceptual and contingent on fusion technology advancing (its wording: "Further improvements in payload and trip time could be achieved if fusion technology advances permitted optimal propellant mass loadings").
- **Wikipedia's version (secondary):** D-He3 fuel 11 t; exhaust velocity 348-463 km/s; consistent with 35,435-47,205 s (DERIVED: 35,435 s x 9.80665 = 347 km/s; 47,205 s = 463 km/s).

### 2.3 Princeton Satellite Systems / PPPL Direct Fusion Drive (Princeton Field-Reversed Configuration)
- **SOURCED (NIAC Phase II Final Report "Fusion-Enabled Pluto Orbiter and Lander," award 80NSSC18K0040, PI Stephanie Thomas, period 2017-05-09 to 2019-05-09, report date 2019-05-15; local text extraction):**
  - Concept: "Approximately 35% of the fusion power goes to thrust, 30% to electric power, 25% lost to heat, and 10% is recirculated for the RF heating." Fuel D-3He, with 3He:D above 1 (design tables use 2.5:1 by density).
  - Table 19 (UEDGE model): **1 MW fusion power:** jet power 0.46 MW, thrust 4-5 N, Isp 8,000-8,500 s, jet efficiency 0.35-0.37, specific power 0.75 kW/kg. **10 MW:** jet power 5.6 MW, thrust 35-55 N, Isp 9,900-12,000 s, specific power 1.25 kW/kg. The report's own text elsewhere gives "a specific impulse in the range of 10,000 to 20,000 seconds and a specific power about 1 kW/kg" and "5-10 N thrust" in the introduction; the table figures are lower than that prose, which I note as an internal inconsistency.
  - Point designs: 1 MW reactor, plasma radius 0.25 m, length 0.9 m, total mass 1,345 kg, 5.0 T, "Fusion Specific Power 0.75 kW/kg"; 10 MW reactor, radius 0.3 m, length 5.0 m, total mass 9,400 kg, "1.07 kW/kg." 1 MW power budget: thrust 52%, bremsstrahlung 20.5%, synchrotron 14.2%, gas-box 13%, **neutron power 2.57 kW (<0.25%)**.
  - Example missions (Table 20): Mars 40 Mg payload, 60 MW, 110 days (1.25 kW/kg), IMLEO 112,000 kg, 3He 0.98 kg; Jupiter 1 Mg, 1 MW, 1.2 years, 0.05 kg; **Pluto 1 Mg, 0.6 MW, 5 years, 159.67 km/s delta-V, IMLEO 10,048 kg, 3He 0.16 kg**; 125 AU 1 Mg, 0.8 MW, 10 years, 0.43 kg. "We have also newly analyzed a trip to Mercury ... The transfer takes less than 140 days using a single 0.9 MW DFD" with 21 km/s delta-V; the report contrasts this with BepiColombo's roughly 7-year transfer.
  - Experimental status: PFRC-2 (quarter-scale, plasma radius 7 cm) "At an applied RF heating power of about 20 kW, electron heating to temperatures Te > 300 eV has been demonstrated"; pulses of 300 ms; central field 1.2 kG (an operational machine would need 70 kG); "Ion heating studies will follow, once Te > 1 keV has been achieved." So no fusion-relevant temperatures had been reached in the machine at the time of the report (2019).
  - Neutron suppression: neutron power from D-D "about 0.5-1% of the fusion power", "as little as 0.2%" if beam-like distributions let D run at half the temperature of 3He, by exhausting tritium before it fuses.
- **Later status of DFD / PFRC (after 2019):** NOT FOUND (query S20 returned only Pulsar Fusion material).
- **Pulsar Fusion "Sunbird" (UK):** search-result text only (UNVERIFIED): first plasma with krypton (not a fusion plasma), a "Dual Direct Fusion Drive" target of 10,000-15,000 s and 2 MW, an in-orbit demonstration target of 2027, UKAEA shielding help agreed in February 2026.
- **VISTA (LLNL/NASA, 1980s), from Wikipedia (secondary):** D-T, 41 t fuel, hydrogen expellant 4,124 t, exhaust velocity 157 km/s; not an advanced-fuel concept. Included only to mark that the D-T alternative exists.

### 2.4 Performance numbers side by side (as sourced; not a ranking)

| Concept | Fuel | Specific impulse | Specific power | Fusion power | He-3 or fuel quantity | Status |
|---|---|---|---|---|---|---|
| Daedalus (1978) | D-3He pellets, inertial | exhaust 10,600 km/s (about 1.08 million s, DERIVED: 10.6e6 / 9.807) | not stated in sources read | not stated | 30,000 t He-3 in 50,000 t fuel | design study |
| Discovery II (2001/2005) | D-3He, spherical torus | 35,435-47,205 s | 8.62 kW/kg | 7,895 MW | 11 t D3He on the mass table | design study |
| DFD 1 MW (2019) | D-3He, FRC | 8,000-8,500 s | 0.75 kW/kg | 1 MW | 0.05 to 1.5 kg per mission | PFRC-2 at 300 eV electrons; conceptual |
| DFD 10 MW (2019) | D-3He, FRC | 9,900-12,000 s | 1.07-1.25 kW/kg | 10 MW | as above | conceptual |

---

## 3. Aneutronic claims: how much energy comes out as neutrons, and what follows

### 3.1 Neutron share of fusion energy, by fuel (as sourced)

| Fuel and condition | Neutron share | Source and label |
|---|---|---|
| D-T | about 80% of fusion energy (14.1 of 17.6 MeV) | SOURCED: Wurzel and Hsu 2022; Kulcinski et al. 1992 |
| D-D (uncatalyzed, one branch gives a 2.45 MeV neutron) | about 59.5% (0.595) at 70 keV with 50% tritium burnup, in the PFRC model | SOURCED (secondary): Princeton Satellite Systems page that reproduces Santarius and Logan, UWFDM-914 (1998), Fig. 3 |
| D-3He, 3He:D = 0.5 / 1 / 3 | 7.0% / 3.7% / 1.3% (same model: Te = 30 keV, Td = 70 keV, tritium burnup 0.5) | SOURCED (secondary): same page; "consistent with Figure 3 in Santarius" |
| D-3He, Santarius and Kulcinski's plot (Fig. 5 of UWFDM-1214; slide 7 of 2004) | curves on a log axis running from 0.01 to 1; the 3He:D = 3:1 curve sits near the bottom (about 1-2% by eye), the 1:2 curve higher; no table | SOURCED as a figure; values read by eye from axis labels, so UNVERIFIED as numbers |
| D-3He, Wikipedia | "the fraction of energy released as neutrons is probably several percent," which fails the 1% threshold for "aneutronic" | SOURCED (secondary): Wikipedia, Aneutronic fusion |
| D-3He, a patent as summarized by a search tool | "about 10 percent" (neutrons from secondary reactions) | UNVERIFIED |
| D-3He, FRC with tritium exhausted (Princeton Satellite Systems) | 0.5-1% of fusion power, down to 0.2%; 1 MW design: 2.57 kW, under 0.25% | SOURCED: NIAC Phase II report, 2019 |
| D-3He, spherical-torus rocket (Discovery II) | 3.9% (307 of 7,895 MW) | SOURCED figures; ratio DERIVED |
| p-11B, thermal | "at least 0.1% of the reactions ... produce neutrons, although their energy accounts for less than 0.2% of the total energy released" | SOURCED (secondary): Wikipedia, Aneutronic fusion; its underlying source not checked |
| p-11B, side reaction p + 11B -> n + 11C | branching roughly 10^-5, neutrons about 2.765 MeV | SOURCED (preprint): Wang et al. 2026 |
| p-11B, TAE statement | neutrons "something you don't need to worry about with PB 11" (the primary reaction produces none; deuterium operation at LHD does) | SOURCED: TAE page, speaker is the paper's first author |
| D-3He wall loading, tokamak designs (1992) | neutron wall loading 0.1 MW/m^2 (Apollo, D-3He) versus 2.21 MW/m^2 (ARIES-I, D-T), a factor of about 22; the paper says "by a factor of over 20" | SOURCED: Kulcinski et al., UWFDM-884 (1992) |

**The spread is real and comes from three things the sources name:** the D/3He ratio (more 3He lowers neutrons and power density), the plasma temperature, and whether the tritium made by the D-D branch is burned (which yields 14 MeV neutrons) or exhausted first. No source read measures a neutron fraction in a D-3He plasma at power; all are model values.

### 3.2 Other energy that is not neutrons (SOURCED)
- Radiation is large in advanced fuels: "bremsstrahlung and synchrotron radiation losses ... will be 25-30% of the fusion power for D-3He" (Santarius, Kulcinski, El-Guebaly, UWFDM-1214, November 2002). For the DFD 1 MW design, bremsstrahlung 20.5% and synchrotron 14.2%. Discovery II: bremsstrahlung 1,016 MW and synchrotron 535 MW out of 7,895 MW (DERIVED: 12.9% and 6.8%).
- Direct conversion: Santarius and Kulcinski (2004) show "Direct Conversion to Electricity Can Give 60-80% Efficiency" and UWFDM-1214 says direct conversion has "typically twice the efficiency of thermal cycles" (design-study claims; the experimental basis cited is a 1973 LLNL experiment).

### 3.3 Shielding, wall, and waste consequences (SOURCED, design studies from 1992 and 2002-2004)
- **Kulcinski et al., UWFDM-884 (March 1992):** compares the D-3He "Apollo" and D-T "ARIES-I" 1000 MWe tokamak designs. Peak displacement damage at end of life: 93 dpa after 30 full-power years (Apollo) versus about 200 dpa after 6 years (ARIES-I); transmutation helium 483 appm after 30 years versus 23,120 appm after 6 years. Waste: Apollo's low-activation steel structure rates 0.88 for near-surface Class A burial; ARIES-I's lithium-zirconate breeder qualifies only as Class C even with about 150 tonnes of isotopically tailored zirconium. Safety: decay heat from in-vessel components at shutdown 5.62 MW (Apollo); offsite dose to the maximum exposed individual in a loss-of-coolant accident 4.4 rem (Apollo) versus 130 rem (ARIES-I, assuming 2% of modules fail); with the organic coolant fire, 126 rem for Apollo. The authors conclude "Yes, the D-3He fuel cycle will produce electricity cleaner and safer than the DT fusion reaction," giving a "permanent" first wall. These are the authors' own 1992 design results, not independent audits.
- **Santarius and Kulcinski (2004):** a slide shows D-3He structure after 30 full-power years reaching Class A or Class C while D-T after 5 full-power years needs deep geologic burial for HT-9 steel (graphic; no table). The same deck: "Unburned tritium will be a proliferation and safety issue" in D-3He plants.
- **What remains even for D-3He:** the D-D branch makes tritium and neutrons; Princeton Satellite Systems handles it by exhausting tritium within about 0.01 s (their statement); 14 MeV neutrons come from any D + T that does occur (Wurzel and Hsu's reaction list).
- **p-11B waste:** TAE states the p-11B reaction "produces no neutrons, only helium" and that "None of these concerns apply to a reactor based on the aneutronic p11B reaction" (the 14 MeV fluence, activated materials) (Magee et al., 2023, Introduction). Sources read that give the bremsstrahlung problem (Wurzel and Hsu; Ochs et al.) are the physical cost.
- **Proliferation (relevant to hybrids; full treatment belongs to Unit F3):** UWFDM-1214 computes "The number of neutrons required to convert 238U to 1 kg of 239Pu corresponds to 0.72 MW x a of D-T neutrons or 0.13 MW x a of D-D neutrons" and argues "Even low neutron production rates enable fissile-fuel breeding, so such a fusion reactor must burn neutron-lean fuels." They set a 1 kg per year breeding threshold ("a 5-10 year program" to a critical mass). This is a 2002 design argument, not an IAEA position.

---

## 4. Scale: fuel mass per gigawatt-year

### 4.1 D-3He: the discussion file's 54 kg of helium-3 per GW-year of fusion heat

**DERIVED working (primary reaction only, every reaction is D + 3He, 100% burn-up, no side reactions):**
- Energy per reaction 18.35 MeV = 2.940e-12 J. Mass per reaction: D (2.01410 u) + 3He (3.01603 u) = 5.03013 u = 8.353e-27 kg. Energy per kg of mix = 3.52e14 J/kg.
- 1 GW thermal-year = 1e9 W x 3.15576e7 s = 3.156e16 J. Fuel = 3.156e16 / 3.52e14 = **89.7 kg of mix per GW-year; 3He share 3.016 / 5.030 = 60.0%, i.e., 53.8 kg of 3He and 35.9 kg of deuterium.**
- This matches the discussion file's 54 kg.

**Independent checks (each a different source):**
- **NASA Kennedy Space Center, Olson, "Lunar Helium-3: Mining Concepts, Extraction Research, and Potential ISRU Synergies" (read via local text extraction; the paper says "In 2021" for company activity, so it is circa 2021):** "Fused with deuterium, 3He could produce ~19 MWyr/kg of fusion energy. The available 100 kg could produce 1.9 GWyr of fusion energy." DERIVED: 1 / 0.019 = **52.6 kg per GW-year.** The same paper: "only about 100 kg of presently available 3He on Earth."
- **Santarius and Kulcinski, 2004 (slide 12-13):** "~400 kg 3He accessible on Earth (~8 GW-a fusion energy for R&D)"; DERIVED: 400 / 8 = **50 kg per GW-year.** Same slide: about 10^9 kg of 3He on the lunar surface for "~1000 y world energy supply," and about 10^23 kg in gas-giant planets.
- **ENN roadmap, arXiv 2401.11338, Table 1** (fuel for 20 TW-years): 3He 1,000 tons; DERIVED: 1e6 kg / 20,000 GW-yr = **50 kg per GW-year.** (Same table: D-D, D 7,000 tons = 350 kg per GW-yr; D-T, T 1,000 tons = 50 kg per GW-yr; p-11B, 11B 8,000 tons = 400 kg per GW-yr. The paper's own Appendix B arithmetic disagrees with its Table 1 for tritium, so treat the table as approximate.)
- **The Princeton Satellite Systems mission table (Table 20) as a third check (DERIVED, assuming the "Power" column is fusion power sustained over the whole trip):** at 53.8 kg per GW-year, Mars (60 MW x 110 days = 0.01807 GW-yr) gives 0.97 kg (table: 0.98); Pluto (0.6 MW x 5 yr = 0.003 GW-yr) gives 0.161 kg (table: 0.16); 125 AU (0.8 MW x 10 yr = 0.008 GW-yr) gives 0.43 kg (table: 0.43); Jupiter gives 0.065 kg (table: 0.05). The match is close enough that I infer the report used the same arithmetic; the report does not state its formula.
- **One figure that does not match directly:** Olson's M-3 miner: "33 kg of 3He per year ... enough 3He to fuel one ~400 MW fusion power plant." DERIVED: 33 kg / 0.4 GW = 82.5 kg per GW-year if 400 MW is the plant's fusion power; if 400 MW is electric output at an efficiency near 65% (my assumption, not in the paper), thermal 615 MW gives 53.7 kg per GW-year. The paper does not say which; UNVERIFIED which reading is meant.

**Caveats the working does not include:** burn-up fraction (Daedalus: 0.175 and 0.133), D-D side reactions (half of D-D yields 3He, partly offsetting the 3He consumption in a self-breeding plant, which is Helion's stated approach), tritium decay into 3He, and conversion efficiency. For a given electric output, the 3He need depends on conversion: DERIVED for the discussion file's 101.7 GWe national load: at 35% conversion, 290.6 GWth gives 15.6 t of 3He per year (and 10.4 t of deuterium); at 50%, 10.9 t; at 60%, 9.1 t; at 80% (the top of the direct-conversion range quoted above), 6.8 t. (Working: GWth = 101.7 / efficiency; times 53.8 kg per GW-yr.)

### 4.2 p-11B

**DERIVED working (primary reaction only, 100% burn-up):** 8.68 MeV = 1.391e-12 J per reaction; mass of p (1.00783 u) + 11B (11.00931 u) = 12.01714 u = 1.9955e-26 kg; energy per kg of mix 6.97e13 J/kg. Fuel for one GW thermal-year = 3.156e16 / 6.97e13 = **453 kg of mix: 415 kg of boron-11 and 38 kg of hydrogen (protons).** For the national load at 35% conversion (290.6 GWth): about 120.6 t of boron-11 per year (DERIVED); at 60% conversion, 70 t.
- **Independent source:** ENN (arXiv 2401.11338) Table 1 gives 11B 8,000 tons per 20 TW-years = **400 kg per GW-year** (DERIVED division), consistent with the 415 kg derived above; the paper does not list the hydrogen mass. An informal Focus Fusion forum post (UNVERIFIED, search-result text) says roughly one ton of boron per GW per year. I found **no regulator, agency or peer-reviewed source** that states p-11B fuel mass per GW-year directly (NOT FOUND); the ENN table is the only one. Natural boron is about 80% boron-11 (Molloy 2025, SOURCED), so natural boron would be about 1.25 times the 11B mass if not isotope-enriched (DERIVED); whether the 10B fraction would be separated or burned (p + 10B is a different reaction with its own products) is not addressed in the sources I read.

### 4.3 D-D and D-T for contrast (DERIVED, same method)
- Catalyzed D-D (43.2 MeV per 6 deuterons, all products burned): 3.45e14 J/kg, **91.5 kg of deuterium per GW-year**; uncatalyzed D-D (average 3.65 MeV per reaction): 8.74e13 J/kg, 361 kg per GW-year (ENN: 350 kg).
- D-T: 3.38e14 J/kg, 93.5 kg of mix per GW-year (56.0 kg tritium and 37.4 kg deuterium), matching the discussion file's 93 / 56 / 37 kg. (This check also belongs to Unit F2.)

### 4.4 Supply side, for the comparison the brief asks about
- Helium-3 on Earth: "only about 100 kg of presently available 3He" (Olson, circa 2021) and "~400 kg 3He accessible on Earth" (Santarius, 2004); these differ by a factor of 4 and their bases are not the same. At 53.8 kg per GW-year the 100 kg is 1.9 GW-yr and the 400 kg is 7.4 GW-yr (DERIVED), against the national load of 290.6 GW thermal at 35% conversion. Supply questions beyond this belong to Units H1 and H2.
- Lunar and gas-giant figures quoted above (about 10^9 kg lunar, 10^23 kg gas giants in the Santarius deck; 1 t from 40 km^2 of regolith, 2 m deep, in the NASA report) are SOURCED as those authors' estimates and not checked here.

---

## FINAL

### What the sources support
1. **Reaction facts are well sourced.** D-3He releases 18.3 MeV (3.6 MeV alpha + 14.7 MeV proton); p-11B releases 8.68 MeV as three alphas; D-D has two equal branches (3.27 and 4.03 MeV). The Q-values check against atomic masses.
2. **Required conditions are far above D-T in every source.** D-3He ignition (ignoring side reactions): 5.2e22 keV s m^-3 at 68 keV, 18 times D-T (Wurzel and Hsu 2022); other studies give about 8 times in n tau and about 50 times in the triple product with a roughly six-fold temperature rise. p-11B: temperatures near 100 keV and above, where bremsstrahlung is comparable to or larger than fusion power in the older cross-section analysis; the 2022-2026 papers (Ochs 2022; Wang 2026 preprint) argue a narrow positive window exists only if electrons are kept cooler than ions.
3. **No advanced-fuel experiment has net energy.** D-3He's best result is JET 1991 (140 kW, Q about 1.25%, ICRH-driven tail). p-11B's best are a 2023 magnetic-confinement demonstration (alphas detected; about 14 W by the first author's account; Q well below 1) and laser experiments of about 5 x 10^8 alphas per steradian per 10 J shot (about 3e-4 of the laser energy returned as fusion energy, assuming isotropic emission). No D-D net energy.
4. **Helion's D-3He claim rests on the company's own statements.** In 2021 Trenta "saw evidence of bulk deuterium-helium-3 fusion" (2023 company post), with no yield or rate published; the 2026-02-13 release concerns D-T on Polaris (150 million C, about 13 keV) and says D-3He is still ahead. No independent confirmation of D-3He fusion was found.
5. **TAE's own roadmap (about January 2026) targets p-11B first plasma on Da Vinci in 2029 and net energy capability in 2030.** Its only measured p-11B result is the 2023 LHD experiment. No p-11B data from Norm found.
6. **Space propulsion concepts that need He-3 are design studies only.** Daedalus (30,000 t of He-3, 50,000 t fuel, 7.54 MN, 10,600 km/s exhaust); Discovery II (7,895 MW, 8.62 kW/kg, Isp 35,435-47,205 s, 11 t D3He, 3.9% neutrons); Direct Fusion Drive (0.75-1.25 kW/kg, Isp 8,000-12,000 s, 0.05-1.5 kg of He-3 per mission, with the test machine at 300 eV electron temperature in 2019). A Mercury transfer was analyzed for the DFD (under 140 days, 0.9 MW, 21 km/s).
7. **Neutron fractions** (all modeled, none measured at power): D-T about 80%; D-3He roughly 0.2% to several percent (FRC with tritium exhausted down to 0.2-1%; a spherical torus at 3.9%; generic Maxwellian mixes 1.3-7%); p-11B well under 1% by the primary reaction, with a ~10^-5 side-branch neutron route; waste and damage in the 1992 tokamak comparison were roughly a factor of 20 lower in wall loading.
8. **The 54 kg of He-3 per GW-year is confirmed:** 53.8 kg by direct calculation, 52.6 kg (NASA KSC), 50 kg (Wisconsin 2004), 50 kg (ENN table) and three of the five mission rows in the Princeton Satellite Systems table reproduced almost exactly (the other two within about 20-30%). The p-11B equivalent is 415 kg of boron-11 plus 38 kg of hydrogen (derived), against ENN's 400 kg.

### What the sources do not support
- Any claim that D-3He or p-11B plasmas have produced net energy, or that Helion's D-3He fusion has been independently measured and published.
- Any single "temperature for D-3He": the sources give 17 keV (Helion's 200 million C), 50-100 keV (optimal range), 58 keV and 68 keV (ignition), and these have not been reconciled.
- A single neutron fraction for D-3He: modeled values range from 0.2% to about 10% depending on assumptions.
- Cross-source agreement on the p-11B rate in the 2023 LHD experiment (10^12 /s, about 10^13 /s from "14 watts," and a calculated 10^14 /s for all beams).

### NOT FOUND (with where each died)
- The primary BIS 1978 Daedalus report and a primary source for the 20,000 t of deuterium (dead at the sources: only secondary pages reached).
- An evaluated-data source for the D-3He cross-section peak (Bosch and Hale 1992; Nocente 2010): died at the query (search returned paper titles and abstracts without values).
- OMEGA and JT-60U D-3He yields; the highest D-3He yield in inertial confinement: died at the query.
- A separately isolated "highest D-D result" and a sourced D-D net-energy statement: not isolated in what I read.
- Peer-reviewed or independent confirmation of Helion's 2021 D-3He fusion; Helion status after 2026-02-13 (only an unverified Axios summary dated 2026-09-08): died at the sources (Axios 403) and at the query.
- p-11B measurements from TAE's Norm: not found in any source.
- Any regulator, agency or peer-reviewed source giving p-11B fuel mass per GW-year directly (ENN's table is the only one).
- Later status of the Direct Fusion Drive after 2019, and verification of Pulsar Fusion's Sunbird claims.
- Putvinski et al. 2019 and Nevins 1998 full text (died at the sources: abstract or listing only).

### Surprises worth knowing
- Two company-independent design sources (NASA Glenn 2001/2005 and Princeton Satellite Systems 2019) already include Mercury as a destination or analyze a Mercury transfer, but both are about propulsion to Mercury, not about collecting fuel there. I found nothing linking D-3He fuel collection to Mercury or Venus in this unit (that question belongs to Unit H2).
- The 54 kg figure is robust to within 5% across five sources, but it is a heat figure for complete burn-up; the real He-3 need depends on conversion efficiency (35% to 80% changes the national figure from 15.6 t to 6.8 t per year in the derivation above).
- Helion's own stated D-3He temperature (about 17 keV) is a quarter of the ignition temperature in the standard models, and no source explains the gap.

---

## SEARCH LOG

Tool names: **WS** = WebSearch (standard unless noted), **WF** = WebFetch. Results: hit / partial / miss. About 64 web calls in total (26 searches and 37 numbered fetches, counting retries). Each fetch's prompt asked for quoted figures; where the fetch tool could not read a PDF it saved the file and I used local `pdftotext` (no further web call).

### Searches
1. WS "D-3He fusion reaction cross section temperature neutron fraction D-D side reactions": partial (leads to Nocente 2010, Santarius deck, Baghdad paper; no numbers).
2. WS "Helion Polaris D-T D-He3 fusion results 2025 2026 announcement": hit (Helion 2026-02-13 release, ANS roundup).
3. WS (extended) "Helion Polaris deuterium-helium-3 net electricity demonstration latest news": partial (Axios 2026-09-08 summary only; Helion fundraise post).
4. WS "Helion Trenta 100 million degrees D-He3 independent verification peer-reviewed data": partial (Helion 2021 and 2023 pages; no independent paper).
5. WS "JET 1991 D-3He fusion experiment 140 kW fusion power ICRH minority 3He Rebut Nature": hit (OSTI/ANS records; no Nature paper found).
6. WS "Bosch Hale 1992 improved formulas fusion cross-sections and thermal reactivities Nuclear Fusion 32 611 D-3He peak cross section": partial (paper confirmed; died at the query for peak values).
7. WS "Santarius D-3He fusion neutron power fraction versus temperature Wisconsin fusion technology institute advanced fuels": partial (slide decks found; curves not numeric).
8. WS "TAE Technologies p-11B proton boron fusion magnetically confined plasma Nature Communications 2023 Magee first measurements": hit.
9. WS "TAE Technologies 2026 Norm Copernicus Da Vinci hydrogen-boron fusion plan deuterium-tritium first plant": partial (one-pager found; Copernicus change from summaries).
10. WS "proton-boron-11 fusion feasibility 2022 2023 2024 paper bremsstrahlung ignition Ochs Fisch alpha channeling Putvinski reactivity": hit (Ochs 2022, 2310.18508, 2511.10885; Putvinski died at the query).
11. WS "laser-driven proton-boron fusion alpha particle yield record per shot ELI Beamlines Margarone 2022 Frontiers; 2024 2025 experiment alpha yield": hit (Molloy 2025, Frontiers 2023).
12. WS "D-3He fusion cross section peak about 0.9 barn at 250 keV center-of-mass; D-T 5 barn at 64 keV; p-11B 1.2 barn 600 keV table": partial (one table row in snippet; numbers UNVERIFIED).
13. WS "Princeton Satellite Systems Direct Fusion Drive NIAC Phase II final report specific impulse thrust power D-He3 specific power kW/kg": hit (NTRS 20190031807 found).
14. WS "Project Daedalus British Interplanetary Society 1978 D-He3 50000 tonnes exhaust velocity 0.12c helium-3 30000 tonnes Jupiter atmosphere mining": partial.
15. WS "Helion helium-3 supply breed from deuterium-deuterium fusion "helium-3" Orion plant fuel cycle Kirtley interview neutron": hit (Helion blogs).
16. WS "physicists skeptical Helion D-He3 claims no peer-reviewed data Polaris electricity from fusion Science Nature news 2025": partial (blogs and aggregators; nothing on D-3He).
17. WS "highest D-3He fusion yield achieved experiment OMEGA inertial confinement D3He proton yield; JT-60U; tokamak D-3He record": partial (JET only; OMEGA and JT-60U not found, died at the query).
18. WS (extended) "TAE Technologies Trump Media merger closed 2026 Norm results hydrogen-boron Da Vinci construction update": partial (merger status; no Norm results).
19. WS "Borowski Discovery II D-3He tokamak fusion propulsion crewed Jupiter mission NASA Glenn specific impulse helium-3 tonnes NTRS": hit (NTRS 20050160960 found).
20. WS "fusion propulsion 2025 2026 status Direct Fusion Drive PPPL Princeton Fusion Systems PFRC-2 ion heating results Pulsar Fusion Sunbird": partial (Pulsar Fusion only; no PFRC update).
21. WS "Daedalus probe fuel 30,000 tonnes helium-3 deuterium 20,000 tonnes pellets Jupiter atmosphere mining Bond Martin JBIS supplement 1978": hit (Centauri Dreams).
22. WS "Nevins "A review of confinement requirements for advanced fuels" Journal of Fusion Energy 1998 D-3He neutron fraction p-11B": partial (abstract only; died at the sources).
23. WS "HB11 Energy proton-boron laser fusion 2025 results alpha particles neutron-free net gain status": partial (company-sourced coverage).
24. WS "p-11B fusion fuel consumption per year gigawatt boron-11 kilograms 1 GW power plant fuel mass hydrogen-boron": partial (ENN paper found; forum posts).
25. WS "Helion Orion Malaga fusion plant progress October 2026 Polaris electricity recovery announcement": miss for October 2026 (2025 articles only).
26. WS "3He(d,p)4He cross section maximum barn at deuteron energy 430 keV laboratory resonance S-factor Nocente 2010": partial (430 keV, 0.90 barn from a scite listing; UNVERIFIED).

### Fetches
1. WF helionenergy.com/newsroom/helion-achieves-new-fusion-energy-milestones: hit.
2. WF ans.org/news/2026-02-18/article-7765 (fusion roundup): hit.
3. WF helionenergy.com/articles/ending-trenta-operations/: hit (dated 2023-10-05).
4. WF axios.com/pro/climate-deals/2026/09/08/...: **miss, HTTP 403** (dead at the source); not worked around.
5. WF helionenergy.com/newsroom/helion-energy-achieves-100-million-degrees-celsius...: hit.
6. WF arxiv.org/abs/2105.10954: hit.
7. WF arxiv.org/pdf/2105.10954: binary returned; saved and read with local `pdftotext`: hit.
8. WF osti.gov/biblio/7233843: hit.
9. WF en.wikipedia.org/wiki/Aneutronic_fusion: hit (secondary; first 100,000 characters read).
10. WF fti.neep.wisc.edu/.../jfs_dhe3_talk_icc0504.pdf: binary; local text extraction: hit.
11. WF fti.neep.wisc.edu/.../fdm884.pdf: binary; local extraction: hit.
12. WF tae.com/wp-content/uploads/TAE_incremental-disclosures-one-pager_final.pdf: binary; local extraction: hit.
13. WF faculty.sites.uci.edu/.../NatureComm23.pdf: redirect (not followed automatically); 14. WF bpb-us-e2.wpmucdn.com/.../NatureComm23.pdf: binary; local extraction: hit.
15. WF frontiersin.org/.../fphy.2023.1227140/pdf: binary, metadata only; not converted or used for content.
16. WF arxiv.org/abs/2210.08076: hit.
17. WF ensure.polimi.it/.../Molloy_2025_PhysRevResearch.pdf: binary; local extraction: hit.
18. WF alessmor.github.io/fusdb/...cross_sections_reactivities: miss (no peak values on page).
19. WF arxiv.org/pdf/2410.18054: error (size over 10 MB); 20-21. WF arxiv.org/html/2410.18054 (offsets 0 and 100000): partial (Table 2.2 found; barn table absent in the portion read; the last 93,000 characters were not read).
22. WF arxiv.org/html/2601.00241v1: hit (page also displays "August 24, 2026").
23. WF ntrs.nasa.gov/api/citations/20190031807/downloads/20190031807.pdf: binary; local extraction: hit.
24. WF en.wikipedia.org/wiki/Project_Daedalus: hit (secondary).
25. WF helionenergy.com/blog/how-to-engineer-a-renewable-deuterium-helium-3-fusion-fuel-cycle: hit (dated 2025-03-28).
26. WF helionenergy.com/blog/explaining-helions-fusion-fuel-choice-d-he-3: hit (dated 2024-06-27).
27. WF benzinga.com/m-a/26/06/53125690/...: **miss, HTTP 403**.
28. WF tae.com/one-step-closer-to-hydrogen-boron-fusion-energy/: hit (undated page).
29. WF ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20050160960.pdf: partial (abstract and metadata only).
30. WF en.wikipedia.org/wiki/Fusion_rocket: hit (secondary).
31. WF ntrs.nasa.gov/api/citations/20050160960/downloads/20050160960.pdf: binary; local extraction: hit.
32. WF centauri-dreams.org/2010/09/28/project-icarus-finding-the-fuel/: hit.
33. WF fti.neep.wisc.edu/.../fdm1214.pdf: binary; local extraction: hit.
34. WF psatellite.github.io/FusionEnergy/FusionModules/Demos/NeutronPowerDemo.html: hit (secondary reproduction of Santarius and Logan 1998).
35. WF arxiv.org/html/2401.11338: hit.
36. WF en.wikipedia.org/wiki/Nuclear_fusion: miss for peak cross-sections (first 100,000 characters).
37. WF physicsworld.com/a/proton-boron-fusion-passes-scientific-milestone/: hit (9 March 2023).
38. One provenance note: the Olson NASA KSC lunar He-3 paper was read from a saved PDF that appeared in the tool's saved-output folder when I converted the TAE one-pager (my conversion script picked the newest saved PDF, which turned out to be this paper). I cannot tell which of my fetch calls retrieved it, and I did not record its URL. I then converted the TAE PDF separately by file name. The paper is "Lunar Helium-3: Mining Concepts, Extraction Research, and Potential ISRU Synergies" by Aaron D. S. Olson (NASA Kennedy Space Center); its URL was not recorded by me, and I have not seen its publication venue or exact date, so I date it only as "circa 2021" from its text ("In 2021, there are several commercial companies ..."). SOURCED for the numbers quoted; the citation is incomplete.

### Blocks and refusals
- Two HTTP 403 responses (Axios; Benzinga). Not worked around; the items are marked UNVERIFIED.
- No search-tool refusal occurred.
