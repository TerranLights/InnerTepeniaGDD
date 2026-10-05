# Founding-Gateway Research B2 — Ross Sea sector RE-RUN WITH WEB SEARCH (Scott, Zukelli)

**Date:** 2026-10-03 · **Scope:** two rows (SCOTT, ZUKELLI) · **Rule set:** LAW 0-R (research fully), DR-19 (founders stand on geography and access, never on station operator or station history).
**Role of this file:** evidence only. It decides nothing. The developer rules.
**Relation to the first pass:** this file does NOT replace `Founding_Gateway_Research_B_Ross_Sea_2026-10-03.md`. That file was written with zero web searches. This one re-runs it with working `WebSearch` and closes its open threads. Where the two disagree, this file says so in §3.
**Treatment:** each row is on its own terms. No game city is compared with another game city. Where two real-world places appear side by side (Christchurch and Hobart), it is because the claim being checked names both. Every operator, program, fishery or station-history fact is labeled **CONTEXT (b)** and is not an input to the basis.
**Style note:** American English; present-day real-world nation names.

---

## 0. HONEST ACCOUNTING (read first)

### 0.1 Effort
- **WebSearch:** about **91 distinct queries** were issued (exact strings in §2.S-G and §2.Z-G). Several calls returned results for two to four sub-queries; if the harness counts those separately, the true count is somewhat higher but under the ~140 ceiling. No WebSearch call failed or was refused this time.
- **WebFetch:** about **100 fetches**. Roughly 25 of them failed or returned nothing usable (403 or 402 paywalls, SSL errors, redirect loops, PDFs the fetch tool could not decode). For **eight PDFs** the tool saved the binary and I ran `pdftotext` on the local copy, so those are read directly rather than through the tool's small-model summary: the USAP Air Operations Manual 2012-13, the HMNZS Aotearoa 2025 IEE (ATS), the NZDF Navy Today issue 263, the ESSD preprint on the 2022 Aotearoa voyage, the CCAMLR Ross Sea fishery report 2025, the USNIC Ross Sea seasonal outlooks 2021-22 and 2022-23, and the USAP Participant Guide chapter 7.
- **Own computation:** all great-circle figures were recomputed with **Vincenty's inverse formula on the WGS-84 ellipsoid**, which is a different method from the first pass's spherical haversine (compared in §A). Coordinates are the first pass's (read off Wikipedia) plus the extra points listed in §A. Computed numbers are always labeled "computed".

