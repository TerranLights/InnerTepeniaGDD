# Davis — `T8` ROUNDS, STEP 2 · RAW

**The evidence `02_Spine.md` rests on.** *Nothing here is edited for presentation. Written 2026-09-15.*

> ## ⭐⭐⭐ THIS IS `T8`'s FIRST REAL INVOCATION — and therefore its own BASELINE (`§N.6`)
> **`§N.5` states the falsification condition in advance:** *T8 is FALSIFIED if, across several real invocations,
> **"`Round 2` and `Round 3` always pass trivially, unanimously, on the first try"*** — *"then the gate adds cost
> without adding signal, exactly the failure Gate 4 already names."*
>
> ### ⛔ IT DID NOT PASS TRIVIALLY.
> **Round 1 produced THREE substantively different drafts, including TWO DIFFERENT SPINES and a contested shape
> verdict. Round 3 caught EIGHT defects — at least one in every reader, plus one in the dispatch brief itself.**

---

# THE THREE ROUNDS — results table

| Round | What it does | Result |
|---|---|---|
| **1** | Three readers, dispatched in parallel on an identical range-aware brief, no knowledge of each other | **3 drafts.** A: 1,340 lines · B: 967 · C: 1,091 |
| **2** | `Tools/triple_read_verify.py` — mechanical ground truth against the bytes on disk | ✅ **`UNANIMOUS — CLEARED TO WRITE`. 30 of 30 field-sets byte-exact** (3 readers × 10 files) |
| **3** | Peer cross-check — the SAME three agents continued by `SendMessage`, context intact | ✅ **All 6 cross-verdicts `CONSISTENT`** · **4 splits put explicitly · 3 resolved · 1 logged unresolved** |

## ⭐ WHAT ROUND 3 CAUGHT — eight defects, and the last is the important one

| # | Defect | Held by | Caught by | Outcome |
|---|---|---|---|---|
| **1** | Shape read as `COST-DOMINANT` | A | A itself, on B's and C's arguments | **WITHDRAWN → `BALANCED` 3–0** |
| **2** | `410 km²` conflated with the spec's `~400 km²` | A | **B and C independently** | **Struck** |
| **3** | `MANDATED`/`FREE` read as in-world compulsion — a layer error | **A and C** | B | **Struck; rebuilt on `35 > 25`** |
| **4** | `G2 × G3` called "substantially independent" | C | **A and B independently** | **Struck — partially DEPENDENT** |
| **5** | Founding deficit addressed `IN ITS OWN PAST` | C | A | **Replaced by B's two-part split** |
| **6** | A queue inferred at the exit — mechanism where fire #1 records a hole | B | C | **STRUCK** |
| **7** | Notable tier counted as 14 nations | C | A | **Corrected to 13** |
| **8** | ⭐⭐ *"Residents understand themselves as researchers"* | ⚠ **THE DISPATCH BRIEF** | **B, then A and C** | **KILLED on the source** |

> ## ⭐⭐⭐ DEFECT 8 — **T8 CAUGHT AN ORCHESTRATOR ERROR, WHICH IS NOT WHAT IT WAS DESIGNED FOR**
> **It did not originate with any reader.** It was handed to all three **as an established bound in the dispatch
> brief**, inherited from `00_Frame.md` §0.7 and ultimately from the Step −1 contract.
> ⛔ ***`Specs/Davis.md` L143 contains no self-understanding at all, and calls the research half a `heritage`.***
> **Two readers killed it independently — one by reading the line closely, one by showing the two roles are two
> depths of one method rather than two tribes.**
> ### ***A reader given a false premise as an established fact refused it on the source.***

## ⚠ THE ONE SPLIT THAT DID NOT CONVERGE

**D6 — *cannot make its own plant*.** **A and B SWAPPED positions in cross-check, each deferring to the other's
original view.** Final: **A `IN THE PARENT` · B `DIFFUSE` · C `IN THE PARENT`.** ⛔ **Logged, not forced to a
verdict — 2–1 with the minority holding the stronger argument is exactly the case `§N.2` says to record rather
than resolve by headcount.** *Full reasoning: `02_Spine.md` §5.3.*

---

# ⛔ ROUND 2 — MECHANICAL GROUND TRUTH, RAW OUTPUT

**Command:**

```
python3 Tools/triple_read_verify.py \
  Davis/.t8_required_step2.txt \
  Davis/.t8_step2_readerA.md  Davis/.t8_step2_readerB.md  Davis/.t8_step2_readerC.md
```

> ### ⭐ AND THE INSTRUMENT WAS VERIFIED BEFORE IT WAS TRUSTED — `M-225`
> **On 2026-09-14 this same script returned a FALSE `⛔ NOT UNANIMOUS` on all three readers**, caused by two
> defects *(an unterminated `parse_proof()` continuation rule, and an unstated `LLAST` convention)*. **Both were
> patched.** ⛔ **A patch present is not a patch working**, so before Round 2 was trusted it was run against two
> controls:
>
> | Control | Expected | Result |
> |---|---|---|
> | Three honest readers, **blank `LLAST`** + content after the final `QUOTE` *(the exact 2026-09-14 failure shape)* | CLEARED | ✅ **`UNANIMOUS — CLEARED TO WRITE`** |
> | Two honest + one with a **fabricated `LMID` and a fabricated `QUOTE`** | CAUGHT | ✅ **`⛔ NOT UNANIMOUS`**, both fields flagged by name |
>
> ***A gate that only ever passes is not a gate.*** **This one clears an honest reader and catches a fabricated
> one, and both were demonstrated on this step, before the real run.**

```
required files: 10
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2497-2525] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Davis.md  [range 1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Energy_Grid_Failure_Rationale.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Davis.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 392-398,496,613] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

---

# ⭐⭐ ROUND 3 — PEER CROSS-CHECK, RAW

**Design: the LIGHTWEIGHT form, per `§N.1`.** ⛔ **Not three fresh cross-checkers** — **the same three Round-1
agents, continued by `SendMessage` with context intact**, so each was comparing against files it had genuinely
just read rather than against a cold read of a summary. *(Corrected 2026-09-14: a prior session had been running
an expensive fresh-dispatch variant that the recipe never specified.)*

**Each reader received:** the other two readers' full output paths, the four standard `T8_CROSSCHECK_PROMPT`
questions, and **the four substantive splits, named explicitly** — with the instruction *"do not converge for the
sake of converging: if you still think you are right after reading their reasoning, say so and say why. If they
have changed your mind, say that plainly — changing your mind on a stated argument is a result, not a failure."*

---

## ROUND 3 · READER A's CROSS-CHECK — verbatim

**READER B — CONSISTENT.**
1. Read-confirmed: B's `72.8 falls / ~28 lands / ~44.8 lost / 38.5%` and freeze–thaw pair (Jan +3.2/−1.2, Dec +2.4/−2.2) match `Specs/Davis.md` L84–86, L95, L106, and my own summation of L95–106 to exactly 72.8.
2. Passage-dependent claims, all found: "~324 GW net… continent-scale flywheel" = `Energy_Grid_Failure_Rationale.md` L61–73; "skiway usable only by ski-equipped aircraft" = airstrips L99. B's snag — tool line numbers vs `awk` on `02` — I hit independently; `awk`/`wc` both return **760**.
3. No contradictions found.

**READER C — CONSISTENT (reads verified; one interpretive error).**
1. Read-confirmed: C's "Mar–Jun 38.2 mm, 52%; Nov–Feb 9.7 mm, 13%" reproduces from L95–106 (I got 52.5% / 13.3%); "281,800 not in the workforce" matches my 1,158,314 − 876,514.
2. Passage-dependent: C's Saint-exclusion citation is real (L131) — but it sits inside fire #6's roster-rule-only guard and reserved item 1. Used as evidence, not as a custom: legal, but watch it.
3. **Contradiction:** C §1.1 calls G2×G3 "substantially independent." L143 states the derivation in its own sentence — *"Davis's own unique geography… genuinely fits it for the… role."* B and I both found this. C is wrong here.

**SPLIT 1 — SHAPE. I withdraw cost-dominant.**
C's objection lands, but not for C's stated reason (`02` defines the shape structurally, not by type). It lands via **`02` §3.1**: standing cost is *"what it must pay regardless of function."* A production **mandate is an obligation on output — function, not cost.** I loaded the cost quadrant with something that belongs in the strength/function register. **BALANCED on both sets, 3-0.** My cost-absent sub-structure survives and is now three-way independent: B ("the balance is what conceals the one unbalanced thing"), C ("the one genuinely cost-absent-shaped item"), me (§3.5's bimodal signal split).

**SPLIT 2 — CHOSEN/SELECTED. Reconcilable; I move.**
- **Vocation:** B is right and I was wrong. L143's own word is *"heritage,"* and both clauses are parent-facing. I carried "residents understand themselves as researchers" from `00.1` without testing it against the line. Conceded.
- **Departure:** B's **motive elective / sequence allocated** split subsumes all three. My 126,176-human argument (B reached it independently) refutes selection-*on-capability* — C correctly notes that does not establish election. Adopt B's formulation.
- **Residue:** adopt B's forbidden-wording rule. My §7.3 phrase *"those for whom the arrangement held"* fails it. Withdrawn.
- **Arrival = assigned:** C and I agree; unopposed.

**SPLIT 3 — G3. B is right; C and I made the same mistake.**
G2×G3 partially dependent: 2-1, me and B. But my *rescue* of G3 on the MANDATED labels is the same move C made, and B killed it correctly on `01` §1.1's layer ruling and fire #11 ("production weight, not a social fact") — the sheet's own FULL/HALF definition is outside the admissible set. What survives is **B's version: the 35-vs-25 percentage asymmetry**, in-world-readable. **Rule-of-three count unchanged** — satisfied by G2+G4+G8 alone under all three readings; G3 stays a half-independent fourth.

**SPLIT 4 — DEFICITS. Chunking, plus two real address errors — mine.**
Water: 3-0, *nowhere at all*. Equipment: **B is right, IN THE PARENT** — a counterparty exists at a scale above; I wrongly said diffuse.
Founding-knowledge: **my DIFFUSE is correct for the deficit I named** (unrecorded live competence). **C's IN ITS OWN PAST is defeated by C's own evidence check** — C writes *"they were never here,"* but §4.1's address means the location *had* the capacity and *lost* it. Davis never had it. B's split (D-3a past-and-remedied / D-3b diffuse) is the cleanest.
Same charge against myself: **my D5 (exit mechanism, "in its own past") is wrong for the identical reason** — withdrawn, merges into D7 as diffuse. And C's D5 (no arrival narrative, fire #3) is a real deficit I omitted.

---

## ROUND 3 · READER B's CROSS-CHECK — verbatim

**READER A — CONSISTENT**
1. Yes. Confirmed: *"126,176 humans departed — 22.39%"* (A §7.2). Census L496/L613: 563,599 − 437,423 = 126,176; ÷563,599 = 22.39%. A's daylight arithmetic also reproduces (147.6 h total; Oct–Feb 100.7 = 68.2%; May–Jul 6.6 = 4.5%).
2. A quotes the airstrips caveat *"conditions/operators can change year to year"* — found, `Antarctic_Stations_With_Airstrips.md` L5. A cites `00_Frame.md`'s era-file rule *"how hard a given place used that exit"* — found, L268. Nothing unlocatable.
3. ⛔ One: A writes **"410 km² of ice-free exposed rock"** (§2.1c, §2.1, §8) and asserts 410 and ~400 are "the same figure at lower precision." `Specs/Davis.md` L60 gives ~400 km² of exposed rock; 410 km² is the extent, *closed by the coastline ruling*, not an oasis measurement. Two objects, one of which A's spine clause rests on.

**READER C — CONSISTENT**
1. Yes. Confirmed: *"281,800 people, roughly a quarter of the city, are not in the workforce"* — 1,158,314 (L496) − 876,514 = 281,800. C's Nov–Feb precipitation 9.7 mm (2.2+1.9+1.8+3.8) also reproduces.
2. C cites the physiological-mismatch statement to `Energy_Grid_Failure_Rationale` §8 — found, L41–43, correctly bounded away from the post-war narrative.
3. No contradiction of fact. One disagreement of reading: C marks G2×G3 *"substantially independent"* without addressing L143's own derivation clause (*"its geography genuinely fits it for the role"*). That is Split 3's territory, not a misread.

**SPLIT 1 — SHAPE.** Balanced survives; I am not moved on the label, and I am moved on A's methodology finding. A routes *function* into STANDING COST, which `02` §3.1 forbids in terms: *"A location's function is what it is for. Its standing cost is what it must pay regardless of function."* A 35% share of workforce is a division of work, not a continuous maintenance obligation. And §4's test is "largest quadrant," not "gained a register" — admitting the tiers also thickens STRENGTH and DEFICIT. A's own composite (*cost-dominant in what can report, cost-absent in what cannot*) concedes no single label fits, which is my §5.2. ✅ Endorse A's transferable finding: *inert numeric obligation data is shape-determining*. Record A as reasoned minority.

**SPLIT 2 — CHOSEN/SELECTED.** Reconciling frame, not a fourth position. All three of us already agree on the gate (A: "no claim as to the gate"; C: voice-neutral; me: queue, unknowable). A's arrival-assigned half is right and I under-stated it. C's voice-neutrality is too strong at the **act**: 22.39% human departure is positive evidence no capability selection produces — absence of a gate is not absence of an act. But C's *cause* — Davis has never held an organ that decides about people — I adopt; it explains why the gate is unwritten and strengthens my residue refusal. Joint: **arrival assigned · act elected · gate unwritten · residue not resolvable.**

**SPLIT 3 — G3, objection stated for refutation.** `MANDATED/FREE` is an undefined label in a project-internal sheet whose legend is in nobody's admissible set. It reads two ways: an in-world obligation, or an authoring status (fixed-by-canon vs. designer-free). `01` §1.1's layer ruling and fire #11 (*"a production weight, not a social fact"*) both require the in-world reading to be **earned**. It has not been. **Refute by producing the sheet's legend or a ratified line where the Federation imposes sector obligations.** What survives regardless: 35 > 25 and industrial 5% — a division of labor, in-world-readable. C's upgrade survives *restated as weight, not compulsion*; C's conclusion (*Davis elected neither vocation*) survives on better ground — L143 calls research a **heritage** and both clauses are parent-facing. ⚠ The objection also hits A: A's rescue of G3's independence is the obligation register, so G3 stays **half-independent**.

**SPLIT 4 — COUNT.** Mostly granularity, one real loss for me. Water: nowhere ×3, **3-0**. Arrival/descent: diffuse, agreed. Shortfall/failure-state: parent, agreed (I had it as shared silence). Transmission: my past+diffuse split is exactly the union of C's *own past* and A's *diffuse* — I keep the split; it reconciles them. **I change my mind on one:** the equipment deficit. A's ground is better — the admitted set names no supplier, so "above Davis" ≠ "in the parent." **My D2 moves from `in the parent` to `diffuse`** (classes still 4). A and C both enumerate *no refusal/unsponsored channel* as a row; I reached the same content as the count's result. Their placement is better. Reconciled: ~7 chunks, four classes, no address conflict standing except the one I conceded.

**LINE-NUMBERING FINDING.** In `02_Generators_Capability_and_Symbols.md` the Read tool's displayed numbering runs **+1 ahead of `sed`/`awk`/`wc -l`** from ~L95 on: tool shows 761 lines and renders *"In most settings almost nothing has one."* at 96; `awk NR` and `wc -l` both give **760** and put it at **95**. Cause: at least one physical line the tool splits in two. Every other required file matched exactly — I re-verified the Davis spec, the runbook range and the census rows at `awk` numbering before writing.
**Can it corrupt a ranged contract? Yes.** Contracts are published as sed specs (`00.1` §4.1, `M-224`). Anyone who builds *or verifies* a range from displayed numbers on an affected file is off by one past the divergence — reading a struck line and dropping an admitted one at each boundary, exactly the `M-224` failure. Not triggered here (`02` was read FULL). Remedy is `M-223`'s shape: expand and verify every range with `sed -n`/`awk`, never with displayed numbers. **Raised, not fixed.**

---

## ROUND 3 · READER C's CROSS-CHECK — verbatim

**READER A — CONSISTENT.**
1. Same material. Independently confirmed: A's daylight split, "100.7 of 147.6 = 68.2%" for Oct–Feb and 6.6 = 4.5% for May–Jul — I re-summed the daylight column at `Specs/Davis.md` L95–106; both totals are exact.
2. Claim requiring a specific passage: *"The grid was originally designed primarily for pre-war human needs."* Found — `Energy_Grid_Failure_Rationale.md` L42. A's ~324 GW flywheel material is L61–73.
3. ⚠ One contradiction: A's §0.1 asserts 410 km² and the spec's ~400 km² are *"the same figure at lower precision, not a competing one,"* then runs the G2 profile on **410 km² of ice-free rock**. Nothing I read says the coastline-ruled extent *is* the ice-free area; B and I both recorded it as an unexplained 2.5% coincidence. A upgraded a corroboration-tier administrative figure into a ratified physical one.
4. ✅ And A corrected me: Notable tier is **13** nations (L22/L40–52), not the fourteen I wrote. 21 total stands.

**READER B — CONSISTENT.**
1. Confirmed: B's freeze–thaw finding — Jan +3.2/−1.2, Dec +2.4/−2.2, `Specs/Davis.md` L95, L106. Sixty days crossing zero daily is real and neither A nor I saw it.
2. Requires a passage: the three ice aviation surfaces (plateau/sea/island). Found — Airstrips L22, L23, L50.
3. ⚠ B treats Amundsen Tower as the exit's channel and derives a *queue*. The Tower's admitted description is power regulation; nothing I read makes it Davis's lift. That is mechanism where fire #1 says there is a hole. B tags it lightly; it should be tagged hard.

**1 — SHAPE. I hold BALANCED.** A's input-set framing is proper and its obligation-register point is real, but cost-dominant is defined as *STANDING COST being the largest quadrant*, and A's own §3.1 shows all four agreeing in STRENGTH and TOLERANCE. Its characteristic finding — identity become maintenance — is contradicted by A's own "it does one thing and the polity depends on it." **Conceded:** A's composite — *cost-dominant in what can report, cost-absent in what cannot* — is better than my flat uniformity note, and I adopt it as sub-structure.

**2 — CHOSEN/SELECTED. Voice-neutrality survives, narrowed.** A's 22.39% refutes *capability-sorting*, not selection; B reaches the same and then correctly refuses election for the **residue** — a census counts locations, not intentions. I adopt B's binding wording rule; my "no organ that decides about people" stands as the reason, and A's §7.4 (arrival assigned, departure elected, no channel between) corroborates it independently.

**3 — G3. B defeats my rationale. Conceded.** I used *MANDATED* as an in-world word; B is right that its referent is unreadable from outside the sheet and that fire #11's "production weight, not a social fact" is the standing analogue. **Upgrade retained, basis replaced:** 35>25 (in-world readable) plus L143's parent-facing construction and the word *heritage*. And **both A and B caught a dependency I missed** — L143 derives the function from the geography; G2×G3 is partially dependent. I adopt B's cell-level refinement: suitability cells are not grounding, calendar cells are.

**4 — COUNT. I move to 7, on reconciled units.** I omitted a real deficit both found — *cannot make its own plant* (industrial 5%; L148 export-shaped), **IN THE PARENT**. On the founding deficit, A and I addressed different objects: mine was the absent correction loop (past); A's the unrecorded competence (diffuse). **B's D-3a/D-3b split is correct and better than either**, plus the finding neither had: the solved founding story anesthetizes its live twin.

**Methodology finding, for the record.** `02` §4.1 files five addresses as **PEER-FREE**, *"available to every pass, with or without siblings."* **"In a neighbor's present" is misfiled.** Its definition requires a co-located peer who holds the thing organically and never departed — establishing that means reading another location's present state, forbidden in-run by the ONE LOCATION law (2026-09-06). The genuinely peer-free set is **four**. The fifth was added 2026-08-31, six days before the ruling that stranded it — the same shape as `01` §1.2's unenumerated sixth comparison instrument. **Consequence:** a pass trusting the heading records *checked and empty* where nothing was runnable, which is the `G6`/`M-117` failure class. Correct in-run entry: **UNAVAILABLE BY LAW, left explicitly open**, with the terminal pass told the axis was deliberately unrun. All three readers found this independently.

---

# ROUND 1 — THE THREE RAW DRAFTS

> ⚠ **These are the Round-1 outputs AS WRITTEN, before Round 3 corrected them.** ***They therefore contain the
> eight defects listed at the top of this file.*** **`02_Spine.md` is the corrected synthesis; these are the
> evidence, not the result.** ⛔ **Do not cite a claim from this section without checking it against
> `02_Spine.md` first.**
>
> ### ⚠ ONE EDIT WAS MADE, AND IT IS DECLARED RATHER THAN SILENT
> **Reader C used two British spellings** *(`millimetre`, `programme`)*. **The project's American-English rule is
> absolute and explicitly admits no exception for quoted material**, so both were normalized —
> ***`millimetre` → `millimeter`, `programme` → `program`.*** ⛔ **No substantive edit of any kind was made to
> any reader's text; no figure, claim, verdict or citation was touched.**
> ⭐ **The header of this section originally read *"UNEDITED,"* and that word was removed when the change was
> made.** ***A claim of untouched evidence has to survive the one edit it actually received, or it is the exact
> overclaim `Gate 0` exists to catch.***



## ROUND 1 · READER A — raw

---

# Davis — Step 2 · BUILD THE SPINE  *(Reader A, independent draft)*

**Frame: Second Interwar (2564–2812)** · written 2026-09-15 · one of three independent readings

> ⚠ **Status of this file.** This is **Reader A's own honest reading**, written blind to the other two readers.
> It is a candidate Step 2, not a ratified one. Nothing here has been cross-checked yet.

---

# 0 · SCOPE, INPUT SET, AND THE TAGS THIS STEP CARRIES

## 0.1 The admitted input set — stated first, because `02` §4.0 makes the shape a property of it

**Read in full at their contracted ranges for this step:**

| Source | Range |
|---|---|
| `00_RUNBOOK.md` — Step 2 | L2497–2525 |
| `02_Generators_Capability_and_Symbols.md` | full, 760 lines |
| `Specs/Davis.md` | the ratified 137-line read spec |
| `Worldspace/Energy_Grid_Failure_Rationale.md` | full, 145 lines |
| `Reference/Real-World/Climate Data/READER/Davis.md` | full, 16 lines |
| `Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md` | full, 99 lines |
| `Official_Population_Census.md` | L392–398, L496, L613 |
| This pass's own `00.1`, `00_Frame.md`, `01_Inherited.md` | full |

**Plus two bounded extractions handed to this step and not present at Step 0:**

1. **EXTENT — `410 km²`**, with a source density of `2,825/km²`. Closed by the coastline ruling rather than
   individually declared. *(`Specs/Davis.md` L60 and L120 say `~400 km²`; that is the same figure at lower
   precision, not a competing one.)*
2. **THE DIVISION-OF-INDUSTRY TIER STRUCTURE** — Agricultural/food **35% MANDATED (FULL)** · Technical/scientific
   **25% MANDATED (HALF)** · Maritime 15% · Commercial 15% · Industrial 5% · Other 5%, all **FREE**. Total
   workforce **876,514**, baselined on Census I. Percentages sum to 100.

**Still withheld and unopened:** `Local_Cultures/Mirny_Subnet/Davis.md` · `Local_Robot_Culture/Mirny_Subnet/Davis.md`
*(open at Step 5, as a check)* · `City_Megasheets/` · `City_Vision_Notes/` *(struck corpus-wide)* · the
differentiation table *(write-only; Davis's column is added at Step 9)* · **every other city** · the symbol
system files · `Extent_and_Density_Per_City.md` and `16_Per_City_Three_Tier_Run.md` themselves *(only the two
bounded extractions above are admitted, not the sheets)*.

## 0.2 Standing tags every finding below inherits

| Tag | What it marks |
|---|---|
| `[COR]` | **Corroboration tier — project-internal derivation.** The tier structure and the extent figure both. A finding carrying `[COR]` is not ratified canon and must be re-checked when those sheets are ratified |
| `PA-3` | Rests on the assumption that **the food obligation runs OUTWARD** — that the subnet does not relieve Davis of its own production |
| `PA-4` | Rests on **direction of access only.** ⛔ No finding anywhere below is scaled off throughput; no throughput figure exists |
| `[ND]` | ⛔ **Pre-declared NON-INDEPENDENT** — `00.1` §5.1 bounded one leak: *a tension between a harvest/agricultural dimension and an archive/record-keeping dimension.* **Anything here that resembles that relation is corroboration at best and is tagged.** See §2.2c, where I state plainly how my G4 reading differs from the leaked relation and where it does not |

## 0.3 Guards carried in from Step 1, honored throughout

- ⛔ **`Access type: ON` is uninterpretable.** No meaning is read off it anywhere below.
- ⛔ **No two nations' figures are compared, at any precision, in either direction.** The within-tier ordering is
  a de-stacking artifact. Per-nation figures are used only for **named portable institutions** — and below they
  are used for **one** thing: the *count* of origin communities (21) and the *share of the largest* (19.04%).
- ⛔ **Headcounts by sector are NOT used.** The sheet's own register carries an unresolved denominator conflict
  (181,808 against one basis, 306,780 against another, unresolved). **Percentages of workforce only.**
- ⛔ **No distributional result.** Band 5 machinery is deferred by `DR-4`. Nothing below is a spread, a mode, or
  a sub-location claim.
- ⛔ **General-population discipline.** *Growers* and *researchers* are roles. No claim below about what people
  here eat, wear, or believe is answered from either. ⭐ **And a flat number enforces it:** the workforce baseline
  is **876,514 of 1,158,314 — 75.67%.** `[COR]` **Roughly one resident in four is not in any sector at all**
  (24.33%), so a description of Davis assembled entirely from its sectors is missing about a quarter of the city
  before it starts.
- ⛔ **Translation discipline.** Generator vocabulary appears only in bracketed citations. Davis never describes
  itself as "physically constrained" or "Earth-elemental."
- ⛔ **`L148` is re-flagged on reuse:** a declared blank, export-shaped, with the import side absent.
- ⛔ **Reserved, not foreclosed:** proper names of people · the demonym · which DLC covers this subnet · disposal
  of the dead · G1's Element meaning · early-Federation currency. A compliance check runs at §10.3.

---

# 1 · ITEM 1 — GENERATOR SELECTION: **CONFIRMED, WITH ONE SUBSTANTIVE CHALLENGE**

**Step 0 selected `G2` (physical) · `G4` (founding) · `G8` (composition), with `G3` (function) carried fourth
*because it is the fragile one and must be exercised rather than leaned on*.**

## 1.1 The three that carry the rule of three — confirmed

`02` §5.1 rule 2: *select for independence rather than for strength; three generators that all descend from the
same fact are one generator wearing three hats.* The file's own worked example names this exact trio as the safe
one — *"Physical constraint, demographic composition, and inspiration research rarely are [the same fact]."*

- **`G2`** descends from latitude, geology and atmosphere.
- **`G4`** descends from a treaty date, a founding population, and what that population did and did not carry.
- **`G8`** descends from two census snapshots and a composition roster.

**No two of these share a parent fact.** ✅ **The rule of three is satisfied on G2/G4/G8 alone**, before G3 is
considered at all. Selection confirmed.

## 1.2 ⛔ THE CHALLENGE — **`G3` IS NOT INDEPENDENT OF `G2`, AND CANON SAYS SO IN THE SAME LINE THAT ESTABLISHES IT**

**`Specs/Davis.md` L143 does not merely state the function. It states the function's derivation:**

> *"Davis's own unique geography … genuinely fits it for the ecological-research/breadbasket role…"*

⭐ **The function was assigned FROM the geography.** That is precisely `02` §5.1's named failure — *function and
the parent's need are frequently the same fact as the physical one* — and it means:

> ## ⛔ **ANY `G2`–`G3` "AGREE" CELL IS ONE GENERATOR COUNTED TWICE. IT IS RESTATEMENT, NOT GROUNDING.**

**Every G2–G3 agreement in §3's table is marked `agree*` with the dependency flagged, and no spine claim rests
on a G2–G3 agreement alone.**

### ⭐ But `G3` has exactly one genuinely independent register, and it is the one the fuller input set supplied

**The OBLIGATION STRUCTURE is not a geographic fact.** `[COR]` Nothing about 410 km² of rock determines that the
food sector is **MANDATED (FULL)** and the research sector **MANDATED (HALF)**. That is a decision taken above
Davis and applied to it. **It descends from the polity, not from the ground.**

| | `G3` on the Step 0 input set | `G3` on this step's input set |
|---|---|---|
| **What it contained** | L143's one line — *what people do* | L143 **+ the mandate structure** — *what people owe* |
| **Independence from `G2`** | ⛔ **almost none** — the line states its own derivation from the geography | ✅ **real, in the obligation register only** |
| **Effect on the count** | a decorative fourth; the pass was really running three | **a genuine fourth** |

> ⭐⭐ **METHODOLOGY FINDING, recorded because it generalizes:** *a function generator read off a canon line that
> names its own geographic derivation is not a fourth generator — it is the physical generator restated in the
> vocabulary of purpose. **What rescues it is the OBLIGATION half: what the place is REQUIRED to produce, which
> no environment can determine.*** **Where canon supplies function without obligation, `G3` should be recorded
> as `PRESENT — DEPENDENT` and excluded from the rule of three.**

## 1.3 The generators NOT selected, and why each stays out

| | Status | Disposition |
|---|---|---|
| **`G1`** *(Earth / Earth)* | ⛔ **UNAVAILABLE TO THIS READING — and for a reason wider than `DR-1`** | §2.5 |
| **`G5`** *(Hwy 110, Prydz Bay)* | ⚠ direction yes, **volume never stated** | Not selected. Appears only as **relation** inside `G2` and `G3` cells, `PA-4`-tagged, never scaled |
| **`G6`** *(defining event)* | ⛔ recorded null; **its ground was withdrawn**, the null neither established nor disproved | §10.2 — **Step 2 does not need it.** Disposition `A` discharged |
| **`G7`** *(real-world inspiration)* | ⚠ designation yes, **research unbuilt** | ⛔ **Step 2 does not research.** The one G7-tier item used is the airstrips reference, admitted to this step's reading list, used for **physical texture only** and tagged. See §2.1e |

> ⚠ **An inherited inconsistency, noted and not re-litigated:** `00.1` §8 counts **six** countable generators;
> `01_Inherited.md` §1.3 and §1.6 count **five**. The difference is whether `G7`-by-designation counts before its
> research exists. **Either count clears the threshold of three by a wide margin**, and Step 2's own selection
> does not turn on it. Flagged once; not escalated.

---

# 2 · ITEM 2 — FOUR FULL PROFILES, RUN SEPARATELY, BEFORE ANY COMPARISON

> **Procedure honored:** each profile below was worked to all four quadrants on its own facts before the next was
> opened, per `02` §5.1 rule 3. The comparison in §3 was not consulted while writing these.

---

## 2.1 `G2` — PHYSICAL AND ENVIRONMENTAL CONSTRAINT

**The facts, flat:** 410 km² of ice-free exposed rock, lakes and fjord-like inlets on the Ingrid Christensen
Coast, Prydz Bay · mean annual **−10.0 °C** · monthly means **+0.9 · −2.2 · −8.0 · −13.5 · −16.0 · −15.7 · −17.1
· −17.1 · −15.7 · −11.8 · −4.2 · +0.0** · warmest mean daily maximum **+3.2 °C** (January) · record high **+13.0**,
record low **−41.8** · prevailing polar easterlies at **~5.6 m/s**, **out of the katabatic regime** · precipitation
**72.8 mm/yr falls**, **~28 mm lands** — **retention 38.5%** *(the corrected figure; L85's "~45%" reused L86's
millimeter figure for what is LOST as a percentage)* · polar night **~37 days**, midnight sun **~55 days** ·
freshwater lakes, saltwater lakes, **hypersaline lakes and landlocked marine basins**.

### (a) ⭐ The first thing to read off the table is not the cold. It is the PHASE of the light.

**The twelve monthly daylight figures average 12.3 h** *(unweighted mean of the twelve monthly values — the
averaging convention is named here deliberately, per `00_Frame.md` §0.3's finding that an unnamed convention
reads as an error to the next person who recomputes it).*

**That is an ordinary annual light budget.** What is not ordinary is how it is distributed:

```
five months  (Oct · Nov · Dec · Jan · Feb)   carry  100.7 of 147.6 monthly-mean daylight-hours  =  68.2%
three months (May · Jun · Jul)               carry    6.6 of 147.6                             =   4.5%
```

> ### ⭐ **Davis does not lack light. It lacks light WHEN IT NEEDS IT, and holds a surplus when it does not.**
> **The deficit is one of phase, not of quantity.**

**And the precipitation runs the same way, in the same direction:** March through June — the *darkening* months —
carry **38.2 mm of 72.8 = 52.5%.** December and January together carry **3.7 mm = 5.1%.** ⭐ **The only two months
whose mean sits at or above freezing are also the two driest**, so there is no meltwater pulse worth the name;
and what fell in the dark months has been reduced by sublimation and wind transport to 38.5% of itself before
anyone can use it.

**Three orders, run:**

1. *First order:* the light and the water both arrive out of phase with the demand.
2. *Second order:* **a city here cannot solve its central problem by moving things across space. It must move
   them across TIME.** Grow under free light, eat in the dark. Draw from a stock, not from a season.
3. *Third order:* ⭐⭐ **the characteristic engineering of this place is temporal, and so is its characteristic
   reasoning.** A place whose every important question is *"will there be enough of this later"* thinks in
   **balances and ledgers**, not in journeys, distances, or arrivals. **That is a cognitive shape, and it is
   produced by the calendar rather than chosen by anyone.**

### (b) The water is a STOCK, and the stock has no readable signal

72.8 mm/yr is a desert budget, and 38.5% of it stays. **The usable water is in the lakes, not in the sky.**

- *Second order:* every liter withdrawn is a liter that does not come back on any schedule a person can perceive.
  A precipitation-fed place is told annually how it did. **A closed-basin place at 72.8 mm/yr is told nothing on
  a human timescale.**
- *Third order:* ⭐ **the city's most important resource has no failure signal at all.** Not a slow one — none.
  Whatever the right level of withdrawal is, nobody living can find out they got it wrong.
- ⭐ **And the basins are themselves the record of the deficit.** Hypersaline lakes and landlocked marine basins
  are what a place looks like after a very long time of losing more than it receives. **The evidence is
  permanently on display and nobody has ever had an occasion to read it as a warning**, because nothing about it
  ever changes within a lifetime.

### (c) The ground holds still — and that is the largest free gift on the list

**410 km² of exposed rock.** Not ice. A foundation that does not move, does not flow, does not swallow, does not
require re-leveling or ice-movement correction. **An entire category of maintenance is simply absent here.**

1. *First order:* structures can be heavy, permanent, and extended rather than compact and replaceable.
2. *Second order:* the built environment outlives the people who built it, and keeps outliving them.
3. *Third order:* ⭐⭐ **Davis is full of arrangements nobody alive chose.** Not ruins — working buildings, working
   layouts, working routes between them, all older than any explanation anyone still holds. **The city inherits
   its own shape the way it inherits its own weather: as a given.**

### (d) The wind is moderate — and the consequence is not comfort, it is the removal of an alibi

**~5.6 m/s, out of the katabatic regime, the Vestfold Hills rock moderating further.** Wind is the variable that
converts cold into a gate; at this figure, it does not. ⭐ **Cold at Davis is a preparation problem, for humans
and for robots alike, on their different axes — not a hard stop.**

1. *First order:* outdoor work is possible on most days.
2. *Second order:* outdoor work is therefore **schedulable** — and a schedulable task is an **assignable** one.
3. *Third order:* ⭐⭐ **nobody here can say the weather decided.** In a place where conditions routinely cancel
   work, the environment does the allocating and absorbs the blame. **Davis's environment does neither.** An
   unpleasant job outdoors is somebody's decision, given to somebody, on a date.
4. *Fourth order:* ⭐⭐⭐ **so the standard of worth available here is COMPLETION, not ENDURANCE.** There is no
   credit for having survived the doing of it, because the doing was never in doubt — only the finishing was.
   *(Recorded as a standard of worth, which `NO FORCED FIT` expressly permits recording as what the place has.
   ⛔ It is NOT promoted into a virtue-category, an institution, or a named practice.)*

### (e) ⭐ The rock and the runway are mutually exclusive surfaces `[COR · G7-tier physical texture]`

**The admitted airstrips reference lists three facilities serving this site — Davis Plateau Skiway, Davis Sea Ice
Skiway, Plog Island Skiway — and all three are ICE.** The same file's own notes define a *skiway* as usable only
by ski-equipped aircraft, as distinct from a wheeled runway on gravel or blue ice, and record that **"Most
Antarctic airstrips are seasonal … and conditions/operators can change year to year."**

⛔ **The operator column is not used** — that is site provenance under GPS, and it does no work here.
⛔ **The Tepenian spec declares road (Hwy 110) and sea (Prydz Bay) only. Air is an UNDECLARED slot.**

> ### ⭐ What the physical texture nonetheless establishes, and it is structural
> **The ice-free rock that makes the city possible is the one surface an aircraft cannot use**, and the surfaces
> that can take an aircraft are the ones the city is not built on — plateau ice, sea ice, an island.
>
> 1. *First order:* the city's ground and its air link sit on different substrates.
> 2. *Second order:* one of those substrates is **fixed** and the other is **seasonal and moving.**
> 3. *Third order:* ⭐ **Davis's most reliable ground is its least useful ground for arrival, permanently, with
>    nobody at fault.** The place you can stand on forever is the place nothing can land on.
>
> ⛔ **NO FORCED FIT — THE AIR SLOT IS LEFT EXPLICITLY OPEN.** *Nothing in Davis's admissible canon states that
> this city has air access at all.* **"None is declared here" must not be read as "none is possible here."**
> **No airfield, no aviation practice, and no seasonal air calendar is invented.** The finding recorded is about
> the **relationship between two kinds of surface**, which holds whether or not aircraft ever come.

### (f) Cold as a free good — the one thing the environment gives away

At a −10.0 °C mean with five months below −15, **keeping things cold costs nothing here and keeping things warm
costs continuously.** ⭐ **Storage is free; growth is expensive.** That inversion is worth carrying forward: a
city whose harvest must cross a dark half-year is sitting on the one utility it never has to pay for.

### `G2` — THE FOUR QUADRANTS

| Quadrant | `G2` |
|---|---|
| **STRENGTH** | **It holds still.** Rock, not ice — an entire maintenance category absent; structures outlive their builders. **It does not cancel work** (moderate wind, no katabatic regime) — the working year is determinate. **It stores for free.** It offers real terrain — inlets, lakes, varied ground — and therefore real distance, which almost nothing else in a settlement of this kind supplies |
| **DEFICIT** | **No water from the sky** — 72.8 mm falls, 38.5% stays; the usable water is a closed stock with no readable signal. **No outdoor field** — two months at a non-negative mean and a mean daily maximum of +3.2 °C in the best of them. **No light when it is needed** — three months carry 4.5% of the annual monthly-mean daylight. **No growth of territory** — 410 km² is the whole of it, and ⚠ whether its boundary is fixed, seasonal or moving is unwritten *(inherited fire 14)*. **No ground that takes an aircraft** *(`[COR]`, and the slot is open)* |
| **STANDING COST** | **Heat**, continuously, against a −10.0 °C mean, forever. **Light, bought**, for the dark half of the cultivation year. **Water lifted and kept liquid** at −17 °C ambient. ⭐ **And notably NOT snow clearance** — at 72.8 mm/yr, digging out is a minor line, which makes Davis's standing cost **thermal and photic rather than the one an Antarctic settlement is assumed to pay** |
| **GRUDGING TOLERANCE** | **Going out, and being alone.** Both are permitted, unforbidden, and cost preparation and time; 410 km² of walkable varied ground means **privacy here is walked to rather than allocated.** ⛔ **And it is seasonal** — the same solitude is cheap in November and foreclosed in June. ⭐ **The cost is read as a personal choice** *("you went out in the dark")* **rather than as a property of the calendar, which is `02` §3.2's stronger answer and therefore the shadow** |

---

## 2.2 `G4` — FOUNDING CONDITION

**The facts, flat:** settled post-Falkland Treaty (2564) on prior station infrastructure. **Founding population:
Australian exiles (L129).** Through the First Interwar the site passed through a rotating succession of operators;
**no living environmental knowledge survived that chain of handoffs — but preserved journals, logs and orientation
manuals left behind across the centuries gave the exiles a real documentary starting point for the Vestfold Hills'
terrain. Learning from a written record isn't the same as being taught by a living institution**, and the exiles
built their own practical mastery of the terrain independently, over generations of their own (L127).

> ### ✅ THE `DR-7` PERSISTENCE TEST, RUN ITEM BY ITEM, IN ONE LINE EACH, AS REQUIRED
> | Item | *Would this still be here if the originating nation had left and never returned?* | |
> |---|---|---|
> | **Journals, logs, orientation manuals** | **Yes** — paper and records left in place outlive their makers | ✅ ADMISSIBLE |
> | **The terrain descriptions they contain** | **Yes** — a description of rock does not require its author | ✅ ADMISSIBLE |
> | **The station infrastructure settled on** | **Yes** — built fabric persists | ✅ ADMISSIBLE |
> | **A living institution, an apprenticeship lineage, a teaching body** | **No** — it requires occupation | ⛔ **INADMISSIBLE — and canon already says it did not survive** |
>
> ⛔ **And the standing limit is honored throughout: `DR-7` admits the MATERIALS and admits nothing about WHO
> MADE THEM.** **No claim below infers anything about the founding population's character, temperament or
> practice from the operator nationality.** The documents are treated as *documents about this terrain* and
> nothing else.
>
> ⭐ **L127 is itself the test's worked illustration:** the living institution required occupation and did not
> survive; the written record did not and did. **The line was already drawing the line the ruling draws.**

### (a) The founders arrived with a MAP and without a TEACHER — and the absence is the yield

1. *First order:* the founding generation did not have to discover the terrain fatally by trial. **The
   documentary inheritance is a casualty-avoidance instrument**, and it worked.
2. *Second order:* ⭐ **therefore Davis has no founding hardship of the usual kind.** The origin story is *we read
   what was left and it was accurate.* That is unheroic to a degree no designer would choose — which is exactly
   why `02` §1 says a generator is worth using in proportion to how much it resists you.
3. *Third order:* ⭐⭐ **a place with no heroic founding has nothing to moralize its rules FROM.** `Cultural
   Synthesis Techniques` §6 — *Necessity Before Meaning* — describes a rule forced by a founding constraint and
   moralized afterward. **At Davis the moralization step never had to happen, because the reason is written down
   and still legible. Davis's rules have footnotes.** A practice here is defensible by citation rather than by
   authority or by *"we have always done it."*
4. *Fourth order:* ⭐⭐⭐ **and therefore a custom whose citation has been LOST is uniquely naked here.** Elsewhere
   *"nobody remembers why"* is the ordinary condition of a tradition. At Davis it is an anomaly — because
   reasons are normally retrievable, an unretrievable one is a scandal that invites a search rather than a
   shrug. **The characteristic local response to an unexplained practice is to go looking for the document.**

### (b) ⛔ THE HARDER HALF — what the inheritance could not contain, and what replaced it

**A manual encodes propositional knowledge. It cannot encode the tacit part** — judgment, tempo, the feel of when
a surface is safe, the thing a living institution transmits by standing next to someone. **The founders had a
description and no procedure.**

**Canon closes the obvious reading:** *"the exiles still built their own practical mastery of the terrain
independently, over generations of their own."* The deficit was closed. **By their own work, over generations.**

> ### ⭐⭐⭐ AND HERE IS THE THIRD-ORDER YIELD, WHICH IS THE SHARPEST THING `G4` PRODUCES
> **The inheritance was TEXTUAL and the output was TACIT. The transmission problem inverted.**
>
> - The founding generation **could read and could not do.**
> - Every generation since **can do and has not written.**
>
> ⇒ ***Davis is text-rich about its terrain and text-poor about its own competence.***
>
> *Fourth order:* **and nobody notices, because a corpus exists.** The archive's presence is read as coverage.
> ⭐ **The single thing most likely to be lost here is the thing nobody believes is at risk**, and the evidence
> for believing it safe is the visible existence of a body of documents that is about something else entirely.

### (c) ⚠ `[ND]` — WHERE THIS DIFFERS FROM THE BOUNDED LEAK, AND WHERE IT DOES NOT

`00.1` §5.1 bounded one leak: **a tension between a harvest/agricultural dimension and an archive/record-keeping
dimension** — that one outgrows the other. **That specific relation is NOT used and is not asserted anywhere in
this file.** Stated plainly so a later reader can audit the distinction:

| | |
|---|---|
| ⛔ **NOT claimed** | That an archive institution and a farming institution compete; that either outgrows the other; that Davis is "really" one and pretends to be the other |
| ✅ **What IS claimed, and why it is a different object** | A claim about **how reasons are held** — that practice here is citable — derived from L127's founding condition alone, with **no institution, no premises, no staff and no rivalry attached.** It would be equally true of a Davis with no libraries at all |
| ⚠ **Where adjacency is unavoidable** | L143 admissibly records that Davis's libraries welcome smuggled books, and inherited fire 10 flags them as an **admission mechanism with only an entrance.** ⭐ **Used here for exactly one thing and tagged:** a place whose founding knowledge arrived as text has no reason to treat an incoming text as an exceptional object. ⛔ **And the same line classifies the practice as broader than Davis**, so it cannot be `Originated` here and is not claimed as distinctive |

### (d) The standing cost nobody is watching

**A corpus assembled across the centuries before 2564 and carried through a 248-year frame is not
self-maintaining.** Media, format, legibility and language all drift. **Keeping an inherited record USABLE is a
continuous custodial obligation** — it regenerates the moment it is finished, which is `02` §3.1's definition of
a standing cost exactly.

⭐ **And it has no failure signal.** Nothing breaks on the day it stops being paid. A corpus does not announce that
it has become unreadable; it simply stops being consulted, then stops being findable, then is not there. **That is
lapse, not collapse.**

### `G4` — THE FOUR QUADRANTS

| Quadrant | `G4` |
|---|---|
| **STRENGTH** | **It began already knowing where it was.** A documentary starting point that was accurate, and has stayed accurate, about the terrain. ⭐ **Reasons here are retrievable** — practice is defensible by citation, not by authority. **It is good at being handed something and using it** — the founding act was exactly that |
| **DEFICIT** | **No living institution, so no tacit transmission and no one to say "not like that."** ⭐⭐ **And the replacement competence — real, hard-won, generations deep — is UNRECORDED.** The place has a text about its landscape and none about its own skill, and cannot see the gap because the text exists. ⛔ **Exile's own mechanism** — threshold, decider, reviewability, heritability — **is absent and is not invented here** *(inherited fire 5; resolves upward)* |
| **STANDING COST** | **Keeping a multi-century record legible and consulted.** Continuous, invisible, and **signal-free** |
| **GRUDGING TOLERANCE** | **Contradicting the record.** Nobody forbids it; the burden of proof sits entirely on the living person; the cost is read as personal eccentricity. ⭐ **And the bias is self-reinforcing** — the corpus's subject is the slowest-changing thing here, so it keeps being right, and keeps being trusted past its subject |

---

## 2.3 `G8` — DEMOGRAPHIC COMPOSITION

**The facts, flat, peer-free, Davis's own:**

```
Census I  (Pre-Orbital)   563,599 H  /  594,715 R  /  1,158,314      robots 51.34%  ·  humans 48.66%
Census II (Orbital)       437,423 H  /  344,173 R  /    781,596      robots 44.03%  ·  humans 55.97%

