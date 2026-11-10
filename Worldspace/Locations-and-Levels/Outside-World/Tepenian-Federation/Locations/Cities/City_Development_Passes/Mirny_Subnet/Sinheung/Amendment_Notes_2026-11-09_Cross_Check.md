# Sinheung: amendment note for the 2026-11-09 cross-check

**What this is.** A dated amendment note, written at the start of the finished-city cross-check of Sinheung on 2026-11-09 (`DR-106`, `DR-104` item 3; `DR-105` item (4): Sinheung follows the plan made for the first finished city). It states what is true now in the sources Sinheung's pass rests on, checked against the live files on 2026-11-09. It sits beside `Amendment_Notes_2026-10-30_Manual_Input_Audit.md` (the note of 2026-11-03, entries SNH-001 to SNH-016, its section 7 and the SNH-S entries), which stands; where this note gives a newer fact or address, this note governs. **No pass file was edited. Everything here is PROPOSED** (`DR-101`, `DR-102`). Entries state the current fact with its source address, not what a text used to say. New entries are SNH-017 and up.

**Isolation, stated as the startup file requires.** This session first ran the finished-city cross-check of another city and then continued here. Sinheung is checked on its own terms: its briefs, reading lists and question lists are written from Sinheung's own note, pass folder and sources only; nothing from the other city enters any Sinheung brief; and the orchestrator never compares the two. This note names no other city; where a source line names one, it is cited by address (another location: not used). The shared process lessons carried over are about method only (they are listed in the log).

