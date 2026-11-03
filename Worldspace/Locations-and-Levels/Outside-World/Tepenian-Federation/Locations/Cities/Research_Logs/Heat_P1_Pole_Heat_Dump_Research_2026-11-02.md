# Heat P1: the heat dump at the South Pole (research unit P1, 2026-11-02)

**Started:** 2026-11-02 21:08 MST. **Ended:** 2026-11-02 21:26 MST.

**Scope.** Unit P1 of `Power_Plant_Heat_Research_BRIEF_2026-11-02.md`: facts about what the ice and air at the geographic South Pole can and cannot absorb, precedents for putting heat or hot water into polar ice, published thermal models of heat sources in cold ice, derived numbers for 1, 10, 100 and 600 GWth, rejection of heat to air and by radiation, and effects of heat sources on local climate and ice. **Facts only; no recommendation, no design, no ranking.** Plant type (fission or fusion) is undecided, so results are per gigawatt of heat (GWth). Labels: **SOURCED** (read at the source in this session; where the source is a secondary page such as Wikipedia or a personal blog, that is stated), **DERIVED** (my arithmetic on stated inputs, working shown), **UNVERIFIED** (seen only in a search snippet, recalled, or inferred), **NOT FOUND**. Several PDFs came back as binary and were converted locally (text extraction or OCR) in the scratchpad; those count as read at the source. Cambridge Core and some DTIC and mirror pages returned HTTP 403 and were not worked around (see the search log).

**Headline of what was not found (stated plainly).** No study of reactor-scale heat (hundreds of megawatts to hundreds of gigawatts) dumped at the Pole or anywhere on an ice sheet was found. The largest sourced heat inputs into polar ice are tens of kilowatts (a Rodwell: about 88 to 97 kW design input), a few megawatts for a few days (the IceCube drill: 4.7 MW thermal), and the Camp Century reactor (2 MWe plus heating, 1960 to 1964).

## PROGRESS

- [x] Q1 The ice and air at the Pole (partial: firn density, ice properties, flow, thickness, temperature profile and basal state found; no direct SPICEcore firn table; ice-specific heat at -50 °C not found)
- [x] Q2 Precedents: Rodwell, IceCube hot-water drill, Camp Century/PM-2A (partial: PM-2A heat disposal NOT FOUND in primary form), other hot-water drills, thermal-pollution assessment (NOT FOUND)
- [x] Q3 Published thermal models of buried heat sources (partial: papers identified; the two key 1976/1978 papers were behind 403/bot blocks; numbers per unit power NOT FOUND at primary level)
- [x] Q4 Derivations (done: conduction, melt per year, air volume, area)
- [x] Q5 Rejection to air (partial: Fairbanks ice fog primary source read; ACC plant data read; ACC design limits at -40 °C and Yakutsk/Norilsk/Bilibino/Pevek NOT FOUND)
- [x] Q6 Radiative rejection (partial: measured atmospheric brightness temperature at the Pole found; radiator precedents NOT FOUND)
- [x] Q7 Effect of a heat source on local climate and ice (partial: Fairbanks heat island sourced; Pole/Antarctic measurements and snow-drift/mass-balance effects NOT FOUND)
- [x] FINAL section and search log

---

## Q1. The ice and air at the Pole

### 1a. Air temperature, wind and inversion

- **Elevation 2,835 m; annual mean air temperature about -49 to -50 °C.** SOURCED: Yang et al. 2024, *Geophysical Research Letters* (DOI 10.1029/2024GL109183), read locally from the PDF: "a high altitude (2,835 m) plateau characterized by a slowly moving ice sheet (10 m/year), low precipitation (5 cm/year), and cold temperatures (−49.3°C annual average)". Winski et al. 2019, *Climate of the Past* 15:1793, read on the journal page: "a mean annual air temperature of −50 °C" and elevation 2,835 m.
- **Monthly means and extremes (secondary source).** SOURCED to the Wikipedia article "Amundsen-Scott South Pole Station" (climate table citing pogoda.ru.net, 1991 to 2020 normals and 1957-present extremes); the article's annual mean is -49.1 °C. Monthly daily means: Jan -28.1, Feb -40.7, Mar -53.6, Apr -57.4, May -57.7, Jun -58.1, Jul -60.2, Aug -59.7, Sep -58.9, Oct -50.9, Nov -37.2, Dec -27.3 °C. Record high -12.3 °C (December; 25 December 2011 per a CIMSS search snippet, UNVERIFIED as to date); record low -82.8 °C (June; 23 June 1982 per a search snippet, UNVERIFIED as to date). The same article gives annual precipitation as 2.3 mm in the table but "approximately 25 millimeters" in the prose (internal conflict; the primary figure used here is Yang et al. 2024's 5 cm/yr and Winski's 7.4 cm/yr water equivalent, below).
- **Surface pressure** 674 hPa on a winter sounding. SOURCED: Hudson and Brandt 2005, *Journal of Climate* 18, Fig. 3 caption (read locally from the PDF).
- **Surface-based inversion (10 years of radiosondes, 1994 to 2003).** SOURCED: Hudson and Brandt 2005, Table 2. Monthly mean inversion strength between 2 m and the warmest point of the troposphere (K) and depth (m): Jan 2.3 K / 265 m; Feb 9.8 / 525; Mar 20.0 / 665; Apr 22.2 / 665; May 22.0 / 605; Jun 22.6 / 625; Jul 21.5 / 585; Aug 21.0 / 605; Sep 22.9 / 605; Oct 16.1 / 585; Nov 6.6 / 505; Dec 1.0 / 245. Mean gradient between 2 and 100 m in winter months about 0.11 to 0.13 K per m. The same paper: individual-sounding winter inversions average about 20 K; "the 13- to 22-m layer ... isothermal or inversion conditions more than 90% of the time in winter, and these inversions can greatly exceed 10 K"; maximum observed strength in a case study 19 K between 2 m and 22 m. The inversion generates its own wind: "winds of 3-5 m/s, likely due to the inversion wind".
- **Wind.** SOURCED: Hudson and Brandt 2005, Table 1 (vector mean winds at Pole): all data 4.2 m/s from 40° (grid), directional constancy 0.75; summer 3.0 m/s; winter 4.6 m/s from 43°. (These are vector means, not scalar mean speeds.) Lazzara et al. 2012 (*Atmospheric Research* 118:240) is reported in a search snippet to find a mean wind speed decline of 0.28 m/s per decade (UNVERIFIED; full text not read).
- **Not found:** a single primary annual-mean wind speed in m/s (scalar) for the Pole; the Lazzara 2012 full text was not retrieved.

### 1b. Ice thickness, flow and basal condition

