# ULM Files — Full Mistake Audit (2026-10-01)

**Scope.** Every ULM methodology file, every `Test_Runs/` file, and every file in every prepared city's pass folder
(Davis, Zhongshan ×2, Shirayuki, Mirny, Sinheung, and the datasheet/Pre-Trip folders for Casey, Kunlun, Vostok,
Dumont d'Urville, Denison, Cape Adare, Zukelli, plus 34 stub READMEs). ~168,700 lines in 24 partitions, each read
**in full, line by line**, by a dedicated reader against the same brief (rules 1–7 below). Coverage tables are in each
partition section. **Nothing has been edited yet.** Every fix below waits for the developer's approval.

**Rules checked:** (1) `DR-19` station/operator never a cause · (2) `DR-24` infrastructure facts are fine ·
(3) `DR-25` records, never a tradition/institution · (4) the Founding Register is the only source of founders ·
(5) founding stated on the city's own geography, never by comparison · (6) Background-Lore vignettes / Course of
Events never an input · (7) real-site history never a cause.

**Tracker:** `Station_Heritage_Removal_Tracker.md`. This file is the itemized worklist behind it.

---

## PART A — DECISIONS THAT GATE MANY LINES (developer's call)

> ### ✅ RULED 2026-10-01 — `DEVELOPER_RULINGS_LOG.md` `DR-26` … `DR-29`
> - **D1 → `DR-26`:** newcomers **can inherit the station's research, equipment, techniques and results.** Zhongshan's
>   habitation continuity stands. Every "research heritage / research tradition / testbed tradition" fix in Part D
>   becomes a **rewording** to *"inherited the station's research results, equipment and techniques"*, **not a
>   deletion.** That covers Zhongshan §15, Janbogo Run 9 Family A, Davis "inherited expertise", and the Zhongshan
>   magnetic-observatory zone (inherited equipment and technique). Still struck: "organic", "heritage" as a word of
>   identity, "administration", and every city-versus-city founding contrast.
> - **D5 → `DR-27`:** raw records are **moved to `Archive/ULM_Records/`, not edited.** Every Part D item that sits in a
>   T8 reader file, a T8 round record, a superseded file, an `_archive_` folder or a `Test_Runs/` run folder or prep is
>   closed by the move.
> - **D2–D4, D6–D8 → `DR-28`:** recommendations adopted as written.
> - **`DR-29`:** **Davis stays as is** (Australian founding on geographic proximity): the Part C Davis rows and the
>   Part D items that strike Davis's Australian founding-wave ties (C_Davis_2 M1–M3, C_Davis_5 M4–M6) are
>   **withdrawn**. **Shirayuki stays** (Japanese founding population). Its spec's **Sejong** and **Lazar** lines go to
>   those cities' **revisits**. Lazar is added to the revisit list.

| # | Question | Lines affected | Recommendation |
|---|---|---|---|
| **D1** | **Zhongshan's 481-year continuous Chinese/Sinian habitation (2083–2564).** It is stated in the law file (`No_National_Stereotypes.md` L17), in `Specs/Zhongshan.md` (L142 "habitation **and administration**", L150), and DR-21 says *"in the 2500s, it would still be the Chinese who would have control over Zhongshan Station."* But `DR-24` lists *"continuous X presence"* and *"a statement of continuity"* as not allowed. Does the pre-2564 continuity stand? | ~120 lines: Test_Runs Tri-Cities, Runs 2–4 ("joined, not founded", "the only city whose thread was never cut", "recognized, not granted"); both Zhongshan passes (I-2, "nothing here ever had to start over"); OBSERVATIONS M-35/36 | **Keep the habitation continuity** as your ruled exception (it's in your law file and DR-21's "still"). **Strip everything that rides on the station:** "research heritage continuous from the founding station", CHINARE heritage/practices, "administration" (a living institution, DR-25), "organic", and every Zhongshan-vs-Sinheung/Shirayuki contrast (rule 5). |
| **D2** | **Real namesakes and real-site history as identity.** Saints named after the real site's explorers (St. Carsten/Borchgrevink, St. Jules/Dumont d'Urville, St. Douglas/Mawson, Hut Point remembrance for Scott/Fort McMurdo); city name kept from the station (Mirny "Russia had been in Antarctica since the beginning", the Soyuz placeholder, Zhongshan "political heritage", Davis "the founders CHOSE his name"); Cape Adare's "precedence" identity (Borchgrevink 1899) | Cape Adare Runs 7–8 (whole pass), Janbogo Run 9 (namesake family), Davis Step 1 + Reconciliation §6, Mirny Step 1, Sinheung spine, datasheets | A Saint already canon in `National_Holidays.md` stays as **Federation-wide** veneration. A city's **identity, core value, founding logic or name-meaning is never derived from its namesake or the real site's history.** "Keeping the name" is a naming fact only; no meaning is built on it. |
| **D3** | **Antarctic station life as a real-world comparable** (`DR-15`): Midwinter Day, USAP chores, station-crew studies, greenhouses, the ASMA/ASPA management plan, resupply schedules, a station home-brew ban, Signy's whaling station, Halley's relocated stations, Marambio's runway | Zhongshan ×2 (ASMA governance, Borrowed Form), Davis Step 3, Sanay Run 11, Mountain Pass Run 10, Extent files | **General** polar-station practice anywhere is an ordinary comparable (DR-15). **Anything about the station at the city's OWN coordinates** (its operators' joint management, its 2008 fire, its resupply ship, its ban, its observatory zone) is that site's history → not an input. Physical facts (runway geology, ice-flow evidence) stay. |
| **D4** | **`Resettled` modifier and `Installation` type** on station sites | Davis 00_Frame/01_Inherited ("ground 1 FALLS"), Mirny Step 0 readers, runbook §C.8b, `01` L113–117/L135, PRE-TRIP L249, MASTER L100–101 | **Close it under DR-19:** a real station's occupancy is never a prior population, and a city is never typed `Installation` because a station stood there. Inherited records stay admissible as records. |
| **D5** | **Raw records** (T8 reader files, `0Xb_T8_Rounds` files, `_archive_` folders, `Test_Runs/`) | roughly half the lines in this audit | Your standing order is "strip it out." **Strip everywhere, including records and archives,** unless you say otherwise. Where a reader suggested a dated annotation, the fix below has been switched to a plain strip. |
| **D6** | **City-to-city ties resting on census tiers** (Shirayuki↔Vostok "both Japan-tiered", Zhongshan↔Kunlun "shared Chinese-origin population", Sinheung↔Mountain Pass via Korean tiers at Kunlun/Vostok) | Shirayuki, Zhongshan, Sinheung passes; `National_Medical_and_Care_Institutes.md` L104–111 | **Leave them until the post-ULM census review** (DR-23). Strip only the station-based phrasing (the CHINARE pairing). Never delete the tie itself ([[never drop a city connection]]). |
| **D7** | **Founder lines for UNRULED cities** that come straight from the station (Vostok spec L128 "Russian… given the station's Soviet/Russian character", Kunlun L168–170 "CHINARE exiles", Denison L277–279 "Mawson's own base", Lazar "founding Russian demographic") | specs + datasheets + Naming-Drift guideline | In the ULM and datasheet files, replace with "UNRULED (Founding Register)". The spec lines themselves join the revisit list (R-items), because only you rule a founder. |

| **D8** | **"Inherited institution / capacity" wording.** On 2026-10-01 (`DR-25`) you ruled that the Division of Industry's *"inherited `[xyz]` institution/tradition/etc"* citations **are fine**, apart from the word "tradition". The readers' brief counted a living inherited institution as a mistake, so these were flagged against your ruling: `16` L2154 Mirny "inherited Soviet/Russian institutional research capacity", L2230 Casey "inherited Australian Antarctic Division capacity", their datasheet copies, Sinheung "deep institutional roots", and Zhongshan "administration" | ~10 lines | **Honor DR-25: keep the "inherited capacity/institution" wording.** Strip only the words "tradition" and "heritage" (e.g. 16 L2154/L2230 "Heritage research" → "Research"). The Janbogo Run 9 "guild continuing the founding station's scientific mission" stays a mistake, because it passes on a *mission*, which is a tradition. |

**Also noted (no decision needed):** the runbook's G6 address list no longer contains Background-Lore (fixed
2026-10-01; readers working from older line numbers flagged it). The Mirny Step 0 "vignettes move to Step 1" choice
(2026-09-29) is overridden by the later "not canon, never an input" ruling, so every Step 1 vignette schedule is struck.

---

## PART B — FIX FIRST: THE UPSTREAM SEEDS IN THE METHODOLOGY

These are the instructions every future city pass reads. Downstream lines cannot stay fixed while these stand.

1. **`02_Generators_Capability_and_Symbols.md` G7.**
   - L239–241: G7 hands over "the actual station, its actual nation, its actual founding… Highest surprise value". Replace with "The actual physical site at the location's coordinates: terrain, ice, climate, access, and any physical infrastructure the founders inherited. Where the site carries a real installation, its name, operator and start year are a coordinate and an infrastructure record only. They are never a cause of the location's founders, identity, culture, institutions or ties."
   - L122: rename the table row "Real-world physical site" and re-rate it.
2. **`00_RUNBOOK.md`:**
   - L38–39: Step −2 1a "admissible G7 attribute"
   - L772: §C.1 "Real-world basis (G7)"
   - L1956: §C.8b, Vostok "Settlement + Installation"
   - L292: "Zhongshan-organic-vs-Sinheung-allocated"
   - L2141–2143: §C.9c, "Zhongshan China-founded — by the Jeju-do allocation". Replace with "Zhongshan Chinese-founded (Sinian Federation) on its own geographic and time-zone access — Founding Register."
   - L2214–2217: §C.9d, "TWO Japan-founded cities… Sayowa"
   - L2638–2640: Step 3.7, "Antarctic Treaty management plan… highest-value source for Phase 5 and Phase 7"
   - The **S05 stepwise card** (L105–107) carries the same Step 3.7 line; fix the runbook first, then re-extract the card.
3. **`05_The_Input_Contract.md`** L675–679, L699–703 and L772 let Course of Events "be read as a prompt" (DEMOTED). **This is the seed of every rule-6 violation in every pass.** Change it to EXCLUDED: never read, cited or scheduled.
4. **`03_The_Phase_Spine.md` L629–634 and `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` L943–947** make `City_National_Connections.md` and `City_Cross_Subnet_Relationships.md` required Phase 5 reading. Both files are partly built from the vignettes and carry heritage ties (see Part C). Route Phase 5 to `Highways.md` / `Airports.md` / `Ports.md` until those two files are cleaned.
5. **`ULM_Input_Required_Reference.md`:**
   - L261: the T1-G7 row hands over `Based on:` ("Davis Station (Australia / Australian Antarctic Division)") as what "anchors" the city.
   - L348–349: "a research station that became a place people are from… itself a finding".
6. **`PRE-TRIP_INSPECTION_RECIPE_TRIAL.md`:**
   - L250: "every station-founded city"
   - L219: the DR-7 row forbids only "character"; add DR-19/24/25 rows.
   - L249: Resettled (D4).
7. **G4 has no Register qualifier.** Add "Founders: the Founding Register only" at:
   - `05` L96, L198, L489, L649–650
   - `Run_Modes_Warm_and_Cold.md` L83, L101
   - `S02` L83
   - `ULM_Piece_Index.md` L109, L111
   - `Test_Runs/COLD_RUN_CHECKLIST.md` L309–310
   - `Test_Runs/RESUME_HERE.md` L594–596, L674–675
8. **`Naming_Drift_Typology_GUIDELINE.md`** (instances declared "canon and closed", L128):
   - L74: Lazar's "founding Russian demographic"
   - L77: Abowasa "Aboa (Finland) + Wasa (Sweden)… settlements coalesce"
9. **`Corpus_Reference_Sheets/No_National_Stereotypes_Quick_Reference.md`** M1–M6. This is a **law-file copy**, so it changes only together with I-2/I-3 on `No_National_Stereotypes.md`, with your approval:
   - "founding nation" used to mean the station-builder
   - Zhongshan "Jeju-do allocation"
   - "for most cities they differ"
   - "the census" as the founder source
   - the Sayowa = Japan worked case
   - "a naming choice"
10. **`Archive/ULM_Records/Test_Runs/2026-09-03_Shirayuki_Run15_Cold/maps/R3/`** tags the `Station_to_City_Map.md` and `Overview.md` operator/country columns as admissible G7/G4.

---

## PART C — SOURCE FILES OUTSIDE THE ULM THAT THE READERS TRACED THE ERRORS TO

Not in the read scope, but each was named, with a line number, as the origin of a pass error. Specs for the 10 ruled-out
cities are already on the revisit list. These others are new:

| File | Line(s) | Problem |
|---|---|---|
| `Specs/Mirny subnet/Davis.md` | L8, L62, L129 | "Australian founding-wave **heritage** with… Casey and Mirny"; "one of the three Australian Antarctic stations alongside Mawson and Casey"; "three cities carrying Australian founding-wave heritage" (rules 1, 5). Re-ground as subnet relation, don't delete the ties |
| ″ | L131, L179/L234, L190 | namesake "carries specific weight in Australian Antarctic culture"; Mawson "both named for Australian Antarctic figures"; "research, the founding heritage" (rules 1, 3) |
| `Specs/Mirny subnet/Shirayuki.md` | ~L17, L27, L29, L31, L35, L77 | "not an organic real-station inheritance like Sayowa's"; Lazar "coalescing with the… Russian Novolazarevskaya station"; Sinheung "Russian"; "Korea… footholds… Janbogo and Sejong"; "a second Japanese city (alongside Sayowa)"; "Sayowa's own JARE-inherited Japanese identity". Also the L25 find-and-replace damage: "real-world station name 'Shirayuki' (Sanskrit…)" should read Bharati |
| `Specs/Mirny subnet/Sinheung.md` (Legacy) | — | "rather than through organic station inheritance" |
| `Specs/Mirny subnet/Mirny.md` | L150–154, L229 | "Primarily Russian exiles"; "Russia had been in Antarctica since the beginning"; "non-founding status" (vs DR-9) |
| `Specs/Mirny subnet/Zhongshan.md` §15 + `Division_of_Industry/16_Per_City_Three_Tier_Run.md` §18 | — | "the research heritage is continuous from the founding station" (DR-25) |
| `16_Per_City_Three_Tier_Run.md` | L2154 (Mirny), L2230 (Casey), L2406 (Vostok), L2497 (DdU) | "…institutional research capacity. Heritage" and "…AAD capacity. Heritage research" (D8: drop only "Heritage"); Russian "liturgical language of science" for an unruled-founder city (D7); "the most distinctively francophone-speaking city" for a city ruled ≠ France |
| `City_National_Connections.md` | L6–8, L18–20, L129, L268, L384, L524 | built from the Historical Vignettes; "Japanese-heritage family correspondence"; "Australian-heritage network"; "Shirayuki's own Bharati-Station-descended founding"; "Sayowa's own JARE heritage" |
| `City_Cross_Subnet_Relationships.md` | L115, L118, L125, L139 | "dramatized as a Course of Events chain"; "Shared Australian Antarctic naming heritage"; "real-world namesakes had a direct historical…" |
| `City_Relationship_Database.md` | L323–330, Sinheung row | Mirny "despite being Russian"; "Real station: Sinheung Station (Russia)"; "one of Tepenia's three Korean-founded cities" (Sejong) |
| `Local_Cultures/Mirny_Subnet/Sinheung.md` §23 | — | "Zhongshan's claim was organic and merely confirmed by Jeju-do… inherited an actively operating Russian research station" |
| `World_History_Reference.md` | L240 | "Every real Antarctic research station became a Tepenian city": a fact, but it is the cited basis for typing cities `Installation` (D4) |
| `National_Holidays.md` | Hut Point line | "Hut Point remembrance ritual… Scott/Fort McMurdo" (D2) |
| `Specs/Mirny subnet/Vostok.md` L128 · `Kunlun.md` L168–170 · `Specs/Janbogo subnet/Denison.md` L277–279 · `Lazar.md` | — | station-derived founders for unruled cities (D7) |
| `Research_Logs/Janbogo_Research_Log.md` | README row | "Jang Bogo Station's real staffing/scale and its historical namesake" (D2) |
| `Inspirational-Influences.md` | Mirny, Sinheung picks | Yakutsk/Nizhny Tagil and Volgograd; check whether they were picked because of the Russian station |

