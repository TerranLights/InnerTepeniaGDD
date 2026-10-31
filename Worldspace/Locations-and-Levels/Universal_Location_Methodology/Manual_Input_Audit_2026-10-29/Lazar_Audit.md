# Lazar — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (216 lines), the whole Pre-Trip (566 lines; standard text compared line for line with earlier cities, only differing lines re-read), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `LZ-…`). Pass folder: `City_Development_Passes/Halley_Subnet/Lazar/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run. Lazar is a **composite of two real sites** (Novolazarevskaya and Maitri) in the Schirmacher Oasis; that matters for the alias set.

**Verdict.** **Nothing blocks a run.** Lazar's sheets are synced to the 2026-10-28 census, and the `09`, `11` and `16` rows are the right city's and current. What is left: **(1)** `Step_3` cites the picks at L186–193, which is now Halley's last picks and **Santa Luce's** section — Lazar's is L217–223 (XS-15); **(2)** `Phase_2` retention contradicts `Step_0`; **(3)** the Pre-Trip does not search **Maitri** (half the city) and the sheets leave out the Maitri entries in the Stations file and the COMNAP catalogue; **(4)** the usual line shifts, plus one new `16` line (the 2026-10-29 Relung Panen update note) missing from the list; **(5)** "datasheets not yet built", extent rows missing, README spec pointer dead; **(6)** three spec passages still describe the population before the −10% ruling, and the wind-vs-cold box quotes a −17.0 °C mean that the spec's own table no longer supports.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Halley subnet/Lazar.md` (216 lines; sheets say 217, builder's convention). Later-era headings **L193** (Connection to Concordia), **L198** (Current Status / Damage), **L204** (Legacy) = the Step −1 list; spec L3, L5–L9, L36–37, L41–43, L47–82, L91–114, L155, L161, L165, L173, L178, L188 land on what the sheets say | ✅ |
| Census Section A heading **L200**, entry L202–206, tier table L204–206, Census I row **L482**, Census II row **L604**; other lines L502, L719–720, L728, L766 | ✅ unchanged |
| Census I **1,170,443 H / 1,211,762 R / 2,382,205**; Census II **783,193 / 856,233 / 1,639,426**; retention in `Step_0` recomputed by hand: 1,639,426 ÷ 2,382,205 = **68.82%**, 783,193 ÷ 1,170,443 = **66.91%**, 856,233 ÷ 1,211,762 = **70.66%**; robot share 1,211,762 ÷ 2,382,205 = **50.87%** | ✅ (`Phase_2` disagrees, **D-01**) |
| `09` row **L74** (Required **637,974** · Workforce **1,796,984** · **35.5%**); `11` row **L331** (header L326: OLD 35.5% / NEW 41.0%); `16` Half B row workforce **1,796,984** = 1,211,762 + 0.5 × 1,170,443 | ✅ the city's own rows, current values |
| `READER/Lazar.md`: twelve monthly means equal the spec's Mean column; annual −10.1 (spec about −10) | ✅ |
| Founding Register row **L52** (and L83, L94); Highways L58–59, 116, 118, 129, 131, 135; CrossSub L95, L203; Stations L40; Sweep **L148** (4/6); NMCI L225; Precip L157; Topics L179; Extent rows L605, L654, L577, L593, L683; Factions `Second_Interwar` L225, 227, 231, 233, 235, 263 | ✅ |
| Zero-hit claims re-run: Energy grid, `06` provenance, Geothermal, Arcanet, Theoretical-Calculations, National Holidays, Robot_Religions, Ice-Cold folder, Meme Machine, True Believer, Robot_Universals, Enneagram index | ✅ |
| Characters canon: only `Calethina/README.md` **L60** names the city (excluded as later-era in the sheet, correctly) | ✅ |
| Addresses tested exist (Local Culture, Local Robot Culture, Enneagram file, vision notes, concept-art folder, megasheet folder, Tools) | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits.** `16`: row **L283 → L284**; L189, 200, 202, 204, 206–207, 212 same; L320, 323, 361, 469 → **L323, 326, 364, 472**, **add L474** (the 2026-10-29 update note: the Bunger Hills / Relung Panen city is no longer excluded); L823, 889, 931, 1415, 1583, 2536 → **L828, 894, 936, 1420, 1588, 2541**. Airports L48, 52 → **L51, 55**. Ports L460, 717 → **L483, 740**. RelDB L23–24, 47, 96 same; L279–280, 286, 373–374, 460, 531 → **L290–291, 297, 384–385, 471, 542**. NatConn L68 … L235 same; L407, 409, 424, 439, 459, 529, 537 → **L412, 414, 429, 444, 464, 534, 542**. Highways, CrossSub, `09`, `11`, Stations, census, extent, Precip, Topics, NMCI, Register unchanged. | live greps | Re-read each list live (SH-010) |
| **A-02** | WRONG | **"Datasheets not yet built" sentences** (2026-10-21 builder text): §C intro, §I `DATASHEET-NOT-YET-BUILT(N-5)=20`, §J row. All 19 files exist. | `Datasheets/` | Reword all three |
| **A-03** | GAP | **Maitri is not in the search set** ("Other strings searched: `Novolazarevskaya`" only; "Station/place names drafted: none parsed"). The spec rests on both sites (L3, L26–28, L96: the climate extremes come from NOAA station `AYM00089514` — *Maitri*, 1 km). Lines found by Maitri/Schirmacher alone and missing from the Pre-Trip and sheets: `Stations` **L83** ("Maitri Helipad · Schirmacher Oasis · India · Concrete"), COMNAP pages **50 and 51** (Maitri; the sheet lists only 8 and 67), and Census **L719** is covered. Also add **Maitri**, **Maitri Station**, **Schirmacher Oasis**, **Novo Runway** (Stations L40) to §A. | spec L3, L96; Stations L40, L83; COMNAP | Add; re-run the name search with Maitri |
| **A-04** | STALE | Pass `README.md` spec pointer is dead (`../../../Specs/Lazar.md`, pre-reorg flat path; the file is `Specs/Halley subnet/Lazar.md`). Local-culture and vision-notes pointers resolve. | README; `ls` | Re-point (deferred README sweep) |
| **A-05** | NOTE | No `Lazar_Inspiration_Place_Research` files yet. Shared items SH-001 … SH-007; megasheet "7 files" = 6 files + 1 subfolder. | | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ · G3 `16` Half B ✅ (MAND 0.0%, src "–": no national mandate; `16` L472 says Lazar's economy is "explicitly unresolved in canon") · G4 Register row ✅ · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ (wrong lines cited, **D-02**) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ not in the sheets (**D-06**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their stated totals; the 25 per-nation shares sum to **100.01%** (rounding); all four count columns sum **exactly** (Census I robots **1,211,762**, humans **1,170,443**; Census II robots **856,233**, humans **783,193**); tier lists equal the table (1 / 5 / 19); monthly means average **−10.05 °C** (stated about −10); precipitation sums to **237.7 mm** (stated); retention 90 ÷ 238 = 38%; polar night May 22 → Jul 23 = **63 days**, midnight sun Nov 16 → Jan 28 = **74 days**; record high +10 (Nov) and low −38 (Jul) match the table; the temperature-range line (L110) matches the means.

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **The wind-vs-cold box (L107) says "At −17.0 °C 12 of the 37 Tepenian cities are colder":** −17.0 °C is the **July** mean; the annual mean is about **−10 °C** (L94, and the monthly means average −10.05). The box was written before the 2026-10-21 column replacement. It also states a peer rank. | spec L94, L107, L124 |
| **S-02** | STALE | **Three passages still describe the population before the −10% ruling and the census change:** L9 and L149 call Lazar "Tepenia's single largest city" with Census I **2,620,319** and Census II **1,803,977** "rank 1st"; the Population Note (L16, dated 2026-07-03) says "roughly 46% larger than the new #2". The authoritative figures are in L36–37 (**2,382,205** / **1,639,426**). A rank claim is also a peer comparison. | spec L9, L16, L36–37, L149 |
| **S-03** | NOTE | **Precipitation probability is "~0%" for April (14.5 mm) and June (34.6 mm)**, which contradicts measured precipitation in those months. | spec L121, L123 |
| **S-04** | NOTE | L91 names Neumayer as "a regional comparison" for the proxy climate data, and L87 compares the latitude with Neumayer's. The `Step_1_and_2` sheet copies the L91 phrase (**D-08**). | spec L87, L91 |
| **S-05** | NOTE | Timeline repo `Worldspace/Locations/README.md` L17 still lists "Abowasa" and "Princess Elisabeth". Flag only. | README L17 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings, census cells copied whole (including the −10% authoring note) |
| `Step_0` | ✅ census, retention (hand-checked); no extent row |
| `Step_1_and_2` | ✅ climate rows, READER, Register; ❌ **D-03**, **D-05**, **D-08**, no extent row |
| `Step_3` | ❌ **D-02** |
| `Step_5` … `Step_9` | ✅ (Step 6 with Subnet column and exact header lines; Step 9 with item 5) |
| `Step_10` | ❌ **D-07** |
| `Phase_2` | ❌ **D-01** |
| `Phase_3` | ✅ ranges L83–152, L165–172, L178–187 |
| `Phase_4` | ✅ `09`, `11`, NMCI; ❌ **D-03** (`16` row) |
| `Phase_5` | ❌ **D-04** |
| `Phase_6`, `Phase_8` | ✅ |
| `Phase_7` | ✅ Sweep L148, Factions; ❌ **D-03** |
| `Phase_9` | ✅ robot share 50.87% |
| `Phase_10` | ✅ |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Phase_2` · Retention | "combined 68.85% · human 66.92% · robot 70.71%" are pre-`DR-68`; `Step_0` gives **68.82% · 66.91% · 70.66%** (hand-checked). | Replace |
| **D-02** | WRONG | `Step_3` · picks rows (8 rows) | Cites `Inspirational-Influences.md` "section at **L186–L193**", picks **L187–L192**. Lazar's heading is now **L217**, its six picks **L218–223**; L186–193 hold the end of Halley's picks and **Santa Luce's** section. | Re-point (XS-15) |
| **D-03** | STALE | `Step_1_and_2` row 33; `Phase_4` row 14; `Phase_7` rows 16–17 | `16` Half B row **L283 → L284**; the "17 other lines" list is the old numbering and misses **L474** (18 lines now). | Re-point; add |
| **D-04** | STALE | `Phase_5` | Airports **L51, 55**; Ports **L483, 740**; RelDB entry "L279–L289" → **L290–L300**, entry lines L280–L286 → **L291–L297**; NatConn 22-line list → live list (A-01). | Re-point |
| **D-05** | GAP | `Step_1_and_2` rows 31–32 | Stations and COMNAP rows cover only the Novolazarevskaya side: add Stations **L83** (Maitri Helipad) and COMNAP pages **50, 51**; the page row says "8, 67". | Add (A-03) |
| **D-06** | GAP | `Step_0`, `Step_1_and_2` | No extent row. Extent **L605**: Lazar · 2,620,319 · **262 km²** @10,000/km² · **374** @7,000 · "Schirmacher Oasis ~34 km²" (2026-09-05 snapshot, before the −10%); **L654** (the −10% row: 262,032 / 180,398, "34 km² of Schirmacher carrying 87–91% of the city on ice"); L577, L593, L683. At the live 2,382,205 the same arithmetic gives **238.2 / 340.3 km²**. | Add (labelled snapshot) |
| **D-07** | STALE | `Step_10` | "`06` (430 lines) … zero hits": **431** lines; zero hits re-run for "Lazar", "Novolazarevskaya". | Re-count (SH-009) |
| **D-08** | NOTE | `Step_1_and_2` row 15 | Copies "plus Neumayer as a regional comparison" (S-04); other rows mark such comparisons "not copied". | Mark not copied |
| **D-09** | NOTE | counts | "217", "74", "293", "378", "166", "36", "199", "28", "146" are each one above `wc -l` (the builder's convention, XS-9). | per SH-009 |

### 2d. DECIDE items (collected)
1. **A-03** Add the Maitri strings and re-run the name search (adds Stations L83, COMNAP pages 50–51 to the sheets).
2. **S-01 / S-02** Approve source edits: the wind-vs-cold box (L107), and the population wording (L9, L16, L149).
