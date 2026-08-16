# Character Development Methodology — Overall Process Scaffold

**What this is:** a broad-scale architecture map of the whole methodology pipeline. **Refreshed 2026-08-09** —
the original version of this file was written as a pre-consolidation map, pointing at roughly 3,459 lines of raw
material in `Character_Development_Methodology_-_DRAFT_Ideas.md` and flagging what each stage would eventually
need to reconcile. All of that reconciliation is now done; every stage file is complete. This refresh replaces
the old "here's what needs sorting" framing with an accurate summary of what's actually in each finished file,
plus the intake layer (`00a`/`00b`) that didn't exist when this scaffold was first written. This file is still
the map, not the territory — full detail lives in each stage's own file.

**Why five stages, and what each one actually does:**

1. **Input Information** — everything that has to already exist, or be gathered, before any generative work
   starts on a given Doll.
2. **Information Processing** — the diagnostic toolkit: techniques for interrogating raw inputs to surface a
   genuine, specific psychology, rather than starting from a blank page or a generic trait list.
3. **Character Data** — the actual structured output of Stage 2, written down as reusable fields on a Doll's
   psychological profile (as distinct from the existing `Character_Spec_Fill-In_Sheet_Template.md`, which is
   surface/mechanical data, not this deep layer).
4. **Story Material** — converting a finished Character Data profile into actual story scaffolding: her role,
   her supporting cast, her thematic shape, what kind of story she's even in.
5. **Beats, Paths & Results** — the full beat-by-beat structural machinery, branching into every possible arc
   type, path, and ending a given Doll's story material can resolve into.

Downstream stages consume upstream ones. Stage 5 can't be built without Stage 4's story material; Stage 4 can't
be built without Stage 3's character data; and so on.

---

## The Intake Layer — `00a` and `00b`, Added After This Scaffold Was First Written

Not one of the five numbered stages — a compression layer sitting in front of Stage 1, built specifically for
scale: the developer's actual Doll count (1,185 and climbing toward the Outer Tepenia trilogy and Cryptograph
Helix) makes manually filling in Stage 1's full field set per Doll unworkable.

- **`00a_Initial_Input.md`** — the minimal seed-field intake (name, a doll-folder pointer if one exists, a rough
  vision statement, robot/human, Enneagram if known, location of origin if known — the last two with an explicit
  "you decide" escape hatch) plus the full Derivation Protocol mapping those six seeds onto every one of Stage
  1's 25 categories, deferring what genuinely doesn't need to exist yet (introduction-scene context, the full
  relationship web, exact ending concepts) rather than front-loading everything.
- **`00b_Clarification_Protocol.md`** — the repeatable algorithm for resolving whatever 00a's derivation leaves
  genuinely ambiguous, per Doll. Confidence-tags every derived field (Sourced / Strong Inference / Weak
  Inference / Blocked), only ever surfaces a question for a Section A field at Weak-Inference-or-worse with no
  safe default, ranks surviving gaps by downstream leverage (Enneagram highest, then Ghost, then robot/human
  status), and phrases whatever survives as closed-form multiple-choice with a "you decide" option. Validated in
  real use on Ayako Hayashi: zero clarification questions generated, one low-stakes proposed default.

---

## Cross-Cutting Constraints — apply at every stage, owned by none

