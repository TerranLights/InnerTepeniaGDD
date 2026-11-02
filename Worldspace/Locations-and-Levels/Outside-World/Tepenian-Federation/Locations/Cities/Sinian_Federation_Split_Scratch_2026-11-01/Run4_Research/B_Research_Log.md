# B: Subdivision and country headcounts for the successor-country splits (research log)

**Run date:** 2026-11-02. **Companion file:** `B_split_headcounts.csv` (71 data rows, same folder).
**Purpose:** for 11 countries, give each listed subdivision **and** the country total from the same source and the same date, so that shares can be computed exactly.
**Tools used:** WebSearch and WebFetch only. Local Python was used only to add up figures already collected (no downloads, no files read). **Totals used: 55 searches (limit 60), 45 fetches (limit about 45).**

**How to read the confidence labels used below and in the CSV:**
- **Primary, fetched:** the number was read from the statistics office's own page, API or table in this run.
- **Secondary, fetched:** read from a page that reproduces the office's figures (citypopulation.de, Wikipedia) because the office's page was blocked or not found.
- **Snippet:** the number appeared only in a search-result summary. The page itself was not opened. Such numbers are marked **UNVERIFIED**.
- **DERIVED:** my own arithmetic sum of figures from one official document, where the document prints no total. Not a published figure.

**Two-vintage rule:** where the requested date and a newer official vintage both exist, the CSV row carries the requested date and the notes column gives the newer figure. Brazil and Thailand have two full sets of rows (census and estimate, registration and census) because the task asked for both kinds or because the requested set was incomplete. The country-total row is labeled with the set it belongs to; never divide one set's unit by another set's total.

---

## 1. Searches (verbatim, in the order run)

