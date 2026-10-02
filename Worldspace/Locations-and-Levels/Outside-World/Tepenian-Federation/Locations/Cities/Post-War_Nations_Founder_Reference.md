# Post-War Nations — Founder Reference

**Derived 2026-10-01** from the developer's map files (`/home/kuroskalacs/Documents/Doll-Fi/media/y-files/Map Files/`),
latest iteration per region. **Purpose:** pick realistic founding nations for Tepenian cities by time-zone proximity
(`DEVELOPER_RULINGS_LOG.md` `DR-19`, `DR-22`). **This is a working summary, not canon.** The maps are "solid, though
still malleable, in-progress" (developer), and **the map files are the authority**. Re-derive this file when they
change.

**Method:** solar time zone = round(longitude ÷ 15). Spans are estimates from each nation's assigned territory, except
East Asia, whose figures come from `polities.csv`.

## ⚠ Dating: which year each region's map shows

| Region | Folder used (under the map root) | Year depicted |
|---|---|---|
| North America | `North America/02 reorganization/07 follow-up - complete - with Hawaii` | none (Alleghenia stages "Undated, for now") |
| Latin America | `Latin America/02 reorganization/08 follow-up` (`nations.py`) | none |
| Europe | `Europe/02 reorganization/04 follow-up - final map INIT 2083` | **start of 2083**; later C-series "no years implied"; CIN founded ~2108–2118 (research estimate only) |
| Russia | `Russia/02 reorganization/09 follow-up` ("CURRENT AUTHORITATIVE STATE") | none (matches Europe INIT 2083) |
| Asia (East) | `Asia (East)/03 official timeline years` (maps A–F) | **F = 2267–present**; series covers 2083–2564. **The only region dated near 2564** |
| Asia (Southeast) | `Asia (Southeast)/02 reorganization/09 follow-up - usable-ready form` | "as of the 2083 war" |
| Asia (South-Central) | `Asia (South-Central)/02 reorganization/05 follow-up - official maps` | none |
| Asia (West) | `Asia (West)/02 reorganization/08 follow-up` (live nation data is in `worldbuilding/nations/middle-east-map-data/`) | none |
| Oceania | `Oceania/02 reorganization/04 follow-up - map-ready` | "post-2083 successor states" |
| Africa | unfinished. Developer: no African country founds a Tepenian city **except South Africa (Sanay; part of Signy)** | — |

**So outside East Asia, whether these borders still stand in 2564 is not established.**

## Nations by solar time zone

