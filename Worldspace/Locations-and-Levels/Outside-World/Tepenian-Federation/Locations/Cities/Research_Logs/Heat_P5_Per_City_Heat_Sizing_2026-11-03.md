# Per-city heat sizing for plant-heat reuse (2026-11-03)

**Status: DERIVED ARITHMETIC ON REPO AND RESEARCH FIGURES. Nothing here is ruled or canon.** Built without web search from the city table in `Heat_P4_City_Screen_For_Plant_Heat_Reuse_2026-11-02.md` (populations, settings, winter means, geothermal flags) and the housing-heat range in `Heat_P3_Agriculture_Aquaculture_and_Housing_Heat_Research_2026-11-02.md`. It sizes only **housing and community heat**; it does not size farms, aquaculture, industry or the Tower. It does not rank cities and does not choose plant sites.

## Assumptions (change any and the table changes with it)
1. **Heat demand per person: 0.5 to 1.5 kW average** (P3, UNVERIFIED outside Fairbanks and Sisimiut; Antarctic cities are colder than both, so the top of the range or above is likely). Demand = Census I population x that range. **Census I is used because the direction chosen for the initial stages (fission first, `Tepenia_Nuclear_History_Proposal_2026-11-02.md` §9) predates the war**; Census II is shown for comparison.
2. **One plant of about 1 GWe (a large light-water unit) rejects about 2 GWth** (efficiency about one-third; the R6 file's large-reactor reference is 3,000 MWt for about 1 GWe). "Plants to cover it" is the demand divided by 2 GWth, rounded up, at least 1. It ignores the electricity penalty of heat extraction (0.12 to 0.2 MWe per MWth, P2), peak-day demand, spares and losses in the pipes (4 percent over 34 km at Mělník-Prague, P2).
3. **The plant must sit within the sourced reach of a hot-water line** (26 to 75 km on real lines, P2). No plant site is in the files, so distance is NOT checked here.
4. **Canon today: Tepenia "heats with electricity" from the national grid** (the Norway analogy, `Division_of_Industry/08` L335 to L341, via the P4 file). Cogeneration would change that; nothing in canon says it exists.
5. **Residents include robots, and this table gives every resident the same heat demand.** Whether robots need housing heat is not settled in the files read here. In the cities checked (Casey, Halley, Neumayer in `09_Per_City_Baseline_Run.md`) humans are 49 to 50 percent of residents, so **a humans-only demand would be about half of every figure below.** The figures below are therefore an upper bound on that point.
6. **Six geothermal cities already have heat that does not depend on a plant** (`Geothermal_Heating.md`): marked "yes" in the last column. Concordia's geothermal status is flagged as unresolved in that file.

## Setting classes (from the P4 city table; not rankings)
- **A · interior ice sheet:** Amundsen Station, Byrd, Concordia, Dome Fuji, Ariun Nuur, Kunlun. Landlocked; heat dump to the ice is workable only at about 1 GWth or less (`Heat_P1_…`).
- **B · floating ice shelf:** Belgrano, Halley, Neumayer. Heat could melt the shelf the city stands on (not researched).
- **C · inland rock (no sea):** Lazar, Sanay, Santa Luce, Troll, Utstein. Bedrock foundation; 80 to 235 km from the sea.
- **D · shelf-sealed oasis:** Relung Panen. Rock oasis, 64 to 145 km of shelf between it and open sea.
- **E · coastal or island rock:** the other 23 cities. The sea is available as a summer heat sink (environmental effect not researched).

## Table (sorted by class, then by Census I population)
| City | Class | Census I | Census II | Heat demand, GWth (0.5 to 1.5 kW each) | Plants (1 GWe, 2 GWth reject) | Winter mean JJA (C) | HDD18 | Geothermal heat |
|---|---|--:|--:|--:|--:|--:|--:|---|
| Concordia | A · interior ice sheet | 1,068,065 | 671,180 | 0.53 to 1.60 | 1 to 1 | -63.5 | 25,826 | FLAG |
| Ariun Nuur | A · interior ice sheet | 441,378 | NOT IN FILES | 0.22 to 0.66 | 1 to 1 | -66.1 | 26,575 | no |
| Byrd | A · interior ice sheet | 429,009 | NOT IN FILES | 0.21 to 0.64 | 1 to 1 | -35.8 | 16,859 | no |
| Kunlun | A · interior ice sheet | 148,497 | NOT IN FILES | 0.07 to 0.22 | 1 to 1 | -63.8 | 26,278 | no |
| Dome Fuji | A · interior ice sheet | 80,120 | NOT IN FILES | 0.04 to 0.12 | 1 to 1 | -65.1 | 25,832 | no |
| Amundsen Station | A · interior ice sheet | 6,857 | 4,891 | 0.00 to 0.01 | 1 to 1 | -59.3 | 24,517 | no |
| Halley | B · floating ice shelf | 1,504,467 | 1,123,950 | 0.75 to 2.26 | 1 to 2 | -28.5 | 13,586 | no |
| Neumayer | B · floating ice shelf | 1,304,201 | 866,628 | 0.65 to 1.96 | 1 to 1 | -24.2 | 12,424 | no |
| Belgrano | B · floating ice shelf | 1,124,011 | 873,648 | 0.56 to 1.69 | 1 to 1 | -20.2 | 11,390 | no |
| Lazar | C · inland rock (no sea) | 2,410,409 | 1,659,460 | 1.21 to 3.62 | 1 to 2 | -16.2 | 10,251 | no |
| Utstein | C · inland rock (no sea) | 1,190,038 | 802,643 | 0.60 to 1.79 | 1 to 1 | -23.7 | 13,128 | no |
| Troll | C · inland rock (no sea) | 1,006,570 | 707,711 | 0.50 to 1.51 | 1 to 1 | -24.4 | 12,853 | no |
| Sanay | C · inland rock (no sea) | 515,789 | 310,996 | 0.26 to 0.77 | 1 to 1 | -22.5 | 12,484 | no |
| Santa Luce | C · inland rock (no sea) | 465,818 | 278,855 | 0.23 to 0.70 | 1 to 1 | -20.9 | 12,059 | no |
| Relung Panen | D · shelf-sealed oasis | 1,000,071 | 714,045 | 0.50 to 1.50 | 1 to 1 | -18.0 | 10,668 | no |
| Cape Adare | E · coastal or island rock | 1,551,776 | 1,085,931 | 0.78 to 2.33 | 1 to 2 | -18.8 | 10,738 | no |
| Casey | E · coastal or island rock | 1,547,850 | 1,077,910 | 0.77 to 2.32 | 1 to 2 | -14.7 | 9,986 | no |
| Mawson | E · coastal or island rock | 1,498,852 | 988,325 | 0.75 to 2.25 | 1 to 2 | -17.4 | 10,661 | no |
| Mirny | E · coastal or island rock | 1,403,549 | 1,052,374 | 0.70 to 2.11 | 1 to 2 | -16.0 | 10,666 | no |
| Janbogo | E · coastal or island rock | 1,362,629 | 993,450 | 0.68 to 2.04 | 1 to 2 | -21.1 | 11,677 | yes |
| Zukelli | E · coastal or island rock | 1,310,769 | 973,539 | 0.66 to 1.97 | 1 to 1 | -21.1 | 11,683 | yes |
| Davis | E · coastal or island rock | 1,210,432 | 817,475 | 0.61 to 1.82 | 1 to 1 | -16.6 | 10,247 | no |
| Zhongshan | E · coastal or island rock | 1,203,607 | 932,895 | 0.60 to 1.81 | 1 to 1 | -15.6 | 10,196 | no |
| Esperanza | E · coastal or island rock | 1,200,000 | 753,159 | 0.60 to 1.80 | 1 to 1 | -10.3 | 8,239 | no |
| Shirayuki | E · coastal or island rock | 1,112,600 | 691,371 | 0.56 to 1.67 | 1 to 1 | -15.6 | 10,196 | no |
| Sinheung | E · coastal or island rock | 1,014,533 | 835,341 | 0.51 to 1.52 | 1 to 1 | -15.6 | 10,196 | no |
| Denison | E · coastal or island rock | 958,340 | 659,355 | 0.48 to 1.44 | 1 to 1 | -16.7 | 10,581 | no |
| Contrapunto | E · coastal or island rock | 644,833 | 514,070 | 0.32 to 0.97 | 1 to 1 | -5.2 | 7,210 | yes |
| Marambio | E · coastal or island rock | 570,269 | 430,145 | 0.29 to 0.86 | 1 to 1 | -14.5 | 9,505 | no |
| Fort McMurdo | E · coastal or island rock | 445,310 | 338,169 | 0.22 to 0.67 | 1 to 1 | -24.3 | 12,510 | yes |
| Dumont d'Urville | E · coastal or island rock | 408,001 | 280,805 | 0.20 to 0.61 | 1 to 1 | -16.7 | 10,581 | no |
| Pergamino | E · coastal or island rock | 386,692 | 246,372 | 0.19 to 0.58 | 1 to 1 | -5.2 | 7,210 | yes |
| Scott | E · coastal or island rock | 386,011 | 313,634 | 0.19 to 0.58 | 1 to 1 | -28.1 | 13,720 | yes |
| Palmer City | E · coastal or island rock | 332,808 | 332,170 | 0.17 to 0.50 | 1 to 1 | -5.1 | 7,185 | no |
| Rothera | E · coastal or island rock | 317,449 | 255,857 | 0.16 to 0.48 | 1 to 1 | -9.1 | 8,052 | no |
| Temirötkel | E · coastal or island rock | 225,376 | 164,957 | 0.11 to 0.34 | 1 to 1 | -17.2 | 10,398 | no |
| Signy | E · coastal or island rock | 188,694 | 133,755 | 0.09 to 0.28 | 1 to 1 | -10.1 | 7,963 | no |
| Puerto Abrigo | E · coastal or island rock | 929 | 691 | 0.00 to 0.00 | 1 to 1 | -5.1 | 7,185 | no |

## Totals by class (Census I basis, DERIVED)
| Class | Cities | Census I people | Heat demand, GWth |
|---|--:|--:|--:|
| A · interior ice sheet | 6 | 2,173,926 | 1.1 to 3.3 |
| B · floating ice shelf | 3 | 3,932,679 | 2.0 to 5.9 |
| C · inland rock (no sea) | 5 | 5,588,624 | 2.8 to 8.4 |
| D · shelf-sealed oasis | 1 | 1,000,071 | 0.5 to 1.5 |
| E · coastal or island rock | 23 | 19,281,309 | 9.6 to 28.9 |
| **All 38** | 38 | 31,976,609 | 16.0 to 48.0 |

## What the arithmetic shows (DERIVED; read the assumptions above first)
- **National housing heat is a small fraction of the Tower's reject heat.** All 38 cities together need about 16 to 48 GWth, against about 600 GWth of reject heat from the Tower's 324 GW (`Heat_P1_…`) and about 190 GWth from the national grid's 101.7 GW. City heat reuse can soak up a meaningful share of the national grid's reject heat but not the Tower's.
- **The cities are the right size for plant-by-plant cogeneration:** the biggest ones need a few GWth, which is the reject heat of one to a few 1 GWe plants.
- **The class split matters more than the totals:** the heat-sink question (class A to D) is where the sources run out, not the demand.
- **Not sized here:** farms and aquaculture, which P3 says would draw on the same heat (lit farms are heat sources and need none); industry; the Tower; summer sinks.

## What this table cannot say
Plant sites (none in the files except Concordia's Power Core and the Tower complex), distance from plant to city, the electricity penalty, summer demand, peak demand, and whether canon permits cogeneration at all.
