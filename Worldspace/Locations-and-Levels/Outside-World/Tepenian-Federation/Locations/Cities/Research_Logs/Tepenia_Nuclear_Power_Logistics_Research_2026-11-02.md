# Nuclear power logistics for Antarctic cities: research file (Unit R6, 2026-11-02)

**Started:** 2026-11-02 17:40 (shell clock). **Ended:** 2026-11-02 17:47 (shell clock, as reported by `date`; the clock may not reflect the full tool latency).

**Scope.** Facts only, no recommendation, no ranking, no design. The developer asks which Antarctic cities or clusters could be powered by nuclear plants, depending on (a) whether nuclear power is logistically feasible in Antarctica and (b) how far electricity, heat, fuel and equipment can be moved. Reference technology is real-world 2020s. Labels: **SOURCED** (read at the source page or document in this session, including PDFs I extracted with `pdftotext`), **DERIVED** (my arithmetic on sourced figures, working shown), **UNVERIFIED** (seen only in a search-result summary, recalled, or inferred), **NOT FOUND** (searched, queries logged). Note on method: every claim taken only from a WebSearch result summary (not from a fetched page) is labeled UNVERIFIED, even where several results agreed. The fictional nation's rule (explosives and waste disposal banned; reactors not banned; spent fuel leaves the territory) is the developer's premise; it is not tested here against any text other than the real Article V.

## PROGRESS

- [x] Q1 Reactor types and sizes (PM-3A, Lomonosov, Bilibino, RITM-200, microreactors, NuScale, remote-community projects; units for 100 MW, 500 MW, 1 GW, 5 GW)
- [x] Q2 Fuel and waste logistics (fuel per year, shipping, PM-3A decommissioning, Article V, Madrid Protocol, Bilibino/Lomonosov practice, diesel comparison with arithmetic)
- [~] Q3 Siting constraints (partly: EPZ rule, air cooling, permafrost foundations, frazil ice; seismic/ice-shelf, Norilsk, Greenland, Svalbard cooling NOT FOUND)
- [x] Q4 Transmission range (HVAC/HVDC losses, subsea cables, Arctic lines, district heat lengths; some per-voltage loss figures NOT FOUND)
- [x] Q5 Other applications (process heat, desalination, floating plants, powerships)
- [x] Retry items: Antarctic power line longer than a few km on ice (still NOT FOUND); station fuel liters per person (still NOT FOUND, partial station totals found)

---

## Q1. Reactor types and sizes for remote, cold, small-grid use

### 1.1 Table of units

All "MWe" are as stated by the source named. Where sources differ, both are given.

| Unit | MWe | MWt | Reload interval | Footprint / transport | Status | Label |
|---|---|---|---|---|---|---|
| **PM-3A (McMurdo)** | 1.75 (air-cooled PWR, also heat and distilled water) | not stated | first refueling 1964 | steel tanks in gravel under a lead shield; 25-person operating team | operated 1962 to Sept 1972; removed by 1979 | SOURCED (Energy Central, navyhistory.au, Wikipedia, AJUS) |
| **Akademik Lomonosov (2 x KLT-40S)** | 2 x 35 gross, 2 x 32 net; "70 MWe plus 586 GJ/hr of heat" (WNA) | 140 to 150 each | 3 to 4.5 years onsite (WNA); 3 to 3.5 years (Rosatom newsletter) | barge hull 21,500 t, 144 m x 30 m | grid December 2019; commercial May 2020; first refueling campaign done 2024 | SOURCED (WNA Russia page; Rosatom newsletter) |
| **Bilibino EGP-6 (4 units)** | 12 gross, 11 net each (48 gross) | 62 each | not stated | land plant on permafrost | units shut down December 2025; decommissioning about 8 years | SOURCED (WNN Dec 2025; WNA SMR page text; "62 MWt" is UNVERIFIED, from a search summary of Wikipedia) |
| **RITM-200S floating unit (Baimskaya)** | 2 reactors, 106 per floating unit ("50 MWe each, about 20% enrichment" in WNA) | 175 per reactor (UNVERIFIED) | 5 to 7 years (WNA); "10 to 12 years at a service base" per other sources (WNA) | 19,100-t hulls (first two) | first reactor made May 2026, second September 2026 (WNA text); plan about 300 MWe from 2028 | SOURCED (WNA Russia page) |
| **RITM-200N (land, Ust-Kuyga, Yakutia)** | 55 each, two units | 190 | 5 to 6 year fuel cycle; 60-year life | containment 6 x 6 x 15.5 m | planned 2030; construction licence April 2023 | SOURCED (WNA Russia page) |
| **Vityaz (NIKIET)** | 1 | 6 | not stated | four modules of up to 60 t | no date given | SOURCED (WNA SMR page) |
| **Project Pele (BWXT, US DoD)** | 1 to 10 MWe threshold (WNA); 1 to 5 MWe (DOE page); 1.5 MWe (search summary, UNVERIFIED) | not stated | at least 3 years (WNA) | under 40 t; "20-foot shipping containers", reactor module by truck (DOE); WNA says transportable by truck, ship and C-17 | WNA: TRISO production finished Nov 2025, core stacking finished June 2026; DOE page (Sept 2024): could operate 2026 | SOURCED (WNA SMR page; DOE page) |
| **eVinci (Westinghouse)** | 5 | 15 | "eight or more full-power years" | "Fully factory-assembled and shipped in containers by rail, barge, or truck"; "less than a 2-acre footprint"; TRISO at 19.75% enrichment | still under development; zero-power criticality test at NCERC reported in 2026 (UNVERIFIED, search summary); commercial deployment "mid-2030s" (UNVERIFIED) | SOURCED (Westinghouse page for specs) |
| **Radiant Kaleidos** | 1.2 commercial design; test unit 1 (UNVERIFIED) | not stated | not stated | "packaged in a single shipping container"; trailer from California to Idaho (UNVERIFIED) | in transit to INL DOME in Aug 2026; no result seen for the test (UNVERIFIED) | UNVERIFIED (Radiant page returned 403; figures from search summary) |
| **Oklo Aurora at Eielson AFB** | up to 5 MWe (WNN 2021, vendor not named there); Oklo selected, notice of intent June 2025 (UNVERIFIED) | not stated | not stated | n/a | "as soon as 2027" (WNN); Air Force and DLA notice of intent to Oklo (WNA SMR page text) | SOURCED for 5 MWe and 2027 (WNN); award details UNVERIFIED |
| **NuScale module** | 77 gross (uprated) | 250 | 24-month reload not confirmed in any result | n/a | uprated design application to NRC (2023); partner target 2029 (search summary) | UNVERIFIED (search summaries only) |
| **Toshiba 4S (Galena, Alaska)** | 10 | not stated | fuel "purported to last 30 years", then the whole reactor removed and replaced | buried underground; needs no cooling water | proposed 2004 to about 2009; never built; abandoned 2011 per search summary | SOURCED (UAF blog); "abandoned 2011" UNVERIFIED |
| **Chalk River MMR (Global First Power / USNC)** | about 5 (15 MWt) per one source; CNSC lists up to 45 MWt | 15 to 45 | not stated | n/a | CNSC lists project as paused; parent Ultra Safe Nuclear filed Chapter 11 in Oct 2024 | UNVERIFIED (CNSC page returned 404; figures from search summary) |
| **BN-350 (Aktau, Kazakhstan)** | 52 net / 90 gross (WNA database via search) | 1,000 | n/a | n/a | 1973 to April 1999; also desalination | UNVERIFIED (search summary; sources conflict, one says 350 MWe) |
| **MH-1A Sturgis (floating)** | 10 | not stated | n/a | converted Liberty ship hull towed to Panama | Panama Canal Zone 1968 to about 1975/76 | UNVERIFIED (search summary) |

