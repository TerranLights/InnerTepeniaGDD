# Ariun Nuur — fix-sweep report (2026-10-30)

**City:** Ariun Nuur (ledger section **B7 · ARIUN NUUR**; pass folder `PASSES/Mirny_Subnet/Ariun_Nuur`; the sheets still say "Vostok", which was left as is under `AN-008`). **Who:** sweep sub-agent. **Date:** 2026-10-30.
**Read:** `SWEEP_BRIEF.md` in full (with §4a); `FIX_LEDGER.md` section A and `### B7 · ARIUN NUUR`; `Ariun_Nuur_Audit.md` in full; the whole Pre-Trip (566 lines before the sweep), the pass `README.md`, `00.2_Position_Coverage_Ledger.md`, all 19 datasheets; the whole spec `Specs/Mirny subnet/Ariun_Nuur.md` (205 lines); every live source line named below, re-opened before writing. For form only (rule 6): the Santa Luce / Relung Panen / Casey rows for the composition file and the Founding Register note (one grep of each Pre-Trip / `Phase_2.md`; nothing else of those cities was read). The megasheet folder was only counted (`ls | wc -l`, `find -type f`, `find -type d`); the city's Local Culture, Local Robot Culture, Enneagram, vision notes, megasheets and Background-Lore were **not** opened.
**Method:** Edit tool only; no `sed -i`, no generators, nothing rebuilt, nothing committed. Read-only helpers used as locators and for checks: `grep -n -i`, `sed -n`, `ls`, `find`, `git diff`, and small read-only Python scripts that printed (never wrote) set comparisons.

