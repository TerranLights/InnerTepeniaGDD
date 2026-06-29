# Player Re-Spec System — Complete Design Reference

*This document supersedes `Player_Re-Spec_-_Costs_and_Trade-Offs.md` and `Player_Re-Spec_-_Options_Beyond_Calethina.md`. Those files are retained for historical context but this is the authoritative reference.*

---

## Design Philosophy

Re-speccing is never a menu option. It is a life-altering decision with irreversible consequences. Changing your MACHINE stats is a narrative event that fundamentally reshapes who the protagonist is, how the world perceives them, and what the future holds.

**Core rule:** Re-spec costs cannot be solved by grinding currency. They must impact identity, body, mind, relationships, story access, and playstyle in ways that cannot be simply bought back.

---

## What Can and Cannot Be Re-Specced

**MACHINE stats — can be re-specced.** Stats represent developed capacity: subsystems that can be intensively reprogrammed at significant cost.

**Traits — cannot be re-specced.** Traits represent fundamental orientation — the deepest layer of who the protagonist is. No method changes a trait. The closest thing is the Scorpio Rebirth Ritual, which installs a competing signal that fights with the existing trait rather than replacing it. The trait remains. It now loses arguments from the inside. This is the mechanism behind echo states.

**Perks — unaffected by re-spec.** Perks are accumulated through play and remain regardless of stat changes, though some may function differently under a new stat configuration.

The romance system's double gate (questline + MACHINE stats/traits) depends on this distinction. Stat-gated romances are reachable through re-spec, at a cost. Trait-gated romances are permanently inaccessible for certain character builds — the rejection line is honest about this, and there is no path in.

---

## Identity Fragmentation — The Spine

Identity Fragmentation (IF) is the cumulative cost of re-speccing. It increases with each re-spec and **cannot be reduced**. It is **visible to the player** — not a hidden penalty, but a known consequence of the choice being made.

Different methods produce different IF costs. Calethina's Lab generates the least fragmentation per re-spec. Extreme methods (Scorpio Rebirth Ritual, crisis events) may advance IF by multiple stages in a single event.

### The Five States

**Whole** *(baseline — no re-specs yet)*
No marker. No effects. The person who emerged from character creation.

**Fractured** *(after 1–2 re-specs through safe or moderate methods)*
- NPCs who know the protagonist well notice something they can't quite name: "you seem different," "the light behind your eyes sits differently"
- Calethina begins asking more questions about how the protagonist is feeling; her tone becomes watchful
- Minor persistent sensory artifacts: occasional audio distortion in dialogue, brief visual flickering during high-intensity moments
- No hard mechanical consequences yet — these are early signs, not punishments

**Fragmenting** *(after 3–4 re-specs, or 1–2 extreme methods)*
- The **"Rebuilt" marker** appears — a visible physical indicator of reconfiguration; different communities read it differently (see below)
- Companions begin referencing "the old you" — with sadness, unease, or suspicion depending on personality and shared history
- Specific questlines branch based on the changed identity; some NPCs extend trust to the new configuration, others withdraw it
- Calethina explicitly voices concern; what she says reflects the specific weight of her relationship with the protagonist
- **Romance route interaction:** characters who knew the protagonist before the re-spec may trigger a secondary dialogue variant — not rejection, but wariness: *"You seem different lately. I'm not sure I know you the same way."* The romance is still accessible if thresholds are met, but the relationship begins in an unusual register

**Unstable** *(after 5–6 re-specs, or an extreme method applied to a protagonist already at Fragmenting)*
- **Echo events:** involuntary behavioral responses from previous configurations surface without warning — an old reaction pattern fires mid-conversation, an old combat behavior triggers before the current one can. Both the protagonist and whoever they're speaking with notice.
- Some questlines permanently close — NPCs whose trust was built with a specific version of the protagonist may decide that person no longer exists
- Calethina's emotional register shifts; what read as concern at Fragmenting now reads as grief
- Significant additional visual change; appearance reflects accumulated transformation
- Social penalties accumulate in districts that value continuity; social bonuses accumulate in districts that value reinvention

**Critical** *(after 7+ re-specs, or an extreme method applied to a protagonist already at Unstable)*
- The **Identity Fragmentation failsafe ending** becomes accessible — one of the four confirmed failsafe endings
- The protagonist's own dialogue options reflect identity confusion: uncertainty about which version of themselves is speaking, references to "the person I was before"
- Calethina's behavior at this stage connects directly to the Devotion ending's emotional core. She has watched this person become someone else. What that means for the relationship — and for her — is one of the most emotionally consequential moments in the game.
- The world treats the protagonist as fundamentally unpredictable; NPCs and factions respond accordingly

