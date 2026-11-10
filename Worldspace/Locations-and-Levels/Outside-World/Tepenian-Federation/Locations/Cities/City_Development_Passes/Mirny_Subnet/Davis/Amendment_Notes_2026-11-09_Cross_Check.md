# Davis: amendment note for the 2026-11-09 cross-check

**What this is.** A dated amendment note, written at the start of the finished-city cross-check of 2026-11-09 (`DR-106`, `DR-104` item 3). It states what is true now in the sources Davis's pass rests on, checked against the live files on 2026-11-09 between 05:03 and 05:30. It sits beside `Amendment_Notes_2026-10-30_Manual_Input_Audit.md` (the note of 2026-11-03, entries DV-001 to DV-030 and its section F), which stays in place; where this note gives a newer fact or address, this note governs. **No pass file was edited. Everything here is PROPOSED** (`DR-101`, `DR-102`). Entries state the current fact with its source address, not what a text used to say (`DR-102`).

**IDs.** New entries are DV-031 and up. Older IDs keep their numbers.

**Names.** This note names no other city. Where a source line names one, the line is cited by address and described neutrally ("another location: not used").

`CITIES` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`. `ULM` = `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`. `SPEC` = `CITIES/Specs/Mirny subnet/Davis.md`. `CENSUS` = `CITIES/Official_Population_Census.md`. `LOG` = `ULM/DEVELOPER_RULINGS_LOG.md`. `DOI` = `CITIES/Division_of_Industry/`. `PASS` = `CITIES/City_Development_Passes/Mirny_Subnet/Davis/`.

---

# A. The note of 2026-11-03, checked against the live files

## DV-031 — Result of the check

**Command.** `python3 -I verify_davis_note.py` (the script is a read-only check: 55 line checks, each requiring named strings on a named line, then a recomputation of every derived figure in DV-001, DV-006, DV-021 and DV-030; it prints OK or DIFF and never prints another location's text). Script and output are kept in the session scratchpad and copied beside this note as `.verify_davis_note_2026-11-09.py` and `.verify_davis_note_2026-11-09_output.txt`.

**Result.** 55 of 55 line checks OK, 0 DIFF. Every figure in DV-001, DV-006, DV-021, DV-025 and DV-030 reproduces. The raw output, whole:

```
OK       Official_Population_Census.md L506
OK       Official_Population_Census.md L650
OK       Official_Population_Census.md L394
OK       Official_Population_Census.md L395
OK       Davis.md L15
OK       Davis.md L16
OK       Davis.md L20
OK       Davis.md L21
OK       Davis.md L32
OK       Davis.md L33
OK       Davis.md L37
OK       Davis.md L38
OK       Davis.md L49
OK       Davis.md L76
OK       Davis.md L99
OK       Davis.md L100
OK       Davis.md L107
OK       Davis.md L108
OK       Davis.md L109
OK       Founding_Register.md L59
OK       09_Per_City_Baseline_Run.md L79
OK       16_Per_City_Three_Tier_Run.md L262
OK       16_Per_City_Three_Tier_Run.md L2006
OK       16_Per_City_Three_Tier_Run.md L2010
OK       16_Per_City_Three_Tier_Run.md L2011
OK       16_Per_City_Three_Tier_Run.md L2012
OK       16_Per_City_Three_Tier_Run.md L2014
OK       16_Per_City_Three_Tier_Run.md L2022
OK       16_Per_City_Three_Tier_Run.md L2074
OK       16_Per_City_Three_Tier_Run.md L2076
OK       16_Per_City_Three_Tier_Run.md L3568
OK       19_National_Balance_Refresh_2026-11-02.md L62
OK       19_National_Balance_Refresh_2026-11-02.md L81
OK       Highways.md L199
OK       Ports.md L559
OK       Airports.md L50
OK       Airports.md L55
OK       Airports.md L57
OK       City_National_Connections.md L303
OK       City_National_Connections.md L304
OK       City_National_Connections.md L307
OK       City_National_Connections.md L308
OK       Language_Blocs_By_City_2026-11-03.md L916
OK       Language_Blocs_By_City_2026-11-03.md L922
OK       Language_Blocs_By_City_2026-11-03.md L923
OK       Language_Blocs_By_City_2026-11-03.md L925
OK       Language_Blocs_By_City_2026-11-03.md L926
OK       Language_Blocs_By_City_2026-11-03.md L927
OK       Extent_and_Density_Per_City.md L617
OK       Extent_and_Density_Per_City.md L636
OK       City_Symbol_Assignments.md L112
OK       DEVELOPER_RULINGS_LOG.md L1555
OK       DEVELOPER_RULINGS_LOG.md L1660
OK       DEVELOPER_RULINGS_LOG.md L1698
OK       README.md L22
TOTAL line checks: 55   OK: 55   DIFF: 0
composition table rows parsed (L32-L76): 45; by tier: {'Primary': 5, 'Significant': 2, 'Notable': 38}
share sum: 100.004%
rows under 1%: 21; under 0.5%: 17; under 0.1%: 10
Census I sum over rows: 1210432
four smallest rows at Census I: [('Tuva', 152), ('Karachay-Cherkessia', 212), ('Ingushetia', 230), ('Finland', 240)]
Census I 1210432, Census II 817475
retention combined 67.54%, humans 76.88%, robots 58.63%, spread 18.25 pp
robots share of Census I 51.20%, of Census II 44.45%
humans departed 136567 = 23.12%; robots departed 256390 = 41.37%; people gone 392957
density on 410 km2: Census I 2952.27, Census II 1993.84
workforce 915098 (robots + humans/2); required 323,548 / 915,098 = 35.36%
file 16 section 19: 383,295 + 252,606 + 279,197 = 915098; mandated 27.60%, free 30.51%
agriculture 35% of 531,803 = 186131.05; technical half 12.5% = 66475.38
retention in climate: 28/72.8 = 38.46%; 28/73 = 38.36%
```

**What the check does not cover.** Line checks test named strings on named lines; they do not re-read the surrounding text. The spec line numbers in the pass files (the +24 shift, DV-024) were not re-checked here. The relationship passages in DV-S02 were checked only at the lines listed above.

---

# B. What changed since the note of 2026-11-03 (filed 22:34)

One commit touched Davis's source files after the note was filed: `8777bb5f` (2026-11-03 23:03, `DR-105`). One uncommitted change is in the symbol file; its diff has no Davis line (checked by command), and Davis's row at `CITIES/City_Symbolic_Substrate/City_Symbol_Assignments.md` L112 is unchanged.

## DV-032 — The census tag sentence

`CENSUS` L33 now reads: where a nation is named as a city's founder in `Founding_Register.md`, its row carries the tag "(founding wave)"; the tag says nothing about when people arrived. This is the meaning `DR-88` (`LOG` L1555) and `DR-99` (`LOG` L1660) give, and the edit is recorded as applied at `LOG` L1661 (the "Applied" row of `DR-99`, 2026-11-03 night). Davis's tag stands on Australia only (`SPEC` L21, L38; `CENSUS` L395); Davis's Register row is `CITIES/Founding_Register.md` L59 (unchanged, checked in DV-031). The statement in DV-023 that `CENSUS` L33 "describes the tag as a nation that set the city's early character before larger communities arrived" is replaced by this one.

## DV-033 — The Register's row for another location and the relationship database's line for it

`DR-99` applied an edit to `Founding_Register.md` (the row of another location, L57) and to a line of `City_Relationship_Database.md` (the same other location). Another location: not used. Davis's own relation lines are unchanged (`City_National_Connections.md` L303–308 checked in DV-031; `City_Relationship_Database.md` L186–193 and `City_Cross_Subnet_Relationships.md` L121–147 unchanged since 2026-11-03). The statement in DV-S02 and in section I of the note of 2026-11-03 that these edits "await the developer's word" is replaced by: they are applied (`LOG` `DR-99`, "Applied" row).

## DV-034 — The character draft sited in Davis

`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/TBN [STP-06 thicc Chinese Hao]/README.md` was edited in the commit above (`DR-105` item 5: the two quotations brought to today's facts). Current text: L22 names Davis, Tepenian Federation, with its subnet, as her present-day primary location; L44–45 state that Davis's composition has the Sinian Federation as one of its five Primary origins and that Davis's founder, per the Founding Register, is Australia. The China share of 20.51% and the "China-Primary founding tier" that DV-029 cites at L44–47 are no longer in those lines. DV-029 is replaced by this entry. The pass location (`04_Phase_10` L499–503, "character canon returns nothing for Davis") is unchanged.

## DV-035 — Rulings and rules that bear on this run, in the present tense

| Ruling | What it says now | Address in `LOG` |
|---|---|---|
| `DR-105` item 4 | A re-derivation uses the rulings as they stand. | L1707–1712 |
| `DR-105` item 5 | Davis's symbol pair stays blank until Davis's own Phase 10 (`DR-8`, `DR-8a`). | L1712 |
| `DR-106` | The finished cities are reviewed before the new runs; the plan for each is `DR-104` item 3. | L1719–1726 |
| `DR-107` item 2 | A piece that needs another piece's result does not start until that result is complete and confirmed. | L1728–1735 |
| `DR-117` items 1, 2, 4 | "Confirmed" means written to file; a reader may repair a single failed PROOF field in its own output; edits and confirmation sessions run at any hour; the derivation itself runs 05:00–14:59. | L1818–1825 |
| `DR-118` item 2 | The amendment-layer rules are in `ULM/Amendment_Layer_Rules.md`. | L1827–1834 |
| `DR-122` item 5 | A single location's run takes a relation only from its own lines. | L1863–1870 |

## DV-036 — Line-number conversions for citations inside the pass

**Spec citations.** A spec line cited in the pass at pass-cited number n, for n from 58 to 236, is current line n + 24 (L82 to L260). This was checked by comparing the text of every one of those 179 lines with the text 24 lines later (`git show d2dd2136:<spec>` against the live spec): 176 are identical. The three whose wording changed are pass-cited L85, L89 and L143 (now L109, L113 and L167); L8 changed at the same number. The composition region (pass-cited L13 to L57) is replaced by current L13 to L81 and has no mapping. The comparison and the mapped numbers for every line the Step −1 contract names are at `PASS/.t8_S1_spec_numbering_map.txt`. The pass files cite the spec in both numberings (DV-024); the +24 rule resolves either.

**Census citations.** Davis's tier table in `CENSUS` is at L390 (heading) to L396; the Census I and Census II rows are L506 and L650 (pass-cited 392–398, 496 and 613).

**Other files whose size the pass records.** `No_National_Stereotypes.md` has 174 lines (the pass records 172; its line citations into that file are two lower than the file's, for example the disambiguation the pass cites at L30 is at L32). `02_Spine.md` has 584 lines (the pass records 585). Both counts checked by `wc -l`, 2026-11-09.

---

# C. Section F restated at the current values

Pass location, the input it rests on, and that input's current value and address. No verdict is given here; verdicts come from the checks written to `Amendment_Checks_2026-11-09_SectionF.md`. Rows C-1 and U-3 changed since the note of 2026-11-03 (DV-032, DV-034).

| # | Pass location (topic) | Input | Current value and address |
|---|---|---|---|
| C-1 | `04_Phase_02` H-2 (L224–258), A.2 closing (L324–331), A.3 (L334–345), B.4 (L583–636), L1400, L1598; `02_Spine.md` L250; `01_Inherited.md` L70 (the contrast between the founding stock and the plurality stock, and the reading of the "(founding wave)" tag) | What the tag means; who is largest | Tag: `CENSUS` L33, `LOG` L1555, L1660 (DV-032); Register `CITIES/Founding_Register.md` L59; Australia 5.74% (`SPEC` L38), Japan 10.42% (L32), Sinian Federation 9.72% (L33) |
| C-2 | `04_Phase_02` C.2 (L939–950), C.3 (L953–976), C.5 (L1012–1021), L1448, L1482 (the scale check on origin communities and the rich-internal-layer conclusion) | Number and size of origin rows | 45 rows; 10 under 0.1% (152 to 1,162 people); 17 under 0.5%; 21 under 1% (`SPEC` L32–76); regional and successor names explained at `CENSUS` Section E; all 45 rows are origins, reasoned by headcount with no cutoff (`LOG` `DR-104`, L1698–1705) |
| C-3 | `04_Phase_02` E.1 (L1060–1081) (the origins as a sample of the places robots occupied) | The list of origins | Rows at `SPEC` L32–76, including Taiwan (L43), Kazakhstan (L51), Manchuria (L57), Mongolia (L60), East Turkestan (L62), Tibet (L70) |
| C-4 | `01_Inherited.md` L87–88, L274; `04_Phase_02` L50, L318–320, L324; `02_Spine.md` L116–118 (the seal on comparing nations' figures and its stated ground) | How the figures are produced | `SPEC` L28 and L78 (DV-022); `LOG` L463–474 (`DR-12`); `LOG` L1523 (`DR-85`); the bar stays on its first ground (DV-S03, `LOG` `DR-104` item 1) |
| C-5 | `04_Phase_05` L35–36, L303–306, L330, L346, L383–386 (heritage relations treated as excluded for want of an independent route) | What Davis's own relation lines rest on | `City_National_Connections.md` L303–315; `City_Relationship_Database.md` L186–193; `City_Cross_Subnet_Relationships.md` L121–147 (L125–126 cites a withheld source, DV-004); Hwy 110 `Highways.md` L199; Register `Founding_Register.md` L59. Relation facts come only from Davis's own lines (`LOG` `DR-122` item 5) |
| C-6 | `04_Phase_08` L241–250, L320; `04_Phase_09` L92 (what any community speaks; the dominant local layer; the marker of belonging) | The language rule | DV-025: Hawaiian (later Tepenian) is the national language (`LOG` `DR-100`, L1664–1672); Davis's supporting set is English, Mandarin, Japanese, German (`Research_Logs/Language_Blocs_By_City_2026-11-03.md` L916–930) |
| C-7 | `02_Spine.md` L107, L116–118; `04_Phase_02` A.4 (L347–363), B.2 chain (L461–476) (nothing load-bearing can be tacit, given the number of origins and the largest share) | Number of rows; largest share | 45 rows; largest 10.42% (`SPEC` L32) |
| U-1 | `04_Phase_07` A.2 (L102–123), A.2b (L125–138), L407; `05_Reconciliation.md` L102–110 (the export headcount that the pass declines to state) | The national food files | DV-007: 44.2% of export supply (`DOI` `19` L81); file 19's latest run gives Davis's farm workforce as 186,131 (L62); `DOI` `16` L2091–2094 states the whole-workforce comparison; file 04 §3 still states 306,780 |
| U-2 | `02_Spine.md` L90–101, L158–182; `04_Phase_02` L708–743 (what crossed the founding gap) | The inheritance rules | `LOG` L623–660 (`DR-24`, `DR-25`, `DR-26`); `No_National_Stereotypes.md` L21 (DV-026); `DOI` `README.md` L3–7 |
| U-3 | `04_Phase_10` L499–503 (no figure sited in Davis) | Character drafts | DV-034 |
| U-4 | `00.1` §4 (L205–286), `00.1a` (the composition region of the contract) | The spec's composition block | `SPEC` L13–78 (DV-005) |
| U-5 | `05_Reconciliation.md` (whole; the check files) | The check files' text | DV-028 |

---

# D. Source defects found while writing this note

1. **The reader-list generator writes a source the Pre-Trip marks forbidden.** Davis's Pre-Trip is correct: its Phase 2 table row (`00.0_Pre-Trip_Inspection.md` L277) marks `CITIES/City_Refugee_District_Affinities.md` "⛔ RESOLVES TO NOTHING ADMISSIBLE" (it maps cities to the districts of another location; `00_RUNBOOK.md` §C.8c Phase 2 row L1974, `§C.8d`, the law of one location), and its Phase 2 T8 line names five admissible rows that do not include it. `Tools/make_t8_required_list.py phase:2` nevertheless wrote the path into the draft list as an entry, because it extracts every backticked absolute path from the phase's table rows without reading the ⛔ marker. The file is excluded from every list in this run and is not read. Checked by command 2026-11-09 (`make_t8_required_list.py`, last changed 2026-10-21, no uncommitted edits to the tool). The tool is not edited here; the fix is a decision for the developer (DEC-280).
2. `SPEC` L8 still describes the Australian founding-wave heritage as shared with two other locations by name (DV-004 stands). Another location: not used.
3. `City_Cross_Subnet_Relationships.md` L125–126 still cites a withheld culture file (DV-004 stands).

---

# E. Questions that stay open (unchanged by this note)

1. **The climate class.** Ice-free oasis (`SPEC` L107) or katabatic margin (`Precipitation_Falls_vs_Lands.md` L163); 28 mm staying and about 38% retention are in use (`DR-104` item 4). Left open by the developer; this run records it as a question and does not decide it.
2. **The symbol pair.** Blank until Davis's own Phase 10 (`DR-105` item 5).
3. **The end-of-pass review of Davis's split** (`DOI` `16` L3568).
4. **The winter-intake island** and **the national food denominator** (section I of the note of 2026-11-03).

---

*Filed 2026-11-09. Read for this note: the note of 2026-11-03; the drift review `CITIES/Research_Logs/Drift_Review_Davis_2026-11-03.md`; the live lines named above; `LOG` `DR-100` to `DR-107`, `DR-111`, `DR-113`, `DR-116` to `DR-118`, `DR-122`.*
