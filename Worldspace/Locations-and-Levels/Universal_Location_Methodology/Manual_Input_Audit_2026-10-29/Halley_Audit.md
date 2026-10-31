# Halley — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (217 lines), the whole Pre-Trip (566 lines; the standard text was read in full on an earlier city and compared line for line — only the lines that differ were re-read), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `HL-…`). Pass folder: `City_Development_Passes/Halley_Subnet/Halley/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run. **City and subnet share the name**, which is the source of the worst finding below.

**Verdict.** **Nothing blocks a run, but one sheet row would mislead it.** Halley's sheets were brought up to the 2026-10-28 census (Census I and II, retention in `Step_0`, the `16` workforce, robot share), and the spec's arithmetic is exact. What is left: **(1)** `Phase_4` carries **Neumayer's** row of `09` (old census values included) as "the city's own row", because the builder matched the Subnet column; Halley's row is the next one down; **(2)** `Step_3` cites the picks section at L149–157, which is now the **Mawson** subnet's section — Halley's is at L180–187 (every sheet from the Mawson subnet onward will have the same +31 shift, see `TRACKER.md` XS-15); **(3)** `Phase_2` retention disagrees with `Step_0`; **(4)** the Pre-Trip and sheets still say the datasheets "are not yet built"; **(5)** the usual line shifts in eight shared files; **(6)** the extent row is missing; **(7)** the spec's record-high line contradicts its own table.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Halley subnet/Halley.md` (217 lines; the sheets say 218, the builder's convention, XS-9). Later-era headings at **L185, L193, L199** (the Step −1 sheet's list is exact); spec L3–L9, L15–16, L20–22, L26–53, L66–87, L135, L137, L145, L157, L165, L175 all land on what the sheets say | ✅ |
| Census Section A heading **L134**, tier table **L138–140** (the `(founding wave)` annotation on L140), Census I row **L486**, Census II row **L606**; other census lines L482, 492, 495–496, 499, 501, 505, 530, 534, 604, 615–616, 618, 622, 624, 631, 648, 652, 747 | ✅ (the Pre-Trip's census list is exact; the table has not moved) |
| Census I **721,889 H / 754,374 R / 1,476,263** and Census II **517,317 / 586,599 / 1,103,916** in spec and census; retention in `Step_0` recomputed by hand: 1,103,916 ÷ 1,476,263 = **74.78%**, 517,317 ÷ 721,889 = **71.66%**, 586,599 ÷ 754,374 = **77.76%** | ✅ (but `Phase_2` disagrees, **D-02**) |
| Founding Register row **L46** (text word for word); Register lines for the Halley subnet L46–53, 74, 90 (the Pre-Trip's list is exact) | ✅ |
| Extent row **L609**; other extent lines L507, 561, 578, 605, 615, 618–619, 621, 623–624 (the Pre-Trip's list is exact) | ✅ (not in the sheets, **D-07**) |
| `READER/Halley.md`: twelve monthly means equal the spec's Mean column exactly; annual −19.2 (stated −19) | ✅ |
| `16` Half B header **L247** (and the Step 6 sheet's ten section-header lines **L44, 56, 68, 80, 93, 106, 116, 128, 138, 153** in `Cross_City_Culture_Differentiation_Table.md`); `11` row **L329** (header L326, Neumayer L328); `Stations` L28 (Halley Skiway); COMNAP pages **8, 78**; `CrossSub` 14 lines (45, 47, 50, 60–61, 95, 109, 118, 159–160, 184, 189, 203–204); NatConn **52** lines (count right; line numbers shifted, **A-01**); Sweep **L147** (6/6 row) and **L187**; DoI README **L49**; Theoretical **L970, L972, L1023**; Factions `Second_Interwar` L61, 63, 71, 73, 167, 201 and `Cross_City_Cultural_Patterns` L24; Universe `Locations/README.md` **L17** | ✅ |
| Zero-hit claims: Energy grid, NMCI, Arcanet, Geothermal, `06` provenance (0 hits; **D-06** for the count), National Holidays, Meme Machine, True Believer, Robot_Religions (6 files), Ice-Cold folder (7 files), `jobs_professions_and_fields/`, Robot_Universals (33 files), Enneagram index | ✅ re-run |
| Characters canon: 587 `.md` files; the only one that names the city (not the subnet) is `Salagéa Aparast/README.md` **L59**; Calethina and Griselda Alejandra Chávez hit only on "Halley subnet" | ✅ |
| Every backticked address tested exists (Local Culture, Local Robot Culture, Enneagram file, vision notes, concept-art folder (empty), megasheet folder (7 entries), the four `Tools/` scripts, Zodiac files) | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). `16`: Halley's row **L273 → L274**; other lines L53, 80, 113, 173, 208, 252, 254 same; L262, 264, 272, 277, 283 → **L263, 265, 273, 278, 284**; L298 → **L301**; L517, 519 → **L522, 524**; L619, 623, 626–627, 631, 639 → **L624, 628, 631–632, 636, 644**; L669–670 → **L674–675**; L869, 890, 930 → **L874, 895, 935**; L1347, 1411 → **L1352, 1416**; L2302, 2536, 3205 → **L2307, 2541, 3210**. `09`: L54–55, 61–65, 74 same; L99, 151, 173, 197, 239 → **L101, 153, 175, 199, 241**. Highways: L62, 67, 116, 120, 185, 187, 190 same; L248, 250, 252, 254, 256 → **L249, 251, 253, 255, 257**; L283–284 → **L298–299**. Airports L48, 52, 60 → **L51, 55, 63**. Ports: L68, 182 same; L322–323, 365, 367, 376–377, 381, 384, 413–414, 431, 716, 791, 836, 844 → **L345–346, 388, 390, 399–400, 404, 407, 436–437, 454, 739, 814, 859, 867** (all +23). RelDB: L23, 27, 47, 71, 73, 84, 93, 95–96 same; L232–233, 236–239, 283, 330, 338, 341, 371, 393, 458, 507, 511, 532 → **L243–244, 247–250, 294, 341, 349, 352, 382, 404, 469, 518, 522, 543** (+11). NatConn: L36 … L283 same; L313, 366, 368, 376, 378, 390 → **L314, 367, 369, 377, 379, 391** (+1); L417, 424, 426, 428, 489, 503, 518, 527, 529, 544, 548, 557, 581 → **L422, 429, 431, 433, 494, 508, 523, 532, 534, 549, 553, 562, 586** (+5). | live greps | Re-read each list live (SH-010) |
| **A-02** | WRONG | **"Datasheets not yet built" sentences** (the 2026-10-21 builder text): §C intro ("**not yet built** — November item N-5; the addresses below are where the files will be created"), §I (`DATASHEET-NOT-YET-BUILT(N-5)=20`), §J row "Datasheets not yet built for this city". All 19 files exist. | `Datasheets/` | Reword all three (as Casey's sheet: "19 files, all present") |
| **A-03** | STALE | Alias set is mechanical (the sheet says so): it drafts "Brunt Ice Shelf · Coats Land · Weddell Sea" as aliases (they are places, and "Weddell Sea" also names Belgrano's and Sanay's lines). Missing real names: **Halley Bay** (the real station's first name), **Halley I … VI** individually, **Halley Research Station**, **Halley Skiway** (the Stations file row, L28), the demonym **Hallite** (spec L216). | spec L3, L58, L216; Stations L28 | Confirm which are aliases; add the missing |
| **A-04** | GAP | **Founding Register is an address only as a §J note** (rows L46–53, 74, 90); the sheets cite it with a line (L46) — no repair needed beyond the §J wording in A-02. | | none |
| **A-05** | STALE | Pass `README.md` "existing sources": the **spec pointer is dead** — `../../../Specs/Halley.md` is the pre-reorg flat path; the file is `Specs/Halley subnet/Halley.md`. The local-culture (`Local_Cultures/Halley_Subnet/Halley.md`) and vision-notes (`City_Vision_Notes/Halley.md`) pointers resolve; the research-log pointer names a file that does not exist yet ("created at Step 3", as the README says). | README; `ls Specs/` | Re-point the spec pointer (the deferred README sweep) |
| **A-06** | NOTE | No `Halley_Inspiration_Place_Research` files exist yet (the other cities' two rounds are made); `Russia_Split_Proportions_RS3_Halley_and_Janbogo_2026-10-29.md` names the city (informational, nothing ruled). | `ls Research_Logs` | Register when/if made |
| **A-07** | NOTE | Shared items (SH-001 … SH-007, megasheet folder "7 files" = 6 files + 1 subfolder). | | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened, `DR-8`) · G2 climate ✅ · G3 `16` Half B ✅ · G4 Register row + `Founding population:` ✅ · G5 `Access type: SPUR` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ (but the sheet cites the wrong lines, **D-03**) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip, ❌ not in the sheets (**D-07**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their stated totals; the 17 per-nation shares sum to **100.00%**; all four count columns sum **exactly** (Census I robots **754,374**, humans **721,889**; Census II robots **586,599**, humans **517,317**); tier lists equal the table (1 Primary, 5 Significant, 11 Notable) and the tier shares equal their weights (Significant 44.12% = 15/34, Notable 32.35% = 11/34); monthly means average **−19.18 °C** (stated about −19); polar night May 3 → Aug 11 = **101 days**; midnight sun Oct 31 → Feb 13 = **106 days**; retention 292 ÷ 450 = 64.9% (stated ~65%); lost 158 ✓; the record low −54.4 (Jul) matches "about −55".

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **L69 "record high approximately +5 °C"** contradicts the monthly table, whose January record high is **+7.2 °C** (December +6.8). The line was not updated when the monthly extremes were added (2026-09-04). The `Step_1_and_2` sheet copies the +5. | spec L69, L93, L104 |
| **S-02** | NOTE | Precipitation is stated three ways: "approximately 300–450 mm" (L71), "falls ~450 mm/yr" (L76), and the monthly column sums to **346 mm** (L93–104). The column is a derived estimate (provenance note L109). | spec L71, L76, L93–104 |
| **S-03** | NOTE | L81 states a peer rank ("10 cities are colder"); the sheets do not carry it. | spec L81 |
| **S-04** | NOTE | The de-stacking note (L28) says each tier's total **and ordering** is preserved, but Germany (Significant, **4.21%**) sits below Netherlands (Notable, **4.30%**) in the table. Tier totals are right. | spec L28, L37–38 |
| **S-05** | NOTE | L137 "Primarily British exiles alongside a broader Atlantic-region community" is not marked as rewritten to the Register (as Mirny's and Ariun Nuur's founding lines were); the Register row says "The UK, in a central role", partial (✅ partial, `DR-22`). Consistent in substance. | spec L137; Register L46 |
| **S-06** | NOTE | The timeline repo's `Worldspace/Locations/README.md` L17 still lists "Abowasa" and "Princess Elisabeth" (rename sweep held). Flag only. | README L17 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ spec location, later-era headings, census; "218 lines" (XS-9) |
| `Step_0` | ✅ census, retention (hand-checked), frame rows; no extent row (**D-07**) |
| `Step_1_and_2` | ✅ climate rows, READER monthly means, Stations, COMNAP, Register, Settled/Founding L135, L137; ❌ **D-04** (`16` row), no extent row |
| `Step_3` | ❌ **D-03** |
| `Step_5` | ✅ stub |
| `Step_6` | ✅ ten sections with the Subnet column and exact header lines |
| `Step_7`, `Step_8` | ✅ standard text |
| `Step_9` | ✅ carries item 5 |
| `Step_10` | ❌ **D-06** |
| `Phase_2` | ✅ tiers, annotations, Falkland rows; ❌ **D-02** |
| `Phase_3` | ✅ section ranges L54–132, L145–156, L165–174 |
| `Phase_4` | ❌ **D-01**, **D-04** |
| `Phase_5` | ✅ content of the quoted rows; ❌ **D-05**, **D-08** |
| `Phase_6` | ✅ zero-hit rows |
| `Phase_7` | ✅ Sweep, DoI README, Theoretical, Factions; ❌ **D-04** |
| `Phase_8`, `Phase_9` | ✅ robot share **51.10%** (754,374 ÷ 1,476,263) |
| `Phase_10` | ✅ Characters row; ❌ **D-09** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | WRONG | `Phase_4` · `09` row | **The row is Neumayer's, not Halley's, and its numbers are pre-`DR-68`:** "City: Neumayer · Subnet: Halley · D 2.50 · Humans 613,735 · Residents 1,252,080 · Required 475,924 · Workforce 945,213 · 50.4%" cited at L52, L54. The builder matched the Subnet column and took the first row. **Halley's own row is `09` L55:** D 2.50 · Humans **721,889** · Residents **1,476,263** · Required **560,759** · Workforce **1,115,319** (`16` has 1,115,318: 0.5 rounding) · **50.3%**. The same sheet's `11` row (L329, Halley: OLD 50.3% / NEW 61.2%) is right. | Replace the row (and say the `#` rank is not carried) |
| **D-02** | STALE | `Phase_2` · Retention | "combined 74.92% · human 71.74% · robot 77.95%" are the pre-`DR-68` figures; `Step_0` (and a hand recomputation) give **74.78% · 71.66% · 77.76%**. The row says "cross-ref `Step_0.md`". | Replace |
| **D-03** | WRONG | `Step_3` · picks rows (8 rows) | Cites `Inspirational-Influences.md` "section at **L149–L157**, picks **L150–L156**". After Relung Panen's section was added (L119–149), Halley's heading is **L180** and its seven picks are **L181–187**; L149–156 now hold the Mawson subnet heading and **Mawson's** picks. A run following the citations would read the wrong city's picks. | Re-point all 8 citations |
| **D-04** | STALE | `Step_1_and_2` row 33; `Phase_4` row 15; `Phase_7` rows 17–18 | `16` Half B row **L273 → L274** (header L247 right); the "31 other lines" list is the old numbering (see A-01). The workforce 1,115,318 is current. | Re-point |
| **D-05** | STALE | `Phase_5` (Highways, Airports, Ports, RelDB, NatConn rows) | Every citation is the old numbering: Highways L248–256 → **L249–257**, L283–284 → **L298–299**; Airports **L51, 55, 63**; Ports (+23) **L345–346 … L867**; RelDB entry "L232–L242" → **L243–L253**, entry lines L233–L239 → **L244–L250**; NatConn 52-line list → live list (A-01). Content of the quoted rows is unchanged. | Re-point |
| **D-06** | STALE | `Step_10` | "`06` (430 lines) … zero hits": the file is **431** lines; zero hits for "Halley" re-run. | Re-count (SH-009) |
| **D-07** | GAP | `Step_0`, `Step_1_and_2` | No extent row. Extent **L609**: Halley · 1,452,345 · **145 km²** @10,000/km² · **207** @7,000 · "Brunt ice shelf — MIGRATING" — a 2026-09-05 snapshot; at the live 1,476,263 the same arithmetic gives **147.6 / 210.9 km²**. | Add (labelled snapshot) |
| **D-08** | NOTE | `Phase_5` · Ports L844 row | The row copies a Ports.md line that names a **Background-Lore vignette** (`…/Halley_03_No_Harbor_By_Design.md`). Vignettes are not canon and never an input; a pointer in an input sheet invites a read. | DECIDE: strike the path or mark "found, not opened" |
| **D-09** | NOTE | `Phase_10` · Salagéa row | Copies "recruitable companion/protagonist of the Halley DLC" as written. Ariun Nuur's sheet excludes DLC-companion status as non-ULM content; this row is inconsistent with that treatment. | DECIDE: exclude as Ariun's |
| **D-10** | NOTE | counts | Line counts "218", "74", "293", "378", "166", "36", "246", "199", "146" are each one above `wc -l` (217, 73, 292, 377, 165, 35, 245, 198, 145): the builder's convention (XS-9), not an error in the file. | per SH-009 |

### 2d. DECIDE items (collected)
1. **D-08** strike or keep the vignette pointer; **D-09** DLC wording in `Phase_10`.
2. **A-03** confirm the alias set.
3. **S-01** approve the L69 source edit (record high: +7.2 °C).
