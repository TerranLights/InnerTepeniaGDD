# Zukelli — sweep report (2026-10-30)

**City:** Zukelli (ledger section B21; pass folder `PASSES/Janbogo_Subnet/Zukelli`). **Who:** sub-agent (Sonnet 5.5), one pass, Edit tool only. **Name:** the pending rename is not swept; every edit is written against the current name.
**Read first:** `SWEEP_BRIEF.md` in full (incl. §4a); `FIX_LEDGER.md` section A and `### B21 · ZUKELLI`; `Zukelli_Audit.md`; then the whole Pre-Trip (565 lines) and all 19 datasheets and the pass `README.md`, before any edit.
**Live sources opened for every number written** (read again at sweep time, not copied from the ledger): `Official_Population_Census.md` (L250–256, L491, L589, L613, L780–781, L804); `Extent_and_Density_Per_City.md` (L596–599, L601–604, L614, L631); `16_Per_City_Three_Tier_Run.md` (L236–252, L268, L1280–1310, L2650–2655, L2740–2832, plus a live `grep -n -i` of the whole file); `09_Per_City_Baseline_Run.md` (L48–67, L126); `Highways.md`, `Airports.md`, `Ports.md`, `Geothermal_Heating.md`, `Arcanet.md` (live `grep -n -i`, then the cited spans); `City_Relationship_Database.md`, `City_National_Connections.md`, `City_Cross_Subnet_Relationships.md` (live `grep -n -i`, then the cited spans); `Upper_Earth_Immigration_Composition.md` (L1–66, L405–420, live grep); `Founding_Register.md`, `Stations`, `Topics`, `Precip`, `READER` (grep); `03_The_Phase_Spine.md` (every MUST OPEN block, L127, L219–220, L272–292, L1101–1140); `00_RUNBOOK.md` (L1821–1822, L1854–1855, L1968–1982, L2090, L2150, L2178–2180, L2986–3056, L3057–3153); `02_Generators…` L609–637; `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` L620–690; `05_The_Input_Contract.md` L705–722; `Cross_City_Culture_Differentiation_Table.md` L44–50 (header only); the Zukelli spec L150–158; `TepenianUniverseTimeline/Worldspace/Locations/` (file count, plus its git history). Git history of `Ports.md` was used to find what the sheets' old `Ports` cites had pointed at.

**Counts:** APPLIED 22 (11 Zukelli entries: ZK-001, 004, 020, 021, 022, 023, 025, 026, 028, 029, 030; 11 shared fixes: SH-001, 002, 003, 004, 005, 008, 010, 011, 012, 013, 014) · ALREADY-RIGHT / not present 1 (SH-006; SH-013 is also already right in the sheets) · PARTIAL 0 · HELD 3 rows (SH-007, SH-009, SH-015…017 / SH-019) · SKIPPED-MISMATCH 1 (ZK-024) · NEEDS-DEVELOPER 0. ⚑ marks judgment calls (rows ZK-020, ZK-022, ZK-029, ZK-030 and the recount). `DECIDE` / `SOURCE` / `NOTE` entries (ZK-002, ZK-003, ZK-005, ZK-027, ZK-S01 … ZK-S06) were left untouched; ZK-006 is the pointer to the SH rows.

---

