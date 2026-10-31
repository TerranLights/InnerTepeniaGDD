# Concordia — amendment notes, 2026-10-30 (manual input audit)

**What this file is.** Twelve of Concordia's thirteen districts were completed and passed their checks by 2026-08-29; the Hub is deferred. **No district file, no Concordia-level file and no megasheet is edited by this note, and none was.** The entry below says what has changed in one of Concordia's sources since the file in question was written, where that file rests on the earlier figures, and the live figures as they stand on 2026-10-30. **Everything quoted from a Concordia file is as written then; the source has since changed.** The files stay the record of what they were written from.

**Limit, stated plainly.** The altitude file was searched for its population figures (the numbers 309, 326, and the words "population" and "million", plus the earlier Census I and II counts); the two places below are the only ones the search found. The other Concordia files that carry the earlier census counts are not covered here.

**Developer decisions of 2026-10-30.** Entries `CNC-001` to `CNC-007` and the source corrections below were added after the walk-through (*"all as recommended"*). No district file and no megasheet was edited. The edits to `Concordia_Second_Interwar_Cultural_Sheet.md` (the census restatement of `CNC-001`, the climate figures of `CNC-002` and the founding wording of `CNC-004`) are culture work and are scheduled for the 05:00–14:59 window of 2026-10-31; the founding rewrites will be drafted and shown to the developer before the sheet is edited. Megasheet copies are fixed through the compilation method, not by hand. Evidence: `Manual_Input_Audit_2026-10-29/Concordia_Audit.md` and `FIX_LEDGER.md`.

---

## CNC-005 — `Concordia_Altitude_and_Atmosphere.md` states Concordia's Census II counts as they stood before the census scenario of 2026-10-28 (`DR-68`)

**What changed.** The adopted Santa Luce population scenario (2026-10-28, `DR-68`) raised Concordia's Census II by +8,107 humans and +7,738 robots. The row (`Official_Population_Census.md` **L623**, in "Section C — Population Figures: Orbital Era (Census II)", table "Antarctic Surface — City Populations") now reads 317,175 humans, 333,972 robots, **651,147** combined, and carries the earlier counts in its own note: "*(was 309,068 / 326,234 / **635,302**)*". The Concordia spec carries the same live counts (`Specs/Janbogo subnet/Concordia.md` **L14**: "Census II (Orbital Era): 317,175 humans / 333,972 robots / **651,147** combined *(was 309,068 / 326,234 / 635,302)*").

**Live figures (2026-10-30), with the figure the altitude file states.** Arithmetic by hand and checked a second time.

| Figure | Stated in the altitude file | Live | Working |
|---|---|---|---|
| Census II humans | "~309,000" | 317,175, about **317,000** | 309,068 + 8,107 = 317,175 |
| Census II robots | "~326,000" | 333,972, about **334,000** | 326,234 + 7,738 = 333,972 |
| Census II combined | not stated | **651,147** | 317,175 + 333,972 = 651,147 |
| Size of the change | | humans +2.6%, robots +2.4% | 8,107 ÷ 309,068 = 0.0262; 7,738 ÷ 326,234 = 0.0237 |

**Where the file states the earlier counts** (`Concordia_Altitude_and_Atmosphere.md`, created 2026-09-04; renames swept 2026-10-04; lines as of 2026-10-30):
- **L12–13**, the closing sentences of the opening callout: "Concordia's ~309,000 humans are not adapted to their city. They are enduring it. Its ~326,000 robots do not notice."
- **L169**, the Concordia row of the elevation table: "~309,000 — survivable, never comfortable".

**What stands.** The file's subject (that humans do not acclimatize at 3,233 m, and that robots are unaffected) does not depend on the counts. The two figures are approximations of Census II as it stood on 2026-09-04; the live approximations are about 317,000 humans and about 334,000 robots. This note records the change and does not alter the file.

---

*Filed 2026-10-30 by the manual input audit sweep. Record of the sweep: `Manual_Input_Audit_2026-10-29/Sweep_Reports/Finished_Cities_Sweep.md`.*


---

## CNC-001 — The census scenario of 2026-10-28 (`DR-68`) rescaled Concordia's population; the sheet and the megasheet copies record the earlier set

| | As recorded (2026-07 to 2026-09) | Live since `DR-68` (census L500 and L623) |
|---|---|---|
| Census I humans / robots / combined | 504,799 / 511,148 / 1,015,947 | **516,937 / 522,926 / 1,039,863** |
| Census II humans / robots / combined | 309,068 / 326,234 / 635,302 | **317,175 / 333,972 / 651,147** |
| Orbit share (1 − Census II ÷ Census I) | roughly 37.5% | **37.4%** (1 − 651,147 ÷ 1,039,863 = 37.38%) |
| Retention, humans (Census II ÷ Census I) | 61.23% | **61.36%** |
| Retention, robots | 63.82% | **63.87%** |
| Retention, combined | 62.53% | **62.62%** |

Where the earlier set stands: `Concordia_Second_Interwar_Cultural_Sheet.md` L11–12; `Districts/Concordia_Ultra_Megasheet/README.md` L32–33; `Concordia_Mega_Init.md` L20–21. The sheet's own lines are to be restated in the 2026-10-31 window; the megasheet copies wait for the compilation method.

