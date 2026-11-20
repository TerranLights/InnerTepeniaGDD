# Ariun Nuur — ULM Step 7 — QA: the gates

**Step 7 · 2026-11-20 · WARM pass (`DR-6`; graphify not used) · PROPOSED; not declared complete.**

- **Sub-units and readers.** The gates ran over the whole pass as three T8 sub-units, split by files, each with three independent
  readers (A, B, C):
  - **Q1:** the Step −1 contract, the frame, the Step 1 audit, the spine, the Step 3 research, Phases 2 and 3.
  - **Q2:** Phases 4 to 8.
  - **Q3:** Phase 4 again (for Gate 3), Phases 9 and 10, Step 5's reconciliation, Step 6's differentiation.
- **Round 2** (the mechanical check of every reader's PROOF fields): **UNANIMOUS** in all three sub-units.
- **Round 3** (each reader's cross-check of the other two): **six CONSISTENT** in each sub-unit.
- **Merge rule** (`M-246`; `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` L653–692): a contradiction takes the most conservative current
  (post-Round-3) view, with the split named; no contradiction means UNION, each single-reader find written and credited; a vote count is
  not the rule; a reader's withdrawal is evidence for the narrower reading; every Round 3 point marked (c) is a developer question with a
  recommended answer, PROVISIONAL. **A gate's verdict for the pass is the most conservative of its sub-unit verdicts**, and each
  sub-unit's evidence is kept under it.
- **Errata are PROPOSED and never applied.** The pass's files are not edited by this step. **The errata enter the Review Panel's brief as
  facts** (runbook L2983).
- Real-world comparables are written by role (`DEC-723`). No other location is named except as a relation from the city's own lines; the
  national tower by role only.
- Numbering in this file: errata `ERR-1` on; requests from `REQ-205`; questions from `Q-288`.

---

## 1 · Verdict table

The pass's verdict is the most conservative of its sub-unit verdicts. "Not assigned" is not a verdict.

| Gate | What it asks | **Pass** | Q1 (contract to Phase 3) | Q2 (Phases 4–8) | Q3 (Phases 9–10, Steps 5–6) |
|---|---|---|---|---|---|
| 0 | Does the completion claim match the file? | **FAIL** | FAIL | FLAG | FAIL |
| 1 | Coverage | **FLAG** | FLAG | FLAG | FLAG |
| 2 | General population | **FAIL** | FAIL | FAIL | FLAG |
| 3 | Internal contradiction (Ordinary Life last) | **FAIL** | not assigned | FAIL | FAIL |
| 4 | The swap test | **FAIL** | PASS | PASS | FAIL |
| 5 | Cross-location consistency (relations) | **FAIL** | FLAG | FAIL | FLAG |
| 6 | Duplicate institutions, within the location; substitutes 3 and 4 | **FAIL** | FLAG | FLAG | FAIL |
| 6 | Against siblings | **NOT RUN** (terminal) | NOT RUN | NOT RUN | NOT RUN |
| 7 | Research accounting | **FLAG** | not assigned | not assigned | FLAG |
| 8 | The standout | **PASS** (SC-1) | not assigned | not assigned | PASS |
| 9 | Asymmetry, second run | **FAIL** | FAIL | FLAG | FLAG |
| 10 | The Review Panel | **NOT RUN** (Step 8) | NOT RUN | NOT RUN | NOT RUN |
| 11 | Plausibility | **FAIL** | not assigned | not assigned | FAIL |
| C | The canon check, federated | **FAIL** | FAIL | FAIL | FAIL |
| F | Frame integrity | **FAIL** | FAIL | FAIL | FAIL |
| I | Inheritance classification | **FLAG** | PASS | PASS | FLAG |
| P | Parent reconciliation | **N/A** (no written children) | N/A | N/A | N/A |
| G | Generator honesty | **FLAG** | FLAG | not assigned | not assigned |
| — | The station-builder scan | **FAIL** | FAIL | FAIL | FAIL |
| — | The generator-vocabulary sweep | **FAIL** (wording) | FAIL | FAIL | FLAG |

**Totals:** 95 errata (`ERR-1` to `ERR-95`); 25 requests (`REQ-205` to `REQ-229`); 52 developer questions (`Q-288` to `Q-339`). The
orchestrator's two instruments (the findings index and the mechanical sweep) failed their known-case checks in all three sub-units; those
are recorded as instrument defects, not as the pass's (REQ-205, REQ-206).

---

## 2 · The gates, one section each

Short names: *contract* (Step −1), *frame* (Step 0), *audit* (Step 1), *spine* (Step 2), *research* (Step 3), *P2* to *P10* (Phases 2 to
10), *Step 5* (the reconciliation), *Step 6* (the differentiation); *DS12* is the Step 1–2 datasheet, *DS2* the Phase 2 datasheet, *DS7*
the Step 7 datasheet, *DS-P7* the Phase 7 datasheet. Line numbers are file lines. Reader items are cited by their own numbers (Q1: A from
1, B from 101, C from 201; the same ranges in Q2 and Q3, prefixed with the sub-unit where needed).

### Gate 0 — Does the completion claim match the file?

**Question** (`04` L102–108): reconcile each completion or status claim against the file, and each open-questions list against what has
been resolved elsewhere, in both directions; read scope words and forward references too. Check the target, never the claim.

#### Q1 — FAIL (A FLAG · B FAIL · C FLAG; A and C conceded the FAIL in Round 3)

**Checked (all three readers):**
- Status lines: contract L13, frame L13, audit L12, spine L9, research L10, P2 L9, P3 L7 all read "PROPOSED; not declared complete". No
  file overclaims.
- Self-counts recounted by hand, all hold: contract L35 "Count: 6"; contract L197 "COVERAGE: Ariun_Nuur.md 1-222, no gaps, no overlaps"
  (CR-9 to CR-71, contiguous); audit L95 (14 + 7 = 21); the spine's L11 series against its tables; spine L214 "agree 9 · conflict 2 ·
  silent 1"; spine L293 (3 + 1 + 4 = 8 assigned, 1 undetermined); spine L597 (16 + 3 + 1 = 20); spine L754 "(73 lines)" (C); research
  L58 "22 targets"; research L205 "7 facts not used"; the web counts 73 + 95 + 88 = 256; P2 L103's tier sums (28.36 / 69.48 / 2.15 /
  99.99); P2 L368 "4 positions covered"; P3 L362 "1 position covered"; P3 L543 "17 questions (Q-85 to Q-101)"; frame §14's span counts
  (C); the sweep's total, 768 (B, C).
- Forward references to Step 7 (audit §1 item 3; P2 L349; P3 L343; frame RF-24 L255): each is discharged under Gate 9.

**Raw evidence of the failure (B101, confirmed at source by A and C in Round 3):**
- P3 L11: "**No finding rests on a treaty-draft article.**" Against FIND-P3-34 (L198): "the only written non-resident channel, treaty
  observers, is not sited here (Phase 2 RF-86)"; RF-86 rests on TD L92 and L98, a treaty-draft source.
- P2 L11: "Every finding that rests on a treaty article is tagged `[treaty draft]` and listed under *Generators used*". Against FIND-P2-19
  (L201: "and no return (TD L77; brief §4 item 5)") and FIND-P2-22 (L208: "humans who came could not go back (TD L77)"), neither tagged
  nor in the list at L336.

**Cross-file mismatches the list could not settle (requests, not pass failures):**
- *The run-modes lines* (A, single-reader find): audit L171: "…the run-modes file (L53, L99, L109, L118, L138: other cities closed for the
  whole pass)…"; frame L218: "RM L53, L99, L105 and L138 keep other cities "CLOSED until Step 6", and RM L118 places Gate 6 at Step 7".
  One list is wrong, or L105 was not edited (REQ-207).
- *`DEC-716`'s source* (A, and C as C223): spine L10: "Step 1's questions (`DEC-708` to `DEC-716`) are unanswered"; the audit holds eight
  question rows, Q-28 to Q-35 (L232–239); research L609: "the same substance as Step 1's Q-35 (`DEC-715`)". The ninth number has no
  visible row (REQ-208).
- *The merge rule's span* (C, single-reader find): spine L8 cites `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` "L670–692", spine L769 "L653–692";
  likewise audit L11 against L356, research L9 against L644, P3 L6 against L547, and P2 L8 "L670–692". The contract and frame receipts
  (L365, L431) give L653–692. *(As read for this merge, L653 opens the unanimous gate and L670 opens its merge amendment; the rule this
  step applies spans L653–692.)* (REQ-209.)
- *The web calls* (A, single-reader find): research L8 and L503 record 256 calls by the readers against the session tool's 284; the 28 are
  stated, not explained (REQ-210).

**Developer question, not a FAIL** (B126; settled as (c) in Round 3 by A and C): contract L249 (Q-3), L251 (Q-5) and frame L208 ("all
unanswered") state positions from before `DR-143`. Those lines were true when written, and the audit's §5 (L154–173) records the
reconciliation (Q-288).

**Fix (PROPOSED):** ERR-1, ERR-2.

#### Q2 — FLAG (A PASS · B PASS · C FLAG; A and B conceded the FLAG in Round 3)

**Checked (all three):** status lines P4 L3, P5 L6, P6 L9, P7 L11 and L1156, P8 L7, each "PROPOSED; not declared complete"; nothing
claims completion. Count lines recounted by hand, all hold: P4 L418 and L618 (16 questions, Q-102 to Q-117); P5 L543 (3 positions); P6
L537 and L605 (14 questions); P7 L959 and L1141 (19 questions); the P7 receipt L1147–1151 (45 findings; 16 reserved; 15 requests; 5
shadows; 6 handed-forward rows; asymmetry rows 144–170 = 27, B; sweep arithmetic 17 + 52 + 16 + 1 = 86, 28 + 58 = 86, 41 + 58 = 99); P7
L25 and L83–84 (4 + 3 + 5 + 1 = 13 addresses); P8 L321; the RF, SH, REQ and Q series run on without gap or overlap from Phase 4 to Phase
8 (A); P4 L14's cold-file spans 7 + 105 + 62 + 1 + 2 = 177 (B). Forward references to Step 7 (P4 L375, L399; P5 L524; P6 L518; P7 L939;
P8 L302) are run under Gates 3 and 9; cross-phase citations found at their targets (A).

**The FLAG (C201; A noted the same mismatch):** P4 L23, raw: "DS4's own coverage line (L11) counts *7 of 7* addresses named, two of them
only through a shared sheet not on this list:** on this list five are opened at source, two (`09`, `11`) are reached only through DS4's
rows, and one is n/a by the spine's own line" *(as C pasted it)*. 5 + 2 + 1 = 8 against DS4's 7; the sentence counts files where DS4
counts addresses and does not say so. A reconciles it by reading DS4's seven as excluding the n/a address; C by reading the robot-biology
folder as one address read through two files (Q-302).

**A count the list could not check (B, single-reader find):** P7 L34 says `16` was opened at "11 spans, 73 lines"; the ranges the same
bullet lists (L1–12, L21–33, L72–85, L122–141, L241–248, L282, L2349–2358) total 7 spans and 12 + 13 + 14 + 20 + 8 + 1 + 10 = 78 lines
(REQ-216).

#### Q3 — FAIL (A FAIL · B FAIL · C FAIL)

**Checked (all three):** status lines Phase 9 L9, Phase 10 L16, Step 5 L15 and L1036, Step 6 L10, each PROPOSED, not declared complete.
Recounted by hand and holding: Phase 9 L368's dual tags (17 + 21 + 7 = 45; deep 22 + surface 23 = 45); Phase 9 L235, L225 (3,907.8 m),
L296, L320, L448; Phase 10 L319 (50 recovered), L338 (62 calls = 24 + 27 + 11), L872–874 (78 = 16 + 19 + 15 + 17 + 8 + 3), L943, L1006,
L1223; the B1 tally L1565–1574 (taken 24; extends 26; WAITS 41 = CST 15 + DCI 26); Step 5's counts (RC 45 + 11 + 16 = 72, out of frame 8;
DF 35; PA 27; AM-P9 12; translation 36; candidates 8; RL 78; carried rows 26); FIND-S5-8's "four of them" (C); Step 5 L1033 (no finding
written at stage B); Step 6 L399 (19 splits, 8 requests, 13 questions).

**The failures:**
- **Step 6 L318 counts a generator conflict that is not one** (A, B; C conceded): "**Result:** nine of ten axes are the product of a
  conflict between generators; §3's is not" *(as B pasted it)*, while the same table's §10 row (L316) reads "G2 against itself at two
  depths". One generator at two depths is not a conflict between generators: the count is eight of ten. (Also Gate 6, substitute 4.)
- **Rows 31 and 84 classed opposite ways** (A, B, C): row 31 (Phase 10 L1600, taken column "extends CAT-33, the null") is counted taken;
  row 84 (L1653, taken column "extends FIND-P10-12 (a null: no marker stands at any computed point of the pole; U3-F203–F205)") is listed at
  L1924 among the rows with nothing taken, while L1696–1699 writes its extends note and L1929 counts it. Which way to class both is a
  developer question (A and B: taken; C: move the null to the not-taken column) (Q-316).
- **Phase 10 L42–44's status claim is not true of the file** (B, single-reader find; A and C agreed): "the spec (whole; excluded lines
  read, nothing resting on them)", against L950–951 and L986 citing spec L135 and stage-B items resting on spec L155, L157 and L171 past its
  clause (RC-74 to RC-78). Step 5's REQ-167 dockets the citations, not the status claim. (See Gate F.)
- **RF-182's credit cell** (B, C): Phase 9 L463 reads "C (FIND-P9-231)"; no FIND-P9-231 exists (the series ends at FIND-P9-46), and the
  finding's own credit at L352 is "C231". A label slip.
- *The Step 7 datasheet L21* (A): written under Gate C (ERR-87).

**FLAG items:** Phase 10 L1025 marks three positions covered, the Parent among them, on a reading Step 5 holds open (RC-61; Q-235
recommends leaving it blank), against Phase 9's rule that a position covered only on a contested reading is not marked (L434) (B; Q-317).
Step 5's REQ-159 asked for a mechanical sweep at Step 7 with a wider term list than the one run, and over Step 6 too: met in part (B; see
Gate 1). Items routed out of Q3's files: RC-52, RC-53, RC-54 (Phases 2, 3, 5), REQ-195 (Phase 8's internal tension, FIND-P8-7 against
FIND-P8-10; Q2's Gate 3 item 10 touches FIND-P8-7) and Step 6 REQ-203 (Phase 3) (A, B; REQ-223).

**Fix (PROPOSED):** ERR-74 to ERR-77; ERR-87 under Gate C.

**Pass verdict: FAIL** (Q1 FAIL · Q2 FLAG · Q3 FAIL).

### Gate 1 — Coverage

**Question** (`04` L110–125): is each applicable phase question answered, not gestured at? A scan proves nothing until it is shown it
could find a hit; each term is pass, fail, covered in substance but absent in term, or absent and unexplained.

#### Q1 — FLAG (A PASS · B PASS · C FLAG)

**Checked (all three, by reading; the brief allowed no search command):** contract §7, all eight generators, dispositions, reserved
findings; frame DL-1 to DL-22, Phase 0 processes A–D, the must-open receipt; audit's 21 rows; spine §8e's four answers (L346–396); research's
22 targets, deficits, convergence, the Unrecognized Instrument; P2 sections A–E, band variance, axis, Borrowed Form "not triggered" with its
reason (L271); P3 sections A–F, the four sensory sub-fields, band variance, failure modes, axis. Every absence met says why: sound (P3 L148),
robot smell (P3 L166, RF-94), built form (P3 L136, REQ-69), born-here (P2 L208), power (spine L330–333); holes are recorded as holes
("location registries", frame L159, REQ-13). **No absent-and-unexplained item.**

**The instruments, verified before any zero was trusted:**
- *The generator-vocabulary sweep* finds what it was built to find (A: P2 L234, P3 L134, contract L35, spine L211, research L222; B: P3
  L188; C: spine L532's "G7-tagged", so a hyphen does not break it). **It cannot find:** the quadrant words STRENGTH and DEFICIT,
  "tolerance" alone, the plural "standing costs", or the pass's own code labels (D-n, SH-n, RF-n, S3-n, UI-n) (A 37, B 132, C). A zero
  from it on those is not evidence (REQ-206).
- *The findings index* **misses eleven findings in Q1's files** (all three readers): FIND-P2-60 to FIND-P2-67 (P2 L317–324, bulleted
  lines), FIND-P2-68 (P2 L330), FIND-P3-46 (P3 L228) and FIND-P3-74 (P3 L326), the last three with a title that opens in italics. Outside
  Q1, C found (and B confirmed) no FIND-P5-32, FIND-P5-34 or FIND-P6-11, and nothing from Phase 10 or Step 5. A reader who trusted it would
  conclude that P2 has no band-variance findings and no axis (REQ-205).

  Raw evidence (A, index lines quoted from the index): L61: "04_Phase_02_Composition_and_Arrival.md:309 | FIND-P2-59 | No one turned away,
  in any line"; L62: "04_Phase_03_Surface_and_Texture.md:110 | FIND-P3-1 | The ground."; P2 L330: "**FIND-P2-68 · *Assigned specialist
  wave, arrival-grown.***"; P3 L326: "**FIND-P3-74 · *Snow without weather.***"

**The FLAG (C, single-reader find, kept):** LAW 0-P (developer ruling 2026-11-19) requires every row of the location's candidate list to be
researched, not only the official picks. Step 3's reading list (research L633, L636–637) gives the official picks (`Inspirational-Influences.md`
L92–95) and the two inspiration-place research files; the spine's G7 is the three official picks (spine L67); no line in Q1's files names
the candidate list. Recorded as a FLAG, not a FAIL, because the ruling is dated the same day as Step 3 (Round 3: A "C is right to FLAG it";
B and C (c)) (Q-289).

#### Q2 — FLAG (A FLAG · B PASS · C PASS; C conceded the FLAG in Round 3, B put its item to the developer)

**Coverage, by reading (all three):** P4 answers the headline test, the four elements, different days by body and layer, physical scale,
what the rhythm fails to provide, band variance and the axis (L164–383); P5 answers 5a–5e, both directions and the axis, 5b a null by
ruling (L339); P6 answers naming, belief as checked facts, death, the failure state and the axis, observance waiting by ruling (L472); P7
answers 7a–7d, band variance and the axis, *Other 10%* a recorded null (L395–404); P8 answers every category as conditions, native and
transplanted, the general population, tools and the axis. Faith, holidays, rites and music wait (`DR-140` items 2–3); mortuary is RESERVED
(RF-14); government and justice wait for the DCI (`DR-137` item 11).

**One absent and unexplained item (A, single-reader find):** refuse and waste disposal. P8 L189 writes only that whatever is set out and
left is kept by the cold and taken by the snow; no admitted line in Q2's files writes disposal or says why it is missing (Q-303; the
emissions point is under Gate 5).

**The instruments, tested against known cases (all three):**
- *The findings index* misses **eight** findings in Q2's files, every one a bold title carrying italics, among them all five
  differentiation axes: FIND-P4-66 (P4 L381), FIND-P5-32 (P5 L398), FIND-P5-34 (P5 L402), FIND-P5-55 (P5 L507), FIND-P6-11 (P6 L284),
  FIND-P6-32 (P6 L486), FIND-P7-45 (P7 L874), FIND-P8-45 (P8 L287). (A counted six; B and C eight; C showed the two A missed, Round 3.) Rows
  that are right: P4-1 at L168, P7-23 at L583, P8-37 at L255 (C) (REQ-205).
- *The sweep* finds a single-line hit (P8 L215, listed as `215:standing cost`) and matches a plural on a phrase's *last* word (P8 L293
  carries only "standing costs" and is listed). **It misses** a phrase split across a line wrap: P7 L576–577 reads "The place's grudging" /
  "tolerances stay tolerances", with no 576 or 577 in the sweep's Phase 7 line (A, B, C); and a plural on a phrase's *first* word: P5 L367
  reads "Every remedy the city's deficits address", with no 367 in the Phase 5 line (B, single-reader find). Phases 6 and 7 are hard-wrapped,
  so their counts are a floor (REQ-206).

#### Q3 — FLAG (A FLAG · B PASS · C PASS)

**Coverage, by reading (all three): answered.** Phase 9 answers its sections (lens decision L206–227; populations L231–268; per-population
life L272–330; relations L334–360; dual tags L364–368; swap L370–402; axis L406–417); Phase 10 answers recover, research (with stage B's pick
incorporation L1227–1933), the lens, Planet and Element, the catalog, border and band; Step 5 answers its required parts; Step 6 writes all
ten rows, the peer-free test per cell and substitutes 3 and 4. Each null says why (Phase 9 L248, L438–446; Phase 10 L729–732, L858: "No
dated local event is in the city's lines. This is a result"). B's limit: the phase spine's own question lists for Phases 9 and 10 are not on
Q3's list, so coverage is checked against each file's declared structure (REQ-225).

**The FLAG (A; B and C record the same limit under the sweep): the sweep's term list is narrower than Step 5's REQ-159 asked, and it does
not reach Step 6.** REQ-159 (Step 5 L853) asked for "quadrant names, standing cost, grudging tolerance, deficit, strength, shape names,
address labels including in the parent, unspeakable, characteristic failure, generator numbers, `D-n`" *(as A pasted it)*; the sweep's list
(sweep L3) lacks bare *deficit*, *strength*, *Balanced* and the other shape names, the address labels, *unspeakable*, *characteristic
failure* and `D-n`. Known hits it cannot find: Phase 9 L344 ("for most of the city the thin air is unspeakable"; listed only for *standing
cost*), Phase 9 L346 (*a deficit*; absent from the sweep), Phase 4 L238 ("*Characteristic failure* (spine D-3)"; absent). It covers every
pass file **through Step 5 only**; Step 6 L58 carries *Balanced* and the address labels, legitimate method-column vocabulary (Q-275), but
unswept (REQ-206).

**No gate in this file passed on a zero from either instrument.** Coverage was judged by reading in all three sub-units; the findings index
was used for navigation only, and its misses were found by reading the files; every "not found" from the sweep is stated with this limit.

**Pass verdict: FLAG** (Q1 FLAG · Q2 FLAG · Q3 FLAG).

### Gate 2 — General population

**Question** (`04` L127–132; quick reference L61–66): per `00b`, every finding checked for whom it describes, inherited ones included; the
Band-1 inversion where it applies.

#### Q1 — FAIL (A FAIL · B FLAG · C PASS; B and C conceded the FAIL in Round 3)

**Checked:** the city is Band 4; frame L167: "at Band 4, `00b` operates normally and its Band-1 inversion does not apply". The research
population is scoped as a subset everywhere it appears (P2 L246, L321; P3 L224: "**The headline institution's profile is not written as the
city's.**"; P3 L250). The altitude cost is scoped to the human 35.50% (spine L119; research L223; P3 L180, L184). Dress is national and
functional, styles left to the CST (P3 L178); first impressions are written for an arrival who stays (P3 L198); per-population culture is
not assumed (P2 L240). C cleared research FIND-25's "A research place whose people have no term" as a general-population point (the no-term
condition is national); its no-departure wording is a Gate 9 matter.

**Raw evidence of the failure (A, errata 1–4; confirmed by B and C):** the need for darkness at the place of rest rests on human melatonin
and sleep research (FACT-40 to FACT-43) and is written for every body. The robot majority's rest night is a charge night "not bound to the
dark" (spine L140, L406).
- research L229: "→ For about 123 days of midnight sun, rest needs **dark** at the place of rest as much as heat → the manufactured day
  (spine standing cost 8) is two costs: heat and light in winter, heat and darkness in summer."
- research L263 (§4, the D-3 row): rest needs a rule and darkness at the place of rest *(as A reports it; written unquoted)*.
- research L461: "| RF-55 | Rest needs darkness in the midnight-sun months as well as heat (FIND-17) |…"
- P2 L252: "- **Rest is located:** rest and charge happen only in heated, powered space; for about 123 days of midnight sun rest needs dark as
  well as heat (spine §8f; research FIND-17)."
- P3 L186, already corrected for its own phase: "In the midnight-sun months rest also needs darkness at the place of rest **for the human
  body**, on the human circadian evidence … For robots, whose shared rest night is a charge night not bound to the dark (spine L406), no
  need for darkness is written."

**And the scope of spine L392 (B141; adopted by A and C in Round 3):** "Staying as a *visitor* in a place built, in the picks' form, for
coming and going (G7 adjusted) (B); the newcomer's first costly years in a research institution (G7 adjusted, PROVISIONAL) (A)." Two
research-institution readings sit untagged in the city's general answer list.

**A FLAG item kept beside the FAIL (B142):** Step 3's targets fall mostly on the human 35.50% (food S3-1; thin air S3-7; sleep and light
S3-4; water as drink); no target addresses the robot majority's own needs, and the robot body appears only through machine analogs (FIND-15,
FIND-29). The skew is partly structural (`DEC-697`), and the research says so for FIND-15 (Q-290).

**Fix (PROPOSED):** ERR-3 to ERR-7.

#### Q2 — FAIL (A PASS · B FAIL · C FAIL; A conceded the FAIL in Round 3)

