# Casey — manual input audit (2026-10-29)

Method: `README.md` in this folder. Everything below was read by hand: the whole Pre-Trip sheet (564 lines), all 19 datasheets (about 600 lines), the ledger and README, the city's spec, and every cited source line was opened and compared. **Nothing was edited.** Paths are shortened: `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`, `ULM` = `Worldspace/Locations-and-Levels/Universal_Location_Methodology`.

**Verdict in two lines.** **(1) Access:** every file the Casey pass needs exists, is the right file, and is listed with a correct tier; the Pre-Trip's per-file *line numbers* are stale for eight shared files (edited after the sheet was built), and a handful of Casey-relevant files and aliases are not registered. **Nothing blocks a run.** **(2) Accuracy:** most rows are transcribed correctly, but **several values are out of date after the 2026-10-28 census change** (`DR-68`/`DR-69`), several citations point at the wrong line, and a few rows carry text the cited line does not hold. Fix list at the end.

Severity words: `BLOCKS` · `WRONG` · `STALE` · `GAP` · `NOTE` (see README).

---

## PART 1 — CAN THE ULM REACH EVERYTHING IT NEEDS?

### 1a. What was checked and is right
| Check | Result |
|---|---|
| All 19 datasheet files named in the Pre-Trip exist (`Datasheets/`), plus README and ledger | ✅ 19 of 19 |
| Spec path `CITIES/Specs/Mirny subnet/Casey.md` (note: **space**, not underscore, in the spec folder) | ✅ exists, 221 lines |
| Census rows: Section A heading L380, tier table L382–386, Census I row **L485**, Census II row **L608** | ✅ all four land on Casey's own lines; figures match the spec exactly (745,935 / 773,714 / 1,519,649 and 445,030 / 612,848 / 1,057,878) |
| Founding Register row L58 | ✅ Casey · Mirny · +7 · Australia |
| `READER/Casey.md` (climate) is keyed by the city's own name and holds the same twelve monthly means and −9.3 °C annual mean as the spec table | ✅ |
| Stations file L18, L68 · `National_Medical_and_Care_Institutes.md` L225 · `City_and_District_Research_Topics.md` L252 · `Precipitation_Falls_vs_Lands.md` L158 · `11_Caloric_Rebuild…` L333 · spec L170 (`## Notable Locations`), L179 (`## Notable Figures`), L181–182 (the two placeholder names) | ✅ each opened; each names Casey |
| `Division_of_Industry_Sweep_2026-08-31.md` L163 (Casey 6/6) and L214–218 | ✅ |
| Concept-art folder `City_Concept-Art/Mirny_Subnet/Casey/` holds only `.gitkeep` | ✅ (an empty result, correctly recorded) |
| Megasheet folder `City_Megasheets/Mirny_Subnet/Casey/` is withheld and recorded, not opened | ✅ (6 files + 1 subfolder; the sheet says "7 files": `NOTE`) |
| Local culture, robot culture and Enneagram files exist and are tiered read-last | ✅ |
| All 12 runbook step ranges, all 11 spine phase ranges, 7 of the law lines, and the 12 step cards and 17 gate cards | ✅ against the live headings (shared; see `TRACKER.md` cross-city list for the exceptions) |

