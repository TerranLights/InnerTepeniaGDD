# Neumayer — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (186 lines), the whole Pre-Trip (565 lines; standard text compared line for line with earlier cities, only differing lines re-read), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `NM-…`). Pass folder: `City_Development_Passes/Halley_Subnet/Neumayer/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run.

**Verdict.** **Nothing blocks a run.** Neumayer's spec is the cleanest read so far: every table and span sums and checks, and the sheets' `09`, `11` and `16` rows are the city's own and current. What is left: **(1)** `Step_3` cites the picks at L164–172, which is now other cities' sections (Neumayer's is L195–202; XS-15); **(2)** `Phase_2` retention is wrong for humans and robots (combined happens to match); **(3)** the usual line shifts in nine shared files, plus Robot Physiology L369 missing from the list; **(4)** a **name collision**: "Neumayer Channel" (a strait by Wiencke Island) is listed as a hit on the city; **(5)** the real names the shared files key on (Atka Iceport, Neumayer I–III, the Skiway) are not aliases; **(6)** "datasheets not yet built", missing extent row, README spec pointer dead.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Halley subnet/Neumayer.md` (186 lines; sheets say 187, builder's convention); later-era headings **L172** (Connection to Concordia) and **L177** (Legacy) = the Step −1 list; spec L3–L8, L15–16, L20–22, L26–62, L63–126, L73–84, L88–91, L129, L133, L139–154, L155–159, L160–166, L167 land on what the sheets say | ✅ |
| Census Section A heading **L146**, entry L148–152 (tier table L150–152), Census I row **L492**, Census II row **L616** | ✅ unchanged |
| Census I **625,874 H / 650,123 R / 1,275,997**; Census II **393,179 / 453,415 / 846,594**; `Step_0` retention recomputed by hand: **66.35% · 62.82% · 69.74%**; robot share 650,123 ÷ 1,275,997 = **50.95%** | ✅ (`Phase_2` disagrees, **D-01**) |
| `09` row **L54** (Required **485,106** · Workforce **963,060** · **50.4%**; header L52); `11` row **L328** (header L326: OLD 50.4% / NEW 61.3%); `16` Half B workforce **963,060** = 650,123 + 0.5 × 625,874 ✓ | ✅ the city's own rows, current values |
| `READER/Neumayer.md` L4–L8; Stations L39 (Neumayer III Skiway); COMNAP pages **8, 49, 76**; Founding Register row **L47** (and L83–84, L94); Sweep **L149**; Theoretical **L971, L974**; Factions (PostWar L89; Second_Interwar L61, 63, 67, 69, 71, 73, 167, 259, 272; Cross_City L22, L49; Hometown L63, L112); Robot_Universals Ch. 14 README **L12**; Extent row L615 and L507, L562, L578; Precip L136; Topics L183–184 | ✅ |
| Zero-hit claims re-run: NMCI, Energy grid, `06` provenance, Geothermal, Arcanet, National Holidays, Robot_Religions, Ice-Cold folder, Meme Machine, True Believer, Enneagram index | ✅ |
| Characters canon: 2 files name the city (Calethina README L58, excluded as later-era; `Formative_History.md`) | ✅ the count |
| Addresses tested exist (Local Culture, Local Robot Culture, Enneagram file, vision notes, concept-art folder (empty), megasheet folder, Tools) | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). `16`: row **L272 → L273**; L80, 114, 185, 222, 231 same; L491, 498–499, 505–506, 518, 535, 575, 588, 673, 1861, 3377 → **L496, 503–504, 510–511, 523, 540, 580, 593, 678, 1866, 3382**. `09` L54 same; L99, 114, 151, 178, 196, 239, 252 → **L101, 116, 153, 180, 198, 241, 254**. Highways L66, 116, 121 same; L238, 240, 242, 267, 285 → **L239, 241, 243, 268, 300**. Airports L48, 52 → **L51, 55**. Ports L103, 176, 182, 245 same; L535, 712, 836 → **L558, 735, 859**. RelDB L23, 31–32, 47, 74 same; L121, 334–335, 341, 396, 439, 518, 529 → **L132, 345–346, 352, 407, 450, 529, 540**. NatConn L37 … L160 same; L313, 366, 489, 548 → **L314, 367, 494, 553**. Robot Physiology: L412, L438 same, **add L369** ("For the robot half of the population, that gradient measures the thing the exile was for. A Neumayerite …"). | live greps | Re-read each list live (SH-010) |
| **A-02** | WRONG | **"Datasheets not yet built" sentences** (2026-10-21 builder text): §C intro, §I `DATASHEET-NOT-YET-BUILT(N-5)=20`, §J row. All 19 files exist. | `Datasheets/` | Reword all three |
| **A-03** | GAP | **Alias set.** The drafted aliases include "Ekström Ice Shelf" and "Queen Maud Land" (places, not names for the city). Missing real names the shared files use: **Atka Iceport** (the city's port, `Ports.md` L558 "Neumayer — Atka Iceport"), **Neumayer Station I / II / III** (spec L129), **Neumayer-Station III** (the climate station, spec L84, L116), **Neumayer III Skiway** (Stations L39), the namesake **Georg von Neumayer** (naming fact only). | spec L3, L84, L129; Ports L558 | Confirm; add |
| **A-04** | WRONG | **A name collision is listed as a hit:** `Ports.md` **L176** reads "Wiencke Island, via the Gerlache Strait and the S-shaped **Neumayer Channel**" — a real strait on the Peninsula, not the city. The Pre-Trip lists L176 under "Names Neumayer at" and `Phase_5` copies the row. | Ports L176 | Remove, or care-note "Neumayer Channel (a strait), not the city" |
| **A-05** | STALE | Pass `README.md` spec pointer is dead (`../../../Specs/Neumayer.md`, pre-reorg flat path; the file is `Specs/Halley subnet/Neumayer.md`). Local-culture and vision-notes pointers resolve. | README; `ls` | Re-point (deferred README sweep) |
| **A-06** | NOTE | No `Neumayer_Inspiration_Place_Research` files yet. Shared items SH-001 … SH-007; megasheet "7 files" = 6 files + 1 subfolder. | | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ · G3 `16` Half B ✅ · G4 Register row ✅ · G5 `Access type: SPUR` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ (wrong lines cited, **D-02**) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ not in the sheets (**D-06**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals; the 26 per-nation shares sum to **99.98%** (rounding); all four count columns sum **exactly** (Census I robots **650,123**, humans **625,874**; Census II robots **453,415**, humans **393,179**); tier lists equal the table (1 / 4 / 21); monthly means average **−16.0 °C** (stated); monthly precipitation sums to **395.5 mm** (stated); retention 257 ÷ 396 = 65%; polar night May 22 → Jul 23 = **63 days**, midnight sun Nov 16 → Jan 27 = **73 days**; the founding line (L133) equals the Register ("The Netherlands and Austro-Bavaria, jointly"). No source error found.

| ID | Sev | Source-level note | Evidence |
|---|---|---|---|
| **S-01** | NOTE | L94 states a peer rank ("14 cities are colder"). The sheets do not carry it. | spec L94 |
| **S-02** | NOTE | L79 "coldest months avg −26 °C": the coldest monthly means are −25.3 (Jul) and −24.6 (Aug); −26 is a rounding up. | spec L79, L105–106 |
| **S-03** | NOTE | L78 "record low −50 °C (8 July 2010)" is below every monthly record low in the table (lowest −47.3, Aug; July −44.8). This is explained, not an error: published-box records are kept over the shorter NCEI period (L113). | spec L78, L113 |
| **S-04** | NOTE | Lost-to-sublimation ~138 against 396 − 257 = 139 (rounding). | spec L89–91 |
| **S-05** | NOTE | Timeline repo `Worldspace/Locations/README.md` L17 still lists "Abowasa" and "Princess Elisabeth". Flag only. | README L17 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings, census |
| `Step_0` | ✅ census, retention (hand-checked); no extent row |
| `Step_1_and_2` | ✅ climate rows, READER L4–8, Stations, COMNAP, Register, founding; ❌ **D-03**, no extent row |
| `Step_3` | ❌ **D-02** |
| `Step_5` … `Step_9` | ✅ (Step 6 with the Subnet column and exact header lines; Step 9 with item 5) |
| `Step_10` | ❌ **D-07** |
| `Phase_2` | ❌ **D-01** |
| `Phase_3` | ✅ ranges L63–126, L139–154, L160–166 |
| `Phase_4` | ✅ `09`, `11`, `16`; ❌ **D-03** (`16` line) |
| `Phase_5` | ❌ **D-04**, **D-05** |
| `Phase_6`, `Phase_8` | ✅ |
| `Phase_7` | ✅ Sweep, Theoretical, Factions; ❌ **D-03** |
| `Phase_9` | ✅ Robot_Universals Ch. 14 hit; robot share 50.95% |
| `Phase_10` | ❌ **D-08** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Phase_2` · Retention | "combined 66.35% · human 62.74% · robot 69.82%": human and robot are the pre-`DR-68` figures (the combined figure happens to be unchanged); `Step_0` gives **66.35% · 62.82% · 69.74%** (hand-checked). | Replace |
| **D-02** | WRONG | `Step_3` · picks rows (8 rows) | Cites `Inspirational-Influences.md` "section at **L164–L172**", picks **L165–L171**. Neumayer's heading is now **L195**, its seven picks **L196–202**; L164–172 hold Dome Fuji's picks, the Halley-subnet heading and Belgrano's heading. | Re-point (XS-15) |
| **D-03** | STALE | `Step_1_and_2` row 37; `Phase_4` row 14; `Phase_7` rows 16–17 | `16` Half B row **L272 → L273**; the "17 other lines" list is the old numbering (A-01). | Re-point |
| **D-04** | STALE | `Phase_5` | Highways L238, 240, 242 → **L239, 241, 243**, L285 → **L300**; Airports **L51, 55**; Ports L535, 712, 836 → **L558, 735, 859**; RelDB entry "L334–L344" → **L345–L355**, entry lines L335–L341 → **L346–L352**; NatConn 15-line list → live list (A-01). | Re-point |
| **D-05** | WRONG | `Phase_5` · Ports L176 row | The row is about "Neumayer Channel" (a strait), not the city (A-04). | Remove or care-note |
| **D-06** | GAP | `Step_0`, `Step_1_and_2` | No extent row. Extent **L615**: Neumayer · 1,252,080 · **125 km²** @10,000/km² · **179** @7,000 · "Ekström ice shelf" — a 2026-09-05 snapshot; at the live 1,275,997 the same arithmetic gives **127.6 / 182.3 km²**. | Add (labelled snapshot) |
| **D-07** | STALE | `Step_10` | "`06` (430 lines) … zero hits": **431** lines; zero hits re-run. | Re-count (SH-009) |
| **D-08** | NOTE | `Phase_10` · Calethina `Formative_History.md` row | Copies the whole build chain, which names five other cities and states Calethina's unmarked in-world origin; Kunlun's sheet copies only the bare stage ("engineering at Kunlun"). | DECIDE: trim to the Neumayer stage ("design work at Neumayer (Halley subnet, confirmed 2026-07-12)") |
| **D-09** | NOTE | `Phase_5` · Highways row 20 | Copies the Temirötkel connecting-road paragraph (another city's own text, which names Neumayer by comparison: "not a minor ramp like the Neumayer connector"); live **L268**. | DECIDE: care-note or drop |
| **D-10** | NOTE | counts | "187", "74", "293", "378", "166", "36", "246", "199", "28", "146" are each one above `wc -l` (the builder's convention, XS-9). | per SH-009 |

### 2d. DECIDE items (collected)
1. **A-03** confirm the alias set (adds Atka Iceport, Neumayer I–III, the Skiway); **A-04 / D-05** remove the "Neumayer Channel" row or care-note it.
2. **D-08 / D-09** trim the two cross-city rows.
