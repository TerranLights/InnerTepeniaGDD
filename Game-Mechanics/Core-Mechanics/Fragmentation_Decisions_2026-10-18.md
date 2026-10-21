# Fragmentation — decisions log

**Started 2026-10-18.** Developer rulings from working through the Fragmentation phenomenon (Identity Fragmentation meter, the Bond/Grief matrix, secondhand discovery) one question at a time. Source files: `Fragmentation_Matrix.md`, `Fragmentation_Matrix_Expansion_Ideas.md`, `Player_Re-Spec_-_Complete_Design.md`. **Nothing below has been applied to those files yet**; edits are made together once the decisions are done, shown to the developer first.

## 0 · What can be re-specced — correction, 2026-10-18
- **Traits are permanent.** Everything else can be re-specced at a cost.
- **Perks are not guaranteed to stay.** Many perks require a minimum in one or more MACHINE stats; if a re-spec drops a stat below a perk's requirement, the player no longer qualifies for it.
- **Contradicts the current text** in `Player_Re-Spec_-_Complete_Design.md` ("Perks — unaffected by re-spec") and softens the "Clean Slate" package line ("perks remain, but effectiveness degrades"). Both need updating once the question below is answered.
- **A perk whose requirement is no longer met: a combination of "dormant" and "weakened" (developer, 2026-10-18).** It does not simply vanish and does not simply keep working. The developer's idea for how, **to be worked out in detail before anything is implemented:** see the next section.
- **Open:** whether perks themselves can be re-chosen as part of a re-spec ("everything else can be re-specced").

## 0.1 · Idea: overwritten perks "glitch" — to be worked out first, not yet implemented
The developer's idea (2026-10-18, in their words condensed): **overwritten perks** (perks from builds prior to a re-spec) stay somewhat in effect through later re-specs but **fire randomly**, either with **different numbers or different stats than they used to** (very likely at lowered or degraded values), or **in ways opposite to or contradicting what they used to do.** They "glitch out." It is somewhat like the **Jinxed trait in Fallout 1**, except that previously overwritten perks would glitch much more often, **for or against the player's favor**, and **the glitches have effects on the surrounding enemies, combatants or people.**

**Link to existing design:** the Identity Fragmentation states already include **echo events** (an old reaction pattern firing involuntarily, from the Unstable state) and the Fragmentation Matrix's release scope lists **"glitchy" re-spec effects** and **residual player-mechanic echoes.** The glitching perks are a natural mechanical form of those.

**Questions to settle (in this order):** (1) which perks glitch; (2) what triggers a glitch and how often; (3) what a glitch can do (degraded, wrong stat, inverted, spills onto others); (4) how it stays readable in a turn-based tactical game; (5) whether and how it can be fixed or purged; (6) how it connects to the Identity Fragmentation states and to echo events.

## 0.2 · Which perks glitch, and re-choosing perks — decided 2026-10-18 (details to refine)
- **All perks the player previously had and currently does not have glitch** ("past perks").
- **Intensity depends on whether the player now meets the perk's requirement:**
  - **Meets the requirement again but does not have the perk:** the perk **glitches less, and to a lesser degree.**
  - **No longer has the perk and no longer meets the requirement:** the perk **glitches harder and more often.**
- **The player can re-choose perks as part of a re-spec.** (Yes, definitely.)
- **Interpretation to confirm:** a perk the character currently holds always meets its requirement and works normally; a perk that a re-spec removes (because the requirement is no longer met, or because the player swapped it out) becomes a "past perk" and glitches as above; re-taking the perk ends its glitching. This replaces the earlier idea of a separate "dormant" state.
- **Still to settle:** what triggers a glitch and how often (the developer: "we'll need to sort that out in greater detail"); what a glitch can do; readability in a turn-based game; whether and how it can be fixed or purged; the tie to the Identity Fragmentation states and echo events.
- **Grief value versus ledger, and whether the summary of the system is right:** the developer wants to look at the full Fragmentation specs again first.

