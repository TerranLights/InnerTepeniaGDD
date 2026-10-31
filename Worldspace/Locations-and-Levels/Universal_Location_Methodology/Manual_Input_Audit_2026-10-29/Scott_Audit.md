# Scott — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (229 lines), the whole Pre-Trip (567 lines; the standard text compared line for line with Fort McMurdo's — same island, same builder form — and only the differing lines re-read), all 19 datasheets, the pass README and coverage ledger; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `SC-…`). Pass folder: `City_Development_Passes/Janbogo_Subnet/Scott/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run. Scott's population did not change in the 2026-10-28 scenario or the 2026-09-05 extent ruling, so every census, `09` and `16` number in the sheets is current. "Scott" is also a person's name and part of "Amundsen–Scott"; the Pre-Trip excludes the hyphen form only.

**Verdict.** **Nothing blocks a run.** Retention, the census rows, `09` and `16` all check, and — unlike several neighbors — the sheets already carry the one cross-file fact that matters for Phase 6 (the Polydimensional Animism pages that name the city). What is left: **(1)** the Pre-Trip is the builder version that says the datasheets are "not yet built" in three places; **(2)** the README's spec pointer is dead; **(3)** `Step_1_and_2` copies the spec's record extremes, which the monthly table overrides, and cites COMNAP page 45 (a false hit); **(4)** the `16` Half B row for this city is a Half-A estimate (source `H`: mandate 2.9%, FREE 56.0%) which the city's own determination, **`16` §30 (L3019)**, replaces with 14.7% / 44.2% — the sheets quote only the estimate, and the §30 heading is in no list; **(5)** line shifts, no extent rows in any sheet; **(6)** source: the "corrected 2026-09-04" note says the gap to Fort McMurdo's mean is 4.6 °C in March (the table gives 3.5), and two count columns are short by 1 and 2.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Janbogo subnet/Scott.md` (229 lines; `Step_-1` says 230, builder's convention). Later-era headings **L198**, **L206**, **L212** = the Step −1 list; `## Notable Locations` **L183**, `## Notable Figures` **L191**; spec L3–9, L15–16, L18–38, L42–44, L48–70, L71–140, L81, L92–97, L101–104, L110–113, L143, L145, L151–172, L173–182, L193–194 land on what the sheets say | ✅ |
| Census Section A heading **L290**, entry L292–298 (tier lines L294–296; the note "New Zealand is Scott's founding nation" at L298); Census I row **L510**; Census II row **L629** | ✅ unchanged |
| Census I **189,817 H / 196,194 R / 386,011**; Census II **153,382 H / 160,252 R / 313,634**; retention by hand: 313,634 ÷ 386,011 = **81.25%**, 153,382 ÷ 189,817 = **80.81%**, 160,252 ÷ 196,194 = **81.68%** — `Step_0` and `Phase_2` right (robot share 50.83%: 196,194 ÷ 386,011 = 50.826%) | ✅ |
| Extent file row **L64** (the naive snapshot: Ross Island entire, 157/km²), **L509** (DECLARED 2026-09-05: 55 and 45 km² → 8,097 and 8,578/km²), and the other lines L14, L20, L25, L76, L697 | ✅ unchanged |
| `09` row **L76** (header L52): D 1.25 · humans 189,817 · residents 386,011 · required **103,401** · workforce **291,103** · **35.5%** (103,401 ÷ 291,103 = 35.52%; `16` has 291,102 — 196,194 + 0.5 × 189,817 = 291,102.5, `09` rounds up); `16` Half B row (values quoted exactly, row now **L280**): D 1.25 · workforce 291,102 · base 41.0 · MAND 2.9 · FREE 56.0 · **src H**; `11`: no row | ✅ (the row line: **D-01**) |
| `READER/Scott.md` (16 lines; "READER station: Scott_Base"; annual −19.6): the twelve monthly means equal the spec's Mean column; the sheets' L4–L8 cites land | ✅ |
| Stations L36, L45, L48, L69; Founding Register row **L70** (founders: **New Zealand**, geography and access, `DR-34`) and L83; Robot Physiology: no hit (as the Pre-Trip says); Robot Religions: `Polydimensional_Animism/Culture.md` L18 and `README.md` L172, L216 (the Enfolded) — the sheets carry all three; Holidays L29–30, **L39** ("St. Robert"), L164; Topics L315–316; Precipitation L160; Geothermal L9, L23, L31, L154, L187, L196; Sweep L34, L38, L43, L158, L243, L249; Theoretical L985, L988; Factions `Second_Interwar` L97, L109, L111, L113, L143, L149, L151 and `Cross_City_Cultural_Patterns` L149; CrossSub L182, L206; picks heading **L63**, picks **L64–66** (Victoria BC [PRIMARY], Hannibal, Alexandria) | ✅ unchanged |
| Zero-hit claims re-run: Energy grid, Meme Machine, True Believer, NMCI, Weapons, Arcanet, Ice-Cold folder (7), jobs folder, `06_Worked_Example_Provenance.md` (431 lines, 0 hits), `Test_Runs` tree; timeline-repo `Worldspace/Characters/`: no hit that is not an author's name or "Amundsen–Scott"; `Robot_Universals`: 0; megasheet folder 7 entries; Research Log `Scott_Research_Log.md` does not exist | ✅ |
| `Step_6` and `Step_9` equal Janbogo's (header lines, Subnet column, item 5) | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). Highways L231 → **L232**. Airports L49, 53 → **L52, 56**. Ports L199, 240, 244, 246, 264 same; L520, 529, 551, 713, 756, 815 → **L543, 552, 574, 736, 779, 838**. CrossSub same. RelDB L30, 50 same; L225–226, 249, 400–401, 504 → **L236–237, 260, 411–412, 515** (the city's entry is L411–L418). NatConn L248, 298 same; L415–416, 461, 464, 594 → **L420–421, 466, 469, 599**. `09` L76 same. `16`: row **L279 → L280**; L166, L222 same; the other 21 entries L353, 436, 2908, 2924, 2959, 2962, 2964, 2974–2975, 2979, 3008, 3035, 3051, 3054, 3057, 3068, 3079, 3087, 3535–3536, 3567 → **L356, 439, 2913, 2929, 2964, 2967, 2969, 2979–2980, 2984, 3013, 3040, 3056, 3059, 3062, 3073, 3084, 3092, 3540–3541, 3572**; add the city's own section heading **L3019** ("## 30. ✅ SCOTT — DETERMINED", upper-case). Precipitation: L160 stands; **L216 is a false positive** (an "Amundsen–Scott South Pole" citation, en dash). Unchanged: census, extent, Stations, Holidays, Topics, Register. | live greps | Re-read each list live (SH-012) |
| **A-02** | WRONG | **"Datasheets not yet built" in three places** (2026-10-21 builder text): §C intro, §I `DATASHEET-NOT-YET-BUILT(N-5)=20` (with `RESOLVE=121`), and a §J row. All 19 files exist. | `Datasheets/` | Reword all three |
| **A-03** | STALE | **Pass README spec pointer is dead:** `../../../Specs/Scott.md` (pre-reorg flat path); the file is `Specs/Janbogo subnet/Scott.md`. The other pointers resolve. | `ls` | Re-point (deferred README sweep) |
| **A-04** | NOTE | **Alias set** is the mechanical draft (Scott Base · Hut Point Peninsula · Ross Island) plus a good ambiguity warning. Not listed, found in shared files: **Hut Point** (Holidays L29–30, L164; spec L186), **St. Robert** (Holidays L39), **the Enfolded** (Polydimensional Animism), **Mount Erebus**; Ross Island and the peninsula are shared with Fort McMurdo (no "different place" note). The exclusion catches "Amundsen-Scott" with a hyphen only: the en-dash form leaks (Precipitation L216). | grep | Confirm; add; widen the exclusion |
| **A-05** | NOTE | **Geothermal.** `Geothermal_Heating.md` names the city (L9, L23, L31, L154, L187, L196) and the spec's terrain finding rests on it; the Pre-Trip's §J keeps the file out of every phase list; `Phase_5` carries it. (As Fort McMurdo, **A-05** there.) | spec L21–28 | DECIDE (with FM-005) |
| **A-06** | NOTE | The existing inspiration input `Reference/Real-World/Inspiration_Place_Research/inputs/Scott.md` has no R1 / R2 output yet. | live | none |
| **A-07** | NOTE | Shared items SH-001 … SH-007, SH-010, SH-011, SH-013. | live | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ · G3 `16` Half B ✅ (an estimate, and §30 not listed, **A-01**, **D-01**) · G4 Register row ✅ (named in §J, cited in the sheets) · G5 `Access type: SPUR` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ in `Step_3` · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ not in the sheets (**D-08**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals (189,817 + 196,194 = 386,011; 153,382 + 160,252 = 313,634); the 12 per-nation shares sum to **100.00%**; Census I robots (**196,194**) and Census II robots (**160,252**) sum exactly; tier lists equal the table (2 / 6 / 4) and the census Section A entry; tier totals are exactly the 8 : 3 : 1 share model (42.10 / 47.37 / 10.53 against 16 / 18 / 4 of 38 shares); monthly means average **−19.55 °C** (stated −19.6); in every month Avg High > Mean > Avg Low and **Avg Low > Rec Low**; monthly precipitation sums to **184 mm** (stated 184); falls 184 − lands 70 = lost **114** (70 ÷ 184 = 38.0%); polar night Apr 26 → Aug 19 = 116 days, midnight sun Oct 24 → Feb 19 = 119 days (same latitude as Fort McMurdo, recomputed there); density 386,011 ÷ 45 = **8,578/km²**; coldest month (August −29.5) and warmest (January −4.6) agree with the table.

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **Record extremes contradict the monthly table.** L94 "record high **+6.8 °C**; record low **−57 °C**": the table's Rec columns give a high of **+10 (Nov)** (+9.4 Dec, +8.3 Jan) and a low of **−50.6 (Jul)**. `Step_1_and_2` carries L94. | spec L94 vs L117–128 |
| **S-02** | WRONG | **The "corrected 2026-09-04" note** says the gap to McMurdo's mean "widens to **4.6 °C in March** and 4.3 °C in August". From the two tables: March **−20.6 vs −17.1 = 3.5**; August −29.5 vs −25.2 = **4.3** (right); the largest gap is **May, 4.7** (−26.2 vs −21.5). The annual gap 3.4 (−19.6 vs −16.2) is right. | spec L85–86 |
| **S-03** | NOTE | **Two count columns are short:** Census I humans sum to **189,816** (stated 189,817), Census II humans to **153,380** (stated 153,382) — rounding residuals of the de-stacking. | spec L15–16, L54–65 |
| **S-04** | NOTE | The Rec High column shows **−4.4** in June, July, August and September — four identical record highs in a row, an artifact of a short NCEI record or a paste. | spec L122–125 |
| **S-05** | STALE | Peer-relative lines, none carried by the sheets: L8 (Fort McMurdo, "the Federation's largest industrial city"), L73–77 (Fort McMurdo's geography "applies here"), L107 "9 of the 37 Tepenian cities are colder" (38 now), L153–157, L165 (other Saints). | spec |
| **S-06** | NOTE | The tier table marks **Australia** "(founding wave)" (L43), while the founders are **New Zealand** — Register `DR-34`, spec L145, and the census note "New Zealand is Scott's founding nation" (L298). New Zealand carries no annotation in this city's table (it does in Fort McMurdo's). | spec L43, L145; census L298 |
| **S-07** | NOTE | The Daylight column shows Feb **24** and Aug **0** against the stated ends of midnight sun (Feb 19) and polar night (Aug 19). L169 "restaurants" is the only food-or-drink-adjacent word in the spec. | spec |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings, header fields, census; **D-07** (230) |
| `Step_0` | ✅ census, retention; ❌ **D-08** (extent) |
| `Step_1_and_2` | ✅ climate rows, READER, Stations, Register; ❌ **D-01** (`16` row), **D-02** (record extremes), **D-03** (COMNAP), **D-08** |
| `Step_3` | ✅ picks L63–66 |
| `Step_5`, `Step_6`, `Step_7`, `Step_8`, `Step_9` | ✅ |
| `Step_10` | ❌ **D-07** (430) |
| `Phase_2` | ✅ census, retention, Register; NOTE **D-09** |
| `Phase_3` | ✅ spec ranges |
| `Phase_4` | ✅ `09` L76; ❌ **D-01** (`16` row) |
| `Phase_5` | ❌ **D-04** (lines) |
| `Phase_6` | ✅ Polydimensional Animism ×3, Holidays ×4 |
| `Phase_7` | ❌ **D-01** (`16`), **D-05** (list, §30) |
| `Phase_8` | NOTE **D-10** |
| `Phase_9` | ✅ |
| `Phase_10` | NOTE **D-06** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Step_1_and_2` · `16` row; `Phase_4`; `Phase_7` | Row cited **L279 → L280**. The row's mandate is a **Half-A estimate (src `H`: "MINE, needs ruling")** — MAND **2.9%**, FREE **56.0%**. The city's own determination, **`16` §30 "SCOTT — DETERMINED" (L3019–3095)**, gives baseline **119,464 (41.0%)** · mandated **42,910 (14.7%)** · FREE **128,729 (44.2%)** · distinctive tier 171,638 (59.0%); the counts sum to 291,103 — the **current** workforce — so §30's numbers are current. The sheets quote the estimate alone and none lists §30. | Re-point; add §30; say it supersedes Half B (SH-013) |
| **D-02** | WRONG | `Step_1_and_2` · record-extreme row | carries spec L94 (+6.8 / −57); the table gives **+10 (Nov)** and **−50.6 (Jul)** (S-01). | Replace from the table |
| **D-03** | WRONG | `Step_1_and_2` · COMNAP row | "pages **8, 45, 55**": Scott Base is on **8** (index) and **55** (the entry); page 45 names "Scott" only inside another station's neighbor sentence. | Remove 45 |
| **D-04** | STALE | `Phase_5` | Highways **L231 → L232**; Airports **L49, L53 → L52, L56**; Ports **L520, L529, L551, L713, L756, L815 → L543, L552, L574, L736, L779, L838**; RelDB entry **L400–L410 → L411–L421**, lines **L401–L407 → L412–L418**; NatConn "7 line(s)" **L415–416, L461, L464, L594 → L420–421, L466, L469, L599**. | Re-point |
| **D-05** | STALE | `Phase_7` · "other lines naming the city" | The `16` "23 line(s)" list per A-01 (+3 / +5; most lines are inside other cities' sections that mention Scott), and §30 (L3019) missing. | Replace / re-point |
| **D-06** | NOTE | `Phase_10` | "587 files, **1 names the city**": the one file's two hits are the authors "James Scott Bell" (L2774) and "Orson Scott Card" (L2906) — **0 files name the city**. | Reword |
| **D-07** | STALE | counts | `Step_10` "(430 lines)" → **431**; "230-line" spec (229), "293" Meme (292), "378" True Believer (377), "246" NMCI (245), "74" Weapons (73), "36" Enneagram (35), "28" Arcanet (27), "146" Energy (145) — builder convention, SH-009. | per SH-009 |
| **D-08** | GAP | `Step_0`, `Step_1_and_2` | No extent rows: spec **L18–38** (declared ~45 km², 386,011 ÷ 45 = 8,578/km², rock kept bare by geothermal heat, shared Hut Point Peninsula) and the extent file's **L64** (snapshot, 157/km² on Ross Island entire), **L509** (declared 55 and 45 km²). | Add, labelled the 2026-09-05 snapshot (SH-011) |
| **D-09** | NOTE | `Phase_2` · annotation rows | "(founding wave) — no date" is on **Australia**; the founders are New Zealand (S-06) and the census note L298 is not carried. | Add L298; flag the annotation |
| **D-10** | NOTE | `Phase_8` · term-check row | "cuisine / food / dish / drink — 0" ✓; the only food-adjacent text is "restaurants" (spec L169, the Developer vision); "230-line" → 229. | Mention L169 |
| **D-11** | NOTE | `Phase_4` · `09` row vs `16` row | `09` workforce **291,103**, `16` **291,102** in the same sheet: `09` rounds 291,102.5 up. | Add "(`09` rounds up)" |

### 2d. DECIDE items (collected)
1. **S-01 / S-02** Approve source edits in the spec: L94 from the table; the March figure (3.5, or the largest-gap month, May 4.7) in the correction note.
2. **D-01** Whether the sheets must carry §30 and say Half B is superseded (SH-013).
3. **S-06** Whether the "(founding wave)" annotation moves from Australia to New Zealand.
4. **A-05** Geothermal as a named input (with Fort McMurdo).