| # | Search string (verbatim) | What it returned |
|---|---|---|
| 1 | `Statbel population 1 January 2025 Flemish Region Walloon Region Brussels-Capital Region` | Statbel "bestat" table views; summary gave 1 Jan 2025 Flemish 6,864,766, Brussels 1,255,795, Walloon 3,704,990, Belgium 11,825,551, and a Belga report on the 1 Jan 2026 Brussels figure. Led to fetches 2–4, 7–8. |
| 2 | `Deutschsprachige Gemeinschaft Bevölkerung 1. Januar 2025 Statbel Ostbelgien Statistik Einwohner` | No 2025 figure. Mostly Statista/Germany noise. Eurydice snippet: 77,527 on 1 Jan 2019. **Dead end at the query** (too generic; German-language noise). |
| 3 | `ostbelgienstatistik.be Bevölkerungsstand DG Gemeinden 2025` | No DG table. Council of Europe "about 77,000" (undated). Statbel municipal PDF view (5813262a) surfaced. **Dead end at the source** (portal not indexed). |
| 4 | `"Deutschsprachigen Gemeinschaft" Einwohner "1. Januar 2025" OR "1. Januar 2026" Ostbelgien Bevölkerung gewachsen` | No dated 2025/2026 figure; "just over 78,000" and "about 78,500" (undated). **Dead end at the source.** |
| 5 | `ONS mid-2024 population estimates UK Northern Ireland population 69.3 million` | ONS mid-2024 bulletin, NISRA release (1,927,900 at 30 Jun 2024), a parliamentary-answer page citing 1,927,855. Led to fetches 9–11. |
| 6 | `Northern Ireland mid-2024 population estimate 1,927,855 NISRA MYE24` | NISRA publication pages and OpenDataNI resources; exact 1,927,855 not confirmed. Led to fetches 12–13. |
| 7 | `ONS population estimates UK mid-2025 bulletin October 2026 revised mid-2024` | ONS mid-2025 bulletin exists (69.5 million; mid-2022 to mid-2024 revised). Led to fetch 17. |
| 8 | `INE cifras oficiales de población revisión del padrón municipal 1 de enero de 2025 total España Cataluña Navarra Álava Bizkaia Gipuzkoa` | Real Decreto 1117/2025 (BOE 11 Dec 2025); summary: Spain 49,128,297 (INE note 2 Dec 2025), Álava 342,161, Gipuzkoa 733,149 (attributed to an INE table). Led to fetches 18–19. |
| 9 | `Condado de Treviño población 1 de enero de 2025 padrón INE habitantes` | en.wikipedia infobox: 1,468 (1 Jan 2025, INE); 2021 census 1,422; electoral roll 1,234 (Jan 2026). |
| 10 | `INE nota de prensa padrón 1 enero 2025 "49.128.297" comunidades autónomas Cataluña` | Confirmed 49,128,297 is the **Censo Anual de Población 2025** (2 Dec 2025); provisional quarterly ECP gave 49,077,984. No Catalonia total. |
| 11 | `"Real Decreto 1117/2025" cifras oficiales padrón total nacional habitantes 1 de enero de 2025` | BOE annex lists provinces only; no national total in the excerpts. Idescat release surfaced (fetch 24). |
| 12 | `"8.146.265" Catalunya població 2025` | kyero.com attributes 8,146,265 to INE (1 Jan 2025). Idescat census-based 8,124,126 (1 Jan 2025). Confirms Padrón ≠ Censo Anual. |
| 13 | `padrón municipal 1 enero 2025 España total habitantes cifras oficiales INE diciembre 2025 diferencia censo anual` | Summary conflated census and Padrón (called 49,128,297 the "padrón revisado"); no independent Padrón national total. Not relied on. |
| 14 | `"49.114.494" habitantes padrón 2025` | No hits for my derived sum. Gave later INE ECP figures (49,315,949 on 1 Jul 2025; 49,442,844 on 1 Oct 2025). |
| 15 | `Valle de Villaverde Cantabria población 2025 habitantes INE padrón` | 249 (INE 2025) per hispanopedia; 252 on 1 Jan 2024 per foro-ciudad. Led to fetch 26. |
| 16 | `"Condado de Treviño" habitantes 2025 "1.472" OR "1.468"` | Wikipedia 1,468 (INE) vs citypopulation 1,472 ("register 2025-01-01"). Resolved by fetch 28. |
| 17 | `IBGE Censo 2022 população por unidade da federação Acre Amapá Amazonas Mato Grosso Pará Rondônia Roraima total Brasil 203.080.756` | Dec 2022 preview figures (not final), 203,062,512 first release. Led to SIDRA fetches 31–32. |
| 18 | `IBGE estimativas da população 2026 "214.211.951" OR "213.421.037" 1º de julho` | Confirms 214,211,951 for 1 Jul 2026 (Poder360 and others; released 28 Aug 2026). 213,421,037 not found in news (it is in SIDRA, fetch 32). |
| 19 | `BPS jumlah penduduk menurut provinsi 2025 ribu jiwa Aceh Papua Papua Barat Daya Papua Tengah Papua Pegunungan Papua Selatan` | BPS table pages (titles only); SUPAS 2025 = 284.67 million; Papua Selatan 542.1 thousand (2024, Databoks). Led to fetch 33 (403). |
| 20 | `jumlah penduduk 2025 Papua Tengah Papua Pegunungan Papua Selatan Papua Barat Daya ribu jiwa BPS proyeksi pertengahan tahun` | Only regency figures (Puncak 117.89k, Paniai 174.21k) and TFRs. **Dead end at the source** (no provincial totals indexed). |
| 21 | `Provinces of Indonesia population mid 2024 estimate Central Papua Highland Papua South Papua Southwest Papua Aceh` | Wikipedia-derived: South Papua 542,100 (mid-2024); Dukcapil 282.48 million (June 2024). Led to fetch 35. |
| 22 | `BPS penduduk Indonesia pertengahan 2025 "284.438" OR "284,438" OR "284.4" juta jiwa provinsi` | Snippet: BPS mid-2025 = 284,438.8 thousand ("laman resmi BPS", page not identified); SUPAS 2025 = 284.67 million; Dukcapil June 2025 = 286.69 million; a detik item "287,6 juta" (later date, not used). |
| 23 | `jumlah penduduk Papua Tengah 2025 "1.492" OR "1,49 juta" ribu jiwa BPS` | Regency figures only (Mimika 228.6k). **Dead end at the source.** |
| 24 | `Thailand registered population 31 December 2024 Department of Provincial Administration Pattani Yala Narathiwat total 65,951,210` | 65,951,210 at 31 Dec 2024 (Khaosod; NSO yearbook 2025); 65,809,011 at 31 Dec 2025. No provinces. The tool reported a prompt injection in one result (cavac.at mirror) and ignored it. |
| 25 | `ประชากร จังหวัดปัตตานี ยะลา นราธิวาส 31 ธันวาคม 2567 กรมการปกครอง จำนวนราษฎร` | Only the 2023 national figure (66,052,615). **Dead end at the source** (DOPA tables not indexed). |
| 26 | `Pattani province population December 2024 registration "741" Yala "553" Narathiwat "824" exact figures` | Pattani 740,904 and Narathiwat 823,996 (2024, Wikipedia mirrors); Yala only 553,000 (rounded). |
| 27 | `Yala province population 2024 DOPA registered "553," people infobox` | Only the rounded 553,000 (2024, rank 46). **Dead end at the source.** |
| 28 | `Thailand 2025 population and housing census preliminary results National Statistical Office 70.3 million "70,275,751"` | NSO preliminary census (Census Day 1 Apr 2025) ≈ 70.3 million (Nation Thailand 27 Jan 2026); exact 70,275,751 only on citypopulation.de. |
| 29 | `จำนวนประชากรจังหวัดยะลา ปี 2567 ทะเบียนราษฎร คน ปัตตานี 740,904` | An agricultural-office document (488,563 "population", basis unclear, not used). **Dead end at the source.** |
| 30 | `PSA 2024 POPCEN Sulu province population Philippines total 112,729,484 Tawi-Tawi` | Philippines 112,729,484 (1 Jul 2024); Sulu 1,146,097 and Tawi-Tawi 482,645 (2024 POPCEN, barangaydirectory.com). Led to fetch 38. |
| 31 | `"1,146,097" Sulu 2024 Census of Population PSA` | Same figure on citypopulation.de, barangaydirectory.com, de.wikivoyage. PSA's own release not found. |
| 32 | `INS populația rezidentă 1 ianuarie 2025 pe județe Satu Mare Bihor Sălaj Maramureș Arad total România` | National 19,043,151 vs 19,036,031 (conflict); no counties. |
| 33 | `insse.ro comunicat de presă populația rezidentă la 1 ianuarie 2025 poprez_ian2025 pdf județe` | INS now issues a provisional release and a definitive release; 19,043,200 (rounded definitive). County PDF not found. |
| 34 | `"populația rezidentă" "1 ianuarie 2025" județul Bihor persoane Satu Mare Maramureș Sălaj Arad regiunea Nord-Vest` | Only 2021 census county figures; citypopulation.de Romania page surfaced (fetch 39). |
| 35 | `"19.036.031" OR "19.043.151" populația rezidentă 1 ianuarie 2025 INS provizorii definitive` | 19,036,031 reported with a decline of 31,500; 19,043,151 with a decline of 24,425. Labels not explicit in this search. |
| 36 | `주민등록 인구 2024년 12월 말 제주특별자치도 전국 51,217,221 행정안전부` | Jeju not found; k-calc.com "2024: 672,252" (date not stated). |
| 37 | `Ministry of the Interior and Safety resident registration population end of 2024 51.21 million by province Jeju 670,000` | National end-2024 51,217,221 (Asia Business Daily); end-2025 51,117,378; 2024 census 51.81 million. No Jeju. |
| 38 | `제주 주민등록인구 2024년 말 기준 명 감소 제주도 인구 2025년 말` | National 51,217,221 again (newsis). No Jeju. Led to fetch 40. |
| 39 | `"제주" 주민등록 인구 "2024년 12월 31일" 기준 67만 명 제주특별자치도 인구 현황` | k-calc.com series 2022–2026 (672,252 for 2024) with no stated reference date. **Dead end at the source.** |
| 40 | `INE Censo 2024 resultados población efectivamente censada 18.480.432 región de La Araucanía 1.010.423 Los Ríos Los Lagos Aysén Magallanes` | INE release (18,480,432); Emol table: Aysén 100,745, Magallanes 166,537. Led to fetch 41. |
| 41 | `censo 2024 "890.284" Los Lagos "398.230" Los Ríos "1.010.423" Araucanía personas censadas` | All three confirmed by secondary sources (Wikipedia table; La Batalla; a local outlet quoting the INE Los Lagos regional director). |
| 42 | `INE Chile censo 2024 población estimada ajustada por omisión cifra oficial de población 2026 publicación estimaciones y proyecciones` | INE Jan 2026 projections (base 2024): 20,150,948 in 2026; peak 2035; regional projections due H2 2026; 1,391,332 uncounted (about 7% omission). |
| 43 | `Чисельність наявного населення України на 1 січня 2022 Держстат 41167335 Луганська Донецька Харківська Дніпропетровська Запорізька Херсонська область` | Derzhstat collection PDF and express release: present population 41,167.3 thousand; resident 40,997.7 thousand. No oblast figures in snippets. |
| 44 | `population 1 January 2022 State Statistics Service Ukraine oblast Donetsk 4,059,372 Luhansk 2,102,921 Kharkiv Dnipropetrovsk Zaporizhzhia Kherson 1,001,598` | Wikipedia list (Donetsk 4,059,372), citypopulation Zaporizhzhia 1,638,462. **Note:** the figures in this query string were recalled from memory as search terms only; none was used until confirmed by fetch 43. |
| 45 | `Херсонська область наявне населення 1 січня 2022 по районах Генічеський Каховський Скадовський Бериславський Херсонський район тис. осіб` | No raion table; Kherson city 279,131 (1 Jan 2022, LIGA). **Dead end at the source.** |
| 46 | `"41 167 335" OR "41167335" населення України 1 січня 2022 без урахування Автономної Республіки Крим та м. Севастополя` | Confirms 41,167,335 = 41,167.3 thousand (Derzhstat), excluding Crimea and Sevastopol. |
| 47 | `German-speaking Community of Belgium population 1 January 2025 inhabitants nine municipalities Eupen Sankt Vith total` | 79,479 on 1 Jan 2024 (EACEA Youth Wiki; Wikipedia infobox), with national 11,763,650. No 2025 figure. The tool reported a prompt injection in a Wikipedia mirror and ignored it. |
| 48 | `Jeju registered population fell end of 2024 resident registration Jeju Island population decline 2024 figure` | Only older figures (677,057 in May 2023) and 2024 half-year outflow. **Dead end at the source.** |
| 49 | `jumlah penduduk Provinsi Aceh 2025 "5.626" ribu jiwa BPS hasil proyeksi` | No provincial total; regency figures only. **Dead end at the source.** |
| 50 | `Bihor populația rezidentă la 1 ianuarie 2025 "556.606" OR "556606" date definitive INS județ` | Settles the vintages: 19,043,151 is the **definitive** 1 Jan 2025 total, 19,036,031 the earlier **provisional** one. No Bihor figure. |
| 51 | `제주 주민등록인구 "672,252" OR "67만2252" OR "67만 2252"` | Only k-calc.com again. **Dead end at the source.** |
| 52 | `2024 인구주택총조사 등록센서스 제주 총인구 명 전국 5180만 시도별 2025년 7월 발표` | 2024 register-based census (1 Nov 2024): 51.81 million nationally; no Jeju figure. **Dead end at the source.** |
| 53 | `제주도 주민등록 인구 2024년 12월 말 기준 "67만1" OR "671,064" OR "67만2" 감소` | No Jeju year-end figure; 2025 net outflow 4,273; foreign nationals 30,511 (2024). **Dead end at the source.** |
| 54 | `Kherson Oblast left bank population before 2022 Henichesk Kakhovka Skadovsk raion population 2022 estimate share of oblast` | Raion figures on citypopulation.de; no source states a left-bank total or share. Led to fetch 45. |
| 55 | `penduduk Papua Pegunungan 2025 "1.484,9" OR "1,48 juta" OR "1.484.900" jiwa` | Regency figures only (Nduga 122.47k, Yahukimo 203.9k). **Dead end at the source.** |

