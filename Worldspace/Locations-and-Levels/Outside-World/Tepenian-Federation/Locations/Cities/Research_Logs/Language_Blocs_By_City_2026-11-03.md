# Language blocs by city: composition arithmetic (2026-11-03)

**Facts only.** For every city, each nation's share in its current composition table (the `Share %` column of the table in its `Specs/<subnet>/<City>.md`, post-`DR-85`/`DR-90`/`DR-93`/`DR-94`) is added up by the main language of that nation. **This file names no city's supporting tier, proposes no threshold, and ranks no city against another.** Hawaiian (later Tepenian) is the dominant language everywhere by ruling and is not a column here. Written 2026-11-03 for later reference; machine-readable copy: `Language_Blocs_By_City_2026-11-03.csv`.

## Method

- **Source of shares:** the first table headed `Tier | Nation | Share %` in each of the 38 spec files (one table per file). Counts of people are summed from the table's own count columns only for the population line.
- **Mapping (one table, below):** every nation or successor region in any table (84 names) is mapped to the main language of its people. The identity of each successor region is from the repo (`Official_Population_Census.md` Section E and the successor-split scratch file `09_Rebalance_and_Successor_Splits.md`); **the language itself is GENERAL knowledge (recalled, not verified)**. No web search was used.
- **Kinds:** **S**, one main language. **S\***, one main language, with named minority languages that are *not* split out (the row's whole share goes to the main language; the flag is shown in the city's table). **M (MULTI)**, a nation or region with several languages and no single main one, or a row built from countries with different languages (Cascadia, Sonora): its share is **not split**. In each city's table every language it might carry is shown with a range: **low** counts only the rows that are certain for that language (S and S\* rows), **high** adds the whole share of every MULTI row that could carry it. **U (UNMAPPED)**: not assigned (one row, Kunlun's Intermarium/Intermaria).
- **Not additive across MULTI rows:** the high values for different languages overlap (a MULTI row is counted once in each language it could carry), so the highs of one city can sum to more than 100%.
- **Check:** each city's table was summed to 100% (rows are rounded to three decimals); all 38 tables total between 99.960% and 100.039%; the largest gaps from 100 are Palmer City (99.960), Janbogo (100.039) and Relung Panen (100.037), which is rounding in the specs' own rows. English and Spanish low/high were recomputed a second time from a fresh read of the spec files: 0 mismatches in 38 cities.
- **Names the tool could not map:** none left; **46 names are ambiguous** and are flagged in the mapping (kinds S\*, M, U).
- **Not in scope:** culture, ranking, any claim about who speaks what in practice. A language's share here is the share of residents whose national origin is a nation of that language, not a count of speakers.

## Mapping: nation or region → language(s)

