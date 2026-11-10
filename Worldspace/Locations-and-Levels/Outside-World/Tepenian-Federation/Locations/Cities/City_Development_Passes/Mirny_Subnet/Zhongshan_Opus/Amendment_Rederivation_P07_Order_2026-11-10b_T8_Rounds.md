# Zhongshan: T8 round record for P07_Order (the baseline, the oasis rock, the partnership and imports), 2026-11-10

**What this is.** The record of the three-reader rounds behind `Amendment_Rederivation_P07_Order_2026-11-10.md` (the piece; 839 lines, `sha256` `96e6212988e74d47`). It states what each tool returned and where each file is; it does not restate the piece. **Everything here is PROPOSED;** no pass file was edited. The run's log is `Amendment_Log_2026-11-10.md`.

**Isolation.** Fresh readers and a fresh merge writer, each with a clean brief and its own private staging folder; nothing from any other location's run is in any list, brief or record of this piece (log Z-01).

**Items re-derived:** `C7` (two derivations of the baseline), `C8` (the division of the oasis rock), `U1` (what the city supplies, and the research partnership), `U3` (imports and the ports); first-check verdicts in the note's section J.

## Round 0: the list and the briefs

The three readers' lists are identical (`cmp`). The list (19 entries), as dispatched:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C7.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C8.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_U1.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_U3.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_07_Order.md :: 145-190,250-284,416-428,470-480,612-628,634-640,912-920
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_04_Ordinary_Life.md :: 300-320
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md :: 1917-1938
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md :: 50,72
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/11_Caloric_Rebuild_and_Livestock_Tier.md :: 292
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/07_QA_Gates.md :: 48-96
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/02_Spine.md :: 210-218,276-296
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md :: 502
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md :: 579-596,602-606
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 1382-1392,1416-1426,1711-1712
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md :: 84
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_05_Relation_and_Geometry.md :: 84-94,318-336
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Ports.md :: 125-131,198-204,224-231
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md :: 488-495
```

Brief template `scratchpad/zs/tools/zs_t8_brief.md` (generator `zs_pieces.py`); the three briefs differ only in the title's reader letter, the reader letter, the staging folder, the output path and the number range (A 1 to 99, B 101 to 199, C 201 to 299). Brief `sha256`: A `16118ba879b65d9d`, B `562cdc4f23326f26`, C `876c33f91a0778ad`. Before dispatch each brief's cited lines were checked against its list (`zs_check_brief.py`; log Z-13 or later).

## Round 1: three independent readers

- Reader A: `.t8_xc_P07_Order_readerA.md` beside the pass (719 lines, `sha256` `a308c7f5d20c3189`).
- Reader B: `.t8_xc_P07_Order_readerB.md` beside the pass (746 lines, `sha256` `1b3570e38956f26b`).
- Reader C: `.t8_xc_P07_Order_readerC.md` beside the pass (839 lines, `sha256` `17e478298cfd5735`).

## Round 2: the mechanical check

Tool: `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/triple_read_verify.py` (last committed 2026-11-03; no uncommitted edits).

**round2_run1.txt** (raw output, whole; also beside the pass as `.t8_xc_P07_Order_round2_run1.txt`):

```
required files: 19
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/Amendment_Notes_2026-11-10_Cross_Check.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C7.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_C8.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_U1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/.xc_20261110_item_U3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_07_Order.md  [range 145-190,250-284,416-428,470-480,612-628,634-640,912-920] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_04_Ordinary_Life.md  [range 300-320] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/16_Per_City_Three_Tier_Run.md  [range 1917-1938] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/09_Per_City_Baseline_Run.md  [range 50,72] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/11_Caloric_Rebuild_and_Livestock_Tier.md  [range 292] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/07_QA_Gates.md  [range 48-96] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/02_Spine.md  [range 210-218,276-296] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 502] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md  [range 579-596,602-606] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1382-1392,1416-1426,1711-1712] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 84] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Zhongshan_Opus/04_Phase_05_Relation_and_Geometry.md  [range 84-94,318-336] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Ports.md  [range 125-131,198-204,224-231] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Relationship_Database.md  [range 488-495] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
exit 0
```

## Round 3: the cross-check (each reader continued by SendMessage, given the other two outputs)

The verdict lines, as `grep` returns them (each reply beside the pass as `.t8_xc_P07_Order_round3_reader<X>.md`):

```
reader A L39: **Verdict on reader B: CONSISTENT**
reader A L121: **Verdict on reader C: CONSISTENT**
reader B L49: **Verdict on reader A: CONSISTENT**, because every quotation, positional line and figure of A's that falls inside our shared spans
reader B L133: **Verdict on reader C: CONSISTENT**, because C's quotations, positional lines and figures match the shared spans and its arithmetic
reader C L39: **Verdict on reader A: CONSISTENT**
reader C L116: **Verdict on reader B: CONSISTENT**
```

## The merge

One merge writer (fresh; not a reader), brief `scratchpad/zs/pieces/P07_Order/M/brief.md` (template `zs_merge_brief.md`; `sha256` `2158939f420f7738`), merge rule `M-246` as `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.2 states it. Its return, as given: `Amendment_Rederivation_P07_Order_2026-11-10.md — 839 lines — The merged P07_Order piece is PROPOSED. It holds 47 findings, 18 choices and 13 questions. Contradictions are settled on content, by the reading that claims least: "knowing nothing of 16 §18" fails on Phase 4 L303; where the research stake is worked is not ruled; L274 holds as written; L278 is unsupported either way; there is no L918 link. It writes the narrower "recorded as another location's mandated role" in place of "led from", and proposes no change to the note, whose row U1 already carries the Z-14 correction.`