## 1 · Results, entry by entry

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| ZK-001 | APPLIED | Pre-Trip, "Names Zukelli at" lists (§C Step 0 reads, §C Step 2 reads, §D Phase 1 `16` row, §D Phase 5 rows, §E) | Census `L588`→`L589`; Highways `L226, L231`→`L227, L232`; Airports `L96`→`L99`; Ports list rebuilt (below); RelDB `L136, L301–302, L308, L501`→`L147, L312–313, L319, L512` (+ "the city's own entry is L312–L319"); NatConn `L400, L408, L440–442, L451, L454`→`L405, L413, L445–447, L456, L459` (+ L459 = the city's own `### Zukelli` heading); `16` row `L267`→`L268` (Step 2 reads, §D Phase 1, §E); the other 15 `16` hits rebuilt; §27 heading `L2744` added to the two `16` lists (§D Phase 1 row, §E row) | Live `grep -n -i -E 'zukelli\|zucchelli'` in each file, odd hits opened. **Ports (`-i`):** 197, 224, 240, 244, 264 (same) + **358** + 360, 363, 369, 384, 573, 734, 778, 782, 825, 860. L358 is the upper-case heading `## ✅ ZUKELLI SHARES THIS PORT`, which the builder's case-sensitive search missed and the ledger list does not carry; I added it, marked "the city's own upper-case heading". `16` (`-i`): 268, 2653, 2744, 2759, 2768, 2779, 2781, 2786, 2792, 2803, 2817, 2818, 2820, 2825, 2826, 2886, 2907, 3091, 3484. Unchanged and re-confirmed: Extent L598, CrossSub L56/182/206, Stations L14/26/71, Topics L290/320, Precip L162, Register L67/90/94, `09` L67, Cymatics L158. |
| ZK-002 | untouched (DECIDE) | — | — | — |
| ZK-003 | untouched (DECIDE) | — | — | — |
| ZK-004 | APPLIED | `Step_3.md` row 1 | pass README `L39`→`L40` | README L40 = "**Research log** … may not exist yet — Step F creates it"; L39 = Vision notes. |
| ZK-005 | untouched (DECIDE) | — | — | — |
| ZK-006 | APPLIED (see SH rows) | — | SH-001, 002, 003, 004, 005, 010, 011, 013 applied; SH-007 HELD | — |
| ZK-020 | APPLIED ⚑ | `Step_0.md` rows 16–18; `Phase_2.md` retention row | human `443,754 ÷ 627,584 = 70.71%`→`451,862 ÷ 639,723 = 70.63%`; robot `493,905 ÷ 631,067 = 78.27%`→`501,644 ÷ 642,845 = 78.03%`; spread `7.56`→`7.40 pp`; Phase_2 combined `74.50%`→`74.34%` (+ human, robot, spread as above) | **By hand:** human 639,723 × 0.70 = 447,806.1; 451,862 − 447,806.1 = 4,055.9; 4,055.9 ÷ 639,723 = 0.00634 → 0.70634 = **70.63%**. Robot 642,845 × 0.78 = 501,419.1; 501,644 − 501,419.1 = 224.9; 224.9 ÷ 642,845 = 0.00034985 → 0.78034985 = **78.03%** (it is below 78.035, so it does not round up). Combined 953,506 ÷ 1,282,568 = 0.743435 = **74.34%**. Spread 78.03 − 70.63 = **7.40 pp** (unrounded 7.401). Census rows re-read: L491 (639,723 / 642,845), L613 (451,862 / 501,644). ⚑ **The ledger and the audit say 78.04% and 7.41 pp; that is a rounding slip (78.0350 vs 78.03499). I wrote the hand-computed values. See New findings 1.** |
| ZK-021 | APPLIED | `Step_1_and_2.md` `16` row; `Phase_4.md` "Workforce cross-check" | `Step_1_and_2`: workforce `944,859`→`962,706`, base `41.4%`→`41.5%` (MAND 14.6 / FREE 43.9 kept). `Phase_4`: "`09` 944,859 = `16` 944,859 = sum of §27" → "`09` 962,707 · `16` 962,706 · §27 sum (391,579 + 55,328 + 497,952) = 944,859, the pre-`DR-68` workforce (631,067 + 0.5 × 627,584 = 944,859)"; citations `09` L67, `16` L268 / L2748–2750, census L491 | Live `16` L268 = `Zukelli \| Janbogo \| 1.25 \| 962,706 \| 41.5% \| 14.6% \| 43.9% \| C`. `09` L67 workforce 962,707. By hand: 642,845 + 0.5 × 639,723 = 642,845 + 319,861.5 = 962,706.5 (`16` 962,706; `09` rounds up). §27 sum: 391,579 + 55,328 = 446,907; + 497,952 = 944,859. Old workforce: 0.5 × 627,584 = 313,792; 631,067 + 313,792 = 944,859. Old Census I "was" figures read at census L491. |
| ZK-022 | APPLIED ⚑ | `Step_0.md` rows 19–20 | row 19: `L618 (table header L607, section L605)`→`L614 (table header L603–604, section L601)`; row 20: `L602–603`→`L598–599` | Live: L601 `## 📋 THE TABLE`, L603–604 header + separator, L614 `Zukelli \| Janbogo \| 1,258,651 \| 126 \| 180 \| Terra Nova Bay`. The quoted sentence runs over two lines: L598 "Terra Nova Bay carries two: Janbogo + Zukelli = 2,569,162, needing 257–367 km² on the Northern" / L599 "Foothills." ⚑ the ledger says "L598"; the two-line quote is **L598–599**, which is what I wrote. Values stand: 1,258,651 ÷ 10,000 = 125.87 → 126, ÷ 7,000 = 179.8 → 180; live 1,282,568 ÷ 10,000 = 128.26 → 128, ÷ 7,000 = 183.22 → 183. |
| ZK-023 | APPLIED | `Step_1_and_2.md` (row `L267`→`L268`, `L2756`→`L2761`); `Phase_4.md` (`L267, L2743–2745`→`L268, L2748–2750`; `L267, L2756`→`L268, L2761`); `Phase_7.md` (every `16` cite) | Phase_7: `L2739–2745`→`L2744–2750`; `L2756 vs L267`→`L2761 vs L268`; `L2747–2748`→`L2752–2753`; `L2750–2754`→`L2755–2759`; `L2758–2764, L2780–2781`→`L2763–2769, L2785–2786`; `L2776–2777`→`L2781–2782`; `L2802–2808`→`L2807–2813`; `L2812–2814`→`L2817–2819`; `L2739–2825`→`L2744–2830`; "not carried": `L2768–2774`→`L2773–2779`, `L2783–2800`→`L2788–2805`, `L2815–2822`→`L2820–2827` | Every number checked against its anchor in the live file: L2744 heading; L2746–2750 table; L2752–2753 "Distinctive tier … Canon §15"; L2755 "The mandate" … L2759 table row; L2761 "This replaces a 14.6% mandate"; L2763 "Why the commercial 25% mandate was withdrawn" … L2768–2769 the §25 quote; L2773 lead-in + L2775–2779 scope-word table; L2781–2782 "(L97) … (L101)"; L2785–2786 "By the Shirayuki ruling"; L2788 "NEW LENS" … L2805 end of that section; L2807–2813 "What stays FREE"; L2815 "Notes"; L2817–2819 the `04` lines; L2820–2827 post-war / perk lines; L2829 rule; L2831 `## 28. ✅ JANBOGO`. (L2830 is the last line before §28.) |
| ZK-024 | SKIPPED-MISMATCH | `Step_1_and_2.md` row "U Location canon"; `Phase_5.md` row "U Location canon + routes" | not changed ("10 files" stays) | Live: `TepenianUniverseTimeline/Worldspace/Locations/` holds **10 files** (4 `.md` + 6 `.png`; `find -type f \| wc -l` = 10, `-name '*.md'` = 4). `git ls-tree` at its last commit (67185e9, 2026-09-24, before the sheets were built) also gives 10 files / 4 `.md`. So the sheets' "10 files" is true as a file count; the ledger's "→ 4 `.md` files" is true only as an `.md` count. README L18 still names the city. If the developer wants the `.md` count, the row can read "10 files (4 `.md`, 6 `.png`)". |
| ZK-025 | APPLIED | `Step_3.md` picks row | `05_The_Input_Contract.md` `L709–713`→`L719 (item 6)` | Live L719 = "6. ⭐ **RATIFICATION IS BY ROOT, NOT BY BANNER — and SILENCE IS NOT CONSENT.**"; L710–713 = the Background-Lore exclusion (item 3a). Picks `Inspirational-Influences.md` L53–56 re-checked (heading L53, three picks). |
| ZK-026 | APPLIED | `Step_6.md`; `Step_9.md` | Step 6 section 1 columns: `Shape · Deficit address · Pass`→`Subnet · Shape · Deficit address · Pass`. Step 9 quick index: added "(5) discharge every deferral to 'the pass's close' — run the stale-anchor and span sweep over the pass's own files … (runbook Step 9 item 5, L3011–3015, `M-291`)" | Live table header `Cross_City_Culture_Differentiation_Table.md` L48 = `City \| Subnet \| Shape … \| Deficit address … \| Pass`. Runbook Step 9: item 5 at L3011–3015; wording copied from the live lines. |
| ZK-027 | untouched (DECIDE) | — | "428-line" stays | — |
| ZK-028 | APPLIED | `Phase_2.md` sequencing row; `Phase_4.md` `09` §3.5 row | `§C.9b L2088`→`L2090`, `§C.9d L2147`→`L2150`; `09` §3.5 `L124`→`L126` | Live runbook L2090 `## C.9b …`, L2150 `## C.9d …` (the Pre-Trip §G row already had these); `09` L126 "# ⭐⭐ 3.5 — THE FREEDOM MARGIN". |
| ZK-029 | APPLIED ⚑ | `Phase_5.md` | Highways `L226, L231`→`L227, L232`, conflict row `L226–228`→`L227–229`; RelDB entry `L301–307`→`L312–318`, Notes `L308`→`L319`, "southern terminus" `L306`→`L317`, other entry `L136`→`L147`; Ports `L335–337, L361`→`L358–360, L384`, shared infrastructure `L339–341`→`L362–364`, tier summary `L570`→**`L734`**, Q&A `L661`→**`L825`**, comparison "(L202–204)"→**"(L366–368)"**; Airports `L96`→`L99`; NatConn section `L449`→`L459`, others `L184, L395, L403, L435–437, L446`→`L190, L405, L413, L445–447, L456` | Each anchor re-read live (Highways L227 Route / L229 Endpoints / L232 bullet; RelDB L312 heading, L317 "Hwy 183 — southern terminus", L318 "Cape Adare (east, Hwy 183)", L319 Notes, L147 Cape Adare's "Mario Zucchelli (west)"; NatConn L459 heading). ⚑ **Two places where the ledger did not land, fixed by anchor:** (1) the ledger gives Ports "tier summary **L593**, Q&A **L684**" — those lines are about Nella Fjord / Stage 2; the anchors are the WIND tier-summary row (**L734**) and the "Does Zukelli share Janbogo's port?" row (**L825**), both already in the ledger's own Ports list for ZK-001. `git show 1914cdb9` shows the old cites L570 / L661 were exactly those two rows. (2) The sheet's "(L202–204)" for the following comparison with the rest of the corpus is the old position of the "MOST TIGHTLY COUPLED CITY PAIR" box; the ledger says it is "unchanged", but live L202–204 is the Hobart footprint table; the box is **L366–368**. Both are in cells of the rows ZK-029 covers. |
| ZK-030 | APPLIED ⚑ | `Phase_10.md` "No invented person names"; `Step_0.md` row 21 | `Phase_10`: runbook `L1980`→`L1982`, spine `L219`→`L220`. `Step_0` "location registries": runbook `L1970`→`L1972`, spine `L284–285`→`L285–286` | Live runbook L1982 = Phase 10 row "… the no-invented-person-names rule"; L1972 = Phase 0 row "P location registries"; spine L220 = "… and the no-invented-person-names rule"; spine L285 = "**P** `Official_Population_Census.md` + location registries", L286 its path. ⚑ the ledger gives "L285"; the old cite was a two-line span (item + path), so I wrote the equivalent span **L285–286** (the Pre-Trip §D Phase 0 row already says "L285–286"). |
| ZK-S01 … S06 | untouched (DECIDE / NOTE) | — | — | — |

### Shared fixes (ledger section A / brief §3)

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| SH-001 | APPLIED | Pre-Trip §G "No invented person names" | spine `L127`→`L220, L1114, L1140` | Live anchors: L220 "and the no-invented-person-names rule"; L1114 "NO INVENTED PERSON NAMES — role placeholders permanently"; L1140 "People as role-archetypes — binding rule: no invented proper names". Spine L127 is a table row, not the rule. The sheets cite spine L219 (not L127): `Phase_10.md` fixed under ZK-030. |
| SH-002 | APPLIED | Pre-Trip §G "Divergence operator" | runbook `L2178`→`L2180` | Live L2180 = "### ⭐ THE DIVERGENCE OPERATOR — the developer's own inputs"; L2178 is a table row. The row cites no other runbook line. |
| SH-003 | APPLIED | Pre-Trip §C Step 5 `T8` reads | `§5.3, lines 610–684`→`610–636` | `02_…` L610 "## 5.3 The both-are-true test"; L637 "# 6. Symbol binding". |
| SH-004 | APPLIED | Pre-Trip §C procedure items 4 and 5 | item 4: `lines 620–643 and 701–703`→`620–643 and 682–684`; item 5: `lines 650–703`→`667–684` | `TRIAL.md`: L620 "### ROUND 3", L643 closing fence of the prompt; L667 "AMENDED 2026-09-28 — THE WRITTEN CONTENT IS A MERGE, NOT A PICK" through L684 "record for the merge."; L682 "Round 3's prompt now carries a fifth section". |
| SH-005 | APPLIED | Pre-Trip §C Step 10 (governing line, `T8` reads, card note) | `3057–3172`→`3057–3152` (twice); "live lines 3045–3161 govern"→"live lines 3057–3152 govern" | Runbook L3057 `# Step 10 — THE READINESS CHECK`; L3153 `# Where everything lives`. |
| SH-006 | ALREADY-RIGHT (not present) | `Step_-1.md`, Pre-Trip | — | The Zukelli `Step_-1.md` "Specs `Status:` field" row cites only the spec (L4); neither it nor the Pre-Trip cites runbook L1821–1822. (Live L1854–1855 holds the "POST-WAR" sentence if a cite is ever wanted.) |
| SH-007 | HELD | — | — | Decision pending (per brief). No `06` / "line 65" row exists in the Zukelli sheets in any case (`Step_10.md` carries only the zero-hit statement). |
| SH-008 | APPLIED | all 11 sheets with a MUST-OPEN header | see §2 | Recounted by hand; header text and date changed in each. |
| SH-009 | HELD | — | — | Left as is ("428-line" in `Step_10.md`, "216 lines" in `Step_-1.md`). |
| SH-010 | APPLIED | Pre-Trip §D Phase 2 table (new row); `Phase_2.md` (two new rows) | added: the city's own section in `Upper_Earth_Immigration_Composition.md` (`### Zukelli` heading **L409**, section **L409–L417**) + the solar-UTC rule (heading **L21**, list "Recording it so it stops being reconstructed from examples" **L26–L33**, rule 1 at **L28**, refinement box **L35–L63**) | Live: L409 `### Zukelli (…)`; L413–417 the tier table; L419 the closing rule; L21 `### ⭐ HOW FACTOR 1 IS MEASURED — the ±3 solar-UTC window`; L35 box start … L63 end. Form copied from the Santa Luce / Relung Panen rows (form only). The phase's MUST OPEN list does not name this file, so the Pre-Trip row says "registered, not dispatched". I did not copy the "— Destroyed" in the heading or the section's text (cited by range only). `Phase_2.md` already carried the rule's numbered list (row "window rule", L28–33); the new rows add the heading/box addresses. Solar UTC check: 164°07′E = 164.117° ÷ 15 = 10.94 → +11 (Register row L67 also +11). |
| SH-011 | APPLIED | Pre-Trip §C Step 0 reads; `Step_0.md` row 19 | added "(2026-09-05 snapshot; the census is live — note L631)" beside the extent-row citation | Live L631 begins "**26,880,794 people needing …** *(Snapshot note, 2026-10-28: the table above records the 2026-09-05 populations …; the census is the live source.)*". Not added where no table row is cited: Pre-Trip §E (Extent L598 line) and `Step_0.md` row 20 (the L598–599 sentence); the Pre-Trip §D Phase 0 table does not cite the Extent file. |
| SH-012 | APPLIED | Pre-Trip, `Phase_5.md`, `Phase_4.md`, `Phase_7.md`, `Step_1_and_2.md` | via ZK-001, ZK-023, ZK-029 | See those rows. |
| SH-013 | APPLIED (Pre-Trip) · ALREADY-RIGHT (sheets) | Pre-Trip `16` lists; `Phase_7.md`, `Phase_4.md`, `Step_1_and_2.md` | `## 27. ✅ ZUKELLI — DETERMINED` **L2744** added to the §D Phase 1 `16` row and the §E row, marked "the city's own upper-case heading"; one clause that the determination supersedes Half B's MAND% / FREE% (shares are in the Phase 7 datasheet) | The sheets already quote §27's shares (5.9 / 52.7; Phase_7 rows 20–21), already say it replaces the 14.6% mandate, and `Step_1_and_2` / `Phase_4` point to `Phase_7`; nothing duplicated. |
| SH-014 | APPLIED | `Step_1_and_2.md` `16` row; `Phase_4.md` cross-check row; `Phase_7.md` rows "§27 — determined tiers", "Distinctive tier", "The mandate" | added "on the flat ABCC working value; counts re-run when per-city ABCC values are set (`16` L1287–1304)" | Live `16`: L1287 `### ⚠ CONSEQUENCE — the ten determinations so far need a baseline re-run`, block through L1304 ("rather than some being converted early"), L1305 blank (per brief §4a). Percentages of the distinctive tier are unaffected, so no clause beside them. |
| SH-015…017, SH-019 | HELD | — | — | Tier U sheets; orchestrator. |

---

## 2 · MUST-OPEN recount (SH-008), by hand

Rule applied: an address counts only if a row of the sheet cites it by full path / full file name. **Directly** = such a row. **Via Tier U** = no such row, but a row cites the Tier U extract sheet of that address. A directory address whose row cites a file inside the directory by full path is counted directly and marked ⚑ (the city's own file inside the registered directory). Named only in a "found, NOT extracted" box, or only by a cross-reference to another city datasheet, is **not covered**. The spine's own MUST OPEN block of each phase is the list (mirrored from runbook `§C.8c`); N was confirmed against it each time.

### Step_0.md — Phase 0 — **3 of 3** (was "3 of 3, 3 directly"; now 2 directly, 1 via Tier U)
| Address | Covering row |
|---|---|
| `…/Reference/Repo_Scope.md` | row "**U** `Repo_Scope.md` — corpus-wide boundary statement" (full path) — direct |
| `…/Timeline Eras/` | no row cites it; rows "Temporal frame", "Act structure", "The consolidating mechanism", "The governing form-of-words rule" cite `Second_Interwar_Period_Quick_Reference.md` (Tier U extract of `Timeline Eras/2 The Second Interwar Period/README.md`) — via Tier U |
| `Official_Population_Census.md` | rows "Census I", "Census II" (full path) — direct. ("+ location registries" names no file: row "**P** Location registries — UNRESOLVED".) |

### Step_1_and_2.md — Phase 1 — **6 of 6** (6 directly, as before)
| Address | Covering row |
|---|---|
| U `Worldspace/Locations/` | row "**U** Location canon — the whole folder" cites `…/Locations/README.md` ⚑ |
| `Cities/Specs/` (incl. `Access type:`) | rows "`Access type:`" and the others cite `Specs/Janbogo subnet/Zukelli.md` ⚑ |
| `Energy_Grid_Failure_Rationale.md` | row of that name (full path) |
| `Climate Data/READER/` | rows "Climate READER file", "Climate — monthly means" cite `READER/Zukelli.md` ⚑ |
| `Reference/Real-World/Stations/` | row "Stations list (background only)" cites `Stations/Antarctic_Stations_With_Airstrips.md` ⚑ |
| `16_Per_City_Three_Tier_Run.md` | row "`16` Half B — this city's own row" (full path) |

### Phase_2.md — Phase 2 — **3 of 3** (was "3 directly"; now 1 directly, 2 via Tier U)
| Address | Covering row |
|---|---|
| `No_National_Stereotypes.md` | no row cites it; row "GPS law" cites `No_National_Stereotypes_Quick_Reference.md` — via Tier U |
| `Falkland_Treaty/` | no row cites it; rows "Falkland Treaty — the human admission route / not nationality-based / staged allocation" cite `Falkland_Treaty_Quick_Reference.md` — via Tier U |
| `Official_Population_Census.md` | rows "Composition tier table", "Census I / II", "Annotation dating" (full path) — direct |

(The spine's fourth bullet, the sequencing ruling, has no address of its own; row "The sequencing ruling" cites the runbook §C.9b / §C.9d.)

### Phase_3.md — Phase 3 — **3 of 4 applicable** (was "4 of 4"; the spine lists 5, one is "where applicable: Davis only")
| Address | Covering row |
|---|---|
| Climate `READER/` | **not covered** — row "Climate (cross-ref)" points to `Datasheets/Step_1_and_2.md` (a city datasheet, not a Tier U sheet) and names no READER path ⚑ |
| `Cities/Specs/` | rows "The bay, stated directly", "The polynya", "Built form", "Developer vision" cite `Specs/Janbogo subnet/Zukelli.md` ⚑ |
| `City_Concept-Art/` | row "Concept-art directory status" (full path of the city's folder) |
| `Davis_Geosciences_Research/` | not applicable (named in the header only) |
| `*_Physical_Infrastructure_Attributes.md` / `City_Megasheets/` | row "Megasheet Physical Infrastructure file" (full path; existence only, withheld) |

### Phase_4.md — Phase 4 — **7 of 7** (7 directly, as before)
Robot Physiology and Robot Cold Physiology — row "Robot Physiology files" (both full paths); `16` — rows "Workforce cross-check", "`16` Half B (cross-ref)"; `09` — rows "`09` §2", "Population figures vs the census", "`09` §3.5"; `11_Caloric_…` — its row; `National_Medical_and_Care_Institutes.md` — its row; `National_Economy_and_Currency.md` — its row. (`City_Logistics.md` is REMOVED from this phase by the spine.)

### Phase_5.md — Phase 5 — **5 of 6** (was "6 of 6")
| Address | Covering row |
|---|---|
| U `Worldspace/Locations/` | row "**U** Location canon + routes" cites `…/Locations/README.md` ⚑ |
| `Highways.md` | rows "Highway routing", "Conflict" (full path) |
| `Airports.md` · `Ports.md` · `Geothermal_Heating.md` (one bullet, three files) | rows "Airport", "Port — shared", "Shared infrastructure", "Geothermal heat" (all three by full path) |
| `City_Cross_Subnet_Relationships.md` | its row (full path) |
| `City_Relationship_Database.md` | rows "Conflict", "own entry", "Notes", "Other entries" (full path) |
| `City_National_Connections.md` | **not covered** — named only in the sheet's warning box (L3) and the "FLAGGED — found, NOT extracted" box (L31); no row transcribes or cites anything from it ⚑ |

### Phase_6.md — Phase 6 — **5 of 5** (5 directly, as before)
`Factions/Robot_Religions/` — row "Robot religions — full sweep" cites `Robot_Religions/Cymatics_reverence/Cymatics_reverence.md` ⚑ (the Tier U roster sheet is also cited, row 12); `National_Holidays.md` — its row; `Ice-Cold_Buddhism_Research/` — its row; `The_Meme_Machine_Extraction.md` and `The_True_Believer_Extraction.md` — one row, both full paths. The mortuary question is RESERVED and has no address.

### Phase_7.md — Phase 7 — **11 of 13** (was "13 of 13, 11 directly + 2 via Tier U"; now 10 directly, 1 via Tier U)
| Address | Covering row |
|---|---|
| `Division_of_Industry/` | no row cites the folder; the header callout cites `Division_of_Industry_Reliability_Quick_Reference.md` (the DoI carve-out extract) — via Tier U |
| `16_Per_City_Three_Tier_Run.md` | rows "`16` §27 …", "Superseded figures", "Distinctive tier", "The mandate", "Why commercial…", "What stays FREE", "`04` status", "Symbol assignment" — direct |
| `Division_of_Industry_Sweep_2026-08-31.md` | rows "Sweep §4.4", "Sweep §5" — direct |
| `01_Burden_Scoring_Model.md`, `08_Volume_Based_Requirement_Reference.md` | one row, both full paths — direct |
| `National_Medical_and_Care_Institutes.md` | **not covered** — row "Medical institutes" says "Zero hits — cross-ref" and cites only `Datasheets/Phase_4.md`; the file name appears in no row of this sheet ⚑ |
| `Theoretical-Calculations/` | row "Theoretical-Calculations — supply line" cites `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md` ⚑ |
| `Industry_Staffing_and_Productivity/`, `jobs_professions_and_fields/` | row "Industry Staffing · SOC" (both full paths) — direct |
| `National_Economy_and_Currency.md` | row "National economy" (full path in the citation cell) — direct |
| `City_Logistics.md` | its row (full path) — direct |
| `Worldspace/Factions/` | **not covered** — named only in the "FLAGGED — found, NOT extracted" table (a file in it at row 1, the folder at row 2) ⚑ |
| `Megacorps/` | its row (full path) — direct |

### Phase_8.md — Phase 8 — **2 of 2** (2 directly, as before)
`Robot_Biology_and_Culture/` — row of that name (full path); `Weapons_and_Tools_Philosophy.md` — row "…· gear catalog" (full path; "gear catalogs, slang" in the spine bullet name no address).

### Phase_9.md — Phase 9 — **4 of 4** (3 directly, 1 via Tier U, as before)
`Laws_of_Robotics.md` — row "Laws of Robotics (read firsthand)"; `Robot_Universals/` — its row; `Doll_Representation_Categories.md` — its row; human-robot baseline (`Robot_Physiology_and_Cultural_Practices.md`) — no row cites it; row "Human-robot relations baseline (Tier U)" cites `Robot_Physiology_Quick_Reference.md` — via Tier U.

### Phase_10.md — Phase 10 — **3 of 3** (3 directly, as before)
`Worldspace/Characters/` (U) — rows "Characters canon — a confirmed resident / an undecided candidate origin / other mentions" (the folder's full path in the third); `Enneagram_Character_Index.md` — its row; `Zodiac_Signs_Full_Attributes.md` — row "Zodiac Lens — the full-attributes file". ("NO INVENTED PERSON NAMES" is a rule with no address.)

⚑ **Judgment calls in the recount:** (a) a directory address covered by a row that cites the city's file inside it (Step_1_and_2 ×4, Phase_3 Specs, Phase_5 U Locations, Phase_6 Robot_Religions, Phase_7 Theoretical-Calculations) is counted directly; (b) a row that only cross-references another city datasheet (Phase_3 climate, Phase_7 medical) is not counted, because that other sheet is not a Tier U sheet; (c) addresses named only in "found, NOT extracted" boxes (Phase_5 National Connections, Phase_7 Factions) are not counted; (d) the Tier U roster/extract sheet is accepted as "via Tier U" for Timeline Eras, No National Stereotypes, Falkland, the DoI folder and the human-robot baseline.

---

## 3 · New findings (not in the ledger; nothing below was fixed unless it sits inside an entry I applied)

1. **Ledger/audit arithmetic slip (applied with the hand-computed value).** ZK-020 / D-01 give robot retention **78.04%** and spread **7.41 pp**. 501,644 ÷ 642,845 = 0.7803498… = **78.03%** (just under 78.035), so the spread is **7.40 pp**. The sheets now say 78.03% / 7.40 pp. The audit file (`Zukelli_Audit.md` L46, D-01) and ledger ZK-020 should be corrected to match; if anyone copies 78.04 into the spec or the census later it will not match the rows.
2. **Ledger Ports numbers that do not land (ZK-029):** "tier summary L593, Q&A L684" — the live anchors are L734 and L825 (applied). The ledger's "L202–204 unchanged" for the Ports comparison box is wrong; it is L366–368 (applied, inside the same row).
3. **ZK-024 not applied** (see table): the "10 files" is correct as a total (4 `.md` + 6 `.png`).
4. **Rows missing for must-open addresses (gaps for the developer, not filled):** Phase 3 — climate folder `…/Reference/Real-World/Climate Data/READER/`; Phase 5 — `City_National_Connections.md`; Phase 7 — `National_Medical_and_Care_Institutes.md` and `Worldspace/Factions/`.
5. **Meta rows that restate a coverage count and now disagree with the recount (left as they are):** `Step_0.md` L7 ("2 of 3 resolved — Repo_Scope ✅ · Timeline eras ✅ · Census ✅"; it lists three ticks under "2 of 3"); `Phase_2.md` L6 ("4 of 4", counts the sequencing ruling); `Phase_3.md` L6 ("5 of 5"); `Phase_5.md` L7 ("6 of 6 … national connections (flagged)"); `Phase_6.md` L5 ("4 of 4 … the mortuary question"); `Phase_7.md` L14 ("13 of 13"); `Phase_10.md` L6 ("4 of 4 … Zodiac Lens (full-attributes file AND substrate folder)"). They agree with the recount in `Step_1_and_2.md` L6 (6 of 6), `Phase_4.md` L10 (7 of 7), `Phase_8.md` L6 (2 of 2), `Phase_9.md` L5 (4 of 4).
6. **Stale spine ranges in those same older meta rows (not in the ledger):** in the convention the sheets use (first bullet line to the last bullet's first line, found by a read-only awk scan of the `📂 MUST OPEN` blocks), the live ranges are Phase 0 L281–285, Phase 1 L329–339, Phase 2 L408–414 ✓, Phase 3 L479–487, Phase 4 L541–555, Phase 5 L623–633 ✓, Phase 6 L760–769, Phase 7 L849–873 ✓, Phase 8 L962–964, Phase 9 L1033–1039, Phase 10 L1108–1114. The sheets say Phase 0 L280–285, Phase 1 L327–337, Phase 3 L480–488, Phase 4 L542–556, Phase 6 L759–765, Phase 8 L963–965, Phase 9 L1034–1040, Phase 10 L1109–1115. (Off by one to two lines, Phase 6 by more; ✓ = agrees.)
7. **`Phase_5.md` L32, FLAGGED box: "Its own Method (L19)"** — in `City_National_Connections.md` the `**Method:**` paragraph is now at **L25** (L19 is inside the "Relationship to …" paragraph). Same sentence block I edited for the section lines; not in the ledger.
8. **`Phase_7.md` rows quoting §27 counts (391,579 / 55,328 / 497,952 / 553,280):** the counts are on the pre-`DR-68` workforce (944,859); `Phase_4`'s row now says so, `Phase_7` carries only the SH-014 clause. (`16` §24–§28 counts are the pre-`DR-68` ones; only the shares are current.)
9. **`Step_9.md` quick index** says "(2) add this location's differentiation **column**"; runbook Step 9 item 2 (L2989–2999) says the city table holds one ROW per city. That is the SH-017 "row / column" question (DECIDE); not touched. The Tier U Step 9 sheet it points to still lists four actions (SH-016, DECIDE), so the quick index now has five items and the pointed-to full text four.
10. **Pre-Trip §I (the 2026-10-21 build log: "TOTAL=183 RESOLVE=140", "82 claims · 82 OK · 0 FAIL", "60 numbers moved") is a dated record and was not recomputed;** the sweep changed ~25 of the cited numbers and added one address row, so the block no longer describes the live sheet.
11. **Pre-Trip §A "No rename flagged"** still sits beside the 2026-10-13 rename ruling that the datasheets carry (ZK-002, DECIDE); unchanged.

---

## 4 · Files edited (15; all under `PASSES/Janbogo_Subnet/Zukelli/`)

- `…/Zukelli/00.0_Pre-Trip_Inspection.md`
- `…/Zukelli/Datasheets/Step_0.md`
- `…/Zukelli/Datasheets/Step_1_and_2.md`
- `…/Zukelli/Datasheets/Step_3.md`
- `…/Zukelli/Datasheets/Step_6.md`
- `…/Zukelli/Datasheets/Step_9.md`
- `…/Zukelli/Datasheets/Phase_2.md`
- `…/Zukelli/Datasheets/Phase_3.md`
- `…/Zukelli/Datasheets/Phase_4.md`
- `…/Zukelli/Datasheets/Phase_5.md`
- `…/Zukelli/Datasheets/Phase_6.md`
- `…/Zukelli/Datasheets/Phase_7.md`
- `…/Zukelli/Datasheets/Phase_8.md`
- `…/Zukelli/Datasheets/Phase_9.md`
- `…/Zukelli/Datasheets/Phase_10.md`

(Full path prefix: `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Janbogo_Subnet/Zukelli/`.) Not edited: `Step_-1.md`, `Step_5.md`, `Step_7.md`, `Step_8.md`, `Step_10.md`, `README.md`, `00.2_Position_Coverage_Ledger.md`, every source file. No commit; no generator run; no `--force`; no name sweep. This report is the only new file.
