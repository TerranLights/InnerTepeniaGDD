# Amundsen Station: the nation-wide composite applied to the spec and census (2026-11-03)

**Status: APPLIED, not committed.** Developer decisions of 2026-11-03: Census Section B national totals as the basis; all 83 nations printed; robots in the humans' proportions; Primary = Korea, Sinian Federation, Japan, Australia, CSA, United Kingdom (break after the UK 5.02% | Indonesia 4.26%); Significant = Indonesia through New England (2.52% | Austro-Bavaria 1.50% is the largest gap); Notable = the other 70; the minimal spec and census wording edits applied; the picks stay a draft in the review pack (`Inspirational-Influences.md` untouched). Source pack: `Amundsen_Station_Review_Pack_2026-11-03.md` sections 3.4 and 4.

## Figures re-verified (scratch script, two methods)
- Section B (Census I humans): 83 nations total 15,598,581; maritime fleet 24,942 (no nation); sum 15,623,523 (agrees).
- Shares = nation humans ÷ 15,598,581. Counts by the largest-remainder method (exact fractions in method 1, floating point in method 2; ties by larger share then name). The two methods agree on every cell. Column sums: Census I robots 5,736; Census I humans 1,121; Census II robots 3,978; Census II humans 913 (all exact).
- All 83 rows (6 Primary, 7 Significant, 70 Notable) match the pack's table cell for cell (0 differences); the pack's percentages are the 2-decimal (3-decimal below 0.1%) roundings of the shares.
- Rounding follows the other specs: their columns also sum exactly to the stated totals (checked on Contrapunto and Mirny).

## Edits (all in place unless stated)
**`Specs/Amundsen-Scott subnet/Amundsen_Station.md`** (249 → 301 lines, +52):
- L15: "skeleton crew" → "a small town of rotating staff drawn from all of Tepenia", old wording kept in brackets.
- L19–L21: the three tier rows replaced by the composite lists (same line count).
- L29–L61 (the 31-row per-nation table) replaced by L29–L113 (the 83-row table; header 2 + 83 rows); old Norway "(Amundsen heritage — Saint Roald)" and Chile "(unique Union Glacier route advantage)" annotations retired (under `DR-32` namesakes are no basis; under a composite neither has a role).
- Basis note appended to the italic note under the table (the former L63, now L115).
- Former L169 (now L221), L177 (now L229), L191 (now L243): the "never primarily a population center", "culture of a facility, not a city" and "already-established 'not a city' identity" wording replaced with the ruled town wording; each line keeps its old text in a dated bracket.
- Old→new line map: lines 1–28 and 62 onward: lines ≤ 61 unchanged except that L29–L61 grew; every old line n ≥ 62 is now n + 52 (old L63 → L115, L169 → L221, L177 → L229, L191 → L243, L210 → L262, L220 → L272, L232 → L284).

**`Official_Population_Census.md`** (no line shifts): L476–L478 tier rows (Section A entry) replaced by the same three lists as the spec; L480 note reworded to the town wording with the old wording bracketed; L670 status cell "skeleton crew" → "small town of rotating staff" with the old word bracketed. Section B (national origin totals, L558 onward) left alone: it includes the station's old 1,121 humans, and the composite is built from it (circular; the largest shift is about 65 people in one nation, 0.0004% of 15,623,523). Census I status cell at L531 ("~84% robot; revised 2026-07-04") unchanged.

## Citations re-synced
- `Tools/remap_line_citations.py --base HEAD --apply` on the Amundsen Station pass folder: 29 numbers in 5 files (`Step_1_and_2` 20, `Phase_10` 1, `Phase_2` 2, `Phase_3` 3, `Step_-1` 3); on `Founding_Register.md`: 1 number (L171 → L223). Master Reference, culture, robot-culture, vision-note, relationship-database and README files: no line-numbered citations to the spec's moved lines.
- Datasheet rows re-quoted by hand because the quoted lines changed: `Step_0.md` L11 (census cell), `Step_-1.md` L20 (spec L15), `Phase_2.md` L10, L11 (tier lists, spec and census), L12 (comparison re-checked), L13–L16 (the four annotation rows now marked retired), `Step_1_and_2.md` L47 (the `Settled:` line, L221) and L49 (tier lists).
- Skipped (dated records): `Population_Work_Prep_2026-11-02.md` (cites the old table row, L32), the research logs and the review pack, the Davis ruling file, audit folders and test runs.

## Tool results
- `verify_city_sheets.py Amundsen_Station --quiet`: 20 checks, 0 FAIL, 2 NOTE (later-era words Step_3 L15 and Step_7 L13; inference markers Step_1_and_2 L38, L39 and Step_3 L11, to be read, not stripped).
- `quotation_audit.py` on `Step_1_and_2.md` and `Phase_2.md`: 0 fragments not found.
- `audit_city_inputs.py --scope all`: only Amundsen Station (1) and Davis (2) gaps, both known (Amundsen's is its picks entry, which waits on the developer's tiers and the pair check).

## Left alone, on purpose
- The italic rework note above the table (the `DR-85` text of 2026-11-02) is kept as history.
- `16` §35 (the station's Division of Industry row) was not re-determined (canon inventory question 5).
- The spec's Geographic, Climate and later sections; the St. Roald passage; the picks (draft in the review pack).
