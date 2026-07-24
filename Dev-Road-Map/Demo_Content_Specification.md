# Demo Content Specification

**What this is:** a working spec for what actually ships in the free Demo build, distinct from the Early
Access content-split plan in `Early_Access_vs_Launch_Content_Split.md` and the conceptual distinction drawn
in `Demo_vs_Early_Access.md`. Written 2026-07-23. Several items below are genuinely undecided and flagged as
such — this is a first pass, not a locked spec.

---

## 1. Where the Demo starts and ends

Grounded in the actual starting sequence from `Storyline/Main-Story/Main_Quest_Revised_Beat_Structure_TENTATIVE.md`:

- **Opens** at Calethina's Engineering & Activation Lab, on the Cancer/Taurus border — the player's actual
  game-start location. Includes the lab intro itself (meeting Calethina, the player's own Bridge Unit
  awakening) and the choice of whether to accept her opening request at all (declining and wandering off on
  one's own is a real, designed option — worth preserving in the Demo precisely because it demonstrates the
  game's own non-linear philosophy in miniature).
- **Recommended endpoint: the end of Beat 1 (Capricorn)** — the heating-grid diagnostic, the industrial-
  pressure content, and the planted (not resolved) thread about Capricorn's rigged historical judgment. This
  gives a full "spark → first real district → first real hook" arc: a complete emotional unit, not a
  cliffhanger mid-scene.
- **Open:** whether the Demo should also let a player wander into Cancer or Taurus proper (both visible from
  the lab, per the corrected starting-location note) as optional exploration space, or stay strictly on the
  lab→Capricorn critical path. Leaning toward allowing it — free-roam taste is part of what a CRPG demo needs
  to sell — but not decided.

## 2. Companions

- **No full recruitable companion in the Demo.** This mirrors the Early Access plan's own Flora/Junction-12
  substitution logic (`Early_Access_vs_Launch_Content_Split.md` Category 2) one step further down: if Flora's
  own recruitment scene gets replaced by a non-recruitable human NPC even in Early Access, the Demo — a
  smaller, earlier, unpaid slice — should do the same. The repair crew at whatever the opening diagnostic
  site turns out to be (Thermal Distribution Junction 12, per that file, if "The Heating Grid Failure" is the
  chosen opening task) is led by that same non-recruitable NPC stand-in.
- **Reasoning:** companion romance is confirmed as one of Early Access's own headline draws (per that file's
  2026-07-10 resolution) — spending it in a free Demo would blunt the thing Early Access is specifically
  supposed to convert into sales. The Demo's job is proving the game's tone, systems, and writing quality, not
  pre-spending its own biggest draw.
- **Open:** whether it's worth teasing one companion at a glance (visible, named, clearly important, not yet
  recruitable) purely as a hook — no decision made here.

## 3. Systems that need to be represented

A Demo's job is proving the core gameplay loop works and reads well, so it should include a working (if
shallow) taste of each pillar system, not just narrative:

- **Turn-based isometric combat** — at least one real encounter, enough to show the core loop.
- **MACHINE stat system** — either a pre-generated starting character with visible stats, or (if character
  creation itself is meant to be a selling point) a trimmed character-creation pass. **Open** which.
- **Dialogue/skill-check system** — Capricorn's own industrial-pressure content and the planted historical-
  injustice thread both naturally exercise this.
- **The throwing-weapons system** (`Game-Mechanics/Combat/Throwing_Weapons.md`) — the retrieval mechanic is
  distinctive enough to be worth surfacing even in a short slice.

**Deliberately excluded, too soon or too large for this scope:** the full perk/leveling arc, the Conflict-
Accumulation System (only becomes legible across many beats), any DLC content, and "throw anything" (already
confirmed Launch-exclusive, not even in Early Access).

## 4. Technical/structural constraints

Per `Demo_vs_Early_Access.md`:

- **Free**, no purchase gate.
- **Frozen build** — the Demo isn't expected to be rebuilt in response to player feedback the way Early
  Access is; budget for a stability/polish pass before release, then leave it largely static except for bug
  fixes.
- **No save carryover** into Early Access/Launch — a separate Steam depot tied to the main store page, not a
  truncated version of the same save-compatible build.