retained, combined        781,596 / 1,158,314  =  67.48%
retained, humans          437,423 /   563,599  =  77.61%
retained, robots          344,173 /   594,715  =  57.87%
spread                                            19.74 pp toward humans

departed, combined        376,718        of which robots 250,542 (66.51%) · humans 126,176 (33.49%)
departure rate, humans    22.39%         departure rate, robots  42.13%
```

**Composition: 21 origin communities.** Primary tier one nation at **19.04%**; Significant tier seven, including
the founding wave at **4.93%**; Notable tier thirteen.

> ⛔ **THE HARD CEILING, honored:** the per-nation figures are a share-weighted model, identical across both
> censuses by construction. **`G8` can never say which communities left. An absence of origin-differential exit
> here is an ARTIFACT, not a finding** *(inherited fire 2)*. ⛔ **No two nations are compared.** The only
> composition facts used below are **how many communities there are (21)** and **how large the largest is
> (19.04%)** — both of which are properties of the roster's shape, not of any nation.

### (a) ⭐ The majority inverts, and it is not a population change

**Robot-majority at Census I; human-majority at Census II.** ⚠ **And the transition is UNDATED** *(inherited fire
12)* — so Band 5 is declared for an unstated fraction of the 248 years, and **no tense may be assigned to the
inversion inside the frame.** It happened; when, and how quickly, is not written and is not invented here.

### (b) 21 origins and no majority — what that structurally FORCES

**The largest single origin community is 19.04%.** ⭐ **A population assembled like that cannot run on a shared
tacit background, because there isn't one to run on.**

1. *First order:* anything everyone must understand has to be **made explicit** — stated, posted, demonstrated,
   written.
2. *Second order:* explicitness is a capability. **Davis can take people in and make them functional without a
   long apprenticeship.** It is structurally good at **induction**, which is `02` §3's *"what others route to
   it; what it is trusted with."*
3. *Third order:* ⭐⭐ **and the cost of that capability is that TIME SERVED BUYS NOTHING.** If competence is
   certified by explicit procedure, then having been here longest confers no standing that a procedure cannot
   confer on a newcomer in a season. ⚠ *Stated as a structural tendency of the arrangement, not as a social
   fact about any group — general-population discipline and the Band 5 deferral both bind here, and the
   distributional question of who actually holds standing is not asked.*

> ⭐⭐ **NOTE THE CONVERGENCE, and it is arrived at from a completely independent parent fact:** `G4` says the
> founding knowledge came as text; `G8` says the composition forces explicitness. **Two generators with no shared
> ancestor return the same structural property.** `02` §5.2: *all agree → well-grounded, build hard on it.*

### (c) ⛔ THE HANDED QUESTION — *when leaving became possible, robots left at higher rates than humans; what about THIS place made that so?*

**Davis's own figures: 42.13% of its robots departed against 22.39% of its humans, a spread of 19.74 pp.**
*(An internal comparison between two populations of the same city — legal, and not a comparison to any other
place.)*

#### ⛔ First, the answer that must be REFUSED, because it explains nothing about Davis

Robots are vacuum-capable and not altitude-limited; humans are neither. **A general capability difference is
available and would produce a differential in this direction anywhere it applied.** `00_Frame.md` §0.3 records the
era file's governing rule for exactly this: the orbital exit is *"national context, true everywhere — therefore
never a differentiator,"* and ***"what differentiates is how hard a given place used that exit."***

⇒ **The general factor is real, is not mine to write, and is not a Davis finding.** What needs a local account is
**Davis's own number.**

#### ⭐ Second, and decisively: the general factor CANNOT be the whole account, and Davis's own arithmetic proves it

> ## **126,176 humans departed — 22.39% of Davis's human population.**
> **Humans have none of the capabilities a vacuum-tier selection would select for.** A better-than-one-in-five
> human departure rate is not producible by a capability filter. ⇒ **Something at Davis was pushing, and it was
> pushing on both populations. The robot figure is the same push meeting a lower barrier.**

#### ⭐⭐⭐ Third — the local account, built from the admitted material and from nothing else

**Two independent structural facts about this city bear on it, and neither has an author:**

**1. The dominant workplace is specified by a third party.** `[COR · PA-3]` The largest sector is sheltered
agriculture and greenhouse cultivation — **warm, lit, humid enclosures built to a plant's requirement.** Nobody
designed them against robots. Nobody designed them for robots either. **The specification was written by the
crop.**

**2. The power layer beneath them was specified for humans.** The admitted energy document states it directly, of
the grid's *original* design — an in-frame fact, extracted from a document whose failure narrative is entirely
post-war and is not used:

> **"The grid was originally designed primarily for pre-war human needs."** — and it names the divergence:
> **robots need stable, high-density siligel-compatible power; humans need consistent low-level heat.**

⛔ *Used for the antecedent design fact only. Everything the same file says about damage, factions, rogue control
AIs, Concordia's districts and the present day is post-2812 and out of frame, and none of it appears anywhere in
this pass.* ⛔ *And no other city's material is imported from it.*

**Run the three orders:**

1. *First order:* Davis's majority population lives and works inside two nested specifications — the enclosure's
   and the grid's — **and neither was written for them.** There is no hostility in this. There is no policy, no
   villain, and no enforcer. The place is simply shaped that way.
2. *Second order:* ⭐ **that produces a cost that is small per day and different in kind** — not a barrier, not a
   gate, not an injury, just a permanent low-grade mismatch between what the majority is and what the majority's
   surroundings were specified around. **`02` §3.2's shadow exactly: real, authorless, invisible from inside,
   and working with everyone in good faith.**
3. *Third order:* ⭐⭐⭐ **a cost with no name and no counterparty cannot be petitioned, negotiated, or even
   stated. It can only be integrated.** Over an unwritten but long stretch of a 248-year frame, it integrates.
   **And when an exit appears, that accumulated integral is the whole of the reason — expressed, at last, as a
   decision, by people who could not have told you what was wrong.**
4. *Fourth order:* ⭐⭐⭐ **and the people who could have named it are the ones who are gone.** The 250,542 who
   departed are the witnesses. The 344,173 who stayed are, by construction, those for whom the arrangement held.
   **Davis after the transition cannot diagnose this — not from denial, but because its evidence physically
   departed.**

⛔ **What is NOT claimed, and must not be read in:** that researchers are robots or growers are human; that any
origin community left preferentially *(foreclosed by the model)*; that anybody was excluded, refused, or pushed
by any person or policy. ⛔ **And the exit's own mechanism — eligibility, refusal, durability, any return trip —
remains the mechanism-shaped hole Step 1 recorded, and is not filled here.**

### (d) The obligation the composition itself imposes

**A population that must be addressed explicitly must be RE-addressed explicitly, permanently.** Procedure has to
be restated, re-posted, re-taught. ⭐ And **the tier system admits and never subtracts** *(inherited fire 11; the
tiers are a production weight, not a social fact)* — so the induction burden only ever grows.

*Third order:* ⭐ **then 376,718 people leave, and the induction machinery is suddenly sized for a city that is no
longer arriving.** A capacity built for intake, applied to a body that has stopped growing. ⚠ *Stated as a
relation between a capacity and a headcount, not as a distribution.*

### `G8` — THE FOUR QUADRANTS

| Quadrant | `G8` |
|---|---|
| **STRENGTH** | ⭐ **It can absorb anyone.** 21 origins, largest at 19.04%, no tacit background to fail to share — so everything load-bearing is explicit and a newcomer becomes functional fast. **It is good at induction**, and that is what it would be trusted with |
| **DEFICIT** | ⛔ **It can measure the outcome of a decision it cannot see.** The census records a destination and not a gate. **It cannot say which communities left** — foreclosed by construction, and the absence is an artifact. ⛔ **It cannot say what a robot's national origin is MADE of, or whether it can change** *(inherited fire 13)* — the model assigns an ancestry to the majority population of Act 1 Davis and never states its content. ⚠ **It cannot date its own largest event** |
| **STANDING COST** | **Explicitness, forever.** Restating the common procedure across 21 origins and two kinds of person, for a roster that only ever adds. **Nobody experiences this as a cost** — it presents as ordinary administration, which is `02` §3.1's diagnostic for the interesting case |
| **GRUDGING TOLERANCE** | **Keeping an origin distinct once Act 2 arrives.** Nobody forbids it, nothing supports it, and it becomes quietly more expensive as origin turns from identity into ancestry. ⭐ **Acute for the majority population specifically**, because a robot's origin has an assigned label whose content is not written anywhere — so the thing being maintained cannot be stated. ⛔ **What it consists of is NOT answered here; the slot stays open** |

---

## 2.4 `G3` — FUNCTION AND PURPOSE  *(the fragile one — exercised, not leaned on)*

**The whole of it in canon is one line, L143:** *"Davis is, above all, Tepenia's breadbasket and a prime
ecological/limnological research hub — sheltered-agriculture and greenhouse cultivation alongside genuine research
heritage make up the clear majority of daily activity."* The same line records a **small arts and music
community**, that **most non-work time goes to bars, eateries and general social establishments**, and that the
city's **libraries welcome smuggled books** *(a broader Tepenian practice, not Davis's own)*.

**`[COR]` The obligation structure:** food **35% MANDATED (FULL)** · technical/scientific **25% MANDATED (HALF)**
· maritime 15% · commercial 15% · industrial 5% · other 5%, all **FREE**. **60% of the workforce under mandate;
40% free.**

### (a) `02` §G3's split question, and the divergence it is supposed to find

- *What is this place for, on its own terms?* — **a research community.**
- *What does its parent need from it?* — **calories.** `PA-3`

**The tier data sharpens this past anything the function line alone could say:**

> ## ⭐⭐⭐ **THE FOOD IS MANDATED-FULL. THE VOCATION IS MANDATED-HALF.**

1. *First order:* both are obligations, at different grades.
2. *Second order:* ⭐ **a HALF-mandate is a worse position for an identity than either extreme.** A fully mandated
   activity is unambiguously the polity's. A free activity is unambiguously the city's own. **A half-mandated one
   is contested at every single instance and no instance settles it** — Davis's research can never become
   straightforwardly *ours* or straightforwardly *theirs*.
3. *Third order:* ⭐⭐ **so the tension does not surface as conflict. It surfaces as DRIFT.** When the two compete
   for the same hour, the tier structure has already decided; nobody has to argue and no argument is on record.
   **Research time is the residual.**
4. *Fourth order:* ⭐⭐⭐ **and a vocation that is structurally a residual is the one an exit reaches first**,
   because it is the one for which nothing is owed to anybody. ⛔ **Whether the people whose work was residual
   are the people who departed is NOT ANSWERABLE from anything admitted** — there is no sector-by-population
   data of any kind, and inventing the link would be exactly the forced fit the law forbids. **The slot is left
   explicitly open**, and it is named here as the single sharpest open question Step 2 produces.

⚠ `PA-3` **tagged on the outward direction throughout.** Mitigation as Step 0 recorded it: both halves sit in one
ratified line as **Davis's own self-description**, so the tension survives as a fact about how Davis describes
itself even if the direction is later revised.

### (b) A breadbasket with no fields — and what an agrarian culture becomes without weather

**Everything is sheltered agriculture and greenhouse cultivation.** With two months at a non-negative mean and a
mean daily maximum of +3.2 °C in the best of them, **there is no open-field anything.**

1. *First order:* the food is an enclosure product, not a land product.
2. *Second order:* ⭐ **nobody here has ever seen the food they grow standing in open air.** Every plant anyone
   has raised has had a roof. **The agricultural imagination of this place has no horizon in it.**
3. *Third order:* ⭐⭐⭐ **the vocabulary of growing here contains no weather.** A grower's hazards are mechanical,
   electrical and thermal — a seal, a lamp, a pump, a line. **A bad year at Davis is a systems failure, not a
   drought.**
4. *Fourth order:* ⭐⭐⭐ **and a systems failure HAS AN AUTHOR, which weather does not.** The oldest consolation
   available to people who grow things — *it was nobody's fault, it was the sky* — **does not exist here.**
   Whatever is lost was lost because something was not done. ⚠ *Recorded as a structural property of blame in
   this place. ⛔ No practice, ritual, institution, penalty or tribunal is invented from it.*

### (c) What the function structurally cannot supply

**Industrial is 5% and free; maritime and commercial are 15% each and free.** `[COR]` **A greenhouse city that
does not build greenhouses.** Every pane, lamp, pump, seal and line arrives.

- *Second order:* **the mandated-full sector's inputs are the free sectors' imports.** The obligation is fixed;
  the means of meeting it are not locally controlled. `PA-4`
- *Third order:* ⭐⭐ **so Davis's real fragility is not agricultural at all — it is logistical**, and inherited
  fires 7 and 8 land together on exactly that point: **a breadbasket with no written failure mode and no stated
  growing season, served by two ways in with no written failure state** — no sea-ice season, no road closure, no
  duty cycle. ⭐ **And L154 writes precisely such a seasonal closed state for the lakes, one line away**, which
  proves the omission is not a house style. ⛔ **The failure state is not invented here. Its absence is recorded
  as a constraint on every later phase.**

### (d) Determinacy, and where the variety has to go instead

**The work is mandated, the enclosure is indifferent to the weather outside, and the wind does not cancel
anything.** ⭐ **Davis's working day is unusually determinate — almost nothing about it is decided by conditions.**

⇒ *Second order:* the variety has to come from somewhere else — and **L143's own leisure profile is exactly what
that produces**: bars, eateries, general social establishments, a small arts and music community taking the
non-work time.
⇒ *Third order:* ⭐⭐ **so Davis's leisure is COMPENSATORY rather than RECUPERATIVE.** It is not there to recover
from an ordeal — the work is not an ordeal, it is a schedule. **It is there to supply a variability the work
structurally does not contain.** ⭐ *This is genuine corroboration: the tier structure and the ratified function
line, two different sources, predict the same leisure shape.* ⚠ **General-population discipline: this is read
off the city-level line, not off either named role.**

### `G3` — THE FOUR QUADRANTS  *(⛔ every cell below is flagged for its `G2` dependency per §1.2)*

| Quadrant | `G3` |
|---|---|
| **STRENGTH** | **It does one thing and the polity depends on it.** The largest sector is not optional, so the city always knows what tomorrow is. ⭐ **A determinate working year** — ⛔ `dep-G2` for the environmental half, ✅ independent for the obligation half |
| **DEFICIT** | ⛔ **It cannot make its own equipment.** ⛔ **It has no written failure mode** — for the crop, for the season, or for either way in. ⛔ **Its own vocation is a residual it cannot convert into a claim** |
| **STANDING COST** | ⭐ **The mandate itself, which does not flex** — 35% FULL, and whatever else changes the calories go out. ⭐ **And the half-mandate, which must be justified at every instance and is never settled by any of them.** ✅ **Independent of `G2`** |
| **GRUDGING TOLERANCE** | **Doing the unmandated.** The research beyond the half; the arts and music; anything in the 40% that is free. Permitted, unsponsored, and paid for out of the residual of a residual |

---

## 2.5 `G1` — READ LAST, AS A CHECK. **AND IT RETURNS NOTHING, FOR TWO REASONS.**

**Davis's pair: `Earth / Earth`.**

| Half | Status |
|---|---|
| **Element — Earth** | ⛔ **RESERVED by `DR-1`.** No finding may rest on what it means |
| **Planet — Earth** | ⚠ **RATIFIED and readable in principle — but `Planetary_Symbols.md` IS NOT IN THIS STEP'S ADMISSIBLE SET AND WAS NOT OPENED** |

> ## ⛔ SO THE CHECK CANNOT BE RUN, AND SAYING SO IS THE RESULT
> **`02` §6.0 is categorical: *read the member from the file, never from the name*** — added after that exact
> error inverted an entire capability reading, with a worked example in which a symbol's registered meaning was
> the **precise opposite** of its traditional one. **I have not read either file. Therefore I may not read either
> half, and the fact that one of them is ratified changes nothing about that.**
>
> ⛔ **And the pairing typology (`02` §6.3) is unavailable a second time over:** the relation between two symbols
> cannot be classified as reinforcing, tensioned, orthogonal or ironic when **neither** member's registered terms
> are in hand. **This is a half-pair with both halves closed.**
>
> ### ⛔⛔ THE `DR-1` TRAP AT DAVIS, RESTATED AT ITS POINT OF MAXIMUM DANGER
> **Davis's strongest physical facts — exposed rock, ground that holds still, soil, cultivation, a breadbasket,
> groundedness — are precisely what a reader would intuitively call "Earth."** ⛔ **Every one of those findings
> above was derived from `G2`, `G3`, `G4` or `G8` and from measured figures, and NONE of them is connected to
> the symbol anywhere in this file.** **Any sentence joining Davis's ground or its agriculture to the Element
> would foreclose a reserved decision**, and the temptation is strongest exactly where the material is richest.
>
> ⇒ **`G1` CONTRIBUTES ZERO CELLS, ZERO CORROBORATION AND ZERO CONTRADICTION.** ⭐ **An unavailable check is not a
> passed check, and it is recorded as unavailable rather than as agreement.**

---

# 3 · ITEM 3 — THE COMPARISON

**One row per quadrant, one column per generator. Every cell marked `agree` · `conflict` · `silent`, relative to
the other cells in its row.** ⛔ `agree*` **marks an agreement that is NOT grounding** because the two generators
are not independent (§1.2).

## 3.1 The table

| | **`G2` physical** | **`G4` founding** | **`G8` composition** | **`G3` function** |
|---|---|---|---|---|
| **STRENGTH** | **agree** — it holds still; the ground, the wind and the calendar are all settled before anyone arrives | **agree** — it arrived already knowing where it was; the terrain came pre-described | **agree** — it can absorb anyone, because everything load-bearing is explicit | **agree\*** — it does one thing and knows it; ✅ the obligation half is independent, ⛔ the environmental half is `G2` restated |
| **DEFICIT** | ⛔ **conflict** with `G4` — no water from the sky, no field, no light in phase, no growth of territory · ⛔ **conflict** with `G3` — the substrate grows nothing | ⛔ **conflict** with `G2` — the place was legible on arrival and has stayed legible · ✅ **agree** with `G8` — the record omits the part that decides | ✅ **agree** with `G4` — it can measure an outcome whose mechanism was never written · **silent** on the material register | ⛔ **conflict** with `G2` — a breadbasket on ground that grows nothing · **agree** with `G3`'s own logistical half |
| **STANDING COST** | **agree** — heat, bought light, water kept liquid; **fast, loud failure signals** | **agree** — a multi-century record kept legible; **no failure signal at all** | **agree** — explicitness restated forever, for a roster that only adds; **no failure signal at all** | **agree** — the mandate that does not flex, and the half-mandate re-argued at every instance; **a slow signal** |
| **GRUDGING TOLERANCE** | **agree** — going out, being alone; seasonal, and charged to the person | **agree** — contradicting the record; the burden sits on the living | **agree** — keeping an origin distinct in Act 2; acute where its content is unstated | **agree** — doing the unmandated, out of the residual of a residual |

## 3.2 Reading the table against `02` §5.2

| Row | Pattern | `02` §5.2 says | Done |
|---|---|---|---|
| **STRENGTH** | **all four agree** *(three independently; `G3` partly restating `G2`)* | *Well-grounded. Build hard. **Use as the spine.*** | ✅ §8 |
| **DEFICIT** | **two agree (`G4`+`G8`), two conflict (`G2`×`G4`, `G2`×`G3`)** | *The conflict is the finding. Run the both-are-true test.* | ✅ §3.3, §3.4 |
| **STANDING COST** | **all four agree — and from four DIFFERENT generator classes** | §4.0 rule 2 check | ✅ §3.5 |
| **GRUDGING TOLERANCE** | **all four agree** | grounding — and `02` §3.2 makes it the shadow | ✅ §3.6 |

## 3.3 ⭐⭐⭐ BOTH-ARE-TRUE, CASE 1 — THE `G2` × `G4` CONFLICT *(handed to this step explicitly)*

> **`G4`:** the founders arrived with an accurate written account of this place and never had to discover it.
> **`G2`:** this place is 410 km² of exposed rock at a −10.0 °C mean that withholds water, light and any field.

⛔ *Do not ask which is right.* **Ask what single property of this place would produce both readings.**

> ## ⭐ **THE ACCURACY OF THE INHERITANCE IS A FUNCTION OF THE STABILITY OF ITS SUBJECT.**
>
> **`G2`'s own first STRENGTH is that the ground holds still.** Rock does not move, so a description of it
> written centuries ago is still correct today — **`G4`'s inheritance works because of the very property that
> makes `G2` severe.** They are not two readings of one object in tension. **They are one property producing two
> effects on two different objects:**
>
> | | The inheritance | The deficit |
> |---|---|---|
> | **Object** | the **substrate** — where the rock is, where the lakes are, which are saline | the **operations on it** — what to do, when, how, and how to tell it is going wrong |
> | **Timescale** | geological — unchanged across the whole record | daily, seasonal, generational |
> | **Verdict** | ✅ **stands** | ✅ **stands** |
>
> ⭐ **Neither generator was misread, and the conflict dissolves into a stronger joint claim than either half.**

**And now the three orders, which is where the finding actually is:**

1. *First order:* Davis holds an inheritance that is permanently, verifiably correct about the one thing that
   never changes, and silent on everything that does.
2. *Second order:* ⭐ **because it keeps being right, it keeps being trusted — including about things it never
   addressed.** Demonstrated reliability on geology is read as reliability in general. **Nobody is lying. The
   document is not wrong. It is simply being asked questions it was never about.**
3. *Third order:* ⭐⭐⭐ **the characteristic error at Davis is not ignorance. It is MISPLACED CITATION** —
   answering a live procedural question with a settled geographic one, and being believed, because the citation
   checks out when anyone bothers to verify it. **An error with a correct footnote is almost impossible to
   argue with in a place whose whole epistemic habit is retrieval.**
4. *Fourth order:* ⭐⭐⭐ **and `02` §3's DEFICIT rule lands exactly** — *"its characteristic failure is what the
   deficit was supposed to prevent."* **The documentary inheritance existed so the founders would not learn this
   terrain fatally by trial. Its characteristic failure is that it now prevents the city from noticing that it
   is learning EVERYTHING ELSE by trial, unrecorded, and calling that normal.**

## 3.4 BOTH-ARE-TRUE, CASE 2 — THE `G2` × `G3` CONFLICT

> **`G3`:** Davis is the breadbasket. **`G2`:** nothing grows on this ground, in this light, on this water.

**Different objects, different scales, and both stand:** `G3`'s food is an **enclosure** product; `G2`'s barrenness
is a fact about the **outdoors**. The conflict is only apparent to a reader who has imagined fields.

⭐ **But do not discard it — the resolution is the finding.** It is what produces **§2.4(b): a breadbasket with no
fields**, and the fourth-order consequence that *a bad year here has an author*. ⭐⭐ **A conflict that dissolves
cleanly can still be the most productive cell in the table, and this one is.**

## 3.5 ⭐⭐ THE STANDING COST ROW — the §4.0 rule 2 check, and a split inside the agreement

**`02` §4.0 rule 2:** *a quadrant that fills only from one generator class is suspect; if STANDING COST is
populated entirely by known institutions and not by physical or functional constraint, the location's cost is
**voluntary, not imposed**.*

> ## ✅ **CHECK PASSED, AND CONVINCINGLY.** STANDING COST at Davis fills from **four different classes** —
> **physical** (`G2`: heat, light, water), **custodial** (`G4`: the record), **social** (`G8`: explicitness), and
> **obligational** (`G3`: the mandate). ⭐ **Davis's cost is IMPOSED, not voluntary**, and it is not an artifact
> of having admitted any institution — **no institution was admitted at all** *(`Local_Cultures/` remains
> unopened)*.

### ⭐⭐⭐ But there is a split inside the agreement, and it is the most valuable thing in this row

| Cost | Failure signal | How you find out |
|---|---|---|
| **Heat** (`G2`) | **immediate and loud** | within hours |
| **Bought light** (`G2`/`G3`) | **fast** | within a growing cycle |
| **The mandate** (`G3`) | **slow but real** | the calories do or do not go out |
| **The record's legibility** (`G4`) | ⛔ **NONE** | nothing breaks, ever, on any day |
| **Explicitness restated** (`G8`) | ⛔ **NONE** | nothing breaks, ever, on any day |
| **The water stock** (`G2`) | ⛔ **NONE on a human timescale** | not within a lifetime |

1. *First order:* Davis's standing costs are **bimodal** — some announce themselves instantly and some cannot
   announce themselves at all.
2. *Second order:* ⭐ **attention goes where the alarms are.** It always does, and correctly.
3. *Third order:* ⭐⭐⭐ **so at Davis, *"we are on top of our maintenance"* is TRUE about everything capable of
   raising an alarm and UNTESTED about everything that is not — and the true half is the evidence offered for the
   untested half.** **Nobody is complacent. The competence is genuine. It is simply being generalized from the
   only domain that can ever report back.**
4. *Fourth order:* ⭐⭐ **the characteristic failure at Davis is therefore LAPSE, NOT COLLAPSE** — a practice done
   less often, then rarely, then not, with no moment at which anyone finds out. `02` §4's cost-absent row names
   this exactly, and here it is occurring **inside** a heavily cost-loaded location. **That combination is the
   real structure, and neither shape label alone captures it.**

## 3.6 THE GRUDGING TOLERANCE ROW — four generators, one underlying rule

**All four cells reduce to the same sentence:**

> ## ⭐⭐⭐ **AT DAVIS, WHAT IS PERMITTED-BUT-EXPENSIVE IS ALWAYS THE THING WITH NO INSTITUTIONAL SPONSOR — AND ITS COST IS ALWAYS CHARGED TO THE PERSON RATHER THAN TO THE ARRANGEMENT.**

Going out alone in winter · contradicting a record that has been right for centuries · keeping an origin distinct
after origin has become ancestry · doing work outside the mandate. **Four different generators, four different
objects, one structure.** Nobody banned any of it. Nobody enforces anything. It costs anyway.

1. *First order:* the unsponsored is affordable to whoever is willing to pay for it personally.
2. *Second order:* ⭐ **which produces people who are privately particular and publicly compliant, and produces
   no politics whatsoever about any of it** — there is nothing to petition, because nothing was decided.
3. *Third order:* ⭐⭐⭐ **the city has no channel through which an unsponsored preference can act on the world.**
   Not a blocked channel. **No channel** — the arrangement never built one, because it never refused anything and
   so never generated the demand for one.
4. *Fourth order:* ⭐⭐⭐ **and then, at an undated point inside the frame, one appears. It requires no petition,
   no counterparty, no argument and no sponsor. It requires leaving.** ⭐ **This is the answer to the handed `G8`
   question, arrived at independently from four generators rather than from the census: Davis's only channel for
   an unsponsored preference was departure, and whoever's costs were most diffuse used it hardest.**

> **Test 1 — delete every other city's name:** none appears; the claim stands. ✅
> **Test 2 — does this require knowing anything about any other place to be true?** No. ✅

## 3.7 ⭐ SHARED SILENCE — a shape result, and it is NOT filled

**No quadrant is empty.** But at a finer grain, **all four generators are silent on the same thing**, and `02`
§5.2 is explicit that shared silence is a shape result to be recorded and not filled:

> ## ⛔ **DAVIS'S ADMITTED MATERIAL HAS NO NEGATIVE DIRECTION.**
> **Nothing in it is written in terms of stopping, refusing, failing, closing, or leaving.**
>
> | What is written | What is not |
> |---|---|
> | what arrives — exiles, documents, 21 communities, a highway, a harbor, books, precipitation, food | **no exit mechanism · no refusal · no eligibility · no return · no growing season · no bad year · no road closure · no sea-ice season · no duty cycle · no exclusion criterion for the tiers** |
>
> ⭐ **And the one enormous outflow — 376,718 people — is recorded as a NUMBER and never as a MECHANISM.**
> ⭐ **One clean counter-example proves this is not a house style:** L154 writes a seasonal closed state for the
> lakes explicitly, one line from two entrances it leaves permanently open.
>
> ⛔ **NOT FILLED.** ⚠ **And per `02` §4.0 this silence is a property of the ADMITTED INPUT SET, not necessarily
> of Davis.** It may narrow at Step 5 when this location's own culture material opens. **Recorded as a shape
> result with its input set attached, and left open.**

---

# 4 · ITEM 4 — THE SHAPE, READ TWICE

> ⛔ **THE CROSS-LOCATION FORM IS NOT USED ANYWHERE.** No sibling is consulted; the question *"does this shape
> repeat a sibling?"* is not asked. ⭐ **The second reading the three-step rule needs is this same location read
> twice, on two different input sets** — `02` §4.0's double reading.

## 4.1 The two input sets, both real and both this pass's own

| | **READING 1 — the Step 0 input set** | **READING 2 — this step's input set** |
|---|---|---|
| Held | Specs at 137 lines · census · the pass files | the same, **plus** the extent figure **410 km²** and the **obligation tier structure** |
| Extent | `UNDETERMINED`; item 6 expected **blocked** | **410 km²; item 6 RUNNABLE** |
| `G3` | one line, **which states its own derivation from `G2`** | one line **+ 35% MANDATED-FULL / 25% MANDATED-HALF** |

## 4.2 The shape under each

> ### **READING 1 → BALANCED**, with a doubling in DEFICIT.
> All four quadrants populated. STANDING COST fills from **three** registers — physical, custodial, social — and
> the **obligational register is silent**, because L143 says what people *do* and not what they *owe*.
> **§4.0 rule 2 therefore fires as a warning:** a cost quadrant with no obligational input reads as a cost the
> city is choosing. **Matching question:** *"What does the balance cost?"*

> ### **READING 2 → COST-DOMINANT.**
> The obligation register fills hard: **60% of the workforce under mandate, 35% of it non-negotiable.** STANDING
> COST becomes the largest quadrant, and it is now imposed from four independent classes rather than three.
> **Matching question:** *"Is this place doing anything other than continuing to exist?"*
> ⭐ **And its characteristic finding lands with a specific twist:** `02` says a cost-dominant location's identity
> has quietly become its own maintenance. **At Davis the identity — research — is literally the half-mandated
> residual of the maintenance — food.** The generic finding and the local fact are the same sentence here.

> ## ⭐⭐ **NEITHER READING MISREAD ITS INPUTS. BOTH READ THEM CORRECTLY.**
> **This is `02` §4.0's mechanism reproducing exactly:** *admit the obligations and STANDING COST fills; withhold
> them and it empties.* ⭐ **New instance worth recording for the methodology:** the demonstrated case involved
> withholding a location's **known institutions**. **Here what was withheld was a bounded NUMERIC extraction of
> an obligation structure — no institution, no culture, no conclusion, just percentages — and it flipped the
> shape just as completely.** ⇒ ***Obligation data is shape-determining even in its most inert, quantitative
> form.***

## 4.3 The three-step rule, in-run form

1. **The shape gives the question** *(shared, and the only shared part)*: **what must Davis keep paying, and what
   is it paying for?**
2. **The generator gives the instrument** *(nothing about the shape predicts which)*: **`G8`'s retention
   arithmetic** — 67.48% combined, 77.61% human, 57.87% robot, spread 19.74 pp. It is the only measure in the
   whole input set of an **outcome** rather than a **condition**.
3. **The instrument gives the consequence — and here the readings separate.**

## 4.4 ⭐⭐⭐ THE DIVERGENCE TABLE — five axes, including TENSE

| Axis | **READING 1** *(balanced; no obligation data)* | **READING 2** *(cost-dominant; obligation data)* |
|---|---|---|
| **What the 19.74 pp spread IS** | a **PREFERENCE** result — the place suited one population less | an **ALLOCATION** result — the arrangement charged unsponsored costs to individuals and one population carried more of them |
| **Where the loss is located** | in the **person** — a disposition people brought or developed | in the **arrangement** — in the tier structure, the enclosure spec, and the grid spec |
| ⭐ **TENSE — where and when the loss happens** | **PUNCTUAL and FINISHED.** It occurred at the transition; the transition is over; the city that remains has completed the event | ⭐⭐ **CONTINUOUS and ONGOING.** It accrued across an unwritten but long stretch of 248 years and was merely **REALIZED** at the transition. **The arrangement that produced it is still running afterward, unchanged, on the people who stayed** |
| **Who could name it** | those who left, about themselves | ⛔ **nobody — by construction.** A diffuse, unsponsored, unpolicied cost has no natural author and no natural occasion |
| **What a reform would have to change** | nothing; the event is over | **the allocation rule itself** — which nobody has ever formulated as a rule |

> ## ⭐⭐⭐ THE SYNTHESIS NEITHER READING GIVES ALONE
> **Both are true, at different scales, and the second produced the first:** the preference was real and
> individual; the allocation was real and structural; **the allocation is what the preference was a preference
> about.**
>
> ### And the joint claim, which is invisible to either reading by itself:
> > # **THE TRANSITION DID NOT CHANGE DAVIS'S ARRANGEMENT AT ALL. IT CHANGED WHO WAS INSIDE IT.**
>
> The 60/40 mandate split, the charge-it-to-the-person rule, the signal-free custodial costs, the two nested
> specifications — **all of it survives the exit intact.** ⇒ ⭐⭐⭐ **the city's capacity to notice its own
> arrangement fell at precisely the moment its remaining population became more content with it.**
>
> ⚠ **Stated as a structural consequence of the arithmetic, NOT as a distributional result** — no spread, no
> mode, no sub-population is asserted, per the Band 5 deferral. ⚠ **And undated:** inherited fire 12 means
> "afterward" cannot be located inside the 248 years.

> ### ✅ THE STEP-3 CHECK `02` DEMANDS
> *"If your step-3 consequence is the same under both readings, you have stopped at step 1 and assumed the
> rest."* **The consequences differ on every one of the five axes, and most sharply on tense** — which `02`
> names as the axis most often skipped and the one that most often separates two readings that otherwise look
> identical. ✅ **The double reading did real work here and was not a formality.**

## 4.5 ⛔ THE SHAPE VERDICT, STATED COMPLETELY

> # **Davis reads BALANCED on the Step 0 input set, and COST-DOMINANT on `G2`/`G4`/`G8`/`G3` plus the extent figure and the obligation tier structure — with a signal-free sub-structure inside the cost quadrant that is characteristic of the cost-ABSENT case.**

**Reported with its input set attached, as `02` §4.0 rule 1 requires.** *"Davis is cost-dominant"* on its own would
be an incomplete claim and is not made anywhere in this file.

⭐ **And the honest composite:** Davis pays a great deal continuously, is told immediately when it stops paying
the loud half, and is told nothing at all when it stops paying the quiet half. **It is cost-dominant in the
things that can report, and cost-absent in the things that cannot** — which is why the place feels well-run from
inside and reads as precarious from the numbers.

⏸️ **A THIRD reading becomes available at Step 5**, when this location's own culture material opens as a check.
⭐ **Its disagreement with these two will be worth more than any of the three individually** *(`02` §4.0 rule 3)*.
**Handed forward.**

---

# 5 · ITEM 5 — EACH DEFICIT'S ADDRESS, AND THE COUNT

**`02` §4.1 PEER-FREE set only.** ⛔ The peer-required set is not reached for; the ONE LOCATION law forbids reading
any counterparty that would populate it.

| # | Deficit | Generator | **Address** | The consequence `02` §4.1 attaches |
|---|---|---|---|---|
| **D1** | **Its own procedural competence is unrecorded** — it inherited text and produced skill, and never wrote the skill down | `G4` | **DIFFUSE** | No counterparty, no politics, **no grievance ever forms.** Produces drift |
| **D2** | **No written failure state for either way in, and no failure mode for the crop** | `G3`×`G2`×`G5` | **IN THE PARENT** | The remedy sits at a scale above this one, so reaching for it means conceding the city cannot manage itself ⇒ **produces UNDER-REPORTING — a shadow with no author** |
| **D3** | **No fresh water from the sky, and no light in phase with the need** *(two faces of one atmospheric fact; counted once, stated as two)* | `G2` | **NOWHERE AT ALL** | Genuinely unremediable ⇒ it never becomes a grievance, because there is no author and no alternative. **It becomes a condition — simply "how water works here"** |
| **D4** | **It cannot make its own equipment** — industrial 5%, and the mandated sector's inputs are the free sectors' imports | `G3` `[COR]` `PA-4` | **DIFFUSE** | The goods arrive along two routes from **no particular place Davis's own material names.** No counterparty ⇒ no grievance ⇒ drift |
| **D5** | **It cannot see the mechanism of its own largest population event** | `G8` | **IN ITS OWN PAST** | **See the evidence check below — it is decisive** |
| **D6** | **What a robot's national origin is made of, and whether it can change** | `G8` | **IN THE PARENT** *(the **Federation**, not the subnet — two-ancestor stamp)* | Under-reporting. ⛔ **Not answered here; slot left open** |
| **D7** | **No channel through which an unsponsored preference can act** | all four | **DIFFUSE** | **See the diffuse check below — it is the sharpest one** |
| — | **In a neighbor's present** | — | ⛔ **UNAVAILABLE IN-RUN, BY LAW** | ⭐ **Not empty because Davis has no neighbors — empty because establishing this address requires reading another location, which the ONE LOCATION law forbids.** ⛔ **Left explicitly open. "Unavailable" must not be read as "none exists"** |

## 5.1 ⭐⭐ THE TWO MANDATED EVIDENCE CHECKS

### Check A — for `IN ITS OWN PAST` (**D5**): *are the people who could NAME this deficit still here?*

> # ⛔ **NO. BY CONSTRUCTION.**
> **The people who used the exit are the 376,718 who left. The 781,596 who remain are exactly those for whom the
> arrangement held.** ⇒ **Davis cannot diagnose this — not from denial, but because its evidence physically
> departed.** `02` §4.1's exact case, and **no internal reform can originate.**
>
> ### ⚠ AND ONE HONEST DEVIATION FROM THE INSTRUMENT, RECORDED RATHER THAN SMOOTHED
> **`02` §4.1 predicts a characteristic NOSTALGIA that is factually correct.** ⛔ **Davis does not produce
> nostalgia here**, because the deficit was never *felt* by the people who stayed — they are not mourning a lost
> capacity, they are living in a place that works for them. ⭐ **What it produces instead is
> SELF-CONFIRMATION**: an account of the city that is correct about everyone who is present, unchallengeable
> because the challengers are gone, and **wrong only about a question nobody is asking.** *The instrument's
> shape holds; its predicted affect does not, and that is worth recording.*
>
> ⚠ **And the past in question is an UNLOCATABLE past** — the transition is undated *(fire 12)*, so the remedy
> lives in a moment nobody can put a year to.

### Check B — for `DIFFUSE` (**D1, D4, D7**): *has anyone here ever had a reason to formulate this as a problem?*

| | Honest answer | Consequence |
|---|---|---|
| **D1** — the unrecorded competence | ⛔ **NO.** The corpus's existence is read as coverage; the skill is demonstrably present and transmitted; nothing ever fails in a way that exposes the gap | **Not merely unaddressed — UNSPEAKABLE.** Reform would require someone inventing the question from nothing |
| **D4** — cannot make its own equipment | ⛔ **NO.** It would take an interruption, and no interruption is written | Same. And `PA-4` forbids supposing one |
| **D7** — no unsponsored channel | ⛔⛔ **NO, AND FOR A REASON THAT IS ITS OWN FINDING** | ⭐⭐⭐ **THE EXIT CONSUMED THE CONSTITUENCY THAT WOULD HAVE NAMED IT.** A remedy-by-departure removes the demand for the remedy. **The people who would have had to formulate the problem solved it privately and individually instead, and left** — and every one of them who did so made it less likely that anyone would ever state it as a problem at all |

> ## ⭐⭐⭐ THE COUNT, AND WHAT THE COUNT MEANS
>
> ```
> DEFICITS ADDRESSED                    7
> DISTINCT ADDRESSES OCCUPIED           4  of 5   (diffuse · in the parent · in its own past · nowhere at all)
>   · diffuse                           3  (D1 · D4 · D7)   — all three fail Check B
>   · in the parent                     2  (D2 · D6)
>   · in its own past                   1  (D5)             — fails Check A
>   · nowhere at all                    1  (D3)
>   · in a neighbor's present           0                   — UNAVAILABLE BY LAW, left explicitly open
>
> DEFICITS THAT CANNOT BE FORMULATED FROM INSIDE DAVIS      4 of 7   (D1 · D4 · D7 · D5)
> ```
>
> ⭐ **That last line is arithmetic, not interpretation, and it explains the shape.** **A city that cannot
> formulate the majority of its own deficits will read BALANCED from inside and COST-DOMINANT from the figures —
> and both readings are correct, because they are answers to different questions.** §4's double reading and §5's
> address count are describing the same property from two directions.
>
> ⚠ **`NOWHERE AT ALL` is earned, not reached for** — `02` warns that most apparent cases are really *diffuse* or
> *in its own past*. **D3 survives the test:** no past Davis had more precipitation, nobody at any scale can
> supply rain, and 68°35′S will not be relocated. **One deficit of seven, and it is the one nobody could ever
> have addressed.**
>
> ⏸️ **`02` §4.2 — THE UNRECOGNIZED INSTRUMENT — IS NOT RUN HERE, DELIBERATELY.** The technique is run *after*
> the capability profile is complete and never before, *"found first it softens the deficit; found second it
> sharpens it."* ⭐ **One candidate is flagged for later and not pursued:** Davis holds liquid water through the
> dark half of the year in basins it cannot drink from — **an abundance unusable in exactly the form in which it
> is abundant.** ⛔ **Not converted into a solution, a technology or a practice here.**

---

# 6 · ITEM 6 — POPULATION ÷ EXTENT

> ⭐ **Step 0 declared the extent band `UNDETERMINED` and expected this item to be BLOCKED. It is not. The figure
> now exists, so the division is valid and the check runs.**

```
                     1,158,314  ÷  410 km²   =   2,825.16  per km²
