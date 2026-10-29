# Mirny · Amendment re-derivation · Piece 1 (Phase 6) · T8 round record · 2026-10-29

**Companion to** `Amendment_Rederivation_P06_Meaning_2026-10-29.md`. Raw tool output is pasted, not summarized (standing rule). Working files are in this folder as `.t8_amend_P6_*`; the reader outputs and Round 3 replies were copied beside them at the merge.

## Setup
- **Reading list:** `.t8_required_amend_P6.txt`, 38 entries, 7,830 admitted lines (built from the Phase 6 list; ranges re-located by text 2026-10-29: Phase Spine 752-840, Pre-Trip 522-530, Phase 3 269-353 and 414-482; plus the Phase 6 file, its round record, the register, the handoff and the rulings DR-54 to DR-59). 0 missing.
- **Brief:** `.t8_amend_P6_brief.md`, identical for A/B/C, sha256[:16] 76398b8246c15a3a, final at dispatch (M-93).
- **Readers:** three Opus general-purpose agents, dispatched ~07:25. A `a80f0c7abfa2fd4ed` (742 lines, ~143 tool uses) · B `ab5e1869613b46502` (792 lines, ~115) · C `a4bbf0548de8121a3` (856 lines, ~141). All 38 PROOF blocks each.
- **Hours:** started 07:08, finished before 09:00; inside 05:00-14:59.

## Round 2 (mechanical, `Tools/triple_read_verify.py`)
### Run 1 — originals — NOT UNANIMOUS
raw output, excerpted (failing lines only; 189 lines of passing checks omitted — full file: scratchpad `amend_P6/round2_raw_P6.txt`):
```
  agent2   ⛔ QUOTE NOT IN ADMISSIBLE RANGE  (not found anywhere in this file - fabricated, sha1:4fa097b2af7b)
  agent3   ⛔ QUOTE NOT IN ADMISSIBLE RANGE  (not found anywhere in this file - fabricated, sha1:924f808ed0f1)
  agent1   ⛔ LMID  MISMATCH  claimed='| **10** Catalog | shared character canon · the character/pe'  actual=''
  agent2   ⛔ QUOTE NOT IN ADMISSIBLE RANGE  (not found anywhere in this file - fabricated, sha1:d40ddaca0498)
  agent3   ⛔ QUOTE NOT IN ADMISSIBLE RANGE  (not found anywhere in this file - fabricated, sha1:d40ddaca0498)
  agent1   ⛔ LMID  MISMATCH  claimed='an extraordinary ecstatic state but "an awakening to what is'  actual='extraordinary ecstatic state but "an awakening to what is co'
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```
**Diagnosis.** Four `QUOTE NOT IN ADMISSIBLE RANGE` lines (readers B and C, files `No_National_Stereotypes.md` and `Cymatics_reverence.md`): the quotes exist verbatim in the files. Cause: the verifier folds a plain-prose line directly under `QUOTE:` into the quote, and B and C had placed the standing-line-5 `EXEMPT:` note there, as `T8_Standing_Brief_Lines.md` line 5 instructs. A brief/checker conflict, not a reading failure (M-301). Two `LMID MISMATCH` lines (reader A): real copy slips, one off-by-one on the Phase Spine entry (the true middle, line 221, is blank; A had copied line 220) and one extra word ("an") copied from the neighboring line on `07_Zen_Aesthetics_and_Philosophy.md`.

### Run 2 — B and C with a blank line inserted before each `EXEMPT:` line (verification copies; originals untouched), A unchanged
raw output, excerpted (failing lines only; full file: `round2_raw_P6_copies.txt`):
```
  agent1   ⛔ LMID  MISMATCH  claimed='| **10** Catalog | shared character canon · the character/pe'  actual=''
  agent1   ⛔ LMID  MISMATCH  claimed='an extraordinary ecstatic state but "an awakening to what is'  actual='extraordinary ecstatic state but "an awakening to what is co'
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```

### Repair of reader A (developer decision 2026-10-29: "for Reader A, I'd say, Option #1 for now" = same-reader re-check; precedent: Phase 10, 2026-10-11)
A was asked by `SendMessage` to re-derive LMID (and re-copy LINES, L1, LLAST) for the two entries from the files, without being told the right values; reply in `t8_amend_P6_readerA_fieldfix.md`. A's report: the spine LMID was line 221, blank, and it had copied 220; the Zen LMID had an extra "an" from line 48; LINES, L1 and LLAST were already right. A's main file is unchanged.

