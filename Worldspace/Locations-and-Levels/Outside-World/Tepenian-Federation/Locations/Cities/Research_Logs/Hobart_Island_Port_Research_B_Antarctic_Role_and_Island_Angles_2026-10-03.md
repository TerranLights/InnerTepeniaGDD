# Hobart Island-Port Research, Part B: Antarctic Role and Island-Specific Angles

**Date:** 2026-10-03. **Scope:** real-world research (present-day Upper Earth) on whether Hobart's island setting makes it
specifically useful for a Tepenia-like society; Part B covers Hobart's established Antarctic role plus the island-specific,
strategic, regulatory and biosecurity angles. **Rules followed:** report evidence with sources; decide nothing; rank nothing;
candidate applications are stated flatly as possibilities. American English throughout (source titles that are British-spelled
proper nouns are paraphrased into American spelling per the project sweep rule).

Source-quality tags used below: **[P]** primary or official (government, treaty text, AAD schedule, port authority, ATS
document); **[S]** secondary but credible (ABC News, Polar Journal-type reporting, university companion); **[W]** read only through a
Wikipedia page by way of a fetch summary (single-source, treat as unverified unless a second source is named);
**[D]** derived by me from other figures (my arithmetic, labeled each time, not a published number).

---

## 0. Honest accounting

**Searches used.** 28 WebSearch calls returned results (several of them ran two or three sub-queries internally, so about 32
underlying queries). A further 4 WebSearch calls were **refused**: the session-wide WebSearch budget (500 calls, shared across
the whole session, not just this task) was exhausted partway through thread 3. I did not work around the limit by scraping a
search engine through the fetch tool. Everything after that point was done by opening known primary URLs directly (about 85
WebFetch or curl retrievals in total across the task). **The parent should know the 100-search budget was not the binding
constraint; the shared session cap was.**

**Source quality.**
- Strong, read in full: the Tasmanian Antarctic Gateway Strategy (State Growth, December 2017) as full text via a Wayback copy
  [P]; the AAD 2025-26 shipping and flight schedule, parsed row by row [P]; the AAD Initial Environmental Evaluation for RSV Nuyina
  operations (October 2024), searched as full text [P]; Annex II of the Madrid Protocol, Article 4, as full text [P]; the CEP
  Non-Native Species Manual (ATCM 40), as full text [P]; Biosecurity Tasmania's Fruit Fly Strategy 2022-2027 and Tasmanian
  Biosecurity Strategy 2023-2027, as full text [P]; four Tasmanian Government media releases via Wayback [P]; the BoM climate table
  for Hobart via Wayback [P].
- Good but read through a fetch summarizer: AAD web pages (distances, biosecurity requirements, cargo), TAAF L'Astrolabe page, CCAMLR
  page, ABC News items, AMSA and ASPI pages.
- Weak: anything attributed [W] (Wikipedia through a summarizer). Several fetch summaries were visibly wrong (the ABS page
  summary gave "Tasmania total 255,792," which is plainly a Greater Hobart or "rest of state" figure; the City of Hobart page summary
  mixed in Punta Arenas text; the IMAS page summary claims a 69,000 m2 building, which I do not trust and did not use). Those are
  flagged where they occur.
- **Access problem:** premier.tas.gov.au, antarctic.tas.gov.au, stategrowth.tas.gov.au, building.tas.gov.au, Serco, and the
  BoM site all returned HTTP 403 to the fetch tool and to curl. Wayback Machine copies fetched with curl recovered most of them.
  The fetch tool itself refuses web.archive.org, so Wayback only worked through curl.

**What is thin.** (a) Sea-level, storm-surge and Derwent-estuary exposure of the Hobart waterfront: no Hobart-specific
source was obtained (thread 5). (b) Naval, border-force and fisheries-patrol presence at Hobart: only fragments. (c) Hobart ship
repair and drydock capability: the one hard datum is negative (Nuyina's scheduled drydock is in Singapore). (d) Cold-storage
capacity and fuel-storage volumes: described, not quantified. (e) Whether bulk mainland cargo is ever staged through Tasmania
for Antarctica: **no evidence found in any source** (dead end at the sources, not the queries). (f) Japan's (and Norway's) port
use: not resolved. (g) Tasmanian supply-security reviews: not obtained because of the search cap.

---

## 1. Summary table

| # | Thread | Key sourced facts (numbers, source tag, where in section 2) | Candidate Tepenia applications suggested (possibilities, unranked) |
|---|---|---|---|
| 1 | Hobart's Antarctic role | AAD HQ in Kingston, about 300 staff [P/W]; CCAMLR Secretariat (27 Members + 10 acceding; Convention in force 7 Apr 1982) and ACAP Secretariat both in Hobart [P]; IMAS, CSIRO, BoM Antarctic office, SOOS, IMOS co-located; science agencies employ 620+ staff, 150+ postgraduates (2017) [P]; Tasmanian Polar Network 70+ members (2017), nearly 70 (2026) [P]; sector A$204M a year and almost 1,200 jobs (Mar 2026) [P]; 2017 Strategy: 0.7% of Tasmanian GSP [P]; AAD 2025-26: RSV Nuyina does 5 Hobart-based voyages plus trials, 13 flown Hobart to Wilkins Aerodrome flights (7 A319, 6 C-17) [P/D]; Hobart is "one of five" Antarctic gateways [P] | A-1, A-5, A-6, A-7, A-8, A-9, A-10, A-11, A-12, A-19, A-21 |
| 2 | Biosecurity | Purpose-built Cargo and Biosecurity Center (CBC) at Macquarie Wharf 2, opened April 2013, A$2.5M, vermin traps, fumigation, cold and cool storage, rodent-detector dogs [P]; Madrid Protocol Annex II Art. 4 (permit rule; food exemption with no live animals) [P]; CEP manual says prevention should concentrate at "gateways to Antarctica (ports, airports)" [P]; Tasmania is a statutory fruit-fly pest-free area, risk appetite set at "very low risk," methyl bromide treats about two-thirds of inbound host consignments that lack area freedom [P]; Medfly established in parts of WA, Qfly in eastern mainland [P] | A-1, A-2, A-3, A-14 |
| 3 | Strategic and political | 1924-34 Tasmanian secession agitation was driven by shipping grievances (Bass Strait ferry service, Navigation Act coastal provisions) and ended with the 1933 Grants Commission [S]; Freight Equalisation Scheme since July 1976 [W]; Basslink fault 21 Dec 2015 to 13 Jun 2016 [W]; Macquarie Island is a Tasmanian Nature Reserve, HIMI and the Antarctic Territory are Commonwealth, not Tasmanian [P/S]; AMSA's rescue center is in Canberra, not Hobart [P]; 2024 TasPorts-AAD wharf dispute and WA offer to host AAD [S/P]; Nuyina's 2024 crane failure [S] | A-12, A-13, A-17, A-18 |
| 4 | Staging node for others | France (IPEV, L'Astrolabe, 1,200 t cargo, 4-5 rotations a summer, about 2,700 km to Dumont d'Urville) [P]; China (MoUs 2013, 2019-expired; 5 pre-COVID calls, now mostly Fremantle) [P/S]; Korea's Araon each season for fuel and traverse gear [P]; Italy, Japan, US also visit [P]; up to A$2M per foreign icebreaker call [P]; no evidence of bulk mainland cargo staged via Tasmania. Computed great-circle distances: Hobart to Commonwealth Bay about 2,700 km versus 3,250 (Melbourne), 3,600 (Adelaide), 4,140 km (Bunbury) [D] | A-4, A-6, A-5, A-13 |
| 5 | Island-port physical facts | Hobart mean July minimum 4.6 C, so no harbor ice [P]; Tasman Bridge (46 m clearance [W]) blocks big ships upriver and blocks Nuyina from the Selfs Point fuel depot [P]; Nuyina therefore bunkers at Burnie (21-22 Sep, 26-27 Nov, 8-9 Feb) [P]; Greater Hobart about 255,000, roughly 40-45% of Tasmania [W/D]; Hobart port 1.6 Mt, 359 vessel arrivals, 1,730 containers (2023/24) [W]; Burnie about 5 Mt, Devonport 3-4 Mt [W] | A-13, A-15, A-20 |

