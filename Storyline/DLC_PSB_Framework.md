# DLC Framework — Planetary Split Brain as Connective Tissue

*This document establishes how the six DLCs connect to each other and to the main game. It does not define DLC storylines — those are TBD. It defines the structural mechanism by which local DLC decisions produce main-game consequences, and how those consequences compound across multiple DLCs.*

*See `DLC_Overview.md` for the geographic and lore overview of each DLC region.*

---

## Core Design Principle

**Each DLC has its own story.** Its own central conflict, its own characters, its own themes, its own personality. The Planetary Split Brain is not the main questline of any DLC — it is the infrastructure through which local decisions become global consequences. The player is never asked to "solve the Split Brain." They are asked to deal with the reality in front of them, and what they do there ripples outward.

A player who owns no DLCs has a complete game. A player who owns DLCs has additional story content and additional consequences — their decisions have world-spanning effects that a base-game-only player's don't. A player who owns multiple DLCs has an experience that compounds: they will notice contradictions between what different subnets believe, without any character explicitly pointing this out and calling it "the Planetary Split Brain problem."

**The connections are discoverable, not mandatory.** No DLC requires the player to have played any other DLC to understand it. But players who have played multiple DLCs will recognize things. That recognition is the reward.

---

## Ending Model — OG Fallout Design

Inner Tepenia uses the Fallout 1, 2, and New Vegas ending model. This is a binding design commitment.

**Completing the main game ends the game.** Ending slides play. Credits roll. Main menu. That is the end of this playthrough. There is no returning to the world afterward, no post-ending free roam, no continuing to play. The Fallout 4 model — where finishing the main game returns you to the world indefinitely — is explicitly rejected.

**DLCs are played during the main game, not after it.** Between main quests, in any order, as part of the same playthrough. A player who wants to experience DLC content must do so before completing the main game.

**Each DLC ends with its own slides.** When the player completes a DLC, that DLC's ending slides play, the subnet state is locked in, and the player is returned to the DLC geographic area. They can continue exploring and return to Concordia. The DLC is resolved; its consequences are now part of the ongoing playthrough.

**The main game ending incorporates all completed DLC states.** When the player finishes the main game, the ending slides reflect every DLC that was completed before that moment. DLCs the player did not complete simply do not appear — no regional slides for those areas on this playthrough. The ending is a snapshot of what the player actually did.

**Point of no return — mandatory warning.** Before the final main game quest, the game delivers a clear warning: completing this will end the game permanently. Any DLC content not yet experienced will be inaccessible after this point. This is modeled directly on FNV's point-of-no-return warning before the Second Battle of Hoover Dam. The player makes an informed choice to end their playthrough.

**The ending model creates natural exploration incentive.** Players who rush to the main game ending miss DLC content and ending slides entirely. Players who explore the DLCs first arrive at the main game ending with a richer, more consequential result. The game does not force exploration; it rewards it.

---

## The Planetary Split Brain — As Background, Not Questline

The Long Night War destroyed Amundsen Station, severing all inter-subnet Arcanet connections permanently. Each of the six subnets (Palmer, Halley, Mawson, Mirny, Janbogo, Byrd) has been informationally isolated since then, developing its own version of historical records — sometimes in direct conflict with other subnets.

In the main game, set in Concordia (Mirny subnet), this manifests as background: some refugee NPCs have accounts that don't quite match the official Concordia record. The player may notice. They may not. Nothing forces the issue.

In each DLC, the player encounters a different subnet's version of history. If they've played multiple DLCs, they will notice that the Palmer account contradicts the Janbogo account, or that both contradict what Concordia believes. No character gives a lecture about this. The contradictions are just there, in dialogue, in terminal entries, in how different NPCs describe the same events.

**DLC 1 (South Pole) is the structural key.** The pre-split archive at Amundsen Station is the only place where all six subnets' records can be reconciled. What the player does with that archive — if they access it at all — has the broadest possible consequences. But even DLC 1's central story is not "access the archive" — the archive is a consequence of being there, not the reason the player goes.

---

## The 4-Order Effects Chain

Player decisions in a DLC travel outward through four orders of consequence:

### Order 1 — The Direct Decision
What the player does and chooses in the DLC. This is the story. Who ends up in power in a region. What happens to a specific character. Whether a community survives, transforms, or is destroyed. The moral choices and their immediate outcomes.

### Order 2 — Local Subnet Effects
How those decisions change the DLC region's local state. Each DLC region has a set of **subnet state variables** (defined below) that the player's decisions affect. A region whose leadership was stabilized has different resources, infrastructure, and Arcanet connectivity than one that was left in conflict. A subnet whose historical records were published is different from one where they were suppressed.

