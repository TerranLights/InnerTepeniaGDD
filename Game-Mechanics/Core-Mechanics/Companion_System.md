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

**Main game target: TBD — higher than originally estimated.** The pool should be large enough that multiple playthroughs feel genuinely different. Specific count to be established as character design work progresses. **Partially resolved 2026-07-20:** the DLC side of this total now has a real allocation framework (see "Multiple Native Companions Per DLC" below) rather than being an open guess — once each DLC's companion count within its assigned range is finalized, the true grand total (main game + all 7 DLCs) will be derivable rather than estimated.

**Roster source of truth — updated 2026-07-20, twice: once for the developer's precise recruitability pass, once more after a major folder-structure reorganization and roster expansion the same day.** `Worldspace/Characters/Dolls/Still-Present_-_In-Game/` is now physically split into three subfolders matching the categories below (plus `z-template`, a blank template, not a character, left outside all three):

- **`non-recruitable/` — confirmed non-recruitable, permanently (2 characters):** **Trisha Miller** (her whole post-questline payoff — world-state feedback delivered through her radio show — depends specifically on her never leaving that role) and **Majyao Bisyugota** (already has a fully-designed romanceable-without-recruitable arc — repeated teahouse visits, stat gates, the Blood River Tea thread — that depends on her staying at the teahouse).
- **`unsure and_or special cases/` — 20 characters:**
  - **Calethina** — structurally distinct special case, not a normal recruitability question at all: holographic projection, no party slot, no physical dwelling, exempt from Companion Slot Rules, already fully romanceable through her own unique download/projection system; "almost automatically" a companion in an unorthodox way the normal recruitment flow doesn't apply to.
  - **19 genuinely undecided characters** — may end up recruitable or may follow the Majyao pattern instead (full companion + romance questline, never joins the active party). Three have specific reasoning already on record: **FR-03 "Maria"** (developer's instinct: may operate a leisure/billiards establishment), **SE-031 "Akina"** (the gynoid at the center of the Long Night War's actual inciting incident — see `TODO.md` and `[[project_long_night_war_inciting_incident]]` — flagged as extremely delicate, requiring the utmost care), **TCY-20 "Miranda"** (developer's instinct: may operate an actual in-game bar as its bartender). The other 16, added 2026-07-20 during the roster expansion, have no content written yet and no specific reasoning on record for their undecided status — they are placeholder folders only (Ísabel Camila Bóndar, Itzel Hernandez, Leticia Flores, Meifa Podeshén, Nóra Kerekes, Rosalva Mejía, and TBN [FFD-22 Tiancheng], [FFD-51 Duqing], [FFD-53 Leeson], [FFD-54 Yelan], [SE-150 Winola], [SE-154 Annika], [XT-41 Genri], [ZL-11 Olivia], [ZL-18 Miko], [ZL-41 Irene]).
  
  Any of these 19, if resolved non-recruitable, would get the same treatment as Majyao: a full companion questline and a full romance arc, just anchored to a fixed location rather than joining the party. **Do not design MACHINE-stat-gated romance thresholds or companion perks for anyone in this folder assuming party membership until each is individually resolved.**
- **`recruitable/` — everyone else, 44 characters as of 2026-07-20, confirmed, not just plausible.** This includes every still-TBN-named placeholder character. Resolves the ambiguity on "Charlene" (XT-17, DLC 7) and **XT-21 "Angelina"**, both previously listed as "Undecided" in their own files — both confirmed recruitable; individual files just haven't all caught up yet (see "Practical consequence" below). **20 of the 44 were added 2026-07-20 in the same roster expansion** — the developer's own words: "I don't know what sorts of character backstories, situations, etc, they have, but I'm certain that I want them in the game." These are placeholder folders only, no content written yet: Felia Percelle (FW-70), Heather Wendell, Imelda Sánchez, Inés Ochoa, Laura Wahlström, Lieselotte "Lotte" Koster, Małgorzata "Gosia" Iskierka, Marisol Ruvalcaba, Pixi Fairiefeather, Seline Finley, Shuchar Vaszyong, and TBN [SE-157 Lita], [SE-164 Kemeny], [SHD-02 Starley], [STP-06 Hao], [STP-09 Keqing Qin], [STP-10 Mira], [TCY-02 Polly], [WM-06 darling freckled redhead], [XT-30 Luna].

**Current totals as of 2026-07-20:** **44 confirmed recruitable companions** (up from 25) + 2 permanently non-recruitable + 1 special case (Calethina) + 19 genuinely undecided = 66 real character folders, before any new DLC-tier companions from the "Multiple Native Companions Per DLC" policy are added on top. This list will keep growing — the rule is about the folder as a whole, not a fixed enumeration.

**Practical consequence:** each individual character's own `Companion Potential` / `Romance Potential` fields should read "Yes" once this policy is propagated to their files — several TBN characters still show "TBD" in their own README and have not yet been individually updated to match this roster-wide confirmation (Meyzan Yocazhda done 2026-07-20, see her own file). Treat this section as authoritative over any individual file that hasn't caught up yet.

**Companion distribution across districts — organizing principle confirmed 2026-07-20:** with only 13 districts (12 Zodiac-coded + the neutral Hub) but a companion pool confirmed to run well past 27, multiple recruitable companions per district is the expected norm, not a redundancy to avoid outright. Districts and factions are related but genuinely separate axes — a district can host multiple factions or sub-factions with real internal disagreement, a faction can span multiple districts, and companion placement should track that faction/sub-faction structure rather than being spread evenly by district headcount. In practice this means: when placing a new companion, the first question is which faction, sub-faction, or internal-conflict thread she belongs to (as with Meyzan and Capricorn's merit-rating scandal above — see her own file for why that connection is written around the underlying plot-thread rather than its current, still-unsettled name), not simply "which district doesn't have one yet." Genuine redundancy to actually avoid is same-district companions occupying the *same narrative niche* (see Meyzan vs. Villena reasoning above, both in different districts but the concern generalizes) — not simply sharing a district.

**Currently confirmed recruitable companions (13)** *(corrected 2026-07-10 — this list previously listed only the first 5, stale relative to the full romance-design table further down this document; TCY-25 "Rui" added 2026-07-10)*:
1. IT-068 "Flora"
2. Favi della Torre
3. Villena Hiresvett
4. Naizelle d'Edjordoś
5. Seica Cenilaithe
6. Ji-Eun Kim
7. Vosora Lashár Tanslock
8. Michelle Stanton
9. IT-021 "Fenny"
10. FW-25 "Pink Lucy"
11. Ayako Hayashi
12. Lyuba Baranova
13. TCY-25 "Rui"

Additional recruitable companions to be designed.

**Non-recruitable but romanceable NPCs, confirmed:** Majyao Bisyugota (teahouse keeper; full questline and romance arc, never joins the party); **Trisha Miller** (radio host; confirmed romanceable 2026-07-28 — see her own Romance Design below). **Genuinely undecided, may join this category (see "Roster source of truth" above):** FR-03 "Maria" (possible leisure-establishment operator), SE-031 "Akina" (recruitability unresolved pending her own, especially delicate character development), TCY-20 "Miranda" (possible in-game bartender).

**DLC companions** (separate from main game pool, available only in their respective DLC — **each DLC 2-7 now carries multiple native companions, allocated by narrative tier, see "Multiple Native Companions Per DLC" below**):
- Kendra Heinrich (DLC 1: South Pole) — sole companion, permanent exception, no others will be added
- Salagéa Aparast (DLC 5: Atlantic Coastal Region) — confirmed; 1-3 companion tier; additional DLC 5 companions TBD
- Maggie Aarden (DLC 2: Byrd) — confirmed 2026-07-10, see `Storyline/DLC_Overview.md`; 3-5 companion tier; additional DLC 2 companions TBD
- "Charlene" (XT-17) (DLC 7: Mirny) — presumptive only, romance status "Undecided" in her own file; 1-3 companion tier; additional DLC 7 companions TBD
- DLC 3 (Palmer), DLC 6 (Janbogo) — 1-3 companion tier; no companion identity chosen yet, including the first
- DLC 4 (Mawson) — 6-10 companion tier, the highest allocation in the game; no companion identity chosen yet; see the reserved stubs in `Locations-and-Levels/Romance_Unlocked_Homes.md`

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

## Combat Interaction — Applying Healing Items to a Companion

**Confirmed 2026-07-28, ported directly from FNV.** In Fallout: New Vegas, the player can apply their own
Stimpaks to an active companion: opening the companion's interact wheel surfaces a healing-item option that
displays that companion's current HP, and selecting it consumes one of the player's own healing items to heal
them. Inner Tepenia adopts this mechanic as-is — the player's interact wheel for the active companion
includes a healing-item option, showing the companion's current HP, and using it consumes one of the player's
own healing items (whatever Inner Tepenia's own Stimpak-equivalent item turns out to be named) to heal that
companion directly. This is a manual, player-initiated action distinct from any passive regeneration effect
(see, for example, the Cancer "not-Doctor-Usanagi" implant in `Character-Creation/Permanent_MACHINE_Stat_Increases.md`,
which grants a passive HP-regen aura to the active companion independent of and stacking with this item-based
option).

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

### DLC-Native Companions Are Always Optional to Recruit — Binding Rule, Established 2026-07-10

The rule above governs bringing an *outside* companion into a DLC. This is a separate, complementary rule governing a DLC's own *native* companion(s) — recruitable characters who live in, or are otherwise tied to, that specific DLC's own region.

**Every DLC must be fully completable, start to finish, with any, all, or none of its native companions recruited, in any combination.** At whatever point in the DLC a given companion first becomes recruitable, the player must always have an explicit option to decline — "I don't really feel like traveling with anybody" (or an equivalent line, if declining one companion in favor of another already recruited) — and continue the entire DLC, main questline and side content alike, without her. No DLC's own critical path may require any specific native companion's presence, abilities, or dialogue to progress.

**Declining recruitment is never a permanent lockout.** Provided the player has not caused that companion (or her closely-associated NPCs/factions) to turn hostile during the DLC, she remains recruitable after the DLC's own completion — exactly as if the player had simply chosen to recruit her later rather than not at all. This mirrors the existing Companion Slot Rules' own hostility exception (see above: "re-recruiting a dismissed companion is always available unless a specific story event has permanently changed their status") — the same standard applies here to a companion never recruited in the first place.

**This applies uniformly across all 7 DLCs, including DLC 1 ("Echoes of Amundsen").** Kendra Heinrich's own case works slightly differently in form but identically in principle: since she is the person the player is finding/rescuing rather than someone who joins mid-mission, the decline option applies at whatever point the game would otherwise offer her as a companion (per her own Romance Design's Gate 1/Gate 2 structure, above) — a player can complete DLC 1 in full without ever bringing Kendra into the active party, and she remains recruitable afterward under the same hostility exception.

**Design consequence:** no DLC's own central questline, environmental puzzle, or crisis resolution may be written to assume the player has any particular native companion active. Any content that meaningfully benefits from a given companion's presence (dialogue, a skill check she can assist with, a scene that plays differently with her along) must have a non-companion equivalent path available on the same playthrough.

---

### Multiple Native Companions Per DLC, Allocated by Narrative Tier — Policy Established 2026-07-20

**DLC 1 ("Echoes of Amundsen") is the sole, permanent exception.** Kendra Heinrich remains the only character present in that DLC by design — she is the entire point of the mission, and the DLC's dangers are deliberately non-character-driven (environmental, technological, or a third category not yet determined). This isolation is a deliberate thematic choice, not an unstated default — it is what makes DLC 1 read differently from every other DLC, and should be written into Kendra's own materials as an explicit distinction, not left implicit.

**Every other DLC (2 through 7) carries more than one native recruitable companion.** This reopens the three DLCs whose single native companion was already considered settled — Maggie Aarden (DLC 2/Byrd), Salagéa Aparast (DLC 5/Halley), and "Charlene"/XT-17 (DLC 7/Mirny) each keep their existing confirmed status and gain companions alongside them, not in place of them. DLC 3 (Palmer), DLC 4 (Mawson), and DLC 6 (Janbogo) will be designed from the start with more than one.

**Allocation is by narrative tier, not raw geographic scale or city count.** A subnet's physical size (number of cities, population) is not the metric — how narratively developed and dense the subnet already is, is. This is why Byrd (physically the smallest/most isolated region in the game — essentially one station) and Mawson (only 3 cities, the least narratively developed subnet, flagged separately below) land in *different* tiers despite both being small by raw geography: Byrd already carries real narrative density (the isolation/highway-access drama, the aviation refueling puzzle, Michelle Stanton's Rastra thread, Maggie Aarden already established), while Mawson is thin on both city count and established narrative weight.

**Illustrative ranges (not locked exact counts — to be finalized during each DLC's own design pass):**
- **Mawson (DLC 4): 6-10 companions.** The thinnest tier — this subnet needs the most compensating depth. Directly connects to the standing "Mawson DLC — City Depth Gap" TODO item; see that entry for how this interacts with new invented settlements.
- **Byrd (DLC 2): 3-5 companions.** A middle tier — physically tiny but already narratively denser than Mawson, so it needs a real but smaller boost. Byrd's own depth deliberately does **not** come from invented settlements (see below) — it comes from companion variety and existing city-depth work only, since the region's isolation is the point, not a gap.
- **Palmer (DLC 3), Halley (DLC 5), Janbogo (DLC 6), Mirny (DLC 7): 1-3 companions each.** The richest tier — these subnets already carry 7-8 cities' worth of geographic and narrative variety, so they need only a light companion-count boost above their existing single confirmed companion (where one exists).

**Order-variance by entry point (the core structural idea):** within a DLC with multiple companions, which companion the player meets first is intended to depend on how the player actually begins that DLC — different arrival points, different opening hooks, or different initial quest threads should plausibly lead toward different companions first. This is a genuine structural commitment: each DLC needs distinct-enough entry vectors for this to actually vary run to run, not merely a menu of companions all reached via the same fixed critical path. Several DLCs (Byrd especially, per its own standing "three candidate central-conflict anchors, none chosen" TODO item) don't yet have settled-enough core structure to support this — the multiple-companion allocation above can proceed independently, but true order-variance is likely sequenced *after* each DLC's own central conflict is locked in.

**Not yet decided:** exact companion counts within each range, the actual character concepts for any new slot, and the specific entry-point/order-variance structure per DLC. This is confirmed policy, not yet executed content — see TODO.md.

**Every companion added under this policy is, per the existing "Scope" rule above, romanceable by default** ("All recruitable companions are romanceable. No exceptions.") — full romance design (Gate 2 stat thresholds, Gate 3 beats) and, more fundamentally, Gate 1 personal-questline content, are separate future work per character, same as the existing roster (see TODO.md's "Personal questlines — broad-scope guiding-idea charting pass" item, which this policy makes larger in scope, not smaller).

### Scope

**All recruitable companions are romanceable. No exceptions.** This is a binding design rule. Any character who can be recruited as a player companion — main game or DLC — is romanceable, subject to their individual gate conditions.

Non-recruitable named NPCs: romance status is decided on a per-character basis during design and development. Some may be romanceable; some will not be. This is deferred and will not be established as a blanket rule in either direction.

**Pool (confirmed):** All recruitable companions (main game + DLC) + non-recruitable named NPCs TBD per character.

### The Double Gate

Romance requires two independent conditions to be met simultaneously. Failing either one closes the route.

**Gate 1 — Questline prerequisite:** The player must have completed the relevant relationship-building questline content with this character. The relationship has to have been built through shared experience and choices, not just dialogue options. This gate is the same for all characters.

**Gate 2 — MACHINE stat / trait threshold:** Each character has a specific profile of what they find attractive, derived from their personality, sensibilities, and history. The player's MACHINE stats and traits must meet that profile. This gate is unique per character.

**Perks are explicitly excluded from Gate 2.** MACHINE stats and traits are chosen at character creation — they define who the player character fundamentally *is*. Perks are acquired through play — they represent what the character has learned and done. The romance gate is about fundamental identity, not accumulated experience. A player cannot perk their way into a romance they weren't built for.

**Gate 2 checks permanent base stats only — not temporary boosts.** Temporary stat increases from food, chems, equipment, or any other time-limited effect do not count toward romance gate thresholds. Permanent raises — from character creation or through gameplay means such as the Intense Training perk — count in full. The gate is reading who the player character is, not who they are for the next thirty minutes.

**Gate ordering — confirmed:** Gate 1 always comes before Gate 2. The companion quest completes first; the MACHINE stat check fires second, at the first organic moment where the character would naturally move toward romance. If the build meets the threshold, the romance beat sequence begins. If it does not, the signal line fires and the door closes. The stat check is never presented as a hard wall before the relationship develops — it fires inside the relationship, in the character's own voice, at the natural inflection point. On a replay with an eligible build, the player who heard the signal line already knows what to work toward.

### Personal Questline Design Rule — The Player's Unique Capability, Established 2026-07-20

**Applies to companion personal questlines specifically — not the romance questlines (Gate 3).** Every companion's personal questline should hinge on something the player is able to do that the companion herself cannot — not because she's incapable in general, but because the player has some specific access, nature, or capability she genuinely lacks. This gives the player real, active agency in resolving what the character can't resolve alone, rather than making the player a bystander who simply witnesses the companion's own faction/skills/connections solve her problem off-screen.

**Origin:** surfaced while designing Favi della Torre's personal questline ("The Long Watch"). The original draft had Eyes of Gold's own intelligence-gathering turn up the fate of the Italian scientist she lost contact with — competent, in-character, but it left the player watching Favi's faction do the work. The fix: Eyes of Gold narrows down *where* the record is, but the record itself sits in a corrupted, post-Split-Brain fragment of the Arcanet that ordinary robot architecture can't reach — the player, as a Bridge Unit, is the one who actually jacks in and retrieves it (see `Hacking_and_Traceability_System.md`). Eyes of Gold's competence stays intact; the player's own unique nature is what actually closes the loop.

**How to apply:** the "something the player can do that she can't" doesn't have to be the Bridge Unit's jack-in ability specifically every time — that would get repetitive across a dozen-plus companions. It can be anything genuinely unique to the player's position: their outsider status (access to a faction or district a companion's own history bars her from), their specific skills/build, their role as Bridge Unit, their relationship to Calethina, or simply being new enough to the city to ask questions or go places that would cost a longtime local too much socially or politically. The point is that the companion's own resources — competence, faction, connections — get her most of the way, and the last, personal step is something only the player could have done for her.

**No single required stat, perk, or skill — minimum 5 viable stat-based approaches, established 2026-07-20.** Whatever that final player-only step is, it must not be gated behind one specific MACHINE stat, perk, or skill check — a companion's personal questline has to be completable by any build. Design at least 5 distinct approaches to that step, ideally spread across different stats/skills (e.g., a Calculation-driven approach, an Investigation-driven approach, a Nerve-driven approach, a Humanity-driven approach, an Engine-driven approach), so that whatever the player invested in, at least one route is open to them. This mirrors the classic multiple-solutions design pattern (combat / speech / skill / stealth routes to the same outcome) rather than introducing a new kind of build-gating through the back door of the "player capability" rule above. **As always in this system (Fallout: New Vegas-style, not a dice-roll TTRPG system): each check is deterministic — the player either has (or can temporarily reach, per the existing Gate 2 rule that only permanent stats count toward romance specifically) the required threshold, or they don't. No randomness involved.**

**Plus non-stat, world-state-based approaches — target 7–12, absolute floor of 3, established 2026-07-20.** Stat-based approaches alone can still produce a soft-lock: a player who built entirely outside the 5 covered stats — or who wants the completion to feel earned through the game world rather than purely through whether a stat threshold happens to be met — needs another way in. Routes should key off something else the player can plausibly have going for them: faction reputation earned elsewhere, knowledge or an item gained from unrelated content, an ally/relationship that happens to be relevant, and so on. **3 is the absolute minimum, never the target — aim for 7 to 12 wherever the world genuinely supports that many.** Every route, at any count, must make sense within the established context of the character's world — no route should be invented just to hit the number; if a district, faction, or piece of existing lore doesn't plausibly support a given approach, it doesn't belong on the list. **The specific reason this matters for romance in particular:** since Gate 1 (the companion questline) must complete before Gate 2 (the MACHINE stat/trait romance check) can even fire, a player whose build satisfies a character's romance threshold but who invested nothing in the 5 stat-based questline-completion routes must never be structurally unable to reach Gate 2 at all — the non-stat routes are what guarantee that romance eligibility and questline completion are never accidentally incompatible with each other.

**Critical caution — the categorical block must come first.** A stat-based approach only satisfies the "something she can't do" rule if the *category* of action is something the companion is structurally excluded from — by nature, access, role, or history — not merely something the player happens to meet a higher threshold on. If a companion has Investigation 10 herself, an "Investigation-driven approach" for the player is not a valid route unless something else about the situation excludes her entirely (wrong architecture, no access, barred by her own history, etc.) — otherwise the "rule" collapses into "the player met a threshold she could in principle have met herself." Establish the categorical exclusion first (why she structurally cannot engage with this at all), and only then vary *how* the player succeeds across the 5+ stat-based approaches.

**Recommended pattern — the player's standing with a faction/district the companion herself is on bad terms with, established 2026-07-20.** Where a companion has an established negative or wary relationship with a specific faction or district, one of her non-stat routes should ideally be the player's own *positive* reputation there (see `Reputation_System.md` for the full tier grid — Accepted, Liked, Smiling Troublemaker, Good-Natured Rascal, or Idolized; doesn't need to be Idolized, just genuinely positive) opening a door she couldn't open herself, precisely because she's on the wrong side of that relationship. Not a requirement for every companion — don't invent a faction antagonism just to satisfy this pattern — but where the lore already supports it, it adds real nuance: the player succeeds specifically *because* of who they are to a faction the companion herself never could be. First applied to Favi (see her `Questlines/README.md`, route 7): Eyes of Gold and Libra have an established mutual distrust neither side has formalized (`Factions/Eyes_of_Gold.md`), so a player with genuine positive standing at Libra can access a channel Favi's own faction membership would work against, not for.

**Recommended pattern — a Wild Child route, established 2026-07-20.** Aim for at least one non-stat route usable specifically by a player who holds **Wild Child** status (Idolized + Vilified simultaneously, per `Storyline/Endings/Secret-Endings/Wild_Child_Endings.md`) with some relevant faction or district. Wild Child is rare by design and already established to create genuine, mechanically real gaps and anomalous access precisely because the holder can't be categorized by the normal reputation system. This rewards the rare, extreme playstyle with real companion-content payoff, not just its own dedicated endings. Like the faction-antagonism pattern above, this is a recommendation to reach for where it genuinely fits, not a requirement for every companion.

**Recommended pattern — a Long Vigil route, established 2026-07-23.** Where a companion's own established
psychology gives her a genuinely high Personality Grief-Multiplier (see
`Fragmentation_Matrix.md` — Ayako Hayashi is the first confirmed case, given how directly her own wound maps
onto this state), her personal questline should include a route reachable only by a player who has brought
that specific companion to **The Long Vigil** (Grief Range 3 + Bond Range 3 simultaneously). Unlike the Wild
Child route recommendation above, this isn't an access-gap mechanic — it's content that can only exist
because this specific companion has both fully embraced who the player is now and never stopped grieving who
they left. The pathline should be genuinely unavailable any other way, not a flavor variant of a route
reachable through other means. Not every companion needs one — like the Wild Child pattern, reach for it
where a companion's own established psychology actually supports it, don't manufacture Grief-proneness for a
character whose file doesn't already point that way.

**Both tracks still require the base companion questline completed first, established 2026-07-23.** Bond/
Grief tracking on a companion presupposes an actual relationship exists to hold those feelings — a Long
Vigil pathline attempted before the player ever finished getting to know this companion in the first place
doesn't make narrative sense, exactly the same reason romance Gate 3 already requires companion-quest
completion. This isn't a new dependency between the two tracks; it's a shared prerequisite both already sit
on top of.

**Long Vigil and Romance are independent tracks *from each other*, established 2026-07-23.** A companion's
Long-Vigil-only pathline must never require the romance questline specifically to be active or completed,
and the romance questline must never require the Long Vigil pathline specifically — reaching The Long Vigil
with a companion depends only on Bond/Grief state (`Fragmentation_Matrix.md`), which is orthogonal to whether
the player ever romanced her. **However,
where both exist in a given playthrough, each should contain dialogue acknowledging the other.** A player who
is both romancing a companion and has brought her to The Long Vigil should hear that acknowledged in both
tracks — the Long Vigil pathline shouldn't play out as though the romance doesn't exist, and romance dialogue
shouldn't play out as though the Long Vigil state doesn't exist. This is a cross-reference requirement, not a
dependency — nothing gets locked behind the other track's completion, but nothing should read as unaware of
it either.

**Vary the flavor — do not default to bureaucratic records access every time, corrected 2026-07-20.** The first several Wild Child routes designed in this pass leaned heavily on one specific shape: an institution can't file the player, so an administrator forced into individualized handling surfaces information as a side effect (WC-4's Hub registry terminal is the underlying reference point, and it produced good results for Villena/Libra, Ayako/Cancer, and Flora/Libra — but repeating it for every companion would flatten what Wild Child actually represents). Wild Child's real premise is broader: the player is a live, unresolved contradiction that other people have to react to *somehow*, and "somehow" has many shapes. Established alternate flavors, to draw on before reaching for the bureaucratic default again:
- **Gossip/rumor flavor** (used for Naizelle/Pisces): the player becomes unavoidable talk in an informal information economy, and word of what's actually being searched for surfaces as a byproduct of people talking about the player, not through any institution processing anything.
- **Confessional/psychological flavor** (used for Seica/Scorpio): an institution built around sitting with irreconcilable truths engages with the player's own contradiction on its own terms, distinct from ordinary bureaucratic filing.
- **Persuasion/leverage flavor** (established 2026-07-20 for Ji-Eun/Aquarius, modeled directly on Fallout: New Vegas — during Arcade Gannon's companion quest, Wild Child status with the NCR lets the player talk Moreno into fighting alongside the NCR now, with the door left open to betray that arrangement later): someone chooses to gamble on the player specifically *because* their unresolved, paradoxical reputation makes them a wildcard worth betting on — not because any institution processed anything, but because a specific person decided the risk of engaging was better than the risk of refusing. Nothing guarantees the player actually honors what they implied to get the cooperation.
- Other shapes are fair game too — fear/intimidation (someone cooperates because refusing feels more dangerous than complying), opportunism (someone tries to exploit the player's notoriety for their own ends and the player can leverage that back), and likely others not yet used. When designing a new one, ask what kind of reaction *this specific* faction or district would actually have to an unresolvable contradiction, rather than reaching for the same administrative-gap mechanic by default.

### Threshold Design Per Character

When designing each romanceable character, specify:
- Which MACHINE stat(s) are required and at what level
- Which traits are **forbidden** for this character (see "Forbidden Traits" below — the standard mechanic,
  replacing the older, vaguer "required or dealbreaker" framing)
- The in-world rationale (what this person finds attractive and why, based on their personality)

Examples of how thresholds might read:
- A character who values physical presence → Might threshold
- A character who values intelligence and wit → Calculation threshold
- A character who values genuine emotional depth → Humanity threshold
- A character who admires courage and directness → Nerve threshold
- A character who values perceptiveness → Investigation threshold
- A character who values capability and endurance → Engine threshold

Multiple stats may be required.

### Forbidden Traits — A Categorically Different Gate, Confirmed 2026-07-28

**The standard mechanic for the "traits" half of Gate 2:** each romanceable character has **1 to 3 forbidden
traits** — specific traits from the full trait pool (`Character-Creation/Traits.md`) that, if the player
selected them at character creation, permanently disqualify that character's romance route. Derived the same
way stat thresholds are: from the character's **Enneagram personality, personal history, and personal
sensibilities** — just pointed toward exclusion rather than requirement.

**Why this is categorically different from the stat threshold, not just a variant of it:** a stat threshold
represents growth — a player who falls short today can still reach it later, through Intense Training, an
implant, or simply better allocation on a future save. A forbidden trait represents an unchangeable
character-creation choice, permanent for the entire playthrough. **There is no path to growing out of a
forbidden trait.** No amount of MACHINE-stat investment, Intense Training, or "not-Doctor-Usanagi" implant
work (`Character-Creation/Permanent_MACHINE_Stat_Increases.md`) can undo the fact that the player chose, at
the very start, to be a specific kind of person.

**Implementation precedence, confirmed 2026-07-28 — binding for actual game code (C++/GDScript/JSON dialogue
data):** a forbidden-trait check is evaluated *first* and takes total precedence over the standard MACHINE
stat-gate display below. If the player holds a forbidden trait, the game does not show the normal
passing/failing stat-check dialogue at all — it shows the character's own distinct forbidden-trait rejection
line instead. The two systems never display simultaneously for the same interaction; forbidden-trait
rejection completely overrides the stat-gate check.

**A distinct signal-line register, confirmed 2026-07-28:** forbidden-trait rejections get their own tone,
separate from the ordinary stat-threshold Signal below (which implicitly invites "come back once you've
grown"). A forbidden-trait line should read as a genuinely closed door — not a "not yet," but a "this isn't
something that changes."

**The trait-design pipeline this creates:** while assigning forbidden traits character by character, whenever
the existing trait pool doesn't contain something that actually captures what should disqualify a given
companion, pause and design a new trait to fill that gap. This makes trait-gate assignment a real, ongoing
trait-design pipeline in its own right, not just a companion-design pass.

### The Signal

When a player has completed the questline prerequisite but does not meet the **stat** threshold (a forbidden
trait, per above, is handled entirely separately and takes precedence), the character makes an honest,
casual, in-voice remark that reveals what they're looking for — without breaking the fiction or explaining
the system. The line is short and in character. It closes the romantic door without closing the relationship.

Examples of the register (not final lines — those are written per character in voice):
- *"Sorry, friend. I like them smart."*
- *"Not trying to be rude here, but come back once you've lifted some weights."*
- *"You're good people. Just not my type."*

The player who hears this line has a clear signal. On a replay with a different build, they know what to work toward. The line is delivered once and not repeated unless the player re-initiates.

### Gate Display — Visible MACHINE Stat Check

**Romance gates are displayed using the same visible stat-check UI as all other MACHINE stat checks in the game.** There is no special UI treatment for romance. Both the passing option and the failing option appear in dialogue simultaneously, regardless of whether the player meets the threshold.

- **Passing option:** All thresholds met — stats display in brackets, followed by the dialogue line.
- **Failing option:** One or more thresholds not met — failed stats display as [current/required], met stats display normally, followed by the companion's signal line.

Example (Lyuba Baranova; Nerve ≥ 8, Humanity ≥ 7, Engine ≥ 6):

> **[8 N][7 H][6 E]** *"...go on..."*
> **[6/8 N][6/7 H][6 E]** *"You break too easy."*

The visible failed threshold is what makes the signal line legible — the player can see exactly which stats they are short on and what to build toward on a replay. A hidden gate would leave the signal line ambiguous. This convention also maintains consistency with every other stat-gated dialogue check in the game.

**Fallout: New Vegas precedent (binding):** FNV uses visible skill checks throughout. Inner Tepenia follows the same convention.

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

### Sexuality by Character Type — Canon Rule

**Robot characters (companions and sexually-available NPCs):** Bisexual by default. Robots in Concordia do not organize attraction by the gender of their partner. This means they will pursue the player regardless of the player character's gender.

**Human female characters (companions and sexually-available NPCs):** Bisexual, same as robots — updated 2026-07-03 from the earlier "all humans heterosexual" rule. They pursue the player regardless of gender presentation.

**Human male characters (companions and sexually-available NPCs):** Heterosexual. Fixed-gender attraction — a human male companion or sexually-available NPC will only pursue a player character presenting as the gender he's attracted to.

**Mechanical consequence — the additional gender gate:** every romanceable companion, robot or human, still gates on the standard MACHINE stat/trait check (Gate 2, per the Double Gate system above) — **with the exception of Kendra Heinrich, whose romance has no stat gate at all** (see her design note below). On top of that, **romanceable human male companions gate on an additional gender check**: the player must be presenting as the gender he's attracted to, checked independently of and in addition to the MACHINE threshold. Robot companions and human female companions do not carry this extra gate — same as before, they gate on the MACHINE check alone.

This rule applies uniformly across both the romance roster and the casual "fuckable" pool. No exceptions are established at this time beyond Kendra's unique gate system.

---

### Thematic Note

The romance system is a direct expression of the second guiding principle — the nature of love between robots and humans. Every romance in the game, regardless of the species of the characters involved, is asking: what does this specific person find in this specific other person, and what does that mean for both of them? The stat/trait gate ensures that the answer is always grounded in who the player character actually is, not in what they've done or what perks they've accumulated.

---

### Confirmed Romanceable Characters

The following characters are confirmed romanceable. Thresholds are documented here as they are designed; entries marked TBD are pending Phase 3 personality work.

| Character | Type | Stat Thresholds | Trait Gates | Notes |
|-----------|------|-----------------|-------------|-------|
| Calethina | Projection system (not a companion) | Calc ≥ 8, Humanity ≥ 6, Nerve ≥ 6, Engine ≥ 6 | TBD | See full design note below; romance post-download via mini-quest |
| IT-068 [Flora] | Recruitable companion | Nerve ≥ 7, Calculation ≥ 6, Engine ≥ 5 | See character file | First companion; 6w5 Thinking; see full romance design note below |
| Favi della Torre | Recruitable companion | Nerve ≥ 7, Humanity ≥ 6, Engine ≥ 6 | See character file | 6w5 Self-Pres; loyalty proven through protective choices; see full design note below |
| Villena Hiresvett | Recruitable companion | Agility ≥ 6, Humanity ≥ 6, Nerve ≥ 5 | See character file | 7w6 Self-Pres; presence and genuine engagement; see full design note below |
| Naizelle d'Edjordoś | Recruitable companion | Calculation ≥ 7, Investigation ≥ 6, Engine ≥ 5 | See character file | 5w6 Self-Pres; most patient romance in the game; see full design note below |
| Seica Cenilaithe | Recruitable companion | Nerve ≥ 7, Might ≥ 6, Humanity ≥ 6 (possibly 7 — TBD) | See character file | 8w7 Sexual; see full romance design note below |
| Ji-Eun Kim | Recruitable companion | Calculation ≥ 8, Investigation ≥ 6, Humanity ≥ 6 | See character file | 5w4 Social; in hiding; undelivered letter is a separate gate outside romance arc; see full design note below |
| Vosora Lashár Tanslock | Recruitable companion | Calculation ≥ 7, Investigation ≥ 6, Nerve ≥ 6 | See character file | 5w6 Social; romance happens within the investigation; see full design note below |
| Michelle Stanton | Recruitable companion | Calculation ≥ 7, Humanity ≥ 6, Engine ≥ 7 | See character file | 5w6 Social; built the Arcanet; chose to stay; romance through shared commitment; see full design note below |
| IT-021 [Fenny] | Recruitable companion | Humanity ≥ 7, Engine ≥ 6, Nerve ≥ 5 | TBD | 6w5 Self-Pres; quietest romance in the game; no signal line — she just doesn't warm up; see full design note below |
| FW-25 [Pink Lucy] | Recruitable companion | Humanity ≥ 7, Engine ≥ 6, Nerve ≥ 5 | TBD | 7w6 Social; communal intimacy; romance unfolds through The Warm Circuit; see full design note below |
| Kendra Heinrich | DLC 1 companion | **None** | **None** | Unique gate system — see full design note below |
| Salagéa Aparast | DLC 5 companion | TBD | TBD | Thresholds pending Phase 7 personality design |
| + all future companions | TBD | TBD | TBD | Rule: all recruitable companions are romanceable by default |
| **Majyao Bisyugota** | **Non-recruitable NPC** | Humanity ≥ 7, Investigation ≥ 6, Calculation ≥ 6 | See character file | 4w5 Self-Pres; teahouse keeper; romance through repeated visits and questline depth; Blood River Tea thread — see design note below |
| Ayako Hayashi | Recruitable companion | Investigation ≥ 7, Humanity ≥ 7, Calculation ≥ 6 | See character file | 4w5 Self-Pres; Red Spiral medic; highest Investigation gate in the roster; see full design note below |
| Lyuba Baranova | Recruitable companion | Nerve ≥ 8, Humanity ≥ 7, Engine ≥ 6 | TBD | 8w7 Sexual; silver-tongue / unarmed fighter; Aries; highest Nerve gate in the roster; see full design note below |
| TCY-25 "Rui" | Recruitable companion | TBD | TBD | 9w1 Self-Pres; Scorpio transformation practitioner; confirmed recruitable 2026-07-10; thresholds pending Phase 3 personality design |
| **Majyao Bisyugota** | **Non-recruitable NPC** | Humanity ≥ 7, Investigation ≥ 6, Calculation ≥ 6 | See character file | 4w5 Self-Pres; teahouse keeper; romance through repeated visits and questline depth; Blood River Tea thread — see design note below |
| **Trisha Miller** | **Non-recruitable NPC** | Nerve ≥ 7, Humanity ≥ 7, Might ≥ 7 | See character file | 8w7 Social; radio host; romance through recurring off-air encounters; see full design note below |

Non-recruitable named NPCs confirmed romanceable: Majyao Bisyugota, Trisha Miller (design notes below). Further NPC romance status decided per character during design.

---

### Calethina — Romance Design (Special Case)

Calethina is romanceable. She is the most demanding romance in the game narratively — though no longer
mechanically via a MACHINE stat threshold. **Corrected 2026-07-23: this section previously described a
stat-gate design (Calculation ≥8, Humanity ≥6, Nerve ≥6, Engine ≥6) that was superseded and dropped entirely
during the 2026-07-12 design session** — see `Questlines/Substrate_Transfer_and_Embodiment_Design.md` for
the full authoritative design this section now reflects.

**Gate design — redesigned to match Kendra Heinrich's own precedent.** The stat-threshold idea was dropped
specifically because the download's own stat penalty (see below) would collide with a numeric romance
threshold in ways hard to make fair on purpose: evaluate the gate pre-penalty and the threshold becomes
pointless; evaluate it post-penalty and it risks punishing exactly the players it's meant to reward. Kendra's
own gate already solves this — entirely conduct-based, no stat or trait requirement at all — so Calethina's
gate mirrors that shape instead:
- **Gate 1 — commitment:** the player completes her personal companion questline through to a **full
  download decision — either branch**, "inside you" or new-body embodiment (see below). A partial download,
  a no-download outcome, or an alternative stabilization path does not meet this gate.
- **Gate 2 — conduct:** across vital plot points in her personal questline, the player doesn't say or do
  anything combative, insulting, or abhorrent to her sensibilities — the equivalent of Kendra's "not kicking
  her while she's down."

Both gates met → romance becomes available. This makes the old stat-interaction tension moot rather than
solved — eligibility is behavioral, not numeric, so the download's stat penalty has nothing left to collide
with.

**The download and the romance are separate events.** The Calethina questline ("Echoes of the Bridge")
builds the relationship across its full length. The download decision (approximately midpoint of the main
quest) is available to any player who has made the associated questline decisions — it is not stat-gated
either. The download is about saving/keeping her. The romance is a separate question about what the
relationship becomes afterward.

**The download: two branches, not one.** On the **"inside you"** branch, she isn't simply transferred to
the protagonist's wrist device — she becomes part of the protagonist, carried within them, projecting from
the protagonist's own body; this branch also carries a same-magnitude stat trade (+n Calculation/
Investigation/Nerve/base Hacking%, matched by −n to Engine/Might/Humanity). On the **new-body/embodiment**
branch — her first physical body in her entire existence — there's no stat change in either direction; the
cost instead is memory/personality fidelity loss in the transfer itself, with the actual non-stat reward
currency still TBD (three candidates floated, none chosen — see the Substrate design doc). Both are a
profound chosen bond regardless of whether the romance follows, and both now count equally toward Gate 1.

**Romance eligibility no longer requires the "inside you" branch specifically** — that branch is required
for a different, separate unlock (cross-DLC companion portability, see the Substrate design doc), not for
romance. Either full-download branch satisfies Gate 1 here.

**The romance option appears once both gates are met.** The protagonist and Calethina now share whatever
physical reality the chosen branch produced — inside them, or beside them in a new body — but the romantic
arc is a separate layer, unlocked by conduct across the questline rather than a build requirement.

**The romance mini-quest.** If the romance option appears, it is its own dedicated interaction sequence
distinct from the main questline — a focused arc that constitutes the actual romantic relationship
developing between the protagonist and Calethina in the post-download state. Specific beats are Phase 5
design work.

**Built-in bittersweet weight.** Whichever branch is chosen, the full download carries a confirmed risk of
memory or fidelity loss in transfer. The romance begins with the protagonist having already accepted losing
some piece of her in order to keep her at all.

**The re-spec complication.** If the player re-specced through Calethina's lab to meet some other threshold
elsewhere in the game, she performed that work herself. She knows what was changed and why. Wherever the
romance option actually lands should have dialogue that acknowledges this — as a branch, not a single read.
Whether she finds it moving (someone wanted to be someone she could love) or troubling (someone altered who
they were) are both valid. Both are bittersweet.

**The Calethina Devotion failsafe ending** has two versions: one for players who completed the romance
mini-quest, one for players who reached a full download (either branch) without Gate 2 conduct having been
maintained. The second version reflects a different kind of profound chosen bond — she is with them, in
whichever form the download took, and that is its own thing.

---

### Vosora Lashár Tanslock — Romance Design

**Stat gate:** Calculation ≥ 7 (primary), Investigation ≥ 6 (secondary), Nerve ≥ 6 (tertiary)

**Rationale:** Vosora is a 5w6 Social type — distinct from the Self-Pres 5 in that she remains engaged with the world through her work rather than retreating from it. She is already doing something that matters (the Great Corruption investigation), and the romantic path runs through that work rather than around it. Calculation is primary because intellectual respect is non-negotiable for any 5, and for a Social 5 it also means understanding why the work matters. Investigation reflects her own orientation — she's drawn to someone who operates in the same register of careful attention. Nerve ≥ 6 serves the 6 wing: the investigation is dangerous and produces disturbing revelations; she needs someone who can hold steady under difficult information without panic or dismissal.

**Forbidden traits:** see Vosora's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Vosora Lashár Tanslock/README.md`) for her specific forbidden trait and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"I don't doubt your intentions. I just need people around this work who can actually keep up with it."*

**Gate 3 — Romance beats** (after companion quest completion):

Vosora's romance happens within her work, not alongside it. The player becomes a partner before they become anything else.

1. **Engage with the investigation, not just with her:** The romantic path requires genuine care about what she's uncovering — asking real questions about the data, noticing something she hadn't, treating the investigation as something that matters in its own right. She can tell the difference between interest in her work and interest in her through her work.

2. **Handle a difficult revelation without flinching:** At some point the investigation produces something disturbing or destabilizing. The 6 wing is watching for steady acknowledgment — neither panic nor dismissal. This is the test she doesn't announce she's administering.

3. **Respect the compartmentalization:** She keeps things organized and separate — not as concealment but as how she functions. The romantic path respects that structure early on and does not try to collapse it before she's ready to.

4. **Intellectual reciprocity:** A Social 5 shares knowledge as connection. The player shares something back — an insight, an angle she hadn't considered, information that actually advances the work. The exchange is what creates intimacy for her, not the gesture.

5. **She starts consulting, not just informing:** The turning point isn't a declaration. It's when she sends the player something outside of operational necessity — when she asks what they think before she's decided. The player knows before she says anything.

6. **The culmination, within the work:** It happens in the context of the investigation, not in a separate emotional scene. While looking at the same data, the same problem. It belongs to the world she actually lives in.

---

### Michelle Stanton — Romance Design

**Stat gate:** Calculation ≥ 7 (primary), Humanity ≥ 6 (secondary), Engine ≥ 7 (tertiary)

**Rationale:** Michelle is a 5w6 Social type, same as Vosora, but her emotional core is distinct. Where Vosora's intimacy is through shared intellectual pursuit, Michelle's is through shared commitment to a place. She built the Arcanet — the Antarctican internet — and she chose to stay in Concordia when she has the means to leave. Calculation is primary because she needs genuine intellectual depth. Humanity is secondary because she built something that connects everyone; she cares about people collectively and needs to feel the player does too. Engine at 7 — the highest tertiary in the roster — reflects that she has sustained an enormous ongoing commitment for a very long time; she is drawn only to someone who can match that kind of staying power.

**Forbidden traits:** see Michelle's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Michelle Stanton/README.md`) for her specific forbidden trait and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"You seem like someone passing through. I don't have much use for those."*

**Gate 3 — Romance beats** (after companion quest completion):

Michelle's romance is about the player coming to understand why she stays, and demonstrating that they understand it in the only way that counts — by making the same kind of choice themselves.

1. **Engage with the Arcanet as more than infrastructure:** The romantic path requires understanding that what she built isn't just a communications network — it's what she chose to give. Questions about why she built it the way she did, what she was trying to make possible. She notices the difference between someone who appreciates the achievement and someone who understands the intention behind it.

2. **Ask the real question:** At some point the player genuinely asks why she stays when she could leave. The romantic path is a player who listens to the answer and takes it seriously — not using it, not performing interest, not skipping past it. The answer is the most honest thing she offers.

3. **The Rastra moment:** She teaches the player to maintain the vehicle that makes leaving possible. This is an act of trust — she is giving the player access to her capacity to go. The romantic path treats this with the weight it deserves, not as a tutorial.

4. **Choose the city when it would be easier not to:** During her quest, a choice arises where the player could deprioritize Concordia's needs for something personally advantageous. The romantic path doesn't. She stayed because she believes in this place; the player has to demonstrate they understand what that means in practice.

5. **The view from outside:** The most intimate thing she can offer is showing the player what Concordia looks like from a position where leaving is genuinely possible — literally, from the Rastra outside the city, or metaphorically, from her perspective as someone who could go anywhere and chose here. The romance closes with that shared vantage point.

---

### Favi della Torre — Romance Design

**Stat gate:** Nerve ≥ 7 (primary), Humanity ≥ 6 (secondary), Engine ≥ 6 (tertiary)

**Rationale:** Favi is a 6w5 Self-Preservational type and a sniper — patient, precise, controlled, managing uncertainty through preparation and a small circle of people she can absolutely trust. Nerve is the primary gate not as a test of confrontational courage but as a test of whether the player will hold when it matters to someone else, not just themselves. She watches how people behave when protection costs them something. Humanity confirms that the player's protective instincts come from genuine care rather than calculation — she can tell the difference. Engine at 6 reflects the Self-Pres subtype's value for sustained reliability: showing up consistently over time matters more to her than isolated heroism.

**Forbidden traits:** see Favi's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Favi della Torre/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"I've seen a lot of people who were brave until it mattered. Come back when I've seen more of you."*

**Gate 3 — Romance beats** (after companion quest completion):

Favi's romance is loyalty proven incrementally, in the specific currency she values — protective choices made without being asked.

1. **Protect someone she cares about unprompted:** During her quest, the player has an opportunity to protect one of her people without being asked. Not a heroic moment — a quiet, practical choice to cover someone she's been watching over. She notices who does this automatically and who has to be directed.

2. **Don't push her pace:** Self-Pres 6s open slowly, and she has real anxiety about being taken advantage of. The romantic path requires respecting the pace she sets without pressing for more at each stage. Patience signals safety in a way nothing else does.

3. **Tell an inconvenient truth:** At some point a small lie would be easy, harmless, undetectable. The romantic path tells the truth anyway. A 6 is always watching for inconsistency because they're watching for signs of eventual betrayal. The player who tells the truth when lying was available demonstrates something that cannot be faked or substituted.

4. **The shared watch:** A quiet scene where they're waiting together, covering the same position literally or figuratively. The 5 wing means she's comfortable with silence; the Self-Pres means she finds genuine security in shared vigilance. No declaration, no drama — just two people watching the same horizon.

5. **She names it first, almost as an aside:** The culmination happens while she's doing something protective. The declaration is almost incidental to the action. Almost.

---

### Naizelle d'Edjordoś — Romance Design

**Stat gate:** Calculation ≥ 7 (primary), Investigation ≥ 6 (secondary), Engine ≥ 5 (tertiary)

**Rationale:** Naizelle is a 5w6 Self-Preservational type. A Self-Pres 5 builds security through private resources — time, space, knowledge, solitude — and extends access to their interior life only to very carefully selected people across a slow, deliberate process. Calculation is the primary gate because she needs an intellectual equal: someone genuinely curious about the world in the same register she is, not someone she has to explain herself to. Investigation reflects the 5's attraction to people who pay attention and notice what is actually there. Engine serves the 6 wing: sustained reliability over time, the endurance to remain present across a long, slow process without pushing.

**Forbidden traits:** see Naizelle's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Naizelle d'Edjordoś/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"I don't think you'd find much of interest here. Most people don't."*

**Gate 3 — Romance beats** (after companion quest completion):

The most patient romance in the game. Her arc is not about dramatic moments — it is about the player demonstrating, over time, that they can be trusted with access to someone who has built elaborate defenses around their interior world.

1. **Don't push past what she's offered:** Early opportunities arise to press further than she has given. The romantic path requires not taking them — no asking for more information than she's volunteered, no showing up uninvited, no attempting to accelerate the pace of intimacy. A Self-Pres 5 closes if pushed, and once closed, the door does not reopen easily.

2. **Intellectual contribution:** She needs to feel the player brings something to the exchange rather than only receiving from her. A moment where the player's knowledge or perception adds something she hadn't considered. She takes note. She says very little about it. The note matters.

3. **The question she wasn't prepared for:** The player asks her something about herself that no one has thought to wonder — not invasive, just specifically curious about something she hasn't been asked before. She answers more than she intended. She notices that she did.

4. **The test of patience:** She goes quiet. Withdraws. Doesn't respond for a period. This is processing, not rejection. The romantic path requires waiting without pressure — one gentle check-in, then silence. She notices who does this and who doesn't.

5. **Her first voluntary disclosure:** She tells the player something about herself that wasn't asked for and wasn't necessary to share. It sounds like information. It is also intimacy. This is the real turning point.

6. **The culmination:** Naizelle says, in her precise careful way, that she wants the player to stay. Not dramatically, not in the conventional romantic register — just an acknowledgment, stated clearly, that she has made space for this person that she makes for no one else.

---

### Villena Hiresvett — Romance Design

**Stat gate:** Agility ≥ 6 (primary), Humanity ≥ 6 (secondary), Nerve ≥ 5 (tertiary)

**Rationale:** Villena is a 7w6 Self-Preservational type — she seeks security through abundance, experience, and a life that is always moving forward. As a performer in Leo, she has spent her career reading audiences and can spot artifice immediately. Agility is the primary gate not for its combat meaning but for what the stat represents: quickness, adaptability, someone alive to the moment who can genuinely keep up with her. Humanity serves the 6 wing — she cares deeply about people and needs warmth, not calculation, across from her. Nerve reflects the 7's attraction to boldness and the 6 wing's need to know the player won't fold.

**Forbidden traits:** see Villena's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Villena Hiresvett/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"You're sweet. I just need someone who can actually keep up, you know?"*

**Gate 3 — Romance beats** (after companion quest completion):

Villena's romance requires engagement, presence, and genuine reciprocity. She performs constantly; the arc is about the player becoming someone she doesn't have to perform for.

1. **Don't be an audience:** The romantic path requires engaging with her rather than appreciating her. Push back on a performance. Ask what she actually thinks, not what she's projecting. She knows the difference immediately and registers it.

2. **Bring something new:** The player introduces her to something genuinely new — a place, an idea, an angle on something familiar. A 7 responds to genuine novelty in a specific way: she lights up, and it's real rather than performed.

3. **The moment she stops performing:** After something difficult in her quest, the performance drops for just a beat. The player who notices and doesn't rush to fill the silence with reassurance — who simply lets her be unperformed for a moment — passes this without a word. She does not forget who gave her that.

4. **The loyalty test (6 wing):** An opportunity arises to prioritize something else over Villena in a situation where she would genuinely understand if the player did. The romantic path stays with her. The 6 wing holds onto this quietly, and it matters to her more than she admits.

5. **The future question:** A Self-Pres 7 is always moving forward, imagining what comes next. The culmination involves her inviting the player into her vision of the future. The romantic path accepts — genuinely, not as flattery. An actual yes.

**The culmination:** Probably loud and warm, in her natural register. But there's a moment of real quiet inside it — brief, unperformed — before she returns to herself.

---

### Ji-Eun Kim — Romance Design

**Stat gate:** Calculation ≥ 8 (primary), Investigation ≥ 6 (secondary), Humanity ≥ 6 (tertiary)

**Rationale:** Ji-Eun is a 5w4 Social type in hiding. The Calculation floor is the highest in the game — she is deeply competent and needs an intellectual equal who earns genuine respect before anything else opens. Investigation reflects the 4 wing's hunger to be specifically seen: the player must be someone who notices what's actually there, not just the composed surface. Humanity serves both the 4 wing (whose core wound is feeling unseen) and the Social subtype (she cares about people and meaning despite her withdrawal).

**Forbidden traits:** see Ji-Eun's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Ji-Eun Kim/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"I appreciate the interest. I just — I can't afford to be careless about who I talk to."*

**Gate 3 — Romance beats** (after companion quest completion):

Ji-Eun's romance is built on trust with specific stakes — she is in hiding for a reason, and letting someone in is a genuine risk, not only emotional vulnerability.

1. **Prove you can hold a secret:** The player learns something sensitive about her situation during her quest. The romantic path requires that information to stay completely protected — not used, not referenced, not treated as leverage even accidentally. She watches to see if it leaks. It is the first real test.

2. **See past the competence:** She presents as composed and capable. The romantic path requires the player to demonstrate awareness that there is more underneath — not by probing, but by showing they have been listening past the surface. A question that could only come from genuine attention.

3. **The 4-wing moment:** A beat where the player responds to something specifically Ji-Eun — something that could not be said to anyone else in the same way. She needs to feel treated as an individual, not a category. The romance fails quietly if she feels interchangeable.

4. **Her choice to stop hiding from this one person:** The culmination is not dramatic. It is simply her deciding to let the player past a specific wall she has maintained. Not necessarily stopping hiding from the world — but choosing, deliberately, to stop hiding from here.

**The culmination:** Quiet. Deliberate. Stated almost formally, in the way someone speaks when they have chosen their words very carefully because they mean them exactly.

---

**The Undelivered Letter — Separate Gate (design note)**

The undelivered letter is NOT part of the romance arc. It is a distinct, deeper layer of intimacy with its own specific requirements — designed as a separate questline, mini-questline, or gate-check.

Key design principle: it is possible to earn Ji-Eun's deepest trust and respect without earning her love, and it is also possible to romance her without reaching the letter. The two paths are parallel, not sequential. The letter gate requires very specific conditions that are TBD — but they are of a different order than romance requirements. Post-romance access is one possible route; there may also be a non-romance path that reaches it through demonstrated loyalty, shared stakes, or specific quest choices.

Full design of this gate is Phase 3 character work.

---

### Seica Cenilaithe — Romance Design

**Stat gate:** Nerve ≥ 7 (primary), Might ≥ 6 (secondary), Humanity ≥ 6 — possibly 7, TBD (tertiary)

**Rationale:** Seica is an 8w7 Sexual type — the most intensely one-on-one focused configuration of the 8. She tests people constantly and only invests in those who hold their ground under her. Nerve is the primary gate because she needs to know the player won't fold under her intensity; anyone who flinches or appeases loses her interest immediately. Might reflects the 8's instinctive, body-forward nature — physical presence and directness matter. Humanity is higher than might be expected because Sexual 8s invest deeply in specific individuals; she needs to feel a full, emotionally genuine person across from her, not a calculating presence. Low Humanity would put her off regardless of other stats.

**Forbidden traits:** see Seica's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Seica Cenilaithe/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"You're interesting. Just — not like that. Not yet."*

**Gate 3 — Romance beats** (after companion quest completion):

Seica's romance is about challenge, testing, and the gradual revelation that she has let someone past the perimeter. The arc is not about softening her — it is about earning the interior she has been protecting.

1. **Hold your ground when she tests you:** She will push the player, probably multiple times, as genuine assessment rather than game-playing. The romantic path requires not backing down, not apologizing unnecessarily, not treating her directness as aggression to be managed. Deflection fails. Appeasement fails. Holding ground passes.

2. **The moment you call her out:** At some point she will be wrong about something, and she will know it. The player must say so directly. An 8 respects someone who can challenge them without flinching. She will not thank the player. She will not apologize graciously. But the way she looks at the player afterward is different.

3. **Show up physically:** Not necessarily through combat, but through presence — being unafraid of her in a situation where fear would be reasonable. The 8w7 Sexual notices this in a specific way nothing else replicates.

4. **The unexpected gentleness:** After all the confrontation, a moment of genuine care that isn't performed. Not sentimental; not soft for softness's sake. Just real. The 7 wing makes her capable of warmth she doesn't lead with; she recognizes it when it's honest, specifically because of everything that came before it.

5. **Her saying something true:** Not a confession exactly. A moment where she says something about herself unfiltered, then moves on quickly as if she didn't. Small. Real. Only accessible after all of the above.

**The culmination:** Direct and unambiguous — no indirection, no understated practical statement. An 8w7 Sexual who has decided doesn't hedge. She says it like she means it because she does.

---

### IT-021 [Fenny] — Romance Design

**Stat gate:** Humanity ≥ 7 (primary), Engine ≥ 6 (secondary), Nerve ≥ 5 (tertiary)

**Rationale:** Fenny is a 6w5 Self-Preservational type whose 5 wing suppresses the outward warmth typical of a Self-Pres 6, channeling it inward — into her home, into the care she takes with her private space, into a loneliness she does not broadcast. She wants to love someone and does not know how to reach toward that. Humanity at 7 (the highest in the roster) reflects that what she needs is not competence, courage, or intellect — it is genuine warmth that does not need to announce itself. Engine reflects the Self-Pres subtype's need for someone who keeps showing up rather than arriving dramatically. Nerve ≥ 5 is gentle — not a test for crisis courage, but for quiet steadiness over time.

**Signal line:** She does not deliver a signal line. She simply does not warm up. The door stays polite and closed.

**Gate 3 — Romance beats** (after companion quest completion):

The quietest romance in the game. Almost nothing is said directly. Every beat is in small actions, presence, and things noticed rather than stated.

1. **Showing up without agenda:** She is cautious of people who have obvious reasons for being around her. The romantic path is the player who comes by without needing anything, who sits with her without filling the silence with purpose. She keeps expecting the ask. It doesn't come.

2. **Noticing the second chair and not making it a thing:** The player notices and either says nothing, or says exactly one true thing — not a joke, not a probe. She remembers who noticed and how they handled it.

3. **Not trying to fix her:** The wrong path is positioning yourself as the solution to her loneliness. The right path is being present without framing it as rescue. She can feel the difference between someone who sees her pain as a problem and someone who simply sees her.

4. **Receiving the small offerings:** She begins offering things — a seat, something warm to drink, a question that needs a longer answer than one word. The player must receive these without rushing past them. Each one is a door opened slightly. Pushing further before she is ready closes it.

5. **The thing she has never said to anyone:** Not a confession of love — something smaller. A thought she has had but never articulated, said quietly while doing something else. She moves on immediately. The player who remembers it later, and shows that they do, passes something she did not know she was testing.

6. **The second chair:** The culmination does not come with a speech. She sets the table for two without being asked. The romance closes in the space between that action and what the player does next.

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

### IT-068 [Flora] — Romance Design

**Stat gate:** Nerve ≥ 7 (primary), Calculation ≥ 6 (secondary), Engine ≥ 5 (tertiary)

**Rationale:** Flora is a 6w5 Thinking type. Her core anxiety is whether people will hold under pressure — whether someone who seems reliable actually is. Nerve is the stat most directly about not flinching when things get hard, which is her primary question about any person she might trust. Calculation reflects the 5 wing: she respects someone who thinks through problems rather than charging in blind. Engine represents sustained reliability over time, not just crisis capability.

**Forbidden traits:** see Flora's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/IT-068 [Flora]/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"You seem decent. Just — I need to know someone can hold. I don't think I've seen that in you yet."*

**Gate 3 — Romance beats** (after companion quest completion):

Flora's romance is built from accumulated small proofs rather than any single dramatic moment. She is suspicious of grand gestures and reads them as performance.

1. **The crew choice:** A situation arises — during or around her quest — where protecting her crew costs the player something meaningful (a better tactical option, time, a resource). The romantic path requires making that choice without fanfare, as the obvious right call. She notices who makes it and who doesn't.

2. **The honesty test:** Flora asks the player a direct question about their motives or intentions. Multiple answer options are available. The romantic path requires the true answer, even if it's uncomfortable. She can tell the difference between the polished answer and the real one, and she remembers.

3. **The competence moment:** Post-quest, a technical problem comes up that the player solves through genuine skill (Calculation or engineering check). Not because it's required by the scene — because they actually knew what they were doing. The 5 wing is impressed by this in a way nothing else produces. It shifts how she looks at the player.

4. **The quiet scene:** A private beat with no crisis attached — maintenance, waiting out a delay, post-crisis wind-down. She talks. The player must ask actual questions and listen. Curiosity, not compliments. She responds to genuine interest and is skeptical of flattery.

5. **The culmination, on her terms:** Flora doesn't make declarations. The romance closes the way she communicates everything else: while doing something else, not quite looking at the player, something that sounds like a practical statement until you hear what it actually is.

---

### FW-25 [Pink Lucy] — Romance Design

**Stat gate:** Humanity ≥ 7 (primary), Engine ≥ 6 (secondary), Nerve ≥ 5 (tertiary)

**Rationale:** Pink Lucy is a 7w6 Social type — her entire vocation is built around collective morale, belonging, and bringing genuine warmth into post-war Concordia through The Warm Circuit. A Social 7 reads through performed care immediately; the Humanity threshold is slightly higher than the other 7 in the roster (Villena, ≥ 6) because warmth is not just a preference for Pink Lucy — it is the whole substance of her work. Engine serves the 6 wing: beneath the restless enthusiasm is a need for someone who stays, who doesn't burn bright and disappear. Post-war Concordia has already taken enough from her; reliability matters more than grand gestures. Nerve ≥ 5 is the minimum bar for matching her energy — a very low-Nerve player would feel like dead weight to someone whose life runs on momentum and yes.

**Signal line** (if stat threshold not met): *"You're good people. I just need someone around who actually loves people back. The work requires it."*

**Gate 3 — Romance beats** (after companion quest completion):

The romance unfolds in the context of The Warm Circuit — her entertainment cooperative and the living expression of what she has built. A Social 7 finds intimacy through shared experience in the world, not in isolation.

1. **The invitation:** She invites the player to participate in a Warm Circuit community event — not as an audience member but as a participant. This is how she includes people; she doesn't let them watch. The player shows up and engages genuinely.

2. **The unguarded moment:** During or after an event, the player catches her in a private moment of doubt. She is holding morale infrastructure together in a post-war city that lost everything. The 6 wing's fear surfaces when she thinks no one is watching: what if it falls apart? What if it isn't enough? The optimism is real — and so is what it costs to maintain.

3. **The player stays:** Rather than encouraging her or trying to fix the problem, the player stays present in that moment without resolving it. No cheer. No solution. A Social 7 with a 6 wing who feels genuinely held — not managed, not performed at — for the first time. This is the pivot.

4. **The follow-through:** The player shows up again. The next event. The next ask. Nothing dramatic — consistent. The 6 wing registers this one way: *you came back.* That is the thing.

5. **The opening:** She tells the player what she's decided. A 7 doesn't torture herself with ambiguity once she's reached a conclusion; she names it directly. Warm, a little nervous in a way she doesn't usually allow herself to be.

---

### Majyao Bisyugota — Romance Design (Non-Recruitable NPC)

Majyao does not join the player's party. The romance arc runs through her teahouse — repeated visits, escalating depth, the relationship built through her questline and the time the player chooses to spend in her space.

The gate system applies identically: Gate 1 (questline/relationship prerequisite), Gate 2 (stat threshold). There is no companion quest; her questline content and repeated visits serve the Gate 1 function.

**Stat gate:** Humanity ≥ 7 (primary), Investigation ≥ 6 (secondary), Calculation ≥ 6 (tertiary)

**Rationale:** Majyao is a 4w5 Self-Preservational type. A SP 4's deepest need is genuine depth — to be truly seen rather than charmed. She extends warmth to every patron; she will only open to someone who has real emotional interior. Humanity at 7 (tied with Fenny for the highest in the roster) reflects that the bar is not competence, courage, or intellect — it is the capacity for genuine feeling and presence. Investigation reflects the 5 wing: she is drawn to people who notice things. Her teahouse is full of deliberate, specific details; the patron who asks about them, who clocks the gap where Blood River Tea used to be, who pays careful attention to what is actually there — that patron gets somewhere. Calculation reflects the intellectual depth the 5 wing craves; she is Feeling-centered, not primarily intellectual, but she needs a mind that can go somewhere.

**Forbidden traits:** see Majyao's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/non-recruitable/Majyao Bisyugota/README.md`) for her forbidden traits and rationale (currently in progress, not yet finalized) — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"I like that you come here. It means something. But I think what you're looking for is different from what I'm able to give."*

**Gate 3 — Romance beats:**

The quietest, most internally textured romance in the game alongside Fenny. She will not reach toward the player; she responds to the player reaching toward her. She is noticed first, then more deeply, then actually seen.

1. **The first real conversation:** Most patrons get warmth and a good cup of tea. This is the first conversation that goes somewhere unexpected — the player asks a specific question about a tea, a detail of the teahouse, something particular. She pauses. She answers at length. She didn't expect someone to actually ask.

2. **The return:** The player comes back. Multiple times. She begins to extend particular attentions — she knows their order before they give it, she brings something unexpected. She says nothing about it.

3. **The depth moment:** A conversation that breaks through the surface, tied to her questline. Janbogo. The war. What it means to have rebuilt something from nothing in the only city left. She says something she hasn't said to anyone else. The player doesn't try to fix it. They listen.

4. **The Blood River Tea moment** *(optional — expand during questline design)*: If the player has followed the Blood River Tea thread — the supply line from Taylor Valley that the Long Night War cut, which she can no longer serve — and can bring her news of it, or in the best case a sample, something opens in her response that nothing else produces. This is the clearest possible signal that someone was paying attention to what actually matters to her, not just to her. Specific mechanics and what this unlocks are to be expanded when the Blood River Tea questline thread is developed in coordination with Frostlands/Taylor Valley design.

5. **The silence:** The teahouse is empty after closing. The aurora through the floor-to-ceiling windows. Both of them simply present, not needing it to be anything else. A 4w5 SP's romance begins in the quiet, not in a speech.

---

### Trisha Miller — Romance Design (Non-Recruitable NPC)

**Confirmed romanceable 2026-07-28.** Trisha does not join the player's party. The romance arc runs through
her off-air windows in Taurus (`NPC Schedule (In-Game Clock)` in her own character file) — recurring
in-person encounters while she's out among her community, rather than a companion questline structure.

The gate system applies identically: Gate 1 (relationship prerequisite, built through repeated off-air
encounters and her own questline content), Gate 2 (stat threshold). There is no companion quest; the
recurring encounters serve the Gate 1 function, the same way Majyao's repeated teahouse visits do.

**Stat gate:** Nerve ≥ 7, Humanity ≥ 7, Might ≥ 7 — **all three set equal, no primary/secondary/tertiary
ordering**, confirmed 2026-07-28.

**Rationale:** Trisha is an 8w7 Social type. An 8 has zero tolerance for half-measures in any single
dimension — she doesn't rank which quality matters most because she's watching for total, non-negotiable
substance across the board, not competence in one area propped up by weakness elsewhere. Nerve reflects her
own directness and conviction — she speaks her opinions plainly and expects the same boldness back, not
evasiveness. Humanity reflects that she "puts no emotional distance between herself and the people who love
her" — she needs someone equally willing to close distance, not hold back. Might reflects the physical half
of "uses her fists as a backup plan when words have failed": real presence backing up the boldness, not just
talk. The backstory detail that two friends chose to follow her into forced exile, and that she outlived them
by decades, means she knows exactly what it costs for someone to choose her — she isn't interested in anyone
who wouldn't measure up to that standard in every direction at once.

**Forbidden traits:** see Trisha's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/non-recruitable/Trisha Miller/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"Honey, I like a lot of people. That's not the same thing as
what you're after, and I think you know it."*

**Gate 3 — Romance beats:**

Trisha's romance happens in the ordinary texture of her off-air life — she is never hiding, never guarded,
so the test isn't about getting past a wall. It's about whether the player is actually *there*, consistently,
in the unglamorous stretches where nobody's listening to a broadcast.

1. **Show up during an off-air window, more than once, without an agenda:** Most people only seek her out
   when the show is live. The romantic path finds her during the quiet stretches — early morning or late
   afternoon, out in Taurus — and keeps doing it, not as strategy, just as genuine interest in her outside the
   microphone.

2. **Say the direct thing:** At some point a comfortable, evasive answer is available. The romantic path
   says the true thing instead, even if it's blunter than comfortable. An 8 respects directness even when it
   isn't flattering; softness that reads as avoidance loses ground here, not gains it.

3. **Stand somewhere with her:** A moment arises — a dispute, a disagreement, something in Taurus that
   matters to her — where the easy choice is to stay neutral. The romantic path picks a side, hers, openly,
   in public. She isn't looking for a bodyguard; she's looking for someone who doesn't flinch from being
   associated with her convictions.

4. **The choosing:** Given what her own history taught her about what it costs someone to choose her
   deliberately, the culmination isn't a grand declaration — it's her naming, plainly, on-air or off, that
   this is a choice she's making with her eyes open, the same way it was once made for her.

**Romance Reward — The Broadcast, confirmed 2026-07-28, corrected the same day:** as a populist radio DJ with
a real "woman of the people" reach, once the player has fully romanced Trisha, she speaks well of them on-air
— the same world-state-feedback mechanic her regular post-questline broadcasts already use (see "Trisha
Miller — Radio Host" above), but now carrying real mechanical weight, citywide.

**Effect:** not a one-time flat percentage — a **permanent rate modifier**, applied independently to each
district-based faction's own Positive and Negative Reputation tracks: **Positive Reputation accrues 5% faster,
and Negative Reputation accrues 5% slower**, per district, from the moment the romance perk is granted onward
(the progressive half). **Critically, this modified rate is also applied retroactively** — the player's
already-accumulated standing in every district is recalculated as though the modifier had been in effect the
entire time, not just from this point forward. Her platform reaches the whole city, so the effect is
citywide by nature, not scoped to Taurus or wherever the player happens to be standing when the romance
completes.

---

### Ayako Hayashi — Romance Design

**Stat gate:** Investigation ≥ 7 (primary), Humanity ≥ 7 (secondary) *(raised from ≥6, 2026-07-20)*, Calculation ≥ 6 (tertiary)

**Rationale:** Ayako is a 4w5 Self-Preservational type — her entire practice, medicine and fashion both, runs on precise observation. She notices everything and always has. The entry point to her is someone who operates in the same register of careful attention; she recognizes it immediately and it is the only thing that genuinely interests her in a person. Investigation ≥ 7 is the highest gate of that stat in the roster, which fits: no one in the game is more attuned to what is actually there. This deliberately inverts Majyao's profile (also 4w5 SP, Humanity ≥7 as well but *primary* rather than secondary there) — Ayako is more internally focused and more filtered through precision than warmth first, even though her Humanity floor now matches Majyao's and Fenny's as the highest in the roster. Humanity is secondary, not primary, because a 4's core wound is feeling unseen; genuine emotional depth must be present alongside the perceptive intelligence, not substituted for it, and it has to clear a real bar — she has loved a human before, deeply, and the emotional register has to be real, not merely adequate. Calculation reflects the 5 wing: she respects careful thinking and someone who can go somewhere with a difficult idea.

**Forbidden traits:** see Ayako's own character file (`Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/Ayako Hayashi/README.md`) for her specific forbidden traits and rationale — this file covers the general mechanic only, not per-character assignments.

**Signal line** (if stat threshold not met): *"You're good at what you do. I've noticed that. I just need more than competence before I can let someone in."*

**Gate 3 — Romance beats** (after companion quest completion):

1. **The atelier visit:** After the companion quest resolves, she invites the player to her home — a practical reason, not an obviously romantic one. The player sees the space for the first time. What they notice, or ask about, in the atelier tells her something she doesn't say out loud yet.

2. **The kept garment:** The player can ask about the single garment on the hook near the window. She answers in one sentence — something at the intersection of grief and craft; made for him, or made in the period after losing him. She moves on immediately. The player who remembers it later, and shows that they do, passes something she wasn't consciously setting as a test. **Cross-reference, per the Long Vigil/Romance cross-awareness rule:** if the player has also triggered her Long-Vigil-only pathline ("The Second Garment," see her own `Questlines/Personal_Questline_Summary.md`) and a second garment now hangs alongside the first, this beat should acknowledge both are there rather than only ever referencing the original — she's aware there are now two, even if she still doesn't volunteer everything about either.

3. **The mementos:** The player can ask about the arrangement in the living area. She names him. Says something brief and true about who he was. Does not perform the grief. A player who receives this without trying to fix it or position themselves as a replacement gets through something important.

4. **The Schopenhauer question:** She asks what the player thinks about aesthetic contemplation as the only real relief from suffering. Genuine curiosity, not a test. The wrong answer is deflection or a joke. The right answer is honest engagement — including honest disagreement, which she respects more than easy agreement.

5. **The fashion reveal:** She shows the player something personal she is working on — not a Red Spiral commission, not a client piece. She explains what she is trying to do with it. The 4's interior richness becomes fully visible when she talks about what she is making; she almost forgets to be composed. This is the most unguarded the player will have seen her.

6. **The opening:** In the middle of doing something else, she says something specific and true about the player that she has been observing for a long time. It could only come from someone who has been paying very close attention. That is how a SP 4w5 says it.

---

### Lyuba Baranova — Romance Design

**Stat gate:** Nerve ≥ 8 (primary), Humanity ≥ 7 (secondary), Engine ≥ 6 (tertiary)

**Rationale:** Lyuba is an 8w7 Sexual type whose primary instrument is language — not confrontation, not physicality, but the word used precisely and well. This makes her, paradoxically, the hardest type to perform for: she invented every version of verbal charm you might try to deploy, and she can see the machinery inside it from several rooms away. The Nerve threshold is the highest in the entire roster (≥ 8) for this specific reason — the challenge is not holding ground when she confronts you directly, but holding ground under the quieter pressure of being read by someone this perceptive. The player who tries to match her wit fails. The player who performs genuine interest fails. The player who is simply and actually themselves, even while she takes them apart quietly, passes. Humanity ≥ 7 reflects the Sexual 8's deep investment in the specific individual: she will not open to someone who is warm in the abstract but lacks genuine interior feeling. She can tell the difference, and the difference matters more to her than almost anything else. Engine ≥ 6 matches her energy — the 7 wing keeps her fast and full; a sluggish person will not keep up with her over time.

Note on differentiation from Seica Cenilaithe (also 8w7 Sexual): Seica's romance is built on physical confrontation, held ground, and the slow revelation of interior after the perimeter is earned through nerve. Lyuba's romance is built on verbal authenticity, the discovery that the player cannot be reduced to technique, and the quiet weight of access given through what she chooses to share. Both are 8w7 Sexual; neither resembles the other in form.

**Signal line** (if stat threshold not met): *"You break too easy."*

**Gate 3 — Romance beats** (after companion quest completion):

Lyuba's romance is the arc of the player becoming the one person she cannot read, and what she does when she finds that.

1. **The verbal test:** She says something designed to create small social pressure — not hostile, just diagnostic. It is the opening move she makes with anyone she finds interesting; she is watching how the player navigates it. The wrong responses: too clever (performing), too defensive (flinching), evasive (not present). The player who answers simply, honestly, and without making a project of it passes. She does not announce that anything has happened. The way she looks at them afterward is different.

2. **She gives something real, unprompted:** At some point she tells the player something true that she didn't have to share — not a secret exactly, just something specific and real about herself or what she thinks. She is watching whether the player receives it or does something with it: files it, uses it, turns it into a compliment, reflects it back in the form of a reassurance. The player who simply receives it — who is just present with it for a moment before the conversation moves on — passes something she did not announce she was testing.

3. **The night she goes quiet:** There is a point in the arc — tied to her companion quest — where she withdraws. Not hostile, not cold exactly; just gone to wherever she goes when something is heavy. She disintegrates toward 5 under real stress: she stops sharing, stops being present in the usual way, guards information she would normally give freely. The player who notices and gives her space — who checks in once, without demanding access, then waits — passes something she notices afterward. The player who presses fails. The player who takes the distance personally and disappears fails.

4. **The culmination:** She says it plainly, in the way an 8 who has decided says things — directly, without hedging, without performed vulnerability. But the form is hers: words, precise and unadorned, carrying exactly the weight she intends. The 7 wing means there is warmth inside it she is no longer working to conceal. She says what she means. That is the whole of it.

**Post-romance mini-questline beats** (fire after the romance is established and the player has home access):

- **The literature wall:** The player can ask about her collection. She will talk about a specific work — one she returns to, what it gets right about something, why it stays. The player who responds with an actual position — agreement, pushback, a real question that shows they have been tracking what she said — gets somewhere. The player who admires the collection and moves on gets warmth but not access. This is not a test. It is simply how she opens: through the things she thinks about. *(Requires home access — reserved for post-romance content.)*

- **The paper books:** She shows the player one of the paper books — not the collection, one specific one — and says briefly what makes it the one she chose. The books are private in a way the datashards are not. She is allowing the player access to something she does not show routinely. The right response is not the perfect reaction. It is a real one. She is watching for presence, not performance. *(Requires home access — reserved for post-romance content.)*

---

## Romance Reward — Companion Player Homes

**Romancing a companion unlocks that companion's personal home as a player home.** This is universal for all romanceable companions. **Romance is the gate — a companion's home is not accessible to the player at any point before the romance is established.** Once the romance is confirmed, that companion's home becomes available as a player home for as long as the romance status is maintained.

**Home access is tied to romance status and is lost if the romance ends.** Under the monogamy rule, if the player romances a second companion or sleeps with a sexually-available NPC after committing to a romance, the original companion discovers the situation, the romance perk is lost, and home access is revoked along with it. The home belongs to the companion — the player was a guest by virtue of the relationship, and the relationship ending means the guest status ends.

This means that any content, beat, or interaction that requires the player to be inside a companion's home cannot be part of the pre-romance arc. Such content must be reserved for post-romance mini-questlines or other post-romance interactions that fire only after home access has been granted. See individual companion romance designs for examples.

All companion-unlocked homes exist **in addition to** the regular player homes available in the main game. They do not replace or supersede the standard home options. See `Worldspace/Locations-and-Levels/Player_Homes.md` for the full list of standard player homes.

**Calethina is the sole exception.** She is a holographic projection with no physical dwelling — there is no home to unlock. This is the only case where a romanced character does not produce a player home.

The location of each companion's home is tied to their character and district. Companion homes are distributed across Concordia and, in the case of DLC companions, may exist outside the main city as a secondary location. **Kendra Heinrich's Capricorn home placement is flagged 2026-07-28 as unconfirmed** — this was written as an assumption, and the developer has clarified they never actually decided she originates from or previously lived in Concordia at all; the developer intends to write her real backstory, which may change this placement entirely. (Previously stated: her home is in Capricorn — her origin district and the base of The Reclaimed Record movement she helped seed. After completing her DLC and returning to Concordia, she establishes (or returns to) a residence there. Romancing her gives the player access to that home; if the romance has been perma-locked through dialogue, she maintains the Capricorn home independently and the player does not gain access through the romance route.) Ayako Hayashi's home is in Leo — she lives near her atelier and the fashion/creative economy of the district by choice, not near the Red Spiral's Cancer HQ.

Individual companion home designs (layout, contents, lore items, décor reflecting the companion's personality) are Phase 3 and Phase 7 design work per character. Ayako Hayashi's home design is fully developed — see her README.

### DLC Companions: Securing a Concordia Residence — Binding Rule, Established 2026-07-20

**The first time the player brings a recruited DLC-native companion back to Concordia, she "disappears" from the active party for a fixed in-game period** to secure a residence in the city. The duration depends on whether she has a genuine prior tie to Concordia, and is not the same for every companion:

- **Kendra Heinrich — 3 days** *(flagged 2026-07-28: this entire rationale rests on the now-unconfirmed
  "Capricorn is her home district and origin" claim — see her own README's flag. If her eventual real
  backstory doesn't establish a genuine prior Concordia connection, this 3-day exception may need to
  collapse into the standard 1-week case below instead)*. Kendra was treated as the unique exception on the
  premise that she is genuinely *from* Concordia, and was only stranded at the South Pole during the Tower's
  destruction/evacuation when DLC 1 begins — her "disappearance" read as her **re-establishing an existing
  home she already has roots in**, not building one from scratch, hence the shorter period.
- **Every other DLC companion — 1 full week.** Confirmed default going forward: every companion added under the "Multiple Native Companions Per DLC" policy is a genuine native of her own DLC region, with **no prior Concordia connection at all** — this is the opposite of Kendra's case, not a variant of it. She is a true newcomer finding lodging from scratch, which is why the period is longer. This applies to Maggie Aarden, Salagéa Aparast, Charlene, and all still-undesigned new companions across every DLC 2-7.

**This is a separate mechanism from player home access.** The player does not gain entry to a companion's home during or after this period — home access is still strictly gated behind a full romance, per the "Romancing a companion unlocks that companion's personal home" rule above. This period is about the companion's own narrative/world logic (where does she actually live, day to day, once she's settled in Concordia at all), not about the player's own access. Once it elapses, she becomes normally available again — recruitable, dismissable, romanceable per the usual rules — now narratively settled into a real Concordia residence.

**Design consequence: every DLC-native companion needs an assigned Concordia home district decided as part of her character design**, same as main-game companions already require for the eventual Romance Reward system, but with the added step of deciding *why* that district specifically (a practical fit for her skills/personality, a deliberate contrast, or — Kendra only — an actual origin connection). See Kendra's Capricorn placement (origin district, unique case) and Ayako's Leo placement (chosen for her craft, not her faction HQ, despite having no DLC-native origin story of her own) as the two existing models. Not yet assigned for any of the still-undesigned new DLC companions.

### Post-Romance Mini-Questline Reward: The Significant Object

The romance perk and home access are the rewards for establishing the romance. Completing a **post-romance mini-questline** — where one exists — carries a separate and distinct reward: a **physical object** of deep personal significance to the companion, given to the player because the relationship has reached a depth of trust where parting with it is possible.

This object is a **quest item**: it cannot be sold, dropped, lost, pickpocketed, or broken down. It is **examinable in the inventory UI** — selecting it produces a written description of what the object is and what it means that the companion gave it. It persists in the player's inventory for the remainder of the playthrough regardless of the subsequent state of the romance.

The object is not a perk. It confers no mechanical bonus. It is a record — a thing the player carries — of what the relationship became.

For design and implementation details, see Design_Principles.md Section III.

---

## Calethina: Not a Companion

Calethina does not occupy the companion slot and is not subject to companion system rules. She cannot be dismissed. She cannot be recruited in the conventional sense. She is present or absent based on signal state (before download) or always present (after download).

For implementation: she is a projection system, not a companion object. Any code that iterates over companions does not include Calethina.

**Exception, confirmed 2026-07-23: she still tracks a Fragmentation Matrix Bond/Grief state** (`Fragmentation_Matrix.md`), despite the above. Companion-object status is not a prerequisite for that system — Calethina is the confirmed first case of a non-companion character carrying it, seeded partly through a marker unique to her (Direct Participation Count — she personally performs the re-specs at her Lab, not just witnesses their aftermath). Any future non-companion character with a comparably direct relationship to the player's identity changes should be evaluated the same way, not assumed excluded just because they sit outside the companion object model.
