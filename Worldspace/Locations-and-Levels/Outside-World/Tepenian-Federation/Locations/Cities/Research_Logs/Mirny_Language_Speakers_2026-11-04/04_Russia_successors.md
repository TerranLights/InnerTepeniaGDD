# G4 — Russia's successor regions: language-speaker shares

Assignment G4, research run 2026-11-04. Search budget 60 (WebSearch = 1, WebFetch = 0.5). **Used: 39 searches + 27 fetches = 52.5.**

**Read this first: what "census" means in every cell below.** The Russian censuses of 2010 and 2021 ask every resident whether they speak Russian, and then which other languages they speak (Russian: *владение языками*). In 2021, up to three other languages could be listed. The answer is self-reported, and one household member often answers for the others. It is the closest census measure to the developer's "can function" definition, but it is not a test. Two caveats apply throughout:
1. **2021 under-reports, so 2010 is the better baseline for English.** In 2021 about 16.5 M of 147.2 M residents had no nationality or language recorded (Kommersant 2023). In Moscow, 23.8 % stated no native language (ru.wikipedia, *Население Москвы*, citing the 2021 census). Even among those who did answer, the English share fell from 5.48 % (2010) to about 3.75 % (2021). Surveys show English *rising* over the same years (Levada: 11 % in 2014, 15 % in 2023), so the 2021 drop is mostly a data-quality artifact.
2. **Regional English tables could not be opened.** rosstat.gov.ru and its regional subdomains failed on every fetch (SSL errors), and web.archive.org is blocked. Regional English figures were therefore taken from published data points where they exist, and the rest are **modeled** (method in the note to Table B). Every modeled cell is marked as such.

### National reference points (Russia as a whole; used to anchor the rows)

| Measure | Value | What was measured | Source |
|---|---|---|---|
| Russian, 2010 | 137,494,893 = **99.41 %** of the 138,312,535 who answered (total population 142,856,536) | Census: speaks Russian | Rosstat 2010 census, *Распространение языков*, via ru.wikipedia *Языки России в порядке численности владеющих* |
| Russian, 2021 | 134.3 M of 135.1 M who answered ≈ **99.4 %** | Census: speaks Russian | Ma Lin, MSU *Lomonosov-2025* paper citing Rosstat 2021 Vol. 5 (weak secondary source) |
| English, 2010 | 7,574,303 = **5.48 %** of those answering / **5.30 %** of total population. Urban **7.1 %**, rural **1.0 %** | Census: speaks the language | Rosstat, *Об итогах ВПН-2010 по РФ* (read via search summary, 02.rosstat.gov.ru); ru.wikipedia list above |
| English, 2021 | 5,066,515 ≈ **3.75 %** of those answering / **3.44 %** of total population | Census: speaks the language | ru.wikipedia *Языки России*; Kommersant 2023 (5.07 M); T-Zh (≈5.1 M, citing Rosstat Tom5_tab4_VPN-2020) |
| English, Levada 2014 | **11 %** of adults speak it "more or less freely". By settlement: Moscow 20, cities 500k+ 13, 100–500k 12, under 100k 9, villages 8. Another 13 % speak *some* foreign language "with difficulty" (excluded here) | Self-assessment survey, 1,602 adults, April 25–28, 2014 | Levada Center, *Владение иностранными языками*, 2014 |
| English, Levada 2023 | **15 %** of adults "more or less freely". Any foreign language: 20 % overall; Moscow 32 %, Northwestern district 38 %, Urals district 10 % | Self-assessment survey, 1,606 adults, August 24–30, 2023 | Levada Center, *Иностранные языки: август 2023 года* |
| English, VTsIOM 2019 | **5 %** speak it fluently | Self-assessment survey (sample not stated in the report I read) | mel.fm, Sept 30, 2019, reporting VTsIOM |
| Any foreign language, FOM | **3 %** speak at least one foreign language freely | Self-assessment survey (year not given in the report I read) | T-Zh, *Какие иностранные языки изучают в России*, citing FOM |
| Chinese / Korean / Japanese, 2010 | 70,722 (0.051 %) / 42,384 (0.031 %) / 33,855 (0.024 %) of those answering | Census: speaks the language | Rosstat 2010 via ru.wikipedia list |
| Chinese, 2021 | ≈ 59,000 | Census: speaks the language | T-Zh citing Rosstat Tom5_tab4_VPN-2020 |
| Chinese, Otkritie 2023 | 1 % of respondents know Chinese. 16 % name it the "most necessary" language (Siberia 23 %, Far East 20 %), which measures interest, not ability | Survey, 1,015 people aged 18–65, cities over 100k | The Moscow Times (Russian service), April 20, 2023, reporting the Otkritie bank survey |

