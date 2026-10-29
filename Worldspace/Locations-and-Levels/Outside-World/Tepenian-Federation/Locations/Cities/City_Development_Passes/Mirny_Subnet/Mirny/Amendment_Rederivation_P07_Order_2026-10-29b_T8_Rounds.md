# Mirny · Amendment re-derivation · Piece 2 (Phase 7, Order) · T8 round record · 2026-10-29

**Companion to** `Amendment_Rederivation_P07_Order_2026-10-29.md`. Raw tool output is pasted, not summarized. Working files are in this folder as `.t8_amend_P7_*`.

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_P7.txt`, 16 entries, about 3,490 admitted lines (the Phase 7 file; the clarified Piece 1 file; the rewritten register; the old Phase 6; the Phase Spine at 82-272 and 841-954 [re-located by text]; the rulings log at 386-421, 634-665, 1075-1226 and 1427-1445; Disciplines 00b and 00d; the National Stereotypes file; the robot physiology file at 71-190 and 329-374; the Input Contract and the Frame at their spans; and **only the cited findings** of Phases 2, 3, 4 and 5: 30, 12, 23 and 69 lines). 0 missing.
- **Brief:** `.t8_amend_P7_brief.md`, identical for A/B/C, sha256[:16] fb3d0512d404d988, final at dispatch (M-93). It carried the two fixes from Piece 1: no unverified quotation (M-300) and a blank line before `EXEMPT:` (M-301).
- **Readers:** three Opus general-purpose agents, dispatched ~08:58. A `a494158cb60b419e1` (708 lines, ~112 tool uses) · B `af1cfe84aafa87a14` (710 lines, ~74) · C `ad9aefd6dc929301c` (747 lines, ~90). All 16 PROOF blocks each. Rulings-log rule honored: **no entry was appended to `DEVELOPER_RULINGS_LOG.md` or any list file while the round was open** (the Piece 1 snag).

## Round 2 (`Tools/triple_read_verify.py`) — UNANIMOUS on the first run
raw output (full; scratchpad `amend_P7/round2_raw_P7.txt`):
```
required files: 16
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,841-954] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 386-421,634-665,1075-1226,1427-1445] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md  [range 71-190,329-374] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md  [range 1-20,207-393] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md  [range 156-282,391-473] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md  [range 205-234] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_03_Surface_and_Texture.md  [range 197-208] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_04_Ordinary_Life.md  [range 111-116,118-124,126-129,146-146,148-151,153-153] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_05_Relation_and_Geometry.md  [range 109-114,130-137,139-141,148-151,163-169,200-201,203-208,210-214,270-272,278-287,289-301,317-318] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_06_Meaning.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Amendment_Rederivation_P06_Meaning_2026-10-29.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/DR-56_Amendment_Register_2026-10-13.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_07_Order.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 (agent-to-agent, `SendMessage` to the same three live agents)
| Reader | vs | Verdict | One-sentence reason |
|---|---|---|---|
| A | B | **CONSISTENT** | one quotation spans L104-105 but is cited as L105 only |
| A | C | **CONSISTENT** | C's whitespace counts used a folder glob that reached one unlisted file; disclosed, nothing used |
| B | A | **CONSISTENT** | every cited line found; A goes past the rulings three times (warnings reach the unlearned; the organization's authority by practice; warnings never bind) |
| B | C | **CONSISTENT** | verbatim; C's snag 2 is overstated (the log's list ends "and others"); C disclosed a folder-wide count over files outside its list |
| C | A | **CONSISTENT** | one wrong line (RP L105 should be L104); "two" vs "three" faculties disagree inside A's file; the organization's authority by practice and CAND-P4 "refused" go beyond the rulings |
| C | B | **CONSISTENT** | B caught P5 L281's M1 falsifier, which C missed; "hazards curated" misnames what is curated; one quotation spans L104-105 |

**6 / 6 CONSISTENT -> gate met.** Replies: `t8_amend_P7_round3_reader{A,B,C}.md`; each carries a SUBSTANCE DIFFERENCES table (17, 23 and 22 rows) that the merge followed.

## Merge dispositions (M-246)
- **Axis:** all three: the claims half survives, the fast-call half fails. A and C: "Knowledge curated; claims unarbitrated" / "Curated knowledge, unarbitrated claims" (same claim). B: "Claims unarbitrated; hazards curated" — conceded in Round 3 (what is curated is the protocol, `DRL` L1140). Recommended in the merge: the A/C form; the developer chooses.
- **Beyond the rulings, moved out of the body (eleven, to [D], conditional or reserved):** the organization's authority "by practice"; warnings reaching the unlearned (conditional on AR-1); a general warning never binding (AR-19); the duty concentrating on those who hold the unstopped hours (AF7-7); learning the wind raising one's exposure to the duty (AF7-8); a warning's silence looking like calm (AF7-3); over-response under one-sided guilt (AF7-2); robot-vs-human likelihood of being best placed (dropped, near a spread); "nearest"; "likeliest at night"; guilt in hindsight.
- **P7-14:** RE-DERIVE (A, C) over B's row-by-row REWORD (same verdicts). **P7-26:** union of A, B, C (heading L382, scope line L380, third order L391). **P7-6:** KEEP for the wind plus a non-wind REWORD by `DR-55`; the register's "adopted" label is inexact (ruled). **CAND-P4:** C's split (a compelling rule refused; non-compelling coordination open). **CAND-10:** B's label for the curating organization. **Phase 5's M1** falls as stated (B). **Q-72 mismatch** (C, confirmed by B) -> AQ-16. **AR/AQ numbering:** renumbered once (AR-17 to AR-27, AQ-10 to AQ-16, AF7-1 to AF7-10).

## Snags specific to the round
1. **The Round 3 message to reader A contained a garbled parenthetical about the proof-block count** (a drafting slip of mine); harmless, the verdict request was clear.
2. **A folder-wide count by reader C** reached one unlisted file; disclosed, nothing used.
3. **Readers' output folder:** no reader wrote outside its output file.

## Audits
**Quotation check** (each double-quoted string of five or more words tested against all 16 required files plus every pass file and the rulings log, after the verifier's normalization): 83 tested, 24 not found; 12 were real non-verbatim quotations (paraphrases put in quote marks, one bracketed edit, one fragment lacking its tail), all fixed in the merged file (re-marked as italics or corrected to the source's exact words); the remaining 12 are quote-pairing artifacts of the checker. **American-English sweep** (British spellings): 0 hits in either file. **Observations log:** M-303, M-304 written. **Not run:** the handoff audit and phase-discipline check (they audit the pass's own phase files, which this piece did not write).

