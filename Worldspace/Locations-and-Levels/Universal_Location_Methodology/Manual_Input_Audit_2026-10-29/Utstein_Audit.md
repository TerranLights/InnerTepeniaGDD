# Utstein (formerly Princess Elisabeth) — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (205 lines), the whole Pre-Trip (568 lines; standard text compared line for line with earlier cities, only differing lines re-read), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `UT-…`). Pass folder: `City_Development_Passes/Halley_Subnet/Utstein/` (renamed from `Princess_Elisabeth` on 2026-10-23). `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run. Renamed 2026-10-03 (`DR-38`); the held shared files mostly still say "Princess Elisabeth".

**Verdict.** **Nothing blocks a run.** The spec's arithmetic is exact, the measured-climate correction of 2026-10-28 is carried into the sheets (not into the Pre-Trip), and the census values are current. What is left: **(1)** `Step_3` cites the picks at L194–200, which is now other cities' lines (Utstein's are L225–230; XS-15); **(2)** `Phase_2` retention is the pre-census-change set; **(3)** the Pre-Trip still calls the climate file "an 8-line STUB" and says the pass folder and concept-art folder "keep the old name by design" (both were renamed); **(4)** all four README source pointers name the old city and the old flat paths; **(5)** the usual line shifts, "datasheets not yet built", and a missing extent row; **(6)** the sheets keep the old name in every shared-file row, which is correct for the shared files but should carry the alias.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Halley subnet/Utstein.md` (205 lines; sheets say 206, builder's convention). Later-era headings **L178, L183, L191** = the Step −1 list; spec L3, L5–L10, L23–24, L28–30, L34–71, L72–136, L82–100, L139, L141, L147–160, L161–165, L166–172, L173 land on what the sheets say | ✅ |
| Census Section A heading **L188**, entry L190–196 (tier table L192–194), Census I row **L495**, Census II row **L618**; other lines L798–799, L801, L804 | ✅ unchanged |
| Census I **565,907 H / 595,927 R / 1,161,834**; Census II **409,511 / 373,098 / 782,609**; `Step_0` retention recomputed by hand: **67.36% · 72.36% · 62.61%**; robot share 595,927 ÷ 1,161,834 = **51.29%** | ✅ (`Phase_2` disagrees, **D-01**) |
| `09` row **L65** (live label "Princess Elisabeth"; header L52): Required **329,183** · Workforce **878,881** · **37.5%**; `11` row **L100** (header L95): marine workers 79,430 · 19.9 Mt · 6.1×; `16` Half B row (live label "Princess Elisabeth") workforce **878,880** = 595,927 + 0.5 × 565,907 | ✅ the city's own rows, current |
| `READER/Princess_Elizabeth.md` (rebuilt 2026-10-28; "READER station: none"; the station's own IMAU AWS16, 2009–2020; annual −18.0): the twelve monthly means equal the spec's Mean column; the `Step_1_and_2` sheet says so | ✅ (the file name is spelled "Elizabeth", **A-05**) |
| Stations **L46** (Perseus Airstrip) and **L51** (Princess Elisabeth Skiway) — the sheet correctly leaves out L25 and L63 ("Princess Elizabeth **Land**", a region); COMNAP pages **8, 26, 63**; Founding Register row **L51** (and L85, L91, L94); Sweep **L150**; Factions `Second_Interwar` L119, 121, 133, 135, 137; Polydimensional Animism `Culture.md` L25 and `README.md` L180, L229; CrossSub L95, L203; Highways L129; Topics L189–190; Extent row L618 | ✅ |
| Zero-hit claims re-run: NMCI, Energy grid, `06` provenance, Theoretical-Calculations, National Holidays, Ice-Cold folder, Robot_Universals; Characters canon: only `Calethina/README.md` (excluded as later-era in the sheet) | ✅ |
| Addresses tested exist (Local Culture, Local Robot Culture, Enneagram file, vision notes, concept-art folder `Utstein/` (empty), the Alias Table `City_Renames_Alias_Table_2026-10-03.md`, Tools) | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). `16`: row **L264 → L265**; L161, 222 same; L349, 438 → **L352, 441**; the other 19 entries +5 (L846 … L3553–3554 → **L851, 906, 1053, 1399, 1491, 1652, 1709, 1789, 1987, 1989, 2046, 2393, 2490, 2601, 2610, 2778, 2804, 3558–3559**). `09` L65 same; L205 → **L207**. Airports L49, 53 → **L52, 56**. Ports L26 same; L460, 717 → **L483, 740**. RelDB L24, 47 same; L284–285, 367–368, 370, 449, 501 → **L295–296, 378–379, 381, 460, 512**. NatConn L9, 133, 140, 145, 244 same; L378, 390, 518, 527, 537 → **L379, 391, 523, 532, 542**. Add `Precipitation_Falls_vs_Lands.md` **L127** (row "Princess_Elisabeth · 200 · 140 · 60"). Highways, CrossSub, `11`, Stations, census, extent, Topics, Register, Polydimensional Animism unchanged. | live greps | Re-read each list live (SH-010) |
| **A-02** | WRONG | **§D Phase 1 climate row:** "⚠ Station/city name divergence … ⚠ The file is an 8-line STUB, not a dataset — open it and record what it says it lacks". `READER/Princess_Elizabeth.md` was **rebuilt on 2026-10-28** as a 16-line dataset (and the spec's climate rows replaced by the station's own AWS16 data the same day). The name divergence remains. | READER file | Reword; cite the rebuilt file |
| **A-03** | WRONG | **"Datasheets not yet built" sentences** (2026-10-21 builder text): §C intro, §I `DATASHEET-NOT-YET-BUILT(N-5)=20`, §J row. All 19 files exist. | `Datasheets/` | Reword all three |
| **A-04** | WRONG | **§J rename row:** "the pass folder and megasheet/concept-art folders keep the old name by design (nothing was moved)". The pass folder is `Utstein/` and the concept-art folder is `Utstein/` (renamed 2026-10-23); only `City_Megasheets/Halley_Subnet/Princess_Elisabeth/` keeps the old name. | `ls` | Reword |
| **A-05** | NOTE | The climate file is spelled **`Princess_Elizabeth.md`** (with a z); the station, the spec and `Precipitation_Falls_vs_Lands.md` use "Elisabeth" (with an s). The Pre-Trip notes the divergence from the current name but not the misspelling; "Princess Elizabeth **Land**" is a different Antarctic region and a false-positive source (Stations L25, L63). | `ls READER/` | Care-note; leave the file name unless the developer wants it fixed |
| **A-06** | STALE | Pass `README.md` "existing sources": **all four pointers name the old city and the old flat paths** — `../../../Specs/Princess_Elisabeth.md`, `Local_Cultures/Halley_Subnet/Princess_Elisabeth.md`, `City_Vision_Notes/Princess_Elisabeth.md`, `Research_Logs/Princess_Elisabeth_Research_Log.md` (none exists). Real: `Specs/Halley subnet/Utstein.md`, `Local_Cultures/Halley_Subnet/Utstein.md`, `City_Vision_Notes/Utstein.md`, `Research_Logs/Utstein_Research_Log.md` (does not exist yet). | README; `ls` | Re-point (deferred README sweep) |
| **A-07** | NOTE | No `Utstein_Inspiration_Place_Research` files yet. Shared items SH-001 … SH-007; megasheet "7 files" = 6 files + 1 subfolder. | | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ (the Pre-Trip row is stale, **A-02**) · G3 `16` Half B ✅ · G4 Register row ✅ · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ (wrong lines cited, **D-02**) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ not in the sheets (**D-05**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals; the 27 per-nation shares sum to **100.01%** (rounding); all four count columns sum **exactly** (Census I robots **595,927**, humans **565,907**; Census II robots **373,098**, humans **409,511**); tier lists equal the table (2 / 5 / 20); monthly means average **−17.94 °C** (stated −18.0); polar night May 16 → Jul 29 = **75 days**, midnight sun Nov 11 → Feb 1 = **83 days**; record high +4.2 (Dec) and low −38.5 (Aug) match the table; the temperature-range line (L88) matches the means; the founding line (L141) equals the Register row. No source error found.

| ID | Sev | Source-level note | Evidence |
|---|---|---|---|
| **S-01** | NOTE | L76 and L10 compare the site with other cities ("closer to Dome Fuji than to Troll or Santa Luce"; "closer to Dome Fuji than to the western Halley subnet cities"). The sheets do not carry them. | spec L10, L76 |
| **S-02** | NOTE | L125 states a peer count ("19 of the 37 cities …"); the precipitation columns are derived estimates, as the note says. | spec L125 |
| **S-03** | NOTE | Timeline repo `Worldspace/Locations/README.md` L17 still lists "Princess Elisabeth" (rename sweep held). Flag only. | README L17 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings L178, L183, L191; census |
| `Step_0` | ✅ census, retention (hand-checked); no extent row |
| `Step_1_and_2` | ✅ climate rows incl. the 2026-10-28 corrections, READER row, Stations, COMNAP, `16` row, Register; ❌ **D-03**, no extent row |
| `Step_3` | ❌ **D-02** |
| `Step_5` … `Step_9` | ✅ (Step 6 with Subnet column and exact header lines; Step 9 with item 5) |
| `Step_10` | ❌ **D-06** |
| `Phase_2` | ❌ **D-01** |
| `Phase_3` | ✅ ranges L72–136, L147–160, L166–172 |
| `Phase_4` | ✅ `09`, `11`, `16` rows (they carry the live label "Princess Elisabeth"); ❌ **D-03** |
| `Phase_5` | ❌ **D-04** |
| `Phase_6`, `Phase_8`, `Phase_10` | ✅ |
| `Phase_7` | ✅ Sweep, Factions; ❌ **D-03** |
| `Phase_9` | ✅ robot share 51.29% |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Phase_2` · Retention | "combined 67.38% · human 72.49% · robot 62.55%" are pre-`DR-68`; `Step_0` gives **67.36% · 72.36% · 62.61%** (hand-checked). | Replace |
| **D-02** | WRONG | `Step_3` · picks rows (7 rows) | Cites `Inspirational-Influences.md` "section at **L194–L200**", picks L195–199. Utstein's heading is now **L225**, its five picks **L226–230**; L194–200 hold the end of Santa Luce's picks and Neumayer's section. | Re-point (XS-15) |
| **D-03** | STALE | `Step_1_and_2` row 34; `Phase_4` row 14; `Phase_7` rows 16–17 | `16` Half B row **L264 → L265**; the "23 other lines" list is the old numbering (A-01). | Re-point |
| **D-04** | STALE | `Phase_5` | Airports L49, 53 → **L52, 56**; Ports L460, 717 → **L483, 740**; RelDB entry "L367–L377" → **L378–L388**, entry lines L368–L374 → **L379–L385**; NatConn 10-line list → live list. | Re-point |
| **D-05** | GAP | `Step_0`, `Step_1_and_2` | No extent row. Extent **L618**: Princess Elisabeth · 1,137,917 · **114 km²** @10,000/km² · **163** @7,000 · "Utsteinen ridge" — a 2026-09-05 snapshot; at the live 1,161,834 the same arithmetic gives **116.2 / 166.0 km²**. | Add (labelled snapshot) |
| **D-06** | STALE | `Step_10` | "`06` (430 lines) … zero hits": **431** lines; zero hits re-run (all three names). | Re-count (SH-009) |
| **D-07** | NOTE | counts | "206", "74", "293", "378", "166", "36", "246", "199", "28", "146" are each one above `wc -l` (builder's convention, XS-9). | per SH-009 |

### 2d. DECIDE items (collected)
1. **A-05** fix the climate file name spelling or leave it with a care-note.
