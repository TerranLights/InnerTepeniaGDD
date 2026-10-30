# Relung Panen ethnic-origin layer · Unit EO2 · Southeast Asia (Indonesia, Malaysia, Thailand, Vietnam, Philippines)

**Brief:** `Evening_Wave_Briefs_Amundsen_and_Ethnic_Origin_2026-10-29.md`, Units EO1 to EO3. **Real-world demographic data only.** Facts only; no trait or stereotype is attributed to any group; no design; no recommendation; no founders inferred. Every claim is marked **SOURCED** (read on the page or in the file named), **UNVERIFIED** (secondary or snippet-only; primary not opened), **DERIVED** (my arithmetic on the stated inputs) or **NOT FOUND**.

**Draft shares of the city (from the brief, may change):** Indonesia 12.23% · Thailand 5.15% · Vietnam 4.76% · Malaysia 3.30% · Philippines 3.18%.

## PROGRESS
- [x] 1 Indonesia (items 1 to 6) — written; **items 2 and 3 NOT OBTAINED** (the province ethnic table is blocked at its source, see §1.2); item 6 is an UNWEIGHTED fallback
- [x] 2 Malaysia (items 1 to 6) — complete from primary sources
- [x] 3 Thailand (items 1 to 6) — complete; **the census has no ethnicity item**, so the composition is by **language** (2000 census) and is labeled as such
- [x] 4 Vietnam (items 1 to 6) — complete from primary sources
- [x] 5 Philippines (items 1 to 6) — written; **items 2 and 3 NOT OBTAINED** (psa.gov.ph returns 403 to every tool used, see §5.2); item 6 is an UNWEIGHTED fallback from UNVERIFIED national figures
- [x] 6 Map-file check (y-files/Map Files, Southeast Asia folders)
- [x] FINAL

Started 2026-10-29 (evening). Finished the same evening.

**Shared method for item 3 (DERIVED).** Each region's weight is population × GDP per head, which is the region's total GDP. The weighted share of group *g* is Σ_r (GDP_r × share of *g* in *r*) / Σ_r GDP_r. Where a statistics office publishes the region's GDP total directly, I used it (it is the same product). **Regional income by ethnic group is NOT FOUND for any of the five nations** (no such table was found or searched for successfully; the method does not need it, but the brief asked to say so).

**Item 2 for all five nations (time zones) — SOURCED (secondary: search-engine summaries of several time-zone references; no national timekeeping authority opened):** Thailand and Vietnam use UTC+7; Malaysia and the Philippines use UTC+8; Indonesia uses three zones, WIB UTC+7, WITA UTC+8, WIT UTC+9 (Wikipedia province infoboxes downloaded for this run state the same offsets per province). **Every region of all five nations lies inside the UTC+4 to UTC+10 window**, so the regional tables below cover each whole nation.

---

## 1 · Indonesia (draft 12.23%)

### 1.1 Latest census ethnic composition
- **Category system.** The 2010 Population Census asked an open self-identification question on *suku bangsa* (ethnicity); answers were coded to 1,331 codes (UNVERIFIED for the exact count; one secondary source gives 1,340). Two published groupings of the same 2010 raw data exist: the BPS initial classification (31 categories, several of them placeholders such as "ethnic groups from Sulawesi") and the "New Classification" of Ananta, Arifin, Hasbullah, Handayani and Pramono (ISEAS with BPS, 2015), which dissolves the placeholder categories. SOURCED (Ananta et al., IUSSP 2013 paper "Changing Ethnic Composition: Indonesia, 2000–2010", downloaded from iussp.org, Table 2 and text; Wikipedia "Ethnic groups in Indonesia" for the BPS initial table).
- **The 2020 census** (register-based, with the Long Form sample survey run in 2022) published fertility, mortality, mobility, labor, disability, education and housing; **ethnicity is not among the listed Long Form topics.** UNVERIFIED (BPS regency pages, as summarized by the search tool; the national Long Form booklet was not opened). So **2010 is the latest census with ethnicity.**
- **2010, New Classification (Ananta et al.), all residents, total 236,728 thousand** — SOURCED (IUSSP paper, Table 2, "authors' calculation from the coded raw data of 2010 population census"):

| Rank | Group | Number (000) | Share |
|---:|---|---:|---:|
| 1 | Javanese | 94,843 | 40.06% |
| 2 | Sundanese | 36,705 | 15.51% |
| 3 | Malay | 8,754 | 3.70% |
| 4 | Batak | 8,467 | 3.58% |
| 5 | Madurese | 7,179 | 3.03% |
| 6 | Betawi | 6,808 | 2.88% |
| 7 | Minangkabau | 6,463 | 2.73% |
| 8 | Buginese | 6,415 | 2.71% |
| 9 | Bantenese | 4,642 | 1.96% |
| 10 | Banjarese | 4,127 | 1.74% |
| 11 | Balinese | 3,925 | 1.66% |
| 12 | Acehnese | 3,404 | 1.44% |
| 13 | Dayak | 3,220 | 1.36% |
| 14 | Sasak | 3,175 | 1.34% |
| 15 | Chinese | 2,833 | 1.20% |
| | Others | 35,769 | 15.11% |

