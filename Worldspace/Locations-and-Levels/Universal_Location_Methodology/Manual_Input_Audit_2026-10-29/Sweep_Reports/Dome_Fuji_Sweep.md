# Dome Fuji — sweep report (2026-10-30)

**City:** Dome Fuji (ledger section B22; pass folder `City_Development_Passes/Mawson_Subnet/Dome_Fuji`). Robot-only; no Census II row; official name pending ("The Temple" informal) — the name was kept everywhere, no name sweep.
**Who:** sub-agent (Sonnet 5.5) under the orchestrator, following `SWEEP_BRIEF.md` (including §4a).
**Read in full before editing:** `SWEEP_BRIEF.md`; `FIX_LEDGER.md` section A (top) and `### B22 · DOME FUJI`; `Dome_Fuji_Audit.md`; the city's whole `00.0_Pre-Trip_Inspection.md` (566 lines before, 565 after); all 19 datasheets; the pass `README.md` and `00.2_Position_Coverage_Ledger.md` (no entry names them; not edited). Live source lines opened for every changed value (list in the table's Check column). Withheld / read-last files were not opened. `graphify` was not run (brief §5).
**Method:** Edit tool only; anchors by text, not line number; every new number copied from the live source line; lists regenerated from a case-insensitive `grep -n -i -E "dome[ _-]?fuji"` and then compared by a read-only Python check against what the Pre-Trip now says (all seven lists plus the census and `16` lists compare equal to live).

**Counts.** APPLIED 20 (10 `DF-` entries + 10 shared fixes) · HELD 5 · ALREADY-RIGHT 1 · NEEDS-DEVELOPER 1 · SKIPPED-MISMATCH 0 (one off-by-one range in the ledger was corrected to the live number and flagged ⚑; see DF-004).

---

