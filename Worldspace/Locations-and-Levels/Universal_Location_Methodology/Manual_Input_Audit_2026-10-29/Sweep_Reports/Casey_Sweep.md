# Casey — sweep report (2026-10-30)

**City:** Casey (ledger section B1; pass folder `PASSES/Mirny_Subnet/Casey`). **Who:** sub-agent (Sonnet 5.5), one sweep run. **No commit made.**

**Read:** `SWEEP_BRIEF.md`; `FIX_LEDGER.md` section A and B1; `Casey_Audit.md`; the whole Casey Pre-Trip, README, `00.2` ledger and all 19 datasheets; and, live, every source line named below (`16`, `09`, `11`, Airports, Ports, Highways, RelDB, NatConn, Cross-Subnet, census, spec, composition file, extent table, Founding Register, NMCI, READER/Casey.md, runbook, spine, trial recipe, `02`, `06`, Robot_Religions folder, Pink Lucy files, Doll/Laws files, Tier U sheet headers, `check_must_open_coverage.py` for the counting unit).

**Counts:** APPLIED 49 (38 Casey entries + 11 shared fixes) · PARTIAL 1 (CASEY-046) · ALREADY-RIGHT / N-A 2 (SH-013 not listed for Casey; SH-006 has nothing to change in the Pre-Trip) · HELD 18 (CASEY-012, 016, 021, 032, 033, 041; CASEY-S01…S06; SH-007, 009, 015, 016, 017, 019) · SKIPPED-MISMATCH 0 (one ledger coordinate was wrong and was applied at the live line: CASEY-035) · NEEDS-DEVELOPER 0.

## 1 · Entries

