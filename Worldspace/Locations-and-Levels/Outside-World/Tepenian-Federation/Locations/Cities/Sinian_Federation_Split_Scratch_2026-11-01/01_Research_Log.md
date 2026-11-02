# Research log: Sinian Federation split populations (2026-11-01, from ~21:35)

**Question researched against:** the official population (and GDP per person) of every present-day unit that
canon assigns to the Sinian Federation, Manchuria, Mongolia, East Turkestan, Tibet and Taiwan (borders in
`00_README.md`).

**Rules:** full-research law (no recalled figures; a second source or angle for figures where one exists; log
every search verbatim and every dead end, with whether it died at the query or at the source). Searches were run
by the main session itself, with no agents. The search count is kept below. This file records what was looked at;
conclusions are in `03_Results.md`.

## Part 1: China and its neighbors

### Searches (verbatim, in order)

| # | Search string | Result |
|--:|---|---|
| 1 | `Seventh National Population Census communiqué No. 3 population of regions provinces 2020 stats.gov.cn` | Found NBS English communiqué No. 3 (P1) |
| 2 | `China Statistical Yearbook 2025 year-end population by region 2024 province table` | Found the yearbook's table list (Table 2-5); the table itself was not in the snippets |
| 3 | `NBS statistical communiqué 2025 national economic and social development population end of 2025` | Found the 2025 communiqué (P3) and the 2025 1% sample-survey communiqué (P2) |
| 4 | `China Statistical Yearbook 2026 published population at year-end by region 2025` | No 2026 yearbook found online (died at the source: not yet published, or not indexed). Snippet: Hainan 10.55 million at end-2025 |
| 5 | `2024年末 常住人口 分省 31个省份 国家统计局 年鉴 2025 分地区年末人口数` | Media compilations of 2025 provincial figures (P6, P7 and others); no single official 2025 table |
| 6 | `Hong Kong population end-2024 Census and Statistics Department provisional figure` | S8: provisional 7,534,200 (Feb 2025), revised 7,500,600 (Aug 2025) |
| 7 | `Macao total population end of 2024 DSEC statistics` | S9: 688,300 |
| 8 | `Mongolia population end of 2024 National Statistics Office 1212.mn` | S10: aggregators only (CEIC 3.5M; Trading Economics 3.54M, both citing the NSO); 1212.mn not in results |
| 9 | `Taiwan population end of December 2024 Ministry of the Interior household registration` | End-2025 23,299,132, down 101,088 from end-2024 (implies 23,400,220) |
| 10 | `Montsame population of Mongolia reached 2024 year end National Statistics Office million` | Same aggregators as #8; no Montsame article (died at the query) |
| 11 | `2024年 内蒙古 新疆 黑龙江 吉林 辽宁 西藏 地区生产总值 统计公报 亿元 人均` | Growth rates only, no totals (died at the sources: the pages hold no totals) |
| 12 | `内蒙古自治区2024年国民经济和社会发展统计公报 地区生产总值 26314.6` | S11: "2024年全区地区生产总值突破2.6万亿元" (trade department head), consistent with P5's 26,314.6 |
| 13 | `新疆维吾尔自治区2024年国民经济和社会发展统计公报 地区生产总值 年末常住人口` | S12: end-2024 population 2622.8万 (P4: 2623); GDP "突破两万亿元" (P5: 20,534.1) |
| 14 | `Taiwan population 23,400,220 end of 2024` | S14 Taiwan News, S15 Taipei Times: 23,400,220, down 20,222 from 2023 (Ministry of the Interior) |
| 15 | `黑龙江省2024年国民经济和社会发展统计公报 年末常住人口 地区生产总值 16476.9` | S17: 2023 year-end 3062万 and 2022 3099万 (both match P4); the 2024 bulletin was not found |
| 16 | `Hong Kong mid-2025 population revised end-2024 7,500,600 news.gov.hk` | Second angle on S8: The Standard gives the revised 7,500,600 (7,219,900 usual + 280,700 mobile residents) |

### Sources (IDs used in `02_unit_data.csv`)

