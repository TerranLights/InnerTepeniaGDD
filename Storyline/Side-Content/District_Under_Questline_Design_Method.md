# District Under-Questline Design Method — Input Synthesis & But/Therefore Construction

**What this is:** the method for constructing per-district "under-questlines" — **declared (2026-07-22) to
be non-main content, not side-content.** The distinction matters: side-content is something the player has
to actively go searching for, out of pure curiosity, with little or no natural lead-in (see "Where this
sits," below). An under-questline is instead something the player runs into simply by playing normally —
through an ordinary conversation, or by noticing something at a location they were already exploring — the
way a district's own dedicated NPCs naturally talk about what's actually going on around them. Distinct from
the base game's own single main questline (which spans Concordia as a whole) and distinct from each
district's own main questline, which is instead the role of `District_Main_Questlines.md` (one capstone
quest per district, feeding a district perk and possibly a district-specific player home). Adapted directly
from `Storyline/DLC-Questlines/DLC_Main_Questline_Design_Method.md`, which governs each DLC's own main
questline (one per subnet) — this file governs the same kind of input synthesis and But/Therefore
construction, scaled down to district level.

**Where this sits (worked calibration, Fallout: New Vegas' Novac plus a non-Tepenia contrast):**
- **District main questline** (`District_Main_Questlines.md`) ≈ Manny Vargas sending the player to clear
  RepCONN Test Site — the town's own central, given assignment.
- **District under-questline** (this method) ≈ two different shapes of the same idea: (1) No-Bark Noonan
  mentioning, in ordinary conversation, that something's been shooting *the* brahmin at the McBride Corral
  every night (they're Dusty McBride's brahmin, not No-Bark's own) — leading to Dusty McBride, and then to
  the invisible Nightkin actually doing it; and (2) Boone's own "One for My Baby" — a companion naturally
  opening up about his missing wife, leading the player to investigate Jeannie May Crawford. Neither required
  the player to go hunting for an easter egg; both simply surfaced from playing the location and its people
  naturally.
- **True side-content** (out of scope for this method entirely) ≈ The Witcher 3's "Frying Pan" — a quest
  with essentially no organic lead-in, found only by a player actively poking at something odd out of pure
  curiosity. Nothing in this project currently designs for that tier; noted here only to mark where
  under-questlines stop.

**What makes these specifically "naturally discoverable":** every under-questline candidate should anchor to
a **significant starting point** the player can actually run into through ordinary exploration or
conversation — not a quest-giver handing out a formal assignment, and not something requiring deliberate,
off-path hunting either. Two starting-point categories, matching the two kinds the developer called out
directly: an **internally-relevant in-world figure** (a named individual whose significance is local to the
district, not a headline character — the No-Bark/Boone role), or an **internally-relevant data-point at a
significant location** (something found, read, or noticed at a specific place in the district). This is also
why Step 1's input list below, unlike the DLC method's own, does *not* exclude Notable Figures — see the
note on input 4.

**A settled distinction.** This is *not* the same thing as `District_Main_Questlines.md`. That
file is each district's own main questline: one required capstone quest, built from internal faction
conflicts (`District_Unity_of_Opposites.md`), slotted into Act 2, feeding "District Idolized" and a district
perk/player-home. This method produces everything else naturally discoverable within a district —
non-main, plural, never load-bearing for any ending condition, and not to be confused with true
hunt-for-it side-content either. Both sit in this same folder specifically so they can be reviewed side by
side.

**This is a living document.** It's being formalized after exactly one test run (three "original" and three
"Zodiac-coded" candidates against Leo district) and is expected to be revised as it gets tested against
further districts, situations, and pressures — treat every section below as a working draft, not a settled
specification.

---

## Step 1: Gather Inputs

For the specific district under construction, pull the following — the same "only the distilled findings,
not the whole document" discipline the DLC method uses, adapted for the fact that a district plays the
"city" role here while *Concordia as a whole* plays the "subnet" role a single subnet played in the DLC
method:

1. **The district's own Cross-Reference Synthesis** (`[District]_Cross_Reference_Synthesis.md`) — only
   each Finding's bolded **4th-order effect:** line, plus the closing **Synthesis** section.

2. **Concordia's own Ultra-Megasheet Cross-Reference Synthesis** (`Concordia_Cross_Reference_Synthesis.md`)
   — same rule: 4th-order-effect lines and the Synthesis section only. This is the whole-city analog of the
   DLC method's own subnet-level input 2.

3. **Cross-district Throughways, in full** (`Final_Megasheet_Data_Processing/Throughways/`) — the direct
   analog of the DLC method's subnet-level Throughways input. Take the full resultant finding of each one,
   not just a single line, since Throughways are causal chains by construction.

4. **The district's own Full Extrapolation** (`[District]_Full_Extrapolation.md`), every section **including
   Notable Figures** (Demonym still excluded, same as the original method). This is a deliberate departure
   from the DLC method's own rule, which excludes Notable Figures — that method is building a subnet-wide
   main questline and deliberately avoids centering on a single named individual. This method does the
   opposite on purpose: Notable Figures is one of the two direct sources for a candidate's own starting
   point (see the note above).

5. **Concordia's own Ultra-Megasheet Full Extrapolation, Section I only** — the district's own specific,
   individually-stated theory of how a "true city" gets built. This is a *stronger* version of what the DLC
   method's input 5 provided: a subnet's own Section I only sketched each city's loose role in a collective
   theme, where Concordia's Section I states each district's own explicit civic belief. This is also the
   section the belief-consequence default (Step 2, below) is built directly on top of — treat it as the
   single most load-bearing input in this list.

6. **The existing Questlines layer — both in-district and cross-district**
   (`Final_Megasheet_Data_Processing/Questlines/in-district_questlines/[District].md` and
   `.../cross-district_questlines.md`), wherever the district appears in either. **This has no subnet-level
   equivalent, and it should be weighted higher than the DLC method's own input 6 (lore-history files) ever
   was.** That input was deliberately downweighted because it was raw, untranslated setting-condition
   history. This one is different: it's already written in almost exactly the shape a finished candidate
   needs — a cause, escalating effects, a genuine fork, real trade-offs on every branch. Where a Questline
   Thread already exists for this district, treat it as a strong seed to build from or refine, not merely a
   supplement to skim past.

7. **Whatever plays the "Local Cultures" role for this district** — in practice, this looks like it's
   folded directly into the district's own Megasheet ("Who Lives Here, and Why," "What It Feels Like")
   rather than living in a separate file the way city-level Local Cultures sheets do. Pull those sections
   directly rather than assuming a separate document exists in the same shape.

8. **The Super-Ultra-Megasheet**, wherever it touches Concordia or this specific district — same role the
   DLC method's input 8 played, one level further up the hierarchy.

---

## Step 2: Construct Candidate Chains

Using everything gathered in Step 1, construct candidate But/Therefore chains for this district's own
under-questlines (per the grammar in `But_Therefore_Quest_Design_Method.md`). A floor of **at least 5 per
district, ideally 15-20** — and unlike a district's own main questline (which narrows many candidates down
to exactly one, per `District_Main_Questlines.md`), **under-questline candidates are not narrowed down.**
Every candidate that passes the tests below is kept as actual content — a district can have any number of
under-questlines running in parallel, since none of them compete for the same "main story" slot.

