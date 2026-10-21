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
