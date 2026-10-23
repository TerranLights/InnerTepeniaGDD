# Datasheet and Pre-Trip coverage report — 2026-10-23 (before and after)

**Why this exists.** The earlier input audit (`City_Input_Audit_2026-10-21.md`) tested that files exist and are shaped correctly. It could not say whether a city's sheets contain what the ULM actually requires. This report does the test the Field Guide itself prescribes (**Rule 1**): for every phase, take each address in the spine's `MUST OPEN` list and check that the phase's datasheet covers it. Run by `Tools/check_must_open_coverage.py`; the parser was checked against the spine (Phase 7 yields 13 addresses, matching the Field Guide's own measurement for Davis). 31 cities: the 30 November cities plus Mirny.

## What was found, and what was done (2026-10-23)
**Before:** the Pre-Trip sheets were sound; the datasheets were not complete. 485 spine addresses were unmatched across 31 cities on the first (strict) pass, 191 once shared reference sheets were credited. **A correction to my first draft of this report:** I wrote that no datasheet recorded its coverage count. In fact the 26 Phase 7 sheets already carried a "MUST-OPEN coverage" row (counting addresses that exist on disk, not addresses the sheet names). The other ten phase sheets carried none.

**Done, city by city** with `Tools/complete_datasheets.py` (adds each missing row using the datasheet builder's own refusals: later-era content, comparisons and multi-city lists are not copied) and checked with `Tools/verify_city_sheets.py` (20 checks per city: 12 on the datasheets, 8 on the Pre-Trip):
1. **Every phase sheet now carries the Rule 1 coverage line** ("N of M addresses named; not covered: ...").
2. **Added rows, in spine order:** the universe repo's `Worldspace/Locations/` (Phases 1 and 5; mostly "checked, nothing for this city"), the Stations files (Phase 1: the airstrips table rows and the COMNAP catalogue page numbers), the SOC occupation data and the superseded-stamp for the Burden Model (Phase 7), and, for the older hand-built sets, the belief-transmission extractions, the cross-subnet file, Denison's missing Phase 5/6/7 items and the concept-art status.
3. **The Division-of-Industry citation gate** was added to the Phase 1 sheets (Phases 4 and 7 already had it).
4. **Ariun Nuur's Pre-Trip alias table was wrong** (it still called the city Vostok and said "no rename flagged"); corrected to the `DR-42` rename.
5. **Denison's Step 6** got its missing DRAFT mark.
6. **Quality fixes found by reading the added rows:** a multi-city list line (the universe README) was being copied: now excluded; commentary and comparison lines in the airstrips file are no longer copied (tables rows only); Scott's name pattern no longer matches "Amundsen–Scott"; the airstrips Country column carries a note that it is the station builder, an infrastructure fact only (`DR-19`, `DR-24`).

**After:** 30 of 30 November cities pass all 20 checks. **Mirny** passes the 12 datasheet checks but not the Pre-Trip structure checks: its Pre-Trip is the older hand-built layout, and its pass has already run, so it was left as is.

## Still open, needs a decision (not added; these are existing content)
- **Casey, Phase 7:** six rows read as conclusions or site history, not value + citation: "The geography is unusually load-bearing", "Why commercial 20% stays FREE" (including the real station's bar), "Additional notes from Casey's own §21" (characterization and the excavation incident), and the Sweep's "good models" row, which is a comparison. Rule 1b: a datasheet carrying a conclusion becomes pre-seeded output.
- **Denison, Step −1:** 11 lines carry later-era words ("Destroyed", "post-war", "destruction") the Field Guide forbids in a datasheet, even inside an explanation of what is excluded.
- **Casey, Phase 3:** a row quotes the spec's note about a pre-exile ruin near the city; the site's history is not an input (`DR-28`), though the Field Guide permits a real pre-exile ruin as a separate category. Your call.

## Raw output (after the fixes)
## Phase 0 — 3 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| U Repo_Scope.md (once per project) | `Repo_Scope.md` | 31 | 0 | 0 |
| U Timeline eras | `Timeline Eras` | 4 | 27 | 0 |
| P Official_Population_Census.md + location registries | `Official_Population_Census.md` | 31 | 0 | 0 |

## Phase 1 — 6 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| U Location canon | `Locations` | 31 | 0 | 0 |
| P Specs/ — incl. its closed-set Access type: token | `Specs` | 31 | 0 | 0 |
| P Energy_Grid_Failure_Rationale.md | `Energy_Grid_Failure_Rationale.md` | 31 | 0 | 0 |
| CLIMATE —  files are named for the REAL-WORLD STATION, not t | `READER` | 31 | 0 | 0 |
| Stations (physical and infrastructure facts only, DR-24; a s | `Stations` | 31 | 0 | 0 |
| 16_Per_City_Three_Tier_Run.md Half B — the G3 figures.  QUER | `16_Per_City_Three_Tier_Run.md` | 31 | 0 | 0 |

## Phase 2 — 3 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| U  No_National_Stereotypes.md — BINDING | `No_National_Stereotypes.md` | 31 | 0 | 0 |
| U Falkland Treaty — the founding instrument | `Falkland_Treaty` | 31 | 0 | 0 |
| P Official_Population_Census.md —  "diaspora/affinity files" | `Official_Population_Census.md` | 31 | 0 | 0 |

## Phase 3 — 5 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| P  Climate — alias-keyed | `READER` | 31 | 0 | 0 |
| P Specs/ | `Specs` | 31 | 0 | 0 |
| P Concept art  only 4 of the 38 cities hold images; the rest | `City_Concept-Art` | 31 | 0 | 0 |
| P Davis_Geosciences_Research/ where applicable | `Davis_Geosciences_Research` | 31 | 0 | 0 |
| _Physical_Infrastructure_Attributes.md live in City_Megashee | `City_Megasheets` | 31 | 0 | 0 |

## Phase 4 — 7 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| Robot_Physiology_and_Cultural_Practices.md — THE LARGEST SIN | `Robot_Physiology_and_Cultural_Practices.md` | 2 | 29 | 0 |
| Robot_Cold_Physiology.md —  the NARROW companion; read the f | `Robot_Cold_Physiology.md` | 30 | 1 | 0 |
| 16 Half B — baseline / mandated / FREE tiers | `16_Per_City_Three_Tier_Run.md` | 30 | 1 | 0 |
| 09 §3.5 — THE FREEDOM GRADIENT | `09_Per_City_Baseline_Run.md` | 31 | 0 | 0 |
| 11_Caloric_Rebuild_and_Livestock_Tier.md | `11_Caloric_Rebuild_and_Livestock_Tier.md` | 31 | 0 | 0 |
| National_Medical_and_Care_Institutes.md (locked-canon) | `National_Medical_and_Care_Institutes.md` | 31 | 0 | 0 |
| P National_Economy_and_Currency.md | `National_Economy_and_Currency.md` | 4 | 27 | 0 |

## Phase 5 — 6 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| U Location canon + routes | `Locations` | 31 | 0 | 0 |
| P Highways.md | `Highways.md` | 31 | 0 | 0 |
| P Airports.md ·  Ports.md ·  Geothermal_Heating.md | `Infrastructure` | 31 | 0 | 0 |
| P City_Cross_Subnet_Relationships.md | `City_Cross_Subnet_Relationships.md` | 31 | 0 | 0 |
| P City_Relationship_Database.md | `City_Relationship_Database.md` | 31 | 0 | 0 |
| P City_National_Connections.md | `City_National_Connections.md` | 31 | 0 | 0 |

## Phase 6 — 5 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| Robot religions — CHECK BEFORE INVENTING A BELIEF.  THE ROST | `Robot_Religions` | 31 | 0 | 0 |
| National_Holidays.md | `National_Holidays.md` | 31 | 0 | 0 |
| Ice-Cold_Buddhism_Research/ (7 files)  the faith's name is a | `Ice-Cold_Buddhism_Research` | 31 | 0 | 0 |
| The_True_Believer_Extraction.md · The_Meme_Machine_Extractio | `The_True_Believer_Extraction.md` | 31 | 0 | 0 |
| The_True_Believer_Extraction.md · The_Meme_Machine_Extractio | `The_Meme_Machine_Extraction.md` | 31 | 0 | 0 |

## Phase 7 — 13 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| Division_of_Industry/ — PRIMARY for 7a; strongest G3 supply  | `Division_of_Industry` | 29 | 2 | 0 |
| Figures — 16 Half B | `16_Per_City_Three_Tier_Run.md` | 31 | 0 | 0 |
| Gaps — Division_of_Industry_Sweep_2026-08-31.md §4.4 | `Division_of_Industry_Sweep_2026-08-31.md` | 31 | 0 | 0 |
| Inputs — 01_Burden_Scoring_Model.md | `01_Burden_Scoring_Model.md` | 31 | 0 | 0 |
| Inputs — 08_Volume_Based_Requirement_Reference.md | `08_Volume_Based_Requirement_Reference.md` | 8 | 23 | 0 |
| National_Medical_and_Care_Institutes.md | `National_Medical_and_Care_Institutes.md` | 4 | 27 | 0 |
| Theoretical-Calculations/ | `Theoretical-Calculations` | 31 | 0 | 0 |
| Industry_Staffing_and_Productivity/ —  SOC tier-marking is A | `Industry_Staffing_and_Productivity` | 31 | 0 | 0 |
| jobs_professions_and_fields/ (SOC) | `jobs_professions_and_fields` | 31 | 0 | 0 |
| P National_Economy_and_Currency.md | `National_Economy_and_Currency.md` | 6 | 25 | 0 |
| P City_Logistics.md  Scoped to one named city; only its DUAL | `City_Logistics.md` | 31 | 0 | 0 |
| P Factions/ — the 7d canon check (existing countercultures a | `Factions` | 31 | 0 | 0 |
| U Megacorps/ | `Megacorps` | 31 | 0 | 0 |

## Phase 8 — 2 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| MANDATORY before ANY siligel / coolant / Glitch-Coolant clai | `Robot_Biology_and_Culture` | 30 | 1 | 0 |
| Weapons_and_Tools_Philosophy.md, gear catalogs, slang | `Weapons_and_Tools_Philosophy.md` | 31 | 0 | 0 |

## Phase 9 — 4 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| U  Laws_of_Robotics.md — binding | `Laws_of_Robotics.md` | 31 | 0 | 0 |
| U  Robot_Universals/ —  Ch. 13 (city as seat of identity) ·  | `Robot_Universals` | 31 | 0 | 0 |
| U Doll_Representation_Categories.md | `Doll_Representation_Categories.md` | 31 | 0 | 0 |
| P human-robot relations baseline | `Robot_Physiology_and_Cultural_Practices.md` | 0 | 31 | 0 |

## Phase 10 — 3 required addresses
| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |
|---|---|--:|--:|--:|
| U Characters canon | `Characters` | 31 | 0 | 0 |
| P Enneagram_Character_Index.md | `Enneagram_Character_Index.md` | 31 | 0 | 0 |
| Zodiac Lens — Zodiac_Signs_Full_Attributes.md (the technique | `Zodiac_Signs_Full_Attributes.md` | 31 | 0 | 0 |

## Does any datasheet record a coverage count, as the Field Guide requires?
341 of 341 (city, phase) datasheets carry one.

## Per city: required items its datasheets do not name
### Byrd — 0 gaps
### Santa Luce — 0 gaps
### Belgrano — 0 gaps
### Halley — 0 gaps
### Lazar — 0 gaps
### Neumayer — 0 gaps
### Utstein — 0 gaps
### Sanay — 0 gaps
### Troll — 0 gaps
### Cape Adare — 0 gaps
### Fort McMurdo — 0 gaps
### Janbogo — 0 gaps
### Scott — 0 gaps
### Zukelli — 0 gaps
### Dome Fuji — 0 gaps
### Mawson — 0 gaps
### Temirotkel — 0 gaps
### Esperanza — 0 gaps
### Pergamino — 0 gaps
### Marambio — 0 gaps
### Palmer City — 0 gaps
### Puerto Abrigo — 0 gaps
### Rothera — 0 gaps
### Contrapunto — 0 gaps
### Signy — 0 gaps
### Casey — 0 gaps
### Kunlun — 0 gaps
### Mirny — 0 gaps
### Denison — 0 gaps
### Dumont d'Urville — 0 gaps
### Ariun Nuur — 0 gaps

## Pre-Trip checks
| City | step blocks (of 11) | phase 'governing' lines (of 11) | phase T8 lines (of 11) | sections present | spine addresses absent from section D |
|---|--:|--:|--:|---|---|
| Byrd | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Santa Luce | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Belgrano | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Halley | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Lazar | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Neumayer | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Utstein | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Sanay | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Troll | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Cape Adare | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Fort McMurdo | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Janbogo | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Scott | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Zukelli | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Dome Fuji | 12 | 11 | 11 | ABCDEFGHIJKLMN | none |
| Mawson | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Temirotkel | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Esperanza | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Pergamino | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Marambio | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Palmer City | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Puerto Abrigo | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Rothera | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Contrapunto | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Signy | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Casey | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Kunlun | 12 | 11 | 11 | ABCDEFGHIJKLMN | none |
| Mirny | 0 | 0 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research, P5 Infrastructure, P6 The_True_Believer_Extraction.md, P6 The_Meme_Machine_Extraction.md, P7 01_Burden_Scoring_Model.md, P7 08_Volume_Based_Requirement_Reference.md |
| Denison | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Dumont d'Urville | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
| Ariun Nuur | 12 | 11 | 11 | ABCDEFGHIJKLMN | P3 Davis_Geosciences_Research |