```

**Source density: 2,825/km². Reproduces exactly.** ✅

- ⛔ **One division, no interpretation**, per `00_RUNBOOK.md` Step 2 item 6.
- ⛔ **Direction honored: extent is the INPUT and density the OUTPUT.** Extent is never derived from density.
- ⏸️ **The extent BAND remains `UNDETERMINED`, and that is a MISSING INSTRUMENT, not an unfilled field.** `01`
  §2.1 defines bands on population only and supplies no extent scale anywhere. ⛔ **Therefore the
  population/extent DIVERGENCE QUESTION cannot be answered in either direction** — there is no extent scale for a
  figure to be divergent against. **Neither asserted nor denied, exactly as Step 0 left it.**
- ⚠ `[COR]` — the extent figure is project-internal derivation and the finding is tagged accordingly. Its status
  is *closed by the coastline ruling rather than individually declared.*
- **Plausibility check — the cheapest in the methodology — PASSES:** the quotient reproduces the source figure to
  the unit, so population, extent and density are mutually consistent.

*(Arithmetic note, not the item-6 result: the same division on Census II gives 781,596 ÷ 410 = **1,906.33/km²**.
`DR-4` fixes Census I as governing; the second figure is recorded only so the two-snapshot instrument is complete
on its face. No finding rests on it.)*

---

# 7 · ⛔ THE "CHOSEN / SELECTED" AMBIGUITY — **RESOLVED IN-PASS, NOT ESCALATED**

**Disposition `A` per `01_Inherited.md` §1.6a: this is a reading-comprehension call the deriving pass is equipped
to make, and Step 2 must resolve it and record which reading it adopted, with reasoning.**

## 7.1 The wording, located

**It is in two places, and they run in OPPOSITE directions.**

### (i) The departure — the spine question inherited from `00.1` §3.3 and `00_Frame.md` §0.6

> ***"When leaving became possible, robots left at substantially higher rates than humans. What about this place
> made that so?"***

**The election is in the verb `left`.** It presumes the population **chose**. `01_Inherited.md`'s load-bearing fire
1 names the alternative in the same breath: *"the census records a **destination, not a gate**"*, and
***"the 781,596 are either STAYERS or a RESIDUE."*** **Stayers is election. Residue is selection.**

### (ii) The arrival — and here the same register is applied to the opposite case

`Specs/Davis.md` **L127 heads the block "Settled:"**, and `00_Frame.md` types Davis a **`Settlement`** —
*"people live here as their home."* ⭐ **But L129 says the founding population is `Australian exiles`, and
inherited fire 5 is explicit: EXILE IS A VERDICT, and only the landing is written.**

> ## ⭐⭐ **"SETTLED" PRESUMES SETTLERS. A SETTLER CHOOSES; AN EXILE IS PLACED.**

## 7.2 The evidence, weighed

**For ELECTION at the departure:**
1. The census's own in-world characterization — *"nobody was born or died in the transition; **they relocated**"*
   — is active voice, and it is the only in-world characterization admitted.
2. `01` §3 and `00_Frame.md` both classify it as **migration to a documented destination**, which is why Davis is
   `LIVING` and not `Declining`.
3. ⭐⭐ **DECISIVE: 126,176 humans departed — 22.39% of Davis's humans.** Humans are not vacuum-capable and are
   altitude-limited. **A capability-based selection cannot produce a better-than-one-in-five human departure
   rate.** ⇒ **A pure selection reading is refuted by Davis's own arithmetic.**

**For SELECTION at the departure:**
1. Fire 1: **eligibility and refusal are unwritten.** The census records a destination, not a gate.
2. Robots are vacuum-capable and not altitude-limited — a capability filter would produce a differential in
   precisely this direction.
3. The exit's physical means is continental infrastructure, and infrastructure of that scale is administered by
   somebody.

## 7.3 ⭐ THE READING ADOPTED

> # **ELECTION AS TO THE ACT. NO CLAIM WHATSOEVER AS TO THE GATE.**
>
> **People went. Whether everyone who wanted to go could, is unwritten and is NOT decided here in either
> direction.**

**Grounds:**
1. The human departure figure **refutes** a pure selection reading on Davis's own arithmetic. *(§7.2, for-3.)*
2. The only in-world characterization admitted is an active-voice relocation.
3. ⛔ **And the gate must not be inferred from its absence in either direction.** That is exactly the error
   `G6`'s null made — a zero returned by an instrument that could not see. **An unwritten gate is unwritten. It
   is not an open gate.**

### ⭐ Which makes the inherited wording BETTER than it looks — because of its own first clause

***"When leaving became POSSIBLE"*** is doing real work. **It locates the change in the world — an option
appeared — rather than in the people, and it asserts an opportunity without asserting an entitlement.** ⇒ **The
question is ADOPTABLE as written**, and it is adopted as the spine question at §8.

### ⛔ Two amendments the adoption carries

1. **"substantially" is re-anchored to the figure.** Per the NO SCORE law, the magnitude is reported flatly —
   **42.13% against 22.39%, a spread of 19.74 pp** — and then asked what *that* number means for *this* place.
   The adverb is not load-bearing anywhere in this file. *(The comparison is Davis's humans against Davis's
   robots — internal, and not a comparison to any other city.)*
2. ⛔ **"Stayers or a residue" is NOT resolved, and Step 2 adopts neither.** ⭐⭐ **What Step 2 adopts instead is
   the claim that survives BOTH readings:** *whichever it was, **the people remaining are those for whom the
   arrangement held.*** That is true under election (they preferred it) and true under selection (it kept them).
   **A finding that survives both readings is the one the spine may safely rest on, and it is the only one
   used.**

## 7.4 ⭐⭐⭐ AND THE SECOND HALF, WHICH IS THE MORE IMPORTANT ONE

**Applying the same test to the arrival gives the opposite answer, and the inherited vocabulary does not mark the
difference:**

> # **AT DAVIS, THE ARRIVAL WAS ASSIGNED AND THE GREAT DEPARTURE WAS ELECTED.**
> **The city's own material calls the first "settling" and the second "leaving," in the same register, as though
> they were the same kind of event. They are opposites on the only axis that matters.**

1. *First order:* the words do not match the facts in one of the two places.
2. *Second order:* ⭐ **a place whose founding was imposed and whose great departure was chosen has no continuous
   story of itself.** The founding generation could not have left. The transition generation did not have to
   stay. **Nothing connects the two conditions, and no single account of "why we are here" can cover both.**
3. *Third order:* ⭐⭐⭐ **Davis's people began with no exit and ended with nothing but an exit — and no
   intermediate channel was ever built between those two states.** **This is D7, arrived at from a completely
   different direction: the reading of two words, rather than the comparison of four generators.** ⭐ **Two
   independent routes to the same structural absence is the strongest corroboration available in a peer-free
   pass.**

⛔ **NOT ESCALATED. Resolved here, as `01_Inherited.md` §1.6a requires, and recorded with its reasoning so the
next step inherits the decision rather than the question.**

⚠ **One consequential note for a later step, stated and not acted on:** the `Settlement` type and the `Settled:`
heading are **not** re-litigated here — Step 0 settled the type and `NO FORCED FIT` bars reopening it for
tidiness. ⭐ **What is recorded is that the word carries an implication the founding facts do not support, and no
finding anywhere in this pass rests on Davis's arrival having been chosen.**

---

# 8 · THE SPINE

> # ⭐⭐⭐ **DAVIS IS A PLACE WHERE EVERYTHING THAT GOVERNS A LIFE WAS DECIDED BEFORE THAT LIFE BEGAN — THE GROUND, THE RECORD, THE COMPOSITION, THE OBLIGATION — AND THE ONLY DECISION IT EVER LEFT TO A PERSON WAS WHETHER TO BE HERE AT ALL.**

**Each clause is seated on a generator, so the sentence cannot float free of its evidence:**

| Clause | Seated on | The fact |
|---|---|---|
| *the ground* | `G2` | 410 km² of rock that does not move, a calendar that cannot be negotiated, and a built environment older than any explanation of it |
| *the record* | `G4` | a terrain description that arrived accurate, has stayed accurate, and was never about what anyone would actually have to do |
| *the composition* | `G8` | 21 origins with the largest at 19.04%, so nothing load-bearing can be tacit and everything must be explicit |
| *the obligation* | `G3` `[COR]` `PA-3` | 35% mandated-full, 25% mandated-half — 60% of the workforce's purpose fixed above the city |
| *the only decision* | `G8` + §3.6 + §7.4 | four generators and a two-word reading independently return the same absence: **no channel for an unsponsored preference except departure** |

> **Test 1 — delete every other city's name:** none appears. The claim stands. ✅
> **Test 2 — does it require knowing anything about any other place to be true?** No. ✅
> **Translation discipline:** no generator vocabulary appears in the claim itself. ✅

## 8.1 The two sub-spines

> ### ⭐ **THE SHADOW** *(from §3.5 and §3.6, and it satisfies `00d` without being derived separately — `02` §3.2)*
> **Nothing here announces its own failure except the things that keep people warm and lit. Everything else
> lapses — later, then rarely, then not — and the reliability of the loud half is the evidence offered for the
> quiet half.** ⭐ **Unintended, authorless, invisible from inside, and everybody is acting in good faith.**

> ### ⭐ **THE DEFICIT ENGINE** *(from §5)*
> **Davis cannot formulate four of its seven deficits from inside itself** — three are diffuse and have never had
> an occasion, and the fourth's witnesses departed. **So the city reads balanced from inside and cost-dominant
> from the figures, and both are correct.**

## 8.2 ⚠ WHAT THE SPINE DELIBERATELY DOES NOT SAY

- ⛔ It does not say Davis is unhappy, oppressed, or badly run. **Nothing here has a villain**, and the
  competence on display is genuine.
- ⛔ It does not say who left or which communities. Foreclosed by the model.
- ⛔ It does not say researchers are robots, or growers human. **Not answerable; slot open.**
- ⛔ It does not say when anything happened inside the frame. The transition is undated.
- ⛔ It does not compare Davis to anywhere. No other location was read.

---

# 9 · ✅ WHAT DAVIS VALUES AND TRADES — recordable by ruling, and recorded

**`00.1` §6 and `00_Frame.md` §0.5 item 6 both state this affirmatively: what Davis values and trades IS
recordable and should be, as the input a future currency pass will need.**
⛔ **Nothing below prices anything, names a unit, or describes a wage, fee, tariff or freight rate.**

| | |
|---|---|
| **What it values** | ⭐ **The retrievable reason** — a practice you can look up outranks a practice you were told *(`G4`)*. ⭐ **The held stock** — a thing kept against a season you cannot see is worth more here than a thing consumed on time *(`G2`)*. ⭐ **The completed task** — worth is measured by finishing, not by enduring, because the environment never made the finishing doubtful *(`G2`)* |
| **What flows OUTWARD** | **Food**, as a non-negotiable obligation `[COR]` `PA-3`. Oasis resources — lakes, fjord access, terrain diversity — and Prydz Bay maritime trade *(L148 ⚠ **re-flagged: a declared placeholder, export-shaped, "Full detail TBD"**)*. Research output, at the half-mandated grade |
| **What flows INWARD** | ⭐ **Everything the 5% industrial share cannot make** — the panes, lamps, pumps, seals and lines the mandated sector runs on. ⚠ **This is the more characterizing half and inherited canon is silent on it** *(Step 1's third guard)*. Books, through libraries that welcome them *(a broader Tepenian practice, ⛔ not Davis's own)* |
| ⭐ **The relation, stated as `02` permits** | **What this place needs from elsewhere: the means of meeting an obligation it cannot refuse.** ⛔ **Direction only; no volume, no rate, no counterparty named.** `PA-4` |

---

# 10 · COMPLIANCE LEDGERS

## 10.1 The fourteen load-bearing fires — how Step 2 was CONSTRAINED by each

| # | Fire | How this step honored it |
|---|---|---|
| **1** | The orbital exit is a mechanism-shaped hole | §2.3(c), §7.3 — **the gate is not inferred in either direction**; the spine rests only on what survives both readings |
| **2** | Hard ceiling: no per-nation differential retention | §0.3, §2.3 — **never attempted**; the roster is used for its shape only (21 origins, largest 19.04%) |
| **3** | Founding wave 4.93% vs Primary 19.04%, nothing in between | ⛔ **Not filled.** No arrival wave, date, order or mechanism is invented. ⭐ §2.3(b) uses only what the roster's SHAPE forces, which needs no wave history |
| **4** | `L127`'s documentary conversion: cost unwritten, no-route-back unperceived | ⭐ **This is the pass's richest seam** — §2.2(b), §3.3. **Carried flagged, and the cost asymmetry is written as the finding rather than closed** |
| **5** | Exile is a verdict; only the landing is written | ⛔ **Not invented.** §7.4 uses only the fact that exile is a verdict, which is what the fire itself establishes |
| **6** | The Saint exclusion | ⛔ **Not used at all.** No custom, honorific or holiday anywhere near the namesake. §10.3 |
| **7** | Two ways in, neither failure state written | §2.4(c), **D2** — recorded as a deficit with an address; ⛔ no closure, season or duty cycle invented |
| **8** | A breadbasket with no failure mode and no growing season | §2.4(b)(c), **D2** — and §2.4(b)'s *a bad year here has an author* is derived from the ENCLOSURE, not from an invented bad year |
| **9** | ~400 km² of exposed rock, not worked, no in-world reason | ⭐ **Read as STRENGTH (it holds still) rather than as an unexploited resource.** ⛔ Reserved finding `A-1` NOT converted; ⛔ no other city's role imported |
| **10** | Libraries: an admission mechanism with only an entrance | §2.2(c) — used once, tagged `[ND]`, and ⛔ **explicitly not claimed as originated here** |
| **11** | The tier system admits and never subtracts | §2.3(d) — used as the source of a permanently loaded induction burden. ⛔ **Guard honored: tiers are a production weight, not a social fact** |
| **12** | Nothing dates the Census I→II transition | ⭐ **Load-bearing throughout §4.4** — it is why the divergence table's TENSE axis can name a direction and not a date, and why §8.2 refuses a chronology |
| **13** | What is a robot's national origin made of? | **D6**, addressed **in the parent (Federation)**, ⛔ **not answered.** And §2.3's tolerance cell uses the *unstatedness* itself as the cost |
| **14** | Is the ice-free boundary fixed, seasonal, or moving? | §2.1 DEFICIT — the 410 km² bound is recorded, ⛔ **and its behavior is explicitly left unwritten**, not assumed fixed |

## 10.2 `G6` — disposition `A`, discharged

**`01_Inherited.md` §1.6a: *"Resolves at Step 2. If Step 2 does not need `G6`, it stays a recorded null through to
Step 9 — either way, no developer input required."***

> ## ✅ **STEP 2 DOES NOT NEED `G6`.**
> The rule of three is satisfied three times over on `G2`/`G4`/`G8` alone; a fourth generator was exercised; the
> shape, the addresses, the division and the spine are all fully determined without any defining event.
> ⛔ **No isolated reader is dispatched. The matching line in the 346-line file is not opened.**
> ⛔ **And the inference one reader drew from the quarantined line's length, word count and punctuation is NOT
> relied on anywhere** *(`01_Inherited.md` §1.5)*.
> ⇒ **`G6` stays a recorded null — neither established nor disproved — through to Step 9.** `PA-5` is not built on.

## 10.3 ⛔ RESERVED — compliance check, all six

| | Reserved | Status in this file |
|---|---|---|
| **1** | **Proper names of people** | ✅ **Zero.** ⭐ **And the second route is clear too** — no practice, method, tool or institution is named after anyone. ⛔ **The namesake at L64/L131 is not built on in any form**: no figure, honorific, holiday or founding story |
| **2** | **The demonym** | ✅ **Zero adjectival forms.** The file writes *"residents of Davis," "people here," "the city's growers."* ⚠ Swept deliberately, since the pull is real |
| **3** | **Which DLC covers this subnet** | ✅ Nothing presumes a player, hub, quest, gate or companion |
| **4** | **Disposal of the dead** *(highest risk)* | ✅ **Not touched.** ⭐ §2.1 states the rock as a STRENGTH of foundation and storage only. ⛔ Reserved finding `A-1` is not converted; no mortuary practice, site or material is named or implied |
| **5** | **`G1`'s Element meaning** | ✅ **§2.5 states the trap explicitly and closes it.** No sentence anywhere joins Davis's ground or agriculture to the symbol |
| **6** | **Early-Federation currency** | ✅ **Nothing priced.** §9 records values and flows without a unit, wage, fee, tariff or rate |

## 10.4 Other standing laws

- ✅ **ONE LOCATION.** No other city is named, ranked, used as a control or implied as a normal. **No `nth of N`,
  no z-score, no corpus superlative.** ⚠ Both one-sentence tests were applied at §3.6, §8 and on every comparative
  formulation. **The two admitted strikes on L117 and L120 — the implicit-normal cases — are not reproduced.**
- ✅ **NO SCORE IN-RUN.** Every figure is Davis's own, stated flatly, followed by *what does that number mean for
  this place*.
- ✅ **BAND 5 MACHINERY DEFERRED.** No spread, mode, sub-location or distributional claim. Base-level fundamental
  facts only, at a declared Band 5.
- ✅ **NO FORCED FIT.** Four slots are left explicitly open and each says so in the affirmative: **the air slot**
  (§2.1e), **the neighbor's-present address** (§5), **whether the residual-vocation population is the departing
  population** (§2.4a), and **what a robot's origin consists of** (§2.3, D6). ⛔ No roster member was assigned and
  no bespoke one invented.
- ✅ **ROBOTS ARE THE MAJORITY.** 594,715 of 1,158,314 at Census I, 51.34%. **Every quadrant was written with that
  in front of it**, and the majority's position is the subject of §2.3(c), the sharpest finding in the file. Cold
  is treated as a preparation problem on different axes, never as a gate.
- ✅ **LAW 0.** Every finding in §2 was run to a third order and several to a fourth; first-order observations
  (*"it is cold," "it grows food"*) appear only as starting conditions.
- ✅ **NO RESEARCH.** No web search, no reading outside the contracted list. The airstrips and READER files were on
  the list.
- ✅ **American English throughout.**

---

# 11 · HANDED FORWARD

| To | Item |
|---|---|
| ⛔ **Step 3** | **`LAW 0-R` binds, and `G7`'s research half is unbuilt.** ⭐ **Step 2 produces a specific brief for it, which is what Step 2 owes Step 3:** the water budget of a closed-basin oasis · what an enclosure specified for a crop is like to work in · the legibility lifetime of a written record across centuries · what a 68°35′S light distribution does to a cultivation calendar. ⛔ **Do not research these at Step 2** |
| **Step 3** | ⭐ **Create `Davis_Research_Log.md`** — verified absent; verbatim search strings, dead ends, and the *changed a finding vs. ornamented one* column |
| ⭐ **Step 4** | **`02` §4.2's UNRECOGNIZED INSTRUMENT candidate, flagged and NOT run:** Davis holds liquid water through the dark half-year in basins it cannot drink from. **Run it after the profile, never before** |
| ⭐ **Step 5** | **The THIRD input set.** `Local_Cultures/` and `Local_Robot_Culture/` open as a CHECK. ⭐ **Run the shape a third time and table the disagreement against §4.4** — `02` §4.0 rule 3 says it will be worth more than any single reading |
| **Step 5** | ⚠ **Pre-declared non-independence, `[ND]`:** if the culture material contains a harvest-versus-archive tension, **that is CORROBORATION AT BEST and must be tagged.** §2.2(c) states in advance exactly what this pass did and did not claim, so the audit is possible |
| **Step 7** | ⚠ Gate 6 and the withheld district originals. §3.3's *misplaced citation* finding and §2.3(c)'s *two nested specifications* finding are the two most likely to meet canon — **run `02` §5.3's both-are-true test before recording either as a kill** |
| **Step 8** | ⭐ **The Review Panel's `unmet` test in peer-free form** will bear hardest on §3.6 and §8: an objection that Davis should have a grievance culture, a founding myth, or a weather-lore would **replace something specific to this place with something true anywhere.** Expect `unmet`, and write the refusal as characterization |
| **Step 9** | ⛔ Davis's column is added to the differentiation table **write-only**. `G6` remains a recorded null |
| ⏸️ **Methodology, not a blocker** | ⭐ §1.2 — **a function generator read off a canon line that names its own geographic derivation is not independent; what rescues it is the OBLIGATION half.** Proposed as a `02` §5.1 addition |
| ⏸️ **Methodology, not a blocker** | ⭐ §4.2 — **obligation data is shape-determining even as inert percentages**, which widens `02` §4.0 past *"known institutions"* |
| ⏸️ **Methodology, not a blocker** | ⭐ §5.1 — **`02` §4.1's `in its own past` predicts nostalgia; where the deficit was never FELT by those who stayed, it produces SELF-CONFIRMATION instead.** The structure holds; the predicted affect does not |
| ⚠ **Still outstanding from Step 0, not re-raised as a question** | `01` §5.2 rule 5 — **no Mirny-subnet registry exists to write `PA-1`…`PA-6` into.** An obligation for the pass owner, unchanged |

---

# 12 · VERDICT

> # ✅ **SPINE BUILT — READY FOR CROSS-CHECK**

**Strongest reason:** the four quadrants agree in three rows and conflict productively in the fourth, and **the
two conflicts both resolved under `02` §5.3 into claims stronger than either half** — the accuracy of the
inheritance turns out to be a function of the same stability that makes the environment severe, which converts a
handed conflict into the pass's sharpest finding. **Three independent generators converge on one cognitive shape
(balances rather than journeys); two independent generators converge on explicitness; and four generators plus a
two-word reading converge on the same structural absence.**

**Biggest doubt, carried forward:** ⭐ **§2.3(c)'s account of the retention spread is the load-bearing finding and
it rests on two facts of different tiers** — an in-frame design statement extracted from a document whose
narrative is entirely post-war, and a `[COR]`-tier tier structure. **Both are honestly sourced and both are
tagged, but if either is later withdrawn, the local account of the spread loses a leg and the question returns
open.** ⚠ **The general-capability explanation would still be available, and it would still not be a Davis
finding.**

**Second doubt:** ⚠ **`G3` was confirmed as a fourth generator only in its obligation register**, which is
`[COR]`-tier. **If the tier extraction is not ratified, the pass falls back to three generators and the shape
falls back to BALANCED** — §4.4 already tables exactly what changes, which is the point of having run it twice.

⛔ **Step 3 — RESEARCH — opens next.**

---

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md
LRANGE: 2497-2525
LINES: 29
L1: # Step 2 — Build the spine
LMID:    > once on the full one.* **1.** The shape gives the question. **2.** The generator gives the instrument.
LLAST:
QUOTE: Read each deficit's **address**, and **count the addresses.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md
LRANGE: FULL
LINES: 760
L1: # Generators, the Capability Frame, and Symbol Binding
LMID: **So the derivation runs the other way from the district method:** rather than deriving a shadow separately and
LLAST:    emphasis.**
QUOTE: The second answer is the stronger one, and it is the shadow.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Davis.md
LRANGE: 1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179
LINES: 137
L1: # Davis
LMID: **Mean annual temperature:** -10.0°C  _(READER station: Davis; 1991–2020 WMO standard normal)_
LLAST: - **Relationship to Mawson (the city, different subnet)** — both named for/connected to Australian Antarctic figures, but administratively and geographically separate; worth clarifying whether any cultural connection existed despite the subnet divide
QUOTE: Davis is, above all, Tepenia's breadbasket and a prime ecological/limnological research hub — sheltered-agriculture and greenhouse cultivation alongside genuine research heritage make up the clear majority of daily activity.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Energy_Grid_Failure_Rationale.md
LRANGE: FULL
LINES: 145
L1: # Why "Just Fix the Energy Grid" Isn't a Practical Solution
LMID: infrastructure could replace.
LLAST: - **Climax (The Great Blackout):** All the half-measures and compromises finally catch up, forcing the player to make the ultimate choice about the future of the entire system.
QUOTE: The grid was originally designed primarily for pre-war human needs.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Davis.md
LRANGE: FULL
LINES: 16
L1: # Climate Reference: Davis
LMID: **Annual mean temperature:** -10.0°C
LLAST: _Source: BAS READER (Reference Antarctic Data for Environmental Research), https://legacy.bas.ac.uk/met/READER/ — cite as Turner et al. (2004), Int. J. Climatol. 24, 191–211._
QUOTE: | +0.9 | -2.2 | -8.0 | -13.5 | -16.0 | -15.7 | -17.1 | -17.1 | -15.7 | -11.8 | -4.2 | +0.0 | -10.0 |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md
LRANGE: FULL
LINES: 99
L1: # Antarctic Stations With Functional Airstrips / Aircraft Ground Infrastructure
LMID: | Plog Island Skiway | Davis Station | Australia | Ice |
LLAST: - Several names on this list use "skiway" specifically (a compacted snow or ice surface usable only by ski-equipped aircraft) as distinct from a genuine wheeled-aircraft runway (gravel or blue ice, usable by wheeled cargo planes) — this distinction may matter if Tepenia's own lore wants to differentiate between "reachable by any aircraft" and "reachable only by specialized ski-equipped planes."
QUOTE: Most Antarctic airstrips are seasonal (open only during the austral summer, roughly October–March) and conditions/operators can change year to year.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md
LRANGE: 392-398,496,613
LINES: 9
L1: **Davis** *(Vestfold Hills, Prydz Bay — mainland coast)*
LMID: | Primary | China |
LLAST: | 14 | Davis | Mirny | 437,423 | 344,173 | **781,596** | |
QUOTE: | 13 | Davis | Mirny | 563,599 | 594,715 | **1,158,314** | *(revised 2026-07-04)* |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00.1_Step_MINUS-1_Input_Contract.md
LRANGE: FULL
LINES: 371
L1: # Davis — Step −1 · THE INPUT CONTRACT
LMID: > **L127:** *"No living environmental **knowledge** survived that chain of handoffs — but preserved journals,
LLAST: ⛔ **Step 0 — FRAME — opens next.**
QUOTE: **Founding population: Australian exiles (L129).** ⭐ **A documentary inheritance without a living institution

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00_Frame.md
LRANGE: FULL
LINES: 397
L1: # Davis — Step 0 · THE FRAME
LMID: declares two numbers **so that the second checks the first** — *"when they diverge, the divergence is
LLAST: ⛔ **Step 1 — AUDIT WHAT IS INHERITED — opens next.**
QUOTE: **Generators selected:**  G2 (physical) · G4 (founding) · G8 (composition) — with G3 (function)

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/01_Inherited.md
LRANGE: FULL
LINES: 363
L1: # Davis — Step 1 · WHAT IS INHERITED
LMID:
LLAST: ⛔ **Step 2 — BUILD THE SPINE — opens next.**
QUOTE: > **The one enormous outflow — 376,718 people — is recorded as a NUMBER and never as a MECHANISM.**


## ROUND 1 · READER B — raw

---

# Davis — Step 2 · BUILD THE SPINE

**Frame: Second Interwar (2564–2812)** · Reader B, independent draft · written 2026-09-15

> **Governing:** `00_RUNBOOK.md` §"Step 2" **L2497–2525** · `02_Generators_Capability_and_Symbols.md` **760 lines,
> in full**. **Inputs:** this pass's own `00.1`, `00_Frame.md`, `01_Inherited.md`; `Specs/Davis.md` at the
> ratified **137-line** read spec; `Official_Population_Census.md` L392–398/496/613; the READER climate
> reference; `Energy_Grid_Failure_Rationale.md`; `Antarctic_Stations_With_Airstrips.md`.
>
> ⛔ **No research performed.** `00_RUNBOOK.md` L2523–2524: *"Do not research yet."* Nothing below rests on a
> web source, and every candidate for Step 3 is filed as such rather than answered here.

---

# 0 · WHAT IS IN FORCE BEFORE THE FIRST WORD IS WRITTEN

| Constraint | Effect on this step |
|---|---|
| **ONE LOCATION** | No city named, ranked, or used as a baseline. **RELATION is used freely** — what flows, in which direction. Both tests applied on sweep: the one-sentence test, and *"does this claim require knowing anything about any other place in order to be true?"* |
| **DR-4 — Census I governs** | `1,158,314` → **Band 5**. The Census I→II change is **relocation, not loss**, and remains admissible `G8` material |
| **Band 5 machinery deferred** | ⛔ **No finding below is presented as a distributional result.** Where a finding would naturally continue into a sub-location layout or a spread, it stops and says so |
| **NO FORCED FIT** | Empty slots are written as empty. Four are declared in §9 |
| **RESERVED ×6** | No person-names (nor practices/tools/institutions named after a person) · no demonym · nothing presuming a player or DLC · **disposal of the dead: reserved finding `A-1` restated and NOT converted** · `G1`'s Element meaning · no currency, price, wage, fee, tariff or freight rate. ✅ **What Davis values and trades IS recorded** |
| **GENERAL-POPULATION DISCIPLINE** | The admitted set describes **growers and researchers**, and both are roles. ⛔ **Nothing below answers a general-population question from either.** §9's second empty slot is the direct consequence |
| **TRANSLATION DISCIPLINE** | Generator labels appear only as bracketed citations. No claim about Davis uses the vocabulary of the instrument that produced it |
| **Tiers** | `[ratified]` = spec/census canon · `[corroboration]` = the Division-of-Industry tier extraction and the real-world airstrip reference, both project-internal or caveated at source · `PA-3` = rests on the food obligation running outward |

---

# 1 · ⛔ TIME-CRITICAL — THE "CHOSEN / SELECTED" AMBIGUITY, RESOLVED IN-PASS

**`01_Inherited.md` §1.6a classifies this ✅ **A** — *"resolves AT Step 2 … Step 2 must resolve it in-pass and
record which reading it adopted, with reasoning — it must NOT escalate this upward."* It is taken first, before
any profile is run, because it governs how `G8` and `G3` may be written at all.**

## 1.1 The wording is at THREE sites, not one

**Searching the inherited material for phrasing that presumes the population *elected* something it may have
been *assigned* returns three distinct sites. They are not the same claim and they do not resolve the same way.**

| | Site | The inherited wording | What it presumes |
|---|---|---|---|
| **(i)** | **THE VOCATION** | `00.1` §3.2 and `00_Frame.md` §0.7: *"residents understand themselves as researchers while the polity above them requires calories"* | that the research half is **Davis's own election**, set against an **imposed** food role |
| **(ii)** | **THE DEPARTURE** | `00.1` §3.3 / `00_Frame.md` §0.6: *"when leaving became possible, robots left at substantially higher rates than humans"*; and the era file's *"how hard a given place **used** that exit"* | that departure was an **act**, taken by those who took it |
| **(iii)** | **THE RESIDUE** | the same sentence read backwards — the `781,596` as *"who stayed"* | that remaining was also an **act** |

## 1.2 Site (i) — THE VOCATION. **Election REFUSED. The evidence positively contradicts it.**

**Go back to the only line in the admissible set that says what Davis is for** `[ratified]`:

> **`Specs/Davis.md` L143:** *"Davis is, above all, Tepenia's breadbasket and a prime ecological/limnological
> research hub — sheltered-agriculture and greenhouse cultivation alongside genuine research **heritage** make up
> the clear majority of daily activity."*

**Three things are true of that sentence and none of them were carried forward:**

1. ⭐⭐ **Both halves are PARENT-FACING.** *"Tepenia's breadbasket"* states a role relative to the nation.
   *"A prime ecological/limnological research **hub**"* also states a role relative to a network — a hub is a hub
   *of* something larger. **Neither clause describes how anyone here understands themselves.**
2. ⭐⭐⭐ **The line's own word for the research half is "heritage."** ***A heritage is received, not elected.***
   If anything in the sentence leans, it leans away from election on **both** sides.
3. **`02` §G3 instructs the pass to split the question in two — *what is this place for on its own terms* and
   *what does its parent need from it*. At Davis only the SECOND has an answer.** The first is not answered
   badly; it is **not answered at all**.

⇒ ⛔ **The inherited G3 tension does not survive in the form it was handed.** *"Researchers by self-understanding
versus growers by obligation"* is a two-tribe reading built on a self-understanding the canon does not contain.
**It is the first plausible answer, and `02`'s LAW 0 names that as the generic one.**

⇒ ✅ **What survives, and it is better:** **Davis has two parent-facing roles of unequal weight and no recorded
self-facing purpose at all.** The unequal weight is measured — **agriculture 35% of the workforce against
technical/scientific 25%** `[corroboration]` — and the corpus reproduces L143's *"clear majority"* exactly, at
**60%** of a **876,514** workforce baselined on Census I.

> ### ⚠ AND A LAYER TRAP AVOIDED, RECORDED BECAUSE IT NEARLY CARRIED THE ARGUMENT
> **The tier extraction also labels agriculture `MANDATED (FULL)` and technical/scientific `MANDATED (HALF)`,
> with the other four sectors `FREE`.** ⭐ **A first draft of this section argued that *both vocations are
> mandated, therefore neither was chosen.*** ⛔ **That argument was killed.**
>
> **`01_Inherited.md` §1.1's layer ruling is explicit — *"Gate 9 scores the IN-WORLD layer. A revision history
> is not a mechanism"* — and fire #11 carries the matching guard for the composition tiers: *"a production
> weight, not a social fact."*** **`MANDATED`/`FREE` is at least as likely to mean *fixed by canon versus open
> to the designer* as it is to mean *required by a polity*, and the sheet's own definition of the FULL/HALF
> split is not in this pass's admissible set.**
>
> ⇒ ✅ **The argument was rebuilt on the PERCENTAGES alone, which are in-world-readable, and on L143's word
> *"heritage,"* which is ratified.** **It reaches the same verdict without importing an authoring artifact into
> the fiction.** ⛔ **No finding in this document rests on the `MANDATED`/`FREE` labels.** *The 35 > 25
> weighting is used; the mandate semantics are not.*

## 1.3 Site (ii) — THE DEPARTURE. **Election ADOPTED for MOTIVE. Selection is real at the level of SEQUENCE.**

**For:** the only two direct descriptions in the admitted set are **"migration"** and, in the census's own words,
**"they relocated"** — both active, neither passive, and **no compulsion mechanism appears anywhere in the
inherited corpus.**

**Against pure selection, and this is decisive because it is arithmetic:**

```
robots  594,715 -> 344,173     57.87% remained    250,542 departed
humans  563,599 -> 437,423     77.61% remained    126,176 departed
```

⭐ **57.87% of robots stayed and 126,176 humans left.** A destination-side draft on what robots are — vacuum
capability, no altitude limit — **would not produce departures in both populations at those proportions.**
**Whatever ran the exit did not sort on being a robot.** ⇒ **The differential needs a person-side or a
Davis-side explanation, which is exactly what the inherited question asks for.** ✅ **The FIRST half of the
inherited question survives contact with the numbers.**

**But selection is nonetheless real in one specific register.** The frame's own epistemic horizon has Amundsen
Tower **completed ~2688 and operating** — mechanically *"a continent-scale flywheel,"* a continuously
circulating pellet stream drawing **~324 GW net** `[ratified]`. **A lift at that standing draw is a scheduled
service, not an open door.** Moving **376,718** people out of one city through that channel has an **order**,
and an order is an **allocation**. ⇒ ⭐ **Motive may be elective and sequence is necessarily allocated. The two
words describe different objects and both are true** *(`02` §5.3, applied to a wording rather than to a
generator)*.

## 1.4 Site (iii) — THE RESIDUE. **Election REFUSED. This is the half that matters.**

**"Leaving became possible" describes a PERMISSION. It does not describe a CAPACITY.** A permission plus a
finite channel is a **queue**, and a queue has three outcomes where a census records two:

```
went   ·   did not want to go   ·   wanted to go and did not
```

**A census counts locations, not intentions.** ⇒ **`01_Inherited.md` fire #1 is right that the 781,596 are
*"either stayers or a residue"* — and the honest answer is that they are BOTH, in a proportion no admitted input
can supply**, because eligibility, refusal, durability and any return trip are all unwritten.

> ## ⛔ THE ADOPTED WORDING RULE, BINDING ON EVERY LATER PHASE OF THIS PASS
>
> | ✅ LEGAL | ⛔ FORBIDDEN |
> |---|---|
> | *"people left"* · *"the city retained 67.48%"* · *"departure was available"* · *"Davis's robots retained at 57.87%"* | *"those who stayed chose to stay"* · *"the people here are the ones who wanted this place"* · *"committed"* · *"the ones who believed in it"* · **any characterization of the remaining population as self-selected** |
>
> ### And the inherited question is re-stated, minimally, to strip the presumption:
> **FROM:** *"When leaving became possible, robots left at substantially higher rates than humans. What about
> this place made that so?"*
> **TO:** ***"Davis's robots retained at 57.87% and its humans at 77.61%. What differs, at Davis, between those
> two populations' relation to this place?"***
>
> ⭐ **Why the re-statement is not cosmetic.** The old form admits only **Davis-defect** answers — *robots left
> because Davis was bad for robots* — which is the generic answer and also an accusation. **The new form admits
> a structural, blameless answer, and §3's comparison produces one** *(F5, below)*: **no defect, no villain,
> everyone in good faith**, which is `00d`'s shadow standard restated.

> ### ⭐⭐ WHAT THIS RESOLUTION COSTS — stated plainly, because it takes something away
> **Davis may no longer be written as a place whose residents chose it.** That is the most natural and most
> flattering thing a city can believe about itself, and **it is the thing this pass is now forbidden to write.**
> ⭐ **In exchange it gets a shadow that is authorless and discoverable:** *if the city's own self-account
> assumes the remaining population elected to remain, then anyone here because their departure did not happen is
> **invisible inside that account, and there is no word for them.*** **Nobody banned it; nobody enforces it;
> it costs anyway.** ⏸️ **Not developed further here — `00d` proportion discipline, and Band 5 forbids sizing
> it. Handed to Phase 4/7 as an un-sized qualitative claim.**

---

# 2 · ITEM 1 — GENERATOR SELECTION: **CONFIRMED, WITH ONE CORRECTION TO ITS STATED RATIONALE**

**`00_Frame.md` L150–152: *"G2 (physical) · G4 (founding) · G8 (composition) — with G3 (function) carried as a
fourth BECAUSE it is the fragile one and must be exercised, not leaned on."***

## 2.1 The independence test, run properly — and G2 × G3 FAILS it

**`02` §5.1 rule 2: *"Select at least three, chosen for independence rather than for strength. Three generators
that all descend from the same fact are one generator wearing three hats."***

| Pair | Independent? | Ground |
|---|---|---|
| **G2 × G8** | ✅ **Yes** | Climate and terrain do not produce a composition table; the composition table says nothing about rock |
| **G2 × G4** | ✅ **Yes** | The founding condition is a statement about **what the founders had** (a documentary corpus, no living teachers); the physical facts are a statement about **what the site is**. Neither derives the other |
| **G4 × G8** | ✅ **Yes** | The founding population is one named community; the composition is twenty-one. **`01` fire #3 records that nothing is written between them** — which is precisely the evidence they are not one fact |
| **G3 × G8** | ✅ **Yes** | — |
| **G3 × G4** | ✅ **Yes** | The founding says nothing about food; the function says nothing about documents |
| ⛔ **G2 × G3** | ⛔ **NO — PARTIALLY DEPENDENT** | **L143 derives the function from the geography in its own sentence:** *"Davis's own unique geography … genuinely **fits it for** the ecological-research/breadbasket role."* **The function was assigned BECAUSE of the physical facts** |

> ### ⛔ THE CONSEQUENCE, AND IT CHANGES HOW §3'S TABLE IS READ
> **`02` §5.2: *"All three agree → well-grounded. Build hard on it."*** ⛔ **That license does NOT extend to a
> G2 × G3 agreement about whether the terrain suits cultivation, because that agreement is one fact read
> twice.** **Every such cell below is marked `agree (NON-INDEPENDENT)` and is explicitly NOT used as
> grounding.**
>
> ⭐ **The dependency is specific and does not contaminate the whole column.** It runs only through the claim
> *terrain ⇒ suitability for the role*. **G2 × G3 cells about the CALENDAR — when work is possible, when damage
> occurs, which obligation has a season of its own — are not downstream of that derivation and ARE grounding.**
> *The distinction is made cell by cell in §3.2, not asserted wholesale.*

## 2.2 Verdict

> ## ✅ **SELECTION CONFIRMED. The rule of three is met by G2 + G4 + G8 — three mutually independent generators.**
> **G3 is carried as a HALF-INDEPENDENT fourth and is exercised, not leaned on.**

⭐ **And this supplies the reason Step 0 did not state.** `00_Frame.md` called `G3` *"the fragile one"* and
grounded that on `00.1`'s *"L143 — one line, and only one."* **That is true and it is the smaller half of the
problem.** ⭐⭐ ***The larger half is that the one line derives G3 from G2, so leaning on G3 would have been
leaning on G2 a second time under another name.*** **Step 0's instinct was right for a reason it had not found.**

**Not selected, and why — each a result rather than a gap:**

| | Standing | Handling here |
|---|---|---|
| **G1** | **Counts ZERO.** Pair is `Earth / Earth`; Element meaning **RESERVED** (`DR-1`) | ⛔ **The check cannot be run at all — see §8** |
| **G5** | Present, **volume never stated** | Used for **direction only** (`PA-4`). ⛔ Nothing scaled off throughput. ⛔ No meaning read off `Access type: ON` |
| **G6** | Recorded null whose **ground was withdrawn**; an independent 562-line era timeline returns a **valid zero** | ⭐ **DECLARED: Step 2 does not need `G6`.** The spine rests on no event. Per `01` §1.6a, it therefore **stays a recorded null through to Step 9** — no isolated reader dispatched, no developer input, disposition ✅**A** discharged |
| **G7** | Designation yes, **research unbuilt** | **Step 3's job.** The one real-world item used here is **physical texture only** and tagged `[corroboration]` |

---

# 3 · ITEM 2 — FOUR PROFILES, RUN SEPARATELY

> **`02` §5.1 rule 3: *"Run each one to a four-quadrant profile, separately, before comparing. Comparing too
> early lets the first-read answer contaminate the others."***
>
> **Order run: G2 → G4 → G8 → G3.** ⚠ **G3 was run LAST and deliberately from `L143` plus the sector
> percentages ALONE, without consulting the completed G2 profile**, precisely because §2.1 establishes that G3
> is partially downstream of G2 and would otherwise have restated it. **Recorded as a procedural fact so a later
> reader can audit the order.**

## 3.1 `G2` — PHYSICAL & ENVIRONMENTAL

**Inputs** `[ratified]`: ~400 km² ice-free exposed rock, lakes and fjord-like inlets, Vestfold Hills, Ingrid
Christensen Coast, Prydz Bay · mean annual **−10.0 °C** · monthly means Jan **+0.9** / Dec **+0.0** / Jul–Aug
**−17.1** · mean daily maxima Jan **+3.2**, Dec **+2.4**, Feb **−0.2** · record high **+13.0**, record low
**−41.8** · wind **~5.6 m/s**, **out of the katabatic regime** · precipitation **72.8 mm falls / ~28 mm lands /
~44.8 mm lost**, retention **38.5%** · polar night **37 days**, midnight sun **55 days** · lakes fresh, saline
and **hypersaline**, with **landlocked marine basins**, ice-covered in winter and **partially open in summer**.
`[corroboration]`: the site's three listed aviation surfaces are **plateau ice, sea ice and island ice** — no
wheeled-aircraft surface is listed, and the source defines a skiway as *"usable only by ski-equipped aircraft."*

**STRENGTH**
- **Ground that does not move.** ~400 km² of exposed rock removes, wholesale, the entire class of obligation
  that ice-borne construction imposes. **Anything built here is built on the thing it is built on.**
- **Shelter from the continental wind regime.** At ~5.6 m/s and out of the katabatic flow, **the marginal cost
  of an additional structure is low and the envelope does not have to be armored** — which is what permits
  *glazed* building at all. ⏸️ **The settlement pattern that follows is NOT written** — that is Band 5
  decomposition, deferred by ruling. **Only the permission is recorded.**
- **Light, in quantity, for five months.** Nov 20.3 h · Dec 24 · Jan 24 · Feb 17.2 · Mar 13.1 · Oct 15.2.
- **Water bodies of several kinds, in one small territory** — fresh, saline, hypersaline, landlocked marine, plus
  fjord inlets. **A range of aquatic conditions inside a single walkable landscape.**
- **A working sea coast** at Prydz Bay.

**DEFICIT**
- ⭐ **No free growing season worth the name.** Two months carry a non-negative mean (Jan +0.9, Dec +0.0) and
  exactly the same two carry a mean daily maximum above freezing. **Five consecutive months (May–Sep) never rise
  above a −15.7 monthly mean.** **This is structural and permanent.**
- ⭐⭐ **No water surplus, ever.** 72.8 mm falls, ~28 mm stays, **~44.8 mm is lost to sublimation and wind
  transport — more is lost than is kept.** And **the most abundant standing water is the wrong kind**: saline,
  hypersaline, landlocked marine. ***The landscape looks wet and is in permanent moisture deficit.***
  ⚠ *The hypersaline lakes are themselves the visible signature of that deficit; the two facts are one fact.*
- ⭐ **The rock is not a plain.** *Hills*, cut by *fjord-like inlets*, studded with *lakes*. **The generic
  reading of "400 km² of exposed rock" is a field, and the evidence says otherwise: it is broken, water-cut
  terrain.** `[corroboration]` corroborates from an unexpected direction — **the site lands aircraft on ice, on
  three separate ice surfaces, while 400 km² of rock sits beside them.** ⇒ **The rock cannot be crossed
  straight, and it cannot be landed on.**
- **37 days at zero daylight.** Not modulated, not managed — absent.

**STANDING COST**
- ⭐⭐⭐ **Freeze–thaw, and it runs in SUMMER.** Jan: mean daily max **+3.2**, mean daily min **−1.2**. Dec:
  **+2.4 / −2.2**. ***For roughly sixty consecutive days Davis crosses zero and comes back, every cycle.***
  **Water enters, freezes, expands. That is the single most destructive process available to stone, seal, joint
  and line — and it is the warm part of the year that does it.** ⚠ **"It is cold" is not this city's
  maintenance problem. Cycling is.**
  - **And the cycle has no marker.** It runs inside the midnight sun (Nov 25 – Jan 18), so **there is no night to
    count by.** The spec's own note concedes the point from the other end — at this latitude *"day" and "night"*
    mean the warm and cool parts of a 24-hour cycle, not light and dark.
- **Recovering water against continuous loss.** Sublimation does not wait for melt; anything exposed loses mass
  on a permanent schedule. **A closed loop is not an efficiency here, it is the only available mode.**
- **Watching the ice-free boundary.** `01` fire #14 asks whether it is fixed, seasonal or moving, and who
  watches it. **The pass cannot answer which — but for a city whose whole territory is the unfavorable side of
  that threshold, the watching is a category of work that regenerates the moment it is finished** (`02` §3.1's
  test for a true standing cost).

**GRUDGING TOLERANCE**
- ⭐⭐ **Being outside.** The environment **permits** it more than a katabatic site would — moderate wind, summer
  highs above freezing, five months of long light — **and punishes it at −41.8 °C and 37 days of dark.**
  ***The moderation is the trap: this site reads benign and is not.***
- **Being near the water.** The lakes are *partially open in summer* — water at or near freezing, in a landscape
  that invites approach. ⛔ **Stated as a physical permission-and-punishment only.** *No practice, custom or
  prohibition is written here; that is Phase 7's and not a capability.*
- ⭐ **Believing the summer.** The same season that reads as relief is the season doing the structural damage.
  **Both the person-scale and the fabric-scale versions of the deception agree, and neither is announced.**

## 3.2 `G4` — FOUNDING CONDITION

**Inputs** `[ratified]`: founding population **Australian exiles** (L129). **L127:** *"No living environmental
knowledge survived that chain of handoffs — but preserved journals, logs, and orientation manuals left behind
across the centuries gave the exiles a real documentary starting point for the Vestfold Hills' terrain. Learning
from a written record isn't the same as being taught by a living institution, and the exiles still built their
own practical mastery of the terrain independently, over generations of their own."*
⚠ **Tier: ratified root, UNVERIFIED CONTENT** (`01` §1.5) — *a ratified file does not ratify every sentence
inside it.*

> ### ✅ THE PERSISTENCE TEST, RUN IN ONE LINE AS `01` §1.6 REQUIRES
> **Journals · logs · orientation manuals — would each still be here if the originating nation had left and
> never returned? ✅ YES for all three: paper outlives its custodian.** ⛔ **What does NOT pass, and is not
> used: the handoff chain itself as a source of character, and the operators' identities.** *`DR-7` admits the
> MATERIALS and admits nothing about WHO MADE THEM.*

**STRENGTH**
- ⭐⭐ **Davis has performed the conversion from record to living practice once, at founding, and the canon says
  how long it took: *generations of their own*.** **This is a proven competence, not a claim** — the practical
  terrain mastery is the founding population's own product and it is still here.
- **The inheritance was site-specific and empirical** — *the Vestfold Hills' terrain*, not doctrine. **Whatever
  the founders started from was about THIS ground.**
- ⭐ **The founding method was verification.** Read, go and check, correct. **A founding population whose first
  survival skill was testing a text against the ground is a population for whom the check is not a virtue but a
  habit of origin.**

**DEFICIT**
- ⭐⭐⭐ **No living institution arrived.** `02` §G4: *"the absences are the yield: what the founding generation
  did not bring is very often a permanent hole, because nobody afterwards knew it was missing."* **Here the
  canon names the hole itself** — *"learning from a written record isn't the same as being taught."*
- **A record is authoritative about the permanent and silent about the timing.** A document can say where a lake
  is. **It cannot say when that lake closes, and it cannot tell you whether the year you are in is ordinary.**
- **The founders arrived under a verdict and only the landing is written.** ⛔ **`01` fire #5: threshold,
  decider, reviewability and heritability are absent and *resolve UPWARD*.** **Not Davis content; not
  invented here.**

**STANDING COST**
- ⭐⭐ **Transmission. It never ends and it has no season.** **The founding condition was not a one-time event
  that closed; it is the city's permanent structural condition, re-opened by every arrival and every departure.**
  ***Every person who was not here last season has to be given the part of this place that is not written down.***

**GRUDGING TOLERANCE**
- ⭐⭐⭐ **Disagreeing with the record.** **If authority here is a corpus checked against ground, then correcting
  it is permitted, unopposed, and expensive in the one thing nobody can lend you: seasons.** ***At Davis,
  being right is slow.*** **And for the interval, a person who is right and cannot yet demonstrate it is
  indistinguishable from a person who is wrong.** **Nobody forbids the correction. Nobody has to.**

## 3.3 `G8` — DEMOGRAPHIC COMPOSITION

**Inputs** `[ratified]`: Census I **563,599 H / 594,715 R / 1,158,314** — **robots 51.34%**. Census II
**437,423 H / 344,173 R / 781,596** — **humans 55.97%**. Retained **combined 67.48% · humans 77.61% · robots
57.87%**, spread **19.74 pp**. Departed **376,718 (32.52%)**, of whom **250,542 were robots — 66.51% of
everyone who left, from a population that was 51.34% robot**. Twenty-one named origins across three tiers.
⛔ **Bounds honored:** the per-nation figures are a share-weighted model, usable for named portable institutions
only; **no two nations' figures compared, at any precision, in either direction**; **tier is a production
weight, not a social fact**; **`G8` can never say which communities left** (`01` fire #2 — an absence of
origin-differential exit is an **artifact**, not a finding).

**STRENGTH**
- ⭐ **The city's core output survived losing a third of its people.** `1,158,314 → 781,596` and Davis remains
  the breadbasket. **Whatever the food system is, it is not the kind of thing that stops when a third of the
  population goes.** `PA-3`
- **A wide intake.** Twenty-one origins, and by Act 2 those are **ancestry, not identity** (the Acts law).
  **The stock is broad; the culture is local.**
- **A population with demonstrated mobility** — it arrived from elsewhere and a third of it moved again.
  `02` §G8: *"a population assembled by attraction is a population that has already demonstrated willingness to
  move."*

**DEFICIT**
- ⭐⭐ **No descent-anchored continuity.** The founding community is **one** community; the Primary tier is
  **another**; **nothing is written between them** — no waves, no dates, no order, no mechanism (`01` fire #3,
  *"the largest clean, peer-free hole in the set"*). **And by Act 2 origin is ancestry.** ⇒ ***Nothing here can
  carry the city's continuity by descent. It has to be carried by practice.***
- ⚠ **What a robot's national origin is MADE of is never stated** (`01` fire #13) — and the model assigns one
  to the **majority** population of Act-1 Davis. ⛔ **Left open. Not filled.**

**STANDING COST**
- ⭐ **Induction.** The tier system *admits and never subtracts* (`01` fire #11). **Arrivals continue; the rate
  is unwritten.** ⇒ **Teaching this specific ground to people who did not grow up on it is a category of work
  that regenerates permanently.** ⭐⭐ ***This is the same obligation `G4` reaches from the other side, and the
  two generators are independent.*** **That agreement is grounding.**

**GRUDGING TOLERANCE**
- ⭐⭐⭐ **Being the population the city's product is not for.** **At Census I the majority here is robots
  (51.34%) and the city's largest sector by workforce produces FOOD** `PA-3`. **Nothing forbids it. Nothing is
  organized against it. The city is simply not shaped around what that majority needs** — a point the universe's
  own energy material makes from the opposite end: *"robots need stable, high-density siligel-compatible power;
  humans need consistent low-level heat"* `[corroboration]`. ⇒ **For more than half of Census-I Davis, the
  city's central purpose is participated in as LABOR and not as BENEFIT.**
- ⭐⭐ **And after the inversion it gets quieter without getting smaller.** At Census II the same asymmetry is
  carried by **44.03%** instead of **51.34%** — **fewer people, the same cost each, and no moment at which
  anything changed.**

## 3.4 `G3` — FUNCTION & PURPOSE

**Inputs** `[ratified]`: **L143**, in full, and nothing else in the admitted set says what Davis is for.
`[corroboration]`: agriculture/food **35%** · technical/scientific **25%** · maritime **15%** · commercial
**15%** · industrial **5%** · other **5%**; workforce **876,514** on the Census I basis; percentages sum to 100.
⛔ **No sector headcount used** — the source's own register carries an unresolved denominator conflict
(181,808 against one basis, 306,780 against another, for the same nominal 35%) and does not resolve it.
⛔ **No finding below is scaled off a sector headcount.**

**STRENGTH**
- ⭐ **Davis never has to ask what it is for.** Two named roles, externally addressed, covering 60% of the
  workforce. **There is no identity vacuum here and no drift about purpose.**
- ⭐⭐ **And therefore no legitimacy problem.** **Nobody here has to argue that growing food matters.** ⇒ **The
  energy a place spends justifying its own existence is not spent here.** ⏸️ **Where it goes instead is NOT
  written by this pass** — that is Phase 4/6 material and inventing it would be the generic move.

**DEFICIT**
- ⭐⭐⭐ **Davis cannot make its own plant.** **Industrial is 5%** — the smallest sector — **and the city's
  defining output depends on built, glazed, sealed, serviced structures.** ⇒ ***Everything Davis's function runs
  ON comes from outside Davis.*** **Direction: food out, hardware in** `PA-3` `[corroboration]`.
  ⚠ **`01` fire #9 sharpens it from the other side: ~400 km² of exposed rock, not worked, with no in-world
  reason.** ⛔ **The guard is honored — no counterparty is named and the answer is NOT written as another
  location's role.** **Stated only as Davis's own dependency, with direction.**
- **The self-facing half of the function is EMPTY.** `02` §G3 requires both questions; only the parent-facing
  one is answered. ⛔ **Per NO FORCED FIT this is left open and is not filled** — see §9.

**STANDING COST**
- **Keeping the estate producing across a year that gives sixty usable outdoor-equivalent days.**
- ⭐⭐⭐ **Keeping the series.** **The research half is ecological and limnological — which is to say SERIAL.**
  ***A long-run record is worth exactly its continuity. Skip five years and you have not lost five years; you
  have lost the comparability of everything before and after.*** ⇒ ⭐⭐ **This is the only Davis obligation whose
  failure is not recoverable by working harder afterwards.** A bad harvest is recoverable. A broken structure is
  recoverable. **A gap in the series is permanent.**
- ⚠ **Delivering against a denominator nobody has resolved.** **Two independent instruments return the same
  unanswered question** — the industry register's 181,808-versus-306,780 conflict, and the census delta
  (`−376,718` against a 35% share baselined on Census I). ⛔ **Not resolved here, and nothing is scaled off
  it.** ⭐ **Recorded because the convergence is itself the finding: the basis on which Davis's obligation is
  denominated is unstated in two places at once.**

**GRUDGING TOLERANCE**
- ⭐ **Not being in either named sector.** **40% of the workforce is maritime, commercial, industrial or
  other, and the city's entire self-description is the other 60%.** **Nothing excludes them. The city simply
  has no account of them.** ⛔ **What that costs is NOT written here** — see §9's second empty slot, and the
  general-population discipline that produces it.

---

# 4 · ITEM 3 — THE COMPARISON

## 4.1 The table

**Every cell marked `agree`, `conflict`, or `silent`, against the quadrant's cross-generator reading.**

| | **G2 — physical** | **G4 — founding** | **G8 — composition** | **G3 — function** *(half-independent)* |
|---|---|---|---|---|
| **STRENGTH** | ground · shelter from the wind regime · light · varied water · a coast | proven record→practice conversion · site-specific inheritance · verification as a habit of origin | output survived a third of the people leaving · wide intake · demonstrated mobility | assigned purpose · no legitimacy problem |
| | **agree** with G4 *(both say: this place has already solved a founding problem and kept the result)* | **agree** with G8 *(continuity by practice, not by descent)* | **agree** with G4 | ⚠ **agree (NON-INDEPENDENT)** with G2 on suitability — **not grounding** |
| **DEFICIT** | no free season · no water surplus · rock that is terrain, not a plain · 37 dark days | no living institution · a record silent on timing · a verdict with no written criterion | no descent-anchored continuity · robot origin undefined | cannot make its own plant · **the self-facing half is empty** |
| | ⛔ **conflict** with G4 → §4.2 **C-1** | ⛔ **conflict** with G2 → **C-1** | **agree** with G4 | **agree** with G8 *(both: nothing internal supplies it)* |
| **STANDING COST** | freeze–thaw in summer · water recovery against loss · watching the boundary | **transmission — permanent, no season** | **induction — permanent, rate unwritten** | the estate · **the series** · an unresolved denominator |
| | ⛔ **conflict** with G3 on WHEN → §4.2 **C-3** | ⭐ **agree** with G8 — **independent, therefore grounding** | ⭐ **agree** with G4 — **independent, therefore grounding** | ⛔ **conflict** with G2 → **C-3** |
| **GRUDGING TOLERANCE** | an environment that reads benign · believing the summer | **being right is slow** | **being the population the product is not for** · the cost gets quieter, not smaller | not being in either named sector |
| | **silent** on people-vs-people | ⛔ **conflict** with G8 → §4.2 **C-4** | ⛔ **conflict** with G4 → **C-4**; ⛔ **conflict** with G3 on STRENGTH → **C-2** | ⛔ **conflict** with G8 → **C-2** |

**Shared silences — all four generators return nothing:**

| Silent on | Reading |
|---|---|
| **ORDER — who decides anything here** | ⭐ **Correct, not missing.** `02` §3.3 puts policy and prohibition in Phase 7 by design. **A capability frame that filled this would have turned into a list of rules and stopped generating** |
| **The exit MECHANISM** | ⛔ **Shape result. NOT filled.** `01` fire #1 — a destination, not a gate |
| **The failure modes of both entrances** | ⛔ **NOT filled.** `01` fire #7 — no sea-ice season, no road closure, no duty cycle written for either. ⚠ *And one of the site's three listed aviation surfaces is SEA ICE, which is seasonal by its nature* `[corroboration]` — **noted as a Step 3 pointer, not written as a closure regime** |
| **What the 40% do here** | ⛔ **NOT filled.** §9, slot 2 |

## 4.2 The four conflicts, mined

> **`02` §5.3: *"Do not ask which generator is right. Ask what single property of this place would produce both
> readings — then check whether the two claims are about different objects or at different scales."***

### ⭐⭐⭐ C-1 · `G2` × `G4` — THE CONFLICT HANDED TO THIS STEP

**G4 says the founders had *"a real documentary starting point for the Vestfold Hills' terrain."* G2 says the
terrain is seasonal: lakes that close and partly open, ice on a fjord, a boundary that may move, sixty days of
daily thaw. A static record cannot describe that.**

> ### THE SINGLE PROPERTY THAT PRODUCES BOTH READINGS
> ***The site has a permanent half and a seasonal half, and the inheritance was authoritative about one and
> obsolete about the other.*** **Different OBJECTS. Both claims stand.**

**The record was right about WHERE and silent about WHEN.** ⇒ **And the founders could not tell which was
which until a year had passed — and could not distinguish *"this lake froze late this year"* from *"this lake
freezes late"* until several had.**

⭐⭐⭐ **THIRD ORDER, and it is the pass's sharpest result:** ***to use a documentary inheritance about a seasonal
landscape you must measure repeatedly and compare against what the last record said. That is a time series.
That is limnology.*** **Davis's named research vocation is not an ornament bolted onto its agriculture — it is
the direct descendant of the founding survival method.** **The founders' problem and the city's science are the
same activity performed on the same objects.**

⭐⭐ **FOURTH ORDER:** **cultivation here is also a serial-observation problem** — when the light comes, when the
freeze releases, whether this year is ordinary. ⇒ ***Davis's two roles are not two things. They are ONE METHOD
applied to two objects.*** **Which kills the "two tribes" reading of §1.2 from a second, independent
direction** — the tension is not between kinds of people; **it is between two applications of one practice,
weighted unequally by whoever set the shares.**

⭐ **And `01`'s own Gate 9 result corroborates the method from an unexpected angle:** the corpus's **one clean
pass — the only inherited line that writes a closed state as well as an open one — is L154, the lakes.**
**Observation is what produces a written closed state.** ⇒ **The boundary of what this city has written down is
the boundary of what it systematically watches.** ⚠ **Stated as a property of the inherited MATERIAL and a
pointer for Step 3 — NOT written as an in-world fact about what Davis knows.**

### ⭐⭐ C-2 · `G3` × `G8` — WHO THE CITY IS FOR

**G3: the largest sector by workforce produces food for the nation** `PA-3`. **G8: the majority of Davis at
Census I is robots.**

> **THE SINGLE PROPERTY:** ***Davis's work and Davis's population are addressed to different beneficiaries.***
> **Different OBJECTS — one claim is about the OUTPUT, the other about the PEOPLE. Both stand.**

⭐ **And this is the blameless, structural answer to the re-stated question of §1.4** — *what differs, at Davis,
between those two populations' relation to this place?* ⇒ **From the beginning, the city's central purpose stood
in a different relation to each of them.** **No defect. No villain. Everyone in good faith.**

⭐⭐⭐ **THIRD ORDER:** **when the two populations' retention diverged by 19.74 pp, the population for whom the
city's purpose was labor-without-benefit is the one that retained less.** ⚠ ***This is the strongest available
reading and it is a reading, not a proof*** — `01` fire #2 forecloses origin-differential exit permanently, and
`01` fire #1 forecloses the mechanism. **Tagged: conditional on the §1.3 election-of-motive reading.**

⭐⭐ **FOURTH ORDER, and nobody decided it:** **the inversion makes the city's population match its output's
beneficiary.** **The function did not change; the population came to fit it.** ⇒ **Anything built in Davis when
robots were the majority persists into a period when they are 44.03% — and there is no moment at which it
stopped being the general case, because the change happened across an interval nothing dates** (`01` fire #12).
⛔ **No specific institution is invented to illustrate this.** **The structural exposure is written; the example
is not.**

### ⭐⭐ C-3 · `G2` × `G3` — WHEN THE EXPENSE FALLS **(and this cell IS grounding — see §2.1)**

**G2: the expensive season is winter — 37 dark days, five months below a −15.7 mean, heat and light bought
against the calendar. G3: the busy season is summer — the estate at maximum use in the sixty-day window.**

> **THE SINGLE PROPERTY:** ***Davis has two expensive seasons and no cheap one, and the two expenses are paid in
> different things, by different work.*** **Winter takes ENERGY. Summer takes FABRIC** *(§3.1's freeze–thaw
> finding)*. **Different OBJECTS. Both stand.**

⭐⭐⭐ **THIRD ORDER:** **there is no slack month.** ⇒ **Any work that has no season of its own — inspection,
repair, induction of newcomers, keeping the series — must be squeezed into whichever season is currently less
bad.**

⭐⭐⭐ **FOURTH ORDER, and it is the finding the whole step converges on:** ***the tasks with no season of their
own are exactly the tasks that lapse.*** **And Davis's two seasonless obligations are the two the other
generators independently name as permanent: `G4`+`G8`'s transmission/induction, and `G3`'s series.**

### ⭐ C-4 · `G4` × `G8` — DURATION AGAINST MOBILITY

**G4: competence here accrues by staying — *"over generations of their own,"* and correction costs seasons.
G8: the population is assembled from twenty-one origins and a third of it relocated inside the frame.**

> **THE SINGLE PROPERTY, at two SCALES:** ***Davis's competence is held by duration of residence, and its
> population's duration of residence is not guaranteed.*** **G4 speaks at the scale of a working life; G8 at the
> scale of a census. Both stand.**

⭐⭐ **THIRD ORDER:** **the city's capacity is silently proportional to a quantity nothing here measures.**
**Nobody counts how long anyone has been paying attention to which lake.**

⭐⭐ **FOURTH ORDER:** **a method that pays out only to those who stay, held by a population that has twice
demonstrated it moves, is a permanent structural mismatch — and neither side of it has a name, a forum, or a
counterparty.** ⇒ **It cannot be complained about. It can only be enacted.**

---

# 5 · ITEM 4 — THE SHAPE, AND THE DOUBLE READING

## 5.1 The shape — reported WITH its input set, as `02` §4.0 requires

> ## **SHAPE: `BALANCED`**
> ### **ON THE INPUT SET:** `G2` + `G4` + `G8` + `G3`(half-independent), **Census I governing (DR-4)**, the
> **Division-of-Industry percentages at corroboration tier**, the **corrected climate readings** (`R-3` warm
> endpoint **+3.2 °C** and two non-negative monthly means; `R-7` retention **38.5%**), the **newly established
> extent figure 410 km²**, **Band 5 machinery deferred**, and **this location's own culture material UNOPENED**.

**Why `Balanced` and not something else, checked against `02` §4's table rather than chosen:**

| Candidate | Verdict |
|---|---|
| **One / Double absence** | ⛔ No quadrant is empty. All four are populated by all four generators |
| **Net-negative** | ⛔ Strengths and deficits are comparable in weight; the deficits are not outrunning them |
| **Cost-dominant** | ⛔ **STANDING COST is real and multi-generator but it is not the largest quadrant.** *Not assigned merely because "hostile-environment outpost" is the expected shape for the type — that would be reading the shape off the category* |
| **Cost-absent** | ⛔ **Explicitly rejected.** §4.0 warns that a thin cost quadrant is usually the artifact of withheld institutions. **Here the quadrant is filled by G2 and G3 physics and mandate structure, not by institutions at all — and this location's institutional material is precisely what is still withheld.** ⇒ **The cost is IMPOSED, not voluntary** *(§4.0 item 2, answered in the direction it warns about)* |
| **Null** | ⛔ Nothing close |
| ⭐ **Balanced** | ✅ **All four quadrants populated, from four generators, with real content in each** |

**⭐ The internal structure the flat verdict would hide: `G3` is DOUBLED.** Two roles, two beneficiaries, two
failure clocks. **Applying §4's Doubled question — *which faculty is doubled, and in which direction?* —
the answer is: FUNCTION is doubled, and in the direction of OBLIGATION, not of identity** *(§1.2)*. **Recorded
as internal structure, not claimed as a second shape.**

## 5.2 The matching question, applied

> ### **`Balanced` → *"What does the balance cost? Two strengths and two deficits is a trade-off, not a gap."***

> ## ⭐⭐⭐ THE ANSWER
> ***The balance costs Davis its failure signal on the one axis where failure is permanent.***
>
> **A place with real strengths, real deficits and real standing costs in all four quadrants is a place where
> everything visibly works — the harvest reports, the structures stand, the water holds, the people arrive.
> Every one of those obligations announces itself the moment it stops being paid.** ⭐ **Exactly one does
> not: the series** *(`G3`, §3.4)*, **and the transmission that keeps it legible** *(`G4`+`G8`, §3.2/§3.3)*.
> **Nobody goes hungry when a measurement is missed.**
>
> ⇒ ***The balance is what conceals the one unbalanced thing.*** **`02` §4's cost-absent row names the failure
> mode precisely — *"not collapse but lapse — a practice performed less often, then rarely, then not, with no
> moment at which anyone finds out"* — and at Davis that mode is not the shape of the whole location. It is the
> shape of one obligation inside an otherwise well-signaled profile, which is the harder case, because the
> surrounding evidence of health is real.**

## 5.3 The DOUBLE READING — this same location read twice

> ⛔ **The cross-location form is forbidden.** **The second reading is `02` §4.0's: the same place on two
> admitted input sets.** **Both sets are genuinely available and neither was manufactured for the exercise.**

**READING A — the NARROWER set, which is what Step 0 actually held:** G2 + G4 + G8 + G3, **without** the extent
figure, **without** the Division-of-Industry percentages, and with the **climate defects uncorrected** (warm
endpoint read as 0 °C; retention stated as ~45%).
**READING B — the FULLER set:** this pass's, as declared in §5.1.

**Both readings return `Balanced`.** ⭐ **The shape is the only thing they share — which is exactly what §4.0's
three-step rule predicts, and it is the test of whether the pass stopped at step 1.**

| Axis | **READING A** — narrower set | **READING B** — fuller set |
|---|---|---|
| **1 · The question** *(shared — the only shared part)* | *What does the balance cost?* | *What does the balance cost?* |
| **2 · The instrument** | ⭐ **`G8`.** On the narrow set it is the only quantitative generator that is not defective — the retention arithmetic is all there is | ⭐ **`G3`.** The sector percentages give function a measured internal asymmetry (**35 against 25**) that the narrow set did not have — **and G3 was the fragile generator the frame carried in order to exercise it** |
| **3 · The consequence** | ⭐⭐ **The balance costs Davis its MAJORITY.** A city where everything works, and a third of it left anyway. **Working is not a reason to stay** | ⭐⭐ **The balance costs Davis its RECORD.** The obligation that cannot be recovered is the one carrying the lighter weight and the only one with no failure signal |
| **4 · The OBJECT of the loss** | **People** — 376,718 of them | **Continuity** — an unknown number of unmade observations |
| **5 · ⭐ TENSE** *(the axis §4.0 says is most often skipped)* | **PAST, completed, and undated.** The loss already happened; nothing in the frame can undo it | **PRESENT and CONTINUOUS.** The loss is happening, has no moment, and is still preventable |
| **6 · The remedy** | ⛔ **None. It is retrospective** | ✅ **Attention. It is prospective** |
| **7 · What the place FEELS like** | ⭐ **A sealed facility.** With the warm endpoint read as 0 °C there is **no month above freezing at all** — no summer, no outdoor season, cultivation entirely artificial year-round | ⭐ **A place with a summer.** Sixty days that thaw and refreeze daily under continuous light, a mean daily maximum of **+3.2 °C**, a record **+13.0**, lakes partly open |

> ## ⭐⭐⭐ WHAT THE DISAGREEMENT IS WORTH — and §4.0 is confirmed a second time inside this pass
>
> **Reading A writes Davis as a city defined by an exodus.** ***That is also the generic Antarctic-decline story,
> and it would have been written with complete internal coherence.*** **Reading B writes a city whose live
> exposure is a silent lapse in the one thing it cannot rebuild.**
>
> ⭐ **The two inputs that separated them are the sector percentages and a column-reading correction** — **neither
> of which is an institution, an interpretation, or a judgment call.** ⇒ ***A defect in reading one column off a
> table, plus one absent corroboration file, was enough to change what kind of place this is.***
>
> ⭐⭐ **And axis 7 is the one that should frighten a later reader.** **The difference between a sealed facility
> and a place with a summer is the difference between two entirely different cultures, two different sets of
> daily hardships, and two different sets of small joys — and it turned on which column an endpoint was read
> from.** **`R-3` was graded *"matters for the growing season."* ⛔ It matters for whether there IS a season.**

---

# 6 · ITEM 5 — EACH DEFICIT'S ADDRESS, AND THE COUNT

> **`00_RUNBOOK.md` L2518: *"5. Read each deficit's **address**, and **count the addresses.**"***
> ⭐ **The PEER-FREE set only** (`02` §4.1). **The peer-required set is not reached: no named counterparty is
> written, and reaching for one would require reading another location.**

| | Deficit | Address | The consequence `02` §4.1 attaches |
|---|---|---|---|
| **D-1** | **No water surplus** *(G2)* | ⭐ **NOWHERE AT ALL** | **Earned, not reached for.** The annual budget — 72.8 mm falling, ~28 mm staying — **is a physical constant no parent, past state, neighbor or diffuse process can alter.** §4.1 warns most apparent cases are really "past" or "diffuse"; **this one is neither.** ⇒ **Genuinely unremediable** |
| **D-2** | **Cannot make its own plant** *(G3, 5% industrial)* | **IN THE PARENT** | *"The remedy exists only at a scale above this one, so reaching it means admitting the location cannot manage itself. **Produces under-reporting**, which is a shadow with no author"* |
| **D-3a** | **No living institution at founding** *(G4)* | **IN ITS OWN PAST** — **and REMEDIED there** | The rare rich case: *"a characteristic nostalgia that is factually correct"* |
| **D-3b** | ⭐ **The SAME deficit, recurring at every arrival and departure** *(G4 × G8)* | ⛔ **DIFFUSE** | *"No counterparty, no politics, no grievance ever forms. Produces drift"* |
| **D-4** | **No descent-anchored continuity** *(G8)* | **DIFFUSE** | As above — and see the caveat below |
| **D-5a** | **No free growing season** *(G2)* | **NOWHERE AT ALL** | Latitude is not petitionable |
| **D-5b** | ⭐ **The ENERGY that substitutes for it** *(G2 × G3)* | **IN THE PARENT** | Under-reporting again, and harder to see |

## 6.1 The two evidence checks `02` §4.1 requires

### ✅ "IN ITS OWN PAST" — **are the people who could NAME the deficit still here?**

**For D-3a, the answer is the unusual one: the witnesses are gone and the ANSWER is still here.** The founding
generation is 248 years past; **their product — the practical terrain mastery they built over generations of
their own — is present and in use.** ⇒ **Davis's past is not epistemically unavailable to it. It is the one
thing that demonstrably survived.**

⭐⭐⭐ **AND THAT IS PRECISELY THE PROBLEM.** **The city holds a correct, completed, successful account of the
one time it faced this deficit.** ⇒ ***A solved-problem story is what makes the live version of the same problem
unformulable.*** **Not denial. Not ignorance. A true and celebrated historical answer functioning as an
anesthetic** — which is why D-3b's address is `diffuse` while D-3a's is `past`, **and why the pair is worth more
than either alone.**

### ✅ "DIFFUSE" — **has anyone here ever had a reason to formulate this as a problem at all?**

- **D-3b — honest answer: NO.** The founding account presents transmission as finished. **There is no occasion
  on which anyone would formulate *"we are still doing the founding, continuously"* as a statement about the
  present.** ⇒ §4.1: *"the deficit is not merely unaddressed — it is unspeakable, and that is a much stronger
  finding."*
- **D-4 — honest answer: NO, and the deficit-status is itself uncertain.** ⚠ **By the Acts law, twenty-one
  origins converging into one Tepenian identity is the national pattern and is not experienced as a loss
  anywhere.** ⛔ **Per NO FORCED FIT this is recorded as a deficit relative to an expectation NOBODY HERE HOLDS,
  and it is NOT promoted into a grievance, a nostalgia, or a tension.** **The slot stays as it reads.**

## 6.2 ⛔ THE ADDRESS THAT WAS NOT USED, AND WHY

**`IN A NEIGHBOR'S PRESENT` is not assigned to any deficit.** ⛔ **Not because Davis has no neighbors — because
using the category requires knowing that a co-located peer has the thing organically, and that is reading
another location.** ⇒ **It is STRUCTURALLY UNAVAILABLE to any in-run pass under the ONE LOCATION law, not absent
from Davis.** ⭐ **Recorded so that a terminal differentiation pass knows this axis was left deliberately
unrun rather than checked and found empty.**

