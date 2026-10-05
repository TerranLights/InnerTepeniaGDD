# Mirny — Step 4 · Phase 3 · T8 round record

**Pass:** Mirny · ULM · Step 4, Phase 3 (Surface & Texture) · 2026-10-03, Round 1 dispatched about 10:55, Round 2 at 11:34, Round 3 closed before 12:00 (clock check 11:34: in window).
**Written file:** `04_Phase_03_Surface_and_Texture.md`. **Required-reading list:** `.t8_required_04_Phase3.txt` (14 entries, ≈ 2,780 admitted lines).
**Reader files:** `.t8_Phase3_reader{A,B,C}.md` (491 / 476 / 526 lines) · `.t8_Phase3_round3_reader{A,B,C}.md` (76 / 107 / 134 lines). Not canon, not an input; archived with the pass (`DR-27`).

## Round 0 — the required-reading list and what is NOT on it
Built from the Phase 3 `MUST OPEN` block (`03_The_Phase_Spine.md` L476–490) and the pre-trip row. **Files:** the spine's Phase 3 specification and the every-phase mechanics, the Climate READER, the Mirny spec at the same
line ranges Step 2 used (whole-line EXCLUDED lines omitted; split lines admitted whole with the contract's §B character map made binding in the brief), the robot physiology file, the two discipline files,
the contract (rulings box and §B map), the pass's own earlier steps and the Phase 2 file, the Phase 3 datasheet, and the binding law file. **Not files, handled by the orchestrator:** concept art (empty, verified
by `ls -a`), the megasheet physical-infrastructure file (withheld, conflict recorded), the Davis geosciences folder (n/a, a different location), `Stations/` (background only), the Cultural Synthesis Techniques
file (not a ULM input, `DR-14`). All 14 entries verified to resolve with no range beyond end of file.

## Round 1 — dispatch
Three `general-purpose` agents, one brief (`T8_PHASE3_PROMPT`), differing only in the reader letter and its one output file. The brief carried the `DR-6` line, the binding rulings, the **character-level §B rule for
the spec** (ADMITTED spans only as findings; DEMOTED as marked context; EXCLUDED never), the named failure modes (inventing texture; the headline institution's profile as the general answer; **an empty
sensory sub-field is a result, never filled**), the Phase 3 structure, the `Canon opened` receipt with an inbound handoff sweep, the `Generators used:` line, a quotation rule (every string in quotation marks
verbatim), and PROOF blocks last. Tool uses: A 31; B 59; C 34. Each reader reported disregarding the graphify hook per the brief.

