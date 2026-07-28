# Permanent MACHINE Stat Increases

**What this is:** a design draft, not a locked decision — written 2026-07-27. Establishes the two mechanisms
by which a player character's MACHINE stats can permanently grow beyond the 5+5 character-creation budget
(`Character_Creation_Overview.md`), distinct from — and compatible with — the existing re-spec system
(`Core-Mechanics/Player_Re-Spec_-_Complete_Design.md`), which *redistributes* the player's existing stat
budget at a real Identity Fragmentation cost rather than growing it. These two systems don't conflict: re-spec
moves points you already have; the mechanisms below add new points to the total pool.

**Hard ceiling, unchanged:** MACHINE stats remain capped at 10 regardless of source — character creation,
Intense Training, or implants. Neither mechanism below can push a stat past that ceiling.

---

## Mechanism 1 — Intense Training (Perk)

**Ported directly from FNV, per developer confirmation 2026-07-27** — reverses an earlier call in
`Perks/FNV_Perk_Cross_Reference_Audit.md`'s "Not Portable As-Is" bucket, which had reasoned that a free stat
increment would undercut the re-spec system's own cost structure. The developer confirmed this perk is wanted
after all; the audit file has been corrected to match (see that file's own updated entry).

**Effect, verified against the real perk 2026-07-27:** Level 2, no other requirement, repeatable **up to 10
times total** across a playthrough — each rank grants a single, permanent +1 to any one MACHINE stat of the
player's choice, chosen at the moment that rank is taken. Written into `Perks/Regular_Perks_-_Level-Up.md`'s
Growth/Learning category with these verified numbers.

**A nice confirmation, found while verifying this perk:** the real FNV wiki entry notes that points from
Intense Training put into Endurance specifically grant "more implants" at Doctor Usanagi — validating the
Engine-substitutes-Endurance design choice below independently, since the two systems already interact the
same way in the source material this is adapted from.

---

## Mechanism 2 — Implants ("not-Doctor-Usanagi" NPCs)

**A second, distinct route to permanent stat growth**, gated through a recurring NPC archetype rather than a
level-up perk choice — multiple such NPCs exist across Concordia's districts (a "not-Doctor-Usanagi" in
Cancer, another in Scorpio, and presumably others elsewhere), each capable of performing the same kind of
procedure.

**The two-part limit, confirmed 2026-07-27:**

