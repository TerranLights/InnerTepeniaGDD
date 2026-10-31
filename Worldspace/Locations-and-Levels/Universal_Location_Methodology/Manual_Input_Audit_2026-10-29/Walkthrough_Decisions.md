# Walk-through decisions (2026-10-30 on)

The developer's answers, city by city, to the items the sweep left open. Order: by subnet, starting with the Mirny subnet (Casey, Relung Panen, Davis, Kunlun, Mirny, Ariun Nuur, then the finished Shirayuki, Sinheung and the two Zhongshan folders; Concordia last). The ledger rows are updated as each city closes; this file keeps the answers in the developer's words.

Standing statement, repeated by the developer 2026-10-30 (already binding as the ONE LOCATION law): *"During this process, never, ever, ever, never compare anything to anything else. Everything gets done on its own terms. After everything is all finished, then we can start comparing cities to each other."*

---

## Casey (done 2026-10-30)

| # | Item | Developer's answer | Done |
|---|---|---|---|
| 1 | Spec L67 temperature line | *"Whatever the actual real-world research says, that's what we use. So go ahead and write the official specs."* | Spec L67 now July mean −14.7 / August −14.9 / January −0.3 (the spec's own table) |
| 2 | Daylight hours in the spec | *(same ruling)* | Spec L51, L96, L97, L108, L127, L132: about 2.5 hours at the winter solstice (computed from 66°16′54″S: 2.49 h) and 24 hours of midnight sun around the December solstice; `16` L2241 "~5 hours" → "~2.5 hours". Line counts unchanged |
| 3 | "Shortest Australia-to-Antarctica route" | *"I'd say your recommendation is the right one. Go ahead and replace it with that."* | Spec L20, census L385, composition file L574 → "a direct sea route from Australia". Casey sheets updated |
| 4 | Subnet hub | *"Mirny is the subnet hub. So Casey is not the subnet hub, no."* | `National_Medical_and_Care_Institutes.md` L224–225: "Mawson (a subnet hub) and Casey"; Casey's `Phase_4.md` row updated |
| 5 | Worker counts in Casey's `16` section | *"we can leave them for now and address them later."* | Left; the sheet already labels them. Revisit when per-city administration values are set |
| 6 | Pink Lucy files | *"Pink Lucy's life background is still open for development, so nothing about her whole trajectory towards Concordia is conclusively determined yet, no."* | Nothing edited in the timeline repo. Casey's `Phase_10.md` row now carries this statement; memory note corrected |
| 7 | Warm or cold | *"It is indeed a warm run."* (cold runs build the method; warm runs produce results) | Sheets stay as built; one sentence added to the `06` Casey heading line |
| 8a | Inspiration-place logs R1/R2 | *"sure, that works"* | Read-allowed at Step 3 (Pre-Trip Step 3 reads; `Step_3.md`) |
| 8b | Four Casey–Mirny airport files | *"Definitely."* + the standing statement above | WITHHELD (Pre-Trip §F; `Step_3.md`) |
| 8c | Relung Panen port-research file | *"agreed"* | Listed as "not a Casey input" |
| 8d | Phase 3 "no research file exists" | *"Yes, go ahead and correct that."* | `Phase_3.md` row corrected |
| 9 | Composition file at Phase 2 | *"sure, that works"* | Pre-Trip Phase 2 `T8` line now "the 4 admissible rows" |

The shared questions that apply to every city were answered next; see "Shared batch A–E" below. Casey's "222 / 378 / 293-line" rows and the "line 65" pointer in her `Step_10.md` are fixed by that batch.

Noted, not changed: the phrase "shortest Australia-to-Antarctica route of any Tepenian city" also stands in the culture-tier file `Neo-Races-and-Cultures/Mirny_Subnet/Casey/Casey_Catalog.md` (not opened, not edited). The composition file's section for another city (L564) uses a similar superlative; it belongs to that city's walk-through.

---

## Shared batch A–E (answered and applied 2026-10-30, during the Casey walk-through)

Developer: *"Definitely, I think your suggestions for Items A through E are all correct. Go ahead and do all of them."* Applied to every city with a datasheet set (34 pass folders), the shared reference sheets and the builders. Concordia has no pass folder; Shirayuki, Sinheung, Zhongshan Opus and Zhongshan Sonnet are finished passes (see the last paragraph).

| Item | Ruling | What was done |
|---|---|---|
| **A** line counts | `wc -l` everywhere | 292 counts that were one too high (file-length statements such as "a 378-line file") corrected in 190 sheets, each checked against the live file by script; counts for files that had grown since the sheet was built set to the live figure (Santa Luce spec 192 → 193, Ariun Nuur spec 203 → 205, the provenance file `06` 428–430 → 431 after every "zero hits" claim about it was re-run live, Falkland draft 141 → 140). A final scan finds no file-length statement left that is one too high (every statement it can match to a file now equals `wc -l`). `build_datasheets.py` now counts with `wc_l`. Not counted: numbers that are counts of hits, not file lengths |
| **B** "line 65" | name the row, not a number | `06` (Casey's entry) and Casey's `Step_10.md` now say "the `Resettled` row of the Status-modifier table" (at L137 on 2026-10-30) and "skip the `Resettled` row". No other city's sheet copies it. Left as dated record: `Pre-Contamination_Reviews/Casey_Pre-Contamination_Review.md` (still says line 65, as it did when written) |
| **C** must-open coverage | honest counts stand; a Tier U extract counts only if the city's sheet cites it and its own source list names the file | No rows added. The rule is written into the `check_must_open_coverage.py` docstring. No Phase 7 sheet cites the roster extract, so no count changes. Two "queued for completion in the post-15:00 audit" notes (Casey and Mirny Phase 7) now say the count is accepted |
| **D** Laws of Robotics row | quote `Laws_of_Robotics.md` word for word, cite the file | 32 `Phase_9.md` rows rewritten (text from L3–6 of the file; Denison's combined row edited in place; Davis keeps its own citation); the headers that said "3 of 4" now say "4 of 4"; Cape Adare and Zukelli were already right. `build_datasheets.py` fixed |
| **E** four Tier U sheets and the runbook | update to the current runbook | Step 10 sheet (item 7 replaced, range L3057–L3152, three omitted sentences restored); Step 9 sheet (five items, range L2986–L3056); Differentiation sheet (ranges L420–L526 and L2886–L2921, row/column by table shape; a closing sentence that no live runbook line supports was removed); Founders and Renames sheet (pass-folder sentence corrected, Alias Table §3b quoted, ranges and counts re-pointed). The false rename sentence fixed in the two Pre-Trips that still carried it (Santa Luce, Relung Panen) and in `build_pretrip.py`. Per-city `Step_9.md` re-worded in 33 sheets (the quick index in 32, Denison's differentiation sentence in one); Denison's and Ariun Nuur's `Step_6.md` and Denison's `Step_10.md` item-7 row corrected. Runbook Step 6 (L2904), its summary line (L471) and the stepwise copy now say ROW for a city; runbook still 3179 lines |

**Left alone, flagged (not part of "one word in the runbook"):** other files that still say "column" for the city table: `04` Part III (written for both tables), `03` L146, `01` L513, `ULM_At_A_Glance`, `ULM_Piece_Index`, `Location_Data-Input_To-Do`, `ULM_Input_Available_Audit`, `PRE-TRIP_INSPECTION_RECIPE_TRIAL`, the project `CLAUDE.md` (two lines), the Zhongshan Opus and Sonnet Pre-Trips (finished passes), and runbook L1667 (that one is about the industry table, a different file). Developer to say whether to harmonize them.

**Finished passes (Shirayuki, Sinheung, Zhongshan Opus, Zhongshan Sonnet):** no pass files were edited. If any of them carries a batch item (a "line 65" pointer, a file-length statement one too high, the "add this city's column" wording in the two Zhongshan Pre-Trips), it goes into that city's amendment-note file when it is walked.


---

## Relung Panen (done 2026-10-30)

Developer: *"yup, all as recommended"* (seven items).

| # | Item | Done |
|---|---|---|
| 1 | Retention figure, spec L21 | 71.5% → 71.4% (694,013 ÷ 971,870 = 71.41%); the copy in `Step_-1.md` follows |
| 2 | Culture files, spec L215–216 | now names the four stub files (`Local_Cultures`, `Local_Robot_Culture`, `City_Vision_Notes`, `City_Enneagram_Personalities`, all dated 2026-10-23) and says there is no `City_Megasheets` entry |
| 3 | Broken links, spec L43, L111, L295 | now `../../Relung_Panen/…`; both targets exist; the copy in `Step_1_and_2.md` follows |
| 4 | "31.7 million people" sentence, spec L219–222 | L220–221 rewritten in place: "whoever controls that input controls what this city can grow … a real point of exposure". Spec still 295 lines. The figure also stands in `Relung_Panen_Dossier_2026-10-03.md` (a dated record; not edited) |
| 5 | `Inspirational-Influences.md` L120 | further candidates (#27–#97) "were researched in two rounds on 2026-10-29; their tiers await the developer"; file still 325 lines; the `Step_3.md` row re-copied |
| 6 | Comparison sentences inside the specs | **Left in the specs** (the sheets already bracket them as "not carried"); comparing is for the terminal pass. This answer is the working rule for every city unless the developer says otherwise |
| 7 | Tidy-ups | stray asterisks removed from the Pre-Trip "Real-world basis" row (cause fixed in `build_pretrip.py`); pass `README.md` opening reworded (no longer "empty by design"); the Phase 7 meta row now says "13 of 13" in all 19 sheets that still said "11 of 11" |

Also done for this city under the shared batch: Laws row and Doll row (full path and Tier U sheet).
Not asked, not done: the ⚑ judgment calls in `Sweep_Reports/Relung_Panen_Sweep.md` §4 stand as written (the two other cities named in the climate-source row stay bracketed).

---

## Davis (decided 2026-10-30; one item waits for approval)

Developer: *"yup, all as recommended"* (five items). Davis is a finished pass: no pass file edited; sheets marked as dated records; filed in `Davis/Amendment_Notes_2026-10-30_Manual_Input_Audit.md`.

| # | Item | Done |
|---|---|---|
| 1 | Old population figures in the sheets | kept, labeled "as recorded at the pass (2026-09-16)", live figures beside each (7 files; derived values recomputed by hand) |
| 2 | Conclusions inside the sheets | kept as a record; strip before any reuse |
| 3 | Half B vs Davis's own ruling | Davis's §19 ruling (28.2% / 31.1%) governs; `16` untouched; the sheets say so |
| 4 | Two relationship passages that lean on removed grounds | **APPLIED 2026-10-30** after approval ("all as recommended"); the draft below is what went in |
| 5 | Small corrections in the sheets | all applied (Ports row, Airports row, Phase 7 rows 2 and 12, two citation pointers, Pre-Trip §K, Pre-Trip "4 admissible rows") |

### Item 4 — drafted replacement wording (re-ground, do not drop; every line count preserved)

Grounds used: the Founding Register (Casey and Davis: Australia; Mawson: Kazakhstan, Russia and Australia jointly; Mirny: founded by Idelsk-Uralia, exile groups present Russia, Australia and the Sinian Federation) and `Highways.md` L199 (Hwy 110 runs Zhongshan → Davis → Mirny → Casey → Concordia). The namesake story is removed as a basis (`DR-32`); the connection ratings and types are unchanged.

`City_Cross_Subnet_Relationships.md`, L123–127 (5 lines):

```
- **Davis (Mirny) ↔ Mawson (Mawson).** Australia is among the founders of both (Founding Register: Davis,
  Australia; Mawson, Kazakhstan, Russia and Australia jointly); confirmed administratively separate,
  symbolic-only connection (occasional ceremonial/national-holiday acknowledgment, not genuine
  operational ties) — established in `Davis_Full_Extrapolation.md` Section IV, low-cost severance under
  the Planetary Split Brain since there was never a deep working relationship to lose.
```

L128–131 (4 lines):

```
- **Mirny subnet's internal links (Davis, Casey, Mirny — Hwy 110 runs through all three) survive the Split Brain**,
  per the same Full_Extrapolation finding — genuinely relevant here because it's the explicit contrast
  case proving intra-subnet links survive while inter-subnet links (like the Davis-Mawson one above) were
  actually severed.
```

`City_National_Connections.md`, Davis's section, L304–308 (5 lines):

```
- **Mawson** (Mawson) — Medium, Cultural/Historical. Australia is among the founders of both cities
  (`DR-19`; Founding Register). *(The real-world namesake thread that stood here is removed: namesakes
  are never a basis, `DR-32`.)*
- **Casey** (Mirny) — Strong, Cultural. Both founded by Australia (`DR-19`; Founding Register), on the same highway, Hwy 110.
- **Mirny** (Mirny) — Strong, Cultural/Infrastructure. Australia is among the exile groups present at Mirny (Founding Register); Hwy 110, plus Mirny's own Relay Vaults link.
```

The same "Australian-heritage network" wording also stands in `City_National_Connections.md` L274–278 (Mirny's section) and L293–295 (Casey's section); drafted the same way so one approval covers all of them:

```
L274–276:
- **Casey** (Mirny) — Strong, Cultural/Infrastructure. Casey's founder, Australia, is among the exile groups
  present at Mirny (Founding Register), and Hwy 110 joins the two; the intra-subnet link the Planetary Split Brain
  never severed, and connected through Mirny's own Relay Hardware Vaults, the intra-subnet Arcanet hub.
L277–278:
- **Davis** (Mirny) — Strong, Cultural/Infrastructure. Davis's founder, Australia, is among the exile groups
  present at Mirny (Founding Register); Hwy 110 and the same Relay Vaults connection.
L293–294:
- **Mirny** (Mirny) — Strong, Cultural/Infrastructure. Australia (Casey's founder) is among the exile groups
  present at Mirny (Founding Register); Hwy 110 joins them, plus Mirny's own Relay Hardware Vaults.
L295:
- **Davis** (Mirny) — Strong, Cultural. Both founded by Australia (Founding Register), on the same highway, Hwy 110.
```

Not touched by this draft: `City_Cross_Subnet_Relationships.md` Part 3 (L139–147), which already says namesakes are never a basis but still speaks of "the existing 'shared naming heritage' treatment (Part 2)", so one sentence there would read as stale once Part 2 is changed.


---

## Kunlun (done 2026-10-30)

Developer: *"yup, all as recommended"* (ten items; Davis item 4 approved in the same answer).

| # | Item | Done |
|---|---|---|
| 1 | Research logs R1 (454 lines) and R2 (320 lines) | read-allowed at Step 3 (neither names another Tepenian city; checked by name); added to the Pre-Trip Step 3 reads; `Step_3.md` row corrected |
| 2 | Nation counts, spec L50–69 | recomputed as share × 135,226 (USA 20,865, China 20,581, Russia 15,483 …); total 135,213, a gap of 13 because the shares sum to 99.99%; stated on L71; `Phase_2.md` follows |
| 3 | 19 or 20 nations | the Netherlands row (0.05%) is what completes the shares, so it stays: **20 nations**; spec L82 now "seventeen". Still saying "19-nation" (dated history, not edited): `Station_to_City_Map.md` L119, `Overview.md` L169, `Official_Population_Census.md` L452 |
| 4 | Spec L103 | −54 °C (the annual mean already on L89); the "#1 coldest of the 37" rank dropped |
| 5 | Spec L106 | remnant deleted; "approximately Apr 18 → Aug 26 (~131 days)" stands (verified for 80°25'S) |
| 6 | Spec L34 | "No Census II row exists for this city (the census lists Kunlun as remaining without Census II figures …)" |
| 7 | Two splits | §22 (26.8% / 44.6%, provisional; you are weighing 35.7% / 35.7%, register item 15, `16` L3569) governs over Half B (0.0% / 71.4%); `16` untouched; Phase 7 quotes both |
| 8 | Phase 7 comparisons | "highest in roster" bracketed as not carried; the "another still-unassessed city" clause removed |
| 9 | Phase 3 megasheet row | sibling file names removed; the folder's other entries are counted, not named |
| 10 | Phase 5 must-open list (shared) | **the spine governs** (it is the contract); no edits; the runbook table's Arcanet mention is recorded as a disagreement, not acted on; honest counts stand. Applies to every city |

Other canon files that still carry Kunlun's old robot total 123,449 as dated history (not edited, flagged): `Station_to_City_Map.md`, `Overview.md`, `City_Relationship_Database.md` L512, `Official_Population_Census.md` L452. Flag only (timeline repo, no worldbuilding edits): `Worldspace/Locations/README.md` L20 still lists "Vostok".


---

## Mirny (done 2026-10-30; one new question open)

Developer: *"for Item #6, make a note in the Weekly To-Do to address that in the future. Everything else can go as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Sheet openers | the Pre-Trip already carried a record banner (refresh of 2026-10-21); a one-line "pre-run record" banner added to all 19 datasheets; `Step_-1`'s "has NOT started" opener reworded |
| 2 | Extra addresses | R1 (473) and R2 (460) read-allowed at Step 3 (neither names another Tepenian city); the four Casey–Mirny airport files WITHHELD and the Russia-split RS2 file "not an input" (Pre-Trip §F); the Airports, Ports, composition (Mirny's section, heading L559) and Register lines and rulings DR-76, 77, 79, 82 registered in §J; `Step_3.md` row updated |
| 3 | README archive paragraph | left until the amendments finish |
| 4 | Spec L69 | mean −16.3 °C / −16.4 °C; warmest month (January) mean −2.0 °C |
| 5 | Spec L112 and L118 | "no polar night"; "midnight sun (nearly a month around the solstice)"; spec still 230 lines |
| 6 | Spec L82 rank | **left**; a line was added to `Dev-Road-Map/Weekly_To-Do_-_Current.md` ("City specs: sentences that compare a city to other cities") |
| 7 | Winter Intake Airport (`DR-82`) | filed at 14:43 as section 4 of `Mirny/Amendment_Notes_2026-10-30_Manual_Input_Audit.md`: R-57 and PA-25 are touched, not overturned; `DR-51`'s deferral stands; five more `DR-82` lines recorded; no pass file edited |
| 8 | Small sheet fixes | Phase 7 box says 6 of 13; the last Phase 7 row has its citation cell (`Worldspace/Factions/`); Phase 5 relationship row restores "as the subnet hub, likely"; Phase 5 airport row cites L3 (the list) and L12 (Mirny's row) |

**Composition file L564** (Mirny's own row, "one of the shortest Australia-to-Antarctica routes"): approved with the Ariun Nuur answers and changed to "a direct sea route from Australia" (file still 1,299 lines).


---

## Ariun Nuur (done 2026-10-30)

Developer: *"yup, all as recommended"* (ten items, the tenth being Mirny's composition-file row).

| # | Item | Done |
|---|---|---|
| 1 | Research logs R1 (316) and R2 (298) | read-allowed at Step 3 (the only name matches are real-world: UC Davis, the word "troll"); Pre-Trip Step 3 reads, §J and `Step_3.md` |
| 2 | "Vostok" inside the sheets | no mass rename; a banner on the Pre-Trip and the 19 sheets; the five spec quotes (`Step_1_and_2` row 26; `Phase_3` rows 13, 15, 16) re-quoted from the live spec with ellipses |
| 3 | Spec L49 | "There is no coastal access; Hwy 37, the only highway, runs through it, and the nearest city, Kunlun, is a very long way away." |
| 4 | Spec L142 | "the subnet hub, Mirny" |
| 5 | Spec L76 | "At −54.8 °C (the annual mean) it is bitterly cold" |
| 6 | Spec tidy-ups | L73 ~3 mm/yr; L63 means (July/August −65.9 / −66.9, December/January −31.3 / −31.9); L169 path now `TepenianUniverseTimeline/Worldspace/Characters/Dolls/TBN [XT-17 …]/`; spec still 205 lines |
| 7 | `09` L201 (old 41.5% in the 19-vs-21 comparison) | left; the sheets cite the refreshed table |
| 8 | Small sheet fixes | `Step_-1` cites L49 for the Pole of Inaccessibility; `Phase_3` row 11 reworded; the copies of the temperature range and the precipitation figure in `Step_1_and_2` follow the spec |
| 9 | File 16 §23 beside Half B | nothing more wanted |
| 10 | Composition file L564 (Mirny) | changed to "a direct sea route from Australia" |


---

## Shirayuki (done 2026-10-30)

Developer: *"yup, all as recommended."* Shirayuki is a finished pass with no Pre-Trip or datasheets; no pass file was edited. All entries are in `Shirayuki/Amendment_Notes_2026-10-30_Manual_Input_Audit.md`.

| # | Item | Done |
|---|---|---|
| 1 | Oct 28 census change | old values labeled "as recorded at the pass (2026-09-06)" with the live ones beside them, derived figures recomputed by hand (retention 61.91 / 58.50 / 65.18, gap +6.68 pp, not here 413,060, 8.4% above the line, footprint 108–155 km², rock about 9–12%, workforce 818,919) |
| 2 | Retired names | one alias entry with file counts |
| 3 | Three notes | `16` §16 counts pre-cut; two Phase 5 phrases not in the Airports file; runbook line numbers as of the pass |
| 4 | Census tier list | `Official_Population_Census.md` L426–428 now match the spec (Primary Japan …); census still 810 lines |
| 5 | Extent L616 and L656 | left; the amendment note carries the live figures |

**Added by the developer in the same message:** (a) a to-do to create the Pre-Trip and datasheet files for the cities that have none (Shirayuki, Sinheung, Zhongshan Opus and Sonnet — Pre-Trips exist but no datasheets — and Concordia); (b) a plan to re-analyze the finished cities (Shirayuki, Sinheung, Zhongshan) with the current methods. Both are in the Weekly To-Do ("Finished cities: Pre-Trips, datasheets and a fresh analysis") and in memory `project_reanalyze_finished_cities`. Neither is started. The amendment notes are the interim record.


---

## Sinheung (done 2026-10-30)

Developer: *"yup, all as recommended."* Finished pass, no Pre-Trip or datasheets; no pass file edited. Entries are in `Sinheung/Amendment_Notes_2026-10-30_Manual_Input_Audit.md`.

| # | Item | Done |
|---|---|---|
| 1 | Oct 28 census change | filed: Census I 479,411 / 506,921 / 986,332, Census II 815,309 (402,176 / 413,133), old values labeled "as recorded at the pass (2026-09-07)" |
| 2 | Retention | 82.66 / 83.89 / 81.50, spread +2.39 pp |
| 3 | Workforce | 746,627 |
| 4 | `16` §17 | the determination (28.2% / 31.2%, L1834) supersedes Half B (26.7% / 32.6%) |
| 5 | Climate | Mean column replaced 2026-10-21; annual −9.9 °C; range −16 °C; READER file rebuilt |
| 6 | Spec L4 | now "Soyuz" (spec 243 lines) |
| 7 | Spec L128 | reworded to the READER `Zhongshan` series |
| 8 | Retired names and README path | one alias entry; README L51's path noted |
| 9 | Census tier list | L416–418 now match the spec (Primary South Korea …); census 810 lines |
| 10 | Extent L620 and L657 | left; live figures in the note |


---

## Zhongshan, Opus and Sonnet folders (done 2026-10-30)

Developer: *"yup, all as recommended."* Opus is a finished pass (Pre-Trip, no datasheets); Sonnet is a partial trial (Step −1 to Phase 3, Pre-Trip, no datasheets). No pass file was edited. Each folder has a new `Amendment_Notes_2026-10-30_Manual_Input_Audit.md`.

| # | Item | Done |
|---|---|---|
| 1 | Three stale lines in both Pre-Trips | dated notes beside the §E headcount (live 580,925 H / 594,481 R), the §J footprint line (live 325–464 km², about 88–91%) and the runbook size / Step 10 range (as of 2026-10-21; 3,179 lines and Step 10 ending at L3152 now) |
| 2 | Census change | Census I 580,925 / 594,481 / 1,175,406; Census II 478,243 / 434,620 / 912,863; old values labeled, file counts given (Opus 8 files, Sonnet 4) |
| 3 | Retention | 77.66 / 82.32 / 73.11, spread 9.22 pp, not here 262,543 |
| 4 | Workforce and `16` (Opus only) | 884,944 (required 315,302, 35.6%); counts scale by 1.02058 (about 364,320 / 136,663 / 383,961); §18 governs over Half B |
| 5 | Footprint and ice | 118–168 km²; cluster 325–464 km²; ice about 88–91% |
| 6 | Retired names | one alias entry per folder |
| 7 | Rewritten spec sentences | filed as a note; Register row L60 |
| 8 | Extent L613, L655, L593 | left; live figures in the Opus note |

Remaining in the Mirny subnet: none except Concordia (not in the subnet folder). Next: Concordia, then the other subnets (Halley, Janbogo, Mawson, Byrd, Palmer, Amundsen Station).


---

## Concordia (decided 2026-10-30; culture-sheet edits scheduled for 2026-10-31, 05:00–14:59)

Developer: *"yup, all as recommended."* Concordia uses the district method; no Pre-Trip or datasheets; no district file or megasheet edited. Entries are in `Concordia-City/Amendment_Notes_2026-10-30_Manual_Input_Audit.md`.

| # | Item | Done |
|---|---|---|
| 1 | Oct 28 census change | filed (Census I 516,937 / 522,926 / 1,039,863; Census II 317,175 / 333,972 / 651,147; orbit share 37.4%; retention 61.36 / 63.87). **Cultural-sheet lines L11–12: to be restated 2026-10-31 in the window.** Megasheet copies: compilation method |
| 2 | Polar night and midnight sun | filed (about 98 and 103 days; other climate values). **Sheet L57: 2026-10-31.** Megasheet copies: compilation method |
| 3 | Acclimatization sentence in the megasheet copies | filed; compilation method |
| 4 | Founders in the cultural sheet (eight lines) | filed as a status entry. **Drafts to be shown to the developer on 2026-10-31 before any edit** |
| 5 | Refugee-diaspora weights | dated note filed; not recomputed |
| 6 | Retired names | one alias entry with counts |
| 7 | Spec L104 | now the table's means (June/July/August −64.1 / −63.2 / −63.3; December/January −30.7 / −31.3); spec 292 lines |
| 8 | Spec L117 "#4 coldest of the 37" | left (Weekly To-Do) |


---

## Halley (done 2026-10-30)

Developer: *"yup, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Alias set | confirmed: Halley Bay, Halley I … VI, Halley Research Station, Halley Skiway, Hallite; Brunt Ice Shelf, Coats Land and the Weddell Sea are places (Pre-Trip §A and §J) |
| 2 | Research files | the Russia-split RS3 file (Halley and Janbogo) registered as "not an input" (Pre-Trip §F, `Step_3.md`); noted that no Halley inspiration-place research exists yet |
| 3 | Phase 5 Ports row | the Background-Lore vignette path struck |
| 4 | Phase 10 Salagéa row | DLC-companion wording excluded |
| 5 | Spec L69 | record high now approximately +7°C (spec 217 lines); `Step_1_and_2` follows |
| 6 | `16` §3 vs Half B | §3 (478,952 / 170,093 / 448,426 = 43.6 / 15.5 / 40.9) governs; quoted beside Half B in `Step_1_and_2`, `Phase_4`, `Phase_7` |
| 7 | Composition note L262 vs Register L46 | composition file untouched; a flag row in the Pre-Trip §J |
| 8 | Spec peer rank L81, nation order L28, precipitation | left (see "Recurring patterns") |
| 9 | Stale README opening (shared) | 29 READMEs reworded (all cities with datasheets and no pass output); pass files of run or finished cities untouched |

### Recurring patterns to decide once, at the end of the walk-through

- **Monthly precipitation column vs the annual figure in the text** (Halley: text "300–450 mm", "falls ~450", table 346; Mawson `MW-S01`; Temirötkel `TK-S05`; more may follow). Options: label the monthly column design-grade, or align the text to the table. Left as is for now.
- **Cross-city comparison sentences inside specs** (Weekly To-Do carries this).


---

## Belgrano (done 2026-10-30)

Developer: *"yup, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Alias set | confirmed: Belgrano II, II Base, II Skiway, Station II, Manuel Belgrano (naming fact), Belgranian / belgranteco; "Coats Land coast / Weddell Sea sector" and "Queen Maud Land" are places |
| 2 | Phase 10 rows | Trisha Miller L7, Salagéa L7 and Griselda L67 excluded as later-era |
| 3 | Spec L68 | means: July/August −20.9 / −20.7 °C; December/January −2.6 / −2.4 °C |
| 4 | Spec L67 | record high +12.1 °C (December) |
| 5 | Spec L122 | "three cities in two subnets" |
| 6 | Spec L80 | ~105 mm/yr; spec still 169 lines |
| 7 | `16` §2 vs Half B | §2 (34.0 / 42.9 / 23.1) governs; quoted beside Half B in `Step_1_and_2`, `Phase_4`, `Phase_7` |
| 8 | Small fixes | Register row cited as L53 (not "L39, 53"); Cross-Subnet L112 removed from the lists (a memory-file identifier) |
| 9 | Left | spec L83 peer rank, L96 "0*", Phase 7 Factions line numbers, timeline README flag |


---

## Lazar (done 2026-10-30)

Developer: *"yup, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Alias set and Maitri names | confirmed (Maitri, Maitri Station, Schirmacher Oasis, Novo Runway); lines naming only Maitri added: Stations L83 (new row in `Step_1_and_2`), COMNAP pages 50 and 51 (verified in the PDF), census L200, composition L1081 |
| 2 | Spec L107 | "At −10.0 °C (the annual mean) this is not a city defined by its cold"; rank dropped |
| 3 | Spec L16 and L149 | live totals (Census I 2,382,205; Census II 1,639,426); percentage-larger claims dropped; Lazar is still the largest (next: Esperanza 1,902,205 / 1,193,886); spec 216 lines |
| 4 | ABCC clause beside the `09` and `11` rows | not added (it concerns `16`'s baseline only) |
| 5 | Left | composition stale-total flag (L336), "~0%" probabilities, Neumayer comparisons, "3 admissible rows", `16` L187 heading in the lists, timeline README flag |


---

## Neumayer (done 2026-10-30)

Developer: *"For Item #3, trim it down as you recommend, but also include a pointer to a file that contains her full trajectory for referencing context. Everything else, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Alias set | confirmed (Atka Iceport, Neumayer Station I / II / III, Neumayer-Station III, Neumayer III Skiway, Georg von Neumayer); Ekström Ice Shelf and Queen Maud Land are places; Ports L97 added to the list (a line-number-only row in `Phase_5`) |
| 2 | Ports L176 | the row is a care-note (a strait, not the city); removed from the Pre-Trip list |
| 3 | Calethina row (Phase 10) | trimmed to the Neumayer stage ("design work at Neumayer (Halley subnet, confirmed 2026-07-12)") **with a pointer to her full trajectory**: `TepenianUniverseTimeline/Worldspace/Characters/Dolls/Calethina/Personal_Background/Formative_History.md` L5 |
| 4 | Highways row 20 | the Temirötkel connector paragraph replaced by the one-location note |
| 5 | `16` §1 vs Half B | §1 (413,123 / 181,974 / 350,115 = 43.7 / 19.3 / 37.0) governs; quoted beside Half B in the three sheets |
| 6 | Spec | L79 means (July/August −25.3 / −24.6; December/January −4.7 / −4.1); L91 ~139 mm/yr; spec still 186 lines; the L94 rank left |
| 7 | Left | Ports L245 partial copy, `09` L160 demonym hit, the two Step 3 label mismatches, the dated note under the raw block, the timeline README flag |


---

## Sanay (done 2026-10-30)

Developer: *"yup, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Alias set | confirmed (SANAE IV, S.A.N.A.E. AWS / AYM00089004, Vesleskarvet, Port of Sanay, Sanay Corridor, Sanay Shipyard / Maritime Shipping Port, Sanaian); Ahlmannryggen and Queen Maud Land are places; Ports L424 added |
| 2 | Spec L78 | relabeled "Mean summer and winter temperatures" (the values are means); the sheet row follows |
| 3 | Port distance | the developer's 2026-09-01 ruling (~200 km) governs: `Ports.md` L760 "~200 km" (file length unchanged); L461–463 stay (the real station's figures) |
| 4 | Bedrock site | spec L88 "ICE SHEET (inland, around a bedrock nunatak)"; L94 "the snow around the rock is redistributed all the time, but the rock itself does not move"; spec still 202 lines |
| 5 | `16` §5 vs Half B | §5 (44.5 / 40.3 / 15.3 on 347,881, before `DR-68`) governs; quoted beside Half B in the three sheets |
| 6 | Division of Industry README | L111, L136, L155, L158, L195 added (Pre-Trip note and a line-numbers-only row in `Phase_7`) |
| 7 | Step 0 Census I status | the `DR-68` note added |
| 8 | Left | older composition tables, "~0%" probabilities, 817 vs 850 m, timeline README flag |


---

## Santa Luce (done 2026-10-30)

Developer: *"yup, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Research files C01 / C02 (R1, R2) | read-allowed at Step 3; registered in the Pre-Trip (Step 3 reads, §J corrected) and `Step_3.md`; the old picks stay withheld (`DR-67`) |
| 2 | Phase 5 Highways L120 row | one-location note |
| 3 | Spec L83 | "Aboa sits at 484 m" (spec 193 lines) |
| 4 | `City_Relationship_Database.md` L74 | states the Register founding; the "only dual-national founding" superlative gone (file 543 lines) |
| 5 | `16` §4 (held, not determined) | quoted beside Half B, labeled "held at current value, flagged for review"; counts before `DR-68`; three alternative readings noted |
| 6 | Precipitation text vs table | left; in "Recurring patterns" |
| 7 | Pass README | HANDOVER file added to the file table |
| 8 | Left | timeline README flag |
| 9 (shared) | Doll row, Phase 9 | 28 sheets: full path, 35 lines, Tier U sheet (`SH-029`) |
| 10 (shared) | `T8` Phase 2 line | 28 Pre-Trips now say 4 admissible rows (`SH-030`); not changed where the file has no section for the city |
| 11 (shared) | `09` row label | 30 Phase 4 sheets carry the old-B1 label (`SH-031`) |


---

## Troll (done 2026-10-30)

Developer: *"yup, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Alias set | confirmed (Troll Airfield, Troll Station, Troll Base, Troll Research Station, Jutulsessen); Queen Maud Land is a region |
| 2 | Spec L94 | "At −17 °C (the annual mean)"; rank dropped |
| 3 | Monthly table | spec L116 note extended. The check by script found the Avg Low below the Rec Low in **February through August** (not only March to August) and the **December Avg High above the Rec High**; both columns marked as estimates not to be cited; no numbers invented |
| 4 | `16` §6 vs Half B | §6 (provisional, Option A) quoted beside Half B in the three sheets; same shares, counts before `DR-68` |
| 5 | Megasheet folder count | "7 entries (6 files and 1 subfolder)" in the Pre-Trip (two places) and Phase 3 |
| 6 | Left | spec L78 vs the records, the peer count, Pre-Trip §I, timeline README flag |


---

## Utstein (done 2026-10-30) — the Halley subnet is complete

Developer: *"yup, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Climate file spelling | care-note in Pre-Trip §A and a pointer in §D Phase 1; the file is not renamed |
| 2 | `16` §7 vs Half B | §7 (43.7 / 14.1 / 42.3 on 861,033 before `DR-68`) governs; quoted beside Half B in the three sheets |
| 3 | Division of Industry README L197 | a line-number-only row in `Phase_7` |
| 4 | `16` L853 and L936 | kept in the lists |
| 5 | README titles | Utstein "(formerly Princess Elisabeth)"; Ariun Nuur "(formerly Vostok)"; renamed to "Ariun Nuur (formerly Vostok)" |
| 6 | Rename rows (six Pre-Trips) | the `Background-Lore/Cities/…` folders added as also keeping the old names (`SH-032`) |
| 7 | Pre-Trip §I | a dated note under the raw block |
| 8 | Left | spec peer comparisons, `Precipitation_Falls_vs_Lands.md` L127 placement, Airports L56 label, timeline README flag |


---

## Janbogo (done 2026-10-30)

Developer: *"yup, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Hit lists that mix in other cities' rows | each Pre-Trip row (census, Extent, `16`, `09`, `11`, Register) now names the city's own lines and says the rest are other cities' rows or district lines, not to be read |
| 2 | Earlier cold test run (Run 9) | the archive folder and the 77-line research log are **zero-intake test-run material**; a new run writes its own section and never reads the old content. **Pattern to apply to the same situation elsewhere** (Mawson's earlier warm run, Sanay's Run 11, Cape Adare's Runs 7–8): ask or apply this rule when each city comes up |
| 3 | Alias set | confirmed; Mount Melbourne, the Drygalski Ice Tongue, "Zukelli/Janbogo Airport" and Majyao are search aids; Terra Nova Bay and the Ross Sea noted as shared with Zukelli |
| 4 | Spec L65 | record low approximately −32 °C (July); record high approximately +11 °C (February); the sheet row follows |
| 5 | `16` §28 wording | kept |
| 6 | Left | peer lines (spec L77, L145, L151), month-average daylight column, Pre-Trip §I and §N |

## Cape Adare (done 2026-10-30)

Developer: *"If that's the case, then there's a possibility that we may need to flag Cape Adare for possible future renaming. Other than that, everything else as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Alias set | confirmed after checking each name against the spec: **Cape Adare, Adare Peninsula, Ridley Beach** are aliases. Adare Hallett (a proxy weather station ~113 km away), Cape Roget (the far end of the peninsula), Possession Island (the other proxy station's island), the Ross Sea and northern Victoria Land are places; St. Carsten / Borchgrevink is a person's name. This differs from the "add the four" recommendation: the recommendation was conditional on the spec check, and the check dropped two. Hits recorded in Pre-Trip §A (`16` L2736–2737 wraps across two lines) |
| 2 | **Possible future rename — FLAGGED** | recorded in Pre-Trip §A (rename row), the ledger and memory. A flag only: no ruling, no new name, no sweep. **The developer's "that" was read as the alias-set finding; the basis is not stated and is to be asked before the flag becomes a ruling** |
| 3 | "10 files" | correct as a total (4 notes + 6 map images; Antarctica empty); parenthetical added; `Phase_5` row 33 value cell now names the timeline repo's folder |
| 4 | Spec density tables | numbers left; dated note appended to spec L71 (census now 1,065,898; frame superseded at L83–98) |
| 5 | Spec temperature table | note at L192 extended: nine months with Avg Low below Rec Low, August Avg High above Rec High, two-station Rec column; no figures invented |
| 6 | St. Carsten's Landing (spec L281) | spec line left; sheets keep not carrying it; not added to `National_Holidays.md` before the holidays pass |
| 7 | Earlier test runs | Run 7 (cold, 17 files) and Run 8 (warm, 1 file) archives are zero-intake; neither wrote a research log (none exists) |
| 8 | Spine ranges and counts | meta lines corrected in 10 datasheets; `Step_0` row 30, `Step_3` row 1, `Step_10` §6.1 range; `Phase_3` "5 of 5" labeled as the 09-30 wording |
| 9 | Phase 7 row 41 | Census I 745,967 kept as `16` L163 stands, live 758,107 beside it |
| 10 | Two missing rows | the climate READER file is now named in `Phase_3`'s Climate row, the medical-institutes file in `Phase_7` row 48 (edited in place, no line added); both coverage headers now read 4 of 4 and 13 of 13; coverage check 0 gaps |
| 11 | Left | precipitation (recurring pattern), composition L426 (already records its own correction), shorthand citations, Pre-Trip §I |

Check: spec still 286 lines; verifier 0 FAIL (1 NOTE, `Step_7.md` L13, untouched); must-open coverage 0 gaps.

## Denison (done 2026-10-30)

Developer: *"In that case, there's a moderately decent chance that we may need to go through the cities and do full, more thorough researches for inspiration picks, similarly to the way we did for Relung Panen, Amundsen Station, and so on. Other than that, everything else as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Inspiration-places research | the partial first research file (48 lines) and the `inputs` file (9 lines) read-allowed at Step 3; the `candidates` file withheld (it names Mirny and Concordia). **Developer note: a full, more thorough inspiration-pick research pass over the cities (as for Relung Panen and Amundsen Station) may be needed. A possibility, not a ruling — in the Weekly To-Do** |
| 2 | Alias set | Denison, Cape Denison, "Home of the Blizzard"; Mackellar, Boat Harbor and the Mawson names are search aids, not aliases; proxy-spelling care-note added |
| 3 | Extent block | spec L20 and census L498 labeled a 2026-09-05 snapshot with the live total beside it; zones not re-split |
| 4 | Wind | canon 19.3 m/s (~69 km/h) measured; changed in the spec (L8, L165), Ports L194, `16` L2639, `04` L414 and the `Step_-1` header quote; Ports L562 (a Guinness quotation) left |
| 5 | Retention | spec L344, census L619 and L787 updated to the live rows; L787's other older figures dated, not replaced |
| 6 | Gateway-port facts | added to `Phase_5`; 2,697 vs 2,698 km is coordinate rounding |
| 7 | Composition file | UTC+9 → UTC+10; "~3,400km via Hobart" → "~2,700km" |
| 8 | `16` L2616 | spec cite L97 → L316 |
| 9 | Spec odds and ends | L178 reworded (George V Land / Adélie Land); L21 stray backtick removed |
| 10 | Sheet gaps | rows added: timeline Locations (`Step_1_and_2`, `Phase_5`), climate file (`Phase_3`), `16` Half B and national economy (`Phase_4`), Geothermal (`Phase_5`), Characters trees (`Phase_10`); `Phase_9` Doll row now cites its Tier U sheet; coverage headers 4/4, 7/7, 3/6 (the three relationship files stay deferred by design), 6/6, 3/3 |
| 11 | Left | cape-only density section, spec L158, peer lines (L204, L47–49, L98, L167, L186–187, L279, L291), census held-row arithmetic note, Pre-Trip §I |

Check: spec still 361 lines; Ports 881, composition 1,299 and the other source files unchanged in length; verifier 0 FAIL (1 NOTE, two later-era-word lines to read); must-open coverage 0 gaps.

## Dumont d'Urville (done 2026-10-30)

Developer: *"yup, all as recommended."* (New name still not chosen; every fix is written against the current name; no sweep.)

| # | Item | Done |
|---|---|---|
| 1 | Rename wording | Pre-Trip §A "No rename flagged" → RENAME PENDING (ruling 2026-10-13), wider search words (hits at spec L166 and L255) |
| 2 | Research files | first file (174 lines) and `inputs` (9 lines) read-allowed at Step 3; `candidates` withheld (names Mirny); registered in the Pre-Trip and `Step_3.md`; underscore spelling added |
| 3 | Alias set | Dumont d'Urville, Station, D10 Skiway, DdU, Petrel Island / Île des Pétrels; Géologie Archipelago and Adélie Land are places |
| 4 | Care-notes | "Dumont Coast Highway" is the road; `Station_to_City_Map.md` recorded as not an input |
| 5 | Spec temperature lines | L95–96 aligned to the table (about −17 °C coldest-month mean; record low about −37 °C Aug; record high about +11 °C Dec) |
| 6 | Polar night | spec L145 reworded to L111–113 |
| 7 | Precipitation column | left (recurring pattern: monthly column 404 mm vs about 655 mm annual) |
| 8 | Population table note | spec L56: "its order within the tier" |
| 9 | Pre-trim population | labeled, not recomputed: `09` L60, `16` L279, `16` §24, `Phase_7` row 1 (live workforce 307,404) |
| 10 | Phase 5 facts | gateway-port rows, extent rows (2026-09-05 snapshot), Geothermal zero-hits row added |
| 11 | Sheet gaps | `Phase_7`: seven rows added (all zero hits), known-missing box closed, header 13 of 13; `Phase_3` climate file row (4 of 4); `Phase_4` national-economy row (7 of 7); `Phase_5` 6 of 6; Register line cites (L71, L90, L94); two later-era entries in `Step_-1` |
| 12 | Left | peer lines (L83, L108, L110, L81, L207), France Significant (GPS-consistent), Pre-Trip §I |

Check: spec still 255 lines; `09` 272 and `16` 3,578 lines unchanged in length; verifier 0 FAIL (2 NOTEs: later-era words to read, inference markers).

## Fort McMurdo (done 2026-10-30)

Developer: *"yup, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Alias set | Fort McMurdo and McMurdo Station; Scott is a different place (nothing swept under it); Hut Point, Hut Point Peninsula (shared with Scott) and Winter Quarters Bay are search aids; Erebus, McMurdo Sound, the Dry Valleys, Cape Evans, Cape Royds, Ross Island and the Ross Sea are places; extra name hits kept |
| 2 | Geothermal heating file | named Phase 3 input, own-lines only (the lines pairing the city with Scott are relation, not compared) |
| 3 | Temperature lines | spec L92–93 aligned to the table (coldest months mean about −25 °C, night low −28 to −29; warmest month December about −3 °C; record low about −51 °C July; record high about +11 °C December) |
| 4 | Polar night | spec L141, L148 → ~116 days |
| 5 | "Island cap" tag | removed from spec L15–16 and census L507 / L627; the extent file says it is a label, not a cap |
| 6 | Factions file's single-city section | stays unopened (factions are created after all three methods); box corrected |
| 7 | Half B vs the city's own section | agree; no shares quoted beside Half B |
| 8 | Sheet gaps | rows added: climate file and geothermal (`Phase_3`, 4 of 4), national economy (`Phase_4`, 7 of 7), timeline Locations (`Phase_5`, 6 of 6), five `Phase_7` rows (13 of 13); in `08` and the staffing README the "McMurdo" hits are the REAL station (a staffing anchor and a CRREL source), recorded as not the city |
| 9 | Left | Census II robots residual (164,620 vs 164,621), the daylight-column rounding, the Cradle line, the peer-ranking lines, README (already corrected) |

Check: spec still 246 lines (`wc -l`); census 810 lines; verifier 0 FAIL (1 NOTE).

## Scott (done 2026-10-30)

Developer: *"yup, all as recommended."*

| # | Item | Done |
|---|---|---|
| 1 | Alias set | Scott and Scott Base; Fort McMurdo is a different place; Hut Point, Hut Point Peninsula (shared) and St. Robert are search aids; the Enfolded is a robot religion, not a name; Erebus and Ross Island are places; "Amundsen-Scott" exclusion widened to the en-dash form |
| 2 | Geothermal heating file | named Phase 3 input, own-lines only |
| 3 | Record extremes (spec L94) | aligned to the table: +10 °C (Nov), −51 °C (Jul) |
| 4 | Gap sentence (spec L86) | "4.7 °C in May and 4.3 °C in August" |
| 5 | "Founding wave" annotation | moved from Australia to New Zealand (spec L43–44, census L295–296, sheet rows); census L298 note added to `Phase_2` |
| 6 | `16` L3540 | "St. Richard (Scott)" → "St. Robert (Scott)" |
| 7 | Comparison clause in `Step_1_and_2` row 24 | trimmed in the sheet, marked as not carried; spec line stays |
| 8 | `Step_6` header-line column | ten numbers updated to the live L48 … L160 |
| 9 | Sheet gaps | rows added: climate file and geothermal (`Phase_3`, 4 of 4), national economy (`Phase_4`, 7 of 7), timeline Locations (`Phase_5`, 6 of 6), five `Phase_7` rows with zero hits (13 of 13) |
| 10 | Left | census residuals, repeated −4.4 °C Rec High (flagged for an NCEI check), peer lines, daylight-column rounding, `16` §30 one-worker rounding, Pre-Trip §I |

Check: spec still 229 lines (`wc -l`); census 810 and `16` 3,578 unchanged in length; verifier 0 FAIL (1 NOTE).

**That completes the Janbogo subnet's walk-through.**
