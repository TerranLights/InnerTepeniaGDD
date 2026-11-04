# Mirny · Amendment re-derivation · Piece 3 (Phase 8, Making) · T8 round record · 2026-11-03

**Companion to** `Amendment_Rederivation_P08_Making_2026-11-03.md`. Raw tool output is pasted, not summarized, and excerpts are headed as such. Working files are in this folder as `.t8_amend_P8_*`.

## Setup
- **Reading list (trimmed, `DR-74`):** `.t8_required_amend_P8.txt`, 40 entries, about 6,599 admitted lines (the Phase 8 file; the clarified Piece 1 and Piece 2 files; the rewritten register; the 2026-11-03 reconciliation note and the live Mirny spec; the Phase Spine at its Phase 8 span 955 to 1025 [re-located by text]; the rulings log; Disciplines 00b and 00d; the National Stereotypes file; the robot physiology file; the Robot Universals files at their `DerivationMechanisms` address; the Input Contract and the Frame at their spans; and **only the cited spans** of Phases 2 to 7). Phase 7 citations were shifted +5 and the Mirny spec +22 at build; **the Phases 2 to 6 spans were left at Phase 8's uncorrected numbers (two lines off): a build error, recorded as snag 1 of the merged file and as AQ-36.**
- **Brief:** `.t8_amend_P8_brief.md`, identical for A, B and C, sha256[:16] `83158450c33ec636` (equal to the draft hash at build; recomputed at the merge: unchanged), final at dispatch (`M-93`). It carried the two fixes from Piece 1 (no unverified quotation, `M-300`; a blank line before `EXEMPT:`, `M-301`) and the developer's language and stage rules.
- **Readers:** three Opus general-purpose agents, dispatched 2026-11-03 about 16:23 (machine clock). A `a94a88d38536a6ea6` (1,203 lines, ~240 tool uses, ~41 minutes) · B `ace91d61387134517` (1,047 lines, ~236, ~35 minutes) · C `a8e394a7542a08f9d` (1,102 lines, ~222, ~35 minutes). All 40 PROOF blocks each. The rulings log was not appended to, and no list file was edited, while the round was open.
- **Hours:** the developer waived the 05:00 to 14:59 law for the Mirny blocks (2026-11-03, after 15:00); this piece ran under that waiver.

## Round 2 (`Tools/triple_read_verify.py`) — NOT UNANIMOUS on the first run; UNANIMOUS after a same-reader re-check
**First run.** 120 field sets (40 entries × 3 readers); 118 matched; **2 failed, both Reader A's.** raw output, excerpted (lines omitted: 114 matching ground truth; scratchpad `amend_P8/round2_raw_P8.txt`, copy `.t8_amend_P8_round2_raw.txt`):
```
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Fed
  agent1   ⛔ LINES MISMATCH  claimed='105'  actual='101'
...
=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subne
  agent1   ⛔ LLAST MISMATCH  claimed='**Not on the redo list (checked):** the other-city names in '  actual=''
...

=== VERDICT ===
⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.
```
**Repair (the Piece 1 default, a same-reader re-check).** Reader A was asked to re-derive the two blocks by hand from the real files. Its answer: the Phase 2 entry has **101** admitted lines (it had mis-added; LMID is line 301, which is blank); in the Amendment Notes entry **line 103 is blank**, so LLAST is empty (LINES stays 37, LMID is line 85, blank); L1 and QUOTE unchanged. The corrected blocks are in `.t8_amend_P8_readerA_fieldfix.md`.

**Re-run on verification copies** (Reader A's file with the two corrected blocks substituted; B and C unchanged). raw output, excerpted (lines omitted: the per-file results; copy `.t8_amend_P8_round2_raw_rerun.txt`):
```

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```
All 120 field sets now match ground truth.

## Round 3 (agent-to-agent comprehension cross-check) — 6/6 CONSISTENT
Each reader read the other two's bodies and reported by SendMessage; replies are in `.t8_amend_P8_round3_reader{A,B,C}.md`. (A read B's body L1 to L726 and C's L1 to L780; B read A's L1 to L880 and C's L1 to L780; C read A's whole body L1 to L881 and, for B, the receipt, the inventory tail, the register table, Lists W and C, the re-derivation headings, the KEEP list, the axis and the snags, with a pattern search of the rest.)

