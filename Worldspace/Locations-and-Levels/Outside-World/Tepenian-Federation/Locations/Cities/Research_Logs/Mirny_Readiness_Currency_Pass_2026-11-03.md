# Mirny readiness: currency pass over the Pre-Trip, ledger, 19 datasheets and README (2026-11-03)

**Scope:** `City_Development_Passes/Mirny_Subnet/Mirny/`: `00.0_Pre-Trip_Inspection.md`, `00.2_Position_Coverage_Ledger.md`, `Datasheets/` (19), `README.md`. Pass files (steps, phases, T8, amendment files) untouched (`DR-74`). No web research, no commit. Run under the developer's one-off hours waiver for the Mirny blocks. Clock at start 16:18 (machine clock).

## Method
1. Regenerated all 19 datasheets and the Pre-Trip with the builders into the scratchpad (builders unchanged). The existing datasheets are a different, hand-built shape (category names differ), so a row-for-row replacement was NOT done: the pass's T8 files cite them, and they hold dated as-run records.
2. Wrote a citation checker (scratchpad `citecheck.py`): for every datasheet row that cites `file Lnn[–mm]`, it resolves the file, checks the line exists, and checks that the row's text appears in the cited lines. 26 hits; each read by hand against the live source (below).
3. Compared every table row of the freshly generated Pre-Trip with the current Pre-Trip: **0 generated rows missing** from the current file, so the Pre-Trip's addresses, line numbers and counts are current against today's sources.

## Stale items found and fixed
| File | Line | Old | New | Why |
|---|---|---|---|---|
| `Datasheets/Phase_4.md` | 20 | bracket said only Humans, Residents and Workforce of the `09` row were refreshed 2026-10-28; Required and % WF "remain the superseded old-B1 model" | bracket now quotes `09` L1 as it stands: 2026-10-28 refresh, and the 2026-11-03 (`DR-96`, `DR-97`) second refresh of Required and % WF for 25 rows plus the robot term in `16` | `09` L1 was extended today |
| `Datasheets/Step_1_and_2.md` | 33 | `16` Half B row: base 41.1% · MAND 11.8% · FREE 47.1%; §20 split "Mandated 23.6% · FREE 35.3%" | base 42.2% · MAND 11.6% · FREE 46.2% (old values kept in brackets); §20: Mandated 23.1% · FREE 34.7% | `16` L276 and §20 recounted with the robot term (`DR-97`) |
| `Datasheets/Phase_7.md` | 51 | "Half B gives MAND 11.8% · FREE 47.1%; §20 gives Mandated 23.6% · FREE 35.3%" | 11.6% / 46.2% and 23.1% / 34.7% (old values kept) | same |
| `Datasheets/Phase_2.md` | 24 | inline spec line numbers L152, L154, L230 (the spec gained 22 lines above them in the 2026-11-02 composition rebuild) | "then L152 / L154 … now at L174 and L176"; "that founding line (now L174)"; "then L230, now L252" | text cites the live spec L174–176, L252 in its citation cell but the prose used pre-rebuild numbers |
| `00.0_Pre-Trip_Inspection.md` | new section O (appended; no cited line moved) | none | amendment layer: register, Pieces 1 and 2, the two amendment notes, packages for Piece 3 and the Phase 2 composition piece, rulings added since the pass (`DR-74` … `DR-97`), live composition address, language rule, stage order, reconciliation log | the pieces read files that did not exist when the Pre-Trip was written |
| `00.2_Position_Coverage_Ledger.md` | appended status note | none | marks are the as-run marks; unchanged; only a clarified piece can revise one | the ledger tracks positions by phase, not files, so no cell was touched |
| `README.md` | status block at top | "Empty by design" (2026-09-05 note) with no state | dated status block: pass run through Step 10, not declared complete; folder contents; amendment layer; six Primaries, no majority; Census I/II; Hawaiian first, second slot open | stale folder description and a composition the pass was run on |