---

## PART D — THE ITEMIZED FINDINGS, BY PARTITION

Format: `file:line` · quoted text · rule · replacement. Each partition ends with **OTHER** (non-heritage errors:
stale counts, broken paths, arithmetic, British spellings). Those are a separate, lower-priority cleanup and are
listed so nothing is lost.


### U1 — runbook, 01, 02 (full coverage: 00_RUNBOOK 1–3160, 01 1–582, 02 1–794)
MISTAKES
1. 02:239–241 G7 def "actual station, its actual nation, its actual founding… Highest surprise value" → physical site only; name/operator/start year coordinate+infrastructure record only. (Contradicts 02:257 block.)
2. 02:122 G7 row "Real-world inspiration | highest…highest" → rename "Real-world physical site", re-rate like G2, footnote.
3. RUNBOOK:38–39 Step −2 1a "basis name … admissible G7 attribute" → "key to climate and physical-site files (coordinate only, DR-19), and key to every conclusion written before the rename."
4. RUNBOOK:772 §C.1 "Real-world basis (G7); founding mechanism (G4)" → "Real-world basis: coordinate and physical-infrastructure facts only (G2/G5; DR-19, DR-24) — never founders or identity · founding mechanism (G4), from the Founding Register".
5. RUNBOOK:1956 §C.8b Vostok "Settlement + Installation — a research station that became a place people are from" → "Settlement — type from the city's own canon; real station = coordinate (DR-19); inherited infrastructure is G2 (DR-24), not a type."
6. RUNBOOK:292 "(the Zhongshan-organic-vs-Sinheung-allocated distinction)" → delete / "(including its sharpest specific claim about the subject's own founding allocation)".
7. RUNBOOK:2214–2217 §C.9d "Tepenia has TWO Japan-founded cities — Shirayuki … and Sayowa" → generic worked case or delete. Sayowa open.
8. RUNBOOK:2638–2640 Step 3.7 "unread Antarctic Treaty management plan … highest-value unread source for Phase 5 and Phase 7" → "admissible for physical-site facts only, DR-24; never for relations or institutions, DR-19".
AMBIGUOUS
A1 RUNBOOK:2068 Stations/ "G2/G7 physical station facts — COMNAP | 1, 5" → G2/G5 infrastructure only?
A2 RUNBOOK:1645 Port Lockroy "40% heritage-themed … cite with caveat" → if from Base A museum, ⛔ do not cite.
A3 RUNBOOK:2072 Vostok_Genetics_Research DNA computing → derived from real station program?
A4 01:113–117 "founded as installation… Settlement + Installation" → add "(a city merely sited where an installation stood does not qualify — DR-19)"?
A5 01:135, 293 Resettled "what did the second population inherit…" → append "(from a station's people: records only — DR-25)"?
A6 02:505 "someone who has organically what this location was only allocated" (PEER-FREE table) → delete / move.
OTHER
- RUNBOOK:2141–2143 "Zhongshan China-founded — by the Jeju-do allocation and the census" → Zhongshan Chinese (Sinian Fed.) per Register; only Shirayuki/Sinheung via Jeju-do.
- 02:243 "Governed entirely by Real-World_Basis_Extrapolation_Method.md" vs DR-14 → "ULM Step 3 research (DR-14/15)". Same DR-14 issue: 01:267, 01:500, 02:214, 02:550, RUNBOOK 2572, 2624, 2629.
- 02:709 "eleven planetary symbols" → ten (02:143, RUNBOOK:1745).
- 02:696 "all 35 outer cities" vs RUNBOOK:1747 "34 of 35".
- 02:309 stale xref to Step 3.7 "measures five of nine completed districts".
- 01:514 "check the most recently written first" — revoked RUNBOOK:2901.
- 01:413 "Must be differentiated against siblings" vs LAW OF ONE LOCATION.
- RUNBOOK:2712 stale anchor "L2137–2138" → L2135–2136.

---

### U2 — 03 spine, 04 gates, 05 input contract, 06 provenance, PRE-TRIP recipe (all full)
MISTAKES
M1 03:629-634 + PRE-TRIP:943-947 Phase 5 MUST-OPEN "P City_Cross_Subnet_Relationships.md" / "P City_National_Connections.md" (MAPPED, sent to readers). Those files are built from vignettes/Course of Events and carry heritage ties: CNC L6-8, L18-20 (built from vignettes), L129 "Japanese-heritage family correspondence", L268 "intra-subnet Australian-heritage network"; CCSR L115, L118 "already dramatized as a Course of Events cross-subnet chain", L125 "Shared Australian Antarctic naming heritage", L139 "real-world namesakes had a direct historical…". → INADMISSIBLE; routes from Highways/Airports/Ports only (or carve-out to infrastructure section). ALSO fix those source files themselves.
M2 05:675-679, 699-703, 772 Course of Events "Suggestion" files "may be read as a prompt" / DEMOTED → EXCLUDED, never read/cite/schedule (rule 6).
M3 PRE-TRIP:250 "for every station-founded city" → "for every city sited at a real station's coordinates".
AMBIGUOUS
A1 05:96, 198, 489, 649-650 G4 founding condition admitted without Register-only qualifier → add "Founders: the Founding Register only…never station/operator/start year (DR-19)".
A2 03:1060-1062 "anchors robot culture in founding-nation threads" → "in the founding population the Founding Register names".
A3 03:900-908 heritage sector failure keeps "single 1899 hut" as signature instance → add rule-7 note.
A4 05:330-339, 763 "first place where Y happened… differentiation for free" → carve-out for real-site firsts?
A5 05:365-367, 267 "oldest known particular is a floor on age" → "never the real station or its history"?
A6 PRE-TRIP:219 DR-7 row forbids only "character" → add DR-19/24/25 rows.
A7 PRE-TRIP:249 Resettled "Most Tepenian cities sit on a real pre-war station" parked → close: prior station occupancy never qualifies.
A8 03:335-336 + PRE-TRIP:904 "Stations … background only" → add DR-24/DR-19 qualifier.
A9 06:149 Zhongshan Run 4 "what does 'the claim' mean" → territorial claim? (rule 7)
OTHER
O1 04:573-579, 06:115-116, PRE-TRIP:8-10 "non-binding" vs 2026-09-11 T1–T8 MANDATORY.
O2 04:141-144, 488, 496, 146-147 sibling tests still live vs in-run ban.
O3 counts: 03:484 "37", 03:700 "38", 03:1166 "34 of 35", 04:433 "thirty-seventh", 05:615 "34", 05:722 "35 of 38".
O4 03:1195, 04:564-565 "never run" stale.
O5 04:920, PRE-TRIP:1061, 1088 "3/1/5" sums to 9; 04:910 "2-of-8" vs "3 of 8".
O6 PRE-TRIP:800 dispatches struck vision notes (PRE-TRIP:251).
O7 03 "Asks:" split: L322/354, 618/650, 754/781, 841/887.
O8 05 §6.1a,b,d,c order; 05:620 "§6.0" → 02 §6.0.
O9 06:369 "05 is 708" (810); 06:286 stale coords.
O10 06 "sixteen gates" L200,212,214,226,228,239,252,267,270 → seventeen.
O11 04:725 "§9.1/§V.2.4" missing file name (PRE-TRIP).

---

### U3 — ULM trackers/inputs: Extent_and_Area_APPROACH, Extent_and_Density_Per_City, Location_Data-Input_To-Do, MASTER_Process_Tracker, ULM_Input_Available_Audit, ULM_Input_Required_Reference, ULM_Run_Progress (all full)
MISTAKES
M1 ULM_Input_Required_Reference:348-349 "Settlement + Installation per §C.8b — 'a research station that became a place people are from'; the dual assignment is itself a finding" → "All 37 entries in this audit are Settlement type. Settlement adds no inputs beyond the above. Modifiers do:" (drop the C.8b reading; runbook §C.8b fixed per U1 M5)
M2 ULM_Input_Required_Reference:261 T1-G7 "Real-world inspiration DESIGNATION — which real case anchors it" address Specs/ Based on: (Based on: = "Davis Station (Australia / Australian Antarctic Division)") → "Real-world SITE designation — the coordinate and physical site only. ⛔ DR-19: the station named in Based on: and its operator/nation are a coordinate, never a generator; read only the place-name and coordinates."
M3 MASTER_Process_Tracker:233-234 "who a real-world site's population actually is, or their real cultural practices" (assistant paraphrase) → "who a city's founding population actually is (per the Founding Register), or that people's real cultural practices".
AMBIGUOUS
A1 Extent_and_Density:192-194 Cap Prud'homme convoys to Concordia corroborate Hwy 183 — delete?
A2 Extent_and_Density:326-327, 386-387 Signy whaling station precedent (rule 7).
A3 Extent_and_Density:426-433 Marambio runway "aviation identity IS the geology" (R-2 open).
A4 Extent_and_Density:561-567 Halley buried/relocated stations precedent.
A5 MASTER:95-97 DR-7 "what a lineage left behind" — clarify infra+records only.
A6 MASTER:100-101 Resettled prior POPULATION vs OCCUPANCY — close per DR-19.
A7 ULM_Run_Progress:70-71 "used to name two Japan-founded cities" — which?
A8 Location_Data-Input_To-Do:469, ULM_Input_Available_Audit:303 Amundsen "research and relay outpost, not a residential city" — USAP program carried over? (census)
A9 Machu Picchu Airport (Audit:376-377, Required_Ref:192) — station-derived infrastructure naming.
OTHER
- Abowasa "BLOCKED on founding-nation fix … First Interwar turnover history": Audit:16, 86, 93, 306-314, 426; To-Do:456, 468 → "Founders ruled Italy + CIN (Founding Register, DR-22); the old Finland/Sweden premise and the Aboa+Wasa name await rework (R-16)." Audit:302 vs 92; :306 "four gaps" lists three.
- To-Do:150 Kowloon ~50,000/km² wrong (1,255,000).
- To-Do:133-137 vs :86-101 extent bounds contradiction.
- Sayowa "~4–5 km² island" → ~1.5 km²: APPROACH:48, 88, 182; To-Do:84, 135; Audit:227.
- Sinheung "~34 km² hills" → ~40 km² (34 = Schirmacher): APPROACH:48; To-Do:84; Audit:228.
- APPROACH:175 "nearly 3×" → ≈1.9×.
- APPROACH:108 Belgrano SHELF-SPREADING vs Density:623 Bertrab nunatak.
- Density:582 Mirny "0% ROCK" vs spec "coast rocky".
- APPROACH:176, 358 "six island-capped… hard ceilings" → eleven, not a ceiling; :337-338 stale; Audit:199.
- Density:517-519 Denison "deliberately held" stale.
- Required_Ref:551-553 "nine… remaining 29" → 13 / 25.
- Extent 0/37 open: To-Do:56, 108-111; Audit:11, 77, 201, 293; Required_Ref:303 vs closed.
- Required_Ref:116, 117, 119, 179 spec path → Specs/<Subnet> subnet/<City>.md.
- Audit:84, 88 air 10/3/23 = 36 vs To-Do:239 11/3/23.
- climate records stale: Audit:173-176 vs 114-117,134; To-Do:196-200.
- To-Do:231-233, 340-349 Denison founding stale vs :62.
- MASTER:9 Davis complete vs :32 step table; :510; :434, 438, 612 counts; :480 3/8→4/8; logs 5/38 :288, 438, 612; :512 Mirny log; :402 ▶ Shirayuki.
- MASTER duplicate R-4, R-12 IDs (:104, :32, :88 vs :259, :266).
- MASTER Sinheung 17 vs 21 files; Shirayuki 23 vs 38.
- ULM_Run_Progress RESUME HERE :56-58, 188-190 Shirayuki stale; :317, 321, 361, 421 totals.
- MASTER:431-435 subnet longitude ranges.
- Required_Ref:294, 300 City_Vision_Notes vs struck.

---

### U4 — ULM top-level files + Stepwise_Execution cards (45 files, all full)
MISTAKES
M1 Stepwise_Execution/01_Spine/S05_…:105-107 (= RUNBOOK L2639) Antarctic Treaty mgmt plan "highest-value unread source for Phase 5 and Phase 7" → "(Run 3 left seven.)" fix runbook then card.
M2 Naming_Drift_Typology_GUIDELINE.md:74 Lazar "founding Russian demographic was overtaken by later American, German, French, and Brazilian immigration" (L128 says instances "canon and closed") → "Lazar ← Novolazarevskaya — a long name shortened under demographic turnover (founding population: UNRULED — see Founding_Register.md; the spec's national attribution is not adopted here)". Spec Lazar.md carries same claim (outside).
M3 Naming_Drift:77 "Fusion | Two adjacent settlements coalesce… Abowasa ← Aboa (Finland) + Wasa (Sweden)" → "Abowasa ← Aboa + Wasa (the two real stations at this coordinate — a coordinate only; founders per Founding_Register.md)". Note R-16 rename pending.
(M4 Shirayuki ← Bharati site L80: fine.)
AMBIGUOUS
A1 S05:62-64 (RUNBOOK L2596) angle "founding" — never the real station's founding?
A2 Naming_Drift:76 "Sanay ← SANAE (South African National Antarctic Expedition)" — operator acronym as name origin OK?
A3 Naming_Drift:110 "St. Douglas at Mawson is a live cult of memory" — Douglas Mawson namesake as identity? canon?
A4 Run_Modes:83, 101; S02:83; ULM_Piece_Index:109, 111 "founding and events" → "founding — Founding_Register.md only — and events (never Background-Lore vignettes or Course of Events)".
A5 G13:40 "UNIVERSE REPO — wins on When · Where · Who" — overrides Register on founders?
A6 ULM_At_A_Glance:33 "Stations" carve-out.
A7 Mechanical_Extraction_Field_Guide:318 transcribe from 16_Per_City_Three_Tier_Run Notes (AUDIT_AGENDA:61 says those Notes read namesakes as character) — warn.
A8 ULM_Diagnosis:60-66 census Primary = founding nation reasoning (census: deferred).
A9 G05:36-38 swap test "Pick the partner" — peer-free form?
OTHER
1 Datasheet_and_PreTrip_Tracker:26 "8 cities (9 folders) — all seven datasheet cities" → "seven of the nine datasheet cities (all except Cape Adare and Zukelli), plus Zhongshan".
2 Datasheet_and_PreTrip_Tracker:116 "±3 window ruled Notable-only… (DR-19 pending log)" — DR-19 is now logged (window is part of DR-19 per my log) — update "pending".
3 ULM_At_A_Glance:22 "5 dispositions" → 6 incl. declined.
4 G11:39 "Five dispositions" (from 04:241) → fix 04, re-extract.
5 S01–S12 origin line ranges stale (+37–45): S01 2427–2452, S02 2453–2520, S03 2521–2537, S04 2538–2566, S05 2567–2661, S06 2662–2751, S07 2752–2884, S08 2885–2920, S09 2921–2960, S10 2961–2984, S11 2985–3044, S12 3045–3135.
6 G17:4 "lines 399–567" → 399–416.
7 S07:63 "CANON IS TWO TIERS" → FOUR.
8 RWBEM_Progress:96 + RealWorld_Basis_Input_Availability:44-45 list struck City_Vision_Notes/.
9 G07:51 "Gate 6 runs LATE — at Step 7" vs terminal; also Stepwise README:73-74, ULM_Piece_Index:68.
10 ULM_At_A_Glance:35 "Davis_Geosciences" → "<City>_Geosciences_Research/ (where one exists)".
11 README:198 "Sixteen techniques" → 18; Cultural_Synthesis_Input_Availability:4 "17 plus one".
12 Stepwise README:115 "M-139" stale.
13 Stepwise README:113 "37 cities" → 38.
14 ULM_Diagnosis:82 "4 of 37" dated.
15 Datasheet tracker:33 Amundsen "Not a city" yet counted in 38.

