# Heat P4: city screen for plant-heat reuse (repo only, no web), 2026-11-02

**Started:** 2026-11-02 21:08 MST (system clock). **Unit:** P4 of `Power_Plant_Heat_Research_BRIEF_2026-11-02.md`. **Method:** repo reading only; no web search, no web fetch.

**Scope.** This file lists, for every city in the census, the facts the repo already holds that a later screen for reusing power-plant heat would need: population, war status, site setting, elevation, latitude, nearest sea, temperatures, geothermal status, canon power sources, and food role. It then quotes every place the files already mention waste heat, cogeneration, district heating, or a nearby reactor or plant, and ends with the list of facts the files do not hold. **Facts only. No ranking, no recommendation, no judgment about which city suits heat reuse.** Labels: **SOURCED** (read at the file and line cited), **DERIVED** (my arithmetic on sourced figures, with the working shown), **NOT IN FILES** (looked for in the files named in the brief and the Specs; absent). Nothing here is UNVERIFIED unless marked.

**Which cities.** All 38 rows of the census city table (`Official_Population_Census.md` L494 to L531 for Census I, with Relung Panen at L514). The census still uses the old city names; the alias table (`City_Renames_Alias_Table_2026-10-03.md` L9 to L12 and L102 to L105) maps them: Abowasa is Santa Luce, Sayowa is Temirötkel, Princess Elisabeth is Utstein, Vostok is Ariun Nuur, Juan Carlos is Pergamino, Port Lockroy is Puerto Abrigo, Sejong is Contrapunto. Current names are used below, with the census name in the identity table. The Maritime fleet row (non-city, `Official_Population_Census.md` L532) is not a city and is left out of the screen.

## Citation key (all paths under `.../Tepenian-Federation/Locations/` unless noted)
- **Census** = `Cities/Official_Population_Census.md`. **Alias** = `Cities/City_Renames_Alias_Table_2026-10-03.md`. **RDB** = `Cities/City_Relationship_Database.md`.
- **Spec <City> Ln** = `Cities/Specs/<subnet> subnet/<City>.md` line n.
- **DS <City> <File> Ln** = `Cities/City_Development_Passes/<Subnet>_Subnet/<City folder>/Datasheets/<File>.md` line n (for example `DS Janbogo Phase_3 L18`).
- **READER <City>** = `Reference/Real-World/Climate Data/READER/<City>.md` (under the GDD root, `.../InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/`).
- **GEO** = `Infrastructure/Geothermal_Heating.md`. **PWR** = `Infrastructure/Amundsen_Power_Supply.md`. **PORTS** = `Infrastructure/Ports.md`.
- **DoI13 / DoI16 / DoI19 / DoI12 / DoI08** = `Cities/Division_of_Industry/13_National_Balance_Under_the_Ruling.md`, `16_Per_City_Three_Tier_Run.md`, `19_National_Balance_Refresh_2026-11-02.md`, `12_Terraforming_and_the_Outdoor_Tier.md`, `08_Volume_Based_Requirement_Reference.md`.
- **LOGI** = `Worldspace/City_Logistics.md` (two levels up from `Locations-and-Levels/`, under the GDD `Worldspace/` root).

## PROGRESS
- [x] Brief and the applicable rules of the fusion brief read.
- [x] Q1 city table (identity and population, site, climate, geothermal and power) for all 38 census rows.
- [x] Q2 food role per city, quoted with file and line.
- [x] Q3 every mention of waste heat, cogeneration, district heating or a nearby reactor in the canon files (not in culture files or `graphify-out/`, which were not read).
- [x] Q4 list of facts the files do not hold.
- [x] FINAL section and read log written.

