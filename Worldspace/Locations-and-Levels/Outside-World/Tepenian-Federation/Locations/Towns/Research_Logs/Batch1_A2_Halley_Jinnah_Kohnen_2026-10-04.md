<!-- Log written 2026-10-04: the research agent's full report, extracted verbatim from its transcript (not re-typed). Findings filled into ../Towns_Priority_Batch_1_Reference_2026-10-04.md (#13 Halley VI, #14 Jinnah, #28 Kohnen). Operators are context only. Ice velocities and Bedmap3 values are the agent's own point samples of ITS_LIVE (annual composites) and Bedmap3 (500 m grid); [search summary only] = unverified. -->

# Real-world research report: Halley VI, Jinnah (Pakistan), Kohnen

Access date for every source below is **2026-10-04** unless a different date is shown. Operating nation or program is context only. Wikipedia was used only to locate leads, and each such use is flagged. "[search summary only]" marks facts I saw only in a WebSearch result summary and did not verify at the source.

**Bottom line for the project's test ("ice not moving fast enough to force a move; ideally bedrock below")**

| Station | Verdict | Confidence |
|---|---|---|
| Halley VI | **ice-fails.** Floating shelf moving about 1,400 m/yr. It has already been moved once (2016-17), and no one has wintered there since 2017. About 400 m of seawater lies below. | High |
| Jinnah | **ice-fails at the only coordinates ever published.** The point is on a floating ice shelf moving about 245 m/yr. The station's current existence and condition are unverified and there is no evidence of use after 1993. | Moderate to high on the ice classification; very low on what exists today |
| Kohnen | **Passes the speed test.** Surface velocity is about 0.74-0.76 m/yr by GPS. Grounded bedrock lies about 2.76-2.78 km below. There is no surface rock; the nearest rock is about 181 km away. | High on speed; moderate to high on thickness |

---

## 1. HALLEY VI (UK, British Antarctic Survey) — operator is context only

### Verified coordinates
- COMNAP Nov 2024 CSV: -75.571111, -25.473889 (75°34.2667'S, 25°28.4333'W), elevation 37 m, WGS84 [S1].
- COMNAP 2017 Catalogue: 75°34'24.56"S, 25°28'1.05"W, altitude 37 m [S2].
- BAS facility page (Internet Archive capture of 2026-10-02): Lat -75.56821, Long -25.50852 [S3].
- The three points differ by about 0.3-1.3 km (my calculation). This is consistent with a station that drifts west with the ice at about 1.4 km/yr. Treat any published point as dated and nominal.
- Hodgson et al. 2019 (The Cryosphere) gives the current site "Halley VIa" at 75°34'S 25°28'W and the original Halley VI site at 75°36'S 26°12'W [S13]. These are degree-minute rounded; I get about 20.6 km between them, while BAS says 23 km [S5, S6, S7]. The difference is rounding.
- The UK gazetteer (placenames.aq, GBR record "Halley (1988)") gives historic positions [S16]:
  - Halley I, 1956: 75°31'S 26°36'W
  - Halley II, 1967: 75°31'S 26°39'W
  - Halley III, 1973: 75°31'S 26°43'W
  - Halley IV, 1983: 75°36'S 26°40'W
  - These are positions when built. The 1956 station was removed by calving at the end of the 1978-79 summer, and the others were buried or abandoned.

### Surface and stability
**Verdict: ice-fails. Confidence high.**

- **Surface type:** floating Brunt Ice Shelf.
  - Bedmap3 mask value 3 (floating ice shelf) in every cell of a 6 km box around the station [S18].
  - Bedmap3 gives about 120-125 m ice thickness, surface 20 m, and seabed -507 m. This implies roughly 400 m of seawater below. The ice base is about -100 m, so the water column is about 407 m (my arithmetic on a 500 m grid cell).
  - BAS says "130 metre-thick" [S3, S4]. BAS news releases say 150 m [S6, S8, S10]. King et al. 2018 describe 150 m sections with about 250 m meteoric-ice flow bands [search summary only].
  - The seabed under the Brunt Basin is 400-800 m deep [S13].
  - The nearest grounded ice is 24.6 km away (Bedmap3 grounding line). The nearest rock is more than 250 km away [S18].
- **Velocity:**
  - GPS at the station (site ZZ6A): about 450 m/yr in 2013 rising to about 900 m/yr by January 2023. Rate of acceleration was a constant 50 m/yr² before the A-81 calving [S11].
  - After A-81 (22 Jan 2023) and a small second calving (end of June 2023), acceleration jumped to about 500 m/yr². Spring-tide velocity at the station reached **1,500 m/yr in Aug 2023**. The paper calls this "almost double the maximum velocities observed over the previous 60 years" [S11].
  - BAS (Sept 2023): about 4 m/day, versus 1-2.5 m/day before [S9]. 1,400 m/yr is 3.8 m/day.
  - ITS_LIVE annual composite (v2-updated-september2025), grid cell at the current station coordinates, in m/yr [S17]:

    | Year | 2013 | 2015 | 2017 | 2019 | 2021 | 2022 | 2023 | 2024 | 2025 |
    |---|---|---|---|---|---|---|---|---|---|
    | Velocity | 487 | 491 | 572 | 661 | 802 | 855 | 1,001 | **1,417** | **1,400** |
    | Error | ±29 | ±29 | ±26 | ±50 | ±74 | ±18 | ±18 | ±12 | ±12 |

    - The 2025 value may be a partial-year composite. This is a fixed-point (Eulerian) sample, not a track of the moving station.
  - **Trend:** BAS (21 May 2024) says the speed at the station "has stabilised since the previous calving last year" [S10]. The ITS_LIVE values for 2024 and 2025 agree: a plateau at about 1,400 m/yr, roughly three times the 2013 speed. BAS pages still print stale values ("approximately 700 metres per year" [S3, S4]; "around 400 metres" in the June 2026 long read [S14]).
- **Recent calvings:**
  - A-74: Feb 2021, 1,270 km² [S9 related]
  - A-81: 22 Jan 2023, about 1,500 km² [S11]. BAS says the station is 20 km from the new ice front [S9]. Bedmap3 gives 20.6 km to the coast/ice-front boundary [S18].
  - A-83: 20 May 2024, 380 km² [S10]
  - A-83 calved from Halloween Crack and left the shelf at "its smallest extent since monitoring began" [S10].
