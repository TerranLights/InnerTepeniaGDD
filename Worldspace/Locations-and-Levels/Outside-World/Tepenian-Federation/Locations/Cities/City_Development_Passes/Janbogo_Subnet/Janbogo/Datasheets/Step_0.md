# Janbogo — Datasheet · Step 0 & Phase 0 (Frame) — MERGED

> ⚠ **DRAFT — Tier C + Tier U.** Merged per the Field Guide's consolidation of Step 0 / Phase 0 (identical underlying facts). **Feeds `00_Frame.md` when Janbogo's own Step 0 runs.** It carries only what a source already states directly. 📎 *Files cited by line number here may carry a pointer to their copy in the `DerivationMechanisms` repo at the very END of the file (put there so no cited line moves): check the bottom of a cited file.*
> ⚠ **Ambiguous name:** the city and its subnet share the name; hits exclude `Janbogo subnet` phrases, but a line may still be about the subnet. Every row below that comes from a name search may be about something else with the same name (a person, a feature, the subnet); read the line.

> 📂 **MUST-OPEN coverage — Field Guide Rule 1 (spine, Phase 0), recounted by hand 2026-10-30:** **3 of 3** addresses are named in this sheet (2 directly, 1 through a shared Tier U sheet it cites).


| Category | Value | Citation |
|---|---|---|
| Census I | 673,610 H / 689,019 R / **1,362,629** combined (status cell: revised 2026-07-04) | `Official_Population_Census.md` L501 |
| Census II | 507,242 H / 486,208 R / **993,450** combined (status cell: revised 2026-07-03) | `Official_Population_Census.md` L644 |
| Retention (computed; formula = Census II count ÷ Census I count) | combined 72.91% · human 75.30% · robot 70.57% | Computed from the two rows above: 993,450÷1,362,629 · 507,242÷673,610 · 486,208÷689,019 |
| `Extent_and_Density_Per_City.md` — the city's own row *(2026-09-05 snapshot; the census is live — note L631)* | City: Janbogo · Subnet: Janbogo · Census I: 1,310,511 · @10k: 131 · @7k: 187 *(km² required at 10,000 and at 7,000 people per km²)* · Site: Terra Nova Bay | `Extent_and_Density_Per_City.md` L612 (table header L603–L604; the band, L84) |
| ↳ same file, at the live Census I (computed) | 1,362,629÷10,000 = 133.4 km² · 1,362,629÷7,000 = 190.6 km² | Computed from `Official_Population_Census.md` L501 and the band at `Extent_and_Density_Per_City.md` L84 |
| ↳ same file — the bay shared with a second city *(2026-09-05 snapshot)* | Terra Nova Bay carries two: Janbogo + Zukelli = 2,569,162, needing 257–367 km² on the Northern Foothills | `Extent_and_Density_Per_City.md` L598 |
| ↳ same file — other lines naming the city *(table rows whose Subnet column reads Janbogo; line numbers only)* | — | `Extent_and_Density_Per_City.md` L607, L614, L622 |
| **Temporal frame — the Second Interwar Period** | **2564–2812. 248 years, beginning at the Falkland Treaty.** The default frame for worldbuilding a Tepenian location; a corpus-wide constant, not a per-city judgment | ⭐ `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md`, in full |
| Act structure within the frame | Act 1: 2564 → somewhere in the 2600s (a hazy range, not yet dated) — national-ethnic-origin cultures still fresh. Act 2: by the late 2600s / early 2700s, onward — properly Tepenian; origin is ancestry, not identity | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` |
| The consolidating mechanism | Interconnection, decisively solidified by Amundsen Tower's completion (~2688) — not a switch, not the creation of unity, not the Tower's only effect | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` §"The consolidating mechanism" |
| **U** `Repo_Scope.md` | Tier U — corpus-wide boundary statement, fixed | — |
| Real-world basis | Jang Bogo Station (Unified Korea), Terra Nova Bay, Ross Sea (~74°37'S, 164°13'E) | `Specs/Janbogo.md` L3 |

**Not mechanical / not included here:** the Type + modifiers declaration, Band assignment, extent band, Status declaration, Configuration, generator selection, the asymmetry check on inherited material — none of this exists until Janbogo's own pass runs.
