# Belgrano — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (169 lines), the whole Pre-Trip (565 lines; the standard text was read in full on earlier cities and compared line for line — only the differing lines were re-read), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `BG-…`). Pass folder: `City_Development_Passes/Halley_Subnet/Belgrano/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run.

**Verdict.** **Nothing blocks a run.** Belgrano's sheets are synced to the 2026-10-28 census, the `09`/`11`/`16` rows are the right city's, and the quoted rows and zero-hit claims check out. What is left: **(1)** `Step_3` cites the picks section at L141–148, which is now the **Mawson** subnet's part of the file (Belgrano's is L172–179; XS-15); **(2)** `Phase_2` retention is the pre-census-change set and contradicts `Step_0`; **(3)** the usual line shifts in eight shared files, plus census L548 missing from the Pre-Trip's list; **(4)** the "datasheets not yet built" sentences; **(5)** the extent row is missing; **(6)** three spec lines contradict the spec's own table or text (temperature range, record high, "three subnets"), and the sheet copies two of them; **(7)** the README spec pointer is dead.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Halley subnet/Belgrano.md` (169 lines; the sheets say 170, the builder's convention); the later-era headings at **L155** (Connection to Concordia) and **L160** (Legacy) are exactly the Step −1 sheet's list; every spec line the sheets cite (L3–L8, L15–16, L20–22, L26–51, L52–117, L62–80, L120, L122, L128–135, L136–140, L141–149, L150–154) lands on what the sheet says | ✅ |
| Census Section A heading **L210**, entry L212–218, tier table **L214–216** (annotation on L216), Census I row **L496**, Census II row **L615**; other census lines L789–790, L804 | ✅ (but L548 is missing from the list, **A-01**) |
| Census I **544,064 H / 551,743 R / 1,095,807**; Census II **437,927 / 415,687 / 853,614**; retention in `Step_0` recomputed by hand: 853,614 ÷ 1,095,807 = **77.90%**, 437,927 ÷ 544,064 = **80.49%**, 415,687 ÷ 551,743 = **75.34%** | ✅ (`Phase_2` disagrees, **D-02**) |
| `09` row **L64** (header L52): D 1.43 · Humans 544,064 · Residents 1,095,807 · Required **312,138** · Workforce 823,775 · **37.9%**; `11` row **L99** (header L95): marine workers 98,484 · 24.6 Mt · 7.6×; `16` Half B row **L252** (header L247): workforce **823,775** = 551,743 + 0.5 × 544,064 ✓ | ✅ the sheets carry the city's own rows with current values |
| `READER/Belgrano.md` L4–L8 (authority, station notes, period, range, annual −13.2); Stations L13 (Belgrano II Skiway); COMNAP pages **8, 10**; Founding Register row **L53** (text word for word) | ✅ |
| NMCI quotes L50, L52, L57, L69, L137; Sweep **L128, L146, L187**; DoI README L49; Theoretical **L970–971, L975–976**; Factions: `PostWar_Refugee` 15 lines (59 … 103), `Second_Interwar` L97, 99, 103, 107, 111, 113, `Cross_City_Cultural_Patterns` L89–91, 94, 109, 126, `Hometown-based_Faction_Possibilities` L29; Polydimensional Animism `Culture.md` L20 and `README.md` L174, L221; CrossSub L109, L203; Extent row **L619** | ✅ unchanged |
| Zero-hit claims re-run: Energy grid, `06` provenance (0 hits), Geothermal, Arcanet, National Holidays, Ice-Cold folder, Meme Machine, True Believer, Robot_Universals (33 files), Enneagram index | ✅ |
| Characters canon: 587 files; **13** name the city (Villena Hiresvett 2 files, Trisha Miller 3, Salagéa Aparast 3, Griselda Alejandra Chávez 5), and the sheet lists exactly those 13 | ✅ the count and the files |
| Every address tested exists (Local Culture, Local Robot Culture, Enneagram file, vision notes, concept-art folder (empty), megasheet folder (6 `.md` files + 1 subfolder), Tools scripts) | ✅ |
| Spec `Founding population:` is consistent with the Register row ("Argentina; accessible from Argentina") | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). `16`: row L252 and L208 same; L327, 410, 449 → **L330, 413, 452**; L544, 555, 557, 562, 570, 581, 584, 589 → **L549, 560, 562, 567, 575, 586, 589, 594** (sheet 584 → 589, 589 → 594); L632, 638, 718, 752, 783, 930 → **L637, 643, 723, 757, 788, 935**; L1425, 1432, 1493, 1886, 3430, 3561 → **L1430, 1437, 1498, 1891, 3435, 3566**. `09` L64 same, L204 → **L206**. Highways L58, 67, 114, 116, 118, 120, 127 same; L256 → **L257**; L343 → **L358**. Airports L3, 19–20 same; L33, 61, 96, 103 → **L36, 64, 99, 108**. Ports L123, 127, 137, 155, 182 same; L322, 359, 372, 376, 381, 413, 432, 713, 768, 803, 836 → **L345, 382, 395, 399, 404, 436, 455, 736, 791, 826, 859**. RelDB L23–24, 36, 47, 73, 89–90, 96 same; L122, 238–239, 286, 341, 372, 374, 396, 519, 532 → **L133, 249–250, 297, 352, 383, 385, 407, 530, 543**. NatConn L45–47 … L210 same; L376, 544, 593 → **L377, 549, 598**. Census: add **L548** (the Census I sum note that names Belgrano's annotations). | live greps | Re-read each list live (SH-010) |
| **A-02** | WRONG | **"Datasheets not yet built" sentences** (2026-10-21 builder text): §C intro, §I count `DATASHEET-NOT-YET-BUILT(N-5)=20`, §J row "Datasheets not yet built for this city". All 19 files exist. | `Datasheets/` | Reword all three |
| **A-03** | STALE | Alias set (mechanical, unconfirmed): drafts "Coats Land coast / Weddell Sea sector" and "Queen Maud Land" as aliases (they are places). Missing real names: **Belgrano II** (READER key and the spec's climate-station name), **Belgrano II Base**, **Belgrano II Skiway** (Stations L13), **Belgrano Station II** (RelDB L90), the namesake **Manuel Belgrano** (spec L8, L124 — a naming fact only), demonym **Belgranian / belgranteco** (spec L167). Spec L161 (the search hit) holds no alias. | spec L3, L8, L124, L167 | Confirm; add |
| **A-04** | STALE | Pass `README.md` "existing sources": the **spec pointer is dead** (`../../../Specs/Belgrano.md`, the pre-reorg flat path; the file is `Specs/Halley subnet/Belgrano.md`). Local-culture and vision-notes pointers resolve; the research-log file does not exist yet (README says so). | README; `ls` | Re-point (deferred README sweep) |
| **A-05** | NOTE | No `Belgrano_Inspiration_Place_Research` files exist yet. Shared items SH-001 … SH-007; megasheet folder "7 files" = 6 files + 1 subfolder. | | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ · G3 `16` Half B ✅ · G4 Register row ✅ · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ (the sheet cites the wrong lines, **D-01**) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ not in the sheets (**D-04**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals; the 15 per-nation shares sum to **99.98%** (rounding); all four count columns sum **exactly** (Census I robots **551,743**, humans **544,064**; Census II robots **415,687**, humans **437,927**); tier lists equal the table (1 / 3 / 11); monthly means average **−13.18 °C** (stated −13.2); precipitation sums to **299.5 mm** (stated); retention 195 ÷ 300 = 65%; polar night Apr 26 → Aug 19 = **116 days**, midnight sun Oct 24 → Feb 19 = **119 days**; record low −58.9 (May) matches the table.

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **L68 "coldest months avg −30 °C; warmest month avg −5 °C"** matches no column of the table below it: the coldest monthly mean is −20.9 (Jul), the coldest average low −25.0 (Jul); the warmest mean is −2.4 (Jan) and the average highs are +0.7 / +0.8. The `Step_1_and_2` sheet copies the line. | spec L68, L89–100 |
| **S-02** | WRONG | **L67 "record high +11.4 °C (January)"**: the table's highest record is **+12.1 °C (December)**; January is +11.4. The sheet copies the line. | spec L67, L89, L100 |
| **S-03** | WRONG | **L122 "extended across three cities in three different subnets"**: it then names Esperanza and Marambio (Palmer) and Belgrano (Halley) — **two** subnets, as Open Questions says (L168, "three Argentine cities in two subnets"). The line also describes other cities' communities inside this city's founding statement. The `Step_1_and_2` sheet copies it. | spec L122, L168 |
| **S-04** | NOTE | L83 states a peer rank ("17 cities are colder"). The sheets do not carry it. | spec L83 |
| **S-05** | NOTE | Daylight column: August "0\*" although polar night ends Aug 19 (twelve days of daylight follow); the only footnote under the table is the polar-night/midnight-sun span line (L110). | spec L96, L110 |
| **S-06** | NOTE | Lost-to-sublimation: ~104 mm against 300 − 195 = 105 (rounding). | spec L78–80 |
| **S-07** | NOTE | Timeline repo `Worldspace/Locations/README.md` L17 still lists "Abowasa" and "Princess Elisabeth". Flag only. | README L17 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings L155, L160; census lines (excluded by design as carrying DLC status cells) |
| `Step_0` | ✅ census rows, retention (hand-checked); no extent row (**D-04**) |
| `Step_1_and_2` | ✅ climate rows, READER L4–8, Stations, COMNAP, `16` row, Register; ❌ **S-01 … S-03** copied, no extent row |
| `Step_3` | ❌ **D-01** |
| `Step_5` … `Step_9` | ✅ (Step 6 with the Subnet column and exact header lines; Step 9 carries item 5) |
| `Step_10` | ❌ **D-05** |
| `Phase_2` | ✅ tiers, annotations, Register; ❌ **D-02** |
| `Phase_3` | ✅ section ranges L52–117, L128–135, L141–149 |
| `Phase_4` | ✅ `09`, `11`, `16`, NMCI rows (the city's own, current values) |
| `Phase_5` | ✅ quoted content; ❌ **D-03** |
| `Phase_6` | ✅ Polydimensional Animism hits |
| `Phase_7` | ✅ Sweep, Theoretical, Factions; ❌ **D-03** |
| `Phase_8`, `Phase_9` | ✅ robot share **50.35%** (551,743 ÷ 1,095,807) |
| `Phase_10` | ❌ **D-06** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | WRONG | `Step_3` · picks rows (7 rows) | Cites `Inspirational-Influences.md` "section at **L141–L148**", picks **L142–L147**. After Relung Panen's section was added, Belgrano's heading is **L172** and its six picks **L173–178**; L141–148 now fall in the Mawson subnet's part of the file. | Re-point (XS-15) |
| **D-02** | STALE | `Phase_2` · Retention | "combined 78.16% · human 80.80% · robot 75.55%" are the pre-`DR-68` figures; `Step_0` gives **77.90% · 80.49% · 75.34%** (hand-checked). The row says "cross-ref `Step_0.md`". | Replace |
| **D-03** | STALE | `Phase_5`, `Phase_7` | Citation numbers are the old set (see A-01): Highways **L257, L358**; Airports **L36, 64, 99, 108**; Ports (+23); NatConn 17-line list → live list; `16` "24 other lines" list → live list; `Phase_5`'s RelDB entry lines L89–L99 are unchanged. | Re-point |
| **D-04** | GAP | `Step_0`, `Step_1_and_2` | No extent row. Extent **L619**: Belgrano · 1,071,890 · **107 km²** @10,000/km² · **153** @7,000 · "Bertrab nunatak" — a 2026-09-05 snapshot; at the live 1,095,807 the same arithmetic gives **109.6 / 156.5 km²**. | Add (labelled snapshot) |
| **D-05** | STALE | `Step_10` | "`06` (430 lines) … zero hits": **431** lines; zero hits for "Belgrano" re-run. | Re-count (SH-009) |
| **D-06** | NOTE | `Phase_10` · Characters rows (4 of them) | Later-era wording is copied where adjacent rows exclude it: Salagéa Aparast README **L7** ("an active, present-day courier … not settled in Concordia"); Trisha Miller README **L7** (present-day residence in "Taurus (residential district), Concordia"); Griselda Alejandra Chávez README **L67** (a TODO list about low orbit, Deimos and an activation date). | DECIDE: exclude as later-era, like the neighboring rows |
| **D-07** | NOTE | counts | "170-line", "74", "293", "378", "166", "36", "199", "28" are each one above `wc -l` (169, 73, 292, 377, 165, 35, 198, 27): the builder's convention (XS-9). | per SH-009 |
| **D-08** | NOTE | `Step_1_and_2` rows 19–20, 41 | Copy S-01, S-02, S-03 (record high, temperature range, "three subnets"). | Follow the source decisions |

### 2d. DECIDE items (collected)
1. **S-01 / S-02 / S-03** Approve three source edits in the spec (L68, L67, L122).
2. **D-06** Exclude the present-day character rows.
3. **A-03** Confirm the alias set.
