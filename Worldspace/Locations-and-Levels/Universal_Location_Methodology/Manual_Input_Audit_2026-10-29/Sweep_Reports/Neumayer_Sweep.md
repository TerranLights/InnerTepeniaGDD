# Neumayer — fix-sweep report (2026-10-30)

**City:** Neumayer (ledger section **B11 · NEUMAYER**; pass folder `PASSES/Halley_Subnet/Neumayer`). **Who:** sweep sub-agent. **Date:** 2026-10-30.
**Read:** `SWEEP_BRIEF.md` in full (including §4a); `FIX_LEDGER.md` section A and `### B11 · NEUMAYER`; `Neumayer_Audit.md` in full; the Halley sweep report (as a model of form only); the whole Pre-Trip (565 lines), the pass `README.md`, `00.2_Position_Coverage_Ledger.md`, all 19 datasheets; every live source line named below (re-opened before writing). The megasheet folder was only counted (`ls | wc -l`, `find -type f` / `-type d`; names not read); Local Culture, Enneagram, vision notes, Background-Lore and the symbol files were **not** opened. Of `16`, only Neumayer's own section (L481–L512) was read, to describe it in New findings 1.
**Method:** Edit tool only; no `sed -i`, no generators, nothing rebuilt, nothing committed. After the edits every changed row was re-checked by read-only comparison: the Pre-Trip "Names Neumayer at" lists, the `16` lists (Pre-Trip Phase 1 row, §E row, `Phase_7` row 17) and the `Phase_7` count were parsed and compared as sets with a live `grep -n -i neumayer` of each file (listed-not-live = none, live-not-listed = none, for all of: `16`, `09`, `11`, Highways, Airports, Ports, CrossSub, RelDB, NatConn, Robot Physiology, Stations); every `Highways` / `Airports` / `Ports` / `RelDB` row of `Phase_5` was compared with its live line; the `Step_3` picks were compared text-for-text with `Inspirational-Influences.md` L195–L202; `git diff` of all 14 changed files was read word by word (only intended changes appear).

**Totals:** APPLIED **19** (9 ledger entries + 10 shared fixes) · ALREADY-RIGHT / not present **1** (SH-006) · HELD **2** (SH-007, SH-009; neither text is present except the "N-line" counts) · DECIDE entries left untouched **6** (NM-003, NM-024, NM-026, NM-027, NM-028, NM-029) · NOTE entries left untouched **2** (NM-S01, NM-S02) · NEEDS-DEVELOPER **1** (SH-013, New findings 1) · SKIPPED-MISMATCH **0**.

---

## 1 · Entry table