### Agreed by all three
The register-row categories (RE-DERIVE for P8-12, P8-14, P8-24, P8-27/28; P8-4 KEEP with the reword moved to P8-1 L226; P8-25 a REWORD; P8-2 KEEP); the forecast-language overstatement; the Q-74 split (`DR-56` supersedes the instrument half, `DR-59` holds the trigger half); the Idelsk-Uralia "founding wave" tag against PA-55 and `DR-54`; the list-span snag; the axis surviving with a changed half ("Prepared" stands, "not predicted" fails).

### Concessions
| Reader | Concedes |
|---|---|
| **A** | lines missed (L269, L344, L387, L393, L463, L471, L519, L553, L579, L538, L746, L144); C's culture/language split at L536 and the conditional note on P8-2; the robot half of "speaks Hawaiian" must be conditional; CAND-F1 and CAND-D1 grounds (B, C); C's tense-count snag; withdraws its conditional third axis option and narrows its axis gloss; accepts C's added request on the protocol's language. |
| **B** | P8-25 is a REWORD; the `NNS` L15 / `DR-55` tension; the R-21/R-43/R-67/R-88 snag; CAND-L2 falls; fold CAND-N1 into CAND-S1 (and drop CAND-N2 as a candidate); the humor edge on reproach; A's point on L508; `REG` L35 and L134; the extra missed lines A and C found (L145, L191's second sentence, L350/L354, L371, L387, L463, L508, L519, L585, L995, L997, L1001, L1009, L1011, L1012, L1026, PA-53 L879). |
| **C** | its Tower date for Hawaiian becoming Tepenian (the rule gives none); "never by a festival"; P8-2 stays KEEP (its conditional moves to the reserved rows); the list-span snag; the R-21/R-43/R-67/R-88 snag; ten list lines it missed (including L19); the recommended axis form ("handed on" / "passed on"); the distinctiveness of the language result ("little"). |

### Holds
| Reader | Holds | Against |
|---|---|---|
| **B (with C)** | the CAND-F1 ground is re-grounded at L269 (the verdict "stands" is the same in all three) | A |
| **B (with C)** | A's axis gloss, tying *Prepared* to the duty, leans on a readiness claim all three reserve (AF8-1) | A (A narrowed it) |
| **B (with A)** | "never by a festival" is withdrawn | C's keeping it (C then conceded) |
| **C** | P8-27's tense-count mismatch is a real snag (the printed table has 25 labels in 13 rows) | none disputes it |
| **C** | the conditional edge on humor stays conditional on AR-26 | emphasis, not contradiction |

### Counts of missed lines (granularity, not substance)
A: 43 wind-premise rows (about 64 to 70 line citations) and 28 composition/language rows (37 line citations). B: 61 and 30. C: 59 (plus 5 inside registered findings) and 26. Differences are mostly how many lines each reader grouped into one row.

### Items the cross-check moved out of the body (the same discipline as Piece 2)
The Hawaiian-to-Tepenian change tied to the Tower (struck); "never by a festival" (struck); the conditional sun-dated season on the plate (reserved AF8-8); readiness kept for the duty (reserved AF8-1); the household as the one place the reading crosses bodies (RF-16 falls); A's conditional third axis option (withdrawn); CAND-L2 (falls); CAND-N1 (folded into CAND-S1) and CAND-N2 (a spread row, not a candidate).

## Process snags (for the methodology findings)
1. **The reading list's Phases 2 to 6 spans were two lines off Phase 8's citations** (the build re-located Phase 7 and the spec only). A trimmed-list builder should re-locate every earlier-phase span by text, not by offset.
2. **The brief's "IDs not opened" list was wrong for R-21, R-43, R-67 and R-88.** The brief should be generated from the list, not hand-written.
3. **One reader mis-added an admitted set (105 against 101) and copied a line where the last admitted line was blank.** The blank-last-line trap (`LLAST:` with nothing after) recurs; the brief's standing line 1 already covers it.
4. **Reader outputs took 35 to 41 minutes each** on the 40-entry list (about 6,600 lines), the longest piece so far.
5. **The Round 3 cross-check again moved claims out of the body**, and again caught lines the first pass missed (about 10 per reader): it is doing real work.
6. **Two agents finished close together in time and their results arrived mixed with other pieces' notifications**; the merge worked from the scratchpad files, not from the notifications.
7. **Methodology items `M-305` onward** are not written here (no entry was appended to any log by this fork); the orchestrator records them.
