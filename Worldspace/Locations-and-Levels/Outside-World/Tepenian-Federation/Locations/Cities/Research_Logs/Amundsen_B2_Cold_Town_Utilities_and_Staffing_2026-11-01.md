# Amundsen B2 - Cold-Town Utilities and Staffing (research log, 2026-11-01)

Real-world research only. Claim marks: SOURCED / UNVERIFIED / DERIVED / NOT FOUND.

## PROGRESS
- [x] 1 Water and sewage in permafrost and extreme cold
- [x] 2 Heat and power
- [x] 3 Published staffing ratios (municipal, emergency, remote-camp)
- [x] 4 Housing, building maintenance, snow management
- [x] 5 Medical, school, childcare, residency rules
- [x] 6 Failures and near-failures
- [x] 7 Waste
- [x] FINAL

## SEARCH LOG (exact strings, dead ends)
Tool note: WebSearch returns an AI-written summary of results, not raw snippets, so every figure below was taken from a fetched primary page (WebFetch or curl + pdftotext) unless marked otherwise. Where only a search-summary figure exists it is marked UNVERIFIED.

Searches run (query strings, in order):
1. `Iqaluit water and sewage trucked service number of truck drivers city of Iqaluit utilidor` - no headcount (died at the sources: city pages never publish driver count)
2. `Inuvik utilidor system water sewer permafrost town operation staff` - system size found; staff count absent
3. `Utqiagvik North Slope Borough water sewer Public Works piped water sewer system number of employees truck haul` - no employee count (died at sources)
4. `Longyearbyen water supply Isdammen sewage utility Longyearbyen lokalstyre technical department employees` - no headcount (sources say only "more personnel" needed)
5. `Longyearbyen power plant diesel conversion coal closure Store Norske Kraft Longyear Energiverk employees 2023 operators`
6. `Longyearbyen Energiverk district heating hot water network buildings heated per cent power plant staff` - no plant staff count (died at sources)
7. `Norilsk district heating CHP plants Norilsk Taimyr Fuel and Energy Company heat supply city staff` - no city staffing
8. `Iqaluit 2021 water crisis fuel contamination Lift station "Public Works" employees number of staff city of Iqaluit annual budget`
9. `Yakutsk utilidors heating pipes permafrost district heating city centralized heat supply Yakutskenergo CHP` - thin (mostly bibliographic records; died at query+sources)
10. `Ny-Alesund water supply sewage treatment waste Kings Bay AS number of employees power plant`
11. `Pituffik Space Base Thule water supply sewage power plant heating Greenland contractor staff Inuit Services`
12. `Iqaluit piped water utilidor trucked water per cent of residents Apex Plateau Tundra Valley water licence NU Public Works trucks fleet`
13. `CFS Alert Nunavut station staff water supply power generation heating fuel number of personnel Canadian Forces Station Alert`
14. `Alaska rural vacuum sewer system arctic communities pump truck haul water "piped" "washeteria" operator staffing small utility`
15. `Norilsk water supply sewage utilidors city population "Norilsk" heating pipes above ground "Norilsk Komplekt" OR "Norilskkomplekt" employees` - no Norilsk utilidor/staff source (died at query; needs Russian-language search)
16. `McMurdo Station sewage treatment plant desalination reverse osmosis water production gallons per day population operators`
17. `Antarctic Blue Ribbon Panel 2012 "More and Better Science in Antarctica" support personnel per scientist ratio McMurdo South Pole population`
18. `South Pole Station winter population 2023 number of people jobs fire brigade medical doctor cooks plumbers heavy equipment operators station staff breakdown`
19. `Australian Antarctic Division station winter expeditioners trades roles Davis Casey Mawson plumber electrician chef doctor winter team size`

20. `Utqiagvik Barrow Utilities and Electric Cooperative BUECI customers employees natural gas generation power outage`
21. `Qulliq Energy Corporation Iqaluit power plant employees customers number of staff generating plant operators diesel 25 communities`
22. `Nukissiorfiit annual report employees number Nuuk hydropower Buksefjord district heating customers control room`
23. `Reykjavik Veitur geothermal district heating customers employees Orkuveita Reykjavikur workforce hitaveita share of homes`
24. `Longyearbyen lokalstyre antall ansatte arsverk tekniske tjenester brann vann avlop organisasjon arsrapport` (Norwegian, diacritics dropped here only in this log line)
25. `Svalbard no right of residence must leave if unemployed sick elderly Governor of Svalbard rules for moving to Longyearbyen requirements`
26. `Longyearbyen sykehus Helse Nord UNN Longyearbyen hospital number of beds staff doctors nurses ambulance evacuation Tromso`
27. `Longyearbyen skole barnehage Svalbard barnehage antall barn elever laerere Longyearbyen skole`
28. `forskrift om bortvisning og utvisning fra Svalbard 3 midler til a livnaere seg bolig lovdata` - gave only regulation outline; the text was read through WebFetch of lovdata (paraphrased by the fetch tool)
29. `Qikiqtani General Hospital Iqaluit beds staff number of physicians nurses medevac Ottawa Nunavut health Iqaluit population`
30. `Kiruna population hospital Kiruna lasarett beds LKAB new city relocation fire brigade district heating Kiruna Energi Kiruna Kommun employees` - population and relocation only (died at query: bed counts, fire brigade not returned)
31. `water utility staffing benchmark employees per 1,000 customer accounts AWWA QualServe median water wastewater FTE per 1,000 connections` - no primary AWWA median (AWWA benchmarking data is members-only; died at the sources)
32. `Census Bureau Annual Survey of Public Employment and Payroll local government full-time equivalent employees per 10,000 population police fire sewerage solid waste highways` - led to the 2023 individual unit files, which were downloaded and computed (see section 3)
33. `NFPA US Fire Department Profile career firefighters per 1,000 population by community size under 2,500 volunteer percent` - NFPA PDF itself blocked (returned HTML); used USFA FA-303 (2006) instead
34. `FBI UCR law enforcement employees per 1,000 inhabitants by population group cities under 10,000 police officers per 1,000`
35. `ICMA municipal staffing per 1,000 residents full-time equivalent employees per capita small cities population 2,500 to 10,000 public works police fire` - NO ICMA figures (ICMA benchmarking is members-only; died at the sources). Only regional studies surfaced (Pennsylvania 3.5 FTE per 1,000; Oregon one FTE per 229 residents) via search summary - UNVERIFIED, not opened.
36. `Halley VI Research Station winter team size roles engineers chef doctor station leader British Antarctic Survey wintering staff 2023`
37. `Rothera Research Station British Antarctic Survey winter population summer population support staff to scientists ratio`
38. `Summit Station Greenland staff winter summer population science technicians Polar Field Services snow management drift buildings elevated`
39. `South Pole elevated station jacks raise building snow drift 36 feet lifting 2023 jacking project NSF Antarctic Sun` - no 2023 jacking event found (NOT FOUND)
40. `Halley VI hydraulic legs skis modules relocation 2016 crack Chasm 1 moved 32 km station design Hugh Broughton snow accumulation lifting`
41. `Vostok Station fire 1982 diesel generator power plant fire 1 died winter survived stoves Soviet Antarctic Expedition details`
42. `Antarctic station fires history Mawson 1959 Halley fire 1985 Davis fire Casey Concordia station fire Belgrano II Dome Fuji fire lessons learned` - no Halley, Davis, Casey, Concordia, Belgrano, Dome Fuji fire found (died at the sources; the coolantarctica list does not include them)
43. `Norilsk diesel fuel spill May 2020 Ambarnaya River tank collapse 21000 tonnes permafrost cause NTEK CHP-3 fine`
44. `Longyearbyen avalanche December 2015 houses destroyed two killed 2017 avalanche Sukkertoppen evacuated lessons Nybyen`
45. `Longyearbyen strombrudd hele byen desember 2025 stromstans Svalbard Energi nodstrom arsak` - no news report; the event is documented only in the council's own 2025 annual report
46. `Longyearbyen fjernvarme utfall mai 2025 OR 2024 fjernvarmen stoppet Svalbard Energi varmeverk problemer Longyearbyen kaldt` - same
47. `cost per tonne to ship waste out of Antarctica retrograde South Pole traverse waste shredder incinerator McMurdo waste retrograde tons per year` - no per-tonne cost (died at the sources)
48. `Summit Station Greenland waste removal backhaul LC-130 waste management plan Environmental Impact Assessment tons of waste per year incinerator` - nothing on waste (died at query/sources)
49. `Ny-Alesund OR Pituffik OR Alert waste incinerator open burning landfill Nunavut community waste incinerator remote camp waste per person per day kg`
50. `Alaska rural backhaul program cost per ton hazardous waste e-waste removal from villages by barge or air ADEC backhaul grant $ per ton` - no per-ton rate
51. `Svalbard waste Longyearbyen waste shipped to mainland cost per tonne Ny-Alesund waste shipped Tromso Kings Bay avfall kostnad per tonn` - no shipping cost
52. `South Pole Station winter crew job titles list fire chief EMT physician assistant heavy equipment operator plumber electrician carpenter cook IT station manager winterover roster` - no roster by trade
53. `McMurdo Station jobs by department Antarctic Support Contract number of employees fleet operations galley housekeeping fire department medical station population summer winter 2024` - no department counts
54. `SSB kommunal sektor antall ansatte arsverk kommuner 2024 ansatte per 1000 innbyggere kommunale arsverk` - national totals only; no per-1,000 ratio published; SSB table 07791 not opened
55. `Faroe Islands SEV electricity company employees customers hydro wind diesel control room Strond Vestmanna Eidi` - no control-room or staffing source (died at the sources)
56. `Iqaluit power plant diesel Qulliq Iqaluit generating station staff number operators Iqaluit electricity demand MW customers`
57. `Polar Continental Shelf Program Resolute Bay facility staff camp support ratio scientists Canadian High Arctic Research Station Cambridge Bay operations staff number` - no ratio (died at the sources)
58. Russian-language: `Norilsk teplotrassy nadzemnaya prokladka vodosnabzhenie kanalizatsiya ... NTEK` (original Cyrillic query; transliterated here) - no utilidor or staffing source (died at the sources)
59. `Iqaluit population 2021 census 7,429 schools ... daycare spaces Iqaluit`
60. `Kiruna kommun invanare 2024 SCB Kiruna lasarett vardplatser raddningstjanst Kiruna deltidsbrandman` - population only
61. `Norilsk population 2021 Russian census Norilsk city hospital beds Norilsk schools kindergartens ...` - population only

