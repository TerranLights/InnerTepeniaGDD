# Mirny repass, unit U0: data recheck (2026-11-04)

**What this is.** The mechanical recheck of everything Mirny's Pre-Trip, datasheets and pass absorbed, against the sources as they stand now. No re-derivation. Run 2026-11-04, 05:20 to 05:24 (system clock), by the Mirny repass cron (first firing). Nothing was edited and nothing was committed. Pass files are untouched (`DR-74`).

**Runbook:** read in full this session, 2026-11-04, starting 05:20 (all 3,179 lines, in chunks).

**Result in one line.** Six tools clean (0 FAIL, 0 GAP). Every census, composition, retention, workforce, language, highway, port and airport figure the sheets carry is current. **Four wording or arithmetic drifts found, all in datasheets or in the spec; none changes a pass finding.** One new fact sits next to Mirny (Winter Intake Airport island, 92 km from Mirny) and is for the piece that reaches Phase 5.

---

## 1. The six checks (raw output pasted in section 5)

| Check | Result |
|---|---|
| `verify_city_sheets.py Mirny` | 20 checks, 0 FAIL, 2 NOTE (D7 later-era words: Step_7 L15, Phase_3 L16, Phase_5 L39, L43 to read; D8 inference marker: Step_-1 L24 to read). Both NOTEs are "read, never strip". P6: 228 claims, 0 failed |
| `audit_city_inputs.py --city Mirny` | tests 40, GAP 0, note 2 |
| `check_must_open_coverage.py --city Mirny` | TOTAL gaps 0 |
| `check_founders_against_register.py --city Mirny` | founder disagreements 0, heritage wording 0, 1,835 files scanned |
| `handoff_audit.py <Mirny folder>` | instrument valid; phases with rows addressed to them and no enumeration: 0 |
| `phase_discipline_check.py <Mirny folder>` | 9 of 9 phases carry the shed marker; ledger blanks listed in section 5; late Lover-faculty marker absent (Step 8 not yet re-run, expected) |
| `git diff 8777bb5f..HEAD` | empty: HEAD is 8777bb5f. No source changed since the handoff. Working tree changes are the four files of the handoff session only (handoff, decisions file, repass queue, perk file), none of them a Mirny input |

---

## 2. Confirmed current (figure by figure)