**Totals:** APPLIED 26 (17 ledger entries + 9 shared fixes) · ALREADY-RIGHT / not present 1 (SH-006) · HELD 2 (SH-007, SH-009) · NEEDS-DEVELOPER 2 (SH-010: the city has no section in the composition file; SH-013: the city's upper-case heading, see New findings 1) · SKIPPED-MISMATCH 0 · DECIDE/NOTE entries left untouched 11 (AN-006, AN-008, AN-024, AN-025, AN-027, AN-031, AN-S01, AN-S02, AN-S03, AN-S04, AN-S05).

---

## 1 · Entry table

### Ledger entries for Ariun Nuur

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| AN-001 | APPLIED | `00.0_Pre-Trip_Inspection.md` (§C Step 2 `T8`; Step 0 `T8` Census line; §D Phase 1, 4, 5 rows; §E) | Every "Names Ariun Nuur at" list regenerated from a live `grep -n -i "ariun\|vostok\|ариун"` on each file and compared as a set. **Airports** L18, 49, 53 → **L18, 52, 56**. **Ports** L205, 459, 717 → **L205, 482, 740**. **CrossSub** …L227 → **…L228** (L47, 78, 97–98, 176, 180 unchanged). **`09`** L57, 199, 237, 239 → **L57, 201, 239, 241**. **RelDB** L14, 26, 49, 105 unchanged; L124, 169, 226, 272–273, 465–466, 473, 520 → **L135, 180, 237, 283–284, 476–477, 484, 531**. **NatConn** L243, 281 unchanged; L320, 332, 336, 338–339, 342, 507–508, 559, 565, 576 → **L321, 333, 337, 339–340, 343, 512–513, 564, 570, 581**. **`16`**: row L281 → **L282** (Step 2 `T8` line, §D Phase 1 row, §E row); other lines L673, 1817, 1904–1905, 2149, 2348, 2352, 2363, 2374, 2376, 2391, 2393, 2396, 2402, 2412, 2414, 2423 → **L678, 1822, 1909–1910, 2154, 2349, 2353, 2357, 2368, 2379, 2381, 2396, 2398, 2401, 2407, 2417, 2419, 2428** (L80, 114, 222, 232 unchanged). L2349 is the city's own upper-case heading (`## 23. ✅ VOSTOK — DETERMINED`) and is marked so in both lists. **Census** (Step 0 `T8` line): added **L644**. Unchanged and re-confirmed live: Highways L5, 156, 162–163, 170; Arcanet L26; RobotPhys L409; NMCI L16, 98–99, 107, 109, 231; `11` L142, 144, 357; Stations L67, 97; Extent L249, 578, 587, 625; Cymatics L19; Precipitation_Falls_vs_Lands L69, 105, 108, 214–215, 235; Research_Topics L278–279. | Script compared each list with the live grep as a set: **listed-not-live = none, live-not-listed = none** for Airports, Ports, CrossSub, RelDB, NatConn, `09`, Highways, `11`, NMCI and the two `16` lists (Phase 1 row and §E row are the identical 22-line set + L282). Odd hits opened: RelDB L105/L135/L180/L237 and NatConn L243/L281/L513/L564/L570/L581 are neighbors' or relation lines that name the city (same convention as the old lists); RelDB L477/L484 are the city's own entry ("Vostok Station", "Lake Vostok"); no hit is the district or the explorer by itself. |
| AN-002 | APPLIED | Pre-Trip §D Phase 7 row "Vostok-specific research" (the only place the text sits; §J does not carry the number) | "registry (L2072)" → **L2074** | `00_RUNBOOK.md` L2074 = the `Vostok_Genetics_Research/` registry row; L2072 = the `jobs_professions_and_fields/` row. |
| AN-003 | APPLIED | Pre-Trip §A "Retired filenames and folders" | "the megasheet and concept-art folders keep `Vostok`" → "only the megasheet folder `City_Megasheets/Mirny_Subnet/Vostok/` keeps the old name; the concept-art folder is `City_Concept-Art/Mirny_Subnet/Ariun_Nuur/` and the pass folder is `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/` (both renamed 2026-10-23, Alias Table §3b, L45–59)" | `ls City_Concept-Art/Mirny_Subnet/` shows `Ariun_Nuur` (and no `Vostok`); `City_Megasheets/Mirny_Subnet/` still has `Vostok`; Alias Table L45 heading and L54 row read live. |
| AN-004 | APPLIED | Pre-Trip §A | Added two alias rows: **Ариун Нуур** (Mongolian, "the pure lake", spec L3 and L10) and **Southern Pole of Inaccessibility** (spec L49; "the Pole of Inaccessibility" at L138). Reworded the "Other scripts / variant spellings" row: the 2026-09-30 "no non-Latin script, nothing found for *formerly/renamed*" check is marked superseded by the 2026-10-03 rename, re-read 2026-10-30. | Spec L3 contains "RENAMED", "formerly" and "Ариун Нуур"; L10 contains "Ариун Нуур"; L49 and L138 read live. (The ledger/audit give spec "L5, L49" for the Pole; **L5 does not contain the phrase**, see New findings 4.) |
| AN-005 | APPLIED | Pre-Trip §D Phase 2 table (new row) and §J (new row) | Added the Founding Register as an address: own row **L63**, the `DR-35` ruling **L84**, the rename **L92**, the cleanup **L94**; **L64** (another city's row) and **L83** (another city's ruling) name the city as a relation. §J note "Founding Register not in the Phase 2 `T8` list" added, in the form of Casey's / Relung Panen's note (recorded as an address, not added to any read list; the developer decides). | `Founding_Register.md` live `grep -n -i`: hits at L63, 64, 83, 84, 92, 94 exactly. **L83 is not in the ledger list**; it was found by the live grep and is added as a relation line (flagged here). |
| AN-006 | DECIDE — untouched | Pre-Trip §D addendum / §J | `Research_Logs/Ariun_Nuur_Inspiration_Place_Research_R1.md` and `_R2.md` not registered (tier is the developer's) | `ls Research_Logs` shows both files exist. |
| AN-007 | APPLIED | `README.md` "This city's existing sources" (4 pointers) | `Specs/Mirny subnet/Vostok.md` → `Ariun_Nuur.md`; `Local_Cultures/Mirny_Subnet/Vostok.md` → `Ariun_Nuur.md`; `City_Vision_Notes/Vostok.md` → `Ariun_Nuur.md`; `Research_Logs/Vostok_Research_Log.md` → `Ariun_Nuur_Research_Log.md` | From the pass folder: the first three relative paths resolve; the fourth does **not exist yet** (the README row already says "may not exist yet"). The README title "Vostok — development pass" is left (AN-008). |
| AN-008 | DECIDE — untouched | Pre-Trip title and all sheet text | rename inside the sheets | — |
| AN-009 | APPLIED (SH-007 HELD) | Pre-Trip | Shared items under SH-001 … SH-006 below. Megasheet "7 files": §D Phase 3 row → "**6** files and **1** subfolder (7 entries by `ls \| wc -l`; split by `find -type f` / `-type d`; names not listed)"; §F row "(**7** files)" → "(**6** files and **1** subfolder)". | `ls … \| wc -l` = 7; `find -maxdepth 1 -type f` = 6; `find -mindepth 1 -maxdepth 1 -type d` = 1. `Datasheets/Phase_3.md` row 10 already says "6-file Megasheet set" (left). No `01` "line 65" coordinate exists in this city's sheets (SH-007 not present). |
| AN-020 | APPLIED | `Datasheets/Phase_2.md` · per-nation row | All eight R/H pairs replaced with the spec's: USA 76,971 / 40,199 · Japan 67,788 / 35,404 · Canada 37,730 / 19,706 · Indonesia 36,771 / 19,205 · Australia 17,513 / 9,146 · South Korea 16,554 / 8,645 · Chile 13,457 / 7,028 · New Zealand 4,638 / 2,422 (shares unchanged) | A script built the expected row string from spec L34–41 and found it **verbatim in the sheet** (True). Sums by script: robots 271,422 and humans 141,755 = Census I. By hand, robots: 76,971 + 67,788 = 144,759; + 37,730 = 182,489; + 36,771 = 219,260; + 17,513 = 236,773; + 16,554 = 253,327; + 13,457 = 266,784; + 4,638 = 271,422. Humans: 40,199 + 35,404 = 75,603; + 19,706 = 95,309; + 19,205 = 114,514; + 9,146 = 123,660; + 8,645 = 132,305; + 7,028 = 139,333; + 2,422 = 141,755. |
| AN-021 | APPLIED | `Datasheets/Phase_4.md` row 14 (L14); `Datasheets/Step_7.md` note | 41.5% → **42.0%** in both. Row 14 now also labels `16` §23's counts "pre-`DR-68`" (121,353 + 66,007 + 137,092 = 324,452), cites `16` L1, and says the two percentages "are therefore also on different workforce denominators, which accounts for part of the gap" (324,452 vs 342,300). Step 7 note says the same and cites both sheets. | `09` L57 reads `\| 4 \| **Vostok** \| Mirny \| 2.50 \| 141,755 \| 413,177 \| **143,796** \| 342,300 \| **42.0%** \|`. 121,353 + 66,007 = 187,360; + 137,092 = 324,452 ✓. `16` L1 header: "The per-city determinations further down … were NOT recomputed." (**Where the old 41.5% came from:** `09` L201, a §3.6 cell that DR-68 did not refresh — see New findings 2.) |
| AN-022 | APPLIED | `Datasheets/Phase_4.md` · DoI carve-out row (L18) | "(129,617 humans)" → "(**141,755** humans)" | Spec L17 and census L508 read 141,755 H. |
| AN-023 | APPLIED | `Datasheets/Phase_7.md` rows 24, 25; `Datasheets/Step_1_and_2.md` row 27 | Half B row cite **L281 → L282**; values "Baseline 37.4%, Mandate 5.8%, Free 56.8%" → **37.8% / 5.8% / 56.5%**; the row's "at the time of the Half B run" reworded to the source's own refresh note (workforce 342,300; Workforce, base%, MAND% and FREE% cells refreshed 2026-10-28 under `DR-68`, mandate shares held; cite L282 and L1). `16` §23 cite **L2344–2350 → L2349–2355** (Phase_7 row 24, Step_1_and_2 row 27). | `16` L282 live: `\| Vostok \| Mirny \| 2.50 \| 342,300 \| 37.8% \| 5.8% \| 56.5% \| D \|`. `16` L2349 = `## 23. ✅ VOSTOK — DETERMINED`; L2351–2355 = the tier table (37.4% / 20.3% / 42.3%). |
| AN-024 | DECIDE — untouched | `Step_1_and_2.md` row 26; `Phase_3.md` rows 13, 15, 16 | re-quote from the live spec (with AN-008) | Not applied (waits with AN-008). |
| AN-025 | DECIDE — untouched | `Step_-1.md` "203 lines"; `Phase_8.md` "203-line file" | live `wc -l` is 205 (SH-009) | Not applied. |
| AN-026 | APPLIED | `Datasheets/Phase_5.md` · Port status (L17) | `Infrastructure/Ports.md` L459, L717 → **L482, L740** | Ports L482 = "**Deep interior / plateau:** … Ariun Nuur …" under heading "5.5 Landlocked"; L740 = `\| **LANDLOCKED** … Ariun Nuur … — **10** \|`. |
| AN-027 | DECIDE — untouched | `Step_10.md` "(429-line file)" | 431 | Not applied. |
| AN-028 | APPLIED | `Datasheets/Step_1_and_2.md` row 19 | `"#2 coldest of the 37," sits above the katabatic regime` → `Sits above the katabatic regime *(the source's clause ranking this city against the others is not carried)*` | Spec L76 holds the rank clause; the kept words "it sits above the katabatic regime" are the spec's. |
| AN-029 | APPLIED | `Datasheets/Step_0.md` (new row 14); `Datasheets/Step_1_and_2.md` (new row 35); `Datasheets/Step_7.md` note | Extent row: Mirny · Census I 389,261 (the 2026-09-05 population) · **39 km²** at 10,000/km² · **56 km²** at 7,000/km² · plateau; at the live 413,177: **41.3** and **59.0 km²**; cites `Extent_and_Density_Per_City.md` row L625 *(2026-09-05 snapshot; the census is live — note L631)* and census L508. Step 7 note "extent/area figure not yet located" → "located: … row L625 …, recorded in `Step_0.md` and `Step_1_and_2.md`". | Extent L625 live: `\| **Vostok** \| Mirny \| 389,261 \| 39 \| 56 \| **plateau** \|`; L631 live = the snapshot note. Arithmetic by hand: 413,177 ÷ 10,000 = 41.3177 → 41.3; 413,177 ÷ 7,000 = 59.0253 → 59.0 (7,000 × 59 = 413,000; 177 ÷ 7,000 = 0.0253). Band 7,000–10,000/km² is Extent L84. |
| AN-030 | APPLIED | `Datasheets/Step_6.md`; `Step_8.md`; `Step_9.md`; `Step_10.md` | Step 6 section 1 columns "Shape · Deficit address · Pass" → "**Subnet** · Shape · Deficit address · Pass". Step 9: new row for **item 5** (discharge every deferral to the pass's close, `M-291`; text copied from runbook L3011–3015, cite L3011–3015). Pointer rows added to the Tier U sheets `Review_Panel_Full_Text_Quick_Reference.md` (Step 8), `Step_9_Record_Full_Text_Quick_Reference.md` (Step 9), `Step_10_Readiness_Check_Full_Text_Quick_Reference.md` (Step 10), each with "the runbook wins where they differ". | Live header of `Cross_City_Culture_Differentiation_Table.md` L48: `\| City \| Subnet \| Shape \| Deficit address \| Pass \|`. All three Tier U files exist. **Note:** the Step 9 and Step 10 Tier U sheets are the stale ones (SH-015 / SH-016, DECIDE); the pointers were added as the ledger asks and nothing was copied from those sheets. |
| AN-031 | DECIDE — untouched | `Phase_6.md` "378-line file" / "293-line file" | 377 / 292 | Not applied. |
| AN-032 | APPLIED | `Datasheets/Phase_10.md` · Characters row (L11) | "2 files matched" → "**3** files matched" | Live `grep -rli vostok` over the timeline repo's `Worldspace/Characters/`: `Dolls/Calethina/README.md`, `Dolls/Calethina/Personal_Background/Formative_History.md`, `Dolls/TBN [XT-17 …Charlene]/README.md` = 3 (the row lists the same three). `grep -rli ariun` there: none. |
| AN-033 | APPLIED | `Datasheets/Phase_7.md` row 47; `Datasheets/Phase_5.md` row 29 | Sweep matrix: "L169, legend elsewhere in file" → "L169; legend at L139". Universe `Locations/` row: **re-enumerated** (not left as dated): "4 `.md` files read (2 at the top level, 2 in a subfolder; re-enumerated 2026-10-30); 1 names the city". | Sweep L139 = "`Y` = the sector is named or clearly described · `.` = absent"; L169 = the city's `6/6` row. Timeline `Worldspace/Locations/`: `find -name "*.md"` = 4, top level = 2, `grep -rli "ariun\|vostok"` = `README.md` only (L20). No other city is named in the new text. |
| AN-S01 | DECIDE — untouched (SOURCE) | spec L49 | "no highways, no coastal access, no neighboring cities" | — |
| AN-S02 | DECIDE — untouched (SOURCE) | spec L142 | "its nearest subnet city" | — |
| AN-S03 | DECIDE — untouched (SOURCE) | spec **L76** (ledger says L77) | "#2 coldest of the 37" | The phrase is on **L76** live; the sheet's row 19 already cites L65, L76. Ledger/audit line number is off by one. |
| AN-S04, AN-S05 | NOTE — untouched | spec L71–73, L63, L169; timeline `Locations/README.md` L20 | — | — |

### Shared fixes (SweepBrief §3)

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| SH-001 | APPLIED | Pre-Trip §G "No invented person names" | spine **L127** → **L220, L1114, L1140** | Spine L220 "…and the no-invented-person-names rule"; L1114 "NO INVENTED PERSON NAMES — role placeholders permanently"; L1140 "People as role-archetypes — binding rule: no invented proper names". `Datasheets/` carry no `L127` cite. |
| SH-002 | APPLIED | Pre-Trip §G "Divergence operator" | runbook **L2178** → **L2180** | `grep -n "THE DIVERGENCE OPERATOR" 00_RUNBOOK.md` = L2180 (`### ⭐ THE DIVERGENCE OPERATOR …`). |
| SH-003 | APPLIED | Pre-Trip §C Step 5 `T8` | `02_Generators…` §5.3 lines 610–684 → **610–636** | `02` L610 = "## 5.3 The both-are-true test"; L637 = "# 6. Symbol binding". |
| SH-004 | APPLIED | Pre-Trip §C procedure items 4 and 5 | item 4 "620–643 and 701–703" → **"620–643 and 682–684"**; item 5 "650–703" → **"667–684"** | `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` L620 (Round 3 heading) – L643 (end of the four-question prompt block, still the four questions) ✓; L682 "**Round 3's prompt now carries a fifth section**" – L684 "record for the merge." ✓; L667 "AMENDED 2026-09-28 — THE WRITTEN CONTENT IS A MERGE, NOT A PICK" – L684 ✓. |
| SH-005 | APPLIED | Pre-Trip §C Step 10 | "3057–3172" (twice: governing rule and `T8` read) → **3057–3152**; card note "live lines 3045–3161 govern" → **"live lines 3057–3152 govern"** | Runbook L3057 `# Step 10 — THE READINESS CHECK`; L3153 `# Where everything lives` (L3151 `---`, L3152 blank). |
| SH-006 | ALREADY-RIGHT (not present) | `Step_-1.md`, Pre-Trip | the cite of runbook L1821–1822 does not occur | `grep -n "1821\|1822"` over the Pre-Trip and all datasheets: no such cite. (Live L1854–1855 anchor exists if a row is ever added.) |
| SH-007 | HELD | — | `01` "line 65" coordinate | Not present in this city's sheets; nothing to hold or change. |
| SH-008 | APPLIED | the 11 sheets with a header (`Step_0`, `Step_1_and_2`, `Phase_2` … `Phase_10`) | every header recounted by hand, "checked 2026-10-23" → "recounted by hand 2026-10-30"; six counts changed (see section 2) | Table in section 2. |
| SH-009 | HELD | `Step_-1.md`, `Phase_8.md`, `Phase_6.md`, `Step_10.md` | "N-line file" counts left as is | — |
| SH-010 | PARTIAL → NEEDS-DEVELOPER | Pre-Trip §D Phase 2 table (2 new rows); `Datasheets/Phase_2.md` (2 new rows, L15–16) | **This city has no section in `Upper_Earth_Immigration_Composition.md`:** `grep -c -i "ariun\|vostok\|ариун"` = 0 (the file's Mirny-subnet block is L531–645). So the rows say so ("None: this city has no section in the file … The spec cites the file once, for the share-weighting method", spec L43) and carry the **solar-UTC rule**: heading L21, list "Recording it so it stops being reconstructed from examples" **L26–L33**, rule 1 at **L28**. | Lines read live (L21, L26, L28, L33). Form copied from Casey's / Relung Panen's / Santa Luce's rows. **Developer question:** whether the city's composition belongs in that file at all (its composition lives only in the spec, L20–43). |
| SH-011 | APPLIED | Pre-Trip Step 0 `T8` line; `Step_0.md` row 14; `Step_1_and_2.md` row 35; `Step_7.md` note | added "(2026-09-05 snapshot; the census is live — note L631)" beside every Extent row cite | L631 live is still the snapshot note. No Extent row cite in §D Phase 0 (that table has no Extent row); §E cites only prose lines (L249, 578, 587), no row. |
| SH-012 | APPLIED | Pre-Trip, datasheets | covered by AN-001, AN-023, AN-026, AN-033 | — |
| SH-013 | NEEDS-DEVELOPER (per §4a) | Pre-Trip | The ledger does not list SH-013 for this city, but the city has an upper-case determination section (`## 23. ✅ VOSTOK — DETERMINED`, L2349). Its heading line was added to both `16` line lists and marked "the city's own upper-case heading". The sheets **already** quoted §23 beside the Half B row and said which governs (Phase_7 rows 24–25, Step_1_and_2 row 27, Phase_4 row 14), so nothing new was quoted by me. | See New findings 1. |
| SH-014 | APPLIED | `Step_1_and_2.md` row 27; `Phase_4.md` row 14; `Phase_7.md` rows 24, 25, 27 | added the clause "on the flat ABCC working value; counts re-run when per-city ABCC values are set (`16` L1287–1304)" beside each `16` baseline % / worker count | `16` L1287 "### ⚠ CONSEQUENCE — the ten determinations so far need a baseline re-run" … L1302–1304 "ABCC stays at the flat 65 per 1,000 residents for ALL cities. New determinations continue on the flat value so that every city re-runs together"; L1305 blank. Range cited **L1287–1304** (not L1305). |

(SH-015 … SH-017, SH-019 are Tier U sheets for the orchestrator; SH-018, SH-020 … SH-023 touch Tier U sheets only.)

---

## 2 · MUST-OPEN recount (SH-008), by hand, 2026-10-30

Rule applied: an address is covered only if a row of the sheet **names it by its full path / full file name** (a file inside a folder counts for the folder), or the sheet cites a shared Tier U sheet that names it. Cross-references to another datasheet do not count; a bare label does not count. Row numbers are file lines in the sheet after the sweep. ⚑ = judgment call.

| Sheet (spine phase) | Address | Covering row | Covered |
|---|---|---|---|
| **Step_0** (Phase 0) — header was 3 of 3 (3 direct) → **3 of 3 (2 direct, 1 via Tier U)** | `Repo_Scope.md` | row 20 (full path `TepenianUniverseTimeline/Reference/Repo_Scope.md`) | direct |
| | `Timeline Eras/` | row 15 cites `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md`, whose header L4 names `Timeline Eras/2 The Second Interwar Period/README.md` | via Tier U ⚑ (the Tier U sheet names a path inside the folder) |
| | `Official_Population_Census.md` | rows 11, 12, 14, 19 | direct |
| **Step_1_and_2** (Phase 1) — was 6 of 6 (6 direct) → **4 of 6 (4 direct, 0 via)** | Universe repo `Worldspace/Locations/` | **not covered** (row 21 of `Step_0.md` carries `TepenianUniverseTimeline/Worldspace/Locations/README.md`, but that is another sheet) | not covered |
| | `Specs/` | rows 13–18 (`Specs/Mirny subnet/Ariun_Nuur.md`) | direct |
| | `Energy_Grid_Failure_Rationale.md` | row 31 (zero-hit check row) | direct |
| | Climate `READER/` | rows 15, 18, 24 (`Reference/Real-World/Climate Data/READER/Vostok.md`) | direct |
| | `Stations/` | **not covered** (row 22 of `Step_0.md` carries it; another sheet) | not covered |
| | `16_Per_City_Three_Tier_Run.md` (Half B) | row 27 (file named; the cited section is §23, the Half B row itself is transcribed in `Phase_7.md` row 25) | direct ⚑ |
| **Phase_2** — was 3 of 3 (3 direct) → **3 of 3 (1 direct, 2 via)** | `No_National_Stereotypes.md` | row 18 cites `Corpus_Reference_Sheets/No_National_Stereotypes_Quick_Reference.md`, whose L4 names `Reference/No_National_Stereotypes.md` | via Tier U |
| | `Falkland_Treaty/` | row 17 cites `…/Falkland_Treaty_Quick_Reference.md`, whose L3–4 name `Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md` and two more files | via Tier U |
| | `Official_Population_Census.md` | row 14 (citation column, L440) | direct |
| **Phase_3** — was 4 of 4 (4 direct) → **3 of 4 (3 direct)**; Davis research folder "where applicable" stays not applicable (spine bullet 4 of 5), as the old header already said | Climate `READER/` | **not covered**: row 11 is a cross-reference to `Step_1_and_2.md`, which names it; the sheet itself does not ⚑ | not covered |
| | `Specs/` | rows 13–16 | direct |
| | `City_Concept-Art/` | row 9 (`City_Concept-Art/Mirny_Subnet/Ariun_Nuur/`) | direct |
| | `City_Megasheets/` | row 10 (`City_Megasheets/Mirny_Subnet/Vostok/`, `Vostok_Physical_Infrastructure_Attributes.md`; existence recorded, never opened) | direct |
| **Phase_4** — was 7 of 7 (6 direct, 1 via) → **7 of 7 (5 direct, 2 via)** | `Robot_Physiology_and_Cultural_Practices.md` | rows 19–21 cite `Robot_Physiology_Quick_Reference.md`, whose L3 names it | via Tier U |
| | `Robot_Cold_Physiology.md` | row 20 cites the same sheet, which has a section "What cold actually costs — `Robot_Cold_Physiology.md`" | via Tier U |
| | `16_Per_City_Three_Tier_Run.md` (Half B) | row 14 (file named; §23 and L1 cited, Half B itself not transcribed here) | direct ⚑ |
| | `09_Per_City_Baseline_Run.md` (§3.5) | rows 13, 14 (file named; L57 cited, §3.5 itself is in `Step_1_and_2.md` row 30) | direct ⚑ |
| | `11_Caloric_Rebuild_and_Livestock_Tier.md` | row 15 | direct |
| | `National_Medical_and_Care_Institutes.md` | rows 16, 17 | direct |
| | `National_Economy_and_Currency.md` | row 22 | direct |
| **Phase_5** — was 6 of 6 → **6 of 6 (6 direct)** (address counted per spine: Airports / Ports / Geothermal share one folder bullet; all three files are named) | Universe repo `Worldspace/Locations/` | row 29 (`…/Worldspace/Locations/`, label "Universe repo") and row 30 | direct ⚑ (abbreviated path) |
| | `Highways.md` | row 31 | direct ⚑ (FLAGGED table: existence/shape only, not extracted) |
| | `Airports.md` · `Ports.md` · `Geothermal_Heating.md` | rows 32 · 17 · 23 | direct (Airports ⚑ as Highways) |
| | `City_Cross_Subnet_Relationships.md` | row 35 | direct ⚑ (FLAGGED) |
| | `City_Relationship_Database.md` | rows 19, 20, 22, 33 | direct |
| | `City_National_Connections.md` | row 34 | direct ⚑ (FLAGGED) |
| **Phase_6** — **5 of 5 (5 direct)** | `Factions/Robot_Religions/` | row 11 (`…/Cymatics_reverence/Cymatics_reverence.md`), row 17 (Tier U) | direct |
| | `National_Holidays.md` | row 13 | direct |
| | `Ice-Cold_Buddhism_Research/` | row 14 | direct |
| | `The_True_Believer_Extraction.md` | row 15 | direct |
| | `The_Meme_Machine_Extraction.md` | row 16 | direct |
| **Phase_7** — **13 of 13 (11 direct, 2 via)**, split unchanged | `Division_of_Industry/` (README first) | row 52 (`Division_of_Industry/README.md`) | direct |
| | `16_Per_City_Three_Tier_Run.md` | rows 24–35 | direct |
| | `Division_of_Industry_Sweep_2026-08-31.md` | rows 46–48 | direct |
| | `01_Burden_Scoring_Model.md` | rows 36–38 | direct |
| | `08_Volume_Based_Requirement_Reference.md` | rows 39–44 | direct |
| | `National_Medical_and_Care_Institutes.md` | no row; the cited `Division_of_Industry_Reliability_Quick_Reference.md` L86 names it | via Tier U |
| | `Theoretical-Calculations/` | row 49 | direct |
| | `Industry_Staffing_and_Productivity/` | row 50 | direct |
| | `jobs_professions_and_fields/` | row 50 | direct |
| | `National_Economy_and_Currency.md` | no row; the same Tier U sheet L126 names it | via Tier U |
| | `City_Logistics.md` | row 51 | direct |
| | `Factions/` | rows 53–55 | direct |
| | `Megacorps/` | row 50 | direct |
| **Phase_8** — **2 of 2 (2 direct)** | `Robot_Biology_and_Culture/` | row 13 | direct |
| | `Weapons_and_Tools_Philosophy.md` | row 11 | direct |
| **Phase_9** — was 4 of 4 (3 direct, 1 via) → **3 of 4 (2 direct, 1 via)** | `Laws_of_Robotics.md` | **not covered**: row 12 transcribes the two laws but names neither the file nor a shared sheet that carries it (its citation, `Robot_Physiology_Quick_Reference.md`, contains no laws; no Tier U sheet does) ⚑ | not covered |
| | `Robot_Universals/` | rows 11, 13, 14 | direct |
| | `Doll_Representation_Categories.md` | row 15 | direct |
| | human-robot baseline (`Robot_Physiology_and_Cultural_Practices.md`) | rows 12–14 cite the Tier U sheet that names it (row 16 cites `Step_0.md` only) | via Tier U |
| **Phase_10** — was 3 of 3 (3 direct) → **3 of 3 (2 direct, 1 via)** | `TepenianUniverseTimeline/Worldspace/Characters/` | row 11 | direct |
| | `Enneagram_Character_Index.md` | row 16 | direct |
| | `Zodiac_Signs_Full_Attributes.md` | row 17 cites `Zodiac_Signs_Quick_Reference.md`, whose L3–4 name `Reference/Real-World/Zodiac_Signs_Full_Attributes.md` (wrapped across two lines) | via Tier U ⚑ |

Headers in the sheets now read: Step_0 3 of 3 · Step_1_and_2 **4 of 6** (names the two uncovered) · Phase_2 3 of 3 · Phase_3 **3 of 4** (names the uncovered one) · Phase_4 7 of 7 · Phase_5 6 of 6 · Phase_6 5 of 5 · Phase_7 13 of 13 · Phase_8 2 of 2 · Phase_9 **3 of 4** (names the uncovered one) · Phase_10 3 of 3.

---

## 3 · New findings (not in the ledger; described, not fixed unless inside an entry)

1. **`16` upper-case section / SH-013 (NEEDS-DEVELOPER).** The city's own determination is `## 23. ✅ VOSTOK — DETERMINED`, `16` L2349 (a name search for "Ariun" misses it; the sheets key it by "Vostok"). Its heading is now in both Pre-Trip `16` lists and marked. The sheets already carry §23 beside Half B and say it supersedes. Question for the developer: confirm nothing more is wanted (for example a Tier-U-style line saying §23 governs).
2. **`09` L201 still carries the pre-`DR-68` figure.** The §3.6 "COMPLETE" table row reads `Vostok | 41.5% | 42.8% | +1.3`; `09` L1 says only the §2 cells were refreshed. That is where the sheets' old "41.5%" came from. Source-level; not touched. (The sheets cite L57, which is right.)
3. **`Phase_9.md` row 12 (Laws of Robotics) cites the wrong sheet.** It transcribes the two laws (they match `Laws_of_Robotics.md` L1–3 in the timeline repo) but cites `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md`, which contains no laws; no Tier U sheet does. Fix would be to cite `Laws_of_Robotics.md` by name (not done; not in the ledger; it would raise Phase 9 to 4 of 4).
4. **`Step_-1.md` "Real-world basis" row cites spec L5 for "Southern Pole of Inaccessibility".** Spec L5 holds only "Vostok Station (USSR / Russia), East Antarctic Plateau (~78°28'S, 106°52'E)"; the phrase is at L49 (and "the Pole of Inaccessibility" at L138). The audit repeats "L5, L49". Not changed (not in the ledger).
5. **Rows missing for must-open addresses (gaps for the developer to decide, not filled):** `Step_1_and_2.md` — Universe repo `Worldspace/Locations/` (location canon) and `Reference/Real-World/Stations/` (both are carried in `Step_0.md` rows 21–22, i.e. in the Phase 0 sheet); `Phase_3.md` — the climate `READER/` folder (row 11 is a cross-reference only); `Phase_9.md` — `Laws_of_Robotics.md` (see 3).
6. **Meta row left as is (§4a):** `Phase_3.md` row 11 says the climate address is "Already fully extracted — see `Step_1_and_2.md`, cross-referenced"; with the recount it no longer matches the Phase 3 header ("not named here").
7. **Pre-Trip §I is a dated build record** (2026-10-21): "TOTAL=183 …", "114 claims · 114 OK", "template: Casey's sheet, 579 lines" describe the file as built, not as it now stands (two rows added, 5 lines longer). Left as the record; no note added (none asked).
8. **Ledger line numbers:** AN-S03 says spec "L77"; the phrase "#2 coldest of the 37" is on **L76**. No other mismatch between ledger and live source was found (every REPOINT anchor landed where the ledger said).
9. **Tiny source rounding:** `16` L2357 states "Distinctive tier: 203,100 (62.6%)"; its table gives 66,007 + 137,092 = 203,099. The sheets quote 203,100 as the source does. No action.
10. **Counts to refresh if the developer later renames inside the sheets (AN-008):** the Phase 3 / Step 1 quotes (AN-024) and the "N-line" counts (AN-025, 027, 031) are the only rows waiting on DECIDE entries.

## 4 · Files edited (all by the Edit tool)

Pass folder `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/`:
- `00.0_Pre-Trip_Inspection.md` (566 → 571 lines)
- `README.md`
- `Datasheets/Step_0.md` · `Step_1_and_2.md` · `Step_6.md` · `Step_7.md` · `Step_8.md` · `Step_9.md` · `Step_10.md`
- `Datasheets/Phase_2.md` · `Phase_3.md` · `Phase_4.md` · `Phase_5.md` · `Phase_6.md` · `Phase_7.md` · `Phase_8.md` · `Phase_9.md` · `Phase_10.md`

Not edited (no entry touched them, or DECIDE): `Datasheets/Step_-1.md`, `Step_3.md`, `Step_5.md`, `00.2_Position_Coverage_Ledger.md`. New file: this report. Nothing outside the pass folder was changed; nothing committed; `git diff --stat` for the folder shows 18 files, 68 insertions, 55 deletions.
