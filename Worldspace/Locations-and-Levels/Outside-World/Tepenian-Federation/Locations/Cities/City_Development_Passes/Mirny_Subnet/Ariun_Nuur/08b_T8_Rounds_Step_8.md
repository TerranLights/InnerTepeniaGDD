# Ariun Nuur — ULM Step 8 (the Review Panel, Gate 10) — T8 round record

**Unit:** Step 8, run as three sub-units by files: **R1** (the frame, the spine, Phases 2–4), **R2** (Phases 5–8, with the spine's §5
shape), **R3** (Phases 9–10 and the Step 5 reconciliation, with the spine's §5 shape); each sub-unit ran the whole panel over its files.
**Written:** `08_Review_Panel.md` (1,559 lines; PROPOSED, not declared complete). **Run mode:** WARM (`DR-6`). **Date:** 2026-11-20.
**Common inputs:** the runbook's Step 8 (L2978–3005); `Disciplines/00f_Review_Panel.md` with L3 and L86 cut (they name other places);
the Step 8 datasheet; the position-coverage ledger; **Step 7's errata as facts** (`07_QA_Gates.md` L1421–1707, runbook Step 8, `M-278`);
`DR-143`. **Lists and briefs (sha256[:16]):** R1 list bfa4d56bd6339962, brief 0464203de50f28ea (12 entries) · R2 list
6d11bed3c2e3a6cc, brief 19f741fd2176671f (12) · R3 list 858223c3b46bba45, brief c6d8689be8da4890 (11). **Merge brief:**
`.t8_merge_brief_08_Step8.md` (a4847e85fc690464; 12 orchestrator points). **No web call** by any agent.

## Round 1 — receipts
| Sub-unit | A | B | C | MANIFEST |
|---|---|---|---|---|
| R1 | 428 lines | 429 | 382 | 12 of 12, each |
| R2 | 253 | 500 | 293 | 12 of 12, each |
| R3 | 319 | 462 | 415 | 11 of 11, each |

Each reader's casting, counts by disposition, Passer-Through result, late Lover verdict and standout are in its receipt line in
`RUN_PROGRESS_Ariun_Nuur.md` and in its own file (`.t8_Step8R{n}_reader{A,B,C}.md`).

## Round 2 — R1, `Tools/triple_read_verify.py`, raw output whole (run 1)

```
required files: 12
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2978-3005] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00f_Review_Panel.md  [range 1-2,4-85,87-834] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_8.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.2_Position_Coverage_Ledger.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md  [range 1421-1707] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00_Frame.md  [range 1-282,301-343,412-431] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md  [range 57-424] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_02_Composition_and_Arrival.md  [range 1-29,97-424,512-533] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_03_Surface_and_Texture.md  [range 1-30,106-411,519-547] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_04_Ordinary_Life.md  [range 1-26,164-474,595-622] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step8_findings_index.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**R1 exact-field check** (`exact_fields.py`; raw output whole):

```
.t8_Step8R1_readerA.md: 24 fields compared exactly, 0 differ
.t8_Step8R1_readerB.md: 24 fields compared exactly, 0 differ
.t8_Step8R1_readerC.md: 24 fields compared exactly, 0 differ
```

## Round 2 — R2, `Tools/triple_read_verify.py`, raw output whole (run 1)

```
required files: 12
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2978-3005] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00f_Review_Panel.md  [range 1-2,4-85,87-834] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_8.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.2_Position_Coverage_Ledger.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md  [range 1421-1707] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md  [range 233-272] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_05_Relation_and_Geometry.md  [range 1-29,255-624] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_06_Meaning.md  [range 1-38,132-608] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_07_Order.md  [range 1-87,256-1020,1117-1156] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_08_Making.md  [range 1-25,126-384] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step8_findings_index.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**R2 exact-field check** (`exact_fields.py`; raw output whole):

```
.t8_Step8R2_readerA.md: 24 fields compared exactly, 0 differ
.t8_Step8R2_readerB.md: 24 fields compared exactly, 0 differ
.t8_Step8R2_readerC.md: 24 fields compared exactly, 0 differ
```

## Round 2 — R3, `Tools/triple_read_verify.py`, raw output whole (run 1)

