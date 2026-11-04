# Mawson — Datasheet · Step 0 & Phase 0 (Frame) — MERGED

> ⚠ **DRAFT — Tier C + Tier U.** Merged per the Field Guide's consolidation of Step 0 / Phase 0 (identical underlying facts). **Feeds `00_Frame.md` when Mawson's own Step 0 runs.** It carries only what a source already states directly. 📎 *Files cited by line number here may carry a pointer to their copy in the `DerivationMechanisms` repo at the very END of the file (put there so no cited line moves): check the bottom of a cited file.*
> ⚠ **Ambiguous name:** the city and its subnet share the name; hits exclude `Mawson subnet` phrases, but a line may still be about the subnet. Every row below that comes from a name search may be about something else with the same name (a person, a feature, the subnet); read the line.

> 📂 **MUST-OPEN coverage — Field Guide Rule 1 (spine, Phase 0), recounted by hand 2026-10-30:** **3 of 3** addresses are named in this sheet (2 directly, 1 through a shared Tier U sheet it cites).


| Category | Value | Citation |
|---|---|---|
| Census I | 736,799 H / 762,053 R / **1,498,852** combined (status cell: revised 2026-07-04) | `Official_Population_Census.md` L499 |
| Census II | 443,999 H / 544,326 R / **988,325** combined | `Official_Population_Census.md` L645 |
| Retention (computed; formula = Census II count ÷ Census I count) | combined 65.94% · human 60.26% · robot 71.43% | Computed from the two rows above: 988,325÷1,498,852 · 443,999÷736,799 · 544,326÷762,053 |
| **Extent (2026-09-05 snapshot; the census is live — note L631):** Mawson · Subnet Mawson | Census I (snapshot) 1,446,733 · @10k 145 km² · @7k 207 km² · Site Holme Bay | `Extent_and_Density_Per_City.md` L610 (table header L603; snapshot note L631) |
| **Extent at the live Census I (computed)** | @10k 147.1 km² · @7k 210.1 km² | Computed from the Census I row above: 1,498,852÷10,000 = 147.07 · 1,498,852÷7,000 = 210.09 (the table's `@10k` / `@7k` columns, L603) |
| **Temporal frame — the Second Interwar Period** | **2564–2812. 248 years, beginning at the Falkland Treaty.** The default frame for worldbuilding a Tepenian location; a corpus-wide constant, not a per-city judgment | ⭐ `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md`, in full |
| Act structure within the frame | Act 1: 2564 → somewhere in the 2600s (a hazy range, not yet dated) — national-ethnic-origin cultures still fresh. Act 2: by the late 2600s / early 2700s, onward — properly Tepenian; origin is ancestry, not identity | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` |
| The consolidating mechanism | Interconnection, decisively solidified by Amundsen Tower's completion (~2688) — not a switch, not the creation of unity, not the Tower's only effect | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` §"The consolidating mechanism" |
| **U** `Repo_Scope.md` | Tier U — corpus-wide boundary statement, fixed | — |
| Real-world basis | Mawson Station (Australia / Australian Antarctic Division), Horseshoe Harbor, Holme Bay, Mac.Robertson Land (~67°36'S, 62°53'E) | `Specs/Mawson.md` L3 |
| **Language** (set 2026-11-03) | Hawaiian (later Tepenian) is the dominant language. **Supporting tier: English, Mandarin, Indonesian, Japanese** — a language not dominant but widely enough understood that business, social talk and general dealings can be done in it; the set is every language group within 12 percentage points of the city's largest group (range mid-points; nations sharing a language summed). Largest group: English 13.2–16.1. Other groups within 12 points: Mandarin 8.9–9.7, Indonesian 8.7–8.9, Japanese 8.5. Mawson is a special case: its largest group is only 13.2–16.1 and the 12-point rule would admit 13 languages, so the developer named these four (option A, 2026-11-03); Russian and the smaller languages are not counted. *These are shares of residents whose national origin is a nation of that language, not counts of speakers; the mapping of nations to languages is recalled general knowledge, not verified.* | `Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` (12-point addendum and rulings); `Research_Logs/Language_Blocs_By_City_2026-11-03.md` |

**Not mechanical / not included here:** the Type + modifiers declaration, Band assignment, extent band, Status declaration, Configuration, generator selection, the asymmetry check on inherited material — none of this exists until Mawson's own pass runs.