`CITIES` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`. `ULM` = `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`. `SPEC` = `CITIES/Specs/Mirny subnet/Sinheung.md`. `CENSUS` = `CITIES/Official_Population_Census.md`. `LOG` = `ULM/DEVELOPER_RULINGS_LOG.md`. `PASS` = `CITIES/City_Development_Passes/Mirny_Subnet/Sinheung/`.

---

# A. The note of 2026-11-03, checked against the live files

## SNH-017 — Result of the check

**Command.** `python3 -I verify_sinheung_note.py` (read-only: 51 line checks, each requiring named strings on a named line or in a named range, then a recomputation of every derived figure in SNH-001 to SNH-004, SNH-011 and SNH-012; it prints OK or DIFF and never another location's text). The script and its output are kept beside this note as `.verify_sinheung_note_2026-11-09.py` and `.verify_sinheung_note_2026-11-09_output.txt`.

**Result.** TOTAL line checks: 51   OK: 51   DIFF: 0. Both live-file lengths the note states (the spec 269 lines, the census 892 lines) still hold. Every recomputed figure reproduces the note's value. The raw output, whole:

```
OK       Official_Population_Census.md L509
OK       Official_Population_Census.md L647
OK       Official_Population_Census.md L416
OK       Official_Population_Census.md L417
OK       Official_Population_Census.md L418
OK       Official_Population_Census.md L33
OK       Sinheung.md L4
OK       Sinheung.md L8
OK       Sinheung.md L71
OK       Sinheung.md L72
OK       Sinheung.md L76
OK       Sinheung.md L77
OK       Sinheung.md L92
OK       Sinheung.md L93
OK       Sinheung.md L94
OK       Sinheung.md L95
OK       Sinheung.md L96
OK       Sinheung.md L102
OK       Sinheung.md L104
OK       Sinheung.md L105
OK       Sinheung.md L108
OK       Sinheung.md L154
OK       Sinheung.md L211
OK       Sinheung.md L213
OK       Sinheung.md L215
OK       Founding_Register.md L62
OK       Founding_Register.md L61
OK       Founding_Register.md L60
OK       16_Per_City_Three_Tier_Run.md L257
OK       16_Per_City_Three_Tier_Run.md L1834
OK       16_Per_City_Three_Tier_Run.md L1838
OK       16_Per_City_Three_Tier_Run.md L1839
OK       16_Per_City_Three_Tier_Run.md L1840
OK       16_Per_City_Three_Tier_Run.md L1850
OK       16_Per_City_Three_Tier_Run.md L1851
OK       09_Per_City_Baseline_Run.md L80
OK       Extent_and_Density_Per_City.md L620
OK       Ports.md L130
OK       Neutral_Transshipment_Hubs.md L60
OK       Sinheung.md L90
OK       Sinheung.md L135
OK       DEVELOPER_RULINGS_LOG.md L538
OK       DEVELOPER_RULINGS_LOG.md L634
OK       DEVELOPER_RULINGS_LOG.md L654
OK       DEVELOPER_RULINGS_LOG.md L919
OK       DEVELOPER_RULINGS_LOG.md L930
OK       Language_Blocs_By_City_2026-11-03.md L1104-L1116
OK       Language_Blocs_By_City_2026-11-03.md L1104-L1116
OK       Language_Blocs_By_City_2026-11-03.md L1104-L1116
OK       Language_Blocs_By_City_2026-11-03.md L1104-L1116
OK       City_Symbol_Assignments.md L1-L400
TOTAL line checks: 51   OK: 51   DIFF: 0
file length Sinheung.md: 269 newline-lines (note says 269): OK
file length Official_Population_Census.md: 892 newline-lines (note says 892): OK
composition rows parsed (L92-L130): 39; by tier: {'Primary': 1, 'Significant': 3, 'Notable': 35}; share sum 99.992%; rows under 1%: 18
East Asian cluster: Korea+Japan+Sinian Federation = 47.85; + Taiwan = 50.71; + Manchuria, Mongolia, East Turkestan, Tibet = 51.495
the thirteen Russia rows together: 6.47% (found 13 of 13)
Census I 1014533, Census II 835341
retention humans 83.09%, robots 81.62%, combined 82.34%, gap 1.47 points
robots share of Census I 51.27%, humans 48.73%
workforce (robots + half the humans) = 767362.5; required 271,073 / 767,363 = 35.33%
section 17: 321,100 + 211,975 + 234,288 = 767363; shares 41.845% / 27.624% / 30.532%; fabrication+Institute half = 211975; distinctive 446263
land need at 10,000 and 7,000 per km2: 101.45 and 144.93 km2; density on 40 km2: 25363 per km2
ratio check (Census I added humans/robots): 1.125; city ratio 0.950; (Census II added): 0.748; city ratio 0.967
```

**What the check does not cover.** Line checks test named strings on named lines; they do not re-read the surrounding text, and the pass-file locations the note lists were found by pattern search, so an unlisted passage may exist (the note says so).

---

# B. What changed since the note of 2026-11-03

## SNH-018 — The sources

The note's last commit is `8777bb5f` (2026-11-03 23:03). No later commit touches any of Sinheung's source files (spec, census, Founding Register, Division of Industry, infrastructure files, relationship files, culture files, language tables, symbol file, climate files, Extent file; checked with `git log --since` on 2026-11-09). The one uncommitted change among them is in `City_Symbolic_Substrate/City_Symbol_Assignments.md`; Sinheung's own row in it carries the same Planet and Element the note states, and the change is another location's row (another location: not used). The census tag sentence at `CENSUS` L33 (the tag "(founding wave)" says nothing about when people arrived) was already in the file when the note was filed; the pass files contain no mention of the tag (counted by command), so no item rests on it.

## SNH-019 — Rulings and rules that bear on this run, in the present tense

| Ruling | What it says now | Address in `LOG` |
|---|---|---|
| `DR-105` item (4) | Sinheung follows the plan of `DR-104` item 3; a re-derivation uses `DR-24` to `DR-26` as they stand. | L1707-1718 |
| `DR-106` | The finished cities are reviewed before the new runs. | L1719-1726 |
| `DR-107` item 2 | A piece that needs another piece's result does not start until that result is complete and confirmed. | L1728-1735 |
| `DR-117` items 1, 2, 4 | "Confirmed" means written to file; a reader may repair a single failed proof field in its own output; edits and confirmation sessions run at any hour; the derivation itself runs 05:00-14:59. | L1818-1825 |
| `DR-118` item 2 | The amendment-layer rules are in `ULM/Amendment_Layer_Rules.md`. | L1827-1834 |
| `DR-122` item 5 | A single location's run takes a relation only from its own lines. | L1863-1870 |

## SNH-020 — The missing sheets cannot be built with the builders

The startup file asks that a city lacking its Pre-Trip or datasheets have them built first with `Tools/build_pretrip.py` and `Tools/build_datasheets.py`. Both tools stop on this city: `build_pretrip.py Sinheung --write` and `--out` print "unknown city key 'Sinheung'", and `build_datasheets.py Sinheung --out` stops with a missing-key error (`KeyError: 'Sinheung'`); `build_pretrip.py --list` lists this city under "Not built by this generator: its ULM pass is complete (Tri-Cities)" (the tool's own table, line 144). Nothing was written, and no tool was edited. **Consequence:** this run's reading lists are built by hand from the note and the pass, as the first city's were; no Pre-Trip and no datasheet exists as an input. Entered as a question for the developer.

---

# C. Section 7 of the note of 2026-11-03 restated

The nine conclusions that rest on current inputs, copied unchanged from section 7 of the note of 2026-11-03 (the input values were verified in part A). No verdict is given here; verdicts come from the one-reader checks written to `Amendment_Checks_2026-11-09_Section7.md`.

| ID | Pass location | Topic | Input | Current value and address |
|---|---|---|---|---|
| SNH-C1 | `02_Spine.md` L116-119; `04_Phase_09_Populations.md` B.1 L74-124, B.2 L178-191, L392, L394 | The explanation offered for the difference between robot and human retention | Census I and II rows | Humans 83.09%, robots 81.62%, difference +1.47 points (`SNH-002`); the census labels later additions "Arithmetic, NOT a migration" (`Census` L509, L647) |
| SNH-C2 | `04_Phase_02_Composition_and_Arrival.md` A.2 L47-72 (pooled-cluster table L54-67); `04_Phase_09_Populations.md` C.3 L290-337; `04_Phase_08_Making.md` L62-64; `04_Phase_07_Order.md` L541 | Whether the largest origin cluster is a plurality or a majority, and the bloc question | Pooled share of the East Asian cluster | Korea 33.00 (`Spec` L92); Korea, Japan, Sinian Federation 47.85 (L92, L93, L95); with Taiwan 50.71 (L102); with Manchuria 0.34, Mongolia 0.25, East Turkestan 0.17, Tibet 0.025 (L116-118, L126) 51.50. The sources do not say which pieces form the cluster. |
| SNH-C3 | `04_Phase_02_Composition_and_Arrival.md` A.4 L91-103 | The nation nearest by reach against the founding nation | Shares of the nearest-zone nations | Russia (core state) 2.03% (`Spec` L105); Idelsk-Uralia 2.03% (L104); Kazakhstan 1.45% (L108); the thirteen Russia rows together 6.47% (`SNH-012`); Korea 33.00% (L92). The spec table has no UTC column. |
| SNH-C4 | `04_Phase_08_Making.md` A.3 L60-99 and 8f F.1-F.2 L389-414 | Which origin clusters carry preservation practices; the starting stock named | Cluster composition | Significant rows Japan 9.40, Germany 8.75, Sinian Federation 5.45 (`Spec` L93-95); Notable rows as in `SNH-012` |
| SNH-C5 | `04_Phase_04_Ordinary_Life.md` L52-53, L94, L202; `04_Phase_08_Making.md` L30; `04_Phase_09_Populations.md` L190 | The figure given for unclaimed working life | Free share of the workforce | 30.5% (`16` L1840, the governing split; `SNH-004`) |
| SNH-U1 | `00_Frame.md` L37, L88, L98; the line-3 header of `04_Phase_02`, `_03`, `_04`, `_05`, `_06`, `_08`, `_09` and `_10`; `04_Phase_02_Composition_and_Arrival.md` L47; `04_Phase_04_Ordinary_Life.md` L168; `09_Record.md` L11 | The population band the pass declares | Census totals against the band edge | Census I 1,014,533, Census II 835,341 (`SNH-001`); band edge: question 1 below |
| SNH-U2 | `04_Phase_08_Making.md` 8f L389-414 | Whether an origin language dominates or marks identity; the pass does not mention the national language | The language rule | `SNH-U2a` below |
| SNH-U3 | `00_Frame.md` L202-207; `05_Reconciliation.md` L57-85 | Station lineage treated as inadmissible; "the plant and not the roots" (`00_Frame.md` L207) | Rulings on inheriting from a station | `DR-25` (Rulings log L634): records, logs, journals, manifests, maps and infrastructure can be inherited, a tradition cannot. `DR-26` (L654), verbatim, 2026-10-01: *"it's perfectly possible for newcomers to inherit the research, equipment, techniques, results, etc. That doesn't need to get thrown away"*; not inheritable: a tradition, and the station's operator or nation as a reason for the city's founders, identity, culture or ties. |
| SNH-U4 | `04_Phase_05_Relation_and_Geometry.md` L136-140, L161-168, L225 | Where the city's imports come from | Port and transshipment listings | `Locations/Infrastructure/Ports.md` L130 and `Locations/Infrastructure/Neutral_Transshipment_Hubs.md` L60 list this city's cluster among the beneficiaries of the French Southern Lands and Heard Island transshipment, with indirect access to Australian and South African supply (developer ruling 2026-09-16); the Nella Fjord port row is `Ports.md` §5.6c. |

The language rule these rows cite (`SNH-U2a` of the 2026-11-03 note): Hawaiian (later Tepenian) is the dominant language everywhere; a city's supporting tier is every group within 12 points of its largest; for this city the largest is Korean (33.00%) and the next group (German, 10.06%) is 22.94 points below it, so the set is Korean alone (`Language_Blocs_By_City_2026-11-03.md` L1104-L1116).

---

# D. Questions that stay open (unchanged by this note)

The note of 2026-11-03 lists none open (its section 8). The band (Band 5 on Census I) and the use of `DR-24` to `DR-26` were settled by `DR-105` (the note's SNH-S05).

*Filed 2026-11-09. Read for this note: the note of 2026-11-03; the drift review `CITIES/Research_Logs/Drift_Review_Sinheung_2026-11-03.md`; the live lines named above; `LOG` `DR-105` to `DR-107`, `DR-117`, `DR-118`, `DR-122`.*

# E. Standing developer decisions from the walkthrough of 2026-11-09 (present tense; `DR-125`)

## SNH-021 — "Time that is your own"
**Developer, 2026-11-09:** *"specify what it actually means, in clear terms, so that future runs don't misinterpret it"*, then *"Yes, write it exactly so"*. **The phrase "time that is your own" means canon's leisure and nothing else.** For robots, leisure is a fact of life and is owed to nobody: hours that belong to nobody, so that a robot's freedom is real rather than granted, and a condition of staying sane (`ROBOT` L340-342, L356-361). For everyone, human and robot, there is the shared night, when all stop at the same time for different reasons (`ROBOT` L336). It does NOT mean the free tier (the 30.5% headcount of workers in work the city chose), it does NOT mean any share of a person's life is free, and it says nothing about human leisure beyond the night, which canon does not state.

## SNH-022 — The language of the frame
**Developer, 2026-11-09:** *"'Hawaiian' is a Pidgin between a primary base of English and Japanese, with a supporting base of Korean, Tagalog, Ilocano, and Mexican Spanish. Later in the future, further influence from a wide variety of languages) resulted in Hawaiian later becoming Tepenian."* Hawaiian and Tepenian are one language over time. Korean is both a supporting base of that language and this city's one supporting-tier language.

## SNH-023 — Wording rules for the amendment
The ruled label "East Asian cluster" stays, and its members (Korea, Japan, the Sinian Federation) are listed each time; "core" is not used. The Census I to II change is written as net counts ("remained in the count"), with the migration reading only as a labeled convention. The census redistribution in the spec's parentheticals is called "arithmetic redistribution". The exile measure is attached to no tier figure until the developer rules. The interim permission of the Census I ruling covers only its two named obligations. The Founding Register's figure governs every founding sentence. Only the admitted categories of what the exiles inherited are stated (plant, records, research, equipment, techniques); the real-world plant facts are comparables. The neutral transshipment arrangement is in force by the 2780s, its start left open, and the cluster's share lands directly at the fjord (conditional).
