# Halley — Datasheet · Step 0 & Phase 0 (Frame) — MERGED

> ⚠ **DRAFT — Tier C + Tier U.** Merged per the Field Guide's consolidation of Step 0 / Phase 0 (identical underlying facts). **Feeds `00_Frame.md` when Halley's own Step 0 runs.** It carries only what a source already states directly. 📎 *Files cited by line number here may carry a pointer to their copy in the `DerivationMechanisms` repo at the very END of the file (put there so no cited line moves): check the bottom of a cited file.*
> ⚠ **Ambiguous name:** the city and its subnet share the name; hits exclude `Halley subnet` phrases, but a line may still be about the subnet. Every row below that comes from a name search may be about something else with the same name (a person, a feature, the subnet); read the line.

> 📂 **MUST-OPEN coverage — Field Guide Rule 1 (spine, Phase 0), recounted by hand 2026-10-30:** **3 of 3** addresses are named in this sheet (2 directly, 1 through a shared Tier U sheet it cites).


| Category | Value | Citation |
|---|---|---|
| Census I | 721,889 H / 754,374 R / **1,476,263** combined (status cell: revised 2026-07-04) | `Official_Population_Census.md` L486 |
| Census II | 517,317 H / 586,599 R / **1,103,916** combined | `Official_Population_Census.md` L606 |
| Retention (computed; formula = Census II count ÷ Census I count) | combined 74.78% · human 71.66% · robot 77.76% | Computed from the two rows above: 1,103,916÷1,476,263 · 517,317÷721,889 · 586,599÷754,374 |
| Extent — required area at the band (table row; **2026-09-05 snapshot**, the census is live — note L631) | City: Halley · Subnet: Halley · Census I (snapshot): 1,452,345 · @10k: 145 km² · @7k: 207 km² · Site: Brunt ice shelf — MIGRATING | `Extent_and_Density_Per_City.md` L609 (header L603; snapshot note L631) |
| Extent at the live Census I (computed: population ÷ band) | 1,476,263 ÷ 10,000 = 147.6 km² · 1,476,263 ÷ 7,000 = 210.9 km² | Computed from `Official_Population_Census.md` L486 and the two bands of `Extent_and_Density_Per_City.md` L603 |
| **Temporal frame — the Second Interwar Period** | **2564–2812. 248 years, beginning at the Falkland Treaty.** The default frame for worldbuilding a Tepenian location; a corpus-wide constant, not a per-city judgment | ⭐ `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md`, in full |
| Act structure within the frame | Act 1: 2564 → somewhere in the 2600s (a hazy range, not yet dated) — national-ethnic-origin cultures still fresh. Act 2: by the late 2600s / early 2700s, onward — properly Tepenian; origin is ancestry, not identity | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` |
| The consolidating mechanism | Interconnection, decisively solidified by Amundsen Tower's completion (~2688) — not a switch, not the creation of unity, not the Tower's only effect | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` §"The consolidating mechanism" |
| **U** `Repo_Scope.md` | Tier U — corpus-wide boundary statement, fixed | — |
| Real-world basis | Halley Stations I–VI (UK), Brunt Ice Shelf, Coats Land, Weddell Sea (~75°35'S, 26°34'W) | `Specs/Halley.md` L3 |

**Not mechanical / not included here:** the Type + modifiers declaration, Band assignment, extent band, Status declaration, Configuration, generator selection, the asymmetry check on inherited material — none of this exists until Halley's own pass runs.
