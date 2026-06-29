# Companion System

## Party Composition

The player's active party consists of:

- **The protagonist** (player character)
- **Calethina** — always present as a holographic projection from the wrist device; not a companion in the mechanical or code sense (no companion slot, no companion system triggers). Her projection quality varies by signal state before the midpoint download; stable and clean everywhere after. She is a constant presence regardless of which companion the player has recruited.
- **One recruited companion** — the single companion slot

**Maximum active party size: 3** (protagonist + Calethina + 1 companion)

This is a hard limit. The player can recruit only one companion at a time. Recruiting a new companion requires dismissing the current one.

---

## Design Rationale

Calethina's constant presence as a projection already gives the player a second meaningful relationship at all times. Adding a full companion on top of that creates a three-entity dynamic (protagonist + Calethina + companion) that preserves the Fallout-adjacent feel of a protagonist with support rather than a party. Allowing two companion slots would produce four de-facto party members — a meaningfully different emotional and tactical register, closer to a party-based RPG than the intended design.

The single companion slot means each companion choice is a genuine commitment. The player leaves 9–11 companions behind per playthrough (based on a main game pool of 10–12 recruitable companions), which drives meaningful replayability without trivializing the decision.

**Fallout precedent:** Fallout: New Vegas allows 1 humanoid + 1 non-humanoid companion simultaneously. Inner Tepenia's model — 1 companion slot + Calethina as a persistent non-slot presence — achieves the same effective dynamic while keeping Calethina architecturally distinct from the companion system.

---

## Total Recruitable Pool

**Main game target: TBD — higher than originally estimated.** The pool should be large enough that multiple playthroughs feel genuinely different. Specific count to be established as character design work progresses.

Currently confirmed recruitable companions (5):
1. Favi della Torre
2. Villena Hiresvett
3. Naizelle d'Edjordoś
4. Seica Cenilaithe
5. Ji-Eun Kim

Additional recruitable companions to be designed. Some TBN characters may be recruitable; classification TBD per character.

**DLC companions** (separate from main game pool, available only in their respective DLC):
- Kendra Heinrich (DLC 1: South Pole)
- Salagéa Aparast (DLC 5: Atlantic Coastal Region)

---

## Major NPCs Who Are Not Recruitable Companions

Some characters have complete questlines and deep player relationships but do not join the party. They are major NPCs, not companions.

### Trisha Miller — Radio Host

Trisha runs her radio show and does not leave that role. She cannot be recruited as a companion.

**Post-questline mechanic:** Trisha's relationship with the player — built through her questline, through the player's choices, through help given or betrayal committed — is expressed through her radio show. After the questline resolves, she talks about the player on air. What she says reflects how the events played out. Players who helped her get one version; players who betrayed her get another; players who made complicated choices in between get something that reflects that complexity.

This makes her radio show a form of world-state feedback: Concordia hears what Trisha says about the player, and NPCs may reference having heard the broadcast. She is one of the primary ways the game communicates reputation back to the player through the world's voice rather than through a UI element.

### Majyao Bisyugota — Teahouse Keeper

Majyao runs her teahouse and does not leave it. She cannot be recruited as a companion. Her questline is large and consequential; its resolution plays out through the teahouse and through Concordia's political landscape, not through party membership.

---

## Companion Slot Rules

- Only one companion may be active at a time
- Dismissing a companion returns them to a fixed location in Concordia (they do not disappear from the world)
- Dismissed companions retain all relationship progress and questline state
- A companion's personal questline can only advance while they are the active companion
- Re-recruiting a dismissed companion is always available unless a specific story event has permanently changed their status

### Companions and DLCs

**Companions cannot be brought into a DLC on its first playthrough.** This is a universal rule across all DLCs. Every DLC must be completable solo. Any companion effect, access route, or solution that references a companion's abilities must be achievable through non-companion means on first play.

**After completing a DLC for the first time, companions may accompany the player on all subsequent runs of that specific DLC.** Completion of DLC 1 unlocks companion access for DLC 1 replays only — it does not grant companion access to any other DLC. Each DLC's companion access is unlocked independently by completing that DLC.

