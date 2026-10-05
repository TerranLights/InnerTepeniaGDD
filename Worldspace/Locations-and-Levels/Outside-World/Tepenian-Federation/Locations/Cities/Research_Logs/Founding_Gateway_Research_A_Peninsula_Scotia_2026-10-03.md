# Founding-Gateway Research A — Peninsula / Scotia Sea sector (2026-10-03)

**Scope.** Four gateway claims (Pergamino, Puerto Abrigo, Contrapunto, Signy), each checked on its own terms. Pure geography and access only. The research station's operator is never an input; where the real-world operators of the area are mentioned it is labeled **CONTEXT (b)** and is not offered as evidence for any basis. The researcher reports evidence; the developer rules.

---

## 0. READ THIS FIRST — limits on the evidence (honest accounting under LAW 0-R)

1. **The WebSearch tool was exhausted at the start of this task.** Every WebSearch call returned "this session has used its web search budget (200 of 200)". **Zero searches were run.** The four attempted search strings are listed in §6. This means the brief's requirement "query every claim from at least 3 angles" was **only partly met**: angles were obtained by *fetching different pages* (English Wikipedia, Spanish Wikipedia, Portuguese Wikipedia, Wikivoyage, tourism-operator pages, COMNAP, Uruguayan Antarctic Institute), not by running differently-worded searches. Nothing was reached via a search engine; the developer should raise `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` and re-run the **open threads** in each section for a proper pass.
2. **Source quality is lower than the brief asked for.** Almost every number below comes from Wikipedia / Wikivoyage (tertiary), passed through WebFetch's summarizing model. The only non-encyclopedic pages that opened and returned usable text were `antarctica21.com` (operator), `iau.gub.uy` (Uruguayan Antarctic Institute — a menu page and a one-paragraph history page only), `comnap.aq` (index pages only), `censo2024.ine.gob.cl` (headline total only). **No port-authority, no academic paper, no government itinerary or timetable was obtained.** Anything marked "single-source" below rests on one Wikipedia article.
3. **Distances.** Two kinds are used and always labeled:
   - **[GC-calc]** = great-circle distance computed by the researcher (haversine, R = 6,371.0088 km, nmi = km / 1.852) from coordinates quoted from the sources named in §7. This is an *arithmetic result*, not a looked-up fact. It is straight-line over the sea surface and ignores land, so it is a lower bound on any route.
   - **[src]** = a distance stated in a fetched source (method unstated unless noted).
   - **No source gave a true shipping-route distance** for any pair. Sailing-time figures marked "arith." are researcher arithmetic (distance / assumed speed), **not sourced**.
4. Where one page contradicted another, both are reported (§3).

---

## 1. Summary table

