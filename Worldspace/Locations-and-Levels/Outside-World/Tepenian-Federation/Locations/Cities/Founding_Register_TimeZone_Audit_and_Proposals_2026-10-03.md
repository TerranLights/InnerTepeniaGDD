# Founding Register — Time-Zone Audit and Proposals

> **⚠ NAMES (2026-10-03):** this record was written under the old names and is kept as written. Read: Port Lockroy = **Puerto Abrigo** · Juan Carlos = **Pergamino** · Sejong = **Contrapunto** · Vostok = **Ariun Nuur** · Abowasa = **Santa Luce** · Sayowa = **Temirötkel** · Princess Elisabeth = **Utstein** · Bunger Hills City = **Relung Panen**. See `City_Renames_Alias_Table_2026-10-03.md`.

**Date:** 2026-10-03 · **Requested by the developer** (hours-law waiver for this task: *"it's really me who's doing the majority of the thinking"*) · **Companion to** `Founding_Register.md`, which this file **does not change**. Only the developer rules; everything below marked **proposed** is a candidate, not canon (`Founding_Register.md` rule 4).

## ⛔ Method and limits (read first)

- **The rule applied.** Founding nations stand on **geography and access** (`DR-19`), with the developer's working test of **"two, maybe three" time zones** (`DR-22`: Halley/UK, Troll/Norway, Janbogo/Korea). *(The formal ±3 window in `Upper_Earth_Immigration_Composition.md` gates the **Notable** census tier only, `DR-19`; the founder test is the developer's own application of the same distance.)*
- **Solar zone** = round(longitude ÷ 15), from each city's own spec coordinates (Byrd, Dome Fuji and Kunlun from their `Based on:` lines). **Gap** = the smallest circular distance between the city's zone and **any zone the nation's territory reaches** (`Post-War_Nations_Founder_Reference.md` spans where listed; otherwise the nation's real longitudes, marked *). Nations are named in **pre-war terms** (`DR-23`); recasting in post-war nations is a CST task.
- **Founders never rest on the station** (`DR-19`/`DR-24`): every justification below is the **city's own geography and access**, and **no city's founder is justified by another city** (`Founding_Register.md` rule 3).
- **Excluded from every pool:** all of South Asia (`NNS` L44) and all of Africa except South Africa (`DR-22`: *"South Africa does remain as the founder of Sanay"*; part of Signy). **Also flagged below:** `DR-22` says Belgrano, Marambio and Esperanza are the **only** cities where Argentina is a founder, so Argentina is **not** proposed anywhere else.
- **Real-world access facts** (which port or coast faces which sector) are stated from general knowledge and are **not researched** (`LAW 0-R`). Each is marked "gateway" and should be verified before anything is ruled. Say the word and I run the research pass.
- Reproducible: the script and its outputs are in this session's scratchpad; all arithmetic is deterministic.

---

## PART 1 — Audit of the existing founding nations

**First check: the Register's `Solar UTC` column.** All 37 cities with coordinates were recomputed from their specs: **0 mismatches.** (Amundsen Station sits on the pole; every longitude is "solar zone" there, so the test does not apply.)

### 1a. Cities that have a founding nation

