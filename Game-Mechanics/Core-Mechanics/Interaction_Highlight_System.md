# Interaction Highlight System

**Established 2026-07-07**, via the Zukelli structural-language mechanic (see `Specs/Zukelli.md` Gameplay Notes and `Game-Mechanics/Perks/Special_Unique_Perks.md`'s "Zukelli Native" perk).

## Baseline: hold-to-highlight

Modeled directly on Baldur's Gate 3's own hold-key highlight convention. Holding a dedicated key (working bind: **Alt**) highlights every interactable object and NPC currently visible on screen — items that can be picked up, containers, levers, dialogue-triggering NPCs, and so on. This is the standard, always-available baseline across the entire game, not something tied to any stat or perk.

## Stat-conditional extension: environmental "super-perception"

Some locations layer an additional, stat-gated tier onto this same key. At Zukelli's ruins specifically, a player who meets the threshold established for the structural-language decoding mechanic — **10 Calculation, 10 Investigation, 6+ Engine, 6+ Nerve** — sees an expanded highlight set when holding Alt: walls, stairs, door-frames, lantern posts, and other architectural elements that carry the city's own surviving color/pattern conduit-marking system light up alongside the normal baseline highlights. This is how the player is actually signaled that the structural-language decode option exists at all, without a quest marker, a tooltip, or dialogue spelling it out directly.

**Design rule:** a player who does *not* meet the stat threshold sees only the normal baseline highlight set when holding Alt at Zukelli — no walls, no stairs, no door-frames. The environment doesn't announce that something extra is there; it simply looks, to that player, like an ordinary use of the ordinary key. The discovery is entirely conditional on the player's own build already qualifying, which keeps the mechanic honestly hidden rather than dangled as an obvious locked door.

**Why this matters as a template:** this solves a real, recurring design problem — how does a player know a stat-gated environmental interaction exists at all, when (per `Game-Mechanics/Perks/Perk_Framework.md` Category F's own design rules) hidden world content is deliberately meant to have no quest marker or tooltip? Reusing the existing hold-to-highlight key, extended conditionally by stat threshold, gives a genuine, discoverable-but-not-spoiled signal. This is worth reusing anywhere else in the project that has a similar "some players can interact with this, most can't, and it shouldn't be obvious which is true until you actually try" design need — not unique to Zukelli, though Zukelli is its first confirmed application.

## Open questions

- Whether other stat-gated environmental mechanics elsewhere in the project (existing or future) should adopt this same extended-highlight signal, on a case-by-case basis
- Exact visual treatment for the expanded highlight set (color, intensity, outline style) — distinct enough from the baseline highlight that a qualifying player notices something is different, without needing to be told
- Whether the key bind itself (Alt) is final, or a placeholder pending full control-scheme design

## Camera-paradigm note, flagged 2026-07-07

Inner Tepenia uses a free-rotating 3D isometric camera deliberately modeled on Baldur's Gate 3's own (see `Movement_Camera_and_Grid_System.md`) — confirmed, not a flat/fixed 2D top-down view. This means the BG3 comparison this file is built on is a genuine like-for-like reference, not a mismatched borrow from an unrelated camera paradigm.

The broader caution still stands for *other* design references, though: this is also a turn-based tactical RPG, and plenty of relevant genre precedent (quest markers, discoverability conventions, HUD design) comes from games with a fundamentally different camera — first-person or over-the-shoulder third-person (Skyrim, Elden Ring), where the player sees a narrow slice of the world at a time. An isometric camera reveals far more of the surrounding map and environment simultaneously, which changes how much a marker or highlight actually needs to do, and how easily a player can be expected to notice something through pure observation versus a first/third-person camera's much tighter field of view. Any future design work borrowing conventions from non-isometric games (quest-marker philosophy very much included — see the broader discussion this file grew out of) should check the source game's actual camera paradigm before assuming the convention transfers cleanly, rather than assuming "it's a well-known RPG mechanic" is sufficient justification on its own.