| # | City / site | Claim | Verdict | Key numbers | One-line basis wording (geography only, no comparisons) |
|---|---|---|---|---|---|
| 1 | **Pergamino** — Hurd Peninsula, Livingston I. (62°39'47"S 60°23'17"W); solar UTC-4 | "Río de la Plata (Montevideo) is the Atlantic-side gateway to the South Shetlands" | **PARTLY SUPPORTED as geography; CONTRADICTED as "gateway"** | Montevideo to site **3,100 km / 1,674 nmi** [GC-calc]; Punta del Este 3,103 km. Uruguay 3,499,451 (2023); Montevideo city 1,287,452 (36.8%), metro 1,947,604. Nearer populated places [GC-calc]: Puerto Williams 954 km, Ushuaia 984 km, Punta Arenas 1,222 km, Stanley 1,229 km, Río Gallegos 1,335 km. Buenos Aires 3,123 km. | "Uruguay's populous Río de la Plata coast lies about 3,100 km (1,670 nmi) north-northeast of the site across the open South Atlantic and Scotia Sea; it is where the nation's people and port are, not the nearest coast to the site." |
| 2 | **Puerto Abrigo** — Goudier I., Port Lockroy, Wiencke I. (64°49'31"S 63°29'40"W) | "Wiencke faces Drake's Pacific mouth; nearest populous gateway on the continental side is Chile's Magallanes coast (Punta Arenas, Puerto Williams)" | **PARTLY SUPPORTED** | To Port Lockroy [GC-calc]: Cape Horn 1,005 km / 543 nmi; Puerto Williams 1,123 km / 606 nmi; Ushuaia 1,145 km / 618 nmi; Punta Arenas 1,362 km / 736 nmi. Puerto Williams 1,868 (2017) to 2,874 (incl. naval); Punta Arenas 132,363 (2024); Ushuaia 79,538 (2022); Magallanes Region 166,537 (2024). | "The site is reached from the Magallanes and Fuegian coast, about 1,120 to 1,360 km (610 to 740 nmi) north-northwest across the western half of the Drake Passage; Punta Arenas (about 132,000) is the region's population center, Puerto Williams its nearest settlement." |
| 3 | **Contrapunto** — King George I. (Isla 25 de Mayo) (~62°13'S 58°47'W; Chilean station/village at 62°12'02"S 58°57'50"W) | "South Shetlands are the shortest open-water crossing from the Magallanes coast" | **SUPPORTED for the archipelago; PARTLY for King George I. specifically** | Cape Horn to Frei/Villa Las Estrellas **838 km / 452 nmi** [GC-calc]; Puerto Williams 949 km / 513 nmi; Punta Arenas 1,226 km / 662 nmi. Drake width 800 km [src], 808 km Cape Horn–SSI [src, es.wiki]. Punta Arenas to King George by air about **2 h** [src: 2 operators; 1 source says ~4 h]. Cape Horn to Smith/Livingston (western SSI) is ~12 to 20 km shorter than to King George [GC-calc]. | "King George Island lies about 840 to 1,230 km (450 to 660 nmi) north-northwest of the Magallanes coast, the shortest open-water crossing from South America to Antarctic land (the Drake Passage, about 800 km at its narrowest)." |
| 4 | **Signy** — Signy I., South Orkneys (60°42'30"S 45°35'42"W); solar UTC-3 | Brazil: "nearest large populous Atlantic coast on the Scotia Sea, with a direct open-water run" | **CONTRADICTED** as stated ("nearest"); "direct open-water run" is **true of the geometry** but equally so for other coasts. South Africa leg: **PARTLY SUPPORTED** (distance real, no sourced operational link) | [GC-calc] to Signy: Ushuaia 1,488 km; Puerto Williams 1,444 km; Stanley 1,252 km; Río Grande (Arg.) 1,526 km; Río Gallegos 1,762 km; Mar del Plata 2,660 km; Punta del Este 2,940 km; Montevideo 2,968 km; Buenos Aires 3,044 km; Chuí (BR) 3,057 km; Rio Grande (BR) 3,224 km; Santos 4,089 km; Rio de Janeiro 4,207 km; **Cape Town 5,376 km / 2,903 nmi**. | Brazil: "Brazil's southern Atlantic coast (Rio Grande, Chuí) lies 3,060 to 3,220 km (1,650 to 1,740 nmi) north-northwest of the site across open ocean east of the Falklands." South Africa: "Cape Town lies about 5,380 km (2,900 nmi) due west-to-east across the South Atlantic; the run is entirely open ocean." |

---

## 2. Per-city findings

### 2.1 PERGAMINO — Livingston Island (Hurd Peninsula)

**Site coordinates.** The brief's ~62°39'S 60°23'W matches the Spanish Juan Carlos I base at **62°39'47"S 60°23'17"W** on Hurd Peninsula (en.wikipedia Juan_Carlos_I_Antarctic_Base). The island-center coordinate on the Livingston Island page is 62°36'S 60°30'W. Solar UTC-4 is arithmetic (60.4°W / 15 = 4.03 h).

**Real facts with numbers**

- Livingston Island [src: en.wikipedia.org/wiki/Livingston_Island]: **809 km** south-southeast of Cape Horn; 796 km southeast of the Diego Ramírez Islands; **1,063 km** due south of the Falkland Islands; 110 km northwest of Cape Roquemaurel on the Antarctic mainland; 1,571 km southwest of South Georgia. Four seasonal stations (Spain, Bulgaria, Chile, USA). Tourists arrive by cruise ship.
- Drake Passage [src: en.wikipedia.org/wiki/Drake_Passage]: "The 800-kilometre-wide (500 mi) passage between Cape Horn and Livingston Island is the shortest crossing from Antarctica to another landmass." es.wikipedia (Pasaje de Drake): minimum width **808.17 km** between Cape Horn and the South Shetlands.
- **[GC-calc] from the site (Juan Carlos I coordinates):**

| From | km | nmi |
|---|---|---|
| Cape Horn | 839 | 453 |
| Diego Ramírez | 796 (src) | — |
| Puerto Williams | 954 | 515 |
| Ushuaia | 984 | 531 |
| Punta Arenas | 1,222 | 660 |
| Stanley (Falklands) | 1,229 | 664 |
| Río Gallegos | 1,335 | 721 |
| Comodoro Rivadavia | 1,921 | 1,037 |
| Mar del Plata | 2,749 | 1,484 |
| **Montevideo** | **3,100** | **1,674** |
| Punta del Este | 3,103 | 1,675 |
| Buenos Aires | 3,123 | 1,686 |
| Chuí (southernmost BR town) | 3,258 | 1,759 |
| Rio Grande (BR) | 3,456 | 1,866 |

- Bearing from the site to Montevideo is about 7° (north, slightly east); a great-circle line from Montevideo runs at about 48.8°S, 57.7°W then 55.7°S, 58.8°W, i.e. **it passes through or beside the Falkland Islands** (Stanley is 51.7°S 57.85°W). Real sailing would deviate around them. [GC-calc]
- Sailing time, **arith. only, unsourced**: 1,674 nmi at 12 kn is about 5.8 days (10 kn about 7 days; 14 kn about 5 days).
- **Montevideo population** [src: en.wikipedia.org/wiki/Montevideo, 2023 census]: city 1,287,452 (about 36.8% of the country); urban area 1,788,170; metro 1,947,604; department 1,319,108. **Uruguay total 3,499,451 (2023 census)**, coastline 660 km "along the Atlantic Ocean and Río de la Plata" [src: en.wikipedia.org/wiki/Uruguay]. Punta del Este 18,193 (2023).

**Is Montevideo / the Río de la Plata really "the Atlantic-side gateway to the South Shetlands"?**

- **Not documented as an Antarctic gateway in any source opened.** en.wikipedia "Antarctic gateway cities" lists five (Punta Arenas, Ushuaia, Cape Town, Hobart, Christchurch). Montevideo is absent. Wikivoyage Montevideo: "no mentions of Antarctica." en/es Wikipedia Port of Montevideo: no mention of Antarctica or Antarctic traffic. (Absence in encyclopedic pages is weak evidence; it died at the sources, see §2.1 dead ends.)
- Wikipedia (Antarctic gateway cities): Punta Arenas has "more than 20 national Antarctic programs"; Ushuaia "services Argentina's own National Antarctic Directorate, but no other national Antarctic program" and handles about 90% of Antarctic tourists. Wikivoyage Punta Arenas: cruise ships "mostly start out of Ushuaia, but there are some cruises from as far away as Buenos Aires, Rio de Janeiro, São Paulo and Valparaíso." (Montevideo not named there.)
- Geometry: the Río de la Plata faces the open South Atlantic; a ship from it reaches the South Shetlands from the north-northeast across the Scotia Sea / southern Drake. So "Atlantic-side" is geometrically accurate. But the **Fuegian/Magallanes coast is 2,100 to 2,200 km nearer** (Puerto Williams 954 km vs 3,100 km) and also borders the Drake.
- **Stronger or equally strong gateway the claim overlooks** (pure geography, no operator argument): (i) Argentina's Tierra del Fuego (Ushuaia 984 km; pop. 79,538 per es.wikipedia 2022; Río Grande 98,017 per en.wikipedia 2022); (ii) Chile's Magallanes (Punta Arenas, Puerto Williams); (iii) Argentina's Patagonian Atlantic coast (Río Gallegos 1,335 km, pop. 115,524, 2022; Comodoro Rivadavia 1,921 km, pop. 201,854, 2022); (iv) Falkland Islands (Stanley, 2,974 in 2021). **Equal-strength (same distance band): Buenos Aires** (3,123 km; city 3,121,707, metro 16,366,641, 2022) is on the same river estuary as Montevideo, 230 km west of it [src: en.wikipedia Montevideo].
- **CONTEXT (b) only — who actually serves the area (operators, not evidence):** Uruguay's Base Artigas is on King George Island, not Livingston. es.wikipedia (Base Artigas) says it is **3,012 km from Montevideo** [src, method unstated; compare GC-calc 3,039 km], receives "7 intercontinental flights per season" by C-130 Hercules and **one ship visit per season (January)**, and gives "the nearest commercial port" as **Ushuaia, about 1,000 km**. en.wikipedia (ROU Vanguardia): the Piast-class vessel's home port was Montevideo, it made annual supply runs to King George Island, and it was decommissioned **2 Sept 2026** (single source). iau.gub.uy confirms logistics are carried by the Uruguayan Navy (Armada) and Air Force (FAU). The 1916 Uruguayan rescue expedition for Shackleton's men left Montevideo (iau.gub.uy/historia); the successful rescue was by the Chilean tug Yelcho from Punta Arenas (en.wikipedia Elephant Island). **The route of the Hercules flights (Montevideo to Punta Arenas to King George) was not found.**
- Other Atlantic-facing nations: Argentina is closer (see above). Brazil is farther (Rio Grande 3,456 km; Rio de Janeiro more). Uruguay's own coast is the nearest of any of the three **Atlantic-facing-estuary** populations to the South Shetlands only if Argentina's Patagonian coast is excluded.

**Verdict: PARTLY SUPPORTED / geography true, "gateway" word contradicted.**

**Searches / URLs opened (this section):** no search strings run (budget exhausted). Pages opened: en.wikipedia Livingston_Island, Juan_Carlos_I_Antarctic_Base, Drake_Passage, Montevideo, Uruguay, Port_of_Montevideo, Antarctic_gateway_cities, ROU_Vanguardia, Artigas_Base, Uruguayan_Air_Force, Punta_del_Este, Buenos_Aires; es.wikipedia Pasaje_de_Drake, Puerto_de_Montevideo, Base_Científica_Antártica_Artigas, Instituto_Antártico_Uruguayo, Fuerza_Aérea_Uruguaya; en.wikivoyage Montevideo, Punta_Arenas; iau.gub.uy, iau.gub.uy/historia, iau.gub.uy/logistica.

**Dead ends (all logged):**
- iau.gub.uy sub-pages `/logistica` (menu only), `/transporte-aereo`, `/bases`, `/campana-antartica`, `/base-artigas`: **died at the sources** (404 or navigation menu only; the real content pages were not reachable by guessable URL).
- gub.uy/instituto-antartico-uruguayo, gub.uy/ministerio-defensa-nacional: **died at the sources** (404 / no Antarctic content in the fetched text).
- comnap.aq/members/uruguay, /antarctic-gateway-cities: 404 (**sources**). COMNAP "Antarctic Facilities Information" page opened but is an index of a station catalogue and CSV files that were not opened.
- es.wikipedia ROU_26_Vanguardia, Uruguay_en_la_Antártida, Programa_Antártico_Uruguayo; en.wikipedia Uruguay_in_Antarctica, Ruperto_Elichiribehety_Station: 404 (**sources**).
- Montevideo-to-Punta-Arenas Hercules routing: **died at the query** (no search possible) and at the sources (the Uruguayan pages opened did not state it).

**Single-source:** Uruguay's "7 flights/season, 1 ship/season, nearest port Ushuaia ~1,000 km, 3,012 km from Montevideo" (Spanish Wikipedia infobox, probably COMNAP-derived but not checked). Vanguardia decommissioning date (en.wikipedia only).

**Open threads:** (a) Uruguayan Air Force KC-130/C-130B flight route and stopover airports; (b) whether any Antarctic cruise or program vessel departs Montevideo today (IAATO ports, Montevideo port authority ANP, Uruguayan Navy); (c) shipping-route (not great-circle) length Montevideo to Livingston; (d) Bulgarian and Spanish Livingston stations' own gateway ports (CONTEXT (b), Spanish Hespérides route was not on the Wikipedia page); (e) Uruguay's population share on the Río de la Plata coast beyond Montevideo department (Canelones, San José, Colonia).

---

### 2.2 PUERTO ABRIGO — Port Lockroy, Goudier Island, Wiencke Island

**Site coordinates.** Port Lockroy **64°49'31"S 63°29'40"W** on Goudier Island, in a bay on Wiencke Island's northwestern shore, Palmer Archipelago [src: en.wikipedia Port_Lockroy]. Wiencke Island: 64°50'S 63°23'W, 26 km long, 67 km² area, "southernmost of the major islands of the Palmer Archipelago", between Anvers Island (across Neumayer Channel, 16 miles long, 64°47'S 63°27'W) and the Peninsula coast (across Gerlache Strait, 64°30'S 62°20'W) [src: en.wikipedia Wiencke_Island, Neumayer_Channel, Gerlache_Strait]. The archipelago is "in the Pacific sector of Antarctica" [src: en.wikipedia Palmer_Archipelago].

**Geometry: "faces the Drake Passage's Pacific mouth"**

- Drake Passage "connects the southwestern part of the Atlantic Ocean (Scotia Sea) with the southeastern part of the Pacific Ocean" (en.wikipedia Drake_Passage); Cape Horn "marks both the northern boundary of the Drake Passage and where the Atlantic and Pacific Oceans meet" (en.wikipedia Cape_Horn).
- **[GC-calc] initial bearings from Port Lockroy: Cape Horn 346°, Ushuaia 344°, Puerto Williams 346°, Punta Arenas 339°, Diego Ramírez 341°, Montevideo 12°.** So the Fuegian/Magallanes coast lies almost due north-northwest, across the western half of the Drake Passage (the Pacific-ward half, since the Passage runs from the Cape Horn meridian 67°17'W eastward to the Scotia Sea). The phrase "faces the Pacific mouth" is a fair description of *bearing*; **no source used that phrase.** Port Lockroy itself is on the Peninsula's western (Pacific-sector) side, reached from the Drake via Gerlache Strait / Neumayer Channel (the passage exists; which approach ships use was not sourced).
- Port Lockroy is **south of the Drake's main funnel**: Wikipedia (Antarctic Peninsula) notes the Peninsula and Cape Horn "channel winds into the relatively narrow Drake Passage."

**Distances to Port Lockroy [GC-calc]**

| From | km | nmi | bearing |
|---|---|---|---|
| Diego Ramírez (Chilean Navy outpost) | 970 | 524 | 341° |
| Cape Horn (Hornos I.; 5 residents in 2019, a lighthouse-keeper family) | 1,005 | 543 | 346° |
| **Puerto Williams** | **1,123** | **606** | 346° |
| **Ushuaia** (Argentina) | **1,145** | **618** | 344° |
| Río Grande (Arg., Tierra del Fuego) | 1,250 | 675 | — |
| **Punta Arenas** | **1,362** | **736** | 339° |
| Stanley | 1,495 | 807 | 15° |
| Río Gallegos | 1,504 | 812 | — |
| Mar del Plata | 3,008 | 1,624 | — |
| Montevideo | 3,363 | 1,816 | 12° |

- **[src] Punta Arenas is "1,418.4 km from the coast of Antarctica"** (es.wikipedia Punta_Arenas; en.wikipedia says "roughly 1,419 km"). Ushuaia "roughly 1,100 km from the Antarctic Peninsula" (en.wikipedia) / "1,150 km north of Esperanza base" (es.wikipedia). Wikipedia (Antarctic Peninsula): Tierra del Fuego "about 1,000 km" from the Peninsula; Wikivoyage (Antarctic Peninsula): the Peninsula's tip is "some 1600 km" from the mainland (**conflict: see §3**).
- Distance Puerto Williams to Ushuaia is 46 km, Punta Arenas to Ushuaia 250 km [GC-calc] (Wikipedia: Punta Arenas "635 km from Ushuaia", Puerto Williams to Punta Arenas ferry route 350 km, **32 h**, Wikivoyage: weekly TABSA ferry; en.wikipedia says "Yaghan" ferry).

**Populations**

| Place | Figure | Source |
|---|---|---|
| Punta Arenas | 132,363 (2024 census; 94.8% urban) | en.wikipedia Punta_Arenas. **Conflicts:** es.wikipedia gives 123,403 (2017) and 148,391 ("2023"); es.wikipedia Magallanes region page gives 131,067. Wikivoyage: about 125,000 (2015). |
| Magallanes Region | 166,537 (2024), about 0.9% of Chile (18,480,432, 2024 census; the INE site confirms the national total) | en.wikipedia Magallanes_Region |
| Puerto Natales | 24,152 (2024) | same |
| Puerto Williams | 1,868 (2017 census, es.wikipedia); 2,874 "including naval personnel and civilians" (en.wikipedia, year unstated); Wikivoyage "about 1,900 (2017)" | **conflict**, see §3 |
| Cabo de Hornos commune | 2,262 (2017); 1,750 (2024) | en.wikipedia Cabo_de_Hornos,_Chile |
| Ushuaia | 79,538 (2022), 56,593 (2010) (es.wikipedia). en.wikipedia gives 89,606 and a "2026 census 84,378" | **conflict**, see §3 |
| Tierra del Fuego Prov. | 190,641 (2022) | en.wikipedia |

**Is "nearest populous gateway on the whole continental side = Magallanes coast (Punta Arenas, Puerto Williams)" true?**

- **Nearest settlement of any size [GC-calc]:** Puerto Williams (1,123 km). True: it is the nearest town (pop. under 3,000) and Chilean.
- **Nearest settlement over about 10,000:** **Ushuaia (Argentina), 1,145 km**, only 22 km farther than Puerto Williams, and 217 km nearer than Punta Arenas. So the claim is **true if "Magallanes coast" means Puerto Williams, but "populous" is carried by Ushuaia (79,538) or Punta Arenas (132,363) respectively**, and Ushuaia is the nearer of the two.
- **Nearest city over 100,000 (among cities computed):** Punta Arenas (1,362 km); the next, Río Gallegos (115,524), is 1,504 km. Río Grande (Arg.) at 98,017 is 1,250 km, just under the threshold. The list is not exhaustive (not every Argentine/Chilean city was computed).
- Neighboring-nation gateway the claim overlooked: **Argentina's Tierra del Fuego (Ushuaia and Río Grande)**, same Fuegian archipelago, same Drake access. The Beagle Channel on which Ushuaia and Puerto Williams stand "connects the Pacific Ocean to the Atlantic Ocean" (en.wikipedia Beagle_Channel); the Strait of Magellan (Punta Arenas) also connects Atlantic (east) and Pacific (west), "570 km long" and "several hundred miles shorter than the Drake Passage" (en.wikipedia Strait_of_Magellan). So the **"which ocean each port faces"** question: all three ports sit inside the channel system that links both oceans; none "faces" one ocean only. Puerto Williams and Ushuaia are both on the Beagle Channel, with Cape Horn about 100 km to the southeast.
- **CONTEXT (b) only:** Wikipedia: Punta Arenas hosts INACH (the Chilean Antarctic Institute, HQ since 2003) and an International Antarctic Centre (built 2018 to 2022); "more than 20 national Antarctic programs travel through" it; Puerto Williams "supports Chile's Antarctic bases". Ushuaia "major port of departure in the world for tourist and scientific expeditions to the Antarctic Peninsula", 90% of tourists, "almost 400 annual calls" (es.wikipedia); about 124,000 cruise visitors a year reached Antarctica by 2025 "mostly on vessels travelling to the Antarctic Peninsula from South America" (en.wikipedia Antarctic_tourism). Port Lockroy: about 18,000 visitors per five-month season (en.wikipedia Port_Lockroy; Wikivoyage says about 10,000 annually; **conflict**).

**Verdict: PARTLY SUPPORTED.** Geometry and "Chile's Fuegian/Magallanes coast is the nearest populated coast to Wiencke" hold only at the settlement scale (Puerto Williams). At the "populous" scale the nearest town above 10,000 is Ushuaia, in Argentina.

**Searches / URLs opened:** en.wikipedia Port_Lockroy, Wiencke_Island, Palmer_Archipelago, Neumayer_Channel, Gerlache_Strait, Cape_Horn, Hornos_Island, Cabo_de_Hornos,_Chile, Diego_Ramírez_Islands, Isla_de_los_Estados, Punta_Arenas, Puerto_Williams, Ushuaia, Magallanes_Region, Tierra_del_Fuego_Province,_Argentina, Strait_of_Magellan, Beagle_Channel, Antarctic_Peninsula, Río_Gallegos, Río_Grande,_Tierra_del_Fuego, Chile, Antarctic_gateway_cities, Antarctic_tourism, Tourism_in_Antarctica; es.wikipedia Punta_Arenas, Ushuaia, Puerto_Williams, Región_de_Magallanes…; en.wikivoyage Antarctic_Peninsula, Punta_Arenas, Ushuaia, Puerto_Williams; censo2024.ine.gob.cl.

**Dead ends:**
- A shipping-lane description of how cruise ships actually approach Wiencke (Drake to Bransfield vs. Bismarck Strait): **died at the query** (no search) and at the sources (Wikipedia Gerlache Strait states no connections).
- Operator pages: Quark, Lindblad/Expeditions, Oceanwide, Hurtigruten (several URLs): **died at the sources** (404, or content with no itinerary/crossing-time text). Oceanwide `.../blog/the-drake-passage-how-long-does-it-take`, coolantarctica.com sub-pages, iaato.org data page: 404.
- Britannica Drake Passage: 403 (**source blocked**).
- The Chilean Navy / INACH official pages were not tried by URL (not guessable); **thread left open**.

**Single-source:** Cabo de Hornos commune 1,750 (2024); Hornos Island "5 residents in 2019"; the "32 h" ferry time (Wikivoyage); Punta Arenas "International Antarctic Centre 2018 to 2022" (en.wikipedia INACH article).

**Open threads:** (a) a real shipping-route distance and the standard crossing time Ushuaia to Port Lockroy (operators generally state about two days; **not verified here**, only "two-day crossing" appears on antarctica21.com and "a couple of days each way" on Wikivoyage); (b) population of Puerto Williams as a settled civilian count versus naval; (c) Chilean Navy/Diego Ramírez staffing; (d) whether Chile's Punta Arenas or Argentina's Ushuaia handles more traffic *to Wiencke specifically* (CONTEXT (b), not geography).

---

### 2.3 CONTRAPUNTO — King George Island (Isla 25 de Mayo)

**Site coordinates.** Island center 62°02'S 58°21'W; island **95 km by 25 km, 1,150 km²**, "120 km off the coast of Antarctica" [src: en.wikipedia King_George_Island_(South_Shetland_Islands)]. The brief's ~62°13'S 58°47'W lies on the Fildes Peninsula side: Chile's Villa Las Estrellas 62°12'02"S 58°57'50"W [src: es.wikipedia, en.wikipedia Villa_Las_Estrellas]; Uruguay's Artigas 62°11'05"S 58°54'12"W (es.wikipedia). Distances below use Villa Las Estrellas / Frei coordinates.

**Drake Passage and the shortest crossing**

- Width: **about 800 km** (en.wikipedia Drake_Passage: "800-kilometre-wide … between Cape Horn and Livingston Island … shortest crossing from Antarctica to another landmass"); **808.17 km** Cape Horn to South Shetlands in a straight line (es.wikipedia). en.wikipedia Cape_Horn: "about 800 kilometres wide" but also "Antarctica, only 650 kilometres away" — **this 650 figure is not reproduced by any computation or other source** (see §3). Elephant Island is 885 km southeast of Cape Horn (en.wikipedia). South Shetlands lie 93 km (Deception) to 269 km (Clarence) from the continent [src: en.wikipedia South_Shetland_Islands].
- **[GC-calc] to Frei / Villa Las Estrellas:**

| From | km | nmi |
|---|---|---|
| Cape Horn (Hornos I.) | 838 | 452 |
| Diego Ramírez | 841 | 454 |
| Isla de los Estados (center) | 879 | 475 |
| **Puerto Williams** | **949** | **513** |
| **Ushuaia** (Argentina) | **983** | **531** |
| Río Grande (Arg.) | 1,066 | 576 |
| Stanley | 1,170 | 632 |
| **Punta Arenas** | **1,226** | **662** |
| Río Gallegos | 1,327 | 717 |
| Comodoro Rivadavia | 1,896 | 1,024 |
| Mar del Plata | 2,693 | 1,454 |
| Montevideo | 3,041 | 1,642 |
| Chuí / Rio Grande (BR) | 3,194 / 3,388 | 1,725 / 1,829 |

- Cape Horn to the western South Shetlands [GC-calc, island-center coordinates]: **Smith Island 826 km / 446 nmi**; Livingston 830 km; King George 844 km; Elephant Island 907 km. Diego Ramírez to Smith 804 km; Isla de los Estados to Smith 919 km. So **the shortest crossing from South America is to the western end of the chain (Smith/Livingston), and King George is the next band, about 12 to 20 km farther** (differences are inside the error of island-center coordinates). Smith Island has no stations or population (en.wikipedia).
- Sources quote **"Livingston"** (not King George) as the Drake's narrowest crossing. Also Artigas page: Ushuaia "1,000 km" [src].

**By air and sea**

- **Airfield: Teniente Rodolfo Marsh Martin Aerodrome (SCRM / TNM)**, gravel runway **1,287 to 1,292 m** (en.wikipedia 1,292 m; es.wikipedia 1,287.5 x 38.1 m; Frei base page "1,300 m"), opened **12 Feb 1980** when two Twin Otters from Punta Arenas landed (es.wikipedia); "most northerly of the aerodromes in Antarctica"; **about 50 intercontinental and 150 intra-Antarctic flights per season** (Frei Base pages, en/es); operated by Chilean Air Force/Aeropuertos Chile. Uruguay's Artigas is 4 km away.
- **Punta Arenas to King George by air:** Aerovías DAP began Punta Arenas to Frei flights on **12 Feb 1989** (Twin Otter), later BAe 146-200 (2008) and Avro RJ; DAP "handles 76% of all air traffic between Antarctica and America" (en.wikipedia Aerovías_DAP; es.wikipedia says "about 80%"). **Flight duration: "just two hours"** (antarctica21.com, operator) and "2-hour charter flights from Punta Arenas between December and February" (Wikivoyage Antarctica). **One source disagrees:** Wikivoyage Southern_Ocean says "roughly 4 hours" (likely a round trip or error; see §3). Flights are charter, "no regular scheduled public service" (en.wikipedia Villa_Las_Estrellas). Great-circle 1,226 km in 2 h implies roughly 610 km/h average [GC-calc arith.], plausible for a jet; the BAe 146 cruise speed was not sourced.
- **Punta Arenas to the Drake by sea:** ship crossings Ushuaia to the Peninsula take "two days" (antarctica21.com: "the traditional two-day Drake Passage crossing"; Wikivoyage: fly-cruise "save a couple of days each way"). Arith. only: Cape Horn to Frei 452 nmi at 10 to 12 kn is about 38 to 45 h.
- Villa Las Estrellas: **about 80 winter, 150 summer** residents; "larger of only two civilian settlements on Antarctica"; hospital, school, bank, post office, chapel (en/es Wikipedia). Es.wikipedia: Villa Las Estrellas is "roughly 950 km southeast of Puerto Williams" (matches [GC-calc] 949 km). A wharf exists (es.wikipedia).

**Is there a shorter crossing from a populous coast?**

- From a **populous** coast: **no**, nothing shorter than Puerto Williams / Ushuaia (950 to 983 km) was found; Río Grande (Arg., 98,017) 1,066 km; Punta Arenas 1,226 km. From **any** coast: Cape Horn (838 km) and Diego Ramírez (841 km) are Chilean Navy outposts, Isla de los Estados (879 km) is Argentine with a four-man naval rotation (en.wikipedia: "a team of four seamen on a 45-day rotation"). None is populous.
- So the claim holds **only if "Magallanes coast" includes the Cabo de Hornos commune** (Puerto Williams, Cape Horn, Diego Ramírez). If "Magallanes coast" means Punta Arenas, then Punta Arenas is the *farthest* of the Fuegian gateways (1,226 km vs 949 km for Puerto Williams and 983 km for Ushuaia).
- **Stronger / equal gateway not named:** Ushuaia (Argentina, 983 km) is a near-tie with Puerto Williams; Argentina's Isla de los Estados is nearer than either.
- **CONTEXT (b) only:** the island hosts stations of Argentina, Brazil, Chile, China, Poland, Russia, South Korea, Peru, Uruguay, USA (en.wikipedia). Brazil's winter resupply is airdropped from Hercules/KC-390 flights "originating from Base Frei in Chile, near Punta Arenas" (pt.wikipedia Comandante Ferraz). INACH has run the Chilean program from Punta Arenas since 2003.

**Verdict: SUPPORTED at archipelago level; PARTLY SUPPORTED for King George Island specifically** (Smith/Livingston are marginally nearer; Puerto Williams/Ushuaia are nearer than Punta Arenas).

**Searches / URLs opened:** en.wikipedia King_George_Island_(South_Shetland_Islands), Teniente_Rodolfo_Marsh_Martin_Airport, Villa_Las_Estrellas, Eduardo_Frei_Montalva_Station, Fildes_Peninsula, South_Shetland_Islands, Smith_Island_(South_Shetland_Islands), Elephant_Island, Aerovías_DAP, Chilean_Antarctic_Institute, Drake_Passage, Cape_Horn; es.wikipedia Base_Presidente_Eduardo_Frei_Montalva, Aeródromo_Teniente_Marsh, Villa_Las_Estrellas, Aerovías_DAP, Pasaje_de_Drake; en.wikivoyage Antarctica, South_Shetland_Islands, Southern_Ocean; antarctica21.com; dapairline.com.

**Dead ends:**
- DAP's own flight timing page: dapairline.com home page opened; "Antártica Full Day" mentioned, **no duration stated** (source). `aeroviasdap.cl` redirects to dapairline.com.
- DGAC / Chilean Air Force official pages, Punta Arenas airport page: en.wikipedia Punta_Arenas_International_Airport 404 (**source**).
- en.wikipedia Presidente_Eduardo_Frei_Montalva_Base, Teniente_Rodolfo_Marsh_Martin_Base: 404 (the working title is "Eduardo_Frei_Montalva_Station").
- Ship-crossing duration (hours) from an official or port-authority source: **died at the query and at the sources**.

**Single-source:** "50 intercontinental and 150 intracontinental flights per season" (Wikipedia Frei base, both languages, same origin); DAP's "76%" vs "80%" share; "4 hours" flight time.

**Open threads:** (a) a DAP / Antarctic Airways timetable stating block time; (b) Chilean Air Force Hercules flight Punta Arenas to Frei (stated hours); (c) Chilean Navy ship Punta Arenas to Frei sailing time; (d) confirm what "Magallanes coast" is meant to include (Cabo de Hornos commune or Punta Arenas only).

---

### 2.4 SIGNY — Signy Island, South Orkney Islands

**Site coordinates.** Signy Research Station **60°42'30"S 45°35'42"W** (en.wikipedia); island 60°43'01"S 45°36'00"W; 19 km², 6.5 x 5 km, summit 288 m (en.wikipedia Signy_Island). Archipelago 60°36'S 45°30'W, **620 km²**, 90% glaciated, **604 km northeast of the Peninsula tip, 844 km southwest of South Georgia**, "seas around the islands are ice-covered from late April to November" (en.wikipedia South_Orkney_Islands). Orcadas Base on Laurie Island 60°44'17"S 44°44'16"W (65 summer / 17 winter residents). Solar UTC-3 is arithmetic (45.6°W / 15 = 3.04 h). Signy has "5 people" Nov to April only, since year-round occupation ended 1995/96 (en.wikipedia).

**[GC-calc] distances to Signy Research Station**

| From | km | nmi | bearing (from Signy) | Pop. (source) |
|---|---|---|---|---|
| King Edward Point, South Georgia | 896 | 484 | — | 22 summer / 19 winter |
| Stanley, Falklands | 1,252 | 676 | 318° | 2,974 (2021) |
| Isla de los Estados (center) | 1,282 | 692 | 293° | none (naval rotation) |
| **Puerto Williams** | 1,444 | 780 | 287° | 1,868 to 2,874 |
| **Ushuaia** | **1,488** | **804** | 286° | 79,538 (2022) |
| Río Grande (Arg.) | 1,526 | 824 | — | 98,017 (2022) |
| Punta Arenas | 1,734 | 936 | 288° | 132,363 (2024) |
| Río Gallegos | 1,762 | 951 | — | 115,524 (2022) |
| Comodoro Rivadavia | 2,179 | 1,177 | — | 201,854 (2022) |
| Mar del Plata | 2,660 | 1,436 | — | 682,605 (2022) |
| Punta del Este | 2,940 | 1,587 | — | 18,193 (2023) |
| **Montevideo** | **2,968** | **1,602** | 340° | 1,287,452 city (2023) |
| Buenos Aires | 3,044 | 1,644 | — | 3,121,707 city (2022) |
| **Chuí (southernmost BR town)** | **3,057** | **1,651** | — | 6,262 (2022) |
| **Rio Grande (RS, Brazil)** | **3,224** | **1,741** | 349° | 191,900 (2022) |
| Santos | 4,089 | 2,208 | — | 418,608 (2022) |
| Rio de Janeiro | 4,207 | 2,272 | — | 6,730,729 city (2025) |
| Recife (coordinate NOT sourced; approx. 8.05°S 34.88°W) | about 5,923 | about 3,198 | — | 1,488,920 (2022) |
| **Cape Town** | **5,376** | **2,903** | 87° (due east) | city 433,688 (2011), metro 4,772,846 (2022) |

[src] Orcadas Base to Ushuaia: **1,502 km (811 nmi)** (en.wikipedia Orcadas_Base; es.wikipedia: 1,501 km) — Orcadas is 0.8° east of Signy, and [GC-calc] Ushuaia to Orcadas is 1,534 km, so the sources' figure is a few percent shorter than my great-circle arithmetic (cause unknown; source method unstated).

**Brazil claim: "nearest large populous Atlantic coast on the Scotia Sea, with a direct open-water run"**

- **"Nearest": CONTRADICTED.** From Signy: Tierra del Fuego (Ushuaia, Río Grande, Puerto Williams) at about 1,440 to 1,530 km; Falklands at 1,252 km; Argentina's Patagonian coast (Río Gallegos 1,762 km; Comodoro Rivadavia 2,179 km; Mar del Plata 2,660 km); Uruguay's coast (Punta del Este 2,940 km, Montevideo 2,968 km); and Brazil's southernmost coast (Chuí 3,057 km; Rio Grande 3,224 km) is **farther than each of these**. Brazil's northeast (Recife) is about 5,900 km (coordinate not sourced), Rio de Janeiro 4,207 km, Santos 4,089 km. **Argentina is nearest on every measure; Uruguay is nearer than Brazil.** **Brazil's most populous Atlantic cities (Rio, Santos) are 4,100 to 4,200 km away.**
- **"Direct open-water run": true as geometry.** [GC-calc] Rio Grande (BR) to Signy great circle runs through 39.2°S 51.0°W, 46.4°S 49.7°W, 53.6°S 48.0°W, i.e. **open South Atlantic about 7° of longitude (several hundred km) east of the Falkland Islands**, no land en route, arriving from the north-northwest (bearing 349° from Signy). The same is true of the Montevideo line (47.9°S 52.2°W midpoint). So "direct open-water" does not distinguish Brazil from Uruguay or Argentina.
- **"On the Scotia Sea":** the Scotia Sea "bounded on the west by the Drake Passage and on the north, east, and south by the Scotia Arc" (en.wikipedia Scotia_Sea); ~900,000 km², max depth 6,022 m; surrounded by Tierra del Fuego, South Georgia, South Sandwich Islands, South Orkneys and the Peninsula. **The South Orkneys are on the Scotia Arc's southern rim; no part of Brazil touches the Scotia Sea.** Tierra del Fuego does.
- **CONTEXT (b) only — Brazilian practice:** Brazil's national program (en/pt Wikipedia) runs ships (Almirante Maximiano, Ary Rongel) from Rio de Janeiro / support station at Rio Grande, and its Air Force (C-130 and KC-390) supplies Comandante Ferraz station "from Base Presidente Eduardo Frei Montalva in Chile, near Punta Arenas" (pt.wikipedia). That is the Peninsula/King George sector, not the South Orkneys. No Brazilian activity at the South Orkneys was found.

**South African leg: "a Cape Town–South Orkneys crossing"**

- **[GC-calc] Cape Town to Signy 5,376 km (2,903 nmi); to Orcadas 5,330 km (2,878 nmi); bearing from Signy to Cape Town 87°, i.e. due east.** The line passes 43.3°S 8.7°E, 51.6°S 4.4°W, 57.9°S 22.5°W (open ocean south of the South Atlantic gyre; arith. waypoints at 25/50/75%, not a navigation route).
- S.A. Agulhas II (home port Cape Town; range **15,000 nmi at 14 kn**; PC5 ice class) supplies SANAE IV, Marion and Gough Islands and in Feb to Mar 2022 was mother ship for the Endurance22 Weddell Sea expedition; the Endurance wreck was found at **68°44'21"S 52°19'47"W**, depth 3,008 m (en.wikipedia SA_Agulhas_II; Endurance_(1912_ship)). [GC-calc] that site is 5,753 km from Cape Town and **947 km from Signy**. SANAE IV is "more than 4,000 km from mainland South Africa" (en.wikipedia SANAE_IV) — this is the only South African Antarctic crossing distance sourced.
- Cape Town is one of five "gateway cities": "farthest from Antarctica", serves South Africa plus "Russia, Germany, Belgium, Norway, Japan", flights to private airfields (White Desert) since 2021 (en.wikipedia, Wikivoyage). **No source ties a South African program or Cape Town service to the South Orkneys.** Historical only: the Scottish National Antarctic Expedition's Scotia wintered at Laurie Island (arrived 25 Mar 1903), called at Stanley, **Buenos Aires** (24 Dec 1903) and then reached **Cape Town on 6 May 1904** via Coats Land and Gough Island (en.wikipedia SNAE) — the Scotia reached Cape Town from the Weddell Sea, not from Laurie Island directly.
- **Verdict (South Africa): PARTLY SUPPORTED** — the 5,400 km (2,900 nmi) open-ocean distance and due-east bearing are real arithmetic; the *operational* Cape Town–South Orkney crossing was **not verifiable**.

**Sea conditions**

- Sea ice: "ice-covered from late April to November" (en.wikipedia South_Orkney_Islands). Weddell Sea: "much of the southern part … permanent, massive ice shelf field, the Filchner–Ronne"; historian T. R. Henry: "the most treacherous and dismal region on Earth"; "strong ice-class vessels equipped with helicopters are required" to reach remote colonies (en.wikipedia Weddell_Sea). Scotia Sea: "many icebergs melt in these waters" (en.wikipedia). Oceanwide Expeditions lists the South Orkney Islands among destinations from Ushuaia (oceanwide-expeditions.com/destinations/antarctica); Wikivoyage Ushuaia: itineraries include "South Georgia Island, South Orkney Islands, South Shetland Islands or the Antarctic Peninsula" from November to March. Wikivoyage Southern Ocean: "roaring forties, filthy fifties and screaming sixties"; storms "unobstructed by any land"; icebergs "as far as 50°S".
- **Nothing was obtained on the Weddell ice edge's actual northern limit, on iceberg density on the Rio Grande/Cape Town approaches, or on seasonal sea-ice extent figures (NSIDC).** Died at the query (no search) and at the sources (Wikipedia pages give no extent figures).
- **CONTEXT (b) only:** Signy is run by the British Antarctic Survey (seasonal Nov to Apr). BAS vessel RRS Sir David Attenborough is registered at **Stanley**; BAS aircraft shuttle "between either Port Stanley Airport … or Punta Arenas … and Rothera" (en.wikipedia). **How Signy is supplied today was not found** (BAS pages returned empty).

**Verdict: CONTRADICTED for "nearest" (Brazil); geometry of open-water run is TRUE but not Brazil-specific; South Africa leg PARTLY SUPPORTED.**

**Searches / URLs opened:** en.wikipedia Signy_Research_Station, Signy_Island, South_Orkney_Islands, Laurie_Island, Coronation_Island, Orcadas_Base, Scotia_Sea, Weddell_Sea, South_Georgia_and_the_South_Sandwich_Islands, Stanley,_Falkland_Islands, Rio_Grande,_Rio_Grande_do_Sul, Port_of_Rio_Grande, Chuí, Santos,_São_Paulo, Rio_de_Janeiro, Recife, Cape_Town, SA_Agulhas_II, SANAE_IV, Scottish_National_Antarctic_Expedition, Endurance_(1912_ship), RRS_Sir_David_Attenborough, British_Antarctic_Survey, ARA_Almirante_Irízar, Brazilian_Antarctic_Program, Comandante_Ferraz_Antarctic_Station; pt.wikipedia Programa_Antártico_Brasileiro, Estação_Antártica_Comandante_Ferraz, NApOc_Almirante_Maximiano; es.wikipedia Base_Orcadas, Islas_Orcadas_del_Sur; en.wikivoyage Southern_Ocean, Ushuaia, Cape_Town, Falkland_Islands, South_Orkney_Islands; oceanwide-expeditions.com.

**Dead ends:**
- bas.ac.uk (home and `/polar-operations/sites-and-facilities/facility/signy/`): **died at the sources** (empty content returned).
- en.wikipedia Endurance22 / Endurance22_expedition: 404 (**source**); the Cape Town departure date and transit time to the Weddell Sea were **not obtained**.
- en.wikivoyage South_Orkney_Islands: redirected to a Southern Ocean overview; the Southern_Ocean page itself 404 on one try and returned content on another (mixed).
- Brazilian Navy / PROANTAR official pages: not reached.
- Shipping-route distances Cape Town to South Orkneys or Rio Grande to South Orkneys: **died at the query** (no search) and at the sources.

**Single-source:** Orcadas to Ushuaia 1,502 km (en.wikipedia; es.wikipedia gives 1,501); Orcadas population (65 summer / 17 winter; es.wikipedia "45 summer", conflict); "SANAE more than 4,000 km from mainland South Africa"; Almirante Irízar home port Buenos Aires.

**Open threads:** (a) South Orkney ice season and iceberg/sea-ice limits from NSIDC / BAS / IAATO; (b) any real Cape Town to South Orkneys voyage (SA Agulhas II voyage reports, Norwegian whaling-era Cape Town links); (c) whether Brazilian Navy or Argentine operators have ever staged to Signy; (d) shipping-route distance and days Ushuaia to Signy (operators' itineraries); (e) the Falklands-to-Signy BAS supply route.

---

## 3. Conflicts between sources (do not average; resolve with a better source)

| Item | Values found | Notes |
|---|---|---|
| Cape Horn to Antarctica | 650 km (en.wikipedia Cape_Horn) vs 800 km (Drake_Passage, Cape_Horn same page) vs 808.17 km (es.wikipedia) vs 809 km (Livingston page) | [GC-calc] 826 to 844 km to Smith/Livingston/King George centers. **650 km is unsupported.** |
| Ushuaia to the Peninsula | ~1,000 km (Antarctic Peninsula, gateway-city pages), "1,100 km" (en.wikipedia Ushuaia), "1,150 km to Esperanza" (es.wikipedia) | Different endpoints. |
| Peninsula tip from South America | "about 1,000 km" (Antarctic Peninsula page) vs "some 1600 km" (Wikivoyage Antarctic Peninsula) | Wikivoyage probably measures to the mainland proper or is in error. |
| Flight Punta Arenas to King George | "two hours" (antarctica21.com; Wikivoyage Antarctica) vs "roughly 4 hours" (Wikivoyage Southern Ocean) | Unresolved. |
| Punta Arenas population | 132,363 (2024, en.wiki) / 131,067 (es.wiki region page) / 123,403 (2017) and 148,391 ("2023") (es.wiki city page) / ~125,000 (2015, Wikivoyage) | The 148,391 figure looks wrong beside the 2024 census; **not checked against INE tables** (the INE page opened gave only the national total). |
| Puerto Williams | 1,868 (2017) / 2,874 incl. naval / ~1,900 (2017) / Cabo de Hornos commune 2,262 (2017) and 1,750 (2024) | Definition (naval or not) differs. |
| Ushuaia | 79,538 (2022, es.wiki) vs 89,606 and "84,378 (2026 census)" (en.wiki) | en.wikipedia's "2026 census" label is suspicious; **no INDEC table opened.** |
| Port Lockroy visitors | ~18,000 per season (en.wikipedia) vs ~10,000 annually (Wikivoyage) | Different years likely. |
| Orcadas summer population | 65 (en.wiki Orcadas_Base) vs 45 (en/es Laurie Island and Orcadas pages) | |
| Livingston coordinate | 62°36'S 60°30'W (island) vs 62°39'47"S 60°23'17"W (Juan Carlos I base, matches the site) | Not a conflict; different referents. |

---

## 4. Surprising or notable

1. **No source opened presents Montevideo or the Río de la Plata as an Antarctic gateway.** The five recognized gateway cities named by Wikipedia are Punta Arenas, Ushuaia, Cape Town, Hobart, Christchurch. Wikivoyage Punta Arenas does mention some cruises from Buenos Aires, Rio de Janeiro, São Paulo and Valparaíso. Uruguay's own station page names **Ushuaia** as its "nearest commercial port." This is the biggest finding against the Pergamino wording.
2. The great-circle line from Montevideo to Livingston passes through or beside the **Falkland Islands** (about 58°W at 51.7°S) [GC-calc]. Montevideo, Stanley and the South Shetlands are nearly on one meridian.
3. **The Drake's narrowest crossing runs to Livingston/Smith, not King George.** Cape Horn to King George is about 840 km, the western end of the chain is about 826 to 830 km [GC-calc].
4. **Ushuaia is only 22 km farther than Puerto Williams from Port Lockroy** (1,145 vs 1,123 km) and **34 km farther from King George** (983 vs 949 km); the two towns are 46 km apart across the Beagle Channel. "Chile's Magallanes coast" and "Argentina's Fuegian coast" are one geographic unit for these distances.
5. **Punta Arenas, the Chilean regional population center, is the farthest of the Fuegian gateways** from all three Peninsula/South Shetland sites (660 to 736 nmi vs 513 to 618 nmi). It is nearest only if a population threshold of about 100,000 is set (Río Grande, Arg., is 98,017).
6. **Brazil's Rio Grande is 3,224 km from Signy; Uruguay's Montevideo is 2,968 km and Argentina's Mar del Plata is 2,660 km** [GC-calc]. The ranking in the Brazil claim is inverted. (This is a distance fact about real coasts, not a comparison between project cities.)
7. **Cape Town is almost due east of the South Orkneys** (bearing 87°) at 5,376 km: a pure open-ocean east-west run across the whole South Atlantic, longer than any Latin American coast in the table.
8. **Endurance22 wreck site is 947 km from Signy** and was reached by a Cape Town ship [GC-calc; en.wikipedia]: the only documented modern South African voyage in the Weddell/South Orkney region, but not to the islands.
9. Wikipedia en lists ROU Vanguardia as **decommissioned 2 Sept 2026** (single source, after the project's "present"); may be a recent edit worth verifying.
10. Cape Horn island has a Chilean Navy family of **five** (2019) and Isla de los Estados a four-man naval rotation: the two nearest land points to the South Shetlands are staffed, not populated.

---

## 5. Claims that could NOT be verified

1. The operational route of Uruguayan Hercules flights (Montevideo / Punta Arenas / King George).
2. Any standard or published ship-crossing duration in hours for Ushuaia/Punta Arenas to the Peninsula/South Shetlands from an official or port-authority source (only "two days" from one operator and Wikivoyage).
3. Any shipping-route (non-great-circle) distance for any pair.
4. Which sea approach cruise ships actually use to reach Wiencke Island (Bransfield/Gerlache vs. Bismarck Strait).
5. Current resupply route and port for Signy Research Station.
6. A real Cape Town to South Orkneys crossing, and the Weddell/Scotia sea-ice limits by month.
7. Authoritative (INE / INDEC) municipal populations for Punta Arenas, Puerto Williams, Ushuaia.
8. Any primary (government/port-authority/academic) source for anything above.

---

## 6. Search strings attempted (all returned "web search budget exhausted"; **0 searches executed**)

1. `Uruguay Antarctic logistics Montevideo Punta Arenas Artigas base King George Island Uruguayan Air Force flights`
2. `Drake Passage width km Cape Horn to South Shetland Islands distance`
3. `Punta Arenas to King George Island flight Teniente Rodolfo Marsh Martin airfield Chilean Air Force flight time`
4. `Cape Town to South Orkney Islands distance nautical miles Signy Island`

All other evidence came from direct page fetches (listed per section). Queries the developer should run with a restored budget (multi-angle, in Spanish and Portuguese too): `Uruguay Hércules Antártida vuelo Montevideo Punta Arenas Base Artigas campaña`, `ROU Vanguardia campaña antártica Montevideo Punta Arenas travesía días`, `Puerto Williams Antártida distancia Cabo de Hornos Islas Shetland del Sur`, `Punta Arenas King George Island flight duration hours DAP BAe 146`, `Drake Passage crossing time hours Ushuaia South Shetlands Port Lockroy itinerary`, `Signy Island resupply RRS Sir David Attenborough Stanley South Orkney`, `S.A. Agulhas II South Orkney Islands voyage Cape Town`, `South Orkney Islands sea ice extent season NSIDC`, `Estación Antártica Comandante Ferraz navio Rio Grande Punta Arenas tempo travessia Península Antártica`, `INDEC censo 2022 Ushuaia población`, `INE censo 2024 Punta Arenas Puerto Williams población`.

---

## 7. Coordinates used for the [GC-calc] figures (with where each was quoted)

Juan Carlos I Base 62°39'47"S 60°23'17"W (en.wikipedia); Port Lockroy 64°49'31"S 63°29'40"W (en.wikipedia); Villa Las Estrellas 62°12'02"S 58°57'50"W (es.wikipedia); Artigas 62°11'05"S 58°54'12"W (es.wikipedia); Signy station 60°42'30"S 45°35'42"W; Orcadas 60°44'17"S 44°44'16"W; Montevideo 34°54'20"S 56°11'03"W; Buenos Aires 34°36'14"S 58°22'53"W; Mar del Plata 38°0'S 57°33'W; Punta del Este 34°58'S 54°57'W; Rio Grande (BR) 32.035°S 52.099°W; Chuí 33°41'28"S 53°27'24"W; Rio de Janeiro 22°54'40"S 43°12'20"W; Santos 23°56'13"S 46°19'30"W; Cape Town 33°55'31"S 18°25'26"E; Punta Arenas 53°09'45"S 70°54'29"W (es.wikipedia); Puerto Williams 54°56'S 67°37'W; Ushuaia 54°48'26"S 68°18'29"W; Río Grande (Arg.) 53°47'S 67°42'W; Río Gallegos 51°37'24"S 69°12'58"W; Comodoro Rivadavia 45°51'53"S 67°28'51"W; Stanley 51°41'42"S 57°51'02"W; Cape Horn 55°58'48"S 67°17'21"W; Isla de los Estados 54°47'S 64°15'W (island center, not its nearest tip); Diego Ramírez 56°29'S 68°44'W; Smith I. 63°00'S 62°30'W; Livingston (center) 62°36'S 60°30'W; King George (center) 62°02'S 58°21'W; Elephant I. 61°08'S 55°07'W; King Edward Point 54°17'S 36°30'W; Endurance wreck 68°44'21"S 52°19'47"W. **Recife coordinate (8.05°S 34.88°W) was NOT in a source** (the page opened gave none) and is used only for the one approximate row, flagged as such. Island-center coordinates can shift a distance by about 10 to 40 km.
