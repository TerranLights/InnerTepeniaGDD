# Founding-Gateway Research B — Ross Sea sector (Scott, Zukelli)

**Date:** 2026-10-03 · **Scope:** two rows (SCOTT, ZUKELLI) · **Rule set:** LAW 0-R (research fully), DR-19 (founders stand on geography and access, never on station operator or station history).
**Role of this file:** evidence only. It decides nothing. The developer rules.
**Treatment:** each row is on its own terms; no city is compared with another city of the project. Where two real-world places are set side by side below (for example Christchurch and Hobart), it is because the *claim being checked itself names both*, and every such figure is a plain distance or population.

---

## 0. HOW THIS RESEARCH WAS ACTUALLY DONE (read first — it limits the confidence)

1. **`WebSearch` was unavailable for this run.** The session's WebSearch budget (200 of 200 calls) was already spent when this task started; four opening queries were refused. Nothing in this file comes from `WebSearch`.
2. **What was used instead:** `WebFetch` on specific pages (Wikipedia in English, German, Italian, Korean; Antarctica New Zealand; Christchurch Airport; Australian Antarctic Program; DVIDS) and, intermittently, **a Brave search results page fetched through `WebFetch`** (it returned results on about six calls and then returned HTTP 429 on every later call). Bing, DuckDuckGo, Yahoo, Ecosia, Startpage, Mojeek, Qwant and a SearX instance were tried and were either captcha-walled, blocked, or returned an empty template.
3. **`WebFetch` returns a summary written by a small model, not the raw page.** Quoted text below is therefore *the tool's extraction*, and it sometimes said "the page does not contain X" when X was on a sub-page. A claim marked "single-source" means exactly one fetched page supports it.
4. **Where a number is MY OWN ARITHMETIC (not a sourced figure), it is labeled "computed".** The great-circle distances were computed with the haversine formula (mean Earth radius 6,371.0088 km; 1 nm = 1.852 km) from coordinates that were *read off Wikipedia pages during this run* (listed in §A). **Method validation:** the computed Christchurch–McMurdo great circle is 3,825 km, which **matches a figure printed by AirportDistanceCalculator.com (3,825 km / 2,377 mi)** as seen in a Brave snippet; the computed Hobart–Macquarie Island distance is 1,552 km against the **Australian Antarctic Program's printed 1,542 km** (0.6% apart); the computed Christchurch–Hobart distance is 1,104 nm against a cruising-wiki snippet of "around 1,100 nautical miles" for the direct Australia–New Zealand passage. So the method reproduces three independent printed figures.
5. **Sailing times in this file are NOT sourced** except where a source is named. A "computed" sailing time is simply great-circle nm divided by an assumed speed; it excludes ice, weather and routing, and is shown only to give the order of magnitude.
6. **Single biggest gap:** no source was found that states, in nautical miles or days, a *scheduled* ship route from Lyttelton, Hobart or Bluff to McMurdo Sound or to Terra Nova Bay. That dies at the **search layer** (see §D), not at the sources: the sources very likely exist (national-program voyage logs, the Heritage Expeditions trip reports named in a Brave snippet) but could not be reached.

---

## 1. SUMMARY TABLE

| | **SCOTT** (Ross Island, ~77°51′S 166°46′E) | **ZUKELLI** (Terra Nova Bay, ~74°42′S 164°07′E) |
|---|---|---|
| **Claim as written** | "NZ's Canterbury coast (Christchurch/Lyttelton) is the **nearest populous gateway** to the Ross Sea." | "Reached by a Southern Ocean run from Tasmania (Hobart); Australia is the **nearest of the shortlist** (Hawaii, Mongolia, Taiwan, Indonesia, Australia)." |
| **Verdict** | **PARTLY SUPPORTED** | **PARTLY SUPPORTED** (shortlist half: SUPPORTED; "reached from Hobart" half: geographically possible but NOT the nearest populous coast, and not how the bay is in fact served today) |
| **Key numbers** (great circle, computed; see §A) | Christchurch–Scott Base **3,825 km / 2,065 nm** (official Antarctica NZ: "3800km south of Christchurch"; Christchurch Airport: "about 3,920km by air"). Lyttelton 3,818 km. Hobart 3,985 km / 2,152 nm. **Dunedin/Port Chalmers 3,566 km; Bluff 3,475 km; Invercargill 3,496 km** (all nearer than Christchurch). Auckland 4,575; Wellington 4,082. | Hobart–Zucchelli **3,636 km / 1,963 nm**. Christchurch 3,491 km / 1,885 nm; Lyttelton 3,484 km; **Bluff 3,131 km; Invercargill 3,151 km; Port Chalmers 3,227 km** (all nearer than Hobart). Macquarie Island (Australian-administered, no permanent residents) 2,243 km. Shortlist: **Honolulu 11,010 km; Kaohsiung 11,258; Taipei 11,499; Jakarta 8,426; Denpasar 7,952; Ulaanbaatar 14,269.** |
| **Populations of the gateway** | Christchurch city 419,200 (Jun 2025); urban 407,800; metro 556,500 (one Wikipedia page, internally uneven); Canterbury region 698,200 (Jun 2025). Dunedin urban ~104,000; Invercargill urban 51,200; Southland 104,800. | Greater Hobart 254,930 (2024); Tasmania 573,479 (Jun 2023). |
| **Is "nearest populous" accurate?** | **Not strictly.** Dunedin (~104,000) and Invercargill (51,200) are 270–350 km nearer. **It is accurate** if "populous" means a city of roughly 200,000 or more, where Christchurch is the nearest of those measured (see S-E). | Hobart is **not** the nearest populous coast to Terra Nova Bay: the South Island of NZ is nearer at every point from Bluff to Christchurch. Hobart is **4.1% (145 km) farther than Christchurch** and **505 km farther than Bluff**. |
| **Stronger / equal gateway the claim overlooked** | Southland/Otago (Bluff–Invercargill–Port Chalmers–Dunedin) is geographically nearer; Christchurch is stronger on *scale and on infrastructure* (airport, Antarctic gateway status since 1901 per Wikipedia, ~100 flights a year). | **Yes: New Zealand's South Island** (Christchurch/Lyttelton equal or stronger; Bluff/Invercargill nearer still). Hobart's only distinct claim is that Australia is on the shortlist and Hobart is Australia's Antarctic port. |
| **One-line basis wording (geography only; for the developer to accept or reject)** | "Ross Island lies about 3,800 km (≈2,060 nm) due south-southwest of the Canterbury coast, across open Southern Ocean; Christchurch is the largest city on that side of the Ross Sea and the airport and port (Lyttelton) from which the Ross Sea is reached." | "Terra Nova Bay lies about 3,640 km (≈1,960 nm) south-southeast of Hobart across the Southern Ocean, and about 3,490 km (≈1,890 nm) south of Christchurch; of the five shortlisted places, Australia (Tasmania) is by far the nearest to it (next nearest, Indonesia, ≈7,950 km)." *(See Z-F: this wording is true of the geography as measured, but the geography alone does not select Australia over New Zealand, which is not on the shortlist.)* |

