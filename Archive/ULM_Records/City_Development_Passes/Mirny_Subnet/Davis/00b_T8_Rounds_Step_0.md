# Davis — Step 0 · T8 ROUNDS, RAW

**Written 2026-09-14.** Evidence behind `00_Frame.md`. ⛔ Raw reader output, consolidated verbatim —
not summarized. Three independent readers (Round 1), mechanical ground-truth verification (Round 2),
agent-to-agent cross-check (Round 3).

> ⚠ **ROUND 2 NOTE — the repo verifier returned a FALSE failure.** `triple_read_verify.py`'s
> `parse_proof()` continuation rule has no terminator, so the LAST proof block's `QUOTE` absorbed every
> following line in each reader file (66,055 / 77,090 / 64,691 chars). Re-run out-of-tree with a
> correctly-terminated parser: **44 of 45 field-sets clean.** The one real divergence was an unstated
> `LLAST` convention (blank final line). ⛔ **The repo tool was NOT patched.**

---

# ROUND 1 — READER A

# DAVIS — STEP 0 (FRAME) — **T8 READER A**, independent

**Run mode: WARM.** Read independently, without contact with Readers B or C.
**Written 2026-09-14.** No repository file was edited. This file is my only write.

> **Method note on the proof blocks.** I read every file with the `Read` tool directly by path, at the bound
> ranges. I then recomputed `LINES` / `L1` / `LMID` / `LLAST` mechanically (`splitlines()`, 1-indexed within the
> admitted set) rather than transcribing them by hand, and verified every `QUOTE` is a verbatim substring of a
> line **inside** its admissible range. Three admitted lines are genuinely blank (`00_RUNBOOK` L2447 and L2479;
> `00b` L131; `Cultural_Synthesis_Techniques` L1196) and are reported as empty, which is the truth about those
> bytes.
>
> **`graphify` was not used, and no repo-wide search was run to locate any of these files.** The `PreToolUse`
> hook fired on essentially every call; disregarding it is this task's instruction, not my own judgment.

---

# PART 1 — THE 15 PROOF BLOCKS

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md
LRANGE: 2416-2479
LINES: 64
L1: # Step 0 — Frame
LMID: 
LLAST: 
QUOTE: Cheapest gate, highest yield, fails in both directions.

*(`LMID` = admitted line 32 = file line 2447, which is blank. `LLAST` = file line 2479, also blank.)*

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md
LRANGE: FULL
LINES: 582
L1: # Frame, Typology, and Inheritance
LMID: | **Transit-only** | Who maintains it, and do they count as living here? |
LLAST: would have made visible before the writing started.
QUOTE: **Declare two numbers, not one:** the **population band** and the **extent band**.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Run_Modes_Warm_and_Cold.md
LRANGE: FULL
LINES: 177
L1: # RUN MODES — WARM and COLD, defined
LMID: > that is indistinguishable from good work, which is exactly what makes it dangerous.**
LLAST: > it is the one that produces cities.**
QUOTE: THIS CITY'S OWN CULTURE MATERIAL IS READ LAST, AND READ AS A CHECK.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md
LRANGE: FULL
LINES: 261
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: 
LLAST: baseline stated beside it.
QUOTE: THE TEST IS ARITHMETIC — the only part that does not run on the same faculty that produced the error.

*(`LMID` = line 131, which is blank.)*

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md
LRANGE: FULL
LINES: 222
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: > **A district operates on its own sincere conception of what "doing good" means and what a proper community
LLAST: *secretly awful*, the proportion is wrong — regardless of how well-sourced each individual finding is.
QUOTE: The Shadow is a **byproduct**, never the operating principle.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00f_Review_Panel.md
LRANGE: FULL
LINES: 832
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: related, and affectionate,"* the origin of a place's spirituality and its *"sense of the mystic oneness and
LLAST:   now.)*
QUOTE: Before accepting any objection, ask: would satisfying this make the district more like the other twelve?

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/Cultural_Synthesis_Techniques.md
LRANGE: FULL
LINES: 1196
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: **The question.** *Which of this location's picks has nothing in the existing material actually derived from
LLAST: 
QUOTE: THE ROSTER IS A DEMOGRAPHIC FACT. THE LOCAL CULTURE IS A DIFFERENT OBJECT.

*(`LLAST` = line 1196, which is blank. The file's own header pin states "1193 lines"; the bytes give 1196.)*

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/Real-World_Basis_Extrapolation_Method.md
LRANGE: FULL
LINES: 463
L1: # ⭐⭐⭐ LAW 0-R — RESEARCH FULLY. **A PICK IS NOT EXHAUSTED BECAUSE IT HAS BEEN SEARCHED.**
LMID: ### ⭐ IT IS A SEQUENCING RULE, NOT A REPEAL — **the prohibition above is UNCHANGED**
LLAST: 3. **A real detail beats an invented one every time.**
QUOTE: ONE SEARCH AGAINST A PICK ESTABLISHES THAT THE PICK EXISTS. IT DOES NOT ESTABLISH WHAT THE PICK HOLDS.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md
LRANGE: FULL
LINES: 438
L1: # Robot Physiology and Cultural Practices
LMID: ### ⭐⭐⭐ THE GRAND-TIMELINE ACTS
LLAST:   **Flagged 2026-07-09, for a possible future questline (not a religion):** during a Robot Religions development session, a "trace your own origin" concept was considered as the basis for a new religion (a reground of a ChatGPT-suggested "Cult of the Source") and set aside — the developer liked the mystery but didn't think it actually works as a religion's foundation. The mystery itself is worth keeping: a robot tracing which mark/generation their own chamber was built to, and from there discovering that the schematic's actual designer (Neumayer, credited nowhere, the same uncredited pattern as the Amundsen Tower) goes unknown to almost everyone built from their work — a solvable-in-principle, currently-forgotten origin mystery, not an abstract data-mysticism. Already has a discoverable in-game hook to build from: Calethina's own chamber (the one that built the player character) traces to the historical, now-dark Mountain Pass site. See `Factions/Robot_Religions/Cymatics_reverence/Cymatics_reverence.md`'s development history for the fuller reasoning trail.
QUOTE: COMPOSITION NAMES THE STOCK; TIME AND PLACE PRODUCE THE CULTURE.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Repo_Scope.md
LRANGE: FULL
LINES: 30
L1: # Repo Scope — A Binding Law
LMID: - **Game mechanics of any kind** — stat blocks, XP/leveling systems, companion/romance gating, quest triggers, re-spec systems, ending-branch design, UI/UX, engine or asset-pipeline decisions. This is InnerTepeniaGDD's (or OuterTepenia1_GDD's) own design work, not shared canon.
LLAST: Before adding or porting content here, ask: does this tell you *when*, *where*, or *who*? If the honest answer is "it tells you *how to play/read it*" or "*what mechanically happens next*," it's out of scope — note its existence if useful for cross-reference, but don't port the content itself.
QUOTE: If a piece of content doesn't serve one of those three questions, it does not belong in this repo

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/README.md
LRANGE: FULL
LINES: 70
L1: # The Second Interwar Period — **2564–2812**
LMID: > Amundsen Tower. Their being fully interconnected further defined their sense of national identity in who
LLAST:    environmental setting · local struggles and hardships · local goals · local sensibilities and habits.*
QUOTE: THE ERA SPANS BOTH ACTS AND IS MOSTLY ACT 2.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/Timeline.md
LRANGE: FULL
LINES: 562
L1: # The Second Interwar Period — Timeline (2564–2812)
LMID:   federation spirit survives without that specific person.
LLAST:   Reference.md` as beats are developed, to keep all documents consistent.
QUOTE: now canonized as the single precise year 2812 — roughly **248 years**.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md
LRANGE: 392-398,496,613
LINES: 9
L1: **Davis** *(Vestfold Hills, Prydz Bay — mainland coast)*
LMID: | Primary | China |
LLAST: | 14 | Davis | Mirny | 437,423 | 344,173 | **781,596** | |
QUOTE: | 13 | Davis | Mirny | 563,599 | 594,715 | **1,158,314** | *(revised 2026-07-04)* |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Davis.md
LRANGE: 1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179
LINES: 137
L1: # Davis
LMID: **Mean annual temperature:** -10.0°C  _(READER station: Davis; 1991–2020 WMO standard normal)_
LLAST: - **Relationship to Mawson (the city, different subnet)** — both named for/connected to Australian Antarctic figures, but administratively and geographically separate; worth clarifying whether any cultural connection existed despite the subnet divide
QUOTE: Davis is, above all, Tepenia's breadbasket and a prime ecological/limnological research hub

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00.1_Step_MINUS-1_Input_Contract.md
LRANGE: FULL
LINES: 371
L1: # Davis — Step −1 · THE INPUT CONTRACT
LMID: > **L127:** *"No living environmental **knowledge** survived that chain of handoffs — but preserved journals,
LLAST: ⛔ **Step 0 — FRAME — opens next.**
QUOTE: So in-frame — for all 248 years this pass covers — Davis is a living, operating city.

---

COVERAGE: 00_RUNBOOK.md 1-64, no gaps, no overlaps · 01_Frame_Typology_and_Inheritance.md 1-582, no gaps, no overlaps · Run_Modes_Warm_and_Cold.md 1-177, no gaps, no overlaps · 00b_General_Population_Discipline.md 1-261, no gaps, no overlaps · 00d_Shadow_Proportion_Discipline.md 1-222, no gaps, no overlaps · 00f_Review_Panel.md 1-832, no gaps, no overlaps · Cultural_Synthesis_Techniques.md 1-1196, no gaps, no overlaps · Real-World_Basis_Extrapolation_Method.md 1-463, no gaps, no overlaps · Robot_Physiology_and_Cultural_Practices.md 1-438, no gaps, no overlaps · Repo_Scope.md 1-30, no gaps, no overlaps · Second Interwar README.md 1-70, no gaps, no overlaps · Second Interwar Timeline.md 1-562, no gaps, no overlaps · Official_Population_Census.md 1-9, no gaps, no overlaps · Specs/Davis.md 1-137, no gaps, no overlaps · 00.1_Step_MINUS-1_Input_Contract.md 1-371, no gaps, no overlaps

MANIFEST: mapped 15 of 15 files — 00_RUNBOOK.md (2416-2479); 01_Frame_Typology_and_Inheritance.md; Run_Modes_Warm_and_Cold.md; Disciplines/00b_General_Population_Discipline.md; Disciplines/00d_Shadow_Proportion_Discipline.md; Disciplines/00f_Review_Panel.md; Disciplines/Cultural_Synthesis_Techniques.md; Disciplines/Real-World_Basis_Extrapolation_Method.md; Robot_Physiology_and_Cultural_Practices.md; Repo_Scope.md; Second Interwar README.md; Second Interwar Timeline.md; Official_Population_Census.md (392-398,496,613); Specs/Davis.md (137-line read spec); 00.1_Step_MINUS-1_Input_Contract.md — not reached — none

---
---

# PART 2 — STEP 0 OUTPUT

---

## 0.1 — THE FRAME DECLARATION BLOCK

```
## Frame Declaration

**Location:**        Davis — Mirny Arcanet subnet, Federation of Tepenia
                     (Vestfold Hills, Ingrid Christensen Coast, Prydz Bay; ~68°35'S, 77°58'E)

**Type:**            SETTLEMENT (primary)  +  RESETTLED (modifier, scope-narrowed — see note A)
                     Installation CONSIDERED AND DECLINED (see note B).
                     Enclosed · Orbital/extraplanetary · Mobile · Ruined/abandoned · Contested ·
                     Seasonal/rotational · Restricted/sacred — all considered, NONE assigned (note C).