**Cleared (all three):** dress written from function for both bodies (P8 L201–209); first impressions scoped by route of arrival (P5
FIND-P5-33, L400); sound and music as conditions only (P8 L175–179); per-population practice scoped on top of the general answer (P8
FIND-P8-37 and FIND-P8-38, L255–263; P6 FIND-P6-8's archive layer for the research population only); "No one here belongs to a majority by
origin" rests on the largest row at 15.97% (C); "for most of the city a meal is a charge and a shipment" (P8 L169) rests on robots 64.50%
(A). Band 4: the Band-1 inversion does not apply. A's note: P6 FIND-P6-7 (L235–236) supports a general claim with a research-layer source
(P4 FIND-P4-34); it survives on the survival layer (P4 FIND-P4-13), a citation-scope note only.

**Raw evidence of the failures (findings stated of everyone that the files themselves narrow):**
- P6 L242 (FIND-P6-8), B and C: "**The survival layer** reaches all 441,378: every arrival, of either body and any of the 25 origin rows, is
  taught …, pays the heat at her stop along with everyone else's, and is then the one who teaches it" *(as C pasted it)*. Against P6 L263
  (FIND-P6-10): "**the never-asked:** the arrival who never teaches, is never asked, or is never the earlier arrival", and P6 L436–439
  (FIND-P6-27); and "all 441,378: every arrival" equates the whole population with arrivals, while P4 L298 (FIND-P4-45) keeps robots built
  here as a layer.
- P7 L815–816 (FIND-P7-42), B: "Every resident is first the taught and then the teacher, a debtor to the earlier arrival and a creditor of
  the next." Against P7 L725–726 (FIND-P7-36): "She is kept in body and never becomes the teacher … she stays a permanent newcomer."
- P4 L309 (FIND-P4-49), C and B: "Whatever the body or layer, the day ends at the same clock hours in a heated place (FIND-P4-6). **That is
  the only written point where every resident's day is the same.**" Against P4 L270 (FIND-P4-42): "The keepers of the life support
  (FIND-P4-8) rest outside the shared night … Their free time falls when the city is asleep." (Also a Gate 3 contradiction.)
- P4 L360 (FIND-P4-64 item 3), C, in a list headed (L357) "Common to every ordinary day, whatever the body, layer or work": "the night is the
  shared stop, robots charging and humans sleeping at once". The same exception.
- P5 L377 (FIND-P5-29), C: "→ **Every body arrives by Hwy 37, at least for its last stretch.**" Meant of arrivals; read flat, it asserts
  every body is an arrival (P4 L298). B read it as about arrivals only and put it to the developer (Round 3, (c)); C's FAIL was not
  withdrawn (Q-304).

**Fix (PROPOSED):** ERR-38 to ERR-42.

#### Q3 — FLAG (A PASS · B PASS · C FLAG; A and B conceded the FLAG in Round 3)

**Cleared (all three):** Band 4, the Band-1 inversion not applying (Phase 9 FIND-P9-10, L260); Phase 9 writes each body's costs and
structure with its count and keeps layers as functions (L218: "Functional layers ... are not populations with a culture of their own", as B
quotes it), and research-population claims are scoped to it (FIND-P9-29, FIND-P9-36); dress as function only (CAT-28); the sensory items are
physics, two conditional (REQ-B2-1); music and visitors are not written; Step 5 stage B reports the culture sheets' claims as claims and
adopts none (L1031–1032); CAT-B1-3's city-wide reading was narrowed at Step 5 (RC-59; REQ-172).

**The FLAG (C, kept; A and B conceded):** the catalog's people slot leans to the headline function. Of Phase 10's 21 role archetypes
(CAT-36 to CAT-50, CAT-76 to CAT-78, CAT-B1-3, CAT-B1-4, CAT-B2-8), 10 are clearly the research layer (CAT-38, 42, 44, 47, 49, 50, 76, 77,
B1-4, B2-8), 3 mixed (CAT-41, 78, B1-3) and 8 general (CAT-36, 37, 39, 40, 43, 45, 46, 48); every stage-B item comes from
research-institution picks; Phase 4 L170 holds that 39.4% of the counted workforce does baseline work, not research, and FIND-P4-60 (L343)
that, for the rest, no listed line writes a purpose of their own. No item claims a research role is general, so no finding is wrong (Q-318).

**Notes kept beside it:** CAT-1 (Phase 10 L689–690), "the honor is paid daily, not once [B]", reads a daily practice of the whole district
into a name; A proposes narrowing it to "the district is where the city's own scientists work", the honor staying a name (FIND-P10-1); B
agreed (Q-319). CAT-25 (L760–761), "The ice tools in every household", is Phase 8's claim (FIND-P8-40) cataloged; whether it holds under
open enclosure (`DEC-703`) is a Gate 11 note (B).

**Pass verdict: FAIL** (Q1 FAIL · Q2 FAIL · Q3 FLAG).

### Gate 3 — Internal contradiction (read Ordinary Life last)

**Question** (`04`, Part I): read Ordinary Life (Phase 4) last and check every other phase against it; list each contradiction with both
lines; Step 5's reconciliation rows, where they already settle one, are cited, not re-derived.

#### Q1 — not assigned

Gate 3 belongs to Q2 (Phases 5–8) and Q3 (Phases 9–10, Steps 5–6). The one contradiction Q1 met in passing (P3 L317 against P3 L270) is
recorded under Gate F, where it is also a breach of a reserved decision.

#### Q2 — FAIL (A FAIL · B FAIL · C FAIL): Phases 5–8 against Phase 4, read last

**Order of reading.** B and C read Phase 4 last of the five phases. A read Phase 4's sections A–C (L164–313) in list order before Phases
5–8, then held L314–474 until last, and disclosed it. No Step 5 reconciliation row is on Q2's list, so none is cited.

**Contradictions (the union; each with both lines; each reader's single finds credited):**

| # | Later line | Phase 4 (or its own) line | Found by |
|---|---|---|---|
| 1 | **Coolant on the melt account.** P8 L155 (FIND-P8-3): "***No admitted line states plain coolant's composition** … so whether coolant is made from water … are not written … **Conditionally,** if its formulation is water-based, it draws on the same melt-and-heat account" *(as A pasted it)* | P4 L206 (FIND-P4-14): "drinking, washing and a robot's coolant (RP L275) draw on the same account as warmth". Phase 4 states as fact what Phase 8 shows has no source. | A |
| 2 | **Siligel by Hwy 37, stated flatly.** P8 L151 (FIND-P8-1): "Whatever either body takes in has come by Hwy 37, or is water made here from ice"; P8 L169 (FIND-P8-10): "both chains run through Hwy 37; neither is grown here" | P4 L214 (FIND-P4-18): "whether this city mines, processes or only receives it is reserved (frame RF-21, PV-6)"; Phase 8's own FIND-P8-2 (L153) keeps the condition | A |
| 3 | **What anyone meets in a day.** P7 L303–304 (FIND-P7-2): "most of what anyone meets in a day is baseline work (Phase 4 FIND-P4-2)" | P4 L170 (FIND-P4-2): "it is not a majority, and it is not a count of the people met in a day". Phase 7 cites the finding that refused this reading. | A |
| 4 | **Teaching's size.** P7 L656 (FIND-P7-28): "***The city's largest unwritten work is teaching, and it is in no sector***" | P4 L200 (FIND-P4-13): "some part of the settled residents' day is always given to teaching the newest"; arrivals are unsized (P4 L278) | A |
| 5 | **Whose deaths stay.** P6 L338–339 (FIND-P6-17): "So the city's deaths stay here, and every death here is a resident's (Phase 4 FIND-P4-61)." | P4 L345 says only that its deaths stay here; P5 L390 (FIND-P5-30) writes passers-through as possible, because the road runs through the city | A (C put it to the developer, (c); B agreed, minor) |
| 6 | **Departure.** P6 L198–199 (FIND-P6-4): "it cannot be escaped by leaving, because a human who came cannot return and no departure is written (brief §4 item 5; RF-30)"; P7 L385–386 (FIND-P7-9): "no departure from the city is written (RF-30), so its expertise does not leave as emigrants" | P4 L246 (FIND-P4-32): "no departure is written (RF-30); every route in is one-way as far as the files write it"; P4 L341 (FIND-P4-59). Phase 4 writes an absence; Phase 6 an impossibility. The same shape as Q1's Gate 9 failure. | B |
| 7 | **The clock.** P7 L485 (FIND-P7-16): "The site's own record has always run on a world clock (research UI-6, reserved RF-70) [A]." | P4 L184 (FIND-P4-5) holds the same fact as the real station's record and reserves it ("the real station's record was kept at four fixed hours (research FIND-39; UI-6, reserved as RF-70 and RF-106)"), though its opening, "The one clock already on the site is a world clock", already leans the same way | B |
| 8 | **The shaft.** P6 L430–432 (FIND-P6-26): "The only work that can be stopped is the work that is the city's purpose … the body's wins and the purpose yields: the city's reason to exist is its first sacrifice." | P4 L303 (FIND-P4-46): "except at the shaft"; P4 L190 (FIND-P4-8): "the shaft is kept filled and watched whether or not anyone works in it"; P7 L446 row (i): "cannot be paused without loss". Phase 6's own FIND-P6-29 and FIND-P6-30 keep the exception. | B |
| 9 | **The shared night.** P7 L549–550 (FIND-P7-20): "The national pattern is broken here every night, by necessity, by whoever keeps the heat." | P4 L309 (FIND-P4-49), "the only written point where every resident's day is the same", against Phase 4's own L190 and L270. **Here Phase 4 is the line in error**; P6 L410–411 ("everyone stops in the same hours") repeats it. | B and C |
| 10 | **Fresh food grown here.** P8 L163 (FIND-P8-7): "what is fresh is the exception that came by the road or was grown on the electric supply (FIND-P8-8)" | P4 L347 (FIND-P4-62): "Frozen keeps, fresh does not, and every fresh thing comes by the road (FIND-P4-15)"; P4 L208 (a conditional); and Phase 8 itself, L151 and L165: "No growing practice is written (RF-37)." | C |
| 11 | **Electricity as received.** P7 L389–392 (FIND-P7-9, *What it receives*): "electricity from a source no record places (`DEC-705`)" | Phase 4 leans the same way at L363 (FIND-P4-64 item 6, *Supply from elsewhere*); **the correct statement is Phase 5's**, L436 (FIND-P5-43): "**Whether the city is on the grid: not written. What powered it before the grid came fully online: not written. Nothing is assumed.**", and L304. Scored under Gate 5 and Gate C. | A and C |
| 12 | **One electric supply.** P4 L188 (FIND-P4-7): "Charge for 284,693 robots is drawn while 156,685 humans sleep in heat, all on one electric supply" | P5 L436 records the national file's line implying grid-dependent heat as flagged at source and a draft (L16); P6 L409 writes the same supply without the adjective. Scored under Gate C. | A |
| 13 | **Every resident teaches.** P6 L242; P7 L815–816 | P4 L200 ("some part of the settled residents' day"). Scored under Gate 2. | B |

**Checked and cleared (the union):** the light regime and dates (P4 L184: polar night April 23 to August 20, 120 days; midnight sun
October 21 to February 20, 123 days; 243 = 120 + 123, hand-counted; P6 L476–477 agrees); the coldest month and the robot's worst season
(P4 L232, L289 against P6 L476, P7 L586, P8 L201); the light season, November to January, −31.3 to −41.4 °C (P4 L264; P6 L478; P8 L209,
L217); burial 6.8–7 cm a year (22.5 ÷ 330 = 0.0682 m) and drift about 2 m a year; water 0.121–0.125 kWh a liter, about three quarters the
melting (1.9 × 54.8 + 333.6 = 437.7 kJ = 0.1216 kWh; 2.1 × 54.8 + 333.6 = 448.7 kJ = 0.1246 kWh; 333.6 ÷ 437.7 = 76%); the industry
figures in every phase; teacher and induction (P4 L200, L301; P5 L409; P6 L208–210; P7 L616–623); the keepers (P4 L190; P7 L447, L449,
L490; P8 L259); the two registers (P4 L303; P7 L445–447); care by window (P4 L224, L339; P5 L432; P7 L700–707); rescue (P4 L333; P6
L351–353; P7 L499–501); one-way routes against the physical road (P4 L246; P5 L406; P7 L559; A, by the both-are-true test: different
objects); the founders' 7.90% (P4 L295 against P7 L605 and P8 L243: a scope statement against flat stock shares); the Neighbor (P4 L415;
P5 L540); arrivals (P5 FIND-P5-31 against P4 FIND-P4-45: different populations, B); the model's shares (P4 FIND-P4-1 against P7 FIND-P7-4);
born-here and built-here (P4 FIND-P4-45; P7 FIND-P7-21, FIND-P7-28); the edgeless robot, about 3,900 m of air, flight mode in a warm room,
opposite outdoor rules, leisure located, the road's closure conditional (C).

**Fix (PROPOSED):** ERR-40 (the shared night), ERR-43 to ERR-51; items 11 and 12 under Gates 5 and C (ERR-52 to ERR-54); item 13 under
Gate 2 (ERR-38, ERR-39).

#### Q3 — FAIL (A FAIL · B FAIL · C FAIL): Phases 9–10 and Steps 5–6 against Phase 4, read last

All three readers read Phase 4 last. This gate is the close point for Phase 4's contradiction role (`04` L138–141): Phases 5–8 are closed
under Q2, Phases 9–10 and Steps 5–6 here.

**Contradictions (the union; each with both lines):**

| # | Line in Phases 9–10 or Steps 5–6 (or Phase 4 itself) | Against | Found by |
|---|---|---|---|
| 1 | **The keepers of the night.** Phase 10 CAT-39 (L792–794): "The keepers of the night: of heat, water, charge and the shaft ... In a night months long they are those who stay with the instruments across it; real facilities give the night as one double shift" *(as B pasted it)* | Phase 4 FIND-P4-6 (L186): "**The night is a time, not a darkness**"; FIND-P4-8 (L190) and FIND-P4-9 (L192): the keepers keep heat, melting, charge and the shaft, while the instruments "run on a calendar with dark periods". CAT-39 takes the polar night for the clock-hour night and the instruments' staff for the life support's keepers. | B (A and C agreed) |
| 2 | **The polar night's light.** Phase 4 FIND-P4-39 (L264): the light season is "the least cold months and the only ones in which the place shows anything to the eye but the city" | Phase 10 CAT-B1-5 (L1331–1336: a nautical twilight around midday every day of the polar night) and CAT-B1-6 (L1337–1342: the moon up all day for about a week); and Phase 4's own dates (L184): outside the polar night the sun rises and sets from about 21 August to 20 October and from about 21 February to 22 April. Step 5 RC-58 reconciled the same conflict for CAT-58 and Phase 3, not for L264. | A (B and C agreed) |
| 3 | **"The street never goes quiet."** Step 5 stage B, RL-43 (L1157) and its mechanism item 6 (L1247–1248) cite "the street never goes quiet (Phase 3 FIND-P3-18; RC-54)" | Step 5's own RC-54 (L346–348) narrowed that Phase 3 line to "never stops"; in the pre-narrowing words it contradicts Phase 4 FIND-P4-6 (L186: "the city goes quiet at an hour on a clock"). Under RC-54 both hold. | A (B and C agreed) |
| 4 | **Charging somewhere cold.** Phase 10 CAT-26 (L763–764), "Charging points somewhere cold", recovered from "Phase 4 L397; Phase 7 L578" (r19, L286) | Phase 4 FIND-P4-17 (L212): "every day is planned so that no charge is taken cold"; FIND-P4-6 (L186): "charge is taken warm". Phase 4 L397 says nothing of a cold place; A's logged off-list read of Phase 7 L576–578 found "charging somewhere cold" among the place's tolerances, permitted and charged. Both-are-true: the ordinary day avoids it; the place permits it at a price; FIND-P4-30 (L242) writes the emergency cold charge and its scar. The citation and the word *points* are wrong. **A developer question** because it rests on one reader's off-list read (C (c); Q-322). | A |
| 5 | **Raising: every year, or every decade.** Phase 10 FIND-P10-3 (L894): "So whatever stands must be lifted every year and travels with the ice"; the axis gloss (L676–677) | Phase 4 FIND-P4-21 (L220): "Raising: the chore no day notices and every decade does". One property at two scales: the snow lands every year; the lifting need not. Phase 10's own stage-B facts side with Phase 4 (L1411: the new complex stands on 3 m struts against burial; L1408–1409: a garage on a sled moved to keep it from drifting in). Also Gate 11. | C (A and B agreed) |
| 6 | **Danger that does not arrive unseen.** Phase 4 FIND-P4-11 (L196): "does not arrive unseen: the air is still, and when visibility closes something is actually falling" | Phase 10 CAT-B2-3 (L1763–1769): on the coldest still days the city's own breath, heat and vapor close the view over the inhabited part, nothing falling (conditional, REQ-B2-1). Step 5 RC-21 and FIND-S5-6 (L804–808) narrowed the spine's form ("holds outdoors and away from the city, not over it"); REQ-165 does not carry it to Phase 4's own sentence. | C (A as A9; B agreed) |
| 7 | **The shared night, un-narrowed in Phase 9.** Phase 9 FIND-P9-39 (L348): "Everyone stops at the same clock hours, robots to charge and humans to sleep"; FIND-P9-15 (L278): kept at the same clock hours as the humans' sleep | Phase 9's own FIND-P9-31 (L326), the night's keepers; Phase 4 FIND-P4-8, FIND-P4-42, FIND-P4-53. **RC-48 is confirmed** (Step 5 L317–325: "every layer and both bodies share the night's hours, less those whose function keeps it"; Q-233 asked Gate 3 to confirm it), but REQ-165 (L859) lists only Phase 4 L309 and L360 for amendment, not Phase 9 L348 or L278. Q-255 (the vision) may narrow it further, to the humans' night. | A, C (B confirmed RC-48) |

**Reconciled by narrowing, or held, PROPOSED (each a developer question or a request):**
- *No sky edge* (B): Phase 4 FIND-P4-5 (L184), FIND-P4-64 item 1 (L358) and Phase 9 FIND-P9-15, FIND-P9-19 (L278, L286: the sky gives
  her day no edge for about 243 days) against CAT-B1-5's noon twilight: an edge (no sunrise or sunset bounds the day) against a midday
  marker. C cleared it; B proposes one docket line beside REQ-170 (Q-320).
- *FIND-P4-40* (L266: "For about 120 days the only light the files write is the city's own"): A would amend it by RC-58's docket line; B
  holds it as worded (it states what the files wrote and names the request CAT-B1-5 answers in part); C cleared it (Q-320).
- *FIND-P10-9* (L919–922: "The threshold is the city's most dangerous ordinary place, for hands and for kept things"): B narrows it to where
  a kept thing, and the hands carrying it, are most at risk (its one research leg is about cryogen transfers); C reads it as consistent as
  worded (Q-321).
- *City-scale staying* (A, B): Phase 9 FIND-P9-33's heading (L330, "No term, so everyone admitted is kept"), Phase 9 L254, Phase 9 L413
  ("a closed road back for every human"), Phase 10 Q-B2-2's reason (L1916) and Q-211's premise (L1208) carry the form Step 5 RC-39 leaves
  open against audit RF-30, and are not on Q-225's list. The same shape as Q1's Gate 9 failure (Q-339).

**Consistent, checked (the union):** polar night 120 days, midnight sun 123, 243 with no sky edge (Phase 4 L184 against Phase 9 L278,
CAT-56, CAT-58, Step 6 row 3); water 0.121–0.125 kWh a liter; robot upkeep 4,484; air by month 3,825–3,950 m; the worst seasons (robots
April to September, humans June to August); the coldest month; raising at 6.8–7 cm a year (2 ÷ 0.07 = 28.6 years; 2 ÷ 0.068 = 29.4); the
light season, November to January; care formed elsewhere; the dead stay; the research may pause and the shaft may not (FIND-P10-4; RC-36);
free of spoilage, not of loss (RC-37); rescue; born-here and built-here nulls; Step 6 row 4 against the Phase 4 axis; SC-1 against Phase 4
L172, L182; CAT-44's "comes for a term and stays" by RC-40. Not internal: the T2 vision's robots with no fixed hours (RL-42, Q-255), a
read-last result.

**Fix (PROPOSED):** ERR-78 to ERR-84.

**Pass verdict: FAIL** (Q2 FAIL · Q3 FAIL; Q1 not assigned).

### Gate 4 — The swap test

**Question** (`04` L143–148): would the strongest findings survive essentially unchanged on a comparable location? Choose the real-world
partner most likely to survive the swap, never a Tepenian city; record which finding was weakest; where the datasheet's note applies (the
two baseline figures that disagree), reconcile or leave explicitly open.

#### Q1 — PASS (A PASS · B PASS · C PASS), the weakest finding a developer question

**Partners, by role:** A: a generic inland ice-plateau research station at comparable latitude and elevation, and a high-latitude inland cold
town with year-round residents. B: a mining city in a continental subarctic interior; an ice-sheet summit research camp; a high-latitude
archipelago research-and-mining town (research FACT-76); a planned science town (research FACT-93); an interior ice-sheet site; a national
laboratory host site; the ocean-navigation revival (research FACT-68). C: a generic year-round inland ice-sheet plateau research station,
and a generic settler town founded by a small specialist group and grown by later arrivals.

**What survives (the union of the three tables):**

| Finding (source) | Result under the swap |
|---|---|
| Heat at every place a body stops; rest located (spine L122, L406) | **In part.** The physical core survives on any plateau site; "one supply carries both bodies' lives" (spine L373) and the unnamed payer do not (A, C). On the subarctic city it holds in winter only; the city's warmest monthly mean is −31.3 °C (B). |
| *Only the work that is its purpose can ever be stopped* (spine L224, L229) | **Survives** on a plateau station or summit camp (A, B, C); already qualified inside the city at the shaft (research FIND-10 L222; P3 FIND-P3-50 L236; Q-55; Q-96). |
| *Snow without weather* (P3 L326–328) | **Survives essentially unchanged** on the plateau station; P3 L328 states the weakness itself (A, B, C). |
| *Assigned specialist wave, arrival-grown* (P2 L330–332) | **Survives almost unchanged** on a planned science town, except the no-return clause, which P2 names national (B). |
| *Attracts by work, repels by body* (P2 L202) | **In part**: the robot half and no-return do not survive (B). |
| "The stock the city weighs most is not the stock that founded it" (P2 L147) | Fails on the station (A); survives in shape on the settler town (C). |
| The archive held by people with no term (P3 L250, L302–304) | Does not survive (B), but its no-term half is over-asserted (Gate 9). |
| *Records are not teachers* (research L235; P2 L244) | Fails on its sharp half (B). |
| "For the robot majority, the native layer is the culture; for the human minority, the native layer is the cost" (P2 FIND-P2-41, L263) | **Fails on both partners: the strongest under the swap** (C). |

**Weakest under the swap (a split, settled as (c) by all three):** A: P3 FIND-P3-74, *Snow without weather*; B: P2's axis, "assigned
specialist wave, arrival-grown"; C: the spine sentence's clause "of all its work only the work that is its purpose can ever be stopped"
(spine L229). Each reader lists another's choice as second weakest (Q-291).

**The datasheet's note** (DS7 L36–38: `09` §2's 42.6%, 43.9% with the robot term, against `16` §23's 39.4%, on one workforce of
363,036). In Q1's files it is **reconciled by rule and left open in substance**: the audit recomputes 154,757 ÷ 363,036 = 42.63% (audit
L127); the spine holds that §23 governs (spine L337–339, `DR-142` item 8); spine REQ-35 (L551) notes that `16` L31–32 discard `09`'s
Required and % WF columns; spine REQ-34 reconciles only the first pass against §23. The datasheet's stated cause (`09` L216; the food term
at 10%) is in no Q1 file. C's hand check, on one denominator:
- `09` without the robot term: 154,757 ÷ 363,036 = 42.63%.
- `09` with the robot term: 154,757 + 4,484 = 159,241; ÷ 363,036 = 43.86%, printed 43.9% *(an inference: it holds only if `09`'s robot
  term is §23's 15.75 per 1,000, 284,693 × 15.75 ÷ 1,000 = 4,483.9)*.
- `16` §23: 143,209 ÷ 363,036 = 39.45%, which already holds the robot term.
- Like for like: 159,241 against 143,209, a gap of 16,032 workers, 4.4 points of the same workforce.
(REQ-211.)

#### Q2 — PASS (A PASS · B PASS · C PASS)

**Partner, by role (all three):** a real-world year-round research station deep on a high inland ice plateau, wintering a crew, supplied
by traverse and by air: the partner most likely to expose a shared answer.

| Axis (source) | Result under the swap |
|---|---|
| P4, *The warm stop, kept by the clock* (L381–383) | **In large part:** clock-set hours in polar night, heated modules, a night layer keeping the plant. Not the 64.50% robot majority for whom stopping outdoors is the danger; not *no date out*. |
| P5, *Parented on paper, supplied by the road* (L507–509) | **In its generic half**, as Phase 5 itself states. Not the subnet's hub about 1,260 km away with no road while the one highway leaves the subnet on both sides; not the shared outpost. |
| P6, *Taught by paper, owed in person* (L486–504) | **Does not survive:** a crew is handed over by a living predecessor and leaves on a date; the comparable pays its newcomers' instruction with a departure date (P6 L225, divergence stated). |
| P7, *An order that cannot send anyone away* (L874–899) | **Seasonally:** in winter a station cannot send anyone away either. Not permanence, all year, both bodies, 441,378 people, care that cannot be made in place. |
| P8, *Carried in, kept frozen, paid for in heat* (L287–289) | **Almost wholly, in its human half**: food carried in, free frozen keeping, snowmelt at a heat cost, burial by accumulation. Only the robot half (siligel as food and warmth, FIND-P8-2; two food chains on one supply, FIND-P8-10) and the language findings hold. |

**Weakest under the swap (all three agree):** Phase 8's human-food, water and keeping findings (FIND-P8-4, FIND-P8-6, FIND-P8-7, FIND-P8-15,
FIND-P8-16; A adds P4 FIND-P4-14), which would stand word for word at the comparable. Phase 8 states the weakness itself (L289: "it is an
axis of conditions, not of culture"). Recorded as the weakest finding, not as a failure: it is accurate physics, and its differentiating
weight rests on the robot half.

**The datasheet's note:** Q2's files use §23's 39.4% only (P4 L168, L170; P7 L285; P8 L255) and say why: P4 L16 ("DS4 L15 carries `09` L57,
whose Required and % WF columns `16` L30–32 says to discard", as C pasted it); P4 L601 (Q-102: "`09` is superseded as a result (`16` L6,
L30–32)"); P7 L282 (§23 governs, `DR-142` item 8); P4 L16 records `09` §3.5 as not opened, a hole and not an empty result. The gaps are
42.6 − 39.4 = 3.2 points and 43.9 − 39.4 = 4.5 points (B). **Settled by rule, not by arithmetic, and left explicitly open** as to which
baseline definition describes the city's civic floor (`09` L216, as the datasheet cites it), under Phase 4's own REQ-81; no Q2 finding
cites 42.6% or 43.9% (REQ-211).

#### Q3 — FAIL (A FAIL · B PASS · C FLAG; A's FAIL was not withdrawn, so it stands by the merge rule; the split is a developer question)

**Partners, by role:** a real-world year-round inland research station on the same ice sheet's high plateau (A, C); for single findings
(B), a year-round inland ice-sheet research station, a year-round frontier settlement with continuous induction of newcomers, a heated
sample archive at a polar station, and a deep ice-core drilling camp on an ice sheet.

| Finding (source) | Result under the swap |
|---|---|
| Step 5 SC-1, physical core (L752) | **Survives essentially unchanged** in its physics; not the city's size measuring the upkeep (441,378), nor two bodies on one supply (A, B, C). |
| Phase 10's axis, *Kept by the cold, raised by hand* (L968–976) | **Survives in structure.** The catalog's own convergence 6 (L1478–1483) finds the practice at three real places on one ice sheet; only the rates (6.8–7 cm and about 2 m a year) are the site's (A, B). C: L970–974 grounds the peer-free "Yes" on the site's rates (research FIND-8, FIND-9), and convergence 6 shows the practice shared, not the figures. |
| Phase 9 FIND-P9-35, arrival order over kind (L340) | **Fails:** a station's crews rotate, so the order resets each season (research FIND-25, as Step 6 L294 cites it) (A, C); B: the induction half survives on a frontier settlement ("induction is a frontier shape", Phase 9 L393). |
| Step 5 SC-4, the archive's two signals (L755) | **In part:** loss without signal at retirement is general; not an archive no single holder fully understands, held by people with no term (A, B). |
| Phase 9 FIND-P9-37, the skew in cost (L344) | Cannot be tested on any real place (no robots) (A). |
| Phase 10 FIND-P10-6, warmth, not cold, spoils what is kept (L906–910) | **Survives unchanged**; it rests on comparables only (C). |
| Phase 10 FIND-P10-7, FIND-P10-8 | Survive in physics (A, C). |
| Phase 10 FIND-P10-9, the threshold | **Survives unchanged** onto any laboratory with a cold store (B). |
| Step 5 FIND-S5-6, the still air's two faces | In part (C). |

**The failure (A, kept):** Phase 10's axis survives the swap in structure, so its peer-free answer "Yes" (L970–971), and Step 6 row 10's
"Yes" (L275), overstate; A proposes "In part". B would make it a FLAG (the peer-free test asks a different question from the swap); C a
FLAG or a question. **Weakest under the swap (a split):** A: the catalog axis (SC-1's physical core close behind); B: FIND-P10-9; C:
FIND-P10-6 (Q-323).

**The datasheet's note:** Q3's files cite §23 only (Phase 4 L168, L170, L272; Phase 7 datasheet L26), record `09`'s columns as discarded
per `16` L30–32 (Phase 4 L16) and superseded (Phase 4 Q-102, L601), and §23 as governing (RC-13, L117–122). **But RC-13 settles §23
against the first-pass Half B row (39.0 / 5.7 / 55.3), not against `09`, and no Q3 file states the `09`-against-§23 gap itself as
reconciled or left open** (C; A agreed and prefers C's fix: state it once, left open) (REQ-211).

**Pass verdict: FAIL** (Q1 PASS · Q2 PASS · Q3 FAIL).

### Gate 5 — Cross-location consistency, within the city's own relations

**Question** (`04` L150–154): is export and import coherent, read as relation? Does anything vented, emitted, sounded or spilled land
somewhere? Are new categories named and cross-referenced where their kind lives?

#### Q1 — FLAG (A PASS · B FLAG · C FLAG; A conceded the FLAG in Round 3)

**Coherent (all three):** export: spec L167 "exported almost nothing else" beside the chambers shipped from the airport outpost (L169),
resolved at P3 FIND-P3-55 (L256): the chamber work sits at the outpost on Hwy 37, not in the city. Import: food (spine D-1), siligel
(reserved, frame RF-21), power (a gap, `DEC-705`), people (`DEC-688`); the outpost's power (spec L171's opening clause, `DEC-693`) reads the
same at audit row 18, spine L65 and RF-39/RF-40. New categories (the street register, three registers, perpetual induction, the robots'
founding arrival not coined as a new mode, P2 L220, Q-81) are named and cross-referenced forward. The distance to the subnet's coastal hub,
about 1,260 km overland with no road, reads the same at contract L24, frame L263, spine L116, P2 L162; P3 L200's paraphrase was settled at
spec L9 (P3 L26).

**The FLAG: where the city's emissions land is unwritten** (B and C, each in its own form):
- B: the labs "breathe once-through outside air, continuously" (P3 L230); heat at every stop is vented somewhere; the air is still (5 m/s
  mean, no katabatic flow, P3 L112). No Q1 file says where vented heat, water vapor and exhaust go in air that barely moves at about
  −55 °C, or what they do to visibility near the city; P3 FIND-P3-36 (L202) and FIND-P3-2 may hold only away from the city's own emissions.
- C: the city's water is melted snow and ice (spine L114; research FIND-7), and snow settles out of a clear sky onto everything (research
  FIND-4); the files write two things the city sends into its outdoor air (once-through lab air, P3 L230; rejected heat, research UI-2,
  UI-7), and no line says where they land, although they land on the snow the city melts. The real site siting its precipitation trap about
  50 m windward of buildings (research FACT-91, L181) is the same shape of concern.
Nothing is asserted; a research request is filed (REQ-212).

**Pointer to Q2 (B133):** the ~1,260 km gap and Hwy 37's route are checked only at the spec in Q1; their owner, `Highways.md`, is Phase
5's read (REQ-214).

#### Q2 — FAIL (A FAIL · B PASS · C FAIL; B conceded the FAIL in Round 3)

**Coherent (all three):** exports: knowledge only (spec L167, as P5 L292, P7 L378, P8 L191 cite it); half the science as a share of
labor, in the model only (P5 L350; P7 L331–340); chambers made off the city's ground at the outpost and shipped out (P5 L281–286; P7
L379–381; P8 L191, L261); no ordinary product, a null (P7 L395–404). Imports: food for humans by Hwy 37 from a coastal port; freight and
building material; siligel by shipment unless made here (PV-6); carers by window; researchers from member cities of the subnet,
PROVISIONAL. New categories (the warm stop, the night's keepers, the turn of instruction, the forward debt, the outpost, the *Other 10%* as
an empty slot) are named, reserved with RF numbers and handed forward (P5 L522; P6 L516; P7 L937; P8 L300). The pass's own canon-side finds
stand: the relationship database L180's stale Hwy 37 order (P5 REQ-100); README L66's *ice-shelf* against §23's *ICE-SHEET* label (P7
REQ-117).

