# Mirny: Pre-Trip rebuilt in the current format (2026-11-03, about 16:30; developer approved)

**What failed.** `verify_city_sheets.py Mirny`: 20 checks, 4 FAIL, all in the Pre-Trip `00.0_Pre-Trip_Inspection.md` (the Datasheets and the ledger passed every check): P2 (step and phase blocks: 0 step headings, 0 governing, 11 T8; wanted 12/11/11), P3 (section D lacked spine addresses: P5 Infrastructure, P6 True Believer and Meme Machine extractions, P7 Burden Scoring Model and Volume-Based Requirement Reference, and more), P6 (no verification block with 0 missing inputs and 0 failed claims) and P7 (placeholder tokens `<Mirny pass folder>`, `<N>`, `<STATION>`, `<Subnet>`, `<one line>`). The old sheet was written in the 2026-09-28 compact format.

**What was rebuilt.** Only the Pre-Trip, by `build_pretrip.py Mirny --out` (a comparison copy; the builder refuses `--write` for hand-built sheets and was not changed), then merged:
- New sheet = the generated one (565 lines), plus a rebuild banner under the title, plus records carried from the old sheet: the Bellingshausen-ship alias row and the "flagged for an eventual rename" row (§A); the Mirny Rename, Zodiac Lens address discrepancy, stale-range root cause and 2026-10-30 registered-addresses rows (§J); and, at the end, the old refresh notice, the Zodiac Lens discrepancy paragraph and the old §N refresh-check raw output. Carried rows are marked *(carried from the as-run sheet of 2026-09-28)*.
- The old sheet is kept unchanged (byte-for-byte copy, including its 2026-10-21 refresh) as `00.0_Pre-Trip_Inspection_AS_RUN_2026-09-28.md` in the pass folder, because the Mirny T8 reader files cite it. Another copy sits in the session scratchpad (`mirny_old/`).

**Not touched.** Every pass output file (steps 5–10, T8 files, readiness check, symbol review), the ledger `00.2_Position_Coverage_Ledger.md` (36 lines of per-phase coverage records; the generated ledger is only 20 and would have lost them), the Datasheets folder. No live file cites the old Pre-Trip by line (only T8 reader scratch files and amendment records do, and those cite the kept as-run copy's text).

**Not carried, on purpose.** The old §A line "No retired placeholder filename found" and the old compact per-step/per-phase text (the generated sheet regenerates them in the current format); the old banner text beyond a one-line summary.

**Tool results after the rebuild.**
- `verify_city_sheets.py Mirny --quiet`: 20 checks, 0 FAIL, 2 NOTE (later-era words Step_7 L15, Phase_3 L16, Phase_5 L39 and L43; inference marker Step_-1 L24: all to be read, not stripped).
- P6: 0 missing inputs; 228 claims, 0 failed.
- `audit_city_inputs.py --scope all`: Mirny 0 gaps; only the known Amundsen Station (1) and Davis (2) gaps remain.
- `quotation_audit.py` on the new Pre-Trip: 3 fragments tested, 0 not found.

**Could not fix / flag.** None of the four checks remains failing. The new sheet's alias table says (generated, 2026-11-03) "No rename flagged" in the spec's first 30 lines, while the carried row records the TODO.md rename flag (2026-07-08); both stand, the carried one is a record.