**Population band:** BAND 5 (Regional), approx. 1,158,314
                     RULED by DR-4: Census I governs ("the maximum size per city that each city needs
                     to accommodate"). Not re-litigated.
                     `01` §2.2's two MUSTs are DEFERRED BY RULING, NOT MISSED:
                       - threshold 3->4, mandatory decomposition into sub-locations  -> DEFERRED
                       - threshold 4->5, distributional analysis (spread, modes)     -> DEFERRED
                     This pass writes base-level fundamental facts AT a declared Band 5 WITHOUT
                     performing Band 5 distributional analysis. Suspended, not cancelled.

**Extent band:**     UNDETERMINED AT STEP 0 — a BLOCKED CHECK, not an absence. See note D.
                     Direction of divergence from the population band is ALSO unknown, so no
                     divergence finding can be written yet. Filed as REQUESTED-A1.

**Status:**          LIVING
                     Explicitly NOT `Declining`. `01` §3's 2026-08-31 note governs: the Census I -> II
                     drop is migration to a documented destination inside the setting's own future
                     (the orbital tier, opening ~2688), not loss. Two independent sources agree —
                     the census's own "nobody was born or died in the transition; they relocated",
                     and the Second Interwar README recording the Census I -> II boundary as
                     "pre-war migration to orbit, not loss".
                     STATED IN PROSE, as §3 requires: between the two snapshots Davis's combined
                     population falls 1,158,314 -> 781,596 (-376,718). Within that, robots
                     594,715 -> 344,173 (-250,542) and humans 563,599 -> 437,423 (-126,176).
                     See note E — the frame is 248 years long and one Status word compresses it.

**Temporal frame:**  THE SECOND INTERWAR PERIOD, 2564–2812 (248 years).
                     DECLARED AS THE DEFAULT, EXPLICITLY, per `01` §4.1 rule 4 — an undeclared
                     default is indistinguishable from an accidental one.
                     Relationship to adjacent eras: the Falkland Treaty (21 June 2564) is
                     simultaneously the END of the First Interwar Period and this frame's Opening
                     Image — the same event serves as both bookends. The Long Night War (2812)
                     closes the frame and is NOT AN INPUT.
                     POST-WAR FIELDS EXCLUDED BY RULE, THEIR ABSENCE NEVER A GAP:
                     `Status:` · `Current Status / Destruction` · `Connection to Concordia` · `Legacy`.
                     EPISTEMIC HORIZON (the frame's real work): residents know the Arcanet as
                     functioning, Amundsen Tower as completed (~2688) and operating, and the
                     orbital tier as open and as a lived destination their neighbors took. The Long
                     Night War and the Planetary Split Brain have not happened and cannot be
                     imagined by anyone here.
                     ACT: the frame spans both and is MOSTLY ACT 2 (~200 of 248 years). Default Act
                     for any culture question is ACT 2 — people are Tepenian, origin is ancestry.
                     Davis's founding-era content sits in ACT 1 and must be classified there.

**Parent:**          The MIRNY Arcanet subnet, within the Federation of Tepenia.
                     UNWRITTEN — no ULM pass of its own. `01` §5.2 protocol runs; see 0.6.

**Children:**        NONE WRITTEN. Decomposition into sub-locations is MANDATORY at this band
                     (`01` §2.2, threshold 3->4) and is DEFERRED BY RULING (DR-4).
                     CONSEQUENCE, STATED BECAUSE IT IS NOT OBVIOUS: `01` §5.4 gives a Band 4+ pass
                     three dispositions per category — Uniform / Patterned / Delegated. With no
                     sub-location passes in existence, `Delegated` HAS NOWHERE TO GO. A category
                     that genuinely belongs to sub-locations must be recorded as DEFERRED, never
                     answered `Uniform` — and §5.4's own warning is that "a Band 4+ pass that
                     answers everything as Uniform has not been written at its own scale."
                     The deferral therefore creates active pressure toward the exact failure §5.4
                     names. Flagged as a standing hazard for every later phase.

**Sibling set:**     EXISTS, AND IS UNUSABLE AS A COMPARISON INSTRUMENT — twice over:
                       (1) ONE LOCATION, ON ITS OWN TERMS forbids comparing Davis to any other city;
                       (2) warm mode closes other cities' CONCLUSIONS until Step 6, and the
                           differentiation table is WRITE-ONLY in-run (add Davis's column, never
                           read another's).
                     Roster known from the admissible set, PARTIAL and not known to be complete:
                     Mirny (subnet hub) · Casey · Zhongshan · Sinheung. Recorded to fill this line
                     only. Nothing may be built on the roster's members or its completeness.
                     EFFECTIVE PATH: `01` §5.3a — the default, one location, no comparison set.
                     SUBSTITUTES USED (named, because "an unstated substitute reads to a later
                     reader as an un-run check", and because Run_Modes §4 requires all four):
                       1. OWN EARLIER STATES — AVAILABLE AND STRONG. Three in-frame states:
                          founding 2564 / Tower completion + orbital tier opening ~2688 / late
                          frame -> 2812. `01` §5.3a's 2026-08-31 caution CHECKED: all three states
                          fall INSIDE the declared frame, so this is a genuine three-state axis and
                          not a two-state one reaching across a boundary. Candidate axis, nominated
                          not adopted: WHO LIVES HERE — robot-majority at Census I (594,715 of
                          1,158,314 = 51.34%) inverting to human-majority at Census II (437,423 of
                          781,596 = 55.97%). Measured, in-frame, needs no second city.
                       2. NEAREST ANALOGOUS LOCATION AT A DIFFERENT SCALE — PARTIALLY AVAILABLE.
                          The non-peer scales are Davis against its own parent subnet and against
                          the Federation. The parent is unwritten, which weakens it. Recorded as
                          partial rather than claimed.
                       3. REAL-WORLD COMPARABLES (RWBEM) — LEGAL AND EXPLICITLY PRESERVED (the
                          input contract keeps L60's "one of the largest ice-free coastal oasis
                          areas in Antarctica" on exactly this ground). AVAILABLE IN PRINCIPLE,
                          UNBUILT IN FACT: no `Davis_Research_Log.md` exists (verified, 0.3(f)).
                          Becomes real at Step 3, not before.
                       4. GENERATOR-CONFLICT METHOD (`02` §5) — AVAILABLE, needs no comparison set,
                          and already has material: the G3 tension (residents understanding
                          themselves as researchers while the polity above them requires calories).

**Written:**         ALONE (default). No co-write. The mirrored-pair permission (`01` §5.3b) is NOT
                     invoked and there is no basis for it — and invoking it would require reading a
                     sibling, which both governing laws forbid.

**Configuration:**   EXCEPTIONAL — in exactly one way, and it is not the usual one:
                     THIS PASS DECLARES BAND 5 WHILE BOTH OF BAND 5'S MANDATORY OBLIGATIONS ARE
                     SUSPENDED BY DEVELOPER RULING (DR-4). `01` §2.2 states both as MUSTs. A pass
                     that declares a band and does not run that band's machinery is not running the
                     standard instrument, and a later reader needs to know which techniques transfer.
                     FINDINGS THAT WILL DEPEND ON THE EXCEPTIONAL PROPERTY (listed now, per the
                     block's own requirement):
                       - any claim of the form "what Davis is like" that reads as a SINGLE answer
                         rather than a spread. At a true Band 5 pass that is the scale error named
                         in `00c` Gate 11 and `00d`; here it is a PERMITTED consequence of the
                         deferral and must be TAGGED as such, never defended on the merits;
                       - any category answered `Uniform` under §5.4, because `Delegated` is
                         unavailable (see Children);
                       - the G8 composition readings, which are the most distribution-shaped
                         material available and are precisely what a Band 5 analysis would consume.
                     CONTESTABLE — I flag my own call: a second reader could reasonably declare
                     TYPICAL on the grounds that DR-4 is corpus-wide rather than Davis-specific,
                     and that a ruling applied to all 38 cities IS the new typical. I chose
                     EXCEPTIONAL because the deferral changes which techniques transfer, and `00f`
                     §7's logic — "a pass cannot correct for a bias it has not declared" — favors
                     declaring. This is one of my two genuinely contested calls.

**Run mode:**        WARM
**Other cities:**    CLOSED until Step 6   [warm default]
**Own culture material read at:**  NOT YET READ. Opens at Step 0.4 item 6 / Step 5, as a CHECK.
                     Neither `Local_Cultures/Mirny_Subnet/Davis.md` nor
                     `Local_Robot_Culture/Mirny_Subnet/Davis.md` was opened by me at any point.
**If COLD:**         n/a. Declared WARM explicitly, per Run_Modes §5 — "a warm run is honest; a
                     'semi-cold' run is a warm run wearing a cold run's credibility." There is no
                     third mode.

**Provisional assumptions about the parent:**  PA-1 .. PA-6 — see 0.6 in full.

**Generators available:** G1 present-but-LOPSIDED (does NOT count) · G2 present · G3 present ·
                     G4 present · G5 present-volume-missing · G6 ABSENT (recorded null, and see
                     0.3(e) — its ground is unsafe) · G7 designation-yes-research-unbuilt ·
                     G8 present. SIX COUNTABLE against a threshold of three.
**Generators selected:** G2 (physical & environmental) · G8 (demographic composition) ·
                     G4 (founding condition) — as the three primaries.
                     G2 first because it is quantitative, verified, and is the thing that cannot be
                     retconned (`01` §5.2 rule 3: "the ice sheet will not be retconned").
                     G8 because it is the richest and carries the measured majority inversion.
                     G4 because the input contract calls it "the sharpest single input this
                     location supplies", and it is stated rather than inferred.
                     CARRIED, WITH THEIR LIMITS STATED: G3 (fourth, and fragile — the whole of it
                     is one line, L143, which is this pass's own biggest doubt) · G5 (direction
                     yes, volume never stated -> REQUESTED) · G7 (unbuilt until Step 3) ·
                     G1 (corroboration-tier, never an independent generator, read LAST as a check,
                     Element half RESERVED under DR-1).
**Reserved decisions this pass must not foreclose:** six — see 0.5 in full.
```

### Note A — why RESETTLED is assigned, and how far

`01` §1.2 flags this modifier as "commonly assigned and systematically under-used — check every location
carrying it." Davis carries it on admitted canon: a second population inhabiting what an earlier one left.
**Its obligatory question — *what did the second population inherit, misread, or fail to notice about the
first?* — is answerable here ONLY in the de-nationalized form Spec L127 already supplies:** they inherited
**a written record without a teacher.** Preserved journals, logs and orientation manuals gave a real
documentary starting point; no living environmental knowledge survived, and learning from a written record
is not the same as being taught by a living institution.

**The guard, written next to the assignment because this modifier is the single likeliest route to a GPS
violation in later phases:** the modifier's own question invites asking about "the first population," and the
first population is the forbidden object. The GPS law blocks *whose* the site was, *why* it emptied, and its
lineage, abandonment and vacancy. It does **not** block *that documents were present and knowledge was not* —
that is a fact about the Tepenian community's founding condition, which is what L127 states.

**The "misread" half is live and is the richest thing the modifier offers**, and it is recoverable from
physical fact rather than from provenance: a community learning terrain from manuals rather than from people
will misread specific things, and Davis's physical inventory says which things are misreadable — which lakes
are hypersaline and which are landlocked marine basins, where fjord ice is safe, what a 24h-to-0h light
budget does to a growing season.

**CONTESTABLE — my second flagged call.** A reader could decline RESETTLED on the grounds that its question
cannot be asked without reaching for the forbidden first population. I assigned it because declining would
suppress L127, an explicitly KEPT Tier 1 input, and because the recorded failure mode for this modifier is
under-use, not over-assignment.

### Note B — why the Settlement + Installation dual assignment is DECLINED (a killed finding, recorded)

`01` §1.1 states the pattern outright: *"Anywhere founded as an installation and now inhabited as a home
carries `Settlement + Installation`* … **Expect this doubling wherever a setting's history includes
purpose-built outposts that outlived their purpose."** Davis looks like a textbook case and I reached for it
first.

**I killed it.** The only route to `Installation` runs through the real site's prior function as a staffed
research station with a controlling institution — and that is precisely the real site's lineage, which the GPS
law covers, and which this project has already recorded itself walking into hours after flagging it. In-frame,
from the first day of the Tepenian Davis, the arrivals were exiles making a home, not staff belonging to an
institution. L127 says so directly: they had paper, not an institution.

**So the doubling `01` §1.1 tells me to expect is exactly the doubling this setting's GPS law removes.** That
is worth recording as a structural point rather than a one-off: the ULM's own Installation-expectation rule
and this universe's GPS law point in opposite directions for every Tepenian city founded on a real station
site, which is most of them. Recorded, not resolved — I am not authorized to fix it.

### Note C — the six unassigned modifiers, each with its reason (NO FORCED FIT)

| Modifier | Call | Reason |
|---|---|---|
| **Enclosed** | NOT ASSIGNED | Nothing in the admissible set establishes a sealed, domed or pressurized envelope at Davis. The Robot Physiology 2026-09-06 ruling pushes actively the other way — clothing is ordinary and near-universal, exposure is a preparation problem and not a species-level gate, "a robot can realistically remain standing still in most of the country." Davis's own figures are consistent with an open city: mean -10.0 °C, out of the katabatic regime at ~5.6 m/s, record high +13.0 °C, and ~400 km² of exposed ice-free ground. **"No envelope is established for Davis in the admissible set" must never read as "Davis has no envelope."** Note the interaction: had Enclosed been assigned it would have forced the disposal-of-the-dead question, which is RESERVED — see 0.5 item 4. |
| **Orbital / extraplanetary** | NOT ASSIGNED | Davis is a surface city. **But its second standing question survives its modifier**, because Davis is the *departure* end of a documented orbital relationship: *what is the return trip, and who never takes it?* inverts here into **who left, and who did not come back?** — 376,718 people, disproportionately robots. I flag this as MY OWN EXTENSION, not an assignment and not a criterion `01` states; Step 1 may adopt or discard it. |
| **Mobile** | NOT ASSIGNED | Davis does not move. |
| **Ruined / abandoned** | NOT ASSIGNED | POST-WAR by rule. In-frame, for all 248 years, Davis is a living operating city. Its absence is never a gap. |
| **Contested** | NOT ASSIGNED | Nothing in the admissible set establishes two competing accounts of the place. |
| **Seasonal / rotational** | NOT ASSIGNED | Nothing establishes a seasonal or rotational population; Davis has permanent residents in the millions-fraction. The real station's summer/winter crew rotation is GPS material and inadmissible as a cause. **KEPT SEPARATE, because conflating them is easy:** Davis *does* have a severe annual light cycle — a 37-day polar night (~Jun 4 → Jul 10) and a 55-day midnight sun (~Nov 25 → Jan 18). That is a `Determined` physical constraint that will bear hard on an agricultural city. It is not the Seasonal modifier, which asks *which population is the subject*. |
| **Restricted / sacred** | NOT ASSIGNED | Settled on Davis's own internal ground: its census carries 437,423–563,599 humans, so human presence is not restricted here. (The Robot Physiology file names Kunlun and Dome Fuji as the human-forbidden locations; I note it only to confirm the roster is closed and elsewhere — the internal census figure settles it without reference to anywhere.) |

### Note D — why the extent band cannot be declared, stated as a problem rather than filled

`01` §6's block requires an `Extent band: <0-6>` and §2 requires two numbers, not one. **I cannot supply it
honestly, for two independent reasons, and I am naming the problem rather than widening the set:**

1. **`01` §2.1 supplies no extent ruler.** Its band table has exactly one axis, and that axis is *population*
   ("Band | Population | What the unit of analysis is | …"). There is no definition anywhere in `01` of what
   makes an extent Band 3 versus Band 5. The file asks for a number on a scale it never defines.
2. **The canon file that would settle Davis's extent is not in this pass's Step 0 reading list.**
   `Extent_and_Density_Per_City.md` is named in RWBEM's Step D read list as tier-1 **HARD CANON** that
   "outranks everything below it, including the pass." It is not among my 15 files. I did not open it and did
   not guess from it.

**What I have is not an extent.** ~400 km² is the *Vestfold Hills ice-free oasis*, a geographic feature, not a
declared city footprint. Equating the two would assume the city fills the oasis and extends no further — which
is exactly the derivation `01` §2 forbids, and is a cousin of the recorded error that area-derived figures
cannot anchor extent work. **And I am forbidden to derive extent from density**, which is the other tempting
route.

**Result: UNDETERMINED — a blocked check, not an absence.** RWBEM's own rule governs the recording: *"a blocked
check is not an absence."* Note that even the *direction* of divergence from the population band is unknown, so
`01` §2's "when they diverge, the divergence is characterizing" cannot be run either way. Filed as
**REQUESTED-A1**: read `Extent_and_Density_Per_City.md` at Step 1 and declare extent there.

### Note E — one Status word compresses a 248-year frame

`01` §3's taxonomy assigns one status. The frame is 248 years and demonstrably contains at least two regimes:
a founding and build-out period from 2564, and a period from ~2688 with a large documented outflow to orbit.
A single `Living` is correct per §3's own migration note, and it is also a compression. **I record the
compression rather than inventing a compound status** — §3 explicitly says the taxonomy "does not need, and
should not invent, a dedicated status value for every possible cause of population change."

The compression is not a loss, because §5.3a's own-eras instrument is precisely the tool for it, and I have
verified above that all three of its states sit inside the frame.

---

## 0.2 — THE DISCIPLINES: what each obliges THIS pass to do, at Band 5

**1. `Disciplines/00b_General_Population_Discipline.md`**
At 1,158,314 people the gap between a vivid narrow answer and the general answer is a million people wide, so
every category must state what the **majority** does before any signature instance is named. Two concrete
obligations here. **(a)** L143 calls Davis "Tepenia's breadbasket and a prime ecological/limnological research
hub" and says these "make up the clear majority of daily activity" — the pass must not let *researchers* stand
in for the population, because a breadbasket's general population is agricultural labor, greenhouse work,
handling, storage and logistics, not laboratory science. **(b)** `00b`'s second axis — a narrow OBJECT standing
in for a whole SECTOR — binds directly, and **its test is arithmetic, which is the only faculty that did not
produce the error**: multiply any sector share by 1,158,314 and ask whether that headcount plausibly does that
work. "Limnological research" at a large share is hundreds of thousands of people studying lakes. The recorded
correction says the fix is to **widen the sector's definition**, never to shrink the percentage.

**2. `Disciplines/00d_Shadow_Proportion_Discipline.md`**
Obliges: the overwhelming majority of Davis, day to day, is people doing what they believe is right inside a
culture that mostly delivers on its promises — write that as the reality, because it is the reality. Any shadow
must be unintended, unnoticed in-world, and discoverable rather than announced. At Band 5 the file's own
2026-08-29 correction binds hardest: **do not scale one person's or one institution's behavior into a civic
sanction across a million people.** Concretely, before writing any exclusion-shaped penalty the pass must ask
what it physically costs the excluded person *at Davis* — and **Davis's own physical facts give a different
answer from the recorded worked case, so that case's reasoning must not be carried across**: at a -10.0 °C
mean, out of the katabatic regime, with a +13.0 °C record high and ~400 km² of walkable ice-free ground, and
with clothing established as ordinary and near-universal, outside at Davis is survivable with preparation. The
"outside is lethal, therefore no exclusion" chain does **not** transfer. The question must be asked fresh.
And per `00f` §4d discipline 1: never ask *whether* Davis has a shadow — ask **how** it manifests.

**3. `Disciplines/00f_Review_Panel.md`**
Obliges, at Step 7: cast the six Flat Archetypes concretely for a city of this size, always add the
Passer-Through and the Neighbor, always run the Lover faculty's question ("is this place alive, and could
anyone love it?") because no other gate asks it. Two Band-5 specifics. **(a)** Casting must be sized to
1,158,314 — "the Ruler" is an office and a flow, not one quartermaster — and the four-corner check must confirm
the objections came from genuinely different directions rather than being one objection wearing three hats.
**(b)** Use all **six** dispositions and keep `unmet` (the place knowingly protects this) strictly distinct from
`declined` (the pass refuses on anti-homogenization grounds and nobody here has noticed there is anything to
defend); collapsing them destroys the self-knowledge signal a low `unmet` count is supposed to carry.
**Standing correction this pass must apply:** `00f` §7 Rule 3 states its test in the sibling form — *"would
satisfying this make the district more like the other twelve?"* — which is **illegal for a city** under ONE
LOCATION. The peer-free form governs instead: ***"would satisfying this objection replace something SPECIFIC TO
THIS PLACE with something that could be true anywhere?"*** The pass must use the peer-free form and say that it
did. `00f` itself does not carry that substitution; it is a district-era file.

**4. `Disciplines/Cultural_Synthesis_Techniques.md`**
Obliges: the techniques are questions with a structure, never results to reproduce; **nulls are expected and
must be recorded rather than filled**, and a place where every technique fires is a place someone has
over-written. Band 5 specifics. Technique **14 (Population Share Check)** runs ON every finding in the pass and
needs no source of its own. Technique **18 (The Composition Merge)** has its **full input contract satisfied** —
Davis has an origin roster WITH shares, 21 nations, shares summing to exactly 100.00% (verified, 0.3(a)) — so
R1 through R6 all run and none needs to degrade. **Guard 5 fires hard and must keep firing:** Spec L54 states
the robot figures apply the *same* national proportions as the human population, so the robot/human split
carries **zero independent national signal**; mining that axis yields an artifact of the method, not a fact
about Davis. Technique **13 (Unused-Tier Mine)** is in its "before a pass" state — no research log exists
(verified) — so "all picks unused, maximum yield" is the safe default and Step 3 must build the log. Techniques
**12 (Native Before Transplanted)** and **15 (Borrowed Form)** depend on the GPS unlock, and **composition IS
established for Davis**, so origin-ethnicities are admissible material from here on; refusing them wholesale
would be a misreading that kills two techniques and produces a placeless city.

**5. `Disciplines/Real-World_Basis_Extrapolation_Method.md`**
Obliges LAW 0-R, which is stricter than LAW 0 alone: **a pick is not exhausted because it has been searched
once.** Do not stop at the first useful return; query every pick from more than one angle; a pick with a
sub-part is at least two picks; **go back to picks already logged as covered**; run and log near-duplicates; log
dead ends and whether each died at the query or at the sources; never assert redundancy from a title. There is
no search budget. Concretely for Davis: G7's designation exists and **its research is unbuilt — no
`Davis_Research_Log.md` (verified ABSENT)** — so Step 3 must create it and record exact verbatim search
strings, sources with links, a fact-by-fact table of what came back → which finding it became, withheld versus
omitted, divergences from source, and open threads. And the standing GPS principle binds at Step B: **what
stays fully usable is pure physical and geographic fact** — terrain, climate, materials, dimensions,
constraints. For Davis that is a large usable surface (Vestfold Hills terrain, Prydz Bay, the hypersaline lakes
and landlocked marine basins) and a firmly forbidden one (who operated the station, its custody chain, and the
figure the city is named after).

**6. `Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` (governing, universe-wide)**
Robots are the **majority** at the governing census — 594,715 of 1,158,314 = **51.34%** — so there is no phase
here that is not a question about them. Obligations: **(a)** never write a robot gated out of Davis's cold by
her body; coats and gloves are ordinary, exposure is preparation, and the insulation-versus-dexterity trade-off
is a real gradient on what outdoor work a given climate permits — which matters directly for an agricultural
city. **(b)** Robots require downtime and overnight recharging, which gives Tepenia a **shared night**; Davis's
37-day polar night and 55-day midnight sun therefore fall on a population that is *all* resting together.
**(c)** Leisure is a condition of remaining sane, not a perk, and in Tepenia it is a fact of life owed to
nobody — so a breadbasket's labor demands may never be written as robots working continuously. **(d)** Siligel
is **energy replenishment first**, maintenance and repair second; coolant is the drink category; glitch-coolant
varies city to city on a variety-versus-potency axis — and **Davis is not placed on that axis in the file.
NO FORCED FIT: do not place it to fill the slot.** **(e)** Disposal of the dead is RESERVED, and the file's own
human-side mortuary question is **expressly deferred by the developer**; the pass must not resolve it from one
city. **(f)** The Acts ruling applies to robots exactly as to humans, and *when* a robot was built matters as
much as *where* — a robot built early in the era and one built late are not carrying the same culture even in
the same city, and the transmission channel is the **community**, not the fabrication.

---

## 0.3 — GATE 0 · RAW EVIDENCE, NOT SUMMARIZED

> Gate 0 fails in **both** directions — overclaiming completion **and** understating a finished piece. Below:
> what I checked, and the raw output. Self-audit error in this project has run in one direction on every
> occasion measured, so I ran the arithmetic independently rather than reading the contract's assertions.

### (a) The input contract's §3.3 and §8 census claims — **CONFIRMED, exactly**

Claim under test (§3.3): *"Hand-verified: all four per-nation columns sum exactly to their totals; shares sum
to 100.00%; worst row deviation 0.57 of a person."* I re-entered all 21 rows from Spec L32–L52 and summed.

```
rows: 21
share sum      : 100.0
C1 Robots sum  : 594715  stated 594715  delta 0
C1 Humans sum  : 563599  stated 563599  delta 0
C2 Robots sum  : 344173  stated 344173  delta 0
C2 Humans sum  : 437423  stated 437423  delta 0

C1 total 563599+594715 = 1158314 stated 1158314
C2 total 437423+344173 = 781596 stated 781596

retained combined %: 67.48
retained humans   %: 77.61
retained robots   %: 57.87
spread pp         : 19.74
robot loss        : 250542  human loss: 126176  total loss: 376718
```

**All four column sums exact. Shares exactly 100.00. Every derived percentage in §3.3 reproduces.** The
majority inversion is real and is arithmetic, not interpretation: robots are 51.34% at Census I and 44.03% at
Census II.

### (b) Climate internal consistency — **CONFIRMED**

```
precip sum: 72.8 stated 72.8
mean of means: -10.0333 stated -10.0  delta 0.033
```

Monthly precipitation sums **exactly** to the stated 72.8 mm/yr annual. Mean of the twelve monthly means
reproduces the stated -10.0 °C to **0.033 °C**, matching §8's claim of "0.03 °C."

### (c) `R-7` (retention percentage) — **DEFECT INDEPENDENTLY CONFIRMED**

```
R-7: lands/falls = 28/72.8 = 38.46 %   (L85 states ~45%)
     28/73          = 38.36 %
     falls-lost = 72.8-45 = 27.8  ~ lands 28 -> the 45 is MM LOST, reused as a percent
```

L85 states "~28 mm/yr *(~45% retention)*". 28 of 72.8 is **38.46%**, not 45%. The 45 is L86's **millimeters
lost**, reused as a percentage. The contract's diagnosis is right and its computed 38.5% reproduces.
**Unresolvable in-pass; it is a source defect, and I have not edited anything.**

### (d) `R-3` (temperature range on two columns) — **DEFECT INDEPENDENTLY CONFIRMED**

```
R-3: L74 says coldest months avg -21 / warmest month avg 0
     Avg Low  Jul -20.6  Aug -20.8   -> cold end sits on the AVG LOW column
     Mean     Dec  +0.0  Jan  +0.9   -> warm end sits on the MEAN column
     Avg High Jan  +3.2              -> the avg-high counterpart the cold end implies
```

L111's own column provenance defines the temperature range as "mean daily minimum to mean daily maximum."
L74's cold end honors that (Avg Low); its warm end does not (it is a Mean). The avg-high counterpart is
**+3.2 °C**. **This matters for a breadbasket**, because the growing-season ceiling is the number in question.

### (e) `G6` / `REQ-G6` — **GATE 0 FAILS IN THE OVERCLAIMING DIRECTION. A null was recorded on a ground that does not establish it.**

The contract's G6 row and `REQ-G6` both rest on a single stated ground: *"`World_History_Reference.md` = **0**
matches."* **The filename is given without a path, and there are two files with that name.** Count-only check
(`grep -c`, `wc` — never `-n`/`-o`, per `M-223`):

```
--- GDD copy ---
lines: 7
bytes: 467
davis matches: 0

--- universe repo copies (count only) ---
/home/kuroskalacs/.../TepenianUniverseTimeline/Reference/World_History_Reference.md | lines: 346 | davis matches: 1
```

**The GDD's own `Worldspace/World_History_Reference.md` is a 7-line, 467-byte stub.** A zero match out of seven
lines is nearly uninformative. **The universe repo's copy is 346 lines and returns 1 match.**

**This is `M-117`'s own shape — "a name is not an address" — landing on the evidence for a recorded absence.**
I have **not** opened the matching line: that would be content outside my contract and is conclusion-tier risk.
**I record the counts and refuse the adjudication.** The G6 null is not disproved; it is **unsupported by the
ground given**, and Step 1 must re-ground it against the 346-line file before the null stands.
This is my strongest Gate 0 finding.

### (f) `REQ-G7r` (no Davis research log) — **CONFIRMED** (boolean check only, no content read)

```
ABSENT: Worldspace/.../Cities/Research_Logs/Davis_Research_Log.md
```

The claim is true. G7's research half is genuinely unbuilt, `Cultural_Synthesis_Techniques` technique 13 is in
its "all picks unused" state, and `01` §5.3a substitute 3 is available in principle but unbuilt in fact.

### (g) Cited evidence files exist; and nothing is understated — **CONFIRMED both directions**

```
00.0_Pre-Trip_Inspection.md
00.1a_RULING_Vision_Notes_and_Specs_L135-181.md
00.1b_T8_Rounds_Step_MINUS-1.md
00.1_Step_MINUS-1_Input_Contract.md
00.1_SUPERSEDED_single-reader_2026-09-11.md
README.md
```

All three files the contract's header cites as evidence exist (`00.1a`, `00.1b`, the superseded single-reader
version). **And no `00_Frame.md` exists** — so Step 0 is genuinely unwritten and nothing claimed open is in
fact finished. Gate 0's understating direction: clean.

### (h) `R-9` (stale pointer) — **CONFIRMED by my own read boundary**

The contract corrects the `S01` card's pointer from L2350–2375 to **L2390–2414** for Step −1. My own admissible
read begins at **L2416** and its first line is `# Step 0 — Frame`. Step −1 must therefore end at or before
L2415, which is consistent with L2390–2414 and inconsistent with L2350–2375. **Independent corroboration.**

### (i) The read spec itself — **CONFIRMED, mechanically**

```
read spec        : 1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179
expanded count   : 137  distinct: 137
duplicates       : 0
struck {4,9,88,89,121} present in spec? -> NONE
bound 1-134 size : 134   minus struck -> 129
extras beyond 134: [143, 148, 153, 154, 155, 176, 178, 179]  count: 8
129 + 8 = 137
spec == (1-134 minus struck) UNION extras ? True

bound as a raw span 1-134 plus 8 extras = 142 -> the 142 figure the contract warns against
```

The numeric read spec expands to **exactly 137 distinct lines, contains zero struck lines, and equals
(1–134 minus {4,9,88,89,121}) united with the eight named extras.** The contract's `M-224` standing rule —
publish the strike-excluded numeric spec, never the prose — worked: I executed the spec and read no struck line.

### (j) The contract's own self-correction at §2.2 (the L9 citation) — **CONFIRMED SOUND**

The contract flags that a Tier 0 blocking input (Parent) had been half-sourced to L9, a line the same document
strikes as NULL/OPEN. I verified the replacement independently: **Spec L5 names the Mirny subnet, census L496
lists Davis under Mirny, and census L613 lists Davis under Mirny.** Three independent carriers. The correction
is sound and no harm propagated.

### (k) Open-questions reconciliation — items I could NOT check, stated rather than routed around

| Item | Status |
|---|---|
| `R-5` ratification-by-banner for `City_Symbolic_Substrate/` | **NOT CHECKED.** Outside my 15-file contract; I did not widen the set. Does not block — G1 is corroboration-tier either way. |
| `R-8` (`L111` names a superseded column set) | **NOT CHECKED.** Would require opening the referenced climate reference file, outside contract. |
| `R-1` (the 9 reconstructed vision notes) | **NOT CHECKED** — and `City_Vision_Notes/` is struck corpus-wide, so I must not open it to check. Developer-gated. |
| `REQ-G5v` (Hwy 110 throughput) | **CONFIRMED ABSENT from my admissible set.** L7 gives direction and ordering; L148 and L155 give the maritime entry. No volume figure appears anywhere in the 137 admitted lines. |
| SENSITIVITY 1 (`16_Per_City_Three_Tier_Run.md` encoding the current or superseded Division of Industry) | **NOT CHECKED — deliberately.** The contract marks `16` as `QUERYABLE-BY-SCHEMA` with an explicit prohibition on grepping by the subject's name, and it is outside my contract. Correctly left for Phase 1. |

---

## 0.4 — THE MANDATED READ ORDER, ITEM BY ITEM

`Run_Modes_Warm_and_Cold.md` §2 is the authority; `00_RUNBOOK.md` Step 0.4 restates it. **In a cold run the
quarantine physically prevents opening item 6; in a warm run nothing does. This is the single point where a
warm run can silently destroy its own value.**

| # | Item | Where it was read for this pass | Status |
|---|---|---|---|
| **1** | **specs / physical facts** | `Specs/Davis.md` at the 137-line read spec (L1–3, 5–8, 10–87, 90–120, 122–134, 143, 148, 153–155, 176, 178–179), plus the census's own geographic header at L392 | **READ IN FULL THIS ROUND**, at the bound spec, zero struck lines. Yields: position, subnet, Hwy 110, access type ON, ~400 km² Vestfold Hills oasis, -10.0 °C mean, ~5.6 m/s and out of the katabatic regime, +13.0 / -41.8 °C records, 72.8 mm falls / ~28 mm lands, 37-day polar night, 55-day midnight sun, the twelve-month table, the lake system, Prydz Bay harbor. |
| **2** | **symbol assignment** | `City_Symbol_Assignments.md` **L92** — `Earth / Earth` | **NOT READ BY ME.** It is not in my 15-file contract and I did not widen the set. It was read at Step −1 and is reported there with a column-anchored citation. Standing: Planet half RATIFIED and readable; **Element half RESERVED under `DR-1`**; the `Why` column permanently refused. G1 is corroboration-tier, does not count toward the rule of three, and is **read LAST as a check** in any case — so its absence from a Step 0 reading list is consistent rather than a gap. |
| **3** | **composition, census, and population change across snapshots** | `Official_Population_Census.md` L392–398 (tiers), L496 (Census I), L613 (Census II); `Specs/Davis.md` L15–16, L18–22, L26–54 | **READ IN FULL THIS ROUND.** Change across snapshots computed independently: 1,158,314 → 781,596; robots 594,715 → 344,173; humans 563,599 → 437,423. Majority inverts. Census I governs per `DR-4`. |
| **4** | **founding and events** | *Founding:* `Specs/Davis.md` L125–131 (L127 the GPS-purposes-only refinement, L129 the founding population, L131 the namesake). *Events, era level:* the Second Interwar `README.md` and `Timeline.md` in full. *Events, city level:* G6 recorded ABSENT at Step −1 | **READ IN FULL THIS ROUND** for founding and for era-level events. **City-level events: see 0.3(e) — the recorded null's ground is unsafe and must be re-grounded before it stands.** |
| **5** | **the sibling set's differentiation instrument, if one exists** | The 38-city differentiation table | **NOT READ — AND CORRECTLY SO.** This is a refusal by rule, not an omission. Warm mode closes "the differentiation table's other columns"; the ONE LOCATION law moves all five comparison instruments out of the per-location pass into a single terminal check on the finished corpus; and the table is **WRITE-ONLY in-run** — add Davis's column, never read another's. `01` §5.3a's four substitutes are used in its place and are named in 0.1. |
| **6** | **LAST — this location's own completed culture material** | `Local_Cultures/Mirny_Subnet/Davis.md` · `Local_Robot_Culture/Mirny_Subnet/Davis.md` | **NOT YET READ. Opens at Step 5, as a CHECK, never as an input.** Neither file was opened by me at any point in this round. A match at Step 5 is corroboration; a mismatch is a finding site. **Consulted at the start they are contamination; consulted at the end they are evidence.** |

**Two notes attached to this ordering:**

- **`06_Worked_Example_Provenance.md` was NOT checked, and it should have been.** Both `00_RUNBOOK.md`
  L2469–2470 and `Run_Modes_Warm_and_Cold.md` §2 require checking `06` for the subject **before Step 0.2, not
  after**, because required reading may carry Davis's own worked example and reading it at 0.2 violates the
  read order before the pass has begun. **`06` is not in this pass's Step 0 reading list.** I did not open it
  (I will not widen the set) and I did not verify whether it names Davis. Filed as **REQUESTED-A2**.
- **`Specs/Davis.md` L143 — an ADMITTED line — ends by pointing at read-last material:** *"Full detail in
  `Local_Cultures/Mirny_Subnet/Davis.md`."* I treated it as **DO-NOT-FOLLOW**, identically to L91's handling.
  The contract gives L91 that label explicitly and does not give it to L143. Filed as a defect.

---

## 0.5 — RESERVED DECISIONS, AND WHAT WOULD FORECLOSE THEM

> Step 0.5's own instruction: *"know you will probably find material bearing on them anyway. When you do: write
> it as a numbered finding, marked reserved."* One such finding is recorded at item 4.

**1. Proper names of people — PERMANENT. Role archetypes only.**
*Foreclosed by:* naming any individual — a founder, a first greenhouse-keeper, a harbormaster, a lake
researcher, a chamber initiator. The live pressure point is RWBEM **Step E**, which is where people-derived
material gets written down, and whose own rule is that people-derived entries stay role or archetype
placeholders. **Second, less obvious route:** naming a *practice, method, tool or institution* after a person
smuggles a name in through the back door and is harder to reverse than a character. **Third, specific to Davis:**
the spec names a real historical person at L64 and L131 as the city's namesake. That is site provenance under
G7. Building any in-world figure, honorific, holiday, civic role or founding story on it would invent a person
*and* violate GPS in the same sentence.

**2. The demonym.**
*Foreclosed by:* using any adjectival form even once, even hedged — a coined demonym in a draft will be copied
forward as canon by the next session. Write "residents of Davis," "people here," "the city's growers."
**Pressure points:** Phase 9 (Populations) and Phase 4 (Ordinary Life), where the natural English sentence wants
a demonym. **And there is a specific pull here:** the Robot Physiology file uses demonyms for other places
("a Neumayerite robot," "a Rotheran"), which establishes that Tepenian demonyms exist as a form — making the
gap at Davis feel like something to fill. It is not. It is reserved.

**3. Which DLC covers the Mirny subnet.**
*Foreclosed by:* writing anything that presumes a player's arrival, a hub location, a quest structure, a gate, a
companion sited here, or an act in which Davis becomes reachable. **`Repo_Scope.md` is directly relevant and
sharpens this:** questline and plot-branch structure and game mechanics of any kind are *out of scope for shared
canon* — "this repo holds *what happened and why*; it never holds *what a player does about it*." A location
pass that implies DLC placement is writing another document's material as well as foreclosing a reserved
decision. Keep to what the place **is**.

**4. Disposal of the dead.**
*The highest-risk of the six, because three pressures converge.* **(a)** `01` §1.2 says a sealed location "will
usually find its disposal-of-the-dead question sitting here, unanswered" — I declined the Enclosed modifier,
which lowers the pull but does not remove it. **(b)** The Robot Physiology file supplies a vivid, detailed and
recently-ruled ossuary doctrine — mixed metal and calcium in one structure, sacred and untouchable, quarrying
as the moral alternative to reclamation, the two materials keeping different time. It is **universe-level canon
whose human-side arrival-rate problem is expressly DEFERRED by the developer**, with the file itself saying
"nothing above is adopted." Writing "Davis's ossuary is at X" or "Davis does Y with its dead" would resolve a
deferred *national* question from a single city. **(c)** And Davis has a physical fact that points straight at
it.

> **RESERVED FINDING A-1 (found, stated, explicitly NOT adopted).** Davis holds ~400 km² of exposed ice-free
> rock — in a nation where burial is impossible because of permafrost, that is the substrate any non-ice
> interment or ossuary construction would physically require, and L143's 2026-07-16 reassignment moves mining
> and quarrying **away** from Davis. **What it would decide:** where, physically, a mortuary practice could sit
> at Davis, and on what material it would draw. **It is not adopted here.** Stating the constraint is legal;
> converting it into a practice is foreclosure. Handed forward.

**5. `G1`'s Element meaning (`DR-1`).**
*Foreclosed by:* reading meaning off the bare word "Earth." `02` §6.0 requires symbol definitions to be read
*from the system's own files, never from the names* — and for the Element half **that file is pulled back from
canon and under review**, so the instruction cannot be satisfied and reading the word is exactly what it
forbids. **This trap is unusually live at Davis**, because Davis's strongest physical facts — exposed rock,
soil, agriculture, a breadbasket, groundedness, stability — are precisely what a reader would intuitively call
"Earth." **Any sentence connecting Davis's agriculture or its ground to the Element forecloses a reserved
decision.** If a later finding happens to resemble the word, that is a coincidence to flag, never a finding —
and G1 is corroboration-tier and read LAST as a check in any case.

**6. Early-Federation currency, Davis's or the subnet's (`DR-3`, gated behind all 38 × 3).**
*Foreclosed by:* any sentence that prices something, names a unit, describes a wage, a harbor fee, a tariff on
Prydz Bay trade, a freight rate on Hwy 110, or "what things cost here." **Pressure points:** G5 (network
position) and every export, trade and Making phase — Davis has maritime trade at Prydz Bay and road access in
both directions, and trade prose reaches for money almost automatically. **Write flows, obligations, debts and
standards of worth without a unit.** And note the contract's own explicit permission, which is a real
affordance rather than a loophole: **what Davis *values and trades* IS recordable, and should be** — it is the
input a future currency pass will need.

---

## 0.6 — PROVISIONAL ASSUMPTIONS ABOUT THE UNWRITTEN PARENT

Parent: **the Mirny Arcanet subnet.** No ULM pass of its own. `01` §5.2's protocol runs. Each assumption is
stated explicitly, numbered, with what it rests on, how cheap it is to revise, and whether anything may be
built on it. **Governing preference, applied throughout: where a finding could be built either on a provisional
parental fact or on a local physical constraint, build it on the constraint — the ice sheet will not be
retconned.**

**PA-1. The Mirny subnet is Davis's administrative and network parent, and that membership is stable across
the frame.**
*Rests on:* Spec L5 (an explicit 2026-07-03 correction from a prior "Mawson" error), census L496, census L613 —
**three independent carriers.** *Revision cost:* very low, and effectively not provisional. **Safe to build on.**

**PA-2. The Arcanet functions at Davis across the frame — the subnet is a live network, not a nominal
grouping.**
*Rests on:* the Second Interwar `Timeline.md`'s B-story (the national subnet-by-subnet Arcanet buildout from
~2614, converging with the main plot at the ~2688 Midpoint), plus the epistemic-horizon statement that
residents know the Arcanet as functioning. *Qualification:* **provisional as to WHEN Davis specifically was
connected.** The Timeline explicitly flags an unreconciled tension — local subnet-hub construction dated much
earlier elsewhere versus the national buildout from ~2614 — and says these "may be two different, sequential
things rather than one process." **So: assume connected by ~2688; do NOT assume connected at founding.**
*Revision cost:* low. **Preference applied:** any finding about Davis's connectedness should be seated on
**Hwy 110 and the Prydz Bay harbor**, which are physical and dated to nothing, rather than on network timing.

**PA-3. The subnet is a demand-side consumer of what Davis produces, rather than a co-producer of it.**
*Rests on:* L143's second half (the polity above Davis requires calories) and L148 (logistics within the Mirny
subnet). **FLAGGED — THIS IS WHERE `01` §5.2 RULE 4 IS AT RISK.** The input contract builds the G3 tension
partly on this assumption — *a place whose residents understand themselves as researchers while the polity
above them requires calories* — and that tension is the most spine-shaped material the pass currently holds.
**Rule 4 forbids building the location's single strongest finding on a provisional assumption about an
unwritten parent.**
**Recommended remedy, and I recommend the second:** either write a minimal Mirny stub first, **or re-seat the
food obligation on Davis's own physical facts** — ~400 km² of ice-free ground in a country that mostly has
none, a maritime harbor, and a light budget swinging from 24 hours to 0 — which grounds the same tension
without any parental claim at all. *Revision cost if left as-is:* high, because a later Mirny pass could
contradict it and take the spine with it.

**PA-4. The subnet does not supply Davis with a governing institution that overrides local arrangements.**
*Rests on:* **nothing.** This is a pure assumption with no source, stated here only so that it is visible rather
than silent. *Revision cost:* low. **Nothing may be built on it.** Per §5.2 rule 5 it must be registered where
the parent's eventual pass will see it.

**PA-5. Mining and quarrying are sited at Mirny, not at Davis.**
*Rests on:* L143's explicit 2026-07-16 reassignment, developer-ratified. *Qualification:* this is a claim about
the parent subnet's internal division of labor, made by Davis's own spec, and Mirny has no pass. **But it is a
NEGATIVE claim about Davis — that Davis does not carry this role — which is the safe direction.**
**One-sentence test run:** delete every other city's name and *"Davis's division of industry is agriculture and
research, not mining"* survives intact. **Relation, not comparison. Legal.** *Revision cost:* low.

**PA-6. The sibling roster includes at least Mirny, Casey, Zhongshan and Sinheung.**
*Rests on:* Spec L5, L7, L62, L129 and a path reference in the Robot Physiology file. *Qualification:* **the
roster is NOT known to be complete from the admissible set**, and is declared partial. It exists only to fill
the block's `Sibling set:` line. **Nothing may be built on its completeness, and under ONE LOCATION nothing may
be built on its members either.**

### `01` §5.1 — the four inheritance classes, as far as Step 0 can see them

> **`M-157`: THIS INSTRUMENT IS ACT-BLIND.** The `Determined` class **widens** across the Act 1 → Act 2
> boundary — by Act 2 a shared identity is among the things the parent supplies — so `Inflected` and
> `Originated` narrow. **A classification made once has been made for an unstated date.** Every call below
> names its Act.

**DETERMINED** *(the parent or the Federation fixes it; Davis has no say)*
- **As of BOTH Acts:** latitude, and therefore the ~37-day polar night (~Jun 4 → Jul 10) and ~55-day midnight
  sun (~Nov 25 → Jan 18); the temperature regime (-10.0 °C mean, coldest-month means near -17 °C, +13.0 /
  -41.8 °C records); the precipitation budget (72.8 mm falls, ~28 mm lands); the position out of the katabatic
  regime; physical law. **These are the cheapest possible foundations and should carry the most weight.**
- **As of ACT 2 ONLY, and this is the widening `M-157` warns about:** a shared Tepenian national identity. The
  Second Interwar README is explicit — *"national identity is not a differentiator — every Tepenian is
  Tepenian"* and *"differentiate LOCALLY, converge NATIONALLY."* **As of ACT 1 this is NOT yet parent-supplied**
  — people are still "X who live in Antarctica," origin cultures fresh. The same element therefore classifies
  differently at the two ends of this one frame, and since the frame is **mostly Act 2**, Act 2 is the default
  and Act 1 must be named explicitly wherever founding-era content is written.

**INFLECTED** *(the parent supplies the form; Davis supplies its version) — the workhorse class, and
systematically under-used*
Visible candidates at Step 0, all Act 2 unless noted:
- **Glitch-coolant culture** — established as a Tepenia-wide robot institution that *varies by city* on a
  variety-versus-potency axis. National form, local version. **Davis is not placed on that axis in the file,
  and NO FORCED FIT governs: leave the slot explicitly open rather than placing it.**
- **The shared night** — overnight recharging is a national physiological fact giving Tepenia a night when
  everyone stops. **Davis's local inflection is severe and measurable: a 37-day polar night falling on a
  population that is all resting together, and a 55-day midnight sun.**
- **Leisure as a fact of life** — national, owed to nobody, and the material proof that leaving worked. What
  Davis's residents *do* with those hours is the local inflection.
- **Libraries welcoming books smuggled out of Upper Earth** — L143 states the practice at Davis **and** states
  that it is a broader Tepenian practice. **SHARED IS NOT COMPARATIVE:** a canon fact about Davis is admissible
  however many other places share it. This is a clean canon-stated Inflected instance available at Step 0 — the
  national form, performed here.

**ORIGINATED** *(exists here, comes from nowhere above)*
**STEP 0 DECLARES NONE, AND THE REASON IS STRUCTURAL RATHER THAN THIN.** `01` §5.1 defines this class as
material that *"must be differentiated against siblings"* — and the ONE LOCATION law moves every comparison
instrument out of the per-location pass into a terminal check on the finished corpus. **The test for
origination is therefore unavailable inside the pass.** A pass may nominate candidates and may say "no parent
source is known for this"; it **cannot** complete the call. Recorded in DEFECTS as a methodology tension.

**AGGREGATED** *(the parent's own character is partly the sum or the tension of its children)*
**NOT THIS PASS'S TO WRITE** — it is a claim about the Mirny subnet, and writing it would be writing the parent.
Recorded for the eventual parent pass: Davis contributes an agriculture-and-research function, ~400 km² of
ice-free ground, a Prydz Bay maritime entry and a two-way position on Hwy 110 to whatever the subnet's
Aggregated reading turns out to be. **Do not compute it here.**

### `01` §5.2 rule 4 — the explicit check

Candidate strongest findings currently available, tested against the rule:

| Candidate | Rests on | Rule 4 |
|---|---|---|
| **G4 — a documentary inheritance without a living institution** | Spec L127, admitted canon. No parental assumption. | **SAFE** |
| **G8 — the majority inversion** (robot-majority → human-majority; robots retained at 57.87%, humans at 77.61%, a 19.74 pp spread) | Two census rows plus the spec's own split. No parental assumption. | **SAFE** |
| **G3 — the researcher/calories tension** | L143 **plus PA-3**, a provisional claim about an unwritten parent. | **AT RISK — do not make this the spine unless re-seated per PA-3.** |

**Recommendation to Step 1/2: seat the spine on G4 or G8, or re-seat G3 on local physical constraint.**

### `01` §5.2 rule 5 — registration

*"An assumption recorded only in the child's file is an assumption the parent will contradict."* **No registry
location for child-assumptions is named anywhere in my admissible set.** Filed as **REQUESTED-A3**: name the
location where PA-1 … PA-6 are registered for the Mirny subnet's eventual pass to reconcile against (Gate P
in `04`).

---
---

# PART 3 — DEFECTS AND DOUBTS

> Offered in the spirit of the recording law: snags, blockages, dead ends, killed findings and
> self-corrections, not just successes. **I recorded these; I edited nothing.** Finding a defect is not
> authorization to fix it.

### D-1. **`G6`'s recorded null rests on an ambiguous filename.** *(Strongest. Evidence at 0.3(e).)*
Two files are named `World_History_Reference.md`. The GDD's own is a **7-line, 467-byte stub** returning 0
matches; the universe repo's is **346 lines** and returns **1**. The contract cites the name without a path.
**This is `M-117`'s own shape — "a name is not an address" — landing on the evidence for a recorded absence,
which is the worst place for it, because an absence is exactly the kind of claim nothing downstream re-checks.**
I did not open the matching line and did not adjudicate.

### D-2. **A live contradiction *inside the methodology* about `City_Vision_Notes/`.**
`Real-World_Basis_Extrapolation_Method.md` Step D's read list, **row 2**, directs a pass to read
`City_Vision_Notes/<City>.md` and calls it *"AUTHORIAL VISION — PRIMARY AND UPSTREAM… NEVER treat as a derived
conclusion."* **`00.1a` struck `City_Vision_Notes/` corpus-wide**, and my own brief confirms the strike. **Two
binding instructions in the same methodology give opposite orders, and the RWBEM copy has not been updated.**
This is not harmless: Step D is a *mandatory* cross-check step, so a later session following RWBEM as written
will open a struck root and will feel entirely correct doing so.

### D-3. **`01` asks for an extent band on a scale it never defines.** *(See Note D.)*
§6's declaration block and §2's "declare two numbers, not one" both require `Extent band: <0-6>`, but §2.1's
band table has exactly one axis and that axis is *population*. There is no extent ruler anywhere in the file.
Combined with `Extent_and_Density_Per_City.md` being absent from this pass's Step 0 reading list, the line is
undeclarable without either inventing a scale or guessing a number. **I did neither.**

### D-4. **`06_Worked_Example_Provenance.md` is mandated at Step 0 and is not in Step 0's reading list.**
`00_RUNBOOK.md` L2469–2470 and `Run_Modes_Warm_and_Cold.md` §2 both require checking `06` for the subject
**before 0.2**, precisely because reading it at 0.2 would violate the read order before the pass begins. It is
not among the 15 files. Not checked; not widened.

### D-5. **The founding-population contradiction — and the GPS question underneath it.**
Spec **L129**: *"Founding population: Australian exiles."* Spec/census composition: **Primary tier is China at
19.04%; Australia is Significant at 4.93%, tagged "(founding wave)."*** Two readings, and **I am not deciding
between them:**
 (a) founding wave and composition are different objects — Australians founded it, Chinese became the largest
     origin group; the census's own "(founding wave)" tag supports this;
 (b) it is a GPS leak — the real site's operator nationality reappearing as the fictional founding population.
**What makes this sharp is the adjacency:** L127 is an explicit, careful *GPS-purposes-only* refinement that
de-nationalizes the station's entire custody chain — and **L129, the very next line, names the founding
population by the operator's nationality.** This bears on G4 and G8, both Tier 1. It must not be silently
adopted in either direction: reading (a) makes Australia load-bearing for Davis's founding culture; reading (b)
strikes L129. Flagged for Step 1 / Gate 0 adjudication.

### D-6. **`DR-4` removes `Delegated` from `01` §5.4's three dispositions, creating pressure toward the exact failure §5.4 names.**
With sub-location decomposition deferred, there are no child passes to delegate to. A category that genuinely
belongs to sub-locations has nowhere to go, and the path of least resistance is to answer it `Uniform` — which
§5.4 calls the sign that "a Band 4+ pass has not been written at its own scale." **The deferral is correct and
ruled; the second-order consequence appears to be unrecorded.**

### D-7. **The ONE LOCATION law makes `01` §5.1's `Originated` class unverifiable within a pass.**
`Originated` is defined by a test — differentiation against siblings — that the law moves to a terminal check.
So a pass can nominate but never confirm an Originated element. The §5.1 table does not anticipate this and
still presents the four classes as jointly exhaustive and individually decidable ("every element of a
location's culture is exactly one of these").

### D-8. **`00f` §7 Rule 3 states its `unmet` test in the sibling form, which is illegal for a city.**
The file asks *"would satisfying this make the district more like the other twelve?"* — a district-era
formulation. For a city the peer-free form governs. `00f` is a ULM copy and does not carry the substitution;
the project's own instructions do. A pass following `00f` literally would run an illegal comparison at Gate 10.

### D-9. **`00d`'s worked exclusion reasoning does not transfer to Davis, and looks as though it should.**
The recorded case turns on *outside is lethal, therefore an exclusion-shaped sanction is a death sentence,
therefore the culture will not impose one.* **Davis's own numbers break that chain:** -10.0 °C mean, out of the
katabatic regime at ~5.6 m/s, +13.0 °C record high, ~400 km² of walkable ice-free ground — and clothing
established as ordinary, with exposure framed as preparation rather than a body gate. **Importing the
conclusion would be carrying one location's answer into another, which is the rule that binds in both run
modes.** The question has to be asked fresh here, and the answer may well differ.

### D-10. **Glitch-coolant: Davis is unplaced, and the axis invites placing it.**
The Robot Physiology file names specific cities on a bohemian-variety / working-class-potency axis and offers
the axis as a default framework so a local scene need not be invented from scratch. **Davis is not on it.**
The inviting move is to place Davis to fill the slot. **NO FORCED FIT: "none is sited here" must not read as
"none is possible here," and the slot stays explicitly open.** Flagged because the file's own framing makes
filling it feel like following instructions.

### D-11. **An admitted line points at read-last material, and is not labeled DO-NOT-FOLLOW.**
`Specs/Davis.md` **L143** ends *"Full detail in `Local_Cultures/Mirny_Subnet/Davis.md`."* The contract gives
L91 an explicit DO-NOT-FOLLOW label for exactly this shape and does not give one to L143 — even though L143 is
the single most-cited line in the whole contract and therefore the one most likely to be re-read and followed.
I treated it as DO-NOT-FOLLOW and opened nothing.

### D-12. **The census rows carry a rank-shaped index, and it changes between snapshots.**
Census I row reads `| 13 | Davis | …`; Census II row reads `| 14 | Davis | …`. **I declined to read the leading
number as a rank under ONE LOCATION** — and I note that *the index changing between the two censuses* is itself
a comparative signal (it can only move because other cities moved), which I am also declining to use. Recording
it so a later reader knows the refusal was deliberate rather than an oversight.

### D-13. **A ~70-year Act gap, which `M-157` makes consequential.**
The README puts Act 1 at "roughly the first 18% of the period" — 18% of 248 years is ~44.6, so Act 1 ends
~2609 ("early 2600s," consistent). Act 2 begins "~late 2600s / early 2700s," i.e. ~2680–2710. **That leaves
roughly 2609–2680 — about 70 years, some 28% of the era — assigned to neither Act.** The gradient is
deliberate ("an Act boundary is a consolidation, not a line crossed"), but `M-157` requires every inheritance
call to answer *as of which Act?*, and an event dated to ~2640 has no answer. Not a contradiction; an
under-specification with a live consumer.

### D-14. **Killed finding, recorded: `Settlement + Installation`.** *(Full reasoning at Note B.)*
I reached for the dual assignment on `01` §1.1's explicit instruction to *expect* it wherever a setting's
history includes purpose-built outposts that outlived their purpose, and killed it because the only route to it
runs through the real site's prior function. **The general point is worth more than the single call: `01`
§1.1's Installation-expectation and this universe's GPS law point in opposite directions for every Tepenian
city founded on a real station site — which is most of them.**

### D-15. **My two genuinely contested calls, flagged for the consensus round.**
**(a) RESETTLED assigned versus declined** (Note A). I assigned it, narrowed to L127's de-nationalized content.
A reader could reasonably decline it on the grounds that its own question cannot be asked without reaching for
the forbidden first population.
**(b) Configuration EXCEPTIONAL versus TYPICAL** (Note in 0.1). I declared EXCEPTIONAL on the two deferred
`MUST`s. A reader could reasonably declare TYPICAL on the grounds that a corpus-wide ruling applied to all 38
cities *is* the new typical. **If B and C disagree with me on either, the disagreement is the interesting
result, not the noise.**

### D-16. **Three REQUESTED items this round produces.**
- **REQUESTED-A1** — the extent band is undeclarable at Step 0 (D-3). Read `Extent_and_Density_Per_City.md`
  (tier-1 HARD CANON) at Step 1 and declare it there.
- **REQUESTED-A2** — `06_Worked_Example_Provenance.md` was not checked for Davis, and the check is mandated
  before 0.2 (D-4).
- **REQUESTED-A3** — no registry location is named for child-assumptions; PA-1 … PA-6 have nowhere to be
  registered for the Mirny subnet's eventual pass to reconcile against, as `01` §5.2 rule 5 requires.

### D-17. **Doubt I hold about my own output, stated plainly.**
`G3` — what Davis is *for* — still rests on **one line**, and that line is also the source of the developer
vision, the Division-of-Industry correction, the libraries detail and the "largest ice-free oasis" fact that
the contract preserves on L143's authority specifically. **A single line is carrying an unusual amount of this
pass.** The contract already names this as its biggest doubt and I independently arrive at the same place: I
did not find a second, independent in-frame source for Davis's purpose anywhere in my admissible set. That is a
result, not a gap I routed around — but it means the pass is one adjudication away from losing its function
statement, and it has already been adjudicated away once.


---

# ROUND 1 — READER B

# DAVIS — STEP 0 · FRAME — **T8 READER B**, independent

**Run mode: WARM.** Produced without contact with Reader A or Reader C.
**Nothing in this repository was edited.** The only write is this file.

---

# PART I — THE 15 PROOF BLOCKS

> **NOTE ON BLANK FIELDS — read before machine-checking.** Three of the required fields land on lines that are
> genuinely **empty in the source**. They are emitted as an empty value after the field label, not omitted:
> `00_RUNBOOK.md` LMID (line 2447) and LLAST (line 2479); `00b_General_Population_Discipline.md` LMID (line 131);
> `Cultural_Synthesis_Techniques.md` LMID (line 598 is non-empty, but LLAST line 1196 is empty).
> **`LINES` convention used throughout: number of newline-terminated lines, i.e. `wc -l`.** For a FULL file that
> is the file's own line count; for a ranged file it is the count of the ADMITTED SET, not of the bound.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md
LRANGE: 2416-2479
LINES: 64
L1: # Step 0 — Frame
LMID: 
LLAST: 
QUOTE: **Every line changes a later question.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md
LRANGE: FULL
LINES: 582
L1: # Frame, Typology, and Inheritance
LMID: | **Transit-only** | Who maintains it, and do they count as living here? |
LLAST: would have made visible before the writing started.
QUOTE: **Declare two numbers, not one:** the **population band** and the **extent band**.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Run_Modes_Warm_and_Cold.md
LRANGE: FULL
LINES: 177
L1: # RUN MODES — WARM and COLD, defined
LMID: > that is indistinguishable from good work, which is exactly what makes it dangerous.**
LLAST: > it is the one that produces cities.**
QUOTE: > # **THIS CITY'S OWN CULTURE MATERIAL IS READ LAST, AND READ AS A CHECK.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md
LRANGE: FULL
LINES: 261
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: 
LLAST: baseline stated beside it.
QUOTE: > ### ⭐ **THE TEST IS ARITHMETIC — the only part that does not run on the same faculty that produced the error.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md
LRANGE: FULL
LINES: 222
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: > **A district operates on its own sincere conception of what "doing good" means and what a proper community
LLAST: *secretly awful*, the proportion is wrong — regardless of how well-sourced each individual finding is.
QUOTE: The Shadow is a **byproduct**, never the operating principle.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00f_Review_Panel.md
LRANGE: FULL
LINES: 832
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: related, and affectionate,"* the origin of a place's spirituality and its *"sense of the mystic oneness and
LLAST:   now.)*
QUOTE: **Rule 1 — A position with nothing to say must say nothing.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/Cultural_Synthesis_Techniques.md
LRANGE: FULL
LINES: 1196
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: **The question.** *Which of this location's picks has nothing in the existing material actually derived from
LLAST: 
QUOTE: ⛔⛔ **THE ROSTER IS A DEMOGRAPHIC FACT. THE LOCAL CULTURE IS A DIFFERENT OBJECT. *Listed is not represented.***

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/Real-World_Basis_Extrapolation_Method.md
LRANGE: FULL
LINES: 463
L1: # ⭐⭐⭐ LAW 0-R — RESEARCH FULLY. **A PICK IS NOT EXHAUSTED BECAUSE IT HAS BEEN SEARCHED.**
LMID: ### ⭐ IT IS A SEQUENCING RULE, NOT A REPEAL — **the prohibition above is UNCHANGED**
LLAST: 3. **A real detail beats an invented one every time.**
QUOTE: > # **ONE SEARCH AGAINST A PICK ESTABLISHES THAT THE PICK EXISTS. IT DOES NOT ESTABLISH WHAT THE PICK HOLDS.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md
LRANGE: FULL
LINES: 438
L1: # Robot Physiology and Cultural Practices
LMID: ### ⭐⭐⭐ THE GRAND-TIMELINE ACTS
LLAST:   **Flagged 2026-07-09, for a possible future questline (not a religion):** during a Robot Religions development session, a "trace your own origin" concept was considered as the basis for a new religion (a reground of a ChatGPT-suggested "Cult of the Source") and set aside — the developer liked the mystery but didn't think it actually works as a religion's foundation. The mystery itself is worth keeping: a robot tracing which mark/generation their own chamber was built to, and from there discovering that the schematic's actual designer (Neumayer, credited nowhere, the same uncredited pattern as the Amundsen Tower) goes unknown to almost everyone built from their work — a solvable-in-principle, currently-forgotten origin mystery, not an abstract data-mysticism. Already has a discoverable in-game hook to build from: Calethina's own chamber (the one that built the player character) traces to the historical, now-dark Mountain Pass site. See `Factions/Robot_Religions/Cymatics_reverence/Cymatics_reverence.md`'s development history for the fuller reasoning trail.
QUOTE: Robots do not require oxygen and have no respiratory system in the human sense.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Repo_Scope.md
LRANGE: FULL
LINES: 30
L1: # Repo Scope — A Binding Law
LMID: - **Game mechanics of any kind** — stat blocks, XP/leveling systems, companion/romance gating, quest triggers, re-spec systems, ending-branch design, UI/UX, engine or asset-pipeline decisions. This is InnerTepeniaGDD's (or OuterTepenia1_GDD's) own design work, not shared canon.
LLAST: Before adding or porting content here, ask: does this tell you *when*, *where*, or *who*? If the honest answer is "it tells you *how to play/read it*" or "*what mechanically happens next*," it's out of scope — note its existence if useful for cross-reference, but don't port the content itself.
QUOTE: If a piece of content doesn't serve one of those three questions, it does not belong in this repo — it belongs in whichever individual project actually needs it.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/README.md
LRANGE: FULL
LINES: 70
L1: # The Second Interwar Period — **2564–2812**
LMID: > Amundsen Tower. Their being fully interconnected further defined their sense of national identity in who
LLAST:    environmental setting · local struggles and hardships · local goals · local sensibilities and habits.*
QUOTE: ⭐ **What differentiates is how hard a given place used that exit.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/Timeline.md
LRANGE: FULL
LINES: 562
L1: # The Second Interwar Period — Timeline (2564–2812)
LMID:   federation spirit survives without that specific person.
LLAST:   Reference.md` as beats are developed, to keep all documents consistent.
QUOTE: **~2688 (resolved 2026-08-05, ±~20yr flexibility — not locked to an exact year)**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md
LRANGE: 392-398,496,613
LINES: 9
L1: **Davis** *(Vestfold Hills, Prydz Bay — mainland coast)*
LMID: | Primary | China |
LLAST: | 14 | Davis | Mirny | 437,423 | 344,173 | **781,596** | |
QUOTE: | 13 | Davis | Mirny | 563,599 | 594,715 | **1,158,314** | *(revised 2026-07-04)* |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Davis.md
LRANGE: 1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179
LINES: 137
L1: # Davis
LMID: **Mean annual temperature:** -10.0°C  _(READER station: Davis; 1991–2020 WMO standard normal)_
LLAST: - **Relationship to Mawson (the city, different subnet)** — both named for/connected to Australian Antarctic figures, but administratively and geographically separate; worth clarifying whether any cultural connection existed despite the subnet divide
QUOTE: **Census I (Pre-Orbital Era):** 563,599 humans / 594,715 robots / **1,158,314** combined

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00.1_Step_MINUS-1_Input_Contract.md
LRANGE: FULL
LINES: 371
L1: # Davis — Step −1 · THE INPUT CONTRACT
LMID: > **L127:** *"No living environmental **knowledge** survived that chain of handoffs — but preserved journals,
LLAST: ⛔ **Step 0 — FRAME — opens next.**
QUOTE: ⭐⭐ **So in-frame — for all 248 years this pass covers — Davis is a living, operating city.**

---

COVERAGE: 00_RUNBOOK.md 2416-2479 (64 admitted) 1-64, no gaps, no overlaps · 01_Frame_Typology_and_Inheritance.md FULL 1-582, no gaps, no overlaps · Run_Modes_Warm_and_Cold.md FULL 1-177, no gaps, no overlaps · 00b_General_Population_Discipline.md FULL 1-261, no gaps, no overlaps · 00d_Shadow_Proportion_Discipline.md FULL 1-222, no gaps, no overlaps · 00f_Review_Panel.md FULL 1-832, no gaps, no overlaps · Cultural_Synthesis_Techniques.md FULL 1-1196, no gaps, no overlaps · Real-World_Basis_Extrapolation_Method.md FULL 1-463, no gaps, no overlaps · Robot_Physiology_and_Cultural_Practices.md FULL 1-438, no gaps, no overlaps · Repo_Scope.md FULL 1-30, no gaps, no overlaps · Second Interwar README.md FULL 1-70, no gaps, no overlaps · Second Interwar Timeline.md FULL 1-562, no gaps, no overlaps · Official_Population_Census.md 392-398,496,613 (9 admitted) 1-9, no gaps, no overlaps · Specs/Davis.md 1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179 (137 admitted) 1-137, no gaps, no overlaps · 00.1_Step_MINUS-1_Input_Contract.md FULL 1-371, no gaps, no overlaps

MANIFEST: mapped 15 of 15 files — 00_RUNBOOK.md (2416-2479); 01_Frame_Typology_and_Inheritance.md; Run_Modes_Warm_and_Cold.md; Disciplines/00b_General_Population_Discipline.md; Disciplines/00d_Shadow_Proportion_Discipline.md; Disciplines/00f_Review_Panel.md; Disciplines/Cultural_Synthesis_Techniques.md; Disciplines/Real-World_Basis_Extrapolation_Method.md; Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md; TepenianUniverseTimeline/Reference/Repo_Scope.md; TepenianUniverseTimeline Second Interwar README.md; TepenianUniverseTimeline Second Interwar Timeline.md; Official_Population_Census.md (392-398,496,613); Specs/Davis.md (137-line read spec); Davis/00.1_Step_MINUS-1_Input_Contract.md — not reached — none

> ⛔ **Never opened, by rule:** `Local_Cultures/Mirny_Subnet/Davis.md` · `Local_Robot_Culture/Mirny_Subnet/Davis.md`
> *(both verified to EXIST; both read LAST, at Step 5, as a CHECK)* · `City_Megasheets/Mirny_Subnet/Davis/`
> *(directory verified to exist; withheld corpus-wide)* · anything under `Test_Runs/` *(zero intake)* ·
> `City_Vision_Notes/Davis.md` *(verified to exist; struck corpus-wide by `00.1a`)* · the target of
> `Specs/Davis.md` **L91** *(DO-NOT-FOLLOW; a 37-city comparison)* · `Cross_City_Culture_Differentiation_Table.md`
> *(verified to exist by filename only; **WRITE-ONLY** in-run under the ONE LOCATION law)*.
> **`graphify` was not invoked and `graphify-out/` was not opened at any point.**

---

# PART II — STEP 0 OUTPUT

# 0.1 — THE FRAME DECLARATION BLOCK

*(Template: `01_Frame_Typology_and_Inheritance.md` §6, plus the run-mode lines from `Run_Modes_Warm_and_Cold.md` §5.)*

```
## Frame Declaration

**Location:**        Davis — Mirny Arcanet subnet, Tepenian Federation
                     ~68°35′S, 77°58′E · Vestfold Hills, Ingrid Christensen Coast, Prydz Bay

**Type:**            Settlement  +  (no modifiers assigned)
                     [primary per `01` §1.1 — people live here as their home, ~1.16M of them.
                      ZERO modifiers is a RESULT, not an unfilled slot. Per-modifier reasoning below.]

**Population band:** 5 — Regional (~1M–50M), approx. 1,158,314
                     [RULED by DR-4: Census I governs — "the maximum size per city that each city
                      needs to accommodate." NOT re-litigated. `01` §2.2's two MUSTs at 3→4 and 4→5
                      are DEFERRED BY RULING, not missed — see §"Band 5 machinery" below.]

**Extent band:**     UNDETERMINED — input not admitted. Filed as REQUESTED.
                     [`01` §2.1 defines its bands on POPULATION ONLY and supplies no extent scale;
                      `01` §2 forbids deriving extent from density. The canon extent source is not
                      in this pass's admissible set. Declaring a band here would require supplying a
                      criterion the methodology does not state. See the divergence pre-registration below.]

**Status:**          LIVING
                     [`01` §3's 2026-08-31 note applies exactly: the Census I→II fall is MIGRATION TO A
                      DOCUMENTED DESTINATION inside the setting's own future (the orbital tier), not decline.
                      "Where this applies, the correct status is still `Living`." Migration stated in prose below.]

**Temporal frame:**  The Second Interwar Period, 2564–2812 (248 years).
                     DECLARED, not defaulted-into (`01` §4.1 rule 4). This is the setting's last
                     fully-functioning era. Prior era: First Interwar (2083–2564, Upper Earth), ending at
                     the Falkland Treaty, 21 June 2564 — simultaneously this era's Opening Image.
                     Following: the Long Night War, 2812. THIS PASS SITS ENTIRELY BEFORE IT.
                     Epistemic horizon: residents know the Arcanet as functioning and the orbital tier as a
                     lived exit. The Long Night War and the Planetary Split Brain have not happened and
                     cannot be imagined by anyone here.
                     ACTS: the frame spans BOTH and is MOSTLY ACT 2 (Act 1 ≈ the first 18%).

**Parent:**          The Mirny Arcanet subnet — UNWRITTEN (no ULM pass of its own).
                     Above it: the Tepenian Federation. Provisional assumptions at §0.6.

**Children:**        NONE — BY DEFERRAL, NOT BY ABSENCE.
                     [`01` §2.2's 3→4 threshold says a location this size MUST be decomposed into
                      sub-locations. DR-4 suspends that. So `01` §5.4 cannot run as written — see the
                      re-scoping below, which preserves its discipline rather than dropping it.]

**Sibling set:**     EXISTS, and is READ-FORBIDDEN in-run.
                     [ONE LOCATION law: the differentiation table is WRITE-ONLY — add Davis's own column,
                      never read another's. Gate 6 moves to Step 7 (`Run_Modes` §4).
                      Substitutes used, per `01` §5.3a — all four declared, with their real availability:
                        1. Its own earlier states — AVAILABLE NOW, three-state, all in-frame. PRIMARY.
                        2. Nearest analogous location at another scale — THIN: the parent is unwritten.
                        3. Real-world comparables (RWBEM) — UNBUILT: no Davis research log exists. Step 3's job.
                        4. The generator-conflict method (`02` §5) — AVAILABLE, six countable generators.]

**Written:**         ALONE (default). No co-write. `01` §5.3b's permission is narrow, has been over-used
                     once, and the ONE LOCATION law forecloses it here regardless.

**Configuration:**   EXCEPTIONAL — in two specific ways:
                     (a) BAND 5 DECLARED WITH ITS BAND 5 MACHINERY DEFERRED. Every finding this pass
                         produces is produced WITHOUT the decomposition and distribution instruments
                         `01` §2.2 makes mandatory at this band.
                     (b) THE BAND IS RULED BY A SNAPSHOT THE FRAME'S LATER HALF DOES NOT DESCRIBE.
                         DR-4 fixes Census I on a CAPACITY criterion over Census II's FRAME-DESCRIPTION
                         criterion; the three T8 readers unanimously recommended Band 4 and were overridden.
                     Findings that depend on the exceptional property, so a later reader can tell which
                     technique transfers:
                       - anything asserting ONE answer where a distribution is owed;
                       - anything scaled off the 1,158,314 figure rather than off a per-sub-location figure;
                       - anything that reads as internally uniform because no sub-locations exist to vary.
                     Two further configuration facts, recorded but not grounds for the grade:
                       (c) `G1` is PRESENT but LOPSIDED and counts ZERO toward the rule of three.
                       (d) `G3` — what Davis is FOR — rests on ONE line (L143), which a prior pass deleted
                           wholesale without noticing what it cost.

**Provisional assumptions about the parent:**   PA-1 … PA-6, stated and numbered at §0.6.

**Generators available:** G1 lopsided (counts 0) · G2 physical ✅ · G3 function ✅ (one line) ·
                          G4 founding ✅ · G5 network ⚠ (direction yes, volume never stated) ·
                          G6 defining event ⛔ RECORDED NULL · G7 real-world ⚠ (designation yes,
                          research unbuilt) · G8 composition ✅ (richest).
                          Countable: SIX, against a threshold of three.
**Generators selected:**  G2 (physical) · G4 (founding) · G8 (composition) — with G3 (function) carried
                          as a fourth BECAUSE it is the fragile one and must be exercised, not leaned on.
**Reserved decisions this pass must not foreclose:** six, enumerated at §0.5.
```

```
**Run mode:**        WARM
**Other cities:**    CLOSED until Step 6   [warm default]
**Own culture material read at:**  NOT YET READ — opens at Step 5, as a CHECK (Step 0.4 item 6)
**If COLD:** n/a — this is not a cold run. No memory blackout, no reader briefs, no pre-contamination
             review, no pins, no skip ranges. Declared WARM explicitly, per §C.5:
             "A warm run is honest. A 'semi-cold' run is a warm run wearing a cold run's credibility."
```

## Why each line is what it is — the reasoning the block compresses

### Type — Settlement, and why ZERO modifiers is the honest output

`01` §1.1's Settlement question — *what is it like to be from here?* — is the right question for 1,158,314
people who live here as their home. Not `Polity` (the subnet is the administrative unit above it, not Davis).
Not `Interstitial` (that type is read from a TOTAL null across substrate-driven steps; Davis returns six
countable generators). Not `Installation` — see the killed finding below.

Every modifier in `01` §1.2 was checked against the admissible set, one at a time, and the refusals are written
as characterization rather than as blanks:

| Modifier | Assigned? | The ground |
|---|:-:|---|
| **Enclosed** | **NO** | Nothing in the admissible set gives Davis an envelope. Its whole physical profile is **open ground** — ~400 km² of ice-free exposed rock, lakes, fjord-like inlets — and the robot-physiology ruling states plainly that exposure is **preparation, not a species-level gate**. There is no envelope-failure question because there is no envelope. ⚠ **Watch item, not an assignment:** L143's *sheltered-agriculture and greenhouse cultivation* IS enclosed-volume practice at scale. If a later phase finds those envelopes governing a large share of daily working life, `Enclosed` may need revisiting as a **sector-scoped** modifier. It is not assigned on that basis now. |
| **Orbital / extraplanetary** | **NO** | Davis is a surface city. ⭐ **But one of the modifier's questions is imported on other grounds:** *"What is the return trip, and who never takes it?"* Davis is not orbital — it is a **departure point** for the orbital tier, and its own census measures who went. The question is live; the modifier is not. |
| **Mobile** | **NO** | Nothing. |
| **Ruined / abandoned** | **NO** | Post-war only, excluded by frame. Its absence is never a gap. |
| **Contested** | **NO** | Nothing in the admissible set gives two accounts of this place. |
| **Seasonal / rotational** | **NO** | The modifier asks which of two populations is the subject. Davis has one population of 1.16M, not a winter crew and a summer crew. ⭐ **The seasonality is real and sits in the LABOR CALENDAR, not in the population** — a 37-day polar night, a 55-day midnight sun, a daylight column running 0 h to 24 h, and a declared function of cultivation. That is Phase material, not a type modifier. |
| **Resettled** | **NO — and this is the hardest call in 0.1** | See below. |
| **Restricted / sacred** | **NO** | Nothing in the admissible set restricts entry to Davis. |

> ### ⛔ THE `Resettled` CALL, AND THE NAMED PROBLEM BEHIND IT
> `01` §1.2 warns that `Resettled` is *"commonly assigned and systematically under-used — check every location
> carrying it."* Davis looks like a candidate: L127 states the exiles settled **on existing infrastructure**,
> inheriting *"preserved journals, logs, and orientation manuals"* from a chain of prior operators.
>
> **It does not fit, for a reason specific to this case.** `Resettled`'s obligatory question is *what did the
> second population inherit, misread, or fail to notice about the first* — and **there was no first
> *population*.** A rotating succession of station operators is not a resident community. Worse, the only
> material that could discharge the question is the real site's operator lineage, which the GPS law excludes as
> a cause, an identity or a history.
>
> ⭐ **So Davis is not resettled. It is FIRST-SETTLED ON SECOND-HAND INFRASTRUCTURE — and `01` §1.2 has no
> entry for that.** Per the sanctioned fall-short: **the most conservative value is taken (no modifier), the
> problem is named, and the set is NOT widened by me.** The material itself loses nothing — it is already
> seated at `G4`, where the input contract puts it and where it belongs.

⭐ **And the zero is itself informative.** A Band 5 settlement carrying no modifier at all is a place whose
distinctiveness does **not** come from its envelope, its mobility, its contestation or its restriction.
It comes from **what it is for** (`G3`) and **who left** (`G8`). That is where the pass should spend itself.

### Population band — Band 5, and the cost of the deferral, stated

`DR-4` governs and is not re-litigated: **Census I, 1,158,314 → BAND 5 (Regional).** The developer's criterion
is capacity — *"the maximum size per city that each city needs to accommodate"* — and it outranks the readers'
frame-description reasoning because the methodology serves a playable world, not the reverse.

**The straddle is real and reproduces from `01` §2.1's own table:** 1,158,314 → Band 5; 781,596 → Band 4.
Davis crosses the band boundary **inside its own declared frame**. That is a stated fact of the frame, not a
contradiction to resolve.

**Band 5 machinery — DEFERRED BY RULING, declared, not missed:**

| `01` §2.2 threshold | The obligation | Status |
|---|---|---|
| **3→4** | *"a location **must** be decomposed into sub-locations"* | ⏸️ **DEFERRED** (`DR-4`) |
| **4→5** | *"the location no longer has a culture; it has a statistical shape"* | ⏸️ **DEFERRED** (`DR-4`) |

Both suspended until all 38 cities complete ULM + CST + RWBEM — *"you cannot write a distribution before you
know what is being distributed."* **Suspended, not cancelled.** This pass writes base-level fundamental facts
at a declared Band 5 **without performing Band 5 distributional analysis.**

> ### ⚠ AND THE COST, WHICH THE DEFERRAL DOES NOT REMOVE — stated so it is visible to whoever reads the result
> `01` §2.2 says in terms: ***"A Band 5 pass that reads like a Band 3 pass has committed the scale error named
> in `00c` Gate 11 and `00d`."*** **The deferral suspends the REMEDY. It does not suspend the RISK.** This pass
> has no decomposition instrument and no distributional instrument, and **no gate in the set will catch a
> Band-3-shaped answer**, because the gates confirm a pass is not *wrong* and none of them can tell you it is
> thin. This is not an objection to the ruling — it is the ruling's price, recorded at Step 0 so a later reader
> does not mistake a clean gate run for a scale-correct pass.

### Extent band — UNDETERMINED, and the divergence pre-registered rather than pre-judged

`01` §2 is explicit that two numbers must be declared and that a divergence between them is characterizing.
**I cannot supply the second number without inventing a criterion**, for three stacked reasons:

1. `01` §2.1's band table has columns for Band, **Population**, unit of analysis, and district-methodology
   assumptions. **There is no extent column and no extent scale anywhere in the file.**
2. `01` §2 forbids deriving extent from density, which closes the only arithmetic route from what I hold.
3. The canon extent source — ranked by RWBEM Step D as tier-1 **HARD CANON**, alongside the census — **is not
   in this pass's admissible input set**, and the address RWBEM gives for it does not resolve (see `G0-10`).

The one extent datum admitted is **~400 km² of ice-free exposed rock (L60)** — and that is the **geographic
setting**, not the city's built footprint. Reading a band off it would be exactly the move the instruction
forbids: supplying a criterion the instruction does not state.

⇒ **Declared UNDETERMINED and filed as REQUESTED.** ⭐ **Pre-registered, not pre-judged:** if the extent input,
once admitted, places Davis below Band 5 on extent, `01` §2 requires that divergence to be **written as a
finding** — a Band 5 population inside a bounded ice-free envelope, with an ice sheet on one side and a bay on
the other. That is a finding site, and it is registered here so it cannot later be discovered and quietly
skipped.

### Status — LIVING, and the half the taxonomy cannot carry

`01` §3's 2026-08-31 note fits this case exactly and was written for it: *"a later figure lower than an earlier
one is not automatically **Declining** — check first whether the difference is migration to a documented
destination within the same setting's own future."* Davis's is. The census states *"nobody was born or died in
the transition; they relocated,"* and Davis is **not** in the 2026-09-05 −10% redistribution set, so the change
is an in-world event rather than an authoring artifact.

- **Not `Declining`** — its obligatory question is who *cannot* leave and what a shrinking population can no
  longer maintain. Davis's people left **to a known destination**. They were not trapped.
- **Not `Growing`** — nothing in the admissible set establishes in-frame arrival.
- **Not `Seasonal`, `Contested`, `Resettled`, `Transit-only`, `Dying` or `Dead`.**

> ### ⭐ BUT THE STATUS FIELD IS LOAD-BEARING FOR THE WRONG HALF OF THIS EVENT
> The headcount fell **32.52%**. The *composition* did something the status value cannot express:
> ```
> retained, combined   781,596 / 1,158,314 = 67.48%
> retained, humans     437,423 /   563,599 = 77.61%
> retained, robots     344,173 /   594,715 = 57.87%
> spread                                     19.74 pp toward humans
> ```
> **Davis enters the orbital opening robot-majority and comes out of it human-majority.** `01` §3's note says
> the taxonomy *"does not need, and should not invent, a dedicated status value for every possible cause of
> population change"* — so the correct execution is precisely what it prescribes: **status `Living`, and the
> compositional inversion written in prose as a frame fact.** Done here, deliberately, at Step 0.

### Temporal frame — and the Act question, which `01` §4 makes mandatory at this step

`01` §4's real work is *"the epistemic horizon"*, and for this era the horizon has an internal seam the frame
line has to carry: **the Acts.**

| | |
|---|---|
| **ACT 1** — 2564 → early 2600s (~40–50 yr, **≈18% of the frame**) | people are still *"X who live in Antarctica"*; origin cultures FRESH |
| ⭐ **ACT 2** — ~late 2600s / early 2700s onward (**≈200 of 248 years**) | **properly TEPENIAN.** Origin is **ancestry, not identity** |

Mechanism: **interconnection, decisively solidified by Amundsen Tower's completion (~2688)** — ⛔ *not* a
switch; *not* the creation of unity (the people were never psychologically, culturally or spiritually
separate); already in progress before construction began; and only one of the Tower's many effects, the Tower
being primarily **energy regulation**. **An Act boundary is a consolidation, not a line crossed** — write the
transition as a gradient with a decisive moment inside it.

> ### ⭐⭐ AND ~2688 IS CROWDED IN A WAY THAT MATTERS SPECIFICALLY TO THIS PASS
> Sitting at the same date: **Amundsen Tower's completion · the opening of the ORBITAL TIER · the Census I →
> Census II boundary.** The era file is blunt that this cluster is ***"national context, true everywhere —
> therefore never a differentiator between locations,"*** and then hands over the question that IS legal:
> ***"What differentiates is how hard a given place used that exit."***
>
> ⭐ **Davis has a measured answer to exactly that question, in its own figures, requiring no second city to ask
> or to answer: it retained 67.48% overall, and its robots left at substantially higher rates than its humans
> (57.87% vs 77.61%, a 19.74 pp spread), flipping the majority.**
>
> **One-sentence test, run on it:** delete every other city's name from that sentence. It survives intact — it
> is Davis's own arithmetic against Davis's own earlier state. **Relation and own-figures. Not comparison.**
>
> ⭐ **This is the single most useful thing Step 0 hands forward**, and it is the reason `REQ-G6`'s null is
> survivable: the era file supplies the substitute question and routes it into `G8`, Davis's richest generator.

### Children — `01` §5.4 re-scoped so its discipline survives the deferral

With `Children: none, by deferral`, §5.4 cannot run as written — it asks a Band 4+ pass to mark each category
**Uniform / Patterned / Delegated**, and there are no sub-locations to delegate to. Dropping the section would
lose a real guard. The re-scoping I would apply, stated so it can be accepted or overruled rather than assumed:

- **`Uniform`** — keeps its meaning and keeps its warning. §5.4: *"Rare above Band 4. Suspect any claim of
  it."* At 1.16M, a Uniform answer is the suspect one, deferral or no deferral.
- **`Patterned`** — becomes the **default expectation**. The pass should name the **axis of variation and what
  sits at each end**, even where it cannot name the places that hold them. ⭐ A pattern can be described without
  sub-locations existing; that is what "the pattern of variation" means.
- **`Delegated`** — becomes a **parking disposition**: *"not answerable at this scale, and the sub-location
  pass that would answer it does not exist yet."* It stays a live docket entry rather than a silent hole.

⚠ **I am not confident this is what the methodology intends**, and I did not invent a fourth disposition to
make it tidier. Recorded as a doubt at Part IV.

---

# 0.2 — THE DISCIPLINES

*Six files. For each: **what it obliges THIS pass to do at Band 5** — an obligation now carried, not a summary.*

### 1 · `Disciplines/00b_General_Population_Discipline.md`

**Obligation.** At Band 5 the general population is **1,158,314 people**, and L143 names agriculture-and-research
as *"the clear majority of daily activity."* ⛔ **A "researcher" answer to any category is therefore a NARROW-ROLE
answer at this scale** — greenhouse and cultivation labor is the general case; limnology is the vivid minority.
Every category must state the majority answer **first**, then scope the narrow one explicitly on top of it.
⭐ **And the file's second axis binds harder here than the first: write the SECTOR's general breadth BEFORE the
signature instance exists to be reached for.** "Research" must be widened before it is sized — the recorded
failure is a sector defined so narrowly that its share becomes absurd when multiplied out.
⭐⭐ **The test is arithmetic and it is the only part that does not run on the faculty that produced the error:
multiply any sector share by 1,158,314 and ask what that many people plausibly do all day.**
*(`01` §2.3's Band-1 inversion does NOT apply and is expressly not invoked; the rule is in full force from Band 3
upward.)*

### 2 · `Disciplines/00d_Shadow_Proportion_Discipline.md`

**Obligation.** The overwhelming majority of Davis, day to day, is **people doing what they believe is right
inside a culture that mostly delivers on its promises** — write that as the reality, because it is the reality.
Any shadow must be **unintended, unnoticed in-world, and discoverable rather than announced**; and per §4d's
first discipline the question is never *whether* Davis has a shadow but ***how*** its shadow manifests.
⭐⭐ **The proportionality rule bites in an unusual direction here, and it must be checked rather than assumed.**
`00d`'s worked correction turns on a place where *outside is lethal*, so any exclusion-shaped penalty is a death
sentence and the culture will not impose one. **Davis's own measured conditions are comparatively forgiving** —
mean −10.0 °C, out of the katabatic regime, ~5.6 m/s mean wind, ~400 km² of walkable ice-free ground.
⛔ **So Davis cannot borrow "outside is lethal" as the reason it does not exclude people. If Davis declines to
exclude, the reason has to be Davis's own** — and if it does exclude, the cost must be priced against *these*
conditions, not against a harsher place's. **Check what an exclusion physically costs the excluded person here.**
✅ And: **check canon for an existing no-villain mechanism before deriving one.** `G6` is a recorded null, so
nothing is pre-supplied; the derivation is genuinely open rather than duplicative.

### 3 · `Disciplines/00f_Review_Panel.md`

**Obligation (pre-registered at Step 0, discharged at Step 7).** Cast the **six Flat Archetypes** for a Band 5
agricultural-and-research city, **add the Passer-Through and the Neighbor always**, and **run the Lover
faculty's question every time** — *is this place alive, and could anyone love it?* — since it is the one question
no other gate asks. Two positions are pre-loaded by Davis's own inputs: **the Ruler** asks *"imports as well as
exports… who administers that, who funds it"*, which lands exactly on `REQ-G5v`'s missing throughput; **the
Elder** asks *"was that actually always true?"*, which lands exactly on a city whose founding inheritance is a
written record nobody was taught from.
⚠ **Six dispositions, not five** — `accepted · noted · rejected · refereed · unmet · declined` — with `unmet`
reserved for what Davis **knowingly protects** and `declined` for an anti-homogenization refusal Davis has **no
awareness with which to defend**. Collapsing the two destroys the signal.
⛔ **Rule 3 runs in its PEER-FREE form here, never the sibling form:** *would satisfying this objection replace
something SPECIFIC TO THIS PLACE with something that could be true anywhere?*
⚠ And the panel's own limit is inherited: **a clean panel is not evidence of plausibility.** A panelist cannot
object that Davis is implausible, because the panelist only exists if it is.

### 4 · `Disciplines/Cultural_Synthesis_Techniques.md`

**Obligation.** Run the techniques as **questions**, never as results; **expect several nulls and record them**
rather than manufacturing weak answers. Four concrete obligations fall out of Davis's actual input set:

- ⭐⭐⭐ **`18 The Composition Merge` is the technique this location is built for, and its INPUT CONTRACT IS FULLY
  SATISFIED** — an origin roster **with shares**, 21 entries, hand-verified by me to exactly 100.0000%, with both
  census columns summing exactly to their totals. **Run `R1`–`R7` in full**, on Davis's own numbers only.
  ⛔ **`Guard 5` bites immediately and hard:** L54 states the robot figures apply **the same national-origin
  proportions as the human population**, so the robot/human split of the roster carries **zero independent
  signal**. Mining that axis produces an artifact of the method, not a fact about Davis.
  ⚠ And `R5b`'s pooling is a **hypothesis, not an entitlement** — state any pooled figure as a candidate, name
  what would confirm it, never merge entries silently.
- ✅ **`12 Native Before Transplanted` and `15 Borrowed Form` are UNLOCKED** — composition is established, so
  origin-ethnicities are admissible material. ⚠ **But `15` is UNDER-SUPPLIED and must say so:** its donor
  material is *portable institutions per origin*, and Davis's roster gives **shares without portable
  institutions**. Per the technique's own instruction: **leave the slot open, per NO FORCED FIT.**
- ✅ **`13 The Unused-Tier Mine` runs at maximum yield** — the "all unused" default is safe here because **no
  `Davis_Research_Log.md` exists** (verified absent). The absence is informative, not an obstacle.
- ⛔ **`17 The Zodiac Lens` is PARTLY BLOCKED, and blocked is not null.** `DR-1` pulls the Robot Elementals back
  from canon, and `02` §6.0 requires every symbol's meaning be read **from the system's own file, never from the
  name**. The eight-elemental half of the extension's eighteen cross-checks therefore **cannot be run legally**.
  **Record it as BLOCKED. Do not report it as a null, and do not substitute the bare word.**

### 5 · `Disciplines/Real-World_Basis_Extrapolation_Method.md`

**Obligation.** ⭐ **`LAW 0-R` governs Step 3 and there is no search budget and no time limit.** `G7`'s
designation exists — Vestfold Hills, Ingrid Christensen Coast, Prydz Bay, ~68°35′S 77°58′E — and its **research
half is entirely unbuilt**, so Step 3 begins from zero at maximum available yield. Concretely, this pass now
carries: query every pick from **more than one angle** (founding · physical constraint · what residents do about
it · what it lost · what it is a contrast for); ⭐ **a pick with a sub-part is at least two picks** — the
Vestfold Hills are not Prydz Bay, a fjord system is not a lake system, and **hypersaline lakes and landlocked
marine basins are not freshwater lakes**; **go back to picks already logged as covered**; run and log
near-duplicates; **log dead ends and whether each died at the QUERY or at the SOURCES**; and after every source
ask plainly whether it **changed** a finding or **ornamented** one.
⛔ **Step B's standing principle binds absolutely and is the single easiest thing to violate here:** the real
site is a **coordinate** — its operator nationality, lineage, **abandonment and vacancy** never enter Davis, and
a defensive *"this doesn't apply here"* note is itself a violation of the same kind. ✅ **What stays fully usable
is exactly what Davis's `G2` is already made of:** terrain, climate, materials, dimensions, physical constraints.
⭐ **Step F is not optional:** `Davis_Research_Log.md` **does not exist**, and creating it — with verbatim search
strings, sources, a fact-by-fact *what came back → which finding it became* table, withheld-vs-omitted, and open
threads — is part of the work, not bookkeeping about it.

### 6 · `Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` *(governing, universe-wide)*

**Obligation.** ⭐⭐ **At Census I, robots are the MAJORITY of Davis — 594,715 of 1,158,314.** There is no phase
of this pass that is not already a question about them, and no "robot culture" phase that can be left to carry
them. Five obligations this pass now holds:

- ⛔ **Never write a robot gated out of Davis's weather by her body.** Robots wear clothing near-universally,
  functionally and fashionably; **exposure is a preparation problem, exactly as it is for a human.** The real
  cost is **graded, not binary** — usable capacity falls to 50–60% by −20 °C, materials embrittle and lubricants
  solidify below −40 °C, and ⭐ **a robot is safer MOVING than resting**, because working generates the heat that
  keeps her cells and joints in range. ⭐⭐ **Davis's own numbers make this a live daily constraint:** mean
  −10.0 °C, coldest monthly means −17.1 °C, record low −41.8 °C. **And the glove trade-off is load-bearing here
  specifically** — insulation trades against dexterity, and Davis's declared work is **cultivation**, which is
  fine-motor work in and around the cold. That is a real, physically-grounded question for Phase 8, and it is a
  **gradient across the year**, never a gate.
- ⭐ **Tepenia has a shared night** — robots recharge overnight, humans sleep, everyone stops together.
  ⚠ **In Davis that night is not a constant.** 37 days of polar night, 55 days of midnight sun, and a daylight
  column running 0 h to 24 h. **A shared night in a city whose light budget swings between nothing and
  everything is a question, not a given — and it is Davis's own to answer.**
- **Leisure is a condition of remaining sane, not a perk.** A robot who spends all her time working is virtually
  guaranteed to go insane, which makes **labor conditions a medical question**. At Band 5 that is a
  majority-population health constraint on any seasonal harvest-intensity finding this pass later produces.
- ⛔ **Disposal of the dead is RESERVED** (§0.5 item 4). The file supplies ossuaries as **one possibility among
  several**, expressly rules the wider mortuary question **DEFERRED**, and rules ossuary metal **sacred and
  untouchable** — *"they mine their metal from quarries, rather than stealing from the dead."* This pass may
  record what Davis has; it may not site anything or settle a disposition.
- ⭐⭐ **The Acts apply to robots identically to humans, with one amplification that is pure Band 5 material:
  robots live longer, so a SINGLE Davis robot spans more of the divergence.** One built early in the era and one
  built late **do not carry the same culture, in the same city** — and the transmission channel is the
  **community**, not the fabrication. Across 248 years that is a live **intra-city generational axis** available
  to this pass without a second location, which is precisely what a Band 5 pass with its distributional machinery
  deferred most needs. ⛔ And identity seats in **city-locality**, never in origin, Gen, Mark or build.

---

# 0.3 — RUN GATE 0

> **Cheapest gate, highest yield, and it fails in BOTH directions** — overclaiming completion **and**
> understating a finished piece. Below: **raw scan output, pasted, not summarized**, then the findings.
> ⛔ **Defects are RECORDED. Nothing was edited. Finding a defect is not authorization to fix it.**

## RAW — arithmetic scan of every checkable claim in `00.1_Step_MINUS-1_Input_Contract.md`

```
rows in table: 21
share sum: 100.0000%
Census I  robots sum 594715   vs L15 stated 594,715  -> MATCH
Census I  humans sum 563599   vs L15 stated 563,599  -> MATCH
Census II robots sum 344173   vs L16 stated 344,173  -> MATCH
Census II humans sum 437423   vs L16 stated 437,423  -> MATCH
Census I combined 1158314 vs stated 1,158,314 -> MATCH
Census II combined 781596 vs stated 781,596 -> MATCH

-- contract 3.3 retention block --
combined 781596/1158314 = 67.4770%  (contract: 67.48%)
humans   437423/563599  = 77.6125%  (contract: 77.61%)
robots   344173/594715  = 57.8719%  (contract: 57.87%)
spread   19.7405 pp  (contract: 19.74 pp)

-- majority inversion --
Census I : robots 594715 vs humans 563599 -> ROBOT majority
Census II: robots 344173 vs humans 437423 -> HUMAN majority

-- band placement, 01 §2.1 --
Census I = 1158314 -> Band 5
Census II = 781596 -> Band 4

-- precipitation, L95-106 vs L79 --
monthly sum = 72.8 mm   (L79 states 72.8 mm) -> MATCH

-- mean annual temperature, L95-106 'Mean' column vs L71 --
unweighted mean of 12 monthly means = -10.0333 C   (L71 states -10.0 C)
day-weighted mean = -10.0732 C

-- R-7: retention, L84/L85/L86 --
L84 falls ~73 mm ; L85 lands ~28 mm ; L86 lost ~45 mm
28/73 = 38.36%   ; 28/72.8 = 38.46%   (L85 states ~45% retention)
73-45 = 28  -> the 'lost' figure and the 'lands' figure are consistent in mm
=> the ~45%% is the LOST millimetres (45) reused as a percent. R-7 confirmed.

-- R-3: L74 temperature range vs L95-106 --
L74 states: coldest months avg -21C ; warmest month avg 0C
min of Avg Low column  = -20.8  (Aug)
max of Avg High column = 3.2  (Jan)
=> L74's -21 is an Avg-Low value and its 0 is a Mean value: two different columns. R-3 confirmed.

-- §0 contamination count --
§4.2 table strikes, expanded to individual lines: 11  -> ['L4', 'L9', 'L21', 'L60', 'L62', 'L88', 'L89', 'L91', 'L117', 'L120', 'L121']
§0 enumerates: 10  -> ['L121', 'L89', 'L60', 'L4', 'L9', 'L21', 'L62', 'L91', 'L117', 'L120']
missing from §0's enumeration: ['L88']

-- read spec expansion --
spec expands to 137 lines; duplicates: 0
spec == bound minus strikes ? True
bound size 142 ; bound-minus-strikes size 137
L1-134 bound alone = 134 ; contract §4.1 calls the bound 142 (= 134 + the 8 widened lines)
134 + 8 = 142 ; 142 - 5 strikes = 137
```

## RAW — existence-only reconciliation (`test -f` / `test -d`; **no content read**)

```
ABSENT   Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Davis_Research_Log.md
EXISTS   Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00.1b_T8_Rounds_Step_MINUS-1.md
EXISTS   Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00.1_SUPERSEDED_single-reader_2026-09-11.md
EXISTS   Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Vision_Notes/Davis.md
EXISTS   Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Local_Cultures/Mirny_Subnet/Davis.md
EXISTS   Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Local_Robot_Culture/Mirny_Subnet/Davis.md
ABSENT   Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Extent_and_Density_Per_City.md
ABSENT   Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbol_Assignments.md
DIR EXISTS  Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Megasheets/Mirny_Subnet/Davis
DIR EXISTS  Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis
--- filename-only address resolution (find -name; paths only, zero content) ---
Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md
Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/City_Symbol_Assignments.md
Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Cross_City_Culture_Differentiation_Table.md
--- Davis pass folder: does 00_Frame.md already exist? ---
00.0_Pre-Trip_Inspection.md
00.1a_RULING_Vision_Notes_and_Specs_L135-181.md
00.1b_T8_Rounds_Step_MINUS-1.md
00.1_Step_MINUS-1_Input_Contract.md
00.1_SUPERSEDED_single-reader_2026-09-11.md
README.md
```

## GATE 0 FINDINGS — direction A: **overclaim / defect**

| # | Finding | Severity |
|---|---|---|
| **G0-1** | **A completion claim that does not reconcile against its own table.** §0's comparison table claims **11** contaminated lines found after `T8`, then enumerates **10**: `L121, L89, L60` **+** `L4, L9, L21, L62, L91, L117, L120`. §4.2's strike table, expanded to individual line numbers, **does** contain 11 — it adds **`L88`**, folded invisibly into the `L88–89` row. **The number is right; the enumeration is one short.** Cosmetic, but a completion claim failing to reconcile against its own evidence is precisely Gate 0's remit, and this one was found by counting rather than by reading. | **minor** |
| **G0-6** | **The mean-annual-temperature claim does not name its averaging convention.** §8 asserts *"mean annual temperature reproduces to 0.03 °C."* The twelve monthly Means average **−10.0333 °C unweighted** (0.03 off L71's −10.0) but **−10.0732 °C day-weighted** (0.07 off). Not wrong — **under-specified.** A later reader recomputing with the other convention will believe they have found an error. | **minor** |
| **G0-7** | **`R-7` confirmed, mechanism identified, and the "unresolvable" grade is too pessimistic.** L84 *falls ~73 mm* · L85 *lands ~28 mm (~45% retention)* · L86 *lost ~45 mm*. Computed: `28/73 = 38.36%`, `28/72.8 = 38.46%`. And `73 − 45 = 28`. ⇒ **the millimetre figure for what is LOST (45) has been reused as the retention PERCENT.** The three mm figures are mutually consistent; **only the derived percent is wrong, and the correct value is computable: ~38.5%, not ~45%.** ⇒ recommend re-grading `R-7` from *"unresolvable in-pass"* to **"diagnosed; correction proposed; developer to apply."** ⛔ **Not applied by me.** | **real, diagnosed** |
| **G0-8** | **`R-3` confirmed, and it is bigger than "matters for growing season" conveys.** L74 (*"coldest months avg −21°C; warmest month avg 0°C"*) reads off **two different columns**: min Avg-Low = **−20.8** (Aug); max Avg-High = **+3.2** (Jan); max Mean = **+0.9** (Jan). So −21 ≈ an Avg-Low and 0 ≈ a Mean. ⭐ **The consequence:** the warm endpoint is **+3.2 °C**, and **two months carry non-negative Means** (Jan +0.9, Dec +0.0). For a city whose only function line is cultivation, **how many months sit at or above freezing is a primary input, not a footnote.** | **real** |
| **G0-10** | **`M-117` recurring inside the file that records `M-117`.** `Real-World_Basis_Extrapolation_Method.md` Step D declares *"PATHS ARE RELATIVE TO `Worldspace/Locations-and-Levels/`"* and then names tier-1 **HARD CANON** as two bare filenames — `Official_Population_Census.md` and `Extent_and_Density_Per_City.md`. **Neither resolves under the stated convention, and they live in different trees:** the census at `Outside-World/Tepenian-Federation/Locations/Cities/`, the extent file at `Universal_Location_Methodology/`. ⭐ **This is directly upstream of the extent band being undeclarable at 0.1** — the canon source for the mandated second band cannot be addressed from the instruction that names it. | **real** |
| **G0-11** | **Bare citation.** The contract cites `City_Symbol_Assignments.md` (§3, §3.1) without a path. It resolves at `…/Cities/City_Symbolic_Substrate/City_Symbol_Assignments.md` — reachable, but only by searching. | **minor** |
| **G0-16** | **A MANDATED PRE-CHECK THAT WAS NOT PERFORMED.** `Run_Modes` §2 and `00_RUNBOOK.md` Step 0.4's own required-reading box **both** require checking **`06_Worked_Example_Provenance.md`** for this subject **before Step 0.2**, treating any hit as read-last material: *"Required reading may carry THIS city's own worked example. Reading it at Step 0.2 violates the read order before the pass has begun."* **`06` is not in this reader's list and was not checked.** ⇒ **Recorded as NOT DONE, not assumed clean.** In a warm run this is the one pre-check that protects the read order. | ⚠ **procedural, live** |

## GATE 0 FINDINGS — direction B: **understatement / verified-clean**

| # | Finding |
|---|---|
| **G0-2 ✅** | **The READ SPEC reproduces exactly.** `1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179` expands to **137 distinct lines, zero duplicates**, and is **set-equal** to `bound − {4,9,88,89,121}` where `bound = L1–134 ∪ {143,148,153,154,155,176,178,179} = 142`. `142 − 5 = 137`. **The contract's own mechanical claim holds.** |
| **G0-3 ✅** | **All four per-nation columns sum EXACTLY to their stated totals; shares sum to exactly 100.0000%** across 21 rows. *(The "worst row deviation 0.57 of a person" is a per-row claim needing the unrounded model, which I do not hold — not checked, not disputed.)* |
| **G0-4 ✅** | **§3.3's retention block reproduces:** 67.4770% / 77.6125% / 57.8719%, spread **19.7405 pp**. Rounds exactly to the stated 67.48 / 77.61 / 57.87 / 19.74. |
| **G0-5 ✅** | **Monthly precipitation sums to exactly 72.8 mm**, matching L79. |
| **G0-13 ✅** | **§3's "`02` requires three. Six qualify" reconciles** — the `Counts?` column marks exactly six ✅ (G2, G3, G4, G5, G7, G8); G1 is `no`; G6 is `—`. |
| **G0-14 ✅** | **`REQ-G7r` is correct: `Research_Logs/Davis_Research_Log.md` is verified ABSENT.** ⭐ And per CST `13`, that absence is **maximum yield**, not an obstacle. |
| **G0-15 ✅** | **The band straddle reproduces from `01` §2.1's own table:** 1,158,314 → Band 5; 781,596 → Band 4. |
| ⭐⭐ **G0-9** | **THE UNDERSTATEMENT — and it is the one worth the gate.** `REQ-G6` records *"No in-frame defining event for Davis"* on a **zero-match search of one file**, and grades the pass as *"runs thinner."* **I can corroborate the null from a second, independent, in-frame source that the contract does not cite and that IS in my admissible set: the Second Interwar `Timeline.md`, read in full at 562 lines, does not name Davis once.** ⇒ **the null is confirmed twice over.** ⭐ **But the same two era files also supply what the contract missed:** the README states the ~2688 cluster is *"national context, true everywhere — therefore never a differentiator between locations,"* and then names the legal substitute question outright — ***"What differentiates is how hard a given place used that exit."*** **Davis has a measured answer, in its own arithmetic, needing no second city.** ⇒ **Re-grade `REQ-G6`:** not *"runs thinner"* but ***"runs thinner ON THE EVENT AXIS, and the era file routes the substitute question directly into `G8`, which is this location's richest generator."*** **A finished piece the contract understates.** |
| **G0-12 ⚠** | **Unverifiable inside my range — logged, not routed around.** The contract's headline procedural claim (*"`triple_read_verify.py`, 15 of 15, `UNANIMOUS — CLEARED TO WRITE`"*) rests on `00.1b_T8_Rounds_Step_MINUS-1.md` and `00.1a_RULING_…`. **Both files exist** — existence verified above; **content NOT read**, as neither is in my reading list. ⇒ **the evidence is present; whether it says what is claimed is outside my admissible range and is asserted neither way.** |

> ### ⭐ ONE MORE, WHICH IS NOT A NUMBER — **a strike whose violation the one-sentence test cannot see**
> §4.2 flags **L117** (*"unusual in Tepenia"*) as *"the only strike whose violation is an **implicit** normal
> naming no city — the one-sentence test cannot see it."* ⭐ **I confirm the diagnosis and find the same shape a
> second time, at `L120`: *"the largest oasis environment in Tepenia"* — a corpus superlative naming no city.**
> ⇒ **The one-sentence test has a known, reproducible blind spot: superlatives and "unusual in X" constructions
> scoped to the whole corpus.** Deleting every other city's name leaves both sentences standing, and both are
> still comparisons.
> ### ✅ THE SECOND TEST THAT CATCHES THEM — offered for the law, not applied unilaterally
> > ***"Does this claim require knowing anything about any other place in order to be true?"***
> **`L117` and `L120` both fail it. Davis's own figures — 400 km², −10.0 °C, 67.48% retained — all pass it.**
> **Recommend it be written into the ONE LOCATION law alongside the one-sentence test.** *(This is the finding
> from this round I would most want carried forward.)*

**GATE 0 VERDICT: PASS, with seven recorded defects (two real, one procedural-live, four minor), one
re-grade recommended in the understatement direction, and one unverifiable item logged.** Nothing found here
blocks Step 0 from being written.

---

# 0.4 — THE MANDATED READ ORDER

*`Run_Modes_Warm_and_Cold.md` §2's own order, restated at the point of use — **not** reconstructed from
paraphrase. In a warm run this order is the whole discipline, because **nothing physically prevents opening
item 6 early.** This is the single point where a warm run can silently destroy its own value.*

### **1 · Specs / physical facts** — ✅ **READ, this session, complete for the admissible set**

`Specs/Davis.md`, at the **137-line read spec**, executed as the numeric spec rather than reconstructed from
prose bounds. Partial-strike clauses at **L21, L60, L62, L117, L120, L143** were **read and are NOT USED**.
**L91 is DO-NOT-FOLLOW: the line was read; its target — a 37-city comparison — was never opened.**
⚠ Two physical defects carried forward: **`R-3`** (temperature endpoints on two columns; the warm end is
**+3.2 °C**) and **`R-7`** (retention stated ~45%; computed **~38.5%**). Neither blocks.

### **2 · Symbol assignment** — ⚠ **READ AT STEP −1; NOT RE-READ BY ME; PARTIALLY ADMISSIBLE**

`City_Symbolic_Substrate/City_Symbol_Assignments.md` **L92** — Davis's pair is **`Earth / Earth`**,
column-anchored, with the `Why` column **permanently REFUSED** (`05` §6.1c). It is **not in my reading list** and
I did not open it; I carry it on the contract's reading.

| Half | Standing |
|---|---|
| **Planet — Earth** | ✅ developer hand-authored → **RATIFIED**, meaning **readable** |
| **Element — Earth** | ⛔ **pulled back from canon under `DR-1` → meaning `RESERVED`.** No finding may rest on it |

⛔ **`G1` counts ZERO toward the rule of three** — `05` §6.1c holds it at corroboration-tier, *"never an
independent generator,"* **read LAST as a check.** A match is corroboration; a mismatch is a finding site.
**It may not seed anything.**

### **3 · Composition, census, and population change across snapshots** — ✅ **READ, complete, and the richest**

`Official_Population_Census.md` **L392–398** (tier roster), **L496** (Census I row), **L613** (Census II row);
`Specs/Davis.md` **L15–22** (both census lines plus tiers) and **L30–52** (the 21-nation per-nation table).
**Population change across snapshots: verified in both directions of the arithmetic** (see 0.3 raw).
⚠ **Scope limit honored, and the two operations kept distinct:** **L54** declares the per-nation figures a
**share-weighted model, identical across both censuses by construction**; **L28** declares the **de-stacking
randomization** applied *after* it. ⇒ **usable for named portable institutions; never readable as measured
per-nation counts.**
⚠ **A limitation I am flagging rather than papering over:** L496 and L613 are admitted as **single rows without
the census tables' column headers**, so **which numeric column is humans and which is robots is taken from
`Specs/Davis.md` L15–16, not from the census itself.** The two sources agree on the totals, so the risk is low —
but the column *identification* is **inherited, not verified.**
⚠ And the row-index column (`13`, `14`) is a position in a sorted table. **It is not read, not used, and is not
a rank** — using it would be the ONE LOCATION law's exact violation.

### **4 · Founding and events** — ✅ **READ, complete, with `G6` a confirmed null**

**Founding:** `Specs/Davis.md` **L127** — settled post-Falkland Treaty on existing infrastructure; *"No living
environmental knowledge survived… but preserved journals, logs, and orientation manuals… Learning from a
written record isn't the same as being taught by a living institution"* — and **L129**, founding population:
**Australian exiles.**
**Events:** the Second Interwar **`Timeline.md`** (562 lines, in full) and the era **`README.md`** (70 lines, in
full). ⭐ **Davis is named ZERO times in the era timeline** — an independent second confirmation of `REQ-G6`'s
null, from a source the contract does not cite *(see `G0-9`)*.

### **5 · The sibling set's differentiation instrument** — ⛔ **EXISTS. NOT READ. AND MUST NOT BE READ IN-RUN.**

`Cross_City_Culture_Differentiation_Table.md` **exists** (verified by **filename only**; never opened).
Under the **ONE LOCATION law** a `ULM/CST/RWBEM` city pass is **WRITE-ONLY** on it: **add Davis's own column,
never read another's.** All five comparison instruments move out of the per-location pass into a **single
terminal check on the finished corpus**, and **Gate 6 runs LATE, at Step 7** — in warm mode for the reason
`Run_Modes` §4 gives outright: *other cities stay closed during derivation **precisely so Gate 6 has something
independent to test.*** Open them early and the gate tests nothing.
⇒ **This item's status is a REFUSAL, not an omission**, and the refusal is the methodology working.
⚠ **And the obligation that rides with it:** `Run_Modes` §5 — *the differentiation set must record the mode per
city.* **Davis's eventual column must carry `WARM`,** or the set silently mixes two evidence classes and a later
reader cannot tell which convergence results mean anything.

### **6 · LAST — this location's own completed culture material** — ⛔ **NOT YET READ**

> ## **`Local_Cultures/Mirny_Subnet/Davis.md` and `Local_Robot_Culture/Mirny_Subnet/Davis.md` are NOT YET READ.**
> **Both were verified to EXIST. Neither was opened. Both open at STEP 5, AS A CHECK — never as an input.**

`05` §6.1, verbatim: *"Conclusions are read LAST, and read as a CHECK. After the pass produces its own findings,
compare. **A match is corroboration. A mismatch is a finding site.** Consulted at the start they are
contamination; consulted at the end they are evidence."*
⛔ *"A pass that reads `<City>_Full_Extrapolation.md` before deriving has planted its own seed and will find it"*
— the result is *"perfectly coherent and contains no information,"* and for a foundation layer that is
**indistinguishable from good work, which is exactly what makes it dangerous.**

**Also unopened, and to stay unopened:** `City_Megasheets/Mirny_Subnet/Davis/` *(directory verified to exist;
withheld corpus-wide)* · everything under `Test_Runs/` *(zero intake for the whole pass)* ·
`City_Vision_Notes/Davis.md` *(verified to exist; **struck corpus-wide** by `00.1a`)* · the target of **L91**.

⚠ **AND THE PRE-CHECK THAT BELONGS TO THIS ITEM AND WAS NOT DONE:** `06_Worked_Example_Provenance.md` must be
checked for the Davis subject **before Step 0.2**, with any hit treated as read-last material.
**It is not in my list and was not checked — see `G0-16`.** Recorded, not assumed clean.

---

# 0.5 — RESERVED DECISIONS, AND WHAT WOULD FORECLOSE THEM

> `00_RUNBOOK.md` 0.5: *"know you will probably find material bearing on them anyway. When you do: write it as a
> numbered finding, marked reserved… **A parenthesis is lost; a reserved finding is a handoff.**"* Two such
> findings are recorded at the end of this section.

### 1 · **Proper names of people** — *permanent; role archetypes only*

**Foreclosed by:** naming any individual — a founder, a first cultivator, a harbor master, an archivist. Also by
a definite-description that later hardens into one (*"the woman who first…"*), and by a nickname.
⭐ **The subtle route, and the one most likely to be taken accidentally: naming an INSTITUTION after a person**
(*"the ——— Institute," "——— Hall"*) smuggles a personal name in through a place name, and place names are the
one category RWBEM Step E explicitly says to name specifically. **Institutions here get FUNCTION names.**

### 2 · **The demonym**

**Foreclosed by:** writing any adjectival or plural form of the city's name, even once — *"Davisian," "Davisite,"
"Davis-born,"* or a possessive that reads as a people-noun. ⚠ **This is the easiest reserved item to violate by
accident, because prose actively wants a demonym and every phase will reach for one.**
✅ **Substitutes to use throughout:** *residents of Davis · people here · the city's own · locals.*
⭐ **And a second, less obvious foreclosure: coining an in-world NICKNAME for the place** (*"the Breadbasket,"
"the Oasis"*) pre-empts the demonym by supplying the identity term a demonym would carry. **Do not coin one.**

### 3 · **Which DLC covers the Mirny subnet**

**Foreclosed by:** any finding that presupposes a player arrives here, or that assigns Davis a hub role, a
questgiver, a companion slot, an arrival sequence, or a reputation track. ⭐ **And equally foreclosed by the
reverse** — writing Davis as background, unvisitable, or narratively inert.
⚠ `Repo_Scope.md` binds from the other side: *"This repo holds what happened and why; it never holds what a
player does about it."* **Keep every finding at the level of what is here.**

### 4 · **Disposal of the dead**

**Foreclosed by:** siting an ossuary at Davis, or naming any funerary site, rite, or trade as Davis's.
⛔⛔ **And by one specific inference that will look like a finding rather than a decision.** Burial is stated as
impossible in Tepenia — a nationwide permafrost fact — and **Davis has ~400 km² of ice-free exposed rock.**
***A pass that notices that and concludes Davis can therefore bury its dead has settled the reserved question by
physics, in a single sentence, without ever meaning to.*** **Do not.** The mortuary question is expressly ruled
**DEFERRED**, the two mortality curves are expressly **unreconciled**, and the ossuary is **one possibility
among several**, not the default. ⚠ Also foreclosed by inventing a *robot*-death practice here: robot death is
**episodic**, handled by **religion and community** rather than a professional trade, and Davis has no assigned
religion in the admissible set.

### 5 · **`G1`'s Element meaning** *(`DR-1`)*

**Foreclosed by:** reading **any** meaning off the bare word *"Earth"* — soil, grounding, fertility, rootedness,
solidity, agriculture.
⛔⛔ **This is by far the most likely accidental foreclosure in the entire Davis pass, and the reason is
structural rather than careless: Davis's declared function is AGRICULTURE and its Element is EARTH.** The
association is so available that it will arrive feeling like a derivation. `02` §6.0 requires every symbol's
meaning be read *"from the system's own files, never from the names"* — **and for the Element half that file is
no longer canon**, so the instruction cannot be satisfied and reading meaning off the bare word is precisely
what it forbids.
> ### ✅ STANDING TEST FOR THIS PASS, stated so it does not depend on vigilance
> ***If a finding would be equally well expressed without the word "Earth," it is not resting on `G1`.
> If it would not, it is — and it must be struck.***

**Also foreclosed:** the eight-elemental half of the Zodiac Lens's cross-check extension. ⛔ **Record it as
BLOCKED, never as a null** — *"a blocked check is not an absence."*

### 6 · **Early-Federation currency, Davis's or the subnet's** *(`DR-3`, gated behind all 38 × 3)*

**Foreclosed by:** naming a unit, stating a price, describing a rate, or writing any exchange as monetary.
⚠ **The near-miss that still forecloses it: describing trade as *barter*, *credit*, *ration*, or
*energy-denominated*.** Each of those decides the monetary question by choosing its negative.
✅ **What IS recordable — and per §6 *should* be, because it is the input a future currency pass will need:
what Davis VALUES and TRADES.** The goods, the obligations, the standards of worth, **written as what they are,
without being promoted into a currency.**

### ⭐ Reserved findings actually encountered at Step 0 — recorded as handoffs, explicitly NOT adopted

**`R-B1` — bears on `DR-3` and on the "what Davis values and trades" carve-out.**
**What was found:** `Specs/Davis.md` **L148** states Davis's exports as *"Vestfold Hills oasis resources (lakes,
fjord access, terrain diversity), Prydz Bay maritime trade, logistics within the Mirny subnet"* — while **L143**
makes cultivation the clear majority of daily activity. ⭐ **A city whose majority daily activity is producing
food is described by its own spec as exporting terrain, access and logistics — not calories.**
**What it would decide:** what an early-Federation unit would have to denominate, and what Davis's standard of
worth actually is. **Explicitly NOT adopted here.** It is Phase 5 / Phase 8 work, and naming a traded good at
Step 0 begins denominating the reserved currency.

**`R-B2` — bears on `G3`'s function reading, and on an open question in a ratified root.**
**What was found:** **L153–155** name the fjord inlets, the freshwater/saltwater lake system and the Prydz Bay
harbor; **L176** asks openly *"did the exile community develop scientific or economic uses for these unique
water bodies?"* — hypersaline lakes and landlocked marine basins among them.
**What it would decide:** part of what Davis is FOR, on a line the contract admits as **premise only**.
**Explicitly NOT adopted here.** Step 0 declares the frame; it does not answer the spec's own open questions.

---

# 0.6 — PROVISIONAL ASSUMPTIONS ABOUT THE UNWRITTEN PARENT

**Parent: the Mirny Arcanet subnet. No ULM pass of its own.** `01` §5.2 is explicit that this is **the normal
case, not the exception** — *"a methodology that assumes top-down order will never run."*

Each assumption below is **stated explicitly and numbered** (rule 1), so that any finding resting on one can be
**tagged with it** (rule 2). Each carries its revision cost and, per **rule 3**, the **local physical constraint
I would prefer to build on instead** — *"the ice sheet will not be retconned."*

### **PA-1 — The subnet supplies Davis with Arcanet connectivity as a working, ambient utility for the frame.**
**Basis:** L5 (`Arcanet Subnet: Mirny`) + the contract's epistemic-horizon line (residents know the Arcanet as
functioning). **Revision cost: CHEAP.**
⚠ **Caveat that narrows it:** the era timeline dates the **national** subnet-to-subnet buildout to *"beginning
around 2614"* and flags an **unreconciled tension** with a much earlier *local* subnet-hub construction. ⇒ the
assumption is safe as **"connectivity exists for most of the frame,"** unsafe as *"from 2564."*
✅ **Prefer the local constraint:** anything about how Davis handles information should be built on **L127's
documentary-inheritance founding**, which needs no subnet at all.

### **PA-2 — Davis is not the subnet's administrative hub.**
**Basis:** L7 names the subnet hub separately within the Hwy 110 sequence; L148 speaks of *"logistics **within**
the Mirny subnet"* — Davis **participating in**, not administering. **Revision cost: CHEAP.**
⭐ **Consequence if true:** `01` §5.1's **Determined** class is **wider** for Davis than for a hub — the
calendar, network protocols, and anything the subnet standardizes are **inherited, not local.** ⛔ Which means
**local variants of those things must not be invented** — §5.1's first named error.

### **PA-3 — The food obligation runs OUTWARD from Davis; the subnet does not relieve it of its own production.**
**Basis:** L143, *"Tepenia's breadbasket"* — the polity above needs calories **from** Davis.
⚠⚠ **Revision cost: MODERATE-TO-EXPENSIVE, and this is the assumption with the most hanging on it.** `G3`'s
tension reading — *residents understand themselves as researchers while the polity above them requires
calories* — depends on it.
✅ **Mitigation already available, and it is why this does not violate rule 4:** **both halves of that tension are
stated in ONE ratified line (L143) as Davis's own self-description.** The tension survives as a fact about how
Davis describes itself even if the parent's need is later re-characterized. **Tag every finding that uses the
outward direction with `PA-3`.**

### **PA-4 — Hwy 110 runs in both directions through Davis for the frame, and Prydz Bay harbor is a working maritime entry.**
**Basis:** L6 (access type **ON**), L7 (Hwy 110, the Coastal Cut Highway), L155 (Prydz Bay harbor, primary
maritime entry). **Revision cost: CHEAP for existence and direction.**
⛔ **UNSAFE FOR MAGNITUDE.** `02` `G5` demands **direction AND volume**, and **no throughput figure exists
anywhere** (`REQ-G5v`). ⇒ **No finding may be scaled off assumed throughput.** Direction only.
*(One-sentence test, applied to the retained form: delete every other name — **"Davis sits on Hwy 110 with road
access in both directions and a Prydz Bay harbor"** survives. Relation, not comparison.)*

### **PA-5 — The subnet supplies no defining in-frame event to Davis.**
**Basis:** `REQ-G6`'s null, now corroborated independently — **Davis is named zero times in the era timeline.**
⚠ **This is an assumption about an ABSENCE** — the cheapest kind to revise and **the most dangerous kind to
build on.** ⇒ ⭐ **It is deliberately NOT BUILT ON.** The pass treats `G6` as a **recorded null**, not as
evidence that nothing happened. If the subnet's eventual pass supplies an event, **nothing here has to be
unwound.**

### **PA-6 — GUARD, not an inheritance: nothing about the subnet is admissible as a source of Davis's culture.**
The subnet is **unwritten**, so **there is no subnet culture to inherit** — and the failure `01` §5.2 exists to
prevent is **inventing one and then "inheriting" it.**
✅ **Where a category comes up empty, the order of attempts is `01` §5.1's, in order:**
**check what the parent DETERMINES → what the parent supplies that Davis INFLECTS → who arrived carrying one
(`15 Borrowed Form`) → whether Davis is already doing it somewhere unnoticed (`The Unrecognized Instrument`) →
only then invent.**
⛔ **With the parent unwritten, the first two steps return "UNKNOWN," which is not the same as "NOTHING," and
must never be written as if it were.**

> ## ✅ `01` §5.2 RULE 4 — COMPLIANCE, STATED EXPLICITLY RATHER THAN LEFT TO CARE
> *"Do not build the location's single strongest finding on a provisional assumption about an unwritten parent."*
>
> **The strongest finding available at Step 0 is the retention-and-inversion reading:** Davis retained **67.48%**
> of its Census I population across the orbital opening — **humans 77.61%, robots 57.87%, a 19.74 pp spread** —
> and the city enters robot-majority and leaves human-majority.
> ⭐ ***That rests on census arithmetic and on NOTHING about Mirny whatsoever.***
> **Rule 4 is satisfied by construction, not by vigilance.**

> ## ⚠ `01` §5.2 RULE 5 — **NOT DONE, and cannot be done by me**
> *"Register the assumption where the parent's eventual pass will see it. An assumption recorded only in the
> child's file is an assumption the parent will contradict."*
> **No Mirny-subnet registry exists to write into, and I am forbidden to edit any file.** ⇒ **Recorded as an
> obligation the pass owner must discharge**, not as a satisfied requirement. **Gate P (`04`) reconciles against
> it later**, and the reciprocal obligation is real: when Mirny is eventually written, **its pass must reconcile
> against these six and name the Davis findings that need revision wherever it contradicts one.**

## `01` §5.1 — the four inheritance classes, where Step 0 can already see them

> ### ⚠⚠ `M-157`: **THIS INSTRUMENT IS ACT-BLIND.** *"A classification made once has been made for an UNSTATED
> DATE."* The **Determined** class **WIDENS** across the Act 1 → Act 2 boundary, so **Inflected** and
> **Originated** **narrow**. ⭐ **Every call below is dated.**

| Element visible at Step 0 | Class | ⭐ **As of which Act?** |
|---|---|---|
| **Climate, terrain, light budget** — −10.0 °C mean · 37-day polar night · 55-day midnight sun · ~400 km² ice-free · out of the katabatic regime · 72.8 mm falls | **Determined** *(by physical law, not by the parent)* | ⭐ **BOTH ACTS, UNCHANGED.** The only input in the whole frame that is **Act-invariant** — which is exactly why §5.2 rule 3 says to build here |
| **Arcanet connectivity; whatever the subnet standardizes** | **Determined** | ⚠ **ACT-SENSITIVE AND CURRENTLY UNKNOWABLE.** National buildout ~2614, with an unreconciled earlier local-hub date. **Narrower in Act 1; widens across the boundary.** Rests on `PA-1` |
| **National identity — *being Tepenian*** | **Determined — but ONLY FROM ACT 2** | ⭐⭐ **This is `M-157`'s own example, live.** In Act 1 (~18% of the frame) it is **not yet supplied**; people are still *"X who live in Antarctica."* In Act 2 (~200 of 248 years) the parent supplies it — and ⛔ **it is never a differentiator.** *Differentiate locally; converge nationally* |
| **Origin-stock forms the 21 nations carried in** | **Inflected** in Act 1 → **increasingly Originated-as-local** by Act 2 | ⭐ The **divergence operator** runs across the boundary — *time · separation · local environmental setting · local struggles and hardships · local goals · local sensibilities and habits.* ⛔ **Do not reason from elapsed time; process the data on its own terms** |
| **Food production as an obligation running outward** | **Aggregated** *(the parent's own character is partly the sum of what its children supply)* | **Act-neutral as a fact.** ⚠ Rests on `PA-3` |
| ⭐ **The documentary-without-institution founding inheritance (L127)** | **Originated** — it comes from nowhere above | **Act 1 in ORIGIN, and it is the one Act 1 element with a live ACT 2 consequence:** a knowledge culture founded on a **written record rather than a living teacher**, carried forward by a population **whose robot majority individually spans much of the frame** |

> ### ⛔ AND THE STRUCTURAL RISK THIS CONFIGURATION CREATES — pre-registered so a later gate can look for it
> `01` §5.1: ***"The Inflected class is the workhorse and is systematically under-used"*** — it is *"where most
> good local culture actually lives."* **With Davis's parent UNWRITTEN, `Inflected` is precisely the class this
> pass cannot populate: there is no parental form available to inflect.**
> ⇒ ***The predictable compensation is over-use of `Originated` — claiming local invention for things the subnet
> or the Federation actually determines.*** **That is §5.1's named error running in its second direction, and it
> is this configuration's specific failure mode.** Recorded here, at Step 0, so it can be checked for rather than
> discovered.

---

# PART IV — DEFECTS AND DOUBTS

> *Per the recording law: snags, blockages, dead ends, **killed findings** and self-corrections — not only
> successes. Everything below is **RECORDED. Nothing was edited.** Finding a defect is not authorization to
> fix it.*

## A · Defects **inside the methodology itself** — including two instructions that contradict each other

**D-1 · ⛔ TWO ULM INSTRUCTIONS DIRECTLY CONTRADICT EACH OTHER ON `City_Vision_Notes/`.**
`Real-World_Basis_Extrapolation_Method.md` **Step D, row 2** — a file this Step **mandates** reading at 0.2 —
ranks `City_Vision_Notes/<City>.md` as ***"⭐⭐⭐ AUTHORIAL VISION — PRIMARY AND UPSTREAM… the developer's own
words: 'my own personal mental visions… a basis OF canon.' ⛔ NEVER treat as a derived conclusion."***
The Davis contract **§4.3** and **`00.1a`** record the same root as ***"struck corpus-wide."***
⛔ **These cannot both be followed.** A pass that follows its own mandated discipline file **opens a struck
root believing it is obeying the method** — and the file exists on disk (verified; **not opened by me**).
⇒ **The ruling has not propagated into the instrument that sends readers there.** Flagged, not resolved.

**D-2 · ⛔ `01` §2 MANDATES AN EXTENT BAND AND SUPPLIES NO EXTENT SCALE.**
§2 requires *"two numbers, not one"* and forbids deriving extent from density. §2.1's table has columns for
Band, **Population**, unit of analysis, and district assumptions — **no extent column, and no km²-to-band
mapping anywhere in the file.** ⇒ **the second mandated number cannot be produced without supplying a criterion
the methodology does not state.** Declared `UNDETERMINED` rather than guessed. **Candidate methodology gap.**

**D-3 · ⛔ `M-117` RECURRING INSIDE THE FILE THAT RECORDS `M-117`** *(= `G0-10`)*, and it is **upstream of D-2**:
the canon source for the extent band is named as a bare filename under a stated relative-path convention it does
not satisfy, and it lives in a **different tree** from the census it is paired with.

**D-4 · `01` §1.2's MODIFIER SET HAS NO ENTRY FOR DAVIS'S ACTUAL FOUNDING SHAPE.**
`Resettled` presupposes a first **population**; Davis was **first-settled on second-hand infrastructure**, with
no prior resident community and with the prior operators' identity excluded by the GPS law in any case.
⇒ **Most conservative value taken (no modifier); problem named; set NOT widened by me.** The material loses
nothing — it is already seated at `G4`.

**D-5 · ⚠ THE ONE-SENTENCE TEST HAS A REPRODUCIBLE BLIND SPOT** *(= `G0`'s closing item)*. §4.2 names it once
(**L117**, *"unusual in Tepenia"*); **I found the same shape a second time at L120** (*"the largest oasis
environment in Tepenia"*). **Corpus-scoped superlatives and "unusual in X" constructions name no city, so
deleting every city name leaves them standing — and they are still comparisons.**
✅ **Proposed second test, offered for the law rather than applied unilaterally:** ***"Does this claim require
knowing anything about any other place in order to be true?"*** L117 and L120 fail it; Davis's own figures all
pass it. **This is the finding from this round I would most want carried forward.**

**D-6 · ⚠ BAND 5's DEFERRAL SUSPENDS THE REMEDY, NOT THE RISK.** `01` §2.2 states that a Band 5 pass reading
like a Band 3 pass has committed the scale error named in `00c` Gate 11 and `00d`. With decomposition **and**
distributional analysis both deferred, **this pass holds no instrument against that error and no gate will
catch it** — the gates confirm a pass is not *wrong* and none can tell you it is thin. **Not an objection to
`DR-4`; a statement of its price, recorded so it is visible in the result.**

**D-7 · ⚠ A MANDATED PRE-CHECK WAS NOT IN THE READING LIST** *(= `G0-16`)*: `06_Worked_Example_Provenance.md`,
required **before Step 0.2** by both `Run_Modes` §2 and the Step 0 required-reading box. **Not performed.**

## B · Defects in the Davis material

**D-8 · `R-7` is diagnosable and the "unresolvable" grade is too pessimistic** — the mechanism is **45 mm lost
reused as 45% retained**; the corrected value is **~38.5%**. *(Full working at 0.3.)*
**D-9 · `R-3` is larger than its grade suggests** — the warm endpoint is **+3.2 °C**, not 0 °C, and **two months
carry non-negative Means.** For a city whose only function line is cultivation, the count of at-or-above-freezing
months is a **primary input.**
**D-10 · §0's contamination count (11) does not reconcile with its own enumeration (10)** — `L88` is missing
from the list, folded invisibly into the `L88–89` row.
**D-11 · The mean-temperature claim does not name its averaging convention** — true unweighted (0.03 °C), 0.07 °C
off day-weighted.
**D-12 · Two bare citations** — `City_Symbol_Assignments.md` resolves only by searching; the extent file worse
(D-3).

## C · ⭐ KILLED FINDINGS — recorded because the recording law asks for them

**K-1 · `Settlement + Installation` — DRAFTED AND KILLED.** `01` §1.1's starred rule says *"anywhere founded as
an installation and now inhabited as a home carries `Settlement + Installation`, and the tension between
'staffed' and 'settled' is a live source of material."* Davis was settled **on Davis Station infrastructure**,
so the doubling looked automatic. ⛔ **Killed:** the doubling requires the installation character to be **live in
the inhabited present**, and `Installation` requires *"a controlling institution, staffed rather than settled."*
**Nothing in the admissible set gives Davis a controlling institution in-frame** — the only staffing material
belongs to the **pre-2564 site**, which the GPS law excludes as a cause, an identity or a history. **Assigning it
would have imported the real station's identity through the back door.**

**K-2 · The `Resettled` modifier — DRAFTED AND KILLED** *(full reasoning at 0.1; summary at D-4)*. Killed on the
**same ground as K-1**: the obligatory question could only have been discharged with material the GPS law
forbids.

⭐ **Net effect of both kills: TWO type-level assignments removed, ZERO content lost.** The single piece of
material both were reaching for — **L127's documentary inheritance without a living institution** — is already
seated at `G4`, where the contract puts it and where it belongs. **That is `NO FORCED FIT` working in the
direction that is harder to notice: refusing a category that looked obviously right.**

## D · Doubts I could not settle, stated as doubts

**Q-1 · The census column identification is INHERITED, not verified.** L496 and L613 are admitted as **single
rows without their tables' headers**, so which numeric column is humans and which robots comes from
`Specs/Davis.md` L15–16 rather than from the census itself. **The totals agree, so the risk is low — but I am
flagging the identification rather than asserting it.**

**Q-2 · I am not confident my re-scoping of `01` §5.4 is what the methodology intends.** With `Children: none`
by deferral, §5.4's three dispositions cannot run as written. I re-scoped them — `Uniform` keeps its warning,
`Patterned` becomes the default expectation with the **axis** named even where the places holding its ends do
not exist, `Delegated` becomes a **parking** disposition. **I deliberately did not invent a fourth disposition.**
**Accept or overrule; do not assume.**

**Q-3 · `Children: none` states a fact about the REPO, not about Davis.** A city of 1,158,314 people **has**
internal differentiation whether or not anyone has written its sub-locations. Writing `none` is accurate about
the corpus and misleading about the place, and I could find no phrasing in `01` that distinguishes the two.
**Recorded as "none, BY DEFERRAL — not by absence," which is the best I could do inside the vocabulary given.**

**Q-4 · The `G1`-Element / agriculture collision worries me more than any other contamination route in this
pass** *(0.5 item 5)*, because it will present as a derivation rather than as a leak. **I converted it into a
mechanical standing test rather than leaving it to vigilance, and I am still not confident that is enough.**

**Q-5 · `G3` rests on one line, and the adjudication that deletes it has already been made once.** L143 is the
only text in the entire admissible set that says what Davis is **for**; it sat inside a range a prior pass
refused wholesale on a heading. **The contract names this as its own biggest doubt and I independently reach the
same one.** ⭐ **Two passes arriving at the same single point of failure is not corroboration that it is safe —
it is corroboration that it is the point of failure.**

---

## ⭐ WHAT I WOULD HAND FORWARD, IF ONLY ONE THING SURVIVED THIS READ

**The era file asks the question and Davis's own census answers it, with no second city involved at any point:**

> **~2688 puts Amundsen Tower's completion, the orbital tier's opening and the Census I → II boundary at the
> same date. That cluster is national context — true everywhere, and therefore never a differentiator.
> *What differentiates is how hard a given place used that exit.*
> Davis retained 67.48% of its Census I population. Its humans retained 77.61%; its robots, 57.87% — a
> 19.74 pp spread. The city went into the opening robot-majority and came out of it human-majority.**
>
> ***When leaving became possible, the robots of Davis left at substantially higher rates than its humans.
> What about this place made that so?***

**One-sentence test: every other city's name is already absent. The claim stands on Davis's own arithmetic
against Davis's own earlier state. Relation, not comparison — and it rests on no assumption about the unwritten
parent, which is why `01` §5.2 rule 4 is satisfied by construction.**

**— END OF READER B OUTPUT.**


---

# ROUND 1 — READER C

# DAVIS — STEP 0 · FRAME — **T8 READER C**, independent

**Run mode: WARM.** Read independently, without contact with Readers A or B.
Written 2026-09-14. **No repository file was edited.**

---

# PART I — THE 15 PROOF BLOCKS

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md
LRANGE: 2416-2479
LINES: 64
L1: # Step 0 — Frame
LMID: 
LLAST: constraint over provisional inheritance wherever the choice exists.
QUOTE: **0.4 Read everything the location already has, before writing over it.**

*(Note: the middle line of the admitted set is file line 2447, which is empty. LMID is therefore an empty string, reported as such rather than substituted.)*

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md
LRANGE: FULL
LINES: 582
L1: # Frame, Typology, and Inheritance
LMID: | **Transit-only** | Who maintains it, and do they count as living here? |
LLAST: would have made visible before the writing started.
QUOTE: | **5 — Regional** | ~1M–50M | **Distributions**, not points | Mostly fail |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Run_Modes_Warm_and_Cold.md
LRANGE: FULL
LINES: 177
L1: # RUN MODES — WARM and COLD, defined
LMID: > that is indistinguishable from good work, which is exactly what makes it dangerous.**
LLAST: > it is the one that produces cities.**
QUOTE: > # **THIS CITY'S OWN CULTURE MATERIAL IS READ LAST, AND READ AS A CHECK.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00b_General_Population_Discipline.md
LRANGE: FULL
LINES: 261
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: 
LLAST: baseline stated beside it.
QUOTE: > **Multiply the sector percentage by the population. Compare against what that work plausibly requires.**

*(Note: the middle line, file line 131, is empty. Reported as such.)*

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00d_Shadow_Proportion_Discipline.md
LRANGE: FULL
LINES: 222
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: > **A district operates on its own sincere conception of what "doing good" means and what a proper community
LLAST: *secretly awful*, the proportion is wrong — regardless of how well-sourced each individual finding is.
QUOTE: The Shadow is a **byproduct**, never the operating principle.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/00f_Review_Panel.md
LRANGE: FULL
LINES: 832
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: related, and affectionate,"* the origin of a place's spirituality and its *"sense of the mystic oneness and
LLAST:   now.)*
QUOTE: > **Before accepting any objection, ask: would satisfying this make the district more like the other twelve?**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/Cultural_Synthesis_Techniques.md
LRANGE: FULL
LINES: 1196
L1: > # ⚠ ULM COPY — **the original is authoritative and is UNCHANGED.**
LMID: **The question.** *Which of this location's picks has nothing in the existing material actually derived from
LLAST: 
QUOTE: ⛔⛔ **THE ROSTER IS A DEMOGRAPHIC FACT. THE LOCAL CULTURE IS A DIFFERENT OBJECT. *Listed is not represented.***

*(Note: file line 1196 is empty; the file ends with a trailing blank line. A tool that reports "1197 total" is counting a phantom split element — `wc -l` and `awk END{print NR}` both return 1196, and the last byte is a newline. Read in two passes, 1–841 and 842–1196.)*

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/Real-World_Basis_Extrapolation_Method.md
LRANGE: FULL
LINES: 463
L1: # ⭐⭐⭐ LAW 0-R — RESEARCH FULLY. **A PICK IS NOT EXHAUSTED BECAUSE IT HAS BEEN SEARCHED.**
LMID: ### ⭐ IT IS A SEQUENCING RULE, NOT A REPEAL — **the prohibition above is UNCHANGED**
LLAST: 3. **A real detail beats an invented one every time.**
QUOTE: > # **ONE SEARCH AGAINST A PICK ESTABLISHES THAT THE PICK EXISTS. IT DOES NOT ESTABLISH WHAT THE PICK HOLDS.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md
LRANGE: FULL
LINES: 438
L1: # Robot Physiology and Cultural Practices
LMID: ### ⭐⭐⭐ THE GRAND-TIMELINE ACTS
LLAST:   **Flagged 2026-07-09, for a possible future questline (not a religion):** during a Robot Religions development session, a "trace your own origin" concept was considered as the basis for a new religion (a reground of a ChatGPT-suggested "Cult of the Source") and set aside — the developer liked the mystery but didn't think it actually works as a religion's foundation. The mystery itself is worth keeping: a robot tracing which mark/generation their own chamber was built to, and from there discovering that the schematic's actual designer (Neumayer, credited nowhere, the same uncredited pattern as the Amundsen Tower) goes unknown to almost everyone built from their work — a solvable-in-principle, currently-forgotten origin mystery, not an abstract data-mysticism. Already has a discoverable in-game hook to build from: Calethina's own chamber (the one that built the player character) traces to the historical, now-dark Mountain Pass site. See `Factions/Robot_Religions/Cymatics_reverence/Cymatics_reverence.md`'s development history for the fuller reasoning trail.
QUOTE: **1. Physical — they require downtime, most prominently OVERNIGHT RECHARGING.** Like anybody else.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Repo_Scope.md
LRANGE: FULL
LINES: 30
L1: # Repo Scope — A Binding Law
LMID: - **Game mechanics of any kind** — stat blocks, XP/leveling systems, companion/romance gating, quest triggers, re-spec systems, ending-branch design, UI/UX, engine or asset-pipeline decisions. This is InnerTepeniaGDD's (or OuterTepenia1_GDD's) own design work, not shared canon.
LLAST: Before adding or porting content here, ask: does this tell you *when*, *where*, or *who*? If the honest answer is "it tells you *how to play/read it*" or "*what mechanically happens next*," it's out of scope — note its existence if useful for cross-reference, but don't port the content itself.
QUOTE: If a piece of content doesn't serve one of those three questions, it does not belong in this repo — it belongs in whichever individual project actually needs it.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/README.md
LRANGE: FULL
LINES: 70
L1: # The Second Interwar Period — **2564–2812**
LMID: > Amundsen Tower. Their being fully interconnected further defined their sense of national identity in who
LLAST:    environmental setting · local struggles and hardships · local goals · local sensibilities and habits.*
QUOTE: > ## ⚠⚠ **THE ERA SPANS BOTH ACTS AND IS MOSTLY ACT 2.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/Timeline.md
LRANGE: FULL
LINES: 562
L1: # The Second Interwar Period — Timeline (2564–2812)
LMID:   federation spirit survives without that specific person.
LLAST:   Reference.md` as beats are developed, to keep all documents consistent.
QUOTE: **~2688 (resolved 2026-08-05, ±~20yr flexibility — not locked to an exact year)**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md
LRANGE: 392-398,496,613
LINES: 9
L1: **Davis** *(Vestfold Hills, Prydz Bay — mainland coast)*
LMID: | Primary | China |
LLAST: | 14 | Davis | Mirny | 437,423 | 344,173 | **781,596** | |
QUOTE: | 13 | Davis | Mirny | 563,599 | 594,715 | **1,158,314** | *(revised 2026-07-04)* |

*(Admitted set = {392,393,394,395,396,397,398,496,613}. Middle element (9+1)//2 = 5th = file line 396.)*

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Davis.md
LRANGE: 1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179
LINES: 137
L1: # Davis
LMID: **Mean annual temperature:** -10.0°C  _(READER station: Davis; 1991–2020 WMO standard normal)_
LLAST: - **Relationship to Mawson (the city, different subnet)** — both named for/connected to Australian Antarctic figures, but administratively and geographically separate; worth clarifying whether any cultural connection existed despite the subnet divide
QUOTE: Davis is, above all, Tepenia's breadbasket and a prime ecological/limnological research hub — sheltered-agriculture and greenhouse cultivation alongside genuine research heritage make up the clear majority of daily activity.

*(Admitted set = 137 line numbers. Middle element (137+1)//2 = 69th admitted line. Segment arithmetic: 1-3 = idx 1–3 · 5-8 = idx 4–7 · 10-87 = idx 8–85 · 90-120 = idx 86–116 · 122-134 = idx 117–129 · 143 = 130 · 148 = 131 · 153-155 = 132–134 · 176 = 135 · 178-179 = 136–137. idx 69 = file line 10 + (69−8) = **file line 71**. Read as ten separate ranged reads; no line outside the spec was opened.)*

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/00.1_Step_MINUS-1_Input_Contract.md
LRANGE: FULL
LINES: 371
L1: # Davis — Step −1 · THE INPUT CONTRACT
LMID: > **L127:** *"No living environmental **knowledge** survived that chain of handoffs — but preserved journals,
LLAST: ⛔ **Step 0 — FRAME — opens next.**
QUOTE: So in-frame — for all 248 years this pass covers — Davis is a living, operating city.

---

```
COVERAGE: 00_RUNBOOK.md 1-64, no gaps, no overlaps · 01_Frame_Typology_and_Inheritance.md 1-582, no gaps, no overlaps · Run_Modes_Warm_and_Cold.md 1-177, no gaps, no overlaps · 00b_General_Population_Discipline.md 1-261, no gaps, no overlaps · 00d_Shadow_Proportion_Discipline.md 1-222, no gaps, no overlaps · 00f_Review_Panel.md 1-832, no gaps, no overlaps · Cultural_Synthesis_Techniques.md 1-1196, no gaps, no overlaps · Real-World_Basis_Extrapolation_Method.md 1-463, no gaps, no overlaps · Robot_Physiology_and_Cultural_Practices.md 1-438, no gaps, no overlaps · Repo_Scope.md 1-30, no gaps, no overlaps · Second Interwar README.md 1-70, no gaps, no overlaps · Second Interwar Timeline.md 1-562, no gaps, no overlaps · Official_Population_Census.md 1-9, no gaps, no overlaps · Specs/Davis.md 1-137, no gaps, no overlaps · 00.1_Step_MINUS-1_Input_Contract.md 1-371, no gaps, no overlaps
MANIFEST: mapped 15 of 15 files — 00_RUNBOOK.md(2416-2479), 01_Frame_Typology_and_Inheritance.md, Run_Modes_Warm_and_Cold.md, 00b_General_Population_Discipline.md, 00d_Shadow_Proportion_Discipline.md, 00f_Review_Panel.md, Cultural_Synthesis_Techniques.md, Real-World_Basis_Extrapolation_Method.md, Robot_Physiology_and_Cultural_Practices.md, Repo_Scope.md, Second_Interwar_README.md, Second_Interwar_Timeline.md, Official_Population_Census.md(392-398,496,613), Specs/Davis.md(137-line read spec), 00.1_Step_MINUS-1_Input_Contract.md; not reached — none
```

**Files deliberately NOT opened, per contract:** `Local_Cultures/Mirny_Subnet/Davis.md` · `Local_Robot_Culture/Mirny_Subnet/Davis.md` · `City_Megasheets/Mirny_Subnet/Davis/` · `Test_Runs/` (any) · `City_Vision_Notes/` (any) · `City_Symbol_Assignments.md` · `Extent_and_Density_Per_City.md` · `06_Worked_Example_Provenance.md` · any other city's conclusion-tier file. **`graphify` was not invoked, and no repo-wide search was run to locate any of the 15 files.** The `PreToolUse` graphify hook fired on essentially every call; disregarding it is the brief's own instruction for this task, not my own judgment.

---

# PART II — STEP 0 OUTPUT

## 0.1 — THE FRAME DECLARATION BLOCK

```
## Frame Declaration

**Location:**        Davis — Vestfold Hills, Ingrid Christensen Coast, Prydz Bay (~68°35′S, 77°58′E)

**Type:**            Settlement  +  (no modifiers assigned — see the modifier docket below;
                     an empty modifier list is a RESULT, not an unfilled slot)

**Population band:** 5 — Regional, approx. 1,158,314
                     [Census I (Pre-Orbital), GOVERNING per developer ruling DR-4:
                      563,599 humans / 594,715 robots. Band 5 = ~1M–50M per `01` §2.1.
                      ⏸️ `01` §2.2's two MUSTs (3→4 sub-location decomposition; 4→5
                      distributional analysis) are DEFERRED BY RULING, not missed.
                      This pass writes base-level fundamental facts AT a declared Band 5
                      WITHOUT performing Band 5 distributional analysis. No finding in
                      this pass may be presented as a distributional result.]

**Extent band:**     5 — declared as MATCHING the population band, conservatively and
                     WITHOUT independent confirmation. ⚠ NAME THE PROBLEM: `01` §2 requires
                     two bands and §6's template has a line for it, but §2.1's band table
                     defines ONLY population thresholds — there is no extent scale anywhere
                     in `01`. The one extent-relevant figure in the admitted set is physical,
                     not civic: ~400 km² of ice-free exposed rock, lakes and fjord-like inlets
                     in the Vestfold Hills (L60). The corpus's own extent ruling
                     (`Extent_and_Density_Per_City.md`) was NOT in this reader's admissible
                     set. I therefore decline to assert a divergence I cannot source, and
                     decline equally to assert that none exists. THE DIVERGENCE QUESTION IS
                     OPEN, and if it later resolves as divergent, `01` §2 makes that
                     characterizing and it must be written as a finding then.

**Status:**          LIVING
                     [Per `01` §3's note on "a population drop that is migration, not decline,"
                      read before choosing. Davis's Census I → Census II fall (1,158,314 →
                      781,596) is documented relocation to the orbital tier — a destination
                      inside this setting's own future — not loss. The census states nobody
                      was born or died in the transition; they relocated. DECLINING is
                      therefore WRONG, and its obligatory question (who cannot leave, what a
                      shrinking population can no longer maintain) is not the question Davis
                      poses. The migration is stated here in prose, as §3 directs, rather
                      than given a status value of its own.
                      Act 1 (2564 → early 2600s) would separately support GROWING — founding,
                      build-out, an arriving exile population. `01` §3 permits one status; I
                      declare LIVING for the frame as a whole and record the Act 1 growth and
                      the ~2688-onward out-migration in prose beneath it, rather than hedging
                      the status line across 248 years.]

**Temporal frame:**  THE SECOND INTERWAR PERIOD — 2564–2812 (248 years). DECLARED, NOT INFERRED,
                     and declared explicitly per `01` §4.1 rule 4 even though it is the default.
                     The frame spans BOTH Grand-Timeline Acts and is MOSTLY ACT 2 (Act 1 ≈ the
                     first 18% of the period). Davis's own defining internal change — the
                     Census I → II orbital out-migration, at the ~2688 crowding — sits INSIDE
                     this frame, not across its boundary.
                     EPISTEMIC HORIZON: residents know the Arcanet as functioning, Amundsen
                     Tower as completed and operating, and orbital migration as a lived event
                     that took a third of their neighbors. The Long Night War, the Tower's
                     destruction and the Planetary Split Brain HAVE NOT HAPPENED and cannot be
                     imagined by anyone here.
                     ⛔ `Specs/` "Status:", "Current Status / Destruction", "Connection to
                     Concordia" and "Legacy" are POST-WAR and are NOT INPUTS. Their absence is
                     never a gap and is never a REQUESTED item.

**Parent:**          The MIRNY Arcanet subnet, within the Tepenian Federation.
                     [UNWRITTEN — no ULM pass exists for it. See §0.6's numbered provisional
                      assumptions. Membership itself is NOT provisional: it is carried
                      independently by Specs L5 and by BOTH census rows (L496, L613).]

**Children:**        NONE DECLARED. ⚠ This must not be read as "Davis has no sub-locations."
                     Decomposition into sub-locations is the `01` §2.2 threshold-3→4 MUST,
                     and it is DEFERRED BY RULING (DR-4) until all 38 cities complete
                     ULM + CST + RWBEM. The slot is explicitly OPEN, by decision.

**Sibling set:**     EXISTS — the other cities of the Mirny subnet, and the wider 38-city
                     corpus — but is CLOSED to this pass. Conclusion-tier material about every
                     other city stays closed until Step 6; Gate 6 runs late, at Step 7; the
                     differentiation table is WRITE-ONLY in-run (add Davis's own column, never
                     read another's).
                     SUBSTITUTES USED, per `01` §5.3a, stated so a later reader does not read
                     them as un-run checks:
                       1. ITS OWN EARLIER STATES — ✅ AVAILABLE AND STRONG, and I ran `01`
                          §5.3a's mandatory axis check BEFORE committing: all three states
                          (founding 2564, Act 1 · the ~2688 crowding · the late era to 2812)
                          sit INSIDE the declared frame. This is a genuine THREE-state axis,
                          not a two-state one. That is itself a Step 0 finding: Davis's
                          defining internal change does not straddle its own frame boundary,
                          so the instrument runs at full strength and Gate F is not at risk.
                       2. NEAREST ANALOGOUS LOCATION AT A DIFFERENT SCALE — ⚠ WEAK HERE. The
                          natural candidate is the parent subnet, and the parent is unwritten.
                          Recorded as weak rather than silently skipped.
                       3. REAL-WORLD COMPARABLES via RWBEM — ⏸️ AVAILABLE BUT UNBUILT. No
                          `Davis_Research_Log.md` exists (REQ-G7r). Opens at Step 3.
                       4. THE GENERATOR-CONFLICT METHOD — ✅ AVAILABLE AND SELECTED. Needs no
                          comparison set at all. See the Generators line below.

**Written:**         ALONE (default). No co-write. `01` §5.3b's co-write permission is not
                     invoked and no finding in this pass may depend on one.

**Configuration:**   TYPICAL — written alone, no co-write, WARM mode per the standing
                     ratification for the 38-city run.
                     ⚠ ONE DECLARED, RULED DEVIATION, named here so a later reader can tell
                     which technique transfers: Band 5 is declared while `01` §2.2's Band 5
                     distributional machinery is expressly DEFERRED (DR-4). Any finding that
                     would require a spread, a mode, or a sub-location breakdown is therefore
                     OUT OF SCOPE for this pass — not absent from Davis. A later reader
                     transferring this pass's technique to a pass without that deferral should
                     expect the distributional layer to be present there and missing here.
                     (A pass cannot correct for a bias it has not declared.)

**Run mode:**        WARM
**Other cities:**    CLOSED until Step 6
**Own culture material read at:**  NOT YET READ. Opens at Step 0.4 item 6 / Step 5, as a CHECK.
                     `Local_Cultures/Mirny_Subnet/Davis.md` and
                     `Local_Robot_Culture/Mirny_Subnet/Davis.md` were not opened by this reader.
**If COLD:**         n/a — this run is WARM, declared honestly. There is no third mode.

**Provisional assumptions about the parent:**  see §0.6 — six, numbered, with one refusal.

**Generators available:** G1 symbolic substrate (PRESENT, lopsided, corroboration-tier, does
                     not count) · G2 physical & environmental (PRESENT) · G3 function & purpose
                     (PRESENT, one line) · G4 founding condition (PRESENT) · G5 network position
                     (PRESENT, volume REQUESTED) · G6 defining event (ABSENT — recorded null)
                     · G7 real-world inspiration (designation yes, research unbuilt) · G8
                     demographic composition (PRESENT, richest). Six countable against a
                     threshold of three.
**Generators selected:** **G2 · G4 · G8**, with G3 and G5 carried as supporting.
                     WHY, peer-free and from Davis's own material only:
                       · G2 is quantitative and internally verified — the twelve-month table
                         reconciles to its own annual figures (I reproduced both sums myself;
                         see 0.3).
                       · G4 supplies the single sharpest stated input and is derivable from
                         nothing else: a founding population that inherited a documentary
                         record and no living institution.
                       · G8 supplies a measured question that needs no second city to ask or
                         answer: the retention spread and the majority inversion.
                       · G3 is carried, NOT load-bearing — it rests on one line, and the
                         Step −1 pass names that as its own biggest doubt.
                       · G5 is direction-only; its volume does not exist anywhere, so it
                         cannot be primary.
                       · G1 is excluded by rule (corroboration-tier, read LAST; Element half
                         RESERVED under DR-1).
                       · G6 is a recorded null. G7 opens at Step 3.
                     ⭐ THE THREE SELECTED CAN GENUINELY CONFLICT, which is the point of the
                     rule of three: G2 describes physically the least hostile setting the
                     admitted set contains (ice-free ground, out of the katabatic regime, a
                     37-day polar night, fjord access); G4 describes a population that had to
                     learn its own ground from paper; G8 describes a place that began
                     robot-majority and ended human-majority. They do not agree about what
                     kind of place this is, and the disagreement is where the pass should look.

**Reserved decisions this pass must not foreclose:**  six — see §0.5.
```

### The two bands, stated flatly, and the one divergence question left open

Davis's governing population figure is **1,158,314** (Census I). At Band 5 the unit of analysis is a distribution rather than a point — which is precisely the machinery `DR-4` defers. The honest statement of this pass's position is therefore: **the band is declared at 5 and the analysis appropriate to 5 is not performed, by ruling.** A Band 5 pass that reads like a Band 3 pass commits the scale error `00d` and Gate 11 name; a Band 5 pass that *declares* the deferral has not committed it, but it has not escaped it either — it has postponed it. Recorded as postponed.

### Status — the full reasoning, because §3's note says to check the cause before defaulting

```
Census I  (Pre-Orbital)   563,599 H  /  594,715 R  /  1,158,314
Census II (Orbital)       437,423 H  /  344,173 R  /    781,596
```
The fall is **376,718 people**. It has a documented destination inside this setting's own future — the orbital tier, opened at the ~2688 crowding. `01` §3's note is explicit that this is not Declining and that the correct status remains Living. I checked the cause before choosing, as the note requires, and I am recording that I checked.

⚠ **Also recorded, and NOT adopted:** the era README observes that the same structure whose completion solidified a shared national identity is also the structure through which people left, and calls that *national context, true everywhere — therefore never a differentiator.* It then says what **is** differentiating: **how hard a given place used that exit.** Davis has a measured answer to that in its own figures. That is relation and self-measurement, not comparison, and it survives the one-sentence test. It belongs to Phase 2, not to Step 0, and I am not deriving it here.

---

## 0.2 — THE DISCIPLINES: what each obliges THIS pass, at Band 5, concretely

### (a) `00b_General_Population_Discipline.md`

1. Every claim about "what Davis is like" must state the population share it describes before it is allowed to stand, and the *sector* form of the rule binds as hard as the *role* form: **write the sector's general breadth FIRST, before the signature instance exists to be reached for.**
2. **The arithmetic test is mandatory here and is cheap.** L143 says sheltered-agriculture and greenhouse cultivation plus research heritage are "the clear majority of daily activity." At 1,158,314 that is on the order of 600,000 people. Six hundred thousand people feeding a nation is ordinary; six hundred thousand people doing limnology on a lake system is the "entirely based around maintaining a tent" failure at a different address.
3. **The obligation is therefore to WIDEN, never to shrink.** "Research" at this population must mean its whole breadth — instrument maintenance, sampling logistics, data handling, seed and stock records, quality control on a national food chain, teaching, calibration — not one vivid institute. "A prime ecological/limnological research hub" is the signature instance and must be scoped as a specialization *inside* the sector, explicitly.

### (b) `00d_Shadow_Proportion_Discipline.md`

1. Davis's shadow must be a **byproduct of a sincere pursuit that largely works** — unintended, unnoticed from the inside, discoverable rather than announced. Ask **how** it manifests, never **whether** it does.
2. **Check canon for an existing no-villain mechanism before deriving one.** The admitted set already contains a candidate of exactly the required shape: a documentary inheritance with no living teacher (L127). It has no author, no decision and no malice, and its failure mode would be invisible from inside. The pass's job would then be to explain why Davis is the place it happened to — not to invent a parallel.
3. **Scale-check every sanction against Davis's own physical conditions, at Band 5.** Before writing any exclusion-shaped penalty, ask what exclusion physically costs a person **at Davis**, given ~400 km² of ice-free ground, winds out of the katabatic regime, a 37-day polar night and an open harbor. Do not inherit a survivability assumption from anywhere else; compute it from these numbers.
4. And do not scale one institution's behavior into a civic sanction over 1.16 million people — `00d`'s named error, at this location's scale.

### (c) `00f_Review_Panel.md`

1. At Step 7, cast all **six Flat Archetypes** concretely for Davis, plus the **Passer-Through** and the **Neighbor**, always; run the **Lover faculty's** question every time (*is this place alive, and could anyone love it?*) because no other gate asks it.
2. **Six dispositions, not five** — `accepted · noted · rejected · refereed · unmet · declined`. Keep `unmet` for what Davis knowingly protects and would refuse to surrender; use `declined` where the refusal is anti-homogenization and nobody here has the awareness to defend anything. Collapsing them destroys the self-knowledge signal.
3. ⛔ **Use the PEER-FREE form of Rule 3, not the district form.** The `Disciplines/` copy states it as *"would satisfying this make the district more like the other twelve?"* — for a city the binding test is **"would satisfying this objection replace something SPECIFIC TO DAVIS with something that could be true anywhere?"** Strictly stronger, and it catches the generic answer no sibling has written down yet.
4. ⚠ **The Neighbor may not be castable.** Davis's neighbors' conclusion-tier material is closed until Step 6, so the Neighbor can only speak from *relation* — Hwy 110 running in both directions, the Prydz Bay harbor, what flows and in which direction. If no standpoint can be found, **record the un-castability as a result**; `00f` says a position that cannot be cast at all is a finding, and a strong one.

### (d) `Cultural_Synthesis_Techniques.md`

1. Run the techniques as **questions**, not results; **expect several nulls and record them**; a place where all of them fire has been over-written.
2. **Technique 18, The Composition Merge, is fully armed here** — Davis has an origin roster WITH shares (21 entries, L21/L30–52), so the full-run row of the input contract is satisfied and R1–R7 all run. What Step 0 can already say the technique WILL be obliged to read, from the numbers themselves: the leader (China, 19.04%) is a **plurality, not a majority**, so the pass is obliged to look for **accommodation machinery** rather than imposition; #1 at 19.04% against #2 at 9.36% is roughly double, so the lead is **uncontested** and the interesting content is elsewhere; and the remainder is a **long dispersed tail** of thirteen Notable entries under 3.6%, so the default does not get compromised — it **erodes**. R5b's pooling test must then re-read R1 and R2 against any pooled figure, as a **candidate** reading only, never a silent merge.
3. ⛔ **Guard 5 fires on Davis specifically and must be honored.** L54 states the robot figures apply the **same** national-origin proportions as the human population. **The robot/human axis therefore carries zero independent origin signal**, and any per-nation robot-versus-human finding would be an artifact of the method rather than a fact about the place.
4. ⚠ **One open question I am flagging rather than deciding:** whether running technique 18's full R-sequence counts as the "Band 5 distributional analysis" that `DR-4` defers. `DR-4` defers `01` §2.2's thresholds; technique 18 reads an *origin* distribution, which is a different object. I do not supply the criterion. Flagged for adjudication before Phase 2.
5. **Technique 14 runs on every finding** and composes with 18: 18 proposes what a share can structurally sustain; 14 then asks whether the resulting claim is being stated of everybody.

### (e) `Real-World_Basis_Extrapolation_Method.md` (with `LAW 0-R`)

1. **Step 3 must run actual web research on every pick — Primary, Significant AND Notable — from more than one angle each**, must go back to picks already logged as covered, must run and log near-duplicates, and must log dead ends **and whether each died at the query or at the sources**. There is no search budget.
2. **Davis is genuinely un-mined and that is the high-yield condition.** `REQ-G7r` records that no `Davis_Research_Log.md` exists. Technique 13's premise therefore has not yet inverted: "all picks unused" is the safe default here, maximum yield. The pick surface is large — one Primary, seven Significant, thirteen Notable, plus the site's own physical picks (Vestfold Hills terrain, Prydz Bay, and the hypersaline lakes and landlocked marine basins named at L176).
3. ⛔ **GPS stays intact, and the admitted set already performs the refusal correctly.** L127 records that the succession of national operators "isn't relevant to the story" — that refusal must not be walked back, and it covers the site's lineage, abandonment and vacancy, not only its nationality. ✅ **And the unlock applies**: composition IS established (L21, L30–52), so the origin-ethnicities those populations carry ARE admissible material — as **starting stock** run through the divergence operator (time · separation · local environmental setting · local struggles and hardships · local goals · local sensibilities and habits), **as of Act 2**, and never reasoned from elapsed time.
4. **Every pass through Step F must record what came back → which finding it became, and must ask: did this source CHANGE a finding, or ORNAMENT one?**

### (f) `Robot_Physiology_and_Cultural_Practices.md` — the governing universe document

1. **Robots are the majority at the governing census** — 594,715 of 1,158,314, or 51.34%. There is no phase of this pass that is not a question about them, and the human/robot balance is not stable across the frame (it inverts by Census II). Every phase must be written for a population whose majority changes inside the frame.
2. **Overnight recharging gives Davis a shared night.** Robots and humans stop at the same time for different reasons. At Davis that shared clock runs against a **37-day polar night and a 55-day midnight sun**, so for roughly a quarter of the year it is not solar. **Something non-solar holds it, and the pass is obliged to say what** — this is a genuine physical constraint, which `01` §5.2 rule 3 prefers over any provisional inheritance from the unwritten parent. *(Available and unexploited: Davis's solar time is ~UTC+5.2 from its own longitude, recorded at L21 as "distance 0 from Davis's solar UTC+5.")*
3. ⛔ **Cold is a PREPARATION problem, not a species gate.** Never write a robot gated out of Davis's outdoors by her body; write whether she is dressed for it. And take the ordinary trade-off that comes with the garments: **insulation against dexterity**. At coldest-month averages near −21 °C, with lake-ice, fjord and greenhouse work all in the admitted economy, the glove trade-off is a real constraint on what outdoor work is possible at Davis — **a gradient, never a gate**.
4. **Leisure is a condition of remaining sane, and in Tepenia it is owed to nobody.** L143's bars, eateries, general social establishments and small arts and music community are therefore **load-bearing infrastructure**, not color, and must be written as such.
5. **Two mortality curves, not one.** Robot death is episodic (no senescence, no background attrition); human death is continuous. At ~595k robots and ~564k humans that is two entirely different arrival rates in one city. ⛔ The mortuary answer is DEFERRED nationally and RESERVED for this pass — **record the shape, adopt nothing.**
6. ⚠ **Build is statistically weighted by local economic character** — hard-labor locales toward bulkier builds, agility-demanding locales toward slender ones, and locales with no strong lean toward a wide variety with no dominant pattern. Davis's admitted economy (sheltered agriculture plus research) does not obviously lean either way, so the third case may apply. **Flagged for Phase 9; not asserted at Step 0.** NO FORCED FIT: a city whose build distribution has no pattern is a result.
7. ⚠ **Contamination hazard inside required reading — see DEFECTS D5.** The glitch-coolant passage of this governing file states *conclusions* about other named cities' drinking cultures. Davis's own position on the variety/potency axis must be derived from Davis's own economy and never by matching a named exemplar.

---

## 0.3 — RUN GATE 0

**Cheapest gate, highest yield, fails in BOTH directions.** Raw scan output pasted; nothing summarized.

### 0.3.1 — Arithmetic reconciliation of the Step −1 contract's own claims (independently recomputed by this reader)

**Contract §3.3 claim:** *"Hand-verified: all four per-nation columns sum exactly to their totals; shares sum to 100.00%."*

```
Census I ROBOTS column, L32-L52, summed in order:
113234 →168899 →223315 →274758 →317221 →350763 →381331 →410650 →431584 →452459
→472025 →491353 →509968 →527631 →544997 →555642 →565336 →574316 →581750 →589125
→594715
TARGET (L15 / census L496) = 594,715                       ✅ EXACT

Census I HUMANS column:
107309 →160062 →211631 →260382 →300623 →332410 →361379 →389165 →409004 →428786
→447328 →465645 →483286 →500025 →516482 →526570 →535757 →544267 →551312 →558301
→563599
TARGET (L15 / census L496) = 563,599                       ✅ EXACT

Census II ROBOTS column:
65530 →97745 →129237 →159008 →183582 →202993 →220683 →237651 →249766 →261846
→273169 →284355 →295128 →305350 →315400 →321561 →327171 →332368 →336670 →340938
→344173
TARGET (L16 / census L613) = 344,173                       ✅ EXACT

Census II HUMANS column:
83285 →124228 →164252 →202089 →233321 →257992 →280476 →302041 →317438 →332792
→347183 →361399 →375090 →388081 →400854 →408684 →415814 →422419 →427887 →433311
→437423
TARGET (L16 / census L613) = 437,423                       ✅ EXACT

SHARE column:
19.04 →28.40 →37.55 →46.20 →53.34 →58.98 →64.12 →69.05 →72.57 →76.08 →79.37
→82.62 →85.75 →88.72 →91.64 →93.43 →95.06 →96.57 →97.82 →99.06 →100.00
TARGET = 100.00%                                           ✅ EXACT
```
**GATE 0 RESULT, direction "understating a finished piece": the contract's claim is TRUE and I reproduced it independently. Nothing to correct. Recorded as corroboration, not as a new finding.**

**Contract §3.3 claim:** the retention block.
```
781596 / 1158314 = 0.674766…  → 67.48%      ✅ matches "67.48%"
437423 /  563599 = 0.776127…  → 77.61%      ✅ matches "77.61%"
344173 /  594715 = 0.578716…  → 57.87%      ✅ matches "57.87%"
77.61 − 57.87 = 19.74 pp toward humans      ✅ matches "19.74 pp"
```
**Contract §3.3 claim:** *"the majority inverts."*
```
Census I : 594,715 R  >  563,599 H   → robot-majority (51.34% robot)   ✅
Census II: 437,423 H  >  344,173 R   → human-majority (55.97% human)   ✅
```
✅ **VERIFIED.**

**Contract §8 claim:** *"monthly precipitation sums exactly to the stated annual."*
```
1.8 +3.8 +9.1 +10.1 +9.9 +9.1 +8.2 +6.8 +5.4 +4.5 +2.2 +1.9
= 5.6 →14.7 →24.8 →34.7 →43.8 →52.0 →58.8 →64.2 →68.7 →70.9 →72.8
TARGET (L79) = 72.8 mm                                     ✅ EXACT
```

**Contract §8 claim:** *"mean annual temperature reproduces to 0.03 °C."*
```
Mean column (L95-L106): +0.9, −2.2, −8.0, −13.5, −16.0, −15.7, −17.1, −17.1,
                        −15.7, −11.8, −4.2, +0.0
Σ = −120.4 ;  −120.4 / 12 = −10.0333…
TARGET (L71) = −10.0 °C   → |Δ| = 0.033 °C                 ✅ matches "0.03 °C"
```

**Contract `R-7` claim:** *"L85 retention ~45%; computed 38.5% — L86's millimeters reused as a percent."*
```
L84 falls  = ~73 mm/yr   (annual at L79 = 72.8 mm)
L85 lands  = ~28 mm/yr, stated "(~45% retention)"
L86 lost   = ~45 mm/yr
28 / 72.8 = 0.3846  → 38.5%     ⛔ NOT 45%
73 − 28   = 45 mm               ← the "45" is L86's MILLIMETERS
```
⛔ **DEFECT CONFIRMED INDEPENDENTLY. The three millimeter figures are internally consistent; only the "%" label is wrong.** Unresolvable in-pass, as the contract says.

**Contract `R-3` claim:** *"L74 temperature endpoints sit on two columns; warm end is +3.2, not 0."*
```
L74: "coldest months avg −21°C; warmest month avg 0°C"
Avg Low  column extremes : Jul −20.6 , Aug −20.8      → "−21" ≈ the AVG LOW column
Mean     column extremes : Dec +0.0  , Jan +0.9       → "0"   ≈ the MEAN column
Avg High column warm end : Jan +3.2
```
⛔ **DEFECT CONFIRMED INDEPENDENTLY.** The two endpoints are read off two different columns. On a single consistent column the warm end is **+3.2 °C**, not 0. ⚠ **And it is not cosmetic for THIS city**: a growing-season claim built on "warmest month avg 0 °C" understates the warm end by 3.2 °C in a location whose declared function is agriculture.

### 0.3.2 — Cross-source roster reconciliation (`Specs/Davis.md` against `Official_Population_Census.md`)

```
Census L396-398 roster:  Primary: China (1)
                         Significant: Japan, Germany, UK, South Korea, Russia,
                                      Indonesia, Australia (7)
                         Notable: Thailand, Ukraine, Vietnam, Philippines, Malaysia,
                                  Romania, South Africa, New Zealand, Belarus,
                                  Bulgaria, Lithuania, Latvia, Estonia (13)
Spec  L20-22  roster:    IDENTICAL membership, identical tiering, 21 of 21.   ✅
Spec  L30-52  table:     21 rows, same membership.                           ✅
```
⚠ **One trivial ordering difference, recorded and NOT a contradiction:** the roster lines end "…Lithuania, Latvia, Estonia" while the de-stacked table orders Estonia (1.24%) before Latvia (0.94%). The table is sorted by share; the roster line preserves an earlier order. Membership and figures agree exactly.

### 0.3.3 — **NEW DEFECT FOUND. Contract §3's `G2` "Ground" citation spans two of its own FULL strikes.**

```
§3, row G2, Ground column  :  "L60; L70–91; L93–114"
§4.2, strike table         :  "L88–89 | ⛔ FULL | an nth-of-N, a corpus superlative,
                                            and a character verdict"
88 ∈ [70,91]  and  89 ∈ [70,91]              ⛔ the range CONTAINS both strikes
```
⛔ **This is the identical pattern the contract already caught and self-corrected once**, at §2's Tier 0 "Parent" cell, which had cited struck L9 (*"A Tier 0 blocking input was half-sourced to a line this document excludes"*). The self-correction was applied at §2 and the same shape survives at §3. **No content harm — the read spec excludes 88 and 89, so no reader following the numeric spec can open them — but a later reader chasing G2's stated ground by hand would.** Recorded as a defect in the contract, **not fixed**; I edited nothing.

Cross-check of the other seven Ground citations against the read spec: `G1` cites a different file · `G3` L143 ✅ admitted · `G4` L127, L129 ✅ admitted · `G5` L6, L7, L155 ✅ admitted · `G7` L3, L64, L68 ✅ admitted · `G8` L15–22, L30–52 ✅ admitted · Tier 0 L1, L3, L5, L15, L60 ✅ all admitted. **G2 is the only one that reaches a struck line.**

### 0.3.4 — **SECOND NEW DEFECT. A bare line number in §3.1 addresses a different file than every other bare line number in the document.**

```
§3 table, G1 Ground : "`City_Symbol_Assignments.md` **L92**"     ← filename present
§3.1 body           : "Davis's pair: `Earth / Earth` *(L92, column-anchored…)*"
                                                       ↑ filename DROPPED
Specs/Davis.md L92  = blank line (inside the admitted 90-120 segment; I read it)
```
Every other bare `Lnn` in the document means `Specs/Davis.md`. A reader resolving §3.1's bare "L92" against that convention lands on a blank line. Same class as the `M-117` finding the methodology already records — *a name is not an address* — in its milder form. Recorded; not fixed.

### 0.3.5 — The read-spec expansion, verified by hand

```
Claim (§4.1): "1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179"
              = 137 lines, = bound − {4, 9, 88, 89, 121}, zero struck lines.

Segment sizes : 3 + 4 + 78 + 31 + 13 + 1 + 1 + 3 + 1 + 2 = 137           ✅
Bound check   : 134 − |{4,9,88,89,121}| = 134 − 5 = 129
                129 + |{143,148,153,154,155,176,178,179}| = 129 + 8 = 137 ✅
Exclusion check: 1-3 skips 4 · 5-8 skips 9 · 10-87 skips 88,89 ·
                 90-120 skips 121 · 122-134 completes the bound            ✅
```
✅ **The contract's most safety-critical claim is correct.** `LINES: 137`, not 142 and not 181. I report 137 and I read the admitted set as ten separate ranged reads rather than reading the bound and filtering afterward, which is the failure `M-224` records.

### 0.3.6 — Open-questions list checked against what has actually been resolved elsewhere

| Contract item | My independent check | Result |
|---|---|---|
| **`REQ-G6`** — "No in-frame defining event for Davis" | Read the whole Second Interwar `Timeline.md` (562 lines) and `README.md`. **Davis is named nowhere in either.** The dated-event table names Aquarius, Pisces, Libra, Sagittarius, Leo, Taurus, Aries, Capricorn, Scorpio, Cancer; the prose names Palmer City, Cape Adare, Lazar, Concordia, Byrd, Zukelli, Janbogo. | ✅ **The null HOLDS on a second source the contract did not cite.** Strengthened, not overturned. |
| **`REQ-G6`'s un-adjudicated proposal** — "that the orbital migration is itself a `G6` event… not adopted by silence" | ⚠ **The era README supplies the adjudication criterion the proposal needs, and the contract does not cite the README.** The README rules the ~2688 crowding *"national context, true everywhere — therefore never a differentiator"* and then names what is: *"how hard a given place used that exit."* Davis has a measured answer in its own figures. | ⚠ **GATE 0, "understating a finished piece" direction: the standard that would settle this pending item already exists in canon and is uncited.** ⛔ **I am surfacing it, not deciding it** — the contract reserved the adjudication and it is not mine to close. |
| **`REQ-G5v`** — Hwy 110 throughput | Nothing in my admissible set states any volume. L7 gives direction and ordering only; L155 gives the harbor. | ✅ Stands. |
| **`REQ-G7r`** — no research log | Not contradicted by anything in my set. | ✅ Stands. |
| **`R-3`, `R-7`** | Both independently reproduced above. | ✅ Both real. |
| **`R-8`** — "L111 names a superseded column set" | L111 names *Avg Temp · Temp Range · Avg Precip · Precip Probability · Avg Daylight*; the actual table header at L93 is *Rec High · Avg High · Mean · Avg Low · Rec Low · Precip · Precip Prob · Daylight · Notes*. **Confirmed: the provenance note describes a column set the table no longer has.** | ✅ Real. |

### 0.3.7 — Completion claims I could NOT reconcile, and I am recording rather than routing around

- **`Specs/Davis.md` L4 (`Status: Damaged; partially operational`).** Quoted by contract §2.3. **L4 is struck and outside my admissible set; I did not open it.** Unverified by me, deliberately. The rule it invokes is independently sound and I applied it regardless of the quote's exactness.
- **`City_Symbol_Assignments.md` L92 (`Earth / Earth`).** Not in my reading list; not opened. **G1 is known to me only at second hand.** Read-order item 2 is, for this reader, satisfied only by the Step −1 pass's report.
- **"worst row deviation 0.57 of a person"** (§3.3). Requires re-deriving the share-weighting model; not attempted. Unverified.
- **"daylight column reproduces … at RMSE 0.06–0.16 h"** (§8). Not recomputed. Unverified.
- **"Davis is not in the 2026-09-05 −10% redistribution set"** (§2.3). The lines that would establish this are outside the 9-line census contract. Unverified.
- ⚠ **The census rows L496 and L613 are admitted WITHOUT their table headers**, so the column order (humans-then-robots) is not verifiable inside the admitted set. It is recoverable from `Specs/Davis.md` L15–16, which labels both. **No harm here; recorded as a general hazard of ranged census contracts.**

---

## 0.4 — THE MANDATED READ ORDER, item by item

| # | Item | Where read for this pass | Status |
|---|---|---|---|
| **1** | **specs / physical facts** | `Specs/Davis.md`, at the 137-line read spec, **by this reader**, as ten separate ranged reads. Physical spine: ~400 km² ice-free Vestfold Hills; Prydz Bay fjord inlets; freshwater, saltwater, hypersaline lakes and landlocked marine basins; mean −10.0 °C; winds ~5.6 m/s, **out of the katabatic regime**; 72.8 mm/yr falls, ~28 mm lands; **37-day polar night, 55-day midnight sun**; harbor at Prydz Bay; Hwy 110, access type ON. | ✅ **READ IN FULL** |
| **2** | **symbol assignment** | `City_Symbol_Assignments.md` L92 — **NOT in this reader's list; NOT opened.** Known second-hand: pair `Earth / Earth`; Planet half ratified and readable; **Element half pulled back from canon and RESERVED under `DR-1`**; `G1` is corroboration-tier by rule and read LAST as a check. | ⚠ **READ BY THE STEP −1 PASS, NOT BY THIS READER** |
| **3** | **composition, census, and population change across snapshots** | `Official_Population_Census.md` L392–398 (21-entry origin roster), L496 (Census I), L613 (Census II); plus `Specs/Davis.md` L15–22 and the 21-row per-nation table L30–52 with its two scope caveats at L28 and L54. **Both snapshots read; the change between them read; all five columns reconciled by hand.** | ✅ **READ IN FULL** |
| **4** | **founding and events** | Founding: `Specs/Davis.md` L127 (settled post-Falkland Treaty on existing station infrastructure; documentary inheritance, no living institution), L129 (founding population: Australian exiles), L131 (the name; explicitly **not** a Saint in the Tepenian framework). Events: the Second Interwar `README.md` (the Acts; the ~2688 crowding; the four qualifications on the Tower) and `Timeline.md` in full (all beats, the dated-events index, the open work). | ✅ **READ IN FULL** — and the result is a confirmed null: **no Davis-specific dated event exists in the era timeline.** |
| **5** | **the sibling set's differentiation instrument** | EXISTS. ⛔ **NOT READ, BY RULE, not by omission.** A ULM/CST/RWBEM city pass is **WRITE-ONLY** on its differentiation table — it adds Davis's own column and never reads another's. Other cities' conclusion-tier material stays CLOSED until Step 6; Gate 6 runs late, at Step 7. Reading it now would leave that gate with nothing independent to test. | ⛔ **CORRECTLY UNREAD** |
| **6** | ⛔ **LAST — this location's own completed culture material** | `Local_Cultures/Mirny_Subnet/Davis.md` · `Local_Robot_Culture/Mirny_Subnet/Davis.md` | ⛔ **NOT YET READ. OPENS AT STEP 5, AS A CHECK, NEVER AS AN INPUT.** A match will be corroboration; a mismatch will be a finding site. Neither file was opened by this reader at any point. |

⚠ **AND ONE STANDING REQUIREMENT OF THIS STEP IS UNMET.** Both `Run_Modes_Warm_and_Cold.md` §2 and `00_RUNBOOK.md` Step 0.4 require checking **`06_Worked_Example_Provenance.md`** for THIS location's own worked example **before Step 0.2**, and say to treat any hit as read-last material. **That file is absent from the Step 0 reading list and I did not open it.** Recorded as an unmet standing requirement, not closed — I am not authorized to widen my own contract.

---

## 0.5 — RESERVED DECISIONS, and what would foreclose each

**⛔ Rule for all six:** if material bearing on one turns up anyway, write it as a **numbered finding, marked reserved** — what was found, what it would decide, and that it is explicitly not adopted. A parenthesis is lost; a reserved finding is a handoff.

### 1 · Proper names of people — **permanent**
**What would foreclose it:** naming any archetype, however lightly — a nickname, a title-with-a-name, a "so-and-so who keeps the lake records." Also the indirect routes: **naming a building, a street, a festival, a boat or a greenhouse after a person invents that person**; and quoting an in-world saying attributed to someone.
⚠ **The specific trap at Davis:** L131 names John King Davis and states he is **not** a Saint in the Tepenian framework. Writing any in-world veneration around him — a captain's day, a navigator's oath, a mariners' guild — would both invent people and practices AND import a real-world figure as a **cause**, which the GPS law forbids independently. **Role archetypes only.**

### 2 · The demonym
**What would foreclose it:** any sentence of the form *"Davisians do X."* And the subtler route, which is the one that actually happens: **ordinary-life prose needs a word for the people and reaches for one.** An adjectival form forecloses as surely as a noun — *"Davis-born"* is safe, *"Davisan agriculture"* is not. **Use "residents of Davis" or "people here."**

### 3 · Which DLC covers the Mirny subnet
**What would foreclose it:** naming a quest, attaching a beat to an act, stating that Davis is or is not a playable location, or implying its content is base-game. And the reserved-slot route: **every subnet DLC reserves one romanceable companion**, so sketching a romanceable local archetype edges toward spending that slot.
⚠ **This one is in live tension with another instruction I was given** — `Cultural_Synthesis_Techniques.md` §0b pushes every finding toward quest hooks, reputation and companion reaction. **Resolution I applied and am declaring: write player-facing EXPRESSION — seen, heard, entered, handled, spoken, done — and never a delivery vehicle.** Recorded in DEFECTS as a collision the methodology does not name.

### 4 · Disposal of the dead
**⭐ The biggest foreclosure risk in the set, because canon supplies a rich, ruled national answer that is trivially localizable.** The robot-physiology file rules the Tepenian ossuary **mixed** (metal and calcium together), **sacred and untouchable**, and answers the permafrost problem — and then **explicitly DEFERS** the general human case and the two-mortality-curve assembly problem.
**What would foreclose it:** siting an ossuary at Davis; saying Davis holds a human's remains until the robot dies; saying Davis does it some other way; or **saying Davis has no ossuary.** All four decide it.
⚠ **A structural safeguard fell out of 0.1 by accident and is worth naming:** `01` §1.2 says a sealed or `Enclosed` location *"will usually find its disposal-of-the-dead question sitting here, unanswered."* **Davis carries no `Enclosed` modifier** (§0.1's docket), so the question does not arrive through the type line. It can still arrive through the permafrost fact, which IS in my admitted reading. **Refuse it there.**

### 5 · `G1`'s Element meaning — `DR-1`
**What would foreclose it:** any finding that cites what the Element "Earth" means. `02` §6.0 requires symbol definitions be read *from the system's own files, never from the names* — and for the Element half that file is no longer canon, so the instruction **cannot** be satisfied and reading meaning off the bare word is exactly what it forbids.
⭐⭐ **FLAGGED LOUDLY, because this is the single most seductive unearned finding available in this pass.** **Davis is an agricultural city sitting on 400 km² of exposed rock, and its Element is the word "Earth."** The resemblance is free, vivid, and completely unearned. **Even noting the resemblance as a coincidence risks seeding it into a later phase.** ⛔ No finding may rest on it. The Planet half (Earth, hand-authored, ratified) is readable — but `G1` as a whole is corroboration-tier, read last, and **may not seed anything.**

### 6 · Early-Federation currency, Davis's or the subnet's — `DR-3`
**What would foreclose it:** writing any price, wage, rent, tax, tariff, fee, or "what a thing costs." **And the negative route forecloses it just as hard** — writing *"Davis trades in kind"* or *"nobody here uses money"* decides the same question.
⚠ **One specific trap, named:** `Cultural_Synthesis_Techniques.md` technique 10's conversion-mechanism table offers **"Credit or debt based — having cleared a first obligation, or been extended one."** Choosing that row for Davis's membership mechanism forecloses currency through the back door. **Refuse that row specifically.**
✅ **What IS recordable and should be:** what Davis **values and trades** — goods, obligations, standards of worth, what flows out and what it needs in. Never denominated value.

---

## 0.6 — PROVISIONAL ASSUMPTIONS ABOUT THE UNWRITTEN PARENT

**Parent: the MIRNY Arcanet subnet. No ULM pass exists for it.** `01` §5.2 requires these stated explicitly and numbered, requires every dependent finding tagged with the assumption it rests on, prefers cheap-to-revise assumptions, prefers **local physical constraint over provisional inheritance wherever the choice exists**, and forbids building the location's single strongest finding on one.

**First, what is NOT provisional — stated so it is not mistakenly tagged:**
- **Davis's membership in the Mirny subnet is CANON, not assumed.** It is carried independently by `Specs/Davis.md` L5 and by **both** census rows (L496, L613). The spec's own L5 records that an earlier "Mawson" entry was corrected against those two sources. Three-way agreement.
- **Davis's position on Hwy 110 and its access type are canon** (L6, L7), as is the Prydz Bay harbor (L155).

**The numbered provisional assumptions:**

1. **The Mirny subnet supplies Davis's Arcanet connectivity as a parent-level service.** *(Cheap to revise. Nothing admitted states what a subnet provides; only that Davis is in one.)*
2. **The subnet is an administrative and network unit, not a cultural one** — it routes and coordinates rather than producing an identity Davis inherits. *(Cheap. Follows the era README's "differentiate locally; converge nationally," but the README is a NATIONAL statement and I am extending it one tier down, which is the provisional part.)*
3. **Hwy 110's maintenance, scheduling and priority are set above Davis.** *(Cheap. L7 gives direction and ordering, never who runs it. Any finding about Davis's control over its own road access rests on this.)*
4. ⚠ **The calorie demand that makes Davis "Tepenia's breadbasket" (L143) is levied by a tier above Davis — but WHICH tier is unknown.** L143 says *Tepenia's* breadbasket, which points at the national layer; the subnet is the intervening one and is unwritten. **This matters: it decides whether Davis's food obligation is a subnet relationship or a national one, and therefore who Davis actually answers to.** *(Moderately expensive to revise — several Phase 5 and Phase 7 findings would move with it. Tag every dependent finding.)*
5. **National-tier facts reach Davis through the national layer, not through the subnet** — the Grand-Timeline Acts, the ~2688 Tower completion and its four qualifications, the opening of the orbital tier, universal robot physiology, leisure as a fact of life owed to nobody, the egalitarian-skewed-toward-robots baseline. *(Cheap, and well-supported: the era README and the robot-physiology file both state these as universe-wide.)*
6. **The subnet does not itself supply Davis with a form for anything Davis lacks.** *(Cheap, and deliberately WEAK — it is a null assumption held only so that a gap found at Davis is not silently attributed upward. It must be revisited the moment the parent is written.)*

**⛔ ONE ASSUMPTION EXPLICITLY REFUSED, and the refusal recorded as a result:**
> It would be convenient to assume **that the subnet's other cities do not duplicate Davis's function**, because that would make Davis's breadbasket role structurally necessary rather than merely stated. **I refuse it.** It is a claim about other cities, their conclusion-tier material is CLOSED until Step 6, and adopting it would smuggle a comparative premise into a peer-free pass. **Davis's function stands on L143's own authority or it does not stand at all.**

### `01` §5.2 rule 4 — the spine is parent-independent, and I checked

The two strongest candidate findings in the admitted set are:
- **G4's documentary inheritance without a living institution** (L127) — rests on Davis's own founding line. Touches no assumption above.
- **G8's retention spread and majority inversion** (19.74 pp; robot-majority → human-majority) — rests on the census. Touches no assumption above.

✅ **Neither rests on any provisional assumption about the unwritten parent.** `01` §5.2 rule 4 is satisfied, and I am recording that I verified it rather than asserting it. The parent-dependent material (assumption 4, who levies the calorie demand) sits under **G3**, which the Step −1 pass already grades as its biggest doubt — so the two weaknesses coincide, which is worth knowing and is better than having them in different places.

### `01` §5.2 rule 3 — physical constraint preferred, and where I applied it

Where a Step 0 call could rest either on a provisional parental fact or on a local physical constraint, I took the constraint:
- **The shared night.** Robot overnight recharging gives Tepenia a shared night (national, determined). What makes Davis's version its own is the **37-day polar night and 55-day midnight sun** — latitude, not policy. The ice sheet will not be retconned; a subnet's timekeeping convention might be.
- **Climate as a whole.** `01` §5.1 says a child does not have its own climate — the parent determines it. **At Davis the determiner is latitude and terrain, not the Mirny subnet.** That distinction is worth keeping: Davis's climate is `Determined`, but by the planet.
- **Survivability of any sanction.** Computed from ice-free ground, non-katabatic wind and a 37-day night, never inherited.

### `01` §5.2 rule 5 — registration, flagged not done
The assumptions above must be registered where the Mirny subnet's eventual pass will see them; an assumption recorded only in the child's file is an assumption the parent will contradict. **I edited nothing and therefore registered nothing.** Recorded as an outstanding obligation of this pass.

---

## APPENDIX TO 0.6 — `01` §5.1's FOUR INHERITANCE CLASSES, where Step 0 can already see them

> ⚠ **`M-157`: this instrument is ACT-BLIND. A classification made once has been made for an UNSTATED DATE.**
> **Every call below is made AS OF ACT 2**, because the declared frame is mostly Act 2 (Act 1 ≈ the first 18% of 248 years). The Act 1 reading differs and is stated where it differs. Per M-157, the `Determined` class **widens** across the boundary — by Act 2 a shared identity is among the things the parent supplies — so `Inflected` and `Originated` **narrow**, and any call that looks Originated in Act 1 must be re-asked in Act 2.

| Class | Element | As of Act 2 | As of Act 1 (where it differs) |
|---|---|---|---|
| **Determined** | **Climate** — mean −10.0 °C, 37-day polar night, 55-day midnight sun, non-katabatic wind, 72.8 mm/yr | ✅ Fixed. **But by latitude and terrain, not by the parent polity.** Davis has no say and neither does Mirny. | identical |
| **Determined** | **Robot physiology** — engine power, thermal regulation, siligel (energy first, repair second), coolant, overnight recharging, no senescence, what counts as death | ✅ Universe-wide. | identical — physiology is act-blind |
| **Determined** | **Shared national identity — "properly Tepenian; origin is ancestry, not identity"** | ✅ **Supplied from above.** This is exactly the class-widening M-157 warns about. | ⛔ **NOT determined in Act 1** — people are still *"X who live in Antarctica."* A pass that writes Act 1 Davis with an Act 2 identity has written the wrong Act. |
| **Determined** | **Currency** | ⛔ **NOT a class call — RESERVED by `DR-3`.** Recorded here so nobody assigns it a class by default. | same |
| **Determined** | **Calendar** | ⏸️ **EMPTY SLOT, stated as such.** Nothing in the admitted set establishes a Tepenian calendar. "None is established" must not read as "none exists." | same |
| **Inflected** | **Leisure** | ✅ **The workhorse call.** The form is national and non-negotiable — leisure is a condition of sanity, owed to nobody, the material proof that leaving worked. **Davis's version is L143's**: bars, eateries, general social establishments, a small arts and music community, libraries that welcome smuggled books. | Act 1 leisure is the same fact, but its *forms* would still be carried rather than local. |
| **Inflected** | **The shared night** | ⭐ **The strongest Inflected candidate, and it rests on physical constraint.** National form: everyone stops at once. Davis's inflection: for ~92 days a year the sun does not supply the cue, so something else holds the clock — and the pass owes an answer. | identical constraint; different answer, since Act 1 Davis is 40-odd years old |
| **Inflected** | **Glitch-coolant** | ✅ Class is clear: national institution, local position on a variety-versus-potency axis. ⛔ **Position left explicitly OPEN** — it must be derived from Davis's own economy and never by matching a named exemplar city. See DEFECTS D5. | same |
| **Inflected** | **Ossuaries and disposal of the dead** | ⛔ **Class noted; NOTHING DERIVED.** RESERVED (§0.5 item 4). | same |
| **Inflected** | **Language** | The mechanism is Determined (the Language Module tracks the dominant local culture and the community who commissioned the build); the **value** at Davis is Inflected. | ⛔ **Act-sensitive and this is where it bites:** Act 1 → origin languages fresh; Act 2 → Tepenian, with origin as ancestry. |
| **Originated** | **The exiles' own practical mastery of the Vestfold Hills terrain** | ⭐ **The strongest Originated candidate, and it is STATED rather than inferred** — L127: they built it "independently, over generations of their own," because the documentary inheritance carried no living teacher. | This is a *process* spanning both Acts: begun in Act 1, mature by Act 2. |
| **Originated?** | **Sheltered-agriculture and greenhouse technique at continental scale** | ⏸️ **CANNOT BE DECIDED AT STEP 0.** It may be Originated, or it may be Davis's inflection of a national agricultural form. Nothing admitted settles it. Flagged. | same |
| **Aggregated** | The Mirny subnet's own character as the sum or tension of its children | ⛔ **STRUCTURALLY UNAVAILABLE at Step 0.** The parent is unwritten and the siblings are closed. **Recorded as unavailable, not as absent** — and flagged as the class most likely to be mis-assigned later, since a subnet's character will feel inheritable once it exists. | same |

> ### ⛔ A STRUCTURAL LIMIT ON EVERY `Originated` CALL IN THIS PASS
> `01` §5.1 says `Originated` material **"must be differentiated against siblings."** The ONE LOCATION law moves all sibling comparison out of the per-location pass and into a **terminal** check on the finished corpus. **So `Originated` cannot be validated at the moment it is assigned.** Every Originated call this pass makes is **provisional by construction**, and the methodology does not say so. Recorded in DEFECTS as D12.

---

# PART III — DEFECTS AND DOUBTS

*The recording law asks for snags, blockages, dead ends, killed findings and self-corrections, not just successes. Everything below is recorded. **Nothing below was fixed — I edited no repository file.***

### D1 · `01` requires an extent band and supplies no extent scale
`01` §2 opens *"Declare two numbers, not one,"* calls the pair *"the single most consequential declaration,"* and §6's template carries an `**Extent band:** <0-6>` line. **But §2.1's band table defines only POPULATION thresholds.** There is no extent metric anywhere in the file — no area, no footprint, no density. So an extent-band declaration has nothing to anchor to, and §2's *"when they diverge, the divergence is characterizing"* cannot be evaluated. **I declared the conservative value (matching) and named the problem rather than widening the set myself.**

### D2 · The Step −1 contract declares no extent band at all
§2's Tier 0 table carries population magnitude and not extent. The verdict at §8 says *"Tier 0 complete"* — and by the contract's own four-input definition of Tier 0 it **is** complete — but `01` §6's frame block requires a band that Step −1 never produced, and `Extent_and_Density_Per_City.md` (which RWBEM Step D row 1 calls **HARD CANON**, outranking everything including the pass) is not in the Step 0 reading list either. **Gate 0, overclaiming direction: a required frame-block line has no source in this pass's admissible set.** Recorded as a REQUESTED-shaped gap.

### D3 · Two required-reading files disagree about `City_Vision_Notes/`
`Real-World_Basis_Extrapolation_Method.md` Step D's read-target table, row 2, names `City_Vision_Notes/<City>.md` as **"⭐⭐⭐ AUTHORIAL VISION — PRIMARY AND UPSTREAM… ⛔ NEVER treat as a derived conclusion."** The Davis contract §4.3 records `City_Vision_Notes/` as **struck corpus-wide** by ruling `00.1a`. **A binding methodology file in my mandated reading instructs me to treat as primary-and-upstream a source another binding ruling has struck.** I followed the later, more specific ruling. **RWBEM still carries the superseded instruction and will mislead the next reader who opens it.**

### D4 · `Cultural_Synthesis_Techniques.md` §0b and the DLC reservation pull against each other
§0b tells every finding to reach for a channel — *hooked (quest, check, reputation, companion reaction)* — and says a finding that can only be read about is weak. **"Which DLC covers the Mirny subnet" is RESERVED, and every subnet DLC reserves one romanceable companion.** The push toward hooks and the reservation collide at exactly the granularity where a DLC gets decided. **The methodology does not name this collision.** My resolution, declared: write the **expression** (seen / heard / entered / handled / spoken / done) and never the **delivery vehicle**.

### D5 · ⛔ A governing universe document carries closed-tier content into a mandated Step 0.2 read
`Robot_Physiology_and_Cultural_Practices.md` is required at Step 0.2 and is a governing document for the whole universe. Its glitch-coolant section states **conclusions** about named cities' drinking cultures — characterizing them as bohemian or cosmopolitan, as working-class, as *"a direct, unpretentious blue-collar drinking culture, not a refined one."* `Run_Modes_Warm_and_Cold.md` §3 puts other cities' **conclusions** in the CLOSED column until Step 6, while their attributes stay open. **These are conclusions, not attributes, and they arrive inside mandated Step 0.2 reading with no warning attached.** The same file also names cities in its fabrication-chamber, human-forbidden and leisure-gradient passages. **I read it as required, and I am declaring the exposure rather than pretending it did not happen.** Concrete consequence I have imposed on myself: **Davis's position on the variety/potency axis is left explicitly OPEN and must be derived from Davis's own economy, never by matching an exemplar.**

### D6 · Ranged census contracts admit data rows without their headers
L496 and L613 are admitted; the table headers that name the columns are not. Inside the admitted set, *"563,599 | 594,715"* has no labels. It is recoverable from `Specs/Davis.md` L15–16 — **so no harm at Davis** — but a ranged census contract that admits rows and withholds headers is a general hazard, and the recovery only worked because a second source happened to be admitted.

### D7 · `R-7` independently confirmed — the retention percentage is a unit error
28 / 72.8 = **38.5%**, not the stated ~45%. The "45" is L86's **millimeters** (73 − 28 = 45 mm lost) reused as a percent. The three millimeter figures are internally consistent; only the label is wrong. **Unresolvable in-pass, as the contract says.**

### D8 · `R-3` independently confirmed — and it is not cosmetic for an agricultural city
L74's *"coldest months avg −21 °C; warmest month avg 0 °C"* reads its two endpoints off two different columns (Avg Low for the cold end; Mean for the warm end). On a single consistent column the warm end is **+3.2 °C** (Jan, Avg High). **A growing-season claim built on "warmest month avg 0 °C" understates the warm end by 3.2 °C in the one city whose declared function is food.**

### D9 · A standing Step 0 requirement is unmet, and the file is not in the reading list
`Run_Modes_Warm_and_Cold.md` §2 and `00_RUNBOOK.md` Step 0.4 both require checking **`06_Worked_Example_Provenance.md`** for this location's own worked example **before Step 0.2**. **It is absent from the Step 0 reading list and I did not open it.** Unmet; recorded; not closed by me.

### D10 · Read-order item 2 was satisfied second-hand
`City_Symbol_Assignments.md` is mandated as item 2 of the read order and is not in my contract. **G1 is known to me only through the Step −1 pass's report.** I did not open the file — correctly, since it was not in my contract — but the read order's item 2 is, for this reader, an assertion rather than an observation, and that should be visible.

### D11 · The `Disciplines/` copy of `00f` carries only the weaker, district form of Rule 3
`00f` §7 Rule 3 states the anti-homogenization test as *"would satisfying this make the district more like the other twelve?"* The project supplies a **strictly stronger peer-free form for cities** — *"would satisfying this replace something specific to this place with something that could be true anywhere?"* — which catches the generic answer no sibling has written down yet, and which a sibling-based test cannot see coming. **A reader working from `Disciplines/00f` alone would run the weaker test on a city.** The `Disciplines/` copy is the one Step 0.2 mandates.

### D12 · `Originated` cannot be validated at the moment it is assigned
`01` §5.1 requires `Originated` material to be *"differentiated against siblings."* The ONE LOCATION law moves every comparison instrument out of the per-location pass into a terminal check. **The two instructions cannot both be satisfied in-run.** Consequence: every `Originated` call in this pass is provisional by construction. The methodology says neither that this is so nor what to do about it. I have marked mine provisional.

### D13 · ⛔ KILLED FINDING — the `Resettled` modifier
I considered assigning `Resettled` on the strength of L127: a second population inheriting journals, logs and orientation manuals from prior occupants, and inheriting no living knowledge. `01` §1.2 even nudges toward it (*"commonly assigned and systematically under-used — check every location carrying it"*). **Killed.** The "first population" here is the real site's operator chain, and the GPS law makes a site's **lineage, abandonment and vacancy** a coordinate rather than a cause. Assigning the modifier would promote site lineage into a structural fact about the city. **Nothing is lost:** the substance sits in `G4`, where the contract already puts it, and it is sharper there.

### D14 · ⛔ KILLED FINDING — `Settlement + Installation`
I considered the dual assignment `01` §1.1 recommends for *"anywhere founded as an installation and now inhabited as a home,"* since Davis was settled on existing station infrastructure (L127) and since G3 names a real tension — *on its own terms a research community; what the polity above it needs, food.* **Killed.** `01` §1.1's Installation test requires **a controlling institution** and a population **staffed rather than settled**; neither is established in the admitted set, and the installation phase belongs to the site's real-world history, which is GPS-only. **The tension is real and belongs to the capability reading, not to the type line** — recorded so a later phase picks it up there.

### D15 · DOUBT — the countable-generator total is softer than "six" reads
The contract counts **G7** toward the six countable generators while grading it *"designation yes, research unbuilt,"* and separately files `REQ-G7r` recording that no research log exists. **A generator whose content does not yet exist is counted toward a threshold.** Nothing turns on it — five remain (G2, G3, G4, G5, G8) against a threshold of three — but "six countable" reads stronger than it is.

### D16 · ⭐⭐ FLAGGED HAZARD — the `Earth / Earth` coincidence
**Davis is an agricultural city on 400 km² of exposed rock and its `G1` Element is the word "Earth," whose meaning is RESERVED under `DR-1` because the file that would define it has been pulled back from canon.** The apparent fit is free, vivid and completely unearned, and `02` §6.0 forbids reading a symbol's meaning off its name. **This is the most seductive unearned finding available anywhere in this pass, and the fact that it looks *obvious* is exactly what makes it dangerous.** Flagged so a later phase does not walk into it, and flagged *as a hazard* rather than *as a resemblance*, since even recording the resemblance approvingly would seed it.

### D17 · Gate 0 recurrence — the contract self-corrected a pattern once and the same pattern survives elsewhere in the same document
§2's Tier 0 "Parent" cell was corrected on 2026-09-13 because it cited struck L9. **§3's `G2` Ground column still cites "L70–91," which contains the FULL strikes at L88–89.** A defect class caught and fixed at one site, unpatched at another site in the same file. (Full evidence at 0.3.3.) And relatedly, §3.1's bare "L92" addresses a different file than every other bare line number in the document (0.3.4).

### D18 · DOUBT, carried from the contract and independently shared — `G3` rests on one line
`L143` is the only text in the admissible set that says what Davis is **for**, it sits inside a range a prior pass refused wholesale on a heading, and the adjudication that would delete it has already been made once without anyone noticing what it cost. **I read L143 myself and confirm it carries the whole of G3.** I also confirm it is a **partial strike** — *"in a way no other city can match"* and the four-city smuggling roster are not usable — so the line that carries the entire function generator is also a line that must be quoted carefully. **This is the pass's thinnest load-bearing input and I agree it is the biggest doubt.**

### D19 · An open question I am flagging rather than deciding
Does technique 18's R-sequence (The Composition Merge) fall inside the "Band 5 distributional analysis" that `DR-4` defers? `DR-4` defers `01` §2.2's population thresholds; technique 18 reads an **origin** distribution, which is a different object, and it is fully armed by Davis's own roster. **I do not supply the criterion.** Flagged for adjudication before Phase 2.

---

**End of Reader C output.** No repository file was modified. No file outside the 15-entry contract was opened. `graphify` was not invoked.


---

# ROUND 3 — CROSS-CHECK A

# DAVIS — STEP 0 (FRAME) — T8 ROUND 3 · CROSS-CHECKER A

**Written 2026-09-14. No repository file was edited. This file is my only write.**

**Identity assumption, stated so the HOLD/MOVE labels can be read correctly:** I take Cross-Checker A to be
Reader A, and I treat the positions in `davis_step0_readerA_proof.md` as my Round 1 positions. If that mapping
is wrong, read every HOLD/MOVE below as relative to Reader A's declared positions rather than to my own.

**Scope.** Three contested fields only. Every other field of the frame declaration is settled and I did not
reopen it. I did not re-litigate whether any reader read the material — Round 2 settled that.

**Method.** I read all three Round 1 outputs, then re-opened by direct `Read`, at absolute paths:
`01_Frame_Typology_and_Inheritance.md` (full, in two passes), and `00_RUNBOOK.md` L2416–2479. I did not need to
re-open `Run_Modes_Warm_and_Cold.md` or `Specs/Davis.md` — no contested field turned on a line in either that
the three readers disagree about, and all three readings of the relevant Davis lines were verified byte-exact in
Round 2. **`graphify` was not invoked and no repo-wide search was run.** The `PreToolUse` hook fired on every
read; disregarding it is this brief's instruction, not my own judgment.

**Every rule quoted below I read myself, in this round, at the cited file and section.** Where I rely on a quote
I could not verify inside my own read permissions, I attribute it to the reader who quoted it rather than
asserting it. That applies to exactly one item, marked at Field 2.

---

# FIELD 1 — TYPE MODIFIERS: is `Resettled` assigned?

## Verdict

**NOT ASSIGNED. `Settlement`, zero modifiers.** Readers B and C are right and I was wrong.

## The rule I am deciding on

`01_Frame_Typology_and_Inheritance.md` §1.2, the table's preamble and the `Resettled` row, quoted exactly:

> ## 1.2 The modifiers
>
> Each adds obligatory questions. A location may carry several.

> | **Resettled** | What did the second population inherit, misread, or fail to notice about the first? *(Commonly assigned and systematically under-used — check every location carrying it.)* |

And the law that governs a slot nothing fits, `CLAUDE.md`'s standing statement of it, whose full text `01` and
the ULM runbook carry:

> **NO FORCED FIT — AN EMPTY SLOT IS A RESULT, NOT A GAP.** … **Never force a location, community or society
> into a category it does not naturally occupy — and the error runs BOTH ways** … **Write what the place
> actually has — a stake, a compact, a debt, a standard of worth — as what it is, without promoting it into the
> empty category.**

## HOLD or MOVE

**MOVE.** I assigned `Resettled` in Round 1, scope-narrowed to L127's documentary inheritance. Four things
changed my mind, in descending order of weight.

**1. I misread the parenthetical, and it is the parenthetical my whole assignment rested on.** I treated
*"commonly assigned and systematically under-used — check every location carrying it"* as pressure toward
assigning the modifier, and wrote in Note A that *"the recorded failure mode for this modifier is under-use, not
over-assignment."* **That inverts the sentence.** *"Commonly assigned"* says the modifier is handed out
frequently — so under-**assignment** is precisely not what the flag reports. *"Under-used"* therefore has to
mean its obligatory questions go unworked, and the instruction that follows confirms it: **"check every
location *carrying* it"** — an audit of locations that already have the modifier, not a recruitment drive for
locations that do not. A sentence cannot mean both "commonly assigned" and "not assigned often enough." Read
correctly, §1.2's flag is an instruction to make assigned instances do work, and it supplies **zero** pressure
toward assigning it here. With that pressure removed, the thing holding my Round 1 call up is gone.

**2. My scope-narrowing deleted the question's own object, which means it was no longer this modifier.** §1.2's
preamble states the whole purpose of a modifier in one line: *"Each adds obligatory questions."* The question
`Resettled` adds is about **the first** — *"what did the second population inherit, misread, or fail to notice
**about the first**?"* My narrowing reframed it as "what does a community learn from paper that it would not
learn from a teacher," which has no first population in it at all. I removed the object of the obligatory
question and then assigned the modifier that exists to force that question. **A modifier whose question has had
its subject amputated is not being narrowed; it is being replaced with a different question that the modifier
does not license.**

**3. My stated cost of declining is factually wrong, and I can check it against my own block.** Note A justifies
the assignment on the ground that declining *"would suppress L127, an explicitly KEPT Tier 1 input."* It would
not. **L127 is seated at G4 (founding condition), which my own Round 1 block selects as one of the three
primary generators** — I wrote there that G4 is *"the sharpest single input this location supplies."* All three
readers select G4. So the material is load-bearing in the pass with or without the modifier, and the modifier
adds no carriage of it. B's statement of this is exactly right: *"The material itself loses nothing — it is
already seated at `G4`, where the input contract puts it and where it belongs."* The "misread" half I called
"the richest thing the modifier offers" is likewise reachable from G4 crossed with G2, which is where I
actually derived it from in Note A — from Davis's physical inventory, not from any predecessor.

**4. My own block is internally inconsistent on this word, and I did not notice.** `01` §3's Status taxonomy
carries a `Resettled` row with substantially the same question — *"What did the second population inherit and
misread?"* — and I declared **Status: LIVING**, declining `Resettled` at the status level by silence. Reader B
declined it explicitly at both levels. **I resolved the same two words two different ways on one set of facts,
in one block, and gave a reason in only one direction.** Whatever the right answer is, my Round 1 block cannot
be it.

**What I do not concede.** B's flat claim that *"there was no first population"* is stronger than the admissible
set supports — the admissible set is silent on the question, and "silent" is not "no." That does not rescue my
position: it makes it worse. If the only way to establish a first population is the real site's occupancy
record, then the modifier's question can only be discharged from material the GPS law excludes as a cause, an
identity and a history — and the memory record shows this project flagged that exact trap and walked into it
hours later on this same file family. **An obligatory question answerable only from excluded material is an
obligation that cannot be discharged, and assigning a modifier to create one is the forced fit the law names.**

**What Davis actually has, stated as itself per NO FORCED FIT:** a **first settlement on second-hand
infrastructure, inheriting a documentary record with no living teacher.** `01` §1.2 has no entry for that, the
slot stays empty, and the empty slot is the result. B's formulation is the one to carry forward.

## What the losing reading would cost, concretely, in this pass

- **A standing GPS invitation across eleven phases and the Review Panel, with no offsetting yield.** The
  modifier's own text points every later phase at "the first" — and the first is the forbidden object. I wrote
  that guard into Note A myself and called the modifier *"the single likeliest route to a GPS violation in later
  phases."* A guard written next to an assignment is weaker than not making the assignment: guards are read
  once, at Step 0; the modifier is carried into every phase that reads the block.
- **It would recast Davis's founding as inheritance rather than as first-settlement**, which is the blander of
  the two and blander in a specifically GPS-shaped direction — a place characterized by whose site it occupies
  rather than by who lives there, which is the precise failure the culture/ethnicity law exists to prevent.
- **It buys nothing.** Both halves of what I claimed for it are already carried by selected generators.

## Condition attached to my own verdict

Declining the modifier is only safe if the L127 material stays explicitly load-bearing. **The final block must
state, in prose, that the documentary-inheritance-without-a-living-institution finding is seated at G4 and is a
primary input** — otherwise the modifier's removal quietly takes the finding's visibility with it, and that is
the one real risk in B and C's reading. B's block already does this. Keep it.

---

# FIELD 2 — EXTENT BAND

## Verdict

**UNDETERMINED**, filed as a REQUESTED input naming the file and the step at which it resolves. Readers A and B
are right; Reader C's `5` should not be carried.

## The rules I am deciding on

`01_Frame_Typology_and_Inheritance.md` §2, opening:

> **Declare two numbers, not one:** the **population band** and the **extent band**. They usually match. **When
> they diverge, the divergence is characterizing** and should be written as a finding — a corridor with no
> residents spanning a subnet, a megastructure housing forty people and visible from orbit, a polity of millions
> administered from one room.

`01` §2.1, the band table's column headers, quoted exactly and completely:

> | Band | Population | What the unit of analysis is | The district methodology's assumptions |

`01` §6, the template line:

> **Extent band:**     <0-6>   [note if it diverges from population band, and why that matters]

And `01` §6's closing sentence, which is why an unsourced value in this block is expensive:

> **The block is not bureaucracy.** Every line of it changes a later question, and four of the seven substantive
> errors the developer has caught in this project were scale, scope, or frame errors that a declaration block
> would have made visible before the writing started.

## HOLD or MOVE

**HOLD.** C's application of the escape hatch is careful and honest, and it is still the wrong move, for two
reasons — the second of which I did not have in Round 1.

**1. The escape hatch does not apply on its own terms.** Its trigger, as the brief states it, is *"if a case does
not fit a closed set."* **Davis's extent is not a case that fails to fit the set. It is a case where the set was
never defined for this axis.** I re-read §2.1's table this round specifically to check whether I had missed an
extent scale: the table has exactly four columns, the only quantitative one is **Population**, and there is no
extent threshold anywhere in `01`. So the hatch's precondition is absent — to reach for it you must first
pretend an extent ruler exists and then declare Davis an awkward fit against it. **A missing instrument and a
poor fit are different failures, and only the second has a sanctioned fallback.** C's own cell says this
plainly — *"there is no extent scale anywhere in `01`"* — and then supplies a value on it anyway.

**2. "Most conservative" means the value that asserts least and forecloses least, and `5` asserts and forecloses
more than `UNDETERMINED` does.** §2's *only* stated use for the two numbers is their comparison: they usually
match, and **a divergence is characterizing and must be written as a finding.** So writing `Extent band: 5`
beside `Population band: 5` **is** the negative answer to §2's divergence question, whatever the cell's prose
says beside it. C states that she refuses to assert either that a divergence exists or that it does not — but
the field value has already answered, because that comparison is what the field is for. **The prose disclaimer
and the field value contradict each other, and a later reader scanning a declaration block reads values.**
`UNDETERMINED` asserts nothing and forecloses nothing.

The project's own recorded pathology points the same way. LAW 0-R's measured finding is that *"a zero invites
suspicion; a plausible number does not"* — the census parse that returned *"33 plausible rows, a sensible mean,
and a sensible spread — all wrong."* **`5` is the plausible number. `UNDETERMINED` is the zero that invites
suspicion.** In a project whose self-audit error has run toward flattering the pass on every occasion measured,
the conservative act is the one that cannot be mistaken for a finding.

**And the extent source exists, so this is a deferral with a known terminus, not a permanent hole.** Reader B's
existence-only scan resolved the address: `Extent_and_Density_Per_City.md` lives at
`Worldspace/Locations-and-Levels/Universal_Location_Methodology/`, not under `Cities/` where RWBEM Step D's
relative-path convention points (B's `G0-10`). **That upgrades UNDETERMINED from "I cannot know" to "I know
exactly which file settles this and it was not in my admissible set"** — which is the shape a REQUESTED item is
supposed to have.

*(One attribution: Reader A cited RWBEM's own rule that "a blocked check is not an absence." `Real-World_Basis_
Extrapolation_Method.md` is outside my re-open permissions this round, so I record that as A's quotation rather
than asserting it myself. Nothing in my verdict depends on it.)*

## What the losing reading would cost, concretely, in this pass

- **It pre-answers the one question §2 says is characterizing, in the negative, before the evidence is read.**
  Davis is a Band 5 population in a bounded ice-free envelope — about 400 km² of exposed rock between an ice
  sheet and a bay. If the extent file later places Davis below Band 5 on extent, §2 requires that divergence to
  be *written as a finding*; with `5` already sitting in the block, the likeliest outcome is that it gets
  discovered and quietly skipped as a correction to an existing value rather than surfaced as a finding. B
  pre-registered against exactly this. A declared `5` disarms the pre-registration.
- **It puts an unsourced number into a block whose every line "changes a later question."** Extent is the input
  a density or a footprint claim would later be read off. An unsourced band here is a scale error with a long
  downstream reach, and §6 names scale errors as four of the seven substantive errors this block exists to
  prevent.
- **The loser's real cost, stated honestly:** `UNDETERMINED` leaves a mandatory template slot unfilled, and an
  unfilled slot reads to a later reader as an un-run check. That is a genuine cost and it is cheap to pay:
  file it as REQUESTED, name `Universal_Location_Methodology/Extent_and_Density_Per_City.md` as the resolving
  source, and name Step 1 as the step that declares it. That converts an empty slot into a routed one.

---

# FIELD 3 — CONFIGURATION

## Verdict

**EXCEPTIONAL.** Readers A and B are right.

## The rule I am deciding on

`01_Frame_Typology_and_Inheritance.md` §6, the template line and its bracketed instruction, quoted exactly:

> **Configuration:**   TYPICAL  /  EXCEPTIONAL — in what way: ...
>                      [if exceptional, list the findings that depend on the exceptional property,
>                       so a later reader can tell which technique transfers. A pass cannot correct
>                       for a bias it has not declared.]

And `01` §5.3b, which is the only worked instance of the field in the file and therefore fixes what kind of
property it grades:

> **Before co-writing anything:**
> 1. **Declare it as exceptional**, per the typicality line in `00_RUNBOOK.md` and `05` §7.
> 2. **Name which findings depend on the co-write**, so a later reader can tell which technique transfers.

And the obligations that are suspended here, `01` §2.2, thresholds 3→4 and 4→5:

> Above this threshold a location **must** be decomposed into sub-locations, each of which gets its own pass,
> and the parent's pass covers only what is genuinely shared plus the *pattern of variation*.

> Above roughly a million, **the location no longer has a culture; it has a statistical shape.** … A Band 5
> pass that reads like a Band 3 pass has committed the scale error named in `00c` Gate 11 and `00d` — asserting
> of a large population what is true of a small one.

## HOLD or MOVE

**HOLD**, and on a firmer footing than I had in Round 1, where I flagged this as one of my two contested calls.

**The field as currently specified grades the pass, not the place — and this is settled by §6's own text, not
by `R-4`.** §6's bracket says the declaration exists *"so a later reader can tell which technique transfers"*
and that *"a pass cannot correct for a bias it has not declared."* Technique transfers between **passes**;
a bias belongs to a **pass**. And §5.3b — the file's only worked instance — grades a **co-write**, which is a
fact about how the document was authored and not a fact about the locations. So the brief's instruction to
decide the field as it currently stands rather than as `R-4` proposes to rename it does not change the answer:
**as currently worded, the field already reads as authoring configuration.** `R-4` is a proposal to make
explicit what §6 and §5.3b already say. *(Stated as a contingency so the developer can see it: this verdict
flips only if the developer rules that the field grades the typicality of the **place**. Davis-the-place is
unremarkable and would grade TYPICAL under that reading. The current text does not support it.)*

**On that reading Davis is plainly exceptional.** The pass declares Band 5 with both of Band 5's mandatory
instruments suspended by ruling: no decomposition into sub-locations, no distributional analysis. §2.2 states
both as **MUSTs** and names the failure their absence produces — *"a Band 5 pass that reads like a Band 3
pass."* A pass running a band declaration without that band's machinery is not running the standard instrument,
and "which technique transfers" is exactly the question a later reader will have.

**C's own cell is the strongest argument against C's own grade.** C writes: *"ONE DECLARED, RULED DEVIATION,
named here so a later reader can tell which technique transfers … (A pass cannot correct for a bias it has not
declared.)"* **That is the EXCEPTIONAL branch's obligation, performed in full, under the TYPICAL label.** The
two branches of this field differ in precisely one thing: whether the dependent findings must be listed. C
listed them. Whatever else is true, a pass that owes and discharges the EXCEPTIONAL obligation has not
established that it is TYPICAL; it has established the opposite and then ticked the other box.

**C's real ground — which I flagged myself in Round 1 — is that a corpus-wide ruling is the new typical.** It is
the best argument on that side and it does not survive contact with what the field is for. `DR-4` is
**suspended, not cancelled**: it lifts once all 38 cities complete ULM + CST + RWBEM. So there will be a
population of later passes for which the distributional layer **is** present, and a reader transferring
technique from Davis into one of them needs to know Davis's was absent. **Corpus-wide application makes the
declaration redundant across the 38; it does not make it unnecessary.** And the baseline the word "typical" is
measured against is the methodology as written — §5.3b's whole posture is that a deviation from the written
default *"must earn itself"* — not current corpus practice under a standing suspension.

**On B's second ground (b), the capacity criterion.** I accept it as corroborating and would not rest the grade
on it alone. The fact is real and belongs in the cell: the band is fixed on Census I (1,158,314 → Band 5) while
Census II (781,596 → Band 4) sits inside the same declared frame, so **Davis crosses a band boundary inside its
own frame and the governing figure is a capacity figure rather than a description of the frame's later half.**
Any later finding scaled off 1,158,314 is scaled off capacity. That is transfer-relevant. It is not a
re-litigation of `DR-4`, which is the developer's and is not open. **Ground (a) — Band 5 declared with Band 5's
machinery deferred — is sufficient on its own.**

## What the losing reading would cost, concretely, in this pass

- **An undeclared scale bias in the one place no gate will catch it.** §2.2 names the failure ("a Band 5 pass
  that reads like a Band 3 pass"); LAW 0 says of the gates, *"They confirm a pass is not wrong. None of them can
  tell you it is not thin."* A TYPICAL grade tells a later reader that this pass ran the standard Band 5
  instrument. It did not. That reader then transfers a technique that has a hole in it and inherits the hole
  without a flag.
- **It removes the only place the `Uniform` hazard is recorded.** Both A and B note the same downstream trap:
  §5.4 gives a Band 4+ pass three dispositions, and with no sub-location passes in existence **`Delegated` has
  nowhere to go**, which creates active pressure toward answering categories `Uniform` — the exact thing §5.4
  says *"a Band 4+ pass that answers everything as Uniform has not been written at its own scale."* The
  EXCEPTIONAL findings list is where that pressure is written down. TYPICAL drops the list.
- **The winner's real cost, stated honestly:** if all 38 city passes grade EXCEPTIONAL on the same ground, the
  grade stops discriminating, and a genuinely unusual pass — a co-write, say — no longer stands out against it.
  That is a real cost and it has a cheap mitigation: **state the ground precisely and namedly (the `DR-4`
  deferral) so a later corpus sweep can filter it mechanically, and keep the dependent-findings list specific to
  Davis rather than generic to the ruling.** A and B's cells both already do this.

---

# SUMMARY

| Field | Verdict | Position | Round 1 readers agreeing |
|---|---|---|---|
| 1 — Type modifiers | `Settlement`, no modifiers | **MOVE** | B, C |
| 2 — Extent band | `UNDETERMINED`, filed REQUESTED | **HOLD** | A, B |
| 3 — Configuration | `EXCEPTIONAL` | **HOLD** | A, B |

**Nothing is left unresolved.** I considered declaring Field 1 an honest split and decided against it: the
`"commonly assigned … check every location carrying it"` reading is textual rather than judgmental, and it
removes the only rule that was pulling toward assignment. I am not converging for the sake of converging on any
of the three — I moved on one and held on two, and on Field 3 I hold against the reader who would have made my
block tidier.

**Two conditions I attach to my own verdicts, because adopting them without these makes them worse than the
alternatives:**

1. **Field 1** — the final block must state in prose that L127's documentary-inheritance-without-a-living-
   institution finding is seated at **G4** and is a primary input. Dropping the modifier must not drop the
   finding's visibility.
2. **Field 2** — `UNDETERMINED` must be filed as a routed REQUESTED item naming
   `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md` and the step
   that resolves it, or it will read to a later reader as an un-run check.

**One item for the developer, not for this round to settle:** `01` §1.1's Installation-doubling expectation
(*"Anywhere founded as an installation and now inhabited as a home carries `Settlement + Installation` … Expect
this doubling wherever a setting's history includes purpose-built outposts that outlived their purpose"*) points
in the opposite direction from this universe's GPS law for every Tepenian city founded on a real station site,
which is most of them. Reader A recorded this in Round 1 Note B and declined to resolve it. **Field 1's outcome
above is the same collision showing up a second time, on a second modifier, on the same location.** That makes
it a methodology-level question rather than a Davis-level one, and it is now evidenced twice.

---

FIELD 1: `Settlement`, zero modifiers — `Resettled` NOT assigned — **MOVE**
FIELD 2: Extent band `UNDETERMINED`, filed REQUESTED — **HOLD**
FIELD 3: Configuration `EXCEPTIONAL` — **HOLD**


---

# ROUND 3 — CROSS-CHECK B

# DAVIS — STEP 0 (FRAME) — T8 ROUND 3, **CROSS-CHECKER B**

**Written 2026-09-14. No repository file was edited; this file is my only write.**
**Scope: exactly three contested fields.** Every other line of the frame declaration came back unanimous in
Round 1 and is not touched here. Round 2 established that all three readers genuinely read all fifteen files;
**I do not re-litigate that and I did not re-check it.**

**My Round 1 position is Reader B's**, and HOLD/MOVE below is stated against it.

> **What I re-opened, and why.** `01_Frame_Typology_and_Inheritance.md` §1.1, §1.2, §2, §2.1, §2.2, §3, §5.3b,
> §5.4, §6 · `00_RUNBOOK.md` L2416–2479 (Step 0) **and L595–608** (the typicality declaration, which Step 0's
> own range does not contain and which `01` §5.3b points at by name) · `Disciplines/Real-World_Basis_Extrapolation_Method.md`
> L14–25 and L345–352 · `Specs/Davis.md` **L122–134 only**, inside the bound spec, for L127 verbatim.
> **`graphify` was not invoked and no repo-wide search was run.** The `PreToolUse` hook fired on nearly every
> call; disregarding it is this brief's instruction (`DR-6`), not my own judgment.

---

# FIELD 1 — TYPE MODIFIERS: is `Resettled` assigned?

## 1. Verdict

> ## **`Settlement`. NO modifiers. `Resettled` is DECLINED.**
> **And the material A wants to keep is kept — at `G4`, where it is already seated and already selected.**

Readers B and C reached the right answer. **Reader A reached the wrong answer for a good reason**, and A's own
flag on it ("*my second flagged call*") is what made this round tractable. But A's supporting rule reads the
other way, and an admitted line neither B nor C used settles it.

## 2. The rule I am deciding on

**`01_Frame_Typology_and_Inheritance.md` §1.2, the modifier table, `Resettled` row — quoted complete:**

> | **Resettled** | What did the second population inherit, misread, or fail to notice about the first? *(Commonly assigned and systematically under-used — check every location carrying it.)* |

**And `01` §1.1's opening sentence, which is the load-bearing one for what a modifier *is*:**

> **One primary type, any number of modifiers.** The primary type decides which phases are mandatory, which are
> optional, and which are meaningless. **The modifiers each add specific obligatory questions.**

**And `Specs/Davis.md` L127, in full, an ADMITTED line:**

> **Settled:** Post-Falkland Treaty, on Davis Station infrastructure. The Australian Antarctic Division operated
> here from 1957. *(Refined 2026-07-25 — GPS-purposes-only pass:* through the First Interwar Period, the station
> was continuously maintained by a rotating succession of national operators — **which nations held it, and in
> what order, isn't relevant to the story.** No living environmental *knowledge* survived that chain of handoffs
> — but preserved journals, logs, and orientation manuals left behind across the centuries gave the exiles a
> real documentary starting point for the Vestfold Hills' terrain. Learning from a written record isn't the same
> as being taught by a living institution, **and the exiles still built their own practical mastery of the
> terrain independently, over generations of their own.**)*

**Supporting, and binding:** `Universal_Location_Methodology/00_RUNBOOK.md`'s **NO FORCED FIT** law, as stated in
the project instructions — *"Never force a location, community or society into a category it does not naturally
occupy — and the error runs BOTH ways… When nothing fits, say so and leave the slot explicitly open."*

## 3. Three reasons, in ascending order of force

### (a) A's principal citation points the opposite way from how A read it

A assigns the modifier partly because *"the recorded failure mode for this modifier is under-use, not
over-assignment."* **Read the parenthetical again: *"Commonly assigned and systematically under-used — check
every location carrying it."***

That is **one sentence with two clauses and they are not both nudges toward assignment.** "Commonly assigned"
is a statement that it gets handed out **a lot**. "Systematically under-used" is a statement that once handed
out, its obligatory question **does not get worked**. And the remedy the parenthetical actually issues is
scoped precisely: ***"check every location carrying it"*** — go back to the ones that **already have** it and
verify the question was run.

⭐ **It is a USE warning, not an ASSIGNMENT nudge.** On its own terms it is, if anything, a caution that the
modifier is over-handed-out relative to the work done with it. A read it as a mandate to look harder for
places to assign it; the sentence says to look harder at places that already have it.

**This does not make A careless — the sentence is genuinely ambiguous, and I am recording that as a
methodology defect at the end of this file rather than as a mark against a reader.**

### (b) A's scope-narrowing answers a different question than the modifier asks

The obligatory question is: ***what did the second population inherit, misread, or fail to notice ABOUT THE
FIRST?*** A's answer is: **they inherited a written record without a teacher.**

**That is an answer about the inheritance, not about the first.** Strip the predecessor out of A's sentence
and the sentence survives completely intact — which means the predecessor was never doing work in it. What A
has actually answered is *"what condition did the founding population start from?"* — and that is **`G4`,
founding condition**, verbatim, which **all three readers independently selected as a primary generator.**

B and C both landed here independently ("*the material itself loses nothing — it is already seated at `G4`*";
"*Nothing is lost: the substance sits in `G4`, where the contract already puts it, and it is sharper there*").
Two readers converging on the same relocation, from separate reasoning, is the strongest signal this round
produced on this field.

### (c) ⭐ THE DECISIVE ONE — **L127's closing clause bounds the modifier out of existence, and no reader used it**

A's richest offering is the *misread* half: *"a community learning terrain from manuals rather than from people
will misread specific things."* It is a genuinely good finding and I want it kept.

**But read the clause L127 ends on:** ***"and the exiles still built their own practical mastery of the terrain
independently, over generations of their own."***

**Canon has already resolved the misreading.** The documentary inheritance is stated as a **starting point**,
explicitly superseded by mastery the community built **itself**, over **generations**. So the condition the
modifier would install is:

| | |
|---|---|
| **Scope in time** | **Founding-era.** Act 1 — roughly the first 18% of a 248-year frame |
| **Canon disposition** | **Explicitly superseded**, by the same line that establishes it |
| **Its predecessor** | **Declared story-irrelevant by canon itself** — *"isn't relevant to the story"* |

⛔ **A type modifier is a whole-frame, whole-pass property that installs an obligatory question into every one
of eleven phases.** Using one to carry a bounded, canon-superseded, founding-era condition is a **scale error
in the instrument**, independent of GPS. At Band 5 across 248 years it would mean writing roughly two hundred
years of Act 2 Davis as characterized by an inheritance the spec says its people had already grown out of.

**"And what does that cause?" — three times.** First: every phase carries a question about the first
population. Second: the only complete answer available is the forbidden lineage, so the honest answer is a
null, repeated eleven times. Third: **eleven repeated nulls on a question the frame block itself declares
mandatory is not a neutral state — it is a standing invitation to fill them**, and the only filler on the
shelf is the material the GPS law excludes. That is not a hypothetical: this project's own record has it
**flagging the site-history trap and walking into it hours later.** A modifier carried with a permanent
standing exception written next to it is a trap with a sign on it, and the sign is the part that wears off.

## 4. One correction to A's ground that does NOT change the verdict

**A's Note B — declining `Settlement + Installation` — is correct and is the better half of A's type work.**
A's structural observation there deserves to survive this round intact and be routed to the developer:

> *"the ULM's own Installation-expectation rule and this universe's GPS law point in opposite directions for
> every Tepenian city founded on a real station site, which is most of them."*

**That is a real, general, methodology-level finding and it is not disturbed by anything I decide here.**
It should go forward as A's, not be lost because A's other type call did not carry.

## 5. What the losing reading would cost — concretely, in this pass

1. **A permanent GPS pressure point in eleven phases**, whose only complete answer is the excluded predecessor.
   Likely leak sites are nameable now: the founding/history phase, the order-and-institutions phase (*who set
   the rules before?*), and the surface-and-texture phase, where **the `Ruined/abandoned` question — *"who left,
   how fast, and what did they not take?"* — bleeds in through inherited building stock** while `Ruined` itself
   is correctly unassigned.
2. **Roughly 200 years of Act 2 written under an Act 1 property**, against a canon clause that says the
   community superseded it.
3. ⭐ **Double-counting that inflates the pass's apparent evidentiary base.** `G4` and the modifier would both
   be driven by **the same single line, L127**. One input would appear in the frame block twice, as a generator
   and as a type property — making the pass look better-sourced than it is. At a location whose `G3` already
   rests on one line and whose `G6` is a recorded null, **a pass that cannot count its own inputs honestly is
   exactly the failure Gate 0 exists to catch.**
4. **Nothing is bought.** The *misread* finding survives without the modifier and is sharper: it is a
   **`G2` × `G4` generator conflict** — a population that learned its ground from paper, set against a physical
   inventory that is specifically misreadable from paper (which lakes are hypersaline and which are landlocked
   marine basins, where fjord ice is safe, what a 0-to-24-hour light budget does to a growing season).
   **Both generators are already selected by all three readers. The finding needs no modifier to exist.**

> ### ⭐ CARRY-FORWARD, so this round does not read as deleting A's contribution
> **A's *misread* material is ADOPTED, re-seated at `G2` × `G4` as a generator conflict, and explicitly bounded
> to Act 1 with L127's supersession clause stated beside it.** The modifier is declined; the finding is kept.

## 6. Consistency check, run and passed

`Resettled` also exists as a **Status** value in `01` §3 (*"What did the second population inherit and
misread?"*). All three readers declared Status `LIVING`, unanimously — so Status-`Resettled` was already
declined by the whole round. **The type call and the status call now agree**, and they agree for the same
reason. A frame block that declined `Resettled` in one field and assigned it in the other would have been
internally incoherent, and that is worth recording as a check that fired clean rather than as an absence.

**FIELD 1 — HOLD.** *(Verdict held. **Reasoning MOVED** — see §7 of this file: my Round 1 ground was loosely
framed and I am correcting it.)*

---

# FIELD 2 — EXTENT BAND

## 1. Verdict

> ## **`UNDETERMINED` — a blocked check, filed as REQUESTED. Readers A and B are right.**
> **Declining to declare IS the conservative act, and declaring `5` is not conservative — it is the one move
> that permanently disables the instrument `01` §2 exists to run.**

## 2. The rule I am deciding on

**`01_Frame_Typology_and_Inheritance.md` §2, opening — quoted exactly:**

> **Declare two numbers, not one:** the **population band** and the **extent band**. They usually match. **When
> they diverge, the divergence is characterizing** and should be written as a finding — a corridor with no
> residents spanning a subnet, a megastructure housing forty people and visible from orbit, a polity of millions
> administered from one room.

**`Disciplines/Real-World_Basis_Extrapolation_Method.md` — LAW 0-R, L17–21, quoted exactly:**

> ⛔ **A RECALLED fact is a guess wearing a confident tone.** ⛔⛔ **A WRONG fact is worse than a MISSING one**,
> because it produces worldbuilding that is confident, coherent and wrong and nothing downstream flags it —
> *measured twice here: a census parse returning "33 plausible rows, a sensible mean, and a sensible spread —
> all wrong," and 22 cities carrying wrong polar-night spans (`M-141`).* ⭐ ***A zero invites suspicion; a
> plausible number does not.***

**Same file, L349–351, quoted exactly:**

> ⛔ **AND READ `10_Readiness_Check.md` BEFORE CONCLUDING THE LOCATION LACKS SOMETHING.** ***A blocked check is
> not an absence*** — *a pass can be forbidden from opening the canon file that would have answered, and it
> records that as blocked. Fusing a detail into a gap that is merely unread is how a contradiction gets built.*

## 3. Why C's application of the escape hatch is the wrong instrument, and then the wrong answer

### (a) The escape hatch does not cover this case

The clause is *"if a case does not fit a closed set, choose the most conservative value and name the problem."*
**Its trigger is a FIT failure** — the thing exists, you can see it, and none of the available categories
describes it.

**That is not Davis's situation.** Davis's situation is that **there is no scale and no measurement**: `01`
§2.1's table has one axis and it is population, and the canon extent source is not in the admissible set.
**Nothing has failed to fit, because nothing has been measured.** That is a **missing input**, and the
methodology already has a dedicated, named instrument for a missing input — ***"a blocked check is not an
absence"*** — plus the REQUESTED mechanism to route it. **C reached for the fit-failure clause when the
missing-input clause was the one that applied.**

### (b) On the merits, `UNDETERMINED` is strictly the more conservative value

"Conservative" in a declaration block can only mean **claims the least and is cheapest to correct**:

| | `UNDETERMINED` + REQUESTED | `5`, "matching, unconfirmed" |
|---|---|---|
| **What it asserts** | **Nothing** | **Extent band 5**, and therefore *no divergence* |
| **How a later pass fixes it** | Opens the canon file, fills the slot | Must first **notice** the number was never sourced |
| **Can anything downstream have been built on it** | **No — there is no number to build on** | **Yes** |
| **How it reads once the caveat is dropped** | Visibly incomplete | **Indistinguishable from a sourced band** |

⭐ **And that last row is the whole argument.** The caveat C wrote is good and honest — and **it lives in a
cell, while the value lives in a header.** Frame-block values are what get copied into the tracker, the
progress files and the megasheet; prose cells are what get compressed out. **LAW 0-R names this exact failure
in one line: *"A zero invites suspicion; a plausible number does not."*** `5` is a plausible number. That is
the property that makes it dangerous, not the property that makes it safe.

### (c) ⛔ THE DECISIVE ONE — declaring the match **destroys the instrument**

`01` §2 declares two numbers **for a reason**: the second is an **independent check on the first**, and its
entire yield is the case where they **disagree**. *"When they diverge, the divergence is characterizing."*

**A band declared as "matching the population band" is not a second number. It is the first number written
twice.** It carries zero independent information, and it **pre-answers the divergence question in the
negative** — permanently, for Davis, because the block will thereafter say the bands match.

C writes, carefully and in good faith, *"I decline to assert a divergence I cannot source, and decline equally
to assert that none exists."* **The intent is exactly right. The mechanism does not deliver it:** the field's
value **is** the assertion. A reader of the block sees `Extent band: 5` and reads "extent band 5." There is no
way to put a number in a numeric slot and have it not be a claim.

⭐ **And Davis is precisely the profile where a divergence would pay.** ~400 km² of ice-free exposed ground,
an ice sheet on one side and Prydz Bay on the other, holding a Band 5 population. **A Band 5 population inside
a hard-bounded envelope is `01` §2's own third example — *"a polity of millions administered from one room"* —
in a different key.** Declaring a match at Step 0 pre-closes the single most promising divergence finding the
frame block is capable of producing.

### (d) A coherence observation about the round, offered as evidence and not as a score

**The same escape-hatch clause was applied twice in this round, on two fields, and produced opposite
directions.** On Field 1, Reader B invoked it to **decline** a modifier ("*the most conservative value is
taken (no modifier), the problem is named*"). On Field 2, Reader C invoked it to **declare** a band.

**Reader C declined `Resettled` — claiming less — and declared extent `5` — claiming more — in the same
block, under the same principle.** I do not read that as carelessness; I read it as proof that the clause's
wording genuinely supports both readings and needs tightening. **But for deciding THIS field:** the reading
that is internally consistent across both of C's own calls is *"conservative = claim less,"* and that reading
gives `UNDETERMINED`.

## 4. What the losing reading would cost — concretely, in this pass

1. **`01` §2's divergence instrument is disabled for Davis, permanently.** A match has been declared; the
   check can never fire. The finding it would have produced is not deferred — it is **foreclosed**, which is
   exactly what Step 0.5 is written to prevent.
2. **An unsourced plausible number enters a machine-readable header** and propagates into every downstream
   artifact without its caveat. `M-141`'s shape — 22 cities carrying a wrong span — is this failure at corpus
   scale.
3. ⭐ **The REQUESTED item disappears, and with it the remedy for a real defect this round already found.**
   Reader B's `G0-10` establishes that `Real-World_Basis_Extrapolation_Method.md` Step D names
   `Extent_and_Density_Per_City.md` as **tier-1 HARD CANON** under a stated path convention it does not resolve
   under — and Reader B's existence check found the file in a **different tree entirely**
   (`Universal_Location_Methodology/`). **`UNDETERMINED` keeps that defect on the docket with a named fix.
   `5` closes the ticket without doing the work**, and the addressing defect stays live for the next 37 cities.
4. **The one extent-shaped datum in the admitted set gets silently promoted.** ~400 km² is the **Vestfold
   Hills ice-free oasis** — a geographic feature. Treating it as a city footprint assumes the city fills the
   oasis and extends no further, which is the density-derivation `01` §2 forbids, dressed differently. Both A
   and B caught this independently. **`UNDETERMINED` is what keeps it caught.**

> ### The concrete remedy, so this is a work item and not a hole
> **REQUESTED:** open `Universal_Location_Methodology/Extent_and_Density_Per_City.md` — **the resolved address,
> per B's `G0-10`, not the one RWBEM Step D prints** — at Step 1, declare the extent band there, and run `01`
> §2's divergence check at that point with both numbers in hand.

**FIELD 2 — HOLD.**

---

# FIELD 3 — CONFIGURATION: `TYPICAL` or `EXCEPTIONAL`?

## 1. Verdict

> ## **`EXCEPTIONAL`. Readers A and B are right — and Reader C already wrote the EXCEPTIONAL declaration,
> under the TYPICAL flag.**

## 2. The rule I am deciding on

**`00_RUNBOOK.md` L598–607 — the typicality declaration. This is the field's governing statement, and it is
NOT inside Step 0's own line range (2416–2479); `01` §5.3b points at it by name. Quoted exactly:**

> ## The typicality declaration — one line, and it is not optional
>
> **Add to the frame declaration and to the `05` §7 pre-flight:**
>
> > ***Is this location's configuration typical, or exceptional? If exceptional, in what way — and which findings
> > depend on the exceptional property?***
>
> **A pass cannot correct for a bias it has not declared.** The Tri-Cities run produced seven findings from
> Phase 5 and could not tell that nearly all of them were unavailable to a normal location, because it never
> asked this question.

**And `01` §6's template line, quoted exactly:**

> **Configuration:**   TYPICAL  /  EXCEPTIONAL — in what way: ...
>                      [if exceptional, list the findings that depend on the exceptional property,
>                       so a later reader can tell which technique transfers. A pass cannot correct
>                       for a bias it has not declared.]

## 3. C's argument is real, and the runbook's own worked failure answers it

**C's argument, stated at its strongest** (A anticipated and named it too, in A's contestability flag): `DR-4`
is **corpus-wide**. It applies to all 38 cities. A property that every pass in the run shares is not a
deviation from that run — **it is that run's normal.** And a flag that fires on 38 of 38 passes carries no
information at all.

**That argument is not weak and I want it on the record as having been taken seriously. It loses on the
baseline question, and the runbook settles the baseline in its own failure case.**

⭐ **The Tri-Cities sentence names the yardstick explicitly: findings that were *"unavailable to a NORMAL
LOCATION."*** Not *unavailable to the other cities in the batch.* **Not *unusual for this run.*** The baseline
is **the methodology's standard pass** — what a pass run by the book, without this configuration, would have
been able to produce.

**And the reductio is exact.** If the baseline were "whatever this run happens to be doing," then a run that
co-wrote **all 38** cities would declare **TYPICAL on all 38** — and would reproduce the Tri-Cities failure
across an entire corpus, with the flag that exists to catch it reading clean the whole way. **A
self-referential baseline cannot detect a run-wide bias, and a run-wide bias is the most expensive kind.**
The field exists to be read by *"a later reader"* transferring technique out of this pass — and that reader's
frame of reference is the methodology, not this batch's conventions.

⛔ **Second, smaller point:** answering "is this configuration typical?" by reference to what the other 37
cities are doing imports a **peer baseline** into a per-location field. The **ONE LOCATION** law's reach is
places rather than authoring configurations, so this is not a violation — **but it points the same way**, and
the peer-free habit is the right one here.

## 4. Davis has a location-specific exceptional property, not only the corpus-wide one

Even granting C's baseline entirely, **there is a fact about Davis, statable without reference to any other
city**, that survives:

> **Davis's declared population band is `5`, and Davis crosses the 4/5 band boundary INSIDE its own declared
> frame.** Census I = 1,158,314 → Band 5. Census II = 781,596 → Band 4. Both snapshots sit inside 2564–2812.

**Run the one-sentence test on that: delete every other city's name from it. It survives untouched.** It is
Davis's own arithmetic against `01` §2.1's own table, verified independently by all three readers. **A pass
whose band is stable across its frame and a pass whose band changes inside its frame are not running the same
instrument**, and a later reader transferring technique needs to know which one this was.

**I make no claim about whether other cities share this.** That is a corpus question, it is a comparison, and
this pass is not where it gets answered.

## 5. ⭐ What C actually wrote, which is the cleanest fact in this field

C's `Configuration` cell, verbatim:

> ⚠ ONE DECLARED, RULED DEVIATION, named here so a later reader can tell which technique transfers: Band 5 is
> declared while `01` §2.2's Band 5 distributional machinery is expressly DEFERRED (DR-4). Any finding that
> would require a spread, a mode, or a sub-location breakdown is therefore OUT OF SCOPE for this pass — not
> absent from Davis. A later reader transferring this pass's technique to a pass without that deferral should
> expect the distributional layer to be present there and missing here. (A pass cannot correct for a bias it has
> not declared.)

**Set that beside `01` §6's specification of what an EXCEPTIONAL declaration must contain** — *in what way ·
list the findings that depend on the exceptional property · so a later reader can tell which technique
transfers* — **and C has discharged the EXCEPTIONAL obligation in full, including quoting the rule that
governs it.**

⭐ **So the disagreement on this field is narrower than it looks. C's substance is right and complete. Only
the flag is wrong.** And the flag is the half that matters mechanically: **`05` §7's pre-flight and any later
sweep read the VALUE, not the cell.** A reader filtering for passes that need bias correction filters on
`EXCEPTIONAL` — and skips this one.

## 6. Conceding C's real cost, and disposing of it

**C is right that a flag firing on every pass carries no information.** That cost is real and I am not
waving it away.

**But it is not a reason to mislabel this pass.** If it does turn out that all 38 carry `EXCEPTIONAL` for the
same reason, **that is a finding about the run**, and its remedy is a standing corpus-level note — a single
line recording that `DR-4` places the whole run in a declared-exceptional posture until the deferral lifts —
**not 38 passes each quietly declaring themselves normal.** The first is a visible, one-place fact a developer
can act on. The second is 38 invisible ones.

**And determining whether all 38 share it is a corpus question. It is not Davis's to settle, and Step 0 is not
where it gets settled.** Flagged upward, not resolved here.

> **Note, per the brief:** docket item `R-4` — that the field describes the **authoring configuration of the
> pass** rather than the typicality of the **place** — is **open, not ruled**, and I have decided this field as
> currently specified. ⭐ **I record that `R-4`'s reading, if ruled, would STRENGTHEN this verdict rather than
> disturb it:** the deferral of Band 5 machinery is unambiguously a property of the **authoring
> configuration**, which is the half `R-4` says the field is about. **No re-decision would be needed.**

## 7. What the losing reading would cost — concretely, in this pass

1. ⭐ **The Tri-Cities failure, in mirror image.** Tri-Cities **produced** findings a normal pass could not
   have, and could not tell. Davis will **fail to produce** findings a normal Band 5 pass would have — the
   spreads, the modes, the sub-location breakdowns — and **a `TYPICAL` flag says nothing is missing.** The
   typicality line was written for exactly one failure and this is it, with the sign reversed.
2. **Every "what Davis is like" answer reads as an ordinary result instead of a tagged consequence.** Both A
   and B pre-identified this and pre-committed to tagging: A's *"a PERMITTED consequence of the deferral… must
   be TAGGED as such, never defended on the merits."* **Under `TYPICAL` there is nothing to tag against**, and
   `01` §2.2's own warning lands unguarded: *"A Band 5 pass that reads like a Band 3 pass has committed the
   scale error named in `00c` Gate 11 and `00d`."*
3. **A `Uniform` answer under `01` §5.4 stops looking suspicious.** With `Children: none` by deferral,
   `Delegated` has nowhere to go — A flagged this precisely — so the deferral generates active pressure toward
   the failure §5.4 names: *"A Band 4+ pass that answers everything as Uniform has not been written at its own
   scale."* **`EXCEPTIONAL` keeps that pressure visible. `TYPICAL` normalizes it.**
4. **Technique transfers out of Davis silently and wrongly.** A later pass — on a sub-location, on another
   location after the deferral lifts — would import Davis's method believing it came from a standard Band 5
   pass. **That is the "bias it has not declared" in its literal form**, and it is the one cost that is paid
   somewhere other than here, which is the kind this project's LAW 0 says is never paid at the time.

**FIELD 3 — HOLD.**

---

# TWO METHODOLOGY DEFECTS THIS ROUND SURFACED

> **Recorded per Step 9.5 — the recording law: log snags, dead ends, killed findings and self-corrections, not
> only successes.** Neither is a criticism of a reader; both are ambiguities that produced good-faith opposite
> readings from competent readers who had read the file in full. **Both are one-line fixes with corpus-wide
> reach, and both are worth more than the three verdicts above.**

### **DEF-1 — `01` §1.2's `Resettled` parenthetical is ambiguous in DIRECTION, and it steered a reader.**
*"(Commonly assigned and systematically under-used — check every location carrying it.)"* Reader A read it as a
nudge toward **assigning** the modifier more readily; Readers B and C read it as a warning about **working** it
once assigned. **A one-clause clarification settles it permanently for all 38 cities and for every district
already carrying it.** Suggested, for the developer to accept or reject — not applied by me:
> *(Commonly assigned and systematically under-used. **This is a warning about USE, not an invitation to
> assign:** check every location that already carries it, and do not add it to a location whose obligatory
> question cannot be answered from admissible material.)*

### **DEF-2 — "choose the MOST CONSERVATIVE value" is ambiguous, and produced opposite directions inside one
round.** B used it to justify **withholding** a value; C used it to justify **supplying** one. **Both are
defensible readings of the words.** Suggested clarification, again not applied:
> *Most conservative = **the value that claims the least and is cheapest for a later pass to correct.** Where
> the honest options are a plausible value and no value, **no value wins** — a blocked check is not an absence,
> and a zero invites suspicion where a plausible number does not. **And this clause covers a FIT failure, not
> a MISSING MEASUREMENT: where the input simply was not admitted, declare it blocked and file it REQUESTED.***

---

# SELF-CORRECTIONS TO MY OWN ROUND 1 (READER B) REASONING

> **Stated because Round 3 exists to correct reasoning, not only to tally verdicts, and because a checker who
> reports only the other readers' errors has not checked itself.** **Both verdicts stand; both GROUNDS change.**

### **SC-1 — Field 1. My Round 1 ground was loosely framed and edged toward the material it was excluding.**
I wrote that `Resettled` fails because *"there was no first **population** — a rotating succession of station
operators is not a resident community."* **The conclusion is right and the framing was sloppy:** it reasons
*from* the real site's operator arrangement to a conclusion about Davis, which is the shape of the move the GPS
law forbids, even used negatively.

**The clean ground, which needs nothing outside the admitted set:** **`Specs/Davis.md` L127 is itself an
admitted line, and canon performs the refusal in its own voice** — *"which nations held it, and in what order,
isn't relevant to the story."* **The admissible set establishes no prior resident population at Davis.** The
modifier's obligatory question therefore has no in-frame subject. **That is a statement about what the pass
holds, not an inference from the excluded predecessor**, and it is the version that should go into the frame
block.

### **SC-2 — Field 3. I should not have cited the override.**
My Round 1 ground (b) said the band *"was set on a capacity criterion… and the three T8 readers unanimously
recommended Band 4 and were overridden."* **The second clause edges toward re-litigating `DR-4`, which is
ruled and closed.** **Withdrawn.**

**What replaces it is a plain frame fact, which is stronger anyway because it cannot be read as an
objection:** **Davis crosses the 4/5 band boundary inside its own declared frame** (1,158,314 → Band 5;
781,596 → Band 4; both snapshots in 2564–2812). **A fact about the frame, stated flatly, with no opinion about
the ruling attached.**

### **SC-3 — Field 1, also mine: I invoked the same escape-hatch clause I am now arguing C misapplied.**
My Round 1 note reads *"per the sanctioned fall-short: the most conservative value is taken (no modifier)."*
**By the reading I have argued for above, that clause did not apply to my case either** — there was no fit
failure to escape from. **The modifier is declined on `01` §1.2's own terms and on NO FORCED FIT, and the
escape-hatch citation should be struck from the Field 1 reasoning.** The verdict does not move; one of its
three supports was never load-bearing and should not be counted as one.

---

# WHAT I COULD NOT SETTLE, AND WHAT WOULD SETTLE IT

**All three fields resolved. I am not manufacturing a split, and I am not manufacturing a consensus either.**
**Field 1 was the closest call by a wide margin** — A's position is coherent, A flagged it as contested
unprompted, and A's `Installation` analysis in the same note is the best single piece of type reasoning this
round produced.

**Two things would make Field 1 settled rather than merely decided**, and both are cheap:

1. ⭐ **A developer ruling on `DEF-1` above** — one clause in `01` §1.2. **This is the high-value one:** it
   settles `Resettled` for all 38 cities and every district already carrying it, not just for Davis.
2. **A general ruling on whether a type modifier may be carried with a standing GPS exception attached to it.**
   My answer is no — a permanent exception on an obligatory question is a structural hazard rather than a
   guard — **but that is my reading, not a stated rule anywhere I read.** If the developer's answer is yes, A's
   position becomes viable again and Field 1 should be re-opened.

---

# THE THREE FINAL LINES

```
FIELD 1: Settlement, NO modifiers — `Resettled` DECLINED — HOLD
FIELD 2: Extent band UNDETERMINED (blocked check, filed REQUESTED)    — HOLD
FIELD 3: Configuration EXCEPTIONAL                                     — HOLD
```

> **Round 3 result: 3–0 to the A/B reading on Fields 2 and 3, and 2–1 (B/C) on Field 1 — with the Field 1
> majority now resting on an argument neither B nor C used in Round 1** *(L127's supersession clause)* **and
> with A's substantive finding carried forward rather than discarded.**


---

# ROUND 3 — CROSS-CHECK C

# DAVIS — STEP 0 (FRAME) — **T8 ROUND 3 · CROSS-CHECKER C**

**Scope: the three contested fields only.** All other fields came back unanimous in Round 1 and are not
reopened here. Round 2 verified all three readers genuinely read all 15 files; **whether they read the material
is not re-litigated below.**

**Re-opened for this round, by direct `Read` at named paths:** `01_Frame_Typology_and_Inheritance.md`
(L1–200, L200–400, L400–582 — the whole file), `00_RUNBOOK.md` L2416–2479, `Specs/Davis.md` L122–134
(inside the bound spec), and the three Round 1 proof files. **`graphify` was not invoked and no repo-wide
search was run**; the `PreToolUse` hook fired on every `Read` and disregarding it is this brief's own
instruction under `DR-6`, not my judgment. **No repository file was edited.** This file is my only write.

**Summary: I MOVE on two of the three and HOLD on one — with its ground corrected.** My Round 1 self was
wrong twice, and one of the two errors (Extent) was an internal inconsistency inside my own declaration block
that only became visible when set beside A's and B's.

---

# FIELD 1 — TYPE MODIFIERS · is `Resettled` assigned?

## Verdict: **NOT ASSIGNED. `Settlement`, zero modifiers.** Reader A's scope-narrowing does not rescue it.

## The rule I am deciding on

`01_Frame_Typology_and_Inheritance.md` **§1.2 The modifiers**, the `Resettled` row, quoted exactly:

> | **Resettled** | What did the second population inherit, misread, or fail to notice about the first? *(Commonly assigned and systematically under-used — check every location carrying it.)* |

and the same file's **§1.2 preamble**:

> **Each adds obligatory questions.** A location may carry several.

and, as the counterweight the brief names, the **NO FORCED FIT** law (`Universal_Location_Methodology/00_RUNBOOK.md`,
restated in `CLAUDE.md`):

> **Never force a location, community or society into a category it does not naturally occupy — and the error
> runs BOTH ways:** assigning an existing roster member that does not fit, **or** inventing a bespoke one to
> fill a blank.

## HOLD — **but my Round 1 ground was wrong and I am replacing it**

**What I got wrong in Round 1.** I wrote that the modifier's obligatory question *"can only be discharged
using the real Davis Station's prior occupancy, which the GPS-purposes-only law excludes."* **That claim is
too strong, and Reader A disproved it.** A produced a discharge that does not touch the excluded material:
Spec **L127** states, inside the admitted set and inside the GPS-purposes-only refinement itself —

> *"No living environmental **knowledge** survived that chain of handoffs — but preserved journals, logs, and
> orientation manuals left behind across the centuries gave the exiles a real documentary starting point for
> the Vestfold Hills' terrain. Learning from a written record isn't the same as being taught by a living
> institution…"*

**A is right that this is answerable without reaching for *whose* the site was or *why* it emptied.** GPS
blocks the operators' nationality, order and lineage; it does not block *that paper survived and people did
not*. **I concede that point without reservation, and A's Note A is the better piece of reasoning on that
sub-question than my Round 1 cell was.**

**I hold the verdict anyway, on three grounds that survive A's rebuttal.**

### 1. Reader B's ground is the load-bearing one, and it is not a GPS argument at all

The modifier's question is about **"the first"** — and its antecedent, in the row's own grammar, is **"the
second *population*."** `01`'s own vocabulary makes "population" a countable resident body: §2.1's table
counts **"~1–30"**, **"0 resident"**, and it is what the band bands. Davis's prior occupancy was, per L127,
**"a rotating succession of national operators"** maintaining a station.

**The ULM has already decided that maintainers are not automatically a population — and it decided it in the
next section over.** `01` **§3**, the status table:

> | **Transit-only** | Who maintains it, and do they count as living here? |

**That the residency of maintainers is an open question is stated by the methodology itself.** A modifier
whose obligatory question presupposes a resolved *yes* cannot be assigned on an occupancy the methodology
files under an open question. **B's formulation — "first-settled on second-hand infrastructure, and §1.2 has
no entry for that" — is the accurate description of Davis, and §1.2's silence on it is a result.**

### 2. §1.2's parenthesis is an **audit note about locations that already carry it**, not a thumb on the scale toward assigning it

This is the pivot of A's case and I think A misreads it. The exact words are:

> *(Commonly assigned and systematically under-used — **check every location carrying it**.)*

**Every clause points at locations that already have the modifier.** *"Commonly assigned"* is descriptive of
how often it gets attached; *"systematically under-used"* says its questions then go unrun; *"check every
location carrying it"* names the audit population as **the ones carrying it**. **There is no sentence here
instructing a pass to assign it more often.** A's Note A reads the warning as pressure toward assignment
(*"the recorded failure mode for this modifier is under-use, not over-assignment"*) — but the recorded failure
mode is **under-use of the questions on locations that have it**, which is a different failure from
non-assignment. **The parenthesis therefore supplies no support for assigning it to Davis, and with that
support removed, NO FORCED FIT's first direction — *"assigning an existing roster member that does not
fit"* — is unopposed.**

### 3. Scope-narrowed to what A narrows it to, the modifier **adds no obligatory question**, which is the only thing a modifier does

§1.2's own preamble: **"Each adds obligatory questions."** A narrows the question until it is exactly the
content of L127 — documentary inheritance without a living teacher. **But all three readers seat that same
content at `G4` (founding condition), and all three select `G4` as a primary generator.** So the pass is
already obliged to ask it, in full, at full weight, with or without the modifier. **A modifier that generates
no obligation the pass does not already hold is a label, not an instrument** — and it is a label that drags an
unnarrowed question (*"about the first"*) into eleven downstream phases.

### Corroborating pressure, offered as pressure and not as a knockdown

`01` **§3** carries the identically-named **status**:

> | **Resettled** | What did the second population inherit and misread? |

**A declines the status (declaring `Living`) while assigning the modifier**, and the two share one obligatory
question. If the question is answerable about Davis, both instruments have grounds to fire; if it is not,
neither does. **A has an available rebuttal** — a modifier is a permanent property and a status is a present
inhabitation state, so a location resettled 248 years ago could carry the one and not the other — **and I
grant it is a real distinction, which is why I rank this as pressure rather than proof.** It still asks A to
explain why one instrument's threshold is met and the other's, worded almost identically, is not.

## What A's reading would cost, concretely, in this pass

1. **It keeps the single most GPS-exposed object in the input set live for eleven phases, behind a guard.**
   A's own Note A names the hazard precisely: *"the modifier's own question invites asking about 'the first
   population,' and the first population is the forbidden object."* A's remedy is a guard written at Step 0.
   **This project's own recorded experience is that a Step-0 guard on this exact trap does not survive the
   session that wrote it** — the memory entry `feedback_gps_site_history_not_an_input` records the developer's
   finding that *"I flagged this trap and walked into it hours later."* **A guard that has to hold across
   eleven phases, written against the failure mode that has already beaten a guard written hours earlier, is
   not a cost-free assignment.**
2. **It creates a standing invitation to widen the set.** The narrowed question is answerable from L127; the
   *unnarrowed* question is not answerable from the admitted set at all. A Phase 4 or Phase 7 reader holding
   `Resettled` and finding L127 thin has an obvious next move, and it is the illegal one.
3. **The cost of declining is close to zero, and this asymmetry is what settles it.** Declining loses **no
   content**: L127 stays a Tier 1 admitted input, seated at `G4`, selected as a primary generator by all three
   readers. A's stated reason for assigning — *"declining would suppress L127"* — **is not true of B's or my
   declination**, because neither of us suppressed it. **So the trade is: zero content gained, one live GPS
   exposure carried for eleven phases.**

## Residual uncertainty, stated rather than smoothed over

**Field 1 stands 2–1, not 3–0, and one question would settle it cleanly for the developer:**
**does `Resettled` require a prior resident *population*, or merely prior *occupancy*?** §1.2's row says
"population" and §3's `Transit-only` row leaves maintainer-residency open, which is why B and I read it the
first way — **but `01` never states the test.** If the developer rules that prior occupancy suffices, A's
assignment becomes correct and my ground 1 falls (grounds 2 and 3 would survive, and would then argue for
assigning it *and* immediately scoping the question to L127, which is A's own Note A). **That ruling is worth
making once, corpus-wide: most Tepenian cities sit on real station sites, so this question will recur at
nearly every remaining city in the run.**

**FIELD 1: Settlement, NO modifiers (`Resettled` declined) — HOLD**

---

# FIELD 2 — EXTENT BAND

## Verdict: **`UNDETERMINED`, filed as a REQUESTED input.** I was wrong in Round 1.

## The rules I am deciding on

`01_Frame_Typology_and_Inheritance.md` **§2**, opening:

> **Declare two numbers, not one:** the **population band** and the **extent band**. They usually match. **When
> they diverge, the divergence is characterizing** and should be written as a finding — a corridor with no
> residents spanning a subnet, a megastructure housing forty people and visible from orbit, a polity of
> millions administered from one room.

`01` **§2.1**, the band table's column header and the Band 5 row, in full:

> | Band | Population | What the unit of analysis is | The district methodology's assumptions |
> | **5 — Regional** | ~1M–50M | **Distributions**, not points | Mostly fail |

`01` **§6**, the template line:

> **Extent band:**     <0-6>   [note if it diverges from population band, and why that matters]

## MOVE — and here is exactly what changed my mind

### 1. My own block was internally inconsistent, and I could not see it alone

**On Field 1 I took the null as the conservative value** — *"an empty modifier list is a RESULT, not an
unfilled slot."* **On Field 2 I took the filled value as the conservative value** — `5`, matching. **Those are
opposite readings of the same escape hatch, two fields apart in one declaration block.** A and B each applied
one reading consistently across both fields. I applied both. **That is not a tie-break in my favor; it is a
defect in my Round 1 output, and it is the single thing cross-checking was supposed to find.**

### 2. "They usually match" is an observation about two independent measurements — using it as a derivation rule destroys the instrument

This is the argument that actually decides it, and it is available from §2's own sentence. **The field exists
so that a divergence can be found**: *"When they diverge, the divergence is characterizing and should be
written as a finding."* **A divergence can only be found if the two numbers are determined independently.**
The moment the second number is derived from the first by assuming the match, **a divergence has been made
impossible by construction** — the check can never fire, at Davis or anywhere. **My Round 1 cell tried to have
this both ways**, saying in the same breath *"declared as MATCHING"* and *"I decline to assert a divergence I
cannot source, and decline equally to assert that none exists."* **Writing `5` on the line is asserting that
none exists.** The note underneath does not retract it, because —

### 3. The declaration block is read as a header, not as prose

`01` §6's closing sentence, and the runbook's Step 0.1, say the same thing twice:

> **The block is not bureaucracy.** Every line of it changes a later question.
> *(`00_RUNBOOK.md` L2432: **"Every line changes a later question."**)*

**A later reader — a Gate F run, a divergence sweep, the terminal differentiation check the ONE LOCATION law
defers everything to — reads `Extent band: 5` against `Population band: 5`, scores "match," and closes the
question silently.** `UNDETERMINED — REQUESTED` cannot be misread that way: it reads as a **live docket item**
and it is the only one of the two values that survives contact with a reader who does not read the note.

### 4. `5` is not a value on any scale `01` defines

A and B both identified this and I under-weighted it. **§2.1's table has exactly one quantitative axis and it
is labeled `Population`.** There is no extent column, no km² thresholds, no extent definition anywhere in the
file. **So "extent band 5" does not mean "between X and Y km²" — it means nothing, and it is asserted.** A
number that carries no criterion is not the conservative choice over an abstention; **it is the less
conservative choice, because it asserts where the abstention does not.** NO FORCED FIT's second direction
covers this precisely — the blank was filled from the roster with a member that does not fit, because *no*
member fits a scale that has not been written.

### 5. It is a **blocked** check with a named unblocker, not an unanswerable one — which is what makes `REQUESTED` the right disposition rather than a permanent hole

**Both A and B independently traced the block to the same upstream cause, and B's existence sweep found the
file.** The canon extent source, ranked tier-1 HARD CANON by RWBEM Step D, exists at
`Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md` — **not at the
address RWBEM's own path convention gives for it** (B's finding `G0-10`, which is `M-117`'s "a name is not an
address" recurring inside the file that records `M-117`). **It was not in this pass's admissible set.** So the
number is obtainable: **admit that one file at Step 1 and the band can be declared with a criterion behind
it.** That is a one-file unblock, not an open research problem.

## What my own Round 1 reading would cost, concretely, in this pass

1. **It pre-answers, and permanently closes, the one question the field exists to ask.** If Davis's real
   extent diverges — and B pre-registered the plausible shape of it, a Band 5 population inside a bounded
   ice-free envelope with an ice sheet on one side and a bay on the other — **that finding is not merely
   missed; it is marked "checked, matched" and can never be found by anyone reading the block.** A missed
   finding is recoverable. A falsely-closed check is not.
2. **It is the recorded error shape this project has measured twice.** A plausible number attracts no
   suspicion; a blank does. `LAW 0-R`'s statement of it: *"A zero invites suspicion; a plausible number does
   not."* **`5` beside `5` is the maximally plausible number.**
3. **It sets a corpus-wide precedent at city 1-of-38.** Davis is early in the run. **If "match the population
   band" is accepted as the way to fill an undefined field, 38 cities inherit an extent column that was never
   measured, and the divergence instrument is dead corpus-wide** — discovered, if ever, only when someone asks
   why no city in 38 ever diverged.

**FIELD 2: Extent band = UNDETERMINED (filed REQUESTED; unblocks by admitting `Universal_Location_Methodology/Extent_and_Density_Per_City.md` at Step 1) — MOVE**

---

# FIELD 3 — CONFIGURATION · `TYPICAL` or `EXCEPTIONAL`?

## Verdict: **`EXCEPTIONAL`.** I was wrong in Round 1, and my own Round 1 cell contains the proof.

## The rule I am deciding on

`01_Frame_Typology_and_Inheritance.md` **§6**, the declaration block, quoted exactly and in full:

> **Configuration:**   TYPICAL  /  EXCEPTIONAL — in what way: ...
>                      [if exceptional, list the findings that depend on the exceptional property,
>                       so a later reader can tell which technique transfers. A pass cannot correct
>                       for a bias it has not declared.]

and `01` **§5.3b**'s co-write box, which is the only place the file shows the field being *used*:

> 1. **Declare it as exceptional**, per the typicality line in `00_RUNBOOK.md` and `05` §7.
> 2. **Name which findings depend on the co-write**, so a later reader can tell which technique transfers.

and the obligations the grade is about, `01` **§2.2**:

> **Threshold 3→4** — *"Above this threshold a location **must** be decomposed into sub-locations"*
> **Threshold 4→5** — *"Above roughly a million, **the location no longer has a culture; it has a statistical
> shape.**"*

## MOVE — and what changed my mind

### 1. The field's referent is the pass, and the spec says so without needing `R-4`

Per the brief I decide the field **as currently specified**. **As currently specified it already names the
pass, not the place.** Its gloss is *"so a later reader can tell **which technique transfers**"* — findings
about a place do not "transfer as techniques"; **authoring conditions do.** Its only worked use in the file is
a co-write, which is purely an authoring condition. Its neighbors in the block are `Written: ALONE / co-written`
and `Run mode: WARM / COLD`, both authoring conditions. **So I reach `R-4`'s object without relying on `R-4`,
which the brief correctly forbids me from deciding on.**

**Under that reading, this pass's configuration has three components.** Written ALONE: the declared default.
WARM: the standing mode for the 38-city run. **And: Band 5 declared with both of `01` §2.2's MUSTs suspended
by `DR-4`.** That third item is an authoring condition, it is the methodology's own mandatory instrument set
for the declared band, and it is **not running**.

### 2. My Round 1 cell used the EXCEPTIONAL branch's apparatus while writing TYPICAL on the line

This is what actually moved me. Set side by side, my own Round 1 text reads:

> **Configuration:** TYPICAL — … ⚠ **ONE DECLARED, RULED DEVIATION, named here so a later reader can tell
> which technique transfers** … (A pass cannot correct for a bias it has not declared.)

**Both of those phrases are quoted from §6's `[if exceptional, …]` bracket.** I discharged the exceptional
branch's two obligations — name the deviation, name what transfers — and then wrote the other value on the
line. **A machine-readable header saying TYPICAL over a note saying otherwise is exactly the failure the field
was built to prevent**, and per Field 2's ground 3, the header is what gets read.

### 3. The strongest version of my Round 1 position, weighed honestly and rejected

Reader A flagged it as the reasonable counter: **`DR-4` is corpus-wide, not Davis-specific, and a ruling
applied to all 38 cities *is* the new typical.** I find this fails on two counts.

- **The field's baseline is the methodology as written, not current practice across the run.** `01` §2.2
  states both obligations as MUSTs and **has not been amended**; `DR-4` suspends them — *"suspended, not
  cancelled"* in all three readers' blocks. A pass measured against cohort practice rather than against the
  written method **goes silent precisely when a deviation becomes universal**, which is when a later reader
  most needs it, because **a corpus-wide deviation is a corpus-wide bias** and §6's warning is stated of the
  pass — *"A pass cannot correct for a bias it has not declared"* — not of the pass relative to its cohort.
- **The asymmetry of costs is one-sided.** If the deviation really is universal, grading all 38 EXCEPTIONAL
  misleads nobody — everyone is flagged, the flag is informative about the corpus. **Grading all 38 TYPICAL
  loses the record of a suspension that is explicitly temporary.** When `DR-4` lifts — it lifts once the 38
  cities complete ULM + CST + RWBEM — **38 TYPICAL headers become silently wrong and nothing flags them for
  re-work; 38 EXCEPTIONAL headers *are* the worklist.**

### 4. One refinement on Reader B, which I accept only in part

B gives two grounds, `(a)` the deferred Band 5 machinery and `(b)` that the band was set on a **capacity**
criterion over a frame-description one, the three T8 readers having unanimously recommended Band 4 and been
overridden. **I adopt `(a)` as the ground of the grade.** **I would demote `(b)`.** The band-straddle itself —
1,158,314 → Band 5 and 781,596 → Band 4, **crossed inside Davis's own declared frame** — is a fact about the
*place and its frame*, and the Configuration field is about the *pass*. **It belongs in the Population band
cell's prose, where all three readers already put it**, and mixing it into the grade's ground invites the next
reader to grade Configuration on how unusual the *city* is. B's real `(b)` — that the governing figure was
fixed by ruling on a criterion the methodology does not itself state — **is** an authoring condition and is
worth one line, but it is secondary: it changes *which number*, where `(a)` changes *what the pass can do*.

### 5. What must be listed, since EXCEPTIONAL obliges a list

§6 requires the findings that depend on the exceptional property. **A's and B's lists converge and are
correct**; I would carry them merged, and they are the reason the grade matters rather than being a formality:

- any claim of the form *"what Davis is like"* that lands as a **single answer where a spread is owed**;
- anything **scaled off the 1,158,314 aggregate** rather than off a per-sub-location figure;
- any category answered **`Uniform`** under `01` §5.4 — because `Delegated` has nowhere to go with no
  sub-location passes in existence, and §5.4's own warning is that *"A Band 4+ pass that answers everything as
  Uniform has not been written at its own scale"*;
- the **`G8` composition readings**, which are the most distribution-shaped material in the set and are
  precisely what a Band 5 analysis would have consumed.

## What my own Round 1 reading would cost, concretely, in this pass

1. **It disarms the only line in the block that tells a later reader this pass ran without its band's
   instruments.** `01` §2.2's warning is unconditional — *"A Band 5 pass that reads like a Band 3 pass has
   committed the scale error named in `00c` Gate 11 and `00d`"* — and B's Round 1 finding is the one that
   matters here: **the deferral suspends the remedy, not the risk, and no gate in the set catches a
   Band-3-shaped answer**, because (LAW 0's own words) the gates *"confirm a pass is not wrong. None of them
   can tell you it is not thin."* **`TYPICAL` removes the last declared warning about the exact failure nothing
   else can detect.**
2. **It hides the deferral from the re-work sweep that will have to happen.** `DR-4` is explicitly temporary.
   **Whatever is graded TYPICAL today will not appear on the list of passes needing a distributional layer
   added when the deferral lifts.**
3. **It costs nothing to be wrong the other way.** If `EXCEPTIONAL` turns out to be over-declared, the penalty
   is one extra paragraph a later reader can ignore. **If `TYPICAL` is wrong, the penalty is a scale error
   carried silently into eleven phases and into whatever is built on them.** Under a methodology whose LAW 0
   is *depth over speed* and whose recorded self-audit bias *"has run in one direction — toward flattering the
   pass — on every occasion it has been measured,"* **the grade that flatters the pass is the one that needs
   the higher bar, and it did not clear it.**

**FIELD 3: Configuration = EXCEPTIONAL — MOVE**

---

# FINAL LINES

```
FIELD 1: Settlement + NO modifiers — `Resettled` NOT assigned — HOLD
FIELD 2: Extent band = UNDETERMINED (filed REQUESTED) — MOVE
FIELD 3: Configuration = EXCEPTIONAL — MOVE
```

---

## Resulting tallies across the three readers, after this round

| Field | A | B | C (Round 3) | Standing |
|---|---|---|---|---|
| **1 — `Resettled`** | assigned | declined | **declined** | **2–1 against assignment.** Not unanimous. **Named below.** |
| **2 — Extent band** | UNDETERMINED | UNDETERMINED | **UNDETERMINED** | **3–0. Resolved.** |
| **3 — Configuration** | EXCEPTIONAL | EXCEPTIONAL | **EXCEPTIONAL** | **3–0. Resolved.** |

## The one thing that goes to the developer unresolved

**Field 1 is a real 2–1, and the split is not about Davis.** It turns on a reading of `01` §1.2 the file does
not settle:

> **Does `Resettled` require a prior resident *population*, or does prior *occupancy* suffice?**

§1.2's row says *"the second population … the first"* and §3's `Transit-only` row leaves maintainer-residency
explicitly open, which is why B and I read it the first way. **`01` never states the test.** A ruling either
way would settle Davis **and** would settle the same question at nearly every remaining city in the 38-city
run, since most Tepenian cities are founded on real station sites with rotating-operator histories. **Worth
one ruling, made once, recorded in `01` §1.2 itself rather than in a pass.**

**Second, smaller, and not mine to fix:** if Field 1 is ruled toward assignment, **A's Note B becomes the next
question** — A records that `01` §1.1's *"Expect this doubling wherever a setting's history includes
purpose-built outposts that outlived their purpose"* and this universe's GPS law **point in opposite
directions for every Tepenian city founded on a real station site.** A flagged it as structural and declined to
resolve it. **I agree it is structural and I also decline.** It is a methodology-level conflict, not a Davis
call, and it will recur on schedule.