These effects are local but consequential. They determine what the region is capable of — and therefore what it can do for or to Concordia.

### Order 3 — Main Game Effects
How the changed subnet affects Concordia and the main game world. Concordia is not isolated; it depends on other regions for trade, information, Arcanet connectivity, and political relationships. A stabilized Janbogo region means Hwy 183 is safer and more functional. A destabilized Palmer region means fewer survivors ever reach Concordia. A published subnet archive means Concordia's population encounters contradictions in their own history.

These effects are present in the main game regardless of when the DLC is played. A player who completes DLC 6 before finishing the main game will see a different Concordia than a player who finishes the main game first and then plays the DLC. The 3rd-order effects should be designed to be legible regardless of playthrough order.

### Order 4 — Ending Slides
The ending slides reflect the cumulative result. Each DLC adds slides covering its region's fate. Multiple DLCs create composite slides covering the relationships between regions — what Tepenia looks like as a whole, what the player's legacy is at a continental scale, what the Split Brain ultimately became or failed to become under the player's influence.

The slides are generated by **subnet state combinations** (see below), not by which specific DLCs the player owns. A player who stabilized two regions and suppressed both subnet archives gets one set of composite slides. A player who destabilized both regions but published both archives gets a different set. The DLC identity is less important than the state pattern.

---

## Subnet State Variables

Each DLC region has five state variables that the player's decisions affect. These are the inputs for Order 2 effects and the primary tracking mechanism for composite endings.

### 1. Political Stability
*Who is in power and how legitimate is that power?*
- **Stable — aligned:** A functional government or leadership structure, allied with or friendly to Concordia
- **Stable — neutral:** Functional but independent; not hostile, not allied
- **Stable — hostile:** Functional and adversarial toward Concordia
- **Unstable:** Ongoing conflict; power is contested; the region cannot project capability outward
- **Collapsed:** No functional governance; the region has effectively ceased to exist as a political entity

### 2. Infrastructure Integrity
*Is the region's highway and Arcanet connectivity functional?*
- **Intact:** Full road and Arcanet connectivity; normal trade and communication
- **Damaged:** Reduced capacity; some routes or connections are down
- **Severed:** The region is effectively cut off from Tepenia's larger network

### 3. Resource Availability
*Can Concordia access this region's resources?*
- **Open:** Trade is possible and ongoing
- **Restricted:** Limited access; political or logistical friction
- **Closed:** No access

### 4. Historical Record State
*What happened to the subnet's version of history?*
- **Isolated:** The subnet's records remain in the region, inaccessible to outsiders (default state for all subnets)
- **Shared:** The subnet's records have been transmitted to or made accessible in Concordia
- **Published:** The subnet's records are publicly available across multiple regions; contradictions with other subnets are now visible
- **Destroyed:** The records were lost or deliberately erased during DLC events

### 5. Relationship to PSB Resolution
*Has the player taken any action that affects the Split Brain's structural state?*
This variable is specifically relevant for DLC 1 (South Pole), where the pre-split archive exists. For other DLCs, this variable tracks whether the player encountered and engaged with the subnet's historical contradictions.
- **Untouched:** Player made no decision regarding the subnet's historical records
- **Engaged:** Player encountered the contradictions but took no action regarding them
- **Contributed:** Player took an action that moves toward or away from PSB reconciliation

---

## Composite Ending Structure

The main game ending plays as designed. Ending slides are added in layers:

### Layer 1 — Base Game Ending
Complete on its own. Covers Concordia, the main story's resolution, and the player's legacy within the city. No DLC dependency.

### Layer 2 — Per-DLC Regional Slides
Each owned and completed DLC adds slides covering that region's fate, based on the subnet state variables at the end of the DLC. These slides are self-contained — a player who only owns DLC 3 gets DLC 3's regional slides without needing any other DLC context.

### Layer 3 — Cross-DLC Composite Slides
Added when specific **state pattern thresholds** are met across multiple DLCs. These slides cover the relationships between regions, continental-scale consequences, and what Tepenia looks like as a whole.

State patterns that trigger composite slides (examples — specific content TBD):
- **2+ regions stabilized:** Tepenia's recovery is beginning; Concordia's trade network is expanding
- **2+ subnet archives published:** The contradictions between historical accounts are now publicly visible; slide covers the political fallout
- **Any region collapsed + any region stabilized:** The contrast defines what Tepenia's future looks like — who survived and who didn't
- **All 6 regions played:** A comprehensive legacy slide covering the shape of the player's continental impact
- **South Pole archive accessed + any other subnet archive published:** PSB reconciliation begins; the unified pre-split history exists somewhere in the world