---

### U5 — Disciplines, Corpus_Reference_Sheets, Pre-Contamination_Reviews (20 files, all full)
MISTAKES (all in Corpus_Reference_Sheets/No_National_Stereotypes_Quick_Reference.md — LAW-FILE COPY, developer approval needed)
M1 L11–12 "were the founding nation swapped" → "station-builder nation".
M2 L26–28 "Zhongshan's Jeju-do allocation gives it continuous single-population habitation instead" → Zhongshan is NOT Jeju-do (Register: Sinian Fed. access); delete Zhongshan clause.
M3 L32–33 "Two different nations, and for most cities they differ." → "Two different questions. Where they happen to name the same nation, that comes from geography and access, never from continuity with the station. Founders come only from the Founding Register."
M4 L38 "Established by | canon: the census, tier tables, per-city founding rulings" → "the Founding Register — the only source of founders".
M5 L57–59 worked case "Shirayuki, Japan 36.27%, and Sayowa, Japan diluted to 2.71% — same stock" → Sayowa open; delete or use Register-ruled pair.
M6 L68–69 "The founding nation may appear as a bare fact (tier tables, 'the station was founded by X,' a naming choice)" → "The real station, its builder/operator and its start year may appear as bare facts about the physical infrastructure the exiles inherited — never as the reason for the city's founders, identity, culture or name." Also L74, L77–78 "founding nation" → "station-builder nation".
AMBIGUOUS
A1 NNS L26 "Byrd fell out of the chain and was abandoned" — canon or real-site history? (rule 7; Byrd unruled)
A2 RWBEM L206–208 "What stays fully usable: pure physical/geographic facts" — add DR-24/25 allowances?
A3 RWBEM L48–49 angle "founding" — exclude when pick is the city's own GPS station?
A4 RWBEM L443–444 "isn't nation-founded the way outer cities are" → "the way many outer cities are" (Dome Fuji, Fort McMurdo, Sayowa)
A5 Shirayuki_Pre-Contamination_Review L376, 739–740 Background-Lore WITHHELD then reopened at Step 7 for comparison — exclude Background-Lore entirely (rule 6)?
OTHER
- Cultural_Synthesis_Techniques: counts 18/19/216/228 (L896,905,914,918,935), "eleven" vs "ten" planetary (L903–904 vs 959); L651 "all fourteen" (file has 18); L718–719 "including including"; L746–753 district worked instances left in full.
- 00b L132 "both copied" vs three; L141 "Leo's Fashion".
- 00d L132–133,151,170 district names; 00f district names (612–619, 649–650, 712–725, 758–763, 769–782, 797–801); 00f unmet contradiction L709/724 vs L820 (copied in QA sheet L80–82, Review Panel sheet L241); 00f L303–306 table vs L372.
- City counts 37 vs 38 vs 35 vs 41 across sheets (Differentiation L6/85; QA L5; RP L5; DoI L38/109/141 vs 137/139; RWBEM L360, 365, 419).
- RWBEM L442–443 garbled "with the location with a founding population".
- NNS L37 "settled the city in 2564" → "from 2564 onward".
- Shirayuki review L725–726 893 vs 871 sum.
- Casey review L140,178,181,184 old raw percentages (82.7/45.2/30.5 → 85.0/43.7/31.5).

---

### T1 — Test_Runs Tri-Cities (Run1), Run2 Zhongshan, Run3 Zhongshan Cold, Run4 Zhongshan Methodology-Delta, CapeAdare Run7 Cold + Run8 Warm, Highway37 Run6/00 — 44 files all full
⚠ **CLUSTER Z depends on decision D1.** The reader struck the 2083–2564 habitation continuity itself, under DR-24's "continuous X presence". If D1 keeps that continuity, only the station-riding parts of these lines are struck: CHINARE heritage, "research heritage", "administration", "organic", and the Shirayuki/Sinheung contrasts. [FR-Z] = "Founded in 2564 by Chinese exiles (state: the Sinian Federation), on China's immediate geographic and time-zone access to Prydz Bay (Founding Register; DR-21). Built on Zhongshan Station's physical infrastructure (DR-24)."
CLUSTER Z (Zhongshan continuity/"joined not founded"/"confirmed not won"/"recognized vs granted"/CHINARE heritage):
 Tri-Cities/01:94 "Confirmed — already theirs | Inherited — must keep proving | Allocated to emptiness" → Register entries; :166 "on Russia's foundations" delete; :167 "a claim that has to keep proving itself" delete.
 Tri-Cities/OBSERVATIONS:327-334 → Register entries.
 Run2/01_Zhongshan:33-34, 92, 93-94, 110, 113-116 (Z-1 "only city whose thread was never cut"), 127, 139-140, 153-154, 165-166, 168-170 (Z-2 "residents did not arrive; they continued"), 198-199, 276-277, 309, 362-365, 378.
 Run3/00_Observations:117 vignettes "Deferred to Step 7" (rule 6) → never; :363-374 M-6 continuous habitation.
 Run3/01:35-39, 114, 202-205, 209, 211.
 Run3/02:106-141 Finding I "Zhongshan was not founded. It was joined." delete; 149, 152, 209-211, 298, 322, 502-508, 517-518, 520-522, 551; :174-176 Palmer founding-wave nations (census).
 Run3/03:147, 150, 219-225, 234-237.  Run3/05:24, 111-121, 325-330.  Run3/06:18, 175.
 Run4/01:39, 47-48, 149-151, 169-170 "Chinese icebreaker routes with pre-exile heritage", 190-197, 199-202 (compare Shirayuki), 204-209, 260, 318-325.
 Run4/02:13-17, 23-35, 37-40 "CHINARE-heritage practices survived", 104-106 "continuing CHINARE heritage", 128-129, 194-196, 228.
 Run4/03:21-24, 29-34 CHINARE Saint, 48-56, 133-136, 161.
 Run4/04:33, 67-72, 75-77, 143 "continuing CHINARE heritage | Inflected (a national tradition continued)", 144.
 Run4/05:11-12, 42-48, 106-110.  Run4/06:104-108.  Run4/07:73-76.  Run4/08:37-38, 58-59.
 Run4/09:32-41 (quotes Sinheung culture sheet "This city's Korean population inherited an actively operating Russian research station" — FIX SOURCE Local_Cultures/Mirny_Subnet/Sinheung.md), 49-51, 72-75, 152, 165-170.
 Run4/10:17-18, 75-80.  Run4/12:37-38.
CLUSTER C (Cape Adare precedence / Borchgrevink 1899 / NZ founding memory — rule 7/4):
 Run7/00:39-41, 125-126, 158-159; 01:3-6, 62-66, 68-69, 81; 02:19-21, 25, 19-20 (census), 33-35, 43-44; 04:4-5; 05:21-24; 06:3, 21-24, 42-47; 07:3, 17-22, 12; 09:13-15, 40-41; 10:3-4, 33-35, 51-52; 11:37-38; 12:80-83; 13:33-37, 111-112; 14:113, 142-144; 15:19-29, 89-98; Research_Log:27.
 Run8/00_Warm_Pass:11 input set includes Background-Lore Cape_Adare_Course_of_Events_Suggestions (rule 6); :179-180; :100-104; :121-128 doctrine; :172 CGRM-001 founding composition.
AMBIGUOUS: Zhongshan in shared Jeju-do act (Tri-Cities/01:19, 50; 03:34; OBS:27; Run2/00:78); Sun Yat-sen naming (Run2/01:19; Run3/01:13; Run4/08:29-31) — canon credits Mèi Sun; Run4/11:36-43 "founding continuity"; Run4/02:158-162 ASMA 6 "highest-value unread source"; St. Carsten feast (CapeAdare/06:10-17, 55-57; 12:157; 15:38-41; Run8:176-177); Run8:136-141 neutrality identity; Run4/09:104-105 "unbrokenly Chinese".
OTHER: Zhongshan ~60-day polar night (Run2/01:88, 189, 208, 347; Run3/01:188, 195; Run3/06:55-56; Run4/02:83-84; Run4/04:116; Run4/06:88; Run4/10:90) → ~49; Run3/01:187 precip 200–300 → 159 mm; CapeAdare/03:11, 65 ~87 → ~69 days; Run2/01:96-97, 176-177 Germany vs Korea 9.70; stale census Tri-Cities/01:61, OBS:305-307; Tri-Cities/01:78 Band 4→5; Run3/01:226 junction; Run3/02:82 Kunlun access; chamber makers Tri-Cities/01:165, 02:150-159; Highway37/00:78-79 Concordia subnet; CapeAdare/00:103-104 sibling list; Highway37/00:212 darkness; Run4/01:117; frame slips Run4/01:119-120, Run3/01:95-96, Run3/02:149, Run3/04:69, Run3/05:164, 228, Run4/03:133-136, Highway37/00:179; Run4/01:261 vs 259; Run8:148-149 vs 179; Run3/02:216 "短"; Run3/02:312 Davis 340 km.

---

### T2 — Archive/ULM_Records/Test_Runs/2026-08-31_Highway37_Run6_Cold (16) + 2026-08-31_Janbogo_Run9_Cold (23) — all full
Highway37: no heritage mistakes.
JANBOGO FAMILIES:
A inherited station research tradition (rules 3,1): root 08_Phase7_Order:19-27 "scientific/applied-research tradition, grounded in … the real Jang Bogo Station's documented research foci … inherited scientific-instrumentation/data-service tradition" → "The non-thematic export: not yet groundable in admissible material — REQUESTED. (The real station's research program is infrastructure provenance only, DR-24/DR-25, and cannot seed a city tradition.)"
 dependents: 08_Phase7:47-48, 50-56, 87-90; 09_Phase8:52-56 → "Arts/craft: not yet groundable — REQUESTED.", :94; 11_Phase10:20-21, 60; Aquarius:30-40, 42-44 "a real historical research-station heritage", 50-51, 45-47, hits 79-80, 123-128, 149-151, 186-192, 229-231, 318-324, 338-341, 348-352; Aries:272-286 H8, 468-472 H18, 474-478 H19, rows 520, 530, 531; Cancer:99-101, 142, 299-304 F12; Capricorn:213-222 HIT 8, 307-312 HIT 8b.
B namesake as identity (rules 1,7): 02_Phase1:76-84 G7 note → "G7 note. The real Jang Bogo Station supplies infrastructure facts only (DR-24); its name and namesake are not an input to Janbogo's identity, function or naming."; 02_Phase1:281-283; 07_Phase6:26-44 → "National_Holidays.md's Saints category was checked; whether and how Janbogo observes it is REQUESTED. The real station's name is not an input (DR-19)."; 07_Phase6:85-87 → "Core value, derived from G2/G5 (the polynya, the highway spur): safe passage through a hostile environment."; Aries:378-390 H11, 492-495 H22, rows 523, 534; Capricorn:171-179, 226-231; Gemini:443-464 F8, 555-560 F8b, rows 592-593; Leo:39, 115; Libra:177-182; Pisces:134-151 HIT 4, 414-418 HIT 4b, row 490; Scorpio:313-320, 511-512.
C "founding operator": 02_Phase1:139; 03_Phase2:10 (census tag), 62 → "founding nation (Founding Register)".
D Zukelli = Italy: 06_Phase5:39-46 → "Differentiation from Zukelli cannot use founding-nation share: Zukelli's founders are unruled (Founding Register)."; :119-121; 11_Phase10:73; Libra:238-240.
E Course_of_Events: 00_Frame_and_PreFlight:148-151 → "Course_of_Events / Background-Lore vignettes are not canon and are not an input (developer ruling); not read."; :172; :218-223; :227.
AMBIGUOUS: 00_Frame:193, 198 G7 = Jang Bogo Station; 06_Phase5:25-26 + Scorpio:339-340 "same station-inheritance founding pattern"; Fort McMurdo Saint via Hut Point (07_Phase6:23-24, 32; Aries:380, 493; Gemini:447); Kunlun astronomy (Hwy37 05_Phase5:77; 11_Zodiac:156-161; 02_Phase2:19-20).
OTHER: Hwy37 01_Phase1:71 "Concordia… belongs to no subnet" vs Register Janbogo; 10_Phase10:14 "unmarked"; 13_Step7:31, 15_Step9:38 "Five of ten" → eight; 11_Zodiac:241-246 Libra double count. Janbogo: 13 nations (10_Phase9:11; Aquarius:198-199; Scorpio:258; Libra:203-204 "eight"→ten); Pisces:176-177 Korea tier; dark season 6–8 wk vs 64 d (04_Phase3:92; 05_Phase4:41; 09_Phase8:63; Aries:251, 257; Leo:17); Libra:52-53, 160-161 misattributed; 00_Frame:202-204 garbled; Aquarius:27 Eustemon→Euctemon; Aquarius:406-407 garbled; CrossSign:31, 69, 55; tallies Cancer:341, Gemini:598-599, Leo:149, Pisces:514-516.

---