- **Cause of the acceleration:** loss of buttressing at the McDonald Ice Rumples pinning point [S11]. The shelf may re-ground on the three grounded icebergs downstream. If it keeps its Aug 2023 speed it would reach them around the end of 2024 [S11].
- **Rifts:**
  - Chasm 1 was dormant for at least 35 years and began moving in 2012 [S8].
  - Halloween Crack was found 31 Oct 2016, about 17 km north of the station [S6, S8, S12].
  - A new rift-type feature is propagating east near the grounding line after A-81 [S11].
  - The shelf is composed of cemented icebergs with thin interstitial regions. At high speed, thinning near the grounding line makes it more vulnerable [S11].
- **Test result:** fails on speed and on bedrock. The site is on a floating shelf with 400 m of water under it. The shelf already forced one relocation, and BAS still cannot be sure of the next calving.

### Status and years
- COMNAP Nov 2024: Type Station, Seasonality **Seasonal**, Status **Open**, Year Established 1956 [S1].
- BAS (2026-10-02 capture): "Occupied 15 Jan 1956 to present"; summer-only; runs autonomously through winter [S3].
- Opening date variants: BAS long read says "6 January 1956" [S14]; BAS facility page says 15 Jan [S3]; gazetteer says 16 Jan [S16].
- **Station generations** (BAS 70-year long read [S14], gazetteer [S16], Wikipedia dates as lead [S24]):
  - Halley I: 1956-1967 (wooden huts, 14 m below surface by abandonment)
  - Halley II: 1967-1973
  - Halley III: 1973-1983
  - Halley IV: 1983-1991
  - Halley V: about 1990/91-2011/12, on stilts; demolished late 2012 (Wikipedia date, lead only)
  - Halley VI: construction 2007-2012, first operational data 28 Feb 2012, officially opened 5 Feb 2013 [S24 lead; BAS says "Operational since 2012" [S3, S4]]
- **Relocation:**
  - BAS EIA "Halley Relocation Project", 2016/17 and 2017/18, decision "Proceed - minor or transitory impact" [S19, item 1796].
  - Site survey in 2015/16. In 2016/17 BAS spent 13 weeks towing all eight modules **23 km upstream** of Chasm 1 [S5, S7].
  - Seven of eight modules were at the new site by 16 Jan 2017 [S6]. Relocation was declared a success on 2 Feb 2017 [S7].
  - Science instruments moved in 2017/18 [S5].
- **Winter closure:**
  - BAS decided on 16 Jan 2017 not to winter in 2017 because Halloween Crack made evacuation in winter unpredictable. 88 people were on station at the time, including 16 winterers [S6].
  - BAS: "This will remain the case for the foreseeable future" [S4]. The current page still says summer-only [S3].
  - Z-fids Oct 2025, quoting the station leader: "ongoing pause in manned winters" [S15].
  - I inferred the last overwintering was 2016. No source states that year directly.
- **Season dates:**
  - BAS: summer "late November to early February" [S3]. The 2024 press release says staff are deployed "between November to March" [S10].
  - 2023/24: 40-person plan; main group of 31 uplifted 2 Feb 2024; final 5 uplifted a day earlier [S9, S15].
  - 2025/26: open-up team deployed about 27 Oct 2025; summer team around mid-Nov 2025 [S15, Z-fids 58].
- **Plans to relocate again, replace, or return to winter ops:** none found.
  - Searches for "Halley VII" returned nothing (dead end at the sources). BAS's June 2026 long read describes future work as continued summer operation plus automation [S14].
  - BAS leaves winter return open only as "until the Brunt Ice Shelf stabilises" [S4], with no timeline.
  - RIFT-TIP (NERC, 1 Sept 2023 to 1 March 2027) works from Halley on rift fracture [BAS RIFT-TIP page via Internet Archive].

### Capacity
- BAS 2026: "Summer: Up to 52". The same page says "approximately 40 staff" in summer, and 16 "used to stay over winter" [S3]. COMNAP 2017: 52 beds, 52 peak summer, 13 winter (this was the pre-closure design figure), 52 conference-room capacity [S2].
- Z-fids says the open-up team is 5 people, or 8 in 2025 [S15].

### Infrastructure
- Eight modules on hydraulic legs and skis: one red central module and seven blue. Also the Drewry summer accommodation building, garage and workshop, cabooses, and the Clean Air Sector Lab [S3, S4, S24 lead].
- COMNAP 2017: 2,000 m² under roof, 200 m² laboratories, 800 m² logistics, 230 V, fossil-fuel power, hospital-type medical room (100 m²), satellite phone, internet, email, VHF [S2].
- **Power (current):**
  - Winter: microturbine generator, "up to 30kW", powering autonomous science cabooses [S3].
  - Second microturbine installed 2023/24 as standby [S15, Z-fids 54 and 55].
  - A microturbine broke down in winter 2023 and was fixed [Z-fids 57].
- **Fuel:** 500 m³ bunkered and 250 tonnes of waste removed in the 2023/24 ship relief; food stocks for 3 years [Z-fids 55].
- **Runway:** one snow skiway, 1,100 m x 50 m [S2].
- **Water:** not found in a primary source. COMNAP lists showers and laundry [S2].
- **State of the modules:**
  - 2023/24: infrastructure raised twice, including a "double raise and a realignment" of the modules [Z-fids 55].
  - Oct 2025: "around twice as much snow as at the end of last season's winter", so another double raise planned. The Drewry is being modernized (double rooms, UK fire-safety regulations) [Z-fids 58].
  - Z-fids is the Halley old-hands newsletter, which reproduces station-leader reports. It is secondary but first-hand.

### Access
- **Air (Twin Otter, Basler, or Dash-class via a DROMLAN chain):** Cape Town to Wolf's Fang runway, then to Halley via Neumayer, summer only [Z-fids 54, 58; search summary only for the Twin Otter route]. COMNAP: 20 flight visits a year [S2].
- **Sea:** ice-shelf relief only. The 2023/24 relief by MV Malik Arctica was "the first ship we've seen in 6 years" [Z-fids 55]. A second relief was planned for 2025/26 [Z-fids 58]. COMNAP lists 2 ship visits a year [S2].
- **Relief sites:** after A-81, five candidate relief sites 15-20 km from the station with shelf edge 12-25 m high [Z-fids 54]. The old N9 and "Creeks" access points are described in a 2016 blog by a journalist (secondary): N9 is cut off by Halloween Crack [Teller blog, S28]. **No coordinates found for "Creek 3" or "Creek 4"** (dead end at the sources).
- **Winter:** access is "extremely difficult" (darkness, extreme cold, frozen sea) [S6, S7].

