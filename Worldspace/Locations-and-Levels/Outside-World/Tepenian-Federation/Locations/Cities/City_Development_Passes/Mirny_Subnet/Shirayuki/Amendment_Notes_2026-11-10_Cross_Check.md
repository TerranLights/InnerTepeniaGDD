# Shirayuki: amendment notes for the cross-check (current as of 2026-11-10)

**What this is.** The record of where Shirayuki's pass text does not match its sources as they stand on 2026-11-10,
what the sources say, and which of the pass's conclusions rest on inputs that have changed. **It edits no pass file,
and no pass file has been edited** (`DR-101`). It states the current fact with its source address, not what any text
used to say (`DR-102`). It is the note the cross-check of 2026-11-10 works from (`DR-104` item 3, `DR-106`); the
note of 2026-10-30 is kept as written.
**How entries are built.** Pass location (file and line, with a neutral description of the topic), then the current
fact, then its source address. Every source line named here was read on 2026-11-10 between 05:06 and 05:12 (the
orchestrator's `awk`/`sed` reads, logged in `Amendment_Log_2026-11-10.md`); every derived figure was recomputed by
command the same morning. Pass line numbers are as the pass files stand today (unchanged since 2026-10-20).
**Entry numbers.** `SRY-001` to `SRY-014`, `SRY-S01` to `SRY-S05`, `SRY-C01` to `SRY-C03` and `SRY-U01` to `SRY-U04`
are cited by other files and keep their meaning; new entries continue each series. **Section letters:** section F
holds the conclusions to be tested (as the cross-check plan names it, `DR-104` item 3); source defects are section G.
**Other locations.** Other cities are named by role, with the line that names them, never compared (law of one
location). A relation is taken only from Shirayuki's own lines (`DR-122` item 5).
Paths: `CITIES` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`;
`ULM` = `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`; `LOG` = `ULM/DEVELOPER_RULINGS_LOG.md`;
`QUEUE` = `Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md`; spec = `CITIES/Specs/Mirny subnet/Shirayuki.md`;
census = `CITIES/Official_Population_Census.md`; `16` and `09` = the files of those numbers in `CITIES/Division_of_Industry/`.

---

## A. Standing decisions (present tense)

**D-1. No pass file is edited; each mismatch is recorded in an amendment note.** Developer, 2026-10-30: *"yup, all as
recommended."* (`ULM/Manual_Input_Audit_2026-10-29/Walkthrough_Decisions.md` L199–L201; `DR-101`, `LOG` L1673–L1679.)

**D-2. The Pre-Trip and datasheet files for Shirayuki do not exist, and the tools that build them do not build
Shirayuki.** The to-do stands (`Walkthrough_Decisions.md` L211; `Dev-Road-Map/Weekly_To-Do_-_Current.md` L73, L80).
`Tools/build_pretrip.py --list` lists Shirayuki under "Not built by this generator: its ULM pass is complete
(Tri-Cities)"; `Tools/build_datasheets.py Shirayuki` stops with `KeyError: 'Shirayuki'` (both run 2026-11-10 05:05;
neither edited). Every reading list of this cross-check is built by hand. Question: `DEC-440`.

**D-3. The cross-check plan.** One reader per item in section F checks whether the conclusion holds, narrows or flips;
only items that change are re-derived, using the rulings as they stand (`DR-104` item 3, `LOG` L1703; `DR-106` items 1
and 3, `LOG` L1724; `DR-105` item 4 records that Shirayuki follows that plan, `LOG` L1712; the startup file, Section 2
item 3).

**`SRY-S01`. The census tier list equals the spec's.** Census L426–L428 and spec L46–L48 are the same three lines
(Primary Japan; Significant Australia, Korea; Notable 35 rows, the Sinian Federation first, Tibet last). The census is
892 lines (`wc -l`). The census prose at L422 is `SRY-S04`.

**`SRY-S02`. The extent row.** `ULM/Extent_and_Density_Per_City.md` L616: Shirayuki, Census I 1,112,600, 111 and
159 km², Larsemann Hills. L656 is a dated scenario row.

**`SRY-S03`. Left in place.** File `16` is not edited by this note; its Shirayuki section is L1754–L1769
(`SRY-006`, `SRY-011`).

**Decisions of 2026-11-03, night (`DR-105` item 4, `LOG` L1712, and its "Noted" row, L1713).**
- **Band.** Census I governs a city's band (`DR-4` 4.1, `LOG` L214–L220); Shirayuki's Census I, 1,112,600, is Band 5
  (`LOG` L1713). Under `DR-4` 4.2 (`LOG` L228–L251) the Band 5 distributional analysis is deferred until all 38
  cities have finished the ULM, CST and RWBEM, and a pass "must say so".
- **The oasis rock.** About 40 km² of ice-free rock for the three Larsemann Hills cities, divided by Census I share
  and stated as arithmetic: Shirayuki's part is 13.36 km² (`SRY-003`).
- **Rock-founded.** Shirayuki is rock-founded; the site sets the difficulty coefficient (`16` L1758: D = 1.25,
  "rock-founded, food term 100%").
- **The Russian-named rows.** Each successor row is its own origin, as with every row.
- **The plan.** As `D-3`.

---

## B. Founding

### SRY-005. Founders come only from the Founding Register, which adds geography to the allocation

**Pass places that state the founding basis as the allocation alone** (unchanged list): `00_Frame.md` L65, L266;
`01_Inherited.md` L197–L204 (section A1); `02_Spine.md` L87; `04_Phase_02_Composition_and_Arrival.md` L42, L107;
`04_Phase_05_Relation_and_Geometry.md` L47; `04_Phase_07_Order.md` L106; `04_Phase_10_Catalog.md` L158;
`04z_Post-Ruling_Enrichment_Review.md` L17; `07_QA_Gates.md` L156; `09.5_Log.md` L64, L206, L475, L707 (dated record).

**Current fact.** `CITIES/Founding_Register.md` L61: founders "Japan, by the Jeju-do court's diplomatic allocation";
basis "The Jeju-do court's diplomatic allocation, **and, in addition, geography**: zone gap 3 to the Prydz Bay coast
(the edge of the rule). Developer: geography is an *additional* factor, not a replacement."; source spec L203 and
`DR-44`. Register rules L8–L14: founders are decided in the Register and nowhere else; a founding nation stands on
geography and access, never on the real station; each founding is stated on the city's own geography and access.
`DR-44` (`LOG` L919 verbatim; L930: "Not a rewrite of the basis"). Spec L203: "Japanese exiles, arriving via the
Jeju-do court's diplomatic allocation." Conclusions resting on the basis: `SRY-C08`.

### SRY-009. The queue question about the national-connections file is closed

**Pass places that treat it as open or the tie as unusable:** `00_Frame.md` L148; `04_Phase_02` L283;
`04_Phase_05` L89–L92, L258; `05_Reconciliation.md` L254, L341 (row 8), L346; `07_QA_Gates.md` L32, L126;
`09_Record.md` L35, L99; `10_Readiness_Check.md` L132–L133; `09.5_Log.md` L707 (dated record).

**Current fact.** `QUEUE` L696 heading carries ✅ and "ANSWERED 2026-10-01"; L698–L702: answered by `DR-19`, the
offending line is gone from `City_National_Connections.md`, the tie was re-grounded on Highway 4, the corpus sweep is
done, closed by the developer 2026-10-01. The live entry: `CITIES/City_National_Connections.md` L388 (heading
"Shirayuki"), L393–L394: a Medium, Infrastructure tie to the Mawson-subnet junction city on Highway 4 (name in force:
`CITIES/City_Renames_Alias_Table_2026-10-03.md` L10). Conclusions resting on it: `SRY-U05`.

---

## C. Population figures and derived numbers

### SRY-001. Census totals

| | Census I | Census II |
|---|---|---|
| Humans | 545,891 | 319,190 |
| Robots | 566,709 | 372,181 |
| Combined | **1,112,600** | **691,371** |

Sources: census L505 (Census I) and L653 (Census II); spec L41 and L42 carry the same totals. **Pass places**
(unchanged list): `00_Frame.md` L29–L30, L45, L157–L159; `01_Inherited.md` L80, L86–L89, L111, L174, L229, L243;
`03_Research.md` L314; `04_Phase_02` L75, L94; `04_Phase_09_Populations.md` L24–L25; `05_Reconciliation.md`
L174–L175, L333; `07_QA_Gates.md` L167–L168, L173–L175 (pasted scan output of the pass's own run); `09.6_Input_Audit.md`
L35; `09.5_Log.md` L571, L647, L925 (dated record).

### SRY-002. Derived figures (computed by command, 2026-11-10)

| Derived figure | Current value |
|---|---|
| Retention, combined (691,371 ÷ 1,112,600) | **62.14%** |
| Retention, humans (319,190 ÷ 545,891) | **58.47%** |
| Retention, robots (372,181 ÷ 566,709) | **65.67%** |
| People not here (1,112,600 − 691,371) | **421,229** (humans 226,701; robots 194,528) |
| Humans gone / robots gone | **41.53%** / **34.33%** |
| Gap, robot retention minus human retention | **+7.20 percentage points** |
| Robot share, Census I then II | **50.94%** then **53.83%** (+2.90 points) |

**Pass places:** as listed in the 2026-10-30 note's `SRY-002` (those pass lines have not moved). **Wording false as
written:** `01_Inherited.md` L95–L99 (the retention layer immune to the census rebalancing) and `05_Reconciliation.md`
L177–L178 (the ratios unchanged and invariant): census L505 and L653 carry different human and robot increments in
their row notes, so the ratios take the values above.

### SRY-003. Band, footprint, rock and ice shares, workforce (computed by command, 2026-11-10)

| Pass statement (topic) | Current value | Address |
|---|---|---|
| Distance of Census I from the one-million line | **11.26% above** (112,600); Census II **30.86% below** (308,629) | census L505, L653 |
| Band | **Band 5** on Census I (`DR-4`; `LOG` L1713) | `LOG` L214–L220 |
| Required footprint at 10,000 and 7,000 per km² | **111.26 to 158.94 km²** | computed |
| Cluster Census I (the three Larsemann Hills cities) and Shirayuki's share | 3,330,740; **33.40%** | census L502, L505, L509 |
| Shirayuki's part of the ~40 km² rock (Census I share, arithmetic, `DR-105` item 4) | **13.36 km²** | computed |
| Share of the footprint on rock / on ice | rock **8.41% to 12.01%**; ice **87.99% to 91.59%** | computed |
| Cluster density on the rock | 3,330,740 ÷ 40 = **83,268.5 per km²** | computed |
| Workforce | **839,655** (352,970 + 97,337 + 389,348) | `16` L277, L1758–L1760 |
| The pass's 25%, 20% and 45% tests on the whole workforce | 209,914; 167,931; 377,845 | computed |
| The same sectors as file `16` applies them (shares of the distinctive tier, 486,685) | 25% = 121,671; education 20% = 97,337 | `16` L1762, L1769 |

**Basis difference.** `04_Phase_07_Order.md` L38–L40 apply the arts and education percentages to the whole
workforce; file `16` applies them to the distinctive tier (L1762, L1769). Both bases are in the sources as written.
**Pass places:** as listed in the 2026-10-30 note's `SRY-003`.

### SRY-006. File 16's Shirayuki counts agree with its Half B row

`16` L1758–L1760: baseline 352,970 (42.0%), mandated 97,337 (11.6%), free 389,348 (46.4%), summing to 839,655, the
Half B row at L277. L1762: distinctive tier 486,685 (58.0%). L1762–L1763: counts recomputed on the current population
with shares held, and the robot term added (`SRY-011`).

### SRY-010. Composition

| Item | Value | Spec line |
|---|---|---|
| Rows in the table | 38 (1 Primary, 2 Significant, 35 Notable); shares sum to 99.989% | L62–L99 (computed) |
| Primary | Japan **34.20%**; the rest of the city **65.80%** | L62 |
| Significant | Australia **9.65%**, Korea **9.10%** | L63, L64 |
| Next rows | Sinian Federation **4.49%** (Notable, the fourth row), Germany 3.90%, Russia (core state) 3.53% | L65–L67 |
| The Sinian Federation's four detached pieces and Taiwan | Manchuria 0.26%, Mongolia 0.21%, East Turkestan 0.13%, Tibet 0.018% (sum 0.618%); Taiwan 2.86%, its own row | table rows |
| The 12 rows naming Russia (core state) or a Russian region | sum **9.07%**; each is its own origin (`DR-105` item 4) | table rows (computed) |
| Robot and human columns | every row gives each nation the same share of robots as of humans (Japan: 193,839 of 566,709 robots and 186,718 of 545,891 humans, 34.20% each) | L62 (computed) |
| How the shares were set | the 2026-11-02 rework: every country in its latest-period form, split by headcount; the Sinian Federation's share multiplied by 0.6427 (random 0.55 to 0.65) and the freed points given to Australia and Korea; tiers relabeled from the final shares | L54; `DR-85`, `LOG` L1527–L1529 |

`CITIES/Upper_Earth_Immigration_Composition.md` L569 gives the same final composition. **Pass places:** as listed in
the 2026-10-30 note's `SRY-010`. Conclusions resting on the composition: `SRY-C01`, `SRY-C04`, `SRY-C09`, `SRY-U04`.

### SRY-011. Division of Industry shares and the robot-keyed term

`16` L277 (Half B): workforce 839,655; baseline **42.0%**, mandated **11.6%**, free **46.4%**. `16` L1762: distinctive
tier **58.0%**. `16` L1763: the baseline includes robots × 15.75 ÷ 1,000 = 8,926 workers (566,709 × 0.01575 =
8,925.7, by command), as `09` §3.6 defines it (`DR-97`, `LOG` L1638–L1643). `09` L78: required 297,848 of 839,655 =
**35.5%**. `09` L216: the two files agree on the robot term and differ on the food requirement (53 in `09` §2, 120.7 in
`16`), "so the two baselines are not the same quantity". `09` L146: the same sectors in the modern United States run
roughly 29% of the workforce (42.0 − 29 = **+13.0 points**).

| Pass place (topic) | Current fact |
|---|---|
| `04_Phase_04_Ordinary_Life.md` L43–L44; `02_Spine.md` L60, L316–L318 (the percentages stated as ratios that do not move) | The shares take the values above (`16` L277). |
| `02_Spine.md` L82 (the robot-keyed correction stated as pending, the margin an upper bound) | The robot term is part of file `16`'s formula (`16` L1763). Conclusion: `SRY-C06`. |
| `02_Spine.md` L74–L75 (two baselines in the source) | `09` L78 gives 35.5%; `16` L277 gives 42.0%; the difference is stated at `09` L216. |
| `02_Spine.md` L81 (the baseline against a US comparable of about 29%) | **+13.0 points**. |
| `04_Phase_10_Catalog.md` L134 (the compulsory-tier share) | **42.0%** (`16` L277). |

---

## D. Language

### SRY-012. The language rule

**Pass places.** `04_Phase_08_Making.md` L198–L243 (section F; L206 derives the dominant local vernacular from Japan's
Primary share; F.1 the vocabulary as a registry), L404–L411 (F.STOCK); `04_Phase_09_Populations.md` L96 (the language
row).

**Current fact.**
- **`DR-100`** (`LOG` L1664–L1671), recorded as: (1) Hawaiian (later Tepenian) is the dominant language everywhere;
  (2) a supporting tier is a language not dominant but widely understood; (3) a city's supporting tier is every
  language group within 12 percentage points of its largest group (mid-points; nations sharing a language summed);
  (5) the shares are national-origin shares, not speaker counts, and the nation-to-language mapping is recalled, not
  verified.
- **General canon, developer 2026-11-09** (`DR-125` item 6, quoted in the startup file, Section 4 item 1):
  *""Hawaiian" is a Pidgin between a primary base of English and Japanese, with a supporting base of Korean, Tagalog,
  Ilocano, and Mexican Spanish. Later in the future, further influence from a wide variety of languages) resulted in
  Hawaiian later becoming Tepenian"*. Recorded as: Hawaiian and Tepenian are one language over time.
- **`DR-85`** verbatim (`LOG` L1527): the Tepenian language is, *"down at its foundational level core, a Pidgin
  between English and Japanese"*.
- **Shirayuki's groups** (`CITIES/Research_Logs/Language_Blocs_By_City_2026-11-03.csv` L708–L712): Japanese 34.200;
  English 12.450 to 14.020 (mid 13.235); Russian 6.090 to 15.300 (mid 10.695); Korean 9.100; Mandarin 7.610 to 7.968.
  The nearest group's mid-point is 20.965 points below Japanese, so the set is **Japanese alone**
  (`Language_Sets_By_City_Reference_2026-11-03.md` L34: "Japanese 34.2 | none | none"; L77 the 12-point cutoff; the
  12-point addendum, L63–L73, lists no Shirayuki row).
- `Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` L426: robot vernacular tracks the
  dominant local culture and the community who had her built.
- Status: the rule is written into no Shirayuki file. The culture files named for the language work are listed at
  `CITIES/Research_Logs/ULM_Runs_Casey_Then_Mirny_Handoff_2026-11-03.md` L46–L47 (the rule at L25); Shirayuki is not
  among them.

Conclusions resting on it: `SRY-C03`, `SRY-U04`.

---

## E. Names, citations, files and new canon

### SRY-004. Names in force

Four places the pass names carry names since ruled; the names in force are in
`CITIES/City_Renames_Alias_Table_2026-10-03.md`: the 38th city (alias L12, `DR-39`); the Mawson-subnet city on
Highway 4 and its junction (L10, L14, `DR-37`); the Halley-subnet city of the demographic tie (L11, `DR-38`); the
plateau city of the kinship tie (L105, `DR-42`; its central scientific district keeps the station's name, L107).
Pass places: as listed in the 2026-10-30 note's `SRY-004`. The real station's name is a coordinate (Register L11–L13;
spec L23).

### SRY-007. Citations in `04_Phase_05` L82–L87 (the wider set)

`04_Phase_05` L82–L84 attribute to `Airports.md` the kinship tie to the plateau city; the source line is
`Locations/Infrastructure/Airports.md` **L18** (the Mountain Pass row), which says "The kinship is in the census, and it
is asymmetric in a way worth keeping" and gives Shirayuki's tie as running to the plateau city. The same tie sentence
is at `CITIES/National_Medical_and_Care_Institutes.md` **L109** ("Shirayuki (Japan) ties to" the plateau city). L86–L87
describe the Halley-subnet tie as unexplained; Shirayuki's own entry, `City_National_Connections.md` L391–L392, gives
"Both share genuine Japanese-heritage demographic presence." **A relation is taken only from Shirayuki's own lines**
(`DR-122` item 5, `LOG` L1868): the table rows at `National_Medical_and_Care_Institutes.md` L104–L107 and the other
city's own entry are that city's lines, not Shirayuki's. Conclusions resting on the ties: `SRY-U03`.

### SRY-008. Runbook line numbers in the record

`10_Readiness_Check.md` L78 and L237 cite `00_RUNBOOK.md` "L2126–2131" and "L2129". Today: L2128 is the heading of
C.9c, L2130 the developer's quotation of 2026-09-06 about using a founding population's culture only once composition
is established, L2140–L2146 the worked instance naming Shirayuki's founders "per the Founding Register". Read the
pass's citations as pointers to the runbook of the pass's own time.

### SRY-013. Culture-file proposals in the pass docket

`05_Reconciliation.md` L170–L178 and L326–L346 (docket rows 1–9, "proposed, not applied") rest on
`CITIES/Local_Cultures/Mirny_Subnet/Shirayuki.md`, the developer's file. Checked 2026-11-10 by pattern only: L9 still
carries 1,178,313 and 728,324 (current: `SRY-001`); L48 still gives day counts of 60 and 61 (current: spec L157–L158,
polar night ~49 days, midnight sun ~62 days); L42 and L263 still name a single neighbor as the oasis's co-sharer
(current: one ~40 km² patch shared by the three Larsemann Hills cities, `DR-105` item 4; spec L221 names the same
single neighbor);
L34, L100, L262 name the real station as infrastructure (Register L11–L13; spec L23). Nothing applied.

### SRY-014. The pass README's state table

`README.md` L42–L46 describe Phase 9, `04z`, Phase 10, files `05` to `10` and the other two methods as not re-run,
never written or not started; the folder holds all of them, and `10_Readiness_Check.md` L321–L322 reads "ULM COMPLETE
FOR SHIRAYUKI". `README.md` L80 calls the culture file unopened; `05_Reconciliation.md` L326 onward reconciles against
it. **Status words are the developer's** (startup file Section 3: never declare a review complete or ready).

### SRY-015. Canon given after the pass ran (2026-09-06 to 09-13): rows 1, 2 (2026-09-28) and 6 (2026-10-01) predate its last edit of 2026-10-01, which cites `DR-24` and `DR-25`; the rest is later

| Canon | Source | Bears on |
|---|---|---|
| **Robots carry a national origin**, learned by immersion after coming online; this resolves the runbook's "open reserved question" | `DR-11`, `LOG` L448–L461 (verbatim L450–L453; "Resolves" L457) | `SRY-C04` |
| **Per-nation figures are weighting**; no finding may rest on a within-tier difference; the per-nation rows are ADMITTED-DEMOTED **for humans and robots alike** | `DR-12`, `LOG` L463–L475 | `SRY-C01`, `SRY-C04` |
| **An origin row covers both humans and robots, each at its own percentage**; whether a row records nationality or residence at departure was not answered | developer, 2026-11-09, `DR-128` item 1, general canon (quoted in the startup file, Section 4 item 3) | `SRY-C04` |
| **Humans could keep arriving after the Falkland Treaty was signed; they could not go back to Upper Earth.** Whether robots kept arriving was not answered | developer, 2026-11-09, `DR-127` item 2, general canon (quoted in the startup file, Section 4 item 2) | `SRY-C05` |
| **"Records can draw people"** (the row of `DR-25` so headed) is a general mechanism any location may use | developer, 2026-11-09, `DR-124` item 4, general canon (quoted in the startup file, Section 4 item 4); `DR-25`, `LOG` L645–L648 | `SRY-C05` |
| **Newcomers can inherit a station's research, equipment, techniques and results**, alongside records and infrastructure; a tradition cannot be inherited | `DR-24`, `DR-25`, `DR-26`, `LOG` L623–L664 | `SRY-C05` |
| **The language rule and the language's origin** | `SRY-012` | `SRY-C03`, `SRY-U04` |
| **A single location's run takes a relation only from its own lines** | `DR-122` item 5, `LOG` L1868 | `SRY-U03`, `SRY-U05` |

### SRY-016. The pass's five queue questions, against the rulings as they stand

| Queue entry (`QUEUE`) | Queue mark | Ruling that now bears on it | Pass places |
|---|---|---|---|
| `DRQ-10` the band crossing (L551) | open | `DR-4` (Census I governs; Band 5 analysis deferred, and the pass says so) and `DR-105`'s noted row (Shirayuki Band 5), `LOG` L214–L251, L1713 | `SRY-C02` |
| `DRQ-11` who allocated the ~40 km² rock, or nobody (L579) | open | `DR-105` item 4 states the division as arithmetic of Census I share; it names no allocating authority | `SRY-C07` |
| `DRQ-12` the ratified-root list (L614) | open | none found | `DEC-003` (open) |
| `DRQ-13` rock-founded versus mostly on ice (L656) | open | `DR-105` item 4: "Shirayuki is rock-founded (the site sets the difficulty coefficient)" | `SRY-C06` |
| `DRQ-14` the national-connections tie (L696) | answered 2026-10-01 | `DR-19` | `SRY-009`, `SRY-U05` |

The queue file is not edited by this note. Whether the developer treats `DRQ-10` and `DRQ-13` as closed by these
rulings is a question (`DEC-441`).

---

## F. Conclusions that rest on current inputs and may change on re-derivation

No verdict is stated here; each row is tested by one reader (`D-3`). Each row gives the pass location, the input it
rests on, and that input's current value.

| ID | Pass location | Input it rests on | Current value of the input |
|---|---|---|---|
| `SRY-C01` | `04_Phase_02` L58–L71 (A.2: the shape of the Significant tier; no available second pole; the Act 2 half); `02_Spine.md` L121–L137 (§2e, `G8`); `00_Frame.md` L311 (`G8` row) | The tier members and shares; the number of origins; how successor rows count | `SRY-010`: Significant Australia 9.65, Korea 9.10; next row 4.49; 38 origins; each Russian-named row its own origin (`DR-105` item 4); no finding on a within-tier difference (`DR-12`) |
| `SRY-C02` | `00_Frame.md` L28–L34 (band line of the declaration), L153–L181 (§2, readings A/B/C, Band 4 chosen provisionally), L292, L364 | The band ruling; Census I's distance from the line | Band 5 on Census I (`DR-4`; `LOG` L1713); 11.26% above the line; the distributional analysis deferred by ruling (`SRY-016`) |
| `SRY-C03` | `04_Phase_08` L198–L243 (F, F.1), L404–L411 (F.STOCK); `04_Phase_09` L96 | The language rule; the language's origin | `SRY-012` |
| `SRY-C04` (new) | `00_Frame.md` L330–L332 (§8 item 7, reserved); `04_Phase_02` L73–L95 (A.3, reserved finding 1), L355 (canon-check row); `04_Phase_09` L58–L88 (§B), L336 (§I row) | Whether robots carry a national origin; the standing of the robot columns | `SRY-015` rows 1–3; spec robot columns copy each row's share (`SRY-010`) |
| `SRY-C05` (new) | `04_Phase_02` L99–L173 (§B: arrival modes; B.1 "nobody in this city is here by a decision they made", scoped to 2564; B.2 the tense table; B.3 nothing to be chosen for at founding; B.4 the causal order); `00_Frame.md` L307 (`G4` row); `02_Spine.md` L95 | Whether arrivals continued after the signing; what a station's records can do | `SRY-015` rows 4–6 |
| `SRY-C06` (new) | `02_Spine.md` L57–L83 (§2b, `G3`: two baselines; the free tier "an UPPER BOUND"), L256–L266 (§6a: "40.9% is a FLOOR", `DRQ-13`), L280 (spine claim 3); `04_Phase_04` L50–L66 (§2a, "reached independently from two directions"), L261, L272, L285 | The difficulty coefficient's basis; the robot term | `DR-105` item 4 (rock-founded; the site sets the coefficient); `16` L1758, L1763, L277 (`SRY-011`) |
| `SRY-C07` (new) | `00_Frame.md` L235 (§3b provisional assumption 3, "load-bearing"), L292–L296, L365; `02_Spine.md` L229–L255 (§6, L253 the apportionment "MODELED"); `04_Phase_03` L216; `04_Phase_07` L108–L135 (§7b, L113 the rock: "NOBODY"), L285; `04_Phase_09` L189–L220 (§E), L339; `05_Reconciliation.md` L291–L312 (the strongest-finding check); `10_Readiness_Check.md` L255 | Who divided the rock | `DR-105` item 4: divided by Census I share, stated as arithmetic (13.36 km²); `DRQ-11` still marked open (`SRY-016`) |
| `SRY-C08` (new) | `02_Spine.md` L84–L105 (§2c, `G4`: the founding's absences; "NO FOUNDING ARGUMENT", L102); `04_Phase_02` L107–L109 (the site chosen by the court); `01_Inherited.md` L197–L223 (A1) | The founding basis | `SRY-005`: the allocation **and, in addition, geography** (zone gap 3, the edge of the rule); "not a rewrite of the basis" (`DR-44`) |
| `SRY-C09` (new) | `01_Inherited.md` L217–L219 (the share descending from the party the founding refused); `02_Spine.md` L135 (`G8` grudging tolerance) | Which rows are the refused party, and their share | Sinian Federation 4.49% (spec L65; Census II 16,711 robots and 14,331 humans); its four pieces 0.618%; Taiwan 2.86% its own row (`SRY-010`) |
| `SRY-U01` | `04_Phase_05` L137–L153 (§5d.1), L168–L201 (§5e), L202–L231 (§6, the merger) | The port section; the gateway rulings | `Locations/Infrastructure/Ports.md` §5.6c (L579 heading); L202 (the gateway row: 4,877 to 4,884 km, long haul, seasonal, shared); L611 (Shirayuki ~8 km, on Grovnes Promontory); `DR-48` to `DR-50` (`LOG` L981–L1019) |
| `SRY-U02` | `04_Phase_06_Meaning.md` L168–L182 (§C, death: asked and deliberately not answered); `00_Frame.md` L326 | The ossuary rulings | `Robot_Physiology_and_Cultural_Practices.md` L75 onward (the ossuary section, developer ruling); the mortuary question deferred corpus-wide |
| `SRY-U03` | `04_Phase_07` L358–L367 (Addendum §D, the plateau city's tier used for a kinship tie, L360–L361); `04_Phase_05` L80–L95 (the wider set) | Where the ties' grounds come from | `SRY-007`; `DR-122` item 5 |
| `SRY-U04` | `04_Phase_08` L306–L421 (the origin-stock addendum: the stock is Japanese; no term coined); `04_Phase_09` L267–L303 (§G, composition then culture) | Japan's tier and share; the language rule | Japan Primary 34.20% (spec L62); Register L61; `SRY-012` |
| `SRY-U05` (new) | `04_Phase_05` L89–L92, L258 ("this pass takes nothing from it"; "a canon relationship is currently unusable"); `00_Frame.md` L148; `04_Phase_02` L283; `05_Reconciliation.md` L254, L341, L346; `07_QA_Gates.md` L32, L126; `09_Record.md` L35, L99; `10_Readiness_Check.md` L132–L133 | The closed queue question; the live tie | `SRY-009`; `DR-122` item 5 |

---

## G. Source defects (the sources disagree with themselves; no choice is made here)

### SRY-S04. Japan's share and the census total, stated differently inside the sources

| Source address | States | Its table or row |
|---|---|---|
| spec L35 and L321 (prose) | Japan **34.20%** | L62: **34.20%** (consistent) |
| census L422 (prose) | Japan **36.27%** | spec L62 and census L426: **34.20%** current |
| `16` L3180 (inside another city's determination) | Japan **36.27%** | flagged by `16` L3580 (current share 34.20%) |
| culture file L9 | Census I 1,178,313; Census II 728,324 | census L505, L653: 1,112,600 and 691,371 |

### SRY-S05. Ruling label of the robot term

`16` L1 and L1763 and `09` L216 cite `DR-97`, matching `LOG` L1638–L1643. Nothing to carry.

---

## H. Open questions for the developer (written in the decisions file, Shirayuki section)

1. `DEC-440` — no Pre-Trip or datasheets can be built for Shirayuki by the current tools (`D-2`).
2. `DEC-441` — whether `DRQ-10` and `DRQ-13` are closed by the rulings in `SRY-016`.
3. `DEC-003` (open since 2026-11-03) — which source folders may ground a finding (`DRQ-12`).
4. Questions raised by the item readers and the re-derivations are added as they arise.

---

## I. Sources checked with no mismatch found (2026-11-10)

- Founding Register L61, L8–L14, L36, L90.
- `Airports.md` L13 (the shared airport lists Shirayuki as a host) and L18.
- `Ports.md` L202, L579, L611.
- `City_Symbol_Assignments.md` L117 (Uranus / Air; the file's uncommitted edits contain no Shirayuki line).
- Spec L157–L158 and L188 (polar night ~49 days, midnight sun ~62 days); spec L23.
- `Extent_and_Density_Per_City.md` L616.
- `City_Renames_Alias_Table_2026-10-03.md` L10–L15, L105, L107.
- No commit after the 2026-10-30 note's last rewrite (2026-11-03 22:57) touches a Shirayuki line in the census, the
  Register, the extent file or the relationship database (`git show -U0 8777bb5f`, hunks at other rows only).

---

## J. The item verdicts of 2026-11-10 (one reader per section F row)

Added at the end of the note so that no line above moves. Each verdict is the reader's own, checked mechanically
(`Tools/triple_read_verify.py` on its PROOF blocks: every field matched the files). Reader files are kept beside the
pass as dot-files `.xc_20261110_item_<ID>.md`. The log of the run is `Amendment_Log_2026-11-10.md` (L-18 to L-33).

| ID | Verdict | What no longer follows (the reader's words, with the pass lines) |
|---|---|---|
| `SRY-C01` | NARROWS | the Act 1 ground "one large group and four equal middle groups" and "unusually FLAT" (`04_Phase_02` L60–L64); the Act 2 half holds |
| `SRY-C02` | FLIPS | the band line "4 — URBAN" and Reading A (`00_Frame.md` L28, L178) against Band 5 on Census I (`LOG` L1713) |
| `SRY-C03` | NARROWS | L206's ground, the dominant vernacular derived from Japan's share (`04_Phase_08`); the speech-marker reasoning holds |
| `SRY-C04` | FLIPS | the "reserved" status and the Act 2 answer "THERE IS NOTHING TO INHERIT." (`04_Phase_02` L86) against `DR-11` |
| `SRY-C05` | NARROWS | B.3's impossibility claims, L144's "only once" and the B.4 order (`04_Phase_02` L139–L160); the `G4` "only" lists |
| `SRY-C06` | NARROWS | the robot-keyed "UPPER BOUND" hedge (`02_Spine.md` L82); "Raised, not resolved" and the floor conditional's open "if" |
| `SRY-C07` | NARROWS | the share as "MODELED, not canon" (`00_Frame.md` L366) and the readiness limit's ground (`10_Readiness_Check.md` L255) |
| `SRY-C08` | NARROWS | parts of `02_Spine.md` L94, L102 ("nothing to reach for"), L104 and `01_Inherited.md` L215, under the added geographic ground |
| `SRY-C09` | NARROWS | the share, headcount, rank and Significant-tier weight of `01_Inherited.md` L217–L218 and `02_Spine.md` L135 |
| `SRY-U01` | NARROWS | §6's label "[CANON — Ports.md], not derived here." (`04_Phase_05` L222) against the port section's SCOPE block (`Ports.md` L688–L690) |
| `SRY-U02` | NARROWS | "because the national practice already runs in the same register as the local value" (`04_Phase_06` L179) |
| `SRY-U03` | FLIPS | the kinship tie's ground in another city's lines (`04_Phase_07` L361); the demographic tie called "UNEXPLAINED" (`04_Phase_05` L86) |
| `SRY-U04` | HOLDS | only the figure at `04_Phase_08` L318 (recorded at L157, L315) |
| `SRY-U05` | FLIPS | the tie "set aside entirely" as "currently unusable", "Raised, not resolved" (`04_Phase_05` L89–L92, L258) |

The 13 items that are not `HOLDS` are re-derived as amendment pieces (`Amendment_Rederivation_*_2026-11-10.md`), each
PROPOSED.
