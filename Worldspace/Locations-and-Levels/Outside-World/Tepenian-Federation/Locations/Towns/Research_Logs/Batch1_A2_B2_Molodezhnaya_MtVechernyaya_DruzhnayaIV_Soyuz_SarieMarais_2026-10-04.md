<!-- Log written 2026-10-04: the research agent's full report, extracted verbatim from its transcript (not re-typed). Findings filled into ../Towns_Priority_Batch_1_Reference_2026-10-04.md (#18 Molodezhnaya, #19 Mountain Evening, #10 Druzhnaya IV, #32 Soyuz, #31 Sarie Marais). Operators are context only. NOTE: ice velocities here are the agent's own ITS_LIVE v2 computations (vector-median per pixel); ITS_LIVE cannot separate rock from ice, so 0 to 3 m/yr means stationary-or-rock, not proven bedrock. -->

# Research report: five stations (Molodezhnaya, Mountain Evening, Druzhnaya IV, Soyuz, Sarie Marais)

Conventions
- All sources were accessed 2026-10-04 unless a snapshot date is given. Source keys [S#] are in the table at the end.
- "(own computation)" marks numbers I calculated here. "(unverified)" marks facts seen only in a search-engine summary or a Wikipedia-derived summary, not in a primary document I opened.
- The operating nation or program is context only. The test applied throughout is "ice not moving fast enough to force relocation; ideally bedrock below".
- Ice-velocity method (own computation, [S15]):
  - Data: ITS_LIVE v2 (Oct 2024 cubes, 120 m pixels), 6,000 to 32,000 image pairs per cube.
  - Method: per pixel, the temporal median of vx and vy separately, then the magnitude of that vector. A median of scalar speed is biased upward by noise: at known rock it gave about 19 m/yr, whereas the vector-median gives about 0 to 2 m/yr.
  - Limit: nothing in ITS_LIVE separates rock from ice. A reading of 0 to 3 m/yr means "stationary or rock", not "proven bedrock". I found no independent second velocity product (MEaSUREs/Mouginot) and no ice-thickness grid. Bedmap3 returned 503 and BedMachine needs a login.
- DEM method (own computation, [S16]): REMA v2.0 32 m mosaic, ellipsoidal heights converted to EGM96 with PROJ geoid grids. The conversions are approximate.

Key corrections to the briefing
1. "Mountain Evening" is Belarus's Mount Vechernyaya (Gora Vechernyaya) station, not Chinese or Japanese. [S1][S2][S5]
2. Soyuz was closed 28 Feb 1989 per AARI, not 2007. The "2007" is only a planned or reconditioning date in secondary sources. [S9]
3. Sarie Marais is at Grunehogna (Ahlmannryggen), not near Fuchs Dome. The SCAR gazetteer puts Fuchs Dome in the Shackleton Range at 80.6°S 27.8°W, about 1,142 km away (own computation). [S14]
4. Druzhnaya IV is on Landing Bluff, a rock nunatak at Sandefjord Bay on the north-eastern edge of the Amery Ice Shelf. It is not in the Prince Charles Mountains and not at Beaver Lake. [S3][S6][S8][S14]
5. The "Molodezhnaya airfield" (compacted-snow runway) was built near Mount Vechernyaya, about 10 to 12 km east of the station. It closed 1991 to 1992. Its coordinates are where Belarus now sits. [S4][S7]

---

## 1. MOLODEZHNAYA (Russia, context only)

**Verified coordinates**
- Inventory: -67.6654, 45.8425. COMNAP 2024 gives -67.665443, 45.842038, elevation 40 m MSL. [S1]
- Second sources:
  - COMNAP 2017 catalogue: 67°40'S 45°51'E, 40 m. [S3]
  - Australian inspection 2020: 67°40'S 45°51'E. [S5]
  - SCAR gazetteer (AUS entry): -67.6667, 45.85. This is 0.4 km from COMNAP (own computation). [S14]
- Elevation: 40 m (COMNAP 2024 and 2017); 42 m (TASS) [S13]. REMA-derived about 30 m at the 32 m pixel (own computation, rugged terrain, approximate).
- Warning: the SCAR gazetteer's USA entry "Molodezhnaya Station" (from COMNAP, May 2006) is at 46.1344°E, -67.6828, 225 ft/m. That is the old Vechernyaya airfield, 12.6 km from the station (own computation). [S14]

**Surface and stability. Verdict: rock-qualifies. Confidence: high for ground stability, moderate for site hazard.**
- Setting:
  - Parallel ice-free rocky ridges up to 1 km long and about 150 m wide, in the Molodezhny Oasis (Thala Hills).
  - The oasis is 8.3 km by 2.7 km with a maximum height of 110 m.
  - The inland ice sheet rises gradually to the south.
  - More than 40 lakes, up to 36 m deep. [S3]
  - COMNAP lists the surface as "ice-free ground" and permafrost as continuous. [S3]
  - 500 to 600 m from the coast. [S13]
- Bedrock: metamorphic and magmatic rocks (pegmatites, migmatites) of the crystalline basement. [S22]
- Ice velocity (own computation, [S15]): vector-median speed 1.4 m/yr at the station pixel. Median 2.2 m/yr and maximum 7 m/yr within 500 m. Within 3 km, up to 65 m/yr, where inland ice enters the window.
- Literature (via the Belarus CEE, [S4]):
  - Ice-sheet edge about 100 m/yr (Kotlyakov 2000).
  - Hayes outlet glacier 900 to 1,400 m/yr.
  - The Hayes glacier borders the Vechernyaya side of the oasis, not the station.
- Station-specific hazards: [S5][S10]
  - Lake outburst: one large fuel tank near the shoreline "ruptured and collapsed", attributed to a flash flood from a lake blocked by an ice dam.
  - Melt pools around building footings, with buildings destroyed by wind, fire or flooding.
  - Parts of the station area are snow or ice covered, with materials "covered and embedded".
  - On 17 Jan 2025, two RAE staff were evacuated from Molodezhnaya to Gora Vechernyaya "due to the threat of flood inundation and worsening weather".
- No ASPA, ASMA or HSM found for Thala Hills. This is a dead end, not a confirmation (see search log).

**Status and years**
- Opened Feb 1962. Official opening 14 Jan 1963. [S3][S12]
- Two different closure accounts (see Contradictions):
  - Australian 2020: "temporarily closed in 1990". [S5]
  - Rosgidromet: mothballed 1999 during the 44th RAE. [S12]
  - A Russian encyclopedia summary: flag lowered 9 Jul 1999, last wintering (unverified, search summary).
- Since 2006 a seasonal field base. [S3][S5]
- Season: COMNAP 2017 lists December to March, with ship visits Jan/Feb/Mar/Dec. [S3]
- Late use: the Akademik Fedorov called on 27 Apr 2022 for helicopter cargo and passenger work with Molodezhnaya and Gora Vechernyaya. [S11]
- Recent:
  - RAE 70 (2024/25) and RAE 71 (from 5 Nov 2025) both list Molodezhnaya as a seasonal field base. [S10]
  - A Mining University geology team worked at "decommissioned Molodyozhnaya Station" in 70th RAE. [S22]
- Winter population 0. [S1][S3]

**Capacity**
- COMNAP 2017: 15 beds, 15 staff in summer, 7,000 m² under roof. [S3]
- COMNAP 2024: peak 15. [S1]
- Seen by the 2020 inspection: seasonal complement of 7 (leader, 3 drivers/operators, 2 diesel mechanics, cook), no scientists. [S5]
- March 2013: 15 participants plus 3 Belarusian specialists. [S13]
- Historical peak: "up to 150" (encyclopedia summary, unverified).

**Infrastructure** (2020 inspection, [S5])
- About 60 buildings, mostly unused and in poor repair.
- 15 fuel tanks, each over 1 million litres, with about 12 near the former skiway. Appear empty, but residual sludge is unassessed.
- Rocket-launch complex, antenna arrays, water pipeline, derelict Il-14 and vehicles.
- Active seasonal use: about 6 buildings (mess, powerhouse/bathhouse, accommodation, warehouse, mechanical).
- Powerhouse with 3 generator sets, in good condition.
- Fresh water from a melt lake above the station.
- Fuel flown in by helicopter in a bulk bag and pumped to an elevated tank with no secondary containment. The inspectors saw extensive fuel contamination.
- Waste water tankered to sea, but some laundry water goes onto ice-free land.
- Communications: satellite phone and VHF. [S3]

**Access** [S5][S3][S7]
- Cargo and people arrive by ship plus helicopter. Ship landing facilities: none.
- A skiway on the plateau about 7 km from the station is used by ski aircraft and the DROMLAN framework (2020: AAD Basler BT-67; flights between Dronning Maud Land and the Larsemann Hills).
- Original heavy runway: built 1981, about 10 km east near Mount Vechernyaya, compacted snow, 2,540 × 42 m, used Oct to Feb by Il-76TD and Il-18D flying from Maputo and Cape Town. Last prepared Nov 1992. COMNAP 2017 quotes 2,560 × 42 m and "12 km ESE". [S7][S3]
- I did not find a source showing Il-76 landings at Molodezhnaya now. RAE 70/71 route Il-76 DROMLAN flights through Novolazarevskaya and Progress "Zenit". [S10]

**Other facilities within about 25 km**
- Mount Vechernyaya, Belarus (section 2 below).
- Old Vechernyaya airfield camp (Soviet field base). [S4][S5]
- Nearest other COMNAP facility: S17 Camp (Japan) at 281 km (own computation). [S1]

**Stated purpose**
- Historical: main Soviet base; hydrometeorological centre; rocket sounding; geophysics. [S3]
- Today: stabilize or dismantle buildings, clean up, support intracontinental aviation. [S5]
- AARI: "base of field route research". [S13]

**Other notes**
- Climate, mean annual: −11 °C, precipitation 270 mm, wind 38 km/h (SE), 190 snowstorm days a year. [S3][S4]
- Absolute minimum about −42 °C. [S4]
- ATS inspection history: US 1967 and 1983 (on the ground), Australia 2010 (aerial) and 2020 (on the ground, the first in 37 years). [S5]
- Australian 2020 finding: a clean-up would be "a very substantial challenge" and should be "a priority".

**Revival realism (evidence only)**
- The Russian operator is already doing seasonal stabilization with 7 to 15 people.
- 2020 inspectors: a "much greater level of resourcing" would be needed for clean-up.
- A "small Molodezhnaya" consolidation was started in 1998 in order to dismantle buildings and clean the territory. [S3]
- Flood damage is documented in 2020 and again in Jan 2025. [S5][S10]

---

## 2. MOUNTAIN EVENING / Mount Vechernyaya / Gora Vechernyaya (Belarus, context only)

**Verified coordinates**
- Inventory: -67.6583, 46.1533. COMNAP 2024: -67.658333, 46.153333, 95 m MSL, operator "Republic of Belarus", seasonal, "Year Established 2006", peak population 12. [S1]
- Second sources:
  - COMNAP 2017 Belarus sheet: 67°39'35"S 46°09'18"E, 95 m, built on ice-free ground. [S2]
  - Draft CEE 2013: same. Mount Vecherniaya itself is 272 m. [S4]
  - Wikipedia: 67°39′35″S 46°09′18″E, 95 m (lead only).
- Inventory vs Belarus catalogue: 0.2 km apart (own computation).
- Distance to Molodezhnaya: see Contradictions (13 to 28 km depending on source).
- The Australian 2020 report prints "67°35'S" in section 7.2. That is a typo against its own other sources. [S5]

**Surface and stability. Verdict: rock-qualifies. Confidence: high.**
- A flat mountain terrace 350 m long and 50 to 80 m wide, east of the mountain, on enderbite and charnockite gneisses. [S4]
- New modules stand on adjustable legs "with small base plates bolted to bedrock". [S5]
- About 70 % of the wider Mount Vechernyaya territory is glacier-covered. Soils are only 20 cm deep over solid rock. [S4]
- Ice velocity (own computation, [S15]):
  - Station pixel: 0 m/yr.
  - Within 500 m: median 1 m/yr, maximum 3 m/yr.
  - The Hayes outlet glacier starts about 2 to 3 km east, with ITS_LIVE speeds of about 100 to 220 m/yr in the 3 km window.
  - CEE literature gives Hayes at 900 to 1,400 m/yr near Lazurnaya Bay, a different location. [S4]
- Hazards: [S4]
  - Wind: summer means 12 to 18 m/s, gusts up to 53 m/s. COMNAP lists a maximum of 194 km/h.
  - Crevasses on the Hayes glacier and in the ice sheet within 20 to 30 km of the coast.
  - Lake-level instability.
  - 190 snowstorm days a year.

**Status and years**
- A Belarusian seasonal camp inside the Russian field base since 2006, using Russian infrastructure. [S4]
- Station: first 3-section module assembled Dec 2015 to Jan 2016. Second 8-section module commissioned 2020/21. [S2][S18]
- Five-section dining-room complex commissioned for experimental operation 20 Jan 2025. [S10]
- Season: December to March. [S2]
- Planned wintering "from February 2021" (Australian inspection). [S5]
- Belta (2024) still describes it as seasonal. [S18]
- The 15th Belarusian Antarctic Expedition (Oct 2022, 12 people) is described as a "seasonal expedition". [S18]
- I found no confirmation that wintering has begun.

**Capacity**
- COMNAP 2017: 7 beds, 7 staff in summer, 12 maximum at one time, 108 m² under roof, laboratory 21 m², 18 m² medical room. [S2]
- Australian 2020: capacity 8; 7 present; 5 to 7 summer scientists and 3 to 4 winter scientists planned. [S5]
- Belarus Republican Centre for Polar Research (as of 31 Dec 2023): 16 new structures, 9 renovated, supports up to 15. [S18]

**Infrastructure** [S5][S18]
- Container modules on legs.
- Diesel gensets: 2 × 100 kVA, 60 kVA, 20 kVA, 6 kVA backup, plus solar.
- Fuel: 13 m³ stationary storage plus 3 insulated tank-containers.
- Heated water and drain line of about 100 m.
- Water from nearby lakes.
- Satellite (BGAN, FLEET, Iridium, Inmarsat C), HF and VHF; VSAT installed.
- Vehicles: snowmobiles, Apache crawler, BOBR amphibious tracked vehicle.
- Helipad on cleared rock.
- Renovated Soviet buildings: a cylindrical former residence (mess, kitchen, medical), a repaired biology laboratory.
- Hydroponics with LED shelves.
- Older Soviet field base (13 buildings at its peak, 7 left in 2013). [S4]

**Access**
- Ship plus helicopter: Russian RAE provides this on contract. [S5]
- Overland route to Molodezhnaya and its skiway. [S5]
- DROMLAN flights via Molodezhnaya skiway (COMNAP 2017: 4 flight visits a year, 2 ship visits). [S2]

**Other facilities within about 25 km**
- Molodezhnaya (see above).
- The old Russian Vechernyaya field base and aerodrome, about 500 m from the new buildings. [S5]

**Stated purpose**
- Atmospheric aerosol, ozone and UV monitoring (AERONET data), hydrometeorology, biology and ecology, geophysics. [S2][S5]
- A political goal: Antarctic Treaty Consultative Party status. [S4]

**Other notes**
- Protected areas: the CEE found no ASPA, ASMA, HSM or SSSI at the site. [S4]
- Inspected by Australia 27 Jan 2020 (first inspection), found compliant. [S5]
- Nearest emergency facility in Antarctica: 1,400 km. [S2]

---

## 3. DRUZHNAYA IV (Russia, context only)

**Verified coordinates**
- Inventory: -69.7478, 73.7092. COMNAP 2024: -69.747827, 73.709214, 20 m MSL, seasonal, open, peak 50. [S1]
- Second sources:
  - SCAR gazetteer, Landing Bluff (AADC, differential GPS): 69°44'32.1"S 73°42'36.9"E, summit 119 m. This is 0.6 km from the inventory point (own computation). [S14]
  - COMNAP 2017: 69°44'S 73°43'E, 20 m, built on ice-free ground. [S3]
  - Australian 2010: 73°42'E (printed as "59°44'S", a typo). [S6]
  - AARI page: 69°44'S **72**°42'E, which is a typo against all the rest. [S8]
- Elevation: 20 m (COMNAP); 3 m (weather platform, Russian Wikipedia, unverified); 119 m is Landing Bluff's summit, not the camp. REMA about 37 m at the inventory pixel (own computation).

**Surface and stability. Verdict: rock-qualifies. Confidence: moderate-high.**
- The base stands on a rock mass called Landing Bluff (AARI: "nunatak Lending"). It has a steep eastern slope and small outcrops to the south-west, on the south-west part of Sandefjord Bay. [S8][S14]
- COMNAP: "ice-free ground", features "Ice shelf... Nunatak, Rock". [S3]
- The Sandefjord shore has "difficult dissected glacial relief" with several nunataks. The ice barrier is no higher than 6 m. [S8]
- The ANARE 1968 survey cairn is on the summit. [S14]
- Ice velocity (own computation, [S15]):
  - The rock patch is about 1 km across, at 1 to 3 m/yr.
  - Station pixel 2 m/yr; 62 m away reaches 2 m/yr or less.
  - Within 2 km the median is 13.6 m/yr.
  - Surrounding glacier ice reaches 10 to 57 m/yr; Amery shelf margin about 40 to 50 m/yr to the east.
- The AARI page says the surrounding nunataks are at 250 to 350 m, which does not match the 119 m summit. I could not reconcile this.
- Hazards: landfast ice 160 to 180 cm, usually breaking out late Jan to early Feb; spring and summer temperatures 0 to −25 °C, down to −30 °C at the season ends; clear weather only about 10 to 12 days a month. [S8]
- Wildlife: small groups of Adélie penguins and skuas, with food waste handling flagged in 2010. [S3][S6]

**Status and years**
- Opened 1 Jan 1987. Five continuous summers 1987 to 1991. Conserved 24 Mar 1991. Reopened 6 Feb 1994. Used in the 1994/95 summers. [S8]
- Geological and geophysical work from the 48th RAE (2003) through the 54th, then the 56th, 58th and 60th RAE. Russian Wikipedia gives these dates: conserved 13 Mar 2013; conserved again 14 Apr 2014; deconserved 8 Jan 2015; conservation begun 1 Mar 2015 (unverified, secondary). [S23]
- The 60th RAE (Nov 2014 to Apr 2015) lists Druzhnaya-4 among its seasonal field sites. [RPR-20 text via S10]
- English Wikipedia: closed 19 Feb 2015 (unverified).
- COMNAP 2024 says "Seasonal, Open". AARI 70th and 71st RAE announcements list it as a seasonal base. On 15 Jan 2025, "unscheduled technical maintenance of the automatic weather station Druzhnaya-4" was done. [S1][S10]
- I found no source confirming people occupied the base after about 2015. The evidence points to a mothballed base with an automatic weather station. (Inference.)
- 2022: environmental monitoring covered it (67th RAE summary). [S10]
- Operating period per COMNAP 2017: October to March. [S3]

**Capacity**
- COMNAP 2017: 50 beds, no showers or laundry, 220 V, 78 kW diesel station, 120 t oil tank. [S3]
- Australian 2010: 16 small wooden structures; 8 expeditioners present plus 12 at outlying camps; some huts removed at season close and returned later. [S6]

**Infrastructure**
- Temporary panel and wooden huts; core huts are generator, kitchen/mess and communications. [S3][S6]
- Diesel generator with fuel in 200 L drums. Empty drums accumulated in a gully; a 2010 project was digging them out. Sources say 400 drums were pressed and packed for removal in 4 containers (unverified, search summary). [S6]
- Human wastes and grey water discharged untreated to the sea. [S6]
- Satellite phone and VHF. [S3]
- Automatic meteorological and geodetic stations. [S3]

**Access**
- COMNAP 2017: ship (2 visits a year) and helicopter; "airstrips 0; helipad No". [S3]
- The geophysics literature says aerogeophysics from the 1980s used Il-14 and An-2 aircraft "based at the ice airfields of field bases Soyuz, Druzhnaya-4 and Progress". [S19]
- 2010: ship plus helicopter from Sandefjord Bay, and from Progress II (about 100 km away). [S6]

**Other facilities within about 25 km**
- None found.
- Nearest per COMNAP: Bharati at 104 km, Law Base at 112 km, Zhongshan at 112 km, Progress at 112 km (own computation). [S1]
- Soyuz is 208 km away (own computation). [S1]
- The Larsemann Hills are ASMA 6, about 100 km away. [S6]
- Druzhnaya III (inventory row): English Wikipedia lists it near Cape Norvegia, 71°06'S 10°49'W, est. 1987, closed 1991 (unverified, a different place).

**Stated purpose**
- Logistics hub for seasonal geological and geophysical studies in Mac. Robertson and Princess Elizabeth Lands, the Prince Charles Mountains, and the Ingrid Christensen Coast oases. [S3]
- Soviet era: supply for Soyuz and aid in building Progress. [S8]

**Other notes**
- Inspected by Australia 13 Jan 2010; the US inspected it in 1976/77. [S6]
- The 2010 inspectors judged operation appropriate to its scale.

**Revival realism (evidence only)**
- Already periodically deconserved (1994, 2015).
- Huts are seasonal and relocatable.
- Infrastructure is small and temporary.
- No runway, no helipad, ship and helicopter only.

---

## 4. SOYUZ (Russia, context only)

**Verified coordinates**
- Inventory: -70.5766, 68.7949. COMNAP 2024: -70.576577, 68.794937, 336 m MSL, seasonal, "Temporarily Closed", 1982, peak 30. [S1]
- Second sources:
  - AARI (Wayback 2016): 70°35'S 68°47'E, 336 m, "eastern shore of Lake Beaver", 260 km from the Prydz Bay coast. These are 1-minute coordinates, so accurate to about ±1 km. [S9]
  - Australian 2010: 70°35'S 68°47'E, "exposed low rock ridge of Jetty Peninsula... eastern shore of the freshwater Beaver Lake". [S6]
  - Wikipedia: 70°34′36″S 68°47′30″E, 360 m (lead only).
- Elevation conflict. 336 m (AARI, COMNAP) vs REMA-derived about 35 m at the inventory pixel (own computation). A coarse DEM grid shows the lake margin at about 20 to 35 m and the Jetty Peninsula ridge at 220 to 310 m about 2 to 4 km east (approximate). The 336 m would match a ridge position, not the inventory coordinate. I could not resolve which is right. [S16]

**Surface and stability. Verdict: rock-qualifies. Confidence: moderate, because the position is uncertain.**
- The base lies on ice-free "Jetty Oasis" at "the slopes of the Jetty oasis". Photo captions place it beside Stagnant Glacier and moraine deposits. [S9]
- The Jetty oasis geology is shield rock, with dykes and pipes of alkaline-ultramafic rock, and a long moraine to the north-west. [S14, via Mindat quote in a search summary, unverified]
- Beaver Lake is a lake of smooth ice, 11.3 by 8 km, enclosed by Flagstone Bench and Jetty Peninsula, at the south end of a stagnant glacier. The Jetty Peninsula runs about 48 km north into the Amery Ice Shelf. [S14]
- Ice velocity (own computation, [S15]):
  - Station pixel 2.2 m/yr.
  - Within 500 m: median 1.0 m/yr, maximum 3.2 m/yr.
  - Within 2 km: median 2.0 m/yr, maximum 12 m/yr.
  - Within 3 km: median 3.6 m/yr.
  - About 65 % of the 12 km window is at 5 m/yr or less.
  - Fast ice of about 70 m/yr is only to the north-west edge.
- Climate and hazards (AARI): [S9]
  - Warmest month (January) mean −3.1 °C; extremes from +3.5 °C (Jan) to −23 °C (Mar).
  - Winds 5 to 9 m/s, up to 20 to 25 m/s, gusts to 30 m/s.
  - December and January are clearest.

**Status and years**
- Opened 3 Dec 1982 (28th Soviet Antarctic Expedition). Closed 28 Feb 1989. [S9]
- "Closed 2007" in the inventory is not supported by AARI. Secondary sources only say plans to resume work were considered from 2007 after some reconditioning in 2006/07, "but these plans were not carried out" (Russian Wikipedia) (unverified). [S23]
- COMNAP 2024: "Temporarily Closed", seasonal. [S1]
- 18 Jan 2010 Australian inspection: unoccupied, "no evidence of use in recent years". [S6]
- No primary source found on any use after 2010.

**Capacity**
- Main staff in 1987: 33 (Russian Wikipedia, unverified). COMNAP peak 30. [S1]

**Infrastructure** (2010) [S6]
- About 12 plywood huts in a line along the ridge.
- Weather damage, snow and ice inside, delaminating plywood, collapsed elements, broken windows, failed door seals.
- Unsecured empty drums and open-top waste containers; localized fuel or lubricant spills; piles of obsolete equipment; open drums with partly burned or oily waste.
- Inspectors called this "a high environmental risk" to the peninsula and to Beaver Lake, with waste "not recoverable".

**Access**
- Soviet era: supplied from Druzhnaya IV. [S8]
- Aircraft: aerogeophysics with Il-14 and An-2 aircraft was based on the ice airfields of Soyuz, Druzhnaya-4 and Progress. [S19]
- The Annals of Glaciology summary calls Soyuz a "base for aircraft for future airborne geophysics". [S19]
- Beaver Lake was used as a landing area by ANARE Beaver aircraft from 1957. [S14]
- I found no runway dimensions or surface type for Soyuz.

**Other facilities within about 25 km**
- Australia's Beaver Lake field site (70°47'S 68°17'E, established 1995, supports Northern Prince Charles Mountains and Amery Ice Shelf operations). It is about 30 km away (own computation). [S14] This is slightly outside 25 km.
- Nothing else in COMNAP; nearest listed is Druzhnaya IV at 208 km (own computation). [S1]

**Stated purpose**
- Summer geological and geophysical work in the Prince Charles Mountains. Irregular meteorological observations mainly for aviation. [S9]
- Lake studies at Lake Ledovoe, about 2 km east (29th and 30th SAE photographs). [S9]

**Other notes**
- Inspected 18 Jan 2010, its first inspection. [S6]
- No protected area found at the site (not verified against the ATS database).
- Not mentioned in the 2017 COMNAP Russia catalogue. [S3]

**Revival realism (evidence only)**
- 2010 inspectors saw weather-related damage to most huts, a "high risk" of debris irretrievably entering the environment, and "a substantial loss of utility as a seasonal station". They recommended securing or removing the structures and remediating the site. [S6]
- Russian planning documents I found stress Russkaya, not Soyuz (the 2030 strategy lists "creating a year-round station on the basis of Russkaya", a search summary, unverified). [S10]
- No source on 2007 reconditioning outcome.

---

## 5. SARIE MARAIS (South Africa, context only)

**Verified coordinates**
- Inventory: -72.0309, -2.8074. Not in the COMNAP Nov 2024 CSV (a closed station) and not in the SCAR gazetteer as "Sarie Marais". [S1][S14]
- Second sources:
  - World Antarctic Postal (WAP) page: 72°02'00"S 02°48'00"W, 1,047 m (a hobbyist radio-card page, low authority). [S21]
  - Wikipedia "Grunehogna Peaks" article: 72°01'35"S 2°48'18"W (lead only).
  - Differences from the inventory are under 0.5 km (own computation).
- SCAR gazetteer: Grunehogna Peaks at -72.05, -2.7833 (2.3 km from the inventory point). Norwegian "Grunehogna" -72.0333, -2.75, altitude 1,390 in the gazetteer (units not stated, presumed metres). [S14]
- Elevation: 1,047 m (WAP). REMA about 1,213 m at the inventory pixel. The 1 km box runs 1,025 to 1,300 m, so the site may be on the lower flank (own computation).
- "Fuchs Dome" is in the Shackleton Range, about 1,142 km away (own computation). [S14]

**Surface and stability. Verdict: unclear, leaning rock-or-nunatak; stability is not a concern. Confidence: low to moderate.**
- Geology: Grunehogna Peaks are in the Ahlmannryggen, on exposed Mesoproterozoic Ritscherflya Supergroup sediments (about 2,000 m thick, with sills). Magnetotelluric work places the Archaean Grunehogna craton beneath. [S14][search summary of papers, unverified]
- The base was called "Grunehogna Mountain Base" in other sources. [S21]
- Ice velocity (own computation, [S15]):
  - Inventory pixel 6.4 m/yr.
  - Median 5.0 m/yr within 2 km.
  - The whole 6 km box is under 12 m/yr, and 96 % is under 10 m/yr.
  - Nearest pixel at 3 m/yr or less is 620 m away; at 5 m/yr or less is 236 m away. The Wikipedia-listed coordinate gives 430 m and 27 m.
  - This cannot tell rock from slow ice.
- Not found: ice thickness, snow accumulation or burial rate.
- The only hint on burial: Cooper (2006) says structures at decommissioned DML bases "that have not become buried below the ice surface" were recycled, with Sarie Marais named as an earlier example. It does not say Sarie Marais was buried. [S20]

**Status and years**
- Erected 1982/83 for geological, geophysical and surveying programs. Decommissioned 2001/02. (Wikipedia, citing Cooper 1991 and an ATS 2003/04 exchange; unverified, I could not open either.) [S17]
- Cooper (2006) confirms decommissioning in line with the Protocol, with structures recycled to South Africa. [S20]
- Radio operation from the site documented on 14 Jan 1992. [S21]
- Wikipedia (search summary): in 1971 mechanical problems stopped a team reaching Borga Base, so a prefabricated hut was set up at Grunehogna; SANAE III supplied the camp about 200 km away (unverified).

**Capacity**
- Not found.

**Infrastructure**
- Not found beyond "summer base used in support of geological parties". [S21]

**Access**
- Overland from SANAE III by traverse (200 km, unverified). Today, DROMLAN flights land at Troll airfield, 184 km away (own computation). [S1][S20]

**Other facilities within about 25 km**
- None found.
- SANAE IV (Vesleskarvet) is 40 km away (own computation). [S1] It is 856 m, about 80 km from the continent's edge and 170 km from the ice-shelf edge. [S17: nmdb]
- Troll 184 km; a COMNAP-listed "SANAP Summer Station" (est. 2010) 248 km away, identity unverified. [S1]

**Stated purpose**
- Summer base for South African geology, geophysics and surveying in western Dronning Maud Land.

**Other notes**
- The WAP "250 km inland from SANAE" figure conflicts with the geometry (see Contradictions).
- Cooper suggests Robertskollen as ASPA-worthy; South Africa had proposed no ASPA or ASMA by 2006. No protected area found at Grunehogna. [S20]

**Revival realism (evidence only)**
- Decommissioned and recycled by South Africa as policy (2006). [S20]
- A 6 km window of slow ice (under 12 m/yr), with 40 km to SANAE IV and 184 km to a wheeled-aircraft runway at Troll.
- I found no information on its current condition, so I cannot say what remains.

---

## Contradictions between sources

1. Molodezhnaya to Mount Vechernyaya distance:
   - 13.2 km (COMNAP coordinates, own computation).
   - 13.3 km (CEE coordinates, own computation).
   - 18 km (Russian encyclopedia summary).
   - 20 km (CEE; Australian 2020 §7.2).
   - 22 km (Australian 2020 §6.2).
   - 25 km (belpolus.by; belta).
   - 28 km (Wikipedia).
   The inventory's "about 13 km" matches the coordinates but not the prose in the primary sources. Route length may differ from great-circle distance. Unresolved.
2. Molodezhnaya closure: Australian 2020 and Wikipedia say 1990 closure. Rosgidromet says mothballed 1999. A search summary says it was conserved in 1990, then reactivated, with the last wintering ending Jul 1999. Reading: 1990 was likely a partial, later-reversed conservation (inference).
3. Molodezhnaya runway: 2,540 × 42 m (S7); 2,560 × 42 m (S3); CEE: landing strip 2,790 × 100 m, aerodrome built 1979, first Il-18D landing Feb 1980; WP15: built 1981. Location: 10 km east (S7); 12 km ESE (S3); about 22 km, at Vechernyaya (S5); AT15 coordinates 46°08'E (Wikipedia); a skiway 7 km on the plateau (S5). They may be different strips (old compacted-snow runway vs current skiway), which I could not confirm.
4. Mount Vechernyaya establishment and capacity: 2006 (COMNAP) vs 2015 (station); 7 beds (S2), 8 (S5), 12 peak (S1), 15 (belpolus 2023); wintering planned for Feb 2021 (S5) vs still seasonal in 2024 (S18).
5. Druzhnaya IV:
   - Longitude 72°42' (AARI) vs 73°42' (all others).
   - AARI says closed 18 Apr 1995; Russian Wikipedia gives later seasons through 2015; English Wikipedia says closed 19 Feb 2015; COMNAP says open seasonal; AARI 2024 to 2025 lists it seasonal.
   - COMNAP says "airstrips 0"; the PMGRE literature says ice airfields. Different decades are possible.
   - Elevation 20 m, 3 m, 119 m (summit).
6. Soyuz:
   - Closed 1989 (AARI) vs 2007 (inventory, English Wikipedia).
   - Elevation 336 m vs REMA about 35 m at the inventory point.
7. Sarie Marais:
   - "250 km inland from SANAE" (WAP/NZ) vs 40 km to SANAE IV and 192 km to the SANAE III gazetteer point (own computation). The 250 km probably means from the coast (inference).
   - 1,047 m (WAP) vs REMA about 1,213 m at the point.
   - The briefing's "Fuchs Dome area" is wrong.
8. Hayes glacier speed: CEE says 900 to 1,400 m/yr; ITS_LIVE shows 100 to 220 m/yr within 3 km of Mount Vechernyaya. Not the same locations. Not reconciled.

---

## Source table (accessed 2026-10-04 unless noted)

- [S1] COMNAP Facilities Nov 2024 CSV: https://www.comnap.aq/s/Facilities_Nov2024.csv (redirects to static1.squarespace.com .../Facilities_Nov2024.csv). Downloaded and parsed in full.
- [S2] COMNAP Belarus station catalogue: https://www.comnap.aq/s/Belarus_Antarctic_Station_Catalogue_Aug2017-19.pdf
- [S3] COMNAP Russia station catalogue Aug 2017: https://static1.squarespace.com/static/61073506e9b0073c7eaaf464/t/615634aa53366351511d2b0b/1633039541354/Russia_Antarctic_Station_Catalogue_Aug2017.pdf
- [S4] Draft CEE, Belarusian station at Mount Vechernyaya (2013): https://www.env.go.jp/nature/nankyoku/kankyohogo/database/eikyou/hyouka_jisshi/pdf/11_mount_vechernyaya_en.pdf
- [S5] Australian Antarctic Treaty Inspections 2020 (ATCM 43): https://documents.ats.aq/ATCM43/att/ATCM43_att061_e.pdf
- [S6] Australian inspections Jan 2010 (ATCM 34 IP39): https://documents.ats.aq/ATCM34/IP/ATCM34_IP039_e.pdf
- [S7] Russia, ATCM 25 WP15 (2001), ice runway at Novolazarevskaya (describes the Molodezhnaya airfield): https://documents.ats.aq/ATCM25/wp/ATCM25_wp015_e.pdf
- [S8] AARI Druzhnaya page, Wayback snapshot 2016: http://web.archive.org/web/2016/http://www.aari.aq/stations/druznaya/druznaya_ru.html (live site refused the connection)
- [S9] AARI Soyuz page, Wayback snapshot 2016: http://web.archive.org/web/2016/http://www.aari.aq/stations/soyuz/soyuz_ru.html
- [S10] AARI / RAE: https://www.aari.ru/ ; 70th RAE start https://www.aari.ru/press-center/news/novosti-aari/startovala-70-ya-rossiyskaya-antarkticheskaya-ekspeditsiya ; 71st RAE https://www.aari.ru/press-center/news/novosti-aari/startovala-71-ya-rossiyskaya-antarkticheskaya-ekspeditsiya ; summary for 15 to 21 Jan 2025 https://www.aari.ru/press-center/news/rae/operativnaya-svodka-ob-osnovnykh-ekspeditsionnykh-sobytiyakh-i-operatsiyakh-rossiyskoy-antarkticheskoy-ekspeditsii-za-period-c-15-po-21-yanvarya-2025-g ; end of 67th RAE season https://www.aari.ru/press-center/news/news-archive/novosti-aari-arh/zavershilsya-sezonnyy-etap-67-y-rossiyskoy-antarkticheskoy-ekspeditsii ; 60th RAE results (RPR-20) https://mgmtmo.ru/edumat/polar/RPR-20.pdf
- [S11] Rosgidromet RAE summary 21 to 28 Apr 2022 (docx): https://www.meteorf.gov.ru/upload/iblock/336/280422РАЭ.docx
- [S12] Rosgidromet, Molodezhnaya: https://www.meteorf.gov.ru/press/200ant/21208/
- [S13] TASS "Russia Antarctic expedition ends Molodezhnaya base mothballing" (year not shown in the text I saw; contents match March 2013): https://tass.com/russia/691412
- [S14] SCAR Composite Gazetteer, queried through the placenames.aq API (https://placenames.aq/api/place_names) and AADC pages: Landing Bluff https://data.aad.gov.au/aadc/gaz/display_name.cfm?gaz_id=184 ; Beaver Lake gaz_id=122334 ; Jetty Peninsula gaz_id=127098. API results for Grunehogna, Fuchs Dome, Druzhnaya 4, Molodezhnaya.
- [S15] ITS_LIVE v2 datacubes (S3: its-live-data/datacubes/v2-updated-october2024), own computation.
- [S16] REMA v2.0 32 m mosaic (https://pgc-opendata-dems.s3.us-west-2.amazonaws.com/rema/mosaics/v2.0/32m_dem_tiles.vrt), own computation with EGM96 shift.
- [S17] Wikipedia, used for leads only: Molodyozhnaya Station (Antarctica); Vechernyaya Base; Druzhnaya Station; Soyuz Station; Landing Bluff; Grunehogna Peaks; SANAE; Borga Base; Research stations in Queen Maud Land; Antarctic Specially Protected Area.
- [S18] Belarus: https://belpolus.by/belorusskaya-antarkticheskaya-stantsiya/ ; https://belta.by/society/view/dlja-kazhdogo-ona-otkryvaetsja-po-svoemu-chto-izuchajut-v-antarktide-belorusskie-uchenye-625862-2024/ ; NASB 15th BAE start https://nasb.gov.by/rus/news/12417/ (search summary only)
- [S19] PMGRE: http://www.pmge.ru/index.php?id=663&lang=RUS ; Annals of Glaciology, "Fifty-five years of Russian radio-echo sounding" (Cambridge, summary only)
- [S20] Cooper (2006), "Antarctica and Islands" background paper for South Africa Environment Outlook, via https://web.archive.org/web/20151210063827/http://soer.deat.gov.za/dm_documents/Antarctica_and_Islands_-_Background_Paper_1DXK5.pdf
- [S21] WAP Online: https://www.waponline.it/grunehogna-mountain-base-and-sarie-marais-field-base-two-names-for-the-same-site-wap-zaf-04/
- [S22] Mining University 70th RAE paper: https://www.rudmet.net/journal/2441/article/39970/ ; https://forpost-sz.ru/en/a/2025-04-20/polar-explorers-mining-university-presented-results-70th-russian-antarctic-expedition
- [S23] Russian Wikipedia (lead only): Дружная-4; Союз (антарктическая станция).
- Other pages opened: AAD field sites https://www.antarctica.gov.au/antarctic-operations/stations-and-field-locations/field-sites/ ; ANU photo page http://rses.anu.edu.au/~rich/druzhruspics.htm (Stanaway, 15 Feb 2002: huts, banya, cross, view toward Sansom Island and Amery shelf edge).

---

## Search log (exact strings) and dead ends

Web searches run:
1. Molodezhnaya Station Antarctica current status seasonal Russian Antarctic Expedition airfield
2. Молодёжная станция Антарктида аэродром сезонная работа 2024 РАЭ
3. Belarus Antarctic station "Mountain Vechernyaya" Enderby Land Belarusian Antarctic Expedition
4. аэродром Молодёжная Ил-76 приземлился Антарктида 2023 2024 РАЭ ледовый аэродром Молодёжная принял
5. Молодёжная полевая база 70-я 71-я РАЭ сезонная зимовка нет, численность, Гора Вечерняя Беларусь
6. Antarctic Treaty inspection report Molodezhnaya Mount Vechernyaya Belarus station inspection 2020 Article VII
7. Молодёжная Антарктида рельеф холмы Тала оазис станция расположена скальный грунт расстояние до Гора Вечерняя аэродром 12 км
8. Druzhnaya 4 Antarctic field base Prydz Bay 69°44′S 73°42′E Soviet station
9. Дружная-4 полевая база Антарктида Земля Принцессы Елизаветы аэродром ледник Эймери история
10. "Дружная-4" полевая база РАЭ 2023 OR 2024 OR 2025 сезонные работы вертолёт геолог
11. Druzhnaya-4 Russian seasonal base Landing Bluff 2024 Russian Antarctic Expedition field season geological Prince Charles Mountains helicopter
12. "Landing Bluff" Sandefjord Bay Prydz Bay nunatak SCAR Composite Gazetteer Antarctica placenames
13. Дружная-4 расконсервация 8 января 2015 полевая база 60-я РАЭ ПМГРЭ Земля Мак-Робертсона
14. Дружная-4 2013 законсервирована база Союз Прогресс 400 бочек контейнеры 59-я РАЭ экологические работы
15. "Дружная-4" Антарктида база консервация состояние 2019 2020 2021 2022 РАЭ сводка
16. Antarctic Treaty inspection "Druzhnaya" IV Landing Bluff seasonal Russian station observation report ATCM
17. Russian Antarctic Expedition seasonal field bases "Druzhnaya-4" "Molodezhnaya" winterover seasonal 2025 Progress Larsemann geological Rosnedra PMGRE
18. Australian Antarctic Treaty Inspections January 2010 report Syowa Druzhnaya IV Soyuz station ATCM XXXIV information paper
19. Soyuz Antarctic field base Beaver Lake Jetty Peninsula Russian 2006 2007 reopening plans AARI Prince Charles Mountains Soyuz runway aircraft
20. база Союз Антарктида 2007 расконсервация 52-я 53-я РАЭ Бивер озеро Джетти оазис Дружная-4 вертолёт Союз состояние
21. Союз (антарктическая станция) полевая база горы Принс-Чарльз полуостров Джетти озеро Бивер 1982 аэродром история закрыта
22. "Soyuz" abandoned Russian base Beaver Lake Prince Charles Mountains huts visited Australian Davis helicopter "Beaver Lake" Soyuz station condition
23. Soyuz station Antarctica Wikipedia "Soyuz Station" Beaver Lake closed 2007 COMNAP "Soyuz" Russia temporarily closed reason
24. "Союз" полевая база озеро Бивер самолёт Ан-2 Ли-2 посадочная площадка Принс-Чарльз Советская антарктическая экспедиция 28-я САЭ строительство базы
25. Soyuz base Prince Charles Mountains Soviet 1982 Il-14 Li-2 aircraft airstrip Beaver Lake ice runway airborne geophysics Lambert Glacier Soviet Antarctic Expedition 28th
26. Beaver Lake Jetty Oasis Amery Oasis Prince Charles Mountains antarctic specially protected area Beaver Lake ecosystem Stagnant Glacier moraine bedrock geology Jetty Peninsula
27. DROMLAN Molodezhnaya runway blue ice compacted snow 67°40' 46° airfield Russian Il-76 Novolazarevskaya Molodezhnaya skiway AT15
28. "Molodezhnaya" skiway DROMLAN Basler Kenn Borek refuel Larsemann Hills Novolazarevskaya intracontinental flight Molodezhnaya fuel
29. Белорусская антарктическая экспедиция Гора Вечерняя зимовка 2021 2022 2023 первая зимовка станция круглогодичная
30. 15-я Белорусская антарктическая экспедиция Гайдашов октябрь 2022 июнь 2023 первая зимовка осенне-зимний сезон станция Гора Вечерняя
31. Sarie Marais Antarctic base South Africa SANAE field base Fuchs Dome Dronning Maud Land history 1982
32. "Sarie Marais" Antarctica SANAE geology field camp Ahlmannryggen Grunehogna Borgmassivet hut South African National Antarctic Programme
33. Grunehogna Craton Ahlmannryggen bedrock Ritscherflya Supergroup nunatak Grunehogna Peaks geology exposed rock ice surface elevation
34. "Sarie Marais" summer station being raised Antarctic legacy Stellenbosch SANAE Grunehogna
35. South Africa Antarctic Treaty exchange of information 2003 Sarie Marais decommissioned removed Grunehogna "Sarie Marais" ATCM
36. "Sarie Marais" Grunehogna South Africa Antarctic "Cooper" 1991 South African Journal of Antarctic Research summer base geological field season Kirwanveggen Ahlmannryggen
37. "Grunehogna Mountain Base" 250km inland from SANAE Antarctica New Zealand Heritage Trust
38. SANAE 1982 1983 Grunehogna base erected geologists Ahlmannryggen Borgmassivet "Sarie Marais" tractor train SANAE III Fimbul ice shelf South African Antarctic geology 1980s field camp
39. "Exchange of Information in Accordance with Article VII (5)" South African Activities 2003/2004 Sarie Marais Grunehogna ats.aq
40. ats.aq South Africa annual information exchange Article VII(5) 2003-2004 SANAE IV Marion "Sarie Marais" summer station decommissioned 2001/2002
41. decommissioning "Sarie Marais" Antarctica hut removed SANAE 2001 2002 field base South African Antarctic Programme environmental report DEAT
42. SANAP summer station 70°39'S 8°14'W South Africa Dronning Maud Land seasonal camp 2010 Antarctic "summer station" SANAE blue ice
43. Thala Hills Enderby Land Antarctic Specially Protected Area OR "Historic Site" Molodezhnaya oasis protected area ATS list ASPA near Syowa Molodezhnaya
44. Молодёжная станция Антарктида 2025 расконсервация OR реконструкция OR очистка полевая база Молодёжная 70-я РАЭ Гора Вечерняя Росгидромет
45. Russian Antarctic Expedition 70th 71st Molodezhnaya field base season 2024-2025 helicopter Akademik Fedorov Molodezhnaya Belarus Gora Vechernyaya cargo ice-class
46. Молодёжная Антарктида паводок прорыв озера ледяная плотина топливный резервуар разрушен база затопление
47. Thala Hills Enderby Land lakes glacial lake outburst flood Molodyozhnaya station permafrost lake level rise Lake Glubokoye Lagernoye ice dam
48. Россия Антарктика стратегия 2030 полевые базы Русская Союз Дружная-4 расконсервация планы Роснедра ПМГРЭ Земля Мак-Робертсона горы Принс-Чарльз новая база
49. aari.ru оперативная сводка РАЭ полевая база Молодёжная сезонный отряд паводок Гора Вечерняя 2025 вертолёт Дружная-4
50. "Дружная-4" РАЭ 64-я OR 65-я OR 66-я OR 67-я OR 68-я OR 69-я полевая база сезонный состав Российские полярные исследования
51. "Druzhnaya-4" OR "Druzhnaya IV" Antarctic 2018 OR 2019 OR 2020 OR 2021 OR 2022 OR 2023 Russian field base visited conserved seasonal geophysical aircraft Prydz Bay
52. "Молодёжная" "паводкового подтопления" 2025 Российская антарктическая экспедиция оперативная сводка января 2025
53. Молодёжная станция последняя зимовка 44-я РАЭ 1998 1999 законсервирована 9 июля 1999 зимовка прекращена 1991 сокращение

Dead ends and where each died:
- **aari.aq live pages** (Druzhnaya): connection refused. I used Wayback instead (died at the source, solved by the archive). The Wayback snapshot of aari.aq/stations/molod/ does not exist (died at the source).
- **raexp.ru Druzhnaya page**: certificate mismatch; with certificate checks off it returned only the generic RAE page, not the station page (died at the source).
- **rosnedra.gov.ru/article/7319.html** (PMGRE 59th RAE results, cited in search results): HTTP 404.
- **Stellenbosch "A history of South African involvement in Antarctica" PDF**: 504 on download and WebFetch timeout. Not read.
- **Cooper (1991) SAJAR 21(2): 7** and the **ATS 2003/04 South African Article VII(5) exchange**: both cited by Wikipedia for Sarie Marais; searches 35, 36, 39, 40 and 41 never surfaced them (died at the query, or the sources are not indexed). So 1982/83 to 2001/02 rests on Wikipedia plus Cooper 2006.
- **Sarie Marais capacity, buildings, current condition**: nothing found. It is absent from COMNAP Nov 2024 and the SCAR gazetteer.
- **Soyuz runway dimensions or surface type; Soyuz use after 2010; Soyuz primary source for "2007"**: nothing found (died at the sources).
- **Bedmap3 and BedMachine ice thickness**: BAS server returned 503; NSIDC needs login (not attempted). No bedrock-depth numbers other than the CEE (ice sheet 10 to 20 m thick at the coast, 500 m at 10 km inland).
- **Second ice-velocity product** (MEaSUREs/Mouginot): not run. Velocities rest on ITS_LIVE plus CEE/Kotlyakov literature.
- **ASPA/ASMA/HSM check**: no official ATS protected-area listing could be queried (the Wikipedia list URL returned 404 and the other page was incomplete). Only the CEE confirms no protected area, for Mount Vechernyaya. For the other four, "none found" is not a verified absence.
- **Mindat Jetty Oasis page**: HTTP 403. Geology text comes from a search-engine summary (unverified).
- **TASS article year**: not displayed in the text I retrieved; inferred from content (15 + 3 people, matches 2013).
- **Molodezhnaya 1990 vs 1999**: not resolved by any one primary source (see Contradictions).
- **Mount Vechernyaya wintering**: no confirming source found for actual wintering.