### Ledger entries for Neumayer

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| NM-001 | APPLIED (Ports L176 kept — see NM-003) | `00.0_Pre-Trip_Inspection.md` (§C Step 2; §D Phase 1, 4, 5 rows; §E) | Every "Names Neumayer at" list regenerated from a live `grep -n -i`. **`16`**: Neumayer's row L272 → **L273** (Step 2 `T8` line; Phase 1 row; §E); other-lines list 17 → **18 lines**: L80, 114, 185, 222, 231, **481** *(new, the city's own upper-case heading — see New findings 1)*, 496, 503–504, 510–511, 523, 540, 580, 593, 678, 1866, 3382 (old L491, 498–499, 505–506, 518, 535, 575, 588, 673, 1861, 3377 re-pointed). **`09`**: L99, 114, 151, 178, 196, 239, 252 → **L101, 116, 153, 180, 198, 241, 254**, plus **L160** (new, see New findings 8); L54 unchanged. **Highways**: L238, 240, 242, 267, 285 → **L239, 241, 243, 268, 300** (L66, 116, 121 unchanged). **Airports**: L48, 52 → **L51, 55**. **Ports**: L535, 712, 836 → **L558, 735, 859** (L103, 176, 182, 245 unchanged; L176 kept, its removal is NM-003, DECIDE). **RelDB**: L121, 334–335, 341, 396, 439, 518, 529 → **L132, 345–346, 352, 407, 450, 529, 540** (L23, 31–32, 47, 74 unchanged). **NatConn**: L313, 366, 489, 548 → **L314, 367, 494, 553** (other 11 unchanged). **Robot Physiology**: **L369 added** (L412, 438 unchanged). `CrossSub` L204, `11` L328, Stations L39: unchanged. | Live `grep -n -i "neumayer"` on each file; Pre-Trip lists parsed and compared as sets with the grep: listed-not-live = none, live-not-listed = none, for all eleven files. Odd hits opened: `RelDB` L74 (names "Neumayer is nearby but off Hwy 7"), L132 ("schematic designed at Neumayer"), L407, L450, L529, L540 — all the city; `NatConn` 15 lines each name the city; `09` L116, L241, L254 name the city in a list/clause; `16` L80, 114, 185, 222, 231 name the city inside other cities' passages (kept as the ledger lists them). Ports L97 matches only on "Atka", does not name the city (New findings 7). |
| NM-002 | APPLIED | `00.0_Pre-Trip_Inspection.md` (§C intro; §I; §J) | §C intro: "(**not yet built** — November item N-5; the addresses below are where the files will be created)" → "(19 files, all present — listing checked 2026-10-30)". §J: row "Datasheets not yet built for this city" **deleted**. §I: the raw block is untouched; one dated note added below its closing fence (see New findings 11). | `ls Datasheets/` = 19 files. Pre-Trip search for "not yet built": none left; "N-5" survives only in the §I raw block and the new note. |
| NM-003 | DECIDE — untouched | Pre-Trip §A; Ports L176 entry | alias set (Atka Iceport, Neumayer Station I/II/III, Neumayer-Station III, the Skiway, Georg von Neumayer; the drafted "Ekström Ice Shelf · Queen Maud Land") and the L176 removal are not changed | — |
| NM-004 | APPLIED | `README.md` row "Spec" | `../../../Specs/Neumayer.md` → `../../../Specs/Halley subnet/Neumayer.md` | `ls` of the new relative path from the pass folder resolves (186-line file); the old path does not exist. |
| NM-005 | APPLIED (SH-007 HELD, below) | Pre-Trip §D Phase 3 row and §F row; `Datasheets/Phase_3.md` megasheet row | "7 files" → "**7 entries — 6 files and 1 subfolder** (counted with `ls \| wc -l` and `find`, names not listed)" (§D); "(**6** files and **1** subfolder)" (§F); "inside a folder of **6 files and 1 subfolder**" (`Phase_3`). Shared items SH-001 … SH-006 are in the next table. | `ls -A \| wc -l` = 7; `find -maxdepth 1 -type f` = 6; `-type d` below the folder = 1. Names not read. |
| NM-020 | APPLIED | `Datasheets/Phase_2.md` Retention row | human 62.74% → **62.82%**, robot 69.82% → **69.74%** (combined 66.35% stays; as `Step_0.md`) | By hand: 846,594 ÷ 1,275,997 = 0.66348 → 66.35%; 393,179 ÷ 625,874 = 0.62821 → 62.82%; 453,415 ÷ 650,123 = 0.69743 → 69.74%. Inputs = `Official_Population_Census.md` L492 (625,874 H / 650,123 R / 1,275,997) and L616 (393,179 / 453,415 / 846,594), both re-read live. |
| NM-021 | APPLIED | `Datasheets/Step_3.md` (heading row + 7 picks) | "Section at L164–L172", picks L165–L171 → **section L195–L202 (heading L195; picks L196–L202)**; the seven rows cite **L196 … L202** | Live: L195 = `##### Neumayer`; L196–L202 = the seven picks (Bell Labs · JPL · Akademgorodok · Bletchley Park · Woods Hole · Mauna Loa · NIST). The five copied rows (JPL L197, Akademgorodok L198, Woods Hole L200, Mauna Loa L201, NIST L202) compared text-for-text: 5 of 5 identical; the two not-copied rows (L196, L199) map by order (New findings 9). |
| NM-022 | APPLIED | `Step_1_and_2.md` row 39 (was 37); `Phase_4.md` row 14; `Phase_7.md` rows 16–17 | `16` Half B row L272 → **L273** (header L247 kept) in the three sheets; `Phase_7` other-lines list replaced by the 18-line list of NM-001 | `16` L247 = column header `\| City \| Subnet \| D \| Workforce \| base% \| MAND% \| FREE% \| src \|`; L273 = `\| Neumayer \| Halley \| 2.50 \| 963,060 \| 43.7% \| 9.4% \| 46.9% \| D \|`; the values in the three sheets equal it. |
| NM-023 | APPLIED (Highways L268: number only, see NM-028) | `Datasheets/Phase_5.md` | Highways L238, 240, 242, 285 → **L239, 241, 243, 300**. Airports L48, 52 → **L51, 55**. Ports L535, 712, 836 → **L558, 735, 859**. RelDB entry "L334–L344" → **L345–L355**, citation L334 → **L345**, entry lines L335 … L341 → **L346 … L352**. NatConn 15-line list (value and citation cells) → live list of NM-001. | Programmatic read-only check of all 23 Highways / Airports / Ports / RelDB rows against their live lines: verbatim rows equal (Highways 8 of 8; Ports L103, L558, L735; RelDB L346, 347, 349, 350, 351); placeholder rows land on a line that names the city (Airports L51, L55; Ports L182, L859; RelDB L352); RelDB L348 = the "Status:" later-era line, still correctly excluded. Entry: L345 = `### Neumayer`, L354 = `---`, L355 blank, L356 = next entry. Two rows differ from their live lines for reasons outside this entry (New findings 5, 6). |
| NM-024 | DECIDE — untouched | `Phase_5.md` Ports L176 row ("Neumayer Channel") | row left (its number is unchanged) | — |
| NM-025 | APPLIED | `Datasheets/Step_0.md` (2 rows after Retention); `Datasheets/Step_1_and_2.md` (2 rows after the COMNAP row) | New rows: **Extent (2026-09-05 snapshot; census is live — note L631):** Neumayer · Subnet Halley · Census I (snapshot) 1,252,080 · @10,000/km² 125 km² · @7,000/km² 179 km² · Site Ekström ice shelf, cited `Extent_and_Density_Per_City.md` L615 (header L603; snapshot note L631); and **Extent at the live Census I (computed):** 127.6 km² · 182.3 km². | Live: Extent L603 = `\| City \| Subnet \| Census I \| @10k \| @7k \| Site \|`; L615 = `\| **Neumayer** \| Halley \| 1,252,080 \| 125 \| 179 \| **Ekström ice shelf** \|`; L631 = "(Snapshot note, 2026-10-28 …)". By hand: 1,275,997 ÷ 10,000 = 127.5997 → 127.6; 1,275,997 ÷ 7,000 = 182.2853 → 182.3. 1,275,997 = Census I L492, which also gives the snapshot's 1,252,080 as "was". |
| NM-026 | DECIDE — untouched | `Step_10.md` "(430 lines)" | left | — |
| NM-027 | DECIDE — untouched | `Phase_10.md` Calethina `Formative_History.md` row | left | — |
| NM-028 | DECIDE — content untouched; number repointed | `Phase_5.md` Highways row 20 (Temirötkel connector paragraph) | the paragraph is left as is; its citation **L267 → L268** (the live line; NM-001's Highways list names L268) | Highways L268 = the paragraph, compared with the sheet's copy: verbatim equal. If the developer drops the row, nothing else needs undoing. |
| NM-029 | DECIDE — untouched | all "N-line file" counts | left (SH-009) | — |
| NM-S01 / S02 | NOTE — untouched | spec L94, L79, L89–91; timeline repo README L17 | not edited (source and timeline repo) | — |

### Shared fixes (ledger section A) as they apply to Neumayer

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| SH-001 | APPLIED | Pre-Trip §G "No invented person names" | spine **L127 → L220, L1114, L1140** | Spine L220 = "… **and the no-invented-person-names rule**"; L1114 = "NO INVENTED PERSON NAMES — role placeholders permanently"; L1140 = "People as role-archetypes — **binding rule: no invented proper names.**" (L127 is a table row of the phase-by-tier grid). Runbook L1982 (the row's other cite) = Phase 10 row of the per-phase table, unchanged. Datasheets searched: no L127 cite. |
| SH-002 | APPLIED | Pre-Trip §G "Divergence operator" | runbook **L2178 → L2180** | Runbook L2180 = "### ⭐ THE DIVERGENCE OPERATOR — the developer's own inputs, and they are the checklist". |
| SH-003 | APPLIED | Pre-Trip §C Step 5 `T8` | `02` §5.3 lines **610–684 → 610–636** | `02` L610 = "## 5.3 The both-are-true test"; L636 blank; L637 = "# 6. Symbol binding — the open protocol". |
| SH-004 | APPLIED | Pre-Trip §C procedure items 4 and 5 | item 4: "620–643 and 701–703" → **"620–643 and 682–684 (the fifth section)"**; item 5: "650–703" → **667–684** | Trial recipe L620 = "### ROUND 3 — Peer cross-check", L643 = closing fence of the Round 3 prompt (the four questions) — kept; L682–684 = "Round 3's prompt now carries a fifth section …"; L667 = "AMENDED 2026-09-28 — THE WRITTEN CONTENT IS A MERGE, NOT A PICK", the box ends L684 (L685 blank). |
| SH-005 | APPLIED | Pre-Trip §C Step 10 (3 places) | governing "3057–3172" (twice) → **3057–3152**; card note "live lines 3045–3161 govern" → **"live lines 3057–3152 govern"** | Runbook L3057 = "# Step 10 — THE READINESS CHECK"; L3151 `---`, L3152 blank, L3153 = "# Where everything lives". The card's own stated origin ("3001–3091") left as it was. |
| SH-006 | ALREADY-RIGHT (not present) | `Step_-1.md` "Specs `Status:` field" row | The row cites `Specs/Neumayer.md` L4 and names the rule without a runbook line number. | grep for 1821 / 1822 / 1854 in all Neumayer sheets: none. |
| SH-007 | HELD (and not present) | — | No "`01` line 65" coordinate in any Neumayer sheet | grep for "line 65", "Resettled": none. |
| SH-008 | APPLIED | all 11 sheets that carry the header | Recount by hand, "checked 2026-10-23" → "recounted by hand 2026-10-30". **Totals changed on 6 sheets:** `Phase_2` split 3/0 → **1 direct / 2 via Tier U**; `Phase_3` 4 of 4 → **3 of 4**; `Phase_4` 7 of 7 (5/2) → **6 of 7 (4/2)**; `Phase_7` 13 of 13 (10/3) → **8 of 13 (7 direct / 1 via)**; `Phase_9` 4 of 4 (3/1) → **3 of 4 (2/1)**; `Phase_10` split 3/0 → **2 direct / 1 via**. Unchanged totals: `Step_0` 3 of 3 (2/1), `Step_1_and_2` 6 of 6, `Phase_5` 6 of 6, `Phase_6` 5 of 5, `Phase_8` 2 of 2. Where k < N the header names the uncovered addresses. | Table in §2. N confirmed against the `📂 MUST OPEN` block of each phase in the spine (L278, 326, 405, 476, 538, 620, 757, 846, 959, 1030, 1105). |
| SH-009 | HELD | all "N-line file" counts | unchanged (146, 187, 74, 293, 378, 166, 36, 246, 199, 28; `Step_10` "430 lines") | — |
| SH-010 | APPLIED | Pre-Trip §D Phase 2 table (2 rows + a clause on the `T8` line); `Datasheets/Phase_2.md` (2 rows) | Added: **Neumayer's own section** — heading `### Neumayer *(Ekström Ice Shelf, Atka Bay, ~70°41'S 8°16'W)*` L266, section **L266–L272**; and **the solar-UTC rule** — heading L21, "Recording it so it stops being reconstructed from examples" list **L26–L33** (rule 1 at L28), refinement box **L35–L63**. Cited by range, not quoted. In the Pre-Trip the rows are marked "registered, not dispatched" (the spine's Phase 2 MUST OPEN list and the runbook name no such file — `grep Upper_Earth_Immigration` in both: no hit); the `T8` line still says 3 rows and now adds "(the two composition-file rows above are registered, not dispatched)". | Composition file L266 = `### Neumayer …`; L268–L272 = header, separator and the three tier rows; L273 blank; L274 = `---`; L276 = `### Troll`. L21 = `### ⭐ HOW FACTOR 1 IS MEASURED — the ±3 solar-UTC window …`; L26 = "**Recording it so it stops being reconstructed from examples:**" (the numbered list runs to L33); L28 = rule 1; L35 = start of "AND THE REFINEMENT THAT CAUGHT A REAL ERROR"; L63 = its last line; L65 = next block. Form taken from the Santa Luce / Relung Panen `Phase_2.md` rows. |
| SH-011 | APPLIED | Pre-Trip §C Step 0 `T8` reads, §E row; the two new extent rows in `Step_0.md`, `Step_1_and_2.md` | Added "(table rows are a 2026-09-05 snapshot; the census is live — note L631)" beside the Extent citations; the datasheet rows carry the same label. | Extent L631 = "(Snapshot note, 2026-10-28: the table above records the 2026-09-05 populations …)". |
| SH-012 | APPLIED | Pre-Trip, `Phase_5`, `Phase_7` | via NM-001, NM-022, NM-023 | see above |
| SH-013 | NEEDS-DEVELOPER | Pre-Trip `16` lists; `Phase_7` row 17 | **Not listed for Neumayer in the ledger.** Per brief §4a only the heading line was added: **L481** `## 1. ✅ NEUMAYER — DETERMINED`, marked "the city's own upper-case heading", in the Pre-Trip Phase 1 row, the §E row and `Phase_7` row 17. The shares were **not** quoted beside Half B. | See New findings 1 — the city's own section differs materially from Half B. |
| SH-014 | APPLIED | `Step_1_and_2.md` row 39, `Phase_4.md` row 14, `Phase_7.md` row 16 | Clause added beside the Half B figures: "(on the flat ABCC working value; counts re-run when per-city ABCC values are set — `16_Per_City_Three_Tier_Run.md` L1287–L1304)". | `16` L1287 = "### ⚠ CONSEQUENCE — the ten determinations so far need a baseline re-run"; L1289 "Every city determined before this ruling used the flat 65"; L1302–L1304 = "WORKING VALUE UNTIL THEN: ABCC stays at the flat 65 per 1,000 residents for ALL cities …"; L1305 blank; L1306 next heading. The text spans **L1287–L1304**. The `09` row in `Phase_4` was not given the clause (it is not a `16` baseline). |
| SH-015 … 017, 019, 018, 020 … 023 | not Neumayer's files | Tier U sheets — the orchestrator's | — | — |

---

## 2 · MUST-OPEN recount (SH-008)

**Rule used (same as the Halley report).** An address counts as **direct** only if a row (or the sheet's own table) transcribes or cites it by its full file or directory name (a directory-qualified short form such as `Specs/Neumayer.md` or `READER/Neumayer.md` is counted, because the bare `Neumayer.md` would be a shared base name); **via Tier U** if no row names it but the sheet cites, by full file name, the Tier U sheet in `Corpus_Reference_Sheets/` that is the registered extract of it (its source list checked in that sheet's own header: `Second_Interwar_Period_Quick_Reference` ← `Timeline Eras/2 …/README.md`; `No_National_Stereotypes_Quick_Reference` ← `Reference/No_National_Stereotypes.md`; `Falkland_Treaty_Quick_Reference` ← `Reference/Falkland_Treaty/…`; `Robot_Physiology_Quick_Reference` ← `Robot_Physiology_and_Cultural_Practices.md` + `Robot_Cold_Physiology.md` + `Robot_Universals/` Ch. 13–14; `Division_of_Industry_Reliability_Quick_Reference` ← `Division_of_Industry/README.md` + `10_Validation_Findings`; `Zodiac_Signs_Quick_Reference` ← `Reference/Real-World/Zodiac_Signs_Full_Attributes.md`); otherwise **not covered**. The count excludes the header line itself and "known missing" lists. Row numbers are the sheet's live line numbers after the sweep. Judgment calls are flagged ⚑.

| Sheet | Address (spine MUST OPEN) | Covered by | Basis |
|---|---|---|---|
| **Step_0** (Phase 0) — **3 of 3** (2 direct, 1 via) | `Repo_Scope.md` | row L18 "**U** `Repo_Scope.md`" | direct |
| | `Timeline Eras/` | rows L15–17 cite `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` (source: `Timeline Eras/2 The Second Interwar Period/README.md`) | via Tier U |
| | `Official_Population_Census.md` | rows L10–11 | direct |
| **Step_1_and_2** (Phase 1) — **6 of 6** (6 direct) | `Worldspace/Locations/` (universe) | row L12 "Universe repo `Worldspace/Locations/`" ⚑ cited as `…/Worldspace/Locations/` (ellipsis) | direct |
| | `Specs/` | spec rows L14–L29, L42–L45 citing `Specs/Neumayer.md` ⚑ short form of `Specs/Halley subnet/Neumayer.md` | direct |
| | `Energy_Grid_Failure_Rationale.md` | row L40 | direct |
| | Climate `READER/` | rows L30–34 citing `READER/Neumayer.md` ⚑ directory-qualified | direct |
| | `Stations/` | rows L35 (`Antarctic_Stations_With_Airstrips.md`) and L36 (`COMNAP_Antarctic_Station_Catalogue.pdf`) | direct |
| | `16` Half B | row L39 (`16_Per_City_Three_Tier_Run.md`) | direct |
| **Phase_2** — **3 of 3** (1 direct, 2 via) | `No_National_Stereotypes.md` | row L21 "GPS law" cites `…/No_National_Stereotypes_Quick_Reference.md` | via Tier U |
| | `Falkland_Treaty/` | rows L18–20 cite `…/Falkland_Treaty_Quick_Reference.md` | via Tier U |
| | `Official_Population_Census.md` | rows L11, 15, 16 | direct |
| **Phase_3** — **3 of 4** (3 direct; Davis not applicable) | Climate `READER/` | **not covered** — no row names it (its rows are in `Step_1_and_2.md`) | — |
| | `Specs/` | rows L13–15 (`Specs/Neumayer.md`) ⚑ | direct |
| | `City_Concept-Art/` | row L10 (`City_Concept-Art/Halley_Subnet/Neumayer`) | direct |
| | `City_Megasheets/` (withheld, record only) | row L11 names `Neumayer_Physical_Infrastructure_Attributes.md` and the folder's contents count ⚑ file inside the folder | direct |
| **Phase_4** — **6 of 7** (4 direct, 2 via) | `Robot_Physiology_and_Cultural_Practices.md` | rows L16, L18 cite `Robot_Physiology_Quick_Reference.md` | via Tier U |
| | `Robot_Cold_Physiology.md` | row L17 ("Robot Cold Physiology — the governing mechanic") cites the same Tier U sheet | via Tier U |
| | `16` Half B | row L14 | direct |
| | `09` (§3.5) | row L12 (`09_Per_City_Baseline_Run.md`; the row quotes the §2 table, not §3.5 — covered at file level) | direct |
| | `11_Caloric_Rebuild_and_Livestock_Tier.md` | row L13 | direct |
| | `National_Medical_and_Care_Institutes.md` | row L15 | direct |
| | `National_Economy_and_Currency.md` | **not covered** — no row names it | — |
| **Phase_5** — **6 of 6** (6 direct) | `Worldspace/Locations/` | rows L12–13 ⚑ ellipsis form | direct |
| | `Highways.md` | rows L14–L21 | direct |
| | `Airports.md` · `Ports.md` · `Geothermal_Heating.md` (one address line, `Infrastructure/`) | rows L22–23 · L24–L30 · L31 — all three files named | direct |
| | `City_Cross_Subnet_Relationships.md` | row L41 | direct |
| | `City_Relationship_Database.md` | rows L33–L40 | direct |
| | `City_National_Connections.md` | row L42 | direct |
| **Phase_6** — **5 of 5** (5 direct) | `Factions/Robot_Religions/` · `National_Holidays.md` · `Ice-Cold_Buddhism_Research/` · `The_Meme_Machine_Extraction.md` · `The_True_Believer_Extraction.md` | rows L10 · L11 · L12 · L13 · L14 | direct |
| **Phase_7** — **8 of 13** (7 direct, 1 via) | `Division_of_Industry/` (README first) | no row names the folder (L19 cites a bare `README.md`); the header box (L3) cites `Division_of_Industry_Reliability_Quick_Reference.md`, whose source is the folder's README ⚑ header-box citation, not a row | via Tier U |
| | `16` Half B | rows L16–17 | direct |
| | `Division_of_Industry_Sweep_2026-08-31.md` | row L18 | direct |
| | `01_Burden_Scoring_Model.md` | row L19 | direct |
| | `08_Volume_Based_Requirement_Reference.md` | **not covered** | — |
| | `National_Medical_and_Care_Institutes.md` | **not covered** (no row; the Pre-Trip says "as Phase 4") | — |
| | `Theoretical-Calculations/` | row L20 | direct |
| | `Industry_Staffing_and_Productivity/` | **not covered** | — |
| | `jobs_professions_and_fields/` | row L21 | direct |
| | `National_Economy_and_Currency.md` | **not covered** | — |
| | `City_Logistics.md` | row L22 | direct |
| | `Factions/` | row L23 | direct |
| | `Megacorps/` | **not covered** (the Tier U sheet that extracts it, `Phase_7_Roster_and_Model_Files_Quick_Reference.md`, is not cited in this sheet) | — |
| **Phase_8** — **2 of 2** (2 direct) | `Robot_Biology_and_Culture/` · `Weapons_and_Tools_Philosophy.md` | rows L12 · L10 | direct |
| **Phase_9** — **3 of 4** (2 direct, 1 via) | `Laws_of_Robotics.md` | **not covered** — no row names the file; the row that gives the two laws (L12) cites `Robot_Physiology_Quick_Reference.md`, which does not carry them (New findings 4) | — |
| | `Robot_Universals/` | rows L10, 11, 13, 14 | direct |
| | `Doll_Representation_Categories.md` | row L15 | direct |
| | human-robot baseline = `Robot_Physiology_and_Cultural_Practices.md` | rows L12–14 cite `Robot_Physiology_Quick_Reference.md` | via Tier U |
| **Phase_10** — **3 of 3** (2 direct, 1 via) | `Worldspace/Characters/` (universe) | rows L10–12 | direct |
| | `Enneagram_Character_Index.md` | row L13 | direct |
| | `Zodiac_Signs_Full_Attributes.md` | row L14 cites `Zodiac_Signs_Quick_Reference.md` (source: `Reference/Real-World/Zodiac_Signs_Full_Attributes.md`) | via Tier U |

*(Sheets without the header — `Step_-1`, `Step_3`, `Step_5`, `Step_6`, `Step_7`, `Step_8`, `Step_9`, `Step_10` — not counted.)*

---

## 3 · New findings (not in the ledger; not fixed unless noted)

1. **Neumayer's own `16` section (`## 1. ✅ NEUMAYER — DETERMINED`, L481–L545; next heading L546) differs materially from Half B (L273); SH-013 is not listed for Neumayer.** Section table (counts are on the pre-`DR-68` workforce): Baseline 413,123 (43.7%), Mandated 181,974 (19.3%), FREE 350,115 (37.0%); by hand 413,123 + 181,974 + 350,115 = 945,212 (the pre-`DR-68` workforce, 638,345 + 0.5 × 613,735 = 945,212.5), 181,974 ÷ 945,212 = 19.25%, 350,115 ÷ 945,212 = 37.04%; distinctive tier 532,089 (56.3%). Half B row L273: workforce 963,060 (the current workforce, 650,123 + 0.5 × 625,874), base 43.7%, MAND 9.4%, FREE 46.9%. The section's own text (L503) says "Half B recorded Neumayer at mandated 9.4% / free 46.9%. That figure was only the research floor …" and calls the miss ~9.9 points. The sheets (`Step_1_and_2`, `Phase_4`, `Phase_7`) quote only Half B. Per brief §4a I added only the heading line L481 to the Pre-Trip's `16` lists (Phase 1 row, §E row) and `Phase_7` row 17, marked "the city's own upper-case heading", and did **not** quote the shares beside Half B. **Needs the developer:** whether the three sheets should quote §1 beside Half B and say which governs (the SH-013 pattern). Easy to revert: delete "L481 *(…)*, " from those three places and set the `Phase_7` count back to 17.
2. **Rows missing for must-open addresses** (shown in §2): `Phase_3` has no Climate `READER/` row; `Phase_4` has no `National_Economy_and_Currency.md` row; `Phase_7` has no rows for `08_Volume_Based_Requirement_Reference.md`, `National_Medical_and_Care_Institutes.md`, `Industry_Staffing_and_Productivity/`, `National_Economy_and_Currency.md`, `Megacorps/`; `Phase_9` none for `Laws_of_Robotics.md`. These are gaps for the developer to decide on; none was filled.
3. **`Phase_7.md` row L24 (meta row) still says "Addresses of the spine's Phase 7 block that exist on disk: 11 of 11"**, while the header now says 8 of 13 and the spine block has 13 addresses (the Pre-Trip's Phase 7 table has 11 rows because `01`/`08` share one). Left alone, as the brief says.
4. **`Phase_9.md` row 12 (Laws of Robotics) is not word-for-word and cites a sheet that does not carry it.** Sheet: "1. A robot will have full capacity … 2. A robot will understand that anything she is capable of doing to others is realistically possible for others to do to her." Source `Laws_of_Robotics.md` L3–L4: "have **the** full capacity" and "anything she is capable of doing to others, **it is also** realistically possible for others to do to her." The citation `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md` holds neither law (grep for "future possibilities" / "Laws of Robotics": no hit). The file `Laws_of_Robotics.md` is not named.
5. **`Phase_5.md` Ports L176 row (NM-024, DECIDE) is also stale in its text:** the sheet's copy ends "(Port Lockroy on day 5 of an operator log)"; the live line reads "(Puerto Abrigo on day 5 of an operator log)" (the 2026-10 rename sweep changed the source). Row untouched; decide with NM-024.
6. **`Phase_5.md` Ports L245 row is a partial copy:** the sheet's value ends "…the developer has not ruled.*"; the live line continues with a 2026-10-29 `DR-82` sentence about the seasonal sea gateway and the ocean research. Not in the ledger; left (the copied part is verbatim, the line number is unchanged).
7. **Ports L97** quotes "Atka Iceport… an iceport about 16 km long and wide …" and does not name Neumayer; it is not a hit for the current alias set. If "Atka Iceport" is confirmed as an alias (NM-003, DECIDE), L97 joins the Ports list.
8. **One list entry beyond the ledger:** `09` **L160** ("… A Neumayerite has half.") is a demonym hit of the live `grep -i`, added to the Pre-Trip's `09` list for the same reason the ledger itself adds Robot Physiology L369 ("A Neumayerite …"). The builder's word-boundary search had missed both. The line is a comparison heading in `09` (it also names another city's resident); only its number is listed. Easy to revert (delete "L160, " in the Pre-Trip Phase 4 row).
9. **`Step_3.md` not-copied rows:** the row now at L196 is labelled "source line compares the city with other places" and the row at L199 "excluded: later-era content"; they map by order to Bell Labs (L196) and Bletchley Park (L199), whose live texts do not plainly match those labels (the builder's heuristic). Labels left as they were; for the developer's awareness.
10. **Pass `README.md`:** the first block still says "Folder opened 2026-09-05. ⚠ Empty by design … never pre-created" while the folder now holds the Pre-Trip, the ledger and 19 datasheets. Not in the ledger; left.
11. **The §I dated note.** NM-002 says "leave §I as the dated build record". The raw block is untouched; I added one italic line below its closing fence ("Dated note, 2026-10-30: … `Datasheets/` now holds 19 files, all present") so the `DATASHEET-NOT-YET-BUILT(N-5)=20` count is not read as current. Delete that line if not wanted.
12. **Spec length:** `Step_-1.md` says "187 lines total"; `wc -l` of the spec is 186 (builder convention, SH-009 HELD).

---

## 4 · Files edited (Edit tool only)

Pass folder `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Halley_Subnet/Neumayer/`:
- `00.0_Pre-Trip_Inspection.md`
- `README.md`
- `Datasheets/Step_0.md`, `Datasheets/Step_1_and_2.md`, `Datasheets/Step_3.md`
- `Datasheets/Phase_2.md`, `Phase_3.md`, `Phase_4.md`, `Phase_5.md`, `Phase_6.md`, `Phase_7.md`, `Phase_8.md`, `Phase_9.md`, `Phase_10.md`

Unedited (checked, nothing to change or only DECIDE items): `Datasheets/Step_-1.md`, `Step_5.md`, `Step_6.md`, `Step_7.md`, `Step_8.md`, `Step_9.md`, `Step_10.md`, `00.2_Position_Coverage_Ledger.md`.
Created: this report (`Manual_Input_Audit_2026-10-29/Sweep_Reports/Neumayer_Sweep.md`). Nothing committed; no source, spec, census, Register, builder script, `FIX_LEDGER.md` or `TRACKER.md` touched.
