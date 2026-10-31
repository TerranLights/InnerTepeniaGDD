# Halley — fix-sweep report (2026-10-30)

**City:** Halley (ledger section **B8 · HALLEY**; city and subnet share the name). **Who:** sweep sub-agent. **Date:** 2026-10-30.
**Read:** `SWEEP_BRIEF.md` in full; `FIX_LEDGER.md` section A and `### B8 · HALLEY`; `Halley_Audit.md` in full; the whole Pre-Trip (566 lines), the pass `README.md`, all 19 datasheets, `00.2_Position_Coverage_Ledger.md`; every live source line named below (re-opened before writing). Megasheets, Local Culture, Enneagram, vision notes and Background-Lore were **not** opened (the megasheet folder was only counted with `ls | wc -l` / `find`, names not read).
**Method:** Edit tool only; no `sed -i`, no generators, nothing rebuilt, nothing committed. Every changed row was re-checked afterward against its live source line by a read-only comparison (Highways, Airports, Ports and RelDB rows in `Phase_5` compared line by line with the sources; the four `16` line lists compared as sets; `Step_3` picks compared text-for-text with `Inspirational-Influences.md` L181–187; `09` row, `16` row, `11` row compared with the sources).

**Totals:** APPLIED 20 (10 ledger entries + 10 shared fixes) · ALREADY-RIGHT / not present 1 · HELD 2 (SH-007, SH-009) · DECIDE entries left untouched 9 (HL-003, 004, 025, 027, 028, 029, S01, S02, S03) · NEEDS-DEVELOPER 1 (SH-013, see New findings 1) · SKIPPED-MISMATCH 0.

---

## 1 · Entry table