```
required files: 11
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2978-3005] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00f_Review_Panel.md  [range 1-2,4-85,87-834] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/Datasheets/Step_8.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/00.2_Position_Coverage_Ledger.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/07_QA_Gates.md  [range 1421-1707] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 2058-2065] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/02_Spine.md  [range 233-272] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_09_Populations.md  [range 1-28,193-520] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/04_Phase_10_Catalog.md  [range 1-47,236-465,579-1107,1197-1933] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/05_Reconciliation.md  [range 1-914,1023-1491] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/.t8_Step8_findings_index.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

**R3 exact-field check** (`exact_fields.py`; raw output whole):

```
.t8_Step8R3_readerA.md: 22 fields compared exactly, 0 differ
.t8_Step8R3_readerB.md: 22 fields compared exactly, 0 differ
.t8_Step8R3_readerC.md: 22 fields compared exactly, 0 differ
```

## Round 3 — cross-check verdicts (the verdict lines of each reply)

- **R1 reader A:**
  - VERDICT B: CONSISTENT — B read the same material, its dispositions are mostly supported, and its one `unmet` (113) is arguable rather than unsupported.
  - VERDICT C: CONSISTENT — C read the same material and caught three erratum extensions I missed, but its one `unmet` (216) is not supported by its ground, as C itself half-concedes at 240.
- **R1 reader B:**
  - VERDICT A: CONSISTENT — A read the same twelve entries and applied the same errata; where we differ it is judgment, and one weak point is a Weakling verdict that charges the subnet rather than the place.
  - VERDICT C: CONSISTENT — C read the same twelve entries, applied the errata more thoroughly than I did, and differs mainly on one `unmet` whose ground does not show the place knowingly holding what is refused (C flags this itself at item 240).
- **R1 reader C:**
  - VERDICT A: CONSISTENT — A read the same twelve entries at the same spans with matching PROOF fields, ran the full panel on the corrected statements, and its dispositions follow from its lines; it has one casting I would not make (a human Child) and a self-reported breach of the tool rule.
  - VERDICT B: CONSISTENT — B read the same material with matching PROOF fields and its dispositions follow from its lines, except one `rejected` (109, the Elder's lake motive) that should be `noted`, because the files leave the founding motive open rather than contradicting it.
- **R2 reader A:**
  - VERDICT B: CONSISTENT — B read the same twelve entries at the same spans, runs the same panel structure on the same corrected statements, and its one `unmet` rests on the same ruled line as mine (`DR-143` item 1); its only slips are minor.
  - VERDICT C: CONSISTENT — C read the same material plus two disclosed off-list reads that §0 item 4 allows, reaches the same standout, Passer-Through result and `unmet` ground as I do, and adds one sound inconsistency I missed (P8 L261); its slips are minor and disclosed.
- **R2 reader B:**
  - VERDICT A: CONSISTENT — A read the same twelve entries, ran the same errata as facts, and reached the same core results I did (*visibly* against *invisibly*, the holder's two-tense paradox, the cold correcting the pupil and not the lesson, the honor `unmet` on `DR-143` item 1, Passer-Through PASS, SC-1 unchanged), with only minor overreach in its Ruler casting and its late Lover verdict.
  - VERDICT C: CONSISTENT — C read the same material and converges on the same core, adds one real catch I missed (P8 L261), and its slips are procedural (a disclosed `tail | od` command outside §0 item 3) or interpretive (an unconditional Masochist "guilty"; its Crone verdict sits against its own finding 217).
- **R2 reader C:**
  - VERDICT A: CONSISTENT — Reader A read the same admitted spans, ran the panel on the corrected errata, and reached the same unmet, the same PASS and the same standout as I did; it also caught two real defects my run missed.
  - VERDICT B: CONSISTENT — Reader B read the same admitted spans, and its dispositions follow its own lines; it caught the same two defects plus a station-builder wording slip; one accepted finding is worded more strongly than its lines support.
- **R3 reader A:**
  - VERDICT B: CONSISTENT — B read the same eleven entries at the same spans (its reading log and PROOF fields match mine field for field), applied the same errata, and reaches PASS and SC-1 unchanged. Its one `unmet` (item 112) rests on a ruled line (`DR-143` item 1), so it is a fair developer question rather than an unsupported call.
  - VERDICT C: CONSISTENT — C read the same material at the same spans (PROOF fields match mine), applied the errata, and converges with me on the Mentor's finding, the declined copy off the plateau, PASS, `unmet` 0 and SC-1. It has one disposition slip, a waiting topic refereed (item 202), noted below.
- **R3 reader B:**
  - VERDICT A: CONSISTENT — A read the same material, applied the errata, cast by role, reached the same standout and Passer-Through result, and converges with me on the Mentor's air-lesson finding; I found no rule slip and no unsupported disposition.
  - VERDICT C: CONSISTENT — C read the same material and its main findings match mine (the store colder than the city's own cold, the air lesson, PASS, SC-1); two calls go further than its lines carry (item 203's acceptance and its Denying "Innocent" One wording).
- **R3 reader C:**
  - VERDICT A: CONSISTENT — A read the same eleven entries at the same spans and ran its panel on the corrected statements; its dispositions are supported, and its main finding is the same as mine (the human's night is a lesson the cold does not check).
  - VERDICT B: CONSISTENT — B read the same material and reached the same two main findings as mine (the human's night; the made-colder store that cannot stop); its one `unmet`, its four-corner check and its count of a faculty as a position are flagged below, not contradicted.

**Eighteen verdict lines, 18 CONSISTENT.**

## Checks on `08_Review_Panel.md` (`checks.py` against each sub-unit's list; raw output whole)

**Against R1's list:**

```
quoted strings checked: 14 not found: 6
  MISS: once a night keeper
  MISS: Nobody had finished teaching me.
  MISS: no way down
  MISS: no way down
  MISS: once a night keeper
  MISS: gives nothing