## Rules and cautions that bind the figures below
1. **There is no present-day census.** `Census` L631: "No genuine Census III (an actual present-day, post-war population table) exists anywhere in this project yet." So "current population" below is **Census I** (peak, pre-orbital; live values after the 2026-10-28 Santa Luce and 2026-11-02 Esperanza arithmetic) and **Census II** (the pre-war snapshot after orbital migration). Neither is a post-war count. Census rows record bookkeeping, not events (`Census` L732 to L738).
2. **Division of Industry citation gate** (`Universal_Location_Methodology/Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md` L34 to L46): a city's sector shares, workforce, difficulty and baseline load are citable; any export or deficit headcount, any "feeds N people", and the national food balance are not. Section 2 respects that: it states each city's food role and sector share only. The food layer's older figures are marked superseded where the files say so (`DoI13` L1).
3. The 13 file's per-city classification of 2026-09-01 (its section 6) was **superseded** by its section 15 (2026-09-02, `DoI13` L839). Where both exist, section 15 and file 16 govern.
4. **Mean winter, degree-days and "months below 0" are DERIVED by me from the monthly means in the files; no file gives heating degree-days** (the only degree-day figures in the files read are Relung Panen's, quoted under table 1C). Working is shown under table 1C.

---

## 1. City table (all 38)

### 1A. Identity, population and war status

| # | City (census name if different) | Subnet | Census I combined (live) | Census II combined | War status (as the spec states) |
|--:|---|---|--:|--:|---|
| 1 | Amundsen Station | Amundsen | 6,857 (`Census` L531) | 4,891 (`Census` L670) | Destroyed (Long Night War) (`Spec Amundsen_Station L4`) |
| 2 | Byrd | Byrd | 429,009 (`Census` L523) | NOT IN FILES (no Census II row) | Survived; struggling (`Spec Byrd L50`) |
| 3 | Belgrano | Halley | 1,124,011 (`Census` L508) | 873,648 (`Census` L648) | Ruins (survived the war, ruined after) (`Spec Belgrano L4; Census L823`) |
| 4 | Halley | Halley | 1,504,467 (`Census` L498) | 1,123,950 (`Census` L639) | Damaged; partially operational (`Spec Halley L4`) |
| 5 | Lazar | Halley | 2,410,409 (`Census` L494) | 1,659,460 (`Census` L637) | Damaged; partially operational (`Spec Lazar L5`) |
| 6 | Neumayer | Halley | 1,304,201 (`Census` L504) | 866,628 (`Census` L649) | Damaged; partially operational (`Spec Neumayer L4`) |
| 7 | Sanay | Halley | 515,789 (`Census` L517) | 310,996 (`Census` L664) | Damaged; partially operational (`Spec Sanay L5`) |
| 8 | Santa Luce (census: Abowasa) | Halley | 465,818 (`Census` L511) | 278,855 (`Census` L657) | Damaged; partially operational (`Spec Santa_Luce L6`) |
| 9 | Troll | Halley | 1,006,570 (`Census` L513) | 707,711 (`Census` L655) | Damaged; partially operational (`Spec Troll L4`) |
| 10 | Utstein (census: Princess Elisabeth) | Halley | 1,190,038 (`Census` L507) | 802,643 (`Census` L651) | Destroyed (ruins; some survivors) (`Spec Utstein L6`) |
| 11 | Cape Adare | Janbogo | 1,551,776 (`Census` L496) | 1,085,931 (`Census` L640) | Destroyed (`Spec Cape_Adare L4`) |
| 12 | Concordia | Janbogo | 1,068,065 (`Census` L512) | 671,180 (`Census` L656) | Survived (last major city) (`Spec Concordia L4`) |
| 13 | Denison | Janbogo | 958,340 (`Census` L510) | 659,355 (`Census` L652) | Destroyed (`Spec Denison L4`) |
| 14 | Dumont d'Urville | Janbogo | 408,001 (`Census` L518) | 280,805 (`Census` L663) | Damaged; partially operational (`Spec Dumont_dUrville L4`) |
| 15 | Fort McMurdo | Janbogo | 445,310 (`Census` L519) | 338,169 (`Census` L660) | Damaged; partially operational (`Spec Fort_McMurdo L4`) |
| 16 | Janbogo | Janbogo | 1,362,629 (`Census` L501) | 993,450 (`Census` L644) | Damaged; partially operational (`Spec Janbogo L4`) |
| 17 | Scott | Janbogo | 386,011 (`Census` L522) | 313,634 (`Census` L662) | Damaged; partially operational (`Spec Scott L4`) |
| 18 | Zukelli | Janbogo | 1,310,769 (`Census` L503) | 973,539 (`Census` L646) | Destroyed (`Spec Zukelli L4`) |
| 19 | Dome Fuji | Mawson | 80,120 (`Census` L530) | NOT IN FILES (no Census II row) | Survived (reduced capacity; robot-only) (`Spec Dome_Fuji L31`) |
| 20 | Mawson | Mawson | 1,498,852 (`Census` L499) | 988,325 (`Census` L645) | Damaged; partially operational (`Spec Mawson L4`) |
| 21 | Temirötkel (census: Sayowa) | Mawson | 225,376 (`Census` L526) | 164,957 (`Census` L667) | Damaged; partially operational (`Spec Temirotkel L7`) |
| 22 | Ariun Nuur (census: Vostok) | Mirny | 441,378 (`Census` L520) | NOT IN FILES (no Census II row) | Survived (remote) (`Spec Ariun_Nuur L6`) |
| 23 | Casey | Mirny | 1,547,850 (`Census` L497) | 1,077,910 (`Census` L641) | Destroyed (Long Night War) (`Spec Casey L4`) |
| 24 | Davis | Mirny | 1,210,432 (`Census` L506) | 817,475 (`Census` L650) | Damaged; partially operational (`Spec Davis L4`) |
| 25 | Kunlun | Mirny | 148,497 (`Census` L529) | NOT IN FILES (no Census II row) | Survived (very marginal; robot-only) (`Spec Kunlun L21`) |
| 26 | Mirny | Mirny | 1,403,549 (`Census` L500) | 1,052,374 (`Census` L642) | Damaged; partially operational (`Spec Mirny L4`) |
| 27 | Relung Panen | Mirny | 1,000,071 (`Census` L514) | 714,045 (`Census` L654) | UNDETERMINED (no war outcome ruled) (`Spec Relung_Panen L9`) |
| 28 | Shirayuki | Mirny | 1,112,600 (`Census` L505) | 691,371 (`Census` L653) | Damaged; partially operational (`Spec Shirayuki L7`) |
| 29 | Sinheung | Mirny | 1,014,533 (`Census` L509) | 835,341 (`Census` L647) | Damaged; partially operational (`Spec Sinheung L5`) |
| 30 | Zhongshan | Mirny | 1,203,607 (`Census` L502) | 932,895 (`Census` L643) | Damaged; partially operational (`Spec Zhongshan L4`) |
| 31 | Contrapunto (census: Sejong) | Palmer | 644,833 (`Census` L515) | 514,070 (`Census` L658) | Destroyed (`Spec Contrapunto L6`) |
| 32 | Esperanza | Palmer | 1,200,000 (`Census` L495) | 753,159 (`Census` L638) | Destroyed (spec); city kept smaller by DR-90 (`Spec Esperanza L4; Census L495`) |
| 33 | Marambio | Palmer | 570,269 (`Census` L516) | 430,145 (`Census` L659) | Destroyed (`Spec Marambio L4`) |
| 34 | Palmer City | Palmer | 332,808 (`Census` L524) | 332,170 (`Census` L661) | Destroyed (Long Night War) (`Spec Palmer_City L4`) |
| 35 | Pergamino (census: Juan Carlos) | Palmer | 386,692 (`Census` L521) | 246,372 (`Census` L666) | Destroyed (`Spec Pergamino L6`) |
| 36 | Puerto Abrigo (census: Port Lockroy) | Palmer | 929 (`Census` L528) | 691 (`Census` L669) | Damaged; partially operational (`Spec Puerto_Abrigo L6`) |
| 37 | Rothera | Palmer | 317,449 (`Census` L525) | 255,857 (`Census` L665) | Damaged; partially operational (`Spec Rothera L4`) |
| 38 | Signy | Palmer | 188,694 (`Census` L527) | 133,755 (`Census` L668) | Survived; fully operational (`Spec Signy L4`) |

*Notes.* Census II has no row for Byrd, Ariun Nuur (Vostok), Kunlun or Dome Fuji (`Census` L675). Kunlun and Dome Fuji have zero humans (`Census` L529, L530). Esperanza's Census I figure is the relocated 1,200,000 (`Census` L495, `DR-90`); its older 1,902,205 is no longer live. Puerto Abrigo's 929 is a deliberate reduction (`Census` L528). Port Lockroy, Dumont d'Urville, Denison, Lazar, Zhongshan, Shirayuki and Sinheung rows carry held-overflow notes that are bookkeeping, not migration (`Census` L726 to L762).

### 1B. Site: setting, elevation, nearest sea

Setting words are the files' own. Elevation is given only where a file states one. 'Nearest sea' is a figure only where a file states one; otherwise the table says what the file says about the coast.

| City | Setting (quoted or paraphrased closely) | Elevation | Distance to nearest sea |
|---|---|---|---|
| Amundsen Station | South Pole, interior ice sheet; ICE-SHEET tier, about 2,850 m of plateau ice (RDB L80; DoI16 L3458) | 2,835 m (DS Amundsen_Station Step_1_and_2 L40, COMNAP: 'elevation 2,835 m'; 'about 2,700 m (9,000 feet) thick') | Landlocked, deep interior (PORTS L482); distance NOT IN FILES as a figure |
| Byrd | West Antarctica, inland on the West Antarctic Ice Sheet; ICE-SHEET tier, bedrock 2,164 m down (RDB L124; DoI13 L851; DoI16 L3355) | approximately 1,530 m (Spec Byrd L167); station record 1,543.2 m (DS Byrd Phase_3 L19) | Interior; PORTS L483 lists it among 'Interior nunatak / inland'; distance NOT IN FILES |
| Belgrano | Weddell Sea coast on a floating ice shelf; ICE-SHELF tier, 'No bedrock at all. Floating on the sea' (RDB L91; DoI13 L776) | NOT IN FILES for the canon city (the real Bertrab Nunatak base is quoted at 256 m, DoI13 L164, but canon puts the city on the shelf, DoI13 L778 to L800) | On the Weddell Sea coast (RDB L91); distance NOT IN FILES as a figure |
| Halley | Brunt Ice Shelf, a floating ice shelf; 'the city that moves' (Spec Halley L7, L8; RDB L245; DoI13 L776) | NOT IN FILES | On the shelf over the Weddell Sea; distance NOT IN FILES as a figure |
| Lazar | Schirmacher Oasis, a rock oasis 25 km long and up to 3 km wide, 34 km2; rock-founded; 86 to 90 percent of the city stands on ice (DoI13 L540; Census L494) | oasis maximum elevation 228 m (DoI13 L540) | 80 km from the Lazarev Sea coast (DoI13 L540); PORTS L483 lists it as interior |
| Neumayer | Ekstrom Ice Shelf, Atka Bay; ICE-SHELF tier (Census L146; DoI13 L776) | NOT IN FILES | On the shelf at Atka Bay; distance NOT IN FILES as a figure |
| Sanay | Vesleskarvet nunatak, bedrock (Census L176; DoI16 L711) | about 850 m (PORTS L461: 'at ~850 m elevation'); AWS 817 m (DS Sanay Phase_3 L16) | about 220 km inland, about 160 km from the ice-shelf edge (PORTS L461); landlocked (PORTS L485 to L488) |
| Santa Luce | Basen nunatak, Kraul Mountains (Vestfjella), a rock outcrop on the mainland ice sheet (Spec Santa_Luce L94; DoI16 L659) | 484 m (DS Santa_Luce Phase_3 L16, station notes) | roughly 130 km inland (Spec Santa_Luce L94; DoI13 L166); landlocked (PORTS L483) |
| Troll | Jutulsessen nunatak, bedrock (Census L156; DoI16 L765) | 1,275 m (DoI13 L162, the real-station basis) | 235 km inland (Spec Troll L100; DoI13 L162); landlocked (PORTS L483) |
| Utstein | Utsteinen nunatak, Sor Rondane Mountains, inland (Census L188; RDB L380) | 1,382 m (DoI13 L163, the real-station basis) | inland; landlocked (PORTS L483); distance NOT IN FILES as a figure |
| Cape Adare | Ross Sea coast, northern entrance, a rock-founded cape (RDB L143; DoI16 L2666) | NOT IN FILES (the climate proxy, Possession Island AWS, is quoted at 30 m, DS Cape_Adare Phase_3 L29) | On the coast (Ridley Beach, a landing only, PORTS L195); distance 0 by site, not stated as a figure |
| Concordia | Dome C on the East Antarctic plateau; ICE-SHEET tier, 3 km or more of ice (Spec Concordia L3, L112; DoI13 L775) | 3,233 m (RDB L177; Spec Concordia L112) | about 1,100 km from the coast (DoI13 L179); PORTS L482 lists it as deep interior |
| Denison | Cape Denison, Commonwealth Bay; ice-free rock about 900 by 700 m, 0.63 km2 (DoI13 L185 to L186); rock-founded (DoI16 L2584) | NOT IN FILES | On the coast (Boat Harbor, PORTS L194); distance 0 by site, not stated as a figure |
| Dumont d'Urville | Petrel Island, Geologie Archipelago, about 5 km off the continental coast (Spec Dumont_dUrville L8); rock-founded (DoI13 L857 to L859) | NOT IN FILES | about 5 km off the continental coast (Spec Dumont_dUrville L8); an island city, in the sea |
| Fort McMurdo | Ross Island, volcanic rock, connected to the mainland by seasonal sea ice across McMurdo Sound (Spec Fort_McMurdo L96; DoI13 L857 to L859) | NOT IN FILES | Island city on the Ross Sea (Winter Quarters Bay, PORTS L199) |
| Janbogo | Terra Nova Bay, mainland coast; rock-founded; a year-round polynya port (Census L240; DoI16 L2835; PORTS L306) | NOT IN FILES | On the bay (PORTS L306); distance 0 by site, not stated as a figure |
| Scott | Ross Island, volcanic rock, next to Fort McMurdo (RDB L413; DoI13 L857 to L859) | NOT IN FILES | Island city on the Ross Sea (PORTS L199) |
| Zukelli | Terra Nova Bay, mainland coast, about 8 km from Janbogo (Census L250; GEO L30) | NOT IN FILES | On the bay, shares Janbogo's port (GEO L171) |
| Dome Fuji | East Antarctic plateau, inland; ICE-SHEET tier (RDB L199; DoI13 L776) | about 3,810 m (RDB L200; Spec Dome_Fuji L146) | Deep interior (PORTS L482); distance NOT IN FILES as a figure |
| Mawson | Indian Ocean coast, Holme Bay, rock-founded; Horseshoe Harbor, 'the only natural rock harbor' (RDB L325; DoI16 L3267; PORTS L203) | NOT IN FILES | On the coast (Horseshoe Harbor); distance 0 by site, not stated as a figure |
| Temirötkel | East Ongul Island, offshore, rock-founded (RDB L455; DoI13 L857 to L859) | NOT IN FILES | about 4 km from the mainland, in Lutzow-Holm Bay, frozen in (RDB L455; PORTS L205) |
| Ariun Nuur | East Antarctic plateau near the Southern Pole of Inaccessibility; ICE-SHEET tier (Spec Ariun_Nuur L66; DoI16 L2353) | 3,488 m (Spec Ariun_Nuur L66; RDB L479) | 'approximately 1,260 kilometers from Mirny on the coast' (Spec Ariun_Nuur L66); deep interior (PORTS L482) |
| Casey | Wilkes Land coast, Bailey Peninsula-adjacent, rock-founded (DoI16 L2185; RDB L165) | NOT IN FILES | On the coast (Newcomb Bay, PORTS L196); distance 0 by site, not stated as a figure |
| Davis | Vestfold Hills, 'the largest ice-free coastal oasis in Antarctica, ~400 km2' (DoI16 L2010) | NOT IN FILES | On the coast (Prydz Bay, PORTS L201); distance 0 by site, not stated as a figure |
| Kunlun | Dome A, the highest point of the East Antarctic Ice Sheet; ICE-SHEET tier (Spec Kunlun L25, L89; RDB L278) | 4,093 m (RDB L279; Spec Kunlun L89) | Deep interior (PORTS L482); distance NOT IN FILES as a figure |
| Mirny | Davis Sea coast; structures on 'four rock outcrops at Mabus Point' (DoI13 L854; RDB L336) | NOT IN FILES | On the coast; distance 0 by site, not stated as a figure |
| Relung Panen | Bunger Hills oasis on the Knox Coast, 'East Antarctic coastal OASIS, shelf-sealed': ice-free basin cut off from open sea by 64 to 145 km of ice shelf (DS Relung_Panen Step_1_and_2 L15; RDB L113) | NOT IN FILES | the oasis is '50 to 85 km inland' (PORTS L198); '64-145 km of ice shelf' to open sea (DS Relung_Panen Step_1_and_2 L15) |
| Shirayuki | Larsemann Hills, Prydz Bay; rock-founded; the three Larsemann cities share about 40 km2 of ice-free hills (DoI16 L1758; Census L754) | NOT IN FILES | On Prydz Bay, shared 'Tri-Cities Port, Nella Fjord' (PORTS L202); distance 0 by site, not stated as a figure |
| Sinheung | Larsemann Hills, Prydz Bay; rock-founded; same hills as Shirayuki and Zhongshan (DoI16 L1838; Census L754) | NOT IN FILES | On Prydz Bay (PORTS L202) |
| Zhongshan | Larsemann Hills, Prydz Bay; 'ice-free oasis'; rock-founded (DoI16 L1921; Census L754) | NOT IN FILES | On Prydz Bay (PORTS L202) |
| Contrapunto | King George Island, South Shetland Islands (RDB L424; Spec Contrapunto L9) | NOT IN FILES | Island city; Marian Cove off Maxwell Bay; 160 to 177 km from the mainland Peninsula (Spec Contrapunto L9 to L10) |
| Esperanza | Hope Bay, Trinity Peninsula mainland, 'mainland Peninsula' (Spec Esperanza L7; DoI16 L1336) | NOT IN FILES | On Hope Bay (about 15 km2 of bay, DoI13 L588) |
| Marambio | Seymour Island, rock-founded, 'notably ice-free' (DoI13 L857; DoI16 L1462) | northern half a plateau, maximum elevation 'only ~180 m' (Spec Marambio L25) | Island city, joined to the mainland by a causeway chain (Spec Esperanza L7) |
| Palmer City | Anvers Island, rock-founded, island cap (DoI16 L1526; RDB L358) | NOT IN FILES | Island city; boat crossing from the mainland ramp (Spec Palmer_City L7) |
| Pergamino | Livingston Island, South Shetland Islands, Hurd Peninsula (RDB L267; Spec Pergamino L10) | NOT IN FILES | Island city; 110 km across the Bransfield Strait from the mainland Peninsula (Spec Pergamino L9); Espanola Cove (Spec Pergamino L10) |
| Puerto Abrigo | Goudier Island (Wiencke Island area), rock-founded (DoI16 L1616; Spec Puerto_Abrigo L10) | NOT IN FILES | Island city; harbor (Spec Puerto_Abrigo L10) |
| Rothera | Adelaide Island, rock-founded (DoI16 L1677; RDB L391) | NOT IN FILES | Island city (RDB L391); distance NOT IN FILES as a figure |
| Signy | South Orkney Islands, rock-founded island (DoI16 L944; RDB L435) | NOT IN FILES | Island city; Borge Bay is 'THE ONLY WAY IN' (Spec Signy L8) |

*Geology tiers (SOURCED, `DoI13` L845 to L847):* ROCK-FOUNDED 28 cities, ICE-SHEET 6 cities (Concordia, Ariun Nuur, Kunlun, Dome Fuji, Byrd, Amundsen Station), ICE-SHELF 3 cities (Halley, Neumayer, Belgrano). Landlocked list (`PORTS` L478 to L488): deep interior Concordia, Ariun Nuur, Dome Fuji, Kunlun, Amundsen Station; interior nunatak Byrd, Troll, Santa Luce, Utstein, Lazar; Sanay appears on both lists on purpose.

### 1C. Latitude and temperatures

Latitude is from the coordinate the spec gives (the datasheet cell names the spec line). Monthly means are the 1991 to 2020 WMO normals unless the note says otherwise. **PROXY** means the city has no station of its own and the files use a neighbor's values unmodified.

| City | Coordinates (cite) | Annual mean, stated (C) | 12 monthly means Jan..Dec (C), source | Mean winter JJA (DERIVED) | Months with mean below 0 (DERIVED) | HDD18 (DERIVED) | Note |
|---|---|--:|---|--:|--:|--:|---|
| Amundsen Station | 90°00'S (`Amundsen_Station Step_-1 L16`) | -49.1 | -28.1 -40.7 -53.6 -57.4 -57.7 -58.1 -60.2 -59.6 -58.9 -50.9 -37.2 -27.3 (`Amundsen_Station Phase_3 L17`) | -59.3 | 12 | 24,517 | - |
| Byrd | ~80°01'S, 119°31'W (`Byrd Step_-1 L17`) | -28.2 | -15.2 -20.1 -28.0 -30.1 -32.9 -34.5 -36.1 -36.7 -36.7 -31.0 -21.6 -14.9 (`Byrd Phase_3 L19`) | -35.8 | 12 | 16,859 | 1957-69 manned-years record, not a 1991-2020 normal (DS Byrd Step_1_and_2 L20) |
| Belgrano | ~77°52'S, 34°38'W (`Belgrano Step_-1 L16`) | -13.2 | -2.4 -7.0 -12.3 -16.3 -17.5 -18.9 -20.9 -20.7 -18.4 -14.1 -7.0 -2.6 (`Belgrano Phase_3 L17`) | -20.2 | 12 | 11,390 | - |
| Halley | ~75°35'S, 26°34'W (`Halley Step_-1 L17`) | -19.2 | -4.7 -10.4 -17.4 -23.3 -25.5 -27.5 -29.0 -29.1 -26.8 -20.2 -11.0 -5.3 (`Halley Phase_3 L18`) | -28.5 | 12 | 13,586 | - |
| Lazar | ~70°46'S, 11°44'E (`Lazar Step_-1 L16`) | -10.1 | -0.4 -3.2 -7.9 -11.8 -13.5 -14.5 -17.0 -17.2 -16.5 -12.0 -5.6 -1.0 (`Lazar Phase_3 L17`) | -16.2 | 12 | 10,251 | - |
| Neumayer | ~70°41'S, 8°16'W (`Neumayer Step_-1 L16`) | -16.0 | -4.1 -8.0 -13.5 -18.1 -20.4 -22.8 -25.3 -24.6 -23.3 -17.4 -9.8 -4.7 (`Neumayer Phase_3 L17`) | -24.2 | 12 | 12,424 | - |
| Sanay | ~71°40'S, 2°51'W (`Sanay Step_-1 L16`) | -16.2 | -6.7 -10.2 -14.3 -17.5 -19.4 -21.3 -23.2 -23.0 -21.7 -17.8 -11.7 -7.3 (`Sanay Phase_3 L17`) | -22.5 | 12 | 12,484 | AWS 2001-2026, not a READER station |
| Santa Luce | ~73°03'S, 13°25'W (`Santa_Luce Step_-1 L17`) | -15.0 | -5.2 -8.7 -13.5 -17.5 -19.0 -19.4 -21.5 -21.9 -20.8 -16.6 -10.5 -5.5 (`Santa_Luce Phase_3 L17`) | -20.9 | 12 | 12,059 | Aboa station Feb 1989-Oct 2001 record mean (DS Santa_Luce Phase_3 L16) |
| Troll | ~72°01'S, 2°32'E (`Troll Step_-1 L17`) | -17.2 | -6.7 -10.3 -14.2 -19.8 -21.1 -22.8 -25.2 -25.3 -24.0 -18.5 -11.4 -6.9 (`Troll Phase_3 L19`) | -24.4 | 12 | 12,853 | AWS record-period mean 1991-2025 |
| Utstein | ~71°57'S, 23°21'E (`Utstein Step_-1 L17`) | -18.0 | -9.0 -12.4 -16.9 -19.9 -20.6 -22.3 -24.3 -24.4 -23.7 -19.2 -13.3 -9.3 (`Utstein Phase_3 L17`) | -23.7 | 12 | 13,128 | station AWS16 2009-2020 |
| Cape Adare | ~71°17'S, 170°14'E (`Cape_Adare Step_-1 L20`) | -11.4 | +1.0 -2.1 -8.7 -16.0 -17.9 -17.2 -19.3 -20.0 -18.5 -13.2 -5.2 +0.6 (`Cape_Adare Phase_3 L30`) | -18.8 | 10 | 10,738 | Possession Island AWS proxy, ~75 km SE (DS Cape_Adare Phase_3 L29) |
| Concordia | ~75°06'S, 123°20'E (`Spec Concordia L3`) | -52.7 | -31.3 -43.3 -55.3 -62.1 -63.1 -64.1 -63.2 -63.3 -61.2 -54.5 -40.6 -30.7 (`READER/Concordia.md L14`) | -63.5 | 12 | 25,826 | READER Concordia, 1991-2020 |
| Denison | ~67°00'S, 142°40'E (`Denison Step_0 L18`) | -11.0 | -1.0 -4.4 -9.3 -13.5 -16.1 -16.7 -16.9 -16.6 -15.8 -13.2 -6.4 -1.6 (`Denison Phase_3 L18`) | -16.7 | 12 | 10,581 | PROXY: Dumont d'Urville values, unmodified (DS Denison Phase_3 L18); the DS notes the site runs colder in winter |
| Dumont d'Urville | ~66°40'S, 140°01'E (`Dumont_dUrville Step_-1 L20`) | -11.0 | -1.0 -4.4 -9.3 -13.5 -16.1 -16.7 -16.9 -16.6 -15.8 -13.2 -6.4 -1.6 (`Dumont_dUrville Phase_3 L26`) | -16.7 | 12 | 10,581 | - |
| Fort McMurdo | ~77°51'S, 166°40'E (`Fort_McMurdo Step_-1 L16`) | -16.2 | -2.7 -8.8 -17.1 -21.3 -21.5 -22.8 -24.9 -25.2 -23.0 -16.7 -8.3 -2.6 (`Fort_McMurdo Phase_3 L18`) | -24.3 | 12 | 12,510 | - |
| Janbogo | ~74°37'S, 164°13'E (`Janbogo Step_-1 L17`) | -14.0 | -1.2 -6.4 -14.1 -19.0 -20.0 -20.0 -21.8 -21.4 -19.8 -15.0 -7.3 -1.5 (`Janbogo Phase_3 L18`) | -21.1 | 12 | 11,677 | proxy Mario Zucchelli ~8 km |
| Scott | ~77°51'S, 166°46'E (`Scott Step_-1 L17`) | -19.6 | -4.6 -11.2 -20.6 -24.8 -26.2 -25.9 -28.8 -29.5 -26.8 -20.4 -11.1 -4.7 (`Scott Phase_3 L21`) | -28.1 | 12 | 13,720 | - |
| Zukelli | ~74°41'S, 164°07'E (`Zukelli Step_-1 L16`) | -14.0 | -1.2 -6.4 -14.1 -19.0 -20.0 -20.1 -21.8 -21.4 -19.8 -15.1 -7.3 -1.5 (`Zukelli Phase_3 L23`) | -21.1 | 12 | 11,683 | Mario Zucchelli READER |
| Dome Fuji | ~77°19'S, 39°42'E (`Dome_Fuji Step_-1 L19`) | -52.7 | -29.6 -41.5 -55.2 -62.9 -64.0 -65.1 -66.0 -64.2 -62.7 -52.6 -39.3 -29.7 (`Dome_Fuji Phase_3 L19`) | -65.1 | 12 | 25,832 | AWS record-period mean 1991-2025 |
| Mawson | ~67°36'S, 62°53'E (`Mawson Step_-1 L17`) | -11.2 | -0.3 -4.2 -10.2 -14.8 -16.7 -16.3 -17.8 -18.1 -16.9 -12.7 -5.3 -0.8 (`Mawson Phase_3 L18`) | -17.4 | 12 | 10,661 | - |
| Temirötkel | ~69°00'S, 39°35'E (`Temirotkel Step_-1 L17`) | -10.5 | -0.8 -2.9 -6.8 -10.4 -13.5 -15.2 -17.6 -18.7 -18.3 -13.3 -6.4 -1.5 (`Temirotkel Phase_3 L17`) | -17.2 | 12 | 10,398 | Syowa READER |
| Ariun Nuur | ~78°28'S, 106°52'E (`Ariun_Nuur Step_-1 L14`) | -54.8 | -31.9 -43.7 -58.1 -64.8 -65.6 -65.5 -65.9 -66.9 -65.7 -56.4 -41.4 -31.3 (`Ariun_Nuur Phase_3 L19`) | -66.1 | 12 | 26,575 | - |
| Casey | ~66°16'S, 110°32'E (`Casey Step_-1 L17`) | -9.3 | -0.3 -2.7 -7.2 -11.1 -14.7 -14.4 -14.7 -14.9 -13.8 -11.6 -5.3 -1.2 (`Casey Phase_3 L23`) | -14.7 | 12 | 9,986 | - |
| Davis | ~68°35'S, 77°58'E (`Davis Step_-1 L11`) | -10.0 | +0.9 -2.2 -8.0 -13.5 -16.0 -15.7 -17.1 -17.1 -15.7 -11.8 -4.2 +0.0 (`Davis Phase_3 L22`) | -16.6 | 10 | 10,247 | - |
| Kunlun | ~80°25'S, 77°07'E (`Kunlun Step_-1 L34`) | -53.9 | -34.9 -44.0 -55.2 -61.4 -62.4 -63.4 -63.7 -64.2 -62.9 -55.4 -44.3 -35.7 (`Kunlun Phase_3 L24`) | -63.8 | 12 | 26,278 | Dome A AWS record-period mean (DS Kunlun Phase_3 L24); spec says about -54 |
| Mirny | ~66°33'S, 93°01'E (`Mirny Step_-1 L19`) | -11.2 | -2.0 -5.2 -10.5 -13.9 -15.8 -15.4 -16.3 -16.4 -15.9 -13.4 -6.8 -2.7 (`Mirny Phase_3 L24`) | -16.0 | 12 | 10,666 | - |
| Relung Panen | ~66°15'S, 100°45'E (`Relung_Panen Step_-1 L18`) | -11.2 | +0.6 -2.1 -9.4 -14.9 -17.3 -17.2 -18.1 -18.7 -17.7 -13.7 -5.7 -0.0 (`Relung_Panen Phase_3 L18`) | -18.0 | 10 | 10,668 | measured AWS anchor (White Smoke Lake, Jan 1992-Jul 1993); the monthly curve is CONSTRUCTED, not measured (DS Relung_Panen Phase_3 L17-L18) |
| Shirayuki | ~69°24'S, 76°11'E (`Spec Shirayuki L5`) | -9.9 | +0.2 -2.9 -8.3 -13.1 -15.2 -14.6 -16.1 -16.1 -15.4 -12.0 -4.8 -0.5 (`READER/Shirayuki.md L27`) | -15.6 | 11 | 10,196 | PROXY: Zhongshan READER |
| Sinheung | ~69°22'S, 76°22'E (`Spec Sinheung L3`) | -9.9 | +0.2 -2.9 -8.3 -13.1 -15.2 -14.6 -16.1 -16.1 -15.4 -12.0 -4.8 -0.5 (`READER/Sinheung.md L15`) | -15.6 | 11 | 10,196 | PROXY: Zhongshan READER |
| Zhongshan | ~69°22'S, 76°22'E (`Spec Zhongshan L3`) | -9.9 | +0.2 -2.9 -8.3 -13.1 -15.2 -14.6 -16.1 -16.1 -15.4 -12.0 -4.8 -0.5 (`READER/Zhongshan.md L14`) | -15.6 | 11 | 10,196 | Zhongshan READER |
| Contrapunto | ~62°13'S, 58°47'W (`Contrapunto Step_-1 L18`) | -1.7 | +1.9 +1.7 +0.8 -1.2 -2.7 -4.9 -5.5 -5.3 -3.9 -2.1 -0.4 +0.8 (`Contrapunto Phase_3 L17`) | -5.2 | 8 | 7,210 | King Sejong READER |
| Esperanza | ~63°24'S, 56°59'W (`Esperanza Step_-1 L16`) | -4.5 | +1.5 +0.9 -2.0 -5.4 -7.5 -10.3 -10.9 -9.6 -6.9 -4.1 -1.0 +0.8 (`Esperanza Phase_3 L17`) | -10.3 | 9 | 8,239 | - |
| Marambio | ~64°14'S, 56°37'W (`Marambio Step_-1 L16`) | -8.0 | -0.8 -1.7 -5.5 -9.9 -12.0 -14.8 -14.9 -13.8 -10.6 -7.4 -3.4 -1.3 (`Marambio Phase_3 L17`) | -14.5 | 12 | 9,505 | - |
| Palmer City | 64°46'S, 64°03'W (`Palmer_City Step_-1 L16`) | -1.7 | +2.2 +1.9 +1.0 -0.8 -2.1 -4.1 -5.3 -5.9 -4.9 -2.6 -0.5 +1.1 (`Palmer_City Phase_3 L17`) | -5.1 | 8 | 7,185 | - |
| Pergamino | ~62°39'S, 60°23'W (`Pergamino Step_-1 L18`) | -1.7 | +1.9 +1.7 +0.8 -1.2 -2.7 -4.9 -5.5 -5.3 -3.9 -2.1 -0.4 +0.8 (`Pergamino Phase_3 L18`) | -5.2 | 8 | 7,210 | PROXY: King Sejong ~95 km; the Juan Carlos I station's own annual mean is -1.2 (DS Pergamino Step_1_and_2 L15) |
| Puerto Abrigo | ~64°49'S, 63°29'W (`Puerto_Abrigo Step_-1 L17`) | -1.7 | +2.2 +1.9 +1.0 -0.8 -2.1 -4.1 -5.3 -5.9 -4.9 -2.6 -0.5 +1.1 (`Puerto_Abrigo Phase_3 L18`) | -5.1 | 8 | 7,185 | PROXY: Palmer READER ~27 km |
| Rothera | ~67°34'S, 68°07'W (`Rothera Step_-1 L16`) | -4.0 | +1.3 +0.7 -0.9 -2.7 -4.3 -7.8 -9.8 -9.7 -8.1 -5.0 -2.3 +0.2 (`Rothera Phase_3 L17`) | -9.1 | 9 | 8,052 | - |
| Signy | ~60°43'S, 45°36'W (`Signy Step_-1 L17`) | -3.8 | +1.7 +1.4 -0.4 -1.8 -6.5 -9.8 -12.5 -7.9 -5.6 -3.9 -1.0 +0.9 (`Signy Phase_3 L17`) | -10.1 | 9 | 7,963 | - |

**Working (DERIVED).** *Mean winter* = (Jun + Jul + Aug monthly means) / 3. *Months below 0* = count of months whose mean is below 0 C. *HDD18* = heating degree-days to a base of 18 C, computed from monthly means as the sum over months of (days in month x (18 minus the monthly mean)); every monthly mean here is below 18 C, so every month counts, and the formula is 365 x 18 minus the sum of (days x monthly mean). Month lengths 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31. **Worked example, Janbogo (`DS Janbogo Phase_3 L18`):** 365 x 18 = 6,570; sum of days x monthly mean = 31(-1.2) + 28(-6.4) + 31(-14.1) + 30(-19.0) + 31(-20.0) + 30(-20.0) + 31(-21.8) + 31(-21.4) + 30(-19.8) + 31(-15.0) + 30(-7.3) + 31(-1.5) = -5,107.2; HDD18 = 6,570 + 5,107.2 = 11,677 (the table says 11,677). **Limits:** the base of 18 C is my choice, not a file's; degree-days from monthly means ignore the spread within a month; the result is not a heating load. **A degree-day figure stated by a file exists only for Relung Panen** (SOURCED, `DS Relung_Panen Phase_3 L17`, the AWS at White Smoke Lake, Jan 1992 to Jul 1993): 'winter freezing degree-days 3,987 C-days' and 'summer degree-days above freezing 71 C-days' (base 0 C, not comparable to HDD18). Its monthly curve is constructed, not measured (`DS Relung_Panen Phase_3 L18`).

**Other sourced extremes the datasheets give:** Amundsen Station coldest months 'avg -60 C', warmest 'avg -28 C' (`DS Amundsen_Station Step_1_and_2 L21`); Concordia record low 'record -84.7 C' (`DoI13` L179); Ariun Nuur and Dome Fuji, Kunlun coldest-month means are in the monthly cells above. Spec records of extremes for coastal cities are in each Step_1_and_2 datasheet and are not repeated.

### 1D. Geothermal status and power source

**SOURCED, `GEO` L11 to L24 (developer ruling 2026-09-05, quoted at `GEO` L7 to L9):** six cities are heated geothermally, as three pairs sharing one source each: **Pergamino + Contrapunto (Deception Island), Scott + Fort McMurdo (Mount Erebus), Janbogo + Zukelli (Mount Melbourne).** `GEO` L38: 'the other 31 cities have NO geothermal heat' (the count predates Relung Panen). **Flag in the same file (2026-11-02, `GEO` L203 to L215, unresolved):** canon says Concordia has its own 'geothermal and nuclear generation' and 'deep drilling' plateau heat (quoted at `GEO` L208 to L211); the file lists options A, B, C and ruled none. **Power:** `PWR` L33: 'What canon does NOT establish: any other generating plant, any reactor outside Concordia and the Tower complex, how the grid was laid out (which cities fed which), or where the grid's generation sat before the Tower fell.'

| City | Geothermal heat (GEO) | Local generation or canon power source (PWR, GEO, DoI13) |
|---|---|---|
| Amundsen Station | No (GEO L38: only the six; Concordia flagged separately) | Amundsen Tower complex: generation 'plausibly an advanced nuclear or fusion reactor array, supplemented by geothermal taps into subglacial volcanic activity... a design inference, not a ruling'; destroyed in the war (PWR L28). The Tower draws about 324 GW net, continuously (PWR L17). |
| Byrd | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Belgrano | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Halley | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Lazar | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Neumayer | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Sanay | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Santa Luce | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Troll | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Utstein | No (GEO L38: only the six; Concordia flagged separately) | Real-station basis only: the real station is described as 'the first zero-emission Antarctic station, running entirely on wind and solar' (DoI13 L163). That is a real-station fact quoted in the food file, not a ruled city power source. |
| Cape Adare | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Concordia | FLAGGED, not resolved: GEO L205 to L215 (Concordia has deep-drilled plateau geothermal heat per canon; not one of the six). | Power Core (Aries district): 'Geothermal and nuclear generation... Massive geothermal pipes and reactor cores'; damaged in the war, 'failing, not absent' (PWR L27). Canon wording at LOGI L113 to L114. Staple-growing power demand about 234 MW continuous, a demand figure, not plant output (PWR L27; DoI13 L273 to L278). |
| Denison | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Dumont d'Urville | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Fort McMurdo | YES, Mount Erebus, paired with Scott (GEO L23). | Same open question (PWR L30). |
| Janbogo | YES, Mount Melbourne, paired with Zukelli (GEO L24); heat plus the Janbogo port (GEO L67 to L82). | Heat is geothermal; 'whether it is also power: open' (PWR L29; GEO L134 to L169, options A, B, C). |
| Scott | YES, Mount Erebus, paired with Fort McMurdo (GEO L23). | Same open question (PWR L30). |
| Zukelli | YES, Mount Melbourne, paired with Janbogo (GEO L24). Destroyed (Spec Zukelli L4). | Same as Janbogo (PWR L29). |
| Dome Fuji | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Mawson | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Temirötkel | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Ariun Nuur | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Casey | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Davis | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Kunlun | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Mirny | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Relung Panen | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Shirayuki | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Sinheung | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Zhongshan | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Contrapunto | YES, Deception Island, paired with Pergamino (GEO L22). Destroyed (PWR L31). | Same open question (PWR L31). |
| Esperanza | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Marambio | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Palmer City | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Pergamino | YES, Deception Island, paired with Contrapunto (GEO L22). Destroyed in the war (PWR L31). | Same open question (PWR L31). |
| Puerto Abrigo | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Rothera | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |
| Signy | No (GEO L38: only the six; Concordia flagged separately) | None established (PWR L33). Tepenia 'heats with electricity' from the national grid, the Norway analogy (PWR L19; DoI08 L336 to L341). |

*National grid facts (SOURCED, `PWR` L11 to L19):* the Tower was the grid's regulation flywheel; at the Midpoint (about 2688) 'the nation's entire energy grid and orbital material economy came fully online'; the grid is chronically unstable from the Tower's fall to the present; national electricity about 101.7 GW; 'Tepenia is a cold country that heats with electricity' except the volcanic exceptions. Cluster geography (straight-line, ANALYSIS NOT CANON, `PWR` L49 to L61) groups cities within about 500 km of one another: Ross Sea (Janbogo, Zukelli, Scott, Fort McMurdo, Cape Adare); Davis plus the three Larsemann cities (110 km); Casey, Mirny, Relung Panen; the Peninsula (six within 385 km, Rothera 739 km); Neumayer, Sanay, Troll (widest pair 411 km); Denison plus Dumont d'Urville (122 km); alone: Concordia, Amundsen Station, Byrd, Kunlun, Dome Fuji, Temirötkel, Mawson, Signy.

---

## 2. Food, as the files state it, per city

**What the files assume nationally (SOURCED).** Growing under the caloric model is 'INDOOR STACKED HYDROPONICS' needing 'power, a structural footprint (~5.2 km2 per average city at 6 layers), and a foundation', not 'soil, sunlight, or mild weather' (`DoI13` L153 to L156); 'no Tepenian crop uses daylight' (`DoI13` L637 heading); 'stacked or spread' is named an open canon decision (`DoI08` L331 to L333). Livestock is a multi-species tier fed from crop residue (`DoI12` L1 to L60 (section 1 on livestock)). The terraformed coastal belt is ruled 1,500 km2 and split by region: Antarctic Peninsula plus islands about 700 km2 (Palmer subnet cities), East Antarctic coastal oases about 400 km2 (Davis, the Tri-Cities, Lazar), Bunger Hills about 400 km2 (Relung Panen, Mirny, Casey) (`DoI12` L224 to L259). The belt's active layer is 'circulated municipal waste heat under the field' (`DoI12` L113). The fishery is at its ecological cap (`DoI13` L28, L205, L235; `DoI19` L14). **Geological food status** (`DoI13` L863 to L865): importers 'only those geologically forced': Halley and Neumayer (floating shelf), Vostok (Ariun Nuur), Byrd and Amundsen Station (ice sheet), Kunlun and Dome Fuji (ice sheet, zero humans); Belgrano was added as an ice-shelf importer afterward (`DoI13` L778 to L800); 'Concordia is treated as a grower, because canon says it is' (`DoI13` L865). **File 16 vintage:** its per-city sections were written 2026-09-02, with later refreshes noted at each (`DoI16` L1; `DoI19`).

In file 16, 'GROWER' means the city's baseline carries the full food term (100 percent); 'forced importer' means the food term is 10 percent. Sector shares are shares of the distinctive tier (`DoI16` and `Division_of_Industry_Reliability_Quick_Reference.md` L34 to L46).

| City | Food role as the files state it | Cite |
|---|---|---|
| Amundsen Station | ICE-SHEET forced importer, 'food term at 10%'; 'Not a city. A strategic infrastructure installation'. No growing area stated. | DoI16 L3453, L3458 |
| Byrd | ICE-SHEET FORCED IMPORTER, 'bedrock 2,164 m down, food term at 10%'. Canon sector 'Import/export & dispatch 25%'. | DoI16 L3355, L3360, L3368 |
| Belgrano | Forced importer (ice shelf), 'food term at 10%'; baseline 44.3 to 34.0 percent after the correction. | DoI16 L553, L567; DoI13 L778 to L800 |
| Halley | Forced importer, 'food term at 10%'; marine sector 'indirect, no own docks'. | DoI16 L604, L608 |
| Lazar | GROWER. Ruled to build 'UPWARD, OUTWARD ONTO THE ICE, and DOWNWARD'; downward is 'the RIGHT ONE FOR FARMS' (thermally cheap). 100 to 180 freshwater lakes: 'the only city in the country that does not pay the melt tax'. Footprint at 6 layers 16.2 km2 against the 34 km2 oasis. | DoI13 L441 to L452, L540, L551; DoI16 L200 to L203 |
| Neumayer | Forced importer, 'food term at 10%'; scientific research (the EDEN ISS line) is the ruled floor, 'derived from Neumayer's food-import debt'. | DoI16 L485, L496 |
| Sanay | GROWER, bedrock nunatak. Defining industry is the port and shipyard chain; 'import-chain work' is 65 percent of its sector list. | DoI16 L711, L716, L737 |
| Santa Luce | GROWER, bedrock nunatak; 'the smallest food burden of the five' original growers; held at current value, flagged for end-of-pass review. | DoI16 L659; DoI13 L166 |
| Troll | GROWER, bedrock nunatak; imports land at Sanay or Belgrano from Africa, are 'trucked here on Hwy 7'. | DoI16 L765, L788 |
| Utstein | GROWER, bedrock nunatak; real station is wind and solar; canon says the city's 'entire existence depended on continuously maintained engineering'; destroyed. | DoI16 L842; DoI13 L163 to L175 |
| Cape Adare | GROWER, rock-founded cape. Marine/resource extraction 25 percent is 'port/harbor ops + the guano phosphate'; it 'CANNOT be a fishery'. | DoI16 L2666, L2677, L2683 |
| Concordia | Grows food: 'the Frostlands (Sagittarius) is Concordia's primary internal food source'; 'heated livestock barns without which no animals survive'; 'hydroponics' among live services; feed is 'dried and preserved feed brought in from outside the district'. Power for staples alone about 234 MW continuous (94 MW if greenhouse). The city's own food-industry determination is deferred by the developer. | DoI13 L254 to L266, L273 to L278; Spec Concordia L239, L254; DoI16 L2511 |
| Denison | Baseline food term 100 percent, D = 2.00. Two readings in file 13: no room, ice-free rock 0.63 km2 (section 6, superseded) and reclassified rock-founded (sections 14 and 15). | DoI16 L2584; DoI13 L185 to L186, L839 |
| Dumont d'Urville | GROWER, Petrel Island. Marine 25 percent of the distinctive tier, about one third food (counted in the national supply tally). | DoI16 L2436, L2440, L2447 |
| Fort McMurdo | GROWER, Ross Island; marine sector is Dry Valleys extraction plus the McMurdo Sound crossing. | DoI16 L2917, L2929 |
| Janbogo | GROWER, Terra Nova Bay. Half of the marine sector (10 percent of the distinctive tier) is 'the year-round polynya fishery'; 'year-round polynya fishing is winter food when nowhere else in Tepenia can put boats out'. | DoI16 L2835, L2848, L2875 |
| Scott | GROWER, Ross Island, 'food term 100%'. | DoI16 L3023 |
| Zukelli | GROWER, Terra Nova Bay; half of marine 20 percent is 'Zukelli's share of the shared polynya port infrastructure'. | DoI16 L2748, L2759 |
| Dome Fuji | Zero humans: 'the food question is moot'. Baseline D = 2.50 ICE-SHEET. | DoI16 L3190 |
| Mawson | GROWER, Holme Bay coast, rock-founded; half of maritime trade is 'Sinheung's import channel'. | DoI16 L3267, L3279, L3289 |
| Temirötkel | GROWER, rock-founded (East Ongul Island). | DoI16 L3100 |
| Ariun Nuur | ICE-SHEET FORCED IMPORTER, 'bedrock ~4 km down under Lake Vostok, food term at 10%'. | DoI16 L2353 |
| Casey | GROWER, Wilkes Land coast; maritime 15 percent; in the Bunger Hills belt allocation. | DoI16 L2185, L2190; DoI12 L259 |
| Davis | GROWER. Agricultural/food production about 35 percent of the distinctive tier, mandated in full: 'FOOD, agriculture 35%, the breadbasket, explicitly national'. In the East Antarctic oasis belt allocation. Vestfold Hills about 400 km2 ice-free. | DoI16 L2010, L2015, L2022; DoI12 L258 |
| Kunlun | Zero humans (D = 2.70); 'the human-keyed term is zero'. | DoI16 L2260 |
| Mirny | GROWER, 'four rock outcrops at Mabus Point, food term 100%'; in the Bunger Hills belt allocation. | DoI16 L2114; DoI12 L259 |
| Relung Panen | Food production 25 percent of the distinctive tier (`DR-71`); agricultural research 4, seed breeding 3, phosphorus and soil recovery 6 percent (`DR-75`); baseline 44.0 percent at D = 1.43; Bunger Hills belt allocation about 400 km2; 'cold-chain logistics is not included and is explicitly pending'; no §5 port assigned. Its food role is ruled 'Strong'. | DS Relung_Panen Phase_7 L18 to L21; DoI19 L13; DoI12 L259; Census L514; PORTS L245 |
| Shirayuki | GROWER, Larsemann Hills, rock-founded. | DoI16 L1758 |
| Sinheung | GROWER, Larsemann Hills; fabrication 45 percent of the distinctive tier. | DoI16 L1838, L1843 |
| Zhongshan | GROWER, Larsemann Hills ice-free oasis; marine 15 percent 'Prydz Bay FISHING and related industries'. | DoI16 L1921, L1926, L1953 |
| Contrapunto | GROWER, rock-founded island, 'food term 100%'; marine 15 percent; in the Peninsula belt allocation. | DoI16 L1030, L1035; DoI12 L257 |
| Esperanza | GROWER, mainland Peninsula. Agricultural/food production 15 percent, mandated in full. Hope Bay is about 15 km2, and growing area at 6 layers would take 'about 80% of the entire bay' (pre-relocation figures); the city was shrunk to 1,200,000 in `DR-90`, workforce 894,835, agriculture workers 80,960 under `DoI19`. A small real greenhouse whose vegetables are 'prized and often reserved for special occasions'. | DoI16 L1336, L1351; DoI13 L588 to L589, L592, L597; DoI19 L12; Census L495 |
| Marambio | GROWER, Seymour Island, rock-founded; the port carries the country's most load-bearing import (bulk cargo). | DoI16 L1462, L1484 |
| Palmer City | GROWER, Anvers Island; ruled on a self-declared non-canon sector list. | DoI16 L1526 |
| Pergamino | GROWER, rock-founded island. Maritime/fishing 30 percent of the distinctive tier, 'national food provider', 'leveraging Livingston Island's coastal access'. | DoI16 L1094, L1098, L1105 |
| Puerto Abrigo | GROWER, 'food term 100%' (a 929-person city). | DoI16 L1616 |
| Rothera | GROWER, Adelaide Island, rock-founded; marine/resource extraction feeds the fabrication chain. | DoI16 L1677, L1691 |
| Signy | GROWER, plus a national fish provider: Marine/fishing 30 percent of the distinctive tier. 'Signy cannot eat its way out of needing farms'. | DoI16 L944, L955, L972 to L973 |

**Indoor farming, aquaculture and growing-area figures the files hold.** Growing area: Lazar 97.2 km2 of growing area, 16.2 km2 footprint at 6 layers, 8.1 km2 at 12 (`DoI13` L425, pre-2026-10-28 population); Esperanza 72.2 km2 growing area, 12.0 km2 at 6 layers (`DoI13` L588 to L589, pre-relocation); the national growing footprint is about 5.2 km2 per average city at 6 layers (`DoI13` L154). **Aquaculture:** NOT IN FILES as a city role in these files; only wild-capture fishery appears (marine capture at its ecological cap, 13,000 fishers, `DoI13` L28; `DoI16` L2848, L955, L1105, L1953). **Food workers per city** are the baseline numbers in each `DoI16` section (for example Janbogo 406,082 baseline workers, `DoI16` L2835); they are the whole baseline tier (food plus the other baseline industries), not food alone, and are not repeated for all 38 here.

**Import dependence, in the files' words.** Forced importers (Halley, Neumayer, Belgrano, Ariun Nuur, Byrd, Amundsen Station; Kunlun and Dome Fuji have no humans) take food in; the import chain runs through Sanay, Belgrano and Mawson for the interior and Sinheung (`DoI16` L737, L788, L3289). Australia is stated as the source of 'excess food' inbound to Tepenia (`PORTS` L220, quoting the novel repo's survey).