- **Runtime target:** a single, complete sitting — commonly 20-60 minutes for CRPG demos of this kind.
  **Open:** no specific target chosen yet; worth timing against the actual Beat 1 content once it's built out
  in-engine.

## 5. What the Demo needs to prove, as a checklist

- The tone and writing quality (the game's central creative pitch — the two north-star questions in
  `user_creative_principles`) come through even without a companion romance arc present.
  This checklist maps directly onto the Steam wishlist-conversion goal in `Steam_Launch_Strategy_and_AI_Disclosure.md` Section 2 — a Demo that fails any of these items is unlikely to convert into a wishlist.
- Combat feels good in a single real encounter.
- The MACHINE stat system's basic shape is legible even from a short slice.
- The district-investigation loop (arrive → gather data/testimony → partial resolution → a planted, unresolved
  hook) reads clearly as the game's own recurring structure.

---

## 6. The New Vegas Lesson: build this content last, not first

Added 2026-07-23, per a design principle the developer specifically drew from interviews/documentaries about
*Fallout: New Vegas*'s own production. Goodsprings, New Vegas's opening area, was deliberately designed and
finalized **late** in development, not early — precisely because its job is to function as a representative
summary of every major thing the player will definitely experience over the full game, which means it can't
actually be locked down until the rest of the game's systems, tone, and content are known well enough to
summarize. See `feedback_fallout_precedence_law` — New Vegas is this project's own standing precedent source
for design questions like this one.

**Two direct implications for Inner Tepenia's Demo, since the Demo's content *is* the game's own opening
sequence:**

1. **Production order, not just content scope.** The Demo shouldn't be treated as "the easy early content,"
   buildable first because it's chronologically first in the story. It should be one of the **last** major
   content pieces locked down — built and iterated on only once combat, the MACHINE stat system, dialogue/
   skill checks, and the district-investigation loop are all far enough along elsewhere in the game to
   actually be represented accurately. Building it early risks the Demo shipping a version of these systems
   that gets meaningfully revised later, making the Demo an inaccurate preview of the real game by the time
   Early Access or Launch arrives.
2. **Design mandate, not just checklist.** Section 5's "what the Demo needs to prove" checklist isn't just a
   QA pass to run once the opening content exists — it's the actual brief the opening content should be
   *designed against* from the start. Calethina's lab intro and Beat 1/Capricorn should be deliberately
   engineered as a compressed, representative sample of the full game's major systems and tone (per the
   Goodsprings precedent), not merely "whatever the first story beat happens to contain that also
   incidentally teaches the player something."

**The genuine tension this creates, left open rather than resolved here:** Section 2 of
`Steam_Launch_Strategy_and_AI_Disclosure.md` recommends launching a Demo well *before* Early Access to build
wishlist velocity and land a Steam Next Fest slot — which pushes toward building the Demo *early*. The New
Vegas lesson above pushes the opposite direction — toward finalizing it *late*. One resolution precedent worth
naming: Goodsprings itself still existed in a rough, playable form throughout most of New Vegas's own
production — it was iterated on repeatedly, not built from a blank slate at the very end. The likely shape for
Inner Tepenia is the same: **rough out the Demo's content early enough to hit a Next Fest window, but treat it
as a living draft that gets revised alongside the rest of the game, with a final polish/finalization pass
deliberately scheduled late** rather than a single early build and then no more.

---

## Still Open

- Exact opening-task choice among the 8 candidates in `starting_task_possibilities_-_Act_1_-_leaving_Calethina's_lab.md`
  — "The Heating Grid Failure" is only a lean, not confirmed, in the source beat-structure file itself.
- Whether free-roam into Cancer/Taurus is included alongside the Capricorn critical path.
- Whether one companion gets a glimpse/tease without being recruitable.
- Pre-generated character vs. trimmed character creation.
- Target runtime.
- Timing relative to Early Access launch and any specific Steam Next Fest window.
- The exact rough-draft-then-finalize schedule described in Section 6 — no specific milestones chosen yet for
  when the Demo's content gets its first playable pass vs. its final polish pass.

See `Tutorial_Section_Specification.md` for the fuller, standalone brief on what the tutorial/opening sequence
itself needs to contain — since that content and the Demo's content are the same sequence, that file expands
on Sections 3, 5, and 6 above in more detail.