### Layer 4 — PSB Resolution Slides
If the player has engaged with the Split Brain across enough DLCs and taken specific actions regarding historical records, additional slides cover the long-term fate of Tepenia's fragmented history — whether the Split Brain was partially or fully reconciled, suppressed, weaponized, or left intact.

These slides are the furthest-downstream consequence of the entire DLC system. They are rare — most players will not see all of them — and they cover the question the game has been asking since the main game: *what actually happened, and who gets to say so?*

---

## Per-DLC Framework

The following captures what is currently known for each DLC. Central storylines are TBD — only the structural anchors are established.

---

### DLC 1 — South Pole
**Arcanet subnet:** Inter-subnet relay (neutral — not a member of any subnet)
**Central character:** Kendra Heinrich (robot, goddess of war archetype, stranded at the South Pole)
**Central location:** Amundsen Station ruins / Amundsen Tower scrap mountain
**Central story:** TBD

**PSB presence:**
DLC 1 is the structural key. The pre-split archive — the only place in Tepenia where all six subnets' records can be reconciled — is cached here. This doesn't make PSB the main story; it makes the South Pole the location where the player could, as a consequence of being there, make decisions about the unified historical record. What they do with that access affects the Historical Record State variable for Layer 4 composite slides.

**What the player will encounter regardless of story:** The physical ruins of the space elevator that evacuated Tepenia. The Amundsen Tower scrap mountain. The most extreme environment in the game. Kendra Heinrich, who has been here a very long time.

**Difficulty — brutally hard by design and by lore.** This is the hardest DLC in the game. The in-lore justification is binding: Kendra Heinrich is a war goddess who held off an army during the evacuation. Whatever damaged her to the point of being stranded and needing rescue is, by definition, among the most formidable threats in Tepenia. The difficulty is not arbitrary — it emerges from the world's internal logic. The environment is a co-antagonist (extreme cold, no infrastructure, no supply lines). The enemies are unique to this location and cannot be recycled from elsewhere. This DLC is designed for players at the end of their build arc, which reinforces its natural capstone position without requiring a hard gate.

**Known 2nd-order effects (TBD pending storyline):**
Depends on what Kendra's situation is and what the player does about it. The South Pole is not a political entity and cannot be "stabilized" in the conventional sense — its political stability variable works differently. TBD.

**Known 3rd-order effects:**
Access to the pre-split archive (if the player pursues it) affects what Concordia's population can know. The South Pole expedition itself, if the player enables or enables repeated access, affects whether future travelers can reach it.

---

### DLC 2 — West Antarctica (Byrd)
**Arcanet subnet:** Byrd ("Pacific")
**Central character:** TBD
**Central location:** Byrd (only surviving city in Tepenia besides Concordia; ~1,530m altitude)
**Central story:** TBD

**PSB presence:**
Byrd has its own account of the Long Night War and the evacuation. Players from Concordia (Mirny subnet) may find Byrd's account contradicts what they know. Byrd is also the only other place in Tepenia where significant living memory of pre-war Tepenia exists.

**Known structural notes:**
Byrd is "struggling" — its survival is not secure. What the player does here determines whether it continues to exist. The nature of its struggle is TBD.

Possible air connection to Framheim (Ross Ice Shelf) — TBD; implies aviation infrastructure or historical significance.

**Known 2nd-order effects:** TBD
**Known 3rd-order effects:** Byrd's survival or collapse directly affects Concordia's relationship to the rest of the continent. If Byrd falls, Concordia becomes more isolated than it already is. If Byrd stabilizes, it becomes a waypoint and potential ally.

---

### DLC 3 — Antarctic Peninsula (Palmer)
**Arcanet subnet:** Palmer ("American")
**Central character:** TBD
**Central location:** Palmer City ruins (first settled location in Tepenia; cultural and entertainment capital)
**Central story:** TBD

**PSB presence:**
The Palmer subnet account of Tepenia's history is likely to be the most different from Concordia's Mirny account — Palmer City was the cultural capital and the first Long Night War target; the Palmer subnet has had the longest time to develop its own isolated narrative. The Bonded Lattice faction's roots are here; the Palmer account of the robot-human bond question may be quite different from Concordia's.

