# Sanay — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (202 lines), the whole Pre-Trip (566 lines; standard text compared line for line with earlier cities, only differing lines re-read), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `SY-…`). Pass folder: `City_Development_Passes/Halley_Subnet/Sanay/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run as a whole, but **Sanay is the subject of the Run 11 cold test run** (the Port of Sanay), which is why `06_Worked_Example_Provenance.md` carries a skip section for it.

**Verdict.** **Nothing blocks a run.** The 2026-10-28 climate correction (the −20 °C stub replaced by the measured −16.2 °C, the READER file rebuilt) is carried into the sheets, but not into the Pre-Trip; the census values are current everywhere. What is left: **(1)** the Pre-Trip still calls the climate file "an 8-line STUB"; **(2)** `Step_10`'s list of `06` lines to skip is incomplete (the Sanay section runs L270–L290; the list stops at L289 and misses L288 and the new L290); **(3)** `Phase_2` retention is the pre-census-change set; **(4)** `Step_3` cites the picks at L173–178, now the wrong city's lines (Sanay's are L204–208; XS-15); **(5)** the usual line shifts (Ports +23 across 32 entries) and "datasheets not yet built"; **(6)** two spec items for the developer: the city-to-port distance (200 km in the spec, 160 km in `Ports.md`) and an ice-shelf boilerplate sentence on a bedrock city.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Halley subnet/Sanay.md` (202 lines; sheets say 203, builder's convention). Later-era headings **L179, L184, L192** = the Step −1 list; spec L3, L5–L9, L16–17, L21–23, L27–58, L59–128, L73–91, L131, L133, L139–148, L149–156, L157–173, L174 land on what the sheets say | ✅ |
| Census Section A heading **L176**, entry L178–184 (tier table L180–182), Census I row **L505**, Census II row **L631** | ✅ unchanged |
| Census I **243,714 H / 243,871 R / 487,585**; Census II **153,905 / 137,057 / 290,962**; `Step_0` retention recomputed by hand: **59.67% · 63.15% · 56.20%**; robot share 243,871 ÷ 487,585 = **50.02%** | ✅ (`Phase_2` disagrees, **D-01**) |
| `09` row **L63** (Required **139,151** · Workforce **365,728** · **38.0%**); `16` Half B row **L254** (workforce **365,728** = 243,871 + 0.5 × 243,714 ✓; D 1.43 · 44.5 / 27.8 / 27.8 · C); `11` has no row for the city (zero hits) | ✅ the city's own rows, current |
| `READER/Sanay.md` (rebuilt 2026-10-28 as a dataset): "READER station: none", S.A.N.A.E. AWS (NOAA `AYM00089004`, 817 m; SANAE IV about 850 m), 2001–2026, annual −16.2; the twelve monthly means equal the spec's Mean column; the `Step_1_and_2` sheet says all of this | ✅ |
| Stations **L58**; COMNAP pages **8, 72**; Founding Register row **L50**; Sweep **L128, L151, L218**; Theoretical **L970, L975–976, L978**; Factions (PostWar L89; Second_Interwar L31, 33, 49, 53, 57, 263; Cross_City L24, 45, 62, 67); NatConn 12 lines (40–41, 46, 48, 79, 91, 112–113, 123, 125, 128, 130); CrossSub L204; Precip L137; Topics L194; Robot Physiology L377; Extent row L624 | ✅ unchanged |
| Zero-hit claims re-run: NMCI, Energy grid, Geothermal, Arcanet, National Holidays, Robot_Religions, Ice-Cold folder, Meme Machine, True Believer, Robot_Universals, Enneagram index; Characters canon: **0** files name the city | ✅ |
| Concept-art folder: the 5 images the sheets list (`bay port broadview …`, 2026-07-08) are all there | ✅ |
| Addresses tested exist (Local Culture, Local Robot Culture, Enneagram file, vision notes, megasheet folder, Tools) | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). Highways L66, 116, 121 same; L240, 242, 285 → **L241, 243, 300**. Airports L49, 53 → **L52, 56**. Ports L59, 122, 127, 137, 182 same; the other 27 entries are all +23: L322, 358–359, 372, 381, 398, 400, 403, 413, 417, 420, 426, 430, 432, 438, 444–446, 449, 465, 713, 719–720, 737, 768, 801, 836, 858 → **L345, 381–382, 395, 404, 421, 423, 426, 436, 440, 443, 449, 453, 455, 461, 467–469, 472, 488, 736, 742–743, 760, 791, 824, 859, 881**. RelDB L23, 31, 47, 73 same; L236, 239, 339, 341, 389, 392–393, 460, 501, 529 → **L247, 250, 350, 352, 400, 403–404, 471, 512, 540**. `09` L63 same; L136–137, 203 → **L138–139, 205**. `16`: row L254 same; L327, 410 → **L330, 413**; the remaining entries +5 (L571, 627, 632, 638 … L3555 → **L576, 632, 637, 643, 643, 724, 733, 737, 741, 744, 752–754, 757, 788, 801, 828, 858, 935, 997, 1069, 1205, 1211, 1240, 1322, 1414, 1499, 1963, 3117, 3176, 3556–3557, 3560**). NatConn, CrossSub, census, extent, Stations, Precip, Topics, Robot Physiology unchanged. | live greps | Re-read each list live (SH-010) |
| **A-02** | WRONG | **§D Phase 1 climate row:** "⚠ The file is an 8-line STUB, not a dataset — open it and record what it says it lacks". `READER/Sanay.md` was **rebuilt on 2026-10-28** as a 16-line dataset (and the spec's −20 °C stub figure corrected to −16.2 °C the same day). | READER file; spec L76 | Reword; cite the rebuilt file |
| **A-03** | WRONG | **"Datasheets not yet built" sentences** (2026-10-21 builder text): §C intro, §I `DATASHEET-NOT-YET-BUILT(N-5)=20`, §J row. All 19 files exist. | `Datasheets/` | Reword all three |
| **A-04** | GAP | **`06` skip list is incomplete** (this is the cold-run contamination control). Sanay's section in `06_Worked_Example_Provenance.md` runs **L270–L290** ("a future cold pass … must skip the example content in the rows below", L274–275). `Step_10` lists only L270, 274–275, 278, 284, 286–287, 289; the section's **L288** (the M-82 to M-86 row) and the new **L290** (the Run 11 cold-run directory, "all of it") are not on it, and neither is the separator L285. | `06` L270–L290; `Step_10` row | List the section as L270–L290 |
| **A-05** | GAP | **Alias set is thin.** The search set is "Sanay" + "SANAE". Missing names the shared files and the spec use: **SANAE IV**, **S.A.N.A.E. AWS** and its NOAA ID **`AYM00089004`** (spec L73, L116), **Vesleskarvet**, **Ahlmannryggen**, and the sub-location names **Port of Sanay**, **Sanay Corridor**, **Sanay Shipyard / Maritime Shipping Port** (spec L161–167; `06`). Demonym **Sanaian** (spec, Open Questions). | spec L3, L73, L116, L161–167; `06` L270 | Add; re-run the search with them |
| **A-06** | STALE | Pass `README.md` spec pointer is dead (`../../../Specs/Sanay.md`, pre-reorg flat path; the file is `Specs/Halley subnet/Sanay.md`). Local-culture and vision-notes pointers resolve. | README; `ls` | Re-point (deferred README sweep) |
| **A-07** | NOTE | No `Sanay_Inspiration_Place_Research` files yet. Shared items SH-001 … SH-007; megasheet "7 files" = 6 files + 1 subfolder. The Pre-Trip's test-run count ("4 further files name Sanay") is by file, as stated. | | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ (the Pre-Trip row is stale, **A-02**) · G3 `16` Half B ✅ · G4 Register row ✅ · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ (wrong lines cited, **D-02**) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ not in the sheets (**D-05**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals; the 21 per-nation shares sum to **100.00%**; all four count columns sum **exactly** (Census I robots **243,871**, humans **243,714**; Census II robots **137,057**, humans **153,905**); tier lists equal the table (1 / 2 / 18); monthly means average **−16.18 °C** (stated −16.2); precipitation sums to **193 mm** (stated "under 200"); retention 130 ÷ 200 = 65%; polar night May 18 → Jul 28 = **72 days**, midnight sun Nov 12 → Jan 31 = **81 days**; the temperature-range line (L79) matches the means (−23.2 / −23.0; Jan −6.7).

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | DECIDE | **City-to-port distance.** The spec says the city sits "**~200 km** inland" (L161) and the Sanay Corridor is "the **~200 km** route" (L167), from the developer's own catch. `Ports.md` says "~160 km from the ice-shelf edge, ~220 km inland" for the real station (L461) and "a coastal offload **160 km** from the city" (L760). | spec L161, L167; Ports L461, L760 |
| **S-02** | WRONG | **L94 carries ice-shelf boilerplate on a bedrock city:** "Drift management is continuous, and the **surface itself moves with the shelf**", and the regime is labelled "ICE SHELF — flat, exposed, heavily redistributed" (L88). The same file says Sanay stands on Vesleskarvet bedrock that "the ice shelf cities could not have" (L61). | spec L61, L88, L94 |
| **S-03** | NOTE | **L78 is headed "Record extremes" but gives means** ("mean summer air temperature −8.3 °C; mean winter −21.8 °C"). The monthly table's real records are +5.4 (Dec) and −46.2 (Jul). `Step_1_and_2` copies the line under "record extremes". | spec L78, L100–111 |
| **S-04** | NOTE | **Precipitation probability "~0%" for March, April and May** although those months carry 16 / 14 / 12 mm; the provenance note (L116) says the column is *measured* days with ≥0.1 mm. | spec L102–104, L116 |
| **S-05** | NOTE | The station height is 817 m at L73 and 850 m at L116; the rebuilt READER file explains it (AWS 817 m, SANAE IV about 850 m) but the spec does not. | spec L73, L116 |
| **S-06** | NOTE | Timeline repo `Worldspace/Locations/README.md` L17 still lists "Abowasa" and "Princess Elisabeth". Flag only. | README L17 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings L179, L184, L192; census |
| `Step_0` | ✅ census, retention (hand-checked); no extent row |
| `Step_1_and_2` | ✅ climate rows (incl. the 2026-10-28 corrections), READER row, Stations, COMNAP, `16` row, Register; no extent row; copies S-03 |
| `Step_3` | ❌ **D-02** |
| `Step_5` … `Step_9` | ✅ (Step 6 with Subnet column and exact header lines; Step 9 with item 5) |
| `Step_10` | ❌ **D-04**, **D-06** |
| `Phase_2` | ❌ **D-01** |
| `Phase_3` | ✅ ranges L59–128, L139–148, L157–173; concept-art listing |
| `Phase_4` | ✅ `09` L63, `16` L254, `11` (none) |
| `Phase_5` | ❌ **D-03** |
| `Phase_6`, `Phase_8` | ✅ |
| `Phase_7` | ✅ Sweep, Theoretical, Factions; `16` list shifted (A-01) |
| `Phase_9` | ✅ robot share 50.02% |
| `Phase_10` | ✅ |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Phase_2` · Retention | "combined 59.33% · human 62.96% · robot 55.72%" are pre-`DR-68`; `Step_0` gives **59.67% · 63.15% · 56.20%** (hand-checked). | Replace |
| **D-02** | WRONG | `Step_3` · picks rows (6 rows) | Cites `Inspirational-Influences.md` "section at **L173–L178**", picks L174–177. Sanay's heading is now **L204**, its four picks **L205–208**; L173–178 fall in Halley/Belgrano/Santa Luce picks. | Re-point (XS-15) |
| **D-03** | STALE | `Phase_5` | Highways **L241, 243, 300**; Airports **L52, 56**; Ports (32 entries, all +23; list in A-01); RelDB entry "L389–L399" → **L400–L410**, entry lines L390–L396 → **L401–L407**; NatConn list unchanged. | Re-point |
| **D-04** | GAP | `Step_10` | The `06` row lists 8 lines "L270, L274–275, L278, L284, L286–287, L289"; the section is **L270–L290** (A-04). | List the whole section |
| **D-05** | GAP | `Step_0`, `Step_1_and_2` | No extent row. Extent **L624**: Sanay · 463,669 · **46 km²** @10,000/km² · **66** @7,000 · "inland bedrock + coastal port" — a 2026-09-05 snapshot; at the live 487,585 the same arithmetic gives **48.8 / 69.7 km²**. | Add (labelled snapshot) |
| **D-06** | STALE | `Step_10` | "`06` (430 lines)": **431** lines (the added row is L290). | Re-count (SH-009) |
| **D-07** | NOTE | `Step_1_and_2` row 19 | Copies the mislabeled "record extremes" line (S-03). | Follow the source decision |
| **D-08** | NOTE | counts | "203", "74", "293", "378", "166", "36", "246", "199", "28", "146" are each one above `wc -l` (builder's convention, XS-9). | per SH-009 |

### 2d. DECIDE items (collected)
1. **S-01** Which distance governs (200 km or 160 km)? **S-02** Fix L88/L94 (a bedrock city has no moving shelf)? **S-03** Relabel L78.
2. **A-05** Add the SANAE / Vesleskarvet / Port of Sanay strings and re-run the search.
