# Port research A: the Shackleton Ice Shelf, its front, and the coastal sea-ice environment

**Date:** 2026-10-25 · **Slice:** A of the Relung Panen port study (real-world physical and logistical facts only)
**Subject site:** the real Bunger Hills oasis, Knox Coast, Wilkes Land, East Antarctica (gazetteer point 66°17'S, 100°47'E)
**Scope:** Shackleton Ice Shelf geometry and front; front dynamics; sea ice, fast ice and polynyas; winds, tides, depth; icebergs; published ship access to this coast. **No fiction in this file.** Nothing here proposes a plot, founders or culture.

**Status labels used below**

- **SOURCED**: a source was opened and read, and the number is quoted from it.
- **DERIVED**: computed in this session from a named public dataset. The method is given, so anyone can rerun it.
- **UNVERIFIED**: seen only in a search snippet, or in a source that cites no evidence, or the method has a known weakness. Do not build on it without checking.
- **NOT FOUND**: searched for and not located. Section 4 says where I looked.

---

## 1. Findings summary

**In one paragraph.** No ocean-facing ice front reaches the Bunger Hills. The Shackleton Ice Shelf sits between the oasis and the open sea on every seaward side. The oasis does hold real marine water: inlets and channels more than 200 m deep, with tidal cracks. That water is enclosed by the ice shelf and glaciers, though. It is joined to the ocean only beneath the floating ice, and the Australian Antarctic Division (AAD) describes it as "effectively isolated from the Southern Ocean for 3,000 or 4,000 years." The nearest point where open sea meets the shelf front is about **55–61 km** in a straight line from the oasis's stations. That point is on the western side, at the corner where the Scott Glacier front meets Mill Island. On the eastern side, the front is about **73–76 km** away. The AAD's own field-site page says "85 km inland from the Shackleton Ice Shelf." Off the front, the sea is covered by drifting sea ice for most of the year. Passive-microwave records show average February concentrations of about 40–57% just off the front (1979–2020). The swing from year to year is very large: some summers clear completely, and others stay above 80% all summer. On the one ship approach to the oasis that is described in print (USS *Edisto*, January 1948), the ship reached shelf ice about 40 miles (≈64 km) from the oasis through "some of the heaviest and most difficult ice ever navigated by ship." The last part of the trip was flown in by helicopter.

### Key figures

| # | Figure | Value | Unit | Source | Data date | Status |
|---|---|---|---|---|---|---|
| 1 | Shackleton Ice Shelf area | 33,820 | km² | Arthur et al. 2020, *The Cryosphere* 14:4103 (also Wikipedia, USGS-derived) | not stated by source | SOURCED |
| 2 | Area of the ADD "ice shelf" polygon that contains the Shackleton system | 34,609 projected in EPSG:3031 ≈ **33,400 true** | km² | SCAR Antarctic Digital Database (ADD) v7.12 polygons, BAS ArcGIS service | ADD 2025 release | DERIVED (true area from the polar-stereographic scale factor at ~65.8°S) |
| 3 | Along-shore length of the shelf; seaward projection | ≈384; ≈145 (west) and ≈64 (east) | km | Wikipedia, "Shackleton Ice Shelf" (USGS GNIS text) | mapping from 1955 Highjump photography | SOURCED (from a secondary source) |
| 4 | Ice thickness toward the front | 180–250 (Denman tongue front ≈450) | m | Thompson et al. 2023, *TC* 17:157, citing BedMachine (Morlighem et al. 2020) | model compiled 2020 | SOURCED |
| 5 | Ice thickness at the calving front | 231 | m | Arthur et al. 2020 | not stated | SOURCED |
| 6 | Ice-front height (freeboard) at Mawson's Western Base, about 95°E (far west, not near Bunger) | 60–100 ft (18–30 m); "eighty to one hundred feet" in another passage | ft | Mawson, *Home of the Blizzard*, ch. 19; AAD "Mawson's Huts" pages | Feb 1912 | SOURCED (historical eyewitness) |
| 7 | Ice-surface height just inside the western front near Scott Glacier and Mill Island | ≈27–34 | m above the EGM2008 geoid | ETOPO 2022 15″ (NOAA NCEI), sampled through ERDDAP | compilation, source year not checked | DERIVED (geometry caveat in §2.1) |
| 8 | Straight-line distance, Edgeworth David base to the nearest open-sea front (western, Scott Glacier/Mill Island corner) | **55.1** | km | ADD front line from Sentinel-1, 2 May 2022 | 2022-05-02 | DERIVED |
| 9 | Same distance from Dobrowolski station / from the Bunger Hills gazetteer point | 59.7 / 61.2 | km | same | 2022-05-02 | DERIVED |
| 10 | Distance to the eastern front (Edgeworth David / Dobrowolski / gazetteer point) | 75.5 / 73.0 / 72.7 | km | ADD front from Sentinel-1, 6 Jun 2016 | 2016-06-06 | DERIVED |
| 11 | Nearest oasis or archipelago rock to any open-sea front | ≈33 | km | ADD rock-coastline and front lines | lines dated 2000 and 2016/2022 | DERIVED |
| 12 | AAD's stated distance from Edgeworth David to the shelf | "85 km inland from the Shackleton Ice Shelf" | km | AAD field-sites page | page current 2026 | SOURCED (method not stated, and it differs from #8) |
| 13 | Advance of the shelf front, 1962–2022 / 2015–2022 | 18 total / ≈0.3 per year | km | Thompson et al. 2023 | 1962–2022 | SOURCED |
| 14 | Ice speed on the main shelf | ≈0.2 (near the grounding line) to ≈1 (toward the front) | m/day (≈73–365 m/yr) | Thompson et al. 2023 (Sentinel-1) | 2017–2021 | SOURCED (m/yr DERIVED) |
| 15 | Scott Glacier calving; iceberg C-39 | >25 km section; C-39 measured 15 × 8 nmi, centered 65°40'S 99°44'E | km / nmi | Thompson et al. 2023; US National Ice Center press release | Apr 2022 | SOURCED |
| 16 | Shackleton Polynya ice production; mean winter thin-ice area | 123 ± 12 km³/yr; 11 ± 1.2 × 10³ km² | — | Tamura et al. 2016, *JGR Oceans* 121, Table 1 | 1992–2013 | SOURCED |
| 17 | Mean February sea-ice concentration in 25 km cells just off the front | 40–57 (by cell) | % | OSI SAF OSI-450-a monthly | 1979–2020 | DERIVED |
| 18 | Mean August sea-ice concentration in the same cells | 59–88 | % | same | 1979–2020 | DERIVED |
| 19 | Open-water days (concentration <15%) per July–June season in those cells | mean 14–29 by cell; range 0–109; 6 of 9 seasons had essentially none in most cells | days | OSI-450-a daily (3,653 days) | seasons 2011/12–2019/20 | DERIVED (probably minimums; see the caveat in §2.3) |
| 20 | Water depth 0.5–15 km seaward of the front | ≈115–460 | m | ETOPO 2022 | compilation | DERIVED / UNVERIFIED (gridded, not soundings) |
| 21 | Depth of the marine inlets inside the oasis | ">200" | m | AARI paleogeography page, "Оазис Бангера" | not stated | SOURCED |
| 22 | Mean wind speed and air temperature at the oasis | 4.6 m/s; −11.2 °C | — | Doran et al. 1996, *Antarctic Science* (White Smoke Lake station) | Jan 1992 – Jul 1993 | SOURCED |
| 23 | Direction of strong winds (>10 m/s) at the oasis | 118 ± 21 | °T | Tafoni study, *Antarctic Science* (abstract snippet only) | not stated | UNVERIFIED |