- **Ice thickness.** SOURCED: Price et al. 2002 (PNAS, PMC122982): "the 2,810-m deep base of the South Pole ice"; BEDMAP gives the same thickness. Winski et al. 2019: "Radar measurements indicate a bed depth at the South Pole of 2812 m, giving an ice-equivalent thickness of 2774 m." (Both agree within 2 m; the setting's 2,700 m foundation figure is not contradicted by either, but neither source says 2,700 m.)
- **Ice flow at the Pole.** SOURCED: Winski 2019: "the current South Pole ice flow velocity of 10 m yr−1"; Yang 2024: "10 m/year"; Price 2002: surface velocity 9 m/yr downhill, zero at the bed. A search snippet from a SPICEcore paper (UNVERIFIED, not opened) gives the direction as about 40° west of north. Radar studies report Holocene speed-up of about 14 to 15 percent since 10 ka (search snippet, UNVERIFIED).
- **Accumulation.** SOURCED: Winski 2019: Holocene average 7.4 cm/yr water equivalent (model input 8 cm/yr). Price 2002: 0.073 m ice per year (the paper also writes cm in one place; units inconsistent in the source). Yang 2024: 5 cm/yr precipitation.
- **Basal condition at the Pole itself: frozen.** SOURCED: Price et al. 2002: temperature at the base of the ice about -9 °C, "7°C below the pressure-melting point"; "South Pole glacial ice is frozen to bedrock"; geothermal heat flux 61 mW/m². Conductivity law used there: K = 9.828 exp(-0.0057 T) W/(m K), T in kelvin.
- **Upstream of the Pole the bed is not frozen everywhere.** SOURCED: Jordan et al. 2018, *Scientific Reports* 8:16785 (read locally): radar shows "a ~100 km long and 50 km wide area where internal ice sheet layers converge with the bed", basal melting up to 6 ± 1 mm/yr and geothermal flux of 120 ± 20 mW/m² (background 48 mW/m² or less), near the ice divide where surface flow is about 1.5 m/yr; the survey area "extends radially ~700 km from South Pole"; the paper contrasts this with "borehole temperature measurements indicating low geothermal flux and frozen bed at South Pole". (The paper in the text I read gives the area as upstream of the Pole; it does not state a single distance from the Pole to the melting area.)

### 1c. Temperature versus depth

- SOURCED: Price et al. 2002: surface ice temperature -51 °C; thermistors at 800 to 2,345 m (59 points, uncertainty 0.11 to 0.24 °C); shallow data from 12 to 50 m; base about -9 °C. The depth-by-depth values are in Fig. 1 of that paper and were not tabulated in the text I read, so I have no numeric profile table. (The brief's "firn temperature -51 °C" matches the CRREL report below, which uses an ambient firn temperature of -51 °C at the South Pole.)
- Winter surface ice and firn at the Pole are therefore about -51 °C in the upper tens of meters, rising to about -9 °C at 2,810 m. DERIVED mean gradient: (-9 − (-51)) / 2,810 m = 42 K / 2,810 m = 0.0149 K/m = 14.9 K/km.

### 1d. Firn depth and density profile

- **South Pole firn density fit, as used by CRREL.** SOURCED: Lunardini and Rand 1995, CRREL Special Report 95-10, "Thermal Design of an Antarctic Water Well" (read locally via OCR), eq. 28a to 28c, "based upon the measurements at the South Pole (Langway 1975)", density in g/cm³, depth z in m (the OCR printed the depth limits as "975" and "1585"; these are 97.5 m and 158.5 m, which the numbers confirm because the branches meet there):
  - ρ = 0.349 + 7.56e-3 z − 3.08e-5 z², for 0 < z < 97.5 m;
  - ρ = 2.102e-3 z + 0.5885, for 97.5 < z < 158.5 m;
  - ρ = 0.922 below 158.5 m.
  - DERIVED check of the fit: at z = 97.5 m branch 1 gives 0.349 + 0.7371 − 0.2928 = 0.7933; branch 2 gives 0.2049 + 0.5885 = 0.7934 (continuous). At 158.5 m branch 2 gives 0.9217 (matches 0.922). So surface density 349 kg/m³; 793 kg/m³ at 97.5 m; ice density reached at about 158.5 m. The same report says the close-off density "starts at about 0.72 g/cm³" and the report uses 0.922 g/cm³ for ice.
- **Close-off depth.** A SPICEcore-era search snippet gives bubble close-off at "roughly 120-123 m" at the drill site (UNVERIFIED; snippet only, citing Battle 1996 and Severinghaus and Battle 2006). Not read at the source.
- **Not found:** a SPICEcore firn density table in numbers from the primary papers (Winski 2019 says it uses the Kuivinen et al. 1982 South Pole density function without reproducing it; Yang 2024 reports its own seismic density result but I did not extract a profile table). NOT FOUND queries are in the log.

### 1e. Thermal properties

- **Thermal conductivity of ice.** SOURCED: Price 2002, K = 9.828 exp(-0.0057 T) W/(m K), T in K. DERIVED values: at -51 °C (222.15 K) 2.77; at -49 °C 2.74; at -29 °C 2.44; at -25 °C 2.39; at -10 °C 2.19; at 0 °C 2.07 W/(m K). Working: e.g. at -25 °C, T = 248.15 K, exp(-0.0057 × 248.15) = exp(-1.4144) = 0.2431; × 9.828 = 2.389. The CRREL report independently uses ice conductivity of 1.28 Btu/(h ft °F) (= 2.21 W/(m K), DERIVED by 1.28 × 1.7307) and diffusivity of 41.4 cm²/h (= 1.15e-6 m²/s, DERIVED: 41.4e-4 m² / 3,600 s) for firn treated as ice (the OCR printed the unit as "W/m2 °C"; the Btu value shows it is W/(m K)).
- **Specific heat of ice.** SOURCED to the Wikipedia article "Properties of water", citing Lide (2003): 2,030 J/(kg K) at -10 °C. Only that one point; the value at -50 °C is lower (about 1.8 kJ/(kg K), recalled, **UNVERIFIED**). All melt numbers below use 2,030, which therefore slightly overstates the sensible-heat term (by roughly 10 percent of that term, or about 1 to 2 percent of the total).
- **Latent heat of fusion.** SOURCED (same Wikipedia page, no inline citation): 333.55 kJ/kg at 0 °C. Density of ice 0.9167 g/mL at 0 °C (same page, citing Lide 2003).
- **Thermal conductivity of firn.** NOT FOUND at a primary source in this session. A search snippet says Calonne et al. 2011 (density-only formula) performed best in a 2021 comparison in East Antarctica, but coefficients were not retrieved. Recalled from memory and **UNVERIFIED**: Calonne 2011, k = 2.5e-6 ρ² − 1.23e-4 ρ + 0.024 W/(m K), which would give about 0.29 W/(m K) at 350 kg/m³ and about 1.5 W/(m K) at 800 kg/m³. The CRREL design treats firn as ice for conduction (above), which is a design simplification, not a measurement.
- **Specific heat and latent heat of firn:** treat as ice (mass basis); no separate source.

---

## Q2. Precedents for putting heat or hot water into polar ice

### 2a. The South Pole Rodwell (Rodriguez well)

What it is. SOURCED: Lunardini and Rand 1995 (CRREL SR 95-10): "The concept is simple and involves melting firn/ice at depth, thereby creating a reservoir of liquid water that can be pumped to the surface as needed ... A hole is driven down into the snow and vertical advance is maintained until impermeable strata are intercepted or until refreezing meltwater forms its own impermeable barrier. The melt then ponds ..." The cavity "can grow laterally rapidly" with large heat supply and small pumping, "but if the pool is overpumped, the cavity tends to develop rapidly downward due to the high temperature of the reservoir water." "As the pool grows, the heat losses increase, until finally an equilibrium size may be reached, when all of the heat input is lost by conduction and convection and no new water can be produced unless the rate of heat supply or the pumping rate ... is increased."

Power and melt, from that report (SOURCED):
- **Camp Century well, 1960 to 1962:** steam generator about 219,825 W (750,000 Btu/h), burning up to 28.5 L (7 gal)/h of fuel oil; ponding at 42.5 to 49 m (140 to 160 ft) depth; pump up to 1.58 L/s; "water production efficiency ... 59 lbm water per lbm of fuel". Camp Tuto (1962): about 73,275 W (250,000 Btu/h); May to June 1962 it produced 5,315 L (1,404 gal)/day with fuel use of 137 kg (302 lbm)/day and 2,006 L (530 gal)/day of potable water delivered; the report states an efficiency of 17.7 (printed with "39 lbm" in the OCR, which does not agree; the OCR is garbled here, treat as approximate).
- **Old South Pole Station well, 1972 to 73 (Williams 1974):** ambient firn temperature "-51°C (60°F)" (the OCR printed "(60°F)"; -51 °C is -59.8 °F, so the sign is lost in the OCR); the well "functioned well without significant adverse freezing problems"; operation was halted by a frozen fuel line at the boiler; it was shut down after supplying about 416,400 L (110,000 gal) of potable water. Table 2 of the report for the first 1,704 h: total energy used 0.73 × 10⁹ Btu; average energy input 428,404 Btu/h (DERIVED: 125.6 kW); useful water withdrawal 37,836 gal; water leakage (percolation into firn) 49,735 gal; final water volume 106,533 gal; depth to water bottom 241.5 ft (73.6 m); water-surface diameter 39.0 ft (11.9 m); water depth 23.9 ft; 32.2 lbm water per lbm fuel. (Derived conversions: 241.5 ft × 0.3048 = 73.6 m; 39 ft = 11.9 m; 428,404 Btu/h × 0.29307 W per Btu/h = 125.6 kW.)
- **Design for the new (1990s) South Pole Station well:** base case A5 uses boiler water at 39.4 °C and 0.63 L/s, "constant energy input to water of 58,620-234,480 W (200,000-800,000 Btu/h)"; the model predicts reservoir depth of 144 m after 10 years with average energy input 97,309 W (332,000 Btu/h) "well within the expected available waste heat flux"; a case with the water withdrawal increased by half and average input of 142,144 W (485,000 Btu/h) gives 149 m after 10 years. "Case 10" with fixed 87,930 W (300,000 Btu/h) of waste heat from the generators (after 62 days on fuel oil, 11,385 L of fuel) gives a final depth of 157.25 m after 10 years; at 303 days the reservoir is at 84.4 m, contains 1,018,276 L (269,000 gal) and has delivered 757,082 L (200,000 gal) of potable water. A too-rapid withdrawal (case 9, 7,570 L/day started in the second year) made the reservoir "sink rapidly and collapse after 421 days of operation". The report concludes "a Rodriguez water well at South Pole Station can operate for 10 years at a reasonable fuel consumption." Convective coefficient used for melting 142 to 284 W/(m² K), mostly 184.5.
- **DERIVED:** the design waste-heat input of one Rodwell, 87.9 kW (case 10) to 97.3 kW (base case), is 8.8e-5 to 9.7e-5 of one GWth. One GWth is 1e9 / 87,930 = 11,370 Rodwell design inputs; 600 GWth is 6.8 million.

Later operation (secondary sources):
- SOURCED to the personal blog "South Pole Water Infrastructure" (brr.fyi, an individual's account, not a primary document): heat comes from "waste heat from the power plant"; "Hot glycol is pumped in from the power plant next door"; pumped-out water about 36 °F (2 °C), heated by heat exchangers to about 84 °F (29 °C) and recirculated; backup boilers; "We use each Rodwell for several years"; the current one is Rodwell 3 and Rodwell 4 is planned; retired Rodwells become the sewage outfall with "millions of gallons of raw, untreated wastewater" stored beneath the station. The page gives no cavity diameter, depth, power or water rate.
- SOURCED to the Wikipedia article "Rodriguez well" (which cites the Antarctic Treaty Secretariat's EIA database): experimental well 1972; Rodwell-1 completed 1993, drinking water 1995 to 2003, wastewater 2003 to 2012; Rodwell-2 completed 2002, drinking 2003 to 2012, wastewater 2014 to 2025; Rodwell-3 completed 2007, drinking from 2012 to present, conversion to wastewater projected 2030; Rodwell-4 projected for 2030. Lifespan "over seven years" ending "when the cavity grows too deep to heat and recirculate efficiently". Note conflict: southpolestation.com (below) says RW1 was completed in 2001-02 and RW2 in 2006-07.
- SOURCED to southpolestation.com "Rodwell" page (a personal historical site): Well 1 (Jamesway, 1972-73): final 39 ft diameter, 217 ft to water, water 24 ft deep, about 550 gal/day over the last three weeks, water out at 34 °F and returned at 70 °F, about 30 gal water per gal fuel, fuel line froze and DFA fuel gelled at -70 °F. Well 2 (milvans in the dome pit, in use from March 1994): about 80 ft diameter, 295 ft to water, water 52 ft deep, about 1,450 gal/day (December 1995); later about 390 ft to water, 72 ft deep, about 2,450 gal/day in 2005; it failed after a 1994 outage and heat-trace fire and an ice lens froze over the water surface in the 2005 winter. "The bulb slowly expands into a significant reservoir of water."
- **Not found:** a measured heat input (kW) for the current Rodwells, current cavity dimensions, or an official lifetime statement; the Antarctic Treaty EIA documents themselves were not retrieved (search for "Rodwell 4 EIA" returned only older NSF documents).

### 2b. IceCube hot-water drill (Enhanced Hot Water Drill, EHWD)

SOURCED: IceCube Collaboration, "The IceCube Neutrino Observatory: Instrumentation and Online Systems" (arXiv:1612.05093, JINST 2017), section 5.1, read locally from the PDF:
- 86 boreholes, about 60 cm diameter, 2,500 m deep; seven field seasons (about 21 months of drilling); peak 20 holes in the 2009-2010 season.
- Table 5: total power 5 MW (4.7 thermal + 0.3 electrical); maximum drill speed 2.2 m/min; maximum ream speed 10 m/min; water flow 760 L/min; water temperature 88 °C at the main hose; gauge pressure 7,600 kPa at the main pumps.
- Table 6 (24-hour-lifetime hole of 2,500 m): total fuel (AN-8) 21,000 L average, 15,000 L peak; time to drill and ream 30 h average, 27 h peak; hole production cycle 48 h average, 32 h peak.
- Hot-water drilling does not work in the firn: "the firn absorbs hot water without melting a hole"; a separate firn drill (copper-coil conical head with circulating hot water) made the top 50 m at 2 m per hour.
- A Rodwell supplies make-up water to compensate for the volume change from ice to water in each hole; the Rodwell cavity needs "development" at the start of each season; the maximum reach of the drill from the equipment site was 450 m.
- Hole lifetime: the hole is made wider than the 35 cm instrument modules to allow for refreezing; the paper's definition: time from end of drilling until the hole closes below the module diameter.

**DERIVED cross-check of the melt energy per hole.** Hole volume = π × (0.30 m)² × 2,500 m = 707 m³ of ice (upper bound, since the top 50 m of firn was made by the firn drill); mass at 917 kg/m³ = 648 t. Energy to warm from an assumed mean -30 °C to 0 °C and melt = 648,000 kg × (333,550 + 2,030 × 30) J/kg = 648,000 × 394,450 J/kg = 2.56e11 J = 256 GJ. Thermal energy delivered by the drill = 4.7 MW × 30 h × 3,600 s/h = 5.08e11 J = 508 GJ. So the melt itself is about half of the delivered thermal energy (ratio 0.50); the rest is heat carried off in the return flow and lost to the hole walls, which are heated to a wider reamed diameter. (The assumed mean ice temperature of -30 °C is my estimate; the reamed diameter is larger than 60 cm in places.) 1 GWth = 213 EHWD thermal powers (1e9 / 4.7e6).

### 2c. Hot-water drilling elsewhere

- UNVERIFIED (search snippet only): the WISSARD drill at Subglacial Lake Whillans (2013) is described as a "1000 kW class" drill, delivering over 270 L/min of 90 °C water through a 1,000 m hose; power from two 225 kW generators plus the IceCube power distribution module; the borehole was over 800 m and the initial hole took about 24 hours. Not opened at the source.

### 2d. Camp Century and the PM-2A reactor

- SOURCED to Wikipedia "Army Nuclear Power Program" (secondary; cites *Army Research and Development Magazine* 1963): PM-2A at Camp Century: "2 MW electric, plus heating"; first criticality 3 October 1960; "successfully powered Camp Century for three years"; "shut down 1963–1964"; enrichment 93 percent. A search snippet from a blog (UNVERIFIED) gives 10 MWt (thermal) for the contract plant; the repo-level 2 MWe is consistent with the ANPP page. The reactor was removed in 1964 and the camp abandoned in 1966 or 1967 (sources disagree; UNVERIFIED snippets).
- SOURCED to Wikipedia "Camp Century" (secondary; the fetch tool's summary, not a quote of the page text): the reactor was shut down because of "unexpected accelerated compression of the reactor trenches"; the page links the compression partly to residual heat from the reactor area needed to keep the feed-water pools from freezing; by about 1963 the trenches "had compressed both vertically and horizontally" and needed extensive trimming; a 1962 core survey showed liquid waste (sewage) had spread up to 170 ft (52 m) horizontally; the sewage sump was 150 ft from the nearest building. (The statement that reactor heat contributed to the compression is the fetch tool's reading of the page and should be checked against the Army engineering reports before use.)
- SOURCED (search snippets, UNVERIFIED as to detail): reactor heat ran lights and hot showers for about 200 men; radioactive cooling water was left in a sump in the ice.
- **NOT FOUND:** a primary Army/CRREL document stating where the PM-2A's rejected heat went (cooling water volume, discharge temperature, melt cavity size); the Clark 1965 report was not retrieved. Queries and dead-end locations are in the log.

### 2e. Thermal-pollution assessment of an Antarctic station

- **NOT FOUND.** Searches for an environmental assessment of waste heat from an Antarctic station returned the NSF's reconstruction EIS announcement (1994) and 1991 programmatic EIS without a heat-rejection analysis; the Rodwell-4 EIA was not retrieved. Not opened: NSF 1994 Federal Register notice, ORNL Antarctic EIA page.

---

## Q3. Published thermal models of heat sources in ice

- **Existence and context (SOURCED, secondary).** Pacific Northwest National Laboratory/Sandia report "Basis for Identification of Disposal Options for Research and Development for Spent Nuclear Fuel and HLW" (March 2011), section 6.2 (read locally): ice-sheet disposal was proposed by Bernhard Philberth (1958, 1961) and evaluated in the 1974/1976 studies (Schneider and Platt 1974; ERDA 1976) and the 1980 Generic EIS. Designs: **melt-down** (each canister in a 50 to 100 m borehole, spaced "1 km, which limits heat source interference"; "would melt down through the ice at a rate of 1 to 1.5 m/day, and reach bedrock after 5 to 10 yr (Aamot 1967)"); **anchored emplacement** (20,000 to 30,000 years to reach bedrock, optimistic); **surface storage** on jack-up pilings (air-cooled, retrievable for about 400 years). Paterson (1976) warned that hot packages reaching bedrock may increase basal slip. A panel (Bull 1975) concluded Antarctic ice was not suitable to protect the biosphere "for several hundred thousand years". The report notes the Antarctic Treaty System "specifically forbids the disposal of radioactive waste".
- **Philberth's thermal papers (identified; text blocked).** K. Philberth, "On the temperature response in ice sheets to radioactive waste deposits", *Journal of Glaciology* 16(74):89-98 (1976), and "The disposal of radioactive waste in ice sheets", *Journal of Glaciology* 19(81):607-617 (1978); "Atomkernenergie-Risiken und Atommüll-Deponierung im Eis", *Polarforschung* 46(2):106-120 (1976). Cambridge Core returned HTTP 403 for both *Journal of Glaciology* papers (article pages and PDFs); the AWI repository PDF of the *Polarforschung* paper was behind a bot-protection page. Bibliography SOURCED from philberth.de.
- **UNVERIFIED (search snippet of the 1976/1978 papers' content):** the waste containers melt down to a depth of about 2 km; "the total disintegration heat is spread through a volume of 100 km² × 2 km. The mean temperature increase in this volume is a few degrees"; the temperature rise "does not influence the rheology of the ice sheet at any time"; canisters melt down while their thermal power exceeds the conductive heat loss; waste near the bed raises basal temperature and "could make the ice sheet slide over its bed". I did not see the thermal power assumed, so the figure **per unit power and per unit area is NOT FOUND**.
- **Zeller et al.:** "Putting Radioactive Wastes on Ice" (Zeller, Saunders, Angino), *Bulletin of the Atomic Scientists* 29(1):4-52 (1973), and Zeller, Angino and Saunders 1976, are cited; text not retrieved. A 1974 student-newspaper report (*University Daily Kansan*, 27 September 1974, OCR text; SOURCED but poor-quality secondary) says canisters "hotter than 500 degrees Fahrenheit" melt down "at a rate of about three feet a day", taking "three to five years" to reach rock more than a mile down, one canister about 1 ft × 10 ft per "four square miles"; no thermal results.
- **Thermal probes (Philberth probe, self-melting).** SOURCED (secondary; K. Philberth 1976 in *Ice-Core Drilling*, summarized in search snippets): 1968 EGIG Jarl-Joset probes reached 218 m and 1,005 m in Greenland before the main heater failed (UNVERIFIED snippet). A CRREL/Journal of Glaciology snippet (UNVERIFIED) gives about 5 kW for a speed of 2.5 m/h in ice at -28 °C; another snippet gives 5 to 15 kW for 2.5 to 5 m/h. **DERIVED consistency check on the 5 kW figure:** area of melted column = P / (v ρ (L + c ΔT)) = 5,000 W / [(2.5/3,600 m/s) × 917 kg/m³ × (333,550 + 2,030 × 28) J/kg] = 5,000 / (6.944e-4 × 917 × 390,390) = 5,000 / 2.486e5 = 0.0201 m², which is a 16 cm diameter column, a plausible probe size. This shows the energy needed per meter of melt column, not a model of far-field temperature.
- **More recent modeling of buried heat sources in cold ice:** NOT FOUND in this session beyond the above (no recent paper retrieved).

---

## Q4. Derivations (working shown)

Inputs (all labeled above): ice conductivity k(T) = 9.828 exp(−0.0057 T[K]); diffusivity α = 1.15e-6 m²/s (CRREL); L = 333.55 kJ/kg; c_i = 2,030 J/(kg K) (a slight overstatement at -50 °C); ρ_ice = 917 kg/m³; surface mean -49 °C; year = 3.156e7 s.

### 4a. Steady conduction through a plate of ice (area A, thickness d)

q = k̄ ΔT / d, with the hot face at the melting point 0 °C and the cold face at the surface annual mean -49 °C; ΔT = 49 K; k̄ taken at -25 °C = 2.39 W/(m K) (ice, not firn). Area required to conduct P = 1 GW: A = P / q.

| Plate thickness d | q = 2.39 × 49 / d (W/m²) | Area to conduct 1 GWth |
|---|---|---|
| 10 m | 11.7 | 85 km² |
| 100 m | 1.17 | 854 km² |
| 1,000 m | 0.117 | 8,540 km² |
| 2,700 m | 0.043 | 23,100 km² |

Scale: 10 GWth ×10, 100 GWth ×100, 600 GWth ×600 of each area (for example 600 GWth through a 100 m plate needs 512,600 km², DERIVED 854 × 600). For firn instead of ice the conductivity is lower by a factor of about 2 to 8 (from the UNVERIFIED density-formula values above), and the areas rise by the same factor.
For comparison, the natural heat flow through the whole sheet is 61 mW/m² (SOURCED, Price 2002); DERIVED two-point estimate for ice between -49 °C at the surface and -9 °C at the bed: 2.44 × 40 / 2,810 = 0.035 W/m² (the difference from 0.061 reflects the non-linear measured profile, which includes vertical advection).

### 4b. Transient conduction into cold ice around a 0 °C boundary

Semi-infinite solid at -49 °C, face held at 0 °C: q(t) = k ΔT / √(π α t), with k = 2.39, ΔT = 49 K, α = 1.15e-6 m²/s. Thermal penetration depth √(α t).

| Time | Penetration depth √(αt) | Heat flux q (W/m²) | Area absorbing 1 GWth |
|---|---|---|---|
| 1 yr | 6.0 m | 11.0 | 91 km² |
| 10 yr | 19 m | 3.5 | 289 km² |
| 100 yr | 60 m | 1.10 | 912 km² |
| 1,000 yr | 190 m | 0.35 | 2,885 km² |
| 10,000 yr | 600 m | 0.11 | 9,122 km² |

(Working: at 1 yr, √(π × 1.15e-6 × 3.156e7) = √114.0 = 10.68; q = 2.39 × 49 / 10.68 = 10.96 W/m². Ignores melting at the boundary and the firn's lower conductivity; it is a conduction-only upper bound for ice at a fixed 0 °C face.)

### 4c. Ice melted per year if the heat is dumped into ice

Energy per kg to bring ice from -51 °C to 0 °C and melt it = 333,550 + 2,030 × 51 = 437,080 J/kg (437 kJ/kg; at -30 °C it is 394 kJ/kg). Mass per year = P × 3.156e7 s / 437,080 J/kg.

| Heat | Ice melted per year (mass) | Ice volume per year (917 kg/m³) | Mass rate | Snowfall of how large an area? (74 kg/m² per yr water equivalent, Winski 2019) |
|---|---|---|---|---|
| 1 GWth | 7.22e10 kg (72 Mt) | 7.9e7 m³ (0.079 km³) | 2.29 t/s | 976 km² (circle radius 18 km) |
| 10 GWth | 7.22e11 kg | 7.9e8 m³ (0.79 km³) | 22.9 t/s | 9,757 km² (radius 56 km) |
| 100 GWth | 7.22e12 kg | 7.9e9 m³ (7.9 km³) | 229 t/s | 97,569 km² (radius 176 km) |
| 600 GWth | 4.33e13 kg | 4.7e10 m³ (47 km³) | 1,373 t/s | 585,413 km² (radius 432 km) |

(Working for 1 GWth: 1e9 W × 3.156e7 s = 3.156e16 J; ÷ 437,080 J/kg = 7.22e10 kg; ÷ 917 = 7.87e7 m³. Snowfall mass over area A = 74 kg/m² × A; A = 7.22e10 / 74 = 9.76e8 m² = 976 km².) Note this is melting to 0 °C water without raising the water temperature further; heating that water to the 29 °C of a Rodwell return, for example, would add 4.19 kJ/(kg K) × 29 K = 121 kJ/kg (c of liquid water recalled, UNVERIFIED) or about 28 percent more energy per kg, so the melt mass would fall by that fraction. Meltwater that does not stay liquid refreezes and returns its heat to the surrounding ice, so the table gives the mass that the heat could melt, not the mass that stays liquid.

For orientation: a Rodwell input of 87.9 kW melts 87,930 W × 3.156e7 / 437,080 = 6.35e6 kg per year (6,350 t), if all the heat went to melting (it does not; the report's losses and withdrawal are significant).

### 4d. Air volume and surface area to reject the heat to air

Air density at the Pole in winter: ρ = p / (R T) = 67,400 Pa / (287.05 × 224 K) = 1.048 kg/m³ (p from Hudson and Brandt 2005 Fig. 3; R and cp of dry air recalled, UNVERIFIED; cp = 1,005 J/(kg K)).

Air mass flow to carry P = 1 GWth with air heating of ΔT_air: ṁ = P / (cp ΔT_air).

| Air heating ΔT_air | Mass flow per GWth | Volume flow per GWth | Cross-section at 4.2 m/s wind (m²) | Crosswind width if mixed through 600 m depth at 4.2 m/s |
|---|---|---|---|---|
| 5 K | 199,000 kg/s | 190,000 m³/s | 45,200 | 75 m |
| 20 K | 49,800 kg/s | 47,500 m³/s | 11,300 | 19 m |
| 40 K | 24,900 kg/s | 23,700 m³/s | 5,650 | 9.4 m |
| 60 K | 16,600 kg/s | 15,800 m³/s | 3,770 | 6.3 m |

For 10, 100 and 600 GWth multiply by 10, 100, 600; for example at ΔT_air = 40 K, 600 GWth needs 1.42e7 m³/s of air (DERIVED: 23,731 × 600) and a 5.65 km crosswind width at 4.2 m/s through a 600 m layer. The wind speed 4.2 m/s is the vector mean (Hudson and Brandt Table 1) and the 600 m depth is the winter inversion depth (Table 2); both are inputs, not design values. Heating the whole inversion layer by ΔT_air of 5 to 20 K compares with the layer's own inversion strength of about 20 K (SOURCED above).

**Finned heat-exchange area: data from real air-cooled condensers.** SOURCED: Black Hills Power presentation to the ACC Users Group (6 November 2012), "Black Hills Power – ACCs", read locally: Wygen III ACC: 18 fans, 4,500 hp total, surface area 7,500,000 ft², heat rejection 550.3 MMBtu/h (160 MW), rated 3.5 in Hg abs at 92 °F; Wygen I and II: 152 MW, surface 2,169,150 ft² (Wygen I original) to 4,652,000 ft² (Wygen II), rated 6.0 in Hg abs at 72 °F (Wygen I) and 5.0 in Hg abs at 92 °F (Wygen II); fans 10 to 18. DERIVED: Wygen III finned surface 7.5e6 ft² × 0.0929 = 696,800 m² for 550.3 MMBtu/h × 0.29307 = 161.3 MW, so 4,320 m² of finned surface per MWth, or 4.3 km² of finned surface per GWth at those design conditions (a hot-ambient design; the finned surface is not the ground footprint, and the footprint was not given). Fan nameplate power: Wygen III 4,500 hp × 745.7 W/hp = 3.36 MW, which is 2.1 percent of the heat duty; Wygen I 2,000 hp = 1.49 MW for 152.7 MW, 1.0 percent (nameplate, not measured power). The design air temperature margin there is small (design 92 °F = 33 °C ambient); the Pole's ambient of -49 °C against a condensing temperature near freezing would give a much larger temperature difference (so less surface per MW), but I did not find a source that states the resulting surface area; the scaling is NOT FOUND and I do not assert it.

### 4e. Radiative area

See Q6 below (area per GWth for a surface radiating to the clear Pole sky).

---

## Q5. Rejection to the air

### 5a. Air-cooled condenser and dry-cooler limits at low ambient

- **Freezing risk and fan control (SOURCED to the Black Hills presentation, read locally):** Neil Simpson 1 lessons learned: "Unable to maintain consistent back pressure during low ambient temperatures due to limit of 3 speeds of fans"; "Icing during ambient temperatures below freezing – condenser warm-ups"; "Wind speed and direction were a larger factor than anticipated in both hot and cold ambient temperatures"; spray-water additions caused scaling and ice problems; "Ice in condenser and warm-ups during cold ambient temps created hotwell & misc. drain tank level problems"; design condition "Wind velocity 50 mph at air temps down to -20°F" (-29 °C). An axial fan of 20.8 ft diameter, 6 blades, 200 rpm, 150 hp motor, was used on that older unit. A search snippet (same deck, UNVERIFIED as to the specific numbers on the chart) says output fell about 4 MW at 11 °F ambient versus a gain of 7 MW at 97 °F.
- **UNVERIFIED (search snippets; sources 403 or not opened):** a Chinese direct-air-cooled-condenser study (Energies 13:170) says at low ambient "the exhaust steam flow rate and the face wind speed have little influence on the exhaust steam pressure ... so it is necessary to take anti-freezing measures"; an MDPI Energies 10(11):1872 study finds the fin base to be the most vulnerable spot at part load; a US patent (US 3,958,429) describes reversing condenser fans at low ambient; freeze risk is highest with low steam flow in one condenser row at ambient below the freezing point of the condensate (US 4,045,961 snippet).
- **NOT FOUND:** a design or operating limit for an ACC or dry cooler at -40 °C to -50 °C (vendor guides, EPRI/ASME papers); fan power fraction of output at -30 °C or colder; any ACC at a plant colder than the Black Hills data (-29 °C design). The MDPI pages returned 403 and were not worked around.

### 5b. Precedents in cold climates (Yakutsk, Fairbanks, Norilsk, Bilibino, Pevek, Arctic Canada)

- **Fairbanks: SOURCED, primary-grade** (C. S. Benson, "Ice Fog", *Engineering and Science* (Caltech), May 1969, read via OCR of the PDF): the five Fairbanks-Ft. Wainwright plants' **cooling water** was the largest man-made water vapor source: "one power plant discharges about 110 gallons of water per second at a temperature of 15 degrees C into a stagnant slough. The water remains, for 3 kilometers, as a stretch of open water which does not freeze even in the coldest weather. The resulting evaporative loss ... is nearly 900 tons of water per day. The five power plants contribute a total of 23,400 gallons per minute. The evaporative loss from this source exceeds 2,500 tons of water per day and constitutes 64 percent of the total man-made input" (table: total 4,063 tons/day of water vapor; cooling water 2,600; power plant coal combustion 760; gasoline 124; fuel oil 202; domestic coal 207; miscellaneous 170).
- **Current practice at Fairbanks (UNVERIFIED, search snippets):** a 2024 UAF article says ice fog now occurs about 6 days a year on average (1990 to 2020) and that a warm open stretch of the Chena River from power-plant cooling water remains a contributor.
- **Yakutsk:** a search snippet (UNVERIFIED) names the combined heat and power plants (YaTETs, YAGRES, YAGRES-2) and says ice fog forms over the city under stable high pressure, with moisture from combustion and respiration; no measured power-plant contribution or fog extent was found. **NOT FOUND:** Yakutsk power-plant heat rejection design, urban heat island numbers.
- **Bilibino (EGP-6 reactors, 48 MWe total):** a search snippet describes the reactor type; the heat sink design (cooling towers, air-cooled condensers) was **NOT FOUND** (one travel page mentions cooling towers; UNVERIFIED). Pevek (floating plant), Norilsk and Arctic Canada: **NOT FOUND**.

### 5c. Ice fog and plume effects

SOURCED: Benson 1969 (above):
- Formation: "Ice fog is produced when the water vapor output from urban environments meets an air mass which is too cold to dissolve it and cold enough to crystallize the condensed vapor into tiny (5 to 10 microns) ice crystals. The condition becomes increasingly serious as air temperatures go below -35 degrees C."
- Extent: "The ice fog layer has a vertical thickness of about 10 meters and rarely exceeds 30 meters, but its thickness and density increase during extended periods when temperatures remain below -40 degrees. Then street level visibility ... [is] reduced to less than 10 meters." "The present sources maintain a maximum ice fog volume of about 3 billion cubic meters over a fairly well-defined area of nearly 200 square kilometers."
- Saturation: "air in L.A. at 20 degrees C can hold 255 times more water in solution ... than air at -45 degrees C in Fairbanks ... the saturative value for the air is less than 0.1 grams of water per cubic meter."
- Crystals about 5 microns with terminal velocity under 1 cm/s; they adsorb pollutants (0.5 percent of mass foreign matter).
- Plume interaction: the 19 percent of vapor from power-plant stacks contributes less to ice fog than the 3 percent from car exhaust because stack height matters, "The latter become very important when the thickness of the fog increases sufficiently so that the power plant exhaust plumes blend into it." Photograph captions show stack plumes penetrating the fog.
- Inversion context: Fairbanks inversions "range up to 30 degrees per 100 meters"; winter low-level winds "almost always less than 2 meters per second" under strong inversions.
- Secondary (search snippets, UNVERIFIED): Kumai and O'Brien 1965 reported fog persisted at -40 °C or lower over populated areas while ice nucleation was observed near -20 °C; a 1973 report lists -20 °C or lower, a continuous source of vapor, and particulate matter as the three factors.
- **DERIVED (scale of the Benson vapor flow):** 2,600 tons/day of evaporated cooling water = 2.6e6 kg/day; at a latent heat of vaporization of about 2.5 MJ/kg (recalled, UNVERIFIED) this is 2.6e6 × 2.5e6 / 86,400 s = 75 MW of latent heat carried by the vapor. That evaporative path is not available for a dry (air-cooled) system; a dry system releases sensible heat to air with no added vapor except from stack or boiler emissions.
- **NOT FOUND:** any record of ice fog from the South Pole station's own exhaust; Hudson and Brandt do not discuss it. Humidity at the Pole was not researched here.

---

## Q6. Radiative rejection

- **Atmospheric brightness temperature on clear winter nights at the Pole: SOURCED.** Hudson and Brandt 2005 (read locally): the median inversion strength is nearly constant at about 3 K (between 2 m and the surface) for downward longwave flux less than 80 W/m²; "This decrease begins around 80 W m−2, or an atmospheric brightness temperature of about −79°C, which is near the lowest temperature reached by the surface." The inversion vanishes by about 150 W/m². The pyrgeometer accuracy is ±4 W/m². So 80 W/m² is the clear-sky floor of downward flux in their winter data; 150 W/m² is about the cloudy end of the range in which the inversion still matters.
- **DERIVED check:** σ T⁴ at 194.15 K (-79 °C) = 5.670e-8 × (194.15)⁴ = 5.670e-8 × 1.421e9 = 80.6 W/m², matching the 80 W/m² statement. An "effective sky temperature" for a blackbody-equivalent sky is therefore about 194 K (-79 °C) for the lowest-flux clear nights, higher with clouds (150 W/m² corresponds to T = (150 / 5.670e-8)^0.25 = 227 K = -46 °C, DERIVED).
- **DERIVED net radiative flux from a hot surface to that sky** (emissivity ε = 0.95, assumed, UNVERIFIED; no convection or conduction counted; no sun, i.e. polar night): net = ε (σ T_r⁴ − F_sky).

| Radiator surface temperature | Net flux, sky 80 W/m² | Area for 1 GWth | Net flux, sky 150 W/m² | Area for 1 GWth |
|---|---|---|---|---|
| 223 K (-50 °C) | 57.6 W/m² | 17.4 km² | -8.9 W/m² (no net loss) | not possible |
| 273 K (0 °C) | 223.9 W/m² | 4.5 km² | 157.4 W/m² | 6.4 km² |
| 300 K (27 °C) | 360.3 W/m² | 2.8 km² | 293.8 W/m² | 3.4 km² |
| 323 K (50 °C) | 511.4 W/m² | 2.0 km² | 444.9 W/m² | 2.25 km² |

(Working: at 273.15 K, σT⁴ = 315.6 W/m²; ε × (315.6 − 80) = 0.95 × 235.6 = 223.9. Areas: 1e9 / net. For 600 GWth multiply areas by 600: for example 2,700 km² at 273 K, clear sky.) A surface radiating also loses heat to the -49 °C air by convection; the convective coefficient for such a radiator was not found, so that extra term is not in the table. The solar term in the polar day is not included; the Pole has about six months of sun.
- **Published ideas or measurements of radiators at polar sites: NOT FOUND.** One search for nocturnal radiative cooling measurements at Dome C or the Pole returned lab and mid-latitude sub-ambient radiative-cooler papers (best-case cooling power of 100 to 150 W/m² for engineered surfaces, snippet UNVERIFIED) and nothing at a polar site. Busetto et al. 2013 (*Antarctic Science* 25:697) parameterizes clear-sky effective emissivity at Dome C and the Pole (bias 0.8 W/m², RMS 6.2 W/m² at Dome C, per the abstract snippet, UNVERIFIED); the text itself was behind Cambridge Core (not fetched).

---

## Q7. Effect of a heat source on the local climate and the ice

- **Fairbanks heat island: SOURCED** (Benson 1969): "In Fairbanks, the city warms the air so that it is about 6 degrees warmer than that of the surrounding areas. This is a significant heat island in the Tanana Valley, but it does not destroy the strong surface inversions because they always involve temperature increases of more than 6 degrees C in the first 50 to 100 meters." (Population then about 30,000 plus 2,000 dogs; area of ice fog about 200 km².) Benson also notes most cities "evolve enough heat to prevent low-level inversions from forming" in the lowest 100 m, with city influence "sometimes still evident as high as 200 to 300 meters above the surface".
- **Heat islands of polar settlements at the Pole or other Antarctic stations: NOT FOUND** as a measured quantity. Search snippets (UNVERIFIED): a blog account says McMurdo is "usually much warmer" than the nearby ice shelf; a 2025 EGUsphere preprint on Concordia mentions station effects on snow accumulation and black carbon; no quantification retrieved.
- **Snow drift and heated structures at the Pole: partly found (all UNVERIFIED, search snippets):** the modern elevated station stands on tall pylons with a sloped wind-facing facade "to maximize scouring of the snow beneath the station" and must be raised periodically as snow accumulates; a 2014 CRREL/EPOLAR report says elevated lift systems keep the heated superstructure from thawing the snow foundation; the old dome was too low and was buried; Concordia's main buildings stand on hydraulic feet. A measured effect of heated structures on the local surface mass balance at the Pole was **NOT FOUND**.
- **Camp Century (SOURCED, secondary, Wikipedia):** heat and liquid waste near the reactor trenches coincided with compression of the trenches and the spread of liquid waste to 52 m laterally (above); the cause assigned to heat by that page is the fetch tool's summary and should be checked.
- **Rodwell cavity management (SOURCED above):** retire a cavity when it is too deep to heat and recirculate (about 7+ years); use the old one for sewage; start a new one nearby. One cavity at about 90 to 125 kW input grows to a water surface of about 12 m diameter in 1,700 hours (1972-73 well) and to tens of meters in diameter and over 100 m depth over years (design: 144 to 157 m reservoir depth after ten years, CRREL).
- **Basal effects:** heat reaching the bed is the only mechanism reported in the literature for changing basal sliding (Paterson 1976, Philberth 1976, as summarized above); at the Pole the bed is frozen at about -9 °C, 7 °C below the pressure melting point (Price 2002) and the flow is about 10 m/yr. No numbers were found on how a heat source of any size would change this.

---

## FINAL: what the sources support, do not support, and NOT FOUND (2026-11-02)

**What the sources support (SOURCED).**
- Pole air: annual mean about -49 to -50 °C; coldest months about -58 to -60 °C; record -12.3 °C to -82.8 °C; winter surface inversion about 20 K and 585 to 665 m deep; vector-mean wind 4.2 m/s from about 40°; surface pressure 674 hPa; clear-night downward longwave floor 80 W/m², equal to a brightness temperature of -79 °C.
- Pole ice: 2,810 to 2,812 m thick; surface ice and firn -51 °C; -9 °C at the base, 7 °C below pressure melting; frozen to bedrock at the Pole; geothermal flux 61 mW/m²; flow 10 m/yr; accumulation 7.4 cm/yr w.e.; firn density 349 kg/m³ at the surface, 793 kg/m³ at 97.5 m, ice density by about 158.5 m (CRREL fit to Langway 1975). Upstream of the Pole, at the divide, a 100 km × 50 km region has basal melting up to 6 mm/yr at 120 mW/m².
- Precedents: the Pole Rodwell has run on waste heat from the station power plant, with design input 88 to 97 kW per cavity and cavities replaced about every 8 to 18 years; the first (1972-73) well took about 126 kW and made a 12 m wide cavity in 1,700 hours; the IceCube drill melted about 700 m³ ice per hole with 4.7 MWth in 30 hours; Camp Century's reactor was 2 MWe plus heating, 1960 to 1964.
- Fairbanks: cooling-water evaporation was 64 percent of the area's vapor input in 1969; ice fog is 10 m thick (rarely over 30 m) over about 200 km² in a city of 30,000; the city's heat island was about 6 °C.
- DERIVED scale: 1 GWth melts 72 Mt of ice per year (the snowfall of about 980 km²); 600 GWth melts 47 km³ per year (snowfall of about 585,000 km²); steady conduction through ice of 100 m thickness carries about 1.2 W/m², so 1 GWth needs about 850 km²; air flow to carry 1 GWth at +40 K is about 23,700 m³/s; a surface at 0 °C radiating to the clear sky at 80 W/m² gives about 224 W/m², so 1 GWth needs 4.5 km² (clear sky, no sun, no convection).

**What the sources do not support.**
- Nothing in the sources gives a reactor-scale (hundreds of MW or more) heat dump at the Pole or on any ice sheet. The largest sustained heat inputs found in polar ice are the ones above (kW to MW).
- Nothing found says how much ice-sheet heat a Pole-sited plant could be rejected into without consequence; the derived numbers are bounds from conduction and latent heat alone, not model results.
- The claim that Camp Century reactor heat caused the trench compression rests on a fetch-tool reading of Wikipedia and should not be used without the Army reports.

**NOT FOUND (queries logged below; "dead end died at" noted).**
- Reactor-scale heat dump at the Pole (expected; no study exists in what was found).
- Philberth (1976, 1978) and Zeller papers' numbers per unit power and unit area (died at the sources: Cambridge Core 403, AWI repository bot-protection page, DTIC 403).
- Primary description of where PM-2A's rejected heat went (died at the query and the sources: only popular accounts returned).
- Thermal-pollution assessment of an Antarctic station; the Rodwell-3 and Rodwell-4 EIA documents (died at the query: only 1990s NSF documents surfaced).
- Firn thermal conductivity coefficients and specific heat of ice at -50 °C (died at the sources: the Cryosphere 2021 page lacked the equations).
- SPICEcore firn density table and firn-ice transition depth in numbers (died at the sources: tables not in the extracted text).
- ACC / dry cooler design and operating limits at -40 °C and below; fan power fraction at those temperatures (died at the sources: MDPI 403; search returned patents and a mid-latitude plant deck).
- Yakutsk, Norilsk, Bilibino, Pevek, Arctic Canada plant heat-rejection designs and ice-fog numbers (died at the query/sources: news and travel pages only).
- Radiators or radiative coolers at a polar site (died at the query).
- Measured heat island of the Pole or another Antarctic station; measured effect of warm structures on surface mass balance at the Pole (died at the query/sources).

**Surprises worth a second look.** (1) The first Pole water well (1972-73) made a 12 m cavity with only about 126 kW, and the design waste-heat input for a ten-year well is 88 to 97 kW; a GWth is more than ten thousand of these. (2) The CRREL report's firn model has ice density only below 158.5 m, so the Pole's firn is about 160 m thick in that fit (close-off 120 to 123 m is a separate snippet figure). (3) The Jordan et al. 2018 finding of a 120 mW/m² geothermal anomaly with basal melt upstream of the Pole contrasts with the frozen bed at the Pole itself. (4) A conduction-only bound (1 GWth through a 100 m ice plate needing about 850 km²) is almost the same as the snowfall area that 1 GWth would melt each year (980 km²); both are coincidental outputs of the same inputs, not a design statement. **End: 2026-11-02 21:26 MST.**

---

## SEARCH LOG (68 web calls; S = WebSearch standard unless noted, F = WebFetch)

Result: hit = answered; partial = some figures; miss = nothing usable. "Died at" for dead ends.

1. S "Rodriguez well Rodwell South Pole station water source cavity melt power": partial (led to brr.fyi, southpolestation.com, Wikipedia, CRREL SR 95-10).
2. S "SPICEcore South Pole ice core firn density temperature profile mean annual temperature": partial (abstracts only).
3. F icecube.wisc.edu thermal_rodwell_crrel.pdf: partial. The PDF is the same CRREL report (scanned images); the fetch tool could not read it; read via local OCR of the copy (title page confirms SR 95-10).
4. F brr.fyi South Pole Water Infrastructure: hit (blog).
5. F southpolestation.com Rodwell page: hit.
6. F apps.dtic.mil ADA295513: miss, 403 (died at the source).
7. F icedrill.org SR-95-10_0.pdf: binary; read via local OCR: hit (primary report).
8. F en.wikipedia Rodriguez_well: hit (secondary).
9. S "South Pole ice flow velocity 10 m per year direction ice thickness 2700 m bed frozen radar": partial (snippets: 10 m/yr, 40° W, 14-15 percent speed-up).
10. S "IceCube South Pole ice temperature profile borehole logging -51 °C surface to -9 °C bottom": partial (Price 2002 found).
11. S "Amundsen-Scott South Pole station climate record temperature highest -12.3 lowest -82.8 annual mean -49.5 inversion": partial (extremes).
12. F pmc.ncbi.nlm.nih.gov PMC122982 (Price et al. 2002): hit.
13. F rcastoragev2 PMC6235973.pdf (Jordan et al. 2018): binary; read via local text extraction: hit.
14. S "IceCube enhanced hot water drill 5 MW thermal power fuel hole 2500 m 60 cm diameter time per hole": hit.
15. S "Camp Century PM-2A reactor waste heat 2 MWe cooling water ice tunnel thermal discharge 1960s": partial (popular accounts; died at the sources).
16. F arxiv.org/pdf/1612.05093: binary; read via local text extraction: hit.
17. F dx.doi.org 10.3189/2014AoG68A033: redirect to Cambridge Core; not followed (Cambridge Core blocked other fetches).
18. S "PM-2A Camp Century 1.56 MW electric reactor 10 MWt heat used for melting water trench Army Nuclear Power Program": partial.
19. S "Camp Century PM-2A reactor cooling ice melting waste heat sump 'Camp Century' engineering report Clark 1965 power plant": partial (died at the query: Clark 1965 report not surfaced).
20. F overlandtrains.com PM-2A: partial (cost and fuel only).
21. F en.wikipedia Camp_Century: partial (trench compression; paraphrased by the tool).
22. S "Philberth self-sinking probe radioactive waste disposal Antarctic Greenland ice sheet heat source temperature rise melting radius thermal": partial.
23. S "Zeller Saltzman Dowell 1973 disposal of radioactive waste in Antarctic ice sheet thermal analysis refreezing Science": partial (correct citation: Zeller, Saunders, Angino 1973, Bulletin of the Atomic Scientists).
24. F cambridge.org S0022143000215517a.pdf (Philberth 1978): 403 (died at the source).
25. F cambridge.org S0022143000031440 (Philberth 1976): 403.
26. F digital.lib.ku.edu 110934 OCR: partial (1974 student newspaper; poor).
27. F digital.lib.ku.edu 29397 OCR: miss (no thermal data).
28. F resolve.cambridge.org core-reader 80D962FE: 403.
29. F apps.dtic.mil AD0672057.pdf: 403.
30. S (extended) "Philberth 1976 'temperature response' ice sheets radioactive waste deposits abstract heat per area W/m2 2 km depth mean temperature increase degrees": partial (abstract numbers only as snippet).
31. F tc.copernicus.org tc-2022-100-ATC3.pdf: binary, not relevant on inspection; not read further.
32. F cambridge.org article 80D962FE (1976): 403.
33. F cambridge.org article 4BF2EA75 (1978): 403.
34. F link.springer.com BF02634783 (Angino et al. 1976): redirect to a login authorization URL; not followed.
35. F curie.pnnl.gov M21UF033701 pdf: binary; read via local text extraction: hit (section 6.2).
36. F philberth.de literature/bibliography: hit (citations).
37. F hdl.handle.net/10013/epic.29441.d001: redirect to epic.awi.de (followed once as a new fetch).
38. F epic.awi.de Polarforsch1976_2_4.pdf: miss (bot-protection page; died at the source; not worked around).
39. S "Lazzara Keller Markle Fifty-year Amundsen-Scott South Pole station surface climatology annual mean temperature wind speed": partial (abstract only).
40. S "South Pole surface-based temperature inversion strength depth ... Hudson Brandt 2005": hit (found PDF).
41. F atmos.uw.edu HudsonBrandt2005.pdf: binary; read via local text extraction: hit.
42. F amrdcdata.ssec.wisc.edu South Pole 1957-2011 dataset page: miss (no statistics; dataset zip not downloaded).
43. F en.wikipedia Amundsen–Scott_South_Pole_Station: hit (climate table). Second half of page not read.
44. S "SPICEcore firn density profile South Pole close-off depth 120 m firn thickness accumulation 7.4 cm water equivalent Winski 2019": partial.
45. F par.nsf.gov purl 10535453 (Yang et al. 2024): binary; read via local text extraction: hit (site numbers only; no firn density table).
46. F cp.copernicus.org articles/15/1793/2019 (Winski 2019): hit (site numbers; no firn profile).
47. S "South Pole firn air Battle 1996 firn diffusive zone convective zone depth density surface 350 kg m-3 close-off 122 m": miss (died at the query).
48. S "thermal conductivity of snow and firn as function of density formula Calonne Sturm ...": partial (no coefficients).
49. F tc.copernicus.org articles/15/4201/2021: partial (no equations; died at the sources).
50. F en.wikipedia Properties_of_water: partial (L, c_i at -10 °C, density).
51. S "ice fog Fairbanks power plant cooling water vapor emission temperature below -30 C threshold extent plume Benson 1970 ice fog": hit (found Benson 1969).
52. F calteches.library.caltech.edu ice.pdf (Benson 1969): binary scan; read via local OCR: hit.
53. F core.ac.uk 162574322.pdf: 403.
54. S "air-cooled condenser cold weather operation freezing risk minimum ambient temperature turn-down fan power -40 °C steam turbine power plant design": partial.
55. S "effective sky temperature Antarctic plateau clear sky clear dry night downwelling longwave radiation South Pole W/m2 radiative cooling": partial.
56. S "South Pole station elevated building snow drifting dome arches buried heat island snow melt below station heated structures effect on surface mass balance": partial (no measurements).
57. S "Antarctic station heat island measured warming near buildings McMurdo Davis Concordia station thermal pollution local temperature increase snow": miss (blog and preprint comments only).
58. S "Yakutsk ice fog heat island city urban temperature winter -40 °C power plant water vapor emission fog extent Gavrilova Yakutsk atmosphere": miss/partial (died at the query).
59. F mdpi.com 1996-1073/10/11/1872: 403.
60. S "Bilibino nuclear power plant cooling system air-cooled condenser or cooling pond permafrost Arctic reactor heat rejection": miss (heat sink design not found).
61. S "air-cooled condenser performance ambient temperature turbine backpressure low ambient fan power consumption percent of output dry cooling cold climate -30 °C": partial.
62. F mdpi.com 1996-1073/13/1/170/html: 403.
63. F acc-usersgroup.org Black Hills Power ACCs pdf: binary; read via local text extraction: hit.
64. S "South Pole Station Rodwell 4 environmental evaluation Rodwell 3 cavity capacity waste heat generators glycol Antarctic Treaty EIA": miss.
65. S "hot water drill power kW subglacial Lake Whillans WISSARD ...": partial (snippet only).
66. F en.wikipedia Army_Nuclear_Power_Program (PM-2A): hit (secondary).
67. S "Philberth probe thermal probe power kW sinking rate m per day heated probe ice Greenland 1968 Jarl-Joset 1005 m self-sinking melting": partial (snippets).
68. S "nocturnal radiative cooling measurement Antarctica Dome C OR South Pole radiator sub-ambient cooling power W/m2 clear sky selective emitter polar": miss for polar sites.

Not opened though surfaced: Lazzara et al. 2012 full text; Busetto et al. 2013; Philberth probe papers on Cambridge Core; Kumai and O'Brien 1965; Hokudai ice-fog PDF; DTIC AD0676811 and AD0691325 (ice-fog/CRREL reports, 403 pattern expected); the Antarctic Treaty EIA database; Dome C radiative-budget paper (Cambridge Core). The Rodwell scratch OCR and text extractions are in the session scratchpad, not in the repo.