**Search count: 55** (limit 60; 5 left unused).

---

## 2. Pages fetched

| # | URL | Result |
|---|---|---|
| 1 | https://statbel.fgov.be/en/themes/population/structure-population | Human-verification challenge (CAPTCHA). No data. Not retried. |
| 2 | https://bestat.statbel.fgov.be/bestat/api/views/3ebe4ddc-27e6-4d3d-a6c0-3121df828953/result/HTML | Statbel, 1 Jan 2026: Belgium 11,867,634; Flanders 6,898,350; Wallonia 3,713,450; Brussels 1,255,834. |
| 3 | https://bestat.statbel.fgov.be/bestat/api/views/fc14c1ce-7361-4d42-a892-fce8e81a1b79/result/HTML | Same 2026 figures; series 2016–2026. |
| 4 | (same URL as 3, second question) | 1 Jan 2025: Belgium 11,825,551; Flanders 6,864,766; Wallonia 3,704,990; Brussels 1,255,795. 1 Jan 2024: 11,763,650; 6,821,770; 3,692,283; 1,249,597. |
| 5 | https://www.ostbelgienstatistik.be/ | **HTTP 403.** Not retried (see §7). |
| 6 | https://brf.be/regional/998168 | 2016 article (Eupen 19,388); no DG total. Dead end. |
| 7 | https://bestat.statbel.fgov.be/bestat/api/views/5813262a-72e3-4bc1-a1fa-68a8b6521f43/result/PDF | Compressed PDF; unreadable by the tool. |
| 8 | https://bestat.statbel.fgov.be/bestat/api/views/5813262a-72e3-4bc1-a1fa-68a8b6521f43/result/HTML | Statbel 2016–2026 table, regions and Belgium only (no DG); 2025 and 2026 figures identical to fetches 2–4. **Used as the CSV source.** |
| 9 | https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualmidyearpopulationestimates/mid2024 | UK mid-2024 = 69,281,400 (released 26 Sep 2025). No country totals in text. |
| 10 | https://www.nisra.gov.uk/news/population-northern-ireland-continues-grow | NI 30 Jun 2024 = 1,927,900 (released 11 Sep 2025). No unrounded figure. |
| 11 | https://parallelparliament.co.uk/question/HL1519/population | **HTTP 403.** |
| 12 | https://admin.opendatani.gov.uk/dataset/mye01t011/resource/8fc7f971-4b9c-4154-9368-2e66c06180b5 | **HTTP 403.** |
| 13 | https://www.nisra.gov.uk/publications/2024-mid-year-population-estimates-northern-ireland-and-estimates-population-aged-85 | File list only (Excel population totals); no figure on the page. |
| 14 | https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/timeseries/nipop/pop | Series page (NIPOP, dataset "pop", release 1 Oct 2026); values only in the CSV. |
| 15 | https://www.ons.gov.uk/generator?format=csv&uri=/peoplepopulationandcommunity/populationandmigration/populationestimates/timeseries/nipop/pop | NI: 2023 1,920,400; **2024 1,927,900; 2025 1,928,400.** |
| 16 | https://www.ons.gov.uk/generator?format=csv&uri=/peoplepopulationandcommunity/populationandmigration/populationestimates/timeseries/ukpop/pop | UK: 2023 68,588,000; **2024 69,256,300; 2025 69,483,900.** |
| 17 | https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualmidyearpopulationestimates/mid2025 | Released 1 Oct 2026. Mid-2025 UK 69,483,900; NI 1,928,400. Mid-2024 UK revised to 69,256,300 (−25,200); revision attributed to England & Wales and Scotland only. |
| 18 | https://boe.es/boe/dias/2025/12/11/pdfs/BOE-A-2025-25362.pdf | Compressed PDF; unreadable. |
| 19 | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-25362 | RD 1117/2025 annex (Padrón, 1 Jan 2025): Álava 342,161; Barcelona 5,983,325; Girona 832,026; Lleida 456,106; Tarragona 874,808; Bizkaia 1,166,816; Gipuzkoa 733,365; Navarra 683,500. No national or community totals; municipalities not listed (INE publishes them). |
| 20 | https://www.ine.es/jaxiT3/Tabla.htm?t=2852 | Table shell only; series ends 2021. |
| 21 | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/2852?nult=1 | Discontinued series; latest 2021. Not used. |
| 22 | https://ine.es/dyngs/Prensa/CensoVariables2025.pdf | Compressed PDF; unreadable. |
| 23 | https://ine.es/dyngs/Prensa/CensoVariables2025.htm | "Censo Anual de Población. Primeros resultados 2025" (2 Dec 2025): Spain 49,128,297 on 1 Jan 2025. No regional totals; no statement on Padrón equivalence. |
| 24 | https://www.idescat.cat/novetats/?id=5405&lang=en | Idescat note on the Padrón (12 Dec 2025, RD 1117/2025); no figures on the page. |
| 25 | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-25362 | Same annex, all 52 province and autonomous-city rows transcribed (used for the DERIVED national sum). |
| 26 | https://www.citypopulation.de/en/spain/localities/cantabria/39101__valle_de_villaverde | Valle de Villaverde: 2025-01-01 = 249 (INE padrón). |
| 27 | https://citypopulation.de/en/spain/castillayleon/burgos/09109__condado_de_trevi%C3%B1o/ | Condado de Treviño: 2025-01-01 = 1,472 ("register"); conflicts with INE (fetch 28). |
| 28 | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/2862?nult=1 | INE table 2862 (Burgos), 2025: Burgos 361,556 (= BOE); **Condado de Treviño 1,468.** |
| 29 | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/2892?nult=1 | Wrong province (Santa Cruz de Tenerife, 1,082,421 = BOE). Wrong guess at the table number. |
| 30 | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/2893?nult=1 | INE table 2893 (Cantabria), 2025: Cantabria 593,964 (= BOE); **Valle de Villaverde 249.** |
| 31 | https://apisidra.ibge.gov.br/values/t/4709/n1/all/n3/11,12,13,14,15,16,51/v/93/p/2022 | Censo 2022: Brazil 203,080,756; RO 1,581,196; AC 830,018; AM 3,941,613; RR 636,707; PA 8,120,131; AP 733,759; MT 3,658,649. |
| 32 | https://apisidra.ibge.gov.br/values/t/6579/n1/all/n3/11,12,13,14,15,16,51/v/9324/p/last%202 | Estimates 2025 and 2026 (values in §3.4). |
| 33 | https://www.bps.go.id/id/statistics-table/3/V1ZSbFRUY3lTbFpEYTNsVWNGcDZjek53YkhsNFFUMDkjMyMwMDAw/jumlah-penduduk--laju-pertumbuhan-penduduk--distribusi-persentase-penduduk--kepadatan-penduduk--rasio-jenis-kelamin-penduduk-menurut-provinsi.html?year=2025 | **HTTP 403.** Not retried on bps.go.id (see §7). |
| 34 | https://en.wikipedia.org/wiki/List_of_Indonesian_provinces_by_population | HTTP 404 (wrong title guessed). |
| 35 | https://en.wikipedia.org/wiki/Provinces_of_Indonesia | "Population (mid 2025)", citing BPS 2026: Aceh 5,626,000; West Papua 587,600; Southwest Papua 636,400; Papua 1,073,600; Central Papua 1,492,300; Highland Papua 1,484,900; South Papua 549,700. No national row (the tool's own sum of the regional table: 284,438,400). |
| 36 | https://en.wikipedia.org/wiki/Provinces_of_Thailand | "Population (December 2024)", DOPA: Pattani 741,000; Yala 553,000; Narathiwat 824,000; total 65,951,000. |
| 37 | https://citypopulation.de/en/thailand/prov/admin/S__southern/ | NSO census 2025-04-01 (preliminary): Pattani 668,941; Yala 566,239; Narathiwat 760,807; Thailand 70,275,751. Also 2000 and 2010 census. |
| 38 | https://www.citypopulation.de/en/philippines/admin/bangsamoro/1566__sulu | PSA: Sulu 2024-07-01 1,146,097 (2020: 1,000,108); Philippines 112,729,484 (2020: 109,035,343). |
| 39 | https://citypopulation.de/en/romania/admin/ | INS estimate 2025-01-01: Arad 410,085; Bihor 556,606; Maramureș 450,711; Satu Mare 330,296; Sălaj 211,033; Romania 19,036,031. |
| 40 | https://www.newsis.com/view/NISX20250103_0003019683 | MOIS 2024 analysis (3 Jan 2025): 51,217,221 at end of 2024. No Jeju figure; no provincial table. |
| 41 | https://www.ine.gob.cl/sala-de-prensa/prensa/general/noticia/2025/03/27/primeros-resultados-del-censo-2024-18.480.432-personas-fueron-censadas-en-chile-manteni%C3%A9ndose-la-tendencia-de-envejecimiento-de-la-poblaci%C3%B3n | "18.480.432 personas fueron censadas en Chile"; fieldwork March–July 2024; La Araucanía "more than 1 million" only; no other regional figures; no mention of an adjusted total. |
| 42 | https://index.minfin.com.ua/ua/reference/people/2022 | HTTP 404. |
| 43 | https://en.wikipedia.org/wiki/List_of_Ukrainian_oblasts_and_territories_by_population | "Population (2022)": Luhansk 2,102,921; Donetsk 4,059,372; Kharkiv 2,598,961; Dnipropetrovsk 3,096,485; Zaporizhzhia 1,638,462; Kherson 1,001,598; source footnote: Derzhstat, "Number of Present Population of Ukraine, as of 1 January 2022". Crimea 1,963,770 and Sevastopol 509,992 also listed (not Derzhstat; not used). No total row. |
| 44 | https://k-calc.com/region/Jeju-do | Jeju yearly series citing MOIS: 2024 = 671,064 (the search snippet had shown 672,252); no reference date for 2022–2025; 2026 = October 2026. |
| 45 | https://citypopulation.de/en/ukraine/admin/65__cherson/ | Kherson raions 2022-01-01: Beryslav 94,103; Kherson 450,233; Henichesk 118,059; Kakhovka 216,458; Skadovsk 122,745; sum = 1,001,598 = oblast total. |

