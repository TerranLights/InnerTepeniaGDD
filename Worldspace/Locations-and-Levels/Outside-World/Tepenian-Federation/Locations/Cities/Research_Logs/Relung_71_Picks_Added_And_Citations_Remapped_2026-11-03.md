# Relung Panen: 71 further picks added to the live picks file, and the citations remapped (2026-11-03)

**Status: DONE, not committed.** Developer accepted the 11 tier changes ("sure, that works", 2026-11-03).

## The insertion
- `Cities/Inspirational-Influences.md`: 71 lines inserted after the 28 existing Relung Panen picks (old L148) and before `### Mawson Subnet`. The file went from 326 to 397 lines. New Relung block: heading L119, notes L120, 28 picks L121–L148, **71 new picks L149–L219**, blank L220, `### Mawson Subnet` at L221 (was L150).
- Counts: 10 PRIMARY, 34 SECONDARY, 27 SUPPORTING among the 71 (B01–B04 24, B05–B08 24, B09–B12 23). Ladakh stays PRIMARY. No other line of the file changed.
- **The shift:** every old line number n >= 149 became n + 71; lines <= 148 are unchanged (so every citation of the Relung picks and of anything before Relung stayed as it was).

## Citations remapped (live files only)
Method: a script took every line naming `Inspirational-Influences` and shifted each `L<number>` (including ranges, lists, bold-wrapped numbers and `lines N–M`) found after the name and before the next different `.md` name on the line, by the rule above. **141 lines in 23 files** (list below, line numbers are the lines edited in each file). Checks: 109 pick-copy rows compared with the new file line (all match; one differs only in an annotation the sheet states it did not copy); 63 heading citations checked (all point to a `#` heading except Santa Luce's Pre-Trip L429, whose range "L260 to L265" ends on a blank line in the new file, as it ended on a blank line before: not changed by this pass).

- `City_Development_Passes/Halley_Subnet/Lazar/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14, 15
- `City_Development_Passes/Halley_Subnet/Troll/Datasheets/Step_3.md`: lines 10, 11, 12, 13, 14, 15
- `City_Development_Passes/Halley_Subnet/Halley/Datasheets/Step_3.md`: lines 10, 11, 12, 13, 14, 15, 16, 17
- `City_Development_Passes/Halley_Subnet/Santa_Luce/00.0_Pre-Trip_Inspection.md`: lines 429
- `City_Development_Passes/Halley_Subnet/Utstein/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14
- `City_Development_Passes/Halley_Subnet/Neumayer/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14, 15, 16
- `City_Development_Passes/Mawson_Subnet/Mawson/Datasheets/Step_3.md`: lines 10, 11, 12, 13, 14
- `City_Development_Passes/Mawson_Subnet/Dome_Fuji/Datasheets/Step_3.md`: lines 10, 11, 12, 13
- `City_Development_Passes/Mawson_Subnet/Temirotkel/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14
- `City_Development_Passes/Halley_Subnet/Sanay/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13
- `City_Development_Passes/Amundsen_Station/Amundsen_Station/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14, 15, 16, 17
- `City_Development_Passes/Halley_Subnet/Belgrano/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14, 15
- `City_Development_Passes/Halley_Subnet/Santa_Luce/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13
- `City_Development_Passes/Byrd_Subnet/Byrd/Datasheets/Step_3.md`: lines 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- `City_Development_Passes/Palmer_Subnet/Pergamino/Datasheets/Step_3.md`: lines 9, 10, 11, 12
- `City_Development_Passes/Palmer_Subnet/Esperanza/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14, 15, 16
- `City_Development_Passes/Palmer_Subnet/Palmer_City/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14
- `City_Development_Passes/Palmer_Subnet/Puerto_Abrigo/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14
- `City_Development_Passes/Palmer_Subnet/Rothera/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14
- `City_Development_Passes/Palmer_Subnet/Contrapunto/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13
- `City_Development_Passes/Palmer_Subnet/Signy/Datasheets/Step_3.md`: lines 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
- `City_Development_Passes/Palmer_Subnet/Marambio/Datasheets/Step_3.md`: lines 9, 10, 11, 12
- `City_Development_Passes/Mirny_Subnet/Relung_Panen/Datasheets/Step_3.md`: lines 9

## Wrongly touched, then restored
The script also shifted one number in each of six T8 reader scratch files under `City_Development_Passes/Mirny_Subnet/Mirny/` (`.t8_Step5_reader{A,B,C}.md` and three `_safeguard_probe/partials/Step5_staging_*.md`). They are records of a finished run, so each edit was inverted by writing the logged original line back; `git diff` for that folder is now empty. (`git checkout` is blocked by a project hook, so the restore was by hand.)

## Skipped on purpose (records of what was true then): 57 lines

- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/FIX_LEDGER.md`: 20 line(s)
- `Research_Logs/Amundsen_Station_Canon_Inventory_2026-10-29.md`: 3 line(s)
- `Station_Heritage_Removal_Tracker.md`: 2 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Palmer_City_Sweep.md`: 2 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Lazar_Sweep.md`: 2 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Signy_Sweep.md`: 2 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Amundsen_Station_Sweep.md`: 2 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Troll_Audit.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Belgrano_Audit.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sanay_Audit.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Ariun_Nuur_Audit.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Relung_Panen_Audit.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Santa_Luce_Audit.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Lazar_Audit.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Pergamino_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Santa_Luce_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Troll_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Halley_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Marambio_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Neumayer_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Rothera_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Sanay_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Belgrano_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Neumayer_Audit.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Puerto_Abrigo_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Dome_Fuji_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Contrapunto_Sweep.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Utstein_Audit.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/TRACKER.md`: 1 line(s)
- `Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Halley_Audit.md`: 1 line(s)
- `Archive/ULM_Records/Test_Runs/2026-08-31_SanayMaritimeShippingPort_Run11_Cold/SanayMaritimeShippingPort_Research_Log.md`: 1 line(s)

## One thing the insertion leaves for later
`Relung_Panen/Datasheets/Step_3.md` copies picks "as written (cap 40)". The picks section now has 99 lines, so the sheet's picks rows (28) are stale against the live file. I annotated its header (71 further picks added, not copied) and did not rebuild the sheet; Relung is outside the November run.

## Tool results
- `audit_city_inputs.py --scope all`: only the known Amundsen Station and Davis gaps.
- `verify_city_sheets.py` for all 23 edited cities: 0 FAIL, except Mirny's 4 FAIL, which are its older sheet format and were there before (and Mirny's own sheets were not edited).

