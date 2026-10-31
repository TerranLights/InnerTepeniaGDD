# Neumayer — Datasheet · Step 0 & Phase 0 (Frame) — MERGED

> ⚠ **DRAFT — Tier C + Tier U.** Merged per the Field Guide's consolidation of Step 0 / Phase 0 (identical underlying facts). **Feeds `00_Frame.md` when Neumayer's own Step 0 runs.** It carries only what a source already states directly. 📎 *Files cited by line number here may carry a pointer to their copy in the `DerivationMechanisms` repo at the very END of the file (put there so no cited line moves): check the bottom of a cited file.*

> 📂 **MUST-OPEN coverage — Field Guide Rule 1 (spine, Phase 0), recounted by hand 2026-10-30:** **3 of 3** addresses are named in this sheet (2 directly, 1 through a shared Tier U sheet it cites).


| Category | Value | Citation |
|---|---|---|
| Census I | 625,874 H / 650,123 R / **1,275,997** combined (status cell: revised 2026-07-04) | `Official_Population_Census.md` L492 |
| Census II | 393,179 H / 453,415 R / **846,594** combined | `Official_Population_Census.md` L616 |
| Retention (computed; formula = Census II count ÷ Census I count) | combined 66.35% · human 62.82% · robot 69.74% | Computed from the two rows above: 846,594÷1,275,997 · 393,179÷625,874 · 453,415÷650,123 |
| **Extent (2026-09-05 snapshot; census is live — note L631)** | City: Neumayer · Subnet: Halley · Census I (snapshot): 1,252,080 · @10,000/km²: 125 km² · @7,000/km²: 179 km² · Site: Ekström ice shelf | `Extent_and_Density_Per_City.md` L615 (header L603; snapshot note L631) |
| **Extent at the live Census I (computed)** | 127.6 km² @10,000/km² · 182.3 km² @7,000/km² | Computed: 1,275,997 ÷ 10,000 · 1,275,997 ÷ 7,000 (Census I, `Official_Population_Census.md` L492) |
| **Temporal frame — the Second Interwar Period** | **2564–2812. 248 years, beginning at the Falkland Treaty.** The default frame for worldbuilding a Tepenian location; a corpus-wide constant, not a per-city judgment | ⭐ `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md`, in full |
| Act structure within the frame | Act 1: 2564 → somewhere in the 2600s (a hazy range, not yet dated) — national-ethnic-origin cultures still fresh. Act 2: by the late 2600s / early 2700s, onward — properly Tepenian; origin is ancestry, not identity | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` |
| The consolidating mechanism | Interconnection, decisively solidified by Amundsen Tower's completion (~2688) — not a switch, not the creation of unity, not the Tower's only effect | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` §"The consolidating mechanism" |
| **U** `Repo_Scope.md` | Tier U — corpus-wide boundary statement, fixed | — |
| Real-world basis | Neumayer Station III (Germany / Alfred Wegener Institute), Ekström Ice Shelf, Queen Maud Land (~70°41'S, 8°16'W) | `Specs/Neumayer.md` L3 |

**Not mechanical / not included here:** the Type + modifiers declaration, Band assignment, extent band, Status declaration, Configuration, generator selection, the asymmetry check on inherited material — none of this exists until Neumayer's own pass runs.
