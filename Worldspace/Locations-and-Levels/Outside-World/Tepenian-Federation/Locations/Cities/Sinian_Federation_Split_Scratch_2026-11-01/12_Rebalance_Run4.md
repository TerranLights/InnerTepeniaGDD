# Run 4: every country in its latest-period form, by headcount (2026-11-02, overnight)

**Scratch, not canon. No official file was changed.** Run overnight at the developer's request (*"go ahead and start
the research now. It's mechanical, so it should be fine to run overnight, and we'll look at the results together in
the morning"*). Figures come from `calc_run4.py` (read-only on the specs, the census and the composition file; it
reuses runs 1–3's functions); every row of every city in every census column is in `12_city_tables.csv`; the
script's whole output is the appendix. The research behind it is in `Run4_Research/` (two data files per unit and a
full search log each).

## What run 4 applies (the developer's decisions in file 11)

1. **Headcount for every split.** Each successor gets its share of the old country's people.
2. **Every name mapped to the latest period of the atlas:**
   - **China:** the Sinian Federation, plus Manchuria, Mongolia (its Inner Mongolia part), East Turkestan and Tibet inside their time-zone windows. Zhongshan's and Kunlun's China rows become the Sinian Federation whole.
   - **USA, Canada, Mexico, Argentina:** as in run 3, now by headcount.
   - **Italy:** Magna Lombardia, Meridia, and Sicilia as its own autonomous-zone row.
   - **Germany:** Germany and Austro-Bavaria.
   - **Russia:** thirteen successors, with the Republic of Karelia going to Finland.
   - **Ukraine:** without its eastern slice, which goes to Russia's core state.
   - **Belgium:** to France (Wallonia and Brussels) and the Netherlands (Flanders).
   - **South Korea:** becomes Korea, with Jeju-do as its own row.
   - **UK:** without Northern Ireland.
   - **Spain:** without Catalonia and the Basque Country (with Navarre and the two enclaves).
   - **Brazil:** without Amazonia.
   - **Indonesia:** without Aceh and West Papua.
   - **Thailand:** without Patani.
   - **Romania:** without its five counties, which go to Hungary.
   - **Chile:** without its five zone regions, which go to Araucanía-Patagonia.
   - **Czech Republic:** renamed Czechia.
3. **New pools** for the places never counted, placed by the time-zone window: Hong Kong, Macau, Taiwan, today's Mongolia, North Korea, Luxembourg, Kosovo, Austria and Petén.
4. **As in run 3:**
   - the Sinian Federation's decline (the same per-city draws, 0.55–0.65)
   - the gap filled in proportion to size by rows at 4.5% or more outside the city's top tier
   - the founder moves at Ariun Nuur (redrawn) and Utstein (the same draws)
5. **Kunlun's Option A** with Mongolia and Künnarantaiga in its middle tier as the founding wave.
6. **All 38 cities included**, the four once held back among them.

**Checks:** every city keeps its exact total in every census column, no count goes negative, and every city's shares
sum as before (the script checks all three). Kunlun's robots now total the census's 135,226, closing the spec
table's 13-robot rounding gap.

### The method choices (each one place in the script, each reversible)

- **M1, order:**
  1. The splits.
  2. China's row: each piece takes its headcount slice where the city is inside its window; outside, the slice stays with the Sinian Federation.
  3. The new pools.
  4. The decline and the fill.
  5. The founder moves.
  6. Kunlun.
- **M2, the top tier:** a successor keeps its source row's top tier only if it keeps at least half of that row. Korea from South Korea does; no American successor does. This decides who may receive the fill.
- **M3, placing a new pool:**
  - Its humans are 2% of its pool, the census's governing exile rate.
  - They go to the cities in its window as one equal percentage of each city, in every census column, and the city's other rows shrink to make room.
  - A piece that belongs to an existing nation goes only where that nation already has a row. These are Hong Kong and Macau (Sinian Federation), North Korea (Korea), Luxembourg (France), Kosovo (Serbia), Austria (Austro-Bavaria) and Petén (Yucatán).
  - Taiwan and today's Mongolia may open new rows.
- **M4, estimating a new pool:** its people × the average pool per person of the three existing nations nearest to it in GDP per person (log scale) and Gini. A place with a Gini is matched only with nations that have one.
- **M5, the exempt cities:** Zhongshan and Kunlun take no decline and no new entrants. Kunlun's rows are by space-program heritage and are not split (see "Still open").

## The research behind it (Run4_Research/)

**Unit A** (51 searches, 46 fetches; `A_Research_Log.md`):
- Population, GDP per person and Gini for the nine new places.
- World Bank population, GDP per person (2025) and Gini for the composition file's 43 nations: 42 have a Gini; New Zealand has none.
- Six of its World Bank values were re-fetched by the orchestrator and match to the digit.
- **Caveats:**
  - **Consumption-based Ginis:** China, Indonesia, South Africa, Thailand, Ukraine, Vietnam, Belarus and Mongolia. These run lower than income Ginis.
  - **Argentina's** Gini covers cities only.
  - **Taiwan's GDP** is February's preliminary figure.
  - **North Korea** has no Gini. Its income is the Bank of Korea's national-income estimate, converted to US dollars.
  - **Petén's own GDP figure** exists at the Bank of Guatemala but could not be read, so Petén uses Guatemala's.