| City | Zone | Founder (Register) | Status | Gap | Verdict |
|---|:-:|---|:-:|:-:|---|
| Esperanza | −4 | Argentina | ✅ | 0 | ✓ |
| Marambio | −4 | Argentina | ✅ | 0 | ✓ |
| Belgrano | −2 | Argentina | ✅ | 2 | ✓ |
| Halley | −2 | UK (central role) | ✅ partial | 1 | ✓ |
| Troll | 0 | Norway | ✅ | 0 | ✓ |
| Sanay | 0 | South Africa | ✅ | 1 | ✓ |
| Abowasa | −1 | Italy + the CIN | ⛔ ruled | 2 / 2 | ✓ |
| Princess Elisabeth | +2 | Scandinavian Trade Union (Norway, Sweden, Finland, Denmark, Iceland, Faroes) | ⛔ ruled | 0–3 | ✓ (Iceland is the widest, at 3) |
| Sayowa | +3 | CIN or Kazakhstan, then Kazakh industrialists | ✅ | 1 / 0 | ✓ |
| Mirny | +6 | Russia, China, Australia | ✅ | 0 / 0 / 2 | ✓ |
| Zhongshan | +5 | China (the Sinian Federation) | ✅ | 1 | ✓ |
| Casey | +7 | Australia | ✅ | 1 | ✓ |
| Janbogo | +11 | Korea | ✅ | 2 | ✓ |
| Rothera | −5 | North America and Argentina, with others | ⛔ ruled | 0 / 0 | ✓ on the zone test; **see finding C below** |
| Juan Carlos, Sejong | −4 | an Anglo-Latin society of immigrants from the Americas | ⛔ ruled | 0 | ✓ (every nation of the Americas at these longitudes is within 0–2) |
| **Davis** | +5 | Australia | ✅ | **3** | ✓ **at the limit** |
| **Shirayuki** | +5 | Japan | 🟡 | **3** | ✓ **at the limit** (and the Register notes *allocation, not geography*) |
| **Sinheung** | +5 | Korea | 🟡 | **3** | ✓ **at the limit** (same note) |
| **Mawson** | +4 | **Australia and Kazakhstan** (ruled `DR-33`, 2026-10-03) | ✅ | **4 / 0** | ✅ **RULED: Kazakhstan added as co-founder (gap 0); Australia stays on geography** |
| **Signy** | −3 | South Africa (partial) | ✅ partial | **4** | ✅ **confirmed by the developer 2026-10-03: *"perfectly geographically feasible"*; a ruled exception** |
| Dome Fuji · Fort McMurdo · Palmer City · Amundsen Station · Concordia | various | not nation-based (disciples; "all of Tepenia"; three relationship groups; technical crews; mixed) | — | n/a | not a time-zone question |

### 1b. Findings for you

- **A · Mawson: RULED 2026-10-03 (`DR-33`): co-founded by Australia and Kazakhstan.** Australia's nearest zone is +8 against Mawson's +4 (a gap of 4, a ruled exception on geography, `DR-19`); Kazakhstan (+3…+6) is at gap 0. Closes `R-23`.
- **B · Signy / South Africa is 4 zones, and is CONFIRMED.** Your ruling rested on the Cape Town–South Orkney crossing, not on the zone. **Developer, 2026-10-03:** *"it is perfectly geographically feasible for it to have been established partially in part by South Africa."* Recorded as a confirmed exception to the zone test. The **co-founder** is still open (Part 2).
- **C · A conflict between two of your rulings: Rothera.** `DR-20` (2026-09-30): Rothera was established by *"industrial workers from North America and Argentina, though with other nations being represented."* `DR-22` (2026-10-01): *"the only cities where Argentina is listed as a founder are Belgrano, Marambio, and Esperanza."* Both cannot stand as written. **Decision needed (FQ-13b):** (i) `DR-22` was describing the specs as they then stood, and Rothera keeps Argentina (then Argentina is the founder of **four** cities); (ii) Argentina leaves Rothera and the "industrial workers" are North American (plus others).
- **D · Four borderline cases at exactly 3** (Davis, Shirayuki, Sinheung; Port Lockroy/UK in the spec). They pass; they are listed so a later ruling that tightens the rule to "two" knows where it bites. **Zukelli's shortlist:** Hawaii 2, Indonesia 2, Australia 1, **Mongolia 3, Taiwan 3**.
- **E · The 🟡 allocation rows (Shirayuki, Sinheung).** They pass the zone test at 3, but their Basis says *"Allocation, not geography"*; `DR-19` says a founder stands on **geography and access**. You already ruled on Shirayuki (*"has a Japanese founding population, so that can stay"*). **Decision needed only if you want the Basis rewritten (FQ-13c):** state the founding on the Prydz Bay coast's geography (the gap is 3 for each).

---

## PART 2 — Proposed founding nations for the undetermined cities