Other sourced context:
- WNA lists GREM (2 MWe per twin-unit plant, 25 years without refueling), ATGOR, and an unnamed Arctic mobile unit as Russian small concepts. SOURCED (WNA SMR page fragment).
- "The Air Force's Eielson base has its own 15 MWe coal-fired plant" (WNA SMR page); WNN says the coal plant "can produce up to 25 MWe but typically runs at 13-15 MWe" and "uses up to 800 tonnes of coal daily". SOURCED.
- A concept paper in *Progress in Nuclear Energy* proposes a very small modular reactor for McMurdo-Scott, South Pole and South Shetland stations. No official nuclear plan or environmental impact assessment for an Antarctic station was found. UNVERIFIED (search summary).

### 1.2 Units needed for 100 MW, 500 MW, 1 GW and 5 GW

**DERIVED.** Working: units = ceiling(target MWe / MWe per unit). This is nameplate only. It ignores spares, outages, refueling downtime, and the fact that net is below gross; a sourced example of the gap is 70 MWe gross against about 64 MWe net for the Lomonosov barge. The unit sizes used are those in 1.1.

| Unit (MWe used) | 100 MW | 500 MW | 1 GW | 5 GW |
|---|---|---|---|---|
| PM-3A-size (1.75) | 58 | 286 | 572 | 2,858 |
| Pele-size (1.5) | 67 | 334 | 667 | 3,334 |
| Kaleidos-size (1.2) | 84 | 417 | 834 | 4,167 |
| eVinci / Eielson-size (5) | 20 | 100 | 200 | 1,000 |
| Galena 4S (10) | 10 | 50 | 100 | 500 |
| Bilibino EGP-6 unit (11 net) | 10 | 46 | 91 | 455 |
| One KLT-40S reactor (32 net) | 4 | 16 | 32 | 157 |
| Lomonosov-size barge (64 net) | 2 | 8 | 16 | 79 |
| RITM-200N (55) | 2 | 10 | 19 | 91 |
| NuScale module (77 gross) | 2 | 7 | 13 | 65 |
| RITM-200S floating unit (106) | 1 | 5 | 10 | 48 |

### 1.3 Status facts that bear on "exists or in demonstration now"

- Only two pieces of this table have produced commercial power in a cold, remote setting: PM-3A (Antarctic, 1962 to 1972) and the Bilibino and Lomonosov plants (Chukotka). SOURCED.
- The Lomonosov plant "moored in Murmansk for fuel loading May 2018, fuel loading completed October 2018, grid connection December 2019, commercial operation May 2020"; more than 1.2 TWh by May 2026. SOURCED (WNA).
- Cost figures from WNA for Lomonosov: contract RUR 9.98 billion; completion cost put at RUR 7.631 billion; Rosenergoatom said the pilot plant cost RUR 21.5 billion and a second would be about RUR 18 billion. SOURCED.
- RITM-200S floating unit contract: price RUR 6.45/kWh "(about 8 US cents/kWh), indexed for inflation"; barge contract $226 million for the first two hulls. SOURCED (WNA).
- A UAF author calls Alaska a niche market ("small," "remote," "low temperature") and says remote deployments are seen as higher risk by vendors; siting in a remote community like Galena "was different in almost every respect from any other plant" the NRC had licensed. SOURCED (UAF blog).
- Microreactor vendor timelines in these sources were still moving in 2026 (Kaleidos slipped from spring to August 2026 per a search summary; Chalk River paused). UNVERIFIED.

---

## Q2. Fuel and waste logistics

### 2.1 Fuel per year, shown

**Large LWR reference (SOURCED, nuclear-power.com):** for a 3,000 MWt reactor "annual enriched uranium: about 25 tonnes", natural uranium about 250 t, fuel inventory about 165 t, fissile consumption about 1,005 kg U-235 per year (320-day cycle). Fissioning 1 g of fissile material gives about 1 MWd of heat. A 3,000 MWt reactor at about 33% efficiency is the 1,000 MWe reactor in the NRC's reference definition (NRC Table S-3 page names a "model 1000-MW(e) light-water reactor" but gives no tonnage; SOURCED but empty on this point).

**Scaling to the targets (DERIVED, linear scaling at the same 25 t per GWe-year):**

| Average electric power | Enriched fuel loaded per year |
|---|---|
| 100 MWe | 2.5 t |
| 500 MWe | 12.5 t |
| 1 GWe | 25 t |
| 5 GWe | 125 t |

Caveat: small reactors using TRISO or higher enrichment have different mass per MWh; no per-tonne annual figure for KLT-40S, RITM-200, eVinci or Pele was found (NOT FOUND, see search log). The scaling above is the large-LWR rate only.

**Diesel for the same energy (DERIVED).** Conversion inputs:
- PM-3A's own Navy record: "13.48 kwh per gallon" derived from actual McMurdo diesel plant operations in 1967 (AJUS, Du Bay 1973). SOURCED. 13.48 kWh per gallon / 3.7854 L = **3.56 kWh per liter**.
- Check against first principles: 38.6 MJ/L / 3.6 = 10.7 kWh/L fuel energy; at 35% = 3.75 kWh/L (search-summary figures, UNVERIFIED). Practical small-generator range quoted: 0.3 to 0.6 L/kWh, i.e. 1.7 to 3.3 kWh/L (UNVERIFIED).
- Density 0.84 kg/L (cluster 0.83 to 0.85, UNVERIFIED).

Working for 100 MWe average: 100 MW x 8,760 h = 876,000 MWh = 876,000,000 kWh. / 3.56 kWh/L = **246 million L**; x 0.84 kg/L = **about 207,000 t of diesel per year**. Results:

| Average power | Energy per year | Diesel at 3.56 kWh/L | Diesel mass (0.84 kg/L) | Enriched uranium (25 t/GWe-yr) |
|---|---|---|---|---|
| 100 MWe | 0.876 TWh | 246 ML | about 207,000 t | 2.5 t |
| 500 MWe | 4.38 TWh | 1,230 ML | about 1.03 million t | 12.5 t |
| 1 GWe | 8.76 TWh | 2,460 ML | about 2.07 million t | 25 t |
| 5 GWe | 43.8 TWh | 12,300 ML | about 10.3 million t | 125 t |

