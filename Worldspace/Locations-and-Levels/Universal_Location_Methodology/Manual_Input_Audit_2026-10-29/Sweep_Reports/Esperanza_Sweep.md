# Esperanza — sweep report (2026-10-30)

**City:** Esperanza (ledger section B27) · **Date:** 2026-10-30 · **Who:** sub-agent (Sonnet 5.5), one pass, Edit tool only, nothing committed.
**Read:** `SWEEP_BRIEF.md` (with §4a); `FIX_LEDGER.md` section A (SH-001 … SH-023) and `### B27 · ESPERANZA`; `Esperanza_Audit.md`; the whole Pre-Trip (565 lines), `README.md`, `00.2_Position_Coverage_Ledger.md` (not edited) and all 19 datasheets; every cited source line re-opened live (Airports, Ports, Highways, RelDB, NatConn, CrossSub, `09`, `11`, `16`, NMCI, Census, Extent, Register, Inspirational-Influences, Upper_Earth_Immigration_Composition, the spec, runbook, spine, `02`, trial recipe, Step 10 section, Tier U sheets for the Tier-U half of the recount). Withheld files (megasheets, culture, Enneagram, vision notes, symbol files, Background-Lore) were not opened. Graphify was not run.
**Pass folder:** `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Palmer_Subnet/Esperanza`.

**Counts:** APPLIED 24 (13 per-city: ES-001, 002, 004, 006, 007, 020, 021, 022, 023, 024, 027, 028, 029; 11 shared: SH-001, 002, 003, 004, 005, 008, 010, 011, 012, 013, 014) · ALREADY-RIGHT 1 (SH-006) · PARTIAL 1 (ES-025) · HELD 2 (SH-007, SH-009; plus the held open-question half of ES-025) · SKIPPED-MISMATCH 0 · NEEDS-DEVELOPER 1 (the open-question half of ES-025). Untouched by design: ES-003, ES-005, ES-026 (`DECIDE`); ES-S01 … ES-S08 (source decisions / notes).

---