1. **Total implant count is capped by the player's Engine stat.** Engine substitutes for FNV's Endurance here
   (Doctor Usanagi's own real gate stat), matching Engine's already-established role as the
   bodily-durability/recovery-speed stat in Inner Tepenia's system. A player with Engine 6 can safely receive
   up to 6 total implants, across all 7 MACHINE stats combined.
2. **Each of the 7 MACHINE stats can only ever receive ONE implant, period — no stacking a second +1 onto the
   same stat, regardless of how many Engine-based slots the player has left.** This is a real, physical
   "this specific augmentation site has already been modified" limit, independent of the total-slot count.
   Practical effect: a player who has already had Calculation implanted once will be refused by *any*
   "not-Doctor-Usanagi," anywhere in the city, not just the one who performed the original procedure —
   visiting a different district's practitioner doesn't reset or bypass this per-stat limit.

**Refusal flavor, confirmed by example:** a player who received a Calculation implant from the Cancer
practitioner, then requests a *second* Calculation implant from the Scorpio practitioner, is turned down with
something to the effect of: *"I'm sorry, but your frame just can't handle this. I'd be putting you in
danger."* The refusal is about the specific stat already being modified, not about the player's remaining
implant capacity — even a player with Engine-based slots to spare gets this same refusal if they try to
double up on one stat.

**Practical ceiling this creates:** since only 7 MACHINE stats exist, the real maximum number of implants any
player can ever receive is `min(Engine stat value, 7)` — a player with Engine 8+ can't actually use their full
slot allowance unless implants exist for all 7 stats; a player with Engine 4 or lower will always have some
stats permanently inaccessible to implant-based growth, regardless of how many different practitioners they
visit.

**NPC identity, confirmed 2026-07-27:** each "not-Doctor-Usanagi" is a named, individual character per
district — not a generic, replicated archetype. **Their in-game function is limited to the implant procedure
itself, with one deliberate exception: ordinary conversation.** They carry no other mechanical role (no
questline, no faction tie confirmed, no companion potential established here) — their value beyond the
procedure is purely the natural, organic lore-dropping a named local practitioner can offer through dialogue,
the same way plenty of non-recruitable named NPCs elsewhere in the game exist mainly to texture their
district rather than drive a quest.

**Which districts actually have one, resolved 2026-07-28** — a "modestly reasonable majority," not all 13,
decided district-by-district against `Districts/District_Canon_Reference.md`'s established identities:

**Confirmed present (7 of 13):**
- **Aquarius** — already-canonical: the district text itself states it has "the city's highest rate of
  experimental augmentation," making this close to a foregone conclusion rather than a stretch.
- **Scorpio** — already-canonical: its own inhabitants list names "shadow augmentation specialists" outright;
  transformation is the district's entire reason for existing.
- **Cancer** — the original illustrative example; built on existing medical/caregiving infrastructure
  (integration facilitators, medical support bots) already established for the district.
- **Pisces** — "fluid-frame robots" (modified for rapid reconfiguration/identity shifting) are already
  canonically "common in Pisces, rare everywhere else," and the district's whole black-market identity means
  access to procedures unavailable or unsanctioned elsewhere.
- **Aries** — the overclock/"push it until it breaks" culture (voluntary hot shifts as a status symbol,
  near-devotional treatment of machinery) maps directly onto a practitioner whose *proprietary specialty*
  leans Engine (see "Per-District Thematic Specialty" below — this is not exclusivity, just flavor);
  confirmed despite Aries' fatalistic "bodies get used up, not upgraded" undercurrent, since the
  overclock-culture fit outweighed it.
- **Concordia Central Hub (Axis Mundi)** — confirmed specifically *because* it's neutral ground: a resident
  wary of a district-branded procedure (an Aquarius-flavored experimental implant, say) can get one here
  without any district affiliation or judgment attached — consistent with the Hub's own "principled
  rootlessness" identity, and distinct enough from Calethina's Lab (activation, not implants) to coexist.
- **Virgo** — resolved after genuine back-and-forth: the district's residents overwhelmingly stay in the
  Undergrid rather than surfacing (per canon: accustomed to low light, navigate by sound/touch, find surface
  brightness "overwhelming"), which means Virgo maintains its own in-house infrastructure end-to-end —
  schools, bureaucratic centers, hospitals, and by extension its own implant practitioner — rather than
  relying on any surface district's version.

**Confirmed absent (6 of 13):**
- **Taurus** — domestic/stability culture with no technical-medical infrastructure; residents are consumers
  of services, not innovators or specialists in this space.
- **Libra** — a regulatory/legal district that oversees and restricts this kind of thing (see its Aquarius
  oversight relationship) rather than performs it.
- **Capricorn** — ruled out on two grounds: its meritocratic "status is *earned*, not bought" self-image sits
  uneasily with a pay-for-a-permanent-implant practitioner, and — the deciding factor — geography/setting:
  it's simply not characteristically a place such a person would be. A Capricornian wanting an implant would
  travel to a similarly industrialized district with its own local practitioner instead (which is exactly
  why Virgo, not Capricorn, ended up the industrial-adjacent district that has one).
- **Sagittarius** — ruled out on the same geographic/setting logic as Capricorn: not every district needs to
  be self-sufficient for this, and Sagittarius residents would instead travel to a district that has one.
- **Leo** — ruled out as simply not internally, characteristically consistent with the district — performance
  and morale culture, not augmentation medicine, no matter how the "vanity"/competitive-edge angle was framed.
- **Gemini** — ruled out for lacking any textual anchor at all: its inhabitants list is entirely
  routing/archival/broadcasting roles, with zero medical or augmentation-adjacent presence anywhere in canon
  (unlike, say, Aries or Virgo, where a real cultural thread could be pointed to).

**A working rule that fell out of this pass, worth reusing elsewhere:** a district doesn't need its own
practitioner just because it has relevant industry or culture nearby — Capricorn and Sagittarius are both
ruled out partly on the logic that their residents simply travel to a neighboring or thematically similar
district instead. Not every district needs to be self-sufficient in every kind of specialist.

---

## Universal Implant Availability vs. Per-District Proprietary Specialty

**Confirmed 2026-07-28 — an important correction to how the district/stat association above should be read:**
all 7 MACHINE stat implants are available at **every** "not-Doctor-Usanagi," regardless of district. The
one-implant-per-MACHINE-stat limit (see above) is a property of the *player's frame*, not of any single
practitioner's specialty — nobody is gatekept from a given stat implant by which district they're standing in.

**What the district/stat association is actually for**, following the real FNV precedent this whole system is
adapted from — verified 2026-07-28: Doctor Usanagi offers the standard nine-part SPECIAL implant series
(4,000 caps each) available to anyone who meets the Endurance-based slot requirement, *plus* two proprietary
combat implants exclusive to her practice: a permanent +4 Damage Threshold implant (8,000 caps) and the
PHOENIX Monocyte Breeder, a passive 1 HP/10-seconds regeneration implant. Those two extras aren't part of the
standard SPECIAL series — they're *her* specialty, on top of it.

Inner Tepenia's 7 practitioners work the same way: universal MACHINE implant access for everyone, plus each
practitioner's own **proprietary bonus implant(s)**, thematically keyed to one MACHINE stat that matches their
district's identity. That stat theme also doubles as an **art-direction and conversation-topic guide** for
each practitioner's office — what the space looks like, and what kind of organic lore-dropping dialogue fits
there.

**Proprietary bonus implant count, confirmed 2026-07-28:** unlike Usanagi's fixed two, each practitioner isn't
limited to offering just two proprietary implants — the number can vary practitioner to practitioner. The only
fixed rule is a **floor of 2 and a ceiling of 9 per location** (i.e., anywhere from 2 to 9 inclusive); where
any given practitioner lands within that range is a per-district creative call, not a fixed count applied
uniformly across all 7.

**Proposed thematic keying, 2026-07-28 (open to further refinement):**

| District | MACHINE Stat Theme | Why |
|---|---|---|
| **Aries** | Engine | Overclock/burnout culture — "operational endurance before burnout" is nearly a direct paraphrase of Aries' own civic identity. |
| **Cancer** | Humanity | Empathy, emotional connection, and care — Cancer's entire reason for existing. |
| **Scorpio** | Nerve | Mental resilience and willpower — transformation through confrontation is the district's whole practice. |
| **Aquarius** | Calculation | Logical/experimental research — the district's baseline mode of operation. |
| **Virgo** | Investigation | Diagnostic precision and systems analysis — matches "precision diagnostic and repair" and "systems analysts" directly. |
| **Pisces** | Agility | Fine motor control and reconfiguration — matches the canonical "fluid-frame robots modified for rapid reconfiguration." |
| **Central Hub** | *(deliberately unspecialized)* | No district's civic identity is actually built around raw physical strength (Might), which is why it doesn't map cleanly onto any of the six above. Rather than forcing an awkward fit, the Hub's practitioner can lean into genuine non-specialization — a deliberately generic, modular office and conversation topics about neutrality/adaptability itself, consistent with the Hub's own "no affiliation, no judgment" identity. |

**Not yet designed:** the actual proprietary bonus implant(s) for each district (the Usanagi-DT/HP-regen
equivalent) — this is the next real design step, one district at a time.

### Per-District Proprietary Bonus Implants — Working List

**Guiding principle, confirmed 2026-07-28:** quality over quota — there's no obligation to fill out toward
the 9-implant ceiling per district. Landing on the *right* implants matters more than landing on a specific
count; some districts may end up with 2-3, others more, purely based on what genuinely fits.

**Aries (Engine theme) — confirmed 2026-07-28, 4 implants:**
1. **Passive HP regeneration** — the most direct Usanagi analog (PHOENIX Monocyte Breeder equivalent);
   frames the "your body just runs a little hotter now" idea literally.
2. **Reduced AP cost for Block Stance** — ties directly into `Combat/Block_Stance.md`; thematically apt since
   Aries pushes equipment (and by extension, a body) past normal tolerances without breaking.
3. **"Overclock Burst"** — a once-per-combat temporary AP surge, mirroring Aries' "running hot" status-symbol
   culture: genuine risk/reward, since running hot in-fiction produces heroes *and* preventable martyrs.
4. **Heat/radiation exposure resistance** — grounded directly in Aries' own history (the Overclock Martyrs,
   geothermal/nuclear core work); a practical, lore-consistent implant nobody else in the city would have
   reason to offer.