**Each entry:** city · zone · what is ruled or open · the **pool** (every nation within 3 zones, pre-war names, minus the exclusions above) · **proposed** · why (the city's own geography and access) · alternatives · flags. *"Gateway"* = the nearest populous port or coast that faces the city's sector (not researched; verify).

### Palmer subnet (Peninsula; zone −4 and its neighbors)

**Port Lockroy** (zone −4; Wiencke Island, Palmer Archipelago) · *Register: ⏸️ open (spec: British; heritage, not a reason).*
- **Pool (gap 0):** Chile, Uruguay, Paraguay, Brazil, Venezuela, Bolivia, Canada · (1) Peru, Colombia, Ecuador · (2) Mexico, Iceland · (3) UK, Ireland, Portugal, Spain, Faroes. *(Argentina omitted: `DR-22`.)* The spec's UK is at gap 3, the edge of the rule.
- **Proposed: Chile.** Gap 0. The Palmer Archipelago faces the Drake Passage's Pacific mouth; the nearest populous gateway on the whole continental side is Chile's Magallanes coast (Punta Arenas, Puerto Williams). *(Gateway; verify.)*
- **Alternatives:** Brazil (gap 0, Atlantic-facing, a long crossing); Uruguay; Canada (zone-matched but a very long haul).

**Sejong** (zone −4; King George Island) · *Ruled: a primarily Anglo-Latin society of immigrants from North, Central and South America; NOT South Korean; first founders open (`DR-20a`). Developer direction: the inherited station records were in Korean and the newcomers spoke Spanish; translators were invited, who invited others (a "New Amsterdam into New York" growth).*
- **Pool:** every nation of the Americas is within 0–2 (see Port Lockroy); the **Spanish-speaking** ones that the ruling requires for the *first* settlers: Chile (0), Uruguay (0), Venezuela (0), Bolivia (0), Peru (1), Colombia (1), Ecuador (1), Mexico (2).
- **Proposed first founders: Chile**, then English-speaking arrivals from **Canada and the eastern United States** (zones −5…−4) as the translators and their circle. Reason: gap 0, and the South Shetlands are the shortest open-water crossing from the Magallanes coast. *(Gateway; verify.)*
- **Alternatives for the first founders:** Peru, Colombia, Ecuador (Pacific coast, gap 1); Uruguay.

**Juan Carlos** (zone −4; Livingston Island) · *Ruled: "essentially the same situation as Sejong"; NOT Spanish; first founders open.*
- **Pool:** as Sejong. **Spanish (Spain) is excluded by ruling** (and is at gap 3).
- **Proposed first founders: Uruguay**, with the same later Anglo and Latin additions. Reason: gap 0; the Río de la Plata (Montevideo) is the Atlantic-side gateway to the South Shetlands. *(Gateway; verify.)*
- **Alternatives:** Peru; Brazil (Portuguese, which is also "Latin"); Chile.
- ⚠ *The developer called these two "the same situation"; to keep them from converging into one story, the first founders are proposed from different coasts. If you want one answer for both, say so.*

**Signy** (zone −3; Signy Island, South Orkney Islands) · *Ruled: South Africa partly; at least one other co-founder open.*
- **Pool for the co-founder (gap ≤ 3):** Uruguay, Paraguay, Brazil (0) · Chile, Venezuela, Bolivia, Iceland (1) · Peru, Colombia, Ecuador, **UK**, Ireland, Portugal, Spain, Faroes (2) · Mexico, France, Netherlands, Norway (3).
- **Proposed co-founder: Brazil.** Gap 0; the South Orkneys sit in the Scotia Sea on the South Atlantic's western side, and Brazil's Atlantic coast is the nearest large populous coast on that sea with a direct open-water run. *(Gateway; verify.)*
- **Alternatives:** Uruguay (Montevideo gateway, gap 0); the UK (gap 2, via its South Atlantic territories).

### Halley subnet (Weddell and Dronning Maud Land coasts; zones −2 to +2)

**Neumayer** (zone −1; Atka Bay, Ekström Ice Shelf) · *Register: ⏸️ open (spec names no founder; Germany ≈ 2 zones).*
- **Pool (gap 0):** UK, Ireland, Iceland, Portugal, Spain, Faroes · (1) Brazil, France, Netherlands, Norway · (2) Uruguay, Paraguay, Canada, **Germany**, Italy, Switzerland, Denmark, Sweden, Finland, the CIN, South Africa* · (3) Chile, Venezuela, Bolivia, Russia, Turkey. *(South Africa is outside by ruling except Sanay/Signy.)*
- **Proposed: France and the Netherlands, jointly.** Gap 1 each; Atlantic-facing ports (the Channel and North Sea coast) sit on the same meridians as the Weddell Sea approach, and a South Atlantic passage from there runs close to the Prime Meridian. *(Gateway; verify.)*
- **Alternatives:** Germany (gap 2; legitimate on the zone and the Atlantic ports, but the real station's operator is German, so it is **kept out of the proposal** to avoid the heritage reading, `DR-19`); Norway (gap 1); Spain or Portugal (gap 0).

**Lazar** (zone +1; Schirmacher Oasis) · *Register: ⏸️ open. The spec's "two coalesced settlements" rests on a Russian-run site and an Indian-run site; **no South Asian population ever came to Tepenia (`NNS` L44)**, so the second community must be re-grounded.*
- **Pool (gap 0):** France, Germany, Italy, Switzerland, Denmark, Norway, Sweden, Finland, the CIN, South Africa* · (1) UK, Spain, Netherlands, Faroes, **Russia**, Turkey · (2) Ireland, Iceland, Portugal, Kazakhstan, Iran · (3) Brazil.
- **Proposed: two communities that coalesced, Russia and the CIN.** Russia (core zones +2…+3) gap 1; the CIN (Eastern Europe) gap 0; the coast faces the Indian Ocean sector south of Africa and is reached from the north over a long sea route in the same longitudinal band. *(Gateway; verify.)*
- **Alternatives:** Russia and Finland (or the STU nations); Russia and Germany; Kazakhstan (gap 2).
- ⚠ *If you want to keep the two-settlement story, the Indian half has to become some other nation; this is the proposal for it.*

### Mawson subnet

*(Mawson, Sayowa and Dome Fuji are ruled; see Part 1 finding A for Mawson.)*

### Mirny subnet (zones +5 to +7)

**Vostok** (zone +7; Lake Vostok, ~1,300 km inland) · *Register: ⏸️ open (spec: Russian exiles; heritage, not a reason).*
- **Pool (gap 0):** Russia, Mongolia, Thailand, Vietnam, Cambodia, Malaysia, Indonesia, Singapore, China · (1) Kazakhstan, Philippines, Taiwan, Korea, Japan, Australia · (2) Papua New Guinea · (3) Iran.
- **Proposed: Russia (Siberian zones) and Mongolia.** Both reach zone +7 on the continental interior; the site is **inland**, so founders come over land/ice from the coast at +6/+7, and these two are the nations whose own territory sits on that meridian band. *(No temperament claim; zone and access only.)*
- **Alternatives:** China (the Sinian Federation); Kazakhstan; a Southeast Asian maritime group (Indonesia, Malaysia, Thailand, Vietnam).

**Kunlun** (zone +5; Dome A, 4,093 m, **zero humans**: a robot-only city) · *Register: ⏸️ open (spec: Chinese, "re-resolved" to a curated multinational population). Canon: Kunlun was launched from Vostok via Highway 37.*
- **Pool (gap 0):** Russia, Kazakhstan · (1) Iran, Mongolia, Thailand, Indonesia, China · (2) Turkey, Vietnam, Cambodia, Malaysia, Singapore · (3) Norway, Sweden, Finland, the CIN, Philippines, Taiwan, Korea, Japan, Australia, South Africa*.
- **Proposed: the same stock as the launching community, namely Vostok's founders (Russia and Mongolia, if Vostok is ruled as proposed), with China (the Sinian Federation, gap 1) as the second founding stock for a curated robot population.** Reason: Kunlun is a plateau city reached from Vostok by `Hwy 37` (relation, not comparison), and the Prydz Bay coast it faces is the Sinian Federation's nearest.
- **Alternatives:** Kazakhstan; a Central Asian group; the spec's China alone.
- ⚠ *Because Kunlun has no humans, "founding nation" means the nationality of the robots' learned origin (`DR-11`), not human settlers.*

**{{Bunger Hills City}}** (zone +7; Bunger Hills, Queen Mary Land) · *Register: ⏸️ open ("NOT YET RULED — developer decision").*
- **Pool:** as Vostok (the same zone): Russia, Mongolia, Thailand, Vietnam, Cambodia, Malaysia, Indonesia, Singapore, China (0) · Kazakhstan, Philippines, Taiwan, Korea, Japan, **Australia** (1) · Papua New Guinea (2) · Iran (3).
- **Proposed: Indonesia and Malaysia, jointly.** Gap 0 each; a Southeast-Asian maritime pair whose open-water run to the Queen Mary Land coast crosses the Indian Ocean on the meridians of the site. *(Gateway; verify.)*
- **Alternatives:** Australia (gap 1; the coast is the nearest populous one, and a strong geography case); Thailand and Vietnam; Mongolia; China.

### Janbogo subnet (Ross Sea and Adélie coasts; zones +8 to +11)

**Scott** (zone +11; Ross Island) · *Register: ⏸️ open (spec: New Zealand exiles; NZ ≈ 1 zone; the gap is actually 0).*
- **Pool (gap 0):** New Zealand, Russia · (1) Japan, Australia, Papua New Guinea, Fiji · (2) Hawaii, Indonesia, Korea · (3) Canada, Mongolia, Malaysia, Philippines, Taiwan, China.
- **Proposed: New Zealand.** Gap 0; New Zealand's Canterbury coast is the nearest populous gateway to the Ross Sea. *(Gateway; verify.)*
- **Alternatives:** Fiji; Australia (via Hobart).

**Denison** (zone +10; Cape Denison, Commonwealth Bay) · *Register: ⏸️ open. Proposed in the composition file: Australia (and New Zealand).*
- **Pool (gap 0):** Australia, Japan, Papua New Guinea, Russia · (1) Indonesia, Korea, New Zealand · (2) Mongolia, Malaysia, Philippines, Taiwan, China, Fiji · (3) Hawaii, Thailand, Vietnam, Cambodia, Singapore.
- **Proposed: Australia.** Gap 0; Commonwealth Bay lies almost due south of Tasmania, so Hobart is the nearest populous gateway. *(Gateway; verify.)* **New Zealand** as a second community (gap 1) if you want a joint founding.
- **Alternatives:** Japan or Papua New Guinea (gap 0); Indonesia.

**Dumont d'Urville** (zone +9; Adélie Land) · *Ruled: NOT France ("the time zones are much too far away"); founder open.*
- **Pool (gap 0):** Russia, Indonesia, Korea, Japan, Australia, Papua New Guinea · (1) Mongolia, Malaysia, Philippines, Taiwan, China · (2) Thailand, Vietnam, Cambodia, Singapore, New Zealand · (3) Kazakhstan, Fiji.
- **Proposed: Japan.** Gap 0; the coast faces the Pacific-Indian sector south of the Japanese archipelago's own meridians, and Japan's reach into the southern ocean is a long but direct run down the same band. *(Gateway; verify.)*
- **Alternatives:** Australia (gap 0; Tasmania is the nearest populous gateway to Adélie Land, a strong geography case); Korea; Indonesia.

**Zukelli** (zone +11; Terra Nova Bay) · *Ruled: NOT Italy; founder open. Developer's shortlist: Hawaii, Mongolia, Taiwan, Indonesia, Australia.*
- **Measured gaps:** Australia **1** · Hawaii **2** · Indonesia **2** · Mongolia **3** · Taiwan **3**. **Within the window but not on the shortlist:** New Zealand (0), Russia (0), Japan (1), Papua New Guinea (1), Fiji (1), Korea (2).
- **Proposed from the shortlist: Australia.** Gap 1, and the Ross Sea sector is reached across the Southern Ocean from the Australian south coast; **Hawaii** is the best geography case among the island options (gap 2, a Pacific crossing). *(Gateway; verify.)*
- **Alternatives:** Hawaii; Indonesia; or any off-list nation above.

**Cape Adare** (zone +11; Adare Peninsula) · *Register: 🟡 mixed, "no single dominant national community" (spec: TBD).* **A nation is not required** (the empty-slot law). If you want one:
- **Pool (gap 0):** New Zealand, Russia · (1) Japan, Australia, Papua New Guinea, Fiji · (2) Hawaii, Indonesia, Korea.
- **If nations are wanted: a joint community of New Zealand and Fiji** (gap 0 and 1; the Ross Sea's Pacific-island gateway band), **or leave it mixed.**

### Byrd subnet (zone −8; Marie Byrd Land)

**Byrd** (zone −8) · *Register: ⏸️ open (spec: American exiles; heritage, not a reason; the United States is a post-war CST question).*
- **Pool (pre-war terms, gap 0):** the **United States' Pacific states**, Canada (British Columbia), Mexico (Sonora, Baja) · (2) Colombia, Ecuador, Hawaii · (3) Chile, Brazil, Peru, Venezuela, Bolivia. *(Argentina excluded.)*
- **Proposed: the United States (Pacific coast) and Canada (British Columbia).** Gap 0 each; Marie Byrd Land faces the Pacific, and the North American Pacific coast sits on its meridian band. *(Post-war: the Pacific successor states, `DR-23`.)*
- **Alternatives:** Mexico (the Pacific states); Chile (gap 3).

---

## PART 3 — Decisions for you (each logged in `follow-up_questions.md`)

| # | Decision | Default |
|--:|---|---|
| ~~FQ-13a~~ | ~~Mawson~~ **RULED `DR-33`: Australia and Kazakhstan** | ✅ done |
| FQ-13b | **Rothera and Argentina:** `DR-20` vs `DR-22`: does Argentina found Rothera? | unresolved; Rothera keeps both for now |
| FQ-13c | Rewrite the **Shirayuki and Sinheung** Basis on geography (gap 3), keeping the Japanese and Korean founders? | wording only; founders unchanged |
| FQ-14 | **The 15 proposals above:** rule each, one at a time or as a batch; or tell me which to change | Register untouched |
| FQ-15 | **Research pass on the gateways:** verify the gateway statements before any proposal is ruled (`LAW 0-R`)? | not run |

**What I did not do:** change `Founding_Register.md`, any spec, the census or any tracker row (other than the follow-up file); research the gateway facts; decide anything for you.

---

## ROUND 2 — after the developer's rulings (2026-10-03, later the same day)

### 2a. What is now canon (in the Register, `DR-34`)
Port Lockroy **Chile** · Juan Carlos **Uruguay first** · Lazar **Russia (core) and the CIN** · Kunlun **Vostok's stock plus the Sinian Federation** · {{Bunger Hills City}} **Indonesia and Malaysia** · Scott **New Zealand**.

### 2b. ⭐ A correction to my own pools
My Round 1 pools listed **"Russia (pre-war, whole)"** at gap 0 for every zone from +2 to +12. That was wrong for this setting: in the developer's authoritative Russia series (`09 follow-up`) **Russia** is the Moscow-area core (+2…+3), and the east belongs to **Künnarantaiga** (Sakha, Amur, Buryat, Chita, Irkutsk, Primor'ye, Sakhalin, Kamchatka, Chukotka, Khabarovsk, Magadan, Yevrey; +6…+12), **Siberia** (Novosibirsk, Omsk, Tomsk, Tyumen, Krasnoyarsk, Altay, Khakass, Kemerovo, Khanty-Mansiy, Yamal-Nenets; +4…+8) and **Tuva** (+6…+7). **Round 2 pools below use post-war successor states.** The USA and Canada are likewise split (Cascadia, Alaska, Sonora, Colorado, Prairie Federation, Midwest Republic, the CSA, Appalachia, New England, Quebec, Hawaii); Italy is Magna Lombardia and Meridia. The Register keeps pre-war names for rows not yet recast (`DR-23`).

### 2c. The developer's direction, applied (still `proposed` until confirmed)
- **Sejong** (zone −4). **First founders: Chile.** Then English-speaking arrivals. **Then** people invited from **Palmer City** (canon: it has representation from every country) **to translate** the records, logs and manifests of the inherited setting, **and later from Korea** for the same purpose. *Zone check:* Chile gap 0; Palmer City is the same zone; Korea is a later wave, not a founder.
- **Neumayer** (zone −1). **The Netherlands and Austro-Bavaria.** *Zone check:* Netherlands (0) gap 1; Austro-Bavaria (+1) gap 2. Both within the rule. The developer's reason: they could *"make the quickest re-upstart of the setting."*
- **Vostok** (zone +7). **Mongolia (gap 0) plus a successor of the old Russia, not Russia itself.** *Zone check:* Siberia (+4…+8) gap 0; Künnarantaiga (+6…+12) gap 0; Tuva (+6…+7) gap 0. **Which successor?** Vostok sits at 106°52′E, **the longitude of Ulaanbaatar and of Lake Baikal's south end**. In the series, **Buryat, Irkutsk and Chita belong to Künnarantaiga**; Siberia's core lies to the west (Krasnoyarsk is at 93°E). **My reading: Künnarantaiga is the better geographic fit, Siberia a close second.** *(A reading of the map data, not a ruling.)* Kunlun's founding stock follows whatever Vostok is ruled.

### 2d. More options for the rest (post-war names; gap in zones)

**Signy — co-founder** (zone −3; South Orkney Islands; South Africa's partial role confirmed).
- **Brazil (0)**: the large Atlantic coast on the western South Atlantic. *(My Round 1 pick.)*
- **Uruguay (0)**: the Río de la Plata gateway.
- **The UK (2)**: via its South Atlantic territories; the nearest populous European-language coast.
- **Iceland (1)** or **Greenland (0)**: North-Atlantic nations, far but zone-aligned.
- **The Guianas trade union (0)**: the northern South American Atlantic coast.
- **Chile (1)**; **Quebec or New England (1)**: the north-western Atlantic seaboard.

**Denison** (zone +10; Cape Denison, Commonwealth Bay).
- **Australia (0)** *(Round 1 pick; Commonwealth Bay lies almost due south of Tasmania)*.
- **Japan (0)**, **Papua New Guinea (0)**, **Künnarantaiga (0)**: all zone-aligned.
- **New Zealand (1)**, **Korea (1)**, **Indonesia (1)**, **Manchuria (1)**: close.
- A **joint** founding (for example Australia with New Zealand, or Australia with Japan) is available.

**Dumont d'Urville** (zone +9; Adélie Land; *not France*).
- **Japan (0)** *(Round 1 pick)*, **Australia (0)** *(Tasmania is the nearest populous gateway)*, **Korea (0)** *(unified 2111)*, **Künnarantaiga (0)**, **Manchuria (0)**, **Indonesia (0)**, **Papua New Guinea (0)**.
- **Siberia, Mongolia, the Sinian Federation, Taiwan, the Philippines, Malaysia (1)**.

**Zukelli** (zone +11; Terra Nova Bay; *not Italy*; your shortlist re-measured: **Australia 1 · Hawaii 2 · Indonesia 2 · Mongolia 3 · Taiwan 3**).
- **Within the window and not on the shortlist:** **New Zealand (0)**, **Künnarantaiga (0)**, **Solomon Is./Vanuatu/New Caledonia (0)**, **Japan (1)**, **Papua New Guinea (1)**, **Fiji (1)**, **Polynesia (Samoa, Tonga, Cook Is., French Polynesia) (1)**, **Korea (2)**, **Manchuria (2)**, **Alaska (2)**.
- **My pick from your shortlist: Australia**, with **Hawaii** the best island option.

**Cape Adare** (zone +11; *no nation is required*, empty-slot law).
- **Leave it mixed**, or a joint community from the zone-aligned set: **New Zealand (0)**, **Künnarantaiga (0)**, **the Melanesian states (0)**, **Fiji and Polynesia (1)**, **Japan, Australia, Papua New Guinea (1)**.

**Byrd** (zone −8; Marie Byrd Land; the United States is gone in the maps).
- **Cascadia (0)** *(the Pacific Northwest and British Columbia; the post-war recast of my Round 1 "United States Pacific coast and Canada (British Columbia)")*, **Alaska (0)**, **Sonora (0)**, **Colorado (0)**, **Prairie Federation (0)**.
- **Polynesia (Samoa, Tonga, Cook Is., French Polynesia) (0)** and **Hawaii (2)**: Pacific island options.
- **Mexico, the Midwest Republic, the CSA (1)**.

**Rothera** (zone −5; the open question `FQ-13b`). Post-war reading of the ruling's *"North America"*: **Appalachia (−6…−5), New England (−5…−4), Quebec (−5…−4), the CSA (−7…−5), the Prairie Federation (−8…−5)** all reach zone −5 (gap 0).

### 2e. Mirny and the Russia successor (a note for the CST)
`DR-9` says Mirny's founders include **Russia**. Mirny is at 93°E (+6): **Siberia, Tuva and Künnarantaiga all reach +6 (gap 0); the Russian core is 3–4 zones away.** Nothing is changed now (`DR-23`); the recast is a CST task.

### 2f. RULED later the same day (`DR-35`)
**Vostok** Künnarantaiga and Mongolia · **Sejong** Chile, then English-speaking arrivals, then Palmer City, then Korea (translators) · **Neumayer** the Netherlands and Austro-Bavaria · **Kunlun's** stock follows Vostok. **Still open:** Signy's co-founder, Denison, Dumont d'Urville, Zukelli, Cape Adare, Byrd, and Rothera (`FQ-13b`).

### 2g. ROUND 3: RULED later the same day (`DR-44`)
**Dumont d'Urville** Japan · **Byrd** a joint team of first-wave Tepenians from the Peninsula and the Halley coast (not an Upper-Earth nation) · **Signy** South Africa and Brazil · **Zukelli** Australia · **Denison** Australia · **Cape Adare** mixed (empty slot) · **Palmer City, Amundsen Station, Concordia** not nation-based · **Shirayuki, Sinheung** the Jeju-do allocation plus geography as an added factor · Rothera's Argentina stays. **Every Register row is now ✅.** Open: `FQ-20` (Australia's share) and the unresearched gateway claims (`FQ-15`).
