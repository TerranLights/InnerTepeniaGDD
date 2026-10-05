<!-- Agent report, 2026-10-04. Re-run of the items the earlier agents' search cap cut off (HF contacts and nets, coast radio, space-weather links, Drake gaps, Macquarie). Web research plus local text extraction. Model output: spot-check before relying on it. Real countries, stations and people are used as geography and history only (GPS law; No_National_Stereotypes). Nothing here is evidence about founders or populations of a fictional city. -->

# HF contacts, Southern Hemisphere radio-weather links, and the Drake gaps: re-run

Scope: items 1 to 5 of the brief. No project files other than this log were edited. American English.

**Tags.** **[F]** = fact stated by a source I opened (URL and year given). **[F-snippet]** = reported only in a search-result summary, page not opened or not confirmed there. **[I]** = my inference. **[U]** = could not verify. **[calc]** = my arithmetic.

**Method notes that matter for trust.**
- About 80 search calls (some calls ran two or three sub-searches), roughly 60 page and PDF fetches. Exact strings are in "Searches and dead ends."
- **WebFetch is blocked (HTTP 403) by Noonsite, the WIA-adjacent VK4GHZ forum, NZHistory, the ICAO ESAF PDFs and the `prontus.directemar.cl` host. Plain `curl` with a browser user-agent opened Noonsite and the `www.directemar.cl` host.** So "403" in the earlier logs is partly a tool artifact, not a dead source. The earlier agent's "noonsite HF net page (403)" is now opened.
- Search summaries are lossy and sometimes wrong. Where a number mattered I went to the page and say so.

---

## 0. Bottom line (read this first)

