# Results, Part 2: Russia, Italy, Germany, Argentina and North America (2026-11-01, ~22:00)

**Scratch results, not canon.** Asked for by the developer at ~21:45: *"after the Sinian Federation (and
surrounding lands) are done, see about calculating for Russia, Italy, Germany, Argentina, and the nations of North
America."* Figures below the Russia section come from `calc_part2.py` reading `05_part2_unit_data.csv`; sources are in
`01_Research_Log.md` Part 2. Nothing in the census, specs, composition file or datasheets has been changed.

**Borders** come from the author's world atlas
(`/home/kuroskalacs/Documents/Doll-Fi/media/y-files/Map Files/x Full Earth/z-full-world-atlas/`: `data/world/numbering.csv`
notes, the region READMEs, the Latin America `nations-assignment.csv`, and the Europe build's region list). Each region
there is drawn in its **final state** (Europe map C-15; North America's eighth round, 2026-09-26; Latin America's
2026-09-28 assignment). Whether those final states are the borders of the exile era is a question for the developer.

**Effective pools** are the composition file's (`Upper_Earth_Immigration_Composition.md` L68–L86): USA ~155M, Germany
~46M, Italy ~27M, Russia ~25M, Canada ~20M, Mexico ~18M, Argentina ~6M. Option A splits a pool by headcount, Option B
by economic size (GDP); every piece keeps its source country's one inequality adjustment.

## Russia: already done on 2026-10-29 (summarized, not redone)

`Research_Logs/Russia_Split_Proportions_RS1b_Input_Table_2026-10-29.md` worked out every successor's population, pool
and zone profile under every variant (sections 6–7). Below is its primary variant (pre-war territory, Kaliningrad left
out, the INIT Karelia), turned into millions of the ~25M pool (DERIVED: 25M × its percentages). Its pool formula is
population × GRP per head × (1 − Gini), i.e. Option B with each region's own inequality. Its "P only" row (§7.2) is
Option A.

| Successor | Option A share (headcount) | Option A pool | Option B share (RS1b primary) | Option B pool |
|---|--:|--:|--:|--:|
| Russia (core; this variant leaves out the eastern-Ukraine slice, which was pre-war Ukraine's) | 31.36% | 7.84M | 41.83% | 10.46M |
| Idelsk-Uralia | 30.90% | 7.72M | 23.41% | 5.85M |
| Siberia | 12.47% | 3.12M | 16.90% | 4.22M |
| Künnarantaiga | 7.20% | 1.80M | 8.24% | 2.06M |
| Donska-Kubania | 11.95% | 2.99M | 7.12% | 1.78M |
| Karelia | 0.84% | 0.21M | 0.97% | 0.24M |
| Dagestan | 2.21% | 0.55M | 0.61% | 0.15M |
| Chechnya | 1.05% | 0.26M | 0.29% | 0.07M |
| Kabardino-Balkaria | 0.63% | 0.16M | 0.20% | 0.05M |
| North Ossetia-Alania | 0.48% | 0.12M | 0.19% | 0.05M |
| Karachay-Cherkessia | 0.33% | 0.08M | 0.10% | 0.03M |
| Tuva | 0.23% | 0.06M | 0.08% | 0.02M |
| Ingushetia | 0.35% | 0.09M | 0.06% | 0.01M |

The Russia rulings it waits on are unchanged (`Population_Work_Prep_2026-11-02.md` item 2): the meaningful-share
threshold, solar or official time zones, pool split or window split, Kaliningrad in or out, which Karelia, and whether
a split Russia keeps its share at Byrd, Palmer City and Contrapunto. RS1b's own finding: no scope variant moves any
successor by more than 5 points; only dropping income altogether (Option A) does.

## Checks

- **USA:** units sum to 341,785,457 people; published total 341,784,857 (July 1 2025 estimate, 50 states + DC (U1); 2025 GDP, million USD (U2)); difference 600; GDP units sum to 30,594,279 against 30,762,099 (difference -167,820)
- **Canada:** units sum to 41,608,982 people; published total 41,608,982 (July 1 2025, Table 17-10-0005-01 (C1)); difference 0
- **Mexico:** units sum to 126,014,024 people
- **Italy:** units sum to 58,942,828 people; published total 58,942,828 (1 Jan 2026 estimate (I1)); difference 0
- **Germany:** units sum to 83,580,000 people
- **Argentina:** units sum to 46,044,573 people; published total 46,044,573 (2022 census, without Argentine Antarctica (A1)); difference 0

## USA (effective pool ~155M)

| Successor | Present-day units | Population | Share of people | Share of GDP | GDP per person vs the country | Option A: by headcount | Option B: by economic size |
|---|---|--:|--:|--:|--:|--:|--:|
| The CSA | Alabama, Arkansas, Florida, Georgia, Louisiana, Mississippi, North Carolina, Oklahoma, South Carolina, Tennessee, Texas | 110,562,521 | 32.35% | 28.91% | 0.89x | 50.14M | 44.81M |
| Appalachia | Delaware, District of Columbia, Illinois, Indiana, Kentucky, Maryland, Michigan, Ohio, Virginia, West Virginia, Wisconsin | 70,965,717 | 20.76% | 19.64% | 0.95x | 32.18M | 30.45M |
| New England | Connecticut, Maine, Massachusetts, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont | 58,042,054 | 16.98% | 19.51% | 1.15x | 26.32M | 30.24M |
| The People's Democratic Republic of Cascadia | Alaska Panhandle (Southeast region), California, Oregon, Washington | 51,700,008 | 15.13% | 17.96% | 1.19x | 23.45M | 27.84M |
| The Midwest Republic | Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota | 22,069,011 | 6.46% | 6.14% | 0.95x | 10.01M | 9.52M |
| Colorado | Colorado, Idaho, Montana, Nevada, Utah, Wyoming | 16,596,833 | 4.86% | 4.75% | 0.98x | 7.53M | 7.36M |
| La República de Sonora | Arizona, New Mexico | 9,749,316 | 2.85% | 2.45% | 0.86x | 4.42M | 3.80M |
| The Sovereign Republic of Hawaii | Hawaii | 1,432,820 | 0.42% | 0.41% | 0.97x | 0.65M | 0.63M |
| Alaska | Alaska (minus the Panhandle) | 667,177 | 0.20% | 0.22% | 1.14x | 0.30M | 0.34M |

## Canada (effective pool ~20M)

| Successor | Present-day units | Population | Share of people | Share of GDP | GDP per person vs the country | Option A: by headcount | Option B: by economic size |
|---|---|--:|--:|--:|--:|--:|--:|
| Demilitarized Zone | Ontario south of the cut line | 15,370,290 | 36.94% | 36.51% | 0.99x | 7.39M | 7.30M |
| Quebec | Newfoundland and Labrador, Prince Edward Island, Nova Scotia, New Brunswick, Quebec | 11,752,686 | 28.25% | 25.21% | 0.89x | 5.65M | 5.04M |
| The Prairie Federation | Ontario north of the cut line (incl. Manitoulin), Manitoba, Saskatchewan, Alberta | 8,646,173 | 20.78% | 23.99% | 1.15x | 4.16M | 4.80M |
| The People's Democratic Republic of Cascadia | British Columbia | 5,702,544 | 13.71% | 13.81% | 1.01x | 2.74M | 2.76M |
| Alaska | Yukon, Northwest Territories, Nunavut (mainland and Hudson Bay part) | 117,349 | 0.28% | 0.40% | 1.42x | 0.06M | 0.08M |
| Neutral Scientific Territory | Nunavut (Baffin Island and satellites) | 19,567 | 0.05% | 0.08% | 1.80x | 0.01M | 0.02M |
| Greenland | Nunavut (Queen Elizabeth Islands) | 374 | 0.00% | 0.00% | 1.80x | 0.00M | 0.00M |

## Mexico (effective pool ~18M)

| Successor | Present-day units | Population | Share of people | Share of GDP | GDP per person vs the country | Option A: by headcount | Option B: by economic size |
|---|---|--:|--:|--:|--:|--:|--:|
| México | The other 23 entities | 101,706,176 | 80.71% | 79.71% | 0.99x | 14.53M | 14.35M |
| La República de Yucatán | Campeche, Chiapas, Quintana Roo, Tabasco, Yucatán | 13,053,672 | 10.36% | 8.90% | 0.86x | 1.86M | 1.60M |
| La República de Sonora | Sonora, Chihuahua | 6,686,709 | 5.31% | 6.91% | 1.30x | 0.96M | 1.24M |
| The People's Democratic Republic of Cascadia | Baja California, Baja California Sur | 4,567,467 | 3.62% | 4.48% | 1.24x | 0.65M | 0.81M |

## Italy (effective pool ~27M)

| Successor | Present-day units | Population | Share of people | Share of GDP | GDP per person vs the country | Option A: by headcount | Option B: by economic size |
|---|---|--:|--:|--:|--:|--:|--:|
| Magna Lombardia | Piemonte, Valle d'Aosta, Liguria, Lombardia, Trentino-Alto Adige, Veneto, Friuli-Venezia Giulia, Emilia-Romagna, Toscana, Umbria, Marche | 33,563,706 | 56.94% | 66.70% | 1.17x | 15.37M | 18.01M |
| Meridia | Lazio, Abruzzo, Molise, Campania, Puglia, Basilicata, Calabria, Sardegna | 20,603,928 | 34.96% | 28.16% | 0.81x | 9.44M | 7.60M |
| Sicilia (autonomous zone within Meridia) | Sicilia | 4,775,194 | 8.10% | 5.14% | 0.63x | 2.19M | 1.39M |

## Germany (effective pool ~46M)

| Successor | Present-day units | Population | Share of people | Share of GDP | GDP per person vs the country | Option A: by headcount | Option B: by economic size |
|---|---|--:|--:|--:|--:|--:|--:|
| Germany | Germany without Bavaria | 70,105,000 | 83.88% | 81.71% | 0.97x | 38.58M | 37.59M |
| Austro-Bavaria | Bavaria | 13,475,000 | 16.12% | 18.29% | 1.13x | 7.42M | 8.41M |

## Argentina (effective pool ~6M)

| Successor | Present-day units | Population | Share of people | Share of GDP | GDP per person vs the country | Option A: by headcount | Option B: by economic size |
|---|---|--:|--:|--:|--:|--:|--:|
| Argentina | 19 units (see the CSV) | 43,428,812 | 94.32% | 89.94% | 0.95x | 5.66M | 5.40M |
| Araucanía-Patagonia Autonomous Zone | Chubut, Neuquén, Río Negro, Santa Cruz, Tierra del Fuego | 2,615,761 | 5.68% | 10.06% | 1.77x | 0.34M | 0.60M |

## Every successor, all source countries combined

Successors that draw on more than one present-day country add their pieces' pools together. A successor's pool here counts only the source countries in this part (for example Cascadia's Alaska Panhandle comes from the USA's pool; Austria, Chile and Guatemala's Petén are not in this part).

| Successor | From | Population (present day) | Option A pool | Option B pool |
|---|---|--:|--:|--:|
| The CSA | USA | 110,562,521 | 50.14M | 44.81M |
| Germany | Germany | 70,105,000 | 38.58M | 37.59M |
| The People's Democratic Republic of Cascadia | USA, Canada, Mexico | 61,970,019 | 26.84M | 31.41M |
| Appalachia | USA | 70,965,717 | 32.18M | 30.45M |
| New England | USA | 58,042,054 | 26.32M | 30.24M |
| Magna Lombardia | Italy | 33,563,706 | 15.37M | 18.01M |
| México | Mexico | 101,706,176 | 14.53M | 14.35M |
| The Midwest Republic | USA | 22,069,011 | 10.01M | 9.52M |
| Austro-Bavaria | Germany | 13,475,000 | 7.42M | 8.41M |
| Meridia | Italy | 20,603,928 | 9.44M | 7.60M |
| Colorado | USA | 16,596,833 | 7.53M | 7.36M |
| Demilitarized Zone | Canada | 15,370,290 | 7.39M | 7.30M |
| Argentina | Argentina | 43,428,812 | 5.66M | 5.40M |
| La República de Sonora | USA, Mexico | 16,436,025 | 5.38M | 5.05M |
| Quebec | Canada | 11,752,686 | 5.65M | 5.04M |
| The Prairie Federation | Canada | 8,646,173 | 4.16M | 4.80M |
| La República de Yucatán | Mexico | 13,053,672 | 1.86M | 1.60M |
| Sicilia (autonomous zone within Meridia) | Italy | 4,775,194 | 2.19M | 1.39M |
| The Sovereign Republic of Hawaii | USA | 1,432,820 | 0.65M | 0.63M |
| Araucanía-Patagonia Autonomous Zone | Argentina | 2,615,761 | 0.34M | 0.60M |
| Alaska | USA, Canada | 784,526 | 0.36M | 0.42M |
| Neutral Scientific Territory | Canada | 19,567 | 0.01M | 0.02M |
| Greenland | Canada | 374 | 0.00M | 0.00M |

## What this shows (plain reading)

1. **⚠ The splits work against the multicultural goal unless the developer weighs them deliberately.** China's split
   leaves the Sinian Federation with about 89–92% of China's pool (file `03`). **The USA's split leaves no successor
   above about 32%** (the CSA, 45–50M of 155M), and Russia's largest piece keeps 31–42%. So in a city where China and
   the USA are now close (for example 19% and 22%), replacing both with their successors would leave **the Sinian
   Federation several times larger than any American successor.** Which American successors reach which city depends
   on the time-zone window and the gateways, so this is a per-city matter, but the direction is the same everywhere.
   *(DERIVED from the tables; no city figure has been computed or changed.)*
2. **The USA becomes four large pieces and five small ones.** The CSA (32% of people, 29% of GDP), Appalachia (21%,
   20%), New England (17%, 20%) and Cascadia (15%, 18%) are each between 23M and 50M; the Midwest Republic, Colorado,
   La República de Sonora's American half, Hawaii and Alaska are smaller.
3. **Canada's largest piece is not a nation.** Southern Ontario, the atlas's **Demilitarized Zone**, holds 15.4 million
   people (37% of Canada). Quebec with the Atlantic provinces is 28%, the Prairie Federation 21%, British Columbia
   (Cascadia) 14%.
4. **Cascadia and La República de Sonora draw on several countries.** Cascadia combines California, Oregon, Washington
   and the Alaska Panhandle (USA), British Columbia (Canada) and both Bajas (Mexico): 62 million people today, a pool of
   27–31M. Sonora combines Arizona and New Mexico with Sonora and Chihuahua: 16 million people, a pool of about 5M.
5. **Italy matches the earlier illustration.** By economic size, Magna Lombardia gets 18.0M and Meridia with Sicilia
   9.0M, the same 18 : 9 the Santa Luce ruling's notes gave as an illustration. **Sardinia** is in Meridia in the atlas
   build (every region not on the northern list), but the ruling's ~23.8M Meridia figure was "without Sardinia"; with
   Sardinia, Meridia plus Sicilia is 25.4M people.
6. **Germany barely changes:** Bavaria (to Austro-Bavaria) is 16% of Germany's people and 18% of its GDP, a pool of
   7.4–8.4M. **Austria itself has no row in the composition file**, so whether Austro-Bavaria also draws on Austria is
   a separate question.
7. **Argentina barely changes by headcount (5.7% leaves), but Patagonia is rich:** the five provinces hold 10% of
   Argentina's GDP (Neuquén's output per person is close to Buenos Aires City's), so Option B doubles the zone's share.
   The zone also takes five Chilean regions; Chile was not part of this request.
8. **Mexico:** México keeps about 81% of people and 80% of the economy; the Yucatán republic takes 10% of people,
   Sonora's Mexican half 5%, and the Bajas (to Cascadia) 4%.

## Decisions for the developer (nothing assumed)

1. **Option A or B** for every country (as in file `03`). Russia's existing research used B, with each region's own
   inequality; using B for China and the rest would match it.
2. **Canada's Demilitarized Zone** (15.4 million people today): where do its exiles count? It is not a nation.
3. **The Neutral Scientific Territory** (Baffin, about 19,600 people) and **Greenland** (which takes the Queen
   Elizabeth Islands' 374 people from Canada, and is not in the composition file at all).
4. **Sardinia:** Meridia, as the atlas build draws it, or not, as the Santa Luce figure assumed?
5. **Austria** (for Austro-Bavaria), **Chile** (for the Araucanía-Patagonia zone) and **Guatemala's Petén** (for the
   Yucatán republic): add these source countries, or leave each successor with only the pieces listed here?
6. **Which era's borders** the census should use (see the top of this file).
7. **How to keep the splits from tipping cities toward the Sinian Federation** (reading 1): this is where the
   developer's rebalance criteria come in. *No proposal is made here; the criteria are the developer's.*

## Approximations to know about (all flagged in the CSV)

- **Alaska Panhandle:** the whole Southeast economic region (70,233, Alaska Department of Labor 2025), Yakutat
  included; whether the Jette–Cook cut leaves Yakutat in the Panhandle is UNVERIFIED.
- **Ontario's cut line:** Northern Ontario (2021) minus Parry Sound District; the small part of Nipissing District south
  of the Mattawa is not removed (no figure found). Northern Ontario is given Ontario's GDP per person (no regional GDP
  gathered).
- **Nunavut:** split by 2021 community counts; which island Igloolik, Kinngait, Sanikiluaq and Sanirajak sit on is from
  memory (UNVERIFIED). About 3,000 people are affected.
- **Trentino-Alto Adige's GDP per person** is the unweighted mean of its two provinces.
- **Mexico's GDP shares** are at constant 2018 prices (the one complete state table found); the INEGI current-price
  shares for the large states differ by about 0.1–0.2 points.
- **Years differ by country** (USA and Canada mid-2025, Italy 1 January 2026, Germany end-2024, Mexico 2020 census,
  Argentina 2022 census provisional). Within each country one year is used, and only within-country shares matter for
  the split.