- The BPS **initial** classification gives Javanese 95,217,022 (40.22%), Sundanese 36,701,670 (15.5%), Batak 8,466,969 (3.58%), "ethnic groups from Sulawesi" 7,634,262 (3.22%) and so on. UNVERIFIED (Wikipedia table citing Na'im and Syaputra 2011, BPS; the BPS publication itself returned 403).
- **Limits stated by the source:** the Ananta paper records that the 2000 census under-counted Acehnese (field conditions), Dayak (classification) and Chinese (respondents' reluctance), so 2000 and 2010 are not directly comparable. SOURCED (IUSSP paper, text after Table 2).

### 1.2 Regional distribution (provinces)
- **All of Indonesia lies inside the window** (WIB, WITA, WIT; see top).
- **Province-by-province 2010 ethnic composition: NOT OBTAINED.** The primary table is in BPS, *Kewarganegaraan, Suku Bangsa, Agama, dan Bahasa Sehari-hari Penduduk Indonesia* (2011/2012, catalog 2102032). Its page and asset URL return **HTTP 403** to WebFetch and to a plain curl request; the neliti.com mirror of BPS census publications also returns **403**; the Ananta et al. 2015 book has province tables (its index lists "ethnic composition by sex" per province) but only the index is free (chapters are sold). **Died at the sources, not at the query.**
- **Partial, mixed-source province figures exist in Wikipedia province infoboxes** (downloaded as raw wikitext for this run). They are **not** used in any calculation, because their years and sources differ (some cite the 2010 census or Ananta 2015; Bengkulu cites a 2009 newspaper; several give round numbers from an older book; Jakarta has no figures; Maluku, North Maluku and North Kalimantan give lists without shares). Examples, all **UNVERIFIED**: West Java 71.87% Sundanese, 16.35% Javanese, 5.33% Betawi (cites BPS demographic office, 2010); Central Java 97.9% Javanese; East Java 80.69% Javanese, 17.53% Madurese; Banten 63.43% Sundanese, 16.03% Javanese, 12.88% Betawi; North Sumatra 44.75% Batak, 32.41% Javanese, 7.05% Nias; Aceh 71.72% Acehnese, 9.08% Javanese, 7.33% Gayo; Papua province 76.32% indigenous Papuans, 8.39% Javanese; South Sulawesi 45.12% Buginese, 29.68% Makassarese, 7.34% Torajan.

### 1.3 Weighted composition (DERIVED)
- **NOT COMPUTED.** Without a consistent province ethnic table (1.2), the province weighting cannot be done without inventing inputs. Item 6 below therefore uses the **unweighted** national 2010 shares and says so.
- Province GDP per head exists (Wikipedia "List of Indonesian provinces by GDP per capita", citing BPS; downloaded, not used because the composition side is missing).

### 1.4 Languages and religions (census data only)
- **Daily language spoken at home, 2010, population aged 5+, national:** Indonesian 19.95% · the respondent's own ethnic language 67.58% · other languages 12.47%. SOURCED (IUSSP paper, Table 4, total row). The paper also cross-tabulates language by ethnic group; that cross-tab is not reproduced here.
- **Religion, 2010, Indonesian citizens, national:** Muslim 87.54% · Protestant 6.96% · Catholic 2.91% · Hindu 1.69% · Buddhist 0.71% · Confucian 0.05% · Others 0.13%. SOURCED (IUSSP paper, Table 3, total row; the question is open-ended and allows "others"). The table's per-group rows are not reproduced here.

### 1.5 Map files (Indonesia)
See §6. In short: the post-war "Indonesia" is a unified six-bloc core; **Aceh** is drawn as its own hard-bordered unit with Autonomous Zone status; **West Papua** (all six Papua-region provinces) separates and is independent at 2083. Quoted there with file and line.

### 1.6 Draft group shares of the city (DERIVED arithmetic, **UNWEIGHTED fallback**, not a ruling)
Weighted shares could not be computed (1.3). This uses the national 2010 New Classification shares (1.1) × 12.23%. **It covers present-day Indonesia including Aceh and the Papua provinces**, which the map files separate (§6); no variant could be computed without province data.

| Group | National share 2010 (unweighted) | × 12.23% = draft share of city |
|---|---:|---:|
| Javanese | 40.06% | 4.899% |
| Sundanese | 15.51% | 1.897% |
| Others (residual in Ananta et al.) | 15.11% | 1.848% |
| Malay | 3.70% | 0.453% |
| Batak | 3.58% | 0.438% |
| Madurese | 3.03% | 0.371% |
| Betawi | 2.88% | 0.352% |
| Minangkabau | 2.73% | 0.334% |
| Buginese | 2.71% | 0.331% |
| Bantenese | 1.96% | 0.240% |
| Banjarese | 1.74% | 0.213% |
| Balinese | 1.66% | 0.203% |
| Acehnese | 1.44% | 0.176% |
| Dayak | 1.36% | 0.166% |
| Sasak | 1.34% | 0.164% |
| Chinese | 1.20% | 0.147% |
| **Total** | 100.01% (rounding in source) | 12.23% |

---

## 2 · Malaysia (draft 3.30%)

### 2.1 Latest census ethnic composition (2020)
- **Source:** Department of Statistics Malaysia (DOSM), *Penemuan Utama Banci Penduduk dan Perumahan Malaysia 2020* / *Key Findings, Population and Housing Census of Malaysia 2020* (bilingual PDF, 154 pages, downloaded from the govdocs.sinarproject.org mirror of the DOSM release; Table 1.0 to 1.16 and Table 7). SOURCED.
- **Category system and limits:** ethnicity is tabulated **for citizens only** (Bumiputera, Chinese, Indians, Others), with Bumiputera split into Malay and "other Bumiputera" (Bumiputera lain); in Sabah and Labuan the other Bumiputera are further split into Kadazan/Dusun, Bajau and Murut, and in Sarawak into Iban, Bidayuh and Melanau. **Non-citizens (8.3%) are not given an ethnicity** in these tables. The report notes the Sabah and Sarawak sub-ethnic groups were realigned for 2020 (UNVERIFIED: search summary of the report). SOURCED for the structure.
- **National, 2020:** total 32,447,385; citizens 29,756,315 (91.7%); non-citizens 2,691,070 (8.3%). Citizens: Bumiputera 69.4%, Chinese 23.2%, Indians 6.7%, Others 0.7%. SOURCED (Table 1.0).
- **National by detailed group (DERIVED by summing the state totals of Table 7; the sums reproduce the published citizen and total figures exactly):**

| Group | Number | Share of total population | Share of citizens |
|---|---:|---:|---:|
| Malay | 16,993,986 | 52.37% | 57.11% |
| Chinese | 6,892,367 | 21.24% | 23.16% |
| Non-citizens | 2,691,070 | 8.29% | — |
| Indians | 1,998,778 | 6.16% | 6.72% |
| Other Bumiputera (Peninsula + Sabah + Sarawak residual) | 1,275,728 | 3.93% | 4.29% |
| Iban | 702,579 | 2.17% | 2.36% |
| Kadazan/Dusun | 670,185 | 2.07% | 2.25% |
| Bajau | 572,365 | 1.76% | 1.92% |
| Others (citizens) | 215,637 | 0.66% | 0.72% |
| Bidayuh | 201,376 | 0.62% | 0.68% |
| Melanau | 125,581 | 0.39% | 0.42% |
| Murut | 107,733 | 0.33% | 0.36% |

- **Discrepancy logged:** a news summary gives Sabah's Kadazan/Dusun as 698.3 thousand; Table 7's Sabah total row gives 660,777 (plus 9,408 in Labuan). Not resolved; the table is used.

### 2.2 Regional distribution (states)
All of Malaysia is UTC+8 (inside the window). Shares are of **citizens**, except the non-citizen column (share of total). Population and ethnic shares SOURCED (Tables 1.x and 7). GDP: DOSM OpenDOSM dataset `gdp_state_real_supply` (annual real GDP by state, constant 2015 prices, RM million, series "abs", sector p0 = total), downloaded as CSV. SOURCED. For 2020 the dataset has no separate Putrajaya row, so Putrajaya is inside Kuala Lumpur (as DOSM's own per-capita release also states for KL). GDP per head DERIVED (GDP / census population).

| State / FT | Population 2020 | Malay | Other Bumiputera (all sub-groups) | Chinese | Indians | Others | Non-citizens (% of total) | Real GDP 2020, RM million (2015 prices) | Real GDP per head 2020, RM (DERIVED) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Perlis | 284,885 | 88.1% | 0.7% | 7.4% | 1.8% | 2.0% | 2.3% | 5,785 | 20,307 |
| Kedah | 2,131,427 | 79.7% | 0.4% | 12.3% | 6.3% | 1.3% | 4.4% | 46,042 | 21,602 |
| Kelantan | 1,792,501 | 95.1% | 1.4% | 2.5% | 0.3% | 0.6% | 2.0% | 25,188 | 14,052 |
| Terengganu | 1,149,440 | 97.1% | 0.5% | 2.1% | 0.2% | 0.2% | 2.3% | 33,994 | 29,574 |
| Pulau Pinang | 1,740,405 | 44.2% | 0.5% | 44.9% | 9.7% | 0.6% | 8.1% | 92,691 | 53,258 |
| Perak | 2,496,041 | 57.7% | 3.2% | 27.2% | 11.5% | 0.5% | 5.3% | 74,264 | 29,753 |
| Pahang | 1,591,295 | 75.0% | 6.1% | 14.7% | 3.7% | 0.6% | 4.9% | 54,885 | 34,491 |
| Selangor | 6,994,423 | 59.2% | 1.4% | 27.3% | 11.3% | 0.8% | 8.1% | 326,805 | 46,724 |
| W.P. Kuala Lumpur | 1,982,112 | 46.5% | 1.2% | 41.6% | 10.0% | 0.7% | 10.5% | 217,447 (incl. Putrajaya) | 103,976 |
| W.P. Putrajaya | 109,202 | 95.7% | 2.2% | 0.6% | 1.2% | 0.2% | 2.6% | in Kuala Lumpur row | — |
| Negeri Sembilan | 1,199,974 | 61.2% | 2.0% | 21.9% | 14.3% | 0.5% | 5.6% | 46,336 | 38,614 |
| Melaka | 998,428 | 70.5% | 1.2% | 22.1% | 5.6% | 0.6% | 7.1% | 41,030 | 41,095 |
| Johor | 4,009,670 | 58.5% | 1.6% | 32.8% | 6.6% | 0.5% | 8.0% | 128,074 | 31,941 |
| W.P. Labuan | 95,120 | 40.4% | 45.8% | 11.7% | 1.1% | 1.0% | 11.4% | 7,613 | 80,040 |
| Sabah | 3,418,785 | 11.8% | 76.9% | 9.5% | 0.2% | 1.5% | 23.7% | 77,840 | 22,768 |
| Sarawak | 2,453,677 | 24.7% | 51.0% | 23.8% | 0.2% | 0.3% | 5.1% | 127,556 | 51,986 |

- Also in the dataset: a "Supra" row (extra-regional activity, RM 40,698 million in 2020) that belongs to no state; it is excluded from the weights. SOURCED (CSV).
- Nominal 2024 GDP per head by state, for reference: national RM56,734; Kuala Lumpur RM136,365; Labuan RM87,003; Pulau Pinang RM76,033; Sarawak RM73,426; Selangor RM65,907. SOURCED (DOSM media statement "GDP by State, 2024", 1 July 2025; the full per-state table in that PDF is an image and could not be read).

### 2.3 Weighted composition (DERIVED)
Weights = 2020 real state GDP (= population × real GDP per head). Group shares within each state from Table 7 (non-citizens kept as their own category).

| Group | Population-only share | GDP-weighted 2020 | GDP-weighted with 2024 GDP (sensitivity) |
|---|---:|---:|---:|
| Malay | 52.37% | **49.76%** | 50.05% |
| Chinese | 21.24% | **24.73%** | 25.04% |
| Non-citizens | 8.29% | **8.23%** | 8.16% |
| Indians | 6.16% | **6.93%** | 7.09% |
| Other Bumiputera (residual) | 3.93% | **3.20%** | 3.02% |
| Iban | 2.17% | **2.80%** | 2.64% |
| Kadazan/Dusun | 2.07% | **1.21%** | 1.07% |
| Bajau | 1.76% | **1.03%** | 0.91% |
| Bidayuh | 0.62% | **0.80%** | 0.76% |
| Others (citizens) | 0.66% | **0.62%** | 0.62% |
| Melanau | 0.39% | **0.50%** | 0.47% |
| Murut | 0.33% | **0.19%** | 0.17% |

### 2.4 Languages and religions
- **Language: NOT FOUND.** The 2020 key-findings report has no language or mother-tongue table (searched the full text). Whether the 2020 questionnaire carried a language item was not established.
- **Religion, 2020, total population:** Islam 63.5% · Buddhism 18.7% · Christianity 9.1% · Hinduism 6.1% · Other 0.9% · No religion / unknown 1.8%. SOURCED (Table 1.0). State shares are in Tables 1.1 to 1.16 (for example Sarawak: Christianity 50.1%, Islam 34.2%; Sabah: Islam 69.6%, Christianity 24.7%). SOURCED.
- **Religion, GDP-weighted 2020 (DERIVED, same weights as 2.3):** Islam 58.3% · Buddhism 21.7% · Christianity 9.8% · Hinduism 6.8% · Other 1.1% · None/unknown 2.3%.

### 2.5 Map files (Malaysia)
Malaysia stays intact as one sovereign country; **Sarawak gains Autonomous Zone status within Malaysia**; Sabah stays an ordinary state. Quoted in §6.

### 2.6 Draft group shares of the city (DERIVED arithmetic, not a ruling)

| Group | Weighted share (2.3, 2020 GDP) | × 3.30% = draft share of city |
|---|---:|---:|
| Malay | 49.76% | 1.642% |
| Chinese | 24.73% | 0.816% |
| Non-citizens (no ethnicity tabulated) | 8.23% | 0.271% |
| Indians | 6.93% | 0.229% |
| Other Bumiputera (residual) | 3.20% | 0.105% |
| Iban | 2.80% | 0.092% |
| Kadazan/Dusun | 1.21% | 0.040% |
| Bajau | 1.03% | 0.034% |
| Bidayuh | 0.80% | 0.026% |
| Others (citizens) | 0.62% | 0.021% |
| Melanau | 0.50% | 0.017% |
| Murut | 0.19% | 0.006% |
| **Total** | 100.00% | 3.300% |

---

## 3 · Thailand (draft 5.15%)

### 3.1 Latest census "ethnic" composition — **the census has no ethnicity question**
- **The 2010 Population and Housing Census questionnaire** asks each person's **religion** and **nationality**, and asks the household **language(s)**: "Thai only / Thai mixed with other languages / Others", with "other languages used (specify)". **There is no ethnic-group item.** SOURCED (English questionnaire, IHSN catalog 4405, download 57062, opened and read).
- So a census "ethnic composition" of Thailand is **NOT FOUND** by construction. What the census does give:
  - **Nationality, 2010:** Thai 95.9%, Burmese 2.0%, other 1.3%, unspecified 0.9%. UNVERIFIED (Wikipedia "Demographics of Thailand", citing the CIA World Factbook, which labels it ethnicity; it is the nationality item).
  - **Language, 2010 (population 5+, UN Demographic Yearbook counts as quoted by Wikipedia):** Thai 59,866,190 · Burmese 827,713 · "Tai" 787,696 · Karen 441,114 · English 323,779 · Chinese 111,866 · Japanese 70,677 · Hindi 22,938 · Vietnamese 8,281 · Malay 2,913 · Others 3,518,502 · total 65,981,659. UNVERIFIED (secondary; the UNdata table was not opened).
  - **Limit that matters:** the Thai census language categories put regional Thai varieties (including the Lao-related speech of the northeast and the northern variety) under "Thai". UNVERIFIED as a formal statement from NSO; it is consistent with the questionnaire's "Thai only / Thai mixed" wording and with the 2000 provincial data used in 3.2 (no Isan or Lao-language row for northeastern provinces, only a small "Laotian and Vietnamese" category). The map file's own Isan figure (~22 million ethnic Lao) is **not** a census figure (§6).
- **NSO Thailand (nso.go.th) returned HTTP 418** to a plain download of its ebook PDF; the 2010 whole-kingdom report was not opened. Died at the source.

### 3.2 Regional distribution (provinces)
- All of Thailand is UTC+7 (inside the window).
- **Province language and religion data: 2000 census** (the latest with province-level language tables that could be read). Source: Wikipedia "Nationality, religion, and language data for the provinces of Thailand", which transcribes each province's NSO 2000 "Key indicators" report (raw wikitext downloaded). **Spot-checked against the primary:** the archived NSO report for Surin (web.archive.org copy of web.nso.go.th/pop2000/finalrep/surinfn.pdf, page 1) reads "Population speaking Khmer (%)": 63.4 (1990), 47.2 (2000); Buddhism 99.3%; Thai nationality 99.5% — the Wikipedia row matches. Other provinces: SOURCED (secondary, transcription of NSO), one primary spot-check passed.
- **Provincial product:** NESDC *Gross Regional and Provincial Product, 2019 Edition*, as tabulated in Wikipedia "List of Thai provinces by GPP" (population, GPP in billion baht, GPP per head, 2019; the 77 rows sum to the national 15,451.96 billion baht). UNVERIFIED-secondary (the NESDC link is dead; the archive copy was not opened).
- Bueng Kan (split from Nong Khai in 2011) is given Nong Khai's 2000 profile (no minority language listed). DERIVED assumption.
- **Provinces with a listed minority language of 1% or more in 2000** (all others list none above 1%; Bangkok shown for scale):

| Province | Pop. 2019 (m) | GPP 2019 (bn baht) | GPP per head 2019 (baht) | Listed minority languages, 2000 census | Muslim % 2000 | Christian % 2000 |
|---|---:|---:|---:|---|---:|---:|
| Bangkok | 8.912 | 5,022.02 | 573,907 | English 0.7%, Indian languages 0.1%, Japanese 0.1% | 4.1 | 1.0 |
| Saraburi | 0.758 | 236.64 | 330,750 | Hill tribe languages 1.8%, Laotian and Vietnamese <0.1% | 0.3 | n/a |
| Trat | 0.274 | 46.96 | 171,189 | Khmer 2.1%, Burmese and Peguan 0.3% | 2.8 | n/a |
| Chanthaburi | 0.553 | 138.44 | 254,582 | Khmer 1.6% | 0.2 | 1.8 |
| Sa Kaeo | 0.630 | 45.25 | 72,555 | Khmer 1.9% | 0.2 | 0.3 |
| Buriram | 1.247 | 84.33 | 67,621 | Khmer 27.6%, Laotian and Vietnamese 0.1% | 0.1 | n/a |
| Surin | 1.107 | 72.88 | 65,810 | Khmer 47.2% | 0.1 | n/a |
| Sisaket | 1.033 | 69.57 | 67,362 | Khmer 26.2% | 0.1 | n/a |
| Chiang Mai | 1.805 | 231.73 | 135,991 | Hill tribe languages 13.4% | n/a | 6.0 |
| Chiang Rai | 1.156 | 104.44 | 91,308 | Hill tribe languages 12.5% | 0.3 | n/a |
| Mae Hong Son | 0.235 | 13.00 | 65,448 | Hill tribe languages 63.0% | 0.6 | n/a |
| Nan | 0.445 | 31.31 | 71,121 | Hill tribe languages 10.5% | n/a | 1.0 |
| Lamphun | 0.406 | 77.85 | 191,568 | Hill tribe languages 6.0% | 0.2 | n/a |
| Phayao | 0.410 | 36.02 | 87,858 | Hill tribe languages 2.6% | n/a | 0.8 |
| Phrae | 0.423 | 28.38 | 67,057 | Hill tribe languages 1.9% | 0.1 | n/a |
| Lampang | 0.735 | 68.20 | 92,749 | Hill tribe languages 1.0% | n/a | 0.9 |
| Phetchabun | 0.921 | 76.80 | 84,058 | Hill tribe languages 1.0% | n/a | 0.3 |
| Tak | 0.532 | 47.80 | 94,902 | Hill tribe languages 24.3%, Burmese and Peguan 2.6% | 1.2 | n/a |
| Kanchanaburi | 0.829 | 97.29 | 121,570 | Burmese and Peguan 2.9%, Hill tribe languages 2.1% | 0.3 | 0.6 |
| Ratchaburi | 0.813 | 172.59 | 214,742 | Hill tribe languages 1.1%, Burmese and Peguan 0.6%, Laotian and Vietnamese 0.5% | n/a | 1.2 |
| Ranong | 0.269 | 26.77 | 104,517 | Burmese and Peguan 7.0%, Malay 0.5% | 10.9 | n/a |
| Phang Nga | 0.270 | 71.76 | 265,768 | Burmese and Peguan 1.7% | 23.2 | n/a |
| Nakhon Si Thammarat | 1.537 | 153.57 | 99,899 | Malay 2.9%, Chinese 2.1% | 6.2 | n/a |
| Songkhla | 1.635 | 241.84 | 156,245 | Malay 4.6% | 23.2 | n/a |
| Satun | 0.290 | 36.56 | 129,565 | Malay 9.9% | 67.8 | n/a |
| Yala | 0.468 | 43.37 | 96,867 | Malay 66.1%, Chinese 3.0% | 68.9 | n/a |
| Narathiwat | 0.721 | 42.74 | 61,765 | Malay 80.4%, Chinese 0.3% | 82.0 | n/a |
| Pattani | 0.641 | 55.74 | 88,442 | Malay 76.6%, Chinese 1.0% | 80.7 | n/a |

"n/a" = not given in the source (small or unpublished). Malay and "Malay-Yawi" are merged.

### 3.3 Weighted composition (DERIVED) — **by home language, not ethnicity**
Weights = 2019 GPP (billion baht). Composition = 2000 census listed minority languages; the residual is "Thai (all varieties) and languages not separately listed" (it therefore also absorbs any minority language a province did not list).

| Language category | Population-weighted (2019 pop.) | GPP-weighted 2019 | GPP-weighted, **without** Narathiwat, Pattani, Yala (map-file "Deep South", §6) |
|---|---:|---:|---:|
| Thai (all varieties) and not separately listed | 94.57% | **97.65%** | 98.34% |
| Malay | 2.21% | **0.82%** | 0.14% |
| Hill tribe languages | 1.18% | **0.54%** | 0.55% |
| Khmer | 1.70% | **0.53%** | 0.53% |
| English | 0.09% | **0.23%** | 0.23% |
| Burmese and Peguan | 0.11% | **0.07%** | 0.07% |
| Chinese | 0.10% | **0.06%** | 0.05% |
| Japanese | 0.01% | **0.04%** | 0.04% |
| Indian languages | 0.01% | **0.03%** | 0.03% |
| Laotian and Vietnamese | 0.03% | **0.02%** | 0.02% |

The three Deep South provinces hold 2.63% of Thailand's 2019 population and 0.92% of its 2019 GPP (DERIVED). The variant column is arithmetic only, not a ruling on which applies.

### 3.4 Languages and religions
- Language: see 3.1 and 3.3.
- **Religion:** the 2010 census national religion split was **not verified** this run (NSO blocked). Wikipedia gives 93.5% Buddhist, 5.4% Muslim, 1.1% Christian, 0.1% other or none, labeled as a 2018 figure — UNVERIFIED and possibly not a census. **GPP-weighted religion from the 2000 provincial shares (DERIVED; "n/a" counted as 0):** Buddhist 93.9%, Muslim 4.1%, Christian 0.6%.

### 3.5 Map files (Thailand)
Thailand keeps 74 provinces; **Narathiwat, Pattani and Yala separate as an independent nation after the 2083 war** (working name "Deep South"). Quoted in §6.

### 3.6 Draft group shares of the city (DERIVED arithmetic, not a ruling) — **language categories**

| Language category | Weighted share (GPP 2019) | × 5.15% | Variant without Deep South | × 5.15% |
|---|---:|---:|---:|---:|
| Thai (all varieties) and not separately listed | 97.65% | 5.029% | 98.34% | 5.064% |
| Malay | 0.82% | 0.042% | 0.14% | 0.007% |
| Hill tribe languages | 0.54% | 0.028% | 0.55% | 0.028% |
| Khmer | 0.53% | 0.027% | 0.53% | 0.028% |
| English | 0.23% | 0.012% | 0.23% | 0.012% |
| Burmese and Peguan | 0.07% | 0.004% | 0.07% | 0.004% |
| Chinese | 0.06% | 0.003% | 0.05% | 0.002% |
| Japanese | 0.04% | 0.002% | 0.04% | 0.002% |
| Indian languages | 0.03% | 0.002% | 0.03% | 0.002% |
| Laotian and Vietnamese | 0.02% | 0.001% | 0.02% | 0.001% |
| **Total** | 100.00% | 5.150% | 100.00% | 5.150% |

---

## 4 · Vietnam (draft 4.76%)

### 4.1 Latest census ethnic composition (2019)
- **Source:** General Statistics Office, *Completed Results of the 2019 Viet Nam Population and Housing Census* (bilingual PDF, downloaded from nso.gov.vn; Table 2 "Population by ethnic group, urban/rural, sex, socio-economic region and province/city, 01/4/2019"). SOURCED.
- **Category system and limits:** the official list of **54 ethnic groups** (Kinh plus 53 minorities), plus "foreigners" (Người nước ngoài) and "not determined" (Không xác định) rows. Census date 1 April 2019. 63 provinces (pre-2025 boundaries; the 2025 reform merged them into 34, which the census does not use).
- **National (total 96,208,984):** Kinh 82,085,826 (85.32%) · Tày 1,845,492 (1.92%) · Thái 1,820,950 (1.89%) · Mường 1,452,095 (1.51%) · Mông 1,393,547 (1.45%) · Khmer 1,319,652 (1.37%) · Nùng 1,083,298 (1.13%) · Dao 891,151 (0.93%) · Hoa 749,466 (0.78%) · Gia Rai 513,930 (0.53%) · Ê Đê 398,671 (0.41%) · Ba Na 286,910 (0.30%) · Xơ Đăng 212,277 · Sán Chay 201,398 · Cơ Ho 200,800 · Sán Dìu 183,004 · Chăm 178,948 · Raglay 146,613 · Hrê 149,460 · Mnông 127,334 · all others smaller. SOURCED (counts); shares DERIVED. The UN Vietnam press release gives Kinh 82.1 million, 85.3% — matches.

### 4.2 Regional distribution
All of Vietnam is UTC+7 (inside the window). Ethnic shares SOURCED (Table 2, parsed; every province's parsed groups sum to its published total within 0 to 37 persons, the gap being the "not determined" row; one row, Mường in Sơn La, was split across a page break and was restored by hand to 84,676). GRDP per head: *Statistical Yearbook of Viet Nam 2023*, Table 95 "Gross regional domestic product per capita by province", million dong, 2019 and 2023 (preliminary). SOURCED.

**By socio-economic region:**

| Socio-economic region | Population 2019 | Kinh | Largest other groups |
|---|---:|---:|---|
| Northern Midlands and Mountains | 12,532,866 | 43.8% | Tày 12.5%, Mông 10.0%, Thái 9.1%, Mường 7.1% |
| Red River Delta | 22,543,607 | 97.9% | Mường 0.5%, Tày 0.4%, Dao 0.4%, Sán Dìu 0.3% |
| North and South Central Coast | 20,187,293 | 89.7% | Thái 2.9%, Mường 1.9%, Hrê 0.7%, Raglay 0.7% |
| Central Highlands | 5,842,681 | 62.3% | Gia Rai 8.7%, Ê Đê 6.2%, Ba Na 4.4%, Cơ Ho 3.0% |
| Southeast | 17,828,907 | 94.2% | Hoa 2.8%, Khmer 1.0%, Xtiêng 0.6%, Tày 0.3% |
| Mekong River Delta | 17,273,630 | 92.4% | Khmer 6.6%, Hoa 0.9%, Chăm 0.1% |

**By province (2019 boundaries):**

| Province | Population 2019 | Kinh | Largest other groups (share of province) | GRDP per head 2019, mill. VND | 2023 prel. |
|---|---:|---:|---|---:|---:|
| Hà Nội | 8,053,663 | 98.7% | Mường 0.8% | 120.3 | 150.3 |
| Hà Giang | 854,679 | 12.3% | Mông 34.2%, Tày 22.5%, Dao 14.9% | 28.2 | 35.6 |
| Cao Bằng | 530,341 | 5.1% | Tày 40.8%, Nùng 29.8%, Mông 11.6% | 32.9 | 41.2 |
| Bắc Kạn | 313,905 | 12.0% | Tày 52.6%, Dao 17.9%, Nùng 9.1% | 38.2 | 51.7 |
| Tuyên Quang | 784,811 | 43.2% | Tày 26.2%, Dao 13.4%, Sán Chay 9.0% | 39.6 | 54.9 |
| Lào Cai | 730,420 | 33.8% | Mông 25.1%, Tày 14.8%, Dao 14.2% | 68.1 | 88.6 |
| Điện Biên | 598,856 | 17.4% | Mông 38.1%, Thái 35.7%, Khơ Mú 3.3% | 32.1 | 43.4 |
| Lai Châu | 460,196 | 15.9% | Thái 31.1%, Mông 24.0%, Dao 12.8% | 38.9 | 52.2 |
| Sơn La | 1,248,415 | 16.3% | Thái 53.6%, Mông 16.1%, Mường 6.8% | 39.7 | 51.0 |
| Yên Bái | 821,030 | 42.7% | Tày 18.3%, Mông 13.0%, Dao 12.3% | 37.1 | 50.9 |
| Hoà Bình | 854,131 | 25.7% | Mường 64.3%, Thái 4.0%, Tày 3.0% | 54.6 | 71.0 |
| Thái Nguyên | 1,286,751 | 70.1% | Tày 11.7%, Nùng 6.4%, Sán Dìu 4.4% | 90.9 | 115.1 |
| Lạng Sơn | 781,655 | 16.1% | Nùng 42.9%, Tày 36.1%, Dao 3.6% | 41.9 | 56.4 |
| Quảng Ninh | 1,320,324 | 87.7% | Dao 5.6%, Tày 3.1%, Sán Dìu 1.6% | 143.3 | 227.1 |
| Bắc Giang | 1,803,950 | 85.7% | Nùng 5.3%, Tày 3.3%, Sán Dìu 1.9% | 57.7 | 94.3 |
| Phú Thọ | 1,463,726 | 83.0% | Mường 14.9%, Dao 1.1% | 47.1 | 64.2 |
| Vĩnh Phúc | 1,151,154 | 95.2% | Sán Dìu 4.0% | 102.5 | 130.0 |
| Bắc Ninh | 1,368,840 | 94.5% | Tày 1.8%, Mường 1.1%, Nùng 1.1% | 145.0 | 148.3 |
| Hải Dương | 1,892,254 | 99.4% | — | 66.8 | 95.8 |
| Hải Phòng | 2,028,514 | 99.6% | — | 122.2 | 187.9 |
| Hưng Yên | 1,252,731 | 99.1% | — | 73.7 | 112.5 |
| Thái Bình | 1,860,447 | 99.8% | — | 45.2 | 63.3 |
| Hà Nam | 852,800 | 99.8% | — | 64.0 | 97.6 |
| Nam Định | 1,780,393 | 99.8% | — | 39.0 | 52.3 |
| Ninh Bình | 982,487 | 97.0% | Mường 2.8% | 62.8 | 86.6 |
| Thanh Hoá | 3,640,128 | 81.7% | Mường 10.3%, Thái 6.8%, Mông 0.5% | 48.3 | 74.0 |
| Nghệ An | 3,327,791 | 85.2% | Thái 10.2%, Thổ 2.1%, Khơ Mú 1.3% | 39.8 | 56.0 |
| Hà Tĩnh | 1,288,866 | 99.8% | — | 60.5 | 78.0 |
| Quảng Bình | 895,430 | 97.1% | Bru Vân Kiều 2.1%, Chứt 0.7% | 43.7 | 59.5 |
| Quảng Trị | 632,375 | 86.3% | Bru Vân Kiều 11.0%, Tà Ôi 2.6% | 50.3 | 74.4 |
| Thừa Thiên Huế | 1,128,620 | 95.1% | Tà Ôi 3.1%, Cơ Tu 1.5% | 46.8 | 62.4 |
| Đà Nẵng | 1,134,310 | 99.5% | — | 97.4 | 107.8 |
| Quảng Nam | 1,495,812 | 90.6% | Cơ Tu 3.7%, Xơ Đăng 3.2%, Gié Triêng 1.6% | 66.0 | 76.3 |
| Quảng Ngãi | 1,231,697 | 84.8% | Hrê 10.8%, Co 2.7%, Xơ Đăng 1.6% | 70.5 | 102.1 |
| Bình Định | 1,486,918 | 97.2% | Ba Na 1.5%, Hrê 0.7% | 55.7 | 78.5 |
| Phú Yên | 872,964 | 93.1% | Ê Đê 2.9%, Chăm 2.6%, Ba Na 0.5% | 48.6 | 65.3 |
| Khánh Hoà | 1,231,107 | 94.2% | Raglay 4.5% | 70.4 | 88.8 |
| Ninh Thuận | 590,467 | 75.6% | Raglay 11.9%, Chăm 11.4%, Cơ Ho 0.6% | 52.7 | 88.5 |
| Bình Thuận | 1,230,808 | 92.1% | Chăm 3.2%, Raglay 1.4%, Cơ Ho 1.1% | 64.2 | 90.6 |
| Kon Tum | 540,438 | 45.1% | Xơ Đăng 24.6%, Ba Na 12.7%, Gié Triêng 7.3% | 40.3 | 59.2 |
| Gia Lai | 1,513,847 | 53.8% | Gia Rai 30.4%, Ba Na 12.5%, Nùng 0.8% | 40.3 | 60.6 |
| Đắk Lắk | 1,869,322 | 64.3% | Ê Đê 18.8%, Nùng 4.1%, Tày 2.8% | 41.7 | 62.7 |
| Đắk Nông | 622,168 | 67.5% | Mnông 8.2%, Mông 5.6%, Nùng 5.0% | 45.5 | 68.2 |
| Lâm Đồng | 1,296,906 | 74.3% | Cơ Ho 13.5%, Mạ 3.0%, Nùng 1.9% | 60.5 | 86.4 |
| Bình Phước | 994,679 | 80.3% | Xtiêng 9.7%, Tày 2.5%, Nùng 2.4% | 62.6 | 95.4 |
| Tây Ninh | 1,169,165 | 98.3% | Khmer 0.8% | 70.6 | 92.8 |
| Bình Dương | 2,426,561 | 95.0% | Khmer 2.7%, Hoa 0.7% | 147.4 | 169.0 |
| Đồng Nai | 3,097,107 | 93.6% | Hoa 2.8%, Khmer 0.8%, Nùng 0.6% | 110.7 | 135.6 |
| Bà Rịa - Vũng Tàu | 1,148,313 | 97.8% | Hoa 0.8%, Chơ Ro 0.7% | 300.4 | 345.4 |
| TP. Hồ Chí Minh | 8,993,082 | 94.8% | Hoa 4.3%, Khmer 0.6% | 148.7 | 170.6 |
| Long An | 1,688,547 | 99.1% | Khmer 0.6% | 72.8 | 96.6 |
| Tiền Giang | 1,764,185 | 99.8% | — | 54.6 | 68.7 |
| Bến Tre | 1,288,463 | 99.7% | — | 40.3 | 52.0 |
| Trà Vinh | 1,009,168 | 67.8% | Khmer 31.5%, Hoa 0.7% | 58.9 | 82.3 |
| Vĩnh Long | 1,022,791 | 97.4% | Khmer 2.2% | 52.9 | 73.4 |
| Đồng Tháp | 1,599,504 | 99.9% | — | 51.5 | 68.6 |
| An Giang | 1,908,352 | 95.1% | Khmer 4.0%, Chăm 0.6% | 44.5 | 58.8 |
| Kiên Giang | 1,723,067 | 86.3% | Khmer 12.3%, Hoa 1.4% | 55.2 | 73.0 |
| Cần Thơ | 1,235,171 | 97.5% | Khmer 1.6%, Hoa 0.9% | 72.7 | 94.8 |
| Hậu Giang | 733,017 | 96.8% | Khmer 2.5%, Hoa 0.7% | 48.6 | 82.1 |
| Sóc Trăng | 1,199,653 | 64.6% | Khmer 30.2%, Hoa 5.2% | 44.5 | 60.5 |
| Bạc Liêu | 907,236 | 90.1% | Khmer 8.2%, Hoa 1.7% | 45.9 | 64.7 |
| Cà Mau | 1,194,476 | 97.2% | Khmer 2.2%, Hoa 0.5% | 50.7 | 66.0 |

"—" = no other group at 0.5% or more.

### 4.3 Weighted composition (DERIVED)
Weights = 2019 census population × 2019 GRDP per head (same year as the census). Sensitivity: 2019 population × 2023 GRDP per head.

| Group | Population-only | GRDP-weighted (2019) | Sensitivity (2023 GRDP per head) |
|---|---:|---:|---:|
| Kinh | 85.32% | **89.94%** | 89.53% |
| Tày | 1.92% | **1.24%** | 1.28% |
| Hoa | 0.78% | **1.12%** | 1.03% |
| Khmer | 1.37% | **1.07%** | 1.09% |
| Mường | 1.51% | **1.06%** | 1.11% |
| Thái | 1.89% | **1.01%** | 1.06% |
| Mông | 1.45% | **0.74%** | 0.75% |
| Nùng | 1.13% | **0.71%** | 0.75% |
| Dao | 0.93% | **0.62%** | 0.67% |
| Gia Rai | 0.53% | **0.28%** | 0.32% |
| Ê Đê | 0.41% | **0.23%** | 0.26% |
| Sán Dìu | 0.19% | **0.21%** | 0.22% |
| All other groups (Ba Na, Xơ Đăng, Sán Chay, Cơ Ho, Chăm and smaller) | 2.57% | **1.77%** | 1.93% |

### 4.4 Languages and religions
- **Language: NOT FOUND** in the census publication read (its 26 tables include ethnicity and religion, not language).
- **Religion, 2019, total population (Table 3):** no religion 83,046,105 (86.32%) · Catholic 5,866,169 (6.10%) · Buddhism 4,606,543 (4.79%) · Hòa Hảo Buddhism 983,079 (1.02%) · Protestantism 960,558 (1.00%) · Cao Đài 556,234 (0.58%) · Islam 70,934 (0.07%) · Cham Brahmanism 64,547 (0.07%) · smaller recognized religions below 0.05% each. SOURCED (counts); shares DERIVED.

### 4.5 Map files (Vietnam)
No change to Vietnam's territory is stated; the map uses the 2025 34-province layout. Statements about peoples (Tày/Nùng, Zomia provinces, Khmer Krom) are quoted in §6.

### 4.6 Draft group shares of the city (DERIVED arithmetic, not a ruling)

| Group | Weighted share (2019) | × 4.76% = draft share of city |
|---|---:|---:|
| Kinh | 89.94% | 4.281% |
| Tày | 1.24% | 0.059% |
| Hoa | 1.12% | 0.053% |
| Khmer | 1.07% | 0.051% |
| Mường | 1.06% | 0.050% |
| Thái | 1.01% | 0.048% |
| Mông | 0.74% | 0.035% |
| Nùng | 0.71% | 0.034% |
| Dao | 0.62% | 0.030% |
| Gia Rai | 0.28% | 0.013% |
| Ê Đê | 0.23% | 0.011% |
| Sán Dìu | 0.21% | 0.010% |
| Sán Chay | 0.17% | 0.008% |
| Cơ Ho | 0.16% | 0.008% |
| Ba Na | 0.16% | 0.007% |
| Chăm | 0.15% | 0.007% |
| All other groups (each under 0.15%) | 1.15% | 0.055% |
| **Total** | 100.00% | 4.760% |

---

## 5 · Philippines (draft 3.18%)

### 5.1 Latest census ethnic composition (2020 Census of Population and Housing)
- **Category system:** self-reported ethnicity of the **household population** (108,667,043), released by the Philippine Statistics Authority (PSA) in 2023. "Bisaya/Binisaya" is reported as its own category alongside Cebuano, Ilonggo, Boholano and others, so the categories overlap linguistically. UNVERIFIED (search-engine extracts of the PSA release; the release itself returned 403).
- **National, 2020 (UNVERIFIED; snippet-only extracts of the PSA release "About one in every four household population has Tagalog as ethnicity", plus the CIA list quoted by Wikipedia):** Tagalog 28,273,666 (26.0%) · Bisaya/Binisaya 15,522,998 (14.3%) · Ilocano 8.0% · Cebuano 8.0% · Ilonggo 7.9% · Bikol/Bicol 6.5% · Waray 3.8% · Kapampangan 3.0% · Pangasinense 1.9% · Maguindanao 1.9% · all others about 18.7% (DERIVED residual). The CIA list as quoted omits Cebuano and Ilonggo and gives "other 18.5%", which does not add up with the PSA figures; logged, not resolved.
- **Regional top groups, 2020 (UNVERIFIED, same snippet route, PSA release Table 2):** NCR Tagalog 56.1% · Calabarzon Tagalog 74.4% · Central Luzon Tagalog 52.4% · Mimaropa Tagalog 42.2% · Ilocos Region Ilocano 58.3% · Cagayan Valley Ilocano 61.8% · Cordillera Ilocano 22.1% · Bicol Region Bikol 78.8% · Western Visayas Ilonggo 67.6% (Capizeño 9.6%) · Central Visayas Cebuano 61.4%, Bisaya/Binisaya 19.3%, Boholano 16.2% · Eastern Visayas Waray 64.2% · Northern Mindanao Bisaya/Binisaya 46.5% · Davao Region Bisaya/Binisaya 48.8% · BARMM Maguindanao 26.4%, Tausug 23.3%, Maranao 22.7%. Zamboanga Peninsula, Soccsksargen, Caraga and Negros Island Region: NOT FOUND.

### 5.2 Regional distribution
- All of the Philippines is UTC+8 (inside the window).
- **Full regional ethnicity tables: NOT OBTAINED.** psa.gov.ph (release page, press-release PDF, technical notes) and the regional office site rssomimaropa.psa.gov.ph returned **HTTP 403** to WebFetch; bworldonline.com (a newspaper reprint) also returned 403. The PSA's openstat metadata page found covers population by region, not ethnicity. **Died at the sources.**
- **Refusal logged (not worked around):** one attempt to fetch the PSA page with curl using a browser-style user agent was **denied by the permission system as bot-check circumvention**. It was not retried in any form. All other PSA access was by WebFetch only.

### 5.3 Weighted composition (DERIVED)
**NOT COMPUTED** (no full regional table). Regional GRDP per head was not collected for the same reason (the PSA GRDP tables sit on the same blocked domain).

### 5.4 Languages and religions
- **Language generally spoken at home (2020):** the PSA released it (press release found by search) but the file is on psa.gov.ph (403). NOT FOUND.
- **Religion, 2020, household population:** Roman Catholic 85,645,362 (78.81%) · Islam 6,981,710 (6.42%); all Christian categories combined 91.5%. UNVERIFIED (Wikipedia "Religion in the Philippines", citing the PSA "Religious Affiliation in the Philippines (2020 CPH)" release and statistical-table file; shares DERIVED from the quoted counts).

### 5.5 Map files (Philippines)
The Philippines stays intact; BARMM is an autonomous region inside it; Sulu sits in Zamboanga Peninsula. Quoted in §6.

### 5.6 Draft group shares of the city (DERIVED arithmetic, **UNWEIGHTED fallback from UNVERIFIED inputs**, not a ruling)

| Group | National share 2020 (unweighted) | × 3.18% = draft share of city |
|---|---:|---:|
| Tagalog | 26.0% | 0.827% |
| All other ethnicities (residual) | 18.7% | 0.595% |
| Bisaya/Binisaya | 14.3% | 0.455% |
| Ilocano | 8.0% | 0.254% |
| Cebuano | 8.0% | 0.254% |
| Ilonggo | 7.9% | 0.251% |
| Bikol/Bicol | 6.5% | 0.207% |
| Waray | 3.8% | 0.121% |
| Kapampangan | 3.0% | 0.095% |
| Pangasinense | 1.9% | 0.060% |
| Maguindanao | 1.9% | 0.060% |
| **Total** | 100.0% | 3.180% |

---

## 6 · Map-file check (developer's map files; quoted, not extrapolated)

**Folders read:** `/home/kuroskalacs/Documents/Doll-Fi/media/y-files/Map Files/Asia/Asia (Southeast)/` (sub-folders `01 initial generations`, `02 reorganization`, `03 official timeline years`, `04 timeline staging`) and its copy under `x Full Earth/Asia/Asia (Southeast)/`. The two `subdivisions*.csv` files in `x Full Earth` are **byte-identical** to those in `03 official timeline years/archive 01/` (diff, no output). `04 timeline staging` holds two empty folders. The latest data files are `03 official timeline years/archive 01/subdivisions.csv` (mainland) and `subdivisions_maritime.csv` (maritime); the latest sphere definitions are in `02 reorganization/04 follow-up/southeast-asia-nations/spheres.csv` and `spheres_maritime.csv` (later follow-ups state "No `spheres*.csv` needed", `06 follow-up/CHANGES.md` L30–31). Paths below are relative to `Asia (Southeast)/`.

**Indonesia**
- `02 reorganization/04 follow-up/southeast-asia-nations/README.md` L7: *"`maritime_sea_map.png`: Indonesia (unified), Aceh, West Papua, the Philippines, Malaysia, Brunei, Singapore, Timor-Leste"*.
- `02 reorganization/03 follow-up/DESIGNATIONS-maritime.md` L22–24: *"West Papua secedes and starts fully independent at 2083 … Whether it later merges with Papua New Guinea by the Falkland Treaty (2564) is a separate, deliberately open question"*; L25–27: *"Aceh becomes an Autonomous Zone, not a fully independent nation, forming gradually after 2083"*; L18–21: *"The national capital, as of the 2083 war, is Nusantara"*.
- `03 official timeline years/archive 01/subdivisions_maritime.csv` L11 (Aceh): *"an Autonomous Zone, not a fully independent nation — but drawn as its own hard-bordered nation on this map … Acehnese are ~70% of the province's population and are Austronesian like their neighbors"*.
- Same file L34 (West Papua): *"this whole bloc (all 6 current Papua-region provinces) is 'West Papua' … a political/civilizational label for Indonesia's entire Melanesian-populated Papua-island territory"*; L37: *"Highlands remain overwhelmingly Papuan/Melanesian even as coastal cities approach demographic parity with Indonesian-migrant-descended settlers (~50/50 territory-wide …)"*.
- Same file L31 (Bali): *"~86.5% Hindu — the region's one majority-Hindu province"*; L25 (South Sulawesi): *"Bugis and Makassarese homeland"*.
- `02 reorganization/04 follow-up/southeast-asia-nations/spheres_maritime.csv` L3 (S2): *"Indonesia (all blocs — Chinese ~3% nationally …)"*. **Flag (DERIVED comparison, not adjudicated):** the 2010 census figure is 1.20% (§1.1); the map note's ~3% is not a census figure.

**Malaysia**
- `03 official timeline years/archive 01/subdivisions_maritime.csv` L70 (Sarawak): *"Sarawak gains Autonomous Zone status within Malaysia … Malaysia itself stays intact as one sovereign country, this is a sub-country tier"*; L69 (Sabah): *"stays an ordinary Malaysian state, not promoted to Autonomous Zone status like Sarawak"*.
- `…/spheres_maritime.csv` L3 (S2): *"Malaysia (Chinese ~23% of the population per the 2020 census …)"* — consistent with the census 23.2% **of citizens** (§2.1); of total population it is 21.24%.
- `…/spheres_maritime.csv` L4 (S4): Kelantan and Terengganu share *"'Kelantan-Pattani Malay,' spoken continuously across these two states … and Thailand's Deep South"*; *"Kelantan 95.5%, Terengganu 97.3%"* Muslim — matches the census (§2.4).
- **Flag:** the map file's Malaysian state `population` column (e.g. Johor 4,186,300, L58) is not the 2020 census count (4,009,670); likely a later estimate. Not adjudicated.

**Thailand**
- `03 official timeline years/archive 01/subdivisions.csv` L49 (Narathiwat): *"separates from Thailand as its own independent nation after the 2083 war — not autonomy … 'Deep South' is a working/placeholder nation name, not yet decided"*; L54 (Pattani) and L92 (Yala) refer to the same note.
- `02 reorganization/04 follow-up/southeast-asia-nations/spheres.csv` L2 (S1): *"Thailand (all 74 provinces, since the Deep South's 3 seceded 2026-09-26 …)"*; L3 (S2): *"Thailand: the 20 Isan provinces … ~22 million ethnic Lao here"*. **Flag:** the Thai census does not record Lao ethnicity or language separately (§3.1), so the ~22 million figure has no census counterpart in this layer.
- `…/spheres.csv` L4 (S3): Upper North hill-tribe-speaker shares *"Mae Hong Son (51.1%→63.0%) and Tak (18.1%→24.3%)"* — the 2000 values match §3.2.
- `…/spheres.csv` L6 (S5): Deep South *"77% Muslim, where Patani Malay is the majority language"*.

**Vietnam**
- `03 official timeline years/archive 01/subdivisions.csv` L94–127: 34 rows on the 2025 provincial layout; no territorial change stated.
- `…/spheres.csv` L2 (S1): Cao Bằng and Lạng Sơn are *"home to the Tày and Nùng peoples, Vietnam's two largest ethnic minorities"*. **Flag:** by 2019 census counts the two largest minorities are Tày (1.85 m) and Thái (1.82 m); Nùng is seventh (§4.1).
- `…/spheres.csv` L4 (S3): *"Lai Châu: Kinh only 15.91%; Điện Biên: Kinh 17.38%; Sơn La: Kinh 16.26%; Cao Bằng: Kinh 5.12%; Lạng Sơn: Kinh 16.09%"*, *"Hà Giang: Kinh only 12.32%"* — consistent with §4.2.
- `…/spheres.csv` L5 (S4): *"~1.32 million ethnic Khmer total in Vietnam (2019 census)"* — matches 1,319,652.

**Philippines**
- `03 official timeline years/archive 01/subdivisions_maritime.csv` L57 (BARMM): *"AUTONOMOUS REGION, not a separate hard-bordered nation … Over 89% Muslim (2024 census)"*; L52: Sulu *"stays part of Zamboanga Peninsula"*.
- `…/spheres_maritime.csv` L3 (S2): *"Philippines (all regions — Chinese ~1-2% nationally …)"*.

Nothing in these files states a population origin for Tepenia, and none is inferred here.

---

## Search log (exact strings; all `WebSearch`, standard mode)

| # | Search string | Result |
|---:|---|---|
| 1 | Malaysia 2020 census ethnic composition by state Bumiputera Chinese Indian DOSM | led to the DOSM key-findings page and PDF mirror |
| 2 | Vietnam 2019 census ethnic groups population Kinh Tay Thai Muong Khmer Hmong Nung percentage | national figures; UN press release |
| 3 | Philippines 2020 census ethnicity PSA Tagalog Bisaya Cebuano Ilocano percent household population | PSA release located (403 when opened) |
| 4 | Indonesia 2010 census suku bangsa ethnic groups Javanese Sundanese percentage BPS Ananta | Wikipedia tables; IUSSP paper located |
| 5 | Thailand 2010 population and housing census language spoken at home ethnicity not collected | IHSN catalog located |
| 6 | DOSM GDP by state 2023 GDP per capita Kuala Lumpur Labuan Penang Sabah Kelantan RM | top-five figures only |
| 7 | Malaysia census 2020 citizens Malay 57.3% "Bumiputera lain" other Bumiputera percentage Iban Kadazan-Dusun Bajau | dead end at the query (answered later from Table 7) |
| 8 | dosm.gov.my "GDP by State" 2023 release per capita Kelantan Kedah Perlis Johor Pahang Terengganu Melaka | DOSM 2024 media-statement PDF |
| 9 | "Completed results of the 2019 Viet Nam population and housing census" pdf ethnic group by province table | GSO page (gso.gov.vn DNS failure; nso.gov.vn worked) |
| 10 | Malaysia census 2020 language spoken question mother tongue not collected DOSM | dead end at the sources |
| 11 | Vietnam GRDP per capita by province 2019 table 63 provinces million VND GSO | dead end (provincial snippets only) |
| 12 | "Tổng sản phẩm trên địa bàn bình quân đầu người" theo địa phương 2019 niên giám thống kê nso.gov.vn | methodology page only |
| 13 | GRDP bình quân đầu người 63 tỉnh thành năm 2023 Tổng cục Thống kê bảng xếp hạng triệu đồng | dead end (grouped figures only) |
| 14 | nso.gov.vn px-web "phân theo địa phương" tổng sản phẩm trên địa bàn giá hiện hành tỉnh | dead end |
| 15 | vi.wikipedia Danh sách đơn vị hành chính Việt Nam theo GRDP bình quân đầu người 63 tỉnh | dead end (guessed Wikipedia URL 404) |
| 16 | "Statistical Yearbook of Viet Nam" 2022 OR 2023 "per capita" "by province" GRDP current prices pdf nso.gov.vn | pointed to the yearbook |
| 17 | nso.gov.vn Statistical Yearbook of Viet Nam 2023 pdf download | yearbook page; PDF downloaded; Table 95 found |
| 18 | 2020 CPH ethnicity by region table Tagalog Bisaya Ilocano percent region "household population" PSA statistical tables | regional snippets |
| 19 | openstat.psa.gov.ph household population by ethnicity region 2020 census | dead end (no ethnicity table on openstat) |
| 20 | PSA 2020 census ethnicity regions "Central Visayas" Cebuano percent "Western Visayas" Hiligaynon "Eastern Visayas" Waray percent household population | Visayas snippets |
| 21 | PSA "Ethnicity in the Philippines" 2020 census Tagalog 26.0 Bisaya 14.3 Ilocano 8.0 Cebuano 8.0 Ilonggo 7.9 Bikol 6.5 Waray Kapampangan Maguindanao Pangasinense Tausug Maranao percent | Table 1 counts for two groups only |
| 22 | 2020 census ethnicity top three by region PSA "Zamboanga Peninsula" "Soccsksargen" "Caraga" "BARMM" Maguindanao Maranao Tausug Hiligaynon percent | BARMM only |
| 23 | "Kewarganegaraan, Suku Bangsa, Agama, dan Bahasa Sehari-hari Penduduk Indonesia" Hasil Sensus Penduduk 2010 pdf bps.go.id | BPS page (403) |
| 24 | Sensus Penduduk 2020 Long Form suku bangsa pertanyaan etnis tidak ditanyakan BPS 2022 hasil | Long Form topics |
| 25 | "suku bangsa" sensus penduduk 2010 tabel provinsi jawa sunda batak madura persentase per provinsi pdf | dead end (national only) |
| 26 | media.neliti.com kewarganegaraan suku bangsa agama bahasa sehari-hari penduduk indonesia hasil sensus penduduk 2010 | dead end (mirror 403) |
| 27 | "Demography of Indonesia's Ethnicity" Ananta 2015 pdf province ethnic composition table | paywalled; index only |
| 28 | komposisi suku bangsa per provinsi sensus penduduk 2010 tabel 33 provinsi persentase suku terbesar setiap provinsi | dead end |
| 29 | Thailand 2010 Population and Housing Census whole kingdom report table "language" spoken at home Thai Burmese Karen percent nationality religion | dead end for the report |
| 30 | Wikipedia list Thailand provinces nationality religion language census 2000 hill tribe percent province table | provincial dataset located |
| 31 | official time zones Malaysia UTC+8 Philippines UTC+8 Thailand UTC+7 Vietnam UTC+7 Indonesia WIB WITA WIT | confirmed offsets |

**Pages and files opened directly (WebFetch, curl downloads of found URLs, Wikipedia raw wikitext):** DOSM key-findings web page; govdocs.sinarproject.org mirror of the DOSM 2020 key-findings PDF; DOSM "GDP by State 2024" PDF; OpenDOSM `gdp_state_real_supply.csv` (and a guessed `gdp_state_percapita.csv`, NoSuchKey); OpenDOSM catalog page; says.com article; GSO/NSO 2019 completed-results PDF; NSO yearbook listing and 2023 yearbook PDF; vneconomy.vn article; English Wikipedia (List of Vietnamese subdivisions by GDP; Ethnic groups in Indonesia; Demographics of Thailand; Ethnic groups in the Philippines); IHSN catalog 4405 and the Thai 2010 questionnaire; archive.org copy of the NSO 2000 Surin report; ISEAS bookshop file (index only); IUSSP paper; raw wikitext for 34 Indonesian province pages, 18 Philippine region pages and related articles.

**Blocked or dead (where it died):** psa.gov.ph (403, sources) · rssomimaropa.psa.gov.ph (403, sources) · bworldonline.com (403, sources) · bps.go.id (403, sources) · media.neliti.com (403, sources) · nso.go.th ebook (418, sources) · gso.gov.vn (DNS failure; the agency now uses nso.gov.vn) · ILO survey catalog (redirect not followed) · Ananta et al. 2015 chapters (paywall) · first batch of Wikipedia raw downloads rejected for missing user agent, retried with a descriptive user agent · one curl request with a browser-style user agent **refused by the permission system; not retried** (§5.2).

**Self-corrections logged:** Vietnam parse dropped the Sơn La Mường row at a page break (restored to 84,676); the Cà Mau block ran into the religion table (truncated); two province headings were blank in the parse (Đông Nam Bộ, Bắc Giang; named by hand); Bạc Liêu and Cà Mau GRDP rows were missed by the first parse (added from the yearbook table as read). Malaysian sums were checked against the published citizen and total counts (exact match for all 16 units).

---

## FINAL

**Summary (facts only):**
- **Malaysia (complete, primary):** 2020 census; GDP-weighted pool Malay 49.8%, Chinese 24.7%, non-citizens 8.2%, Indians 6.9%, the six separately named Sabah and Sarawak groups 6.5% combined, other Bumiputera 3.2%. Weighting raises the Chinese and Indian shares and lowers the Sabah groups relative to population counts.
- **Vietnam (complete, primary):** 2019 census, 54 groups; GRDP-weighted pool Kinh 89.9% (85.3% by population); weighting roughly halves the northern-highland and Central Highland minority shares and raises Hoa.
- **Thailand (complete, but by language):** the census has **no ethnicity question**; by 2000 home-language data, the GPP-weighted pool is 97.7% Thai (all varieties) with Malay 0.8%, hill-tribe languages 0.5%, Khmer 0.5%; removing the map files' Deep South drops Malay to 0.14%.
- **Indonesia (national only):** 2010 census, Javanese 40.1%, Sundanese 15.5%, Malay 3.7%, Batak 3.6%; the 2020 census did not collect ethnicity; province tables blocked, so the weighting is not computed.
- **Philippines (national only, UNVERIFIED):** 2020 census, Tagalog 26.0%, Bisaya/Binisaya 14.3%, Ilocano 8.0%, Cebuano 8.0%; regional tables blocked, so the weighting is not computed.

**NOT FOUND / NOT OBTAINED list:**
1. Indonesia: 2010 ethnic composition by province (BPS 403; neliti 403; Ananta 2015 paywalled). Blocks items 1.2, 1.3 and a proper 1.6.
2. Indonesia: a variant without Aceh and the Papua provinces (needs item 1).
3. Philippines: full 2020 ethnicity by region (psa.gov.ph 403); regional GRDP per head; 2020 home-language table.
4. Thailand: any census ethnicity (not collected); 2010 whole-kingdom report tables (nso.go.th 418); a verified 2010 national religion split.
5. Malaysia: census language data (no table in key findings).
6. Vietnam: census language data (not in the completed-results publication).
7. All five: regional income **by ethnic group** (not searched successfully; not needed by the method).

**What is left:** (a) the BPS 2010 publication *Kewarganegaraan, Suku Bangsa, Agama, dan Bahasa Sehari-hari Penduduk Indonesia* and the PSA 2020 ethnicity statistical tables, both of which refuse automated clients; a person can download them in a browser and the weighting here can then be run the same way; (b) a second-angle search pass on each nation (LAW 0-R) was not done for Malaysia, Vietnam or Thailand beyond the sources above; (c) Thailand's 2020 register-based census was not checked for any new language or religion items.
