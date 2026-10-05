<!-- Agent report, 2026-10-04. Web research plus live measurement (RIPE Atlas, TeleGeography cable API). Slice: COMMUNICATIONS DEMAND (latency, redundancy, cable facts, who generates cross-hemisphere traffic). Real countries and firms are used as geography and economy only (GPS law); no national-character claims. Model output: spot-check before relying on it. -->

# Does Australia gain from communicating with South America and South Africa? Evidence from latency, cables, chokepoints and traffic sources (2026-10-04)

No project files were edited. Only this file was created. All times are as of 2026-10-04 (UTC clock on the research host read 22:35 UTC on 4 Oct 2026).

## 0. Bottom line (read this first)

1. **The premise of a latency penalty is TRUE and large, and it is mostly physics plus routing, not trade.** Today every Australia-to-South-America and Australia-to-South-Africa packet detours through the northern hemisphere: Sydney to Johannesburg goes Sydney, San Jose (California), then on to Johannesburg (RIPE Atlas traceroute, section 3.4); Sydney to Santiago and Sydney to Sao Paulo also go via San Jose; Perth to Cape Town goes Perth, Oman, Marseille, London, Cape Town. Measured round-trip times today are 265-312 ms (Sydney-Santiago), about 303 ms (Sydney-Sao Paulo), 415-474 ms (Sydney-Cape Town), 430-474 ms (Sydney-Johannesburg) and 353-524 ms (Perth-Cape Town). The physics floor (light in fiber, great-circle path) is 108 ms (Sydney-Johannesburg), 111 ms (Sydney-Santiago) and 85 ms (Perth-Cape Town). Measured values are 2.4 to 4.7 times the floor. [F, my measurements]
2. **The Grok figures are roughly right for the public Internet, too high for a cloud backbone.** Johannesburg-Sydney "about 400 ms": measured 424 ms (WonderNetwork) and 430 ms (RIPE Atlas) on the public Internet, 328 ms on Microsoft's private backbone. South America "about 300 ms": measured 265-312 ms (Santiago), 295-312 ms (Sao Paulo), 306-346 ms (Buenos Aires). "Umoja about 110-150 ms to eastern South Africa": my own estimate gives about 98-114 ms Perth-Johannesburg and about 146-161 ms Sydney-Johannesburg, so the claim is plausible but is NOT published by Google (Umoja's length is unpublished). "Humboldt about 2028": consistent (installation from Q4 2026, service 2028 per single-source trade press; TeleGeography does not list Humboldt under that name at all). [F / I]
3. **Umoja is NOT in service as of 4 Oct 2026.** TeleGeography's live data says planned, ready-for-service 2028, landing Mandurah (Western Australia) to Amanzimtoti (KwaZulu-Natal, landing point flagged "TBD"), supplier SubCom, owner Google. The ANU National Security College paper (Aug 2026, using TeleGeography as of Jan 2026) says 2027. Google confirmed the African terrestrial part (built with Liquid Intelligent Technologies) as complete in 2024; in July 2026 TechCentral reported the Eastern Cape hub had permits but had "yet to break ground". The "early 2026" start date in the earlier log is NOT supported by any source I opened. [F]
4. **Redundancy is the best-evidenced reason, and it is happening right now.** Perth lost all direct low-latency subsea paths to Singapore in August-September 2026 (INDIGO West and INDIGO Central shunt faults on 8 Aug; Australia-Singapore Cable severed off Java on 4 Sep). Rerouted Australia-Singapore traffic reached 300-400 ms. My live RIPE Atlas measurements on 4 Oct 2026 still show Perth probes on some networks at 192-312 ms to Singapore (one network at 53 ms). The ANU paper states that the Red Sea carries "the great majority of Australia's westwards-bound data traffic" and that the Indonesian straits are the other chokepoint. A southern route (Perth to Africa, Perth to Chile via French Polynesia) bypasses both. [F]
5. **But redundancy is a reason for southern ROUTES, not for Australia to want South America or South Africa as destinations.** Direct commercial traffic between Australia and these continents is tiny. The identifiable generators of cross-hemisphere traffic are, in order of evidence: (a) hyperscaler backbones (Google built Humboldt and Umoja, Meta's Waterworth lists Brazil and South Africa; Humboldt's 144 Tbit/s design capacity is 2.9 times Australia's entire 2024 international bandwidth of 49,090 Gbit/s); (b) the SKA (the only quantified, funded Australia-South Africa data flow: the SKA-NREN Forum states "Expect significant traffic between AU & ZA", about 20-100 Gbit/s class); (c) multinational mining and resource firms with management in both hemispheres (Gold Fields, South32), which need links but not special ones; (d) astronomy and Antarctic programs (small). **Trade, finance and mining operations do NOT generate a measurable need beyond the generic Internet.** Mining remote-operations centers are domestic (Perth for the Pilbara, Santiago for Chilean mines). [F / I]
6. **Time zones kill live overlap with South America entirely** (0 hours of 09:00-17:00 overlap for Perth or Sydney with Santiago, Buenos Aires or Sao Paulo, in every season) and limit South Africa to 2 hours (Perth) or 0-1 hours (Sydney). Cross-hemisphere work is asynchronous (follow-the-sun handover) except Perth-South Africa. [C]

## 1. Method, tags and limits

- **[F]** = source opened and read (URL and year given). **[F-snippet]** = search-engine summary only. **[I]** = my inference. **[C]** = my computation (script text in section 11). **[U]** = unverified.
- Live measurements used the RIPE Atlas public API (anchoring-mesh ping and traceroute measurements, last 24 h or last 6 h before 22:35 UTC on 4 Oct 2026), the TeleGeography Submarine Cable Map JSON API (all 712 cable records fetched), Microsoft's published Azure P50 latency matrix (30-day window ending 30 Jul 2026), and WonderNetwork's ping table (page fetched 4 Oct 2026).
- Search budget: about 35 WebSearch calls and about 45 fetch or curl calls. Dead ends are in section 12.
- Caveat on public-Internet latency: each number reflects specific networks (the source ISP and the target host's ISP). Different anchors in the same city differ by up to 150 ms (for example, Sydney to the two Cape Town anchors: 415 ms and 474 ms). Quote ranges, not points.

## 2. Cable facts (verified against TeleGeography's live data and primary pages)

### 2.1 Cables touching Australia, from TeleGeography's API (fetched 2026-10-04) [F: https://www.submarinecablemap.com/api/v3/cable/all.json and per-cable JSON]

In service (those relevant here): Southern Cross (2000); Australia-Japan Cable (2001); Telstra Endeavour (2008, Sydney-US); PIPE Pacific Cable-1 (2009); Hawaiki (2018); Australia-Singapore Cable (ASC, 2018, 4,600 km, via Christmas Island and Indonesia); INDIGO-West (2019, Perth-Jakarta-Singapore, 4,600 km); INDIGO-Central (2019, Perth-Sydney, 4,850 km); JGA-South (2020); Oman Australia Cable (OAC, Oct 2022, 11,000 km, Perth-Cocos-Diego Garcia-Oman, owner SUBCO, supplier SubCom); Southern Cross NEXT (2022, 13,700 km, via Fiji, Kiribati, Tokelau, New Zealand to the US); Darwin-Jakarta-Singapore (2023). The ANU paper counts 16 operational international cables. **None of the in-service cables lands in South America or Africa.**

Planned (as listed 4 Oct 2026):

| Cable | RFS per TeleGeography | Route | Owner | Note |
|---|---|---|---|---|
| Honomoana | 2026 | Melbourne and Sydney, French Polynesia (Faratea and Papenoo), Auckland, San Diego; 15,215 km | Google | Pacific Connect; the Australian end of the French Polynesia hop that Humboldt needs |
| Tabua | 2026 | Australia-Fiji-US | Google | |
| **Umoja** | **2028** | **Mandurah WA to Amanzimtoti, South Africa (TBD)**; length not published | Google | ANU (Jan 2026 data) says 2027 |
| TalayLink | 2028 | Mandurah and Melbourne, Christmas Island, Satun (Thailand) | Google | |
| Bosun | 2029 (ANU: 2027) | Darwin-Christmas Island | Google | Australia Connect initiative |
| APX East | 2028 Q4 | TeleGeography record lists Sydney, Suva, Kapolei and "Los Angeles, Chile"; 13,000 km | SUBCO | **Data error: SUBCO's own press release describes Sydney to California (mainland US), with Hawaii and Fiji branches in 2029; "Los Angeles, Chile" appears to be a mix-up with Los Angeles, California. APX East is NOT a Chile-Australia cable.** [I from F-snippet: https://sub.co/news/press-release-subco-announces-australia-us-express-submarine-cable-for-2028-apx-east] |
| Halaihai | 2029 | Valparaiso (TBD), French Polynesia, Guam, Tinian; 17,483 km | Google | Central Pacific Connect |
| Project Waterworth | none given | 50,000 km; Darwin (TBD), Fortaleza (Brazil), Cape Town, Amanzimtoti, Mumbai, Chennai, Penang, Los Angeles, Myrtle Beach | Meta | Meta's own announcement says "the U.S., India, Brazil, South Africa, and other key regions", 24 fiber pairs, no completion date, and does not mention Australia; the Darwin entry comes from TeleGeography only. [F: https://engineering.fb.com/2025/02/14/connectivity/project-waterworth-ai-subsea-infrastructure/] |

### 2.2 Humboldt

- Announced 11 Jan 2024 by Google Cloud with Desarrollo Pais and the Office of Posts and Telecommunications of French Polynesia; "first direct cable route between South America and Asia-Pacific"; benefits listed: resilience, "lower latency for businesses and public sector organizations", geographically diverse routes; interconnects the South Pacific Connect cables. No length, fiber pairs or date in the post. [F: https://cloud.google.com/blog/products/infrastructure/announcing-humboldt-the-first-cable-route-between-south-america-and-asia-pacific]
- Route Valparaiso (landing at Santo Domingo) to French Polynesia to Sydney, about 14,800 km (14,810 km, USD 395 million CAPEX in a REUNA slide of Jan 2022). 50/50 Google and Desarrollo Pais; installation agreement June 2025; capacity stated by Chile as 144 Tbit/s, 25-year life; 16 fiber pairs and a second Santo Domingo-Panama City leg of about 6,500 km reported by one trade source. [F: https://en.wikipedia.org/wiki/Humboldt_Cable ; https://www.amlight.net/wp-content/uploads/2022/01/AlbertAstudillo-REUNA-SA3CC2022.pdf ; F-snippet: https://developingtelecoms.com/telecom-technology/optical-fixed-networks/20454-humboldt-cable-gets-go-ahead-from-chile.html]
- Status: regional approval of the landing; subsea work to start Q4 2026, service 2028, earlier estimates 2027. [F-snippet, several outlets]
- **TeleGeography's map has no cable named Humboldt** (checked all 712 records). It does list Honomoana (Sydney to French Polynesia, 2026) and Halaihai (Valparaiso to French Polynesia to Guam, 2029). [I] The Humboldt route is probably carried in TeleGeography's data as those two records combined; I could not confirm.
- Neither Humboldt nor any Chile-Australia cable appears in the ANU paper's Figure 4 list of planned Australian cables (Jan 2026). [F]

### 2.3 Umoja and Africa

- Google announcement 23 May 2024: first fiber route to connect Africa and Australia, anchored in Kenya, through Uganda, Rwanda, DRC, Zambia, Zimbabwe and South Africa (including the Google Cloud region), then across the Indian Ocean to Perth. Terrestrial path built with Liquid Intelligent Technologies. Stated purpose: "a new route distinct from existing connectivity routes" for "a region that has historically experienced high-impact outages". Kenya's president William Ruto: "crucial in ensuring the redundancy and resilience of our region's connectivity...especially in light of recent disruptions caused by cuts to sub-sea cables". No launch date in the post. [F: https://cloud.google.com/blog/products/infrastructure/investing-in-connectivity-and-growth-for-africa]
- July 2026: Google confirmed the Eastern Cape as the southern anchor of a four-hub African "Digital Exchange Port" network; permits secured, construction not begun, exact site undisclosed, no completion date. The hub also lands a planned South Africa-India cable (Visakhapatnam and Chennai). [F: https://techcentral.co.za/google-plots-e-cape-as-southern-anchor-of-four-hub-africa-network/283283/ ; F-snippet: https://w.media/google-announces-digital-exchange-port-connecting-south-africa-to-india/]
- African cables in service touching South Africa (TeleGeography [F]): SAFE (2002, to India and Malaysia, no Australia), SAT-3/WASC (2002), SEACOM/Tata TGN-Eurasia (2009), EASSy (2010), ACE (2012), WACS (2012), DARE-1 (2021), METISS (2021), Equiano (2023, to Portugal), T3 (2023), 2Africa (2024). No cable in service links South Africa to South America; SACS (Angola-Fortaleza, 6,165 km, 40 Tbit/s, 2018) is the only African-South American cable and does not touch South Africa. [F-snippet: https://en.wikipedia.org/wiki/SACS_(cable_system)]
- Cape Town to Buenos Aires RIPE Atlas RTT is 168 ms on the best pair and 380 ms on the worst (section 3.2), against a floor of 67 ms: the third leg of the ring is also poor.

## 3. Latency: measured, physical floor, and today's routes

### 3.1 Physics floor [C]

Light in single-mode fiber: group index 1.4682 (SMF-28 typical at 1550 nm), so v = 299,792.458 / 1.4682 = 204,190 km/s. Round-trip time per 100 km of fiber is 0.979 ms (vacuum: 0.667 ms). Great-circle distance by haversine on a sphere of radius 6,371.0088 km. Real cable routes are 1.2 to 1.4 times the great circle; the measured Sydney to San Jose RTT of about 145 ms against a great-circle floor of 117 ms is a ratio of 1.24 (cable route plus equipment), which is the calibration I use.

| Pair | Great-circle km | RTT floor (ms) | At 1.2x route | At 1.4x route |
|---|---|---|---|---|
| Sydney-Johannesburg | 11,041 | 108 | 130 | 151 |
| Sydney-Cape Town | 11,012 | 108 | 129 | 151 |
| Perth-Johannesburg | 8,314 | 81 | 98 | 114 |
| Perth-Cape Town | 8,697 | 85 | 102 | 119 |
| Mandurah-Durban | 7,830 | 77 | 92 | 108 |
| Sydney-Santiago | 11,347 | 111 | 133 | 156 |
| Sydney-Sao Paulo | 13,357 | 131 | 157 | 183 |
| Sydney-Buenos Aires | 11,801 | 116 | 139 | 162 |
| Perth-Santiago | 12,711 | 125 | 149 | 174 |
| Perth-Sao Paulo | 13,569 | 133 | 160 | 186 |
| Perth-Buenos Aires | 12,590 | 123 | 148 | 173 |
| Sydney-San Jose, California | 11,965 | 117 | 141 | 164 |
| San Jose-Johannesburg | 16,932 | 166 | 199 | 232 |
| Cape Town-Buenos Aires | 6,870 | 67 | 81 | 94 |
| Cape Town-Sao Paulo | 6,345 | 62 | 75 | 87 |
| Sydney-Perth | 3,291 | 32 | 39 | 45 |
| Sydney-Singapore | 6,306 | 62 | 74 | 87 |
| Perth-Singapore | 3,914 | 38 | 46 | 54 |

Humboldt: 14,800 km of cable alone gives 145 ms round trip; with about 5 ms of terminal equipment and 144 km of Chilean land fiber, Santiago-Sydney is about 151 ms. [C]

### 3.2 Measured round-trip times today

**Source A: RIPE Atlas anchoring mesh, median of per-sample minimum RTT over the last 24 h, probes on Telstra (Sydney AS1221 probe 7326; Perth AS1221 probe 7262), Vocus (Perth 7432) and Spintel (Perth 7547).** [F, my measurement via https://atlas.ripe.net/api/v2/ ; raw output in section 11]

| Pair | Measured range (ms) | Physics floor | Ratio |
|---|---|---|---|
| Sydney to Johannesburg | 430 (AS12008 anchor), 474 (AS3491 anchor) | 108 | 4.0-4.4 |
| Sydney to Cape Town | 415 (AS328266), 474 (AS37153) | 108 | 3.8-4.4 |
| Perth to Johannesburg | 434-493 (four source networks) | 81 | 5.4-6.1 |
| Perth to Cape Town | 353-524 | 85 | 4.2-6.2 |
| Sydney to Santiago | 265 (two anchors), 312 (a third) | 111 | 2.4-2.8 |
| Sydney to Sao Paulo | 303 | 131 | 2.3 |
| Sydney to Buenos Aires | 306 (CABASE anchor), 448 (ARIU university anchor) | 116 | 2.6-3.9 |
| Perth to Santiago | 310-379 | 125 | 2.5-3.0 |
| Perth to Sao Paulo | 348-380 | 133 | 2.6-2.9 |
| Perth to Buenos Aires | 357-447 | 123 | 2.9-3.6 |
| Sydney to Perth (control) | 47.4-49.0 | 32 | 1.5 |
| Cape Town to Sydney | 415 (Atomic), 474 (xneelo) | 108 | |
| Cape Town to Buenos Aires | 168 (Atomic), 380 (xneelo) | 67 | 2.5-5.7 |
| Cape Town to Sao Paulo | 239 (Atomic), 333 (xneelo) | 62 | 3.8-5.4 |
| Santiago to Sao Paulo | 48-49 | | |
| Santiago to Buenos Aires | 22 | | |

**Source B: Microsoft Azure published P50 round-trip latency between regions, 30 days ending 30 Jul 2026 (private backbone, so the best case).** [F: https://learn.microsoft.com/en-us/azure/networking/azure-network-latency ; raw table https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main/articles/networking/azure-network-latency.md ; region locations https://learn.microsoft.com/en-us/azure/reliability/regions-list : Australia East = New South Wales, Australia Southeast = Victoria, Brazil South = Sao Paulo State, South Africa North = Johannesburg, South Africa West = Cape Town]

| Pair | P50 RTT (ms) |
|---|---|
| Australia East - South Africa North | 328 |
| Australia East - South Africa West (Cape Town) | 328 |
| Australia Southeast - South Africa North | 321 |
| Australia East - Brazil South | 295 |
| Australia Southeast - Brazil South | 307 |
| Australia East - West US | 140 |
| Australia East - Southeast Asia (Singapore) | 95 |
| Australia East - UK South | 261 |
| Australia East - Central India | 144 |
| South Africa North - Brazil South | 321 |
| South Africa North - UK South | 163 |
| South Africa North - Southeast Asia | 177 |
| Brazil South - West US | 169 |
| Brazil South - Southeast Asia | 331 |

Azure's page lists no Perth region and, although a Chile Central (Santiago) region exists, no Chile row in the matrix. Note that Australia East to South Africa North at 328 ms is larger than going via Southeast Asia (95 + 177 = 272), so the cloud backbone itself does not use a Singapore route for it. [I]

**Source C: WonderNetwork ping table (fetched 4 Oct 2026).** [F: https://wondernetwork.com/pings/Sydney and /Perth ; HTML parsed, distances are WonderNetwork's] From Sydney: Johannesburg 424 ms, Cape Town 414, Sao Paulo 312, Santiago 308, Buenos Aires 346, Montevideo 362, Lima 278, Nairobi 409, Singapore 166, Los Angeles 159, London 269, Perth 46, Auckland 34. From Perth: Johannesburg 476, Cape Town 483, Sao Paulo 358, Santiago 353, Buenos Aires 392, Singapore 210, Jakarta 232, Sydney 46. **Caveat: WonderNetwork's Perth to Singapore (210 ms) and Perth to Jakarta (232 ms) are about the same as Sydney's plus 46 ms, so their Perth server's traffic hairpins through Sydney. Treat WonderNetwork Perth figures as pessimistic.**

**Source D: Verizon Enterprise monthly latency (August 2026, past-12-month window).** [F: https://www.verizon.com/business/terms/latency/] Australia to US 152 ms; Chile to US 98 ms; Argentina to US 118 ms; Trans-Pacific 113 ms; Singapore to US 169 ms. Sum Australia-US-Chile 250 ms, which matches the 265 ms Sydney-Santiago measurement via San Jose within a few percent. [I]

### 3.3 Grok's claims, checked

| Claim | Verdict |
|---|---|
| Johannesburg-Sydney about 400 ms today | Supported on the public Internet: 424 ms (WonderNetwork), 430-474 ms (RIPE Atlas). Azure private backbone: 328 ms. |
| South America about 300 ms or more today | Supported: Santiago 265-312, Sao Paulo 295-312, Buenos Aires 306-346 (public); Azure to Sao Paulo 295. Perth values are higher (310-380 ms). |
| Umoja about 110-150 ms to eastern South Africa | Plausible but unsourced; my estimate (section 3.5) is 98-114 ms Perth-Johannesburg and 146-161 ms Sydney-Johannesburg. Google publishes no latency figure. |
| Humboldt about 2028 | Consistent with installation Q4 2026 and service 2028 (single-source trade press); older sources say 2027. |
| Value of the new cables is redundancy as much as speed | Supported (sections 4 and 8). Google's own posts and the ANU paper use the resilience framing; the Humboldt post lists resilience first. |

### 3.4 What route do packets take TODAY (RIPE Atlas traceroutes, last 6 h)

Hop RTTs are cumulative minimums; hostnames from reverse DNS. [F, my measurement; full output in the scratch copy referenced in section 11]

- **Sydney (Telstra) to Johannesburg (anchor 2507):** Telstra Global Sydney 3 ms; San Jose (Equinix/GTT cr4-sjc1) **145.6 ms**; GTT Johannesburg (cr1-jhb2) **424.5 ms**; target 430 ms. The San Jose to Johannesburg leg is therefore about 279 ms. Path floor Sydney to San Jose to Johannesburg by great-circle legs: 283 ms [C]. Which ocean the second leg crosses is not shown (it could cross the Atlantic via the US east coast and Europe, or via the Pacific and Asia); [I] the latency says it is not a short path.
- **Sydney to Sao Paulo (anchor 2474):** Telstra Global to San Jose at **145.6 ms**; GTT Sao Paulo (cr1-sao6) at **299.8 ms**; target 302 ms.
- **Sydney to Santiago (anchor 3062):** Telstra Global to San Jose at **145.6 ms** (Lumen sjo1); Cirion (Santiago edge sgo1) at **265 ms**; target 265 ms.
- **Sydney to Buenos Aires (anchor 4327):** Telstra Global Palo Alto at 186.5 ms (a different US West Coast exchange); Argentine carrier at 306-330 ms; target 328 ms.
- **Perth (Telstra) to anything in South America or Africa:** Perth to Adelaide (29 ms) to Melbourne (37 ms) to Sydney (48 ms) first, then the same San Jose paths as above. Perth traffic on the Telstra network crosses Australia to Sydney and leaves from the east coast, adding about 47 ms.
- **Perth (Spintel via Megaport) to Sao Paulo and Santiago:** Perth to Los Angeles (about 216 ms, a router on AS38195 with a Los Angeles hostname), then Dallas (226 ms), Miami (255 ms), then Sao Paulo (360 ms) or Lima (315 ms) and Santiago (344-366 ms).
- **Perth to Cape Town (anchor 4099, Global Secure Layer backbone):** Perth to Muscat **97 ms** (the Oman Australia Cable), then Marseille 272-310 ms, Paris 254-283 ms, London 258-283 ms, then Cape Town **397-418 ms**. The packet goes Perth, Oman, Europe, then down the West African coast to Cape Town: about 24,600 km by great-circle legs, floor 241 ms [C], against a direct great circle of 8,697 km (floor 85 ms).
- **Perth (Spintel) to Johannesburg:** Perth to Marseille (AS38195 router with an "mrs" hostname, 192 ms), London (Liquid Telecom, 260 ms), Johannesburg (Liquid, 429-453 ms).

**Reading:** the 3x-5x penalty is not caused by physics alone but by the absence of any southern-hemisphere cable. Every packet that Australia sends to these continents today passes through the US West Coast or Europe.

### 3.5 What the new cables would change [C, with stated assumptions]

- **Humboldt (Santiago-Sydney):** about 151 ms (14,800 km cable + 144 km land + 5 ms equipment). Sydney-Buenos Aires about 173 ms and Sydney-Sao Paulo about 199 ms if carried over Chile's existing Santiago-Buenos Aires (22 ms) and Santiago-Sao Paulo (48 ms) legs. Perth-Santiago about 199 ms (adding the measured Perth-Sydney 47.5 ms). Current measured: 265-312 (Sydney-Santiago), 303 (Sydney-Sao Paulo), 306 (Sydney-Buenos Aires), 310-380 (Perth-Santiago). **Saving: about 110-160 ms, or roughly 40-50 percent.**
- **Umoja (Perth-Johannesburg):** Mandurah-Amanzimtoti great circle 7,832 km, plus 510 km to Johannesburg. At subsea route factors 1.10, 1.20 and 1.30 (the cable's length is unpublished): 98, 106 and 114 ms including 8 ms of equipment. Sydney-Johannesburg adds the measured Sydney-Perth 47.5 ms: 146, 154, 161 ms. Current measured: 430-493 (Johannesburg), 353-524 (Perth-Cape Town). **Saving: about 280-350 ms, or roughly 65-75 percent, to the eastern South African seaboard; Cape Town needs a further 1,300 km of land or coastal fiber.**

## 4. Redundancy, chokepoints and the fault record

### 4.1 Australian government and expert statements (primary)

The most thorough single source is the ANU National Security College Occasional Paper "Connected & protected: Building Australia's submarine cable resilience" (Brewster, Bashfield, Kang, Constable, Bergin; August 2026; peer-reviewed series; the NSC is a joint ANU and Australian Government initiative). [F: https://nsc.anu.edu.au/sites/default/files/2026-08/Connected_and_Protected_web.pdf ; text extracted with pdftotext]. Key statements (page numbers are approximate, read from the layout-extracted text; quotations keep the paper's wording except that British spellings in them have been converted to American, per the project rule):

- "Approximately 99 per cent of Australia's international data traffic transits submarine cables." Australia has 16 operational international cables, 17 cable landing stations, and "few alternatives" (satellite "unlikely to come close"). [p. 12-14]
- International bandwidth demand rose from 15,205 Gbit/s (2020) to **49,090 Gbit/s (2024)**, a 34 percent compound annual growth rate (source: TeleGeography). [p. 13, Figure 1]
- "Most of Australia's international cable connections are trans-Pacific"; the Indian Ocean ones "mostly connect Australia with Southeast Asia and Europe via Singapore". The Oman Australia Cable "provides Australia's first direct connection to the Middle East, diversifying routes that previously required transit through Southeast Asia." [p. 14]
- "The Australia-Singapore Cable and INDIGO cables...transit through geopolitically sensitive waters, including the Sunda Strait." [p. 16]
- "The 'Great Southern Route', which connects the Pacific and Indian oceans, transiting south of the Australian continent, is increasingly being used to bypass Southeast Asian waters. This route offers advantages in terms of geographic diversity, avoiding the congested and geopolitically sensitive South China Sea and Malacca Strait." [p. 17]
- "Threats also exist...in choke points such as the Indonesian archipelago (Sunda and Malacca straits) and the Red Sea, through which the great majority of Australia's westwards-bound data traffic flows." [p. 56]
- A one-week digital disruption would cost A$5.9 billion and a four-week one A$35 billion and some 163,000 jobs (2020 AustCyber study, 2025 dollars). [p. 12]
- Concentration: Sydney and Perth host most international landings. (Another source in my first search put the Sydney share at 63 percent; I did not find that figure in the ANU text, so treat it as [F-snippet].)
- Antarctic cables: the Australian Antarctic Division (2021 parliamentary inquiry) and the Bureau of Meteorology asked for a feasibility study; two active proposals exist, a US NSF SMART cable (McMurdo to Sydney or Invercargill, with possible branches to Macquarie Island) and a Chilean one (Puerto Williams to King George Island, feasibility study due 2026); "Australia also has significant interests in connecting the Australian Antarctic Territory and acting as a hub to connect with Antarctic research stations operated by other countries." [p. 17-19]
- **The paper does not mention South America, Africa, Humboldt or Umoja's value to Australia as destinations**; it lists Umoja only in the table of planned cables (2027). It frames the value as route diversity and hub status. [F: grep of the full text]

### 4.2 The record of faults relevant to Australia and South Africa

| Date | Event | Effect | Source |
|---|---|---|---|
| 2006 | Taiwan earthquake severed multiple cables | Reportedly disrupted 90 percent of Internet traffic around Asia (Luzon Strait region) | ANU paper p. 46 [F] |
| 2011 | Japan earthquake | 4 of 20 cables to Japan ruptured | ANU paper [F] |
| 2021 | Maersk Surabaya's dragged anchor severed the ASC at Perth | Legal action | ANU paper [F] |
| 14 Mar 2024 | Suspected underwater rockslide off Cote d'Ivoire cut WACS, SAT-3, MainOne and ACE | 13 countries affected incl. South Africa (Vodacom disrupted 10:30-16:00 UTC); Ghana's regulator reported 90-100 percent capacity loss; Microsoft reported degraded Azure South Africa regions and said Red Sea cuts were simultaneously reducing East Coast capacity | [F: https://blog.cloudflare.com/undersea-cable-failures-cause-internet-disruptions-across-africa-march-14-2024 ; F-snippet: Internet Society and Microsoft notices] |
| 24 Feb 2024 | Anchor of the attacked ship Rubymar probably cut Seacom, AAE-1 and EIG in the Red Sea | About 25 percent of Asia-Europe traffic by HGC's estimate; East Africa affected | [F-snippet: https://techblog.comsoc.org/?p=1071883 and others] |
| 6 Sep 2025 | Multiple cables cut near Jeddah incl. SMW4 and IMEWE | Azure warned of added latency for traffic through the Middle East; Cloudflare reported up to 30 percent delay India-Europe | [F-snippet: https://www.theregister.com/2025/09/07/asia_tech_news_roundup/ ; telecomreview] |
| 2025 | Two Vocus cables off Western Australia cut by a suspected anchor in cyclonic weather | | ANU paper p. 56 [F] |
| **8 Aug 2026** | **INDIGO-West (Perth-Singapore) hard down with a shunt fault; INDIGO-Central (Perth-Sydney) shunt fault straight after; both about 47.6 km offshore inside Perth's Cable Protection Zone; an unidentified vessel crossed the cable corridor; Australian Federal Police assessed a crime report** | Australian users saw minimal disruption but Perth-Singapore RTT rose from about 46 ms to over 120 ms; repair ship expected 30 Aug | [F: https://ipregistry.co/blog/perth-indigo-cable-faults ; F-snippet corroboration: submarinenetworks.com] |
| **4 Sep 2026** | **Australia-Singapore Cable fully severed in Indonesian waters between Anyer and Singapore (about 615 km from Singapore per Vocus, 18 Sep update); repairs delayed by Indonesian permits** | Combined with INDIGO West: about 100 Tbit/s of direct bandwidth out of Western Australia removed; 100 percent of direct low-latency Perth-Singapore paths eliminated; Melbourne-Singapore traffic detoured through the US, Japan and Hong Kong at about 400 ms; some traffic went overland across the Nullarbor | [F: https://www.lightreading.com/cable-technology/asc-cable-break-disrupts-key-australia-singapore-route ; https://www.itnews.com.au/news/vocus-hit-by-australia-singapore-cable-break-628720 (its "6 September" is a date mismatch; 4 Sep was a Friday and matches Light Reading and the analysis pieces) ; F: https://www.submarinenetworks.com/en/nv/insights/a-deep-dive-analysis-of-the-perth–singapore-subsea-outages (this piece did not mention the Oman Australia Cable or any African route as a contingency)] |

**Live check on 4 Oct 2026 (my measurement, RIPE Atlas, last 24 h):** from Perth to three Singapore anchors, the Vocus-network probe measured 53 ms, the Telstra-network probe 192, 276 and 305 ms, the Spintel probe 126, 311 and 312 ms; Sydney (Telstra) to Singapore measured 145, 221 and 260 ms. Before the faults the same Perth-Singapore RTT was about 46-60 ms. [F measurement; the link between these figures and the faults is [I]; I did not verify that the faults remain unrepaired on 4 Oct.]

### 4.3 Why a southern path matters (what the record shows)

- Australia's westward traffic depends on two narrow corridors: the Indonesian straits to Singapore, and from there the Red Sea to Europe. The August-September 2026 events show that two Perth-Singapore cables plus the Australia-Singapore Cable can be out within four weeks.
- The Oman Australia Cable (2022) was built to avoid Southeast Asia and Perth traffic to Europe now partly uses it (my traceroute: Perth to Muscat 97 ms), but it then still crosses the Arabian Sea and Mediterranean corridor.
- **Umoja gives Perth a route to Africa's Indian Ocean coast, from which Africa's Atlantic cables (WACS, Equiano, SACS to Brazil) offer a westward onward path that avoids both Singapore and the Red Sea.** [I; Google's posts say "new route distinct from existing connectivity routes".] South Africa's own resilience case is stronger: in March 2024 its West Coast cables failed while the East Coast was already degraded by the Red Sea cuts ("impacting all Africa capacity", Microsoft).
- **Humboldt gives Australia and Chile a route that does not touch the US**; Chile's current international links run through Panama and the US West Coast (Curie: Valparaiso-Panama-Los Angeles; SAm-1; Mistral). [F: TeleGeography; F-snippet for the rationale]
- Counter-evidence: both new cables are Google's. The Humboldt and Umoja value to Australian users is a side effect; the primary beneficiary is Google's own cross-region network. [I]

## 5. Who actually generates cross-hemisphere traffic

### 5.1 Mining remote operations are domestic, not cross-hemisphere [F / F-snippet]

- Rio Tinto's Perth Operations Center (next to Perth airport) remotely runs Pilbara mines, rail and ports 1,500 km away; it has about 200 controllers and schedulers and over 230 planning and support staff, connected "via a series of fiber optic cables". Nothing found says it runs sites outside Australia. [F-snippet: https://www.businessnews.com.au/node/81645 ; https://www.steelorbis.com/steel-news/latest-news/rio-tinto-launches-its-new-operations-center-in-perth-539860.htm]
- BHP's Perth Integrated Remote Operations Center (since late 2012) runs most of the Western Australian iron ore operations 24/7: hubs, more than 1,000 km of rail and Port Hedland. [F-snippet: https://www.bhp.com/news/media-center/releases/2023/01/celebrating-10-years-of-remote-operations (page itself returned 403)]
- BHP's Chilean copper mines (Escondida, Spence) are run from **BHP Copper Advanced Services in Santiago** (US 48.3 million, over 230 people, 5.4 TB per day, a subsea link from Antofagasta to Santiago; inaugurated 15 Oct 2024, original center 2018). [F: https://im-mining.com/?p=105670] The page I read says nothing about any connection to Perth. Anglo American's first global Integrated Remote Operations Center runs Los Bronces from Santiago (more than 100 staff, 700 cameras). [F-snippet: https://im-mining.com/?p=75231]
- **Result: no evidence that any Perth-based center supports Chile or South Africa operations.** Teleoperation needs round-trips of tens of milliseconds; 265-500 ms rules out cross-hemisphere control loops regardless of cable. [I]
- Volume: the Santiago center's 5.4 TB per day is 0.50 Gbit/s on average, which is 0.001 percent of Australia's 2024 international bandwidth, and it never leaves Chile. [C]

### 5.2 Corporate and finance links: real, but ordinary

- **Gold Fields** (head office Johannesburg; regional offices Perth, Accra, Lima, Santiago; mines in South Africa, Ghana, Australia (four in Western Australia, about 1,600 staff), Peru, Chile (Salares Norte)). [F-snippet: https://altss.com/profile/gold-fields.md and search summary] **South32** (head office Perth; Hillside Aluminium and South Africa Manganese in South Africa; Brazil Alumina; a 45 percent stake in Sierra Gorda, Chile; Cerro Matoso, Colombia; secondary JSE listing per a JSE notice). [F-snippet: https://en.wikipedia.com/wiki/South32 ; https://senspdf.jse.co.za/documents/SENS_20211021_S452702.pdf] These are concrete cases of management links spanning Perth, Johannesburg and Santiago. Volumes of ERP, e-mail and video are not published and are small against SKA flows. [I]
- Australian mining capital in Africa: "more than 170 Australian companies...in 35 African countries" with investment quoted as more than A$30 billion in an older speech and more than A$60 billion (currency unclear) in 2024-2026 reports; Africa Down Under is held in Perth each year. [F-snippet: https://www.miningweekly.com/article/australian-mining-companies-investment-into-africa-reaches-60bn-2024-09-05 (403 on fetch); DFAT minister's speech page timed out] Most of that investment is in West Africa and Southern Africa, not specifically in South Africa. [I]
- Australia-South Africa goods trade: US 2.27 billion (2024; South Africa exports US 1.06 billion, imports US 1.21 billion), mainly alumina (artificial corundum US 656 million) and vehicles. [F-snippet via tradingeconomics-type summary] In 2017 trade was A$3.6 billion (A$2.0 billion exports, 1.8 billion imports); South Africa ranked 24th among Australia's export destinations. [F: https://en.wikipedia.org/wiki/Australia%E2%80%93South_Africa_relations] About 189,000-194,000 South African-born residents in Australia. [F: same]
- Australia-South America trade (from the earlier log, not re-verified by me): Chile about A$1.4 billion, Argentina about A$1.7 billion (2024 goods and services A$800 million exports plus A$893 million imports per a DFAT snippet), Brazil about US 1.7 billion. DFAT country-brief pages and fact-sheet PDFs timed out on every fetch, so I could not update these. [U for 2024-25 figures]
- Finance: ASX-JSE ties are secondary listings of mining juniors (Southern Palladium, Orion Minerals, Firestone) and South32; ASX-listed Latin America lithium and copper juniors exist (Latin Resources, Solis Minerals and others). I found **no evidence of a direct ASX-B3, ASX-JSE or ASX-BCS market-data link or latency-sensitive trading flow**. Trading flows to Chile and South Africa travel through the usual hubs. [F-snippet; absence is [U]]
- Mining services: about 80 Australian firms supply Escondida and about 60 METS firms export to Chile (from the earlier log). Services trade is not communications-intensive. [I]

### 5.3 The SKA: the one quantified Australia-South Africa data flow [F]

- SKA-Low (Western Australia, Murchison) sends about 9 Tbit/s to the Perth Science Processing Center over 820 km of optical transport; SKA-Mid (Karoo) sends about 20 Tbit/s to Cape Town over 737 km. Planned export of about 300 PB per year per telescope ("130 Pflops" each) to SKA Regional Centers at 100 Gbit/s per telescope in the full design. [F: https://www.amlight.net/wp-content/uploads/2025/05/SA3CC_May25_v3-Richard-Hughes-Jones.pdf (Richard Hughes-Jones for the SKA-NREN Forum, 7 May 2025)]
- Planned data paths today: from Perth, "five flows on the submarine cable from Perth to Singapore", then the academic network; "two 20 Gbit/s flows would be carried to London to reach SRCs in Europe and South Africa". From Cape Town, five flows go on the cable to London, and "different submarine cables" reach India and Australia. **So today's plan carries Australia-South Africa SKA data via London.** [F: SKA-NREN Forum Meeting 6, 26 Feb 2024, https://indico.skatelescope.org/event/1143/contributions/10301/attachments/9444/16327/SKA-NREN%20Forum%20ReportTechWG_26Feb24_v1.pdf]
- Forecast: "Expect significant traffic between AU & ZA"; "ODPs to Europe about 40 percent (19 percent to the UK)"; the AA* (end-2027) scenario has "Data rate out of AU about 60 Gbit/s (inter-continental)"; the full design has "almost 100 Gbit/s into UK, ZA, AU". The working group tunes data transfer nodes for RTT of about 300 ms, and measured Europe-to-Australia RTT is 262 ms. Costs: a 100 Gbit/s primary circuit is USD 1.7-2.3 million per year (10-15 year IRU, 2020 prices). [F: same document]
- Scale: a 20 Gbit/s flow is 0.04 percent and a 100 Gbit/s flow 0.2 percent of Australia's 2024 international bandwidth. [C] The SKA's total archive flow is about 700 PB per year, an average of 178 Gbit/s across all centers. [C]
- Lifetime: the SKA is a roughly 50-year facility (not in the sources; [I]); it is a 2020s-2070s driver, not a durable one by itself.

### 5.4 Astronomy beyond the SKA [F / F-snippet]

- Australia has a 10-year ESO strategic partnership (2017) and a roughly 10 percent share of the Giant Magellan Telescope at Las Campanas. [F-snippet: ANU and Astronomy Australia pages] Chile's research network REUNA carries ALMA (1 Gbit/s Array Operations Site to Calama to Antofagasta, 100 Gbit/s Antofagasta-Santiago), 100 Gbit/s of Vera Rubin traffic from Argentina and 200 Gbit/s of RedCLARA traffic; its slide on Humboldt reads "14,810 km, USD 395 mill CAPEX", and a trade report says the scientific community "emerged as the first party interested" in the Chile-Australia cable. [F: REUNA PDF above; F-snippet: bnamericas.com (403 on fetch)]
- The data from Chilean observatories flows to the US and Europe (AmLight, BELLA), not to Australia; Australian astronomers get access through partner archives. I found no source describing an Australia-to-Chile data stream. [I; absence [U]]

### 5.5 Hyperscaler backbones [F / I]

- Google, Microsoft and Meta decide most new cable routes. Humboldt (Google 50 percent, built to link Google's Santiago region and data center to Asia-Pacific), Umoja (lands in South Africa "including the Google Cloud region" and Perth), Halaihai, Honomoana and Waterworth are hyperscaler projects; the ANU paper notes "technology companies now driving infrastructure development based on their respective data center strategies" and that hyperscalers' investments reflect "Australia's emerging role as a regional data hub". SUBCO's own APX East release says hyperscalers and neoclouds are looking to deploy 3 GW of AI factories in Australia by 2028, needing 75-150 Tbit/s of international capacity. [F; F-snippet]
- This is the demand that justifies cable-sized capacity: Humboldt's stated 144 Tbit/s is 2.9 times Australia's entire 2024 international bandwidth. It is a private cloud and AI backbone need (replication, training data, region failover), not an Australia-Chile trade need. [I, C]

## 6. Time zones and overlap of business hours [C]

Offsets use the IANA tz database (Python zoneinfo). Chile is on UTC-4 in southern winter and UTC-3 in southern summer; Argentina and Brazil (Sao Paulo) UTC-3 all year; Johannesburg UTC+2; Perth UTC+8 all year; Sydney UTC+10, or UTC+11 in southern summer.

| Pair | UTC offset difference | Overlap of 09:00-17:00 local | 08:00-18:00 | 07:00-19:00 |
|---|---|---|---|---|
| Perth - Johannesburg | 6 h | **2 h** (Perth 15:00-17:00 = Johannesburg 09:00-11:00) | 4 h | 6 h |
| Sydney - Johannesburg | 8 h (winter), 9 h (summer) | 0 h | 2 h (winter), 1 h (summer) | 4 h, 3 h |
| Perth - Santiago | 12 h (Chile winter), 11 h (summer) | 0 h | 0 h | 0-1 h |
| Perth - Buenos Aires / Sao Paulo | 11 h | 0 h | 0 h | 1 h |
| Sydney - Santiago | 14 h (summer), 14 h (winter) | 0 h | 0 h | 2 h |
| Sydney - Buenos Aires / Sao Paulo | 13 h (winter), 14 h (summer) | 0 h | 0 h | 1-2 h |

Reading: Sydney 09:00 is 19:00 the previous day in Santiago (southern summer). Live collaboration between Australia and South America is essentially impossible within normal hours; it works as a relay (end-of-day handover). Perth and South Africa share a two-hour window. [C] This limits demand for real-time voice and video on the South America axis and supports asynchronous bulk data (replication, archives) as the main flow. [I]

## 7. Antarctic and Southern Ocean connectivity, ground stations, and the Punta Arenas plus Western Australia pair

- **No cable reaches Antarctica.** Proposals: Chile's Drake Passage cable (feasibility study finalized August 2026, started February 2025; base route about 1,600 km, US 370 million, Punta Arenas and Puerto Williams to three Chilean bases; full route about 4,100 km, US 620 million, nine landings connecting Chile, Argentina, Brazil, US and UK bases; about eight years of work if approved; needs international coordination, financing and political will); NSF SMART cable (McMurdo to Invercargill or Sydney); the 2021 Australian proposal (Tasmania to Mawson, Davis, Casey, Macquarie; preliminary). [F: https://maritime-executive.com/article/antarctica-submarine-cable-project-confirmed-feasible ; ANU paper p. 18-19]
- **Today's Antarctic links are satellite and tiny.** Wikipedia (compilation) says "The Australian Stations each have a satellite data connection, currently contracted to Speedcast. This provides each station with a 9 Mbps symmetric connection"; McMurdo has a shared 17 Mbps connection (Starlink testing from Sept 2022); Scott Base uses Spark NZ and Horizons 3E, with Starlink trials; South Pole uses TDRS-F1, GOES and Iridium; SANAE IV has a permanent satellite link to SANAP headquarters in Cape Town with "near-broadband" Internet. [F: https://en.wikipedia.org/wiki/Telecommunications_in_Antarctica ; F-snippet: SANAE page]. Four Australian stations (three on the continent plus Macquarie Island, if all are on the same contract) at 9 Mbit/s each total 0.036 Gbit/s. [C] That is about 2,800 times smaller than one 100 Gbit/s SKA flow.
- **Starlink:** Antarctica has no gateway; traffic relies on laser inter-satellite links to ground stations elsewhere; the search summaries I read did not name which countries host the gateways serving Antarctica. [F-snippet: https://interestingengineering.com/innovation/starlink-arrives-antarctica-high-speed-internet ; the earlier log's gizmodo claim about a Sydney ground station remains [S]]
- **Geostationary satellites cannot cover latitudes beyond about 81 degrees (NSF DTS report, per the earlier log).** [F-snippet]
- **"Punta Arenas plus Western Australia is an explicit satellite-ground-station pair": VERIFIED as a marketing statement by SSC Space.** The Punta Arenas station page (opened) says: "When paired with SSC Space's Western Australia facility, the station provides 'unmatched coverage opportunities' for polar-orbiting missions, reducing latency through dual-site support"; it was established in 2012, at latitude -52.93, longitude -70.85, 28 km north of Punta Arenas, with 7.3-11.5 m antennas in S, X and Ka bands and fiber from two providers. SSC's station list (opened) shows the Western Australia Space Center at latitude -29.05, longitude 115.35, Santiago (-33.15, -70.66), partner stations at O'Higgins (Antarctica) and **Hartebeesthoek (South Africa)**, plus Esrange, Inuvik, North Pole (Alaska), Siracha, South Point (Hawaii), Clewiston, Irbene and Stockholm. [F: https://sscspace.com/services/satellite-ground-stations/our-stations/punta-arenas-station/ ; https://sscspace.com/services/satellite-ground-stations/our-stations/] The longitude gap between the two sites is 186 degrees, which is near-antipodal, so a polar orbit passes a station at least once per orbit pair. [C/I] It is a commercial pairing for polar-satellite downlink, not an Antarctic-program link. KSAT and AWS also operate at Punta Arenas; ESA's deep-space antennas include New Norcia (Western Australia) and Malargue (Argentina); NASA's DSN has Canberra (earlier log, [S]).
- None of these satellite or station facts requires an Australia-South America or Australia-South Africa terrestrial or cable link to function; they are geography-driven (high-latitude sites) and each station backhauls to its own home country.

## 8. Judgement

### 8.1 Does trade, mining or finance generate a need beyond the generic Internet?

**No, not on the evidence found.**
- Trade values are small (Chile about A$1.4 billion; South Africa about US 2.3 billion; Brazil about US 1.7 billion) against the 49,090 Gbit/s Australian international bandwidth, and goods trade needs documents and tracking, not low latency.
- Mining operations (the largest economic activity linking Perth, Santiago and Johannesburg) are run domestically; the cross-hemisphere traffic is corporate IT and video among management centers. Gold Fields and South32 are real multi-hemisphere firms but their bandwidth is small and their data goes through the same public hubs and clouds as everyone's.
- Finance: no direct market link found; listings are secondary.
- Where a latency penalty matters (real-time trading, teleoperation, voice) the time-zone gap or physics already prevents the use case on the South America axis. The only business-hours overlap is Perth-South Africa (2 h).

### 8.2 What does generate measurable demand

1. **Hyperscaler and AI backbone traffic** (cloud region replication; Google's own cables) is the direct reason Humboldt and Umoja exist; it is very large in capacity terms but is a private, corporate need. [I]
2. **The SKA** is the only quantified, funded, long-lived Australia-South Africa data flow (tens of Gbit/s to about 100 Gbit/s; expected "significant traffic between AU & ZA"; today routed via London).
3. **Route resilience:** Perth currently depends on two narrow westward corridors; the 2026 faults prove that. The southern routes (Umoja, Humboldt) are the only route diversity not through the Indonesian straits and the Red Sea.
4. **Multi-hemisphere resource corporate management** (Gold Fields, South32, Anglo American): present but small.
5. **Science and Antarctic programs:** real but small (9 Mbit/s stations; a few Gbit/s for astronomy).

### 8.3 Ranking against the earlier agents' reasons for an Australia-South America-South Africa link

This ranking is by strength of evidence that the reason gives Australia a durable benefit from linking with these two continents specifically, scoring the earlier reasons as reported in `Open_Research_Topics.md` section 5 (I did not re-verify them).

| Rank | Reason | Evidence quality | Durable for an 800-year setting? |
|---|---|---|---|
| 1 | Search and rescue and gateway logistics (five states share Antarctic SAR; five gateway cities) | Strong (institutional, COMNAP, AMSA) | Yes |
| 2 | Great-circle geometry (Sydney to Santiago via 62 S; Perth to Buenos Aires near the Pole) | Strong (computed; confirmed by my physics floors) | Yes: the geometry never changes; the northern detour cost (150-200 ms) is permanent without a southern path |
| 3 | **Chokepoint-avoiding redundancy (this report)** | **Strong, with a live 2026 case** | Mostly yes: Indonesian straits and the Red Sea are geological and geopolitical constants; the specific faults are not |
| 4 | **Hyperscaler backbone demand (this report)** | Strong for today, weak for the long run | Contingent on the cloud economy |
| 5 | SKA (Perth and Cape Town centers) | Strong (quantified) | Weak: finite instrument life, though the setting could keep it |
| 6 | Weather-data scarcity and the Southern Annular Mode | Moderate | Yes |
| 7 | HF space-weather forecasting | Moderate | Yes |
| 8 | ESO and GMT astronomy partnerships | Moderate, small data | Moderate |
| 9 | Mining corporate management (Gold Fields, South32) | Moderate, small volume | Weak |
| 10 | Trade, finance, diaspora | Weak | Weak |

This report supports reasons 2 and 3 numerically, adds 4, and finds nothing that lifts 9 or 10.

### 8.4 One-sentence reading for the worldbuilding [I]

Australia does not need South America or South Africa as trading partners in order to want links to them; it needs two southern routes that do not run through the Indonesian straits and the Red Sea, and those routes happen to land on the two nearest southern continents, with SAR, gateway logistics and Antarctic geometry (and for South Africa the SKA) giving the link its institutional reasons.

## 9. Open gaps

- No published latency figures from Google for Humboldt or Umoja; Umoja's route length and capacity unpublished.
- No Chile row in Azure's latency matrix (Chile Central is new); no Perth Azure region. Cloudflare Radar was not queried.
- DFAT pages and fact-sheet PDFs (country briefs, goods and services trade 2024-25) could not be fetched (timeouts; curl returned nothing). Trade figures for 2024-25 are not updated.
- TeleGeography has no "Humboldt" record; I could not confirm how it maps to Halaihai and Honomoana. TeleGeography's APX East record carries what looks like a "Los Angeles, Chile" landing error (not reported to them).
- Whether INDIGO-West, INDIGO-Central and ASC were repaired by 4 Oct 2026 was not established; the live RIPE numbers fit continued degradation but I did not rule out routing policy.
- The Atlantic leg of the Sydney to San Jose to Johannesburg path (and the Perth to Marseille leg) cannot be seen in the hop data.
- No data on actual traffic volumes between Australia and South America or South Africa as a share of Australia's total (TeleGeography's inter-regional tables are paywalled).
- Cross-hemisphere mining IT volumes (Gold Fields, South32) are not public.
- Starlink gateway countries serving Antarctica not found; Iridium gateway locations not researched; Hartebeesthoek's role beyond the SSC partner listing not researched.
- ESO and GMT data flows to Australia not found; ALMA and Rubin figures come from a 2022 slide.
- The SKA slide text "correlators were moved to Cape Town for SKA Low, Perth for SKA Mid" (SA3CC May 2025) conflicts with the same deck's other pages (Karoo to Cape Town, Murchison to Perth); I did not use it.

## 10. Calculations: what was done (scripts in section 11)

1. Fiber speed and RTT floors: `physics.py` (haversine; v = c / 1.4682).
2. Humboldt and Umoja estimates: `est.py` (route factors 1.10-1.30, +8 ms equipment for Umoja, +5 ms for Humboldt, measured Perth-Sydney 47.5 ms).
3. Scale comparisons: 5.4 TB per day = 5.4e12 x 8 / 86,400 = 0.50 Gbit/s; 20 and 100 Gbit/s over 49,090 Gbit/s; 700 PB per year = 178 Gbit/s; 144 Tbit/s over 49.09 Tbit/s = 2.9.
4. Business-hours overlap: `tz.py` (IANA time zones, three sample dates).
5. Live latency: `atlas2.py` (median of per-sample minimum RTT, 24 h) and `atlas3.py` (latest traceroute in the last 6 h, reverse DNS).

## 11. Scripts and raw output (scratch files at /tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/462f6b67-5cf4-4e6a-9bd4-27aaf5e5b77e/scratchpad/comms_demand/ ; text reproduced below)


### 11.x Script: physics.py

```python
from math import radians,sin,cos,asin,sqrt
C=299792.458; N=1.4682   # SMF-28 group index at 1550 nm (Corning data sheet), v = c/N
V=C/N
def gc(a,b):
    la1,lo1=map(radians,a); la2,lo2=map(radians,b)
    h=sin((la2-la1)/2)**2+cos(la1)*cos(la2)*sin((lo2-lo1)/2)**2
    return 2*6371.0088*asin(sqrt(h))
P={'Sydney':(-33.8688,151.2093),'Perth':(-31.9505,115.8605),'Johannesburg':(-26.2041,28.0473),'Cape Town':(-33.9249,18.4241),'Durban':(-29.8587,31.0218),
'Santiago':(-33.4489,-70.6693),'Valparaiso':(-33.0472,-71.6127),'Sao Paulo':(-23.5505,-46.6333),'Buenos Aires':(-34.6037,-58.3816),'San Jose CA':(37.3382,-121.8863),
'Los Angeles':(34.0522,-118.2437),'Singapore':(1.3521,103.8198),'London':(51.5074,-0.1278),'Muscat':(23.588,58.3829),'Mandurah':(-32.5269,115.7217),'Papeete':(-17.5516,-149.5585),
'Fortaleza':(-3.7319,-38.5267),'Marseille':(43.2965,5.3698),'Mauritius':(-20.1609,57.5012),'Melbourne':(-37.8136,144.9631),'Auckland':(-36.8485,174.7633),'Hobart':(-42.8821,147.3272),'Punta Arenas':(-53.1638,-70.9171),'Mumbai':(19.076,72.8777)}
def rtt(d): return 2*d/V*1000
print(f"v in fiber = {V:.0f} km/s ; RTT per 100 km of fiber = {rtt(100):.3f} ms ; c vacuum RTT/100km = {2*100/C*1000:.3f}")
pairs=[('Sydney','Johannesburg'),('Sydney','Cape Town'),('Perth','Johannesburg'),('Perth','Cape Town'),('Perth','Durban'),('Mandurah','Durban'),
('Sydney','Santiago'),('Sydney','Valparaiso'),('Sydney','Sao Paulo'),('Sydney','Buenos Aires'),('Perth','Santiago'),('Perth','Sao Paulo'),('Perth','Buenos Aires'),
('Sydney','San Jose CA'),('San Jose CA','Johannesburg'),('San Jose CA','Sao Paulo'),('San Jose CA','Santiago'),('Sydney','Los Angeles'),
('Perth','Muscat'),('Muscat','Marseille'),('Marseille','London'),('London','Cape Town'),('Perth','Singapore'),('Sydney','Singapore'),
('Cape Town','Buenos Aires'),('Cape Town','Sao Paulo'),('Cape Town','Santiago'),('Johannesburg','Sao Paulo'),('Sydney','Papeete'),('Papeete','Valparaiso'),('Perth','Mauritius'),('Mauritius','Durban'),('Sydney','London'),('Sydney','Perth'),('Hobart','Punta Arenas'),('Perth','Mumbai')]
print("pair, great-circle km, RTT floor at GC (ms), RTT at x1.2 route, x1.4 route")
for a,b in pairs:
    d=gc(P[a],P[b]); print(f"{a:13s}-{b:13s} {d:8.0f} km  {rtt(d):6.1f}  {rtt(d*1.2):6.1f}  {rtt(d*1.4):6.1f}")
print()
# Humboldt 14,800 km cable
for L in (14800,):
    print('Humboldt cable',L,'km -> fiber RTT floor',round(rtt(L),1),'ms; (+ ~10-20% for repeaters/terminal equipment: unknown) ')
# routes
def chain(*cities,mult=1.0):
    d=sum(gc(P[a],P[b]) for a,b in zip(cities,cities[1:]))
    return d,rtt(d*mult)
for name,ch in {'Sydney-SJC-Johannesburg (GC legs)':('Sydney','San Jose CA','Johannesburg'),'Sydney-SJC-Sao Paulo':('Sydney','San Jose CA','Sao Paulo'),'Sydney-SJC-Santiago':('Sydney','San Jose CA','Santiago'),
 'Perth-Muscat-Marseille-London-Cape Town':('Perth','Muscat','Marseille','London','Cape Town'),'Perth-Singapore-Mumbai-Marseille-London-Cape Town':('Perth','Singapore','Mumbai','Marseille','London','Cape Town')}.items():
    d,r=chain(*ch); print(f"{name}: GC-leg sum {d:.0f} km, RTT floor {r:.0f} ms")
```

### 11.x Script: est.py

```python
exec(open('physics.py').read().split("print(f\"v in fiber")[0])
P['Amanzimtoti']=(-30.0527,30.8761)
def r(d): return 2*d/V*1000
print("Umoja estimate (inference; Umoja's route length is not published)")
gc_sub=gc(P['Mandurah'],P['Amanzimtoti']); print('Mandurah-Amanzimtoti GC',round(gc_sub),'km')
gc_land=gc(P['Amanzimtoti'],P['Johannesburg']); print('Amanzimtoti-Johannesburg GC',round(gc_land),'km')
for f_sub in (1.10,1.20,1.30):
    for f_land in (1.2,):
        d=gc_sub*f_sub+gc_land*f_land
        base=r(d)
        print(f" subsea factor {f_sub}: cable+land {d:.0f} km -> fiber RTT {base:.0f} ms ; with +8 ms equipment/switching {base+8:.0f} ms ; Perth<->Joburg; Sydney<->Joburg add Perth-Sydney measured 47.5 ms RTT -> {base+8+47.5:.0f}")
print()
print("Humboldt estimate")
L=14800
for eq in (0,5,10):
    base=r(L)+eq
    print(f" cable 14800 km RTT floor {r(L):.0f} ms + {eq} ms equipment => Valparaiso-Sydney {base:.0f} ms")
# Santiago-Sydney incl Santiago-Valparaiso 120 km
base=r(14800+120*1.2)+5
print('Santiago<->Sydney ~',round(base),'ms (14,800 km + 144 km land + 5 ms equip)')
for city,ms in [('Buenos Aires',22),('Sao Paulo',48)]:
    print(f"Sydney<->{city}: {base:.0f}+ measured Santiago<->{city} {ms} = {base+ms:.0f} ms (if Humboldt then Chile backbone)")
print('Perth<->Santiago via Sydney: ',round(base+47.5),'ms')
```

### 11.x Script: tz.py

```python
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta, timezone
zones={'Perth':'Australia/Perth','Sydney':'Australia/Sydney','Johannesburg':'Africa/Johannesburg','Cape Town':'Africa/Johannesburg','Santiago':'America/Santiago','Buenos Aires':'America/Argentina/Buenos_Aires','Sao Paulo':'America/Sao_Paulo'}
def offs(city,date):
    z=ZoneInfo(zones[city]); return z.utcoffset(datetime(date.year,date.month,date.day,12,tzinfo=z)).total_seconds()/3600
def overlap(a,b,date,s=9,e=17):
    oa,ob=offs(a,date),offs(b,date)
    # utc interval of local business hours
    ia=(s-oa,e-oa); ib=(s-ob,e-ob)
    # consider day shifts of 24h
    best=0
    for k in (-24,0,24):
        lo=max(ia[0],ib[0]+k); hi=min(ia[1],ib[1]+k); best=max(best,hi-lo)
    return oa,ob,best
import datetime as dt
for label,date in [('15 Jan 2027 (Southern summer)',dt.date(2027,1,15)),('15 Jul 2026 (Southern winter)',dt.date(2026,7,15)),('15 Oct 2026 (now)',dt.date(2026,10,15))]:
    print('==',label)
    for a in ('Perth','Sydney'):
        for b in ('Johannesburg','Santiago','Buenos Aires','Sao Paulo'):
            oa,ob,h=overlap(a,b,date); h2=overlap(a,b,date,8,18)[2]; h3=overlap(a,b,date,7,19)[2]
            print(f"{a:7s} UTC{oa:+.0f}  {b:13s} UTC{ob:+.0f}  diff {oa-ob:+.0f} h; overlap 09-17: {max(h,0):.0f} h ; 08-18: {max(h2,0):.0f} h ; 07-19: {max(h3,0):.0f} h")
# show the overlapped window for Perth-Johannesburg and Sydney-Santiago in local times
def window(a,b,date,s=9,e=17):
    oa,ob=offs(a,date),offs(b,date)
    ia=(s-oa,e-oa)
    for k in (-24,0,24):
        ib=(s-ob+k,e-ob+k); lo=max(ia[0],ib[0]); hi=min(ia[1],ib[1])
        if hi>lo: return f"{a} {(lo+oa)%24:.0f}:00-{(hi+oa)%24:.0f}:00 = {b} {(lo+ob)%24:.0f}:00-{(hi+ob)%24:.0f}:00"
    return 'none'
for date in (dt.date(2027,1,15),dt.date(2026,7,15)):
    print(date)
    for a,b in [('Perth','Johannesburg'),('Sydney','Johannesburg'),('Perth','Santiago'),('Sydney','Santiago'),('Sydney','Buenos Aires'),('Perth','Buenos Aires')]:
        print(' ',window(a,b,date))
```

### 11.x Script: atlas2.py

```python
import json,urllib.request,time,statistics
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=90))
        except Exception as e: err=e; time.sleep(2)
    return {'err':str(err)}
targets={'Johannesburg':[2507,2220],'CapeTown':[4099,2967],'Santiago':[4687,3062,3701],'SaoPaulo':[2474],'BuenosAires':[4327,3816],'Sydney':[3744],'Perth':[3429,3886]}
sources={'Sydney-Telstra':7326,'Perth-Telstra':7262,'Perth-Vocus':7432,'Perth-Spintel':7547}
now=int(time.time()); start=now-86400
out=[]
for tn,anchors in targets.items():
    for a in anchors:
        ad=get(f'https://atlas.ripe.net/api/v2/anchors/{a}/')
        ip=ad['ip_v4']
        m=get(f'https://atlas.ripe.net/api/v2/measurements/?target_ip={ip}&type=ping&status=2&page_size=10')
        mesh=[r['id'] for r in m.get('results',[]) if 'mesh' in r.get('tags',[])]
        if not mesh: print('no mesh',tn,a); continue
        mid=mesh[0]
        for sn,p in sources.items():
            r=get(f'https://atlas.ripe.net/api/v2/measurements/{mid}/results/?probe_ids={p}&start={start}&stop={now}&format=json')
            if isinstance(r,dict): print(tn,a,sn,r); continue
            mins=[x['min'] for x in r if x.get('min',-1)>0]; avgs=[x['avg'] for x in r if x.get('avg',-1)>0]
            if mins:
                print(f"{sn:15s} -> {tn:12s} anchor {a} ({ad['city']}, AS{ad['as_v4']}) meas {mid}: n={len(mins)} median_min={statistics.median(mins):.1f} median_avg={statistics.median(avgs):.1f} p10avg={sorted(avgs)[len(avgs)//10]:.1f}")
                out.append((sn,tn,a,mid,len(mins),statistics.median(mins),statistics.median(avgs)))
            else: print(sn,tn,a,mid,'no data',len(r))
json.dump(out,open('atlas_pings.json','w'))
```

### 11.x Script: atlas3.py

```python
import json,urllib.request,time,socket,statistics,sys
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=90))
        except Exception as e: err=e; time.sleep(2)
    return {'err':str(err)}
targets={'Johannesburg':2507,'CapeTown':4099,'Santiago':3062,'SaoPaulo':2474,'BuenosAires':4327}
sources={'Sydney-Telstra':7326,'Perth-Telstra':7262,'Perth-Spintel':7547}
now=int(time.time()); start=now-6*3600
def rdns(ip):
    try: return socket.gethostbyaddr(ip)[0]
    except Exception: return ''
cache={}
for tn,a in targets.items():
    ad=get(f'https://atlas.ripe.net/api/v2/anchors/{a}/'); ip=ad['ip_v4']
    m=get(f'https://atlas.ripe.net/api/v2/measurements/?target_ip={ip}&type=traceroute&status=2&page_size=10')
    mesh=[r['id'] for r in m.get('results',[]) if 'mesh' in r.get('tags',[])]
    if not mesh: print('no tr mesh',tn); continue
    for sn,p in sources.items():
        r=get(f'https://atlas.ripe.net/api/v2/measurements/{mesh[0]}/results/?probe_ids={p}&start={start}&stop={now}&format=json')
        if not isinstance(r,list) or not r: print(sn,tn,'none',str(r)[:100]); continue
        x=r[-1]
        print(f"=== {sn} -> {tn} anchor {a} AS{ad['as_v4']} meas {mesh[0]} ts {x['timestamp']} proto {x.get('proto')}")
        for h in x['result']:
            rt=[q for q in h.get('result',[]) if 'from' in q]
            if not rt: print(f"  {h['hop']:2d} *"); continue
            ip_=rt[0]['from']; rtts=[q['rtt'] for q in rt if 'rtt' in q]
            if ip_ not in cache: cache[ip_]=rdns(ip_)
            print(f"  {h['hop']:2d} {ip_:40s} {min(rtts) if rtts else 0:7.1f} ms  {cache[ip_]}")
```

### 11.x Script: atlas4.py

```python
import json,urllib.request,time,statistics
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=90))
        except Exception as e: err=e; time.sleep(2)
    return {'err':str(err)}
targets={'Sydney':3744,'Perth':3429,'Johannesburg':2507,'CapeTown':4099,'SaoPaulo':2474,'Santiago':3062,'BuenosAires':4327}
sources={'CapeTown-Atomic(7463)':7463,'CapeTown-xneelo(7062)':7062,'JNB-DigiCert(6993)':6993,'Santiago-Databyte(7747)':7747,'Santiago-NetActuate(6801)':6801,'SaoPaulo-DigiCert(6977)':6977,'BuenosAires-CABASE(7578)':7578}
now=int(time.time()); start=now-86400
for tn,a in targets.items():
    ad=get(f'https://atlas.ripe.net/api/v2/anchors/{a}/'); ip=ad['ip_v4']
    m=get(f'https://atlas.ripe.net/api/v2/measurements/?target_ip={ip}&type=ping&status=2&page_size=10')
    mesh=[r['id'] for r in m.get('results',[]) if 'mesh' in r.get('tags',[])]
    for sn,p in sources.items():
        r=get(f'https://atlas.ripe.net/api/v2/measurements/{mesh[0]}/results/?probe_ids={p}&start={start}&stop={now}&format=json')
        if not isinstance(r,list): print(sn,tn,str(r)[:80]); continue
        mins=[x['min'] for x in r if x.get('min',-1)>0]
        if mins: print(f"{sn:26s} -> {tn:13s} (anchor {a}) n={len(mins)} median_min={statistics.median(mins):.1f}")
```

### 11.x Script: atlas5.py

```python
import json,urllib.request,time,statistics
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=90))
        except Exception as e: err=e; time.sleep(2)
    return {'err':str(err)}
d=get('https://atlas.ripe.net/api/v2/anchors/?country=SG&page_size=100&fields=id,city,fqdn,is_disabled,probe')
sg=[a for a in d['results'] if not a['is_disabled']][:6]
print([(a['id'],a['fqdn']) for a in sg])
d2=get('https://atlas.ripe.net/api/v2/anchors/?country=OM&page_size=20&fields=id,city,fqdn,is_disabled,probe'); print([(a['id'],a['fqdn'],a['is_disabled']) for a in d2.get('results',[])])
d3=get('https://atlas.ripe.net/api/v2/anchors/?country=MU&page_size=20&fields=id,city,fqdn,is_disabled,probe'); print([(a['id'],a['fqdn'],a['is_disabled']) for a in d3.get('results',[])])
now=int(time.time()); start=now-86400
srcs={'Perth-Telstra':7262,'Perth-Vocus':7432,'Perth-Spintel':7547,'Sydney-Telstra':7326}
for a in sg[:4]+[x for x in d2.get('results',[]) if not x['is_disabled']][:2]+[x for x in d3.get('results',[]) if not x['is_disabled']][:2]:
    ad=get(f"https://atlas.ripe.net/api/v2/anchors/{a['id']}/"); ip=ad['ip_v4']
    m=get(f'https://atlas.ripe.net/api/v2/measurements/?target_ip={ip}&type=ping&status=2&page_size=10')
    mesh=[r['id'] for r in m.get('results',[]) if 'mesh' in r.get('tags',[])]
    if not mesh: print('no mesh',a); continue
    for sn,p in srcs.items():
        r=get(f'https://atlas.ripe.net/api/v2/measurements/{mesh[0]}/results/?probe_ids={p}&start={start}&stop={now}&format=json')
        mins=[x['min'] for x in r if isinstance(r,list) and x.get('min',-1)>0]
        if mins: print(f"{sn:15s} -> {a['fqdn'][:34]:34s} {ad['city']:12s} median_min={statistics.median(mins):.1f} ms")
```

### 11.y Raw RIPE Atlas ping medians (atlas2.py output, 4 Oct 2026, last 24 h; format: source -> target, anchor, n samples, median of min RTT ms, median of avg RTT ms)

```
Sydney-Telstra  -> Johannesburg anchor 2507 meas 29766764 n=360 median_min=429.8 median_avg=430.0
Perth-Telstra   -> Johannesburg anchor 2507 meas 29766764 n=360 median_min=476.5 median_avg=476.6
Perth-Vocus     -> Johannesburg anchor 2507 meas 29766764 n=359 median_min=478.8 median_avg=478.8
Perth-Spintel   -> Johannesburg anchor 2507 meas 29766764 n=359 median_min=450.5 median_avg=450.6
Sydney-Telstra  -> Johannesburg anchor 2220 meas 25159223 n=360 median_min=473.9 median_avg=474.1
Perth-Telstra   -> Johannesburg anchor 2220 meas 25159223 n=360 median_min=493.2 median_avg=493.3
Perth-Vocus     -> Johannesburg anchor 2220 meas 25159223 n=359 median_min=433.8 median_avg=433.8
Perth-Spintel   -> Johannesburg anchor 2220 meas 25159223 n=360 median_min=479.0 median_avg=479.0
Sydney-Telstra  -> CapeTown     anchor 4099 meas 86150185 n=360 median_min=415.3 median_avg=415.4
Perth-Telstra   -> CapeTown     anchor 4099 meas 86150185 n=360 median_min=416.6 median_avg=416.7
Perth-Vocus     -> CapeTown     anchor 4099 meas 86150185 n=360 median_min=401.5 median_avg=401.6
Perth-Spintel   -> CapeTown     anchor 4099 meas 86150185 n=360 median_min=397.0 median_avg=397.1
Sydney-Telstra  -> CapeTown     anchor 2967 meas 35361303 n=360 median_min=474.4 median_avg=474.5
Perth-Telstra   -> CapeTown     anchor 2967 meas 35361303 n=360 median_min=524.1 median_avg=524.3
Perth-Vocus     -> CapeTown     anchor 2967 meas 35361303 n=360 median_min=468.9 median_avg=469.2
Perth-Spintel   -> CapeTown     anchor 2967 meas 35361303 n=360 median_min=353.3 median_avg=353.4
Sydney-Telstra  -> Santiago     anchor 4687 meas 169403062 n=360 median_min=311.6 median_avg=311.8
Perth-Telstra   -> Santiago     anchor 4687 meas 169403062 n=360 median_min=363.1 median_avg=363.3
Perth-Vocus     -> Santiago     anchor 4687 meas 169403062 n=360 median_min=360.7 median_avg=360.8
Perth-Spintel   -> Santiago     anchor 4687 meas 169403062 n=360 median_min=379.3 median_avg=379.4
Sydney-Telstra  -> Santiago     anchor 3062 meas 43406702 n=360 median_min=265.0 median_avg=265.1
Perth-Telstra   -> Santiago     anchor 3062 meas 43406702 n=360 median_min=310.2 median_avg=310.3
Perth-Vocus     -> Santiago     anchor 3062 meas 43406702 n=360 median_min=352.8 median_avg=352.9
Perth-Spintel   -> Santiago     anchor 3062 meas 43406702 n=360 median_min=367.8 median_avg=367.9
Sydney-Telstra  -> Santiago     anchor 3701 meas 66410849 n=360 median_min=265.3 median_avg=265.5
Perth-Telstra   -> Santiago     anchor 3701 meas 66410849 n=360 median_min=312.0 median_avg=312.1
Perth-Vocus     -> Santiago     anchor 3701 meas 66410849 n=360 median_min=348.0 median_avg=348.1
Perth-Spintel   -> Santiago     anchor 3701 meas 66410849 n=360 median_min=366.9 median_avg=367.0
Sydney-Telstra  -> SaoPaulo     anchor 2474 meas 29650317 n=360 median_min=303.4 median_avg=303.6
Perth-Telstra   -> SaoPaulo     anchor 2474 meas 29650317 n=360 median_min=348.3 median_avg=348.4
Perth-Vocus     -> SaoPaulo     anchor 2474 meas 29650317 n=360 median_min=365.3 median_avg=365.3
Perth-Spintel   -> SaoPaulo     anchor 2474 meas 29650317 n=360 median_min=379.8 median_avg=379.8
Sydney-Telstra  -> BuenosAires  anchor 4327 meas 112718717 n=360 median_min=306.4 median_avg=307.0
Perth-Telstra   -> BuenosAires  anchor 4327 meas 112718717 n=360 median_min=357.2 median_avg=357.8
Perth-Vocus     -> BuenosAires  anchor 4327 meas 112718717 n=360 median_min=384.7 median_avg=384.8
Perth-Spintel   -> BuenosAires  anchor 4327 meas 112718717 n=360 median_min=367.8 median_avg=368.4
Sydney-Telstra  -> BuenosAires  anchor 3816 meas 94342428 n=359 median_min=448.4 median_avg=448.5
Perth-Telstra   -> BuenosAires  anchor 3816 meas 94342428 n=360 median_min=446.7 median_avg=446.8
Perth-Vocus     -> BuenosAires  anchor 3816 meas 94342428 n=360 median_min=387.9 median_avg=387.9
Perth-Spintel   -> BuenosAires  anchor 3816 meas 94342428 n=360 median_min=444.9 median_avg=444.9
Sydney-Telstra  -> Sydney       anchor 3744 meas 68453928 n=360 median_min=0.1 median_avg=0.1
Perth-Telstra   -> Sydney       anchor 3744 meas 68453928 n=360 median_min=47.4 median_avg=47.6
Perth-Vocus     -> Sydney       anchor 3744 meas 68453928 n=360 median_min=49.0 median_avg=49.1
Perth-Spintel   -> Sydney       anchor 3744 meas 68453928 n=360 median_min=48.1 median_avg=48.1
Sydney-Telstra  -> Perth        anchor 3429 meas 88122901 n=359 median_min=47.4 median_avg=47.6
Perth-Telstra   -> Perth        anchor 3429 meas 88122901 n=359 median_min=0.1 median_avg=0.1
Perth-Vocus     -> Perth        anchor 3429 meas 88122901 n=359 median_min=0.7 median_avg=0.8
Perth-Spintel   -> Perth        anchor 3429 meas 88122901 n=359 median_min=1.1 median_avg=1.1
Sydney-Telstra  -> Perth        anchor 3886 meas 84190565 n=360 median_min=48.9 median_avg=49.1
Perth-Telstra   -> Perth        anchor 3886 meas 84190565 n=360 median_min=0.7 median_avg=0.8
Perth-Vocus     -> Perth        anchor 3886 meas 84190565 n=360 median_min=0.1 median_avg=0.1
Perth-Spintel   -> Perth        anchor 3886 meas 84190565 n=360 median_min=1.4 median_avg=1.5
```

### 11.z Raw RIPE Atlas traceroutes (atlas3.py output; last result in the 6 h before 22:35 UTC, 4 Oct 2026)

```
=== Sydney-Telstra -> Johannesburg anchor 2507 AS12008 meas 29766763 ts 1791153268 proto ICMP
   1 203.41.0.41                                  0.1 ms  
   2 203.48.8.166                                 0.3 ms  tel4239945.lnk.telstra.net
   3 203.48.8.165                                 0.9 ms  Bundle-Ether803-206.chw-edge903.sydney.telstra.net
   4 203.50.11.176                                1.0 ms  bundle-ether12.stl-core30.sydney.telstra.net
   5 203.50.6.116                                 0.9 ms  bundle-ether2.pad-gw30.sydney.telstra.net
   6 203.50.13.86                                 3.1 ms  bundle-ether1.sydp-core03.telstraglobal.net
   7 202.84.247.17                              145.6 ms  i-92.eqnx03.telstraglobal.net
   8 198.47.107.249                             145.6 ms  ae10.cr4-sjc1.ip4.gtt.net
   9 141.136.105.114                            424.5 ms  ae1.cr1-jhb2.ip4.gtt.net
  10 76.74.41.138                               426.5 ms  ip4.gtt.net
  11 156.154.135.254                            430.0 ms  
=== Perth-Telstra -> Johannesburg anchor 2507 AS12008 meas 29766763 ts 1791153255 proto ICMP
   1 203.41.0.249                                 0.1 ms  
   2 138.217.126.74                               0.4 ms  tel4198808.lnk.telstra.net
   3 138.217.126.73                               0.8 ms  Bundle-Ether802-218.wel-edge903.perth.telstra.net
   4 203.50.6.174                                 2.0 ms  bundle-ether12.wel-core30.perth.telstra.net
   5 203.50.6.238                                29.2 ms  bundle-ether2.fli-core30.adelaide.telstra.net
   6 203.50.6.124                                37.6 ms  bundle-ether4.win-core30.melbourne.telstra.net
   7 203.50.13.130                               47.8 ms  bundle-ether3.stl-core30.sydney.telstra.net
   8 203.50.6.116                                48.1 ms  bundle-ether2.pad-gw30.sydney.telstra.net
   9 203.50.13.86                                48.1 ms  bundle-ether1.sydp-core03.telstraglobal.net
  10 202.84.247.17                              193.0 ms  i-92.eqnx03.telstraglobal.net
  11 198.47.107.249                             194.9 ms  ae10.cr4-sjc1.ip4.gtt.net
  12 141.136.105.114                            473.8 ms  ae1.cr1-jhb2.ip4.gtt.net
  13 76.74.41.138                               508.6 ms  ip4.gtt.net
  14 156.154.135.254                            476.6 ms  
=== Perth-Spintel -> Johannesburg anchor 2507 AS12008 meas 29766763 ts 1791153258 proto ICMP
   1 202.87.175.241                               0.4 ms  ae0-900.core02.per1.spintel.net.au
   2 162.43.138.46                                0.9 ms  ae1-220.per-nxt1-ip-1.megaport.com
   3 162.43.129.20                                1.0 ms  ae1-4060.per-vo1-ip-1.megaport.com
   4 27.122.123.136                               1.4 ms  
   5 172.21.93.47                               192.9 ms  
   6 172.21.92.175                              192.5 ms  
   7 202.130.207.68                             192.5 ms  TenGigE0-0-0-13.bdr01-ipt-6leongou-mrs.fr.as38195.net
   8 195.66.224.68                              260.6 ms  ae-0-0-0.luk-pr3-tho.liquidtelecom.net
   9 5.11.12.35                                 429.2 ms  hu-0-0-0-5.lng-pe4-adc.liquidtelecom.net
  10 41.173.241.169                             430.3 ms  
  11 41.84.151.62                               428.8 ms  hu-0-0-0-10.lng-p2-cpt.liquidtelecom.net
  12 41.175.222.211                             431.2 ms  hu-0-6-0-0.lza-p3-jhb.liquidtelecom.net
  13 41.175.242.17                              450.2 ms  hu-7-0-0-11.lza-p4-jhb.liquidtelecom.net
  14 41.60.135.93                               429.0 ms  be-20.lza-pe2-jhb.liquidtelecom.net
  15 41.60.134.175                              452.2 ms  
  16 156.154.135.254                            453.1 ms  
=== Sydney-Telstra -> CapeTown anchor 4099 AS328266 meas 86150184 ts 1791153168 proto ICMP
   1 203.41.0.41                                  0.1 ms  
   2 203.48.8.166                                 0.3 ms  tel4239945.lnk.telstra.net
   3 203.48.8.165                                 0.8 ms  Bundle-Ether803-206.chw-edge903.sydney.telstra.net
   4 110.145.206.62                               3.2 ms  opt2823000.lnk.telstra.net
   5 61.88.33.3                                   3.0 ms  
   6 61.88.33.10                                  3.4 ms  
   7 206.148.27.234                               1.2 ms  transit-edge.globalsecurelayer.com
   8 206.148.24.212                               1.7 ms  po5.syd-eqxsy5-bb13.globalsecurelayer.com
   9 206.148.24.221                              47.5 ms  po1.per-ndcp2-bb7.globalsecurelayer.com
  10 206.148.24.11                               47.5 ms  po4.per-eqxpe2-bb5.globalsecurelayer.com
  11 206.148.24.217                              47.4 ms  po1.per-eqxpe2-cr6.globalsecurelayer.com
  12 206.148.27.4                               143.7 ms  po8.mct-eqxmc1-bb1.globalsecurelayer.com
  13 206.148.27.3                               272.3 ms  po5.mrs-ixmrs2-cr4.globalsecurelayer.com
  14 206.148.26.68                              254.7 ms  po8.par-thpa2-cr4.globalsecurelayer.com
  15 206.148.26.175                             257.9 ms  e33.lon-thn-cr8.globalsecurelayer.com
  16 206.148.26.15                              259.4 ms  e50.lon-eqxld8-cr6.globalsecurelayer.com
  17 223.165.7.140                              278.9 ms  e4.lon-eqxld8-cr9.globalsecurelayer.com
  18 223.165.7.141                              265.8 ms  unknown.globalsecurelayer.com
  19 *
  20 *
  21 102.216.76.17                              440.9 ms  cpt-ter-rs1-vl120.atomic.ac
  22 102.216.76.21                              418.7 ms  cpt-ter-rs2-vl122.atomic.ac
  23 102.208.239.123                            415.4 ms  cpt-ter-anchor1.atomic.ac
=== Perth-Telstra -> CapeTown anchor 4099 AS328266 meas 86150184 ts 1791153176 proto ICMP
   1 203.41.0.249                                 0.4 ms  
   2 138.217.126.74                               0.3 ms  tel4198808.lnk.telstra.net
   3 138.217.126.73                               1.1 ms  Bundle-Ether802-218.wel-edge903.perth.telstra.net
   4 139.130.82.154                               3.6 ms  opt4048251.lnk.telstra.net
   5 61.88.33.13                                  2.5 ms  
   6 *
   7 124.19.61.63                                 0.6 ms  
   8 206.148.27.234                               1.1 ms  transit-edge.globalsecurelayer.com
   9 206.148.27.4                                97.5 ms  po8.mct-eqxmc1-bb1.globalsecurelayer.com
  10 206.148.27.3                               310.1 ms  po5.mrs-ixmrs2-cr4.globalsecurelayer.com
  11 206.148.26.68                              261.1 ms  po8.par-thpa2-cr4.globalsecurelayer.com
  12 206.148.26.175                             258.5 ms  e33.lon-thn-cr8.globalsecurelayer.com
  13 206.148.26.15                              258.8 ms  e50.lon-eqxld8-cr6.globalsecurelayer.com
  14 223.165.7.140                              315.5 ms  e4.lon-eqxld8-cr9.globalsecurelayer.com
  15 223.165.7.141                              269.0 ms  unknown.globalsecurelayer.com
  16 *
  17 *
  18 102.216.76.17                              416.2 ms  cpt-ter-rs1-vl120.atomic.ac
  19 102.216.76.21                              420.8 ms  cpt-ter-rs2-vl122.atomic.ac
  20 102.208.239.123                            416.8 ms  cpt-ter-anchor1.atomic.ac
=== Perth-Spintel -> CapeTown anchor 4099 AS328266 meas 86150184 ts 1791153173 proto ICMP
   1 202.87.175.241                               0.3 ms  ae0-900.core02.per1.spintel.net.au
   2 202.87.175.0                                 0.5 ms  ae0-100.core01.per1.spintel.net.au
   3 103.136.102.44                               0.5 ms  as137409.per.edgeix.net.au
   4 206.148.24.102                               0.5 ms  e29.per-ndcp2-bb7.globalsecurelayer.com
   5 206.148.24.11                                0.5 ms  po4.per-eqxpe2-bb5.globalsecurelayer.com
   6 206.148.24.217                               0.4 ms  po1.per-eqxpe2-cr6.globalsecurelayer.com
   7 206.148.27.4                                96.8 ms  po8.mct-eqxmc1-bb1.globalsecurelayer.com
   8 206.148.27.3                               290.5 ms  po5.mrs-ixmrs2-cr4.globalsecurelayer.com
   9 206.148.26.68                              283.4 ms  po8.par-thpa2-cr4.globalsecurelayer.com
  10 206.148.26.175                             283.4 ms  e33.lon-thn-cr8.globalsecurelayer.com
  11 206.148.26.15                              262.5 ms  e50.lon-eqxld8-cr6.globalsecurelayer.com
  12 223.165.7.140                              262.3 ms  e4.lon-eqxld8-cr9.globalsecurelayer.com
  13 223.165.7.141                              396.9 ms  unknown.globalsecurelayer.com
  14 *
  15 *
  16 102.216.76.17                              397.1 ms  cpt-ter-rs1-vl120.atomic.ac
  17 102.216.76.21                              397.0 ms  cpt-ter-rs2-vl122.atomic.ac
  18 102.208.239.123                            397.1 ms  cpt-ter-anchor1.atomic.ac
=== Sydney-Telstra -> Santiago anchor 3062 AS52511 meas 43406701 ts 1791153221 proto ICMP
   1 203.41.0.41                                  0.2 ms  
   2 203.48.8.166                                 0.2 ms  tel4239945.lnk.telstra.net
   3 203.48.8.165                                 0.9 ms  Bundle-Ether803-206.chw-edge903.sydney.telstra.net
   4 203.50.11.176                                1.2 ms  bundle-ether12.stl-core30.sydney.telstra.net
   5 203.50.6.116                                 1.4 ms  bundle-ether2.pad-gw30.sydney.telstra.net
   6 203.50.13.86                                 1.5 ms  bundle-ether1.sydp-core03.telstraglobal.net
   7 202.84.247.17                              145.6 ms  i-92.eqnx03.telstraglobal.net
   8 4.68.68.125                                146.2 ms  ae10.edge1.sjo1.sp.lumen.tech
   9 200.189.207.6                              265.1 ms  ae2.3601.edge1.sgo1.ciriontechnologies.net
  10 8.243.191.134                              263.4 ms  
  11 *
  12 *
  13 138.186.10.34                              265.2 ms  34.10.186.138.static.hostednode.net
=== Perth-Telstra -> Santiago anchor 3062 AS52511 meas 43406701 ts 1791153229 proto ICMP
   1 203.41.0.249                                 0.2 ms  
   2 138.217.126.74                               0.4 ms  tel4198808.lnk.telstra.net
   3 138.217.126.73                               1.0 ms  Bundle-Ether802-218.wel-edge903.perth.telstra.net
   4 203.50.6.174                                 0.7 ms  bundle-ether12.wel-core30.perth.telstra.net
   5 203.50.6.238                                29.5 ms  bundle-ether2.fli-core30.adelaide.telstra.net
   6 203.50.6.124                                37.1 ms  bundle-ether4.win-core30.melbourne.telstra.net
   7 203.50.13.130                               47.8 ms  bundle-ether3.stl-core30.sydney.telstra.net
   8 203.50.6.116                                48.8 ms  bundle-ether2.pad-gw30.sydney.telstra.net
   9 203.50.13.86                                48.9 ms  bundle-ether1.sydp-core03.telstraglobal.net
  10 202.84.247.17                              193.0 ms  i-92.eqnx03.telstraglobal.net
  11 4.68.68.125                                193.3 ms  ae10.edge1.sjo1.sp.lumen.tech
  12 200.189.207.6                              311.4 ms  ae2.3601.edge1.sgo1.ciriontechnologies.net
  13 8.243.191.134                              310.0 ms  
  14 *
  15 *
  16 138.186.10.34                              310.4 ms  34.10.186.138.static.hostednode.net
=== Perth-Spintel -> Santiago anchor 3062 AS52511 meas 43406701 ts 1791153221 proto ICMP
   1 202.87.175.241                               0.2 ms  ae0-900.core02.per1.spintel.net.au
   2 162.43.138.46                                0.7 ms  ae1-220.per-nxt1-ip-1.megaport.com
   3 162.43.129.20                                1.0 ms  ae1-4060.per-vo1-ip-1.megaport.com
   4 27.122.123.136                               1.4 ms  
   5 103.200.15.137                             197.1 ms  
   6 103.200.13.168                             216.5 ms  HundredGigE0-0-1-2.921.bdr01-ipt-624sgran-lax.us.as38195.net
   7 206.72.211.186                             216.6 ms  206.72.211.186.any2ix.coresite.com
   8 200.25.75.21                               226.2 ms  ae300.0.edge1.dal1.as7195.net
   9 200.25.51.213                              226.2 ms  ae0.0.edge2.dal1.as7195.net
  10 200.25.75.52                               253.7 ms  ae400.0.edge1.mia1.as7195.net
  11 200.25.75.25                               315.2 ms  ae610.0.edge1.lim1.as7195.net
  12 200.25.51.149                              344.4 ms  ae6.0.edge2.scl1.as7195.net
  13 148.222.224.5                              366.1 ms  
  14 *
  15 *
  16 138.186.10.34                              366.8 ms  34.10.186.138.static.hostednode.net
=== Sydney-Telstra -> SaoPaulo anchor 2474 AS12008 meas 29650316 ts 1791152992 proto ICMP
   1 203.41.0.41                                  0.1 ms  
   2 203.48.8.166                                 0.2 ms  tel4239945.lnk.telstra.net
   3 203.48.8.165                                 0.8 ms  Bundle-Ether803-206.chw-edge903.sydney.telstra.net
   4 203.50.11.176                                1.1 ms  bundle-ether12.stl-core30.sydney.telstra.net
   5 203.50.6.116                                 0.9 ms  bundle-ether2.pad-gw30.sydney.telstra.net
   6 203.50.13.86                                 1.6 ms  bundle-ether1.sydp-core03.telstraglobal.net
   7 202.84.247.17                              145.6 ms  i-92.eqnx03.telstraglobal.net
   8 198.47.107.249                             145.4 ms  ae10.cr4-sjc1.ip4.gtt.net
   9 89.149.187.82                              299.8 ms  ae4.cr1-sao6.ip4.gtt.net
  10 208.116.240.222                            300.1 ms  ip4.gtt.net
  11 156.154.122.254                            302.1 ms  
=== Perth-Telstra -> SaoPaulo anchor 2474 AS12008 meas 29650316 ts 1791152983 proto ICMP
   1 203.41.0.249                                 0.2 ms  
   2 138.217.126.74                               0.3 ms  tel4198808.lnk.telstra.net
   3 138.217.126.73                               1.0 ms  Bundle-Ether802-218.wel-edge903.perth.telstra.net
   4 203.50.6.174                                 1.1 ms  bundle-ether12.wel-core30.perth.telstra.net
   5 203.50.6.238                                29.1 ms  bundle-ether2.fli-core30.adelaide.telstra.net
   6 203.50.6.124                                37.3 ms  bundle-ether4.win-core30.melbourne.telstra.net
   7 203.50.13.130                               47.5 ms  bundle-ether3.stl-core30.sydney.telstra.net
   8 203.50.6.116                                48.8 ms  bundle-ether2.pad-gw30.sydney.telstra.net
   9 203.50.13.86                                48.1 ms  bundle-ether1.sydp-core03.telstraglobal.net
  10 202.84.247.17                              192.9 ms  i-92.eqnx03.telstraglobal.net
  11 198.47.107.249                             194.9 ms  ae10.cr4-sjc1.ip4.gtt.net
  12 89.149.187.82                              347.0 ms  ae4.cr1-sao6.ip4.gtt.net
  13 208.116.240.222                            347.2 ms  ip4.gtt.net
  14 156.154.122.254                            347.0 ms  
=== Perth-Spintel -> SaoPaulo anchor 2474 AS12008 meas 29650316 ts 1791152991 proto ICMP
   1 202.87.175.241                               0.2 ms  ae0-900.core02.per1.spintel.net.au
   2 162.43.138.46                                0.7 ms  ae1-220.per-nxt1-ip-1.megaport.com
   3 162.43.129.20                                1.0 ms  ae1-4060.per-vo1-ip-1.megaport.com
   4 27.122.123.136                               1.4 ms  
   5 103.200.15.139                             217.3 ms  
   6 103.200.13.168                             215.9 ms  HundredGigE0-0-1-2.921.bdr01-ipt-624sgran-lax.us.as38195.net
   7 206.72.211.186                             215.7 ms  206.72.211.186.any2ix.coresite.com
   8 200.25.75.21                               225.7 ms  ae300.0.edge1.dal1.as7195.net
   9 200.25.51.213                              225.5 ms  ae0.0.edge2.dal1.as7195.net
  10 200.25.51.214                              255.2 ms  ae1214.0.edge2.mia1.as7195.net
  11 200.25.51.34                               255.1 ms  ae0.0.edge1.mia1.as7195.net
  12 200.25.51.14                               359.5 ms  ae1055.0.edge7.gru1.as7195.net
  13 200.25.51.247                              360.9 ms  ae0.0.edge8.gru1.as7195.net
  14 200.25.91.167                              358.8 ms  
  15 156.154.122.254                            380.1 ms  
=== Sydney-Telstra -> BuenosAires anchor 4327 AS52376 meas 112718716 ts 1791153231 proto ICMP
   1 203.41.0.41                                  0.2 ms  
   2 203.48.8.166                                 0.4 ms  tel4239945.lnk.telstra.net
   3 203.48.8.165                                 0.9 ms  Bundle-Ether803-206.chw-edge903.sydney.telstra.net
   4 203.50.11.176                                0.8 ms  bundle-ether12.stl-core30.sydney.telstra.net
   5 203.50.6.116                                 1.0 ms  bundle-ether2.pad-gw30.sydney.telstra.net
   6 203.50.13.86                                 1.5 ms  bundle-ether1.sydp-core03.telstraglobal.net
   7 202.84.247.41                              186.5 ms  i-92.paix02.telstraglobal.net
   8 195.22.206.150                             186.8 ms  
   9 185.70.203.99                              306.5 ms  
  10 185.70.203.13                              308.5 ms  
  11 190.210.110.213                            329.2 ms  customer-static-210-110-213.iplannetworks.net
  12 200.68.121.90                              330.0 ms  customer-static-68-121-90.iplannetworks.net
  13 201.182.140.236                            329.9 ms  
  14 200.9.157.230                              329.4 ms  
  15 200.9.157.207                              327.9 ms  
=== Perth-Telstra -> BuenosAires anchor 4327 AS52376 meas 112718716 ts 1791153230 proto ICMP
   1 203.41.0.249                                 0.2 ms  
   2 138.217.126.74                               0.2 ms  tel4198808.lnk.telstra.net
   3 138.217.126.73                               1.1 ms  Bundle-Ether802-218.wel-edge903.perth.telstra.net
   4 203.50.6.174                                 1.5 ms  bundle-ether12.wel-core30.perth.telstra.net
   5 203.50.6.238                                29.2 ms  bundle-ether2.fli-core30.adelaide.telstra.net
   6 203.50.6.124                                38.5 ms  bundle-ether4.win-core30.melbourne.telstra.net
   7 203.50.13.130                               49.1 ms  bundle-ether3.stl-core30.sydney.telstra.net
   8 203.50.6.116                                48.5 ms  bundle-ether2.pad-gw30.sydney.telstra.net
   9 203.50.13.86                                48.1 ms  bundle-ether1.sydp-core03.telstraglobal.net
  10 202.84.247.41                              233.9 ms  i-92.paix02.telstraglobal.net
  11 195.22.206.150                             233.8 ms  
  12 185.70.203.99                              357.5 ms  
  13 185.70.203.13                              353.7 ms  
  14 190.210.110.213                            375.8 ms  customer-static-210-110-213.iplannetworks.net
  15 200.68.121.90                              374.7 ms  customer-static-68-121-90.iplannetworks.net
  16 201.182.140.236                            375.2 ms  
  17 200.9.157.230                              376.4 ms  
  18 200.9.157.207                              379.2 ms  
=== Perth-Spintel -> BuenosAires anchor 4327 AS52376 meas 112718716 ts 1791153230 proto ICMP
   1 202.87.175.241                               0.2 ms  ae0-900.core02.per1.spintel.net.au
   2 162.43.138.46                                0.9 ms  ae1-220.per-nxt1-ip-1.megaport.com
   3 138.217.49.189                               1.4 ms  Bundle-Ether28.wel-edge903.perth.telstra.net
   4 203.50.6.174                                 1.8 ms  bundle-ether12.wel-core30.perth.telstra.net
   5 203.50.6.238                                29.9 ms  bundle-ether2.fli-core30.adelaide.telstra.net
   6 203.50.6.124                                38.0 ms  bundle-ether4.win-core30.melbourne.telstra.net
   7 203.50.13.130                               49.1 ms  bundle-ether3.stl-core30.sydney.telstra.net
   8 203.50.6.116                                49.0 ms  bundle-ether2.pad-gw30.sydney.telstra.net
   9 203.50.13.86                                49.1 ms  bundle-ether1.sydp-core03.telstraglobal.net
  10 202.84.247.41                              237.8 ms  i-92.paix02.telstraglobal.net
  11 195.22.206.150                             233.0 ms  
  12 185.70.203.89                              370.4 ms  
  13 185.70.203.13                              369.4 ms  
  14 190.210.110.213                            390.1 ms  customer-static-210-110-213.iplannetworks.net
  15 200.68.121.90                              391.4 ms  customer-static-68-121-90.iplannetworks.net
  16 201.182.140.236                            391.4 ms  
  17 200.9.157.230                              390.7 ms  
  18 200.9.157.207                              390.7 ms  
```

### 11.w Azure matrix extract (azparse.py output from the Microsoft Learn page dated 2026-07-30; values P50 ms, source row to destination column; reverse direction differs by 0-4 ms)

```
Australia East      ->South Africa North   328  (reverse 328)
Australia East      ->South Africa West    328  (reverse 328)
Australia Southeast ->South Africa North   321  (reverse 321)
Australia East      ->Brazil South         295  (reverse 295)
Australia Southeast ->Brazil South         307  (reverse 307)
Australia East      ->West US              140  (reverse 140)
Australia East      ->Southeast Asia       95  (reverse 95)
Australia East      ->UK South             261  (reverse 261)
Australia East      ->Central India        144  (reverse 145)
South Africa North  ->Brazil South         321  (reverse 321)
South Africa North  ->UK South             163  (reverse 164)
South Africa North  ->Southeast Asia       177  (reverse 177)
Brazil South        ->West US              169  (reverse 169)
Brazil South        ->Southeast Asia       331  (reverse 330)
Australia East      ->Australia Southeast  15  (reverse 15)
```

### 11.v Method for the TeleGeography extraction

`curl -sL -A "Mozilla/5.0" https://www.submarinecablemap.com/api/v3/cable/all.json` returned 712 cable ids; each fetched from `/api/v3/cable/<id>.json` (fields: name, length, landing_points[name,country,is_tbd], owners, suppliers, rfs, rfs_year, is_planned). Script: fetchall.py (8 threads). Filter by landing-point country (Australia, South Africa, Chile, Argentina, Brazil, Peru) in q.py. The HTML pages of submarinecablemap.com are JavaScript-rendered and WebFetch returns nothing useful; the JSON API is the usable route.

### 11.u Raw output of atlas5.py (Perth and Sydney probes to Singapore and Mauritius anchors; median of per-sample minimum RTT, last 24 h, 4 Oct 2026)

```
Perth-Telstra   -> sg-sin-as12008      192.3 ms     Perth-Vocus  -> same 53.0   Perth-Spintel -> same 125.7   Sydney-Telstra -> same 145.0
Perth-Telstra   -> sg-sin-as132337     305.0 ms     Perth-Vocus  -> same 53.0   Perth-Spintel -> same 311.3   Sydney-Telstra -> same 260.2
Perth-Telstra   -> sg-sin-as139225     275.9 ms     Perth-Vocus  -> same 53.1   Perth-Spintel -> same 312.5   Sydney-Telstra -> same 221.4
Perth-Telstra   -> mu-ebn-as327821 (Ebene, Mauritius)       513.5   Perth-Vocus 333.3   Perth-Spintel 412.3   Sydney-Telstra 465.9
Perth-Telstra   -> mu-qbe-as328699 (Quatre Bornes, Mauritius) 507.5  Perth-Vocus 541.3   Perth-Spintel 388.5   Sydney-Telstra 498.5
```

(Perth to Mauritius, 5,906 km great-circle with a floor of 58 ms, measures 330-540 ms: there is no direct Perth-Mauritius path today either.)

## 12. Searches and dead ends (exact strings, in order)

### 12.1 WebSearch queries run (35)

1. `Google Umoja subsea cable Africa Australia Perth status 2026 ready for service`
2. `Humboldt cable Google Chile Sydney latency milliseconds Santiago Sydney` (no latency figure in any result)
3. `Halaihai cable Google Valparaiso French Polynesia Guam Honomoana Humboldt 2026`
4. `Google Umoja announcement blog "Umoja" Africa Australia "distinct from existing" route resilience Liquid Intelligent Technologies Perth` (allowed domains blog.google, cloud.google.com, techcrunch.com)
5. `Umoja cable Eastern Cape Digital Exchange Port Google July 2026 Amanzimtoti landing`
6. `Australia international submarine cable resilience Department of Infrastructure Communications Sunda Strait Indonesia chokepoint diversity cable routes` (found the ANU paper and the Perth-Singapore outage pieces)
7. `Red Sea cable cuts September 2025 Azure latency Asia Europe SMW4 IMEWE Microsoft`
8. `West Africa March 2024 subsea cable cuts WACS SAT-3 South Africa impact Congo Canyon Microsoft Azure`
9. `BHP Integrated Remote Operations Centre Perth Escondida Spence Santiago operations centre Chile global operations remote`
10. `Rio Tinto Operations Centre Perth Pilbara remote operations also controls mines outside Australia Mongolia South Africa Richards Bay Minerals`
11. `BHP Escondida "centro de operaciones" remoto Santiago Antofagasta Spence operaciones remotas 2024 OR 2025`
12. `Anglo American Collahuasi OR "Los Bronces" remote operations centre Santiago OR Johannesburg Australia operations centre Moranbah Perth shared`
13. `Australia South Africa two-way trade goods and services 2024-25 DFAT country brief Australian investment South Africa` (allowed domains dfat.gov.au, austrade.gov.au; no figures returned)
14. `Australia Brazil two-way trade goods and services 2024-25 DFAT Australia Chile Argentina trade total` (same filter; only an Argentina 2024 figure came back)
15. `Australia South Africa bilateral trade value billion 2024 Australian companies mining South Africa ASX JSE dual listed`
16. `TeleGeography blog Humboldt cable South America Asia Pacific demand traffic currently routes via United States Chile Asia latency` (no TeleGeography post found)
17. `TeleGeography Africa Asia Pacific bandwidth Australia Africa traffic Umoja Waterworth Indian Ocean new routes analysis`
18. `Project Waterworth Meta Darwin Australia landing South Africa Cape Town Brazil Fortaleza 2026 update` (**returned only Darwin water-supply pages: dead end at the query, "Waterworth" collided with water infrastructure; died at the query not the sources; the Meta engineering page was fetched directly instead**)
19. `SKA Observatory data flow Science Processing Centre Perth Cape Town SKA Regional Centre Network 700 petabytes per year distribution to regional centres bandwidth Gbps`
20. `SKAO science data products transfer from Perth SPC and Cape Town SPC to SRCNet nodes AARNet SANReN TENET network capacity Australia South Africa research link` (led to the SKA-NREN Forum and SA3CC decks)
21. `Australian Antarctic Division station communications satellite Starlink Casey Davis Mawson bandwidth Mbps data link Hobart 2025` (no Starlink-at-Australian-stations evidence; Wikipedia's 9 Mbit/s Speedcast figure came from a follow-on fetch)
22. `SANAE IV Marion Island satellite communications bandwidth South African National Antarctic Programme data link Cape Town Starlink Intelsat` (no bandwidth figure)
23. `number of ASX-listed companies with projects in Latin America Argentina Chile Peru mining lithium copper Australian companies Latin America Austmine` (no total count)
24. `Australian mining investment Africa Down Under 2026 ASX-listed companies operating in Africa number countries A$ billion`
25. `February 2024 Red Sea cable cuts AAE-1 Seacom EIG Rubymar impact 25% Asia Europe traffic HGC Global Communications`
26. `Australia-Singapore Cable ASC fault September 2026 Anyer Java Indigo Perth outage latency`
27. `Perth Indigo West Central cable outage August 2026 Vocus Telstra AARNet Western Australia internet impact`
28. `AARNet Humboldt cable Chile research and education network astronomy data Australia Chile ESO GMT RENATA REUNA direct link`
29. `Giant Magellan Telescope data center Australia Astronomy Australia Limited GMT data flow archive Australian Astronomical Optics Macquarie GMT-Consortium operations` (no data-flow architecture found)
30. `Starlink Antarctica McMurdo laser inter-satellite links gateway ground station location New Zealand Australia Chile NSF traffic routed` (gateway countries not named)
31. `Equiano SACS South Atlantic Cable System Angola Brazil South Africa Brazil direct cable none Cape Town São Paulo latency`
32. `SUBCO APX East cable Sydney Fiji Hawaii Chile Los Angeles Biobío announcement` (revealed the TeleGeography "Los Angeles, Chile" error)
33. `Humboldt cable 2026 status Desarrollo País Google installation start SubCom Valparaiso Papeete 2028 delayed OR approved OR landing Sydney`
34. `Gold Fields Perth Johannesburg head office Australia region operations Salares Norte Chile Peru Ghana corporate IT shared services remote operations`
35. `South32 headquarters Perth operations South Africa Hillside Aluminium South Africa Manganese Brazil Alumar Chile Sierra Gorda Colombia Cerro Matoso`

### 12.2 Fetches and dead ends

- Opened and used: TeleGeography JSON API (`https://www.submarinecablemap.com/api/v3/cable/all.json` and per-cable files; `.../landing-point/landing-point-geo.json`); Google Cloud blog posts (Humboldt 2024-01-11, Africa Connect/Umoja 2024-05-23, Australia Connect/Bosun 2024-11-25); Meta engineering post on Waterworth; Wikipedia pages (Humboldt Cable, Australia-South Africa relations, Telecommunications in Antarctica); Microsoft Learn Azure latency page and its GitHub markdown, and the Azure regions list; WonderNetwork Sydney and Perth ping pages (raw HTML); RIPE Atlas API (anchors, anchor-measurements, measurements, results); Verizon latency page; ANU NSC "Connected & protected" PDF (saved and read with pdftotext); SKA-NREN Forum and SA3CC PDFs (Hughes-Jones); REUNA SA3CC 2022 PDF; SSC Space station pages; TechCentral on the Eastern Cape hub; im-mining BHP Copper Advanced Services; ipregistry, Light Reading, iTnews and submarinenetworks pieces on the Perth faults; Cloudflare blog 14 Mar 2024; maritime-executive on Chile's Antarctic cable; cloudnews.tech opinion piece on a Chile-South Africa link.
- **Dead ends (and where each died):**
  - Wikipedia "Umoja (cable)" returned 404 (died at the source; the TeleGeography JSON replaced it).
  - `https://www.submarinecablemap.com/submarine-cable/umoja` and `/humboldt` HTML pages: the content is JavaScript-rendered, so WebFetch got only the page header (died at the source; the JSON API worked).
  - `https://blog.google/around-the-globe/google-africa/google-announces-umoja-first-subsea-cable-africa-australia/`: 404 (a guessed URL; the Google Cloud blog URL found by search worked).
  - DFAT country-brief pages (`/geo/south-africa|brazil|chile|argentina/<name>-country-brief`) and fact-sheet PDFs (`chle-cef.pdf`, `safr-cef.pdf`, `braz-cef.pdf`, `arge-cef.pdf`) timed out three times with WebFetch (60 s) and returned nothing to curl (the site blocks or drops automated requests). Trade figures for 2024-25 therefore remain unverified; the DFAT minister's Africa Down Under speech page also timed out.
  - AT&T global network latency page (`ipnetwork.bgtmo.ip.att.net/pws/global_network_avgs.html`): connection refused.
  - 403 Forbidden to WebFetch: bhp.com (10 years of remote operations), miningweekly.com (Australian mining investment in Africa), south32.net (operations), bnamericas.com (scientific community and the Chile-Australia cable).
  - TeleGeography blog "the-need-for-speed": 404.
  - The ANU PDF could not be parsed by WebFetch (binary); read via the saved copy and pdftotext.
  - Cloudflare Radar was not queried; its public pages are not suited to pairwise Australia-Chile or Australia-South Africa latency. RIPE Atlas gave the pairwise data instead.
  - "Humboldt" in TeleGeography: not found as a cable name under any id containing "humboldt", "humboldt-cable" or "humboldt-connect" (all returned the HTML shell or no record).
  - Not searched at all: Southern Cross NEXT capacity and utilization details, SEACOM, SAFE, WACS, EASSy and Equiano capacities (only existence, year, route and length were taken from TeleGeography); Indigo capacity (the Perth outage pieces quote about 100 Tbit/s combined with ASC); Australian Home Affairs or DFAT statements beyond the ANU paper; ASX-B3 and ASX-JSE trading-link or cross-listing statistics; Australia-Chile or Australia-South Africa services trade; shipping and AIS data-exchange volumes; Iridium gateway locations; Hartebeesthoek's coverage claims; ESA New Norcia and Dongara specifics.

### 12.3 Where I would look next (not done)

1. TeleGeography's paid inter-regional bandwidth and pricing tables (Australia to Latin America and Africa); the 2024 Australian international bandwidth by region.
2. Google Cloud region-to-region latency (Santiago, Sydney, Johannesburg, Perth/Melbourne) from Google's published inter-region tables or cloudping, to extend the Azure result to Chile.
3. A repeat of atlas2.py after the INDIGO and ASC repairs, to measure the recovered Perth-Singapore baseline.
4. The ACMA page "International submarine cables landing Australia" for the authoritative cable list.
5. The SKAO SRCNet network design document to see whether a direct Perth to Cape Town circuit is in the plan once Umoja exists.