## 1 · Result table

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| ES-001 | APPLIED | Pre-Trip §C Step 2 (T8 reads), §D Phase 1 `16` row, §D Phase 4 `09` row, §D Phase 5 Airports / Ports / RelDB / NatConn rows, §E | `16` row 259→**260** (twice); `09` L104, L207→**L106, L209**; Airports L41, L48→**L44, L51**; Ports L513, L710, L729→**L536, L733, L752**; RelDB L123, L208–209, L213, L260, L295–296, L350–351, L417→**L134, L219–220, L224, L271, L306–307, L361–362, L428**; NatConn L407, L439, L459→**L412, L444, L464** (still 9 lines); `16` other 23 lines→**L317, 366, 1151, 1236, 1344, 1350, 1361, 1367, 1375, 1389, 1394, 1405, 1412, 1425, 1429, 1446, 1448, 1516, 1749, 1891, 2804, 3229, 3565** **plus the §11 heading L1332** (marked "the city's own upper-case heading … supersedes Half B's MAND% / FREE%") | Each list regenerated from a live `grep -n -i esperanza` of the file: Airports 44, 51 · Ports 155, 169, 177, 536, 733, 752 · RelDB 20, 46, 134, 219, 220, 224, 271, 306, 307, 361, 362, 428 · NatConn 75, 183, 185, 189, 208, 209, 412, 444, 464 (= 9) · `09` 81, 106, 209 · `16` 260, 317, 366, 1151, 1236, 1332, 1344 … 3565 (24 lines incl. the heading). Odd hits opened: RelDB L271, L306–307, L361–362, L428 are neighbors' entries that name Esperanza (same kind as the old list); NatConn L412, L444, L464 are Lazar-related passages naming Esperanza (same kind as the old L407, L439, L459). Highways L55, 75, 77, 79, CrossSub L36, L202, NMCI (13 lines), `11` L264/L332, Register L39–40, Extent L409/460/464/512, Topics L204/207, Precip L169 re-read: unchanged |
| ES-002 | APPLIED | Pre-Trip §C intro box (L53); §J row | "**not yet built** — November item N-5; the addresses below are where the files will be created" → "19 files, all present"; §J row "Datasheets not yet built for this city" deleted. §I `DATASHEET-NOT-YET-BUILT(N-5)=20` / `RESOLVE=121` left as the dated build record, as the ledger says | `ls Datasheets/` = 19 files (Phase_2–10 = 9, Step_-1, 0, 1_and_2, 3, 5, 6, 7, 8, 9, 10 = 10) |
| ES-003 | untouched (`DECIDE`) | — | Only SH-011's label was put on the Pre-Trip's extent citations (see SH-011). The old-census figures, the 190 / 272 recomputation and the open question (Extent L460–470, L464, Ports L513) were **not** added | — |
| ES-004 | APPLIED | `README.md` | `../../../Specs/Esperanza.md` → `../../../Specs/Palmer subnet/Esperanza.md` | `ls` of the resolved path from the pass folder: the file exists. Local-culture pointer also resolves (existence only) |
| ES-005 | untouched (`DECIDE`) | — | alias set not changed | — |
| ES-006 | APPLIED | Pre-Trip §D Phase 10 "U Characters" row (carve-out cell) | Added the GDD tree: `Worldspace/Characters/` names Esperanza in **13 files** (Griselda Alejandra Chávez 2 · Shuchar Vaszyong 5 · TBN [TCY-45 heavenly summertime Momo] 6), file list given, coordinates only; the timeline-repo tree stated as 3 files | `grep -ril esperanza` on both trees: GDD 13 files (2 + 5 + 6 = 13 ✓), timeline repo 3 files (Griselda README, Conflict_Experiences, Formative_History) ✓ |
| ES-007 | APPLIED | Pre-Trip | the shared items below | see SH rows |
| ES-020 | APPLIED | `Phase_2.md` "Retention" | 62.72% · 52.62% · 73.18% → **62.76% · 52.79% · 73.08%** | By hand: 1,193,886 ÷ 1,902,205: 1,902,205 × 0.6276 = 1,193,823.8, remainder 62.2 → +0.0033 → 62.76%. 510,762 ÷ 967,477: × 0.5279 = 510,731.0, remainder 31.0 → +0.0032 → 52.79%. 683,124 ÷ 934,728: × 0.7308 = 683,099.2, remainder 24.8 → +0.0027 → 73.08%. Equals `Step_0.md` |
| ES-021 | APPLIED | `Step_3.md` picks rows | Section L223–L231 → **L254–L261** (heading `##### Esperanza` L254, picks L255–L261); every pick's citation +31 (Auroville L256, SOS L257, Boys Town L258, Sardinia L260, Kibbutz L261); L224 row (withheld) → the Basque baserri pick copied from L255 with its leading annotation omitted and marked as omitted; L228 row (excluded as "later-era") → Pestalozzi Children's Village copied as written from **L259** | Each picks line compared word for word with the live line. Annotation omitted because it states the pick's tier-token history and "the only one in the file" (a cross-city remark) |
| ES-022 | APPLIED | `Step_1_and_2.md` row 38; `Phase_4.md` row 3; `Phase_7.md` row 1 | Half B row citation → **L260** (Step_1_and_2: "L247, L260 (header L247, row L260)"); Half B row marked as the first-pass split, superseded by the city's own determination; new row for **§11** (L1332–L1457): baseline 555,826 (39.7%) · mandated 359,037 (25.6%) · FREE 485,756 (34.7%) · distinctive 844,793 (60.3%); mandate HALF education 12.5% (105,599) + FULL agricultural 15% (126,719) + HALF maritime/harbor 10% (84,479) + HALF other/administrative 5% (42,240, the birth registry); counts on the pre-`DR-68` workforce; SH-014 clause added to both rows | By hand: 555,826 + 359,037 + 485,756 = 1,400,619 ✓; 359,037 + 485,756 = 844,793 ✓; 105,599 + 126,719 + 84,479 + 42,240 = 359,037 ✓; shares 555,826 ÷ 1,400,619 = 39.68%, 359,037 ÷ 1,400,619 = 25.63%, 485,756 ÷ 1,400,619 = 34.68%, 844,793 ÷ 1,400,619 = 60.32% ✓ (rounded to the file's figures); 1,400,619 = 922,950 + 0.5 × 955,337 = 922,950 + 477,668.5 = 1,400,618.5 ✓ (the pre-`DR-68` Census I); current workforce 934,728 + 0.5 × 967,477 = 934,728 + 483,738.5 = 1,418,466.5 (Half B 1,418,466; `09` 1,418,467). `16` L260, L1332–L1457 (L1458 is `## 12.`) re-read. ⚑ See New findings 1 |
| ES-023 | APPLIED | `Phase_5.md` | Airports L41, L48 → L44, L51; Ports L513, L710, L729 → L536, L733, L752; RelDB entry "L208–L218" → **L219–L229**, entry lines L209–L215 → **L220–L226**; NatConn "9 line(s)" list (both cells) → L75, L183, L185, L189, L208–209, **L412, L444, L464** | Live RelDB map: L219 heading, L220 Real station, L221 Region, L222 Status (still excluded as later-era), L223 Arcanet subnet, L224 Highways (compares), L225 Direct highway neighbors, L226 Notes; the row texts are unchanged, only the numbers moved (+11). Ports L536 is the Hope Bay row (same text) |
| ES-024 | APPLIED | `Phase_7.md` · `16` "other lines" row | 23 lines → **24 lines** (the 23 re-pointed lines + the §11 heading L1332), both the value and the citation cell | list count by hand: 4 + 1 + 5 + 4 + 4 + 3 + 3 = 24 ✓ |
| ES-025 | PARTIAL | `Step_0.md`, `Step_1_and_2.md` | New row in each: "Extent table — the city's own row": Esperanza · Palmer · Census I cell 1,878,287 · @10k 188 · @7k 268 · Site: Hope Bay — `Extent_and_Density_Per_City.md` L606 *(2026-09-05 snapshot; the census is live — note L631)*. **Left out:** the open question (Extent L460–470, L464, Ports L513) and the Site cell's "⚠ James Ross I. reserved for it — §8" annotation, because both depend on ES-003 (`DECIDE`) — the row says the annotation is held | L606 read live: `\| Esperanza \| Palmer \| 1,878,287 \| 188 \| 268 \| Hope Bay ⚠ *James Ross I. reserved for it — §8* \|`; L631 is the snapshot note (confirmed) |
| ES-026 | untouched (`DECIDE`) | — | "N-line file" counts left (incl. `Step_10.md` "430 lines") | — |
| ES-027 | APPLIED | `Step_0.md` Census I and II rows | status cells now also carry the `DR-68` scenario note: Census I "+12,140 H / +11,778 R, was 955,337 / 922,950 / 1,878,287 — arithmetic, not a migration"; Census II "+8,108 H / +7,739 R, was 502,654 / 675,385 / 1,178,039 — arithmetic, not a migration" | Census L483 / L605 read live. By hand: 955,337 + 12,140 = 967,477 ✓; 922,950 + 11,778 = 934,728 ✓; 955,337 + 922,950 = 1,878,287 ✓; 502,654 + 8,108 = 510,762 ✓; 675,385 + 7,739 = 683,124 ✓; 502,654 + 675,385 = 1,178,039 ✓. (The source cell also names the Santa Luce redistribution; the clause was left out to keep the row single-city.) |
| ES-028 | APPLIED | `Phase_8.md` term-check row | "craft — 2 hit(s)" → "craft — 2 hit(s): spec L138 (“Belgrano-crafted goods”, with the whalebone-and-metal pianos as the example) and spec L151 (“whalebone-and-metal pianos, crafted in Belgrano”)" | `grep -n -i craft` on the spec: exactly L138 and L151. (The ledger's one phrase fits L151 exactly and L138 only as its example, so both are quoted separately.) |
| ES-029 | APPLIED | `Phase_7.md` header and last row | header "13 of 13" → **8 of 13**; last row "exist on disk: 11 of 11" → "named in this sheet: 8 of 13 … All 13 exist on disk (checked 2026-10-30)" | All 13 spine addresses tested with `-e`: all exist (so "11 of 11 on disk" had been wrong too). The ledger entry names this row, so §4a's "leave a meta row" lesson did not apply |
| SH-001 | APPLIED | Pre-Trip §G | spine `L127` → **L220, L1114, L1140** | L220 "and the no-invented-person-names rule"; L1114 "NO INVENTED PERSON NAMES — role placeholders permanently"; L1140 "People as role-archetypes — binding rule: no invented proper names" (live L127 is a table row). Datasheets: the only "L127" is `Factions` (`City_Origin_Factions_PostWar_Refugee.md` L127), a different file — left |
| SH-002 | APPLIED | Pre-Trip §G | runbook `L2178` → **L2180** | L2180 `### ⭐ THE DIVERGENCE OPERATOR — …` |
| SH-003 | APPLIED | Pre-Trip §C Step 5 `T8` | `02_…` §5.3 "lines 610–684" → **610–636** | `02` L610 `## 5.3`, L637 `# 6. Symbol binding` |
| SH-004 | APPLIED | Pre-Trip §C procedure items 4, 5 | item 4 "620–643 and 701–703" → **620–643 and 682–684**; item 5 "650–703" → **667–684** | Trial recipe L620 `### ROUND 3` … L643 closing fence (still the Round 3 prompt); L682–684 "Round 3's prompt now carries a fifth section"; L667 "AMENDED 2026-09-28 — THE WRITTEN CONTENT IS A MERGE, NOT A PICK" through L684 |
| SH-005 | APPLIED | Pre-Trip §C Step 10 (three places) | "3057–3172" (twice) → **3057–3152**; card note "live lines 3045–3161 govern" → "3057–3152" | Runbook L3057 `# Step 10`, L3071 §10.1, L3117 §10.2, L3131 §10.3, L3153 `# Where everything lives` |
| SH-006 | ALREADY-RIGHT | `Step_-1.md` | the "Specs `Status:` field" row cites `00_RUNBOOK.md` with **no line number** (and no `1821` anywhere in the Pre-Trip or sheets) | grep for `1821` in all files: no hit |
| SH-007 | HELD | — | no "line 65" / `Resettled` coordinate in any Esperanza file (Pre-Trip, `Step_10.md`) — nothing to change; the shared decision is not touched | grep |
| SH-008 | APPLIED | 11 sheets | headers recounted by hand and re-dated "recounted by hand 2026-10-30": Step_0 3 of 3 · Step_1_and_2 6 of 6 · Phase_2 3 of 3 (split 1 / 2) · **Phase_3 3 of 4** · **Phase_4 6 of 7** · Phase_5 6 of 6 · Phase_6 5 of 5 · **Phase_7 8 of 13** · Phase_8 2 of 2 · Phase_9 4 of 4 · Phase_10 3 of 3 (split 2 / 1) | See §2 |
| SH-009 | HELD | — | "N-line file" counts left | — |
| SH-010 | APPLIED | Pre-Trip §D Phase 2 table (2 rows); `Phase_2.md` (2 rows) | added the city's own section (`### Esperanza`, **L178–L186**) and the solar-UTC rule (heading **L21**, list **L26–L33**, rule 1 **L28**, refinement box **L35–L63**), "registered, not dispatched" (the spine's Phase 2 block does not name the file, so N stays 3) | Composition file: L178 heading, L180–L184 tier table, L186 founding note, L188 `---`, L190 `### Marambio`; L26 "Recording it so it stops …", L28 rule 1, L33 end of rule 4, L35 `> ## ⛔⛔ AND THE REFINEMENT …`, L63 last line of the box. Form copied from the other pass sheets for form only |
| SH-011 | APPLIED | Pre-Trip §C Step 0 (Extent line) and §E; `Step_0.md` and `Step_1_and_2.md` extent rows | "(2026-09-05 snapshot; the census is live — note L631)" added beside the Extent citations (row 606 in the Step 0 reads; the L409/460/464/512 list in §E; both new sheet rows) | Extent L631 begins "26,880,794 people needing 2,688–3,840 km² …" and carries "Snapshot note, 2026-10-28 … the table above records the 2026-09-05 populations … the census is the live source" |
| SH-012 | APPLIED | Pre-Trip, `Phase_5.md`, `Phase_7.md` | the stale line numbers into `16`, `09`, Airports, Ports, RelDB, NatConn — as ES-001 / 023 / 024 | Unchanged and re-read live: Highways, CrossSub, `11`, Register, NMCI, Extent lines, Topics, Precip, Sweep L121/171/189/193, Factions lines, Polydimensional Animism L18/L172/L218, the universe `Locations/README.md` L21, spec L155/L160 headings |
| SH-013 | APPLIED | Pre-Trip §D Phase 1 `16` row and §E; the three sheets above | the city's §11 (upper-case "ESPERANZA") quoted beside Half B in `Step_1_and_2`, `Phase_4`, `Phase_7`, with the supersession stated; L1332 listed, marked "the city's own upper-case heading" | `16` L1332 `## 11. ✅ ESPERANZA — DETERMINED`. The ledger lists SH-013 for this city, so the shares were quoted (§4a branch not needed). ⚑ New findings 1 |
| SH-014 | APPLIED | `Step_1_and_2.md` (Half B row, §11 row); `Phase_4.md` (same two); `Phase_7.md` (same two) | clause "on the flat ABCC working value; counts re-run when per-city ABCC values are set (`16` L1287–L1304)" | Live: L1287 `### ⚠ CONSEQUENCE — the ten determinations so far need a baseline re-run` … L1304 "rather than some being converted early." (L1305 blank, L1306 next heading) — so **L1287–L1304**, not L1305. `Phase_4.md`'s `09` and `11` rows were not given the clause (they quote `09`/`11` figures, not `16`'s) |