## CNC-002 — Polar night, midnight sun and climate figures in the sheet and megasheet copies

The sheet (L57), the Ultra-Megasheet README (L35) and Mega_Init (L23) say about **82 days** of polar night and **85 days** of midnight sun. The climate was rebuilt on 2026-09-04; the spec (`Specs/Janbogo subnet/Concordia.md` L120–121) now says polar night **May 5 → Aug 10 (about 98 days)** and midnight sun **Nov 1 → Feb 11 (about 103 days)**. Checked by hand on 2026-10-30 for 75°06′S with the sun's apparent edge raised by 0.833°: the sun stays below the horizon while its declination is above about +15.7° (about 97 days) and stays up while its southern declination is above about 14.1° (about 103 to 108 days), so the spec's figures stand. Other live values: record low **−84.6 °C** (August 2010), record high **−5.4 °C** (January), wind about **2.8 m/s**, precipitation about **25 mm** (falls 25, lands 22), mean annual **−52.7 °C**.

## CNC-003 — The acclimatization sentence in the megasheet copies is the reverse of the altitude file

`Concordia_Mega_Init.md` L23 and `Districts/Concordia_Ultra_Megasheet/README.md` L35 say altitude acclimatization is *"a real physiological fact for every resident, not lore flavor."* `Concordia_Altitude_and_Atmosphere.md` (2026-09-04) says humans do **not** acclimatize at 3,233 m (91–94% oxygen saturation, heated but unpressurized) and that robots are unaffected. The fix belongs to the compilation method.

## CNC-004 and CNC-S02 — The cultural sheet's founding wording (drafts to come)

`Concordia_Second_Interwar_Cultural_Sheet.md` L15, L71, L95–96, L110, L118 and L259 call the city "French- and Italian-founded" and speak of "the French-Italian founders", founding-institutional languages, founding cuisine, founding sensibility and an inherited French-Italian facility. `Founding_Register.md` L73 (`DR-44`): *"No founding nation. Robots and human partners who went inland, then successive waves of coastal refugees. The French/Italian station is not a reason (`DR-19`)."* The sheet's own L43 already says the city filled by *"plain geography … not the founders' flag."* **Status: the eight rewrites are to be drafted in the 2026-10-31 window and shown to the developer before any edit.**

## CNC-006 — Weights in the refugee-diaspora files predate later changes

`Districts/District_Refugee_Diaspora_Composition.md` (2026-07-31) and `City_Refugee_District_Affinities.md` (35 cities, 2026-07-09) use city populations as they stood on those dates. Since then: the −10% cut of 2026-09-05 (Lazar, Zhongshan, Shirayuki, Sinheung; Denison −15%; Dumont d'Urville −10%), the Port Lockroy reduction (128,887 → 929), the Santa Luce reduction (1,034,241 → 437,614; its "~9.0%" of Cancer's outer diaspora is about 4.0% by hand) and `DR-68` (+1.3% to +6.3%). Relung Panen (971,870) has no affinity row. **Not recomputed; to be re-derived after the megasheet rewrite.**

## CNC-007 — Retired names in the district work

Counts from a search of `Districts/` (occurrences; the audit counted 67 lines for Sayowa): Sayowa → **Temirötkel** (18 files, 83 occurrences: the Hub megasheets and PreWar, `Deep_Dives/13_Hub`, `11_Sagittarius`, `Staging/` ×3, `Final_Megasheet_Data_Processing`, `District_Source_Index`); Abowasa → **Santa Luce** (1 file); Port Lockroy → **Puerto Abrigo** (1); Princess Elisabeth → **Utstein** (2 files, 7 occurrences: `13_Hub`, `09_Gemini`); Juan Carlos → **Pergamino** (4 files, 8: `03_Leo`, `08_Libra`, the Leo megasheet README and Mega_Init); Sejong → **Contrapunto** (3 files, 8: `08_Libra`, `09_Gemini`, the Gemini Full Extrapolation); **Vostok** the city → **Ariun Nuur** (4 files, 11: `04_Scorpio`, `07_Aquarius`, `11_Sagittarius`, the Sagittarius Full Extrapolation; read each: the district keeps the name). See `Cities/City_Renames_Alias_Table_2026-10-03.md`.

## Source corrections (developer, 2026-10-30)

- **`CNC-S01` — applied.** `Specs/Janbogo subnet/Concordia.md` L104 read *"coldest month (August) avg −65°C; warmest month (December/January) avg −27°C"*; −27 is neither a mean nor an Avg High (−24.9 / −24.8). It now reads: *"coldest months (June/July/August) mean −64.1°C / −63.2°C / −63.3°C; warmest months (December/January) mean −30.7°C / −31.3°C"*. The spec is still 292 lines. The same wording stands in `Concordia_Mega_Init.md` L23 and the Ultra-Megasheet README L35 and waits for the compilation method.
- **`CNC-S03` — left in place.** The spec's *"At −52.7 °C it is the #4 coldest of the 37"* (L117) is a peer rank; it stays, and the Weekly To-Do carries the question.

---

*Entries filed 2026-10-30 at the developer's direction ("all as recommended"). The district work is to be revisited when the finished cities are re-analyzed (see the Weekly To-Do).*