Mass ratio at 1 GWe: 2.07 million t / 25 t = about 83,000 to 1 (DERIVED). The range from the practical-efficiency spread (1.7 to 3.3 kWh/L) moves the 1 GWe diesel figure between about 1.96 and 4.3 million t. For comparison, the same source gives a coal plant of 1,000 MWe burning about 10,000 t of coal per day (SOURCED, nuclear-power.com).

**PM-3A as a check (SOURCED table, DERIVED sums).** AJUS Table 1: electrical energy delivered 1962 to 1972 totaled **60,739 MWh**, diesel-fuel equivalent **4,505 thousand gallons** (60,739,000 kWh / 13.48 = 4.506 million gal, matches). That is about 17.05 ML, or about 14,300 t of diesel at 0.84 kg/L (DERIVED). Average delivered power about 60,739 MWh / (about 10.55 years x 8,760 h) = about 0.66 MW (DERIVED; the first year was partial, so the divisor is approximate). Availability by year ranged from 54% (1972) to 87% (1965). Water distillation by nuclear steam, 1967 to 1972, displaced a further 54 to 83 thousand gallons of diesel per year (AJUS Table 2). In 1972 the plant delivered power 4,706:25 hours, an annual availability of 54%. All SOURCED.

Note on shipping weight: PM-3A displaced about 14,300 t of diesel over its life, and its decommissioning shipped out about 12,000 to 14,000 t of soil (2.3). Both are the same order of tonnage; this is a DERIVED comparison, not a claim by any source.

### 2.2 How fuel is shipped and how often

- **Lomonosov.** Fuel assemblies are made at Elemash (Rosatom), shipped by train to Murmansk, loaded with large equipment on a motor vessel, and sent to Chukotka via the Northern Sea Route. First reactor refueling began late July 2023, maintenance due to finish end of 2023; second reactor 2024. Cartridge-type core, "refueling interval of 3-3.5 years." SOURCED (Rosatom newsletter). WNA: whole plant returns to a shipyard "at the end of a 12-year operating cycle" for a two-year overhaul and used-fuel storage, then returns to service. SOURCED (WNA).
- **Spent fuel at Lomonosov: sources disagree.** Rosatom: "Both fresh and spent fuel is stored on board the FNPP in dedicated isolated rooms" (SOURCED, does not say where it finally goes). A search summary of the plant's own site said spent fuel "will be taken to the special storage facilities in mainland Russia" (UNVERIFIED; fnpp.info did not resolve, DNS failure).
- **RITM-200S floating units.** WNA: the design means "no onboard used fuel storage is required," since refueling happens at a service base; one of four units is held in reserve "for refuelling and maintenance." SOURCED.
- **Tow to site.** Lomonosov left Kola Bay 23 August 2019, towed by the icebreaker Dikson with two support ships; route Murmansk to Pevek about 4,700 km; mooring about 14 September. UNVERIFIED (search summaries). Hull built in St. Petersburg area (Baltiysky Zavod launch June 2010 per WNA). SOURCED.
- **Bilibino spent fuel.** Unit 1 fuel moved to an onsite storage pool; unloading across the site "expected to take about two years." SOURCED (WNN Dec 2025). Removal from site: Sosny study (SOURCED, PDF text) describes options:
  - Sea: ice road to a port near the site, then summer sea transport to a mainland port, then rail. "Each leg is available only about four months a year, so a full cycle takes about two years." Estimated cost about 50 billion roubles including reprocessing at Mayak.
  - Air: from the local airfield to a rail-linked airport; existing runway takes up to 20-t aircraft; Type B(U) overpack about 70 billion roubles including 10 billion for a runway upgrade; Type C overpack about 40 billion roubles.
  - Continued pool storage: about 70 billion roubles (2009 prices) for 50 years.
  - The paper calls de-fuelling an "extremely expensive project" owing to remoteness and the lack of transport infrastructure.
  - Destination "Mayak" for reprocessing and a reprocessing finish around 2042 are UNVERIFIED (search summaries).
- **PM-3A fuel.** Fuel (93% enriched) was delivered; "fuel flown in by helicopter in 55-gallon drums" in one account, with helicopters burning "nearly as much aviation fuel as they carried" (Energy Central, citing a 1978 Bulletin article). SOURCED to that page. Refueling in 1964. SOURCED.

### 2.3 PM-3A decommissioning (what was shipped, when, how, cost)

| Item | Finding | Label |
|---|---|---|
| Shutdown | September 1972 after a shield-water leak between reactor tank and steam generator tank; suspected chloride stress corrosion cracking; 1972 availability 54% | SOURCED (AJUS 1973) |
| Plan | Cannot be entombed in concrete because of the Treaty; dismantled plant plus contaminated ground shipped to the US aboard USNS *Private John R. Towle* | SOURCED (navyhistory.au) |
| Planned vs actual duration | "planned to take three years"; "soil removal ran for nearly six years"; "declared complete in February 1979" | SOURCED (Atomic Insights) |
| Quantity | **"More than 14,000 metric tons of soil"** bulk packed on ships, "fewer than 200 tons" counted radioactive for transport (Atomic Insights). **"12,000 tonnes of irradiated gravel and soil"** (navyhistory.au; Energy Central). Another summary gave 7,700 m3 of irradiated rock and dirt (UNVERIFIED). The sources differ by about 2,000 t | SOURCED, conflict recorded |
| Destination | Atomic Insights and Wikipedia: Port Hueneme Naval Base, California, soil incorporated into asphalt/parking lot. navyhistory.au and Energy Central: "buried in concrete-lined pits in the United States." The sources conflict | SOURCED, conflict recorded |
| Pressure vessel activity | about 40,000 curies in the vessel; about 5 curies in the rest of the plant; soil action level 10 pCi/g; frozen soil "required blasting" | SOURCED (Atomic Insights; the article's view that the action level was misapplied is the author's opinion) |
| Depth dug | about 15 m per Energy Central citing the Bulletin | SOURCED to that page |
| Cost | Construction: Martin Marietta contract $1.4 million, final about $3 million. Congress appropriated $13 million for reactors at McMurdo and two inland bases. **Decommissioning cost: NOT FOUND** (no dollar figure on any fetched page) | SOURCED / NOT FOUND |
| Crew | 25-person Naval Facilities Engineering Command team ran the plant, cited as a cost and closure factor | SOURCED (navyhistory.au; Energy Central) |

Key points as stated: the Navy and its command interpreted the Treaty "to require full removal, including buildings and possibly contaminated soil," and independent consultants kept finding soil above the action level (Atomic Insights). The Cambridge *Polar Record* article "Atomic energy for Antarctica: the rise and fall of Nukey Poo" was blocked (HTTP 403 twice); it is the likely home of precise tonnage and cost figures.

### 2.4 Antarctic Treaty Article V and the Madrid Protocol