### T3 — Janbogo_Run9 (Taurus, Virgo, 13–17), MountainPassAirport_Run10 (all), SanayMaritimeShippingPort_Run11 (all), Sinheung_Run5 00–07 — 51 files all full
J=Janbogo_Run9, M=MountainPass_Run10, S=Sanay_Run11, H=Sinheung_Run5
MISTAKES
J1 Taurus:159-160 "founding station's original research vocation, persisting" → "(a city-originated trade; the station left records, not a vocation)".
J2 Virgo:186-191 "inherited scientific/applied-testbed tradition" → "Phase 8's own undeveloped precision-instrument/data-equipment craft thread (a Janbogo-originated trade)".
J3 Virgo:296-303 Finding 7 guild continuing station's research programs → delete (or records-custodian body).
J4 Virgo:316-317 → "Phase 7a/8's own instrument-craft thread".
J5 Virgo:491-495 Synthesis (c) → delete.
J6 Virgo:527, 535 rows → delete.
J7 13_QA_Gates_Part1:254 "Inflected… Traces to the real station's own pre-existing research mission, inherited at founding" → "| The scientific/testbed export (Phase 7a) | Originated | A Janbogo trade; the station handed down records only (DR-25) |"; :257 recount 5/1/1.
J8 13_QA_Gates_Part1:163-165 namesake function / research foci admissible → delete.
J9 15_Step7_Gate6:19 parenthetical → delete.
J10 14_Step5:92 "founding operator nation (South Korea, 10.23%)" → "founding nation (Korea, per the Founding Register)".
J11 14_Step5:100 "Operator status — the nation that founded/ran the real station" → "Korea's founding claim, stated on Janbogo's own geography and access per the Register".
J12 14_Step5:105-106 "operator status structurally outranked by scale" → "a founding nation structurally outranked by scale".
J13 14_Step5:87-90, :100 Cape Adare Borchgrevink 1899 precedence, NZ earliest arrival → delete.
J14 15_Step7_Gate6:60-64 Janbogo 10.23% vs Zukelli (Italy) 6.24% → delete.
M15 01_Phase1:120 "a deliberately curated astronomy-and-comms-heritage population" → "entirely robot".
M16 02_Phase2:11-13 "…rather than founding-operator history" → "Entirely robot (per Specs/Kunlun.md)".
M17 02_Phase2:90-91 "technical/scientific-heritage cultures (Kunlun's curated astronomy-and-comms lineage" → "Both source populations supply technical staff".
M18 01_Phase1:229-230; Research_Log:14-17 "Vostok (Vostok Station, Russia) and Kunlun (Kunlun Station, China), which already have their own dedicated real-world anchors" → "the stations at Vostok's and Kunlun's coordinates".
S19 01_Phase1:133 "Sinheung's founding claim sitting permanently beside Zhongshan's organic one" → "Troll's airfield sitting permanently beside Sanay's need for one".
H20 00_Frame:28-29 "all three founded by the same single diplomatic instrument (the Jeju-do court)" → "Sinheung and Shirayuki allocated by the Jeju-do court; Zhongshan Chinese on its own geography and access (DR-21)".
H21 00_Frame:203 same.
H22 00_Frame:210-211 "G7 Real-world inspiration designation available — Progress Station/AARI" → delete.
H23 00_Frame:229-231 "rather than organic station inheritance" → "settled by the Jeju-do court's diplomatic allocation".
H24 01_Phase1:81-82 "and confirmed Zhongshan's claim to China" → drop.
H25 01_Phase1:83-85 "not a claim grown organically the way most Tepenian cities' founding stories work (station inheritance…" → keep "a claim secured by treaty before any Korean exile had set foot on the site".
H26 01_Phase1:87-88 "Russian polar research infrastructure (Progress Station, AARI) — deep institutional roots" → "inherited, fully-built polar research physical plant; records only, no living institution".
H27 01_Phase1:90-95 "Every other Larsemann Hills founding at least has … prior operator history… (Zhongshan literally sits on Zhongshan Station…)" → delete.
H28 01_Phase1:102 "No organic, lived claim… prior presence" → "A claim secured on paper before the population arrived".
H29 01_Phase1:104 "the way Zhongshan's Chinese identity can rest on physical/nominal continuity with the original station" → delete.
H30 01_Phase1:198-202, 217-222 "comparison population (founders with an organic, lived claim)… Zhongshan and Shirayuki" → delete, withdraw variant.
H31 02_Phase2:35-37 Specs Legacy quote "one of only two Tepenian cities settled this way rather than through organic station inheritance" → drop clause; FIX Specs/Sinheung Legacy (& Shirayuki) source.
H32 03_Phase3:10-25 "G7 research — Progress Station, the direct real-world basis… logistics relay… independently true of Sinheung" → "Real-world comparable (physical plant only)", delete corroboration.
H33 05_Phase5:40-41 "three cities that share a founding mechanism" → "two cities that share a founding mechanism (the Jeju-do court) and a third that does not".
H34 06_Phase6:19-20 "not at stake in a city that grew organically" → "for a city whose claim was allocated".
AMBIGUOUS: J Virgo:476-482, 16_Step8:11, 63-71 testbed track; J 15_Step7:20 founding-day observance on Jang Bogo→Janbogo naming; J 13_QA:305-307 census as founding source; M Concordia Station French-Italian partnership as comparable (01:247-249, 05:41, 07:30-32, Log:46); S SANAP resupply (01:26, 84, 157-159; Log:52-53, 82-84); H 00_Frame:233-234 "notable absence: no Russian founding population" reword; H 01:103 "start[ed] to genuinely" Course-of-Events?; H 06 §A stake; M 09:132 single-founder Settlement for Vostok/Kunlun.
OTHER: J Taurus:86-87, 16_Step8:98-99 polynya unique (shared with Zukelli); Taurus:80 "only year-round ice-free"; 17_Step9:82 27 vs 30 files; 17:105-107 vs 84-90; 15:60, 16:88 Zukelli at Step 6 M-72; 14:121 Gates open. M 13_Step7:58-62 false zero-hit scan (20 British hits!); Research_Log:35-40 "Concordia unrelated" false; 06:91-93, Log:51 Midwinter Concordia's own; 06:105-107 "only true polar night"; 00:167, 366-367 Band 1 stale; 03:101, 07:101 twelve; 09:99, 11:525, 527 phantom results; 11 tallies; 15:78, 109-111. S 11:143-145; 13:136-138; 15:11; 00:117 SANAE 1960-1997 chain wrong; 01:25 "tidewater-accessible" (SANAE IV ~170 km inland — spec issue). H 03:18 five→four orders; 06:76 two generations; 06:51 G8 phantom; 02:93 vs 97; 02:68-75 UK absence (census).

---

### T4 — Sinheung_Run5_Cold 08–17, Run13/00, Run14/00_RUN_STATUS, Run15 extracts+maps, COLD_RUN_CHECKLIST, Casey prep, RESUME_HERE, RUN_LOG, Sanay prep, Dry_Run trace, Worked_Examples_Archive/*, Zhongshan_Extracted_Worked_Examples (39 files, all full)
MISTAKES
A Zhongshan organic vs Sinheung allocated:
1 S5/09_Phase9:84-86 → "Zhongshan, whose Chinese (Sinian Federation) founders settled on the oasis's own geography and access rather than through a Jeju-do court allocation, would be the sharper swap-test partner at Step 7." (still comparison — prefer delete)
2 S5/11_Step5:40-41 parenthetical → delete.
3 S5/12_Step7_Gate6:17 row → delete; 19-26 "word-for-word" convergence → withdraw. Source Local_Cultures/Mirny_Subnet/Sinheung.md §23.
4 S5/13_Step7_QA:96-97 Progress Station G7 research (summer/winter swing, Mirny-transfer logistics) changed findings → delete; re-ground.
5 S5/16_Zodiac_Lens:95-96 "Zhongshan, by contrast, has an organic founding claim (a station under its own name, prior operator presence)" → delete.
6 S5/17_CrossCheck:196, 200 → NULL; 206-210 rewrite "The tri-city relationship is two-layered: a formal, equal-in-appearance ceremony (base), with the real substantive give-and-take happening through a quieter channel beneath it (Water)."; 385-389 delete; 467-469 delete.
7 RUN_LOG:82-83 parenthetical → delete.
8 Worked_Examples_Archive/Sinheung:13-17 "someone who has organically what this location was only allocated"; "neighbor's organic one" → "someone who has what this location lacks"; delete instance.
9 RUN_LOG:48-50 "(the 2564 exiles arrived at an inhabited place; every other Tepenian city was founded on an empty one)" → delete.
10 Zhongshan_Extracted_Worked_Examples:23-24 "the 2564-exiles-joined-not-founded finding" → delete.
B R15/specs_admissible_extract.md (copy of Specs/Shirayuki.md):
11 :17 "not an organic real-station inheritance like Sayowa's, but" → delete words.
12 :27 "See also: Lazar.md … resolved by coalescing with the adjacent, continuously-operated Russian Novolazarevskaya station." → delete.
13 :29 "genuine real-world neighbors are Chinese (Zhongshan…) and Russian (Sinheung/Progress Station…) — neither Japanese. Rather than force an organic real-station-adjacency explanation the way Lazar's resolution used," → "This city's founding was resolved through".
14 :31 "Korea already held claim to multiple Antarctic footholds that would become Janbogo and Sejong … Rather than let China's proximity default into a third claim," → "The Jeju-do court …"; delete "gives Tepenia's Japanese exile community a second city (alongside Sayowa) … Sayowa inherited its own real station directly".
15 :77 "rather than any organic real-station inheritance — a genuinely different founding mechanism from Sayowa's own JARE-inherited Japanese identity" → "Japanese exiles, arriving via the Jeju-do court's diplomatic allocation."
 ⇒ SAME TEXT IN Specs/Mirny subnet/Shirayuki.md — FIX SPEC.
C operator nations as admissible G7 input:
16 R15/maps/R3/…Station_to_City_Map.md [68,73,"A","G7"] (Progress Station | Russia | Sinheung), lines 3, 11–12, 150 G4.
17 R15/maps/R3/…Overview.md line 3 "All Tepenian cities grew from real Antarctic research stations", 70, 112–117 A/G7.
D vignettes:
18 ULM_Dry_Run_Findability_Trace:286-288 "G6 is available: … Background-Lore/…-style vignettes" → delete clause.
19 Run13/00_Frame_and_PreFlight:144-145 "Readable as prompts" → "NOT canon; never read, cited or used as an input."
20 SanayShipyard_ColdRun_Prep:86-93, 94-97 → "Not canon — never read, scheduled or cited."
E 21 RUN_LOG:178-179 "Cape Adare's founding logic (organized around Borchgrevink's 1899 precedence," → delete phrase.
AMBIGUOUS: Run14/00_RUN_STATUS:98, R15/run14_inherited_extract:16 "Bharati Gallery Halls"; R15/EXPOSURE_LEDGER:107-113 G7 founding inference; COLD_RUN_CHECKLIST:309-310, RESUME_HERE:594-596, 674-675 G4/G7 no caveat; Casey prep:184; R15/national_medical_extract:56-59 Kunlun Chinese/Vostok Japanese Primary; Symbol_Pairings:18 Kunlun observatory; RUN_LOG:181-182 Cape Adare NZ founding memory, :199; Sanay prep:207-210 German-Primary single-founder (vs Register SA), :56, :133; RESUME_HERE:789-790.
OTHER: R15/specs_extract:25 "real-world station name 'Shirayuki' (Sanskrit…)" → Bharati (find-replace damage; confirmed in `Specs/Mirny subnet/Shirayuki.md` L23); :77 Sayowa "same subnet"; Casey prep:143-157 stale ranges; "Sixteen gates" → 17 (RUN_LOG:23, 45, 76, 137, 171, 245, 297, 342; Zhongshan_Extracted:29; S5/15:100; RESUME_HERE:187); RUN_LOG:19-33 index missing Run 14/15; RESUME_HERE:335, 498-499; Dry_Run:231-235 census §I China Primary for Shirayuki (census: deferred); S5/08:24, 33; S5/12:16; S5/16:239, 368-370; S5/17 arithmetic.

---

### T5 — Test_Runs/OBSERVATIONS_and_Methodology_Findings.md (1–8409 full)
MISTAKES
1 OBS:967-970 "because Zhongshan's claim was confirmed (organic, prior operator presence) while Sinheung's was allocated from nothing" → "Step 5's reconciliation, run entirely before any withheld file was opened, located Sinheung's founding condition in its own allocation by the Jeju-do court."
2 OBS:975-976 quote "Zhongshan's claim was organic and merely confirmed by Jeju-do; this city's claim was made by Jeju-do from nothing. Both cities know it." + OBS:974-975 "with the Zhongshan comparison stated almost word-for-word" → delete. SOURCE Local_Cultures/Mirny_Subnet/Sinheung.md carries same (outside).
3 OBS:1008-1011 "comparison population — Zhongshan and Shirayuki's own founding populations, who DO have organic/prior-operator claims" → delete Sinheung example (Shirayuki = Jeju-do allocation, Register L61).
4 OBS:2065-2066 "founding operator nation not the demographic majority" → "(founding nation — Korea — not the demographic majority)".
5 OBS:2091-2092 "the quantified Zukelli founding-dilution comparison (10.23% vs. 6.24%)" → delete; OBS:2087 "Five findings" → "Four".
6 OBS:1895-1904 M-68 Finding 1 Jang Bogo namesake decides Saints; sweep of "35 outer cities' real-world station namesakes" → delete or "Whether Janbogo holds a Tepenian Saint is a question for the Saints canon, not for the real station's naming; REQUESTED."
7 OBS:4230-4232 "REAL-WORLD BASIS NAME… simultaneously an admissible G7 attribute" → "…because it is a GPS coordinate only (never a G7 input, per 02 §G7) and is also the key to conclusion-tier prose written before the rename."
8 OBS:5433-5435 "with the founding nation's name attached" → "with the station operator's name attached".
9 OBS:1365-1367, 1369-1376, 1392-1399 M-57 St. Carsten's date "formally adopted" from Background-Lore Cape_Adare_Course_of_Events_Suggestions §6; "answer was sitting in Background-Lore… hard rule" → not canon; REQUESTED item stands; exclude Background-Lore from search scope.
10 OBS:1649-1651, 1653-1662, 1669, 1674-1675 M-62 "status marking, not exclusion", "demoted to prompt standing… may be read", "Janbogo's eleven vignettes demoted", "open question" → excluded, never input.
11 OBS:7970 M-236 "proposals awaiting a ratification decision" → not canon.
AMBIGUOUS
- OBS:7752-7755 M-230 Davis "heritage"; spec Davis.md L190 "ecological / limnological research, the founding heritage" — DR-25?
- Cape Adare precedence/1899 Borchgrevink hut identity: OBS:1203-1205, 1323-1325, 1331-1334, 1424, 1477-1480 — rule 7?
- OBS:2089-2090 "G4 founding-footprint mismatch (real station staffing numbers…)" — rule 1?
- OBS:2273-2279 Midwinter Day tradition fused (Mountain Pass Airport) — rule 3?
- OBS:2514 "manual inherited from a defunct founding institution" (Sanay) — SANAE?
- OBS:448 Zhongshan "early organic-settlement period".
- OBS:1898 Scott, Fort McMurdo hold Saints — via real Ross Island huts?
OTHER
- OBS:881 "M-40" doesn't exist; OBS:1427 "(M-?/Runs 3–4)" → M-9; order M-38b..M-42 before M-34 (OBS:787-930); city counts drift 35/34/37/38.

---

