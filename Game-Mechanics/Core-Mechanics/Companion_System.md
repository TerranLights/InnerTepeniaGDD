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

**Gate ordering — confirmed:** Gate 1 always comes before Gate 2. The companion quest completes first; the MACHINE stat check fires second, at the first organic moment where the character would naturally move toward romance. If the build meets the threshold, the romance beat sequence begins. If it does not, the signal line fires and the door closes. The stat check is never presented as a hard wall before the relationship develops — it fires inside the relationship, in the character's own voice, at the natural inflection point. On a replay with an eligible build, the player who heard the signal line already knows what to work toward.

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

### Sexuality by Character Type — Canon Rule

**Robot characters (companions and sexually-available NPCs):** Bisexual by default. Robots in Concordia do not organize attraction by the gender of their partner. All confirmed romance companions are robots; all are bisexual. This means they will pursue the player regardless of the player character's gender.

**Human characters (companions and sexually-available NPCs):** Heterosexual. Human characters have a fixed-gender attraction. Any human companion or sexually-available NPC will only pursue a player character of the opposite gender presentation.

This rule applies uniformly across both the romance roster and the casual "fuckable" pool. No exceptions are established at this time.

---

### Thematic Note

The romance system is a direct expression of the second guiding principle — the nature of love between robots and humans. Every romance in the game, regardless of the species of the characters involved, is asking: what does this specific person find in this specific other person, and what does that mean for both of them? The stat/trait gate ensures that the answer is always grounded in who the player character actually is, not in what they've done or what perks they've accumulated.

---

### Confirmed Romanceable Characters

The following characters are confirmed romanceable. Thresholds are documented here as they are designed; entries marked TBD are pending Phase 3 personality work.

| Character | Type | Stat Thresholds | Trait Gates | Notes |
|-----------|------|-----------------|-------------|-------|
| Calethina | Projection system (not a companion) | Calc ≥ 8, Humanity ≥ 6, Nerve ≥ 6, Engine ≥ 6 | TBD | See full design note below; romance post-download via mini-quest |
| IT-068 [Flora] | Recruitable companion | Nerve ≥ 7, Calculation ≥ 6, Engine ≥ 5 | TBD | First companion; 6w5 Thinking; see full romance design note below |
| Favi della Torre | Recruitable companion | Nerve ≥ 7, Humanity ≥ 6, Engine ≥ 6 | TBD | 6w5 Self-Pres; loyalty proven through protective choices; see full design note below |
| Villena Hiresvett | Recruitable companion | Agility ≥ 6, Humanity ≥ 6, Nerve ≥ 5 | TBD | 7w6 Self-Pres; presence and genuine engagement; see full design note below |
| Naizelle d'Edjordoś | Recruitable companion | Calculation ≥ 7, Investigation ≥ 6, Engine ≥ 5 | TBD | 5w6 Self-Pres; most patient romance in the game; see full design note below |
| Seica Cenilaithe | Recruitable companion | Nerve ≥ 7, Might ≥ 6, Humanity ≥ 6 (possibly 7 — TBD) | TBD | 8w7 Sexual; see full romance design note below |
| Ji-Eun Kim | Recruitable companion | Calculation ≥ 8, Investigation ≥ 6, Humanity ≥ 6 | TBD | 5w4 Social; in hiding; undelivered letter is a separate gate outside romance arc; see full design note below |
| Vosora Lashár Tanslock | Recruitable companion | Calculation ≥ 7, Investigation ≥ 6, Nerve ≥ 6 | TBD | 5w6 Social; romance happens within the investigation; see full design note below |
| Michelle Stanton | Recruitable companion | Calculation ≥ 7, Humanity ≥ 6, Engine ≥ 7 | TBD | 5w6 Social; built the Arcanet; chose to stay; romance through shared commitment; see full design note below |
| IT-021 [Fenny] | Recruitable companion | Humanity ≥ 7, Engine ≥ 6, Nerve ≥ 5 | TBD | 6w5 Self-Pres; quietest romance in the game; no signal line — she just doesn't warm up; see full design note below |
| FW-25 [Pink Lucy] | Recruitable companion | Humanity ≥ 7, Engine ≥ 6, Nerve ≥ 5 | TBD | 7w6 Social; communal intimacy; romance unfolds through The Warm Circuit; see full design note below |
| Kendra Heinrich | DLC 1 companion | **None** | **None** | Unique gate system — see full design note below |
| Salagéa Aparast | DLC 5 companion | TBD | TBD | Thresholds pending Phase 7 personality design |
| + all future companions | TBD | TBD | TBD | Rule: all recruitable companions are romanceable by default |
| **Majyao Bisyugota** | **Non-recruitable NPC** | Humanity ≥ 7, Investigation ≥ 6, Calculation ≥ 6 | TBD | 4w5 Self-Pres; teahouse keeper; romance through repeated visits and questline depth; Blood River Tea thread — see design note below |
| Ayako Hayashi | Recruitable companion | Investigation ≥ 7, Humanity ≥ 6, Calculation ≥ 6 | TBD | 4w5 Self-Pres; Red Spiral medic; highest Investigation gate in the roster; see full design note below |
| **Majyao Bisyugota** | **Non-recruitable NPC** | Humanity ≥ 7, Investigation ≥ 6, Calculation ≥ 6 | TBD | 4w5 Self-Pres; teahouse keeper; romance through repeated visits and questline depth; Blood River Tea thread — see design note below |