08_Review_Panel.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [27]}
tower-name count: 0
```

**Against R2's list:**

```
quoted strings checked: 14 not found: 6
  MISS: once a night keeper
  MISS: Nobody had finished teaching me.
  MISS: no way down
  MISS: no way down
  MISS: once a night keeper
  MISS: gives nothing
08_Review_Panel.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [27]}
tower-name count: 0
```

**Against R3's list:**

```
quoted strings checked: 14 not found: 6
  MISS: once a night keeper
  MISS: Nobody had finished teaching me.
  MISS: no way down
  MISS: no way down
  MISS: once a night keeper
  MISS: gives nothing
08_Review_Panel.md British-form hits: []
other-location name scan (names: line numbers): {'Mirny': [27]}
tower-name count: 0
```

**Triage (orchestrator).** Four quotations missed against all three lists; each is a reader's own words quoted from that reader's file
(*"Nobody had finished teaching me."* R1 A; *"gives nothing"* R2 A; *"no way down"* R1 A, R1 B, R3 C; *"once a night keeper"* R2 A's
Round 3 reply quoting its own casting). None is a source misquote. **British forms 0; tower name 0; other-location scan:** L27, the
city's own subnet relation.

**The T5 marker check** (`Tools/phase_discipline_check.py`, raw output of its T5 section):

```
=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===
  EARLY (Phase 6) verdict: alive, yes; lovable, not yet shown. [...the Phase 6 line, L506, as printed...]
  LATE (Step 8) verdict   : alive, yes; lovable, not yet shown. The glimpses the readers cite are written beside this verdict as candidates, never as love shown (see below).
  (5 other line(s) in 08_Review_Panel.md merely mention the Lover faculty; they are NOT the marker.)

  Both dedicated markers present. COMPARE BY HAND: if the early verdict changed what any
  phase between 6 and 8 wrote, T5 is FALSIFIED per its own stated
  condition and must be withdrawn, not quietly kept.
```
*(raw output, excerpted (1 span omitted: the early verdict's text after its first clause, which is Phase 6 L506 verbatim))*. **Compared
by hand:** the merge writer found Phases 7 and 8 record the Lover faculty as not reached (Phase 7 L957, Phase 8 L319), so whether the
early verdict changed what they wrote cannot be told from the files; T5 is **neither confirmed nor falsified** on this pass.

## Procedural events (the recording law)
1. **The panel was split by files** (three sub-units) because the finished pass is more than one reader holds. Every sub-unit got the
   spine's §5 shape so each panel knew what the whole place claims. Cost: castings and objections came back three times and had to be
   settled into one casting per position; benefit: nine independent panels, convergences across opposed corners counted as evidence.
2. **`unmet` drifted toward the ruled honor line.** Five readers grounded an `unmet` on `DR-143` L2063 item 1; in Round 3 two withdrew
   (R1 C to `declined`; R3 B under Rule 1). The merge wrote **`unmet` 0** with the counts under the developer's other readings (2, or 3).
3. **Uncastable positions were voiced anyway** (the Child as a conditional human child or a robot built here) by five readers; Round 3
   conceded the result rule (`00f` L757–764). Filed as a question (Q-340).
4. **Pass labels that pre-empt the panel:** Phase 7 L894–895, Phase 8 L289 and Phase 9 L402, L417 label anticipated refusals `unmet`;
   under the self-knowledge test they are `declined` (requests).
5. **Command slips, disclosed:** `tail -c` on the reader's own output file (R1 A); `tail -c | od -c` on listed files (R2 C); `sed`,
   `cat -A`, `cut`, `head` on the reader's own output (R3 B); pipes on `sed` output (R1 A, R1 B, R2 B, R3 A). **The merge writer**
   appended its casting section with a shell heredoc (`cat >>`) rather than Edit, and ran read-only `sed`, `grep`, `wc` and `tail` on the
   findings index and its own output. No PROOF field rests on any of these; Round 2 was UNANIMOUS at the first run in every sub-unit.
6. **Self-corrected positional lines:** R2 C (`DR-143`'s middle line, L2060 to L2061) and R3 B (the runbook span's last line, blank),
   both before hand-back.
7. **No repair was needed** in any sub-unit.

## Questions filed
Q-340 to Q-360 filed as `DEC-1057` to `DEC-1077` (21), each PROVISIONAL on its recommended answer. **Next: `DEC-1078`.**

## Tokens
Readers (last figures, incl. Round 3) 3,912,286 (R1 1,266,030 · R2 1,210,044 · R3 1,436,212); merge writer 424,373; **total
4,336,659**; web calls 0. Rows in `TOKEN_LOG_Ariun_Nuur.md`.