---

## 2. Findings by question

### 2.1 Q1: location, size, thickness, front height, front length, distance to the oasis

**Location and extent.**
- **SOURCED.** The shelf "front[s] the coast of East Antarctica from 95° E to 105° E." It separates the Queen Mary Coast (west) from the Knox Coast of Wilkes Land (east). Along-shore length is about 384 km. It projects about 145 km seaward in the west and about 64 km in the east. Area is 33,820 km². *(Wikipedia, "Shackleton Ice Shelf", text drawn from USGS GNIS; "mapped in greater detail in 1955, using aerial photography obtained by US Navy Operation Highjump, 1946–47".)*
- Arthur et al. (2020) independently give the same area: "Shackleton Ice Shelf, in Queen Mary Land, East Antarctica (65° S, 100° E), covers an area of 33 820 km²." **SOURCED.**
- **UNVERIFIED.** The Russian Wikipedia article gives 37,400 km², 180–200 m thickness, a surface height of 15–35 m, ice domes up to 250–300 m, a coastline length of 440 km and a 170 km projection into the Mawson Sea. It cites no sources. The Great Russian Encyclopedia (bigenc.ru) appeared in a search snippet with 37,000 km² and 180–200 m, but the page refused access (HTTP 401). The figures disagree with #1 because sources define the shelf differently (whether the Denman, Scott and Roscoe tongues count). Treat the size as about 33,000–37,000 km², depending on definition.
- **DERIVED.** The ADD v7.12 high-resolution polygon layer has one "ice shelf" polygon covering the Shackleton system. Its area is 34,609 km² in projected EPSG:3031 units. The projection's areal scale factor at about 65.8°S is about 1.035 (standard parallel 71°S), so the true area is about 33,400 km². Queried from `services7.arcgis.com/.../High_resolution_vector_polygons_of_the_Antarctic_coastline/FeatureServer/1`, feature 1487.
- **Knox Coast** is "that portion of the coast of Wilkes Land between Cape Hordern 100.52 degrees E and the Hatch Islands 109.28 degrees E" (AAD gazetteer #359). **SOURCED.**

**Thickness.**
- **SOURCED.** Thompson et al. 2023 (citing BedMachine, Morlighem et al. 2020): "Close to the grounding line ice thicknesses range from 300 to 1400 m, thinning toward the ice front where ice thickness is in the range of 180–250 m with the exception of the front of the Denman Glacier tongue at ∼450 m thick."
- On the side next to Denman, the shelf "thins from ∼300 m thick closer to the grounding line to ∼150 m thick close to the Denman Glacier–Shackleton Ice Shelf shear margin" (ICECAP radar, December 2016). An area of "heavily fractured ice shelf ice, ∼2300 km² in size, held in place by fast ice and ∼150 m thinner than the adjacent ice shelf body" is the source of rifts R1 and R2. Rift R1 starts from the lee side of Masson Island, in the western part of the shelf.
- Arthur et al. 2020: "Ice thickness varies across the ice shelf from 231 m (at the calving front) to <10 m around Mill Island." **SOURCED** (quoted as written; the "<10 m" figure probably reflects how their thickness grid handles the Mill Island ice rise, and I did not check it further).
- Rintoul et al. 2025 (*Science Advances* 11:eadx1024): "The draft of the ice shelf is relatively deep (>300 m) beneath the floating tongues" and relatively shallow elsewhere. AAPP summary: "much of its base sits only 100–300 meters below the ocean surface." **SOURCED.**

**Front height (freeboard).**
- **SOURCED, historical, about 95°E (Western Base, roughly 250 km west of Bunger, not the Bunger sector).** Mawson's party described "a perpendicular cliff, sixty to one hundred feet above the water," and elsewhere "the cliff was eighty to one hundred feet in height." That is about 18–30 m. *(Home of the Blizzard ch. 19, AAD; mawsonshuts.antarctica.gov.au.)* The AAD page adds that the largest "ice barriers" stand "as much as 50 meters above sea level."
- **DERIVED.** ETOPO 2022 15″ surface elevation (EGM2008 heights, NOAA NCEI, sampled through the CoastWatch ERDDAP) gives about **27–34 m** on the shelf just inside the western front near Scott Glacier and Mill Island. **Caveat:** ETOPO still shows ice about 30 m high up to 3–5 km seaward of the ADD May 2022 front. Its ice surface comes from a source older than the April 2022 Scott calving. The value is therefore the general shelf-surface height in that sector, not the height of today's cliff.
- **UNVERIFIED and anomalous.** In the eastern sector, ETOPO shows only **2–4 m** for the first ~25 km inside the ADD 2016 eastern front, rising to 10–18 m nearer the Highjump Archipelago. Ice shelf 180–250 m thick would stand about 20–35 m high. A 2–4 m surface is what sea ice (fast ice) would look like, or a gap in the DEM. In MODIS imagery from February 2021, large floes are breaking out inside the ADD eastern front line at about 101.5–102.3°E (NASA GIBS MODIS Terra true color, 13 Feb 2021; visual). Rintoul et al. 2025 place float profiles "under the fast ice east of the SIS." **Open question: part of what the ADD maps as "ice shelf" on the eastern side may be multiyear fast ice.** If so, the "eastern front" in #10 is a seasonal or episodic fast-ice edge, not a shelf cliff. See §4.
- A PGC "rema_dev" ImageServer was also sampled. It returned uniform values of about −3 m across the eastern sector, which looks like fill data, and its vertical datum is undocumented. **Not used** (dead end, §5).

**Front length.**
- **DERIVED.** The ADD "ice shelf and front" lines facing the sea between about 93.7°E and 102.5°E add up to **≈784 km** along their traced path. That length follows every tongue, rift mouth and re-entrant, so it is not comparable with the 384 km along-shore figure. Segments: feature 82, Sentinel-1 IW, 2 May 2022, 578.5 km; feature 218, north of Mill Island, Sentinel-1 EW, 6 Jun 2016, 68.3 km; feature 121, eastern front, 6 Jun 2016, 81.4 km; feature 220, western end, 29 May 2016, 56.0 km.
- Denman Glacier's ice front was "35 km wide" (Miles et al. 2021). **SOURCED.**
- Mill Island: an ice-domed island "46 km long and 30 km wide," 1,260 km², "46 km north of the Bunger Hills" (Wikipedia, USGS GNIS). **SOURCED (secondary).** Its northern coast forms part of the seaward front. ADD calls the west and east sides of the island "ice coastline" (AUSLIG RADARSAT-1, 29 Sep 1997). In the ADD polygons, Mill Island is "land" (projected area 1,270 km²).

**Where the front is relative to the oasis.**
- **SOURCED.** The oasis is bounded "by the ice sheet to the east, Apfel Glacier to the south, Edisto Glacier to the west and Shackleton Ice Shelf to the north" (search-result summary of Bunger Hills literature; the AAD 2024 article says "the Edisto Glacier to the west, the continental ice sheet to the south and east, and an ice shelf to the north"). Wikipedia: "On the north, Bunger Hills is bordered by Shackleton Ice Shelf, which separates the area from the open sea."
- **SOURCED.** Inside the oasis there is marine water: Edisto Channel ("a channel between the islands off the Bunger Hills"; its south end "is filled by Edisto Ice Tongue"), plus Penal Bay, Vetvistaja Bay, Luchistaja Bay, Igrivaja Bay, Majachnaja Bay and others. These appear on AAD map 16154 (March 2024, 1:200,000, coastline from the AAD 1:1M series 2023, bathymetry from GEBCO 2021). On that map the "Sea" of the embayment is closed off to the north by the gray ice shelf.
- **SOURCED.** The water is enclosed. AAD, 13 Dec 2024: "The marine environment around the Bunger Hills is unlike anywhere else in Antarctica… effectively isolated from the Southern Ocean for 3,000 or 4,000 years." The AARI paleogeography page (Russian): oceanic waters are connected to the oasis's inner marine basins beneath the floating parts of the glaciers. Marine water areas reach depths of more than 200 m. Tidal cracks run around the perimeter of the lakes. Gore and Berg 2020 (*Antarctic Science* editorial, from its abstract and snippet only; the full text refused access): the oasis is "surrounded by the ice sheet, heavily crevassed glaciers and Shackleton Ice Shelf, which has made sea- and land-based approaches difficult and rarely attempted."
- **DERIVED.** Straight-line distances from the ADD front lines (great-circle distance; code in §5):

| From | To the western open-sea front (Scott Glacier/Mill Island corner, 65.770°S 100.293°E; 2022) | To the front north of Mill Island (2016) | To the eastern front (65.780°S 101.809°E; 2016) | To the grounded ice coast east of the shelf (102.49°E; 2022) |
|---|---|---|---|---|
| Edgeworth David (66.2498°S 100.6032°E) | **55.1 km** | 74.0 km | 75.5 km | 93.7 km |
| Dobrowolski (66°16'29"S 100°44'49"E) | 59.7 km | 78.3 km | 73.0 km | 89.1 km |
| Bunger Hills gazetteer point (66.2833°S 100.7833°E) | 61.2 km | 79.7 km | 72.7 km | 88.1 km |
| Nearest exposed rock of the oasis or Highjump Archipelago (≈66.02°S) | ≈33 km | ≈50 km | ≈34 km | ≈57 km |

The AAD's "85 km inland" (#12) is larger than every station-to-front figure above. The page does not say how it was measured; it may be a route distance or use an older front. **Unresolved.**

**Glacier tongues reaching the sea near the oasis.**
- **SOURCED (Thompson et al. 2023).** The floating system is the Shackleton Ice Shelf "together with the distinctive tongues of the Denman and Northcliff Glacier, Scott Glacier, and Roscoe Glacier, as well as an area of fast ice to the west of the Denman Glacier tongue."
- Scott Glacier's floating front borders the embayment between the Denman tongue and Mill Island. "There is no clear margin between Scott Glacier and Apfel Glacier offshore of the Taylor Islands, so we cannot comment on a distinct ice front position." Apfel Glacier, which drains past the south of the oasis, therefore has **no separately mapped sea front**.
- I found **no** feature named "Edisto Inlet" in this area. "Edisto Inlet" is a different place, in the Ross Sea. The local names are Edisto Channel and Edisto Ice Tongue.

### 2.2 Q2: front dynamics

- **SOURCED (Thompson et al. 2023, imagery: ARGON KH-5 16 May 1962; Landsat-1 27 Feb 1974; Landsat-5 10–12 Feb 1991; MODIS MOA 2008–09; Sentinel-1/-2 2015–2022, mapped twice a year):**
  - "Between 1962 and 2022… the ice front position of the Shackleton Ice Shelf advanced a total of 18 km with no obvious change in the annual rate of advance."
  - "Calving occurred from the ice front of the Shackleton Ice Shelf, on the side adjacent to Roscoe Glacier in 1991, and a portion of the calved ice has since remained grounded just offshore of it."
  - "Between 2015 and 2022, the front of the Shackleton Ice Shelf then advanced steadily by ∼0.3 km yr⁻¹."
  - Denman: retreated in 1984 through a 54 km calving, then advanced about 63 km since 1991, at 1.8 km/yr in 2015–2022. A late-1940s Denman iceberg longer than 70 km was "roughly 100 km offshore of the ice front" in 1962.
  - Scott Glacier: advanced about 0.75 km/yr in 2015–2019. "Since 2020, small-scale calving has been occurring on the side of the Scott Glacier adjacent to Mill Island, where the ice front position now lies ∼5 km inland of the 2015 front." "In April 2022, a section >25 km long calved from the Chugunov Island side of Scott."
  - Figure 3 caption, Scott front near Mill Island: on 26 Nov 2020, "the central portion of the front has lost some of the blocks held in place by fast ice." By 27 Feb 2021, "the fast ice has broken up."
  - Rifts: R1 is "∼15 km wide at the margin and extends over 40 km into the ice shelf." R2 is ∼5 km wide, extends 16.5 km, then branches into ∼14 and ∼21 km arms; it lengthened 3.8 km in 2015–2022. Near Roscoe, a rift 15 km long and 2 km wide reached "within 3.2 km of the ice front" in 2022, up from 8.5 km in 2015.
  - The main shelf's "flow [is] restrained by islands, ice rises and ice rumples."
- **SOURCED (USNIC press release, 25 Apr 2022).** "Iceberg C-39 has calved from the Scott Glacier area of the Shackleton Ice Shelf… As of April 22, C-39 was centered at 65° 40' South and 99° 44' East and measured 15 nautical miles on its longest axis and 8 nautical miles on its widest axis." First spotted by Jan Lieser (Australian Bureau of Meteorology) and confirmed on Sentinel-1A. **DERIVED:** its center was 83 km from the Bunger Hills gazetteer point.
- **Ice speed (SOURCED, Sentinel-1 feature tracking, 2017–2021).**

| Glacier | Speed | Converted (DERIVED) | Note |
|---|---|---|---|
| Main shelf | ≈0.2 m/d at the grounding line to ≈1 m/d toward the front | ≈73–365 m/yr | |
| Denman tongue | ≈5 m/d | ≈1.8 km/yr | |
| Scott Glacier | 1.2 m/d at the grounding line to >4 m/d near the front | ≈0.44 to >1.46 km/yr | Front speed rose from 2 to 4 m/d between Jan 2020 and Jan 2022 |
| Apfel Glacier | 0.4–0.6 m/d | ≈150–220 m/yr | |
| Roscoe Glacier | about 1 m/d, unchanged | ≈365 m/yr | |

- **Mass trends (SOURCED, as cited in Thompson et al. 2023).** Average thickness change was −3.4 m in 2010–2017 (Hogg et al. 2021). Basal melt for most of the system is 0–1 m/yr. The outer shelf has some of the most intense surface melt outside the Antarctic Peninsula (≈200 mm w.e./yr; Trusel et al. 2013). Surface lakes form "from late November" and peak in "early to late January" (Arthur et al. 2020).
- **Iceberg grounding (SOURCED, Miles et al. 2021, *TC* 15:663).** The 1984 Denman berg, "54 km long (1800 km²)," "drifted ∼60 km northwards before grounding on the sea floor and remained nearly stationary for 20 years before breaking up and dispersing in 2004." There are historical sightings of a large tabular berg in the same place in 1840 (Wilkes) and 1914 (Mawson), but not in 1931.
- **Stability for building on or beside the front.** No source assesses this. The sourced facts that bear on it:
  - Mawson's 1912 Western Base was built 600–640 yd (about 0.6 km) inside the cliff edge, near 95°E. The shelf there did not calve under it, but "a large section of the glacier — many thousands of tons — calved off into the sea" during the stay, and the resulting waves "smashed into fragments all the floe left in the bay." Wild wrote that "the edge of the glacier was very badly broken."
  - The main front has advanced steadily (#13).
  - The Scott sector, the closest part of the front to the oasis, has been calving and speeding up since 2020.
  - **No published engineering or stability assessment was found.**

### 2.3 Q3: sea ice, fast ice, polynyas, open water

- **SOURCED (Rintoul et al. 2025).** "The ice shelf blocks the westward transport of sea ice, resulting in generally heavy sea ice cover to the east and a large and persistent polynya to the west of the SIS." The float surfaced "in the Shackleton Polynya close to the Roscoe Ice Front," and profiles 176–191 were "under the fast ice east of the SIS."
- **SOURCED (Tamura et al. 2016, Table 1, ERA-Interim, 1992–2013).** Shackleton Polynya ice production is 123 ± 12 km³/yr. Mean winter (March–October) thin-ice area is 11 ± 1.2 × 10³ km². Interannual variability "correlates more strongly with polynya extent than with atmospheric forcing, with the exception of the Shackleton Polynya, which correlates better with wind." The neighboring Vincennes polynya (east, toward Casey) produces 90 ± 13 km³/yr.
  - **UNVERIFIED:** a figure of "123 ± 12 Gt/yr, >23,000 km², extends ~200 km offshore" appeared in a search summary attributed to Ribeiro et al. 2023. The Wiley page refused access. Tamura's 123 is **km³**, not Gt, so the summary probably mislabeled the unit.
- **SOURCED (1948).** "Aircraft flights located the ice-free area but no open water at all existed this year. This illustrates how ice conditions can change from year to year" (Nutt 1948, *Arctic* 1(2)).
- **SOURCED (2025).** "The lack of sea ice was exactly why the Denman Marine Voyage was able to get closer to the ice shelf front than expected." *RSV Nuyina* got "within one kilometer of the ice shelf front" (AAPP, 2025–26).

**Satellite record, DERIVED** from EUMETSAT OSI SAF OSI-450-a (sea-ice concentration climate data record v3.0, 25 km EASE2 grid, THREDDS/OPeNDAP at thredds.met.no). Six cells sit 4–19 km off the ADD front and 86–109 km from the oasis:

| Cell | Center | Position relative to the front |
|---|---|---|
| W1 | 99.85°E 65.61°S | west embayment, 19 km from the front |
| W2 | 99.33°E 65.65°S | off the Denman tongue, 4 km |
| N1 | 100.28°E 65.34°S | north of Mill Island, 13 km |
| N2 | 100.80°E 65.30°S | north of Mill Island, 9 km |
| E1 | 101.41°E 65.48°S | east, 7 km |
| E2 | 102.04°E 65.66°S | east, 14 km |

Caveat: 25 km cells next to an ice front blend ice-shelf and coastal signals. Treat these as *offshore* conditions, not conditions *at* the front.

Mean monthly concentration (%), 1979–2020:

| Month | W1 | W2 | N1 | N2 | E1 | E2 |
|---|---|---|---|---|---|---|
| Jan | 76.7 | 87.1 | 63.4 | 56.5 | 66.4 | 72.0 |
| **Feb** | **53.0** | **57.1** | **48.2** | **40.0** | **42.3** | **47.2** |
| **Mar** | **41.0** | **39.2** | **47.2** | **43.1** | **42.0** | **40.6** |
| Apr | 46.9 | 38.7 | 68.0 | 68.9 | 62.2 | 55.0 |
| Jun | 62.7 | 50.9 | 85.0 | 86.7 | 77.7 | 67.1 |
| Aug | 68.3 | 59.3 | 86.5 | 88.1 | 84.3 | 76.5 |
| Oct | 67.7 | 61.8 | 82.9 | 84.5 | 84.6 | 79.7 |
| Dec | 72.5 | 79.5 | 64.9 | 61.5 | 73.3 | 75.3 |

In 2011–2020 the February means were lower, at 28–36%.

February monthly means vary enormously from year to year:
- **0% in every cell:** 2012 and 2018. Also 2011 in all cells except E2.
- **Above 80% in most cells:** 1983, 1995, 1996 and 2007.
- The cells off the east side cleared in some Februaries (1993, 2000, 2002, 2013, 2014) while the western cells stayed 40–80% covered.

Four monthly files are missing on the server (1986-04 to 06 and 1987-12, HTTP 404).

**Open-water days.** DERIVED from OSI-450-a daily data, 2011–2020, all 3,653 days, no gaps. Open water means concentration <15%. A season runs 1 Jul to 30 Jun.

| Season | W1 | W2 | N1 | N2 | E1 | E2 | Window, where open (first to last day <15%) |
|---|---|---|---|---|---|---|---|
| 2011/12 | 107 | 55 | 109 | 109 | 90 | 71 | ~1–11 Dec 2011 to ~25–26 Mar 2012; longest unbroken run 87–89 days |
| 2012/13 | 0 | 0 | 0 | 4 | 22 | 30 | east only, 25 Jan – 12 Mar 2013 |
| 2013/14 | 42 | 10 | 57 | 60 | 53 | 15 | ~5 Jan – 15 Mar 2014 |
| 2014/15 | 2 | 22 | 0 | 0 | 0 | 0 | essentially none |
| 2015/16 | 0 | 0 | 0 | 0 | 0 | 0 | none |
| 2016/17 | 0 | 0 | 0 | 0 | 0 | 1 | none |
| 2017/18 | 52 | 35 | 70 | 71 | 69 | 46 | 31 Dec 2017 – 15 Mar 2018 |
| 2018/19 | 1 | 2 | 1 | 1 | 0 | 0 | none (but see the caveat below) |
| 2019/20 | 9 | 6 | 7 | 14 | 17 | 16 | ~20 Feb – early Apr 2020, broken up |
| **Mean** | **24** | **14** | **27** | **29** | **28** | **20** | |

Spread across seasons, all cells: 0 to 109 days. The mean longest unbroken run is 9–20 days.

The same cells at looser cutoffs:

| Cutoff | W1 | N2 | E1 | E2 |
|---|---|---|---|---|
| Days <30% (mean) | 35 | 35 | 35 | 38 |
| Days <50% (mean) | 85 | 71 | 57 | 65 |

**Caveat, checked against imagery.** On 1 Mar 2019, MODIS shows mostly open water in the eastern bay, but OSI-450-a reports 25–45% for cells E1 and E2 that day. On 22 Feb 2020 the two sources agree (E1 at 0%, matching open water in MODIS). Coastal 25 km cells can read higher than the real concentration because of land and ice-shelf spill-over and small bergs. **The open-water day counts are therefore probably minimums.** Six out of nine seasons nonetheless had essentially no open water at the 15% threshold in most cells.

**Fast ice.**
- **SOURCED:** "an area of fast ice to the west of the Denman Glacier tongue." It has "decelerated by ∼8% in 2018–2021" (Thompson et al. 2023). It holds the fractured shelf ice of the R1 and R2 rift region in place. Fast ice also held blocks at the Scott front until it broke up in 2020–21.
- **SOURCED:** fast ice lies east of the shelf (Rintoul et al. 2025).
- **Thickness: NOT FOUND for this coast.** The only sea-ice thickness clue near the oasis is indirect: AAD 2024 divers drilled "40 centimeter-wide holes… into the sea ice" inside the oasis. That is hole width, not ice thickness.
- **NOT FOUND:** a fast-ice persistence figure for this specific sector. The circumpolar dataset exists (Fraser and Massom, AADC doi:10.26179/5d267d1ceb60c, v2.2, 2000–2018, 1 km, 15-day), but its download page is a JavaScript app that a script could not fetch. The regional analysis in Fraser et al. 2012 (*J. Climate* 25:1137) refused access (HTTP 403).

**Ice-free window dates.**
- **DERIVED:** from the daily record, the open-water window in the cells off the front, when there is one, started between about 1 Dec and 20 Feb. It ended in mid-March in most years, and in early April in 2020. In 2011/12 it ran about 1 Dec – 26 Mar. There was no window in 2014/15, 2015/16, 2016/17 or 2018/19. The monthly minimum falls in February–March.
- **SOURCED anchors:**
  - Edisto entered heavy pack on 12 Jan 1948.
  - Nella Dan called at the "Shackleton Ice Shelf" for Edgeworth David on 13–17 Jan, 13 Feb and 4–5 Mar 1986 (AAD 1985–86 shipping schedule).
  - The 2025 Denman Marine Voyage ran March–May (left Hobart early March, home early May).

**Inside the oasis.** **Observed** (MODIS true-color through NASA GIBS, cleared dates 22 Feb 2020, 1 Mar 2019 and 28 Feb 2025): the enclosed marine embayment of the Bunger Hills was partly ice-free in late February in all three years. It stays enclosed by shelf ice on its seaward side. This is visual interpretation only and is labeled UNVERIFIED.

### 2.4 Q4: winds, swell, tides, depth

**Winds.**
- **SOURCED (Doran et al. 1996, White Smoke Lake, Bunger Hills, Jan 1992 – Jul 1993):** "the mean wind speed 4.6 m s⁻¹, and the mean air temperature −11.2 °C."
- **SOURCED (Arthur et al. 2020, citing Doran et al. 1996):** katabatic winds "descend from the Polar Plateau… and reach 19 m s⁻¹ in summer." Blue-ice areas next to the Bunger Hills are "indicative of persistent snow surface scouring by easterly katabatic winds."
- **UNVERIFIED (snippet of a tafoni study, *Antarctic Science*; the page refused access):** present-day strong winds (>10 m/s) at Bunger Hills "dominantly blow from 118 ± 21 °T."
- **UNVERIFIED (Russian sources from search snippets; not opened):** mean annual wind 6 m/s, maximum to 56 m/s; mean annual temperature −8.2 °C (rather than Doran's −11.2 °C). These are probably from the 1956–58 Oazis station record, but the period was not confirmed.
- **SOURCED, historical, about 95°E:** Western Base blizzards with winds "frequently attaining velocities judged to reach ninety miles per hour" (1912).
- **SOURCED:** Rintoul et al. 2025 link ice-front processes to "easterly winds."

**Swell.**
- **NOT FOUND** as a wave climatology for this coast.
- The only item: the 2025 *Nuyina* voyage "endured huge swells and gale force winds" on its way down (ABC, 3 Apr 2025). The sea-ice cover described in §2.3 damps swell for most of the year (general physics, not site-sourced).

**Tides.**
- **NOT FOUND** as a tidal range for the front or the oasis.
- **SOURCED qualitatively:** White Smoke Lake is "tidally-forced… twice daily lake level fluctuations." Tidal cracks run around lake perimeters (AARI).
- The nearest tide gauge is Casey (GLOSS 278, 66.28°S 110.53°E, about 440 km east). Its BODC handbook page gives no tidal statistics, and the Casey 1996–2007 dataset page refused access.

**Depth.**
- **DERIVED (ETOPO 2022; a gridded compilation, not soundings):**
  - West embayment, 10–15 km off the western front: ≈453–456 m.
  - North of Mill Island: −173 m at 0.5 km offshore, deepening to −461 m at 10 km.
  - East: −115 m at 0.5 km, −164 m at 5 km, −282 m at 15 km.
- **SOURCED:** "Four deep (>800 dbar) channels are found beneath the SIS, the deepest reaching to 1177 dbar" (Rintoul et al. 2025, float). The deepest subglacial trough in Antarctica (>3500 m below sea level) lies beneath Denman (Thompson et al. 2023).
- **SOURCED:** inside the oasis, ROV survey sites were "between 10 and 50 meters deep, progressing to depths of between 100 and 200 meters where possible" (AAD 2024). Marine water areas are deeper than 200 m (AARI).

### 2.5 Q5: icebergs and hazards

- **SOURCED:** "Near the corner of the ice shelf, where our model predicts the Antarctic Coastal Current flows, we saw large numbers of icebergs being carried rapidly westward" (AAPP, Denman Marine Voyage 2025).
- **SOURCED:** large Denman tabular bergs ground on a shoal about 60 km north of the front and can stay for about 20 years (1984–2004). There were sightings at the same place in 1840 and 1914.
- **SOURCED:** part of the 1991 Roscoe-side calving "remained grounded just offshore" (Thompson et al. 2023).
- **SOURCED:** C-39 (15 × 8 nmi) calved in April 2022 from the Scott front, the part of the front nearest the oasis.
- **SOURCED:** a "jade-colored iceberg" was seen near the shelf in 2025 (ABC).
- **Observed** (MODIS, 2019–2025): many small bergs in the open water east of Mill Island, and Bowman Island visible to the northeast. UNVERIFIED, visual only.
- **SOURCED, historical:** Mawson reported calving waves at the ice cliff that broke up the bay's floe in 1912.
- **NOT FOUND:** iceberg counts or density statistics for this sector (ALTIBERG and the BYU/NIC databases were identified but not queried).

### 2.6 Q6: published ship access to this coast (one-paragraph pointer; other slices hold the detail)

- **1840:** Wilkes's USEE mapped part of the shelf from *Vincennes* (Wikipedia, SOURCED).
- **1912:** Mawson's AAE ship *Aurora* landed the Western Party on the shelf near 95°E. Stores were moored to a floe, then hauled up the cliff by "flying-fox": "32 tonnes of stores were lifted to the top of the ice cliffs within four days" (SOURCED).
- **1936:** *William Scoresby* discovered Mill Island (SOURCED).
- **12 Jan 1948, USS *Edisto*:** "finally penetrated the pack to a low area of shelf ice some forty miles distant from the 'Oasis'." The shelf "was skirted to the eastward." *Burton Island* "remained outside the pack." Helicopters "transferred the exploring party to the shore forty miles away" (Nutt 1948, *Arctic* 1(2):88; SOURCED).
- **1986:** *Nella Dan* called at the "Shackleton Ice Shelf" three times for Edgeworth David (SOURCED).
- **2025:** *RSV Nuyina* spent about two months near the shelf (Denman Marine Voyage) and came within 1 km of the front in a low-ice year (SOURCED).

---

## 3. What a ship-based landing would face (sourced and derived facts only)

1. **No sea-level water route to the oasis.** The oasis's marine water is closed off from the ocean by the ice shelf and glaciers; any connection runs beneath floating ice. This has been described as isolation of "3,000 or 4,000 years" (AAD 2024; AARI; Wikipedia). A ship can reach only the outer front.
2. **Distance from the front.** The nearest open-sea front is about 55 km (from Edgeworth David) to 61 km (from the gazetteer point) in a straight line, at the Scott Glacier/Mill Island corner (ADD, Sentinel-1, 2 May 2022). The eastern front is about 73–76 km away, and parts of that "front" may be fast ice (§2.1). The AAD gives 85 km by an unstated method. In 1948 the ship-to-oasis distance was "forty miles" (≈64 km).
3. **The surface between the front and the oasis.**
   - Floating shelf ice 180–250 m thick near the front, 300 m or more near the grounding line.
   - Surface about 27–34 m above the geoid on the western route (ETOPO), with rifts and crevasses.
   - Fast-ice-held fractured zones.
   - Blue ice scoured by easterly katabatics next to the oasis.
   - The oasis is surrounded by "heavily crevassed glaciers" (Gore and Berg 2020, abstract).
4. **Front height and condition.**
   - The nearest Bunger-sector figures (ETOPO): about 27–34 m.
   - The only eyewitness cliff heights are 60–100 ft (18–30 m) near 95°E in 1912.
   - The cliff edge was "very badly broken" in 1912.
   - The Scott sector has been calving since 2020; the >25 km C-39 calving was in April 2022.
5. **Sea ice offshore.**
   - Heavy pack east of the shelf, and a polynya west of it.
   - Mean February concentration of 40–57% just off the front (1979–2020), with large swings between years.
   - "No open water at all" in 1948; low sea ice let a ship within 1 km of the front in 2025.
   - The best months by the monthly record are February–March.
   - Open water (<15%) just off the front averaged 14–29 days a season in 2011/12–2019/20. It ran 0–109 days, and was essentially zero in 6 of 9 seasons (probably undercounted near the coast).
6. **Icebergs.** A westward berg stream in the coastal current near the shelf's corner. Giant Denman bergs ground about 60 km north of the front for decades. Calving waves at the cliff.
7. **Water depth.** Roughly 115–460 m within 15 km of the front by gridded data (ETOPO). **No sourced soundings at a specific berth.**
8. **Weather.** Mean wind at the oasis is 4.6 m/s (1992–93), with summer katabatic gusts to 19 m/s. Blizzard-force winds were recorded on the shelf near 95°E (1912).

---

## 4. NOT FOUND / open threads

| Item | Where I looked | Died at |
|---|---|---|
| Tidal range at the front or in the oasis | BODC GLOSS 278 (Casey) page; data.gov.au Casey gauge (403); Bunger epishelf-lake searches; DInSAR and CATS2008 searches | Sources: no number published, or access refused |
| Fast-ice thickness and persistence for this sector | Fraser 2012 *J. Climate* (403 at AMS and figshare); Fraser 2021 *TC* (circumpolar only, no regional figure); AADC dataset (download is a JS app) | Sources (access) |
| Whether the ADD's eastern "ice shelf" (about 101.2–102.5°E, 65.8–66.0°S) is shelf or multiyear fast ice | ADD polygons (classed "ice shelf"); ETOPO (2–4 m surface); MODIS (floes breaking out in 2021) | Conflicting evidence. Next step: Sentinel-1/2 time series, BedMachine mask, ICESat-2 freeboard |
| Present cliff height in the Bunger sector, measured | ETOPO (pre-2022 surface); PGC rema_dev (datum unknown); Russian Wikipedia 15–35 m (unsourced) | Sources |
| Swell and wave climatology | General searches; ABC voyage report (anecdote only) | Query: no site-specific product found |
| Iceberg density statistics | ALTIBERG and NIC/BYU database pages (identified, not queried) | Not attempted, out of time; open |
| Ribeiro et al. 2023 (*JGR Oceans*): shelf water and polynya figures | Wiley (403); AMSA 2024 abstract read | Sources (access) |
| Rintoul et al. 2025: polynya size and fast-ice edge positions | PMC full text (figure-dependent; numbers not in text) | Sources |
| Gore and Berg 2020 editorial, full text | Cambridge (403 through WebFetch and curl) | Sources (access) |
| Source of the AAD "85 km" figure | AAD field-sites page | Sources (method not stated) |
| Open-water day counts before 2011 and after 2020 | Only 2011–2020 daily data fetched (OSI-450-a ends 2020; the OSI-430-a extension was not fetched) | Open |
| Recent calvings 2023–2026 | Searches; Wikipedia "2025 in Antarctica" and "2026 in Antarctica"; USNIC | Nothing found. Absence not confirmed for the Denman tongue |

---

## 5. Search log

Format: search string or URL → result → whether it died at the query or at the source.

**Web searches**

1. `Shackleton Ice Shelf area thickness ice front Bunger Hills` (extended) → Arthur 2020, Thompson 2023, Wikipedia. **Hit.**
2. `Shackleton Ice Shelf front position change calving Denman Glacier Sentinel` (extended) → Thompson 2023, Miles 2021, Ribeiro 2023. **Hit.**
3. `Bunger Hills marine inlets Transkriptsii Gulf Highjump Archipelago fjords sea ice` (extended) → AAD 2024 "Marine mystery", Edisto Channel, AAD map 16154. **Hit.**
4. `"Edisto Inlet" OR "Edisto Channel" Bunger Hills Knox Coast gazetteer` → only Edisto Channel; **"Edisto Inlet" dead at the query** (it is a Ross Sea name).
5. `Bunger Hills "hidden Antarctic oasis" Antarctic Science 2020 editorial…` → abstract snippet. **Full text died at the source** (403).
6. `Bunger Hills epishelf lake marine embayment tidal Shackleton Ice Shelf isolation radiocarbon Verkulich` (extended) → epishelf and tidal qualitative facts. **Hit.**
7. `Shackleton polynya area sea ice production Knox Coast Shackleton Ice Shelf` (extended) → Ribeiro 2023 (403), Tamura 2016, Rintoul 2025. **Partial.**
8. `landfast sea ice Antarctica circumpolar dataset Fraser 2000-2018 Shackleton…` (extended) → Fraser datasets. **No regional number.**
9. `"Oceanic Regime Shift to a Warmer Continental Shelf Adjacent to the Shackleton Ice Shelf" pdf Ribeiro` → AMSA abstract only. **Died at the source.**
10. `"Circulation and ocean–ice shelf interaction beneath the Denman and Shackleton Ice Shelves"` → PMC copy found. **Hit.**
11. `Shackleton polynya "123" Gt sea ice production "23,000" km2` → the Gt and 23,000 km² figures **not confirmed** (died at the query). Led to Tamura Table 1.
12. `Tamura 2016 "Shackleton" polynya ice production km3…` → figshare PDF. **Hit.**
13. `"East Antarctic landfast sea ice distribution and variability, 2000–08" Fraser…` → abstract only. **Died at the source** (403 at AMS and figshare).
14. `Shackleton Ice Shelf grounded icebergs fast ice … Knox Coast polynya sea ice heavy` (extended) → PMC Rintoul. **Hit.**
15. `Bunger Hills climate mean annual wind speed temperature Oasis station 1956-1959…` (extended) → Doran 1996. The snippet wrongly placed it in 1956–58; the abstract says 1992–93. **Self-corrected.**
16. `оазис Бангера климат ветер скорость средняя годовая температура станция Оазис` (extended, Russian) → AARI page (read); pogodaiklimat and other pages (snippet only, UNVERIFIED).
17. `Shackleton Ice Shelf ice front height cliff freeboard meters above sea level REMA surface elevation` (extended) → Mawson's Huts pages. The REMA 10–20 / 50–55 m snippet **could not be traced to a source** (dead end at the query).
18. `"Shackleton" ice shelf REMA "surface elevations" "pinning points"…` → irrelevant (a Pine Island paper downloaded and discarded). **Dead at the query.**
19. `REMA mosaic ArcGIS ImageServer…` → elevation2 (returned nothing without a token); rema_dev (fill values, datum unknown). **Discarded.**
20. `"Shackleton Ice Shelf" ice cliff height meters ship voyage front observed` (extended) → Mawson quotes again. **Hit (historical only).**
21. `シャクルトン棚氷 しらせ 観測 2020 フロート 定着氷` (Japanese) → nothing relevant. **Dead at the query.**
22. `sea ice concentration climatology Knox Coast Wilkes Land 100°E 105°E open water days…` (extended) → nothing site-specific. **Dead at the query**, so I computed it myself from OSI SAF.
23. `Edgeworth David base Bunger Hills 1986 established Icebird helicopter ship access ANARE` → AAD field sites (85 km); 1985–86 schedule. **Hit.**
24. `Doran 2000 "Bunger Hills" climatology wind direction katabatic…` → tafoni snippet (118 ± 21 °T). **Page died at the source** (403).
25. `Bunger Hills epishelf lake tidal range cm Gibson Andersen…` → no number. **Dead at the sources.**
26. `Bunger Hills tide fluctuations lake level twice daily amplitude cm…` → no number. **Dead at the query.**
27. `tidal range Casey station Antarctica tide gauge…` → GLOSS page with no statistics; commercial tide sites (not used). **Dead at the sources.**
28. `Denman Glacier Shackleton Ice Shelf tidal amplitude grounding line DInSAR tide range CATS2008 m` → no site number. **Dead at the query.**
29. `iceberg grounded near Shackleton Ice Shelf Denman tabular iceberg drift…` (extended) → Miles 2021. **Hit.**
30. `Antarctic iceberg trajectories Shackleton Ice Shelf westward coastal current…` → general only.
31. `multibeam bathymetry survey Shackleton Ice Shelf Denman Glacier front voyage Nuyina 2024 2025…` (extended) → Denman Marine Voyage. **Hit.**
32. `"Denman Marine Voyage" Nuyina "within one kilometer" ice shelf front sea ice 2025` (extended) → AAPP article. **Hit.**
33. `Море Моусона ледовые условия айсберги глубина шельфовый ледник Шеклтона` (Russian) → BRE snippet; **BRE died at the source** (401); booksite (403).
34. `Mawson Sea Antarctica marginal sea area depth ice conditions icebergs 95° 113°E` → low-quality and LLM-generated pages. **Not used.**
35. `multiyear landfast sea ice east of Shackleton Ice Shelf Bowman Island…` (extended) → nothing quantitative. **Dead at the query.**
36. `Shackleton Ice Shelf calving 2023 OR 2024 OR 2025 OR 2026 iceberg named…` (extended) → USNIC C-39. **Hit**; nothing newer found.
37. `"Operation Windmill" Bunger Hills January 1948 cairn helicopter…` → Nutt 1948 PDF. **Hit.**
38. `沙克尔顿冰架 登曼冰川 冰架前缘 海冰 雪鹰601 航空调查` (Chinese) → Snow Eagle 601 surveyed the shelf; no front or sea-ice numbers. **Dead at the query.**
39. `SCAR Antarctic Digital Database coastline high resolution line v7 download gpkg zip` → found the BAS ArcGIS FeatureServer. **Hit.**
40. `Mill Island Antarctica coordinates…` → Wikipedia (GNIS). **Hit.** The AAD gazetteer search URL returned 404, so that route died at the source.
41. `REMA mosaic …` (see 19).

**Pages opened and read** (WebFetch, or curl plus pdftotext)

- tc.copernicus.org/articles/17/157/2023 (HTML and PDF, full text grepped)
- tc.copernicus.org/articles/14/4103/2020
- tc.copernicus.org/articles/15/663/2021 (PDF)
- tc.copernicus.org/articles/15/5061/2021 (PDF; no regional figures)
- en.wikipedia.org: Shackleton_Ice_Shelf; Bunger_Hills; Mill_Island; Edgeworth_David_Base; Operation_Windmill (no Bunger detail); 2025_in_Antarctica; 2026_in_Antarctica
- ru.wikipedia.org/wiki/Шельфовый_ледник_Шеклтона (unsourced numbers)
- antarctica.gov.au: 2024 "Marine mystery in the Bunger Hills"; 2025 Denman Marine Voyage return article; field-sites page; 1985–86 shipping schedule; Home of the Blizzard chapter 19
- mawsonshuts.antarctica.gov.au: four Western Party pages
- data.aad.gov.au gazetteer: Edisto Channel #332, Knox Coast #359, Bunger Hills #123088
- AAD map 16154 PDF (rendered and viewed)
- paleopolar.aari.ru: Oazis Bangera page
- pmc.ncbi.nlm.nih.gov PMC12680056 (Rintoul et al. 2025)
- aappartnership.org.au: "Melting from the top"
- abc.net.au, 3 Apr 2025
- repository.lsu.edu geo_pubs/692 (Doran 1996 abstract)
- figshare: Tamura 2016 PDF
- usicecenter.gov: C-39 press release PDF
- pubs.aina.ucalgary.ca: Arctic1-2-88.pdf (Nutt 1948)
- bodc.ac.uk: GLOSS 278

**Refused or failed (died at the source)**

- cambridge.org: Gore and Berg editorial; tafoni paper (403)
- agupubs (Ribeiro 2023) (403)
- science.org (Rintoul) (403; the PMC copy was used instead)
- journals.ametsoc.org (Fraser 2012) (403)
- researchgate (403)
- bigenc.ru (401)
- booksite.ru (403)
- forum.arctic-sea-ice.net (403)
- data.gov.au, Casey tide (403)
- springer and geoscienceletters (login redirect)
- data.aad.gov.au/eds/5121 (JavaScript app)

**Data pulls and derivations** (scripts kept in the session scratchpad, `agentA_shackleton/scripts/`)

- **ADD v7.12 high-res coastline polylines** (BAS ArcGIS FeatureServer `High_resolution_vector_polylines_of_the_Antarctic_coastline/FeatureServer/1`, envelope 94–106°E, 64–67.5°S, 290 features). Each line carries a `lineage` field with its Sentinel scene ID. Distances are great-circle (haversine, R = 6371.0088 km) to front vertices. Plotted and checked visually.
- **ADD polygons**, point queries for surface class. A full-geometry download was abandoned because the response ran past 75 MB.
- **ETOPO 2022 v1 15″** through `coastwatch.pfeg.noaa.gov/erddap/griddap/ETOPO_2022_v1_15s`, as point transects across three fronts and along two front-to-oasis lines.
- **OSI SAF OSI-450-a**:
  - monthly 1979–2020: 504 files, 4 missing (HTTP 404)
  - daily 2011–2020: OPeNDAP ASCII subsets of grid rows 233–238 and columns 321–323
  - open water = concentration <15%
- **NASA GIBS WMS**, MODIS Terra true color. Clear dates were chosen automatically by the darkness of the oasis rock pixels: 22 Feb 2020, 1 Mar 2019, 13 Feb 2021 and 28 Feb 2025, with the ADD front overlaid. Three cloudy dates (2022-03-01, 2023-02-25, 2024-02-20) were discarded.
- **Self-corrections in this pass**
  - The WebFetch summarizer converted m/d to m/yr wrongly ("5 m d⁻¹ (0.5 m/yr)"). All conversions were redone by hand.
  - The Doran climate period was wrongly given as 1956–58 in a search snippet; it is 1992–93.
  - A snippet put "Edisto Inlet" near the oasis; the feature is Edisto Channel.
  - The first background download was lost when its shell exited, and was re-run as a managed background task.