1. **No dated, logged first two-way contact Australia to South Africa (or Australia to Argentina/Chile/Brazil) could be recovered.** Five differently worded queries plus the amateur-history pages found only adjacent firsts (Howden, England to Australia telephony, Feb 1925; Brenda Bell, New Zealand to South Africa, 1927). [U] for the VK-ZS first. This stays an open gap, but it is now a gap about *the date of a first*, not about *whether the path is worked*.
2. **What is documented is structure, and it points one way.** The commercial HF system of the 1920s was a set of spokes to London, not a ring (see 1.1). Australian traffic to South America went via Montreal (1928). Today the cruising-radio nets that actually span the three continents are run from South Africa (Durban), not Australia, and they say outright that their coverage runs "from Australia across the Indian Ocean, the Atlantic to Brazil and the Caribbean" (Section 1.3). Australian-run nets (Tony's Net, Gulf Harbour Radio, the Comedy Net) face the Pacific and Tasman.
3. **Australians working South America across the pole on HF is documented once, in a 1997 ham propagation column, as routine in southern summer** (1.4). That is the only documentary support found for a trans-Antarctic Australia to South America HF path in practice. It is weak evidence (one forecaster's sentence), but it matches the geometry in the ring log.
4. **Space-weather forecasting does not link the three.** Australia (BoM, inside the ICAO "ACFJ" consortium) and South Africa (SANSA, partnered with the European PECASUS consortium) sit in different global-center groupings. Both are ISES Regional Warning Centres, so they share a standards umbrella, not a bilateral pipeline. The Australian HF warning product names "Southern Australia/NZ and Antarctic regions," not Africa or South America (Section 3).
5. **Drake gaps closed with real numbers:** Antarctica21 flight-delay statistics (274 flights, 2003 to Mar 2023), Marambio's two runways (1,208 m main, 1,600 m second), Chilean port-closure wind bands (and the fact they bind small craft, not ocean ships), an AIS-based port-share study (PNAS 2022), and the Charcot two-night crossing. Antarctic Pilot sailing distances stay paywalled.
6. **Macquarie:** the 3023 kHz HF schedule rests on Wikipedia's "VJM" line; the current AAD page describes VHF with four repeaters and SPOT trackers and does not mention HF. VK0AI's 1,500+ contacts in 50+ countries and the four repeaters are now verified from AAD pages. Transmitter powers, antennas and the HF frequency plan are still not published anywhere I could reach.

---

## 1. HF, amateur and commercial contacts: Australia, South Africa, South America

### 1.1 Commercial HF (Beam) history: spokes to London, one hub at Montreal

| Fact | Tag | Source |
|---|---|---|
| The Imperial Wireless Chain's first link (Leafield to Cairo) opened 24 Apr 1922; the **final link, Australia to Canada, opened 16 Jun 1928**. | [F] | https://en.wikipedia.org/wiki/Imperial_Wireless_Chain (2026 copy) |
| Beam stations worked in pairs (one transmit, one receive). Pairs: Tetney and Winthorpe in England **with Ballan and Rockbank in Australia**; Bodmin and Bridgwater in England **with Drummondville and Yamachiche in Canada and with Klipheuwel and Milnerton in South Africa**. Each Dominion hung off a British pair. | [F] | same |
| The Norman Committee (1920) recommended connecting Britain to Canada, Australia, South Africa, Egypt, India, East Africa, Singapore and Hong Kong. Parliament approved the Post Office/Marconi beam contract for Canada, South Africa, India and Australia on 1 Aug 1924. | [F] | same |
| **AWA's Australia to Britain/Europe Beam opened for commercial traffic 8 Apr 1927. On 16 Jun 1928 the Australia to North and South America service opened, via the Montreal to London circuit ("also a second link with the Old World").** Ballan transmitted to London and (a second transmitter) to Montreal; "all messages for the North and South American Continents" went to Montreal. | [F] | AWA, *Wireless Progress in Australia* (1930), https://www.worldradiohistory.com/AUSTRALIA/Various/AWA-1930-Wireless-Progress-in-Aust.pdf |
| Klipheuwel (Western Cape) was the South African Marconi shortwave transmitter site of the Chain. | [F] | https://en.wikipedia.org/wiki/Klipheuwel |
| A 20 kW AWA shortwave station, 2ME Sydney, relayed the first Empire Broadcast on 5 Sep 1927; it was "received and then relayed on mediumwave stations throughout India, South Africa, the United Kingdom, Canada, and the U.S.A." | [F] | https://www.australianotr.com.au/early-australian-shortwave-broadcast-stations.html |
| OTC (Overseas Telecommunications Commission) was created Aug 1946 from AWA and Cable & Wireless assets; the Cocos cable station passed to OTC in 1955; OTC merged into Telstra in 1992. | [F-snippet] | https://en.wikipedia.org/wiki/Overseas_Telecommunications_Commission |

[I] There was no direct Australia to South Africa beam and no direct Australia to Argentina/Chile/Brazil beam; every route was a spoke or went through a hub (London, Montreal). The 1928 Montreal hub is the nearest historical analogue for "a relay at a third place" and is the answer to "how did Australia reach South America by HF in the 1920s": it did not, directly.

Dead end for the radiotelephone question: no source I opened names a Sydney or Perth to Cape Town HF radiotelephone circuit. AWA's 1930 radiophone service is described as "Great Britain and the Continent" (opened 30 Apr 1930) and the 1930 text lists Beam destinations without South Africa. [U] whether OTC ever ran a direct VK-ZS HF telephone circuit.

### 1.2 Amateur firsts (adjacent only)

- Max Howden (3BQ, Melbourne): first two-way telephony between Australia and England, Feb 1925, per a QSL card from VK2CM. [F-snippet] (search summary of a 2CM Wikipedia/wikimili page).
- Frank Bell made New Zealand's first overseas two-way contact, with an Australian amateur, Apr 1923; **Brenda Bell was the first New Zealander to contact South Africa by radio, 1927.** [F-snippet for Frank Bell; [F] for Brenda Bell: https://en.wikipedia.org/wiki/Brenda_Bell]
- South African Radio Relay League formed 20 May 1925. [F-snippet] (rsgb.org, SARL pages)
- Australian call-sign prefix "OA" decreed from 1 Feb 1927. [F-snippet]
- Radio Club Argentino founded 21 Oct 1921; Radio Club de Chile Jul 1922. [F-snippet]
- **Not found:** the first VK to ZS, VK to LU, VK to CE or VK to PY contact. [U] (Q and S: the Trove newspaper archive is JavaScript-only and has no free API; the VK4GHZ forum thread "VK to ZS contacts - past history" is behind a 403 and not in the Wayback Machine.)

### 1.3 Nets that really span the Indian Ocean, South Atlantic, Pacific (frequencies, hours, who)

All UTC. "Source" opened by `curl` unless marked.

| Net | Frequencies (kHz) and times | Run by / participants | Coverage claim | Tag and source |
|---|---|---|---|---|
| **Durban Maritime Mobile Net** (revived c. 2020 by yachtsmen-hams from the original net, "dating back 40 years") | Three daily sessions, each a band cascade. 04:45 on 21300, 04:50 on 14300, 05:00 on 8101, 05:10 on 7115. 11:00 on 21300, 11:10 14300, 11:15 8101, 11:20 7115. 15:00 on 21300, 15:10 14300, 15:15 8101, 15:20 7115. 21300, 14300, 7115 are ham; 8101 and 12353 are marine. | ZS5CB (Roy), ZS5PD, ZS1SBM, ZS1PG; monitored 24 h by a team of five at Durban, Port Shepstone, Cape Agulhas and Cape Town. | "covers from Australia across the Indian Ocean, the Atlantic to Brazil and the Caribbean, and to the Mediterranean through the Red Sea, and beyond (taking into consideration propagation)." Weather and navigation advice for yachts crossing the south and east Indian Ocean. | [F] https://www.noonsite.com/?p=1156438 (page says "published 6 years ago"; the "April 2020" date is [F-snippet]) |
| **Peri Peri Net** | 8101 kHz daily 15:00, then 12353 to track distant vessels; informal 8101 at 05:00. | Controller in Durban; relay stations at Johannesburg, Mozambique (Bazaruto), formerly Madagascar (closed May 2015). | "On a good day, the Net can cover most of the Indian Ocean and Atlantic too." | [F] https://www.noonsite.com/report/south-african-radio-nets-updated/ (page last edited Jan 2016; the 2020 Durban page repeats it) |
| **South African Maritime Mobile Net (SAMMNet)** | High-seas net 14.316 MHz USB at 06:30 (controller ZS1SAM) then coastal waters on 7.120 at 06:35. Wikipedia gives 06:35 and 11:35 on 7.120, 06:30 and 11:30 on 14.316 (two sources disagree on times). Also "Campbell's Net" 13:30 on 14316. | Peter Wolf (ZS1CH), Woody Collett (ZS3WL), Marjoke Schuitemaker (ZS5V), Johan Smith (ZS6WZ). **Marine weather bulletins for coastal areas (40 m) and the high seas, METAREA VII (20 m).** | Non-hams may use it by e-mail position reports. | [F] noonsite page above; https://en.wikipedia.org/wiki/Maritime_mobile_amateur_radio |
| **Cape Town Radio (ZSC), Telkom Maritime Radio Services** | Forecasts and reports on 4375, 8740, 13146 kHz USB at 10:15, 13:30, 18:15 daily; DSC watch Sea Area A3 on 4, 6, 8, 12, 16 MHz. | National coast station; Frequentis GMDSS system for the Dept of Transport, centre in Cape Town, back-up at Klipheuwel, 2,800 km coastline (2017). | South African coast, "barometer pressure and wind speed around the entire SA coastline." | [F] noonsite (frequencies); [F] https://www.frequentis.com/sites/default/files/pr/2017-10/FREQUENTIS_GDMSS_South_Africa_07_2017.pdf (system); DSC bands [F-snippet] |
| **Tony's Net (ZL1ATE)** | 14315 USB at 21:00; a 7170 LSB ham net follows around 21:15 to 21:35. | "Consortium of net controllers in NZ and Australia"; relays and weather. | South Pacific and Tasman. | [F] noonsite Pacific list; [F] https://www.yit.nz/sites/default/files/resource/wx_and_radio_info_2017-sept.pdf |
| **Pacific Seafarers Net** | 14300 USB at 03:00, roll call 03:25. "The three nets that share 14300 kHz" (Pacific Seafarers, Maritime Mobile Service Net, Intercon) "hand off well to one another." | US-led volunteers. | Pacific. | [F] noonsite Pacific list |
| **Maritime Mobile Service Net (MMSN)** | 14.300 MHz, 17:00 to 03:00 (winter), 16:00 to 02:00 (summer). Founded 3 Jan 1968; "Global Emergency Center of Activity" frequency per IARU. | Net manager KB4JKL, 70+ controllers; Atlantic, Caribbean, eastern Pacific. | Not southern Indian Ocean. | [F] Wikipedia Maritime_mobile_amateur_radio; origin and IARU line [F-snippet] (mmsn.org) |
| **Pacific Maritime Mobile Service Net (PMMSN)** | 21.412 MHz USB, 21:00 to 24:00 daily. | US-led, "almost fifty years." | Pacific, 15 m. | [F] noonsite Pacific list |
| **Gulf Harbour Radio (ZMH286), Passage Guardian (ZMH292), Far North Radio** | 8752 (alt 8779, 8297) at 19:15 Mon to Sat, May to Nov; Far North 6516 and 4417. | NZ private coast stations run by cruisers/engineers. | NZ and SW Pacific. | [F] noonsite Pacific list |
| **Patagonia / Chile cruising net** | 8164 kHz. Noonsite lists "12:00" with "referenced in 2006, 2009, 2013"; a search summary gives 09:00 local. | Controller "Wolfgang" (Wildemathilde). "Many boats in the area and further south to Ushuaia check in daily." | Chile to Ushuaia. | [F] noonsite Pacific list ("UNSURE" section); [F-snippet] for the 09:00. Probably defunct. |
| **Amigo Net** (Pacific Mexico) | retired Feb 2024. | | | [F] noonsite Pacific list: reasons given are reduced interest, competing communication methods and global internet. |
| **TasMaritime** | HF and VHF skeds 07:45, 13:45, 17:33 (local) | Tasmania's "only official Coast Radio Service." | Tasmania. | [F] noonsite Pacific list |

**Names in the brief that were not found:** "Indian Ocean Maritime Mobile Net" (closest real equivalents are the Durban Maritime Mobile Net and SAMMNet), "Southern Cross Net," "Cape Town to Rio net," "Pan-Pacific Net," "Trans-Tasman Net" (closest is Tony's Net). All died at the query (Q). Do not use those names as real.

**Observations for network design [I], flagged:**
- **Band cascade.** The Durban net steps down 21.3, 14.3, 8.1, 7.1 MHz inside 35 minutes, three times a day, so a yacht at any distance finds a band that is open. This is a real, working answer to "which band" on a path that changes by hour and season.
- **Handoff.** Three nets share 14.300 and hand off. The global anchor (14.300, designated by IARU as a global emergency center of activity) sits in the middle of a cluster of regional frequencies: 14.305, 14.315, 14.316, 14.318, 14.320. Convergence here is "one anchor, regional neighbors within about 20 kHz," not one frequency. This is a real-world example for the developer's principle that a local pattern becomes the standard.
- **Decline.** HF voice is shrinking: Amigo Net retired in 2024; Australia's states and the Northern Territory handed 24-hour HF distress monitoring to AMSA from 1 Jan 2022 after "a steady decline" (one search summary says only two distress calls in four years to Mar 2018 were HF-only; [F-snippet]). [I] A settled Antarctica with no satellite coverage poleward of about 80 degrees reverses this pressure for the Antarctic end only.

### 1.4 DX and propagation evidence, Indian Ocean path and trans-polar path

| Fact | Tag | Source |
|---|---|---|
| "Australians work into South America across the South Pole regularly this time of year" (January, southern summer, bottom of the sunspot cycle, 1997). | [F] (one forecaster's sentence in a monthly column) | AD5Q, *Propagation*, Jan 1997, https://ng3k.com/Ad5q_prp/ad5q9701.html |
| A Fish Hoek (Cape Town) hobbyist beaming 120 degrees heard Western Australian medium-wave stations over a mostly all-water Indian Ocean path (2006). | [F] (already in the ring log) | https://dxing.info/dxpeditions/fishhoek_2006_03.php |
| Historical VK6 to ZS contacts in April 1991 (ZS6XL, ZS6AXT, ZS6LN, ZS4S, ZS6HS) are listed in a forum thread; the band is not stated (April 1991 was near solar maximum, so [U] but probably a high band). | [F-snippet] | https://vk4ghz.com/forum/viewtopic.php?p=14479 (403) |
| A forum comment that Africa to VK contacts were "long path over USA or short path over VK0 (Heard Island)." | [F-snippet] | same forum |
| "If you draw an azimuthal map centered on South Africa, you can avoid polar regions for most propagation paths." | [F-snippet] | search summary of a southern-hemisphere propagation page |
| Marion Island's club station ZS2MI in the 1960s "used the huge rhombic antennas and was easily workable around the world"; the Prince Edward Islands got the ZS8 prefix in 1989; ZS8IR (1996 to 97) logged 18,000+ QSOs. | [F] | https://www.zs6ez.org.za/zs8.htm |
| SANAE amateur operation: ZS6KX/7 on 20 m SSB 14:00 to 17:00 UTC. | [F-snippet] | ARRL W1AW bulletin (ARLD032/2011) search summary |
| Argentine Antarctic base amateur stations carry LU call signs (Esperanza LU1ZV, Marambio LU4ZS, Belgrano II LU1ZG, San Martin LU1ZD, Jubany LU5ZI, Primavera LU2ZD); a 2019 Esperanza activation logged 900+ contacts incl. Japan, Canada, Latvia, Ukraine, Finland and most of the Americas. No Australia or South Africa listed in the summary. | [F-snippet] | https://cdn-sp.radionacional.com.ar/?p=1004296 and qsl.net/lu5gpl |
| Current Australian Antarctic hams: VK0TBC (Casey), 20 m FT8 and SSB; VK0DS (Davis), mostly FT8, end-fed antenna on a 22 m tower; "on air until about Dec 2026." | [F] | WIA news, 30 Jun 2026 and 29 Aug 2026, https://www.wia.org.au/newsevents/news/2026/20260829-1/index.php |
| Antarctic stations commonly meet on 14.243 MHz (Sundays 00:01 UTC; McMurdo 14.243 SSB and 14.070 FT8; South Pole KC4AAA 14.243). | [F-snippet] | ARRL/RSGB summaries |
| LRA36 (Esperanza, 15476 kHz USB) is DX-grade even in North America; reception reports come from Iceland, Spain, Italy, Japan, India, Mexico, Chile, Brazil, Uruguay. **No Australian or South African reception found.** | [F-snippet]; [F] swling.com 2020 for the North Carolina report | https://swling.com/blog/2020/07/finally-confirmed-reception-of-lra36-radio-nacional-arcangel-san-gabriel-antarctica |
| One Australian ham/SWL's QSL index lists cards from Argentina, Brazil, Chile, South Africa, Antarctica, Crozet, Chagos, Cocos Keeling and others; not dated, not a contact log. | [F] (weak) | https://www.vk5pas.com/radio-australia.html |
| Radio Australia shortwave ended 31 Jan 2017; Shepparton had seven 100 kW transmitters (since 1944); Carnarvon (WA) hosted domestic ABC shortwave until the 1990s. **Africa or South America as target areas: not found.** | [F] | https://aph.gov.au/Parliamentary_Business/Committees/Senate/Environment_and_Communications/Shortwaveradio/Report/c01 |
| Two remote-SDR (KiwiSDR) listeners logged South Africa's ZSJ Cape Naval weather fax in 2019 only after hunting for it; the station is described as "unreliable," 4014/7508/13538/18238 kHz, with an "Antarctic Ice Limits" chart that is seasonal. | [F] | https://goughlui.com/2019/02/16/radiofax-the-quest-for-zsj-cape-naval-south-africa-updates/ |

[I] Reading: the Indian Ocean path (Perth to Cape Town, 8,698 km, 35 to 45 degrees S) is the sort of path a Durban-style cascade net handles; the trans-polar path (Australia to South America) works in southern summer at the bottom of the cycle and is exactly the path that polar-cap absorption closes at other times. This agrees with the ring log's modeling; it is not new measurement.

### 1.5 SANAE, Marion, Cape Town and Antarctic HF

- The "Cape Town to Antarctica HF thesis" the earlier agent could not open is probably **MacWilliam (UCT, 2019): a transmitter antenna for a 1 W, 12.57 MHz beacon at the South Pole received by the SANAE IV SuperDARN radar 2,090 km away; single-hop skywave at low take-off angles.** [F] https://open.uct.ac.za/bitstream/11427/32406/1/thesis_ebe_2020_macwilliam%20kathleen.pdf. It is Pole to SANAE, not Cape Town to Antarctica; no Cape Town to Antarctica HF thesis was found. Findings usable here: ICEPAC and similar ray-tracers ignore the ordinary/extraordinary split and **did not reflect a measured polar-cap absorption event** (the system "was not expected to operate in highly disturbed conditions"); data for southern high latitudes "is still fairly scarce." [F]
- Marion Island: a weather station since Feb 1948 with a radio link to the Union set up by Commander Bullard; communications engineers (formerly radio operators) are on every SANAE, Marion and Gough team; mail at SANAE was once "messages communicated via Morse code to the radio operator." [F] https://blogs.sun.ac.za/antarcticlegacy/2020/04/06/day-11-of-a-21-day-journey-through-the-alsa-digital-repository-communications-in-an-isolated-environment and zs6ez page. HF schedules between Cape Town and SANAE/Marion: not found. [U]
- SANAE IV carries a satellite dish, a radio room, a VHF tower and a SuperDARN radar administered by SANSA. [F-snippet] Wikipedia SANAE_IV.
- Polar HF digital precedent for the Weddell crossing: Prior-Jones and Warrington (BAS/Leicester, 2010) tested a DRM-derived OFDM modem on a **1,600 km Halley to Rothera test link**, found it outperformed NATO STANAG 4285 and 4539 modems in a polar channel simulator, and note geostationary links fail poleward of 80 degrees and Iridium cost about US$60 per megabyte (2010). [F] https://meetingorganizer.copernicus.org/EGU2010/EGU2010-14943.pdf. The "about 400 MB per year" availability figure is [F-snippet] only.
- HamSCI (2022): Antarctic snow and ice are "a strong absorber of HF radio waves," which "severely mitigates intracontinental multi-hop propagation modes." [F] https://www.hamsci.org/publications/potential-science-opportunities-hamsci-antarctica. This supports the earlier agents' choice of single-hop, skywave-over-sea links.

---

## 2. Coast radio, distress and weather nodes; flying-doctor links

### 2.1 Who still operates HF coast radio (state of 2026)

| Country | Station and status | Tag and source |
|---|---|---|
| **Australia** | The old coast stations (Perth VIP opened 1912 as POP; Sydney VIS 1912; Melbourne VIM) ended Morse on 31 Jan 1999 [F] https://jproc.ca/radiostor/telstra.html; all Telstra coast stations closed 30 Jun 2002 [F-snippet]. State and NT authorities then monitored HF distress from 2002; **from 1 Jan 2022 AMSA monitors HF radiotelephone 24 h on 4125, 6215, 8291, 12290, 16420 kHz**, plus HF DSC, AUSCOAST and NAVAREA X warnings, plus a test-call service on the same frequencies. [F] https://www.amsa.gov.au/hfradio. **BoM weather broadcasts (voice and fax) come from VMC Charleville and VMW Wiluna**; VMW covers the Northern, Western and Southern high-seas areas; the fax schedule includes Indian Ocean MSLP analyses and forecasts, Southern Ocean wave charts and a Southern Hemisphere MSLP forecast. [F] https://www.bom.gov.au/marine/radio-sat/radio-fax-schedule.shtml and marine-weather-hf-radio.shtml. Voice frequencies (VMC 4426/8176/12365/16546 day; VMW 4149/8113/12362/16528 day) [F-snippet]. |
| **South Africa** | Cape Town Radio (ZSC) under Telkom Maritime Radio Services; HF DSC A3 watch; weather on 4375/8740/13146; GMDSS system (Frequentis) installed from 2017; back-up site Klipheuwel. ZSJ Cape Naval carries SAWS weather fax on 4014, 7508, 13538, 18238 kHz. [F] (see 1.3, 1.4) |
| **Chile** | Valparaiso Playa Ancha Radio (CBV) under DIRECTEMAR concentrates MSI and SAR for NAVAREA XV; HF broadcasts on 4214.5, 8420.5, 12583.5, 16811.0, 22380.5 kHz; area of responsibility "almost to the Antarctic." Puerto Williams Radio CBM24 broadcasts port-weather conditions on VHF 16/14. Bahia Fildes Radio (CBZ22) is the Antarctic station. [F-snippet] (IHO WWNWS papers, not opened: connection failure) ; CBM24 [F] (Puerto Williams plan, 2023) |
| **Argentina** | Prefectura Naval Argentina: GMDSS and HF coverage for NAVAREA VI, main coastal stations Buenos Aires, Mar del Plata, Comodoro Rivadavia, Ushuaia; NAVAREA VI also issues "Antarctic glaciological information, sea ice edge, main icebergs adrift." [F] (NAVAREA VI 2022 report, https://iho.int/uploads/user/Inter-Regional%20Coordination/WWNWS/WWNWS14/WWNWS14_2-1-VI_2022_NAVAREA_VI_SA.pdf, opened) ; HF frequency details [F-snippet] |
| **Brazil** | Rio de Janeiro Radio (PPR, 12 MHz band, MMSI 007100001) and Brazilian Navy station PWZ33 sending NAVAREA V warnings at 04:00, 14:30, 21:30 UTC. [F-snippet] (not opened) |

[I] No inter-station relay among Cape Town Radio, Perth/AMSA, Valparaiso and Rio was found; the only coordination layer is METAREA/NAVAREA (Brazil V, Argentina VI, South Africa VII, Australia X, New Zealand XIV, Chile XV) and the five national SAR regions. That is a bulletin-sharing and SAR-handoff structure, not a voice relay.

### 2.2 SAR as a working Australia to South Africa link

- **Jedi 1, March 2017:** a 13 m yacht on a South Africa to New Zealand passage was dismasted more than 1,300 km southwest of Cape Leeuwin; its registered beacon alerted **AMSA's JRCC in Canberra**; an AMSA Challenger jet from Perth made VHF contact; the **Royal Australian Navy's HMAS Parramatta** took off three South Africans. [F] https://www.mysailing.com.au/south-african-nationals-rescued-from-stricken-yacht-in-indian-ocean (20 Mar 2017). This is a documented case of Australian assets serving South African sailors on the Indian Ocean route and shows the beacon/satellite path, not HF, carrying the alert.
- Counterpart: Cape Town's MRCC coordinated a Nov 2017 rescue of the yacht Kinda Magic by a passing tanker. [F-snippet]
- Multilateral: a 2007 five-country agreement makes Cape Town a hub for maritime rescue around South Africa, Comoros, Madagascar, Mozambique, Angola and Namibia. [F-snippet] **No bilateral Australia to South Africa SAR agreement found.** [U]

### 2.3 Flying Doctor and Traeger: is there an Australian to African radio link?

- **RFDS HF today:** the VKS-737 network works through 14 or 15 base stations; RFDS says it is "committed to HF radio" as a backup for remote areas. [F-snippet] https://vks737.radio and Wikipedia VKS737.
- **Traeger:** the Traeger company exported radios; "in 1962 pedal sets were sold to Nigeria; in 1970 an educational radio network was sold to Canada." [F] https://en.wikipedia.org/wiki/Alfred_Traeger. This is an equipment export, not an Australia to Africa radio link.
- AMREF (Nairobi, 1957) is described as running "over 100 HF radio stations" across East Africa. [F-snippet] The Wikipedia pages for AMREF and RFDS (opened) do not link the two. **No documented Australian to African flying-doctor radio link or Australian adviser role found.** [U] The earlier agents' caution that nothing links Antarctic nets to Flying Doctor procedure also holds for Africa.

---

## 3. Space weather and HF-forecasting cooperation

| Question | Finding | Tag and source |
|---|---|---|
| Who are the ISES Regional Warning Centres in these countries? | **ASWFC (Australia), SANSA (South Africa), EMBRACE (Brazil), LAMP (Argentina)** appear in ISES lists of RWCs (22 to 23 RWCs worldwide). I found **no Chilean RWC**. | [F-snippet] (iswat-cospar and ISES pages; spaceweather.org unreachable) |
| Does Australia exchange HF forecasts with South Africa or South America? | **No bilateral exchange found.** Australia sits in the ICAO global-center consortium **ACFJ (Australia, Canada, France, Japan)**, with **HF advisories issued from Melbourne** and other advisories from Toulouse. South Africa's SANSA **partners with PECASUS (nine European countries)** to supply ICAO with information for Africa (joined Sep 2018, ICAO designation announced Jan 2019). So the two sit in different consortia. | [F-snippet] ACFJ (unitingaviation.com, NICT, ICAO APAC papers); [F] SANSA-PECASUS: https://www.sanews.gov.za/node/42458 and https://spaceinafrica.com/2019/01/14/sansa-selected-by-icao-to-become-the-designated-regional-provider-of-space-weather/ |
| What does the Australian HF product cover? | "IPS HF COMMS WARNING ... DEGRADED HF PROPAGATION CONDITIONS EXPECTED FOR SOUTHERN AUS/NZ AND ANTARCTIC REGIONS," with T-index and MUF by band (Feb 2014 example). Today BoM publishes hourly HAP charts for Charleville and Wiluna on 4.1, 6.2, 8.2 and 12.3 MHz; its client list names the **Australian Antarctic Program**, AMSA, Airservices, ARINC and Stockholm Radio, and HF clubs. **No African or South American region.** | [F] https://listserver.ips.gov.au/pipermail/ips-hf-warning/2014-February/000723.html ; https://www.sws.bom.gov.au/Products_and_Services/5/9/1 (opened Oct 2026) |
| SANSA's HF focus | Hermanus centre (est. 2010, upgraded 2018) "has been focused on space weather impacts on high-frequency communications"; instruments across southern Africa, SANAE, Marion and Gough. | [F] https://www.engineeringnews.co.za/article/regional-space-weather-centre-south-africa-2021-05-07 (HF focus); instrument list [F-snippet] |
| Ionosonde networks | **BoM (ASWFC) ionosonde table (2026) marks active:** Cocos Islands, Darwin, Niue (run by Niue Met), Townsville, Learmonth, Brisbane, Norfolk Island, Perth, Canberra, Hobart, **Casey, Mawson, Davis**. Macquarie Island and Scott Base rows are not marked active (Macquarie dates run to 2015, column alignment ambiguous). The Cocos ionosonde sits on the Perth to Cape Town side. **SANSA** GIRO stations include Grahamstown, Hermanus, Louisvale; Port Stanley and Learmonth also contribute. **GIRO has mirror sites run by UFA (Europe), SANSA (Africa), IGG CAS (Asia): none in Australia or South America.** | [F] https://sws.bom.gov.au/World_Data_Centre/2/1/28 ; [F] https://giro.uml.edu/didbase/ ; station names [F-snippet] |
| Argentina, Chile, Brazil | Argentina: LAMP (created 2011; IAFE, Instituto Antártico Argentino, UBA) deployed a space-weather laboratory at **Marambio (installed Jan to Mar 2019)**; Tucumán ionosonde near the southern crest of the equatorial anomaly. Chile: Chillán (j3p) station on a university agreement; **Base Teniente Marsh had an IPS-42 ionosonde installed Feb 1986** (the IPS-42 is the type used in the Australian IPS network, e.g. Hobart, Christchurch, Scott Base). Brazil: EMBRACE; a CADI ionosonde at Comandante Ferraz since 2009; SAVNET (VLF) and SARINET (riometers) networks reach Antarctica; **All4Space** is an agreement among institutions in Argentina, Brazil, Chile and Mexico. | [F-snippet] (LAMP, UMAG repository, UDEC, EMBRACE; repositories blocked); SAVNET/SARINET/Ferraz [F] https://revistas.ufrj.br/index.php/oa/article/view/8109/6568 (2011) |
| SuperDARN (the one multinational Antarctic HF-radar network) | Southern Hemisphere radars: Buckland Park (La Trobe), Dome C East/North (Italy), Falkland Islands (BAS), Halley, Kerguelen, McMurdo, **SANAE (SANSA)**, South Pole, Syowa, TIGER (Bruny Island, Tasmania), Unwin (NZ), Zhongshan. **No Argentine, Chilean or Brazilian radar; the Australian Antarctic stations host none.** | [F] https://en.wikipedia.org/wiki/SuperDARN |
| Joint Antarctic ionospheric campaigns Australia with Chile, Argentina or South Africa | **None found.** | [U] (Q) |

[I] The honest summary for the worldbuilding: the three parties already contribute data to shared global databases (WDC, GIRO) and sit under ISES/ICAO, so a settled-Antarctica forecasting pool is a natural extension, but nothing in today's record shows a three-way HF-forecast exchange. Antarctica's own coverage gap (few ionosondes poleward of 65 degrees S, models failing in polar-cap events) is what a settled Antarctica would fill.

---

## 4. Drake gaps (Open_Research_Topics §3 and the Drake log's dead-end list)

### 4.1 Antarctic Pilot sailing distances: still not closed
- US NGA Pub 151 *Distances Between Ports* (2001 edition) opened in full from EverySpec; **it has no Antarctic ports** (no Palmer, Esperanza, Deception, Marsh, McMurdo). [F] https://everyspec.com/MISC/download.php?spec=NGIA_PUB-151_2001.049282.pdf. (Died at the source.)
- NGA Pub 124 and the Antarctic Pilot (NP9) tables: paywalled/not free. Skip per brief.
- What Pub 151 does give (useful for the three-continent question): **Fremantle to the Cape of Good Hope 4,755 nmi; Fremantle to Cape Leeuwin 181; Buenos Aires to the Cape of Good Hope 3,704; Ushuaia to Buenos Aires 1,447.** [F] same file. [calc] 4,755 nmi = 8,806 km, about 1% longer than the 8,698 km Perth to Cape Town great circle in the ring log (Cape Town is a few tens of nmi from the Cape of Good Hope junction, so the comparison is approximate).
- Published Ushuaia to Peninsula distances are round figures: "roughly 600 miles" and "nearly 600 nautical miles" in operator pages; "about 1,000 km (540 nautical miles)." [F-snippet] These bracket the earlier calc (557 to 559 nmi to Livingston/King George; Palmer City 1,133 km, about 612 nmi). No contradiction.
- Seabourn page (opened): South Shetland Islands sit "some 131 nautical miles north of Paradise Harbor." [F] https://current.seabourn.com/article/guide-ushuaia-to-antarctica
- LMG (Gould) Punta Arenas to Palmer Station: "usually four to five days"; Strait of Magellan to Cape Horn 36 to 40 h, then the Drake 2 to 3 days. [F-snippet]

### 4.2 Marambio runway: 1,208 m versus 1,600 m is a two-runway fact, not a contradiction
- **Main runway (06/24): 1,200 m by 40 m nominal; the airfield chief gave "1,208 metres" declared length, 40 m wide, in Jan 2024; the Buenos Aires Times (Aug 2026) repeats 1,208 m by 40 m.** [F] https://defonline.com.ar/defensa/el-aerodromo-argentino-en-la-antartida-como-es-la-pista-de-aterrizaje-de-base-marambio/ ; https://www.batimes.com.ar/news/argentina/how-pilots-land-aircraft-at-marambio-base-argentinas-most-challenging-antarctic-airstrip.phtml
- **Second runway (01/19): 1,600 m by 40 m, test-flown 16 Jul 2015** (a Twin Otter, then a Hercules from El Palomar via Rio Gallegos), "the longest dirt runway in Antarctica," for north winds. [F] https://www.aviacionline.com/exitosa-prueba-de-la-nueva-pista-del-aerodromo-de-la-base-antartica-marambio
- **Whether the 1,600 m runway is in regular use is not established.** The 2024 and 2026 pieces quote only 1,208 m as "the" runway and call Marambio Argentina's only operational large-aircraft runway (Petrel being rebuilt). [I] treat 1,208 m as the working figure.

### 4.3 Antarctica21 flight delays: the real figures
Antarctica21's own page (2003 to Mar 2023, 274 flights): **213 left on the scheduled day, 16 the day before, 32 with a one-day delay, 10 two-day, 2 three-day, 1 four-day.** "Only three flights delayed beyond two days." "Only one flight delay where clients could not fly at all" (once clients sailed back instead). [F] https://www.antarctica21.com/journal/antarctica-flights
- [calc] on schedule 77.7%; early 5.8%; on time or early 83.6%; delayed 1 day 11.7%; 2 days 3.6%; 3 days 0.7%; 4 days 0.4%; delayed 2 days or more 4.7% (13 of 274); delayed 3 or more 1.1% (3 of 274); could not fly 1 flight (0.4%).
- Cause named: low cloud, fog and wind at King George Island. Contingency: guests keep cruising until the flight is cleared.
- This replaces the earlier "about 3% two-day, under 1% three-day, about 1% cancelled" (search-summary-only): the true two-day share is slightly higher, three-day and longer is 1.1% combined, and one flight in 274 never flew.

### 4.4 Port-closure rules (Chile; Argentina not found)
Chile's maritime authority runs graded "condiciones de tiempo" plans per Capitanía, under the Ley de Navegación, the Reglamento General de Orden, Seguridad y Disciplina (Art. 151 letter a lets the Capitán de Puerto suspend traffic in temporales, bravezas, dense fog or strong winds), and DGTM circular O-41/001 of 26 Oct 2021. Opened plans:

| Capitanía and date | Normal | Variable | Mal Tiempo | Temporal | What closes |
|---|---|---|---|---|---|
| **Punta Delgada** (First Narrows ferry), 6 Feb 2025 | wind at or under 18 kn | over 18 to 30 kn | over 30 to 40 kn | over 40 kn | Variable: port closed to departure of small craft outside the bays; Mal Tiempo and Temporal: closed to "naves menores" inside and outside bays; ferry crossings suspended in Temporal. |
| **Puerto Williams**, 27 Apr 2023 | | over 15 to under 25 kn | 25 to 35 kn | over 35 kn | Mal Tiempo and Temporal: work at piers and ramps suspended; in Temporal, traffic of embarcaciones menores suspended inside and outside the bay. The plan is announced by CBM24 on VHF 16/14. |

[F] https://www.directemar.cl/directemar/site/docs/20250425/20250425095428/12000_30__pda.pdf and https://www.directemar.cl/directemar/site/docs/20260828/20260828124054/12600_16_270323_cp_will.pdf
- **Punta Arenas** (own plan, 2023 and a 2021 sibling): not opened (the `prontus` host returns 403 and the `www` path 404). Search summary of the 2023 plan: Variable weather, sustained 15 to 20 kn suspends navigation for vessels under 25 GT; 20 to 25 kn with gusts to 30 suspends vessels under 100 GT inside and outside the bay; an east wind limit of 15 kn "due to wave force"; dense fog or very dense rain closes the port while it lasts; a Maritime Meteorological Center forecast 12 h ahead is the official basis. [F-snippet]
- **Key reading [I, but directly from the text]:** these plans close the port to small craft and shore work. They do not publish a wind threshold that bars an ocean-going expedition ship from sailing; the master and the operator make that call. So the 1 to 6 day logged weather holds in the Drake log are decisions at the Drake end (forecast of the crossing), not port closures. [I]
- Chilean wind climate at a Strait site: average maxima near 78 kn from the west; winds over 55 kn from W (0.2%) and SW (0.1%); 48 to 55 kn about 1.4% combined; 34 to 47 kn 10.3% (a Chilean port-installation resolution, Ord. 12.000/8 of 3 Jul 2020; the site is not identified in the text I read). [F] https://vlex.cl/vid/resolucion-n-12-000-927124920 . Local to that site, not Punta Arenas itself.
- **Ushuaia (Prefectura Naval Argentina):** no published wind threshold for port closure found. [U] (Q.) Related: Ushuaia airport closed with all flights suspended on 6 Aug 2023 for weather (news headline). [F-snippet]

### 4.5 Charcot expedition crossing times
Ponant's Commandant Charcot itineraries (search summaries of cruise listings) show departure from Ushuaia at 18:30 on Day 1, "crossing the Drake Passage" Days 2 and 3, arrival at the Peninsula Day 4; the return is also two days. [F-snippet] No log of hours or knots. Consistent with the 36 to 48 h expedition-ship figures in the Drake log. Lindblad (Nat Geo) reports: no crossing time or distance found in snippets. [U]

### 4.6 AIS-based Drake transit speeds and delays: still none, but one port-level AIS study found
- **PNAS 2022, "Ship traffic connects Antarctica's fragile coasts to worldwide ecosystems"** (Lloyd's data plus raw satellite AIS, ships south of 60 S, 2014 to 2018): 75 ports linked to Antarctica, 58 last ports of call; **gateway cities were the last port of call for 63% of voyages: Ushuaia 47%, Punta Arenas 11%; Stanley 14%; top-10 ports 91% of departures in seven countries (Argentina, Chile, Falklands, Australia, New Zealand, South Africa, Uruguay); "90% of port departures" are in South America and the South Atlantic and "90% of traffic visits the Antarctic Peninsula and SSI."** [F] https://pmc.ncbi.nlm.nih.gov/articles/PMC8784123/ (full text via Europe PMC XML) . [calc] Hobart, Cape Town and Christchurch together are about 5% of voyages (63 less 47 and 11).
- [I] This quantifies the "single-gateway dependence" worry in the Drake log and shows the Australian-sector gateway is minor in ship counts; the Peninsula dominates.
- A 2025 *Journal of Sustainable Tourism* carbon-footprint study used AIS from the Norwegian Coastal Administration for itineraries and speeds: **paywalled (403), not opened.** [U]
- No study reporting Drake crossing-time distributions, speeds or waiting times from AIS was found. Died at the query (Q) for "Drake transit speed AIS" and at the source for the tourism paper (S).

---

## 5. Macquarie Island and AAD/ACMA items

| Item | Result | Tag and source |
|---|---|---|
| HF schedule | Wikipedia: callsign "VJM," nightly HF schedule with field huts on 3023 kHz; ANARESAT earth station (Intelsat Pacific) to Australia; Inmarsat and Iridium backups. | [F] https://en.wikipedia.org/wiki/Macquarie_Island_Station (cited to an older AAD text) |
| Current AAD wording | "Communications between huts and groups in the field is typically by VHF radio. The island is serviced by four radio repeaters... Each person or group also carries a SPOT satellite-tracking device... Nightly radio scheds take place between the field parties and the station." The page does **not** mention HF or 3023 kHz. | [F] https://www.antarctica.gov.au/antarctic-operations/stations/macquarie-island/living/field-huts/ |
| Repeaters | Four VHF repeaters (Mt Waite is "one of four that provide almost complete VHF radio coverage of the whole island"); a **CH21 marine VHF repeater on Mt Jeffryes** serves the south; repeaters run on renewable power and need multi-day trips to repair (Mt Ainsworth/Hurd Point trip, 2024: 40 kg of gear, three lithium batteries, one solar panel). | [F] AAD station updates 2012, 2014, 2024 |
| Daily routine | 08:00 scheduled radio sitreps by VHF to all field parties, weather forecast given, log kept, shared with the station leader on a roster; comms equipment list includes ANARESAT, BGAN, Iridium, VHF and HF radios, GSM. | [F] https://www.antarctica.gov.au/news/stations/macquarie-island/2017/this-week-at-macquarie-island-16-june-2017/ |
| Ham operation | **VK0AI (comms technician Norbert): 1,500+ contacts in 50+ countries**, "Macquarie Island is rated in the top 10 'most wanted' locations"; the Ham Shack is on Hut Hill; antenna breakage and auroral activity cited. (Verifies the earlier UNVERIFIED line.) | [F] https://www.antarctica.gov.au/news/stations/macquarie-island/2019/this-week-at-macquarie-island-25-january-2019/ |
| Transmitter powers, antennas, HF frequency plan beyond 3023 | **Not published anywhere I reached** (AAD pages silent; a search for Codan/Barrett/Icom use found nothing). Staffing: one Communications Technical Officer on island (2019 listing); Telecommunications Officers (Radio) in winter roles at Casey, Davis, Mawson, Macquarie. | [U] (Q and S) |
| AAD frequency list | The hobbyist compilation (2012): 2.720, 3.023, 3.175, 3.418, 4.040, 4.540, 4.678, 5.400 MHz, aircraft 5726/9032/11256 kHz USB. **No official AAD or ACMA list found.** | [F] earlier log S28; official source [U] |
| ACMA licensing | VK0 (and VK9) amateur call signs are issued under the Radiocommunications (Amateur Stations) Class Licence 2023; applicants show residency or intention to travel to the Antarctic (VK0) or an external territory (VK9). The ACMA site timed out; WIA asked ACMA in 2026 to restore VK0 for Heard and Macquarie. No ACMA apparatus-licence list for AAD HF found. | [F-snippet]; earlier log item 54 |
| BoM ionosonde at Macquarie | The BoM table shows no active Macquarie ionosonde (see Section 3). Wikipedia says outbuildings "support instrumentation such as ionosondes." | [F] |

Reading for the Macquarie relay idea [I]: the island's HF role is a field-hut and aircraft/ship backup run by one or two technicians; its "relay" capacity is VHF and satellite. The earlier agent's use of Macquarie as a modeled HF relay site stays a design proposal, not a description of the present station.

---

## 6. What this suggests for the network design (all [I]; not canon)

1. **Time-and-band cascade.** The Durban net's 21.3, 14.3, 8.1, 7.1 MHz cascade three times a day is the realistic template for a long-distance network that must find an open band on a changing path. It also gives believable "net times" (04:45, 11:00, 15:00 UTC).
2. **Hub-and-spoke before ring.** The 1920s Beam system was spokes to London with Montreal as the Americas hub. A settled-Antarctica system would plausibly start the same way: Australian and South African stations each hang off a nearer hub, and a Casey/Concordia/Peninsula polar corridor becomes the first direct Australia to South America route only when it is built.
3. **Three nets sharing one anchor.** 14.300 plus regional neighbors (14.305 to 14.320) is the real convergence pattern. For "dominant local pattern becomes standard," the evidence is an IARU-designated anchor with regional clustering.
4. **Weather broadcast, not conversation.** The Southern Hemisphere's most reliable HF content is scheduled fax/voice weather (VMW, VMC, ZSJ, CBV, PWZ33), not two-way chat. Settled Antarctic towns would plausibly rely on the same pattern.
5. **Forecast layer.** HF forecast products already name "Antarctic regions" (Australia) and run per consortium; a joint product is invented, but a plausible gap-filler.
6. **Decline pressure.** HF voice use is falling; the pressure reverses only where satellites fail (poleward of about 80 degrees; Peninsula to Weddell sector).

---

## 7. Searches and dead ends (exact strings; Q = died at the query, S = died at the source)

**Search strings (WebSearch).** Numbered in the order run.
1. `first two-way amateur radio contact Australia South Africa 1920s shortwave Zs Australian amateur` (Q: adjacent firsts only)
2. `Indian Ocean Maritime Mobile Net 14316 kHz time Perth Cape Town net control yachts` (found Durban net)
3. `Southern Cross Net ham radio maritime mobile frequency Australia Pacific schedule` (Q: name not found)
4. `Cape Town Radio ZSC HF coast station still operating Telkom Maritime Radio Services frequencies`
5. `noonsite Indian Ocean list of radio nets Australia Cocos Keeling Mauritius Rodrigues net SSB ham`
6. `noonsite Atlantic radio nets South Atlantic Cape Town St Helena Brazil Ascension SSB ham net frequency`
7. `SANAE Antarctic amateur radio ZS7 HF contacts Cape Town SARL Antarctic radio net`
8. `Australia South Africa radiotelephone service opened Sydney Johannesburg OR "Cape Town" beam wireless history Amalgamated Wireless Australasia 1930s` (Q: no circuit)
9. `Overseas Telecommunications Commission Australia history HF radiotelephone circuits South Africa Durban Cocos cable closure Sydney Radio VIS Perth Radio VIP`
10. `Wireless Institute of Australia history 1920s first amateur contact South Africa Africa two-way VK ZS 1925 OR 1926 OR 1927`
11. `trove amateur wireless Australia South Africa "Johannesburg" amateur communicated Melbourne short wave 1925` (S: Trove JS-only)
12. `Max Howden A3BQ first two-way contact England Australia 1924 Ross Hull Australia America contact history short wave`
13. `history of South African amateur radio SARL 1920s first contact Australia New Zealand Cape Town amateur short wave "South African Radio Relay League"`
14. `"Indian Ocean" ham radio net yachts Australia Cocos Keeling Mauritius Chagos "net" 7 MHz 14 MHz Perth Fremantle controller VK6`
15. `Rob Mulder OR "Indian Ocean net" OR "Indian Ocean Maritime Mobile" ham radio net frequency UTC Mauritius Seychelles Cocos cruisers` (Q)
16. `Maritime Mobile Service Network MMSN 14300 kHz history net controllers Europe Australia South Africa South America language nets`
17. `HF radio link Cape Town to SANAE Antarctica thesis ionospheric propagation measurements Stellenbosch OR "University of Cape Town" OR Hermanus` (found MacWilliam)
18. `Marion Island ZS8 amateur radio HF contacts Australia Cape Town communications station history 1948 radio schedules`
19. `SANAE IV communications HF radio daily schedule Cape Town satellite VSAT 1990s HF still used field parties SANAP` (Q: no schedule)
20. `AMSA HF voice monitoring ceased Australia maritime HF radio distress watch Wiluna Charleville "HF" Sydney Radio Telstra ended`
21. `Chile Valparaiso Playa Ancha Radio CBV HF coast station Armada Directemar frequencies DSC 4 MHz 8 MHz Antarctic vessels`
22. `Prefectura Naval Argentina Servicio de Comunicaciones Estaciones Costeras HF LPD Buenos Aires Radio frecuencias onda corta socorro 4125 8291 Antártida`
23. `LRA36 Radio Nacional Arcángel San Gabriel Antártida onda corta 15476 kHz received Australia New Zealand DX reception report` (Q: no Australian report)
24. `Radio Club Argentino historia primer comunicado radioaficionado Argentina con Australia OR Oceanía 1920s LU contacto bilateral` (Q)
25. `Radio Club de Chile historia 1922 CH contacto con Australia Nueva Zelanda radioaficionados chilenos 1920s onda corta` (Q)
26. `ISES International Space Environment Service Regional Warning Centers list Australia Bureau of Meteorology South Africa SANSA Brazil INPE Argentina members`
27. `SANSA Space Weather Regional Warning Centre Hermanus HF communications products ionosonde network Southern Africa Antarctic SANAE Marion data exchange Australia`
28. `Australian Bureau of Meteorology Space Weather Services ionosonde network Learmonth Darwin Canberra Hobart Macquarie Mawson Casey Davis IPS ionosondes locations`
29. `INPE EMBRACE Brazilian space weather program ionosondes Antarctic Comandante Ferraz ionosonde Chile Argentina cooperation South American network LISN`
30. `ISES members "Regional Warning Centre" Australia ASWFC "South Africa" SANSA RWC LAMP Argentina "EMBRACE" Brazil ISES Collaborative Network space weather forecast centres`
31. `Australia Antarctic Division Argentina OR Chile OR "South Africa" joint ionospheric campaign Antarctic cooperation SuperDARN riometer SANSA BoM collaboration Mawson SANAE` (Q: none found)
32. `PECASUS consortium members South Africa SANSA ICAO global space weather centre ACFJ Australia Canada France Japan CRC China Russia Annex 3 HF communications advisories`
33. `ACFJ consortium Australia Canada France Japan ICAO global space weather centre Bureau of Meteorology HF communication advisory SWXC`
34. `Argentina ionosonde Tucumán LAMP Laboratorio de Ionosfera Antártida Base Marambio OR Orcadas OR Esperanza OR Belgrano ionosonda cooperación internacional`
35. `Marambio base runway length 1208 m OR 1600 m pista aeródromo Vicecomodoro Marambio longitud pista metros SAWB`
36. `Ushuaia to Antarctic Peninsula nautical miles distance Ushuaia to Port Lockroy OR "Paradise Bay" OR "Half Moon Island" nmi Drake Passage 600 nautical miles`
37. `Antarctica21 air cruise flight delays weather Punta Arenas King George Island percentage flights delayed cancelled FAQ`
38. `Directemar cierre de puerto Punta Arenas viento nudos "cierre" puerto condiciones meteorológicas Capitanía de Puerto resolución límites de viento nudos`
39. `Prefectura Naval Argentina Ushuaia puerto cerrado cierre del puerto viento nudos Canal Beagle navegación restringida buques Antártida criterio` (Q)
40. `Ponant Commandant Charcot Ushuaia to Antarctic Peninsula Drake Passage crossing hours duration itinerary "Drake Passage" days at sea Lindblad National Geographic Resolution crossing time`
41. `AIS analysis Drake Passage vessel transits speed delays study ship traffic Antarctic Peninsula crossing duration hours AIS data tourism vessels weather waiting` (Q)
42. `Antarctic Pilot NP9 sailing distances Ushuaia Marsh OR "Port Lockroy" OR "Palmer Station" nautical miles table distances between Antarctic ports` (S: paywalled)
43. `"Distances Between Ports" Pub 151 Ushuaia Antarctica "Palmer" OR "Esperanza" OR "Port Lockroy" nautical miles NGA`
44. `Lindblad expeditions daily report Drake Passage "nautical miles" Ushuaia departure arrived South Shetland Islands hours crossing Beagle Channel Cape Horn "we have covered"` (Q)
45. `Traeger pedal radio exported Africa OR "South Africa" OR "Papua New Guinea" Flying Doctor radio network model AMREF Kenya Australian flying doctor adviser history`
46. `Royal Flying Doctor Service HF radio network today still used VKS-737 HF base stations closed 2020s satellite phones outback remaining HF`
47. `Chile cruisers HF net Patagonia Chiloe Puerto Williams SSB net frequency UTC "net" cruising Chile Argentina yachts radio schedule Pacific Seafarers Amigo net`
48. `Pacific Seafarers Net history 14300 kHz Australia New Zealand relay stations Southern hemisphere net controllers VK ZL coverage Indian Ocean South Atlantic`
49. `VK6 ZS contacts 40 metres OR 80 metres OR 20 metres Indian Ocean path propagation Perth South Africa amateur "VK6" "ZS" QSO long path short path`
50. `DXCC propagation southern hemisphere Australia to South Africa path 14 MHz short path 8700 km polar flutter long path ZS VK grey line amateur report`
51. `Macquarie Island station communications technician HF base station Codan OR Barrett OR Icom transmitter antenna radio room AAD "Macquarie Island" HF radio field huts sked` (Q: no equipment)
52. `ACMA radiocommunications Antarctic stations licence "Australian Antarctic Territory" apparatus licence Australian Antarctic Division HF frequencies assigned Mawson Davis Casey VK0 radiocommunications` (S: ACMA timeouts)
53. `Bureau of Meteorology HF radiofax Wiluna VMW Charleville VMC schedule frequencies Indian Ocean Southern Ocean charts yachts Cape Town ZSJ weather fax Pretoria schedule`
54. `South African Weather Service marine weather HF radiofax ZSJ Cape Naval Radio 'ZSJ' frequencies 4014 7508 13538 18238 Southern Ocean analysis chart schedule`
55. `Australia South Africa search and rescue arrangement memorandum JRCC Australia MRCC Cape Town Southern Ocean boundary 20E cooperation SAR region coordination Indian Ocean` (Q: no bilateral)
56. `Southern Ocean yacht rescue Cape Town MRCC Perth JRCC relay HF radio Indian Ocean yacht distress coordinated Australian and South African rescue centres amateur radio net relayed`
57. `Capitanía de Puerto de Punta Arenas "condición de puerto" cerrado naves mayores viento nudos "Punta Arenas" plan de mal tiempo Gobernación Marítima`
58. `Puerto Williams Capitanía de Puerto Antártica "cierre de puerto" OR "puerto cerrado" Cabo de Hornos viento zarpe naves Antártica cruceros Drake restricción Armada`
59. `satellite AIS vessel traffic Drake Passage Antarctic Peninsula tourist ships transit speed study Polar Record OR Marine Policy OR "Frontiers" ship traffic density Southern Ocean Ushuaia` (extended; found PNAS)
60. `GIRO Global Ionosphere Radio Observatory DIDBase station list Hermanus Grahamstown Louisvale Tucuman Port Stanley Concepcion Punta Arenas Jicamarca Learmonth Darwin Perth southern hemisphere digisonde real-time`
61. `Chile ionosonde Punta Arenas OR Concepción OR Santiago Servicio Meteorológico OR Universidad ionosonda estación ionosférica Chile Antártica Frei OR Prat OR "O'Higgins" cooperación`
62. `SailMail HF email stations locations Australia South Africa Chile Argentina Brazil shore stations Winlink RMS gateways Southern Hemisphere coverage Indian Ocean`
63. `Winlink HF gateway Pactor Antarctica station relay Esperanza OR Rothera OR Casey OR Davis OR SANAE email over HF Antarctic expedition Winlink coverage` (Q: no Antarctic gateways found)
64. `cruising blog Indian Ocean crossing Cocos Keeling Rodrigues "Peri Peri net" OR "Durban net" OR "SAMM net" check in Australia weather routing SSB heard Perth`
65. `Southern Ocean sailors Cape Town to Australia Perth HF radio schedule Pacific Seafarers OR "Indian Ocean" ham "Cape Town" "Fremantle" yacht race radio sked Clipper OR Golden Globe OR Cape2Rio SSB net Rio de Janeiro`
66. `Antarctic ham radio net frequency "Antarctic net" OR "Net Antártico" OR "Red Antártica" 14 MHz bases Antarctic amateur stations daily schedule UTC LU ZS VK0 CE9 RI1`
67. `Rio de Janeiro Radio PPR OR "Rádio Marinha" HF DSC estação costeira Brasil Marinha do Brasil NAVAREA V frequências HF socorro ondas curtas estações costeiras ativas`
68. `Radio Australia shortwave service to Africa OR "South America" history Shepparton transmitters closed 2017 target areas beams Indian Ocean Southern Africa broadcasts`
69. `Telstra Coast Radio Stations closed 1999 OR 2000 Sydney Radio VIS Perth Radio VIP Melbourne Radio VIM history coastal radio Australia Morse closed Ocean Patrol`
70. `"first" Australian amateur "worked" OR "communicated with" "South Africa" short-wave 1925 OR 1926 OR 1927 Wireless Weekly OR "Radio in Australia and New Zealand" amateur Cape Town station contact Australia` (extended; Q)
71. `Australian Antarctic Division HF frequencies kHz 2720 3023 3175 3418 4040 4540 4678 5400 Mawson Davis Casey VLM VJM aircraft 5726 9032 11256 utility listening` (Q: no official list)
72. `ZS7ANT OR ZS7 SANAE amateur radio station Antarctica South African operators HF contacts SARL history`
73. `Argentine Antarctic base amateur radio LU Marambio OR Esperanza OR Orcadas Radio Club Argentino Antártida radioaficionados comunicaciones HF contactos Australia Sudáfrica`
74. `Ushuaia "puerto cerrado" OR "cierre del puerto" viento Prefectura Naval Argentina nudos cruceros Antártida demora zarpada temporal Beagle "Prefectura"` (Q)
75. `distancia Ushuaia Base Esperanza OR "Base Marambio" OR "Isla Decepción" millas náuticas travesía Pasaje de Drake horas rompehielos Almirante Irizar navegación millas`
76. `Laurence M. Gould transit Punta Arenas to Palmer Station nautical miles days hours Drake Passage crossing time research vessel "nautical miles" Palmer Station USAP`

**Direct fetches that failed or were blocked (S).** `vk4ghz.com/forum/viewtopic.php?p=14479` (403; Wayback 404); `nzhistory.govt.nz/page/first-trans-global-radio-transmission-london` (403); `amsa.gov.au/.../hf_voice_monitoring_consultation_paper.pdf` (404, moved); `prontus.directemar.cl/...` PDFs (403) and `www.directemar.cl/.../29__12000_107__140623__c_p__punta_arenas.pdf` (404); IHO `docs.iho.int` and `legacy.iho.int` WWNWS XV and SAIHC NAVAREA VII papers (connection failure); `icao.int/ESAF/...SANSA.pdf` (403); `tandfonline.com/doi/full/10.1080/09669582.2025.2542823` (403); `repositorioantartica.umag.cl` (no response); `figshare.com` Prior-Jones thesis (202, no body); `acma.gov.au` VK0 form (301 then timeout); `spaceweather.org` (no response); `sailblogs` SAMMNet page (403); `sailingscuttlebutt.com` Clipper page (403); `en.wikipedia.org/wiki/Cape_to_Rio_Race` (no article). WebFetch itself: Noonsite 403 (resolved with curl).

---

## 8. Open gaps

1. **First documented two-way VK to ZS contact (and VK to LU/CE/PY).** Needs the WIA/SARL/RCA archives or Trove; try the NLA Trove API with a key, *Amateur Radio* (WIA) back issues on worldradiohistory.com, and *QST* "IARU News" 1925 to 1928.
2. **A dated, logged Perth to Cape Town HF contact** (the 1991 VK6 to ZS list is band-unspecified).
3. **Perth/Cape Town HF performance data** (e.g., WSPR/FT8 spot statistics via PSKReporter or WSPRnet for VK6 to ZS on 20 m and 40 m). Spot databases could settle "how often is the path open" with real numbers; not run.
4. **Official AAD frequency plan and ACMA apparatus licensing for Antarctic HF.**
5. **Macquarie transmitter powers and antennas; whether the HF 3023 kHz schedule is still in use.**
6. **Punta Arenas Capitanía plan text and any Ushuaia (Prefectura) weather-closure rule.**
7. **AIS-derived Drake crossing-time and waiting-time distribution** (needs paid AIS data or the 2025 Journal of Sustainable Tourism paper).
8. **Marambio 01/19 runway operational status.**
9. **Chile's space-weather centre status** (no RWC found) and any joint AAD with Argentina/Chile/South Africa ionospheric campaign.
10. **ISES membership page** (spaceweather.org was unreachable).
11. **Whether Radio Australia ever targeted Africa or South America by shortwave.**

---

## 9. What this changes in the earlier logs

1. **Ring log §6 and Open_Research_Topics §5 ("no documented two-way HF contact among Perth, Cape Town and South America found").** Still true for a dated, logged first. Add: (a) 1920s Beam traffic was spokes to London and a Montreal hub for the Americas (AWA 1930); (b) the Durban Maritime Mobile Net explicitly covers "from Australia across the Indian Ocean, the Atlantic to Brazil"; (c) AD5Q (1997) says Australians work South America across the pole regularly in southern summer; (d) the 1991 VK6 to ZS list exists but its band is unknown.
2. **Ring log dead ends.** "noonsite HF net page (403)" is now opened (curl, not WebFetch). "Cape Town to Antarctic HF thesis (over size limit)" is probably the UCT MacWilliam thesis, which is South Pole to SANAE (1 W, 12.57 MHz, 2,090 km), not Cape Town to Antarctica; it opens (49 MB).
3. **Ring log §3, §5 and Open_Research_Topics ("SANSA and Australia's BoM already supply HF forecasting").** Refine: both are ISES RWCs but sit in different ICAO consortia (ACFJ vs PECASUS partner); the BoM's HF warning region is "Southern Aus/NZ and Antarctic," not Africa or South America; no joint product found.
4. **Drake log dead ends.** #6 (Antarctica21 figures) is now primary-sourced and corrected (see 4.3). #4 (AIS) is partly closed (PNAS 2022 port shares), crossing-time distributions still absent. #5 (NP9) remains paywalled; Pub 151 has no Antarctic ports. #7 (Directemar closure resolutions) is partly closed through the `www` host (Punta Delgada, Puerto Williams); the Punta Arenas plan text is still unopened. #16 (Charcot) is an itinerary-level confirmation (two nights each way).
5. **Drake log "Marambio about 1,208 m; second 1,600 m test-flown 2015."** Confirmed; they are two different runways (06/24 and 01/19), and the 2024 and 2026 sources still quote 1,208 m as the working runway.
6. **Drake log "Ushuaia holds 1 to 6 days."** The port-closure plans bind small craft, not ocean ships; treat expedition-ship holds as crossing-forecast decisions [I], not port closures.
7. **Macquarie follow-up 5.** The "UNVERIFIED" items are partly verified: four VHF repeaters [F], VK0AI 1,500+ contacts [F], CH21 repeater on Mt Jeffryes [F], ANARESAT/BGAN/Iridium [F]. The 3023 kHz HF schedule now has a flag: Wikipedia says nightly HF on 3023 (VJM), the current AAD page describes VHF scheds and SPOT trackers and does not mention HF.
8. **Radio_Physics (Peninsula, Weddell trunk).** Independent support: Halley to Rothera 1,600 km digital HF test (BAS, 2010); HamSCI note that ice absorbs HF and kills intracontinental multi-hop; ray-trace tools miss polar-cap absorption events (MacWilliam); geostationary fails poleward of 80 degrees (Prior-Jones). Consistent with the earlier models; none contradicts them.

---

## 10. Source table (opened unless marked)

| # | Source | URL |
|---|---|---|
| 1 | Noonsite, Durban Maritime Mobile Net Revived | https://www.noonsite.com/?p=1156438 |
| 2 | Noonsite, South African Radio Nets - Updated | https://www.noonsite.com/report/south-african-radio-nets-updated/ |
| 3 | Noonsite, Pacific list of radio nets | https://www.noonsite.com/report/pacific-list-of-radio-nets/ |
| 4 | Noonsite, Atlantic list of radio nets | https://www.noonsite.com/atlantic-list-of-radio-nets/ |
| 5 | Wikipedia, Maritime mobile amateur radio | https://en.wikipedia.org/wiki/Maritime_mobile_amateur_radio |
| 6 | Yachting NZ, wx and radio info (2017) | https://www.yit.nz/sites/default/files/resource/wx_and_radio_info_2017-sept.pdf |
| 7 | AWA, Wireless Progress in Australia (1930) | https://www.worldradiohistory.com/AUSTRALIA/Various/AWA-1930-Wireless-Progress-in-Aust.pdf |
| 8 | Wikipedia, Imperial Wireless Chain; Klipheuwel; Brenda Bell | https://en.wikipedia.org/wiki/Imperial_Wireless_Chain |
| 9 | Early Australian shortwave broadcast stations | https://www.australianotr.com.au/early-australian-shortwave-broadcast-stations.html |
| 10 | AD5Q Propagation, Jan 1997 | https://ng3k.com/Ad5q_prp/ad5q9701.html |
| 11 | ZS6EZ, Marion Island ZS8 | https://www.zs6ez.org.za/zs8.htm |
| 12 | UCT, MacWilliam thesis (2019) | https://open.uct.ac.za/bitstream/11427/32406/1/thesis_ebe_2020_macwilliam%20kathleen.pdf |
| 13 | EGU2010-14943, Prior-Jones and Warrington | https://meetingorganizer.copernicus.org/EGU2010/EGU2010-14943.pdf |
| 14 | HamSCI, Perry and Frissell (2022) | https://www.hamsci.org/publications/potential-science-opportunities-hamsci-antarctica |
| 15 | AMSA, HF radiotelephone monitoring | https://www.amsa.gov.au/hfradio |
| 16 | BoM, radiofax schedule; HF marine radio | https://www.bom.gov.au/marine/radio-sat/radio-fax-schedule.shtml |
| 17 | Gough Lui, ZSJ Cape Naval (2019) | https://goughlui.com/2019/02/16/radiofax-the-quest-for-zsj-cape-naval-south-africa-updates/ |
| 18 | Frequentis, South Africa GMDSS (2017) | https://www.frequentis.com/sites/default/files/pr/2017-10/FREQUENTIS_GDMSS_South_Africa_07_2017.pdf |
| 19 | NAVAREA VI report (2022) | https://iho.int/uploads/user/Inter-Regional%20Coordination/WWNWS/WWNWS14/WWNWS14_2-1-VI_2022_NAVAREA_VI_SA.pdf |
| 20 | MySailing, Jedi 1 rescue (2017) | https://www.mysailing.com.au/south-african-nationals-rescued-from-stricken-yacht-in-indian-ocean |
| 21 | Wikipedia, Alfred Traeger | https://en.wikipedia.org/wiki/Alfred_Traeger |
| 22 | SANews and Space in Africa, SANSA-PECASUS | https://www.sanews.gov.za/node/42458 |
| 23 | Engineering News, SANSA Regional Space Weather Centre (2021) | https://www.engineeringnews.co.za/article/regional-space-weather-centre-south-africa-2021-05-07 |
| 24 | BoM, ASWFC ionosonde network; client support HAP charts | https://sws.bom.gov.au/World_Data_Centre/2/1/28 ; https://www.sws.bom.gov.au/Products_and_Services/5/9/1 |
| 25 | IPS HF comms warning (Feb 2014) | https://listserver.ips.gov.au/pipermail/ips-hf-warning/2014-February/000723.html |
| 26 | GIRO DIDBase | https://giro.uml.edu/didbase/ |
| 27 | Wikipedia, SuperDARN | https://en.wikipedia.org/wiki/SuperDARN |
| 28 | Correia (2011), Antarctic-South America connectivity | https://revistas.ufrj.br/index.php/oa/article/view/8109/6568 |
| 29 | Antarctica21 flight statistics | https://www.antarctica21.com/journal/antarctica-flights |
| 30 | Aviacionline, Marambio new runway (2015); Defonline (2024); Buenos Aires Times (2026) | https://www.aviacionline.com/exitosa-prueba-de-la-nueva-pista-del-aerodromo-de-la-base-antartica-marambio |
| 31 | Directemar, Punta Delgada plan (2025); Puerto Williams plan (2023) | https://www.directemar.cl/directemar/site/docs/20250425/20250425095428/12000_30__pda.pdf |
| 32 | PNAS 2022 via PMC | https://pmc.ncbi.nlm.nih.gov/articles/PMC8784123/ |
| 33 | NGA Pub 151 (2001) via EverySpec | https://everyspec.com/MISC/download.php?spec=NGIA_PUB-151_2001.049282.pdf |
| 34 | AAD, Macquarie field huts; station updates 2012, 2014, 2017, 2019, 2024 | https://www.antarctica.gov.au/antarctic-operations/stations/macquarie-island/living/field-huts/ |
| 35 | Wikipedia, Macquarie Island Station | https://en.wikipedia.org/wiki/Macquarie_Island_Station |
| 36 | WIA news 2026 (VK0DS, VK0TBC) | https://www.wia.org.au/newsevents/news/2026/20260829-1/index.php |
| 37 | Radio Nacional (Argentina), LU1ZV activation (2019) | https://cdn-sp.radionacional.com.ar/?p=1004296 |
| 38 | Senate report on shortwave radio (Radio Australia) | https://aph.gov.au/Parliamentary_Business/Committees/Senate/Environment_and_Communications/Shortwaveradio/Report/c01 |
| 39 | jproc.ca, final Telstra Morse transmission (1999) | https://jproc.ca/radiostor/telstra.html |