**Fetch count: 45.**

---

## 3. Country by country: figures taken, source, same-source check, sums and shares

Shares below are each unit's population divided by its country total from the same row set (computed locally from the numbers in the CSV).

### 3.1 Belgium (Statbel, 1 January 2025)
- **Taken:** Flemish Region 6,864,766; Walloon Region 3,704,990; Brussels-Capital Region 1,255,795; Belgium 11,825,551. **Primary, fetched** (fetches 4 and 8, two Statbel views with identical numbers).
- **Same source and date:** yes (one Statbel table, 1 Jan 2025).
- **Adds up:** the three regions sum to 11,825,551 exactly (a full partition; combined share 100%). Shares: Flemish 58.05%, Walloon 31.33%, Brussels 10.62%.
- **Latest vintage (1 Jan 2026, same table):** 6,898,350 / 3,713,450 / 1,255,834 / 11,867,634 (shares 58.13% / 31.29% / 10.58%).
- **German-speaking Community (note only):** **79,479 on 1 Jan 2024, UNVERIFIED** (search snippets 47; EACEA Youth Wiki and the en.wikipedia infobox, not fetched). It sits inside the Walloon Region; against Statbel's 1 Jan 2024 Belgium total of 11,763,650 it is 0.68%, and against Walloon 2024 (3,692,283) 2.15%. **No 1 Jan 2025 figure found.** Earlier dated figures from snippets: 77,527 (1 Jan 2019, Eurydice), 77,949 (1 Jan 2020, Wikipedia).