> **Note on the Zukelli wording cell.** Terra Nova Bay (164.1°E) lies about 17° of longitude east of Hobart (147.3°E), so the bay is south-southeast of Hobart. The cell states both Hobart and Christchurch distances so that the wording stays true if the developer later widens the shortlist; the developer may delete the Christchurch clause if the shortlist is to stay closed.

---

## 2. PER-CITY FINDINGS

### SCOTT — Ross Island (Scott Base 77°50′57″S 166°46′06″E; McMurdo Station 77°50′47″S 166°40′06″E)

**Claim (as written):** *"New Zealand's Canterbury coast (Christchurch / Lyttelton) is the nearest populous gateway to the Ross Sea."*

#### S-A. Site coordinates (sourced)
- Scott Base **77°50′57″S 166°46′06″E**, Pram Point, Ross Island, ~3 km from McMurdo Station by road. https://en.wikipedia.org/wiki/Scott_Base
- McMurdo Station **77°50′47″S 166°40′06″E**, southern tip of Ross Island. https://en.wikipedia.org/wiki/McMurdo_Station
- Ross Island **77°30′S 168°00′E**, east side of McMurdo Sound, ~43 nm N–S. https://en.wikipedia.org/wiki/Ross_Island
- Antarctica New Zealand gives Scott Base at **77° 51′ S, 166° 46′ E** and "**3800km south of Christchurch and 1350km from the South Pole**". https://www.antarcticanz.govt.nz/scott-base *(official; matches the great circle below to within 0.7%)*
- Solar time (computed): 166.77°E ÷ 15 = 11.1 h, so the site's *solar* offset is UTC+11, as stated in the brief. (Terra Nova Bay: 164.1°E ÷ 15 = 10.9 h, also UTC+11. Christchurch 172.64°E ÷ 15 = 11.5 h; Hobart 147.3°E ÷ 15 = 9.8 h, i.e. solar UTC+10.) *Computed only; no legal-time source was fetched.*

#### S-B. Distances (great circle, computed from the coordinates in §A; nm = km ÷ 1.852)

| Origin | to Scott Base | to McMurdo | to Cape Adare (71°17′S 170°14′E) | to Antarctic Circle at 170°E (66°33′S) |
|---|---|---|---|---|
| **Christchurch** | 3,825 km / 2,065 nm / 2,377 mi | 3,825 km | 3,089 km / 1,668 nm | 2,565 km / 1,385 nm |
| **Lyttelton** | 3,818 km / 2,061 nm | 3,818 km | 3,081 km / 1,664 nm | 2,557 km / 1,381 nm |
| **Hobart** | 3,985 km / 2,152 nm | 3,984 km | 3,398 km / 1,835 nm | 2,969 km / 1,603 nm |
| Bluff | 3,475 km / 1,877 nm | 3,475 km | 2,747 km / 1,483 nm | 2,221 km / 1,199 nm |
| Invercargill | 3,496 km / 1,888 nm | 3,496 km | 2,767 km | 2,241 km |
| Port Chalmers (Dunedin) | 3,566 km / 1,925 nm | 3,566 km | 2,832 km | 2,306 km |
| Wellington | 4,082 km / 2,204 nm | 4,082 km | 3,345 km | 2,824 km |
| Auckland | 4,575 km / 2,470 nm | 4,575 km | 3,838 km | 3,317 km |
| Macquarie Island (for reference) | 2,600 km / 1,404 nm | 2,599 km | 1,931 km | 1,453 km |

