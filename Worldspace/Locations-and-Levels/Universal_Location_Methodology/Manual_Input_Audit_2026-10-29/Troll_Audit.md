# Troll — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (181 lines), the whole Pre-Trip (566 lines; standard text compared line for line with earlier cities, only differing lines re-read), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `TR-…`). Pass folder: `City_Development_Passes/Halley_Subnet/Troll/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run. "Troll" is also an ordinary word; the Pre-Trip searched it case-sensitively (capital T), which is right.

**Verdict.** **Nothing blocks a run.** Troll's sheets are synced to the 2026-10-28 census and the `09`, `11` and `16` rows are the right city's. What is left: **(1)** `Step_3` cites the picks at L179–185, which is now other cities' lines (Troll's are L210–215; XS-15); **(2)** `Phase_2` retention is the pre-census-change set; **(3)** the usual line shifts, "datasheets not yet built", missing extent row, dead README spec pointer; **(4)** two spec problems: the wind-vs-cold box quotes a −22.0 °C mean (the annual mean is −17 °C), and the Avg High/Avg Low columns are lower than the record lows in five months.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Halley subnet/Troll.md` (181 lines; sheets say 182, builder's convention). Later-era headings **L166** (Connection to Concordia) and **L171** (Legacy) = the Step −1 list; spec L3–L8, L15–16, L20–22, L26–62, L63–126, L73–91, L129, L131, L137–146, L147–153, L154–160, L161 land on what the sheets say | ✅ |
| Census Section A heading **L156**, entry L158–162 (tier table L160–162), Census I row **L501**, Census II row **L622** | ✅ unchanged |
| Census I **487,859 H / 490,507 R / 978,366**; Census II **331,757 / 355,920 / 687,677**; `Step_0` retention recomputed by hand: **70.29% · 68.00% · 72.56%**; robot share 490,507 ÷ 978,366 = **50.14%** | ✅ (`Phase_2` disagrees, **D-01**) |
| `09` row **L62** (header L52): Required **279,026** · Workforce **734,437** · **38.0%**; `11` row **L101** (header L95): marine workers 65,568 · 16.4 Mt · 5.0×; `16` Half B workforce **734,436** = 490,507 + 0.5 × 487,859 = 734,436.5 (`09` rounds up, `16` down) | ✅ the city's own rows, current |
| `READER/Troll.md` (rebuilt 2026-10-21): twelve monthly means equal the spec's Mean column; annual −17.2 | ✅ |
| Stations **L65, L98**; COMNAP pages **8, 56**; Founding Register row **L48**; Sweep **L152**; Factions (PostWar L89; Second_Interwar L31, 33, 39, 41, 53, 57); CrossSub L76, 118–119, 121–122, 203; Highways L116; Precip L128; Topics L198; Robot Physiology L283; Extent row L623 | ✅ unchanged |
| Zero-hit claims re-run: NMCI, Energy grid, `06` provenance, Geothermal, Arcanet, Theoretical-Calculations, National Holidays, Robot_Religions, Ice-Cold folder, Meme Machine, True Believer, Robot_Universals, Enneagram index; Characters canon: **0** files name the city | ✅ |
| Addresses tested exist (Local Culture, Local Robot Culture, Enneagram file, vision notes, concept-art folder (empty), megasheet folder, Tools) | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). `16`: row **L262 → L263**; L209 same; the other 32 entries +5 (L719 … L3554 → **L724, 784, 786, 789, 802, 808, 815–816, 827–828, 830–831, 834, 905, 935, 1008, 1013, 1052, 1128, 1130, 1497, 1734, 1902, 2031, 2811, 2896, 3253, 3279, 3284, 3426, 3557, 3559**). `09` L62 same; L203 → **L205**. Airports L3, 14 same; L33, 60, 96 → **L36, 63, 99**. Ports L182 same; L460, 717 → **L483, 740**. RelDB L23, 47 same; L124, 285, 395, 454–455 → **L135, 296, 406, 465–466**. NatConn L47 … L128 same; L368, 417, 503, 509 → **L369, 422, 508, 514**. Highways, CrossSub, census, extent, Stations, Precip, Topics, Robot Physiology unchanged. | live greps | Re-read each list live (SH-010) |
| **A-02** | WRONG | **"Datasheets not yet built" sentences** (2026-10-21 builder text): §C intro, §I `DATASHEET-NOT-YET-BUILT(N-5)=20`, §J row. All 19 files exist. | `Datasheets/` | Reword all three |
| **A-03** | STALE | Pass `README.md` spec pointer is dead (`../../../Specs/Troll.md`, pre-reorg flat path; the file is `Specs/Halley subnet/Troll.md`). Local-culture and vision-notes pointers resolve. | README; `ls` | Re-point (deferred README sweep) |
| **A-04** | NOTE | Alias set (mechanical, unconfirmed): drafted "Jutulsessen nunatak · Queen Maud Land · Troll Research Station". Names used in the shared files: **Troll Airfield** (spec L7, L69; Airports), **Troll Station** (Stations L65), **Troll Base** (RelDB, "Troll Base (Norway)"). | spec; Stations L65; RelDB | Confirm; add |
| **A-05** | NOTE | No `Troll_Inspiration_Place_Research` files yet. Shared items SH-001 … SH-007; megasheet "7 files" = 6 files + 1 subfolder. | | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ · G3 `16` Half B ✅ · G4 Register row ✅ · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ (wrong lines cited, **D-02**) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ not in the sheets (**D-05**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals; the 26 per-nation shares sum to **99.99%** (rounding); all four count columns sum **exactly** (Census I robots **490,507**, humans **487,859**; Census II robots **355,920**, humans **331,757**); tier lists equal the table (1 / 5 / 20); monthly means average **−17.18 °C** (stated about −17); retention 140 ÷ 200 = 70%; polar night May 16 → Jul 29 = **75 days**, midnight sun Nov 11 → Feb 1 = **83 days**; the temperature-range line (L79) matches the means.

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **The wind-vs-cold box (L94) says "At −22.0 °C (7 cities are colder)":** the annual mean is about **−17 °C** (L76, and the monthly means average −17.18). The box was written before the 2026-10-21 column replacement; it also states a peer rank. | spec L76, L94 |
| **S-02** | WRONG | **Avg Low (night) is lower than Rec Low in five months:** Apr −36 vs −30.1, May −41 vs −29.9, Jun −42 vs −34.8, Jul −42 vs −34.7, Aug −40 vs −37.2 (an average cannot be below the record). The provenance note admits the Avg High / Avg Low rows "no longer fit the corrected Mean in May and June" (L116) but only those two months. | spec L103–107, L116 |
| **S-03** | NOTE | L78 "winter lows around −50 °C … summer reaches about 0 °C" against the table's lowest record −39.5 and highest +5 (Nov). Explained: published-box records are kept over the shorter NCEI period (L113). | spec L78, L113 |
| **S-04** | NOTE | L116 states a peer count ("19 of the 37 cities now carry measured values …"); not carried by the sheets. | spec L116 |
| **S-05** | NOTE | Timeline repo `Worldspace/Locations/README.md` L17 still lists "Abowasa" and "Princess Elisabeth". Flag only. | README L17 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings L166, L171; census |
| `Step_0` | ✅ census, retention (hand-checked); no extent row |
| `Step_1_and_2` | ✅ climate rows, READER row, Stations, COMNAP, `16` row, Register; ❌ **D-03**, no extent row |
| `Step_3` | ❌ **D-02** |
| `Step_5` … `Step_9` | ✅ (Step 6 with Subnet column and exact header lines; Step 9 with item 5) |
| `Step_10` | ❌ **D-06** |
| `Phase_2` | ❌ **D-01** |
| `Phase_3` | ✅ ranges L63–126, L137–146, L154–160 |
| `Phase_4` | ✅ `09`, `11`, `16` rows; ❌ **D-03** (line) |
| `Phase_5` | ❌ **D-04** |
| `Phase_6`, `Phase_8`, `Phase_10` | ✅ |
| `Phase_7` | ✅ Sweep, Factions; ❌ **D-03** |
| `Phase_9` | ✅ robot share 50.14% |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Phase_2` · Retention | "combined 70.39% · human 68.03% · robot 72.73%" are pre-`DR-68`; `Step_0` gives **70.29% · 68.00% · 72.56%** (hand-checked). | Replace |
| **D-02** | WRONG | `Step_3` · picks rows (7 rows) | Cites `Inspirational-Influences.md` "section at **L179–L185**", picks L180–184. Troll's heading is now **L210**, its five picks **L211–215**; L179–185 fall in the Belgrano / Halley / Santa Luce part of the file. | Re-point (XS-15) |
| **D-03** | STALE | `Step_1_and_2` row 36; `Phase_4` row 16; `Phase_7` rows 18–19 | `16` Half B row **L262 → L263**; the "33 other lines" list is the old numbering (A-01). | Re-point |
| **D-04** | STALE | `Phase_5` | Airports L33, 60, 96 → **L36, 63, 99**; Ports L460, 717 → **L483, 740**; RelDB entry "L454–L464" → **L465–L475**, entry lines L455–L461 → **L466–L472**; NatConn 16-line list → live list. | Re-point |
| **D-05** | GAP | `Step_0`, `Step_1_and_2` | No extent row. Extent **L623**: Troll · 954,450 · **95 km²** @10,000/km² · **136** @7,000 · "Jutulsessen" — a 2026-09-05 snapshot; at the live 978,366 the same arithmetic gives **97.8 / 139.8 km²**. | Add (labelled snapshot) |
| **D-06** | STALE | `Step_10` | "`06` (430 lines) … zero hits": **431** lines; zero hits re-run. | Re-count (SH-009) |
| **D-07** | NOTE | `Phase_4` row 14 vs rows 16, `Step_1_and_2` | `09` Workforce **734,437**, `16` **734,436** in the same sheet: `09` rounds 734,436.5 up. | Add "(`09` rounds up)" |
| **D-08** | NOTE | counts | "182", "74", "293", "378", "166", "36", "246", "199", "28", "146" are each one above `wc -l` (builder's convention, XS-9). | per SH-009 |

### 2d. DECIDE items (collected)
1. **S-01 / S-02** Approve source edits: the wind-vs-cold box (L94) and the Avg High / Avg Low columns.