| Nation or region in the tables | Kind | Language(s) | Source | Note |
|---|---|---|---|---|
| Aceh | M | Acehnese / Indonesian | REPO (Indonesia successor); GENERAL |  |
| Alaska | S* | English | REPO (USA 0.22% + Canada 0.40% successor); GENERAL | indigenous languages not split |
| Amazonia | S | Portuguese | REPO (Brazil successor); GENERAL |  |
| Appalachia | S | English | REPO for the region identity (Section E: successors of the USA/UK); language GENERAL |  |
| Araucanía-Patagonia | S | Spanish | REPO (successor identity per Section E); language GENERAL |  |
| Argentina (without Patagonia) | S | Spanish | REPO (successor identity per Section E); language GENERAL |  |
| Australia | S | English | REPO for the region identity (Section E: successors of the USA/UK); language GENERAL |  |
| Austro-Bavaria | S | German | REPO (Section E: Germany/Austria successors); GENERAL |  |
| Basque Country | M | Basque / Spanish | REPO (Spain successor); GENERAL |  |
| Belarus | M | Belarusian / Russian | GENERAL |  |
| Brazil | S | Portuguese | REPO (Brazil successor); GENERAL |  |
| Bulgaria | S | Bulgarian | GENERAL |  |
| CSA | S | English | REPO for the region identity (Section E: successors of the USA/UK); language GENERAL |  |
| Cascadia | M | English / Spanish | REPO: Cascadia is built from USA 17.96% + Canada 13.82% + Mexico 4.48% (scratch file 09); language GENERAL | Mexican-origin part is Spanish-speaking; split is city-specific and not recoverable from the table |
| Catalonia | M | Catalan / Spanish | REPO (Spain successor); GENERAL |  |
| Chechnya | M | Russian / Chechen | REPO (Russia successor); GENERAL |  |
| Chile | S | Spanish | REPO (successor identity per Section E); language GENERAL |  |
| Colorado | S | English | REPO for the region identity (Section E: successors of the USA/UK); language GENERAL |  |
| Croatia | S | Croatian | GENERAL |  |
| Czechia | S | Czech | REPO (Czech Republic renamed); GENERAL |  |
| Dagestan | M | Russian / Dagestani languages (Avar, Dargin, Lezgin and others) | REPO (Russia successor); GENERAL |  |
| Demilitarized Zone (s. Ontario, not a nation) | S* | English | REPO (Canada's former southern-Ontario territory; treatment of the zone itself still open per Section E); GENERAL | French minority not split; the zone's treatment is an open developer item |
| Denmark | S | Danish | GENERAL |  |
| Donska-Kubania | S* | Russian | REPO (Russia successors); GENERAL | indigenous languages not split |
| East Turkestan | M | Uyghur / Mandarin | REPO (China successor); GENERAL |  |
| Estonia | S | Estonian | GENERAL |  |
| Finland | S* | Finnish | REPO (the Russian successor row that took the Republic of Karelia, per scratch file 09); GENERAL | Swedish minority not split |
| France | S* | French | REPO (Section E: also carries Belgium's and Luxembourg's people); GENERAL |  |
| Germany | S | German | REPO (Section E: Germany/Austria successors); GENERAL |  |
| Hawaii | M | Hawaiian (the dominant language everywhere) / English | REPO (USA 0.41% successor); GENERAL for English | Modern Hawaiian is the national language; the row's own mix is not given |
| Hungary | S | Hungarian | REPO (Section E lists Romania as the old name carried here); GENERAL |  |
| Iceland | S | Icelandic | GENERAL |  |
| Idelsk-Uralia | M | Russian / Tatar and Bashkir | REPO (Russia successor); GENERAL |  |
| Indonesia | S* | Indonesian | REPO; GENERAL | regional languages not split |
| Ingushetia | M | Russian / Ingush | REPO (Russia successor); GENERAL |  |
| Intermarium/Intermaria | U | — | REPO (Kunlun's heritage row for the Intermarium/Intermaria meta-nation, Upper_Earth_Immigration_Composition.md L95; Poland is its political center) | member-state languages not given; left UNMAPPED |
| Japan | S | Japanese | GENERAL |  |
| Kabardino-Balkaria | M | Russian / Kabardian and Balkar | REPO (Russia successor); GENERAL |  |
| Karachay-Cherkessia | M | Russian / Karachay and Circassian languages | REPO (Russia successor); GENERAL |  |
| Kazakhstan | M | Kazakh / Russian | REPO (DR-93 nation added); GENERAL |  |
| Korea | S | Korean | REPO (South and North Korea, with Jeju-do, per Section E); GENERAL |  |
| Künnarantaiga | S* | Russian | REPO (Russia successor, the Russian Far East, capital Vladivostok, per Post-War_Nations_Founder_Reference.md); GENERAL | indigenous languages not split |
| Latvia | S* | Latvian | GENERAL | Russian-speaking minority not split |
| Lithuania | S | Lithuanian | GENERAL |  |
| Magna Lombardia | S* | Italian | REPO (Italy successors); GENERAL | Sicilian and other regional languages not split |
| Malaysia | M | Malay / Chinese (Mandarin and other) / Tamil / English | GENERAL | no majority language by population; split not given |
| Manchuria | S* | Mandarin | REPO (China successor); GENERAL | Manchu is nearly extinct |
| Meridia | S* | Italian | REPO (Italy successors); GENERAL | Sicilian and other regional languages not split |
| Midwest Republic | S | English | REPO for the region identity (Section E: successors of the USA/UK); language GENERAL |  |
| Mongolia | M | Mongolian / Mandarin | REPO (Section E: Mongolia 'with Inner Mongolia'); GENERAL | Inner Mongolia is largely Mandarin-speaking; split not recoverable |
| México | S | Spanish | REPO (successor identity per Section E); language GENERAL |  |
| Netherlands | S | Dutch | REPO (Section E: carries Belgium's Dutch-speaking part); GENERAL |  |
| New England | S | English | REPO for the region identity (Section E: successors of the USA/UK); language GENERAL |  |
| New Zealand | S | English | REPO for the region identity (Section E: successors of the USA/UK); language GENERAL |  |
| North Ossetia-Alania | M | Russian / Ossetian | REPO (Russia successor); GENERAL |  |
| Northern Ireland | S* | English | REPO (UK successor); GENERAL | Irish is a minority language; not split |
| Norway | S | Norwegian | GENERAL |  |
| Patani | M | Patani Malay / Thai | REPO (Thailand successor per Section E); GENERAL |  |
| Philippines | M | Filipino (Tagalog) / English | GENERAL |  |
| Poland | S | Polish | GENERAL |  |
| Prairie Federation | S* | English | REPO (Canada successor); GENERAL | French and other minorities not split |
| Quebec | S* | French | REPO (Canada successor); GENERAL | English minority not split |
| Romania | S | Romanian | GENERAL |  |
| Russia (core state) | S | Russian | REPO (Russia successor, Moscow core; Section E also puts Ukraine here); GENERAL |  |
| Serbia | S* | Serbian | REPO (Section E: Kosovo's people count here); GENERAL | Albanian-speaking Kosovo part not split |
| Siberia | S* | Russian | REPO (Russia successors); GENERAL | indigenous languages not split |
| Sicilia (autonomous zone within Meridia) | S* | Italian | REPO (Italy successors); GENERAL | Sicilian and other regional languages not split |
| Sinian Federation | S* | Mandarin | REPO (China's nine Han states, with Hong Kong and Macau, per Section E); GENERAL | Cantonese, Wu, Min, Hakka and other Sinitic languages are spoken in parts of it; not split |
| Slovakia | S | Slovak | GENERAL |  |
| Slovenia | S | Slovene | GENERAL |  |
| Sonora | M | English / Spanish | REPO: Sonora is built from USA 2.45% + Mexico 6.91% (scratch file 09); language GENERAL | Mexican-origin part is Spanish-speaking; split city-specific |
| South Africa | M | English / Afrikaans / Zulu and other Bantu languages | GENERAL |  |
| Spain | S | Spanish | REPO (successor identity per Section E); language GENERAL |  |
| Sweden | S | Swedish | GENERAL |  |
| Taiwan | S* | Mandarin | REPO (separate nation per Section E); GENERAL | Taiwanese Hokkien, Hakka not split |
| Thailand | S | Thai | GENERAL |  |
| Tibet | M | Tibetan / Mandarin | REPO (China successor); GENERAL |  |
| Tuva | M | Russian / Tuvan | REPO (Russia successor); GENERAL |  |
| Ukraine | M | Ukrainian / Russian | GENERAL | Section E lists Ukraine's people under Russia (core state) for the old country; this row exists separately in 14 tables |
| United Kingdom | S | English | REPO for the region identity (Section E: successors of the USA/UK); language GENERAL |  |
| Uruguay | S | Spanish | REPO (successor identity per Section E); language GENERAL |  |
| Vietnam | S | Vietnamese | GENERAL |  |
| West Papua | S* | Indonesian | REPO (Indonesia successor); GENERAL | Papuan languages not split |
| Yucatán | S* | Spanish | REPO (Mexico and Petén successor); GENERAL | Mayan languages not split |

**Ambiguous names (kinds S\*, M, U), by kind:**

- **MULTI (range):** Aceh; Basque Country; Belarus; Cascadia; Catalonia; Chechnya; Dagestan; East Turkestan; Hawaii; Idelsk-Uralia; Ingushetia; Kabardino-Balkaria; Karachay-Cherkessia; Kazakhstan; Malaysia; Mongolia; North Ossetia-Alania; Patani; Philippines; Sonora; South Africa; Tibet; Tuva; Ukraine
- **one main language, minorities not split:** Alaska; Demilitarized Zone (s. Ontario, not a nation); Donska-Kubania; Finland; France; Indonesia; Künnarantaiga; Latvia; Magna Lombardia; Manchuria; Meridia; Northern Ireland; Prairie Federation; Quebec; Serbia; Siberia; Sicilia (autonomous zone within Meridia); Sinian Federation; Taiwan; West Papua; Yucatán
- **UNMAPPED:** Intermarium/Intermaria

## Per-city tables

### Amundsen Station

*Census I table counts: robots 5,736, humans 1,121; Census II: robots 3,978, humans 913. Share total 99.963%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 41.70 | 46.37 | United Kingdom 10.85; CSA 7.79; Australia 5.72; Appalachia 4.39; Cascadia 3.98; New England 3.59; New Zealand 3.33; Demilitarized Zone (s. Ontario, not a nation) 2.12; Midwest Republic 1.36; Prairie Federation 1.19; Colorado 1.03; Sonora 0.60; Northern Ireland 0.27; Hawaii 0.09; Alaska 0.06 |
| Mandarin | 14.43 | 15.20 | Sinian Federation 10.85; Taiwan 2.81; Manchuria 0.77; Mongolia 0.39; East Turkestan 0.33; Tibet 0.05 |
| German | 12.14 | 12.14 | Germany 8.94; Austro-Bavaria 3.20 |
| Japanese | 10.13 | 10.13 | Japan 10.13 |
| Spanish | 4.87 | 9.45 | Cascadia 3.98; Argentina (without Patagonia) 3.14; Chile 1.33; Sonora 0.60; Araucanía-Patagonia 0.40 |
| Korean | 6.64 | 6.64 | Korea 6.64 |
| French | 1.62 | 1.62 | Quebec 1.62 |
| Norwegian | 1.55 | 1.55 | Norway 1.55 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Russian | 0.00 | 1.45 | Kazakhstan 1.45 |
| Mongolian | 0.00 | 0.39 | Mongolia 0.39 |
| Uyghur | 0.00 | 0.33 | East Turkestan 0.33 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.09 | Hawaii 0.09 |
| Tibetan | 0.00 | 0.05 | Tibet 0.05 |

**MULTI / UNMAPPED rows in this city:** Cascadia 3.980% (MULTI: English / Spanish); Kazakhstan 1.450% (MULTI: Kazakh / Russian); Sonora 0.600% (MULTI: English / Spanish); Mongolia 0.390% (MULTI: Mongolian / Mandarin); East Turkestan 0.330% (MULTI: Uyghur / Mandarin); Hawaii 0.089% (MULTI: Hawaiian (the dominant language everywhere) / English); Tibet 0.047% (MULTI: Tibetan / Mandarin)

### Byrd

*Census I table counts: robots 215,671, humans 213,338. Share total 100.019%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 28.53 | 39.13 | Australia 6.99; CSA 4.39; Demilitarized Zone (s. Ontario, not a nation) 4.22; Cascadia 3.65; Appalachia 2.82; Prairie Federation 2.38; New England 2.30; Philippines 2.23; Malaysia 2.20; South Africa 2.02; New Zealand 1.90; United Kingdom 1.88; Midwest Republic 0.88; Colorado 0.66; Sonora 0.44; Alaska 0.06; Hawaii 0.06; Northern Ireland 0.05 |
| Spanish | 5.58 | 9.87 | Cascadia 3.65; Uruguay 1.96; Argentina (without Patagonia) 0.92; Chile 0.88; México 0.77; Spain 0.70; Sonora 0.44; Araucanía-Patagonia 0.20; Catalonia 0.15; Yucatán 0.15; Basque Country 0.05 |
| Japanese | 6.74 | 6.74 | Japan 6.74 |
| French | 4.72 | 4.72 | Quebec 3.23; France 1.49 |
| Russian | 1.16 | 3.57 | Belarus 1.17; Ukraine 0.81; Russia (core state) 0.78; Idelsk-Uralia 0.37; Siberia 0.15; Donska-Kubania 0.14; Künnarantaiga 0.09; Dagestan 0.03; Chechnya 0.01; Kabardino-Balkaria 0.01; North Ossetia-Alania 0.01; Ingushetia 0.00; Karachay-Cherkessia 0.00; Tuva 0.00 |
| Korean | 3.19 | 3.19 | Korea 3.19 |
| Dutch | 2.63 | 2.63 | Netherlands 2.63 |
| Lithuanian | 2.27 | 2.27 | Lithuania 2.27 |
| Filipino (Tagalog) | 0.00 | 2.23 | Philippines 2.23 |
| Thai | 2.16 | 2.22 | Thailand 2.16; Patani 0.06 |
| Indonesian | 2.17 | 2.21 | Indonesia 2.12; West Papua 0.04; Aceh 0.04 |
| Chinese (Mandarin and other) | 0.00 | 2.20 | Malaysia 2.20 |
| Malay | 0.00 | 2.20 | Malaysia 2.20 |
| Portuguese | 2.20 | 2.20 | Brazil 1.98; Amazonia 0.22 |
| Tamil | 0.00 | 2.20 | Malaysia 2.20 |
| Croatian | 2.16 | 2.16 | Croatia 2.16 |
| Latvian | 2.15 | 2.15 | Latvia 2.15 |
| Slovak | 2.06 | 2.06 | Slovakia 2.06 |
| Afrikaans | 0.00 | 2.02 | South Africa 2.02 |
| Zulu and other Bantu languages | 0.00 | 2.02 | South Africa 2.02 |
| Czech | 1.96 | 1.96 | Czechia 1.96 |
| Vietnamese | 1.94 | 1.94 | Vietnam 1.94 |
| Finnish | 1.90 | 1.90 | Finland 1.90 |
| Mandarin | 1.82 | 1.82 | Sinian Federation 1.82 |
| Romanian | 1.70 | 1.70 | Romania 1.70 |
| Hungarian | 1.43 | 1.43 | Hungary 1.43 |
| Norwegian | 1.23 | 1.23 | Norway 1.23 |
| German | 1.19 | 1.19 | Germany 1.00; Austro-Bavaria 0.19 |
| Belarusian | 0.00 | 1.17 | Belarus 1.17 |
| Polish | 1.16 | 1.16 | Poland 1.16 |
| Bulgarian | 1.06 | 1.06 | Bulgaria 1.06 |
| Slovene | 0.92 | 0.92 | Slovenia 0.92 |
| Italian | 0.91 | 0.91 | Magna Lombardia 0.52; Meridia 0.32; Sicilia (autonomous zone within Meridia) 0.07 |
| Swedish | 0.90 | 0.90 | Sweden 0.90 |
| Serbian | 0.86 | 0.86 | Serbia 0.86 |
| Ukrainian | 0.00 | 0.81 | Ukraine 0.81 |
| Tatar and Bashkir | 0.00 | 0.37 | Idelsk-Uralia 0.37 |
| Catalan | 0.00 | 0.15 | Catalonia 0.15 |
| Patani Malay | 0.00 | 0.06 | Patani 0.06 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.06 | Hawaii 0.06 |
| Basque | 0.00 | 0.05 | Basque Country 0.05 |
| Acehnese | 0.00 | 0.04 | Aceh 0.04 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.03 | Dagestan 0.03 |
| Chechen | 0.00 | 0.01 | Chechnya 0.01 |
| Kabardian and Balkar | 0.00 | 0.01 | Kabardino-Balkaria 0.01 |
| Ossetian | 0.00 | 0.01 | North Ossetia-Alania 0.01 |
| Ingush | 0.00 | 0.00 | Ingushetia 0.00 |
| Karachay and Circassian languages | 0.00 | 0.00 | Karachay-Cherkessia 0.00 |
| Tuvan | 0.00 | 0.00 | Tuva 0.00 |

**MULTI / UNMAPPED rows in this city:** Cascadia 3.650% (MULTI: English / Spanish); Philippines 2.230% (MULTI: Filipino (Tagalog) / English); Malaysia 2.200% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); South Africa 2.020% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Belarus 1.170% (MULTI: Belarusian / Russian); Ukraine 0.810% (MULTI: Ukrainian / Russian); Sonora 0.440% (MULTI: English / Spanish); Idelsk-Uralia 0.370% (MULTI: Russian / Tatar and Bashkir); Catalonia 0.150% (MULTI: Catalan / Spanish); Patani 0.063% (MULTI: Patani Malay / Thai); Hawaii 0.057% (MULTI: Hawaiian (the dominant language everywhere) / English); Basque Country 0.054% (MULTI: Basque / Spanish); Aceh 0.044% (MULTI: Acehnese / Indonesian); Dagestan 0.026% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Chechnya 0.013% (MULTI: Russian / Chechen); Kabardino-Balkaria 0.007% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.006% (MULTI: Russian / Ossetian); Ingushetia 0.004% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.004% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.003% (MULTI: Russian / Tuvan)

### Belgrano

*Census I table counts: robots 565,015, humans 558,996; Census II: robots 427,150, humans 446,498. Share total 99.985%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 27.79 | 35.38 | CSA 9.08; Appalachia 5.83; New England 4.76; United Kingdom 4.75; Cascadia 4.24; South Africa 2.44; Midwest Republic 1.81; Colorado 1.36; Sonora 0.80; Northern Ireland 0.14; Hawaii 0.12; Alaska 0.06 |
| Spanish | 13.41 | 18.45 | Uruguay 4.82; Cascadia 4.24; Argentina (without Patagonia) 4.08; Chile 3.67; Araucanía-Patagonia 0.84; Sonora 0.80 |
| German | 14.92 | 14.92 | Germany 11.07; Austro-Bavaria 3.85 |
| Portuguese | 13.48 | 13.48 | Brazil 12.14; Amazonia 1.34 |
| Hungarian | 5.22 | 5.22 | Hungary 5.22 |
| Polish | 5.09 | 5.09 | Poland 5.09 |
| Slovak | 4.58 | 4.58 | Slovakia 4.58 |
| Czech | 2.75 | 2.75 | Czechia 2.75 |
| Slovene | 2.69 | 2.69 | Slovenia 2.69 |
| Afrikaans | 0.00 | 2.44 | South Africa 2.44 |
| Zulu and other Bantu languages | 0.00 | 2.44 | South Africa 2.44 |
| Serbian | 1.85 | 1.85 | Serbia 1.85 |
| Croatian | 0.61 | 0.61 | Croatia 0.61 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.12 | Hawaii 0.12 |

**MULTI / UNMAPPED rows in this city:** Cascadia 4.240% (MULTI: English / Spanish); South Africa 2.440% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Sonora 0.800% (MULTI: English / Spanish); Hawaii 0.120% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Halley

*Census I table counts: robots 767,646, humans 736,821; Census II: robots 598,062, humans 525,888. Share total 100.021%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 35.07 | 42.47 | United Kingdom 10.07; CSA 7.46; Cascadia 4.88; Appalachia 4.79; New England 3.92; Demilitarized Zone (s. Ontario, not a nation) 3.75; Prairie Federation 2.11; South Africa 1.76; Midwest Republic 1.49; Colorado 1.12; Sonora 0.66; Northern Ireland 0.29; Hawaii 0.10; Alaska 0.07 |
| Spanish | 6.03 | 11.57 | Cascadia 4.88; Chile 3.23; Argentina (without Patagonia) 2.15; Sonora 0.66; Araucanía-Patagonia 0.65 |
| Portuguese | 11.46 | 11.46 | Brazil 10.32; Amazonia 1.14 |
| French | 10.21 | 10.21 | France 7.34; Quebec 2.87 |
| German | 5.84 | 5.84 | Germany 3.46; Austro-Bavaria 2.38 |
| Dutch | 4.22 | 4.22 | Netherlands 4.22 |
| Serbian | 4.09 | 4.09 | Serbia 4.09 |
| Croatian | 4.08 | 4.08 | Croatia 4.08 |
| Slovene | 4.00 | 4.00 | Slovenia 4.00 |
| Polish | 3.49 | 3.49 | Poland 3.49 |
| Afrikaans | 0.00 | 1.76 | South Africa 1.76 |
| Zulu and other Bantu languages | 0.00 | 1.76 | South Africa 1.76 |
| Czech | 1.75 | 1.75 | Czechia 1.75 |
| Hungarian | 1.55 | 1.55 | Hungary 1.55 |
| Slovak | 0.83 | 0.83 | Slovakia 0.83 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.10 | Hawaii 0.10 |

**MULTI / UNMAPPED rows in this city:** Cascadia 4.880% (MULTI: English / Spanish); South Africa 1.760% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Sonora 0.660% (MULTI: English / Spanish); Hawaii 0.097% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Lazar

*Census I table counts: robots 1,225,034, humans 1,185,375; Census II: robots 867,696, humans 791,764. Share total 100.021%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 25.14 | 30.09 | United Kingdom 9.61; CSA 6.04; Appalachia 3.88; New England 3.17; Cascadia 2.83; South Africa 1.52; Midwest Republic 1.21; Colorado 0.91; Sonora 0.53; Northern Ireland 0.28; Hawaii 0.08; Alaska 0.04 |
| German | 11.02 | 11.02 | Germany 7.80; Austro-Bavaria 3.22 |
| Portuguese | 8.87 | 8.87 | Brazil 7.99; Amazonia 0.88 |
| Russian | 3.53 | 8.14 | Russia (core state) 2.04; Belarus 1.77; Idelsk-Uralia 1.48; Ukraine 1.11; Siberia 0.59; Donska-Kubania 0.56; Künnarantaiga 0.34; Dagestan 0.10; Chechnya 0.05; Kabardino-Balkaria 0.03; North Ossetia-Alania 0.02; Ingushetia 0.02; Karachay-Cherkessia 0.01; Tuva 0.01 |
| Spanish | 1.43 | 4.79 | Cascadia 2.83; Argentina (without Patagonia) 1.35; Sonora 0.53; Araucanía-Patagonia 0.08 |
| Norwegian | 3.35 | 3.35 | Norway 3.35 |
| Hungarian | 3.31 | 3.31 | Hungary 3.31 |
| Finnish | 3.29 | 3.29 | Finland 3.29 |
| Czech | 3.24 | 3.24 | Czechia 3.24 |
| Estonian | 3.23 | 3.23 | Estonia 3.23 |
| Polish | 3.15 | 3.15 | Poland 3.15 |
| Slovene | 3.01 | 3.01 | Slovenia 3.01 |
| Serbian | 2.96 | 2.96 | Serbia 2.96 |
| Slovak | 2.94 | 2.94 | Slovakia 2.94 |
| Romanian | 2.52 | 2.52 | Romania 2.52 |
| French | 2.42 | 2.42 | France 2.42 |
| Belarusian | 0.00 | 1.77 | Belarus 1.77 |
| Lithuanian | 1.73 | 1.73 | Lithuania 1.73 |
| Afrikaans | 0.00 | 1.52 | South Africa 1.52 |
| Zulu and other Bantu languages | 0.00 | 1.52 | South Africa 1.52 |
| Tatar and Bashkir | 0.00 | 1.48 | Idelsk-Uralia 1.48 |
| Croatian | 1.44 | 1.44 | Croatia 1.44 |
| Latvian | 1.40 | 1.40 | Latvia 1.40 |
| Bulgarian | 1.31 | 1.31 | Bulgaria 1.31 |
| Dutch | 1.17 | 1.17 | Netherlands 1.17 |
| Ukrainian | 0.00 | 1.11 | Ukraine 1.11 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.10 | Dagestan 0.10 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.08 | Hawaii 0.08 |
| Chechen | 0.00 | 0.05 | Chechnya 0.05 |
| Kabardian and Balkar | 0.00 | 0.03 | Kabardino-Balkaria 0.03 |
| Ossetian | 0.00 | 0.02 | North Ossetia-Alania 0.02 |
| Ingush | 0.00 | 0.02 | Ingushetia 0.02 |
| Karachay and Circassian languages | 0.00 | 0.01 | Karachay-Cherkessia 0.01 |
| Tuvan | 0.00 | 0.01 | Tuva 0.01 |

**MULTI / UNMAPPED rows in this city:** Cascadia 2.830% (MULTI: English / Spanish); Belarus 1.770% (MULTI: Belarusian / Russian); South Africa 1.520% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Idelsk-Uralia 1.480% (MULTI: Russian / Tatar and Bashkir); Ukraine 1.110% (MULTI: Ukrainian / Russian); Sonora 0.530% (MULTI: English / Spanish); Dagestan 0.100% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Hawaii 0.078% (MULTI: Hawaiian (the dominant language everywhere) / English); Chechnya 0.050% (MULTI: Russian / Chechen); Kabardino-Balkaria 0.030% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.023% (MULTI: Russian / Ossetian); Ingushetia 0.017% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.015% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.011% (MULTI: Russian / Tuvan)

### Neumayer

*Census I table counts: robots 663,395, humans 640,806; Census II: robots 464,878, humans 401,750. Share total 99.977%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 20.76 | 25.43 | CSA 6.19; United Kingdom 5.00; Appalachia 3.97; New England 3.25; Cascadia 2.89; Midwest Republic 1.24; South Africa 1.15; Colorado 0.93; Sonora 0.55; Northern Ireland 0.14; Hawaii 0.08; Alaska 0.04 |
| German | 14.14 | 14.14 | Germany 7.72; Austro-Bavaria 6.42 |
| Spanish | 6.02 | 9.46 | Argentina (without Patagonia) 2.92; Cascadia 2.89; Chile 2.52; Araucanía-Patagonia 0.58; Sonora 0.55 |
| French | 5.71 | 5.71 | France 5.71 |
| Portuguese | 4.51 | 4.51 | Brazil 4.06; Amazonia 0.45 |
| Dutch | 4.46 | 4.46 | Netherlands 4.46 |
| Hungarian | 3.76 | 3.76 | Hungary 3.76 |
| Swedish | 3.58 | 3.58 | Sweden 3.58 |
| Lithuanian | 3.53 | 3.53 | Lithuania 3.53 |
| Slovak | 3.25 | 3.25 | Slovakia 3.25 |
| Bulgarian | 3.04 | 3.04 | Bulgaria 3.04 |
| Russian | 1.00 | 2.99 | Ukraine 1.99; Russia (core state) 1.00 |
| Croatian | 2.95 | 2.95 | Croatia 2.95 |
| Finnish | 2.95 | 2.95 | Finland 2.95 |
| Romanian | 2.63 | 2.63 | Romania 2.63 |
| Ukrainian | 0.00 | 1.99 | Ukraine 1.99 |
| Serbian | 1.85 | 1.85 | Serbia 1.85 |
| Estonian | 1.83 | 1.83 | Estonia 1.83 |
| Latvian | 1.83 | 1.83 | Latvia 1.83 |
| Norwegian | 1.75 | 1.75 | Norway 1.75 |
| Czech | 1.31 | 1.31 | Czechia 1.31 |
| Slovene | 1.25 | 1.25 | Slovenia 1.25 |
| Polish | 1.21 | 1.21 | Poland 1.21 |
| Afrikaans | 0.00 | 1.15 | South Africa 1.15 |
| Zulu and other Bantu languages | 0.00 | 1.15 | South Africa 1.15 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.08 | Hawaii 0.08 |

**MULTI / UNMAPPED rows in this city:** Cascadia 2.890% (MULTI: English / Spanish); Ukraine 1.990% (MULTI: Ukrainian / Russian); South Africa 1.150% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Sonora 0.550% (MULTI: English / Spanish); Hawaii 0.080% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Sanay

*Census I table counts: robots 257,143, humans 258,646; Census II: robots 148,520, humans 162,476. Share total 100.010%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| German | 26.27 | 26.27 | Germany 20.59; Austro-Bavaria 5.68 |
| English | 7.06 | 11.46 | United Kingdom 6.86; South Africa 4.40; Northern Ireland 0.20 |
| Portuguese | 11.36 | 11.36 | Brazil 10.23; Amazonia 1.13 |
| Russian | 1.39 | 5.83 | Ukraine 2.75; Belarus 1.69; Russia (core state) 1.39 |
| Spanish | 5.78 | 5.78 | Argentina (without Patagonia) 3.91; Chile 1.41; Araucanía-Patagonia 0.46 |
| Serbian | 4.52 | 4.52 | Serbia 4.52 |
| Estonian | 4.50 | 4.50 | Estonia 4.50 |
| Afrikaans | 0.00 | 4.40 | South Africa 4.40 |
| Zulu and other Bantu languages | 0.00 | 4.40 | South Africa 4.40 |
| Hungarian | 4.26 | 4.26 | Hungary 4.26 |
| Slovene | 4.04 | 4.04 | Slovenia 4.04 |
| Bulgarian | 3.88 | 3.88 | Bulgaria 3.88 |
| Norwegian | 3.80 | 3.80 | Norway 3.80 |
| Ukrainian | 0.00 | 2.75 | Ukraine 2.75 |
| Czech | 2.34 | 2.34 | Czechia 2.34 |
| Croatian | 2.11 | 2.11 | Croatia 2.11 |
| Latvian | 2.10 | 2.10 | Latvia 2.10 |
| Romanian | 2.03 | 2.03 | Romania 2.03 |
| Slovak | 2.00 | 2.00 | Slovakia 2.00 |
| Polish | 1.99 | 1.99 | Poland 1.99 |
| Lithuanian | 1.74 | 1.74 | Lithuania 1.74 |
| Belarusian | 0.00 | 1.69 | Belarus 1.69 |

**MULTI / UNMAPPED rows in this city:** South Africa 4.400% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Ukraine 2.750% (MULTI: Ukrainian / Russian); Belarus 1.690% (MULTI: Belarusian / Russian)

### Santa Luce

*Census I table counts: robots 237,052, humans 228,766; Census II: robots 137,861, humans 140,994. Share total 99.985%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 21.26 | 25.72 | United Kingdom 7.44; CSA 5.40; Appalachia 3.46; New England 2.83; Cascadia 2.52; South Africa 1.39; Midwest Republic 1.08; Colorado 0.81; Sonora 0.48; Northern Ireland 0.21; Hawaii 0.07; Alaska 0.03 |
| Russian | 6.51 | 11.61 | Russia (core state) 3.71; Idelsk-Uralia 2.78; Ukraine 1.85; Siberia 1.10; Donska-Kubania 1.06; Künnarantaiga 0.64; Dagestan 0.20; Chechnya 0.09; Kabardino-Balkaria 0.06; North Ossetia-Alania 0.04; Ingushetia 0.03; Karachay-Cherkessia 0.03; Tuva 0.02 |
| Portuguese | 8.76 | 8.76 | Brazil 7.89; Amazonia 0.87 |
| Italian | 8.34 | 8.34 | Magna Lombardia 6.25; Meridia 2.09 |
| Spanish | 3.00 | 6.00 | Argentina (without Patagonia) 2.83; Cascadia 2.52; Sonora 0.48; Araucanía-Patagonia 0.17 |
| French | 4.45 | 4.45 | France 4.45 |
| German | 4.08 | 4.08 | Austro-Bavaria 2.10; Germany 1.98 |
| Dutch | 3.73 | 3.73 | Netherlands 3.73 |
| Latvian | 2.98 | 2.98 | Latvia 2.98 |
| Hungarian | 2.89 | 2.89 | Hungary 2.89 |
| Serbian | 2.80 | 2.80 | Serbia 2.80 |
| Croatian | 2.79 | 2.79 | Croatia 2.79 |
| Estonian | 2.79 | 2.79 | Estonia 2.79 |
| Tatar and Bashkir | 0.00 | 2.78 | Idelsk-Uralia 2.78 |
| Czech | 2.66 | 2.66 | Czechia 2.66 |
| Romanian | 2.30 | 2.30 | Romania 2.30 |
| Ukrainian | 0.00 | 1.85 | Ukraine 1.85 |
| Swedish | 1.61 | 1.61 | Sweden 1.61 |
| Lithuanian | 1.54 | 1.54 | Lithuania 1.54 |
| Bulgarian | 1.43 | 1.43 | Bulgaria 1.43 |
| Afrikaans | 0.00 | 1.39 | South Africa 1.39 |
| Norwegian | 1.39 | 1.39 | Norway 1.39 |
| Slovak | 1.39 | 1.39 | Slovakia 1.39 |
| Zulu and other Bantu languages | 0.00 | 1.39 | South Africa 1.39 |
| Finnish | 1.35 | 1.35 | Finland 1.35 |
| Slovene | 1.20 | 1.20 | Slovenia 1.20 |
| Polish | 1.17 | 1.17 | Poland 1.17 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.20 | Dagestan 0.20 |
| Chechen | 0.00 | 0.09 | Chechnya 0.09 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.07 | Hawaii 0.07 |
| Kabardian and Balkar | 0.00 | 0.06 | Kabardino-Balkaria 0.06 |
| Ossetian | 0.00 | 0.04 | North Ossetia-Alania 0.04 |
| Ingush | 0.00 | 0.03 | Ingushetia 0.03 |
| Karachay and Circassian languages | 0.00 | 0.03 | Karachay-Cherkessia 0.03 |
| Tuvan | 0.00 | 0.02 | Tuva 0.02 |

**MULTI / UNMAPPED rows in this city:** Idelsk-Uralia 2.780% (MULTI: Russian / Tatar and Bashkir); Cascadia 2.520% (MULTI: English / Spanish); Ukraine 1.850% (MULTI: Ukrainian / Russian); South Africa 1.390% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Sonora 0.480% (MULTI: English / Spanish); Dagestan 0.200% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Chechnya 0.093% (MULTI: Russian / Chechen); Hawaii 0.070% (MULTI: Hawaiian (the dominant language everywhere) / English); Kabardino-Balkaria 0.056% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.042% (MULTI: Russian / Ossetian); Ingushetia 0.031% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.029% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.021% (MULTI: Russian / Tuvan)

### Troll

*Census I table counts: robots 503,779, humans 502,791; Census II: robots 367,383, humans 340,328. Share total 100.018%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 23.17 | 27.76 | United Kingdom 8.04; CSA 5.90; Appalachia 3.79; New England 3.10; Cascadia 2.76; South Africa 1.24; Midwest Republic 1.18; Colorado 0.89; Sonora 0.52; Northern Ireland 0.23; Hawaii 0.08; Alaska 0.04 |
| Russian | 6.63 | 12.51 | Russia (core state) 3.56; Idelsk-Uralia 3.04; Belarus 1.31; Siberia 1.21; Donska-Kubania 1.16; Ukraine 1.02; Künnarantaiga 0.70; Dagestan 0.21; Chechnya 0.10; Kabardino-Balkaria 0.06; North Ossetia-Alania 0.05; Ingushetia 0.03; Karachay-Cherkessia 0.03; Tuva 0.02 |
| Portuguese | 8.22 | 8.22 | Brazil 7.40; Amazonia 0.82 |
| Spanish | 3.36 | 6.64 | Argentina (without Patagonia) 3.17; Cascadia 2.76; Sonora 0.52; Araucanía-Patagonia 0.19 |
| French | 5.58 | 5.58 | France 5.58 |
| German | 4.33 | 4.33 | Germany 2.19; Austro-Bavaria 2.14 |
| Finnish | 3.35 | 3.35 | Finland 3.35 |
| Czech | 3.32 | 3.32 | Czechia 3.32 |
| Slovak | 3.32 | 3.32 | Slovakia 3.32 |
| Croatian | 3.25 | 3.25 | Croatia 3.25 |
| Serbian | 3.23 | 3.23 | Serbia 3.23 |
| Dutch | 3.22 | 3.22 | Netherlands 3.22 |
| Slovene | 3.18 | 3.18 | Slovenia 3.18 |
| Bulgarian | 3.04 | 3.04 | Bulgaria 3.04 |
| Tatar and Bashkir | 0.00 | 3.04 | Idelsk-Uralia 3.04 |
| Latvian | 3.02 | 3.02 | Latvia 3.02 |
| Hungarian | 1.52 | 1.52 | Hungary 1.52 |
| Polish | 1.52 | 1.52 | Poland 1.52 |
| Swedish | 1.38 | 1.38 | Sweden 1.38 |
| Lithuanian | 1.34 | 1.34 | Lithuania 1.34 |
| Belarusian | 0.00 | 1.31 | Belarus 1.31 |
| Estonian | 1.25 | 1.25 | Estonia 1.25 |
| Afrikaans | 0.00 | 1.24 | South Africa 1.24 |
| Norwegian | 1.24 | 1.24 | Norway 1.24 |
| Zulu and other Bantu languages | 0.00 | 1.24 | South Africa 1.24 |
| Romanian | 1.08 | 1.08 | Romania 1.08 |
| Ukrainian | 0.00 | 1.02 | Ukraine 1.02 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.21 | Dagestan 0.21 |
| Chechen | 0.00 | 0.10 | Chechnya 0.10 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.08 | Hawaii 0.08 |
| Kabardian and Balkar | 0.00 | 0.06 | Kabardino-Balkaria 0.06 |
| Ossetian | 0.00 | 0.05 | North Ossetia-Alania 0.05 |
| Ingush | 0.00 | 0.03 | Ingushetia 0.03 |
| Karachay and Circassian languages | 0.00 | 0.03 | Karachay-Cherkessia 0.03 |
| Tuvan | 0.00 | 0.02 | Tuva 0.02 |

**MULTI / UNMAPPED rows in this city:** Idelsk-Uralia 3.040% (MULTI: Russian / Tatar and Bashkir); Cascadia 2.760% (MULTI: English / Spanish); Belarus 1.310% (MULTI: Belarusian / Russian); South Africa 1.240% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Ukraine 1.020% (MULTI: Ukrainian / Russian); Sonora 0.520% (MULTI: English / Spanish); Dagestan 0.210% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Chechnya 0.100% (MULTI: Russian / Chechen); Hawaii 0.076% (MULTI: Hawaiian (the dominant language everywhere) / English); Kabardino-Balkaria 0.061% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.046% (MULTI: Russian / Ossetian); Ingushetia 0.034% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.032% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.023% (MULTI: Russian / Tuvan)

### Utstein

*Census I table counts: robots 609,199, humans 580,839; Census II: robots 384,561, humans 418,082. Share total 100.017%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 20.01 | 23.70 | Australia 6.95; CSA 4.51; Appalachia 2.90; New England 2.37; Cascadia 2.11; United Kingdom 1.63; South Africa 1.12; Midwest Republic 0.90; Colorado 0.68; Sonora 0.40; Hawaii 0.06; Northern Ireland 0.05; Alaska 0.03 |
| French | 8.76 | 8.76 | France 8.76 |
| Portuguese | 7.91 | 7.91 | Brazil 7.12; Amazonia 0.79 |
| German | 6.12 | 6.12 | Germany 3.71; Austro-Bavaria 2.41 |
| Russian | 0.88 | 5.42 | Ukraine 1.74; Kazakhstan 1.45; Belarus 1.35; Russia (core state) 0.88 |
| Finnish | 5.21 | 5.21 | Finland 5.21 |
| Japanese | 5.08 | 5.08 | Japan 5.08 |
| Norwegian | 5.05 | 5.05 | Norway 5.05 |
| Spanish | 1.15 | 3.65 | Cascadia 2.11; Argentina (without Patagonia) 1.08; Sonora 0.40; Araucanía-Patagonia 0.07 |
| Danish | 3.02 | 3.02 | Denmark 3.02 |
| Dutch | 2.93 | 2.93 | Netherlands 2.93 |
| Serbian | 2.65 | 2.65 | Serbia 2.65 |
| Polish | 2.64 | 2.64 | Poland 2.64 |
| Swedish | 2.61 | 2.61 | Sweden 2.61 |
| Bulgarian | 2.48 | 2.48 | Bulgaria 2.48 |
| Czech | 2.43 | 2.43 | Czechia 2.43 |
| Latvian | 2.43 | 2.43 | Latvia 2.43 |
| Romanian | 2.18 | 2.18 | Romania 2.18 |
| Ukrainian | 0.00 | 1.74 | Ukraine 1.74 |
| Hungarian | 1.61 | 1.61 | Hungary 1.61 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Belarusian | 0.00 | 1.35 | Belarus 1.35 |
| Croatian | 1.30 | 1.30 | Croatia 1.30 |
| Lithuanian | 1.30 | 1.30 | Lithuania 1.30 |
| Slovak | 1.22 | 1.22 | Slovakia 1.22 |
| Estonian | 1.17 | 1.17 | Estonia 1.17 |
| Afrikaans | 0.00 | 1.12 | South Africa 1.12 |
| Zulu and other Bantu languages | 0.00 | 1.12 | South Africa 1.12 |
| Slovene | 1.10 | 1.10 | Slovenia 1.10 |
| Icelandic | 0.55 | 0.55 | Iceland 0.55 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.06 | Hawaii 0.06 |

**MULTI / UNMAPPED rows in this city:** Cascadia 2.110% (MULTI: English / Spanish); Ukraine 1.740% (MULTI: Ukrainian / Russian); Kazakhstan 1.450% (MULTI: Kazakh / Russian); Belarus 1.350% (MULTI: Belarusian / Russian); South Africa 1.120% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Sonora 0.400% (MULTI: English / Spanish); Hawaii 0.058% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Cape Adare

*Census I table counts: robots 778,737, humans 773,039; Census II: robots 642,910, humans 443,021. Share total 99.998%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 42.64 | 50.87 | Australia 11.82; CSA 7.91; United Kingdom 5.59; Appalachia 4.43; Cascadia 4.08; New England 3.62; New Zealand 3.06; Demilitarized Zone (s. Ontario, not a nation) 2.31; Philippines 1.99; Malaysia 1.46; Midwest Republic 1.38; Prairie Federation 1.30; Colorado 1.03; Sonora 0.61; Northern Ireland 0.13; Hawaii 0.09; Alaska 0.06 |
| Mandarin | 15.34 | 15.66 | Sinian Federation 11.62; Taiwan 2.91; Manchuria 0.81; Mongolia 0.32 |
| Japanese | 11.52 | 11.52 | Japan 11.52 |
| Indonesian | 9.96 | 10.14 | Indonesia 9.78; West Papua 0.18; Aceh 0.18 |
| Spanish | 3.58 | 8.27 | Cascadia 4.08; Chile 3.08; Sonora 0.61; Araucanía-Patagonia 0.50 |
| Korean | 6.47 | 6.47 | Korea 6.47 |
| Filipino (Tagalog) | 0.00 | 1.99 | Philippines 1.99 |
| French | 1.76 | 1.76 | Quebec 1.76 |
| Chinese (Mandarin and other) | 0.00 | 1.46 | Malaysia 1.46 |
| Malay | 0.00 | 1.46 | Malaysia 1.46 |
| Tamil | 0.00 | 1.46 | Malaysia 1.46 |
| Mongolian | 0.00 | 0.32 | Mongolia 0.32 |
| Acehnese | 0.00 | 0.18 | Aceh 0.18 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.09 | Hawaii 0.09 |

**MULTI / UNMAPPED rows in this city:** Cascadia 4.080% (MULTI: English / Spanish); Philippines 1.990% (MULTI: Filipino (Tagalog) / English); Malaysia 1.460% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Sonora 0.610% (MULTI: English / Spanish); Mongolia 0.320% (MULTI: Mongolian / Mandarin); Aceh 0.180% (MULTI: Acehnese / Indonesian); Hawaii 0.089% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Concordia

*Census I table counts: robots 536,198, humans 531,867; Census II: robots 345,435, humans 325,745. Share total 99.969%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 16.63 | 21.89 | Australia 8.10; New Zealand 3.55; Philippines 2.47; Malaysia 1.84; CSA 1.35; United Kingdom 1.21; Appalachia 0.87; Cascadia 0.75; New England 0.71; Midwest Republic 0.27; Demilitarized Zone (s. Ontario, not a nation) 0.21; Colorado 0.20; Sonora 0.18; Prairie Federation 0.12; Northern Ireland 0.03; Hawaii 0.02; Alaska 0.01 |
| Russian | 5.68 | 14.30 | Belarus 3.56; Russia (core state) 2.94; Idelsk-Uralia 2.72; Kazakhstan 1.45; Siberia 1.08; Donska-Kubania 1.04; Künnarantaiga 0.62; Ukraine 0.43; Dagestan 0.19; Chechnya 0.09; Kabardino-Balkaria 0.05; North Ossetia-Alania 0.04; Ingushetia 0.03; Karachay-Cherkessia 0.03; Tuva 0.02 |
| Korean | 10.03 | 10.03 | Korea 10.03 |
| Japanese | 9.66 | 9.66 | Japan 9.66 |
| Indonesian | 7.83 | 7.97 | Indonesia 7.68; West Papua 0.15; Aceh 0.14 |
| Mandarin | 7.59 | 7.96 | Sinian Federation 4.45; Taiwan 2.86; Manchuria 0.28; Mongolia 0.21; East Turkestan 0.14; Tibet 0.02 |
| Vietnamese | 3.99 | 3.99 | Vietnam 3.99 |
| Belarusian | 0.00 | 3.56 | Belarus 3.56 |
| Spanish | 2.18 | 3.42 | Spain 1.07; México 0.98; Cascadia 0.75; Catalonia 0.23; Sonora 0.18; Yucatán 0.13; Basque Country 0.08 |
| Tatar and Bashkir | 0.00 | 2.72 | Idelsk-Uralia 2.72 |
| Filipino (Tagalog) | 0.00 | 2.47 | Philippines 2.47 |
| French | 2.19 | 2.19 | France 2.03; Quebec 0.16 |
| Chinese (Mandarin and other) | 0.00 | 1.84 | Malaysia 1.84 |
| Malay | 0.00 | 1.84 | Malaysia 1.84 |
| Tamil | 0.00 | 1.84 | Malaysia 1.84 |
| Serbian | 1.50 | 1.50 | Serbia 1.50 |
| Thai | 1.45 | 1.49 | Thailand 1.45; Patani 0.04 |
| Estonian | 1.46 | 1.46 | Estonia 1.46 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Hungarian | 1.42 | 1.42 | Hungary 1.42 |
| Dutch | 1.40 | 1.40 | Netherlands 1.40 |
| Croatian | 1.36 | 1.36 | Croatia 1.36 |
| Finnish | 1.36 | 1.36 | Finland 1.36 |
| Czech | 1.30 | 1.30 | Czechia 1.30 |
| Norwegian | 1.30 | 1.30 | Norway 1.30 |
| Polish | 1.24 | 1.24 | Poland 1.24 |
| Lithuanian | 0.79 | 0.79 | Lithuania 0.79 |
| Latvian | 0.76 | 0.76 | Latvia 0.76 |
| Swedish | 0.71 | 0.71 | Sweden 0.71 |
| Italian | 0.71 | 0.71 | Magna Lombardia 0.40; Meridia 0.25; Sicilia (autonomous zone within Meridia) 0.06 |
| Bulgarian | 0.68 | 0.68 | Bulgaria 0.68 |
| Slovak | 0.62 | 0.62 | Slovakia 0.62 |
| Romanian | 0.58 | 0.58 | Romania 0.58 |
| German | 0.55 | 0.55 | Germany 0.46; Austro-Bavaria 0.09 |
| Ukrainian | 0.00 | 0.43 | Ukraine 0.43 |
| Slovene | 0.26 | 0.26 | Slovenia 0.26 |
| Catalan | 0.00 | 0.23 | Catalonia 0.23 |
| Mongolian | 0.00 | 0.21 | Mongolia 0.21 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.19 | Dagestan 0.19 |
| Acehnese | 0.00 | 0.14 | Aceh 0.14 |
| Uyghur | 0.00 | 0.14 | East Turkestan 0.14 |
| Chechen | 0.00 | 0.09 | Chechnya 0.09 |
| Basque | 0.00 | 0.08 | Basque Country 0.08 |
| Kabardian and Balkar | 0.00 | 0.05 | Kabardino-Balkaria 0.05 |
| Patani Malay | 0.00 | 0.04 | Patani 0.04 |
| Ossetian | 0.00 | 0.04 | North Ossetia-Alania 0.04 |
| Ingush | 0.00 | 0.03 | Ingushetia 0.03 |
| Karachay and Circassian languages | 0.00 | 0.03 | Karachay-Cherkessia 0.03 |
| Tuvan | 0.00 | 0.02 | Tuva 0.02 |
| Tibetan | 0.00 | 0.02 | Tibet 0.02 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.02 | Hawaii 0.02 |

**MULTI / UNMAPPED rows in this city:** Belarus 3.560% (MULTI: Belarusian / Russian); Idelsk-Uralia 2.720% (MULTI: Russian / Tatar and Bashkir); Philippines 2.470% (MULTI: Filipino (Tagalog) / English); Malaysia 1.840% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Kazakhstan 1.450% (MULTI: Kazakh / Russian); Cascadia 0.750% (MULTI: English / Spanish); Ukraine 0.430% (MULTI: Ukrainian / Russian); Catalonia 0.230% (MULTI: Catalan / Spanish); Mongolia 0.210% (MULTI: Mongolian / Mandarin); Dagestan 0.190% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Sonora 0.180% (MULTI: English / Spanish); Aceh 0.140% (MULTI: Acehnese / Indonesian); East Turkestan 0.140% (MULTI: Uyghur / Mandarin); Chechnya 0.092% (MULTI: Russian / Chechen); Basque Country 0.083% (MULTI: Basque / Spanish); Kabardino-Balkaria 0.054% (MULTI: Russian / Kabardian and Balkar); Patani 0.042% (MULTI: Patani Malay / Thai); North Ossetia-Alania 0.041% (MULTI: Russian / Ossetian); Ingushetia 0.031% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.029% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.021% (MULTI: Russian / Tuvan); Tibet 0.019% (MULTI: Tibetan / Mandarin); Hawaii 0.018% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Denison

*Census I table counts: robots 486,742, humans 471,598; Census II: robots 357,593, humans 301,762. Share total 99.968%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 33.23 | 43.63 | CSA 9.33; Australia 6.75; Appalachia 6.25; New England 4.26; Cascadia 3.79; New Zealand 3.75; Philippines 3.48; Malaysia 2.32; Midwest Republic 1.62; Colorado 1.22; Sonora 0.71; Hawaii 0.10; Alaska 0.05 |
| Mandarin | 17.02 | 17.48 | Sinian Federation 13.23; Taiwan 2.90; Manchuria 0.89; Mongolia 0.46 |
| Korean | 13.95 | 13.95 | Korea 13.95 |
| Indonesian | 11.60 | 11.80 | Indonesia 11.39; West Papua 0.21; Aceh 0.20 |
| Japanese | 8.16 | 8.16 | Japan 8.16 |
| Spanish | 0.00 | 4.50 | Cascadia 3.79; Sonora 0.71 |
| Vietnamese | 3.56 | 3.56 | Vietnam 3.56 |
| Filipino (Tagalog) | 0.00 | 3.48 | Philippines 3.48 |
| Chinese (Mandarin and other) | 0.00 | 2.32 | Malaysia 2.32 |
| Malay | 0.00 | 2.32 | Malaysia 2.32 |
| Tamil | 0.00 | 2.32 | Malaysia 2.32 |
| Thai | 1.35 | 1.39 | Thailand 1.35; Patani 0.04 |
| Mongolian | 0.00 | 0.46 | Mongolia 0.46 |
| Acehnese | 0.00 | 0.20 | Aceh 0.20 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.10 | Hawaii 0.10 |
| Patani Malay | 0.00 | 0.04 | Patani 0.04 |

**MULTI / UNMAPPED rows in this city:** Cascadia 3.790% (MULTI: English / Spanish); Philippines 3.480% (MULTI: Filipino (Tagalog) / English); Malaysia 2.320% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Sonora 0.710% (MULTI: English / Spanish); Mongolia 0.460% (MULTI: Mongolian / Mandarin); Aceh 0.200% (MULTI: Acehnese / Indonesian); Hawaii 0.100% (MULTI: Hawaiian (the dominant language everywhere) / English); Patani 0.039% (MULTI: Patani Malay / Thai)

### Dumont d'Urville

*Census I table counts: robots 206,807, humans 201,194; Census II: robots 159,635, humans 121,170. Share total 99.994%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 33.75 | 42.61 | Australia 12.55; CSA 7.73; Appalachia 4.00; New Zealand 3.98; New England 3.27; Philippines 3.25; Cascadia 2.91; Malaysia 2.07; Midwest Republic 1.24; Colorado 0.94; Sonora 0.55; Hawaii 0.08; Alaska 0.04 |
| Mandarin | 17.38 | 18.36 | Sinian Federation 13.56; Taiwan 2.90; Manchuria 0.92; Mongolia 0.49; East Turkestan 0.43; Tibet 0.06 |
| French | 13.37 | 13.37 | France 13.37 |
| Japanese | 13.28 | 13.28 | Japan 13.28 |
| Indonesian | 6.48 | 6.59 | Indonesia 6.37; West Papua 0.11; Aceh 0.11 |
| Vietnamese | 3.87 | 3.87 | Vietnam 3.87 |
| Spanish | 0.00 | 3.46 | Cascadia 2.91; Sonora 0.55 |
| Filipino (Tagalog) | 0.00 | 3.25 | Philippines 3.25 |
| Chinese (Mandarin and other) | 0.00 | 2.07 | Malaysia 2.07 |
| Malay | 0.00 | 2.07 | Malaysia 2.07 |
| Tamil | 0.00 | 2.07 | Malaysia 2.07 |
| Korean | 1.78 | 1.78 | Korea 1.78 |
| Mongolian | 0.00 | 0.49 | Mongolia 0.49 |
| Uyghur | 0.00 | 0.43 | East Turkestan 0.43 |
| Thai | 0.13 | 0.13 | Thailand 0.13; Patani 0.00 |
| Acehnese | 0.00 | 0.11 | Aceh 0.11 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.08 | Hawaii 0.08 |
| Tibetan | 0.00 | 0.06 | Tibet 0.06 |
| Patani Malay | 0.00 | 0.00 | Patani 0.00 |

**MULTI / UNMAPPED rows in this city:** Philippines 3.250% (MULTI: Filipino (Tagalog) / English); Cascadia 2.910% (MULTI: English / Spanish); Malaysia 2.070% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Sonora 0.550% (MULTI: English / Spanish); Mongolia 0.490% (MULTI: Mongolian / Mandarin); East Turkestan 0.430% (MULTI: Uyghur / Mandarin); Aceh 0.110% (MULTI: Acehnese / Indonesian); Hawaii 0.081% (MULTI: Hawaiian (the dominant language everywhere) / English); Tibet 0.061% (MULTI: Tibetan / Mandarin); Patani 0.004% (MULTI: Patani Malay / Thai)

### Fort McMurdo

*Census I table counts: robots 223,120, humans 222,190; Census II: robots 164,621, humans 173,548. Share total 99.987%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 29.56 | 38.53 | CSA 8.40; Appalachia 4.31; United Kingdom 3.98; Cascadia 3.60; New England 3.53; Malaysia 3.17; New Zealand 3.06; Australia 1.84; Philippines 1.52; Midwest Republic 1.34; Demilitarized Zone (s. Ontario, not a nation) 1.24; Colorado 1.01; Prairie Federation 0.69; Sonora 0.59; Northern Ireland 0.11; Hawaii 0.09; Alaska 0.05 |
| Mandarin | 13.77 | 14.09 | Sinian Federation 10.11; Taiwan 2.91; Manchuria 0.75; Mongolia 0.32 |
| French | 12.59 | 12.59 | France 11.65; Quebec 0.94 |
| German | 12.16 | 12.16 | Germany 10.54; Austro-Bavaria 1.62 |
| Japanese | 10.87 | 10.87 | Japan 10.87 |
| Spanish | 3.39 | 7.58 | Cascadia 3.60; Chile 2.92; Sonora 0.59; Araucanía-Patagonia 0.47 |
| Italian | 4.69 | 4.69 | Magna Lombardia 2.67; Meridia 1.64; Sicilia (autonomous zone within Meridia) 0.38 |
| Chinese (Mandarin and other) | 0.00 | 3.17 | Malaysia 3.17 |
| Malay | 0.00 | 3.17 | Malaysia 3.17 |
| Tamil | 0.00 | 3.17 | Malaysia 3.17 |
| Korean | 1.93 | 1.93 | Korea 1.93 |
| Indonesian | 1.71 | 1.74 | Indonesia 1.67; West Papua 0.04; Aceh 0.03 |
| Filipino (Tagalog) | 0.00 | 1.52 | Philippines 1.52 |
| Mongolian | 0.00 | 0.32 | Mongolia 0.32 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.09 | Hawaii 0.09 |
| Acehnese | 0.00 | 0.03 | Aceh 0.03 |

**MULTI / UNMAPPED rows in this city:** Cascadia 3.600% (MULTI: English / Spanish); Malaysia 3.170% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Philippines 1.520% (MULTI: Filipino (Tagalog) / English); Sonora 0.590% (MULTI: English / Spanish); Mongolia 0.320% (MULTI: Mongolian / Mandarin); Hawaii 0.087% (MULTI: Hawaiian (the dominant language everywhere) / English); Aceh 0.034% (MULTI: Acehnese / Indonesian)

### Janbogo

*Census I table counts: robots 689,019, humans 673,610; Census II: robots 486,208, humans 507,242. Share total 100.039%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 31.28 | 39.70 | Australia 11.79; CSA 7.02; Appalachia 3.66; Cascadia 3.18; Malaysia 3.00; New England 2.99; Philippines 1.67; New Zealand 1.59; Demilitarized Zone (s. Ontario, not a nation) 1.40; Midwest Republic 1.14; Colorado 0.85; Prairie Federation 0.79; Sonora 0.50; Hawaii 0.07; Alaska 0.04 |
| Mandarin | 14.37 | 14.71 | Sinian Federation 10.67; Taiwan 2.91; Manchuria 0.79; Mongolia 0.34 |
| Korean | 12.49 | 12.49 | Korea 12.49 |
| Indonesian | 10.23 | 10.40 | Indonesia 10.06; West Papua 0.17; Aceh 0.17 |
| Italian | 9.91 | 9.91 | Magna Lombardia 6.14; Meridia 3.06; Sicilia (autonomous zone within Meridia) 0.71 |
| Spanish | 3.09 | 6.77 | Cascadia 3.18; Chile 2.66; Sonora 0.50; Araucanía-Patagonia 0.43 |
| German | 4.45 | 4.45 | Germany 3.73; Austro-Bavaria 0.72 |
| Japanese | 4.22 | 4.22 | Japan 4.22 |
| Chinese (Mandarin and other) | 0.00 | 3.00 | Malaysia 3.00 |
| Malay | 0.00 | 3.00 | Malaysia 3.00 |
| Tamil | 0.00 | 3.00 | Malaysia 3.00 |
| Filipino (Tagalog) | 0.00 | 1.67 | Philippines 1.67 |
| French | 1.07 | 1.07 | Quebec 1.07 |
| Mongolian | 0.00 | 0.34 | Mongolia 0.34 |
| Acehnese | 0.00 | 0.17 | Aceh 0.17 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.07 | Hawaii 0.07 |

**MULTI / UNMAPPED rows in this city:** Cascadia 3.180% (MULTI: English / Spanish); Malaysia 3.000% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Philippines 1.670% (MULTI: Filipino (Tagalog) / English); Sonora 0.500% (MULTI: English / Spanish); Mongolia 0.340% (MULTI: Mongolian / Mandarin); Aceh 0.170% (MULTI: Acehnese / Indonesian); Hawaii 0.074% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Scott

*Census I table counts: robots 196,194, humans 189,817; Census II: robots 160,252, humans 153,382. Share total 100.009%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 46.85 | 54.67 | United Kingdom 11.45; Australia 10.29; CSA 7.99; Appalachia 4.50; Cascadia 3.93; New England 3.68; New Zealand 3.37; Demilitarized Zone (s. Ontario, not a nation) 1.77; Malaysia 1.67; Philippines 1.51; Midwest Republic 1.40; Colorado 1.05; Prairie Federation 1.00; Sonora 0.62; Northern Ireland 0.29; Hawaii 0.09; Alaska 0.06 |
| Mandarin | 15.04 | 15.36 | Sinian Federation 11.43; Taiwan 2.91; Manchuria 0.70; Mongolia 0.32 |
| Japanese | 11.80 | 11.80 | Japan 11.80 |
| Spanish | 3.53 | 8.08 | Cascadia 3.93; Chile 3.04; Sonora 0.62; Araucanía-Patagonia 0.49 |
| Korean | 7.34 | 7.34 | Korea 7.34 |
| Indonesian | 5.87 | 5.96 | Indonesia 5.77; West Papua 0.10; Aceh 0.09 |
| Chinese (Mandarin and other) | 0.00 | 1.67 | Malaysia 1.67 |
| Malay | 0.00 | 1.67 | Malaysia 1.67 |
| Tamil | 0.00 | 1.67 | Malaysia 1.67 |
| Filipino (Tagalog) | 0.00 | 1.51 | Philippines 1.51 |
| French | 1.35 | 1.35 | Quebec 1.35 |
| Mongolian | 0.00 | 0.32 | Mongolia 0.32 |
| Acehnese | 0.00 | 0.09 | Aceh 0.09 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.09 | Hawaii 0.09 |

**MULTI / UNMAPPED rows in this city:** Cascadia 3.930% (MULTI: English / Spanish); Malaysia 1.670% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Philippines 1.510% (MULTI: Filipino (Tagalog) / English); Sonora 0.620% (MULTI: English / Spanish); Mongolia 0.320% (MULTI: Mongolian / Mandarin); Aceh 0.094% (MULTI: Acehnese / Indonesian); Hawaii 0.091% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Zukelli

*Census I table counts: robots 656,116, humans 654,653; Census II: robots 513,107, humans 460,432. Share total 99.971%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 37.41 | 47.24 | Australia 11.75; CSA 7.75; Cascadia 4.12; Appalachia 3.87; Demilitarized Zone (s. Ontario, not a nation) 3.50; Malaysia 3.29; New Zealand 3.23; New England 3.17; Prairie Federation 1.97; Philippines 1.81; Midwest Republic 1.20; Colorado 0.91; Sonora 0.53; Hawaii 0.08; Alaska 0.06 |
| Mandarin | 16.20 | 16.57 | Sinian Federation 12.38; Taiwan 2.91; Manchuria 0.91; Mongolia 0.37 |
| Korean | 14.09 | 14.09 | Korea 14.09 |
| Indonesian | 7.08 | 7.19 | Indonesia 6.96; West Papua 0.12; Aceh 0.11 |
| Spanish | 1.74 | 6.39 | Cascadia 4.12; Chile 1.50; Sonora 0.53; Araucanía-Patagonia 0.24 |
| Italian | 5.97 | 5.97 | Magna Lombardia 3.40; Meridia 2.09; Sicilia (autonomous zone within Meridia) 0.48 |
| Japanese | 4.49 | 4.49 | Japan 4.49 |
| Chinese (Mandarin and other) | 0.00 | 3.29 | Malaysia 3.29 |
| Malay | 0.00 | 3.29 | Malaysia 3.29 |
| Tamil | 0.00 | 3.29 | Malaysia 3.29 |
| French | 2.68 | 2.68 | Quebec 2.68 |
| Filipino (Tagalog) | 0.00 | 1.81 | Philippines 1.81 |
| Mongolian | 0.00 | 0.37 | Mongolia 0.37 |
| Acehnese | 0.00 | 0.11 | Aceh 0.11 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.08 | Hawaii 0.08 |

**MULTI / UNMAPPED rows in this city:** Cascadia 4.120% (MULTI: English / Spanish); Malaysia 3.290% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Philippines 1.810% (MULTI: Filipino (Tagalog) / English); Sonora 0.530% (MULTI: English / Spanish); Mongolia 0.370% (MULTI: Mongolian / Mandarin); Aceh 0.110% (MULTI: Acehnese / Indonesian); Hawaii 0.078% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Dome Fuji

*Census I table counts: robots 80,120 (robots column only; no human column in this table). Share total 99.962%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 19.09 | 25.75 | Australia 6.05; CSA 3.50; United Kingdom 2.34; Appalachia 2.25; Cascadia 1.93; Malaysia 1.85; New England 1.84; Philippines 1.65; New Zealand 0.82; South Africa 0.77; Midwest Republic 0.70; Demilitarized Zone (s. Ontario, not a nation) 0.62; Colorado 0.53; Sonora 0.41; Prairie Federation 0.35; Northern Ireland 0.07; Hawaii 0.04; Alaska 0.03 |
| Spanish | 5.58 | 8.33 | Cascadia 1.93; México 1.47; Spain 1.41; Chile 0.82; Argentina (without Patagonia) 0.77; Uruguay 0.74; Sonora 0.41; Catalonia 0.30; Yucatán 0.19; Araucanía-Patagonia 0.18; Basque Country 0.11 |
| French | 6.95 | 6.95 | France 6.48; Quebec 0.47 |
| Indonesian | 6.31 | 6.42 | Indonesia 6.20; West Papua 0.11; Aceh 0.11 |
| German | 6.35 | 6.35 | Germany 3.91; Austro-Bavaria 2.44 |
| Russian | 1.65 | 6.24 | Belarus 1.77; Kazakhstan 1.45; Russia (core state) 0.97; Idelsk-Uralia 0.67; Ukraine 0.59; Siberia 0.27; Donska-Kubania 0.26; Künnarantaiga 0.15; Dagestan 0.05; Chechnya 0.02; Kabardino-Balkaria 0.01; North Ossetia-Alania 0.01; Ingushetia 0.01; Karachay-Cherkessia 0.01; Tuva 0.01 |
| Korean | 5.60 | 5.60 | Korea 5.60 |
| Mandarin | 5.29 | 5.50 | Sinian Federation 5.29; East Turkestan 0.18; Tibet 0.03 |
| Portuguese | 3.06 | 3.06 | Brazil 2.76; Amazonia 0.30 |
| Japanese | 2.74 | 2.74 | Japan 2.74 |
| Dutch | 2.31 | 2.31 | Netherlands 2.31 |
| Hungarian | 1.93 | 1.93 | Hungary 1.93 |
| Chinese (Mandarin and other) | 0.00 | 1.85 | Malaysia 1.85 |
| Malay | 0.00 | 1.85 | Malaysia 1.85 |
| Tamil | 0.00 | 1.85 | Malaysia 1.85 |
| Slovene | 1.81 | 1.81 | Slovenia 1.81 |
| Belarusian | 0.00 | 1.77 | Belarus 1.77 |
| Croatian | 1.76 | 1.76 | Croatia 1.76 |
| Serbian | 1.73 | 1.73 | Serbia 1.73 |
| Czech | 1.68 | 1.68 | Czechia 1.68 |
| Latvian | 1.67 | 1.67 | Latvia 1.67 |
| Filipino (Tagalog) | 0.00 | 1.65 | Philippines 1.65 |
| Estonian | 1.63 | 1.63 | Estonia 1.63 |
| Norwegian | 1.61 | 1.61 | Norway 1.61 |
| Romanian | 1.58 | 1.58 | Romania 1.58 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Finnish | 0.95 | 0.95 | Finland 0.95 |
| Slovak | 0.93 | 0.93 | Slovakia 0.93 |
| Bulgarian | 0.92 | 0.92 | Bulgaria 0.92 |
| Swedish | 0.91 | 0.91 | Sweden 0.91 |
| Vietnamese | 0.91 | 0.91 | Vietnam 0.91 |
| Thai | 0.79 | 0.81 | Thailand 0.79; Patani 0.02 |
| Afrikaans | 0.00 | 0.77 | South Africa 0.77 |
| Zulu and other Bantu languages | 0.00 | 0.77 | South Africa 0.77 |
| Italian | 0.75 | 0.75 | Magna Lombardia 0.43; Meridia 0.26; Sicilia (autonomous zone within Meridia) 0.06 |
| Polish | 0.74 | 0.74 | Poland 0.74 |
| Lithuanian | 0.73 | 0.73 | Lithuania 0.73 |
| Tatar and Bashkir | 0.00 | 0.67 | Idelsk-Uralia 0.67 |
| Ukrainian | 0.00 | 0.59 | Ukraine 0.59 |
| Catalan | 0.00 | 0.30 | Catalonia 0.30 |
| Uyghur | 0.00 | 0.18 | East Turkestan 0.18 |
| Acehnese | 0.00 | 0.11 | Aceh 0.11 |
| Basque | 0.00 | 0.11 | Basque Country 0.11 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.05 | Dagestan 0.05 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.04 | Hawaii 0.04 |
| Tibetan | 0.00 | 0.03 | Tibet 0.03 |
| Chechen | 0.00 | 0.02 | Chechnya 0.02 |
| Patani Malay | 0.00 | 0.02 | Patani 0.02 |
| Kabardian and Balkar | 0.00 | 0.01 | Kabardino-Balkaria 0.01 |
| Ossetian | 0.00 | 0.01 | North Ossetia-Alania 0.01 |
| Ingush | 0.00 | 0.01 | Ingushetia 0.01 |
| Karachay and Circassian languages | 0.00 | 0.01 | Karachay-Cherkessia 0.01 |
| Tuvan | 0.00 | 0.01 | Tuva 0.01 |

**MULTI / UNMAPPED rows in this city:** Cascadia 1.930% (MULTI: English / Spanish); Malaysia 1.850% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Belarus 1.770% (MULTI: Belarusian / Russian); Philippines 1.650% (MULTI: Filipino (Tagalog) / English); Kazakhstan 1.450% (MULTI: Kazakh / Russian); South Africa 0.770% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Idelsk-Uralia 0.670% (MULTI: Russian / Tatar and Bashkir); Ukraine 0.590% (MULTI: Ukrainian / Russian); Sonora 0.410% (MULTI: English / Spanish); Catalonia 0.300% (MULTI: Catalan / Spanish); East Turkestan 0.180% (MULTI: Uyghur / Mandarin); Basque Country 0.110% (MULTI: Basque / Spanish); Aceh 0.110% (MULTI: Acehnese / Indonesian); Dagestan 0.047% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Hawaii 0.045% (MULTI: Hawaiian (the dominant language everywhere) / English); Tibet 0.026% (MULTI: Tibetan / Mandarin); Patani 0.023% (MULTI: Patani Malay / Thai); Chechnya 0.023% (MULTI: Russian / Chechen); Kabardino-Balkaria 0.014% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.010% (MULTI: Russian / Ossetian); Ingushetia 0.008% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.007% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.005% (MULTI: Russian / Tuvan)

### Mawson

*Census I table counts: robots 762,053, humans 736,799; Census II: robots 544,326, humans 443,999. Share total 99.975%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 13.16 | 16.15 | Australia 9.38; United Kingdom 3.54; South Africa 2.99; Northern Ireland 0.24 |
| Russian | 3.35 | 11.68 | Kazakhstan 4.80; Russia (core state) 3.35; Belarus 2.84; Ukraine 0.69 |
| Mandarin | 8.94 | 9.66 | Sinian Federation 8.94; Mongolia 0.37; East Turkestan 0.31; Tibet 0.04 |
| Indonesian | 8.73 | 8.88 | Indonesia 8.57; West Papua 0.16; Aceh 0.15 |
| Japanese | 8.46 | 8.46 | Japan 8.46 |
| French | 5.98 | 5.98 | France 5.98 |
| Korean | 5.50 | 5.50 | Korea 5.50 |
| Kazakh | 0.00 | 4.80 | Kazakhstan 4.80 |
| German | 3.49 | 3.49 | Austro-Bavaria 1.98; Germany 1.51 |
| Estonian | 3.07 | 3.07 | Estonia 3.07 |
| Afrikaans | 0.00 | 2.99 | South Africa 2.99 |
| Zulu and other Bantu languages | 0.00 | 2.99 | South Africa 2.99 |
| Norwegian | 2.95 | 2.95 | Norway 2.95 |
| Vietnamese | 2.89 | 2.89 | Vietnam 2.89 |
| Thai | 2.79 | 2.87 | Thailand 2.79; Patani 0.08 |
| Belarusian | 0.00 | 2.84 | Belarus 2.84 |
| Dutch | 2.83 | 2.83 | Netherlands 2.83 |
| Slovene | 2.62 | 2.62 | Slovenia 2.62 |
| Bulgarian | 2.59 | 2.59 | Bulgaria 2.59 |
| Czech | 1.52 | 1.52 | Czechia 1.52 |
| Slovak | 1.50 | 1.50 | Slovakia 1.50 |
| Hungarian | 1.40 | 1.40 | Hungary 1.40 |
| Lithuanian | 1.30 | 1.30 | Lithuania 1.30 |
| Polish | 1.23 | 1.23 | Poland 1.23 |
| Croatian | 1.17 | 1.17 | Croatia 1.17 |
| Latvian | 1.12 | 1.12 | Latvia 1.12 |
| Romanian | 1.11 | 1.11 | Romania 1.11 |
| Ukrainian | 0.00 | 0.69 | Ukraine 0.69 |
| Mongolian | 0.00 | 0.37 | Mongolia 0.37 |
| Uyghur | 0.00 | 0.31 | East Turkestan 0.31 |
| Acehnese | 0.00 | 0.15 | Aceh 0.15 |
| Patani Malay | 0.00 | 0.08 | Patani 0.08 |
| Tibetan | 0.00 | 0.04 | Tibet 0.04 |

**MULTI / UNMAPPED rows in this city:** Kazakhstan 4.800% (MULTI: Kazakh / Russian); South Africa 2.990% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Belarus 2.840% (MULTI: Belarusian / Russian); Ukraine 0.690% (MULTI: Ukrainian / Russian); Mongolia 0.370% (MULTI: Mongolian / Mandarin); East Turkestan 0.310% (MULTI: Uyghur / Mandarin); Aceh 0.150% (MULTI: Acehnese / Indonesian); Patani 0.082% (MULTI: Patani Malay / Thai); Tibet 0.043% (MULTI: Tibetan / Mandarin)

### Temirotkel

*Census I table counts: robots 132,020, humans 93,356; Census II: robots 79,758, humans 85,199. Share total 100.004%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 18.36 | 19.85 | Australia 9.37; United Kingdom 8.78; South Africa 1.49; Northern Ireland 0.21 |
| German | 10.78 | 10.78 | Germany 7.81; Austro-Bavaria 2.97 |
| Indonesian | 9.51 | 9.67 | Indonesia 9.34; West Papua 0.17; Aceh 0.16 |
| Russian | 0.50 | 9.32 | Kazakhstan 5.13; Belarus 2.70; Ukraine 0.99; Russia (core state) 0.50 |
| Mandarin | 5.91 | 6.26 | Sinian Federation 5.91; East Turkestan 0.31; Tibet 0.04 |
| Korean | 5.73 | 5.73 | Korea 5.73 |
| French | 5.66 | 5.66 | France 5.66 |
| Kazakh | 0.00 | 5.13 | Kazakhstan 5.13 |
| Serbian | 3.18 | 3.18 | Serbia 3.18 |
| Dutch | 3.03 | 3.03 | Netherlands 3.03 |
| Slovene | 3.01 | 3.01 | Slovenia 3.01 |
| Croatian | 3.00 | 3.00 | Croatia 3.00 |
| Lithuanian | 2.71 | 2.71 | Lithuania 2.71 |
| Norwegian | 2.71 | 2.71 | Norway 2.71 |
| Belarusian | 0.00 | 2.70 | Belarus 2.70 |
| Latvian | 2.67 | 2.67 | Latvia 2.67 |
| Japanese | 2.62 | 2.62 | Japan 2.62 |
| Romanian | 2.44 | 2.44 | Romania 2.44 |
| Hungarian | 1.77 | 1.77 | Hungary 1.77 |
| Czech | 1.51 | 1.51 | Czechia 1.51 |
| Afrikaans | 0.00 | 1.49 | South Africa 1.49 |
| Zulu and other Bantu languages | 0.00 | 1.49 | South Africa 1.49 |
| Bulgarian | 1.20 | 1.20 | Bulgaria 1.20 |
| Polish | 1.19 | 1.19 | Poland 1.19 |
| Estonian | 1.08 | 1.08 | Estonia 1.08 |
| Ukrainian | 0.00 | 0.99 | Ukraine 0.99 |
| Slovak | 0.61 | 0.61 | Slovakia 0.61 |
| Uyghur | 0.00 | 0.31 | East Turkestan 0.31 |
| Acehnese | 0.00 | 0.16 | Aceh 0.16 |
| Tibetan | 0.00 | 0.04 | Tibet 0.04 |

**MULTI / UNMAPPED rows in this city:** Kazakhstan 5.130% (MULTI: Kazakh / Russian); Belarus 2.700% (MULTI: Belarusian / Russian); South Africa 1.490% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Ukraine 0.990% (MULTI: Ukrainian / Russian); East Turkestan 0.310% (MULTI: Uyghur / Mandarin); Aceh 0.160% (MULTI: Acehnese / Indonesian); Tibet 0.044% (MULTI: Tibetan / Mandarin)

### Ariun Nuur

*Census I table counts: robots 284,693, humans 156,685. Share total 99.990%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 37.49 | 44.27 | CSA 8.74; Australia 6.14; Cascadia 5.90; Appalachia 5.61; Demilitarized Zone (s. Ontario, not a nation) 4.89; New England 4.59; Prairie Federation 2.75; Midwest Republic 1.74; New Zealand 1.63; Colorado 1.31; Sonora 0.77; Hawaii 0.11; Alaska 0.09 |
| Japanese | 15.97 | 15.97 | Japan 15.97 |
| Indonesian | 12.65 | 12.91 | Indonesia 12.39; West Papua 0.26; Aceh 0.26 |
| Spanish | 4.73 | 11.40 | Cascadia 5.90; Chile 4.07; Sonora 0.77; Araucanía-Patagonia 0.66 |
| Mandarin | 2.86 | 7.08 | Mongolia 4.22; Taiwan 2.86 |
| Korean | 6.16 | 6.16 | Korea 6.16 |
| Russian | 3.68 | 5.13 | Künnarantaiga 3.68; Kazakhstan 1.45 |
| Mongolian | 0.00 | 4.22 | Mongolia 4.22 |
| French | 3.74 | 3.74 | Quebec 3.74 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Acehnese | 0.00 | 0.26 | Aceh 0.26 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.11 | Hawaii 0.11 |

**MULTI / UNMAPPED rows in this city:** Cascadia 5.900% (MULTI: English / Spanish); Mongolia 4.220% (MULTI: Mongolian / Mandarin); Kazakhstan 1.450% (MULTI: Kazakh / Russian); Sonora 0.770% (MULTI: English / Spanish); Aceh 0.260% (MULTI: Acehnese / Indonesian); Hawaii 0.110% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Casey

*Census I table counts: robots 786,985, humans 760,865; Census II: robots 624,310, humans 453,600. Share total 100.013%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 31.46 | 40.11 | Australia 10.23; CSA 7.85; Appalachia 4.30; New England 3.52; New Zealand 3.17; Philippines 3.16; Cascadia 3.13; Malaysia 1.68; Midwest Republic 1.34; Colorado 1.01; Sonora 0.59; Hawaii 0.09; Alaska 0.04 |
| Mandarin | 12.88 | 13.67 | Sinian Federation 9.35; Taiwan 2.86; Manchuria 0.67; Mongolia 0.40; East Turkestan 0.34; Tibet 0.05 |
| Korean | 11.95 | 11.95 | Korea 11.95 |
| French | 11.11 | 11.11 | France 11.11 |
| Russian | 3.64 | 7.21 | Idelsk-Uralia 1.81; Russia (core state) 1.81; Kazakhstan 1.45; Siberia 0.72; Donska-Kubania 0.69; Künnarantaiga 0.42; Dagestan 0.13; Chechnya 0.06; Kabardino-Balkaria 0.04; North Ossetia-Alania 0.03; Ingushetia 0.02; Karachay-Cherkessia 0.02; Tuva 0.01 |
| Japanese | 6.18 | 6.18 | Japan 6.18 |
| Indonesian | 5.58 | 5.67 | Indonesia 5.48; West Papua 0.10; Aceh 0.09 |
| Spanish | 0.00 | 3.72 | Cascadia 3.13; Sonora 0.59 |
| Filipino (Tagalog) | 0.00 | 3.16 | Philippines 3.16 |
| Vietnamese | 3.03 | 3.03 | Vietnam 3.03 |
| Tatar and Bashkir | 0.00 | 1.81 | Idelsk-Uralia 1.81 |
| Chinese (Mandarin and other) | 0.00 | 1.68 | Malaysia 1.68 |
| Malay | 0.00 | 1.68 | Malaysia 1.68 |
| Tamil | 0.00 | 1.68 | Malaysia 1.68 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Thai | 1.04 | 1.07 | Thailand 1.04; Patani 0.03 |
| Mongolian | 0.00 | 0.40 | Mongolia 0.40 |
| Uyghur | 0.00 | 0.34 | East Turkestan 0.34 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.13 | Dagestan 0.13 |
| Acehnese | 0.00 | 0.09 | Aceh 0.09 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.09 | Hawaii 0.09 |
| Chechen | 0.00 | 0.06 | Chechnya 0.06 |
| Tibetan | 0.00 | 0.05 | Tibet 0.05 |
| Kabardian and Balkar | 0.00 | 0.04 | Kabardino-Balkaria 0.04 |
| Patani Malay | 0.00 | 0.03 | Patani 0.03 |
| Ossetian | 0.00 | 0.03 | North Ossetia-Alania 0.03 |
| Finnish | 0.02 | 0.02 | Finland 0.02 |
| Ingush | 0.00 | 0.02 | Ingushetia 0.02 |
| Karachay and Circassian languages | 0.00 | 0.02 | Karachay-Cherkessia 0.02 |
| Tuvan | 0.00 | 0.01 | Tuva 0.01 |

**MULTI / UNMAPPED rows in this city:** Philippines 3.160% (MULTI: Filipino (Tagalog) / English); Cascadia 3.130% (MULTI: English / Spanish); Idelsk-Uralia 1.810% (MULTI: Russian / Tatar and Bashkir); Malaysia 1.680% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Kazakhstan 1.450% (MULTI: Kazakh / Russian); Sonora 0.590% (MULTI: English / Spanish); Mongolia 0.400% (MULTI: Mongolian / Mandarin); East Turkestan 0.340% (MULTI: Uyghur / Mandarin); Dagestan 0.130% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Aceh 0.092% (MULTI: Acehnese / Indonesian); Hawaii 0.087% (MULTI: Hawaiian (the dominant language everywhere) / English); Chechnya 0.061% (MULTI: Russian / Chechen); Tibet 0.047% (MULTI: Tibetan / Mandarin); Kabardino-Balkaria 0.036% (MULTI: Russian / Kabardian and Balkar); Patani 0.031% (MULTI: Patani Malay / Thai); North Ossetia-Alania 0.028% (MULTI: Russian / Ossetian); Ingushetia 0.021% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.019% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.014% (MULTI: Russian / Tuvan)

### Davis

*Census I table counts: robots 619,764, humans 590,668; Census II: robots 363,374, humans 454,101. Share total 100.004%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 17.02 | 25.78 | United Kingdom 9.36; Australia 5.74; Philippines 3.06; Malaysia 2.95; South Africa 2.75; New Zealand 1.69; Northern Ireland 0.23 |
| Mandarin | 13.29 | 14.08 | Sinian Federation 9.72; Taiwan 2.86; Manchuria 0.71; Mongolia 0.40; East Turkestan 0.34; Tibet 0.05 |
| Russian | 4.46 | 11.61 | Russia (core state) 2.78; Ukraine 2.20; Idelsk-Uralia 1.67; Belarus 1.54; Kazakhstan 1.45; Siberia 0.66; Donska-Kubania 0.64; Künnarantaiga 0.38; Dagestan 0.12; Chechnya 0.06; Kabardino-Balkaria 0.03; North Ossetia-Alania 0.03; Ingushetia 0.02; Karachay-Cherkessia 0.02; Tuva 0.01 |
| Japanese | 10.42 | 10.42 | Japan 10.42 |
| German | 9.93 | 9.93 | Germany 8.54; Austro-Bavaria 1.39 |
| Korean | 8.35 | 8.35 | Korea 8.35 |
| Indonesian | 5.84 | 5.94 | Indonesia 5.74; West Papua 0.10; Aceh 0.10 |
| Thai | 3.23 | 3.33 | Thailand 3.23; Patani 0.10 |
| Vietnamese | 3.10 | 3.10 | Vietnam 3.10 |
| Filipino (Tagalog) | 0.00 | 3.06 | Philippines 3.06 |
| Chinese (Mandarin and other) | 0.00 | 2.95 | Malaysia 2.95 |
| Malay | 0.00 | 2.95 | Malaysia 2.95 |
| Tamil | 0.00 | 2.95 | Malaysia 2.95 |
| Afrikaans | 0.00 | 2.75 | South Africa 2.75 |
| Zulu and other Bantu languages | 0.00 | 2.75 | South Africa 2.75 |
| Romanian | 2.51 | 2.51 | Romania 2.51 |
| Ukrainian | 0.00 | 2.20 | Ukraine 2.20 |
| Tatar and Bashkir | 0.00 | 1.67 | Idelsk-Uralia 1.67 |
| Belarusian | 0.00 | 1.54 | Belarus 1.54 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Bulgarian | 1.42 | 1.42 | Bulgaria 1.42 |
| Lithuanian | 1.18 | 1.18 | Lithuania 1.18 |
| Estonian | 1.17 | 1.17 | Estonia 1.17 |
| Latvian | 0.89 | 0.89 | Latvia 0.89 |
| Mongolian | 0.00 | 0.40 | Mongolia 0.40 |
| Uyghur | 0.00 | 0.34 | East Turkestan 0.34 |
| Hungarian | 0.29 | 0.29 | Hungary 0.29 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.12 | Dagestan 0.12 |
| Acehnese | 0.00 | 0.10 | Aceh 0.10 |
| Patani Malay | 0.00 | 0.10 | Patani 0.10 |
| Chechen | 0.00 | 0.06 | Chechnya 0.06 |
| Tibetan | 0.00 | 0.05 | Tibet 0.05 |
| Kabardian and Balkar | 0.00 | 0.03 | Kabardino-Balkaria 0.03 |
| Ossetian | 0.00 | 0.03 | North Ossetia-Alania 0.03 |
| Finnish | 0.02 | 0.02 | Finland 0.02 |
| Ingush | 0.00 | 0.02 | Ingushetia 0.02 |
| Karachay and Circassian languages | 0.00 | 0.02 | Karachay-Cherkessia 0.02 |
| Tuvan | 0.00 | 0.01 | Tuva 0.01 |

**MULTI / UNMAPPED rows in this city:** Philippines 3.060% (MULTI: Filipino (Tagalog) / English); Malaysia 2.950% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); South Africa 2.750% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Ukraine 2.200% (MULTI: Ukrainian / Russian); Idelsk-Uralia 1.670% (MULTI: Russian / Tatar and Bashkir); Belarus 1.540% (MULTI: Belarusian / Russian); Kazakhstan 1.450% (MULTI: Kazakh / Russian); Mongolia 0.400% (MULTI: Mongolian / Mandarin); East Turkestan 0.340% (MULTI: Uyghur / Mandarin); Dagestan 0.120% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Aceh 0.096% (MULTI: Acehnese / Indonesian); Patani 0.095% (MULTI: Patani Malay / Thai); Chechnya 0.056% (MULTI: Russian / Chechen); Tibet 0.047% (MULTI: Tibetan / Mandarin); Kabardino-Balkaria 0.034% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.026% (MULTI: Russian / Ossetian); Ingushetia 0.019% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.018% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.013% (MULTI: Russian / Tuvan)

### Kunlun

*Census I table counts: robots 148,497 (robots column only; no human column in this table). Share total 99.994%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| Mandarin | 15.09 | 20.75 | Sinian Federation 15.09; Mongolia 5.66 |
| English | 17.81 | 18.96 | United Kingdom 6.97; CSA 5.66; New Zealand 2.65; Australia 2.53; South Africa 1.15 |
| Russian | 11.32 | 11.32 | Russia (core state) 5.66; Künnarantaiga 5.66 |
| French | 10.59 | 10.59 | Quebec 7.74; France 2.85 |
| Japanese | 7.26 | 7.26 | Japan 7.26 |
| Spanish | 6.17 | 6.17 | Argentina (without Patagonia) 2.62; Chile 2.30; Spain 1.25 |
| Italian | 5.66 | 5.66 | Meridia 2.83; Magna Lombardia 2.83 |
| Mongolian | 0.00 | 5.66 | Mongolia 5.66 |
| Korean | 4.36 | 4.36 | Korea 4.36 |
| German | 3.58 | 3.58 | Germany 2.51; Austro-Bavaria 1.07 |
| Swedish | 2.55 | 2.55 | Sweden 2.55 |
| Norwegian | 1.88 | 1.88 | Norway 1.88 |
| Afrikaans | 0.00 | 1.15 | South Africa 1.15 |
| Zulu and other Bantu languages | 0.00 | 1.15 | South Africa 1.15 |
| Dutch | 0.05 | 0.05 | Netherlands 0.05 |
| UNMAPPED | 6.86 | 6.86 | Intermarium/Intermaria |

**MULTI / UNMAPPED rows in this city:** Intermarium/Intermaria 6.860% UNMAPPED; Mongolia 5.660% (MULTI: Mongolian / Mandarin); South Africa 1.150% (MULTI: English / Afrikaans / Zulu and other Bantu languages)

### Mirny

*Census I table counts: robots 710,578, humans 692,971; Census II: robots 528,352, humans 524,022. Share total 99.977%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 25.23 | 34.38 | United Kingdom 13.73; Australia 6.96; Philippines 4.24; New Zealand 4.22; Malaysia 3.44; South Africa 1.47; Northern Ireland 0.32 |
| Mandarin | 15.77 | 16.74 | Sinian Federation 12.00; Taiwan 2.86; Manchuria 0.91; Mongolia 0.48; East Turkestan 0.43; Tibet 0.06 |
| Korean | 13.71 | 13.71 | Korea 13.71 |
| Indonesian | 12.24 | 12.44 | Indonesia 12.03; West Papua 0.21; Aceh 0.20 |
| Russian | 4.29 | 9.73 | Idelsk-Uralia 2.14; Russia (core state) 2.14; Belarus 1.49; Kazakhstan 1.45; Siberia 0.85; Donska-Kubania 0.81; Künnarantaiga 0.49; Dagestan 0.15; Chechnya 0.07; Kabardino-Balkaria 0.04; North Ossetia-Alania 0.03; Ingushetia 0.03; Karachay-Cherkessia 0.02; Tuva 0.02 |
| Japanese | 7.81 | 7.81 | Japan 7.81 |
| Filipino (Tagalog) | 0.00 | 4.24 | Philippines 4.24 |
| Thai | 3.39 | 3.49 | Thailand 3.39; Patani 0.10 |
| Chinese (Mandarin and other) | 0.00 | 3.44 | Malaysia 3.44 |
| Malay | 0.00 | 3.44 | Malaysia 3.44 |
| Tamil | 0.00 | 3.44 | Malaysia 3.44 |
| Tatar and Bashkir | 0.00 | 2.14 | Idelsk-Uralia 2.14 |
| Vietnamese | 1.65 | 1.65 | Vietnam 1.65 |
| Belarusian | 0.00 | 1.49 | Belarus 1.49 |
| Afrikaans | 0.00 | 1.47 | South Africa 1.47 |
| Zulu and other Bantu languages | 0.00 | 1.47 | South Africa 1.47 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Mongolian | 0.00 | 0.48 | Mongolia 0.48 |
| Uyghur | 0.00 | 0.43 | East Turkestan 0.43 |
| Acehnese | 0.00 | 0.20 | Aceh 0.20 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.15 | Dagestan 0.15 |
| Patani Malay | 0.00 | 0.10 | Patani 0.10 |
| Chechen | 0.00 | 0.07 | Chechnya 0.07 |
| Tibetan | 0.00 | 0.06 | Tibet 0.06 |
| Kabardian and Balkar | 0.00 | 0.04 | Kabardino-Balkaria 0.04 |
| Ossetian | 0.00 | 0.03 | North Ossetia-Alania 0.03 |
| Finnish | 0.03 | 0.03 | Finland 0.03 |
| Ingush | 0.00 | 0.03 | Ingushetia 0.03 |
| Karachay and Circassian languages | 0.00 | 0.02 | Karachay-Cherkessia 0.02 |
| Tuvan | 0.00 | 0.02 | Tuva 0.02 |

**MULTI / UNMAPPED rows in this city:** Philippines 4.240% (MULTI: Filipino (Tagalog) / English); Malaysia 3.440% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Idelsk-Uralia 2.140% (MULTI: Russian / Tatar and Bashkir); Belarus 1.490% (MULTI: Belarusian / Russian); South Africa 1.470% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Kazakhstan 1.450% (MULTI: Kazakh / Russian); Mongolia 0.480% (MULTI: Mongolian / Mandarin); East Turkestan 0.430% (MULTI: Uyghur / Mandarin); Aceh 0.200% (MULTI: Acehnese / Indonesian); Dagestan 0.150% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Patani 0.100% (MULTI: Patani Malay / Thai); Chechnya 0.072% (MULTI: Russian / Chechen); Tibet 0.060% (MULTI: Tibetan / Mandarin); Kabardino-Balkaria 0.042% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.033% (MULTI: Russian / Ossetian); Ingushetia 0.025% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.023% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.016% (MULTI: Russian / Tuvan)

### Relung Panen

*Census I table counts: robots 507,856, humans 492,215; Census II: robots 364,524, humans 349,521. Share total 100.037%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 14.64 | 20.75 | Australia 11.84; Malaysia 3.11; Philippines 3.00; New Zealand 2.80 |
| Mandarin | 15.57 | 16.44 | Sinian Federation 11.85; Taiwan 2.86; Manchuria 0.86; Mongolia 0.44; East Turkestan 0.38; Tibet 0.05 |
| Russian | 7.49 | 13.30 | Idelsk-Uralia 3.73; Russia (core state) 3.73; Siberia 1.48; Kazakhstan 1.45; Donska-Kubania 1.42; Künnarantaiga 0.86; Dagestan 0.26; Chechnya 0.13; Kabardino-Balkaria 0.07; North Ossetia-Alania 0.06; Ingushetia 0.04; Karachay-Cherkessia 0.04; Tuva 0.03 |
| Indonesian | 12.84 | 13.07 | Indonesia 12.60; West Papua 0.24; Aceh 0.23 |
| Japanese | 12.86 | 12.86 | Japan 12.86 |
| Korean | 12.43 | 12.43 | Korea 12.43 |
| Thai | 5.64 | 5.78 | Thailand 5.64; Patani 0.14 |
| Vietnamese | 5.36 | 5.36 | Vietnam 5.36 |
| Tatar and Bashkir | 0.00 | 3.73 | Idelsk-Uralia 3.73 |
| Chinese (Mandarin and other) | 0.00 | 3.11 | Malaysia 3.11 |
| Malay | 0.00 | 3.11 | Malaysia 3.11 |
| Tamil | 0.00 | 3.11 | Malaysia 3.11 |
| Filipino (Tagalog) | 0.00 | 3.00 | Philippines 3.00 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Mongolian | 0.00 | 0.44 | Mongolia 0.44 |
| Uyghur | 0.00 | 0.38 | East Turkestan 0.38 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.26 | Dagestan 0.26 |
| Acehnese | 0.00 | 0.23 | Aceh 0.23 |
| Patani Malay | 0.00 | 0.14 | Patani 0.14 |
| Chechen | 0.00 | 0.13 | Chechnya 0.13 |
| Kabardian and Balkar | 0.00 | 0.07 | Kabardino-Balkaria 0.07 |
| Ossetian | 0.00 | 0.06 | North Ossetia-Alania 0.06 |
| Tibetan | 0.00 | 0.05 | Tibet 0.05 |
| Finnish | 0.04 | 0.04 | Finland 0.04 |
| Ingush | 0.00 | 0.04 | Ingushetia 0.04 |
| Karachay and Circassian languages | 0.00 | 0.04 | Karachay-Cherkessia 0.04 |
| Tuvan | 0.00 | 0.03 | Tuva 0.03 |

**MULTI / UNMAPPED rows in this city:** Idelsk-Uralia 3.730% (MULTI: Russian / Tatar and Bashkir); Malaysia 3.110% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Philippines 3.000% (MULTI: Filipino (Tagalog) / English); Kazakhstan 1.450% (MULTI: Kazakh / Russian); Mongolia 0.440% (MULTI: Mongolian / Mandarin); East Turkestan 0.380% (MULTI: Uyghur / Mandarin); Dagestan 0.260% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Aceh 0.230% (MULTI: Acehnese / Indonesian); Patani 0.140% (MULTI: Patani Malay / Thai); Chechnya 0.130% (MULTI: Russian / Chechen); Kabardino-Balkaria 0.075% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.057% (MULTI: Russian / Ossetian); Tibet 0.053% (MULTI: Tibetan / Mandarin); Ingushetia 0.042% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.038% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.028% (MULTI: Russian / Tuvan)

### Shirayuki

*Census I table counts: robots 566,709, humans 545,891; Census II: robots 372,181, humans 319,190. Share total 99.989%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| Japanese | 34.20 | 34.20 | Japan 34.20 |
| Russian | 6.09 | 15.30 | Russia (core state) 3.53; Belarus 2.83; Idelsk-Uralia 2.55; Ukraine 1.95; Kazakhstan 1.45; Siberia 1.01; Donska-Kubania 0.97; Künnarantaiga 0.58; Dagestan 0.18; Chechnya 0.09; Kabardino-Balkaria 0.05; North Ossetia-Alania 0.04; Ingushetia 0.03; Karachay-Cherkessia 0.03; Tuva 0.02 |
| English | 12.45 | 14.02 | Australia 9.65; New Zealand 2.80; South Africa 1.57 |
| Korean | 9.10 | 9.10 | Korea 9.10 |
| Mandarin | 7.61 | 7.97 | Sinian Federation 4.49; Taiwan 2.86; Manchuria 0.26; Mongolia 0.21; East Turkestan 0.13; Tibet 0.02 |
| German | 4.65 | 4.65 | Germany 3.90; Austro-Bavaria 0.75 |
| Romanian | 2.99 | 2.99 | Romania 2.99 |
| Vietnamese | 2.98 | 2.98 | Vietnam 2.98 |
| Belarusian | 0.00 | 2.83 | Belarus 2.83 |
| Thai | 2.74 | 2.82 | Thailand 2.74; Patani 0.08 |
| Tatar and Bashkir | 0.00 | 2.55 | Idelsk-Uralia 2.55 |
| Ukrainian | 0.00 | 1.95 | Ukraine 1.95 |
| Lithuanian | 1.66 | 1.66 | Lithuania 1.66 |
| Afrikaans | 0.00 | 1.57 | South Africa 1.57 |
| Zulu and other Bantu languages | 0.00 | 1.57 | South Africa 1.57 |
| Bulgarian | 1.51 | 1.51 | Bulgaria 1.51 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Latvian | 1.27 | 1.27 | Latvia 1.27 |
| Estonian | 1.15 | 1.15 | Estonia 1.15 |
| Hungarian | 0.34 | 0.34 | Hungary 0.34 |
| Mongolian | 0.00 | 0.21 | Mongolia 0.21 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.18 | Dagestan 0.18 |
| Uyghur | 0.00 | 0.13 | East Turkestan 0.13 |
| Chechen | 0.00 | 0.09 | Chechnya 0.09 |
| Patani Malay | 0.00 | 0.08 | Patani 0.08 |
| Kabardian and Balkar | 0.00 | 0.05 | Kabardino-Balkaria 0.05 |
| Ossetian | 0.00 | 0.04 | North Ossetia-Alania 0.04 |
| Finnish | 0.03 | 0.03 | Finland 0.03 |
| Ingush | 0.00 | 0.03 | Ingushetia 0.03 |
| Karachay and Circassian languages | 0.00 | 0.03 | Karachay-Cherkessia 0.03 |
| Tuvan | 0.00 | 0.02 | Tuva 0.02 |
| Tibetan | 0.00 | 0.02 | Tibet 0.02 |

**MULTI / UNMAPPED rows in this city:** Belarus 2.830% (MULTI: Belarusian / Russian); Idelsk-Uralia 2.550% (MULTI: Russian / Tatar and Bashkir); Ukraine 1.950% (MULTI: Ukrainian / Russian); South Africa 1.570% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Kazakhstan 1.450% (MULTI: Kazakh / Russian); Mongolia 0.210% (MULTI: Mongolian / Mandarin); Dagestan 0.180% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); East Turkestan 0.130% (MULTI: Uyghur / Mandarin); Chechnya 0.086% (MULTI: Russian / Chechen); Patani 0.080% (MULTI: Patani Malay / Thai); Kabardino-Balkaria 0.051% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.038% (MULTI: Russian / Ossetian); Ingushetia 0.029% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.027% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.019% (MULTI: Russian / Tuvan); Tibet 0.018% (MULTI: Tibetan / Mandarin)

### Sinheung

*Census I table counts: robots 520,192, humans 494,341; Census II: robots 424,595, humans 410,746. Share total 99.992%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| Korean | 33.00 | 33.00 | Korea 33.00 |
| German | 10.06 | 10.06 | Germany 8.75; Austro-Bavaria 1.31 |
| Japanese | 9.40 | 9.40 | Japan 9.40 |
| Mandarin | 8.65 | 9.10 | Sinian Federation 5.45; Taiwan 2.86; Manchuria 0.34; Mongolia 0.25; East Turkestan 0.17; Tibet 0.03 |
| English | 3.37 | 8.96 | Australia 3.37; Malaysia 2.76; Philippines 1.67; South Africa 1.16 |
| Russian | 4.08 | 7.90 | Idelsk-Uralia 2.03; Russia (core state) 2.03; Kazakhstan 1.45; Siberia 0.81; Donska-Kubania 0.77; Künnarantaiga 0.47; Dagestan 0.14; Chechnya 0.07; Kabardino-Balkaria 0.04; North Ossetia-Alania 0.03; Ingushetia 0.02; Karachay-Cherkessia 0.02; Tuva 0.01 |
| Indonesian | 4.08 | 4.16 | Indonesia 3.99; West Papua 0.09; Aceh 0.08 |
| Thai | 3.34 | 3.44 | Thailand 3.34; Patani 0.10 |
| Estonian | 3.32 | 3.32 | Estonia 3.32 |
| Hungarian | 3.23 | 3.23 | Hungary 3.23 |
| Lithuanian | 2.93 | 2.93 | Lithuania 2.93 |
| Chinese (Mandarin and other) | 0.00 | 2.76 | Malaysia 2.76 |
| Malay | 0.00 | 2.76 | Malaysia 2.76 |
| Tamil | 0.00 | 2.76 | Malaysia 2.76 |
| Tatar and Bashkir | 0.00 | 2.03 | Idelsk-Uralia 2.03 |
| Vietnamese | 1.84 | 1.84 | Vietnam 1.84 |
| Filipino (Tagalog) | 0.00 | 1.67 | Philippines 1.67 |
| Kazakh | 0.00 | 1.45 | Kazakhstan 1.45 |
| Bulgarian | 1.37 | 1.37 | Bulgaria 1.37 |
| Latvian | 1.27 | 1.27 | Latvia 1.27 |
| Afrikaans | 0.00 | 1.16 | South Africa 1.16 |
| Zulu and other Bantu languages | 0.00 | 1.16 | South Africa 1.16 |
| Mongolian | 0.00 | 0.25 | Mongolia 0.25 |
| Uyghur | 0.00 | 0.17 | East Turkestan 0.17 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.14 | Dagestan 0.14 |
| Patani Malay | 0.00 | 0.10 | Patani 0.10 |
| Acehnese | 0.00 | 0.08 | Aceh 0.08 |
| Chechen | 0.00 | 0.07 | Chechnya 0.07 |
| Kabardian and Balkar | 0.00 | 0.04 | Kabardino-Balkaria 0.04 |
| Ossetian | 0.00 | 0.03 | North Ossetia-Alania 0.03 |
| Tibetan | 0.00 | 0.03 | Tibet 0.03 |
| Finnish | 0.02 | 0.02 | Finland 0.02 |
| Ingush | 0.00 | 0.02 | Ingushetia 0.02 |
| Karachay and Circassian languages | 0.00 | 0.02 | Karachay-Cherkessia 0.02 |
| Tuvan | 0.00 | 0.01 | Tuva 0.01 |

**MULTI / UNMAPPED rows in this city:** Malaysia 2.760% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Idelsk-Uralia 2.030% (MULTI: Russian / Tatar and Bashkir); Philippines 1.670% (MULTI: Filipino (Tagalog) / English); Kazakhstan 1.450% (MULTI: Kazakh / Russian); South Africa 1.160% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Mongolia 0.250% (MULTI: Mongolian / Mandarin); East Turkestan 0.170% (MULTI: Uyghur / Mandarin); Dagestan 0.140% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Patani 0.098% (MULTI: Patani Malay / Thai); Aceh 0.082% (MULTI: Acehnese / Indonesian); Chechnya 0.068% (MULTI: Russian / Chechen); Kabardino-Balkaria 0.040% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.031% (MULTI: Russian / Ossetian); Tibet 0.025% (MULTI: Tibetan / Mandarin); Ingushetia 0.023% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.021% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.015% (MULTI: Russian / Tuvan)

### Zhongshan

*Census I table counts: robots 607,752, humans 595,855; Census II: robots 446,082, humans 486,813. Share total 99.986%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| Mandarin | 35.83 | 35.83 | Sinian Federation 35.83 |
| English | 4.94 | 10.90 | Australia 3.66; Malaysia 3.04; Philippines 1.72; New Zealand 1.28; South Africa 1.20 |
| Korean | 9.70 | 9.70 | Korea 9.70 |
| German | 8.47 | 8.47 | Germany 7.10; Austro-Bavaria 1.37 |
| Japanese | 7.30 | 7.30 | Japan 7.30 |
| Russian | 3.59 | 5.68 | Idelsk-Uralia 1.79; Russia (core state) 1.79; Siberia 0.71; Donska-Kubania 0.68; Künnarantaiga 0.41; Dagestan 0.13; Chechnya 0.06; Kabardino-Balkaria 0.04; North Ossetia-Alania 0.03; Ingushetia 0.02; Karachay-Cherkessia 0.02; Tuva 0.01 |
| Vietnamese | 3.56 | 3.56 | Vietnam 3.56 |
| Estonian | 3.55 | 3.55 | Estonia 3.55 |
| Thai | 3.09 | 3.18 | Thailand 3.09; Patani 0.09 |
| Lithuanian | 3.14 | 3.14 | Lithuania 3.14 |
| Chinese (Mandarin and other) | 0.00 | 3.04 | Malaysia 3.04 |
| Malay | 0.00 | 3.04 | Malaysia 3.04 |
| Tamil | 0.00 | 3.04 | Malaysia 3.04 |
| Indonesian | 2.92 | 2.98 | Indonesia 2.86; West Papua 0.06; Aceh 0.06 |
| Romanian | 2.58 | 2.58 | Romania 2.58 |
| Tatar and Bashkir | 0.00 | 1.79 | Idelsk-Uralia 1.79 |
| Filipino (Tagalog) | 0.00 | 1.72 | Philippines 1.72 |
| Latvian | 1.58 | 1.58 | Latvia 1.58 |
| Bulgarian | 1.21 | 1.21 | Bulgaria 1.21 |
| Afrikaans | 0.00 | 1.20 | South Africa 1.20 |
| Zulu and other Bantu languages | 0.00 | 1.20 | South Africa 1.20 |
| Hungarian | 0.30 | 0.30 | Hungary 0.30 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.13 | Dagestan 0.13 |
| Patani Malay | 0.00 | 0.09 | Patani 0.09 |
| Chechen | 0.00 | 0.06 | Chechnya 0.06 |
| Acehnese | 0.00 | 0.06 | Aceh 0.06 |
| Kabardian and Balkar | 0.00 | 0.04 | Kabardino-Balkaria 0.04 |
| Ossetian | 0.00 | 0.03 | North Ossetia-Alania 0.03 |
| Finnish | 0.02 | 0.02 | Finland 0.02 |
| Ingush | 0.00 | 0.02 | Ingushetia 0.02 |
| Karachay and Circassian languages | 0.00 | 0.02 | Karachay-Cherkessia 0.02 |
| Tuvan | 0.00 | 0.01 | Tuva 0.01 |

**MULTI / UNMAPPED rows in this city:** Malaysia 3.040% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Idelsk-Uralia 1.790% (MULTI: Russian / Tatar and Bashkir); Philippines 1.720% (MULTI: Filipino (Tagalog) / English); South Africa 1.200% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Dagestan 0.130% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Patani 0.090% (MULTI: Patani Malay / Thai); Chechnya 0.060% (MULTI: Russian / Chechen); Aceh 0.059% (MULTI: Acehnese / Indonesian); Kabardino-Balkaria 0.036% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.027% (MULTI: Russian / Ossetian); Ingushetia 0.020% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.019% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.013% (MULTI: Russian / Tuvan)

### Contrapunto

*Census I table counts: robots 328,142, humans 316,691; Census II: robots 279,766, humans 234,304. Share total 100.003%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 28.94 | 33.93 | United Kingdom 10.98; CSA 7.00; Appalachia 4.49; Cascadia 3.68; New England 3.67; Midwest Republic 1.40; Sonora 1.22; Colorado 1.05; Northern Ireland 0.31; Hawaii 0.09; Alaska 0.04 |
| Spanish | 19.02 | 23.92 | México 9.10; Argentina (without Patagonia) 4.02; Cascadia 3.68; Chile 3.04; Yucatán 1.22; Sonora 1.22; Uruguay 0.91; Araucanía-Patagonia 0.73 |
| French | 11.61 | 11.61 | France 11.61 |
| German | 10.72 | 10.72 | Germany 8.99; Austro-Bavaria 1.73 |
| Portuguese | 6.68 | 6.68 | Brazil 6.02; Amazonia 0.66 |
| Italian | 6.13 | 6.13 | Magna Lombardia 3.49; Meridia 2.14; Sicilia (autonomous zone within Meridia) 0.50 |
| Russian | 3.85 | 6.10 | Idelsk-Uralia 1.92; Russia (core state) 1.92; Siberia 0.76; Donska-Kubania 0.73; Künnarantaiga 0.44; Dagestan 0.14; Chechnya 0.06; Kabardino-Balkaria 0.04; North Ossetia-Alania 0.03; Ingushetia 0.02; Karachay-Cherkessia 0.02; Tuva 0.01 |
| Korean | 5.79 | 5.79 | Korea 5.79 |
| Tatar and Bashkir | 0.00 | 1.92 | Idelsk-Uralia 1.92 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.14 | Dagestan 0.14 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.09 | Hawaii 0.09 |
| Chechen | 0.00 | 0.06 | Chechnya 0.06 |
| Kabardian and Balkar | 0.00 | 0.04 | Kabardino-Balkaria 0.04 |
| Ossetian | 0.00 | 0.03 | North Ossetia-Alania 0.03 |
| Finnish | 0.02 | 0.02 | Finland 0.02 |
| Ingush | 0.00 | 0.02 | Ingushetia 0.02 |
| Karachay and Circassian languages | 0.00 | 0.02 | Karachay-Cherkessia 0.02 |
| Tuvan | 0.00 | 0.01 | Tuva 0.01 |

**MULTI / UNMAPPED rows in this city:** Cascadia 3.680% (MULTI: English / Spanish); Idelsk-Uralia 1.920% (MULTI: Russian / Tatar and Bashkir); Sonora 1.220% (MULTI: English / Spanish); Dagestan 0.140% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Hawaii 0.091% (MULTI: Hawaiian (the dominant language everywhere) / English); Chechnya 0.064% (MULTI: Russian / Chechen); Kabardino-Balkaria 0.038% (MULTI: Russian / Kabardian and Balkar); North Ossetia-Alania 0.029% (MULTI: Russian / Ossetian); Ingushetia 0.022% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.020% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.014% (MULTI: Russian / Tuvan)

### Esperanza

*Census I table counts: robots 589,670, humans 610,330; Census II: robots 430,946, humans 322,213. Share total 99.991%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 39.48 | 47.72 | CSA 11.76; United Kingdom 9.55; Appalachia 7.55; New England 6.17; Cascadia 6.13; Midwest Republic 2.35; Sonora 1.96; Colorado 1.76; Northern Ireland 0.27; Hawaii 0.15; Alaska 0.07 |
| Spanish | 33.36 | 41.45 | México 14.08; Argentina (without Patagonia) 7.87; Uruguay 6.60; Cascadia 6.13; Chile 2.14; Sonora 1.96; Yucatán 1.85; Araucanía-Patagonia 0.82 |
| Portuguese | 18.91 | 18.91 | Brazil 17.03; Amazonia 1.88 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.15 | Hawaii 0.15 |

**MULTI / UNMAPPED rows in this city:** Cascadia 6.130% (MULTI: English / Spanish); Sonora 1.960% (MULTI: English / Spanish); Hawaii 0.150% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Marambio

*Census I table counts: robots 286,827, humans 283,442; Census II: robots 234,522, humans 195,623. Share total 100.024%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 40.16 | 47.48 | United Kingdom 13.10; CSA 8.92; Appalachia 5.73; Cascadia 5.67; New England 4.68; Demilitarized Zone (s. Ontario, not a nation) 2.66; Midwest Republic 1.78; Sonora 1.53; Prairie Federation 1.50; Colorado 1.34; Northern Ireland 0.38; Hawaii 0.12; Alaska 0.07 |
| Spanish | 34.22 | 44.61 | México 11.38; Spain 10.98; Cascadia 5.67; Uruguay 4.74; Chile 4.19; Catalonia 2.35; Sonora 1.53; Yucatán 1.51; Basque Country 0.84; Araucanía-Patagonia 0.72; Argentina (without Patagonia) 0.70 |
| German | 6.59 | 6.59 | Germany 5.53; Austro-Bavaria 1.06 |
| Portuguese | 6.50 | 6.50 | Brazil 5.85; Amazonia 0.65 |
| Catalan | 0.00 | 2.35 | Catalonia 2.35 |
| French | 2.04 | 2.04 | Quebec 2.04 |
| Basque | 0.00 | 0.84 | Basque Country 0.84 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.12 | Hawaii 0.12 |

**MULTI / UNMAPPED rows in this city:** Cascadia 5.670% (MULTI: English / Spanish); Catalonia 2.350% (MULTI: Catalan / Spanish); Sonora 1.530% (MULTI: English / Spanish); Basque Country 0.840% (MULTI: Basque / Spanish); Hawaii 0.120% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Palmer City

*Census I table counts: robots 166,896, humans 165,912; Census II: robots 151,482, humans 180,688. Share total 99.960%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 27.46 | 34.50 | CSA 6.61; United Kingdom 5.42; Appalachia 4.21; Cascadia 4.05; New England 3.44; Demilitarized Zone (s. Ontario, not a nation) 2.10; Australia 1.33; Midwest Republic 1.31; Prairie Federation 1.18; Colorado 0.98; South Africa 0.96; Sonora 0.88; Philippines 0.82; New Zealand 0.67; Malaysia 0.25; Northern Ireland 0.15; Hawaii 0.09; Alaska 0.06 |
| Spanish | 13.30 | 18.35 | México 4.64; Cascadia 4.05; Uruguay 3.70; Argentina (without Patagonia) 2.88; Sonora 0.88; Chile 0.74; Yucatán 0.64; Spain 0.41; Araucanía-Patagonia 0.29; Catalonia 0.09; Basque Country 0.03 |
| French | 11.69 | 11.69 | France 10.09; Quebec 1.60 |
| Portuguese | 9.74 | 9.74 | Brazil 8.78; Amazonia 0.96 |
| German | 9.56 | 9.56 | Germany 8.03; Austro-Bavaria 1.53 |
| Russian | 0.87 | 1.98 | Russia (core state) 0.49; Belarus 0.44; Idelsk-Uralia 0.38; Ukraine 0.23; Siberia 0.15; Donska-Kubania 0.14; Künnarantaiga 0.09; Dagestan 0.03; Chechnya 0.01; Kabardino-Balkaria 0.01; North Ossetia-Alania 0.01; Ingushetia 0.00; Karachay-Cherkessia 0.00; Tuva 0.00 |
| Dutch | 1.42 | 1.42 | Netherlands 1.42 |
| Estonian | 1.39 | 1.39 | Estonia 1.39 |
| Czech | 1.35 | 1.35 | Czechia 1.35 |
| Slovak | 1.29 | 1.29 | Slovakia 1.29 |
| Thai | 1.22 | 1.26 | Thailand 1.22; Patani 0.04 |
| Serbian | 1.16 | 1.16 | Serbia 1.16 |
| Korean | 1.09 | 1.09 | Korea 1.09 |
| Italian | 1.06 | 1.06 | Magna Lombardia 0.60; Meridia 0.37; Sicilia (autonomous zone within Meridia) 0.09 |
| Norwegian | 1.01 | 1.01 | Norway 1.01 |
| Croatian | 0.97 | 0.97 | Croatia 0.97 |
| Afrikaans | 0.00 | 0.96 | South Africa 0.96 |
| Zulu and other Bantu languages | 0.00 | 0.96 | South Africa 0.96 |
| Slovene | 0.86 | 0.86 | Slovenia 0.86 |
| Filipino (Tagalog) | 0.00 | 0.82 | Philippines 0.82 |
| Romanian | 0.77 | 0.77 | Romania 0.77 |
| Japanese | 0.73 | 0.73 | Japan 0.73 |
| Polish | 0.70 | 0.70 | Poland 0.70 |
| Bulgarian | 0.62 | 0.62 | Bulgaria 0.62 |
| Mandarin | 0.58 | 0.58 | Sinian Federation 0.58 |
| Vietnamese | 0.58 | 0.58 | Vietnam 0.58 |
| Latvian | 0.48 | 0.48 | Latvia 0.48 |
| Swedish | 0.46 | 0.46 | Sweden 0.46 |
| Belarusian | 0.00 | 0.44 | Belarus 0.44 |
| Tatar and Bashkir | 0.00 | 0.38 | Idelsk-Uralia 0.38 |
| Indonesian | 0.37 | 0.38 | Indonesia 0.36; West Papua 0.01; Aceh 0.01 |
| Finnish | 0.32 | 0.32 | Finland 0.32 |
| Hungarian | 0.32 | 0.32 | Hungary 0.32 |
| Lithuanian | 0.28 | 0.28 | Lithuania 0.28 |
| Chinese (Mandarin and other) | 0.00 | 0.25 | Malaysia 0.25 |
| Malay | 0.00 | 0.25 | Malaysia 0.25 |
| Tamil | 0.00 | 0.25 | Malaysia 0.25 |
| Ukrainian | 0.00 | 0.23 | Ukraine 0.23 |
| Catalan | 0.00 | 0.09 | Catalonia 0.09 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.09 | Hawaii 0.09 |
| Patani Malay | 0.00 | 0.04 | Patani 0.04 |
| Basque | 0.00 | 0.03 | Basque Country 0.03 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.03 | Dagestan 0.03 |
| Chechen | 0.00 | 0.01 | Chechnya 0.01 |
| Acehnese | 0.00 | 0.01 | Aceh 0.01 |
| Kabardian and Balkar | 0.00 | 0.01 | Kabardino-Balkaria 0.01 |
| Ossetian | 0.00 | 0.01 | North Ossetia-Alania 0.01 |
| Ingush | 0.00 | 0.00 | Ingushetia 0.00 |
| Karachay and Circassian languages | 0.00 | 0.00 | Karachay-Cherkessia 0.00 |
| Tuvan | 0.00 | 0.00 | Tuva 0.00 |

**MULTI / UNMAPPED rows in this city:** Cascadia 4.050% (MULTI: English / Spanish); South Africa 0.960% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Sonora 0.880% (MULTI: English / Spanish); Philippines 0.820% (MULTI: Filipino (Tagalog) / English); Belarus 0.440% (MULTI: Belarusian / Russian); Idelsk-Uralia 0.380% (MULTI: Russian / Tatar and Bashkir); Malaysia 0.250% (MULTI: Malay / Chinese (Mandarin and other) / Tamil / English); Ukraine 0.230% (MULTI: Ukrainian / Russian); Catalonia 0.088% (MULTI: Catalan / Spanish); Hawaii 0.085% (MULTI: Hawaiian (the dominant language everywhere) / English); Patani 0.036% (MULTI: Patani Malay / Thai); Basque Country 0.032% (MULTI: Basque / Spanish); Dagestan 0.027% (MULTI: Russian / Dagestani languages (Avar, Dargin, Lezgin and others)); Chechnya 0.013% (MULTI: Russian / Chechen); Kabardino-Balkaria 0.008% (MULTI: Russian / Kabardian and Balkar); Aceh 0.008% (MULTI: Acehnese / Indonesian); North Ossetia-Alania 0.006% (MULTI: Russian / Ossetian); Ingushetia 0.004% (MULTI: Russian / Ingush); Karachay-Cherkessia 0.004% (MULTI: Russian / Karachay and Circassian languages); Tuva 0.003% (MULTI: Russian / Tuvan)

### Pergamino

*Census I table counts: robots 196,950, humans 189,742; Census II: robots 127,462, humans 118,910. Share total 100.008%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 33.36 | 39.04 | CSA 9.58; United Kingdom 8.81; Appalachia 6.15; New England 5.03; Cascadia 4.58; Midwest Republic 1.91; Colorado 1.44; Sonora 0.98; Northern Ireland 0.38; Hawaii 0.12; Alaska 0.06 |
| Spanish | 27.67 | 36.40 | Spain 10.88; Argentina (without Patagonia) 4.75; Cascadia 4.58; Uruguay 4.53; Chile 4.10; Catalonia 2.33; México 2.14; Sonora 0.98; Araucanía-Patagonia 0.95; Basque Country 0.84; Yucatán 0.32 |
| Italian | 14.23 | 14.23 | Magna Lombardia 8.11; Meridia 4.97; Sicilia (autonomous zone within Meridia) 1.15 |
| French | 8.51 | 8.51 | France 8.51 |
| German | 5.03 | 5.03 | Germany 4.22; Austro-Bavaria 0.81 |
| Portuguese | 2.36 | 2.36 | Brazil 2.13; Amazonia 0.23 |
| Catalan | 0.00 | 2.33 | Catalonia 2.33 |
| Basque | 0.00 | 0.84 | Basque Country 0.84 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.12 | Hawaii 0.12 |

**MULTI / UNMAPPED rows in this city:** Cascadia 4.580% (MULTI: English / Spanish); Catalonia 2.330% (MULTI: Catalan / Spanish); Sonora 0.980% (MULTI: English / Spanish); Basque Country 0.840% (MULTI: Basque / Spanish); Hawaii 0.120% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Puerto Abrigo

*Census I table counts: robots 472, humans 457; Census II: robots 304, humans 387. Share total 99.992%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 40.43 | 46.71 | United Kingdom 13.94; CSA 10.35; Appalachia 6.64; New England 5.43; Cascadia 5.00; Midwest Republic 2.06; Colorado 1.55; Sonora 1.15; Northern Ireland 0.40; Hawaii 0.13; Alaska 0.06 |
| Spanish | 12.11 | 18.26 | Cascadia 5.00; Chile 4.94; México 3.60; Argentina (without Patagonia) 2.13; Sonora 1.15; Araucanía-Patagonia 0.93; Yucatán 0.51 |
| French | 16.70 | 16.70 | France 16.70 |
| German | 14.82 | 14.82 | Germany 12.43; Austro-Bavaria 2.39 |
| Portuguese | 9.65 | 9.65 | Brazil 8.69; Amazonia 0.96 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.13 | Hawaii 0.13 |

**MULTI / UNMAPPED rows in this city:** Cascadia 5.000% (MULTI: English / Spanish); Sonora 1.150% (MULTI: English / Spanish); Hawaii 0.130% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Rothera

*Census I table counts: robots 163,689, humans 153,760; Census II: robots 134,073, humans 121,784. Share total 100.006%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 38.72 | 46.57 | CSA 9.24; United Kingdom 6.92; Cascadia 6.54; Appalachia 5.93; Demilitarized Zone (s. Ontario, not a nation) 5.28; New England 4.85; Prairie Federation 2.97; Midwest Republic 1.84; Colorado 1.39; Sonora 1.19; Northern Ireland 0.20; Hawaii 0.12; Alaska 0.10 |
| Spanish | 13.67 | 21.40 | Cascadia 6.54; México 5.75; Chile 4.50; Argentina (without Patagonia) 1.80; Sonora 1.19; Araucanía-Patagonia 0.83; Yucatán 0.79 |
| German | 14.31 | 14.31 | Germany 12.00; Austro-Bavaria 2.31 |
| Portuguese | 13.99 | 13.99 | Brazil 12.60; Amazonia 1.39 |
| French | 11.47 | 11.47 | France 7.43; Quebec 4.04 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.12 | Hawaii 0.12 |

**MULTI / UNMAPPED rows in this city:** Cascadia 6.540% (MULTI: English / Spanish); Sonora 1.190% (MULTI: English / Spanish); Hawaii 0.120% (MULTI: Hawaiian (the dominant language everywhere) / English)

### Signy

*Census I table counts: robots 95,560, humans 93,134; Census II: robots 79,827, humans 53,928. Share total 100.015%.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 44.08 | 55.66 | United Kingdom 16.46; CSA 10.76; Appalachia 6.91; New England 5.65; South Africa 5.46; Cascadia 5.03; Midwest Republic 2.15; Colorado 1.62; Sonora 0.95; Northern Ireland 0.47; Hawaii 0.14; Alaska 0.07 |
| French | 17.33 | 17.33 | France 17.33 |
| Spanish | 11.19 | 17.17 | Argentina (without Patagonia) 5.72; Cascadia 5.03; Chile 2.47; Uruguay 2.26; Sonora 0.95; Araucanía-Patagonia 0.74 |
| Portuguese | 8.03 | 8.03 | Brazil 7.23; Amazonia 0.80 |
| German | 7.80 | 7.80 | Germany 6.54; Austro-Bavaria 1.26 |
| Afrikaans | 0.00 | 5.46 | South Africa 5.46 |
| Zulu and other Bantu languages | 0.00 | 5.46 | South Africa 5.46 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.14 | Hawaii 0.14 |

**MULTI / UNMAPPED rows in this city:** South Africa 5.460% (MULTI: English / Afrikaans / Zulu and other Bantu languages); Cascadia 5.030% (MULTI: English / Spanish); Sonora 0.950% (MULTI: English / Spanish); Hawaii 0.140% (MULTI: Hawaiian (the dominant language everywhere) / English)
