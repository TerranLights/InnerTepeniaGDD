# Universal Rules

Game-wide rules that apply across all systems, content, and design decisions regardless of context. These are binding. When a specific system document conflicts with a rule listed here, this document takes precedence unless a specific named exception is documented below.

Cross-reference: some of these rules are also documented within their originating system docs. This file exists as the single consolidated reference.

---

## Inventory

**Quest items are weightless.**
All items classified as quest items carry zero inventory weight, regardless of their physical nature or size. This is unconditional — there are no heavy quest items. Applies to main-quest critical items, companion-given objects, post-romance mini-questline rewards, and any other item that receives quest item classification.

**Quest items cannot be sold, dropped, lost, pickpocketed, or broken down.**
Quest item classification confers full protection. The player cannot remove a quest item from their inventory by any means, intentional or accidental. This protection is permanent for the duration of the playthrough.

**Quest items are examinable in the inventory UI.**
Every quest item has a written description accessible from the inventory screen. The description conveys what the item is, its significance, and where relevant, what it means that the player has it.

---

## Companion System

**All recruitable companions are romanceable. No exceptions.**
Any character who can be recruited as a player companion — main game or DLC — is romanceable, subject to their individual gate conditions. This rule admits no exceptions. If a character is recruitable, they are romanceable.

**Maximum active party size: 3.**
The player, Calethina (always present as a holographic projection, not occupying a companion slot), and one recruited companion. This is a hard limit. Two companion slots are not available under any circumstance.

**Companions cannot be brought into a DLC on its first playthrough.**
Every DLC must be completable solo. Companion access for a given DLC is unlocked only after that DLC has been completed at least once, and applies only to that DLC on subsequent runs.

**Romance gates use the visible MACHINE stat check UI.**
Romance gates are displayed using the same visible stat-check format as all other MACHINE stat checks. Both the passing and failing dialogue options are shown simultaneously. Failed thresholds display as [current/required]. See `Core-Mechanics/Companion_System.md` for full documentation and format examples.

**Perks are excluded from romance gates.**
Romance gates check MACHINE stats and traits only — never perks. Stats and traits define who the player character fundamentally is. Perks represent what they have learned and done. A player cannot perk their way into a romance they were not built for.

**Romance gates check permanent base stats only — not temporary boosts.**
Temporary stat increases from food, chems, equipment, or any other time-limited effect do not count toward romance gate thresholds. The gate is checking who the player character fundamentally is, not their momentary enhanced state. Permanent stat raises — whether set at character creation or raised through gameplay means such as the Intense Training perk — count in full. Temporary boosts do not count at all, and there is no "angry later" consequence for attempting to use them; they are simply not read by the gate check.

**A companion's player home is accessible only while the romance is active.**
Home access is granted when the romance is established and revoked if the romance ends (via the monogamy rule). The home belongs to the companion; the player's access is contingent on the relationship.

---

## Skill & Stat Checks

**Added 2026-08-09.** Generalizes the existing "Romance gates check permanent base stats only" rule (above)
into the two standing laws governing every other skill/stat check in the game.

