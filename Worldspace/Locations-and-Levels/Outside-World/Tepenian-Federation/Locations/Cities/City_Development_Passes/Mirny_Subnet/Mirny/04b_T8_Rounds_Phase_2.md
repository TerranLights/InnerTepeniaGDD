# Mirny — Step 4 · Phase 2 · T8 round record

**Pass:** Mirny · ULM · Step 4, Phase 2 (Composition & Arrival) · 2026-10-03, dispatched 09:16–09:51, Round 3 closed before 10:16 (clock check 09:51: in window).
**Written file:** `04_Phase_02_Composition_and_Arrival.md`. **Required-reading list:** `.t8_required_04_Phase2.txt` (15 entries, ≈ 2,740 admitted lines).
**Reader files:** `.t8_Phase2_reader{A,B,C}.md` (417 / 662 / 467 lines) · `.t8_Phase2_round3_reader{A,B,C}.md` (85 / 160 / 110 lines). Not canon, not an input; archived with the pass (`DR-27`).

## Round 1 — dispatch
Three `general-purpose` agents, one brief (`T8_PHASE2_PROMPT`), differing only in the reader letter and its one output file. The brief carried the `DR-6` line (read at the named
range; no graphify; no repo-wide search; a graphify hook notice is disregarded as compliance, not override), the binding rulings (`DR-4`, `DR-9`, `DR-11/12`, `DR-15/16`, `DR-28`, GPS law, `DR-8`, `RV-1…RV-6`),
the structure to produce, the `Canon opened` receipt and the `Generators used:` line, and PROOF blocks last. Reader A: 35 tool uses; B: 43; C: 34. Each reader reported disregarding the graphify
hook per the brief. **One housekeeping event:** reader B wrote a temporary draft file in the Mirny folder while assembling its output; a hook blocked `rm`, so it moved the draft to the scratchpad; the folder holds only the reader's one output file.

## Round 2 — `triple_read_verify.py`, raw output (pasted, not summarized)
```
$ python3 Tools/triple_read_verify.py .t8_required_04_Phase2.txt .t8_Phase2_readerA.md .t8_Phase2_readerB.md .t8_Phase2_readerC.md
required files: 15
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Scaffold.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Real_World_Influences.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-38,370-376,474,476,480-481,488,588,590,592,596-597,603] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,401-470] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md  [range 1-20,380-393] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00_Frame.md ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```
Exit status 0. Re-run once after the Round 3 files were written (identical result), to capture the full output above.

## Round 3 — peer cross-check (same three readers, `SendMessage`; each pointed at the other two readers' files)
The prompt carried the four questions of `T8_CROSSCHECK_PROMPT` plus the fifth section (disposition differences: (a) the other reader is right · (b) mine is right · (c) a developer question), and required a disposition on
five known points: (i) midnight sun ~27 vs ~29 days · (ii) the "founding wave" annotation vs `DR-9` · (iii) the treaty's status · (iv) the arrival-mode verdicts · (v) the "who is not here" lists.

| Reader | vs reader | Verdict | Reason in one sentence |
|---|---|---|---|
| A | B | **CONSISTENT** | B read the same 15 files at the same ranges (PROOF fields identical); differences are judgment calls and one overstated limit, not source contradictions |
| A | C | **CONSISTENT** | C read the same files at the same ranges; its flaws are two over-reaches in one verdict row and one understated tension |
| B | A | **CONSISTENT** | same admitted lines, founders, tiers, arithmetic and quotations; two slips (E8, E6) are inference errors, not a different read |
| B | C | **CONSISTENT** | same findings on founders, the unread eleven, R-13 and the treaty text; a misreading of `RP` L88 and an overstatement of "Dominant" are inference slips |
| C | A | **CONSISTENT** | quotations, line numbers and PROOF lines match; the two errors are local and change no verdict |
| C | B | **CONSISTENT** | quotations, anchors and PROOF lines match; its extra finds are all confirmable from admitted lines |

**6 / 6 CONSISTENT → gate met.** *(Each reader also cross-checked every other reader's PROOF fields: all identical across the three, including the blank-line positions.)*

### What Round 3 caught (the gate adding signal, not passing trivially)
Real errors found in another reader's output, all confirmed against the source and none carried into the written file: **E8** (A: "the Notable tier's nations are Southeast Asian"; three of the seven are not, `CEN` L376) · **E6** (A: "the physically frail among robots" are absent; `RP` L67 says robot components degrade) · **C's reading of `RP` L88**
as "the same sort" as the treaty's ties (the quote includes a means ground the treaty lacks) · **C's "Fled, human: fits in its generative part"** (rests partly on a personhood withdrawal that applies to robots, not humans; IV.2.1) · **B's "No stock has a majority"** listed as a tier property (it is a property of the weight model) · **A's "does not fit" for human *Fled*** (stronger than the files allow) · **A's "nothing selected"** (the arrangements are unwritten).

### Dispositions on the five known points
| Point | Disposition | Written as |
|---|---|---|
| (i) midnight sun | all three state both; nothing rests on the difference | ~29 (canon, `CON` C-2); ~27 in-frame noted from `RES` §2 |
| (ii) founding wave vs `DR-9` | all three: `DR-9` alone; the annotation is not an arrival order; `FRM` Q-34 vs R-10 is a real internal conflict (A found it) | nothing rests on it; Q-35 stays open |
| (iii) treaty status | two senses of "ratified"; draft-tier is the safe outcome; substance confirmed, wording draft (B accepted the tiering split from A and C) | [CONF] / [DRAFT]; "unratified" not used |
| (iv) arrival modes | agreed on all but two cells: human *Fled* → **cannot be read** (A and C withdrew); robot *Sentenced* → **does not fit**, facts recorded (B conceded as a labeling choice) | merged table |
| (v) who is not here | convergent core; additions credited (B: E3; C: E10; A: E9, E7-children); out of the list: observers → Phase 5, "no living teacher" → G4; dropped: "frail"; B's E-4 considered, not adopted | §E |

## Merge (per the amended `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2, `M-246`)
Contradictions → the most conservative current (post-Round-3) view, the split named. Population-origin material → DEMOTED, never EXCLUDED (nothing here needed that exception: no reader excluded any origin material; all three used the three founding stocks as starting stock and refused to write the other eleven).
No contradiction → union, each single-reader find credited (provenance table at the end of the phase file). **Quotation re-check by script:** all 72 italic-quoted strings in the phase file were matched against the 15 inputs; 7 mismatches were found and corrected before the write was final (a paraphrase set in quote marks, an inexact IV.2.2 quotation, three reader-level
descriptors, and two of this file's own formulations), and every quotation now matches its source or is marked as the file's own wording.

## Snags in this round (the recording law)
- The brief's "per 03_Research" for ~29 days was half right (the research gives both numbers). Caught by all three readers.
- Census line-number drift of 2 (and contract-row drift of 2) in the Frame, the datasheet and the contract: found independently by all three readers; cited by quote in the phase file. The broader question (line-anchored citations into files edited 2026-10-01) is queued for the pass's close.
- One reader's draft file had to be moved aside (a hook blocks `rm`).
- The hook notice to run graphify appeared on essentially every tool call in the readers and in the orchestrator's own Bash and Read calls; the orchestrator's reads were of named files, not codebase questions.