**The failure: electricity listed as received** (A, C; B conceded). P5 L304 (the table): "| **its own electricity** | **not written** |";
P5 L436 (FIND-P5-43): "**Whether the city is on the grid: not written. What powered it before the grid came fully online: not written.
Nothing is assumed.**"; P5 L357: "The nation does not supply, in any line: … **and a written source of electricity for the city itself**"
*(as C pasted it)*. Against them, P4 L363 (FIND-P4-64 item 6), under "**Supply from elsewhere:**": "electricity for both from a source
unwritten"; and P7 L389–392 (FIND-P7-9), under "What it receives": "electricity from a source no record places (`DEC-705`)". Listing
electricity as supplied from elsewhere assumes an import that `DEC-705` and PV-7 leave open: a lag behind the ruling (also Gate C).

**A FLAG kept beside it, the shared environment** (C; B as REQ-B107; A under Gate 1 as the refuse point): the labs' once-through heated
air is costed (P5 L436; P8 L187) but its destination is not; the city's refuse, spills and worn parts appear only as "whatever is set out
and left is kept by the cold and taken by the snow" (P8 L189); what fills the shaft is not named in Q2's spans (P8 L277; Phase 3
FIND-P3-23 by its index title only); a city of 441,378 standing on moving ice gives off heat. No Q2 line writes where anything the city
emits or spills arrives; nothing contradicts it. Recorded beside Q1's request (REQ-212); nothing is to be written about the lake (RF-6).

**Fix (PROPOSED):** ERR-52, ERR-53.

#### Q3 — FLAG (A PASS · B PASS · C FLAG; A conceded the FLAG in Round 3, B called it minor and put it to the developer)

**Coherent (all three):** §23's forced importer with a food term at 10%, the mandate half the science (Phase 7 datasheet L26–34); what
flows out is research, booked as labor in the model only (RC-66; FIND-S5-9); the one making for others happens off the city's ground, at
the waypoint outpost (RC-18; Phase 9 FIND-P9-14; CAT-11); what flows in by Hwy 37 is food for humans, carers, siligel, parts and arrivals
(FIND-S5-3; Step 6 row 8); people and means from member cities of the Mirny subnet (PA-8; Step 6 row 8). New categories are named,
numbered and routed (the made-colder store, CAT-6, REQ-154; the clean side, CAT-B1-1, RF-194; the city's own ice fog, CAT-B2-3, RF-207;
the map of what lies under the snow, CAT-B1-2; the placement log, the sealed carrier, the first stop). Relation slips already carried:
CAT-11's airfield citation (REQ-176); the outpost's end read past spec L171's clause (RC-78; RF-211); the relay at the next city on Hwy 37
(RL-46, Q-261). Written shared-environment consequences: the city's own vapor over the inhabited part (CAT-B2-3; FIND-S5-6, conditional);
the shaft's fill fluid reaching what is sampled from the lake (FIND-P10-8); heat melting snow under buildings (B1 extends CAT-23).

**The FLAG (C):** one emission has no written landing: what the city discards and where it goes under the snow is asked, not written
(REQ-B1-2, L1539–1540); nor what the shaft's fill fluid does to the lake itself, as distinct from the samples (RF-6 holds the lake's
contents) (REQ-212; Q-303).

**Pass verdict: FAIL** (Q1 FLAG · Q2 FAIL · Q3 FLAG).

### Gate 6 — Duplicate institutions (within the location only), with substitutes 3 and 4

**Question** (`04` L156–167): does this pass name the same institution twice? The against-siblings half is terminal and **NOT RUN**.
Substitutes 3 (real-world comparables) and 4 (the generator-conflict method) run; substitute 1 deferred to after the pass; substitute 2 not
run (`DR-142` item 2).

#### Q1 — FLAG (A PASS · B PASS · C FLAG)

**Checked (all three):** the research program (spec L167); the research facilities and labs, one institution under three words (spec L177;
P3 L230; P3 L240); the shaft and drilling apparatus; the archive (spec L179); the stores (P3 L234); the cold-record marker (spec L178, an
open slot); the district's name honoring scientists (`DEC-684`); the airport outpost (a relation). The marker and the district honor are two
acts of honor on two objects (B). The research program and "a scientific culture built from records" (P2 FIND-P2-35) are one thing seen as
institution and as culture (C). The common cold store (research FIND-37) is a reserved candidate (B).

**The FLAG (C, single-reader find, kept; settled as (c) by all three):** *the stores* may be named twice. P3 counts the stores (FIND-P3-49,
L234; FIND-P3-51, L240) and the archive (FIND-P3-52, L250) as separate institutions, but the stores' evidence is ice cores and samples
("cores kept in the real site's trench", L234, from research FACT-87), while F-3 says that whatever the archive holds as objects keeps best
cold (FIND-P3-69, L302), and research's common cold store (FIND-37, L249) is a food store. A reads the archive (understanding held in
people, P3 L250) and the stores as distinct (Q-292).

**Substitutes:** 3 was run at Step 3 (research §3–§5, each comparable with its outcome and divergence stated, research L87–187); 4 was run at
spine §4 (two conflicts mined by the both-are-true test, L218–224; contract Q-9's conflict discharged, L227); frame DL-12 (L103) names
both, records substitute 1 as deferred and substitute 2 as not run.

#### Q2 — FLAG (A FLAG · B FLAG · C FLAG)

**Three FLAG items, each a developer question:**
- **One mechanism under five names** (all three): membership by the turn of instruction (P5 FIND-P5-35, L408–414; RF-131); the social
  contract with a debt inside it (P6 FIND-P6-4, L186–206; RF-137); the standard of worth, being needed (P6 FIND-P6-7, L233); learning and
  belonging as one process (P7 FIND-P7-29, L661–664; RF-160, RF-161); the mark of being from here (P8 FIND-P8-32, L233; RF-174). Each cites
  the others (P6 L191; P7 L662–664: "Learning and belonging are one process here"; P8 L233), so it is not a hidden duplicate; but four or
  five reserved rows invite a later phase to write one mechanism as several institutions. B proposes RF-137 as the parent, the others its
  aspects; C agreed in Round 3 (Q-307).
- **The shaft's watch in two rows with two answers** (C, single-reader find; A and B agreed in Round 3): P7 L446, row (i): "| (i) | the
  shaft | not whether, but who watches: … | not written |"; P7 L449, row (l): "| (l) | the night's keeping | on whoever keeps heat, water,
  charge and the shaft running through the shared night … | the keepers, a function |" *(both as C pasted them)*. Row (l), P7 L490, P6
  L447 and P4 L611 (Q-112) give it to the keepers; P4 L303 calls the shaft "the research's one never-off structure". The same object as
  Gate 3 item 8 (Q-308).
- **Heat and charge booked in two tiers** (A; B cleared it by scale; C (c)): P4 L170 and P7 L301–302 put keeping the city's bodies "fed,
  warmed, cared for and charged" in the baseline (39.4%); P7 L370–373 puts heat at every stop, water by melting and warm charge in the
  survival sector, "beyond every city's baseline". The both-are-true test reconciles them by scale, but no line says how the tiers split the
  work (Q-306).

**Cleared:** the night's keepers are a subset of the baseline functions (P4 L190, L303); the institution that keeps the clock (P4 L184; P7
L444, row (g)) and the research institutions' calendar (row (h)) are not asserted to be one body, and the clock-keeper is unnamed; the
outpost is written once, as a joint work (P5 L281).

**Substitutes:** 3 was run as the Gate 4 swap: the shared answers it exposes are Phase 8's conditions and Phase 7's seasonal no-exit; the
keepers match the picks' rostered night layer, written as a real-world form "not transplanted" (P4 L190); induction diverges from a real
crew's handover on the no-term axis (P6 L225, divergence stated). 4: conflicts mined, not smoothed (the physical constraint against the
purpose: the headline written away from, P4 L168–172; the purpose yields first, P6 L429–434, contested, Q-142; survival booked FREE, P7
L349–357; a founding from records against an archive held in people, P7 L620–623; one road against two bodies, P8 L169; the robot against
the human outdoor rule, P4 FIND-P4-12, P8 FIND-P8-20; the picks' cohorts against no term, P7 FIND-P7-32). C names one conflict left
unresolved, the shaft's register (research structure against the street's keeping): the same item as the two rows above. Substitute 1
deferred; substitute 2 not run.

#### Q3 — FAIL (A FAIL, minor · B FLAG within the location, FAIL on substitute 4 · C PASS; C conceded in Round 3)

**Within the location:** no institution is named twice in A's or C's reading (the archive and its holders are a place and a role; the
common cold store and the made-colder store are two stores). **A's FAIL (minor, not withdrawn), duplicate catalog entries:** CAT-35 (L779–781,
"The drilling apparatus, as the research's tool") repeats CAT-2's "its drilling apparatus" (L692; spec L177); CAT-78 (L869, "the first
teacher of the newest arrival") repeats CAT-36 (L785, "The earlier arrival who teaches where to stop"); its other half, the oldest living
keeper of the shaft, is its own. C found the CAT-2/CAT-35 double independently (under its Gate 0). B adds the other doubles (CAT-56 and
CAT-72, the first sunrise as a setting and as an event; CAT-59 and CAT-71, the arrival; CAT-50 and CAT-77, the city's own honored
scientists) and **one research program under two names** (B, single-reader find; A and C agreed): CAT-12's "the lake program" (L727–728)
and "the genetics program" whose living stock needs CAT-6 (L709–710; FIND-P10-7; L1380–1383), with CAT-76's "lake genetics program"
(L862–863); whether these are one institution or two is written nowhere, and Step 5's REQ-169 narrowing would remove the second name. **B's
objection, beside the FAIL:** the gate asks about institutions named twice, not things or roles, so FLAG fits better (Q-324). The research
population (Phase 9 FIND-P9-29) and the archive's holders (CAT-38) are one group under two names, already equated at Phase 9 L250 and L322
(A): recorded, not a defect.

**Substitute 3 (A, B, C):** run; every comparable the catalog uses converges on a structure and diverges only in figures (convergences B1-1
to B1-6, B2-1 to B2-7); Phase 9's order of arrival never resets because the city has no date out (Phase 9 L413). B adds that §10's axis is
about as exposed as §3, which Step 6 flags alone (L291, L309).

**Substitute 4, FAIL (A, B; C conceded):** Step 6 L318 counts nine of ten axes as products of a generator conflict, but §10's axis is "G2
against itself at two depths" (L316): eight of ten. With A's Gate 4 point, the catalog axis is the pass's second single-generator axis (with
§3's), the more exposed to the author-defaults risk Step 6 L282–283 names. Phase 9's axis is kind (G8) against arrival order and no return
(G4, G6), a conflict (A, C). Substitute 1 deferred; substitute 2 not run.

**Fix (PROPOSED):** ERR-74 (substitute 4), ERR-86.

**The against-siblings half: NOT RUN** (terminal; `04` L156–167; `DR-142` item 2).

**Pass verdict: FAIL** (Q1 FLAG · Q2 FLAG · Q3 FAIL).

### Gate 7 — Research accounting

**Question** (quick reference; `04` Part I): every pick in the catalog's pick-incorporation table (official picks and candidate rows)
classed changed · ornamented · withheld · omitted; roughly 70–80% changed is expected; a low share is reported, not adjusted.

#### Q1 and Q2 — not assigned

#### Q3 — FLAG (A FLAG · B FLAG · C FLAG): a low share, reported, not adjusted

**Checked (all three):** stage B1's table (Phase 10 L1244–1274, rows 1–29) and stage B2's (L1597–1655, rows 30–86), with stage A's
research for rows 1–3. The pass classes each row *taken* (a new item or an *extends* note) or *not taken* with a closed set of reasons, not
in the gate's four terms, so each reader classed the rows: *changed* = a new catalog item or a changed finding; *ornamented* = *extends*
notes only; *withheld* = nothing taken, held for a named later stage or barred by a named ruling; *omitted* = nothing taken, no line
allows it and a request only. Every row 1–85 was researched; row 86 waits by the developer's ruling (L1655), as LAW 0-P requires. Withheld
is not unused: the WAITS lines (41 in B1; 29 in B2) record what each would give and where it is held.

**The share, as written: 27 of 85 = 31.8% changed** (C's count; **B withdrew its 31 of 86 in Round 3** in favor of it, agreeing that rows
whose convergence only *supports* a finding are ornament, and that unresearched row 86 is out of the base).

| Class | Rows (C's count, the share written) | Count |
|---|---|---|
| changed | B1: 1, 2, 3, 6, 11, 12, 14, 20, 22, 24, 25, 26, 27, 28, 29 · B2: 43, 45, 53, 54, 60, 66, 75, 76, 77, 79 · plus 49, 59 (convergence 1 lifts FIND-P10-6 "from an analogy among comparables to evidence", L1823–1824) | 27 |
| ornamented | B1: 4, 5, 9, 10, 13, 15, 16, 21, 23 · B2: 30, 31, 32, 38, 39, 42, 46, 51, 52, 55, 56, 57, 58, 61, 63, 64, 65, 68, 69, 70, 71, 72, 73, 80, 83 | 34 |
| withheld | B1: 7, 8, 17, 18, 19 · B2: 33, 34, 35, 37, 40, 41, 47, 50, 67, 74, 78, 81, 82, 85 | 19 |
| omitted | 36, 44, 48, 62, 84 (row 84 per its tally; see Gate 0) | 5 |
| not researched | 86 | 1 |

27 + 34 + 19 + 5 = 85.

**All three counts, reported:** A: 25 of 86 = 29.1% (28 of 86 = 32.6% lenient, adding rows 49, 59 and 51); over the 85 researched rows
29.4% (32.9%). B (withdrawn): 31 of 86 = 36.0%. C: 27 of 85 = 31.8%. If every *taken* row counted as changed: 61 of 85 = 71.8% (C; B's
61 of 86 = 70.9%). The three official picks: 3 of 3 changed. A's hand check of one row against its source: row 12 (L1257) → CAT-B1-2 and
CAT-B1-3 rest on the facts it names: changed, confirmed.

**Open choices, each a developer question (Q-325):** (1) whether an *extends* note counts as change (settled in Round 3 toward ornament
for this share; the developer's to confirm); (2) the base: the whole LAW 0-P list, or the PRIMARY tier as well (A: 26 PRIMARY rows, 11 to
12 changed, 42–46%); (3) rows 43 and 45 count as changed only through CAT-B2-8, whose one city line is the excluded spec L157 (Gate F): if
CAT-B2-8 stays held, the share falls to 25 of 85 = 29.4% (A: 23 of 86 = 26.7%). Neither choice lifts the share above one third. The cause
the files show is LAW 0-P's whole-list scope (every candidate row researched, most of them lower tiers), with many rows' yield falling in
the waiting topics; the low share is reported and not adjusted.

**Pass verdict: FLAG** (Q3 only).

### Gate 8 — The standout

**Question:** name the single strongest thing the pass produced, and why (Step 5's SC-1 is the reconciled candidate; confirm or dispute it
on the evidence).

#### Q1 and Q2 — not assigned

#### Q3 — PASS (A PASS with a FLAG on what to record · B PASS · C PASS): SC-1 confirmed

**SC-1 is confirmed as the strongest finding on the evidence (all three):** "The city is kept alive against its environment, not by it:
heat must be paid without pause at every place a body stops, water is bought with the same heat, and the city's size measures that
unending upkeep." (Step 5 L752, as C quotes it). It is the finding the most others rest on (L764–768: SC-4's loud half, SC-5's prices,
SC-6's bill, SC-8's extension, RC-36's single property); its legs are measured climate, ice physics, Census I and rulings, with no
provisional parent assumption (L768–769); stage B found its named leg (i) "**CONTRADICTED IN PART, by tier-3 lines only**" (L1288) and legs
(ii) and (iii) untouched (L1305–1309); the T2 vision on the robots' hours does not touch it (L1261–1262).

**Recorded against it, not a dispute of the verdict (all three):** under the swap its physical core survives on a real plateau station
(Gate 4), so it is the strongest by load and by evidence, not the most place-specific product. **The place-specific standout is a split
(c):** A names SC-4, the archive's two signals (L755: a heat lapse announces itself within hours; an understanding no single holder has
thins with no signal; it stands on spec L179, Phase 9 FIND-P9-30 and Phase 10 FIND-P10-5, and its no-signal leg is now a contested absence,
L1316–1320); B and C name SC-3, taught by paper, owed in person (L754; spec L145), which fails the swap but rests on PROPOSED readings and
absences (Q-326).

**Pass verdict: PASS** (Q3 only), the place-specific standout put to the developer.

### Gate 9 — Asymmetry, second run (on what this pass wrote)

**Question** (`04` L221–241): for every threshold, gate, conversion, verdict, admission or status change this pass wrote, does the mechanism
run both ways? What happens to whoever it decides against, is that as durable, and is there a route back? A "no route back" nobody
perceives as a problem is a shadow.

#### Q1 — FAIL (A FAIL · B FAIL · C FLAG; C conceded the FAIL in Round 3)

**Items that hold (the union of the three readers' tables):** the type, Settlement, run both ways (frame DL-2 L74); Band 4 with
decomposition deferred (RF-3); the extent band "by construction", its circularity stated (frame DL-5; spine §7); status Living, at the
height (RF-11); the generator selection, with those left out read beside (Q-41); the shape *Balanced* against *Cost-dominant* (Q-46); the
deficit addresses, with SH-6 and RF-50 recorded; the station rule's seven dropped facts (research §3.2; Q-63); the contract's exclusions,
with a route back demonstrated (spec L171's opening clause readmitted by `DEC-693`); the assignment with no rotation (P2 FIND-P2-17, L195;
SH-9; RF-84); the specialized admission (P2 FIND-P2-21, L206; SH-10, losing side named as unwritten); the permanent price written as free
choice (SH-8); the founding-wave tag (nothing conferred or denied, P2 FIND-P2-8); the staffed-against-settled tension, written as two
registers inside one Settlement (P3 FIND-P3-54, L254; RF-24); the labs' heat (SH-11) and the slow burial (SH-12); *only the purpose may
fall silent* beside the shaft that cannot pause (P3 FIND-P3-18 against FIND-P3-50; Q-96); the smell register (P3 FIND-P3-22); breath as the
one written mark between bodies (RF-96).

**The failure: absence of a written departure turned into "no one leaves".** RF-30 (audit L208) reserves departures from the city, and
lists among what would foreclose it: "**Asserting that no one left**; importing departure from the Census I → II change…; citing a road as
a written departure". The ruled fact is narrower: a human cannot return to *Upper Earth* (brief §4 item 5; `DR-127` item 2). Leaving the
city for elsewhere in the nation is "possible and written nowhere" (P2 L214, L222, L299). The spine itself shows the correct form at L219.
Raw evidence (A; B added the spine sentence, the FIND-25 heading and RF-104):
- research L237 (FIND-25), heading: "**A place people cannot leave keeps what the comparables send away.**"; body: "…and **the city must
  hold its losing side inside,** working or not"
- research L478 (RF-72): "The city must hold its losing side (FIND-25)"
- spine L229: "and those who came have stayed"
- P2 L232 (FIND-P2-32): "the population cannot renew itself by people leaving"
- P2 L406 (SH-10): "so whoever came and did not fit has no exit and no written place"
- P3 L198 (FIND-P3-34): "so her first impression is of the place she will live in"
- P3 L252 (FIND-P3-53): "met by the same physics and the same law that keep everyone here"
- P3 L302 (FIND-P3-69, item 2): "so understanding does not leave with people who leave"
- P3 L304 (FIND-P3-70): "whatever the archive loses, it does not lose by people leaving; its understanding is held by a population that
  stays." RF-104 (L384) carries the same title.

**A new fire, all three readers (a shadow candidate, not an erratum):** "a condition, not a filter" (P3 FIND-P3-45, L226; forwarded at
L343). Only the favorable side is written; the side decided against, an arrival who cannot learn to stop safely in the cold or whose body
cannot bear it, and who cannot go back, is unwritten in Q1's files; the cold's verdict on that person is durable; no route back is written.
The index titles FIND-P7-27 and FIND-P7-36 ("What becomes of the ones who cannot learn it: they are kept.") may discharge it; read as
titles only in Q1 (see Q2) (Q-293).

**Fix (PROPOSED):** ERR-8 to ERR-16.

#### Q2 — FLAG (A FLAG · B FLAG · C FLAG); the fires are the union

**Mechanisms with both sides written (the union of the three tables):** membership by the turn of instruction (P5 L408–414; P7 L661;
P8 L233), its losing side the never-asked and the permanent newcomer (P6 L263, L436–439, SH-23; P7 L722–736); the forward debt (P6
L186–206; SH-23); the honor's admission (P6 L173–184), its losing side the keepers of the heat (SH-25), perceived; the carers' window (P4
L224, L339); the rescue threshold (P4 L333; P4 L242, the scar SH-13, repair open at its source); exclusion's price (P7 L583–602; SH-28,
"whoever the order fails is kept by default"), perceived; the mandate as allocation (P7 L331–340; SH-27; Q-156); the trade closed in place
(P7 L716–720; SH-30); the forfeiture (P7 FIND-P7-22, national, `[treaty draft]`); the language tier (P8 L223–229; SH-5); subnet membership
(P5 L367, row 115, cost and change said to be not written). Items handed forward from Phase 4 are answered: the keepers (SH-15) and the
night's exposure (SH-14) with their losing sides (P4 L448–452); everyone kept and the losing side held inside (P4 L341; P7 L733).

**Pointer back to Q1's shadow candidate** (P3 FIND-P3-45): Phase 7 writes what becomes of an arrival who cannot learn the cold's lesson:
she is kept in body and never becomes the teacher (P7 L722–736, FIND-P7-36), so the losing side of *being kept* is written. The losing
side of *belonging* is A's fire 2 below (Q-293, Q-310).

**Second-run fires, each an unwritten or unnoticed losing side** (A 22–23; B 116–117; C, the Gate 9 table; all agreed in Round 3, with C's
pre-empted-disposition point put to the developer):
1. **Membership can lapse** (A): P5 L414 defines membership as being needed, not being admitted, and L413 says nobody un-becomes a member by
   leaving; but being needed can stop (a holder no longer asked for; a settled resident once no one newer comes, P7 L656). Loss by ceasing
   to be needed, the reverse of the file's own criterion, is unwritten (Q-309).