### Other facilities within about 25 km
- No other nation's station is nearby. Real distances from the current station (my haversine calculation on the BAS point):
  - Original Halley VI site 6: about 19.5-20.6 km (BAS says 23 km).
  - Halley I-IV historical positions: 31-34 km (and they are gone or buried).
  - Coats field station (BAS, 1964-65, 77°54'S 24°08'W): about 262 km.
  - Belgrano II: 346 km.
  - Svea: 423 km. Aboa and Wasa: 458 km.
- Within the BAS site and area: a seven-sensor GPS network "Lifetime of Halley" [S3]. The older BAS project page says 15 GPS and ApRES radar on the shelf [S8]. Windy Bay emperor penguin colony is about 20 km from base [BAS 2011 blog via S4 page]. RIFT-TIP deep-field camps are about 60 km out [S14].

### Stated purpose
- Atmospheric science, space weather, ozone, glaciology. The ozone hole was found at Halley in 1985. WMO Global Atmosphere Watch station since 2013 [S3, S14].

### Other notes
- **Climate** [S3; S2; S13]:
  - BAS: winter below -20 °C, extreme low about -55 °C; 105 days of darkness; winds mostly from the east; surface snow lifted to visibility of a few meters.
  - COMNAP 2017: mean annual -20 °C; February -13; July -31.
  - Snow accumulation: BAS 1.2 m/yr; Hodgson 2019 gives 90 cm/yr mean for 1972-2017, range 48-149 cm [S13].
- **Hazards:** calving and rifts (above), burial, extreme cold, and wind. Wikipedia mentions a July 2014 power failure at -55 °C [lead only, unverified here].
- **Protected areas:** none found within 25 km. I could not check the ATS protected-areas database because it is JavaScript-rendered. The Halley Bay emperor colony is a documented Important Bird Area, and it largely failed to breed 2016-2018 [search summary only].
- **Other BAS facility numbers:** BAS 2026 lists "Staff Summer: Up to 52" and a coordinate that has drifted from COMNAP's.

### Revival realism
There is nothing to revive: the station is open and used every summer. What has been tried is a return to winter operations, and BAS has not committed to one. Evidence against it in the near term: velocity three times the 2013 level, three large calvings since 2021, and a station that is about 20 km behind a new, rifted ice front. Evidence for continued operation: ship relief resumed in 2023/24, a second microturbine was installed, and RIFT-TIP runs to 2027.

---

## 2. JINNAH ANTARCTIC STATION (Pakistan, National Institute of Oceanography) — operator is context only

### Verified coordinates
**No independent verification is possible. The location is unverified and the published coordinates cannot be reconciled with each other.**

- Wikipedia and Wikidata: 70.4°S 25.75°E (70°24'S 25°45'E), precision stated as 0.1° [S24 lead; S26]. Wikidata cites Wikipedia as its source, so it is not independent.
- The 1991 Ministry of Science and Technology text, as reproduced on a philatelic blog and in Haq's Musings: "located at 7024 S and 25 E ... Princess Rangnhild Coast", commissioned 25 Jan 1991 [S25a; S25b]. That is 70°24'S 25°00'E, 0.75° of longitude (about 28 km) west of Wikipedia's longitude. I do not know where Wikipedia's "45'" came from.
- Wikipedia also gives Jinnah II at 70°50'S 25°10'E (125 km north of the Iqbal weather observatory per Wikipedia) and the Iqbal Observatory at 71°27'36"S 25°17'24"E [S24 lead]. Wikipedia's "125 km south of the station" is wrong against its own coordinates: I get about 119 km.
- **Not in any primary register:**
  - COMNAP Nov 2024 CSV and the 2017 Catalogue: no Jinnah, no Pakistan row [S1, S2]. Pakistan is not a COMNAP member [COMNAP members page].
  - SCAR gazetteer (placenames.aq): zero hits for Jinnah, Iqbal or Pakistan across name, narrative and named-for fields.
  - ATS Reports by Party: Pakistan has no information-exchange entry [ATS, Reports by Party page].
  - ATS EIA database: no Pakistani entry in the IDs I scanned (0-3500).
  - Pakistan acceded to the Antarctic Treaty on **1 March 2012** [ATS Parties page]. It is a non-consultative party.

### Surface and stability
**Verdict: ice-fails at the published coordinates. Confidence: moderate to high on the surface classification, because two independent datasets agree and the result is the same at both candidate longitudes. The coordinate uncertainty (about ±11 km from the 0.1° precision, plus the 28 km longitude disagreement) is the main limit.**

- Bedmap3 (500 m grid) [S18]:

  | Point | Class | Ice thickness | Surface | Seabed |
  |---|---|---|---|---|
  | 70.4°S 25.75°E | floating ice shelf | 408 m | 57 m | -391 m |
  | 70°24'S 25°00'E | floating ice shelf | 264 m | 26 m | -334 m |
  | Jinnah II, 70.833°S 25.167°E | floating ice shelf | 415 m | 53 m | -382 m |
  | Iqbal, 71.46°S 25.29°E | **rock** | 0 | 885 m | not applicable |

- The mask values are 1 grounded ice, 2 transient grounded, 3 floating ice shelf, 4 rock (Bedmap3 paper) [S18].
- At 70.4°S 25.75°E the nearest grounded ice is 10 km away, the nearest rock is 118 km away, and the coastline is about 14.5 km away (my calculation on the Bedmap3 mask). The 70°24'S 25°E variant gives 13.8 km, 117.7 km and about 11.7 km.
- ITS_LIVE annual velocity at 70.4°S 25.75°E [S17]:

  | Year | 2013 | 2015 | 2017 | 2019 | 2021 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|---|
  | m/yr | 257 | 258 | 246 | 236 | 229 | 251 | 260 | 245 |

  - Errors are ±4-15 m/yr in 2017-2025. The ITS_LIVE floating-ice flag is also set. A point 1 km west shows 265-305 m/yr.
  - Jinnah II's point shows about 106 m/yr, and the Belgian Roi Baudouin base site shows about 66 m/yr, also floating. The Roi Baudouin cross-check fits: the Belgian base (1957-1968) was built on this ice shelf [S27].
- The wording "Sør Rondane Mountains" is loose. The mountains begin about 170-190 km south and the nearest rock to the Wikipedia point is 118 km away. The 1991 text says "Princess Ragnhild Coast".
- Implication (my arithmetic): a structure left on the surface in 1991 would have moved about 8-9 km seaward in 35 years at about 250 m/yr and been buried. No source says any Jinnah I building survives.
- Pakistan's own 1991 description is of prefab huts, igloos and tents (below), not a permanent structure.