### 1b. Findings
| ID | Sev | Finding | Evidence | Proposed fix |
|---|---|---|---|---|
| **A-01** | STALE | **Pre-Trip cites file `16_Per_City_Three_Tier_Run.md` at the old line numbers.** Casey's Half B row is now **L267** (sheet: L266, which is now Juan Carlos's row); the 13 other mentions moved +3 to +5. The file gained 5 lines on 2026-10-29 (Relung Panen row and note). | live `grep` of the file: Casey at L267, 441, 2145, 2154, 2203, 2206, 2210, 2222, 2224, 2228, 2247, 2428, 2804, 3484; sheet lists 266, 438, 2140, 2149, 2198, 2201, 2205, 2217, 2219, 2223, 2242, 2423, 2799, 3479 | Re-point (E, Phase 1 row, Phase 4 row) |
| **A-02** | STALE | `09_Per_City_Baseline_Run.md`: sheet L87, L103, L148, L210, L252 | live: L87 (same), **L105, L150, L212, L254** (+2 after Relung Panen row added) | Re-point |
| **A-03** | STALE | `Airports.md`: sheet L47, L51 | live **L50, L54**; also names Casey at **L12** (Mirny onward-flight note, `DR-82`), L3, L21–23, L104 | Re-point; add L12 |
| **A-04** | STALE | `Ports.md`: sheet L538, L710 | live **L561, L733** (+23); also new **L298, L300** (§3e, `DR-82`: mentions Casey as the one door for Relung Panen's people) | Re-point; add L298, L300 |
| **A-05** | GAP | **`Highways.md`: the Relung Panen Spur is not registered.** Sheet lists L90, L199, L204 only. The file also names Casey at **L207, L274, L276, L278, L291**: the dedicated spur from Relung Panen joins Hwy 110 *at Casey* (added 2026-10-21, the day the sheet was refreshed). | opened L204–207 and L274–291 | Add the five lines |
| **A-06** | STALE | `City_Relationship_Database.md`: sheet L21, L28, L49, L152–153, L169–170, L203, L329, L501 | live: L21, L28, L49 (same); the later ones moved **+11** (now L163–164, L180–181, L214, L340, L512); new mentions L116, L117 (Relung Panen entry), L169. Casey's own entry is now **L163–170** | Re-point |
| **A-07** | STALE | `City_National_Connections.md`: sheet L274, L290, L297, L300, L306, L419, L435, L464 | live: L274, 290, 297, 300 (same); L306→**307**; L419, 435, 464→**424, 440, 469**; new **L301** (Casey–Relung Panen link) and **L397** | Re-point; add L301, L397 |
| **A-08** | GAP | `City_Cross_Subnet_Relationships.md` L207 names Casey; the sheet lists only L42, L54, L94, L99, L128 (the Phase 5 datasheet row does list L207) | opened | Add L207 |
| **A-09** | NOTE | **`Extent_and_Density_Per_City.md` row L608 (Casey) shows 1,495,731, the 2026-09-05 population** (required area 150 / 214 km²); the census now says 1,519,649 (→ 152 / 217). **This is by design:** the note at L631 says the table "records the 2026-09-05 populations … left as the dated record; the census is the live source." The Pre-Trip cites the row as Casey's extent record without saying it is a dated snapshot. | row L608 and note L631 opened | Add "(2026-09-05 snapshot; census is live)" beside the citation in Step 0 and the Pre-Trip, so a reader does not take the mismatch for an error |
| **A-10** | GAP | **The composition file (`CITIES/Upper_Earth_Immigration_Composition.md`) is not registered at Phase 2** (nor in the Phase 2 datasheet). Casey's own section is **L569–575**; its tiers match the spec exactly. The solar-UTC rule is at L28. | opened L569–575 | Add a Phase 2 row (already done by hand for Santa Luce and Relung Panen; the builder does not add it for any city) |
| **A-11** | GAP | **Casey-named research files are not registered or classified:** `Research_Logs/Casey_Inspiration_Place_Research_R1.md`, `…_R2.md`, `Casey_Mirny_Airport_Comparison/Geology_Research/Operations_Research/Research_BRIEFS_2026-10-29.md`, and `Relung_Panen_Port_Research_2026-10-25_C_Casey_to_Bunger_Hills_Terrain.md`. The Pre-Trip says the research log does not exist (true: `Casey_Research_Log.md`) and says nothing of these. | `ls Research_Logs | grep -i casey` | Register them (tier to be decided by the developer: Relung Panen's sheet marks its Casey/Mirny airport files WITHHELD) |
| **A-12** | GAP | **Alias set is missing three names the city is keyed under elsewhere:** **Windmill Islands**, **Bailey Peninsula**, **Newcomb Bay** (Ports L561; Extent row L608; `16` L2185). The recipe says the sweep is only as wide as the alias set. | opened those lines | Add to §A |
| **A-13** | WRONG | Shared line citations in the Pre-Trip that are wrong or loose (same in every city's sheet): "No invented person names" cited at spine **L127** (that line is the applicability table; the rule is at spine L220, L1114, L1140); divergence operator at runbook **L2178** (the operator heading is L2180); Step 5's "`02` §5.3 lines 610–684" (§5.3 ends at L636); Round 3's "section 5 … lines 701–703" (the fifth section is at trial-recipe L682–684; L701–703 is a correction box); Step 10's range **3057–3172** (Step 10 ends at L3152; L3153+ is the file index) and, in the same bullet, the card note "live lines 3045–3161". | each line opened against the live file | Recorded once in `TRACKER.md`; fix in the builder + each sheet |
| **A-14** | NOTE | README (`Casey/README.md`) lists `City_Vision_Notes/Casey.md` under "existing sources"; the Pre-Trip and `DR-10` say the folder is struck from every step. | README opened | Reword the README row |
| **A-15** | NOTE | The Pre-Trip is **WARM**. `06_Worked_Example_Provenance.md` has a Casey entry saying a *cold* pass must skip **Casey's own section of file `16`** ("conclusion-tier, the heaviest entry") — yet the sheet and the Phase 7 datasheet read exactly that section and tell the reader not to skip it. This is consistent **only because the run is warm**. If Casey is ever run cold, both must be redone. | `06` L292–332 | Developer decision: confirm WARM |

### 1c. Required inputs (`ULM_Input_Required_Reference.md`) — Casey
T0-1 spec ✅ · T0-2 position (`Geographic Basis`, coordinates) ✅ · T0-3 census ✅ · T0-4 parent ✅ · T1-G1 symbol pair: an entry exists in `City_Symbol_Assignments.md` (count only; not opened, per `DR-8`) ✅ · G2 climate block, reader file, precipitation reference ✅ · G3 `16` Half B row + non-stub Economy text (the spec's Economy section is "TBD"; the figures come from `16`) ✅ · G4 Register row + `**Founding population:**` ✅ · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G7 three picks with tiers ✅ · G8 census tier table + composition file ✅ (but see A-10) · T2-8 extent row exists ✅ (stale: A-09). **Nothing is missing that blocks Tier 0 or Tier 1.**

---

## PART 2 — IS EVERY PIECE OF INFORMATION RIGHT?

### 2a. The spec (primary source), read in full
Checked right: the 13-nation share column sums to **100.00%**; all four count columns sum **exactly** to the census totals (773,714 · 745,935 · 612,848 · 445,030); the monthly means average to the stated −9.3 °C; the monthly precipitation sums to the stated **225.1 mm**; the coordinates match the real station (66°16′54″S 110°31′36″E); the midnight-sun span Dec 11–Jan 2 is 23 days.

| ID | Sev | Source-level finding (the spec itself) | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **L67 "Temperature range: coldest months (July/August) avg −16 °C; warmest month (January) avg +1 °C"** contradicts the spec's own table (July −14.7, August −14.9, January mean −0.3). Looks like the pre-2026-09-04 estimate that the climate correction left behind. | table L109–110, L103 |
| **S-02** | WRONG | **Daylight prose contradicts the table and the latitude.** Prose: winter solstice "approximately **5–6 hours**" (L51, L96, L108 note, L127, L132), summer "18–19 hours" (L51, L97). Table: June **2.7 h**, July 4.0 h, December **24 h**; L84 says the sun does not set Dec 11–Jan 2. DERIVED check: at 66.27°S on June 21 with refraction the day is about 2.5 h. | table L101–114; L84 |
| **S-03** | WRONG | **"shortest Australia-to-Antarctica route of any Tepenian city"** (spec L20; census L385; composition file L573) contradicts `Ports.md` L193–196: Dumont d'Urville **2,682 km**, Denison **2,697 km**, Cape Adare **3,398 km** are all closer to Hobart than Casey (**3,423 km**). | `Ports.md` table |
| **S-04** | NOTE | `16` §21 (Casey's section) carries the pre-`DR-68` worker counts: 436,698 + 207,641 + 484,495 = **1,128,834**. The same file's Half B row (L267) and `09` L87 now say **1,146,682**. **Labelled, not an error:** the file's title line (L1) says the per-city determinations "were NOT recomputed" after the 2026-10-28 refresh of Half B. The percentages (38.7 / 18.4 / 42.9) did not change. The Phase 7 datasheet carries the §21 counts with no such caveat (D-23). | `16` L1, L2185–2190 vs L267 |
| **S-05** | NOTE | Pink Lucy character files (universe repo, `Characters/Dolls/TBN [FW-25 Pink Lucy]/`) disagree with each other: README L44 and `Formative_History.md` L3 say her route was resolved to Janbogo, "not to Casey"; **`Conflict_Experiences.md` L3 and `Timeline.md` L13 still say "Janbogo, or Casey — route undetermined"**. README L44 also says Casey "was destroyed early in the war as a targeted strategic chokepoint", while the Casey spec says the timing is TBD. (The timeline repo takes no worldbuilding edits; this is a flag only.) | opened |
| **S-06** | NOTE | `National_Medical_and_Care_Institutes.md` L225 calls Casey a "subnet hub"; `City_Relationship_Database.md` **L49** (first written L47, the Halley row; corrected 2026-10-30) names **Mirny** as the Mirny subnet's hub and Casey a member. The Phase 4 datasheet already flags the tension. | opened |
| **S-07** | NOTE | COMNAP catalogue p. 28 gives Casey mean annual temperature **−5.9 °C** (Feb −0.1, Jul −10.5); the READER 1991–2020 normal used everywhere is −9.3 °C (Feb −2.7, Jul −14.7). The datasheets cite only the catalogue's page numbers, so no wrong figure is carried; noted so nobody "corrects" the spec to COMNAP. | PDF pp. 8, 23 opened |
| **S-08** | NOTE | Spec L80 says "28 of the 37 Tepenian cities are colder"; the corpus is 38 cities and the sentence is a cross-city comparison (the Step 1 datasheet correctly does not carry it). | L80 |

### 2b. Datasheet rows, file by file
(✅ = value and citation match the live source; every cited line was opened.)

| File | Rows | Result |
|---|---|---|
| `Step_-1` | 11 | ✅ except **D-01** and **D-02** below |
| `Step_0` | 10 | ✅ values; retention figures recomputed by hand: 69.613% · 59.661% · 79.209% · 19.55 pp ✅; Tier U rows ✅ against `Second_Interwar_Period_Quick_Reference.md` (read in full); **D-03** |
| `Step_1_and_2` | 22 | ✅ climate, extremes, winds, precipitation, polar night, Stations L18/L68, COMNAP pp. 8 and 23 (both name Casey), picks, Register; ❌ **D-04, D-05, D-06, D-07** |
| `Step_3` | 3 | ✅ picks L70–73 (Flagstaff PRIMARY; Memphis and Reno SECONDARY, annotations match) ❌ **D-08** |
| `Step_5` | stub | ✅ both read-last files exist; nothing staged (correct) |
| `Step_6`–`Step_9` | Tier U | ✅ the ten section headers of the differentiation table match the live file (L44–L153); gate and panel indexes: **pending the Tier U audit** (shared) |
| `Step_10` | 6 + notes | ❌ **D-09** |
| `Phase_2` | 12 | ✅ tiers, share percentages, Census rows; ❌ **D-10, D-11, D-12** |
| `Phase_3` | 10 | ✅ eight quotes match L51/L53/L55/L57/L125/L126/L127/L158/L174; ❌ **D-13, D-14** |
| `Phase_4` | 7 | ✅ `09` L87 values (and 387,716 ÷ 1,146,682 = 33.8%), `11` L333, `NMCI` L217–225 content; ❌ **D-15, D-16** |
| `Phase_5` | 11 | ✅ Hwy 2 and Hwy 110 route lines, Airports L12/L50/L54, Cross-Subnet lines; ❌ **D-17 to D-20** |
| `Phase_6` | 6 | ✅ every zero-hit claim re-run and true; ❌ **D-21, D-22** |
| `Phase_7` | 11 | ✅ every figure matches the source text of `16` §21; ❌ **D-23, D-24** |
| `Phase_8` | 4 | ✅ spec hit counts (music only at L158; cuisine, dress, craft none), zero-hit claims, placeholders L181–182 |
| `Phase_9` | 6 | ✅ zero-hit claims, Doll categories (35 lines); ❌ **D-25** |
| `Phase_10` | 5 | ✅ Enneagram index 35 lines/0 hits, four files name Casey; ❌ **D-26** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Proposed fix |
|---|---|---|---|---|
| **D-01** | WRONG | Step_-1 · "Specs Status field" | Cites `00_RUNBOOK.md` **L1821–1822** as the rule that `Status:` is never an input. Those lines are about the city symbol rule. The rule is at **L1854–1855** (§C.8a). | Re-point |
| **D-02** | NOTE | Step_-1 · "Specs file length" | "222 lines"; `wc -l` gives 221. (All "N-line file" counts in the sheets are one higher than `wc -l`, e.g. 378 vs 377, 293 vs 292.) | Decide one convention |
| **D-03** | NOTE | Step_0, Phase_2 · Census I | Tag "(revised 2026-07-04)" only; the live row also carries the `DR-68` revision of 2026-10-28. Values are correct. | Add the second tag |
| **D-04** | WRONG | Step_1_and_2 · `16` Half B row | **Workforce 1,128,834 → live 1,146,682**; line **L266 → L267**. (Percentages and D are right.) | Correct value and line |
| **D-05** | GAP | Step_1_and_2 | The climate reader file is never named as an address; the sheet's "6 of 6" coverage count was satisfied by the spec's name (`Casey.md`). | Add a READER row |
| **D-06** | NOTE | Step_1_and_2 · Founding | "built by the Australian Antarctic Division" is not in the cited L142 (L166 says only that the Division "operated specialized equipment at the real Casey Station"). | Add L166 or drop the clause |
| **D-07** | NOTE | Step_1_and_2 · Register row | No line number (L58). | Add |
| **D-08** | NOTE | Step_3 · research log | "`Research_Logs/` has no Casey file" is true only for `Casey_Research_Log.md`; six Casey-named files now exist (A-11). | Reword |
| **D-09** | STALE | Step_10 · provenance | Says `06_Worked_Example_Provenance.md` is 406 lines with Casey hits at L291–314 and six rows. Live: **431 lines**, Casey section **L292–332**, a **seventh row** (Casey's own section of `16`, "skip the whole section") and an "orchestrator exposure" note. Also **the coordinate "`01` §1 line 65" is wrong in both places:** the evaluative `Resettled` row is at `01` **L137** (L65 is a LAW 0 paragraph); the line moved on 2026-09-03 and the "skip line 65" instruction has pointed at the wrong line ever since. | Fix in `06` and in this row (this one matters if Casey is ever run cold) |
| **D-10** | **WRONG** | Phase_2 · per-nation full figures | **All 52 per-nation counts are the pre-`DR-68` values** (e.g. USA 167,347R/161,166H vs spec L31 169,934/163,832; China 145,243/139,878 vs 147,488/142,192). The percentages are right. The old robot counts add up to the old total (about 761,936). | Replace with spec L31–43 |
| **D-11** | **WRONG** | Phase_2 · Retention | **69.67% / 59.54% / 79.42% / 19.87 pp** are the old-census figures, and the sheet says "computed from the two rows above" and "cross-ref Step_0" — Step_0 (and the rows above) give **69.61 / 59.66 / 79.21 / 19.55**. | Recompute |
| **D-12** | NOTE | Phase_2 · annotation rows | The tier-table parenthetical is shown in backticks as "(founding wave — on a short, direct sea route from Australia)"; the source reads "…shortest Australia-to-Antarctica route of any Tepenian city" (see S-03). The reword is not marked. | Mark as "[comparison not carried]" like the other rows do |
| **D-13** | GAP | Phase_3 · research folder | "none exists for Casey" — `Research_Logs/Casey_Mirny_Airport_Geology_Research_2026-10-29.md` now is Casey's geology research (the spine's Davis-style research item). | Register (A-11) |
| **D-14** | NOTE | Phase_3 · L127 quote | The quote carries "approximately 5 hours" (spec error S-02) and a comparison class ("cities further south … further north"). | Hold until S-02 is settled |
| **D-15** | WRONG | Phase_4 · `16` cross-check | "Workforce matches exactly (1,128,834 / 1,128,834)" — wrong, and contradicts the sheet's own row above it (1,146,682). Line L266 → L267. | Correct |
| **D-16** | NOTE | Phase_4 · NMCI | Range L217–225 omits the header line (L214) that the row quotes; "non-hub" is from RelDB L49 (first written L47; corrected 2026-10-30), not the spec. | Add L214, L49 |
| **D-17** | GAP | Phase_5 · Highways | Omits the Relung Panen spur (Highways L204, L207, L274–278, L291). | Add (A-05) |
| **D-18** | STALE | Phase_5 · RelDB rows | Cites **L152–160 and L160**; Casey's entry is now **L163–170**. The row says three highway neighbors; the live entry has **four** (Relung Panen, west, via the spur). | Re-point, add the fourth |
| **D-19** | STALE | Phase_5 · National Connections | Cites L285–286, L289–290, L291–293; the links are now **L291–292, L296–297, L298–300**. Omits the new **L301** (Relung Panen, "everything that reaches or leaves that city by land passes through Casey"). | Re-point, add |
| **D-20** | STALE | Phase_5 · Port | Ports **L537, L709 → L561, L733**; the quote lost its dash ("Vincennes Bay itself a V-shaped inlet"); the Hobart distance rows (L196, 3,423 km, "direct, seasonal") and L189 and L298–300 are not transcribed. | Re-point, restore dash, add rows |
| **D-21** | NOTE | Phase_6 · roster | "the real 2-religion, 6-file roster (file count re-verified: 6)" is **correct as to files** (Polydimensional Animism 5 files + Cymatics Reverence 1 = 6), **but the roster folder lists six names**: four more (God-mind universe simulation, Ice-Cold Buddhism, Sylvester James Gates Adinkras, The Eyes of Gold) exist as **empty folders**. The roster is "OPEN"; saying "2-religion" hides that four more are named. The zero-hit result is true. *(Corrected 2026-10-29: this row first read "wrong"; the folder was re-listed with its contents.)* | Say "6 files across 2 developed religions; 4 further roster folders are empty" |
| **D-22** | NOTE | Phase_6 · line counts | 378 / 293 vs 377 / 292 (see D-02). | — |
| **D-23** | STALE | Phase_7 · every `16` citation | All shifted by **+5** (L2180–2185 → L2185–2190; L2201–2203 → L2206–2208; L2217–2224 → L2222–2229; L2230–2231 → L2235–2236; L2235–2243 → L2240–2248). The values match the source text; the source labels those counts as not recomputed (S-04), but the sheet does not say so, and it sits beside Step 1's refreshed workforce of 1,146,682. | Re-point; add a line "§21 counts are the 2026-09-02 figures (file 16 L1)" |
| **D-24** | WRONG | Phase_7 · MUST-OPEN | The sheet says in a box that it covers "~5 of the spine's 13" and lists eight items as known-missing, and then states "**13 of 13** addresses are named". The count was satisfied by the names in the known-missing list. | Make the two agree |
| **D-25** | **WRONG** | Phase_9 · robots share | "**50.94%** of Casey's Census I (773,714 of 1,519,649 = 50.91…%)": the figure in front is the old census's; the right figure is **50.91%**. | Correct |
| **D-26** | WRONG | Phase_10 · Pink Lucy | "same finding in all four" is false (two files say the route is undetermined, S-05). The row also quotes a characterization of the city ("comparatively muted and function-oriented") taken from a character file — a conclusion inside a value-and-citation sheet (Field Guide Rule 1b). | Reword; drop the characterization |

*Added after the Relung Panen audit (same checks re-run on Casey's sheets):*

| ID | Sev | File · row | Finding | Proposed fix |
|---|---|---|---|---|
| **D-28** | NOTE | `Step_6.md` · table section 1 | Lists "Shape · Deficit address · Pass"; the live differentiation table's section 1 header (L48) reads "City · **Subnet** · Shape · Deficit address · Pass". The other nine sections match the live headers. | Add "Subnet" |
| **D-29** | STALE | `Step_9.md` | Lacks the runbook's Step 9 **item 5** ("discharge every deferral to the pass's close", added 2026-10-21, `M-291`; runbook Step 9 section). Relung Panen's rebuilt sheet carries it. | Add the item-5 paragraph |
| **D-27** | NOTE | `Phase_9.md` · Doll Representation row | (as in the ledger) cites only "`Doll_Representation_Categories.md`, 35 lines"; no path. The Laws of Robotics row cites `Robot_Physiology_Quick_Reference.md`, whose headings do not include the Laws (to be confirmed in the Tier U audit). | Cite full paths |

### 2d. Rows that rest on the shared Tier U sheets
Rows that cite `Corpus_Reference_Sheets/…` (Second Interwar ✅ checked; Falkland Treaty, No National Stereotypes, Robot Physiology, Doll Categories, DoI Reliability, QA Gates, Review Panel, Steps 9 and 10, Differentiation, Zodiac) are **verified once in the shared Tier U audit** (`TRACKER.md`), not per city. One open question already: Phase_9 cites `Robot_Physiology_Quick_Reference.md` for the Laws of Robotics text, and the sheet has no heading for it (to confirm).

---

## What I would change first (for the developer to approve)
1. **Values now wrong after the census change:** D-04, D-10, D-11, D-15, D-25.
2. **Citations to re-point:** the eight stale shared files (A-01 to A-08), D-01, D-18 to D-20, D-23 (the remap tool does the numbers; the new mentions need adding by hand).
3. **Add what is missing:** the Relung Panen spur (A-05, D-17, D-19), the composition-file row (A-10), the Casey-named research files (A-11), three aliases (A-12), a climate-reader row (D-05).
4. **Source fixes for the developer:** S-01, S-02, S-03, S-05.