## 1 · Results table

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| DF-001 | APPLIED | Pre-Trip §C Step 0 (census) | Census "other lines": L530, L552, L588, L642 → **L530, L548, L552, L589, L642, L644** | live grep: census lines 354, 356, 518, 530, 548, 552, 589, 642, 644. L548 (the `DR-69` rebuild note, "Kunlun and Dome Fuji have no humans") and L644 (the `DR-68` scenario note, "Kunlun, Dome Fuji, Byrd and Vostok still have no Census II rows") opened; both are about the city. L354/356 (Section A heading and entry) and L518 are cited elsewhere in the row |
| DF-001 | APPLIED | Pre-Trip §C Step 2 (`16` line) | "Dome Fuji's row, line 282" → **283** | opened `16` L283: `\| Dome Fuji \| Mawson \| 2.50 \| 66,849 \| 27.3% \| 14.5% \| 58.1% \| H \|`; header L241 (HALF B heading) and L247–248 (column header and separator) still land |
| DF-001 | APPLIED | Pre-Trip §D Phase 1 `16` row | row L282 → **L283**; other lines (18) → **20, incl. L3186**: L114, L116, L138, L174, L222, L336, L353, L442, L795, L2315, **L3186**, L3212, L3229, L3233, L3257–3258, L3340, L3347, L3484, L3575. §32 heading marked "the city's own upper-case heading" | live grep: 21 hits = {row 283} + these 20 lines (count: 5+5+1+3+2+2+1+1 = 20). Odd hits opened: L3257–3258 (the "Stale-canon flag" bullet naming `Specs/Dome_Fuji.md`), L3340 and L3347 (Mawson-subnet closing lines), L3484, L3575 — all name the city |
| DF-001 | APPLIED | Pre-Trip §D Phase 4 `09` row | L90, L109, L212, L219, L223 → **L90, L111, L214, L221, L225** | live grep of `09`: 90, 111, 214, 221, 225. (`11` L335, L339 unchanged, re-confirmed) |
| DF-001 | APPLIED | Pre-Trip §D Phase 5 Highways | …L170, L281 → **…L170, L296** | live: 156, 161, 163, 170, 296; L296 reads `\| Interior (between Dome Fuji and Kunlun) \| Hwy 22, Hwy 37 \| Bidirectional dual-junction \|` |
| DF-001 | APPLIED | Pre-Trip §D Phase 5 Airports | L18, L47, L52, L60, L63 → **L18, L50, L55, L63, L66** | live: 18, 50, 55, 63, 66 (each old line +3). L63 = "Dome Fuji · Mawson · Temirötkel…", L66 = "⚠ Bears on Dome Fuji, a continent-wide pilgrimage site…" |
| DF-001 | APPLIED | Pre-Trip §D Phase 5 Ports | L182, L205, L459, L717 → **L182, L205, L482, L740** | live: 182, 205, 482 ("Deep interior / plateau" list), 740 (LANDLOCKED row) |
| DF-001 | APPLIED | Pre-Trip §D Phase 5 City_Cross_Subnet_Relationships | …L118, L120 → **…L118, L120, L121** | live: 47, 75, 78, 97, 113, 114, 118, 120, 121. L121 names `Specs/Dome_Fuji.md` inside the "three-subnet logistics triangle" paragraph (odd hit; it is the city's own spec file name) |
| DF-001 | APPLIED | Pre-Trip §D Phase 5 City_Relationship_Database | L26, L48, L124, L186–187, L192–193, L226, L272–273, L449, L472–473, L501, L520 → **L26, L48, L135, L197–198, L203–204, L237, L283–284, L460, L483–484, L512, L531** | live grep matches; odd hits opened (L135, L237, L283–284, L460, L483–484, L512, L531): all name the city (neighbor entries and general notes that mention it) |
| DF-001 | APPLIED | Pre-Trip §D Phase 5 City_National_Connections | 23 lines, L311… → **L95, L99–100, L137, L312, L318–319, L342, L369, L371, L492–493, L503–504, L506, L508, L511–512, L516, L518, L523, L530, L598** | live grep: 23 lines; count by hand 1+2+1+1+2+1+1+1+2+2+1+1+2+1+1+1+1+1 = 23. Odd hits (L137, L369, L371, L523, L530, L598) opened |
| DF-001 | APPLIED | Pre-Trip §E (rule/canon files naming the city) | `16`: L282 and 18 lines → **L283 and 19 lines + L3186 (upper-case heading)**; added `Precipitation_Falls_vs_Lands.md` **L118** (absolute path) | `Precipitation_Falls_vs_Lands.md` L118 = `\| Dome_Fuji \| 25 \| **22** \| 2 \|` (the city's row). Extent L249, L578, L588; NMCI L231; Topics L330–331 unchanged |
| DF-002 | APPLIED | Pre-Trip §C intro box; §J | "(**not yet built** — November item N-5; the addresses below are where the files will be created)" → "(19 files, all present)"; §J row "Datasheets not yet built for this city" **deleted**; §I left as the dated build record (as the ledger says) | `ls Datasheets/` = 19 files |
| DF-003 | HELD | — | not touched (ledger status DECIDE: whether spec L3–27 / `15` Resolution 3 become named inputs) | — |
| DF-004 | APPLIED ⚑ | Pre-Trip §D Phase 6 Holidays row | "Names Dome Fuji at L100" → **"L100–107 (entry `### Deepest Cold (Dome Fuji)`: heading L100, text L102–107); L103 names a Background-Lore vignette path — a vignette is not canon and never an input (not opened, not copied)"** | ⚑ **The ledger says L100–106; live the entry ends at L107** ("within the faith." is L107; `grep -n`: L100 heading, L103 the path, L104 "precise coldest point…", L106 "…doctrinal dispute", L107 "within the faith."). Applied with the live number, per the REPOINT rule; the ledger text for DF-004/DF-026 should read L100–107 |
| DF-005 | APPLIED | Pre-Trip §D Phase 10 "Characters" row (carve-out cell) | appended: timeline repo tree 587 `.md` files, 0 name the city; GDD `Worldspace/Characters/` tree 1 file names it — `Dolls/Still-Present_-_In-Game/unsure and_or special cases/Calethina/Personal_Background/Player_Chamber_Origin_Chain_DRAFT.md` (hit at L75; the file's own header: working draft, not developer-confirmed) | re-run 2026-10-30: `grep -ril` over the timeline tree → 0 (`find … -name "*.md"` = 587); over the GDD tree → exactly that one file; L75 and the header (L3 "Status: working draft, not developer-confirmed") opened |
| DF-006 | HELD | — | not touched (DECIDE: alias set) | — |
| DF-007 | APPLIED | umbrella | see SH rows below | — |
| DF-020 | APPLIED | `Step_3.md` picks rows | section "L134–L138" / cites L134, L135, L136, L137 → **"L165–L168 (heading L165, picks L166–L168)" / L165, L166, L167, L168** | `Inspirational-Influences.md` live: L165 `##### Dome Fuji`, L166 Paro Taktsang [PRIMARY], L167 Potala Palace [SECONDARY], L168 Angkor Wat [SECONDARY]; the three pick lines are word-for-word the sheet's |
| DF-021 | APPLIED | `Step_1_and_2.md` Half B row; `Phase_4.md` row 3; `Phase_7.md` row 1 | `16` row L282 → **L283** (Step_1_and_2: "L247, L283 (header L247, row L283)"); **§32 row added** in each: Baseline 15,046 (27.3%) · Mandated 8,005 (14.5%) · FREE 32,021 (58.1%); counts sum 15,046 + 8,005 + 32,021 = 55,072 (the Census I figure before the 2026-10-28 scenario `DR-68`; Census I now 66,849 = 55,072 + 11,777); shares equal Half B | `16` L3186 heading, L3188–3192 table read live; `16` L1 header text quoted ("The per-city determinations further down and the national food balance in files 04 and 13 were NOT recomputed"); Census L518 "+0 H / +11,777 R (was 0 / 55,072 / 55,072)" |
| DF-021 | APPLIED | `Phase_7.md` row 2 (`16` other lines) | 18 lines → **20 lines** incl. L3186 (list as in the Pre-Trip) | as above |
| DF-022 | APPLIED | `Phase_5.md` | Highways L281 → **L296**; Airports L47/L52/L60/L63 → **L50/L55/L63/L66**; Ports L459/L717 → **L482/L740**; RelDB entry "L186–L196" → **"L197–L207"** (citation L186 → L197), entry lines L187–L193 → **L198–L204** (all seven re-read: values word-for-word the live lines; L201 is the later-era Status line, still "not copied"); CrossSub "8 line(s)" → **"9 line(s)"** (+L121); NatConn "23 line(s)" re-listed per DF-001 | Airports/Highways values compared by script; RelDB L198–L204 compared character-for-character with the sheet rows (L201 intentionally excluded) |
| DF-023 | APPLIED | `Step_1_and_2.md` rows "climate type" (L123), "prevailing winds" (L127), "polar night" (L141) | removed "nearly identical to Concordia and Ariun Nuur"; "same pattern as Concordia and Ariun Nuur"; "shorter than Ariun Nuur and Concordia due to slightly lower latitude" — each replaced by the bracket *[the source's comparison clause with other places is not copied]* (the form the sheet already uses for L124) | spec L123, L127, L141 re-read. Judgment: at L141 I dropped "due to slightly lower latitude" with the peer clause because "slightly lower" is itself the comparison |
| DF-024 | APPLIED | `Step_0.md` and `Step_1_and_2.md` | added 4 extent rows each: Extent file **L628** "Dome Fuji · Mawson · Census I 55,072 · @10k 6 · @7k 8 · Site **Dome F**" labelled "**2026-09-05 snapshot; the census is live — note L631**"; and L249, L578, L588 as "multi-city list, line number only" | live: L601 heading "THE TABLE — required area at the band, all 25", L603 header `\| City \| Subnet \| Census I \| @10k \| @7k \| Site \|`, L628 row, L631 snapshot note ("the table above records the 2026-09-05 populations… The table was left as the dated record; the census is the live source") |
| DF-025 | HELD | — | "N-line file" counts left as they are (DECIDE; SH-009 held) | — |
| DF-026 | APPLIED ⚑ | `Phase_6.md` Holidays row | value "### Deepest Cold (Dome Fuji)" / cite L100 → heading **plus the entry's text L102–L107 copied as written, with the L103 vignette path replaced by a bracket note ("not canon and never an input; not copied")** / cite **L100–L107** | ⚑ same off-by-one as DF-004 (ledger L100–106; live entry to L107). Copy checked by script against the live lines (equal once the path is replaced) |
| DF-S01…S05 | NOT TOUCHED | spec / `15` | source items (DECIDE / NOTE) | — |
| SH-001 | APPLIED | Pre-Trip §G "No invented person names" | spine `L127` → **L220, L1114, L1140** | spine L220 "…and the no-invented-person-names rule", L1114 "NO INVENTED PERSON NAMES — role placeholders permanently", L1140 "People as role-archetypes — binding rule: no invented proper names"; the runbook L1982 half of the row re-read and still lands. The only other "L127" in the city's files is spec L127 (a different file) |
| SH-002 | APPLIED | Pre-Trip §G "Divergence operator" | runbook `L2178` → **L2180** | L2180 = "### ⭐ THE DIVERGENCE OPERATOR — the developer's own inputs…" |
| SH-003 | APPLIED | Pre-Trip §C Step 5 `T8` | `02` §5.3 "lines 610–684" → **610–636** | L610 "## 5.3 The both-are-true test"; L637 "# 6. Symbol binding" |
| SH-004 | APPLIED | Pre-Trip §C procedure items 4 and 5 | item 4 "lines 620–643 and 701–703" → **"620–643 and 682–684"**; item 5 "lines 650–703" → **"667–684"** | `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md`: L620 "### ROUND 3" … prompt ends L643 (still right); L667 "AMENDED 2026-09-28 — THE WRITTEN CONTENT IS A MERGE, NOT A PICK" … L684 "…on record for the merge."; L682–684 = "Round 3's prompt now carries a fifth section…" |
| SH-005 | APPLIED | Pre-Trip §C Step 10 (3 spots) | "lines 3057–3172" (twice) → **3057–3152**; card note "live lines 3045–3161 govern" → **"live lines 3057–3152 govern"** | runbook L3057 "# Step 10 — THE READINESS CHECK"; L3153 "# Where everything lives" |
| SH-006 | ALREADY-RIGHT | `Step_-1.md` "Specs `Status:` field" row; Pre-Trip | the row cites only `Specs/Dome_Fuji.md` L31 and names the runbook's "Second Interwar default" with **no line number**; no "1821/1822" anywhere in the city's files | grep; (live runbook L1854–1855 "And `Specs/` "Status:" fields are POST-WAR" noted for the record) |
| SH-007 | HELD | `Step_10.md` etc. | left alone per brief. `grep -n -i "line 65\|L65\|Resettled"` over the Pre-Trip and all 19 sheets returns nothing — this city's `Step_10.md` row for `06` reads "zero hits" and carries no `01` coordinate, so there is nothing here for the held decision to touch | grep |
| SH-008 | APPLIED | all 9 sheets with a MUST-OPEN header | recounted by hand; see §2. Results: Step_0 3/3 · Step_1_and_2 6/6 · Phase_2 3/3 (1 direct + 2 via) · Phase_3 **3/4** · Phase_4 **6/7** · Phase_5 **5/6** · Phase_6 5/5 · Phase_7 **8/13** · Phase_8 2/2 · Phase_9 **3/4** · Phase_10 3/3 (2 + 1). "checked 2026-10-23" → "recounted by hand 2026-10-30" | §2 |
| SH-009 | HELD | — | "N-line file" counts untouched | — |
| SH-010 | NEEDS-DEVELOPER | Pre-Trip §D Phase 2; `Phase_2.md` | **not added.** `Upper_Earth_Immigration_Composition.md` has **no Dome Fuji section**: `grep -n -i "fuji\|valkyrie\|dome f\|dome_f\|ice.cold\|pilgrim"` over the 1,299-line file returns nothing, and the Mawson subnet section (L479–530) has headings only for Mawson, Sinheung, Shirayuki and Temirötkel. The file is a human-exile composition and the city has 0 humans | decision wanted: add a row saying "no section in this file (robot-only city; composition lives in the census Section A entry and the spec)" plus the solar-UTC rule (L28, "round(longitude ÷ 15)"; the Founding Register row L56 gives Solar UTC +3), or leave the file out |
| SH-011 | APPLIED | Pre-Trip §C Step 0 reads; `Step_0.md`, `Step_1_and_2.md` | added "(2026-09-05 snapshot; the census is live — note L631)" beside Extent "Dome Fuji's row **628**" (Pre-Trip) and in the new extent rows (sheets) | L631 re-read: it is still the snapshot note. The label is on the table row (L628) and the table lines (L601–604) only; L249, L578, L588 are text lines outside the table, so they are not labelled |
| SH-012 | APPLIED | via DF-001 / DF-022 | — | — |
| SH-013 | APPLIED | Pre-Trip `16` lists (§D Phase 1, §E); `Step_1_and_2.md`, `Phase_4.md`, `Phase_7.md` | the ledger lists SH-013 for this city (§32 equals Half B), so the §32 shares were quoted beside Half B in all three sheets, with "supersedes Half B's first-pass split; here the shares are equal", and the §32 heading **L3186** was added to the Pre-Trip `16` lists, marked "the city's own upper-case heading" | `16` L3186–3192 |
| SH-014 | APPLIED ⚑ | `Step_1_and_2.md` (Half B row + §32 row), `Phase_4.md` (Half B row + §32 row), `Phase_7.md` (Half B row + §32 row) | clause added beside each quoted `16` baseline % / count: "*(on the flat ABCC working value; counts re-run when per-city ABCC values are set — `16` L1287–1304)*" | `16` L1287 "### ⚠ CONSEQUENCE — the ten determinations so far need a baseline re-run" … L1296–1304 "PER-CITY ABCC VALUES — PARKED… WORKING VALUE UNTIL THEN: ABCC stays at the flat 65 per 1,000 residents for ALL cities… rather than some being converted early." L1305 blank. ⚑ **Not applied to `Phase_4.md` row 1** (the `09` §2 row: Required 18,264 · % WF 27.3%): those are `09` columns, which `16` L28 and L30–32 declare superseded, not `16` baselines; the clause would claim a basis (the flat ABCC value) that I could not verify for `09`. See New findings |

---

## 2 · MUST-OPEN recount (SH-008), by hand

Rule used: an address counts only if a row of the sheet writes it out by full path / full file (or directory) name, or transcribes it **through a Tier U sheet the row cites** (that sheet's own source line names the address). Shared base names alone (`README.md`, `Dome_Fuji.md`) and mentions inside "not copied" lists do not count. ⚑ = judgment call (directory-qualified short form, or a file inside the address folder named without the folder). The list for each phase is the 📂 MUST OPEN block in `03_The_Phase_Spine.md` (L278, L326, L405, L476, L538, L620, L757, L846, L959, L1030, L1105). Header N confirmed equal to the list size in every sheet except Phase 3 (list has 5 addresses; the header's N=4 leaves out the Davis-only folder, which the spine marks "where applicable" — kept).

### Step_0.md (Phase 0) — 3 of 3 (2 direct, 1 via Tier U)
| Address | Covered by |
|---|---|
| `…/TepenianUniverseTimeline/Reference/Repo_Scope.md` | row "**U** `Repo_Scope.md`" (direct) |
| `…/TepenianUniverseTimeline/Timeline Eras/` | rows "Temporal frame", "Act structure", "The consolidating mechanism" → `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` (source: `Timeline Eras/2 The Second Interwar Period/README.md`) — via Tier U ⚑ (one era of the four) |
| `…/Cities/Official_Population_Census.md` | rows "Census I", "Census II" (direct) |

### Step_1_and_2.md (Phase 1) — 6 of 6 (6 direct)
| Address | Covered by |
|---|---|
| `…/TepenianUniverseTimeline/Worldspace/Locations/` | row "Universe repo `Worldspace/Locations/` — directory enumerated" + "↳ README.md" (direct ⚑ cited with an elided `…/` prefix) |
| `…/Cities/Specs/` | rows citing `Specs/Dome_Fuji.md` (direct ⚑ directory-qualified short form) |
| `…/Worldspace/Energy_Grid_Failure_Rationale.md` | row `Energy_Grid_Failure_Rationale.md` (direct) |
| `…/Reference/Real-World/Climate Data/READER/` | row "Climate READER file", citation `READER/Dome_Fuji.md` (direct ⚑ directory-qualified short form) |
| `…/Reference/Real-World/Stations/` | rows `Antarctic_Stations_With_Airstrips.md` L24, L97 and `COMNAP_Antarctic_Station_Catalogue.pdf` (direct ⚑ files inside the folder, folder path not written) |
| `…/Division_of_Industry/16_Per_City_Three_Tier_Run.md` | Half B row and the new §32 row (direct) |

### Phase_2.md — 3 of 3 (1 direct, 2 via Tier U) — *was written "3 directly"*
| Address | Covered by |
|---|---|
| `…/Reference/No_National_Stereotypes.md` | row "GPS law — the operative distinction" → `Corpus_Reference_Sheets/No_National_Stereotypes_Quick_Reference.md` (source line names `Reference/No_National_Stereotypes.md`) — via Tier U |
| `…/Reference/Falkland_Treaty/` | three "Falkland Treaty —" rows → `Corpus_Reference_Sheets/Falkland_Treaty_Quick_Reference.md` (source: `Falkland_Treaty_Draft_v1.md`, `Scaffold.md`, `Real_World_Influences.md`) — via Tier U |
| `…/Cities/Official_Population_Census.md` | rows "Composition tier table (census Section A entry)", "Census I" (direct) |

### Phase_3.md — **3 of 4** (3 direct; Davis folder n/a)
| Address | Covered by |
|---|---|
| `…/Climate Data/READER/` | **not covered** (no row of this sheet names it; the READER file is in `Step_1_and_2.md`) |
| `…/Cities/Specs/` | rows "Spec — `## Geographic Basis`", "`## Character & Culture`", "`## Notable Locations`" citing `Specs/Dome_Fuji.md` (direct ⚑) |
| `…/Cities/City_Concept-Art/` | row "Concept-art directory status", citation `City_Concept-Art/Mawson_Subnet/Dome_Fuji` (direct ⚑ the city's folder inside the address) |
| `…/Cities/City_Megasheets/` (withheld; "record the conflict") | row "Megasheet Physical Infrastructure file" naming `Dome_Fuji_Physical_Infrastructure_Attributes.md` (direct ⚑ the file inside the withheld folder, folder not named) |
| `…/Davis_Geosciences_Research/` | n/a (Davis only; not counted) |

### Phase_4.md — **6 of 7** (4 direct, 2 via Tier U)
| Address | Covered by |
|---|---|
| `Robot_Physiology_and_Cultural_Practices.md` | rows "Robot Physiology — appearance/clothing baseline", "Siligel / coolant / smoking…" → `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md` (via Tier U) |
| `Robot_Cold_Physiology.md` | row "Robot Cold Physiology — the governing mechanic" → same Tier U sheet (via) |
| `16_Per_City_Three_Tier_Run.md` | Half B row and §32 row (direct) |
| `09_Per_City_Baseline_Run.md` | row 1 (direct) |
| `11_Caloric_Rebuild_and_Livestock_Tier.md` | row 2 (direct) |
| `National_Medical_and_Care_Institutes.md` | row 4 (direct) |
| `…/Worldspace/National_Economy_and_Currency.md` | **not covered** |

### Phase_5.md — **5 of 6** (5 direct)
| Address | Covered by |
|---|---|
| `…/TepenianUniverseTimeline/Worldspace/Locations/` | **not covered** in this sheet (it is enumerated in `Step_1_and_2.md`) |
| `…/Infrastructure/Highways.md` | five Highways rows (direct) |
| `…/Infrastructure/` (Airports · Ports · Geothermal_Heating) | rows `Airports.md` ×5, `Ports.md` ×4, `Geothermal_Heating.md` (direct ⚑ the three named files; the folder path is not written) |
| `…/Cities/City_Cross_Subnet_Relationships.md` | row (direct) |
| `…/Cities/City_Relationship_Database.md` | entry + seven line rows (direct) |
| `…/Cities/City_National_Connections.md` | row (direct) |
(`Arcanet.md` has a row but is not in the spine's Phase 5 list; not counted.)

### Phase_6.md — 5 of 5 (5 direct)
`Factions/Robot_Religions/` (row "Factions/Robot_Religions/ — directory enumerated", path written) · `National_Holidays.md` (row) · `Ice-Cold_Buddhism_Research/` (row, path written) · `The_True_Believer_Extraction.md` (row) · `The_Meme_Machine_Extraction.md` (row). All direct.

### Phase_7.md — **8 of 13** (7 direct, 1 via Tier U) — *was written "13 of 13 (10 + 3)"*
| Address | Covered by |
|---|---|
| `…/Cities/Division_of_Industry/` | header box cites `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md` (source: `Division_of_Industry/README.md`) — via Tier U ⚑ (the row for `01` cites the base name `README.md` only) |
| `16_Per_City_Three_Tier_Run.md` | Half B, §32 and "other lines" rows (direct) |
| `Division_of_Industry_Sweep_2026-08-31.md` | five rows (direct) |
| `01_Burden_Scoring_Model.md` | row "status stamp in the folder README" (direct; the citation cell is `README.md`) |
| `08_Volume_Based_Requirement_Reference.md` | **not covered** |
| `National_Medical_and_Care_Institutes.md` | **not covered** (it is in `Phase_4.md`) |
| `Theoretical-Calculations/` | row (direct) |
| `Reference/Real-World/Industry_Staffing_and_Productivity/` | **not covered** |
| `jobs_professions_and_fields/` | row (direct) |
| `…/Worldspace/National_Economy_and_Currency.md` | **not covered** |
| `…/Worldspace/City_Logistics.md` | row (direct) |
| `…/Worldspace/Factions/` | row (direct) |
| `…/TepenianUniverseTimeline/Megacorps/` | **not covered** |
Meta row elsewhere in the sheet (row "MUST-OPEN coverage (spine, Phase 7)": "…exist on disk: **11 of 11**") restates a count and now disagrees with the header — **left as is, reported** (brief §4a).

### Phase_8.md — 2 of 2 (2 direct)
`Robot_Biology_and_Culture/` (row headed "`Robot_Biology_and_Culture/` mandatory facts (Tier U…)", direct ⚑ directory name written, content taken from the Tier U sheet) · `Weapons_and_Tools_Philosophy.md` (row, direct).

### Phase_9.md — **3 of 4** (2 direct, 1 via Tier U)
| Address | Covered by |
|---|---|
| `…/TepenianUniverseTimeline/Reference/Laws_of_Robotics.md` | **not covered ⚑** — the row "Laws of Robotics (Tier U)" states two laws but names no file and cites `Robot_Physiology_Quick_Reference.md`, which does not hold them (and the wording differs from the file; see New findings) |
| `…/Reference/Robot_Universals/` | row (direct; path written) and the two "↳" rows |
| `…/Reference/Doll_Representation_Categories.md` | row (direct) |
| human-robot baseline = `Robot_Physiology_and_Cultural_Practices.md` | rows citing `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md` (source line names the file; its §"Human-robot relations — the baseline" is at its L81) — via Tier U ⚑ (no row is headed with the baseline) |

### Phase_10.md — 3 of 3 (2 direct, 1 via Tier U) — *was written "3 directly"*
`…/TepenianUniverseTimeline/Worldspace/Characters/` (row, direct) · `Enneagram_Character_Index.md` (row, direct) · `Zodiac_Signs_Full_Attributes.md` (row "Zodiac Lens — all 12 signs' full attributes (Tier U)" → `Corpus_Reference_Sheets/Zodiac_Signs_Quick_Reference.md`, via Tier U).

Sheets with no MUST-OPEN header (no count to restate): `Step_-1.md`, `Step_3.md`, `Step_5.md`, `Step_6.md`, `Step_7.md`, `Step_8.md`, `Step_9.md`, `Step_10.md`.

---

## 3 · New findings (not in the ledger; nothing below was fixed)

**Rows missing for must-open addresses (gaps for the developer to decide on):**
- `Phase_3.md`: the Climate `READER/` folder.
- `Phase_4.md`: `Worldspace/National_Economy_and_Currency.md`.
- `Phase_5.md`: the universe repo `Worldspace/Locations/` (**U** Location canon + routes).
- `Phase_7.md`: `08_Volume_Based_Requirement_Reference.md`, `National_Medical_and_Care_Institutes.md`, `Industry_Staffing_and_Productivity/`, `National_Economy_and_Currency.md`, the universe repo's `Megacorps/`.
- `Phase_9.md`: `Laws_of_Robotics.md` (see next item).

**Other findings:**
1. **Ledger range, DF-004 / DF-026.** The Deepest Cold entry in `National_Holidays.md` runs L100–**L107**, not L100–106 (the last words, "within the faith.", are L107). Applied with the live number; the ledger text should be corrected.
2. **`Phase_9.md` row "Laws of Robotics (Tier U)"** (not fixed). Its text is not the file's: the sheet says "A robot will have full capacity…" and "…anything she is capable of doing to others is realistically possible for others to do to her"; `Laws_of_Robotics.md` L3 reads "…will have **the** full capacity…" and L4 "…anything she is capable of doing to others, **it is also** realistically possible for others to do to her." The row cites `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md`, and a search of that sheet finds neither law nor the word "Laws". Needs a re-copy from the file and a correct citation (or a Tier U sheet that holds the laws).
3. **`Phase_4.md` row 1 (`09` §2 row)** transcribes `09`'s `Required` (18,264) and `% WF` (27.3%) columns, which `16` L30–32 ("discard its `Required` and `% WF` columns, which used the circular B1 rate") declares SUPERSEDED. For this zero-human city the % equals `16`'s base% (27.3%), so no number is wrong; the question is whether the row should carry the columns at all, and whether SH-014's clause belongs beside them (I did not add it; see SH-014 row).
4. **`Phase_7.md` meta row** says "11 of 11" while the header now says 8 of 13 (left, per brief).
5. **`16` §32 text itself** (source, not edited): L3234 says "its entire 55,072 population IS the devotee body" and L3258 names the "Sayowa Junction" (retired name); the file's L1 header says the per-city determinations were not recomputed after `DR-68`. Consistent with the ledger's "counts pre-`DR-68`".
6. **City_Relationship_Database L204** (copied as written in `Phase_5.md`) says "altitude too extreme for population growth" while Census I reads 66,849; **L512** quotes the 2026-07-04 figure 55,072. Both are dated source notes; flag only.
7. **`Step_1_and_2.md` row "↳ README.md"** copies the timeline repo's `Worldspace/Locations/README.md` L19 as written ("Mawson subnet: Dome Fuji, Mawson, Sayowa") — "Sayowa" is the retired name of Temirötkel; the timeline repo is flag-only and the rename sweep is not mine.
8. **`Phase_3.md` header N.** The spine's Phase 3 block lists five addresses (Climate, Specs, Concept art, Davis folder "where applicable", Megasheets); the header's N=4 excludes the Davis-only folder. Kept (⚑ convention question for the orchestrator: should a "where applicable" address that does not apply count in N?).
9. **Pre-Trip §I** still carries "DATASHEET-NOT-YET-BUILT(N-5)=20", "RESOLVE=123", "126 claims · 126 OK" etc. as the dated 2026-10-21 build record (left on purpose, per DF-002); after this sweep it no longer describes the file (e.g. its line lists have moved). A dated note or a re-run of the existence test is for the orchestrator.
10. **Dome Fuji `16` Half B row** carries `src: H` ("Half A estimate, MINE, needs ruling" per `16` L244–L245 legend) while the city's own §32 is a determination; not a sheet defect, noted because the sheets now quote both.

---

## 4 · Files edited (13, all with the Edit tool)

All under `…/Cities/City_Development_Passes/Mawson_Subnet/Dome_Fuji/`:
- `00.0_Pre-Trip_Inspection.md`
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

Not edited: `Step_-1.md`, `Step_5.md`–`Step_10.md` (no `PENDING` entry reaches them; the held items DF-003, DF-025, SH-007, SH-009 are the only ones that would have), the pass `README.md`, `00.2_Position_Coverage_Ledger.md`, every spec / census / `09` / `16` / Airports / Ports / Highways / relationship file, the timeline repo, `FIX_LEDGER.md`, `TRACKER.md`, the builder scripts. Nothing was committed.

New file: `Manual_Input_Audit_2026-10-29/Sweep_Reports/Dome_Fuji_Sweep.md` (this report).