### 3.2 United Kingdom (ONS, mid-2024)
- **Taken:** Northern Ireland 1,927,900; UK 69,256,300. **Primary, fetched** (ONS "pop" time series CSVs, release 1 Oct 2026; fetches 15–16; confirmed by the mid-2025 bulletin, fetch 17).
- **Same source and date:** yes (one ONS dataset, mid-2024, same release). Both are rounded by ONS to the nearest 100.
- **Adds up:** NI 2.78%; rest of UK 67,328,400.
- **Conflict:** the original mid-2024 bulletin (26 Sep 2025) gave UK 69,281,400; ONS revised it to 69,256,300 on 1 Oct 2026. NI was not revised (still 1,927,900). **Chose the revised value** because it is the current official vintage and comes from the same release as the NI figure. With the old total, NI's share is 2.7827% instead of 2.7837% (immaterial).
- **Latest vintage (mid-2025, same release):** NI 1,928,400; UK 69,483,900 (NI 2.78%).
- **Unrounded NI:** 1,927,855 appeared only in a snippet from a parliamentary-answer page that returned 403. **UNVERIFIED; not used.**

### 3.3 Spain (INE Padrón, 1 January 2025)
- **Taken:** Álava 342,161; Bizkaia 1,166,816; Gipuzkoa 733,365; Navarra 683,500 (**primary, fetched**, BOE annex of RD 1117/2025, fetch 19); Catalonia 8,146,265 (**DERIVED** from the four Catalan provinces in the same annex; matches the 8,146,265 that kyero.com attributes to INE); Condado de Treviño 1,468 (**primary, fetched**, INE table 2862); Valle de Villaverde 249 (**primary, fetched**, INE table 2893).
- **Country total:** **49,114,494, DERIVED and UNVERIFIED as a published figure**. It is my arithmetic sum of the 52 annex rows as transcribed by the fetch tool (fetch 25). The annex prints no national total, and a search for the number found nothing (search 14). Two internal checks support the transcription: Burgos (361,556) and Cantabria (593,964) in the INE municipal tables equal their annex rows, and Santa Cruz de Tenerife (1,082,421) also matched by accident in fetch 29.
- **Same source and date:** the units and the derived total are all from the Padrón at 1 Jan 2025 (BOE annex and INE Padrón tables, same RD). **Flag:** the national total is derived, not published.
- **Adds up:** units combined 11,073,824 = 22.55% of 49,114,494 (Catalonia 16.59%; Álava 0.70%; Bizkaia 2.38%; Gipuzkoa 1.49%; Navarra 1.39%; Treviño 0.0030%; Villaverde 0.0005%). The units do not overlap (Treviño is in Burgos and Villaverde in Cantabria, neither of which is in the list).
- **Conflicts:**
  - **Padrón vs Censo Anual.** The widely quoted 49,128,297 is the INE **Censo Anual de Población 2025** (fetch 23), a different series from the Padrón. Evidence that they differ: Catalonia is 8,146,265 in the Padrón but 8,124,126 in the census-based series (Idescat, snippet, UNVERIFIED). **Never divide Padrón units by 49,128,297.** If a census-based set is wanted, its regional figures have to be gathered separately (not done).
  - **Gipuzkoa** 733,149 (snippet, attributed to an INE "España en cifras" table, probably another series or date) vs 733,365 (BOE annex). **Chose the BOE annex.**
  - **Condado de Treviño** 1,472 (citypopulation.de "register") vs 1,468 (INE table 2862). **Chose INE.**
  - The quarterly ECP (49,077,984 provisional for 1 Jan 2025) is a third series; not used.