**Terminology, confirmed 2026-08-16 (full law in `Character-Creation/Skills.md`'s "Flat Thresholds, No Dice
Rolls"):** these are **checks**, never "rolls" — not even casually. No randomness exists behind a skill/stat
check anywhere in this system; the word "roll" implies exactly the mechanic this project doesn't have. The sole
named exception is ranged combat hit chance and aimed-shot body-part probability, where actual randomness
applies and "roll" is accurate.

**Every stat/skill check in the game evaluates the player's current, effective stat total, including temporary
buffs — with exactly one standing exception: Romance questline trigger checks (Gate 2, above), which check only
the permanent, unadjusted MACHINE stat.**
Food, chems, equipment, and any other stacking bonus all count toward every ordinary dialogue/quest/world-
interaction check in the game, exactly as in Fallout: New Vegas — a player with a natural 5 Strength who eats
Bighorner or Brahmin Steak for a temporary +2 Strength buff passes a check requiring 7 Strength exactly as if
the 7 were natural (see, for example, the Tyrone/Melissa/Great Khans interaction in the Chomps Lewis supply
questline — the +2 Strength buff lets the player deliver the "I'm sorry, I can't hear you over the sound of all
these muscles" line at 5 base Strength). Romance gates are the sole named exception to this rule, not the
default — every other system that reads a MACHINE stat should assume buffs count unless a future rule names
another explicit exception the same way this one is named.

**The Perfect-10 Mastery Dividend: a Natural 10 in a stat/skill check should let the player talk their way past
a real number of subsequent checks within that same questline — never a permanent, game-wide effect.**
A **Natural 10** is a *permanent* stat value of 10, reached only through starting character-creation
allocation, spending Intense Training points, or installing a non-Dr.-Usanagi implant (see
`Character-Creation/Permanent_MACHINE_Stat_Increases.md`) — the three established permanent-stat-increase
paths. An **Adjusted 10** is a stat that merely reads 10 right now because of a temporary buff stacked on a
lower permanent value, per the buffable-check rule above. The Mastery Dividend is earned only by a Natural 10;
an Adjusted 10 clears the single check it's attached to, exactly as the buffable-check rule requires, but
represents no genuine, rare life-area mastery and does not unlock the Dividend.

**Implementation: a Natural 10 option is offered as its own separate dialogue choice**, distinct from an
ordinary buffable stat check on the same stat, so the two are never conflated in the UI or in the underlying
check logic:
```
{{NPC dialogue}}

[10 STAT] {{dialogue}}
[Nat 10 STAT] {{dialogue}}   // grants the Mastery Dividend for the rest of this questline
[55 SKILL-A] {{dialogue}}
[80 SKILL-B] {{dialogue}}
[45 SKILL-C] {{dialogue}}
```
The plain `[10 STAT]` option stays ordinarily buffable and only resolves the single check it's attached to; the
separate `[Nat 10 STAT]` option is what gates the Dividend, and only a permanent Natural 10 can select it.

---

## World Canon

**No Indians or South Asians ever came to Tepenia.**
No characters from India, Pakistan, Bangladesh, Sri Lanka, or any other South Asian nation are part of Tepenian history or population. Station locations with South Asian names (Maitri, Bharati) have non-Indian founding populations. The Maitri site's resolution is finalized: it coalesced with the adjacent Russian-run Novolazarevskaya settlement into a single city, now named **Lazar** (see `Cities/Specs/Lazar.md`). The Bharati site's resolution is also finalized (2026-07-03): its founding population is Japanese, allocated via a pre-exile diplomatic decision of the International Court of Diplomacy at Jeju-do (an Upper Earth institution, not a Tepenian one) — named **Shirayuki** (白雪, "white snow"), 2026-07-08 (see `Cities/Specs/Shirayuki.md`). This is hard canon, not a gap.

**All robot characters are bisexual. Human female characters are bisexual; human male characters are heterosexual.** *(Updated 2026-07-03 — previously "all human characters are heterosexual"; refined so human women follow the same bisexual default as robots, while human men remain the sole heterosexual-only category.)*
Applies universally to companions, romanceable NPCs, and the sexually-available character pool. No exceptions are established. **Mechanical consequence:** romanceable human male companions gate on an additional gender check (the player must be presenting as the gender he's attracted to) on top of the standard MACHINE stat check — see `Companion_System.md`. Robot companions and human female companions gate on the MACHINE check alone, same as before.

---

## Design Law

**Fallout Precedence Law: New Vegas always wins.**
When Fallout 1/2 and Fallout: New Vegas establish conflicting design precedents, New Vegas takes precedence unconditionally. No exceptions. See `memory/feedback_fallout_precedence_law.md` for full documentation.

**No Level-Scaling. None. No exceptions.** *(Established 2026-08-02, developer's own words: "Immutable Law.")*
Enemies, loot, and encounters never scale to match the player's level. The world has a fixed, designed difficulty the player grows into (or doesn't) — direct consequence of Fallout Precedence Law above, since this is exactly how Fallout: New Vegas itself works (Deathclaws outside Goodsprings at level 1 are a real, permanent danger, not a scaled-down "early game" version of a Deathclaw). **This is not scoped to Inner Tepenia alone** — the developer has confirmed this is a binding law across every game this studio makes, present and future (Outer Tepenia 1/2/3 and any other title), not a per-project preference open to reconsideration. Also recorded in the developer's own global Claude Code instructions (`~/.claude/CLAUDE.md`) for that reason — this file's copy is the Inner-Tepenia-specific documentation of a rule whose actual authority is cross-project.