## 6.3 ⭐⭐ THE COUNT, AND WHAT IT MEANS

```
7 deficit-addresses
4 distinct address classes used   ·   nowhere at all (2) · in the parent (2) · diffuse (2) · in its own past (1)
1 class structurally unavailable in-run   ·   in a neighbor's present
0 peer-required addresses
```

> ## ⭐⭐⭐ **DAVIS HAS FOUR KINDS OF DEFICIT AND NO MECHANISM FOR COMPLAINING ABOUT ANY OF THEM.**
>
> **Read the classes for what each one forecloses, and the result is not four separate facts but one:**
>
> | | |
> |---|---|
> | **Two are physically unremediable** *(D-1, D-5a)* | **Nobody can be petitioned about a precipitation budget or a latitude.** ⇒ **These constraints generate no politics whatsoever** |
> | **Two are diffuse** *(D-3b, D-4)* | **No counterparty exists, so no critic is ever produced** |
> | **Two ARE addressed — and both to the parent** *(D-2, D-5b)* | ⭐ **And these are the two Davis is structurally disposed to UNDER-ASK about**, because asking reads as conceding that the obligation is at risk |
> | **One is historical and already answered** *(D-3a)* | **And the answer is what conceals its live twin** |

**THIRD ORDER — D-1, run out:** because the water budget is beyond argument, **water discipline at Davis
produces no grievance and no blame.** ⇒ **It is the one constraint everybody obeys and nobody resents** —
structurally available as a shared, uncontested standard. ⏸️ **NOT converted into a norm, a virtue or a
practice.** *That is culture-pass work and inventing it here would foreclose it.*