---

## 2. Per-thread findings

### Thread 1. Hobart's established Antarctic role

**1.1 The national program and what Hobart carries**
- AAD headquarters are in Kingston, a suburb of Hobart; the head office has been in Tasmania since 1981; about 300 staff (June 2022)
  [W for Wikipedia AAD page; the 1981 date from a search summary of Wikipedia AAT/AAD pages; "operational base for the AAD" is
  repeated in the 2017 Strategy, p. 5 [P]].
- RSV Nuyina: delivered 19 Aug 2021 [W]; 1,200 t below decks in up to 96 twenty-foot containers; two 55 t knuckle-boom cranes; two
  barges of over 45 t each; 1.9 million L cargo fuel [P: antarctica.gov.au Nuyina cargo and resupply pages]; range 16,000 nm [P: IEE].
- **The AAD schedule for 2025-26** [P, parsed from the Wayback copy of
  https://www.antarctica.gov.au/antarctic-operations/travel-and-logistics/shipping-and-air-schedules/2526/ ]:

| Voyage | Depart Hobart | Back in Hobart | Purpose |
|---|---|---|---|
| VTRIALS | 4 Sep 2025 | 16 Sep 2025 | marine science trials (1 Sep load; 6-15 Sep at sea) |
| V1 | 26 Sep 2025 | 17 Nov 2025 | Casey fly-off, Heard Island campaign, Davis over-ice resupply, refuel and changeover |
| V2 | 25 Nov 2025 | 3 Feb 2026 | Casey resupply and refuel, moorings, Heard Island campaign |
| VR1 (French L'Astrolabe) | 13 Dec 2025 | 8 Jan 2026 | Macquarie Island, Dumont d'Urville (French program) |
| V3 | 10 Feb 2026 | 25 Mar 2026 | Mawson resupply and refuel, Davis summer retrieval |
| V4 | 2 Apr 2026 | 27 Apr 2026 | Macquarie Island resupply |
| V5 | from 30 Apr 2026 | (dry docking Singapore 28 Jun to 15 Sep 2026; Casey 8 Oct 2026) | per schedule |

  Turnarounds in Hobart between Nuyina voyages: 8 days (17-25 Nov), 7 days (3-10 Feb), 8 days (25 Mar-2 Apr) [D from the table].
- **Flights Hobart to Wilkins Aerodrome 2025-26** [P, my count of schedule rows]: 17 scheduled round trips (11 A319 numbered
  FSND010-110; 6 C-17 numbered FC17020-070); 4 A319 pairs marked cancelled (11 Nov, 16 Dec, 11 Feb, 16 Feb); so **13 not-cancelled
  round trips (7 A319, 6 C-17)** between 15 Nov 2025 and 6 Mar 2026. An earlier fetch summary said "about 15-20"; my parse of the
  rows gives the figures above. Wilkins: 3,200 m blue-ice runway about 65 km from Casey, A$46M, first flight 11 Jan 2008, flight about 4
  hours from Hobart, C-17 freight flights since 2015 [W]. The 2017 Strategy confirms an A319 serves both Wilkins and McMurdo and that
  RAAF C-17 freight flights from Hobart had begun [P].
- Per-voyage solid cargo into the stations [P: IEE, Oct 2024]: Davis 650-900 t a season; Casey 750-1,000 t; Mawson 200-290 t (sum
  1,600-2,190 t [D]). Return cargo ("RTA") is usually less than incoming. Fresh and frozen produce: about 52,000 kg a year and a
  A$1.3M catering budget (AAD Magazine, June 2017, via fetch summary, not read verbatim); mostly potatoes, carrots, apples and citrus;
  soft fruit avoided; eggs paraffin-sealed; packed in refrigerated containers with ozone generators [S].
- Transit figures, Hobart to station [P: IEE; second source: Nuyina first-voyage reporting]: Casey 1,848 nm in 7-11 days; Davis
  2,597 nm in 10-13 days; Mawson 2,956 nm in 12-16 days. **Unresolved conflict:** a fetch summary of the AAD "stations" page printed
  4-5, 6-7 and 7-8 days next to the same distance table; I could not find that text in a primary read and do not rely on it.
- Straight-line distances, AAD table [P] (km): Hobart to Casey 3,443; Davis 4,838; Mawson 5,475; Macquarie Island 1,542. Perth to
  Casey 3,837; Davis 4,736; Mawson 5,223; Heard Island 4,122. Melbourne to Casey 3,861; Davis 5,234. Adelaide to Casey 3,936;
  Davis 5,249. (URL: https://www.antarctica.gov.au/about-antarctica/geography-and-geology/geography/distances/ ). The table has **no
  entry for Dumont d'Urville or Commonwealth Bay**.

**1.2 Institutions and economy**
- **CCAMLR**: Secretariat at 181 Macquarie Street, Hobart; Convention opened 20 May 1980, in force 7 April 1982; 27 Members plus 10
  acceding states [P: https://www.ccamlr.org/en/organization/about-ccamlr ; W for the 1980 date]. The page does not say why Hobart.
- **ACAP** (albatross and petrel agreement): Secretariat at 119 Macquarie Street, Hobart; in force 1 Feb 2004; 13 parties [W].
- 2017 Strategy [P, full text, https://www.stategrowth.tas.gov.au/__data/assets/pdf_file/0019/164224/Tasmanian_Antarctic_Gateway_Strategy_12_Dec_2017.pdf
  via Wayback]: IMAS and many CSIRO climate researchers sit in purpose-built facilities on the Hobart waterfront; co-located are
  the ACE CRC, the international project office of the Southern Ocean Observing System (SOOS), the national IMOS office and an ARC
  Antarctic Gateway Partnership initiative; the BoM Antarctic office is in Hobart; RSV Investigator (Marine National Facility) is based there;
  science agencies employ **more than 620 staff**; **150+ postgraduates**. "Of the five recognized Antarctic gateways, Hobart is unique
  in its depth, breadth and combination of infrastructure, world class Antarctic scientific expertise and logistical support services."
- **Tasmanian Polar Network (TPN)**: "more than 70 businesses, research institutions and government agencies" (2017); "nearly 70
  organizations" (Mar 2026 release) [P]. Members supply scientific instrumentation, ship outfitting and **food provisioning**, technical
  and mechanical products, waste management, medical services, marine engineering; the Strategy states no other gateway hosts a
  comparable body. A Wayback read of the TPN member page lists a cold-storage and freight forwarder (Link Logistics), electrical and
  power-system firms, a construction firm, hose and lifting suppliers, a polar travel firm and CARMM; it did not show ship repair,
  clothing, fuel or stevedoring members, which does not prove their absence.
- Many national programs "source cold-climate products and services" from Tasmanian businesses: Australia, France, Italy, China, the
  United States, New Zealand, Korea, Russia, Japan [P, 2017 Strategy p. 14]. Traverse equipment design and manufacture is named as one
  example.
- **Economic value** [P, Tasmanian Government releases via Wayback]: 2017 Strategy: more than A$180M a year, 0.7% of GSP, 750+ direct
  and at least 430 indirect jobs; Antarctic Tasmania report (2020): about A$159M a year, almost 950 jobs, A$229M overall economic value,
  about 7,000 expeditioner nights; Oct 2024: more than A$183M, nearly 1,000 jobs; 2023-24 report (Nov 2025): public-sector real
  spending A$316.24M, **1,166 FTE** (about 0.5% of Tasmania's workforce), average wage A$162,164 versus A$93,795 for Tasmania; **Mar
  2026: more than A$204M a year, almost 1,200 jobs, over A$6M a year from expeditioners (about 16,000 nights), over A$3M a year from
  conference delegates.** The series are not one metric (contribution versus spending), so they are not strictly comparable.
- Each visit by another nation's icebreaker "inject[s] up to A$2 million" (City of Hobart page and Antarctic Tasmania [P/S]).
- Port: Tasmania's Hobart port has a dedicated Antarctic and cruise terminal at Macquarie Wharf 2, which also houses the AAD Cargo and
  Biosecurity Center; "Nuyina is berthed only 5 minutes from Hobart's city center" [P: antarctic.tas.gov.au gateway page via Wayback; antarctica.gov.au]. TasPorts lists for Hobart: 24/7 port
  availability, provedoring, stevedoring, quarantine, **secure expedition storage**, fuel bunkerage, common-user deep-water berths, a lay-up berth, tugs
  and pilotage [P: https://tasmanianpolarnetwork.com.au/members/tasports/ ]. (Note the fuel entry versus the Burnie bunkering in 4.2.)
- The 2017 Strategy (Goal 4) says sea-floor leveling at Macquarie Wharf 2 provides for year-round lay-up of the new icebreaker; the
  2016 Hobart Port Master Plan describes refueling and enhanced Antarctic logistics options there [P].
- Wharf politics: Oct 2024 Commonwealth and Tasmanian agreement, **A$188M over four years from the Commonwealth for a new Macquarie
  Wharf 6**, 30-year priority access for Nuyina, shoreside power, a refueling solution; construction from 2025 [P: premier.tas.gov.au 16
  Oct 2024; pm.gov.au]. Earlier TasPorts quoted A$515M over 30 years, called "exorbitant" by the federal Environment Minister;
  Wharf 6 suffers "concrete cancer" [S: ABC 2 Aug 2024, PS News 30 Jun 2024].
- The AAD's own 2022 strategy summary states the aim to "reinforce Hobart's position as the premier gateway to East Antarctica" [P].
- Antarctic Gateway Campaign: launched Aug 2024; A$1.4M over four years to 2028; March 2026 industry prospectus [P].

**Search strings (thread 1):** "Hobart Antarctic gateway Tasmanian Government Antarctic and Southern Ocean strategy economic value";
"Antarctic sector Tasmania economic contribution $ million jobs Antarctic Southern Ocean sector Hobart"; "Hobart Antarctic season
2025-26 ships Nuyina Aurora Australis Hobart wharf Macquarie Point Antarctic precinct"; "Australian Antarctic Division Kingston Tasmania
headquarters staff Nuyina resupply Casey Davis Mawson voyages 2025-26"; "Hobart to Casey Davis Mawson station distance kilometers days
voyage Nuyina travel time from Hobart Antarctic stations"; "Italian Antarctic program PNRA Laura Bassi Hobart Mario Zucchelli Station
Terra Nova Bay Hobart port logistics". **Dead ends:** query found, source blocked (403) for the Tasmanian Government pages, recovered by
Wayback; Macquarie Point Wikipedia page contained no precinct detail, so the precinct's current status is **open**.

### Thread 2. Biosecurity

**2.1 Antarctic rules (treaty and national)**
- Protocol on Environmental Protection (Madrid Protocol): signed 4 Oct 1991, in force 14 Jan 1998; 58 Treaty parties, 29 consultative [W];
  Annex II (fauna and flora) governs introductions [P].
- **Annex II, Article 4, text read in full** [P, https://iaato.org/sites/default/files/Environmental-Protocol.pdf ]: (1) no species not
  native to the Treaty area may be introduced except under permit; (2) dogs not to be introduced; (3) permits only for species in
  Appendix B; (4) permitted organisms must be removed or incinerated before the permit expires, and any other non-native organism
  introduced "shall be removed or disposed of, by incineration or by equally effective means, so as to be rendered sterile"; (5)
  nothing in the Article applies to food imports provided **no live animals are imported for this purpose and all plants and animal parts and products are
  kept under carefully controlled conditions** and disposed of under Annex III and Appendix C; (6) each Party must require precautions against
  introducing micro-organisms. (A fetch summary had misdescribed this as a poultry clause; the text above is the primary reading.)
- **CEP Non-Native Species Manual** [P, https://documents.ats.aq/ATCM40/att/atcm40_att056_e.pdf , read as text]: Prevention principle 5:
  "Prevention should focus on pre-departure measures within the logistics and supply chain: at the point of origin outside Antarctica (e.g., cargo, personal gear,
  packages), at gateways to Antarctica (ports, airports), on means of transport (vessels, aircraft), at Antarctic stations and field camps." Guidance
  lines: check cargo clean of soil, mud, vegetation and propagules before loading; confirm vessels rodent-free before departure; pack, store and load cargo
  on a clean sealed surface (bitumen or concrete) remote from waste ground; food and food wastes strictly managed; reference to COMNAP and SCAR 2010
  checklists for supply chain managers and ATCM XXXV WP 06 on fresh fruit and vegetables.
- COMNAP/SCAR note that meat is generally supplied frozen and long-term storage at -20 C likely kills most introduced macro-organisms; fresh foods
  include fruit, vegetables and eggs [S, search result summary of ATS documents; not read in the primary].
- **AAD requirements** [P, https://www.antarctica.gov.au/antarctic-operations/travel-and-logistics/cargo-and-freight/biosecurity/ ]: three measures:
  external surface inspection; internal inspection with internal fogging of cargo transport units; external inspection and fogging of containers and break-bulk.
  Biosecurity risk material: animals and traces, insects and traces, plant material (seeds, leaves, bark, straw), dirt, soil, fungi, mold, pooled water.
  Prohibited: polystyrene beads or chips, radio-isotopes, pesticides, unless permitted. The Kingston warehouse and the CBC run an ongoing pest-control program
  with fogging and rodent dog-detection.
- **The Hobart facility** [P]: AAD Cargo and Biosecurity Center at the eastern end of the redeveloped Macquarie Wharf 2 shed; opened April 2013; A$2.5M
  federal funding inside a A$7M TasPorts redevelopment; vermin traps, impenetrable walls, automatic shutter doors, **cold and cool storage units**, a fumigation
  area, briefing rooms, warehousing, and a cruise-terminal side (https://www.antarctica.gov.au/magazine/issue-24-june-2013/in-brief/new-biosecure-hub-for-antarctic-gateway/ ).
  The IEE (Oct 2024) says the CBC "complies with standards required for Approved Arrangements" under the Commonwealth biosecurity system, that cargo is quarantined at AAD
  head office and the CBC before loading, that Nuyina carries rat guards for berthing lines, holds a Lloyd's Register ECO(BIO) notation, has a biofouling plan with annual
  hull inspection before the first voyage of a season, a hull-scrubbing robot if needed, and a docking every five years. The IEE also names the Hobart loading of
  "cargo, equipment, stores and personnel" as itself a potential introduction route.
- Policy effectiveness [S, ARC SAEF summary of a century of data]: on sub-Antarctic islands, introduction rates stayed steady or fell after biosecurity policies despite
  more visitors; the Antarctic Peninsula shows rising introductions; prevention is far cheaper than cure; removing invasive species from Macquarie Island cost about A$25M.
  A Cambridge paper title (psychrotolerant fungi on wooden cargo packaging) exists; its abstract was **not** retrieved (open thread).

**2.2 Tasmania's island regime**
- **Strategy documents** [P, read as text]: Tasmanian Biosecurity Strategy 2023-2027: "Tasmania has significant regional benefits in terms of its biosecurity
  status, being an island, largely free of many terrestrial and marine pests and diseases... However, we cannot rely on our relative isolation." Appropriate Level of
  Protection set at "very low risk"; matter that fails is "restricted" (import conditions) or "prohibited" (https://nre.tas.gov.au/Documents/Tasmanian%20Biosecurity%20Strategy%202023-2027.pdf ).
- Fruit Fly Strategy 2022-2027 [P, https://nre.tas.gov.au/Documents/Fruit%20Fly%20Strategy_2022.pdf ]: all of Tasmania is a pest-free area for Queensland fruit fly (Qfly) and
  Mediterranean fruit fly (Medfly); "All fruit fly host material must be free of fruit fly before it is shipped to Tasmania"; high-risk produce checked by a specialist team in Victoria;
  clearance checks in Melbourne; checks at embarkation on TT-Line ferries; uniformed officers and detector dogs at ports and airports aiming at 100% inspection of air passengers;
  parcels screened; about 1,100 traps; methyl bromide fumigation "used to treat about two-thirds of all such inbound consignments" where area freedom is not available; fruit-fly host exports
  about A$40M (2019-20). Climate: "conditions for permanent establishment of Qfly and Medfly on the Tasmanian mainland are likely to be seen from the 2040s onward."
- 2018 incursion [S, ABC]: Qfly detected January 2018 (Flinders Island, Spreyton, George Town); control zones lifted 9 Jan 2019; Tasmania spent about A$5.5M on the response and
  received A$20M federal funding; international recognition was still pending in February 2019. A 2024 detection (mango larvae at Devonport, plus one male fly in a Launceston trap) rests
  on a single search summary [single-source]. Medfly is established in parts of Western Australia and Qfly in eastern mainland Australia [P: Biosecurity Tasmania fruit fly page].
- Securing Our Borders program announced May 2019; targeted inspections of high- and medium-risk produce each October to March [P: preventfruitfly.com.au].
- **Direction of friction.** Everything above restricts mainland host produce *entering* Tasmania. I found **no source** describing whether sealed cargo destined only for
  Antarctica and transiting Tasmanian ports is exempt or subject to Tasmanian import conditions. The AAD cargo pages treat Hobart as a screening point; they do not mention Tasmanian
  import rules.
- Is the island setting an advantage for screening cargo bound for a sensitive environment? Sources say (a) Tasmania itself is a low-pest environment, so the starting
  pest load of cargo staged there is lower than on the mainland [S/P, the Tasmanian strategies' own claim]; (b) the treaty manual says screening should occur at "gateways"; (c) the IEE and CEP manual
  treat any transport hub as a possible stepping stone [P]. No source states the island setting is an advantage for Antarctic screening as such; the inference is mine.

**Search strings (thread 2):** "Antarctic Cargo and Biosecurity Center Macquarie Wharf 2 Hobart AAD cargo inspection non-native species"; "Tasmania fruit fly free status outbreak
Queensland fruit fly Spreyton 2018 Hobart eradication declared"; "Tasmania Biosecurity Act 2019 fruit fly 2024 detection Tasmania incursion Biosecurity Tasmania Spirit of Tasmania quarantine checks";
"Antarctic Treaty Protocol Environmental Protection Annex II non-native species Manual of non-native species cargo food fresh produce Antarctica COMNAP"; "Annex II Article 4 Protocol
Environmental Protection "no live poultry" "fresh foods" introduction non-native species Antarctic Treaty text"; "COMNAP SCAR checklists supply chain managers reduce risk non-native species
introductions Antarctica cargo food fresh produce"; "Australian Antarctic Division biosecurity cargo packing requirements clean cargo Antarctica Hobart quarantine inspection rodents seeds";
"Tasmania island biosecurity advantage Biosecurity Tasmania strategy "island state" pest free status value export Hobart port ship inspections". **Dead ends:** the Madrid Protocol Annex II PDF at ncaor.gov.in
(certificate error) and at documents.ats.aq (redirect to a not-found page) died at the source; the IAATO copy worked. premier.tas.gov.au "Fly home without fruit fly" (403). Biosecurity Tasmania import-conditions
page guessed URL returned 404 (the "in-transit goods" question is therefore open).

### Thread 3. Strategic and political

- **Secession history** [S, Companion to Tasmanian History (Petrow) via Wayback; W for Wikipedia]: talk of secession in the 1920s-30s was anti-federal feeling; in 1924 "anti-federal feeling over
  deleterious shipping arrangements" led businessman Thomas Murdoch to move for secession; the Tasmanian Rights League (1925) sought "justice" or secession, with "justice" defined as an efficient
  ferry service across Bass Strait, exemption from the coastal provisions of the Navigation Act, and financial stability for small states; petition of 10,429 signatures (1926); the Hobart Chamber
  of Commerce and the Mercury newspaper supported it; the 1933 Commonwealth Grants Commission and its first award (A$290,000 for 1934-35) "dealt [sentiment] an effective blow." From the 1970s to the 1990s proposals
  surfaced "sometimes linked to the advantages of duty free status, but few took them seriously"; the First Party of Tasmania formed in the 1990s [W]. **No current separatist movement was found.**
- **Freight subsidy** [W]: Tasmanian Freight Equalisation Scheme since July 1976 (after the Nimmo Report); about A$100M paid in 2010-11; A$200.12M over 18 months in 2016-17; A$700 a container
  subsidy for international exports since 2016. (Services Australia page timed out; single-source.)
- **Bass Strait and island links**: Spirit of Tasmania, Geelong to Devonport, 242 nm, 9-11 hours; new ships delayed, Devonport terminal cost rose from A$90M to A$495M [W]. Freight market shares Toll 55%, SeaRoad 24%,
  TT-Line 21%; "99% of goods leaving and entering Tasmania" go by sea [W, single-source, unverified]. Basslink: 500 MW, 370 km, in service 2006; **fault from 21 Dec 2015 to 13 Jun 2016**; one economist's estimate of
  A$140-180M cost to Hydro Tasmania; Marinus Link final investment decision 1 Aug 2025, Stage 1 750 MW, completion planned 2030 [W]. These are the nearest published "island dependence" data I could obtain; no
  Tasmanian supply-security review was retrieved.
- **Territorial administration**: the Australian Antarctic Territory (5.9 million km2, 42% of Antarctica) is administered by the AAD under Commonwealth law, with ACT civil law and Jervis Bay criminal law applied;
  sovereignty frozen under the Treaty and recognized by France, New Zealand, Norway and the UK [W]. **It is not under Tasmanian law**; Hobart is its operational base. Heard Island and McDonald Islands are an
  external Commonwealth territory (Act of 1953) managed by the AAD for the Department of Climate Change, Energy, the Environment and Water; about 4,100 km southwest of Perth; entry prohibited without permit; first
  environmental management visits in more than two decades occurred on Nuyina's V1 and V2 in 2025-26; 1-3 vessels fish toothfish there [P/W]. **Macquarie Island, by contrast, is a Tasmanian Nature Reserve** (waters to 3 nm),
  World Heritage listed in 1997 (to 12 nm), managed day to day by the Tasmania Parks and Wildlife Service, with the AAD running the research station since 1948 [P: parks.tas.gov.au; antarctica.gov.au]. It lies 1,542 km from Hobart [P].
- **Rescue**: Australia's search and rescue region is "nearly 53 million square kilometers" including the Antarctic Territory; the Rescue Coordination Center is in **Canberra** [P: AMSA]. (ASPI says about 12% of Earth's surface;
  53 million km2 is about 10% [D]; discrepancy noted, not resolved.) AAD's crisis management team activates at Kingston; an East Antarctic Emergency Coordination Group links Australia, France, Italy, China, Japan, Russia and India [P: AAD Magazine 2017].
  In the 2013 Akademik Shokalskiy case, "five days for the Aurora Australis to arrive on scene" [P].
- **Defense and enforcement** (thin): RAAF C-17 freight flights Hobart to Wilkins since 2015 [P/W]; Defense airdropped 10 t to Bunger Hills in 2022 (Operation Southern Discovery) and was asked in April 2024 to consider an airdrop to Mawson [S: ABC 25 Apr 2024];
  ADV Ocean Protector (Southern Ocean patrol ship) has Fremantle as home port and was photographed in Hobart in 2011 [W]; HMAS Huon, "the main naval facility in Tasmania from 1901 to 1994," implies no major naval base at Hobart now [W, single-source].
- **Vulnerability and resilience evidence**: (a) April 2024: Nuyina's two main cranes malfunctioned and **only about half the cargo could be offloaded**, with building materials and dry goods left aboard; airdrop planning followed [S: ABC]. (b) Nuyina cannot pass the Tasman Bridge to
  the Selfs Point fuel depot; refueling at Burnie costs a 660 km detour and "nearly $1 million annually"; fuel-barge expressions of interest planned [S: ABC 2 Aug 2024; P: IEE public-comment table]. (c) Airport runway works made Antarctic flights unavailable for roughly October to December (2024) [S: ABC]. (d) Single-ship dependence: the schedule shows
  Nuyina leaves for **dry docking in Singapore** 28 Jun to 15 Sep 2026 [P]. (e) WA's Ports Minister said in June 2024 the state was ready to take AAD headquarters to Fremantle; the Commonwealth then funded Wharf 6 [S/P].

**Search strings (thread 3):** "Tasmania secession movement history separatist sentiment Tasmanian independence federation 1901 Tasmanian Senate Hare-Clark"; "Macquarie Island Heard Island McDonald Islands administered Tasmania Macquarie
Island Tasmanian state waters Tasmanian Nature Reserve Australian Antarctic Division administers Heard"; "Australian Antarctic Territory administration Hobart Antarctic Division Australian Antarctic Territory Acceptance Act 1933 Tasmania law applies Hobart Magistrates";
"AMSA search and rescue region Southern Ocean Australia SAR region Antarctica Hobart rescue coordination Australian Antarctic Territory"; "Macquarie Island Tasmania Parks and Wildlife Service Macquarie Island Nature Reserve Tasmanian jurisdiction World Heritage Hobart 1,500 km";
"Australian Border Force Hobart Southern Ocean patrol Ocean Protector Antarctic fishing patrol toothfish Heard Island Hobart based vessels". **Refused (budget exhausted):** "Tasmanian Freight Equalisation Scheme Bass Strait Passenger Vehicle Equalisation Scheme how it works cost per year Services Australia";
"Basslink cable fault 2015 2016 Tasmania energy crisis Hydro Tasmania drought Basslink outage 6 months Marinus Link"; "Tasmania supply chain resilience review Bass Strait freight shipping disruption essential supplies food fuel Tasmanian Government";
"Tasmania Commonwealth Grants Commission Productivity Commission Tasmanian shipping inquiry Bass Strait Tasmania freight share of Tasmania trade by sea percent". **Dead ends:** utas.edu.au Companion page (403, recovered via Wayback); Services Australia page (timeout);
Defense C-17 release (timeout twice); the Australian Border Force/fisheries presence at Hobart did not surface beyond the Ocean Protector fragment.

### Thread 4. Hobart as transshipment or staging node

- **France**: Hobart has been the Antarctic gateway for the Australian and French programs "over the last four decades" [P, 2017 Strategy]; Tasmanian Government MoU with IPEV in 2014 [P]. L'Astrolabe (72 m by 16 m, 14 knots, about 1,200 t cargo, 60 berths)
  works Hobart to Dumont d'Urville, "4 to 5 rotations" in the 120 days from November to February, about **2,700 km** each way [P: https://taaf.fr/collectivites/lastrolabe/ ]. The AAD 2025-26 schedule lists its voyage VR1 (Hobart 13 Dec 2025 to 8 Jan 2026, via Macquarie Island, at Dumont d'Urville 20-30 Dec) [P].
  A 2017 French report says the ship was blocked 40 km from DDU by pack ice [S: Mer et Marine].
- **China**: MoU with the State Oceanic Administration in 2013; TPN and the Polar Research Institute of China signed an MoU to use Hobart as a technical services hub for maintenance and supply of specialized equipment [P, 2017]. Xue Long made two summer calls in 2018, worth about A$2.5M [S: ABC 15 Sep 2018].
  Pre-pandemic there were about 5 port calls a season; since the pandemic only one Hobart visit (Mar 2024), with Chinese vessels now using Fremantle; the Premier invited both icebreakers back in Nov 2024; the 2013-19 MoUs are described as expired; nine ice-class vessels hold approval to transit the Tasman Bridge [S: ABC 26 Nov 2024].
- **South Korea**: icebreaker Araon "visits Hobart each season to source fuel and to access specialist Tasmanian products, such as traverse equipment" [P, 2017]; Araon's other staging port is Lyttelton, New Zealand [W].
- **United States**: the AAD air link carries US expeditioners to McMurdo from Hobart and Christchurch; US research vessels visit "periodically" [P, 2017]; the Premier asked US officials in Oct 2024 for more visits by the icebreaker Polar Star [P].
- **Italy and Japan**: "also visit" [P, 2017]; Italy's Laura Bassi works mainly through Lyttelton [S]. **Japan's actual port was not confirmed** (Shirase to Fremantle is my recollection, unverified, three fetch attempts failed).
- Visit value: up to A$2M per foreign icebreaker call [P].
- **Bulk mainland cargo staged through Tasmania for Antarctica: no evidence in any source.** The AAD's own cargo flows are small and containerized (section 1.1). Hobart's total port throughput is about 1.6 Mt (2023/24), 359 vessel arrivals, 1,730 containers [W, single-source]; Tasmania's heavy
  tonnage moves through Burnie (about 5 Mt) and Devonport (3-4 Mt) and Bell Bay (minerals, forestry) [W].
- **Distance and time**, from the AAD table (published) and my own great-circle computation ([D], validated against the AAD table: my Hobart-Casey 3,424 km versus 3,443; Perth 3,834 versus 3,837; Melbourne 3,840 versus 3,861; Adelaide 3,948 versus 3,936):

| From | Dumont d'Urville (66.66 S 140.00 E) | Commonwealth Bay (67.01 S 142.66 E) | Casey | Bunger Hills (66.28 S 100.77 E) |
|---|---|---|---|---|
| Hobart | 2,681 km | 2,697 km | 3,424 (AAD 3,443) | 3,819 |
| Melbourne | 3,220 (+20%) | 3,247 (+20%) | 3,840 (AAD 3,861) | 4,209 (+10%) |
| Torquay / Jan Juc | 3,160 (+18%) | 3,188 (+18%) | 3,767 | 4,134 (+8%) |
| Adelaide Outer Harbor | 3,547 (+32%) | 3,594 (+33%) | 3,948 (AAD 3,936) | 4,271 (+12%) |
| Bunbury | 4,036 (+51%) | 4,138 (+53%) | 3,681 | 3,795 (-0.6%) |
| Fremantle (for reference) | 4,170 | 4,270 | 3,822 | 3,935 |

  Straight-line, ignoring sea ice, shipping routes and weather; the Hobart-DDU figure matches the TAAF-published 2,700 km. At L'Astrolabe's 14 knots (about 620 km a day) these straight-line lengths are about 4.3 days from Hobart to either point versus about 5.2, 5.8 and 6.7
  days from Melbourne, Adelaide and Bunbury to Commonwealth Bay [D]. **For the Bunger Hills end of the coast, Bunbury is about equal to Hobart and the eastern terminals are 8-12% longer.** No source publishes Fremantle, Melbourne or Adelaide departure times to the Adélie Land
  or Commonwealth Bay coast; the AAD table stops at Casey, Davis and Mawson. The cited "10 to 11 days" for the mainland terminals is the project's own figure; I did not find an external source for it.

**Search strings (thread 4):** "Hobart to Dumont d'Urville distance nautical miles L'Astrolabe voyage days IPEV Hobart"; "Araon icebreaker Hobart port call Korea Antarctic Jang Bogo station resupply Hobart fuel"; "Xue Long Xue Long 2 Hobart port call Zhongshan Station
resupply Chinese Antarctic expedition Hobart"; "Fremantle to Davis Station Mawson distance nautical miles Fremantle Antarctic gateway proposal Western Australia Perth Antarctic Division relocate"; "Hobart closest port to East Antarctica Commonwealth Bay Cape Denison distance km
from Hobart days sailing"; "Antarctic gateway cities comparison Hobart Christchurch Cape Town Punta Arenas Ushuaia distance to Antarctica sailing time". **Dead ends:** Wikipedia JARE, Syowa, Shirase page names (404 or no logistics content), so Japan's port is open.

### Thread 5. Island-port physical facts

- **Harbor ice and climate** [P: BoM Hobart (Ellerslie Road, 094029), Wayback copy prepared 14 May 2026]: mean maximum 11.8 C and mean minimum 4.6 C in July (coldest month); mean annual rainfall 611 mm over 86.8 rain days; mean 9 am wind about 13 km/h (annual); mean 3 pm wind about 16 km/h. With a mean July minimum above freezing, the estuary does not freeze (my inference; no source states "no harbor ice" directly). Lowest recorded temperature -2.8 C [W]. These are present-day values, not projections for the project's era.
- **Harbor**: described as "second-deepest natural port in the world" (Wikipedia Hobart) and "deepest sheltered harbor in the Southern Hemisphere" (Wikipedia River Derwent); the two superlatives disagree and no depth figure was obtained [W, unverified]. Much of the waterfront is reclaimed land [W].
- **Tasman Bridge**: clearance 46 m [W, single-source; not confirmed]; 5 Jan 1975 collision by the bulk ore carrier Lake Illawarra killed 12 and closed the bridge until 8 Oct 1977 [W]; traffic is halted when big ships transit; Nuyina's air draft means it cannot go upriver to the Selfs Point fuel depot [P: IEE public-comment table; S: ABC]. The AAD schedule shows what that means in practice: **Nuyina bunkers at Burnie, Tasmania** each voyage:
  21-22 Sep 2025 ("Bunker vessel with MGO and SAB"), 26-27 Nov 2025 (same, "Depart for Antarctica"), 8-9 Feb 2026 ("with MGO"), and anchors in the Derwent River on 2-3 Apr 2026 for watercraft familiarization [P].
- **Southern Ocean weather window** (observed, not forecast): the AAD season runs from Nuyina's first loading on 1 Sep and first departure on 26 Sep to its last Macquarie Island return on 27 Apr [P]; the Antarctic stations' hardest approach is Mawson, where "challenging environmental conditions... preclude access to the station's harbor until later in the season" and some years need a helicopter-supported resupply [P: IEE]. Wilkins is seasonal, with warmer temperatures limiting flights [W]. I did not obtain a published sea-state or storm-frequency statistic for the Hobart approaches.
- **Sea-level and storm exposure of the Hobart waterfront: not obtained.** Only generic national text was retrieved (BoM State of the Climate: sea levels rising around Australia, more frequent extreme high levels; global mean sea level up more than 22 cm since 1900) [P], plus Biosecurity Tasmania's statement that Tasmania's warming is projected to be slower than the mainland's [P].
- **Population**: Greater Hobart 254,930 (2024) [W]; Tasmania 573,479 (June 2023) [W], giving about 44% [D]; Wikipedia's Tasmania page says "around 40%," its Hobart page "roughly half," and its Derwent page "nearly 40% ... around the estuary's margins." The ABS fetch gave a Greater Hobart figure of 255,250 (June 2025) but a garbled state total; treat 40-45% as the range. Tasmania is "240 km to the south of the Australian mainland" [W]; 68,401 km2 [W].
- **Ship building and repair**: Incat builds aluminum wave-piercing catamarans at Prince of Wales Bay, Hobart (location since 1989; a second yard planned at Boyer from Aug 2024) [W]; the Australian Maritime College belongs to the University of Tasmania [W]. No source gave a drydock able to take an icebreaker; Nuyina's dry docking is scheduled for Singapore [P].

**Search strings (thread 5):** none specific (the search cap blocked the planned queries); content came from direct page fetches of BoM, Wikipedia (Hobart, Tasmania, River Derwent, Tasman Bridge, Incat, Port of Hobart, Transport in Tasmania) and the AAD schedule. **Dead ends:** "Sea_level_rise_in_Tasmania" and "Sea_level_rise_in_Australia" Wikipedia pages (404); "Climate change in Tasmania" page has no sea-level content; CSIRO and Tasmanian climate-change office pages (404 or not archived); the TasPorts "Port of Hobart" page URL guessed (404).

---

## 3. Flat candidate list: Hobart-specific applications (possibilities only, unranked)

Each item is a possibility suggested by sourced evidence, stated flatly; none is a recommendation, and the order carries no meaning.

- **A-1. Clean-cargo checkpoint.** A dedicated quarantine and cargo-consolidation center (inspection, fogging, fumigation, rodent screening, cold and cool storage) at the point where mainland or bulk cargo changes to cargo for the sensitive southern coast. (Real analog: the AAD Cargo and Biosecurity Center, Macquarie Wharf 2, 2013; the CEP manual's "gateways" principle.)
- **A-2. Pest-free provisioning source.** An island that is a pest-free area for fruit flies as a source of clean fresh produce (potatoes, carrots, apples, citrus) and pre-inspected food for the polar coast, with sealed packing and Antarctic-grade packaging rules. (Real analog: AAD food list; Tasmania's fruit fly pest-free status; Medfly in WA and Qfly on the eastern mainland.)
- **A-3. Island as a quarantine buffer, with a reverse friction.** The island's strict import regime could serve as a second line between mainland cargo and the polar coast; equally, the same regime could burden or delay mainland surplus food landing there. Both are possible; no source resolves transit-cargo treatment.
- **A-4. Shortest-leg staging port for the Adélie Land and Commonwealth Bay end of the coast.** About 2,700 km versus 3,200 to 4,100 km from the mainland terminals; for the Bunger Hills end, Bunbury is about equal. (Computed distances, section 2 thread 4.)
- **A-5. Polar equipment and services cluster.** Local manufacture and supply of traverse equipment, cold-climate gear, ship outfitting, scientific instruments, hose and lifting gear, power systems, provedoring, medical and engineering services, sold to several national programs. (Real analog: Tasmanian Polar Network, 70+ members.)
- **A-6. Multi-program gateway and fueling stop.** A port that other nations' icebreakers and research ships use for fuel, provisions, technical services and crew change, with standing agreements (MoUs) and measurable local income per call (up to A$2M). (France, China, Korea, Italy, Japan, US all named.)
- **A-7. Treaty and regulatory seat.** A harbor city where the Southern Ocean fisheries commission (CCAMLR) and albatross and petrel agreement (ACAP) sit, so that fisheries rules, licensing data and conference traffic concentrate there.
- **A-8. Science and forecasting cluster.** Marine and Antarctic research institutes, a meteorological Antarctic office, an ocean-observing program office and a marine research vessel on the waterfront, supplying ice, ocean and weather knowledge to shipping and to the coast.
- **A-9. Air-bridge and urgent-cargo node.** An airport that runs a scheduled passenger jet and military heavy-lift flights to an ice runway (about 4 hours; 13 not-cancelled round trips in 2025-26), for personnel, medical cases and high-priority freight, while ships carry volume.
- **A-10. Medical screening and remote-medicine hub.** Pre-deployment medical screening and a remote and maritime medicine center (CARMM) serving expeditions.
- **A-11. Home port and lay-up base for the icebreaking resupply ship.** A dedicated Antarctic terminal, shoreside power, a long-term priority berth (30 years), and year-round lay-up, close to the city center (5 minutes).
- **A-12. Administrative headquarters for a distant territory.** The agency that administers the Antarctic territory, runs its crisis-management team and coordinates multi-nation emergency groups, located on the island though the territory's law is the mainland Commonwealth's.
- **A-13. Division of labor among the island's ports.** Bunkering at Burnie because large icebreakers cannot pass the Tasman Bridge to the Hobart fuel depot; bulk tonnage at Burnie, Devonport and Bell Bay; Hobart specializing in polar, cruise and small-volume cargo. Hobart's measured throughput (1.6 Mt) is small next to Burnie's (about 5 Mt).
- **A-14. Waste back-haul reception.** Return of station waste ("RTA") and Annex III-controlled waste to the gateway port for sorting and disposal.
- **A-15. Ice-free, sheltered, always-open harbor.** A deep estuary with a mean July minimum above freezing, 24/7 port availability and tugs and pilots, so the shipping season is limited by the Southern Ocean, not by the home port.
- **A-16. Rescue and evacuation support node.** A base whose crisis team, medical expertise, helicopters and ship and aircraft assets support an East Antarctic multi-nation emergency group; the formal rescue coordination center stays on the mainland (Canberra).
- **A-17. Single-vessel risk and mitigations.** The 2024 crane failure (half the cargo undelivered), the Singapore dry-docking absence, the fuel-access constraint and the runway-works gap are evidence of the single-point risks of an island gateway, and of mitigations tried (airdrop, fuel barge, second berth).
- **A-18. Island politics of freight.** An island polity whose history includes secession agitation over shipping terms, a long-running freight subsidy, interstate rivalry for the polar function (WA offered to host the agency), and a port-fee dispute with its federal customer.
- **A-19. Training and education pipeline.** University-based polar and maritime teaching (150+ postgraduates; 52 PhD students in Antarctic topics in 2019-20) feeding the polar workforce.
- **A-20. Ship-building and repair gap.** An island yard that builds fast aluminum ferries but, in the sources, no drydock for an icebreaker; the large-ship docking goes overseas (Singapore).
- **A-21. Conference and diplomacy venue.** Annual Antarctic meetings (4,114 delegate-days, about A$3.5M in 2019-20; later A$3M a year) and a civic gateway-cities agreement (Hobart, Christchurch, Cape Town, Ushuaia, Punta Arenas).

---

## 4. Remaining gaps

1. Hobart sea-level, storm-surge and Derwent flood exposure (no Hobart-specific source obtained).
2. Whether goods in transit to Antarctica are exempt from Tasmanian import conditions; whether any mainland food is staged through Hobart.
3. A published depth for the Hobart channel and berths; an authoritative Tasman Bridge clearance figure (46 m is single-source; 45 m is another commonly stated value I could not confirm).
4. Cold-storage and fuel-storage capacity at Hobart; Hobart Port Master Plan (2016) text; current status of the Macquarie Point Antarctic and Science Precinct.
5. Ship repair, dry dock and slipway capability in Tasmania (beyond Incat's aluminum ferry yard).
6. Naval, Border Force and fisheries-patrol presence at Hobart; Tasmanian supply-security reviews; current Freight Equalisation budget; Bass Strait share of Tasmania's freight (the "99% by sea" figure is single-source).
7. Japan's and Norway's actual ports; Italy's and the US's frequency of Hobart calls.
8. A published transit time for Fremantle, Melbourne or Adelaide departures to the Adélie Land or Commonwealth Bay coast (none found).
9. The second source for the January 2024 fruit fly detection; the Cambridge abstract on fungi in wooden cargo packaging; the COMNAP/SCAR 2010 checklist text itself.
10. A reconciliation of the AAD station-page transit times (4-8 days) with the IEE (7-16 days).
11. Items whose search was refused by the session budget (section 2 thread 3 "Refused" list) should be rerun if the cap is raised.
12. An ABC piece titled "'Open your eyes': Why China's sixth Antarctic base is raising concerns" (27 Sep 2026) appeared in results and was not read; it may bear on the strategic angle.