**Cancer (Humanity theme) — confirmed 2026-07-28, 3 implants:**
1. **Passive companion HP-regeneration aura** — simply having a companion currently active in the party grants
   them a passive HP-replenishment effect, automatically, no action required. This is distinct from and stacks
   with manually applying a healing item to that companion (see `Companion_System.md`'s new "Combat
   Interaction — Applying Healing Items to a Companion" section, confirmed the same day, ported directly from
   FNV's Stimpak-on-companion mechanic) — one is a passive frame-level effect from this implant, the other is
   an active, player-initiated item use; they're independent and both apply simultaneously if present.
2. **Resistance to fear/despair-type status effects** — grounded directly in Cancer's grief-support culture
   and its history stabilizing traumatized war refugees and newly-activated robots.
3. **Enhanced empathic read** — passively reveals a companion's or NPC's hidden emotional state/mood in
   dialogue, framed as heightened social awareness rather than persuasion (kept distinct from Nerve's
   "influence over companions," which belongs to Scorpio's theme instead).

**Scorpio (Nerve theme) — confirmed 2026-07-28, 4 implants:**
1. **Resistance to manipulation/intimidation-type effects** — mental fortitude specifically against being
   controlled, coerced, or broken by hostile influence. Deliberately distinct from Cancer's fear/despair
   resistance: Cancer's is protective/caregiving-flavored (grief, emotional collapse), this one is
   confrontational (resisting an opponent's deliberate attempt to dominate or manipulate the player) — matching
   Scorpio's ethos of surviving intentional psychological confrontation rather than being sheltered from it.
2. **Companion Rally implant** — an activated ability that temporarily boosts the active companion's combat
   performance. Maps almost literally onto Nerve's own stated definition ("influence over companions" per
   `MACHINE_Stats.md`) — the more honest home for this than Cancer, despite Cancer being the "caregiving"
   district.
3. **Enemy intimidation/demoralize implant** *(flagged 2026-07-28 for future review — the core idea is good,
   but the exact shape/execution needs further refinement before it's considered finished)* — an activated
   ability to frighten or demoralize an enemy (a debuff), grounded directly in the district's confrontational
   psychological-warfare identity.
4. **"Emergence Reflex"** *(named 2026-07-28 — originally sketched as "Second Wind," renamed to avoid the
   collision with Baldur's Gate 3's own perk of that name; "Emergence" is drawn directly from Scorpio's own
   canonical mask-culture vocabulary — descent, integration, emergence — rather than a generic term. **Flagged
   2026-07-28 for a possible future renaming** — this name itself isn't locked, just the current placeholder)*
   — a temporary Nerve-based buff triggered automatically when the player drops to critically low HP, built on
   the district's own canonical near-death simulation facilities (years-long waitlists, genuine demand
   citywide) — surviving a brush with death as a source of strength rather than pure trauma.

**Aquarius (Calculation theme) — confirmed 2026-07-28, 4 implants:**
1. **Reduced AP cost for hacking actions** — the same shape as Aries' Block Stance AP discount, but for
   hacking; fits Aquarius's tech-forward identity directly.
2. **Passive minor trace-signature reduction** — a modest, always-on reduction in hack traceability
   (`Core-Mechanics/Hacking_and_Traceability_System.md`). Deliberately kept smaller than, and stacking with,
   the existing Data Ghost / Ghost in the Machine perks rather than competing with them — a baseline
   improvement anyone can get, further sharpened by real skill investment.
3. **Tactical Damage Calculator** — passively reveals the exact damage output of an attack before committing
   to it, removing guesswork. An analytical/optimization-flavored bonus fitting Calculation's "problem-solving"
   definition directly.
4. **An experimental double-edged implant** *(flagged 2026-07-28 for future review — the core idea is good,
   but the exact trade-off and whether it fits the system's "permanent, safe growth" premise needs further
   thought)* — a stronger permanent bonus paired with a genuine built-in cost (a fixed trade-off, not
   randomized — e.g., +X to something, −Y to something else), embodying Aquarius's "savior and reckless
   hazard" duality and its own Contamination Events history.

**Virgo (Investigation theme) — 2 of 3 confirmed 2026-07-28, 1 pending:**
1. **Dark-adapted senses** *(pending 2026-07-28 — see Open Questions below; raised a genuine open design
   question about player-visible vs. character-perceived visibility in a top-down isometric renderer that
   needs resolving before this implant can be finalized)* — permanently improved perception/detection in
   darkness or low-visibility conditions, matching Virgo residents' canonical adaptation to navigating "by
   sound and tactile memory as much as by sight."
2. **Hazard/danger sense** — passively reveals structural or environmental hazards (traps, unstable terrain,
   failing infrastructure) before they trigger. Grounded in Virgo's own "predictive structural-integrity/
   failure models" and its entire "We Keep You Alive" civic mission — redirected from the city's
   infrastructure onto the player's own path.
3. **Enhanced hidden-object/secret detection** — passively highlights hidden caches, secret passages, or
   points of interest in the environment. Matches Virgo's meticulous, detail-obsessed culture directly (the
   district that "knows every pipe... which backup system is six months past due").

**Pisces (Agility theme) — confirmed 2026-07-28, 4 implants:**
1. **Sleight-of-hand / pickpocket implant** — enhanced fine motor control for stealing, lockpicking, or
   concealment. Matches Pisces' black-market/smuggling identity directly.
2. **"Rapid Reconfiguration"** — a quick-change ability letting the player briefly alter their appearance or
   identity marker to avoid recognition or slip past hostile detection — nearly a literal translation of the
   district's own canonical "fluid-frame robots modified for rapid reconfiguration and identity shifting" onto
   the player character.
3. **Improved evasion/reflexes** — a passive dodge/evasion bonus, the most direct hit on Agility's own core
   definition ("speed, reflexes, coordination").
4. **Reduced AP cost to disengage from combat** — makes it easier to slip away mid-fight, echoing both the
   district's ethos ("everything eventually dissolves") and its literally labyrinthine, ever-shifting
   geography.

**Central Hub (deliberately unspecialized) — confirmed 2026-07-28, 3 implants:**
1. **Dialogue-only universal boost** — a flat **+1 to all effective MACHINE stats** and **+10% to all
   effective skills**, but strictly scoped to dialogue checks — **not** combat, **not** romance gate
   thresholds (which already only read permanent base stats per `Companion_System.md`'s Gate 2 rule, so this
   exclusion is consistent with existing design), **not** repair/crafting/fixing, and **not** physical
   world-interaction of any kind. Makes "being a generalist" the Hub practitioner's own distinct flavor rather
   than the absence of one — a broad, modest bonus instead of one narrow, powerful specialty like the other
   six districts.
2. **Reputation dampener (double-edged)** — reduces the rate of *negative* reputation progress, but
   symmetrically also reduces the rate of *positive* reputation progress. A genuine trade-off matching the
   Hub's "no affiliation, no judgment" identity: the player becomes harder to sour on, but also harder to
   truly win over, in either direction at once.
3. **Passive district-rumor pickup** — unlocks an always-available dialogue option/topic ("What's the word
   from around the city?") in conversations with NPCs in any district; selecting it surfaces a small,
   hand-authored ambient lore/rumor snippet about a *different* district than the one the player is currently
   in. Deterministic, not a random roll — reuses the same "organic lore-dropping through dialogue" pattern
   already established for the "not-Doctor-Usanagi" NPCs themselves. **Confirmed 2026-07-28 despite the
   real, significant content workload this implies** (hand-authored rumor snippets per district) — the
   developer's own call that the player-experience payoff justifies it.

---

## Open Questions

- ~~Whether "not-Doctor-Usanagi" NPCs are meant to be named, distinct individual characters or a more generic,
  replicated archetype~~ — **resolved 2026-07-27:** named individuals per district, mechanically limited to
  the implant procedure plus ordinary conversation/lore-dropping, no other in-game function.
- ~~Whether every district has one, or only some~~ — **resolved 2026-07-28:** 7 of 13 (Aquarius, Scorpio,
  Cancer, Pisces, Aries, the Central Hub, Virgo). See the district-by-district breakdown above.
- Cost/price for an implant procedure, and whether it requires anything beyond credits (a quest, a reputation
  threshold, specific materials) — not yet designed.
- **New, 2026-07-28 — genuinely unresolved, raised while designing Virgo's "Dark-adapted senses" implant:**
  how much of a gap should there be between what the *character* can perceive (in-fiction low-light/no-light
  vision) and what the *player* can actually see on screen, in a top-down isometric renderer? No existing
  fog-of-war, lighting, or vision-cone system has been established anywhere in `Game-Mechanics/` to answer
  this against — this implant (and potentially the game's broader lighting/visibility model) needs that
  question sorted out first, rather than assuming a specific rendering behavior here.
- ~~The actual proprietary bonus implant(s) for each of the 7 practitioners~~ — **resolved 2026-07-28,** all 7
  districts complete (Aries, Cancer, Scorpio, Aquarius, Virgo, Pisces, Central Hub) — see "Per-District
  Proprietary Bonus Implants — Working List" above. Two items remain flagged for future refinement within
  that list: Scorpio's enemy-intimidation implant (#3) and Aquarius's experimental double-edged implant (#4).
- ~~Whether Intense Training can be taken multiple times~~ — **resolved 2026-07-27, verified against the real
  perk:** yes, up to 10 times total, Level 2 requirement, no other gate.
