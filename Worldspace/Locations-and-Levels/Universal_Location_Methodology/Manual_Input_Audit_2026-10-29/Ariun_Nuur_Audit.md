# Ariun Nuur (pass folder `Ariun_Nuur`; sheets still say "Vostok") — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (205 lines), the whole Pre-Trip (566 lines), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `AN-…`). Pass folder: `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/` (renamed from `Vostok` on 2026-10-23). `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run.

**Verdict.** **Nothing blocks a run.** Unlike Casey and Mirny, this city's sheets were brought up to the 2026-10-28 census (the population scenario sync, commit `5ee58d0e`): Census I, the `09` row, the `16` workforce and the retention-free Census II absence are all current. What is left: **(1)** the Pre-Trip's line lists for eight shared files are stale (the usual +1 to +23 shifts), and a handful of its statements describe the rename state of 2026-09-30; **(2)** the Phase 2 per-nation counts are still the pre-census-change set; **(3)** five sheet rows quote the spec with the old name "Vostok" where the live spec now says "Ariun Nuur", so they are not verbatim; **(4)** the sheets contradict themselves about the `09` baseline (41.5% in one row, 42.0% in the next); **(5)** the spec still says "no highways, no neighboring cities" and "#2 coldest" in places that the Hwy 37 correction and the mean-temperature change have overtaken; **(6)** the pass README's four source pointers still name `Vostok`.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Mirny subnet/Ariun_Nuur.md` (205 lines); every spec line the sheets cite (L5–L11, L17–L24, L30, L32–41, L49–53, L57, L61–66, L70–73, L76, L79–80, L86–99, L104, L109–112, L128–132, L154, L158–167, L169, L173–179, L183–193, L199) lands on what the sheet says | ✅ (the "203 lines" count is off, **D-06**) |
| Census Section A heading **L432**, entry L434–440 (the note at L440 quoted word for word), Census I row **L508**, other lines L530, L642; Census II: none (census L642/L644 say Byrd and Vostok are "not yet computed") | ✅ |
| Census I **141,755 H / 271,422 R / 413,177** in the spec (L17) and the census row | ✅ equal; sheets carry the new values (`Step_0`, `Phase_2` row 12, `Phase_4`, `Phase_9`) |
| Per-nation table: shares sum to **100.00%**; robot column sums to **271,422**; human column to **141,755** (hand-added); tier lists equal the table (2 / 4 / 2 nations) | ✅ |
| Monthly means average **−54.77 °C** (stated −54.8); monthly precipitation sums to **22.0 mm** (stated 22); polar night Apr 24 → Aug 21 = **120 days**, midnight sun Oct 22 → Feb 21 = **123 days**; record low −89.2 (Jul) and record high −14.0 (Jan) match the table | ✅ |
| `READER/Vostok.md` is the real climate file (the file has not been renamed; no `READER/Ariun_Nuur.md` exists); the sheet cross-check is right | ✅ |
| `09` row **L57** (D 2.50 · 141,755 · 413,177 · Required **143,796** · Workforce **342,300** · 42.0%) matches the sheet; `16` Half B row workforce **342,300** = 271,422 + 0.5 × 141,755 = 342,299.5 | ✅ |
| `16` Half B header **L241–248**; `01` §6 **L199**, caveat **L306–307**, pilot row **L284**; `08` **L22, L505, L573, L605, L715, L730**; Sweep **L90, L169, L249–250**; Factions `Second_Interwar` **L280** ("Still not represented: Ariun Nuur, Denison"); `Inspirational-Influences.md` heading **L92**, picks L93–95 (CRISPR, MIP, ChemMatCARS); runbook registry for `Vostok_Genetics_Research/` at **L2074** (the Step_3 sheet is right; the Pre-Trip is not, **A-02**) | ✅ |
| Zero-hit claims re-run: `06` provenance (0 hits, **D-08** for the line count), National Holidays, Ice-Cold Buddhism folder, Meme Machine and True Believer extractions, Geothermal, `Robot_Universals`, Enneagram index, Theoretical-Calculations | ✅ (Robot_Religions: the single hit is `Cymatics_reverence` **L19**, as the sheet says; NatConn's own section **L333–344** has the five relations the sheet counts; Factions has two files naming the city, as the sheet says) |
| Characters canon: Calethina README **L56** and `Formative_History.md` **L7** ("a since-defunct Vostok/Kunlun joint venture"), and Charlene's README under `Dolls/TBN [XT-17 …]/` | ✅ the facts (**D-13** for the count) |
| `Extent_and_Density_Per_City.md` row **L625** and other lines **L249, L578, L587**; `Highways` L5, L156, L162–163, L170; `Arcanet` L26; `RobotPhys` L409; `NMCI` L16, L98–99, L107, L109, L231; `11` L142, L144, L357; `Stations` L67, L97; `Precipitation_Falls_vs_Lands.md` and `City_and_District_Research_Topics.md` L278–279 | ✅ unchanged |
| All addresses tested: Local Culture, Local Robot Culture, Enneagram file, vision notes, the Neo-Races catalog (`Neo-Races-and-Cultures/Mirny_Subnet/Ariun_Nuur/Ariun_Nuur_Catalog.md`), the concept-art folder `…/Ariun_Nuur/` (empty), `Vostok_Genetics_Research/` (3 files), the megasheet folder `…/Vostok/` (6 `.md` files and 1 subfolder: the Pre-Trip's "7 files" counts entries) | ✅ |
| Runbook anchors L216, L309, L378, L430, L747, L1982, L2060, L2090, L2150, L2696–2698; LAW 0-R body at **L2573** (heading L2571) | ✅ |
| Pre-Trip §I count "DATASHEET-NOT-YET-BUILT(N-5)=0" and "19 files, all present" | ✅ no stale "not built" sentence |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §D and §E, vs live). Airports L18, L49, L53 → **L18, 52, 56**. Ports L205, L459, L717 → **L205, 482, 740**. CrossSub L227 → **L228**. `09` L57, L199, L237, L239 → **L57, 201, 239, 241**. RelDB L14, 26, 49, 105 same; L124, L169, L226, L272–273, L465–466, L473, L520 → **L135, 180, 237, 283–284, 476–477, 484, 531**. NatConn L243, L281 same; L320, L332, L336, L338–339, L342, L507–508, L559, L565, L576 → **L321, 333, 337, 339–340, 343, 512–513, 564, 570, 581**. `16`: row L281 → **L282**; L80, 114, 222, 232 same; L673 → **L678**; L1817 → **L1822**; L1904–1905 → **L1909–1910**; L2149 → **L2154**; L2348, 2352, 2363, 2374, 2376, 2391, 2393, 2396, 2402, 2412, 2414, 2423 → **L2353, 2357, 2368, 2379, 2381, 2396, 2398, 2401, 2407, 2417, 2419, 2428**, and add **L2349** (the §23 heading). Census: add **L644** (the DR-68 scenario note). | live `grep -n` of each file | Re-read each list live (SH-010) |
| **A-02** | STALE | §J "the runbook's §C.9 registry (L2072) tags `Vostok_Genetics_Research/` Phase 7": the registry row is **L2074** (L2072 is the `jobs_professions_and_fields/` row; the Step_3 sheet already says L2074). | runbook L2072, L2074 | Correct |
| **A-03** | WRONG | §A "the megasheet and concept-art folders keep `Vostok`": the **concept-art** folder is `Ariun_Nuur` (renamed 2026-10-23; the Pre-Trip's own Phase 3 row uses it). Only `City_Megasheets/Mirny_Subnet/Vostok/` keeps the old name. | `ls` | Reword |
| **A-04** | STALE | §A "Other scripts / variant spellings … the spec's first 25 lines hold no non-Latin script" (checked 2026-09-30): the spec now carries Mongolian **Ариун Нуур** ("the pure lake") at L10 (added with the 2026-10-03 rename). Also not in the alias set: **Southern Pole of Inaccessibility** (spec L5, L49), **Lake Vostok** is listed. | spec L10 | Add the alias; reword the "checked" row |
| **A-05** | GAP | **Founding Register is not an address.** Rows that name the city: **L63** (its own row), **L84** (the `DR-35` ruling), **L92** (the rename), **L94** (the cleanup); Kunlun's row **L64** names it as a relation. The Pre-Trip only mentions the file in passing at §A ("Founders unchanged"). | Register | Add to §D Phase 2 and §J (as Casey's note) |
| **A-06** | GAP | **Two research files made today are in neither the Pre-Trip nor the sheets:** `Research_Logs/Ariun_Nuur_Inspiration_Place_Research_R1.md` and `_R2.md`. `Step_3` says only that no Vostok-named log exists; the Pre-Trip says the Step 3 log `Ariun_Nuur_Research_Log.md` does not exist (still true). | `ls Research_Logs` | Register with a tier |
| **A-07** | STALE | Pass `README.md` "existing sources" names the old city name in all four pointers: `../../../Specs/Mirny subnet/Vostok.md`, `Local_Cultures/Mirny_Subnet/Vostok.md`, `City_Vision_Notes/Vostok.md`, `Research_Logs/Vostok_Research_Log.md`. Real: `Specs/Mirny subnet/Ariun_Nuur.md`, `Local_Cultures/Mirny_Subnet/Ariun_Nuur.md`, `City_Vision_Notes/Ariun_Nuur.md`, `Research_Logs/Ariun_Nuur_Research_Log.md` (does not exist yet). (The README source-pointer sweep was deferred by the developer to the end; it belongs in the sweep.) | README | Re-point |
| **A-08** | NOTE | The Pre-Trip title ("Vostok — Pre-Trip Inspection"), every sheet title and most row text still use "Vostok" for the city; the folder is `Ariun_Nuur`. The Pre-Trip §A explains the rename. Whether to rename inside the sheets is the developer's call; doing so changes quoted text (**D-05**). | | DECIDE |
| **A-09** | NOTE | §C Step 10 range 3057–3172, Step 5/Round 3 ranges, spine L127, runbook L2178 — the shared items (SH-001 … SH-007). Megasheet folder "7 files" = 6 files + 1 subfolder. | | shared |
| **A-10** | NOTE | `Step_8`, `Step_9`, `Step_10` are the older short form: none points to its Tier U sheet (`Review_Panel_Full_Text_Quick_Reference.md`, `Step_9_Record_Full_Text_Quick_Reference.md`, `Step_10_Readiness_Check_Full_Text_Quick_Reference.md`, all of which exist); the corpus' newer sheets (Kunlun, Mirny) carry the pointer and a quick index. | `Corpus_Reference_Sheets/` | Add the pointers (**D-11**) |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened, `DR-8`) · G2 climate ✅ · G3 `16` Half B + §23 ✅ · G4 Register row ✅ (not an address in the Pre-Trip, **A-05**) · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ (CRISPR, MIP, ChemMatCARS) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ not in the sheets (**D-10**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Arithmetic and tables are right (see 1a). Source-level findings:

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **L49 says "There are no highways, no coastal access, no neighboring cities."** The same file says the opposite three times after the 2026-07-06 correction: Highway access (L9, "sits on Hwy 37 … between Kunlun and Concordia"), Connection to Concordia (L177) and Current Status (L187). The correction fixed those and left the Geographic Basis paragraph. | spec L9, L49, L177, L187 |
| **S-02** | STALE | **L142: "the 1,260km of plateau between Ariun Nuur and its nearest subnet city"**: Kunlun, a Mirny-subnet city, is a direct Hwy 37 neighbor (L9, L118). The 1,260 km is the distance to Mirny, the hub. | spec L9, L118, L142 |
| **S-03** | WRONG | **L77 "it is the #2 coldest of the 37"** states a peer rank and contradicts L61 ("the coldest mean annual temperature of any Tepenian city") and L10 ("Coldest city in Tepenia"). The means in the live specs are Ariun Nuur −54.8, Kunlun about −54, Dome Fuji about −53, so L61 and L10 are right and the rank is stale. The `Step_1_and_2` sheet row 19 copies "#2 coldest of the 37" (**D-09**). | spec L10, L61, L77 |
| **S-04** | NOTE | Precipitation regime: falls ~25, lands ~22, "lost ~2" (L71–73): 25 − 22 = 3. Retention 22/25 = 88% (stated ~90%). Rounding, but it does not close. | spec L71–73 |
| **S-05** | NOTE | L63 "warmest month (December/January) avg −28 °C": the warmest monthly **means** are −31.3 (Dec) and −31.9 (Jan); the average **highs** are −27.1 and −27. −28 matches neither. | spec L63, L88, L99 |
| **S-06** | NOTE | L169 gives Charlene's character folder as `…/Dolls/Still-Present_-_In-Game/recruitable/TBN […]/`; the folder is now `Characters/Dolls/TBN [XT-17 unorthodox science teacher Charlene]/`. | spec L169; `find` |
| **S-07** | NOTE | The timeline repo's `Worldspace/Locations/README.md` L20 still lists "Vostok" (rename sweep held). Flag only. | README L20 |
| **S-08** | NOTE | Census II "Not yet computed" (L18) agrees with the census (L642/L644: Byrd and Vostok not yet computed). No conflict, unlike Kunlun. | |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ every excluded-section line range (L6, L183–187, L191–193, L173–179, L10, L154, L199, L114–122, L11) and the founding line; ❌ **D-06** |
| `Step_0` | ✅ Census I current; Census II absence; L5, L49 |
| `Step_1_and_2` | ✅ climate rows L57–L76, L79–80, L86–99, L104; `09` L57; `08` L505 labelled snapshot; picks; ❌ **D-04**, **D-05**, **D-09**, extent row missing |
| `Step_3` | ✅ picks L92–95, registry L2074 |
| `Step_5` | ✅ stub; Factions L280 |
| `Step_6` | ✅ ten sections; ❌ **D-11** (no Subnet column) |
| `Step_7` | ❌ **D-02**, **D-10** (the note) |
| `Step_8`, `Step_9`, `Step_10` | ❌ **D-11**, **D-08** |
| `Phase_2` | ✅ tiers, de-stacking note (L30), Census rows; ❌ **D-01** |
| `Phase_3` | ✅ L49–53, L111–112, L160–163 land; ❌ **D-05** |
| `Phase_4` | ✅ `09` L57; `11` quote L142–144; ❌ **D-02**, **D-03** |
| `Phase_5` | ✅ spec L7, L9, L49; ❌ **D-07**, **D-14** |
| `Phase_6` | ✅ Cymatics L19, zero-hit rows; ❌ **D-12** |
| `Phase_7` | ✅ `01`, `08`, Sweep, Factions L280; ❌ **D-04**, **D-14** |
| `Phase_8` | ❌ **D-06** |
| `Phase_9` | ✅ robots 271,422 ÷ 413,177 = **65.7%** |
| `Phase_10` | ✅ the facts; ❌ **D-13** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Phase_2` · per-nation row | Counts are the **pre-`DR-68`** set (USA 73,631 R / 36,757 H; Japan 64,846 / 32,372; … robot column sums to 259,644). **Live (spec L34–41):** USA 76,971 R / 40,199 H · Japan 67,788 / 35,404 · Canada 37,730 / 19,706 · Indonesia 36,771 / 19,205 · Australia 17,513 / 9,146 · South Korea 16,554 / 8,645 · Chile 13,457 / 7,028 · New Zealand 4,638 / 2,422. Shares unchanged. | Replace |
| **D-02** | WRONG | `Phase_4` row 14; `Step_7` note | "`09`'s baseline (41.5%) and `16` §23's (37.4%) differ": `09` L57 reads **42.0%** (the sheet's own row 13 and `Step_1_and_2` say 42.0%). The gap is also partly a denominator effect: `16` §23's worker counts (121,353 + 66,007 + 137,092 = 324,452) are the **pre-`DR-68`** workforce, while `09` and the Half B row use 342,300 (`16` L1 says per-city determinations were not recomputed). | Correct 41.5 → 42.0; label §23 as pre-`DR-68` |
| **D-03** | STALE | `Phase_4` · DoI carve-out row | "(129,617 humans)": the current human count is **141,755**. | Replace |
| **D-04** | STALE | `Phase_7` · Half B row; `Step_1_and_2` row 27; `Phase_7` row 24 | Half B row cited **L281** → **L282**; its values "Baseline 37.4%, Mandate 5.8%, Free 56.8%" → live **37.8% / 5.8% / 56.5%**. `16` §23 cited **L2344–2350** → **L2349–2355** (+5). | Replace; re-read the section |
| **D-05** | WRONG | `Step_1_and_2` row 26; `Phase_3` rows 13, 15, 16 | Quoted "verbatim" text reads "Vostok" where the live spec reads **"Ariun Nuur"**: spec L110 ("paradoxically, Ariun Nuur is much calmer"), L111 ("the sky at Ariun Nuur"), L49–51 ("Ariun Nuur sits near … at Ariun Nuur's location"), L160–163 ("most significant structures in Ariun Nuur"; "The Ariun Nuur research archive"). `Phase_3` row 16 also joins fragments from L160 and L162 with no ellipsis. | Re-quote from the live text |
| **D-06** | STALE | `Step_-1` · "Specs file, 203 lines"; `Phase_8` · "full 203-line file" | Live `wc -l` is **205**. | Re-count (SH-009) |
| **D-07** | STALE | `Phase_5` · Port status | Ports **L459, L717** → **L482, L740**. | Re-point |
| **D-08** | STALE | `Step_10` | "`06` (429-line file) … zero hits for Vostok": **431** lines now; zero hits for "Vostok" and "Ariun Nuur" re-run. | Re-count |
| **D-09** | NOTE | `Step_1_and_2` row 19 | Includes "#2 coldest of the 37" (a peer rank) while row 22 says the ranking clauses are not carried; see **S-03**. | Drop the rank |
| **D-10** | GAP | `Step_0`, `Step_1_and_2`, `Step_7` | No extent row, and the `Step_7` note says Vostok's "own extent/area figure [is] not yet located". It is: Extent **L625** (Mirny · 389,261 · **39 km²** @10,000/km² · **56** @7,000 · plateau) — a 2026-09-05 snapshot; at the live 413,177 the same arithmetic gives **41.3 / 59.0 km²**. | Add the row (labelled snapshot); fix the note |
| **D-11** | GAP | `Step_6`, `Step_8`, `Step_9`, `Step_10` | `Step_6` section-1 columns lack **Subnet**; `Step_9` lacks item 5; `Step_8`, `Step_9`, `Step_10` carry no pointer to their Tier U sheets (they exist; A-10). | As Casey, plus pointers |
| **D-12** | NOTE | `Phase_6` | "378-line file" / "293-line file": `wc -l` is 377 / 292 (XS-9). | Re-count |
| **D-13** | NOTE | `Phase_10` · Characters row | "2 files matched": it lists **three** (Calethina README, `Formative_History.md`, Charlene README), and three is the live count. | "3 files" |
| **D-14** | NOTE | `Phase_7` · Sweep matrix row; `Phase_5` · Universe `Locations/` rows | Sweep legend "elsewhere in file": it is **L139**. The Universe `Locations/` directory "4 `.md` files read" (2026-10-23): README.md (L20) is the only one that names the city; the directory now holds 2 top-level `.md` files plus folders. | Cite L139; re-enumerate or leave as dated |

### 2d. DECIDE items (collected)
1. **A-08** Rename "Vostok" to "Ariun Nuur" inside the Pre-Trip and sheets (which fixes the quoting issue D-05 at the same time), or leave the sheets keyed to the old name?
2. **A-06** Tier for the two new research files.
3. **S-01 / S-02 / S-03** Approve three source edits in the spec (L49, L142, L77), or leave for the culture pass?
