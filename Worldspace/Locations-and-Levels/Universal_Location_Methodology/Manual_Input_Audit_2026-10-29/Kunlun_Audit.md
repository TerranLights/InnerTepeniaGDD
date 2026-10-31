# Kunlun — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (250 lines), the whole Pre-Trip (567 lines), all 19 datasheets, the pass README and the coverage ledger; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `KL-…`). Pass folder: `City_Development_Passes/Mirny_Subnet/Kunlun/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`.

**Verdict.** **Nothing blocks a run.** Kunlun's sheets are in good shape on content (the climate rows, the founding row, the Phase 6 quotations and the Phase 10 character facts all match their sources). What is left: **(1)** the Pre-Trip line lists for six shared files are stale, and two lists are short (the Founding Register is not an address at all; the census and Division-of-Industry lines are missing some lines that name the city); **(2)** the per-nation robot counts in the spec (and so in `Phase_2.md`) still sum to the **old** Census I total (123,449 against the live 135,226), and the spec says "19 nations" over a table of 20 rows; **(3)** a stale cold-city statement and an authoring remnant sit in the spec; **(4)** a handful of small citation slips in the sheets (one wrong heading line, two off-by-one lines, a "no research file" sentence that is no longer true); **(5)** the extent row is missing from the sheets, and the Step 7 note that says the extent figure "is not located" is out of date.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Mirny subnet/Kunlun.md` (250 lines; "Based on" L20, subnet L22, highway L24, founding L156–170, "forbidden as a protective safety measure" L180, Vosora flag L250) | ✅ all land |
| Census I row **L517** (0 humans · 135,226 robots); Section A heading **L444**, entry **L446–452**; Census II: no row (census **L642** and the DR-68 note **L644** both say Kunlun, Dome Fuji, Byrd and Vostok have none) | ✅ the sheets' "Census II does not exist" is source-supported |
| Extent row **L627** (Mirny · 123,449 · 12 km² @10k · 18 km² @7k · Dome A), table header **L603–604**, snapshot note **L631**, other lines **L249, L578, L587** | ✅ (a dated snapshot, by design) |
| Founding Register row **L64** (text matches the sheets' founding row word for word) | ✅ (but see **A-02**) |
| `Stations` L31 (Kunlun Skiway), L97; NMCI zero hits; Arcanet; Geothermal (198 lines, zero hits); `11` L334/L339; CrossSub; Topics L263–264; Precip L119; Holidays L124, L159; RobotPhys L379, L408–409; ColdPhys L8, L181 | ✅ |
| `READER/Kunlun.md` twelve monthly means equal the spec's Mean column; annual mean −53.9 | ✅ |
| Pass README spec / local-culture / vision-notes pointers (`../../../Specs/Mirny subnet/Kunlun.md`, `Local_Cultures/Mirny_Subnet/Kunlun.md`, `City_Vision_Notes/Kunlun.md`) | ✅ all resolve; research-log pointer is marked "may not exist yet" and does not (two other research files do exist, **A-05**) |
| Pre-Trip §I count "DATASHEET-NOT-YET-BUILT(N-5)=0" | ✅ true (all 19 files exist); no stale "not built" sentence in this Pre-Trip |
| Position-coverage ledger (all blank, "pass has not yet begun") | ✅ |
| Zero-hit claim for `06_Worked_Example_Provenance.md` | ✅ re-run: 0 hits (file is now 431 lines; **D-03**) |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip vs live). Highways **281→296** (live 156, 162, 163, 170, 296). Airports **48, 52→51, 55** (L18 same). Ports **459, 717→482, 740** (L182, 205 same). RelDB (sheet 124, 169–170, 193, 226, 265–266, 472–473, 501, 520) → **135, 180–181, 204, 237, 276–277, 483–484, 512, 531** (L26, 49 same). NatConn: sheet 308, 316–317, 324, 327, 329, 333, 339, 342–343, 499, 502, 508, 516, 593 → **309, 317–318, 325, 328, 330, 334, 340, 343–344, 504, 507, 513, 521, 598**. `09`: L108, 211, 219, 223, 237 → **110, 213, 221, 225, 239** (L89 same). `16` (list below). | live `grep -n` of each file | Re-read each list live (SH-010) |
| **A-02** | GAP | **The Founding Register is not an address in this Pre-Trip.** The word "Register" never appears; the sheets cite `Founding_Register.md` with no line number. Founders come only from the Register (`DR-19`), and it holds four lines naming the city: **L64** (the row), **L83** and **L84** (the 2026-10-03 rulings: Kunlun's stock follows Ariun Nuur) and **L94** (the 2026-10-13 cleanup). Casey's Pre-Trip carries the row and a §J note; this one carries neither. | Register L64, 83, 84, 94 | Add the Register to §D Phase 2 (with the four lines) and add the §J note as in Casey's sheet |
| **A-03** | GAP | **`16` list is short and shifted.** Live lines naming the city: 114, 116, 185, 222, **286** (Half B row; sheet L285), 336, 1823, 1909, 1911, 2154, **2256** (Kunlun's own §22 heading, not in the Pre-Trip list), 2275, 2280, 2291, 2296, 2308, 2309, 2314, 2337, 2364, 2417, 2428, 3201, 3209, 3231, 3236, 3250, 3569. §J's "16 open-items table row 15 (L3564)" → **L3569**. | `16` | Re-read live; add L2256 |
| **A-04** | GAP | **Other lines that name the city are missing from the Pre-Trip lists:** NatConn **L239, L241, L282** (other cities' sections that name Kunlun); census **L548** (Census I sum note, "Kunlun and Dome Fuji have no humans") and **L644** (the DR-68 scenario note, "still have no Census II rows"); census **L588 → L589**. | NatConn, census | Add / correct |
| **A-05** | GAP | **Two research files made today are in neither the Pre-Trip nor the sheets:** `Research_Logs/Kunlun_Inspiration_Place_Research_R1.md` and `_R2.md`. `Step_3.md` says `Cities/Research_Logs/` holds no Kunlun file (**D-02**). | `ls Research_Logs` | Register with a tier (whether the run may read them is the developer's call) |
| **A-06** | STALE | §A alias row "Dome Fuji · Mountain Pass Airport": "Mountain Pass Airport is the waypoint between Kunlun and **Vostok**" — the city is now **Ariun Nuur** (the folder and the real site keep "Vostok"). | Pre-Trip §A | Reword to "Ariun Nuur (folder Vostok)" |
| **A-07** | GAP | Alias set misses names the shared files key on: **CHINARE** (spec L20 "Based on: Kunlun Station (China / CHINARE)"; the Register and the founding rows use it), **Mountain Cut Throughway** (Hwy 37's name, spec L24; the highway and airport files use it). | spec L20, L24 | Add to §A |
| **A-08** | NOTE | §C Step 10 range, Step 5 and Round 3 lines, runbook L2178, spine L127 and the "skip line 65 of `01`" instruction are the shared defects already logged (SH-001 … SH-007, XS-7). | | shared |
| **A-09** | NOTE | Pre-Trip §K "Concept-art directory" and megasheet counts: not re-counted here beyond the empty `.gitkeep` directory (the sheet says "EMPTY — .gitkeep only"), which is right. | | none |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened, `DR-8`) · G2 climate ✅ · G3 `16` Half B + §22 ✅ (they disagree, **S-06**) · G4 Register row + `Founding population:` ✅ (but not in the Pre-Trip, **A-02**) · G5 `Access type` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ (Kunlun's row exists: NOIRLab, Kitt Peak / Mauna Kea, CHEXS/CHESS, MIT) · G8 census tier table + composition ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ missing from the sheets (**D-10**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: the 20 per-nation shares sum to **99.99%** (rounding; 15.43 + 15.22 + 11.45 + 7.19 + 6.75 + 6.48 + 6.38 + 5.26 + 4.05 + 3.33 + 2.65 + 2.47 + 2.44 + 2.37 + 2.35 + 2.14 + 1.75 + 1.16 + 1.07 + 0.05); the robot counts sum to **123,449** exactly (see S-01); monthly means average **−53.96 °C** (stated −54); monthly precipitation sums to **19.0 mm** (stated 15–20); polar night Apr 18 → Aug 26 = **131 days**, midnight sun Oct 17 → Feb 26 = **133 days**; the record extremes match the table.

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **The per-nation robot counts were not rescaled for the census change.** The table (L50–69) sums to **123,449** — the old Census I robot total. Census I row L517 now reads **135,226** (+11,777, `DR-68`). Every sheet row that restates a per-nation count (`Phase_2.md`) is faithful to the spec and therefore also stale. The same old total sits in `08_Volume_Based_Requirement_Reference.md` L506 / L518 / L719 / L733 and `01_Burden_Scoring_Model.md` L110 / L285 (the Division-of-Industry files; whether they are labelled dated snapshots was not checked beyond these lines). | spec L50–69; census L517 |
| **S-02** | WRONG | **"19 nations" over a 20-row table.** The spec says 19 nations (L162) and "a further sixteen" beyond the three Primary (L82), but the table has **3 Primary + 8 Significant + 9 Notable = 20** rows. The 20th row, **Netherlands, is 0.05% / 62 robots** — a tenth to a fortieth of every other Notable row (1.07–2.47%). | spec L50–69, L82, L162 |
| **S-03** | STALE | **L103 still reads "At −58.0 °C it is the #1 coldest of the 37".** The mean was corrected to **−54 °C** (L89, the table, the READER file; the sheet's `Step_1_and_2` row says the earlier −58 was wrong). The sentence also states a peer rank, against the one-location law. | spec L89, L103 |
| **S-04** | WRONG | **Authoring remnant at L106:** "…similar to Concordia's ~82 days... wait, at 80°25'S this would be longer" — a note to self left in the text (and a peer comparison). | spec L106 |
| **S-05** | DECIDE | **Census II wording.** Spec L34 says "Not yet computed"; the census (L642, L644) says Kunlun and Dome Fuji "remain without Census II figures for the same reasons given at the Census I table" (an absence by design), and names Byrd and Vostok as the ones "not yet computed". | spec L34; census L642, L644 |
| **S-06** | DECIDE | **`16` contradicts itself on Kunlun's Mandated/Free split.** Half B row L286: Mandated **0.0%** / Free **71.4%** (source "–"). §22 (L2256 on): Mandated **26.8%** / Free **44.6%** (provisional; register item 15 marks it for the developer's review). `Phase_7.md` explains the 0.0% as "a pre-determination snapshot … unassessed", which is an inference the source does not state. | `16` L286, L2256, L3569 |
| **S-07** | NOTE | `16` §22's worker counts (35,306 / 33,054 / 55,089) sum to the old 123,449; `16` L1 says per-city determinations were not recomputed after `DR-68` (labelled, not an error). | `16` L1, §22 |
| **S-08** | NOTE | The timeline repo's `Worldspace/Locations/README.md` L20 still lists "Vostok" in the Mirny subnet (rename sweep held). Flag only; the timeline repo takes no worldbuilding edits. | README L20 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ boundaries, founding strike text, census lines; ❌ **D-12** (spec length "251 lines"; wc 250) |
| `Step_0` | ✅ census rows (Census II absence); no extent row (**D-10**) |
| `Step_1_and_2` | ✅ climate rows (−54 °C, L89), founding row (L168–170 + Register); ❌ **D-06** (`16` §22 lines), **D-09** (no line number for `11`), no extent row |
| `Step_3` | ❌ **D-01**, **D-02** |
| `Step_5` | ✅ |
| `Step_6` | ✅ ten table sections; ❌ **D-11** (no Subnet column) |
| `Step_7` | ✅ 17-gate index; ❌ **D-10** (Gate 11 note) |
| `Step_8` | ✅ (the Child note matches spec L180) |
| `Step_9` | ❌ **D-11** (item 5 missing) |
| `Step_10` | ✅ zero hits; ❌ **D-03** ("429 lines" now 431) |
| `Phase_2` | ✅ tiers, Census II absence, Register; ❌ **D-04**, **D-05** |
| `Phase_3` | ✅ ranges; ❌ **D-08** (duplicate row) |
| `Phase_4` | ❌ **D-04b** (−58 °C) |
| `Phase_5` | ✅ spec L22, L24; landlocked; the "no other city is named" rule is kept; Geothermal zero hits |
| `Phase_6` | ✅ the load-bearing correction (`Analysis_Notes.md` L594–596), Metaphysics L77–80, Zen L22–24, Synthesis L36–38, Extraction L139; ❌ **D-07** (L6–9) |
| `Phase_7` | ✅ Sweep L91, L109–111, L165, L249–250; ❌ **D-06**, **D-07b** (legend line), **D-13** (Half B row line) |
| `Phase_8` | ✅ zero-hit statement |
| `Phase_9` | ✅ consistent with the census (0 humans) |
| `Phase_10` | ✅ Calethina README L58 ("engineering at Kunlun") + Formative_History, Vosora README L67, spec L250 |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | WRONG | `Step_3` · picks row | "`Inspirational-Influences.md` L97–101 (the Kunlun heading is **L91**)": L91 is blank; the Kunlun heading is **L97**, the four picks are L98–101 (the Mirny subnet heading is L68). | "heading L97; picks L98–101" |
| **D-02** | STALE | `Step_3` · research-log row | Says `Cities/Research_Logs/` has no Kunlun file; two exist (`Kunlun_Inspiration_Place_Research_R1.md`, `_R2.md`, made today). | Reword; register (A-05) |
| **D-03** | STALE | `Step_10` | "`06` (429 lines) … 0 matches": the zero-hit result holds; the file is 431 lines. | Re-count (SH-009) |
| **D-04** | STALE | `Phase_2` · per-nation rows, "Full 19-nation table" | Counts are the old-census set (USA 15.43% / 19,053 …, sum 123,449); the table is 20 rows. | Follow the spec decision (S-01, S-02) |
| **D-04b** | WRONG | `Phase_4` · Robot Cold Physiology row | "directly relevant at **−58 °C mean**": the mean is **−54 °C** (spec L89; `Step_1_and_2` is right). | −54 °C |
| **D-05** | NOTE | `Phase_2`/`Step_0` · Census II | "DOES NOT EXIST — source-affirmed": defensible from census L642/L644; the spec's L34 wording conflicts (S-05). | Cite census L642, L644 beside it |
| **D-06** | STALE | `Step_1_and_2` row 32; `Phase_7` row 21 | `16` §22 cited at "L2251–2256": the §22 heading is **L2256** (+5); read the section live. Worker counts sum the old 123,449 (S-07). | Re-read; label as pre-DR-68 |
| **D-07** | STALE | `Phase_6` · Sacred-sites row | `00_Extraction_Checklist.md` **L6–9**: the quotation runs **L7–9** (L6 is another sentence). | L7–9 |
| **D-07b** | WRONG | `Phase_7` · 6-industry matrix row | "legend at **L140**": L140 is a blank line; the legend ("`Y` = named or clearly described · `.` = absent") is **L139**. | L139 |
| **D-08** | NOTE | `Phase_3` | Two "Concept-art directory status" rows (row 12 and row 23; "1 file total" / "1 file(s) total"). | Keep one |
| **D-09** | GAP | `Step_1_and_2` · `11` row | `11_…` is cited with no line number; live lines **L334, L339**. | Add |
| **D-10** | GAP | `Step_0`, `Step_1_and_2`, `Step_7` | No extent row, although the Pre-Trip lists the extent file; and `Step_7` says Kunlun's "own extent/area figure [is] not yet located". It is: Extent **L627** (Mirny · 123,449 · **12 km²** @10,000/km² · **18 km²** @7,000 · Dome A) — a 2026-09-05 snapshot; at the live 135,226 the same arithmetic gives **13.5 km²** and **19.3 km²**. | Add the row (labelled snapshot); fix the Step 7 note |
| **D-11** | GAP | `Step_6`, `Step_9` | `Step_6` section-1 columns lack **Subnet** (live header: City · Subnet · Shape · Deficit address · Pass); `Step_9` lacks item 5 (as CASEY-048/049). | As Casey |
| **D-12** | NOTE | `Step_-1` · "Specs file length" | "251 lines total": `wc -l` is 250 (SH-009). | Re-count |
| **D-13** | STALE | `Phase_7` · Half B row | Cites `16` **L285**; the row is **L286**. The explanation of the 0.0% as "unassessed at that point in the run" is an inference (S-06). | L286; quote both rows and flag |
| **D-14** | NOTE | `Phase_5` · Universe `Worldspace/Locations/` row | "4 `.md` files read; 1 name the city" enumerated 2026-10-23; only `README.md` L20 names Kunlun now, and the directory holds 2 top-level `.md` files plus folders. | Re-enumerate or leave as dated |
| **D-15** | NOTE | `Phase_7` · `01`/`08` rows | `01_Burden_Scoring_Model.md` L110 / L285 and `08_…` L506 still use 123,449 (S-01). | Label as pre-DR-68 if copied |

### 2d. DECIDE items for the developer (collected)
1. **S-01** Rescale the spec's per-nation robot counts to 135,226 (and then the `Phase_2` rows)? Same shares, new counts is the straightforward fix; the alternative is to label the table "pre-DR-68".
2. **S-02** "19 nations" or 20: either the Netherlands row (0.05% / 62 robots) is a stray, or the text should say 20. If it is a stray, removing it changes the other shares.
3. **S-03 / S-04** Fix L103 (−54 °C, drop the peer rank) and delete the L106 remnant?
4. **S-05** Reword spec L34 to the census's "no Census II by design"?
5. **S-06** Which Mandated/Free pair governs (0.0 / 71.4 from Half B, or 26.8 / 44.6 from §22), and should Half B's row be refreshed? (§22's pair is marked provisional for the developer's review, register item 15.)
6. **A-05** Tier for the two new research files.