| UTC (solar) | Nations whose territory reaches this zone |
|---|---|
| −12…−10 | Hawaii (sovereign republic, −11…−10, NW chain to −12) · Samoa, American Samoa, Niue, Tonga, Wallis & Futuna (−12…−11) · Cook Is., French Polynesia, Pitcairn (−11…−8) · Kiribati (to −10) · New Zealand's Chathams/Tokelau (−11) · Künnarantaiga's Chukotka (−11) · Alaska's Aleutians (−11) |
| −9…−7 | Alaska (−11…−5) · Cascadia (−9…−7) · Colorado · Sonora (−8…−7) · Prairie Federation (−8…−5) · México (−7…−6) · Midwest Republic (−7…−6) · the CSA (−7…−5) · Chile's Rapa Nui (−7) |
| −6…−5 | Appalachia · New England (−5…−4) · Quebec (−5…−4) · Yucatán · Central America (Guatemala, Belize, El Salvador, Honduras, Nicaragua, Costa Rica) · Panama · Cuba · Jamaica · Dominican Republic · Bahamas · Aruba-Curaçao · Colombia · Ecuador · Peru · Bolivia · Amazonia (−5…−3) · Argentina (−5…−4) · Chile (−5…−4) · APAZ (Argentine–Chilean condominium, −5…−4) |
| −4…−2 | Venezuela · the Lesser Antilles states (all sovereign) · Guyana, Suriname, French Guiana (trade union) · Brazil (−4…−2) · Paraguay · Uruguay · Falklands ("deliberately unclaimed") · Greenland (to −1; status inconsistent between maps) · Iceland (−2…−1) |
| −1…0 | United Kingdom (England, Scotland, Wales) · Ireland · Northern Ireland · Crown Dependencies · Portugal · Spain · Catalonia · Basque Country · Andorra · Faroes · France (0…+1, incl. Wallonia, Brussels, Luxembourg) · Netherlands (incl. Flanders) |
| +1 | Germany (no Bavaria) · Austro-Bavaria · Switzerland, Liechtenstein, Monaco · **Magna Lombardia** (northern Italy, cap. Bologna) · **Meridia** (southern Italy + Sardinia, incl. Rome; Sicily autonomous) · San Marino, Vatican, Malta · Denmark · Norway (0…+2), Sweden (+1…+2), Finland (+1…+2), all in the Scandinavian Trade Union |
| +2…+3 | **CIN** (+1…+2; 21 states: Poland core → Lithuania + Kaliningrad → Czechia + Slovakia → Latvia → Estonia → Belarus → Ukraine (minus east) → Hungary → Romania → Moldova → Bulgaria → Croatia + Slovenia → Serbia → Montenegro → Greece → Skoprodija; Albania barred) · Cyprus · Russia (core, +2…+3) · Donska-Kubania · Karelia · North Caucasus republics (+3) · Turkey · Kurdistan · Syria · Lebanon · Jordan · Palestine · Iraq · Nejd and Hejaz · Georgia · Armenia · Azerbaijan |
| +4…+5 | Idelsk-Uralia (+2…+5) · Persia · Balochistan · Afghanistan · Qatar · UAE · Oman · the Yemens · Kazakhstan (+3…+6) · Central Asian republics · Pakistan · Sri Lanka · Nepal · East Turkestan (+5…+6) · Tibet (+5…+7) · India's remainder (unmapped, "out of scope") |
| +6…+7 | Siberia (+4…+8) · Tuva · Bangladesh · Bhutan · Madhyama · Myanmar · Thailand · Deep South · Laos · Vietnam · Cambodia · Aceh · Mongolia (+6…+8) · Sinian Federation (+6…+8) |
| +8 | **Sinian Federation** (Han core only, founded 2179) · **Taiwan** · **Mongolia** (incl. Inner Mongolia) · Manchuria (+8…+9) · Korea (+8…+9) · Philippines · Malaysia · Brunei · Singapore · **Indonesia** (+6…+9) · **Australia** (+8…+10) |
| +9…+10 | **Japan** (+8…+10) · **Korea (unified 2111)** · Timor-Leste · West Papua (independent) · Papua New Guinea · Micronesia · Palau · Guam · Northern Marianas · Australia (east) |
| +11…+12 | Solomon Is. · Vanuatu · New Caledonia · Nauru · Marshall Is. · **New Zealand** · Fiji · Tuvalu · Kiribati · Künnarantaiga (Russian Far East, cap. Vladivostok, +6…+12) |

## Nations that no longer exist

These are **gone in the map files**, though the census and specs still use them:
- **USA:** replaced by Alaska, Cascadia, Colorado, Sonora, Prairie Federation, Midwest Republic, Appalachia, New England, the CSA, plus Hawaii.
- **Canada:** split among Alaska, Cascadia, the Prairie Federation, Quebec and Greenland.
- **Italy:** split into Magna Lombardia and Meridia.
- **Russia:** split into 13 states.
- **China:** the Sinian Federation covers the Han core only; Manchuria, Tibet and East Turkestan are separate.
- **Belgium:** dissolved into France and the Netherlands. The map draws this already at the start of 2083, while the developer said early 2100s.
- **UK:** now excludes Northern Ireland.

## Open points from the maps
- Only East Asia is dated near 2564.
- Greenland's status is inconsistent between maps.
- Undecided: whether West Papua merges with PNG, and whether Guyana, Suriname and French Guiana merge.
- Nine Oceania territories are flagged for an author decision.
- India's remainder, the Maldives, Svalbard and the Atlantic islands are unmapped.