**Known structural notes:**
Palmer City is destroyed. This DLC is set in ruins — it is an archaeology of what Tepenia was at its most vibrant. 100 Miles Davis Blvd. The founding jazz records. The Antarctica flag. All of this exists as rubble, archive, or living memory among survivors.

Signy (South Orkney Islands) is the northernmost Tepenian outpost — maritime access only, weak Arcanet connection; probably accessible as a side location from this DLC.

**Known 2nd-order effects:** TBD
**Known 3rd-order effects:** Palmer City survivors, if any exist, could reach Concordia. The Palmer account of history, if shared, would be the single most culturally disruptive thing Concordia has encountered — it's the account from the people who built the world first.

---

### DLC 4 — Mawson Region
**Arcanet subnet:** Mawson
**Central character:** TBD
**Central location:** TBD (Mawson, Syowa, or another city in the region)
**Central story:** TBD

**PSB presence:**
The Mawson subnet covers the Indian Ocean coast — the most culturally diverse region in Tepenia by national origin (Australian, Japanese, Russian, Indian, Sinian Federation). Its account of history likely reflects that diversity differently than the Mirny (Australian-origin) account in Concordia.

**Known structural notes:**
Syowa is the major highway junction where Hwy 37 (inland plateau, to Concordia) meets Hwy 7-ext (Atlantic coast system). It was a major transfer point in pre-war Tepenia. Whatever happens to Syowa affects the highway network at a continental scale.

Zhongshan is the Sinian Federation city in this region — the primary point of contact between the Sinian Federation and the rest of Tepenia. Its status has implications for the Sinian Federation storyline (deliberately deferred).

**Known 2nd-order effects:** TBD — but Syowa's infrastructure state directly affects Hwy 37 functionality.
**Known 3rd-order effects:** Hwy 37 connects the East Antarctic plateau to Concordia; disruption or restoration of Syowa affects Concordia's inland route.

---

### DLC 5 — Atlantic Coastal Region
**Arcanet subnet:** Halley ("Atlantic")
**Central character:** Salagéa Aparast (confirmed DLC 5 protagonist)
**Central location:** TBD (Halley, Belgrano, or another city in the region)
**Central story:** TBD — built around Salagéa Aparast

**PSB presence:**
Halley was built on a floating ice shelf — it physically moved over time. Its relationship to geography is unlike any other Tepenian city. Its Arcanet connection runs through Hwy 59 (the Atlantic Throughway / Arcanet Line) to the South Pole relay. Damage to Hwy 59 simultaneously disrupts highway traffic and Arcanet connectivity. If DLC 1 (South Pole) has been played and Hwy 59's state is already established, this DLC intersects with it.

Belgrano Highway Extension (built 2611–2614) — the only confirmed dated infrastructure project; represents Tepenia actively building during peacetime. Whether it still exists and functions is a DLC 5 design question.

**Known 2nd-order effects:** TBD
**Known 3rd-order effects:** Hwy 59 is the Atlantic coast's link to the rest of Tepenia. If it's intact and functional, the Atlantic region can communicate and trade with Concordia. If severed, the Atlantic coast is cut off. This is the most direct infrastructure connection between any DLC and main game connectivity.

---

### DLC 6 — Janbogo Region (Ross Sea)
**Arcanet subnet:** Janbogo
**Central character:** TBD
**Central location:** TBD (Janbogo, Fort McMurdo, or another city in the region)
**Central story:** TBD

**PSB presence:**
Janbogo is partially operational in the main game — it is the key link between Concordia and the outside world. The player already knows Janbogo exists before this DLC. The DLC expands what that actually means: the history, the political reality, the people. The Janbogo subnet nexus hardware sitting inside Concordia's Gemini district (see Phase 1 design tasks) becomes legible here.

Fort McMurdo was the largest pre-war city in Tepenia — a mining and resource-processing hub. Destroyed, but its ruins are significant.

**Known 2nd-order effects:** Janbogo's political stability directly determines the safety and functionality of Hwy 183 — the primary route connecting Concordia to the Ross Sea region. This is the most operationally direct DLC-to-main-game connection.
**Known 3rd-order effects:** If Janbogo stabilizes under terms favorable to Concordia, Concordia's isolation decreases substantially. If it destabilizes further, Hwy 183 becomes dangerous. If it collapses, Concordia loses its most important external connection. This DLC has the highest direct impact on Concordia's day-to-day reality.

---

## DLC Order and Gating Policy

**There is no hard gate. No DLC purchase is required to access any other DLC. Any DLC can be played in any order.** This is a firm design commitment — player freedom and agency take priority.

