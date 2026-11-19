# Ariun Nuur — ULM Phase 2 (composition and arrival) — T8 round record

**Unit:** Phase 2, Step 4's first phase. **Written:** `04_Phase_02_Composition_and_Arrival.md` (533 lines; PROPOSED, not declared
complete). **Run mode:** WARM (`DR-6`). **Date:** 2026-11-19; brief frozen and readers dispatched 07:38, Round 1 back by 07:57, Round 3 by
08:00, merge returned 08:13, record 08:15.
**List:** `.t8_required_04_Phase2.txt` (15 entries): the Pre-Trip's Phase 2 rows (the no-national-stereotypes law; the treaty; the census;
the Founding Register's rules and this city's row; the composition file's solar-UTC rule) and the sequencing ruling it names (runbook
§C.9b–§C.9e), with every line naming another location's worked example cut from the runbook spans, the law, the Register and the
composition file; the spine's Phase 2; the runbook's Step 4; the spec; the earlier five outputs; the Phase 2 datasheet; `DR-143`. The
"diaspora/affinity files" address resolves to nothing admissible (the spine's own line). **Brief:** `.t8_brief_04_Phase2.md` (211 lines;
built from the phase template; sha256[:16] 10f65f72a82deaab). Reader outputs archived here as `.t8_Phase2_reader{A,B,C}.md`; Round 3
replies as `.t8_Phase2_round3_reader{A,B,C}.md`. Three Opus readers; one fresh Opus merge writer (`M-246`).

## Round 1 — receipts (as returned)

| Reader | Lines | Axis | Findings | Asymmetry rows | Handed forward | Positions | RF · SH · REQ · Q | Handoff places | Manifest |
|---|--:|---|--:|--:|--:|--:|---|--:|---|
| A | 475 | assigned specialists, outgrown by arrivals | 37 | 13 | 8 | 6 | 8 · 1 · 7 · 7 | 10 | 15 of 15 |
| B | 459 | assigned specialist wave, arrival-grown | 44 | 17 | 7 | 2 | 9 · 2 · 5 · 7 | 10 | 15 of 15 |
| C | 419 | specialist posting, never rotated | 41 | 11 | 8 | 5 | 7 · 2 · 6 · 8 | 15 | 15 of 15 |

## Round 2 — `Tools/triple_read_verify.py` (last commit `8777bb5f` 2026-11-03; clean), first run, raw output whole

```
required files: 15
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2090-2129,2131-2140,2145-2217,2219-2314,2316-2319,2662-2694,2696-2698,2700-2729,2731-2759] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/03_The_Phase_Spine.md  [range 401-471] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md  [range 1-17,20,22-43,46-47,50,52-94,96-137,139-169,171-174] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-41,432-440,520] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md  [range 1-12,63] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Upper_Earth_Immigration_Composition.md  [range 23-25,28-29,31-35] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Ariun_Nuur.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/03_Research.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Phase_2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — cross-check verdicts (the first two verdict lines of each reply)

| Reader | On | Verdict |
|---|---|---|
| A | B | CONSISTENT |
| A | C | CONSISTENT |
| B | A | CONSISTENT |
| B | C | CONSISTENT |
| C | A | CONSISTENT |
| C | B | CONSISTENT |

**All six CONSISTENT; no repair.** Settled in Round 3 and written in the corrected form: ten Significant rows below 4.5% (B's eight); a
*fled to it* reading resting on the treaty's preamble dropped (findings rest on the draft's articles only, `DR-142` item 3); a
real-world place name in a composition row label not reproduced; no demonyms. The (c) points became Q-69 to Q-84, filed as `DEC-750` to
`DEC-765`.

## Procedural events (the recording law)

1. **Reader B** ran `tail -c 300` on its own output; **reader C** used a `printf` wrapper around `sed -n` on listed files; **reader A**
   missed two EXEMPT lines (a demonym and a place name on positional lines) and reproduced the place name in a table. All raised in Round 3
   or self-reported; the merge carries none of them.
2. **The merge writer** removed a language name containing a demonym from a paraphrase of the national-language ruling, and wrote the
   supporting base as *Korean, among the other tongues the ruling names*; the ruling's own list stands at its source. It created no other
   file.
3. **The orchestrator,** while building the list, printed parts of the Founding Register's multi-city lines and saw other cities' names
   (logged at 07:38; nothing carried). The phase template gained three lines after this phase (articles only; no demonyms; a blank last
   line).

## Quotation checks, before this record existed

**Pre-check (T8 line 13), per quotation, normalized.** First run, raw:

```
quoted strings checked: 41 not found: 2
  MISS: evidenced at scale
  MISS: a robot's fabrication and her home city are, as a rule, the same place
04_Phase_02_Composition_and_Arrival.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [3]}
tower-name count: 0
```

**Triage:** *a robot's fabrication and her home city are, as a rule, the same place* is at runbook L2679–2680 inside the admitted span; the
miss is the blockquote's wrap marker (`the` / `> same place`), not a defect. *evidenced at scale* was a reader's phrase in quotation marks,
**rewritten as italics** (one line). After the fix, raw:

```
quoted strings checked: 40 not found: 1
  MISS: a robot's fabrication and her home city are, as a rule, the same place
