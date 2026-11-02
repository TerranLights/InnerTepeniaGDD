# Run 4 Research A: population, income and inequality for 9 new places + 43-country calibration set

**Date:** 2026-11-02 · **Tools:** WebSearch and WebFetch only (no curl, no shell downloads) · **Files written:** `A_new_places.csv`, `A_calibration_43.csv`, this log. No other file was read or edited.

**Budget used:** **51 WebSearch calls** (limit 60) · **46 WebFetch calls** (limit about 50).

---

## 0. Conventions and method

- **Gini scale:** every Gini in both CSVs is on a **0–100 scale** (the World Bank's scale). Official figures published on a 0–1 scale (Taiwan 0.341, Hong Kong 0.397, Macau 0.324) are shown ×100. The 0–1 originals are quoted in the notes.
- **Which source goes in the value column:**
  - **GDP per person:** World Bank `NY.GDP.PCAP.CD` wherever it exists (Austria, Guatemala, Hong Kong, Luxembourg, Macau, Mongolia, Kosovo). The official national figure goes in the notes. Taiwan (not in World Bank data) uses DGBAS. North Korea uses the Bank of Korea's GNI per person, converted by me (see §3).
  - **Gini:** the World Bank value wherever it exists (Austria, Guatemala, Luxembourg, Mongolia, Kosovo), **so the new places sit on the same basis as the calibration set.** The official or Eurostat figure goes in the notes. Taiwan, Hong Kong and Macau have no World Bank Gini, so their official figures are used, and each basis is labeled.
  - **Population:** the latest official figure where I could confirm it (Taiwan, Hong Kong, Macau, Austria, Luxembourg, Kosovo, Kırklareli). The World Bank (UN-based) value is used where the official figure could not be confirmed (Mongolia, Guatemala) and for North Korea (UN estimate, as the brief asked).
  - **Pairing caution:** where the population is official and the GDP per person comes from the World Bank, multiplying the two mixes bases. Each row's notes give the World Bank 2025 population so you can pair like with like.
- **World Bank API:** I used `mrnev=1` (most recent **non-empty** value) rather than `mrv=1`. `mrv=1` can return a null for a country that has no value in the latest year; `mrnev=1` returns each country's own latest available year. The API header reported `lastupdated: 2026-10-08` on every call.
- **Transcription check:** WebFetch passes the page through a summarizing model, so every value was read back by that model, not taken from raw JSON. **All 47 Gini values were fetched twice** (plain call, then the `footnote=y` call) **and matched exactly.** The population and GDP values were fetched once each, so a residual transcription risk remains for them. If an exact digit matters, re-pull the API raw.
- **Verification labels used in notes:** "page read" = I opened the source. "Search snippet" = seen only in search-result text. **UNVERIFIED** = a single secondary source, or sources disagreeing with no resolution.

---

## 1. Searches (verbatim)

| # | Query (verbatim) | Mode / filter | What it returned | Outcome |
|---|---|---|---|---|
| 1 | `DGBAS 2025 GDP per capita US dollars Taiwan national accounts preliminary` | standard | News quoting DGBAS: 2025 per capita GDP US$39,477; earlier forecasts 38,066 (Aug 2025) and 38,748 | Lead on the Taiwan GDP figure |
| 2 | `Taiwan 2025 per capita GDP US$ revised DGBAS August 2026` | standard | Same figures; no August 2026 revision; CBC annual report gives 2025 growth 8.68% | August revision not found |
| 3 | `"Preliminary Estimate for 2026Q2" Outlook per capita GDP Taiwan` | standard | Q2 2026 growth 12.93%; 2026 forecast 11.05%; 2026 per capita forecast US$45,610 (Taiwan News) | No 2025 revised figure |
| 4 | `主計總處 114年 平均每人GDP 美元 概估 115年8月` | standard | Older forecast US$38,748 for 2025; nothing from Aug 2026 | Dead end (query) |
| 5 | `"114年" 平均每人GDP 3萬9 美元 主計總處 國民所得 統計` | standard | Same older forecasts; DGBAS yearbook PDF link | Dead end (query) |
| 6 | `Taipei Times August 2026 DGBAS per capita GDP US$45,610 last year` | standard | Irrelevant (Djibouti, US, Bahamas) | **Dead end (query)** |
| 7 | `"39,477" Taiwan per capita GDP 2025` | standard | Confirms US$39,477 (DGBAS specialist, Feb 2026, via CNA/OCAC/ANI); IntelliNews cites US$39,489 (IMF) | **Figure taken:** Taiwan GDP |
| 8 | `Taiwan 2025 Survey of Family Income and Expenditure Gini coefficient disposable income quintile ratio 6.` | standard | 2025 quintile ratio 6.2 (TaiwanPlus); 2024 Gini 34.1 (Statista); 2023 0.339 | Lead on the Gini |
| 9 | `114年家庭收支調查 吉尼係數 可支配所得 6.2倍` | standard | Latest report found is 113 (2024); no 2025 Gini | Dead end (query) |
| 10 | `Focus Taiwan income gap 2025 Gini coefficient DGBAS household survey 14-year high` | standard | TaiwanInsight cites official 0.341; tax-based Gini 0.272 is a different measure | 2025 Gini not found |
| 11 | `Taiwan population end of 2025 Ministry of the Interior household registration total 23.` | standard | 23,299,132 at end-Dec 2025 (Focus Taiwan; Taiwan News); age breakdown | **Figure taken:** Taiwan population |
| 12 | `Hong Kong 2021 Population Census thematic report household income distribution Gini coefficient original post-tax post-social transfer` | standard | Only 2016 (0.539 original; 0.473 post-tax post-transfer) and 2011 figures | 2021 not found |
| 13 | `"Household Income Distribution in Hong Kong" 2021 Population Census Gini coefficient 2023 press release` | standard | Same 2016 figures; data.gov.hk catalog entry | 2021 not found |
| 14 | `Hong Kong Gini coefficient 2021 census 0.5 "post-tax post-social transfer" household income` | standard; domains censtatd.gov.hk, info.gov.hk, legco.gov.hk, scmp.com, news.gov.hk | LegCo paper (Apr 2025): latest is the 2021 per capita post-tax post-social-transfer Gini = 0.397, published 2023 | **Figure taken:** HK Gini |
| 15 | `2021 Population Census thematic report household income distribution Gini coefficient 0.397 per capita original household income` | standard; domains censtatd.gov.hk, info.gov.hk, povertyrelief.gov.hk | 2016 per capita original 0.499 and per capita post-tax post-transfer 0.420; 2021 median income | 2016 per capita figures |
| 16 | `C&SD announces results of study on household income distribution 2023 Gini Coefficient 2021 original monthly household income 0.5` | extended | US Census and CBO material only | **Dead end (query)** |
| 17 | `2021年人口普查 主題性報告 香港的住戶收入分布 堅尼系數 原本住戶收入 除稅及福利轉移後` | standard | HK01: 2021 report kept only one Gini (0.397, down from 0.420 in 2016) | Lead → fetch 33 |
| 18 | `Hong Kong mid-2026 population provisional figure Census and Statistics Department` | standard; domains info.gov.hk, censtatd.gov.hk, news.gov.hk | Mid-2026 provisional 7,518,300 (released 2026-08-18); mid-2025 revised 7,498,900; end-2025 revised 7,508,700 | **Figure taken:** HK population |
| 19 | `Hong Kong per capita GDP 2025 HK$ US$ Census and Statistics Department gross domestic product 2025 annual` | same domains | Per capita GDP 2025 HK$444,044 (Annual Digest 2026; Q1 2026 release) | Official HK$ figure |
| 20 | `Macao DSEC Gini coefficient household budget survey 2022/2023 income distribution` | standard | HIES 2023/2024: per capita Gini 0.324; 0.396 excluding subsidies | Lead → fetch 34 |
| 21 | `Macao total population end of June 2026 DSEC; Macao per-capita GDP 2025 MOP US$` | standard; domains gov.mo, dsec.gov.mo, gcs.gov.mo, macaudailytimes.com.mo, macaonews.org, macaubusiness.com | End-June 2026: 686,500; end-2025: 688,900 | **Figure taken:** Macau population |
| 22 | `Macao GDP 2025 whole year per-capita GDP MOP DSEC real growth` | same domains | Per capita GDP 2025 MOP607,263 (+4.3%); Macau Business ≈ US$75,500 | Official MOP figure |
| 23 | `Mongolia National Statistics Office 2025 GDP per capita US dollars population end of 2025 1212.mn` | standard | Aggregators only (7,108 WB-based; 7,079 IMF) | No NSO figure |
| 24 | `Montsame Mongolia population 2025 year-end National Statistics Office million; GDP per capita 2025 USD NSO` | standard; domains montsame.mn, 1212.mn, nso.mn, ikon.mn, news.mn | NSO homepage "3,660,609" (undated); 2024 per capita US$6,898 (Montsame); NSO bulletin PDF link | Partial |
| 25 | `"population of Mongolia" reached 2025 end of year NSO 3.5 million OR 3.6 million` | standard | CEIC end-2024 3.5 million (NSO); model estimates only | No official 2025 figure |
| 26 | `Mongolia Household Socio-Economic Survey 2024 poverty rate Gini coefficient NSO World Bank results` | standard | 2022 Gini 31.4 (WB), CEIC 0.314 (2018 0.327); HSES 2024 Gini not published in results | Cross-check of the Gini |
| 27 | `Statistik Austria population 1 January 2026 Bevölkerung Jahresbeginn 2026` | standard | Preliminary 9,219,113 (2026-02-09); later 9,215,956 (2026-06-29 release) | **Figure taken:** Austria population |
| 28 | `Statistik Austria EU-SILC 2025 Gini-Koeffizient Einkommen; BIP pro Kopf 2025 Euro Österreich` | standard | EU-SILC 2025 release (2026-04-29), no Gini value in snippets | Led to Eurostat fetch 37 |
| 29 | `STATEC population Luxembourg 1er janvier 2026 habitants` | standard | 690,959 on 1 Jan 2026 (Chronicle.lu); 691,000 (Paperjam citing STATEC) | **Figure taken:** Luxembourg population |
| 30 | `Kosovo Agency of Statistics SILC Gini coefficient 2023 OR 2024 income inequality ASK` | standard | Eurostat: Kosovo 2018 only (44.2); WB 38.3 (2022) | Cross-check of the Gini |
| 31 | `Bank of Korea North Korea 2025 economic growth estimate per capita gross national income million won` | standard | BOK 2026-07-31: per capita GNI 1,873,000 won; GNI 48.5 trillion won ($33.79bn per Korea Times); growth 3.5% | **Figure taken:** NK income |
| 32 | `North Korea per capita gross national income 2025 1.873 million won dollars Bank of Korea` | standard | Confirms 1.87 million won; 2024 was 1.719 million won; no published per-person US$ figure | Confirmation |
| 33 | `2025 annual average won-dollar exchange rate Bank of Korea 1,42 OR 1,43 OR 1,44 won per dollar yearly average` | standard | 2025 annual average 1,422.16 (base rate, Kyunghyang/JoongAng); FRED 1,421.3963; year-end close 1,439 | Exchange rate for the conversion |
| 34 | `World Population Prospects 2024 Democratic People's Republic of Korea population 2025 2026 thousands UN DESA` | standard | 2025: 26,571,036 (WPP 2024 via Worldometers, statbase.ru); 2024: 26,498,823 | Cross-check of the NK population |
| 35 | `INE Guatemala proyección de población 2025 2026 total habitantes estimaciones censo 2018` | standard | INE (secondary site): 18,079,810 (2025), 18,312,373 (30 June 2026); WB 18,687,881 | INE figure UNVERIFIED |
| 36 | `proyecciones INE Guatemala población 2025 18 millones departamentos más poblados Petén habitantes` | standard; domains agn.gt, ine.gob.gt, prensalibre.com, lahora.gt, censopoblacion.gt | Older AGN article (17.4 million, undated); INE projections page | Dead end (source not surfaced) |
| 37 | `Banguat PIB per cápita 2025 dólares Guatemala Banco de Guatemala producto interno bruto per cápita US$` | standard | Banguat 2023 US$5,923 (Prensa Libre); Focus Economics 2025 US$6,506 (Macrobond) | No Banguat 2025 figure |
| 38 | `"PIB per cápita" Guatemala 2025 Banguat "US$6" OR "US$7" récord` | standard | Same; no Banguat 2025 figure | **Dead end (query)** |
| 39 | `ENCOVI 2023 pobreza por departamento Petén porcentaje INE Guatemala resultados` | standard | National poverty 56%; IPM-Gt; Petén's monetary rate not shown | Petén not found |
| 40 | `Petén pobreza total ENCOVI 2023 "Petén" por ciento pobreza monetaria departamento` | standard | IPM national 57.68%; ENCOVI 2011 Petén 65.67% (old) | Petén 2023 not found |
| 41 | `Prensa Libre Encovi 2023 pobreza departamentos Alta Verapaz Petén Sololá porcentaje pobreza 2024 INE resultados departamentales` | standard | Alta Verapaz 90.3% / 83.1% (conflicting); no Petén figure | **Dead end (query)** |
| 42 | `Kosovo Agency of Statistics GDP per capita 2025 euro; Kosovo population estimate 2025 census 2024 1,586,659` | standard | Focus Economics EUR 6,956 (2025, Macrobond); WB US$7,899 | No KAS euro figure. **See §7: a recalled number was typed into this query.** |
| 43 | `Kosovo 2024 census final results total population resident ASK announced` | standard | Conflict: 1,602,515 (PM's office, final) vs 1,586,659 (Periskopi, Albanian Times) | Led to fetch 45 |
| 44 | `Kırklareli nüfusu 2025 TÜİK adrese dayalı nüfus kayıt sistemi sonuçları` | standard | 2024: 379,031 (local paper); Türkiye 2025 total 86,092,168 | 2025 provincial figure not found |
| 45 | `"Kırklareli" nüfusu 2025 yılında kişi oldu ADNKS Şubat 2026` | standard | Same 2024 figure; real-estate sites with absurd values (ignored) | **Dead end (query)** |
| 46 | `PIB por departamento Guatemala Petén producto interno bruto departamental Banguat estimación regional per cápita` | standard | **Banguat publishes departmental GDP per person, 2013–2024**; Petén share 2.9% (2024) / 3.0% (2023p) | Official series exists |
| 47 | `"Petén" PIB per cápita departamental Banguat quetzales 2024 departamentos más bajos Sacatepéquez Guatemala Escuintla` | standard | Sacatepéquez 2024 = 49,030.3; no Petén row in the snippet | Petén value not reached |
| 48 | `"PIB Per Capita por departamento" Petén 2024 cifras en quetzales año de referencia 2013` | extended; domain banguat.gob.gt | Table confirmed (2014–2024, nominal quetzales, INE populations, 2024 preliminary); snippet cut before Petén's values | **Dead end (source format)** |
| 49 | `Taiwan Gini coefficient 0.341 2024 household income survey DGBAS disposable income top 20% bottom 20% 6.` | standard; domains focustaiwan.tw, taipeitimes.com, taiwannews.com.tw, stat.gov.tw, dgbas.gov.tw, taiwaninsight.org | DGBAS 113 (2024) FIES report: household disposable-income Gini 0.341 (2023: 0.339); quintile ratio 6.14 | **Figure taken:** Taiwan Gini |
| 50 | `il il nüfus 2025 TÜİK listesi Kırklareli Edirne Tekirdağ 2025 nüfusu açıklandı` | standard | Tekirdağ 2025 1,208,441; no Kırklareli 2025 figure | **Dead end (query)** |
| 51 | `"3,660,609" Mongolia population` | standard | No source contains that number | **Dead end (query)**; figure stays UNVERIFIED |

*Numbers that appear inside queries (for example "1,42 OR 1,43", "0.5", "23.", "US$45,610") are search terms, not data. None was used as a value unless a result confirmed it.*

---

## 2. Pages fetched

| # | URL | Result |
|---|---|---|
| 1 | `https://api.worldbank.org/v2/country/CHN;USA;JPN;DEU;FRA;GBR;ITA;KOR;RUS;ESP/indicator/NY.GDP.PCAP.CD?format=json&mrnev=1&per_page=100` | 10 records, all 2025 |
| 2 | `…/CAN;MEX;BRA;IDN;AUS;NLD;BEL;SWE;ARG;NOR/indicator/NY.GDP.PCAP.CD?…` (same parameters) | 10 records, all 2025 |
| 3 | `…/FIN;ZAF;NZL;CHL;URY;POL;THA;CZE;UKR;VNM/indicator/NY.GDP.PCAP.CD?…` | 10 records, all 2025 |
| 4 | `…/PHL;ROU;MYS;HUN;SVK;BLR;HRV;BGR;SRB;LTU;SVN;LVA;EST/indicator/NY.GDP.PCAP.CD?…` | 13 records, all 2025 |
| 5 | `…/MNG;AUT;GTM;LUX;XKX;HKG;MAC;PRK/indicator/NY.GDP.PCAP.CD?…` | 7 records (2025); **PRK absent** (no WB GDP for North Korea) |
| 6–10 | the same five country groups, `indicator/SP.POP.TOTL?format=json&mrnev=1&per_page=100` | all records 2025; PRK present (UN-based) |
| 11–15 | the same five groups, `indicator/SI.POV.GINI?format=json&mrnev=1&per_page=100` | years vary; **NZL absent**; HKG, MAC, PRK absent |
| 16 | `https://api.worldbank.org/v2/country/NZL;HUN/indicator/SI.POV.GINI?format=json&date=2010:2025&per_page=100` | NZL null for all of 2010–2025; HUN last non-null 2017 (30.6), null for 2018–2025 |
| 17 | `https://eng.stat.gov.tw/` | Navigation only; links to National Accounts and FIES |
| 18 | `https://eng.stat.gov.tw/cl.aspx?n=2315` | Indicator names only, no values (rendered client-side) |
| 19 | `https://eng.stat.gov.tw/cp.aspx?n=4212` | No values; links to an xlsx file |
| 20 | `https://eng.stat.gov.tw/cl.aspx?n=2332` | Navigation only |
| 21 | `https://focustaiwan.tw/business/202608140022` | Aug 2026 growth forecasts; no per capita figure |
| 22 | `https://eng.stat.gov.tw/News.aspx?n=2337&sms=10854` | List of GDP releases (Aug 2026 release = s=236587; Feb 2026 = s=235721) |
| 23 | `https://eng.stat.gov.tw/News_Content.aspx?n=2337&s=236587` | No per capita GDP in HTML; full text in a PDF |
| 24 | `https://ws.dgbas.gov.tw/001/Upload/464/relfile/10854/236587/enewstotal11508.pdf` | **Unreadable** (compressed PDF); the tool saved the binary locally, and I did not open it (see §7) |
| 25 | `https://eng.stat.gov.tw/Point.aspx?sid=t.1&n=4200&sms=11713` | Unrendered template placeholders only |
| 26 | `https://eng.stat.gov.tw/News_Content.aspx?n=2337&s=235721` | No per capita figure in HTML; PDF attachment only |
| 27 | `https://www.taiwannews.com.tw/en/news/6412537` | Q2 growth; no per capita figure |
| 28 | `https://ocacnews.net/article/418912` | Empty page |
| 29 | `https://www.taiwanplus.com/news/taiwan-news/economy/260816006/household-income-gap-reaches-14-year-high-in-taiwan` | 2025 quintile ratio 6.2 (top 20% ≈ US$78,000, bottom ≈ US$12,000); no Gini |
| 30 | `https://data.gov.hk/en-data/dataset/hk-censtatd-census21c-b1120108/resource/803adb30-e116-4a4e-b33a-31b6f031442e` | **HTTP 404** |
| 31 | `https://www.legco.gov.hk/yr2025/english/panels/ws/papers/ws20250414cb1-810-1-e.pdf` | **Certificate check failed. STOP** (see §6) |
| 32 | `https://www.censtatd.gov.hk/en/data/stat_report/product/B1120108/att/B11201082021XXXXB0100.pdf` | **Unreadable** (compressed PDF; binary saved locally, not opened) |
| 33 | `https://www.hk01.com/深度報道/905725/堅尼系數被-縮水-收入差距再擴大` | **Read.** 2021: 0.397 (vs 0.420); economically active households 0.376 (vs 0.402); the 2021 report kept only the per capita post-tax post-transfer measure, and C&SD said the other 14 could not be provided. Dated 2023-06-07 |
| 34 | `https://www.gov.mo/en/news/343962/` | **Read.** HIES 2023/2024: per capita Gini 0.324 (2017/18 0.315); 0.396 excluding subsidies; 204,177 households; released 2024-09-20 |
| 35 | `https://en.nso.mn/home` | Agency name only (client-side rendering) |
| 36 | `https://www.1212.mn/uploads/1773909111705-Bulletin%202026%20I%20en.pdf` | **Certificate check failed. STOP** (see §6) |
| 37 | `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/ilc_di12?geo=AT&geo=LU&geo=HU&geo=XK&sinceTimePeriod=2022&format=JSON&lang=EN` | AT 27.8/28.1/28.4/27.4; LU 29.1b/30.6/30.1/30.5b; HU 26.9/28.6/28.0/29.5 (2022–2025); XK no data; updated 2026-10-20 |
| 38 | `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_pc?geo=AT&geo=LU&unit=CP_EUR_HAB&na_item=B1GQ&sinceTimePeriod=2023&format=JSON&lang=EN` | EUR per person: AT 52,560/54,470/56,300; LU 122,970/128,710p/132,950p (2023–2025); updated 2026-10-22 |
| 39 | `https://api.worldbank.org/pip/v1/pip?country=MNG,GTM,XKX&year=all&fill_gaps=false&format=csv` | Welfare types: MNG consumption (0.3142 in 2022); GTM income (0.4521 in 2023); XKX income, SILC-C (0.5741 / 0.4938 / 0.3831 for 2020–22) |
| 40 | `https://api.worldbank.org/pip/v1/pip?country=CHN,…,LUX&year=MRV&fill_gaps=false&format=csv` (all 43 + AUT, LUX) | **HTTP 404**. Bad request on my side: `year=MRV` is probably invalid, or NZL has no data. Replaced by fetches 41–43 |
| 41 | `https://api.worldbank.org/v2/country/CHN;IDN;THA;PHL;RUS;SRB;VNM;ZAF;MYS;UKR;BLR;HUN;JPN;KOR/indicator/SI.POV.GINI?format=json&mrnev=1&per_page=100&footnote=y` | Footnotes give the survey and the income-or-consumption basis; values match fetches 11–15 |
| 42 | `…/USA;DEU;FRA;GBR;ITA;ESP;CAN;MEX;BRA;AUS;NLD;BEL;SWE;ARG;NOR;FIN;CHL/indicator/SI.POV.GINI?…&footnote=y` | As above; ARG is "Urban only" |
| 43 | `…/URY;POL;CZE;ROU;SVK;HRV;BGR;LTU;SVN;LVA;EST;AUT;LUX;MNG;GTM;XKX/indicator/SI.POV.GINI?…&footnote=y` | As above; **ROU and XKX footnotes empty** |
| 44 | `https://agn.gt/segeplan-presenta-los-mapas-de-pobreza-2023/` | **HTTP 403 (site refused access). Not retried** |
| 45 | `https://kryeministri.rks-gov.net/en/blog/the-first-final-results-from-the-census-of-population-households-and-housing-in-kosovo-are-presented/` | **Read.** "total resident population in Kosovo is 1,602,515", dated Prishtina, 19 December 2024 |
| 46 | `https://www.banguat.gob.gt/sites/default/files/banguat/Publica/PIB_Regional/8_PIB_Per_Capita_por_departamento.pdf` | **Unreadable** (compressed PDF; binary saved locally, not opened) |

---

## 3. Figures taken, and where from

### Part 1: new places

| Place | Field | Value | Source | Check |
|---|---|---|---|---|
| Taiwan | population | 23,299,132 (end-Dec 2025) | Ministry of the Interior via Focus Taiwan and Taiwan News (search 11) | Two outlets agree; age groups sum exactly |
| Taiwan | GDP/person | US$39,477 (2025, DGBAS preliminary of 2026-02-13) | News quoting DGBAS (searches 1, 7) | IMF-based 39,489 agrees within 0.03%. **August 2026 revision not found** |
| Taiwan | Gini | 0.341 → 34.1 (2024, household disposable income) | DGBAS FIES 2024 report (search 49) | TaiwanInsight 0.341; Statista 34.1 |
| Hong Kong | population | 7,518,300 (mid-2026, provisional) | C&SD release of 2026-08-18 (search 18) | Usual + Mobile Residents sum exactly; mid-2025 revised figure equals the WB 2025 value |
| Hong Kong | GDP/person | US$56,983.07 (WB 2025) | Fetch 5 | C&SD HK$444,044 → implied HK$7.79/US$ (my arithmetic; used only as a consistency check) |
| Hong Kong | Gini | 0.397 → 39.7 (2021, per capita post-tax post-social-transfer) | HK01 (fetch 33); LegCo snippet (search 14) | Two sources. **Original-income 2021 Gini not published** |
| Macau | population | 686,500 (end-June 2026) | DSEC Q2 2026 (search 21) | Female + male sum exactly |
| Macau | GDP/person | US$75,901.75 (WB 2025) | Fetch 5 | DSEC MOP607,263 → implied MOP8.00/US$; Macau Business ≈ US$75,500 |
| Macau | Gini | 0.324 → 32.4 (2023/2024, per capita, after subsidies) | gov.mo release (fetch 34) | Page read |
| Mongolia | population | 3,568,978 (2025, WB) | Fetch 10 | NSO not reachable (STOP) |
| Mongolia | GDP/person | US$7,108.23 (WB 2025) | Fetch 5 | IMF 7,079; NSO 2024 US$6,898 |
| Mongolia | Gini | 31.4 (2022, consumption) | Fetches 15, 39, 43 | PIP 0.3142; CEIC 0.314 |
| Austria | population | 9,215,956 (1 Jan 2026) | Statistik Austria release of 2026-06-29 (search 27) | Preliminary 9,219,113; WB 9,208,163 |
| Austria | GDP/person | US$62,930.04 (WB 2025) | Fetch 5 | Eurostat EUR 56,300 |
| Austria | Gini | 31.2 (WB 2023, income) | Fetches 15, 43 | Eurostat EU-SILC 2025: 27.4 (different basis) |
| Guatemala | population | 18,687,881 (WB 2025) | Fetch 10 | INE projection 18,079,810 (2025) **UNVERIFIED** |
| Guatemala | GDP/person | US$6,598.18 (WB 2025) | Fetch 5 | Banguat 2025 not found |
| Guatemala | Gini | 45.2 (2023, income, ENCOVI) | Fetches 15, 39, 43 | PIP 0.4521 |
| Petén | GDP/person | **blank** | Official Banguat series exists (2013–2024) but could not be read | Share of national GDP 2.9% (2024) |
| Petén | poverty | **blank** | INE ENCOVI 2023 departmental figure exists but was not found | ENCOVI 2011: 65.67% (UNVERIFIED, old) |
| North Korea | population | 26,571,036 (1 July 2025) | UN WPP 2024 via WB (fetch 10) | Worldometers and statbase.ru agree |
| North Korea | GNI/person | KRW 1,873,000 → **US$1,317** (my conversion at 1,422.16 KRW/US$) | BOK via Korea Times and others (searches 31, 32); exchange rate (search 33) | Range US$1,305–1,318 depending on the rate used |
| North Korea | Gini | **none exists** | — | — |
| Luxembourg | population | 690,959 (1 Jan 2026) | STATEC via Chronicle.lu (search 29) | Paperjam (STATEC) 691,000 |
| Luxembourg | GDP/person | US$147,252.18 (WB 2025) | Fetch 5 | Eurostat EUR 132,950 (provisional) |
| Luxembourg | Gini | 33.6 (WB 2023, income) | Fetches 15, 43 | Eurostat EU-SILC 2025: 30.5 (break in series) |
| Kosovo | population | 1,602,515 (2024 census, final) | PM's office (fetch 45) | Conflicts with 1,586,659 (§4) |
| Kosovo | GDP/person | US$7,899.42 (WB 2025) | Fetch 5 | KAS euro figure not found |
| Kosovo | Gini | 38.3 (WB 2022, income, SILC) | Fetches 15, 39 | Unstable series (§4) |
| Kırklareli | population | 379,031 (31 Dec 2024) | Local newspaper citing TurkStat (search 44) | **UNVERIFIED** (single secondary source); 2025 not found |

**North Korea conversion, shown in full:** 1,873,000 ÷ 1,422.16 = 1,317.01 → **US$1,317**. At FRED's 1,421.3963 it is US$1,317.72. At the rate implied by Korea Times (48.5 trillion won ÷ US$33.79 billion ≈ 1,435.3) it is US$1,304.92. This conversion is arithmetic on two sourced numbers; no value was invented. The concept is **GNI**, not GDP.

### Part 2: calibration set

All 43 rows come from fetches 1–4 and 6–9 (population and GDP, all 2025) and fetches 11–14 (Gini). The income-or-consumption basis comes from the footnotes in fetches 41–43. Values were copied with the precision the API returned.

**Consumption-based Ginis: 7 in the calibration set** (China, Indonesia, South Africa, Thailand, Ukraine, Vietnam, Belarus), **plus Mongolia among the new places.** **Every other calibration value is income-based**, except Romania, whose footnote is empty. Consumption Ginis normally run lower than income Ginis for the same country, so a calibration fit should either add a basis flag or treat these 8 separately.

**Gini year spread:** 2017 (Hungary); 2020 (Japan, Australia, Ukraine, Belarus); 2021 (UK, South Korea, Netherlands, Malaysia); 2022 (China, Germany, Canada, Vietnam, South Africa); 2023 (most of Europe, Russia, Philippines, Serbia); 2024 (US, Argentina, Brazil, Mexico, Chile, Thailand, Uruguay); 2025 (Indonesia).

---

## 4. Conflicts and how I resolved them

1. **Kosovo population: 1,602,515 vs 1,586,659.** The PM's office page (read, dated 19 Dec 2024) gives 1,602,515 as the "total resident population." Periskopi and Albanian Times give 1,586,659, which appears to match the July 2024 preliminary count. Albanian Times says the 1,602,515 figure excludes diaspora whose registration was still ongoing. **Chose 1,602,515** because it is the later official release and I read the page itself. The WB 2025 value (1,576,876) is lower than both.
2. **Guatemala population: INE vs UN.** INE's projection for 2025 (18,079,810, reported second-hand) is about 608,000 below the WB/UN figure (18,687,881). **Chose the WB value**, because the INE figure could not be confirmed at INE, and the WB value pairs consistently with the WB GDP per person. The INE figure is in the notes, marked UNVERIFIED.
3. **Gini basis for the European new places (Austria, Luxembourg).** The WB per-person Ginis (31.2, 33.6) and the official EU-SILC equivalised-income Ginis (27.4, 30.5) differ by about 3–4 points. **Chose WB** for consistency with the calibration set. Eurostat's figures are recorded in the notes.
4. **Hong Kong Gini basis.** The latest published figure (0.397) is per capita post-tax post-social-transfer. The 2016 household-level original-income Gini (0.539) is a different measure and is not comparable. **Used 0.397 for 2021** and recorded both 2016 values.
5. **Macau US$ conversion.** WB US$75,902 vs Macau Business ≈ US$75,500 for the same DSEC MOP figure, a 0.5% gap. **Used WB.**
6. **Taiwan GDP vintage.** DGBAS preliminary (Feb 2026) US$39,477 vs IMF-based US$39,489. These agree, but DGBAS's own August 2026 revision may differ, and I could not read it. **Used 39,477**, flagged as an open thread.
7. **North Korea population vs the BOK's base.** The BOK's totals imply about 25.9 million people (48.5 trillion ÷ 1.873 million, my arithmetic). The UN figure is 26.57 million. The brief asks for the UN population, which I used. The mismatch is recorded so that population × income is not read as reproducing the BOK's total GNI.
8. **Kosovo Gini series.** PIP: 0.574 (2020) → 0.494 (2021) → 0.383 (2022). This is an implausibly fast fall for real inequality and probably reflects survey or method changes. **Used the latest value (38.3) as the WB reports it**, flagged as unstable.
9. **Luxembourg and Austria euro-to-dollar factors.** WB/Eurostat gives 1.108 for Luxembourg and 1.118 for Austria, which should be one exchange rate. The gap means the population bases or data vintages differ. Not resolved; recorded.

---

## 5. Dead ends: where each one died

| Target | Died at | Detail |
|---|---|---|
| Taiwan 2025 GDP, DGBAS revised (Aug 2026) | **Source (format)** | DGBAS English pages render client-side; the release PDFs are compressed and unreadable to the fetch tool. The figure exists. |
| Taiwan 2025 Gini | **Query** | The 2025 survey was released in Aug 2026 (the quintile ratio 6.2 was found); the Gini was probably published too but never surfaced. |
| Hong Kong 2021 original-income Gini | **Source** | Not published (HK01: C&SD said it could not be provided). |
| Hong Kong 2021 thematic report PDF | **Source (format)** | Unreadable PDF; the data.gov.hk resource page returned 404. |
| Mongolia NSO 2025 population and GDP | **Source** | Certificate failure on 1212.mn (STOP); en.nso.mn renders client-side. |
| Mongolia "3,660,609" date | **Query** | No source carries the number. |
| Mongolia HSES 2024 Gini | **Source** | Probably not yet published (searches found the microdata catalog only). |
| Guatemala INE population at INE | **Source** | Projections are in Excel and PDF files; the INE page was not opened (budget). |
| Guatemala Banguat 2025 US$ per person | **Query / source** | The series reaches 2025 per Alphacast, but no snippet showed the value. |
| Petén GDP per person | **Source (format)** | The official Banguat table exists; its PDF is unreadable to the fetch tool, and search snippets truncate before the Petén row. |
| Petén poverty (ENCOVI 2023) | **Query** | INE published departmental figures (Aug 2024); not surfaced in 3 searches; the AGN page returned 403. |
| Kosovo KAS GDP in euros | **Query** | Only Macrobond-based figures surfaced. |
| Kırklareli 2025 population | **Query** | TurkStat's 2025 provincial data exists; 3 searches did not surface it. |
| PIP welfare types for 43 countries in one call | **Query (my request)** | `year=MRV` call returned 404; solved by the WB API `footnote=y` route instead. |
| North Korea Gini | **Source** | Does not exist. |
| New Zealand WB Gini | **Source** | The World Bank has none. |

---

## 6. STOP notes (refusals and certificate failures; none worked around)

- **STOP 1:** `https://www.legco.gov.hk/yr2025/english/panels/ws/papers/ws20250414cb1-810-1-e.pdf`: *"unable to verify the first certificate."* Not retried and no alternative route to that document was tried. The 0.397 figure it carries had already appeared in a search snippet, and HK01 confirms it independently.
- **STOP 2:** `https://www.1212.mn/uploads/1773909111705-Bulletin%202026%20I%20en.pdf` (Mongolia NSO): *"unable to verify the first certificate."* Not retried. Mongolia's official NSO figures were left unretrieved; World Bank values were used and labeled.
- **Refusal (HTTP 403):** `https://agn.gt/segeplan-presenta-los-mapas-de-pobreza-2023/`. Not retried.
- No WebSearch call was refused.

---

## 7. Snags and self-corrections

- **A recalled number entered a query (search 42).** I typed "1,586,659" into the Kosovo query from memory. It was never used as a value. The next search showed it conflicts with the final official count (1,602,515), and that conflict was resolved from the PM's page itself (§4.1). Recorded because a recalled figure in a query can steer results toward confirming itself.
- **Fetch count miscounted mid-run.** At one point I believed I had used about 48 fetches; a recount gave 44 at that moment, and 46 at the end. No call was skipped or duplicated because of it.
- **PDFs saved by the fetch tool were not opened.** Three unreadable PDFs (DGBAS, C&SD, Banguat) were saved by WebFetch as binaries in the session's tool-results folder. Extracting them with a shell tool would have recovered the Taiwan August revision, the HK 2021 tables and the Petén figure. **I did not**, because the brief forbids reading any file other than the three outputs and forbids shell downloads. That trade cost three figures and is the single largest source of blanks in this run.
- **One search summary gave Taiwan a "per-person Gini 0.277"**, but the quote it showed contained only quintile ratios. Not used; marked UNVERIFIED.
- **One search summary placed Petén "among departments above 60%" multidimensional poverty**, and another did not. Not used; marked UNVERIFIED.
- **The order of research put the WB calibration pulls first** (15 fetches) and then spent 9 fetches on the DGBAS site, which renders client-side. In hindsight, about 6 of those were avoidable: the first two DGBAS pages already showed that the site yields no values without JavaScript.

---

## 8. Open threads

1. **Taiwan:** DGBAS's revised 2025 per capita GDP from the 2026-08-14 release (PDF `enewstotal11508.pdf`), and the 2025 FIES Gini (released Aug 2026; quintile ratio 6.2).
2. **Hong Kong:** the 2026 Population Census (enumeration from January 2026, per C&SD) will produce a new household-income report, probably in 2028.
3. **Mongolia:** NSO end-2025 population and 2025 US$ GDP per person (blocked by the certificate failure); the HSES 2024 Gini.
4. **Guatemala:** confirm the INE projection at ine.gob.gt; Banguat's 2025 per capita GDP in US$.
5. **Petén:** read the Petén row of Banguat's departmental GDP-per-person table (2024, nominal quetzales; convert with Banguat's 2024 average exchange rate, which also still needs sourcing) and INE's ENCOVI 2023 departmental poverty table. Both exist; both need a tool that can read PDF or Excel.
6. **Kosovo:** KAS 2025 population estimate and GDP per person in euros; whether the 2024 census total includes diaspora.
7. **Kırklareli:** TurkStat ADNKS value for 31 Dec 2025.
8. **Calibration:** New Zealand has no WB Gini (an alternative such as Stats NZ or the OECD income-distribution database would be a different basis). Hungary's WB Gini is from 2017. Romania's welfare type is unconfirmed.
9. **Transcription:** WB population and GDP values were read once through the fetch summarizer. If exact digits matter, re-pull them raw.

---

## 9. Counts

- **WebSearch:** 51 of 60.
- **WebFetch:** 46 of about 50. Of those, 19 went to the World Bank data API, 2 to the World Bank PIP API and 2 to the Eurostat API. The other 23 were page and PDF fetches, of which 5 were readable and useful (HK01, gov.mo, PM's office Kosovo, TaiwanPlus, eng.stat.gov.tw release list).

---

## FINAL summary

**Found and filled:** population, GDP per person and Gini for Taiwan, Hong Kong, Macau, Mongolia, Austria, Guatemala, Luxembourg and Kosovo. Population and income for North Korea. Population for Kırklareli. All 43 calibration countries have population and GDP per person for 2025, and 42 of 43 have a WB Gini with its year and its income-or-consumption basis.

**Left BLANK (not estimated):**
- **North Korea Gini:** none exists.
- **New Zealand Gini** (calibration): the World Bank has none.
- **Petén GDP per person:** an official Banguat series exists but could not be read.
- **Petén poverty rate:** INE's departmental figure exists but was not found.
- **Petén population:** not looked up.
- **Kırklareli GDP and Gini:** not requested.

**UNVERIFIED (recorded in notes, not used as the main value unless stated):**
- **Kırklareli 379,031** (31 Dec 2024). **This one IS the main value**, from a single secondary source; the 2025 figure was not found.
- Guatemala INE projections 18,079,810 (2025) and 18,312,373 (2026).
- Mongolia NSO homepage figure 3,660,609 (undated).
- Kosovo GDP EUR 6,956 (Macrobond).
- Macau household-basis Ginis 0.35 / 0.36.
- Taiwan per-person Gini 0.277.
- Petén multidimensional poverty above 60%, and ENCOVI 2011 Petén 65.67%.

**Flagged but used:**
- Taiwan GDP is the February 2026 preliminary; the August revision was not found.
- Hong Kong has no 2021 original-income Gini (not published).
- North Korea's US$ figure is my conversion of the BOK's won figure, and it is GNI, not GDP.
- Kosovo's Gini series is unstable.
- Argentina's WB Gini is urban only.
- Hungary's WB Gini is from 2017.
- Romania's Gini basis is unconfirmed.
- 7 calibration Ginis plus Mongolia's are consumption-based.
