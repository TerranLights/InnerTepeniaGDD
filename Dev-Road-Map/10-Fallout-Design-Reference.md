# Fallout Design Reference

*A synthesis of design analysis from Fallout 1, Fallout 2, and Fallout: New Vegas, compiled for Inner Tepenia GDD use.*

*Methodology: Full research passes against Fallout 1/2 walkthrough documentation, NV wiki, developer interviews (Josh Sawyer GDC 2012, subsequent statements), design analysis literature, and community-verified mechanical documentation. This document distills findings into actionable guidance for specific GDD systems.*

---

## How to Use This Document

When designing a specific GDD system, find the relevant section here. Each section has three parts:

- **What Fallout does** — the specific design as implemented
- **What Inner Tepenia should adopt** — direct recommendations
- **What Inner Tepenia should adapt or reject** — departures from the Fallout model with reasons

The Fallout Precedence Law is in effect throughout: when Fallout 1/2 and New Vegas conflict, **New Vegas wins**. Where both agree, treat that agreement as especially strong signal.

---

## Section 1: Quest Structure

### What Fallout does

**Fallout 1/2:** Quests are built around multi-path resolution with consequential commitment. Multiple completion vectors (combat, speech, stealth, skill-based) for the same objective are standard. Skill checks are distributed throughout dialogue trees rather than concentrated at a single gate — a player who fails the Speech option finds a different path through Agility, Strength, or Luck. The game treats failed checks as redirections, not dead ends.

The signature F1/2 structural move is the **Junktown pattern**: the surface-reading-correct choice produces a worse outcome than the ambiguous one. Killian Darkwater (the lawman) produces a "horrible town" in the ending slides; Gizmo (the criminal) produces a "successful trading post." The game does not editorialize. The ending slides deliver the verdict after the fact. Related: the **Gecko/Vault City pattern** (F2), in which genuine resolution is structurally impossible — both communities have legitimate grievances, the political system makes mutual benefit unachievable, and every path has real costs.

F1's final boss is the fullest expression of this design: The Master can be defeated through combat, but also by confronting him with evidence (requires INT 6+ to obtain) or very high Speech. Upon losing the intellectual argument, he destroys himself. A villain whose defeat is achieved through argumentation, and who, losing the argument, chooses to end his own plan.

**Fallout NV:** The "Seven Solutions" pattern. "Beyond the Beef" has seven distinct paths to the same narrative endpoint. The average FNV quest has 2-4 paths. The pattern: one combat path, one speech path, one skill/SPECIAL path, and sometimes a faction reputation path that bypasses steps entirely.

FNV introduces **shared-objective interlocking**: the four faction quest lines share many objectives (deal with the Boomers, the Omertas, the Great Khans) but route the player through them with different motivations, NPCs, and success criteria. Completing a shared objective via side quest before the faction quest is issued is supported — the quest engine detects and skips the completed stage.

The key decision point is placed **late** in the quest, after the player understands the stakes. Early branches recombine before this point. Consequences diverge at the decision point.

### What Inner Tepenia should adopt

**From F1/2:**
- The Junktown pattern as a recurring structural move. Not every quest — but most major district quests should have at least one resolution path where the "obvious correct" choice produces a messier outcome than the ambiguous one. The player who investigates before acting gets better outcomes; the player who acts on surface readings gets technically successful but costly results.
- The Gecko/Vault City pattern for the main conflict and at least one major side questline. At minimum one questline per Act should have no clean resolution — both positions are legitimate, the political structure prevents mutual benefit, every path costs something real.
- Distributed skill checks throughout dialogue. Never concentrate a quest's single non-combat path at one Speech gate.
- At least one major antagonist who can be argued out of their plan through evidence and reasoning. The Master pattern. This character should have a coherent internal logic that the player can engage intellectually, not just overcome physically.

