# Fusion power, helium-3, and uranium off Earth: the discussion and its findings (2026-11-02)

**Status: DISCUSSION RECORD AND ANALYSIS. Nothing here is ruled or canon.** Written at the developer's request so a new session can pick it up. The developer wants to **look further into both fusion and helium-3** in a fresh session with a replenished web-search quota (§5 lists exactly what is thin). Related files: `Tepenia_Nuclear_History_Proposal_2026-11-02.md`, `Tepenia_Nuclear_Power_Logistics_Research_2026-11-02.md` (R6), `Tepenia_Nuclear_Waste_Reuse_Research_2026-11-02.md` (R7), `Tepenia_Nuclear_Byproducts_in_Orbit_Research_2026-11-02.md` (R8), `Uranium_and_Thorium_Abundance_Off_Earth_Research_2026-11-02.md` (R9), `Locations/Infrastructure/Amundsen_Power_Supply.md`.

**Labels used here:** SOURCED = from a research file or repo file that read the source; DERIVED (mine) = my own arithmetic with the stated assumptions; GENERAL = my background knowledge, not checked in this session, and possibly stale (my knowledge ends around mid-2026). Treat GENERAL items as leads, not facts.

---

## 1 · Where fusion stands (what the repo has already sourced)

From `CurrentNovelDocs/worldbuilding/Object_Oriented_Location_Synthesis/research/benefits_of_mining_the_sun.md` §F2 (SOURCED there):
- **D-T laser fusion record:** 8.6 MJ out from 2.08 MJ of laser, target gain 4.13, on 7 April 2025 (LLNL). That counts the laser energy only, not the plant's.
- **Magnetic fusion** had not reached scientific breakeven (Q = 1) by the 2022 review it cites; the best D-T tokamak results were 0.27 (TFTR) and 0.64 (JET).
- **D-³He** (deuterium-helium-3): reaction 18.3 MeV; the best result found is JET 1991, 140 kW, Q = 1.25%; its ignition requirement is **18 times higher** than D-T; net energy is **not demonstrated**.
- **Helium-3 per gigawatt-year of fusion heat: 54 kg** (DERIVED there). Supply for all of the world's 2025 primary energy as fusion heat would be about 1,030 t/yr.
- **He-3 concentrations:** solar wind 39–54 g per tonne of wind; Jupiter's atmosphere 23 g/t; a Uranus case 15 g/t; lunar regolith about 4.2 ppb (240,000 t of regolith per kg). The solar wind is the richest by mass, but capture area is huge: 67,000–93,000 km² at 0.1 AU (6.7–9.3 million km² at 1 AU) for 54 kg a year.
- **Source of He-3 for fusion programs:** "must be bred via other reactions or mined from the moon" (Wurzel and Hsu); Helion breeds it from D-D and tritium decay (company blog, secondary).

Gaps the repo itself notes: no D-³He net energy anywhere; no fusion power plant exists.

## 2 · Fuel logistics for D-T fusion at Tepenian scale (DERIVED, mine)

