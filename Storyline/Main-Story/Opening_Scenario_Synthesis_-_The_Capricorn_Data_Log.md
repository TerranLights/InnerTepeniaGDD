# Opening Scenario Synthesis — The Capricorn Data Log

**What this is:** a proposed upgrade to the opening-task candidates in
`starting_task_possibilities_-_Act_1_-_leaving_Calethina's_lab.md`, written up as its own file specifically
because the developer flagged it as "something we'll need to come back to" — a real design direction, not
yet locked in. Written 2026-07-23, cross-referenced from `Tutorial_Section_Specification.md`'s "Still Open"
list.

---

## Where this came from

The original Grok-drafted `Main_Story-Hook_Progression.md` (June 22, 2026) already sends the player to
Capricorn early and already has them retrieve a data log there — Beat 2's own "Outcome" line reads
*"Acquisition of a key data-core revealing the broader systemic energy crisis,"* fed by an environmental hook
of "sabotaged production line or quota logs showing power diversions hitting residential areas hardest."

**The problem:** as originally written, this is a flat retrieve-and-read beat. There's no choice in *how* the
player gets the log, no reputation stakes attached to the method, and none of the resolution-path variety the
game's own climax (Beat 11's Talk/Sneak/Fight structure) later relies on. It does its narrative job but
teaches the player nothing about how the game actually plays.

This matters because `Main_Quest_Revised_Beat_Structure_TENTATIVE.md`'s current Beat 1 already commits to
this same Capricorn data-log beat, now explicitly as the vehicle for the planted (not resolved) Capricorn
rigged-historical-judgment thread. **This synthesis doesn't replace that commitment or the "Heating Grid
Failure" opening-task lean** — the heating-grid crisis is what plausibly sends the player to Capricorn in the
first place (per the original draft's own NPC hook: "industrial districts are cutting power... investigate
the factories"). This file specifically answers the *unresolved* question of what actually happens once the
player arrives there.

## The synthesis

Once in Capricorn, the data log the player needs is held behind a live standoff between three parties already
present in the original Grok draft's own NPC hooks for this beat: a **factory foreman** (management,
blames residential districts), **floor workers** (labor, resentful of overclocking demands), and a
**black-market contact** operating in the industrial zone. Rather than picking one NPC to talk to and moving
on, the player chooses *how* to get the log — and each method is a distinct resolution path, mirroring the
climax's own Talk/Sneak/Fight structure in miniature:

- **Force** *(Fight-coded)* — pressure or confront the foreman directly for access. Likely gated by
  Might/Nerve; can escalate into the tutorial's one real combat encounter if it goes wrong.
- **Negotiate** *(Talk-coded)* — work the labor angle, trade something the workers need for their help getting
  the log. Likely gated by Humanity/Nerve — the Reputation Matrix's first real registration point, since
  siding with labor vs. management here plausibly moves rep in opposite directions.
- **Quiet** *(Sneak-coded)* — pull the log off a terminal without either side noticing, using the black-market
  contact's own smuggler access or a straightforward Agility/Investigation/Hacking check. This path doubles as
  a natural candidate for the tutorial's unmarked-discovery requirement, if the terminal itself isn't flagged
  by a quest marker.

**Whichever path the player takes, the log itself still contains the same planted thread** (the evidence
toward Capricorn's rigged historical judgment) — the method changes reputation consequences and framing, not
the core information delivered, so the beat's existing narrative commitment stays intact regardless of how
the player gets there.

## Why this is better than the flat original

Checked against `Tutorial_Section_Specification.md`'s own checklist, this single scenario — rather than a
separate side-scenario bolted on — hits:

- MACHINE stat check mattering immediately (varies by path).
- Tag skill payoff (Hacking/Persuasion-adjacent skills matter differently per path).
- Reputation Matrix's first registration (siding with labor vs. management vs. the black market).
- One real combat encounter (available via the Force path, not forced).
- An unmarked discovery (available via the Quiet path).
- The robot-human relations baseline, legible through the foreman/worker dynamic itself.
- The planted-not-resolved hook, unchanged from the existing beat-structure commitment.

The original Grok version hit essentially none of these on its own — it was a narrative beat with no systemic
teaching function attached.

---

## Still Open

- Exact NPC names for the foreman, worker contact, and black-market contact — none assigned yet.
- Whether all three paths are fully mechanically distinct (their own skill checks, their own combat/stealth/
  dialogue systems exercised) or some are lighter flavor variants of each other.
- Where this scenario sits relative to the tutorial's first level-up — before, during, or immediately after.
- Whether choosing one path forecloses the others entirely, or whether a failed attempt at one gracefully
  routes into another (Fallout-style failure-forward design, worth checking against this project's own
  precedent conventions before deciding).
- Final confirmation that "The Heating Grid Failure" is in fact the chosen opening-task trigger — this
  synthesis assumes that lean holds, but it isn't locked in the source file.
