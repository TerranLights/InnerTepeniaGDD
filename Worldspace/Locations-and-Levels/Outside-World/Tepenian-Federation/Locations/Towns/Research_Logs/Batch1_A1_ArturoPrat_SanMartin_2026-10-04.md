# Research log: Batch 1, A1: Arturo Prat and San Martín (2026-10-04)

**Method.** One research agent, no search budget, 45 web searches plus direct data pulls. All accessed 2026-10-04. Read as raw text: COMNAP facilities CSV (GitHub v3.5.0, 2024-05-15), SCAR Composite Gazetteer API (`placenames.aq/api/place_names`), the 1993 Art. VII joint inspection report, the 1987 ASPA 144 plan, the 2015 IBA volume, three Revista de Marina PDFs (via Wayback). Everything else came through a summarizing fetch tool. Official Chilean and Argentine program pages carry almost no ground-stability data: **the stability verdicts rest on gazetteer text, the inspection report and indirect evidence, not bedrock measurements.** Operators are context only. Findings are in `../Towns_Priority_Batch_1_Reference_2026-10-04.md` (#1, #7).

## Verdicts
| Station | Verdict | Confidence |
|---|---|---|
| Arturo Prat (#1) | qualifies with caveats: ice-free shingle peninsula, glacier immediately adjacent | about 85% not on ice; about 60% bedrock shallow |
| San Martín (#7) | qualifies (qualified): rock-cored island in Marguerite Bay | about 75% rock; low on rock type and depth |

## Contradictions (unresolved)
1. Prat coordinates: most 62°28.7'S 59°39.8'W; Spanish Wikipedia/Hispanopedia 59°37'49"W (1.7 km east); INACH/UOH "62°30'S 59°39'W" (rounded). Prat elevation 0, 3, 5 or 33 m.
2. Prat closure/reopening: closed 23 Feb 2004 (decision 2003), reopened 12 Mar 2008. Some sources (POLARIN, Wikipedia lead, INACH catalogue) still say "summer base since 2004"; Navy Nov 2024 relief describes year-round.
3. Prat winter 8 / 9 / 11, summer 20 / 30 / 32 / 35; INACH lab 8 vs 11 beds.
4. González Pacheco's death: 1960 (Revista de Marina 1972 no.6) vs 9 Apr 1961 (1972 no.1; Aimone 2008). The 150 m fall figure appears only in Aimone 2008.
5. Nearest station to Prat: the 1993 report says Juan Carlos I at 37 km, ignoring Maldonado (5.1 km; COMNAP est. 1990). Unresolved.
6. Risopatrón is 11.3 km from Prat by COMNAP coordinates (not 8 km: that figure is the Maldonado to Risopatrón distance).
7. Poisson Hill: "ice-covered" (US gazetteer) vs "ice-free" (Wikipedia).
8. The Clinic (2013) puts Prat on King George Island (wrong; it is Greenwich Island).
9. POLARIN wind "mean 42.1 m/s, max 92.6 m/s" implausible as m/s (92.6 = exactly 50 kn).
10. San Martín reopening 1973 (SCAR UK) / 1975 (1993 report) / 21 Mar 1976 (Army, Cancillería). Closure cause: logistics vs Feb 1959 fire (SCAR UK). Spanish Wikipedia lists fires 1952, 1958, 1959.
11. **2008 fire at San Martín (asserted in the brief): not found in any source.** Possible origin (inference): Irízar fire 10 Apr 2007.
12. San Martín coordinates 67°06' (COMNAP) vs 67°08' (Army page). Capacity 20 / 21 / 19 / 23. Climate: "winter average -37 °C" vs annual means -3 to -6 °C. Refuges: 7 (Wikipedia, Cancillería) vs 9 (blog). Uspallata Glacier flows into Neny Bay (US) vs into Northeast Glacier (UK).

## Dead ends (where each died)
- 2008 fire/damage at San Martín: died at the sources (8+ queries, 4 direct pages).
- Bedrock depth or any geotechnical survey at Prat: died at the sources.
- Geology of Barry Island/Debenham Islands: died at both (queries returned regional Marguerite Bay geology; the Cambridge Quaternary Research paper returned 403).
- Glacier velocity near either station: died at the sources (Greenwich studies do not name or measure Fuerza Aérea Glacier; a Spanish query surfaced Upsala Glacier, Patagonia: query mismatch).
- Current Art. VII inspection reports for Prat and San Martín: died at query and sources (ATS inspections database 404/login; only the 1993 UK/Italy/Korea report retrieved).
- Current ASPA 144 plan: died at the sources (only the 1987 plan, expired 1997).
- Blocked fetches: revistamarina.cl 403 (read via Wayback); helis.com, zona-militar.com, hcdn.gob.ar PDF unreachable; Chilean Navy/INACH pages gave no usable Prat data.
- Chile Bay raised-beach/permafrost literature: died at the sources (only POLARIN "discontinuous permafrost").
- Prat storm-surge/sea-level damage: not found.
- POLARIN San Martín page: ID scan 1 to 200 timed out; only Prat (Station/110) retrieved.
- Marguerite Bay sea-ice review (Turkish paper): located, not read in full.
- "Uspallata Glacier airstrip": Wikipedia and an Argentine blog only; no primary source.

## Search strings (2026-10-04)
1. `Arturo Prat Antarctic base Greenwich Island coordinates elevation COMNAP facilities`
2. `San Martín Base Barry Island Marguerite Bay coordinates 68°07'S 67°06'W`
3. `Base San Martín Antártida incendio 2008 Barry Island historia reconstrucción`
4. `Base Arturo Prat Isla Greenwich Armada de Chile base antártica dotación invernada`
5. `San Martín base Argentina Antarctica fire 2008 evacuated Rothera`
6. `"Base San Martín" Antártida incendio 2008 destruyó`
7. `COMNAP Antarctic Facilities Information San Martín Argentina Barry Island`
8. `Greenwich Island South Shetland geology Iquique Cove Arturo Prat base raised beach volcanic rock glacier ice cap`
9. `Base Prat Greenwich erosión costera deslizamiento temporal daños infraestructura Caleta Iquique`
10. `Antarctic Treaty Article VII inspection report Arturo Prat Station Chile Greenwich Island`
11. `Iquique Cove Greenwich Island SCAR gazetteer Arturo Prat Station`
12. `ats.aq inspection Arturo Prat Station Chile inspection report Greenwich Island Chilean Navy permanent station reopened 2008`
13. `Prat base Greenwich Island Chile new buildings construction 2008 reopening winter personnel INACH modernization`
14. `Greenwich Island glacier retreat Discovery Bay ice cap Guesalaga Peninsula Chile Bay glaciers`
15. `Greenwich Island Discovery Bay geology Chile Bay Quaternary glacial deposits raised beaches volcanic Greenwich Island geomorphology paper`
16. `ASPA 144 Chile Bay (Discovery Bay) Greenwich Island management plan Arturo Prat Station glacier`
17. `permafrost active layer Greenwich Island Arturo Prat Chile Bay borehole raised beach Discovery Bay`
18. `Maldonado station Greenwich Island Ecuador Cierro Spur geology rock outcrop Fort Hill Formation Discovery Bay Greenwich Island`
19. `Base Prat Armada de Chile dotación invernal 2024 2025 Antártica relevo base Capitán Arturo Prat`
20. `Base Prat Greenwich Island 2023 2024 2025 Chile news storm damage OR renovation OR "nueva base" Prat Antarctica`
21. `Antarctic Treaty inspection "San Martín" Argentina Barry Island inspection report observers visited Marguerite Bay`
22. `"San Martín" base antártica argentina 2008 incendio personal Ejército Antártida Barry`
23. `Argentine Antarctic base San Martin fire destroyed building 2008 OR 2009 OR 2010 OR 2011 Marguerite Bay Debenham Islands`
24. `Almirante Irízar fire April 2007 Argentine Antarctic bases resupply San Martín effect campaign 2008 Ushuaia Antarctic bases supplied`
25. `Campaña Antártica de Verano Base San Martín relevo dotación helicópteros rompehielos Irízar bahía Margarita hielo marino`
26. `Marguerite Bay sea ice fast ice Debenham Islands San Martín Argentine station winter sea ice breakup resupply helicopter Twin Otter ski runway`
27. `Debenham Islands Marguerite Bay geology granodiorite OR granite OR diorite Barry Island Millerand Island British Graham Land Expedition 1936 rock`
28. `Barry Island Debenham Islands Antarctica low rocky island ice-free Uspallata Glacier distance San Martín station glacier flow`
29. `González-Ferrán Katsui 1971 Greenwich Island geology South Shetland "Base Prat" volcanic Quaternary glaciers`
30. `Greenwich Island Antarctica Fuerza Aérea glacier OR "Quito Glacier" OR "Chile Bay" glacier terminus retreat Discovery Bay Arturo Prat 1956 2019 Landsat`
31. `Base San Martín nuevo laboratorio construcción 2024 2025 Antártida LASAN ampliación base conjunta Debenham`
32. `glaciar Uspallata OR "Northeast Glacier" velocidad movimiento Base San Martín glaciología Instituto Antártico Argentino Freiburg mediciones`
33. `Stonington Island East Base Historic Site and Monument HSM number Base E Marguerite Bay Antarctic Treaty historic sites list`
34. `"Debenham Islands" granodiorite OR tonalite OR gabbro OR "granite" Fallières Coast geology plutonic Marguerite Bay Lassiter OR Fallieres pluton`
35. `Debenham Islands Important Bird Area Antarctica site description Barry Island rocky vegetation ice-free areas penguins skuas`
36. `British Graham Land Expedition southern base Barry Island Debenham Islands hut Penola 1936 "Barry Island" rock island description Rymill Southern Lights`
37. `Historic Site and Monument 32 33 34 35 Greenwich Island Arturo Prat Chile monolith shelter bust Virgin of Carmen Antarctic Treaty list of historic sites`
38. `Greenwich Island Prat Chile Antarctic station tide gauge sea level meteorological data Arturo Prat 1966 temperature record wind snow Bahía Chile climate`
39. `incendio Base Prat Antártica Armada de Chile Greenwich fuego base naval Arturo Prat`
40. `Capitán González Pacheco 1960 murió base Prat Antártica refugio González Pacheco accidente`
41. `Base San Martín Antártida clima temperatura media anual -5 viento máximo nevadas Servicio Meteorológico Nacional estadísticas 1976 San Martín 89...`
42. `San Martín Antarctic station climate Marguerite Bay mean annual temperature Debenham Islands meteorological record`
43. `tutiempo.net climate Capitan Arturo Prat Antarctica station annual averages`
44. `INACH Base Prat laboratorio Greenwich "Prat" estación científica capacidad personas ZAEP inach.cl`
45. `polarin-gis.org San Martín Station Argentina Barry Island Debenham`

## Sources (accessed 2026-10-04)
- COMNAP facilities CSV (Prat record 28; San Martín 16; Maldonado 38; Risopatrón 33; Cámara 6; Frei 27; Turkish camp 237): https://raw.githubusercontent.com/PolarGeospatialCenter/comnap-antarctic-facilities/master/dist/csv/COMNAP_Antarctic_Facilities_Master.csv
- SCAR Composite Gazetteer: https://placenames.aq/
- 1993 Art. VII inspection report (UK/Italy/Korea): https://repository.kopri.re.kr/bitstream/201206/4357/1/2-115.pdf
- ASPA 144 plan (1987, expired 1997): http://www.ats.aq/documents/recatt/Att145_e.pdf
- Chilean Met Service (DMC) AWS sheet: https://climatologia.meteochile.gob.cl/application/informacion/fichaDeEstacion/950014
- POLARIN Prat: https://www.polarin-gis.org/Home/Station/110 ; EU-PolarIN: https://eu-polarin.eu/captain-arturo-prat-navy-station-laboratories-cl/
- Revista de Marina 1972 no.1 (https://revistamarina.cl/revistas/1972/1/cronica4.pdf), 1972 no.6, 2008 no.6 Aimone (https://revistamarina.cl/revistas/2008/6/aimone.pdf), read via Wayback
- Greenwich Island glacier change papers: https://www.scielo.br/j/aabc/a/dndjrXyncP3ZryjvwSfNSrf/?lang=en ; https://redi.cedia.edu.ec/document/199956
- seawaves.com (Nov 2024 relief): https://seawaves.com/?p=17296 ; Hispanopedia (secondary): https://es.hispanopedia.com/wiki/Base_naval_Capit%C3%A1n_Arturo_Prat ; tutiempo WMO 890570: https://en.tutiempo.net/climate/ws-890570.html ; HSM list: https://www.legislation.gov.uk/uksi/2017/706/schedule/2/made
- San Martín: Argentine Army page https://www.argentina.gob.ar/ejercito/antartida/base-san-martin ; Cancillería https://cancilleria.gob.ar/es/iniciativas/dna/antartida-argentina/bases/san-martin ; blog http://antartida-argentina.blogspot.com/2018/03/la-base-san-martin.html ; relief news https://www.argentina.gob.ar/noticias/inicio-el-reabastecimiento-de-la-base-san-martin (2020), https://elciudadanoweb.com/antartida-del-complejo-relevo-de-dotacion-de-la-base-san-martin-a-la-vista-a-la-tumba-de-pujato/ (2023), https://www.argentina.gob.ar/noticias/el-rompehielos-ara-almirante-irizar-reabastecio-la-base-antartica-conjunta-san-martin (2025), https://gacetamarinera.com.ar/nota/2086 (2026, summary); aidca account https://aidca.org/ridca4-antartico7-ridca4-antartico-mauro-figueroa-morales-base-antartica-san-martin/ ; tutiempo WMO 890660 https://en.tutiempo.net/climate/ws-890660.html
- IBA 2015: https://www.era.gs/resources/iba/Important_Bird_Areas_in_Antarctica_2015_v5.pdf ; UOH/INACH annex: https://www.uoh.cl/investigacion/wp-content/uploads/sites/12/2025/08/ANEXO-N-u-4-Plataformas-Antaarticas.pdf
- Distances marked haversine are from COMNAP coordinates (agent arithmetic).