`PT` = `00.0_Pre-Trip_Inspection.md`; datasheets by short name. Every changed value was re-opened against its live source after writing.

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| CASEY-001 | APPLIED | PT §C Step 2 `T8` | `16` Casey row "line 266" → **267** | `16` L267 = `\| Casey \| Mirny \| 1.11 \| 1,146,682 \| 38.7% \| 18.4% \| 42.9% \| C \|`; L266 is another city's row; header L241–248 still valid |
| CASEY-002 | APPLIED | PT §D Phase 1 `16` row; PT §E | L266 / 13 mentions → **L267** / L441, 2145, 2154, **2181, 2185**, 2203, 2206, 2210, 2222, 2224, 2228, 2247, 2428, 2804, 3484 | live `grep -n -i "casey\|bailey peninsula"`: 16 hits. **Differs from ledger's list by two** (L2181 = Casey's own `## 21. CASEY — DETERMINED` heading, upper case, missed by the case-sensitive builder; L2185 = "Bailey Peninsula-adjacent"). Added per brief rule 4 (`-i`, alias names). Old→new map checked against the pre-edit file (`git show 5ee58d0e`): all +5, L438→L441 +3 |
| CASEY-003 | APPLIED | PT §D Phase 4 `09` row | L87, L103, L148, L210, L252 → L87, **105, 150, 212, 254** | `09` live -i grep: 87, 105, 150, 212, 254 (all name Casey) |
| CASEY-004 | APPLIED (superset of ledger) | PT §D Phase 5 Airports | L47, L51 → **L3, L12, L21, L22, L23, L50, L54, L104** | live -i grep returns those 8 lines. Ledger gave L12, L50, L54 only. Extra five all name Casey (L3 marker note; L21–23 Relung Panen rows; L104 list-status note) and are labelled as such in the row. Headings checked: L40 "Everything Else Has No Air Access", L50–56 list |
| CASEY-005 | APPLIED | PT §D Phase 5 Ports | …L262, L538, L710 → …L262, **L298, L300, L561, L733** | live grep: 189, 196, 207, 218, 224, 232, 240, 244, 262, 298, 300, 561, 733 |
| CASEY-006 | APPLIED | PT §D Phase 5 Highways | L90, L199, L204 → + **L207, L274, L276, L278, L291** | all five open on the Relung Panen Spur text |
| CASEY-007 | APPLIED | PT §D Phase 5 RelDB | → **L21, 28, 49, 116–117, 163–164, 169, 180–181, 214, 340, 512** (Casey's entry L163–170) | live grep; `### Casey` = L163; L116–117 are inside `### Relung Panen (added 2026-10-21)` L111–118 |
| CASEY-008 | APPLIED | PT §D Phase 5 NatConn | → **L274, 290, 297, 300, 301, 307, 397, 424, 440, 469** | live grep; Casey section heading L290, Relung Panen link L301 |
| CASEY-009 | APPLIED | PT §D Phase 5 Cross-Subnet | + **L207** | live grep: 42, 54, 94, 99, 128, 207 |
| CASEY-010 | APPLIED | PT §A alias table | new row: Windmill Islands · Bailey Peninsula · Newcomb Bay | Ports L196, L561 (Newcomb Bay, Windmill Islands); Extent L608 ("Bailey Pen., Windmill Is."); `16` L2185 (Bailey Peninsula) |
| CASEY-011 | APPLIED | PT §D Phase 2 table (new row); `Phase_2.md` (two new rows) | composition file registered (SH-010) | composition file: heading L569, tier table L571–575 (matches spec L19–21 exactly); solar-UTC list L26–33, rule 1 at L28 ("Casey 110°32'E → +7"). Form copied from Santa Luce / Relung Panen `Phase_2.md`. PT row says plainly it is not one of the spine's three Phase 2 addresses, so the Phase 2 `T8` count line is unchanged |
| CASEY-012 | HELD | PT §D Phase 3 / §F | tier decision pending | DECIDE; not touched |
| CASEY-013 | APPLIED | PT §D Phase 3 row; PT §F row | "7 files" → "6 files and 1 subfolder" (both places) | `ls` of the withheld folder: 5 files + `README.md` = 6 files, 1 subfolder (names not opened; contents not read) |
| CASEY-014 | APPLIED | PT §C Step 0 `T8` | extent row 608 + "(2026-09-05 snapshot; the census is live — note L631)" | Extent L608 = 1,495,731; L631 = the snapshot note |
| CASEY-015 | APPLIED | `README.md` | Vision notes row marked "⛔ struck: not an input at any step (`DR-10`)" | `DEVELOPER_RULINGS_LOG.md` L437 `DR-10`; form follows Santa Luce README row |
| CASEY-016 | HELD | whole PT | WARM vs `06` | DECIDE; not touched |
| CASEY-020 | APPLIED | `Step_-1.md` | runbook L1821–1822 → **L1854–1855** | runbook L1854–1855 = "And `Specs/` "Status:" fields are POST-WAR…never an input to a Second Interwar pass" |
| CASEY-021 | HELD | `Step_-1.md` | "222 lines" | DECIDE (SH-009) |
| CASEY-022 | APPLIED | `Step_-1.md`, `Step_0.md`, `Phase_2.md` Census I rows | + Scenario `DR-68`, 2026-10-28, +12,140 H / +11,778 R, was 733,795 / 761,936 / 1,495,731 | census L485 carries exactly that |
| CASEY-023 | APPLIED | `Step_1_and_2.md` Half B row | 1,128,834 → **1,146,682**; L266 → **L267** (+ SH-014 clause, + note "refreshed 2026-10-28, `DR-68`, per `16` line 1") | `16` L267; `16` line 1 text read |
| CASEY-024 | APPLIED | `Step_1_and_2.md` | new row for `Reference/Real-World/Climate Data/READER/Casey.md` (annual −9.3; 12 monthly means) | READER/Casey.md L8 and L14 read; all 13 values match |
| CASEY-025 | APPLIED | `Step_1_and_2.md` Founding row | dropped "built by the Australian Antarctic Division"; now "(an infrastructure fact, `DR-24`; L166 separately states the Division *"operated specialized equipment at the real Casey Station"*)", cite L142, L166 | spec L142 does not say "built by"; L166 text copied word for word |
| CASEY-026 | APPLIED | `Step_1_and_2.md` Register row | + "row L58" | Register L58 = Casey · Mirny · +7 · Australia · "extremely close… comparatively easy access" · DR-19 |
| CASEY-027 | APPLIED | `Step_1_and_2.md` composition row; `Phase_2.md` rows 1 and 2 | "on a short, direct sea route from Australia" → "[the source's comparison with other cities is not carried]" | spec L20 / census L385 text is the superlative |
| CASEY-028 | APPLIED (tier part held with CASEY-012) | `Step_3.md` research-log row | "no Casey file" → names the 6 Casey-named files + the Relung Panen file whose name contains Casey; "names only, no tier assigned" | `ls Research_Logs \| grep -i casey` = those 7 names; `Casey_Research_Log.md` still absent |
| CASEY-030 | APPLIED | `Phase_2.md` per-nation row | all 13 × 4 counts replaced | spec L31–43 read; column sums by hand/Python = 773,714 · 745,935 · 612,848 · 445,030 = the census totals |
| CASEY-031 | APPLIED | `Phase_2.md` Retention row | 69.67/59.54/79.42/19.87 → **69.61 / 59.66 / 79.21 / 19.55** | by hand: 1,057,878÷1,519,649 = 0.69613; 445,030÷745,935 = 0.59661; 612,848÷773,714 = 0.79209; 79.209 − 59.661 = 19.548 → 19.55 pp |
| CASEY-032 | HELD | `Phase_3.md` | research folder | DECIDE |
| CASEY-033 | HELD | `Phase_3.md` L127 quote | hold until spec daylight error settled | DECIDE |
| CASEY-034 | APPLIED | `Phase_4.md` cross-check row | "1,128,834 / 1,128,834" → "1,146,682 / 1,146,682"; L266 → **L267** (+ SH-014 clause) | `09` L87 workforce 1,146,682; `16` L267 1,146,682 |
| CASEY-035 | APPLIED (ledger coordinate wrong; live line used) | `Phase_4.md` NMCI row | cite NMCI L214 (header), L216–225; "non-hub" now cited to RelDB **L49** (ledger said L47) | NMCI L214 = "# ⏸️ FOR FUTURE REVIEW — where the satellite campuses actually go", L216 "NOT decided", L225 names Casey. **RelDB L47 is the Halley row; the Mirny subnet row (hub Mirny; Casey under Member Cities) is L49.** Same wrong L47 appears in CASEY-S06 and `Casey_Audit.md` S-06 |
| CASEY-036 | APPLIED | `Phase_5.md` | new Highways row: Relung Panen Spur | Highways L207, L274–278, L291 read; quotes copied |
| CASEY-037 | APPLIED | `Phase_5.md` RelDB rows | L152–160 → **L163–169**; L160 → **L170**; neighbors now four; "non-hub" also cited to subnet table L49 | RelDB L163–170 read; L169 lists four neighbors; L170 = Notes line |
| CASEY-038 | APPLIED | `Phase_5.md` NatConn rows | L285–286 → **L291–292**; L289–290 → **L296–297**; L291–293 → **L298–300**; new row L301 | NatConn Casey section heading L290; each link read |
| CASEY-039 | APPLIED | `Phase_5.md` Port row + 4 new rows | L537, L709 → **L561, L733**; dash restored; rows for Ports L189, L196, L298, L300 | all five Ports lines read; L196 = "3,423 km · Newcomb Bay (§5.6) · Windmill Islands, Vincennes Bay · Direct, seasonal" |
| CASEY-040 | APPLIED | `Phase_6.md` roster row | "2-religion, 6-file roster" → 6 files in 2 developed folders + 4 empty roster folders named | `find` on `Factions/Robot_Religions/`: Polydimensional_Animism 5 files, Cymatics_reverence 1, four empty dirs; `grep -rli casey` = 0 |
| CASEY-041 | HELD | `Phase_6.md` | "378-line / 293-line" | DECIDE (SH-009); `wc -l` is 377 / 292, left as is |
| CASEY-042 | APPLIED | `Phase_7.md` | every `16` cite re-pointed (+5); new row on §21 counts; SH-014 clause | live: Baseline row L2185 … Technical/Maritime L2235–2236, notes L2240–2248; `16` line 1 "…were NOT recomputed"; 436,698 + 207,641 + 484,495 = 1,128,834; 207,641 + 484,495 = 692,136 ✓. §21 mandate heading (dated 2026-09-02) is L2192 |
| CASEY-043 | APPLIED | `Phase_7.md` MUST-OPEN box + header | "~5 of 13" and "13 of 13" → "6 of 13" (5 direct, 1 via Tier U); known-missing list now 7 items | see recount table |
| CASEY-044 | APPLIED | `Phase_9.md` | 50.94% → **50.91%** | 773,714 ÷ 1,519,649 = 0.50914 → 50.914% |
| CASEY-045 | APPLIED | `Phase_10.md` Pink Lucy row | "same finding in all four" removed; two files resolve to Janbogo, two read undetermined; characterization dropped | README L44, Formative_History L3 (resolved); Timeline L13, Conflict_Experiences L3 (undetermined) — quotes copied |
| CASEY-046 | PARTIAL | `Step_10.md` | `06` = 431 lines (`wc -l`); hits L292–L329; Casey section L292–L337; seventh row (`16` §21, "skip the whole section", `06` L315) added; orchestrator-exposure note added as coordinates and tier only. **Left: the `01` "§1 L65" coordinate (SH-007, HELD)** | `06` live. Ledger said "section L292–332"; live section runs to L337 (next heading L339), so L292–L337 is written |
| CASEY-047 | APPLIED | `Phase_9.md` Doll row | full path of the source + Tier U sheet path | source = `…/TepenianUniverseTimeline/Reference/Doll_Representation_Categories.md`, 35 lines by `wc -l` |
| CASEY-048 | APPLIED | `Step_6.md` | section 1 columns + "Subnet" | table L48 = `City \| Subnet \| Shape … \| Deficit address … \| Pass` |
| CASEY-049 | APPLIED | `Step_9.md` | item 5 paragraph added | runbook Step 9 item 5, L3011–3015, quoted word for word; form from Relung Panen `Step_9.md` |
| CASEY-S01 … S06 | HELD | spec, census, composition, `16`, timeline repo, RelDB/NMCI | SOURCE / DECIDE | untouched |

### Shared fixes

| ID | Result | File | Old → New (short) | Check |
|---|---|---|---|---|
| SH-001 | APPLIED | PT §G | spine L127 → **L220, L1114, L1140** | all three anchors read; L127 is a table row of "M" cells |
| SH-002 | APPLIED | PT §G | runbook L2178 → **L2180** | L2180 = "### ⭐ THE DIVERGENCE OPERATOR…"; row's other cite (No_National_Stereotypes file) unchanged |
| SH-003 | APPLIED | PT §C Step 5 | `02` §5.3 610–684 → **610–636** | `02` L610 "## 5.3", L637 "# 6. Symbol binding" |
| SH-004 | APPLIED | PT §C items 4, 5 | 620–643 and 701–703 → **620–643 and 682–684**; 650–703 → **667–684** | trial recipe L620–643 = Round 3 heading + four-question prompt; L682–684 = "Round 3's prompt now carries a fifth section"; L667 = "AMENDED 2026-09-28 — THE WRITTEN CONTENT IS A MERGE, NOT A PICK", box ends L684 |
| SH-005 | APPLIED | PT §C Step 10 (3 places) | 3057–3172 (×2) → **3057–3152**; card note "3045–3161" → "3057–3152" | runbook L3057 "# Step 10", L3153 "# Where everything lives" |
| SH-006 | APPLIED | `Step_-1.md` | L1821–1822 → **L1854–1855** | PT carries no such cite (grep) |
| SH-007 | HELD | `Step_10.md` | "§1 L65" left as is | brief |
| SH-008 | APPLIED | 11 sheets with the header | see recount table | by hand |
| SH-009 | HELD | all | "222 / 378 / 293-line" left as is. My two *new* counts are labelled `wc -l` (431, 35) | brief |
| SH-010 | APPLIED | PT §D Phase 2; `Phase_2.md` | composition rows (see CASEY-011) | |
| SH-011 | APPLIED | PT §C Step 0 only | snapshot label (see CASEY-014) | no datasheet and no §D Phase 0 row cites the extent table (grep) |
| SH-012 | APPLIED | PT + sheets | via CASEY-001…009, 034, 037–039, 042 | |
| SH-013 | N/A | — | not in Casey's ledger section | Casey is not in the list; §21 shares (38.7 / 18.4 / 42.9) equal Half B's, so no supersession to quote |
| SH-014 | APPLIED | `Step_1_and_2.md`, `Phase_4.md`, `Phase_7.md` | clause added beside the `16` baseline % / worker counts | `16` L1287 heading "CONSEQUENCE — the ten determinations so far need a baseline re-run"; flat-65 working value L1302–1304; range L1287–1305 written |
| SH-015…017, 019 | HELD | Tier U | orchestrator | |

## 2 · MUST-OPEN recount (SH-008), by hand, 2026-10-30

Counting unit = the spine's `📂 MUST OPEN` absolute-address lines (the unit `check_must_open_coverage.py` uses; N is confirmed for every sheet). Covered only where a row transcribes or cites the address by its full file / folder name; "via Tier U" = the sheet cites a Tier U sheet whose header names the address's source file. Names found only inside a "known missing" list do not count. Headers rewritten as "recounted by hand 2026-10-30".

| Sheet (phase) | Address → covering row | k of N (old header) |
|---|---|---|
| `Step_0.md` (0) | `Repo_Scope.md` → row "U `Repo_Scope.md`" · Timeline Eras/ → via Tier U (rows citing `Second_Interwar_Period_Quick_Reference.md`, whose header names `Timeline Eras/2 The Second Interwar Period/README.md`) · `Official_Population_Census.md` → Census I and II rows | **3 of 3** (2 direct, 1 via) — unchanged |
| `Step_1_and_2.md` (1) | `Worldspace/Locations/` → "Universe repo … directory enumerated" rows · `Specs/` → `Specs/Casey.md` rows · `Energy_Grid_Failure_Rationale.md` → its row · Climate READER/ → **new row (CASEY-024); not covered before it** · Stations/ → `Antarctic_Stations_With_Airstrips.md` L18/L68 + `COMNAP_…Catalogue.pdf` rows · `16` Half B → Half B row | **6 of 6** (6 direct) — 5 of 6 before CASEY-024 |
| `Phase_2.md` (2) | `No_National_Stereotypes.md` → via Tier U (`No_National_Stereotypes_Quick_Reference.md`) · `Falkland_Treaty/` → via Tier U (`Falkland_Treaty_Quick_Reference.md`) · Census → Census I/II rows | **3 of 3** (1 direct, 2 via) — was "3 directly" |
| `Phase_3.md` (3) | Climate READER/ → **not covered** · `Specs/` → `Specs/Casey.md` rows · Concept art → "Concept-art directory status" row · Megasheets → `Casey_Physical_Infrastructure_Attributes.md` row · (Davis research: n/a) | **3 of 4** (3 direct) — was "4 of 4" |
| `Phase_4.md` (4) | `Robot_Physiology_and_Cultural_Practices.md` → via Tier U · `Robot_Cold_Physiology.md` → via Tier U (both named in `Robot_Physiology_Quick_Reference.md`'s header) · `16` Half B → cross-check row · `09` → §2 row · `11_Caloric_…` → row · NMCI → row · `National_Economy_and_Currency.md` → **not covered** | **6 of 7** (4 direct, 2 via) — was "7 of 7 (5, 2)" |
| `Phase_5.md` (5) | `Worldspace/Locations/` → rows 1–3 · `Highways.md` → routing + spur rows · `Infrastructure/` bullet = `Airports.md` ✓ (Airport row) · `Ports.md` ✓ (Port rows) · `Geothermal_Heating.md` ✗ → **not counted (2 of its 3 files)** · Cross-Subnet → row · RelDB → rows · NatConn → rows | **5 of 6** (5 direct) — was "6 of 6"; 6 of 6 only if the `Infrastructure/` bullet is counted on any one of its three file names |
| `Phase_6.md` (6) | `Robot_Religions/` · `National_Holidays.md` · `Ice-Cold_Buddhism_Research/` · `The_True_Believer_Extraction.md` · `The_Meme_Machine_Extraction.md` → one row each | **5 of 5** (5 direct) — unchanged |
| `Phase_7.md` (7) | `Division_of_Industry/` (README carve-out) → via Tier U (gate box cites `Division_of_Industry_Reliability_Quick_Reference.md` and transcribes the README's line-1 stamp) · `16` → §21 rows · `Division_of_Industry_Sweep_2026-08-31.md` → §4.4 rows · `Theoretical-Calculations/` → row · `City_Logistics.md` → row · `Factions/` → row · **not covered (only in the known-missing list):** `01_Burden_Scoring_Model.md`, `08_Volume_Based_Requirement_Reference.md`, `National_Medical_and_Care_Institutes.md`, `Industry_Staffing_and_Productivity/`, `jobs_professions_and_fields/`, `National_Economy_and_Currency.md`, `Megacorps/` | **6 of 13** (5 direct, 1 via) — was "13 of 13"; the box said ~5. The README item is the one borderline count: without it, 5 of 13 |
| `Phase_8.md` (8) | `Robot_Biology_and_Culture/` → "mandatory facts" row · `Weapons_and_Tools_Philosophy.md` → row | **2 of 2** (2 direct) — unchanged |
| `Phase_9.md` (9) | `Laws_of_Robotics.md` → Laws row (**transcribes the text; never names the file; cites the Robot Physiology sheet, which does not carry the Laws**) · `Robot_Universals/` → rows · `Doll_Representation_Categories.md` → Doll row (full path now, CASEY-047) · human-robot baseline (`Robot_Physiology_and_Cultural_Practices.md`) → via Tier U | **4 of 4** (3 direct, 1 via) — same split; note written into the header. Strict reading: 3 of 4 |
| `Phase_10.md` (10) | `Characters/` → Pink Lucy row (path) · `Enneagram_Character_Index.md` → row · `Zodiac_Signs_Full_Attributes.md` → via Tier U (`Zodiac_Signs_Quick_Reference.md`) | **3 of 3** (2 direct, 1 via) — was "3 directly" |

`Step_-1`, `Step_3`, `Step_5`–`Step_10` carry no MUST-OPEN header; nothing to recount.

## 3 · New findings (not in the ledger; not fixed)

1. **Ledger/audit coordinate error:** RelDB "L47" (CASEY-035, CASEY-S06, `Casey_Audit.md` S-06) is the Halley row; the Mirny subnet row is **L49**. CASEY-S06 should be re-pointed before the developer walk-through.
2. **`Phase_9.md` Laws row:** cites `Robot_Physiology_Quick_Reference.md`, which holds no Laws text (grep of all Tier U sheets finds none); wording also differs slightly from `Laws_of_Robotics.md` L3–4 ("the full capacity", "it is also realistically possible"). The source file is never named.
3. **`Step_-1.md` "non-hub member | `Specs/Casey.md` L5":** "non-hub" is not on spec L5 (the source is RelDB L49). I fixed the same defect in `Phase_4.md` and `Phase_5.md` (inside CASEY-035/037) but left this row.
4. **Census II rows** in `Step_-1`, `Step_0`, `Phase_2` carry no `DR-68` tag although census L608 does (CASEY-022 names Census I only).
5. **Phase 7 sheet still carries post-war and spec-error text** inside rows I only re-pointed (the §21 "Additional notes" row quotes "winter days shrink to ~5 hours" = CASEY-S02; `Phase_3.md` L127 quote likewise = CASEY-033). Held.
6. **`Step_10.md` now says "skip the whole `16` §21 section"** (from `06` L315) while the Pre-Trip (§D Phase 1, 4, 7; §E) and `Phase_7.md` read it: consistent only because the run is WARM (CASEY-016).
7. **Pre-Trip banner** still says line numbers were refreshed 2026-10-21 and §I's raw block (74 claims, dated 2026-10-21) is now out of date; I did not add a banner (not an entry). The Phase 2 `T8` line still says "the 3 admissible rows" (the new composition row is flagged as outside the spine's three).
8. `16` §21 cites `Highways.md` "L56, L89, L197" internally (L2208); the live Hwy 2 / Hwy 110 headings are L88 / L197 (L56 is unchecked). Source-file issue, not Casey's sheets.
9. `Phase_3.md` still says "Per-city research folder … none exists" (CASEY-032, held) beside the new `Step_3.md` list of seven Casey-named research files.

### Incidental exposure (for the orchestrator)
- To re-point `Phase_7.md` I read Casey's `16` §21 in full (L2176–2262). `06` L315–L331 says a Casey pass must skip it and that a fresh session must run Casey's ULM; this sweep session did not run any pass step, but it is another session that has read §21.
- One `awk` range meant for the differentiation-table header (L48) also printed the first 240 characters of L50 (the Davis row); nothing from it was used. A `grep` for section headings of `16` also printed the title of another city's section (L2110).
- I read the four Pink Lucy character files (timeline repo, read-only) to check CASEY-045.

## 4 · Files edited (all with the Edit tool; none outside the brief's list)

`PASS` = `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey`

- `PASS/00.0_Pre-Trip_Inspection.md`
- `PASS/README.md`
- `PASS/Datasheets/Step_-1.md`, `Step_0.md`, `Step_1_and_2.md`, `Step_3.md`, `Step_6.md`, `Step_9.md`, `Step_10.md`
- `PASS/Datasheets/Phase_2.md`, `Phase_3.md`, `Phase_4.md`, `Phase_5.md`, `Phase_6.md`, `Phase_7.md`, `Phase_8.md`, `Phase_9.md`, `Phase_10.md`
- created: `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Casey_Sweep.md` (this report)

Not touched: `00.2_Position_Coverage_Ledger.md` (no entry names it), `Step_5.md`, `Step_7.md`, `Step_8.md`, every numbered pass output, `FIX_LEDGER.md`, `TRACKER.md`, the builder scripts, every source file.
