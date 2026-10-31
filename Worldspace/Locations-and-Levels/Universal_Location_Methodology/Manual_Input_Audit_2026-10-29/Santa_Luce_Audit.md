# Santa Luce — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (193 lines), the whole Pre-Trip (591 lines), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `SL-…`). Pass folder: `City_Development_Passes/Halley_Subnet/Santa_Luce/` (the Pre-Trip's own header says it was generated against the old name "Abowasa"; the folder was renamed). `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`.

**Verdict.** **Nothing blocks a run.** Today's hand work on this city (the two-Italys composition, the census figures, the DR-67 withholding) is consistent everywhere I looked, and the spec's arithmetic is exact. What is left: **(1)** the Pre-Trip's line lists for six shared files and several sentences about "datasheets not yet built" and "research rounds not run" are stale; **(2)** five datasheet citations point at blank lines or a heading (Highways), one Phase 2 figure set is from the old census, and two cells contradict a neighbor; **(3)** the pass README's source pointers all name the old city name and the wrong folder; **(4)** the new inspiration research for this city (four files made today) is not registered anywhere.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Halley subnet/Santa_Luce.md`; Census Section A heading L166, tier table **L168–172** (updated for `DR-83`: Magna Lombardia and Meridia); Census I row **L499**; Census II row **L624** | ✅ all land on this city; figures match the spec exactly |
| Founding Register row **L49** (text matches the datasheet row word for word) and rulings rows L85, L91, L94 | ✅ |
| Extent row **L621** (437,614 · 44 / 63 km² · Basen nunatak, updated in place) | ✅ (this row was updated in place on 2026-10-29 and follows the live census) |
| `16` Half B row **L278** (D 1.54 · 330,697 · 45.6% · 5.4% · 49.0% · H; workforce = 223,780 + 0.5 × 213,834 = 330,697 ✓); `09` row L61 (128,426 ÷ 330,697 = 38.8% ✓) | ✅ |
| Composition file section **L288–L296** and gateway row **L138** (Magna Lombardia ≈18M and Meridia ≈9M marked illustrative; tiers equal the spec's) | ✅ |
| `READER/Aboa.md` (keyed by the old station name, rebuilt 2026-10-21): twelve monthly means equal the spec table's Mean column exactly (−5.2 … −5.5; average −15.0) | ✅ |
| Local Cultures and Enneagram files exist (withheld for this pass, `DR-67`); **the Local Robot Culture file does not exist** (as the sheet says); vision-notes file exists, struck; megasheet folder `City_Megasheets/Halley_Subnet/Abowasa/` (6 files + 1 subfolder; the sheet says 7); concept-art folder empty | ✅ |
| Own working files (README, hand-over, robot-culture revisit tracker) registered as read-last; `Inspirational-Influences.md` picks section **L189–L194** | ✅ |
| Shared layer (ranges, cards, Tier U/project paths) | ✅ except the shared items in `TRACKER.md` |
| Zero-hit claims: Stations file, `11`, NMCI, Arcanet, Geothermal, Energy grid | ✅ re-run |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | WRONG | **The sheet says the datasheets are not built.** §C (intro box): "(**not yet built** — November item N-5; the addresses below are where the files will be created)"; §J: "**Datasheets not yet built for this city**"; §I's verification counts "DATASHEET-NOT-YET-BUILT=20". All 19 exist. | `Datasheets/` (19 files) | Reword all three; replace "(19 files, all present)" as in Casey's sheet |
| **A-02** | STALE | **Line lists after later edits** (Pre-Trip vs live): Highways L240→**241**, L242→**243**, L256→**257**, L284–285→**299–300**; Airports L33, L41, L97, L114→**36, 44, 100, 119**; Ports L460, L717→**483, 740**; RelDB L237–238, L339, L341, L395, L501, L529, L532→**248–249, 350, 352, 406, 512, 540, 543** (L23, 27, 31, 47, 67–68, 95 unchanged); NatConn L594→**599**; `16` L352, 436, 623, 632, 649, 664, 669–670, 689, 811, 930, 3550→**355, 439, 628, 637, 652/654, 669, 674–675, 694, 816, 935, 3555** (plus **L1**, the title line, which names the city); `09` L202→**204** (+L1). | live `grep` of each file | Re-read each list live |
| **A-03** | NOTE | §D Phase 1 `16` row says "Santa Luce's row **L277**"; §C Step 2 and §E say **L278**, which is right (L277 is Shirayuki's row). | `16` L277–278 | Use L278 everywhere |
| **A-04** | GAP | Founding Register rows: sheet lists L49, 85, 91, 94; **L95** (the 2026-10-23 `DR-60` row, "Italy resolved to its two successors") also names the city. | Register | Add |
| **A-05** | GAP | **Alias set is thin.** Missing: **Vestfjella** (the spec's own name for the range), **Aboa-Wasa / Nordenskiöld Base** (spec L71), **Camp Maudheimvida / Maudheimvida** (the IMAU station the extremes come from, spec L83), **Aboa Weather Station**, the placeholder spellings `{{ Abowasa }}` / `{{ABOWASA}}`, the demonym **Abowasian** (spec L151). | spec L71, L83, L151 | Add to §A |
| **A-06** | GAP + STALE | **Four research files made today are not registered:** `Research_Logs/Santa_Luce_C01_Inspiration_Place_Research_R1.md`, `…_R2.md`, `…C02_…_R1.md`, `…_R2.md` (the first 13 of the 76 candidates). §J still says "**both research rounds are not run**". The picks themselves are withheld (`DR-67`); whether these files are readable by the run is the developer's call. | `ls Research_Logs` | Register with a tier; fix §J |
| **A-07** | GAP | Pass `README.md` "existing sources" points at names and folders that no longer exist: `../../../Specs/Abowasa.md` (real: `Specs/Halley subnet/Santa_Luce.md`), `Local_Cultures/Halley_Subnet/Abowasa.md`, `City_Vision_Notes/Abowasa.md` (struck), `Research_Logs/Abowasa_Research_Log.md`. (Known: the README source-pointer sweep was deferred to the end by the developer; it belongs in the sweep.) | README | Re-point |
| **A-08** | NOTE | §C Step 10 range 3057–3172 (SH-005); Megasheet folder "7 files" is 6 files and a subfolder. | | shared |
| **A-09** | NOTE | §A "Climate READER key … `READER/Aboa.md`" is correct, but the file is not a READER station file (it says "READER station: none"); the sheet's Phase 1 row explains this well. | `READER/Aboa.md` L3 | none |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened, `DR-8`; withheld here by `DR-67` anyway) · G2 climate ✅ · G3 `16` Half B ✅ · G4 Register row + `Founding population:` ✅ · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (ruled non-blocking) · G7 picks: **withheld by ruling; the run is thinner at G7 and must say so** (the sheet says so) · G8 census tier table + composition file ✅ · T2-8 extent ✅. **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: 28 shares sum to **100.00%**; tier totals equal the 8/3/1 weights (Primary 17.02% = 8/47; Significant 38.29% ≈ 18/47; Notable 44.69% ≈ 21/47); tier lists (L22–24) equal the per-nation table; monthly means average **−15.01 °C** (stated −15); coldest/warmest (−22 / −5) match; polar-night span May 12–Aug 2 = 83 days and midnight-sun span Nov 8–Feb 5 = 90 days check out; record high +4.1 and record low −45.4 match the table; monthly precipitation sums to 126 mm.

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | NOTE | **Precipitation is stated three ways:** "approximately 100–150 mm" (L90), "Falls ~150 mm/yr" with 105 landed and 45 lost (L95–97), and the monthly column sums to **126 mm** (L106–117). The column is labelled "DERIVED, NOT MEASURED" (L122). | spec |
| **S-02** | NOTE | Station altitude: L83 says Aboa sits at "~400 m"; L122 and `READER/Aboa.md` say **484 m**. | spec L83, L122 |
| **S-03** | WRONG | **`City_Relationship_Database.md` L74** (Santa Luce's own entry, "Notes") still reads "Finnish-Swedish joint founding, the only dual-national founding in Tepenia" — the founding the Register and spec have superseded (`DR-22`, `DR-60`). The datasheet correctly does not copy it. | RelDB L74 |
| **S-04** | NOTE | The universe repo's `Worldspace/Locations/README.md` L17 still lists "Abowasa" and "Princess Elisabeth" (rename sweep held). The timeline repo takes no worldbuilding edits: flag only. | README L17 |
| **S-05** | NOTE | Spec L10 (Significance) and the spec's "Status/Current Status" carry later-era text; correctly excluded by the sheets. | |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ every row and line (the three later-era headings at L172, L177, L185 ✓; census L17–18 ✓); ❌ **D-01** |
| `Step_0` | ✅ census rows; retention recomputed by hand 59.14 / 61.93 / 56.48; no extent row (**D-09**) |
| `Step_1_and_2` | ✅ climate rows L79–L97 word for word; Register L49 ✓; Settled/Founding L135, L137 ✓; Economy L155; ❌ **D-02, D-03** |
| `Step_3` | ❌ **D-04** |
| `Step_5` | ✅ DR-67 flag; the missing robot-culture file is correctly marked |
| `Step_6`–`Step_9` | ✅ ten table sections incl. the Subnet column; Step 9 carries item 5 |
| `Step_10` | ✅ zero hits in `06` ("430 lines" now 431) |
| `Phase_2` | ✅ tiers, annotations (none), census Section A L170–172, composition L288–296, Falkland rows; ❌ **D-05** |
| `Phase_3` | ✅ ranges (Geographic Basis L67–L132, Character & Culture L143–L154, Notable Locations L160–L166) |
| `Phase_4` | ✅ `09` L61, `16` L278, NMCI zero |
| `Phase_5` | ✅ RelDB entry L67–L77, Airports L36/44/100/119, Ports L26/182/483/740, composition L138; ❌ **D-06, D-07, D-08** |
| `Phase_6` | ✅ zero-hit claims re-run |
| `Phase_7` | ✅ Sweep L145, Factions lines L89 / L31, 33, 45, 51, 53, 57 all name the city; ❌ **D-10** |
| `Phase_8` | ✅ term check (the 8 raw "dish" hits are "Swedish"); stale line count (**D-11**) |
| `Phase_9` | ✅ robots 51.14% (223,780 ÷ 437,614 = 51.136%) |
| `Phase_10` | ✅ 587 files, Notable Figures L167 |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | NOTE | `Step_-1` · "Specs file length" | "192 lines" counted 2026-10-21; the spec is now **193** (`DR-83` added rows). | Re-count (and SH-009) |
| **D-02** | WRONG | `Step_1_and_2` · `16` row | "(header L247, **row L277**)": the row is **L278** (L277 is another city's). The citation cell before it says L278. | Correct |
| **D-03** | NOTE | `Step_1_and_2` · L90 row | Copies "one of the drier Halley subnet cities" (a peer comparison) while L81 (also a comparison) is marked "not copied". | Mark L90's clause "[comparison not carried]" |
| **D-04** | WRONG | `Step_3` · picks section row | "Section at **L158–L163**"; the section is **L189–L194** (the next cell cites L189 correctly). | Correct |
| **D-05** | **WRONG** | `Phase_2` · Retention | "**58.73% · 61.64% · 55.97%**" are the old-census figures (old Census II ÷ old Census I); the sheet says "cross-ref `Step_0.md`", which gives **59.14 · 61.93 · 56.48**. | Recompute |
| **D-06** | STALE | `Phase_5` · Highways rows | Five citations point at blank lines or a heading: L240, L242, L256 are blank; L285 is the heading "Major Junctions Index". Live: **L241, L243, L257, L299, L300** (texts unchanged). | Re-point |
| **D-07** | STALE | `Phase_5` · NatConn | L594 → **L599** | Re-point |
| **D-08** | NOTE | `Phase_5` · Highways L120 | Copies a line whose subject is another city's ice-shelf movement. | Mark "compares/describes another city: not copied" or keep as relation |
| **D-09** | GAP | `Step_0`, `Step_1_and_2` | No row for the extent band (Extent row L621: 44 km² at 10,000/km², 63 km² at 7,000, Basen nunatak). | Add |
| **D-10** | WRONG | `Phase_7` · "other lines naming the city" | The Value cell lists the **old** numbers (L352, 436, 623, 632, 649, 664, 669–670, 689, 811, 930, 3550) and the Citation cell the **re-pointed** ones (L355, 439, 628, 637, 654, 669, 674–675, 694, 816, 935, 3555): they disagree. The live list is also one longer (**L652**, a section heading "{{ABOWASA}} — HELD AT CURRENT VALUE", and the title line L1). | Make both cells the live list |
| **D-11** | NOTE | `Phase_8` · "full 192-line file" | now 193 (SH-009). | |
| **D-12** | GAP | `Step_3` / Pre-Trip | the four new research files (A-06). | Register |
| **D-13** | NOTE | all | "N-line file" counts one above `wc -l` (SH-009): 146, 166, 293, 378, 74, 246. | |
| **D-14** | NOTE | `Phase_9` | Laws / Doll rows cite `Robot_Physiology_Quick_Reference.md` / a bare filename (Tier U audit). | |

### 2d. Source corrections needed (the developer decides)
SL-S01 spec precipitation (L90 / L95–97 / table sum) · SL-S02 spec L83 altitude "~400 m" vs 484 m · SL-S03 `City_Relationship_Database.md` L74 founding statement · SL-S04 (flag) universe-repo `Worldspace/Locations/README.md` L17 names · SL-S05 pass README pointers (A-07).