---

## Re-Spec Methods

### Calethina's Lab *(Primary Method)*

**Location:** Mid-ring Taurus edge  
**Accessibility:** Available from early-mid game; requires relationship investment with Calethina  
**Risk level:** Lowest  
**IF cost:** Lowest per re-spec

The safest and most controlled option. Calethina understands the protagonist's architecture better than anyone and can perform precise modifications that minimize collateral damage to memory and identity integrity.

But "safest" is not "free." The emotional cost is specific: Calethina knew who walked in. She changed them. She knows exactly what was overwritten and what it cost. Every subsequent visit is her performing this again on someone who is already not quite the person she first knew.

**Calethina's arc through repeated re-speccing:**
- *First visit:* Professional, thorough, honest about the risks. She may be slightly unsettled, but she helps.
- *Second visit:* She asks why. Not to block the choice — she will still do it. But she asks, and the question carries weight.
- *Third+ visit:* Her dialogue shifts register. She still performs the re-spec, but what she says before and after changes. By Fragmenting, she explicitly voices concern. By Unstable, she has moved into grief. By Critical, she says something that is only fully understood in relation to the Devotion ending.

The person most capable of helping the protagonist stop being themselves kept doing it anyway. What that says about Calethina, and about what she decided the relationship was worth to her, is one of the most consequential design questions in the game. Write this with proportional care.