- **Article V, SOURCED (treaty text extracted from `documents.ats.aq/recatt/att005_e.pdf`):** "1. Any nuclear explosions in Antarctica and the disposal there of radioactive waste material shall be prohibited. 2. In the event of the conclusion of international agreements concerning the use of nuclear energy, including nuclear explosions and the disposal of radioactive waste material, to which all of the Contracting Parties whose representatives are entitled to participate in the meetings provided for under Article IX are parties, the rules established under such agreements shall apply in Antarctica." The text bans neither reactors nor their use.
- **Madrid Protocol Annex III (waste), UNVERIFIED.** A search summary of the annex text says radioactive materials are among the wastes that must be removed from the Treaty Area by the generator of such waste, for waste generated after entry into force, and that stored waste must be kept "in such a way as to prevent its dispersal into the environment." I could not fetch the annex text (the Indian-hosted copy failed on a certificate mismatch; not worked around).
- **SOURCED (Australian Antarctic Division waste page):** "radioactive materials, are prohibited from import to Antarctica." The same page does not discuss removal of radioactive materials, and says only that countries are obliged to apply waste-management principles and plans. The relation of this import line to reactor fuel is not explained on the page. The fictional nation's rule set differs from the Protocol, so this is context, not a test.
- **Governance commentary (UNVERIFIED, search summaries):** one source says the Protocol "lacks clear guidance" on how its environmental assessment framework applies to controlled nuclear technologies; another says PM-3A shows Article V "does not preclude the use of nuclear reactors in Antarctica."

---

## Q3. Siting constraints in polar conditions

### 3.1 Cooling water and heat rejection

- **Air-cooled reactors exist in cold-remote service.** PM-3A was an "air-cooled" 1.75 MWe PWR (SOURCED, Energy Central, navyhistory.au). Its seawater intake line for the distillation plant corroded and was replaced in a summer with "fiberglass pipe with integrated insulation and heat tapes" (AJUS 1973, SOURCED). The seawater distillation units used nuclear steam.
- **Bilibino:** a LinkedIn post (non-authoritative) says Bilibino is the only nuclear plant in the world with air-cooled condensers. UNVERIFIED. One search summary says the EGP-6 is graphite-moderated with natural circulation and was suitable for permafrost; foundation design not found.
- **Toshiba 4S:** "needed no cooling water" (UAF blog, SOURCED).
- **Sea-ice and frazil effects on seawater intakes, UNVERIFIED (search summaries, mid-latitude cases).** Frazil ice on intake screens has forced a nuclear shutdown at Salem, New Jersey (Delaware River, January 2019); a Lake Michigan plant intake in 8 m of water saw 15 blockage events in two months at air temperatures of -2 to -20 degrees C; a Finnish survey of Gulf of Bothnia seawater-cooled plants recorded frazil and algae blockages; a review concludes heating the intake flow so it is not supercooled is "the most reliable prevention method"; practices include back-flushing, intake heaters and flow reversal. No Arctic or Antarctic sea-ice intake design guidance for nuclear plants was found.
- **Lomonosov at Pevek:** barge-mounted; no intake or ice-protection detail found. A search summary reports that in January 2017 a convoy for the Pevek berth was blocked by heavy ice and two cargo ships wintered near Pevek; Pevek port navigation "is usually closed in November"; the harbor was said to be built "to withstand the tough climatic conditions." UNVERIFIED.
- **Svalbard coal plant (Longyearbyen):** capacity figures conflict (11 MWe plus 20 MWt in one summary; at most 28 MW with 12 MWe and 16 MW heat in another); closed October 2023, replaced by diesel generators; CO2 about 70,000 t/year. Cooling-water details NOT FOUND. UNVERIFIED.

### 3.2 Foundations on permafrost and ice

- **Ross Island wind turbines (SOURCED, power-technology.com):** each turbine stands on eight 13-tonne precast concrete blocks "frozen into permafrost" under a steel eight-legged "spider" foundation, built in New Zealand and shipped because "no concrete plant, aggregate, or fresh water on site" ruled out a gravity pad; work limited to the Antarctic summer, construction over two seasons (began November 2008, opened January 2010). This is a wind precedent, not a reactor.
- **Bilibino** sits in permafrost; a Nunatsiaq News item citing *Nature* puts the plant and grid in an area of high risk from increasing ground instability (UNVERIFIED, search summary). Reactor foundation design NOT FOUND.
- **PM-3A:** reactor in steel tanks "embedded in gravel" (navyhistory.au, SOURCED).
- **Seismic or ice-shelf stability for reactor siting:** NOT FOUND (no source in any query).

### 3.3 Emergency planning zones and remoteness

SOURCED (Morgan Lewis summary of the NRC rule, effective 18 December 2023):
- Large LWR baseline: plume exposure EPZ 10-mile radius; ingestion EPZ 50-mile radius. Reactors under 250 MWt and gas-cooled reactors can apply for smaller zones.
- New 10 CFR 50.160 framework for SMRs (LWRs at 1,000 MWt or less per module) and advanced reactors: scalable, consequence-based EPZ; criterion is the area where public dose "would exceed 10 millisieverts over 96 hours after a release"; if the EPZ does not extend beyond the site boundary, local first responders need not take part in radiological drills.
- Specific EPZ distances for any named SMR were not in the source.

Remoteness and response: PM-3A needed 25 people and had a hydrogen fire in year one that took the reactor out for eight weeks, forcing emergency diesel while ice blocked icebreakers (Energy Central, SOURCED). An NRC pre-application process was opened for a 4S at Galena (UNVERIFIED).

### 3.4 Other Arctic examples

- **Alert (Nunavut):** relies entirely on generators; fuel type unresolved in results (one says jet fuel, job postings say diesel); no annual volumes. UNVERIFIED / NOT FOUND for volumes.
- **Greenland (Qaanaaq, Thule):** no data found. NOT FOUND.
- **Norilsk:** not searched separately (no dedicated query). NOT FOUND.
- **Eielson (Alaska):** coal plant uses up to 800 t of coal per day with 90 days' supply on site and "needs a facility to thaw the coal" (WNN, SOURCED). Base is independent but has a grid connection "useful for frequency control."

---

## Q4. Electricity transmission range

### 4.1 Loss figures

SOURCED (Wikipedia "High-voltage direct current"): "HVDC transmission loss is quoted at 3.5% per 1,000 km versus 6.7% for AC lines at the same voltage"; "a typical loss for an 800 kV UHVDC line is 2.6% over 800 km" (about 3.3% per 1,000 km, DERIVED); break-even distance about 50 km for submarine cables and "perhaps 600-800 km" for overhead lines; for short distances converter losses may exceed an AC line's. The page gives no per-km cost; one 2010 project: €700 million for a 2,000 MW 64 km Spain–France line including a tunnel (about €11 million per km, DERIVED).

SOURCED (ABB slide, DOE 2013 deck): HVDC Light converter station losses fell "from 3% to 1% per converter station since 2000"; the chart of energy losses against distance (0 to 1,000 km, 0 to 10%) has no numeric curve values in the extracted text.

