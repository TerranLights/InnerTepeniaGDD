# Amundsen Station: a nation-wide language-bloc composite (2026-11-03)

**Facts only. DERIVED (arithmetic on repo figures); the language of each nation is GENERAL knowledge carried over from the mapping in `Language_Blocs_By_City_2026-11-03.md`. This file names no tier, proposes no threshold and ranks no city.** Hawaiian (later Tepenian) is the dominant language everywhere and is not ranked here.

**Why this file exists.** Developer ruling, 2026-11-03: Amundsen Station's population is a composite of all of Tepenia, because people live and work there for periodic stays and come from all over the country. The station's own spec table is a computed composition and does not reflect that, so its row in the main language-bloc file is provisional. This file gives two nation-wide bases. Nothing in the Amundsen Station spec was changed.

## Method

- **Basis A (primary): the National Origin Totals in `Official_Population_Census.md` Section B.** The census file's own text and heading call it "National Origin Totals — Human Population (Census I)", rebuilt 2026-11-02 (`DR-85`) from each city's final per-nation Specs table (Census I human column). **There is no Census II national-origin table in the file** (Section C holds city and subnet populations only), so Census I humans is the only national basis and is the current one. 83 named nations or regions plus a "Maritime fleet (no nation assigned)" line of 24,942 people; total 15,623,523 (the brief said 82 nations: the table lists 83).
- **Shares** are each nation's humans divided by 15,623,523. The maritime fleet line has no nation, so no language: it is shown as its own line (0.160%) and is the only part of the total that is unassigned. Assigned nations sum to 99.840%.
- **Mapping:** exactly the mapping table, kinds and ranges of `Language_Blocs_By_City_2026-11-03.md` (S and S* rows count in **low** and **high**; M (MULTI) rows count in **high** only, once in every language they could carry; so highs can overlap and sum to more than 100%). Every Section B name was already in that mapping (checked by script: 0 missing); the one spelling difference, the Demilitarized Zone row (a semicolon in the census, a comma in the mapping), was matched by hand. Nothing new was added; no GENERAL addition was needed. No web search was used. "Hawaii" (9,706 people) appears as a MULTI row carrying Hawaiian and English, as in the main file, so a "Hawaiian" line of 0.06% shows at the bottom; it is a mapping artifact, not a claim that the language is minor.
- **Basis B (comparison): population-weighted sum of the other cities' blocs** from the CSV: the 37 other cities' low and high shares weighted by each city's **Census I** population taken from the main file's own "Census I table counts" lines (the table counts, which are the figures behind each city's share table). **Amundsen Station itself is excluded** (it is the subject). **Concordia, Dome Fuji and Kunlun are included**: Concordia with its table counts; Dome Fuji and Kunlun are robots-only tables (no human column), so they count only in **B2**. B1 weights by humans only (the same people Section B counts); B2 weights by robots plus humans (the whole Census I population). Census II was not used: not every city's table counts line carries a Census II figure.
- **Checks:** (1) every Section B nation was summed twice, once through the language sets found in the CSV and once through the mapping table's own text; the two methods agree on every language, low and high (0 differences). (2) Basis B1's total humans, 15,597,460, equals Section B's 15,623,523 minus the maritime fleet (24,942) minus Amundsen Station's own humans (1,121), exactly; so B1 and A describe the same people except those two groups, as they should. (3) Share totals below.

## Basis A: Section B (Census I humans, 15,623,523)

*Share total: assigned nations 99.840% + maritime fleet (no nation, no language) 0.160% = 100.000%. Intermarium/Intermaria does not occur in Section B (UNMAPPED: none).*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 25.53 | 32.17 | Australia 5.29; CSA 5.12; United Kingdom 5.01; Appalachia 3.11; Cascadia 2.58; New England 2.52; New Zealand 1.41; Malaysia 1.24; Philippines 1.23; South Africa 1.03; Midwest Republic 0.96; Demilitarized Zone (s. Ontario, not a nation) 0.77; Colorado 0.72; Sonora 0.50; Prairie Federation 0.44; Northern Ireland 0.14; Hawaii 0.06; Alaska 0.03 |
| Mandarin | 8.18 | 8.51 | Sinian Federation 6.48; Taiwan 1.37; Manchuria 0.33; Mongolia 0.23; East Turkestan 0.10; Tibet 0.01 |
| Spanish | 5.07 | 8.26 | Cascadia 2.58; Argentina (without Patagonia) 1.27; Chile 1.21; México 1.12; Uruguay 0.67; Sonora 0.50; Spain 0.38; Araucanía-Patagonia 0.27; Yucatán 0.15; Catalonia 0.08; Basque Country 0.03 |
| Korean | 6.51 | 6.51 | Korea 6.51 |
| Japanese | 6.07 | 6.07 | Japan 6.07 |
| Russian | 2.42 | 5.59 | Russia (core state) 1.40; Idelsk-Uralia 0.98; Belarus 0.77; Kazakhstan 0.71; Ukraine 0.55; Siberia 0.39; Donska-Kubania 0.37; Künnarantaiga 0.26; Dagestan 0.07; Chechnya 0.03; Kabardino-Balkaria 0.02; North Ossetia-Alania 0.01; Ingushetia 0.01; Karachay-Cherkessia 0.01; Tuva 0.01 |
| German | 5.58 | 5.58 | Germany 4.09; Austro-Bavaria 1.49 |
| Indonesian | 4.33 | 4.41 | Indonesia 4.26; West Papua 0.08; Aceh 0.08 |
| Portuguese | 4.10 | 4.10 | Brazil 3.69; Amazonia 0.41 |
| French | 3.83 | 3.83 | France 3.24; Quebec 0.59 |
| Vietnamese | 1.27 | 1.27 | Vietnam 1.27 |
| Chinese (Mandarin and other) | 0.00 | 1.24 | Malaysia 1.24 |
| Malay | 0.00 | 1.24 | Malaysia 1.24 |
| Tamil | 0.00 | 1.24 | Malaysia 1.24 |
| Filipino (Tagalog) | 0.00 | 1.23 | Philippines 1.23 |
| Italian | 1.21 | 1.21 | Magna Lombardia 0.73; Meridia 0.39; Sicilia (autonomous zone within Meridia) 0.08 |
| Hungarian | 1.17 | 1.17 | Hungary 1.17 |
| Thai | 1.09 | 1.12 | Thailand 1.09; Patani 0.03 |
| Estonian | 1.06 | 1.06 | Estonia 1.06 |
| Afrikaans | 0.00 | 1.03 | South Africa 1.03 |
| Zulu and other Bantu languages | 0.00 | 1.03 | South Africa 1.03 |
| Dutch | 0.99 | 0.99 | Netherlands 0.99 |
| Tatar and Bashkir | 0.00 | 0.98 | Idelsk-Uralia 0.98 |
| Serbian | 0.97 | 0.97 | Serbia 0.97 |
| Slovene | 0.96 | 0.96 | Slovenia 0.96 |
| Polish | 0.96 | 0.96 | Poland 0.96 |
| Czech | 0.92 | 0.92 | Czechia 0.92 |
| Slovak | 0.90 | 0.90 | Slovakia 0.90 |
| Romanian | 0.90 | 0.90 | Romania 0.90 |
| Lithuanian | 0.87 | 0.87 | Lithuania 0.87 |
| Bulgarian | 0.87 | 0.87 | Bulgaria 0.87 |
| Norwegian | 0.86 | 0.86 | Norway 0.86 |
| Croatian | 0.83 | 0.83 | Croatia 0.83 |
| Finnish | 0.77 | 0.77 | Finland 0.77 |
| Belarusian | 0.00 | 0.77 | Belarus 0.77 |
| Latvian | 0.76 | 0.76 | Latvia 0.76 |
| Kazakh | 0.00 | 0.71 | Kazakhstan 0.71 |
| Ukrainian | 0.00 | 0.55 | Ukraine 0.55 |
| Swedish | 0.35 | 0.35 | Sweden 0.35 |
| Mongolian | 0.00 | 0.23 | Mongolia 0.23 |
| Danish | 0.11 | 0.11 | Denmark 0.11 |
| Uyghur | 0.00 | 0.10 | East Turkestan 0.10 |
| Catalan | 0.00 | 0.08 | Catalonia 0.08 |
| Acehnese | 0.00 | 0.08 | Aceh 0.08 |
| Dagestani languages (Avar, Dargin, Lezgin and others) | 0.00 | 0.07 | Dagestan 0.07 |
| Hawaiian (the dominant language everywhere) | 0.00 | 0.06 | Hawaii 0.06 |
| Chechen | 0.00 | 0.03 | Chechnya 0.03 |
| Patani Malay | 0.00 | 0.03 | Patani 0.03 |
| Basque | 0.00 | 0.03 | Basque Country 0.03 |
| Icelandic | 0.02 | 0.02 | Iceland 0.02 |
| Kabardian and Balkar | 0.00 | 0.02 | Kabardino-Balkaria 0.02 |
| Ossetian | 0.00 | 0.01 | North Ossetia-Alania 0.01 |
| Tibetan | 0.00 | 0.01 | Tibet 0.01 |
| Ingush | 0.00 | 0.01 | Ingushetia 0.01 |
| Karachay and Circassian languages | 0.00 | 0.01 | Karachay-Cherkessia 0.01 |
| Tuvan | 0.00 | 0.01 | Tuva 0.01 |

| *(no language assigned)* | – | – | Maritime fleet (no nation assigned) 0.160 |

## Basis B1: Census I humans only (37 other cities; total weight 15,597,460)

*Weighted average of the cities' share totals: 99.999%. Top 15 blocs, nations shown for the first eight.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 25.57 | 32.22 | Australia 5.29; CSA 5.13; United Kingdom 5.02; Appalachia 3.12; Cascadia 2.58; New England 2.52; New Zealand 1.42; Malaysia 1.25; … (10 more) |
| Mandarin | 8.19 | 8.53 | Sinian Federation 6.48; Taiwan 1.38; Manchuria 0.33; Mongolia 0.23; East Turkestan 0.10; Tibet 0.01 |
| Spanish | 5.08 | 8.27 | Cascadia 2.58; Argentina (without Patagonia) 1.27; Chile 1.21; México 1.12; Uruguay 0.67; Sonora 0.50; Spain 0.38; Araucanía-Patagonia 0.27; … (3 more) |
| Korean | 6.52 | 6.52 | Korea 6.52 |
| Japanese | 6.08 | 6.08 | Japan 6.08 |
| Russian | 2.42 | 5.60 | Russia (core state) 1.40; Idelsk-Uralia 0.98; Belarus 0.77; Kazakhstan 0.71; Ukraine 0.55; Siberia 0.39; Donska-Kubania 0.37; Künnarantaiga 0.26; … (7 more) |
| German | 5.59 | 5.59 | Germany 4.09; Austro-Bavaria 1.50 |
| Indonesian | 4.34 | 4.42 | Indonesia 4.26; West Papua 0.08; Aceh 0.08 |
| Portuguese | 4.10 | 4.10 | Brazil 3.69; Amazonia 0.41 |
| French | 3.84 | 3.84 | France 3.25; Quebec 0.59 |
| Vietnamese | 1.27 | 1.27 | Vietnam 1.27 |
| Chinese (Mandarin and other) | 0.00 | 1.25 | Malaysia 1.25 |
| Malay | 0.00 | 1.25 | Malaysia 1.25 |
| Tamil | 0.00 | 1.25 | Malaysia 1.25 |
| Filipino (Tagalog) | 0.00 | 1.23 | Philippines 1.23 |

## Basis B2: Census I robots plus humans (37 other cities; total weight 31,969,752)

*Weighted average of the cities' share totals: 99.999%. Top 15 blocs, nations shown for the first eight.*

| Language bloc | Low % | High % | Contributing nations (share %) |
|---|--:|--:|---|
| English | 25.52 | 32.13 | Australia 5.29; CSA 5.13; United Kingdom 5.00; Appalachia 3.10; Cascadia 2.57; New England 2.51; New Zealand 1.42; Malaysia 1.24; … (10 more) |
| Mandarin | 8.19 | 8.57 | Sinian Federation 6.49; Taiwan 1.37; Manchuria 0.32; Mongolia 0.27; East Turkestan 0.10; Tibet 0.01 |
| Spanish | 5.04 | 8.21 | Cascadia 2.57; Argentina (without Patagonia) 1.26; Chile 1.22; México 1.09; Uruguay 0.65; Sonora 0.49; Spain 0.39; Araucanía-Patagonia 0.27; … (3 more) |
| Korean | 6.52 | 6.52 | Korea 6.52 |
| Japanese | 6.12 | 6.12 | Japan 6.12 |
| Russian | 2.47 | 5.64 | Russia (core state) 1.42; Idelsk-Uralia 0.97; Belarus 0.77; Kazakhstan 0.72; Ukraine 0.55; Siberia 0.39; Donska-Kubania 0.37; Künnarantaiga 0.30; … (7 more) |
| German | 5.58 | 5.58 | Germany 4.08; Austro-Bavaria 1.50 |
| Indonesian | 4.37 | 4.44 | Indonesia 4.29; West Papua 0.08; Aceh 0.08 |
| Portuguese | 4.04 | 4.04 | Brazil 3.64; Amazonia 0.40 |
| French | 3.89 | 3.89 | France 3.25; Quebec 0.64 |
| Vietnamese | 1.26 | 1.26 | Vietnam 1.26 |
| Chinese (Mandarin and other) | 0.00 | 1.24 | Malaysia 1.24 |
| Malay | 0.00 | 1.24 | Malaysia 1.24 |
| Tamil | 0.00 | 1.24 | Malaysia 1.24 |
| Italian | 1.22 | 1.22 | Magna Lombardia 0.74; Meridia 0.40; Sicilia (autonomous zone within Meridia) 0.08 |

## Side by side (top eight blocs by high %)

| Language | A low–high | B1 low–high | B2 low–high |
|---|--:|--:|--:|
| English | 25.53–32.17 | 25.57–32.22 | 25.52–32.13 |
| Mandarin | 8.18–8.51 | 8.19–8.53 | 8.19–8.57 |
| Spanish | 5.07–8.26 | 5.08–8.27 | 5.04–8.21 |
| Korean | 6.51–6.51 | 6.52–6.52 | 6.52–6.52 |
| Japanese | 6.07–6.07 | 6.08–6.08 | 6.12–6.12 |
| Russian | 2.42–5.59 | 2.42–5.60 | 2.47–5.64 |
| German | 5.58–5.58 | 5.59–5.59 | 5.58–5.58 |
| Indonesian | 4.33–4.41 | 4.34–4.42 | 4.37–4.44 |

*A language's share here is the share of residents whose national origin is a nation of that language, not a count of speakers. The three bases differ only slightly because B1 is built from the same people as A (see check 2); B2 differs more because it adds the robots, whose composition each city's table gives by the same shares.*