### Status and years
- Landing 15 Jan 1991; station "commissioned" Friday 25 Jan 1991 [S25a]. The Pakistan Maritime Museum says 18 Jan 1991 [S25c]. The Wikidata inception date is 15 Jan 1991 [S26].
- First expedition: left Karachi 12 Dec 1990 on the chartered Swedish MV Columbialand, about 40 people from NIO, Pakistan Navy and Army; reconnaissance of "nearly 1000 miles" of coast [S25a; S25c].
- Iqbal Observatory (unmanned weather station): ISSRA says 18 Jan 1991 [S25d]; Wikipedia says 1992-93 [S24]. Jinnah II: ISSRA says 5 Jan 1992 [S25d]; Wikipedia says the 1992-93 expedition. Wikipedia and Gulf News both date these to "1991 and 1993".
- **No expedition since 1993:** Gulf News (25 Oct 2020), quoting the NIO Director General: "No independent expedition was sent by Pakistan after 1993 reportedly due to lack of funds" [S25e]. Pakistan's own SCAR national reports for 2007-08, 2008-09 and 2009-10 each say only "There has been no expedition to Antarctica" [S25f].
- NIO's website (Internet Archive captures 2001 and 2012) still says "Pakistan is maintaining two summer research stations and one weather observatory in the vicinity of SOR Rondane Mountain Range" and gives no coordinates, dates or condition [S25g]. This is stale boilerplate rather than a status report.
- ISSRA (Aug 2024): "Pakistan halted its operations as stations were no longer maintained" [S25d].
- Wikipedia lists the station as "Active" and claims a 2005 PAF airstrip, a 2001 Badr-B link and a 2010 approved expansion, all unsourced and contradicted by the sources above [S24 lead]. I treat those claims as unverified.
- Current state: not found. **Most likely defunct or lost, but no source says so directly.**

### Capacity
- 1991 station: three laboratory prefab huts, three prefab igloos "for accommodation of 9 persons", four tents, plus an unmanned weather station [S25a; S25b]. Nothing later.

### Infrastructure
- As above. Power, water, fuel, communications and runway: not found for the 1991 station. The 2005 "airstrip" is only in Wikipedia and is contradicted by the no-expedition evidence.

### Access
- 1991: by sea on MV Columbialand [S25a]. ISSRA says PAF aircraft and PNS Tariq and PNS Behr Paima supported the missions [S25d].
- Now: no Pakistani logistics. NIO's DG said in 2020 that joining multinational expeditions is more feasible than independent ones, and that independent missions are too expensive [S24; S25e].