**"Clean Slate" package (Calethina's Lab):**
- Lose 2–3 major perks connected to the changed stats (perks remain, but their effectiveness degrades)
- Temporary adjustment period with minor stat instability, then normalizes
- Permanent minor social debuff with NPCs who knew the protagonist well before
- Calethina grows more distant with each use

---

### Alternative Methods

| Method | Location / District | Flavor | Risk Level | IF Cost |
|--------|---------------------|--------|------------|---------|
| **Black Market Neural Rewrite** | Pisces (The Markets / Shadow Exchange) | Illegal underground neural surgeons; fast, discreet, dirty | Very High | High |
| **Scorpio Rebirth Ritual** | Scorpio (Rebirth Clinics / Ritual Arenas) | Psychological breakdown and ritualistic reconstruction; you are torn apart and remade | Extremely High | Very High (may jump multiple IF stages) |
| **Aquarius Experimental Overhaul** | Aquarius (Prototype Chambers / Robotics Institute) | Cutting-edge prototype augmentation and neural lattice reconfiguration; unpredictable | High | High |
| **Aries Forge Rebuild** | Aries (The Power Core / Overclock Decks) | Heavy industrial cybernetic overhaul; treated like broken machinery being reforged | High | High |
| **Virgo Deep System Purge** | Virgo (Undergrid Maintenance Hubs) | Full diagnostic purge and code rewrite by maintenance crews | Medium-High | Medium |
| **Faction Oathbinding** | Libra (Council Chambers) or high-reputation faction leaders | A faction remolds you in exchange for permanent allegiance | High | High + permanent faction lock |
| **Crisis / Environmental Event** | Various (story-triggered) | Accidental or forced re-spec during catastrophic event | Variable | Variable (uncontrollable) |

All alternative methods require significant reputation, specific items, story progress, or favors to unlock. Each should have its own dedicated scene or small quest — a re-spec is a narrative event. Visual and audio feedback is mandatory; different methods should produce visibly and audibly distinct changes.

**Note on the Scorpio Rebirth Ritual and traits:** This is the only method that approaches trait-level change — but what it produces is a competing signal, not a replacement. The trait remains. The installed signal fights it. Echo states are this conflict made behavioral.

---

## District-Specific Re-Spec Flavors

**Cancer — "Sanctuary Rebinding"**
Sacrifice combat and aggressive capabilities for stronger protective and healing abilities. Gain emotional vulnerability — higher sensitivity when companions are hurt. Permanent bond with Cancer; viewed as soft or overprotective by Aries and Sagittarius.

**Taurus — "Homebound Recalibration"**
Lose nomadic and exploration-related capabilities, and memories of life outside stable habitation zones. Permanent social bonus in Taurus and Cancer; major distrust from frontier districts. Gain "Rooted" overlay: reduced effectiveness when operating far from residential zones for extended periods.

**Leo — "Spotlight Overhaul"**
Gain dramatic presence and charisma; lose subtlety and stealth capabilities. Constant need for public acknowledgment — social penalties when Fame drops. Dialogue becomes more theatrical, which alienates stoic districts.

**Scorpio — "Rebirth Ritual"**
Major personality signal overhaul: gain ruthless pragmatism alongside a competing empathy signal that produces echo states. Risk of uncontrollable echo events during high-stress moments. Scorpio reveres you as having been through the ritual; most other districts see you as unstable or alien.

**Aries — "Forge Rebuild"**
Significantly more machine-efficient: lose organic empathy and social nuance, gain raw power and structural durability. Vulnerability to EMP and cold. Aries respects you as one of their own; residential districts fear you.

**Capricorn — "Production Overhaul"**
Trade adaptability for efficiency: lose flexibility, gain production and crafting bonuses. Permanent visible corporate markings or serial numbers that reduce trust with anti-authority groups. Strong industrial faction ties; hated by Pisces and Sagittarius.

**Aquarius — "Lattice Swap"**
Random or high-risk side effects with each application — new unpredictable weaknesses appear alongside bleeding-edge capabilities. Viewed as a walking experiment: scientific curiosity from Gemini and Aquarius; fear from Virgo and Cancer.

**Libra — "Oathbinding Pact"**
Permanent faction alignment lock — major bonuses with one faction, heavy penalties with rivals. Lose independent dialogue options; many choices are now filtered through the oath. Gain diplomatic influence in the Hub; distrusted as a political instrument by others.

**Gemini — "Subnet Integration"**
Gain massive data and analysis capabilities; risk information overload (occasional stun or confusion in high-data environments). Permanent Arcanet echo — the protagonist hears rumors constantly, even unwanted. Gemini treats them as kin; Pisces and Scorpio suspect they're being monitored.

**Pisces — "Market Rebuild"**
Heavy criminal reputation — permanent infamy with law-abiding districts. Gain black-market capabilities and access; risk being hunted or betrayed. Visible underworld modifications (markings, illegal implants) that change how almost everyone reacts.

**Sagittarius — "Frost-Forged"**
Gain extreme cold and environmental resistance; lose refined social skills, become more direct and survival-oriented in dialogue. Deep respect from outer districts; seen as wild or untrustworthy in the inner city.

**Virgo — "Deep System Purge"**
Risk permanent loss of random skills or memory fragments during the purge. Become more computationally efficient but lose creativity and emotional range. Undergrid crews treat you as family; surface dwellers find you unnervingly sterile.

**Hub / 13th District — "Axis Recalibration"**
Available only late in the story or at great cost. Major shift in core directive toward balance or city-first thinking. Gain powerful central authority access; become symbolically tied to the failing system. Many districts view you as part of the problem.

---

## General Cost Categories

Every re-spec draws from one or more of these categories. Severity scales with method and current IF state.

**A — Memory and Identity Loss**
Specific memories connected to the changed configuration may be permanently erased. Background perk memories tied to old stats may degrade. "Fragmented Self" episodes: involuntary memory playback, glitches, intrusive echoes of previous configurations.

**B — Physical and Augmentation Sacrifice**
Downgrade or removal of augmentations tied to the old configuration. Cumulative physical changes that reflect new configuration — some visible, some not. Increased Siligel dependency or new mechanical vulnerabilities.

**C — Reputation and Faction Locks**
Permanent infamy with specific districts depending on method chosen. Quest and ending lockouts if the changed configuration contradicts a faction's requirements. The "Rebuilt" marker appears at Fragmenting state.

**D — Psychological and Trauma Costs**
Permanent conditions that reflect the transition. Altered core directive. At extreme IF states: echo events. At Critical: identity confusion becomes a dialogue-level reality.

**E — Story and World Consequences**
Changed NPC reactions over time — not always immediate. Altered story paths available. Some questlines become accessible only after specific re-spec events; others permanently close.

**F — Ability and Skill Mutation or Loss**
Loss of access to skill trees or perk categories that no longer fit the configuration. New capabilities with built-in drawbacks (a power mode that drains health; a perception bonus that causes overstimulation). "Skill Atrophy" on previously high skills that lose stat support.

**G — Companion and Relationship Impacts**
Certain companions become distrustful or leave permanently if the re-spec fundamentally conflicts with their values or with who they understood the protagonist to be. New companion relationships or romance routes may open while old ones close. All companions who have known the protagonist through a re-spec should have dialogue acknowledging it — in their own register: sadness, suspicion, grief, curiosity, acceptance. No generic reaction.

**H — Sensory and Perception Changes**
Permanent alteration to how the world is perceived. Loss of specific sensory bonuses in exchange for new types. Risk of Overload Events at high IF states — senses temporarily shut down or go haywire during intense moments.

**I — Temporal, Lifespan, and Energy Costs**
Accelerated wear on the protagonist's systems — a cycle count that represents long-term stability. Increased vulnerability to cold and blackouts after certain methods. Tradeoffs between immediate power and long-term survival that affect late-game options.

---

## The "Rebuilt" Marker — How the World Reads It

The "Rebuilt" marker appears at the Fragmenting IF state and becomes increasingly prominent through Unstable and Critical. It is a visible physical indicator of reconfiguration — not a UI label, but a change in how the protagonist appears in the world.

Different communities interpret the same marker completely differently:

- **Aries:** Respect. You chose to be something harder. That takes something.
- **Taurus / Cancer:** Loss. They knew you before. What's standing here is related to that person, but it isn't that person.
- **Scorpio:** Recognition. You've been to the edge of yourself. That's a form of initiation, whether you intended it or not.
- **Aquarius:** Curiosity. What exactly did you become? What are the new parameters? Can they study this?
- **Virgo:** Unease. The purge should happen in controlled conditions. How controlled were yours?
- **Pisces:** A calling card. They can tell something about how the work was done. They may know who did it.
- **Gemini:** Data. They have opinions about you and will share them regardless of whether you invited this.
- **Libra:** Diplomatic concern. Which version of you agreed to which commitments?
- **Leo:** Aesthetic interest. Are you more interesting now, or less? The answer determines how they treat you.
- **Sagittarius:** Pragmatism. Can you still handle yourself out there? That's the only relevant question.
- **Capricorn:** Efficiency analysis. Were the gains worth the costs? They have calculated this before you could answer.
- **Hub:** Political calculation. Who are you aligned with now, and is that the same as before the change?

---

## The Romance Connection

When a player re-specs specifically to meet a romance threshold, the system responds in a way that reflects what the change cost:

At **Fragmenting** IF state or above, a character who knew the protagonist before the re-spec may notice that something has shifted. The standard rejection line (used when a threshold is not met) is replaced by a secondary variant: not "you don't meet my threshold" but something like *"You seem different lately. I'm not sure I know you the same way."*

The romance route is technically accessible — the threshold is now met. But the relationship begins in a register that reflects the cost of getting there. Whether that resolves over time or carries a persistent shadow is determined by subsequent choices and by the writer's handling of the specific character.

**Trait-gated romances remain inaccessible regardless of IF state.** Traits cannot be changed. The rejection line for a trait gate is honest and final. There is no path in.

---

## The Identity Fragmentation Failsafe Ending

One of the four confirmed failsafe endings is triggered by reaching the Critical IF state. This is not a punishment — it is an ending that takes the protagonist's choices seriously.

A character who has re-specced themselves to Critical fragmentation has made a long sequence of decisions about who they wanted to be. Each decision had a cost they accepted. The game honors that by asking: after all of that, what remains? Who is asking the question?

The specific narrative content of this ending is Phase 5 work. The mechanical trigger is defined here: Critical IF state, regardless of other story progress.

---

## Implementation Notes

- **IF is visible, not hidden.** The player is making an active, informed choice. A hidden meter would function as a trap; a visible meter is a consequence the player owns.
- **Every re-spec is a scene.** The method determines the scene's texture. A menu is not sufficient.
- **Visual and audio feedback are mandatory.** Appearance changes should be cumulative and method-specific. A Scorpio Rebirth re-spec looks different from a Virgo Purge re-spec. Voice may shift subtly with each change.
- **NPCs reference the method, not just the result.** "I heard you went to Scorpio for this" carries different weight than "I can see you've changed."
- **Partial re-specs are available at Calethina's Lab.** Modifying one stat costs less IF than a full overhaul. The cost scales with the scope of change.
- **All alternative methods require gating.** Extreme methods are not available on demand — they require significant reputation, specific items, story progress, or favors. Access scales with risk.
- **Companion reactions are individual, not generic.** Each companion who has known the protagonist through a re-spec needs a specific written response in their own voice. No shared dialogue trees for this.