**From FNV:**
- The quest anatomy: acquisition method → investigation/travel → skill-check distribution → key decision point (late, after stakes are clear) → outcome with world-state flags.
- Shared-objective interlocking for the faction quest lines. The district quests already have this via the Consequence Web. Apply the same principle to the faction questlines: shared objectives across multiple factions, resolvable by any of them, with faction-specific framing and consequences.
- Targeting 3+ solution paths for all major quests. 5+ for the most important quests (major stabilization path quests, Calethina questline beats, Planetary Split Brain).
- Quest state flags that track everything, including small choices, for the ending slides.

### What Inner Tepenia should adapt or reject

- FNV has point-of-no-return issues (players accidentally lock themselves out without clear warning). Inner Tepenia's GDD should specify explicit point-of-no-return notifications in quest design — not necessarily a warning screen, but at minimum NPC dialogue that signals "this is the last chance to turn back."
- F2's fourth-wall-breaking humor (Monty Python references, the game acknowledging its own save system). Avoid this entirely. It undercuts the emotional weight that makes F1's design distinctive.

---

## Section 2: Stat and Skill System

### What Fallout does

**F1/2 SPECIAL:** Seven attributes (1-10). At character creation: two optional **traits** (both double-edged — always a bonus paired with a penalty) and three **tagged skills** (20% bonus, double improvement rate). The trait system defines character identity through what you give up, not just what you gain. Gifted (+1 to all SPECIAL, −10% to all skills, fewer skill points) is the purest expression: everything comes at cost.

**Low Intelligence is a full alternative playthrough mode.** INT below 4 produces broken speech, unique NPC reactions, closed quest paths, and opened interactions unavailable to normal-INT characters. This is not a punishment — it is an identity. The game treats cognitive limitation as a legitimate character type.

**Perks** (every 3-4 levels) are rare enough to feel like identity statements. Sniper changes the critical hit calculation architecture. Fast Metabolism is a build commitment, not a small bonus. Rarity makes each one matter.

**FNV skill system:** 13 skills, threshold-based checks (not probability). If your skill meets the threshold, you succeed. If not, you fail — visibly (displayed in red in dialogue). Failed checks are presented, not hidden; the player sees what they're missing. This makes character build decisions feel consequential: you know exactly what your build cannot access.

Skill magazines provide temporary +10 boosts, serving as a resource-management bypass valve — a player who didn't invest in Medicine can pass Medicine 50 if they stock the right item. This prevents permanent single-playthrough content locks without eliminating the felt cost of a low skill.

**Intelligence is the most mechanically impactful SPECIAL stat** in FNV (increases skill points per level, creating a multiplier effect across the whole playthrough). Charisma is the weakest (only governs Speech and Barter, which are accessible via other routes).

### What Inner Tepenia should adopt

**From F1/2:**
- The trait system at character creation. Inner Tepenia's 10 traits are already designed and this principle is preserved. The design standard for each trait: every trait must have a real penalty. If removing the downside would still leave a trait most builds would take, the downside isn't strong enough.
- Low-MACHINE alternative content. Inner Tepenia's MACHINE stats should have at least one "low-stat alternative mode" — likely low Humanity or low Calculation — that produces distinct dialogue and encounter responses rather than just fewer options. This is one of F1/2's most distinctive design features and Inner Tepenia should honor it.
- Perks that are identity statements. Even at FNV density (Inner Tepenia's 160 level-up perks over 64 levels), individual perks should be specific enough that two different builds would make meaningfully different use of the same perk. Flat stat bonuses are filler. Behavioral change perks are design.

**From FNV:**
- The threshold model (score-based, not probability-based). Inner Tepenia's skill checks should be deterministic: meet the threshold, succeed. This is already implied by the design of the MACHINE stat system; confirm it explicitly in the core mechanics documentation.
- Visible failed checks in dialogue. Show unavailable options with some visual distinction (a different color, an icon, a greyed state). The player should be able to see what they're missing without being able to easily access it.
- The magazine bypass valve. Some form of consumable temporary skill boost prevents single-playthrough content locks while preserving the felt cost of a low skill.

### What Inner Tepenia should adapt or reject

- FNV's Charisma weakness (only governs Speech and Barter, creating a social-character archetype that isn't mechanically distinct from a high-Intelligence build that invested in Speech). Inner Tepenia's Humanity stat risks the same problem if its primary function is social dialogue checks. Humanity should have effects that Intelligence cannot substitute for — specifically in the robot experience domain. Emotional intelligence, the quality of bond, the ability to understand robot grief — these should be Humanity-gated in ways that no amount of Calculation compensates for.
- F1/2's INT-below-3 alternative dialogue is one of the great design achievements in CRPG history, but the specific implementation (robots speaking in broken half-sentences) would have a different valence in Inner Tepenia. The equivalent might be a very low Humanity build — Dolls who have suppressed or lost significant emotional range — producing a distinctly different register of interaction. The specific form this takes is a design decision, but the principle is worth preserving.