Non-recruitable named NPCs confirmed romanceable: Majyao Bisyugota (design note below). Further NPC romance status decided per character during design.

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

### Vosora Lashár Tanslock — Romance Design

**Stat gate:** Calculation ≥ 7 (primary), Investigation ≥ 6 (secondary), Nerve ≥ 6 (tertiary)

**Rationale:** Vosora is a 5w6 Social type — distinct from the Self-Pres 5 in that she remains engaged with the world through her work rather than retreating from it. She is already doing something that matters (the Great Corruption investigation), and the romantic path runs through that work rather than around it. Calculation is primary because intellectual respect is non-negotiable for any 5, and for a Social 5 it also means understanding why the work matters. Investigation reflects her own orientation — she's drawn to someone who operates in the same register of careful attention. Nerve ≥ 6 serves the 6 wing: the investigation is dangerous and produces disturbing revelations; she needs someone who can hold steady under difficult information without panic or dismissal.

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

**Signal line** (if stat threshold not met): *"You seem like someone passing through. I don't have much use for those."*

**Gate 3 — Romance beats** (after companion quest completion):

Michelle's romance is about the player coming to understand why she stays, and demonstrating that they understand it in the only way that counts — by making the same kind of choice themselves.

1. **Engage with the Arcanet as more than infrastructure:** The romantic path requires understanding that what she built isn't just a communications network — it's what she chose to give. Questions about why she built it the way she did, what she was trying to make possible. She notices the difference between someone who appreciates the achievement and someone who understands the intention behind it.

2. **Ask the real question:** At some point the player genuinely asks why she stays when she could leave. The romantic path is a player who listens to the answer and takes it seriously — not using it, not performing interest, not skipping past it. The answer is the most honest thing she offers.

3. **The Kharkovchanka moment:** She teaches the player to maintain the vehicle that makes leaving possible. This is an act of trust — she is giving the player access to her capacity to go. The romantic path treats this with the weight it deserves, not as a tutorial.

4. **Choose the city when it would be easier not to:** During her quest, a choice arises where the player could deprioritize Concordia's needs for something personally advantageous. The romantic path doesn't. She stayed because she believes in this place; the player has to demonstrate they understand what that means in practice.

5. **The view from outside:** The most intimate thing she can offer is showing the player what Concordia looks like from a position where leaving is genuinely possible — literally, from the Kharkovchanka outside the city, or metaphorically, from her perspective as someone who could go anywhere and chose here. The romance closes with that shared vantage point.

---

### Favi della Torre — Romance Design

**Stat gate:** Nerve ≥ 7 (primary), Humanity ≥ 6 (secondary), Engine ≥ 6 (tertiary)

**Rationale:** Favi is a 6w5 Self-Preservational type and a sniper — patient, precise, controlled, managing uncertainty through preparation and a small circle of people she can absolutely trust. Nerve is the primary gate not as a test of confrontational courage but as a test of whether the player will hold when it matters to someone else, not just themselves. She watches how people behave when protection costs them something. Humanity confirms that the player's protective instincts come from genuine care rather than calculation — she can tell the difference. Engine at 6 reflects the Self-Pres subtype's value for sustained reliability: showing up consistently over time matters more to her than isolated heroism.

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

**Signal line** (if stat threshold not met): *"I like that you come here. It means something. But I think what you're looking for is different from what I'm able to give."*

**Gate 3 — Romance beats:**

The quietest, most internally textured romance in the game alongside Fenny. She will not reach toward the player; she responds to the player reaching toward her. She is noticed first, then more deeply, then actually seen.

1. **The first real conversation:** Most patrons get warmth and a good cup of tea. This is the first conversation that goes somewhere unexpected — the player asks a specific question about a tea, a detail of the teahouse, something particular. She pauses. She answers at length. She didn't expect someone to actually ask.

2. **The return:** The player comes back. Multiple times. She begins to extend particular attentions — she knows their order before they give it, she brings something unexpected. She says nothing about it.

3. **The depth moment:** A conversation that breaks through the surface, tied to her questline. Janbogo. The war. What it means to have rebuilt something from nothing in the only city left. She says something she hasn't said to anyone else. The player doesn't try to fix it. They listen.