---

## 3. Mentions of waste heat, cogeneration, district heating, a nearby reactor or plant

Searched with `grep -i` for: waste heat, cogeneration, district heat, heat reuse, reject heat, combined heat, heat recovery, reactor, steam, in `Cities/Specs`, `Cities/Division_of_Industry`, `Cities/City_Master_Reference`, `Cities/City_Relationship_Database.md`, `Infrastructure/`, the census, `City_Logistics.md`, and the datasheets. `Local_Cultures`, `Local_Robot_Culture`, `City_Megasheets` and `graphify-out/` were not read.

1. **Byrd: waste heat is canon.** `Spec Byrd L7 to L13` (CGRM 2026-09-02, Path 6, developer ruling): 'Byrd's underground complex of machinery and factories produces enormous waste heat. That heat is piped, essentially by conduction, to a network of radiators sitting ABOVE the city but IMMEDIATELY BELOW the surface'; 'A large industrial complex built INSIDE an ice sheet cannot dump its waste heat locally, doing so melts the structure it lives in'; the radiator field 'keeps the airplane lanes free of accumulating snow... as a BYPRODUCT'. Repeated at `DoI16 L3396 to L3404` (the aviation sector is justified by this coupling). A research log on it exists (`Cities/Research_Logs/Byrd_S3_Waste_Heat_Runway_and_Aviation_2026-11-01.md`; research, not canon, not read for this unit).
2. **National terraforming: waste heat is the active layer.** `DoI12 L112 to L116`: PASSIVE layer survives a grid collapse; ACTIVE 'circulated municipal waste heat under the field... closes the remainder... NO' survival; 'The active layer is the city's waste heat, and it dies when the city's power dies.' Applies to the terraformed coastal belt, not to a named plant.
3. **Concordia: ice melting uses power-system waste heat.** `LOGI L102`: 'Ice melting: Primary source. Surface ice and snow collected and melted using waste heat from power systems (particularly geothermal).' `LOGI L113 to L114`: geothermal pipes and reactor cores in the Aries Power Core; nuclear 'present in the power core system'. `LOGI L191`: 'Heating: Primarily geothermal, supplemented by Cancer (TBN) heating plants.'
4. **Geothermal district loops (six cities).** `GEO L47 to L51`: open-loop wells, re-injection, 'Heat pumps and exchangers circulate water between buildings through a shared district loop. The heat is municipal and shared by construction.' `GEO L55 to L63`: snow-melt pavement from the loop; bare ground. `GEO L101`: heat 'comes out of the ground under the city'.
5. **Plant sites and reactors in canon.** `PWR L27 to L33`: reactors only at the Concordia Power Core and (inferred, not ruled) the Tower complex; every other plant 'open'. `PWR L41`: treaty gloss in tension with Concordia's reactors. `PWR L45`: key facts from the nuclear logistics research, including 'the longest clearly sourced nuclear district-heat pipe is 23 km' (a research figure, not canon). `PWR L63`: 1 GW is about 10 floating RITM-200S-class units, or 16 Lomonosov-size barges, or about 200 five-megawatt microreactors (DERIVED in the research file). `PWR L69 to L76`: open questions (is nuclear allowed; where spent fuel goes; other plants before the war; plants per cluster).
6. **District heating as a national fact.** `DoI08 L335 to L341`: 'in Norway most homes are heated through electricity instead of district heating (only ~2% district heating, vs Sweden's 60%)'; 'Norway is Tepenia's analog, not Iceland. A cold country that heats with electricity'. `PWR L19` repeats it.
7. **Research cue in a datasheet, not canon.** `DS Davis Phase_3 L15` lists 'the Trans-Alaska obligation: manage your own waste heat forever or destroy your foundation' among the real-world research cues for Davis. `DS Signy Step_3 L20` lists Vestmannaeyjar, Iceland, a real town whose district heating comes from geothermal heat, as an inspiration pick for Signy.
8. **Not found in canon:** any statement that a Tepenian city uses plant heat for housing or farms other than Byrd's radiators, Concordia's melt water, the six geothermal loops and the national belt layer; any named plant site other than Concordia's Power Core, the Tower complex and the six geothermal fields; any cogeneration statement; any pipe, heat network or heat-sharing between non-geothermal cities. (NOT IN FILES for the files named above.)