**THIRD ORDER — D-2 and D-5b together, and they compound:** **Davis's food obligation is physically an ENERGY
obligation.** The calories are produced by light and heat the environment withholds for most of the year, in
structures Davis does not make, on a grid that for the majority of the frame is regulated nationally by a single
machine `[ratified]`. ⇒ ***Both inputs to Davis's defining output are external, and both are systematically
under-asked-for.*** ⭐⭐ **FOURTH ORDER:** and the hardware need accrues **invisibly, in the summer**, by
freeze–thaw *(§3.1)* — **so the request is chronically late and chronically small at exactly the time the damage
is accumulating.** **The two shadows are the same shadow, and neither has an author.**

**THIRD ORDER — the count as a whole:** **in a place with four kinds of deficiency and no channel for
complaint, the only remaining expression of a deficiency is DEPARTURE.** ⚠⚠ **Tagged, and deliberately not
promoted:** **this is the pass's strongest available hypothesis about the 376,718 and it is CONDITIONAL on the
§1.3 election-of-motive reading, foreclosed as to mechanism by `01` fire #1, and foreclosed as to origin by fire
#2.** ⛔ **It is written as a hypothesis with its conditions attached, not as a finding.**

---

# 7 · ITEM 6 — POPULATION ÷ EXTENT