| ID | Source | What it gave | Status |
|---|---|---|---|
| P1 | NBS, Seventh National Population Census communiqué No. 3, https://www.stats.gov.cn/english/PressRelease/202105/t20210510_1817188.html | Table 3-1: all 31 provinces (2020); "Servicemen 2000000"; national 1,411,778,724. Excludes Hong Kong, Macao, Taiwan and foreigners; includes mainland servicemen; "preliminary" | Read in full |
| P2 | NBS, 2025 1% sample-survey communiqué, https://www.stats.gov.cn/english/PressRelease/202605/t20260522_1963789.html | National 1,405.45 million (00:00, 1 Nov 2025); **no provincial table** | Read; dead end for provinces (died at the source) |
| P3 | NBS, 2025 statistical communiqué, https://www.stats.gov.cn/english/PressRelease/202602/t20260228_1962661.html | Year-end 2025 population 1,404.89 million (−3.39 million); GDP 140,187.9 billion yuan; GDP per person 99,665 yuan | Read |
| P4 | China Statistical Yearbook 2025, Table 2-5 "Population at Year-end by Region" (10,000 persons, 2015–2024), https://www.stats.gov.cn/sj/ndsj/2025/html/E02-05.jpg | All 31 provinces, 2024 column used; national 140,828. Note a): servicemen are in the national total, not in any region | Table is an image. The first fetch failed ("socket hang up"); the second saved the image, which was read directly |
| P5 | China Statistical Yearbook 2025, Table 3-9 "Gross Regional Product (2024)", https://www.stats.gov.cn/sj/ndsj/2025/html/E03-09.jpg | GRP (hundred million yuan) and per capita GRP (yuan) for all 31 provinces; "preliminary data" | Image, read directly. Table links came from https://www.stats.gov.cn/sj/ndsj/2025/left_.htm (`html/E02-05.jpg`, `html/E03-09.jpg`) |
| P6 | Yicai, 2026-03-03, https://www.yicai.com/news/103068269.html | 2025 year-end figures for 8 provinces: Zhejiang 6701, Guangdong 12859, Hainan 1055, Shandong 10043, Guangxi 4989, Gansu 2443, Guizhou 3857, Qinghai 592 (10,000 persons) | Read; spot check only |
| P7 | The Paper, 2026-03-03, https://www.thepaper.cn/newsDetail_forward_32690017 | Zhejiang 6701 (2025), from the provincial bulletin; says the 2025 estimate rests on the 1% sample survey | Read |
| S8 | Hong Kong Census and Statistics Department releases (2025-02-18 provisional; 2025-08-14 revised), via search summaries and The Standard | End-2024: 7,500,600 (revised) | **Primary pages came back empty** (P2025081400404.htm and its PDF; died at the source). Figure rests on two search summaries |
| S9 | Macao government portal, DSEC release of 5 March 2025, https://www.gov.mo/en/?p=353271 | End-2024: 688,300 (+0.7%) | Read |
| S10 | CEIC and Trading Economics (both citing Mongolia's National Statistics Office) | Dec 2024: about 3.5 / 3.54 million | **UNVERIFIED at the primary source** |
| S11 | Search summary of an Inner Mongolia commerce-department statement | 2024 GDP "over 2.6 trillion yuan" | Order-of-size check on P5 only |
| S12 | Search summary of a Xinjiang report | End-2024 population 2622.8万; GDP "over 2 trillion yuan" | Second source for P4 and P5 |
| S14, S15 | Taiwan News and Taipei Times, January 2025 (Ministry of the Interior data) | End-2024: 23,400,220 | Two outlets agree; the ministry's own table was not opened |
| S17 | Search summary quoting Heilongjiang's 2022 and 2023 bulletins | 3099万 (2022), 3062万 (2023) | Matches P4's 2022 and 2023 columns |

### Borders (not researched; read from canon and the author's atlas)

- Timeline repo, `Worldspace/Locations/Earth/Upper_Earth/Asia_East/README.md` ("Settled facts") and Map E; `Reference/World_History_Reference.md` § The Sinian Federation.
- The author's atlas, `/home/kuroskalacs/Documents/Doll-Fi/media/y-files/Map Files/x Full Earth/z-full-world-atlas/data/world/numbering.csv`, rows 161–169 (East Asia). Row 167 confirms that **Hainan, Hong Kong and Macau are in the Sinian Federation**, so the Macau assumption in `00_README.md` is settled.

### Conflicts

- Hong Kong end-2024: 7,534,200 (provisional, Feb 2025) vs **7,500,600** (revised, Aug 2025). The revised figure is used.
- China's national population: the official NBS year-end figures (1,408.28 million for 2024, 1,404.89 million for 2025) vs UN and aggregator model figures near 1.42 billion (Worldometers, Macrotrends). The NBS figures are used.

### Dead ends

- P2 has no provincial table (died at the source).
- No 2026 yearbook online (search 4).
- Search 11: provincial news pages give growth rates, not totals (died at the sources).
- Search 10: no Montsame article (died at the query).
- Hong Kong primary release pages came back empty (died at the source).

### Open threads

- Hong Kong and Macau GDP and inequality (needed only if the developer adds them to the Sinian pool).
- Mongolia's official 2024 year-end figure from 1212.mn.
- The full 2025 provincial table (China Statistical Yearbook 2026), to replace the 2024 basis when it appears.
- Taiwan's Ministry of the Interior table itself (two outlets agree, so this is low priority).


## Part 2: Russia, Italy, Germany, Argentina and North America (from ~21:45)

**Question researched against:** the official population and GDP of every present-day unit that the author's atlas
assigns to a successor of the USA, Canada, Mexico, Italy, Germany or Argentina. Russia was not re-researched: its
inputs and splits already exist (`Research_Logs/Russia_Split_Proportions_RS1b_Input_Table_2026-10-29.md`).

### Searches (verbatim, in order)

| # | Search string | Result |
|--:|---|---|
| 17 | `ISTAT popolazione residente al 1 gennaio 2025 per regione tabella bilancio demografico` | National figures only (58.93 million at 1 Jan 2025, provisional); no regional table in results |
| 18 | `ISTAT conti economici territoriali PIL per abitante regioni 2024 tabella` | ISTAT report 2022–2024 (I3) found |
| 19 | `Bayern Bevölkerung Bruttoinlandsprodukt 2024 Bundesländer Tabelle Statistisches Bundesamt BIP je Einwohner` | G1 (bayme vbm "Bayern Daten 2026") |
| 20 | `Statistik Austria Bevölkerung 1.1.2025 Bruttoinlandsprodukt 2024 pro Kopf` | Austria 9,197,213 (1.1.2025, secondary); GDP 2024 494.1 vs 484.2 billion euro (conflict); reference only |
| 21 | `Destatis Bevölkerung nach Bundesländern 31.12.2024 Bayern Deutschland insgesamt Zensus 2022 Basis` | G2: Germany 83.58 million, Bavaria 13,475 thousand (31 Dec 2024) |
| 22 | `INDEC Censo 2022 población por provincia resultados definitivos Chubut Neuquén Río Negro Santa Cruz Tierra del Fuego total país` | National totals only (provisional 46,044,703; definitive reported as 46,234,830 by outlets) |
| 23 | `CEPAL desagregación provincial del valor agregado bruto de Argentina 2004-2022 producto bruto geográfico por provincia participación` | CEPAL series found (2004–2021); tables not reachable (repository 403) |
| 24 | `participación provincial en el VAB Argentina 2021 CEPAL Neuquén Chubut Santa Cruz Tierra del Fuego Río Negro porcentaje producto per cápita` | A2 (Fundar via La Nación); Santa Cruz ~1.4% and Río Negro ~1.5% of national value added (second angle) |
| 25 | `Statistics Canada population estimates July 1 2025 by province and territory The Daily table Ontario Quebec British Columbia` | C1 (Newfoundland statistics agency's copy of Table 17-10-0005-01) |
| 26 | `INEGI Conteo de Población y Vivienda 2025 resultados población por entidad federativa Sonora Chihuahua Baja California` | INEGI Encuesta Intercensal 2025 found (released 22 Sep 2026); its state table is a chart image (not usable) |
| 27 | `INEGI PIB por entidad federativa 2024 participación porcentual estados Ciudad de México Nuevo León Sonora Chihuahua Baja California` | INEGI PIBE 2024 bulletin (M3): current-price shares for the 11 largest states only |
| 28 | `PIBE 2024 INEGI participación en el PIB nacional Campeche Tabasco Quintana Roo Yucatán Baja California Sur porcentaje 2024` | M2 (Chiapas statistics committee table, all states) |
| 29 | `Alaska Department of Labor population estimates 2024 Southeast region boroughs Juneau Ketchikan Sitka total Southeast Alaska` | U3 found via the department's page |
| 30 | `BEA GDP by state sum of states differs from U.S. total federal military and civilian activity located overseas note` | Explains the 0.55% gap in the US GDP check (U4) |

### Sources (IDs used in `05_part2_unit_data.csv`)

| ID | Source | What it gave | Status |
|---|---|---|---|
| U1 | en.wikipedia, *List of U.S. states and territories by population* (U.S. Census Bureau, July 1 2025 estimates) | All 50 states + DC; printed total 341,784,857 | Read twice (all 51 values re-confirmed). **The 51 values sum to 341,785,457, 600 more than the printed total** (conflict; not resolved; negligible) |
| U2 | en.wikipedia, *List of U.S. states and territories by GDP* (BEA SAGDP1, 2025, million USD) | All 50 states + DC; US total 30,762,099 | Read. States sum to 30,594,279, 0.55% below the US total, which U4 explains |
| U3 | Alaska Department of Labor and Workforce Development, https://live.laborstats.alaska.gov/node/12837 | 2025: Southeast region 70,233; statewide 738,737 | Read. Statewide differs from U1's 737,270 (different estimate series); only the Panhandle's share is used |
| U4 | BEA FAQ and releases via search summary; EIA State Energy Data notes | State GDP excludes federal military and civilian activity overseas; the gap is typically 0.53–0.73 points (the magnitude is from a secondary blog) | Search summary |
| C1 | Newfoundland & Labrador Statistics Agency, *Annual Estimates of Population for Canada, Provinces and Territories, from July 1, 1971 to July 1, 2026* (release 09/23/26), source Statistics Canada Table 17-10-0005-01, https://www.stats.gov.nl.ca/Statistics/Topics/population/PDF/Annual_Pop_Prov.PDF | July 1 2025 (updated postcensal): Canada 41,608,982 and every province | PDF saved by WebFetch, read with `pdftotext`. The first 2025 release gave 41,651,653 (search 25); the updated figure is used |
| C2 | en.wikipedia, *List of Canadian provinces and territories by gross domestic product* (Statistics Canada table 36-10-0221-01, 2024, million CAD) | Every province and territory | Read |
| C3 | en.wikipedia, *Northern Ontario* | 2021: 789,519 (statistical region, includes all of Nipissing and Parry Sound districts); the French River–Lake Nipissing–Mattawa boundary | Read |
| C4 | en.wikipedia, *Parry Sound District* | 2021: 46,909 | Read |
| C5 | en.wikipedia, *Qikiqtaaluk Region* | 2021 community counts (13 communities, 19,355) | Read; page gives no island per community |
| M1 | en.wikipedia, *List of Mexican states by population* (INEGI 2020 census) | All 32 entities; 126,014,024 | Read |
| M2 | Comité Estatal de Información Estadística y Geográfica de Chiapas, *PIB Chiapas 2024* (citing INEGI PIBE base 2018), http://www.ceieg.chiapas.gob.mx/storage/posts/productos/PIB/PIB_Chiapas_2024.pdf | 2024 shares at constant 2018 prices for every state named in the CSV | PDF saved, read with `pdftotext` |
| M3 | INEGI, PIBE 2024 bulletin (5 Dec 2025), https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/pibent/PIBE2024_RR.pdf | Current-price shares: Baja California 3.9, Chihuahua 3.8, Sonora 3.3 (second angle on M2's 3.74, 3.67, 3.24) | PDF saved, read with `pdftotext` |
| I1 | tuttitalia.it, *Regioni italiane per popolazione* (ISTAT, 1 Jan 2026, estimated) | All 20 regions; 58,942,828 | Read |
| I2 | en.wikipedia, *List of Italian regions by GDP*, Table 2 (OECD, GDP per capita 2023, euro) | All regions, South Tyrol and Trentino separate | Read |
| I3 | ISTAT, *Conti economici territoriali, anni 2022–2024* (22 Dec 2025), https://www.istat.it/wp-content/uploads/2025/12/REPORT-CONTI-TERRITORIALI_Anni-2022-2024.pdf | 2024 GDP per person in the text for 14 regions and the four macro-areas (second angle on I2; e.g. Lombardia 50.4k vs I2's 49.0k for 2023) | PDF saved, read with `pdftotext`; the full regional table is a chart |
| G1 | bayme vbm, *Bayern Daten 2026* (citing the Bavarian statistics office) | 2024 GDP: Germany 4,329.0 billion euro, Bavaria 791.6 billion; per inhabitant 51,833 and 58,817 | PDF saved, read with `pdftotext` |
| G2 | Destatis via search summary (GENESIS 12411-0010: Germany 83.58 million, 31 Dec 2024); Bavaria 13,475 thousand via statistiken-aktuell.de citing Destatis | Populations | Search summaries. Second angle: G1's GDP ÷ GDP per inhabitant implies Bavaria 16.11% of Germany, against 16.12% here |
| G3 | (same as G1, G2) | Germany without Bavaria = Germany minus Bavaria (DERIVED) | — |
| A1 | en.wikipedia, *List of Argentine provinces by population* (INDEC 2022 census, provisional; total 46,044,703) | All 24 jurisdictions | Read; **the 24 values sum exactly to the printed total**. Tierra del Fuego's Antarctic 130 are taken out (from es.wikipedia's note) |
| A2 | La Nación, 30 Jul 2026, *El ranking de las provincias según su PBI per cápita* (Fundar estimate, 2021 PPP US$) | All 24 jurisdictions; national 26,772 | Read. A think-tank estimate, not an official series. Second angle: Santa Cruz's implied share of national output (1.37%) matches the official ~1.4% (search 24) |

### Conflicts

- **Argentina, first read:** es.wikipedia's *Anexo: Provincias de Argentina por población*, as returned by the fetch,
  gave six provinces different figures from A1 (Buenos Aires 17,523,996, Córdoba 3,840,905, Corrientes 992,595, Río
  Negro 750,768, Chubut 592,621, Santa Cruz 337,226), and those 24 values summed to 406,139 less than the printed
  total. A1's values sum exactly, so A1 is used. Whether the fetch mixed columns or the page mixes vintages was not
  established.
- **USA:** the 51 state values in U1 sum to 600 more than U1's printed total (re-read twice, unresolved, negligible).
- **Austria 2024 GDP:** 494.1 vs 484.2 billion euro (different data vintages). Austria is reference only.
- **Bavaria's share:** 16.1% here (31 Dec 2024) vs "15.8%" for 2025 in G1's own summary line. Not resolved.
- **Mexico GDP shares:** constant-price (M2) vs current-price (M3) differ by 0.1–0.2 points for the large states.
- **Canada July 1 2025:** 41,651,653 (first release) vs 41,608,982 (updated, used).
- **Italy:** the Santa Luce ruling's Meridia figure (~23.8M, "without Sardinia") vs the atlas build, which puts Sardinia
  in Meridia.

### Dead ends

- ISTAT's regional population table (search 17) and the CEPAL provincial tables (search 23, repository 403: died at
  the source).
- INEGI's 2025 intercensal state table and the PIBE 2024 full table are chart images (died at the source).
- tuttitalia's Trentino-Alto Adige province page returned 404 (died at the source).
- The bayme vbm 2026 PDF and the Statistik Austria release: the first returned binary (extracted locally), the second
  failed to fetch.

### Open threads

- A census-office figure for the Nipissing District south of the Mattawa (to trim the Prairie Federation's Ontario part).
- Which island Igloolik, Kinngait, Sanikiluaq and Sanirajak sit on (Nunavut split).
- Whether Yakutat lies south of the Jette–Cook cut.
- The South Tyrol and Trentino populations (for a weighted Trentino-Alto Adige figure).
- INEGI's definitive 2025 intercensal state figures (to replace the 2020 census basis).
- Chile's five regions, Austria and Guatemala's Petén, if the developer wants them added.

## Search count

30 web searches in all (Part 1: 16; Part 2: 14), none refused. About 970 of the session's 1,000 remain.