04_Phase_02_Composition_and_Arrival.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [3]}
tower-name count: 0
```

**`Tools/quotation_audit.py`** (last commit `5a63e074` 2026-11-02; clean), `--phase 2 --own-pass`. Whole output saved beside this record
as `.t8_Phase2_quotation_audit.txt`; result block, raw:

```
=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 18
NOT FOUND in corpus: 3
  of those, in TABLE CELLS : 1
  of those, in PROSE       : 2

  [04_Phase_02_Composition_and_Arrival.md:37]           at phases 2 and 4. - p. opened here at its rules and this city's row; the
  [04_Phase_02_Composition_and_Arrival.md:69]  [CELL]  and take up residence in tepenia, on the assembly's schedule and conveyance (td l46, art. ii.2.1); no individual designation, accu
  [04_Phase_02_Composition_and_Arrival.md:197]           them, and none is compelled (td l48-49); afterward any human may elect at any time (td l50) treaty draft ; by ruling she could not

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage:** all three are connective prose captured between adjacent quotations (L37, L69, L197). **Confirmed defects: 0 (CELL 0, PROSE 0).**

## Phase-close instruments (raw output whole)

**`Tools/handoff_audit.py`** (T1):

```
pass audited : Ariun_Nuur
phase files  : 1

=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===
  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): 2
  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : none
  SELF-TEST (fixed positive and negative strings)       : passed
  INSTRUMENT VALID: YES - the detector separates a formal block from no block on the built-in controls

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | FORMAL   |    0 | n/a - nothing addressed to it

TOTAL outbound handoff rows: 6
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 0

=== outbound rows, per target, for hand reconciliation ===
  -> Phase 3:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 3** | the founding wave's specialization, its criterion and its losing side (R
  -> Phase 4:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 4** | whose ordinary day: the arrival layers (founding-wave descendants, later
  -> Phase 5:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 5** | who the visitor is: Hwy 37 as the only written route of arrival, departu
  -> Phase 8:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 8** | composition established: the origin stocks as admissible, composition-gr
  -> Phase 9:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 9** | which populations exist: 25 rows, both bodies at their own counts, the h
  -> Phase 10:
       [04_Phase_02_Composition_and_Arrival.md]  | **Phase 10** | the district's honor of the city's own scientists (FIND-P2-37); the fou
```

**`Tools/phase_discipline_check.py`** (T3, T4, T5), run before the ledger was updated:

```
pass audited : Ariun_Nuur

=== T3 - POSITION-COVERAGE LEDGER ===
  phases in header: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Child              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Lover (position)   filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Parent             filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Ruler              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Elder              filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Mentor             filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Passer-Through     filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  The Neighbor           filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10
  ⭐ The Lover FACULTY    filled=0  blank=9   blank at: P2, P3, P4, P5, P6, P7, P8, P9, P10

  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not
  fill a blank by writing new phase content toward it - that is the
  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).

=== T4 - PER-PHASE SHED MARKER ===
  [04_Phase_02_Composition_and_Arrival.md]  T4 present: the origin stocks' own cultures, the per-row decimals and headcounts below the tier, the l

  1/1 phase files carry a T4 marker.
  >> If EVERY phase's answer was literally 'nothing', T4 is falsified
     per its own stated condition (the question would be decorative).
     This tool cannot see the marker's CONTENT well enough to judge
     that - read the 1 lines above by hand.

=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY marker absent in (no Phase 6 file found)
  LATE marker absent (08_Review_Panel.md missing or has no 'T5 - LATE LOVER FACULTY:' line yet)

  T5 not fully applied this pass (one or both markers absent).
```

**Ledger:** `00.2_Position_Coverage_Ledger.md` updated from the phase file's own table (P2: Lover (position) and Parent national only;
Mentor; Passer-Through as a null). Child and Elder contested (Q-73), left blank.

## American English sweep and the one-location check

From the same script, raw: `04_Phase_02_Composition_and_Arrival.md British-form hits: []`; `other-location name scan (names: line
numbers): {'Mirny': [3]}`; `tower-name count: 0`. The one hit is the pass folder's path. **No other location named.**

## Tokens (from the task notifications; full rows in `Universal_Location_Methodology/TOKEN_LOG_Ariun_Nuur.md`)

| Agent | Round 1 | Round 3 (delta) | Last figure |
|---|--:|--:|--:|
| reader A | 440,590 | 62,256 | 502,846 |
| reader B | 453,478 | 58,251 | 511,729 |
| reader C | 434,595 | 76,824 | 511,419 |
| merge writer | — | — | 235,482 |
| **Unit total (sum of last figures)** | | | **1,761,476** |

Web calls: readers 0; `Tools/web_quota_count.py`: WebSearch: 215 | WebFetch: 69 | TOTAL: 284 (unchanged)
**The record grows after this check** (T8 line 8): no DOUBLE-CHECK script was run on this record.