### 0.2 Source quality
- **Strongest (primary / official, text read):** USNIC Ross Sea outlooks (U.S. National Ice Center); USAP Air Operations Manual; NZDF Navy Today #263 (HMNZS Aotearoa, 2022); NZDF/ATS Initial Environmental Evaluation for the 2025 Aotearoa voyage; ESSD preprint on Aotearoa 2022; CCAMLR Fishery Report 2025; Australian Antarctic Division (AAD) pages (distances, A319 flights, Macquarie Island); Christchurch Airport; Antarctica NZ; KOPRI (Korea); PNRA/ENEA/CNR (Italy); Heritage Expeditions' own trip reports (day logs with positions); USAP Participant Guide; ABS release pages.
- **Good (named secondary):** Lyttelton Port Company (LPC); OGS; Antarctic Science Platform (NZ); ANSTO participant account; CIRES participant blog; NASA participant blog; Xinhua, CCTV, China Daily, CGTN, Guangming (Chinese state media; Chinese-language pages translated by the fetch tool); gCaptain; Maritime Executive; ChristchurchNZ (a city agency, so promotional in tone).
- **Weak (snippets or tools' summaries; marked where used):** Wikipedia-derived population numbers for NZ places (the Stats NZ release page itself would not render, so Canterbury 698,200 and Christchurch 419,200 rest on two search-tool summaries that quote the Stats NZ release; the rest of the NZ population numbers are Wikipedia pages that cite Stats NZ); tour-agent pages for itineraries (Adventure Life, Chimu, Antarctica Travel Centre, Cool Antarctica); search-tool summaries when the page itself was blocked.
- **Known tool weakness:** `WebFetch` returns a small model's summary. Direct quotes below are the tool's extraction, except where marked "read from PDF text".

### 0.3 What is still thin (full list in §4)
1. **No official sailing time for the cargo-ship leg Lyttelton to McMurdo** from the U.S. Military Sealift Command side; the U.S. pages reached never state it. The best sourced figure is the NZ Navy's own (8 days, 2,380 nm, 2022).
2. **No quantitative summer ice-edge climatology** (a latitude by date) from NSIDC; USNIC gives navigability dates, Heritage gives first-pack-ice positions, the Aotearoa IEE gives "likely 70-75 S". That is a good bracket but not a climatology.
3. **Stats NZ's own release page did not render**; the NZ place populations are second-hand.
4. **Qinling's own logistics** are inferred from news about the ships' port calls; no document states "Qinling is served from X".
5. **Hobart air link frequency after 2021-22** was not found.
6. **Italian C-130 flight time Christchurch to Terra Nova Bay** rests on one photo caption ("almost eight hours") and one participant blog (Safair, "7-hour flight").

---

## 1. SUMMARY TABLE

| | **SCOTT** (Ross Island; Scott Base 77°50′57″S 166°46′06″E, McMurdo 77°50′47″S 166°40′06″E) | **ZUKELLI** (Terra Nova Bay; Mario Zucchelli Station 74°41′39″S 164°06′50″E; USAP manual gives 74°41.0′S 164°06.7′E) |
|---|---|---|
| **Claim as written** | "NZ's Canterbury coast (Christchurch/Lyttelton) is the nearest populous gateway to the Ross Sea." | "Reached by a Southern Ocean run from Tasmania (Hobart); Australia is the nearest of the shortlist (Hawaii, Mongolia, Taiwan, Indonesia, Australia)." |
| **First-pass verdict** | PARTLY SUPPORTED | PARTLY SUPPORTED (shortlist half SUPPORTED; "reached from Hobart" half geographically possible, not nearest, "not how the bay is in fact served") |
| **New verdict** | **PARTLY SUPPORTED (unchanged), now double-checked and sharpened.** "Nearest populous" is still true only above a population threshold of about 105,000; the Southland/Otago coast is 260-350 km nearer. | **SHORTLIST HALF: SUPPORTED (unchanged, now independently confirmed). "REACHED FROM HOBART" HALF: UPGRADED to SUPPORTED AS A REAL, DOCUMENTED ROUTE** (ship and aircraft), while Christchurch/Lyttelton remains the larger hub and the South Island remains nearer by 145 km (Christchurch) to 505 km (Bluff). The first pass's "not how the bay is served today" was too strong. |
| **Distance (great circle, computed WGS-84; km / nm)** | Christchurch to Scott Base **3,832 / 2,069**; Lyttelton **3,825 / 2,065**; Hobart **3,992 / 2,155**; Bluff **3,483 / 1,880**; Invercargill 3,503 / 1,892; Dunedin 3,567 / 1,926; Port Chalmers 3,573 / 1,929. Bearing from Lyttelton: **182° (due south)**. | Christchurch to Zucchelli **3,497 / 1,888**; Lyttelton 3,490 / 1,884; **Hobart 3,642 / 1,967**; Bluff 3,137 / 1,694; Stewart Island (Oban) 3,103; Macquarie Island 2,248 / 1,214. Bearing from Hobart: **172° (south, a little east)**. |
| **Independent confirmation of those distances** | Antarctica NZ (official): "3800km south of Christchurch." USAP Participant Guide: **3,864 km (2,415 mi)**. AirportDistanceCalculator (snippet): 3,825 km. timeanddate (snippet): Hobart to McMurdo **2,154 nm** (computed 2,155). | AAD (official): Hobart to Zucchelli "about **3,650 km**" (computed 3,642). distancede.com: Christchurch to Zucchelli **3,494 km** (computed 3,497). USAP manual: Zucchelli is "190 miles" from McMurdo (computed 193 nm). Web calculator: Jakarta to McMurdo 8,655 km (computed 8,652). |
| **Air: time and carrier** | **5 h (C-17), 7 h (LC-130)**, Christchurch Airport, about **3,920 km by air**; about 100 flights a year, 5,500 passengers (Christchurch Airport page; re-verified this run). | Christchurch to Zucchelli: **about 7 h** (Safair L-100-30, NASA participant blog, 2015) or **"almost eight hours"** (Italian Air Force C-130, photo caption); **Hobart to Zucchelli: about 5.5 h each way ("return flight ... about 11 hours")** on the AAD's Airbus A319, 3,650 km, **flown in 2018 (AAD); announced for 2019-20, 2020-21 (two passenger flights) and 2021-22 (one passenger flight)** per CNR and Italian press releases (announcements, not flight logs). |
| **Sea: time** | **HMNZS Aotearoa, 2022: Lyttelton 3 Feb, McMurdo 11 Feb = 8 days, "over 2,380 nautical miles"** (NZDF Navy Today #263; the route was lengthened by weather, a detour east to 180° and a ship-training detour to Cape Adare and Terra Nova Bay; the great circle is 2,065 nm). | **Lyttelton to Zucchelli (Laura Bassi): 8 days 18 hours, "2,300 miles in total, 850 of them breaking through ice"** (LPC); **Lyttelton to Jang Bogo (Araon): 8 days** (Jan 2017) and **10-12 days early season** (2014); KOPRI says "10 days by ship from Christchurch". **Hobart to Jang Bogo (Araon, Nov 2015): "over eleven days"**, early season, ice over 2 m thick (ANSTO). **Lyttelton to Qinling (Xuelong 2, Nov 23 to Dec 6 2023): about 13 days** (derived). Commercial Hobart departures reach the Victoria Land coast on itinerary day 11 (embark day 2). |
| **Populations** | Christchurch city **419,200** (30 Jun 2025); Canterbury **698,200**; Lyttelton 3,220; Dunedin urban ~104,000 / TA ~132,800; Port Chalmers 1,400; Invercargill urban ~51,200 / city ~58,000; Bluff 1,840; Southland 104,800; Otago 253,900. | Greater Hobart **255,250** (30 Jun 2025, ABS); Tasmania **576.0 thousand** (30 Jun 2025, ABS). Macquarie Island: **no permanent residents; 24 expeditioners in Aug 2026**, usual range 14-40. |
| **Updated one-line basis wording (geography and access only; developer to accept or reject)** | "Ross Island lies about 3,800 km due south of the Canterbury coast (Christchurch and Lyttelton), five to seven hours by air and about eight days by sea across the Southern Ocean; Christchurch, the largest city of the South Island (about 420,000), is the airport and port from which the Ross Sea is worked, though the Southland and Otago coast (Bluff, Invercargill, Dunedin) is 260 to 350 km nearer." | "Terra Nova Bay lies about 3,640 km almost due south of Hobart across the Southern Ocean (a flight of about 5.5 hours; a voyage of about 8 to 11 days by way of Macquarie Island or the lee of New Zealand's south), and about 3,500 km south of Christchurch; of the five shortlisted places, Tasmania is by far the nearest (next nearest, Indonesia, about 7,950 km)." |

> **Wording corrections to the first pass's basis cells.** (1) The first pass said Ross Island lies "south-southwest" of Canterbury; the computed initial bearing is **182°, due south**. (2) The first pass said Terra Nova Bay is "south-southeast" of Hobart; **172°** is nearly due south with a slight easterly lean. (3) The first pass's Zukelli cell omitted flights; the Hobart air link is real (Z-E).

---

## 2. PER-CITY FINDINGS

### SCOTT — Ross Island

**Claim (as written):** "New Zealand's Canterbury coast (Christchurch / Lyttelton) is the nearest populous gateway to the Ross Sea."

#### S-A. Coordinates (confirmed)
- Scott Base 77°50′57″S 166°46′06″E, McMurdo Station 77°50′47″S 166°40′06″E (first pass, Wikipedia). Antarctica NZ official: Scott Base "77° 51′ S, 166° 46′ E" and "3800km south of Christchurch and 1350km from the South Pole." https://www.antarcticanz.govt.nz/scott-base
- USNIC (U.S. National Ice Center) gives McMurdo Station "77°51′S, 166°40′E." https://usicecenter.gov/current/ross_sea_seasonal_outlook_2022-2023.pdf (read from PDF text)

#### S-B. Distances: which figure, from whom (the five figures for Christchurch to McMurdo are not in conflict; they measure different things)
| Figure | What it is | Source |
|---|---|---|
| 3,800 km | "south of Christchurch" (rounded, official) | Antarctica NZ, https://www.antarcticanz.govt.nz/scott-base |
| 3,825 km | great circle, Christchurch to McMurdo (printed by a calculator; also the computed Lyttelton figure) | AirportDistanceCalculator (snippet); computed |
| 3,832 km | great circle, WGS-84, Christchurch city centre to McMurdo | computed this run |
| 3,864 km (2,415 mi) | "south of Christchurch" | USAP Participant Guide ch. 7, read from PDF text. https://www.usap.gov/USAPgov/travelAndDeployment/documents/ParticipantGuide-Chapter7.pdf |
| about 3,920 km | by air (the flown route) | Christchurch Airport, re-fetched this run: https://www.christchurchairport.co.nz/about-us/who-we-are/gateway-to-antarctica/ |

Great-circle table, computed with Vincenty/WGS-84 (km; nm). Haversine from the first pass agrees to within 0.2-0.4% (§A).

| Origin | to McMurdo (km / nm) | to Scott Island (67°22′S 179°54′E, where ships enter the Ross Sea) | to Cape Adare |
|---|---|---|---|
| Christchurch | 3,832 / 2,069 | | 3,093 km / 1,670 nm |
| Lyttelton | 3,825 / 2,065 | 2,680 km / 1,447 nm | 3,086 km / 1,666 nm |
| Hobart | 3,992 / 2,155 | 3,346 km / 1,807 nm | 3,404 km / 1,838 nm |
| Bluff | 3,483 / 1,880 | | 2,751 km / 1,486 nm |
| Invercargill | 3,503 / 1,892 | | |
| Port Chalmers | 3,573 / 1,929 | | |
| Dunedin (city) | 3,567 / 1,926 | | |
| Stewart Island (Oban) | 3,449 / 1,862 | | |
| Geelong (Australia; used by an NZ Navy ship in 2025) | 4,543 / 2,453 | | |

- **Nearest populated NZ points vs Christchurch (to McMurdo):** Bluff 350 km nearer; Invercargill 329; Dunedin 266; Port Chalmers 259. Hobart is 159 km farther; Wellington 257 km farther; Auckland 749 km farther. (computed)
- **Lyttelton to Cape Adare is independently confirmed:** the U.S. Coast Guard's Green Wave incident account (all distances in nautical miles) puts a vessel near Cape Adare "1700 miles from Lyttelton"; computed great circle 1,666 nm. https://www.southpolestation.com/trivia/90s/greenwave.html

#### S-C. Transit time and distance by sea (sourced)
1. **NZDF Navy Today #263 (March 2022), the best single source.** HMNZS Aotearoa "restocked in Lyttelton and departed on 3 February"; "After eight days' passage from New Zealand and over 2,380 nautical miles," she "became the first Navy ship in over 50 years to effect a resupply to Antarctica." Detail: 60° S reached 6 Feb; first icebergs 7 Feb in "iceberg alley"; Scott Island that evening; Coulman Island 9 Feb "towards Terra Nova Bay, encountering their first pack ice"; 10 Feb science; **arrived McMurdo 11 Feb**; "the ice had since broken up and drifted out to sea." Route: south-east to the 180° meridian, then (bad weather) straight south past Stewart Island and back east. Hence 2,380 nm against a 2,065 nm great circle (+15%). The Executive Officer's remark that a straight southward run meets the Balleny Islands and their ice is on the same page. Read from PDF text. https://www.nzdf.mil.nz/assets/Uploads/DocumentLibrary/NavyToday_Issue263-v2.pdf
2. **Corroboration:** the ESSD preprint (the voyage's science data paper) says the ship "departed Lyttleton on February 3, 2022, and returned to New Zealand on February 25"; she entered the Ross Sea "near Scott Island (67 22 S, 179 54 E)" and "could have transited to McMurdo Sound via open water," but turned toward Cape Adare and Terra Nova Bay for ice training; the February 2022 ice extent "was the 4th lowest recorded since 1979." Read from PDF text. https://essd.copernicus.org/preprints/essd-2025-8/essd-2025-8.pdf
3. **2025 NZ Navy plan (ATS Initial Environmental Evaluation):** Geelong departure 27 Jan 2025; rendezvous with the Polar Star "near the sea ice edge (likely **70-75°S**, dependent on conditions during the voyage)"; arrival 8 Feb 2025; "The anticipated time for AOTEAROA to travel from Geelong to McMurdo Station is **6.5 days at 10.5 knots**, three additional days have been allocated" for weather; "up to 14 days of the planned 29 days at sea" south of 60° S; 5 days from McMurdo back to 60° S. Read from PDF text. https://documents.ats.aq/EIES/EIA/02717enIEE%20HMNZS%20AOTEAROA%202025%20Ross%20Sea%20Voyage%20January%20to%20Feb%202025%20-%20Amendment_for%20ATS.pdf · A search summary says the ship arrived 10 Feb and left 12 Feb. **Internal inconsistency flagged:** 6.5 days at 10.5 kn is about 1,640 nm, but Geelong to McMurdo is 2,453 nm by great circle (about 9.7 days at 10.5 kn); read the "6.5 days" as the plan's own (probably ice-edge-to-McMurdo or wrongly stated) figure and do not use it.
4. **Cargo ships (CONTEXT (b), U.S. program):** "Ocean Giant" arrived McMurdo 26 Jan 2025 after calling at Lyttelton; the sealift ships treat Lyttelton as a loading stop; "Ocean Gladiator" "departed Hueneme ... first stop scheduled for Lyttelton, New Zealand in mid-January," about two weeks from California. No days-from-Lyttelton figure was stated on any page reached. https://www.dvidshub.net/news/490246/msc-chartered-ship-mv-ocean-giant-conducting-cargo-offload-support-operation-deep-freeze-2025 · https://maritime-executive.com/article/annual-antarctic-resupply-mission-begins-as-sealift-ship-departs-california
5. **A figure NOT to use:** gCaptain writes of the chartered ship Plantijngracht, "After a stop in Christchurch ... will steam roughly **8,040 nautical miles** over nearly a month before reaching McMurdo." The sentence reads as though 8,040 nm is the Christchurch leg, but that is impossible (the great circle is 2,065 nm). Read as the whole Port Hueneme to McMurdo passage. https://gcaptain.com/msc-sends-dutch-heavy-lift-ship-to-antarctica-sparking-foreign-flag-debate/
6. **Tow, not a transit:** the Polar Star towing the Green Wave from off Cape Adare reached Lyttelton on 1 March 1998 after starting the tow 18 February (about 11-12 days at tow speed). https://www.southpolestation.com/trivia/90s/greenwave.html

**Tourist ships from the South Island (CONTEXT (b); shows the sea time, not an input):**
- **Heritage Expeditions, Bluff.** Trip report HA260205: Bluff 6 Feb 2026, first iceberg 9 Feb, Antarctic Circle 14 Feb (day 10), Cape Adare 15 Feb (day 11), Scott Base 20 Feb (day 16), Terra Nova Bay 23 Feb (day 19), Bluff 4 Mar; **"4,942.3 nautical miles (5,687 statute miles or 9,153 kilometres)" for the whole 28 days**, including The Snares, Auckland Islands, Macquarie Island and Campbell Island; furthest south 77°56.974′S 164°34.077′E. https://www.heritage-expeditions.com/trip-reports/340/ The log of 12 Jan 2015 (report 69): noon positions Snares 48°10′S, Enderby 50°30′S, Macquarie 54°32′S (17 Jan); first iceberg **61°09.8′S 167°12.0′E (20 Jan)**; Antarctic Circle 21 Jan; **pack ice entered 22 Jan at 69°24′S 173°57′E**; "7/10ths of ice with leads" 23 Jan; Terra Nova Bay 24 Jan. https://www.heritage-expeditions.com/trip-reports/69/ Report 162 (Jan 2016): "ten-tenths pack ice" near Ross Island on 26 Jan; "pack ice locked in" at Cape Adare. https://www.heritage-expeditions.com/trip-reports/162/ Campbell Island "lies approximately 660-kilometres south of Bluff" (Heritage); computed 664 km. https://www.heritage-expeditions.com/destinations/antarctica-travel/ross-sea-antarctica-cruise/
- **PONANT Le Soleal, Dunedin (22 days):** embark day 1; days 2-3 at sea and Enderby Island; days 4-6 at sea; **Ross Sea sites days 7-14** (Cape Adare, Terra Nova Bay, Inexpressible Island, Ross Island, Franklin Island); returns via Macquarie Island, The Snares. A note on the page: "2028/2029 season departures begin and end in Christchurch." https://www.chimuadventures.com/en-us/antarctica/ross-sea-expedition-27-lesoleal (agent page)
- **Generic:** "It takes about seven days sailing to reach Antarctica from Australia or New Zealand"; most Ross Sea cruises are 26-30 days; the primary port is Invercargill/Bluff and "less frequently trips may leave from Hobart." https://www.coolantarctica.com/Travel/antarctica_trip_new_zealand_australia.php (agent page; generic)

#### S-D. Air (re-verified, plus new)
- Christchurch Airport (official): Scott Base and McMurdo "about 3,920km by air from Christchurch. It takes five hours to fly in a US Air Force C-17 Globemaster or seven hours in a US Air Force Hercules LC-130"; about 100 direct flights a year; "over 5,500 passengers and 1,400 tonnes of cargo"; the airport "regularly welcomes personnel from the United States, Italy, South Korea, and New Zealand." https://www.christchurchairport.co.nz/about-us/who-we-are/gateway-to-antarctica/
- **No Hobart air link to McMurdo or Scott Base was found.** (Hobart's air link goes to Wilkins Aerodrome near Casey, "approximately 4 hours and 30 minutes in either direction," A319, up to 38 passengers, range "over 5,000 nautical miles", https://www.antarctica.gov.au/antarctic-operations/travel-and-logistics/aviation/intercontinental-operations/a319-background-information/; and, since 2018, occasionally to Terra Nova Bay, see Z-E.)

#### S-E. Sea ice on the Ross Sea route (this closes first-pass thread 2 in part)
- **USNIC (U.S. National Ice Center) Ross Sea outlooks**, the operational source for the U.S. program. "Navigable" means 4/10 or less ice cover. Ross Sea ice-edge recession is forecast by analog years. Data points: in 2018 "melt-out was well underway at the end of November with the Ross Sea polynya extending **200 NM northward** from the Ross Ice Shelf"; "By the 3rd week of December 2018, the polynya extended northward to **72°S**, leaving only 200 NM of pack ice left to melt along the 175°E meridian"; "In 2018, the Ross Sea became navigable (<40% sea ice concentration) on or around **31 December 2018**, which was the first time in recent memory this occurred in December"; in 2020 "the Ross Sea became navigable ... in the **3rd week of January**"; the 2021-22 outlook projected **17 January 2022**; the 2022-23 outlook "conservatively" expected the central Ross Sea navigable by **3 January 2023** (both are forecasts, not outcomes). Fast ice in McMurdo Sound: the typical scenario "leaves around **14-16 NM of fast ice** for the USCGC Polar Star to cut"; in 2021 it extended 38 NM to Cape Bird; in 2022 only about 15 NM. https://usicecenter.gov/current/ross_sea_seasonal_outlook_2021-2022.pdf · https://usicecenter.gov/current/ross_sea_seasonal_outlook_2022-2023.pdf (both read from PDF text).
- **Where the pack begins on a January/February sailing from NZ:** first icebergs 60-62°S (Heritage 2015: 61°09.8′S; Aotearoa 2022: 60°S on 6 Feb, icebergs 7 Feb); pack ice at about 69°S in late January (Heritage 2015: 69°24′S, 22 Jan); the Aotearoa plan expects the Polar Star rendezvous "near the sea ice edge (likely 70-75°S)" in early February. In the very low-ice February of 2022, the ship "could have transited to McMurdo Sound via open water" (ESSD).
- **NSIDC:** at the Antarctic minimum (1.98 million km² on 1 March 2025) "Sea ice is also present in the Amundsen and Ross Seas, but in low concentration"; "Nearly all of the remaining high-concentration sea ice is in the Weddell Sea." https://nsidc.org/sea-ice-today/analyses/antarctic-sea-ice-minimum-hits-near-record-low-again · NSIDC learning page: Antarctic sea ice "extending only to about 75 degrees South latitude (in the Ross and Weddell Seas)" (this describes the southern limit, i.e. the ice shelf edge). https://nsidc.org/learn/parts-cryosphere/sea-ice
- **Search-summary only (pages blocked):** "The Ross Sea is virtually ice-free in February" and Ross Sea winter maximum about 3.8 million km² (Eayrs et al., Reviews of Geophysics, 2019); a conflicting snippet gave the Ross Sea minimum as March, about 0.8 million km². **The two do not agree on month or value; neither was read on the page.**

#### S-F. Populations (official where reached)
- **Christchurch city 419,200 and Canterbury 698,200 at 30 June 2025**, quoted from the Stats NZ release by two search summaries (the page itself returned no body). https://www.stats.govt.nz/information-releases/subnational-population-estimates-at-30-june-2025/ Christchurch urban area 407,800 (Wikipedia, citing Stats NZ).
- **Dunedin:** urban ~104,000; territorial authority ~132,800; Otago region 253,900 (June 2025). **Port Chalmers** 1,400. **Invercargill:** urban ~51,200; city (TA) ~58,000 (Wikipedia/search summary, 2025); Figure.NZ citing Stats NZ: **57,600 (30 June 2024)**. **Southland region 104,800.** **Bluff 1,840.** **Lyttelton 3,220.** (Wikipedia pages citing Stats NZ; June 2025.)
- **Small populated places nearer to the Ross Sea than Christchurch:** Stewart Island/Rakiura about 500 (June 2025; census 2023: 486), 3,449 km to McMurdo; Chatham Islands about 620 (June 2025), 3,557 km to Zucchelli (farther than Christchurch). Campbell Island and the Auckland Islands have **no permanent residents** (Campbell's weather station was automated in 1995).

#### S-G. Exact search strings used for SCOTT (WebSearch)
1. `Lyttelton to McMurdo Station sea voyage days nautical miles resupply vessel`
2. `Heritage Expeditions Ross Sea voyage Bluff to Ross Sea days at sea Campbell Island distance nautical miles`
3. `Polar Star departed Lyttelton New Zealand arrived McMurdo Sound days transit Operation Deep Freeze`
4. `"Lyttelton" "McMurdo" vessel "nautical miles" "Southern Ocean" transit "days" resupply Ocean Giant OR Ocean Gladiator OR Plantijngracht`
5. `Antarctica New Zealand Scott Base resupply vessel from Lyttelton "days" sail Ross Island`
6. `"nautical miles" from New Zealand to McMurdo Sound ship "Lyttelton" icebreaker Krasin OR Aotearoa OR "Polar Star" OR Greenpeace OR "Esperanza" Ross Sea`
7. `HMNZS Aotearoa McMurdo Station resupply voyage Lyttelton arrived McMurdo days at sea Southern Ocean nautical miles 2022`
8. `Antarctica New Zealand "Scott Base" "five days" OR "six days" OR "seven days" OR "eight days" sail from Lyttelton resupply ship McMurdo`
9. `HMNZS Aotearoa arrives McMurdo Station ice pier February 2022 Polar Star escort arrived date`
10. `Aotearoa Geelong McMurdo 2025 Polar Star rendezvous Ross Sea ice edge latitude HMNZS Aotearoa Antarctica 2025 fuel`
11. `Antarctic Sun HMNZS Aotearoa arrives McMurdo Polar Star escort Ross Sea 2022 New Zealand navy ship pier "Aotearoa" "McMurdo" arrived February 2022 days from Lyttelton`
12. `Antarctica New Zealand Scott Base supply vessel arrives Ross Island "left Lyttelton" OR "departed Lyttelton" days later arrived McMurdo Sound vessel resupply Scott Base 2023 OR 2024 OR 2025`
13. `Ocean Giant departed Lyttelton arrived McMurdo Station vessel offload date "Lyttelton" "McMurdo" Operation Deep Freeze resupply vessel arrives ice pier February`
14. `Operation Deep Freeze Lyttelton Christchurch cargo vessel Polar Star escort "sailed from Lyttelton" McMurdo "days" 2024 OR 2025 OR 2026 Ocean Gladiator Plantijngracht arrived McMurdo`
15. `Military Sealift Command chartered ships arrive Lyttelton halfway point journey McMurdo Station Operation Deep Freeze "nautical miles" remaining Lyttelton to McMurdo`
16. `Polar Star Green Wave tow 1998 Cape Adare Lyttelton transit days miles Coast Guard icebreaker towed fishing vessel Ross Sea`
17. `"Green Wave" Polar Star tow Lyttelton February 1998 Ross Sea Wellington OR Lyttelton "1,515" OR "twelve days" OR "12 days"`
18. `Ross Sea sea ice minimum February extent latitude ice edge 70°S climatology polynya Terra Nova Bay summer ice breakout`
19. `NSIDC Antarctic sea ice Ross Sea regional extent February minimum Ross Sea sector lowest ice`
20. `McMurdo Sound sea ice breakout date annual ice pier icebreaker channel 60 miles Polar Star fast ice edge January`
21. `Ross Sea sector sea ice extent seasonal cycle February minimum million km² Parkinson Cavalieri Antarctic sea ice variability five sectors`
22. `Ross Sea sea ice edge latitude summer "70°S" OR "71°S" icebreaker ship transit pack ice northern limit January Ross Sea expedition`
23. `Ross Sea sea ice extent February minimum "million square kilometers" OR "10^6 km2" regional Antarctic sea ice Ross Sea Weddell Sea summer minimum values Parkinson 2012`
24. `usicecenter.gov Ross Sea seasonal outlook 2024-2025 OR 2025-2026 McMurdo Sound fast ice navigable Ross Sea forecast date`
25. `Stats NZ subnational population estimates 30 June 2025 Christchurch city Canterbury region Otago Southland population`
26. `Stats NZ urban rural area population estimates Lyttelton Bluff Port Chalmers Invercargill Dunedin urban area 2025`
27. `Stats NZ "Otago region" "Southland region" population estimate 30 June 2025 Invercargill city Dunedin city territorial authority`
28. `Stats NZ news release "Canterbury" "698,200" OR "Christchurch city" "419,200" subnational population estimates 30 June 2025 Otago Southland`
29. `Campbell Island New Zealand subantarctic uninhabited automated weather station since 1995 no permanent residents; Auckland Islands uninhabited; Stewart Island Rakiura population 2023 census`
30. `Chatham Islands population Stats NZ 2025 estimated resident population Stewart Island Rakiura population census 2023`
31. `Dunedin Port Otago Bluff Invercargill Southland Antarctic gateway Ross Sea cruise ships departure Antarctic role Southland Dunedin Antarctic strategy`
32. `Bluff Southland Great South Antarctic Ross Sea expeditions Heritage Expeditions Bluff port departures Heritage Adventurer economic Ross Sea gateway Invercargill`
33. `Quark Expeditions Ross Sea voyage Bluff OR Invercargill OR Dunedin OR Hobart itinerary days Ross Sea Ocean Explorer`
34. `Ross Sea cruise departure ports Bluff Hobart Dunedin Christchurch Lyttelton operators list Antarctica Ross Sea expedition Heritage Aurora Quark Poseidon`
35. `Heritage Expeditions Ross Sea "Lyttelton" OR "Bluff" OR "Hobart" departure Antarctic Peninsula-free "Ross Sea" voyage 2027 itinerary day 8 Antarctic Circle Cape Adare`
36. `distance between Honolulu and Antarctica Terra Nova Bay OR McMurdo km Honolulu to McMurdo Station distance miles`
37. `distance Taipei OR Kaohsiung to McMurdo Station km Ulaanbaatar to McMurdo Station distance km`

*(Searches 36 and 37 also feed Z-C.)*

#### S-H. Dead ends (query vs sources)
- **Cargo-ship (MSC) days from Lyttelton to McMurdo:** died at the **sources**. Eight articles on Ocean Giant, Ocean Gladiator, Plantijngracht (gCaptain, Maritime Executive, Marine Insight, DVIDS, MSC) give arrival dates and "halfway point" language but never a transit time from Lyttelton. The DVIDS "halfway points" page and one globalsecurity mirror were unreadable (HTTP 402 / extraction empty).
- **Antarctica NZ "supply run" page:** says only that "Both vessels departed Lyttelton port this week for McMurdo Sound." Sources.
- **Aotearoa 2022 arrival date from the NZDF news pages:** the news pages (NZDF 4 Feb and 16 Feb 2022, Inside Government, Wikipedia) never give it; found in **Navy Today #263** (PDF) after the search tool led there. A search summary that said "reaching McMurdo on 16 February" is **wrong or refers to the news date** (the Navy Today log says 11 February); treat the 16 Feb as a bad extraction.
- **NSIDC regional Ross Sea numbers:** died at the **sources** (NSIDC "Sea Ice Today" pages talk about the continental total; the Eayrs paper returned 403; NASA Earth Observatory URL redirected away).
- **Official Stats NZ release body:** died at the **tool** (page returned only a title).
- **timeanddate and dateandtime.info distance pages:** died at the **tool** (HTTP 403 / fetch error). `curl` from the shell has no network in this environment (timed out), so no calculator could be run from the shell.
- **Quark Expeditions Ross Sea itinerary:** died at the **query** (results gave Heritage and Aurora, not Quark); no Quark Ross Sea page was found.
- **USAP "ParticipantGuide" ship section:** the PDF has no shipping-time table.

#### S-I. Single-source items
- 2,380 nm / 8 days (Aotearoa 2022): one document, Navy Today #263 (but consistent with the ESSD preprint's dates and with the 6 Feb / 11 Feb log).
- 1,700 nm Cape Adare to Lyttelton: one page (southpolestation.com), consistent with computed 1,666 nm.
- First-pack-ice positions: Heritage's own logs for 2015 and 2016 only.
- Stewart Island, Chatham Islands populations: search-summary only.

#### S-J. Open threads for SCOTT
1. A cargo-ship passage time Lyttelton to McMurdo from the U.S. side (MSC voyage log).
2. A true climatological ice-edge latitude by date.
3. Official Stats NZ figures read on the page (rather than via snippets).
4. A ruling on how "populous" is to be read (the answer to "nearest" changes at about 105,000 people).

---

### ZUKELLI — Terra Nova Bay, Victoria Land

**Claim (as written):** "Terra Nova Bay is reached by a Southern Ocean run from Tasmania (Hobart); Australia is the nearest of the developer's shortlist (Hawaii, Mongolia, Taiwan, Indonesia, Australia) to Terra Nova Bay."

#### Z-A. Site coordinates (now official)
- USAP Air Operations Manual: "Approximate location is 74 41.0′S, 164 06.7′E; 190 miles grid south (true north) of McMurdo Station" (computed Zucchelli to McMurdo 358 km = 193 nm; consistent). Read from PDF text. https://www.usap.gov/logistics/documents/FY13_Air-Operation-Manual.pdf
- PNRA: station at "74°42′ South and 164°07′ East," open "from mid-October to mid-February," "an average of 83 people," maximum 124 beds. https://www.pnra.aq/stazione-mario-zucchelli
- KOPRI: Jang Bogo "74° 37′ S, 164° 12′ E," "approximately 12,730 kilometers from Seoul," up to 62 people. https://eng.kopri.re.kr/eng/html/infra/02040101.html
- **Correction to the brief:** the German station Gondwana (Cape Möbius, Gerlache Inlet) is a separate seasonal station; **it has no airfield of its own.** The airfields at Terra Nova Bay are Italian: a seasonal sea-ice runway (two ice runways of 3,090 m and 1,640 m per Wikipedia; PNRA: "a 3,000-meter runway prepared annually on sea ice"; the USAP manual lists it as 10,000 x 250 ft), the **Boulder Clay gravel runway** (2,200 m x 60 m; first C-130J landing 22 Nov 2022, ENEA), and the Enigma Lake skiway (725 m, Twin Otter and Basler). The USAP manual says the sea-ice runway "is operational from late October through early December," and "may not be operational every season." ENEA says New Zealand and South Korea "have already expressed their strong interest in collaborating" on Boulder Clay. https://www.media.enea.it/comunicati-e-news/archivio-anni/anno-2022/antartide-primo-volo-tecnico-sulla-nuova-pista-italiana

#### Z-B. Distances (computed WGS-84; km / nm; haversine from the first pass agrees to 0.2%)
| Origin | to Zucchelli | to Qinling (74°56′04″S 163°42′55″E) |
|---|---|---|
| **Hobart** | **3,642 / 1,967** | 3,663 / 1,978 |
| Southport, Tasmania (southernmost settlement area) | 3,586 / 1,936 | |
| Macquarie Island | 2,248 / 1,214 | |
| **Christchurch** | **3,497 / 1,888** | 3,526 / 1,904 |
| Lyttelton | 3,490 / 1,884 | 3,519 / 1,900 |
| Bluff | 3,137 / 1,694 | |
| Stewart Island (Oban) | 3,103 / 1,675 | |
| Invercargill / Port Chalmers / Dunedin | 3,158 / 3,233 / 3,226 | |
| Sydney | 4,598 / 2,483 | |
| Geelong | 4,198 / 2,267 | |

- **Hobart minus Christchurch:** 145 km (4.2%) to Zucchelli; 159 km (4.2%) to McMurdo; 311 km (10.0%) to Cape Adare. **Hobart minus Bluff:** 506 km (16.1%) to Zucchelli.
- **Independent confirmations of these numbers:**
  - **AAD (official): "Mario Zucchelli Station, about 3650km from Hobart"** (computed 3,642, +0.2%). https://www.antarctica.gov.au/news/2018/first-sea-ice-landing-near-italian-station-for-australias-antarctic-airbus/
  - **distancede.com: Christchurch to Mario Zucchelli 3,494 km**, "4 heures 50 minutes" (a generic jet-speed estimate; do not use the time). https://www.distancede.com/distance-de-vol-entre-christchurch-et-base-antarctique-mariozucchelli-antarctique/VolHistoire/2086565.aspx
  - **German Wikipedia's "Christchurch und Lyttelton ... rund 3200 km entfernt" (the first pass's conflict): no other source supports it; two independent calculations say about 3,490 km.** The German text also says "Versorgt werden kann die Forschungsstation auch von Schiffen, die von Lyttelton (Christchurch) ... operieren." https://de.wikipedia.org/wiki/Mario-Zucchelli-Station *(re-fetched; the sentence is confirmed to exist, and it is the outlier.)*
  - Method check against AAD's printed distances: computed Hobart to Casey **3,431 km** vs AAD **3,443 km** (0.3%) and a Tasmanian government figure of 3,429 km; computed Hobart to Macquarie Island 1,554 km vs AAD **1,542 km** (0.8%).
- **The "Hobart to Antarctica" three-figure conflict (first-pass thread 8) is resolved geometrically:** the nearest point of the continent to Hobart is on the Adélie/George V coast at about 66.5° S, 140-147° E; computed Hobart to Cape Denison **2,701 km**, to Dumont d'Urville 2,685 km, to the Antarctic Circle at 147°E 2,636 km. So **2,575 km and 2,610 km** (Tasmanian government and tourism sources, snippets) are consistent with the nearest coast; **2,500 km** (Wikipedia, for "Tasmania") fits the island's southern tip; **Wikipedia's "approximately 2,200 kilometres" for Hobart is not supported by geometry** and should not be quoted. None of these is a distance to Terra Nova Bay.

#### Z-C. The shortlist (computed WGS-84; km / nm; haversine in brackets)
| Place | Coordinates used | to Zucchelli | to McMurdo |
|---|---|---|---|
| **Australia: Hobart** | 42°52′50″S 147°19′30″E | **3,642 / 1,967** [3,636] | 3,992 / 2,155 |
| Australia: Macquarie Island (no permanent residents) | 54°38′S 158°52′E | 2,248 / 1,214 | 2,607 / 1,407 |
| **Indonesia: Denpasar** | 8°40′18″S 115°14′02″E | **7,948 / 4,292** [7,952] | 8,215 / 4,436 |
| Indonesia: Jakarta | 6°11′S 106°50′E | 8,421 / 4,547 [8,426] | 8,652 / 4,672 |
| Indonesia: Kupang (Timor, the nearest large Indonesian city) | 10°10.6′S 123°36′E | 7,602 / 4,105 | |
| **Hawaii: Honolulu** | 21°18′N 157°51′W | **10,987 / 5,932** [11,010] | 11,238 / 6,068 |
| Hawaii: Hilo (island of Hawaii, the farthest south) | 19°43.8′N 155°05.4′W | 10,864 / 5,866 | |
| **Taiwan: Kaohsiung** | 22°36′54″N 120°17′51″E | **11,235 / 6,067** [11,258] | 11,542 / 6,232 |
| Taiwan: Taipei | 25°02′15″N 121°33′45″E | 11,475 / 6,196 [11,499] | 11,786 / 6,364 |
| **Mongolia: Ulaanbaatar** | 47°55′19″N 106°54′55″E | **14,241 / 7,689** [14,269] | 14,526 / 7,844 |
| Fiji: Suva | 18°08.5′S 178°26.5′E | 6,346 / 3,426 | 6,669 / 3,601 |
| Fiji: Nadi | 17°48′S 177°25′E | 6,375 / 3,442 | |
| New Caledonia: Noumea | 22°16.5′S 166°27.5′E | 5,830 / 3,148 | 6,180 / 3,337 |
| Tonga: Nuku'alofa | 21°08′S 175°12′W | 6,080 / 3,283 | |
| French Polynesia: Papeete; Cook Islands: Avarua | | 6,929; 6,316 | |

- **Reading:** Australia (Tasmania) is the nearest by a factor of 2.2 (Indonesia, Denpasar) to 3.9 (Mongolia). The nearest point of each other shortlisted place (Hilo; Kupang; southern Taiwan) cannot narrow that gap. **No Pacific island is nearer than New Zealand or Tasmania:** the nearest foreign-flag Pacific capital checked (Noumea) is 5,830 km; Fiji 6,346 km. **Populated places nearer than Hobart:** New Zealand's South Island, Stewart Island (about 500 people) and the Chatham Islands are not nearer (3,557 km) but Macquarie Island (2,248 km, expeditioners only) is.
- **Independent confirmation of the Asian distances:** a web calculator prints Jakarta to McMurdo as **8,655 km**; computed 8,652 km. The other shortlist distances were not on any page that could be reached.
- Populations (context): Honolulu 350,964 (2020), Taipei 2,494,813 (Mar 2023), Jakarta 11,010,514 (mid-2025), Denpasar 670,210 (2024), Ulaanbaatar about 1.79 million (2025), Greater Hobart 255,250 (June 2025, ABS). *(Honolulu through Ulaanbaatar are first-pass numbers, not re-verified here.)*
- **ABS (official, fetched):** Greater Hobart **255,250** at 30 June 2025 (+540, +0.2%, release 31 March 2026). https://www.abs.gov.au/statistics/people/population/regional-population/latest-release · Tasmania **576.0 thousand** at 30 June 2025 (+1,200). https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/jun-2025 (search summary of the ABS page).

#### Z-D. Is the "reach it from Hobart" idea a real route? Evidence found this run (CONTEXT (b) for programs; the routes themselves are geography and access)
**By ship from Hobart:**
1. **RV Araon (Korea), Hobart to Jang Bogo, Nov-Dec 2015.** An ANSTO scientist wrote: "No sooner had the crew and researchers arrived safely aboard the icebreaker RV Araon, in what appeared to be an unseasonably idyllic November day in Hobart ..."; "After tracking east from Hobart for the first two days to avoid bad weather, the captain allowed us a final calm lunch in the shelter of far south New Zealand before turning us toward the Ross Sea"; "over eleven days from Hobart"; on arrival "the RV Araon got to within several kilometres of Jang Bogo Station, but is battling sea ice in places over 2m thick"; ashore 9 December; homeward 17 December. https://www.ansto.gov.au/news/ansto-technology-and-expertise-heading-to-antarctica-for-atmosphere-studies (primary participant account; single source for the "eleven days" and the lee-of-NZ route).
2. **Commercial: Aurora Expeditions "Ross Sea Odyssey" (Hobart to Dunedin, 26 days; ship Greg Mortimer).** Day 1 Hobart; day 2 embark; days 3-5 at sea; days 6-7 Macquarie Island; days 8-10 at sea ("Antarctic Convergence ... Antarctic Circle"); **days 11-17 Victoria Land coast and Ross Sea** (sites include McMurdo Sound, "Cape Washington, Terra Nova Bay", Franklin Island, Cape Hallett, Cape Adare); days 18-21 at sea; days 22-24 Auckland Islands and Campbell Island; day 25 at sea; day 26 Dunedin. Hobart to Macquarie is 839 nm (computed) in about 3.5 days; Macquarie to Cape Adare 1,045 nm in about 3.5 days. https://www.adventure-life.com/antarctica/ross-sea/cruises/18732/ross-sea-odyssey · https://www.chimuadventures.com/en-us/antarctica/ross-sea-odyssey-greg-mortimer (agent pages). A separate "Antarctica Featuring the Ross Sea 27 Days" itinerary departs from and returns to Hobart (Greg Mortimer), with Balleny Islands, Terra Nova Bay, McMurdo Sound and the subantarctic islands. https://www.antarcticatravelcentre.com.au/portfolio_page/antarctica-featuring-the-ross-sea-27-days/
3. **China, CONTEXT (b):** Xuelong called at Hobart on 17 Nov 2018 ("the last time it will do so before sailing to the Antarctic," then to Zhongshan, with preparation for the Inexpressible Island station; Xinhua) and 18 Nov 2025; Xuelong's Qinling Station summer team and ocean team were to sail to Hobart in Feb 2026 "to return by plane" (Xinhua, 19 Feb 2026); an ABC piece states that before the pandemic "we had five port calls of [Chinese] vessels" in a season at Hobart and that since then the ships had mostly used Fremantle. http://www.xinhuanet.com/english/2018-11/17/c_137613897.htm · https://www.news.cn/20260219/53b537191a8440e9a910d5142e3e7dd3/c.html · https://www.abc.net.au/news/2024-11-26/china-antarctic-icebreaker-invited-to-use-hobart-as-gateway/104642498
4. **Australian fishing vessels in the Ross Sea (CONTEXT (b)):** the CCAMLR Fishery Report 2025 lists **"2 from Australia"** among 23 vessels notified for the 2026 Ross Sea (Subarea 88.1) toothfish season, and its vessel tables name the Australian-flag Antarctic Aurora and Antarctic Discovery; the fishery typically lasts 6-9 weeks and "a large sea ice bridge must be navigated through." The vessels "normally land into Hobart and Mauritius" and Hobart is the home port of Antarctic Aurora (colto.org / MSC pages, search summaries). Read from PDF text: https://fishdocs.ccamlr.org/FishRep_881_TOA_2025.pdf · https://www.colto.org/2021/01/08/australian-longline-launch-antarctic-aurora/

**By air from Hobart (the first pass found none; this is new):**
5. **AAD A319 (operated by Skytraders), Hobart to Mario Zucchelli.** 19 Oct 2018: first landing on the sea-ice runway; "Mario Zucchelli Station, about 3650km from Hobart"; "the return flight from Hobart to the Italian station will take about 11 hours"; 220 Italian, French, Korean, German and New Zealand expeditioners. https://www.antarctica.gov.au/news/2018/first-sea-ice-landing-near-italian-station-for-australias-antarctic-airbus/ Later seasons: Italian expedition 35 (2019): "An Airbus-A319 from the Australian Antarctic Division will make some flights from Hobart ... to MZS"; expedition 36 (2020-21): "due voli passeggeri da Hobart (Australia) con Airbus-A319" plus one RNZAF cargo flight from Christchurch; expedition 37 (2021-22): "10 intercontinental flights ... one of which, intended for passengers only, will be operated from Hobart." https://tgposte.poste.it/2019/10/23/antartide-al-via-35a-spedizione-italiana-riapre-base-zucchelli/ · https://www.cnr.it/it/comunicato-stampa/9767/antartide-parte-la-36a-spedizione-italiana-in-modalita-emergenziale · https://www.miamisic.org/antarctica-37th-italian-expedition-begins-in-covid-free-mode/ The AAD's A319 page: range "over 5,000 nautical miles providing the ability to fly Hobart to Antarctica and return without refuelling." **Not found:** any such flight after 2021-22, and any Hobart air link to McMurdo.

**Reading (not a ruling):** a Hobart route to Terra Nova Bay exists by sea (11 days in an early-season ice year; 8-9 days on a commercial January itinerary) and by air (5.5 h), but it is the less-used of the two; the South Island has the larger share of the traffic (Z-E).

#### Z-E. Who serves Terra Nova Bay, and from where (CONTEXT (b) ONLY; not an input to the basis)
| Program (station) | Gateways documented | Source |
|---|---|---|
| **Italy (Mario Zucchelli)** | **Air:** Christchurch (Italian Air Force C-130J of the 46th Air Brigade; Safair L-100-30 chartered earlier; RNZAF cargo flights); Hobart (AAD A319, 2018-2022). **Sea:** Lyttelton ("second home port" of Laura Bassi); the ship sails Italy to Lyttelton in about 40 days (2023: Naples 25 Nov, Lyttelton about 40 days later), then does round trips from Lyttelton to Terra Nova Bay. PNRA: Christchurch became "l'hub aeroportuale d'eccellenza per i collegamenti continentali con l'Antartide." About 230 personnel pass through Christchurch each summer (ChristchurchNZ). | PNRA https://www.pnra.aq/it/mariozucchelli/come-si-raggiunge · CNR https://www.cnr.it/en/press-release/12311/antartide-inizia-la-39a-spedizione-italiana · ENEA https://www.media.enea.it/en/press-releases-and-news/years-archive/year-2024/antarctica-icebreaker-laura-bassi-departs-for-the-south-pole.html · ChristchurchNZ https://www.christchurchnz.com/business/growth-sectors/christchurch-antarctic-gateway/international-programs |
| **South Korea (Jang Bogo)** | **Sea:** Lyttelton (Araon "usually visits Lyttelton on its way to and from Antarctica four times"); also **Hobart (Nov 2015)**; KOPRI: "a 12-hour flight from Seoul to Christchurch, New Zealand, followed by a 10-day sea voyage to Terra Nova Bay." **Air:** uses the Italian runway (Wikipedia, KOPRI); Korean staff flew Hobart to Zucchelli in 2018 and 2019-20. | KOPRI https://eng.kopri.re.kr/eng/html/infra/02040101.html · ChristchurchNZ (above) · AAD (above) |
| **China (Qinling, Inexpressible Island; opened 7 Feb 2024)** | **Lyttelton:** Xuelong 2 resupplied there on 22 Nov 2023 after "21 days and over 5,800 nautical miles" from Shanghai and went on to the Ross Sea with the cargo ship Tianhui; arrived at the site on the night of 6 Dec (Beijing time); left 12 Dec for Lyttelton again; Xuelong docked at Lyttelton on 11 Jan 2026 after Qinling (arrived there 29 Dec 2025); ChristchurchNZ: Xuelong 2 "visited Lyttelton four times for personnel rotation" in 2023-24. **Hobart:** see Z-D.3. **New Zealand, 2017-18:** the 34th expedition's Xuelong "will arrive in New Zealand to stock up" and then "sail south to the west coast of the Ross Sea" for preliminary work on the fifth station (search summary of Chinese state media; the port is given as Auckland in one summary and was not confirmed on a page). | https://m.gmw.cn/2023-11/22/content_1303578372.htm · https://news.cctv.com/2023/12/07/ARTI8BvVLlBlvIMAkpILHZGi231207.shtml · https://baike.baidu.com/en/item/China's%2042nd%20Antarctic%20Scientific%20Expedition%20Team/944450 |
| **Germany (Gondwana, seasonal)** | Christchurch ("Germany uses Christchurch as their gateway to the Ross Sea region"; 10-20 scientists and support staff; works in "close logistic cooperation with the Italian Antarctic Program"). | ChristchurchNZ (above) |
| **United States (McMurdo)** | not at Terra Nova Bay; the Terra Nova Bay sea-ice runway is listed as an emergency divert for U.S. C-130s. | USAP manual |

- **Time Lyttelton to Terra Nova Bay by ship (all CONTEXT (b), different seasons):** Laura Bassi 8 days 18 hours (LPC, "2,300 miles in total, 850 of them breaking through ice," Italy's 41st expedition; the unit "miles" is unstated), departing 6 Jan 2024 and entering the Ross Sea about a week later (ASP); Laura Bassi 7 Dec to 16 Dec 2021 (OGS, scheduled arrival); Araon 8 days (Jan 2017, Oregon State blog via search snippet; the blog page itself would not load); Araon "10 to 12 days" (Dec 2014, CIRES participant blog; "depending on when we actually leave and the sea conditions"); Xuelong 2 and Tianhui about 13 days (derived: leave Lyttelton the morning after the 22 Nov 2023 resupply; arrive late 6 Dec). The early-season voyages (Nov-Dec) are slower because of fast ice and the cargo-ship escort.
- **Hobart (11 days, 2015) versus Lyttelton (10-12 days, 2014)** are the two early-season Araon voyages; the sea time from the two ports in the same early-season conditions is therefore **similar**.
- **Terra Nova Bay ice at the shore (primary):** PNRA: "in late October when surrounding waters remain ice-covered, the ship unloads materials onto the pack ice" for sledge convoys; by February "a small dock and barge" are used. https://www.pnra.aq/stazione-mario-zucchelli · Research papers (search summary, pages blocked): "From November to March, Terra Nova Bay is mostly ice-free with a peak in February"; the bay's polynya has a mean size of about 1,300 km² (up to 5,000 km²) because of katabatic winds and the shelter of the Drygalski Ice Tongue. In Jan 2024 "a large patch of sea ice is lingering right where we have some planned activities" and "no priority sites on the transit into Terra Nova Bay could be accessed due to ice cover" (ASP, Laura Bassi). https://www.antarcticscienceplatform.org.nz/updates/ross-sea-voyage-update-arrival-in-terra-nova-bay

#### Z-F. Macquarie Island and other outposts (first-pass thread 7)
- **Macquarie Island Station** (Australia, AAD; 54°38′S 158°52′E; **2,248 km from Zucchelli**, 1,542 km from Hobart per AAD) has **no permanent inhabitants**; all residents are rotating expeditioners. "The number of expeditioners on station varies from 14 to 40." ABC, 28 Aug 2026: "The station is currently home to **24 expeditioners**"; Australia is withdrawing them (the ship Nuyina expected early October) "because of the psychological risks ... inside a mass mortality event" (bird flu), interrupting a presence that "has been permanent, year-round ... since 1948." https://www.antarctica.gov.au/antarctic-operations/stations-and-field-locations/macquarie-island/living/ · https://www.abc.net.au/news/2026-08-28/macquarie-island-scientists-to-be-evacuated-over-bird-flu-fears/107088108
- Other outposts nearer than Hobart to the bay: none populated beyond Macquarie. NZ's Campbell and Auckland Islands have no permanent residents; Stewart Island (about 500) and the Chatham Islands (about 620) are small settled places; Stewart Island is nearer than Hobart (3,103 km), the Chathams are not (3,557 km).
- **Australian vessels in the Ross Sea:** see Z-D.4 (fishing). **No Australian national-program research vessel voyage to the Ross Sea from Hobart was found** (AAD stations are in East Antarctica; its distances table lists none in the Ross Sea).

#### Z-G. Exact search strings used for ZUKELLI (WebSearch)
1. `RV Araon Lyttelton to Terra Nova Bay Jang Bogo voyage days`
2. `Laura Bassi Mario Zucchelli Station Lyttelton Terra Nova Bay voyage days PNRA`
3. `Qinling Station Xuelong 2 Terra Nova Bay departed Hobart OR Lyttelton OR Shanghai 2024 construction`
4. `Hobart to Ross Sea Aurora Expeditions Greg Mortimer Ross Sea Odyssey itinerary Hobart Dunedin days at sea Macquarie Island`
5. `Terra Nova Bay polynya summer open water Mario Zucchelli ship access January sea ice conditions Drygalski Ice Tongue Italica`
6. `Australian Antarctic Division Ross Sea voyage from Hobart Nuyina OR "Aurora Australis" Terra Nova Bay OR "Ross Sea" Hobart departure`
7. `Hobart Ross Sea toothfish fishing vessels depart Hobart Ross Sea CCAMLR Australian vessel transit days`
8. `Xuelong 2 Ross Sea Terra Nova Bay Qinling arrival port call Hobart OR Lyttelton OR Auckland OR Sydney 40th Chinese Antarctic expedition route`
9. `秦岭站 雪龙2 天惠轮 新西兰 利特尔顿 OR 霍巴特 罗斯海 恩克斯堡岛 建站 航线`
10. `Xuelong icebreaker Hobart port call November 2018 Ross Sea Terra Nova Bay new station site survey`
11. `Tian Hui cargo ship Qinling station Terra Nova Bay Lyttelton OR Hobart OR Shanghai Xuelong 2 construction materials arrived`
12. `"雪龙2" 抵达 罗斯海 恩克斯堡岛 2023年12月 天惠轮 抵达 卸货 秦岭站 从利特尔顿 起航 航行 天`
13. `Xuelong 2 Tianhui arrive Inexpressible Island Terra Nova Bay December 2023 left Lyttelton November 23 sea ice Ross Sea escort`
14. `Xuelong 34th Chinese Antarctic expedition 2017-2018 route Hobart OR Auckland OR Lyttelton Ross Sea Terra Nova Bay Inexpressible Island site selection`
15. `China Antarctic expedition Xuelong Lyttelton Christchurch port Qinling Station personnel rotation Xuelong 2 New Zealand Lyttelton Ross Sea Inexpressible Island 2025 2026`
16. `雪龙号 第42次南极考察 霍巴特 离开 秦岭站 抵达 12月29日 中山站 航行 天 海里`
17. `Mario Zucchelli Station Gondwana runway flights Christchurch Basler Twin Otter Italian Antarctic Program logistics PNRA`
18. `Lyttelton Port Company Antarctic Italy Korea Laura Bassi Araon home port Antarctic programmes visit Lyttelton`
19. `Italica Mario Zucchelli Station Lyttelton Terra Nova Bay cargo ship PNRA ENEA "Italica" sailing days`
20. `Christchurch to Mario Zucchelli Station flight hours Boulder Clay runway C-130J OR L-100 Italian Air Force Terra Nova Bay "hours" flight from Christchurch`
21. `Boulder Clay runway Terra Nova Bay first intercontinental flight Christchurch hours flight duration Antarctica Italy 2022`
22. `Korea Jang Bogo Station Christchurch flight Zucchelli Boulder Clay Airbus A319 OR C-17 OR Basler transit hours KOPRI`
23. `campagna antartica PNRA volo intercontinentale Christchurch Mario Zucchelli C-130J "ore di volo" pista Boulder Clay primo atterraggio`
24. `campagna antartica PNRA volo Hobart Airbus A319 Mario Zucchelli ENEA personale volo da Hobart`
25. `Boulder Clay runway Baia Terra Nova C-130J Aeronautica Militare Christchurch volo durata ore atterraggio pista in ghiaia 2023 OR 2024 OR 2025 spedizione antartica`
26. `"Mario Zucchelli" Christchurch volo "circa" ore Hercules C-130 viaggio Antartide Baia Terra Nova partenza Christchurch ore di volo scienziati arrivo base`
27. `Stazione Mario Zucchelli distanza da Christchurch km volo ore Nuova Zelanda Baia Terra Nova`
28. `Terra Nova Bay Mario Zucchelli "km" from Christchurch OR "from New Zealand" distance Italian Antarctic station 3,500 km OR 3,400 km OR 3,200 km`
29. `Jang Bogo Station Korea Terra Nova Bay "Christchurch" km distance KOPRI Jang Bogo Station "from Christchurch"`
30. `distance Hobart to Mario-Zucchelli Antarctic base km distancede OR distance.to OR distancecalculator`
31. `Australian Antarctic Airbus A319 Hobart Mario Zucchelli sea-ice runway Terra Nova Bay flights Italian program Hobart 2019 OR 2022 OR 2023 OR 2024 OR 2025`
32. `Skytraders A319 Hobart Terra Nova Bay Italy ENEA flights "Hobart" Zucchelli intercontinental flight Australia Italy agreement`
33. `Italian Antarctic program Hobart agreement Australian Antarctic Division Airbus Terra Nova Bay "Hobart" PNRA ENEA volo Hobart Zucchelli`
34. `Araon Hobart Terra Nova Bay OR "Ross Sea" Korean icebreaker Hobart port call Australia Jang Bogo`
35. `Araon Hobart November 2015 Jang Bogo Station ANSTO Chambers eleven days Antarctica radon atmosphere Korean icebreaker voyage`
36. `ANSTO Jang Bogo Station Korea Antarctic radon measurements Hobart Araon Terra Nova Bay collaboration KOPRI`
37. `아라온호 호바트 출항 2015 11월 장보고기지 남극 보급 항해 일`
38. `Araon Hobart Tasmania port visit icebreaker Korean Jang Bogo resupply sailed from Hobart December 2015 OR 2016 OR 2017 OR 2018 Ross Sea`
39. `ciresblogs spaceweather RV Araon departs Hobart Jang Bogo 2015 "Breaking Big Ice" OR "Final Destination" Bullett Araon voyage Hobart days sea ice`
40. `Hobart to Cape Adare OR "Terra Nova Bay" OR "McMurdo Sound" nautical miles Southern Ocean voyage sailing days ship Hobart Ross Sea "nautical miles"`
41. `Hobart closer to Antarctica than Perth Townsville 2610 km Tasmania Antarctic gateway Hobart distance to Antarctica Commonwealth Bay Casey`
42. `Hobart Antarctic gateway Tasmania supports Australia France China national Antarctic programs Hobart port icebreakers Nuyina L'Astrolabe Xue Long visits per year`
43. `Antarctic gateway cities Hobart Christchurch Punta Arenas Ushuaia Cape Town which national programs use each COMNAP gateway`
44. `Gondwana Station BGR GANOVEX Terra Nova Bay logistics Christchurch OR Hobart OR Lyttelton German expedition access Italian Zucchelli flight`
45. `Macquarie Island station population expeditioners number winter summer Australian Antarctic Division permanent residents`
46. `Aurora Australis OR Nuyina OR "Southern Surveyor" Australian research vessel Ross Sea voyage Terra Nova Bay OR "Ross Sea" Tasmania Hobart departure Australian science Ross Sea`
47. `Ross Sea toothfish fishery Subarea 88.1 participating members vessels flag states New Zealand Norway Russia Korea Ukraine UK Spain Australia Antarctic Aurora Ross Sea`
48. `Antarctic Aurora longline vessel Australian Longline Hobart Ross Sea toothfish landing port Hobart Antarctic Discovery`
49. `Terra Nova Bay sea ice annual cycle open water January February fast ice breakup Gerlache Inlet ship unloading Mario Zucchelli dock February Terra Nova Bay polynya summer extent`
50. `ABS Regional population 2024-25 Greater Hobart Tasmania population estimated resident population June 2025`
51. `ABS National, state and territory population June 2025 Tasmania population 30 June 2025`
52. `distance from Denpasar OR Jakarta to McMurdo Station Antarctica km calculator Bali to Antarctica distance`
*(Searches 36-37 of the SCOTT list also feed Z-C. The two lists together contain every query; a few were run as paired sub-queries by the tool, and the count of "about 91" is therefore approximate.)*

#### Z-H. Dead ends (query vs sources)
- **A published Hobart-to-Terra-Nova-Bay sea-route distance in nautical miles:** died at the **sources.** The AAD distances page lists only Casey, Davis, Mawson, Macquarie, Heard (km); Tasmania's gateway documents returned 403; no ship log states Hobart to Terra Nova Bay in miles. Only the computed 1,967 nm and the ANSTO "over eleven days" exist.
- **Qinling logistics document:** died at the **sources.** Chinese state media give port calls (Lyttelton 22 Nov 2023; Hobart 18 Nov 2025; Lyttelton 11 Jan 2026) but no "Qinling is served from X" sentence; the first-pass guess that Hobart serves Qinling is partly right (Hobart is an entry and exit port for some ships and personnel) and partly wrong (the 2023-24 construction run used Lyttelton).
- **Baidu / Zhihu pages on the Ross Sea route:** surfaced in search but were not opened (Zhihu article "2025-2026 ... 罗斯海航线全攻略" and the Chinese route paper at html.rhhz.net); open thread.
- **Oregon State blog on Araon from Lyttelton (8 days):** the page redirects to an outage notice; used only as a search summary (marked).
- **KOPRI voyage logs, PNRA logistics PDFs, Italian "Rapporto sulla Campagna Antartica" (e.g., 2012-13):** search results exist; not opened (long PDFs); open threads.
- **Tasmanian government PDFs (Tasmanian Antarctic Gateway Strategy; "Tasmania Delivers ... Antarctica"; Hobart Connections), tourism.tas.gov.au, antarctic.tas.gov.au:** HTTP 403 on every fetch (tool/site block), so the 2,575 km and 2,610 km figures stay as search-summary quotes.
- **Aurora Expeditions' own Ross Sea Odyssey page:** redirect loop in the first pass; this run used agent pages (Adventure Life, Chimu, Antarctica Travel Centre).

#### Z-I. Single-source items
- **"over eleven days from Hobart" (Araon, 2015): one ANSTO page.**
- **Xuelong 2 Lyttelton to Qinling about 13 days:** two Chinese-state-media pages and a date inference.
- **Italian C-130 "almost eight hours":** one photo caption (search summary).
- **Laura Bassi "8 days 18 hours, 2,300 miles ... 850 ... in ice":** LPC page, unit of "miles" unstated.
- **Australian vessels "normally landing into Hobart":** one MSC/colto summary.
- **Hobart A319 flights 2019-20, 2020-21, 2021-22:** each a single CNR/ENEA/news page; the 2018 flight is on the AAD site.

#### Z-J. Open threads for ZUKELLI
1. A sourced sea-route in nautical miles Hobart to Terra Nova Bay (the ANSTO voyage has no mileage).
2. Hobart A319 flights after 2021-22.
3. The Araon's 2014-2025 port pattern (Hobart vs Lyttelton), from KOPRI voyage logs.
4. Chinese route paper (html.rhhz.net) and PRIC reports for Xuelong 2's 2023 Lyttelton-to-Qinling passage with mileage.
5. Whether the developer's shortlist is meant to restrict the answer to Australia (a ruling).

---

## A. COORDINATES USED AND METHOD NOTE

**First-pass coordinates reused (Wikipedia, as read in the first pass):** Scott Base 77°50′57″S 166°46′06″E · McMurdo 77°50′47″S 166°40′06″E · Zucchelli 74°41′39″S 164°06′50″E · Qinling 74°56′04″S 163°42′55″E · Cape Adare 71°17′S 170°14′E · Macquarie Island 54°38′S 158°52′E · Christchurch 43°31′52″S 172°38′10″E · Lyttelton 43°36′S 172°43′E · Hobart 42°52′50″S 147°19′30″E · Bluff 46°36′S 168°20′E · Invercargill 46°24′47″S 168°20′51″E · Port Chalmers 45°49′04″S 170°37′08″E · Honolulu 21°18′N 157°51′W · Taipei 25°02′15″N 121°33′45″E · Kaohsiung 22°36′54″N 120°17′51″E · Jakarta 6°11′S 106°50′E · Denpasar 8°40′18″S 115°14′02″E · Ulaanbaatar 47°55′19″N 106°54′55″E · Antarctic Circle 66°33′51″S.

**Added this run (approximate, from memory and unsourced beyond a one-decimal check; none enters a verdict):** Campbell Island 52°33′S 169°09′E · Geelong 38°09′S 144°22′E · Dunedin 45°52.5′S 170°30′E · Stewart Island (Oban) 46°54′S 168°08′E · Chatham (Waitangi) 43°57′S 176°33′W · Southport TAS 43°26′S 146°58′E · Suva, Nadi, Noumea, Nuku'alofa, Apia, Papeete, Avarua, Hilo, Kupang, Sydney (city coordinates) · Scott Island 67°22′S 179°54′E (ESSD) · Cape Denison 67°00.6′S 142°39.8′E · Dumont d'Urville 66°40′S 140°00′E · Casey 66°16.9′S 110°31.7′E.

**Method:** haversine R = 6,371.0088 km (first pass) vs **Vincenty inverse on WGS-84** (this run). The spherical figures run about 0.2% shorter than the ellipsoidal ones for the NZ and Tasmanian origins, and about 0.2% longer for the northern-hemisphere shortlist places. **Method validation:** computed Hobart to Casey 3,431 km vs AAD 3,443 km; Hobart to Macquarie 1,554 km vs AAD 1,542 km; Hobart to Zucchelli 3,642 km vs AAD 3,650 km; Christchurch to Zucchelli 3,497 km vs distancede 3,494 km; Hobart to McMurdo 2,155 nm vs timeanddate 2,154 nm; Jakarta to McMurdo 8,652 km vs 8,655 km; Zucchelli to McMurdo 193 nm vs USAP "190 miles". Eight external figures agree to within 0.8%.

**Computed sailing times (not sourced; no ice, no weather):** Lyttelton to McMurdo 2,065 nm = 10.8 / 8.6 / 7.2 / 6.1 days at 8 / 10 / 12 / 14 knots; Hobart to McMurdo 2,155 nm = 11.2 / 9.0 / 7.5 / 6.4; Lyttelton to Zucchelli 1,884 nm = 9.8 / 7.9 / 6.5 / 5.6; Hobart to Zucchelli 1,967 nm = 10.2 / 8.2 / 6.8 / 5.9; Bluff to Zucchelli 1,694 nm = 8.8 / 7.1 / 5.9 / 5.0. **Check against sourced voyages:** Aotearoa 2,380 nm in 8 days = 12.4 kn average (a fast passage); Laura Bassi 2,300 nm in 8.75 days = 11 kn; Araon Hobart 11 days = 1,967 nm at 7.5 kn only if the route was direct (it was not: two days east, then ice).

---

## 3. CHANGES FROM THE FIRST PASS

**Facts changed or corrected**
1. **"No Hobart air link to the Ross Sea sector" is wrong.** The AAD flew its A319 from Hobart to Mario Zucchelli on the sea-ice runway in 2018 (3,650 km, about 11 h return) and Italian sources record Hobart passenger flights in 2019-20, 2020-21 (two) and 2021-22 (one). (Z-D.5)
2. **"No program sails to Terra Nova Bay from Hobart" is wrong.** The Korean Araon did so in Nov-Dec 2015 (about 11 days, ice over 2 m); commercial Ross Sea itineraries start in Hobart; Xuelong uses Hobart for Qinling-related movements (Nov 2025, Feb 2026). The pattern "Christchurch/Lyttelton is the main hub" remains true, but "not Hobart" is too strong. (Z-D)
3. **Qinling's gateway:** Lyttelton for the 2023-24 construction run and the 2025-26 rotation; Hobart for entry and exit in 2025-26; "New Zealand" (port unconfirmed) in 2017-18. The first pass left it "UNVERIFIED." (Z-E)
4. **Direction wording:** Ross Island is **due south** of Lyttelton (bearing 182°), not "south-southwest"; Terra Nova Bay is south, slightly east, of Hobart (172°). (Summary)
5. **"Gondwana airfield":** the brief's wording was mistaken; the airfields are Italian (sea-ice runway; Boulder Clay gravel runway, first C-130J landing 22 Nov 2022; Enigma Lake skiway). (Z-A)
6. **Heritage "4,942.3 nm"** is now verified as the total of the 28-day HA260205 voyage (including four subantarctic island stops), not a transit figure. **New warning:** the Heritage trip-report page titled "1570" has a voyage number, not a mileage; a fetch summary read "Approximately 1,570 nautical miles traversed over 28 days" off the report number and must be disregarded. (S-C)
7. **Polar Star tow figure resolved:** the Wikipedia "1,515 mile" figure is the odd one out. A separate account with all distances in nautical miles says the tow began at a position "1700 miles from Lyttelton" and ended 1 March after starting 18 February; the great circle Lyttelton to Cape Adare is 1,666 nm. Do not use 1,515. (S-B)
8. **German Wikipedia's 3,200 km** is unsupported: two independent calculations give about 3,490-3,497 km. (Z-B)
9. **Three "Hobart to Antarctica" distances (2,200 / 2,500 / 2,610 km):** resolved; the nearest mainland coast is about 2,640-2,700 km by computation, so 2,575 and 2,610 are consistent, 2,500 fits southern Tasmania, **2,200 is not supported by geometry.** (Z-B)
10. **Populations updated:** Greater Hobart 255,250 (30 Jun 2025, ABS; the first pass had 254,930 for 2024); Tasmania 576.0 thousand (June 2025); Macquarie Island 24 expeditioners (Aug 2026), none permanent, being withdrawn from October 2026 because of a bird-flu mortality event. (Z-F)
11. **Christchurch to McMurdo:** the first pass had 3,825 km computed and 3,800 km official; this run adds the USAP figure **3,864 km** and the corrected computed value **3,832 km** (ellipsoid). All are the same distance by different conventions. (S-B)
12. **The 8,040 nm "Christchurch to McMurdo" claim in gCaptain** is flagged as a misreading; do not use. (S-C.5)

**Facts newly sourced (threads closed)**
- **Thread 1 (sourced sea times and distances):** NZ Navy 2022, Lyttelton to McMurdo, 8 days, 2,380 nm; Laura Bassi Lyttelton to Terra Nova Bay 8 d 18 h; Araon 8 days (Jan) and 10-12 days (early season) from Lyttelton, about 11 days from Hobart; Xuelong 2 about 13 days; Hobart commercial itinerary about 9 days from embarkation to the Victoria Land coast; Bluff to Campbell 359 nm / 664 km; Dunedin (Le Soleal) 6 days to the Ross Sea with one island call.
- **Thread 2 (ice):** USNIC navigability dates (31 Dec 2018; third week of January 2020; forecasts of 17 Jan 2022 and 3 Jan 2023); fast ice 14-16 NM typical; first iceberg 60-62°S, first pack about 69°S in late January (Heritage 2015), "ice edge likely 70-75°S" in early February (NZDF plan); record-low-ice February 2022 had open water to McMurdo; Terra Nova Bay mostly ice-free November to March.
- **Thread 3:** Qinling and other programs' gateways (Z-E); the Italian runways.
- **Thread 4:** Christchurch to Zucchelli flight about 7-8 h; Hobart to Zucchelli about 5.5 h; Christchurch to McMurdo 5-7 h (re-verified).
- **Thread 5:** populations (S-F, Z-C).
- **Thread 6:** shortlist distances recomputed on the ellipsoid and checked against eight external figures (§A); Fiji and Pacific islands added.
- **Thread 7:** Macquarie (Z-F); Australian vessels in the Ross Sea: fishing yes (two Australian-flag longliners, CCAMLR 2025), national research voyages none found.
- **Thread 8:** all five conflicts addressed above.

**Verdict changes**
- SCOTT: none (PARTLY SUPPORTED stands; sharpened).
- ZUKELLI: **"reached from Hobart" upgraded** from "geographically possible, not how it is served" to "a documented route by sea and air, smaller in traffic than the Christchurch/Lyttelton route." The shortlist half is unchanged (SUPPORTED, with an independent official figure, AAD's 3,650 km).

---

## 4. REMAINING GAPS

1. Official cargo-ship passage time Lyttelton to McMurdo (U.S. MSC / USAP voyage records).
2. Quantitative summer ice-edge climatology on the 170°E-180° line, by date (NSIDC or USNIC archives; the USNIC "Ross Sea Outlook" bi-weekly updates and the USNIC weekly analyses are the likely source).
3. The text of the Stats NZ and ABS release tables (not snippets) for Dunedin, Invercargill, Southland, Otago and Tasmania.
4. KOPRI Araon voyage logs for Hobart vs Lyttelton by season; PRIC (China) route paper for the 2023 Qinling run with mileage.
5. Hobart A319 flights to Terra Nova Bay after 2021-22; any intention of a regular service.
6. Italian PNRA expedition reports (e.g., "Rapporto sulla Campagna Antartica") for the flight time Christchurch to Zucchelli and the Laura Bassi's yearly mileage.
7. Tasmanian government gateway documents (403) for the Hobart-side distance and the national programs using Hobart.
8. Nearest Hawaiian, Indonesian and Taiwanese points: computed to Hilo, Kupang and Kaohsiung only; they cannot change the ranking.
9. A ruling, not research: how "populous" is to be read for SCOTT, and whether ZUKELLI's shortlist restricts the answer to Australia.

---

## 5. REGISTER LINE FOR THE TRACKER
`Founding_Gateway_Research_B2_Ross_Sea_RERUN_2026-10-03.md` — web-search re-run of B. SCOTT: Christchurch/Lyttelton gateway PARTLY SUPPORTED (unchanged; 3,800 km due south, 5-7 h by air, 8 d / 2,380 nm by sea per NZDF; Southland/Otago 260-350 km nearer; Christchurch 419,200, Dunedin urban ~104,000). ZUKELLI: Australia nearest of the shortlist SUPPORTED (Hobart 3,642 km, AAD 3,650 km; Denpasar 7,948 km next); "reached from Hobart" UPGRADED: documented by sea (Araon 2015, ~11 d; commercial Hobart itineraries) and by air (AAD A319, 2018-2022, ~5.5 h); Christchurch/Lyttelton still the larger hub and 145 km nearer; Bluff 505 km nearer. ~91 searches, ~100 fetches.