- **This is a non-linear methodology** (the DRAFT file's own Standing Scope Note) — every beat is defined by
  functional role, never by fixed percentage-of-runtime placement.
- **No Good Endings / Ending Distribution law** — negative endings are a minority, bittersweet is the largest
  category, positive endings are real but never costless. Codified as canon in `Companion_System.md` and the
  district/DLC/main-quest equivalents; Stage 5's Ending-Shape Cross-Mapping Table builds toward this
  distribution.
- **No National Stereotypes** — applies most directly to the Background Taxonomy (Stage 3) and to any
  in-fiction regional-reputation shorthand (flagged explicitly where the villain/anti-hero sheet's Mordred/
  Cornwall example shows the failure mode to avoid).
- **No Level-Scaling** — not a character-psychology concern directly, but a standing law all downstream content
  design still has to respect.
- **The Dual-Outcome Companion Perk law** (`Companion_System.md`) — 2-5 mutually exclusive branches per
  questline, genuine trade-offs. The mechanical skeleton Stage 5's branching content serves.
- **Two stat-check design laws** (added 2026-08-09, synthesized into Stage 5 and now also codified project-wide
  in `Universal_Rules.md`): every skill/stat check in the game reads the player's current, effective stat total
  including temporary buffs, with exactly one exception — Romance Gate 2 checks permanent, unadjusted stats
  only; and a Natural 10 (permanent, never a buffed Adjusted 10) in a stat-based questline approach grants a
  Mastery Dividend, letting the player talk past a real number of subsequent checks within that same questline.

---

## Stage 1 — Input Information: complete

**File status:** Section A (12 necessary-field categories, each citing the specific downstream node or tool
that needs it) and Section B (13 optional-but-enriching categories) are both fully built. No open items.

**What it actually contains:** foundational identity facts; the mandatory Enneagram assignment; intended story
role/scope; existing biographical and historical material (the single most input-hungry category, feeding
Stage 3's Ghost node directly); existing mechanical/surface data; world-context reference access (Robot
Universals' Friction Bank chapters, relevant District Megasheets, faction/religious canon); the project's
standing design-law constraints; the writer's one-time Mirror Interview priming answers (not a per-Doll cost);
existing narrative introduction context; existing supporting cast; existing questline/ending concepts; and a
memory/prior-notes check. Section B covers soft-detail delivery material, speech/dialect notes, reputation,
a pre-existing Basic Headline if one exists, extended relationships, food/music preferences, "Tribe," existing
voice specimens, concept art, secondary foils, cross-media appearances, prior playtesting, and the developer's
own unformalized instincts.

---

## Stage 2 — Information Processing: complete

**File status:** Governing Principles, two consolidated technique-nodes, four standalone tools, and a
troubleshooting checklist are all built. The original scaffold's "three overlapping motivational-axis systems"
question is resolved: Enneagram stays the mandatory primary axis, Direction (Swain's five wishes) is an optional
secondary lens (moved to Stage 3 as a data field), and Compelling Need (Maslow) stays in Stage 2 specifically
because it's situational — what's driving her *right now* — not a fixed trait.

**What it actually contains:** four Governing Principles (Backstory Proportionality, the Consistency Caution,
the developer-refined Mystery Caution — full resolution stays in private design notes, delivered in media only
through soft ambient detail — and the "Character Is Not You" caution); two consolidated nodes (the Why Chain/
Interrogation Technique, merging Card and Boutros; Self-to-Character Memory Mining, merging Boutros's Mirror
Interview and Corbett's defense-mechanism excavation); and four standalone tools (the In-Voice Character
Interview, Obstacle Brainstorm-and-Triage, the Scenario Diagnostic Template — still the single most fully-built
tool in the whole methodology — and Compare-and-Contrast Self-Image, plus Compelling Need and the Public/Private
Values Gap).

---

## Stage 3 — Character Data: complete

**File status:** the vocabulary reconciliation flagged as "real, undone work" in the original scaffold is fully
resolved. Six previously-competing Want/Need-style triads are consolidated into seven canonical nodes, with
every source vocabulary named explicitly so nothing was silently lost. A full per-Doll fill-in worksheet
(tier determination, construction order, Stage 2 cross-references) exists on top of the vocabulary. No open
items.

**What it actually contains:** a front-gate tier system (walk-on/minor/major, bridging Stage 3's Drift-vs-Drive
question with Stage 4's Character Hierarchy); seven consolidated nodes (Want, Need/Truth, Lie/Flaw, Ghost,
Desire/Motive — including the flagged Boutros/Truby "Desire" terminology collision — Greatest Fear, and the
Background Taxonomy); eight standalone fields; a diagnostic test; a two-tier coverage-checklist system (the
12-Category Notebook as master checklist, the Ten Ways as a separate delivery-channel audit); and the Six Life
Arc archetype assignment, explicitly flagged as pre-built content for the existing nodes, not a seventh
competing vocabulary.

---

## Stage 4 — Story Material: complete

**File status:** the consolidation pass, the Player-Necessity Rule (added 2026-08-09, synthesized from this
project's own already-mature `Companion_System.md` methodology, not book-mined), and a full worked example
(Calethina) are all in place. No open items.

**What it actually contains:** a three-step Front-Gate/Sequencing Trio (MICE Quotient → Character Hierarchy →
Story Problem vs. Character Problem); one genuine merge (Contagonist, absorbing Corbett's Counterweight); Impact
Character and Revenant kept deliberately separate after a near-merge turned out to lose real information, with
the non-Truth-aligned Revenant case routed to the villain/anti-hero sheet; standalone tools (the Normal World,
the Characteristic Moment, Antagonist vs. Antagonistic Force, the Twelve Archetypal Antagonists, Four-Corner
Opposition, the Four Elements of Relationship Sizzle, Corbett's remaining functional-role catalogue);
composability notes between orthogonal systems; two staging/sympathy techniques surfaced late (Card's general
sympathy-lever catalogue, Boutros's cat-save/delay-the-worst-act); the Player-Necessity Rule and its four
supporting constraints (the categorical-block sanity check, the compounding-reasons technique, the no-escort-
quest constraint, retrofit discipline); and the Calethina worked example, which surfaced a concrete design gap
(a missing Tempter figure) rather than just confirming what already existed.

---

## Stage 5 — Beats, Paths & Results: complete, three deliberately-deferred items

**File status:** the Midpoint Menu, the full canonical beat sequence, the Branching Investigation-Route
Structure (added 2026-08-09, alongside Stage 4's Player-Necessity Rule, both from the same source), the Act 3
micro-sequence, arc-type beat implications, chiastic mirroring, the Ending-Shape Cross-Mapping Table, and two
full worked examples (Calethina, Ayako Hayashi) are all in place. Three items remain open, all Doll-specific
real-world dependencies, not methodology gaps — see below.

**What it actually contains:**
- **The Midpoint Menu** — twelve interchangeable Midpoint mechanics (not one canonical beat), spanning fully-
  sourced entries (Bell's two-type Mirror Moment, Weiland's Moment of Truth, the Negative Arc's Refused
  Redemption), Snyder's False Victory/False Defeat, and broader craft-convention entries, plus three
  supplementary cross-references. Two naming collisions were caught and resolved during construction ("Point of
  No Return" and "False Victory," each independently colliding across two different mined sources).
- **The full beat sequence** — Weiland's 11-beat skeleton as the canonical spine, with every other source's name
  for the same beats folded in as a glossary rather than treated as competing, plus the generalized
  Trigger-Type Design Pattern for Inciting Event construction (one thematically-matched trigger type per
  companion, 7-16 concrete instances, a small non-district-bound subset).
- **The Branching Investigation-Route Structure** — synthesized from `Companion_System.md`'s already
  in-production Personal Questline Design Rule, not book-mined: minimum 5 deterministic stat-based approaches to
  the same player-unique task, non-stat world-state approaches at a floor of 3 (target 7-12), a route-validity
  QA check, a menu of recommended non-stat route archetypes (faction-antagonism, Wild Child with a six-flavor
  taxonomy, Long Vigil), and a multi-companion non-overlap principle. Distinct from the Trigger-Type Design
  Pattern: that one gates questline *entry*, this one gates the *middle*.
- The Act 3 micro-sequence, the Three Arc Types' beat-level implications, chiastic mirroring, the Ending-Shape
  Cross-Mapping Table (with its own flagged Disillusionment "straddle" case, now confirmed twice in independent
  real-world Doll data — Calethina's Accord ending and Ayako's own questline design), series-spanning arc
  models, common ending failure modes, and QA tools.

**The three open items**, all deferred pending real-world context rather than unresolved methodology:
1. Calethina's Second Pinch Point — genuinely undetermined pending more district/world development.
2. The specific trigger content for Calethina's own "Unusual Readings" system (the system itself is resolved
   and written into her project file; the 39+ district and 20-40 non-district individual triggers are not yet
   designed).
3. The Ending-Shape Cross-Mapping Table's blind spot for reactive/Flat-Arc-adjacent companions (the Accord edge
   case) — a real, named limitation of the table as built, not smoothed over.

---

## Cross-Stage Notes

- **The vocabulary reconciliation the original scaffold flagged as undone is now fully resolved** — see Stage 3
  above. Nothing carries forward from the old "at least five different Want/Need-style triads" note.
- **Convergent-across-independent-sources findings kept accumulating past the original three**: beyond Truby/
  Corbett's split-theme technique and the coping-mechanism convergence already noted originally, real-world
  Doll data has now independently confirmed the Ending-Shape table's Disillusionment straddle twice (Calethina,
  Ayako) and turned up two beats (Ayako's Inciting Event and First Plot Point) that were already established
  canon before this methodology ever touched her file — worth continuing to treat this as validation, not
  coincidence, whenever it recurs.
- **Two genuinely different source types now feed this methodology, worth keeping distinct.** Stages 1-3 and
  most of 4-5 come from book-mining (the craft-theory DRAFT file). The Player-Necessity Rule, the Branching
  Investigation-Route Structure, and the two stat-check laws come from a different source entirely: this
  project's own already-mature, in-production `Companion_System.md` methodology and the real companion files
  built on it. Both are legitimate, but they carry different evidentiary weight and different revision paths —
  the book-mined material can be re-checked against its source books; the in-production material should be kept
  in sync with `Companion_System.md` and `Universal_Rules.md` directly, since those files, not this methodology,
  are the actual source of truth for anything now codified as project-wide canon.
- **The villain/anti-hero supplement sheet remains a parallel, not subordinate, resource** — feeds Stage 4
  (antagonist/villain story material) and Stage 3 (irredeemability thresholds), kept deliberately separate.
- **Two real worked examples now exist** (Calethina: Stages 4-5; Ayako Hayashi: full Stages 1-5), both
  documented in their respective stage files and cross-referenced in project memory
  ([[project_calethina_lie_and_tempter_gap]], [[project_ayako_hayashi_pipeline_findings]]). A third and fourth
  Tier-1 candidate (Vosora Lashár Tanslock, Ji-Eun Kim) were identified during the roster survey and are ready
  for the same treatment whenever useful.

---

## What This File Is Not

Not the finished methodology in full — that's the seven files it maps (`00a`, `00b`, `01` through `05`). This
file is the navigational summary, refreshed to stay accurate as of 2026-08-09; if any stage file changes
substantially again, this scaffold should get another pass rather than being left to drift stale a second time.
