# Upper Earth Immigration Composition — Reference

**Purpose:** Nation-of-origin immigration composition for each Tepenian city, derived from a three-factor composite analysis. Use this file when designing city culture, faction presence, NPC demographics, dialect flavoring, or any content that draws on a city's founding population character.

---

## Methodology

Three factors combined:

**1. Geographic proximity** — shorter routes carry more people faster; Southern Hemisphere nations have structural advantages over Northern Hemisphere nations for almost every Antarctic location.

**2. Population size** — the absolute number of people available to exile from each nation.

**3. GDP per capita × Gini inequality penalty (robot-ownership proxy)** — only people who could afford robots (or who loved/supported someone who owned one) would have been exile-eligible. High-GDP nations contribute a higher *proportion* of their population as effective exiles. However, high-inequality nations (high Gini coefficient) further reduce the eligible pool: wealth concentrated at the top means fewer people across the total population had meaningful robot access. Both GDP per capita AND income equality determine effective exile population.

**How the tiers are formed:** All nations in each city are ranked together by Gini-adjusted effective population. Tier 1 takes the nations with the largest effective pool (typically the top 1–2, determined by natural gaps in the ranking). Tier 2 takes the mid-range cluster. Tier 3 takes the smallest effective pools. Tier boundaries fall at the largest ratio gaps in each city's specific ranking.

**Gini-adjusted effective exile populations (approximate):**
| Nation | Gini-adjusted effective exiles | Notes |
|--------|-------------------------------|-------|
| China | ~210M | High pop, medium GDP, moderate Gini penalty |
| USA | ~155M | High pop, high GDP — significant Gini penalty (Gini ~0.39) reduces from raw high |
| Japan | ~65M | High GDP, low Gini — small penalty |
| Germany | ~46M | High GDP, very low Gini — minimal penalty |
| France | ~35M | High GDP, moderate Gini |
| UK | ~32M | High GDP, moderate-high Gini |
| Italy | ~27M | High GDP, moderate Gini |
| South Korea | ~26M | High GDP, moderate Gini |
| Russia | ~25M | Medium GDP, high Gini — significant reduction |
| Spain | ~20M | High GDP, moderate Gini |
| Canada | ~20M | High GDP, moderate Gini |
| Mexico | ~18M | Medium GDP, high Gini — significant reduction from 128M raw population |
| Brazil | ~17M | Lower-medium GDP, very high Gini (0.53) — massive reduction from raw population |
| Indonesia | ~16M | Lower-medium GDP, moderate Gini |
| Australia | ~13M | High GDP, moderate Gini |
| Netherlands | ~10M | High GDP, low Gini |
| Belgium | ~6.4M | High GDP, low Gini |
| Sweden | ~6M | High GDP, very low Gini |
| Argentina | ~6M | Medium GDP, high Gini — significant reduction |
| Norway | ~3.3M | High GDP, very low Gini — small nation |
| Finland | ~3.3M | High GDP, very low Gini — small nation |
| South Africa | ~3M | Lower-medium GDP, extreme Gini (0.63) — severe reduction from 60M population |
| New Zealand | ~2.6M | High GDP, moderate Gini — small nation |
| Chile | ~2.3M | Medium GDP, high Gini — significant reduction |
| Uruguay | ~0.6M | Medium GDP, moderate-high Gini — small nation |
| Poland | ~12M | Medium-high GDP, low Gini — strong effective conversion from 38M raw population; political center of the Intermarium/Intermaria meta-nation |
| Thailand | ~8M | Lower-medium GDP, high Gini — large population base preserves meaningful pool despite inequality penalty |
| Czech Republic | ~5M | High GDP, very low Gini — excellent conversion from 11M pop; among the highest per-capita robot-access rates of any nation |
| Ukraine | ~5M | Low GDP, very low Gini — Gini penalty minimal; raw economic constraint limits eligible fraction |
| Vietnam | ~5M | Low GDP, moderate Gini — large population (97M) partially compensates very low robot-access rate |
| Philippines | ~5M | Low GDP, high Gini — massive population base (110M) saves the effective number despite severe inequality |
| Romania | ~4.5M | Medium GDP, moderate Gini — solid mid-tier Intermarium member |
| Malaysia | ~5M | Medium GDP, moderate-high Gini — smaller base but better GDP than SEA peers |
| Hungary | ~3M | High GDP, low Gini — strong per-capita conversion from 10M pop; core Intermarium member |
| Slovakia | ~2.2M | High GDP, very low Gini — excellent rate but small nation (5.5M) |
| Belarus | ~1.5M | Lower-medium GDP, very low Gini — economic constraint is the binding factor |
| Croatia | ~1.3M | High GDP, low Gini — good rate; small nation (4M) |
| Bulgaria | ~1.2M | Lower-medium GDP, moderate Gini — Intermarium east member |
| Serbia | ~1.2M | Lower-medium GDP, moderate Gini — Intermarium south member |
| Lithuania | ~1M | High GDP, moderate Gini — Baltic Intermarium member |
| Slovenia | ~1M | Very high GDP, very low Gini — excellent rate; tiny population limits total |
| Latvia | ~0.6M | High GDP, moderate Gini — small Baltic nation |
| Estonia | ~0.6M | High GDP, low Gini — small Baltic nation; highest effective conversion rate of any Intermarium member |

**Intermarium/Intermaria note:** In the centuries leading up to the Falkland Treaty, Eastern Europe forms a political meta-nation — the Intermarium (later Intermaria) — centered on Poland. In the exile context, Intermarium nations constitute a culturally cohesive bloc at every QML city they appear in, despite being individually small. Collectively their combined effective pool (~40M across 14 member nations) rivals major European contributors.

**Where nations are very close** (Italy/South Korea/Russia at 25–27M; Spain/Canada at ~20M; Belgium/Sweden/Argentina at ~6M; Norway/Finland at ~3.3M) the ordering between them is approximate.

**Included source regions:** North and South America (including Mexico), Europe (incl. Russia and the full Intermarium/Intermaria bloc: Poland, Czech Republic, Slovakia, Hungary, Romania, Bulgaria, Ukraine, Belarus, Serbia, Croatia, Slovenia, Lithuania, Latvia, Estonia), Southeast Asia (Thailand, Vietnam, Philippines, Malaysia), Oceania (Australia, NZ), South Africa only from Africa.
**Excluded:** Indian subcontinent (India, Pakistan, Bangladesh, Sri Lanka, etc.), rest of Africa, Middle East.

**Operator identity:** Station founding nation is noted where it shapes the city's GDD character, but it is NOT used as a factor in this composite. Cities are analyzed as if ownership is irrelevant.

**How to read the tiers:**
- **Tier 1 — Primary:** Dominant long-run immigration character by Gini-adjusted effective population; shapes language, customs, city identity
- **Tier 2 — Significant:** Visible distinct communities; meaningfully present in city culture
- **Tier 3 — Notable:** Present and recognizable but not identity-defining; background texture

**Important temporal note:** Tiers reflect the long-run immigration equilibrium by Gini-adjusted effective population. They do NOT necessarily reflect *founding wave character*, which is determined by geographic proximity — whoever arrived first set the initial cultural identity. At many cities, a geographically close nation with a small Gini-adjusted effective pool established the founding character before large-pool distant nations arrived in volume. This temporal tension (founding identity vs. long-run population majority) is built into the GDD city designs and noted explicitly below where significant.

---

## Real-world Antarctic access gateways

| Gateway city | Serves | Key nations using it |
|-------------|--------|---------------------|
| Ushuaia / Punta Arenas (Argentina/Chile) | Antarctic Peninsula | Argentina, Chile, Brazil, USA, Europe via South America |
| Cape Town, South Africa | Queen Maud Land, Weddell Sea | South Africa, European Atlantic nations, Argentina/Brazil via South Atlantic |
| Christchurch / Lyttelton (NZ) | Ross Sea | New Zealand, USA, Australia, East Asian Pacific route |
| Hobart / Fremantle (Australia) | East Antarctic Indian Ocean coast | Australia, Japan, Indonesia/SE Asia, China, South Korea |
| Cape Town → Novo airfield (Russia-operated) | QML interior (Troll, Aboa, Princess Elisabeth, Maitri area) | South Africa, European nations by intercontinental air |
| Punta Arenas → Union Glacier (Chile) | South Pole direct | Chile, Argentina, private air operators |

---

## PALMER SUBNET ("American") — Antarctic Peninsula

**Corridor:** Drake Passage via Ushuaia and Punta Arenas. The Peninsula is the closest part of Antarctica to any inhabited landmass (~1,000km from Tierra del Fuego).

**Key Gini-adjustment finding:** USA rises to T1 sole primary at most Peninsula cities. Brazil and Argentina — previously the founding T1 nations — drop to T2 and T3 respectively when all nations in each city are ranked by Gini-adjusted effective population. The founding wave character of Peninsula cities remains overwhelmingly South American (Argentina, Chile, and Brazil arrive first), but long-run equilibrium is American-dominated.

---

### Palmer City *(Anvers Island, ~64°46'S 64°03'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective — by far the largest pool in this city's composition; natural break of 3.4× separates USA from next nation |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Canada** (20M), **Mexico** (18M), **Brazil** (17M) | Atlantic corridor Europeans + Mexico + Brazil; Mexico at 18M is nearly equivalent to Brazil; all 17–46M Gini-adjusted |
| 3 — Notable | **Argentina** (6M), **Chile** (2.3M), **Uruguay** (0.6M) | Geographic proximity nations — these three set the *founding wave character* of the city well before higher-volume distant nations arrive in volume; Argentina's high Gini drops it to 6M effective |

*Founding note: Argentina, Chile, and Uruguay arrive first by proximity. Their cultural stamp on Palmer City is disproportionate to their long-run Gini-adjusted share.*

---

### Rothera *(Adelaide Island, ~67°34'S 68°08'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective; same Peninsula dynamics |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Canada** (20M), **Mexico** (18M), **Brazil** (17M) | Atlantic corridor + Mexico; UK elevated by BAS/Rothera heritage in GDD; Mexico at 18M joins Brazil in the cluster |
| 3 — Notable | **Argentina** (6M), **Chile** (2.3M) | Founding wave proximity nations |

---

### Esperanza *(Hope Bay, ~63°24'S 56°59'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective |
| 2 — Significant | **UK** (32M), **Mexico** (18M), **Brazil** (17M), **Argentina** (6M) | No German/French presence in Esperanza's composition; UK (32M), Mexico (18M), Brazil (17M), and Argentina (6M) form T2; Argentina retained for founding-wave significance despite smaller effective pool |
| 3 — Notable | **Chile** (2.3M), **Uruguay** (0.6M) | Sub-3M Gini-adjusted proximity nations |

*Founding note: Esperanza's founding character is overwhelmingly Argentine — it is the Peninsula city closest to Buenos Aires embarkation ports. The GDD identity is Argentine; USA dominates long-run effective.*

---

### Marambio *(Seymour Island, ~64°14'S 56°39'W — air hub)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective; Marambio's air hub role specifically enables US logistics access |
| 2 — Significant | **Germany** (46M), **UK** (32M), **Spain** (20M), **Canada** (20M), **Mexico** (18M), **Brazil** (17M) | Spain at 20M elevated at Marambio — historical direct air access; Mexico at 18M joins the cluster; Spain and Canada both 20M Gini-adjusted |
| 3 — Notable | **Argentina** (6M), **Chile** (2.3M), **Uruguay** (0.6M) | Founding wave proximity nations |

---

### Juan Carlos I *(Livingston Island, South Shetlands, ~62°39'S 60°23'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Italy** (27M), **Spain** (20M) | European cluster; Spain at 20M elevated by cultural proximity to T3 Latin American population; Italy at 27M |
| 3 — Notable | **Mexico** (~18M), **Brazil** (17M), **Argentina** (6M), **Chile** (2.3M) | Mexico drops below European nations despite 128M raw population due to high Gini + medium GDP; South Shetlands are most proximate Peninsula location for South American founding wave |

---

### Port Lockroy *(Goudier Island, ~64°49'S 63°29'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Mexico** (18M), **Brazil** (17M) | Mexico at 18M joins T2 alongside Brazil; UK elevated by historical operator heritage; small settlement overall |
| 3 — Notable | **Argentina** (6M), **Chile** (2.3M) | Founding wave proximity nations |