- **Cross-check 1 (printed):** AirportDistanceCalculator.com prints Christchurch–McMurdo **3,825 km (2,377 mi)** (via a Brave snippet; page not opened). Identical to the computed figure.
- **Cross-check 2 (official, route):** Christchurch Airport and Antarctica NZ both state "**about 3,920km by air from Christchurch**" for Scott Base/McMurdo — that is a *flown route* figure and is 2.5% longer than the great circle; the two are consistent. https://www.christchurchairport.co.nz/about-us/who-we-are/gateway-to-antarctica/ and https://adam.antarcticanz.govt.nz/nodes/view/34390
- **Cross-check 3 (Wikipedia):** McMurdo article: "about 3,920 kilometres (2,440 mi) away by air" from Christchurch Airport. https://en.wikipedia.org/wiki/McMurdo_Station
- **Cross-check 4:** Ross Dependency article: "roughly 2,000+ km south of New Zealand" (loose, to the Dependency boundary at 60°S, not to Ross Island). https://en.wikipedia.org/wiki/Ross_Dependency
- **Lyttelton to the Ross Sea ice edge:** the ice edge moves every season and **no source for its summer position at 170°E was obtained** (the Wikipedia "Antarctic sea ice" page gives only the hemispheric extent, ~18 million km² in September and ~3 million km² in February). The Antarctic Circle row above (66°33′51″S, per https://en.wikipedia.org/wiki/Antarctic_Circle) is a *fixed reference line*, not the ice edge. **Open thread.**

#### S-C. Flight and sailing times
- **By air (official):** "It takes five hours to fly in a US Air Force C-17 Globemaster or seven hours in a US Air Force Hercules LC-130" (Christchurch Airport page above). Antarctica NZ's ADAM node 34390 states the same: ~5 h C-17, ~7 h C-130 (it says "RNZAF C-130 Hercules"). A Brave snippet attributed to LEARNZ gives C-17 average 5 h, C-130 average 7 h (page not opened → treat as a snippet only).
- **Historical air-time, for context:** "In 1955 ... eight US Air Force aircraft made the 14-hour flight from Harewood Airfield to McMurdo Station" (Christchurch Airport page above).
- **By sea:** *no scheduled-voyage time was obtained for Lyttelton to McMurdo or Scott Base.* Partial data points:
  - **Heritage Expeditions** (New Zealand operator; Brave snippet quoting its trip reports; pages not opened): the standard Ross Sea expedition, embarking at **Bluff**, runs **28 days**; one such voyage logged **4,942.3 nautical miles** (~9,153 km) over those 28 days, including The Snares, Auckland Islands, Macquarie Island and Campbell Island; return from the Ross Sea to **Campbell Island** was "three to four days" (one report: 700 nm from Campbell Island on the evening before arrival). These are *round-trip itinerary totals with stops*, not a transit time.
  - **Polar Star data point (discarded as a transit figure):** Wikipedia says Polar Star "took the Green Wave in tow and proceeded on a 12-day 1,515 mile transit to Lyttelton" from off Cape Adare (Feb 1998). A statute-mile figure of 1,515 (= 1,316 nm) is *shorter* than the great circle from Cape Adare to Lyttelton (1,664 nm), so the position, the unit, or the start point is not as stated; this is a tow at tow speed and is **not used**. https://en.wikipedia.org/wiki/USCGC_Polar_Star
  - **Computed only (not sourced):** Lyttelton–McMurdo 2,061 nm = 8.6 days at 10 kn, 7.2 days at 12 kn, 6.1 days at 14 kn, ice excluded. Hobart–McMurdo 2,151 nm = 9.0 / 7.5 / 6.4 days at the same speeds. (Nuyina's stated top speed is 16 kn, https://en.wikipedia.org/wiki/RSV_Nuyina, so 12–14 kn is plausible cruising.)
- **Ross Sea cruise lengths (Brave snippet only):** operators advertise Ross Sea cruises of "24 to 34 days" (Aurora Expeditions blog text, quoted in a snippet); examples listed: 24, 26 (Hobart→Dunedin aboard Greg Mortimer), 27 and 28 days. A Divergent Travelers snippet: "even after you cross [the Antarctic Circle], you're still a solid two days away from reaching Cape Adare." Cape Adare is not Ross Island, so this is not a transit time to the site.

#### S-D. Populations (sourced)
- **Christchurch:** "urban population of 407,800, and a metropolitan population of 556,500"; "As of June 2025, Christchurch City had an estimated population of 419,200 residents across ... 1,415.15 km²". Largest city on the South Island; second-largest urban area in NZ. https://en.wikipedia.org/wiki/Christchurch *(the page uses 407,800 for "urban" and 419,200 for "city/territorial authority"; do not mix.)*
- **Canterbury region:** 698,200 (June 2025), 13.1% of NZ; Christchurch ≈ 58% of it. https://en.wikipedia.org/wiki/Canterbury,_New_Zealand
- **Lyttelton (town):** 3,220 (June 2025), 43°36′S 172°43′E, ~12 km from Christchurch via the road tunnel; handled 34% of South Island exports and 61% of imports by value; berthed Discovery, Nimrod and Terra Nova. https://en.wikipedia.org/wiki/Lyttelton,_New_Zealand
- **Dunedin:** urban area ~104,000; territorial ~132,800 (June 2025). https://en.wikipedia.org/wiki/Dunedin · **Port Chalmers** 1,400 (June 2025), 45°49′04″S 170°37′08″E; staging port for Scott (Discovery 1901, Terra Nova 1910), Shackleton, Byrd (1928), Ellsworth (1933). https://en.wikipedia.org/wiki/Port_Chalmers
- **Invercargill:** urban ~51,200; Southland region 104,800 (June 2025). https://en.wikipedia.org/wiki/Invercargill · https://en.wikipedia.org/wiki/Southland_Region · **Bluff** 1,840 (June 2025), 46°36′S 168°20′E, "the main gateway for New Zealand ships heading down to the Antarctic" (Wikipedia's wording). https://en.wikipedia.org/wiki/Bluff,_New_Zealand
- **Wellington** urban ~209,800, metro 433,900; **Auckland** urban ~1,547,200 (June 2025). https://en.wikipedia.org/wiki/Wellington · https://en.wikipedia.org/wiki/Auckland
- **Hobart** (the claim names Hobart in the brief): Greater Hobart 254,930 (2024); coordinates 42°52′50″S 147°19′30″E. https://en.wikipedia.org/wiki/Hobart

#### S-E. "Is nearest populous accurate?" — reading the numbers
1. **Nearest of all the places named in the brief, by great circle to Ross Island:** Bluff (3,475 km), Invercargill (3,496), Port Chalmers/Dunedin (3,566), then **Christchurch (3,825)**, Lyttelton (3,818), Hobart (3,985), Wellington (4,082), Auckland (4,575). Christchurch is *not* the nearest populated place to Ross Island; it is ~270–350 km farther than the Southland/Otago coast.
2. **If "populous" is set at a city of about 100,000:** Dunedin (urban ~104,000) is nearer. **At 200,000 or more:** among the places measured, Christchurch (419,200) is the nearest, with Hobart (254,930) at 3,985 km and Wellington (209,800) at 4,082 km farther. So the claim is true only with a threshold that excludes Dunedin and is higher than ~105,000. *(Only the places listed above were measured; towns on the Australian south coast, Pacific islands and Chile/South Africa were not computed for Ross Island and are plainly farther: Honolulu is 11,259 km from Scott Base.)*
3. **Chile and South Africa:** not computed against coordinates (their coordinates were not fetched); the brief rules them out and the Antarctic gateway article (below) places them on other sides of the continent. *No distance claimed.*
4. **Fiji and other Pacific islands:** **not researched** (no coordinates fetched); open thread.
5. **Timing of the advantage:** Wikipedia's Christchurch page states the city "has been recognised as an Antarctic gateway since 1901, and is nowadays one of the five Antarctic gateway cities hosting Antarctic support bases for several nations." https://en.wikipedia.org/wiki/Christchurch

#### S-F. Context (b) ONLY — which programs actually use which gateway (NOT an input to the basis)
- *Label: historical/operational fact about today's traffic, not geography.* Christchurch Airport: "the base for all Antarctic flights operated by the United States Navy, the United States Air Force, the United States Air National Guard, and the Royal New Zealand Air Force as part of Operation Deep Freeze." https://en.wikipedia.org/wiki/Christchurch_Airport · the Airport's own page: "around 100 direct flights a year ... more than 5,500 passengers and 1,400 tonnes of cargo" (see link in S-C).
- The Wikipedia "Antarctic gateway cities" article lists five gateways (Punta Arenas, Ushuaia, Cape Town, Hobart, Christchurch); Christchurch serves NZ, US, Italy, South Korea; "offers almost no commercial travel to Antarctica." https://en.wikipedia.org/wiki/Antarctic_gateway_cities
- Ross Dependency: "from 160° east to 150° west", claimed by New Zealand since the 1923 Order in Council; claims are in abeyance under the 1961 Antarctic Treaty; Scott Base is operated by New Zealand. https://en.wikipedia.org/wiki/Ross_Dependency *(A territorial claim is political, not geographic; listed as context only.)*
- Lyttelton "was the base for seven supporting United States Navy vessels" in 1955 and "continues supporting resupply missions today" (ADAM node 34390, above).

#### S-G. Exact search strings used for SCOTT
*(Brave through `WebFetch` unless stated; WebSearch refused all four of its calls.)*
1. WebSearch (refused, budget): `Christchurch to McMurdo Station distance km flight time C-17` · `Lyttelton to McMurdo Sound nautical miles icebreaker transit days` · `Hobart to Terra Nova Bay distance nautical miles Mario Zucchelli Station voyage L'Astrolabe` · `Hobart to Ross Sea voyage days distance km Aurora Australis or tourist expedition`
2. `Christchurch to McMurdo Station flight time hours distance km` (Bing; died at the **sources**: returned only Christchurch tourism pages)
3. `Christchurch McMurdo flight "hours" C-17 distance km Antarctic flight time` (Brave; worked)
4. `christchurchairport.co.nz Antarctic gateway "five hours" C-17 McMurdo` (Brave; worked)
5. `Bluff to Ross Sea voyage Heritage Expeditions days nautical miles Campbell Island` (Brave; worked)
6. `Ross Sea expedition cruise from Hobart Tasmania days at sea to Cape Adare itinerary` (Brave; worked)
7. `Hobart to McMurdo distance km nautical miles` (Brave; worked, returned only generic calculators)
8. `learnz Boeing C-17 Globemaster average flight time 5 hours Christchurch McMurdo` (Brave; **died at the query/tool**: HTTP 429)
9. `Polar Star icebreaker Lyttelton to McMurdo transit days`, `icebreaker departed Lyttelton New Zealand arrived McMurdo Sound days transit`, `Lyttelton to McMurdo Station ship voyage takes days` (Brave; HTTP 429 each time)

#### S-H. Dead ends (and where each died)
- **Scheduled sea-transit time Lyttelton→McMurdo/Scott Base** — died at the **query layer** (search tool rate-limited, Bing returned an empty template). Official pages fetched (Antarctica NZ "travelling-to-antarctica", Scott Base page, Wikipedia Scott Base, Wikipedia HMNZS Aotearoa, NZDF home) contain no such figure: died at the **sources** for those pages.
- **USAP pages** (`usap.gov/logisticsandoperations/` HTTP 404; `usap.gov/travelanddeployment/` navigation only) — **sources**.
- **timeanddate.com distance pages** (n=1032, n=396) — HTTP 403 — **sources/tool**. AirportDistanceCalculator guess-URLs — HTTP 404 — **query** (URL pattern guessed wrong).
- **Lyttelton Port Company home page** (lpc.co.nz) — no Antarctic content — **sources**.
- **The Press article on Christchurch's gateway economics** — page body not returned — **sources/tool**.
- **DVIDS article** (Nov 14, 2024) — fetched, but the extraction had no distance/time/program list — **sources** (only the "one of five global gateway cities" line).
- **Ross Sea ice-edge latitude in summer** — Wikipedia "Antarctic sea ice" has no regional figure — **sources**; no NSIDC page was reached — **query**.
- **Heritage Expeditions pages** (`/expeditions/in-the-wake-of-scott-shackleton/`, `/destinations/ross-sea/`) — HTTP 404; the home page confirms Ross Sea voyages depart "from New Zealand" — **query** (URLs guessed).

#### S-I. Single-source items
- 4,942.3 nm / 28 days and the Campbell Island legs: one Brave snippet summary of Heritage Expeditions trip reports (not opened).
- Ross Sea cruise lengths 24–34 days: snippets of operator/agent pages (not opened).
- "Five hours / seven hours": **two official pages that agree** (Christchurch Airport and Antarctica NZ ADAM) plus a LEARNZ snippet — treat as verified.
- "3,800 km south of Christchurch": **one** official page (Antarctica NZ), matched by the computed 3,825 km and the AirportDistanceCalculator printed figure — treat as verified.

#### S-J. Open threads
1. A sourced **sea-route** distance and transit time for Lyttelton→McMurdo (ideally from a US/NZ vessel log or the Heritage Expeditions trip reports).
2. A sourced **typical summer ice-edge latitude** near 170°E–180° for a "to the ice edge" figure.
3. **Fiji and Pacific islands** not measured.
4. Whether "Canterbury coast" should read as Christchurch **plus** Lyttelton plus the 698,200-person region: sourced here, but a one-clause wording choice for the developer.

---

### ZUKELLI — Terra Nova Bay, Victoria Land (~74°42′S 164°07′E)

**Claim (as written):** *"Terra Nova Bay is reached by a Southern Ocean run from Tasmania (Hobart); Australia is the nearest of the developer's shortlist (Hawaii, Mongolia, Taiwan, Indonesia, Australia) to Terra Nova Bay."*

#### Z-A. Site coordinates (sourced)
- **Mario Zucchelli Station 74°41′39″S 164°06′50″E**, 15 m above sea level on a granitic headland; seasonal, mid-October to mid-March. https://en.wikipedia.org/wiki/Mario_Zucchelli_Station
- Terra Nova Bay "74°50′S 164°30′E", ~40 nm (74 km) long between Cape Washington and the Drygalski Ice Tongue; coastal polynya (katabatic winds off the David, Reeves and Priestley glaciers); three stations: Zucchelli (Italy), Jang Bogo (South Korea), Qinling (China, Inexpressible Island, opened 2024). https://en.wikipedia.org/wiki/Terra_Nova_Bay
- Jang Bogo Station 74°37′26″S 164°13′44″E. https://en.wikipedia.org/wiki/Jang_Bogo_Station · Gondwana Station 74°38′07″S 164°13′19″E (German, seasonal). https://en.wikipedia.org/wiki/Gondwana_Station · Qinling Station 74°56′04″S 163°42′55″E. https://en.wikipedia.org/wiki/Qinling_Station
- Ross Sea (Wikipedia): between Victoria Land and Marie Byrd Land; "637,000 square kilometres" (NIWA); McMurdo Sound "usually free of ice during the summer". https://en.wikipedia.org/wiki/Ross_Sea

#### Z-B. Distances to Terra Nova Bay (great circle, computed to Zucchelli at 74°41′39″S 164°06′50″E; coordinates sourced as in §A)

| Origin | km | nm | statute mi |
|---|---|---|---|
| **Hobart** | **3,636** | **1,963** | 2,259 |
| **Christchurch** | **3,491** | **1,885** | 2,169 |
| Lyttelton | 3,484 | 1,881 | 2,165 |
| Bluff | 3,131 | 1,690 | 1,945 |
| Invercargill | 3,151 | 1,702 | 1,958 |
| Port Chalmers (Dunedin) | 3,227 | 1,742 | 2,005 |
| Wellington | 3,754 | 2,027 | 2,333 |
| Auckland | 4,246 | 2,293 | 2,638 |
| Macquarie Island (Tasmania, Australia) | 2,243 | 1,211 | 1,393 |

- **Hobart to Qinling Station (74°56′S 163°43′E): 3,656 km / 1,974 nm; Christchurch to Qinling: 3,520 km / 1,900 nm** (computed).
- **To the west coast of the Ross Sea (Cape Adare 71°17′S 170°14′E):** Hobart 3,398 km / 1,835 nm; Christchurch 3,089 km / 1,668 nm (computed). **To McMurdo/Ross Island:** Hobart 3,984 km / 2,151 nm; Christchurch 3,825 km / 2,065 nm.
- **Hobart – Christchurch** (computed): 2,045 km / 1,104 nm (matches "direct route passage is around 1100 nautical miles" for Australia→NZ, a cruising-wiki snippet at cruiserswiki.org/wiki/Australia_to_New_Zealand, not opened).
- **Hobart − Christchurch gap to Terra Nova Bay: 145 km = 4.1%; to Ross Island: 159 km = 4.2%; to Cape Adare: 310 km = 10.0%.**
- **German Wikipedia states** the station is "roughly 3,200 km from Christchurch and Lyttelton"; the computed great circle is ~3,490 km. **Discrepancy of ~290 km; the German figure is the source's own and is unexplained.** https://de.wikipedia.org/wiki/Mario-Zucchelli-Station *(single source, rounded, disagrees with computation.)*
- **Route vs. great circle:** the great circle Hobart→Terra Nova Bay passes close to Macquarie Island (Hobart–Macquarie 838 nm + Macquarie–Terra Nova Bay 1,211 nm = 2,049 nm via the island, against 1,963 nm direct; computed), so a Hobart run to the bay is a Southern Ocean crossing roughly 6.5–8 days at 12–10 knots with no ice (computed; see §0 point 5).

**Hobart's own distances to Antarctica as printed by sources (these are to the Australian sector, not the Ross Sea; they show where Hobart's real pull is):**
- Casey **3,443 km**; Davis 4,838 km; Mawson 5,475 km; Macquarie Island 1,542 km; Heard Island 5,398 km. Australian Antarctic Program distances table. https://www.antarctica.gov.au/about-antarctica/geography-and-geology/geography/distances/ *(the same page, as extracted, lists no Ross Sea, McMurdo, Scott Base, Terra Nova Bay or Cape Adare distance: the Ross Sea is outside Australia's own station set.)*
- Wikipedia (Casey Station): "3,443 km (2,139 mi) from Hobart ... a four-hour flight from Hobart, followed by a four-hour ride in an over-snow bus." https://en.wikipedia.org/wiki/Casey_Station
- Wikipedia (Hobart): "approximately 2,200 kilometers (1,367 miles)" to Antarctica; Wikipedia (Tasmania): "about 2,500 kilometres south of the continent's George V Coast"; a Brave snippet of antarctic.tas.gov.au: "Hobart is closer to Antarctica (2610 km) than it is to Townsville (2625 km) or Perth (3021 km)." **These three do not agree with one another** (2,200 / 2,500 / 2,610 km) and each is to a different point on the coast; none is to Terra Nova Bay.
- Hobart's flight route to Antarctica per the sources seen goes to **Casey (Wilkins)**; **no Hobart–Ross Sea scheduled flight was found**.
- Hobart is the "home port for both Australian and French Antarctic operations" (Hobart article); "L'Astrolabe ... carries supplies and personnel to [Dumont d'Urville] from the port of Hobart" (Dumont d'Urville article). https://en.wikipedia.org/wiki/Dumont_d%27Urville_Station *(context (b), and neither is Ross Sea traffic.)*

#### Z-C. The shortlist — plain distances to Zucchelli (great circle, computed; coordinates sourced as in §A)

| Place | Coordinates used (source) | to Zucchelli, km | nm |
|---|---|---|---|
| **Australia: Hobart, Tasmania** | 42°52′50″S 147°19′30″E (Wikipedia) | **3,636** | **1,963** |
| Australia: Macquarie Island (Tasmania) | 54°38′S 158°52′E (Wikipedia) | 2,243 | 1,211 |
| Indonesia: Denpasar (Bali) | 8°40′18″S 115°14′02″E (Wikipedia) | 7,952 | 4,294 |
| Indonesia: Jakarta | 6°11′S 106°50′E (Wikipedia) | 8,426 | 4,550 |
| Hawaii: Honolulu | 21°18′N 157°51′W (Wikipedia) | 11,010 | 5,945 |
| Taiwan: Kaohsiung (southern) | 22°36′54″N 120°17′51″E (Wikipedia) | 11,258 | 6,079 |
| Taiwan: Taipei | 25°02′15″N 121°33′45″E (Wikipedia) | 11,499 | 6,209 |
| Mongolia: Ulaanbaatar (landlocked) | 47°55′19″N 106°54′55″E (Wikipedia) | 14,269 | 7,704 |

- **Reading:** on any point chosen within each place, Australia (Hobart or any Tasmanian point) is the nearest by a factor of about 2.2 to 3.9. **This half of the claim is SUPPORTED by the numbers.** The nearest Indonesian point is a Lesser Sunda or Java-coast point; the nearest Hawaiian point is the island of Hawaii (farther south than Honolulu; *not computed*) — neither can approach 3,636 km on any reading.
- Populations (context): Honolulu city 350,964 (2020), urban 853,252, metro 1,016,508; Taipei 2,494,813 (Mar 2023), Greater Taipei 7,047,559; Kaohsiung ~2.7 million; Jakarta city 11,010,514 (mid-2025); Denpasar 670,210 (2024); Ulaanbaatar ~1.79 million (2025); Greater Hobart 254,930 (2024). Wikipedia pages cited in §A.
- **Hawaii vs. Antarctica gateways (flag):** the sources seen do not list Honolulu, Taipei, Jakarta or Ulaanbaatar among the five Antarctic gateway cities (Punta Arenas, Ushuaia, Cape Town, Hobart, Christchurch). Not a geographic fact; context (b).

#### Z-D. Is New Zealand (Christchurch) much nearer than Hobart? — the numbers
- **Not "much" nearer by great circle: 145 km (4.1%) nearer to Terra Nova Bay.** To Ross Island 159 km (4.2%); to Cape Adare 310 km (10.0%).
- **The nearest populated New Zealand points are meaningfully nearer**: Bluff 3,131 km is **505 km (13.9%)** nearer than Hobart; Invercargill 485 km; Port Chalmers/Dunedin 409 km.
- **In populous terms:** Christchurch city 419,200 (Jun 2025; urban 407,800) vs Greater Hobart 254,930 (2024). *(Each number is its own; the two are not netted against each other here.)*
- **NZ's Ross Dependency (160°E–150°W)** contains Terra Nova Bay (164°E). That is a political claim under the 1961 Antarctic Treaty, listed as context only. https://en.wikipedia.org/wiki/Ross_Dependency

#### Z-E. Context (b) ONLY — who actually serves Terra Nova Bay today (NOT an input to the basis)
- **Italy (Zucchelli):** German Wikipedia: "Flights depart from Christchurch, New Zealand ... Ships operate from Lyttelton (near Christchurch), with the research vessel Laura Bassi handling supply missions." https://de.wikipedia.org/wiki/Mario-Zucchelli-Station *(single source; the Italian and English Wikipedia pages fetched give no port.)* Christchurch Airport's own page lists Italy among the nations hosted in Christchurch. The ADAM page: "The Antarctic air logistics operations of the US, Italy and New Zealand are staged through Christchurch Airport to McMurdo Sound."
- **South Korea (Jang Bogo):** "Materials were 'shipped from Busan to Lyttelton, New Zealand for transfer to the new Korean icebreaker, the RS Araon.' For air operations, the base relies on the ice runway operated by Zucchelli Station." https://en.wikipedia.org/wiki/Jang_Bogo_Station · RV Araon "left Christchurch, New Zealand on Jan. 12 ... began sailing toward Terra Nova Bay" (first foreign port of call: Lyttelton). https://en.wikipedia.org/wiki/RV_Araon
- **China (Qinling):** the Polar Research Institute of China operates Xue Long and Xue Long 2; the fetched pages **do not state which port** serves Qinling. **UNVERIFIED** (the page extraction's inference about Hobart was its own guess and is discarded). Wikipedia's gateway article says Hobart "services Australia, France, and China's national programs" generally, without reference to the Ross Sea.
- **Germany (Gondwana):** no logistics found.
- **Pattern (context only):** every Terra Nova Bay program for which a gateway was found (Italy, South Korea) uses **Christchurch/Lyttelton**, not Hobart. **No source seen shows a program that sails to Terra Nova Bay from Hobart.** (Absence in the pages reached is not proof of absence; see §D.)

#### Z-F. Verdict reasoning
1. *"Australia is the nearest of the shortlist"* — **SUPPORTED** (§C).
2. *"Terra Nova Bay is reached by a Southern Ocean run from Tasmania (Hobart)"* — **geographically true, but not the nearest populous coast, and not how the bay is served today.** Hobart is 3,636 km / 1,963 nm away; the whole South Island of NZ is nearer (Bluff 3,131 km up to Christchurch 3,491 km), and Christchurch/Lyttelton is the gateway the sources seen name for the bay's two documented national programs.
3. **A stronger gateway exists that the claim does not mention: New Zealand's South Island (Southland/Otago/Canterbury).** For a project that must pick a founding nation from the shortlist *only*, Australia remains the nearest *shortlisted* nation; the developer should know that the geography, taken alone, points to New Zealand.
4. **Australia-specific geography that stands on its own:** Macquarie Island (Tasmania, "approximately halfway between Tasmania and the Antarctic continent", 1,500 km from Hobart per Wikipedia / 1,542 km per the AAD) lies 2,243 km from Terra Nova Bay; Macquarie has "no permanent inhabitants" and a rotating research staff of "20 to 40 people". https://en.wikipedia.org/wiki/Macquarie_Island *(a possible Australia-side geographic foothold if the developer wants one; context, not a decision.)*

#### Z-G. Exact search strings used for ZUKELLI
(Brave through `WebFetch` unless stated)
1. WebSearch (refused): see §S-G.
2. `Hobart to Ross Sea voyage nautical miles` (Brave; worked: only generic calculators and a Tasmanian "Ross" town)
3. `Hobart to McMurdo distance km nautical miles` (Brave; worked: AAD distances page; travelmath's generic "Hobart to Antarctica" 5,758 km is a straight line to a **generic Antarctic point**, unusable)
4. `Hobart to Terra Nova Bay Antarctica distance` (Brave; worked: generic Antarctica pages; cruisecentres.com.au says Terra Nova Bay is accessible "by sea from Lyttleton, New Zealand and Hobart, Tasmania" — **page itself failed with an SSL error, snippet only**)
5. `Ross Sea expedition cruise from Hobart Tasmania days at sea to Cape Adare itinerary` (Brave; worked)
6. `Greg Mortimer Ross Sea Odyssey Hobart to Dunedin itinerary days at sea` (Brave; **HTTP 429**)
7. `Xuelong Ross Sea Qinling station departed Hobart arrived Terra Nova Bay days`, `Xuelong 2 Ross Sea Qinling Station Hobart departure`, `Terra Nova Bay Mario Zucchelli station how to reach Christchurch flight hours Italian ship Lyttelton days`, `Mario Zucchelli Station logistics Christchurch Lyttelton Italica Terra Nova Bay voyage`, `Araon Lyttelton Terra Nova Bay Jang Bogo days voyage Christchurch Korea Antarctic`, `Hobart Ross Sea voyage "days at sea" Cape Adare Tasmania Southern Ocean crossing` (Brave; **HTTP 429 each**, died at the **query/tool layer**)
8. `Hobart to Ross Sea Cape Adare days at sea nautical miles expedition ship` (Bing; empty template — **tool**)

#### Z-H. Dead ends (and where each died)
- **Hobart to Terra Nova Bay or to the Ross Sea west coast — a sourced distance by ship** — died at the **sources**: the AAD distances page omits the Ross Sea; the Hobart/Port of Hobart/Aurora Australis/Nuyina Wikipedia pages carry no Ross Sea route. The only numbers are the computed great circles.
- **Hobart-based Ross Sea cruise itinerary (Greg Mortimer, "Ross Sea Odyssey"; wildearth-travel.com page; Adventure Life page)** — the pages fetched were directory/nav pages or the wrong page: died at the **sources** (query for the exact itinerary page then rate-limited).
- **Aurora Expeditions' Ross Sea page** — redirect loop (>10 redirects) — **tool**.
- **Hobart–Terra Nova Bay flight** — none found; Hobart's flight route in the sources goes to Casey/Wilkins. **Sources.**
- **Qinling's gateway port** — **query** (rate-limited) and **sources** (Wikipedia silent).
- **PNRA logistics** — `pnra.aq` home page lacks the logistics text; `pnra.aq/en/logistics` 404; Italian Wikipedia page lacks it — **sources**. English Wikipedia titles `Italian_National_Antarctic_Program`, `Italian_Antarctic_Programme`, `Italian_Antarctic_Research_Programme`, `RV_Italica` — 404 (**query**, guessed titles); `Programma_Nazionale_di_Ricerche_in_Antartide` says only that PNRA "charters aircraft, helicopters, and a cargo/research ship" — **sources**.
- **ATS station catalogue** — 404 — **query**.
- **Korean Wikipedia (Jang Bogo)** — no routing — **sources**.

#### Z-I. Single-source items
- Italy's flights from Christchurch and ships from Lyttelton: **German Wikipedia only** (the Christchurch Airport and ADAM pages corroborate the Christchurch–Italy link at the airport level, not the ship port).
- "~3,200 km" (German Wikipedia) conflicts with the computed 3,490 km; do not use it.
- Cruisecentres.com.au "by sea from Lyttleton, New Zealand and Hobart, Tasmania": **snippet only** — the one source seen that names Hobart as a sea access to Terra Nova Bay, and it is an agent's port listing, not a program log.
- Macquarie Island staff "20 to 40 people": single page.
- Hobart–Antarctica distances (2,200 / 2,500 / 2,610 km): three sources, three answers.

#### Z-J. Open threads
1. A sourced list of **which programs and operators sail to Terra Nova Bay from which port** (Italy's ship logs; Korea's Araon voyage reports; China's Xue Long 2 voyage to Qinling; any Hobart-based Ross Sea cruise stopping in Terra Nova Bay).
2. A sourced **sea-route nm** Hobart–Terra Nova Bay.
3. Whether any Australian program (AAD) has ever worked in Terra Nova Bay or the Ross Sea west coast; not found.
4. Nearest **Hawaiian** point (island of Hawaii) and nearest **Indonesian** point (Rote/Sumba/Java south coast) to the bay — not computed; they cannot change the ranking.
5. Whether the developer's shortlist is *meant* to restrict the answer to Australia even though New Zealand is not on it (a ruling, not a research question).

---

## A. COORDINATES USED (all read during this run from the cited Wikipedia page unless stated)

Scott Base 77°50′57″S 166°46′06″E · McMurdo 77°50′47″S 166°40′06″E · Zucchelli 74°41′39″S 164°06′50″E · Qinling 74°56′04″S 163°42′55″E · Cape Adare 71°17′S 170°14′E · Balleny Islands 66°55′S 163°45′E · Macquarie Island 54°38′S 158°52′E · Christchurch 43°31′52″S 172°38′10″E · Lyttelton 43°36′S 172°43′E · Hobart 42°52′50″S 147°19′30″E · Bluff 46°36′S 168°20′E · Invercargill 46°24′47″S 168°20′51″E · Port Chalmers 45°49′04″S 170°37′08″E · Wellington 41°17′20″S 174°46′38″E · Auckland 36°50′57″S 174°45′55″E · Honolulu 21°18′N 157°51′W · Taipei 25°02′15″N 121°33′45″E · Kaohsiung 22°36′54″N 120°17′51″E · Jakarta 6°11′S 106°50′E · Denpasar 8°40′18″S 115°14′02″E · Ulaanbaatar 47°55′19″N 106°54′55″E · Antarctic Circle 66°33′51″S. (Wikipedia gave Dunedin no coordinates in the extraction; Port Chalmers stands for it, 13 km NE of the city centre.)

Computation script (not committed): haversine, R = 6,371.0088 km, 1 nm = 1.852 km, 1 mi = 1.609344 km.

## B. SURPRISING OR UNVERIFIABLE

1. **The Southland/Otago coast, not Canterbury, is the nearest populated NZ coast to both sites** (Bluff 3,475 km to Ross Island, 3,131 km to Terra Nova Bay; Christchurch 3,825 and 3,491). Christchurch's stronger case is scale (the only NZ city above ~200,000 that is also the airport and logistics base) and tradition, not proximity.
2. **The Hobart–Christchurch gap is small (4%) to the two sites and widens (10%) toward the Ross Sea's west coast (Cape Adare).** The Southern Ocean run from Tasmania is almost the same length as the run from the South Island.
3. **Hobart's printed distance to Casey (3,443 km) and the computed distance to Terra Nova Bay (3,636 km) are within 6% of each other**, and Davis (4,838 km) and Mawson (5,475 km) are farther. Terra Nova Bay is therefore not unusually remote from Hobart by the measure of Australia's own stations.
4. **Single discrepancy of note:** the German Wikipedia's "roughly 3,200 km from Christchurch and Lyttelton" for Zucchelli is ~290 km under the great circle; unexplained.
5. **The Polar Star "12-day 1,515 mile transit" from off Cape Adare to Lyttelton is internally inconsistent with the great circle** and was not used.
6. **Three Hobart-to-Antarctica distances disagree** (2,200 / 2,500 / 2,610 km) — a warning not to quote any "Hobart to Antarctica" figure without saying to which coast point.
7. **Not found at all:** any scheduled Hobart→Ross Sea ship or aircraft service by a national program. The Ross Sea cruise market (24–34 day itineraries) does list Hobart-departing voyages (Greg Mortimer, Hobart→Dunedin, 26 days) per snippets; the pages were not opened.
8. **Process note (for the log):** self-audit risk was handled by labeling every computed figure and by cross-checking three of them to printed values. The cross-checks all agreed to within 1%.

## C. WHAT WOULD CLOSE THE OPEN THREADS
A re-run with `WebSearch` available (budget reset) targeting: Heritage Expeditions trip reports 69, 162 and 340; the Korean Polar Research Institute's Araon voyage logs (Lyttelton→Terra Nova Bay days); PNRA's Laura Bassi voyage reports; PRIC / Xinhua reporting on Xue Long 2's 2023–24 Qinling voyage ports; USAP or Antarctica NZ vessel-resupply pages for Lyttelton→McMurdo days; NSIDC/AAD Ross Sea ice-edge climatology.

## D. REGISTER LINE FOR THE TRACKER (note: the "§D" referred to in §0 point 6 means the dead-end lists S-H and Z-H)
`Founding_Gateway_Research_B_Ross_Sea_2026-10-03.md` — SCOTT: Christchurch gateway PARTLY SUPPORTED (nearest city ≥ ~200,000; Southland/Otago ~270–350 km nearer). ZUKELLI: Australia nearest of the shortlist SUPPORTED (Hobart 3,636 km; next nearest shortlisted place 7,952 km); "reached from Hobart" PARTLY SUPPORTED (NZ South Island 145–505 km nearer; Italy and Korea use Christchurch/Lyttelton, context only). Sea-route times unsourced. WebSearch was budget-exhausted for this run.