> **`00_RUNBOOK.md` L2519: *"Divide population by extent. (One division; no interpretation.)"***
> ⭐ **This was expected to be BLOCKED.** `00_Frame.md` declared the extent band `UNDETERMINED` and the
> divergence question open. **The extent FIGURE has since been established at 410 km² — closed by the coastline
> ruling rather than individually declared — so the division IS runnable.**

```
1,158,314  ÷  410 km²  =  2,825.16 / km²          [Census I — GOVERNING per DR-4]
```

**Reproduces the source's stated 2,825/km² exactly.**

```
  781,596  ÷  410 km²  =  1,906.33 / km²          [Census II — arithmetic only]
```

⛔ **No interpretation.** ⛔ **Extent is the input and density the output — never the reverse.**

⚠ **The extent BAND remains `UNDETERMINED`, and that is not changed by having the figure.** `01` §2.1 defines
its bands on **population only** and supplies **no extent scale at all** — a missing instrument, not a poor fit.
⇒ ⛔ **The population/extent DIVERGENCE QUESTION stays open, neither asserted nor denied.** **A band cannot be
declared from a number when no scale exists to declare it against, and declaring one would pre-answer the
divergence question in the negative and permanently** *(`00_Frame.md` §0.1a·2, which is still good law)*.

⭐ **One observation, recorded flatly and NOT built on:** the established extent is **410 km²** and the spec's
ice-free area is **~400 km²** — within 2.5% of each other. ⚠ **The extent figure comes from a coastline ruling,
not from the oasis**, so **no causal claim is made.** **The coincidence is noted so a later pass that resolves
the extent instrument knows it is there.**

---

# 8 · `G1` — READ LAST, AS A CHECK. ⛔ **THE CHECK CANNOT BE RUN.**

**Davis's pair is `Earth / Earth`.** `05` §6.1c holds `G1` at corroboration tier, *"never an independent
generator,"* to be read last: **a match is corroboration, a mismatch is a finding site.**

| Half | Standing | This pass |
|---|---|---|
| **Element — Earth** | ⛔ **RESERVED** by `DR-1` | **No finding may rest on what it means.** None does |
| **Planet — Earth** | ✅ Ratified, **meaning readable** | ⛔ **`Planetary_Symbols.md` IS NOT IN THIS PASS'S ADMISSIBLE SET.** The member's registered terms were not opened |

> ## ⛔ **RESULT: NO CORROBORATION CHECK WAS PERFORMED, AND ITS ABSENCE IS NOT CORROBORATION.**
> **`02` §6.0 is unambiguous — *"read the member from the file, never from the name"* — and it supplies the
> worked case in which a pass that read Saturn from the tradition rather than the file would have produced
> *"the precise opposite of the intended reading, and would have been internally coherent while doing it."*
> ⇒ **With the file unopened, running the check from the bare word is the one thing forbidden outright.**
>
> ⛔⛔ **AND THE TEMPTATION HERE IS THE SPECIFIC ONE `00_Frame.md` §0.5 RESERVED ITEM 5 WARNS ABOUT:** **Davis's
> strongest physical facts — exposed rock, ground, soil, cultivation, groundedness — are exactly what a reader
> would intuitively call "Earth."** ***An intuitive match on a reserved member is not corroboration; it is the
> foreclosure the reservation exists to prevent.*** **No sentence in this document connects Davis's ground or
> its agriculture to either half of the pair.**
>
> ⇒ **FILED, not escalated** *(`01` §1.6a's rule: only a genuinely new item is a candidate for a fresh
> question)*: **the Planet half's file should be added to the admissible set at a later step so the check can
> actually be run.** **It does not block — `G1` counts zero either way.**

---

# 9 · ⛔ EMPTY SLOTS — DECLARED, NOT FILLED

> **NO FORCED FIT: an empty slot is a result. *"None is sited here"* must never read as *"none is possible
> here."***

| | Slot | Status |
|---|---|---|
| **1** | ⭐⭐ **What Davis is for ON ITS OWN TERMS** | ⛔ **EMPTY IN CANON.** `02` §G3 asks two questions; L143 answers only the parent-facing one, and its word for the other half is *"heritage."* **This pass does not supply a self-facing purpose.** ⚠ **This is the single largest empty slot in the step and it is the reason the inherited "researchers versus calories" tension had to be rewritten** |
| **2** | ⭐⭐ **What the other 40% of the workforce does here** | ⛔ **EMPTY.** Maritime 15 · commercial 15 · industrial 5 · other 5 — **labels, and nothing behind them.** ⭐⭐ **And the general-population discipline turns this from a gap into a structural bar: the admitted set describes ONLY growers and researchers, and both are roles, so the pass is FORBIDDEN from answering any general-population question from the only material it has.** ⇒ ***This is precisely the deficit `00_RUNBOOK.md` L2523 says research must wait for. Step 3 now knows where to point*** |
| **3** | **The exit mechanism** | ⛔ **EMPTY and shared-silent across all four generators.** Not filled |
| **4** | **Order — who decides anything** | ⛔ **CORRECTLY EMPTY.** Phase 7's, by `02` §3.3. **Not a gap** |
| **5** | ⏸️ **Reserved finding `A-1`** — ~400 km² of exposed rock in a nation where burial is impossible | ⛔ **RESTATED AND STILL NOT ADOPTED.** *Stating a physical constraint is legal; converting it into a practice is foreclosure.* **Carried forward untouched** |
| **6** | **A subnet-culture inheritance** | ⛔ **`PA-6` GUARD HONORED.** The parent is unwritten, so *"what the parent determines"* returns **UNKNOWN, which is not NOTHING.** **Nothing was inherited from it and nothing was invented to inherit** |

---

# 10 · ⭐⭐⭐ THE SPINE

> # **Davis was assigned both of its vocations and did not choose its remaining population.**
> # **The only thing here that canon calls its own is its METHOD — serial, seasonal, checked-against-the-record observation of a landscape no document could describe.**
> # **The city owns its practice and nothing else, and its practice is the one asset that fails without a sound.**

**Why this sentence and not another — every clause is load-bearing and each is sourced to an independent leg:**

| Clause | Where it comes from | Why it cannot be dropped |
|---|---|---|
| ***assigned both of its vocations*** | `G3` — L143's two parent-facing roles and the word *"heritage"*; corroborated by 35 against 25 | **Removes the election presumption at site (i)** and kills the two-tribe reading |
| ***did not choose its remaining population*** | `G8` — the census records a destination, not a gate | **Removes the election presumption at site (iii)**, which is the half that would have flattered the city |
| ***its METHOD is its own*** | `G4` — *"the exiles still built their own practical mastery of the terrain independently, over generations of their own"* | ⭐ **The ONLY thing in the admitted set canon attributes to the people here rather than to an inheritance or an assignment** |
| ***a landscape no document could describe*** | `G2` × `G4` conflict **C-1** | **The method is not a temperament; it is forced by a specific property of this specific ground** |
| ***fails without a sound*** | `G3`'s series + `G2`×`G3` conflict **C-3** + the `Balanced` shape's own question | **The one obligation with no failure signal, and the one that cannot be recovered by effort afterwards** |

> ## ⭐ THE CLOSING TEST, `02` §LAW 0 — *"Could a person live an entire life here — and would that life be unlike a life in any comparable place?"*
> **A life here is spent on a serial obligation nobody can see you meeting, in a place that did not pick you and
> that you may or may not have picked, doing work whose product is addressed to somebody else, on ground whose
> most dangerous season is its warmest and whose most abundant water cannot be drunk — where being right takes
> seasons and there is nobody to complain to about any of it.** ⭐ **That is not *"probably, I suppose."***

---

# 11 · HANDED FORWARD

| To | Item |
|---|---|
| ⭐⭐ **Step 3 — research** | **The deficit is now known and it is the GENERAL POPULATION** *(§9 slots 1 and 2)*. **The admitted set describes only two roles, and the discipline forbids answering from either.** ⇒ **Research picks must target the 40%, not the 60%.** `LAW 0-R` binds; **create `Davis_Research_Log.md`** |
| **Step 3** | **`G7` picks flagged by this step, unresearched:** ice-free-oasis limnology and lake typology (hypersaline, landlocked marine) · freeze–thaw damage regimes in cold-arid rock · sublimation-dominated water budgets and closed-loop recovery · polar sheltered cultivation under a 37-day night · ski-only aviation access and its seasonal availability. ⚠ **Each is at least two picks** (`LAW 0-R`) |
| **Step 3** | ⚠ **`R-3` is bigger than its grading.** §5.3 axis 7 shows the warm-endpoint correction decides whether Davis HAS a summer. **Any later re-grade must account for that** |
| ⭐ **CST — Unrecognized Instrument** *(`02` §4.2 — run after the profile, never before)* | ⭐⭐ **CANDIDATE IDENTIFIED, NOT ADOPTED:** **Davis cannot reliably transmit practice to people who were not here (D-3b, diffuse, unspeakable) — and it runs, as a named vocation, a continuous serial-observation program whose entire purpose is to make a landscape legible to someone who was not present when it was observed.** ***The research method IS a transmission instrument and nothing in the admitted set notices that it generalizes.*** ⛔ **Handed over as a candidate; the technique belongs to CST, not to the spine** |
| **CST — Necessity Before Meaning** *(`02` §G4 pairing)* | **The founding constraint is available** — *check the record against the ground before trusting it.* ⛔ **NOT moralized here.** The pairing is flagged; executing it is culture-pass work |
| **Step 5** | **First opening of `Local_Cultures/` and `Local_Robot_Culture/`, as a CHECK.** ⚠ **Pre-declared non-independence stands:** if a later phase derives a harvest-versus-archive tension, that is **corroboration at best** and must be tagged *(`00.1` §5.1)*. ⚠ **And `Robot_Physiology_…`'s leak-register exposure means Davis's own position on the topics it covers stays explicitly open** |
| **Step 6 / terminal** | **`IN A NEIGHBOR'S PRESENT` was left deliberately unrun, not checked and found empty** *(§6.2)*. **The terminal differentiation pass should know that** |
| **Step 9** | **`G6` stays a recorded null** — Step 2 declared it unneeded *(§2.2)*. Disposition ✅**A** discharged; **no developer input required** |
| ⏸️ **Not escalated, filed only** | **`Planetary_Symbols.md` should enter the admissible set at a later step so the `G1` check can actually be run** *(§8)*. ⛔ **Not a new developer question** — it is a contract-scope item, and `01` §1.6a forbids re-raising what is already classified |

---

# 12 · ⭐ THE RECORDING LAW — snags, dead ends, killed findings, self-corrections

> **Standing Step 9.5 obligation: log what did not work, not only what did.**

| | |
|---|---|
| ⛔ **KILLED — the inherited G3 tension in its handed form** | *"Residents understand themselves as researchers while the polity requires calories."* **L143 contains no self-understanding at all and calls the research half a *heritage*.** ⭐ **Killed twice, independently: once by reading the line closely (§1.2), once by conflict C-1 showing the two roles are one method** |
| ⛔ **KILLED — a first draft of the §1.2 argument** | It argued *both vocations are MANDATED, therefore neither was chosen.* **Killed on `01` §1.1's layer ruling and fire #11's guard: `MANDATED`/`FREE` may well be an authoring status, and importing it into the fiction is the exact error the layer ruling names.** ⭐ **The verdict was rebuilt on the percentages and on L143's own wording, and survives without it** |
| ⛔ **KILLED — assigning `IN A NEIGHBOR'S PRESENT` to D-2** | The hardware deficit fits the category well. ⛔ **Using it requires asserting what a co-located peer has, which is reading another location. Refused, and re-addressed to the parent** |
| ⛔ **DEAD END — the `G1` corroboration check** | **Cannot be run: the Element half is RESERVED and the Planet half's file is outside the admissible set.** **It died at the CONTRACT, not at the source** |
| ⚠ **SELF-CORRECTION — G2 × G3 independence** | **This step began by treating all four generators as independent.** **L143 derives the function from the geography in its own sentence, so G2 × G3 agreements about suitability are one fact read twice and are NOT grounding.** ⭐ **Caught before the comparison table was built, and it changed how three cells are marked** |
| ⚠ **SELF-CORRECTION — the shape** | **`Cost-dominant` was the expected shape for a hostile-environment settlement and was the first candidate considered.** ⛔ **Rejected on the count: STANDING COST is real but not the largest quadrant.** ***Assigning it would have been reading the shape off the location's TYPE rather than off its profile*** |
| ⚠ **SNAG — an instrument divergence, found while assembling the proof blocks** | ⛔⛔ **The file-reading tool's displayed line numbers diverge from `sed`/`awk` numbering for at least one required file** (`02_Generators_…md`: the tool shows 761 lines and renders `awk` line 95 as line 96; `awk`/`wc -l` both return **760**). **Every ranged contract in this run is written as a `sed` spec** *(`00.1` §4.1, `M-224`)*. ⭐ **All ranged reads in this step were therefore re-acquired and verified at `awk` numbering before anything was written; the Davis spec, the runbook range and the census lines were confirmed to match exactly, and the 137-line admitted set reproduces from the `sed` spec.** ⚠ **Raised, not fixed** — *finding a defect is not authorization to fix it* — **but it is the `M-117`/`M-223`/`M-225` family and it can silently mis-range a contract that nobody re-checks** |
| ✅ **NOT ADOPTED, carried intact** | **Reserved finding `A-1`** *(disposal of the dead)* · **the exit mechanism** · **the settlement pattern** · **any specific institution illustrating the C-2 inversion** · **any norm derived from D-1's uncontested water constraint** |
| ✅ **VERIFIED, not asserted** | Retention `67.4770 / 77.6125 / 57.8719`, spread `19.7405 pp` · shares `51.34 / 48.66` and `55.97 / 44.03` · departures `376,718`, of which `250,542` robots = `66.51%` · monthly means average `−10.0333` against a stated `−10.0` · monthly precipitation sums to exactly `72.8` · retention `28 ÷ 72.8 = 38.46%` · `1,158,314 ÷ 410 = 2,825.16` · admitted read spec expands to exactly **137** lines |

---

# 13 · VERDICT

> # ✅ **SPINE BUILT — the six items are complete.**

| Item | Result |
|---|---|
| **1 · Select ≥3 independent generators** | ✅ **Confirmed** G2 + G4 + G8, mutually independent; **G3 exercised as a half-independent fourth** — with the correction that **the one line grounding G3 derives it from G2** |
| **2 · Four-quadrant profiles, separately** | ✅ **Four profiles, run G2 → G4 → G8 → G3**, G3 last and deliberately built from L143 and the percentages alone |
| **3 · Compare, mark every cell, mine the conflicts** | ✅ **Table built; four conflicts run through the both-are-true test; four shared silences recorded as shape results** |
| **4 · Read the shape; apply its question** | ✅ **`Balanced`, reported with its input set; the DOUBLE READING run on two genuinely available sets, diverging on six of seven axes including tense** |
| **5 · Deficit addresses, counted** | ✅ **7 addresses, 4 classes, 1 class structurally unavailable in-run; both evidence checks run** |
| **6 · Population ÷ extent** | ✅ **`1,158,314 ÷ 410 = 2,825.16/km²`** — expected to be blocked, and it ran |
| ⛔ **The time-critical item** | ✅ **RESOLVED IN-PASS AT THREE SITES, NOT ESCALATED** |

**Strongest reason:** **the step's two hardest inputs both turned.** **The handed G2 × G4 conflict resolved into
a single property that explains why this city's science and this city's survival are the same activity; and the
"chosen/selected" ambiguity, resolved rather than assumed, took away the most flattering thing Davis could
believe about itself and returned an authorless shadow in its place.**

**Biggest doubt, carried forward:** ⭐ **the whole of `G3` still rests on one ratified line, and this step's
reading of that line is CLOSER to it than the inherited reading was, not further — which means a single
re-reading of L143 could move the spine again.** ⚠ **And `G3`'s corroboration is a project-internal derivation
whose own register carries an unresolved denominator conflict.** ⛔ **The percentages are used; nothing is
scaled.**

**Second doubt:** **C-2's third-order reading — that the population for whom the city's purpose was
labor-without-benefit is the one that retained less — is the pass's best explanation of a 19.74 pp spread and
it is a reading, not a proof.** **It is tagged in three places and is never written as established.**

⛔ **Step 3 — RESEARCH — opens next, and it now knows its deficit: the general population, and the 40%.**

---

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md
LRANGE: 2497-2525
LINES: 29
L1: # Step 2 — Build the spine
LMID:    > once on the full one.* **1.** The shape gives the question. **2.** The generator gives the instrument.
LLAST:
QUOTE: 5. Read each deficit's **address**, and **count the addresses.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md
LRANGE: FULL
LINES: 760
L1: # Generators, the Capability Frame, and Symbol Binding
LMID: **So the derivation runs the other way from the district method:** rather than deriving a shadow separately and
LLAST:    emphasis.**
QUOTE: | **Diffuse** — nowhere in particular | No counterparty, no politics, **no grievance ever forms.** Produces drift. |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Davis.md
LRANGE: 1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179
LINES: 137
L1: # Davis
LMID: **Mean annual temperature:** -10.0°C  _(READER station: Davis; 1991–2020 WMO standard normal)_
LLAST: - **Relationship to Mawson (the city, different subnet)** — both named for/connected to Australian Antarctic figures, but administratively and geographically separate; worth clarifying whether any cultural connection existed despite the subnet divide
QUOTE: Davis is, above all, Tepenia's breadbasket and a prime ecological/limnological research hub — sheltered-agriculture and greenhouse cultivation alongside genuine research heritage make up the clear majority of daily activity.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Energy_Grid_Failure_Rationale.md
LRANGE: FULL
LINES: 145
L1: # Why "Just Fix the Energy Grid" Isn't a Practical Solution
LMID: infrastructure could replace.
LLAST: - **Climax (The Great Blackout):** All the half-measures and compromises finally catch up, forcing the player to make the ultimate choice about the future of the entire system.
QUOTE: - The grid was originally designed primarily for pre-war human needs. Modern bonded pairs and robot-heavy populations have very different energy profiles (robots need stable, high-density siligel-compatible power; humans need consistent low-level heat).

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Davis.md
LRANGE: FULL
LINES: 16
L1: # Climate Reference: Davis
LMID: **Annual mean temperature:** -10.0°C
LLAST: _Source: BAS READER (Reference Antarctic Data for Environmental Research), https://legacy.bas.ac.uk/met/READER/ — cite as Turner et al. (2004), Int. J. Climatol. 24, 191–211._
QUOTE: | +0.9 | -2.2 | -8.0 | -13.5 | -16.0 | -15.7 | -17.1 | -17.1 | -15.7 | -11.8 | -4.2 | +0.0 | -10.0 |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md
LRANGE: FULL
LINES: 99
L1: # Antarctic Stations With Functional Airstrips / Aircraft Ground Infrastructure
LMID: | Plog Island Skiway | Davis Station | Australia | Ice |
LLAST: - Several names on this list use "skiway" specifically (a compacted snow or ice surface usable only by ski-equipped aircraft) as distinct from a genuine wheeled-aircraft runway (gravel or blue ice, usable by wheeled cargo planes) — this distinction may matter if Tepenia's own lore wants to differentiate between "reachable by any aircraft" and "reachable only by specialized ski-equipped planes."
QUOTE: - Several names on this list use "skiway" specifically (a compacted snow or ice surface usable only by ski-equipped aircraft) as distinct from a genuine wheeled-aircraft runway (gravel or blue ice, usable by wheeled cargo planes) — this distinction may matter if Tepenia's own lore wants to differentiate between "reachable by any aircraft" and "reachable only by specialized ski-equipped planes."

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md
LRANGE: 392-398,496,613
LINES: 9
L1: **Davis** *(Vestfold Hills, Prydz Bay — mainland coast)*
LMID: | Primary | China |
LLAST: | 14 | Davis | Mirny | 437,423 | 344,173 | **781,596** | |
QUOTE: | 13 | Davis | Mirny | 563,599 | 594,715 | **1,158,314** | *(revised 2026-07-04)* |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00.1_Step_MINUS-1_Input_Contract.md
LRANGE: FULL
LINES: 371
L1: # Davis — Step −1 · THE INPUT CONTRACT
LMID: > **L127:** *"No living environmental **knowledge** survived that chain of handoffs — but preserved journals,
LLAST: ⛔ **Step 0 — FRAME — opens next.**
QUOTE: | **G3** | Function & purpose | ✅ **PRESENT** | ✅ | **L143 — one line, and only one** |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00_Frame.md
LRANGE: FULL
LINES: 397
L1: # Davis — Step 0 · THE FRAME
LMID: declares two numbers **so that the second checks the first** — *"when they diverge, the divergence is
LLAST: ⛔ **Step 1 — AUDIT WHAT IS INHERITED — opens next.**
QUOTE: **Generators selected:**  G2 (physical) · G4 (founding) · G8 (composition) — with G3 (function)

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/01_Inherited.md
LRANGE: FULL
LINES: 363
L1: # Davis — Step 1 · WHAT IS INHERITED
LMID:
LLAST: ⛔ **Step 2 — BUILD THE SPINE — opens next.**
QUOTE: | **1** | ⭐⭐ **The orbital exit is a MECHANISM-SHAPED HOLE.** Eligibility, refusal, durability and any return trip all unwritten; the census records a **destination, not a gate** | `G8` | **Decides which of two cities Davis is** — all three readers reached that phrasing independently. **The 781,596 are either stayers or a residue** |


## ROUND 1 · READER C — raw

---

# Davis — Step 2 · BUILD THE SPINE  *(Reader C, independent)*

**Frame: Second Interwar (2564–2812)** · written 2026-09-15 · `00_RUNBOOK.md` L2497–2525 · `02` in full

> **Status of this document.** One of three independent readers running the same brief blind. Nothing here is a
> consensus position; it is one reader's honest derivation, written to be cross-checked. Where I disagree with
> an inherited framing I say so and give the ground.
>
> **Tier tags used throughout:** `[ratified]` — developer-authored canon · `[corrob]` — project-internal
> derivation, corroboration tier *(the 410 km² extent; the Division-of-Industry tier grading)* ·
> `[PA-3]` — rests on the assumption that the food obligation runs outward.

---

# §0 · ⛔ TIME-CRITICAL — THE "CHOSEN / SELECTED" AMBIGUITY, RESOLVED IN-PASS

**Discharged FIRST, before any profile is written, because it decides the voice of every sentence that follows.**
`01_Inherited.md` §1.6a classifies this **disposition A — resolves AT Step 2, by Step 2's own readers, as
ordinary interpretive analysis. It must NOT be escalated.** It is not escalated here.

## 0.1 · Where the wording is — **three sites, not one**

| # | The wording | Where it sits | What it presumes |
|---|---|---|---|
| **1** | ***"When leaving became possible, robots left at substantially higher rates than humans. What about this place made that so?"*** | `00_Frame.md` §0.6, and again at `00.1` §3.3 | ⛔ **ELECTION, twice over.** *"became possible"* presumes an option opening; *"robots left"* presumes the movers as agents of their own move |
| **2** | *"nobody was born or died in the transition; **they relocated**"* · *"**MIGRATION** to a documented destination"* | the census, quoted at `00.1` §2.2 and `00_Frame.md` §0.1 Status | ⚠ **Softer election.** *Relocate* and *migrate* are both intransitive-agentive verbs |
| **3** | *"**Founding population:** Australian **exiles**"* | `Specs/Davis.md` L129 `[ratified]` | ⭐ **ASSIGNMENT — and in the opposite direction from 1 and 2** |

**Site 1 is the one `01` §1.6 flagged, and it is the dangerous one, because it is also the pass's own declared
strongest finding** — `00_Frame.md` §0.6 puts it in the box discharging `01` §5.2 rule 4. **The spine would
have been built on it.**

## 0.2 · What the evidence actually supports, axis by axis

| Axis | Reading the evidence supports | Ground |
|---|---|---|
| **Founding — how people came to be here** | ⭐ **ASSIGNMENT. Established.** | *Exile* is a verdict word. `01` fire #5: *"Exile is a verdict and only the landing is written — threshold, decider, reviewability, heritability all absent."* **Nobody elected to arrive.** And L131's Saint exclusion `[ratified]` is a second negative verdict handed down from outside, with its criterion written and its mechanism not (fire #6) |
| **Function — what people here do all day** | ⭐⭐ **ASSIGNMENT. Established, and newly so.** | The tier structure `[corrob]` grades agriculture **MANDATED (FULL)** and technical/scientific **MANDATED (HALF)**; maritime, commercial, industrial and other are **FREE**. **35 + 25 = 60% of the workforce structure is assigned; 40% is not.** ⭐ **The word in the data is *mandated*.** Davis does not elect to be the breadbasket, and it does not elect to do the science either |
| **Exit — the orbital transition** | ⛔ **NEITHER. The evidence is absent in BOTH directions.** | `01` fire #1: *"the census records a **destination, not a gate.** Eligibility, refusal, durability and any return trip all unwritten."* `01` §1.1: **the one enormous outflow of 376,718 people is recorded as a NUMBER and never as a MECHANISM.** Fire #2 forecloses the origin axis permanently. **There is no gate, no criterion, no refusal, no decider, and no petitioner anywhere in the admitted set** |

## 0.3 · ⭐⭐ THE READING I ADOPT

> ## **Assignment is established everywhere Davis's inherited material actually speaks. The exit is VOICE-NEUTRAL: neither election nor assignment is established, and every sentence about it must be true under both.**

**The asymmetry is the tell.** *Where evidence exists, it says assignment — twice, independently, from a founding
fact and a functional fact. Election is presumed only at the one site where evidence is entirely absent.* A pass
that inherited site 1 unexamined would have imported the single unsupported reading into the single highest-stakes
place in the pass.

### ⭐ And the silence has a CAUSE, derived rather than assumed — see §3.3

