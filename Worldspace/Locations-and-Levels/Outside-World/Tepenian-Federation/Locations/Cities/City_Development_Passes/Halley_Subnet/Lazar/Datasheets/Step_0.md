# Lazar — Datasheet · Step 0 & Phase 0 (Frame) — MERGED

> ⚠ **DRAFT — Tier C + Tier U.** Merged per the Field Guide's consolidation of Step 0 / Phase 0 (identical underlying facts). **Feeds `00_Frame.md` when Lazar's own Step 0 runs.** It carries only what a source already states directly. 📎 *Files cited by line number here may carry a pointer to their copy in the `DerivationMechanisms` repo at the very END of the file (put there so no cited line moves): check the bottom of a cited file.*

> 📂 **MUST-OPEN coverage — Field Guide Rule 1 (spine, Phase 0), recounted by hand 2026-10-30:** **3 of 3** addresses are named in this sheet (2 directly, 1 through a shared Tier U sheet it cites).


| Category | Value | Citation |
|---|---|---|
| Census I | 1,170,443 H / 1,211,762 R / **2,382,205** combined *(a long status cell is present: an authoring note, not copied)* | `Official_Population_Census.md` L482 |
| Census II | 783,193 H / 856,233 R / **1,639,426** combined *(a long status cell is present: an authoring note, not copied)* | `Official_Population_Census.md` L604 |
| Retention (computed; formula = Census II count ÷ Census I count) | combined 68.82% · human 66.91% · robot 70.66% | Computed from the two rows above: 1,639,426÷2,382,205 · 783,193÷1,170,443 · 856,233÷1,211,762 |
| Extent table — the city's row (the table is titled *"required area at the band"*; columns: City · Subnet · Census I · @10k · @7k · Site) | Lazar · Halley · 2,620,319 · 262 · 374 · Schirmacher Oasis ~34 km² | `Extent_and_Density_Per_City.md` L605 (title L601, header L603) — 2026-09-05 snapshot; the census is live — note L631 |
| Extent — the −10% discharge row (columns: Source · Why reduced · Census I · Census II) | Lazar · **−10%** — *34 km² of Schirmacher carrying **87–91% of the city on ice*** · **262,032** · **180,398** | `Extent_and_Density_Per_City.md` L654 (header L649) — 2026-09-05 snapshot; the census is live — note L631 |
| Required area at the live Census I (computed; formula = Census I ÷ the table's band density, 10,000/km² and 7,000/km²) | 2,382,205÷10,000 = 238.2 km² · 2,382,205÷7,000 = 340.3 km² | Computed from the Census I row above and the @10k / @7k columns of `Extent_and_Density_Per_City.md` L603 |
| ↳ other lines naming the city | *[source lines are a multi-city list, a comparison, and another city's founding rule; not copied, line numbers recorded only]* | `Extent_and_Density_Per_City.md` L577, L593, L683 — 2026-09-05 snapshot; the census is live — note L631 |
| **Temporal frame — the Second Interwar Period** | **2564–2812. 248 years, beginning at the Falkland Treaty.** The default frame for worldbuilding a Tepenian location; a corpus-wide constant, not a per-city judgment | ⭐ `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md`, in full |
| Act structure within the frame | Act 1: 2564 → somewhere in the 2600s (a hazy range, not yet dated) — national-ethnic-origin cultures still fresh. Act 2: by the late 2600s / early 2700s, onward — properly Tepenian; origin is ancestry, not identity | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` |
| The consolidating mechanism | Interconnection, decisively solidified by Amundsen Tower's completion (~2688) — not a switch, not the creation of unity, not the Tower's only effect | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` §"The consolidating mechanism" |
| **U** `Repo_Scope.md` | Tier U — corpus-wide boundary statement, fixed | — |
| Real-world basis | Two adjacent real-world sites in the Schirmacher Oasis, Queen Maud Land — Novolazarevskaya Station (Russia, continuously operated since 1961) and the Maitri Station site (originally India, but see canon note below) (~70°46'S, 11°44'E) | `Specs/Lazar.md` L3 |

**Not mechanical / not included here:** the Type + modifiers declaration, Band assignment, extent band, Status declaration, Configuration, generator selection, the asymmetry check on inherited material — none of this exists until Lazar's own pass runs.
