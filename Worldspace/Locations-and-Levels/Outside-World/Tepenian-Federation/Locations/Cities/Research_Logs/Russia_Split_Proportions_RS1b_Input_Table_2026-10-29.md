# Russia-split proportions · Unit RS1b · The shared input table (2026-10-29)

**⚠ The First Interwar record does not exist.** The developer's Russia folders for it (`03 official timeline years`, `04 timeline staging`) are empty (RS1 section 2). **Every figure in this file is a present-day real-world regional figure standing in for that unwritten record**, aggregated to the successors' territories, and is therefore DERIVED as a Tepenian input even where the real-world number itself is SOURCED.

**Brief:** `Research_Logs/Russia_Split_Proportions_Research_BRIEF_2026-10-29.md`, section "Added 2026-10-29 (coordinator, after RS1)". **Method and successor table:** `Research_Logs/Russia_Split_Proportions_RS1_Inventory_and_Method_2026-10-29.md`. **Machine-readable companion:** `Research_Logs/Russia_Split_Inputs_2026-10-29.csv` (91 rows, one per source unit, with full source strings). Draft research only: nothing here is a ruling, a design or a recommendation; no other file is edited.

**Labels:** SOURCED (URL or file and line; "secondary" = a transcription of the official statistic, not the statistics office itself) · UNVERIFIED · DERIVED · NOT FOUND.

## PROGRESS
- [x] 1 Population (one year for all units)
- [x] 2 GRP per head (one year for all units)
- [x] 3 Gini
- [x] 4 Solar zone per subject (S7 rule)
- [x] 5 Recipient mapping (`09 follow-up/subdivisions.csv`)
- [x] 6 Per-successor pools and zone profiles
- [x] 7 Split (a) variants
- [x] FINAL

---

## 0 · The defaults applied, and the years that follow from them

Coordinator defaults, applied exactly (NOT rulings): **S1 = V1** (83 pre-war federal subjects; Crimea, Sevastopol and the six eastern-Ukraine units out), with V1c and V2 reported · **S2 = K-out**, K-in reported · **S3 = INIT**, C-15 reported · **S4: θ = 10%**, with 5% and 25% shown as the meaningful-zone sets in section 6 · **S5 = solar zones**, official zones reported · **S6 = no wraparound** · **S7 = the solar zone of each subject's largest city**, territory centroid reported · **E = P × y × (1 − G)**, falling back to **E = P × y for all units** wherever any unit lacks a Gini.