### How DLC 1 Is Special Without Being a Gate

DLC 1 contains the pre-split archive — the only place in Tepenia where all six subnets' records can be reconciled. This is architecturally important. It does not need to be a purchase requirement to be meaningful.

**Every other DLC surfaces the contradiction but cannot resolve it.** DLCs 2–6 each take place in a specific subnet. Players encounter that subnet's isolated account of history. If they have played other DLCs, they will notice that accounts conflict. The Split Brain is visible as a problem throughout the series — none of the other DLCs contain the structural means to address it at the source.

**DLC 1 is where the resolution lives.** The Layer 4 PSB resolution ending slides — the deepest composite ending content — require DLC 1's contribution to the PSB Relationship State. Players who don't own DLC 1 still receive complete regional slides and cross-DLC composite slides from their other DLCs. They simply do not receive the layer that addresses what the Split Brain ultimately became. This is not a punishment; it is what DLC 1 contributes.

**DLC 1 sells itself through mystery.** A player who has completed DLCs 3, 5, and 6 has encountered three contradictory accounts of the same historical events. The South Pole — already referenced throughout the main game and other DLCs as the site of Amundsen Tower, the inter-subnet relay, the place everything once connected — is where the answer is. That player does not need to be told to buy DLC 1. The accumulated contradictions create the motivation.

**Environmental difficulty does soft gating.** The South Pole is the most isolated and extreme environment in the game. Reaching Amundsen Station requires a level of preparation that naturally suits a later-game player. No lock is needed; the world creates the tendency.

### Recommended Order (Suggested, Not Required)

In the same way Fallout: New Vegas suggests playing Lonesome Road last without requiring it, Inner Tepenia's DLCs have a natural order that produces maximum resonance — without mandating it:

- **DLCs 2–6 in any order** — each is self-contained; cross-DLC recognition compounds with each additional DLC played
- **DLC 1 as a natural capstone** — the archive is most meaningful once the player has encountered the contradictions it resolves; Kendra's story is complete on its own, but lands differently once the player understands what the South Pole's absence has meant for the rest of Tepenia

Players who play DLC 1 first still get a complete, satisfying experience. They arrive at the archive before fully understanding what it resolves. The archive will still be there on a second playthrough — and it will mean something different.

**DLC 1 is Inner Tepenia's Lonesome Road:** complete independently, most rewarding as a capstone, designed to be sought rather than required.

---

## Design Constraints

**Never make PSB the main questline of a DLC.** It is background, consequence, and connective tissue. Players who never think about it still play a complete game. Players who notice it are rewarded.

**DLCs must be completable independently.** No DLC should require the player to have played another DLC to understand what's happening. Cross-DLC rewards are for players who engage with the full series; they are never required for a satisfying individual experience.

**Do not over-explain the connections.** No character should give a speech about how this region connects to that region connects to Concordia. The connections are real and structural — they manifest in what the world looks like, not in what characters say about the world.

**DLCs are played during the main game, not after it.** Inner Tepenia uses the Fallout 1/2/New Vegas ending model: completing the main game ends the game permanently — ending slides, credits, main menu. There is no post-ending world to return to. DLCs must be played between main quests, before the point of no return. This is a firm design commitment; the Fallout 4 model (return to the world after the ending) is explicitly rejected.

**The 3rd-order main game effects are visible during play.** A player who completes DLC 6 before finishing the main game will see Janbogo's state reflected in Concordia while they are still playing. This is not a post-game feature — it is a during-game consequence.

**DLC completion locks in the subnet state.** Each DLC ends with its own ending slides, then returns the player to the DLC area. They can continue exploring that area and return to Concordia. The subnet state variables from that DLC are now fixed and will be incorporated into the main game ending if and when it is reached.

**Each DLC ends.** It has a beginning, a middle, and a resolution. The resolution may be ambiguous or bittersweet — but it is a resolution. The DLC is not a chapter in a larger story; it is its own story that happens to have consequences.

---

## Open Questions (for future design sessions)

- Central storylines for all six DLCs (TBD — do not design around PSB as the focus)
- Central characters for DLCs 2, 3, 4, 6
- Specific subnet state thresholds for composite ending slides
- How DLC release order affects player experience (earlier DLCs establish the world; later DLCs reference it — release order is a separate question from playthrough order)
- Byrd air connection to Framheim — aviation infrastructure or historical site? TBD
- Dumont d'Urville (DLC 6 region) — included directly or side-content only?
- Ji-Eun Kim — if she appears in a DLC rather than the main game, which region?