Dead ends / failed fetches:
- Battelle `Pituffik_Guide.pdf` URL returned only the site shell (no guide text) - died at the source URL.
- `petersonschriever.spaceforce.mil` 821st Support Squadron fact sheet: HTTP 403 (died at the source).
- Yellowknifer/NNSL Inuvik utilidor article: first URL redirected, redirect URL 404 (died at the source). Facts from it appear only in a search summary -> UNVERIFIED.
- City of Iqaluit trucked-services pages give no driver/truck counts (died at the sources).
- Veitur district-heating page: gives only "serving 65% of the population"; no customers, pipe length, staff (died at the page).
- AWWA benchmarking article: no numbers (died at the page).
- NFPA fire department profile PDF: returned HTML, not readable (died at the source).
- Summit Station 2016 presentation (eu-interact.org): HTTP 503 twice (died at the source).
- NAV "work and residence on Svalbard": 404. gov.nu.ca Qikiqtani General Hospital page: 403. waste360 and recyclenation McMurdo-waste pages: 403. usap.gov 2022-23 science planning summary: 404. Longyearbyen Energiplan 2023-2030 PDF: 404 via fetch and HTML via curl.
- Longyearbyen fire annual reports (lokalstyre getfile.php links): returned HTML to curl, not PDFs (died at the source); the 2025 council annual report was used instead.

