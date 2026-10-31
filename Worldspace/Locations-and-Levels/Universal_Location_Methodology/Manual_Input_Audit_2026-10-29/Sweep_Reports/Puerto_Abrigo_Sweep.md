# Puerto Abrigo — sweep report (2026-10-30)

**City:** Puerto Abrigo (formerly Port Lockroy; ledger section B31; pass folder `PASSES/Palmer_Subnet/Puerto_Abrigo`).
**Who:** sub-agent (Claude), one city, edits by the Edit tool only; nothing committed, no generator run, no `--force`, no `sed -i`.
**Read:** `SWEEP_BRIEF.md` (all, incl. §4a); `FIX_LEDGER.md` section A (SH-001 … SH-023) and `### B31`; `Puerto_Abrigo_Audit.md`; the whole Pre-Trip (567 lines), `README.md`, `00.2_Position_Coverage_Ledger.md` and all 19 datasheets; every cited live source line named below. **Not opened:** megasheets, the city's culture / robot-culture / Enneagram / vision-note / symbol files, the Background-Lore vignettes (Phase 3 / §F only record their existence). The GDD `Worldspace/Characters/` tree was searched for file names and line numbers only (PA-008); no file in it was read.

Shared sources re-read live for this sweep: `03_The_Phase_Spine.md` (L127, L220, L1114, L1140; the eleven `📂 MUST OPEN` blocks), `00_RUNBOOK.md` (L1982, L2178–2180, Step 10 L3057–3152, `# Where everything lives` L3153), `02_Generators_Capability_and_Symbols.md` (L610, L636–637), `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` (L620–643, L667–684), `Extent_and_Density_Per_City.md` (§4 L105–L160, L631, L705), `Upper_Earth_Immigration_Composition.md` (L21–L63, L210–L218), `16` (L1, L6, L27–L32, L241–L248, L281, L1287–L1305, L1612–L1673), `09` (L1, L5, L50–L52, L77, L246–L266), Airports, Ports, Highways, RelDB, NatConn, CrossSub, Precipitation, the census, the Register, and the Tier U sheet headers.

## Tally