2. ***Never a filter* holds for being kept, not for belonging** (A): P4 L200 (FIND-P4-13) and P7 L642–646 call the survival lesson "a
   condition, never a filter"; P5 L403 ("an outsider is someone not yet taught"), P8 L233 ("the line between inside and outside is
   knowledge") and P7 L726 ("she stays a permanent newcomer") build a filter for belonging on the same knowledge, with a losing side. Two
   objects, so no contradiction, but no line says so; P4 L399 handed exactly this to Step 7 (Q-310).
3. **The purpose yields first, and the shaft** (B): the ordering decides against the research; for the instruments the outcome is a pause
   with a route back, for the shaft, which "cannot be paused without loss" (P7 L446), closure with no route back. FIND-P6-26 does not say
   which (Gate 3 item 8; Q-311).
4. **No point of entry for anyone who never arrived** (B): the only written membership is keyed to arrival order; for a robot built here
   (P4 L298) or a human born here (a null), Phases 4–8 write no point of entry. The index lists a Phase 9 finding, "Conditional: a robot
   built here comes online as the newest arrival" (index L381), on Q3's list (Q-312; see Q3 below).
5. **The last arrival** (C): once arrivals stop, whoever arrived last has no one newer, ever; P7 L655 turns teaching only toward the newest
   among those already here, so she stays the taught: a timing form of SH-23 with no route back, and no line notices it (Q-313).
6. **The Review Panel's disposition used before the Panel runs** (C; (c)): P7 L894 disposes of an objection as "**refused, `unmet`,
   written as characterization.**", and P8 L289 the same. Step 8 is the route back, but these lines use the Panel's own word in advance
   (Q-314).

#### Q3 — FLAG (A FLAG · B FLAG · C FLAG); the fires are the union

**Mechanisms with both sides written (the union):** arrival order and membership at the turn of instruction, against whoever never becomes
the earlier arrival (Phase 9 FIND-P9-35, L340 third order; SH-35 L475; Phase 7 FIND-P7-36; Phase 6 SH-23); rescue, against the one not
reached (FIND-P9-41; Phase 4 FIND-P4-55; RF-182); the human minority renewed only by the road (FIND-P9-26; SH-37); the marker's raising,
re-filed under `DR-143` item 2 (FIND-P10-2; RC-69; REQ-180), the marker buried if raising lapses (SH-39), its route back for a buried marker
unwritten (C); the sample judgment, the lake's or the shaft's (FIND-P10-8; SH-43; the strict shadow, B2 sign 6, L594); the keeper's
successor, narrowed at RC-59; the hardest choice under shortage falling on the shaft (FIND-S5-2), route back by re-drilling in the catalog
(CAT-B1-8); the excepted robot under the predominance rule (FIND-P9-4; RF-32), perceived; Step 5's OUT OF FRAME rows, route back by an
admitted line or a ruling (Q-237); Step 6's cells, route back by the developer's wording (REQ-198). Phase 10 L998 hands the district honor's
city half to Step 7; it is run below.

**Second-run fires, each an unwritten or unnoticed losing side, each offered as a shadow candidate** (all three agreed in Round 3 that
they add to each other and none contradicts another):
1. **Membership held by the road or a chamber** (A): with no birth written, a permanent newcomer can turn the instruction around only when
   someone newer arrives by Hwy 37 (FIND-P9-26; SH-37) or, if a chamber stands, is built here (FIND-P9-13; PV-5), so the city's membership
   mechanism depends on its renewal (Q-327). The same family as Q2's fires 4 and 5.
2. **No written way into the research population** (A): FIND-P9-36 (L342) draws the city's one between-group line by being needed; a
   researcher becomes a member when a question first comes to her, and no line writes how a resident outside the research population is
   first asked; reserved as RF-183 (Q-328). B holds it as perceived (Phase 6 SH-23).
3. **The long pause** (A): during a pause (CAT-73 L852–854; FIND-P10-4; a real pause ran about a year and a half, one sector nearly three
   years, L1432–1434) no question comes to a researcher, so the research population crosses FIND-P9-36's line to the side with no written
   purpose, kept but not needed (Q-329).
4. **The honor and the keepers of heat** (A; B and C record the same leaving-out as perceived through SH-25): the city's one written honor
   names its purpose (FIND-P10-1; RC-68), and "The keepers of heat stand in no record" (Phase 6 SH-25, as CAT-39 and FIND-P10-6 carry it)
   (Q-330).
5. **The clean side's way out** (A): CAT-B1-1 (L1290–1297) writes a passage entered only from the city's side; how anyone leaves the clean
   side is not written; the rule is reserved for the DCI with RF-194 (Q-331). B adds that the losing side of the credential that opens
   nothing until instruction is done (RF-194), the one who cannot complete instruction (Phase 7 FIND-P7-36), must be written with it.
6. **The request path** (B): FIND-P10-15 (L938–941), *in person, or by request*: a request is a gate, and no line writes who is decided
   against (a request not answered) or any route back; the sender "never arrives and is not cataloged as a person". Weaker than textbook
   (Q-332).
7. **The unchosen successor** (C): a part one keeper holds alone passes only by that keeper's choice (Step 5 FIND-S5-7, L809–812; CAT-B1-3
   narrowed by RC-59); the would-be successor the keeper does not choose has no route back, and a part whose keeper goes before choosing is
   lost with no signal; the lost part is written (FIND-P6-25), the unchosen person is not. Weaker than textbook; RC-59 already withdrew the
   choosing as a practice into RF-212 (Q-333).

**Not reached:** the sweep places Phase 9 carries to Step 7 (L429: places 3, 9, 23, 30, 50, 65, 80, 83, 85, 88, 95, 96, 100–102, 104, 107,
109, 111) lie in Phase 9's sweep section, outside Q3's admitted span (B; REQ-224).

**Pass verdict: FAIL** (Q1 FAIL · Q2 FLAG · Q3 FLAG). Shadow candidates are offered as developer questions, never numbered SH here.

### Gate 10 — The Review Panel

**NOT RUN.** It is Step 8 (brief §2), run after this step; never recorded as "N/A". All nine readers recorded it NOT RUN.

### Gate 11 — Plausibility

**Question:** would a person actually do this, at this cost, for this reason? Its mechanical sub-check divides the population (Census I)
by the built extent (`Extent_and_Density_Per_City.md` L625), stated flatly as this city's own figure with the row hand-checked; report what
it cleared as well as what it flagged.

#### Q1 and Q2 — not assigned

For the record (B, C, from Q1's files): 441,378 ÷ 44 = 10,031 per km² and 441,378 ÷ 63 = 7,006 per km², which return the extent table's
own assumed densities, so the division is circular by construction (frame DL-5 L89; spine §7 L301). An independent footprint is still
requested (frame REQ-14; spine REQ-43; P3 REQ-69). Q2's readers found the same (B item 103; C question 206; A in Round 3), and C found no
distance, crowding or sparseness claim in Phases 4–8 to price against it (P4 FIND-P4-50).

#### Q3 — FAIL (A FLAG · B FLAG · C FAIL; C's FAIL was not withdrawn, so it stands by the merge rule; the verdict is a developer question)

**The density sub-check, the row hand-checked (all three).** Raw source row, as reader A pasted it whole:

```
raw source row (Extent_and_Density_Per_City.md L625), whole:
| **Vostok** | Mirny | 441,378 | 44 | 63 | **plateau** |
```

*(The first cell is the city's own former row label in that source's spelling; it is reproduced only inside the pasted row.)* Columns:
the city, the subnet, population, km² at 10,000 per km², km² at 7,000 per km², terrain. 441,378 ÷ 10,000 = 44.14 → 44; 441,378 ÷ 7,000 =
63.05 → 63. The national note (L631): 26,111,826 ÷ 10,000 = 2,611.2 and ÷ 7,000 = 3,730.3, "2,611–3,730 km²". The population is Census I
(156,685 + 284,693 = 441,378; B checked it at spec L17).

**This city's own figure:** 441,378 ÷ 44 = **10,031 people per km²**; 441,378 ÷ 63 = **7,006 per km²**.

**The density check is circular and cannot clear density.** The extent was made from the population at two fixed densities (Phase 4
FIND-P4-50, L317: "44–63 km² by construction, at the table's two assumed densities"; Step 5 PA-13, L587: "the division is circular"), so
the division returns the assumed densities by construction. The figures are reported; they price texture claims against 7,000–10,000 per
km² and test nothing else.

**Cleared (the union):** a compact city fits every written texture (short crossings between warm stops, FIND-P4-50; one supply at one
night load; the ice fog over the inhabited part, CAT-B2-3); the human night at altitude is sourced to a wintering crew and says so ("crews,
not residents", Phase 9 L294); the made-colder store, sealed carrier and placement log cost the same anywhere (FIND-P10-5, P10-7, P10-8;
living cells need about −130 to −135 °C, colder than the −89.2 °C record); SC-1; robot upkeep 4,484; the burial and drift arithmetic; rescue
needing another person (FIND-P9-41); renewal of humans by the road (FIND-P9-26, conditional).

**The FAIL (C, kept):** **lifting every standing thing every year** (Phase 10 L894; axis L676–677). Would a person lift every doorway,
post and collar each year for about 7 cm? Not at this cost: the pass's own facts show lifting on a cycle of years (3 m struts; sled moves),
and Phase 4 L220 says the chore shows per decade. The erratum is written once, under Gate 3 (ERR-82), and cited here.

**The FLAG readings beside it:**
- **The tonnage, as pricing for Step 10 (A; B checked it):** the measured accumulation, 22.5 kg per m² a year (Phase 4 L220), over the
  built extent is 22.5 × 44,000,000 m² = **990,000 tonnes a year** to 22.5 × 63,000,000 m² = **1,417,500 tonnes a year**, landing and
  staying on a city as dense as a real dense city. At that scale raising is jacking buildings, building above the snow (the real site's new
  complex stands on 3 m struts, catalog L1411) or moving about a million tonnes a year; a household-chore register understates it. The pass
  already writes the chore's size as unknown (Phase 4 L319). Offered as pricing, not a finding (Q-334).
- **Perpetual induction at city scale (A, B; C cleared it and gave way):** Phase 9 FIND-P9-35 (L340) and Phase 4 FIND-P4-13 assert
  person-to-person induction of every arrival in a city of 441,378 with an unwritten arrival rate, on comparables drawn from crews and
  stations of tens (research FIND-23, CONV-4; Step 6 L293). Who teaches a newcomer who arrives with many others at once is not written. The
  structure may stand; its scale is unpriced (`04` L257).
- **The shared night for every robot at the same clock hours (A, B; C's clearance gives way):** every robot charging at the same clock
  hours, in a city whose life support needs someone at every hour (Phase 4 FIND-P4-8), whose sky sets no edge, and where the national
  pattern is broken nightly by necessity (Phase 7 FIND-P7-20, as Step 5 L1238–1240 cites it), is the least plausible form of the claim; it
  supports Q-255's narrowing on plausibility grounds as well as the vision's.
- FIND-P10-9: a cryogen-handling injury pattern (fact 17) asserted of residents' hands at the threshold (B; Q-321). CAT-25's "every
  household" ice tools: plausible if crossings are outdoors, less so if the city is enclosed (`DEC-703` open) (B). Sound carried far in the
  still cold (CAT-B2-4), in a city at 7,000–10,000 per km²: weak, conditional, not failed (C).

**Pass verdict: FAIL** (Q3 only); the FAIL against FLAG split is put to the developer (Q-334).

### Gate C — The canon check, federated

**Question** (`04` L299–340): the four-question canon check against all three tiers, negative results traced to named paths; shared
constants checked at their SOURCE; a ruling's applied list checked against every file that states the fact; redirect stubs; rank order;
RESERVED routing; new things cross-referenced; which canon files were opened. (Runbook §E was not on the lists; the readers ran the gate on
`04`'s statement.)

#### Q1 — FAIL (A FAIL · B FAIL · C FAIL)

**Holds (all three):** every Q1 file carries a receipt of the canon it opened (contract L355–367; frame L412–431; audit L338–356; spine
L738–769; research L619–644; P2 L15–27; P3 L17–27). Negative results carry named paths (the grid and power files name neither the city nor
the outpost, spine L330–332; the concept-art folder opened and empty, P3 L23; "location registries" a recorded hole, frame L159). Shared
constants at source, hand-checked: Census I 156,685 + 284,693 = 441,378 at census L520, robots 284,693 ÷ 441,378 = 0.6450; the era
2564–2812 and the national tower's completion ~2688 (±~20) at the timeline (frame L93); the twelve monthly means sum to 657.2, ÷ 12 =
54.77 (spine L311); precipitation 22.0 mm (spine L314); polar night 120 and midnight sun 123 days (spine L319); the workforce 143,209 +
71,444 + 148,383 = 363,036; the Mandated 71,444 ÷ 363,036 = 19.68% and ÷ 219,827 = 32.50%; the live "≈ 3.8×" (71,444 ÷ 18,774 = 3.81,
DS-P7 L34; contract L102); the extent 44 and 63 km² at L625. Rank order is stated (§23 governs, spine L339; the record high's three values
not adjudicated, research FIND-35, Q-57; §23's "Canon §15" with no counterpart in the spec, spine L342, RF-42, REQ-39, Q-40). RESERVED
routing holds (robot return, audit Q-31; robot smell, P3 Q-90; the founding motive's national grounds, RF-83).

**The failure: rulings applied to some sources and not others** (`04` L333):
- **DS12 lags `DEC-691` and the contract's dispositions.** B and C through the audit (L220, REQ-24(a); the audit's L171 records that DS12
  was outside the 05:07 edits); A by an off-list read of DS12 L17–35, logged under the brief's §0 item 4. Raw evidence (A):
  - DS12 L35 ends: ""The name was kept" (now L149 of that file) is a naming fact only", against contract CR-45 and `DEC-691`, which EXCLUDE
    spec L149.
  - DS12 L17: "exact match, full monthly table also matches", against spine L312: the record holds the means only.
  - DS12 L26: "not reproduced here to avoid redundant duplication of a 12-row table": a pointer, not the data (contract REQ-7; spine
    REQ-35).
  - DS12 L34 calls the station's operation from 1957 "an infrastructure fact, `DR-24`", against contract CR-43, which holds it a coordinate
    only; the clause names the builder's nationality.
- **DS2 L16 lags the census's own retirement of its composition-tension clause** (census L440, `DR-35`), as P2 records it at L415 (REQ-62)
  (C, single-reader find; A and B agreed in Round 3).

**FLAG items, each a request or a question:**
- *The quarantined `06` folder* (A, single-reader find): frame §1 (L23–24) quarantines, for the whole run, the folder runbook L2074 names
  ("a folder named after the city and its topic") without knowing which folder it is; P3 L27 records "the city's own genetics research
  folder (tagged for Phase 7, brief §4 item 19; DS3 L13; research row 51)" as not opened. If they are the same folder, tagging it for Phase
  7 breaches the quarantine (Q-296; Q2 checks Phase 7).
- *The run-modes lines* (A): `DEC-695`'s applied lines, L105 against L109 (REQ-207).
- *Constants carried before the research corrected them* (C): the lake's length, about 250 km at spine L62, L110 and contract CR-2 (spec
  L70), against research FIND-30's about 230 km (L242; Q-56); and the "about 90% retained" split at spine L107, L133 and contract CR-32,
  CR-33, against research FIND-4's measured fall and accumulation "the same size" (L216; Q-61). Nothing rests on either (Q-298).
- *The real station's crew life against the pass's own rule* (B140): contract CR-7 (L122) and research Q-63's recommended line (L610)
  admit access and infrastructure and not crew life; research FIND-12 (L224) uses the station's greens grown in living rooms, FIND-25
  (L237) its winterers' "date out", CONV-1 (L278) its summer supply and stock (Q-297).

**Fix (PROPOSED):** ERR-17 to ERR-20.

#### Q2 — FAIL (A FAIL · B FLAG · C FAIL; B conceded the FAIL in Round 3)

**Holds (all three):** each phase records its canon opened by file and span (P4 L9–23; P5 L12–26; P6 L23–35; P7 L23–84; P8 L12–22).
Shared constants at source, one row hand-checked: the extent row L625 gives 441,378, 44 and 63 km², matching P4 L282 and L317, P6 L242,
P7 L370 and L492, P8 L151; 284,693 + 156,685 = 441,378; 284,693 ÷ 441,378 = 0.64501; §23 against DS-P7 L26 (143,209 ÷ 363,036 = 0.39448;
71,444 ÷ 363,036 = 0.19680; 148,383 ÷ 363,036 = 0.40873; 219,827 ÷ 363,036 = 0.60552; 284,693 + 0.5 × 156,685 = 363,035.5; the robot term
4,483.9, split 3,558.7 and 925.3); altitude 3,488 m (P4 L232) and the −54.8 °C annual mean against DS7 L38; 624.2 hPa in the standard
atmosphere ≈ 3,903 m; the live "about 3.8×" at DS-P7 L34 against P7 L344–346, which uses neither the stale 3.5× nor 18,774. (§23 was checked
against the datasheet that quotes it, not against `16` itself, which is on no Q2 list: B.) Spec-borne constants not on the list (1,260 km;
−31.3 °C and −64.8 °C; the record high −14.0 °C) agree across Q2's phases but were not checked at source (C). `DR-143`'s applied list is
honored in Q2's files for items 1, 2, 3, 4, 5, 6, 7 and 8 (the city's half of the honor, P6 L173–184; the marker, P6 L179, L475; no date;
the national tower by role; enclosure neither declared nor denied, P4 L317; the cold box in words only; the geneticist not an input, P7
L73–76; Census I governs). Rank order: §23 over the first-pass row and over `08` (P7 L282–284); admitted lines over the datasheet's
restatements (P5 L420). Matters binding beyond the city are routed out (siligel keeping, Q-177; coolant's make-up, Q-178; boiling at 624.2
hPa, REQ-133; the gear-catalog hold, Q-172; the conditions-only rule for every city, Q-175).

**The failures:**
- **`DEC-705` applied to some files and not others** (`04` L333; A, C): `DR-143` item 9 holds the city's power source a gap "before any
  energy finding" (as C quotes it); Phase 5 applies it in full (P5 L436, L458; P6 L414; P8 L151), but P4 L188 ("all on one electric
  supply"), P4 L363 and P7 L391–392 (electricity as supplied from elsewhere or received) assume a form or a direction the ruling leaves
  unwritten (A item 24; C).
- **A datasheet restatement used as a finding, against `DEC-687`** (A, single-reader find; B and C agreed): P5 L420 says of the datasheet's
  corridor restatement that "no finding rests on it", but P5 L400 (FIND-P5-33) ends "→ **The first thing every arrival meets is the
  corridor's emptiness**" with no condition, after writing "If the datasheet's restatement holds" earlier in the same finding; P7 L888 writes
  "one highway through an unpeopled corridor" as a fact (A item 25).

**FLAG items:**
- *Negatives named in this repo only* (B, C): Phase 5 names a universe-repo check (P5 L23); Phases 6–8's negatives for faith, holidays and
  factions (P6 L27–29: `National_Holidays.md`, `Ice-Cold_Buddhism_Research/`, `Robot_Religions/`; P7 L51–72: the industry, jobs, factions
  and megacorporation folders) name this repo's paths only. By the gate's rule, a negative counts only with its paths named (REQ-219).
- *Spec L17 cited for 156,685 humans* (B, single-reader find): P7 L568 and P8 L161 cite spec L17, while Phase 4 cites frame DL-4 and Census
  I for the same figure; the spec is not on the list (REQ-217).
- *The closed-population premise still in `16` §23's narrative* (B; C agreed): `DR-127` item 2 and `DR-130` item 1 withdrew it; DS7 L31
  flags it and P7 Q-156 refuses to use it, but §23's narrative still carries it and its stale 3.5× (DS7 L34: the narrative was not
  rewritten). A canon-side lag; no Q2 finding rests on it (REQ-221).

**Fix (PROPOSED):** ERR-52 to ERR-55.

#### Q3 — FAIL (A FAIL · B FLAG · C FLAG; A's FAIL was not withdrawn, so it stands; B's reading is a developer question)

**Holds (all three):** each file names the canon it opened (Phase 9 L12–25; Phase 10 L20–44; Step 5 L25–50 and L1043–1070; Step 6
L19–47). Shared constants: Census I at spec L17 (156,685 / 284,693 / 441,378; B's logged off-list read) = Phase 9 L235 = the extent row
L625; 284,693 ÷ 441,378 = 0.6450; 284,693 ÷ 156,685 = 1.817 (Step 5 DK-1); the height dated before the national tower's completion, about
2688 (`DR-143` item 3) = Phase 9 L235; §23 through the Phase 7 datasheet L26 (an extraction; `16` is on no Q3 list): 143,209 + 71,444 +
148,383 = 363,036; 219,827 ÷ 363,036 = 60.55%; 71,444 ÷ 219,827 = 32.50%; 71,444 ÷ 18,774 = 3.81. The culture sheet's 389,261 is the spec's
own figure from before 2026-10-28, docketed at DK-1 (B). `DR-143` items 1–9 are followed in Q3's files (CAT-1, CAT-77; FIND-P10-2; Phase 9
FIND-P9-5; the national tower by role; robots' cold in words only, Phase 9 L200, Phase 10 L250–252; CAT-76, FIND-P10-14; `DEC-688` at
FIND-P9-7; `DEC-705` at B1 row 22, L1267, "barred by a ruling"). Rank order and RESERVED routing hold (Step 5's tier column; RF-209; Q-256;
Step 6 REQ-202; Q-B1-1; Q-261).

**The failure (A, kept):** **a correction applied to one file and not the other** (`04` L333). The Step 7 datasheet L21 still points Gate 10
to "see `Review_Panel` Tier U content (Step 8)" *(as A quotes it)*, while the gates' quick-reference sheet at its L359 records: "corrected
2026-11-18: the earlier version of this sheet cited "`Corpus_Reference_Sheets/Review_Panel` content", a name no file has" *(as A pasted
it)*. **B's reading, beside it:** the sheet's note is a dated correction, not a ruling, so the finding is real but belongs under Gate 0, and
Gate C would be a FLAG (Q-335). It is one of the datasheet lags this step records as errata, not applied (ERR-87).

**FLAG items:**
- *Project canon at second hand* (B, single-reader find; C agreed): stage B1 opened no file on the Phase 10 list and cites every city line
  "through the stage-A item that already carries it" (L1233–1234); the stage-A carriers checked (CAT-18 L745; CAT-58 L831) do carry those
  lines, so no error is found, but the gate asks for canon against the source (REQ-225).
- *§23's "Canon §15"* (C): Step 5 REQ-181 / RC-14 (L1367–1370): it may be the city's own culture file's §15, which would make the sector
  shares (Phase 4 FIND-P4-1's Science as 65%; RC-17; RC-19) self-originated corroboration, not independent derivation. Open at source
  (Q-262, the pass's own).
- *The first-pass workforce in two source files* (A, single-reader find; B confirmed): the Phase 7 datasheet L27 reads "of 324,452" and L41
  reads "Workforce 324,453". Nothing in the pass rests on it (REQ-226).
- *Census I at its own source* (A): every file read carries 441,378 by citation, and the extent row is a census derivative (REQ-226).
- Runbook §E's four questions are not on Q3's list; they were run as `04` gives them (B; REQ-225).

**Pass verdict: FAIL** (Q1 FAIL · Q2 FAIL · Q3 FAIL).

### Gate F — Frame integrity

**Question** (`04` L342–357): does the pass stay inside its declared type, band, status and temporal frame? Were the excluded spec sections
ever used as input (DS7 L34–35)?

#### Q1 — FAIL (A PASS · B FAIL · C PASS; A and C conceded the FAIL in Round 3)

**Holds (all three):** type Settlement, no Corridor or Installation default (P3 L320); every category declared Patterned or Delegated, none
Uniform (spine L400; P2 L313–324; P3 L312–318); status Living, at the height, no decline read, Census II not used (P2 L307), the seam
written "as what is visible at the height" (P3 L262); the temporal frame: the war only as the frame's end, the "500+ years" clause struck
(contract CR-53), the grid's ~2688 in frame with RF-39 guarding against dating the height from it, real-world dates only in comparables and
site measurements. **The excluded spec lines** (L6, L11, L95, L131–139, L149, L153–161, L171 beyond its readmitted opening clause,
L190–196, L200–204, L208–210, L216, L217 as input, L219, L220, every struck clause) appear only as named exclusions (spine L326; P3 L22;
research L216, L422); P2 FIND-P2-48 and FIND-P2-49 (L287, L289) use spec L30 as provenance only, as CR-23 admits it.

**A watch item, not a failure (A):** research FIND-22 (L234) and P3 FIND-P3-11 and FIND-P3-50 (L130, L236) use the real borehole's history
(the lake reached at about 3,769 m, the water rising and freezing, "decades of summer seasons"). CR-29 struck the drilling as an event and
kept the resulting borehole, equipment and data; the findings frame these as inherited record and physical behavior; they are admissible on
research Q-63's PROVISIONAL line and rest on it (Q-297).

**The failure (B108, B125):** P3 FIND-P3-72 (L317), under *Delegated (deferred by ruling)*, places "the labs, stores, shaft and archive"
in the central scientific district (its bounds open, RF-1). No admitted line places them there. The same file says at FIND-P3-59 (L270):
"Whether the inherited station lies inside the district is not written (RF-1)", and at FIND-P3-57 (L266) that the borehole sits where the
station stood. RF-1 (contract L205) forecloses treating the district as the whole science sector and assigning functions to its edges.

**Fix (PROPOSED):** ERR-21.

#### Q2 — FAIL (A FAIL · B FAIL · C FAIL)

**Holds (all three):** type Settlement (P4 L303: "the type stays Settlement"); Phase 5's admitted text (399 lines) runs longer than Phase
8's (284), and 5c and 5e are primary for an isolated settlement (P5 L26). Band 4: P4 L353–369, P6 L295–302 and P7 L849–868 write the thin
shared layer and the shape, declare nothing Uniform and defer the interior by place (RF-1, RF-3). Status: a living city at its height
(`DR-136` item 6, as P5 L339 cites it). Temporal: post-war lines are refused by name where met (Highways L5's later clauses and Airports
L18's post-war half, P5 L269, L434; institutes L117–119, P4 L18; the outpost's ending, P5 L331; P8 L17); the DS7 L32 person's name is not
carried (P7 L334); the grid's completion, about 2688, is "used for no date" (P5 L513).

**The failure (all three):** P7 L591–593 (FIND-P7-23): "… the corridor's only written stop between cities the waypoint (Phase 5
FIND-P5-29), the subnet's hub about 1,260 km away with no road (spec L9, L159), no coast, …" *(as C pasted it)*. Spec L159 lies inside
the excluded `Character & Culture` section, L153–161 (P6 L34; P8 L21; P7 L938). P5 L369 states the rule this breaks: spec L159 "is excluded
with its section as a culture conclusion (contract CR-47) and is read at Step 5 as a check only". The value is right and stands on spec L9
and L66 (P4 L319; P5 L261; P7 L889); only the citation draws on the excluded line. Cleared excluded-line mentions: P5 L292, L369, L486,
L492, L523; P6 L34, L154, L314 (a clause dropped because it rested on an excluded line), L517; P7 L81, L938; P8 L21, L301.

**FLAG items:**
- *The outpost's power and the date of the height* (A; (c)): P5 L290 (FIND-P5-14) writes that the outpost "ran on residual overflow from
  the national tower's regulated grid"; P5 L436 records that the grid came fully online at the national tower's completion, about 2688;
  `DR-143` item 3 dates the governing census figure to before ~2688 (±~20). No date is drawn (RF-18), so no fact leaks directly, but whether
  that grid's surplus existed at the city's height is undecided, and P7 L398–399, L443 and L465 lean on it (Q-315).
- *Spec L221* (B): P8 FIND-P8-32 cites spec L221; whether it lies in an excluded section cannot be checked from the list (REQ-218).
- *Band variance not in Phase 5's or Phase 8's admitted spans* (C): whether the phase spine requires it there is unchecked (REQ-220).

**Fix (PROPOSED):** ERR-56.

#### Q3 — FAIL (A FAIL · B FAIL · C FAIL)

**Holds (all three):** type Settlement, not Installation (Phase 9 L219; Phase 4 L303); Band 4, Patterned and Delegated, nothing Uniform
(Phase 9 FIND-P9-10, L260; Phase 10 L960–962); status the undated height (`DEC-698`), the culture sheet's post-war status set aside (RL-4,
Q-265); post-war facts kept out (Phase 4 L18; RL-51, RL-60 OUT OF FRAME); real-world dates in Phase 10 (2023–2026) are source dates, never
in-world. Phase 9 read the excluded section and rests nothing on it (L23); Step 5 stage B opened no spec line (L1066); Step 6 opened none
(L43; its §8 cells rest on spec L9 and L66).