## 0.3 · A "Jinxed"-premise trait will exist — 2026-10-18
The Fallout 1/2 trait Jinxed (not in New Vegas, so a valid option under the Precedence Law) **will be in Inner Tepenia in principle**, though possibly under a different name: its fundamental premise stays. The glitching past perks are modeled on that premise (glitches that affect the people around the player, for or against the player's favor).

## 0.4 · Summary confirmed; current perks versus past perks — 2026-10-21
- The developer confirmed the summary of the whole Fragmentation system (re-spec as cause; the IF meter; the Bond/Grief matrix and seeding; The Long Vigil; secondhand discovery) is right.
- **New idea: conflicts between a perk the player has now and a past perk they no longer have** should be able to **produce novel or interesting results, either positive or negative.** To be designed together with the glitching past perks (a possible method: tag perks, author a small set of interaction results for known conflicting pairs, and use a generic fallback for the rest).
- **Grief value versus ledger:** the developer asked what the mechanics of each would actually look like; options laid out 2026-10-21; decision pending.

## 1 · Grief: single value or ledger — decided 2026-10-21
**A ledger:** one Grief entry per past configuration a companion actually knew, each seeded at its re-spec. Reasoning (developer asked which is more emotionally fulfilling): grief is for particular people, not a quantity; the player is seen and remembered as more than one self; a resolution scene can resolve exactly one loss; the player's own history becomes real; and the stored past-configuration snapshots are shared with the glitching past perks. **Safeguards:** the ledger stays hidden (shown only through dialogue, behavior and the named states, never as numbers or a list of grievances); dialogue surfaces one or two entries at a time; the tone is tenderness, not shaming the player for re-specced selves, and some entries can be about gratitude as much as loss.
**The "visible tier"** is the named state the 16-cell grid shows (the same kind of rubric as Fame/Infamy; The Long Vigil is its Wild Child). The grid has one Grief range per companion, so a ledger needs a rule to produce it. Options: the highest entry only; the highest plus a small, shrinking bump per extra unresolved entry (recommended); a capped sum. **Deferred 2026-10-21: "we'll need to sort this out later."**

## 2 · Can Grief be resolved — decided 2026-10-21
**Grief itself is not reduced by a confrontation. An honest confrontation scene raises Bond instead.** (Developer: an honest confrontation scene can definitely exist; "instead of reducing Grief, what it does is increase Bond.") This matches the matrix's founding property that embracing who you are now does not require finishing grieving who you were, so **Grief entries stay in the ledger; progress is made on the Bond axis.**
- **Consequence:** the confrontation scene moves a companion toward the higher-Bond cells (Steadfast Mourner, Unwavering, The Long Vigil) without erasing the grief. It therefore does **not** cost the player The Long Vigil; it makes it more reachable.
- **Still to decide:** what deflecting does (nothing, or a small Bond loss); how big the Bond gain is; whether an acknowledged (confronted) entry counts differently toward the visible tier.

## 2a · What deflecting does — decided 2026-10-21
**Option A with a twist:** deflecting does nothing now, **but the companion remembers.** The scene can return later, harder to open. The player is never punished for not being ready (the tenderness safeguard), and can come back.

## 3 · Can Bond decay — decided 2026-10-21
**Option C: Bond drops only through specific events** (for example betraying a confidence, acting against the self the companion bonded with, abandoning them at a critical moment) and **never through the passage of time or neglect alone.** A Bond drop shifts the companion toward the cells where Grief outweighs Bond. Consistent with the Reputation decision that nothing fades just because time passes.

## 4 · Thresholds — decided 2026-10-21
Same principle as Reputation. **Bond:** each range threshold is a share of the Bond a companion or district can earn through their own content (questline, banter, romance beats, confrontation scenes). **Grief:** each range threshold is a share of the maximum Grief that companion could ever be seeded with (personality multiplier times full relationship depth); the Grief side waits for the deferred visible-tier rule. Numbers are filled in once the content exists.

## 5 · Secondhand discovery: how much Grief — decided 2026-10-21
**Option B, a soft weighting.** A companion who never knew a past configuration but discovers it through evidence in the world (items, testimony, records, Leyline chatter, other companions) is seeded at a **reduced rate** (for example half), with **no ceiling**. Finding out counts for less than living through the loss, but enough evidence can match it. Consequence: The Long Vigil is reachable through discovery, with its own flavor (possibly its own named cell or a footnote on the existing one).

## 6 · Player control over disclosure — decided 2026-10-21
**Option A: all three.** The player can **volunteer** the truth (the companion gets a firm ledger entry at once, weighted between discovered and firsthand, and it works like an honest conversation so it can raise Bond), **stay silent** (the companion discovers at the pace of the world), or **deny or obscure** it (a lie; if discovered later, it is an event that drops Bond). Fits the rule that Bond drops only through specific events and the no-costless-choices principle.

## 7 · How the investigation works — decided 2026-10-21
**Option C, a hybrid.** All five footprint sources are kept (items and records found in the world, NPC testimony, district records, Leyline chatter, other-companion banter). A **generic footprint system serves every companion**; **authored investigation threads exist only for companions whose personal questlines are developed enough to support them** (same judgment call as the Accomplishment Weight system). **Personalized footprints, decided yes:** footprints derive from what each past configuration actually did (its stored snapshot and biggest accomplishments), so they describe the player's real past selves.

## Deferred 2026-10-21
- **Personality multiplier values** for the remaining companions and districts, and whether an Enneagram-based formula can produce defaults: to be figured out later.
- **The companion Long Vigil perks:** to be figured out later.
- Also still open: the visible-tier rule; the glitching past perks in detail (trigger and frequency, what a glitch can do, readability, fixing or purging, the tie to IF states and echo events); how current and past perks conflict; the Bond gain from a confrontation scene; whether a confronted entry counts differently toward the visible tier.

## Fragmentation: all decisions made so far (summary) — 2026-10-21
Traits permanent, everything else re-specced at a cost, perks re-choosable; past perks glitch (more and harder if the requirement is also no longer met); Grief is a ledger (one entry per past configuration) and is never reduced; an honest confrontation scene raises Bond, and deflecting does nothing now but is remembered; Bond drops only through specific events; thresholds are shares of what is obtainable; secondhand discovery is seeded at a reduced rate with no ceiling (so The Long Vigil is reachable through it); the player can volunteer, stay silent or deny; the investigation is a generic footprint system plus authored threads for developed companions, with footprints personalized from each past self. **Edits to the real files applied 2026-10-21** (Fragmentation_Matrix.md, Fragmentation_Matrix_Expansion_Ideas.md, Player_Re-Spec_-_Complete_Design.md, TODO.md).

## Glitching perks: deferred — 2026-10-21
The details of the glitching past perks (trigger and frequency, what a glitch can do, readability, fixing or purging, the tie to IF states and echo events, and how current and past perks conflict) **wait until the perks themselves are defined**: the developer will figure them out once it is known what the perks actually are.