UNVERIFIED (search summaries):
- ABB: 800 kV HVDC Xiangjiaba–Shanghai (2,000 km) losses "under 7%" (about 3.5% per 1,000 km); "At a transmission capacity of 5,000 MW, losses are as low as around 2% per 1,000 km" (attribution unclear); independent estimate about 10% for 2,000 km HVDC and 12% for 500 kV AC at the same length.
- AEP-derived document: per 100 miles at 1,000 MW the total losses for EHV AC lines run roughly 0.5% to 1.1%, columns unlabeled in the scrape; reach at 1,500 MW: 765 kV single circuit about 550 miles (about 885 km), 500 kV about 140 miles (225 km), 345 kV double circuit about 110 miles, 345 kV single circuit about 50 miles (single utility source).
- Hydro-Québec's 735 kV grid: losses "range from 4.5 to 8%" varying with temperature and operating situation. Series compensation used since 1995. Ice-storm 1998: 1,500 towers damaged; 400 km of high-voltage lines rebuilt; an HV-DC de-icer at Lévis rated at 250 MW.
- No per-1,000 km loss figure found for 110, 220 or 765 kV AC specifically. NOT FOUND (queries 4.1a, 4.1b in log).

**Applying the sourced 3.5% and 6.7% per 1,000 km (DERIVED, linear, line only, no converters; same loading assumption as the source):**

| Distance | HVDC line loss at 3.5%/1,000 km | HVDC plus 2 converters at 1% each | AC at 6.7%/1,000 km |
|---|---|---|---|
| 100 km | 0.35% | 2.35% | 0.67% |
| 300 km | 1.05% | 3.05% | 2.0% |
| 400 km | 1.4% | 3.4% | 2.7% |
| 800 km | 2.8% | 4.8% | 5.4% |
| 1,000 km | 3.5% | 5.5% | 6.7% |
| 1,500 km | 5.25% | 7.25% | 10.05% |

The 1%-per-converter figure is the ABB HVDC Light value for recent stations; classic HVDC converter losses are not given in the source. Real loss also depends on loading and conductor size, which the sources do not specify.

### 4.2 Existing long lines and Arctic examples

- **Longest overhead HVDC (SOURCED, Wikipedia list):** Jinping–Sunan 2,090 km, 800 kV, 7,200 MW (2013); Xiangjiaba–Shanghai 1,980 km, 800 kV, 6,400 MW (2010); Hami–Zhengzhou 2,210 km, 800 kV, 8,000 MW (2014). SOURCED (Wikipedia HVDC): Zhundong–Wannan 1,100 kV, 3,400 km, 12 GW, 2018 (the intro gives "over 3,000 km"; the page does not reconcile).
- **Chukotka (Pevek–Bilibino):** two parallel single-circuit **110 kV** overhead lines "each about 500 km" (NEI Magazine, SOURCED); the Russian decree gives two lines totaling 986.9 km (first stage about 490.59 km; UNVERIFIED, search summary); NucNet: "490-km-long," about $36 million earmarked, Bilibino to Pevek (SOURCED). Older lines: Bilibino to Zeliony Mys about 300 km and to Pevek about 400 km at 110 kV (UNVERIFIED). Bilibino supplied about 80% of the isolated Chaun-Bilibino system (UNVERIFIED). The new lines replace an existing 1960 line (UNVERIFIED).
- **Antarctic ice (retry):** the only power-line item found: Ross Island wind farm has "ground-laid cables" to Scott Base and McMurdo, with **no lengths or voltages** on the fetched page (SOURCED); a 150 kW Scott Base load; 60 Hz at McMurdo, 50 Hz at Scott Base through a static frequency converter. Any Antarctic overhead or buried power line longer than a few km: **NOT FOUND** (queries 4.2c, 4.2d). A blog search hit mentioned "1600 km of power lines" at the South Pole, UNVERIFIED and not credible as a length of line.

### 4.3 Subsea power cables

| Link | Route / total length | Subsea | Voltage | Capacity | Cost | Year | Label |
|---|---|---|---|---|---|---|---|
| North Sea Link | 720 km (730 km in text) | not separated | ±515 kV DC | 1,400 MW | est. €2 billion | 2021 | SOURCED (Wikipedia; page inconsistent) |
| Viking Link | 765 km route | 650 km undersea (Wikipedia, via summary); Prysmian "1,250 km of submarine route" cable (two cables) of 1,400 km total | ±525 kV DC | 1,400 MW (summary) | Prysmian contract "close to €700 million" (cables) | commissioning scheduled Dec 2023 | SOURCED (Prysmian) / UNVERIFIED (route split) |
| NordLink | 625 km | 516 km | 500 kV DC | 1,400 MW | est. €1.5 to 2 billion | 2021 | SOURCED (Wikipedia) |
| NorNed | 580 km | 580 km cable | 450 kV | 700 MW | n/a | 2008 | SOURCED (Wikipedia list) |
| Basslink | 370 km | 298 km cable, 72 km pole | 400 kV | 500 MW | n/a | 2006 | SOURCED |
| Cook Strait (Pole 3) | 611 km | 40 km cable, 571 km pole | 350 kV | 735 MW | n/a | 2013 | SOURCED |
| Skagerrak 1+2 / 3 | 230 km | 130 km cable | 250 / 350 kV | 500 / 440 MW | n/a | 1977 / 1993 | SOURCED |
| Fenno-Skan 2 | 303 km | 200 km cable | 500 kV | 800 MW | n/a | 2011 | SOURCED |
| Baltic Cable | 262 km | 250 km | 450 kV | 600 MW | n/a | 1994 | SOURCED |
| SwePol | 245 km | 245 km | 450 kV | 600 MW | n/a | 2000 | SOURCED |
| Estlink 1 | 105 km | 105 km | 150 kV | 350 MW | n/a | 2006 | SOURCED |

**Cost per km (DERIVED, rough, mixed scopes).** Viking Link: €700M / 1,250 km of cable = about €0.56M per cable-km (cable supply and installation contract, includes some land cable); €700M / 765 route-km = about €0.92M per route-km. NordLink: €1.5 to 2 billion / 625 km = €2.4 to 3.2M per route-km (whole project including converters). North Sea Link: €2 billion / 720 km = about €2.8M per route-km. These are project totals; the sources give no per-km cable cost. A project-level cost per kilometer in Antarctic conditions: NOT FOUND.

**Antarctic subsea:** every search hit on Antarctic cables concerned fiber optics (a New Zealand to McMurdo route above 4,900 km; Australian proposals; Chilean pre-feasibility with about 1,600 km base route and 4,100 km full configuration, UNVERIFIED), not power.

### 4.4 District heat transport