**Assumptions:** national electricity 101.7 GW (the food model's figure, `Division_of_Industry/13`); 35% thermal-to-electric conversion; 17.6 MeV per D-T reaction; breeding ratio 1 (the plant makes as much tritium as it burns); natural lithium is 7.59% Li-6 (GENERAL).

| Quantity | Working | Result |
|---|---|---|
| Thermal power for 101.7 GW electric | 101.7 ÷ 0.35 | **about 290 GW thermal** |
| D-T energy per kg of fuel mix | 17.6 MeV per 5 atomic mass units | **about 3.4 × 10¹⁴ J/kg** |
| Fuel per gigawatt-thermal-year | 3.15 × 10¹⁶ J ÷ 3.4 × 10¹⁴ | **about 93 kg (37 kg deuterium, 56 kg tritium)** |
| **National deuterium** | 37 kg × 290 | **about 11 t/yr** (from seawater) |
| **National tritium** | 56 kg × 290 | **about 16 t/yr** (bred from lithium) |
| **National natural lithium for the breeding blanket** | about 1.5 t Li per gigawatt-thermal-year × 290 | **about 430 t/yr** |
| For comparison, fission fuel | 25 t enriched U per GWe-yr × 101.7, about 8 t natural U per t of fuel | about 2,500 t fuel and **about 20,000 t natural uranium** per year |

**Reading (DERIVED):** fusion's fuel need is **about three orders of magnitude smaller** than fission's, and its main inputs are available locally (deuterium from the Southern Ocean) or in small tonnage (lithium, a modest import). **The hard part is not mass but tritium self-sufficiency:** a D-T plant must breed at least as much tritium as it burns and handle a tritium inventory. Tritium is scarce in the real world. **Checked 2026-11-02 evening (F2, SOURCED):** world commercial stock is 20 to 30 kg, at $25,000 to $40,000 per gram, decaying 5.5% a year; the national burn above (about 16 t a year) is **540 to 810 times the entire world stock, every year**, so a Tepenian D-T economy would have to breed nearly all of it, and no plant-scale breeding ratio has ever been measured. The three fuel-mass figures in the table above all held against sources (F2: 3.37 × 10¹⁴ J/kg; 93.5 kg per GWth-year; Li-6 112 kg, with the 1.5 t as its natural-lithium equivalent). Published "lithium per 1 GW" figures range 1.5 to 7 t depending on thermal versus electric GW and on enrichment. The lithium problem is the roughly 100 t of Li-6 held in each blanket, not the annual use.

## 3 · Fit with the setting

> **CORRECTED 2026-11-02 (evening), after the fusion and helium-3 research (files F1–F4, H1, H2, listed in §7).** Three statements below were written from memory (GENERAL) and the research did not support them as written. The corrected text follows each; the old wording is kept in brackets so the change is visible.

- **Treaty:** Article V.1 of the draft bans nuclear explosive devices and the disposal of radioactive waste in Tepenian territory. **Fusion is neither** an explosive device nor disposal. **Waste (corrected, F3, SOURCED):** fusion waste is mostly low- and intermediate-level, with no transuranic elements and few long-lived isotopes, **but its volume is much larger than fission's** (one IAEA-led review: DEMO may produce as much as 10,000 t of solid waste from in-vessel components alone, against about 2,500 t of waste, high-level and intermediate, for a comparable fast fission reactor), **its in-vessel components are not clearable even after 100 years** (niobium-94 from steel impurities), and tritium-bearing waste may need decay storage of 50 to about 100 years. So a fusion-first Tepenia has **no plutonium alarm and no high-level waste, but it does have a large activated-steel waste stream that the treaty's waste article would have to be read against.** [Old wording: "its waste is mostly activated structure and tritium, shorter-lived than fission waste (GENERAL; unsourced here)".] **There is no enrichment or reprocessing** for D-T fuel itself. **The Antarctic Treaty (F3, SOURCED, verbatim in that file):** Article V bans nuclear explosions and the disposal of radioactive waste; it does not ban non-explosive nuclear use. A May 2026 Kobe/Tasmania white paper and the 1959 US negotiating record both read it that way; the Madrid Protocol never uses the words "nuclear" or "reactor"; the white paper says the Protocol has never been applied to a reactor. (The US PM-3A reactor at McMurdo is the precedent; dates are in F3.)
- **The Tower:** the design file says its primary generation is *plausibly* "an advanced nuclear/fusion reactor array" for about 324 GW net. **Plant size (corrected, F3, SOURCED):** published pilot and demonstration plants are **100 to 500 MWe net** (ARC 190 MWe; EU-DEMO 350 MWe in the 2024 proposal, down from 500 MWe in the 2017 baseline; JA-DEMO about 250 MWe; STEP at least 100 MWe), with only the older US ARIES-ACT2 study sized at 1,000 MWe. **DERIVED (mine):** 324 GW at 190 MWe is about 1,700 plants; at 350 MWe, about 930; at 1,000 MWe, 324. The national 101.7 GW is about 535, 290 and 102 plants on the same three sizes. [Old wording: "at roughly 400 MWe per plant (GENERAL; current commercial designs), that is on the order of a thousand plants" — the 400 figure was not supported.] Nothing in the research says fusion plants of this number are plausible within a given century; no fusion device has yet delivered net electricity (F1).
- **Siting and cooling:** **NOT FOUND (F3):** plant footprints, fusion-specific cooling-water volumes, and any cold-climate or polar fusion siting study. The agent's own arithmetic for ARC's cooling needs is in F3 (DERIVED there). Treat the coastal-rock constraints from the fission files as the only guide.
- **Possible friction even for fusion** (proposals): fusion neutrons can breed fissile material from uranium-238 or thorium (a fusion-fission hybrid), so Upper Earth could allege proliferation; the Tower's mass driver would still look like a weapon; national power on that scale would still alarm a world that remembers the 2083 nuclear war.

### Story options (proposals)
1. **Fusion replaces fission** as the answer to "needed power to survive": cleaner legally, less direct friction.
2. **Fission first, fusion later:** a bridging era with the friction from the nuclear-history proposal, ending with a fusion breakthrough that Tepenia monopolizes.
3. **Helium-3 as the reason to go to the inner system.** D-³He (if it ever works) needs solar-wind or gas-giant helium-3; the repo's own sourced figures put the solar wind as the richest source, concentrated near the Sun. This is the physics-based answer to "why would anyone go to Mercury or Venus", and fits the starlifting idea. It is **conditional on D-³He fusion producing net energy, which no experiment has approached.** **Checked 2026-11-02 evening (F4, H1, H2, SOURCED):** the best D-³He result is still JET 1991 (Q about 1.25%); Helion's D-³He claims are company statements only; the 54 kg of helium-3 per GW-year holds (four independent sources, 50 to 52.6 kg; direct calculation 53.8 kg). **But the supply case is thin:** the only published Mercury or Venus helium-3 statements are Dawson's 1986 suggestions (Mercury 5.4 kg a year); Mercury's whole implanted supply is about 18 kg a year and its helium is released thermally; no engineered solar-wind collector concept was found; powering 101.7 GWe takes about 8 to 16 t of helium-3 a year, against a lunar miner design (Mark-III class) of 33 kg a year, so about 280 to 880 such miners for the national grid plus the Tower. At 0.1 AU, 54 kg a year needs about 60,000 to 76,000 km² of perfect capture (100,000 to 125,000 km² with an inner-wind model). Gas-giant figures for Uranus and Neptune rest on an assumed isotope ratio nobody has measured there. Read: helium-3 is a defensible *stated* reason, but nothing sourced shows the inner system is where an engineered supply would come from.

---

## 4 · Uranium off Earth: the findings (R9, SOURCED in that file)

- **Mercury:** surface U **90 ± 20 ppb** (north, MESSENGER), Th 155 ± 54 ppb (the 2011 paper said 220 ± 60); modeled bulk silicate 23–35 ppb U; **no enriched region found**; the chapter warns U may be overestimated through radon transport.
- **Venus:** Vega 1 U 0.64 ± 0.47 ppm, Th 1.5 ± 1.2; Vega 2 U 0.68 ± 0.39, Th 2.0 ± 1.0 (both basalt); Venera 8 the outlier at U 2.2 ppm, Th 6.5 ppm. Surface 737 K, 92 bar. (An encyclopedia page's "200 ppm" for Venera 8 is a roughly 100-fold units error.)
- **Moon:** highest Kaguya U about 2 ppm; urKREEP about 5 ppm; tiny Apollo samples 10–20 ppm; all below the ">100 ppm" a 2015 review calls low-grade ore on Earth. **Chondrites:** 8–16 ppb.
- **Earth for scale:** the "2.7 ppm" crustal figure is the **upper-crust** value; the **bulk crust is 1.17 ppm**. The 2026 Red Book (via the World Nuclear Association page) lists 8.1 million tonnes recoverable at under $260 per kg U.
- **Mining arithmetic (DERIVED in R9):** 20,000 t U a year at Mercury's 90 ppb is about **222 billion tonnes of rock, about 2.1 times world material extraction (106 Gt)**; at 5 ppm (urKREEP) about 4 Gt; at a 0.02% ore about 0.1 Gt. **The uranium's electricity yield breaks even at about 5 kWh per tonne of rock at Mercury's grade; published grinding energy is 10–60 kWh per tonne, so mining average Mercury rock for uranium costs more energy than it yields.** Launch energy for the uranium alone is about 10⁻⁵ of its yield (the rock mass dominates).
- **Derived by me:** 8.1 Mt of recoverable resource at 20,000 t a year would last about **400 years** of Tepenia's whole national load.

**Verdict:** uranium is **not** a physical reason to mine Mercury, Venus, the Moon or asteroids. Earth's resources are far better.

**Ways the story can still use the idea** (proposals): (1) an undiscovered rich Mercury deposit (fiction against current data; a boom-and-bust rush on a misleading survey would fit the radon flag); (2) uranium as the stated reason while the real pull is solar energy and materials; (3) fuel from elsewhere (Earth mines or seawater) as a trade good and leverage, not the reason for Mercury; (4) thorium plus breeders; (5) helium-3 for fusion (§3).

**Not found (R9):** Venera 9 and 10 per-site values; direct Mars U (the 0.15 ppm in the file is derived from an assumed Th/U); Mercury and tether launch studies; any uranium-rich asteroid claim; Venus cloud-top conditions; operator-page grades for Olympic Dam, Cigar Lake and McArthur River.

---

## 5 · What to research next (for the fresh session): fusion and helium-3

**Fusion (current state, as of late 2026; my own knowledge may be stale, so check everything):**
1. **Status of the main programs:** ITER (schedule and cost), SPARC and ARC (Commonwealth Fusion Systems), Helion (Polaris and the Microsoft plant), Tokamak Energy, TAE, General Fusion, Type One, Proxima, China's BEST/EAST/CFETR, Wendelstein 7-X, NIF and laser-fusion companies. What has been demonstrated (Q values, durations, tritium breeding blankets) versus announced.
2. **Fuel cycle:** tritium inventory worldwide and how a plant breeds it; breeding ratio requirements; lithium-6 enrichment; deuterium extraction cost; blanket designs; tritium handling and permeation.
3. **Plant size and economics:** published power plant designs (MWe, footprint, capacity factor, activated waste volume and half-lives), neutron damage and component lifetime, cooling and heat rejection, siting in cold or polar conditions.
4. **Advanced fuels:** D-³He, p-¹¹B, D-D: demonstrated reactions, required temperatures, neutron fractions, whether any has net energy; Helion's D-³He claims and their evidence.
5. **Fusion-fission hybrids and proliferation:** what a fusion plant could breed; safeguards proposals.
6. **Fusion in space:** propulsion and power concepts (including those that need helium-3).
7. **Regulation:** how fusion is regulated differently from fission (NRC, UK, IAEA); the Antarctic Treaty and Madrid Protocol treatment of fusion, if any.

**Helium-3:**
1. **Terrestrial supply today:** tritium decay from weapons stocks, annual production, price per liter, DOE Isotope Program sales, the Interlune lunar-He-3 contracts and their status.
2. **Lunar He-3:** concentrations by site, the processing rate (tonnes of regolith per gram), equipment studies, the published economics, legal status of lunar resources (Outer Space Treaty, Artemis Accords, the Moon Agreement).
3. **Solar wind and gas-giant He-3:** published collection concepts, capture areas, how He-3 would be separated; the Palaszewski gas-giant mining papers (NTRS) and their He-3 yields; Saturn, Uranus and Neptune atmospheric mining studies.
4. **Breeding He-3:** from D-D and tritium decay (Helion's approach), and from other reactors; yields per gigawatt-year.
5. **Why a civilization would go to the inner system for it:** the best-sourced numbers for He-3 per square kilometer of solar-wind capture at 0.1–0.5 AU; any proposal tying He-3 to Mercury or Venus.

**Also still thin** (from the other units): a sourced check of uranium transport and enrichment ownership; Mars uranium; and the Venera 9 and 10 values.

---

## 6 · The one-line summary
Nothing off Earth is a good uranium mine; fusion fuel needs are tiny and local (deuterium from seawater, a little lithium), with tritium self-sufficiency the hard problem; and helium-3 is the physically defensible reason to go to the Sun's neighborhood, if and only if helium-3 fusion works.

---

## 7 · Research results since this file was written (2026-11-02, evening)

The §5 list was run as six units (brief: `Fusion_and_Helium3_Research_BRIEF_2026-11-02.md`). Each file has SOURCED / DERIVED / UNVERIFIED / NOT FOUND labels, a FINAL section and a full search log. §2, §3 and Story option 3 above carry corrections drawn from them.

| Unit | File | One-line result |
|---|---|---|
| F1 | `Fusion_F1_Program_Status_Research_2026-11-02.md` | ITER D-T 2039; NIF record still 8.6 MJ (gain 4.13); no device has net electricity; private raise USD 14.24 billion cumulative (FIA 2026) |
| F2 | `Fusion_F2_Fuel_Cycle_Research_2026-11-02.md` | Fuel-mass figures confirmed; world tritium stock 20–30 kg; no plant-scale breeding ratio measured |
| F3 | `Fusion_F3_Plant_Regulation_Treaty_Research_2026-11-02.md` | Plants 100–500 MWe net; fusion waste larger in volume than fission's; Antarctic Treaty Article V text quoted; no "Article I(c)" exists |
| F4 | `Fusion_F4_Advanced_Fuels_and_Space_Research_2026-11-02.md` | No advanced fuel has net energy; 54 kg He-3 per GW-year confirmed; Helion D-³He claims uncorroborated |
| H1 | `Helium3_H1_Terrestrial_Supply_and_Lunar_Research_2026-11-02.md` | US supply about 1.1 kg a year (2011); Interlune's DOE deal is 3 L; legal texts quoted |
| H2 | `Helium3_H2_Solar_Wind_Gas_Giants_Breeding_Research_2026-11-02.md` | Solar-wind figures reproduced; no Mercury or near-Sun He-3 proposal beyond Dawson 1986; Mercury's implanted supply about 18 kg a year |

**Still thin after the research:** plant footprint and cooling water; polar siting; a measured breeding ratio; independent confirmation of Helion's D-³He; any engineered solar-wind collector; helium-3 content of asteroids, comets and Mercury regolith; weapons tritium stocks; a primary price for helium-3 after 2011; the EU legal status of fusion; a final US NRC fusion rule.