| Result | Count | Which |
|---|--:|---|
| APPLIED | 26 | PA-001, 003, 004, 005, 007, 008, 020, 021, 022, 025, 026, 028, 029, 030, 031 · SH-001, 002, 003, 004, 005, 008, 010, 011, 012, 013, 014 |
| PARTIAL | 1 | PA-023 (row 15 and row 31 done; row 30 left on purpose) |
| ALREADY-RIGHT | 1 | SH-006 (the sheet cites no runbook line for the `Status:` rule) |
| HELD | 2 | SH-007, SH-009 (brief §3: leave as is) |
| SKIPPED-MISMATCH | 0 | (no change was refused; five places where the live text or range differs from the ledger's wording were written as seen live and are listed under "Where the live text differed") |
| NEEDS-DEVELOPER | 2 | the Kyoto pick's tail clause (PA-020); the Phase 7 "13 of 13 on disk" meta row against brief §4a (PA-029) |
| Not touched (DECIDE / SOURCE / NOTE) | 11 | PA-002, 006, 024, 027 (DECIDE) · PA-S01, S02 (DECIDE/SOURCE) · PA-S03 … S07 (NOTE) |

## Results

`PASS` = `…/City_Development_Passes/Palmer_Subnet/Puerto_Abrigo`. "Pre-Trip" = `00.0_Pre-Trip_Inspection.md`.

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| PA-001 | APPLIED | Pre-Trip §C Step 2, §D Phase 1 / Phase 5, §E | Airports L48 → **L51**; Ports L484, 512, 710, 728–729, 803 → **L507, L535, L733, L751–752, L826, +L859**; RelDB L123, 213, 350–351, 356–357, 384, 501 → **L134, L224, L361–362, L367–368, +L370, L395, L512** (entry L367–L377); NatConn L353, L446 → **L354, L451**; `16` row L280 → **L281**, others → **L184, L356, L439, L1636–1637, L1642, L1652, L1715, L1750, L3567, +L1612 (§14 heading), +L1663**; Extent **+L105, +L132**; Precipitation **+L175** (`Port_Lockroy`); Highways, CrossSub, census, Register, `09` L77, Topics left as they are | live `grep -n -i` (names, upper case, underscore, bare `lockroy`/`abrigo`) in each file; every hit opened. Two extra hits found by the bare half-name search and added with a note ⚑: Airports **L44–L45** and `16` **L1511–L1512** (the name wraps across the line break). The Ports L752 line, `16` L1512 and Airports L45 were opened to confirm they are this city |
| PA-002 | DECIDE — not touched | Pre-Trip | the Pre-Trip's `09` L77 / `16` L281 cites are not labeled | — |
| PA-003 | APPLIED | Pre-Trip §C intro, §J | "(**not yet built** — November item N-5 …)" → "(**19 files, all present**)"; §J row "Datasheets not yet built for this city" **deleted**; §I left as the dated build record (it still reads `DATASHEET-NOT-YET-BUILT(N-5)=20`) as the entry says | `ls Datasheets/` = 19 files |
| PA-004 | APPLIED | Pre-Trip §J rename row | "… keep the old name by design (nothing was moved)" → pass and concept-art folders are `Puerto_Abrigo/`, as are the culture / robot-culture / Enneagram / vision-note files; only `City_Megasheets/Palmer_Subnet/Port_Lockroy/` and the climate READER key `Port_Lockroy.md` keep the old name | `ls`: pass, concept-art, `Specs/Palmer subnet/`, `Local_Cultures`, `Local_Robot_Culture`, `City_Enneagram_Personalities`, `City_Vision_Notes` all `Puerto_Abrigo*`; `City_Megasheets/Palmer_Subnet/Port_Lockroy` and `READER/Port_Lockroy.md` still old |
| PA-005 | APPLIED (range differs, see below) | Pre-Trip §C Step 0 `T8` reads | "Puerto Abrigo's rows **56**, **651**" → the resolved extent **§4 (heading L105; table L114–L119; "no spanning to Wiencke Island was needed" L137; §4 runs L105–L160)** with the snapshot label; L56 / L651 kept as "earlier state, superseded by §4"; L105, L132 added to the other-lines list. §D Phase 0 has no extent row, so nothing to change there | Extent L56, L105–L160, L651, L631 re-read |
| PA-006 | DECIDE — not touched | Pre-Trip §A | alias set | — |
| PA-007 | APPLIED | `README.md` | title and the four pointers → `Puerto Abrigo`, `../../../Specs/Palmer subnet/Puerto_Abrigo.md`, `…/Local_Cultures/Palmer_Subnet/Puerto_Abrigo.md`, `…/City_Vision_Notes/Puerto_Abrigo.md`, `…/Research_Logs/Puerto_Abrigo_Research_Log.md` (still "may not exist yet": `ls Research_Logs` has no such file) | `ls` of each target (the log does not exist, as the README already says) |
| PA-008 | APPLIED | Pre-Trip §D Phase 10, "Characters" row | added the GDD tree's **10 files** (file names and line numbers, not read): Methodology seed L104; Imelda Sánchez ×4 (README L24, L216; Timeline L24; War_Experiences L5, L7, L19; Questlines/README L27); Calethina ×5 (README L49, L75, L80, L94; Play-by-Play L65, L67, L68, L69, L80, L121; UNMARKED L16; Player_Chamber DRAFT L26, L33; Substrate_Transfer L119) | `grep -rl -i` + `grep -o` over the GDD tree = 10 files, matches the ledger's "Imelda ×4, Calethina ×5, a Methodology seed". The universe repo's tree (2 files) was not re-run; the entry says it is right |
| PA-009 | pointer | — | shared items | see SH rows |
| PA-020 | APPLIED ⚑ | `Datasheets/Step_3.md` | section "L249–L255" → **L280–L285** (heading L280); picks L250–254 → **L281–L285**; L282 flagged "an empty slot: the line names no pick"; the Kyoto pick (L284) now copied instead of excluded — **but its tail clause withheld** (see NEEDS-DEVELOPER) | script check: each copied pick is a substring of its live line (L281, L283, L285 exact; L282 exact; L284 first 229 of 298 characters) |
| PA-021 | APPLIED (label option; PA-002 / PA-S01 stay DECIDE) ⚑ | `Step_1_and_2.md` (row 34), `Phase_4.md` (`09` row, `16` row), `Phase_7.md` (row 1) | quoted `09` L77 and `16` Half B rows kept as the live source reads, now repointed to **L281**, each carrying "the Workforce is on the pre-Gate 11 population (Census I 63,338 H / 65,549 R / 128,887: Extent L116); Census I now reads 457 H / 472 R / 929 (census L516)"; `src` H quoted from its legend (`16` L244–L245); **new row for §14** (L1612–L1669: baseline 39,879 / 41.0%, mandated 2,867 / 2.9%, FREE 54,472 / 56.0%, distinctive 57,339 / 59.0%, the courier-node mandate = 5% of the distinctive tier, the post-office question settled) saying the counts sit on the pre-Gate 11 workforce and that §14 supersedes Half B; **new computed row** "workforce on the current Census I = 472 + 0.5 × 457 = 700.5 (≈ 701)" with the formula cited (`09` L5, L259). In `Phase_4.md` the `09` row also says `16` discards the Required and % WF columns (`16` L28–L32) | arithmetic below; every cited line re-opened (see list under "Hand arithmetic") |
| PA-022 | APPLIED | `Phase_5.md` | Airports **L51**; Ports **L507, L535, L733, L751, L752, L826, +L859**; RelDB entry **L367–L377**, lines **L368 / L369 / L370 (excluded) / L371 / L372 / L373 / L374 (excluded)**; NatConn "8 line(s)" **L354, L451**; Airports also **L44–L45** ⚑ | script check: every quoted Ports / Highways / RelDB value is a substring of its live line, except the pre-existing Ports L176 text (see New findings) |
| PA-023 | PARTIAL | `Step_1_and_2.md` | row 15 completed with spec L98–L99 ("Proxy station: `Palmer` — BAS READER, 1991–2020 WMO standard normal, 30 years; full record 1976–2026", "~27 km" cited from L129); row 31 labelled "PROXY: `Palmer` Station values, unmodified (1991–2020 WMO normal)", cited READER L20, L22, L24, L26. **Row 30 left:** it is the site's own climate authority (READER L7, "UKAHT … no continuous climate record"); the label "Palmer Station values" would misstate it | spec L98–L99, L105, L129; READER L3, L7, L12–L22 |
| PA-024 | DECIDE — not touched | `Phase_5.md` | RelDB care-note | — |
| PA-025 | APPLIED | `Phase_7.md` | `16` "other lines" row: "10 line(s)" → "14 line(s): L184, L356, L439, L1511–1512, L1612, L1636–1637, L1642, L1652, L1663, L1715, L1750, L3567" | live `grep -n -i` of file 16 |
| PA-026 | APPLIED | `Step_0.md`, `Step_1_and_2.md` | new extent row from Extent §4: 0.024 km² (200 m × 120 m), Census I / II, 38,708/km², 25.8 m², "no spanning to Wiencke Island was needed", snapshot label; L56 and L651 named by line number only as earlier-state rows. The comparison "0.84× Manila" and "4.3× Kowloon" were not copied (no comparisons in a row) | Extent L114–L119, L129, L137, L705; arithmetic below |
| PA-027 | DECIDE — not touched | `Step_10.md` etc. | "N-line file" counts | — |
| PA-028 | APPLIED ⚑ | `Phase_2.md` | the second copy of each annotation row deleted (spec L65, census L104); 28 → 26 lines before the SH-010 rows | spec L65 and census L104 re-read: each line carries `(founding wave)` twice (Argentina, Chile) — see New findings |
| PA-029 | APPLIED ⚑ | `Phase_7.md` | header → "8 of 13" (recounted); the last row "exist on disk: 11 of 11" → "**13 of 13** *(re-checked by `ls` 2026-10-30)*" | `ls`/`test -e` on all 13 spine addresses: all exist. The two counts now measure different things and no longer collide |
| PA-030 | APPLIED | `Phase_8.md` | term-check row: "dress … 1 hit" now says L115 "clothing material" (2026-09-04 climate correction note); "craft … 1 hit" says L203 "small-craft maritime activity" | spec grep: dress/clothing/attire only L115; craft only L203; cuisine/food/dish/drink and music none |
| PA-031 | APPLIED | `Step_1_and_2.md`, `Phase_4.md`, `Phase_7.md` | "(now Puerto Abrigo, `DR-40`)" added once per sheet beside the first quoted "City: Port Lockroy" (Step_1_and_2 row 34; Phase_4 `09` row; Phase_7 row 1) | — |
| SH-001 | APPLIED | Pre-Trip §G | spine **L127 → L220, L1114, L1140** with the three anchor phrases (the rest of the row, runbook L1982, unchanged) | spine L220 "and the no-invented-person-names rule"; L1114 "NO INVENTED PERSON NAMES — role placeholders permanently"; L1140 "People as role-archetypes — binding rule: no invented proper names"; runbook L1982 is the Phase 10 row |
| SH-002 | APPLIED | Pre-Trip §G | runbook **L2178 → L2180** ("THE DIVERGENCE OPERATOR") | `grep -n` = L2180 |
| SH-003 | APPLIED | Pre-Trip §C Step 5 | §5.3 "lines 610–684" → **610–636** | 02 L610 "## 5.3", L637 "# 6. Symbol binding" |
| SH-004 | APPLIED | Pre-Trip §C items 4 and 5 | item 4 "620–643 and 701–703" → **620–643 (the four questions) and 682–684 (the fifth section)**; item 5 "650–703" → **667–684** (the box "AMENDED 2026-09-28 — THE WRITTEN CONTENT IS A MERGE, NOT A PICK") | TRIAL L620–643 (Round 3 prompt), L682–684 ("Round 3's prompt now carries a fifth section"), L667–684 |
| SH-005 | APPLIED | Pre-Trip §C Step 10 | "3057–3172" (twice) → **3057–3152**; card note "live lines 3045–3161 govern" → **3057–3152 govern** | runbook `# Step 10` L3057, `# Where everything lives` L3153 |
| SH-006 | ALREADY-RIGHT | `Step_-1.md` | the row "Specs `Status:` field" cites no runbook line (it says "`00_RUNBOOK.md`, the Second Interwar default"); no L1821–1822 anywhere in the pass folder | `grep -rn 1821 1822` over the pass folder |
| SH-007 | HELD | — | brief §3. (No `01` "line 65" cite exists in this city's sheets anyway: `Step_10.md` cites only `06` "(430 lines)".) | `grep` |
| SH-008 | APPLIED | all 11 datasheets that carry the header | recounted by hand; see the recount tables. Four headers now read k < N | — |
| SH-009 | HELD | — | brief §3. The "245-line", "246-line" … counts are untouched | — |
| SH-010 | APPLIED | Pre-Trip §D Phase 2; `Phase_2.md` | two rows added (the city's own section L210–L218, heading L210; the solar-UTC rule: heading L21, list L26–L33, rule 1 L28, refinement box L35–L63). In the Pre-Trip they are "⏸️ registered, not dispatched" and the `T8` line keeps "the 3 admissible rows" (the phase's MUST-OPEN text does not name the file), the same form as Santa Luce's Pre-Trip | composition file L21, L26, L28, L32–L33, L35, L63, L210–L218 re-read; form copied from Santa Luce / Relung Panen (form only) |
| SH-011 | APPLIED | Pre-Trip §C Step 0, §E; `Step_0.md`, `Step_1_and_2.md` | "(2026-09-05 snapshot; the census is live — note L631)" beside the Extent citations | L631 re-read: still the "Snapshot note, 2026-10-28 … the census is the live source" (see New findings for what it is attached to) |
| SH-012 | APPLIED | Pre-Trip, `Phase_5.md`, `Phase_7.md` | all the stale `16`, Airports, Ports, RelDB, NatConn lines (PA-001 / PA-022 / PA-025) | live re-reads |
| SH-013 | APPLIED | Pre-Trip §D Phase 1 and §E; `Step_1_and_2.md`, `Phase_4.md`, `Phase_7.md` | `16` §14 heading **L1612** listed (marked "the city's own upper-case heading"); the shares 41.0 / 2.9 / 56.0 quoted beside Half B's (identical to Half B's, so they agree), with "§14 supersedes" | `16` L1612–L1669 |
| SH-014 | APPLIED | `Step_1_and_2.md`, `Phase_4.md`, `Phase_7.md` | "On the flat ABCC working value; counts re-run when per-city ABCC values are set (`16` L1287–L1304)" on every quoted `16` baseline % / count (Half B row and §14 row in each sheet) | live: the CONSEQUENCE block is L1287–L1304 (L1305 blank, L1306 is the next heading); I cite what I saw, per brief §4a |

### Where the live text differed from the ledger's wording (written as seen live)
1. **Extent §4 range.** Ledger (PA-005, PA-026, D-07): "§4 (L105–131)". Live: §4 starts L105 and runs to L160 (next section `# 5` at L164); the figures are L114–L119 and L137. Cited those.
2. **`16` §14 range.** Ledger (PA-021): "L1612–1675". Live: §14 is L1612–L1669; its closing rule is L1671 and §15 starts L1673. Cited L1612–L1669.
3. **SH-014 range.** Brief: "L1287–1305". Live: L1287–L1304.
4. **PA-001 "RelDB L367–L377".** Live: entry heading L367, lines L368–L374, a separator at L376; the 11-line shift is exact, so the ledger's range was kept.
5. **PA-028.** The ledger calls the rows "duplicate annotation rows". The source lines hold two annotations each (see New findings); the deletion was still made as the entry directs.

## Hand arithmetic (every figure re-derived from the live lines; ratios to five decimals before rounding)

**Population (census L516, L636; Extent §4 L116–L117; spec L25–L26).** 457 + 472 = 929 ✓. 387 + 304 = 691 ✓. 128,887 − 929 = 127,958 ✓ (the held overflow, Extent L144). Retention: 691 ÷ 929 = 0.74381 → 74.38 %; 387 ÷ 457 = 0.84683 → 84.68 %; 304 ÷ 472 = 0.64407 → 64.41 % (`Step_0`, `Phase_2` already right). Robots' share 472 ÷ 929 = 0.50807 → 50.81 % (`Phase_9` already right).

**Extent (Extent L116–L119, L129, L705).** 200 m × 120 m = 24,000 m² = 0.024 km² ✓. 929 ÷ 0.024 = 38,708.33 → **38,708/km²** ✓. 128,887 ÷ 0.024 = 5,370,291.67 → 5,370,292/km² ✓ (L56's figure, the earlier state). 24,000 ÷ 929 = 25.83423 → **25.8 m²** per person ✓.

**Workforce (formula `robots × 1.0 + humans × 0.5`: `09` L5, L259; `16` L27).**
- Old, as `09` L77 / `16` L281 print it: 65,549 + 0.5 × 63,338 = 65,549 + 31,669 = **97,218** ✓ (so those two rows are on the old population, not mistyped).
- Current: 472 + 0.5 × 457 = 472 + 228.5 = **700.5** (≈ 701).
- Ratio old ÷ current = 97,218 ÷ 700.5 = **138.78372** (the "~139×"); 128,887 ÷ 929 = 138.73735.

**`09` L77 "Required" and "% WF" (not carried into the sheets; `16` L30–L32 discards both columns).** `Required = Humans × (53·D + 85.6)/1000 + Residents × (64·D + 113.2)/1000` (`09` L50), D = 1.25: human coefficient (66.25 + 85.6)/1000 = 0.15185; resident coefficient (80 + 113.2)/1000 = 0.1932. Old: 63,338 × 0.15185 = 9,617.8753; 128,887 × 0.1932 = 24,900.9684; sum 34,518.8437 → **34,519** ✓ (L77). Current: 457 × 0.15185 = 69.39545; 929 × 0.1932 = 179.4828; sum 248.87825 → **≈ 249**; % WF = 248.87825 ÷ 700.5 = 0.35529 → 35.5 % (old 34,519 ÷ 97,218 = 0.35506 → 35.5 %) — the ledger's "≈ 249" and "35.5 %" are right, and the sheets say only that the row is on the old population.

**`16` §14 (L1616–L1620, L1627).** 39,879 + 2,867 + 54,472 = **97,218** ✓ (so the §14 counts sit on the old workforce). 2,867 + 54,472 = 57,339 ✓. Shares: 39,879 ÷ 97,218 = 0.41020 (41.0 %); 2,867 ÷ 97,218 = 0.02949 (2.9 %); 54,472 ÷ 97,218 = 0.56031 (56.0 %); 57,339 ÷ 97,218 = 0.58980 (59.0 %). Mandate ÷ distinctive tier = 2,867 ÷ 57,339 = 0.05000 (5 %) ✓. **The three shares equal Half B's 41.0 / 2.9 / 56.0, so §14 and Half B agree on shares; only the counts differ in basis.**

**Scaling §14's counts to the current workforce (NOT written into any sheet).** Factor 700.5 ÷ 97,218 = 0.00720545. Baseline 39,879 × factor = 287.35; mandated 2,867 × factor = 20.66; FREE 54,472 × factor = 392.50 (sum 700.5). Whole workers: 287 / 21 / 392 (sum 700). The ledger's PA-S01 gives "≈ 287 / 20 / 393" and audit A-01 says "about 21" for the mandate; applying the printed shares (41.0 / 2.9 / 56.0 %) to 700.5 gives 287.2 / 20.3 / 392.3. The three methods differ by one worker in two cells, so no scaled sector count was put into a sheet; that waits for the PA-S01 decision.

**Source lines re-opened for the new rows:** `09` L5, L50, L52, L77, L259; `16` L27–L32, L244–L245, L247, L281, L1287–L1304, L1612–L1669 (table L1614–L1618, L1620, L1627, L1663–L1668); census L516, L636; Extent L105, L114–L119, L129, L137, L631, L705; READER L3, L7, L12–L26; spec L98–L99, L105, L115, L129, L203; Inspirational-Influences L280–L285.

## MUST-OPEN recount (SH-008)

N = the number of address lines in the `📂 MUST OPEN` block of that phase in `03_The_Phase_Spine.md` (read live; all eleven N's equal the sheets' old N, except that Phase 3 excludes `Davis_Geosciences_Research`, "where applicable: Davis only"). **Covered** = a row of the sheet names the address by full path or full file name; "via Tier U" = a row cites a `Corpus_Reference_Sheets/` sheet whose own header names the address. Header wording changed from "checked 2026-10-23" to "recounted by hand 2026-10-30" in every sheet below. `Step_-1`, `Step_3`, `Step_5` … `Step_10` carry no such header.

| Sheet (phase) | Old header | **New k of N** (direct / via) | Address → covering row |
|---|---|---|---|
| `Step_0.md` (0) | 3 of 3 (2/1) | **3 of 3 (2/1)** | `Repo_Scope.md` → row "**U** `Repo_Scope.md`"; `Timeline Eras/` → via Tier U `Second_Interwar_Period_Quick_Reference.md` (rows "Temporal frame", "Act structure", "consolidating mechanism"; its line 4 names `Timeline Eras/2 The Second Interwar Period/README.md`) ⚑; `Official_Population_Census.md` → rows "Census I", "Census II" |
| `Step_1_and_2.md` (1) | 6 of 6 (6/0) | **6 of 6 (6/0)** | `Worldspace/Locations/` (universe repo) → row "Universe repo `Worldspace/Locations/` — directory enumerated"; `Specs/` → rows citing `Specs/Puerto_Abrigo.md` ⚑; `Energy_Grid_Failure_Rationale.md` → its row; Climate `READER/` → rows citing `READER/Port_Lockroy.md` ⚑; `Stations/` → rows `Antarctic_Stations_With_Airstrips.md` and `COMNAP_Antarctic_Station_Catalogue.pdf` (no row names `Stations/` itself) ⚑; `16_Per_City_Three_Tier_Run.md` → Half B row and §14 row |
| `Phase_2.md` (2) | 3 of 3 (3/0) | **3 of 3 (1/2)** | `No_National_Stereotypes.md` → via Tier U `No_National_Stereotypes_Quick_Reference.md` (row "GPS law"; its line 4 names `Reference/No_National_Stereotypes.md`); `Falkland_Treaty/` → via Tier U `Falkland_Treaty_Quick_Reference.md` (three Falkland rows; its lines 3–4 name `Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md` and two siblings) ⚑; `Official_Population_Census.md` → rows "Census I/II", tier-table rows |
| `Phase_3.md` (3) | 4 of 4 (4/0) | **3 of 4 (3/0)** | **not covered:** Climate `READER/` (no row of this sheet names it; `READER/Port_Lockroy.md` is cited only in `Step_1_and_2.md`). Covered: `Specs/` → rows `Specs/Puerto_Abrigo.md` L88, L197, L216 ⚑; `City_Concept-Art/` → row "Concept-art directory status" (`City_Concept-Art/Palmer_Subnet/Puerto_Abrigo`) ⚑; `City_Megasheets/` → row "Megasheet Physical Infrastructure file" names the withheld file `Port_Lockroy_Physical_Infrastructure_Attributes.md` (the folder path itself is not given) ⚑. `Davis_Geosciences_Research` not applicable |
| `Phase_4.md` (4) | 7 of 7 (5/2) | **6 of 7 (4/2)** | `Robot_Physiology_and_Cultural_Practices.md` and `Robot_Cold_Physiology.md` → via Tier U `Robot_Physiology_Quick_Reference.md` (three rows; its line 3 names both); `16_…` → Half B and §14 rows; `09_Per_City_Baseline_Run.md` → its row; `11_Caloric_Rebuild_and_Livestock_Tier.md` → its row; `National_Medical_and_Care_Institutes.md` → its row. **Not covered:** `National_Economy_and_Currency.md` (named in no sheet of this city) |
| `Phase_5.md` (5) | 6 of 6 (6/0) | **5 of 6 (5/0)** | **not covered:** the universe repo's `Worldspace/Locations/` (location canon and routes; the only row naming it is in `Step_1_and_2.md`). Covered: `Highways.md` → rows L75, L80; the "Airports · Ports · Geothermal" bullet (address `Infrastructure/`) → rows `Airports.md`, `Ports.md` (nine rows), `Geothermal_Heating.md` ⚑ (counted as one address through its three files); `City_Cross_Subnet_Relationships.md`, `City_Relationship_Database.md`, `City_National_Connections.md` → their rows. (The `Arcanet.md` row is extra: the spine block does not list it.) |
| `Phase_6.md` (6) | 5 of 5 (5/0) | **5 of 5 (5/0)** | `Factions/Robot_Religions/`, `National_Holidays.md`, `Ice-Cold_Buddhism_Research/`, `The_Meme_Machine_Extraction.md`, `The_True_Believer_Extraction.md` → one row each (the mortuary line has no address) |
| `Phase_7.md` (7) | 13 of 13 (10/3) | **8 of 13 (7/1)** | Covered: `Division_of_Industry/` → via Tier U `Division_of_Industry_Reliability_Quick_Reference.md` (cited in the banner; its lines 3–5 name `…/Cities/Division_of_Industry/README.md`; the folder name also appears in the banner, and the row `README.md` L49 is a bare base name) ⚑; `16_…` → Half B, §14 and "other lines" rows; `Division_of_Industry_Sweep_2026-08-31.md` → five rows; `01_Burden_Scoring_Model.md` → row "status stamp in the folder README"; `Theoretical-Calculations/` → its row; `jobs_professions_and_fields/` → its row; `City_Logistics.md` → its row; `Factions/` → its row. **Not covered:** `08_Volume_Based_Requirement_Reference.md`, `National_Medical_and_Care_Institutes.md` (only in `Phase_4.md`), `Industry_Staffing_and_Productivity/`, `National_Economy_and_Currency.md`, `Megacorps/` (universe repo) |
| `Phase_8.md` (8) | 2 of 2 (2/0) | **2 of 2 (2/0)** | `Robot_Biology_and_Culture/` → row "`Robot_Biology_and_Culture/` mandatory facts"; `Weapons_and_Tools_Philosophy.md` → its row |
| `Phase_9.md` (9) | 4 of 4 (3/1) | **3 of 4 (2/1)** | `Robot_Universals/` → its row; `Doll_Representation_Categories.md` → its row; `Robot_Physiology_and_Cultural_Practices.md` → via Tier U `Robot_Physiology_Quick_Reference.md` (three rows). **Not covered:** `Laws_of_Robotics.md` — the row headed "Laws of Robotics (Tier U)" transcribes its two laws but names no file, and the Tier U sheet it cites (Robot Physiology) neither contains nor names them ⚑ |
| `Phase_10.md` (10) | 3 of 3 (3/0) | **3 of 3 (2/1)** | `Worldspace/Characters/` (universe repo) → row "Characters canon (`TepenianUniverseTimeline/Worldspace/Characters/`)"; `Enneagram_Character_Index.md` → its row; `Zodiac_Signs_Full_Attributes.md` → via Tier U `Zodiac_Signs_Quick_Reference.md` (its lines 3–4 name `Reference/Real-World/Zodiac_Signs_Full_Attributes.md`) |

⚑ **Recount judgment calls.** (a) A *directory* address counted as covered when a row cites a file inside it by full file name or `Dir/File` form: `Specs/`, Climate `READER/`, `Stations/` (Step_1_and_2), `City_Concept-Art/` and `City_Megasheets/` (Phase_3), `Infrastructure/` (Phase_5). If the developer rules that a directory is covered only when a row names the directory itself (not a file inside it), the affected sheets are `Step_1_and_2.md` (`Specs/`, `READER/`, `Stations/`), `Phase_3.md` (`Specs/`, `City_Concept-Art/`, `City_Megasheets/`) and `Phase_5.md` (`Infrastructure/`), and their "not covered" lists would grow by those addresses. (b) "Via Tier U" counted when the Tier U sheet's header names the source with a path that includes the address, even with an ellipsis prefix (`Timeline Eras/…`, `Falkland_Treaty/…`, `…/Division_of_Industry/README.md`). (c) The meta row at the bottom of `Phase_7.md` ("exist on disk") was reworded under PA-029; see the tally.

## New findings (not in the ledger; described, not fixed unless inside an entry)

**Rows missing for must-open addresses (gaps for the developer to decide on):**
- `Phase_3.md`: Climate `READER/`.
- `Phase_4.md`: `National_Economy_and_Currency.md`.
- `Phase_5.md`: the universe repo's `Worldspace/Locations/`.
- `Phase_7.md`: `08_Volume_Based_Requirement_Reference.md`, `National_Medical_and_Care_Institutes.md`, `Industry_Staffing_and_Productivity/`, `National_Economy_and_Currency.md`, `Megacorps/`.
- `Phase_9.md`: `Laws_of_Robotics.md` (see the next item).

**Other findings.**
1. **`Phase_9.md` "Laws of Robotics" row cites the wrong file.** It prints the two laws and cites `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md`; that Tier U sheet does not contain them (`grep -i "Laws of Robotics\|Laws_of_Robotics"` = no hit). The text is `TepenianUniverseTimeline/Reference/Laws_of_Robotics.md` L1–L2 (with small wording differences: the source says "the full capacity" and "it is also realistically possible"). The row's citation should be that file. Not fixed.
2. **`Phase_5.md` Ports L176 row quotes the old name.** The sheet reads "(Port Lockroy on day 5 of an operator log)"; live `Ports.md` L176 now reads "(Puerto Abrigo on day 5 of an operator log)". Line number is right; the quoted text is stale. Not in PA-022, so not changed.
3. **Line-wrapped names escape every name search.** Found: `Airports.md` L44–L45 ("Port" / "Lockroy" in the list of six cities that were in "and others"), `16` L1511–L1512 (Marambio's Notes), and `Division_of_Industry_Sweep_2026-08-31.md` L60–L61 ("Port" / "Lockroy's real-world basis"). The first two were added to the Pre-Trip and sheet lists (inside PA-001 / PA-022 / PA-025) ⚑; the Sweep one was **not** added (`Phase_7.md` lists Sweep L52, L128, L175, L188, L245; no entry covers it). Worth a line in the alias work (PA-006).
4. **PA-028's "duplicates" were two annotations each.** Spec L65 and census L104 both read "Argentina *(founding wave)*, Chile *(founding wave)*", so the generator wrote one row per annotation. After the deletion, `Phase_2.md` has one annotation row per source and no longer says there are two.
5. **Stale "second-smallest / fourth-smallest" claims outside the spec:** `Ports.md` L752 ("canon calls Puerto Abrigo the Federation's second-smallest city") and `16` L184 ("Fourth-smallest city", on 63,338) repeat the old-population ranking that spec L17 (PA-S02) also carries; Extent L136 and spec L54 say it is now the smallest settlement. Source files, so for the developer's choice with PA-S02.
6. **`Upper_Earth_Immigration_Composition.md` later tables** still carry pre-Gate 11 figures for this city: L1004 (63,856 / 129,942), L1252 (53,703 / 95,906); L787, L839, L888, L1135 are older cap-working tables (457,000 / 100K / 65,000). Outside the city's own section (L210–L218, which is tier-only and has no numbers). Source level; no sheet cites them.
7. **SH-011's note L631 belongs to a different table.** L631 is the "Snapshot note, 2026-10-28" under the §10 table of the other 25 cities (L603–L628), which does not contain Puerto Abrigo; Puerto Abrigo's own §4 is dated 2026-09-05 in its heading. The label was applied as the brief directs; the wording "2026-09-05 snapshot; the census is live" is true of §4 as well.
8. **`Phase_10.md` is silent on the GDD Characters tree** (10 files). PA-008 names only the Pre-Trip row; the datasheet's "587 files … 2 name the city" refers to the universe repo's tree and is unchanged.
9. **Spine Phase 5 block's address for three files is one folder** (`Infrastructure/`), so "6 of 6" can be read as 6 or as 8 (`Highways`, `Airports`, `Ports`, `Geothermal_Heating`, three relationship files, `Locations/`). The count above uses the 6 address lines.
10. **The Pre-Trip's Phase 5 table lists `Arcanet.md`, which the spine's Phase 5 block does not;** it is labeled "named in the runbook's Phase 5 row". No change.
11. **§I of the Pre-Trip** still carries the 2026-10-21 counts (`RESOLVE=120`, `DATASHEET-NOT-YET-BUILT(N-5)=20`, "72 claims · 72 OK"); left as the dated build record per PA-003. Its "72 claims" no longer match the lists after this sweep.
12. **`16` L1 header (DR-68, 2026-10-28)** says the per-city determinations further down "were NOT recomputed" and that only cities changed in the Santa Luce scenario had Half B refreshed; that is why Puerto Abrigo's Half B (changed on 2026-09-05) still shows 97,218. Context for PA-S01.

## NEEDS-DEVELOPER

1. **PA-020, Kyoto pick (L284).** The ledger asks to copy the pick "as real-world history, wrongly excluded as later-era". The live line ends with a clause about this city itself ("the inverse of Puerto Abrigo's own *spared by mattering too little*"), which restates its later-era condition (what the Status field says). I copied the real-world part and wrote "*[tail clause excluded: it states the city's own later-era condition, outside the Second Interwar default scope; not copied]*". If the developer wants the whole line as written, it is one row to change.
2. **PA-029 against brief §4a.** §4a says "a meta row that restates a coverage count and now disagrees with the recounted header: leave it and report it". The ledger entry PA-029 (PENDING) says "make agree after SH-008 recount". I applied the entry: the meta row said "exist on disk: 11 of 11"; I verified all 13 spine addresses exist on disk and reworded it to "13 of 13 (re-checked by `ls` 2026-10-30)". To undo, restore "11 of 11" in `Phase_7.md` (last row).

## Held / not touched

- DECIDE: **PA-002** (Pre-Trip `09` / `16` rows are not labeled; the sheets are, through PA-021), **PA-006** (alias set), **PA-024** (RelDB care-note), **PA-027** (N-line counts), **PA-S01** (refresh `09` L77 / `16` L281 / §14 to the 929 city or label), **PA-S02** (spec L17 "second-smallest"). PA-S03 … S07 are NOTE.
- **PA-021 caveat.** I applied the *label* option, which keeps the sheets true whichever way PA-S01 goes; if the developer corrects `09` / `16` at source, the "pre-Gate 11" sentences in `Step_1_and_2.md` (row 34 and the next two rows), `Phase_4.md` (rows 1–3) and `Phase_7.md` (rows 1–2) have to be revisited.
- SH-007, SH-009 (brief §3). SH-015 … SH-019 are Tier U sheets (orchestrator).

## Files edited (14)

All under `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Palmer_Subnet/Puerto_Abrigo/`:
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

Not edited: `Datasheets/Step_-1.md`, `Step_5.md`, `Step_6.md`, `Step_7.md`, `Step_8.md`, `Step_9.md`, `Step_10.md`, and `00.2_Position_Coverage_Ledger.md` (no entry names it).

Created: this report, `AUDIT/Sweep_Reports/Puerto_Abrigo_Sweep.md`. No amendment-note file (Puerto Abrigo is not a finished city).