---

## 4. Facts a screen would need that the files do not hold (input list for a later web-research step)

Items are phrased as missing inputs, not as a recommendation.

**Plants and heat sources**
1. Sites, types (fission, fusion), sizes (MWe, MWth) and numbers of any plant other than Concordia's Power Core and the Tower complex; whether plants sit near cities (`PWR` L33 states none are established). Whether geothermal heat is also power (`PWR` L29 to L31; `GEO` L134).
2. Output of the Concordia Power Core and the Tower complex in electricity and heat; how much heat they reject and where (not stated; only the 324 GW net Tower draw, `PWR` L17).
3. Condenser or reject-heat temperature of any canon plant (none stated).
4. Whether Byrd's waste-heat radiator field is sized in watts (the files give no power figure, `Spec Byrd L7 to L13`).

**Climate and ice**
5. Heating degree-days from observed data (the files hold only Relung Panen's freezing degree-days; every other figure here is DERIVED from monthly means).
6. Daily and hourly temperature extremes, wind speed, ice-fog and inversion data by city (partly held in the Step_1_and_2 datasheets as spec lines; not collected here).
7. Elevation for the 26 cities marked NOT IN FILES in table 1B (coastal, island, shelf and oasis cities; no file states a figure for the canon city).
8. Distance to the nearest open sea for the inland and plateau cities as a figure (Byrd, Amundsen Station, Utstein, Kunlun, Dome Fuji, Rothera), and for the oasis and shelf cities as measured distances.
9. Ice thickness and ice flow at ice-sheet and ice-shelf cities other than Amundsen Station (about 2,700 m, `DS Amundsen_Station Step_1_and_2 L40`) and Byrd (2,164 m to bedrock, `DoI13 L851`); basal condition (frozen or wet) for any city.
10. Seasonal melt, summer climate and sun-hours by city (partly in the datasheets; not collected).

**Cities and their loads**
11. A post-war population for every city (no Census III, `Census` L631).
12. Housing floor area, building stock and building envelope per city; building heat loss per m2 or per person; present heating energy per person (`DoI08 L336` quotes a real national per-capita figure for Norway, not for any Tepenian city).
13. Indoor-farm area actually built or planned per city; whether farms are stacked or spread (`DoI08 L333` calls this open); lamp heat as a share of farm heat (not in these files).
14. Aquaculture as a Tepenian industry (not in these files).
15. Livestock barn area and heat per city beyond Concordia's 'heated livestock barns' (`Spec Concordia L239`).
16. Where a heat pipe could run: terrain, permafrost or ice conditions, road and utilidor layout between a plant site and a city, per route (the PWR cluster table is straight-line only and 'roads are longer', `PWR` L49).
17. Water sources and melting loads per city (Lazar's lakes are held, `DoI13` L540; others not collected).

**Treaty and rules**
18. Whether reactors are allowed (`PWR` L69); the Falkland Treaty draft's Article V.1 bans nuclear explosives and disposal of radioactive waste but not reactors (`PWR` L40), and the scaffold's gloss disagrees (`PWR` L41).
19. The canon status of the 'only six geothermal cities' line against Concordia (`GEO` L203 to L215).

---

## FINAL

**What the files support (SOURCED).**
- All 38 census rows have a population (Census I live values, Census II where a row exists), a war status, and a site description; every city has a setting word from the relationship database, the spec, the ports file or the food file.
- Coordinates are held for all 38; temperatures (annual mean and 12 monthly means) are held for all 38, with proxies for Denison, Pergamino, Puerto Abrigo, Shirayuki and Sinheung, an old manned-years record for Byrd, a constructed monthly curve for Relung Panen, and non-READER sources for Sanay, Santa Luce, Utstein and Cape Adare.
- Six cities have geothermal heat (three pairs); Concordia has geothermal and nuclear generation and a flagged conflict with the 'only six' line; the Tower complex had a power plant (inferred, not ruled); no other generating plant is established.
- Every city's food status is stated (grower, forced importer, or zero humans), with a sector share where the file gives one. The six forced importers plus Kunlun and Dome Fuji (zero humans) are named.
- Waste heat is canon at Byrd (radiator field), at Concordia (melt water), in the six geothermal loops, and as the active layer of the national terraformed belt.

**What the files do not support.** Any plant site, plant size or reject-heat figure beyond Concordia and the Tower; any heating-degree-day or heating-load figure; elevations for 26 cities; distance-to-sea figures for several inland cities; a post-war population; any aquaculture role; any statement about heat reuse by a non-geothermal city other than Byrd and Concordia.

**NOT IN FILES list:** see section 4 (19 items).

**Cautions found while reading.**
- The census, the DoI file 13 section 6 and the geothermal file's 'other 31' count predate later rulings; they are quoted with their dates.
- `DoI16` was written 2026-09-02 on older populations; its shares are held, its worker counts were refreshed only where the file says so (Esperanza, `DoI16` L1340 area; Relung Panen, `DoI19` L13).
- The geothermal file's pair for Pergamino and Contrapunto sits on Deception Island; both cities are Destroyed (`PWR` L31). The census still carries them under old names Juan Carlos and Sejong.
- The Bunger Hills belt allocation (`DoI12` L259) names Relung Panen, Mirny and Casey; Casey is Destroyed (`Spec Casey L4`).

**Ended:** 2026-11-02, MST (stamped below).

---

## Read log (repo only; no web searches were run)

| # | Tool | Target | Result |
|--:|---|---|---|
| 1 | Read | `Power_Plant_Heat_Research_BRIEF_2026-11-02.md` (48 lines) | read in full |
| 2 | Read | `Fusion_and_Helium3_Research_BRIEF_2026-11-02.md` (63 lines), rules 1 to 8 | read in full |
| 3 | Read | `Official_Population_Census.md` L1 to L300 (Section A), L486 to L560 (Census I), L627 to L842 (Census II, overflow, losses) | read; city table L494 to L532 |
| 4 | Read | `Infrastructure/Geothermal_Heating.md` (217 lines), `Amundsen_Power_Supply.md` (81 lines) | read in full |
| 5 | Read | `City_Renames_Alias_Table_2026-10-03.md` L1 to L115 | read; old-to-new names |
| 6 | Bash (grep, sed) | `City_Development_Passes/*/*/Datasheets/*.md` for coordinates, climate, elevation | 73 files mention elevation or coordinates; Step_-1, Step_0, Step_1_and_2, Phase_3 hold the figures; Concordia, Shirayuki, Sinheung, Zhongshan have no Datasheets folder, so their climate comes from `READER/` files and their Specs |
| 7 | Bash (python, scratch) | parsed 12 monthly means from the datasheets and four READER files; computed JJA, months below 0, HDD18 | all 38 cities parsed |
| 8 | Bash (grep) | `City_Relationship_Database.md` Region and Altitude lines | 38 Region lines, 4 Altitude lines |
| 9 | Bash (grep) | `Cities/Specs/*/*.md` Status, Based-on, elevation lines | statuses for 38 specs (Spec files are canon, not culture files) |
| 10 | Read | `Division_of_Industry/13_*.md` L149 to L470, L534 to L636, L730 to L931 | read; geology tiers L845 to L847 |
| 11 | Bash (awk, grep) | `Division_of_Industry/16_*.md` per-city DETERMINED sections for food lines | 36 sections scanned for grower, importer, marine, agriculture lines |
| 12 | Bash (grep, sed) | `Division_of_Industry/08`, `12`, `19`; `Infrastructure/Ports.md` L185 to L250, L470 to L495 | read the cited lines |
| 13 | Bash (grep) | waste heat, cogeneration, district heat, reactor, steam across Cities, Infrastructure, Specs, DoI, datasheets, `City_Logistics.md` | hits listed in section 3; research-log hits not read |
| 14 | Read | `Universal_Location_Methodology/Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md` L1 to L60 | read; citation gate |
| 15 | Not done | web search | rule: none for this unit |

*End time stamp: 2026-11-02 21:17 MST (system clock).*