- **Haiyang "Warm Nuclear No. 1" (China), SOURCED (WNN):** a **23 km** long-distance pipeline from the Haiyang plant to Haiyang and Rushan, operating from 25 November 2023; the project's **83 km** main network and 11 first-level heat exchange stations cost nearly CNY 4 billion (USD 555 million); 12.5 million m2 supplied and winter needs of about 400,000 people; 4.56 million GJ of heat supplied to date; district heating first delivered November 2020. The plant has two AP1000 units operating.
- **Qinshan (Zhejiang):** first phase commissioned December 2021: 460,000 m2 plus 5,000 m2 of apartments for nearly 4,000 residents of Haiyan County; goal 4 million m2 by 2025 (UNVERIFIED). Pipe length: NOT FOUND.
- **Bilibino:** designed as combined heat and power; each unit supplies Bilibino central heating "up to 25 Gcal/hour" (UNVERIFIED, search summary); plant and town distance and pipe length: **NOT FOUND**. Rated 48 MWe with 78 MWt of heat in one summary (UNVERIFIED).
- **Lomonosov at Pevek:** WNA: "70 MWe plus 586 GJ/hr of heat" (SOURCED); 586 GJ/h / 3,600 s = about 163 MW thermal (DERIVED). A search summary quoted "50 Gcal/h" (UNVERIFIED), which is about 58 MW (DERIVED; the two figures differ by a factor of about 2.8 and the page text does not reconcile them). Heat first delivered to the Pevek city network in June 2020 (title of a fnpp.info news item, UNVERIFIED).
- **Russian district-heat pipe lengths:** the OECD-NEA Sozoniuk presentation on Russian nuclear cogeneration experience returned HTTP 521 (source down; not worked around). NOT FOUND.

---

## Q5. Other nuclear applications that avoid long lines