### Other facilities within about 25 km
- None known. Real distances from the Wikipedia point (70.4°S 25.75°E), my calculation:
  - Roi Baudouin, Belgium's 1957-68 base (70.433°S 24.317°E): about 54 km.
  - Jinnah II (Wikipedia coordinates): 53 km.
  - Iqbal Observatory (Wikipedia coordinates, on rock): 119 km.
  - Asuka (Japan, temporarily closed): 139 km.
  - Princess Elisabeth: 193 km. Perseus blue-ice airstrip (71°25'42"S 23°33'57"E): about 139 km [search summary only for the Perseus coordinates].
  - Novolazarevskaya 515 km, Maitri 519 km, Troll 845 km.
  - The 70°24'S 25°00'E variant is about 26 km from the Roi Baudouin site and 182 km from Princess Elisabeth.
- Nothing sits within 25 km.

### Stated purpose
- Pakistan: multidisciplinary research (geology and geophysics, environment, oceanography, glaciology, weather) and a "permanent base" aspiration [S25a; S25g]. Politically: scientific presence and SCAR membership (associate member from 1992; ISSRA says 1989 [S25d]).

### Other notes
- Protected areas: none known near the site. The only Queen Maud Land ASPAs I found in a search summary are ASPA 142 (Svarthamaren) and ASPA 163 (Dakshin Gangotri), neither near. A western Sør Rondane ASPA proposal exists (search summary only).
- Climate and hazards: not documented by Pakistan. The ice-shelf setting implies calving, blowing snow and coastal katabatic winds, but I found no source specific to the site.

### Revival realism
Nothing found suggests a revival. Pakistan has not mounted an independent expedition in over 30 years, is not a COMNAP member, files no Antarctic Treaty information exchange, and has publicly said joining other nations' expeditions is more feasible. The site itself is on a moving floating shelf. A revival would have to be a new station at a new site, not the 1991 one.

---

## 3. KOHNEN STATION (Germany, Alfred Wegener Institute) — operator is context only

### Verified coordinates
- COMNAP Nov 2024 CSV: -75.001909, 0.066336 (75°0.1145'S, 0°3.9802'E), elevation 2,892 m, WGS84 [S1].
- Oerter et al. 2009 (AWI primary paper): station 75°00'06"S 0°04'04"E; the borehole at 75°00'09"S 0°04'06"E, 2,892 m (WGS84) on 10 Jan 2001 [S20]. Wesche et al. 2007 give the drill site as 75.00258°S 0.06848°E, 2,891.7 m [search summary only].
- ATS EIA: 75°00'00"S 0°04'00"E [S19, items 2602, 2721, 2836].
- Oerter prints the runway's end points with a typographic error: "74°0.037'S" should be 75°00.037'S [S20].

### Surface and stability
**Verdict: passes the speed test; grounded ice over bedrock about 2.76-2.78 km down. Confidence: high on speed, moderate to high on thickness.**

- Ice sheet, East Antarctic plateau. Bedmap3: mask 1 (grounded ice), ice thickness 2,760 m, surface 2,879 m, bed +119 m above sea level [S18]. AWI/COMNAP: ice thickness 2,782 ±10 m, "the bedrock is covered by 2782 m ice and snow" [S20; S2]. Subtracting gives bed about +110 m (my arithmetic).
- There is **no surface rock**. The nearest rock in the Bedmap3 mask is about 181 km away [S18].
- **Velocity (the key figure):**
  - GPS surface flow velocity at the drill site: **0.756 m/yr** toward 273.4° (Wesche et al. 2007, cited in Oerter 2009) [S20].
  - Wesche et al. 2007 abstract: annual mean velocity magnitude of 12 survey points "amounts to 0.74 m a⁻¹"; the site is "in the immediate vicinity of a transient and forking ice divide" [search summary only].
  - ITS_LIVE annual composite for the grid cell at the station gives 3.1 m/yr (2022), 3.3 (2023), 3.2 (2024), 2.5 (2025), with errors 0-1 m/yr; earlier years scatter 1.4-13.5 with errors up to 11 m/yr [S17]. **Contradiction:** ITS_LIVE feature tracking cannot resolve speeds this low and its error bars are probably underestimated. The GPS figure is the primary value; I treat 2-3 m/yr as an upper bound.
  - Either way the speed is nowhere near forcing a relocation.
- **Snow accumulation:** 64 ±0.5 kg m⁻² yr⁻¹ for the last 1,000 and 4,000 years (ice core B32); 65 from radar [S20]. At about 350-400 kg m⁻³ near-surface density that is about 0.16-0.18 m of new snow per year, or 1.6-1.8 m per decade (my arithmetic).
- **Snow burial of the station:** the station sits on a steel platform with 16 pillars. COMNAP 2017: "the platform has to be lifted up every second year; four technicians are needed to open the station" [S2]. AWI 2021/22: platform leveled and "the entire platform station was raised" [S22, BzPM 767]. AWI 2023/24: raising was "not necessary" and also "not possible due to the lack of a replacement hydraulic cylinder" [S22, BzPM 796].
- **Temperature:** mean annual -44.6 °C at 10 m depth (1997/98); winter to -70 °C; summer not warmer than -17 °C; midnight sun 31 Oct-12 Feb [S20]. COMNAP 2017 gives -42.2 °C mean annual, -32.2 °C February, -52.3 °C July, and 16.2 km/h mean wind [S2].

### Status and years
- COMNAP Nov 2024: Seasonal, **Temporarily Closed**, Year Established 2000, peak population 28 [S1]. The AWI paper says "put into operation on January 11, 2001" [S20]. Wikipedia and COMNAP's own 2017 catalogue say 2001 [S2].
- Built over two summers, 1999/2000 and 2000/2001. EPICA drilling ran four summer seasons from 2001/02 and ended **16 Jan 2006 at 2,774.15 m** [S20].
- **Seasons from the AWI "ANT-Land" expedition reports** (Berichte zur Polar- und Meeresforschung):

  | Season | Status | Source |
  |---|---|---|
  | 2018/19 | open: traverse and science (Kohnen-QK1 sampling); opening delayed by weather | BzPM 733 |
  | 2019/20 | "Kohnen Station was closed" | BzPM 745 |
  | 2020/21 | "Kohnen Station was closed" (COVID-limited season) | BzPM 758 |
  | 2021/22 | opened; traverse arrived about 3 Dec 2021; drinking-water pipe repaired; platform raised; trench roof braced; closed 24 Jan 2022 | BzPM 767 |
  | 2022/23 | "was not opened" | BzPM 784 |
  | 2023/24 | opened; traverse reached it 3 Dec 2023; 6-person science team from 19 Dec; "left winterised" 20 Jan 2024; trench being cleared and closed | BzPM 796 |
  | 2024/25 | "was not opened this summer season"; automatic weather station not serviced | BzPM 807 |
  | 2025/26 | **not found.** The report had not appeared in the AWI repository when I looked | gap |

  - Earlier traverses reached Kohnen in 2015/16 (per a 2026 PANGAEA dataset, search summary only), 2018/19, 2021/22 and 2023/24.
- **Why closed:** **no AWI document I found states a reason.** The reports just say "closed" or "not opened". The pattern since about 2018 is opening roughly every two to three years for technical work and a small science team. COVID explains 2020/21 only as context. Anything beyond that would be inference.
- **AWI planning:**
  - The AWI proposals page (accessed 2026-10-04) asks for projects at Neumayer for 2027/28 and at **Kohnen for 2028/29**, deadline 30 June 2026 [S23].
  - An earlier DFG call asked for "Kohnen Station for 2024/25" (the season in which it was not opened) [S23].
- **Permits:** Germany files an IEE every year titled "Continued operation of Kohnen Station" (decision: "Proceed - no more than a minor or transitory impact") for 1 Nov-31 Oct periods: 2018/19, 2020/21, 2021/22, 2022/23, 2023/24, 2024/25 and 2025/26 [S19, items 2010, 2251, 2326, 2516, 2602, 2721, 2836]. Item 2836 (2025/26) is labeled "Operation of Kohnen **wintering** station", which looks like a template error. These are paper permits, not evidence of occupation.
- **Planned trench roof:** BzPM 767 says a third roof over the drill trench was planned for 2023-24 "to keep the trench and its borehole accessible for the EPICA campaign". BzPM 796 instead describes clearing out and closing the trench, and says the borehole extension to the surface was postponed [S22].

### Capacity
- COMNAP 2017: 8 beds, 4 staff and 2 scientists at peak (summer), max 28 people at a time, 160 m² under roof [S2].
- Oerter 2009: camp designed for 20 permanent people during drilling plus 5-7 short-term; "up to 27" with movable containers [S20]. AWI: "up to 20 researchers at a time" [S23]. Wikipedia says 28 [lead only].
- Summer only, no winter staff [S2; S23].

### Infrastructure
- Eleven 20-ft ISO containers on a steel platform on 16 pillars (about 32 m x 8 m): radio room, mess room, kitchen, bathroom, two bedrooms, snow melter, generator, store, workshop [S20; S2]. Some containers came from the dug-out Filchner Station [S23].
- Drill and science trench: 66 m long, 4.8 m wide, 6 m deep, wooden roof (with a second level) [S20; S23]. Its roof loads are being managed with snow blowers [S22, BzPM 767].
- Power: fossil fuel, 220 V, 24 h [S2]. 2021/22: diesel engine replaced; an external genset supplied the station, a 10-ft container genset was backup [S22]. 2023/24: station generator repaired. Wikipedia mentions 100 kW [lead only, unverified].
- Water: snow melter fed from the roof by crane [S20]; water system replaced with copper pipes in 2023/24 [S22].
- Communications: email, satellite phone, VHF [S2]; repair of the aeronautical radio in 2023/24 [S22].
- Runway: snow runway; Oerter says 1,200 m long, orientation 065°/245° [S20]; COMNAP 2017 says 2,000 m x 20 m [S2]; Wikipedia says 2,957 ft [lead only]. **Contradiction, unresolved.**
- Winter storage facility, food stores and cargo containers are left on site [S22].

### Access
- **Traverse:** from Neumayer III, 750-760 km, about 10-11 days with up to six PistenBully vehicles [S20; S22; S23]. Fuel use about 400 L per tonne of payload per 1,000 km; about 180 tonnes per season to run the base during EPICA [S20].
- **Air:** by Basler BT-67 or Dornier 228 (AWI) and Polar 5/6 [S20; S23], including refueling stops; the 2009 paper says air supply was mainly for people and light cargo. DROMLAN has served Kohnen from Novolazarevskaya and Troll since 2002/2005 [S20; DROMLAN search summary only].
- Nearest hubs (my great-circle calculations from the COMNAP point): Neumayer III 554 km (route about 750-760 km); Troll 341 km; SANAE IV 381 km; Tor 382 km; Maitri 604 km; Novolazarevskaya 605 km; Halley VI 719 km.

### Other facilities within about 25 km
- No other station. Within a few kilometers:
  - AWS9 (University of Utrecht) at 75°00'09"S 0°00'26"W, 2,892 m, operated 31 Dec 1997 to 21 Jan 2008 and replaced by a new AWS about 150 m NNE [S20]. An AWI automatic weather station was erected in 2021/22 [S22].
  - Snow-height gauges 1 km away (dismantled Jan 2008) [S20].
  - Boreholes B32-B52 (COFI 2012/13, and 2023/24 thermometry) [S22].
  - The airstrip, about 2 km from AWS9.
- Nearest other nation's facilities are 330 km and beyond (Svea, temporarily closed, 332 km).

### Stated purpose
- Logistics base for the EPICA deep ice core in Dronning Maud Land (EDML), and refueling station for plateau flight campaigns; later the Coldest Firn (CoFi) project since 2012/13 [S20; S2; S23].

### Other notes
- Protected areas: none near. Hazards: extreme cold, altitude 2,892 m (a higher rate of medical incidents is noted in BzPM 758), whiteouts, trench-roof snow loads, burial.
- AWI says the station "can accommodate up to 20 researchers" and lists Halley, SANAE IV and Neumayer III as "adjacent stations" [S23].

### Revival realism
Kohnen is a mothballed summer camp kept alive by periodic, small AWI technical visits, not a candidate for a new year-round post. Evidence: it opens only every two to three years, needs a 10-day diesel traverse and about four technicians to open, the platform needs raising every second year and it was last raised in 2021/22, the 2023/24 visit emptied and closed the trench, and AWI has stopped even annual openings. Evidence for continued life: AWI keeps renewing its annual permit, lists Kohnen in the 2028/29 call for proposals, and has a runway and a ready-built camp. No source mentions a plan to restart deep drilling there. Beyond EPICA, the successor project, is at Little Dome C near Concordia (search summary only).

---

## 4. Contradictions between sources

1. **Halley VI ice speed:** BAS pages say about 700 m/yr [S3, S4] and 400 m/yr [S14, S6]. The BAS Sept 2023 release says 4 m/day, the TC paper says 900 to 1,500 m/yr [S11, S9], and ITS_LIVE says about 1,400 m/yr [S17]. The BAS figures are stale; I used the measurements.
2. **Halley VI ice thickness:** BAS 130 m [S3] vs 150 m [S6, S8, S10] vs Bedmap3 120-125 m [S18]. Method and date differences; not reconcilable.
3. **Halley opening date:** 6 Jan / 15 Jan / 16 Jan 1956 [S14, S3, S16].
4. **Halley relocation distance:** 23 km [BAS] vs about 20.6 km from rounded degree-minute positions [S13].
5. **Halley staff:** 52 beds [S2, S3] vs "approximately 40" summer [S3] vs a plan for 40 in 2023 [S9]; 16 winterers (design) vs 13 (COMNAP 2017 [S2]).
6. **Jinnah longitude:** 25°E in the 1991 Ministry text vs 25°45'E in Wikipedia/Wikidata. Wikipedia's "125 km south" for the Iqbal Observatory also disagrees with its own coordinates (119 km).
7. **Jinnah region:** "Sør Rondane Mountains" (Wikipedia, NIO [S24, S25g]) vs "Princess Ragnhild Coast" (1991 text) vs "Schirmacher Oasis" (ISSRA 2024 [S25d]). Schirmacher Oasis is at about 11.7°E, so ISSRA is inconsistent with every coordinate given.
8. **Jinnah dates:** establishment 15 Jan (Wikidata), 18 Jan (Pakistan Maritime Museum, ISSRA for the weather station) or 25 Jan 1991 (Ministry text, Wikipedia); Iqbal Observatory 18 Jan 1991 (ISSRA) vs 1992-93 (Wikipedia).
9. **Pakistan and the Antarctic Treaty:** accession 1 Mar 2012 [ATS]; Gulf News says 2011; Pakistan Maritime Museum says "Atlantic Treaty 2012". ISSRA says Pakistan is not a treaty signatory and "retains membership of SCAR since 1989"; Gulf News and tvinkal give 1992.
10. **Jinnah status:** "Active" and "maintained" (Wikipedia, Pakistan government post) vs "no longer maintained" (ISSRA), "no expedition since 1993" (Gulf News) and "no expedition" (SCAR reports 2007-10).
11. **Kohnen velocity:** GPS 0.74-0.756 m/yr [S20, Wesche 2007] vs ITS_LIVE 2.5-3.3 m/yr [S17] (instrument noise floor).
12. **Kohnen runway:** 1,200 m [S20] vs 2,000 m x 20 m [S2] vs 2,957 ft (Wikipedia).
13. **Kohnen distance to Neumayer:** 757 km (Wikipedia, route) vs 554 km great circle (my calculation). Not a real conflict; one is a route.
14. **Kohnen status:** COMNAP "Temporarily Closed" [S1] vs Wikipedia "operational" vs AWI's open-every-few-seasons pattern. Consistent with each other only if "temporarily closed" means "not staffed this season".

---

## 5. Search log (exact strings and dead ends)

**Web searches (WebSearch):**
- `Halley VI Research Station 2025-26 season status summer only BAS`
- `Jinnah Antarctic Station Pakistan Sør Rondane location status`
- `Kohnen Station AWI temporarily closed EPICA Dronning Maud Land status`
- `Halley Research Station Brunt Ice Shelf A81 iceberg calving January 2023 station location distance chasm`
- `Brunt Ice Shelf speed up after A81 calving Halley VI velocity m/yr Christmas 2023 Cryosphere Hogg Luckman`
- `Halley VI station velocity ice flow metres per year Brunt Stancomb-Wills Halley station GPS 2023 2024 acceleration`
- `Brunt Ice Shelf 2025 Halley VI station future relocation Halley VII BAS decision`
- `Brunt Ice Shelf 2026 calving rift McDonald Ice Rumples velocity Halley station`
- `Halley Research Station 2025/26 season BAS summer field season Brunt Ice Shelf microturbine team flown`
- `"Halley VII" British Antarctic Survey replacement research station`
- `Halley station access Wolfsfang runway DROMLAN flights Cape Town Halley skiway aircraft Basler Twin Otter BAS season`
- `Halley Research Station "Creek 4" OR "Creek 3" relief route Brunt Ice Shelf ship relief Drewry Point`
- `Hodgson 2019 "McDonald Ice Rumples" bathymetry seabed depth metres beneath Brunt Ice Shelf grounding history`
- `King 2018 "Brunt Ice Shelf" ice thickness radar Halley "ice thickness" 150 m cavity water depth hundreds of metres`
- `Brunt Ice Shelf ice thickness Halley VI BEDMAP ice draft water column depth beneath Halley station seabed depth McDonald Ice Rumples`
- `"Brunt Ice Shelf" 2025 new study rift Halloween crack calving Halley station risk Oliver Marsh`
- `"Brunt Ice Shelf" ice velocity "2024" OR "2025" Sentinel-1 acceleration deceleration pinning point grounded icebergs result`
- `Brunt Ice Shelf news 2026 iceberg A-83 Halley Research Station summer season 2025-26 BAS update velocity`
- `Halley Bay emperor penguin colony Windy Creek Important Bird Area Antarctic Specially Protected Area ...`
- `Pakistan Antarctic Programme Jinnah Antarctic Station 1991 first expedition location Sør Rondane ...`
- `Pakistan Antarctic station Jinnah revive programme 2024 2025 NIO Antarctic expedition status abandoned dismantled`
- `Pakistan accession Antarctic Treaty 2012 Pakistan non-consultative party ats.aq information exchange Jinnah station`
- `COMNAP Antarctic Station Catalogue 2017 Pakistan Jinnah station Princess Ragnhild Coast`
- `niopk.gov.pk Pakistan Antarctic Programme Polar Research Cell Jinnah Antarctic Station expeditions`
- `"Jinnah" Pakistan Antarctic "Iqbal" automatic weather station "71°27" OR "70°50" OR "70°24" ...`
- `Pakistan Antarctic expedition 1991 landing "Princess Ragnhild Coast" Jinnah station ice shelf Columbialand unloaded site`
- `Pakistan Antarctic station Jinnah "no longer" OR "abandoned" OR "defunct" ...`
- `ats.aq Pakistan Jinnah Antarctic Station Pakistan information paper ATCM ...`
- `Perseus blue ice runway Princess Elisabeth Antarctica ...`
- `Kohnen-Station AWI Sommerstation Dronning Maud Land zuletzt betrieben Saison Kohnen Station geschlossen Rückbau`
- `Kohnen Station last season occupied 2016/17 OR 2017/18 OR 2018/19 AWI Antarctic "Kohnen Station" snow buried closed since`
- `AWI Neumayer Kohnen season report "Kohnen" station "this season" OR "diese Saison" not opened pandemic 2020/21 ...`
- `"Expeditions to Antarctica: ANT-Land 2022/23" OR "ANT-Land 2023/24" OR "ANT-Land 2024/25" ...` (and 2019/20, 2018/19 variants)
- `"Kohnen Station" "was not opened" OR "remained closed" OR "was closed" season 2023/24 OR 2024/25 AWI Neumayer`
- `AWI Kohnen station future "Kohnen" EPICA borehole trench Beyond EPICA decision keep or dismantle ...`
- `AWI "2025/26" Kohnen Station traverse OR "Kohnen" Neumayer Station III season 2025/26 call for proposals 2026/27 Kohnen`
- `Wesche Eisen Oerter Schulte Steinhage 2007 Surface topography and ice flow in the vicinity of the EDML deep-drilling site ...`
- `DROMLAN Kohnen skiway refuelling AWI Dronning Maud Land Air Network ...`
- `Antarctic Specially Protected Areas Dronning Maud Land list ASPA ...`
- `Bedmap3 data download netcdf ...` and `Bedmap3 mask values 0 ocean 1 grounded ice ...`

**Direct data work (not web search):**
- COMNAP CSV and 2017 PDF downloaded and parsed.
- SCAR gazetteer API queried (Jinnah, Iqbal, Pakistan, Halley, Brunt, Kohnen, Roi Baudouin, Perseus, Creek).
- ITS_LIVE annual composite read at the three stations and at 16 other points.
- Bedmap3 GeoTIFFs (mask, thickness, bed, surface; BAS PDC DOI 10.5285/2d0e4791-8e20-46a3-80e4-f5f6716025d2) downloaded and sampled.
- ATS EIA database items 0-3500 scanned for Kohnen, Halley, Jinnah and Pakistan.
- Oerter et al. 2009 (Polarforschung 78) and AWI BzPM 733, 745, 758, 767, 784, 796, 807 read from their PDFs.
- Internet Archive captures read for BAS, NIO and Polar Conservation Organisation pages.

**Dead ends:**
- **BAS website direct:** CloudFront WAF challenge (HTTP 202, empty body); WebFetch also returned empty. Died at the source. Worked around with Internet Archive captures (capture 20261002205058 for the facility page, "web/2025" and "web/2026" redirects for the others).
- **"Halley VII":** no hit in any source. Died at the sources (no such plan appears to exist).
- **Creek 3 / Creek 4 coordinates:** not found. Only "Creeks" and "N9" in a 2016 blog, and generic 15-20 km relief sites in Z-fids. Died at the sources.
- **ATS protected-areas database for Halley, Jinnah and Kohnen:** JavaScript-rendered, not scrapable. Died at the source. EIA database did work (server-rendered).
- **BedMachine v3:** needs an Earthdata login. Replaced with Bedmap3 (open).
- **Jinnah in the SCAR gazetteer, COMNAP CSV, COMNAP 2017 catalogue and ATS information exchange:** none. Died at the sources (the station is simply not registered).
- **niopk.gov.pk:** only a tweet about "30 years in Antarctic"; archived NIO pages give no coordinates. Died at the sources.
- **SPRI library record 118700:** behind a Cambridge login wall. Not read.
- **Tribune.com.pk (2020):** HTTP 403 live; the Wayback copy is about an Argentina-Pakistan meeting, with no station detail.
- **Headland 2009 (chronological list) and Riffenburgh Encyclopedia of the Antarctic:** books, not consulted. Wikipedia cites Headland for the 25 Jan 1991 date.
- **Kohnen 2025/26 season status:** the AWI report for it is not yet in the repository. Died at the sources.
- **AWI's reason for closing Kohnen:** not stated in any AWI document read. Died at the sources.
- **Kohnen seasons 2016/17 and 2017/18:** not checked (gap).
- **Kohnen GPS velocity newer than 2007:** none found.

---

## Source table (all accessed 2026-10-04 unless noted)

- **S1** COMNAP Facilities_Nov2024.csv: https://www.comnap.aq/s/Facilities_Nov2024.csv (redirects to static1.squarespace.com/static/61073506e9b0073c7eaaf464/t/673356c10f9d077dbd45e569/1731417793555/Facilities_Nov2024.csv)
- **S2** COMNAP Antarctic Station Catalogue, Aug 2017 (Kohnen p.78, Halley VI p.138): https://www.comnap.aq/s/COMNAP_Antarctic_Station_Catalogue.pdf
- **S3** BAS Halley VI page (Wayback capture 2026-10-02): https://web.archive.org/web/20261002205058/https://www.bas.ac.uk/polar-operations/sites-and-facilities/facility/halley/
- **S4** BAS Halley VI page, older text (Wayback capture 2025-12-31): https://web.archive.org/web/20251231205917/https://www.bas.ac.uk/polar-operations/sites-and-facilities/facility/halley/
- **S5** BAS "Halley Research Station relocation" project: https://www.bas.ac.uk/project/moving-halley/ (read via Wayback)
- **S6** BAS press release 16 Jan 2017: https://www.bas.ac.uk/news/halley-research-station-antarctica-to-close-for-winter/ (via Wayback)
- **S7** BAS 2 Feb 2017: https://www.bas.ac.uk/news/halley-vi-research-station-relocation-success/ (via Wayback)
- **S8** BAS "Brunt Ice Shelf movement": https://www.bas.ac.uk/project/brunt-ice-shelf-movement/ (via Wayback)
- **S9** BAS press release 13 Sep 2023: https://www.bas.ac.uk/news/brunt-ice-shelf-speeds-up-after-calving-of-giant-iceberg/ (via Wayback)
- **S10** BAS press release 21 May 2024: https://www.bas.ac.uk/media-post/brunt-ice-shelf-in-antarctica-calves-new-iceberg/ (via Wayback)
- **S11** Marsh, Luckman & Hodgson 2024, The Cryosphere 18, 705: https://tc.copernicus.org/articles/18/705/2024/
- **S12** Morris et al. 2025, The Cryosphere 19, 4303: https://tc.copernicus.org/articles/19/4303/2025/
- **S13** Hodgson et al. 2019, The Cryosphere 13, 545: https://tc.copernicus.org/articles/13/545/2019/
- **S14** BAS long read, 2 June 2026: https://www.bas.ac.uk/blogpost/seventy-years-on-the-ice-the-extraordinary-story-of-halley-research-station/ (via Wayback)
- **S15** Z-fids Newsletters 54-58 (Halley old-hands association; secondary, quotes station leaders): https://zfids.org.uk/zfidnl54.htm ... zfidnl58.htm
- **S16** UK/SCAR Composite Gazetteer API: https://placenames.aq/api/place_names (name_id 109178, "Halley (1988)")
- **S17** ITS_LIVE annual composites v2-updated-september2025 (catalog https://its-live-data.s3.amazonaws.com/datacubes/catalog_v02.json); my point queries, 120 m grid
- **S18** Bedmap3 (Pritchard et al. 2025, Scientific Data; https://nora.nerc.ac.uk/id/eprint/539065/1/s41597-025-04672-y.pdf), data BAS PDC DOI 10.5285/2d0e4791-8e20-46a3-80e4-f5f6716025d2; my point sampling, 500 m grid
- **S19** ATS EIA database: https://www.ats.aq/devAS/EP/EIAItemDetail/ items 1796, 2010, 2251, 2326, 2516, 2602, 2721, 2836
- **S20** Oerter, Drücker, Kipfstuhl & Wilhelms 2009, "Kohnen Station - the Drilling Camp for the EPICA Deep Ice Core in Dronning Maud Land", Polarforschung 78(1-2): https://epic.awi.de/id/eprint/19885/1/Oer2009c.pdf
- **S21** Wesche et al. 2007, J. Glaciol. 53(182), 442-448 (abstract seen via search summary only): https://epic.awi.de/id/eprint/33762/
- **S22** AWI ANT-Land reports, Berichte zur Polar- und Meeresforschung: BzPM 733 (2018/19), 745 (2019/20), 758 (2020/21), 767 (2021/22), 784 (2022/23), 796 (2023/24), 807 (2024/25) at epic.awi.de/id/eprint/50136, 52837, 55241, 57569, 58813, 60186, 60770
- **S23** AWI Kohnen station page https://www.awi.de/en/fleet-stations/stations/kohnen-station.html; AWI proposals page https://www.awi.de/en/about-us/logistics/proposals.html; SPP Antarktisforschung call https://www.spp-antarktisforschung.uni-rostock.de/en/detailansicht-der-news/n/call-for-proposals-neumayer-station-iii-for-2023-24-and-kohnen-station-for-2024-25-antarctica/
- **S24** Wikipedia (leads only): Halley_Research_Station, Jinnah_Antarctic_Station, Pakistan_Antarctic_Programme, Kohnen_Station
- **S25** Pakistan sources: (a) Ministry text on philatelic blog http://paknetmag.blogspot.com/2009/08/pakistan-scientific-expedition-to.html; (b) Haq's Musings http://www.riazhaq.com/2008/01/pakistan-joins-antarctic-research.html; (c) Pakistan Maritime Museum https://pmm.com.pk/antarctica-expeditions/; (d) ISSRA Insight Aug 2024 https://issra.pk/pub/insight/2024/Exploring-Opportunities-For%20Pakistan-to-Revive%20Its-Antarctic-Programme/Insight.html; (e) Gulf News 25 Oct 2020 https://gulfnews.com/world/asia/pakistan/pakistan-eager-to-revive-antarctic-expedition-1.74813273; (f) SCAR national reports 2007-10 https://scar.org/library-data/national-member-reports/pakistan; (g) NIO "Antarctic Research" page via Wayback (2001 and 2012 captures), http://www.niopk.gov.pk/antarct.html and /Antarctic.aspx; (h) ATS Parties page https://www.ats.aq/devAS/Parties?lang=e; ATS Reports by Party https://www.ats.aq/devAS/InformationExchange/LatestReports?lang=e
- **S26** Wikidata Q627249 https://www.wikidata.org/wiki/Special:EntityData/Q627249.json
- **S27** SCAR gazetteer entries (Roi Baudouin, Prinsesse Ragnhild Kyst, Breid Bay, Asuka Camp), same API as S16
- **S28** Matthew Teller blog, 7 Dec 2016 (secondary): https://www.matthewteller.com/?p=2001

**Items I saw only in search summaries (unverified):** Wesche 2007 abstract details; King et al. 2018 thickness figures; Hodgson 2019 pinning-point overlap numbers; Perseus airstrip coordinates; DROMLAN network members; Halley emperor colony failure; ASPA 142 and 163; Beyond EPICA at Little Dome C; the 2015/16 Kohnen traverse.

Nothing was written to the project; scratch files are only under the session scratchpad directory.