## 1 Water and sewage
### 1.1 Longyearbyen (Svalbard) - water and sewer
- SOURCED (Longyearbyen lokalstyre Arsberetning 2025, https://www.lokalstyre.no/download/18.5626f86419ddcc34b6b3d6/1777558120002/Vedlegg%20sak%2009-26%20%C3%85rsberetning%202025%20-%20Longyearbyen%20lokalstyre.pdf): population "2 515 personer ved utgangen av 2025" (2,518 at start of 2025; 2,546 Jan 2022; 2,561 Jan 2023; 2,532 Jan 2024). About half of households are one person. Norwegian share just over 63 percent.
- SOURCED (same): Technical services unit ("Enhet for tekniske tjenester") covers river protection, avalanche protection, roads, snowmobile trails, public places, cemetery, water and sewer, waste, and landfill operation. "Enheten har 9 faste stillinger; enhetsleder, senioringeniør, driftsingeniør vann og avløp, driftsingeniør vei og nærmiljø, fagleder renovasjon, driftsleder renovasjon, og tre operatører på miljøstasjonen." (9 permanent posts; one is the water-and-sewer operations engineer, one is the senior water-and-sewer engineer hired in 2025; three are waste-station operators.) The unit "har driftskontraktsansvar for avtaler med Assemblin og LNS" - day-to-day operation is partly contracted out. The report states "lav bemanning pa VA" (low water-and-sewer staffing) and that the unit "over tid vaert underbemannet", producing a maintenance backlog.
- DERIVED: 9 permanent posts for 2,515 residents = 3.6 per 1,000 for the whole unit (roads, water, sewer, waste, landfill, avalanche and river works), before contractor staff. Contractor headcount NOT FOUND.
- SOURCED (same): Cost-recovery rate ("dekningsgrad", a self-cost accounting figure, not population coverage) 83 percent for water and 68 percent for sewer in 2025; combined under-recovery 6.6 million NOK for the year, 8.7 million NOK accumulated.
- SOURCED (same): Timeline: April 2024 Legionella found in drinking water; autumn 2024 manganese above infant thresholds; Feb 2025 Legionella and manganese (children under 12 months advised not to drink tap water); June 2025 sulfate; September 2025 manganese and nickel up, general advice not to drink tap water; emergency solution of purified water from Svalbard Bryggeri (brewery) plus own purification units in public buildings. A reserve water source project is "more complex" because it is uncertain whether Isdammen is a stable enough raw-water source.
- SOURCED (https://www.lokalstyre.no/engelsk/longyearbyen-local-council/news-archive/news-front-page/2026-02-11-the-water-situation-status-research-and-the-way-forward): Isdammen produced about 141,720 m3 for consumption since the September incident, and about 150 m3 of drinking water came from the brewery, "Drinking water thus accounts for only one percent of total production." Four projects: secure Isdammen, reserve water, strengthen firefighting-water capacity, replace aging distribution network. Plan includes "strengthening technical operations with more personnel". A reverse-osmosis plant at the brewery is planned.
- SOURCED (https://www.lokalstyre.no/engelsk/longyearbyen-local-council/news-archive/news-front-page/2026-03-20-the-water-supply-in-longyearbyen-must-be-secured): "The ice pond is Longyearbyen's only source of drinking water." SINTEF/UNIS/UiB condition analysis; report expected Q2 2027.
- SOURCED (council report, fire section): "Rornett og vanndistribusjon i Longyearbyen er ikke dimensjonert for a tilfredsstille dagens krav til slukkevanns-kapasitet" - the pipe network is not sized for current firefighting-water requirements; "manglende slukkevanns-kapasitet" was a significant problem in the fires at road 228 and road 232.
- NOT FOUND: operator headcount at the water treatment plant; sewage treatment details beyond the 2022 tourism-site remark that sewage once went untreated into the fjord (UNVERIFIED; svalbardblues/spitsbergen-svalbard.com summary only).

### 1.2 Inuvik (NWT) - utilidors
- SOURCED (https://www.inuvik.ca/living-here/water-sewer-and-utilities/, via fetch): "Altogether, the Town of Inuvik has 950 water and sewer connections"; 16 km of above-ground utilidor, under 1 km buried line; 15.8 km of water mains and 16.3 (unit omitted on page) of sewer mains in town; about 500 m of water and sewer line replaced per year at about $1.5 million per year; older utilidor lines date from the late 1950s; the Town became owner-operator under a June 2000 agreement with the GNWT; water from Hidden Lake and a year-round intake at East Channel; sewage to lagoon system; "circulation and heating stations" listed; a Utilidor Lead Hand and an after-hours Utilidor operator on call. Page gives no staff count.
- UNVERIFIED (search summary only; source article could not be opened): about 6,400 m of original utilidor still in service and a replacement estimate of $80 million (Yellowknifer/NNSL, "$80 million to replace utilidor system already 30 years past service life"); the reservoir is gravity-fed so fire water is seen as secure.
- NOT FOUND: Inuvik public works headcount (died at the sources).

### 1.3 Iqaluit (Nunavut) - piped plus trucked
- SOURCED (Nunatsiaq News, 14 Sept 2015, https://nunatsiaq.com/stories/article/65674city_of_iqaluit_to_hold_meeting_on_waterless_wednesdays/): "Only 11 per cent of Iqaluit's population requires trucked water delivery and sewage pump-out"; "more than 40 per cent of the city's sewage and water budget is spent annually on trucked water service"; the water and sewage budget was $8 million; over 600 buildings (491 residences) lost regular Wednesday trucked service. No truck or driver count. (2015 data.)
- SOURCED (City of Iqaluit notice, https://iqaluit.ca/node/14520, undated, Sept 2025 per search summary): "temporary staffing shortages" - water delivery "extremely limited" and "sewer service is temporarily unavailable"; city "hiring trucked services drivers and other Public Works positions". Shows the trucked system fails when a small crew is short.
- SOURCED (search summary of iqaluit.ca postings; UNVERIFIED as to current relevance): a 2018 casual posting for municipal truck drivers; no headcount. Trucked-service areas: Apex, Tundra Valley, parts of Lower Base.
- NOT FOUND: number of Iqaluit trucks, drivers, utilidor operators (died at the sources).

### 1.4 Utqiagvik (Alaska)
- SOURCED (Arctic Sounder / ADN, 30 May 2024, https://www.adn.com/arctic-sounder/news/2024/05/30/north-slope-borough-plans-to-bring-the-water-and-sewer-system-above-ground): households first got water and sewer in the mid-1980s; the system was buried; permafrost thaw is making pipes shift and break; the borough is designing a pilot above-ground system for about 27 houses without service, preliminary cost about $5 million, with electric heat trace and insulation on waste lines; Bethel has run above-ground for over 20 years. Public Works director Scott Danner.
- UNVERIFIED (third-party aggregator via search summary): Barrow Utilities and Electric Cooperative reported 113 employees in 2023 with revenue about $33.1 million (electric, gas, water, wastewater). Not opened at primary source.
- NOT FOUND: water/sewer operator count and haul-truck count for Utqiagvik.

### 1.5 Ny-Alesund (Svalbard) - research village run by a company
- SOURCED (Svalbardposten, 4 Sept 2015, https://svalbardposten.no/environment-kings-bay-ny-alesund/spending-millions-for-the-environment/141047): "123 people currently", community maximum 200; sewage plant costs about 1.5 million NOK, capacity 10,000 liters a day; sewage no longer discharged to the fjord; sludge pumped out and composted; energy-saving cut diesel use by about 200,000 liters; 12 to 15 million NOK spent on environment since 2013.
- SOURCED (Wikipedia Kings Bay (company), fetched): 32 employees in 2007 (infobox). UNVERIFIED (search summary): "permanent staff of 20-25 employees" depending on season. The company supplies power, water, district heating, fire protection, housing, catering and airport/harbor.
- CONFLICT noted: sewage plant capacity is described as 10,000 L/day (Svalbardposten) vs 65 population equivalents and 10 m3/day (manufacturer page, search summary); same figure in different units, not a true conflict.

### 1.6 CFS Alert (Nunavut) and Pituffik (Greenland)
- SOURCED (CBC, 13 April 2006, via army.ca copy https://army.ca/forums/threads/costly-fuel-prompts-cuts-at-northern-military-station.42168): "approximately 70 armed forces personnel at the base, down from a peak of about 200 in the 1980s"; cooks, janitors, drivers and mechanics moved to civilian contractors because heating cost forced cuts.
- SOURCED (Wikipedia CFS Alert, fetched): "about 55 people stationed at CFS Alert" (2024); only six people responsible for actual operations; remaining staff cover airfield, construction/engineering, food service, logistics; by 2008 a civilian contractor ran the power plant; maintenance contract to Canadian Base Operators until 2012, then Nasittuq Corporation (majority Inuit-owned). Facilities listed: water treatment plant, primary and backup power plants.
- UNVERIFIED (search summary): 2022 federal contract to Nasittuq for CFS Alert support services, 8.5 years initial; scope includes power plants, buildings, generators, water and sewage; fuel use over 2,000,000 L a year for power and heat (2013 conference paper); water from Dumbell Lake.
- UNVERIFIED (search summary): Pituffik Space Base population "700+" (Battelle guide) or about 600 (jobs blog); base maintenance contractor Inussuk Group per one source, V2X per another (conflict); Serco $323 million contract (2024) for a backup power plant. Primary pages not opened (Battelle PDF returned only site shell; 821st Support Squadron page 403).
- NOT FOUND: water/sewer system description for Pituffik; staff counts per system at either site.

### 1.7 Vacuum sewers and haul systems in rural Alaska
- SOURCED (ANTHC final report to US DOE, https://www.energy.gov/sites/default/files/2019/06/f63/ANTHC-final-report.pdf, read via pdftotext): vacuum sewers are "typically installed in places where the topography is primarily flat and the elevation differential is not enough for a gravity powered sewer system to function without freezing during the winter" and are "the most costly and energy intensive form of sewer system," because of large vacuum pumps, leaks that lengthen pump run time, "man-power needed to maintain pipe grade," and heat added to above-ground pipes. Three plants (Alakanuk, Kotlik, Noorvik) used 31,688 gal diesel for heat and 458,568 kWh electricity per year before retrofit; 378,711 kWh in 2018 after; oil-less vacuum pumps replaced rotary-vane pumps because rotary-vane pump fires were a hazard.
- NOT FOUND: operators per vacuum system. The report says local plant operators are trained and supported by ANTHC utility-support engineers, laborers, plumbers (lines 254-258 of text) but gives no counts.

### 1.8 McMurdo and South Pole water and sewer (remote-camp reference)
- SOURCED (Blue Ribbon Panel report, "More and Better Science in Antarctica Through Increased Logistical Effectiveness," July 2012, https://nsf-gov-resources.nsf.gov/files/antarctica-07232012.pdf, read via pdftotext): South Pole winter population "around 50"; summer "would be 150 if only the Elevated Station is occupied. With additional, summer-only accommodations, the overall population approaches 250, limited by the operational capacities of the water and sewage systems." Station provides "over 5000 meals per week during the summer" and uses "approximately 450,000 gallons of fuel annually." Wastewater plants at Palmer and South Pole "are in need of upgrading"; McMurdo's is "generally state-of-the-art."
- UNVERIFIED (search summaries of blogs): McMurdo makes water by seawater reverse osmosis; figures of 40,000 to 55,000 gallons per day vary by source and year; solids from wastewater are boxed and shipped to the US. A job posting names an "Operator in Responsible Charge" for the water plant.

## 2 Heat and power
### 2.1 Longyearbyen (Svalbard) - heat and power
- SOURCED (Longyearbyen lokalstyre Arsberetning 2025, same URL as section 1.1): energy supply was run by the council's wholly owned subsidiary Svalbard Energi AS (SEAS) in 2025; "Det er gjennom hele 2025 jobbet med a overfore SEAS til Store Norske" (SEAS being transferred to Store Norske through 2025; infrastructure and buildings had to be separated and agreements set up). Events in 2025 listed by the council: May, "utfall av fjernvarme i deler av byen" (district-heating outage in parts of town); December, "strømstans i hele byen" (power stoppage across the whole town). The fire service reports an emergency-power solution was established and put into operation in 2025.
- SOURCED (High North News, "All ready for the transition from coal to diesel in Longyearbyen," https://en.highnorthnews.com/politics/all-ready-for-the-transition-from-coal-to-diesel-in-longyearbyen/134303, fetched): "The transition from coal to diesel involves a down-sizing of 13 people in Svalbard Energy by June next year"; transition cost "expected to cost NOK 212 million"; Mine 7 operations extended to summer 2025 "to act as a backup plan for energy supply"; Svalbard has no security-of-supply law setting emergency volumes for fuel; the council energy plan says renewables are to be phased in "as quickly as possible". Year of the article not shown on the page.
- SOURCED (Tom Antle, "District Heating in the Arctic," pellet.org, read via pdftotext): Longyearbyen "1,750 residents" (figure in the slide; differs from the council's 2,515); community-wide, above-ground district heating; coal-fired CHP "8 MWe/20 MWth," plant built 1982; "Coal use ended in 2025" (slide); "C$30 M CapEx to switch to diesel"; "Diesel supposed to be stopgap before renewables"; diesel bought on the open market at much higher cost.
- CONFLICT: coal end date. rcinet / Barents Observer-type reports (via search summary) give 19 October 2023 as the plant's last coal day; the Antle slide says 2025; HNN says Mine 7 was extended to summer 2025 as a backup. Not resolved from sources read.
- SOURCED (TU.no, "Longyearbyen fyrer for kråka...", https://www.tu.no/artikler/longyearbyen-fyrer-for-kraka-bruker-dobbelt-sa-mye-varme-om-vinteren-som-hus-pa-fastlandet/450263, date not shown on fetched text): current consumption about 70 GWh district heat and 40 GWh electricity per year, "fordelt pa 1.850 forbrukere" (1,850 consumers); in winter buildings use over twice the heat of mainland buildings; about 50 percent of heated area is housing, over 40 percent commercial; over half the floor area built before 1970; no measurements of district-heating network losses.
- DERIVED: 110 GWh total per year / 2,515 residents = about 44 MWh per resident per year; 110 GWh / 1,850 consumers = about 59 MWh per consumer. (Different years for the two inputs.)
- NOT FOUND: operator headcount per shift at Energiverket; control-room staffing; the number of customers per grid operator.

### 2.2 Nuuk and Greenland (Nukissiorfiit)
- SOURCED (Nukissiorfiit Annual Report 2024, https://nukissiorfiit.gl/wp-content/uploads/2025/06/ENG-Nukissiorfiit-Arsrapport-2024.pdf, read via pdftotext): 411 employees; 20,600 customers; 5 hydropower plants (91.3 MW total); 27 heating plants; 72 waterworks (3 renovated in 2024); 17 towns and 54 small settlements served; 4 wind turbines (71 kW); sales 266.5 GWh; 5.2 million m3 (water). Five-year table: full-time employees 411.0 (2024), 400.5, 393.0, 416.0, 437.0.
- DERIVED: 20,600 customers / 411 employees = 50.1 customers per employee (about 20 employees per 1,000 customers), for a company that does power, water and heat together. A customer here is not defined in the text read.
- SOURCED (same): 28 December 2024 Nuuk blackout "caused by a fallen conductor on the transmission line from the hydropower plant at Utoqqarmiut Kangerluarsunnguat"; parts of the city kept a skewed voltage, so "our emergency power plant did not automatically start up as it would otherwise." Ten container emergency generators acquired, eight in Nuuk and two in Aasiaat; the eight in Nuuk are "a temporary measure ... until we get a new emergency diesel generator built." Outages also hit Aasiaat, Qaqortoq and Ilulissat in 2024. Employees "worked around the clock." Retention is stated as a challenge: "Nukissiorfiit faces challenges in retaining and attracting a well-trained work force on public sector wages." Battery banks installed in three small settlements in 2024. A control, regulation and monitoring (CRM) system is mentioned for maintenance but no control-room staffing is given.
- SOURCED (Antle slide deck): Greenland has 16 district-heating systems and 23 plants; Nuuk and Sisimiut waste-to-energy CHP plants, each 8.2 MWth; waste-to-energy supplies almost all heat for Sisimiut and about 10 percent for Nuuk; Ilulissat (about 4,700 people) has a 22.5 MWe hydropower plant but distributes heat by district heating; Nanortalik (about 1,100) uses diesel-generator heat recovery plus oil. (Slide text, not independently checked.)

### 2.3 Nunavut (Qulliq Energy Corporation)
- SOURCED (QEC Annual Report 2024-25, https://www.assembly.nu.ca/sites/default/files/2026-06/TD-025-7%282%29-EN-QEC_Annual_Report_2024-2025.pdf, read via pdftotext): "approximately 16,000 customers across Nunavut"; "25 stand-alone diesel power plants in 25 communities, with a total installed capacity of approximately 84,000 kilowatts"; "Each community in Nunavut has its own independent electricity generation and distribution system. There is no back-up grid." Each community plant is "operated by local employees, supported by electricians, mechanics, meter technicians, power line technicians, and fleet staff based in the regional hubs of Iqaluit, Cambridge Bay, and Rankin Inlet." 41 positions filled in 2024-25; 57 percent of the workforce identify as Nunavut Inuit. QEC owned 133 staff housing units, 81 of them in Iqaluit, plus 29 transient units.
- NOT FOUND: QEC total headcount in the annual report. UNVERIFIED (search summary of undated parliamentary testimony): about 200 employees and 15,000 customers, which would be about 75 customers per employee; not opened at source.
- UNVERIFIED (search summary): Iqaluit residents burn about one million liters of diesel a month; Iqaluit plant in service about 50 years with expansion of two 5 MW diesel units planned; second Iqaluit generator from 1993.

### 2.4 Utqiagvik, Alaska
- SOURCED (North Slope Borough public service announcement, 11 Feb 2026, https://www.north-slope.org/wp-content/uploads/2026/02/PSA-Utqiagvik-Power-Outage_asc-v3_021126.pdf): about 2:15 a.m. the west (Barrow) side lost electricity, "resulting in outages to heat, power, local phone service, and internet"; as of 9:30 a.m. Borough offices including Public Works were closed; crews did door-to-door checks "to identify homes that may be experiencing freeze-ups." 911 dispatch stayed up. Cause and duration not stated.
- UNVERIFIED: BUECI reported 113 employees (2023) per an aggregator (section 1.4).

### 2.5 Norilsk
- SOURCED (Nornickel Annual Report 2023, "Energy assets," read via pdftotext): the Energy Division runs three CHP plants, two hydropower plants and four gas fields; NTEC "supplies electricity, heat, and water to Norilsk households, as well as to all industrial and commercial consumers in the Norilsk Industrial District"; "The local electricity grid is operationally and geographically isolated from the national grid ... which means stricter reliability requirements"; NTEC operates five generating facilities: three thermal plants "with a total installed capacity of 1,154 MW" and two hydropower plants "1,102 MW," total 2,256 MW; renewables 58 percent of generation in the Norilsk Industrial District in 2023; emergency diesel tanks being rebuilt (three at CHPP-1).
- SOURCED (Wikipedia-derived search summary of Rosstat data; UNVERIFIED): Norilsk Urban District 175,237 residents (2021 census); temporary residents bring it to about 220,000 (commonly stated, not sourced).
- NOT FOUND: NTEC headcount; city heating-network design (above-ground or buried); utilidor staffing (died at the query: Russian-language search returned only Nornickel reports).

### 2.6 Reykjavik, Faroe Islands, Yakutsk, Ny-Alesund (thin)
- SOURCED (Veitur, https://veitur.is/en/f/district-heating): "Our responsibility is to provide a reliable supply of hot water, serving 65% of the population." Search-summary-only (UNVERIFIED): parent company says three quarters of the population use its district heating; third-party headcounts for the group range from 196 to 606 and are inconsistent.
- UNVERIFIED (search summary): SEV (Faroe Islands) is municipality-owned, main supplier (about 90 percent of production), grid not interconnected, target 100 percent renewable electricity by 2030, a third-party profile lists 73 employees. Control-room data NOT FOUND.
- Yakutsk: search summary only (UNVERIFIED): heating mains run above ground; citations were bibliographic records. NOT FOUND: CHP capacity, staffing, network length.
- Ny-Alesund: company supplies power, district heating, water, sewer and fire protection with 20-25 permanent staff (UNVERIFIED search summary) or 32 (2007, Wikipedia).
- Alaska (ANTHC report): vacuum-sewer plants spend large heat and electric loads; see section 1.7.
- CFS Alert: UNVERIFIED search summary: heat from fuel-fired boilers and a hot-water district network; over 2,000,000 L of fuel a year; South Pole fuel use 450,000 gallons a year (BRP, SOURCED, section 1.8).

## 3 Staffing ratios
### 3.1 US municipal governments - Census 2023 Annual Survey of Public Employment and Payroll (DERIVED)
Source: Census Bureau 2023 ASPEP Individual Unit Files, https://www2.census.gov/programs-surveys/apes/tables/2023/2023_individual_unit_files.zip (files 23empst.txt and 23empid.txt, downloaded and parsed). Method (DERIVED): for each band of municipal governments (unit type "Municipal," a sampled subset, unweighted) summed the "Full-Time Employees" for a function code and divided by the summed population of the governments in the band. Function codes were matched to names by comparing the text file with the Excel file for Scottsboro AL and Hoover AL. Caveats: sample, not a complete count; full-time employees only (part-time and volunteers excluded); a function a city does not run (contracted out, run by a county, district or utility) shows as zero, so these ratios are municipal-payroll ratios, not service-level ratios. Sewer and water are often run by separate utilities not counted here.

Full-time employees per 1,000 residents (units in band in brackets; share of units reporting that function in the second row):

| Function | 1,000-2,499 (n=260) | 2,500-4,999 (n=262) | 5,000-9,999 (n=374) | 10,000-24,999 (n=653) |
|---|---|---|---|---|
| All functions | 13.05 | 15.72 | 12.12 | 11.07 |
| Police, sworn (power of arrest) | 2.45 | 2.54 | 2.38 | 1.97 |
| Police, other staff | 0.32 | 0.50 | 0.47 | 0.42 |
| Fire, firefighters | 0.27 | 0.65 | 1.12 | 1.30 |
| Fire, other | 0.04 | 0.05 | 0.05 | 0.09 |
| Highways (streets, snow, roads) | 1.34 | 1.30 | 1.03 | 0.80 |
| Sewerage | 0.70 | 0.53 | 0.60 | 0.46 |
| Water supply | 0.99 | 0.86 | 0.76 | 0.56 |
| Solid waste | 0.42 | 0.39 | 0.38 | 0.33 |
| Electric power | 0.48 | 0.52 | 0.40 | 0.29 |
| Parks and recreation | 0.46 | 0.69 | 0.76 | 0.61 |
| Libraries | 0.19 | 0.20 | 0.20 | 0.15 |
| Financial administration | 1.04 | 0.71 | 0.67 | 0.50 |
| Other government administration | 1.07 | 0.93 | 0.72 | 0.51 |

Share of governments in band that report any water-supply staff: 73, 79, 79, 75 percent; sewerage 68, 71, 79, 78 percent; firefighters 23, 50, 69, 81 percent; solid waste 30, 37, 44, 53 percent; electric power 21, 30, 25, 22 percent.
DERIVED reading, using the 5,000-9,999 band: water supply 0.76 + sewerage 0.60 + solid waste 0.38 + highways 1.03 = about 2.8 full-time municipal public-works and utility employees per 1,000 residents among governments that run those functions; about 19 employees for a 7,000-person government. This reading is arithmetic on the table only and is not a recommendation.

### 3.2 Police, fire, ambulance - US national series
- SOURCED (FBI, Crime in the United States 2018, Police Employees, https://ucr.fbi.gov/crime-in-the-u.s/2018/crime-in-the-u.s.-2018/topic-pages/police-employee-data.pdf): "Nationwide, the rate of sworn officers was 2.4 per 1,000 inhabitants. The rate of full-time law enforcement employees (civilian and sworn) per 1,000 inhabitants was 3.4"; "the highest rate of officers to individuals among the city population groups was an average of 3.8 officers per 1,000 inhabitants in cities with fewer than 10,000 residents"; county agencies 2.8; sworn officers 70.4 percent of all law enforcement personnel. (Search summary, UNVERIFIED as to page: 2002 all-employee rate in cities under 10,000 was 4.1 per 1,000.)
- SOURCED (USFA, "Four Years Later - A Second Needs Assessment of the U.S. Fire Service," FA-303, Oct 2006, read via pdftotext), Table ES-1, firefighters by population protected: under 2,500: 7,750 career, 398,350 volunteer, 406,100 total; 2,500-4,999: 6,100 career, 155,750 volunteer, 161,850 total; 5,000-9,999: 14,400 / 119,100 / 133,500; 10,000-24,999: 48,150 / 83,900 / 132,050; total 1,101,250, of which 73 percent volunteer; "Nearly half the volunteers serve in communities with less than 2,500 population." "In communities with less than 2,500 population, 21% of fire departments ... deliver an average of 4 or fewer volunteer firefighters to a mid-day house fire." National standards name 4 as the minimum for interior attack (same document).
- SOURCED (FireRescue1 summary of NFPA, published 1 Nov 2013, 2012 data): about 1,129,250 US firefighters, 345,950 career (31 percent) and 783,300 volunteer (69 percent); 30,100 departments, 20,050 strictly volunteer.
- DERIVED: 406,100 firefighters under 2,500 population protected, but the table does not give the population protected, so no per-1,000 rate can be computed from it.
- NOT FOUND: ambulance/EMS staffing per 1,000 for small US towns; public-health staffing per 1,000 (BLS and ICMA not reached).
- SOURCED (Longyearbyen council 2025, section 3.4): fire service also runs the ambulance (131 of 377 callouts).

### 3.3 Water-utility benchmarks
- UNVERIFIED (search summary of a 2019 North Richland Hills TX budget page quoting AWWA): national median of 509 customer connections per employee (about 2 employees per 1,000 connections). Not opened.
- UNVERIFIED (search summary): World Bank guidance cited in a Trinidad review: 4 to 6 staff per 1,000 connections is good practice for developing-country utilities.
- AWWA says its current benchmarking survey added "Staffing Levels per 1,000 Population Served" for water and wastewater (SOURCED, https://www.awwa.org/AWWA-Articles/utility-benchmarking-provides-useful-staffing-level-comparisons/) but the article gives no values.
- NOT FOUND: ICMA ratios (members-only), BLS ratios per 1,000 residents, Canadian municipal ratios, Nordic per-1,000 ratios other than Longyearbyen. KS (Norway) reports about 500,400 employees and 455,300 full-time equivalents in municipal administration (search summary, row labels unclear; UNVERIFIED).
- UNVERIFIED (search summary): League of Oregon Cities survey average one FTE for every 229 residents (about 4.4 per 1,000); smallest-city quintile averaged 2.2 FTE per city; Pennsylvania sample about 3.5 full-time employees per 1,000. Not opened.

### 3.4 Longyearbyen (Nordic comparator, all SOURCED from the 2025 council annual report; arithmetic DERIVED)
- Residents 2,515 (31 Dec 2025). Council: "ca. 140 arsverk ... ca. 170 ansatte" (about 140 full-time equivalents, about 170 employees); turnover about 14 percent (22 resignations); sick leave 5.4 percent; 12 managers.
- DERIVED: 140 FTE / 2,515 = 55.7 FTE per 1,000 residents; 170 employees = 67.6 per 1,000. This council runs school, kindergartens, culture, technical services, fire/ambulance, port, planning and administration (the hospital is run by UNN, energy by SEAS), so it is not comparable to the US table above.
- Technical services: 9 permanent posts (3.6 per 1,000), plus contracts with Assemblin and LNS; described as under-staffed.
- Fire and rescue: 25 people, 4 full-time and 21 part-time, five watch teams on a rotating one-week-in-five roster, plus a reserve bank of 5-8; alarm handling by the 110 center in Tromso. DERIVED: 9.9 per 1,000 total, 1.6 full-time per 1,000. 377 callouts in 2025 (131 ambulance, 22 fires) = about 150 callouts per 1,000 residents.
- Hospital: 23 staff (see 5.1); DERIVED 9.1 per 1,000.
- School and kindergarten: see 5.2.

### 3.5 Remote-camp ratios
- SOURCED (Blue Ribbon Panel 2012, https://nsf-gov-resources.nsf.gov/files/antarctica-07232012.pdf): "the logistics effort supporting that science is the vast base of the iceberg - representing, in terms of person-days in Antarctica, nine times the number devoted to research activity (Figure 1). ... the 1:9 ratio of science to support." The O&M contractor staff, subcontractors and aviation support are "a total of well over 1000 people, not including shipboard personnel," and "dominate the USAP population." The report lists an action to "Conduct a review to reduce contractor personnel requirements by approximately 20 percent, particularly among those positioned on the ice," and says the investment would be repaid in about seven years "if ... a 20 percent reduction in contractor staff is in fact possible and implemented." Populations: McMurdo "varies from 130 to 1100"; South Pole about 50 in winter, about 250 summer; Palmer 15 to 45.
- DERIVED from SOURCED: person-days 1 science : 9 support is 10 percent science; applied to a 50-person winter crew that is 5 science and 45 support. (This is an illustration of the ratio, not a measured crew split.)
- SOURCED (southpolestation.com/trivia/ncs/jobs.html, fetched): universities hire winterovers for named experiments: University of Chicago hires two for the South Pole Telescope, sometimes a machinist; University of Wisconsin two for IceCube; University of Minnesota for BICEP (number not stated). Antarctic Fire Department firefighters "rotate to Pole for a few weeks in turn" in summer. DERIVED: at least 4 named science-experiment winterovers of a winter population of 45 (USAP 2022-23 planning summary, via search summary, UNVERIFIED) to about 50 (BRP, SOURCED): at most about 9 percent of winter population, and not counting BICEP.
- SOURCED (Wikipedia Firefighting in Antarctica, fetched): the McMurdo Antarctic Fire Department "had about 55 staff during the summer" when McMurdo's population is 1,200 to 1,400 (about 4 per 100 residents; DERIVED); a South Pole station 3 operates in summer; South Pole firefighting "was long handled by a volunteer brigade staffed by station personnel, who receive one week of training."
- SOURCED (IceCube/WIPAC article via search summary, UNVERIFIED as to page): all winter residents at the Pole serve on the fire response team or the trauma team.
- SOURCED (AAD, https://www.antarctica.gov.au/antarctic-operations/stations-and-field-locations/amenities-and-operations/station-duties-and-volunteer-positions/): "Everyone participates in community duties"; additional appointments include "Fire Chief" and "Lay Surgical Assistants"; "Most of these roles are undertaken by wintering expeditioners."
- SOURCED (Summit Station, geo-summit.org and Wikipedia, fetched): winter "a skeleton crew of four to six" to summer "up to 45" (geo-summit) or "typically five in wintertime and up to 52 in the summer" (Wikipedia); two science technicians visit the observatory daily; a medical clinic is in the vestibule linking two buildings.
- SOURCED (CFS Alert, Wikipedia, fetched): about 55 people stationed (2024), "only six people are responsible for actual operations," the rest are airfield, construction/engineering, food service, logistics. DERIVED: 6 of 55 = 11 percent operations staff.
- UNVERIFIED (search summaries): AAD about 70 expeditioners across the 4 stations in winter and about 300 in summer (BoM careers page); 20 at Casey and 22 at Davis in winter (older fact file); BAS Halley VI 16 in winter, 52 in summer; Rothera 22-27 winter, 130-160 summer. A recruitment list (2010, UNVERIFIED) names station leader, doctors, plant inspectors, mechanics, chefs, communications operators, carpenters, plumbers, electricians, field training officers; expeditioners may be trained in "search and rescue, firefighting and surgical assistants."
- NOT FOUND: a published support-per-scientist or support-per-technician count per station for BAS or AAD; Canadian northern camps (PCSP) ratio (search returned only "around 200 projects" and "about 30 camps supported by two logistics managers," UNVERIFIED).

## 4 Housing, maintenance, snow
### 4.1 Elevated station at the South Pole (design and jacking)
- SOURCED (southpolestation.com/foundationdesign.html, fetched): "The elevated station is designed to be raised twice by a full story height"; "Jacking is accomplished by adding new column sections, typically one story high, on top of the existing columns"; "The structure will be raised using four 57 mm rods at each foundation column"; jacking "in 250 mm increments," whole structure at once or pod by pod; columns start at 5.3 m and reach 12.8 m after both lifts; the building pad sits 1.8 m above existing snow (this delays the first lift by about 10 years); "The snow pad is developed by backfilling snow in 300 mm lifts and driving over it with front-end loaders," compacted to 0.55-0.60 g/cm3; design differential settlement 150 mm; leveling with hydraulic jacks and steel shims (75 mm of shims at each support point). The station is raised to avoid drifts: "A substantial effort is necessary each year to move drifted snow to maintain access to the facilities."
- SOURCED (southpolestation.com/trivia/00s/jackinga1.html): 4 December 2002 photo of crews preparing the jacking system to level sections during construction. No jack count or crew size given.
- SOURCED (Blue Ribbon Panel 2012): new Elevated Station dedicated 2008; summer population 150 if only the elevated station is occupied, with summer-only accommodations about 250, "limited by the operational capacities of the water and sewage systems"; the 50,000 sq ft logistics facility is in underground arches and tape and adhesives lose effectiveness in the cold; bulk items stored outdoors on elevated snow berms and "Substantial maintenance is required annually to keep the berms free of snow, conduct inventories, and locate items."
- SOURCED (IceCube winterover blog, 9 Dec 2013, https://dglo.blogspot.com/2013/12/snow-removal.html): clearing is a job at the start of the summer season done by the winter-overs once they get the machinery running; tractors drive underneath the elevated station; priorities are the runway and then drifts against buildings; the old station is "under 20-30 feet of snow."
- UNVERIFIED (search summary of a 2002 Antarctic Sun article and a 2019 ERDC study): the station settled faster than designed; snow foundation creep away from column loads.
- NOT FOUND: any actual jacking of the elevated station after construction (searched; died at the query); crew size or days needed for a full lift.

### 4.2 Summit Station, Greenland (snow management, buildings)
- SOURCED (geo-summit.org Working at Summit): the Mobile Science Facility is moved because of the "high snow accumulation environment"; the Summit Mobile Garage is built to be sledded between locations "to limit drifting and scouring"; the MSF is leveled to within 0.5 degree after each move; the skiway is 16,800 ft long and 200 ft wide; a Berthing Module slated for replacement "by a new elevated berthing facility in July 2019" (as stated on the page); summer visitors sleep in unheated Arctic Oven tents; "Medical care is provided from a Medical Clinic in the vestibule."
- SOURCED (Wikipedia Summit Camp, fetched): the 1989-era Big House was "an insulated panel building ..., elevated to minimize snow drifts"; "Accumulation is the single largest factor in elevation change"; surface rose about 1.9 cm per year from 2008 to 2018; staffed year-round since 2003.
- UNVERIFIED (search summary of National Guard releases): 2024 season, 109th Airlift Wing flew over 500 hours and moved 1.8 million pounds of cargo, 70,000 gallons of fuel and 1,200 passengers to Summit.
- NOT FOUND: Summit heavy-equipment fleet and operator count (the 2016 NSF presentation returned HTTP 503).

### 4.3 Halley VI (British Antarctic Survey) and Troll
- UNVERIFIED (search summaries of Live Science, Flowtech case study, Science Alert, NBC): Halley VI has eight modules on hydraulic legs fitted with skis; the legs can be raised to build a snow platform under each ski and the module lifted by synchronously extending the legs; the design counters snow accumulation; in 2016-17 the modules were towed about 23 km (13 weeks of work) away from a reactivating ice chasm; a new crack 17 km north (October 2016) led BAS to decide not to winter a team in 2017; winter population about 16 and summer about 52 (sources vary).
- NOT FOUND: Troll station (Norway) snow management and building-elevation details; no source reached.

### 4.4 Heavy-equipment pool and shops (McMurdo reference)
- SOURCED (Blue Ribbon Panel 2012): the McMurdo vehicle maintenance shop "consists of eight bays ... bulldozers, graders, tractors, lift trucks, trucks and vans, and shuttles. The facility is under-sized." "Many of the vehicles date from the 1950s ... spare parts are no longer commercially available"; maintenance "requires a skilled cadre of mechanics and machinists who may also be called upon to fabricate parts"; the Panel says the fleet is "woefully out-of-date" and wants "at least two and ideally four additional service bays." The traverse from McMurdo uses "heavy agricultural tractors and specialized sleds," drive time about 30 days to the Pole and 15 days back, delivering "the equivalent of 30 LC-130 missions" in 2010/11; vehicles run 12 hours a day with 12 hours for maintenance and crew rest.
- SOURCED (Wikipedia Firefighting in Antarctica): McMurdo airport fire station has seven fully tracked ARFF vehicles.
- NOT FOUND: a numeric count of vehicles in any station pool.

### 4.5 Housing and building maintenance (staffed-town examples)
- SOURCED (Governor of Svalbard, https://www.sysselmesteren.no/en/entry-and-residence): "Most housing is owned by employers and offered to employees, so it is hard to get without a job" (paraphrase of the fetch result); the state owns nearly all land; "those planning to come to the archipelago are advised to obtain work and housing before they arrive."
- SOURCED (QEC annual report): the utility owns 133 staff housing units (Iqaluit 81, Baker Lake 31, Cambridge Bay 15, Rankin Inlet 6) and has 29 transient units "some of which are vacant due to significant and ongoing renovation requirements"; plumbing and roof repairs done by its facilities team.
- SOURCED (Longyearbyen council 2025): "Tekniske tjenester og eiendom har over tid vaert underbemannet" (technical services and property under-staffed over time); resources go to day-to-day operation, so "vedlikeholdsetterslep" (maintenance backlog) is now visible in infrastructure and buildings. Also an "unusually large" surface-water problem in several places and snow-removal/roads handled by the same 9-post unit plus contractors.
- SOURCED (Inuvik town page): about 500 m of utilidor line replaced each year at about $1.5 million; Utilidor Lead Hand plus after-hours utilidor operator.

## 5 Medical, school, childcare, residency
### 5.1 Longyearbyen - health
- SOURCED (UNN information sheet "Longyearbyen Hospital," https://en.visitsvalbard.com/dbimgs/LongyearbyenHospital2026.pdf, read via pdftotext): day services 9am-4pm: doctors' office/outpatient clinic and "inpatient ward," dentist, physiotherapist, health clinic/midwife/school health service; emergency service 24/7/365 plus an emergency vehicle with an anesthesia nurse and/or a doctor. Staff "Total of 23": 1 department manager, 1 professional-development nurse, 1 counsellor (deputy), 4 doctors (3 GPs and 1 surgeon), 6 nurses (3 operating-theater nurses and 3 anesthesia nurses), 1 physiotherapist, 1 midwife (public health nurse 0-5 years), 2 public health nurses (school children), 1 dentist plus 1 health secretary, 2 health secretaries on the phone, 2 cleaners. "Hospital are dimensioned to serve the local population (around 2500 people)." After 4 pm, weekends and holidays: "1 nurse present at the hospital, + on call: 1 Doctor and 1 Nurse." Diagnostics: laboratory, skeletal X-ray, ultrasound. "Minor surgery room, no planned surgeries." Complicated or life-threatening cases are air-ambulanced to UNN in Tromso. "Major incident response: specialized medical support from the mainland depends on the number of casualties, the severity and type of injuries, and prevailing weather conditions." Tourists outside Schengen may be charged for care and air ambulance.
- UNVERIFIED (UNN web page via search summary): six beds including one ICU bed with ventilator and one isolation bed; no CT or MRI; no delivery room.
- SOURCED (council report): the fire and rescue unit "ivaretar ambulansetjenesten pa vegne av UNN HF og Longyearbyen sykehus" (runs the ambulance service for UNN and the hospital); 131 ambulance callouts in 2025.
- DERIVED: 23 staff / 2,500 = 9.2 per 1,000.

### 5.2 Longyearbyen - school and childcare (council report 2025)
- 2025-26 pupils: 194 in grades 1-10, 41 in upper secondary (32 general studies, 7 sales/service/tourism, 1 apprentice, 2 vocational completing, six mainland pupils), about 90 in the culture school, about 70 children in after-school care. "Longyearbyen skole er Longyearbyen lokalstyres storste enhet" (the school is the council's largest unit). A combined primary, lower and upper-secondary school. UNVERIFIED (job-advertisement summary): about 240-250 pupils and more than 50 staff.
- Kindergartens: two (Polarflokken, Kullungen), 72 places each, approved for up to 78 each, ages 1-6; "Barnehagene har hatt full barnehagedekning"; all applicants placed by requested start date. DERIVED: 144 places / 2,515 = 57 per 1,000 residents; school-age (235 pupils) = 93 per 1,000.
- Council notes more of the smallest children in 2025 and "noe faerre elever pa skolen," and that about half of households are one person.

### 5.3 Svalbard residence rules
- SOURCED (Governor of Svalbard, entry and residence page): "Among the requirements is that you must have the means to be able to reside on Svalbard"; Immigration Act does not apply, no visa or permit needed to travel there (Schengen visa needed when travelling via mainland); the Governor may reject people who do not meet the requirements; the page does not address sick, unemployed or elderly people.
- SOURCED (regulation of 3 Feb 1995 no. 96 on rejection and expulsion from Svalbard, read via lovdata through the fetch tool, which returned a summary and short quotes): the Governor may reject a person arriving or already present on Svalbard if the person (a) is presumed to lack sufficient funds ("ikke har tilstrekkelige midler til a oppholde seg") or a lawful way to earn a living, (c) is presumed unable to look after themselves, (d) does not live or work permanently on Svalbard and is strongly suspected of breaking Svalbard laws, among other grounds; expulsion (para 2) is for defying a rejection, for non-residents suspected of offenses, or prior convictions with risk of new offenses, with a ban of at least two years; the Governor may order a person to stay at a set place pending the decision and the rejected person bears transport costs.
- DERIVED/STATUS: the circulated claim "must leave if unemployed or sick" is not verbatim in either text read. What the texts support is the means-to-reside and ability-to-care-for-oneself grounds, combined with employer-owned housing. The full regulation text should be read on Lovdata before any wording is relied on.
- UNVERIFIED (search summary of Norwegian sources): residents have no right to economic assistance for living costs or housing; National Insurance membership continues for people who settle on Svalbard.

### 5.4 Iqaluit
- UNVERIFIED (search summaries; the gov.nu.ca page returned 403): Qikiqtani General Hospital is described by the Government of Nunavut as a 35-bed acute-care facility (20 adult, 15 pediatric), the only hospital in the territory, serving about 16,000 people in the Qikiqtani Region; 2009 article: 45 nursing positions; at the 2007 opening only 20 of 35 beds were used for lack of staff (a 2009 article gives a different reason). Medevac flows to Ottawa not found.
- UNVERIFIED (search summary of Nunavut Education Annual Report 2023-24 and Child Care Canada): 1,348 licensed child-care spaces in Nunavut, 535 in Iqaluit; a new Inuktitut daycare in Apex has 36 spaces (20 + 16 new); Inuksuk High School daycare 24 spaces; older wait-list estimates 700-800 names. Iqaluit's own population and school enrollments were not returned by search (2021 census figure not confirmed).
- Trucked water and sewage and its crew: see section 1.3.

### 5.5 Kiruna and Norilsk (size comparators, thin)
- UNVERIFIED (Ekonomifakta via search summary): Kiruna municipality 22,426 residents in 2024 (23,241 in 2014); LKAB relocation of the town is under way; the hospital is being replaced at a new site (contract awarded by Region Norrbotten, ready "before 2031" per one report); about 1,800 mine employees live in the town (one report). NOT FOUND: bed counts, fire service, municipal staffing.
- UNVERIFIED (search summary of Rosstat/Wikipedia): Norilsk Urban District 175,237 (2021 census); commonly stated 220,000 including temporary residents. NOT FOUND: hospital size, schools, kindergartens.

### 5.6 Remote stations - medical
- SOURCED (Blue Ribbon Panel 2012): "NSF provides small-clinic medical services"; telemedicine introduced; "during 2002-2004, ultrasound imaging enabled by the telemedicine capability made intercontinental medical evacuation unnecessary in one-quarter of potential cases"; the South Pole winter-over physician's cancer diagnosis and treatment plan was worked with US physicians by satellite link; the report flags the McMurdo clinic as outdated ("modernize medical clinic at McMurdo" among actions). The report names a South Pole "winter-over physician" (number of medical posts not stated); other winter residents serve on a trauma team (UNVERIFIED search summary).
- SOURCED (AAD page): "Lay Surgical Assistants" and "Fire Chief" are additional appointments held mostly by wintering expeditioners.
- SOURCED (Summit, geo-summit.org): medical clinic in the vestibule between the Green House and Berthing Module.
- SOURCED (CBC 2006 via army.ca): Alert moved cooks, janitors, drivers and mechanics to contractors; medical staffing at Alert NOT FOUND.

## 6 Failures
Dated list. Each line: date, place, event, what was learned where the source says.

### 6.1 Fires at remote stations
- Nov 1948, Hope Bay (UK): base "burned to the ground," 2 killed, one survivor lived in a tent for 16 days. SOURCED (coolantarctica.com/Antarctica fact file/science/antarctica_fire_history.php, fetched). Cause not stated.
- 1952, Port Martin (France): main building destroyed, personnel moved 60 km. SOURCED (same).
- 1958 and 3 April 1959, Mawson (Australia): main power house burned (1958 during construction; 1959 in service). SOURCED (same); cause/lessons not given.
- 3 Aug 1960, Mirny (USSR): 8 killed. SOURCED (same; Wikipedia Firefighting in Antarctica says the fire was driven by strong winds).
- Oct 1981, McMurdo: attempted arson by a winter-over, small damage. SOURCED (coolantarctica).
- 12 April 1982, Vostok (USSR): powerhouse fire about 4 a.m., "15 minute conflagration," all three main diesels and backups destroyed, power, heat and light lost; 1 killed; 20 people on station; rescue impossible for about 8 months because aircraft fuel and hydraulics freeze; crew restarted a worn engine from an ice-coring project to power a radio; mechanics in Moscow recalled a scrapped diesel buried near the station, restored it over about two months; "After 227 days the surviving 19 people were rescued." SOURCED (The Conversation, "Building a telescope in the coldest place on Earth," https://theconversation.com/building-a-telescope-in-the-coldest-place-on-earth-21482). Cause not stated there. UNVERIFIED (search summary of other sources): short circuit at the main power plant, extinguisher failed in the cold, date given as 12 or 13 April, victim named as the mechanic Alexey Karpenko; one source says one generator destroyed (conflicts with "all three").
- 12 April 1984, Almirante Brown (Argentina): station leader/physician deliberately burned the whole base so the crew would not winter again; no injuries; rescued by a US ship. SOURCED (coolantarctica, Wikipedia).
- May 1991, McMurdo Old Chapel: Quonset hut destroyed; firefighters fought for about five hours and sprayed an ice barrier on the adjacent building. SOURCED (coolantarctica).
- Sept 2001, Rothera (BAS): Bonner Marine Laboratory destroyed by an electrical fault; 3 of 5 research projects could not continue; "Prevention of injury to personnel is paramount." SOURCED (coolantarctica).
- 5 Oct 2008, Progress (Russia): 1 killed, 2 seriously injured, radio equipment destroyed so the team "could not contact outside officials for four days." SOURCED (coolantarctica).
- May 2009, Scott Base (NZ): A-frame hut burned when priming fuel flashed over on re-ignition of a heater. SOURCED (coolantarctica).
- 25 Feb 2012, Comandante Ferraz (Brazil): generator hut; unattended fuel tank overflowed during refueling, probably a short circuit; 2 killed, 1 injured; about 70 percent of the station destroyed; 44 of 59 people evacuated by helicopter; about 800 tonnes of debris later shipped to Brazil. SOURCED (coolantarctica).
- 21 June 2020, Mirny: fire damaged several labs, no injuries. SOURCED (Wikipedia Firefighting in Antarctica).
- Lessons stated in sources: emergency supplies are stored in a separate hut "well away" from the station (coolantarctica); buildings are spaced apart to limit spread (Wikipedia); "liquid water is often hard to obtain in large quantity" so dry chemical is used at the Pole (Wikipedia); a 1953 Polar Record article argued repeated losses showed "fundamental errors in the design of the huts" and a tendency to underestimate fire (UNVERIFIED, search summary).
- NOT FOUND: any fire at Halley, Davis, Casey, Concordia, Belgrano or Dome Fuji (searched; the fire lists read do not include them). Not asserted either way.
- Town-scale fire: Longyearbyen fires at road 228 and road 232; "manglende slukkevanns-kapasitet" (lack of firefighting-water capacity) was a significant problem at 228; densification added operational difficulty at 232 (council report 2025, SOURCED; dates not given in the text read). 22 fires/near-fires in 2025.

### 6.2 Water failures
- Longyearbyen 2024-2026: Legionella April 2024; manganese from autumn 2024; Feb 2025 Legionella and manganese; June 2025 sulfate; Sept 2025 manganese and nickel, advice not to drink tap water, emergency supply via brewery and local purification units, 150 m3 from the brewery vs 141,720 m3 produced; only ice pond source; staffing "lav bemanning pa VA" and overtime. SOURCED (sections 1.1).
- Iqaluit 12 Oct 2021: state of emergency after fuel-like products found in treated water; contamination pathway severed 24 Oct; Do Not Consume order lifted 10 Dec 2021; cause an old underground fuel tank next to the North Clearwell wicking light hydrocarbons through concrete. UNVERIFIED (search summary of WSP, Global News, Grainews; primary pages not opened). Military sent a purification system (same summaries).
- Iqaluit trucked service collapse when drivers were short (iqaluit.ca notice; SOURCED, undated, section 1.3).
- Utqiagvik: permafrost thaw makes buried pipes shift and break, leaks degrade permafrost further (Danner quote "The permafrost is not going to heal itself"). SOURCED (ADN, 2024).
- Inuvik: UNVERIFIED (search summary) original utilidor about 30 years past its service life; original wood piles heaving and sinking.
- South Pole: summer population capped near 250 by water and sewage capacity (BRP, SOURCED).

### 6.3 Power and heat failures
- 28 Dec 2024, Nuuk: fallen conductor on the hydropower transmission line; emergency plant did not auto-start because of skewed voltage; the 2021 Nuuk outage lasting several days was "the first of its magnitude since the plant was built in 1993" (UNVERIFIED search summary for the 2021 event); Nuuk emergency supply now eight temporary container generators. SOURCED (Nukissiorfiit 2024 report).
- 2024: outages also in Aasiaat, Qaqortoq, Ilulissat. SOURCED (same).
- May 2025 (district heating in parts of Longyearbyen) and December 2025 (whole-town power stoppage). SOURCED (council report; causes not given in text read).
- 11 Feb 2026, Utqiagvik west side: outage from 2:15 a.m., heat, power, phones, internet lost; borough offices closed; door-to-door freeze-up checks. SOURCED (NSB PSA).
- 29 May 2020, Norilsk: diesel tank at a Nornickel thermal power plant ruptured, more than 20,000 tonnes of diesel (about 6,000 t into the ground, 15,000 t into waterways per TASS); Nornickel blamed melting permafrost undermining the tank supports; state of emergency declared 3 June; three criminal cases and a plant employee detained; the largest Russian spill except 1994 Komi. SOURCED (Al Jazeera, 4 June 2020). UNVERIFIED (search summary of Warsaw Institute): the cause was not settled, the tank pillars were about 30 years old and earlier checks reported corrosion; conflicting low-quality source blames corrosion holes.
- Alert: heating cost forced civilian-contractor shift (2006; SOURCED).
- Vostok 1982 (above): loss of power was the whole emergency.
- QEC: no back-up grid in any community (SOURCED); Nukissiorfiit stresses outages are "a major issue."

### 6.4 Natural-hazard and site failures
- 19 Dec 2015, Longyearbyen avalanche: 2 killed, 11 houses lifted off their bases, insurance costs near NOK 50 million; aftermath: new risk-assessment map and an avalanche warning system run by NVE; remains removed. SOURCED (UNIS article, 16 Feb 2017). UNVERIFIED: a Feb 2017 avalanche damaged two houses and led to evacuation of parts of town; a 2020 Safety Science paper says the second event "demonstrated the limitations of the established system in 2015" (search summaries).
- Jan 2025, Longyearbyen: Nybyen evacuated and movement banned because of avalanche danger. SOURCED (council report).
- Halley VI Oct 2016: new ice crack, no winter team in 2017; station moved 23 km in 2016-17. UNVERIFIED (search summaries).
- South Pole elevated station settled faster than designed (UNVERIFIED, Antarctic Sun 2002 via search summary).
- McMurdo: melting permafrost listed fuel-line stanchions; rising lake levels in Dry Valleys required moving camps; warm temperatures limited the ice pier and runway. SOURCED (BRP 2012, section 4.9.4).

### 6.5 What the sources say was learned (only where stated)
- Longyearbyen: firefighting-water capacity, a reserve water source, and a replacement distribution network became projects; more technical staff is the stated response (council and lokalstyre pages).
- Nuuk: backup generation must start automatically under abnormal voltage; more container generators and a new emergency diesel plant (Nukissiorfiit 2024).
- Iqaluit trucked service: the city says trucked delivery is "highly inefficient" (Nunatsiaq, 2015).
- Vostok: no written "lessons" in the sources read; the response in the account was to restart old engines and, in the fire-precaution literature, to keep emergency supplies separate (above).

## 7 Waste
### 7.1 South Pole and McMurdo
- SOURCED (Polar Journal, "Waste disposal at the South Pole," https://polarjournal.net/waste-disposal-at-the-south-pole/, fetched): "There are no dumpsters at the South Pole, so anything that needs to be disposed of is palletized and flown out"; LC-130s carry the pallets to McMurdo, then ships or aircraft take them to the United States; a four-member team packed 137 pallets between 22 Nov and 27 Dec; the trash team's usual 10 days was extended to 35; cargo had piled up and been buried by wind because aircraft "could not fly to the South Pole station in 2021 and 2022"; NSF asked the 109th Airlift Wing for help in 2015 with a five-year plan; pallet lashing at -40 degrees was hard.
- SOURCED (Blue Ribbon Panel 2012): "There is a large accumulation of nonhazardous waste at the South Pole that must be flown out or removed by traverse. The 'waste berms' where this material is stored require annual maintenance so that the waste does not become permanently buried by drifting snow"; a shredder pilot to reduce volume before retrograde to McMurdo was funded; "modern compactors and incinerators would also likely be advantageous"; action to "Expedite removal or conversion into energy of the significant volume of waste remaining at South Pole Station." McMurdo "receives more than 11 million pounds of cargo a year, more than 60 percent of it on a single ship with icebreaker escort"; the backload "has retrograded more tonnage than it delivered, ranging from waste not permitted to remain in Antarctica to scientific samples." Waste streams include food and human waste, scrap wood, cardboard, paper, metal cans, construction remnants. Port Hueneme (California) warehouse handles about 40 million pounds a year and receives sorted hazardous and non-hazardous waste. The portable modular causeway used at McMurdo in 2010/11 displaced the shipping containers that would have carried waste out. Wastewater solids from McMurdo are boxed and shipped to the US (UNVERIFIED search summary of a Case Western blog).
- SOURCED (BRP): air versus sea: air cargo costs "approximately four or ten times the cost per pound" of ship cargo depending on aircraft; "Transporting cargo via LC-130 costs $5.25 per pound, whereas via the C-17 it costs $2.37 per pound."
- DERIVED (arithmetic; 2012-report dollars; cargo cost, not a waste rate): $5.25/lb x 2,204.6 lb per tonne = about $11,570 per tonne by LC-130; $2.37/lb = about $5,225 per tonne by C-17 (C-17 flies only to McMurdo, not the Pole). South Pole waste moves by LC-130 to McMurdo; the ship leg is cheaper but its rate was not found.
- UNVERIFIED (search summaries of Waste360 and Recycle Nation, pages returned 403 when fetched): the yearly ship carries about 4.86 million pounds of waste home; about 420 shipping containers a year; shipping cost about $800,000; recycling offsets about 10 percent of shipping cost. DERIVED chain (UNVERIFIED inputs, undated): 4.86 million lb = about 2,200 tonnes; $800,000 / 2,200 t = about $360 per tonne by sea. Treat as a rough pointer only.
- NOT FOUND: a published per-tonne cost for shipping waste off a plateau station; annual tonnage retrograded from the Pole.

### 7.2 Australian stations (AAD)
- SOURCED (AAD Waste Management Strategy and Return-to-Australia Plan 2026-2031, https://www.antarctica.gov.au/site/assets/files/116146/aad_waste_management_strategy_and_rta_plan_-_2026_-_2031_-_final.pdf, read via pdftotext): Table 1 of returned-to-Australia waste (tonnes), 2020-21 / 2021-22 / 2022-23 / 2023-24 / 2024-25: liquid waste treated and disposed 8 / 62 / 14 / 6 / 31; sent to recycling 15 / 109 / 39 / 23 / 38; sent to landfill 30 / 129 / 143 / 99 / 84. 2021-22 and 2022-23 had three ships; "Typical RTA waste volumes are reflected in years 2020-21, 2023-24 and 2024-25." Targets for 2026-27: liquid 15 t, recycling 25 t, landfill 71 t. Incineration occurs at all three stations for biohazardous, kitchen, sanitary, hydroponic and medical waste; "The vast majority (80%) of the AAD station's incinerated waste is vegetable matter"; incinerators are "used to the minimum necessary"; the plan says reducing return volume reduces "shipping and associated fuel costs." Storage and return rely on shipping containers whose certification can lapse. Per-tonne cost not published.
- DERIVED: typical year 2024-25 returned 153 t (31 + 38 + 84) across three stations whose winter population totals about 70 for four stations including Macquarie (BoM careers page, UNVERIFIED) and summer about 300; that is about 0.5 tonne per summer-peak person per year (arithmetic with UNVERIFIED population; shown only to illustrate magnitude).

### 7.3 Longyearbyen, Ny-Alesund, Alert, Iqaluit, Alaska
- SOURCED (Longyearbyen council report 2025): household waste about 18 percent of total waste handled; of waste through the waste station about 24 percent material-recycled, 72 percent energy-recovered, about 4 percent landfilled; summer cruise tourism generates much waste and more than budgeted; the station also receives beach-clean waste; a reuse shop operates with the folk high school; the unit has 9 permanent posts of which 3 are waste-station operators.
- SOURCED (Port of Longyearbyen tariff 2026, https://portlongyear.no/wp-content/uploads/2026/04/Prisregulativ_Logyearbyen_2026_EN_03.pdf): ship waste delivery: "Price per m3 sorted waste NOK 2.119,74"; "Price per kg sorted waste NOK 21,90"; hazardous waste per delivery NOK 160,68; fine NOK 21.279,80 for incorrectly sorted waste. This is a port reception fee for vessels, not a freight rate.
- UNVERIFIED (search summaries): Longyearbyen handles about 2,000 tonnes a year, sorts and bales, and ships containers to the mainland (Sweden cited for cheaper disposal); Statistics Norway says about 80 percent of Svalbard waste goes to energy recovery on the mainland.
- SOURCED (Svalbardposten 2015): Ny-Alesund sewage sludge pumped out and composted; sewage plant 10,000 L/day.
- UNVERIFIED (search summary): at Alert the 2006 cuts followed heating costs; waste practice NOT FOUND. Iqaluit gasifier processes about half a tonne a day while the city produces about 50 times that (Deeply article, via search summary); open burning common in small Nunavut and Alaska communities (Arctic Council report, via search summary); Alaska remote camps under 50 residents may not burn on the ground, only in an incinerator or contained device (Alaska DEC general permit, via search summary).
- UNVERIFIED (search summary of an Alaska commission letter): Backhaul Alaska served more than 50 communities in 2023 at about $1.12 million; about 110 communities and about 907 tons backhauled to date; EFAB consultation slide shows $65,915 per village for a 17-village pilot vs $22,867 per village at larger scale. Per-ton rate not published in what was read.

## FINAL
### Factual table (place, population, who lives there, jobs and counts, services present, social and civic life, what failed)
Marks: S = SOURCED, U = UNVERIFIED, D = DERIVED. Details and URLs are in the numbered sections above.

| Place | Population | Who lives there | Jobs and counts | Services present | Social and civic life | What failed |
|---|---|---|---|---|---|---|
| Longyearbyen, Svalbard | 2,515 at end of 2025 (S) | About 63 percent Norwegian citizens; about half of households one person; stable number of children; no residence right, must have means to reside, employer-owned housing (S) | Council about 140 FTE / 170 employees (S); technical-services unit 9 permanent posts plus contractors (S); fire/ambulance 25 (4 full-time, 21 part-time) (S); hospital 23 staff (S); energy plant 13 posts cut in the diesel change (S, HNN) | Water (single pond source), sewer, district heat and power from one diesel-fired plant (S); hospital, ambulance run by fire service, school grades 1-13 (235 pupils), 2 kindergartens (144 places) (S); port, waste station 24/72/4 percent recycled/energy/landfill (S) | Elected local council; culture school about 90 pupils; many one-person households (S) | Manganese/Legionella/nickel water events 2024-25; whole-town power stoppage Dec 2025; district-heat outage May 2025; 2015 avalanche (2 dead, 11 homes); fire-water shortfall at two fires; staffing shortfall in technical services (S) |
| Ny-Alesund, Svalbard | 123 in 2015, maximum 200 (S) | Researchers plus company staff | Kings Bay AS 20-25 permanent (U) or 32 (2007, S) | Power, district heat, water, sewer, fire protection, housing, catering, airport, harbor (S) | Not found | Direct sewage discharge to fjord until a plant was built (S); no failure event found |
| Inuvik, NWT | Not read | Not read | Utilidor lead hand + after-hours operator; headcount not published (S) | 950 water/sewer connections, 16 km above-ground utilidor, heating stations (S) | Not found | Utilidor aging and permafrost heave (U) |
| Iqaluit, Nunavut | Not confirmed | Not read | Staff counts not published; city hiring trucked-service drivers (S) | Utilidor plus truck service; 11 percent of people on trucks using about 40 percent of the water/sewer budget (2015, S); 35-bed hospital (U) | Not found | 2021 fuel in water (U); trucked service suspended for lack of drivers (S) |
| Utqiagvik, Alaska | Not read | Not read | Utility reports 113 employees (U) | Buried water/sewer from mid-1980s failing under thaw; above-ground pilot for 27 homes (S) | Not found | 11 Feb 2026 west-side outage; pipe breaks (S) |
| Nuuk and Greenland towns | Not read | Not read | Nukissiorfiit 411 employees, 20,600 customers (S); 50 customers per employee (D) | 5 hydro plants 91.3 MW, 27 heating plants, 72 waterworks (S) | Not found | 28 Dec 2024 Nuuk blackout; outages in 3 other towns in 2024 (S) |
| Nunavut communities | About 16,000 customers (S) | Not read | QEC headcount not in annual report; staff housing 133 units (S) | 25 isolated diesel plants, no back-up grid (S) | 57 percent of utility workforce Inuit (S) | Not found for the year |
| CFS Alert | About 55 people (2024, S) | Military, civilians, contractors | 6 of 55 on operations (S); contractor runs maintenance (S) | Power plants, water treatment, boilers (S) | Tours of months (U) | Heating cost forced trades to contractors (2006, S) |
| Pituffik, Greenland | About 600-700 (U) | Contractors majority (U) | Not found | Not found | Not found | Backup power plant upgrade contract (U) |
| South Pole | About 50 winter; 150 elevated station summer; about 250 with summer annex (S) | Contractor staff plus a few science winterovers (S) | At least 4 named experiment winterovers (S/D); all winter residents on fire or trauma team (U) | Elevated station on columns, 5,000 meals/week, 450,000 gal fuel/yr (S) | Shared community duties (AAD, S) | Vostok 1982 powerhouse fire (S); capacity capped by water/sewer (S) |
| McMurdo | 130 to 1,100 (S) | Contractor, NSF, military | Fire dept about 55 summer (S); vehicle shop 8 bays (S) | Reverse-osmosis water, wastewater plant, clinic (S/U) | Not found | Oldest-vehicle fleet; waste backlog (S) |
| Summit Station | 4-6 winter; up to 45-52 summer (S) | Science and support | Two technicians visit the observatory daily (S) | Clinic, kitchen, berthing, sled-moved science buildings (S) | Not found | Not found |
| Halley VI | About 16 winter, about 52 summer (U) | BAS staff | Not found | Eight modules on hydraulic legs with skis (U) | Not found | 2016-17 ice-crack relocation, no winter team (U) |
| Rothera / AAD stations | 22-27 winter, 130-160 summer (U); AAD about 70 winter total (U) | Expeditioners | Trades and doctors listed (U) | Incinerator at every AAD station (S) | Rotating community duties (S) | 2001 Rothera lab fire (S) |
| Norilsk | 175,237 (2021, U) | Not read | NTEC headcount not found | 3 CHP plants 1,154 MW thermal, isolated grid (S) | Not found | 29 May 2020 diesel tank collapse, over 20,000 t (S) |
| Kiruna | 22,426 (2024, U) | Not read | Not found | Not found | Not found | Town relocation under way (U) |
| Reykjavik / Faroe | Not read | Not read | Veitur 65 percent of population served (S) | Not found | Not found | Not found |
| US municipalities 5,000-9,999 (Census 2023 sample) | Sum 2.78 million over 374 units (D) | Not applicable | Per 1,000: police sworn 2.38, firefighters 1.12, highways 1.03, water 0.76, sewerage 0.60, solid waste 0.38, parks 0.76 (D) | Not applicable | Not applicable | Not applicable |

### NOT FOUND list
1. Operator or driver headcounts for any named municipal water/sewer system (Iqaluit, Inuvik, Utqiagvik, Longyearbyen plant, Norilsk, Yakutsk, Pituffik, Alert).
2. Control-room staffing for any microgrid (Longyearbyen, Nuuk, Faroe, Utqiagvik, Iqaluit); customers per grid operator other than company-wide ratios.
3. Longyearbyen energy plant staff (only the 13-post reduction) and Svalbard Energi headcount.
4. ICMA, BLS, Canadian municipal and Nordic per-1,000 ratios for public works, ambulance and public health (ICMA/AWWA data are member-only).
5. A published support-staff-per-scientist or per-technician count by station for BAS, AAD, USAP beyond the 1:9 person-day ratio and the Pole experiment winterovers; Canadian northern camp ratios.
6. Summit Station equipment fleet and operator numbers; Troll snow and elevation details; Halley VI primary BAS page; any actual jacking of the South Pole elevated station after construction.
7. Cost per tonne for shipping waste off a plateau station (only air cargo $/lb and an unverified sea rate).
8. Fires at Halley, Davis, Casey, Concordia, Belgrano and Dome Fuji; fire at Belgrano specifically.
9. Iqaluit and Kiruna hospital staff or bed counts at primary sources; Norilsk hospital, schools and kindergartens; medevac volumes.
10. Yakutsk and Norilsk heat network design and utilidor staffing; Reykjavik district-heating customer count and Veitur headcount.
11. The verbatim Svalbard rule that residents must leave if unemployed or sick.
12. Alaska Backhaul per-ton rate; Longyearbyen shipping cost per tonne.

### Unresolved conflicts
1. Longyearbyen coal end date: 19 Oct 2023 (reports in search summary) vs "coal use ended in 2025" (Antle slide) vs Mine 7 extended to summer 2025 as backup (HNN). Not resolved.
2. Longyearbyen population: 2,515 (council, S) vs 1,750 (Antle slide) vs "around 2,500" (hospital sheet). The 2025 council figure is the primary.
3. Vostok fire: one source says all three diesels and backups destroyed (The Conversation), another says one generator (Meduza via search summary); date 12 vs 13 April 1982; victim name from one source only.
4. Norilsk tank collapse cause: Nornickel says melting permafrost under the supports; a secondary source says earlier checks showed corrosion and the cause was not settled.
5. Pituffik contractor: Inussuk Group vs V2X, and population 600 vs 700+.
6. Nunavut diesel capacity: 84,000 kW (QEC 2024-25, S) vs 76,000 kW and about 53 MW in older summaries.
7. Nukissiorfiit employee counts differ by table definition across years (2020 report 437 vs a 2021 table 416 for the same year, via search summary).
8. Ny-Alesund sewage plant: 10,000 L/day (Svalbardposten) vs 65 population equivalents (manufacturer, search summary) vs designed for 200 people.
9. South Pole winter population: about 50 (BRP 2012), 45 (USAP 2022-23, U), 42 (podcast, U), 40-50 (EurekAlert caption, U).
10. Iqaluit hospital beds: 35 (GN) vs about 20 in use (various years).
11. The AWWA 509 connections per employee, the Oregon 229 residents per FTE and the Pennsylvania 3.5 per 1,000 are single-document figures from search summaries and do not agree in definition.
