# The "But / Therefore" Method — Quest & Plot Design Rules

**Source:** Trey Parker and Matt Stone (South Park), via [perell.com's summary](https://perell.com/note/but-therefore-rule/) and a
[r/Screenwriting discussion thread](https://www.reddit.com/r/Screenwriting/comments/7266rn/) (saved locally in this
folder as HTML, since Reddit blocks direct fetches). Brought in 2026-07-15 as a working tool for DLC
quest design — see `TODO.md`'s DLC entries and `project_dlc_quest_design_plan` memory for the session
this was pulled in to support.

**Status:** a reusable method, not itself a quest or a piece of lore. Nothing here is canon. This
document stays in `to-be-integrated/` until it's proven useful in practice, at which point it should
move to `Storyline/` or a new `Game-Mechanics/Narrative-Design/` location — see the "to-be-integrated/
queue" item in `TODO.md`.

**Companion document:** `But_Therefore_Lore_Design_Method.md` (same folder) adapts this same technique
for *history/culture* design (cities now, subnets and nation-level lore eventually) rather than
player-facing quest beats.

---

## 1. The core rule

Parker and Stone tested this on their writers' room whiteboard: **whenever you can connect two beats
in your outline with "and then," the story is inert. Whenever you connect them with "but" or
"therefore," the story has momentum.**

- **Weak (And Then):** *Jimmy went to the mall, and then he got tired, and then he got a coffee, and
  then he walked back to the lot, and then he drove home.* Every beat is true, in order, and nobody
  cares.
- **Strong (But / Therefore):** *Jimmy went to the mall, but he realized he was tired. Therefore he
  got a coffee. But he'd parked in an illegal spot because he was tired. Therefore, when he got back,
  his car had been towed.*

Nothing in the second version is a bigger event than the first. The only thing that changed is that
every beat is now a *consequence* of the beat before it, and half of those consequences are
*unwelcome*. That's the whole rule.

---

## 2. "But" and "Therefore" are not interchangeable — they do two different jobs

This is the sharpest, most useful distinction to come out of the discussion thread (credit: u/120_pages),
and it's worth holding onto as two separate tools rather than one combined mantra:

- **"Therefore" = consequence.** Something happens *because* of what just happened. This is what
  stops a plot from being episodic — events stop being random and start being caused.
  *Bob proposed to Jill. Therefore, Jill broke up with Dan.*
- **"But" = reversal.** Something happens that **subverts the expectation the last beat just set up.**
  This is what keeps a plot from being predictable, even once it's causally connected.
  *Bob proposed to Jill. But Jill took out a life insurance policy and started plotting with Dan to
  kill him.*

A quest built entirely out of "Therefore" chains is causally sound but can still be flat — one damn
thing correctly causing the next damn thing, with no surprise anywhere. A quest needs **both**: the
"Therefore" beats give it a spine, and the "But" beats keep bending that spine somewhere the player
didn't expect.

---

## 3. The failure mode: "But / Therefore" wearing an "And Then" costume

Flagged directly in the discussion thread, and worth taking seriously: **the words "but" and
"therefore" don't do the work by themselves.** You can write a chain that's technically all
Buts-and-Therefores and is still just a disguised And-Then list, if none of the "buts" are genuine
reversals:

> Our secret agent found the villain's lair — **and then** ran into three henchmen — **and then**
> used the gadget from page ten — **and then** made a lucky escape — **and then** reached a dead end
> — **and then** the henchmen caught up — **and then** her partner appeared in a vent — **and then**
> the villain flooded the vents with gas.

Every one of those beats *could* be phrased with "but"/"therefore," and it would still read as flat,
because each event was already the expected next step. **The test isn't "did I use the word 'but,'"
it's "did this beat actually make the player's situation worse, or force a choice they didn't see
coming, relative to what the last beat implied was about to happen."** If a beat doesn't pass that
test, it's an And Then no matter which conjunction is sitting in front of it.

---

## 4. Worked example, using an actual Inner Tepenia anchor

Applying this to a real, already-established DLC anchor rather than an abstract one — **DLC 5's
Troll Airfield conflict** (Halley subnet; see `Specs/Troll.md`, `TODO.md`'s DLC 5 entry, and
`Halley_Subnet_Ultra_Megasheet`'s own Throughway 1, which already establishes Troll's airfield as the
single point of failure for the whole subnet's freight *and* the national Rastra spare-parts supply):

> The player needs passage through Troll to reach [the rest of DLC 5]. **But** the airfield's control
> is fractured between competing factions, and none of them will grant passage without something in
> return. **Therefore** the player has to pick a faction to help. **But** helping that faction means
> actively worsening Sanay's own freight backlog (Sanay depends on Troll to distribute what it
> receives) — the "help" has a cost someone else pays. **Therefore** the player now has a reason to
> go to Sanay, whether to warn them, make it up to them, or exploit the backlog themselves. **But**
> once at Sanay, it turns out the backlog is *also* delaying Rastra spare parts nationwide — meaning
> the fight over one regional airfield has a supply-chain reach the player didn't expect when they
> first walked in. **Therefore** the "simple" fetch-passage quest has quietly become a decision with
> consequences the player can trace out past the edge of the subnet.

Notice what this does *not* require: no new lore was invented. Every fact used (fractured control,
Sanay's dependency, the national Rastra-parts stake) is already established canon. The method's job
here isn't to generate content — it's to find the causal spine and the reversal points that are
**already sitting in facts you've already written**, and sequence them so the player feels each one
land instead of just being told about it.

---

## 5. Plot schematics

### 5a. The Linear Escalation Chain (single-thread side quest)

For a quest with one throughline and no branching companion/faction stakes attached:

```
SETUP           — establish what the player wants, and why it looks achievable
   │
   ▼ BUT
COMPLICATION 1  — the obvious path is blocked or costs more than expected
   │
   ▼ THEREFORE
ACTION 1        — player does the thing this complication demands
   │
   ▼ BUT
COMPLICATION 2  — that action created a new, bigger problem (not just "more of the same")
   │
   ▼ THEREFORE
ACTION 2        — player commits further, usually with less room to back out
   │
   ▼ BUT
REVERSAL        — the goalposts move; what the player thought they were solving turns out
                  to be a smaller piece of something else (per Section 4's Troll example)
   │
   ▼ THEREFORE
RESOLUTION      — player's choice at the climax is shaped by everything above, not just
                  the original setup
```

**Design check:** if you can delete Complication 1 or Complication 2 without changing what the player
does at Resolution, that complication isn't load-bearing — it's an And Then. Every But needs to
change the shape of what comes after it, not just delay it.

### 5b. The Branching Consequence Tree (companion quests, major faction quests)

Inner Tepenia already has binding design laws for this tier of content — see
`feedback_dual_outcome_companion_perks`, `feedback_no_good_endings`, and
`feedback_companion_mediated_access` memories. The But/Therefore method is the mechanism that
*produces* those outcomes rather than bolting them on at the end:

```
SETUP
   │
   ▼ BUT
FORK POINT      — a genuine reversal that splits into 2+ paths, not a menu of flavor options.
                  Each path must cost something different, per "No Good Endings."
   │
   ├──▼ THEREFORE (Path A)          ├──▼ THEREFORE (Path B)
   │  ACTION A1                     │  ACTION B1
   │     │                          │     │
   │     ▼ BUT                      │     ▼ BUT
   │  COMPLICATION A2                │  COMPLICATION B2
   │  (different in kind from        │  (different in kind from
   │   B2, not just relabeled)       │   A2, not just relabeled)
   │     │                          │     │
   │     ▼ THEREFORE                │     ▼ THEREFORE
   │  PERK/ACCESS A                  │  PERK/ACCESS B
   │  (per Companion-Mediated        │  (per Companion-Mediated
   │   Access: a new place or        │   Access: a different new
   │   faction opens up)             │   place or faction opens up)
```

**Design check:** if Path A's complication and Path B's complication are the same event with the
names swapped, the fork isn't real — it's cosmetic. The whole point of forking on a "but" is that the
two branches genuinely don't converge back to the same beats.

### 5c. The Quest Beat Worksheet

A blank, fill-in-the-blank version of 5a, meant to be copy-pasted and actually typed into during
drafting — the point is to force every transition to be explicitly labeled, so a chain of accidental
And-Thens can't hide:

```
Quest: ___________________________     Subnet/DLC: ___________________________

SETUP:            ______________________________________________
   BUT             ______________________________________________
COMPLICATION 1:    ______________________________________________
   THEREFORE       ______________________________________________
ACTION 1:          ______________________________________________
   BUT             ______________________________________________
COMPLICATION 2:    ______________________________________________
   THEREFORE       ______________________________________________
ACTION 2:          ______________________________________________
   BUT             ______________________________________________
REVERSAL:          ______________________________________________
   THEREFORE       ______________________________________________
RESOLUTION:        ______________________________________________

Self-check: could any BUT line above be deleted without changing what the player
does two lines later? If yes, that BUT is an AND THEN in disguise — rewrite it.
```

---

## 6. How this interacts with Inner Tepenia's own standing design laws

This method is a generator, not a replacement for the project's existing narrative rules. When
drafting a quest chain, route the "But" reversal points through whichever of these already applies:

- **No Good Endings** — a companion-branch "But" should cost something real, not just look
  dramatic. If a reversal doesn't force a genuine trade-off, it's decoration.
- **Dual-Outcome Companion Perks** — a Fork Point (5b) is usually where a companion questline's
  2-5 mutually exclusive perks actually originate. Design the fork first; the perks should fall out
  of what each branch's "Therefore" naturally grants, not get bolted on afterward.
- **Companion-Mediated Access** — each branch's final "Therefore" is a natural place to grant the
  new place/faction access this law requires.
- **Cross-DLC Bypass Design Law** — a "But" reversal is often the natural seam where a cross-DLC
  item or gift (the DLC1-directed gift chain) can slot in as an alternate route past a complication,
  the same way Section 4's Troll example could plausibly gain a "but the player already has X from
  DLC 5" shortcut.
- **XP Lump-Sum Model** — since quest XP pays out once on completion regardless of path taken, the
  Branching Consequence Tree's two paths don't need separately tuned XP values — only the perks and
  access differ, not the payout mechanism.

---

## 7. Before calling a quest draft done

Read the chain top to bottom using only the conjunctions (skip the content). If it reads
**But-Therefore-But-Therefore** all the way down with no run of two or more Therefores (or two or more
Buts) in a row, and no beat that could be deleted without consequence, the quest has the shape the
method is looking for. If it reads like a list with "but"/"therefore" stapled on, go back to Section 3.