**The years, and why (DERIVED from source coverage; each choice follows the brief's wording "one year for all, the latest year common to all"):**

| Input | Year used | Coverage | Why this year |
|---|---|---|---|
| Population, 85 Russian units | **2021 census** (15 Oct to 14 Nov 2021) | all 85 | The brief asks for the 2021 census where possible |
| Population, 6 Ukrainian units (V2 only) | **1 January 2022** Ukrstat estimate | all 6 | Ukraine held no 2021 census; 1 Jan 2022 is the estimate closest to the Russian census dates |
| GRP per head, 85 Russian units (V1, V1c) | **2024** | all 85 | The latest year present for every Russian unit (statbase.ru's Rosstat series ends in 2024 with all 85) |
| Gini, 85 Russian units (V1, V1c) | **2022** | all 85 | The latest year present for every unit in the secondary table found: 81 units have 2023, but Stavropol', Astrakhan', Rostov and Volgograd end at 2022 |
| GRP per head, V2 (all 91 units) | **2021** | 85 + 4 of 6 Ukrainian units | Ukrstat's regional accounts stop at 2021, so 2021 is the latest year any V2 table can share. Donetsk and Luhansk have no per-head figure after 2013 (section 2.3) |
| Gini, V2 | **none** | Ukrainian units NOT FOUND | So V2 uses **E = P × y2021 for all units**, as the default requires |

⚠ GRP (2024) and Gini (2022) are different years in the primary form. That follows from each series' own latest common year; the sensitivity table in section 7.2 gives the same-year form (P × y2022 × (1 − G2022)) beside it.

---

## 1 · Population

**85 Russian units (83 pre-war subjects plus Crimea and Sevastopol).**
- **The 83 pre-war subjects: SOURCED secondary.** Tim Bespyatov, *Ethnic composition of Russia 2021*, column "Всего" (https://pop-stat.mashke.org/russia-census-2021-ethnic/total.htm), a full transcription of the 2021 census table by subject. It is the same table EO3 used (`Relung_Panen_Ethnic_Origin_EO3_Oceania_and_Siberia_2026-10-29.md` L338); it was re-downloaded this session and is byte-identical to EO3's copy. Sum of the 83: **144,699,673** (DERIVED; equals EO3 L346).
- **Arkhangel'sk and Tyumen' are the "without autonomous okrug" figures** (978,873 and 1,601,940), because the package carries Nenets, Khanty-Mansiy and Yamal-Nenets as their own units (`R09/sub` L43, L48, L60).
- **Cross-check (second source): SOURCED secondary**, en.wikipedia *2021 Russian census*, provisional table "Provisional population results on 1 October 2021 (thousands)" (revision 1376053421). Spot checks match to the thousand: Moscow 13,010 vs 13,010,112 · Nenets 41 vs 41,434 · Yamal-Nenets 510 vs 510,490 · Kaliningrad 1,030 vs 1,029,966 · Arkhangelsk incl. Nenets 1,020 vs 978,873 + 41,434 = 1,020,307 · Tyumen incl. both okrugs 3,824 vs 1,601,940 + 1,711,480 + 510,490 = 3,823,910. Moscow Oblast differs slightly (8,532 provisional vs 8,524,665 final); the final count is used.
- **Crimea 1,934,630 and Sevastopol 547,820: SOURCED secondary**, en.wikipedia *Demographics of Crimea* (revision 1375592310): *"According to the 2021 Russian census, the total population of the Republic of Crimea and Sevastopol was at 2,482,450 (Crimea: 1,934,630, Sevastopol: 547,820)."* They agree with the provisional 1,935 and 548 thousand in the census page above. Rosstat's own Crimea census page (rosstat.gov.ru/free_doc/new_site/population/demo/perepis_krim/) was found in search but not opened (TLS-blocked host; not bypassed).
- **Sum check (DERIVED):** 144,699,673 + 1,934,630 + 547,820 = **147,182,123**, consistent with the provisional national 147,190 thousand.

**6 Ukrainian units (V2 only).** **SOURCED:** Main Department of Statistics in Lviv Oblast (a regional office of Ukrstat), *Кількість наявного населення на 1 січня*, column 2022, thousand persons (https://lv.ukrstat.gov.ua/ukr/help/pb_fig2021/chapter_1_3.html): Dnipropetrovs'k 3,096.5 · Donets'k 4,059.4 · Zaporizhzhya 1,638.5 · Luhans'k 2,102.9 · Kharkiv 2,599.0 · Kherson 1,001.6 (whole oblast). The federal ukrstat.gov.ua host failed its certificate check here (*"certificate has expired"*); it was not bypassed. ⚠ Whether Ukrstat's Donetsk and Luhansk estimates include the parts occupied since 2014 is **UNVERIFIED** (the GRP table's note, section 2.3, says GRP excludes them; the population table carries no such note).

**Kherson, left bank only: DERIVED, and resting on a guess.** The package takes only the left bank (`R09/sub` L91). No source gives a left-bank population. The developer's own working note gives *"roughly 0.4 M (⚠️ an area-weighted guess)"* at the 2001 baseline (`EUB` L110). The 2001 census total for the oblast is 1,175,122 (**SOURCED secondary**, en.wikipedia *Kherson Oblast*, revision 1374090773, "Historical population"). Left-bank share = 0.4M ÷ 1,175,122 = **34.04%**; applied to 1 Jan 2022: 1,001,598 × 0.3404 = **340,935**. Both the share and the result inherit the developer's flag.

---

## 2 · GRP per head

### 2.1 Russian units, primary year 2024
**SOURCED secondary:** statbase.ru, *Валовой региональный продукт России на душу населения. Регионы — статистика с 1998 по 2024 годы* (https://statbase.ru/data/rus-gross-domestic-product-by-region-per-capita-national-stat/, read 2026-10-29), the 2024 regional table, in rubles, 85 rows. Its own notes: the series *"содержат изменения, связанные с учетом итогов ВПН-2020"*; *"С 2022 года без учета статистической информации по Донецкой Народной Республике (ДНР), Луганской Народной Республике (ЛНР), Запорожской и Херсонской областям"*; and the Rosstat methodological caveat that head-office regions are overstated and branch regions understated. Its page text gives the national 2024 average as 1,276,523 rubles. Arkhangel'sk and Tyumen' appear without their okrugs (the table has exactly 85 rows with the three okrugs separate, and their 2024/2022 ratios, 1.21 and 1.26, sit beside the ru.wikipedia "без округов" 2022 figures; **DERIVED** reading).

### 2.2 Russian units, 2021 and 2022 (sensitivities; and 2021 is the V2 year)
**SOURCED secondary:** ru.wikipedia, *Список субъектов Российской Федерации по валовому продукту на душу населения*, revision `oldid=152668547` (the current revision when read; the page says it is unreviewed since a checked version of 16 June 2025), columns "2021" and "2022", thousand rubles; page text: *"Материал взят с сайта Федеральной государственной службы статистики"*; *"Данные по Архангельской и Тюменской областям представлены без округов."*

**⚠ An error found in that source.** The ru.wikipedia **2022** value for **Ingushetia is 275.4**, identical to Kabardino-Balkaria's 275.4 in the same column, and nearly double its 2021 value (142.9). statbase.ru's Ingushetia page says, verbatim, that the region's maximum per-head GRP was reached *"в 2024 году, когда он составил 204 566 рублей"* and that 2023 was 181,994 (https://statbase.ru/data/ru6-gross-domestic-product-by-region-per-capita-national-stat/). **A 2022 value of 275.4 is therefore impossible; it is very probably a copy of the Kabardino-Balkaria cell.** The correct 2022 value was NOT FOUND (statbase's per-year series loads by script and was not extracted). It is left as published in the 2022 sensitivity rows, flagged in the CSV, and **is not used in the primary form.** Its effect: Ingushetia's split (a) share is 0.11% under the 2022 form against 0.06% under 2021 and 2024.

**Other large 2022 → 2024 moves, checked and left as published** (ratio 2024/2022; the median over the 85 units is 1.33; DERIVED): Kemerovo 0.84 and Murmansk 0.98 (both fall), Chechnya 1.66, Magadan 1.68, Amur 1.69, Kalmykia 1.79 (all rise). None shows the duplicated-cell pattern; whether each is a real economic movement is **UNVERIFIED**.

### 2.3 The six Ukrainian units (V2 only), 2021
**SOURCED:** Main Department of Statistics in Lviv Oblast, *Валовий регіональний продукт у розрахунку на одну особу*, grn, 2010 to 2021 (https://lv.ukrstat.gov.ua/ukr/help/pb_fig2021/chapter_3_1.html). 2021: Dnipropetrovs'k **186,697** · Zaporizhzhya **138,521** · Kharkiv **122,227** · Kherson **87,378** (whole oblast, applied to the left bank: DERIVED assumption) · Ukraine **131,734**. ⚠ en.wikipedia's *List of regions of Ukraine by GDP* (revision 1374263879) gives slightly different per-head values for 2021 (e.g., Dnipropetrovsk 188,072), computed from its own population column; the Ukrstat figures are used.

**Donetsk and Luhansk: NOT FOUND after 2013.** The table shows "х" for both from 2014 to 2021, with the note, verbatim: *"Здійснення розрахунків показників на одну особу щодо Донецької та Луганської областей є некоректним у зв'язку з відсутністю інформації у частині тимчасово окупованих територій цих областей."* en.wikipedia's list also gives "N/A". **DERIVED stand-in, used only in V2:** each oblast's 2013 ratio to Ukraine, applied to Ukraine's 2021 figure. Donetsk 37,830 ÷ 33,473 × 131,734 = **148,881** grn; Luhansk 24,514 ÷ 33,473 × 131,734 = **96,476** grn. This freezes their 2013 relative position; section 7.2 shows the alternative (both at the Ukraine average), which moves no successor by more than 0.01 point.

**Currency: DERIVED** at the World Bank's official exchange rate, period average 2021 (indicator `PA.NUS.FCRF`, API `https://api.worldbank.org/v2/country/UKR;RUS/indicator/PA.NUS.FCRF?date=2013:2022&format=json`, last updated 2026-10-08): RUB 73.65435 and UAH 27.28619 per USD, so **2.6993 RUB per UAH**. PPP sensitivity (`PA.NUS.PPP`, 2021: RUB 23.6851, UAH 7.30216 per international dollar) gives 3.2436 RUB per UAH; section 7.2.

---

## 3 · Gini

**Rosstat's regional table was not reachable** (rosstat.gov.ru and its regional subdomains fail TLS verification here; not bypassed), and no Wikipedia list by subject exists (RS1 G2; re-searched, section 9).

**Used: SOURCED secondary**, CEIC, *Russia Household Income Ratio: Gini Coefficient* (https://www.ceicdata.com/en/russia/household-income-ratio-gini-coefficient), series *"Gini Coefficient: Income Concentration Index"* by region, *"reported by Federal State Statistics Service"*. The free page states, per series, the latest value and the previous one. 87 regional series were extracted (85 subjects plus the two "including okrugs" aggregates, which are not used). **2022 is present for all 85 subjects**: as the "previous" value for 81 series, and as the "latest" value for Stavropol', Astrakhan', Rostov and Volgograd (whose series end in 2022). Arkhangel'sk uses *"Arkhangelsk Region excl Area"* and Tyumen' *"Tumen Region excl Areas"*. Range (DERIVED): 0.310 (Jewish AO) to 0.440 (Yamal-Nenets); Moscow 0.412, St. Petersburg 0.402.

**⚠ A cross-check disagrees slightly.** The Gaidar Institute's monitoring note (https://www.iep.ru/files/RePEc/gai/monreo/monreo-2025-4-1385.pdf, p. 2, *"Источник: Росстат"*) gives 2022 → 2023 for Kalmykia 0.315 → 0.343, Orel 0.366 → 0.388 and Smolensk 0.372 → 0.393; CEIC gives 0.313 → 0.333, 0.357 → 0.402 and 0.365 → 0.397. The 2022 values differ by 0.002 to 0.009. Rosstat publishes more than one Gini measure (RS1 G1: a further measure added from 2021), so the two may be different measures or different vintages; **which one CEIC carries is UNVERIFIED.** At this size the effect on (1 − G) is under 1.5% per unit.

**Kaliningrad (K-in only):** 0.325 (2022), same source.

**The six Ukrainian units: NOT FOUND.** No oblast Gini table was found (search S6, section 9); ukrstat.gov.ua fails its certificate check. Hence V2 uses E = P × y for all units.

---

## 4 · Solar zone per subject (S7)

**Rule (DERIVED):** solar zone = round(longitude ÷ 15) of the subject's **largest city**, the rule in `UEIC` L28 and `PWN` L9. "Largest" is taken from the developer's own Natural Earth populated-places data, already assigned to units by RS1 (scratch `out/places_by_successor.csv`; NE `pop_max`). Coordinates are NE's.

**Corrections where NE's largest place is wrong or is outside the package territory** (the zone is unaffected in every case, because each unit, or every candidate city, lies in one zone):
- **Yamal-Nenets:** NE's top row, "Nakhodka 159,551", is the Primorye city's population attached to a Yamal namesake. Next: Noyabrsk 75.62°E and Novy Urengoy 76.63°E, both **+5**.
- **Khakass:** Abakan is not in NE; the unit lies wholly in +6 (`out/unit_zones.csv`), so **+6**.
- **Moskovskaya (Moscow Oblast):** Balashikha and other large suburbs are absent from NE; NE's largest is Noginsk 38.48°E → **+3**. That Balashikha is the largest and lies near 37.9°E (also +3) is **UNVERIFIED** (recall). ⚠ NE's "Moskva" polygon contains Podolsk, which is administratively Moscow Oblast; this does not change either unit's zone.
- **Leningrad:** NE's largest is Vyborg; the unit lies wholly in +2.
- **Kherson (left bank):** NE's only Kherson place is Kherson city, which is on the right bank and stays Ukrainian (`EUB` §7). The whole oblast lies in +2, so the left bank is **+2**.

**Knife-edge cases (a city within about 0.35° of a zone boundary; DERIVED):**

| Unit | City | Longitude | lon ÷ 15 | Zone | If it fell the other way (primary form) |
|---|---|---|---|---|---|
| Moskva | Moscow | 37.61°E | 2.507 | +3 | Russia's profile goes from +2 28.8% / +3 71.2% to **+2 78.5% / +3 21.5%** (Moscow is 49.7% of Russia's pool and 20.8% of the whole V1 pool) |
| Amur | Blagoveshchensk | 127.53°E | 8.502 | +9 | Künnarantaiga +8 rises from 6.4% to 13.3% (crosses θ = 10%) |
| Tula | Tula | 37.63°E | 2.509 | +3 | Russia +2 from 28.8% to 30.6% |
| Donets'k (V2) | Donetsk | 37.83°E | 2.522 | +3 | V2 Russia +2 from 32.4% to 35.1% |
| Sakhalin | Yuzhno-Sakhalinsk | 142.74°E | 9.516 | +10 | Künnarantaiga +10 falls from 14.5% to 3.4% (drops out at θ = 10%) |

**Territory-centroid alternative** (`out/unit_zones.csv`, RS1): it differs from S7 for exactly seven units: Moskva (+2), Tula (+2), Donets'k (+2), Belgorod (+3), Komi (+4), Tyumen' (+5) and Novosibirsk (+5); the zone profiles in section 6 give its effect.

**Official zones: SOURCED secondary**, en.wikipedia *Time in Russia* (revision 1379421792), table of zones and *"Area covered"*. The zone of each unit's largest city is used for Sakha (Yakutsk, UTC+9; three districts are +10 and six are +11). Crimea and Sevastopol: Moscow Time, per en.wikipedia *Time in Ukraine* (revision 1329019867), which says Crimea *"switched … to Moscow Time"* in 2014 (that sentence carries *"citation needed"*: **UNVERIFIED**). The six Ukrainian units: UTC+2, Ukraine's legal time (same page); the page also says the Donetsk and Luhansk "people's republics" switched to Moscow Time in October 2014, which is not used here.

---

## 5 · Recipient mapping

**SOURCED**, `MAP/Russia/02 reorganization/09 follow-up/subdivisions.csv` (the authoritative file, RS1 §1.1), column `nation`, at the file lines given in the table below (line 1 is the header). Names are exactly as the file gives them; **Idelsk-Uralia and Donska-Kubania are marked provisional** by RS1 §1.2 (conflicting sources). Units: Russia 18 (+6 Ukrainian in V2) · Idelsk-Uralia 25 · Donska-Kubania 7 (+ Crimea and Sevastopol in V1c and V2) · Künnarantaiga 12 · Siberia 11 · Tuva, Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania 1 each · Karelia 2.
- **C-15** (`EUI` L40): Republic of Karelia (L57) → Finland, a non-Russia-split recipient, shown as its own row; Murmansk (L59) → Idelsk-Uralia; the Karelia nation then holds nothing.
- **Kaliningrad:** not in `subdivisions.csv` (`TRK` L149); a CIN member (`EUI` L31). In the K-in variant it is its own row.

### 5.1 The per-unit input table (all 91 source units)

P = population (section 1). y = GRP per head in thousand rubles (2024 primary; 2022 and 2021 sensitivity; the Ukrainian units in 2021 rubles converted from hryvnia). G = Gini 2022. Zones: S7 solar (primary), territory centroid (alternative), official.

| Unit (`R09`) | `R09` line | Recipient (INIT) | P | y 2024 | y 2022 | y 2021 | G 2022 | Solar zone S7 | S7 city | Centroid zone | Official zone |
|---|--:|---|--:|--:|--:|--:|--:|--:|---|--:|--:|
| Chechnya | 2 | Chechnya | 1,510,824 | 344.807 | 207.9 | 187.1 | 0.372 | 3 | Grozny | 3 | 3 |
| Dagestan | 3 | Dagestan | 3,182,054 | 348.978 | 275.2 | 254.0 | 0.370 | 3 | Makhachkala | 3 | 3 |
| Ingush | 4 | Ingushetia | 509,541 | 204.566 | 275.4 | 142.9 | 0.311 | 3 | Nazran | 3 | 3 |
| Kabardin-Balkar | 5 | Kabardino-Balkaria | 904,200 | 381.560 | 275.4 | 239.0 | 0.355 | 3 | Nalchik | 3 | 3 |
| Karachay-Cherkess | 6 | Karachay-Cherkessia | 469,865 | 347.711 | 266.4 | 233.9 | 0.319 | 3 | Cherkessk | 3 | 3 |
| North Ossetia | 7 | North Ossetia-Alania | 687,357 | 473.305 | 327.2 | 291.8 | 0.345 | 3 | Vladikavkaz | 3 | 3 |
| Belgorod | 8 | Russia | 1,540,486 | 1015.794 | 847.4 | 890.4 | 0.368 | 2 | Belgorod | 3 | 3 |
| Bryansk | 9 | Russia | 1,169,161 | 636.575 | 479.0 | 419.3 | 0.360 | 2 | Bryansk | 2 | 3 |
| City of St. Petersburg | 10 | Russia | 5,601,911 | 2301.327 | 2030.0 | 1723.6 | 0.402 | 2 | St.  Petersburg | 2 | 3 |
| Kaluga | 11 | Russia | 1,069,904 | 855.283 | 650.3 | 641.2 | 0.330 | 2 | Kaluga | 2 | 3 |
| Kursk | 12 | Russia | 1,082,458 | 788.412 | 625.3 | 642.7 | 0.356 | 2 | Kursk | 2 | 3 |
| Leningrad | 13 | Russia | 2,000,997 | 1174.111 | 826.8 | 743.7 | 0.345 | 2 | Vyborg (NE largest; unit wholly in zone 2) | 2 | 3 |
| Lipetsk | 14 | Russia | 1,143,224 | 939.205 | 695.1 | 753.4 | 0.367 | 3 | Lipetsk | 3 | 3 |
| Moskovskaya | 15 | Russia | 8,524,665 | 1249.020 | 915.5 | 811.8 | 0.372 | 3 | Noginsk (NE largest; Balashikha absent from NE) | 3 | 3 |
| Moskva | 16 | Russia | 13,010,112 | 3103.504 | 2338.7 | 2099.5 | 0.412 | 3 | Moscow | 2 | 3 |
| Novgorod | 17 | Russia | 583,387 | 842.000 | 658.7 | 598.5 | 0.340 | 2 | Velikiy Novgorod | 2 | 3 |
| Orel | 18 | Russia | 713,374 | 639.833 | 527.0 | 482.3 | 0.357 | 2 | Orel | 2 | 3 |
| Pskov | 19 | Russia | 599,084 | 607.585 | 437.4 | 385.6 | 0.344 | 2 | Pskov | 2 | 3 |
| Ryazan' | 20 | Russia | 1,102,810 | 757.419 | 573.9 | 505.9 | 0.349 | 3 | Ryazan | 3 | 3 |
| Smolensk | 21 | Russia | 888,421 | 761.465 | 556.0 | 488.0 | 0.365 | 2 | Smolensk | 2 | 3 |
| Tambov | 22 | Russia | 982,991 | 609.973 | 469.9 | 455.6 | 0.352 | 3 | Tambov | 3 | 3 |
| Tula | 23 | Russia | 1,501,214 | 891.344 | 684.7 | 603.9 | 0.344 | 3 | Tula | 2 | 3 |
| Tver' | 24 | Russia | 1,230,171 | 690.823 | 516.5 | 466.4 | 0.329 | 2 | Tver | 2 | 3 |
| Voronezh | 25 | Russia | 2,308,792 | 757.722 | 611.0 | 571.3 | 0.385 | 3 | Voronezh | 3 | 3 |
| Sakha (Yakutia) | 26 | Künnarantaiga | 995,686 | 2520.579 | 2031.1 | 1705.2 | 0.404 | 9 | Yakutsk | 9 | 9 |
| Amur | 27 | Künnarantaiga | 766,912 | 1365.680 | 806.6 | 726.2 | 0.384 | 9 | Blagoveshchensk | 9 | 9 |
| Buryat | 28 | Künnarantaiga | 978,588 | 594.962 | 464.6 | 371.9 | 0.355 | 7 | Ulan-Ude | 7 | 8 |
| Chita | 29 | Künnarantaiga | 1,004,125 | 923.857 | 571.0 | 521.1 | 0.348 | 8 | Chita | 8 | 9 |
| Chukchi Autonomous Okrug | 30 | Künnarantaiga | 47,490 | 4678.057 | 3042.0 | 2947.5 | 0.410 | 12 | Anadyr | 12 | 12 |
| Kamchatka | 31 | Künnarantaiga | 291,705 | 1611.201 | 1244.9 | 1217.7 | 0.362 | 11 | Petropavlovsk-Kamchatsky | 11 | 12 |
| Khabarovsk | 32 | Künnarantaiga | 1,292,944 | 1240.000 | 846.1 | 809.4 | 0.351 | 9 | Khabarovsk | 9 | 10 |
| Maga Buryatdan | 33 | Künnarantaiga | 136,085 | 3936.320 | 2349.5 | 2364.4 | 0.397 | 10 | Magadan | 10 | 11 |
| Primor'ye | 34 | Künnarantaiga | 1,845,165 | 1184.384 | 877.0 | 749.7 | 0.361 | 9 | Vladivostok | 9 | 10 |
| Sakhalin | 35 | Künnarantaiga | 466,609 | 3665.840 | 3630.0 | 2667.6 | 0.393 | 10 | Yuzhno Sakhalinsk | 10 | 11 |
| Yevrey | 36 | Künnarantaiga | 150,453 | 786.448 | 551.1 | 530.3 | 0.310 | 9 | Birobidzhan | 9 | 10 |
| Irkutsk | 37 | Künnarantaiga | 2,370,102 | 1284.374 | 1008.5 | 845.6 | 0.353 | 7 | Irkutsk | 7 | 8 |
| Khakass | 38 | Siberia | 534,795 | 749.963 | 657.1 | 597.8 | 0.320 | 6 | (Abakan not in NE; unit wholly in zone 6; NE largest Chernogorsk) | 6 | 7 |
| Krasnoyarsk | 39 | Siberia | 2,856,971 | 1522.495 | 1173.2 | 1105.1 | 0.379 | 6 | Krasnoyarsk | 6 | 7 |
| Altay | 40 | Siberia | 2,163,693 | 605.547 | 443.5 | 410.9 | 0.353 | 6 | Barnaul | 6 | 7 |
| Gorno-Altay | 41 | Siberia | 210,924 | 623.316 | 429.4 | 359.1 | 0.343 | 6 | Gorno Altaysk | 6 | 7 |
| Kemerovo | 42 | Siberia | 2,600,923 | 716.694 | 849.2 | 708.7 | 0.342 | 6 | Novokuznetsk | 6 | 7 |
| Khanty-Mansiy | 43 | Siberia | 1,711,480 | 5610.363 | 4016.8 | 3364.5 | 0.383 | 5 | Surgut | 5 | 5 |
| Novosibirsk | 44 | Siberia | 2,797,176 | 966.865 | 714.2 | 611.0 | 0.368 | 6 | Novosibirsk | 5 | 7 |
| Omsk | 45 | Siberia | 1,858,798 | 779.599 | 515.7 | 440.9 | 0.366 | 5 | Omsk | 5 | 6 |
| Tomsk | 46 | Siberia | 1,062,666 | 1053.060 | 779.3 | 692.2 | 0.340 | 6 | Tomsk | 6 | 7 |
| Tyumen' | 47 | Siberia | 1,601,940 | 1365.511 | 1084.2 | 999.4 | 0.373 | 4 | Tyumen | 5 | 5 |
| Yamal-Nenets | 48 | Siberia | 510,490 | 12196.003 | 10383.0 | 8295.1 | 0.440 | 5 | Noyabrsk (NE 'Nakhodka' row is a mis-assigned namesake) | 5 | 5 |
| Tuva | 49 | Tuva | 336,651 | 449.353 | 326.2 | 280.7 | 0.363 | 6 | Kyzyl | 6 | 7 |
| Bashkortostan | 50 | Idelsk-Uralia | 4,091,423 | 739.699 | 551.8 | 503.0 | 0.375 | 4 | Ufa | 4 | 5 |
| Tatarstan | 51 | Idelsk-Uralia | 4,004,809 | 1361.839 | 1052.7 | 901.7 | 0.379 | 3 | Kazan | 3 | 3 |
| Ivanovo | 52 | Idelsk-Uralia | 927,828 | 557.302 | 400.2 | 338.2 | 0.335 | 3 | Ivanovo | 3 | 3 |
| Kostroma | 53 | Idelsk-Uralia | 580,976 | 711.210 | 506.4 | 450.6 | 0.320 | 3 | Kostroma | 3 | 3 |
| Vladimir | 54 | Idelsk-Uralia | 1,348,134 | 743.499 | 590.3 | 548.1 | 0.325 | 3 | Vladimir | 3 | 3 |
| Yaroslavl' | 55 | Idelsk-Uralia | 1,209,811 | 868.435 | 631.3 | 589.9 | 0.350 | 3 | Yaroslavl | 3 | 3 |
| Arkhangel'sk | 56 | Idelsk-Uralia | 978,873 | 883.412 | 730.9 | 691.6 | 0.339 | 3 | Archangel | 3 | 3 |
| Karelia | 57 | Karelia | 533,121 | 919.389 | 750.5 | 845.7 | 0.324 | 2 | Petrozavodsk | 2 | 3 |
| Komi | 58 | Idelsk-Uralia | 737,853 | 1671.788 | 1339.8 | 1184.1 | 0.353 | 3 | Syktyvkar | 4 | 3 |
| Murmansk | 59 | Karelia | 667,744 | 1714.106 | 1750.7 | 1660.7 | 0.323 | 2 | Murmansk | 2 | 3 |
| Nenets | 60 | Idelsk-Uralia | 41,434 | 14250.822 | 11818.0 | 9878.6 | 0.419 | 4 | Naryan Mar | 4 | 3 |
| Vologda | 61 | Idelsk-Uralia | 1,142,827 | 1081.981 | 911.1 | 909.2 | 0.338 | 3 | Cherepovets | 3 | 3 |
| Chelyabinsk | 62 | Idelsk-Uralia | 3,431,224 | 870.657 | 663.7 | 614.1 | 0.338 | 4 | Chelyabinsk | 4 | 5 |
| Kurgan | 63 | Idelsk-Uralia | 776,661 | 615.394 | 443.3 | 354.9 | 0.337 | 4 | Kurgan | 4 | 5 |
| Orenburg | 64 | Idelsk-Uralia | 1,862,767 | 1134.336 | 855.2 | 764.7 | 0.348 | 4 | Orenburg | 4 | 5 |
| Perm' | 65 | Idelsk-Uralia | 2,532,405 | 1046.002 | 802.5 | 706.5 | 0.367 | 4 | Perm | 4 | 5 |
| Sverdlovsk | 66 | Idelsk-Uralia | 4,268,998 | 1124.324 | 830.2 | 743.7 | 0.395 | 4 | Yekaterinburg | 4 | 5 |
| Udmurt | 67 | Idelsk-Uralia | 1,452,914 | 979.471 | 677.2 | 606.4 | 0.325 | 4 | Izhevsk | 4 | 4 |
| Chuvash | 68 | Idelsk-Uralia | 1,186,909 | 606.492 | 425.8 | 348.6 | 0.336 | 3 | Cheboksary | 3 | 3 |
| Kirov | 69 | Idelsk-Uralia | 1,153,680 | 635.117 | 486.5 | 430.4 | 0.322 | 3 | Kirov | 3 | 3 |
| Mariy-El | 70 | Idelsk-Uralia | 677,097 | 530.998 | 380.1 | 340.7 | 0.336 | 3 | Yoshkar Ola | 3 | 3 |
| Mordovia | 71 | Idelsk-Uralia | 783,552 | 625.379 | 441.1 | 393.3 | 0.346 | 3 | Saransk | 3 | 3 |
| Nizhegorod | 72 | Idelsk-Uralia | 3,119,115 | 1009.914 | 753.9 | 638.3 | 0.384 | 3 | Nizhny Novgorod | 3 | 3 |
| Penza | 73 | Idelsk-Uralia | 1,266,348 | 652.090 | 476.1 | 433.3 | 0.343 | 3 | Penza | 3 | 3 |
| Samara | 74 | Idelsk-Uralia | 3,172,925 | 1062.849 | 771.2 | 701.1 | 0.365 | 3 | Samara | 3 | 4 |
| Saratov | 75 | Idelsk-Uralia | 2,442,575 | 645.768 | 495.4 | 423.4 | 0.359 | 3 | Saratov | 3 | 4 |
| Ul'yanovsk | 76 | Idelsk-Uralia | 1,196,745 | 669.092 | 504.7 | 435.3 | 0.342 | 3 | Ulyanovsk | 3 | 4 |
| Krasnodar | 77 | Donska-Kubania | 5,838,273 | 922.283 | 745.0 | 573.8 | 0.408 | 3 | Krasnodar | 3 | 3 |
| Adygey | 78 | Donska-Kubania | 496,934 | 567.832 | 387.2 | 350.7 | 0.404 | 3 | Maykop | 3 | 3 |
| Rostov | 79 | Donska-Kubania | 4,200,729 | 746.513 | 565.4 | 498.2 | 0.386 | 3 | Rostov | 3 | 3 |
| Stavropol' | 80 | Donska-Kubania | 2,907,593 | 553.020 | 414.5 | 367.5 | 0.335 | 3 | Stavropol | 3 | 3 |
| Kalmyk | 81 | Donska-Kubania | 267,133 | 813.187 | 454.4 | 386.7 | 0.313 | 3 | Elista | 3 | 3 |
| Astrakhan' | 82 | Donska-Kubania | 960,142 | 944.947 | 807.0 | 696.4 | 0.335 | 3 | Astrakhan | 3 | 4 |
| Volgograd | 83 | Donska-Kubania | 2,500,781 | 621.115 | 494.5 | 435.4 | 0.342 | 3 | Volgograd | 3 | 3 |
| Crimea | 84 | Donska-Kubania | 1,934,630 | 470.793 | 347.1 | 326.8 | 0.322 | 2 | Simferopol | 2 | 3 |
| Sevastopol | 85 | Donska-Kubania | 547,820 | 504.990 | 416.8 | 352.2 | 0.330 | 2 | Sevastopol | 2 | 3 |
| Kaliningrad | — | Kaliningrad (K-in only) | 1,029,966 | 937.145 | 723.7 | 681.6 | 0.325 | 1 | Kaliningrad | 1 | 2 |
| Luhans'k | 86 | Russia | 2,102,900 | NOT FOUND | NOT FOUND | 260.4 (96476 UAH (DERIVED stand-in)) | NOT FOUND | 3 | Luhansk | 3 | 2 |
| Donets'k | 87 | Russia | 4,059,400 | NOT FOUND | NOT FOUND | 401.9 (148881 UAH (DERIVED stand-in)) | NOT FOUND | 3 | Donetsk | 2 | 2 |
| Kharkiv | 88 | Russia | 2,599,000 | NOT FOUND | NOT FOUND | 329.9 (122227 UAH) | NOT FOUND | 2 | Kharkiv | 2 | 2 |
| Dnipropetrovs'k | 89 | Russia | 3,096,500 | NOT FOUND | NOT FOUND | 504.0 (186697 UAH) | NOT FOUND | 2 | Dnipro | 2 | 2 |
| Zaporizhzhya | 90 | Russia | 1,638,500 | NOT FOUND | NOT FOUND | 373.9 (138521 UAH) | NOT FOUND | 2 | Zaporizhzhya | 2 | 2 |
| Kherson | 91 | Russia | 340,935 | NOT FOUND | NOT FOUND | 235.9 (87378 UAH) | NOT FOUND | 2 | (left bank; Kherson city is right bank) | 2 | 2 |

---

## 6 · Per-successor pools and zone profiles

### 6.1 Pools under the primary variant (V1 · K-out · INIT; E = P × y2024 × (1 − G2022))
W in trillion rubles of Gini-adjusted GRP (DERIVED). The population columns are given so the income effect is visible.

| Successor | Units | Population (2021) | Pop. share | W (tn RUB) | **W share = split (a)** |
|---|--:|--:|--:|--:|--:|
| Russia | 18 | 45,053,162 | 31.36% | 47.73 | **41.83%** |
| Idelsk-Uralia | 25 | 44,387,883 | 30.90% | 26.70 | **23.41%** |
| Donska-Kubania | 7 | 17,171,585 | 11.95% | 8.13 | **7.12%** |
| Künnarantaiga | 12 | 10,345,864 | 7.20% | 9.40 | **8.24%** |
| Siberia | 11 | 17,909,856 | 12.47% | 19.28 | **16.90%** |
| Tuva | 1 | 336,651 | 0.23% | 0.10 | **0.08%** |
| Karelia | 2 | 1,200,865 | 0.84% | 1.11 | **0.97%** |
| Chechnya | 1 | 1,510,824 | 1.05% | 0.33 | **0.29%** |
| Dagestan | 1 | 3,182,054 | 2.21% | 0.70 | **0.61%** |
| Ingushetia | 1 | 509,541 | 0.35% | 0.07 | **0.06%** |
| Kabardino-Balkaria | 1 | 904,200 | 0.63% | 0.22 | **0.20%** |
| Karachay-Cherkessia | 1 | 469,865 | 0.33% | 0.11 | **0.10%** |
| North Ossetia-Alania | 1 | 687,357 | 0.48% | 0.21 | **0.19%** |
| **Total** | 82 | 143,669,707 | 100% | 114.09 | 100% |

**Concentration (DERIVED):** Moscow city alone is 20.8% of the whole V1 pool and 49.7% of Russia's; St. Petersburg 6.8%, Moscow Oblast 5.9%, Khanty-Mansiy 5.2%, Yamal-Nenets 3.1%, Tatarstan 3.0%. This is the income factor applied to head-office and resource regions (section 2.1's caveat), not a population fact.

### 6.2 Zone profiles q(z), primary (solar zones, S7, E as in 6.1)
The last column lists the meaningful zones Z(θ) at **θ = 5% / 10% (default) / 25%**.

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Russia | +2: 28.8% · +3: 71.2% | {+2,+3} / {+2,+3} / {+2,+3} |
| Idelsk-Uralia | +3: 57.1% · +4: 42.9% | {+3,+4} / {+3,+4} / {+3,+4} |
| Donska-Kubania | +3: 100.0% | {+3} / {+3} / {+3} |
| Künnarantaiga | +7: 24.9% · +8: 6.4% · +9: 49.6% · +10: 14.5% · +11: 3.2% · +12: 1.4% | {+7,+8,+9,+10} / {+7,+9,+10} / {+9} |
| Siberia | +4: 7.1% · +5: 53.6% · +6: 39.3% | {+4,+5,+6} / {+5,+6} / {+5,+6} |
| Tuva | +6: 100.0% | {+6} / {+6} / {+6} |
| Karelia | +2: 100.0% | {+2} / {+2} / {+2} |
| Chechnya | +3: 100.0% | {+3} / {+3} / {+3} |
| Dagestan | +3: 100.0% | {+3} / {+3} / {+3} |
| Ingushetia | +3: 100.0% | {+3} / {+3} / {+3} |
| Kabardino-Balkaria | +3: 100.0% | {+3} / {+3} / {+3} |
| Karachay-Cherkessia | +3: 100.0% | {+3} / {+3} / {+3} |
| North Ossetia-Alania | +3: 100.0% | {+3} / {+3} / {+3} |

### 6.3 Zone profiles under the reported alternatives (only the rows that differ from 6.2)

Each block lists only the successors whose row differs from the primary table in 6.2, so the "official" blocks for V1c and C-15 repeat most of the plain official-zones block; the rows that are new in each are Donska-Kubania (V1c) and Idelsk-Uralia and Finland (C-15).

**Territory centroid (S7 alternative):**

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Russia | +2: 78.3% · +3: 21.7% | {+2,+3} / {+2,+3} / {+2} |
| Idelsk-Uralia | +3: 54.1% · +4: 45.9% | {+3,+4} / {+3,+4} / {+3,+4} |
| Siberia | +5: 69.5% · +6: 30.5% | {+5,+6} / {+5,+6} / {+5,+6} |

**Official zones (S5 alternative):**

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Russia | +3: 100.0% | {+3} / {+3} / {+3} |
| Idelsk-Uralia | +3: 44.6% · +4: 17.4% · +5: 38.0% | {+3,+4,+5} / {+3,+4,+5} / {+3,+5} |
| Donska-Kubania | +3: 92.6% · +4: 7.4% | {+3,+4} / {+3} / {+3} |
| Künnarantaiga | +8: 24.9% · +9: 29.2% · +10: 26.8% · +11: 14.5% · +12: 4.6% | {+8,+9,+10,+11} / {+8,+9,+10,+11} / {+9,+10} |
| Siberia | +5: 55.9% · +6: 4.8% · +7: 39.3% | {+5,+7} / {+5,+7} / {+5,+7} |
| Tuva | +7: 100.0% | {+7} / {+7} / {+7} |
| Karelia | +3: 100.0% | {+3} / {+3} / {+3} |

**V1c, solar:**

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Donska-Kubania | +2: 9.0% · +3: 91.0% | {+2,+3} / {+3} / {+3} |

**V1c, official:**

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Russia | +3: 100.0% | {+3} / {+3} / {+3} |
| Idelsk-Uralia | +3: 44.6% · +4: 17.4% · +5: 38.0% | {+3,+4,+5} / {+3,+4,+5} / {+3,+5} |
| Donska-Kubania | +3: 93.2% · +4: 6.8% | {+3,+4} / {+3} / {+3} |
| Künnarantaiga | +8: 24.9% · +9: 29.2% · +10: 26.8% · +11: 14.5% · +12: 4.6% | {+8,+9,+10,+11} / {+8,+9,+10,+11} / {+9,+10} |
| Siberia | +5: 55.9% · +6: 4.8% · +7: 39.3% | {+5,+7} / {+5,+7} / {+5,+7} |
| Tuva | +7: 100.0% | {+7} / {+7} / {+7} |
| Karelia | +3: 100.0% | {+3} / {+3} / {+3} |

**V2, solar** (E = P × y2021 for every unit; so even the unchanged successors' profiles shift slightly):

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Russia | +2: 32.4% · +3: 67.6% | {+2,+3} / {+2,+3} / {+2,+3} |
| Idelsk-Uralia | +3: 56.9% · +4: 43.1% | {+3,+4} / {+3,+4} / {+3,+4} |
| Donska-Kubania | +2: 8.8% · +3: 91.2% | {+2,+3} / {+3} / {+3} |
| Künnarantaiga | +7: 24.4% · +8: 5.4% · +9: 49.0% · +10: 16.1% · +11: 3.7% · +12: 1.4% | {+7,+8,+9,+10} / {+7,+9,+10} / {+9} |
| Siberia | +4: 7.6% · +5: 51.1% · +6: 41.3% | {+4,+5,+6} / {+5,+6} / {+5,+6} |

**V2, centroid:**

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Russia | +2: 79.9% · +3: 20.1% | {+2,+3} / {+2,+3} / {+2} |
| Idelsk-Uralia | +3: 53.8% · +4: 46.2% | {+3,+4} / {+3,+4} / {+3,+4} |
| Donska-Kubania | +2: 8.8% · +3: 91.2% | {+2,+3} / {+3} / {+3} |
| Künnarantaiga | +7: 24.4% · +8: 5.4% · +9: 49.0% · +10: 16.1% · +11: 3.7% · +12: 1.4% | {+7,+8,+9,+10} / {+7,+9,+10} / {+9} |
| Siberia | +5: 66.8% · +6: 33.2% | {+5,+6} / {+5,+6} / {+5,+6} |

**V2, official:**

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Russia | +2: 8.8% · +3: 91.2% | {+2,+3} / {+3} / {+3} |
| Idelsk-Uralia | +3: 44.9% · +4: 16.6% · +5: 38.5% | {+3,+4,+5} / {+3,+4,+5} / {+3,+5} |
| Donska-Kubania | +3: 92.9% · +4: 7.1% | {+3,+4} / {+3} / {+3} |
| Künnarantaiga | +8: 24.4% · +9: 28.6% · +10: 25.8% · +11: 16.1% · +12: 5.1% | {+8,+9,+10,+11,+12} / {+8,+9,+10,+11} / {+9,+10} |
| Siberia | +5: 54.8% · +6: 3.9% · +7: 41.3% | {+5,+7} / {+5,+7} / {+5,+7} |
| Tuva | +7: 100.0% | {+7} / {+7} / {+7} |
| Karelia | +3: 100.0% | {+3} / {+3} / {+3} |

**C-15, solar:**

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Idelsk-Uralia | +2: 2.8% · +3: 55.5% · +4: 41.7% | {+3,+4} / {+3,+4} / {+3,+4} |
| Finland (Rep. of Karelia piece, C-15) | +2: 100.0% | {+2} / {+2} / {+2} |

**C-15, official:**

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Russia | +3: 100.0% | {+3} / {+3} / {+3} |
| Idelsk-Uralia | +3: 46.2% · +4: 16.9% · +5: 36.9% | {+3,+4,+5} / {+3,+4,+5} / {+3,+5} |
| Donska-Kubania | +3: 92.6% · +4: 7.4% | {+3,+4} / {+3} / {+3} |
| Künnarantaiga | +8: 24.9% · +9: 29.2% · +10: 26.8% · +11: 14.5% · +12: 4.6% | {+8,+9,+10,+11} / {+8,+9,+10,+11} / {+9,+10} |
| Siberia | +5: 55.9% · +6: 4.8% · +7: 39.3% | {+5,+7} / {+5,+7} / {+5,+7} |
| Tuva | +7: 100.0% | {+7} / {+7} / {+7} |
| Finland (Rep. of Karelia piece, C-15) | +3: 100.0% | {+3} / {+3} / {+3} |

**K-in** (Kaliningrad's own row; every other successor's profile is unchanged from 6.2 under solar zones and from the official-zones table above under official zones):

| Successor | q(z) | Z(5%) / Z(10%) / Z(25%) |
|---|---|---|
| Kaliningrad (K-in), solar | +1: 100.0% | {+1} / {+1} / {+1} |
| Kaliningrad (K-in), official | +2: 100.0% | {+2} / {+2} / {+2} |

**S6 (no wraparound):** Künnarantaiga's only territory past the date line is Chukotka east of 180° (RS1 §1.2); with S7 Chukotka sits at +12 (Anadyr, 177.47°E), so no unit is placed at −11 or −12 and wraparound cannot arise under S7.

---

## 7 · Split (a), city-independent

*p_k = W_k ÷ Σ W_j* (RS1 §5 Step 3). Percentages of the former-Russia share; each row sums to 100% (rounding aside).

### 7.1 All S1 × S2 × S3 variants
V1 and V1c: E = P × y2024 × (1 − G2022). **V2: E = P × y2021 for all units** (Ukrainian Gini NOT FOUND; the default's fallback).

| Variant | Russia | Idelsk-Uralia (prov.) | Donska-Kubania (prov.) | Künnarantaiga | Siberia | Tuva | Karelia | Chechnya | Dagestan | Ingushetia | Kabardino-Balkaria | Karachay-Cherkessia | North Ossetia-Alania | Kaliningrad (K-in) | Finland, Rep. of Karelia (C-15) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| V1 · K-out · INIT (primary) | 41.83 | 23.41 | 7.12 | 8.24 | 16.90 | 0.08 | 0.97 | 0.29 | 0.61 | 0.06 | 0.20 | 0.10 | 0.19 | — | — |
| V1 · K-out · C-15 | 41.83 | 24.09 | 7.12 | 8.24 | 16.90 | 0.08 | — | 0.29 | 0.61 | 0.06 | 0.20 | 0.10 | 0.19 | — | 0.29 |
| V1 · K-in · INIT | 41.60 | 23.27 | 7.08 | 8.19 | 16.81 | 0.08 | 0.96 | 0.29 | 0.61 | 0.06 | 0.19 | 0.10 | 0.19 | 0.57 | — |
| V1 · K-in · C-15 | 41.60 | 23.95 | 7.08 | 8.19 | 16.81 | 0.08 | — | 0.29 | 0.61 | 0.06 | 0.19 | 0.10 | 0.19 | 0.57 | 0.29 |
| V1c · K-out · INIT | 41.54 | 23.24 | 7.77 | 8.18 | 16.78 | 0.08 | 0.96 | 0.28 | 0.61 | 0.06 | 0.19 | 0.10 | 0.19 | — | — |
| V1c · K-out · C-15 | 41.54 | 23.92 | 7.77 | 8.18 | 16.78 | 0.08 | — | 0.28 | 0.61 | 0.06 | 0.19 | 0.10 | 0.19 | — | 0.29 |
| V1c · K-in · INIT | 41.31 | 23.11 | 7.73 | 8.14 | 16.69 | 0.08 | 0.96 | 0.28 | 0.61 | 0.06 | 0.19 | 0.10 | 0.18 | 0.56 | — |
| V1c · K-in · C-15 | 41.31 | 23.78 | 7.73 | 8.14 | 16.69 | 0.08 | — | 0.28 | 0.61 | 0.06 | 0.19 | 0.10 | 0.18 | 0.56 | 0.29 |
| V2 · K-out · INIT | 45.53 | 21.36 | 7.12 | 7.38 | 16.06 | 0.07 | 1.18 | 0.21 | 0.61 | 0.06 | 0.16 | 0.08 | 0.15 | — | — |
| V2 · K-out · C-15 | 45.53 | 22.20 | 7.12 | 7.38 | 16.06 | 0.07 | — | 0.21 | 0.61 | 0.06 | 0.16 | 0.08 | 0.15 | — | 0.34 |
| V2 · K-in · INIT | 45.29 | 21.25 | 7.08 | 7.34 | 15.98 | 0.07 | 1.18 | 0.21 | 0.61 | 0.06 | 0.16 | 0.08 | 0.15 | 0.53 | — |
| V2 · K-in · C-15 | 45.29 | 22.09 | 7.08 | 7.34 | 15.98 | 0.07 | — | 0.21 | 0.61 | 0.06 | 0.16 | 0.08 | 0.15 | 0.53 | 0.34 |

**Readings (DERIVED, arithmetic only):** V1c adds Crimea and Sevastopol to Donska-Kubania (+0.65 point). V2 adds the eastern-Ukraine slice to Russia (13.8 million people, 8.8% of V2 Russia's pool) and, because it must drop the Gini factor and use 2021, also moves every other successor; its Russia share is 3.7 points above V1. K-in takes 0.53 to 0.57 point, spread pro rata. C-15 moves Murmansk's pool to Idelsk-Uralia (+0.68 point) and the Republic of Karelia's to Finland (0.29 point). **No scope variant moves any successor by more than 5 points; the largest move is V2's Russia, +3.70.**

### 7.2 Sensitivity to the pool formula (V1 · K-out · INIT unless stated)

| Form | Russia | Idelsk-Uralia | Donska-Kubania | Künnarantaiga | Siberia | Tuva | Karelia | Chechnya | Dagestan | Ingushetia | Kabardino-Balkaria | Karachay-Cherkessia | North Ossetia-Alania |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| P x y2024 x (1-G2022) [primary] | 41.83 | 23.41 | 7.12 | 8.24 | 16.90 | 0.08 | 0.97 | 0.29 | 0.61 | 0.06 | 0.20 | 0.10 | 0.19 |
| P x y2024 (no Gini) | 42.72 | 22.71 | 7.10 | 8.11 | 17.00 | 0.08 | 0.89 | 0.28 | 0.60 | 0.06 | 0.19 | 0.09 | 0.18 |
| P x y2022 x (1-G2022) | 41.90 | 22.87 | 7.22 | 8.10 | 17.22 | 0.08 | 1.21 | 0.22 | 0.63 | 0.11 | 0.18 | 0.10 | 0.17 |
| P x y2022 | 42.80 | 22.18 | 7.20 | 7.98 | 17.31 | 0.08 | 1.10 | 0.22 | 0.61 | 0.10 | 0.17 | 0.09 | 0.16 |
| P x y2021 x (1-G2022) | 42.61 | 23.09 | 6.84 | 7.86 | 16.77 | 0.08 | 1.36 | 0.23 | 0.66 | 0.06 | 0.18 | 0.10 | 0.17 |
| P x y2021 | 43.54 | 22.40 | 6.81 | 7.74 | 16.85 | 0.08 | 1.24 | 0.23 | 0.64 | 0.06 | 0.17 | 0.09 | 0.16 |
| P only | 31.36 | 30.90 | 11.95 | 7.20 | 12.47 | 0.23 | 0.84 | 1.05 | 2.21 | 0.35 | 0.63 | 0.33 | 0.48 |
| V2 · K-out · INIT, UAH at PPP | 45.97 | 21.19 | 7.06 | 7.32 | 15.93 | 0.07 | 1.18 | 0.21 | 0.61 | 0.05 | 0.16 | 0.08 | 0.15 |
| V2, Donetsk & Luhansk at Ukraine 2021 average | 45.54 | 21.36 | 7.12 | 7.38 | 16.06 | 0.07 | 1.18 | 0.21 | 0.61 | 0.06 | 0.16 | 0.08 | 0.15 |

⚠ The "y2022" rows carry the erroneous Ingushetia value (section 2.2). **The only formula change that moves a successor by more than 5 points is dropping income altogether (P only):** Russia −10.5, Idelsk-Uralia +7.5, Donska-Kubania +4.8, Siberia −4.4. Every income-weighted form keeps Russia within 41.8 to 43.5%.

---

## 8 · NOT FOUND (inputs), in one place

- **Gini for the six Ukrainian units** (no table found; ukrstat.gov.ua fails its certificate check). Forces V2 onto E = P × y.
- **GRP per head for Donetsk and Luhansk after 2013** (Ukrstat does not compute it). V2 uses a DERIVED stand-in.
- **GRP per head for any Ukrainian unit after 2021.**
- **The correct 2022 GRP per head of Ingushetia** (the ru.wikipedia value is wrong).
- **A left-bank Kherson population from any statistical source** (the developer's area-weighted guess is used).
- **Rosstat primaries** for all three Russian series (TLS-blocked; secondary transcriptions used throughout).
- **Which Gini measure CEIC carries** (section 3).

---

## 9 · Search and retrieval log (exact strings; per LAW 0-R)

| # | String or URL | Tool | Result |
|---|---|---|---|
| S1 | `коэффициент Джини по субъектам Российской Федерации 2021 все регионы таблица` | WebSearch | No all-subject table. rosstat.gov.ru/folder/13723 and single-region 2021 PDFs (Tuva 0.364, Khakassia 0.330, Krasnoyarsk 0.385, snippets) on TLS-blocked hosts. **Dead at the source.** |
| S2 | `перепись 2021 Республика Крым Севастополь численность населения итоги 1 934 630` | WebSearch | Rosstat and Krymstat PDFs only (TLS-blocked); snippets inconsistent. **Dead at the source**; resolved by S8. |
| S3 | `валовий регіональний продукт у розрахунку на одну особу 2021 по регіонах України Донецька Луганська Харківська Дніпропетровська Запорізька Херсонська` | WebSearch | Found the Lviv office page (Lviv 2021 = 119.0 thousand grn). Used via R4. |
| S4 | `ВРП на одну особу 2021 Донецька область Луганська область тис. грн Держстат регіони рейтинг` | WebSearch | No Donetsk/Luhansk 2021 value. **Dead at the source** (Ukrstat does not compute it; R4 note). |
| S5 | `average official exchange rate 2021 hryvnia per US dollar 27.2862 ruble per dollar 73.6541` | WebSearch | Daily NBU fixings only. **Dead at the query**; resolved by R7 (World Bank API). |
| S6 | `коефіцієнт Джині за регіонами України 2021 Донецька Харківська Запорізька Дніпропетровська область` | WebSearch | Academic papers with an integral inequality index, no oblast Gini values. **Dead at the sources** (not opened beyond snippets). |
| S7 | `statbase коэффициент Джини по регионам России 2021` | WebSearch | Gaidar Institute note (R10); Chukotka 2021 = 0.410 (snippet). No all-region table. |
| S8 | `"2021 census" Crimea population 1,934,630 Sevastopol 547,820` | WebSearch | Found en.wikipedia *Demographics of Crimea*; verified by R5. |
| S9 | `"коэффициент Джини" "Ненецкий автономный округ" "Ямало-Ненецкий" "Республика Ингушетия" 2021 регионы таблица значения` | WebSearch | Same papers as S1/S7. **Dead at the query.** |
| S10 | `Gini coefficient by federal subject of Russia 2021 dataset all regions csv` | WebSearch | Found the CEIC page (R11), used. |
| S11 | `ВРП на душу населения Ингушетия 2022 год тысяч рублей Росстат` | WebSearch | Found statbase.ru (R12, R13), used. |
| R1 | ru.wikipedia GRP-per-head list (`oldid=152668547`) | curl | Read; parsed all 85 rows and the national row. |
| R2 | https://pop-stat.mashke.org/russia-census-2021-ethnic/total.htm | curl | Read; identical to EO3's copy. |
| R3 | en.wikipedia `2021_Russian_census`; ru.wikipedia `Всероссийская_перепись_населения_(2020)` | curl | Read; provisional tables (thousands) used as cross-check. |
| R4 | lv.ukrstat.gov.ua `pb_fig2021/chapter_3_1.html`, `chapter_1_3.html`, `chapter_2_1.html`; `pb_fig2022/chapter_1_3.html` | curl | First three read and used; the 2022 page returned **404**. |
| R5 | en.wikipedia `Demographics_of_Crimea`, `Republic_of_Crimea`, `Sevastopol`, `Kherson_Oblast` | curl | Crimea and Kherson figures read and used. |
| R6 | en.wikipedia `List_of_regions_of_Ukraine_by_GDP`; uk.wikipedia `Валовий_регіональний_продукт` | curl | The en list read (2021, Donetsk/Luhansk N/A); the uk URL redirected to the GDP article, no regional table. **Dead end.** |
| R7 | api.worldbank.org `PA.NUS.FCRF`, `PA.NUS.PPP` (UKR; RUS; 2013–2022) | curl | Read and used. |
| R8 | https://ukrstat.gov.ua/ | curl | **Certificate expired; not bypassed.** |
| R9 | en.wikipedia `Time_in_Russia`, `Time_in_Ukraine` | curl | Read and used. |
| R10 | https://www.iep.ru/files/RePEc/gai/monreo/monreo-2025-4-1385.pdf | curl + pdftotext | Read; national and three regional Gini values (section 3); no full table. |
| R11 | https://www.ceicdata.com/en/russia/household-income-ratio-gini-coefficient | curl | Read; 87 regional series extracted. |
| R12 | statbase.ru `rus-gross-domestic-product-by-region-per-capita-national-stat` | curl | Read; 2024 table, 85 rows. The page offers XLSX/CSV/JSON downloads by script; not used. |
| R13 | statbase.ru `ru6-…` (Ingushetia) | curl | Read; the 2023/2024 values and "maximum in 2024" statement. Its year-by-year series loads by script: **not extracted (open thread).** |
| R14 | jour.fnisc.ru article 8211; naukaru.ru 91666, 179752, 188752; smolgu.ru `science/1.pdf`; emjume.elpub.ru 778 | curl | jour.fnisc.ru: **certificate expired, not bypassed**; emjume returned an HTML page, not the PDF; the rest read: Gini discussed, **no all-region table**. |

**Open threads:** the statbase per-year series (would give a clean 2022 and 2023 for every unit, fixing Ingushetia); Rosstat's Gini table itself (to settle which measure CEIC carries); a raion-level left-bank Kherson population; Ukrainian household-survey inequality by oblast.

---

## FINAL

**Inputs:** all 85 Russian units have a 2021-census population, a 2024 GRP per head and a 2022 Gini from secondary transcriptions of Rosstat, so the primary form E = P × y × (1 − G) runs for V1 and V1c. The six Ukrainian units have 2022-start populations and 2021 GRP per head (two of them DERIVED stand-ins) but no Gini, so V2 runs on E = P × y2021 for all units. Solar zones follow S7, with five corrections to NE's largest-place picks (none changes a zone) and five knife-edge cities listed.

**Split (a), primary (V1 · K-out · INIT):** Russia **41.83%** · Idelsk-Uralia (prov.) **23.41%** · Siberia **16.90%** · Künnarantaiga **8.24%** · Donska-Kubania (prov.) **7.12%** · Karelia **0.97%** · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06%.

**Sensitivity in one line:** no scope variant (V1c, V2, K-in, C-15) or income-weighted formula moves any successor by more than 5 points (largest: V2's Russia, +3.7); dropping income altogether does (Russia −10.5, Idelsk-Uralia +7.5). For split (b), the inputs that matter most are **Moscow's zone (37.61°E, +3 by 0.11°)**, which decides whether Russia's people are mostly +2 or mostly +3, and Blagoveshchensk and Yuzhno-Sakhalinsk for Künnarantaiga's +8 and +10.

**What is left:** RS2 to RS4 (windows, split (b), counts, tiers, sensitivity), which read RS1 and this file. Nothing here is a ruling.