This applies to companion presence only. Items or technology *obtained from* a companion before DLC entry (e.g., a portable device given by Ji-Eun Kim) are unaffected — the player carries those in on any run, companion or not.

---

## Romance System

### Scope

**All recruitable companions are romanceable. No exceptions.** This is a binding design rule. Any character who can be recruited as a player companion — main game or DLC — is romanceable, subject to their individual gate conditions.

Non-recruitable named NPCs: romance status is decided on a per-character basis during design and development. Some may be romanceable; some will not be. This is deferred and will not be established as a blanket rule in either direction.

**Pool (confirmed):** All recruitable companions (main game + DLC) + non-recruitable named NPCs TBD per character.

### The Double Gate

Romance requires two independent conditions to be met simultaneously. Failing either one closes the route.

**Gate 1 — Questline prerequisite:** The player must have completed the relevant relationship-building questline content with this character. The relationship has to have been built through shared experience and choices, not just dialogue options. This gate is the same for all characters.

**Gate 2 — MACHINE stat / trait threshold:** Each character has a specific profile of what they find attractive, derived from their personality, sensibilities, and history. The player's MACHINE stats and traits must meet that profile. This gate is unique per character.

**Perks are explicitly excluded from Gate 2.** MACHINE stats and traits are chosen at character creation — they define who the player character fundamentally *is*. Perks are acquired through play — they represent what the character has learned and done. The romance gate is about fundamental identity, not accumulated experience. A player cannot perk their way into a romance they weren't built for.

### Threshold Design Per Character

When designing each romanceable character, specify:
- Which MACHINE stat(s) are required and at what level
- Which traits (if any) are required or are dealbreakers
- The in-world rationale (what this person finds attractive and why, based on their personality)

Examples of how thresholds might read:
- A character who values physical presence → Might threshold
- A character who values intelligence and wit → Calculation threshold
- A character who values genuine emotional depth → Humanity threshold
- A character who admires courage and directness → Nerve threshold
- A character who values perceptiveness → Investigation threshold
- A character who values capability and endurance → Engine threshold

Multiple stats may be required. Traits may open or close routes regardless of stat levels.

### The Signal

When a player has completed the questline prerequisite but does not meet the stat/trait threshold, the character makes an honest, casual, in-voice remark that reveals what they're looking for — without breaking the fiction or explaining the system. The line is short and in character. It closes the romantic door without closing the relationship.

Examples of the register (not final lines — those are written per character in voice):
- *"Sorry, friend. I like them smart."*
- *"Not trying to be rude here, but come back once you've lifted some weights."*
- *"You're good people. Just not my type."*

The player who hears this line has a clear signal. On a replay with a different build, they know what to work toward. The line is delivered once and not repeated unless the player re-initiates.

### Romance Exclusivity — Monogamy Rule

The general design principle is **monogamy once a committed romance is established.**

**Before full romance:** The player can engage in casual sexual encounters freely. A separate pool of characters exists — sexually available with only minimal stat-gating and/or quest-gating, no full romance arc required — and these encounters carry no relationship consequences prior to the player committing to a full romance.

**Once the player has fully romanced one character** (completed the arc, received the romance perk), the rules change:

- Any subsequent sexual encounter — whether with a previously-available casual partner or by triggering a second full romance — starts a timer
- Approximately three in-game days later *(placeholder — exact duration TBD)*, the romanced companion discovers the situation
- They react with fury and the romance perk is immediately lost

**The consequence is total.** There is no partial loss. The player has to choose, and the penalty for failing to honor that choice is losing the perk entirely.

**Second full romance — symmetric loss:** If the player has triggered a second full romance (not just a casual encounter), both characters find out and both romance perks are lost simultaneously. The player cannot navigate between two committed relationships.

**Home access after perk loss:** TBD — to be resolved during Romance Reward system finalization. The question is whether home access is treated as part of the romance perk (and thus lost) or as a separate reward that persists.

**The "fuckable" character pool:** A designed set of characters who are sexually available to the player at any time with only minimal gating. These are not romanceable in the full arc sense — no romance perk, no unlocked home, no relationship arc. They exist to give the player options for casual encounters pre-commitment. Once the player has committed to a full romance, sleeping with any of them triggers the monogamy rule above.

---

### Thematic Note