## Round 2 — `triple_read_verify.py`, raw output (pasted, not summarized)
```
$ python3 Tools/triple_read_verify.py .t8_required_04_Phase3.txt .t8_Phase3_readerA.md .t8_Phase3_readerB.md .t8_Phase3_readerC.md
required files: 14
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 82-272,472-531] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Mirny.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Mirny.md  [range 1-3,5-8,10-58,60-83,85-98,100-135,137,139-140,142-143,145-157,159,161,163,165,167,169-182,184-188,193-195,197,199,201,203-205,207,209-211,213,215,217-221,224-226,229-230] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md  [range 1-20,207-393] ===
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

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Phase_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```
Exit status 0. 42 / 42 field checks (14 files × 3 readers) match ground truth; blank-line positions (the spine copy's LMID and LLAST, the spec's and the Frame's LMID) were handled identically by all three.

## Round 3 — peer cross-check (same three readers, `SendMessage`; each pointed at the other two readers' files)
The prompt carried the four questions plus the fifth section (disposition differences) and required a disposition on eight known points: (i) sea-ice dates · (ii) the ring · (iii) the terrain under the city ·
(iv) the spec lines edited 2026-10-01 vs the contract's spans · (v) the contract's `[VISION-DATED]` tag · (vi) the four sensory sub-fields per body · (vii) the split, the seam and the Retroactive Mechanism ·
(viii) seasonal variance. It asked specifically about non-verbatim quotations, EXCLUDED-span use, invented texture and comparison to another city.

| Reader | vs reader | Verdict | Reason in one sentence |
|---|---|---|---|
| A | B | **CONSISTENT** | B's PROOF fields, receipts and quotations match; no excluded span, no other city; defects are three small unsupported embellishments and two line-anchor slips |
| A | C | **CONSISTENT** | C's PROOF fields and quotations match; the one drift only C caught (the spec edits) was confirmed; defects are one unsupported word and several flagged derivations |
| B | A | **CONSISTENT** | every testable claim matches and PROOF blocks are identical; the over-reaches are labeled [D] or reserved |
| B | C | **CONSISTENT** | all PROOF fields and 125 quotations match; the contract-map handling is in two places sharper than B's own; over-reaches are minor and marked [D] |
| C | A | **CONSISTENT** | every quotation verbatim, no excluded span, all 14 PROOF blocks match; three over-reaches tagged [D] or reserved |
| C | B | **CONSISTENT** | every quotation verbatim, no excluded span, all 14 PROOF blocks match; unsupported ordinary-day and visitor claims are derivations B labels as such |

**6 / 6 CONSISTENT → gate met.** *(Machine checks the readers ran on each other: 84–125 quotations per file, 0–1 genuinely non-verbatim; all PROOF fields identical across the three.)*

### What Round 3 caught (the gate adding signal)
**The spec was edited after the contract was written** (2026-10-01, the heritage cleanup): five spec lines (L21, L150, L152, L154, L229) are shorter than the contract's §B character spans assume. **Only reader C
detected it**; A and B, reading by the contract's spans, had not noticed, and a byte-versus-character coincidence on L150 would have shown a clean match to a byte slicer. Also caught: the contract's
`[VISION-DATED 2026-07-05]` tag is **not in the spec text** it annotates (C; confirmed); `00_Frame` A.1's quotation of L150 is **not verbatim** (C; confirmed); the `00_Frame` anchor to the contract's L3 row is two lines
stale (A); and a list of over-reaches in all three outputs (full list in the phase file's Snag 6), including "dry", "loud" flanks, "the street at night is empty", "a calm exists offshore", "a blue sky", an
unsourced obliquity constant, a time budget for the typical resident, and a reading of "dangerous regardless of cold protection" that spelled out hazards no file names.

### Dispositions on the eight known points
| Point | Disposition | Written as |
|---|---|---|
| (i) sea ice | all three record the conflict; **(c)** a developer matter; A's "onset markers" reconciliation not adopted | both stated, unadjudicated (`RV-9`); Q-40 |
| (ii) the ring | **(b)** only "outer wind-fortified ring" with a sheltered core is admitted; closure, solidity, arcs, roofing are conditional [D] | PA-15; Q-38; "if closed" |
| (iii) terrain | **(c)** both branches, undecided; A's ice-branch property not adopted | R-25; Q-39 |
| (iv) spec edits | **(a)** C is right; L150 chars 1–786 still align (A, B re-measured); one phrase usable under either numbering | Snag 3; docket correction, never applied |
| (v) the tag | **(a)** C is right: the tag is the contract's label; the span stays ADMITTED, with 2026-07-05 a canon-edit date | Snag 2 |
| (vi) the sub-fields | smell agreed (label corrected); robot hearing: A and C right, B's conditional dropped; feel: single-finder items credited; first impressions: B's entry/relay claims demoted | §B |
| (vii) split, seam, mechanism | split: empty slot, human interior [CORR] only; seam: union of five latent seams; mechanism: union of the sink and the ring | §C, §D, §F |
| (viii) seasonal variance | no contradiction; "June–August inside a May–September plateau"; "inside largely the same, outside not" | §E |

## Merge (per the amended `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2, `M-246`)
Contradictions → the most conservative current (post-Round-3) view, the split named. Population-origin material → DEMOTED, never EXCLUDED: not engaged (this phase writes no origin culture).
No contradiction → union, each single-reader find credited (provenance table at the end of the phase file). **Quotation re-check by script:** all 55 italic-quoted strings in the phase file match the admitted
sources verbatim; the plain-quoted strings the script could not find are, by inspection, the readers' struck claims quoted in order to strike them, the alternate axis names, and scare quotes.

## Snags in this round (the recording law)
- **The spec edit drift is a standing hazard for every later phase that reads the spec by the contract's §B spans:** L21, L150, L152, L154, L229. Later phases must re-measure before using any text on those lines.
- The brief's phrase "the enclosed ring" came from the Phase 2 file's feeds and the spine's type-variance line; the Frame assigns no *Enclosed* modifier. All three readers read it conservatively; the brief's wording was
  the source of the near-error (one reader's "closed ring" sentence), caught in Round 3.
- The hook notice to run graphify appeared on essentially every call, again.