---

## Section 3: Companion Design

### What Fallout does

**F1/2 companions:** Minimal explicit characterization; almost everything emerges from mechanics and player projection. Ian (F1) is the archetype — a pragmatic caravan guard remembered primarily for his friendly fire liability (burst weapons don't check for allies in the cone). Cassidy (F2) has a heart condition that creates real party composition decisions. Myron (F2) is the deliberate anti-companion: useless in combat, enormously self-important, his ending is a precisely aimed editorial about vanity and legacy (killed by a random raider, his name forgotten, his creation — Jet addiction — outliving him). These companions are memorable because of mechanical liabilities and pointed design choices, not rich written characterization.

**FNV companions:** The opposite approach — richly characterized, with explicit personal quest arcs. Boone's quest confronts his guilt over the Bitter Springs massacre; Veronica's quest asks whether the Brotherhood's isolationism can be changed (the "good" outcome is blocked by faction dynamics — a deliberately tragic structure); Arcade's quest interlocks directly with the main quest's endgame. Lily's companion design is a continuous mechanical choice rather than a discrete quest: medication dosage throughout the playthrough affects her behavior, her combat utility, and her ending.

**FNV trigger systems:** Boone and Arcade accumulate "history points" from specific world actions in their presence. Veronica's quest triggers from 3 out of 9 possible Brotherhood-adjacent dialogue moments. These systems are invisible — no UI progress bar — which means players who don't explore will miss significant companion content.

### What Inner Tepenia should adopt

**From F1/2:**
- Companion mechanical liabilities. At least one companion should have a flaw that generates emergent stories — not a personality flaw (which is just characterization) but a mechanical one: a combat tendency that creates risk, a health condition that affects party decisions, a specific situational uselessness. This makes companions feel real in a way that voiced dialogue alone doesn't.
- The deliberate anti-companion. At least one recruitable NPC in Inner Tepenia should be designed in the spirit of Myron: a character whose presence is arguably not worth it, whose ending is a pointed editorial about their character, and whose failure is the point rather than a design gap.

**From FNV (these are already largely in the design; verify each is honored):**
- Personal quest arcs for all main companions that resolve a character question, not a plot question. The destination is always: what does this companion understand about themselves by the end? Equipment rewards are secondary.
- The history point trigger system (invisible accumulation) over the explicit "bring companion to location X" trigger where possible. The invisible trigger rewards players who engage organically with the world; the explicit location trigger can feel like a mechanical checklist.
- Unique ending slides for each companion with real variation based on quest outcome.
- Companion passive perks that are thematically connected to the companion's identity.

**Inner Tepenia-specific extension:**
- The robot companion experience is a direct expression of the first guiding principle. Companion Dolls should have at least some content that specifically engages with what it is like to be them — not exposition about robot rights, but specific, phenomenological detail about their experience of memory, time, love, and existence that has no human equivalent. This is the territory where Inner Tepenia goes further than either F1/2 or FNV.

### What Inner Tepenia should adapt or reject

- FNV's companion trigger system is "invisible to the player" by design, but this caused significant content to be missed. Inner Tepenia should use invisible history-point systems but pair them with ambient cues — NPC commentary, world reactions — that signal to the attentive player that something is accumulating. Not a progress bar, but detectable signal.

---

## Section 4: Faction System

### What Fallout does

**F1/2:** Faction affiliations are loosely systematized. Multiple factions can be worked simultaneously; they don't always know about each other's relationships with the player. Ideology is implicit rather than explicitly labeled. The "correct" ideological reading of each faction is left to the player. The Killian/Gizmo dynamic (criminal produces better outcome than lawman) is the faction design philosophy in miniature: factional moral authority is not reliable.

**FNV:** The reputation model uses **two separate, permanent tracks per faction: Fame and Infamy.** These do not cancel; they accumulate independently and combine into a composite title. High scores on both tracks simultaneously produce "mixed" titles (Merciful Thug, Soft-Hearted Devil). Neither track can be reduced — only offset by accumulating more of the other type.

Faction tier structure: Major Powers (determine main quest ending), Regional Factions (sub-objectives of the main quest), Settlements (community standing). Each tier has different behavioral effects at reputation thresholds.

Sawyer's design principle: **factions feel real because members disagree internally.** NCR soldiers question the Republic's expansionism. Legion members vary in ideological commitment. This requires NPC-level diversity within each faction — individual characters who hold minority views.

### What Inner Tepenia should adopt

**From FNV (this is already in the architecture; verify it holds through Phase 2):**
- Separate Fame/Infamy tracks. Inner Tepenia's reputation architecture document already specifies this. The key design enforcement: Fame and Infamy should never cancel. A player who massacres Cancer district and then spends a month doing care work does not get a clean slate. The district is confused, not forgiving.
- Internal faction dissenter NPCs. Every faction designed in Phase 2 should include at least one named character who challenges the faction's orthodoxy from within. This character is often the most interesting NPC in the faction — they hold the tension of belonging to something they also critique.
- Three-tier faction hierarchy (applied to Inner Tepenia context): Eyes of Gold and the other major faction(s) function as Major Powers; the nine developed factions function as Regional Factions; the minor groups (Quiet Shift, Treaty Scholars, Last Builders) function as Settlement-level groups.

**From F1/2:**
- The principle that faction moral authority is not reliable. The faction the player "should" support often produces the messier outcome. At least one major faction in Inner Tepenia should follow this pattern — the faction that presents as legitimate, established, or morally coherent produces an ending that reveals a cost the player didn't anticipate.
- Factions that can be worked simultaneously without automatic mutual awareness. This creates emergent moral complexity that a more rigid "choose your faction" system forecloses.

**Inner Tepenia-specific extension:**
- The Unity of Opposites principle as faction design constraint. Each faction must need something that only their ideological opposition can provide. This is stronger than the Fallout model's "factions have internal dissent" — it requires that the faction system be genuinely interlocked rather than just diverse.

### What Inner Tepenia should adapt or reject

- FNV's disguise system (wearing faction armor overrides reputation checks) was "very time consuming and buggy as hell" by Sawyer's own account. If Inner Tepenia implements any equivalent disguise/infiltration mechanic, it needs explicit design rules about what it covers and what it doesn't. The intent is good; the implementation risk is high.
- FNV's faction system is more legible and intentional than F1/2's. This is mostly an improvement — but the cost is reduced emergence. Inner Tepenia should aim for FNV's intentionality while preserving some of F1/2's "factions don't always know about each other" messiness for situations where that messiness produces interesting play.

---

## Section 5: Time Pressure and Pacing

### What Fallout does

**F1 — the Water Chip timer:** A primary-quest timer (150 days, extendable to 250) creates real urgency in exploration. Every side quest is weighed against the primary mission — the timer creates **cost-of-mercy**: each decision to help someone is also a decision to accept risk. Tim Cain originally wanted to remove it; Black Isle kept it. In retrospect, the Water Chip timer works. It creates stakes escalation and makes the world feel in motion without the player.

The timer is generous: players who know where they're going feel no pressure. Players deciding whether to take on side content feel the weight. It punishes inefficiency, not specific build choices.

**F2 — no timer:** The engine technically has a 13-year cap (effectively infinite). The result: the main quest doesn't feel time-pressured. This makes the world easier to explore but softens emotional investment in the main threat. F2 compensates with volume of content; the sense of a world in danger is softer.

**FNV — enemy level gating:** No explicit timer. Soft gating through hostile territory (high-level deathclaws on the direct Vegas route) encourages following the intended Act I path without forcing it. Reputation gating and quest state gating handle most pacing after Act I. The point of no return is poorly communicated — a known design weakness.

### What Inner Tepenia should adopt

The Water Chip model. A primary-quest timer attached to the central survival threat gives structure without eliminating exploration. The timer should be:
- Generous enough that focused players feel no pressure
- Real enough that players deciding whether to take on extended side content feel the weight
- Framed as cost-of-mercy rather than punishment — the player is choosing to spend time, not failing to run fast enough
- Extendable by specific main quest actions (the Watershed equivalent)

Apply FNV's enemy-level soft gating to discourage skipping acts entirely (players who try to access Act 3 content at Act 1 level should encounter natural resistance, not a locked door).

Improve on FNV's point-of-no-return communication: the most consequential faction commitment moments should have dialogue that signals "this changes things" without requiring a warning pop-up.

### What Inner Tepenia should adapt or reject

- F2's no-timer approach produces a more relaxed experience but softer stakes. Inner Tepenia's survival premise (the district energy crisis) is inherently time-sensitive — removing time pressure from it would undercut the premise. Keep the timer.
- F1's second timer (super mutant invasion) was the mistake, not the Water Chip timer. A single primary-quest timer is the correct model. Multiple timers running simultaneously create anxiety rather than urgency.

---

## Section 6: Moral Framework and Tone

### What Fallout does

**F1 — bleak humanism:** The world is broken; people are surviving through compromises and cruelties; the protagonist is the best hope available, which is not saying much. Humor is dark and self-deprecating, never breaking the fiction. The design team's stated philosophy: "hit the player with an emotional sledgehammer as often as possible." This is not gratuitous — emotional consequence is the primary player feedback mechanism.

F1's ending: the Vault Dweller defeats the Master, destroys the mutant army, saves the wasteland — and is exiled by the Overseer, who cannot let a hero return without inspiring others to leave. "You saved us, but you'll kill us." No celebration. The protagonist wins and loses simultaneously. The exile is canonical and is what gives F1 its emotional weight.

**F2 — tonal drift:** Pop culture references, fourth-wall breaks, self-aware humor. This is the major tonal weakness of F2 — it undercuts the emotional weight that made F1 distinctive. When the game winks at the player, the stakes feel lighter.

**FNV — balanced bittersweet:** Maintains the bittersweet moral register. The Courier can achieve more unambiguously good outcomes than the Vault Dweller, but the overall ethical landscape remains consequentialist and unresolved. FNV's major improvement: the ideological factions give moral choices more explicit philosophical scaffolding — there are more ideas in debate than in F1/F2.

**Consistent across all three:**
- No clean endings, only better-or-worse states
- Antagonists have coherent internal logic (the Master's plan emerges from a coherent if monstrous reading of the world's problems; Caesar's Legion is a functioning civilization with a theory of history)
- The world does not reward heroism (exile, continued poverty and struggle, the survival of Jet addiction after Myron's death)
- No explicit moral commentary — consequences speak, the game does not judge

### What Inner Tepenia should adopt

- F1's bleak humanism tone specifically. Not F2's satirical register. Not FNV's slightly more optimistic range.
- The exile ending structure at the macro level: the protagonist wins the immediate conflict and loses something essential in the canonical good ending. This loss is presented without editorializing.
- Antagonists with coherent internal logic. At least one major antagonist should be a genuine intellectual opponent — someone the player can argue with, potentially talk down, and who, upon losing the argument, makes a choice that reflects their internal consistency even in defeat.
- No moral commentary from the game. The ending slides deliver the verdict; the game does not judge. NPC reactions can carry moral weight; no UI element, loading screen quote, or narrator voice should editorialize.
- Epilogue slides remember everything, including small choices. The game should behave as if the player's entire engagement mattered. This is FNV's explicit design philosophy ("vibes-based curation" of slides — developers asked "what would be interesting if the player did this?" and included slides for it). Apply this standard to Inner Tepenia's ending design.

### What Inner Tepenia should adapt or reject

- F2's fourth-wall-break humor is explicitly not canonical for Inner Tepenia. The guiding principles (the robot experience, the nature of love between robots and humans) require the fiction to be taken seriously. Any joke that winks at the player about it being a game undercuts the project.
- FNV's "slightly more optimistic range" — the Courier can achieve more unambiguous wins than the Vault Dweller. Inner Tepenia's bittersweet-only commitment is stronger than FNV's; don't let FNV's design nudge the endings toward clean resolution.

---

## Section 7: Town and Hub Design

### What Fallout does

Every major F1/F2 hub follows the same structural template: **faction-divided space with interlocking quest chains.** Towns are not settings — they're political environments where multiple power groups coexist in tension, and player actions tip the balance.

The five-element anatomy of a well-designed F1/F2 hub:
1. A visible power structure and a hidden or competing one
2. At least one quest whose surface reading is misleading or incomplete
3. Interlocking quest chains (actions for one faction affect standing with another)
4. Distinct ending states visible in epilogue slides
5. NPCs who are witnesses to and participants in local politics, not just quest-givers

Hubs are geopolitically interdependent — the Hub's caravan system connects to other locations, Vault City's conflict with Gecko has geopolitical consequences, New Reno's families are entangled with Redding and NCR. Towns form a web of interdependencies.

**FNV's contribution:** The major-vs-minor location distinction. Major locations have 3-6 associated quests, multiple named NPCs, and ending slides. Minor locations have environmental storytelling — a self-contained scene readable without dialogue — and unique loot. The density of unmarked locations is what makes the Mojave feel full rather than empty.

"The setting and the story are influenced by each other but neither dictates the other." Locations feel like they predate the narrative and would exist without it.

### What Inner Tepenia should adopt

The five-element hub anatomy applies to Concordia's districts — each district is a major location by FNV's definition. This is already substantially true from the district design work. Verify each district against the five elements: does Cancer have a visible power structure and a competing one? (Yes — the Unlimited vs. the Triage Realists vs. the Surveillance faction.) Does it have a quest with a misleading surface reading? Does it have interlocking quest chains? This audit is Phase 5 work.

The major/minor location distinction for intra-district spaces: individual buildings, workshops, apartments, and sub-locations within a district are "minor locations" in FNV terms. They should have environmental storytelling (something readable from the scene without dialogue) and may have unique items. The test: could a player learn something specific and true about this place without talking to anyone?

Geopolitical interdependency between districts is already handled by the Consequence Web system. Apply the same logic to the new faction questlines: faction actions in one district should visibly affect situations in another.

---

## Section 8: Dialogue System

### What Fallout does

**FNV threshold model:** If skill meets threshold, check succeeds. No dice roll. Failed checks are shown in red — the player can still select them; the NPC responds to the weak argument with dismissal or skepticism. This preserves immersion while communicating the check's outcome clearly.

**Threshold distribution:** Dense at 25-50 (widely accessible), moderate at 50-75 (build-specific), sparse at 75-100 (build-defining). The highest checks unlock the most advantageous or unusual content, rewarding specialization.

**Dialogue options per beat:** 3-6. Below 3 feels railroaded; above 6 creates decision fatigue. 4-5 is the functional sweet spot for most beats.

**Companion dialogue:** Triggered by location proximity and event exposure, not an approval meter. Companions have no UI progress bar — players who don't explore will miss companion commentary. The system is invisible but real.

**Skill magazines:** +10 temporary boost, allowing bypass of checks up to ~10 points above current skill level. Resource-management bypass valve.

### What Inner Tepenia should adopt

- The threshold model (deterministic, not probabilistic). Already implied; confirm explicitly in the dialogue design spec.
- Visible failed checks with distinct visual treatment. The player should see what they're missing without being able to easily access it.
- The 3-6 option range per dialogue beat.
- Threshold distribution curve: dense at low thresholds, sparse at high. The highest MACHINE stat checks (80+) should unlock the most unusual content — the kind of interaction that could only exist with a deeply specialized character.
- Companion commentary as invisible accumulation triggered by world events and locations. Pair with ambient cues that signal to attentive players that something is building.
- A consumable bypass valve for skill thresholds.

---

## Section 9: Endings and Epilogue

### What Fallout does

**F1/2:** Slideshow narrated by Ron Perlman ("War. War never changes."). Slide selection based on world-state flags. The slides cover: major quest outcomes, faction states, individual NPC fates. The best slides are editorial — they deliver a verdict on the player's choices through specific downstream consequences, not through moral commentary during the game.

F1's exile ending is the structural template: canonical good ending = win the conflict + lose something essential. The protagonist's success produces their expulsion from the community they protected.

**FNV:** The same slideshow model, more comprehensive. Sawyer's design principle: "vibes-based curation" — include slides for things developers find interesting, not just for major quests. The NCR Misfits got ending slides because someone asked "what happens if the player gives these incompetent soldiers Psycho?" This rewards curious, experimental engagement with the world.

FNV's known design gap: the Courier's personal ending depicts them as celebrated by but subordinate to the chosen faction. The protagonist's own arc — their personal ambitions, their identity — is not fully reflected. The Courier becomes a celebrated instrument, not an architect.

### What Inner Tepenia should adopt

- The slideshow model is already planned. Confirm the "vibes-based curation" philosophy: include ending slides for unexpected or unusual player choices, not just for quest completion flags. Inner Tepenia should remember more than FNV, not less.
- The exile structure as the template for the canonical good ending. The protagonist Doll wins the central conflict and loses something essential — not as a punishment but as the canonical bittersweet outcome.
- Correct FNV's personal ending gap: the protagonist Doll's personal arc should have a dedicated set of ending slides that reflect their specific journey — not which faction they backed, but who they became and what they chose about themselves. This is a direct expression of the first guiding principle.
- Companion ending slides with real variation based on questline outcome.

---

## Consolidated Design Laws

Synthesized from both research passes. These are repeatable principles with the strongest cross-game evidence:

**1. Multiple paths, one destination.** The narrative destination is fixed; the method and path are open. This allows radical player agency without requiring entirely different narratives per choice.

**2. Distribute skill checks; never gate a single path behind a single check.** A player who fails one check finds a different route to the same destination.

**3. Surface readings are unreliable.** The obviously-correct choice should have hidden costs. The ambiguous choice should have hidden goods. Players who investigate before acting get better outcomes; players who trust appearances get technically successful but messier results.

**4. Consequences speak; the game does not judge.** Moral weight is delivered through downstream consequences and ending slides. The game never tells the player their choice was wrong.

**5. Every antagonist has a theory.** Antagonists should have coherent internal logic — their position should be engage-able, even when their methods are monstrous. At least one should be arguable out of their plan.

**6. Separate tracks for conflicting states.** Fame and Infamy don't cancel. Track the positive and negative history of a relationship separately rather than resolving them to a single score.

**7. Factions feel real because members disagree.** Every faction needs internal dissenter NPCs — characters who belong to the faction while challenging its orthodoxy.

**8. Companions resolve character questions, not plot questions.** The companion quest's destination is always what the companion understands about themselves by the end. Equipment rewards are secondary.

**9. Mechanical liabilities make companions memorable.** A companion with a flaw that generates emergent stories (friendly fire, health conditions, specific uselessness) is more memorable than a companion who is simply well-characterized.

**10. The ending remembers everything.** Include slides for unexpected or unusual player choices, not just for main quest completion. The game should behave as if every engagement mattered.

**11. The canonical good ending is bittersweet.** The protagonist wins the immediate conflict and loses something essential. This loss is presented without editorializing.

**12. The world existed before the player and would continue without them.** Every major location has an ongoing situation the player enters, not a staged scenario set up for their arrival.

**13. Friction is meaning.** Failed skill checks, locked content, and consequence asymmetry are the mechanisms by which choices acquire weight. They are not obstacles to be removed.