### 3.4 Brazil (IBGE)
- **Census 2022 (primary, fetched, SIDRA 4709):** Acre 830,018; Amapá 733,759; Amazonas 3,941,613; Mato Grosso 3,658,649; Pará 8,120,131; Rondônia 1,581,196; Roraima 636,707; Brazil 203,080,756. Same table, same reference date. The seven states combined: 19,502,073 = **9.60%** (Pará 4.00%, Amazonas 1.94%, Mato Grosso 1.80%, Rondônia 0.78%, Acre 0.41%, Amapá 0.36%, Roraima 0.31%).
- **Latest estimate, 1 Jul 2026 (primary, fetched, SIDRA 6579; national figure also in Poder360 and others):** Acre 887,794; Amapá 809,953; Amazonas 4,360,926; Mato Grosso 3,950,330; Pará 8,756,324; Rondônia 1,757,338; Roraima 761,012; Brazil 214,211,951. Combined 21,283,677 = **9.94%**.
- **1 Jul 2025 estimate (same table):** Acre 884,372; Amapá 806,517; Amazonas 4,321,616; Mato Grosso 3,893,659; Pará 8,711,196; Rondônia 1,751,950; Roraima 738,772; Brazil 213,421,037. Combined 21,108,082 = **9.89%**.
- **Conflicts:** the first census release (June 2023) gave 203,062,512; the current SIDRA value is 203,080,756 (chosen). The December 2022 "prévia" (207,750,291) is a modeled preview and is not a census result. The estimates sit about 10 million above the census count because they are built from projections with a coverage adjustment; never mix a census unit with an estimate total.