### Ledger entries for Halley

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| HL-001 | APPLIED | `00.0_Pre-Trip_Inspection.md` (§C Step 2; §D Phase 1, 4, 5 rows; §E) | Every "Names Halley at" list re-generated from a live `grep -n -i` and the odd hits opened. **`16`**: row L273 → **L274** (Step 2 `T8` line, §D Phase 1 row, §E row); other-lines list 31 lines → **32 lines** (see note A). **`09`**: L99, 151, 173, 197, 239 → **L101, 153, 175, 199, 241** (L54–55, 61–65, 74 unchanged). **Highways**: L248, 250, 252, 254, 256 → **L249, 251, 253, 255, 257**; L283–284 → **L298–299**. **Airports**: L48, 52, 60 → **L51, 55, 63**. **Ports**: 15 entries +23 → **L345–346, 388, 390, 399–400, 404, 407, 436–437, 454, 739, 814, 859, 867** (L68, 182 unchanged). **RelDB**: **L243–244, 247–250, 294, 341, 349, 352, 382, 404, 469, 518, 522, 543** (L23, 27, 47, 71, 73, 84, 93, 95–96 unchanged). **NatConn**: 52 lines, 19 re-pointed (**L314, 367, 369, 377, 379, 391, 422, 429, 431, 433, 494, 508, 523, 532, 534, 549, 553, 562, 586**; L36–283 unchanged). | Live `grep -n -i "halley\|hallite"` on each file; the Pre-Trip lists then parsed and compared with the grep as sets: listed-not-live = none for all six files; live-not-listed = only the subnet-only lines in note B. `16` lists: Pre-Trip Phase 1 row, §E row, `Phase_7` row 18 (value and citation) are identical sets of 32 lines. Count of NatConn list = 52. |
| HL-002 | APPLIED | `00.0_Pre-Trip_Inspection.md` (§C intro; §I; §J) | §C intro: "(**not yet built** — November item N-5; the addresses below are where the files will be created)" → "(19 files, all present — listing checked 2026-10-30)". §J: row "Datasheets not yet built for this city" **deleted**. §I: raw block left as the dated build record; a dated note added below the closing fence saying the `DATASHEET-NOT-YET-BUILT(N-5)=20` count was the state at generation and `Datasheets/` now holds 19 files. | `ls Datasheets/` = 19 files. `grep` of the Pre-Trip for "not yet built": none left; "N-5" survives only in the §I raw block and its new note. |
| HL-003 | DECIDE — untouched | Pre-Trip §A | alias set not changed | — |
| HL-004 | DECIDE — untouched | Pre-Trip §D addendum | `Russia_Split_Proportions_RS3…` not registered | — |
| HL-005 | APPLIED (SH-007 HELD, see below) | Pre-Trip (§D Phase 3 row; §F row), `Datasheets/Phase_3.md` row 12 | Megasheet folder "7 files" → "**6 files and 1 subfolder**" (Pre-Trip: "7 entries by `ls \| wc -l`, names not listed"). Shared items listed under SH-001 … SH-006 below. | `ls \| wc -l` = 7 entries; `find -maxdepth 1 -type f` = 6, `-type d` (below the folder) = 1. Names not read. |
| HL-006 | APPLIED | `README.md` row "Spec" | `../../../Specs/Halley.md` → `../../../Specs/Halley subnet/Halley.md` | `ls` of the new relative path from the pass folder resolves; the other three pointers also resolve (existence only). |
| HL-020 | APPLIED | `Datasheets/Phase_4.md` row 13 (`09`) | Neumayer's row (613,735 · 1,252,080 · 475,924 · 945,213 · 50.4%, cited L52, L54) → Halley's own row: **D 2.50 · Humans 721,889 · Residents 1,476,263 · Required 560,759 · Workforce 1,115,319 · % WF 50.3%**, cited **L52, L55**. The `#` rank is not carried. | `09` L52 = column header, L55 = `\| 2 \| **Halley** \| Halley \| 2.50 \| 721,889 \| 1,476,263 \| **560,759** \| 1,115,319 \| **50.3%** \|`. Row text compared with the live line. |
| HL-021 | APPLIED | `Datasheets/Phase_2.md` Retention row | "74.92% · 71.74% · 77.95%" → **74.78% · 71.66% · 77.76%** (as `Step_0.md`) | By hand: 1,103,916 ÷ 1,476,263 = 0.74778 → 74.78%; 517,317 ÷ 721,889 = 0.71662 → 71.66%; 586,599 ÷ 754,374 = 0.77760 → 77.76% (e.g. 1,476,263 × 0.7478 = 1,103,949, 33 above the numerator → 0.74778). The three inputs equal `Official_Population_Census.md` L486 and L606 as already carried in the sheet. |
| HL-022 | APPLIED | `Datasheets/Step_3.md` (heading row + 7 picks) | Section "L149–L157", picks L150–156 → **section L180–L187 (heading L180; picks L181–L187)**; the seven pick rows cite **L181 … L187**. | Live: L180 = `##### Halley`; L181–187 = the seven picks; each pick's text compared with the sheet's value: 7 of 7 identical. (Old L149–156 are the Mawson subnet's heading and picks.) |
| HL-023 | APPLIED | `Step_1_and_2.md` row 35 (was 33); `Phase_4.md` row 15; `Phase_7.md` rows 17–18 | `16` Half B row L273 → **L274** (header L247 kept) in all three sheets; `Phase_7` row 18 other-lines list replaced by the 32-line list of HL-001. | `16` L247 = column header, L274 = `\| Halley \| Halley \| 2.50 \| 1,115,318 \| 43.7% \| 9.4% \| 47.0% \| D \|`; values in the three sheets equal it. |
| HL-024 | APPLIED | `Datasheets/Phase_5.md` | Highways: L248, 250, 252, 254, 256 → **L249, 251, 253, 255, 257**; L283, L284 → **L298, L299**. Airports: L48, 52, 60 → **L51, 55, 63**. Ports: L322, 323, 365, 367, 376, 377, 381, 384, 413, 414, 431, 716, 791, 836, 844 → **L345, 346, 388, 390, 399, 400, 404, 407, 436, 437, 454, 739, 814, 859, 867**. RelDB: entry "L232–L242" → **L243–L253**, citation L232 → **L243**; entry lines L233–L239 → **L244–L250**. NatConn: the 52-line list (value and citation cells) → live list of HL-001. | Programmatic read-only check: all 28 re-pointed Highways / Airports / Ports / RelDB rows compared with their live lines; verbatim rows equal the live line; placeholder rows ("multi-city list" / "compares…") land on a line that names Halley; RelDB L246 = the "Status:" later-era line, still correctly excluded. The Ports L867 row's **content is untouched** (HL-027 DECIDE); only its line number moved. |
| HL-025 | DECIDE — untouched | `Step_10.md` "430 lines" | left as is | — |
| HL-026 | APPLIED | `Datasheets/Step_0.md` (2 rows after Retention), `Datasheets/Step_1_and_2.md` (2 rows after the COMNAP row) | New rows: **Extent (2026-09-05 snapshot; census is live — note L631):** Halley · Subnet Halley · Census I (snapshot) 1,452,345 · @10k 145 km² · @7k 207 km² · Site Brunt ice shelf — MIGRATING, cited `Extent_and_Density_Per_City.md` L609 (header L603; snapshot note L631); and **Extent at the live Census I (computed):** 147.6 km² · 210.9 km². | Live: Extent L603 = column header, L609 = `\| **Halley** \| Halley \| 1,452,345 \| 145 \| 207 \| **Brunt ice shelf — MIGRATING** \|`, L631 = "(Snapshot note, 2026-10-28 …)". By hand: 1,476,263 ÷ 10,000 = 147.6263 → 147.6; 1,476,263 ÷ 7,000 = 210.8947 → 210.9. 1,476,263 = Census I L486 (which also says the previous value was 1,452,345, the snapshot's figure). |
| HL-027 | DECIDE — untouched | `Phase_5.md` Ports L867 row (vignette path) | content left; number repointed under HL-024 | — |
| HL-028 | DECIDE — untouched | `Phase_10.md` Salagéa row | left | — |
| HL-029 | DECIDE — untouched | "N-line file" counts | left (SH-009) | — |
| HL-S01 / S02 / S03 | DECIDE / NOTE — untouched | spec L69 etc.; timeline repo README | not edited (source and timeline repo) | — |

**Note A — `16` list, one added line (rule 4, "use -i").** The ledger's list is the builder's case-sensitive result. The live `-i` search adds **L600 `## 3. ✅ HALLEY — DETERMINED`** (the city's own section, upper-case heading). It is now in the list (Pre-Trip §D Phase 1 row, §E row, `Phase_7` row 18; marked as the city's own upper-case heading); the count changed 31 → 32. Easy to revert if not wanted.
**Note B — hits examined and left out (subnet-only or continuation lines).** `16`: L78, 314, 323, 324, 548, 565, 638 (continuation of L636), 694, 757, 829, 3253, 3555. Airports: L19, L36. Ports: L263, L435. RelDB: L132, 133, 135, 385, 407, 506, 523. NatConn: L34, 41, 82, 113, 129, 137, 140, 540, 541, 542. CrossSub: L63, 76, 112, 122. Each line opened; each names only "Halley subnet" / "Halley-subnet" or a file name containing it.

### Shared fixes (ledger section A) as they apply to Halley

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| SH-001 | APPLIED | Pre-Trip §G "No invented person names" | spine **L127 → L220, L1114, L1140** | Spine L220 contains "and the no-invented-person-names rule"; L1114 = "NO INVENTED PERSON NAMES — role placeholders permanently"; L1140 = "People as role-archetypes — binding rule: no invented proper names". Datasheets searched: no L127 cite. Runbook L1982 (the other cite in the row) = Phase 10 row of the per-phase table, unchanged. |
| SH-002 | APPLIED | Pre-Trip §G "Divergence operator" | runbook **L2178 → L2180** | Runbook L2180 = "### ⭐ THE DIVERGENCE OPERATOR — …". |
| SH-003 | APPLIED | Pre-Trip §C Step 5 `T8` | `02` §5.3 lines **610–684 → 610–636** | `02` L610 = "## 5.3 The both-are-true test"; L637 = "# 6. Symbol binding". |
| SH-004 | APPLIED | Pre-Trip §C procedure items 4 and 5 | item 4: "620–643 and 701–703" → **"620–643 and 682–684 (the fifth section)"**; item 5: "650–703" → **667–684** | Trial recipe L620–643 = the Round 3 prompt (four questions) — kept; L682–684 = "Round 3's prompt now carries a fifth section …"; L667 = "AMENDED 2026-09-28 — THE WRITTEN CONTENT IS A MERGE, NOT A PICK", box ends L684. |
| SH-005 | APPLIED | Pre-Trip §C Step 10 (3 places) | governing "3057–3172" (twice) → **3057–3152**; card note "live lines 3045–3161 govern" → **"live lines 3057–3152 govern"** | Runbook L3057 = "# Step 10 — THE READINESS CHECK"; L3153 = "# Where everything lives"; L3151 `---`, L3152 blank. The card's own stated origin ("3001–3091") left as it was. |
| SH-006 | ALREADY-RIGHT (not present) | `Step_-1.md` "Specs `Status:` field" row | The row cites `Specs/Halley.md` L4 and names the rule without a runbook line number; no L1821–1822 in Step_-1 or the Pre-Trip. | grep for 1821 / 1822 / 1854 in all Halley sheets: none. |
| SH-007 | HELD (and not present) | — | No "`01` line 65" coordinate in any Halley sheet (`Step_10.md` has no such row). | grep for "line 65", "Resettled": none. |
| SH-008 | APPLIED | all 11 sheets that carry the header | Recount by hand, "checked 2026-10-23" → "recounted by hand 2026-10-30". **Totals changed on 6 sheets:** `Phase_2` split 3/0 → **1 direct / 2 via Tier U**; `Phase_3` 4 of 4 → **3 of 4**; `Phase_4` 7 of 7 → **6 of 7**; `Phase_7` 13 of 13 (10/3) → **8 of 13 (7 direct / 1 via Tier U)**; `Phase_9` 4 of 4 → **3 of 4 (2/1)**; `Phase_10` split 3/0 → **2 direct / 1 via Tier U**. Unchanged totals: `Step_0` 3 of 3 (2/1), `Step_1_and_2` 6 of 6, `Phase_5` 6 of 6, `Phase_6` 5 of 5, `Phase_8` 2 of 2. Where k < N the header now names the uncovered addresses. | Table in §2 below. N was confirmed against the `📂 MUST OPEN` block of each phase in the spine (L278, 326, 405, 476, 538, 620, 757, 846, 959, 1030, 1105) and the runbook table L1968–1982. |
| SH-009 | HELD | all "N-line file" counts | unchanged (218, 74, 293, 378, 166, 36, 246, 199, 146) | — |
| SH-010 | APPLIED | Pre-Trip §D Phase 2 table (2 rows); `Datasheets/Phase_2.md` (2 rows) | Added: **Halley's own section** — heading `### Halley` L254, section **L254–L262**; and **the solar-UTC rule** — heading L21, "Recording it so it stops being reconstructed from examples" list L26–L33 (rule 1 at L28), refinement box L35–L63. Cited by range, not quoted. In the Pre-Trip the rows are marked "registered, not dispatched" (the spine's Phase 2 MUST OPEN list does not name the file; READER SCOPE says nothing is added to `T8` "to be safe"); the `T8` line still says 3 rows. | Composition file L254 = `### Halley *(Brunt Ice Shelf, Coats Land, ~75°35'S 26°34'W)*`, L262 = founding note, L264 = `---`, L266 = `### Neumayer`; L21 = `### ⭐ HOW FACTOR 1 IS MEASURED — the ±3 solar-UTC window`, L26 = "Recording it so it stops…", L28 = rule 1, L35 = start of the refinement box, L63 = its last line, L65 = next block. Form of the sheet row taken from the existing Santa Luce / Relung Panen `Phase_2.md` rows. |
| SH-011 | APPLIED | Pre-Trip §C Step 0 `T8` reads, §E row; the two new extent rows in `Step_0.md`, `Step_1_and_2.md` | Added "(table rows are a 2026-09-05 snapshot; the census is live — note L631)" beside the Extent citations; the datasheet rows carry the same label. | Extent L631 = "(Snapshot note, 2026-10-28 …)". |
| SH-012 | APPLIED | Pre-Trip and `Phase_5`, `Phase_7` | via HL-001, HL-023, HL-024 | see above |
| SH-013 | NEEDS-DEVELOPER | — | **Not listed for Halley in the ledger, not applied.** Halley's own `16` §3 (L600–L651) exists and differs from Half B — see New findings 1. | — |
| SH-014 | APPLIED | `Step_1_and_2.md` row 35, `Phase_4.md` row 15, `Phase_7.md` row 17 | Clause added beside the Half B figures: "(on the flat ABCC working value; counts re-run when per-city ABCC values are set — `16_Per_City_Three_Tier_Run.md` L1287–L1304)". | `16` L1287 = "### ⚠ CONSEQUENCE — the ten determinations so far need a baseline re-run"; L1289 "Every city determined before this ruling used the flat 65"; L1302–1304 "WORKING VALUE UNTIL THEN: ABCC stays at the flat 65 per 1,000 residents for ALL cities …"; L1305 blank, L1306 next heading. The text spans **L1287–L1304**, not L1305 as in the ledger. The `09` row in `Phase_4` was not given the clause (it is not a `16` baseline). |
| SH-015 … 017, 019, 018, 020 … 023 | not Halley's files | Tier U sheets — the orchestrator's | — | — |

---

## 2 · MUST-OPEN recount (SH-008)

**Rule used.** An address counts as **direct** only if a row (or the sheet's own table) transcribes or cites it by its full file name or full directory name (a directory-qualified short form such as `Specs/Halley.md` or `READER/Halley.md` is counted, because the bare `Halley.md` would be a shared base name); **via Tier U** if no row names it but the sheet cites, by full file name, the Tier U sheet in `Corpus_Reference_Sheets/` that is the registered extract of it (checked in that sheet's own source list); otherwise **not covered**. The count excludes the header line itself and "known missing" lists. Judgment calls are flagged ⚑ so the orchestrator can apply a stricter reading.

| Sheet | Address (spine MUST OPEN) | Covered by | Basis |
|---|---|---|---|
| **Step_0** (Phase 0) — **3 of 3** (2 direct, 1 via) | `Repo_Scope.md` | row "**U** `Repo_Scope.md`" (L19) | direct |
| | `Timeline Eras/` | rows citing `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` (L16–18; its source is `Timeline Eras/2 The Second Interwar Period/README.md`) | via Tier U |
| | `Official_Population_Census.md` | rows Census I / II (L11–12) | direct |
| **Step_1_and_2** (Phase 1) — **6 of 6** (6 direct) | `Worldspace/Locations/` (universe) | row "Universe repo `Worldspace/Locations/`" (L13–14) ⚑ cited as `…/Worldspace/Locations/` (ellipsis) | direct |
| | `Specs/` | spec rows citing `Specs/Halley.md` (many) ⚑ short form of `Specs/Halley subnet/Halley.md` | direct |
| | `Energy_Grid_Failure_Rationale.md` | row L36 | direct |
| | Climate `READER/` | row "Climate READER file" citing `READER/Halley.md` (L30) ⚑ directory-qualified | direct |
| | `Stations/` | rows citing `Antarctic_Stations_With_Airstrips.md` (L31) and `COMNAP_Antarctic_Station_Catalogue.pdf` (L32) | direct |
| | `16` Half B | row L35 (`16_Per_City_Three_Tier_Run.md`) | direct |
| **Phase_2** — **3 of 3** (1 direct, 2 via) | `No_National_Stereotypes.md` | row "GPS law" (L23) cites `…/No_National_Stereotypes_Quick_Reference.md` (source: `Reference/No_National_Stereotypes.md`) | via Tier U |
| | `Falkland_Treaty/` | rows L20–22 cite `…/Falkland_Treaty_Quick_Reference.md` (source: `Reference/Falkland_Treaty/…`) | via Tier U |
| | `Official_Population_Census.md` | rows L12, 15, 17, 18 | direct |
| **Phase_3** — **3 of 4** (3 direct; Davis not applicable) | Climate `READER/` | **not covered** — no row names it (the Pre-Trip says "as Phase 1"; its rows are in `Step_1_and_2.md`) | — |
| | `Specs/` | rows L14–16 (`Specs/Halley.md`) ⚑ | direct |
| | `City_Concept-Art/…/Halley` | row L11 | direct |
| | `City_Megasheets/` (withheld, record only) | row L12 names `Halley_Physical_Infrastructure_Attributes.md` and the folder's contents count ⚑ file inside the folder | direct |
| **Phase_4** — **6 of 7** (4 direct, 2 via) | `Robot_Physiology_and_Cultural_Practices.md` | rows L17, 19 cite `Robot_Physiology_Quick_Reference.md` (its header lists the file as a source) | via Tier U |
| | `Robot_Cold_Physiology.md` | row L18 ("Robot Cold Physiology — the governing mechanic") cites the same Tier U sheet (source list names the file) | via Tier U |
| | `16` Half B | row L15 | direct |
| | `09` (§3.5) | row L13 (`09_Per_City_Baseline_Run.md`; the row quotes the §2 table, not §3.5 — covered at file level) | direct |
| | `11_Caloric_Rebuild_and_Livestock_Tier.md` | row L14 | direct |
| | `National_Medical_and_Care_Institutes.md` | row L16 | direct |
| | `National_Economy_and_Currency.md` | **not covered** — no row names it | — |
| **Phase_5** — **6 of 6** (6 direct) | `Worldspace/Locations/` | rows L13–14 | direct |
| | `Highways.md` | rows L15–28 | direct |
| | `Airports.md` · `Ports.md` · `Geothermal_Heating.md` (one address line, `Infrastructure/`) | rows L29–31 · L32–48 · L49 — all three files named | direct |
| | `City_Cross_Subnet_Relationships.md` | row L59 | direct |
| | `City_Relationship_Database.md` | rows L51–58 | direct |
| | `City_National_Connections.md` | row L60 | direct |
| **Phase_6** — **5 of 5** (5 direct) | `Factions/Robot_Religions/` · `National_Holidays.md` · `Ice-Cold_Buddhism_Research/` · `The_Meme_Machine_Extraction.md` · `The_True_Believer_Extraction.md` | rows L11 · L12 · L13 · L14 · L15 | direct |
| **Phase_7** — **8 of 13** (7 direct, 1 via) | `Division_of_Industry/` (README first) | no row names the folder (L21 cites a bare `README.md`); the header box (L3) cites `Division_of_Industry_Reliability_Quick_Reference.md`, whose source is the folder's README ⚑ header-box citation, not a row | via Tier U |
| | `16` Half B | rows L17–18 | direct |
| | `Division_of_Industry_Sweep_2026-08-31.md` | rows L19–20 | direct |
| | `01_Burden_Scoring_Model.md` | row L21 | direct |
| | `08_Volume_Based_Requirement_Reference.md` | **not covered** | — |
| | `National_Medical_and_Care_Institutes.md` | **not covered** (no row; the Pre-Trip says "as Phase 4") | — |
| | `Theoretical-Calculations/` | row L22 | direct |
| | `Industry_Staffing_and_Productivity/` | **not covered** | — |
| | `jobs_professions_and_fields/` | row L23 | direct |
| | `National_Economy_and_Currency.md` | **not covered** | — |
| | `City_Logistics.md` | row L24 | direct |
| | `Factions/` | row L25 | direct |
| | `Megacorps/` | **not covered** (the Tier U sheet that extracts it, `Phase_7_Roster_and_Model_Files_Quick_Reference.md`, is not cited in this sheet) | — |
| **Phase_8** — **2 of 2** (2 direct) | `Robot_Biology_and_Culture/` · `Weapons_and_Tools_Philosophy.md` | rows L13 · L11 | direct |
| **Phase_9** — **3 of 4** (2 direct, 1 via) | `Laws_of_Robotics.md` | **not covered** — no row names the file; the row that gives the two laws (L12) cites `Robot_Physiology_Quick_Reference.md`, which does not carry them (see New findings 3) | — |
| | `Robot_Universals/` | rows L11, 13, 14 | direct |
| | `Doll_Representation_Categories.md` | row L15 | direct |
| | human-robot baseline = `Robot_Physiology_and_Cultural_Practices.md` | rows L12–14 cite `Robot_Physiology_Quick_Reference.md` (source list names the file) | via Tier U |
| **Phase_10** — **3 of 3** (2 direct, 1 via) | `Worldspace/Characters/` (universe) | rows L11–12 | direct |
| | `Enneagram_Character_Index.md` | row L13 | direct |
| | `Zodiac_Signs_Full_Attributes.md` | row L14 cites `Zodiac_Signs_Quick_Reference.md` (source: `Reference/Real-World/Zodiac_Signs_Full_Attributes.md`) | via Tier U |

*(Sheets without the header — `Step_-1`, `Step_3`, `Step_5`, `Step_6`, `Step_7`, `Step_8`, `Step_9`, `Step_10` — not counted.)*

---

## 3 · New findings (not in the ledger; not fixed unless noted)

1. **`16` §3 "HALLEY — DETERMINED" (L600–L651) disagrees with Half B (L274); SH-013 is not listed for Halley.** §3 table: Baseline 478,952 (43.6%), Mandated 170,093 (15.5%), FREE 448,426 (40.9%) = 1,097,471 workers (by hand: 478,952 + 170,093 = 649,045; + 448,426 = 1,097,471; 170,093 ÷ 1,097,471 = 15.50%; 448,426 ÷ 1,097,471 = 40.86%). Half B row L274: workforce 1,115,318, base 43.7%, MAND 9.4%, FREE 47.0%. §3 L624 itself says 9.4% is the commuter figure; the 15.5% adds the Arcanet half (7.5% of the distinctive tier). The sheets (`Step_1_and_2`, `Phase_4`, `Phase_7`) quote only Half B. Per SH-013 this would need the §3 shares quoted beside Half B and a statement of which governs — **not applied** (not in Halley's ledger section); the §3 heading line L600 is now in the `16` line lists. Needs the developer / orchestrator to say whether SH-013 applies to Halley.
2. **Rows missing for must-open addresses** (shown in §2): `Phase_3` has no Climate READER row; `Phase_4` has no `National_Economy_and_Currency.md` row; `Phase_7` has no rows for `08_…`, `National_Medical_and_Care_Institutes.md`, `Industry_Staffing_and_Productivity/`, `National_Economy_and_Currency.md`, `Megacorps/`; `Phase_9` none for `Laws_of_Robotics.md`. One added row each would close them (the `Phase_7` meta row L26 still says "11 of 11 … exist on disk" while the spine block has 13 and the header now says 8 of 13 — an inconsistent count, left alone).
3. **`Phase_9.md` row 12 (Laws of Robotics) is not word-for-word and cites a sheet that does not carry it.** Sheet: "1. A robot will have full capacity … 2. A robot will understand that anything she is capable of doing to others is realistically possible for others to do to her." Source `Laws_of_Robotics.md` L3–L4: "have **the** full capacity" and "anything she is capable of doing to others, **it is also** realistically possible for others to do to her." The citation is `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md`, which holds neither law (search: no hit for "future possibilities" or "Laws of Robotics"; only an aside "Law 1"). The file `Laws_of_Robotics.md` is not named.
4. **Composition file founding note (L262)** says Halley's initial settlement was "South African and Argentine"; the Founding Register row L46 says "The UK, in a central role" (partial, `DR-22`). The new `Phase_2` rows cite the section by range and do not quote it; Step −1 will decide the spans. For the developer's awareness.
5. **Hit lists are mechanical (as the Pre-Trip already says).** Some listed lines are other cities' rows or the subnet's: `16` L301 is the Halley-subnet aggregate row (7,533,054); `09` L54 (Neumayer), L61–65 and L74 are rows of other cities in the Halley subnet; `16` L53 is "Halley VI" among real-world anchors. All kept as the ledger lists them.
6. **`09` row in `Phase_4`:** the file's L1 note says the Required and % WF columns "remain the superseded old-B1 model" (only Humans / Residents / Workforce were refreshed 2026-10-28). The row now carries Halley's own values as the ledger asks; it does not carry that label.
7. **SH-014 range:** the ledger gives L1287–1305; the text ends at L1304 (L1305 is blank). Cited as L1287–L1304.
8. **Pass `README.md`:** the first block still says "Folder opened 2026-09-05. ⚠ Empty by design." (the folder now holds the Pre-Trip, ledger and 19 datasheets). Not in the ledger; left.

---

## 4 · Files edited (Edit tool only)

Pass folder `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Halley_Subnet/Halley/`:
- `00.0_Pre-Trip_Inspection.md`
- `README.md`
- `Datasheets/Step_0.md`, `Datasheets/Step_1_and_2.md`, `Datasheets/Step_3.md`
- `Datasheets/Phase_2.md`, `Phase_3.md`, `Phase_4.md`, `Phase_5.md`, `Phase_6.md`, `Phase_7.md`, `Phase_8.md`, `Phase_9.md`, `Phase_10.md`

Unedited (checked, nothing to change): `Step_-1.md`, `Step_5.md`, `Step_6.md`, `Step_7.md`, `Step_8.md`, `Step_9.md`, `Step_10.md`, `00.2_Position_Coverage_Ledger.md`.
Created: this report. Nothing committed; no source, spec, census, Register, builder script, `FIX_LEDGER.md` or `TRACKER.md` touched.