**The failure: Phase 10 used excluded spec lines as input** (all three; raw, from the pass's own lines as C pasted them):
- spec **L135** (under the excluded Gameplay Notes): Phase 10 L950 "about 1,260 km away overland with no road (spec L135; ...)" and L986
  "(spec L9, L135, L169; ...)". Step 5 RC-77.
- spec **L155** (`Character & Culture`): Phase 10 L1653 (row 84, "the pole the city approaches (spec L155)"), L1696–1697 ("The city's
  location approaches the continent's pole of inaccessibility (spec L155)"), L1917 (Q-B2-3) and stage A's Q-217 (L1214). Step 5 RC-74.
- spec **L157** (`Character & Culture`): Phase 10 L1810, CAT-B2-8's only city line. Step 5 RC-75.
- spec **L171 past its opening clause**: Phase 10 L1688–1690, stage B2's extension of CAT-11 (the outpost "stopped for good when that
  supply ended"), a post-height fact and its wartime cause. Step 5 RC-78.
- spec **L167's struck vision sentence** (the genetics wording): Phase 10 CAT-6 L709, CAT-15 L733–734 ("spec L167, its genetics-floors
  sentence only"), FIND-P10-7 L911–914, CAT-76 L862, and B1's extension of CAT-6 L1380–1382. Step 5 RC-72, REQ-169.
Stage B2's writer opened the spec at L124–180 (catalog L1579, L1590), a range crossing L153–161 (A). **Step 5 caught every case**
(FIND-S5-8, L813–818; REQ-167, REQ-168, REQ-169) and proposed dockets; **none is applied, so the catalog's text still rests on them.**
Phase 10 L42–44's claim that nothing rests on the excluded lines is the Gate 0 face of the same failure.

**Fix (PROPOSED):** ERR-76 (the status claim), ERR-88 to ERR-92.

**Pass verdict: FAIL** (Q1 FAIL · Q2 FAIL · Q3 FAIL).

### Gate I — Inheritance classification

**Question** (`04` L359–387): is every element correctly classed (determined · inflected · originated · aggregated)? Originated
outnumbering Inflected by more than about 3:1 is a stop-and-recheck flag.

#### Q1 — PASS (A PASS · B PASS · C PASS)

The Q1 files class nothing explicitly (the audit sends classification to the step whose text names it, audit Q-29 L233; frame PV-4 leaves
one class open), so each reader classed the named institutions, customs and forms from the files' own wording. Three counts, all under the
flag:
- A: Determined 9 · Inflected 5 · Aggregated 1 · Originated 10 (7 canon or ruling, 3 the pass's own); **Originated:Inflected 2:1.** A
  notes that the four classes do not name a predecessor site (the shaft, taken up from the site, classed Originated).
- B: Determined 10 · Inflected 5 · Aggregated 1 · Originated 6, one unclassable (the cold-record marker, its form Phase 10's);
  **about 1.2:1.**
- C: Determined 12 · Inflected 6 · Originated 6 · Aggregated 0; **1:1.**
The readers differ on single calls (the national language's supporting tier: Inflected for A and C, Aggregated for B; perpetual induction:
Originated for A, Inflected for B and C); no call changes the verdict. No local variant of a parent-determined thing (currency, calendar,
law) is produced (frame PV-2). Everything classed Originated was taken to Gate 6.

#### Q2 — PASS (A PASS · B PASS · C PASS)

The phases carry no class column in their admitted spans (except P8's native and transplanted layers), so each reader classed the named
institutions and customs:
- A: Originated 4 · Inflected 8 (or 4 against 7 if the turn, the debt and worth are one); **0.5:1.** Unclassable: the institution that
  keeps the clock (its parent position unwritten, REQ-84, Q-111).
- B: Originated 7 · Inflected 14, with Determined and Aggregated rows listed; **0.5:1.** The same clock item unclassable.
- C: Determined 10 · Inflected 8 · Originated 6 · Aggregated 3; **0.75:1.**
**One split settled in Round 3:** B classed the turn of instruction Originated; A and C class it Inflected, from the national mentor and
mentee bond (RP L418, cited at P4 L200, P6 L238, P7 L631–632); B conceded (a). A adds that the pass nowhere classes the forward debt, which
is better classed Inflected on the same ground; claiming origination for it would be Gate I's second failure, a risk and not yet an act
(Q-307). No local climate, currency or calendar is invented.

#### Q3 — FLAG (A FLAG · B FLAG · C FLAG); the ratio passes everywhere

**Counts:** Phase 9's own dual tags, mapped (directly inherited → determined; adapted → inflected; genuinely emergent → originated): 17 ·
21 · 7 (L368), **Originated:Inflected 7:21 = 1:3** (all three). Phase 10, classed by each reader: A 9 originated against 6 inflected
(**1.5:1**); B 4 against 6 among its fifteen findings; C 10 against 8 (**1.25:1**). Step 5's FIND-S5-1 to FIND-S5-10 (B): aggregated 6,
inflected 3, method 1. No local variant of a parent-determined thing is written (Step 5 PA-2).

**Three flags (all kept; no contradiction among them):**
- **FIND-P9-35, the order of arrival, tagged "genuinely emergent" (L340)** (A; B agreed): it rests on a national institution, cited in the
  finding itself ("Mentor and mentee bonds are a genuine robot institution, maker and made is not (physiology L418)", as A quotes it), and
  on Phase 2's perpetual induction: the failure `04` L367–368 names. Proposed: class it inflected (C (c); Q-336). The same mechanism Q2
  classed inflected (Q-307).
- **The national relations baseline** (Phase 9 FIND-P9-34; frame PV-4; Q-184: Determined or Inflected) (B, C): already a developer
  question.
- **The shared night here** (C; B agreed): national canon (Phase 4 FIND-P4-6) against the city's T2 vision (Step 5 RL-42; Q-255):
  determined, or inflected out of existence, is the developer's.

**Pass verdict: FLAG** (Q1 PASS · Q2 PASS · Q3 FLAG).

### Gate P — Parent reconciliation

**N/A.** It runs on a parent's pass; this city has no written children. Its one named sub-location, the central scientific district, has
no pass of its own (frame DL-11, L101), and decomposition is deferred by ruling (RF-3). All readers who recorded it recorded N/A.

### Gate G — Generator honesty (assigned to Q1 only)

**Question** (`04` L405–419): at least three independent generators, each run to a full profile before comparison; conflicts mined, not
smoothed; nulls recorded; deficits researched after the profile; the Unrecognized Instrument run after the profile. *(Q2's and Q3's "not
assigned" is not a verdict.)*

#### Q1 — FLAG (A PASS with a caveat · B FLAG, withdrawn in Round 3 · C FLAG)

**Holds (all three):** three generators, G2 · G7 · G8 (spine L74), chosen under `02` §5.1's own sentence naming physical constraint,
composition and inspiration research as the independent kind (spine L76); eight shared roots named and handled (L84–92); two conflicts in
twelve cells, each resolved by the both-are-true test into two objects (L218–224), contract Q-9's conflict discharged (L227), the silent
cell put to the developer (Q-44); nulls recorded (L70); Step 3's targets follow the profile (research L31); the Unrecognized Instrument run
after the research (spine L401; research L294).

**The caveat and the FLAG:**
- *Profile before comparison* (A's caveat; B's FLAG on spine L173, "in this city leaving is hard (G2)"): G7's *adjusted* clauses were
  written knowing G2 (L150, L158, L159, L173). A shows the comparison's G7 cells (L209–212) rest on the picks' *unadjusted* features, so
  independence holds at the cell level; **B withdrew its FLAG in Round 3 in favor of A's reading.** C adds that the merged profiles carry
  two forward references into the comparison (L159, L181), so profile-before-comparison is not verifiable from the merge; recorded, not
  failed.
- *The picks' provenance* (C, kept; settled as (c)): G7 may share a root with excluded material, the struck genetics line (spine L92,
  RF-43, REQ-36), still open after Step 3 (research REQ-53, Q-65). If the picks were chosen from that line, G7 is not independent of an
  excluded input (Q-299).

**Pass verdict: FLAG** (Gate G ran in Q1 only).

### The station-builder scan (assertions and denials)

**Question** (runbook L2944; `DR-19`): a sentence saying the station's builder does *not* explain a form is the same violation as one
saying it does. Every hit read in context.

#### Q1 — FAIL (A FAIL · B FAIL · C FAIL)

**Method (all three):** by reading every mention of the station's builder, operator or operators in context (no search command was
allowed); C verified the method on the one hit the pass had marked itself (P2 RF-87, L392). **No assertion found.**

**Denials inside findings, raw text:**

| File:line | Raw text | Readers |
|---|---|---|
| P2 L283 (FIND-P2-46) | "**Not a characterizing absence; no cause is drawn, and the station is never one:** the law exists so that a city is characterized by who lives there, not by whose station it occupies (RB L2136), and a sentence whose meaning would change if the station-builder were swapped fails the self-check (NNS L7)." | A, B, C: FAIL |
| P2 L392 (RF-87, foreclose column) and P2 L524 (Q-75's recommended answer) | "any cause, the station above all (NNS L7)"; "and never the station as a cause (`DR-19`; NNS L7)" | A and B: FAIL; C cleared them in Round 1 and gave way on Q-75 in Round 3 |
| P2 L210 (FIND-P2-23) | "and the station passed through operators whose identity is irrelevant (NNS L13, L15; frame DL-3)" | A, C: FAIL; B borderline, conceding C under a strict reading |
| P2 L195 (FIND-P2-17) | "with no national-origin match to the station's former operator required (TD L55)" | A, C: FAIL; B cleared it as a swap-invariant treaty article; (c) |
| spine L187 | "**the language of the inherited station records is in no listed line, and it must not be inferred from the station's operators** (`DR-19`)" | C: FAIL; A and B borderline; B conceded C under a strict reading |
| P3 L274 (FIND-P3-61) | "the records' language is not inferred from the station's operators (spine RF-46)" | C: FAIL; A and B borderline |
| spine L109 (G2 strength 5) | "its operator is a coordinate and is not used" | C: FAIL; A and B cleared it; (c) |

By the merge rule, a FAIL not withdrawn stands; the reach of runbook L2944 (a treaty article paraphrased inside a finding; a guard on
inference; an operator named only to be set aside) is put to the developer (Q-300), and the form of the FIND-P2-46 fix (A and B rewrite
it flat; C withdraws the finding) is a second question (Q-301). In every corrected text the core state is written by role: *the core state
of one founder's predecessor nation*.

**Cleared (input dispositions and foreclosure columns, not findings about the place):** contract L24, CR-11 (L135), CR-30 (L154), CR-43
(L167); frame DL-2 (L74, about the site) and DL-3 (L82, about people); audit item 12 (L114); research FACT-2 and FIND-1 (L92, L213, the
operator's values as a data source), FACT-13 (L103, "the operator not used (`DR-19`)"), §8 OMITTED (L407); spine RF-46 (L535) and P2 RF-76
(L381) foreclose columns; P2 FIND-P2-44 (L279) and P3 L274's mention of the station's *personnel and papers* (`DR-25`), not its builder.

**Outside the pass files, on the list:** DS-P7 L35 states that the station's character, naming the builder's nationality, "is never a
reason" (a denial in a datasheet row) (A, single-reader find; REQ-213). DS12 L34 is under Gate C (ERR-19).

**Fix (PROPOSED):** ERR-22 to ERR-27.

#### Q2 — FAIL (A FAIL · B FAIL · C FLAG; C conceded the FAIL in Round 3)

**No assertion found** (all three, by reading). **The failure (A, B; C gave way): a denial inside a finding.** P6 L217–218 (FIND-P6-5):
"**Narrowed in Round 3:** the real station's record-writers are not made creditors of the city's debt, and no debt structure or peer-free
answer rests on them" *(as C pasted it)*. This denies that the station's people explain a city form (the debt), the shape runbook L2944
names; the same finding then states the positive ground (L219–220). Its echo at P6 L488–489 (FIND-P6-32): "Here *paper* names the founding's
condition only, never a creditor (split 3)." (B.)

**Put to the developer (all three, (c)):** method statements inside findings that name the station's operator or people only to set them
aside: P5 L279 (FIND-P5-11): "Under `DR-19` both are a coordinate only, never a cause; no relation runs through the station, and **nothing in
this phase is drawn from its operator or its life.**"; P8 L229 (FIND-P8-30): "The language of the inherited station records is in no listed
line **and is not inferred from the station's operators** (spine RF-46)."; P6 L380 (FIND-P6-21 (d)), the real station's scientists honored
by name only (B). And B's world-clock line (P7 L485, with P4 L184), which B also counts here, may be site history rather than the builder
((c)); it is an erratum under Gate 3 either way (Q-300).

**Cleared:** the station's journals, logs, manuals and the inherited borehole as the founders' inheritance (`DR-25`; P4 L295; P6 L208–213;
P7 L616–623; P8 L193); the honor's two halves as ruled (P6 L151, L173–177); the 1983 record as an inherited record only (P6 L365–367,
L475); P7 L367–369 ("The real site's history is never the signature instance", a method guard naming no builder); P7 L66 (bookkeeping);
P7 L961 and P8 L323 (lists of what was shed); P4 L232's crews at the real site (a physiological comparable).

**Outside the pass, on the list (A; B agreed):** DS-P7 L35 and L56 name the station builder's nationality in their *not carried* notes, to
deny they ground anything; the name is not reproduced here (REQ-213).

**Fix (PROPOSED):** ERR-57 (and ERR-49 for the world clock).

#### Q3 — FAIL (A FAIL · B FAIL · C FLAG; C's FLAG gives way)

**No assertion found** (all three, by reading; a reading scan is not exhaustive, C). **Denials in findings, a catalog item and a record**
(the operator's name not reproduced):

| File:line | Text | Readers |
|---|---|---|
| Phase 9 L212 | the lens table's robot row, column "What it is never anchored in": "the station's operator or nation (`DR-19`);" | A, B FAIL; C lists it as a denial inside a finding's table |
| Phase 10 L790–791 (CAT-38) | "the records' language is not inferred from the station's operators (spine RF-46) [B]" | A, B FAIL; C lists it as a denial inside a catalog item |
| Step 6 L299 | substitute 3's divergence cell: "the station is a coordinate and a paper inheritance, never the population's origin" | A FAIL; B FLAG with a rewrite; C lists it as a denial in a record |

**Put to the developer:**
- *Phase 9 L202*, a bar in *What waits*: "No population is anchored on the station's operator or nation; founders come only from the
  Founding Register" *(as A pasted it)*. B rewrites it to the positive rule; A and C hold it as a method guard ((c); Q-337).
- *Step 5 DK-3's "keep"* (L1126 RL-12; L1389 DK-3): stage B proposes keeping, in the culture sheet, the sentence that the station operators'
  nation has no representation in any tier. A and C would strike it (a composition sentence whose only content is the builder's nation's
  absence); B clears it as a census fact ((c); Q-338).
- *Step 5 RL-31* (L1145): the culture sheet's "no surviving culinary tradition from the station operators' nation" is a denial-form claim,
  handed to the CST without marking its form (B, single-reader find; C agreed) (REQ-227).

**Cleared:** Phase 10 L351 ("the real site is researched as a site, never its operator (`DR-19`)", a research rule); L1584; CAT-1 and CAT-77
(the real station's scientists as a naming fact only); FIND-P10-2 (the station's papers as an inherited record); CAT-12, FIND-P10-8; Step 5
RL-27, DK-12, Q-260 (method guards in dockets and a question); RC-46 (the runway a coordinate's physical fact).

**Fix (PROPOSED):** ERR-93 to ERR-95.

**Pass verdict: FAIL** (Q1 FAIL · Q2 FAIL · Q3 FAIL).

### The generator-vocabulary sweep

**Question:** the orchestrator's mechanical sweep (file:line:term, word-boundary, case-insensitive; 768 hits over every pass file through
Step 5) inspected in context; a hit is not a defect; the real ones listed with a plain rewrite.

#### Q1 — FAIL, wording only (A FAIL · B FAIL · C FAIL)

**Raw output, excerpted (54 lines omitted: the header, the contract, frame, audit and spine blocks, whose hits inside the admitted spans are
all method sections, generator tables, receipts or citations, and the other sub-units' files and the total):**

```
## 03_Research.md — 20 hits

87:G2, 220:standing cost, 222:standing cost, 223:standing cost, 227:standing cost, 229:standing cost, 243:G7, 244:G3, 301:standing cost, 301:standing cost, 357:G8, 357:G8, 366:G7, 371:G7, 397:G8, 398:G3, 398:G8, 447:G7, 468:G3, 468:G5

## 04_Phase_02_Composition_and_Arrival.md — 31 hits

26:G1, 40:G4, 49:G4, 49:G4, 49:G3, 49:G3, 49:G8, 52:G4, 52:G3, 56:G8, 57:G3, 57:G8, 214:G7, 234:standing cost, 261:G8, 261:standing cost, 271:G8, 332:standing cost, 336:G8, 336:G4, 336:G6, 336:G2, 336:G3, 336:G5, 336:G7, 336:G1, 342:G3, 342:G4, 343:standing cost, 396:standing cost, 450:standing cost

## 04_Phase_03_Surface_and_Texture.md — 45 hits

27:G1, 33:G3, 33:G4, 33:G3, 41:G3, 44:G3, 45:G3, 46:G3, 47:G3, 71:G4, 71:G3, 72:G3, 72:G8, 73:G3, 74:G3, 74:G5, 75:G3, 77:G3, 77:G5, 134:G2, 134:quadrants, 152:standing cost, 154:standing cost, 182:standing cost, 188:standing cost, 188:standing cost, 206:standing cost, 228:G3, 230:G7, 264:standing cost, 264:standing cost, 302:G8, 302:standing cost, 332:G2, 332:G3, 332:standing cost, 332:G4, 332:G5, 332:G7, 332:G8, 332:G1, 332:G6, 338:G3, 391:standing cost, 443:standing cost
```

**Not inspected** (outside the admitted spans, in bookkeeping sections the lists cut): contract L309, L313, L327, L329–331, L342; frame
L291–293, L367, L375, L390; audit L190, L267; spine L18–45, L433–437, L616–695; research L357, L366, L371; P2 L40–57, L450; P3 L33–77, L443.

**Legitimate:** every contract, frame and audit hit read; the spine's hits inside its spans (the generator method is the spine's content;
"(G7 adjusted)" and "(G4, read beside)" at L366 and L392 are labels); research L87, L220 ("Spine standing cost 7", a pointer), L227, L229,
L243, L244, L301, L397, L398, L447, L468; P2 L26, L261, L271, L336, L342; P3 L27, L152, L154, L182, L206, L302, L332, L338, L391.

**Real hits: method words carrying meaning in finding prose** (A and C; B cleared six of them in Round 1 and conceded (a) in Round 3): research
L222 (FIND-10), research L223 (FIND-11), P2 L214 (FIND-P2-25), P2 L234 (FIND-P2-33's title, echoed at L343 and L396), P2 L332 (FIND-P2-68),
P3 L134 (FIND-P3-13), P3 L188 (FIND-P3-31), P3 L228 (FIND-P3-46), P3 L230 (FIND-P3-47), P3 L264 (FIND-P3-56). Their plain rewrites are in
§5.

**Fix (PROPOSED):** ERR-28 to ERR-37.

#### Q2 — FAIL, wording only (A FAIL · B FAIL · C FAIL)

**Raw output, excerpted (46 lines omitted: the hits outside Q2's files, sweep L1–32 and L52–65).** *(Reader C headed this block "Raw
output, whole"; it is an excerpt of the sweep's L33–51, and is labeled here as one.)*

```
## 04_Phase_04_Ordinary_Life.md — 25 hits

21:G1, 46:standing cost, 60:G3, 93:standing cost, 168:standing cost, 188:standing cost, 190:G7, 198:G7, 200:G8, 200:standing cost, 220:standing cost, 246:standing cost, 262:standing cost, 262:standing cost, 317:standing cost, 359:standing cost, 387:G2, 387:G3, 387:G4, 387:G5, 387:G6, 387:G7, 387:G8, 387:G1, 587:G6

## 04_Phase_05_Relation_and_Geometry.md — 21 hits

25:G1, 94:G5, 94:G5, 195:G3, 195:G5, 205:G3, 205:G5, 409:G8, 409:standing cost, 416:standing cost, 422:standing cost, 442:standing cost, 513:G5, 513:G2, 513:G3, 513:G4, 513:G6, 513:G7, 513:G8, 513:G1, 667:standing cost

## 04_Phase_06_Meaning.md — 16 hits

35:G1, 78:G8, 156:G8, 156:standing cost, 187:standing cost, 188:standing cost, 189:G8, 190:standing cost, 508:G2, 508:G3, 508:G4, 508:G5, 508:G6, 508:G7, 508:G8, 508:G1

## 04_Phase_07_Order.md — 26 hits

78:G1, 107:G7, 107:G7, 114:G7, 155:G8, 155:standing cost, 163:G7, 235:G7, 366:G7, 438:G7, 598:standing cost, 623:G4, 628:G8, 628:standing cost, 650:standing cost, 655:G8, 695:standing cost, 697:G7, 903:G2, 905:G3, 910:G4, 912:G5, 915:G6, 918:G7, 922:G8, 925:G1

## 04_Phase_08_Making.md — 14 hits

22:G1, 179:standing cost, 199:standing cost, 203:standing cost, 215:standing cost, 293:G2, 293:standing cost, 293:G3, 293:G4, 293:G5, 293:G7, 293:G8, 293:G6, 293:G1
```

102 hits in Q2's files. **Not inspected** (19, outside the admitted spans): P4 L46, L60, L93, L587; P5 L94 (2), L195 (2), L205 (2), L667;
P6 L78; P7 L107 (2), L114, L155 (2), L163, L235. **Legitimate** (citations, method lines, generators-used lines, the "(G1, Phase 10)"
refusal tags, a bare "(G4.)" tag): P4 L21, L168, L188, L198, L200 (2), L220, L262 (its citation half), L359, L387 (8); P5 L25, L409 (2),
L513 (8); P6 L35, L156 (2), L188, L189, L190, L508 (8); P7 L78, L366, L438, L623, L628 (2), L655, L695, L697, L903–925; P8 L22, L293 (9).

**Real hits: method words carrying meaning in finding prose** (all three; fourteen from the sweep, plus two it missed): P4 L190
(FIND-P4-8), L246 (FIND-P4-32), L262 (FIND-P4-38's heading), L317 (FIND-P4-50); P5 L367 (missed by the sweep: a plural on the first word,
B), L416 (FIND-P5-36), L422 (FIND-P5-39), L442 (FIND-P5-46); P6 L187 (FIND-P6-4); P7 L576–577 (FIND-P7-22; missed by the sweep: a line
wrap, all three), L598 (FIND-P7-23), L650 (FIND-P7-28); P8 L179 (FIND-P8-13), L199 (the dress axis line), L203 (FIND-P8-21), L215
(FIND-P8-25). Plain rewrites in §3. The three readers' wordings differ, not their substance (B, Round 3).

**Fix (PROPOSED):** ERR-58 to ERR-73.

#### Q3 — FLAG (A FLAG · B FLAG · C FLAG)

**Raw output, excerpted (54 lines omitted: the sweep's L1–52 and L64–65, the header, the twelve other files' sections and the total; the
gate reader checks hits in its own files only; Phase 4's section is Q2's). Step 6 has no section: the sweep stops at Step 5.** *(As A and C
pasted it.)*

```
## 04_Phase_09_Populations.md — 19 hits

20:G1, 115:G8, 135:G8, 138:G3, 138:G8, 141:G8, 142:G3, 142:G8, 340:G8, 340:standing cost, 344:standing cost, 421:G8, 421:G2, 421:G3, 421:G4, 421:G5, 421:G6, 421:G7, 421:G1

## 04_Phase_10_Catalog.md — 53 hits

63:G1, 66:G1, 68:G1, 68:G1, 69:G1, 70:G1, 72:G1, 78:G1, 78:G1, 79:G1, 79:G1, 80:G1, 82:G1, 85:G1, 88:G1, 95:G1, 105:G1, 107:G1, 109:G1, 116:G1, 118:G1, 126:G1, 132:G1, 134:G1, 136:G1, 140:G1, 144:G1, 149:G1, 163:G7, 164:G6, 165:G2, 166:G7, 167:G7, 168:G7, 169:G1, 171:G3, 172:G6, 173:G3, 173:G4, 175:G5, 176:G5, 177:G2, 178:G2, 182:G2, 982:G1, 982:G2, 984:G3, 985:G4, 985:G5, 986:G6, 987:G7, 988:G8, 1173:G1

## 05_Reconciliation.md — 52 hits

64:G2, 64:G7, 64:G8, 69:G7, 70:G2, 70:G8, 326:G7, 356:G5, 445:G7, 526:G1, 527:G1, 586:G2, 586:G5, 586:G8, 586:G2, 586:G7, 586:G8, 594:G5, 604:G2, 604:G7, 604:G8, 667:G1, 667:G1, 697:STANDING COST, 698:standing cost, 702:standing cost, 703:standing cost, 705:standing cost, 709:standing cost, 710:standing cost, 711:standing cost, 712:standing cost, 714:standing cost, 715:standing cost, 716:standing cost, 719:standing cost, 720:standing cost, 721:standing cost, 722:standing cost, 723:grudging tolerance, 724:standing cost, 725:standing cost, 727:standing cost, 728:standing cost, 729:standing cost, 757:G8, 837:G7, 853:quadrant, 853:standing cost, 853:grudging tolerance, 863:G7, 891:G5
```

**Not inspected** (outside the admitted spans): Phase 9 L115, L135, L138, L141, L142; Phase 10 L63–182 (44 hits) and L1173 (REQ-206).
**Legitimate (all three):** Phase 9 L20 (a refusal's pointer, "the symbol files (G1, Phase 10)"), L340 and L344 (bracketed citations),
L421 and Phase 10 L982–988 (generators-used lines); Step 5 L64–70 (generator against generator, method by definition), L326, L356, L757,
L891 (citations of a spine row), L445, L837, L863 (a "(G7, PROVISIONAL)" provenance tag), L526–527, L586, L594, L604, L667 (method rows on
the generator set), L697–729 (the translation table itself), L853 (REQ-159's list). Step 6, by reading: L58's *Balanced* and address
labels sit in a method column (Q-275), and the substitute-4 table (L305–316) is the method itself.

**No real generator word among the mechanical hits in Q3's spans. Real hits the instrument cannot see, found by reading:** Phase 9 L344
("unspeakable") and L346 ("a deficit", "unspeakable"), already Step 5's T-35 and T-36 (all three); and two new ones (B, single-reader find;
A and C agreed): Phase 9 L396, the swap-test row label "FIND-P9-38, the minority's unspeakable cost", and Phase 9 L462, RF-181, "The
minority's chief cost unspeakable to the majority". All four wait on Q-254 (the word *unspeakable*) and go to the append-only translation
docket (REQ-173); their plain rewrites are in §5.

**Pass verdict: FAIL** (Q1 FAIL · Q2 FAIL · Q3 FLAG), wording only.

---

## 3 · Errata (PROPOSED; never applied; these enter the Review Panel's brief as facts, runbook L2983)

### Q1's files

**Gate 0**
- **ERR-1 · P3 L11 against FIND-P3-34 (L198)** (B121). Corrected: tag FIND-P3-34 `[treaty draft]`, add it to the Generators-used line
  (L332), and amend L11 to "One finding, FIND-P3-34, rests in part on a treaty-draft article, through Phase 2 RF-86." Or drop the observers
  clause from FIND-P3-34.
- **ERR-2 · P2 L11 against FIND-P2-19 (L201) and FIND-P2-22 (L208)** (B122). Corrected: tag both `[treaty draft]` and add them to L336's
  list; or, where the no-return fact is all that is needed, cite brief §4 item 5 (`DR-127` item 2) alone and drop the TD citation.

**Gate 2**
- **ERR-3 · research L229 (FIND-17)** (A 1). Corrected: "→ For the human body, through about 123 days of midnight sun, rest needs **dark**
  at the place of rest as much as heat; no such need is written for the robot majority, whose rest night is a charge night not bound to the
  dark (spine L406) → for humans the manufactured day is two costs: heat and light in winter, heat and darkness in summer."
- **ERR-4 · research L263 (§4, the D-3 row)** (A 2). Corrected: "…rest needs a rule, and for the human body darkness at the place of rest
  (FIND-17, FIND-18)…"
- **ERR-5 · research L461 (RF-55)** (A 3). Corrected: "For the human body, rest needs darkness in the midnight-sun months as well as heat
  (FIND-17)".
- **ERR-6 · P2 L252 (FIND-P2-38, bullet 2)** (A 4). Corrected: "- **Rest is located:** rest and charge happen only in heated, powered
  space; for the human body, about 123 days of midnight sun add a need for dark at the place of rest (spine §8f; research FIND-17; scoped
  as P3 FIND-P3-30 scopes it); no such need is written for robots."
- **ERR-7 · spine L392 (§8e, "What it permits but punishes")** (B141). Corrected: tag both readings "research population only (G7
  adjusted)", or move them beside the four answers; they are not answers for all 441,378.

**Gate 9**
- **ERR-8 · research L237 (FIND-25)** (A 5; B124 for the heading). Heading corrected: "**A place whose people cannot go back keeps what the
  comparables send away.**" Ending corrected: "…and if its losing side stays, the city holds it, working or not; whether anyone left the
  city for elsewhere in the nation is unwritten (RF-30)."
- **ERR-9 · research L478 (RF-72)** (A 6). Corrected: "Whoever the order does not fit and who stays is held by the city (FIND-25); whether
  any leave for elsewhere in the nation is unwritten (RF-30)".
- **ERR-10 · spine L229, the spine sentence** (B124). Corrected: "… and no departure of those who came is written; …" in place of "and
  those who came have stayed".
- **ERR-11 · P2 L232 (FIND-P2-32)** (A 7). Corrected: "Every route in from Upper Earth is one-way (brief §4 item 5); no departure from the
  city is written (RF-30), so the files give the population no renewal by people leaving, and whatever a place does through turnover, this
  one, as written, does with the people it has…"
- **ERR-12 · P2 L406 (SH-10)** (A 8). Corrected: "…so whoever came and did not fit has no return to Upper Earth, no written exit from the
  city (RF-30) and no written place…"
- **ERR-13 · P3 L198 (FIND-P3-34)** (A 9). Corrected: "…so her first impression is of a place she cannot leave for Upper Earth; whether
  she stays in the city is not written (RF-30)…"
- **ERR-14 · P3 L252 (FIND-P3-53)** (A 10; B124). Corrected: "→ **The last need meets the population's own condition as the files write
  it:** no human arrival can return to Upper Earth (brief §4 item 5) and no departure from the city is written (RF-30), so nothing in the
  files takes holders away from the archive by leaving. PROPOSED."
- **ERR-15 · P3 L302 (FIND-P3-69, item 2)** (A 11; B124). Corrected: "(2) **no term:** arrivals cannot go back to Upper Earth and no
  departure from the city is written (brief §4 item 5; RF-30; Phase 2 FIND-P2-32), so the files write no loss of understanding by people
  leaving;"
- **ERR-16 · P3 L304 (FIND-P3-70, second order) and RF-104 (L384)** (A 12; B124). Corrected: "…because the understanding lives in people,
  and the files write no arrival with a term and no departure (Phase 2 FIND-P2-32; RF-30), **the files write no loss to the archive by
  people leaving;** as written, its understanding is held by those who stay." RF-104's title: "The archive's understanding, as the files
  write it, is held by people with no written departure".

**Gate C**
- **ERR-17 · DS12 L35** (A 17; B127; C201). Corrected end: "…"The name was kept" (spec L149) is EXCLUDED (contract CR-45; `DR-143` item
  10, `DEC-691`), read as *the central district keeps the name*." Dated, in place, moving no cited line (audit REQ-24(a)).
- **ERR-18 · DS12 L17 and L26** (A 18). L17 corrected: "cross-verified against the READER record — exact match **for the twelve monthly
  means and the annual mean only**; the record holds no other column (spine §8a)". L26 to carry the monthly table, not a pointer (contract
  REQ-7; spine REQ-35).
- **ERR-19 · DS12 L34** (A 19). Corrected: the station's operation from 1957 and its succession of operators are a coordinate only
  (contract CR-43; `DR-19`, `DR-24`); the clause naming the builder's nationality is struck; the rest of the line (the preserved journals,
  logs and manuals) stands (audit REQ-24(d)).
- **ERR-20 · DS2 L16** (C202). Corrected: the stale deferral clause removed, as retired at census L440 (`DR-35`); the no-representation
  verdict worded for the core state of one founder's predecessor nation only, as P2 REQ-62 (L415) gives it. Dated, in place, moving no
  cited line.

**Gate F**
- **ERR-21 · P3 L317 (FIND-P3-72)** (B125). Corrected: "**Delegated (deferred by ruling):** texture by place inside the city, the central
  scientific district included (its bounds and contents open, RF-1), and every interior; where the labs, stores, shaft and archive sit is
  not written; the decomposition is not performed."

**The station-builder scan**
- **ERR-22 · P2 L283 (FIND-P2-46), with RF-87 (L392) and Q-75 (L524)** (A 15–16; B123; C207). Corrected (A's and B's flat form;
  C's withdrawal is the alternative put at Q-301): "**FIND-P2-46 · The core state of one founder's predecessor nation, as a founding stock
  and as a row.** Not a founder (Register L63; DS2 L21) and no row at any tier (spec L32–58); the founding stock is a successor state, not
  the core state (spec L147), at 3.68%. Stated flatly, once; nothing is drawn from it (RF-87; Q-75)." The sentence beginning "Not a
  characterizing absence" is struck. RF-87's foreclosure to read "any cause or characterization drawn from it". Q-75's recommended answer:
  "Intended as written; record it once as a fact of the Register and the table and draw nothing from it (`DR-19`; NNS L7); confirm at the
  post-ULM census review".
- **ERR-23 · P2 L210 (FIND-P2-23)** (A 14; C206). Strike ", and the station passed through operators whose identity is irrelevant". The
  sentence then reads: "No population came with the place. The real station's personnel could not be alive, present or personally
  interacting with the founding exiles (NNS L13, L15; frame DL-3); "no living scientific legacy or institutional culture survived" the chain
  of handoffs (spec L145)."
- **ERR-24 · P2 L195 (FIND-P2-17)** (A 13; C205; subject to Q-300). Strike ", with no national-origin match to the station's former
  operator required (TD L55)". The sentence then reads: "…"each population being assigned to a station" by arrangement (TD L54, Art.
  II.3.2); the Register supplies the content of the arrangement here: founders on time-zone proximity (Register L63) (Q-69)."
- **ERR-25 · spine L187** (C204; subject to Q-300). Corrected: "the language of the inherited station records is in no listed line
  (RF-46)."
- **ERR-26 · P3 L274 (FIND-P3-61)** (C208; subject to Q-300). Corrected: "That seam is not visible at the surface; the records' language is
  in no listed line (spine RF-46)."
- **ERR-27 · spine L109 (G2 strength 5)** (C203; subject to Q-300). Corrected: "A flat ice surface already serves aircraft at the real
  site: a skiway with an ice surface (stations L67; infrastructure only, `DR-24`)." (the operator clause removed)

**The generator-vocabulary sweep** (plain language; low stakes; where A's and C's wordings differ, A's is given first and C's after the
slash)
- **ERR-28 · research L222 (FIND-10):** "is a standing cost only while it is kept filled and watched" → "costs upkeep without a pause for as
  long as it is kept filled and watched" / "costs without pause, and stays open only while it is kept filled and watched".
- **ERR-29 · research L223 (FIND-11):** "where the cold's standing cost already falls" → "where the cold's never-ending heating cost already
  falls".
- **ERR-30 · P2 L214 (FIND-P2-25):** "(spine RF-47, a G7 adjustment, not canon)" → "(spine RF-47, an adjustment from the inspiration picks,
  not canon)".
- **ERR-31 · P2 L234 (FIND-P2-33's title), with its echoes at L343 and L396:** "Every arrival is a standing cost before it is anything
  else." → "Every arrival is first a cost the city must keep paying." / "Every arrival is a cost the place must keep paying, before she is
  anything else."
- **ERR-32 · P2 L332 (FIND-P2-68):** "each a standing cost paid in heat at every resting place" → "each a cost paid in heat, without a
  pause, at every resting place".
- **ERR-33 · P3 L134 (FIND-P3-13):** "The spine's G2 quadrants (L104–143)" → "The spine's physical-constraint profile (L104–143)".
- **ERR-34 · P3 L188 (FIND-P3-31):** "a step across the place's whole standing cost" → "a step across everything the place must keep paying
  for".
- **ERR-35 · P3 L228 (FIND-P3-46):** "This answers the spine's G3 tension as texture only" → "This answers the spine's tension over what the
  city is for, as texture only".
- **ERR-36 · P3 L230 (FIND-P3-47):** "(research FIND-18; G7 real-world form, nothing written for the city)" → "(research FIND-18; the
  inspiration picks' real-world form, nothing written for the city)".
- **ERR-37 · P3 L264 (FIND-P3-56):** "Raising, wherever it is done, is a standing cost" → "Raising, wherever it is done, is a cost paid
  without a pause".

### Q2's files

**Gate 2**
- **ERR-38 · P6 L242 (FIND-P6-8)** (B E-106; C 206). Corrected: "**The survival layer** reaches every resident; every arrival, of either
  body and any of the 25 origin rows, is taught …, pays the heat at her stop with everyone else's, and, once someone newer comes to her, is
  the one who teaches it (whoever never teaches: FIND-P6-10, FIND-P6-27; SH-23)". A robot built here is a resident and not an arrival (P4
  FIND-P4-45).
- **ERR-39 · P7 L815–816 (FIND-P7-42)** (B E-106). Corrected: "Every resident who arrived is first the taught and a debtor to the earlier
  arrival; whoever the instruction turns to becomes a teacher and a creditor of the next; whoever it never turns to stays a debtor only
  (FIND-P7-36)."
- **ERR-40 · P4 L309 (FIND-P4-49), with P6 L410 (FIND-P6-24)** (B E-105; C 203; Gates 2 and 3). P4 L309 corrected: "Whatever the body or
  layer, the day ends at the same clock hours in a heated place (FIND-P4-6), except for the night's keepers, who rest outside it
  (FIND-P4-8, FIND-P4-42). **That is the only written point where nearly every resident's day is the same.**" P6 L410: "nearly everyone
  stops in the same hours (the keepers excepted, Phase 4 FIND-P4-42)".
- **ERR-41 · P4 L360 (FIND-P4-64 item 3)** (C 204). Add after "robots charging and humans sleeping at once": ", for everyone but its keepers
  (FIND-P4-42)".
- **ERR-42 · P5 L377 (FIND-P5-29)** (C 207; subject to Q-304). Corrected: "→ **Every body that arrives comes by Hwy 37, at least for its
  last stretch** (a robot built here does not arrive, Phase 4 FIND-P4-45)."

**Gate 3**
- **ERR-43 · P4 L206 (FIND-P4-14), coolant** (A 1). Corrected: "drinking and washing draw on the same account as warmth, and so does a
  robot's coolant if its formulation is water-based, which no admitted line states (Phase 8 FIND-P8-3; Q-178)".
- **ERR-44 · P8 L151 (FIND-P8-1) and L169 (FIND-P8-10), siligel** (A 2). L151 corrected: "Whatever either body takes in has come by Hwy 37
  (siligel on the provisional assumption of shipment, PV-6; the city's place in its chain reserved, RF-21), or is water made here from ice
  by spending heat". L169 corrected: "the human chain runs through Hwy 37, and the robot chain does too if siligel is shipped (PV-6; RF-21);
  neither is grown here".
- **ERR-45 · P7 L303–304 (FIND-P7-2)** (A 3). Corrected: "→ *Expression:* the baseline is the work every body here depends on every day;
  its 39.4% is a headcount share, not a count of what anyone meets in a day (Phase 4 FIND-P4-2), and none of it is the headline."
- **ERR-46 · P7 L656 (FIND-P7-28)** (A 4). Corrected: "Teaching is unwritten work of unknown size, and it is in no sector", matching
  Phase 4 FIND-P4-13's "some part of the settled residents' day".
- **ERR-47 · P6 L338–339 (FIND-P6-17)** (A 7; subject to Q-305). Corrected: "So the city's deaths stay here, and every death the files place
  here is a resident's; a passer-through's is possible and unwritten (Phase 5 FIND-P5-30)."
- **ERR-48 · P6 L198–199 (FIND-P6-4) and P7 L385–386 (FIND-P7-9), departure** (B E-102). P6 corrected: "it is not written as escapable by
  leaving: a human who came cannot return to Upper Earth, and no departure from the city is written (brief §4 item 5; RF-30)". P7
  corrected: "so no line has its expertise leaving as emigrants".
- **ERR-49 · P7 L485 (FIND-P7-16) and P4 L184 (FIND-P4-5), the world clock** (B E-103; also the station-builder scan, Q-300). P7
  corrected: "In the research, the real station's record was kept at fixed world-clock hours (research UI-6); it is a site fact, reserved
  (RF-70), and nothing is drawn from it for the city's clock." P4 corrected: "In the research, the real station's record was kept at four
  fixed world-clock hours (research FIND-39); a site fact, reserved (RF-70, RF-106), and not an input to the city's clock."
- **ERR-50 · P6 L430–432 (FIND-P6-26), the shaft** (B E-104). L430 corrected: "The only work that can be stopped is the work that is the
  city's purpose, except the shaft, which is kept filled and watched and cannot pause without loss (Phase 4 FIND-P4-8, FIND-P4-46)", and
  L431–432's "the purpose yields" read as "the purpose's stoppable part yields".
- **ERR-51 · P8 L163 (FIND-P8-7), fresh food** (C 205). Corrected: "what is fresh is the exception that came by the road (Phase 4
  FIND-P4-62); growing it here would be an electric load, and no growing is written (FIND-P8-8), so freshness, not plenty, is what a meal
  here can lack".

**Gates 5 and C: electricity and `DEC-705`**
- **ERR-52 · P4 L363 (FIND-P4-64 item 6)** (A 5; C 202). Corrected: "**Supply from elsewhere:** care, food for humans, siligel by shipment
  unless the city's geography says otherwise (RF-21); and electricity for both, from a source unwritten, whether made here or brought in
  (`DEC-705`)".
- **ERR-53 · P7 L389–392 (FIND-P7-9)** (A 5; C 201). Move electricity out of *What it receives* to its own line: "*Not written either way:*
  electricity, whose source no record places, made here or brought in (`DEC-705`; Phase 5 FIND-P5-25, FIND-P5-43)."
- **ERR-54 · P4 L188 (FIND-P4-7)** (A 6). "all on one electric supply" corrected to "all on one supply (spine §8e)". The robot charge is
  electric; the form of human heat is not written (`DEC-705`; Phase 5 FIND-P5-43; the power file's L16 flagged).
- **ERR-55 · P5 L400 (FIND-P5-33) and P7 L888 (FIND-P7-45), the corridor** (A 8; `DEC-687`). P5 corrected: "→ **If the datasheet's
  restatement holds (row 118; REQ-97), the first thing every arrival meets is the corridor's emptiness …**" (rest unchanged). P7 corrected:
  "the road beyond the city is one highway to a shared waypoint, through a corridor whose residents, if any, no admitted line writes (Phase
  5 FIND-P5-38)".

**Gate F**
- **ERR-56 · P7 L593 (FIND-P7-23)** (A 9; B E-101; C 208). "(spec L9, L159)" corrected to "(spec L9, L66)". Spec L159 is in the excluded
  section L153–161 (contract CR-47).

**The station-builder scan**
- **ERR-57 · P6 L217–220 (FIND-P6-5) and P6 L488–489 (FIND-P6-32)** (A 10; B E-107). P6 L217–220 corrected: "→ **Narrowed in Round 3:**
  the debt is grounded on the city's own lines (spec L145 as the founding's condition, the city's own half of the honor, the induction
  findings); the paper is the founding's condition, not a party to the debt (split 3)." The denial sentence is dropped; the split note
  stays. P6 L488–489 corrected: "Here *paper* names the founding's condition (spec L145)."

**The generator-vocabulary sweep** (plain language; low stakes; where the readers' wordings differ, the first is A's, then B's or C's)
- **ERR-58 · P4 L190 (FIND-P4-8):** "a G7 form, not transplanted" → "the picks' real-world form, not transplanted".
- **ERR-59 · P4 L246 (FIND-P4-32):** "every arrival is a standing cost paid in heat at every resting place" → "every arrival adds a cost
  paid in heat, every day, at every resting place".
- **ERR-60 · P4 L262 (FIND-P4-38's heading):** "Every free hour carries the standing cost." → "Every free hour costs heat." / "Every free
  hour is paid for in heat."
- **ERR-61 · P4 L317 (FIND-P4-50):** "a step across the place's whole standing cost" → "a step across the full cost of the cold" / "a step
  out of paid heat into the full cold".
- **ERR-62 · P5 L367:** "Every remedy the city's deficits address" in the parent → "Every remedy for what the city lacks lies in the parent".
- **ERR-63 · P5 L416 (FIND-P5-36):** "each one is a new standing cost before anything else" → "each one adds a lasting cost in heat before
  anything else".
- **ERR-64 · P5 L422 (FIND-P5-39):** "recorded as a candidate standing cost" → "recorded as a possible lasting cost".
- **ERR-65 · P5 L442 (FIND-P5-46):** "so raising is a standing cost" → "so raising is a cost that never ends".
- **ERR-66 · P6 L187 (FIND-P6-4):** "every arrival is a standing cost paid in heat by everyone" → "every arrival adds a cost in heat that
  everyone pays".
- **ERR-67 · P7 L576–577 (FIND-P7-22):** "The place's grudging tolerances stay tolerances, each permitted and charged and none prohibited"
  → "What the place permits and charges for stays permitted and charged, and none of it is prohibited".
- **ERR-68 · P7 L598 (FIND-P7-23):** "still runs into the standing cost" → "still runs into the cost of heat".
- **ERR-69 · P7 L650 (FIND-P7-28):** "is first a standing cost paid in heat" → "first adds a lasting cost paid in heat".
- **ERR-70 · P8 L179 (FIND-P8-13):** "every indoor hour carries the standing cost" → "every indoor hour costs heat".
- **ERR-71 · P8 L199 (the dress axis line):** "crosses the place's whole standing cost" → "crosses from paid heat into the full cold".
- **ERR-72 · P8 L203 (FIND-P8-21):** "a step across the place's whole standing cost" → "a step from paid heat into the full cold".
- **ERR-73 · P8 L215 (FIND-P8-25):** "Every free hour carries the standing cost" → "Every free hour costs heat".

### Q3's files

**Gate 0**
- **ERR-74 · Step 6 L318** (A E4; B E-105; also Gate 6, substitute 4). Corrected: "eight of ten axes are the product of a conflict between
  generators; §3's (G2 nearly alone) and §10's (G2 against itself at two depths, L316) are not, and both are flagged for the
  author-defaults risk."
- **ERR-75 · Phase 10 L1653 and the B2 tally L1923–1927, rows 31 and 84** (A E5; B E-101; C 202; which way is Q-316). The two rows must be
  classed alike. Either count row 84 taken, as row 31 is: "Rows with something taken: 38 (… 83, 84). Rows with nothing taken: 18 … no line
  of the city allows it 18 · CST 9 · DCI 8 · barred 1 · a request 18"; or move both nulls to their not-taken columns (L1653's taken cell
  reads "—"; extends notes 27).
- **ERR-76 · Phase 10 L42–44** (B E-103). As an amendment note: "excluded lines read; citations at L950–951 and L986 (spec L135) and
  stage-B items resting on spec L155, L157 and L171 past its clause are held OUT OF FRAME (Step 5 RC-74 to RC-78; REQ-167)".
- **ERR-77 · Phase 9 L463 (RF-182's credit cell)** (B E-102; C 201). "C (FIND-P9-231)" → "C (C231)", matching FIND-P9-41's own credit at
  L352.

**Gate 3**
- **ERR-78 · Phase 10 L793–794 (CAT-39)** (B E-104). Corrected: "Through every nightly stop, at the clock's hours and in every season,
  they keep heat, water, charge and the shaft running (Phase 4 FIND-P4-6, FIND-P4-8); real facilities give the night as one double shift
  so that no handover falls in the middle of it (fact 7), a form only." The clause about staying with the instruments moves to CAT-47 (the
  instruments' keepers), whose calendar may stop (Phase 4 FIND-P4-9).
- **ERR-79 · Phase 4 L264 (FIND-P4-39)** (A E3). "the least cold months and the only ones in which the place shows anything to the eye but
  the city" → "the least cold months, under a sun that does not set; outside the polar night the sun rises and sets, and inside it the sky
  still holds a noon twilight and the moon's week (CAT-B1-5, CAT-B1-6)". (Phase 4 L266 is put to the developer at Q-320.)
- **ERR-80 · Step 5 L1157 and L1247–1248** (A E9). "the street never goes quiet (Phase 3 FIND-P3-18; RC-54)" → "the street's work never
  stops (Phase 3 FIND-P3-18, as RC-54 narrows it)".
- **ERR-81 · Phase 10 L286 (r19) and L763–764 (CAT-26)** (A E8; subject to Q-322). Source "Phase 4 L397; Phase 7 L578" → "Phase 7 L578
  (charging somewhere cold, a tolerance: permitted and charged); Phase 4 FIND-P4-17 (no charge is planned cold) and FIND-P4-30 (an
  emergency cold charge leaves a permanent scar)"; title "Charging points somewhere cold" → "Charging somewhere cold, a tolerance."
- **ERR-82 · Phase 10 L894 (FIND-P10-3) and the axis gloss L676–677** (C 205; Gates 3 and 11). "So whatever stands must be lifted every
  year and travels with the ice" → "So the snow lands on whatever stands every year, and whatever stands must be lifted again and again, on
  a cycle of years, and travels with the ice"; the same change to "must be lifted every year against the snow" at L676–677. Basis: Phase 4
  L220; Phase 10 L1408–1411.
- **ERR-83 · Phase 4 L196 (FIND-P4-11)** (C 206; A A9). Add, conditional on REQ-B2-1: "away from the city; over the inhabited part on the
  coldest still days, the city's own vapor may close the view with nothing falling (CAT-B2-3; FIND-S5-6)"; add Phase 4 L196 to REQ-165.
- **ERR-84 · Phase 9 L348 (FIND-P9-39) and L278 (FIND-P9-15)** (A E2; C 204; pending Q-255, which may narrow it further). L348:
  "Everyone stops at the same clock hours, robots to charge and humans to sleep" → "Everyone but those who keep the night's heat, water,
  charge and shaft stops at the same clock hours, robots to charge and humans to sleep (FIND-P9-31)". L278: add "unless she keeps the night
  (FIND-P9-31)". Add both to REQ-165's list beside Phase 4 L309 and L360.

**Gate 4**
- **ERR-85 · Phase 10 L970–971 and Step 6 L275, the axis's peer-free answer** (A E10; subject to Q-323). "Yes" → "In part: raising, moving
  or losing what stands on an ice sheet is a practice real places on the same ice sheet share (convergence 6, L1478–1483); what holds only
  here is the site's own burial rate and drift, a city of 441,378 standing on them, and that what lies below is kept for nothing while what
  stands is raised."

**Gate 6**
- **ERR-86 · Phase 10 L779–781 (CAT-35) and L869 (CAT-78)** (A E7; C 203; the form is Q-324). CAT-35 → "see CAT-2 (its drilling
  apparatus); the real complex's parts are a researched comparable, conditional on REQ-145" (C's alternative: fold CAT-35 into CAT-2 as its
  apparatus, keeping fact 24's parts list; the count at L872–874 then reads 77, physical things 18). CAT-78 → "The oldest living keeper of
  the shaft. A role only, unnamed, uncounted" (its "first teacher of the newest arrival" is CAT-36).

**Gate C**
- **ERR-87 · The Step 7 datasheet L21** (A E6; also Gate 0; B's reading at Q-335). "see `Review_Panel` Tier U content (Step 8)" → "see
  `Corpus_Reference_Sheets/Review_Panel_Full_Text_Quick_Reference.md` (Step 8)", as the quick-reference sheet's L359 was corrected on
  2026-11-18 (that line checked at its source for this merge).

**Gate F** (each caught at Step 5, none applied; the corrections are Step 5's own dockets, REQ-167 and REQ-169)
- **ERR-88 · Phase 10 L950–951 and L986, spec L135** (C 207; A E1; B E-106). Strike the L135 citations; the distance stands on spec L9 and
  L66 (RC-77).
- **ERR-89 · Phase 10 L1214 (Q-217), L1653, L1696–1699, L1917, spec L155** (C 208). Mark the nearness clause OUT OF FRAME; the null (no
  marker at any computed position) stands alone; Q-217 and Q-B2-3 re-put without the premise (RC-74; Q-238).
- **ERR-90 · Phase 10 L1810, spec L157** (C 209). Hold CAT-B2-8, or re-ground it beside CAT-78 or on CAT-17 (RC-75; RF-210).
- **ERR-91 · Phase 10 L1688–1690, spec L171 past its clause** (C 210). Narrow to the admitted clause: "the outpost ran on the national
  grid's overflow", reading "another grid's" as "the national grid's" (RC-78; RF-211).
- **ERR-92 · Phase 10 L709, L733–734, L862, L911–914, L1380–1382, the struck L167 sentence** (C 211). Read "any living stock the research
  keeps", laboratory floors with no subject, and CAT-76 a role without a program, until `DR-10` and spine Q-38 are answered (RC-72;
  REQ-169; Q-256).

**The station-builder scan**
- **ERR-93 · Phase 9 L212** (A E11; B E-107). Delete "the station's operator or nation (`DR-19`);" from the robots' *never anchored in*
  cell; the cell keeps "a city-wide origin; the founders' stock; Gen/Mark; build (Ch. 13 L29–36)".
- **ERR-94 · Phase 10 L790–791 (CAT-38)** (A E11; B E-108). "the records' language is not inferred from the station's operators (spine
  RF-46) [B]" → "the records' language is not written (spine RF-46) [B]".
- **ERR-95 · Step 6 L299** (A E11; B's rewrite). Strike "the station is a coordinate and a paper inheritance, never the population's
  origin"; the cell reads "It grounds no motive (`DR-19`). No cell uses it."

**The datasheet lags, together** (orchestrator's record): DS12 L17, L26, L34, L35 (ERR-17 to ERR-19), DS2 L16 (ERR-20) and the Step 7
datasheet L21 (ERR-87) are errata on the datasheets, not applied. DS-P7 L35 and L56 are a request (REQ-213).

**Errata: 95 (ERR-1 to ERR-95), all PROPOSED, none applied.**

---

## 4 · The station-builder scan's result

**FAIL in all three sub-units. No assertion that the station's builder explains a form was found anywhere. Denials stand inside findings,
a catalog item, a recommended answer and a record:** P2 L283 (FIND-P2-46) with RF-87 and Q-75's answer; P2 L210; P2 L195; spine L109,
L187; P3 L274; P6 L217–220 with L488–489; Phase 9 L212; Phase 10 L790–791; Step 6 L299 (ERR-22 to ERR-27, ERR-57, ERR-93 to ERR-95). The
world clock (P7 L485; P4 L184) carries a real station's practice into the city's era (ERR-49). **Put to the developer:** how far runbook
L2944 reaches (Q-300); Phase 9 L202 (Q-337); Step 5 DK-3's "keep" (Q-338); the FIND-P2-46 fix (Q-301). **Outside the pass:** DS12 L34
(ERR-19); DS-P7 L35 and L56 (REQ-213); Step 5 RL-31 for the CST (REQ-227). Every scan was a reading scan (no search command was allowed); a
reading scan is not exhaustive.

---

## 5 · The generator-vocabulary sweep's real hits, with their plain rewrites

| File:line | Method words in finding prose | Plain rewrite |
|---|---|---|
| research L222, L223 | "a standing cost"; "the cold's standing cost" | ERR-28, ERR-29 |
| P2 L214, L234 (with L343, L396), L332 | "a G7 adjustment"; "a standing cost" (×2) | ERR-30 to ERR-32 |
| P3 L134, L188, L228, L230, L264 | "G2 quadrants"; "whole standing cost"; "G3 tension"; "G7 real-world form"; "a standing cost" | ERR-33 to ERR-37 |
| P4 L190, L246, L262, L317 | "a G7 form"; "a standing cost" (×2); "whole standing cost" | ERR-58 to ERR-61 |
| P5 L367 *(missed by the sweep)*, L416, L422, L442 | "deficits address"; "standing cost" (×3) | ERR-62 to ERR-65 |
| P6 L187 | "a standing cost" | ERR-66 |
| P7 L576–577 *(missed by the sweep)*, L598, L650 | "grudging tolerances"; "the standing cost"; "a standing cost" | ERR-67 to ERR-69 |
| P8 L179, L199, L203, L215 | "the standing cost"; "whole standing cost" (×2); "the standing cost" | ERR-70 to ERR-73 |
| Phase 9 L344 *(off the sweep's list)* | "unspeakable" (Step 5 T-35) | "for most of the city the thin air is a cost no one's body gives a reason to name; for the rest it is each person's own" (Step 5's rewrite, L731–732) |
| Phase 9 L346 *(off the list)* | "a deficit", "unspeakable" (Step 5 T-36) | "thin air is a lack no one in particular can remedy" (Step 5's rewrite) |
| Phase 9 L396 *(off the list; B)* | "the minority's unspeakable cost" | "FIND-P9-38, the minority's cost the majority's bodies give no reason to name" |
| Phase 9 L462 (RF-181) *(off the list; B)* | "unspeakable to the majority" | "The minority's chief cost, one the majority's bodies give no reason to name" |

The last four wait on Q-254 (the word *unspeakable*) and go to the append-only translation docket (REQ-173); they are not given ERR
numbers because no Q3 reader failed them. Low stakes throughout: wording only.

---

## 6 · Requests (each to the orchestrator unless named; PROPOSED)

**The orchestrator's instruments (defects of the instruments, not of the pass)**
- **REQ-205 · The findings index.** It lists "every line beginning with a bold FIND id" but misses lines that begin "- **FIND-" and bold
  FIND lines whose title opens in italics. The union of what the readers found: FIND-P2-60 to FIND-P2-68, FIND-P3-46, FIND-P3-74 (Q1, 11);
  FIND-P4-66, FIND-P5-32, FIND-P5-34, FIND-P5-55, FIND-P6-11, FIND-P6-32, FIND-P7-45, FIND-P8-45 (Q2, 8, every differentiation axis of Phases
  4–8 among them); and nothing past FIND-P9-45 (no FIND-P9-46, nothing from Phase 10 or Step 5; Step 5's own REQ-160 records it). Widen the
  pattern, re-issue the index, hand-check it against these cases, and label it incomplete until then. *(Q1 A 31, B 131, C 221; Q2 A REQ-A1,
  B REQ-B104, C 207.)*
- **REQ-206 · The mechanical sweep.** It misses phrases split across a line wrap (P7 L576–577), a plural on a phrase's first word (P5 L367,
  "deficits address"), and every term off its list that Step 5's REQ-159 asked for (bare *deficit*, *strength*, *tolerance* alone, *Balanced*
  and the other shape names, the address labels, *unspeakable*, *characteristic failure*, `D-n`, and the pass's code labels); it does not
  cover Step 6. Join wrapped lines, match stems on every word, widen the list, sweep Step 6, prove it first on P7 L576–577, P5 L367, Phase 9
  L344 and Phase 4 L238; treat 768 as a floor; and give the hits outside the admitted spans (contract, frame, audit, spine, research, P2, P3,
  P4–P7 bookkeeping lines as listed under each sub-unit; Phase 9 L115–142; Phase 10 L63–182 and L1173) to a reader whose spans reach them.
  *(Q1 A 37, B 132; Q2 A REQ-A1, B REQ-B105, C 208; Q3 A R1, B REQ-B101, C's request 202.)*

**From Q1's files**
- **REQ-207 · The run-modes lines.** Audit L171 says `DEC-695`'s edits were applied at L53, L99, L109, L118 and L138; frame L111, L218 and
  REQ-21 name L53, L99, L105, L118 and L138. Check whether L105 was edited and correct whichever record is wrong. *(A 30.)*
- **REQ-208 · `DEC-716`'s source.** Step 1 holds eight question rows (Q-28 to Q-35) against nine numbers (`DEC-708` to `DEC-716`); name the
  ninth's row, together with audit REQ-30's 28-against-27 mapping for `DEC-707`. *(A 32; C 223.)*
- **REQ-209 · The merge rule's span.** Align the header lines (spine L8, audit L11, research L9, P2 L8, P3 L6: "L670–692") with the
  receipts (L653–692), the span this step applies. *(C 220.)*
- **REQ-210 · The web calls.** Research L8 and L503 record 256 calls by the readers against the session tool's 284; record where the other
  28 came from. *(A 33.)*
- **REQ-211 · The two baselines, stated once.** Put `09` §2 (L57, L201, L216) and `16` (L30–32, L129, §23 L2349–2358) on one list at source,
  and write once in a pass file: "§23's 39.4% governs (`DR-142` item 8); `09` §2's 42.6% and 43.9% are not used, by `16` L30–32; the two
  differ by baseline definition (`09` L216, as the Step 7 datasheet states it), left open (Phase 4 REQ-81)". On one denominator the like-for-
  like gap is 16,032 workers, 4.4 points (Q1 C). *(Q1 A 35, B 135, C 222; Q2 A REQ-A2, B Q-B105, C 211; Q3 A R3, C's request 203.)*
- **REQ-212 · Where the city's emissions land: a later research round, from read sources (LAW 0-R).** What vented heat, water vapor and
  exhaust do in still air at about −55 °C and 624 hPa, how long any haze persists and how far it reaches; how emissions deposit into surface
  snow, and how snow for melting is sited and kept clean (the real site's windward trap, research FACT-91, is one trace); where the labs'
  once-through air, refuse, spills, the shaft's fill and the city's discards under the snow (REQ-B1-2) end up. Nothing is written about the
  lake (RF-6). Until then, Phase 3's clear-air statements (FIND-P3-2, FIND-P3-36) read as true away from the city's own emissions. *(Q1 B
  136, C 224; Q2 B REQ-B107, C 209; Q3 C.)*
- **REQ-213 · DS-P7 L35 and L56.** A dated, in-place correction, moving no cited line, so the *not carried* notes state what is not carried
  without naming the station builder's nationality (runbook L2944). *(Q1 A 36; Q2 A REQ-A3.)*
- **REQ-214 · The ~1,260 km gap and Hwy 37's route at `Highways.md`**, their owner; Q1 and Q2 checked them only at the spec and across
  phases. *(Q1 B 133; Q2 C.)*
- **REQ-215 · The spine's "about 18,140 workers fall on the human-keyed term" (spine L198)**, a reader's arithmetic on a formula off Q1's
  list, to be hand-checked at source. *(Q1 B 134.)*

**From Q2's files**
- **REQ-216 · Phase 7 L34's "11 spans, 73 lines" for `16`**, against the 7 spans and 78 lines its own ranges total; check against Phase 7's
  reading list. *(B REQ-B101.)*
- **REQ-217 · Spec L17, cited for 156,685 humans at P7 L568 and P8 L161.** Q3's reader B read spec L17 off-list (logged) and found 156,685
  humans, 284,693 robots, 441,378 combined; record that the citation holds. *(Q2 B REQ-B102.)*
- **REQ-218 · Spec L221** (P8 FIND-P8-32): confirm whether it lies in a section the contract excludes. *(B REQ-B103.)*
- **REQ-219 · Universe-repo negatives.** State whether Phases 6–8's negatives for faith, holidays and factions were searched in the universe
  repo under both names, by a filenames-only check, and name the paths; until then they count for this repo only. *(B REQ-B106; C 204.)*
- **REQ-220 · Band variance in Phases 5 and 8.** It is not in their admitted spans; check the phase spine's Phase 5 and Phase 8 band lines,
  and list it for Step 10 if required, or record "not required" with the line. *(C 212.)*
- **REQ-221 · `16` §23's narrative still carries the closed-population premise and the stale 3.5×**, withdrawn by `DR-127` item 2 and
  `DR-130` item 1; record the canon-side lag for the post-ULM industry review. *(B.)*

**From Q3's files**
- **REQ-222 · Extend REQ-165's amendment list:** Phase 9 L278 and L348 (ERR-84), Phase 4 L196 (ERR-83), L264 (ERR-79) and, on the
  developer's word, L266 (Q-320); after the developer's word (`DR-101`). *(A R2; C's request 201.)*
- **REQ-223 · Gate 3 for Step 5's within-phase rows outside Q3's files:** RC-52, RC-53, RC-54 (Phases 2, 3, 5; Q-233), REQ-195 (Phase 8,
  FIND-P8-7 against FIND-P8-10; Q2's Gate 3 item 10 touches FIND-P8-7) and Step 6 REQ-203 (Phase 3). No sub-unit ran Gate 3 on them; put
  them on the next list. *(A A4; B REQ-B105.)*
- **REQ-224 · Phase 9's sweep places handed to Step 7** (L429: places 3, 9, 23, 30, 50, 65, 80, 83, 85, 88, 95, 96, 100, 101, 102, 104, 107,
  109, 111) on a Gate 9 reader's list; they lie outside Q3's admitted span. *(B REQ-B104.)*
- **REQ-225 · On the next list that runs these gates:** runbook §E's four questions at source; `16` §23 at source for the shared constants;
  stage B1's city lines checked at their source, not through the stage-A carriers; the phase spine's question lists for Phases 9 and 10.
  *(B REQ-B102.)*
- **REQ-226 · Census I at the census file itself**, since every file read carries 441,378 by citation and the extent row is a census
  derivative; and the first-pass workforce, 324,452 at the Phase 7 datasheet L27 against 324,453 at L41. *(A R4, A22.)*
- **REQ-227 · Step 5 RL-31** (the culture sheet's denial naming the station operators' nation) added to REQ-194's flags for the CST, so the
  line is never written with that framing (`DR-19`). *(B REQ-B106.)*
- **REQ-228 · A later research round, from read sources:** the sun's daily path at the real site during the midnight sun, and the noon
  twilight across the polar night, so "no sky edge" can be worded on measured light, beside REQ-B1-1. *(B REQ-B103.)*

**The recording law (Step 9.5)**
- **REQ-229 · Record the readers' procedural slips, all disclosed, none load-bearing:** Q1 B ran `ls` on the spec folder and piped `sed`
  through `od -c` and `cut`; Q2 A read Phase 4's L164–313 before Phases 5–8 and ran `wc -l` on its own output; Q2 B wrote its PROOF blocks
  with a shell heredoc and ran an `ls -d` listing; Q2 C ran `wc -l` on its own output, disclosed only in Round 3; Q3 A piped `sed` through
  `cut` and ran `wc -l` on its own output; Q3 B piped `sed` through `wc -c`, `head -c`, `cut` and `cat -A`; Q3 C piped through `cut`, used
  `echo` separators and a `for` loop over `sed`, and ran `wc -l` on its own output. Label slips: Q2 B recorded Gate 10 "N/A" (it is NOT
  RUN, brief §2); Q2 C headed an excerpt "Raw output, whole" (relabeled here); Q1 B named a real nation and two real-world regions (written
  here by role, `DEC-723`). *(From each reader's own log and the Round 3 replies.)*

---

## 7 · Questions for the developer (each recommended answer PROVISIONAL)

**From Q1's files**
- **Q-288 · (Gate 0)** The contract's and frame's question tables (contract L249 Q-3, L251 Q-5; frame L208 "all unanswered") state positions
  from before `DR-143`. *Recommended:* add a dated note at the end of each file, moving no cited line, pointing to the audit's §5
  (L154–173); not an erratum, since the lines were true when written. *(B 126.)*
- **Q-289 · (Gate 1)** Was every row of the candidate list researched (LAW 0-P), not only the official picks at Step 3? *Recommended:*
  record that Phase 10's stage B researched rows 1–85 of the whole pick list, row 86 waiting by your ruling (Gate 7), so LAW 0-P is met at
  Phase 10 for this pass, while Step 3's own list held the official picks only on the day the law was ruled; confirm it on the LAW 0-P
  coverage tracker. *(C 219.)*
- **Q-290 · (Gate 2)** Step 3 has no research target on the robot majority's own needs. *Recommended:* at the next research round, add
  machinery-and-materials targets that bear on the robot body without setting a robot threshold (`DEC-697`; research Q-66), and record that
  the skew is partly structural. *(B 142.)*
- **Q-291 · (Gate 4)** Which Q1 finding is weakest under the swap: *Snow without weather* (A), the Phase 2 axis (B) or the spine clause
  "only the work that is its purpose can ever be stopped" (C)? *Recommended:* record all three as the weak set; keep the spine clause as a
  consequence, not the identity sentence's carrying clause, pending Q-55 and Q-96.
- **Q-292 · (Gate 6)** Are *the stores* the archive's physical holdings, food stores, or both? *Recommended:* split them in the pass: sample
  and core stores (possibly the archive's physical part, its form unwritten, REQ-79) and food stores (research FIND-37, RF-74); which is
  which stays open until Phase 10 and your word. *(C 227.)*
- **Q-293 · (Gate 9)** The losing side of "a condition, not a filter" (P3 FIND-P3-45): a shadow candidate? *Recommended:* no new candidate
  for *being kept*: Phase 7 FIND-P7-36 (L722–736) writes it (she is kept in body and never becomes the teacher); Phase 3 carries one line
  pointing there. The losing side of *belonging* goes with Q-310. *(A 40; B 144; C 226.)*
- **Q-294 · (Gate 9)** May frame RF-24 (staffed against settled) close, now that P3 FIND-P3-54 writes it as two registers inside one
  Settlement? *Recommended:* yes: "written as registers; the type stays Settlement; no dual typing", with P3 L254 as the record; reopen only
  if a later phase finds an institution that controls who is present. *(A 39.)*
- **Q-295 · (Gate 9)** Restate the shared "no term" once, at a single source: "no term to Upper Earth; departures within the nation
  unwritten (RF-30)"? *Recommended:* yes; correct the source findings (ERR-8 to ERR-16, ERR-48) and let later phases cite the corrected
  form. *(A 41.)*
- **Q-296 · (Gate C)** Is "the city's own genetics research folder", tagged for Phase 7 (P3 L27), the folder `06` quarantines for the whole
  run (frame L23–24; runbook L2074)? *Recommended:* the orchestrator confirms by name; if it is, the tag is withdrawn and Phase 7 is checked
  for any use of the folder (Q2 found the geneticist not an input, `DR-143` item 7, but did not check the folder). *(A 34.)*
- **Q-297 · (Gates C and F)** Where does the real station's practice fall on research Q-63's line? *Recommended:* answer Q-63 as
  recommended; keep CONV-1's member as access and infrastructure and the borehole's history as inherited record (CR-29); strike FIND-12's
  greens sentence and FIND-25's winterers clause, which are crew life. No finding's conclusion changes. *(B 140; A's watch item.)*
- **Q-298 · (Gate C)** When Q-56 (the lake's length) and Q-61 (the falls/lands split) are answered, apply each at once to every line that
  carries it? *Recommended:* yes: spine L62, L107, L110, L133 and contract CR-2, CR-32, CR-33; reword "what falls stays" on the measured
  figures, which make the argument stronger. *(C 228.)*
- **Q-299 · (Gate G)** Settle the picks' provenance before Step 8? *Recommended:* answer research REQ-53 / Q-65 (spine REQ-36): when and on
  what basis the three picks were set, and whether they came from the struck genetics line; until then keep G7 counted as independent with
  the doubt stated, and every genetics direction G7-only and PROVISIONAL (RF-43). *(C 229.)*
- **Q-300 · (The station-builder scan, all sub-units)** How far does runbook L2944's denial rule reach: a treaty article paraphrased inside a
  finding (P2 L195); a guard on inference or an operator named only to be set aside (spine L109, L187; P3 L274; P5 L279; P8 L229; P6 L380);
  a real station's practice carried as the city's (the world clock, P7 L485, P4 L184)? *Recommended:* the rule binds inside findings,
  catalog items, cells and recommended answers: strike the operator clause or write the positive rule ("a coordinate only (`DR-19`)"; "is
  in no listed line (RF-46)"). Input dispositions, foreclosure columns and canon-opened bookkeeping may keep their prohibitions, and even
  there need not name the operator. The world clock is site history, and its Gate 3 erratum (ERR-49) stands either way. *(Q1 A 38, B 145,
  C 225; Q2 A Q-A1, B Q-B101, C 202.)*
- **Q-301 · (The station-builder scan)** FIND-P2-46: rewrite it flat (A, B) or withdraw it to the post-ULM census review (C)?
  *Recommended:* rewrite it flat (ERR-22): the missing row is the city's own table's fact, and withdrawing it would leave the census review
  without it; the station appears nowhere in it.

**From Q2's files**
- **Q-302 · (Gate 0)** P4 L23 counts 5 + 2 + 1 = 8 against DS4's "7 of 7". *Recommended:* count addresses: the robot-biology folder is one
  address read through two files (RP and the cold file); correct L23 with a dated note, moving no cited line. *(C 201.)*
- **Q-303 · (Gates 1 and 5)** Refuse, waste and the city's discards are unwritten in Phases 4–10, and no line says why. *Recommended:* write
  nothing in-run; record at Step 10 that they are not written and, if a standing content boundary governs them, cite it as the reason; the
  physics of what sinks under the snow joins REQ-212. *(Q2 A Q-A3; Q3 C's question 203.)*
- **Q-304 · (Gate 2)** P5 L377, "Every body arrives by Hwy 37": about arrivals only (B), or an overclaim (C)? *Recommended:* apply ERR-42;
  one clause removes the doubt.
- **Q-305 · (Gate 3)** P6 L338–339, "every death here is a resident's": *Recommended:* apply ERR-47 (minor).
- **Q-306 · (Gate 6)** Which tier holds heat and warm charge: the baseline (P4 L170; P7 L301–302), the survival sector (P7 L370–373), or
  both by scale? *Recommended:* both by scale (every city's floor in the baseline, the extra this cold demands in the survival sector); say
  so in one clause in FIND-P7-8; derive no split figure in-run. *(A Q-A4.)*
- **Q-307 · (Gates 6 and I)** Name the one mechanism written as membership, the forward debt, the standard of worth, learning and
  belonging, and the mark of being from here (P5 FIND-P5-35; P6 FIND-P6-4, FIND-P6-7; P7 FIND-P7-29; P8 FIND-P8-32) once, and class it
  inflected? *Recommended:* yes: one structure seen from five phases, named once at Phase 10 or Step 10, RF-137 the parent with RF-131,
  RF-160, RF-161 and RF-174 as its aspects; classed inflected from the national mentor and mentee bond (RP L418), with the forward debt and
  Phase 9 FIND-P9-35 (Q-336). *(A Q-A5; B Q-B104; C 213.)*
- **Q-308 · (Gate 6)** The shaft's watch: the keepers' function or the research's? *Recommended:* follow Phase 4's Q-112: set row (i)'s *who
  is present* to "the night's keepers, a function (row (l))"; the structure stays the research's, its watch the keepers'. *(C 205.)*
- **Q-309 · (Gate 9, shadow candidate)** Membership can lapse when someone stops being needed (P5 L413–414). *Recommended:* write that
  whether being needed, once reached, can lapse is not written; carry it to Phase 9 and the DCI; write no status rule; hold it as a shadow
  candidate until answered. *(A Q-A6.)*
- **Q-310 · (Gate 9)** Narrow "a condition, never a filter" (P4 L200; P7 L642–646) to being kept? *Recommended:* yes, by one clause in
  FIND-P4-13 and FIND-P7-27: "never a filter for being kept; the same knowledge marks belonging (Phase 5 FIND-P5-35)"; the permanent
  newcomer (P7 L726) is that filter's written losing side. *(A Q-A7.)*
- **Q-311 · (Gate 9, shadow candidate)** If the purpose yields first, does the shaft yield? *Recommended:* no: the shaft is excepted
  (ERR-50); the yielding is a pause with a route back for the instruments only, and SH-22 is checked with that exception. *(B Q-B103.)*
- **Q-312 · (Gate 9, shadow candidate)** What is the point of entry to membership for a robot built here or a human born here?
  *Recommended:* for a robot built here, Phase 9 writes it conditionally (FIND-P9-13, if a chamber stands, PV-5: she comes online as the
  newest arrival); for a human born here it stays a null; hold it with Q-327 and write no rite or status. *(B Q-B102.)*
- **Q-313 · (Gate 9)** Once arrivals stop, whoever came last has no one newer, ever (P7 L655). *Recommended:* already reserved: Phase 9's
  SH-35 (L475) writes that if arrivals slow, the last to come stays newest; cite it from Phase 7; no new candidate. *(C 210.)*
- **Q-314 · (Gate 9)** P7 L894 and P8 L289 dispose of an objection as "refused, `unmet`" before the Review Panel runs. *Recommended:* reword
  to "refused under the peer-free test; its disposition is the Review Panel's (Step 8)"; Step 8 disposes freely. *(C 203.)*
- **Q-315 · (Gate F)** Does the outpost's power from the national tower's regulated grid (P5 L290) belong to the city's height, the grid
  being fully online at about 2688 and the height dated before it? *Recommended:* hold FIND-P5-14 and its uses (P7 L398–399, L443, L465) as
  written, with a note that the grid's reach at the height is undated, until you place the height; draw no date (RF-18). *(A Q-A2.)*

**From Q3's files**
- **Q-316 · (Gate 0)** Rows 31 and 84: taken or not? *Recommended:* taken, as extends notes on nulls (their cells and the extends section
  already say so): 38 taken, 18 not; both rows classed alike (ERR-75). For Gate 7 both are ornament either way. *(A, B; C would move them.)*
- **Q-317 · (Gate 0)** Phase 10 L1025 marks the Parent position covered on a reading Step 5 holds open. *Recommended:* follow Q-235's
  recommendation: leave the Parent unmarked until answered; the count reads 2. *(B 104.)*
- **Q-318 · (Gate 2)** The catalog's people lean to the research layer (10 of 21 roles). *Recommended:* accept it for this pass as the pick
  list's effect; note it at Step 10; let the CST, which writes what people do in a day, carry the general population's roles; write no role
  for them in-run. *(C's question 201.)*
- **Q-319 · (Gate 2)** Narrow CAT-1's "so the honor is paid daily, not once" (Phase 10 L689–690)? *Recommended:* yes, to "the district is
  where the city's own scientists work"; the honor stays a name only. *(A Q9.)*
- **Q-320 · (Gate 3)** "No sky edge" against the measured noon twilight, and Phase 4 FIND-P4-40 (L266)? *Recommended:* one docket line
  beside REQ-170: "for about 243 days no sunrise or sunset bounds the day; in the polar night a faint noon twilight marks midday, not when
  to stop", touching P4 FIND-P4-5, FIND-P4-64 item 1 and Phase 9 FIND-P9-15, FIND-P9-19 by note only; FIND-P4-40 joins RC-58's reading as
  it stands (A's alternative: amend L266 to "the only light enough to work by is the city's own; the sky holds a faint noon twilight and the
  moon's week"). *(B Q-B103; A E3.)*
- **Q-321 · (Gates 3, 4 and 11)** FIND-P10-9, the threshold as "the city's most dangerous ordinary place": *Recommended:* narrow it to
  "the threshold is where a kept thing, and the hands carrying it, are most at risk", since its one research leg is about cryogen transfers.
  *(B.)*
- **Q-322 · (Gate 3)** CAT-26's source rests on one reader's off-list read of Phase 7 L578. *Recommended:* the orchestrator confirms Phase 7
  L578 at source (one line), then ERR-81 is applied; Phase 4 L397 does not carry the claim on any reading. *(A; C (c).)*
- **Q-323 · (Gate 4)** The Phase 10 axis's peer-free "Yes": FAIL (A), FLAG (B, C) or PASS; and which finding is weakest (the catalog axis,
  FIND-P10-9 or FIND-P10-6)? *Recommended:* amend both "Yes" answers to "In part" (ERR-85), the practice being shared and the rates the
  site's; record the three as the weak set; the gate stays FAIL until the amendment is applied.
- **Q-324 · (Gate 6)** Does the gate reach things and roles named twice, or institutions only; are the lake program and "the genetics
  program" one; fold CAT-35 into CAT-2, or cross-reference? *Recommended:* the gate is about institutions, so the item doubles are
  bookkeeping: cross-reference a setting and its recurring event (CAT-56/CAT-72; CAT-59/CAT-71), merge the role doubles (CAT-78's second
  half into CAT-36; CAT-50 into CAT-77) and fold CAT-35 into CAT-2 (ERR-86); treat the lake and genetics programs as one research program by
  applying REQ-169. *(B Q-B105, Q-B106; A; C.)*
- **Q-325 · (Gate 7)** The share's definition and base. *Recommended:* report the whole-list share (27 of 85 = 31.8%), the PRIMARY-tier share
  and the official picks (3 of 3) every time, and adjust none; an *extends* note is ornament unless it changes a finding's wording, standing
  or scope; rows 43 and 45 follow CAT-B2-8's fate (ERR-90); add a changed · ornamented · withheld · omitted column to the pick-incorporation
  tables so the gate need not class them afterward. *(A Q2; B Q-B101; C's question 206.)*
- **Q-326 · (Gate 8)** The place-specific standout beside SC-1: SC-4 (A) or SC-3 (B, C)? *Recommended:* SC-4, the archive's two signals: it
  stands on a ratified line (spec L179) and on Phase 9 and 10 findings, while SC-3 rests on PROPOSED readings and absences; record SC-3
  beside it, and SC-4's no-signal leg as a contested absence wherever it is cited. *(A Q1; B Q-B107; C's question 207.)*
- **Q-327 · (Gate 9, shadow candidate)** Membership held by the road or a chamber (A15). *Recommended:* yes, reserved beside SH-35 and
  SH-37, weaker than textbook (no adverse outcome written); no practice. *(A Q4.)*
- **Q-328 · (Gate 9, shadow candidate)** No written way into the research population for a resident outside it (FIND-P9-36; RF-183).
  *Recommended:* write that how such a resident is first asked is not written; keep RF-183; hold it as a candidate, no rule. *(A 16.)*
- **Q-329 · (Gate 9, shadow candidate)** A long pause carries the research population across the city's one between-group line (kept, not
  needed). *Recommended:* yes, reserved, conditional on REQ-145 and on FIND-P9-36's line; no rule. *(A Q5.)*
- **Q-330 · (Gate 9, shadow candidate)** Link Phase 6 SH-25 (the keepers of heat stand in no record) to FIND-P10-1 (the one honor names the
  scientists) as one candidate? *Recommended:* yes, reserved; no honor, roll or practice written. *(A Q6.)*
- **Q-331 · (Gate 9, shadow candidate)** The clean side's way out is unwritten (CAT-B1-1). *Recommended:* reserve it with RF-194 for the
  DCI, and write its losing side, the one who cannot complete instruction (Phase 7 FIND-P7-36), with it. *(A 19; B.)*
- **Q-332 · (Gate 9, shadow candidate)** FIND-P10-15's request path: the unanswered sender. *Recommended:* yes, weaker than textbook; who
  decides which requests are answered waits for the DCI, and the unanswered sender is written beside the one who comes in person. *(B
  Q-B108.)*
- **Q-333 · (Gate 9, shadow candidate)** The unchosen successor in single custody (FIND-S5-7). *Recommended:* yes, weaker than textbook,
  reserved with RF-212. *(C's question 204.)*
- **Q-334 · (Gate 11)** C's FAIL on yearly lifting against A's and B's FLAG; and carry the tonnage and the induction-scale question to Step
  10? *Recommended:* the FAIL stands until ERR-82 is applied; carry the city-scale pricing of raising (about 990,000 to 1,417,500 tonnes of
  snow a year on the 44–63 km² extent) and the scale question on perpetual induction to Step 10 as pricing and scale notes, not findings;
  the shared-night plausibility point goes with Q-255. *(A Q7.)*
- **Q-335 · (Gate C)** Is a dated correction to a shared sheet within Gate C's applied-list rule, or a Gate 0 matter (B)? *Recommended:*
  within it: a statement corrected at one source is corrected wherever it is carried; record the datasheet's L21 under Gate 0 as well;
  ERR-87 stands either way.
- **Q-336 · (Gate I)** Reclass Phase 9 FIND-P9-35 (the order of arrival) from genuinely emergent to inflected? *Recommended:* yes: it
  inflects the national mentor bond, cited in the finding itself, and Phase 2's perpetual induction; the substance is unchanged (with
  Q-307). *(A Q3.)*
- **Q-337 · (The station-builder scan)** Phase 9 L202, a method bar that names the operator before denying it. *Recommended:* rewrite it to
  the positive rule, "Founders come only from the Founding Register (`DR-19`)."; nothing is lost. *(B Q-B109; A and C hold it as method.)*
- **Q-338 · (The station-builder scan)** Step 5 DK-3 proposes keeping the culture sheet's sentence that the station operators' nation has no
  representation in any tier. *Recommended:* strike it from the sheet's prose: a census row count needs no mention of whose station it was
  (`DR-19`; runbook L2944). *(A Q8; C's question 205; B clears it.)*
- **Q-339 · (Gate 3)** Add to Q-225's scope the other lines that carry city-scale staying (Phase 9 FIND-P9-33's heading L330, Phase 9 L254,
  Phase 9 L413, Phase 10 Q-B2-2's reason L1916 and Q-211's premise L1208)? *Recommended:* yes; each to read "no departure from the city is
  written" and, for the human, "could not return to Upper Earth"; the same rule as Q1's Gate 9 errata (Q-295). *(B Q-B104; A A11.)*

---

## 8 · Found by / confirmed by

*Found by* is the reader or readers who wrote it in Round 1; *confirmed by* is a reader who agreed in Round 3 (or Round 1). A **1** marks a
single-reader find written under the merge rule's UNION and credited to its finder.

| # | Find | Sub-unit | Found by | Confirmed by | 1 | Written as |
|---|---|---|---|---|---|---|
| 1 | Treaty-draft tags missing (P3 L11; P2 L11) | Q1 | B | A, C | 1 | ERR-1, ERR-2 |
| 2 | Question tables before `DR-143` | Q1 | B | (c) | 1 | Q-288 |
| 3 | Run-modes L105 against L109 | Q1 | A | B, C | 1 | REQ-207 |
| 4 | `DEC-716`'s source | Q1 | A, C | B | | REQ-208 |
| 5 | Merge-rule span cited two ways | Q1 | C | A, B | 1 | REQ-209 |
| 6 | 256 against 284 web calls | Q1 | A | C | 1 | REQ-210 |
| 7 | Index misses (Q1's eleven) | Q1 | A, B, C | | | REQ-205 |
| 8 | Sweep vocabulary gaps | Q1 | A, B, C | | | REQ-206 |
| 9 | LAW 0-P candidate coverage at Step 3 | Q1 | C | A | 1 | Q-289 |
| 10 | Darkness at rest written for every body | Q1 | A | B, C | 1 | ERR-3 to ERR-6 |
| 11 | Spine L392's research readings unscoped | Q1 | B | A, C | 1 | ERR-7 |
| 12 | No research target on the robot majority's needs | Q1 | B | A | 1 | Q-290 |
| 13 | The baselines like for like (16,032 workers) | Q1 | C | | 1 | REQ-211 |
| 14 | Where emissions land | Q1 | B, C | A | | REQ-212 |
| 15 | The stores against the archive's holdings | Q1 | C | (c) | 1 | Q-292 |
| 16 | "No one leaves" from RF-30's silence | Q1 | A, B | C | | ERR-8 to ERR-16 |
| 17 | Spine L229, FIND-25's heading, RF-104 in that set | Q1 | B | A, C | 1 | ERR-8, ERR-10, ERR-16 |
| 18 | FIND-P3-45's losing side | Q1 | A, B, C | | | Q-293 |
| 19 | RF-24 may close | Q1 | A | | 1 | Q-294 |
| 20 | One source for "no term" | Q1 | A | | 1 | Q-295 |
| 21 | DS12 L35 lags `DEC-691` | Q1 | A, B, C | | | ERR-17 |
| 22 | DS12 L17, L26, L34 lag | Q1 | A | B, C | 1 | ERR-18, ERR-19 |
| 23 | DS2 L16 lags census L440 | Q1 | C | A, B | 1 | ERR-20 |
| 24 | The `06` quarantine and the genetics folder | Q1 | A | B, C | 1 | Q-296 |
| 25 | Lake length; 90% retention | Q1 | C | B | 1 | Q-298 |
| 26 | Crew life against Q-63 | Q1 | B | (c) | 1 | Q-297 |
| 27 | The borehole's history rests on Q-63 | Q1 | A | | 1 | Q-297 |
| 28 | P3 L317 places the institutions in the district | Q1 | B | A, C | 1 | ERR-21 |
| 29 | G7's provenance | Q1 | C | (c) | 1 | Q-299 |
| 30 | FIND-P2-46 and its companions | Q1 | A, B, C | | | ERR-22 |
| 31 | P2 L210 denial | Q1 | A, C | B | | ERR-23 |
| 32 | P2 L195 denial | Q1 | A, C | (B (c)) | | ERR-24 |
| 33 | Spine L187; P3 L274 | Q1 | C | B | | ERR-25, ERR-26 |
| 34 | Spine L109 | Q1 | C | (c) | 1 | ERR-27 |
| 35 | DS-P7 L35 (and L56) naming the builder's nationality | Q1, Q2 | Q1 A; Q2 A | Q2 B | | REQ-213 |
| 36 | Q1's vocabulary hits | Q1 | A, C | B | | ERR-28 to ERR-37 |
| 37 | `Highways.md` owns the 1,260 km | Q1 | B | | 1 | REQ-214 |
| 38 | The spine's 18,140 workers | Q1 | B | | 1 | REQ-215 |
| 39 | P4 L23's count | Q2 | C (A noted) | A, B | | Q-302 |
| 40 | P7 L34's span count | Q2 | B | C | 1 | REQ-216 |
| 41 | Refuse and waste unwritten | Q2 | A | (B (c)) | 1 | Q-303 |
| 42 | Index misses (Q2's eight) | Q2 | B, C (A six) | A | | REQ-205 |
| 43 | Sweep misses a line wrap (P7 L576–577) | Q2 | A, B, C | | | REQ-206; ERR-67 |
| 44 | Sweep misses a first-word plural (P5 L367) | Q2 | B | A, C | 1 | REQ-206; ERR-62 |
| 45 | P6 L242 survival layer "all 441,378" | Q2 | B, C | A | | ERR-38 |
| 46 | P7 L815–816 every resident teaches | Q2 | B | A, C | 1 | ERR-39 |
| 47 | P4 L309 the shared night | Q2 | B, C | A | | ERR-40 |
| 48 | P4 L360 item 3 | Q2 | C | A, B | 1 | ERR-41 |
| 49 | P5 L377 every body arrives | Q2 | C | (B (c)) | 1 | ERR-42; Q-304 |
| 50 | Coolant on the melt account | Q2 | A | B, C | 1 | ERR-43 |
| 51 | Siligel by Hwy 37 stated flatly | Q2 | A | B, C | 1 | ERR-44 |
| 52 | What anyone meets in a day | Q2 | A | B, C | 1 | ERR-45 |
| 53 | The largest unwritten work | Q2 | A | B, C | 1 | ERR-46 |
| 54 | Every death a resident's | Q2 | A | B (C (c)) | 1 | ERR-47; Q-305 |
| 55 | Departure as impossibility | Q2 | B | A, C | 1 | ERR-48 |
| 56 | The world clock | Q2 | B | A, C | 1 | ERR-49 |
| 57 | The shaft left out of P6 L430 | Q2 | B | A, C | 1 | ERR-50 |
| 58 | Fresh food grown here | Q2 | C | A, B | 1 | ERR-51 |
| 59 | Electricity listed as received | Q2 | A, C | B | | ERR-52, ERR-53 |
| 60 | One electric supply | Q2 | A | B, C | 1 | ERR-54 |
| 61 | The unpeopled corridor without its condition | Q2 | A | B, C | 1 | ERR-55 |
| 62 | Spec L159 cited | Q2 | A, B, C | | | ERR-56 |
| 63 | P6 L217–220 denial | Q2 | A, B | C | | ERR-57 |
| 64 | Q2's vocabulary hits | Q2 | A, B, C | | | ERR-58 to ERR-73 |
| 65 | One mechanism, five names | Q2 | A, B, C | | | Q-307 |
| 66 | The shaft's watch in two rows | Q2 | C | A, B | 1 | Q-308 |
| 67 | Heat and charge in two tiers | Q2 | A | (c) | 1 | Q-306 |
| 68 | Membership can lapse | Q2 | A | B, C | 1 | Q-309 |
| 69 | *Never a filter* against belonging | Q2 | A | B, C | 1 | Q-310 |
| 70 | The shaft's closure when the purpose yields | Q2 | B | A, C | 1 | Q-311 |
| 71 | No entry point for the built or born here | Q2 | B | A, C | 1 | Q-312 |
| 72 | The last arrival | Q2 | C | A, B | 1 | Q-313 |
| 73 | The Panel's disposition used early | Q2 | C | (c) | 1 | Q-314 |
| 74 | Universe-repo negatives | Q2 | B, C | A | | REQ-219 |
| 75 | Spec L17 to check | Q2 | B | C | 1 | REQ-217 |
| 76 | §23's narrative premise | Q2 | B | C | 1 | REQ-221 |
| 77 | The outpost's grid power at the height | Q2 | A | (c) | 1 | Q-315 |
| 78 | Spec L221 | Q2 | B | | 1 | REQ-218 |
| 79 | Band variance in P5 and P8 | Q2 | C | | 1 | REQ-220 |
| 80 | Step 6 L318, nine of ten | Q3 | A, B | C | | ERR-74 |
| 81 | Rows 31 and 84 classed apart | Q3 | A, B, C | | | ERR-75; Q-316 |
| 82 | Phase 10 L42–44's status claim | Q3 | B | A, C | 1 | ERR-76 |
| 83 | RF-182's credit cell | Q3 | B, C | A | | ERR-77 |
| 84 | The Step 7 datasheet L21 | Q3 | A | B, C | 1 | ERR-87 |
| 85 | Phase 10 L1025's Parent mark | Q3 | B | | 1 | Q-317 |
| 86 | The catalog's research-role lean | Q3 | C | A, B | 1 | Q-318 |
| 87 | CAT-1 "paid daily" | Q3 | A | B | 1 | Q-319 |
| 88 | CAT-39 | Q3 | B | A, C | 1 | ERR-78 |
| 89 | Phase 4 L264 | Q3 | A | B, C | 1 | ERR-79 |
| 90 | Step 5's pre-narrowing "never goes quiet" | Q3 | A | B, C | 1 | ERR-80 |
| 91 | CAT-26's source | Q3 | A | B (C (c)) | 1 | ERR-81; Q-322 |
| 92 | Lifted every year | Q3 | C | A, B | 1 | ERR-82 |
| 93 | Phase 4 L196 | Q3 | C, A | B | | ERR-83 |
| 94 | Phase 9 L348 and L278 | Q3 | A, C | B | | ERR-84 |
| 95 | No sky edge against the noon twilight | Q3 | B | (c) | 1 | Q-320 |
| 96 | FIND-P10-9 | Q3 | B | (c) | 1 | Q-321 |
| 97 | City-scale staying lines | Q3 | A, B | | | Q-339 |
| 98 | The axis's peer-free "Yes" | Q3 | A | (c) | 1 | ERR-85; Q-323 |
| 99 | The baseline gap unstated in Q3's files | Q3 | C | A | 1 | REQ-211 |
| 100 | CAT-35 and CAT-78 doubles | Q3 | A, C | B | | ERR-86 |
| 101 | One research program under two names | Q3 | B | A, C | 1 | Q-324 |
| 102 | The other catalog doubles | Q3 | B | C | 1 | Q-324 |
| 103 | Rows 43 and 45 rest on CAT-B2-8 | Q3 | A | B | 1 | Q-325 |
| 104 | SC-4 as the place-specific standout | Q3 | A | | 1 | Q-326 |
| 105 | Membership held by the road or a chamber | Q3 | A | B | 1 | Q-327 |
| 106 | No way into the research population | Q3 | A | B | 1 | Q-328 |
| 107 | The long pause | Q3 | A | B | 1 | Q-329 |
| 108 | The honor and the keepers of heat | Q3 | A | B | 1 | Q-330 |
| 109 | The clean side's way out | Q3 | A | B | 1 | Q-331 |
| 110 | The request path | Q3 | B | (c) | 1 | Q-332 |
| 111 | The unchosen successor | Q3 | C | B | 1 | Q-333 |
| 112 | The raising tonnage | Q3 | A | B | 1 | Gate 11; Q-334 |
| 113 | Induction at city scale | Q3 | A, B | | | Gate 11 |
| 114 | The shared night for every robot | Q3 | B, A | (C gives way) | | Gate 11 |
| 115 | Canon cited at second hand | Q3 | B | C | 1 | REQ-225 |
| 116 | §23's "Canon §15" | Q3 | C | | 1 | Gate C (Q-262) |
| 117 | 324,452 against 324,453 | Q3 | A | B | 1 | REQ-226 |
| 118 | FIND-P9-35 classed emergent | Q3 | A | B | 1 | Q-336 |
| 119 | The shared night unclassable | Q3 | C | B | 1 | Gate I |
| 120 | Phase 9 L212; CAT-38; Step 6 L299 | Q3 | A, B | (C lists them) | | ERR-93 to ERR-95 |
| 121 | Phase 9 L202 | Q3 | B | (c) | 1 | Q-337 |
| 122 | DK-3's "keep" | Q3 | A, C | (B clears) | | Q-338 |
| 123 | RL-31's denial form | Q3 | B | C | 1 | REQ-227 |
| 124 | "Unspeakable" at Phase 9 L396 and L462 | Q3 | B | A, C | 1 | §5 |
| 125 | The sun's path, to research | Q3 | B | | 1 | REQ-228 |
| 126 | Phase 9's sweep places, not reached | Q3 | B | | 1 | REQ-224 |
| 127 | Gate 3 rows outside every sub-unit | Q3 | A, B | | | REQ-223 |

**Single-reader finds credited: 92.**

---

## 9 · Splits settled

| Gate | Split | Settled as | Why |
|---|---|---|---|
| 0 (Q1) | B FAIL; A, C FLAG | **FAIL** | A and C conceded B121, B122 in Round 3 |
| 0 (Q1) | B126 a FAIL | **a developer question** (Q-288) | true when written; the audit's §5 records the reconciliation (orchestrator; A and C (c)) |
| 1 (Q1) | C FLAG; A, B PASS | **FLAG** | A agreed; B and C put it to the developer (Q-289) |
| 2 (Q1) | A FAIL; B FLAG; C PASS | **FAIL** | B and C conceded |
| 4 (Q1) | three weakest findings | **a developer question** (Q-291) | all three hold on their partners |
| 5 (Q1) | B, C FLAG; A PASS | **FLAG** | A conceded |
| 6 (Q1) | C FLAG; A, B PASS | **FLAG** | not withdrawn; (c) (Q-292) |
| 9 (Q1) | A, B FAIL; C FLAG | **FAIL** | C conceded |
| F (Q1) | B FAIL; A, C PASS | **FAIL** | A and C conceded |
| G (Q1) | B FLAG on spine L173; A PASS | **withdrawn** | B withdrew in favor of A's cell-level reading |
| G (Q1) | C FLAG on the picks' provenance | **FLAG** | kept; (c) (Q-299) |
| Station-builder (Q1) | P2 L195: A, C FAIL; B cleared | **FAIL stands** | not withdrawn; the reach is Q-300 |
| Station-builder (Q1) | Spine L109, L187; P3 L274: C FAIL; A, B borderline | **FAIL stands** | not withdrawn; B agreed under a strict reading; Q-300 |
| Station-builder (Q1) | Q-75's answer: A, B FAIL; C cleared | **FAIL** | C gave way |
| Station-builder (Q1) | FIND-P2-46: rewrite (A, B) or withdraw (C) | **a developer question** (Q-301) | both remove the denial |
| Sweep (Q1) | B cleared six hits; A, C real | **real** | B conceded; plain language binds finding prose |
| Sweep (Q1, Q2) | Q1 B expected the plural "standing costs" missed; Q2 tested P8 L293 | **a last-word plural is caught** | settled by the test, the narrower claim |
| I (Q1) | single calls differ | **no change** | all three counts under 3:1 |
| 0 (Q2) | C FLAG; A, B PASS | **FLAG** | A and B conceded; the resolution is Q-302 |
| 1 (Q2) | A FLAG; B, C PASS | **FLAG** | C conceded; B put the refuse point to the developer (Q-303) |
| 2 (Q2) | A PASS; B, C FAIL | **FAIL** | A conceded |
| 2 (Q2) | P5 L377: C FAIL; B (c) | **FAIL stands** | not withdrawn; Q-304 |
| 3 (Q2) | Every death: A FAIL; C (c) | **FAIL stands** | not withdrawn; B agreed, minor; Q-305 |
| 5 (Q2) | A, C FAIL; B PASS | **FAIL** | B conceded |
| C (Q2) | A, C FAIL; B FLAG | **FAIL** | B conceded |
| 6 (Q2) | Heat and charge: A FLAG; B cleared | **FLAG** | (c) (Q-306) |
| Index (Q2) | six (A) or eight (B, C) | **eight** | the two A missed were shown at source |
| I (Q2) | The turn of instruction: B originated; A, C inflected | **inflected** | B conceded (RP L418) |
| Station-builder (Q2) | P6 L217: A, B FAIL; C FLAG | **FAIL** | C conceded |
| Station-builder (Q2) | P5 L279, P8 L229, P6 L380; the world clock as a builder hit | **developer questions** (Q-300) | all three (c) |
| F (Q2) | The grid at the height: A FLAG alone | **a developer question** (Q-315) | (c) |
| 10 (Q2) | B "N/A"; A, C NOT RUN | **NOT RUN** | brief §2 |
| Label (Q2) | C's "Raw output, whole" | **an excerpt** | it is the sweep's L33–51 (orchestrator) |
| 0 (Q3) | Step 6 L318: A, B FAIL; C confirmed | **FAIL** | C conceded |
| 0 (Q3) | Row 84: taken (A, B) or moved (C) | **FAIL on the inconsistency; which way is Q-316** | (c) |
| 0 / C (Q3) | The datasheet L21 under Gate 0 or Gate C | **written under Gate C, cited from Gate 0** | A's FAIL not withdrawn; B's reading is Q-335 |
| 2 (Q3) | C FLAG; A, B PASS | **FLAG** | A and B conceded |
| 3 (Q3) | CAT-26: A FAIL; C (c) | **erratum and a developer question** (Q-322) | it rests on one reader's off-list read |
| 3 (Q3) | No sky edge; FIND-P4-40 (A amend, B docket, C clear) | **a developer question** (Q-320) | substance agreed |
| 3 (Q3) | FIND-P10-9: B narrows; C consistent | **a developer question** (Q-321) | (c) |
| 4 (Q3) | A FAIL; B PASS; C FLAG | **FAIL** | A did not withdraw; Q-323 |
| 4 (Q3) | three weakest findings | **a developer question** (Q-323) | (c) |
| 5 (Q3) | C FLAG; A, B PASS | **FLAG** | A conceded; B (c), minor |
| 6 (Q3) | A FAIL; B FLAG; C PASS | **FAIL** | A did not withdraw; C conceded; B's objection is Q-324 |
| 6 (Q3) | CAT-35 folded (A, C) or cross-referenced (B) | **a developer question** (Q-324) | (c) |
| 6 sub. 4 (Q3) | A, B FAIL; C confirmed | **FAIL** | C conceded |
| 7 (Q3) | A 25–28 of 86; B 31 of 86; C 27 of 85 | **27 of 85 = 31.8%** | B withdrew; supporting convergences are ornament; row 86 is unresearched; the remaining choices are Q-325 |
| 8 (Q3) | SC-4 (A) or SC-3 (B, C) as the place-specific standout | **a developer question** (Q-326) | SC-1 confirmed by all three |
| 9 (Q3) | Seven candidates from three readers | **union** | none contradicts another; each is a question |
| 11 (Q3) | C FAIL; A, B FLAG | **FAIL** | C did not withdraw; Q-334 |
| 11 (Q3) | The shared night for every robot: B flags; C clears | **flagged** | C's clearance gives way (orchestrator) |
| 11 (Q3) | Induction at scale: A, B flag; C clears | **flagged** | two readers; C gave way |
| C (Q3) | A FAIL; B, C FLAG | **FAIL** | A did not withdraw |
| I (Q3) | FIND-P9-35 reclass: A; C (c) | **a developer question** (Q-336) | B agreed |
| Station-builder (Q3) | C FLAG; A, B FAIL | **FAIL** | C's FLAG gives way |
| Station-builder (Q3) | Step 6 L299: A FAIL; B FLAG | **FAIL** | the more conservative view |
| Station-builder (Q3) | Phase 9 L202 as method | **a developer question** (Q-337) | (c) |
| Station-builder (Q3) | DK-3: strike (A, C) or keep (B) | **a developer question** (Q-338) | (c) |
| Across sub-units | Q2 C's "last arrival" as new; Phase 9 SH-35 | **already reserved** (Q-313) | SH-35 (L475) writes it |
| Across sub-units | Q1's FIND-P3-45 losing side; Phase 7 FIND-P7-36 | **written for being kept** (Q-293) | the belonging half is Q-310 |
| Across sub-units | Q2 B's spec L17 request; Q3 B's read of spec L17 | **answered** (REQ-217) | 156,685 / 284,693 / 441,378 at source |
| Across sub-units | Q2 B's entry point; Phase 9 FIND-P9-13 | **answered in part** (Q-312) | a robot built here is written conditionally; the born-here human stays a null |

Nothing in this file is declared complete or ready. Every verdict, erratum and recommended answer is PROPOSED.