### 3.5 Indonesia (BPS, mid-2025)
- **Taken (secondary, fetched, en.wikipedia citing BPS 2026; bps.go.id returned 403):** Aceh 5,626,000; Papua Barat 587,600; Papua Barat Daya 636,400; Papua 1,073,600; Papua Tengah 1,492,300; Papua Pegunungan 1,484,900; Papua Selatan 549,700. **All UNVERIFIED against BPS directly.**
- **Country total:** **284,438,800, UNVERIFIED** (snippet in search 22 quoting "284.438,8" thousand from BPS's own page; page not identified). It agrees with the regional table on the same Wikipedia page, which the fetch tool summed to 284,438,400 (a 400-person gap, consistent with rounding 38 provinces to hundreds).
- **Same source and date:** the provinces and the total are both BPS mid-2025 projections, but they reached me through different secondary channels. **Flagged.**
- **Adds up:** seven provinces combined 11,450,500 = **4.03%** (Aceh 1.98%; Papua Tengah 0.52%; Papua Pegunungan 0.52%; Papua 0.38%; Papua Barat Daya 0.22%; Papua Barat 0.21%; Papua Selatan 0.19%). Plausibility: Papua Selatan was 542,100 at mid-2024 (snippet), so 549,700 at mid-2025 is +1.4%, a believable growth rate.
- **Other national series (do not mix):** SUPAS 2025 (the intercensal survey, released May 2026) gives 284.67 million, with no provincial breakdown found. Dukcapil civil registry: 282.48 million (June 2024) and 286.69 million (June 2025).

### 3.6 Thailand (DOPA registration, 31 December 2024; NSO census 2025 as an alternative set)
- **DOPA set:** Thailand 65,951,210 (snippets: Khaosod English 17 Jan 2025 and the NSO Statistical Yearbook 2025; consistent with the fetched Wikipedia footnote of 65,951,000). Pattani **740,904 UNVERIFIED** (snippet); Narathiwat **823,996 UNVERIFIED** (snippet); **Yala BLANK** (exact figure not found; the rounded 553,000 is in fetch 36). Rounded fetched values: Pattani 741,000; Yala 553,000; Narathiwat 824,000.
  - Adds up (exact where available): Pattani 1.12%, Narathiwat 1.25%. With the rounded figures, all three combined are about 2,118,000 ≈ 3.21% (rounded inputs; for orientation only, not an exact share).
- **NSO census set (Census Day 1 Apr 2025, PRELIMINARY; secondary, fetched from citypopulation.de citing NSO):** Pattani 668,941; Yala 566,239; Narathiwat 760,807; Thailand 70,275,751. Same source and date. Combined 1,995,987 = **2.84%** (Pattani 0.95%, Yala 0.81%, Narathiwat 1.08%). **UNVERIFIED against NSO's own table.** NSO's headline of about 70.3 million is confirmed by Nation Thailand (snippet).
- **Conflict:** registration and census disagree sharply for these provinces (Pattani registered 741k vs counted 669k; Narathiwat 824k vs 761k; Yala 553k vs 566k), and nationally (66.0 vs 70.3 million, because the census counts residents, including migrants, where they live). **Both sets are recorded; pick one and keep it whole.**
- **Latest DOPA total:** 65,809,011 at 31 Dec 2025 (snippet).

### 3.7 Philippines (PSA 2024 POPCEN, reference date 1 July 2024)
- **Taken:** Sulu 1,146,097; Philippines 112,729,484. **Secondary, fetched** (citypopulation.de citing PSA, fetch 38); the same Sulu figure is on barangaydirectory.com and de.wikivoyage (snippets), and the national figure is in The Star (19 Jul 2025, snippet). PSA's own table was not reached, so Sulu is **UNVERIFIED against PSA directly**.
- **Same source and date:** yes (one census, one reference date, one reproducing page).
- **Adds up:** Sulu 1.02%; rest 111,583,387. (2020 census: Sulu 1,000,108 of 109,035,343 = 0.92%.)
- **Tawi-Tawi:** reported separately in the same census (482,645, barangaydirectory.com, snippet; 440,276 in 2020), so Sulu's figure excludes Tawi-Tawi. The September 2024 Supreme Court ruling that Sulu is not part of BARMM (snippet) changes its regional grouping, not its provincial count.

### 3.8 Romania (INS resident population, 1 January 2025)
- **Taken (secondary, fetched, citypopulation.de citing INS):** Satu Mare 330,296; Bihor 556,606; Sălaj 211,033; Maramureș 450,711; Arad 410,085; Romania 19,036,031. **County figures UNVERIFIED against INS directly.**
- **Same source and date:** yes, one table and one vintage (the provisional 1 Jan 2025 release).
- **Adds up:** five counties combined 1,958,731 = **10.29%** (Bihor 2.92%; Maramureș 2.37%; Arad 2.15%; Satu Mare 1.74%; Sălaj 1.11%). Plausibility against the 2021 census on the same page: every county moved by less than 1% (Bihor +0.96%, Arad −0.01%).
- **Conflict:** INS later issued a **definitive** 1 Jan 2025 total of **19,043,151** (decline of 24,425; snippets 32, 35, 50), replacing the **provisional** 19,036,031 (decline of 31,545). The definitive county figures were **not** found. **Kept the provisional set together** so that units and total share one vintage. The share error from the 7,120-person national revision is about 0.04% relative, but county revisions are unknown.
- Arad is in the Vest development region, not Nord-Vest; this does not affect the split, but region-level shortcuts cannot be used for it.

### 3.9 South Korea (MOIS resident registration, end of 2024)
- **Taken:** South Korea 51,217,221 (**primary-reported, fetched**: newsis report of the MOIS 2024 analysis, 3 Jan 2025; also Asia Business Daily, snippet).
- **Jeju: BLANK, UNVERIFIED.** The only figures found are from k-calc.com, which cites MOIS but gives no reference date and showed two different 2024 values (672,252 in a search snippet; 671,064 on the fetched page). Neither can be paired safely with the national year-end total, so neither is used.
- **Same source and date:** cannot be checked until Jeju is found.
- **Other series:** end of 2025: 51,117,378 (snippet). Statistics Korea's 2024 register-based census (1 Nov 2024): about 51.81 million, with no Jeju figure found.

### 3.10 Chile (INE Censo 2024, first results)
- **Taken:** La Araucanía 1,010,423; Los Ríos 398,230; Los Lagos 890,284; Aysén 100,745; Magallanes 166,537; Chile 18,480,432.
- **Confirmation status:** the national figure is **primary, fetched** (INE release, fetch 41). The INE release itself gives no regional numbers (only that La Araucanía passed 1 million for the first time). The regional figures are **confirmed by secondary sources, via snippets**: Emol's table (Aysén 100,745 vs 103,158 in 2017; Magallanes 166,537 vs 166,533), the Wikipedia census table and La Batalla (La Araucanía, Los Ríos), and a local outlet quoting the INE Los Lagos regional director (Los Lagos). **All five match the values supplied in the brief; none was read from INE's own regional table, so they stay UNVERIFIED at the primary level.**
- **Same source and date:** yes (one census; fieldwork March–July 2024; all figures are persons counted).
- **Adds up:** combined 2,566,219 = **13.89%** (La Araucanía 5.47%; Los Lagos 4.82%; Los Ríos 2.15%; Magallanes 0.90%; Aysén 0.55%); rest 15,914,213.
- **Later official total:** INE published estimates and projections on the 2024 base in **January 2026**, giving **20,150,948 for 2026** (national; snippet citing INE's English press release). The gap to the census count reflects omission (about 1,391,332 people not counted, about 7%; snippet, UNVERIFIED). **Regional projections were due in the second half of 2026 and were not found.** Do not divide census-counted regions by the projected national total.

### 3.11 Ukraine (Derzhstat, present population, 1 January 2022)
- **Taken (secondary, fetched, en.wikipedia citing the Derzhstat collection "Number of Present Population of Ukraine, as of 1 January 2022"):** Luhansk 2,102,921; Donetsk 4,059,372; Kharkiv 2,598,961; Dnipropetrovsk 3,096,485; Zaporizhzhia 1,638,462 (also on citypopulation.de, snippet); Kherson 1,001,598.
- **Country total:** 41,167,335 (Derzhstat express release: 41,167.3 thousand; the exact figure is in snippets 43 and 46). **It excludes Crimea and Sevastopol**, per Derzhstat's standing convention as reported in the snippets; Wikipedia's Crimea (1,963,770) and Sevastopol (509,992) figures do not come from this Derzhstat total and were not used.
- **Same source and date:** yes (one Derzhstat collection, 1 Jan 2022), although the oblast figures came through Wikipedia and were not read from the Derzhstat PDF.
- **Adds up:** six oblasts combined 14,497,799 = **35.22%** (Donetsk 9.86%; Dnipropetrovsk 7.52%; Kharkiv 6.31%; Luhansk 5.11%; Zaporizhzhia 3.98%; Kherson 2.43%); rest 26,669,536.
- **Caveats:** the Donetsk and Luhansk figures include areas outside government control since 2014, estimated from administrative data; Wikipedia flags them as outdated and citypopulation.de calls them probably too high (snippet). The resident (permanent) population of 40,997.7 thousand is a different measure; do not mix the two.
- **Kherson, east/left of the Dnieper:** no source gives a left-bank total or share. The raion figures (fetch 45, sum = 1,001,598): Beryslav 94,103; Kherson 450,233; Henichesk 118,059; Kakhovka 216,458; Skadovsk 122,745. The three raions generally understood to lie wholly on the left bank (Henichesk, Kakhovka, Skadovsk; this geography is not sourced in this run) total 457,262 = 45.65% of the oblast. The Kherson raion straddles the river (Kherson city is on the right bank; the left-bank hromadas, such as Oleshky, are not broken out), so the true left-bank share is **above 45.65% by an unknown amount. Not estimated; CSV value left blank.**

---

## 4. Conflicts and how they were resolved (summary)

| Country | Conflict | Resolution |
|---|---|---|
| UK | Mid-2024 UK total: 69,281,400 (Sep 2025) vs 69,256,300 (revised, Oct 2026) | Revised value, same release as NI |
| Spain | Padrón vs Censo Anual (national 49,128,297 is census; Catalonia 8,146,265 Padrón vs 8,124,126 census) | Padrón throughout; national total derived from the Padrón annex and flagged |
| Spain | Gipuzkoa 733,149 (snippet) vs 733,365 (BOE) | BOE |
| Spain | Treviño 1,472 (citypopulation) vs 1,468 (INE) | INE |
| Brazil | 203,062,512 (first release) vs 203,080,756 (current SIDRA) | Current SIDRA |
| Indonesia | BPS projection 284,438,800 vs SUPAS 284.67 million vs Dukcapil 286.69 million | BPS projection (matches the provincial series); others noted |
| Thailand | DOPA registration vs NSO census 2025 (large provincial gaps) | Both sets recorded separately; keep each whole |
| Romania | 19,036,031 (provisional) vs 19,043,151 (definitive) | Provisional, because only its county figures were available |
| South Korea | Jeju 672,252 (snippet) vs 671,064 (fetched), no date | Neither used; blank |
| Chile | Counted 18,480,432 vs projected 20,150,948 (2026) | Census count, as requested; projection noted |
| Ukraine | Present 41,167,335 vs resident 40,997,700 | Present population (matches the oblast series) |

---

## 5. Dead ends (and where each died)

| Line | Dead end | Died at |
|---|---|---|
| Belgium DG 2025 | Searches 2 and 3 | 2: **query** (generic German terms pulled in Statista/Germany noise); 3: **source** (portal not indexed) |
| Belgium DG 2025 | Search 4; fetch 6 (2016 article) | **Source** |
| Belgium DG 2025 | Fetch 5, ostbelgienstatistik.be | **Source** (HTTP 403) |
| Belgium | Fetch 1, statbel.fgov.be | **Source** (CAPTCHA) |
| UK unrounded NI | Fetches 11, 12 | **Source** (HTTP 403) |
| Spain | Fetches 18, 22 (PDFs) | **Source** (compressed PDFs unreadable by the tool) |
| Spain | Fetches 20, 21 (INE table 2852) | **Query** (discontinued table chosen; series ends 2021) |
| Spain | Fetch 29 (INE table 2892) | **Query** (wrong table number guessed) |
| Spain | Search 14 (published Padrón total) | **Source** (no published national Padrón total found) |
| Indonesia | Fetch 33 (bps.go.id) | **Source** (HTTP 403) |
| Indonesia | Fetch 34 | **Query** (wrong Wikipedia title, 404) |
| Indonesia | Searches 20, 23, 49, 55 | **Source** (provincial BPS totals not indexed; only regency pages) |
| Thailand Yala | Searches 25, 27, 29 | **Source** (DOPA tables not indexed; only the rounded value is published in reachable pages) |
| Korea Jeju | Searches 36, 38, 39, 48, 51, 52, 53 | **Source** (MOIS and KOSIS tables not indexed; news gives national totals only) |
| Ukraine | Fetch 42 (minfin) | **Query** (guessed URL, 404) |
| Ukraine Kherson left bank | Searches 45, 54 | **Source** (no published left-bank aggregate) |

---

## 6. Open threads

1. **Spain:** find a *published* Padrón national total for 1 Jan 2025 (INE's Padrón table by province, current series) to replace the derived 49,114,494; or build a complete Censo Anual 2025 set (Catalonia, the three Basque provinces, Navarra, the two municipalities) if the census series is preferred.
2. **Belgium:** the German-speaking Community at 1 Jan 2025 (or 2026) from Statbel's municipal table (nine municipalities) or Ostbelgien Statistik.
3. **UK:** the unrounded mid-2024 NI and UK figures (ONS dataset "Estimates of the population for the UK, England, Wales, Scotland and Northern Ireland", Excel) if exact counts are needed.
4. **Indonesia:** read BPS's own provincial table (mid-2025) to confirm the seven provinces and the 284,438.8 thousand total; check whether BPS has re-based the series on SUPAS 2025.
5. **Thailand:** the exact DOPA Yala figure (31 Dec 2024) and confirmation of Pattani and Narathiwat; NSO's own preliminary census table for the three provinces.
6. **Philippines:** PSA's own 2024 POPCEN table for Sulu.
7. **Romania:** the definitive 1 Jan 2025 county figures (INS TEMPO POP105A) to pair with 19,043,151; the provisional 1 Jan 2026 release also exists.
8. **South Korea:** Jeju at 31 Dec 2024 from MOIS (jumin.mois.go.kr) or KOSIS.
9. **Chile:** INE's regional table to confirm the five regions at primary level; INE's regional projections (base 2024), due in the second half of 2026.
10. **Ukraine:** the oblast rows from the Derzhstat PDF itself; a hromada-level 2022 figure for the left-bank part of the Kherson raion to close the left-bank share.

---

## 7. STOP notes and integrity notes

- **No search was refused and no certificate check failed** during this run.
- **HTTP 403 responses** came from ostbelgienstatistik.be, parallelparliament.co.uk, admin.opendatani.gov.uk and bps.go.id. **STOP on each domain:** none was retried, and no other route into the same site was attempted. Where another *independent* source existed (ONS for the UK; Wikipedia citing BPS for Indonesia), it was used and labeled secondary.
- **Prompt injections:** the search tool reported embedded instructions in two results (a cavac.at Wikipedia mirror in search 24; a Wikipedia mirror in search 47). They were ignored; nothing from those pages was used.
- **Figures recalled from memory:** only as search terms (search 44, and the brief's Chilean figures in searches 40–41). None entered the CSV until a source confirmed it.
- **Locally saved fetch copies** (two PDFs and two ONS CSVs saved automatically by the fetch tool) were not opened, per the brief's rule against reading other files.

---

## 8. Count of searches and fetches

- **WebSearch: 55 used** (limit 60).
- **WebFetch: 45 used** (limit about 45).

---

## 9. FINAL summary

**Budget:** 55 searches and 45 fetches.

**Primary, fetched, same source and date (solid):** Belgium (three regions and total, 1 Jan 2025 and 1 Jan 2026); UK (NI and UK, mid-2024 revised and mid-2025); Spain's four provinces and two municipalities; Brazil (census 2022, and the 2025 and 2026 estimates); South Korea's national total; Chile's national total.

**Blank (value not found; not estimated):**
- South Korea: **Jeju** at end of 2024.
- Thailand: **Yala**, exact DOPA figure at 31 Dec 2024 (rounded 553,000 noted).
- Ukraine: **Kherson Oblast's left-bank share** (raion figures given; lower bound 45.65%).

**DERIVED (my arithmetic on one official document; not a published figure):**
- Spain: **national Padrón total 49,114,494** (also UNVERIFIED as published) and **Catalonia 8,146,265** (the latter matches a secondary attribution to INE).

**UNVERIFIED (secondary or snippet-only, or the vintage is uncertain):**
- Belgium: German-speaking Community **79,479 (1 Jan 2024, not 2025)**.
- UK: unrounded NI 1,927,855 (not used).
- Indonesia: **all seven provinces** (Wikipedia citing BPS) and the **total 284,438,800** (snippet).
- Thailand: **Pattani 740,904; Narathiwat 823,996** (snippets); the **whole 2025 census set** (citypopulation.de citing NSO, preliminary).
- Philippines: **Sulu 1,146,097** and the total (citypopulation.de citing PSA; PSA not reached).
- Romania: **all five counties and the total** (citypopulation.de citing INS; provisional vintage; definitive counties not found).
- Chile: **the five regional figures** at the primary level (secondary sources agree with the brief's values; INE's own regional table not read); the omission figure 1,391,332.
- Ukraine: **the six oblasts** (Wikipedia citing Derzhstat) and the total's exact unit figure (snippets; it agrees with Derzhstat's 41,167.3 thousand).
