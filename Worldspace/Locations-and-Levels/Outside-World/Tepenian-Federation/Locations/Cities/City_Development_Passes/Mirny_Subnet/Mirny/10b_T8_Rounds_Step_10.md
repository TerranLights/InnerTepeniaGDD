# Mirny — Step 10 · The Readiness Check · T8 round record

**Pass:** Mirny · ULM · Step 10 · 2026-10-12 to 2026-10-13.
- **Clock checks:** 2026-10-12 ~11:57 (list, brief and checkpoint; Round 1 dispatched) · ~12:02 (readers B, A and C finished, in that order) · ~12:05 (Round 2) · ~12:10 (Round 3 requested; replies by ~12:20) · evening of the 12th (file-system half, partly) · 2026-10-13 05:02 onward (the Symbol review, the remaining checks, the merge, this record).
- **Files:** list `.t8_required_10_Step10.txt` (3 entries, 669 admitted lines: the runbook's Step 10 text L3045–L3133, `MEMORY.md` in full at 151 lines, `06_Worked_Example_Provenance.md` in full at 429 lines); brief `.t8_Step10_brief.md`; readers `.t8_Step10_reader{A,B,C}.md` (239 · 205 · 209 lines; 3 PROOF each); Round 3 `.t8_Step10_round3_reader{A,B,C}.md`; Round 2 raw `.t8_Step10_round2_raw.txt`. A deliberately lean design (the plan limit): the readers did the **reading half** (the eleven items restated, the index scan, the manifest scan, the limits); the orchestrator ran the **file-system half** with commands and pasted raw output below.

## Round 1 — what each reader wrote
| Reader | Distinctive |
|---|---|
| A | the fullest limits list (ten); the alias hazard (a scan for the new name finds one of four lines); the header gap list; the stale `06` L310 against L362–364 contradiction (Q-147 in its numbering) |
| B | the line-by-line Casey table; L124 classed CHARACTER-STATEMENT by `06` L315's own tiering; the runbook *failed three times* staleness; the cited harness `git status` fact, labeled |
| C | six subject lines found by eye, then Casey L313 caught by its own grep; the *§3d* question; hits classed ATTRIBUTE-ONLY with L124 flagged sector-adjacent |

## Round 2 — `triple_read_verify.py` (raw output, excerpted: paths shortened)
**UNANIMOUS — CLEARED TO WRITE**, 3/3 files, 9/9 field sets, first run (full raw: `.t8_Step10_round2_raw.txt`).
```
required files: 3
agents: agent1, agent2, agent3

=== …/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 3045-3133] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== ~/.claude/…/memory/MEMORY.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== …/Worldspace/Locations-and-Levels/Universal_Location_Methodology/06_Worked_Example_Provenance.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE

```

## Round 3 — peer cross-check
All six replies **CONSISTENT**. Conditions applied at the merge:
| Point | Decision |
|---|---|
| MEMORY L124 | A and B CHARACTER-STATEMENT, C ATTRIBUTE-ONLY: merged to the conservative value; C conceded in Round 3 |
| L103 | all three ATTRIBUTE-ONLY; A and C flag it borderline: kept as attribute, borderline noted |
| Casey lines in `06` | all three: the same eleven lines; C's first miss of L313 corrected by its own grep |
| Limits | union of the three lists (A ten, B eleven, C ten); no conflict |
| Reader B's *plus its rationale* for L124 | softened: the line names an industry and a link, not a mandate |
| Source outside the list | A's and B's use of the session-start `git status` kept as labeled out-of-scope facts, verified directly by the orchestrator (item 2) |
| Reader B read runbook L3134 (one line outside) | nothing drawn from it; recorded |

## File-system half — raw output (excerpted where stated)

### Item 6 — every path named in the handoff
```
tokens: 20 resolved: 20 unresolved: 0
```

### Item 9 — Gate 0 outward: files named by the tracker's Mirny row (L533) and LAST TOUCHED (L361), with line counts
*(excerpt as run on 2026-10-12 before Step 9's files existed; the four Step 0–3 round records print MISSING because they are archived, see below)*
```
Gate 0 outward — Mirny tracker row (L533) and LAST TOUCHED (L361): files named, and what each contains (line count)
  EXISTS   656 lines  00.1_Step_MINUS-1_Input_Contract.md
  EXISTS   653 lines  00_Frame.md
  EXISTS    49 lines  01_Inherited.md
  EXISTS   176 lines  02_Spine.md
  EXISTS   144 lines  03_Research.md
  EXISTS   561 lines  04_Phase_02_Composition_and_Arrival.md
  EXISTS   539 lines  04_Phase_03_Surface_and_Texture.md
  EXISTS   400 lines  04_Phase_04_Ordinary_Life.md
  EXISTS   585 lines  04_Phase_05_Relation_and_Geometry.md
  EXISTS   375 lines  04_Phase_06_Meaning.md
  EXISTS   705 lines  04_Phase_07_Order.md
  EXISTS  1023 lines  04_Phase_08_Making.md
  EXISTS   568 lines  04_Phase_09_Populations.md
  EXISTS   627 lines  04_Phase_10_Catalog.md
  EXISTS   836 lines  05_Reconciliation.md
  EXISTS   378 lines  06_Differentiation.md
  EXISTS  2025 lines  07_QA_Gates.md
  EXISTS   247 lines  08_Review_Panel.md
  EXISTS    96 lines  09_Record.md
  EXISTS   291 lines  09.5_Log.md
  EXISTS   138 lines  09b_T8_Rounds_Step_9.md
  EXISTS   142 lines  08b_T8_Rounds_Step_8.md
  EXISTS   152 lines  07b_T8_Rounds_Step_7.md
  EXISTS   200 lines  06b_T8_Rounds_Step_6.md
  EXISTS   259 lines  05b_T8_Rounds_Step_5.md
  EXISTS   272 lines  04b_T8_Rounds_Phase_10.md
  EXISTS   266 lines  04b_T8_Rounds_Phase_9.md
  EXISTS   590 lines  04b_T8_Rounds_Phase_8.md
  EXISTS   503 lines  04b_T8_Rounds_Phase_7.md
  EXISTS   401 lines  04b_T8_Rounds_Phase_6.md
  EXISTS   361 lines  04b_T8_Rounds_Phase_5.md
  EXISTS   160 lines  04b_T8_Rounds_Phase_4.md
  EXISTS   145 lines  04b_T8_Rounds_Phase_3.md
  EXISTS   136 lines  04b_T8_Rounds_Phase_2.md
  MISSING            03b_T8_Rounds_Step_3.md
  MISSING            02b_T8_Rounds_Step_2.md
  MISSING            01b_T8_Rounds_Step_1.md
  MISSING            00b_T8_Rounds_Step_0.md
```
The four MISSING names are in `Archive/ULM_Records/City_Development_Passes/Mirny_Subnet/Mirny/` (`00.1b`, `00b`, `01b`, `02b`, `03b`: five files), as `README.md` L49 and `DR-27` state.

### Item 1a — normalized scan of the required reading (hits as file:line:token only)
```
ITEM 1a — normalized scan (line-initial '>' and whitespace stripped; hits as file:line:token only, content withheld)
00_RUNBOOK.md                                    lines= 3161 hits= 11  distinct-lines=[9, 1332, 1333, 1958, 2073, 2074, 2218]  (joined-text 'ariun nuur' matches: 0)
01_Frame_Typology_and_Inheritance.md             lines=  589 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
02_Generators_Capability_and_Symbols.md          lines=  805 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
03_The_Phase_Spine.md                            lines= 1196 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
04_QA_Gates_and_Differentiation.md               lines=  927 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
05_The_Input_Contract.md                         lines=  822 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
06_Worked_Example_Provenance.md                  lines=  430 hits= 13  distinct-lines=[292, 294, 311, 312, 313, 314, 315, 319, 328, 329, 332]  (joined-text 'ariun nuur' matches: 0)
README.md                                        lines=  242 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
Disciplines/00b_General_Population_Discipline.md lines=  262 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
Disciplines/00d_Shadow_Proportion_Discipline.md  lines=  223 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
Disciplines/00f_Review_Panel.md                  lines=  835 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
Disciplines/Cultural_Synthesis_Techniques.md     lines= 1197 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
Disciplines/README.md                            lines=  125 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
Disciplines/Real-World_Basis_Extrapolation_Method.md lines=  470 hits=  0  distinct-lines=[]  (joined-text 'ariun nuur' matches: 0)
TOTAL hits: 24
```
The runbook hits by token and line, from `grep -n -o`: L9 Casey · L1332 Casey (three tokens on L1332, one on L1333) · L1958 Vostok · L2073 Kunlun, Vostok · L2074 Vostok (two) · L2218 Casey.

### Items 2, 7, 8, 10 — commands and results (excerpts)
- **Item 2:** `git status --short -- Universal_Location_Methodology` listed `M MASTER_Process_Tracker.md` and `M Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` only; `git diff --stat` over the runbook, `06`, `Disciplines/` and `Tools/` printed nothing.
- **Item 7:** `find <city> -type f | wc -l` gave 22 files and 2 folders for each of Casey, Kunlun and Vostok; the file-name lists are identical across the three; Casey totals 1,142 lines; `Bunger_Hills_City` holds 1 file.
- **Item 8:** `00_RUNBOOK.md` L66 (*The whole directory is closed until Step 7*), L2492, L2792 close `Test_Runs/` to a cold run; the observations file path is `Universal_Location_Methodology/Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`.
- **Item 10:** `grep -o *M-2[4-9][0-9]*` over `00_RUNBOOK.md`: `M-246` only; over `04`, both Pre-Trip recipes and `Datasheet_and_PreTrip_Tracker.md`: `M-246` only in the Pre-Trip recipe trial; 59 distinct M-numbers in the 240s and 290s are recorded in the observations file.
- **Casey memory bands:** `grep -c *CONTAMINATION BANNER*` returned 1 for each of `project_casey_bug_check_resolved.md`, `project_casey_recheck.md` and `project_pink_lucy_migration_resolved.md`, each at lines 10 to 15, immediately after the frontmatter.
- **Memory surface:** `grep -ril -E *casey|kunlun|vostok|ariun*` (filenames only) matched 97 of 343 files.
- **Per-city file `16`:** the Mirny pass lists name it twice: Phase 4 `:: 109-134,241-248,275`; Phase 7 `:: 1-139,241-248,275,445-465,2105-2173`.
- **Safeguard probe (for Step 9's correction):** `_safeguard_probe/README.md`: run 2026-10-11 ~12:05, nine tests, all passed.

## Post-write checks
- **Quotation audit:** run on the Step 10 files; result in the DOUBLE-CHECK block.
- **Handoff audit:** *INSTRUMENT VALID: NO* as at every check since Phase 5 (M-284); not re-pasted.
- **Founders script:** not re-run (repo-wide heritage section, MP-2); this step wrote no founders.
- **Position-Coverage Ledger:** not touched.

## DOUBLE-CHECK
Run after the three files were final; this record continues after the check (M-288).
```
DC-1 lines: {'10_Readiness_Check.md': 97, '10b_T8_Rounds_Step_10.md': 148, 'Symbol_Review_2026-10-13.md': 59, '.t8_required_10_Step10.txt': 3}
DC-2 PROOF blocks: {'A': 3, 'B': 3, 'C': 3}
DC-3 items: ['1', '1a', '1b', '1c', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'] OK
DC-4 R       [180, 181, 182, 183, 184, 185] OK
DC-4 Q       [145, 146, 147, 148, 149] OK
DC-4 PA      [96, 97, 98, 99] OK
DC-4 S10-RF  [1, 2, 3, 4, 5] OK
DC-5 T4 one line: 1
DC-6 double-quoted strings (r, b outside fences, symbol review): 0 0 0
DC-7 British spellings: none
DC-8 the word compact: 0
DC-9 sign words in readiness check: none
DC-10 does it declare completion?: True | 'complete' claims: []
DC-11 unresolved placeholders: 0 (the one counted was this block's own marker)
```
**Quotation audit** (`quotation_audit.py`, default mode; header and controls shown, the rest of its output lists earlier files' own-pass quotations by design): **0 lines reported for `10_Readiness_Check.md` and `10b_T8_Rounds_Step_10.md`**; the four lines it first reported for `Symbol_Review_2026-10-13.md` were this step's own phrases set in quote marks and were set in italics before this check.
```
pass audited : Mirny
corpus mode  : default (own pass excluded)
corpus files : 5179   chars: 51,695,684

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
```
**Verdict:** items 1–11 (fourteen checks) are all present and in order; R-180…R-185, Q-145…Q-149, PA-96…PA-99 and S10-RF-1…5 are consecutive; the T4 line is on one physical line; no double-quoted string, British spelling or the retired word *compact* in the three files; the readiness check does not declare the pass complete. Five of the fourteen checks fired: items 1, 1a, 7, 8 (cold runs only) and 10; see `10_Readiness_Check.md` §1 and §3.

## Snags
1. No reader was cut off by the safeguard flag or by a usage limit in this step's reading half; each finished in about five minutes (a contrast with Steps 5 to 9).
2. The file-system half was split across two days by the usage limit (12th evening) and the hours law; the state file's log holds the sequence.
3. Step 9's statement that the safeguard probe had not been run was wrong (see `10_Readiness_Check.md` §5, snag 5).
4. The `Symbol_Review_2026-10-13.md` and `DR-54` to `DR-56` work interleaved with this step; none of it changes an item's result.
