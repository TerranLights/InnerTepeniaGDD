# Fort McMurdo — Datasheet · Step 0 & Phase 0 (Frame) — MERGED

> ⚠ **DRAFT — Tier C + Tier U.** Merged per the Field Guide's consolidation of Step 0 / Phase 0 (identical underlying facts). **Feeds `00_Frame.md` when Fort McMurdo's own Step 0 runs.** It carries only what a source already states directly. 📎 *Files cited by line number here may carry a pointer to their copy in the `DerivationMechanisms` repo at the very END of the file (put there so no cited line moves): check the bottom of a cited file.*

> 📂 **MUST-OPEN coverage — Field Guide Rule 1 (spine, Phase 0), recounted by hand 2026-10-30:** **3 of 3** addresses are named in this sheet (2 directly, 1 through a shared Tier U sheet it cites).


| Category | Value | Citation |
|---|---|---|
| Census I | 222,190 H / 223,120 R / **445,310** combined (status cell: revised 2026-07-04; the "island cap" tag was removed 2026-10-30) | `Official_Population_Census.md` L507 |
| Census II | 173,548 H / 164,621 R / **338,169** combined (status cell: the "island cap" tag was removed 2026-10-30) | `Official_Population_Census.md` L627 |
| Retention (computed; formula = Census II count ÷ Census I count) | combined 75.94% · human 78.11% · robot 73.78% | Computed from the two rows above: 338,169÷445,310 · 173,548÷222,190 · 164,621÷223,120 |
| Extent — the spec's own declaration (2026-09-05; population unchanged) | **Extent band ~55 km²**; 445,310 ÷ 55 = **8,097/km²** *(the spec states: inside the 7,000–10,000 band; was 181/km² measured against Ross Island entire)*. The block states that the city stands on rock and its own heat keeps it bare; one of the six geothermal cities. Hut Point Peninsula measures 3.7–5.6 km wide by 28 km long, ≈104–157 km², shared with Scott; Mount Erebus is the heat both cities share | `Specs/Fort_McMurdo.md` L18–L38 (extent band L19; terrain finding L21–L24; peninsula L30–L38) |
| Extent file — the city's row (**2026-09-05 snapshot; the census is live — note L631**) | Ross I. · 2,460 km² · Census I 445,310 · **181/km²** · *rural* *(the whole island's area)* | `Extent_and_Density_Per_City.md` L63; Ross I. area row L697 |
| Extent file — the declaration (**2026-09-05 snapshot; the census is live — note L631**) | **DECLARED 2026-09-05: 55 km² → 8,097/km²**; populations unchanged; site-derived from Hut Point Peninsula (~104–157 km²); rock, kept bare by geothermal heat *(the source line pairs the city with its same-peninsula neighbor; only this city's own figure is copied here)* | `Extent_and_Density_Per_City.md` L509 |
| **Temporal frame — the Second Interwar Period** | **2564–2812. 248 years, beginning at the Falkland Treaty.** The default frame for worldbuilding a Tepenian location; a corpus-wide constant, not a per-city judgment | ⭐ `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md`, in full |
| Act structure within the frame | Act 1: 2564 → somewhere in the 2600s (a hazy range, not yet dated) — national-ethnic-origin cultures still fresh. Act 2: by the late 2600s / early 2700s, onward — properly Tepenian; origin is ancestry, not identity | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` |
| The consolidating mechanism | Interconnection, decisively solidified by Amundsen Tower's completion (~2688) — not a switch, not the creation of unity, not the Tower's only effect | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` §"The consolidating mechanism" |
| **U** `Repo_Scope.md` | Tier U — corpus-wide boundary statement, fixed | — |
| Real-world basis | McMurdo Station (USA), Ross Island, Ross Sea (~77°51'S, 166°40'E) | `Specs/Fort_McMurdo.md` L3 |

**Not mechanical / not included here:** the Type + modifiers declaration, Band assignment, extent band, Status declaration, Configuration, generator selection, the asymmetry check on inherited material — none of this exists until Fort McMurdo's own pass runs.