### Run 3 — final (A with its two repaired blocks swapped into a verification copy; B and C as in Run 2) — UNANIMOUS
raw output (full; `round2_raw_P6_final.txt`):
```
required files: 38
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,752-840] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 386-421,634-665,1075-1226] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.0_Pre-Trip_Inspection.md  [range 522-530] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Factions/Robot_Religions/Polydimensional_Animism/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Factions/Robot_Religions/Polydimensional_Animism/Beliefs.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Factions/Robot_Religions/Polydimensional_Animism/Culture.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Factions/Robot_Religions/Polydimensional_Animism/Rituals.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Factions/Robot_Religions/Polydimensional_Animism/Open_Questions.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Factions/Robot_Religions/Cymatics_reverence/Cymatics_reverence.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/National_Holidays.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Ice-Cold_Buddhism_Research/00_Extraction_Checklist.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Ice-Cold_Buddhism_Research/01_Metaphysics_of_Matter.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Ice-Cold_Buddhism_Research/03_Systems_Thinking_and_Interdependence.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Ice-Cold_Buddhism_Research/04_Technology_and_Machine_Ethics.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Ice-Cold_Buddhism_Research/07_Zen_Aesthetics_and_Philosophy.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Ice-Cold_Buddhism_Research/08_Synthesis_Doctrine_Notes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Ice-Cold_Buddhism_Research/09_Vocabulary_Sheet.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/The_True_Believer_Extraction.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/The_Meme_Machine_Extraction.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,5-8,10-58,60-83,85-98,100-135,137,139-140,142-143,145-157,159,161,163,165,167,169-182,184-188,193-195,197,199,201,203-205,207,209-211,213,215,217-221,224-226,229-230] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md  [range 1-131,156-282,391-473] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_03_Surface_and_Texture.md  [range 269-353,414-482] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_04_Ordinary_Life.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_05_Relation_and_Geometry.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_6.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_06_Meaning.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04b_T8_Rounds_Phase_6.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/DR-56_Amendment_Register_2026-10-13.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/ULM_AUTORUN_HANDOFF.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 (agent-to-agent, `SendMessage` to the same three live agents; each read the other two's files)
| Reader | vs | Verdict | One-sentence reason |
|---|---|---|---|
| A | B | **CONSISTENT** | passages spot-checked are at the cited lines; B's slips are a few anchor errors and one over-reach ("at night") |
| A | C | **CONSISTENT** | every spot-checked passage found; C's hindsight guilt in the body of a finding goes past the ruling and is held reserved |
| B | A | **CONSISTENT** | findings and anchors match B's sources; two PROOF mid-line fields wrong (already known and repaired); "gone by ~2614" should read "elderly or already dead" |
| B | C | **CONSISTENT** | all 21 quotes checked are verbatim; C caught the rulings log growing mid-run; same "gone by ~2614" over-statement |
| C | A | **CONSISTENT** | content matches the sources; slips are two wrong PROOF LMIDs, no EXEMPT lines on two entries, and the alternate axis word "nearest" over-reads the ruling |
| C | B | **CONSISTENT** | content matches; one over-reach ("at night") and a self-reported deleted script in the shared folder |

**6 / 6 CONSISTENT -> gate met.** Replies: `t8_amend_P6_round3_reader{A,B,C}.md`. Each reply carries a SUBSTANCE DIFFERENCES table; the merge follows them.

## Merge dispositions (M-246: union; conservative where they contradict)
- **Axis:** A and C replace it, B keeps the first half; in Round 3 B conceded the first half's ground fails. Three candidates are offered; the developer chooses. A's alternate "nearest goes" dropped (over-reads "a foremost position").
- **Strongest finding:** two forms offered. The collision clause ("the knowledge counsels staying in, the duty sends the best placed out", B and C) is [D] and soft; carried as a reserved sharpening.
- **P6-4:** RE-DERIVE (A, B) over C's conditional REWORD; C accepted this in Round 3.
- **Guilt in hindsight / without fault:** reserved (A's version), not in the body of a finding (C's placement went past the ruling).
- **Human founders "gone by 2614":** corrected to "elderly or already dead" (B's Round 3 catch; `FRM` L169).
- **Debt to the first generation:** [CAND]; felt-ness is in no admitted line.
- **Findings found by one reader only (union, credited):** A: the L248 player row, the provenance rows L371/L373/L375, the raw audit block, the Phase 6 "no strongest finding" fact. B: L51 generators line, L168/L301 reflex rows, L287 nulls, the duty's object cannot predate the relay. C: RF-7 answered in part by DRL L1124, Q-61 answered in part by L1130, Step 2's unamended deficits, the Phase 6 self-contradiction between P6-13 and P6-3/P6-17.
- **Dropped as past the lines:** "nearest", "likeliest at night".

## Snags specific to the round
1. **Brief error (mine):** trap 5 quoted a phrase not in the admitted lines (M-300).
2. **Brief/checker conflict (mine):** the EXEMPT-line instruction vs the verifier's continuation rule (M-301).
3. **Inputs not frozen:** DR-74 and DR-75 were appended to the rulings log during the round; the admitted span ends at 1226; no admitted line moved (C S1; A, B corroborate).
4. **Safeguard classifier note:** reader C's completion notice said the safety classifier was unavailable (rate-limited) when it reviewed that subagent's work; its output was verified by the mechanical and peer checks above.
5. **Independence:** B's deleted script's directory listing showed that A's and C's output files existed; none was opened before Round 3.

## Audits
**Quotation audit** (`Tools/quotation_audit.py <pass> --files Amendment_Rederivation_P06_Meaning_2026-10-29.md --own-pass`): instrument valid (all positive controls found, negative control absent); 68 fragments tested, 40 not found, 9 of them in table cells and 31 in prose. **Triage by hand:** the tool pairs quotation marks across lines, so most flagged fragments are the connective text between two adjacent quotations. A second hand-written check (each double-quoted string of 5+ words tested against all 38 required files plus every pass file, after the same normalization): 117 tested, 38 not found, of which 13 were real non-verbatim quotations, now fixed in the merged file (paraphrases that had been put in quote marks were re-marked as italics; two quotes were corrected to the source's exact words: "the only reading of wind and ice made public and trusted", "the storm that breaks the relay also stops people walking"). The remaining 25 are quote-pairing artifacts. **American-English sweep** (British spellings): 0 hits in either file. **Observations log:** M-300, M-301, M-302 written. **Not run:** the handoff audit and phase-discipline check (they audit the pass's own phase files, which this piece did not write).

