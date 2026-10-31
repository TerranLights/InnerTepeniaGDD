# Relung Panen — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (295 lines), the whole Pre-Trip (622 lines), all 19 datasheets, the pass README and ledger, the city's status file; every cited line opened and compared. **Nothing was edited**; the required edits are in `FIX_LEDGER.md` (entries `RP-…`). Shortened paths: `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`, `ULM` = `Worldspace/Locations-and-Levels/Universal_Location_Methodology`.

**Verdict.** **Nothing blocks a run.** The sheets were rebuilt twice today and it shows: the city-specific line lists are almost all right, the figures match the census and spec, and the hand-added addendum is accurate. What remains: **(1)** a few lines added to shared files after the build are not listed; **(2)** the Phase 8 term count is wrong ("food: 0 hits" against 7 real hits); **(3)** one pick is wrongly excluded as "later-era" (Cinque Terre); **(4)** several climate rows are cut off mid-sentence; **(5)** the city's own Division of Industry determination (file 18) is registered but not transcribed; **(6)** the climate "reader" row is garbled (there is no reader file for this site); **(7)** a handful of source-file statements are stale (retention 71.5%, "await approval and research", stubs, links).

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Mirny subnet/Relung_Panen.md` (underscore filename), 295 lines | ✅ |
| Census I row **L502** and Census II row **L621** | ✅ both Relung Panen; figures match the spec exactly |
| Founding Register row **L65** (+ rulings rows L83, 85, 87, 94, 96) | ✅ |
| `16` Half B header L247 and row **L258**; other mentions L63, L289, L471–472, L474, L3574 | ✅ all seven live |
| `09` L52 (header) and L91 (row); `11` L264, L385 (prose naming the old placeholder); `NMCI` zero hits | ✅ |
| RelDB entry **L111–121** and mentions L28, L49, L169; Cross-Subnet L207; NatConn L301, L396–397 | ✅ (L398 not listed: A-03) |
| Highways L207, L272, L274, L276, L278, L291; Airports L3, L17, L20–22, L64, L86, L99, L102; Ports L26, L144, L149, L151, L198, L207, L224, L232, L240, L244–245, L247, L262, L289, L300 | ✅ every listed line is live and names the city |
| The 16 research files + 24 inspiration files + file 18 + the five own working files + `How_Soil_Is_Made…`; withheld Casey/Mirny airport files named WITHHELD | ✅ all exist |
| Local culture, robot culture, Enneagram, vision-note and neo-race files exist as **stubs** (1.4–1.8 KB; created 2026-10-23), correctly tiered read-last / not inputs | ✅ |
| `City_Megasheets/` has no entry for this city (no folder at all) | ✅ a real absence |
| No READER climate file exists for this site (listing checked); the city's own `Climate.md` is the climate source | ✅ real absence (see A-02 for the wording) |
| Step cards, gate cards, runbook step ranges (except Step 10), spine ranges, all Tier U / project paths | ✅ shared layer, see `TRACKER.md` |
| Research log `Relung_Panen_Research_Log.md` does not exist | ✅ |
| §J's twelve city-specific open items (port, airports, intake, founding remainder, power, cold chain, 71 tiers, census table, two climate records, extent/coordinates, stubs) | ✅ each states "does not block"; each statement matches its source |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | NOTE | §C Step 10 governing range and `T8` reads say **3057–3177** (Casey's sheet says 3172). Step 10 ends at **L3152**. The sheet's own check "12 of 12 ranges equal the live range" is therefore wrong for Step 10. | runbook headings | shared fix SH-005 |
| **A-02** | WRONG | **Climate row is garbled.** §D Phase 1: "⚠ Station/city name divergence — the file is keyed `Relung_Panen.md`, not the city's current name `Relung_Panen`" (same string twice; the address is the city's own `Climate.md`, not a reader file). §A: "Climate READER key … differs from the city's current name". There is **no READER file** for this site. | `ls READER` for bunger/relung/oasis: none; Required Reference says so | Reword both rows: "No READER file exists (a real absence); `Cities/Relung_Panen/Climate.md` is the climate file; its §4 records the sources tried" |
| **A-03** | GAP | **Lines naming the city that are missing from the lists:** `Highways.md` **L281**; `Airports.md` **L23** (Winter Intake Airport row); `Ports.md` **L298, L302** (§3e) and **L872** (a research-log filename); `City_National_Connections.md` **L398**; `Official_Population_Census.md` **L770**; `Extent_and_Density_Per_City.md` **L686**. | live `grep` | Add |
| **A-04** | GAP | **Alias set is thin.** Missing: the five candidate names the spec lists as "gathered, not chosen" (L5: *Dobrowolski · Oazis · Bunger · Figurnoye · Edgeworth David*); the site names the research files use (*Oasis station · White Smoke Lake · Algae Lake · Apfel Glacier · Shackleton Ice Shelf · Denman Glacier*); and **three spellings of one place**: spec "Transkriptsii Gulf" (L13, L252), `Airports.md` "Transkripsii Inlet", research "Transcription Gulf". The "non-Latin script at L9, 13" hit is the ⏸️/⛔ symbols, not a script. | spec L5, L13; Airports L21 | Add to §A; drop the false hit |
| **A-05** | GAP | **Phase 2 (§D) does not list the composition file**, although the datasheet does (`Upper_Earth_Immigration_Composition.md` L579–642, verified; gateway row L137). | opened | SH-010 |
| **A-06** | GAP | **Phase 7 (§D) and `Phase_7.md` do not carry the city's own determination (file 18)**, the central Phase 7 input: D = 1.43; baseline 322,197 (43.9%); distinctive 411,031; food 25% = 102,758, agricultural research 4% = 16,441, seed breeding 3% = 12,331, phosphorus and soil recovery 6% = 24,662; mandate 156,192 (21.3%); free 254,839 (34.8%). It is named only in the §D addendum. All figures re-checked: workforce 494,585 + 0.5 × 477,285 = 733,227.5 ✓; shares sum to 38%; spec L230 agrees. | file 18 opened | Add rows |
| **A-07** | NOTE | Extent: the sheet says there is no row in the "other 25" table and the city's extent is "declared elsewhere in the file" but does not name where (the extent record is §11, with L642, L645, L666, L686 in the list). Also the file's table figures are a **dated snapshot** (SH-011). | `Extent…` L631 | Say "§11" |
| **A-08** | NOTE | Pass `README.md` "existing sources": "Local culture … *(does not exist yet)*" (stubs exist since 2026-10-23) and "Vision notes" listed as a source (struck, `DR-10`). | opened | Reword |
| **A-09** | NOTE | §I's "carried-over names: Wilkes@L26" is a false hit (the spec's own region name *Wilkes Land*); the sheet does not say so. §D Phase 1 says the Megasheet folder "holds 0 files" — the folder does not exist. | | Reword |

### 1c. Required inputs
T0-1 spec ✅ · T0-2 coordinates/Geographic Basis ✅ · T0-3 census ✅ · T0-4 parent ✅ · G1 symbol pair: **no entry exists yet** (spec L289: "correctly last"; by design) · G2 climate (own `Climate.md`, no reader file: real absence, documented) ✅ · G3 `16` Half B row + file 18 ✅ (A-06) · G4 Register row + `Founding population:` ✅ · G5 `Access type: SPUR` + Highways/Airports/Ports ✅ · G6 defining event: none (canon gap, ruled non-blocking) · G7 28 tiered picks ✅ · G8 census row + composition file; **the census has no per-city tier table (on hold by ruling)**, the spec's table serves ✅ · T2-8 extent declared ✅. **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: the 11 shares sum to **100.00%**; all four count columns sum **exactly** (494,585 · 477,285 · 353,062 · 340,951); monthly means average **−11.18 °C** (stated −11.2); monthly precipitation sums to **92.2 mm** (stated ~92); amplitude 19.3 K = 0.6 − (−18.7); winter solstice daylight **2.7 h** agrees with the table (and is consistent with the latitude); density 971,870 ÷ 450 km² = 2,160/km² and the old 947,954 ÷ 450 = 2,107 ✓; "29% of what it could take" = 971,870 ÷ 3,375,000 ✓; workforce and mandate figures agree with file 18.

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **L21 "(retention 71.5%)"** is the pre-`DR-68` figure. 694,013 ÷ 971,870 = **71.41%** (human 71.44%, robot 71.39%), which is what the sheets compute. | arithmetic |
| **S-02** | NOTE | **L215–216** says `T2-5` records no `Local_Cultures`, `City_Vision_Notes`, `City_Enneagram_Personalities` or `City_Megasheets` entry. Four stub files exist (2026-10-23); the Megasheet folder does not. | listing |
| **S-03** | NOTE | **L43, L111, L295** link to `../Relung_Panen/README.md` and `../Relung_Panen/Climate.md`; from `Specs/Mirny subnet/` these resolve to `Specs/Relung_Panen/…` (does not exist). The folder is `CITIES/Relung_Panen/` (`../../Relung_Panen/`). | path test |
| **S-04** | NOTE | **L219–222** ("whoever holds this city holds the food supply of 31.7 million people … the most concentrated point of failure") is a "feeds N people" style claim, which the Division-of-Industry reliability rule says is not citable, and it sits against the 2026-10-28 ruling (Strong 25% role; the city is optional) and the spec's own L14. | spec L14, L230 |
| **S-05** | WRONG | `Inspirational-Influences.md` **L120** (the city's picks intro) says the further candidates "await approval and research". They were **researched in two rounds on 2026-10-29** (24 files); only their tiers await the developer. | Pre-Trip addendum; Research_Logs |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` (13 rows) | ✅ every cell and line (L1, L3, L8, L9–13, L14 compare-flag, L19–21, the three later-era headings at L263/L269/L276 ✓); length "296" is `wc` 295 (SH-009) |
| `Step_0` (7) | ✅ census rows and retention (71.41 / 71.44 / 71.39 recomputed by hand); no extent row (A-07) |
| `Step_1_and_2` (36) | ✅ Climate.md L20–26 (each cell ✓), L101/L114, research E L26–28 (each figure ✓), Register L65, spec L196–197, L35–37, L226; COMNAP page 68 = the Oazis entry (printed pp. 118–119); ❌ **D-02, D-03, D-04** |
| `Step_3` (30) | ✅ 28 picks transcribed word for word (L121–L148, 2 PRIMARY / 17 SECONDARY / 9 SUPPORTING); ❌ **D-05, D-06** |
| `Step_5` | ✅ stub, both files exist |
| `Step_6`–`Step_9` | ✅ all ten section headers and column names match the live table (L44–L160); Step 9 carries item 5 ✓ |
| `Step_10` | ✅ zero hits in `06` (only the "430 lines" length is now 431 because a pointer line was appended: **D-12**) |
| `Phase_2` (16) | ✅ tiers, annotations, census, retention, Falkland rows, Register; composition file L579–642 ✓ |
| `Phase_3` (6) | ✅ ranges: Geographic Basis L76–L193, Character & Culture L213–L225, Notable Locations L246–L256 |
| `Phase_4` (7) | ✅ `09` L91 ✓ (275,990 ÷ 733,228 = 37.6%), `16` L258 ✓ ❌ **D-03** |
| `Phase_5` (49) | ✅ every cited line live and correct; RelDB entry L111–L118 ✓; ❌ **D-07** (missing lines) |
| `Phase_6` (6) | ✅ zero-hit claims all re-run true (6 religion files, 7 Buddhism files) |
| `Phase_7` (9) | ✅ `16` lines, DoI README L49 ✓; ❌ **D-08, D-09** |
| `Phase_8` (4) | ❌ **D-10** |
| `Phase_9` (5) | ✅ 33 files / zero hits; robot share **50.89%** (494,585 ÷ 971,870 = 50.889) ✓; Laws-of-Robotics citation to `Robot_Physiology_Quick_Reference.md` pending the Tier U audit |
| `Phase_10` (5) | ✅ 587 character files, zero hits; Enneagram index zero hits; Notable Figures L257 ✓ |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | NOTE | all | "N-line file" counts one above `wc -l` (296 vs 295; 100 vs 99; 146 vs 145; 166 vs 165; 293 vs 292; 378 vs 377; 74 vs 73; 251 vs 250; 246 vs 245) | SH-009 |
| **D-02** | WRONG | `Step_1_and_2` · spec L109, L113, L126, L131, L189 | **Rows cut off mid-sentence** (the cell holds only the first physical line of a wrapped paragraph): L109 ends "for the annual", L113 "cut off from open", L126 "so", L189 "wet cold rather". L131 (precipitation) is cut after "anchored between Davis's measured 72.8 mm", which also **names another city**, while L116 and L117 (which compare with other cities) were correctly not copied. | Complete each row from the live lines (L109–111, L113–114, L126–128, L131–133, L189–190); treat L131 as "compares the city with other places: not copied" or drop the fragment |
| **D-03** | NOTE | `Step_1_and_2`, `Phase_4`, `Phase_7` · `16` Half B row | The free-tier cell reads **"34.8%\*"** in the source (the asterisk means "before cold-chain"); the sheets print "34.8%". | Add the asterisk and its meaning |
| **D-04** | GAP | `Step_0` / `Step_1_and_2` | No row for the extent band (spec L30–31: ~450 km², up to 942 km² with marine areas; density 2,160/km²; the extent file's §11) | Add, with SH-011 |
| **D-05** | STALE | `Step_3` · picks line L120 | Transcribes the source's "(#27 to #97) await approval and research" (source stale, S-05); the Pre-Trip addendum says they are researched. | Fix the source (RP-S05), then the row follows |
| **D-06** | WRONG | `Step_3` · row for L147 | "[source line excluded: later-era content]". **L147 is Cinque Terre, Italy [SUPPORTING]** ("on cliff terraces often one vine row wide, 57 small rack monorails … a growers' cooperative was founded in 1973 to stop the land being abandoned"). It is not later-era; the word "abandoned" (land abandonment) tripped the scan. | Copy the row |
| **D-07** | GAP | `Phase_5` | Missing: `Highways.md` L281; `Airports.md` **L23**; `Ports.md` L298, L302; `City_National_Connections.md` **L398** ("3 line(s)" should be 4). | Add |
| **D-08** | GAP | `Phase_7` | The city's own determination (file 18, A-06) is not transcribed. | Add rows |
| **D-09** | NOTE | `Phase_7` | Header "13 of 13 addresses named" and the last row "11 of 11 exist on disk" disagree. | Reconcile (SH-008) |
| **D-10** | **WRONG** | `Phase_8` · spec term check | "cuisine / food / dish / drink — **0 hit(s)**": the spec contains **"food" 7 times** (L14, L218–240 agricultural role). "dress/clothing/attire — 0 hits": the one raw hit is *address* (L291), so semantically 0. music 0, craft 0 ✓. | Recount; say "food: 7 (all agricultural production, not cuisine)" |
| **D-11** | NOTE | `Phase_9` | Laws of Robotics and Doll categories rows cite `Robot_Physiology_Quick_Reference.md` / a bare filename (see Casey D-27). | Tier U audit |
| **D-12** | NOTE | `Step_10` · "06 (430 lines)" | now 431: the 2026-10-29 pointer lines added a final line to the 41 method and tracking files, so any sheet that states one of those files' length is now one short. | Re-state, or stop stating lengths |

### 2d. Source corrections needed (the developer decides)
RP-S01 spec L21 71.5% → 71.4% · RP-S02 spec L215–216 · RP-S03 spec L43, L111, L295 links · RP-S04 spec L219–222 · RP-S05 `Inspirational-Influences.md` L120 · plus the stale placeholder names in `11` L264, L385 (held for the rename sweep) and `Relung_Panen/ULM_Input_Status.md`'s out-of-date rows (kept as history by design).
