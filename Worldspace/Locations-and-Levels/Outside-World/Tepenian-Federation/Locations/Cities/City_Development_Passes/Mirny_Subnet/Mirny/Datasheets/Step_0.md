# Mirny — Datasheet · Step 0 & Phase 0 (Frame) — MERGED

> ⚙ **Pass run: this sheet is the pre-run record.** Wording below such as "has NOT started" or "none of this exists until Mirny's own … actually runs" speaks from before the pass and is kept as written.

> ⚠ **DRAFT — Tier C + Tier U.** Merged 2026-09-15: Step 0 and Phase 0 draw on identical underlying facts 📎 *Files cited by line number here may carry a pointer to their copy in the `DerivationMechanisms` repo at the very END of the file (put there so no cited line moves): check the bottom of a cited file.*
> (census, coordinates, timeline era) and had no genuine difference between them — kept separate they were
> pure duplication. **Feeds `00_Frame.md` when Mirny's own Step 0 actually runs.** Mirny's own Frame
> declaration has not been written; this file carries only what a source already states directly.

> 📂 **MUST-OPEN coverage — Field Guide Rule 1 (spine, Phase 0), recounted by hand 2026-10-30:** **3 of 3** addresses are named in this sheet (2 directly, 1 through a shared Tier U sheet it cites).

| Category | Value | Citation |
|---|---|---|
| Census I | 692,971 H / 710,578 R / **1,403,549** (revised 2026-07-04; `DR-68` 2026-10-28, was 665,901 / 685,529 / 1,351,430; `DR-90` 2026-11-02) | `Official_Population_Census.md` L500 — cross-verified against `Specs/Mirny.md` L15, exact match (re-checked 2026-10-30; attribution corrected 2026-11-08, `DR-122`) |
| Census II | 524,022 H / 528,352 R / **1,052,374** *(was 507,344 / 509,151 / 1,016,495 before `DR-68` 2026-10-28; `DR-90` 2026-11-02)* | `Official_Population_Census.md` L642 — cross-verified against `Specs/Mirny.md` L16, exact match (re-checked 2026-10-30; attribution corrected 2026-11-08, `DR-122`) |
| Retention (computed; formula = retained ÷ Census-I count) | combined 74.98% · human 75.62% · robot 74.36% · spread **1.26 pp toward humans** *(corrected 2026-11-08, `DR-122`: was 1.89, the spread of the superseded interim rows of 2026-10-28)* | Computed from the two rows above: 1,052,374÷1,403,549 = 74.98%; 524,022÷692,971 = 75.62%; 528,352÷710,578 = 74.36%; spread 75.62 − 74.36 = 1.26 (unrounded 75.6196 − 74.3552 = 1.2644) |
| Extent *(2026-09-05 snapshot; the census is live — note L631)* | Mirny · Subnet Mirny · Census I (snapshot) 1,351,430 · @10,000/km² **135 km²** · @7,000/km² **193 km²** · Site: coastal ice *(a record of the 2026-09-05 table. Corrected 2026-11-08, `DR-122`: the cited line now holds the live row, Census I of 2026-11-03: 1,403,549 · @10,000/km² **140 km²** · @7,000/km² **201 km²** · Site: coastal ice)* | `Extent_and_Density_Per_City.md` L611 (table header L603; note L631, which now reads *"Census I of 2026-11-03; the census is the live source."*) |
| Extent at the live Census I (computed) | 140.35 km² @10,000/km² · 200.51 km² @7,000/km² *(corrected 2026-11-08, `DR-122`: was 137.5 and 196.5, computed from the superseded interim total 1,375,348)* | Computed: 1,403,549÷10,000 = 140.35; 1,403,549÷7,000 = 200.51 (Census I from `Official_Population_Census.md` L500; the two densities are the extent table's column heads; the table's own row, `Extent_and_Density_Per_City.md` L611, prints 140 and 201) |
| **Temporal frame — the Second Interwar Period** | **2564–2812. 248 years, beginning at the Falkland Treaty.** The default frame for worldbuilding a Tepenian location. Corpus-wide constant, not a per-city judgment | ⭐ `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md`, in full |
| Act structure within the frame | Act 1: 2564 → somewhere in the 2600s (a hazy range, not yet dated) — national-ethnic-origin cultures still fresh. Act 2: by the late 2600s/early 2700s, onward (most of the period) — properly Tepenian, origin is ancestry not identity | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` §"The Act structure" |
| The consolidating mechanism | Interconnection, decisively solidified by Amundsen Tower's completion (~2688) — not a switch, not the creation of unity, not the Tower's only effect | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` §"The consolidating mechanism" |
| The governing form-of-words rule | *"a Japanese city"* → *"a Japan-FOUNDED Tepenian city."* Stock: national origin. People: Tepenian. Local culture: its own | `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` §"What this means for any pass" |
| **U** `Repo_Scope.md` | Tier U — corpus-wide boundary statement, fixed | — |
| Real-world coordinate (GPS only) | Mirny Station, Davis Coast, East Antarctica | `Specs/Mirny.md` L3 |
| Coordinates | ~66°33′S, 93°01′E | `Specs/Mirny.md` L3 |
| **Language** (set 2026-11-03) | Hawaiian (later Tepenian) is the dominant language. **Supporting tier: English and Russian** (set by the developer as a Mirny special case, `DR-111`, 2026-11-04; corrected here 2026-11-08, `DR-122`) — a language not dominant but widely enough understood that business, social talk and general dealings can be done in it; the 12-point rule's set is every language group within 12 percentage points of the city's largest group (range mid-points; nations sharing a language summed). Largest group: English 25.2–34.4. No other group is within 12 percentage points, so the 12-point rule alone gives English, as it does by actual speakers (`DR-111`). *These are shares of residents whose national origin is a nation of that language, not counts of speakers; the mapping of nations to languages is recalled general knowledge, not verified.* | `Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` (12-point addendum and rulings); `Research_Logs/Language_Blocs_By_City_2026-11-03.md`; `DEVELOPER_RULINGS_LOG.md` L1769 (`DR-111`) |

**Not mechanical / not included here:** the Type+modifiers declaration, Band assignment, extent band, Status
declaration, Configuration, generator selection, the asymmetry check on inherited material — none of this
exists until Mirny's own Step 0 actually runs.