*Note: Port Lockroy is a small settlement; total founding population modest regardless of national composition.*

---

### Sejong *(King George Island, ~62°13'S 58°47'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** (210M), **USA** (155M) | The two largest Gini-adjusted effective pools globally; both reach KGI via Pacific/Atlantic routes (~14,000–15,000km); natural gap of ~3× separates this pair from the next cluster |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Italy** (27M), **South Korea** (26M), **Russia** (25M), **Mexico** (18M), **Brazil** (17M) | Large effective pools 17–46M; Mexico at 18M joins the cluster; South Korea and Russia drop from operator-primary positions by Gini composite |
| 3 — Notable | **Argentina** (6M), **Chile** (2.3M), **Uruguay** (0.6M) | Founding wave proximity nations; sub-7M Gini-adjusted |

*Key note: South Korea drops from primary founding operator to T2 by Gini-adjusted composite. The KGI real-world multi-national character was almost entirely operator-driven. China and USA are the correct long-run population primaries.*

---

### Signy *(South Orkney Islands, ~60°43'S 45°36'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective; sole primary by wide margin |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Brazil** (17M) | Atlantic crossing nations; 17–46M Gini-adjusted cluster |
| 3 — Notable | **Argentina** (6M), **South Africa** (3M), **Chile** (2.3M), **Uruguay** (0.6M) | Geographic proximity nations; South Africa's Cape Town → South Orkneys crossing is the shortest from any inhabited coast to Signy specifically — founding wave advantage real, long-run effective pool is 3M |

*Key note: South Africa's geographic advantage at Signy gave it a disproportionate founding wave presence; extreme Gini (0.63) reduces effective to 3M. Founding character is South Atlantic proximity nations; long-run majority is US and European.*

---

## HALLEY SUBNET ("Atlantic") — Queen Maud Land / Weddell Sea

**Corridor:** Cape Town, South Africa (sea and Novo airfield gateway) and South Atlantic approaches from South America.

**Key Gini-adjustment finding:** South Africa drops dramatically across this entire subnet. Previously Tier 1 primary at almost every QML city based on Cape Town gateway proximity, South Africa's extreme Gini coefficient (0.63) reduces its effective pool from 60M raw population to ~3M — smaller than Argentina (6M). USA rises to T1 sole primary at most Halley cities. South Africa retains its geographic founding wave advantage but is correctly identified as a small-effective-pool nation in long-run composition.

---