## Merge checks (run on the piece before this record existed)

**1 · Normalized quotation pre-check** (`scratchpad/zs/tools/zs_postmerge.py`; corpus: the list's sources whole, the pass's numbered files and amendment notes, the reader outputs and Round 3 replies, the item outputs). Raw output, whole:

```
corpus files: 45; quoted strings (12+ chars, paired within a block): 175; not found: 11; blocks with an odd quote count (hand-check): 0
  NOT FOUND (block at L297): **The city requires `120–172 km²` and carries about 36% (`14.45 km²`) of the `~40 km²` oasis rock, by Census I share, as arithmetic (D-6).** **So the overwhelming majority of it, 88 to 92%, stands on engineered apron — and the dense, shared-wall, nothing-is-soundproof condition belongs to the ROCK CORE specifically, not to the whole city**
  NOT FOUND (block at L300): Nobody designed it. It follows from about `8–12%` of the ground never needing to be rebuilt.
  NOT FOUND (block at L306): **The oasis itself.** `DRQ-11` — who, in the world, allocated `~40 km²` between three cities, *or did nobody* — **is open**. The amount this city's figures carry is set by D-6 as arithmetic: 14.45 km² (36.136%).
  NOT FOUND (block at L308): ⛔ **NO IN-WORLD ALLOCATION IS RECORDED.** *The share is set by ruling as arithmetic (D-6: 14.45 km²); who, if anyone, divided the rock in the world is open, and this pass does not invent it. Naming what the contested good IS does not decide whose it is.*
  NOT FOUND (block at L413): The developer ruled three-quarters of that sector mandated: **`137,200 workers` — `15.1%` of everyone who works here — are nationally committed to producing qualified people for somewhere else.** *Beside the mandate, the city is a partner in a joint, ongoing agricultural research project, recorded as another location's mandated role (`DR-72` L1386-1387; `DR-75` L1421; `DR-105` item 4). No share of this city's workforce, no place of work and no reason for its place are ruled.*
  NOT FOUND (block at L418): and a research stake in a project shared among several parties sits on the same side
  NOT FOUND (block at L422): **This adds the fourth and it is the structural one: the outsourceable half is the half that leaves** — certainly for the training mandate; for the research partnership it depends on where the city's share of the work is done, which is not ruled.
  NOT FOUND (block at L425): **`15.1%` of the workforce is nationally committed to producing engineers and researchers who leave.** That makes transmission not one civic function among many but **the main thing the city is for**, and for that share the apprenticeship question and the economy question are the same question. The city also holds a partner's place in a joint agricultural research project; how it is staffed and booked is not ruled.
  NOT FOUND (block at L429): **Beyond the cluster: a research partnership.** This city is a partner in a joint, ongoing agricultural research project recorded as another location's mandated role (`DR-72` L1386-1387; `DR-75` L1421; `DR-105` item 4). None of the oasis's other cities is a party. The city's research work goes into the project; nothing else about the flow is ruled.
  NOT FOUND (block at L523): ⚠ **`City_Relationship_Database.md` L495** calls this city a coastal port receiving an Upper Earth partner's freighter shipments (raw materials staged via two of that partner's ports, as part of the subnet's coastal supply line). **Reconciled:** `Ports.md`'s receiving-node table (L125-131) does not list this city or its cluster among that partner's direct nodes (L129). Since the developer ruling of 2026-09-16 it lists the city's three-city cluster, as one unit, as a receiving node, not the principal one, of the neutral transshipment route (L130): inbound raw materials only, with indirect access to two Upper Earth powers' supply and no direct bilateral relationship with either. §5.6c gives the cluster its one shared constructed port, long haul and seasonal (L202). **So this city receives through a shared harbor that is a secondary national node for inbound raw materials. It is not a direct gateway and not the principal node, and `16` §18 rules it 
  NOT FOUND (block at L523): ** (now also the spec's L180, corrected under D-6). Whether its freight arrives only through the neutral hubs, also by direct sailing, or onward along the coastal supply line is open.
```