4. **The Blood River Tea moment** *(optional — expand during questline design)*: If the player has followed the Blood River Tea thread — the supply line from Taylor Valley that the Long Night War cut, which she can no longer serve — and can bring her news of it, or in the best case a sample, something opens in her response that nothing else produces. This is the clearest possible signal that someone was paying attention to what actually matters to her, not just to her. Specific mechanics and what this unlocks are to be expanded when the Blood River Tea questline thread is developed in coordination with Frostlands/Taylor Valley design.

5. **The silence:** The teahouse is empty after closing. The aurora through the floor-to-ceiling windows. Both of them simply present, not needing it to be anything else. A 4w5 SP's romance begins in the quiet, not in a speech.

---

### Ayako Hayashi — Romance Design

**Stat gate:** Investigation ≥ 7 (primary), Humanity ≥ 6 (secondary), Calculation ≥ 6 (tertiary)

**Rationale:** Ayako is a 4w5 Self-Preservational type — her entire practice, medicine and fashion both, runs on precise observation. She notices everything and always has. The entry point to her is someone who operates in the same register of careful attention; she recognizes it immediately and it is the only thing that genuinely interests her in a person. Investigation ≥ 7 is the highest gate of that stat in the roster, which fits: no one in the game is more attuned to what is actually there. This deliberately inverts Majyao's profile (also 4w5 SP, but Humanity-primary) — Ayako is more internally focused and more filtered through precision than warmth first. Humanity is secondary because a 4's core wound is feeling unseen; genuine emotional depth must be present alongside the perceptive intelligence, not substituted for it. She has loved a human before, deeply, and the emotional register has to be real. Calculation reflects the 5 wing: she respects careful thinking and someone who can go somewhere with a difficult idea.

**Signal line** (if stat threshold not met): *"You're good at what you do. I've noticed that. I just need more than competence before I can let someone in."*

**Gate 3 — Romance beats** (after companion quest completion):

1. **The atelier visit:** After the companion quest resolves, she invites the player to her home — a practical reason, not an obviously romantic one. The player sees the space for the first time. What they notice, or ask about, in the atelier tells her something she doesn't say out loud yet.

2. **The kept garment:** The player can ask about the single garment on the hook near the window. She answers in one sentence — something at the intersection of grief and craft; made for him, or made in the period after losing him. She moves on immediately. The player who remembers it later, and shows that they do, passes something she wasn't consciously setting as a test.

3. **The mementos:** The player can ask about the arrangement in the living area. She names him. Says something brief and true about who he was. Does not perform the grief. A player who receives this without trying to fix it or position themselves as a replacement gets through something important.

4. **The Schopenhauer question:** She asks what the player thinks about aesthetic contemplation as the only real relief from suffering. Genuine curiosity, not a test. The wrong answer is deflection or a joke. The right answer is honest engagement — including honest disagreement, which she respects more than easy agreement.

5. **The fashion reveal:** She shows the player something personal she is working on — not a Red Spiral commission, not a client piece. She explains what she is trying to do with it. The 4's interior richness becomes fully visible when she talks about what she is making; she almost forgets to be composed. This is the most unguarded the player will have seen her.

6. **The opening:** In the middle of doing something else, she says something specific and true about the player that she has been observing for a long time. It could only come from someone who has been paying very close attention. That is how a SP 4w5 says it.

---

## Romance Reward — Companion Player Homes

**Romancing a companion unlocks that companion's personal home as a player home.** This is universal for all romanceable companions. The home becomes available to the player-character once the romance has been established, and remains available regardless of whether the companion is the currently active companion.

All companion-unlocked homes exist **in addition to** the regular player homes available in the main game. They do not replace or supersede the standard home options. See `Worldspace/Locations-and-Levels/Player_Homes.md` for the full list of standard player homes.

**Calethina is the sole exception.** She is a holographic projection with no physical dwelling — there is no home to unlock. This is the only case where a romanced character does not produce a player home.

The location of each companion's home is tied to their character and district. Companion homes are distributed across Concordia and, in the case of DLC companions, may exist outside the main city as a secondary location. Kendra Heinrich's home is in Capricorn — her origin district and the base of The Reclaimed Record movement she helped seed. After completing her DLC and returning to Concordia, she establishes (or returns to) a residence there. Romancing her gives the player access to that home; if the romance has been perma-locked through dialogue, she maintains the Capricorn home independently and the player does not gain access through the romance route. Ayako Hayashi's home is in Leo — she lives near her atelier and the fashion/creative economy of the district by choice, not near the Red Spiral's Cancer HQ.

Individual companion home designs (layout, contents, lore items, décor reflecting the companion's personality) are Phase 3 and Phase 7 design work per character. Ayako Hayashi's home design is fully developed — see her README.

---

## Calethina: Not a Companion

Calethina does not occupy the companion slot and is not subject to companion system rules. She cannot be dismissed. She cannot be recruited in the conventional sense. She is present or absent based on signal state (before download) or always present (after download).

For implementation: she is a projection system, not a companion object. Any code that iterates over companions does not include Calethina.