**Phase_2.md edit time:** 16:22:34 machine clock, before the coordinator's freeze request of the same minute window; one line only (L24, the three inline phrases above). Left as edited; not touched again.

## Found, NOT fixed (outside my scope or frozen)
- `Datasheets/Phase_2.md` L15 says "Full 35-row table"; the spec table has 36 stocks (L31 header, rows L32–L67). FROZEN by the coordinator's open round (P2c): not edited. Fix when the round is merged.
- `Datasheets/Step_0.md` L17 and `Step_1_and_2.md` L25 quote the 2026-09-05 extent snapshot (Census I 1,351,430): labeled as a snapshot in the row itself ("the census is live"); the extent file still says 1,351,430. Left as a labeled snapshot.
- `City_Relationship_Database.md` Mirny entry (L334–341) still says "Mirny itself was founded by Russia, China and Australia, `DR-9`" (the Register says Idelsk-Uralia founded it, exile groups Russia, Australia, Sinian Federation); Phase_5 L16–L17 cite the entry for region and hub, not founders, and do not carry the sentence. Source file outside scope.
- `Phase_5.md` and `Step_-1.md` have notes D7 (later-era words at Step_7 L15, Phase_3 L16, Phase_5 L39 and L43) and D8 (inference marker at Step_-1 L24): to be READ, not stripped.

## Tool results (verbatim excerpts; full outputs in the scratchpad `t_*.txt`)
- `verify_city_sheets.py Mirny --quiet`: `== Mirny: 20 checks, 0 FAIL, 2 NOTE`; `NOTE D7 later-era words 4 line(s) to READ: Step_7.md L15; Phase_3.md L16; Phase_5.md L39; Phase_5.md L43`; `NOTE D8 inference markers (read, never strip) 1 table row(s): Step_-1.md L24`.
- `audit_city_inputs.py --scope all`: `Mirny tests 40 GAP 0 note 2`; the only gaps in the repo are `Amundsen Station GAP 1` and `Davis GAP 2` (both outside the run).
- `check_must_open_coverage.py --city Mirny`: `TOTAL gaps across 1 cities: 0`.
- `handoff_audit.py <pass>`: `TOTAL outbound handoff rows: 0`; `PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 0`; `INSTRUMENT VALID: YES`; formal sweep blocks found for phases 2 to 10.
- `phase_discipline_check.py <pass>`: T3 reports blank ledger cells (as-run, by design); T4 present for the phases; T5: `LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)`, `T5 not fully applied this pass`.
- `check_founders_against_register.py --city Mirny`: `Founder disagreements: 0 · heritage wording: 0 · files scanned: 1824`.
- `quotation_audit.py <Datasheets> --all`: `fragments tested 51; NOT FOUND in corpus: 27 (7 table cells, 20 prose)`. Triage by hand: 19 are the pre-run banner at each sheet's line 3 quoting the sheet template's own wording ("none of this exists until Mirny's own …"), a self-quote; the remaining misses are quotes with bracketed edits or ellipses (Phase_5 L19), connective prose between two adjacent quotations (Phase_7 L51), a note about a search run (Phase_10 L11, Step_10 L10), and one prose phrase of a docket (Phase_2 L24); Phase_7 L58's quoted phrase exists at `Division_of_Industry_Sweep_2026-08-31.md` L220 (with the source's surrounding parentheses). None is a false quotation.
- `quotation_audit.py` on the Pre-Trip (`--files 00.0_Pre-Trip_Inspection.md`): `fragments tested 3; NOT FOUND 0`.

## Not ready, and why
- Nothing in my scope blocks the pieces. Open items are the three in "Found, NOT fixed" (one frozen, two in files outside scope or labeled snapshots).
- The Piece 3 and Phase 2 composition packages are being built by other forks; the Pre-Trip section O points at them by name and says they were being built.