Both readings of the exit require **an entity with the authority to decide about a person.** Davis's inherited
material contains no such entity in any register: none in the founding *(the living institution did not survive
the handoff; exile's decider is off-site)* `[G4]`, none in the demography *(the tiers admit and never subtract —
fire #11)* `[G8]`, none in the function *(the mandate is set above Davis)* `[G3]`.

> ### ***The ambiguity is not a gap in the record. It is the record faithfully reporting a city that has never possessed the organ that would produce an answer.*** **The exit's terms are missing for the same reason the refusal instrument is missing. That is ONE finding, not two.**

### ⭐⭐⭐ And the Act stamp makes it deeper

`M-157` requires it, and `01` §1.2 measures it: ***across the Act boundary, exile stops being a STATUS and
becomes a LINEAGE.*** In Act 1 (≈2564 → the frame's first 18%) exile is an assignment borne by living people.
By Act 2 — most of the frame — **nobody living at Davis was exiled to it.** They are here because they were
born here.

> ## ***For the great majority of the 248 years, no decision about who is at Davis has ever been made by anyone at Davis — including about themselves.***

## 0.4 · What this changes in practice — the corrected spine wording

| ⛔ Not this | ✅ This |
|---|---|
| *"When leaving became possible, robots left at substantially higher rates than humans."* | **"Across the transition Davis's robot population fell by 250,542 and its human population by 126,176. The city entered robot-majority and left human-majority. Whatever the terms of the move were, they bore differently on robots and on humans, by 19.74 pp of retention."** |
| *"the stayers"* / *"the residue"* *(fire #1's binary)* | ⭐ **Neither. Both words presuppose an act of sorting Davis had no instrument to perform or to record.** What the arithmetic supports is weaker, stranger and better: **a measured differential in attachment, with its mechanism outside the city** |
| *"what about this place made robots leave?"* | ⭐ **"What is it about Davis that its robots and its humans were differently attached to it?"** — a question about **the place's grip**, answerable from Davis's own generators. The movers' intentions are not |

⚠ **Check run, and it passes:** this resolution does **not** destabilize `00_Frame.md`'s `Status: LIVING`. Under
assignment the fall is still relocation to a documented destination inside the setting's own future, not loss.
**`01` §3's migration test survives both readings.** Nothing downstream unwinds.

---

# §1 · ITEM 1 — GENERATOR SELECTION: **CONFIRMED, WITH ONE SUBSTANTIVE AMENDMENT**

**Step 0 selected `G2` · `G4` · `G8`, carrying `G3` as a fourth *"BECAUSE it is the fragile one and must be
exercised, not leaned on."*** I confirm the selection. I do not confirm its stated reason for `G3`.

## 1.1 · Independence check — `02` §5.1 rule 2

| Pair | Independent? | |
|---|---|---|
| `G2` × `G8` | ✅ **Fully.** A climate normal and a census are not the same fact in any sense | |
| `G3` × `G8` | ✅ **Fully.** | |
| `G2` × `G3` | ✅ **Substantially.** The function is *suited* to the physical site, but suitability is a relation between two independently-determined facts, not a shared origin | |
| `G3` × `G4` | ✅ **Yes here, and this is the trap `02` §5.1 names.** *"Function, founding purpose, and the parent's need are frequently the same fact."* **At Davis they are not:** the founding was a **verdict** (exile), not a purpose — nobody was sent here *to farm*. The function was assigned afterward, from above `[corrob]`. **Two different facts with two different authors** | |
| ⚠ `G2` × `G4` | ⚠ **PARTIALLY DEPENDENT — declared, not concealed.** `G4`'s inheritance is *a written record of `G2`'s terrain* (L127: *"a real documentary starting point for the Vestfold Hills' terrain"*). Their **contents** overlap | **The selection still stands, and the dependency is why:** the two are independent *in kind* — one measures the present subject, the other is a fact about transmission — and §3.3 below shows they **disagree about what kind of teacher this place is.** A single generator cannot disagree with itself |

## 1.2 · ⭐ THE AMENDMENT — `G3` is no longer the courtesy fourth

Step 0 carried `G3` as the fragile one. **That grading is now out of date.** The Division-of-Industry tier
extraction `[corrob]` supplies something no other generator at Davis supplies: **a grading of compulsion** —
`MANDATED (FULL)` / `MANDATED (HALF)` / `FREE`, across six sectors summing to 100%. `G2` grades nothing; `G4`
grades nothing; `G8` grades nothing. ⭐ **`G3` became the instrument of the fuller reading in §4, and it carried
the decisive evidence in §0.2.** It is load-bearing, not exercised.

⚠ **The `02` G3 warning still binds and is honored:** lowest surprise on the stack, and a pass that reads
function tends to restate it. **Restatement is what §2.4 refuses to do** — every `G3` entry below is a
consequence of the *grading*, not of the word "breadbasket."

## 1.3 · The generators NOT selected — declined with reasons, per `02` §5.1 rule 1

| | Disposition |
|---|---|
| **`G1`** | ⏸️ **Corroboration tier, counts zero, read LAST — and the check is UNRUNNABLE here.** See §7 |
| **`G5`** | ⛔ **DECLINED for spine use.** Direction exists; **volume does not, anywhere** (`REQ-G5v`), `PA-4` forbids magnitude, and `Access type: ON` is uninterpretable in contract (guard 1). `02` G5 demands *"direction AND volume."* **Half a generator is not a generator.** Used below only for RELATION, never for scale |
| **`G6`** | ✅ **NOT NEEDED — and that discharges `01` §1.6a's disposition-A row exactly as written.** Four generators against a threshold of three; the spine is built without it. **The recorded null therefore stands unadjudicated through to Step 9. No developer input required, and none is requested** |
| **`G7`** | ⛔ **Research half unbuilt, and Step 2 forbids research.** `00_RUNBOOK.md` L2523: *"Do not research yet."* **Step 3's job.** ⚠ One admitted real-world reference is in this reader's set and is handled at §9.3 — as physical texture only, and NOT adopted |

**Countable, selected, and profiled: FOUR — `G2`, `G4`, `G8`, `G3`.**

---

# §2 · ITEM 2 — FOUR FULL QUADRANT PROFILES, RUN SEPARATELY

> ⛔ **Discipline observed:** each profile below was derived from its own generator's inputs alone, and written
> out completely, before the next was opened. Cross-generator observations were withheld to §3. Where a
> profile reaches toward another generator I have cut it and noted the cut.

> ⛔ **BAND 5 GUARD, standing over all four profiles.** `DR-4` defers decomposition and distributional analysis.
> **Nothing below is a distributional result.** Monthly climate values and sector percentages are *source data*,
> not spreads or modes. No sub-location is asserted, and no finding is scaled off a sector headcount
> *(the denominator conflict in the industry sheet is unresolved and its headcounts are not used)*.

> ⛔ **GENERAL-POPULATION GUARD, standing over all four profiles.** `00b` is in full force at Band 5. Davis's
> function line names *researchers* and *growers* and **both are roles.** Arithmetic that fixes the scale of the
> trap: population **1,158,314**, workforce **876,514** `[corrob]` — **281,800 people, roughly a quarter of the
> city, are not in the workforce at all**, and a further 40% of those who are work in sectors the city's own
> self-description does not mention. ⭐ **L143's "clear majority of daily activity" is a claim about workers.
> It is not a claim about people here.** No quadrant below answers what people eat, wear or believe.

---

## 2.1 · `G2` — PHYSICAL & ENVIRONMENTAL CONSTRAINT

**Inputs, all `[ratified]`:** ~400 km² of ice-free exposed rock, freshwater lakes, saltwater lakes, hypersaline
lakes, landlocked marine basins, fjord-like inlets, Ingrid Christensen Coast, Prydz Bay · mean annual
**−10.0 °C** · monthly means Jan **+0.9**, Feb −2.2, Mar −8.0, Apr −13.5, May −16.0, Jun −15.7, Jul −17.1,
Aug −17.1, Sep −15.7, Oct −11.8, Nov −4.2, Dec **+0.0** · mean daily maxima Jan **+3.2**, Dec +2.4, Feb −0.2,
Aug −14.2 · mean daily minima Jan −1.2 … Aug −20.8 · records **+13.0** (Jan) / **−41.8** (Apr) · wind **~5.6 m/s
(~20 km/h), OUT of the katabatic regime** · precipitation **72.8 mm/yr falls**, **~28 mm lands**, **~45 mm lost
to sublimation and wind transport** — **true retention 38.5%**, not the stated ~45% *(`R-7`, diagnosed: the
millimeter figure for what is LOST was reused as a percentage)* · polar night **37 days** (Jun 4 → Jul 10) ·
midnight sun **55 days** (Nov 25 → Jan 18) · daylight by month 24 / 17.2 / 13.1 / 9.0 / 4.7 / 0 / 1.9 / 7.0 /
11.2 / 15.2 / 20.3 / 24 h · precipitation probability ~6–7% in Dec–Jan against ~20–22% in Mar–May.

⚠ **`R-3` applied, not deferred:** the spec's L74 *"warmest month avg 0°C"* reads two different columns. **The
warm endpoint is +3.2 °C and TWO months carry non-negative means.** For a city whose only function line is
cultivation this is a primary input, and it is used as one below.

### ⭐ STRENGTH — what the environment gives freely

1. ⭐⭐ **WIND THAT IS MERELY WIND — and this, not the temperature, is the function-relevant fact.** A mean of
   5.6 m/s, explicitly out of the katabatic regime. **A katabatic site's wind is a structural design load and a
   scheduling tyrant.** Davis's is neither. *Consequence:* **low-mass, high-glazing, pressure-sensitive
   structure is physically possible over large areas here.** Sheltered cultivation and greenhouse work need
   exactly that, and a katabatic regime forbids exactly that. **The single most enabling physical fact at Davis
   is the absence of a wind.**
2. **GROUND THAT DOES NOT MOVE.** ~400 km² of exposed rock — not an ice shelf, not a glacier, no ice-movement
   correction, no re-levelling cycle, no relocation. **A structure put down on Vestfold rock is in the same
   place 248 years later.**
3. **LIQUID WATER IN PLACE, SEASONALLY.** Lakes of four kinds, *"partially open in summer"* (L154). Fresh water
   that is **found**, not manufactured out of ice at a continuous energy charge.
4. **A REAL ABOVE-FREEZING WINDOW.** Two months of non-negative mean; mean daily maxima at or above zero in
   Dec, Jan and effectively Feb; a record +13.0. **There is a season here in which being outdoors is not a
   protective operation.**
5. **A HUGE, CONCENTRATED LIGHT BUDGET.** 55 days of midnight sun inside a four-month block running
   Nov 20.3 h → Dec 24 → Jan 24 → Feb 17.2 h. ⭐ **Davis's annual light is not short. It is stacked.**
6. **A SHORT DARK.** 37 days of polar night, not four months; by August there are 7.0 h.
7. **AN INDENTED COAST.** Fjord-like inlets cutting into the ice-free hills — the physical precondition of a
   harbor, as distinct from the harbor itself.

### ⛔ DEFICIT — what it withholds absolutely

1. ⭐⭐ **WATER FROM THE SKY.** 72.8 mm falls; 28 mm stays; 45 mm leaves. ***38.5% retention.*** **This is a
   desert, and its precipitation is not a supply — it is noise.** No rain-fed anything, ever; 28 mm/yr is not a
   snowpack and not a reservoir.
2. ⭐ **AND THE LITTLE THERE IS ARRIVES IN THE WRONG MONTHS.** Mar–Jun carry **38.2 mm — 52% of the annual
   total** — into the cold and the dark. Nov–Feb, the entire light-and-work block, carry **9.7 mm, 13%.**
   ***Everything the weather gives Davis arrives when it cannot be used, and 45 of every 72.8 mm leaves before
   anyone can act on it.***
3. **AN OPEN-GROUND SEASON.** Ten of twelve months carry negative means; eight sit below −8. **Everything that
   grows here grows inside something. There is no field.**
4. **WARMTH AS A BACKGROUND CONDITION.** Even the warmest month's mean daily minimum is −1.2. The place never
   stops taking heat out of everything in it.
5. ⏸️ **A GROWING MEDIUM — *unstated, and left open.*** The inputs say **"exposed rock"** and never say soil.
   ⛔ **I do not assert that Davis lacks soil and I do not assert that it has it.** What the admitted set
   supports is narrower and still useful: **the ground is documented as a foundation and never as a medium**
   (fire #9 — *"~400 km² of exposed rock, not worked, with no in-world reason"*). **NO FORCED FIT: slot left
   explicitly open.**

### ⭐ STANDING COST — what it demands continuously

1. **Heat, forever, into a −10.0 °C annual mean.** *(First order. Recorded and not dwelt on — `02` G2: "It is
   cold" is not a finding.)*
2. ⭐⭐ **WATER HELD ACROSS AN INTERVAL THE CITY DOES NOT SET.** The lakes are *"ice-covered in winter,
   partially open in summer"* (L154) and the sky cannot bridge a gap of any size. **Every litre used in August
   was taken in February, or taken from under ice, or made from the sea.** *And the atmosphere is a permanent
   withdrawal:* 45 mm/yr leaves to sublimation and transport whether or not anyone does anything, so **any
   stored open surface is losing while it waits.** ⭐ **Davis's water accounting has a leak term with no task
   attached to it.**
3. **TRANSPARENCY.** A sheltered-cultivation city with a 37-day night and a 55-day midnight sun must hold
   transparent surface against rime, drift and thermal cycling. §3.1's exact test: *a category of task that
   regenerates the moment it is finished.*
4. ⭐ **THE EDGE OF THE ICE-FREE GROUND.** Fire #14. The 400 km² is bounded by a margin, not a wall, and the
   admitted set does not say whether that margin is fixed, seasonal or moving. **The demand is real regardless:
   a city whose entire territory is the un-iced fraction of a coast must know where that fraction currently is.**
   *(Sharpened at §6.2.)*
5. ⭐ **THREE DEMANDS STACKED ON ONE INTERVAL.** In the dark months, cultivation light must be **supplied**
   rather than received (0–1.9 h of daylight in Jun–Jul against 24 h in Dec–Jan); human occupants need
   consistent low-level heat; robot occupants need stable, high-density siligel-compatible power
   `[Energy_Grid_Failure_Rationale §8 — the PHYSIOLOGICAL MISMATCH statement only;` ⛔ *that file's grid-failure
   narrative is post-war and is NOT used, and no claim about Davis's energy scarcity is made or implied]*.
   **Three unlike demands, one interval, every year.**

### ⚠ GRUDGING TOLERANCE — permitted, and expensive

1. ⭐⭐ **BEING OUTDOORS IN THE GOOD SEASON.** Permitted, and by this place's standards genuinely pleasant —
   +3.2 mean daily maximum, 20 km/h, 24 h of light, 1.8 mm of precipitation in the whole of January. **Punished
   because it is precisely the interval in which everything cultivated must be attended.** ⭐ ***The environment
   and the work want the same 120 days, and the environment is only generous while nobody's time is their own.***
2. ⭐ **BEING OUTDOORS IN WINTER — and the absence of the katabatic wind is the trap.** You *can* walk out in
   July: 5.6 m/s, no event-generating wind. It costs −17.1, a mean daily minimum of −20.6, 1.9 h of light and a
   record of −41.8. ⭐ **A place that STOPS you produces a discipline. A place that merely CHARGES you produces
   individual judgement calls, repeated, most of which are fine.** *Third order:* ***Davis's environmental harm
   is not dramatic, it is cumulative — the site does not kill people with a single wind, it presents a slow
   bill — and a slow bill is exactly the thing nobody can point at.***
3. **DISPERSAL ACROSS THE GROUND.** Permitted — the rock is there, stable, and nothing forbids it. Charged in
   heat delivery, water delivery, and distance in the dark. **Nobody bans spreading out; spreading out simply
   costs.**
4. **ACTIVITY IN THE DARK MONTHS.** Nobody forbids it. Everything done then draws on the same stacked interval
   as everything else done then. ⭐ *Third order:* **Davis's winter is not a season of rest — it is a season in
   which every activity competes with every other, and the competition is never framed as competition.** It is
   framed as *"we don't do much in winter,"* which sounds like a description of a temperament and is a
   description of an allocation.

---

## 2.2 · `G4` — FOUNDING CONDITION

**Inputs, all `[ratified]`:** founding population **Australian exiles** (L129); settled post-Falkland Treaty on
Davis Station infrastructure; through the First Interwar the station was held by a rotating succession of
operators; ⭐ **L127 — *"No living environmental knowledge survived that chain of handoffs — but preserved
journals, logs, and orientation manuals left behind across the centuries gave the exiles a real documentary
starting point for the Vestfold Hills' terrain. Learning from a written record isn't the same as being taught by
a living institution, and the exiles still built their own practical mastery of the terrain independently, over
generations of their own."***

> ### ✅ PERSISTENCE TEST — `DR-7`, run in one line, in the text, as `01` §1.6 requires
> ***Would preserved journals, logs and orientation manuals still be here if the originating nation had left
> and never returned?*** **YES — a written record does not require occupation to persist. ADMISSIBLE.**
> ⛔ **And the guard rides with it: `DR-7` admits the MATERIALS and admits nothing about WHO MADE THEM.**
> Nothing below infers the founding population's character from any operator's nationality; the operators are a
> coordinate and appear nowhere in the findings.

### ⭐ STRENGTH

1. ⭐⭐ **AN EXTENSIBLE PRIOR.** The founders did not arrive ignorant. They arrived holding **centuries of
   somebody else's observations of this exact ground**, in a form that could be read, copied, indexed, argued
   with and — decisively — **added to.** ⭐ ***A documentary inheritance is the only kind of inheritance that is
   extensible in the medium it arrived in. You cannot add a page to an apprenticeship. You can add a page to a
   log.***
   - *Second order:* the founding act at Davis was therefore not *learn to survive* but **verify the record
     against the ground.** Every early generation's work had a template to check itself against, and every
     check generated a new entry.
   - *Third order:* ⭐⭐ ***the city's first native competence was neither cultivation nor science. It was
     reading — specifically, reading a record written by people who are not available to be asked.***
2. **NO INCUMBENT.** No living institution survived, so there was **nothing here to defer to, unlearn, or ask
   permission of.** Every practice at Davis is in principle dated and authored inside the city's own generations.
3. **AN EXPLICIT, CANON-STATED SUPERSESSION.** L127 says the exiles *"still built their own practical mastery of
   the terrain independently, over generations of their own."* **The inheritance was a starting point and canon
   says so** — so `G4`'s strength is a *launch* condition, not a permanent dependency.

### ⛔ DEFICIT — *"what the founding generation did not bring is very often a permanent hole, because nobody afterwards knew it was missing"*

1. ⭐⭐⭐ **THE CORRECTION LOOP.** A living institution does two things a record cannot: it **answers a question
   you did not know to ask**, and it **stops you before you do the wrong thing.** A record answers only
   questions you already had words for. ***So the founding generation inherited every answer and no
   supervision.*** The absence is not knowledge. **It is the negative feedback path.**
   - *Second order:* a culture that learns only from late reports develops a very high tolerance for
     *provisional* practice and a very high regard for **the record of what went wrong** — because failure,
     with no teacher to absorb it, has nowhere else to go but onto a page.
   - *Third order:* ⭐⭐ ***Davis's characteristic knowledge form is the WRITTEN NEGATIVE — "we tried this, and
     here is what happened."*** That is what a documentary tradition with no living teacher inevitably
     accumulates, and it is the **inverse** of an apprenticeship tradition, which transmits successes by
     demonstration and loses its failures silently. ***Davis's stored knowledge is disproportionately made of
     things that did not work.***
   - *Fourth order:* **a place whose stored wisdom is mostly negative cannot easily tell a newcomer what to do.
     It can only tell them what not to do.** That is a real handicap for absorbing arrivals — and Davis absorbed
     twenty-one origin communities.
2. ⭐ **NO NATIVE SOURCE OF LEGITIMACY.** Exile is a verdict delivered from outside (fire #5); the institution
   that could have constituted an authority here did not survive; **there is no founding charter, no surviving
   order and no teacher.** What the founding supplies instead is a **document**, and a document's authority is
   only ever *this is what was observed.*
3. ⭐ **A SCALE-MISMATCHED INHERITANCE.** L127 is precise about the record's subject: *"the Vestfold Hills'
   **terrain**."* It is terrain notes, made by tens of people, for tens of people. **It is now the founding
   document of a city of 1,158,314.** ***The record can tell you what a lake does. It cannot tell you what a
   lake does when a city drinks from it.***

### ⭐ STANDING COST

1. ⭐ **THE RECORD MUST BE KEPT READABLE — physically, linguistically, and referentially.** Centuries of
   accreted logs in several hands is not a tidy corpus; it is a heap. **Legibility is permanent, invisible, and
   never finished** — §3.1's test exactly.
2. ⚠ **THE RECORD MUST BE EXTENDED, or the method quietly stops being the thing that distinguishes the place.**
   ⭐ **And nothing breaks if it stops.** *(Flagged here and carried to the shape read at §4 — this is the one
   genuinely `cost-absent`-shaped item in the entire profile: an obligation with no failure signal.)*
3. ⭐⭐ **THE DISTINCTION MUST BE MAINTAINED between *what the record says* and *what we have verified
   ourselves*.** L127 establishes two bodies of knowledge, different provenance, one subject. **Keeping them
   apart is work. Letting them merge is free.**
   - *Third order:* ***once merged, the city cannot tell which of its practices are verified and which are
     inherited on trust — and the merge is the default, because merging is simply what happens when nobody is
     maintaining the distinction. It is a standing cost that becomes invisible to the people the moment they
     stop paying it.***

### ⚠ GRUDGING TOLERANCE

1. ⭐⭐ **DISAGREEING WITH THE RECORD.** Nobody forbids it — **the record has no defenders**; its authors are
   five centuries dead and were never one institution. It costs anyway: **you must produce the
   counter-observation yourself, then write it, then persuade people to read a new page against an old one that
   has worked so far.**
   - *Third order:* ⭐ ***the whole cost falls on the person who was right first, and it falls before anyone
     knows they were right.*** **Authorless, nobody in bad faith, no policy and no enforcer** — and read
     in-world not as a structural charge but as *"that's what it takes to make a case."* **`00d`'s structure,
     arrived at by filling the quadrant honestly rather than by deriving a shadow and testing it.**
2. **ARRIVING AND NOT READING.** Nothing stops anyone from working here without ever engaging the corpus. But
   the corpus is where the *why* of every local practice sits, so a non-reader is permanently downstream of
   decisions they cannot reconstruct. **Not forbidden. Merely expensive, permanently, and invisibly.**
3. ⭐ **NEEDING TO BE SHOWN RATHER THAN TOLD.** A founding with no living institution makes **apprenticeship
   itself** the effortful, non-default channel: the page is the default, and the city has no inherited structure
   that assigns anyone to demonstrate. ***The person who cannot learn from a book pays a price nobody here has
   ever named.***

---

## 2.3 · `G8` — DEMOGRAPHIC COMPOSITION

**Inputs, all `[ratified]`, arithmetic re-reproduced by this reader:**

```
Census I  (Act 1 inheritance)   563,599 H  /  594,715 R  /  1,158,314      R = 51.34%
Census II (Act 2 event)         437,423 H  /  344,173 R  /    781,596      H = 55.97%, R = 44.03%
change                         −126,176 H  / −250,542 R  /   −376,718
retained  combined  67.48%   ·   humans  77.61%   ·   robots  57.87%   ·   spread 19.74 pp toward humans
of the 376,718 departures, 250,542 — 66.51% — were robots, in a city that was 51.34% robot
21 origin communities:  Primary China 19.04%  ·  seven Significant, incl. Australia (founding wave) 4.93%
                        ·  fourteen Notable, 0.94–3.52%
```

> ### ⚠⚠ ACT STAMP — `M-157`, required and applied
> **Composition is an ACT 1 inheritance. The inversion across the census gap is an ACT 2 event. They are not
> one series.** By Act 2 the national percentages are **ancestry figures, not identity figures.**
> ⚠ **And fire #12 bites here: nothing dates the transition.** It sits in Act 2 by the frame's own epistemic
> horizon *(orbital migration is a lived event; Amundsen Tower completes ~2688)*, but **its year is unwritten,
> so the Band 5 declaration covers an unstated fraction of 248 years.** Stated, not resolved.

> ### ⛔ THREE GUARDS, carried verbatim from `01` and honored in every line below
> **(1)** The per-nation figures are a **share-weighted model**, identical across both censuses by construction:
> usable for **named portable institutions only**, never as measured counts. **(2)** No two nations' figures are
> compared at any precision in either direction — the within-tier ordering is a de-stacking artifact.
> **(3)** Fire #2's **hard ceiling**: the model forecloses per-nation differential retention *permanently*, so
> **an absence of origin-differential exit is an ARTIFACT and may never be written as a finding.**

### ⭐ STRENGTH

1. ⭐⭐ **NO ORIGIN GROUP IS LARGE ENOUGH TO BE THE DEFAULT.** Twenty-one communities; the largest at 19.04%;
   **the founding community at 4.93%.** *(Stated as Davis's own figures, flatly. No rank, no comparison, no
   other city.)*
   - *Second order:* **whatever the common ground at Davis is, it cannot be an origin culture.** The founders
     are too small to impose one and the largest group is under a fifth. It has to be something **the place
     itself supplies.**
   - *Third order:* ⭐ ***being from here outranks being from anywhere.*** Generational depth substitutes for
     origin — **and generational depth is available to everyone born here, robots included.**
   - ✂️ *Cut from this profile and held to §3:* what the place supplies instead. That answer belongs to the
     comparison, not to `G8` alone.
2. ⭐⭐ **A ROBOT-MAJORITY CITY AT CENSUS I — 51.34%.** In Act 1 terms **Davis's default person is a robot**, and
   every general-population question is majority-answered by one. Robots are human-looking, clothed, gloved,
   gel-brained, vacuum-capable and not altitude-limited; **cold is a real cost to them on different axes, and an
   environmental hazard is a preparation problem, not a gate.** *Capability consequence, stated carefully:*
   **the marginal cost of maintaining presence across 400 km² through a 37-day night is lower for this
   population than it would be otherwise — lower, not zero.**
3. **DEMONSTRATED ABSORPTION.** From an exile founding to 1,158,314 across twenty-one origins. **Whatever the
   mechanism was, the capacity is evidenced by the total.**

### ⛔ DEFICIT

1. ⭐ **THE EXODUS IS LEGIBLE BY KIND AND PERMANENTLY ILLEGIBLE BY ORIGIN.** Fire #2's ceiling. ⭐ **This is a
   deficit that improves the question:** it forces the one enormous demographic event onto the human/robot
   axis — the axis that matters most — and refuses every other axis forever.
2. ⭐⭐ **NO MECHANISM OF REFUSAL AND NONE OF SUBTRACTION.** Fire #11: **the tier system admits and never
   subtracts; no exclusion criterion exists anywhere.** Fire #1: the exit is a mechanism-shaped hole. **In the
   whole inherited set, Davis has no written way to say no to anyone and no written way to let anyone go.**
   Structurally, Davis is documented as an **accumulator**: everything it has, it acquired; nothing it has, it
   chose against.
   - *Third order:* ⭐⭐ ***an accumulator with no subtraction rule has no instrument that can register a loss as
     a decision.*** When 376,718 people were no longer here, nothing in the city could record it as anything
     but a smaller number. ***Davis's demography has arithmetic and no grammar.***
3. ⭐ **NO ARRIVAL NARRATIVE.** Fire #3: twenty-one communities, **no waves, no dates, no order, no mechanism,
   nothing written in between the 4.93% founders and the 19.04% largest group.** **A city that cannot rank its
   own arrivals cannot produce the ordinary politics of precedence** — no *we came second*, no seniority ladder,
   no first-comer claim except the founders', and they are 4.93%.
   - *Asked once per Act, as fire #3 directs:* **Act 1** — plural-by-origin, and the question has live stakes
     for people who remember arriving. **Act 2** — origin is ancestry, the stakes evaporate, and **the question
     stops being askable before it was ever answered.**

### ⭐ STANDING COST

1. ⭐ **A COMMON MEDIUM MUST BE RE-SUPPLIED TO EVERY COHORT, FOREVER, AT THE CITY'S OWN EXPENSE** — because no
   origin supplies one and the founders cannot impose one. *(What the medium is: §3.)*
2. ⭐⭐ **TWO INCOMPATIBLE UTILITY PROFILES IN ONE SETTLEMENT, AT ROUGHLY HALF AND HALF.** Robots need stable,
   high-density siligel-compatible power; humans need consistent low-level heat `[physiological mismatch only;`
   ⛔ *post-war grid narrative NOT used]*. **594,715 against 563,599 is the most expensive possible ratio,
   because neither population can be treated as the exception.**
   - *Third order:* ⭐⭐⭐ ***a city at 51/49 cannot optimize. It must build everything twice or build everything
     to a compromise — and the compromise is worse for both than a dedicated build would be. Nobody at Davis is
     optimally accommodated, and nobody is badly enough accommodated to complain.*** **Authorless, unintended,
     invisible from inside, everyone in good faith.**
   - ⚠ *Sized nowhere.* `00d` at Band 5: qualitative and explicitly un-sized until the deferral lifts.

### ⚠ GRUDGING TOLERANCE

1. ⭐ **LEAVING.** Nothing in the inherited set forbids it, and 376,718 did it. **What the material actually
   supports is: departure occurred, and its terms are entirely unrecorded** — and the cost is invisible *by
   construction*, because the instrument that would have measured it (a gate, an eligibility rule, a refusal)
   was never written. ⛔ **Written voice-neutral per §0: whatever the terms were, they bore differently on
   robots and on humans, by 19.74 pp.**
2. ⭐⭐ **BEING THE ONLY ONE OF YOUR ORIGIN IN A ROOM.** With twenty-one communities and none above 19.04%,
   **minority status is the ordinary condition at Davis — for everyone, including the largest group.**
   Permitted, unremarkable, and it charges: every practice that needs a critical mass of co-origin people is
   **expensive to keep and free to let lapse.**
   - *Third order:* ⭐⭐ ***origin practices at Davis are not suppressed. They are outnumbered. They fade by
     scheduling rather than by prohibition, and nobody can name the moment.***
   - ⭐ **That is the Act 1 → Act 2 transition as it looks on the ground at Davis** — *differentiate locally,
     converge nationally*, discharged with a local mechanism rather than asserted.
3. **STAYING.** Whatever the terms, the people who remained kept a city that had become smaller by a third and
   gained nothing in its place. Permitted; costly; **and unperceived as a cost, because staying is the default
   and defaults are invisible.**

---

## 2.4 · `G3` — FUNCTION & PURPOSE

**Inputs:** L143 `[ratified]` — *"Davis is, above all, Tepenia's breadbasket and a prime ecological/limnological
research hub — sheltered-agriculture and greenhouse cultivation alongside genuine research heritage make up the
clear majority of daily activity."* · L148 `[ratified, declared blank + placeholder]` — Vestfold Hills oasis
resources, Prydz Bay maritime trade, logistics within the subnet; **export-shaped, import side absent**
(guard 3) · tier structure `[corrob]`:

```
Agricultural / food production   35%   MANDATED (FULL)
Technical / scientific           25%   MANDATED (HALF)
Maritime 15% · Commercial 15% · Industrial 5% · Other 5%      ALL FREE
workforce 876,514, baselined on Census I.   percentages sum to 100.
⛔ headcounts NOT usable — the sheet's denominator conflict is unresolved. No finding is scaled off one.
```

**`02` G3's two questions, and they diverge:** *on its own terms* — a research community with genuine research
heritage. *What the parent needs* — **calories.**

> ## ⭐⭐ BUT THE TIER GRADING CORRECTS THE INHERITED FRAMING, AND THE CORRECTION MATTERS
> `00_Frame.md` §0.7 hands Step 2 the tension as *"residents understand themselves as researchers while the
> polity above requires calories."* ⛔ **That framing is not quite right, and the grading is why: BOTH sectors
> are MANDATED.** The polity does not merely tolerate Davis's science — **it requires it, at half grip.**
> ⭐ **So the tension is not city-versus-polity. It is INSIDE THE MANDATE: 35 FULL against 25 HALF, on one
> calendar.** *(Tagged `PA-3` where it depends on the food obligation running outward.)*
> ### ⭐⭐⭐ And that is WORSE, not better, which is why it is worth the correction.
> ***An external conflict can be resented and negotiated. An internal one — where both halves of your own
> obligation are legitimate and one is graded higher — cannot be. There is nobody to be angry at, because the
> thing taking your research weeks is your own food mandate.***

### ⭐ STRENGTH

1. **DAVIS IS DEPENDED UPON, AND THE GRADING SAYS SO.** A `MANDATED (FULL)` sector is §3's STRENGTH signature
   exactly — *what others route to it; what it is trusted with.* **35% of the workforce structure, at full
   grip.** *(Stated as Davis's own figure. No other city appears in this claim and none is needed for it.)*
2. **TRUSTED WITH TWO THINGS, NOT ONE.** The research is mandated too — **a quarter of the workforce structure.**
3. ⭐⭐ **THE TWO MANDATED SECTORS SHARE A SUBJECT.** Ecology and limnology are the science of **lakes and living
   systems**; sheltered agriculture is the cultivation of living systems in water. ⭐ **Davis's science and
   Davis's obligation study the same object.**
   - *Third order:* ***a city whose science and whose work are about the same thing does not experience them as
     two careers. It experiences them as two depths of one practice*** — and the line between *grower* and
     *researcher* is **how far down you go**, not what you do.
   - ⚠ **Both are roles.** This is a claim about the *structure of two roles*, not about the general population.
     The guard at the head of §2 stands.

### ⛔ DEFICIT

1. ⭐⭐ **A MANDATED-FULL FOOD SECTOR WITH NO PERMISSION TO FAIL — and, more precisely, with NO WAY TO BE SHORT.**
   Fire #8: *no failure mode, no stated growing season, no bad year, no reserve, no rationing, no consequence.*
   **Not "it is never short." It has no mechanism for being short, and no name for it.**
   - *Third order:* ⭐⭐ ***a place with no name for its own shortfall absorbs shortfall internally and
     invisibly. The mandate is the thing with a number on it; local consumption is the thing without. So the
     illegible side is the side that flexes.*** `[PA-3]` **Authorless; nobody decides it; it simply follows from
     which of the two quantities is written down.**
2. ⭐ **DAVIS CANNOT DECIDE WHAT IT IS FOR.** **60% of the workforce structure is assigned from above.**
   Whatever the city's own sense of itself may be, three fifths of its labor structure is not available for it
   to change.
3. **THE IMPORT SIDE IS ABSENT.** L148 is export-shaped and its more characterizing half is missing (guard 3).
   `G3` can say what Davis sends and **cannot say what Davis needs.** ⛔ **Silence, not a gap to fill. Carried
   to §3.4.**

### ⭐ STANDING COST

1. ⭐⭐ **THE CROP CYCLE IS A STANDING COST IN THE STRICT SENSE: a category of task that regenerates the moment
   it is finished.** Harvest is not an achievement; it is the beginning of the next one. **And the clock is not
   the city's** — it is set by light and temperature, and at Davis both are savagely concentrated.
2. ⭐⭐ **THE RESEARCH OBLIGATION IS A STANDING COST TOO — and this is the half a reader would miss.**
   `MANDATED (HALF)` means the science is **owed, continuously,** the way a harvest is owed. **Research that is
   owed on a cadence is not the same activity as research that is pursued: it must produce, periodically,
   whether or not the ground has offered anything.**
   - *Third order:* ⭐⭐⭐ ***a delivery cadence applied to a discipline whose subject is slow — lakes, ice-on and
     ice-off, long series — produces a permanent, specific friction: the subject moves on a timescale of years
     and the obligation reports on a timescale set by somebody else. What that produces is a great deal of
     intermediate data and very few conclusions.***
3. ⭐ **KEEPING THE FULL MANDATE FROM EATING THE HALF.** §3.1 question 3 — *what fails first if attention lapses
   for a week?* **Not the food: it is the sector with the number on it and the full grip.** ***The research
   fails first, quietly, and by reassignment rather than by decision.***

### ⚠ GRUDGING TOLERANCE

1. ⭐⭐ **DOING THE RESEARCH PROPERLY.** Permitted — it is mandated, it is a quarter of the workforce structure,
   nobody forbids it. **Punished, because a half-mandate and a full mandate draw on the same weeks**: the lakes
   are open in summer, so the field season **is** the growing season.
   - *Third order:* ⭐⭐⭐ ***the cost is read in-world not as a conflict of obligations but as a personal failing
     of time management.*** `02` §3.2's stronger answer exactly — the cost read as the natural consequence of a
     personal choice. ***Nobody at Davis is told to stop doing science. They are simply never given a week in
     which the science is the thing that is owed.***
2. ⭐⭐ **WORKING IN THE FREE 40%.** Maritime, commercial, industrial, other — genuinely free, and **two fifths
   of the workforce.** Punished only in that **the city's own self-description does not mention them at all.**
   - *Third order:* ⭐ ***two fifths of Davis's workers do something Davis's account of itself omits — and,
     with 281,800 people outside the workforce entirely, the city's self-description covers a minority of its
     own inhabitants.*** **An unnarrated fraction that large is where a place's actual texture lives and where
     its self-image never looks.** *(This is `00b`'s trap, paid off arithmetically rather than asserted.)*

---

# §3 · ITEM 3 — THE COMPARISON

## 3.1 · The table — one row per quadrant, one column per generator, every cell marked

| | **`G2` physical** | **`G4` founding** | **`G8` composition** | **`G3` function** |
|---|---|---|---|---|
| **STRENGTH** | **agree** — no katabatic wind, stable ground, a stacked light block, water in place: precisely the endowment the function needs | ⚠ **agree (with `G8`)** — an extensible prior; **no incumbent** | ⚠ **agree (with `G4`)** — no origin large enough to be the default; **no incumbent**; robot-majority presence | **agree** — nationally depended-upon; two mandates sharing one subject |
| **DEFICIT** | ⛔ **CONFLICT** — the environment refuses constantly, absolutely and without appeal | **agree** — no correction loop; no native legitimacy | **agree** — no refusal, no subtraction, no arrival narrative | **agree** — no way to be short; cannot decide its own purpose |
| **STANDING COST** | **agree** — water across the frozen interval, a permanent sublimation leak, transparency, the ice margin, three demands on one interval | **agree** — legibility, extension, the verified/inherited distinction | **agree** — a common medium re-supplied to every cohort; two utility profiles at half and half | **agree** — the regenerating cycle; the owed cadence; the full mandate against the half |
| **GRUDGING TOLERANCE** | **agree** — the good season is the working season; winter charges cumulatively; dispersal costs | **agree** — disagreeing with the record; not reading; needing to be shown | **agree** — leaving, on unrecorded terms; permanent minority status; staying | **agree** — doing the science properly; working in the unnarrated 40% |
| *(off-table)* **an in-city decider** | **silent** | **silent** | **silent** | **silent** |
| *(off-table)* **what flows INWARD** | **silent** | **silent** | **silent** | **silent** *(L148's missing half)* |
| *(off-table)* **a growing medium** | **silent** *(rock stated; soil never)* | **silent** | **silent** | **silent** |
| *(off-table)* **disposal of the dead** | **silent** | **silent** | **silent** | **silent** |

## 3.2 · ⭐⭐ THE STRONGEST AGREEMENT — **two independent generators, one structural fact**

`G4` says the living institution did not survive the handoff. `G8` says no origin group reaches a fifth and the
founders are at 4.93%. ***These descend from entirely different facts — a transmission event and a census — and
they say the same thing:***

> # **Davis has no inherited authority of any kind.**

**`02` §5.2: where two independent generators agree, build hard.** Everything below is built on this.

## 3.3 · ⛔⛔ THE CONFLICT — **the richest cell in the table**

**Three of four generators say Davis has no instrument of refusal.** `G4`: nothing to say *not that.* `G8`:
nothing to say *not you.* `G3`: nothing to say *not this year.* **And `G2` is the one that says no constantly:**
28 mm lands of 72.8 that fall, ten months below freezing, thirty-seven days of no light at all, and 45 mm/yr
leaving whatever anyone does.

> ### ⭐ Both-are-true, run as `02` §5.3 directs — *not which is right; what single property produces both*
>
> **The property: Davis's refusals are all environmental and none of them are social.** The city was founded on
> a documentary inheritance into a place whose constraints are physical, quantified, legible and
> non-negotiable — ***so the environment did all of the refusing, and no social instrument for refusal ever had
> to be invented.***
>
> **Different objects, both claims stand:** `G2` is about **the world** refusing; `G4`/`G8`/`G3` are about
> **the city** refusing. There is no contradiction to resolve, and the unresolved-looking cell was the finding.

### The three orders out of it

1. **First:** at Davis, *no* is a fact about the weather, not something a person says.
2. **Second:** a place where every refusal comes from outside develops **no practice of being refused by a
   person** — and therefore no practice of **appealing** one.
3. ⭐⭐⭐ **Third:** ***and therefore no practice of ASKING.*** **A petition presumes somebody who can say no.**
   If the only things that say no here are the precipitation budget and the ice margin, **the form was never
   needed and was never developed.**

> ### ⭐⭐ AND THIS EXPLAINS THE INHERITED SILENCE RATHER THAN PATCHING IT
> **Step 1 found the exit's mechanism-shaped hole as a documentation defect. It is not one.** ***The city had no
> instrument for adjudicating people, so when an allocation involving 376,718 of them occurred, nothing in
> Davis was equipped to record it as a decision.*** **§0's resolution and §3.3's conflict are the same result
> reached from two directions.**

## 3.4 · ⭐ SHARED SILENCE — a shape result, and NOT filled

`02` §5.2: *all generators silent on a quadrant → genuine emptiness → this is a shape result. Do not fill it.*
**Four silences, all four unanimous across all four generators, all four left explicitly open:**

| Silence | Ruling |
|---|---|
| **An in-city decider** | ⛔ **Left open, and it is the profile's central negative result** *(§3.3)*. ⚠ *Prohibitions and who-decides belong to Phase 7 by `02` §3.3 in any case — the capability frame must not become a list of rules* |
| **What flows INWARD** | ⛔ **Left open.** L148's import half is absent and `G5` has no volume. ✅ **What IS legal and IS recorded:** Davis's material is export-shaped in every direction — road access both ways on Hwy 110, a Prydz Bay maritime entry, oasis resources and subnet logistics stated as things Davis *has* and *sends.* **Delete every other city's name and that survives: it is relation, not comparison** |
| **A growing medium** | ⛔ **Left open.** Rock is stated; soil is never stated, in either direction. **NO FORCED FIT** |
| **Disposal of the dead** | ⛔ **Left open. Reserved finding `A-1` is NOT converted.** The physical constraint is legal to state and is not restated here; converting it into a practice would be foreclosure, and nothing in this step needs it |

**"None is sited here" is not written anywhere above, and nothing above reads as "none is possible here."**

---

# §4 · ITEM 4 — THE SHAPE, ITS INPUT SET, AND THE DOUBLE READING

## 4.1 · ⛔ The input set, declared FIRST — `02` §4.0 item 1 makes the shape meaningless without it

> **Reading B (this pass's shape) is produced by: `G2` + `G4` + `G8` + `G3`, run on the Step −1 admissible
> contract** *(`Specs/Davis.md` at the 137-line read spec; `Official_Population_Census.md` L392–398, L496, L613)*
> **PLUS four post-contract additions:** the **410 km² extent** `[corrob]` · the **Division-of-Industry tier
> grading and 876,514 workforce** `[corrob]` · the **two ratified climate corrections** (`R-3`: warm endpoint
> **+3.2 °C**, two non-negative months; `R-7`: retention **38.5%**) · **`DR-7`'s admission of L127's material.**
> ⛔ **Excluded:** `Local_Cultures/`, `Local_Robot_Culture/` *(open at Step 5, as a check)* · the
> differentiation table *(write-only)* · all other cities.

## 4.2 · The shape verdict

> # **BALANCED — all four quadrants populated, from all four generators, with no empty cell.**
> ### **And its distinguishing feature: STANDING COST is the only quadrant in which all four generators return entries OF THE SAME KIND.**

⛔ **I considered `cost-dominant` and reject it as an overclaim.** Its finding is *"the location's identity has
quietly become its own maintenance,"* and it is expected *"for hostile-environment outposts, declining
settlements, and anything on life support."* **Davis is declared LIVING, holds 1,158,314 people, and its
strength quadrant is full of genuine free gifts rather than hard-won ones.** The cost quadrant is heavy; it is
not dominant.

⭐ **§4.0 item 2's check, run and passed:** STANDING COST fills from **physical, founding, demographic and
functional** constraint alike — **not from known institutions.** ***Davis's standing cost is IMPOSED, not
voluntary.***

## 4.3 · ⭐⭐ The uniformity — what all four cost entries have in common

**Water across the frozen months. The record across generations and across hands that are gone. A common medium
across cohorts. The crop across the dark. The verified/inherited distinction across time.**

> # ***Davis's standing cost is, in every single register, the cost of carrying something across a gap in which it cannot be replenished.***

**And it is physical before it is metaphorical**, which is what earns it: **52% of the annual precipitation
falls in Mar–Jun, into the cold and the dark; 13% falls across the entire Nov–Feb light-and-work block; and 45
of every 72.8 mm leaves regardless.** ***Even the water is an interval problem.***

- *Third order:* ⭐⭐ **a city organized around carry-over does not measure itself by what it produces. It
  measures itself by what it still has at the end of the interval** — a completely different relationship to
  time than a city organized around throughput.
- *Fourth order:* ⭐ **the measure everyone here reaches for is duration — *how long will this last* — applied
  to water, to seed, to light, to a page.** ***The standing verb of the place is HOLD, not MAKE.***
  ⛔ *(Nothing priced, no unit named, no wage, fee, tariff or freight rate — `DR-3` untouched.)*

## 4.4 · Balanced's question — *what does the balance cost?*

> ## ⭐⭐ **It costs Davis the ability to see what it is paying.**
> **The strengths are free gifts** — a wind that is only wind, ground that does not move, a stacked light
> block, water already liquid. **Nobody built them and nobody maintains them.** **The costs are all carry-over
> costs** — paid continuously, across intervals, by everyone, and itemized nowhere. ***A place like that has no
> feedback on its own performance: it cannot tell, from inside, whether it is doing well because it is well-run
> or because the mean wind speed is 5.6 m/s.***
>
> ### ⭐⭐⭐ Third order — and it explains the one line of canon that says what Davis is
> ***That is why L143 describes Davis by its ENDOWMENT and not by its WORK.*** *"Breadbasket"* and *"research
> hub"* both name what the place is **good for**; neither names what it **costs**. **A city that cannot see its
> own account describes itself by what it was given.**

## 4.5 · ⭐ THE DOUBLE READING — `02` §4.0 item 3 and `00_RUNBOOK.md` L2509–2517

**The second location the three-step rule needs is this same location read twice.**

- **Reading A — the NARROW set:** the four generators on the Step −1 contract **alone**. No extent figure, no
  tier grading, `R-3`/`R-7` still only proposed, `G3` a single ungraded sentence. **This is what Steps 0 and 1
  actually had.**
- **Reading B — the FULL set:** as declared at §4.1.

**Step 1 — the shape gives the question.** ✅ **Shared, as the rule requires:** both readings return four
populated quadrants and both therefore ask *what does the balance cost?*

**Step 2 — the generator gives the instrument, and nothing about the shape predicts which.** Under **A** the
instrument is **`G4`** — on the thin set it is the only generator returning a sharp result, since `G3` is one
sentence, `G2` is a table with two known defects, and `G8` is arithmetic. Under **B** the instrument is
**`G3`** — the tier grading supplies a distinction no other generator has.

**Step 3 — the instrument gives the consequence, and here the readings separate.**

| Axis | **Reading A** *(narrow: contract set only)* | **Reading B** *(full)* |
|---|---|---|
| **Instrument** | `G4` — the documentary inheritance | `G3` — the grading of compulsion |
| **What the balance costs** | The ability to **check itself**: with no correction loop, Davis never learns it was wrong until the ground reports, and the ground reports late | The ability to **choose**: 60% of the workforce structure is assigned, so the balance costs Davis the authorship of its own days |
| ⭐ **TENSE — where and when the loss happens** | ⭐ **PAST-TENSE, ONE-TIME.** The loss occurred at the founding, five centuries back: the living institution did not survive the handoff. Everything since is consequence. **Davis is a city living downstream of a loss it did not witness** | ⭐ **PRESENT-TENSE, RECURRING.** The loss happens every season, in the ordinary allocation of weeks: the half-mandate yields to the full mandate on the same calendar, forever, in the same direction. **Davis is a city paying continuously and itemizing never** |
| **Who pays** | Whoever notices something the record does not cover — a diffuse, unnameable few | Whoever is trying to do the science in the harvest weeks — recurring, structurally identifiable, and (because the two mandates share a subject) numerous |
| **Where the remedy would live** | **In its own past** | **In the parent** |
| **Is the loss still live?** | No — it is settled and historical | **Yes — it recurs annually** |
| **Can the city perceive it?** | **No.** The witnesses are five centuries gone and were never Davis's | ⭐ **Almost — and it MISREADS it.** The cost is fully visible as individual failure and never as structural charge |

> ## ⭐⭐⭐ THE DISAGREEMENT IS WORTH MORE THAN EITHER READING — the honest synthesis
> **Davis's standing cost has two layers with different tenses. The narrow reading can see only the old one;
> the full reading can see only the live one. And the old one is the REASON the live one is invisible:**
>
> ### ***A city with no correction loop has no instrument for noticing a recurring misallocation — so a present-tense, repeating cost presents to it as a past-tense, settled condition.***
>
> **The founding loss is not merely historical. It is the mechanism by which the current loss goes unrecorded.**
> *(This is exactly what §4.0 item 3 promises and it was not visible from either reading alone.)*

⚠ **`02`'s check applied honestly:** the step-3 consequences are **not** the same under both readings — they
differ in instrument, in payer, in address, in tense and in perceptibility. **The shape was not doing all the
work.**

---

# §5 · ITEM 5 — DEFICIT ADDRESSES (PEER-FREE), AND THE COUNT

> ⛔ **One address in `02` §4.1's peer-free set is STRUCTURALLY UNAVAILABLE to this pass: *"in a neighbor's
> present."*** It requires a named counterparty's **present state**, which requires reading another location,
> which the ONE LOCATION law forbids in-run. ⭐ **Recorded as UNAVAILABLE, not as empty** — it is not that no
> neighbor qualifies; it is that the instrument needs an input the law refuses. *(Noted as a methodology
> observation: one of the five peer-free addresses is not in fact peer-free.)*

| | Deficit | Gen | **Address** | Consequence |
|---|---|---|---|---|
| **D1** | **No correction loop** | `G4` | ⭐ **IN ITS OWN PAST** | Remedy is historical, not geographical |
| **D2** | **No social instrument of refusal or subtraction** | `G8` `G4` `G3` | ⭐ **DIFFUSE** | No counterparty, no grievance, no critic — produces drift |
| **D3** | **No shortfall vocabulary under a MANDATED-FULL obligation** | `G3` | **IN THE PARENT** `[PA-3]` | Reaching it means admitting the city cannot meet its own number ⇒ **under-reporting** |
| **D4** | **No water from the sky; the whole supply is stored and leaking** | `G2` | ⭐ **NOWHERE AT ALL** | Genuinely unremediable |
| **D5** | **No arrival narrative; the founders are 4.93%** | `G8` | **DIFFUSE** | No precedence politics can form |

## 5.1 · ⚠ EVIDENCE CHECK for **D1** — *"are the people who could NAME this deficit still here?"*

⛔ **No — and in the strongest available form: they were never here.** The living institution was never Davis's;
it belonged to operators who were gone before the exiles arrived. **So there is no departed witness who could be
asked, no returning visitor, and no Davis record of the thing itself** — the only record Davis holds is the one
the institution *left*, and by its nature that record documents **the terrain and not the teaching.**

> ### ⭐⭐ This is a step past `02` §4.1's exodus case, and it deserves its own name
> **The exodus city's nostalgia is factually correct and epistemically unchallengeable.** ***Davis's is not
> nostalgia at all, because there is nothing to be nostalgic for.*** **The city cannot frame the absence as a
> loss**, because it has no prior state to compare against — not in memory, not in record, not in anyone's
> family account.
>
> *Third order:* ***Davis does not experience "we used to be able to do this." It experiences "this is how one
> learns." A deficit with no prior state anywhere is indistinguishable, from inside, from the nature of
> knowledge itself.***

## 5.2 · ⚠ EVIDENCE CHECK for **D2** and **D5** — *"has anyone here ever had a reason to formulate this as a problem at all?"*

**D2 — ⛔ NO, and the reason is structural.** A grievance requires a counterparty; the absence of a refusal
instrument supplies none *by definition*; and **`G2` already performs the refusing** — impersonally, absolutely,
and adequately (§3.3). **Nobody at Davis has ever stood in front of a person who could have said no and did.**

> ### ⭐⭐ So D2 is not merely unaddressed — **it is unspeakable in §4.1's precise sense: the observation has no natural author and no natural occasion.** ***And that is the strongest single result on this axis, because it explains the exit's mechanism-shaped hole without inventing a mechanism to fill it.***

**D5 — ⛔ NO.** No arrival order was ever recorded, so the question *who was here first* has no stakes-bearing
answer beyond the founders', and they are 4.93%. ⚠ **And by Act 2 the question stops being askable at all**
(origin becomes ancestry), **so it expires before it is ever asked.** ⭐ *What follows, handed forward rather
than built here:* **a city with no seniority axis distributes standing on some other axis** — the two the
profile actually supports are **generational depth** (open to everyone born here, robots included) and
**engagement with the record.** Phase 2 onward.

## 5.3 · ⭐ Why **D4** earns `nowhere at all` — `02` §4.1 says the case *"must be earned"*

**Not "in its own past":** there is no past in which more precipitation fell. **Not "in the parent":** no
import is written, `PA-4` forbids scaling anything off assumed throughput, and a water import at this population
would be a magnitude claim I cannot make. **Not "diffuse":** it is precisely located — the atmosphere over this
coast. ⭐ **The only "remedy" is not needing sky water, which is a redesign and not a remedy.** ✅ **Earned.**

> ### ⭐⭐ And the consequence is the opposite of what the address usually implies
> ***A genuinely unremediable deficit produces the one clean, blameless, universally-shared fact in the city.***
> Everyone knows it; nobody resents it; no one is at fault; it is the only thing here that is everyone's problem
> in the same way. ⭐ ***In a city with no social instrument of refusal, the unremediable physical deficit is the
> closest thing it has to a shared civic fact.***

## 5.4 · ⭐⭐ THE COUNT, AND WHAT THE COUNT MEANS

> ## **FIVE deficits addressed. FOUR distinct addresses. `in its own past` ×1 · `diffuse` ×2 · `in the parent` ×1 · `nowhere at all` ×1 · `in a neighbor's present` ×0 (UNAVAILABLE, not empty).**

⚠ **`02` §4.1's count warning — *"a count above one should raise suspicion"* — belongs to the PEER-REQUIRED set
(multiply-addressed) and is not imported here.** The peer-free count is read on its own terms:

1. **No two of Davis's sharpest deficits share an address.** ⇒ **there is no single remedy and no single
   counterparty** ⇒ ***the city cannot form a reform program. It can only form four unrelated complaints.***
2. **Two of the four cannot be formulated at all** (D2 and D5, both diffuse, both failing their evidence check).
3. **One is unremediable by construction** (D4) — and is therefore the only one everybody already knows.
4. ⭐⭐⭐ **Which leaves exactly ONE deficit Davis can perceive as a problem: D3, addressed in the parent — and
   §4.1 says that address produces *under-reporting.*** ***One perceivable deficit out of five, and its
   perception mechanism is a mechanism for not mentioning it.***

---

# §6 · ITEM 6 — POPULATION ÷ EXTENT

> ## ⭐ **IT IS RUNNABLE. Step 0 expected it blocked; the extent figure now exists.**

```
POPULATION   1,158,314          [ratified, Census I, governing by DR-4]
EXTENT             410 km²      [corrob — schema extraction; closed by the coastline ruling]

1,158,314 ÷ 410  =  2,825.16 / km²
```

**One division. No interpretation.**

- ✅ **Plausibility check — the cheapest in the methodology — PASSES.** The result reproduces the source's own
  stated density of **2,825/km²** exactly. *(A hand-check of the kind Step 7 requires, run here as the runbook
  directs: "Do it here, not at QA.")*
- ✅ **Direction is correct: extent is the INPUT and density the OUTPUT.** ⛔ Extent is never derived from
  density.
- ⏸️ **The BAND stays UNDETERMINED and the DIVERGENCE QUESTION stays OPEN.** `01` §2.1 defines bands on
  population only and supplies no extent scale at all. ***The figure exists; the instrument that would grade it
  does not.*** **Population band remains 5, ruled by `DR-4`, not re-litigated.**

## 6.2 · ⚠ A separate observation, adjacent to the division and not part of it

**410 km² (Davis's extent) against ~400 km² (the Vestfold Hills' ice-free area, `Specs/Davis.md` L60).** The
admitted set does not state that these are the same object, and they differ by ~2.5%. ⭐ **But they describe the
same coastal ice-free region, and to within the precision available, Davis's extent IS its ice-free ground.**

> ### ⭐⭐ Which sharpens load-bearing fire #14 into something answerable later
> ***If the city's extent is the ice-free area, then the city limit and the ice margin are the same line*** —
> and whether that line is fixed, seasonal or moving is not a scenery question but a **territorial** one.
> ⛔ **Not resolved here** *(the admitted set does not say)*. **Handed forward with the sharpening attached.**

---

# §7 · `G1` — READ LAST, AS A CHECK. ⛔ **THE CHECK IS UNRUNNABLE, AND THAT IS THE REPORT**

**Davis's pair: `Earth / Earth`.** Corroboration tier; counts zero toward the rule of three.

| Half | Status | Ruling here |
|---|---|---|
| **Element — Earth** | ⛔ **RESERVED** by `DR-1` | **No finding above rests on it.** ⚠ *Unusually live at Davis:* exposed rock, ground, cultivation and groundedness are **precisely** what a reader would intuitively call "Earth." **Every such sentence in this document has been checked and none connects Davis's ground or its agriculture to the Element** |
| **Planet — Earth** | ✅ ratified, meaning **readable in principle** | ⛔ **NOT READ, and deliberately: `Planetary_Symbols.md` is outside this reader's admissible set.** `02` §6.0 is categorical — ***read the member from the FILE, never from the NAME.*** Reading "Earth" off the bare word is the exact error §6.0 exists to prevent, and it inverted a whole capability reading once already |

**Pairing relation (`02` §6.3):** the pair is **doubled** — both tokens are the same word. §6.3 would classify a
doubled pair `Reinforcing`, **but that classification names a quality, and naming the quality requires both
members' registered content, one of which is reserved.** ⛔ **Classification DEFERRED with the member reading.**

> ⭐ **So: not a null, not a corroboration, not a mismatch — an UNRUN check with a stated reason.** It neither
> supports nor challenges anything above, and the spine does not lean on it in either direction.

---

# §8 · THE SPINE

## 8.1 · ⭐⭐⭐ The `G2` × `G4` conflict, mined — the one Step 0 handed forward explicitly

**`00_Frame.md` §0.7:** *"the `G2`×`G4` conflict: a documentary inheritance without a living institution,
against ~400 km² of exposed rock and a −10.0 °C mean."*

**Where they actually conflict — and it is not where it looks.** They do not disagree about content. ⭐ ***They
disagree about what kind of TEACHER this place is.*** `G4` says the teaching institution is absent. `G2`
describes an environment that is an unusually good teacher: **consistent** (a 30-year normal reproduces; the
monthly table sums exactly to its own annual), **survivable while you learn** (5.6 m/s, no katabatic event
generator, a genuine above-freezing season), and **slow** (its failure modes are cumulative, not instantaneous).

> ### Both-are-true — what single property produces both readings?
> # ***Davis's environment can be learned from written observation because it is STATIONARY.***
> **The wind is not an event generator. The ground does not move. The lakes freeze and open on a schedule. The
> precipitation is small and steady.** ***The five-century-old record survived usefully because its subject
> did not change.***
>
> **Different objects, different scales, both stand:** `G4`'s absence is about **transmission** — person to
> person. `G2`'s presence is about **the subject** — the ground itself.

### The orders out of it

1. **First:** the record still works because the ground is still the ground.
2. **Second:** ⭐ **so verification replaces authority.** Nobody here has to be *believed* — the ground can be
   checked — and going and looking has been the cheapest way to settle anything since the first generation,
   **because the thing you would look at has not moved.**
3. **Third:** ⭐⭐ ***Davis's characteristic form of argument is "show me the entry," and its characteristic form
   of authority is a dated observation rather than a person.*** Which is why the founding produced no native
   legitimacy (§2.2 D2) **and never needed to** — the legitimacy is in the log. And why disagreeing with the
   record is permitted-but-expensive rather than forbidden: **you can always beat the record; you simply have to
   go out and come back with a better entry, and that costs you a season.**
4. **Fourth:** ⭐⭐ **this is the one thing the place supplies that no origin supplies** — which is what the
   twenty-one communities converge on (`G8` strength 1's cut, now legal to make), what a delivery cadence needs
   (`G3`), and what a lake under ice can only be known by (`G2`). ***The record is not a library. It is the
   city's only instrument of agreement.***

## 8.2 · ⭐⭐⭐ THE SPINE, STATED

> # **Davis settles things by going and looking.**
>
> **It was founded by people whose only teacher was a written record of ground that has not moved since
> `[G4 × G2]`; it inherited no authority of any kind, from either its founding or its composition
> `[G4 + G8]`; and nothing social here has ever had to say no, because the environment does all the refusing
> `[G2 vs G4/G8/G3]`. So the dated observation became the only thing anyone here has ever had to agree with —
> and everything the city is good at, everything it cannot do, everything it must keep paying and everything it
> quietly charges people for, hangs off that.**

**What hangs off it, in the frame's own vocabulary:**

| | |
|---|---|
| **What it is good at** | Holding ground nobody has to negotiate for, growing things under a sky that gives nothing, and studying the thing it grows — because its work and its science are two depths of one practice |
| **What it cannot do** | Correct itself in time · say no to a person · name its own shortfall · account for its own arrivals |
| **What it pays, continuously** | Carrying things across intervals in which they cannot be replenished — water, light, a page, a cohort, a distinction |
| **What it permits and charges for** | Disagreeing · not reading · needing to be shown · doing the science in the weeks the harvest wants · and leaving, on terms nobody wrote down |
| ⚠ **Its shadow, qualitative and un-sized** *(`00d` at Band 5)* | ⭐ **With no institution to which a cost can be addressed, structural costs land on individual reputations.** The one who disputes the record is *difficult*; the one who cannot learn from a page is *slow*; the one whose science never finishes is *disorganized*; the one keeping an origin practice alive is *keeping it up*; the one who goes out in July is *careless* — until once they are not fine. ***Davis converts structural charges into character judgements about persons, authorlessly, in complete good faith, and invisibly from inside*** |

## 8.3 · ⭐⭐ THE UNRECOGNIZED INSTRUMENT — run now, and never earlier (`02` §4.2)

*The location is already doing the thing it cannot do, somewhere, for an unrelated reason, and has never noticed
the method generalizes.*

**Davis's central deficit is that it has no instrument of refusal (D2).** ⭐ **And Davis has possessed, for
centuries, a fully developed apparatus for refusing a proposition:** *verify the claim against the ground, and
write down the difference.* **It has a procedure, it takes evidence, it produces a dated result, and it
preserves the disagreement rather than suppressing it.**

> # ***Davis has a refusal instrument. It has never once been turned on a decision about a person or an allocation.***

⭐ **Found second, so it sharpens rather than softens** — exactly as the technique requires. **The change
available here is not to bring Davis something new but to connect two things it already holds.** ⛔ *What that
connection would be used for, and by whom, is not this pass's to write — nothing here presumes a player, a hub,
a quest, a gate or a companion (`RESERVED` item 3).*

## 8.4 · The closing test — `02` LAW 0

> *Could a person live an entire life here — and would that life be unlike a life in any comparable place?*

**A life spent in a city whose arguments end with a dated entry; whose year is a four-month blaze of light and
work followed by an eight-month carry; whose science is always owed and never finished; where the only thing
that ever refuses you is the weather; and where what it costs you is never named as a cost but as a quality of
your character.** ✅ **Yes.**

---

# §9 · RECORDING — snags, kills, open slots, and what this step does NOT claim

## 9.1 · ⛔ FINDINGS KILLED, recorded rather than quietly dropped

1. ⭐⭐ **KILLED: the link between the `G3` tension and "who leaves."** `02` G3 says a function divergence
   *"will surface in governance, in export culture, and in **who leaves**,"* and `00.1` §3.2 notes that Davis
   *"has a measured answer to 'who leaves.'"* ⛔ **The two cannot be joined.** The measured differential is by
   **kind** (robot/human); **fire #2's hard ceiling forecloses reading sector or origin off it permanently.**
   ⭐ **And the tension itself has no differential to offer:** it is a contest over the **same summer weeks**
   — ice-off and the growing season are one interval — and **whoever is doing the work is in it, robot or
   human.** ✅ **Empty slot. Left open. NO FORCED FIT.** *(`02`'s named instrument is unavailable here by
   construction, not by oversight.)*
2. **KILLED: reading `G5` for asymmetry.** `02` G5's yield is *"direction AND volume."* Volume does not exist
   anywhere. **Direction alone was used for relation and for nothing else.**
3. **NOT USED: any inference about `G6`'s single matching line.** `01` §1.5 flags that one reader inferred a
   content class from a quarantined line's length and punctuation and that a second reader called it a hazard.
   ⛔ **Step 2 relies on it nowhere, and `G6` was not needed** (§1.3).
4. **NOT USED: the census rows' leading ordinals** (`| 13 |`, `| 14 |`) — an inter-city rank inside admitted
   lines. Quoted once, below, as byte-level proof; **used in no claim.**

## 9.2 · ⚠ SNAGS AND SELF-CORRECTIONS DURING THIS STEP

1. ⚠ **I began by accepting `00_Frame.md` §0.6's headline question as the spine and had to stop.** It is the
   pass's own strongest finding and it bakes election in. **§0 exists because that framing nearly wrote the
   spine before it was examined.**
2. ⚠ **I initially reached for `cost-dominant` because the cost quadrant is uniform.** Uniformity is not
   dominance; the strength quadrant is equally full and the location is declared LIVING. **Corrected to
   BALANCED and the uniformity reported as the balance's distinguishing feature instead.**
3. ⚠ **`G2` × `G4` are partially content-dependent** *(the inheritance is a record OF the terrain)*. Declared at
   §1.1 rather than concealed; the selection survives because they disagree in kind.
4. ⚠ **One of `02` §4.1's five "peer-free" addresses is not peer-free** *("in a neighbor's present")*. Recorded
   as unavailable-by-law; **a methodology observation, offered and not applied unilaterally.**
5. ⚠ **`R-3` and `R-7` were applied as corrected values** (warm endpoint +3.2 °C, two non-negative months;
   retention 38.5%). `01` handed them forward as *diagnosed, corrections proposed, not applied.* **Using them
   is a judgement this step makes and declares; the source spec still carries the old figures.**

## 9.3 · ⚠ THE ADMITTED REAL-WORLD AIRSTRIP REFERENCE — texture noted, NOT adopted

`Antarctic_Stations_With_Airstrips.md` is in this reader's admissible set and lists **three** air facilities at
the real Davis Station — **Davis Plateau Skiway, Davis Sea Ice Skiway and Plog Island Skiway, all ice-surface,
no gravel or blue-ice wheeled runway** — and states in its own caveat that **most Antarctic airstrips are
seasonal, open roughly October–March.**

- ✅ **Legal use, and the only one taken:** `02` G7's surviving carve-out permits a real-world comparable for
  **physical texture** — surface, vehicle form, seasonal usability — **never for character.** The texture here
  is that such access is **ski-surface and interval-bound**, which is the same shape as everything else in §4.3.
- ⛔ **NOT adopted, and deliberately.** **Tepenian canon states no aviation for Davis anywhere in the admitted
  set.** Inventing one would be a forced fit in the second direction the law names — *inventing a bespoke
  member to fill a blank.* ⏸️ **Slot left explicitly open: "none is stated" does not read as "none is
  possible."** ⚠ The file's own caveat *(compiled via automated fetch; verify before treating as load-bearing)*
  is honored: nothing above rests on it.

## 9.4 · HANDED FORWARD

| To | Item |
|---|---|
| **Step 3** | ⭐ **The spine gives the research its target:** a stationary, quantified environment and a documentary founding. `LAW 0-R` binds; `Davis_Research_Log.md` is still absent |
| **Step 3** | ⭐ **The `G2` picks that pay:** the wind's non-katabatic character *(the enabling fact, not the temperature)*; the four lake types including hypersaline and landlocked marine basins; sublimation loss in a low-precipitation coastal oasis |
| **Phase 2+** | ⭐ **Where standing is distributed, given no seniority axis:** generational depth, and engagement with the record. **Two candidates, neither chosen here** |
| **Phase 2+** | ⭐ **The five empty `Inflected` slots** — `01` calls this *"where most good local culture actually lives,"* and the spine now says what they should be inflected BY |
| **Step 5** | The culture material opens as a **check**. ⚠ **Pre-declared non-independence stands:** if it returns a harvest-versus-archive tension, that is **corroboration at best and must be tagged** (`00.1` §5.1) |
| ⏸️ **Still open, NOT re-raised** | `Resettled` · `Settlement + Installation` · the `City_Vision_Notes/`↔RWBEM collision · the second ONE LOCATION test — **all disposition B in `01` §1.6a and flagged once already.** ⛔ **No new developer question is raised by this step** |

## 9.5 · ⛔ WHAT THIS STEP DOES NOT CLAIM

**No comparison to any city, no rank, no z-score, no "nth of N," no superlative, no other place as baseline —
and the second test was applied: no claim above requires knowing anything about any other place in order to be
true.** · **No distributional result; no sub-location; no finding scaled off a sector headcount or off assumed
throughput.** · **No person named, no practice named after a person, no demonym, no player, no mortuary
practice, no Element meaning, nothing priced.** · **No general-population claim derived from either named role.**
· **No generator vocabulary in Davis's own claims — citations bracketed throughout.**

---

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md
LRANGE: 2497-2525
LINES: 29
L1: # Step 2 — Build the spine
LMID:    > once on the full one.* **1.** The shape gives the question. **2.** The generator gives the instrument.
LLAST:
QUOTE: 5. Read each deficit's **address**, and **count the addresses.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md
LRANGE: FULL
LINES: 760
L1: # Generators, the Capability Frame, and Symbol Binding
LMID: **So the derivation runs the other way from the district method:** rather than deriving a shadow separately and
LLAST:    emphasis.**
QUOTE: Do not ask which generator is right. Ask what single property of this place would produce both readings —

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Davis.md
LRANGE: 1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179
LINES: 137
L1: # Davis
LMID: **Mean annual temperature:** -10.0°C  _(READER station: Davis; 1991–2020 WMO standard normal)_
LLAST: - **Relationship to Mawson (the city, different subnet)** — both named for/connected to Australian Antarctic figures, but administratively and geographically separate; worth clarifying whether any cultural connection existed despite the subnet divide
QUOTE: Learning from a written record isn't the same as being taught by a living institution

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Energy_Grid_Failure_Rationale.md
LRANGE: FULL
LINES: 145
L1: # Why "Just Fix the Energy Grid" Isn't a Practical Solution
LMID: infrastructure could replace.
LLAST: - **Climax (The Great Blackout):** All the half-measures and compromises finally catch up, forcing the player to make the ultimate choice about the future of the entire system.
QUOTE: robots need stable, high-density siligel-compatible power; humans need consistent low-level heat

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/Davis.md
LRANGE: FULL
LINES: 16
L1: # Climate Reference: Davis
LMID: **Annual mean temperature:** -10.0°C
LLAST: _Source: BAS READER (Reference Antarctic Data for Environmental Research), https://legacy.bas.ac.uk/met/READER/ — cite as Turner et al. (2004), Int. J. Climatol. 24, 191–211._
QUOTE: | +0.9 | -2.2 | -8.0 | -13.5 | -16.0 | -15.7 | -17.1 | -17.1 | -15.7 | -11.8 | -4.2 | +0.0 | -10.0 |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md
LRANGE: FULL
LINES: 99
L1: # Antarctic Stations With Functional Airstrips / Aircraft Ground Infrastructure
LMID: | Plog Island Skiway | Davis Station | Australia | Ice |
LLAST: - Several names on this list use "skiway" specifically (a compacted snow or ice surface usable only by ski-equipped aircraft) as distinct from a genuine wheeled-aircraft runway (gravel or blue ice, usable by wheeled cargo planes) — this distinction may matter if Tepenia's own lore wants to differentiate between "reachable by any aircraft" and "reachable only by specialized ski-equipped planes."
QUOTE: Most Antarctic airstrips are seasonal (open only during the austral summer, roughly October–March) and conditions/operators can change year to year.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md
LRANGE: 392-398,496,613
LINES: 9
L1: **Davis** *(Vestfold Hills, Prydz Bay — mainland coast)*
LMID: | Primary | China |
LLAST: | 14 | Davis | Mirny | 437,423 | 344,173 | **781,596** | |
QUOTE: **Davis** *(Vestfold Hills, Prydz Bay — mainland coast)*

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00.1_Step_MINUS-1_Input_Contract.md
LRANGE: FULL
LINES: 371
L1: # Davis — Step −1 · THE INPUT CONTRACT
LMID: > **L127:** *"No living environmental **knowledge** survived that chain of handoffs — but preserved journals,
LLAST: ⛔ **Step 0 — FRAME — opens next.**
QUOTE: No finding may rest on what the Element "Earth" means.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00_Frame.md
LRANGE: FULL
LINES: 397
L1: # Davis — Step 0 · THE FRAME
LMID: declares two numbers **so that the second checks the first** — *"when they diverge, the divergence is
LLAST: ⛔ **Step 1 — AUDIT WHAT IS INHERITED — opens next.**
QUOTE: When leaving became possible, robots left at substantially higher rates than humans. What about this place made that so?

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/01_Inherited.md
LRANGE: FULL
LINES: 363
L1: # Davis — Step 1 · WHAT IS INHERITED
LMID:
LLAST: ⛔ **Step 2 — BUILD THE SPINE — opens next.**
QUOTE: The one enormous outflow — 376,718 people — is recorded as a NUMBER and never as a MECHANISM.