**Not applied on purpose (outside the sweep):** SH-015 … SH-017, SH-019 (Tier U, orchestrator); SH-018, SH-020 … SH-022 (Tier U sheets); ES-S01 … ES-S08.

---

## 2 · MUST-OPEN recount (SH-008), by hand

Convention used: an address is counted when a row **cites it by file/path name or transcribes it**; for a directory address, a row naming the city's file *inside* it counts (⚑ marked); an address whose content reaches the sheet only through a cited Tier U sheet counts as "via Tier U" if that Tier U sheet is cited by a row of this sheet and was extracted from the address. The spine's `📂 MUST OPEN` block is the list; N matches each sheet's own N (a bullet naming several files counts once; each file named was still checked).

### Step_0.md — Phase 0 · N = 3 (spine L281–286) → **3 of 3** (2 direct, 1 via Tier U) — header numbers unchanged, date changed
| Address | Covering row |
|---|---|
| `Repo_Scope.md` | row "**U** `Repo_Scope.md`" (direct) |
| `Timeline Eras/` | rows "Temporal frame", "Act structure", "consolidating mechanism" cite `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` (source = `Timeline Eras/2 The Second Interwar Period/README.md`) — via Tier U ⚑ (the folder is not named; only that era's README is extracted) |
| `Official_Population_Census.md` | rows Census I, Census II (direct) |

### Step_1_and_2.md — Phase 1 · N = 6 (spine L329–340) → **6 of 6** (6 direct)
| Address | Covering row |
|---|---|
| `Worldspace/Locations/` (universe) | "Universe repo `Worldspace/Locations/` — directory enumerated" |
| `Specs/` | the many `Specs/Esperanza.md` rows ⚑ (file inside) |
| `Energy_Grid_Failure_Rationale.md` | its row |
| `READER/` | rows "READER — …" citing `READER/Esperanza.md` ⚑ (file inside) |
| `Stations/` | rows `Antarctic_Stations_With_Airstrips.md` and `COMNAP_Antarctic_Station_Catalogue.pdf` ⚑ (files inside) |
| `16_Per_City_Three_Tier_Run.md` | the Half B row and the new §11 row |

### Phase_2.md — Phase 2 · N = 3 (spine L408–413) → **3 of 3** (1 direct, 2 via Tier U; was "3 directly")
| Address | Covering row |
|---|---|
| `No_National_Stereotypes.md` | "GPS law — the operative distinction" → `No_National_Stereotypes_Quick_Reference.md` (via Tier U) |
| `Falkland_Treaty/` | three "Falkland Treaty — …" rows → `Falkland_Treaty_Quick_Reference.md` (via Tier U) |
| `Official_Population_Census.md` | rows "Composition tier table (census Section A entry)", annotation, Census I, Census II (direct) |
(The composition file added by SH-010 is not in the spine's block, so it is not counted.)

### Phase_3.md — Phase 3 · N = 4 applicable (5 listed; `Davis_Geosciences_Research/` "where applicable", not applicable) (spine L479–488) → **3 of 4** (3 direct)
| Address | Covering row |
|---|---|
| Climate `READER/` | **not covered** — no row of `Phase_3.md` names it (its rows are in `Step_1_and_2.md`) |
| `Specs/` | "Spec — `## Geographic Basis`", "`## Character & Culture`", "`## Notable Locations`" (`Specs/Esperanza.md`) ⚑ |
| `City_Concept-Art/` | "Concept-art directory status" (`City_Concept-Art/Palmer_Subnet/Esperanza`) |
| `City_Megasheets/` (physical infrastructure attributes, withheld) | "Megasheet Physical Infrastructure file" (cites `Esperanza_Physical_Infrastructure_Attributes.md`; the folder itself is not named) ⚑ |

### Phase_4.md — Phase 4 · N = 7 (spine L541–554) → **6 of 7** (4 direct, 2 via Tier U; was 7 of 7)
| Address | Covering row |
|---|---|
| `Robot_Physiology_and_Cultural_Practices.md` | "Robot Physiology — appearance/clothing baseline (Tier U)" and "Siligel / coolant / smoking …" → `Robot_Physiology_Quick_Reference.md` (via Tier U) |
| `Robot_Cold_Physiology.md` | "Robot Cold Physiology — the governing mechanic (Tier U)" → same Tier U sheet, whose source list names this file (via Tier U) |
| `16_Per_City_Three_Tier_Run.md` | Half B row, §11 row |
| `09_Per_City_Baseline_Run.md` | its row |
| `11_Caloric_Rebuild_and_Livestock_Tier.md` | its row |
| `National_Medical_and_Care_Institutes.md` | 13 rows (L29 … L209) |
| `National_Economy_and_Currency.md` | **not covered** (no row; `grep -i economy` in the sheet finds nothing) |

### Phase_5.md — Phase 5 · N = 6 bullets (spine L623–634) → **6 of 6** (6 direct)
| Address | Covering row |
|---|---|
| `Worldspace/Locations/` (universe) | "Universe repo `Worldspace/Locations/` — directory enumerated" |
| `Highways.md` | four rows |
| `Airports.md` · `Ports.md` · `Geothermal_Heating.md` (one bullet, three files) | rows for each of the three |
| `City_Cross_Subnet_Relationships.md` | its row |
| `City_Relationship_Database.md` | entry rows |
| `City_National_Connections.md` | its row |
(`Arcanet.md`, from the runbook's L1977 row, also has a row; it is not in the spine block.)

### Phase_6.md — Phase 6 · N = 5 (spine L760–768; the mortuary question is reserved, not an address) → **5 of 5** (5 direct)
`Factions/Robot_Religions/` (directory row + three Polydimensional Animism rows) · `National_Holidays.md` · `Ice-Cold_Buddhism_Research/` · `The_True_Believer_Extraction.md` · `The_Meme_Machine_Extraction.md` — each has its own row.

### Phase_7.md — Phase 7 · N = 13 (spine L849–874) → **8 of 13** (7 direct, 1 via Tier U; was 13 of 13)
| Address | Covering row |
|---|---|
| `Division_of_Industry/` | via Tier U: the box and "Three things" cite `Division_of_Industry_Reliability_Quick_Reference.md` (extracted from the folder's README and `10_Validation_…`); the one table row naming the folder README says only `README.md` L49 (a shared base name, not counted) ⚑ |
| `16_Per_City_Three_Tier_Run.md` | Half B row, §11 row, "other lines" row |
| `Division_of_Industry_Sweep_2026-08-31.md` | four rows |
| `01_Burden_Scoring_Model.md` | "status stamp in the folder README" row (names the file) |
| `08_Volume_Based_Requirement_Reference.md` | **not covered** |
| `National_Medical_and_Care_Institutes.md` | **not covered in this sheet** (its 13 rows are in `Phase_4.md`) |
| `Theoretical-Calculations/` | its row |
| `Industry_Staffing_and_Productivity/` | **not covered** |
| `jobs_professions_and_fields/` | its row |
| `National_Economy_and_Currency.md` | **not covered** |
| `City_Logistics.md` | its row |
| `Factions/` | its row |
| `Megacorps/` (universe repo) | **not covered** (the Tier U sheet `Phase_7_Roster_and_Model_Files_Quick_Reference.md` holds it, but this sheet does not cite that sheet) |

### Phase_8.md — Phase 8 · N = 2 (spine L962–965) → **2 of 2** (2 direct)
`Robot_Biology_and_Culture/` — row "`Robot_Biology_and_Culture/` mandatory facts (Tier U, cross-ref `Phase_4.md`)" ⚑ (directory named in the row; content cited through `Robot_Physiology_Quick_Reference.md`) · `Weapons_and_Tools_Philosophy.md` — its row.

### Phase_9.md — Phase 9 · N = 4 (spine L1033–1040) → **4 of 4** (3 direct, 1 via Tier U) — numbers unchanged
| Address | Covering row |
|---|---|
| `Laws_of_Robotics.md` | row "Laws of Robotics (Tier U)" transcribes the two laws ⚑ (the file name is not written; the cited Tier U sheet does not contain them; wording differs slightly — New findings 2) |
| `Robot_Universals/` | its directory row and the Ch. 13 / Ch. 14 rows |
| `Doll_Representation_Categories.md` | its row |
| human-robot baseline (`Robot_Physiology_and_Cultural_Practices.md`) | via Tier U: the sheet cites `Robot_Physiology_Quick_Reference.md` (3 rows), which holds "Human-robot relations — the baseline" (its L81); no row cites the baseline itself ⚑ |

### Phase_10.md — Phase 10 · N = 3 (spine L1108–1113; the no-invented-names rule is not an address) → **3 of 3** (2 direct, 1 via Tier U; was "3 directly")
`Worldspace/Characters/` (timeline repo) — "Characters canon" row (direct) · `Enneagram_Character_Index.md` — its row (direct) · `Zodiac_Signs_Full_Attributes.md` — row "Zodiac Lens — all 12 signs' full attributes (Tier U)" → `Zodiac_Signs_Quick_Reference.md`, whose source is that file (via Tier U).

---

## 3 · New findings (not in the ledger; nothing fixed unless inside an entry)

1. **`16` §11 does not itself say it supersedes Half B.** Its table (25.6 / 34.7) and heading ("DETERMINED") are the later, city-specific figures; the word "supersedes" appears in the ledger's SH-013 and in the brief, not in Esperanza's own §11 text. The sheets now say "the city's own determination supersedes its MAND% / FREE%" as the brief directs. Worth a one-line confirmation by the developer (or a line in §11) so the claim has a source line. Also: §11 L1361–1363 quotes the NMCI sentence "about 2% of a 1.88 M city" (the old Census I) — source-level, same family as ES-S07.
2. **`Phase_9.md` "Laws of Robotics" row** — the text differs from `Laws_of_Robotics.md` L3–4 ("will have full capacity …" vs source "will have the full capacity …"; law 2 is reworded: "is realistically possible for others to do to her" vs source "it is also realistically possible for others to do to her"), and the citation points at `Robot_Physiology_Quick_Reference.md`, which does not contain the laws. Not fixed (not in an entry).
3. **Rows missing for must-open addresses** (gaps for the developer, not filled): `Phase_3.md` — Climate `READER/`; `Phase_4.md` — `National_Economy_and_Currency.md`; `Phase_7.md` — `08_Volume_Based_Requirement_Reference.md`, `National_Medical_and_Care_Institutes.md` (in `Phase_4.md` only), `Industry_Staffing_and_Productivity/`, `National_Economy_and_Currency.md`, `Megacorps/`.
4. **Pre-Trip §I** still reads "DATASHEET-NOT-YET-BUILT(N-5)=20", "RESOLVE=121", "108 claims · 108 OK" and "60 numbers moved" — left as the dated build record per ES-002; those counts are no longer the state of the file (the §C intro and §J row are now corrected). The Pre-Trip's "Re-run note" and §K text are unchanged.
5. **Pre-Trip §J "Founding Register not in the Phase 2 table"** (L526 before the edits; L528 now) is still true for the Pre-Trip table, while `Phase_2.md` has the Register row; also §J's other "Raised 2026-09-30/10-21" items are unchanged.
6. **`Phase_10.md`** names only the timeline-repo tree (3 files); the GDD tree's 13 files (ES-006) were added to the Pre-Trip only, as the ledger says.
7. **`Phase_4.md` NMCI L176 row** copies "§15 education sector of ~25% is **350,155 workers**" — the stale whole-workforce basis (ES-S07, `DECIDE`); left. (The row copies only the first source line; the "1.88 M city" wording is on NMCI L174.)
8. **`Phase_7.md` last row** said "exist on disk: 11 of 11"; the spine block lists 13 and all 13 exist — corrected under ES-029.
9. **Spec L138** (not edited) points to another city's read-last culture file (`Local_Cultures/Halley_Subnet/Belgrano.md`); the Phase 8 row now quotes only L138's trade phrase and does not copy the pointer. Same as ES-S06.
10. **Judgment calls (⚑)** in §2: directory addresses counted by a named file inside (Specs/, READER/, Stations/); `Timeline Eras/` via the Second-Interwar sheet; `City_Megasheets/` via the named file; `Division_of_Industry/` via the Tier U reliability sheet; the Laws of Robotics transcription; the Phase 8 `Robot_Biology_and_Culture/` row; the Phase 9 baseline.

## NEEDS-DEVELOPER
- **ES-025 (open-question half):** whether the sheets say that Esperanza has no declared extent (Extent L460–470, L464, Ports L513) and whether the extent row keeps the Site cell's "⚠ James Ross I. reserved for it — §8" annotation. Held with ES-003. (The extent rows are in `Step_0.md` and `Step_1_and_2.md` without the annotation, and say so.)

(The three `DECIDE` entries ES-003, ES-005 and ES-026, and the `SOURCE` / `NOTE` entries ES-S01 … ES-S08, are the developer's walk-through list and were not touched.)

---

## 4 · Files edited (all with the Edit tool; nothing created in the pass folder)

Pass folder `…/Cities/City_Development_Passes/Palmer_Subnet/Esperanza/`:
- `00.0_Pre-Trip_Inspection.md`
- `README.md`
- `Datasheets/Step_0.md`
- `Datasheets/Step_1_and_2.md`
- `Datasheets/Step_3.md`
- `Datasheets/Phase_2.md`
- `Datasheets/Phase_3.md`
- `Datasheets/Phase_4.md`
- `Datasheets/Phase_5.md`
- `Datasheets/Phase_6.md`
- `Datasheets/Phase_7.md`
- `Datasheets/Phase_8.md`
- `Datasheets/Phase_9.md`
- `Datasheets/Phase_10.md`

Not edited: `00.2_Position_Coverage_Ledger.md`, `Datasheets/Step_-1.md`, `Step_5.md` … `Step_10.md` (no applicable old text), every other file. This report is the only file created.