- **Desalination and process steam, PM-3A:** the plant "provided electricity, heat, and desalinated water" (SOURCED). Water distilled by nuclear energy 1967 to 1972: 1,943; 2,168; 2,647; 1,924; 2,838; 1,857 thousand gallons per year (AJUS Table 2, SOURCED); the plant also supplied the Coast Guard icebreaker *Northwind*, the supply ship *Private John R. Towle* and a drilling project with over 2,000 gallons per week; about 6 million gallons in 1972 (SOURCED).
- **BN-350 (Aktau):** fast reactor with desalination, reported 80,000 to 120,000 m3/day of fresh water across sources, operated 1973 to April 1999; electrical figures conflict (52 net/90 gross vs 130 vs 350 MWe). IAEA reports over 150 reactor-years of nuclear desalination experience. UNVERIFIED (search summaries; IAEA bulletin not fetched).
- **Cogeneration on Lomonosov:** see 4.4 (electric plus heat).
- **Floating nuclear plants as mobile power:** Lomonosov (above); RITM-200S floating units for Baimskaya, four units planned (one in reserve), about 300 MWe from 2028, serviced at a base rather than carrying used fuel (WNA, SOURCED). MH-1A Sturgis: 10 MWe, converted Liberty ship, supplied Panama Canal Zone grid from 1968; decommissioning reported at $34.7 to $51 million, hull towed to Brownsville 2018 (UNVERIFIED).
- **Newer floating proposals (UNVERIFIED, search summaries):** Core Power (UK) with Glosten, barge-based plant for US ports, mid-2030s market entry; Seaborg (Denmark) with Samsung Heavy and KHNP, molten-salt power barge, prototype target 2026 and production from 2028; KRISO and ABS (2024) floating SMR platform study for island areas; China ACP100S floating design paper (2020). No confirmed deployed unit.
- **Conventional (non-nuclear) powerships as a comparison only:** Karadeniz powerships, up to 470 MW per vessel, liquid fuel or gas, deployed in Ghana (December 2017) and Indonesia; Sierra Leone projects from 2017. No remote-coastal-community nuclear use. UNVERIFIED (search summaries).
- **Icebreaker reactors as mobile power:** RITM-200 reactors power the Project 22220 icebreakers (UNVERIFIED); no case of an icebreaker supplying a town was found. NOT FOUND.
- **Microgrid cost reference, diesel displaced by renewables at Ross Island:** three 0.33 MW turbines (0.99 MW) save 463,000 L of diesel per year (11% of Ross Island's electricity fuel); upgrade to three EWT DW54X-1MW turbines plus a battery targets over 90% of Scott Base demand (power-technology SOURCED for 463,000 L; upgrade UNVERIFIED). No capacity factor found.

---

## FINAL

### What the sources support

1. **Reactor operation in Antarctica has precedent** (PM-3A, 1962 to 1972, 1.75 MWe, 93% enriched fuel, 25-person crew, 54% to 87% annual availability) and **Article V's text bans only explosions and waste disposal** (SOURCED). PM-3A displaced about 4.5 million gallons (about 17 ML, about 14,300 t) of diesel over its life (SOURCED/DERIVED).
2. **Small cold-region units do exist and run**: Lomonosov (2 x KLT-40S, about 64 to 70 MWe plus heat, since 2019/2020; refueling every 3 to 4.5 years), Bilibino (4 x 12 MWe, 1974 to 2025). **Microreactors (1 to 5 MWe) are in demonstration, not commercial**: Pele, eVinci, Kaleidos, Oklo; they are designed to ship in containers by truck, rail or barge (eVinci, Pele SOURCED; Kaleidos UNVERIFIED).
3. **Fuel mass is tiny compared with diesel for the same energy**: about 25 t of enriched uranium per GWe-year (large LWR) against about 2.07 million t of diesel (DERIVED, ratio about 83,000:1). A 100 MWe average load is 2.5 t/yr of fuel against about 207,000 t of diesel.
4. **Spent fuel and decommissioning waste are the heavy logistic items**: PM-3A shipped out 12,000 to 14,000 t of soil plus the dismantled plant over six years; Bilibino's removal options were costed at 40 to 70 billion roubles with a two-year, four-months-a-year shipping cycle; the RITM-200S design avoids onboard storage by servicing at a base.
5. **Transmission**: HVDC about 3.5% per 1,000 km versus 6.7% for AC at equal voltage, converter stations about 1% each (HVDC Light); subsea HVDC links of 580 to 765 km exist at 700 to 1,400 MW (NorNed, NordLink, North Sea Link, Viking); Chukotka runs two 110 kV lines of about 490 to 500 km each for a small isolated grid. Heat pipelines: 23 km is the longest clearly sourced nuclear district-heat pipe (Haiyang).
6. **Emergency planning zones for SMRs are now consequence-based** (10 mSv in 96 hours), and may stop at the site boundary.

### What the sources do not support (conflicts and gaps in the evidence)

- Total PM-3A decommissioning cost, and a single agreed tonnage and destination (12,000 vs 14,000 t; asphalt at Port Hueneme vs concrete-lined pits).
- Where Lomonosov's spent fuel finally goes (onboard storage vs shipped to mainland).
- Commercial availability or a delivered price for any microreactor.
- Any claim that a nuclear plant has been sited on an ice shelf or sea-ice coast of Antarctica other than PM-3A on rock at McMurdo.

### NOT FOUND (queries in the log)

- Annual fuel tonnes for KLT-40S, RITM-200, eVinci, Pele and Kaleidos (not found in any fetched page).
- Decommissioning cost of PM-3A (Cambridge article blocked).
- Seismic and ice-shelf stability criteria for reactor siting.
- Arctic or Antarctic sea-ice intake design for nuclear or large thermal plants; Svalbard plant cooling; Norilsk; Greenland (Qaanaaq, Thule); Alert fuel volumes.
- Loss per 1,000 km for 110, 220, 500 and 765 kV AC from a primary source; transmission cost per km.
- Any power line longer than a few km on Antarctic ice (retry failed again); lengths of the Ross Island cables.
- Fuel liters per person at stations (retry): only station and program totals found, below.
- Bilibino plant-to-town heat pipe length; Russian district-heat pipe lengths (source down).
- Madrid Protocol Annex III exact text (not fetched).

### Fuel liters per person (retry result, UNVERIFIED, search summaries)

Australian Antarctic operations used roughly 6.4 to 7.1 megaliters of fuel per year across 2015-16 to 2019-20; SANAE IV about 297,872 L of Special Antarctic Blend diesel per year for electricity; Comandante Ferraz (Brazil) 358,985 L of diesel in 2011 (about 983.5 L/day); Casey consumption rose after a year when a fuel resupply failed. No per-person figure. The AAD State of Environment indicator page (403) was the likely source.

---

## Summary (under 250 words)

Reactors in cold, remote service have real precedent: PM-3A at McMurdo (1.75 MWe, 1962 to 1972) and Russia's Bilibino (4 x 12 MWe, to 2025) and Akademik Lomonosov (about 64 to 70 MWe plus heat, since 2019). Article V's text bans explosions and waste disposal, not reactors. Microreactors of 1 to 5 MWe (eVinci, Pele, Kaleidos, Oklo) are designed to ship in containers but are still in demonstration; 100 MW needs about 20 five-MWe units, 1 GW about 200, or 10 floating RITM-200S-class units.

Fuel is light: about 25 t of enriched uranium per GWe-year against about 2.07 million t of diesel (ratio about 83,000 to 1, derived). The heavy loads are waste and decommissioning: PM-3A shipped out 12,000 to 14,000 t of soil over six years; Bilibino spent-fuel removal was costed at 40 to 70 billion roubles with a two-year, short-season shipping cycle.

Transmission: HVDC about 3.5% loss per 1,000 km (AC 6.7% at the same voltage), converters about 1% each; subsea HVDC of 580 to 765 km at 700 to 1,400 MW exists; Chukotka runs two 110 kV lines of about 490 to 500 km. The longest clearly sourced nuclear heat pipe is 23 km (Haiyang).

Still NOT FOUND: PM-3A decommissioning cost, reactor annual fuel masses for small units, ice-shelf or seismic siting criteria, Arctic sea-ice intake design, any Antarctic power line longer than a few km, and liters per person.

---

## SEARCH LOG

Tool names: WS = WebSearch, WF = WebFetch, BASH = shell (pdftotext on downloaded PDFs). Results: hit, partial, miss. "Died at" gives where a dead end failed.

### Searches (WS)

| # | Query | Result |
|---|---|---|
| 1 | PM-3A McMurdo nuclear power plant decommissioning removal cost tons soil shipped | partial (no cost) |
| 2 | Akademik Lomonosov floating nuclear power plant KLT-40S 2x35 MWe fuel refueling interval spent fuel return | hit |
| 3 | Bilibino nuclear power plant EGP-6 11 MWe decommissioning spent fuel Chukotka | hit |
| 4 | Westinghouse eVinci microreactor 5 MWe 15 MWt shipped in containers 8 years refueling heat pipe status 2026 | hit |
| 5 | Oklo Aurora Powerhouse 15 MWe Eielson Air Force Base microreactor status 2026 fuel | partial (15 MWe not confirmed) |
| 6 | NuScale VOYGR 77 MWe module 250 MWt refueling every 24 months NRC design approval uprate | partial (no refueling interval) |
| 7 | PM-3A Nukey Poo McMurdo 1.8 MW fuel oil saved gallons per year 1962 1972 shutdown cracks removal 1979 12,000 tons | partial; led to AJUS table |
| 8 | Madrid Protocol Annex III waste disposal and waste management radioactive removal from Antarctic Treaty area text "radioactive" | partial (summary only) |
| 9 | Bilibino nuclear plant district heating Bilibino town heat supply pipeline length reactors cogeneration 1974 | partial (no pipe length) |
| 10 | Qinshan nuclear district heating Haiyang "Warm Nuclear No. 1" pipeline length km Shandong households heating | hit |
| 11 | tonnes of enriched uranium fuel loaded per year 1000 MWe light water reactor 20 to 27 tonnes annual fuel requirement spent fuel per year | hit |
| 12 | diesel fuel energy content MJ per liter 38.6 MJ/L density 0.84 kg/L generator efficiency 35 percent kWh per liter | hit (summary) |
| 13 | BWXT BANR advanced nuclear reactor microreactor 50 MWt Project Pele 1.5 MWe transport container shipping status 2026 | partial (BANR nothing) |
| 14 | Kaleidos microreactor DOE 1.2 MWe NASA gas-cooled Radiant Nuclear transported shipping container 2026 demonstration DOME | hit (summary) |
| 15 | Chalk River Global First Power Micro Modular Reactor 5 MWe Ontario licence status remote communities Canada SMR Saskatchewan | partial; Saskatchewan miss |
| 16 | Galena Alaska Toshiba 4S reactor 10 MWe proposal cancelled Copper Valley Alaska microreactor remote community nuclear Alaska 2025 | partial; Copper Valley miss |
| 17 | RITM-200 reactor 55 MWe 175 MWt specifications refueling 7 years icebreaker Arktika weight modules floating power unit 106 MWe Baimsky transport tow | partial; weight and tow miss |
| 18 | HVDC 800 kV transmission losses per 1000 km percent versus HVAC 765 kV 500 kV losses per 1000 km ABB Siemens | partial (765 kV miss) |
| 19 | Longyearbyen coal power plant Svalbard capacity MW heat cooling water seawater diesel conversion 2023 Store Norske Lunckefjell | partial; cooling and Lunckefjell miss |
| 20 | frazil ice seawater intake power plant cold climate sea ice blockage cooling water intake design nuclear plant Arctic | partial; no Arctic-specific source |
| 21 | Bilibino nuclear power plant permafrost foundation cooling towers air cooling closed circuit water supply river design cold climate | partial; foundation miss |
| 22 | NRC emergency preparedness small modular reactors final rule 10 CFR 50.160 scalable emergency planning zone site boundary 2023 | partial; led to fetch |
| 23 | Alert Nunavut Canadian Forces Station power generation diesel fuel liters per year and Greenland Qaanaaq Thule diesel; Canada microreactor Arctic Nunavut feasibility study | miss (volumes, Greenland, Nunavut study) |
| 24 | Hydro-Quebec 735 kV transmission line James Bay to Montreal 1,000 km series compensation losses winter ice storm 1998 transmission towers collapsed | partial |
| 25 | Viking Link 765 km subsea cable length NordLink 623 km length Denmark UK 1400 MW cost per km HVDC subsea cable cost per km million | partial (NordLink miss, then fetched) |
| 26 | Antarctic station power line cable overhead buried length kilometers ice Halley McMurdo Scott Base wind farm cable Casey Davis Mawson power cable between stations | miss (only fiber-optic hits); retry failed |
| 27 | Antarctic station fuel consumption liters per person per year diesel Davis Casey Mawson annual fuel use population station | partial (totals, no per-person) |
| 28 | Bilibino spent nuclear fuel shipped Mining and Chemical Combine Zheleznogorsk Chukotka transport ship Northern Sea Route spent fuel removal Pevek floating plant spent fuel Atomflot | partial; led to Sosny paper |
| 29 | Karadeniz powership floating power plant 470 MW barge supplies remote coastal communities Lebanon Sierra Leone heavy fuel oil powership capacity | partial |
| 30 | MH-1A Sturgis floating nuclear power plant Panama Canal Gatun Lake 10 MWe Liberty ship barge history | hit (summary) |
| 31 | Akademik Lomonosov towed from Murmansk to Pevek 2019 Northern Sea Route 4,700 km tow journey days icebreaker escort moored Pevek ice conditions | partial (ice conditions miss) |
| 32 | Pevek floating nuclear plant winter operation sea ice seawater cooling intake ice protection pier Akademik Lomonosov cooling water system | miss for intake; Russian-language suggested |
| 33 | BN-350 Aktau nuclear desalination plant MWe distilled water cubic meters per day Kazakhstan; nuclear desalination IAEA operating experience | partial; figures conflict |
| 34 | Ross Island wind energy project McMurdo Scott Base three turbines power line cable capacity factor percent diesel savings | partial; capacity factor miss |
| 35 | Chaun-Bilibino power system 110 kV line Pevek Bilibino length km isolated grid Chukotka transmission line connect floating plant Bilibino | hit |
| 36 | transmission line losses percent per 100 miles by voltage 115 kV 230 kV 345 kV 500 kV 765 kV surge impedance loading practical length limit AC line | partial (weak sources, 115 and 230 kV miss) |
| 37 | China floating nuclear power plant ACP100S ACPR50S offshore plan; Seaborg CMSR power barge; Core Power floating nuclear; Korea KRISO floating SMR remote island power | partial (China miss) |
| 38 | proposal nuclear power Antarctic research station small modular reactor Madrid Protocol environmental impact assessment nuclear power station Antarctica study | partial (no official plan) |

### Fetches (WF) and extractions (BASH)

| # | URL / action | Result |
|---|---|---|
| 1 | atomicinsights.com/how-clean-clean-blasting-out-frozen-soil/ | hit |
| 2 | cambridge.org/core/product/A35009D4403A289EF51E5F61EE54CFF4/core-reader | **dead end: HTTP 403 (died at the source, paywall/block)** |
| 3 | world-nuclear.org small-nuclear-power-reactors (first 20,000 chars) | partial (Pele, Eielson only) |
| 4 | world-nuclear.org Russia nuclear power | hit (first 100,000 characters read; last 49,650 not read) |
| 5 | world-nuclear.org small-nuclear-power-reactors, offset 20000 | partial (Russian entries only) |
| 6 | westinghousenuclear.com/evinci | hit |
| 7 | wnn.world-nuclear.org us-air-force-confirms-site-for-first-microreactor | hit |
| 8 | resolve.cambridge.org PDF of the Polar Record article | **dead end: HTTP 403** |
| 9 | conferences.iaea.org experience of FNPP operation .doc | **dead end: HTTP 403** |
| 10 | en.wikipedia.org/wiki/PM-3A | hit (partial detail) |
| 11 | fnpp.info/about | **dead end: DNS failure (ENOTFOUND)** |
| 12 | rosatomnewsletter.com/?p=18515 | hit |
| 13 | world-nuclear-news.org bilibino-units-being-shut-down-for-decommissioning | hit |
| 14 | energycentral.com cold-sad-tale--nukey-poo | hit |
| 15 | ats.aq/e/ats.htm | miss (page not found) |
| 16 | ncaor.gov.in Annex III PDF | **dead end: TLS certificate mismatch; not worked around** |
| 17 | ats.aq/e/antarctictreaty.html | miss (no Article V text) |
| 18 | navyhistory.au rise-and-fall-of-nukey-poo | hit |
| 19 | s3.amazonaws.com AJUS vol VIII no 4 p228 PDF | hit after BASH `pdftotext` on the saved copy (scratchpad) |
| 20 | documents.ats.aq/recatt/att005_e.pdf | hit after BASH `pdftotext` on the saved copy (Article V text) |
| 21 | wnn Chinese long-distance nuclear heating project | hit |
| 22 | test.oecd-nea.org Sozoniuk presentation | **dead end: HTTP 521 (source down)** |
| 23 | world-nuclear.org what-is-uranium-how-does-it-work | partial (no per-reactor tonnage) |
| 24 | nrc.gov Table S-3 | partial (no tonnage) |
| 25 | nuclear-power.com fuel-consumption-of-conventional-reactor | hit |
| 26 | energy.gov/node/4844950 (Pele) | hit |
| 27 | radiantnuclear.com/blog/kaleidos-shipped/ | **dead end: HTTP 403** |
| 28 | uaf.edu ACEP blog on nuclear power and the perils of pioneering | hit |
| 29 | cnsc-ccsn.gc.ca Global First MMR project page | **dead end: HTTP 404** |
| 30 | morganlewis.com NRC emergency preparedness blog | hit |
| 31 | energy.gov HVDC2013-Tang_0.pdf | hit after BASH `pdftotext` (limited numbers) |
| 32 | en.wikipedia.org/wiki/North_Sea_Link | hit |
| 33 | en.wikipedia.org/wiki/List_of_HVDC_projects (first 100,000 characters) | hit (rest unread) |
| 34 | en.wikipedia.org/wiki/NordLink | hit |
| 35 | prysmian.com Viking Link page | hit |
| 36 | en.wikipedia.org/wiki/High-voltage_direct_current (first 100,000 characters) | hit (rest unread) |
| 37 | sosnycompany.com spent fuel management at Bilibino | hit |
| 38 | data.aad.gov.au State of Environment indicator 56 | **dead end: HTTP 403** |
| 39 | nucnet.org Pevek power line | hit |
| 40 | neimagazine.com power lines for Russian floating NPP | hit |
| 41 | power-technology.com Ross Island wind farm | hit |
| 42 | antarctica.gov.au waste page | partial (import ban only; no removal statement) |

Counts: 38 searches and 42 fetches, about 80 web calls plus shell extractions. Not done as dedicated queries (budget): Norilsk, Greenland nuclear or thermal siting, seismic or ice-shelf siting, Russian-language Bilibino design literature, KLT-40S or RITM-200 fuel mass, Basslink and Cook Strait cable costs.

Note on tool hooks: a graphify notice appeared on file and shell calls; per the brief's rule it was not used and `graphify-out/` was not opened.
