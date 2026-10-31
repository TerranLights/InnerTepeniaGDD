# Signy — sweep report (2026-10-30)

**City:** Signy (ledger section B33; pass folder `PASSES/Palmer_Subnet/Signy`).
**Who:** sub-agent, sweep run for the orchestrator. **Date:** 2026-10-30.
**Read:** `SWEEP_BRIEF.md` (all, with §4a); `FIX_LEDGER.md` section A (SH-001…SH-023, incl. SH-013 and SH-014) and section B33; `Signy_Audit.md` (all); the whole Pre-Trip (565 lines), the pass `README.md`, `00.2_Position_Coverage_Ledger.md`, and all 19 datasheets; every live source line named below (spec `Specs/Palmer subnet/Signy.md` L1–L80, L175–L200, L239–L243; `Inspirational-Influences.md` L232–L248; `Highways.md`, `Airports.md`, `Ports.md`, `City_Relationship_Database.md`, `City_National_Connections.md`, `City_Cross_Subnet_Relationships.md`; `16` L1, L222–L264, L936–L1025, L1285–L1306; `09` L1–L12, L52, L73; `Extent_and_Density_Per_City.md` L59, L296–L345, L511, L522–L541, L599–L631; `Upper_Earth_Immigration_Composition.md` L21–L70, L130–L146, L232–L246; `03_The_Phase_Spine.md` MUST OPEN blocks for Phases 0–10; `00_RUNBOOK.md` L1821–L1855, L1982, L2178–L2181, L3057, L3150–L3153; `02_Generators…` L610, L636–L637; `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` L612–L708; the first lines of the Tier U sheets cited by the datasheets). **Withheld files were not opened** (megasheets, the city's culture / Enneagram / vision-note / symbol files, Background-Lore vignettes). The GDD `Worldspace/Characters/` tree was searched by file name only (`grep -ril`); no character file was opened. `graphify` was not run (brief §5).
**Tools:** Edit only for every change. Two read-only Python checks (`-I`) in the scratchpad compared every copied row and every line list with the live files (all PASS; output summarized under "Checks").

## 1 · Results, one row per ledger entry and per shared fix

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| SG-001 | APPLIED | Pre-Trip §C Step 0 (L99), §C Step 2 (L126), §D Phase 1 (L256), §D Phase 5 (L303–309), §E (L392) | Highways L303, 313, 327, 330 → **L318, 328, 340, 342, 345**; Airports L42, 49, 86 → **L45, 52, 89**; Ports L471, 474, 498, 710, 728, 836 → **L494, 497, 501, 521, 733, 751, 859** (L5, 15, 148, 157, 180 same); RelDB L422–423, 425, 428, 501, 506, 513 → **L433–434, 436, 439, 512, 517, 524** (L46, 53 same; entry L433–L442, lines L434–L439); NatConn L328, 339–340, 466, 594 → **L329, 340–341, 471, 599** (L144, 146, 204, 238–239 same); CrossSub L202 same; `16` row L263 → **L264**; 21 other lines → **L318, 955, 957, 963, 968, 973, 987, 995, 998, 1009, 1016–1017, 1020, 1654, 1714, 1749, 2023, 2026, 2036, 3565, 3568** and **L940** added (22 lines); Extent list + **L296, L335**. The upper-case hits are labeled in the lists ("the city's own upper-case …") | Live `grep -n -i signy` of each file compared with the cited list by script: Highways [318, 328, 340, 342, 345], Airports [45, 52, 89], Ports [5, 15, 148, 157, 180, 494, 497, 501, 521, 733, 751, 859], RelDB [46, 53, 433, 434, 436, 439, 512, 517, 524], NatConn [144, 146, 204, 238, 239, 329, 340, 341, 471, 599], CrossSub [202], `16` 22 lines, Extent 22 lines (L59 is cited separately as the row) — **all equal**. Each odd hit opened (L340, L501, L335, L296, L940, L433): all the city's own lines |
| SG-002 | APPLIED | Pre-Trip §C intro box (L53); §J row (L528); §I L483 left | "(**not yet built** — November item N-5; the addresses below are where the files will be created)" → "(**19 files, all present**)"; §J row "Datasheets not yet built for this city" deleted; §I `DATASHEET-NOT-YET-BUILT(N-5)=20` left as the dated build record (ledger) | `ls Datasheets/` = 19 files. `grep -rn -i "not yet built\|N-5"` over the folder now hits only the §I verification line (`DATASHEET-NOT-YET-BUILT(N-5)=20`, left on purpose) |
| SG-003 | APPLIED | Pre-Trip §C Step 0 (L99) | "Signy's row **59**" → row 59 labeled the first-pass table (Signy I., 19 km², 188,694, 9,931/km², the island alone; 2026-09-05 snapshot; census live — note L631); added the city's declaration: Extent **§7 heading L296, section L296–L393, status row L511**, and `Specs/Signy.md` **L29–L50**; lines 522–540 and 601–604 kept (method lines), 601–604 labeled snapshot (SH-011) | Extent L59 `Signy I. \| 19 \| 188,694 \| 9,931` read live; L296 heading, L298–L306 ruling and table, L511 status row read live; §7 ends at L393 (L395 is `---`, L397 `# 8`); spec L29–L50 read live |
| SG-004 | HELD | — | alias set — DECIDE; untouched | — |
| SG-005 | APPLIED | `README.md` | spec pointer `../../../Specs/Signy.md` → `../../../Specs/Palmer subnet/Signy.md`; opening "⚠ Empty by design…" → "the folder holds the Pre-Trip sheet, the Position-Coverage ledger and the 19 datasheets in `Datasheets/`; the pass's own output files … appear here one at a time, as each piece is run — never pre-created" | `ls` confirms the new spec path and the local-culture, vision-note and picks pointers resolve (existence only). The research-log pointer stays absent as the README itself says |
| SG-006 | APPLIED | Pre-Trip §D Phase 10 "Characters" row (L369) | added: this project's `Worldspace/Characters/` tree names Signy in **6 files**, all in `Dolls/Still-Present_-_In-Game/recruitable/TBN [TCY-45 heavenly summertime Momo]/` — `README.md`, `Personal_Background/PreWar_History.md`, `War_Experiences.md`, `Loyalties.md`, `Timeline.md`, `Relationships.md` (names only, not opened); timeline-repo tree: 587 files, 0 hits (re-run) | `grep -ril signy` on the GDD tree = exactly those 6 paths; timeline-repo `find … -name '*.md'` = 587, `grep -ril` = 0 |
| SG-007 | HELD | — | timeline-repo flags — DECIDE; untouched (the timeline repo takes no edits) | — |
| SG-008 | APPLIED | Pre-Trip | shared items — see SH rows below | — |
| SG-020 | APPLIED | `Step_3.md` | section "L203–L216" → "**L234–L246** (heading L234, picks L235–L246)"; the 12 pick citations L204…L215 → **L235…L246**; the excluded row (old L214) replaced by the Vestmannaeyjar pick copied as written, cited L245 | Script: all 12 pick rows equal live L235–L246 text and cite their own line; L234 is `##### Signy` |
| SG-021 | APPLIED (prose omitted) | `Step_1_and_2.md` (Half B row, new §8 row); `Phase_4.md` row 3 + new row; `Phase_7.md` row 1 + new row | Half B row cite L263 → **L264** (header L247 kept), labeled "first-pass split, written 2026-09-02; the city's own determination in the next row supersedes it"; new §8 row: baseline 58,480 (41.1%) · mandated 46,006 (32.4%) · FREE 37,641 (26.5%) · sum 142,127 · distinctive 83,647 (58.9%) · mandate 30% marine/fishing FULL = 25,094 · 15% biological/ecological research HALF = 12,547 · 10% maritime trade HALF = 8,365 · sum 46,006 (55%); cite `16` **L940–L1022** (heading L940; table L942–L946; distinctive tier L948; mandate L953–L958). The ledger's narrative points (siligel shortage and "survived" status set aside as post-war, food double-count, two-island commute internal) were **not copied**: rule 3 (value + citation only) and the Second Interwar default scope; the cited range holds them. See New findings F-3 on the "supersedes" wording | Arithmetic by hand below; row text equals live L944–L946, L948, L953–L958; `16` L264 row equals the sheet's Half B cells |
| SG-022 | APPLIED | `Phase_5.md` | Highways L303→**L318**, L313→**L328**, L327→**L342**, L330→**L345**, **L340 added** (withheld: compares the city with other places); Airports L42→**L45**, L49→**L52**, L86→**L89**; Ports L471→**L494**, L474→**L497**, L498→**L521**, L710→**L733**, L728→**L751**, L836→**L859**, **L501 added** (the city's own port row, copied as written with `\|` escapes); RelDB entry L422–L431 → **L433–L442** (heading L433, lines L434–L439), rows L423/424/425/426/427/428 → **L434/435/436/437/438/439**; NatConn "10 line(s)" list → L144, L146, L204, L238–239, **L329, L340–341, L471, L599** | Script: every value equals (or sits inside) its live line; every withheld row's line names Signy; live name-hit lists equal the cited sets; NatConn count 10 = 144, 146, 204, 238, 239, 329, 340, 341, 471, 599 |
| SG-023 | APPLIED | `Phase_7.md` row 2 | "21 line(s): L315 … L3563" → "**22 line(s)**: L318, **L940**, L955, L957, L963, L968, L973, L987, L995, L998, L1009, L1016–1017, L1020, L1654, L1714, L1749, L2023, L2026, L2036, L3565, L3568" (L940 labeled the city's own upper-case heading); same list in the citation cell | list equals the live `grep -n -i signy` of `16` minus L264 (script) |
| SG-024 | APPLIED | `Step_1_and_2.md` climate-type row; prevailing-winds row | "the mildest climate in the Palmer subnet" → `*[one clause compares the city with other places; not copied]*`; "**The most wind-exposed Palmer subnet city;** the open-ocean position provides no shelter" → `*[one clause compares …]*; **the open-ocean position provides no shelter**`; all figures kept | spec L177, L200 read live; the clauses withheld are exactly the quoted ones |
| SG-025 | HELD | — | DECIDE (L180 temperature-range label); untouched | — |
| SG-026 | APPLIED | `Step_1_and_2.md` `Settled:` row | "[source line excluded: later-era content …]" → spec L239 copied as written (Post-Falkland Treaty … the 2564 exiles converted it to year-round habitation …); the 1976 sentence (L243) is not in the row | Script: row value equals L239 minus the `**Settled:** ` label, character for character |
| SG-027 | APPLIED | `Step_0.md`, `Step_1_and_2.md` | new row in each: "Extent (the sources' own declaration; 2026-09-05 snapshot; the census is live — note L631)": spec extent band · Extent §7 text · 188,694 unchanged · density on Signy I. alone 9,931/km² · first-pass row; cites Extent L296–L306 (heading L296; ruling L298–L300; table L302–L306), L511, L59 and spec L29–L50 (band L30) | Extent L305 "Signy I. 19 km² + a moored settlement around Coronation I.", L306 "9,931/km²", L511, L59 and spec L30 read live. "plausible" (L59) and "top of the band" (L306) not copied (judgment words) |
| SG-028 | HELD | — | DECIDE (N-line counts, SH-009); untouched, including `Step_10` "(430 lines)" | — |
| SG-029 | PARTIAL | `Phase_5.md` | labeled "(fragment of a wrapped paragraph)": Highways L342, Airports L45, Airports L89, Ports L15, Ports L497, Ports L521, Ports L751 (7 rows). **Ports L494 not labeled: SKIPPED-MISMATCH** | Live L494 is two complete sentences ("Pergamino, Contrapunto and Signy all carry `Access type: NONE` — no road." / "Signy has no airstrip either."), not a fragment as the ledger says. Whole-sentence copying was not chosen for the others because the sentences are multi-city lists or continue into comparing or post-war text (see F-4) |
| SG-030 | APPLIED | `Phase_6.md` | README L180 row "The Cyclical (Signy/Utstein) …" → `*[source line compares the city with other places; not copied, line number recorded only]*` — now L25, L180 and L228 are all withheld | L25 and L228 read live (both compare the city with the whole corpus); L180 names another city |
| SG-031 | PARTIAL | `Phase_7.md` | header recounted by hand (SH-008): "13 of 13" → **"8 of 13"**. The last row ("MUST-OPEN coverage … **11 of 11** … exist on disk") **left as is** (brief §4a: leave and report) | the row restates an older count (11) of the same list, which the spine's Phase 7 block gives as 13 addresses; see F-5 |
| SG-032 | NOTE | — | optional census-note row; untouched | — |
| SG-S01…S10 | HELD / NOTE | — | spec entries (1976 occupation, 60° parallel, distances, record extremes, daylight line, peer lines, founders annotation, where the people live, megasheet pointers); not touched | — |
| SH-001 | APPLIED | Pre-Trip §G row "No invented person names" | spine **L127 → L220, L1114, L1140** | spine L220 "and the no-invented-person-names rule", L1114 "NO INVENTED PERSON NAMES — role placeholders permanently", L1140 "People as role-archetypes — binding rule: no invented proper names" read live; runbook L1982 (Phase 10 row) also names the rule — kept; no datasheet cites spine L127 |
| SH-002 | APPLIED | Pre-Trip §G row "Divergence operator" | runbook **L2178 → L2180** (heading "THE DIVERGENCE OPERATOR") | L2180 `### ⭐ THE DIVERGENCE OPERATOR` read live (L2178 is an unrelated table row) |
| SH-003 | APPLIED | Pre-Trip §C Step 5 `T8` | `02_Generators…` §5.3 "610–684" → **610–636** | L610 `## 5.3 The both-are-true test`; L637 `# 6. Symbol binding` |
| SH-004 | APPLIED | Pre-Trip §C items 4 and 5 | item 4 "lines 620–643 and 701–703" → "**620–643 (the four questions) and 682–684 (the fifth section …)**"; item 5 "lines 650–703" → "**667–684**, the amended merge rule …" | trial recipe L620–L643 (Round 3 prompt, four questions), L682–L684 ("Round 3's prompt now carries a fifth section …"), L667 (`AMENDED 2026-09-28 — THE WRITTEN CONTENT IS A MERGE, NOT A PICK`) to L684 (box ends; L685 blank). L701–L703 is an unrelated 2026-09-11 correction box |
| SH-005 | APPLIED | Pre-Trip §C Step 10 | "3057–3172" (twice) → **3057–3152**; card note "live lines 3045–3161 govern" → "**3057–3152**" | runbook L3057 `# Step 10 — THE READINESS CHECK`, L3153 `# Where everything lives` |
| SH-006 | ALREADY-RIGHT | `Step_-1.md`, Pre-Trip | the "Specs `Status:` field" row cites `00_RUNBOOK.md` by name only ("the Second Interwar default"), no L1821–1822 anywhere | `grep -n "1821\|1822"` in the Pre-Trip and all datasheets = no hit |
| SH-007 | HELD | — | no `01` "line 65" coordinate occurs in this city's files (`grep` for "line 65", "L65", "Resettled" = no hit); nothing to leave or change | — |
| SH-008 | APPLIED | the 11 datasheets that carry the header | recounted by hand; see section 2 | section 2 |
| SH-009 | HELD | — | "N-line file" counts untouched | — |
| SH-010 | APPLIED | Pre-Trip §D Phase 2 table (new row); `Phase_2.md` (2 new rows) | the city's own section (**heading L234, section L234–L242**) and the solar-UTC rule (**heading L21; the list "Recording it so it stops being reconstructed from examples" L26–L33, rule 1 at L28; refinement box L35–L63**); form copied from the Santa Luce / Relung Panen rows (form only); "registered, not dispatched" | composition file read live: L21, L26, L28, L33, L35–L63, L234, L236–L240, L242 (key note), L244 (`---`) |
| SH-011 | APPLIED | Pre-Trip L99, L392; `Step_0.md` and `Step_1_and_2.md` extent rows | "(2026-09-05 snapshot; the census is live — note L631)" beside the Extent citations | Extent L631 read live: "Snapshot note, 2026-10-28 … The table was left as the dated record; the census is the live source." |
| SH-012 | APPLIED | Pre-Trip + `Phase_5.md` + `Phase_7.md` | all stale line numbers into `16`, Highways, Airports, Ports, RelDB, NatConn (see SG-001/022/023); unchanged and re-read live: `09` L52/L73, CrossSub L202, Register L45/50/82/90/94, Topics L241, Precipitation L173/226–227, Sweep L129/178/188/221, Factions L191–203, Polydimensional Animism L25/180/228, DoI README L49 | lines read live (`09` L73 = Signy row 142,127 / 35.6%) |
| SH-013 | APPLIED | `Step_1_and_2.md`, `Phase_4.md`, `Phase_7.md`; Pre-Trip §D Phase 1 and §E `16` lists | the city's own §8 (shares) quoted beside Half B; Half B labeled the first-pass split, §8 "supersedes" it; L940 listed in the Pre-Trip's `16` lists as the city's own upper-case heading | see SG-021 and F-3 |
| SH-014 | APPLIED | `Step_1_and_2.md`, `Phase_4.md`, `Phase_7.md` (each: Half B row and §8 row) | clause added: "on the flat ABCC working value; counts re-run when per-city ABCC values are set (`16` L1287–L1304)" | `16` L1287 `### ⚠ CONSEQUENCE — the ten determinations so far need a baseline re-run`; L1302–L1304 "ABCC stays at the flat 65 per 1,000 residents for ALL cities … in one pass"; **L1305 is blank**, so the cite is L1287–L1304 (brief §4a) |

### Counts
APPLIED 24 (13 per-city + 11 shared) · PARTIAL 2 (SG-029, SG-031) · ALREADY-RIGHT 1 (SH-006) · HELD 6 (SG-004, SG-007, SG-025, SG-028, SH-007, SH-009) · SKIPPED-MISMATCH 1 sub-row (Ports L494, inside SG-029) · NEEDS-DEVELOPER 0 entries (three new findings below need a ruling: F-1, F-2, F-3). SG-S01…S10 and SG-032 untouched by design.

### Arithmetic by hand (SG-021)
- Workforce: 95,560 + 0.5 × 93,134 = 95,560 + 46,567 = **142,127** (equals Half B and `16` §8 total).
- Tier counts: 58,480 + 46,006 + 37,641 = 104,486 + 37,641 = **142,127** ✓.
- Shares (five decimals, then one decimal as `16` prints): 58,480 ÷ 142,127 = **0.41146** → 41.1% · 46,006 ÷ 142,127 = **0.32370** → 32.4% · 37,641 ÷ 142,127 = **0.26484** → 26.5% · (0.41146 + 0.32370 + 0.26484 = 1.00000).
- Distinctive tier: 46,006 + 37,641 = **83,647**; 83,647 ÷ 142,127 = **0.58854** → 58.9%.
- Mandate: 83,647 × 0.30 = 25,094.1 → **25,094**; × 0.15 = 12,547.05 → **12,547**; × 0.10 = 8,364.7 → **8,365**; 25,094 + 12,547 + 8,365 = **46,006**; 55% × 83,647 = 46,005.85 → 46,006 ✓.
- Retention (Step_0 / Phase_2, unchanged, re-run): 133,755 ÷ 188,694 = 0.70885 → 70.88% (0.708849…) · 53,928 ÷ 93,134 = 0.57904 → 57.90% · 79,827 ÷ 95,560 = 0.83536 → 83.54%; robots' share of Census I 95,560 ÷ 188,694 = 0.50643 → 50.64% (Phase_9, unchanged).

## 2 · MUST-OPEN recount (SH-008), by hand

Rule applied: an address counts only if a row transcribes it or cites it by its full path / full file name; a row that cites a shared Tier U sheet counts as "via Tier U" (the sheet's own source line was read to confirm it covers the address). ⚑ = judgment call. N was confirmed against the spine's MUST OPEN block for each phase (Phase 0: 3 · 1: 6 · 2: 3 · 3: 5 listed, Davis is "where applicable" → 4 · 4: 7 · 5: 6 (the Infrastructure/ line names Airports, Ports and Geothermal_Heating together) · 6: 5 · 7: 13 · 8: 2 · 9: 4 · 10: 3).

| Sheet | Address | Covering row | k of N |
|---|---|---|---|
| **Step_0** (Phase 0) | `Repo_Scope.md` | row "**U** `Repo_Scope.md`" (direct) | |
| | Timeline Eras/ | rows citing `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` (its source line: `Timeline Eras/2 The Second Interwar Period/README.md`) — via Tier U ⚑ | |
| | `Official_Population_Census.md` | Census I and Census II rows (direct) | **3 of 3** (2 direct, 1 via) — unchanged |
| **Step_1_and_2** (Phase 1) | Locations/ (universe repo) | row "Universe repo `Worldspace/Locations/` — directory enumerated" ⚑ (ellipsis-prefixed form `…/Worldspace/Locations/`) | |
| | Specs/ | rows citing `Specs/Signy.md` ⚑ (directory-qualified) | |
| | `Energy_Grid_Failure_Rationale.md` | its row (direct) | |
| | READER/ | rows citing `READER/Signy.md` L4–L14 ⚑ (directory-qualified) | |
| | Stations/ | rows for `Antarctic_Stations_With_Airstrips.md` and `COMNAP_Antarctic_Station_Catalogue.pdf` ⚑ (files inside the folder) | |
| | `16_Per_City_Three_Tier_Run.md` | Half B row and §8 row (direct) | **6 of 6** (6 direct, 0 via) — unchanged |
| **Phase_2** | `No_National_Stereotypes.md` | "GPS law" row, cites `…/No_National_Stereotypes_Quick_Reference.md` (source line names `Reference/No_National_Stereotypes.md`) — via Tier U | |
| | Falkland_Treaty/ | three Falkland rows, cite `…/Falkland_Treaty_Quick_Reference.md` (source: `Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md` + Scaffold + Real_World_Influences) — via Tier U | |
| | `Official_Population_Census.md` | rows citing L122–124, L515, L635 (direct) | **3 of 3** (1 direct, 2 via) — was "3 directly, 0 via" |
| **Phase_3** | READER/ | **not covered** — no row of this sheet names it (its rows are in `Step_1_and_2.md`) | |
| | Specs/ | rows `Specs/Signy.md` L159, L247, L264 ⚑ | |
| | City_Concept-Art/ | row "Concept-art directory status" cites `City_Concept-Art/Palmer_Subnet/Signy` ⚑ | |
| | City_Megasheets/ | row "Megasheet Physical Infrastructure file" (names `Signy_Physical_Infrastructure_Attributes.md`, folder of 7) ⚑ | |
| | Davis_Geosciences_Research/ | not counted: "where applicable", Davis only (the header says so) | **3 of 4** (3 direct, 0 via) — was 4 of 4 |
| **Phase_4** | `Robot_Physiology_and_Cultural_Practices.md` | rows cite `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md` (its source line names this file) — via Tier U | |
| | `Robot_Cold_Physiology.md` | row "Robot Cold Physiology — the governing mechanic (Tier U)", same Tier U sheet (its source line names the file) — via Tier U | |
| | `16` | Half B row, §8 row (direct) | |
| | `09` | row 1 (direct) | |
| | `11_Caloric_Rebuild_and_Livestock_Tier.md` | row 2 (direct) | |
| | `National_Medical_and_Care_Institutes.md` | row 4 (direct) | |
| | `National_Economy_and_Currency.md` | **not covered** | **6 of 7** (4 direct, 2 via) — was 7 of 7 |
| **Phase_5** | Locations/ (universe repo) | row 1 ⚑ (ellipsis-prefixed) | |
| | `Highways.md` | rows (direct) | |
| | Infrastructure/ (Airports.md · Ports.md · Geothermal_Heating.md) | rows for `Airports.md`, `Ports.md`, `Geothermal_Heating.md` ⚑ (one address, three named files) | |
| | `City_Cross_Subnet_Relationships.md` | row (direct) | |
| | `City_Relationship_Database.md` | rows (direct) | |
| | `City_National_Connections.md` | row (direct) | **6 of 6** (6 direct) — unchanged |
| **Phase_6** | Robot_Religions/ | rows `Factions/Robot_Religions/` and the Polydimensional_Animism rows | |
| | `National_Holidays.md` | row | |
| | Ice-Cold_Buddhism_Research/ | row | |
| | `The_True_Believer_Extraction.md` | row | |
| | `The_Meme_Machine_Extraction.md` | row | **5 of 5** (5 direct) — unchanged |
| **Phase_7** | `Division_of_Industry/` | the READ-FIRST box cites `…/Division_of_Industry_Reliability_Quick_Reference.md` (source: DoI `README.md` + `10_Validation_Findings…`) — via Tier U ⚑ (the box, not a table row; the row "`01_Burden_Scoring_Model.md` — status stamp" cites the base name `README.md` only) | |
| | `16` | rows 1, 2 (direct) | |
| | `Division_of_Industry_Sweep_2026-08-31.md` | rows (direct) | |
| | `01_Burden_Scoring_Model.md` | row (direct) | |
| | `08_Volume_Based_Requirement_Reference.md` | **not covered** | |
| | `National_Medical_and_Care_Institutes.md` | **not covered** (it is in `Phase_4.md`, not here) | |
| | Theoretical-Calculations/ | row (direct) | |
| | Industry_Staffing_and_Productivity/ | **not covered** | |
| | jobs_professions_and_fields/ | row (direct) | |
| | `National_Economy_and_Currency.md` | **not covered** (the box mentions "national currency" but not the file) | |
| | `City_Logistics.md` | row (direct) | |
| | Factions/ | row (direct) | |
| | Megacorps/ | **not covered** (the Tier U sheet `Phase_7_Roster_and_Model_Files_Quick_Reference.md`, which covers it, is not cited in this sheet) | **8 of 13** (7 direct, 1 via) — was 13 of 13 |
| **Phase_8** | Robot_Biology_and_Culture/ | row "`Robot_Biology_and_Culture/` mandatory facts" (names the directory; value cited to the Tier U sheet) | |
| | `Weapons_and_Tools_Philosophy.md` | row | **2 of 2** (2 direct) — unchanged |
| **Phase_9** | `Laws_of_Robotics.md` | **not covered** ⚑ — the row "Laws of Robotics (Tier U)" paraphrases the laws and cites `Robot_Physiology_Quick_Reference.md`, which does not carry them (F-1). If the paraphrase is accepted as a transcription the count is 4 of 4 | |
| | Robot_Universals/ | row 1 `Reference/Robot_Universals/` (direct ⚑ short form); rows Ch. 13 / Ch. 14 | |
| | `Doll_Representation_Categories.md` | row (direct) | |
| | `Robot_Physiology_and_Cultural_Practices.md` (human-robot baseline) | the three rows citing `Robot_Physiology_Quick_Reference.md` — via Tier U ⚑ (no row addresses the baseline itself) | **3 of 4** (2 direct, 1 via) — was 4 of 4 |
| **Phase_10** | Characters/ (timeline repo) | row 1 `Worldspace/Characters/` ⚑ (repo-qualified) | |
| | `Enneagram_Character_Index.md` | row 2 (direct) | |
| | `Zodiac_Signs_Full_Attributes.md` | row cites `Corpus_Reference_Sheets/Zodiac_Signs_Quick_Reference.md` (source line names the file) — via Tier U | **3 of 3** (2 direct, 1 via) — was "3 directly" |

Sheets with no MUST-OPEN header (`Step_-1`, `Step_3`, `Step_5`–`Step_10`) were not touched for SH-008.

## 3 · New findings (not in the ledger; not fixed)

- **F-1 · `Phase_9.md` "Laws of Robotics (Tier U)" row is wrong twice.** It cites `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md`, whose source line lists `Robot_Physiology_and_Cultural_Practices.md`, `Robot_Cold_Physiology.md` and `Robot_Universals/` Ch. 13 and 14 — not `Laws_of_Robotics.md`; a search for "maximize her own" in all of `Corpus_Reference_Sheets/` finds nothing. And the text is a paraphrase of `Laws_of_Robotics.md` L3–L4 ("have **the** full capacity …"; "anything she is capable of doing to others, **it is also** realistically possible for others to do to her"). Needs a ruling (copy the two laws word for word and cite `Laws_of_Robotics.md` L3–L4, or cite a Tier U sheet that holds them).
- **F-2 · `Phase_4.md` row 1 copies the `09` columns that `16` and `09` call superseded.** Row: "Required: 50,598 … % WF: 35.6%". `16` L28–L32 says "discard its `Required` and `% WF` columns, which used the circular B1 rate", and `09`'s own header (L1) says the Required and % WF columns "remain the superseded old-B1" figures. The population, workforce and D cells in the row are fine. Left as is (not in the ledger); no SH-014 clause was added to this row for the same reason.
- **F-3 · No source line says that `16` §8 supersedes Half B for Signy.** `16` L1 (2026-10-28) says only that the per-city determinations "were NOT recomputed"; the "replaces the 0.0% that stood in Half B" sentences exist for other cities. The "supersedes" wording in the three sheets follows SH-013 and the audit (D-02) and is attributed to "manual-input audit, 2026-10-30" in the row. If the developer would rather the sheets quote both and leave the ranking to him, delete the clause in the row label and in the Pre-Trip's `16` row. (Both quantities share workforce 142,127 and base 41.1%; only MAND% / FREE% differ: 17.7 / 41.2 against 32.4 / 26.5.)
- **F-4 · Peer clauses the ledger did not list, still copied in this city's sheets:** `Step_-1.md` "Highway access" row (spec L7: "the most isolated Palmer subnet city; even within the Palmer subnet, Signy is a significant sea voyage from the nearest other city"); `Step_1_and_2.md` "Spec climate — polar night" row (spec L181: "the northernmost city in the Federation"); `Phase_5.md` Highways L328 row ("A significant sea voyage even from the nearest other Palmer-subnet city"); `Phase_5.md` Highways L342 fragment, which opens the comparing clause "the most isolated Palmer subnet city" and whose sentence continues into war-survival text at L343–L344 (labeled a fragment per SG-029, but withholding it as the other Highways lines are would be the consistent treatment); `Phase_5.md` Ports L494 row names two other cities in one sentence. Same pattern as SG-024.
- **F-5 · `Phase_7.md` last row still says "11 of 11 … exist on disk"** while the spine's Phase 7 block lists 13 addresses and the recounted header reads 8 of 13. Left per brief §4a (SG-031 asks to make them agree; the brief says leave and report). If the row is meant to restate the header, the fix is a one-word change after the developer decides the convention.
- **F-6 · Rows missing for must-open addresses** (gaps for the developer to decide on, not filled): `Phase_3`: READER/; `Phase_4`: `National_Economy_and_Currency.md`; `Phase_7`: `08_Volume_Based_Requirement_Reference.md`, `National_Medical_and_Care_Institutes.md`, `Industry_Staffing_and_Productivity/`, `National_Economy_and_Currency.md`, `Megacorps/`; `Phase_9`: `Laws_of_Robotics.md` (see F-1).
- **F-7 · Pre-Trip §C Step 0 cites Extent L522–540 and L601–604, which are the "other 25" (continental cities) section and table;** Signy is one of the eleven island-capped cities (§2 result table row 59, §7), and none of L522–L628 names it. The ledger asked only to add the city's declaration; the two ranges were kept and labeled, not removed. The developer may want them dropped from Signy's Step 0 reads.
- **F-8 · Pre-Trip §I (L484 after the edits) still records `DATASHEET-NOT-YET-BUILT(N-5)=20`** in its dated 2026-10-21 verification block; left as the dated build record per the ledger. A reader who sees "20" next to "19 files, all present" in §C should read §I as a snapshot.

## 4 · Checks run (read-only)
- Script 1 (all PASS): the 12 `Step_3` pick rows equal live `Inspirational-Influences.md` L235–L246 and cite their own lines; `Settled:` row equals spec L239; `Ports.md` L501 row equals the live row (pipes escaped); every `Phase_5` copied value sits inside its live line; every withheld row's line names Signy; `16` L264 equals the Half B cells; `16` L940 heading; L1287 heading; L1304 text; L1305 blank.
- Script 2 (all OK): every "Names Signy at" list in the Pre-Trip equals the live case-insensitive hit set of its file; the `16` lists (§D Phase 1, §E) equal the live hits minus L264 (22 lines); the Extent lists equal the live hits minus L59.
- Runbook Step ranges in Pre-Trip §C (12 of 12) equal the live `# Step` headings.
- `git diff --stat` for the folder: 14 files, 88 insertions, 77 deletions; nothing outside the allowed files changed. No commit made.

## 5 · Files edited (full paths)
Pass folder `PASS` = `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Palmer_Subnet/Signy`
- `PASS/00.0_Pre-Trip_Inspection.md`
- `PASS/README.md`
- `PASS/Datasheets/Step_0.md`
- `PASS/Datasheets/Step_1_and_2.md`
- `PASS/Datasheets/Step_3.md`
- `PASS/Datasheets/Phase_2.md`
- `PASS/Datasheets/Phase_3.md`
- `PASS/Datasheets/Phase_4.md`
- `PASS/Datasheets/Phase_5.md`
- `PASS/Datasheets/Phase_6.md`
- `PASS/Datasheets/Phase_7.md`
- `PASS/Datasheets/Phase_8.md`
- `PASS/Datasheets/Phase_9.md`
- `PASS/Datasheets/Phase_10.md`

Report: `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Signy_Sweep.md`. Not edited: `Step_-1`, `Step_5`–`Step_10`, `00.2_Position_Coverage_Ledger.md`, the spec and every other source file.