### Halley *(Brunt Ice Shelf, Coats Land, ~75°35'S 26°34'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective; despite ~13,000km Atlantic route, largest pool in this city's composition |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Canada** (20M), **Brazil** (17M) | Atlantic and Cape Town corridor nations; Germany leads European cluster |
| 3 — Notable | **Poland** (12M), **Netherlands** (10M), **Argentina** (6M), **Czech Republic** (5M), **Hungary** (3M), **South Africa** (3M), **Slovakia** (2.2M), **Chile** (2.3M), **Croatia** (1.3M), **Serbia** (1.2M), **Slovenia** (1M) | Poland leads Intermarium west bloc (UTC+1 nations, just within ±3 of Halley's UTC-2); Netherlands (10M) alongside; Argentina via Weddell Sea approach; South Africa T3 despite gateway role; Romania/Belarus/eastern Intermarium outside ±3 window |

*Founding note: Halley's initial settlement was South African and Argentine. South Africa's gateway role gives it an outsized founding cultural impact relative to its 3M long-run effective pool.*

---

### Neumayer *(Ekström Ice Shelf, Atka Bay, ~70°41'S 8°16'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Brazil** (17M) | Cape Town corridor Europeans; Germany leads; German operator heritage in GDD is supported by T2 effective-pool reality |
| 3 — Notable | **Poland** (12M), **Netherlands** (10M), **Belgium** (6.4M), **Sweden** (6M), **Argentina** (6M), **Czech Republic** (5M), **Ukraine** (5M), **Romania** (4.5M), **Norway** (3.3M), **Finland** (3.3M), **Hungary** (3M), **South Africa** (3M), **Chile** (2.3M), **Slovakia** (2.2M), **Croatia** (1.3M), **Bulgaria** (1.2M), **Serbia** (1.2M), **Lithuania** (1M), **Slovenia** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | Full Intermarium west (UTC+1) + east (UTC+2) blocs within ±3 of Neumayer's UTC-1; Belarus (UTC+3) just outside; Poland leads at 12M; 21 nations in T3 reflects Neumayer's position as the central QML gateway |

---

### Troll *(Jutulsessen nunatak, ~72°01'S 2°32'E — Troll Airfield)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Russia** (25M), **Brazil** (17M) | Cape Town/Novo corridor; Russia present via Novolazarevskaya/Novo airfield; Germany leads European cluster |
| 3 — Notable | **Poland** (12M), **Netherlands** (10M), **Sweden** (6M), **Argentina** (6M), **Czech Republic** (5M), **Ukraine** (5M), **Romania** (4.5M), **Norway** (3.3M), **Finland** (3.3M), **Hungary** (3M), **South Africa** (3M), **Slovakia** (2.2M), **Belarus** (1.5M), **Croatia** (1.3M), **Bulgaria** (1.2M), **Serbia** (1.2M), **Lithuania** (1M), **Slovenia** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | Full Intermarium bloc including Belarus (UTC+3, just within ±3 of Troll's UTC+0); Norway and Finland via Troll Airfield intercontinental air routes — Norwegian founding character is GDD-embedded despite T3 effective |

*Key note: Troll Airfield's intercontinental air capability gives Norway faster access than distance alone suggests. The Norwegian founding character of Troll is culturally legitimate. Norway is correctly T3 in long-run Gini-adjusted composition.*

---

### Aboa *(Vestfjella nunataks, ~73°03'S 13°25'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Russia** (25M), **Brazil** (17M) | Same Cape Town/Novo cluster as Troll |
| 3 — Notable | **Poland** (12M), **Netherlands** (10M), **Belgium** (6.4M), **Sweden** (6M), **Argentina** (6M), **Czech Republic** (5M), **Ukraine** (5M), **Romania** (4.5M), **Norway** (3.3M), **Finland** (3.3M), **Hungary** (3M), **South Africa** (3M), **Slovakia** (2.2M), **Croatia** (1.3M), **Bulgaria** (1.2M), **Serbia** (1.2M), **Lithuania** (1M), **Slovenia** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | Same Intermarium west + east bloc as Neumayer (UTC+1 and UTC+2 nations, within ±3 of Aboa's UTC-1); Finland and Sweden are founding operator nations at Aboa — T3 in long-run Gini composite but Novo air corridor established their founding wave character |

*Key note: Finland and Sweden are correctly T3 by Gini-adjusted effective but the Finnish-Swedish co-founding character of Aboa is geographically supported. Their founding wave arrival via Novo set Aboa's initial identity.*

---

### Sanay *(Vesleskarvet nunatak, ~71°41'S 2°51'W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **Germany** | 46M Gini-adjusted effective — the largest pool in Sanay's composition since USA is not listed for this city; natural break of ~1.4× to UK below |
| 2 — Significant | **UK** (32M), **Brazil** (17M) | Second and third largest effective pools at this city |
| 3 — Notable | **Poland** (12M), **Argentina** (6M), **Czech Republic** (5M), **Ukraine** (5M), **Romania** (4.5M), **Norway** (3.3M), **Hungary** (3M), **South Africa** (3M), **Slovakia** (2.2M), **Chile** (2.3M), **Belarus** (1.5M), **Croatia** (1.3M), **Bulgaria** (1.2M), **Serbia** (1.2M), **Lithuania** (1M), **Slovenia** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | Full Intermarium including Belarus (all within ±3 of Sanay's UTC+0); South Africa — despite being SANAE founding operator — drops to T3 by Gini-adjusted effective (3M) |

*Key note: South Africa is no longer T1 primary at Sanay when ranked by Gini-adjusted effective population. The founding character of Sanay is South African (SANAE = South African National Antarctic Expedition; the only South African Antarctic station). Germany leads the long-run composition by effective population. Both facts are true simultaneously.*

---

### Princess Elisabeth *(Sør Rondane Mountains, ~71°57'S 23°21'E)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** (155M), **Japan** (65M) | USA: 155M; Japan: 65M via Fremantle/eastern approach to this 23°E position — the easternmost QML city makes the Indian Ocean eastern approach viable; natural gap of ~2.4× separates USA|Japan from next cluster |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Brazil** (17M), **Australia** (13M) | European Cape Town corridor and Australia at 13M via Fremantle eastern approach; Australia appears at this specific city and not at more westerly QML stations |
| 3 — Notable | **Poland** (12M), **Netherlands** (10M), **Belgium** (6.4M), **Argentina** (6M), **Czech Republic** (5M), **Ukraine** (5M), **Romania** (4.5M), **Norway** (3.3M), **Finland** (3.3M), **Hungary** (3M), **South Africa** (3M), **Slovakia** (2.2M), **Belarus** (1.5M), **Croatia** (1.3M), **Bulgaria** (1.2M), **Serbia** (1.2M), **Lithuania** (1M), **Slovenia** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | Full Intermarium including Belarus (all within ±3 of PE's UTC+2); Belgium's founding operator heritage in GDD culturally embedded despite T3 Gini effective; South Africa to T3 |

*Key note: Princess Elisabeth is the only Halley subnet city with meaningful eastern-approach immigration (Japan, Australia). Belgian founding character is GDD-embedded despite T3 by Gini composite.*

---

### Maitri_TBD *(Schirmacher Oasis, ~70°46'S 11°44'E — non-Indian founding population)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective |
| 2 — Significant | **Germany** (46M), **France** (35M), **UK** (32M), **Russia** (25M), **Brazil** (17M) | Russia at 25M: Novolazarevskaya co-located at this exact site, giving Russia infrastructure advantage; Russia's founding wave character at Maitri is the most justified of any Halley subnet city; Germany leads European cluster |
| 3 — Notable | **Poland** (12M), **Netherlands** (10M), **Argentina** (6M), **Czech Republic** (5M), **Ukraine** (5M), **Romania** (4.5M), **Norway** (3.3M), **Finland** (3.3M), **Hungary** (3M), **South Africa** (3M), **Slovakia** (2.2M), **Belarus** (1.5M), **Croatia** (1.3M), **Bulgaria** (1.2M), **Serbia** (1.2M), **Lithuania** (1M), **Slovenia** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | Full Intermarium including Belarus (all within ±3 of Maitri's UTC+1); Russia's T2 position reflects co-located Novolazarevskaya infrastructure; SA gateway but T3 by Gini |

*Key note: Russia holds a uniquely justified secondary position at Maitri_TBD — Novolazarevskaya co-location and Novo airfield operator role. Russia's T2 position is supported by both operator heritage and 25M Gini-adjusted effective.*

---

### Belgrano *(Confín Coast, Coats Land, ~77°52'S 34°37'W — Ruins accessible in DLC 5)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** | 155M Gini-adjusted effective; Atlantic route reaches even this deep Weddell Sea position |
| 2 — Significant | **Germany** (46M), **UK** (32M), **Brazil** (17M) | Atlantic corridor Europeans and Brazil; no France in Belgrano's composition |
| 3 — Notable | **Poland** (12M), **Argentina** (6M), **Czech Republic** (5M), **Hungary** (3M), **South Africa** (3M), **Slovakia** (2.2M), **Chile** (2.3M), **Croatia** (1.3M), **Serbia** (1.2M), **Slovenia** (1M), **Uruguay** (0.6M) | Argentina has the shortest approach to Belgrano and set the founding wave character; Intermarium west bloc (UTC+1 nations, just within ±3 of Belgrano's UTC-2) constitute the largest collective T3 presence; South Africa at T3 despite gateway proximity |

*Founding note: Argentina set the founding character of Belgrano — the Buenos Aires Weddell approach is shorter to this specific deep Weddell position than Cape Town. Argentine GDD identity is geographically legitimate for the founding wave; USA and Germany dominate long-run effective composition.*

---

## BYRD SUBNET ("Pacific") — West Antarctica / Ross Ice Shelf

**Corridor:** Christchurch (NZ) / Hobart (Australia) → Ross Sea → Ross Ice Shelf; secondary via Punta Arenas → Pacific (Chile approach).

**Key Gini-adjustment finding:** USA and Japan rise to T1 co-primaries at Ross Ice Shelf cities. Australia drops from sole T1 to T2. New Zealand — geographically the closest nation — drops to T3 at ~2.6M Gini-adjusted effective.

---

### Framheim *(Ross Ice Shelf, ~78°30'S 163°W)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** (155M), **Japan** (65M) | The two largest effective pools in this city's composition; both reach the Ross Ice Shelf via Pacific route (~14,000km) but their combined ~220M effective dwarfs all others; natural gap of ~2.4× separates USA|Japan from next cluster |
| 2 — Significant | **South Korea** (26M), **Canada** (20M), **Indonesia** (16M), **Australia** (13M) | Pacific corridor nations; Australia at 13M (~3,700km via Hobart) sets the *founding wave character* before higher-volume distant nations arrive |
| 3 — Notable | **New Zealand** (2.6M), **Chile** (2.3M) | Both sub-3M Gini-adjusted; NZ at ~3,800km from Christchurch is geographically closest — sets the very earliest arriving character |

*Founding note: NZ and Australia arrive first and set the founding wave character. USA and Japan dominate long-run composition.*

---

### Little America *(Ross Ice Shelf, ~78°30'S 163°W)*

Identical geographic position to Framheim. Same composite composition.

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **USA** (155M), **Japan** (65M) | Same; USA's "Little America" cultural identity pull amplifies its already-dominant effective contribution at this specific city |
| 2 — Significant | **South Korea** (26M), **Canada** (20M), **Indonesia** (16M), **Australia** (13M) | Same Pacific corridor cluster |
| 3 — Notable | **New Zealand** (2.6M), **Chile** (2.3M) | Same |

---

## JANBOGO SUBNET — Ross Sea

**Corridor:** Christchurch (NZ) → Ross Sea coast; secondary via Hobart (Australia).

**Key Gini-adjustment finding:** China and USA rise to T1 co-primaries at most Janbogo cities, replacing Australia and NZ from their previous T1 positions. China's 210M Gini-adjusted effective at ~14,000km produces the largest single national contribution at these cities. Australia drops to T2; NZ to T3.

---

### Janbogo *(Terra Nova Bay, ~74°37'S 164°13'E)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** (210M), **USA** (155M) | The two largest Gini-adjusted effective pools globally; both reach Terra Nova Bay via Pacific routes despite ~14,000km; natural gap of ~3× separates this pair from next cluster |
| 2 — Significant | **Japan** (65M), **Germany** (46M), **Italy** (27M), **South Korea** (26M), **Canada** (20M), **Indonesia** (16M), **Australia** (13M) | Pacific and Atlantic corridor nations 13–65M; Italy elevated by operator heritage in GDD; Australia (~3,700km Hobart/Christchurch) sets the founding wave character |
| 3 — Notable | **Philippines** (5M), **Malaysia** (5M), **New Zealand** (2.6M), **Chile** (2.3M) | Philippines and Malaysia (UTC+8, distance=3 from Janbogo's UTC+11) represent the SE Asian corridor's western reach; NZ at ~3,500km from Christchurch arrives first and establishes early character |

*Key note: South Korea drops from primary founding operator to T2 by Gini composite. Australia and NZ set the founding wave character via geographic proximity; China and USA dominate long-run composition.*

---

### Zukelli *(Terra Nova Bay, ~74°42'S 164°07'E — Destroyed)*

Same geographic position as Janbogo.

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** (210M), **USA** (155M) | Same |
| 2 — Significant | **Japan** (65M), **Italy** (27M), **South Korea** (26M), **Canada** (20M), **Indonesia** (16M), **Australia** (13M) | Italy: 27M effective — operator heritage strongly embedded in GDD city identity |
| 3 — Notable | **Philippines** (5M), **Malaysia** (5M), **New Zealand** (2.6M), **Chile** (2.3M) | Philippines and Malaysia via Pacific corridor; same geographic proximity founding wave nations for NZ and Chile |

---

### Cape Adare *(Northern Ross Sea coast, ~71°18'S 170°09'E)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** (210M), **USA** (155M) | Largest effective pools; both reach Cape Adare via Pacific routes |
| 2 — Significant | **Japan** (65M), **UK** (32M), **South Korea** (26M), **Canada** (20M), **Indonesia** (16M), **Australia** (13M) | UK elevated by historical Borchgrevink connection in GDD; Australia (~3,500km from Hobart — shortest approach from any major nation) sets early founding character |
| 3 — Notable | **Philippines** (5M), **Malaysia** (5M), **New Zealand** (2.6M), **Chile** (2.3M) | Philippines and Malaysia via Pacific; Cape Adare is the closest Antarctic point to NZ; NZ geographic primacy strongest here; founding wave is NZ-dominated |

---

### Fort McMurdo *(Ross Island, ~77°51'S 166°40'E)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** (210M), **USA** (155M) | The two largest effective pools; USA's operator heritage is GDD-justified and effective population reality confirms it as co-primary in the long run |
| 2 — Significant | **Japan** (65M), **Germany** (46M), **France** (35M), **UK** (32M), **Italy** (27M) | Pacific and Atlantic corridor large nations; 27–65M effective cluster |
| 3 — Notable | **South Korea** (26M), **Canada** (20M), **Indonesia** (16M), **Australia** (13M), **Philippines** (5M), **Malaysia** (5M), **New Zealand** (2.6M), **Chile** (2.3M) | South Korea drops from operator-primary to T3 by Gini composite; Australia and NZ set the founding wave character; Philippines and Malaysia via Pacific (UTC+8, distance=3 from McMurdo's UTC+11) |

*Key note: The American founding character of Fort McMurdo in the GDD reflects both operator heritage AND effective population reality. Australia and NZ are the founding wave nations; USA and China dominate long-run composition.*

---

### Scott *(Ross Island, ~77°51'S 166°46'E — 3km from Fort McMurdo)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** (210M), **USA** (155M) | Same McMurdo-adjacent dynamics |
| 2 — Significant | **Japan** (65M), **UK** (32M), **South Korea** (26M), **Canada** (20M), **Indonesia** (16M), **Australia** (13M) | NZ founding character embedded in GDD (Scott Station = NZ operator heritage); UK at 32M elevated by Commonwealth-NZ connection |
| 3 — Notable | **Philippines** (5M), **Malaysia** (5M), **New Zealand** (2.6M), **Chile** (2.3M) | Philippines and Malaysia via Pacific; NZ founder wave character — Scott's GDD identity is New Zealand despite NZ being T3 in Gini composition |

---

### Dumont d'Urville *(Adélie Land, ~66°40'S 140°01'E)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** (210M), **USA** (155M) | Largest effective pools; both reach DdU via Pacific routes |
| 2 — Significant | **Japan** (65M), **France** (35M), **South Korea** (26M), **Indonesia** (16M), **Australia** (13M) | Japan at 65M via Hobart/Fremantle (~9,000km) — shorter Japan-to-Antarctica route than most stations; France at 35M — founding operator heritage strongly embedded in GDD; Australia at 13M (Hobart → DdU ~2,800km, one of the shortest resupply routes of any Tepenian city) sets the founding wave character |
| 3 — Notable | **Thailand** (8M), **Vietnam** (5M), **Philippines** (5M), **Malaysia** (5M), **New Zealand** (2.6M) | SE Asian corridor dominant in T3 (all UTC+7–8, within ±3 of DdU's UTC+9); NZ via Christchurch/Hobart |

*Key note: France's cultural identity in the GDD is legitimate given its founding operator status. Australia (Hobart gateway) sets the founding wave character. China and USA dominate long-run composition.*

---

## MAWSON SUBNET — East Antarctic Coast (Indian Ocean Sector)

**Corridor:** Hobart and Fremantle (Australia) → East Antarctic Indian Ocean coast. South Africa (Cape Town) is a secondary gateway for the westernmost Mawson cities.

**Key Gini-adjustment finding:** China rises to T1 sole primary at every Mawson subnet city — its 210M Gini-adjusted effective at ~11,000km via Fremantle produces the largest national contribution everywhere. Japan consistently leads T2. Australia drops from T1 co-primary to T2 mid-tier. South Africa drops from T1 co-primary (at Mawson and Sayowa) to T3 across the entire subnet.

---

### Mawson *(Mac. Robertson Land, ~67°36'S 62°52'E)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** | 210M Gini-adjusted effective; ~11,000km via Fremantle; natural gap of ~3× separates China from Japan; sole T1 primary |
| 2 — Significant | **Japan** (65M), **Germany** (46M), **France** (35M), **UK** (32M), **South Korea** (26M), **Indonesia** (16M), **Australia** (13M) | Japan leads (65M, ~8,500km Fremantle); Germany and France via Cape Town approach (~9,500km); Australia (~4,500km Hobart/Fremantle) sets the founding wave character |
| 3 — Notable | **Poland** (12M), **Netherlands** (10M), **Thailand** (8M), **Czech Republic** (5M), **Ukraine** (5M), **Vietnam** (5M), **Romania** (4.5M), **Norway** (3.3M), **Hungary** (3M), **South Africa** (3M), **Slovakia** (2.2M), **Belarus** (1.5M), **Croatia** (1.3M), **Bulgaria** (1.2M), **Lithuania** (1M), **Slovenia** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | Mawson is uniquely dual-gateway: full Intermarium (UTC+1–3 nations, all within ±3 of UTC+4) meet SE Asian corridor (Thailand and Vietnam, UTC+7, just within ±3); South Africa T3 despite Cape Town approach |

---

### Davis *(Vestfold Hills, Prydz Bay, ~68°35'S 77°58'E)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** | 210M Gini-adjusted effective; sole T1 |
| 2 — Significant | **Japan** (65M), **Germany** (46M), **UK** (32M), **South Korea** (26M), **Indonesia** (16M), **Australia** (13M) | Japan leads T2; Germany and UK via Cape Town approach now competing with Hobart at this longitude; Australia (~4,000–4,500km Hobart/Fremantle) sets founding wave character |
| 3 — Notable | **Thailand** (8M), **Ukraine** (5M), **Vietnam** (5M), **Philippines** (5M), **Malaysia** (5M), **Romania** (4.5M), **South Africa** (3M), **New Zealand** (2.6M), **Belarus** (1.5M), **Bulgaria** (1.2M), **Lithuania** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | SE Asian corridor (Thailand, Vietnam, Philippines, Malaysia — UTC+7–8, all within ±3 of Davis's UTC+5) meets Intermarium east (Ukraine, Romania, Bulgaria, Baltic states, Belarus — UTC+2–3); SA via Cape Town (long at this longitude); NZ via Hobart |

---

### Zhongshan *(Larsemann Hills, Prydz Bay, ~69°22'S 76°22'E)*

Same geographic cluster as Davis.

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** | 210M Gini-adjusted effective; operator heritage in GDD + largest effective pool = sole T1 primary; the founding nation is also the long-run dominant nation |
| 2 — Significant | **Japan** (65M), **Germany** (46M), **UK** (32M), **South Korea** (26M), **Russia** (25M), **Indonesia** (16M), **Australia** (13M) | Russia at 25M: operator heritage partially justifies GDD secondary character; Australia sets founding wave character |
| 3 — Notable | **Thailand** (8M), **Ukraine** (5M), **Vietnam** (5M), **Philippines** (5M), **Malaysia** (5M), **Romania** (4.5M), **South Africa** (3M), **New Zealand** (2.6M), **Belarus** (1.5M), **Bulgaria** (1.2M), **Lithuania** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | Same SE Asian + Intermarium east corridor as Davis (both UTC+5 cluster) |

---

### Soyuz *(Larsemann Hills, Prydz Bay — Destroyed)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** | 210M Gini-adjusted effective; sole T1 |
| 2 — Significant | **Japan** (65M), **Germany** (46M), **UK** (32M), **South Korea** (26M), **Russia** (25M), **Indonesia** (16M), **Australia** (13M) | Russia at 25M: founding operator heritage at Soyuz is culturally legitimate in GDD even as T2 by effective population; Australia sets founding wave character |
| 3 — Notable | **Thailand** (8M), **Ukraine** (5M), **Vietnam** (5M), **Philippines** (5M), **Malaysia** (5M), **Romania** (4.5M), **South Africa** (3M), **Belarus** (1.5M), **Bulgaria** (1.2M), **Lithuania** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | SE Asian + Intermarium east corridor as per Prydz Bay UTC+5 cluster; South Africa gateway proximity cannot overcome extreme Gini reduction |

---

### Bharati_TBD *(Prydz Bay area, ~69°24'S 76°11'E — non-Indian founding population)*

Same Prydz Bay geographic cluster as Zhongshan and Davis.

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** | 210M Gini-adjusted effective; sole T1; no operator defined — purely geographic/effective-population baseline |
| 2 — Significant | **Japan** (65M), **Germany** (46M), **UK** (32M), **South Korea** (26M), **Russia** (25M), **Indonesia** (16M), **Australia** (13M) | Same Prydz Bay T2 cluster; Australia sets founding wave character |
| 3 — Notable | **Thailand** (8M), **Ukraine** (5M), **Vietnam** (5M), **Philippines** (5M), **Malaysia** (5M), **Romania** (4.5M), **South Africa** (3M), **New Zealand** (2.6M), **Belarus** (1.5M), **Bulgaria** (1.2M), **Lithuania** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | Same SE Asian + Intermarium east as Prydz Bay UTC+5 cluster |

*Design note: With no operator defined and no Indian population by canon, Bharati_TBD has the most "purely Gini-geographic" composition of any Tepenian city. The result is Chinese-primary with East Asian and European secondary — a fundamentally different character from surrounding operator-identity-driven cities.*

---

### Sayowa *(Lützow-Holm Bay, East Ongul Island, ~69°00'S 39°35'E)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** | 210M Gini-adjusted effective; ~11,000km via Fremantle; sole T1 |
| 2 — Significant | **Japan** (65M), **Germany** (46M), **France** (35M), **UK** (32M), **South Korea** (26M), **Indonesia** (16M), **Australia** (13M) | Sayowa's ~39°E longitude: dual-gateway city where Cape Town (~5,000–5,500km) and Hobart/Fremantle (~5,000–5,500km) are equally competitive; European Cape Town nations and East Asian Fremantle nations appear together in T2 |
| 3 — Notable | **Poland** (12M), **Netherlands** (10M), **Czech Republic** (5M), **Ukraine** (5M), **Romania** (4.5M), **Norway** (3.3M), **Hungary** (3M), **South Africa** (3M), **Slovakia** (2.2M), **Belarus** (1.5M), **Croatia** (1.3M), **Bulgaria** (1.2M), **Serbia** (1.2M), **Lithuania** (1M), **Slovenia** (1M), **Latvia** (0.6M), **Estonia** (0.6M) | Full Intermarium including Belarus (all within ±3 of Sayowa's UTC+3); South Africa drops to T3 despite Cape Town gateway advantage |

*Key note: Sayowa is the only Mawson subnet city where Cape Town and Fremantle approaches are genuinely equally competitive. The T2 composition reflects this dual-gateway character: European (Germany, France, UK via Cape Town) alongside East Asian (Japan, South Korea, Indonesia via Fremantle).*

---

## MIRNY SUBNET ("Australian") — Davis Coast / Wilkes Land Interior

**Corridor:** Hobart (Australia) → East Antarctic Davis Coast / Wilkes Land.

---

### Mirny *(Davis Coast, ~66°33'S 93°01'E)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** | 210M Gini-adjusted effective; sole T1 |
| 2 — Significant | **Japan** (65M), **UK** (32M), **South Korea** (26M), **Russia** (25M), **Indonesia** (16M), **Australia** (13M) | Japan leads T2; Russia at 25M — operator heritage in GDD; Australia (~3,500–4,000km Hobart — one of the shortest Australia-to-Antarctica routes) sets founding wave character |
| 3 — Notable | **Thailand** (8M), **Vietnam** (5M), **Philippines** (5M), **Malaysia** (5M), **South Africa** (3M), **New Zealand** (2.6M), **Belarus** (1.5M) | SE Asian corridor (all UTC+7–8, within ±3 of Mirny's UTC+6) is the dominant T3 presence; Belarus (UTC+3, distance=3) just qualifies; Romania/Ukraine outside ±3 window; SA via Cape Town long at 93°E |

---

### Casey *(Wilkes Land, ~66°17'S 110°32'E)*

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** (210M), **USA** (155M) | Casey sits at the boundary between Ross Sea and East Antarctic corridors; the Pacific approach from USA (~12,000km) is shorter here than at deeper East Antarctic stations, bringing USA into T1 co-primary alongside China |
| 2 — Significant | **Japan** (65M), **France** (35M), **South Korea** (26M), **Russia** (25M), **Indonesia** (16M), **Australia** (13M) | Japan leads T2; France at 35M — operator of nearby DdU; Australia (~3,400km Hobart — shortest Australia-to-Antarctica route of any Tepenian city) sets founding wave character |
| 3 — Notable | **Thailand** (8M), **Vietnam** (5M), **Philippines** (5M), **Malaysia** (5M), **New Zealand** (2.6M) | SE Asian corridor (UTC+7–8) dominant in T3; Thailand and Vietnam share the same solar UTC as Casey; Philippines and Malaysia one step east; NZ via Hobart elevated by Casey's boundary position between Ross Sea and East Antarctic corridors |

---

## AMUNDSEN STATION — South Pole (Inter-Subnet Relay, DLC 1)

**Corridors:** McMurdo chain (Christchurch → McMurdo → Pole by air) and Union Glacier direct (Punta Arenas → Union Glacier → Pole by air).

| Tier | Nations | Key drivers |
|------|---------|-------------|
| 1 — Primary | **China** (210M), **USA** (155M) | The two largest Gini-adjusted effective pools globally; both reach the South Pole via long routes but their combined effective (~365M) far exceeds all others in this city's composition; natural gap of ~2.4× separates USA from Japan below |
| 2 — Significant | **Japan** (65M), **Germany** (46M), **UK** (32M), **South Korea** (26M), **Canada** (20M), **Australia** (13M) | Pacific and Atlantic corridor large nations 13–65M; Australia via McMurdo chain sets the founding wave character alongside NZ |
| 3 — Notable | **Argentina** (6M), **Norway** (3.3M), **New Zealand** (2.6M), **Chile** (2.3M) | Chile uniquely elevated at the South Pole specifically — Union Glacier route (~3,700km Punta Arenas → Pole) is the shortest direct path from any inhabited continent to the geographic Pole; Argentina via Union Glacier shared gateway; Norway: Amundsen heritage pull + Novo → Pole air option; NZ via McMurdo chain |

*Key note: Chile's Union Glacier route makes it prominent at the South Pole in a way not seen at any other Tepenian city. Despite only 2.3M Gini-adjusted effective, Chile's geographic advantage here is unique and GDD-justified. Norway's Amundsen heritage (Saint Roald) gives it cultural significance disproportionate to its T3 effective population.*

---

## Summary: Five Key Findings from Gini-Adjusted Reanalysis

**1. China and USA are T1 co-primaries at the majority of Tepenian cities.**
Once the full Gini adjustment is applied and all nations in each city are ranked together by effective population, China (210M) and USA (155M) emerge as co-T1 primaries at Janbogo, Fort McMurdo, Scott, Dumont d'Urville, Casey, and Amundsen. USA is T1 sole primary at Palmer, Halley, and Signy subnet cities. China is T1 sole primary at the entire Mawson and Mirny subnets.

**2. South Africa drops to T3 across almost the entire Halley subnet.**
South Africa's extreme Gini coefficient (0.63) reduces its effective pool from 60M raw population to ~3M — smaller than Argentina (6M). Despite controlling the Cape Town gateway, South Africa is T3 at every Halley city. It retains the founding wave advantage (arrives first, sets early character) but not the long-run population majority.

**3. Geographic proximity nations set the founding wave character but not the long-run majority.**
The systematic finding: geographically close nations with small Gini-adjusted effective pools (Argentina at the Peninsula, South Africa at QML, Australia/NZ at the Ross Sea) arrive first and establish founding cultural identity. But large-effective-pool distant nations (USA, China, Japan, Germany) eventually dominate in total volume. Both facts are true simultaneously and both matter for GDD city design.

**4. Germany consistently leads European groupings.**
Germany's combination of 46M effective population and very low Gini coefficient makes it the leading European contributor at every city where European nations appear. Previously often listed after UK or France; Germany now leads every European cluster.

**5. Brazil drops from Peninsula T1 to T2; South Korea drops at every city it appears.**
Brazil's extreme Gini (0.53) reduces effective pool from ~60M raw to 17M. It falls from founding T1 primary at Peninsula cities to T2 secondary. South Korea drops from operator-primary at Sejong, Janbogo, and Zukelli to T2 secondary (Sejong) or T3 (Janbogo, Zukelli, McMurdo) at every city it appears.

---

*Cross-reference: city spec files are in `Specs/`. Station-to-city mapping is in `Station_to_City_Map.md`.*

---

## Pre-Long Night War Tepenian Census

**Methodology:**
- Human exiles per nation = Gini-adjusted effective population × **3%** (the fraction of the robot-eligible ceiling that actually exiled)
- Robot population ≈ equal to human population (solo unattached robots offset by human ideological allies without robot relationships; net effect approximately 1:1)
- City distribution: each nation's exiles distributed across its eligible cities (within ±3 solar time zones of the nation's home UTC), weighted by tier — **T1 = 8 shares, T2 = 3 shares, T3 = 1 share**
- All figures are pre-Long Night War equilibrium estimates; margin of error ≈ ±15%

**Total Tepenian population (pre-war):**

| | Count |
|--|--|
| Humans | ~24,950,000 |
| Robots | ~24,950,000 |
| **Combined** | **~49,900,000 (~50M)** |

*For scale: comparable to South Korea, Spain, or Argentina. The Long Night War did not merely end a city — it ended a civilization.*

---

### Nation exile totals (humans only)

| Nation | Gini-adj. effective | Human exiles (3%) |
|--------|--------------------|--------------------|
| China | 210M | 6,300,000 |
| USA | 155M | 4,650,000 |
| Japan | 65M | 1,950,000 |
| Germany | 46M | 1,380,000 |
| France | 35M | 1,050,000 |
| UK | 32M | 960,000 |
| Italy | 27M | 810,000 |
| South Korea | 26M | 780,000 |
| Russia | 25M | 750,000 |
| Spain | 20M | 600,000 |
| Canada | 20M | 600,000 |
| Mexico | 18M | 540,000 |
| Brazil | 17M | 510,000 |
| Indonesia | 16M | 480,000 |
| Australia | 13M | 390,000 |
| Poland | 12M | 360,000 |
| Netherlands | 10M | 300,000 |
| Thailand | 8M | 240,000 |
| Belgium | 6.4M | 192,000 |
| Sweden | 6M | 180,000 |
| Argentina | 6M | 180,000 |
| Czech Republic | 5M | 150,000 |
| Ukraine | 5M | 150,000 |
| Vietnam | 5M | 150,000 |
| Philippines | 5M | 150,000 |
| Romania | 4.5M | 135,000 |
| Malaysia | 5M | 150,000 |
| Norway | 3.3M | 99,000 |
| Finland | 3.3M | 99,000 |
| South Africa | 3M | 90,000 |
| Hungary | 3M | 90,000 |
| New Zealand | 2.6M | 78,000 |
| Chile | 2.3M | 69,000 |
| Slovakia | 2.2M | 66,000 |
| Belarus | 1.5M | 45,000 |
| Croatia | 1.3M | 39,000 |
| Bulgaria | 1.2M | 36,000 |
| Serbia | 1.2M | 36,000 |
| Lithuania | 1M | 30,000 |
| Slovenia | 1M | 30,000 |
| Uruguay | 0.6M | 18,000 |
| Latvia | 0.6M | 18,000 |
| Estonia | 0.6M | 18,000 |
| **TOTAL** | **~832M** | **~24,950,000** |

---

### City populations (pre-war, humans + robots combined)

Sorted by total population. Cities marked *(destroyed)* or *(ruins)* still had full populations before the Long Night War.

| Rank | City | Subnet | Humans (est.) | Robots (est.) | **Total** |
|------|------|--------|--------------|--------------|-----------|
| 1 | **Sejong** | Palmer | 1,144,000 | 1,144,000 | **2,288,000** |
| 2 | **Fort McMurdo** | Janbogo | 1,071,000 | 1,071,000 | **2,141,000** |
| 3 | **Janbogo** | Janbogo | 1,041,000 | 1,041,000 | **2,082,000** |
| 4 | **Casey** | Mirny | 996,000 | 996,000 | **1,992,000** |
| 5 | **Zukelli** *(destroyed)* | Janbogo | 987,000 | 987,000 | **1,975,000** |
| 6 | **Mawson** | Mawson | 943,000 | 943,000 | **1,886,000** |
| 7 | **Dumont d'Urville** | Janbogo | 913,000 | 913,000 | **1,826,000** |
| 8 | **Sayowa** | Mawson | 906,000 | 906,000 | **1,812,000** |
| 9 | **Amundsen Station** | South Pole | 904,000 | 904,000 | **1,808,000** |
| 10 | **Scott** | Janbogo | 894,000 | 894,000 | **1,788,000** |
| 11 | **Princess Elisabeth** | Halley | 890,000 | 890,000 | **1,779,000** |
| 12 | **Zhongshan** | Mawson | 881,000 | 881,000 | **1,762,000** |
| 13 | **Cape Adare** | Janbogo | 861,000 | 861,000 | **1,722,000** |
| 14 | **Juan Carlos I** | Palmer | 848,000 | 848,000 | **1,695,000** |
| 15 | **Bharati_TBD** | Mawson | 843,000 | 843,000 | **1,686,000** |
| 16 | **Soyuz** *(destroyed)* | Mawson | 838,000 | 838,000 | **1,675,000** |
| 17 | **Aboa** | Halley | 809,000 | 809,000 | **1,617,000** |
| 18 | **Davis** | Mawson | 805,000 | 805,000 | **1,611,000** |
| 19 | **Mirny** | Mirny | 790,000 | 790,000 | **1,579,000** |
| 20 | **Marambio** | Palmer | 751,000 | 751,000 | **1,502,000** |
| 21 | **Troll** | Halley | 750,000 | 750,000 | **1,501,000** |
| 22 | **Maitri_TBD** | Halley | 660,000 | 660,000 | **1,321,000** |
| 23 | **Neumayer** | Halley | 639,000 | 639,000 | **1,278,000** |
| 24 | **Framheim** | Byrd | 573,000 | 573,000 | **1,146,000** |
| 25 | **Little America** | Byrd | 573,000 | 573,000 | **1,146,000** |
| 26 | **Halley** | Halley | 557,000 | 557,000 | **1,114,000** |
| 27 | **Palmer City** | Palmer | 513,000 | 513,000 | **1,026,000** |
| 28 | **Rothera** | Palmer | 510,000 | 510,000 | **1,020,000** |
| 29 | **Signy** | Palmer | 466,000 | 466,000 | **931,000** |
| 30 | **Port Lockroy** | Palmer | 457,000 | 457,000 | **914,000** |
| 31 | **Belgrano** *(ruins, DLC 5)* | Halley | 408,000 | 408,000 | **816,000** |
| 32 | **Sanay** | Halley | 365,000 | 365,000 | **730,000** |
| 33 | **Esperanza** | Palmer | 363,000 | 363,000 | **727,000** |
| — | **TOTAL** | — | **24,950,000** | **24,950,000** | **49,900,000** |

---

### Subnet totals (pre-war)

| Subnet | Cities | Human total | Combined total |
|--------|--------|-------------|----------------|
| Janbogo / Ross Sea | 6 | 5,767,000 | 11,533,000 |
| Mawson / Indian Ocean | 6 | 5,216,000 | 10,432,000 |
| Halley / Queen Maud Land | 8 | 5,079,000 | 10,157,000 |
| Palmer / Antarctic Peninsula | 8 | 5,051,000 | 10,102,000 |
| Mirny / Wilkes Land | 2 | 1,786,000 | 3,571,000 |
| Byrd / Ross Ice Shelf | 2 | 1,146,000 | 2,291,000 |
| Amundsen / South Pole | 1 | 904,000 | 1,808,000 |
| **TOTAL** | **33** | **24,949,000** | **49,894,000** |

---

### Census design notes

**Sejong (KGI) is the largest Tepenian city**, not Fort McMurdo as some might expect. Its exceptional size results from King George Island's unique multi-national composition: the only city with both China (210M) and USA (155M) at T1 co-primary, PLUS Russia, South Korea, and Italy contributing large T2 pools, PLUS the most diverse T2 cluster of any Tepenian city. The real-world multi-station character of KGI produces the largest accumulated gravity score.

**The Ross Sea/Janbogo subnet is the most populous subnet overall** (~11.5M combined), driven by the China+USA T1 co-primary composition across six cities. The Mawson and Halley subnets are nearly equal in size despite very different compositions — Mawson's China-only T1 with large East Asian T2 cluster versus Halley's USA T1 with European T2 cluster.

**Two major cities were destroyed in the Long Night War:** Zukelli (~1,975,000 total) and Soyuz (~1,675,000 total). Combined: ~3,650,000 people — a loss greater than the entire Palmer subnet's human population. Belgrano (~816,000 total) became ruins in the DLC 5 timeframe.

**The Intermarium/Intermaria bloc collectively contributes ~1.2M human exiles** distributed across QML and Mawson cities, constituting the second-largest European cultural community after the Germany-France-UK-Italy core. As a political meta-nation, their community cohesion in Tepenia exceeds their individual national sizes suggest.

**The Southeast Asian corridor (Thailand, Vietnam, Philippines, Malaysia — ~690,000 combined exiles)** is concentrated in the Mawson/Mirny/Janbogo overlap zone, creating a distinct cultural corridor from Mawson east through Casey and into the Ross Sea cities via Philippines and Malaysia. Indonesia (480,000 exiles) is their T2-ranked peer already embedded in these cities.

---

## Island Population Balancing — Revised Physical Census

The Gini-adjusted tier calculation distributes exiles mathematically without regard for the physical carrying capacity of the locations. Eleven cities are on islands — from the vast ice sheet of King George Island to the real-world 40m × 20m footprint of Goudier Island. The revised census below caps each island city at a semi-comfortable population for its actual land area (generous for sci-fi vertical construction, still constrained by ocean boundaries and harsh climate logistics), and redistributes the overflow to the nearest eligible mainland/ice-shelf coastal cities within ±3 solar time zones.

**Redistribution methodology:**
- Overflow from each island city flows only to mainland coastal or ice-shelf cities (not to other islands, not to interior cities like Troll, Aboa, Sanay, or the South Pole)
- Peninsula island overflow → **Esperanza** (50%, only mainland Peninsula coast), **Halley** (20%), **Belgrano** (15%), **Neumayer** (15%) — Rothera overflow excludes Neumayer (distance = 4 time zones)
- Ross Island (McMurdo + Scott) overflow → **Janbogo** (40%), **Zukelli** (25%), **Cape Adare** (20%), **Framheim** (7.5%), **Little America** (7.5%)
- DdU overflow → **Casey** (30%), **Mirny** (25%), **Janbogo** (20%), **Zukelli** (10%), **Cape Adare** (10%), **Framheim/Little America** (2.5% each)
- Sayowa overflow → **Mawson** (25%), **Mirny** (20%), **Maitri_TBD** (15%), **Davis** (15%), **Zhongshan** (15%), **Bharati_TBD** (10%)

### Island caps

| City | Island | Island size / notes | Raw calc. | **Cap** | Overflow |
|------|--------|---------------------|-----------|---------|---------|
| Port Lockroy | Goudier Island | ~40m × 20m real; GDD expands to surrounding waters but site is tiny; small settlement by design | 457K | **100K** | 357K |
| Signy | South Orkney Islands | Signy Island ~20 km²; isolated sub-Antarctic; hard supply chain | 466K | **150K** | 316K |
| Sayowa | East Ongul Island | ~28 km² ice-free; very small; but dual-gateway role earns a slightly higher cap | 906K | **200K** | 706K |
| Rothera | Adelaide Island | ~2,500 km² but ~95% glaciated; ice-free patches small | 510K | **250K** | 260K |
| Palmer City | Anvers Island | ~2,432 km², heavily glaciated; limited buildable coastline | 513K | **280K** | 233K |
| Juan Carlos I | Livingston Island | ~1,200 km², heavily glaciated; South Shetlands | 848K | **300K** | 548K |
| Scott | Ross Island (shared) | Shared with Fort McMurdo; combined Ross Island cap = 650K humans | 894K | **300K** | 594K |
| Fort McMurdo | Ross Island (shared) | Largest ice-free zone on Ross Island; ~1/3 of 2,460 km² usable | 1,071K | **350K** | 721K |
| Dumont d'Urville | Petrel Island | Small island in Géologie Archipelago; GDD city expands into surrounding Adélie coastline | 913K | **350K** | 563K |
| Marambio | Seymour Island | ~1,200 km², ~70% permanently ice-free — the most buildable island in the entire Peninsula zone; air hub | 751K | **450K** | 301K |
| Sejong | King George Island | Largest South Shetland (~1,200 km²); most ice-free patches of any S. Shetland; 11-nation founding character | 1,144K | **500K** | 644K |
| **Total overflow** | | | | | **5,241K** |

### Final city populations (island-balanced)

Ranked by final human population. Cities in **bold** gained population from overflow. Capped cities listed with their cap. Two cities marked *(destroyed)* and one *(ruins)* reached these populations before their fate.

| Rank | City | Subnet | Raw humans | **Final humans** | **Final total** | Notes |
|------|------|--------|-----------|-----------------|-----------------|-------|
| 1 | **Janbogo** | Janbogo | 1,041K | **1,680K** | **3,360K** | Mainland coast; receives Ross Is. + DdU overflow |
| 2 | **Esperanza** | Palmer | 363K | **1,649K** | **3,298K** | ONLY mainland Peninsula coast city; sole destination for all Peninsula island overflow |
| 3 | Zukelli *(destroyed)* | Janbogo | 987K | **1,372K** | **2,745K** | Mainland coast; receives Ross Is. + DdU overflow; later destroyed |
| 4 | **Cape Adare** | Janbogo | 861K | **1,180K** | **2,360K** | Mainland coast; receives Ross Is. + DdU overflow |
| 5 | **Casey** | Mirny | 996K | **1,165K** | **2,330K** | Mainland coast; receives DdU overflow |
| 6 | **Halley** | Halley | 557K | **1,123K** | **2,247K** | Ice shelf coast; absorbs Peninsula island overflow |
| 7 | **Mawson** | Mawson | 943K | **1,119K** | **2,239K** | Mainland coast; receives Sayowa overflow |
| 8 | **Mirny** | Mirny | 790K | **1,071K** | **2,143K** | Mainland coast; receives DdU + Sayowa overflow |
| 9 | **Neumayer** | Halley | 639K | **999K** | **1,997K** | Ice shelf coast; absorbs Peninsula island overflow |
| 10 | **Zhongshan** | Mawson | 881K | **987K** | **1,974K** | Mainland coast; receives Sayowa overflow |
| 11 | **Bharati_TBD** | Mawson | 843K | **914K** | **1,828K** | Mainland coast; receives Sayowa overflow |
| 12 | **Davis** | Mawson | 805K | **911K** | **1,823K** | Mainland coast; receives Sayowa overflow |
| 13 | Amundsen Station | Amundsen | 904K | 904K | 1,808K | South Pole; multi-corridor, no island cap |
| 14 | Princess Elisabeth | Halley | 890K | 890K | 1,779K | Inland mountain range; no cap, no overflow received |
| 15 | **Belgrano** *(ruins, DLC 5)* | Halley | 408K | **854K** | **1,708K** | Mainland coast; absorbs Peninsula island overflow |
| 16 | Soyuz *(destroyed)* | Mawson | 838K | 838K | 1,675K | Mainland coast; no change |
| 17 | Aboa | Halley | 809K | 809K | 1,618K | Inland; no change |
| 18 | **Maitri_TBD** | Halley | 660K | **766K** | **1,533K** | Coastal-adjacent; receives Sayowa overflow |
| 19 | Troll | Halley | 750K | 750K | 1,501K | Inland; no change |
| 20 | **Framheim** | Byrd | 573K | **686K** | **1,371K** | Ice shelf; receives Ross Is. + DdU overflow |
| 21 | **Little America** | Byrd | 573K | **686K** | **1,371K** | Ice shelf; same as Framheim |
| 22 | Sejong *(capped)* | Palmer | 1,144K | **500K** | **1,000K** | KGI; still a major international hub at 1M total |
| 23 | Marambio *(capped)* | Palmer | 751K | **450K** | **900K** | Seymour Island; largest island city by cap |
| 24 | Sanay | Halley | 365K | 365K | 730K | Inland; no change |
| 25 | Fort McMurdo *(capped)* | Janbogo | 1,071K | **350K** | **700K** | Ross Island; twin city with Scott |
| 26 | Dumont d'Urville *(capped)* | Janbogo | 913K | **350K** | **700K** | Petrel Island |
| 27 | Scott *(capped)* | Janbogo | 894K | **300K** | **600K** | Ross Island; twin city with Fort McMurdo |
| 28 | Juan Carlos I *(capped)* | Palmer | 848K | **300K** | **600K** | Livingston Island |
| 29 | Palmer City *(capped)* | Palmer | 513K | **280K** | **560K** | Anvers Island |
| 30 | Rothera *(capped)* | Palmer | 510K | **250K** | **500K** | Adelaide Island |
| 31 | Sayowa *(capped)* | Mawson | 906K | **200K** | **400K** | East Ongul Island |
| 32 | Signy *(capped)* | Palmer | 466K | **150K** | **300K** | South Orkney Islands |
| 33 | Port Lockroy *(capped)* | Palmer | 457K | **100K** | **200K** | Goudier Island |
| — | **TOTAL** | — | **24,948K** | **24,948K** | **49,896K** | Total preserved; only redistribution |

### Subnet totals (island-balanced)

| Subnet | Human total | Combined total | Change from raw |
|--------|-------------|----------------|-----------------|
| **Halley / Queen Maud Land** | **6,557K** | **13,113K** | ▲+1,478K (absorbs Peninsula island overflow) |
| **Janbogo / Ross Sea** | **5,232K** | **10,463K** | ▼−535K (loses McMurdo/Scott/DdU to caps, gains as mainland destination) |
| **Mawson / Indian Ocean** | **4,969K** | **9,938K** | ▼−247K (Sayowa capped; mainland Mawson cities absorb partial offset) |
| **Palmer / Antarctic Peninsula** | **3,679K** | **7,357K** | ▼−1,372K (most Peninsula cities are islands; overflow leaves to QML) |
| **Mirny / Wilkes Land** | **2,236K** | **4,473K** | ▲+451K (Casey+Mirny absorb DdU+Sayowa overflow) |
| **Byrd / Ross Ice Shelf** | **1,371K** | **2,742K** | ▲+225K (receives Ross Is. + DdU overflow) |
| **Amundsen / South Pole** | **904K** | **1,808K** | unchanged |

### Island-balancing design notes

**Esperanza becomes the dominant city of the Antarctic Peninsula** — not Sejong. As the only true mainland coast city in the Palmer subnet, it absorbs overflow from seven island cities and grows from a modest 727K total (raw) to ~3.3M total. Its Argentine founding wave character is massively amplified: Esperanza is the place Peninsula people go when the islands fill up, and the first city most Argentines build toward. GDD should treat Esperanza as the de facto capital of the Antarctic Peninsula zone.

**Janbogo overtakes Esperanza to become the single largest Tepenian city** (~3.36M total), displacing Sejong from the raw-calculation top slot. Terra Nova Bay mainland coast absorbs Ross Island + DdU overflow and becomes the commercial and strategic heart of the Ross Sea region. The Janbogo-Zukelli twin-city complex at Terra Nova Bay combined is ~6.1M total (before Zukelli's destruction).

**Zukelli's destruction becomes the single most devastating event of the Long Night War.** At ~2.74M total inhabitants, Zukelli would have been the third-largest city in all of Tepenia. Its loss is comparable to losing a mid-sized nation-state's entire population in one event.

**The Halley subnet becomes the most populous subnet overall** (~13.1M combined, up from ~10.2M raw) once Peninsula island overflow is factored in. Halley, Neumayer, and Belgrano all grow substantially. **Belgrano in particular** — described in the GDD as DLC 5 ruins — reaches ~1.7M total before its fall. Ruins of a 1.7M-person city is a very different narrative weight than ruins of a small outpost.

**Sayowa drops from a calculated 906K to a capped 200K** due to East Ongul Island's true size (~28 km² ice-free). Despite its small physical footprint, Sayowa retains enormous cultural significance as the gateway between the European Atlantic corridor and the East Asian Pacific corridor — the only dual-approach Mawson subnet city. Small population, outsized identity.

---

## Canon Census I — Before Space Colonization (Pre-Orbital Era)

**Rate change:** All prior census figures used a 3% exile fraction. Revised to **2%** (a slightly more conservative read on what fraction of the robot-eligible population actually relocated). The island-balanced final figures above are multiplied by **×0.65** (= 2/3, rounded) to produce all canon population numbers. No redistribution logic changes; only the scale shifts.

**Canon totals:**

| | Count |
|--|--|
| Humans | ~15,125,000 |
| Robots | ~15,709,000 |
| **Combined** | **~30,834,000 (~30.8M)** |

*For scale: comparable to Peru or Venezuela — a mid-sized nation-state. The Long Night War killed a country.*

*Note: Human and robot totals are no longer equal. Amundsen Station has a disproportionate robot workforce (see city table); additionally, human populations received a random 1–5% further reduction per city (modeling natural variation in arrival and survival rates), while robot populations were unchanged.*

### Canon nation exile totals

| Nation | Exiles (2% rate) | | Nation | Exiles (2% rate) |
|--------|------------------|-|--------|-----------------|
| China | 4,095,000 | | Netherlands | 195,000 |
| USA | 3,022,500 | | Thailand | 156,000 |
| Japan | 1,267,500 | | Belgium | 124,800 |
| Germany | 897,000 | | Sweden | 117,000 |
| France | 682,500 | | Argentina | 117,000 |
| UK | 624,000 | | Czech Republic | 97,500 |
| Italy | 526,500 | | Ukraine | 97,500 |
| South Korea | 507,000 | | Vietnam | 97,500 |
| Russia | 487,500 | | Philippines | 97,500 |
| Spain | 390,000 | | Malaysia | 97,500 |
| Canada | 390,000 | | Romania | 87,750 |
| Mexico | 351,000 | | Norway | 64,350 |
| Brazil | 331,500 | | Finland | 64,350 |
| Indonesia | 312,000 | | South Africa | 58,500 |
| Australia | 253,500 | | Hungary | 58,500 |
| Poland | 234,000 | | New Zealand | 50,700 |
| | | | Chile | 44,850 |
| | | | Slovakia | 42,900 |
| | | | Belarus | 29,250 |
| | | | Croatia | 25,350 |
| | | | Bulgaria | 23,400 |
| | | | Serbia | 23,400 |
| | | | Lithuania | 19,500 |
| | | | Slovenia | 19,500 |
| | | | Uruguay | 11,700 |
| | | | Latvia | 11,700 |
| | | | Estonia | 11,700 |
| **TOTAL** | **16,216,200** | | | |

### Canon city populations (island-balanced, 2% rate)

| Rank | City | Subnet | **Humans** | **Total** | Status |
|------|------|--------|-----------|-----------|--------|
| 1 | **Janbogo** | Janbogo | 1,050,638 | **2,163,829** | |
| 2 | **Esperanza** | Palmer | 1,039,659 | **2,129,157** | |
| 3 | Zukelli | Janbogo | 849,869 | **1,732,384** | *(destroyed)* |
| 4 | Casey | Mirny | 738,418 | **1,505,155** | |
| 5 | Cape Adare | Janbogo | 730,539 | **1,488,846** | |
| 6 | Mawson | Mawson | 713,748 | **1,454,926** | |
| 7 | Halley | Halley | 711,583 | **1,456,098** | |
| 8 | Mirny | Mirny | 668,613 | **1,356,934** | |
| 9 | Zhongshan | Mawson | 634,485 | **1,284,494** | |
| 10 | Neumayer | Halley | 616,805 | **1,258,342** | |
| 11 | Bharati_TBD | Mawson | 578,925 | **1,183,333** | |
| 12 | Davis | Mawson | 567,640 | **1,166,618** | |
| 13 | Princess Elisabeth | Halley | 556,576 | **1,143,687** | |
| 14 | Belgrano | Halley | 536,403 | **1,080,914** | *(ruins, DLC 5)* |
| 15 | Soyuz | Mawson | 521,255 | **1,073,601** | *(destroyed)* |
| 16 | Aboa | Halley | 508,243 | **1,042,458** | |
| 17 | Maitri_TBD | Halley | 485,482 | **976,095** | |
| 18 | Troll | Halley | 478,489 | **960,002** | |
| 19 | Framheim | Byrd | 430,488 | **884,682** | |
| 20 | Little America | Byrd | 425,052 | **862,581** | |
| 21 | Sejong | Palmer | 318,175 | **647,855** | *(island cap)* |
| 22 | Marambio | Palmer | 284,047 | **571,487** | *(island cap)* |
| 23 | Sanay | Halley | 233,539 | **467,600** | |
| 24 | Dumont d'Urville | Janbogo | 225,066 | **456,411** | *(island cap)* |
| 25 | Fort McMurdo | Janbogo | 223,041 | **447,015** | *(island cap)* |
| 26 | Juan Carlos I | Palmer | 191,451 | **390,175** | *(island cap)* |
| 27 | Scott | Janbogo | 190,964 | **388,343** | *(island cap)* |
| 28 | Palmer City | Palmer | 178,633 | **358,322** | *(island cap)* |
| 29 | Rothera | Palmer | 154,489 | **318,955** | *(island cap)* |
| 30 | Sayowa | Mawson | 123,656 | **256,100** | *(island cap)* |
| 31 | Signy | Palmer | 93,951 | **190,349** | *(island cap)* |
| 32 | Port Lockroy | Palmer | 63,856 | **129,942** | *(island cap)* |
| 33 | **Amundsen Station** | Amundsen | 1,126 | **6,889** | *~84% robot; see note* |
| — | **TOTAL** | — | **15,124,904** | **30,833,579** | |

### Canon subnet totals

| Subnet | Humans | Combined |
|--------|--------|----------|
| Halley / Queen Maud Land | 4,127,120 | 8,385,196 |
| Janbogo / Ross Sea | 3,270,117 | 6,676,828 |
| Mawson / Indian Ocean | 3,139,709 | 6,419,072 |
| Palmer / Antarctic Peninsula | 2,324,261 | 4,736,242 |
| Mirny / Wilkes Land | 1,407,031 | 2,862,089 |
| Byrd / Ross Ice Shelf | 855,540 | 1,747,263 |
| Amundsen / South Pole | 1,126 | 6,889 |
| **TOTAL** | **15,124,904** | **30,833,579** |

*Amundsen Station: pre-war human population reduced to 0.2% of computed figure; robot population reduced to 1%. The South Pole was always an extreme-environment research-and-automation outpost, not a residential city — a skeleton crew of humans embedded in a robot-majority operational facility. No overflow redistributed.*

*All other cities: human populations received an independent random reduction of 1–5% (modeling variation in actual arrival and survival rates vs. the theoretical composite). Robot populations were not adjusted.*

---

## Explanatory Summary: Full Methodology and Reasoning

### What this document is

This file is the pre-Long Night War census for the Tepenian Federation, expressed in terms of where everyone came from. It is both a population registry and a cultural origin map. Every number in the city tables above was derived from a layered chain of logic, not chosen arbitrarily or filled in by feel. This section explains that chain in full — the assumptions, the tools used to operationalize them, the adjustments applied along the way, and the narrative meaning of the final results.

---

### Why Antarctica, and who came

The Tepenian Federation is a refuge state built on a continent no one wanted. The Falkland Treaty established Antarctic exile as the sanctioned fate for humans who chose to maintain intimate relationships with their robots — or who could not be separated from them by any other means the governing powers were willing to apply. This was not a death sentence. It was removal.

The people who came were therefore not refugees fleeing poverty or war in the conventional sense. They were, overwhelmingly, people who had enough — enough money to own a robot in the first place, and enough attachment to that robot to accept exile rather than surrender it. This is the foundational filter that shaped the entire demography of Tepenia: **only those who could afford robots and loved them enough to leave everything else are here.**

This means the exile population skews heavily toward the globally wealthy and the globally middle class. The world's poorest billions are almost entirely absent, not because they were excluded by policy, but because they never owned robots to begin with. Antarctica is, paradoxically, one of the wealthiest populations per capita in the world — because it filtered out the bottom.

---

### The three factors, and why each one matters

Every nation's presence in every city was determined by three factors combined.

**Factor 1: Geographic proximity.** Antarctica is hard to reach. The further away a nation is, the more it costs to make the journey, the longer the voyage, and the more dangerous the crossing — especially in the early exile period before Tepenia had established reliable infrastructure. Southern Hemisphere nations have a structural, permanent advantage: Argentina, Chile, South Africa, Australia, and New Zealand are simply closer. This does not mean distant nations are absent; China and the United States dominate most of the census despite being far away, because their sheer scale overwhelms the proximity penalty. But proximity matters at the margins, and it matters enormously for determining *which city* a given nationality tends to land at. The Antarctic Peninsula receives disproportionate South American traffic. The Indian Ocean sector receives Australian and East Asian traffic. The Ross Sea sector is where the Pacific routes converge.

**Factor 2: Raw population.** A nation of 1.4 billion people will produce more exiles than a nation of 5 million, all else being equal. China's dominance in the census is not a policy choice or a lore preference — it is arithmetic. More people means more robot owners, which means more potential exiles. Small nations (Uruguay, the Baltic states, Slovenia) appear in the census at all only because the Gini-adjusted calculation preserves their contribution even at small absolute scale.

**Factor 3: GDP per capita with Gini inequality correction.** This is the most important factor for understanding why the census looks the way it does, and why many large nations are underrepresented relative to their raw population. The underlying question is: what fraction of a nation's population could realistically have owned a robot? Robot ownership was expensive. It was not a luxury for the ultra-rich only, but it was firmly in the upper-middle-class tier and above. GDP per capita is the best available proxy for what fraction of a nation's population lives in that range. A nation with high GDP per capita will have a higher robot-ownership fraction than a low-GDP nation of the same size.

But GDP per capita alone is misleading for high-inequality nations. A country where the top 5% holds 90% of the wealth looks "rich" by GDP per capita but has a tiny actual middle class. The Gini coefficient measures this inequality. A Gini of 0.20 means wealth is spread very evenly; a Gini of 0.60 means it is extremely concentrated. For every nation, a Gini penalty was applied that reduces the robot-eligible fraction proportionally to inequality.

The combined result is the **Gini-adjusted effective population**: the approximate number of people in each nation who had meaningful robot access. This number, not raw population, is what determines tier placement and exile allocation.

---

### Why some large nations are smaller in the census than you'd expect

**South Africa** is the clearest example of the Gini correction at work. South Africa has a population of roughly 60 million — larger than most European nations included here. But its Gini coefficient is approximately 0.63, among the highest in the world, reflecting one of the most extreme wealth concentrations on the planet. After the Gini penalty, South Africa's effective robot-eligible population drops to roughly 3 million. It appears in the census as a T3 nation at most cities, and is T2 only where proximity advantages survive the correction (specifically the QML subnet, closest to the Cape route).

**Brazil** follows the same pattern. Raw population of ~215 million makes it look like it should be a major player. But Brazil's Gini (~0.53) and its relatively modest GDP per capita combine to reduce the effective pool to approximately 17 million — comparable to Indonesia and significantly less than Germany despite a population nine times Germany's size.

**Mexico** is a similar case. 128 million raw population, but a Gini of ~0.45 and GDP per capita in the mid tier produces an effective pool of ~18 million. Mexico is present at Peninsula cities as T2 — it qualifies, but it is never dominant.

**Russia** has moderate GDP per capita and high inequality (Gini ~0.37), reducing its effective pool from a large raw number to approximately 25 million — respectable, but placed behind Italy and South Korea despite Russia's larger raw population.

Conversely, nations like **Germany** and **Japan** punch well above their raw population weight. Germany's Gini is very low (~0.29), meaning wealth is distributed broadly, meaning a very high fraction of Germans lived in the robot-ownership tier. Japan is similar. These nations have effective pools much closer to their raw populations than high-Gini nations of similar size.

The **Czech Republic, Slovakia, and Estonia** show this effect at the small end: tiny nations, but such low Gini coefficients that they achieve among the highest per-capita effective conversion rates in the entire census. Every Czech, Slovak, or Estonian who was robot-eligible is in this census.

---

### Why certain regions are absent

**The Indian subcontinent (India, Pakistan, Bangladesh, Sri Lanka)** is absent from the Tepenian census entirely. This is established canon, not a calculation result. No one from the subcontinent came to Tepenia. The in-world reason for this is TBD in the lore, but the canon fact is fixed: the Maitri and Bharati stations (Indian-founded in the real world) have non-Indian founding populations in the Tepenian timeline.

**The rest of Africa** is absent for calculated reasons. Sub-Saharan Africa generally has low GDP per capita combined with moderate-to-high Gini coefficients, producing near-zero effective robot-eligible populations at current historical tech levels. The continent's wealth is concentrated far too narrowly to generate meaningful exile numbers. South Africa is the sole African inclusion precisely because it clears the floor threshold — barely, and after heavy Gini penalty — while its geographic proximity to the Peninsula gives it marginal access that makes the effective contribution worth tracking.

**The Middle East** is absent on similar grounds. Oil wealth in the Gulf states is extremely concentrated — family dynasties and sovereign funds, not a broad middle class. Egypt and the Levant have moderate populations but low-to-moderate GDP per capita with meaningful Gini penalties. None clear the effective-population threshold that would make them visible in city compositions.

**Most of Southeast Asia** is absent. The region's inclusion is limited to Thailand, Vietnam, the Philippines, and Malaysia — the four nations whose combination of population size and GDP/Gini profile generates enough effective exile-eligible people to matter. Indonesia is the outlier: it appears in the census despite lower GDP per capita because its raw population (~275 million) is large enough to preserve a meaningful effective number even after penalty. The rest of SEA (Myanmar, Cambodia, Laos, etc.) do not clear the threshold.

**Latin America below Mexico** produces only Argentina, Brazil, Chile, and Uruguay. Argentina and Chile are proximity nations for the Peninsula; without geographic advantage, their effective populations would be too small to justify T2 placement. Uruguay has the smallest effective population of any nation in the census (~0.6M) and appears only at the nearest Peninsula cities.

---

### How the solar time zone window works

Not every nation can practically reach every city. Antarctic logistics in the early exile period depend heavily on existing shipping and air routes, which cluster by hemisphere and longitude. The heuristic used here is the **±3 solar time zone window**: a nation's exiles can realistically reach any city within three solar time zones of their home longitude. Beyond that, routes become so indirect and costly that the nation's presence effectively disappears.

This is why the **Intermarium/Intermaria bloc** — Eastern European nations centered on Poland — appears at QML/Halley cities but not at the deep Indian Ocean or Ross Sea cities. Poland sits at UTC+1. It can reach cities in the range UTC-2 through UTC+4. Halley (UTC-2) is exactly at the edge; Mawson (UTC+4) is at the other edge. The Ross Sea cities (UTC+11) are distance 10 — entirely unreachable.

This is also why **Thailand and Vietnam** (UTC+7) appear at Mawson (UTC+4, distance 3) and Davis/Mirny/Casey (UTC+5–7) but not at Peninsula cities (UTC-4 through UTC-2, distance 9–11). And why **Philippines and Malaysia** (UTC+8) extend one step further toward the Ross Sea, reaching Janbogo/Zukelli/Cape Adare (UTC+11, distance 3) and DdU (UTC+9, distance 1) but nothing in the Pacific or Atlantic quadrants.

The time zone window is a proxy for logistics, not a hard physical limit. It is intended to be directionally correct, not technically precise. The point is that immigration flows followed existing routes, and routes cluster by longitude.

---

### The tier system: what it means and how tiers are formed

Within each city's composition, all qualifying nations are ranked together by Gini-adjusted effective population. Tier breaks are placed at the largest ratio gaps in that city's specific ranking — not at fixed thresholds. This means tier membership can shift between cities. A nation that is T1 at one city might be T2 at another city where larger nations also qualify.

Once tiers are established, city allocation is distributed as follows: **T1 receives 8 shares, T2 receives 3 shares, T3 receives 1 share** per nation in that tier. This is the mechanism that makes T1 nations disproportionately dominant — not just "the biggest," but structurally ensured a much larger slice of the city's immigration flow.

This tier system creates the cultural layering visible in city designs: the T1 nation(s) shape the city's primary identity, language dominance, naming conventions, and faction character. T2 nations are distinct visible communities that contribute to the city's multicultural texture without defining it. T3 nations are present — you'd recognize them in the city if you looked — but they do not determine who the city fundamentally *is*.

The founding wave (who arrived first, due to proximity advantages) can differ from the long-run T1 composition (who arrived in largest numbers over time). This tension — founding character vs. population majority — is deliberately preserved in city designs. A city might feel culturally Argentinian in its architecture and earliest customs while being statistically Chinese and American in population.

---

### The exile rate: 2% of the effective population

The fraction of each nation's Gini-adjusted effective population that actually became Tepenian exiles is **2%**. This is the governing assumption for the entire census. Two percent of everyone who realistically could have owned a robot chose — or was forced — to accept exile rather than part with theirs.

This fraction is deliberately modest. The exile events were disruptive but not total. Most robot-eligible people found ways to comply with separation mandates, pay fines, enter programs, or otherwise avoid going to Antarctica. The exiles are the ones who couldn't do that — either because their attachment was too deep, because their robot refused separation, or because they were caught in a political context where compliance wasn't an option.

Two percent of the Gini-adjusted global effective pool produces approximately **16.2 million human exiles**. This was previously calculated at 3% (~24.95 million), but was revised down to 2% (×0.65 applied globally to all prior figures) for a more conservative and narratively grounded estimate. The 2% figure also produces a pre-war Tepenian population that feels geopolitically meaningful without being implausible: a mid-sized nation-state, not a superpower.

---

### Island population balancing: why Sejong isn't the largest city

The raw census calculation — pure math applied to the tier system with no geographic constraints — produced some physically absurd results. The most obvious was **Sejong**, on King George Island in the South Shetlands. Sejong occupies one of the most geographically diverse and internationally prominent sites in the early Antarctic settlement period (closest significant Antarctic base to South America; surrounded by multinational station infrastructure). The math put Sejong near the top of the city hierarchy.

The problem is that King George Island is approximately 1,300 km². Much of it is glaciated. The ice-free habitable area is a small fraction of that. Even with sci-fi vertical construction, multi-layer arcology design, and underground expansion, King George Island physically cannot support a million-person city. It would be overcrowded beyond any architectural justification.

Eleven cities were identified as sitting on actual islands with binding physical capacity constraints. Each was assigned a realistic cap based on island size, ice coverage estimate, and a generous sci-fi multiplier for vertical and subsurface construction:

- **Port Lockroy** (Goudier Island, ~0.016 km² ice-free): capped at 65,000 combined (~100,000 pre-×0.65 scaling)
- **Signy** (Signy Island, ~19 km² largely ice-free): capped at 195,000 combined
- **Sayowa** (East Ongul Island, ~28 km²): capped at 260,000 combined
- **Rothera** (Adelaide Island, ~4,463 km² but mostly glaciated): capped at 325,000 combined
- **Palmer City** (Anvers Island, largely glaciated): capped at 364,000 combined
- **Juan Carlos I** (Livingston Island): capped at 390,000 combined
- **Scott** (Pram Point, Ross Island): capped at 390,000 combined
- **Fort McMurdo** (Ross Island): capped at 455,000 combined
- **Dumont d'Urville** (Île des Pétrels, ~0.3 km²): capped at 455,000 combined
- **Marambio** (Seymour Island, ~133 km²): capped at 585,000 combined
- **Sejong** (King George Island, ~1,300 km²): capped at 650,000 combined

The overflow from these caps — roughly 5.24 million humans at the 3% rate — was redistributed to mainland coastal and ice-shelf cities within ±3 time zones. Interior cities (Troll, Aboa, Sanay, Princess Elisabeth, Amundsen) were excluded as redistribution targets because inland infrastructure cannot absorb mass population without independent logistical support that isn't assumed in this model. Other islands also cannot receive overflow.

The practical effect of this redistribution was dramatic. **Esperanza** — the only city on the actual Antarctic mainland Peninsula coast — absorbed 50% of all Peninsula island overflow and grew from a modest ~363,000 to over a million humans, becoming the dominant Peninsula city. **Janbogo**, on the Terra Nova Bay mainland coast, absorbed the combined overflow from the Ross Sea islands and from Dumont d'Urville, growing to become the single largest city in all of Tepenia.

---

### Amundsen Station: a different kind of city

Amundsen Station at the geographic South Pole is not a city in any conventional sense. It has no harbor, no trade routes, no immigrant flow by sea or road. Everything that reaches the South Pole must either be flown in or conveyed overland by tracked vehicle across one of the most hostile environments on Earth.

The composite formula, applied naively, would put significant population at Amundsen because it is accessible (in principle) from all time zones equally — there is no solar time zone at the pole. But this masks the real operational reality: the Pole is a research outpost. It always has been. Even in the sci-fi future of Inner Tepenia, the South Pole is where you send robots to run automated scientific infrastructure with minimal human oversight, not where humans choose to build communities.

Amundsen Station's human population was therefore reduced to **0.2% of the computed figure** (producing ~1,126 humans) and its robot population to **1% of the computed figure** (producing ~5,763 robots), for a total of ~6,889. The ~84% robot composition reflects the outpost's operational reality: it exists to do work that robots are better suited for. The humans present are a skeleton crew of specialists — scientists, engineers, command personnel — embedded in a facility that runs primarily on automated systems.

---

### The random variation passes: final calibration

After all the above — the three-factor composite, the 2% exile rate, the island capacity caps, and the Amundsen reduction — two final randomization passes were applied.

**First pass (humans, ±1–5% per city, always downward):** Each city's human population was reduced by a randomly generated percentage between 1.00% and 5.00%. This models the gap between the theoretical composite (what the math says *should* have happened) and what actually happened. Real migration is not a clean optimization problem. Ships were lost. People died in transit or in the brutal early settlement period. Some planned to come but never did. Some arrived, hated it, and found ways back. The 1–5% reduction is not a correction to the formula — the formula is deliberately assumed correct at the population scale — it is noise introduced to give each city a non-round, non-symmetric population that feels observed rather than calculated.

**Second pass (robots, ±1–2% per city, direction randomly up or down):** Each city's robot population was adjusted by a randomly generated percentage between 1.00% and 2.00%, in either direction. Robot populations are less subject to the organic variation that affects human populations (robots don't die of exposure, they don't turn back at the port), but they are subject to production and deployment variation: some cities received more units than planned, some fewer; some robots were diverted mid-route; some arrived but were reassigned. The ±1–2% range is narrower than the human pass, reflecting that robotic logistics are more controllable than human migration — but not perfectly so.

These two passes are the last step. They do not change the analytical meaning of the census; they add texture to it.

---

### The final numbers and what they mean

**Pre-Long Night War Tepenian Federation census:**

| | Count |
|--|--|
| Humans | ~15,124,904 |
| Robots | ~15,708,675 |
| **Combined** | **~30,833,579** |

Approximately 30.8 million people — human and robot — lived in Tepenia before the Long Night War. For scale, this is a mid-sized nation-state: comparable to Peru, Venezuela, or Malaysia. It is not a superpower. It is a community.

Of that combined population, two cities no longer exist. **Zukelli** (~1,732,000 combined pre-war) and **Soyuz** (~1,073,000 combined pre-war) were destroyed in the Long Night War. Together they represent approximately 2.8 million people — a city the size of Chicago — annihilated. **Belgrano** survives as ruins by the time of Inner Tepenia's events (it is the setting for DLC 5). Its pre-war population was ~1,080,000 combined.

The three lost or ruined cities total approximately 3.9 million combined — roughly 12.5% of the entire pre-war Tepenian population.

The largest surviving city is **Esperanza**, at approximately 2.1 million combined (humans + robots). The largest city overall by pre-war population was **Janbogo**, at approximately 2.16 million — and Janbogo survived the war, making it the dominant metropolitan center in post-war Tepenia.

**By subnet**, the Halley/Queen Maud Land network was the most populous at ~8.39 million combined — nearly 27% of the entire Tepenian population lived in the QML arc. This makes the destruction of Belgrano, one of QML's major cities, particularly significant: the ruins are not the ruins of a forgotten backwater but of a once-substantial city in the federation's most densely settled region.

The demographic character of Tepenia is, in aggregate, heavily shaped by **China and the USA** — the two nations whose Gini-adjusted effective populations dwarf all others. At most cities, these two nations are T1 co-primaries or near-primaries. Japan, Germany, France, the UK, and South Korea form the consistent upper-T2 layer. The Intermarium bloc — individually small, collectively significant — provides a distinctive Eastern European presence concentrated in the QML arc. Southeast Asia (Thailand, Vietnam, Philippines, Malaysia) provides the Indo-Pacific texture of the Mawson and Ross Sea subnets.

The result is a population that is statistically global but skewed sharply toward the wealthy, the educated, and the emotionally committed — the specific subset of humanity that decided their robots were worth a continent.

---

## Canon Census II — After Space Colonization (Orbital Era)

**Context:** Tepenia did not remain a purely Antarctic civilization. Roughly one-third of the way through Tepenia's existence as a country, construction began on **Amundsen Tower** — the space elevator anchored at the geographic South Pole, exploiting the rotational axis as the optimal anchor point for a permanent surface-to-orbit tether. By approximately the halfway point of Tepenia's pre-war history, Amundsen Tower was operational and low-earth orbital construction was underway.

The first orbital structure was a robot-exclusive station — a staging platform built entirely by robotic labor, requiring no human life-support infrastructure. From that station, robots began construction on the first **Von Braun Wheel**, a rotating habitat designed for both robots and humans. Once the Wheel was complete, Tepenians began departing the Antarctic surface in substantial numbers: taking work contracts, establishing permanent residences, building the infrastructure that would eventually form the backbone of Tepenian space civilization.

By the time the Long Night War began, a significant fraction of the Tepenian population was living or working in low-earth orbit — which is why the war's early mass-evacuation via Amundsen Tower was logistically viable. There was somewhere to go because they had already spent generations building it.

This census captures the **snapshot immediately before the Long Night War**, after decades of orbital migration had already redistributed a meaningful portion of the population off-surface.

**Methodology:** Each city's "After" population was calculated by applying two independent randomly-generated retention rates (one for humans, one for robots) between 55% and 85% of the city's "Before" population. The gap — everyone who left — is the orbital migration pool. Population is conserved: Before total = After Antarctic total + Orbital total.

---

### After census: city populations (Orbital Era, pre-Long Night War)

| Rank | City | Subnet | **Humans** | **Total** | Status |
|------|------|--------|-----------|-----------|--------|
| 1 | **Janbogo** | Janbogo | 817,606 | **1,595,949** | |
| 2 | **Zukelli** | Janbogo | 616,325 | **1,302,304** | *(destroyed in Long Night War)* |
| 3 | Esperanza | Palmer | 591,358 | **1,385,929** | |
| 4 | Zhongshan | Mawson | 522,372 | **996,684** | |
| 5 | Halley | Halley | 509,209 | **1,088,069** | |
| 6 | Mirny | Mirny | 507,344 | **1,016,495** | |
| 7 | Soyuz | Mawson | 437,854 | **888,292** | *(destroyed in Long Night War)* |
| 8 | Davis | Mawson | 437,423 | **781,596** | |
| 9 | Casey | Mirny | 436,922 | **1,042,031** | |
| 10 | Belgrano | Halley | 429,820 | **837,768** | *(ruined in Long Night War; DLC 5)* |
| 11 | Mawson | Mawson | 427,321 | **952,446** | |
| 12 | Cape Adare | Janbogo | 426,343 | **1,050,051** | |
| 13 | Princess Elisabeth | Halley | 401,403 | **766,762** | |
| 14 | Neumayer | Halley | 385,071 | **830,747** | |
| 15 | Bharati_TBD | Mawson | 336,124 | **728,324** | |
| 16 | Troll | Halley | 323,650 | **671,832** | |
| 17 | Aboa | Halley | 310,791 | **607,441** | |
| 18 | Little America | Byrd | 304,422 | **555,739** | |
| 19 | Maitri_TBD | Halley | 272,889 | **593,063** | |
| 20 | Framheim | Byrd | 248,865 | **604,953** | |
| 21 | Sejong | Palmer | 234,304 | **514,070** | *(island cap)* |
| 22 | Marambio | Palmer | 195,623 | **430,145** | *(island cap)* |
| 23 | Fort McMurdo | Janbogo | 173,548 | **338,169** | *(island cap)* |
| 24 | Scott | Janbogo | 153,382 | **313,634** | *(island cap)* |
| 25 | Sanay | Halley | 145,798 | **275,117** | |
| 26 | Palmer City | Palmer | 135,457 | **249,020** | *(island cap)* |
| 27 | Dumont d'Urville | Janbogo | 134,634 | **312,006** | *(island cap)* |
| 28 | Rothera | Palmer | 121,784 | **255,857** | *(island cap)* |
| 29 | Juan Carlos I | Palmer | 118,910 | **246,372** | *(island cap)* |
| 30 | Sayowa | Mawson | 85,199 | **164,957** | *(island cap)* |
| 31 | Signy | Palmer | 53,928 | **133,755** | *(island cap)* |
| 32 | Port Lockroy | Palmer | 53,703 | **95,906** | *(island cap)* |
| 33 | Amundsen Station | Amundsen | 913 | **4,891** | *~81% robot; skeleton crew* |
| — | **TOTAL (Antarctic)** | — | **10,350,295** | **21,630,374** | |

### After census: subnet totals (Antarctic surface only)

| Subnet | Humans | Combined |
|--------|--------|----------|
| Halley / Queen Maud Land | 2,778,631 | 5,670,799 |
| Janbogo / Ross Sea | 2,321,838 | 4,912,113 |
| Mawson / Indian Ocean | 2,246,293 | 4,512,299 |
| Palmer / Antarctic Peninsula | 1,505,067 | 3,311,054 |
| Mirny / Wilkes Land | 944,266 | 2,058,526 |
| Byrd / Ross Ice Shelf | 553,287 | 1,160,692 |
| Amundsen / South Pole | 913 | 4,891 |
| **TOTAL (Antarctic)** | **10,350,295** | **21,630,374** |

### Orbital population (Von Braun Wheel + associated infrastructure)

| | Count |
|--|--|
| Humans in orbit | 4,774,609 |
| Robots in orbit | 4,428,596 |
| **Combined orbital** | **9,203,205** |

*Approximately 9.2 million Tepenians — nearly 30% of the total pre-war population — were living or working in low-earth orbit at the time the Long Night War began. This is the population that was not at risk of ground-level destruction, and the population that the mass Amundsen Tower evacuations during the war were attempting to reach.*

### Full Tepenian census: After (combined Antarctic + Orbital)

| | Antarctic | Orbital | **Grand Total** |
|--|-----------|---------|----------------|
| Humans | 10,350,295 | 4,774,609 | **15,124,904** |
| Robots | 11,280,079 | 4,428,596 | **15,708,675** |
| **Combined** | **21,630,374** | **9,203,205** | **30,833,579** |

*Population is conserved: the Before and After grand totals are identical. Nobody was born or died in the transition — they moved.*

### Design notes

**Zukelli at rank 2 in the After census** is a narrative artifact of the random retention rolls: Zukelli's population happened to hold well (72.5% of humans, 77.7% of robots stayed) right up to its destruction. This means Zukelli was still a large, thriving, densely inhabited city when the Long Night War hit it. Its destruction was not the end of a fading place — it was the killing of a city near its peak.

**Esperanza drops from #2 to #3** in the After ranking, overtaken by Zukelli due to Esperanza's lower human retention (56.9%). This likely reflects the Peninsula's generally strong orbital migration draw — perhaps because the Peninsula subnet's proximity to Amundsen Tower (via the inter-subnet rail system) made orbital access easier, incentivizing earlier and larger departure.

**The orbital population (~9.2M combined) is approximately 30% of the total Tepenian population** at the time of the war. This is a large fraction — enough to sustain a functional civilization in orbit with full industrial, scientific, and social infrastructure. It explains why the orbital remnant after the Long Night War is a going concern rather than a stranded handful of survivors.

**The human-robot split in orbit** (4.77M humans vs. 4.43M robots) is slightly human-heavy relative to the Antarctic split — reflecting that orbital habitats were designed for human habitation from the Von Braun Wheel stage onward, and that the early robot-only station had long since been absorbed into the broader orbital infrastructure by the war's onset.
