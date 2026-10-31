# Mirny — manual input audit (2026-10-29) · RUN CITY: sheets + drift

Method: `README.md` in this folder. Read by hand: the spec in full (230 lines), the whole Pre-Trip (569 lines), all 19 datasheets, the pass README, the DR-56 amendment register header; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `MY-…`). Pass folder: `City_Development_Passes/Mirny_Subnet/Mirny/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`.

**What kind of city this is.** Mirny's ULM pass has been run (21 pass files, T8 rounds, Step 10) and is now under the DR-56 amendment re-derivation (Phases 6 and 7 verified 2026-10-29; Phases 8–10 and Steps 5–8 still to come). So this audit does two things: (a) the usual access and accuracy check of the Pre-Trip and the 19 sheets, and (b) a drift check of what the pass was built on. **Pass files are never edited; drift is logged as `AMEND` notes.** The pass files were not re-read; drift was found by comparison (old values counted by search, live sources opened).

**Verdict.** **Nothing blocks.** Mirny's Pre-Trip is the older, address-only form (written 2026-09-28, refreshed 2026-10-21 for runbook lines), so it has no per-file "names Mirny at" lists and none of the line-list rot found in Casey and Kunlun. Its addresses all resolve. What is wrong: **(1)** every census-derived figure in the sheets (and in 15–19 of the 21 pass files) is from before the 2026-10-28 census change; **(2)** about a dozen citation slips in the sheets (Census II row, `16` row, `09` figures, `16` §20 shifted +5, Ports/RelDB/NatConn lines, a wrong cross-reference, wrong picks lines); **(3)** the spec's temperature-range line contradicts its own table, and three monthly-table notes still carry the retracted symmetric-light wording; **(4)** the airport ruling of 2026-10-29 (`DR-82`) changes Mirny's Phase 5 inputs — the ruling itself lists the Mirny amendment note as still to do; **(5)** the sheets and Pre-Trip speak as though the pass has not started, and the README claims T8 records are archived when only the earliest five are.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Mirny subnet/Mirny.md`, 230 lines (sheet says 230 ✓); the cited lines L1, L3–L9, L18–22, L26–47, L53–57, L68–72, L82, L85–99, L132–134, L150, L152, L162, L168, L174, L176, L191, L227, L230 all land on what the sheets say | ✅ |
| Census Section A heading/entry **L370**, Census I row **L488**, Census II row **L609** | ✅ the rows exist; the values the sheets quote are old (**D-01**) |
| `READER/Mirny.md` L14: twelve monthly means equal the spec's Mean column exactly; annual −11.2 | ✅ |
| `09` Mirny row **L71**; `16` §20 (heading **L2110**); `Highways.md` L199–201; `Airports.md` L12; Sweep rows L166 (Constr = Y), L23–26, L220; Theoretical-Calculations L992–994; `City_Logistics.md` L1–3 (Concordia-scoped) | ✅ (several cited ranges are shifted, **D-07, D-13**) |
| Factions: four files name Mirny (Hometown-based, Cross_City_Cultural_Patterns, PostWar_Refugee, Second_Interwar); the seven-city grouping heading is at `Second_Interwar` L31 | ✅ |
| `National_Holidays.md` L109–115 ("Two Days a Year (Mirny)") | ✅ (the sheet already flags its "a few days near each solstice" as the retracted light model) |
| Robot_Religions and Ice-Cold Buddhism folders: zero hits for Mirny; `The_True_Believer_Extraction.md` and `The_Meme_Machine_Extraction.md`: zero hits; Weapons_and_Tools_Philosophy (73 lines): zero hits; Robot_Universals: zero hits; Enneagram index (35 lines): zero hits; Doll Representation Categories (35 lines) | ✅ re-run |
| Zero-hit claims: Stations file (99 lines), Energy grid, `11` | ✅ re-run; NMCI has **one** raw hit now — Sinheung L76, the "Mirny subnet" qualifier (**D-16**) |
| COMNAP catalogue: Mirny named on pages **8** and **65** (86 pages) | ✅ |
| Megasheet Physical Infrastructure file (15,462 bytes) | ✅ |
| Every backticked address in the Pre-Trip that I tested (spec, Local Culture, Local Robot Culture, Enneagram file, Concept-Art folder, the four `Tools/` scripts, both Zodiac files, DoI README and `10_Validation`, Run-Modes, the Pre-Trip recipe, Robot Physiology, Robot Cold Physiology, Energy grid, READER) | ✅ all exist |
| Runbook anchors L309, L378, L430, L2431, L2458–2459, L2512–2513, L2571, L2696 and the `DR-8a` row at rulings log L399; `TODO.md` L813–816 ("Mirny Rename"); `05` L490 | ✅ |
| Pass README spec, local-culture, vision-notes, research-log and picks pointers | ✅ all resolve (`Mirny_Research_Log.md` exists) |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | NOTE | The Pre-Trip is the pass-time record of a pass that has since run: §B ("Mirny is part of the active run"), §I (72 addresses OK, 2026-09-28), §K (ledger "all cells blank"), §7 self-test, and every "check first" pointer speak of an unrun pass. It is not wrong as a record, but it is not what a reader of the current state needs. | Pre-Trip | One-line banner "pass run; this is the pre-run record" (DECIDE) |
| **A-02** | WRONG | §G "The divergence operator — `00_RUNBOOK.md` **L2227**": L2227 is the "WHAT SURVIVES" lesson box; the operator itself (the six inputs) is at **L2180**. §N's own check only confirmed that L2227 holds 'WHAT SURVIVES'. | runbook L2180, L2227 | Cite L2180 for the operator (keep L2227 as the lesson) |
| **A-03** | WRONG | §J `DR-8a` row cites rulings log "L399, **L428**": L399 is the `DR-8a` row; L428 is the Mirny founding ruling (`DR-9`, "The founding population is all three"). The "SETTLED 2026-09-16" line is **L1186**. | rulings log L399, L428, L1186 | Replace L428 by L1186 |
| **A-04** | STALE | §C Step 6: "(incl. the **nine-section** inventory)": the table has **ten** sections since 2026-10-21 (the Step_6 sheet says ten). | Pre-Trip, Step_6 sheet | "ten-section" |
| **A-05** | GAP | **Inputs created or changed after the pass was run, in neither the Pre-Trip nor the sheets:** `Airports.md` L12 (with the `DR-82` note), L64, L99; `Ports.md` L189, L200, L224 (new §3e and ocean research); `Upper_Earth_Immigration_Composition.md` (Mirny's tier lists, L563–565 in that file; XS-13); `Founding_Register.md` rows **L57**, **L88** (`DR-46`), **L94**; `Research_Logs/Casey_Mirny_Airport_Comparison/Geology/Operations/BRIEFS_2026-10-29` (4 files), `Mirny_Inspiration_Place_Research_R1.md` and `_R2.md`, `Russia_Split_Proportions_RS2_Mirny_Subnet_2026-10-29.md`; the extent file (**A-06**); rulings `DR-76`, `DR-77`, `DR-79`, `DR-82`. | greps above | Register with tiers, so the amendment pieces and any later re-run open the same set |
| **A-06** | GAP | **No extent address anywhere** (neither the Pre-Trip nor any sheet names `Extent_and_Density_Per_City.md`). Mirny's row is **L611** (Mirny · 1,351,430 · **135 km² @10,000/km² · 193 km² @7,000** · coastal ice — a dated 2026-09-05 snapshot, note at L631); lines L578, L587 also name the city. At the live Census I 1,375,348 the same arithmetic gives **137.5 / 196.5 km²**. | extent L611 | Add the row (labelled snapshot) to `Step_0` and `Step_1_and_2` and an address to the Pre-Trip |
| **A-07** | NOTE | README: "this pass's T8 reader files (`.t8_*`) and T8 round records (`*b_T8_Rounds_*`) are at `Archive/ULM_Records/…/Mirny/`, same file names." Only **5** files are there (the Step −1 to Step 3 rounds). The folder still holds **146** hidden `.t8_*` files, **17** `*b_T8_Rounds*` files, two assembler scripts (`assemble_merge5.py`, `assemble_qa7.py`) and `_safeguard_probe`; a citation to any of them does not resolve at the archive. (The folder is under active amendment, so a move now would be unwise.) | `ls` | Reword the README sentence; DECIDE when to archive |
| **A-08** | NOTE | Megasheet folder "7 files" (Pre-Trip §C, §F): 6 files and 1 subfolder. | `ls` | Reword (as SL-008) |
| **A-09** | NOTE | `Phase_5.md` names other cities as relation (Zhongshan, Davis, Casey, Concordia, Ariun Nuur, Kunlun). Relation is legal under the one-location law; later sheets (Kunlun's) instead state "no other city is named in this file". | `Phase_5.md` | None, unless the convention is unified |
| **A-10** | NOTE | Shared items already logged (SH-001 … SH-007): runbook Step −1 rule L1821–1822 → L1854–1855 (Step_-1 sheet); `06` provenance skip-line defect (XS-7) — **not** applicable to the Step_10 sheet here, which cites no skip line. | | shared |

### 1c. Required inputs
Mirny's pass has run, so the question is whether the inputs it used still exist: **all of them do** (existence check above). What the pass could not have used is listed in **A-05**.

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: the 14 per-nation shares sum to **100.00%**; all four count columns sum **exactly** to the stated totals — Census I robots **697,307**, Census I humans **678,041**, Census II robots **516,890**, Census II humans **515,452** — and the combined totals (**1,375,348**; **1,032,342**) are the sums of those; tier lists (L18–22) equal the per-nation table (1 Primary, 6 Significant, 7 Notable); monthly means average **−11.19 °C** (stated −11.2); monthly precipitation sums to **527.1 mm** (stated); retention 200 ÷ 527 = 37.9% (stated ~38%), lost 327 ✓; midnight sun Dec 8 → Jan 5 = **29 days** ✓; record high +8.7 (Dec) and low −36.5 (Aug) match the table; the spec was rescaled correctly for `DR-68` (unlike Kunlun's).

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **L69 contradicts the table below it.** "coldest months (July/August) avg **−22 °C**; warmest month (January) avg +1 °C": the coldest monthly **mean** is −16.4 (Aug), the coldest average **low** −20.2 (Aug) / −19.6 (Jul); −22 matches neither. The +1 matches January's average **high** (+1.1), so the line mixes measures. | spec L69, L107–118 |
| **S-02** | STALE | **Monthly-table Notes still carry the retracted symmetric-light wording:** June row "polar night in minimal form" (L112) and December row "midnight sun in minimal form" (L118), against the corrected L85–86 (**no polar night; ~29 days of midnight sun**). L100–101, L132, L138 and L164 also use the grazing model (the Phase_3 sheet already flags L132 as demoted at Step −1; the table notes are not flagged). | spec L85–86, L112, L118 |
| **S-03** | NOTE | L82 states a peer rank ("20 of the 37 Tepenian cities are colder than this one"; the corpus has 38 cities). The sheet correctly does not carry it. | spec L82 |
| **S-04** | NOTE | L184 (relay hardware) lists five cities (Zhongshan, Casey, Davis, Ariun Nuur, Kunlun) — a dated partial list; the subnet now has nine members (also Shirayuki, Sinheung, Relung Panen). The sheet already says so. | spec L184 |
| **S-05** | NOTE (pending) | The tier lists name "Russia" (L21, L36: Significant, 7.22%, 50,379 robots / 48,987 humans). `Russia_Split_Proportions_RS2` (2026-10-29) works out how that share would divide among the successor states; **nothing is ruled**, so nothing changes yet. | spec L21, L36; RS2 §5 |
| **S-06** | NOTE | L229 states Sinheung's Russia share as 6.85% — matches Sinheung's spec (L92). | spec L229 |
| **S-07** | NOTE | The timeline repo's `Worldspace/Locations/README.md` L20 still lists "Vostok" (rename sweep held). Flag only. | README L20 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ spec location, length (230), L1/L3–L9; ❌ **D-01** (census), **D-10** (runbook line) |
| `Step_0` | ✅ temporal frame rows; ❌ **D-01**, **D-02**, no extent row (**A-06**) |
| `Step_1_and_2` | ✅ climate rows (monthly means, records, winds, precipitation, polar night, Antarctic Circle), Stations zero-hit, COMNAP pages, Register text, L176; ❌ **D-05**, **D-12**, no extent row |
| `Step_3` | ✅ the four picks match the live text; ❌ **D-09** (lines) |
| `Step_5` | ✅ deliberate stub; the three files exist |
| `Step_6` | ✅ ten sections; ❌ **D-17** (no Subnet column) |
| `Step_7`, `Step_8` | ✅ identical to the corpus-wide text (the Kunlun-only notes are absent, correctly) |
| `Step_9` | ❌ **D-17** (item 5 missing) |
| `Step_10` | ❌ **D-11** |
| `Phase_2` | ✅ tiers, annotation, Falkland rows, GPS rows, Register statement; ❌ **D-01, D-02, D-12** |
| `Phase_3` | ✅ L53–57, L85–86, L132–134, L162, L168; megasheet file size; ❌ **D-19** (duplicate row) |
| `Phase_4` | ❌ **D-04**, **D-16** |
| `Phase_5` | ✅ Highways L199–201, Airports L12; ❌ **D-13**, **D-14** |
| `Phase_6` | ✅ National Holidays, zero-hit rows (counts: True Believer now 377, Meme Machine 292 by `wc -l`, XS-9) |
| `Phase_7` | ✅ Sweep L166, L23–26, L220; Theoretical L992–994; `10_Validation` L263; Factions seven-city heading L31; ❌ **D-06, D-07, D-08** |
| `Phase_8` | ✅ spec L168, L191, L227; Weapons file (73 lines) |
| `Phase_9` | ❌ **D-03** |
| `Phase_10` | ✅ Enneagram index (35 lines), spec L191–192; ❌ **D-15** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Step_-1`, `Step_0`, `Phase_2` · Census I and II | Quote the pre-`DR-68` figures and say "exact match". **Live:** Census I **678,041 H / 697,307 R / 1,375,348** (row L488, same line); Census II **515,452 H / 516,890 R / 1,032,342**, row **L609** (sheets say **L603**). | Replace; the spec and census now agree at the new values |
| **D-02** | STALE | `Step_0`, `Phase_2` · Retention | 75.22 / 76.19 / 74.27 / spread 1.92 pp. By hand: 1,032,342 ÷ 1,375,348 = **75.06%**; 515,452 ÷ 678,041 = **76.02%**; 516,890 ÷ 697,307 = **74.13%**; spread **1.89 pp** toward humans. | Replace |
| **D-03** | STALE | `Phase_9` · robot share | "50.73% (685,529 of 1,351,430)". By hand: 697,307 ÷ 1,375,348 = **50.70%**. | Replace |
| **D-04** | STALE | `Phase_4` · `09` row and the `16` cross-check | `09` L71 (right line) now reads Humans **678,041** · Residents **1,375,348** · Required workforce **368,677** (sheet 362,213) · Workforce **1,036,328** (sheet 1,018,480) · % of workforce required **35.6%** (unchanged). The cross-check cites `16` **L275**; Mirny's row is **L276**, workforce 1,036,328, base 41.1% · MAND 11.8% · FREE 47.1% unchanged. | Replace |
| **D-05** | STALE | `Step_1_and_2` · `16` Half B row | **L275 → L276**; workforce **1,018,480 → 1,036,328** (697,307 + 0.5 × 678,041 = 1,036,327.5). | Replace |
| **D-06** | GAP | `Step_1_and_2` vs `Phase_7` | The two sheets give different mandated/free splits without a word of explanation: Half B (MAND **11.8%** · FREE **47.1%**) and §20 (Mandated **23.6%** · FREE **35.3%**). The source explains it itself: *"Half B mandated only the Arcanet 20%"*; §20 added the industrial 20% (`16` L2131). | Add the sentence and the cite |
| **D-07** | STALE | `Phase_7` · `16` §20 rows | Citations are the old numbering: §20 table **L2105–2113 → L2110–2118**; mandate quote **→ L2134–2136** (section L2133–2141); Chain 1 row **L2139 → L2144**; Chain 2 row **→ L2145** (framing L2147–2149); What stays FREE **→ L2157–2161** (all +5). The §20 worker counts (418,565 / 239,966 / 359,949; sum 1,018,480) are the pre-`DR-68` set (`16` L1 says per-city determinations were not recomputed). | Re-read live; label as pre-`DR-68` |
| **D-08** | WRONG | `Phase_7` · Sweep matrix row | "legend already recorded at `Phase_3.md`/cross-city convention": `Phase_3.md` holds no legend. The legend is Sweep **L139**. | Cite Sweep L139 |
| **D-09** | STALE | `Step_3` · picks row | "`Inspirational-Influences.md` L75–78": heading **L75**, the four picks **L76–79**. | L75–79 |
| **D-10** | STALE | `Step_-1` · `Status:` row | "`00_RUNBOOK.md` L1821–1822": the rule is at **L1854–1855** (SH-006). | Re-point |
| **D-11** | STALE | `Step_10` | "`06` (406 lines)… 2 raw hits at L107 and L314": the file is **431 lines**; only **L107** matches now (L314 no longer does). The conclusion (zero genuine hits) stands. | Re-run and replace |
| **D-12** | STALE | `Step_1_and_2`, `Phase_2` · tier rows | "Census `L370–375`": heading L370, tier table **L372–376** — the Notable row is **L376**. | L370–376 |
| **D-13** | STALE | `Phase_5` | Ports **L363 → L386**, **L714 → L737**, **L770 → L793** (L129 same) — +23; RelDB entry **L323–330 → L334–341**, routing **L328–329 → L339–340** — +11; NatConn Sinheung bullet **L264–266 → L271–273**, civic-institutions bullets **L272–275 →** Dual-Kitchen Halls **L283–285** and windbreak ring **L286–288**; the flagged "Australian-heritage network" bullets **→ L274–276** (Casey) and **L277–278** (Davis). | Re-read live |
| **D-14** | GAP | `Phase_5` · Airport and Port rows | New Mirny content: `Airports.md` L12 now carries the **`DR-82`** note (receives the onward flights of winter arrivals processed at the Winter Intake Airport; whether this airport or a new airfield is not ruled); L64, L99. `Ports.md` L189, L200 ("canon node, subnet hub · tier not established · Davis Sea coast"), L224. The sheet's "tier not established" is still right. | Add |
| **D-15** | STALE | `Phase_10` · Characters row | "Two files matched": now **four** (Calethina README and `Formative_History.md`; Ji-Eun Kim README and `Timeline.md`). Same two characters; the Calethina hits are "Kunlun (Mirny subnet)" and "Kunlun/Mirny" — still the subnet-qualifier shape. The two Ji-Eun Kim hits were not re-read in context. | Update count; re-read |
| **D-16** | NOTE | `Phase_4`, `Phase_7` · NMCI "zero hits" | One raw hit now (NMCI L76, Sinheung "(Mirny subnet…)"); no hit for the city. | Phrase as "no hit for the city; one subnet-qualifier hit" |
| **D-17** | GAP | `Step_6`, `Step_9` | `Step_6` section-1 columns lack **Subnet**; `Step_9` lacks item 5 (as CASEY-048/049). | As Casey |
| **D-18** | NOTE | `Step_1_and_2` · founding row | Cites `Founding_Register.md` with no line; rows are **L57** (Mirny), **L88** (`DR-46`), **L94**. | Add lines |
| **D-19** | NOTE | `Phase_3` rows 11 and 21 | Duplicate "Concept-art directory status" row. | Keep one |
| **D-20** | NOTE | all sheets | Speak as though the pass has not started ("Mirny's own ULM pass has NOT started", "none of which exists yet for Mirny"). | DECIDE: banner or leave |

### 2d. Drift — what the pass was built on has changed (AMEND notes, pass files untouched)
| ID | What changed | Where the pass is affected | Note to file beside the pass |
|---|---|---|---|
| **DF-1** | `DR-68` census (2026-10-28): Mirny **+12,140 humans / +11,778 robots** | Old values counted by search in the pass: Census I humans **665,901** in 19 of 21 files, robots **685,529** in 16, combined **1,351,430** in 15 (18 times in `07_QA_Gates.md`), Census II figures in 1–3 files, workforce **1,018,480** in 4, robot share **50.73%** in 16, retention **75.22%** in 3. Derived values now: robot share **50.70%**; retention **75.06 / 76.02 / 74.13**; workforce **1,036,328** (`09` required 368,677, 35.6%); Gate 11 area **137.5 km² @10,000/km², 196.5 @7,000** (extent snapshot said 135 / 193). Shares unchanged; every tier list and axis stands. | AMEND: "figures in this pass are pre-`DR-68`; shares unchanged" |
| **DF-2** | `DR-82` (2026-10-29): the Australian-side winter intake; processed arrivals fly on to **Mirny** | `04_Phase_05` arrival types ("by air" row, L247), the air row, `R-57` ("when Mirny Airport was built" — deferred on purpose, `DR-51`), `PA-25` ("Mirny Airport's in-frame existence and date are not assumed"). The ruling itself says *"Still to do: an amendment note for Mirny's finished pass (its Phase 5 arrival types, air row and R-57), never an edit."* `DR-51`'s deferral is **not** closed. | AMEND: already requested by the ruling; also Phase 2 (arrival modes) if it reads the air route |
| **DF-3** | Ocean/Ports research and `Ports.md` §3e (2026-10-29) | Pass `PRT` citations (L129, L363, L714, L770) now shifted +23; new Mirny facts (L200 distance and "Davis Sea coast", L224). The pass's "tier not established" is unchanged. | AMEND: line shift only; no finding changes |
| **DF-4** | `Russia_Split_Proportions_RS2` (informational, nothing ruled) | If the developer later rules the Russia split, the label "Russia" in Mirny's tier lists (spec L21, L36) and the pass's Phase 2 will need re-labelling. | NOTE: hold; no action now |
| **DF-5** | `DR-56`/`DR-57`/`DR-76`/`DR-77`/`DR-79` (wind-reading culture) | Already tracked in `DR-56_Amendment_Register_2026-10-13.md` (rewritten 2026-10-29): Phases 6 and 7 verified; Phases 8–10 and Steps 5–8 still to come. | NOTE: not duplicated here |
| **DF-6** | Spec edits since the pass | L152 founding rewritten 2026-10-13 (covered by the register). No line has shifted since Step −1's admitted ranges (L191, L227, L162, L168 land as the contract says). | none |

### 2e. DECIDE items (collected)
1. **A-01 / D-20** One-line "pass run; pre-run record" banner on the Pre-Trip and sheets, or leave as records?
2. **A-05** Tiers for the new research files and rulings (the amendment pieces will need them).
3. **A-07** When to move the later T8 records to the archive (not while the amendments run).
4. **S-01** Fix L69 to a single measure (mean or average low) and **S-02** the three table notes (the rest of the grazing wording is already tracked by the amendment work).
5. **DF-2** File the `DR-82` amendment note now, or in the next 05:00–14:59 window as the ruling says.