### C_Davis_1 — Davis .t8_phase2_reader{A,B,C}, .t8_step2_reader{A,B,C}, .t8_step3_readerA (all full)
MISTAKES (rule 3 DR-25 — "research heritage", stale spec L143 wording; live spec no longer has it, commit 1914cdb)
- .t8_step2_readerB:51-53 quote "alongside genuine research heritage make up" → "alongside research make up the clear majority of daily activity."
- .t8_step2_readerB:60-61 "The line's own word for the research half is 'heritage.' A heritage is received, not elected." → delete item 2.
- .t8_step2_readerB:86-87 "and on L143's word 'heritage,' which is ratified." → "and on L143's two parent-facing clauses."
- .t8_step2_readerB:789 "its word for the other half is 'heritage.'" → end at "answers only the parent-facing one."
- .t8_step2_readerB:808 "L143's two parent-facing roles and the word 'heritage'" → "L143's two parent-facing roles; corroborated by 35 against 25."
- .t8_step2_readerB:844 "calls the research half a heritage." → delete clause.
- .t8_step2_readerA:509-511, readerC:451-453 stale quote → current.
- .t8_step2_readerC:465-466 "a research community with genuine research heritage." → "a research community."
- .t8_phase2_readerA:530-531 "its own word for the research half is 'heritage.'" → delete.
- .t8_phase2_readerB:784 "a serial observation heritage" → "a serial observation practice the exiles built themselves".
AMBIGUOUS
- .t8_step2_readerC:700-704, 739-742 D1 "living institution did not survive the handoff… belonged to operators" as Davis's own-past deficit → rule 7? alt "NOWHERE AT ALL".
- .t8_phase2_readerB:243-248, 977, 1067 H7 "(founding wave)" — close as answered by Register.
- Proof blocks quote spec L234 Mawson tie (readerA:1283, B:910, C:1034). Spec also L129 "three cities carrying Australian founding-wave heritage across the subnet" (rules 1,5), L131 "carries specific weight in Australian Antarctic culture" (rule 1) — FIX AT SPEC.
OTHER
- .t8_step2_readerC:355 "fourteen Notable" → thirteen.
- .t8_step2_readerC:700 "five centuries back" → "before the founding, across the 2083–2564 handoff chain".
- spec path Cities/Specs/Davis.md → Specs/Mirny subnet/Davis.md (A:1278, B:905, C:1029); stale proof quotes A:1284, B:911.
- .t8_step3_readerA:440-441, 867 "NOT OPENED" vs 460, 859 AAD geology dataset.

---