The romance system is a direct expression of the second guiding principle — the nature of love between robots and humans. Every romance in the game, regardless of the species of the characters involved, is asking: what does this specific person find in this specific other person, and what does that mean for both of them? The stat/trait gate ensures that the answer is always grounded in who the player character actually is, not in what they've done or what perks they've accumulated.

---

### Confirmed Romanceable Characters

The following characters are confirmed romanceable. Thresholds are documented here as they are designed; entries marked TBD are pending Phase 3 personality work.

| Character | Type | Stat Thresholds | Trait Gates | Notes |
|-----------|------|-----------------|-------------|-------|
| Calethina | Projection system (not a companion) | Calc ≥ 8, Humanity ≥ 6, Nerve ≥ 6, Engine ≥ 6 | TBD | See full design note below; romance post-download via mini-quest |
| Favi della Torre | Recruitable companion | TBD | TBD | Thresholds pending Phase 3 personality design |
| Villena Hiresvett | Recruitable companion | TBD | TBD | Thresholds pending Phase 3 personality design |
| Naizelle d'Edjordoś | Recruitable companion | TBD | TBD | Thresholds pending Phase 3 personality design |
| Seica Cenilaithe | Recruitable companion | TBD | TBD | Thresholds pending Phase 3 personality design |
| Ji-Eun Kim | Recruitable companion | TBD | TBD | Thresholds pending Phase 3 personality design |
| Vosora Lashár Tanslock | Recruitable companion | TBD | TBD | Thresholds pending Phase 3 personality design |
| Kendra Heinrich | DLC 1 companion | **None** | **None** | Unique gate system — see full design note below |
| Salagéa Aparast | DLC 5 companion | TBD | TBD | Thresholds pending Phase 7 personality design |
| + all future companions | TBD | TBD | TBD | Rule: all recruitable companions are romanceable by default |

Non-recruitable named NPCs: romance status decided per character during design. Not established here.

---

### Calethina — Romance Design (Special Case)

Calethina is romanceable. She is the most demanding romance in the game, both narratively and mechanically.

**Stat threshold:**
- Calculation ≥ 8 *(she needs someone who can actually interface with her at her level)*
- Humanity ≥ 6 *(she is drawn to consciousness that leans toward warmth and connection)*
- Nerve ≥ 6 *(she needs to know the protagonist can hold under pressure)*
- Engine ≥ 6 *(endurance — she has outlived everyone; she needs to know you will sustain)*

No trait gates currently defined. Traits may be added during Phase 3 character design once her full personality is written.

**The download and the romance are separate events.** The Calethina questline ("Echoes of the Bridge") builds the relationship across its full length. The download decision (approximately midpoint of the main quest) is available to any player who has made the associated questline decisions — it is not stat-gated. The download is about saving/keeping her. The romance is a separate question about what the relationship becomes afterward.

**The download: what it is.** On the full personality download, she is not simply transferred to the protagonist's wrist device — she becomes part of the protagonist, carried within them. Her holographic projection then projects from the protagonist's own body. This is a profound chosen bond regardless of whether the romance follows.

**Full download only.** The romance option does not follow a partial download, a no-download outcome, or an alternative stabilization solution. Those each produce their own emotionally valid outcomes, but the romance mini-quest does not open.

**The romance option appears after the download.** Once the full download has occurred, the game checks the stat threshold. If met, a romance option opens. If not met, it does not. The protagonist and Calethina now share an intimate physical reality regardless — she is inside them — but the romantic arc is a separate layer that requires the build to support it.

**The romance mini-quest.** If the romance option appears, it is its own dedicated interaction sequence distinct from the main questline — a focused arc that constitutes the actual romantic relationship developing between the protagonist and Calethina in the post-download state. Specific beats are Phase 5 design work.

**Built-in bittersweet weight.** Even on the romantic path, the full download carries a confirmed risk: some of her memories may be lost or altered in transfer. The romance begins with the protagonist having already accepted losing pieces of her in order to keep her at all.

**The re-spec complication.** If the player re-specced through Calethina's lab to meet her stat thresholds, she performed the work herself. She knows what was changed and why. The point at which the romance option appears (post-download) should have dialogue that acknowledges this — as a branch, not a single read. Whether she finds it moving (someone wanted to be someone she could love) or troubling (someone altered who they were to reach her) are both valid. Both are bittersweet.

