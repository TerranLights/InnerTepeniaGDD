# Quest Tracking and Active Quest State

**What this is:** a design draft, not a locked decision — written 2026-07-25 to formalize a question the
developer raised directly: the player must be able to have **no quest tracked at all**, as a real, explicit
state, not just an absence. Consolidates the existing (but scattered) quest-marker discussion from `TODO.md`'s
"Quest Marker Design" entry (flagged 2026-07-07, deliberately deferred) into one place, and adds the
active-quest-state question that entry never covered.

---

## The Core Problem

Cyberpunk 2077 (2020s) still gets this wrong in places Fallout: New Vegas (2010) mostly didn't have to worry
about, because NV's own UI never forced a persistent, always-on-screen tracker the way many modern
open-world HUDs do. The lesson isn't "old games solved this" — it's that **whichever quest happens to be
tracked should be the player's own explicit, current choice, and "nothing tracked" needs to be just as valid
and just as reachable a choice as any specific quest.** A quest log that silently defaults to auto-selecting
whatever was last touched, with no clean way back to "nothing," is the actual failure mode worth designing
against from the start.

**Why this matters for Inner Tepenia specifically, and matters more for Outer Tepenia:** Inner Tepenia's
confirmed camera (`Movement_Camera_and_Grid_System.md`) is a free-rotating 3D isometric camera deliberately
modeled on Baldur's Gate 3's own — this genuinely lowers the practical stakes here, since there's no
persistent first-person HUD compass/arrow nagging the player every second the way there would be in a
real-time, over-the-shoulder game. The three-future-game Outer Tepenia trilogy doesn't get that same cover —
a real-time game with an active tracker is exactly where this problem bites hardest (see the Cyberpunk 2077
comparison above). Building the underlying tracking-state discipline correctly here, even though the camera
partially masks the issue, is what makes it a solved problem by the time it actually matters.

---

## The Three-State Model

Quest tracking should always resolve to exactly one of three states, never anything murkier:

1. **A specific quest is actively tracked.** Whatever UI/marker treatment the eventual marker-design decision
   settles on (see below) applies to this one quest and no other.
2. **No quest is tracked.** A first-class, always-reachable state — not the absence of state 1, but its own
   deliberate option in the quest log UI. Selecting it should feel exactly as intentional as selecting any
   specific quest.
3. *(Not really a third state, but worth naming explicitly so it isn't conflated with #2):* **quests that are
   never trackable at all**, per the existing Cradle unmarked-content precedent (`Design_Principles.md`
   Section IV) and the confirmed unmarked-questline category (`TODO.md` line 682) — no journal entry, no
   marker, no tracker, by design. This is different from a player *choosing* state 2 for an otherwise-
   trackable quest; it's a quest that was never eligible for tracking to begin with.

**UI implication:** the quest log needs an explicit "Track Nothing" (or equivalent) option sitting in the same
list as trackable quests, not a separate settings toggle buried elsewhere. It should be exactly as easy to
reach as tracking any individual quest.

---

## The Named Anti-Pattern — Cyberpunk 2077's "No Way Back"

**The exact failure, described directly by the developer, binding to avoid across the whole series:** the
player is tracking Quest FF (or tracking nothing, deliberately). An unsolicited trigger — a phone call, a
region entered, anything not initiated by the player — auto-activates Quest HJ, and the tracker silently
switches to it. The player finishes HJ. The tracker does **not** return to FF (or to nothing). Instead, it's
now sitting on whatever *other* quest, Quest ABC, happened to auto-update most recently — something the
player may never have chosen to track at all, and has no memory of asking for. There is no way back to what
the player actually wanted tracked, ever, without manually hunting through the log.

**Why this is worse than it sounds:** it isn't just that the tracker changed without asking — it's that the
change is **permanent and untraceable**. The player's own deliberate choice is gone, replaced by whatever
happened to be the most recent side effect of an unrelated system, with zero path back to their actual
intent. This must never happen in any Tepenia game.

### The Fix — Two Layers, Preferring the First

**Preferred solution: never let the persistent Tracked Quest change without the player's own explicit
action, full stop.** Split the concept in two:
- **Tracked Quest** — the persistent, player-controlled selection from the Three-State Model above (a
  specific quest, or deliberately nothing). This *never* changes except by direct player input.
- **Objective Prompt** — a separate, transient, event-driven UI element for something time-sensitive
  happening *right now* (the phone call, the region trigger). It can appear, show its own steps, and
  disappear when resolved — entirely without touching the Tracked Quest underneath it. When HJ's prompt
  clears, FF (or nothing) is still exactly what's tracked, because it was never actually altered.

This is the stronger fix, because there's no state to restore — nothing was ever silently changed in the
first place. It fully avoids the entire class of bug, not just the specific scenario above.

**Fallback, if the UI genuinely needs the main tracker itself to display the interrupting quest (e.g., a
full quest-step breakdown that doesn't fit in a transient prompt):** implement a strict **return-address
stack**, the same shape as a function call stack. Before switching to display HJ, push the current state
(FF, or nothing) onto the stack. When HJ resolves, pop back to exactly what was pushed — not to whatever
else happens to have updated in the meantime. **Critical rule:** if the player manually changes tracking to
anything at all while HJ is displayed, that explicit choice immediately overwrites the pushed stack entry —
the restore-on-completion behavior must never fight a player's own later decision. Only auto-triggered
completions restore automatically; explicit player choices always win outright.

**A quest merely becoming available or updating in the background during the interruption (Quest ABC in the
example) must never itself claim the tracker slot.** Only the specific quest that caused the interruption is
allowed to (temporarily) claim display space; anything else just gets added to the log, silently, for the
player to find and choose later if they want to.

---

## How This Interacts With the Undecided Marker Question

This document doesn't resolve `TODO.md`'s own still-open "Quest Marker Design" question (which of the four
options — Bethesda-style pinpoint, New Vegas-style approximate region, Elden Ring-style none, or diegetic
markers tied to the PC's own nature — actually gets used). That decision and this one are orthogonal:
whichever marker treatment gets chosen, the three-state model above still needs to hold. If the eventual
decision is "no markers at all," the practical stakes of state 2 shrink (there's nothing on-screen to turn
off), but the underlying journal-selection discipline is still worth having for consistency across the
series and for the quest log's own UI clarity.

---

## Open Questions

- Whether "no quest tracked" should be the actual default state on first entering a new area/session, or
  whether the game should auto-suggest (without forcing) the most recently advanced quest — auto-*suggesting*
  without auto-*selecting* may thread the needle here, but this isn't decided.
- Exact UI treatment of the "Track Nothing" option — a persistent list entry, a keyboard shortcut, both.
- How this state model carries forward into Outer Tepenia's own real-time HUD design — flagged as the more
  urgent version of this problem, not designed here.
- **Which of the two anti-pattern fixes above is the actual commitment** — the separate Objective
  Prompt/Tracked Quest split (preferred, structurally immune to the bug) or the return-address stack
  (fallback, needed only if the UI genuinely can't support a transient prompt). Leaning toward the former;
  not finalized.