### C_Davis_2 — Davis .t8_step3_reader{B,C}, 00.0, 00.1_SUPERSEDED, 00.1, 00.1a, 00.1b, 00_Frame (all full)
SPEC: Davis L8 "Shares Australian founding-wave heritage with Mirny subnet neighbors Casey and Mirny itself … named after John King Davis"; L62 "one of the three Australian Antarctic stations alongside Mawson and Casey … alongside fellow Australian-founding-wave city Casey"; L129 "three cities carrying Australian founding-wave heritage across the subnet" → SPEC FIXES.
MISTAKES
M1 00.1:255-256 L8 "CLEARED ON CONTENT: real-world basis, coordinates, heritage and geographic facts"; 00.1_SUPERSEDED:49-51 → PARTIAL STRIKE (keep Vestfold/Prydz).
M2 00.1:269 "the subnet/founding-wave roster is legal relation"; 00.1b:485 → PARTIAL (keep AAD operated since 1957 + Mirny subnet).
M3 00.1b:491 "L129 KEEP"; 00.1:275 "L127 · L129 KEEP" → PARTIAL (keep "Founding population: Australian exiles.").
M4 00.1:150-152, 00.1a:66-67 L143 "genuine research heritage" admitted (strike lists 00.1:277-280, 00.1b:506-507 miss it) → strike/now gone from spec.
M5 00_Frame:178-183 ground 1 struck "THIS GROUND IS NO LONGER GOOD LAW" → reinstate (station occupancy never a first population; records only).
M6 00_Frame:371 Resettled POPULATION vs OCCUPANCY "(Settles most of the 38-city run)… DR-7 removes the GPS OBSTACLE" → "a real station's prior occupancy is never a prior population… open only for in-world Tepenian prior populations".
M7 00.1_SUPERSEDED:78, 00.1:296 G6 runbook address Background-Lore/Cities/<Subnet>/<City>/ → strike the Background-Lore address from these two files. (The runbook's own G6 address list is already clean.)
M8 00.1:305, 00.1_SUPERSEDED:87 vignette tension "CORROBORATION AT BEST" → cannot be source nor corroboration.
M9 00.1_SUPERSEDED:177-180 "DEMOTED (readable as prompt)" → NOT CANON, NEVER AN INPUT.
AMBIGUOUS
1 00_Frame:334 "documentary-inheritance founding"; 00.1:190-191; 00_Frame:192-194, 368 — G4 also on geography?
2 .t8_step3_readerB:158, 423-425, 1107 home-brewing ban at named station.
3 00.1_SUPERSEDED:139-140, 164 Hobart/Fremantle staging; Datasheets/Phase_7:52.
4 00.0:321-323 Davis↔Mawson re-derive; Datasheets/Phase_5:21 → strike under DR-19?
5 .t8_step3_readerC:109-110, 649-651 "legitimacy is in the log".
6 README row Janbogo_Research_Log "Jang Bogo Station's real staffing/scale and its historical namesake" (B:1691, C:1217) — Research_Logs/Janbogo_Research_Log.md not yet read for this (Part C).
OTHER
- 00.1b:261, 296-298 vs :424 withdrawn.
- 00.1b:525, 585 Band 4 Census II vs DR-4.
- 00.1b:379-380 stale running.
- 00.0:468 "two" entries gives three; path lines L71, 106, 251.
- .t8_step3_readerC:1348, 1356-1357 phantom content.
- .t8_step3_readerB:1464 17 vs 23 retrievals.

---

### C_Davis_3 — Davis 00b_T8_Rounds_Step_0 (4128), 01_Inherited (363), 01b_T8_Rounds_Step_1 (4541) — all full
MISTAKES
M-1 (rules 1,7) "§0.1a ground 1 FALLS" — station occupancy treated as possible first population:
 01_Inherited:154 "⛔ FALLS — see §1.3a" → "✅ STANDS — DR-7 admits the records only (DR-25); the station's occupancy is a coordinate and never a first population (DR-19)"
 :158 "one ground falls; the verdict stands" → "no ground falls; the verdict stands"
 :160 "DR-7 kills the first:" → delete
 :164 "⛔ FALLS. DR-7 does not exclude it" → "✅ STANDS. DR-7 admits records, not the occupancy as a population"
 :168-170 "carries a ground that is no longer good law" → delete
 :212-213 "It REOPENS 00_Frame.md §0.1a ground 1 … Resettled question returns" → "Ground 1 is unaffected (DR-19, DR-25)"
 :303 "Resettled — prior POPULATION or merely prior OCCUPANCY? ⏸️ B" → A, resolved by DR-19
 :358-360 "is now KNOWN-BAD LAW and must be corrected" → delete
 source 01b:4360-4363 "Ruling (a) supplies… a prior occupying population… for 481 years. Ground 1 does not survive" → "Ruling (a) admits the records only; custodial operators are never a population of Davis (DR-19)"; 01b:4523 delete. (Contradicts 01b:1007, 1449, 3028.)
M-2 00b:336 "a second population inhabiting what an earlier one left" → "the founders inherited infrastructure and records (DR-24/25); there was no earlier population"; 00b:3870-3875, 4115-4121, 01b:4336-4339 → settled by DR-19.
M-3 00b:2269, 01b:1555 quote spec "genuine research heritage" (source already fixed); 00b:2468 "plus research heritage" → "plus research".
M-4 Spec L179(?) Mawson relationship "both named for/connected to Australian Antarctic figures … whether any cultural connection existed" quoted at 00b:151, 1161, 2268; 01b:728, 1554, 2570 → delete at source.
M-5 Spec L131 closing clause "a figure whose name carries specific weight in Australian Antarctic culture" quoted 01b:943, 2571 → delete at source; 01b:409 "C-1 RATIFIED CANON" → add "(closing clause excluded — real-world provenance)".
M-6 real namesake (John King Davis) generating identity: 01b:73-74, 955-956, 1774 "He is pre-2083 (1884–1967)", 1783-1786 → "What does the Saint roster's admission rule decide, who authors it, and is there an appeal?"
AMBIGUOUS
Q-1 01_Inherited:134 "L127 IS ADMISSIBLE" vs 184-185 "operator lineage, institutional discontinuity"; spec L127 "continuously maintained by a rotating succession of national operators" — provenance only, or KEEP OUTCOME CUT CHAIN (01_Inherited:204)?
Q-2 01b:3900, 3906-3907 "shared-heritage roster plausibly is relation", 614-618 founding-wave roster legal relation — rule 5 / rule 1?
Q-3 01b:348 "research tradition is Inflected in form (research is inherited)"; 01_Inherited:125-128 — national scientific life OK, L143 heritage not.
Q-4 Second Interwar README/Timeline used as G6 corroboration (00b:130-136, 1700; 01_Inherited:256) — not a mistake: the Second Interwar README/Timeline are canon era files, not vignettes.
Q-5 01_Inherited:73 fire #6 Saint exclusion — namesake admissible?
OTHER
- 00b:933-944 D-5 reading (b) "GPS leak … strikes L129" → withdrawn (Register rules Australia).
- 01b:2958, 3639 "on Davis Station infrastructure" ambiguous → resolved DR-24.
- 01b:1226 44.04% → 44.03%.
- 01_Inherited:165 "explicitly superseded" → add caveat (disputed 01b:1446-1450, 3020-3029).

---

### C_Davis_4 — Davis 02_Spine (585), 02b_T8_Rounds_Step_2 (3664), 03_Research (348), 03b_T8_Rounds_Step_3 (2899), 04_Phase_02 (1601) — all full
Root: spec L143 old wording "genuine research heritage" (now removed from spec by my uncommitted edit). Spec still has L190 "ecological / limnological research, the founding heritage" and L234 Mawson naming tie — OUTSIDE partition, needs fixing.
MISTAKES (rule 3/1)
- 02_Spine:359-360 "Its own word for the research half is 'heritage' — an inheritance, not an identity" → "Both clauses are parent-facing: 'Tepenia's breadbasket' and 'a prime… research hub' both say what Davis is FOR, to somebody else." (delete heritage sentence)
- 02_Spine:42-43 "calls the research half a `heritage`." → "contains no self-understanding at all; both of its clauses are parent-facing."
- 02_Spine:437 "`G3` — L143's two parent-facing roles and the word *heritage*; corroborated by 35 against 25" → drop "and the word *heritage*".
- 02_Spine:581-582 "rests on L143's wording and on 35 > 25" → keep, note heritage gone.
- 02b (raw T8 record): L40, 168, 199, 225, 1660, 1686-1687, 2389, 2408, 2444, 3038-3039 → dated annotation suggested (or strip per developer's "just strip it" rule).
- Suggested replacement derivation: B's C-1 02b L2069-2073 "direct descendant of the founding survival method".
AMBIGUOUS
A1 03b:1340, 1606-1607 home-brewing banned 2021 by "operating authority" — real AAD ban at this site? rule 7.
A2 03b:2439, 1558 Esperanza "first birth in 1978"; 2131-2135, 2454-2461 McMurdo/Amundsen–Scott/Concordia comparables — other city sites' real history as comparables?
A3 02b:1537, 2510, 3607 PROOF quotes of spec L234 Mawson naming tie (source = spec issue).
OTHER
O1 stale spec quotes 02b:763-765, 1538, 1651-1653, 2511, 3024-3026; path Cities/Specs/Davis.md → Specs/Mirny subnet/Davis.md (02b L92, 1532, 2505, 3602; 04_Phase_02:40).
O2 02_Spine:32 (02b L29) defect 2 attribution: held by A and C; caught by B.
O3 02b:3273, 3277 "loss at the founding, five centuries back" → "before the founding, in the handoff chain".
O4 03_Research:218, 307, 310, 328, 344 "not spent/unread" vs table 255-264 (spent; Gore 1996 obtained).
O5 04_Phase_02:857, 877, 884, 578, 978 Act 1 ≈18% vs 2688 transition ≈50%.
O6 03b:850-851 "operator sources not read" vs L870 data.gov.au AAD geology (admissible).

---

### C_Davis_5 — Davis 04_Phase_03..10, 04b, 05..10, README, Datasheets/* (36 files, all full)
MISTAKES
M1 05_Reconciliation:155-162 §6 GPS NARROWING "✅ Legitimate — the ULM wrongly refused it | 'The founding generation CHOSE his name deliberately.'" "The law… does not bar a population from choosing a name and meaning it." → one "⛔ GPS violation — stands" column; L162 → "⇒ The law bars a site's identity AND its namesake's biography as inputs; the city's name is a coordinate label."
M2 04_Phase_06:119 "A city whose inherited expertise" → "rebuilt expertise".
M3 04_Phase_10:139 "inherited expertise" → "own rebuilt expertise".
M4 04_Phase_05:36, 105, 114, 305, 330, 346 "intra-subnet Australian-heritage network… Re-derive or escalate"; H31 → add "⛔ AND inadmissible under DR-19 regardless of source"; H31 → "Whether Davis has any relation to another city grounded in geography/access or the Founding Register, independent of the withheld Megasheets."; others "operator-heritage relations (inadmissible, DR-19)".
M5 Datasheets/Phase_5:20-22, 43-49 "shared Australian-heritage naming… Re-derive it" → "⛔ Do not re-derive…".
M6 Datasheets/Phase_5:11 "Clean — relation-legal: Davis — Real station: Davis Station (Australia)"; 04_Phase_05:25 → "GPS coordinate only; nothing extracted".
M7 Datasheets/Phase_5:12 Davis ↔ Neumayer "two most genuinely comparable 'hard science' civic identities… atmospheric/glaciological research at Neumayer, paleoclimate sediment-core research at Davis" → refused. (SOURCE file? probably City_Cross_Subnet_Relationships / National connections.)
M8 04_Phase_04:104-105 "genuine research heritage" quote → "[research]" + note.
M9 05_Reconciliation:147 Vladivostok 'wish' "History-file — and moot" → "History-file — not canon; inadmissible."
AMBIGUOUS
A1 04_Phase_05:73-79 "two independently developed long-term climate-record traditions".
A2 Datasheets/Phase_7:52 Hobart/Fremantle.
A3 07_QA:227, Datasheets/Step_3:13 USAP Participant Guide chores.
A4 04b:157-165 H6 founding wave — close by Register.
A5 04_Phase_09:76-77 "21-fold with no single thread to anchor to".
A6 05_Reconciliation:160-163 H62 — close by DR-19.
OTHER
1 04_Phase_03:446 vs 413, 438, 470 (adopted).
2 04_Phase_03:205-206 salt side reversed.
3 04_Phase_10:438 Gore stale.
4 04_Phase_10:242 "canon-established" → research-established.
5 port season: 04_Phase_05:202, 22, 266-277; 07_QA:160-161 vs "year-round" 04_Phase_07:161; 04_Phase_10:422; 05_Reconciliation:97; stale maritime rejected 04_Phase_04:275-278, 432; Datasheets/Phase_4:24; Phase_5:13.
6 05_Reconciliation:102, 105, 205-207 stale.
7 05_Reconciliation:155 "Phase 10 refused" → Phase 7.
8 06_Differentiate:112-113 vs 80-85; 07_QA:206.
9 Gate 7 tallies: 07_QA:11, 22, 424 vs 210; 08_Review_Panel:312; 09_Record:60, 114; 10_Readiness:133.
10 08_Review_Panel:30, 289 disposition counts.
11 04_Phase_05:355-363 numbering.
12 04_Phase_06:354 "двух-sided" → "two-sided".
13 04_Phase_06:112-117 Local_Cultures §4 unlabeled.
14 README stale: 3-4, 26, 142-166, 162, 185, 132-133.
15 Datasheets/Phase_2:3, 14.
16 Datasheets/Step_-1:19 exclusion list.
17 Datasheets/Phase_3:13 "Vestfold largest ice-free coastal oasis" — Bunger Hills larger? (from 16 L2059).
18 minor: workforce 876,514/515; log 1,943/1,953; 09.5_Log:149 orphan row; 04_Phase_10:626-635 order; provenance boxes.

---

### C_ZhongshanOpus_1 — Zhongshan_Opus current 00.0–06 (18 files, all full)
MISTAKES
M1 04_Phase_07_Order:268-270 quote "Technical/scientific: ~35% — the research heritage is continuous from the founding station; Zhongshan produces engineers…" → delete clause; docket row to delete it in source 16_Per_City_Three_Tier_Run.md §18 and Specs §15.
M2 01_Inherited:31 I-2 "Continuous Sinian habitation and administration … Specs/Zhongshan.md, Founding · No_National_Stereotypes.md L17" → "Continuous Sinian habitation through the entire First Interwar (~481 yr) — a ruled exception to the rotating-operator model | No_National_Stereotypes.md L17 (Specs L142's 'and administration' is parked at R-24)".
M3 00.1_Step_MINUS-1:118 "The one city whose claim to its own site was settled by an international court BEFORE anyone arrived" (also false: Shirayuki, Sinheung) → "This city's claim to its own site was settled by an international court before anyone arrived — exclusively, and uncontested."; :254 "1 known 'ONLY'" → "Tier 3: the exclusive, uncontested court-settled claim — highest-yield".
M4 03_Research:167-171 annual resupply ship; 04_Phase_04:206 "one annual resupply ship" → "a ~Nov–Mar port window (Ports.md §5.6c)".
AMBIGUOUS
A1 ASMA/ASPA 174/2008 Progress fire as governance model: 03_Research:82-85, 89-93, 108-111; 04_Phase_02:241; 04_Phase_07:579-589.
A2 Midwinter observance: 03_Research:99-111; 04_Phase_10:307; 05_Reconciliation:335, 420.
A3 Kunlun/Vostok ties on unruled founders: 01_Inherited:38; 04_Phase_06:143-147; 04_Phase_09:61, 247; 04_Phase_08:203-210.
A4 city name = station name: 00.1:121 "brought its political heritage"; 02_Spine:119; 04_Phase_06:58, 246-249; 04_Phase_10:319 Founding Elder chose it.
A5 "China's existing presence" 01_Inherited:62-63; 04_Phase_02:251.
A6 station-crew studies 03_Research:205-216.
A7 comparisons: 02_Spine:67-69 Princess Elisabeth; 04_Phase_06:291-296 Dome Fuji; 04_Phase_02:301.
A8 "Nobody was taught it" applied to resident population 04_Phase_08:339-341, 840-842; 04_Phase_10:260.
OTHER
- 01_Inherited:73, 77 64.17% → 47.17%.
- 04_Phase_05:293-294 thirty years → ~124.
- 04_Phase_10:305 −9.40 → +9.40.
- currency "energy" 04_Phase_04:33, 72-74; 04_Phase_05:155; 04_Phase_07:558 vs 04_Phase_07:40 & DR-3 (energy-backed NOT canon!).
- 04_Phase_06:245 "EVERY SAINT IS AN EXPLORER WHOSE NAME BECAME A CITY" vs St. Ernest.
- 00_Frame:261, 361 "read in full" vs 00.0:172, 00.1:134, 268.
- 04_Phase_02:37 vs 00_Frame:280-299 City_Vision_Notes.
- duplicate R-11.
- missing §0.6b (04_Phase_03:59; 04_Phase_08:417, 946; 00_Frame:232, 335); 04_Phase_03:41 §0.6a→§0.4.
- 04_Phase_08:838 "canon's own words" is pass prose.
- 04_Phase_08:1031 §6.2 → §6.6.
- research log 270 vs 662 lines.

---

### C_ZhongshanOpus_2 — CUR (07,08,09.5,09,10,README) + _archive_pre-redo_2026-09-10/ (14 files) — all full
CUR files clean except ambiguous E (07_QA_Gates:135).
MISTAKES (all ARCH/ = _archive_pre-redo_2026-09-10/)
M1 ARCH/04_Phase_06_Meaning:66 "§15 (via 16 §18) — 'the research heritage is continuous from the founding station.'" feeding "Nothing here ever had to start over" (L76, 83–86, 166, 175, 254–259, 269) → delete L66; ground on L63 site claim + habitation. SOURCE Specs/Zhongshan.md §15 and 16 §18 carry it (outside).
M2 ARCH/04_Phase_07_Order:258–261 "continuity, held in the station, the site claim, the unbroken research heritage … The city applies continuity to its institutions" → "continuity, held in the site claim and in five centuries of unbroken habitation. The heritage communities are asking for the city's own standard to be extended to them. The city applies continuity to its own story and forbids the one question that would apply it to people."; L324 "as it is to institutions" → "as it is to the city's own story".
M3 ARCH/09.5_Log:1118–1119 quote "Technical/scientific: ~35% — the research heritage is continuous from the founding station; Zhongshan produces engineers…" → omit clause + ⛔ note.
M4 ARCH/02_Spine:124 "It carried a political heritage, not only people (the naming act)" → delete.
M5 ARCH/03_Research:122–134, 192–195, 473 inland traverse/resupply ops as identity; F-5 "resupply vessel… unloaded by air" → delete / "Superseded by M-193: Tepenia's harbor is a built port (Ports.md §5.6c); outpost logistics do not transfer."
M6 ARCH/03_Research:90–106, 470 "ship comes ONCE a year… HELICOPTERS" → "⛔ Superseded by M-193 — outpost resupply assumes a home country; Tepenia's harbor is CONSTRUCTED (Ports.md)."
M7 ARCH/03_Research:152–164, 224–227 2008 Progress fire "help came 1.5 km away and foreign" as governance evidence → delete; downstream "four instruments" (Phase 2 L95–97, 290; Phase 7 L187).
M8 ARCH/03_Research:367–380, 399–400, 475 magnetic quiet zone 80 m as city practice → delete; reword.
M9 ARCH/00_Frame:304–305, 462; ARCH/09.5_Log:105, 126 Background-Lore "DEMOTED… readable as a prompt" → "⛔ NOT CANON — never an input, never opened, never cited".
AMBIGUOUS
A ARCH/01_Inherited:43 "Continuous Sinian habitation and administration… exception to the rotating-operator model".
B ARCH/04_Phase_02:143–152 rotating hand-off chain; "a site that fell OUT of the chain and was abandoned".
C ARCH/04_Phase_06:64–65 quoting Specs L150 "maintained continuously… never actually left".
D ARCH/03_Research:145–146, 315 ASMA management "STRUCTURE survives" → Phase 7 governance.
E Midwinter: ARCH/03_Research:218–227; ARCH/04_Phase_06:204–206; CUR/07_QA_Gates:135 "The Midwinter-shaped observance | inflected".
F ARCH/03_Research:435 station greenhouse practice → Phase 7.
G Zhongshan–Kunlun tie (ARCH/04_Phase_05:117–118; ARCH/01_Inherited:50) mirrors CHINARE pair; canon in Airports.md, National_Medical_and_Care_Institutes.md L109.
H ARCH/04_Phase_06:215 quotes National_Holidays.md "Hut Point remembrance ritual … Scott/Fort McMurdo" (source outside).
I ARCH/01_Inherited:65–66 "confirmed China's existing presence".
OTHER
1 _Opus path artifacts: ARCH/00_Frame:304, 471; ARCH/04_Phase_03:42; ARCH/09.5_Log:126.
2 ARCH/09.5_Log:1200, 1202 R figures are totals → R 647,448 / 582,703.
3 ARCH/04_Phase_05:157 148,786 → ~133,907.
4 ARCH/04_Phase_05:278, ARCH/09.5_Log:1461 "the only fully functioning city" post-war leak.
5 ARCH/00_Frame:229 "founding (post-2564, the Jeju-do settlement)" → "founding (2564; site claim settled pre-exile at Jeju-do)".
6 ARCH/09.5_Log:897 stale; Hwy 22 hitchhiking ARCH/04_Phase_04:141, 04_Phase_05:214, 09.5_Log:1036.

---

### C_ZhongshanSonnet — Zhongshan_Sonnet live (8) + arch/ (15) — all full. NOTE: archive content largely identical to Zhongshan_Opus archive.
LIVE MISTAKES
1 03_Research:82-85 ASMA/ASPA 174/2008 Progress fire table → delete; re-source from Jeju-do + Falkland III.1 + non-Antarctic commons research.
2 03_Research:89-96, 108-111 "shared-oasis coordination custom, modeled on the real ASMA's own verbs" → delete + handoff.
3 03_Research:168-173 annual resupply ship (M-193 error) → keep only sea-ice physics "fast ice forms late February… largely ice-free only January–March."
4 03_Research:149-154 "Helicopters are therefore the only reliable means" corroborating §15 → keep only "small-boat access to eastern Broknes is difficult… due to ice debris".
5 04_Phase_02:232-234 "(the real ASMA management plan, the ASPA permit regime, Antarctic emergency-response norms, and Midwinter Day's exchange ritual)" → delete parenthetical; Art. III.1.
6 00.1:32 "DEMOTED, NOT CLOSED." → "⛔ NOT CANON — never an input; not read, not cited."
7 00.1:150 "UNRATIFIED pending a header read at Step 3." → "⛔ NOT CANON — never read."
8 00.1:152-156 "It MAY be read as a prompt." → delete.
9 00.1:257, 265-267 → "EXCLUDED — Background-Lore is not canon (developer ruling)."
10 00_Frame:379 "readable as a prompt" → "Not canon — never an input."
11 01_Inherited:194 "Background-Lore/ (unratified → demoted)" → "(not canon — excluded)".
12 01_Inherited:38, 184 "Kinship tie to Kunlun, via shared Chinese-origin population" → delete I-9 or "National_Medical_and_Care_Institutes.md L109 names a Zhongshan–Kunlun tie; its basis is unruled (Kunlun's founders are not in the Register) — not used."
13 00.1:118 (+ arch/00_Frame:86) "The one city whose claim…" → "This city's claim to its own site was confirmed exclusively and uncontested by the Jeju-do court before the exile era."
ARCH MISTAKES 14 arch/03_Research:96-106, 192-195; 15 :124-134; 16 :145-164; 17 :277-282, 315; 18 :369-380; 19 arch/04_Phase_06:66, 68-86; 20 arch/04_Phase_07:258-261 → "continuity, held in the site claim and an unbroken resident population."; 21 arch/09.5_Log:1118-1121 (source DoI §15 / 16 §18); 22 arch/09.5_Log:897; 23 arch/04_Phase_05:116-119 "Zhongshan's tie runs to Kunlun, Shirayuki's to Vostok, Sinheung's to both" → delete; 24 Background-Lore: arch/00_Frame:304-305, 462; arch/01_Inherited:206; arch/02_Spine:36; arch/09.5_Log:105, 126 → "not canon — excluded".
AMBIGUOUS: naming "political heritage" 00.1:121, 02_Spine:119, arch/02_Spine:124; "existing presence" 01_Inherited:63, 04_Phase_02:244, arch/01:66; "administration" 01_Inherited:31, 04_Phase_02:133; station-crew culture 03_Research:99-111, 201-216, arch/03:203-234, 435, arch/04_Phase_06:204-206; arch/03:70 lake depletion; road as institutional register 04_Phase_03:130-136, arch/04_Phase_03:291-298.
OTHER: "before anyone arrived" vs DR-21 continuity (01_Inherited:75; 02_Spine:119, 179, 348; 00.1:118; 04_Phase_02:246; arch/02_Spine:124, 183, 330; arch/01:79; arch/04_Phase_02:265) → "before the exile era began"; 64.17% → 47.17% (01:77; arch/01:81; arch/09.5:518); 02_Spine:68-69 Princess Elisabeth comparison delete; 02_Spine:331-332 mischaracterized; broken paths 00.0:304, 305, 307, 509-511, 00.1:84; 00.0:278 four→five; truncated paths 00.1:44, 45, 133, 134, 142, 177, 206, 207; read-order contradictions 00_Frame:261, 361, 309; 04_Phase_02:328, 37; 04_Phase_03:59 garbled + §0.6b; 04_Phase_03:41; 00_Frame:333-334 "a a"; arch manufacturing contradictions; arch/04_Phase_08:332 vs 260; arch/04_Phase_05:278, arch/09.5:1461 post-war; arch/04_Phase_05:138; arch/00_Frame:229; headcounts; arch/09.5:1200, 1202 R; arch/04_Phase_04:105, 110 31→32; G1 Metal stale (arch/00_Frame:113 vs live :101); arch NE katabatic.

---

### C_Shirayuki_1 — Shirayuki current pass (23 files, all full). No Bharati/India cause.
MISTAKES
A rule 7 vacancy/abandonment as cause:
1 00_Frame:126 "THE SITE HAD BUILT FORM AND HAD NEVER HAD PEOPLE." → "THE SITE HAD BUILT FORM, AND THE FORM WAS NOT DESIGNED FOR THE PEOPLE WHO MOVED IN."; 109-111 "No population ever occupied it… no staffed era" → "The building stock existed (physical infrastructure, DR-24). The city's own history begins in 2564, as a settlement."; 130 "inherited DESIGN INTENT with no one attached".
2 00_Frame:263 "BUILT FORM WITHOUT PREDECESSOR" → "INHERITED BUILT FORM (infrastructure only, DR-24)".
3 00_Frame:304 "without a predecessor to learn from" → "with only the infrastructure and whatever records it held (DR-25)".
4 02_Spine:95 "Without a predecessor | The site had never been occupied. No handover, no one to ask about the ground" → "The city's own history begins in 2564; it inherited buildings and records (DR-24/DR-25), not people".
5 04_Phase_07_Order:248-251 "OUTLASTED ITS MAKERS' CARE ENTIRELY. They left." → "The pre-exile station stock was standing when the exiles arrived in 2564 and has stood since … that has lasted, and it was not even made for us."
6 09.5_Log:28 item 5, :758 item 300 → annotate.
B rule 4: 7 09.5_Log:475 item 152 "TWO Japan-founded cities: Shirayuki … and Sayowa" → delete/annotate.
C rule 6 Course_of_Events:
8 01_Inherited:68 "readable as prompts" → "NOT CANON — not an input, not even as a prompt."
9 01_Inherited:396 obligation 5 asymmetry check over 11 CoE files → delete.
10 01_Inherited:405-406 "likeliest home of more" → delete.
11 05_Reconciliation:18 "TITLES ONLY, as prompts" → "NOT OPENED — not canon, not an input"; :73-76 vignette titles corroborate → delete; :291 row → delete.
12 04_Phase_10_Catalog:349-351 read-last opens CoE vignettes as CHECK → delete vignettes.
13 09.5_Log:81 item 24, :873 item 370, :884 item 381 → annotate.
AMBIGUOUS
- 00_Frame:137-143 canon-note vacancy as cause?
- 02_Spine:102 "No inherited site knowledge", :95 vs DR-25 records.
- 01_Inherited:202 Jeju-do rationale "balance China's overwhelming regional presence" — rule 5?
- Vostok tie 04_Phase_05:82; 04_Phase_07:360-361 "Vostok is Japanese-Primary"; 09.5_Log:348; 09.6_Input_Audit:60.
- 05_Reconciliation:259, :347 docket row 8 "The Bharati Station physical infrastructure" landmark name vs canon note "name does not carry forward".
- 05_Reconciliation:33, 91; 02_Spine:67 research identity unchecked origin.
- 10_Readiness_Check:78, 237 → runbook L2126-2131 Sayowa (= U1 M7).
OTHER
- "no shore / 8 km inland" 02_Spine:117; 04_Phase_05:29; 04_Phase_08:47 (from Ports.md §5.6c) vs real Grovnes coastal; conflicts 04_Phase_09:16, 04_Phase_08:255.
- 01_Inherited:217 "fifteen kilometers" vs ~8 km; China ~59,000 → ~47,064.
- 02_Spine:81 "+6.4 points" vs 11.9.
- 04_Phase_03:117, 04_Phase_10:97-98 ten sub-zero months → eleven; 04_Phase_03:122.
- 07_QA_Gates:18 FIVE vs :208 SIX hits; :64 Gate G count; 09.5_Log:926.
- 03_Research:17 search counts; 07_QA_Gates:138-140.
- 07_QA_Gates:243-245 stale lines → 04_Phase_10:297-298.
- 05_Reconciliation:352-353 duplicate bullet.
- 09.5_Log:571, 647, 563 census figures.
- British spellings (correct to favor / recognizable / traveled / labeled / labeling): 09.6_Input_Audit:7; 08_Review_Panel:69; 03_Research:381; 09.5_Log:662; 09.5_Log:945.
- 04z:78 "Built by people who never came" → "Built before the exile, for a purpose nobody here had".

---

### C_Shirayuki_2 — Shirayuki/_Archive/2026-09-06_pre-consolidation/ (15 files, all full). Bharati never used as cause.
MISTAKES
M1 Sayowa as Japan-founded (rule 4/5): 00_Frame:286 "where organic Japanese identity elsewhere diluted to a fraction" → "Japan 36.27% Primary — a protected plurality; 16 further nations"; 01_Inherited:241-242 (struck S-5) → "The claim: Japan's diplomats foresaw dilution risk; Shirayuki held at 36.27%; 'the diplomatic foresight worked exactly as intended.'"; 04_Phase_09:255-259 "Tepenia has TWO Japan-founded cities" block → delete; 09.5_Log:475 item 152 → delete/WITHDRAWN.
M2 04z_Post-Ruling_Enrichment_Review:171-186 §8 "organic real-station inheritance" (Sayowa founding mechanism) → delete §8.
M3 04_Phase_02:178-179 (struck S-1) "Zhongshan has an organic founding and sits between them at 77.90%"; 09.5_Log:206 item 64 → delete clause.
M4 04_Phase_07:351-354 "THE PRE-EXILE STATION STOCK OUTLASTED ITS MAKERS' CARE ENTIRELY. THEY LEFT. IT IS STILL STANDING." → "THE INHERITED BUILDING STOCK WAS STANDING BEFORE THE CITY EXISTED, AND IS STILL STANDING."; 09.5_Log:758 item 300 same.
M5 Course_of_Events rule 6: 01_Inherited:80 "readable as prompts" → "NOT canon and never an input — not opened, not scheduled."; :298-299 delete; :570-574 N-7 delete; :587 obligation 6 delete; 09.5_Log:81 item 24 → "Course_of_Events is not canon and is not an input; never scheduled."
AMBIGUOUS
1 00_Frame:106-131 §1c vacancy "HAD NEVER HAD PEOPLE" (canon note) + 02_Spine:91-93; 09.5_Log:28, 36.
2 04_Phase_06:316-338 "ONE GENUINELY OLD THING… somebody else's building"; 04z:74-82 rock era.
3 Shirayuki↔Vostok kinship on census tiers (04_Phase_05:103-105; 09.5_Log:348) — Vostok unruled.
4 04z:192-200 Novosibirsk → Russia Significant tier — Progress station leftover? (census)
5 02_Spine:82, 97 (struck S-3) "newest in the cluster" as strength.
OTHER
1 census split wrong 01_Inherited:360-362; 04_Phase_02:395; 09.5_Log:563, 647 (→ 518,822/541,660 → 302,512/352,980; left 216,310/188,680).
2 01_Inherited:395-396 robots who "stayed" 188,712 → "352,980 robots who stayed … 302,512 humans who stayed".
3 01_Inherited:204 China 59,000 → ~47,000.
4 sector denominators 04_Phase_07:37-39, 303; 09.5_Log:408, 754 vs 02_Spine:376-379.
5 04_Phase_07:206, 09.5_Log:413 xref → 02_Spine §5.
6 "most of the year inside station stock" 04_Phase_04:368-379; 04_Phase_06:316-318; 09.5_Log:259, 284 vs 04_Phase_03:204-205.
7 04z:81-82 vs 04_Phase_03:109, 187.
8 04_Phase_05:172, 183 port window Nov–Mar "four months".
OUTSIDE PARTITION SOURCES:
- Specs/Mirny subnet/Shirayuki.md:35 "a guaranteed second Japanese city … organic demographic chance the way Sayowa was" — FIX.
- City_National_Connections.md:384 "Shirayuki's own Bharati-Station-descended founding", :524 "Sayowa's own JARE heritage" — FIX.

---

### C_Mirny_1 — Mirny .t8 reader files Step0/1/2/3 (19 files, all full)
MISTAKES
M1 .t8_Step0_round3_readerA:89-98, 234 "Settlement + Installation (dual) + Resettled" via WHR L240 "Every real Antarctic research station became a Tepenian city" + RB L1958 → "Current view: Settlement + Resettled (restricted to DR-7 materials). Installation NOT assigned: 'founded as a station' is the site's pre-2564 lineage (DRL L352); the persisting station is a material, not a type."; L234 → "1. Type: Settlement + Resettled; Installation not assigned — 3(i)."
  NB: World_History_Reference L240 "Every real Antarctic research station became a Tepenian city" is the cited basis (Part C, D4).
M2 .t8_Step0_readerB:34, 100-108, 228 → remove Installation.
M3 .t8_Step0_readerC:38-48, 153-161, 228, 700-704 → remove Installation.
M4 Background-Lore scheduled for Step 1 "by developer ruling, 2026-09-29": readerA:377, 491; readerB:391, 509, 510; readerC:360, 559 → "NOT an input at any step… R-5 closes on the admitted set". The 2026-09-29 "vignettes move to Step 1" choice is overridden by the later "not canon, never an input" ruling (Part A note).
M5 .t8_Step1_readerA:28 row 3, :43, :129 Q6 name kept "Russia had been in Antarctica since the beginning, and it would remain." (spec L154 chars 20–309 excluded GPS) → row "EXCLUDED — GPS…Not scored"; delete L43, Q6; Fires 9→8.
M6 .t8_Step1_round3_reader{A:42, B:45, C:47-49} → "Not a Gate 9 item… Row withdrawn."
M7 .t8_Step1_readerC:29 A7 "rotating succession of national operators" (L150 chars 35–361 excluded) → records-only row.
M8 .t8_Step2_readerC:401-405, 539-540 "founding loss happened in 'that chain of handoffs'… Every shift change is a small version of that loss" → "Resolution [D]: continuity is built from shift changes…"; "C4, the shift: the system must never stop, and people must, so continuity is built from shift changes. [D]"
M9 .t8_Step2_readerB:176, 181-185 "the way the operators' knowledge was lost"; "written by more than one operator over centuries" → replacements given.
M10 .t8_Step2_readerA:179 "people don't survive handoffs but documents do" → "The founding generation arrived to documents with no one left to explain them."
AMBIGUOUS
A1 Resettled modifier (Step0 readerA:89-98; B:109-115, 528-531; C:45-48, 162-164; B H-2 "first population = real-world station operator").
A2 "in its own past" = station's pre-city past: Step2 readerA:489, B:442, C:488, round3 A:81, B:119.
A3 "Operator handoffs" labels Step1 readerA:15, 26; readerB:30, 78.
A4 spec L154 chars 1–19 "keeping the name" (Step0 PROOF lines A:667, B:699, C:842) — station name.
A5 Step 1 readers given excluded spans (root of M5–M7).
OTHER
O1 founding "unresolved" despite DR-9: Step1 readerA:27, 75-80; B:74, 112; C:153-160; round3 B:51 → "Resolved by DR-9: exiles from Russia, China and Australia; spec L150/L152 and L229 to correction docket."
O2 "Polity, Band 6" Step0 B:58, 178; C:94 → Band 5.
O3 "Act 1, answered" Step0 A:167, 492; B:228-229.
O4 Step0 B:507 "hub routes nine places"; Step2 A:454 COST-DOMINANT; Step2 A:233.
SPEC: Mirny spec L150/152 "(Primarily) Russian exiles", L154 name continuity, L229 "non-founding status" — spec fixes.

---

### C_Mirny_2 — Mirny pass folder 43 files (Step3/StepMINUS1 readers, 00.0, 00.1, 00.1b, 00.2, 00_Frame, 00b, 01, 01b, 02, 02b, 03, 03b, Datasheets/*, README) all full
Canon-track files state founders correctly (DR-9).
MISTAKES
M-1 Datasheets/Phase_7:50 "Technical/scientific 20% ('inherited Soviet/Russian institutional research capacity')" → strip gloss; SOURCE 16_Per_City_Three_Tier_Run.md L2121–2128 (DoI) carries it (16 L2154). ⚠ Subject to D8: DR-25 kept the DoI's "inherited [xyz] institution/capacity" citations.
M-2 Datasheets/Phase_5:11 "Real station: Mirny Station (Russia) … 'Hub of the Mirny... Arcanet subnet despite being Russian'" in Clean → "Region: East Antarctic coast · Arcanet subnet: Mirny — hub city"; SOURCE City_Relationship_Database.md L323–330 labels Mirny "Russian" — FIX SOURCE.
M-3 Datasheets/Step_1_and_2:24 "Primarily Russian exiles alongside a broader mix…" → "Founding population | Exiles from Russia, China and Australia (DR-9). Spec L152 'Primarily Russian exiles…' is contradicted by DR-9 → correction docket; not an input."
M-4 00.0_Pre-Trip:23 "Bellingshausen's ship Mirny | The real-world naming origin the current name and founding story are built around" → "The real station's naming lineage — GPS-excluded; not an input to the name or the founding (DR-19)."
M-5 00.0_Pre-Trip:24 "no longer resembles the Russian-station/ship basis the name and founding story are built around" → "⚠ FLAGGED FOR AN EVENTUAL RENAME, deliberately deferred (TODO.md L774-777, 2026-07-08). Founders: exiles from Russia, China and Australia (DR-9). The station and its ship-name lineage are a coordinate only (DR-19)…"
M-6 Datasheets/Step_-1:16, Step_0:18 "Real-world basis | Mirny Station (Soviet Union / Russia)" → "Real-world coordinate (GPS only) | Mirny Station, Davis Coast, East Antarctica".
M-7 Background-Lore G6 address scheduled: .t8_StepMINUS1_readerA:514-516, 141-143; readerB:50, 270, 337; readerC:96, 337, 433 → "G6 addresses: World_History_Reference.md and U Timeline Eras/ only. Background-Lore … never an input." ROOT: 00_RUNBOOK L1882–1883 lists Background-Lore/Cities/<Subnet>/<City>/ as G6 address — FIX RUNBOOK.
AMBIGUOUS
A-1 Installation via WHR L240 "Every real Antarctic research station became a Tepenian city": 00_Frame:124, 128-130, 566-568 Q-20; 00b:148 → answer No.
A-2 Resettled/D-5 00_Frame:113-119, 235 "FOUNDED ON AN INHERITED STATION" → Phase 2.
A-3 name kept: 00.1:327, 387; 01_Inherited:36; StepMINUS1 readerB:196, 268; round3 A:85-87, B:185-189, C:76-83.
A-4 Datasheets/Step_1_and_2:23 Founding row operator succession → relabel "Inherited infrastructure and records (DR-24/DR-25)".
A-5 Datasheets/Phase_2:19 "founding narrative built around Russian heritage" → "Resolved by DR-9…".
A-6 Datasheets/Phase_5:22-34 "Australian-heritage network" add DR-19.
A-7 Datasheets/Phase_5:17 "Dual-Kitchen Halls institutionalize Russian-Chinese coexistence" (from City_National_Connections) — drops Australia.
A-8 Datasheets/Step_3:9 Yakutsk/Nizhny Tagil Russia picks — chosen due to station?
OTHER
O-1 00_Frame:204-207 "Own earlier states — USED" vs DEFERRED (DR-16).
O-2 00_Frame:212-213 "Real-world comparables — PENDING Q-21" → USED (DR-15).
O-3 00_Frame:465, 501, 513-514, 569-574 stale.
O-4 00.1:116, 387, 401, 435-447 founders contested; readerA:471-473, B:323, C:399-400 → annotate RESOLVED by DR-9.
O-5 02_Spine:75 "three founding stocks weigh 37.29%" demoted decimals → tiers (DR-12); .t8_Step3_readerC:240.
O-6 workforce splits 02_Spine:67 & Step_1_and_2:21 vs Phase_7:46 (16 L275 vs §20).
O-7 Phase_2:10 13 vs 14 nations; Step_1_and_2:5, Phase_8:9 231 vs 230 lines; Step_0:12, Phase_2:13 76.20/1.93 → 76.19/1.92.
O-8 Phase_3:13-15 quote excluded L162, L168 (DR-10); Phase_7:49 developer vision.
O-9 Phase_3:16, Phase_6:9 light model stale.
O-10 README:37 path; :40 Step F; Step_3:8 stale.
O-11 Phase_8:11 placeholder; Phase_5:14 L184 roster; Phase_2:11 DR-4 stale.

---

### C_Sinheung — Sinheung pass 21 files all full. Russia mostly correct as GPS.
MISTAKES
M1 00_Frame:87 "one of only two cities settled this way rather than by organic inheritance." → "one of only two cities settled by the Jeju-do court allocation." (SOURCE: spec Legacy line, also Shirayuki spec)
M2 04_Phase_09:465-471 datasheet §20 quote "Russian-descended community… none of the residual institutional weight its own infrastructure might otherwise suggest" adopted as "GPS law working correctly… Adopted into D.7" → "Datasheet §20 gives the Russian-descended community a low-visibility claim. Recorded as a composition fact only (census: deferred). The station's operator nationality confers nothing on any resident community, and the datasheet's 'its own infrastructure… residual institutional weight' clause is docketed as a GPS violation, the same class as C.1."; 05_Reconciliation:140 strike "worth keeping", move to C.1 docket; 05:191 "folded into D.7" → "docketed (C.1 class)".
M3 Sejong Korean-founded: 04_Phase_05:227 "Sejong · Janbogo | 'one of Tepenia's three Korean-founded cities' — ceremonial kinship" → "Janbogo | shared Korean founding (Register: Janbogo = Korea, DR-22) — ceremonial kinship, 'genuine but limited'"; :277 → "Korea-founded is per the Founding Register (Jeju-do allocation); the relationship file's 'three Korean-founded cities' contradicts the Register (Sejong) and is docketed."; 09.5_Log:401 entry 321 superseded. SOURCE relationship file (City_Relationship_Database? / City_National_Connections) "one of Tepenia's three Korean-founded cities" — FIX SOURCE.
M4 Zhongshan via Jeju-do: 00_Frame:226 → "Three cities occupy this oasis; this site was allocated to Korea by the Jeju-do court (Shirayuki to Japan by the same court)."; 04_Phase_05:90 → "Three separate governments on one oasis; this city's title from the Jeju-do allocation."; 04_Phase_03:104, 09.5_Log:71, 163 → "worth a diplomatic claim"; 04_Phase_09:317-319, 09.6_Input_Audit:154-155, 09.5_Log:383 quote runbook §C.9c "Zhongshan China-founded — by the Jeju-do allocation" → annotate superseded (= U1 OTHER RUNBOOK:2141-2143).
AMBIGUOUS
A1 "Soyuz" placeholder from station namesake as founding deficit: 02_Spine:67-73, 140, 206, 226; 03_Research:319; 04_Phase_05:103-106; 09_Record:42-43; 09.5_Log:82, 202.
A2 03_Research:51 Volgograd pick (Inspirational-Influences L102-105) — station-derived?
A3 04_Phase_10:18-19, 87, 133 Baek Ji-hoon "adapting the inherited research infrastructure into the fabrication economy".
A4 01_Inherited:193-199, 09.5_Log:57 Mountain Pass kinship via census.
OTHER
E1 00_Frame:126, 02_Spine:68 "Soyuz" not Progress's namesake (Soyuz is different station) — spec error?
E2 chamber manufacturers two/handful/three (01:29, 110; 02:41, 211; 04_Phase_05:115; 00_Frame:216 vs 04_Phase_05:223; 07:210; 09_Record:34).
E3 09.6_Input_Audit:71-81, 09.5_Log:370 fabricated currency quote "not an abstract, faith-based fiat currency" (DR-3) → superseded.
E4 09.5_Log:182, 346, 352 unmarked superseded.
E5 02_Spine:258 2.6–3.7× vs 2.4–4.0×; 09.5_Log:70 107–153 km² stale.
E6 04_Phase_02:98-99, 09.5_Log:138 "furthest by reach" wrong; Yekaterinburg/Perm meridian loose.
E7 04_Phase_09:217 "against Esperanza's ~21,000" comparison → delete.
E8 04_Phase_10:56 "smaller and less advanced than the northern one".
E9 Register Sinheung row is 🟡 not ✅ (awareness).
E10 04_Phase_08:448 five vs three.
E11 04_Phase_05:279-281 flags City_Relationship_Database.md "Real station: Sinheung Station (Russia)". The source already reads "Progress Station (Russia)" (L433), so the pass's flag is stale.
E12 RUNBOOK §C.9c Zhongshan Jeju-do.

---

### C_datasheet — 179 files (DOCKET, README, follow-up (empty), 34 stub READMEs, 5 city READMEs, 5 Pre-Trips, 5 ledgers, datasheets for Cape Adare, Denison, DdU, Zukelli, Casey, Kunlun, Vostok) — all full. Pre-Trips/DOCKET/README/ledgers/stubs clean.
J=City_Development_Passes/Janbogo_Subnet, M=…/Mirny_Subnet
DdU (≠ France):
- J/Dumont_dUrville/Datasheets/Step_0:21 "a French city → a France-FOUNDED Tepenian city" → source wording "a Japanese city → a Japan-FOUNDED Tepenian city."
- Step_1_and_2:26 "French exiles built on Dumont d'Urville Station infrastructure… continuous French presence at the site from 1956" → "Settled post-Falkland Treaty on the existing Dumont d'Urville Station infrastructure (built by France/IPEV, 1956 — an infrastructure fact, DR-24); through the First Interwar the station was maintained by rotating operators; preserved journals, audio logs and orientation manuals gave the exiles a documentary starting point (records, DR-25). ⛔ The spec's 'French exiles' / 'continuous French presence' is ruled out by the Founding Register."
- Step_1_and_2:27 "Primarily French exiles…" → "⛔ Spec L164 founder line ruled out by the Founding Register (Dumont d'Urville ≠ France). Not an input."
- Phase_5:20 "IPEV… despite France being the founding/operating nation" → "Primary Dumont d'Urville Sea port for Australian freighter shipments (raw materials, staged via Hobart)."
- Phase_7:44 → "Staged via Australia, Hobart."
- Phase_7:42 St. Jules / "most distinctively francophone-speaking city" → "⛔ 16 §24 namesake/francophone note — not carried (DR-19; rule 7)."
- Phase_8:10 "French remained the civic-default language, an echo of the original station's operating history" → "⛔ Spec L176 language line derives the language from the station's operator — not an input (DR-19)."
- census: Step_1_and_2:28, Phase_2:9.
Zukelli (≠ Italy): Step_-1:27, Step_1_and_2:30, Phase_2:15 "Primarily Italian exiles" flagged only for census → "Spec L142: 'Primarily Italian exiles.' ⛔ Ruled out by the Founding Register (Zukelli ≠ Italy; Italy and the CIN founded Abowasa). Not an input (DR-19)." census Step_1_and_2:33, Phase_2:10. Also OTHER 14: "DR-19 pending approval" stale in same lines.
Denison (unruled): Step_1_and_2:25 "Australian exiles first… Cape Denison was Mawson's own base, so the founding claim on it was historical" → "Founding population — UNRULED in the Founding Register. ⛔ Spec L279's 'Australian exiles first' and its expedition-based reason are not inputs (DR-19, rule 7)."; :24 expedition legacy → "Settled post-Falkland Treaty at Cape Denison. ⛔ The expedition-legacy framing (spec L277) is real-site history — not an input."; :26, :27 delete; Phase_2:11 same as :25; Phase_2:12 delete; Step_-1:23-26 "admissible header fields… founded on the legendary Mawson expedition site" → retitle + ⛔; Phase_10:9 expedition hut landmark → add ⛔. census Step_1_and_2:28, Phase_2:7.
Kunlun (unruled): Step_1_and_2:32, Phase_2:16 "Chinese (CHINARE) exiles founded and named the station" → "Founding population — UNRULED (Founding Register). ⛔ Spec L168–170 makes CHINARE/Chinese exiles the founders — station operator as founder, not an input (DR-19)."; Step_-1:23-24 "Founding, Founding Population Resolution, Character & Culture… is clean" → "Admissibility of the remaining sections is Step −1's ruling. ⛔ Founding / Founding Population Resolution (L156–170) name the station operator as founders — DR-19 strike."; Step_0:20 "real-world founding nation is a GPS fact only" → "the nation that built or ran the real station is a GPS fact only". census Step_0:9.
Vostok (unruled): Step_1_and_2:29 "Primarily Russian exiles, given the station's deep Soviet/Russian institutional character." → "Founding population — UNRULED in the Founding Register. ⛔ Spec L128 derives it from the station's Soviet/Russian character — not an input (DR-19)."; Step_-1:13 "Full file, minus the exclusions" → "Admitted range — not pre-staged; Step −1's own ruling. ⛔ Spec L128 is a DR-19 strike candidate."; Phase_7:31 "Russian… liturgical language of science" → "⛔ 16 §23 founding-legend / 'liturgical language' note — not carried (DR-19, DR-25)."; Phase_7:52 Factions quote → delete; Phase_2:12 "Confirmed… by three independent sources" → "Spec L128 states Russian founders — UNRULED; DR-19 strike candidate; census tension deferred." census Step_0:16.
Casey (ruled Australia): Phase_7:53 "'inherited Australian Antarctic Division capacity' (heritage research)" → "Technical/scientific 15% — free. ⛔ 16 §21's 'inherited AAD capacity' gloss not carried (DR-25)."; Phase_5:34 → "⇒ Not admissible on any source: an 'X-heritage network' tie between cities is barred by DR-19."; Step_1_and_2:22 "Casey Station had been Australia's largest Antarctic station before exile" → "…on existing Casey Station infrastructure (AAD — infrastructure fact, DR-24); rotating operators; preserved journals, logs and manuals (records, DR-25)."; Step_1_and_2:24, Phase_2:8-9 "shortest Australia-to-Antarctica route of any Tepenian city" → "(founding wave — on a short, direct sea route from Australia)".
Cape Adare (rule 7 left open): J/Cape_Adare/Datasheets/Step_-1:25; Step_1_and_2:33; Phase_3:26; Phase_5:20; Phase_7:11-12; Phase_10:14; Step_3:11 → "real-site history — ⛔ not an input (rule 7); recorded only so Step −1 strikes it."
AMBIGUOUS: 1 Saints after explorers (Cape_Adare Step_1_and_2:35 St. Carsten; DdU Step_-1:25 St. Jules); 2 Zukelli Step_-1:17 named for Mario Zucchelli; 3 placeholders Cape_Adare Phase_10:13, Zukelli Phase_10:14 Italian names Elisa Faranda / Renzo Adorni; 4 Kunlun space/astronomy heritage composition (Step_-1:37; Phase_2:11, 17, 18); 5 "Mirny ('Australian')" subnet nickname (Casey Step_-1:19, Phase_5:11; Kunlun Step_-1:34, Step_0:14; Vostok Step_0:13); 6 Casey Phase_3:18 "Splinters" from records; 7 Vostok Phase_7:24 Lake Vostok research program 65%; 8 Kunlun Phase_8:12 "Unmarked background lore"; 9 Zukelli Step_1_and_2:32 founding tied to Janbogo; 10 Cape_Adare Step_3:11 Borchgrevink research topic; 11 Vostok Step_5:12-17 Local_Cultures at one remove.
OTHER: 1 Concordia/README:37 broken path; 2 Denison Step_-1:77-102 copies City_Vision_Notes (DR-10); 3 Denison Phase_7:7 base% 44.4 vs 53.2; 4 Denison Step_8:17 "declined" defn; 5 religion roster 2 vs 6; 6 Kunlun Phase_6:42 zero holiday hits vs Pre-Trip L318; 7 Vostok Step_3:12 genetics folder exists; 8 Vostok Phase_3:7, Step_3:13 concept-art; Phase_3:8 megasheet count; 9 Vostok Step_5:9 xref; 10 Vostok Pre-Trip:335 §J; 11 Casey Phase_7:55 tally; Phase_4:21, Phase_6:9 Mirny comparisons; 12 Casey Step_0:16 altered quote; 13 06 provenance line counts; 14 Zukelli DR-19 "pending" stale; 15 Kunlun Step_1_and_2:32 vs :31; 16 DdU Pre-Trip:31 "above"→below; 17 DdU Phase_5:19 "Cape Denison".

---

---

## PART E — STATUS AND PARKED QUESTIONS (2026-10-01, evening)

**Applied.**
- Part B (methodology seeds) and Part C (source files) were applied by the orchestrator.
- Part D was applied by ten parallel fixers, one per partition, each checking every non-heritage item against its
  source before changing it.
- Raw records were archived, not edited (`DR-27`).
- The fixers' reports are in the session scratchpad (`ulmread/fixreports/`).

**Verified.**
- The founder-check script now flags only ⛔ rule markers and census tags inside ULM and pass files. All other hits
  sit in the revisit cities' own text: specs, culture files, megasheets.
- The forbidden-phrase sweep is clean. The one quoted megasheet line in `16` §Davis is left alone under `DR-29`.
- The British-spelling sweep of every changed file is clean.

**Parked for the developer — none of these blocks anything:**

1. **The Davis↔Mawson connection** rests on the two namesakes' real history (Aurora relief voyage). `DR-28` says that
   is not an input; `DR-29` keeps Davis as written. Keep it, re-ground it on both cities' Australian founding, or drop
   the namesake story? (`City_Cross_Subnet_Relationships.md` Part 3 left untouched pending this.)
2. **CST techniques inside the ULM** — the Unrecognized Instrument (Step 3.6), the Zodiac Lens (Phase 10 §B2), the
   Surviving Witness and Necessity Before Meaning. Their CST citations are gone. Does `DR-14` bar the techniques
   themselves?
3. **Sayowa's name** — `{{ Syowa/Showa }}` was written as a placeholder; add it to the rename list (`R-17`)?
4. **Sinheung**
   - "Soyuz" is a different real station from Progress, so the spec's naming note is wrong somewhere.
   - Chamber manufacturers: two, a handful, or three?
   - Confirm the reworded spine deficit, "a title it did not win / nowhere at all".
5. **Shirayuki**
   - "Bharati Station" as an in-world landmark name versus the spec's CANON NOTE.
   - Shore or inland (`Ports.md` §5.6c versus two pass lines and the real coastal site).
   - The spec gives ~15 km to Zhongshan; its own coordinates give ~8 km.
6. **Mirny**
   - The mandated workforce share is 11.8% (`16` L275) or 23.6% (`16` §20, which rests on a vision note that may fall
     under `DR-10`).
   - Is "Two Days a Year" canon or open?
7. **Casey**
   - The "Splinters" bar is revived from the real station's own records (records versus site history).
   - The founding creed comes from the Wilkes ruins.
8. **Placeholders**
   - Zukelli's Italian names (Faranda, Adorni).
   - Cape Adare's "heritage documentation of Borchgrevink's hut".
9. **`DR-10a` scope** — the developer-vision quotes in the Zukelli and Dumont d'Urville datasheets.
10. **St. Carsten** is not on the `National_Holidays.md` Saints roster. Is he a Saint?
11. **Cape Adare's New Zealand "earliest founding wave" census tag** may itself be station-derived (census review).
12. **`02` §4.1's "in a neighbor's present" deficit address** has no valid case left. Keep it?
13. **Zhongshan** — "nobody was taught it" is applied to the continuous population's everyday culture (cuisine,
    writing). Does that match the law?
14. **Act 1's length** conflicts inside the law file itself (`No_National_Stereotypes.md` L111 vs L131).
15. **Davis**
    - Harbor season (`H65`).
    - Hobart/Fremantle staging versus the port ruling's TAAF/HIMI hubs.
16. **The LAW 0-R "founding" research angle** (copied in `CLAUDE.md` and elsewhere) versus `DR-28`.
17. **FYI** — the ULM copy of `00f_Review_Panel.md` now letters its archived district cases "District A–F", per the
    file's own pointer header.

**Still needs approval:** the law file `No_National_Stereotypes.md` (I-2/I-3) together with its quick-reference
copy; `CLAUDE.md` (I-21); the check hook (I-22).