**Unit B** (55 searches, 45 fetches; `B_Research_Log.md`):
- Each country's units and total are from one source and date.
- **Read on the statistics office's own pages:** Belgium, the UK, Spain (total summed from the official decree annex), Brazil and Romania (via City Population).
- **Secondary or snippet-only, UNVERIFIED:** Indonesia, Thailand, the Philippines, the Chile regions (they match the census exactly) and Ukraine.
- **Where two vintages came back, one whole set was used:** Brazil's 1 July 2026 official estimate, and Thailand's 2025 census preliminary (the registration set lacked Yala's figure).

**Gaps filled by the orchestrator, each logged:**
- **Jeju-do,** 672,252: a 2024 figure from an aggregator citing the Ministry of the Interior. UNVERIFIED, after two more searches and a fetch of the ministry's year-end article, which gives no provincial figures.
- **Petén,** 640,151: INE Guatemala's 2023 projection, from file 11.
- **Kherson's left bank,** 34.04%: the October 29 research's figure, from the developer's own area-weighted estimate. Unit B notes that the three districts wholly on the left bank already hold 45.65%, a figure sourced for the populations but resting on general knowledge of which districts lie on that bank. So the true share is probably higher. It changes Ukraine's split by under 0.3 point.
- **Sulu** needs no split. The atlas's Southeast Asia notes say it only moved to the Zamboanga Peninsula region within the Philippines.

## The new pools

| Place | People | GDP per person (US$) | Gini | Nearest nations | Pool | Humans (2%) | Joins | Cities | Added to each |
|---|--:|--:|--:|---|--:|--:|---|--:|--:|
| Taiwan | 23,299,132 | 39,477 | 34.1 | Spain, Italy, South Korea | 10.61M | 212,264 | its own row | 16 | 2.92% |
| Austria | 9,215,956 | 62,930 | 31.2 | Canada, UK, Sweden | 4.63M | 92,584 | Austro-Bavaria | 12 | 1.72% |
| Hong Kong | 7,518,300 | 56,983 | 39.7 | USA, Lithuania, Italy | 3.15M | 63,051 | Sinian Federation | 15 | 0.88% |
| North Korea | 26,571,036 | 1,317 | — | Philippines, Indonesia, Vietnam | 1.31M | 26,221 | Korea | 16 | 0.36% |
| Luxembourg | 690,959 | 147,252 | 33.6 | Australia, Germany, UK | 0.34M | 6,828 | France | 9 | 0.17% |
| Macau | 686,500 | 75,902 | 32.4 | Australia, UK, Germany | 0.34M | 6,784 | Sinian Federation | 15 | 0.10% |
| Mongolia (today's country) | 3,568,978 | 7,108 | 31.4 | Thailand, Indonesia, Vietnam | 0.26M | 5,161 | Mongolia | 12 | 0.09% |
| Kosovo | 1,602,515 | 7,899 | 38.3 | Vietnam, Malaysia, Thailand | 0.16M | 3,204 | Serbia | 10 | 0.07% |
| Petén | 640,151 | (Guatemala's) 6,598 | 45.2 | Brazil, Mexico, Philippines | 0.06M | 1,106 | Yucatán | 8 | 0.05% |

**Only Taiwan and Austria matter much:**
- **Taiwan** is about 2.9% of each of the 16 cities in its window: the Mirny, Janbogo and Ross Sea cities, Concordia, Dumont d'Urville, Denison and Amundsen Station.
- **Austria** adds about 1.7% to Austro-Bavaria in the Halley and Queen Maud Land cities and the Mawson side.
- **Hong Kong** adds under 1% to the Sinian Federation before its decline, and the rest are under 0.4%.

## Results

### Every city

| City | Leader after | Lead (1st ÷ 2nd) | Sinian Federation | Top five after (%) |
|---|---|--:|--:|---|
| Amundsen Station | United Kingdom 11.01 | 1.00 | 11.00 | United Kingdom 11.0, Sinian Federation 11.0, Japan 10.3, Germany 9.1, CSA 7.9 |
| Byrd | Australia 6.99 | 1.04 | 1.82 | Australia 7.0, Japan 6.7, CSA 4.4, Demilitarized Zone 4.2, Cascadia 3.7 |
| Belgrano | Brazil 12.15 | 1.10 | — | Brazil 12.1, Germany 11.1, CSA 9.1, Appalachia 5.8, Hungary 5.2 |
| Halley | Brazil 10.32 | 1.02 | — | Brazil 10.3, United Kingdom 10.1, CSA 7.5, France 7.3, Cascadia 4.9 |
| Lazar | United Kingdom 9.61 | 1.20 | — | United Kingdom 9.6, Brazil 8.0, Germany 7.8, CSA 6.0, Appalachia 3.9 |
| Neumayer | France 10.78 | 1.40 | — | France 10.8, Germany 7.7, CSA 6.2, United Kingdom 5.0, Brazil 4.1 |
| Sanay | Germany 20.60 | 2.01 | — | Germany 20.6, Brazil 10.2, United Kingdom 6.9, Austro-Bavaria 5.7, Serbia 4.5 |
| Santa Luce | Brazil 7.89 | 1.06 | — | Brazil 7.9, United Kingdom 7.4, Magna Lombardia 6.3, CSA 5.4, France 4.5 |
| Troll | United Kingdom 8.04 | 1.09 | — | United Kingdom 8.0, Brazil 7.4, CSA 5.9, France 5.6, Appalachia 3.8 |
| Utstein | France 8.89 | 1.23 | — | France 8.9, Brazil 7.2, Australia 7.0, Finland 5.3, Japan 5.2 |
| Cape Adare | Australia 11.82 | 1.02 | 11.62 | Australia 11.8, Sinian Federation 11.6, Japan 11.5, Indonesia 9.8, CSA 7.9 |
| Concordia | Korea 10.00 | 1.03 | 4.52 | Korea 10.0, Japan 9.7, Australia 8.2, Indonesia 7.7, Sinian Federation 4.5 |
| Denison | Korea 13.80 | 1.04 | 13.23 | Korea 13.8, Sinian Federation 13.2, Indonesia 11.4, CSA 9.3, Japan 8.2 |
| Dumont d'Urville | Sinian Federation 13.56 | 1.01 | 13.56 | Sinian Federation 13.6, France 13.4, Japan 13.3, Australia 12.6, CSA 7.4 |
| Fort McMurdo | France 11.54 | 1.07 | 10.01 | France 11.5, Japan 10.8, Germany 10.4, Sinian Federation 10.0, CSA 8.3 |
| Janbogo | Korea 12.24 | 1.05 | 10.57 | Korea 12.2, Australia 11.7, Sinian Federation 10.6, Indonesia 10.0, CSA 7.0 |
| Scott | Japan 11.80 | 1.03 | 11.42 | Japan 11.8, United Kingdom 11.4, Sinian Federation 11.4, Australia 10.3, CSA 8.0 |
| Zukelli | Korea 13.80 | 1.13 | 12.25 | Korea 13.8, Sinian Federation 12.3, Australia 11.6, CSA 7.7, Indonesia 6.9 |
| Dome Fuji | France 6.58 | 1.04 | 5.37 | France 6.6, Indonesia 6.3, Australia 6.1, Korea 5.6, Sinian Federation 5.4 |
| Mawson | United Kingdom 10.03 | 1.05 | 9.07 | United Kingdom 10.0, Australia 9.5, Sinian Federation 9.1, Indonesia 8.7, Japan 8.6 |
| Temirötkel | Sinian Federation 9.73 | 1.02 | 9.73 | Sinian Federation 9.7, Australia 9.5, Indonesia 9.5, United Kingdom 8.9, Germany 7.9 |
| Ariun Nuur | Japan 16.21 | 1.29 | — | Japan 16.2, Indonesia 12.6, CSA 8.9, Australia 6.2, Korea 6.2 |
| Casey | Korea 12.00 | 1.06 | 9.49 | Korea 12.0, France 11.3, Australia 10.4, Sinian Federation 9.5, CSA 8.0 |
| Davis | Japan 10.57 | 1.07 | 9.86 | Japan 10.6, Sinian Federation 9.9, United Kingdom 9.5, Germany 8.7, Korea 8.4 |
| Kunlun | Sinian Federation 15.09 | 1.95 | 15.09 | Sinian Federation 15.1, Canada 7.7, Japan 7.3, UK 7.0, Intermarium/Intermaria 6.9 |
| Mirny | United Kingdom 13.93 | 1.01 | 12.18 | United Kingdom 13.9, Korea 13.8, Indonesia 12.2, Sinian Federation 12.2, Japan 7.6 |
| Relung Panen | Japan 13.05 | 1.02 | 12.03 | Japan 13.0, Indonesia 12.8, Korea 12.5, Sinian Federation 12.0, Australia 12.0 |
| Shirayuki | Japan 34.71 | 3.58 | 4.56 | Japan 34.7, Australia 9.7, Korea 9.0, Sinian Federation 4.6, Germany 4.0 |
| Sinheung | Korea 33.06 | 3.51 | 5.46 | Korea 33.1, Japan 9.4, Germany 8.8, Sinian Federation 5.5, Indonesia 4.1 |
| Zhongshan | Sinian Federation 35.83 | 3.74 | 35.83 | Sinian Federation 35.8, Korea 9.6, Japan 7.3, Germany 7.1, Australia 3.7 |
| Contrapunto | France 11.61 | 1.06 | — | France 11.6, United Kingdom 11.0, México 9.1, Germany 9.0, CSA 7.0 |
| Esperanza | Brazil 17.03 | 1.21 | — | Brazil 17.0, México 14.1, CSA 11.8, United Kingdom 9.6, Argentina (without Patagonia) 7.9 |
| Marambio | United Kingdom 13.10 | 1.15 | — | United Kingdom 13.1, México 11.4, Spain 11.0, CSA 8.9, Brazil 5.9 |
| Palmer City | France 10.09 | 1.15 | 0.58 | France 10.1, Brazil 8.8, Germany 8.0, CSA 6.6, United Kingdom 5.4 |
| Pergamino | United Kingdom 13.33 | 1.22 | — | United Kingdom 13.3, Spain 10.9, CSA 9.6, France 8.5, Magna Lombardia 8.1 |
| Puerto Abrigo | France 16.70 | 1.20 | — | France 16.7, United Kingdom 13.9, Germany 12.4, CSA 10.3, Brazil 8.7 |
| Rothera | Brazil 12.60 | 1.05 | — | Brazil 12.6, Germany 12.0, CSA 9.2, France 7.4, United Kingdom 6.9 |
| Signy | France 17.33 | 1.05 | — | France 17.3, United Kingdom 16.5, CSA 10.8, Brazil 7.2, Appalachia 6.9 |

**Reading it (DERIVED):**
- **Lead:** 24 of the 38 cities have their leading nation at most 1.14 times the next.
- **The intended exceptions:** the founding allocations (Zhongshan, Shirayuki, Sinheung), Kunlun (Option A), and Sanay and Esperanza, which were left as they are.
- **Everywhere else, the lead is at most 1.40,** and nine cities fall between 1.15 and 1.40:
  - **Neumayer 1.40.** France leads.
  - **Ariun Nuur 1.29.** Japan, after the founder move.
  - **Utstein 1.23.** France, now that Japan has given way to the Nordic founders.
  - **Pergamino 1.22, Marambio 1.15 and Lazar 1.20.** The United Kingdom leads in all three. In Pergamino and Marambio, Spain lost Catalonia and the Basque Country.
  - **Puerto Abrigo 1.20 and Palmer City 1.15.** France leads.
- **Largest single share outside the intended cases:** Signy's France at 17.3%.
- **The Sinian Federation** is in the top five in 20 of its 22 cities (all but Byrd and Palmer City, where it is under 2%), leads two others by a hair (Dumont d'Urville 13.6%, Temirötkel 9.7%), and dominates only Zhongshan and Kunlun, as ruled.

### Nationally (Census I humans, 15,612,333 in the specs)

| Rank | Nation | Humans | Share | Listed today as |
|--:|---|--:|--:|---|
| 1 | Sinian Federation | 996,450 | 6.38% | China 1,660,450 (incl. Zhongshan's, unchanged) + Hong Kong, Macau |
| 2 | Korea | 984,677 | 6.31% | South Korea 892,502 + North Korea |
| 3 | Japan | 926,954 | 5.94% | 953,710 |
| 4 | United Kingdom | 859,530 | 5.51% | part of the UK (855,222) |
| 5 | CSA | 827,410 | 5.30% | part of the USA (2,462,596) |
| 6 | Australia | 805,878 | 5.16% | 727,081 |
| 7 | Indonesia | 647,311 | 4.15% | 606,976 |
| 8 | Brazil | 627,519 | 4.02% | 704,963 |
| 9 | Germany | 626,198 | 4.01% | 735,406 |
| 10 | France | 532,669 | 3.41% | 490,468 + part of Belgium + Luxembourg |
| 11 | Appalachia | 503,510 | 3.23% | part of the USA |
| 12 | Cascadia | 418,032 | 2.68% | parts of the USA, Canada, Mexico |
| 13 | New England | 408,879 | 2.62% | part of the USA |
| 14 | México | 224,527 | 1.44% | part of Mexico |
| 15 | Argentina (without Patagonia) | 223,633 | 1.43% | part of Argentina |
| 16 | New Zealand | 217,522 | 1.39% | 226,668 |
| 17 | Taiwan | 211,371 | 1.35% | new |
| 18 | Austro-Bavaria | 208,698 | 1.34% | part of Germany + Austria |

*The full table (83 rows) is in the appendix.*
- **No origin is above 6.4%,** and the top ten are all between 3.4% and 6.4%.
- **The run's changes compared with run 3:**
  - **Headcount enlarges the CSA** (32% of the USA's people against 29% of its economy).
  - **Spain and Germany shrink:** Spain loses Catalonia and the Basque Country; Germany loses Bavaria, which becomes Austro-Bavaria.
  - **Taiwan enters at 1.35%.**
  - **The Sinian Federation is first, barely:** Hong Kong and Macau join it, while the four pieces leave it only inside their windows.
- **Smallest rows:** the Caucasus republics, Tuva, Tibet and Iceland hold under 0.02% each.

## What needs the developer (new in run 4)

1. **Neumayer:** France leads at 10.8% (1.40 times Germany).
   - **Why:** Belgium's French-speaking half and Luxembourg join France, while Bavaria leaves Germany.
   - **The founders:** Neumayer's founders, the Netherlands and Austro-Bavaria, hold about 3% each (Austro-Bavaria 3.2%, after Austria's addition).
   - **What it is:** the same kind of founder mismatch as Ariun Nuur and Utstein; the developer's call whether to move a share as there.
2. **Kunlun's other rows still carry today's names** (USA, Russia, Canada, UK, Italy, Germany, South Korea, Argentina).
   - **Why they weren't split:** they are there for space-program heritage, so a headcount split would be meaningless.
   - **The question:** which successor carries each program (for example, the USA's) is a design question.
3. **Jeju-do and the Demilitarized Zone** each sit as their own row.
   - **Jeju-do:** 11,273 humans nationally. It is the International Court of Diplomacy's neutral ground, but people live there, unlike the Neutral Scientific Territory.
   - **The Demilitarized Zone:** 117,931 humans; already waiting for the developer.
4. **China's four pieces keep their slices without a decline.** Whether they decline too is still open; Manchuria has China's lowest birth rates today.
5. **Taiwan enters without a decline,** although its birth rate is among the world's lowest. The developer left Japan and Korea as they are; Taiwan is the same question.
6. **The tier labels** (Primary, Significant, Notable) no longer follow from the numbers in most cities and need a mechanical relabeling before the specs are edited.
7. **Kherson's left bank** (34.04% used; probably higher, see above) and **Jeju-do's population** (UNVERIFIED) are the two softest inputs, and both are small.
8. **Still open from before:** the Demilitarized Zone; Zukelli's Italian share (now split into Magna Lombardia, Meridia and Sicilia, to whom to give part of it); Kazakhstan, Uruguay and Malaysia as founders.

## Sources

The two research logs in `Run4_Research/` list every search and page. Orchestrator's additions this run:
- Searches: `제주특별자치도 주민등록인구 2024년 12월 말 기준 행정안전부`, which led to k-calc.com, an aggregator, with no official page; and `제주 인구 2024년말 67만 주민등록 감소 연합뉴스 제주도 인구`, which led to Newsis's article on the Ministry of the Interior's 2024 figures, with no provincial figures.
- Fetches: Newsis, https://www.newsis.com/view/NISX20250103_0003019683 (national total 51,217,221 only); and the World Bank API spot check, https://api.worldbank.org/v2/country/USA;CHN;JPN;AUT;LUX;MNG/indicator/NY.GDP.PCAP.CD?format=json&mrv=1&per_page=50 (all six match Unit A).

This session's searches: 10 by the orchestrator, 51 in Unit A and 55 in Unit B. None was refused. The units logged four 403 errors and three certificate-check failures, and none was worked around.

---

## Appendix: the script's full output

*Pasted from `python3 calc_run4.py`, unedited apart from heading levels.*

### Inputs

**Successor headcount shares** (share of the old country's people):

- **USA:** CSA 32.35% · Alaska 0.20% · Cascadia 15.13% · Sonora 2.85% · Colorado 4.86% · New England 16.98% · Appalachia 20.76% · Hawaii 0.42% · Midwest Republic 6.46%
- **Canada:** Quebec 28.26% · Prairie Federation 20.79% · Demilitarized Zone (s. Ontario; not a nation) 36.96% · Cascadia 13.71% · Alaska 0.28%
- **Mexico:** Cascadia 3.62% · Sonora 5.31% · Yucatán 10.36% · México 80.71%
- **Argentina:** Araucanía-Patagonia 5.68% · Argentina (without Patagonia) 94.32%
- **Italy:** Magna Lombardia 56.94% · Meridia 34.96% · Sicilia (autonomous zone within Meridia) 8.10%
- **Germany:** Austro-Bavaria 16.12% · Germany 83.88%
- **Russia:** Russia (core state) 31.36% · Idelsk-Uralia 31.36% · Siberia 12.47% · Donska-Kubania 11.95% · Künnarantaiga 7.20% · Dagestan 2.21% · Chechnya 1.05% · Kabardino-Balkaria 0.63% · North Ossetia-Alania 0.48% · Finland 0.37% · Ingushetia 0.35% · Karachay-Cherkessia 0.33% · Tuva 0.23%
- **Belgium:** Netherlands 58.05% · France 41.95%
- **UK:** Northern Ireland 2.78% · United Kingdom 97.22%
- **Spain:** Catalonia 16.59% · Basque Country 5.96% · Spain 77.45%
- **Brazil:** Amazonia 9.94% · Brazil 90.06%
- **Indonesia:** Aceh 1.98% · West Papua 2.05% · Indonesia 95.97%
- **Thailand:** Patani 2.84% · Thailand 97.16%
- **Romania:** Hungary 10.29% · Romania 89.71%
- **South Korea:** Jeju-do (neutral zone) 1.31% · Korea 98.69%
- **Chile:** Araucanía-Patagonia 13.89% · Chile 86.11%
- **Ukraine:** Russia (core state) 33.61% · Ukraine 66.39%
- **Czech Republic:** Czechia 100.00%

**China (2024 year-end, 31 provinces):** Sinian Federation 89.42% · Mongolia 1.70% · Manchuria 6.76% · Tibet 0.26% · East Turkestan 1.87%

**New pools (M4: 3 nearest existing nations by GDP per person and Gini):**

| Place | People | GDP per person (USD) | Gini | Nearest nations | Pool per person | Pool | Humans (2%) | Joins | Cities | Share added in each |
|---|--:|--:|--:|---|--:|--:|--:|---|--:|--:|
| Hong Kong | 7,518,300 | 56,983 | 39.7 | USA, Lithuania, Italy | 0.419 | 3.15M | 63,051 | Sinian Federation | 15 | 0.884% |
| Macau | 686,500 | 75,902 | 32.4 | Australia, UK, Germany | 0.494 | 0.34M | 6,784 | Sinian Federation | 15 | 0.095% |
| Taiwan | 23,299,132 | 39,477 | 34.1 | Spain, Italy, South Korea | 0.456 | 10.61M | 212,264 | Taiwan | 16 | 2.918% |
| Mongolia | 3,568,978 | 7,108 | 31.4 | Thailand, Indonesia, Vietnam | 0.072 | 0.26M | 5,161 | Mongolia | 12 | 0.093% |
| North Korea | 26,571,036 | 1,317 | — | Philippines, Indonesia, Vietnam | 0.049 | 1.31M | 26,221 | Korea | 16 | 0.360% |
| Luxembourg | 690,959 | 147,252 | 33.6 | Australia, Germany, UK | 0.494 | 0.34M | 6,828 | France | 9 | 0.172% |
| Kosovo | 1,602,515 | 7,899 | 38.3 | Vietnam, Malaysia, Thailand | 0.100 | 0.16M | 3,204 | Serbia | 10 | 0.069% |
| Austria | 9,215,956 | 62,930 | 31.2 | Canada, UK, Sweden | 0.502 | 4.63M | 92,584 | Austro-Bavaria | 12 | 1.718% |
| Petén | 640,151 | 6,598 | 45.2 | Brazil, Mexico, Philippines | 0.086 | 0.06M | 1,106 | Yucatán | 8 | 0.049% |

**Log:**

- Unit B Belgium: total 11,825,551; units used: Flemish Region, Walloon Region, Brussels-Capital Region
- Unit B United Kingdom: total 69,256,300; units used: Northern Ireland
- Unit B Spain: total 49,114,494; units used: Catalonia, Álava (Araba/Álava), Biscay (Bizkaia), Gipuzkoa, Navarre (Navarra), Condado de Treviño (municipality; province of Burgos), Valle de Villaverde (municipality; Cantabria)
- Unit B Brazil: total 214,211,951; units used: Acre, Amapá, Amazonas, Mato Grosso, Pará, Rondônia, Roraima
- Unit B Indonesia: total 284,438,800; units used: Aceh, Papua Barat (West Papua), Papua Barat Daya (Southwest Papua), Papua, Papua Tengah (Central Papua), Papua Pegunungan (Highland Papua), Papua Selatan (South Papua)
- Unit B Thailand: total 70,275,751; units used: Pattani, Yala, Narathiwat
- Unit B Romania: total 19,036,031; units used: Satu Mare, Bihor, Sălaj, Maramureș, Arad
- Unit B South Korea: Jeju blank; used 672,252 (k-calc.com, UNVERIFIED)
- Unit B South Korea: total 51,217,221; units used: Jeju Special Self-Governing Province
- Unit B Chile: total 18,480,432; units used: La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes
- Unit B Ukraine: no left-bank Kherson figure; used 34.04% of 1,001,598 (RS1b, the developer's area-weighted guess)
- Unit B Ukraine: total 41,167,335; units used: Luhansk Oblast, Donetsk Oblast, Kharkiv Oblast, Dnipropetrovsk Oblast, Zaporizhzhia Oblast, Kherson Oblast
- new pool: Petén population blank in Unit A; used 640,151 (INE 2023 projection)
- new pool Hong Kong: 63,051 humans (2% of 3,152,552) -> 15 cities at 0.884% each
- new pool Macau: 6,784 humans (2% of 339,186) -> 15 cities at 0.095% each
- new pool Taiwan: 212,264 humans (2% of 10,613,221) -> 16 cities at 2.918% each
- new pool Mongolia: 5,161 humans (2% of 258,052) -> 12 cities at 0.093% each
- new pool North Korea: 26,221 humans (2% of 1,311,059) -> 16 cities at 0.360% each
- new pool Luxembourg: 6,828 humans (2% of 341,390) -> 9 cities at 0.172% each
- new pool Kosovo: 3,204 humans (2% of 160,192) -> 10 cities at 0.069% each
- new pool Austria: 92,584 humans (2% of 4,629,203) -> 12 cities at 1.718% each
- new pool Petén: 1,106 humans (2% of 55,291) -> 8 cities at 0.049% each

*Every city keeps its exact total in every census column, no count is negative, and shares still sum as before: yes.*

### Every city

| City | Leader after | Lead (1st ÷ 2nd) | Sinian Federation | Top five after (%) |
|---|---|--:|--:|---|
| Amundsen Station | United Kingdom 11.01 | 1.00 | 11.00 | United Kingdom 11.0, Sinian Federation 11.0, Japan 10.3, Germany 9.1, CSA 7.9 |
| Byrd | Australia 6.99 | 1.04 | 1.82 | Australia 7.0, Japan 6.7, CSA 4.4, Demilitarized Zone 4.2, Cascadia 3.7 |
| Belgrano | Brazil 12.15 | 1.10 | — | Brazil 12.1, Germany 11.1, CSA 9.1, Appalachia 5.8, Hungary 5.2 |
| Halley | Brazil 10.32 | 1.02 | — | Brazil 10.3, United Kingdom 10.1, CSA 7.5, France 7.3, Cascadia 4.9 |
| Lazar | United Kingdom 9.61 | 1.20 | — | United Kingdom 9.6, Brazil 8.0, Germany 7.8, CSA 6.0, Appalachia 3.9 |
| Neumayer | France 10.78 | 1.40 | — | France 10.8, Germany 7.7, CSA 6.2, United Kingdom 5.0, Brazil 4.1 |
| Sanay | Germany 20.60 | 2.01 | — | Germany 20.6, Brazil 10.2, United Kingdom 6.9, Austro-Bavaria 5.7, Serbia 4.5 |
| Santa Luce | Brazil 7.89 | 1.06 | — | Brazil 7.9, United Kingdom 7.4, Magna Lombardia 6.3, CSA 5.4, France 4.5 |
| Troll | United Kingdom 8.04 | 1.09 | — | United Kingdom 8.0, Brazil 7.4, CSA 5.9, France 5.6, Appalachia 3.8 |
| Utstein | France 8.89 | 1.23 | — | France 8.9, Brazil 7.2, Australia 7.0, Finland 5.3, Japan 5.2 |
| Cape Adare | Australia 11.82 | 1.02 | 11.62 | Australia 11.8, Sinian Federation 11.6, Japan 11.5, Indonesia 9.8, CSA 7.9 |
| Concordia | Korea 10.00 | 1.03 | 4.52 | Korea 10.0, Japan 9.7, Australia 8.2, Indonesia 7.7, Sinian Federation 4.5 |
| Denison | Korea 13.80 | 1.04 | 13.23 | Korea 13.8, Sinian Federation 13.2, Indonesia 11.4, CSA 9.3, Japan 8.2 |
| Dumont d'Urville | Sinian Federation 13.56 | 1.01 | 13.56 | Sinian Federation 13.6, France 13.4, Japan 13.3, Australia 12.6, CSA 7.4 |
| Fort McMurdo | France 11.54 | 1.07 | 10.01 | France 11.5, Japan 10.8, Germany 10.4, Sinian Federation 10.0, CSA 8.3 |
| Janbogo | Korea 12.24 | 1.05 | 10.57 | Korea 12.2, Australia 11.7, Sinian Federation 10.6, Indonesia 10.0, CSA 7.0 |
| Scott | Japan 11.80 | 1.03 | 11.42 | Japan 11.8, United Kingdom 11.4, Sinian Federation 11.4, Australia 10.3, CSA 8.0 |
| Zukelli | Korea 13.80 | 1.13 | 12.25 | Korea 13.8, Sinian Federation 12.3, Australia 11.6, CSA 7.7, Indonesia 6.9 |
| Dome Fuji | France 6.58 | 1.04 | 5.37 | France 6.6, Indonesia 6.3, Australia 6.1, Korea 5.6, Sinian Federation 5.4 |
| Mawson | United Kingdom 10.03 | 1.05 | 9.07 | United Kingdom 10.0, Australia 9.5, Sinian Federation 9.1, Indonesia 8.7, Japan 8.6 |
| Temirötkel | Sinian Federation 9.73 | 1.02 | 9.73 | Sinian Federation 9.7, Australia 9.5, Indonesia 9.5, United Kingdom 8.9, Germany 7.9 |
| Ariun Nuur | Japan 16.21 | 1.29 | — | Japan 16.2, Indonesia 12.6, CSA 8.9, Australia 6.2, Korea 6.2 |
| Casey | Korea 12.00 | 1.06 | 9.49 | Korea 12.0, France 11.3, Australia 10.4, Sinian Federation 9.5, CSA 8.0 |
| Davis | Japan 10.57 | 1.07 | 9.86 | Japan 10.6, Sinian Federation 9.9, United Kingdom 9.5, Germany 8.7, Korea 8.4 |
| Kunlun | Sinian Federation 15.09 | 1.95 | 15.09 | Sinian Federation 15.1, Canada 7.7, Japan 7.3, UK 7.0, Intermarium/Intermaria 6.9 |
| Mirny | United Kingdom 13.93 | 1.01 | 12.18 | United Kingdom 13.9, Korea 13.8, Indonesia 12.2, Sinian Federation 12.2, Japan 7.6 |
| Relung Panen | Japan 13.05 | 1.02 | 12.03 | Japan 13.0, Indonesia 12.8, Korea 12.5, Sinian Federation 12.0, Australia 12.0 |
| Shirayuki | Japan 34.71 | 3.58 | 4.56 | Japan 34.7, Australia 9.7, Korea 9.0, Sinian Federation 4.6, Germany 4.0 |
| Sinheung | Korea 33.06 | 3.51 | 5.46 | Korea 33.1, Japan 9.4, Germany 8.8, Sinian Federation 5.5, Indonesia 4.1 |
| Zhongshan | Sinian Federation 35.83 | 3.74 | 35.83 | Sinian Federation 35.8, Korea 9.6, Japan 7.3, Germany 7.1, Australia 3.7 |
| Contrapunto | France 11.61 | 1.06 | — | France 11.6, United Kingdom 11.0, México 9.1, Germany 9.0, CSA 7.0 |
| Esperanza | Brazil 17.03 | 1.21 | — | Brazil 17.0, México 14.1, CSA 11.8, United Kingdom 9.6, Argentina (without Patagonia) 7.9 |
| Marambio | United Kingdom 13.10 | 1.15 | — | United Kingdom 13.1, México 11.4, Spain 11.0, CSA 8.9, Brazil 5.9 |
| Palmer City | France 10.09 | 1.15 | 0.58 | France 10.1, Brazil 8.8, Germany 8.0, CSA 6.6, United Kingdom 5.4 |
| Pergamino | United Kingdom 13.33 | 1.22 | — | United Kingdom 13.3, Spain 10.9, CSA 9.6, France 8.5, Magna Lombardia 8.1 |
| Puerto Abrigo | France 16.70 | 1.20 | — | France 16.7, United Kingdom 13.9, Germany 12.4, CSA 10.3, Brazil 8.7 |
| Rothera | Brazil 12.60 | 1.05 | — | Brazil 12.6, Germany 12.0, CSA 9.2, France 7.4, United Kingdom 6.9 |
| Signy | France 17.33 | 1.05 | — | France 17.3, United Kingdom 16.5, CSA 10.8, Brazil 7.2, Appalachia 6.9 |

### Nationally (Census I humans, 15,612,333)

| Rank | Nation | Humans | Share | Listed today as |
|--:|---|--:|--:|---|
| 1 | Sinian Federation | 996,450 | 6.38% | China 1,660,450 (with Zhongshan's, unchanged) + Hong Kong, Macau |
| 2 | Korea | 984,677 | 6.31% | part of South Korea + North Korea |
| 3 | Japan | 926,954 | 5.94% | 953,710 |
| 4 | United Kingdom | 859,530 | 5.51% | part of UK |
| 5 | CSA | 827,410 | 5.30% | part of USA |
| 6 | Australia | 805,878 | 5.16% | 727,081 |
| 7 | Indonesia | 647,311 | 4.15% | 606,976 |
| 8 | Brazil | 627,519 | 4.02% | 704,963 |
| 9 | Germany | 626,198 | 4.01% | 735,406 |
| 10 | France | 532,669 | 3.41% | 490,468 + part of Belgium + Luxembourg |
| 11 | Appalachia | 503,510 | 3.23% | part of USA |
| 12 | Cascadia | 418,032 | 2.68% | part of USA, Canada, Mexico |
| 13 | New England | 408,879 | 2.62% | part of USA |
| 14 | México | 224,527 | 1.44% | part of Mexico |
| 15 | Argentina (without Patagonia) | 223,633 | 1.43% | part of Argentina |
| 16 | New Zealand | 217,522 | 1.39% | 226,668 |
| 17 | Taiwan | 211,371 | 1.35% | new |
| 18 | Austro-Bavaria | 208,698 | 1.34% | part of Germany + Austria |
| 19 | Vietnam | 193,697 | 1.24% | 197,574 |
| 20 | Chile | 193,349 | 1.24% | 229,408 |
| 21 | Russia (core state) | 192,810 | 1.23% | part of Russia, Ukraine |
| 22 | Malaysia | 190,985 | 1.22% | 198,508 |
| 23 | Philippines | 188,793 | 1.21% | 196,541 |
| 24 | Hungary | 178,884 | 1.15% | 166,778 + part of Romania |
| 25 | Thailand | 165,734 | 1.06% | 173,181 |
| 26 | Estonia | 162,271 | 1.04% | 165,919 |
| 27 | South Africa | 158,351 | 1.01% | 162,098 |
| 28 | Midwest Republic | 155,463 | 1.00% | part of USA |
| 29 | Idelsk-Uralia | 149,995 | 0.96% | part of Russia |
| 30 | Serbia | 148,365 | 0.95% | 148,201 + Kosovo |
| 31 | Slovenia | 147,443 | 0.94% | 150,283 |
| 32 | Poland | 147,334 | 0.94% | 150,296 |
| 33 | Czechia | 140,759 | 0.90% | part of Czech Republic |
| 34 | Netherlands | 139,383 | 0.89% | 117,470 + part of Belgium |
| 35 | Slovakia | 137,848 | 0.88% | 140,484 |
| 36 | Romania | 137,680 | 0.88% | 157,022 |
| 37 | Lithuania | 133,436 | 0.85% | 136,473 |
| 38 | Bulgaria | 132,978 | 0.85% | 136,049 |
| 39 | Norway | 132,469 | 0.85% | 121,223 |
| 40 | Croatia | 126,886 | 0.81% | 129,454 |
| 41 | Finland | 118,701 | 0.76% | 103,357 + part of Russia |
| 42 | Belarus | 118,637 | 0.76% | 122,235 |
| 43 | Uruguay | 118,501 | 0.76% | 119,026 |
| 44 | Demilitarized Zone (s. Ontario; not a nation) | 117,931 | 0.76% | part of Canada |
| 45 | Colorado | 116,915 | 0.75% | part of USA |
| 46 | Latvia | 115,241 | 0.74% | 117,792 |
| 47 | Magna Lombardia | 111,703 | 0.72% | 13,649 + part of Italy |
| 48 | Quebec | 90,175 | 0.58% | part of Canada |
| 49 | Ukraine | 84,595 | 0.54% | 130,844 |
| 50 | Manchuria | 84,458 | 0.54% | part of China |
| 51 | Sonora | 83,439 | 0.53% | part of USA, Mexico |
| 52 | Amazonia | 69,215 | 0.44% | part of Brazil |
| 53 | Prairie Federation | 66,338 | 0.42% | part of Canada |
| 54 | Meridia | 60,375 | 0.39% | 4,550 + part of Italy |
| 55 | Siberia | 59,623 | 0.38% | part of Russia |
| 56 | Spain | 59,488 | 0.38% | 77,165 |
| 57 | Donska-Kubania | 57,165 | 0.37% | part of Russia |
| 58 | Sweden | 53,823 | 0.34% | 39,657 |
| 59 | Araucanía-Patagonia | 44,642 | 0.29% | part of Argentina, Chile |
| 60 | Künnarantaiga | 39,737 | 0.25% | part of Russia |
| 61 | Mongolia | 34,352 | 0.22% | part of China |
| 62 | Yucatán | 29,915 | 0.19% | part of Mexico + Petén |
| 63 | Northern Ireland | 23,335 | 0.15% | part of UK |
| 64 | Denmark | 17,367 | 0.11% | new |
| 65 | East Turkestan | 14,912 | 0.10% | part of China |
| 66 | Sicilia (autonomous zone within Meridia) | 12,960 | 0.08% | part of Italy |
| 67 | Catalonia | 12,740 | 0.08% | part of Spain |
| 68 | West Papua | 11,954 | 0.08% | part of Indonesia |
| 69 | Aceh | 11,549 | 0.07% | part of Indonesia |
| 70 | Jeju-do (neutral zone) | 11,273 | 0.07% | part of South Korea |
| 71 | Dagestan | 10,591 | 0.07% | part of Russia |
| 72 | Hawaii | 10,089 | 0.06% | part of USA |
| 73 | Alaska | 5,610 | 0.04% | part of USA, Canada |
| 74 | Chechnya | 5,033 | 0.03% | part of Russia |
| 75 | Patani | 4,753 | 0.03% | part of Thailand |
| 76 | Basque Country | 4,579 | 0.03% | part of Spain |
| 77 | Iceland | 3,136 | 0.02% | new |
| 78 | Kabardino-Balkaria | 3,012 | 0.02% | part of Russia |
| 79 | North Ossetia-Alania | 2,291 | 0.01% | part of Russia |
| 80 | Tibet | 2,106 | 0.01% | part of China |
| 81 | Ingushetia | 1,700 | 0.01% | part of Russia |
| 82 | Karachay-Cherkessia | 1,567 | 0.01% | part of Russia |
| 83 | Tuva | 1,126 | 0.01% | part of Russia |

### City by city (rows under 0.10% added together by source; every row is in the CSV)

#### Amundsen Station

*China's pieces in window: Mongolia, Manchuria, Tibet, East Turkestan · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36%, Austria 1.72% · Sinian draw 0.6410; fill to: CSA, United Kingdom, Germany, Japan, Korea, Australia*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | United Kingdom | UK | — | 11.01% | 123 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 11.00% | 122 |
| Significant | Japan |  | 9.59% | 10.28% | 114 |
| Significant | Germany |  | 10.09% | 9.07% | 100 |
| Significant (successor) | CSA | USA | — | 7.91% | 90 |
| Significant | Korea | South Korea + North Korea | — | 6.43% | 72 |
| Significant | Australia |  | 5.22% | 5.60% | 62 |
| Significant (successor) | Appalachia | USA | — | 4.45% | 49 |
| Significant (successor) | Cascadia | USA + Canada | — | 4.04% | 46 |
| Significant (successor) | New England | USA | — | 3.64% | 41 |
| Notable | New Zealand |  | 3.59% | 3.38% | 38 |
| Significant | Austro-Bavaria | Germany + Austria | — | 3.25% | 36 |
| Notable | Argentina (without Patagonia) | Argentina | — | 3.18% | 36 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.86% | 32 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.16% | 24 |
| Significant | Quebec | Canada | — | 1.65% | 19 |
| Notable | Norway |  | 1.67% | 1.57% | 18 |
| Significant (successor) | Midwest Republic | USA | — | 1.38% | 16 |
| Notable | Chile |  | 1.67% | 1.35% | 15 |
| Notable (China piece) | Manchuria | China | — | 1.23% | 15 |
| Significant | Prairie Federation | Canada | — | 1.21% | 14 |
| Significant (successor) | Colorado | USA | — | 1.04% | 12 |
| Significant (successor) | Sonora | USA | — | 0.61% | 7 |
| Notable | Araucanía-Patagonia | Argentina + Chile | — | 0.41% | 5 |
| Notable (China piece) | Mongolia | China | — | 0.40% | 5 |
| Notable (China piece) | East Turkestan | China | — | 0.34% | 4 |
| Significant | Northern Ireland | UK | — | 0.28% | 3 |
| | *1 smaller row from USA* | USA | — | 0.09% | 1 |
| | *1 smaller row from South Korea* | South Korea | — | 0.07% | 1 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.06% | 1 |
| | *1 smaller row from China* | China | — | 0.05% | 0 |

#### Byrd

*new pools: Petén 0.05% · Sinian draw 0.6184; fill to: Australia, Japan*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Australia |  | 6.42% | 6.99% | 13,867 |
| Significant | Japan |  | 6.19% | 6.74% | 13,371 |
| Significant (successor) | CSA | USA | — | 4.39% | 8,706 |
| Significant (successor) | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 4.22% | 8,377 |
| Significant (successor) | Cascadia | USA + Canada + Mexico | — | 3.65% | 7,247 |
| Significant (successor) | Quebec | Canada | — | 3.23% | 6,405 |
| Significant | Korea | South Korea | — | 3.15% | 6,243 |
| Significant (successor) | Appalachia | USA | — | 2.82% | 5,587 |
| Notable | Netherlands | Belgium | 2.10% | 2.63% | 5,212 |
| Significant (successor) | Prairie Federation | Canada | — | 2.38% | 4,713 |
| Significant (successor) | New England | USA | — | 2.30% | 4,570 |
| Notable | Lithuania |  | 2.27% | 2.27% | 4,502 |
| Notable | Philippines |  | 2.23% | 2.23% | 4,423 |
| Notable | Malaysia |  | 2.20% | 2.20% | 4,363 |
| Notable | Croatia |  | 2.16% | 2.16% | 4,283 |
| Notable | Thailand |  | 2.22% | 2.16% | 4,277 |
| Notable | Latvia |  | 2.15% | 2.15% | 4,264 |
| Notable | Indonesia |  | 2.21% | 2.12% | 4,206 |
| Notable | Slovakia |  | 2.06% | 2.06% | 4,085 |
| Notable | South Africa |  | 2.02% | 2.02% | 4,006 |
| Notable | Brazil |  | 2.20% | 1.98% | 3,929 |
| Notable | Czechia | Czech Republic | — | 1.96% | 3,887 |
| Notable | Uruguay |  | 1.96% | 1.96% | 3,887 |
| Notable | Vietnam |  | 1.94% | 1.94% | 3,848 |
| Notable | Finland | Russia | 1.90% | 1.90% | 3,777 |
| Notable | New Zealand |  | 1.90% | 1.90% | 3,768 |
| Notable | United Kingdom | UK | — | 1.88% | 3,720 |
| Significant | Sinian Federation | China | — | 1.82% | 3,618 |
| Notable | Romania |  | 1.90% | 1.70% | 3,380 |
| Notable | France | Belgium | 1.11% | 1.49% | 2,959 |
| Notable | Hungary | Romania | 1.23% | 1.42% | 2,827 |
| Notable | Norway |  | 1.23% | 1.23% | 2,439 |
| Notable | Belarus |  | 1.17% | 1.17% | 2,320 |
| Notable | Poland |  | 1.16% | 1.16% | 2,301 |
| Notable | Bulgaria |  | 1.06% | 1.06% | 2,102 |
| Notable | Germany |  | 1.19% | 1.00% | 1,979 |
| Notable | Argentina (without Patagonia) | Argentina | — | 0.92% | 1,833 |
| Notable | Slovenia |  | 0.92% | 0.92% | 1,825 |
| Notable | Sweden |  | 0.90% | 0.90% | 1,784 |
| Notable | Chile |  | 1.02% | 0.88% | 1,742 |
| Significant (successor) | Midwest Republic | USA | — | 0.88% | 1,737 |
| Notable | Serbia |  | 0.86% | 0.86% | 1,705 |
| Notable | Ukraine |  | 1.22% | 0.81% | 1,606 |
| Notable | Russia (core state) | Ukraine + Russia | — | 0.78% | 1,552 |
| Notable | México | Mexico | — | 0.77% | 1,537 |
| Notable | Spain |  | 0.91% | 0.70% | 1,397 |
| Significant (successor) | Colorado | USA | — | 0.66% | 1,306 |
| Notable | Magna Lombardia | Italy | — | 0.52% | 1,039 |
| Significant (successor) | Sonora | USA + Mexico | — | 0.44% | 869 |
| Notable | Idelsk-Uralia | Russia | — | 0.37% | 741 |
| Notable | Meridia | Italy | — | 0.32% | 638 |
| Notable | Amazonia | Brazil | — | 0.22% | 434 |
| Notable | Araucanía-Patagonia | Chile + Argentina | — | 0.20% | 391 |
| Notable | Austro-Bavaria | Germany | — | 0.19% | 381 |
| Notable | Catalonia | Spain | — | 0.15% | 299 |
| Notable | Siberia | Russia | — | 0.15% | 294 |
| Notable | Yucatán | Mexico + Petén | — | 0.15% | 293 |
| Notable | Donska-Kubania | Russia | — | 0.14% | 282 |
| | *8 smaller rows from Russia* | Russia | — | 0.15% | 295 |
| | *1 smaller row from Italy* | Italy | — | 0.07% | 148 |
| | *1 smaller row from Thailand* | Thailand | — | 0.06% | 125 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.06% | 117 |
| | *1 smaller row from USA* | USA | — | 0.06% | 113 |
| | *1 smaller row from Spain* | Spain | — | 0.05% | 108 |
| | *1 smaller row from UK* | UK | — | 0.05% | 107 |
| | *2 smaller rows from Indonesia* | Indonesia | — | 0.09% | 177 |
| | *1 smaller row from South Korea* | South Korea | — | 0.04% | 83 |

#### Belgrano

*new pools: Kosovo 0.07%, Austria 1.72%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 13.73% | 12.15% | 66,062 |
| Significant | Germany |  | 13.44% | 11.07% | 60,243 |
| Significant (successor) | CSA | USA | — | 9.08% | 49,387 |
| Significant (successor) | Appalachia | USA | — | 5.83% | 31,700 |
| Notable | Hungary |  | 5.32% | 5.23% | 28,435 |
| Notable | Poland |  | 5.18% | 5.09% | 27,698 |
| Notable | Uruguay |  | 4.91% | 4.82% | 26,264 |
| Significant (successor) | New England | USA | — | 4.77% | 25,927 |
| Significant | United Kingdom | UK | — | 4.75% | 25,843 |
| Notable | Slovakia |  | 4.66% | 4.58% | 24,925 |
| Significant (successor) | Cascadia | USA | — | 4.24% | 23,094 |
| Notable | Argentina (without Patagonia) | Argentina | — | 4.08% | 22,172 |
| Significant | Austro-Bavaria | Germany + Austria | — | 3.85% | 20,926 |
| Notable | Chile |  | 4.34% | 3.67% | 19,990 |
| Notable | Czechia | Czech Republic | — | 2.75% | 14,954 |
| Notable | Slovenia |  | 2.74% | 2.69% | 14,660 |
| Notable | South Africa |  | 2.48% | 2.44% | 13,244 |
| Notable | Serbia | Kosovo | 1.82% | 1.85% | 10,099 |
| Significant (successor) | Midwest Republic | USA | — | 1.81% | 9,858 |
| Significant (successor) | Colorado | USA | — | 1.36% | 7,413 |
| Significant | Amazonia | Brazil | — | 1.34% | 7,288 |
| Notable | Araucanía-Patagonia | Argentina + Chile | — | 0.84% | 4,559 |
| Significant (successor) | Sonora | USA | — | 0.80% | 4,355 |
| Notable | Croatia |  | 0.62% | 0.61% | 3,291 |
| Significant | Northern Ireland | UK | — | 0.14% | 739 |
| Significant (successor) | Hawaii | USA | — | 0.12% | 640 |
| | *1 smaller row from USA* | USA | — | 0.05% | 298 |

#### Halley

*new pools: Luxembourg 0.17%, Kosovo 0.07%, Austria 1.72%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 11.69% | 10.32% | 74,511 |
| Significant | United Kingdom | UK | — | 10.07% | 72,756 |
| Significant (successor) | CSA | USA | — | 7.46% | 53,872 |
| Significant | France | Luxembourg | 7.31% | 7.34% | 52,966 |
| Significant (successor) | Cascadia | USA + Canada | — | 4.88% | 35,221 |
| Significant (successor) | Appalachia | USA | — | 4.79% | 34,579 |
| Notable | Netherlands |  | 4.30% | 4.22% | 30,457 |
| Notable | Serbia | Kosovo | 4.10% | 4.09% | 29,525 |
| Notable | Croatia |  | 4.16% | 4.08% | 29,411 |
| Notable | Slovenia |  | 4.08% | 4.00% | 28,867 |
| Significant (successor) | New England | USA | — | 3.92% | 28,281 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 3.75% | 27,036 |
| Notable | Poland |  | 3.56% | 3.49% | 25,197 |
| Significant | Germany |  | 4.21% | 3.46% | 24,982 |
| Notable | Chile |  | 3.82% | 3.23% | 23,282 |
| Significant | Quebec | Canada | — | 2.86% | 20,674 |
| Significant | Austro-Bavaria | Germany + Austria | — | 2.38% | 17,202 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.15% | 15,504 |
| Significant | Prairie Federation | Canada | — | 2.11% | 15,208 |
| Notable | South Africa |  | 1.80% | 1.76% | 12,767 |
| Notable | Czechia | Czech Republic | — | 1.75% | 12,597 |
| Notable | Hungary |  | 1.58% | 1.55% | 11,178 |
| Significant (successor) | Midwest Republic | USA | — | 1.49% | 10,752 |
| Significant | Amazonia | Brazil | — | 1.14% | 8,220 |
| Significant (successor) | Colorado | USA | — | 1.12% | 8,087 |
| Notable | Slovakia |  | 0.85% | 0.83% | 6,004 |
| Significant (successor) | Sonora | USA | — | 0.66% | 4,751 |
| Notable | Araucanía-Patagonia | Chile + Argentina | — | 0.65% | 4,688 |
| Significant | Northern Ireland | UK | — | 0.29% | 2,084 |
| | *1 smaller row from USA* | USA | — | 0.10% | 698 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.07% | 532 |

#### Lazar

*new pools: Luxembourg 0.17%, Kosovo 0.07%, Austria 1.72%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | United Kingdom | UK | — | 9.61% | 112,403 |
| Significant | Brazil |  | 9.05% | 7.99% | 93,543 |
| Significant | Germany |  | 9.48% | 7.80% | 91,240 |
| Significant (successor) | CSA | USA | — | 6.04% | 70,709 |
| Significant (successor) | Appalachia | USA | — | 3.88% | 45,385 |
| Notable | Norway |  | 3.42% | 3.35% | 39,246 |
| Notable | Hungary | Romania | 3.08% | 3.31% | 38,707 |
| Significant | Finland | Russia | 3.34% | 3.29% | 38,482 |
| Notable | Czechia | Czech Republic | — | 3.24% | 37,900 |
| Notable | Estonia |  | 3.29% | 3.23% | 37,765 |
| Significant | Austro-Bavaria | Germany + Austria | — | 3.22% | 37,642 |
| Significant (successor) | New England | USA | — | 3.17% | 37,120 |
| Notable | Poland |  | 3.21% | 3.15% | 36,869 |
| Notable | Slovenia |  | 3.07% | 3.01% | 35,179 |
| Notable | Serbia | Kosovo | 2.95% | 2.96% | 34,619 |
| Notable | Slovakia |  | 3.00% | 2.94% | 34,431 |
| Significant (successor) | Cascadia | USA | — | 2.83% | 33,064 |
| Notable | Romania |  | 2.87% | 2.52% | 29,553 |
| Significant | France | Luxembourg | 2.30% | 2.42% | 28,401 |
| Significant | Russia (core state) | Russia + Ukraine | — | 2.04% | 23,840 |
| Notable | Belarus |  | 1.81% | 1.77% | 20,817 |
| Notable | Lithuania |  | 1.76% | 1.73% | 20,217 |
| Notable | South Africa |  | 1.55% | 1.52% | 17,777 |
| Significant | Idelsk-Uralia | Russia | — | 1.48% | 17,300 |
| Notable | Croatia |  | 1.47% | 1.44% | 16,882 |
| Notable | Latvia |  | 1.43% | 1.40% | 16,369 |
| Notable | Argentina (without Patagonia) | Argentina | — | 1.35% | 15,795 |
| Notable | Bulgaria |  | 1.34% | 1.31% | 15,401 |
| Significant (successor) | Midwest Republic | USA | — | 1.21% | 14,113 |
| Notable | Netherlands |  | 1.19% | 1.17% | 13,707 |
| Notable | Ukraine |  | 1.70% | 1.11% | 12,923 |
| Significant (successor) | Colorado | USA | — | 0.91% | 10,614 |
| Significant | Amazonia | Brazil | — | 0.88% | 10,320 |
| Significant | Siberia | Russia | — | 0.59% | 6,876 |
| Significant | Donska-Kubania | Russia | — | 0.56% | 6,593 |
| Significant (successor) | Sonora | USA | — | 0.53% | 6,235 |
| Significant | Künnarantaiga | Russia | — | 0.34% | 3,972 |
| Significant | Northern Ireland | UK | — | 0.28% | 3,219 |
| Significant | Dagestan | Russia | — | 0.10% | 1,222 |
| | *1 smaller row from Argentina* | Argentina | — | 0.08% | 950 |
| | *2 smaller rows from USA* | USA | — | 0.11% | 1,343 |
| | *6 smaller rows from Russia* | Russia | — | 0.15% | 1,700 |

#### Neumayer

*new pools: Luxembourg 0.17%, Kosovo 0.07%, Austria 1.72%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France | Belgium + Luxembourg | 10.03% | 10.78% | 67,497 |
| Significant | Germany |  | 9.39% | 7.72% | 48,328 |
| Significant (successor) | CSA | USA | — | 6.19% | 38,732 |
| Significant | United Kingdom | UK | — | 4.99% | 31,288 |
| Significant | Brazil |  | 4.60% | 4.06% | 25,422 |
| Significant (successor) | Appalachia | USA | — | 3.97% | 24,861 |
| Notable | Hungary | Romania | 3.53% | 3.76% | 23,581 |
| Notable | Sweden |  | 3.65% | 3.58% | 22,400 |
| Notable | Lithuania |  | 3.60% | 3.53% | 22,117 |
| Notable | Slovakia |  | 3.32% | 3.26% | 20,389 |
| Significant (successor) | New England | USA | — | 3.25% | 20,334 |
| Significant | Austro-Bavaria | Germany + Austria | — | 3.20% | 20,040 |
| Notable | Bulgaria |  | 3.10% | 3.04% | 19,022 |
| Notable | Finland |  | 3.01% | 2.95% | 18,453 |
| Notable | Croatia |  | 3.01% | 2.95% | 18,446 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.92% | 18,271 |
| Significant (successor) | Cascadia | USA | — | 2.89% | 18,111 |
| Notable | Romania |  | 2.99% | 2.63% | 16,478 |
| Notable | Netherlands | Belgium | 1.56% | 2.61% | 16,278 |
| Notable | Chile |  | 2.99% | 2.52% | 15,788 |
| Notable | Ukraine |  | 3.05% | 1.99% | 12,442 |
| Notable | Serbia | Kosovo | 1.82% | 1.85% | 11,615 |
| Notable | Latvia |  | 1.87% | 1.83% | 11,488 |
| Notable | Estonia |  | 1.87% | 1.83% | 11,482 |
| Notable | Norway |  | 1.78% | 1.75% | 10,912 |
| Notable | Czechia | Czech Republic | — | 1.31% | 8,243 |
| Notable | Slovenia |  | 1.27% | 1.25% | 7,818 |
| Significant (successor) | Midwest Republic | USA | — | 1.24% | 7,731 |
| Notable | Poland |  | 1.23% | 1.21% | 7,534 |
| Notable | South Africa |  | 1.17% | 1.15% | 7,161 |
| Notable | Russia (core state) | Ukraine | — | 1.01% | 6,300 |
| Significant (successor) | Colorado | USA | — | 0.93% | 5,814 |
| Notable | Araucanía-Patagonia | Argentina + Chile | — | 0.58% | 3,646 |
| Significant (successor) | Sonora | USA | — | 0.55% | 3,416 |
| Significant | Amazonia | Brazil | — | 0.45% | 2,805 |
| Significant | Northern Ireland | UK | — | 0.14% | 895 |
| | *2 smaller rows from USA* | USA | — | 0.12% | 736 |

#### Sanay

*new pools: Kosovo 0.07%, Austria 1.72%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Germany |  | 25.00% | 20.60% | 50,194 |
| Significant | Brazil |  | 11.57% | 10.23% | 24,949 |
| Significant | United Kingdom | UK | — | 6.86% | 16,701 |
| Significant (successor) | Austro-Bavaria | Germany + Austria | — | 5.68% | 13,833 |
| Notable | Serbia | Kosovo | 4.53% | 4.52% | 11,008 |
| Notable | Estonia |  | 4.58% | 4.50% | 10,952 |
| Notable | South Africa |  | 4.48% | 4.40% | 10,728 |
| Notable | Hungary | Romania | 4.10% | 4.26% | 10,389 |
| Notable | Slovenia |  | 4.11% | 4.04% | 9,839 |
| Notable | Argentina (without Patagonia) | Argentina | — | 3.91% | 9,527 |
| Notable | Bulgaria |  | 3.95% | 3.88% | 9,464 |
| Notable | Norway |  | 3.87% | 3.80% | 9,253 |
| Notable | Ukraine |  | 4.21% | 2.75% | 6,685 |
| Notable | Czechia | Czech Republic | — | 2.34% | 5,707 |
| Notable | Croatia |  | 2.15% | 2.11% | 5,136 |
| Notable | Latvia |  | 2.14% | 2.10% | 5,120 |
| Notable | Romania |  | 2.30% | 2.03% | 4,931 |
| Notable | Slovakia |  | 2.04% | 2.00% | 4,892 |
| Notable | Poland |  | 2.03% | 1.99% | 4,859 |
| Notable | Lithuania |  | 1.77% | 1.74% | 4,233 |
| Notable | Belarus |  | 1.72% | 1.69% | 4,116 |
| Notable | Chile |  | 1.67% | 1.41% | 3,452 |
| Notable | Russia (core state) | Ukraine | — | 1.39% | 3,385 |
| Significant | Amazonia | Brazil | — | 1.13% | 2,752 |
| Notable | Araucanía-Patagonia | Argentina + Chile | — | 0.46% | 1,130 |
| Significant | Northern Ireland | UK | — | 0.20% | 479 |

#### Santa Luce

*new pools: Luxembourg 0.17%, Kosovo 0.07%, Austria 1.72%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 8.93% | 7.89% | 16,863 |
| Significant | United Kingdom | UK | — | 7.44% | 15,922 |
| Significant | Magna Lombardia |  | 6.38% | 6.26% | 13,382 |
| Significant (successor) | CSA | USA | — | 5.40% | 11,544 |
| Significant | France | Belgium + Luxembourg | 3.72% | 4.45% | 9,532 |
| Notable | Netherlands | Belgium | 2.91% | 3.74% | 7,987 |
| Significant | Russia (core state) | Russia + Ukraine | — | 3.72% | 7,944 |
| Significant (successor) | Appalachia | USA | — | 3.46% | 7,410 |
| Notable | Latvia |  | 3.04% | 2.98% | 6,361 |
| Notable | Hungary | Romania | 2.68% | 2.89% | 6,179 |
| Significant (successor) | New England | USA | — | 2.83% | 6,060 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.83% | 6,068 |
| Notable | Serbia | Kosovo | 2.79% | 2.80% | 6,004 |
| Notable | Croatia |  | 2.84% | 2.78% | 5,954 |
| Notable | Estonia |  | 2.84% | 2.78% | 5,940 |
| Significant | Idelsk-Uralia | Russia | — | 2.78% | 5,943 |
| Notable | Czechia | Czech Republic | — | 2.66% | 5,682 |
| Significant (successor) | Cascadia | USA | — | 2.52% | 5,398 |
| Notable | Romania |  | 2.62% | 2.30% | 4,917 |
| Significant | Austro-Bavaria | Germany + Austria | — | 2.10% | 4,487 |
| Notable | Meridia |  | 2.13% | 2.09% | 4,461 |
| Significant | Germany |  | 2.41% | 1.98% | 4,232 |
| Notable | Ukraine |  | 2.84% | 1.85% | 3,953 |
| Notable | Sweden |  | 1.64% | 1.61% | 3,441 |
| Notable | Lithuania |  | 1.57% | 1.54% | 3,306 |
| Notable | Bulgaria |  | 1.46% | 1.43% | 3,062 |
| Notable | Norway |  | 1.42% | 1.39% | 2,967 |
| Notable | Slovakia |  | 1.42% | 1.39% | 2,982 |
| Notable | South Africa |  | 1.42% | 1.39% | 2,967 |
| Significant | Finland | Russia | 1.34% | 1.35% | 2,885 |
| Notable | Slovenia |  | 1.22% | 1.20% | 2,560 |
| Notable | Poland |  | 1.19% | 1.17% | 2,489 |
| Significant | Siberia | Russia | — | 1.10% | 2,363 |
| Significant (successor) | Midwest Republic | USA | — | 1.08% | 2,304 |
| Significant | Donska-Kubania | Russia | — | 1.06% | 2,264 |
| Significant | Amazonia | Brazil | — | 0.87% | 1,860 |
| Significant (successor) | Colorado | USA | — | 0.81% | 1,733 |
| Significant | Künnarantaiga | Russia | — | 0.64% | 1,365 |
| Significant (successor) | Sonora | USA | — | 0.48% | 1,017 |
| Significant | Northern Ireland | UK | — | 0.21% | 456 |
| Significant | Dagestan | Russia | — | 0.20% | 420 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.17% | 366 |
| | *6 smaller rows from Russia* | Russia | — | 0.27% | 584 |
| | *2 smaller rows from USA* | USA | — | 0.10% | 220 |

#### Troll

*new pools: Luxembourg 0.17%, Kosovo 0.07%, Austria 1.72%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | United Kingdom | UK | — | 8.04% | 39,228 |
| Significant | Brazil |  | 8.38% | 7.40% | 36,117 |
| Significant (successor) | CSA | USA | — | 5.90% | 28,788 |
| Significant | France | Luxembourg | 5.52% | 5.58% | 27,215 |
| Significant (successor) | Appalachia | USA | — | 3.79% | 18,478 |
| Significant | Russia (core state) | Russia + Ukraine | — | 3.56% | 17,350 |
| Significant | Finland | Russia | 3.38% | 3.35% | 16,328 |
| Notable | Czechia | Czech Republic | — | 3.32% | 16,226 |
| Notable | Slovakia |  | 3.39% | 3.32% | 16,235 |
| Notable | Croatia |  | 3.31% | 3.25% | 15,843 |
| Notable | Serbia | Kosovo | 3.23% | 3.23% | 15,795 |
| Notable | Netherlands |  | 3.28% | 3.22% | 15,683 |
| Notable | Slovenia |  | 3.24% | 3.18% | 15,505 |
| Notable | Argentina (without Patagonia) | Argentina | — | 3.17% | 15,453 |
| Significant (successor) | New England | USA | — | 3.10% | 15,113 |
| Notable | Bulgaria |  | 3.10% | 3.04% | 14,814 |
| Significant | Idelsk-Uralia | Russia | — | 3.04% | 14,826 |
| Notable | Latvia |  | 3.08% | 3.02% | 14,735 |
| Significant (successor) | Cascadia | USA | — | 2.76% | 13,461 |
| Significant | Germany |  | 2.66% | 2.19% | 10,686 |
| Significant | Austro-Bavaria | Germany + Austria | — | 2.14% | 10,433 |
| Notable | Poland |  | 1.55% | 1.52% | 7,435 |
| Notable | Hungary | Romania | 1.42% | 1.52% | 7,385 |
| Notable | Sweden |  | 1.41% | 1.38% | 6,741 |
| Notable | Lithuania |  | 1.37% | 1.34% | 6,564 |
| Notable | Belarus |  | 1.34% | 1.31% | 6,403 |
| Notable | Estonia |  | 1.27% | 1.25% | 6,095 |
| Notable | Norway |  | 1.26% | 1.24% | 6,012 |
| Notable | South Africa |  | 1.26% | 1.24% | 6,023 |
| Significant | Siberia | Russia | — | 1.21% | 5,893 |
| Significant (successor) | Midwest Republic | USA | — | 1.18% | 5,747 |
| Significant | Donska-Kubania | Russia | — | 1.16% | 5,650 |
| Notable | Romania |  | 1.23% | 1.08% | 5,261 |
| Notable | Ukraine |  | 1.57% | 1.02% | 4,987 |
| Significant (successor) | Colorado | USA | — | 0.89% | 4,321 |
| Significant | Amazonia | Brazil | — | 0.82% | 3,984 |
| Significant | Künnarantaiga | Russia | — | 0.70% | 3,405 |
| Significant (successor) | Sonora | USA | — | 0.52% | 2,539 |
| Significant | Northern Ireland | UK | — | 0.23% | 1,123 |
| Significant | Dagestan | Russia | — | 0.21% | 1,047 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.19% | 930 |
| Significant | Chechnya | Russia | — | 0.10% | 497 |
| | *2 smaller rows from USA* | USA | — | 0.11% | 547 |
| | *5 smaller rows from Russia* | Russia | — | 0.20% | 958 |

#### Utstein

*new pools: Luxembourg 0.17%, Kosovo 0.07%, Austria 1.72% · from Japan: Iceland 0.55, Norway 2.41, Sweden 2.65, Finland 2.77, Denmark 3.07*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France | Belgium + Luxembourg | 7.73% | 8.89% | 50,312 |
| Significant | Brazil |  | 8.18% | 7.22% | 40,876 |
| Significant | Australia |  | 7.19% | 7.05% | 39,869 |
| Founder | Finland |  | 2.57% | 5.29% | 29,955 |
| Primary | Japan |  | 16.94% | 5.15% | 29,169 |
| Founder | Norway |  | 2.76% | 5.12% | 28,991 |
| Significant (successor) | CSA | USA | — | 4.58% | 25,905 |
| Significant | Germany |  | 4.58% | 3.77% | 21,311 |
| Founder | Denmark |  | — | 3.07% | 17,367 |
| Notable | Netherlands | Belgium | 1.42% | 2.97% | 16,825 |
| Significant (successor) | Appalachia | USA | — | 2.94% | 16,627 |
| Notable | Serbia | Kosovo | 2.67% | 2.69% | 15,178 |
| Notable | Poland |  | 2.73% | 2.68% | 15,140 |
| Founder | Sweden |  | — | 2.65% | 14,983 |
| Notable | Bulgaria |  | 2.57% | 2.52% | 14,258 |
| Notable | Czechia | Czech Republic | — | 2.46% | 13,903 |
| Notable | Latvia |  | 2.51% | 2.46% | 13,944 |
| Significant | Austro-Bavaria | Germany + Austria | — | 2.44% | 13,817 |
| Significant (successor) | New England | USA | — | 2.40% | 13,599 |
| Notable | Romania |  | 2.52% | 2.22% | 12,530 |
| Significant (successor) | Cascadia | USA | — | 2.14% | 12,114 |
| Notable | Ukraine |  | 2.71% | 1.76% | 9,975 |
| Significant | United Kingdom | UK | — | 1.66% | 9,385 |
| Notable | Hungary | Romania | 1.41% | 1.64% | 9,252 |
| Notable | Belarus |  | 1.40% | 1.37% | 7,793 |
| Notable | Croatia |  | 1.35% | 1.32% | 7,501 |
| Notable | Lithuania |  | 1.35% | 1.32% | 7,479 |
| Notable | Slovakia |  | 1.26% | 1.24% | 6,963 |
| Notable | Estonia |  | 1.21% | 1.19% | 6,733 |
| Notable | South Africa |  | 1.16% | 1.14% | 6,427 |
| Notable | Slovenia |  | 1.14% | 1.12% | 6,309 |
| Notable | Argentina (without Patagonia) | Argentina | — | 1.10% | 6,242 |
| Significant (successor) | Midwest Republic | USA | — | 0.91% | 5,171 |
| Notable | Russia (core state) | Ukraine | — | 0.89% | 5,051 |
| Significant | Amazonia | Brazil | — | 0.80% | 4,509 |
| Significant (successor) | Colorado | USA | — | 0.69% | 3,888 |
| Founder | Iceland |  | — | 0.55% | 3,136 |
| Significant (successor) | Sonora | USA | — | 0.40% | 2,284 |
| | *1 smaller row from Argentina* | Argentina | — | 0.07% | 376 |
| | *2 smaller rows from USA* | USA | — | 0.09% | 491 |
| | *1 smaller row from UK* | UK | — | 0.05% | 269 |

#### Cape Adare

*China's pieces in window: Mongolia, Manchuria · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, North Korea 0.36% · Sinian draw 0.6333; fill to: CSA, Australia, Japan, Indonesia, Korea, United Kingdom*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Australia |  | 10.76% | 11.82% | 89,589 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 11.62% | 88,098 |
| Significant | Japan |  | 10.49% | 11.52% | 87,398 |
| Significant | Indonesia |  | 9.28% | 9.78% | 74,159 |
| Significant (successor) | CSA | USA | — | 7.91% | 59,960 |
| Significant | Korea | South Korea + North Korea | — | 6.15% | 46,648 |
| Significant | United Kingdom | UK | — | 5.37% | 40,734 |
| Significant (successor) | Appalachia | USA | — | 4.43% | 33,560 |
| Significant (successor) | Cascadia | USA + Canada | — | 4.08% | 30,932 |
| Significant (successor) | New England | USA | — | 3.62% | 27,448 |
| Notable | Chile |  | 3.74% | 3.08% | 23,405 |
| Notable | New Zealand |  | 3.19% | 3.06% | 23,136 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 22,044 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.30% | 17,473 |
| Notable | Philippines |  | 2.08% | 1.99% | 15,081 |
| Significant | Quebec | Canada | — | 1.76% | 13,361 |
| Notable | Malaysia |  | 1.52% | 1.46% | 11,040 |
| Significant (successor) | Midwest Republic | USA | — | 1.38% | 10,436 |
| Significant | Prairie Federation | Canada | — | 1.30% | 9,829 |
| Notable (China piece) | Manchuria | China | — | 1.28% | 9,737 |
| Significant (successor) | Colorado | USA | — | 1.04% | 7,849 |
| Significant (successor) | Sonora | USA | — | 0.61% | 4,609 |
| Notable | Araucanía-Patagonia | Chile | — | 0.50% | 3,773 |
| Notable (China piece) | Mongolia | China | — | 0.32% | 2,447 |
| Significant | West Papua | Indonesia | — | 0.18% | 1,380 |
| Significant | Aceh | Indonesia | — | 0.18% | 1,333 |
| Significant | Northern Ireland | UK | — | 0.13% | 1,017 |
| | *1 smaller row from USA* | USA | — | 0.09% | 678 |
| | *1 smaller row from South Korea* | South Korea | — | 0.07% | 504 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.06% | 449 |

#### Concordia

*China's pieces in window: Mongolia, Manchuria, Tibet, East Turkestan · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36% · Sinian draw 0.5996; fill to: Japan, Korea, Australia, Indonesia (FALLBACK)*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Korea | South Korea + North Korea | — | 10.00% | 51,665 |
| Primary | Japan |  | 9.32% | 9.74% | 50,390 |
| Primary | Australia |  | 7.82% | 8.17% | 42,251 |
| Primary | Indonesia |  | 7.72% | 7.75% | 40,013 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 4.52% | 23,343 |
| Significant | Vietnam |  | 4.23% | 4.05% | 20,905 |
| Significant | Belarus |  | 3.77% | 3.61% | 18,639 |
| Significant | New Zealand |  | 3.76% | 3.60% | 18,624 |
| Significant (successor) | Russia (core state) | Russia + Ukraine | — | 2.98% | 15,427 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 15,018 |
| Significant (successor) | Idelsk-Uralia | Russia | — | 2.76% | 14,277 |
| Significant | Philippines |  | 2.62% | 2.51% | 12,935 |
| Notable | France | Belgium | 1.51% | 2.06% | 10,677 |
| Significant | Malaysia |  | 1.95% | 1.87% | 9,645 |
| Notable | Serbia |  | 1.59% | 1.52% | 7,873 |
| Notable | Estonia |  | 1.55% | 1.48% | 7,676 |
| Significant | Thailand |  | 1.58% | 1.47% | 7,611 |
| Notable | Hungary | Romania | 1.43% | 1.44% | 7,449 |
| Notable | Netherlands | Belgium | 0.59% | 1.42% | 7,331 |
| Significant (successor) | Finland | Russia | 1.41% | 1.38% | 7,135 |
| Notable | Croatia |  | 1.44% | 1.38% | 7,119 |
| Significant | CSA | USA | — | 1.37% | 7,093 |
| Notable | Czechia | Czech Republic | — | 1.32% | 6,836 |
| Notable | Norway |  | 1.38% | 1.32% | 6,813 |
| Notable | Poland |  | 1.32% | 1.26% | 6,519 |
| Notable | United Kingdom | UK | — | 1.23% | 6,346 |
| Significant (successor) | Siberia | Russia | — | 1.10% | 5,676 |
| Notable | Spain |  | 1.47% | 1.09% | 5,626 |
| Significant (successor) | Donska-Kubania | Russia | — | 1.05% | 5,442 |
| Notable | México | Mexico | — | 1.00% | 5,139 |
| Significant | Appalachia | USA | — | 0.88% | 4,554 |
| Notable | Lithuania |  | 0.84% | 0.80% | 4,158 |
| Notable | Latvia |  | 0.81% | 0.78% | 3,996 |
| Significant | Cascadia | USA + Mexico + Canada | — | 0.77% | 3,965 |
| Significant | New England | USA | — | 0.72% | 3,725 |
| Notable | Sweden |  | 0.75% | 0.72% | 3,712 |
| Notable | Bulgaria |  | 0.72% | 0.69% | 3,559 |
| Significant (successor) | Künnarantaiga | Russia | — | 0.63% | 3,279 |
| Notable | Slovakia |  | 0.66% | 0.63% | 3,261 |
| Notable | Romania |  | 0.69% | 0.59% | 3,056 |
| Notable (China piece) | Manchuria | China | — | 0.50% | 2,572 |
| Notable | Germany |  | 0.58% | 0.47% | 2,390 |
| Notable | Ukraine |  | 0.69% | 0.44% | 2,275 |
| Notable | Magna Lombardia | Italy | — | 0.41% | 2,102 |
| Significant | Midwest Republic | USA | — | 0.27% | 1,417 |
| Notable | Slovenia |  | 0.28% | 0.27% | 1,397 |
| Notable | Meridia | Italy | — | 0.25% | 1,290 |
| Notable | Catalonia | Spain | — | 0.23% | 1,206 |
| Notable (China piece) | Mongolia | China | — | 0.22% | 1,127 |
| Notable | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 0.22% | 1,125 |
| Significant | Colorado | USA | — | 0.21% | 1,065 |
| Significant (successor) | Dagestan | Russia | — | 0.19% | 1,009 |
| Significant | Sonora | USA + Mexico | — | 0.19% | 964 |
| Notable | Quebec | Canada | — | 0.16% | 859 |
| Significant (successor) | West Papua | Indonesia | — | 0.15% | 781 |
| Significant (successor) | Aceh | Indonesia | — | 0.15% | 754 |
| Notable (China piece) | East Turkestan | China | — | 0.14% | 709 |
| Notable | Yucatán | Mexico | — | 0.13% | 659 |
| Notable | Prairie Federation | Canada | — | 0.12% | 632 |
| Significant (successor) | Jeju-do (neutral zone) | South Korea | — | 0.12% | 603 |
| | *6 smaller rows from Russia* | Russia | — | 0.27% | 1,401 |
| | *1 smaller row from Germany* | Germany | — | 0.09% | 460 |
| | *1 smaller row from Spain* | Spain | — | 0.08% | 434 |
| | *1 smaller row from Italy* | Italy | — | 0.06% | 299 |
| | *1 smaller row from Thailand* | Thailand | — | 0.04% | 223 |
| | *1 smaller row from UK* | UK | — | 0.04% | 181 |
| | *1 smaller row from China* | China | — | 0.02% | 101 |
| | *1 smaller row from USA* | USA | — | 0.02% | 92 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.01% | 52 |

#### Denison

*China's pieces in window: Mongolia, Manchuria · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36% · Sinian draw 0.6464; fill to: CSA, Appalachia, Korea, Indonesia, Japan, Australia*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Korea | South Korea + North Korea | — | 13.80% | 63,022 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 13.23% | 60,448 |
| Significant | Indonesia |  | 10.77% | 11.39% | 52,023 |
| Significant (successor) | CSA | USA | — | 9.33% | 42,621 |
| Significant | Japan |  | 7.41% | 8.16% | 37,262 |
| Significant | Australia |  | 5.87% | 6.47% | 29,525 |
| Significant (successor) | Appalachia | USA | — | 5.99% | 27,357 |
| Significant (successor) | New England | USA | — | 4.26% | 19,437 |
| Significant (successor) | Cascadia | USA | — | 3.79% | 17,313 |
| Notable | New Zealand |  | 3.92% | 3.75% | 17,139 |
| Notable | Vietnam |  | 3.72% | 3.56% | 16,244 |
| Notable | Philippines |  | 3.64% | 3.48% | 15,926 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 13,267 |
| Notable | Malaysia |  | 2.42% | 2.32% | 10,559 |
| Significant (successor) | Midwest Republic | USA | — | 1.62% | 7,391 |
| Notable (China piece) | Manchuria | China | — | 1.44% | 6,581 |
| Notable | Thailand |  | 1.45% | 1.35% | 6,166 |
| Significant (successor) | Colorado | USA | — | 1.22% | 5,559 |
| Significant (successor) | Sonora | USA | — | 0.71% | 3,265 |
| Notable (China piece) | Mongolia | China | — | 0.46% | 2,079 |
| Significant | West Papua | Indonesia | — | 0.21% | 965 |
| Significant | Aceh | Indonesia | — | 0.20% | 931 |
| Significant | Jeju-do (neutral zone) | South Korea | — | 0.15% | 706 |
| Significant (successor) | Hawaii | USA | — | 0.11% | 479 |
| | *1 smaller row from USA* | USA | — | 0.05% | 223 |
| | *1 smaller row from Thailand* | Thailand | — | 0.04% | 180 |

#### Dumont d'Urville

*China's pieces in window: Mongolia, Manchuria, Tibet, East Turkestan · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36% · Sinian draw 0.6236; fill to: CSA, France, Japan, Australia, Indonesia*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 13.56% | 27,291 |
| Significant | France |  | 11.80% | 13.37% | 26,894 |
| Significant | Japan |  | 11.72% | 13.28% | 26,724 |
| Significant | Australia |  | 11.08% | 12.55% | 25,252 |
| Significant (successor) | CSA | USA | — | 7.38% | 14,845 |
| Significant | Indonesia |  | 5.59% | 6.08% | 12,230 |
| Significant (successor) | Appalachia | USA | — | 4.00% | 8,047 |
| Notable | New Zealand |  | 4.16% | 3.98% | 8,000 |
| Notable | Vietnam |  | 4.04% | 3.87% | 7,778 |
| Significant (successor) | New England | USA | — | 3.27% | 6,581 |
| Notable | Philippines |  | 3.40% | 3.25% | 6,544 |
| Significant (successor) | Cascadia | USA | — | 2.91% | 5,862 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 5,845 |
| Notable | Malaysia |  | 2.16% | 2.07% | 4,153 |
| Significant | Korea | South Korea + North Korea | — | 1.76% | 3,539 |
| Notable (China piece) | Manchuria | China | — | 1.57% | 3,164 |
| Significant (successor) | Midwest Republic | USA | — | 1.24% | 2,502 |
| Significant (successor) | Colorado | USA | — | 0.94% | 1,882 |
| Significant (successor) | Sonora | USA | — | 0.55% | 1,106 |
| Notable (China piece) | Mongolia | China | — | 0.49% | 982 |
| Notable (China piece) | East Turkestan | China | — | 0.43% | 873 |
| Notable | Thailand |  | 0.14% | 0.13% | 259 |
| Significant | West Papua | Indonesia | — | 0.11% | 220 |
| Significant | Aceh | Indonesia | — | 0.11% | 214 |
| | *2 smaller rows from USA* | USA | — | 0.12% | 238 |
| | *1 smaller row from China* | China | — | 0.06% | 123 |
| | *1 smaller row from South Korea* | South Korea | — | 0.02% | 38 |
| | *1 smaller row from Thailand* | Thailand | — | 0.00% | 8 |

#### Fort McMurdo

*China's pieces in window: Mongolia, Manchuria · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, North Korea 0.36% · Sinian draw 0.5591; fill to: CSA, Germany, France, Japan*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France |  | 9.73% | 11.54% | 25,625 |
| Significant | Japan |  | 9.08% | 10.77% | 23,939 |
| Significant | Germany |  | 10.49% | 10.43% | 23,175 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 10.01% | 22,241 |
| Significant (successor) | CSA | USA | — | 8.32% | 18,484 |
| Significant (successor) | Appalachia | USA | — | 4.31% | 9,584 |
| Significant | United Kingdom | UK | — | 3.98% | 8,829 |
| Significant (successor) | Cascadia | USA + Canada | — | 3.60% | 8,000 |
| Significant (successor) | New England | USA | — | 3.53% | 7,839 |
| Notable | Malaysia |  | 3.31% | 3.17% | 7,044 |
| Notable | New Zealand |  | 3.20% | 3.07% | 6,817 |
| Notable | Chile |  | 3.54% | 2.92% | 6,491 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 6,461 |
| Significant | Magna Lombardia | Italy | — | 2.67% | 5,937 |
| Notable | Korea | South Korea + North Korea | — | 1.91% | 4,239 |
| Notable | Australia |  | 1.92% | 1.84% | 4,095 |
| Notable | Indonesia |  | 1.82% | 1.67% | 3,714 |
| Significant | Meridia | Italy | — | 1.64% | 3,643 |
| Significant | Austro-Bavaria | Germany | — | 1.62% | 3,597 |
| Notable | Philippines |  | 1.59% | 1.52% | 3,377 |
| Significant (successor) | Midwest Republic | USA | — | 1.34% | 2,979 |
| Notable (China piece) | Manchuria | China | — | 1.25% | 2,780 |
| Notable | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 1.24% | 2,746 |
| Significant (successor) | Colorado | USA | — | 1.01% | 2,241 |
| Notable | Quebec | Canada | — | 0.94% | 2,100 |
| Notable | Prairie Federation | Canada | — | 0.69% | 1,545 |
| Significant (successor) | Sonora | USA | — | 0.59% | 1,316 |
| Notable | Araucanía-Patagonia | Chile | — | 0.47% | 1,046 |
| Significant | Sicilia (autonomous zone within Meridia) | Italy | — | 0.38% | 845 |
| Notable (China piece) | Mongolia | China | — | 0.31% | 699 |
| Significant | Northern Ireland | UK | — | 0.11% | 253 |
| | *1 smaller row from USA* | USA | — | 0.09% | 193 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.05% | 112 |
| | *2 smaller rows from Indonesia* | Indonesia | — | 0.07% | 157 |
| | *1 smaller row from South Korea* | South Korea | — | 0.02% | 47 |

#### Janbogo

*China's pieces in window: Mongolia, Manchuria · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, North Korea 0.36% · Sinian draw 0.5550; fill to: CSA, Korea, Australia, Magna Lombardia, Indonesia*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Korea | South Korea + North Korea | — | 12.24% | 80,615 |
| Significant | Australia |  | 9.99% | 11.68% | 76,924 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 10.57% | 69,599 |
| Significant | Indonesia |  | 8.88% | 9.96% | 65,605 |
| Significant (successor) | CSA | USA | — | 6.95% | 45,812 |
| Significant | Magna Lombardia | Italy | — | 6.08% | 40,053 |
| Significant | Japan |  | 4.41% | 4.22% | 27,798 |
| Significant | Germany |  | 4.64% | 3.73% | 24,570 |
| Significant (successor) | Appalachia | USA | — | 3.66% | 24,095 |
| Significant (successor) | Cascadia | USA + Canada | — | 3.18% | 20,960 |
| Significant | Meridia | Italy | — | 3.06% | 20,147 |
| Notable | Malaysia |  | 3.13% | 3.00% | 19,769 |
| Significant (successor) | New England | USA | — | 2.99% | 19,707 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 19,153 |
| Notable | Chile |  | 3.22% | 2.66% | 17,469 |
| Notable | Philippines |  | 1.74% | 1.67% | 11,008 |
| Notable | New Zealand |  | 1.66% | 1.59% | 10,492 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 1.39% | 9,182 |
| Notable (China piece) | Manchuria | China | — | 1.34% | 8,794 |
| Significant (successor) | Midwest Republic | USA | — | 1.14% | 7,494 |
| Significant | Quebec | Canada | — | 1.07% | 7,020 |
| Significant (successor) | Colorado | USA | — | 0.86% | 5,635 |
| Significant | Prairie Federation | Canada | — | 0.78% | 5,164 |
| Significant | Austro-Bavaria | Germany | — | 0.72% | 4,723 |
| Significant | Sicilia (autonomous zone within Meridia) | Italy | — | 0.71% | 4,669 |
| Significant (successor) | Sonora | USA | — | 0.50% | 3,311 |
| Notable | Araucanía-Patagonia | Chile | — | 0.43% | 2,817 |
| Notable (China piece) | Mongolia | China | — | 0.34% | 2,211 |
| Significant | West Papua | Indonesia | — | 0.17% | 1,146 |
| Significant | Aceh | Indonesia | — | 0.17% | 1,109 |
| Significant | Jeju-do (neutral zone) | South Korea | — | 0.13% | 846 |
| | *1 smaller row from USA* | USA | — | 0.07% | 486 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.05% | 297 |

#### Scott

*China's pieces in window: Mongolia, Manchuria · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, North Korea 0.36% · Sinian draw 0.6337; fill to: CSA, Japan, United Kingdom, Australia, Korea, Indonesia*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Japan |  | 10.81% | 11.80% | 22,394 |
| Significant | United Kingdom | UK | — | 11.45% | 21,737 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 11.42% | 21,691 |
| Significant | Australia |  | 9.43% | 10.29% | 19,538 |
| Significant (successor) | CSA | USA | — | 7.99% | 15,159 |
| Significant | Korea | South Korea + North Korea | — | 7.26% | 13,778 |
| Significant | Indonesia |  | 4.98% | 5.22% | 9,900 |
| Significant (successor) | Appalachia | USA | — | 4.50% | 8,539 |
| Significant (successor) | Cascadia | USA + Canada | — | 3.93% | 7,467 |
| Significant (successor) | New England | USA | — | 3.68% | 6,985 |
| Notable | New Zealand |  | 3.52% | 3.37% | 6,406 |
| Notable | Chile |  | 3.69% | 3.04% | 5,771 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 5,519 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 1.77% | 3,357 |
| Notable | Malaysia |  | 1.74% | 1.67% | 3,163 |
| Notable | Philippines |  | 1.58% | 1.51% | 2,867 |
| Significant (successor) | Midwest Republic | USA | — | 1.40% | 2,654 |
| Significant | Quebec | Canada | — | 1.35% | 2,567 |
| Notable (China piece) | Manchuria | China | — | 1.26% | 2,394 |
| Significant (successor) | Colorado | USA | — | 1.05% | 1,998 |
| Significant | Prairie Federation | Canada | — | 1.00% | 1,888 |
| Significant (successor) | Sonora | USA | — | 0.62% | 1,174 |
| Notable | Araucanía-Patagonia | Chile | — | 0.49% | 930 |
| Notable (China piece) | Mongolia | China | — | 0.32% | 601 |
| Significant | Northern Ireland | UK | — | 0.29% | 545 |
| | *2 smaller rows from Indonesia* | Indonesia | — | 0.19% | 364 |
| | *1 smaller row from USA* | USA | — | 0.09% | 172 |
| | *1 smaller row from South Korea* | South Korea | — | 0.08% | 151 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.06% | 107 |

#### Zukelli

*China's pieces in window: Mongolia, Manchuria · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, North Korea 0.36% · Sinian draw 0.5894; fill to: CSA, Korea, Australia, Indonesia*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Korea | South Korea + North Korea | — | 13.80% | 88,290 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 12.25% | 78,400 |
| Significant | Australia |  | 9.55% | 11.63% | 74,430 |
| Significant (successor) | CSA | USA | — | 7.67% | 49,074 |
| Significant | Indonesia |  | 5.89% | 6.88% | 44,041 |
| Significant | Japan |  | 4.69% | 4.49% | 28,723 |
| Significant (successor) | Cascadia | USA + Canada | — | 4.12% | 26,367 |
| Significant (successor) | Appalachia | USA | — | 3.87% | 24,775 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 3.50% | 22,419 |
| Significant | Magna Lombardia | Italy | — | 3.40% | 21,758 |
| Notable | Malaysia |  | 3.44% | 3.30% | 21,086 |
| Notable | New Zealand |  | 3.37% | 3.23% | 20,665 |
| Significant (successor) | New England | USA | — | 3.17% | 20,264 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 18,602 |
| Significant | Quebec | Canada | — | 2.68% | 17,142 |
| Significant | Meridia | Italy | — | 2.09% | 13,357 |
| Significant | Prairie Federation | Canada | — | 1.97% | 12,611 |
| Notable | Philippines |  | 1.89% | 1.81% | 11,585 |
| Notable | Chile |  | 1.82% | 1.50% | 9,613 |
| Notable (China piece) | Manchuria | China | — | 1.46% | 9,370 |
| Significant (successor) | Midwest Republic | USA | — | 1.20% | 7,704 |
| Significant (successor) | Colorado | USA | — | 0.91% | 5,794 |
| Significant (successor) | Sonora | USA | — | 0.53% | 3,404 |
| Significant | Sicilia (autonomous zone within Meridia) | Italy | — | 0.48% | 3,096 |
| Notable (China piece) | Mongolia | China | — | 0.37% | 2,356 |
| Notable | Araucanía-Patagonia | Chile | — | 0.24% | 1,549 |
| Significant | Jeju-do (neutral zone) | South Korea | — | 0.14% | 893 |
| Significant | West Papua | Indonesia | — | 0.12% | 739 |
| Significant | Aceh | Indonesia | — | 0.11% | 712 |
| | *1 smaller row from USA* | USA | — | 0.08% | 499 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.06% | 405 |

#### Dome Fuji

*China's pieces in window: Tibet, East Turkestan · new pools: Luxembourg 0.17%, Kosovo 0.07%, Austria 1.72% · Sinian draw 0.5526; fill to: Indonesia, Australia, France, Korea*

| Tier | Row | From | Before | After |
|---|---|---|--:|--:|
| Significant | France | Belgium + Luxembourg | 5.00% | 6.58% |
| Significant | Indonesia |  | 5.51% | 6.30% |
| Significant | Australia |  | 5.16% | 6.14% |
| Significant | Korea | South Korea | — | 5.62% |
| Primary | Sinian Federation | China | — | 5.37% |
| Significant | Germany |  | 4.83% | 3.97% |
| Significant (successor) | CSA | USA | — | 3.55% |
| Significant | Brazil |  | 3.17% | 2.80% |
| Significant | Japan |  | 2.84% | 2.78% |
| Significant | Austro-Bavaria | Germany + Austria | — | 2.48% |
| Significant | United Kingdom | UK | — | 2.37% |
| Notable | Netherlands | Belgium | 1.90% | 2.34% |
| Significant (successor) | Appalachia | USA | — | 2.28% |
| Significant (successor) | Cascadia | USA + Mexico + Canada | — | 1.96% |
| Notable | Hungary | Romania | 1.81% | 1.96% |
| Notable | Malaysia |  | 1.91% | 1.87% |
| Significant (successor) | New England | USA | — | 1.86% |
| Notable | Slovenia |  | 1.87% | 1.83% |
| Notable | Belarus |  | 1.83% | 1.79% |
| Notable | Croatia |  | 1.82% | 1.78% |
| Notable | Serbia | Kosovo | 1.72% | 1.75% |
| Notable | Czechia | Czech Republic | — | 1.71% |
| Notable | Latvia |  | 1.73% | 1.70% |
| Notable | Philippines |  | 1.71% | 1.68% |
| Notable | Estonia |  | 1.69% | 1.66% |
| Notable | Norway |  | 1.67% | 1.64% |
| Notable | Romania |  | 1.82% | 1.60% |
| Notable | México | Mexico | — | 1.50% |
| Notable | Spain |  | 1.89% | 1.44% |
| Significant | Russia (core state) | Russia + Ukraine | — | 0.99% |
| Significant | Finland | Russia | 0.98% | 0.97% |
| Notable | Slovakia |  | 0.96% | 0.94% |
| Notable | Bulgaria |  | 0.95% | 0.93% |
| Notable | Sweden |  | 0.94% | 0.92% |
| Notable | Vietnam |  | 0.94% | 0.92% |
| Notable | Chile |  | 0.99% | 0.84% |
| Notable | New Zealand |  | 0.85% | 0.83% |
| Notable | Thailand |  | 0.84% | 0.80% |
| Notable | South Africa |  | 0.80% | 0.78% |
| Notable | Argentina (without Patagonia) | Argentina | — | 0.78% |
| Notable | Uruguay |  | 0.77% | 0.75% |
| Notable | Poland |  | 0.77% | 0.75% |
| Notable | Lithuania |  | 0.76% | 0.75% |
| Significant (successor) | Midwest Republic | USA | — | 0.71% |
| Significant | Idelsk-Uralia | Russia | — | 0.68% |
| Notable | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 0.63% |
| Notable | Ukraine |  | 0.92% | 0.60% |
| Significant (successor) | Colorado | USA | — | 0.53% |
| Notable | Quebec | Canada | — | 0.48% |
| Notable | Magna Lombardia | Italy | — | 0.44% |
| Significant (successor) | Sonora | USA + Mexico | — | 0.41% |
| Notable | Prairie Federation | Canada | — | 0.35% |
| Significant | Amazonia | Brazil | — | 0.31% |
| Notable | Catalonia | Spain | — | 0.31% |
| Significant | Siberia | Russia | — | 0.27% |
| Notable | Meridia | Italy | — | 0.27% |
| Significant | Donska-Kubania | Russia | — | 0.26% |
| Notable | Yucatán | Mexico | — | 0.19% |
| Notable (China piece) | East Turkestan | China | — | 0.19% |
| Notable | Araucanía-Patagonia | Chile + Argentina | — | 0.18% |
| Significant | Künnarantaiga | Russia | — | 0.16% |
| Significant | West Papua | Indonesia | — | 0.11% |
| Notable | Basque Country | Spain | — | 0.11% |
| Significant | Aceh | Indonesia | — | 0.11% |
| | *1 smaller row from UK* | UK | — | 0.07% |
| | *1 smaller row from Italy* | Italy | — | 0.06% |
| | *1 smaller row from South Korea* | South Korea | — | 0.06% |
| | *7 smaller rows from Russia* | Russia | — | 0.12% |
| | *1 smaller row from USA* | USA | — | 0.05% |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.03% |
| | *1 smaller row from China* | China | — | 0.03% |
| | *1 smaller row from Thailand* | Thailand | — | 0.02% |

#### Mawson

*China's pieces in window: Mongolia, Tibet, East Turkestan · new pools: Mongolia 0.09%, Austria 1.72% · Sinian draw 0.5642; fill to: United Kingdom, Australia, Indonesia, Japan, France, Korea*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | United Kingdom | UK | — | 10.03% | 72,452 |
| Significant | Australia |  | 8.29% | 9.52% | 68,731 |
| Primary | Sinian Federation | China | — | 9.07% | 65,465 |
| Significant | Indonesia |  | 7.89% | 8.69% | 62,782 |
| Significant | Japan |  | 7.48% | 8.59% | 61,961 |
| Significant | France |  | 5.29% | 6.07% | 43,827 |
| Significant | Korea | South Korea | — | 5.52% | 39,841 |
| Notable | Estonia |  | 3.17% | 3.11% | 22,485 |
| Notable | South Africa |  | 3.09% | 3.03% | 21,937 |
| Notable | Norway |  | 3.05% | 2.99% | 21,587 |
| Notable | Vietnam |  | 2.99% | 2.94% | 21,158 |
| Notable | Belarus |  | 2.93% | 2.88% | 20,789 |
| Notable | Netherlands |  | 2.92% | 2.87% | 20,673 |
| Notable | Thailand |  | 2.97% | 2.83% | 20,456 |
| Notable | Slovenia |  | 2.71% | 2.66% | 19,195 |
| Notable | Bulgaria |  | 2.68% | 2.63% | 19,006 |
| Significant | Austro-Bavaria | Germany + Austria | — | 2.01% | 14,527 |
| Notable | Czechia | Czech Republic | — | 1.54% | 11,155 |
| Significant | Germany |  | 1.86% | 1.53% | 11,066 |
| Notable | Slovakia |  | 1.55% | 1.52% | 10,967 |
| Notable | Hungary | Romania | 1.32% | 1.43% | 10,310 |
| Notable | Lithuania |  | 1.34% | 1.32% | 9,488 |
| Notable | Poland |  | 1.27% | 1.25% | 9,004 |
| Notable | Croatia |  | 1.21% | 1.19% | 8,575 |
| Notable | Latvia |  | 1.16% | 1.14% | 8,225 |
| Notable | Romania |  | 1.28% | 1.13% | 8,171 |
| Notable | Ukraine |  | 1.08% | 0.70% | 5,097 |
| Notable (China piece) | Mongolia | China | — | 0.38% | 2,712 |
| Notable | Russia (core state) | Ukraine | — | 0.36% | 2,581 |
| Notable (China piece) | East Turkestan | China | — | 0.31% | 2,251 |
| Significant | Northern Ireland | UK | — | 0.25% | 1,774 |
| Significant | West Papua | Indonesia | — | 0.16% | 1,146 |
| Significant | Aceh | Indonesia | — | 0.15% | 1,107 |
| | *1 smaller row from Thailand* | Thailand | — | 0.08% | 597 |
| | *1 smaller row from South Korea* | South Korea | — | 0.06% | 454 |
| | *1 smaller row from China* | China | — | 0.04% | 317 |

#### Temirötkel

*China's pieces in window: Tibet, East Turkestan · new pools: Luxembourg 0.17%, Kosovo 0.07%, Austria 1.72% · Sinian draw 0.5829; fill to: Indonesia, Australia, Germany, United Kingdom, Korea, France*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Sinian Federation | China | — | 9.73% | 9,082 |
| Significant | Australia |  | 8.27% | 9.51% | 8,877 |
| Significant | Indonesia |  | 8.59% | 9.48% | 8,846 |
| Significant | United Kingdom | UK | — | 8.91% | 8,320 |
| Significant | Germany |  | 8.22% | 7.93% | 7,399 |
| Significant | Korea | South Korea | — | 5.75% | 5,370 |
| Significant | France | Luxembourg | 4.82% | 5.74% | 5,362 |
| Notable | Serbia | Kosovo | 3.22% | 3.22% | 3,014 |
| Notable | Netherlands |  | 3.14% | 3.08% | 2,872 |
| Notable | Slovenia |  | 3.12% | 3.06% | 2,858 |
| Notable | Croatia |  | 3.11% | 3.05% | 2,843 |
| Significant | Austro-Bavaria | Germany + Austria | — | 3.02% | 2,817 |
| Notable | Lithuania |  | 2.81% | 2.76% | 2,573 |
| Notable | Norway |  | 2.80% | 2.75% | 2,563 |
| Notable | Belarus |  | 2.79% | 2.74% | 2,555 |
| Notable | Latvia |  | 2.76% | 2.71% | 2,526 |
| Significant | Japan |  | 2.71% | 2.66% | 2,478 |
| Notable | Romania |  | 2.81% | 2.47% | 2,305 |
| Notable | Hungary | Romania | 1.54% | 1.79% | 1,675 |
| Notable | Czechia | Czech Republic | — | 1.53% | 1,423 |
| Notable | South Africa |  | 1.54% | 1.51% | 1,406 |
| Notable | Bulgaria |  | 1.24% | 1.22% | 1,136 |
| Notable | Poland |  | 1.23% | 1.21% | 1,121 |
| Notable | Estonia |  | 1.12% | 1.10% | 1,028 |
| Notable | Ukraine |  | 1.55% | 1.01% | 940 |
| Notable | Slovakia |  | 0.63% | 0.62% | 573 |
| Notable | Russia (core state) | Ukraine | — | 0.51% | 476 |
| Notable (China piece) | East Turkestan | China | — | 0.32% | 297 |
| Significant | Northern Ireland | UK | — | 0.22% | 203 |
| Significant | West Papua | Indonesia | — | 0.17% | 161 |
| Significant | Aceh | Indonesia | — | 0.17% | 156 |
| | *1 smaller row from South Korea* | South Korea | — | 0.07% | 61 |
| | *1 smaller row from China* | China | — | 0.04% | 42 |

#### Ariun Nuur

*new pools: Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36% · from Japan: Mongolia 4.19, Künnarantaiga 3.73*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Japan |  | 24.97% | 16.21% | 22,981 |
| Significant | Indonesia |  | 13.55% | 12.57% | 17,813 |
| Significant (successor) | CSA | USA | — | 8.87% | 12,567 |
| Significant | Australia |  | 6.45% | 6.23% | 8,839 |
| Significant | Korea | South Korea + North Korea | — | 6.18% | 8,756 |
| Significant (successor) | Cascadia | USA + Canada | — | 5.99% | 8,488 |
| Significant (successor) | Appalachia | USA | — | 5.69% | 8,066 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 4.96% | 7,038 |
| Significant (successor) | New England | USA | — | 4.65% | 6,597 |
| Founder | Mongolia | Mongolia | — | 4.29% | 6,075 |
| Notable | Chile |  | 4.96% | 4.13% | 5,849 |
| Significant | Quebec | Canada | — | 3.80% | 5,381 |
| Founder | Künnarantaiga |  | — | 3.73% | 5,290 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 4,118 |
| Significant | Prairie Federation | Canada | — | 2.79% | 3,959 |
| Significant (successor) | Midwest Republic | USA | — | 1.77% | 2,509 |
| Notable | New Zealand |  | 1.71% | 1.65% | 2,340 |
| Significant (successor) | Colorado | USA | — | 1.33% | 1,886 |
| Significant (successor) | Sonora | USA | — | 0.78% | 1,109 |
| Notable | Araucanía-Patagonia | Chile | — | 0.67% | 944 |
| Significant | West Papua | Indonesia | — | 0.27% | 381 |
| Significant | Aceh | Indonesia | — | 0.26% | 368 |
| Significant (successor) | Hawaii | USA | — | 0.11% | 162 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.09% | 129 |
| | *1 smaller row from South Korea* | South Korea | — | 0.08% | 110 |

#### Casey

*China's pieces in window: Mongolia, Manchuria, Tibet, East Turkestan · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36% · Sinian draw 0.5501; fill to: CSA, Korea, France, Australia, Japan, Indonesia*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Korea | South Korea + North Korea | — | 12.00% | 89,534 |
| Significant | France |  | 10.05% | 11.27% | 84,111 |
| Significant | Australia |  | 9.26% | 10.39% | 77,438 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 9.49% | 70,816 |
| Significant (successor) | CSA | USA | — | 7.97% | 59,438 |
| Significant | Japan |  | 5.33% | 5.98% | 44,594 |
| Significant | Indonesia |  | 4.92% | 5.30% | 39,516 |
| Significant (successor) | Appalachia | USA | — | 4.36% | 32,552 |
| Significant (successor) | New England | USA | — | 3.57% | 26,625 |
| Notable | New Zealand |  | 3.36% | 3.22% | 23,961 |
| Notable | Philippines |  | 3.35% | 3.21% | 23,930 |
| Significant (successor) | Cascadia | USA | — | 3.18% | 23,716 |
| Notable | Vietnam |  | 3.21% | 3.07% | 22,905 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 21,671 |
| Significant | Idelsk-Uralia | Russia | — | 1.84% | 13,718 |
| Significant | Russia (core state) | Russia | — | 1.84% | 13,717 |
| Notable | Malaysia |  | 1.78% | 1.70% | 12,676 |
| Significant (successor) | Midwest Republic | USA | — | 1.36% | 10,122 |
| Notable (China piece) | Manchuria | China | — | 1.23% | 9,193 |
| Notable | Thailand |  | 1.13% | 1.05% | 7,813 |
| Significant (successor) | Colorado | USA | — | 1.02% | 7,613 |
| Significant | Siberia | Russia | — | 0.73% | 5,453 |
| Significant | Donska-Kubania | Russia | — | 0.70% | 5,229 |
| Significant (successor) | Sonora | USA | — | 0.60% | 4,473 |
| Significant | Künnarantaiga | Russia | — | 0.42% | 3,151 |
| Notable (China piece) | Mongolia | China | — | 0.40% | 3,006 |
| Notable (China piece) | East Turkestan | China | — | 0.34% | 2,538 |
| Significant | Jeju-do (neutral zone) | South Korea | — | 0.13% | 981 |
| Significant | Dagestan | Russia | — | 0.13% | 969 |
| | *2 smaller rows from Indonesia* | Indonesia | — | 0.19% | 1,413 |
| | *2 smaller rows from USA* | USA | — | 0.13% | 964 |
| | *7 smaller rows from Russia* | Russia | — | 0.20% | 1,511 |
| | *1 smaller row from China* | China | — | 0.05% | 359 |
| | *1 smaller row from Thailand* | Thailand | — | 0.03% | 229 |

#### Davis

*China's pieces in window: Mongolia, Manchuria, Tibet, East Turkestan · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36% · Sinian draw 0.5719; fill to: Japan, Germany, United Kingdom, Korea, Indonesia, Australia*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Japan |  | 9.36% | 10.57% | 60,876 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 9.86% | 56,759 |
| Significant | United Kingdom | UK | — | 9.50% | 54,692 |
| Significant | Germany |  | 9.15% | 8.67% | 49,915 |
| Significant | Korea | South Korea + North Korea | — | 8.39% | 48,278 |
| Significant | Indonesia |  | 5.14% | 5.57% | 32,084 |
| Significant | Australia |  | 4.93% | 5.57% | 32,064 |
| Notable | Thailand |  | 3.52% | 3.27% | 18,842 |
| Notable | Vietnam |  | 3.29% | 3.15% | 18,126 |
| Notable | Philippines |  | 3.25% | 3.11% | 17,906 |
| Notable | Malaysia |  | 3.13% | 3.00% | 17,246 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 16,725 |
| Significant | Russia (core state) | Russia + Ukraine | — | 2.82% | 16,244 |
| Notable | South Africa |  | 2.92% | 2.79% | 16,087 |
| Notable | Romania |  | 2.97% | 2.55% | 14,680 |
| Notable | Ukraine |  | 3.51% | 2.23% | 12,838 |
| Notable | New Zealand |  | 1.79% | 1.71% | 9,861 |
| Significant | Idelsk-Uralia | Russia | — | 1.69% | 9,746 |
| Notable | Belarus |  | 1.63% | 1.56% | 8,981 |
| Notable | Bulgaria |  | 1.51% | 1.45% | 8,319 |
| Significant | Austro-Bavaria | Germany | — | 1.41% | 8,128 |
| Notable (China piece) | Manchuria | China | — | 1.23% | 7,087 |
| Notable | Lithuania |  | 1.25% | 1.20% | 6,887 |
| Notable | Estonia |  | 1.24% | 1.19% | 6,833 |
| Notable | Latvia |  | 0.94% | 0.90% | 5,179 |
| Significant | Siberia | Russia | — | 0.67% | 3,873 |
| Significant | Donska-Kubania | Russia | — | 0.65% | 3,715 |
| Notable (China piece) | Mongolia | China | — | 0.40% | 2,318 |
| Significant | Künnarantaiga | Russia | — | 0.39% | 2,237 |
| Notable (China piece) | East Turkestan | China | — | 0.34% | 1,957 |
| Notable | Hungary | Romania | — | 0.29% | 1,683 |
| Significant | Northern Ireland | UK | — | 0.23% | 1,327 |
| Significant | Dagestan | Russia | — | 0.12% | 687 |
| Significant | West Papua | Indonesia | — | 0.10% | 580 |
| | *1 smaller row from Indonesia* | Indonesia | — | 0.10% | 560 |
| | *1 smaller row from Thailand* | Thailand | — | 0.10% | 551 |
| | *1 smaller row from South Korea* | South Korea | — | 0.09% | 517 |
| | *7 smaller rows from Russia* | Russia | — | 0.19% | 1,074 |
| | *1 smaller row from China* | China | — | 0.05% | 276 |

#### Kunlun

| Tier | Row | From | Before | After |
|---|---|---|--:|--:|
| Primary | Sinian Federation |  | — | 15.09% |
| Significant | Canada |  | 7.19% | 7.74% |
| Significant | Japan |  | 6.75% | 7.26% |
| Significant | UK |  | 6.48% | 6.97% |
| Significant | Intermarium/Intermaria |  | 6.38% | 6.86% |
| Significant | USA |  | 15.43% | 5.66% |
| Significant | Russia |  | 11.45% | 5.66% |
| Significant (founding wave) | Mongolia |  | — | 5.66% |
| Significant (founding wave) | Künnarantaiga |  | — | 5.66% |
| Significant | Italy |  | 5.26% | 5.66% |
| Significant | South Korea |  | 4.05% | 4.36% |
| Significant | Germany |  | 3.33% | 3.58% |
| Significant | France |  | 2.65% | 2.85% |
| Notable | New Zealand |  | 2.47% | 2.65% |
| Notable | Argentina |  | 2.44% | 2.62% |
| Notable | Sweden |  | 2.37% | 2.55% |
| Notable | Australia |  | 2.35% | 2.53% |
| Notable | Chile |  | 2.14% | 2.30% |
| Notable | Norway |  | 1.75% | 1.88% |
| Notable | Spain |  | 1.16% | 1.25% |
| Notable | South Africa |  | 1.07% | 1.15% |
| Notable | Netherlands |  | 0.05% | 0.05% |

#### Mirny

*China's pieces in window: Mongolia, Manchuria, Tibet, East Turkestan · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36% · Sinian draw 0.5616; fill to: United Kingdom, Korea, Indonesia, Japan, Australia*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | United Kingdom | UK | — | 13.93% | 94,459 |
| Significant | Korea | South Korea + North Korea | — | 13.77% | 93,357 |
| Significant | Indonesia |  | 10.96% | 12.21% | 82,735 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 12.18% | 82,588 |
| Significant | Japan |  | 6.54% | 7.59% | 51,449 |
| Significant | Australia |  | 5.83% | 6.76% | 45,880 |
| Notable | Philippines |  | 4.50% | 4.31% | 29,222 |
| Notable | New Zealand |  | 4.48% | 4.29% | 29,067 |
| Notable | Malaysia |  | 3.65% | 3.49% | 23,659 |
| Notable | Thailand |  | 3.70% | 3.44% | 23,296 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 19,698 |
| Significant | Idelsk-Uralia | Russia | — | 2.17% | 14,700 |
| Significant | Russia (core state) | Russia | — | 2.17% | 14,700 |
| Notable | Vietnam |  | 1.75% | 1.67% | 11,352 |
| Notable (China piece) | Manchuria | China | — | 1.57% | 10,627 |
| Notable | Belarus |  | 1.58% | 1.51% | 10,257 |
| Notable | South Africa |  | 1.56% | 1.49% | 10,102 |
| Significant | Siberia | Russia | — | 0.86% | 5,844 |
| Significant | Donska-Kubania | Russia | — | 0.83% | 5,603 |
| Significant | Künnarantaiga | Russia | — | 0.50% | 3,377 |
| Notable (China piece) | Mongolia | China | — | 0.49% | 3,300 |
| Notable (China piece) | East Turkestan | China | — | 0.43% | 2,933 |
| Significant | Northern Ireland | UK | — | 0.33% | 2,231 |
| Significant | West Papua | Indonesia | — | 0.21% | 1,457 |
| Significant | Aceh | Indonesia | — | 0.21% | 1,407 |
| Significant | Dagestan | Russia | — | 0.15% | 1,038 |
| Significant | Jeju-do (neutral zone) | South Korea | — | 0.15% | 991 |
| Notable | Patani | Thailand | — | 0.10% | 681 |
| | *7 smaller rows from Russia* | Russia | — | 0.24% | 1,616 |
| | *1 smaller row from China* | China | — | 0.06% | 415 |

#### Relung Panen

*China's pieces in window: Mongolia, Manchuria, Tibet, East Turkestan · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36% · Sinian draw 0.6195; fill to: Indonesia, Japan, Korea, Australia, Thailand, Vietnam*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Japan |  | 11.98% | 13.05% | 62,264 |
| Significant | Indonesia |  | 12.23% | 12.78% | 61,004 |
| Significant | Korea | South Korea + North Korea | — | 12.47% | 59,506 |
| Primary | Sinian Federation | China + Hong Kong + Macau | — | 12.03% | 57,396 |
| Significant | Australia |  | 11.03% | 12.01% | 57,327 |
| Notable | Thailand |  | 5.15% | 5.45% | 26,007 |
| Notable | Vietnam |  | 4.76% | 5.18% | 24,739 |
| Significant | Idelsk-Uralia | Russia | — | 3.78% | 18,048 |
| Significant | Russia (core state) | Russia | — | 3.78% | 18,046 |
| Notable | Malaysia |  | 3.30% | 3.16% | 15,073 |
| Notable | Philippines |  | 3.18% | 3.04% | 14,524 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 13,866 |
| Notable | New Zealand |  | 2.97% | 2.84% | 13,566 |
| Significant | Siberia | Russia | — | 1.50% | 7,174 |
| Significant | Donska-Kubania | Russia | — | 1.44% | 6,877 |
| Notable (China piece) | Manchuria | China | — | 1.40% | 6,659 |
| Significant | Künnarantaiga | Russia | — | 0.87% | 4,145 |
| Notable (China piece) | Mongolia | China | — | 0.44% | 2,117 |
| Notable (China piece) | East Turkestan | China | — | 0.39% | 1,837 |
| Significant | Dagestan | Russia | — | 0.27% | 1,275 |
| Significant | West Papua | Indonesia | — | 0.24% | 1,143 |
| Significant | Aceh | Indonesia | — | 0.23% | 1,106 |
| Significant | Jeju-do (neutral zone) | South Korea | — | 0.14% | 673 |
| Notable | Patani | Thailand | — | 0.14% | 668 |
| Significant | Chechnya | Russia | — | 0.13% | 604 |
| | *6 smaller rows from Russia* | Russia | — | 0.29% | 1,381 |
| | *1 smaller row from China* | China | — | 0.05% | 260 |

#### Shirayuki

*China's pieces in window: Mongolia, Manchuria, Tibet, East Turkestan · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36% · Sinian draw 0.6427; fill to: Australia, Korea*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Japan |  | 36.27% | 34.71% | 184,290 |
| Significant | Australia |  | 8.76% | 9.69% | 51,473 |
| Significant | Korea | South Korea + North Korea | — | 9.03% | 47,965 |
| Significant | Sinian Federation | China + Hong Kong + Macau | — | 4.56% | 24,191 |
| Significant | Germany |  | 4.93% | 3.96% | 21,011 |
| Significant | Russia (core state) | Russia + Ukraine | — | 3.58% | 19,029 |
| Notable | Romania |  | 3.54% | 3.04% | 16,137 |
| Notable | Vietnam |  | 3.16% | 3.02% | 16,057 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 15,424 |
| Notable | Belarus |  | 3.00% | 2.87% | 15,244 |
| Notable | New Zealand |  | 2.97% | 2.84% | 15,091 |
| Notable | Thailand |  | 2.99% | 2.78% | 14,760 |
| Significant | Idelsk-Uralia | Russia | — | 2.58% | 13,720 |
| Notable | Ukraine |  | 3.11% | 1.98% | 10,490 |
| Notable | Lithuania |  | 1.76% | 1.68% | 8,943 |
| Notable | South Africa |  | 1.66% | 1.59% | 8,434 |
| Notable | Bulgaria |  | 1.60% | 1.53% | 8,131 |
| Notable | Latvia |  | 1.35% | 1.29% | 6,860 |
| Notable | Estonia |  | 1.22% | 1.17% | 6,200 |
| Significant | Siberia | Russia | — | 1.03% | 5,454 |
| Significant | Donska-Kubania | Russia | — | 0.98% | 5,229 |
| Significant | Austro-Bavaria | Germany | — | 0.76% | 4,038 |
| Significant | Künnarantaiga | Russia | — | 0.59% | 3,151 |
| Notable (China piece) | Manchuria | China | — | 0.46% | 2,466 |
| Notable | Hungary | Romania | — | 0.35% | 1,850 |
| Notable (China piece) | Mongolia | China | — | 0.21% | 1,112 |
| Significant | Dagestan | Russia | — | 0.18% | 969 |
| Notable (China piece) | East Turkestan | China | — | 0.13% | 680 |
| | *1 smaller row from South Korea* | South Korea | — | 0.10% | 525 |
| | *7 smaller rows from Russia* | Russia | — | 0.28% | 1,509 |
| | *1 smaller row from Thailand* | Thailand | — | 0.08% | 432 |
| | *1 smaller row from China* | China | — | 0.02% | 96 |

#### Sinheung

*China's pieces in window: Mongolia, Manchuria, Tibet, East Turkestan · new pools: Hong Kong 0.88%, Macau 0.10%, Taiwan 2.92%, Mongolia 0.09%, North Korea 0.36% · Sinian draw 0.5888; fill to: Japan, Germany*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Korea | South Korea + North Korea | — | 33.06% | 158,474 |
| Significant | Japan |  | 7.78% | 9.42% | 45,163 |
| Significant | Germany |  | 8.64% | 8.78% | 42,070 |
| Significant | Sinian Federation | China + Hong Kong + Macau | — | 5.46% | 26,194 |
| Significant | Indonesia |  | 4.41% | 4.05% | 19,419 |
| Significant | Australia |  | 3.57% | 3.42% | 16,379 |
| Notable | Thailand |  | 3.65% | 3.39% | 16,270 |
| Notable | Estonia |  | 3.52% | 3.37% | 16,149 |
| Notable | Hungary |  | 3.43% | 3.28% | 15,735 |
| Notable | Lithuania |  | 3.11% | 2.98% | 14,268 |
| New (time-zone window) | Taiwan | Taiwan | — | 2.91% | 13,928 |
| Notable | Malaysia |  | 2.93% | 2.80% | 13,442 |
| Significant | Idelsk-Uralia | Russia | — | 2.06% | 9,855 |
| Significant | Russia (core state) | Russia | — | 2.06% | 9,855 |
| Notable | Vietnam |  | 1.95% | 1.87% | 8,946 |
| Notable | Philippines |  | 1.77% | 1.69% | 8,121 |
| Notable | Bulgaria |  | 1.45% | 1.39% | 6,651 |
| Significant | Austro-Bavaria | Germany | — | 1.33% | 6,391 |
| Notable | Latvia |  | 1.35% | 1.29% | 6,194 |
| Notable | South Africa |  | 1.23% | 1.18% | 5,643 |
| Significant | Siberia | Russia | — | 0.82% | 3,918 |
| Significant | Donska-Kubania | Russia | — | 0.78% | 3,755 |
| Notable (China piece) | Manchuria | China | — | 0.63% | 3,019 |
| Significant | Künnarantaiga | Russia | — | 0.47% | 2,264 |
| Significant (successor) | Jeju-do (neutral zone) | South Korea | — | 0.43% | 2,084 |
| Notable (China piece) | Mongolia | China | — | 0.25% | 1,205 |
| Notable (China piece) | East Turkestan | China | — | 0.17% | 833 |
| Significant | Dagestan | Russia | — | 0.15% | 694 |
| | *1 smaller row from Thailand* | Thailand | — | 0.10% | 475 |
| | *2 smaller rows from Indonesia* | Indonesia | — | 0.17% | 814 |
| | *7 smaller rows from Russia* | Russia | — | 0.23% | 1,086 |
| | *1 smaller row from China* | China | — | 0.02% | 117 |

#### Zhongshan

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Sinian Federation |  | — | 35.83% | 208,145 |
| Significant | Korea | South Korea | — | 9.57% | 55,611 |
| Significant | Japan |  | 7.30% | 7.30% | 42,408 |
| Significant | Germany |  | 8.47% | 7.10% | 41,271 |
| Significant | Australia |  | 3.66% | 3.66% | 21,262 |
| Notable | Vietnam |  | 3.56% | 3.56% | 20,681 |
| Notable | Estonia |  | 3.55% | 3.55% | 20,622 |
| Notable | Lithuania |  | 3.14% | 3.14% | 18,241 |
| Notable | Thailand |  | 3.18% | 3.09% | 17,948 |
| Notable | Malaysia |  | 3.04% | 3.04% | 17,660 |
| Notable | Indonesia |  | 2.98% | 2.86% | 16,615 |
| Notable | Romania |  | 2.88% | 2.58% | 15,009 |
| Significant | Idelsk-Uralia | Russia | — | 1.79% | 10,421 |
| Significant | Russia (core state) | Russia | — | 1.79% | 10,420 |
| Notable | Philippines |  | 1.72% | 1.72% | 9,992 |
| Notable | Latvia |  | 1.58% | 1.58% | 9,178 |
| Significant | Austro-Bavaria | Germany | — | 1.37% | 7,933 |
| Notable | New Zealand |  | 1.28% | 1.28% | 7,435 |
| Notable | Bulgaria |  | 1.21% | 1.21% | 7,029 |
| Notable | South Africa |  | 1.20% | 1.20% | 6,972 |
| Significant | Siberia | Russia | — | 0.71% | 4,142 |
| Significant | Donska-Kubania | Russia | — | 0.68% | 3,972 |
| Significant | Künnarantaiga | Russia | — | 0.41% | 2,393 |
| Notable | Hungary | Romania | — | 0.30% | 1,722 |
| Significant | Jeju-do (neutral zone) | South Korea | — | 0.13% | 740 |
| Significant | Dagestan | Russia | — | 0.13% | 736 |
| | *1 smaller row from Thailand* | Thailand | — | 0.09% | 525 |
| | *2 smaller rows from Indonesia* | Indonesia | — | 0.12% | 697 |
| | *7 smaller rows from Russia* | Russia | — | 0.20% | 1,145 |

#### Contrapunto

*new pools: Petén 0.05%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France |  | 11.62% | 11.61% | 36,781 |
| Significant | United Kingdom | UK | — | 10.98% | 34,776 |
| Significant | México | Mexico | — | 9.10% | 28,826 |
| Significant | Germany |  | 10.72% | 8.99% | 28,467 |
| Significant (successor) | CSA | USA | — | 7.00% | 22,170 |
| Significant | Brazil |  | 6.69% | 6.02% | 19,073 |
| Significant | Korea | South Korea | — | 5.71% | 18,086 |
| Significant (successor) | Appalachia | USA | — | 4.49% | 14,230 |
| Notable | Argentina (without Patagonia) | Argentina | — | 4.02% | 12,719 |
| Significant (successor) | Cascadia | USA + Mexico | — | 3.68% | 11,661 |
| Significant (successor) | New England | USA | — | 3.67% | 11,638 |
| Significant | Magna Lombardia | Italy | — | 3.49% | 11,049 |
| Notable | Chile |  | 3.53% | 3.04% | 9,623 |
| Significant | Meridia | Italy | — | 2.14% | 6,782 |
| Significant | Idelsk-Uralia | Russia | — | 1.92% | 6,074 |
| Significant | Russia (core state) | Russia | — | 1.92% | 6,073 |
| Significant | Austro-Bavaria | Germany | — | 1.73% | 5,471 |
| Significant (successor) | Midwest Republic | USA | — | 1.40% | 4,425 |
| Significant | Yucatán | Mexico + Petén | — | 1.22% | 3,854 |
| Significant (successor) | Sonora | USA + Mexico | — | 1.22% | 3,850 |
| Significant (successor) | Colorado | USA | — | 1.05% | 3,328 |
| Notable | Uruguay |  | 0.91% | 0.91% | 2,881 |
| Significant | Siberia | Russia | — | 0.76% | 2,414 |
| Notable | Araucanía-Patagonia | Argentina + Chile | — | 0.73% | 2,317 |
| Significant | Donska-Kubania | Russia | — | 0.73% | 2,315 |
| Significant | Amazonia | Brazil | — | 0.66% | 2,104 |
| Significant | Sicilia (autonomous zone within Meridia) | Italy | — | 0.50% | 1,572 |
| Significant | Künnarantaiga | Russia | — | 0.44% | 1,394 |
| Significant | Northern Ireland | UK | — | 0.31% | 996 |
| Significant | Dagestan | Russia | — | 0.14% | 429 |
| | *2 smaller rows from USA* | USA | — | 0.13% | 421 |
| | *1 smaller row from South Korea* | South Korea | — | 0.08% | 241 |
| | *7 smaller rows from Russia* | Russia | — | 0.21% | 668 |

#### Esperanza

*new pools: Petén 0.05%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 18.92% | 17.03% | 164,816 |
| Significant | México | Mexico | — | 14.08% | 136,162 |
| Significant (successor) | CSA | USA | — | 11.76% | 113,750 |
| Significant | United Kingdom | UK | — | 9.55% | 92,379 |
| Significant | Argentina (without Patagonia) | Argentina | — | 7.87% | 76,144 |
| Significant (successor) | Appalachia | USA | — | 7.55% | 73,011 |
| Notable | Uruguay |  | 6.60% | 6.60% | 63,812 |
| Significant (successor) | New England | USA | — | 6.17% | 59,716 |
| Significant (successor) | Cascadia | USA + Mexico | — | 6.13% | 59,305 |
| Significant (successor) | Midwest Republic | USA | — | 2.35% | 22,705 |
| Notable | Chile |  | 2.49% | 2.14% | 20,752 |
| Significant (successor) | Sonora | USA + Mexico | — | 1.96% | 18,982 |
| Significant | Amazonia | Brazil | — | 1.88% | 18,182 |
| Significant | Yucatán | Mexico + Petén | — | 1.86% | 17,946 |
| Significant (successor) | Colorado | USA | — | 1.76% | 17,076 |
| Significant | Araucanía-Patagonia | Argentina + Chile | — | 0.82% | 7,932 |
| Significant | Northern Ireland | UK | — | 0.27% | 2,646 |
| Significant (successor) | Hawaii | USA | — | 0.15% | 1,474 |
| | *1 smaller row from USA* | USA | — | 0.07% | 687 |

#### Marambio

*new pools: Petén 0.05%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | United Kingdom | UK | — | 13.10% | 37,117 |
| Significant | México | Mexico | — | 11.37% | 32,245 |
| Significant | Spain |  | 14.19% | 10.99% | 31,128 |
| Significant (successor) | CSA | USA | — | 8.92% | 25,282 |
| Significant | Brazil |  | 6.50% | 5.85% | 16,595 |
| Significant (successor) | Appalachia | USA | — | 5.73% | 16,227 |
| Significant (successor) | Cascadia | USA + Mexico + Canada | — | 5.67% | 16,071 |
| Significant | Germany |  | 6.59% | 5.52% | 15,654 |
| Notable | Uruguay |  | 4.74% | 4.74% | 13,420 |
| Significant (successor) | New England | USA | — | 4.68% | 13,272 |
| Notable | Chile |  | 4.87% | 4.19% | 11,872 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.66% | 7,552 |
| Significant | Catalonia | Spain | — | 2.35% | 6,666 |
| Significant | Quebec | Canada | — | 2.04% | 5,775 |
| Significant (successor) | Midwest Republic | USA | — | 1.78% | 5,047 |
| Significant (successor) | Sonora | USA + Mexico | — | 1.53% | 4,349 |
| Significant | Yucatán | Mexico + Petén | — | 1.51% | 4,276 |
| Significant | Prairie Federation | Canada | — | 1.50% | 4,248 |
| Significant (successor) | Colorado | USA | — | 1.34% | 3,795 |
| Significant | Austro-Bavaria | Germany | — | 1.06% | 3,010 |
| Significant | Basque Country | Spain | — | 0.85% | 2,396 |
| Notable | Araucanía-Patagonia | Chile + Argentina | — | 0.72% | 2,033 |
| Notable | Argentina (without Patagonia) | Argentina | — | 0.70% | 1,982 |
| Significant | Amazonia | Brazil | — | 0.65% | 1,831 |
| Significant | Northern Ireland | UK | — | 0.38% | 1,062 |
| Significant (successor) | Hawaii | USA | — | 0.12% | 328 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.07% | 211 |

#### Palmer City

*new pools: Petén 0.05% · Sinian draw 0.6378; fill to: CSA, Brazil, France, Germany, México, United Kingdom*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France | Belgium | 9.54% | 10.09% | 16,738 |
| Significant | Brazil |  | 9.68% | 8.78% | 14,564 |
| Significant | Germany |  | 9.51% | 8.03% | 13,325 |
| Significant (successor) | CSA | USA | — | 6.61% | 10,968 |
| Significant | United Kingdom | UK | — | 5.42% | 9,001 |
| Significant | México | Mexico | — | 4.64% | 7,701 |
| Significant (successor) | Appalachia | USA | — | 4.21% | 6,987 |
| Significant (successor) | Cascadia | USA + Mexico + Canada | — | 4.05% | 6,725 |
| Notable | Uruguay |  | 3.70% | 3.70% | 6,138 |
| Significant (successor) | New England | USA | — | 3.44% | 5,714 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.88% | 4,771 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.10% | 3,481 |
| Significant | Quebec | Canada | — | 1.60% | 2,662 |
| Significant | Austro-Bavaria | Germany | — | 1.53% | 2,542 |
| Notable | Netherlands | Belgium | 0.76% | 1.42% | 2,358 |
| Notable | Estonia |  | 1.39% | 1.39% | 2,311 |
| Notable | Czechia | Czech Republic | — | 1.35% | 2,246 |
| Notable | Australia |  | 1.33% | 1.33% | 2,206 |
| Significant (successor) | Midwest Republic | USA | — | 1.31% | 2,173 |
| Notable | Slovakia |  | 1.29% | 1.29% | 2,141 |
| Notable | Thailand |  | 1.26% | 1.22% | 2,029 |
| Significant | Prairie Federation | Canada | — | 1.18% | 1,958 |
| Notable | Serbia |  | 1.16% | 1.16% | 1,930 |
| Notable | Korea | South Korea | — | 1.08% | 1,788 |
| Notable | Norway |  | 1.01% | 1.01% | 1,668 |
| Significant (successor) | Colorado | USA | — | 0.98% | 1,634 |
| Notable | Croatia |  | 0.97% | 0.97% | 1,602 |
| Significant | Amazonia | Brazil | — | 0.96% | 1,594 |
| Notable | South Africa |  | 0.96% | 0.96% | 1,589 |
| Significant (successor) | Sonora | USA + Mexico | — | 0.88% | 1,462 |
| Notable | Slovenia |  | 0.86% | 0.86% | 1,431 |
| Notable | Philippines |  | 0.82% | 0.82% | 1,352 |
| Notable | Romania |  | 0.86% | 0.77% | 1,272 |
| Notable | Chile |  | 0.86% | 0.74% | 1,224 |
| Notable | Japan |  | 0.73% | 0.73% | 1,208 |
| Notable | Poland |  | 0.70% | 0.70% | 1,168 |
| Notable | New Zealand |  | 0.67% | 0.67% | 1,116 |
| Significant | Yucatán | Mexico + Petén | — | 0.64% | 1,062 |
| Notable | Bulgaria |  | 0.62% | 0.62% | 1,024 |
| Notable | Magna Lombardia | Italy | — | 0.60% | 1,002 |
| Notable | Sinian Federation | China | — | 0.58% | 963 |
| Notable | Vietnam |  | 0.58% | 0.58% | 958 |
| Notable | Russia (core state) | Russia + Ukraine | — | 0.49% | 820 |
| Notable | Latvia |  | 0.48% | 0.48% | 802 |
| Notable | Sweden |  | 0.46% | 0.46% | 762 |
| Notable | Belarus |  | 0.44% | 0.44% | 723 |
| Notable | Spain |  | 0.53% | 0.41% | 682 |
| Notable | Idelsk-Uralia | Russia | — | 0.38% | 626 |
| Notable | Meridia | Italy | — | 0.37% | 615 |
| Notable | Indonesia |  | 0.38% | 0.36% | 606 |
| Notable | Finland | Russia | 0.32% | 0.32% | 546 |
| Notable | Hungary | Romania | 0.23% | 0.32% | 527 |
| Notable | Araucanía-Patagonia | Argentina + Chile | — | 0.29% | 485 |
| Notable | Lithuania |  | 0.28% | 0.28% | 460 |
| Notable | Malaysia |  | 0.25% | 0.25% | 407 |
| Notable | Ukraine |  | 0.35% | 0.23% | 384 |
| Significant | Northern Ireland | UK | — | 0.15% | 256 |
| Notable | Siberia | Russia | — | 0.15% | 249 |
| Notable | Donska-Kubania | Russia | — | 0.14% | 239 |
| | *2 smaller rows from Spain* | Spain | — | 0.12% | 198 |
| | *8 smaller rows from Russia* | Russia | — | 0.15% | 250 |
| | *1 smaller row from Italy* | Italy | — | 0.09% | 143 |
| | *1 smaller row from USA* | USA | — | 0.09% | 141 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.06% | 93 |
| | *1 smaller row from Thailand* | Thailand | — | 0.04% | 59 |
| | *1 smaller row from South Korea* | South Korea | — | 0.01% | 24 |
| | *2 smaller rows from Indonesia* | Indonesia | — | 0.02% | 25 |

#### Pergamino

*new pools: Petén 0.05%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | United Kingdom | UK | — | 13.33% | 25,288 |
| Significant | Spain |  | 14.06% | 10.88% | 20,655 |
| Significant (successor) | CSA | USA | — | 9.58% | 18,177 |
| Significant | France |  | 8.51% | 8.51% | 16,133 |
| Significant | Magna Lombardia | Italy | — | 8.10% | 15,381 |
| Significant (successor) | Appalachia | USA | — | 6.15% | 11,667 |
| Significant (successor) | New England | USA | — | 5.03% | 9,542 |
| Significant | Meridia | Italy | — | 4.98% | 9,442 |
| Notable | Argentina (without Patagonia) | Argentina | — | 4.75% | 9,008 |
| Significant (successor) | Cascadia | USA + Mexico | — | 4.58% | 8,682 |
| Significant | Germany |  | 5.03% | 4.22% | 8,001 |
| Notable | Chile |  | 4.76% | 4.10% | 7,769 |
| Significant | Catalonia | Spain | — | 2.33% | 4,423 |
| Notable | México | Mexico | — | 2.14% | 4,056 |
| Notable | Brazil |  | 2.37% | 2.13% | 4,050 |
| Significant (successor) | Midwest Republic | USA | — | 1.91% | 3,628 |
| Significant (successor) | Colorado | USA | — | 1.44% | 2,729 |
| Significant | Sicilia (autonomous zone within Meridia) | Italy | — | 1.15% | 2,188 |
| Significant (successor) | Sonora | USA + Mexico | — | 0.99% | 1,870 |
| Notable | Araucanía-Patagonia | Argentina + Chile | — | 0.95% | 1,796 |
| Significant | Basque Country | Spain | — | 0.84% | 1,589 |
| Significant | Austro-Bavaria | Germany | — | 0.81% | 1,538 |
| Significant | Northern Ireland | UK | — | 0.38% | 724 |
| Notable | Yucatán | Mexico + Petén | — | 0.32% | 613 |
| Notable | Amazonia | Brazil | — | 0.24% | 447 |
| Significant (successor) | Hawaii | USA | — | 0.12% | 236 |
| | *1 smaller row from USA* | USA | — | 0.06% | 110 |

#### Puerto Abrigo

*new pools: Petén 0.05%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France |  | 16.71% | 16.70% | 77 |
| Significant | United Kingdom | UK | — | 13.94% | 64 |
| Significant | Germany |  | 14.83% | 12.43% | 57 |
| Significant (successor) | CSA | USA | — | 10.35% | 47 |
| Significant | Brazil |  | 9.65% | 8.69% | 40 |
| Significant (successor) | Appalachia | USA | — | 6.64% | 30 |
| Significant (successor) | New England | USA | — | 5.43% | 25 |
| Significant (successor) | Cascadia | USA + Mexico | — | 5.00% | 23 |
| Notable | Chile |  | 5.74% | 4.94% | 22 |
| Significant | México | Mexico | — | 3.60% | 16 |
| Significant | Austro-Bavaria | Germany | — | 2.39% | 11 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.13% | 9 |
| Significant (successor) | Midwest Republic | USA | — | 2.07% | 10 |
| Significant (successor) | Colorado | USA | — | 1.55% | 7 |
| Significant (successor) | Sonora | USA + Mexico | — | 1.15% | 5 |
| Significant | Amazonia | Brazil | — | 0.96% | 4 |
| Notable | Araucanía-Patagonia | Chile + Argentina | — | 0.93% | 5 |
| Significant | Yucatán | Mexico + Petén | — | 0.51% | 2 |
| Significant | Northern Ireland | UK | — | 0.40% | 2 |
| Significant (successor) | Hawaii | USA | — | 0.13% | 1 |
| | *1 smaller row from USA* | USA | — | 0.06% | 0 |

#### Rothera

*new pools: Petén 0.05%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 14.00% | 12.60% | 19,377 |
| Significant | Germany |  | 14.31% | 12.00% | 18,444 |
| Significant (successor) | CSA | USA | — | 9.24% | 14,204 |
| Significant | France |  | 7.43% | 7.43% | 11,417 |
| Significant | United Kingdom | UK | — | 6.92% | 10,638 |
| Significant (successor) | Cascadia | USA + Canada + Mexico | — | 6.54% | 10,051 |
| Significant (successor) | Appalachia | USA | — | 5.93% | 9,118 |
| Significant | México | Mexico | — | 5.75% | 8,845 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 5.28% | 8,121 |
| Significant (successor) | New England | USA | — | 4.85% | 7,456 |
| Notable | Chile |  | 5.23% | 4.50% | 6,924 |
| Significant | Quebec | Canada | — | 4.04% | 6,210 |
| Significant | Prairie Federation | Canada | — | 2.97% | 4,569 |
| Significant | Austro-Bavaria | Germany | — | 2.31% | 3,545 |
| Significant (successor) | Midwest Republic | USA | — | 1.84% | 2,836 |
| Notable | Argentina (without Patagonia) | Argentina | — | 1.80% | 2,771 |
| Significant | Amazonia | Brazil | — | 1.39% | 2,138 |
| Significant (successor) | Colorado | USA | — | 1.39% | 2,132 |
| Significant (successor) | Sonora | USA + Mexico | — | 1.19% | 1,834 |
| Notable | Araucanía-Patagonia | Chile + Argentina | — | 0.83% | 1,283 |
| Significant | Yucatán | Mexico + Petén | — | 0.79% | 1,210 |
| Significant | Northern Ireland | UK | — | 0.20% | 305 |
| Significant (successor) | Hawaii | USA | — | 0.12% | 184 |
| | *1 smaller row from USA + Canada* | USA + Canada | — | 0.10% | 148 |

#### Signy

*new pools: Luxembourg 0.17%*

| Tier | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France | Luxembourg | 17.19% | 17.33% | 16,145 |
| Significant | United Kingdom | UK | — | 16.46% | 15,329 |
| Significant (successor) | CSA | USA | — | 10.76% | 10,026 |
| Significant | Brazil |  | 8.04% | 7.23% | 6,732 |
| Significant (successor) | Appalachia | USA | — | 6.91% | 6,435 |
| Significant | Germany |  | 7.81% | 6.54% | 6,088 |
| Notable | Argentina (without Patagonia) | Argentina | — | 5.72% | 5,328 |
| Significant (successor) | New England | USA | — | 5.65% | 5,263 |
| Notable | South Africa |  | 5.47% | 5.46% | 5,081 |
| Significant (successor) | Cascadia | USA | — | 5.03% | 4,688 |
| Notable | Chile |  | 2.87% | 2.47% | 2,296 |
| Notable | Uruguay |  | 2.26% | 2.26% | 2,099 |
| Significant (successor) | Midwest Republic | USA | — | 2.15% | 2,002 |
| Significant (successor) | Colorado | USA | — | 1.62% | 1,504 |
| Significant | Austro-Bavaria | Germany | — | 1.26% | 1,170 |
| Significant (successor) | Sonora | USA | — | 0.95% | 883 |
| Significant | Amazonia | Brazil | — | 0.80% | 743 |
| Notable | Araucanía-Patagonia | Argentina + Chile | — | 0.74% | 691 |
| Significant | Northern Ireland | UK | — | 0.47% | 439 |
| Significant (successor) | Hawaii | USA | — | 0.14% | 130 |
| | *1 smaller row from USA* | USA | — | 0.06% | 61 |

*Every row, every census column: `12_city_tables.csv`.*
