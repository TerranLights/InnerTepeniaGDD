# Davis cross-check of 2026-11-09: erratum on the four composition rows (DR-94 item 4)

**What this is.** An erratum to the amendment pieces written earlier in this review, found at Round 3 of the Phase 2 piece and then checked by the orchestrator against the ruling log. It states the current fact with its address, lists where the earlier pieces carry the superseded reading, and proposes the correction. **PROPOSED; nothing is applied; no pass file is edited; the pieces below are left as written** (their wording is the record of what the readers were given; their pinned hashes stay valid). Names no other city: another location, not used.

## The current fact

`DEVELOPER_RULINGS_LOG.md` L1613, the Item 4 row of `DR-94` (2026-11-02): *"Manchuria declines like the Sinian Federation; Mongolia, East Turkestan, Tibet and Taiwan do not."* This is the answer to the question that `DR-85` (L1529) lists as not decided: "whether China's four pieces and Taiwan decline too". `DR-94` (2026-11-02) is numbered after `DR-85` (2026-11-01 to 2026-11-02) and decides it. In Davis's table the Manchuria row carries the multiplier the ruling names (`SPEC` L28; 0.5855). **The shares of the rows for Mongolia, East Turkestan, Tibet and Taiwan are therefore not open.** No finding may rest on a gap between rows of one tier (`DR-104` item 1), which is a separate bar that stands.

Checked by the orchestrator by reading L1606 to L1617 and L1527 to L1531 of the log on 2026-11-09.

## Why it happened

The Step -1 piece (S1) and the language piece (P89) had `DR-85` in their reading lists and not `DR-94`; the first check's reader for the contract item (U-4) asked the question from `DR-85`'s not-decided row; the S1 piece carried the reading as "reserved, PROVISIONAL"; and the briefs of the Phase 2 piece and the language piece carried it as an orchestrator-verified result (the second item of the shared list taken from the S1 piece). The Phase 2 piece's list contained `DR-94`: its readers B and C found the supersession in Round 3 and the merge recorded it (below). **The error is the orchestrator's:** the S1 and P89 reading lists were built without scanning the rulings log for a later ruling on a question that an included ruling lists as open.

## Where the superseded reading appears

| File and lines | What it says there | Current statement |
|---|---|---|
| `Amendment_Rederivation_S1_…_2026-11-09.md` L40-41 (section 0, "stable in part") | The exact shares of the four rows are a reserved decision (PROVISIONAL) | Not reserved: the four rows do not decline (`DR-94` item 4); no finding depends on a gap within a tier (`DR-104` item 1) |
| same, L72, L93, L110 (the line table, spec L22, L43, L60) | The four rows' shares are open under `DR-85` | ADMITTED; the shares are settled; the rows are not "open" |
| same, L386, L435-L449, L990-L993 (question AM-S1-Q5 and its finding) | "Is Davis's composition block settled?": the four rows may change | Answered by `DR-94` item 4: settled for these four rows; take the current block as the input; do not mark the four rows open |
| same, L1073 (a reserved item) | Reserved and not adopted: the four pieces | Decided: they do not decline |
| `Amendment_Rederivation_P89_Language_…_2026-11-09.md` L29, L88, L615-L616 (AM-P89-K14), L728-L739 (AM-P89-N10), L906 (AM-P89-D34), L1006-L1008 (AM-P89-Q12), L1097, L1387, L1399 | Mandarin's place in the supporting tier is flagged as sensitive to the reserved decision on the four rows; a question asks whether to carry the tier "as computed on the current shares" with that flag | The scenario the flag tests (the four rows declining and freeing points) does not arise under `DR-94` item 4. The supporting tier as computed on the current shares (English, Mandarin, Japanese, German; `Language_Blocs_By_City_2026-11-03.md` L916-L930) stands without the flag; question AM-P89-Q12 is moot |
| `Amendment_Rederivation_P2_Composition_2026-11-09.md` L802, AM-P2-D112 (L954), L1070 | Records that the S1 reading "appears superseded by `DR-94` item 4" and recommends re-checking it | **Confirmed superseded** by the orchestrator's reading of the ruling: `DR-94` item 4 governs, as the later ruling |
| `.t8_brief_P2.md` and `.t8_brief_P89.md`, section 6, orchestrator-verified result 9 (the second item of the S1 list) | The exact shares are a reserved decision left open by `DR-85` | Superseded as above |
| `.t8_check_U4_reader.md`, XU4-40 (and the question "whether Davis's composition block is now settled") | Asks from `DR-85` whether the four rows may still change | Answered by `DR-94` item 4 |

## What does not change

The mapped read spec and the line-by-line classification of the composition region in the S1 piece stand (the verdicts were ADMITTED either way; only the word "open" attached to four rows is superseded). The language piece's other findings stand (the Module delivers the vernacular; the claim register is learned by living there; the tier arithmetic). The Phase 2 piece's findings stand; it already carried the correction.

## For the developer

None. This erratum states a fact the developer already ruled (`DR-94` item 4); it asks nothing. The two questions it makes moot (AM-S1-Q5, AM-P89-Q12) are marked answered in the decisions file rather than put again.

*Filed 2026-11-09.*