## Table

All shares are % of the row's whole population unless the note says otherwise. A "modeled" cell is an estimate built from national census rates, as explained in the method note under the table. Korean, Indonesian and Japanese are negligible in every row (see the last block of the table).

| Nation (real-world region used) | Language | LOW % | BEST % | HIGH % | What the source measured | Source | Confidence | Note |
|---|---|---|---|---|---|---|---|---|
| **Idelsk-Uralia** (Republic of Tatarstan + Republic of Bashkortostan only; 2021 population 4,004,000 + 4,091,423 = 8,095,423. No neighbors added, see note) | Russian | 98.0 | 98.4 | 99.4 | Census 2021: speaks Russian. Tatarstan 98.2 % of those who stated language knowledge (3,923,329 of 4.004 M); Bashkortostan 98.5 % | Idel.Realii (RFE/RL), *Куда пропали татары?*, Mar 9, 2023, https://www.svoboda.org/a/32297639.html ; Ishmukhametova, *The Functioning of Bilingualism in the Republic of Bashkortostan*, Tomsk J. Linguistics & Anthropology 2024 no. 4, https://journals.rcsi.science/2307-6119/article/view/272837 | high | HIGH = national 2010 rate (99.41 %). 2021 non-response in Tatarstan was only about 2 %, so 98.2 % is a fair reading. |
| Idelsk-Uralia | Tatar | 29 | 30 | 38.5 | Census, speaks Tatar. 2021: Tatarstan 1,547 K (39.4 % of those stating language) + Bashkortostan 822.9 K (20.1 %) = 2,369.9 K, which is **29.3 %** of 8.095 M. 2010: 1,965 K + 1,063 K = 3,028 K, which is **38.5 %** of about 7.86 M | Idel.Realii 2023 (above); Ishmukhametova 2024 (20.1 %) | high (2021) / medium (2010 share) | BEST leans to 2021 because Tatarstan's 2021 non-response was low, so the 21 % fall in Tatarstan is mostly real. The 2010 denominator uses Tatarstan's 3.786 M (from Kommersant's 2021 figure minus its stated growth) and Bashkortostan's ≈4.07 M (2010 census, not re-checked this run). |
| Idelsk-Uralia | Bashkir | 11.5 | 11.7 | 14.5 | Census 2021: speaks Bashkir. About 940 K in Bashkortostan (23 % of 4,091,423), plus Bashkir speakers in Tatarstan (not found; ethnic Bashkirs there number 11.0 K in 2021) | Idel.Realii 2023; Ishmukhametova 2024; Kommersant, *Татарское отшествие*, 2023, https://www.kommersant.ru/doc/5759479 | high | HIGH = all 1,152,404 Bashkir speakers in Russia in 2010 placed inside these two republics (14.7 %), a ceiling, not an estimate. |
| Idelsk-Uralia | English | 3.0 | 4.0 | 12 | Census 2021, Bashkortostan: **3.2 %** speak English (measured). Tatarstan: no regional figure found; modeled at about 4.5 % (2010 basis), 3.0–3.8 % (2021 basis). Combined 2010-basis model about 4.1 % | Ishmukhametova 2024 (Bashkortostan 3.2 %); model (method note); HIGH from Levada 2014/2023 structure | medium (Bashkortostan) / low (Tatarstan, modeled) | HIGH = Levada-type self-assessment ("more or less freely"), with the national 15 % scaled for a region with no Moscow. Kireev: Bashkortostan's rural districts are "relatively decent" among the republics. |
| Idelsk-Uralia | Mandarin / Korean / Indonesian / Japanese | — | negligible | — | National census 2010: Chinese 0.05 %, Korean 0.03 %, Japanese 0.02 % of all Russia | Rosstat 2010 via ru.wikipedia | high | No regional concentration expected. |
| **Russia (core state)** (Central Federal District: Moscow city + Moscow oblast + 16 oblasts; ≈38–40 M) | Russian | 99.4 | 99.8 | 99.9 | Census 2010: speaks Russian. No district figure retrieved; national rate 99.41 % | Rosstat 2010 via ru.wikipedia | medium | Russia's non-speakers of Russian are concentrated in the North Caucasus republics and Tuva, outside this district. The national rate is used as the floor. |
| Russia (core state) | English | 5 | 8 | 18 | Census 2010: Moscow city **15.15 %** (measured, % of total population). Moscow oblast and the 16 other oblasts: modeled (about 5.6 % and 4.2 %). District total modeled at **≈7.7 %** (range 7.3–9.1). 2021 measured points: Bryansk oblast 25,111 (≈2.1 %), Voronezh oblast 77.6 K (≈3.4 %) | Kireev (LiveJournal), *Процент людей, владеющих английским языком*, https://kireev.livejournal.com/1046255.html (2010 census map); Bryansk/Voronezh 2021 Rosstat regional tables read via search summaries; Levada 2014/2023 | medium-low (modeled) | LOW = 2010 model × 0.67 (the national 2021/2010 ratio). HIGH = Levada-type: Moscow 20 % in 2014, rising since (Moscow any foreign language 32 % in 2023), rest ≈13 %, with Moscow ≈30 % of the district. Kireev's 2010 city figures: Voronezh 6.51, Smolensk 6.46, Kursk 5.39 % (cities, not oblasts). The Bryansk and Voronezh percentages use approximate 2021 populations (≈1.17 M, ≈2.31 M). |
| Russia (core state) | Mandarin / Korean / Indonesian / Japanese | — | negligible | — | Census 2010 national; Levada 2014: Chinese under 1 % in Moscow and every settlement type | Rosstat 2010; Levada 2014 | high | — |
| **Siberia** (Siberian Federal District in its current 10-subject form: Altai Rep., Altai krai, Irkutsk, Kemerovo, Krasnoyarsk, Novosibirsk, Omsk, Tomsk, Tuva, Khakassia; ≈17 M. Buryatia and Zabaykalsky are in the Far East row; the Ural district's Tyumen, Khanty-Mansi and Yamal are not included) | Russian | 99.0 | 99.5 | 99.8 | Census: speaks Russian. No district figure retrieved | Rosstat 2010 national rate; reasoning | medium-low | The main pocket of non-speakers is Tuva (Tuvans are 88.7 % of Tuva's ≈0.32 M people, and about 85 % of respondents there speak Tuvan). The rest of the district is overwhelmingly Russian-speaking. |
| Siberia | English | 3 | 4.5 | 13 | Census 2010: no subject figure retrieved; modeled at **≈4.4 %** | Model; Kireev 2010 qualitative: Novosibirsk and Tomsk oblasts above average (urban); Tuva and Altai near zero | low (modeled) | LOW = model × 0.67 (2021 basis). HIGH = Levada-type. |
| Siberia | Indigenous languages | — | below 10 % | — | Census 2010: Tuvan 253,673 speakers in all Russia, ≈1.5 % of the district | Rosstat 2010 via ru.wikipedia | high | Altai and Khakas are smaller. Nothing reaches 10 %. |
| Siberia | Mandarin | — | negligible (< 0.5) | — | Census 2010: 70,722 Chinese speakers in all Russia (≤0.4 % of the district even if all lived there). Levada 2014: Chinese under 1 % everywhere. Otkritie 2023: 1 % know Chinese nationally (cities over 100k) | Rosstat 2010; Levada 2014; Moscow Times / Otkritie 2023 | high | Interest is rising (23 % of Siberians call Chinese the most necessary language), but ability is not. |
| Siberia | Korean / Indonesian / Japanese | — | negligible | — | Census 2010 national | Rosstat 2010 | high | — |
| **Donska-Kubania** (Rostov oblast + Krasnodar krai + Republic of Adygea, which lies inside Krasnodar krai; ≈10 M. **Stavropol not added**) | Russian | 99.4 | 99.8 | 99.9 | Census: speaks Russian. No regional figure retrieved | Rosstat 2010 national rate | medium | — |
| Donska-Kubania | English | 2.5 | 4 | 12 | Census 2010: no subject figure retrieved; modeled at **≈3.7–4.6 %** (less urban than the other rows) | Model; Kireev 2010 qualitative: Krasnodar city much above Sochi; large rural settlements in Krasnodar and Stavropol krais (less so Rostov) approach small-town levels | low (modeled) | LOW = 2021 basis; HIGH = Levada-type. Adding Stavropol would change little (Kireev groups it with Krasnodar). |
| Donska-Kubania | Other languages over 10 % | — | none shown | — | Census 2010: Armenian speakers in all Russia 660,935, ≤6.6 % of the region even if all lived here | Rosstat 2010 via ru.wikipedia | medium | Ukrainian (1,129,838 in all Russia in 2010) cannot be ruled out by that bound alone. Its regional share was not checked; it is probably a few percent. |
| Donska-Kubania | Mandarin / Korean / Indonesian / Japanese | — | negligible | — | Census 2010 national | Rosstat 2010 | high | — |
| **Künnarantaiga** (Russian Far East: Far Eastern Federal District in its current 11-subject form, including Buryatia and Zabaykalsky since 2018; ≈8 M) | Russian | 99.0 | 99.5 | 99.8 | Census 2010: Buryatia **98.2 %** speak Russian (measured). Sakha and the others not retrieved | Buryatstat 2010 release, read via search summary (03.rosstat.gov.ru) | medium-low | Sakha (Yakuts ≈50 % of ≈0.96 M) is the other non-Russian-majority subject. Russian there is near-universal per Ivanova 2014, but no census share was retrieved. |
| Künnarantaiga | English | 3.5 | 5.5 | 13 | Census 2010: Primorsky krai **125,741 = 6.43 %** of total population (1,956,497), or 6.86 % of the 1,833,419 who stated language knowledge (measured). Buryatia **32.9 K ≈ 3.4 %** (measured). District modeled at ≈5–5.5 % | Primorskstat 2010 table *pub-04-05_Терр=05000000.pdf* (25.rosstat.gov.ru, read via search summary); Buryatstat 2010 release; Kireev 2010: Far East "relatively high" | medium (Primorsky, Buryatia) / low (rest) | Primorsky is the largest subject (≈1.9 M) and the Vladivostok area. LOW = 2021 basis; HIGH = Levada-type. |
| Künnarantaiga | Mandarin | — | negligible (≈0.4–0.9) | — | Census 2010: Primorsky 8,397 = **0.43 %** (measured). All Russia 70,722, ≤0.9 % of the district even if all lived there. 2021: ≈59 K nationally | Primorskstat 2010; Rosstat 2010; T-Zh 2021 | high | Below the 2 % threshold everywhere checked. Interest (20 % "most necessary", Otkritie 2023) is not ability. |
| Künnarantaiga | Korean | — | negligible (≤0.5) | — | Census 2010: 42,384 Korean speakers in all Russia, ≤0.5 % of the district even if all lived there | Rosstat 2010 | high | Sakhalin's Korean community is local; not checked separately. |
| Künnarantaiga | Japanese / Indonesian | — | negligible | — | Census 2010: Japanese 33,855 in all Russia (≤0.4 %); Indonesian not among the listed languages | Rosstat 2010 | high | — |
| Künnarantaiga | Indigenous languages | — | below 10 % | — | Census 2010: Yakut 450,140 in all Russia (401,240 in Sakha), ≈5 % of the district. Buryat 218,557, ≈2.7 % | Rosstat 2010 via ru.wikipedia; Kuzmina (libryansk.ru) citing 2010 | high | Nothing reaches 10 % district-wide. |
| **Finland** (Republic of Karelia; 2010 population 643.5 K) | Russian | 99.4 | 99.9 | 99.95 | Census: speaks Russian. Not retrieved | Rosstat 2010 national rate | medium | — |
| Finland (Karelia) | Karelian | 2.0 | 2.5 | 2.7 | Census 2010: **16,876** in Karelia speak Karelian = 2.6 %. Census 2021: 13,800 speakers (scope unclear, possibly all Russia), down 73.7 % since 2002; median speaker age 64 | Udmurt Univ. *Finno-Ugric* journal article (journals.udsu.ru/finno-ugric/article/download/2531/2507) citing 2010; The Barents Observer citing 2021 | medium | Ethnic Karelians were 45,570 (7.4 %) in 2010. Not all speak the language. |
| Finland (Karelia) | Finnish | 0.5 | 1.5 | 3 | **Not found.** Ethnic Finns were 1.4 % of Karelia in 2010. All 38,873 Finnish speakers in Russia (2010) placed in Karelia would be 6.0 %, a hard ceiling | Karelia 2010 booklet via search summary; Rosstat 2010 via ru.wikipedia | low | Estimate only. Many of Russia's Finnish speakers live in St Petersburg and Leningrad oblast. |
| Finland (Karelia) | English | 3 | 5 | 13 | Census 2010: no figure retrieved; modeled at ≈4.6 % (highly urban) | Model; Kireev 2010: Karelia's English "higher than its urbanization would predict" | low (modeled) | — |
| Finland (Karelia) | Mandarin / Korean / Indonesian / Japanese | — | negligible | — | Census 2010 national | Rosstat 2010 | high | — |

**Method note for the modeled English cells.** The 2010 census gives English at 7.1 % of urban and 1.0 % of rural respondents. Taking Moscow (15.15 % of 11.5 M) and St Petersburg (13.83 % of 4.9 M) out of the urban figure leaves about 5.6 % for other cities. The model is region English ≈ urban share × 5.6 % + rural share × 1.0 %. The urban shares are approximate 2010 values, **recalled and not verified in this run**: Tatarstan ≈75 %, Bashkortostan ≈60 %, Rostov + Krasnodar + Adygea ≈59 %, Siberian district ≈73 %, Far Eastern district ≈72 %, Karelia ≈78 %, Moscow oblast ≈81 %, the other Central oblasts ≈70 %. Checks against measured points:
- Primorsky: 6.43 % measured against 4.5 % modeled. The Far East runs above the model, as Kireev says.
- Buryatia: 3.4 % measured against 3.7 % modeled.
- Bashkortostan 2021: 3.2 % measured against 2.5 % modeled (model × 0.67).

The model is therefore roughly right, with regional quirks of about ±1.5 points. "2021 basis" means 2010-basis × 0.67 (5,066,515 ÷ 7,574,303).

**How BEST was chosen for English.** The developer's bar is "business and social talk", which sits between two kinds of survey. The census self-report and VTsIOM's "fluent" are each about 5 % nationally. FOM's "freely" (3 %) is stricter. Levada's "more or less freely" (11–15 %) is looser and excludes only those who speak "with difficulty". BEST follows the 2010-basis census level, the most complete measured layer, which also matches VTsIOM's 5 % fluent. LOW follows the 2021 census, and HIGH follows the Levada-type self-assessment.

## Source log

**Sources used**
1. Rosstat, 2010 census *Распространение языков* (national counts by language), via ru.wikipedia *Языки России в порядке численности владеющих* — https://ru.wikipedia.org/wiki/Языки_России_в_порядке_численности_владеющих — national 2002/2010 counts and denominators.
2. Rosstat, *Об итогах ВПН-2010 по Российской Федерации* (02.rosstat.gov.ru PDF; read only through a search summary) — English 5.5 % of respondents, urban 7.1 %, rural 1.0 %.
3. Primorskstat, 2010 census table *pub-04-05_Терр=05000000.pdf* — https://25.rosstat.gov.ru/storage/mediabank/pub-04-05_Терр=05000000.pdf (read only through a search summary) — English 125,741; Chinese 8,397; 1,833,419 stated language knowledge; 123,078 did not.
4. Buryatstat 2010 census release (03.rosstat.gov.ru; search summary) — English 32.9 K (3.4 %); Chinese ≈2.7 K; Russian 98.2 %.
5. Bryansk and Voronezh 2021 census tables (32.rosstat.gov.ru *Tom5_tab4_VPN-2020(1).pdf*; 36.rosstat.gov.ru *ВПН-2020_139.pdf*; search summaries) — English 25,111 and 77.6 K.
6. A. Kireev (LiveJournal), *Процент людей, владеющих английским языком* — https://kireev.livejournal.com/1046255.html — 2010 census map: Russia 5.31 %, Moscow 15.15 %, St Petersburg 13.83 %, plus qualitative regional statements.
7. A. Kireev, *Карта владения английским языком по районам России* — https://kireev.livejournal.com/1183614.html — 2010 city figures (Voronezh 6.51, Smolensk 6.46, Kursk 5.39) and qualitative notes on the South, the Far East and Karelia.
8. Idel.Realii (RFE/RL), *Куда пропали татары?*, Mar 9, 2023 — https://www.svoboda.org/a/32297639.html — Tatar and Bashkir counts for Tatarstan and Bashkortostan in 2010 and 2021.
9. A. Sh. Ishmukhametova, *The Functioning of Bilingualism in the Republic of Bashkortostan*, Tomsk Journal of Linguistics and Anthropology 2024 no. 4, DOI 10.23951/2307-6119-2024-4-58-67 — https://journals.rcsi.science/2307-6119/article/view/272837 — Bashkortostan shares: Russian 98.5, Bashkir 23, Tatar 20.1, English 3.2 %. The population base of 4,091,423 is the 2021 census figure. The abstract wrongly says "Republic of Belarus".
10. Kommersant, *Татарское отшествие*, 2023 — https://www.kommersant.ru/doc/5759479 — 2021: Russia 147.2 M, of whom 16.5 M had no nationality recorded; English 5.07 M; Tatar 3.26 M; Tatarstan 4.004 M.
11. T-Zh (Tinkoff Journal), *Какие иностранные языки изучают в России* — https://t-j.ru/foreign-languages-stat/ — 2021 census English ≈5.1 M, Chinese ≈59 K; FOM 3 % freely.
12. Levada Center, *Владение иностранными языками*, May 28, 2014 — https://www.levada.ru/2014/05/28/vladenie-inostrannymi-yazykami/ — full tables by settlement type.
13. Levada Center, *Иностранные языки: август 2023 года* — https://www.levada.ru/2023/09/14/inostrannye-yazyki-avgust-2023-goda/ — English 15 %; regional breakdowns of "any language".
14. mel.fm, *ВЦИОМ: свободным владением английского могут похвастаться только 5% россиян*, Sept 30, 2019 — https://mel.fm/novosti/1847902-vtsiom
15. The Moscow Times (Russian service), Apr 20, 2023 — https://ru.themoscowtimes.com/2023/04/20/zhiteli-sibiri-i-dalnego-vostoka-massovo-zahoteli-uchit-kitaiskii-a40680 — Otkritie survey on Chinese.
16. ru.wikipedia *Население Москвы* — 2021 native-language non-response in Moscow: 3,100,389 (23.83 %).
17. Ma Lin, *Анализ языковой ситуации РФ по данным переписи населения 2020 года*, MSU Lomonosov-2025 (search summary) — 2021: 135.1 M stated language knowledge; Russian 134.3 M. A weak (student) source.
18. Kuzmina (libryansk.ru, 2024, search summary), citing the 2010 census — Yakut 401,240 in Sakha.
19. Udmurt University *Finno-Ugric* journal article (search summary) — Karelian 16,876 in Karelia (2010). The Barents Observer (search summary) — Karelian 13,800 (2021).
20. Karelia 2010 census booklet (10.rosstat.gov.ru; search summary) — population 643.5 K; Karelians 7.4 %; Finns 1.4 %; Veps 0.5 %.
21. en.wikipedia *Yakut language* — about 450,000 native speakers (Britannica). Context only.
22. skyeng.ru magazine and the EF EPI 2024 fact sheet (search summary) — regional EF test scores. Not population shares, so not used in the table.

**Searches run** (Q = died at the query, i.e. no relevant results; S = died at the sources, i.e. results but no usable number; ✓ = usable)
1. `перепись 2010 владение языками населением по субъектам Российской Федерации английский таблица` — S (Rosstat PDFs listed, unreadable)
2. `demoscope.ru перепись 2010 владение языками субъекты английский язык число владеющих` — Q
3. `итоги переписи 2021 владеют английским языком млн человек регионы доля Москва` — ✓ national (T-Zh); S for regions
4. `"владеют английским" перепись 2010 регионы рейтинг доля населения Москва Санкт-Петербург Краснодарский край` — Q
5. `владение иностранными языками перепись 2010 по федеральным округам английский Центральный Сибирский Дальневосточный процент` (extended) — ✓ Kireev; S for districts
6. `перепись английским языком владеют жителей Приморья китайским языком владеют` — ✓ Primorsky 2010
7. `pub-04-05 владение языками английский Центральный федеральный округ Сибирский федеральный округ Дальневосточный федеральный округ Южный` (rosstat domains) — S
8. `Russian census 2010 knowledge of English by federal subject percent Moscow 15% Saint Petersburg map regions English speakers` — S
9. `Республика Татарстан перепись 2010 владение языками татарский русский английский численность лиц владеющих` — ✓ Tatar/Russian; S for English
10. `Башкортостан итоги переписи 2021 владеют башкирским языком татарским языком русским английским процент жителей республики` — ✓ Ishmukhametova
11. `Татарстан перепись 2020 английским языком владеют тысяч человек жителей республики иностранные языки` — S (3,923,329 stated languages; English not found)
12. `"pub-04-05" Терр=92000000 OR Терр=80000000 владение языками английский татарский башкирский` — Q
13. `Краснодарский край перепись владение языками английский армянский адыгейский численность лиц владеющих языком` — S for Krasnodar; ✓ Bryansk 2021
14. `demoscope weekly ssp владение языками 2010 субъекты федеральные округа английский немецкий французский китайский таблица` (demoscope.ru) — S
15. `ВЦИОМ опрос знание иностранных языков английский свободно владеют федеральный округ Москва Санкт-Петербург доля россиян` — ✓ VTsIOM 5 %
16. `Левада-центр владение иностранными языками опрос английский "свободно" "со словарем" Москва большие города доля` — ✓ partial (Levada 2015: 14 %)
17. `levada.ru знание иностранных языков английский владею свободно опрос 2014 OR 2015 OR 2019` (levada.ru) — ✓
18. `география владения иностранными языками регионы России перепись английский доля населения статья Приморский край Новосибирская область Краснодарский край` (extended) — S
19. `перепись английским языком владеют жителей Хабаровского края китайским языком владеют указавших владение языками` — S for Khabarovsk; ✓ Buryatia
20. `Английский язык в России Википедия владение по субъектам перепись 2021 таблица` (wikipedia) — ✓ 2021 English 5,066,515
21. `Мосстат итоги переписи 2021 москвичи владеют английским языком тысяч человек владение иностранными языками Москва Московская область` — S (Buryatia 3.4 % confirmed)
22. `"переписи" москвичей владеют английским языком "млн" Москва английский второй по распространенности язык столица` — S
23. `Ростовская область итоги переписи владение языками английский армянский украинский численность владеющих Ростовстат` — S for Rostov; ✓ Voronezh 2021
24. `Тыва перепись 2010 владеют русским языком процент населения Якутия владение русским языком перепись 2021` — S
25. `владение русским языком по субъектам Российской Федерации перепись 2010 таблица доля владеющих Тыва Якутия Чечня Татарстан Башкортостан 99,4` — ✓ partial (Buryatia 98.2 %)
26. `Новосибирская область перепись владение языками английский численность владеющих английским языком Новосибирскстат итоги` — S
27. `Республика Карелия перепись 2010 2021 владеют карельским языком финским языком человек процент населения` — ✓ partial (Karelian 2021)
28. `Карелия итоги переписи владение языками финским владеют английским владеют карельским Карелиястат` — ✓ partial (Karelian 2010)
29. `Башкортостан перепись 2010 башкирским языком владеют человек татарским языком владеют человек в республике` — S (ethnic shares only)
30. `Московская область перепись владение языками английским языком владеют человек Мособлстат итоги переписи иностранные языки` — S
31. `"Ростовской области" перепись 2010 "английским" владели тысяч жителей донского края языки` — S
32. `итоги ВПН-2020 владение русским языком указали млн человек процент от указавших владение языками английский 5,1 млн` — ✓ partial (Ma Lin)
33. `Якутия перепись 2010 владение языками русским владеют якутским владеют английским владеют численность Саха(Якутия)стат` — ✓ partial (Yakut 401,240)
34. `перепись английским языком владеют жителей Кубани армянским языком владеют указавших владение языками Краснодарстат` — S
35. `EF EPI 2024 Russia regions score Central Volga Southern Siberian Far Eastern Northwestern Ural federal district English proficiency` — S (test scores only)
36. `владение языками английский татарский русский численность лиц владеющих перепись` (regional rosstat domains 16/23/61/54) — S
37. `"английским языком" перепись 2010 "по федеральным округам" владеющих доля ЦФО СЗФО ДФО ЮФО СФО` (extended) — ✓ urban/rural split
38. `pub-04-05_Терр владение языками население указавшие владение языками английский немецкий китайский` — Q
39. `Республика Карелия перепись 2010 финским языком владеют человек карельским 16876 вепсским владение языками` — ✓ partial (ethnic shares; Finnish not found)

**Fetches (27, counted as 13.5)**
- Failed (8):
  - rosstat.gov.ru results2.html and Vol4 pub-04-05.pdf: SSL "self signed certificate in certificate chain".
  - 02.rosstat.gov.ru PDF: SSL "WRONG_VERSION_NUMBER".
  - web.archive.org: blocked for this tool.
  - journals.kantiana.ru (Arefyev) and kasogve.elpub.ru: HTTP 403.
  - demoscope.ru: garbled Cyrillic once, timed out once.
- No usable figures (5):
  - ru.wikipedia *Население Татарстана* (no language section in the part read).
  - business-gazeta.ru/article/524611.
  - journals.rcsi.science 369890 (Fatkhutdinova 2025): the PDF came back as binary and was not opened; the article page has no figures.
  - The bakhtiniada.ru redirect.
- Usable (14):
  - t-j.ru, Kommersant, Ishmukhametova page, Idel.Realii, Kireev ×2, Levada 2014, Levada 2023, mel.fm, skyeng (EF only), Moscow Times, ru.wikipedia language list, ru.wikipedia *Население Москвы*, en.wikipedia *Yakut language*.

## Gaps and conflicts

- **English, census against surveys (the biggest spread).** For Russia as a whole:
  - census 2010: 5.48 % of respondents, 5.30 % of the total population;
  - census 2021: about 3.75 % / 3.44 %;
  - VTsIOM 2019: 5 % "fluent";
  - FOM: 3 % speak a foreign language "freely";
  - Levada: 11 % (2014) and 15 % (2023) "more or less freely".

  The rows carry this spread as LOW/HIGH. BEST follows the 2010 census level.
- **2010 against 2021 census.** English fell from 7,574,303 to 5,066,515, and Tatar from 4,280,718 to about 3.26 M (Kommersant's rounded figure; the exact 2021 count was not retrieved). Much of the drop comes from 2021 non-response, which was 16.5 M nationally and 23.8 % in Moscow for native language. Tatarstan's own non-response was low (about 2 %), so its fall in Tatar speakers (1,965 K to 1,547 K) is largely real.
- **Russian in 2021: two figures.** Kommersant gives 137.5 M Russian speakers for 2021. Ma Lin gives 134.3 M of 135.1 M. Kommersant's figure equals the 2010 count (137,494,893), so it may be misattributed. The share is about 99.4 % either way.
- **Buryatia English.** One search summary said "32.9 K (0.3 %)" and a later one said "32.9 K (3.4 %)". 32.9 K out of Buryatia's ≈0.97 M is 3.4 %, so 3.4 % is used.
- **The national English share has three published forms.** Kireev's 5.31 % is of the total population. Rosstat's 5.5 % is of those answering. The Tyumen statistics press office (tyumedia.ru/82606.html, search summary) gives 4.0 % "of the total population", and I could not tell whether that is national or Tyumen-only.
- **Bashkortostan year.** Ishmukhametova's abstract does not name the census year. Her base of 4,091,423 is the 2021 census population, and her Tatar share (20.1 % of 4,091,423 ≈ 822 K) matches Idel.Realii's 2021 count of 822.9 K, so the figures are treated as 2021.
- **Regional English census figures not obtained** for Tatarstan, Moscow oblast, any Central oblast in 2010, Krasnodar, Rostov, Adygea, every Siberian subject, Khabarovsk, Sakha and Karelia. These cells are modeled.
- **Russian by subject not obtained** except for Tatarstan, Bashkortostan and Buryatia. The other rows use the national rate and reasoning.
- **Finnish in Karelia not found.** It is estimated with a hard ceiling of 6.0 %.

## Not done

- **Rosstat regional tables.** The census tables by subject (2010 Vol. 4 and 2021 Vol. 5) are the proper source for every English and Russian cell, but every rosstat.gov.ru and regional-subdomain fetch failed on SSL, and the web archive is blocked. A later run with working access to those PDFs or XLSX files, or the developer opening them, would replace every modeled cell with a measured one. The key files are `pub-04-05_Терр=<code>.pdf` (2010, per subject) and `Tom5_tab4_VPN-2020` (2021, per subject).
- **Idelsk-Uralia neighbors** (Udmurtia, Chuvashia, Mari El, Orenburg, Samara, Ulyanovsk, Chelyabinsk, Perm) were not added and no searches were spent on them. Adding them would lower the Tatar share (29 %) and the Bashkir share (11.7 %) roughly in proportion to the added population, minus their own Tatar and Bashkir speakers. It would also add Chuvash, Udmurt and Mari, each of which could top 10 % only if Chuvashia were included at large weight.
- **Siberia** excludes the Ural Federal District (Tyumen, Khanty-Mansi, Yamal-Nenets). Including it would not change Russian, and its English level is near the district's.
- **Stavropol** was not added to Donska-Kubania. Kireev puts its English level near Krasnodar's.
- **Not checked:** Sakhalin's Korean speakers, Ukrainian in Donska-Kubania, and Sakha's Russian share.
- **Urban shares in the model** are recalled 2010 values and were not verified in this run.