| Item | Sheet says | Live source | Verdict |
|---|---|---|---|
| Census I | 692,971 H / 710,578 R / 1,403,549 | `Official_Population_Census.md` L500; `Specs/Mirny subnet/Mirny.md` L15 | **current** |
| Census II | 524,022 H / 528,352 R / 1,052,374 | census L642; spec L16 | **current** |
| Retention | 74.98% combined, 75.62% human, 74.36% robot, 1.89 pp | recomputed here: 0.74979, 0.75620, 0.74355 | **current** |
| Composition tier table | 6 primary, 11 significant, 19 notable (36 stocks) | spec L18 to L22 and census L372 to L376, identical | **current** |
| `(founding wave)` on Idelsk-Uralia | tag = Register founder | spec L20 to L22, census L374 to L376 | **current** |
| Per-nation table | sums to the census | rows L32 to L67 summed: Census I robots 710,578, humans 692,971; Census II robots 528,352, humans 524,022; shares add to 99.977% | **current** (the sheet's row count is wrong, see drift 4) |
| Language row | English alone as the supporting tier, largest group 25.2 to 34.4 | `Language_Sets_By_City_Reference_2026-11-03.md` L32 | **current** |
| Workforce | 1,057,064 (`16` Half B row L276, header L247; `09` L71) | live | **current** |
| Division of Industry splits | Half B 42.2 / 11.6 / 46.2; Mirny's own section (`16` section 20) 42.2 / 23.1 / 34.7; counts 446,228 / 244,334 / 366,502; distinctive tier 610,836 (57.8%) | live, and the sheet (Phase_7 L50 to L51) states the difference itself | **current** |
| `09` row | difficulty 1.25, humans 692,971, residents 1,403,549, required 376,393, workforce 1,057,064, 35.6% | `09` L71 | **current** |
| Extent table row | 1,403,549 people; 140 km² at 10,000/km²; 201 at 7,000/km²; coastal ice | `Extent_and_Density_Per_City.md` L611 | **current** (it is the sheets that differ, drift 1) |
| Highways | Hwy 110 midpoint, neighbors Davis west and Casey east | `Highways.md` L199 to L201; relationship database L339 to L340 | **current** |
| Ports | Australia three-node group; Hobart table 4,159 km; tier not established | `Ports.md` L129, L189, L200, L386, L737, L793 | **current** (Ports changed 2026-11-03 for Relung Panen; Mirny's lines are untouched) |
| Airports | Mirny Airport row L12 with the `DR-82` note | `Airports.md` L3, L12 | **current** (the Winter Intake row changed, see section 4) |
| Relationship entry | founded by Idelsk-Uralia, with Idelsk-Uralia, Russia, Australia and the Sinian Federation present as exile groups | `City_Relationship_Database.md` Mirny entry | **current** and agrees with the Register |
| Founding Register | founded by Idelsk-Uralia; exile groups present: Idelsk-Uralia (also), Russia, Australia, Sinian Federation | `Founding_Register.md` L57 (changed 2026-11-03 22:54) | **current**; the sheets lag it (drift 2) |
| Culture file | last changed 2026-11-03 10:46 (language set), no uncommitted change | `Local_Cultures/Mirny_Subnet/Mirny.md` | **current** |

---

## 3. Drifted

| # | Where | Says | Should say | Kind |
|---|---|---|---|---|
| **1** | `Datasheets/Step_0.md` L18 and `Datasheets/Step_1_and_2.md` L26 ("Extent at the live Census I (computed)") | 137.5 km² at 10,000/km² and 196.5 km² at 7,000/km²; the citation cell says "1,403,549 ÷ 10,000 = 137.5" | **140.4 km²** and **200.5 km²** (1,403,549 ÷ 10,000 = 140.35; ÷ 7,000 = 200.51). The sheet's figures are those of the earlier population 1,375,348 (`DR-90` added the Esperanza share after), so the sheet states a sum that does not come out as written. Same wrong figures sit in the frozen `00.0_Pre-Trip_Inspection_AS_RUN_2026-09-28.md` L265 (a dated record, leave) and in `Amendment_Notes_2026-10-30_Manual_Input_Audit.md` L39 to L40 (correct on that date, superseded) | arithmetic |
| **2** | `Datasheets/Phase_2.md` L27 (Founding Register row) | "exile groups present: Russia, Australia and the Sinian Federation (China)" | "exile groups present: Idelsk-Uralia (also), Russia, Australia and the Sinian Federation (China)", the Register L57 wording (changed after the sheet was rebuilt; `DR-99`, `DR-105`). `Datasheets/Step_1_and_2.md` L36 carries the same shorter list (it describes the spec line, so it is accurate to the spec but not to the Register) | wording, lags the Register |
| **3** | `Specs/Mirny subnet/Mirny.md` L174 (founding population) and L252 (city-name flag) | exile groups: Russia, Australia, Sinian Federation | add Idelsk-Uralia as an exile group, as the Register L57 and the relationship database already say. This is a **source** drift (the spec was not touched when the Register was amended). Not edited by this unit; it is two lines | source lag |
| **4** | `Datasheets/Phase_2.md` L15 (per-nation breakdown) | "Full 35-row table ... `Specs/Mirny.md` L30–67 (table L30–66)" | 36 rows; header L30, data rows L32 to L67 (L66 and L67 are the last two). The 36 is the figure the whole repass uses; the sheet's own composition row three lines above lists 36 nations | count and range |

**Effect on the pass.** None of the four changes a finding. Drift 1 touches only the Gate 11 area line, and the pass's Gate 11 reading rests on the extent table row, which is current. Drifts 2 and 3 are the Idelsk-Uralia exile-group matter that unit U2 re-derives. Drift 4 is bookkeeping.

---

## 4. Unresolved, for later units

- **New fact next to Mirny (not drift in any cited line).** `Airports.md` Winter Intake Airport row (L23), changed 2026-11-03 (`DR-96`): the airport is now described by properties as an ice-cap island on the Davis/Shackleton coast, reached by air in winter and stocked by the summer ship, with two unchosen candidates, one of them **about 92 km from Mirny** (Drygalski Island) and one 367 km away (Mill Island). Mirny's own airport row is unchanged and still says Mirny receives the onward flights. This bears on Mirny's Phase 5 (relation) and on the Phase 5 and 6 parts of unit U2. It is not for this unit to write into any finding; **carried to U2/U3 and the Phase 5 reads as an input to check**.
- **Drift 1, 2 and 4 fixes** are sheet edits. Sheets are inputs, not pass files, but this unit is read-only by order. Proposed text is in section 3; they can be applied in one pass whenever a unit that rebuilds sheets next runs (U2 will need the Phase_2 and Step_1_and_2 rows rebuilt anyway).
- **Drift 3 fix** is two spec lines (L174, L252), for a morning window with the language-line work already planned.
- Nothing here needs the developer's decision. No entry was added to the decisions file.

---

## 5. Raw tool output

(Pasted below by script from the same commands, run 2026-11-04 about 05:23.)


### `verify_city_sheets.py Mirny`

```
== Mirny: 20 checks, 0 FAIL, 2 NOTE
  PASS D1 19 manifest files                             all present
  PASS D2 spine MUST OPEN covered                       all 57 addresses covered
  PASS D3 coverage line on phase sheets                 all 11 carry it
  PASS D4 Step_5 deliberate stub                        stub statement present
  PASS D5 Step_6 section inventory                      ten sections incl. Phase 10
  PASS D6 DoI reliability gate cited (Phases 1, 4, 7)   cited in all three
  NOTE D7 later-era words                               4 line(s) to READ: Step_7.md L15; Phase_3.md L16; Phase_5.md L39; Phase_5.md L43
  NOTE D8 inference markers (read, never strip)         1 table row(s): Step_-1.md L24
  PASS D9 DRAFT marking                                 all marked
  PASS D10 shared sheets cited exist                    all exist
  PASS D11 README Datasheets row                        
  PASS D12 Step_-1 spec ranges and Step_0 census rows   line-range citations present; census named
  PASS P1 sections A-N                                  ABCDEFGHIJKLMN
  PASS P2 step/phase blocks                             steps 12, governing 11, T8 11 (want 12, 11, 11)
  PASS P3 spine addresses in section D                  all present
  PASS P4 datasheet files pointed to                    all 19
  PASS P5 aliases in section A                          all 1 names present
  PASS P6 verification block                            0 missing inputs; 228 claims, 0 failed
  PASS P7 placeholders / carried names                  none
  PASS P8 ledger exists                                 
```

### `audit_city_inputs.py --city Mirny`

```
Mirny                  tests 40  GAP 0  note 2 
```

### `check_must_open_coverage.py --city Mirny`

```

PRE-TRIP: step blocks / governing / T8 lines / sections / spine addresses missing from section D
  Mirny                12 11 11  ABCDEFGHIJKLMN P3 Davis_Geosciences_Research
phases parsed (addresses per phase): {0: 3, 1: 6, 2: 3, 3: 5, 4: 7, 5: 6, 6: 5, 7: 13, 8: 2, 9: 4, 10: 3}
coverage counts recorded in datasheets: 11 of 11
P0  Repo_Scope.md                                direct  1  via-shared  0  none  0
P0  Timeline Eras                                direct  0  via-shared  1  none  0
P0  Official_Population_Census.md                direct  1  via-shared  0  none  0
P1  Locations                                    direct  1  via-shared  0  none  0
P1  Specs                                        direct  1  via-shared  0  none  0
P1  Energy_Grid_Failure_Rationale.md             direct  1  via-shared  0  none  0
P1  READER                                       direct  1  via-shared  0  none  0
P1  Stations                                     direct  1  via-shared  0  none  0
P1  16_Per_City_Three_Tier_Run.md                direct  1  via-shared  0  none  0
P2  No_National_Stereotypes.md                   direct  0  via-shared  1  none  0
P2  Falkland_Treaty                              direct  1  via-shared  0  none  0
P2  Official_Population_Census.md                direct  1  via-shared  0  none  0
P3  READER                                       direct  1  via-shared  0  none  0
P3  Specs                                        direct  1  via-shared  0  none  0
P3  City_Concept-Art                             direct  1  via-shared  0  none  0
P3  Davis_Geosciences_Research                   direct  1  via-shared  0  none  0
P3  City_Megasheets                              direct  1  via-shared  0  none  0
P4  Robot_Physiology_and_Cultural_Practices.md   direct  0  via-shared  1  none  0
P4  Robot_Cold_Physiology.md                     direct  0  via-shared  1  none  0
P4  16_Per_City_Three_Tier_Run.md                direct  1  via-shared  0  none  0
P4  09_Per_City_Baseline_Run.md                  direct  1  via-shared  0  none  0
P4  11_Caloric_Rebuild_and_Livestock_Tier.md     direct  1  via-shared  0  none  0
P4  National_Medical_and_Care_Institutes.md      direct  1  via-shared  0  none  0
P4  National_Economy_and_Currency.md             direct  1  via-shared  0  none  0
P5  Locations                                    direct  1  via-shared  0  none  0
P5  Highways.md                                  direct  1  via-shared  0  none  0
P5  Infrastructure                               direct  1  via-shared  0  none  0
P5  City_Cross_Subnet_Relationships.md           direct  1  via-shared  0  none  0
P5  City_Relationship_Database.md                direct  1  via-shared  0  none  0
P5  City_National_Connections.md                 direct  1  via-shared  0  none  0
P6  Robot_Religions                              direct  1  via-shared  0  none  0
P6  National_Holidays.md                         direct  1  via-shared  0  none  0
P6  Ice-Cold_Buddhism_Research                   direct  1  via-shared  0  none  0
P6  The_True_Believer_Extraction.md              direct  1  via-shared  0  none  0
P6  The_Meme_Machine_Extraction.md               direct  1  via-shared  0  none  0
P7  Division_of_Industry                         direct  1  via-shared  0  none  0
P7  16_Per_City_Three_Tier_Run.md                direct  1  via-shared  0  none  0
P7  Division_of_Industry_Sweep_2026-08-31.md     direct  1  via-shared  0  none  0
P7  01_Burden_Scoring_Model.md                   direct  1  via-shared  0  none  0
P7  08_Volume_Based_Requirement_Reference.md     direct  1  via-shared  0  none  0
P7  National_Medical_and_Care_Institutes.md      direct  1  via-shared  0  none  0
P7  Theoretical-Calculations                     direct  1  via-shared  0  none  0
P7  Industry_Staffing_and_Productivity           direct  1  via-shared  0  none  0
P7  jobs_professions_and_fields                  direct  1  via-shared  0  none  0
P7  National_Economy_and_Currency.md             direct  1  via-shared  0  none  0
P7  City_Logistics.md                            direct  1  via-shared  0  none  0
P7  Factions                                     direct  1  via-shared  0  none  0
P7  Megacorps                                    direct  1  via-shared  0  none  0
P8  Robot_Biology_and_Culture                    direct  1  via-shared  0  none  0
P8  Weapons_and_Tools_Philosophy.md              direct  1  via-shared  0  none  0
P9  Laws_of_Robotics.md                          direct  1  via-shared  0  none  0
P9  Robot_Universals                             direct  1  via-shared  0  none  0
P9  Doll_Representation_Categories.md            direct  1  via-shared  0  none  0
P9  Robot_Physiology_and_Cultural_Practices.md   direct  0  via-shared  1  none  0
P10 Characters                                   direct  1  via-shared  0  none  0
P10 Enneagram_Character_Index.md                 direct  1  via-shared  0  none  0
P10 Zodiac_Signs_Full_Attributes.md              direct  1  via-shared  0  none  0
TOTAL gaps across 1 cities: 0
```

### `check_founders_against_register.py --city Mirny`

```
====================================================================================================
FOUNDERS vs. THE FOUNDING REGISTER — places to READ (not a verification)
====================================================================================================

====================================================================================================
STATION-HERITAGE WORDING (DR-19) — places to READ
====================================================================================================

----------------------------------------------------------------------------------------------------
Founder disagreements: 0 · heritage wording: 0 · files scanned: 1835
Scoped to: Mirny · other cities' files skipped: 1512 (names and lines deliberately not shown) · withheld files skipped: 340
Lines in shared files skipped because they also name another city: 1 (not shown; read them in the preparation phase, not during a pass)
Excluded: Background-Lore (locked), graphify-out, Archive/ (DR-27), pass run records (use --include-passes),
and the rule/tracking files themselves. Hits are where to READ; a clean result is not proof.
```

### `handoff_audit.py <Mirny folder>`

```
pass audited : Mirny
phase files  : 9
=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2, 3, 4, 5, 6, 7, 8, 9, 10
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls
  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      3 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      4 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      5 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      6 |        0 | FORMAL   |    0 | n/a - nothing addressed to it
      7 |        0 | FORMAL   |   38 | n/a - nothing addressed to it
      8 |        0 | FORMAL   |   27 | n/a - nothing addressed to it
      9 |        0 | FORMAL   |   28 | n/a - nothing addressed to it
     10 |        0 | FORMAL   |   33 | n/a - nothing addressed to it
TOTAL outbound handoff rows: 0
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 0
=== outbound rows, per target, for hand reconciliation ===
```

### `phase_discipline_check.py <Mirny folder>`

```
pass audited : Mirny
=== T3 - POSITION-COVERAGE LEDGER ===
  phases in header: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Child              filled=3  blank=6   blank at: P3, P4, P5, P6, P7, P8
  The Lover (position)   filled=3  blank=6   blank at: P2, P3, P5, P6, P7, P8
  The Parent             filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Ruler              filled=2  blank=7   blank at: P2, P3, P4, P5, P6, P8, P9
  The Elder              filled=4  blank=5   blank at: P3, P4, P5, P7, P8
  The Mentor             filled=3  blank=6   blank at: P2, P3, P4, P5, P6, P9
  The Passer-Through     filled=5  blank=4   blank at: P2, P4, P6, P7
  The Neighbor           filled=3  blank=6   blank at: P2, P3, P4, P6, P7, P8
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).
=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the axis had no use for the Chose it attract/repel analysis at Mirny, the Inherited it and
  [04_Phase_03_Surface_and_Texture.md]  T4 present: this phase's axis had no use for smell (no admitted input), interiors and building fabric 
  [04_Phase_04_Ordinary_Life.md]  T4 present: this phase's axis had no use for dwellings and amenity layout, a shift roster, an intracit
  [04_Phase_05_Relation_and_Geometry.md]  T4 present: this phase's axis had no use for rivalry (none recorded), 5b's sibling form, the per-natio
  [04_Phase_06_Meaning.md]  T4 present: this phase's axis had no use for the roster's denominational strongholds, aesthetics, nume
  [04_Phase_07_Order.md]  T4 present: this phase's axis had no use for the Federation's own form of government above the region,
  [04_Phase_08_Making.md]  T4 present: this phase's axis had no use for the national food tonnages, calories, tier shares and sit
  [04_Phase_09_Populations.md]  T4 present: this phase's axis had no use for the national drink, smoking and siligel detail, the robot
  [04_Phase_10_Catalog.md]  T4 present: this phase's axis had no use for the gear catalog and its two Mirny items, the Zodiac subs
  9/9 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 9 lines above by hand.
=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: Alive in its conditions and its two bodies — a working coast that keeps nine places talking without being thanked, where people stop together, own their own calls, and get a sunset with no night after it and an open sea nobody can promise — and lovable by someone who wants to be trusted with their own reading; but what its people laugh at and do with their own hours is still the largest empty slot, so for now the love is for how the place holds its conditions more than for any custom it is known to keep (an early, provisional verdict; it must not steer Phases 7–8, or it is falsified and withdrawn).
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)
  (1 other line(s) in 08_Review_Panel.md merely mention the Lover faculty; they are NOT the marker.)
  T5 not fully applied this pass (one or both markers absent).
```

### `git diff 8777bb5f..HEAD --stat` and `git rev-parse HEAD`

```
8777bb5f75a70fd7966af8826b74c798239d4ec2
(empty diff)
```