**The Calethina Devotion failsafe ending** has two versions: one for players who completed the romance mini-quest, one for players who downloaded without the romance threshold met. The second version reflects a different kind of profound chosen bond — she is inside them, they carry her, and that is its own thing.

---

### Kendra Heinrich — Romance Design (Unique Gate System)

Kendra is the only recruitable companion in the entire game whose romance has **no MACHINE stat gate and no trait gate.** This is a deliberate exception, and the reason is specific to her character.

Stat gates work by asking: *are you the kind of person this character would find attractive?* That is the right question for most characters — attraction has a profile, and that profile maps to who the protagonist fundamentally is.

Kendra is a Type 8w7. A Type 8 does not open up because of who you are in the abstract. They open up because of what happened between you and them — a specific act, a specific moment of genuine seeing. Her romance gate is therefore not about character profile. It is about what the player did and how they showed up for her during her DLC.

**Gate 1 — You defeated what defeated her.**
The player must successfully complete the DLC's central combat challenge — the enemy or threat formidable enough to strand a war goddess. Kendra was there. She witnessed the player do something she couldn't do in her current state. For an 8, respect is the precondition for everything else. You cannot reach her interior without first earning that.

**Gate 2 — You broke through her emotional exterior.**
Kendra's armor exists specifically to prevent people from seeing inside. The DLC places her in the position she has never been in — damaged, stranded, needing help, unable to protect herself. How the player handles that throughout the DLC determines whether Gate 2 is met. This is tracked through DLC dialogue choices and how the player treats her vulnerability.

The things that break through for an 8w7 specifically:
- Not being condescending about rescuing her — not making her feel like a burden or a charity case
- Not expecting gratitude in a way that creates a debt dynamic
- Not being intimidated by her directness, even when she is being difficult about her situation
- Not treating her as less because she is damaged — respecting her as she is, not as she was
- Genuine curiosity about who she is, not just what she is capable of
- Possibly: pushing back on her when she is wrong — an 8 respects people who don't fold

**The romance mini-quest.** When both gates are cleared, a romance mini-quest opens — its own dedicated interaction sequence. Given that Kendra is a DLC companion who can continue as a main game companion after the DLC, the mini-quest may unfold partly in the South Pole setting and partly in Concordia. Specific beats are Phase 7 design work.

**Why no stat gate.** Any build can romance Kendra. A high-Might character and a high-Humanity character have equal access. What matters is not who the protagonist is at character creation — it is what they did in the South Pole and how they treated a war goddess who needed help for the first time in her life.

---

## Romance Reward — Companion Player Homes

**Romancing a companion unlocks that companion's personal home as a player home.** This is universal for all romanceable companions. The home becomes available to the player-character once the romance has been established, and remains available regardless of whether the companion is the currently active companion.

All companion-unlocked homes exist **in addition to** the regular player homes available in the main game. They do not replace or supersede the standard home options. See `Worldspace/Locations-and-Levels/Player_Homes.md` for the full list of standard player homes.

**Calethina is the sole exception.** She is a holographic projection with no physical dwelling — there is no home to unlock. This is the only case where a romanced character does not produce a player home.

The location of each companion's home is tied to their character and district. Companion homes are distributed across Concordia and, in the case of DLC companions, may exist outside the main city as a secondary location. Kendra Heinrich's home is in Capricorn — her origin district and the base of The Reclaimed Record movement she helped seed. After completing her DLC and returning to Concordia, she establishes (or returns to) a residence there. Romancing her gives the player access to that home; if the romance has been perma-locked through dialogue, she maintains the Capricorn home independently and the player does not gain access through the romance route.

Individual companion home designs (layout, contents, lore items, décor reflecting the companion's personality) are Phase 3 and Phase 7 design work per character.

---

## Calethina: Not a Companion

Calethina does not occupy the companion slot and is not subject to companion system rules. She cannot be dismissed. She cannot be recruited in the conventional sense. She is present or absent based on signal state (before download) or always present (after download).

For implementation: she is a projection system, not a companion object. Any code that iterates over companions does not include Calethina.