Each candidate must satisfy the same three tests the DLC method uses, plus one new test specific to this
method:

- **Anchored to a starting point.** Name the specific figure or location/data-point (from input 4 or 7)
  the candidate actually starts from — the concrete thing a player runs into through ordinary exploration or
  conversation, not an assignment handed to them and not something requiring deliberate off-path hunting.
  If a candidate can't point to one, it isn't a natural under-questline yet, whatever else it gets right.

- **Non-conflicting.** Doesn't contradict anything gathered in Step 1.
- **Characteristically consistent.** Reads as something that could only happen in *this* district
  specifically — grounded in its own stated civic belief (input 5) and its own established population,
  character, and cross-district relationships (inputs 4 and 7).
- **Actually emergent, not invented.** Traces back to a specific 4th-order effect, Throughway finding, Full
  Extrapolation section, or existing Questline Thread — not a new idea dropped on top of the source material.

**Plus one additional, default rule specific to under-questlines** (confirmed 2026-07-22, after the Leo test
run — see `feedback_district_belief_consequence_default` memory for the full reasoning): **default to
"can this district handle the results of its own belief system," not "is this district's belief system
actually fair, true, or correct."** Each district already holds a sincere civic conviction (input 5) — write
the district as consistently acting on that conviction throughout the candidate, the way any conscious
entity naturally does, rather than maneuvering it toward doubting its own first principles. The escalating
pressure in a candidate chain should test whether *living by* the district's own belief remains sustainable
once real circumstance bears down on it — not build toward the revelation that the belief itself was
mistaken. The belief can surface real, previously-unexamined implications along the way without the
district's own core sincerity collapsing; it's being tested, not talked out of what it believes.

**Cross-district candidates are explicitly allowed, not just single-district ones.** The strongest material
already assembled in the existing Questlines layer (the Recognition Cascade, the Falkland Treaty's three
branches) is cross-district by nature — an under-questline reaching into a second or third district, the
way a subnet's own DLC candidates reached across multiple cities, should be treated as a normal, expected
shape, not an exception.

---

## Worth Your Attention

This method has only been run once, informally, against a single district (Leo, three "original" and three
"Zodiac-coded" candidates, none of them written to file under this method's own name yet, and none anchored
to an explicit starting point since that requirement postdates the test run). Worth testing deliberately
rather than assuming an answer: how the starting-point requirement holds up in practice — whether every
district's Full Extrapolation actually has enough Notable Figures and location-level detail to anchor 5
genuinely distinct candidates without straining — and how the belief-consequence default holds up against a
district whose own civic belief is less performance-and-recognition-coded than Leo's, or against a candidate
that's cross-district by construction rather than single-district.