**2 · Quotation audit** (`python3 Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools/quotation_audit.py "<pass folder>" --files <piece> --own-pass`, from the repo root; tool last committed 2026-11-02; no uncommitted edits). Raw output, excerpted (14 miss lines omitted, kept whole beside the pass as `.t8_xc_P07_Order_quotation_audit.txt`):

```
pass audited : Zhongshan_Opus
corpus mode  : default (own pass excluded)
corpus files : 6898   chars: 109,002,757
files audited: Amendment_Rederivation_P07_Order_2026-11-10.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 50
NOT FOUND in corpus: 14
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 14


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.

exit 0
```

**2b · Triage of the audit's misses** (same script; the audit reads no dot-file). Raw output, whole:

```
audit NOT FOUND fragments: 14; (a) found in the corpus: 2; (b) the piece's own unquoted prose: 6; (c) for hand triage: 6
  (c) L66: did not hold on the pass's own day either. 16 18's figure as first written
  (c) L172: (l296). the ground for a divide rather than a deficit
  (c) L300: nobody designed it. it follows from about 8-12% of the ground never needing to be rebuilt
  (c) L310: (if question 67 is answered with option b or c, this line, l616's
  (c) L418: and a research stake in a project shared among several parties sits on the same side
  (c) L449: (l333-334), and 16 18 independently rules the city
```

Hand triage of class (c): 6 fragments in class (c), each read at its line: L66, L172, L310 and L449 are the piece's prose between two adjacent quotations; L300 and L418 are proposed replacement text. Pre-check: the 11 strings not found (blocks at L297, L300, L306, L308, L413, L418, L422, L425, L429 and two at L523) are the piece's proposed replacement wording, each written after the pass address it would replace (for example: 07_QA_Gates.md L93: then the proposed sentence). No misquotation found.

**3 · American English sweep** (British forms; only "judgement" is kept). Raw output: none (0 hits).

**4 · Other locations' names and status words** (`grep` for 56 names and aliases, whole words; and for complete, completed, ready). Raw output: names none; status words none.

*Record written 2026-11-10 08:00 by script from the files named above; the checks ran on the piece, not on this record.*
