# Reputation system — decisions log

**Started 2026-10-18.** Developer rulings from working through the open reputation questions one at a time. The base file is `Reputation_System.md` (the two-axis Fame/Infamy grid and the merchant discounts). **All six decisions were applied to `Reputation_System.md` on 2026-10-18.**

**Reference (Fallout: New Vegas, from the fallout wiki):** two cumulative counters, Fame and Infamy; actions worth 1, 2, 4, 7 or 12 points (very minor to very major); each faction sets its own range thresholds (for example 15/50/100 for Caesar's Legion, 2/5/10 for the White Glove Society), scaled to how much content it offers; points cannot be removed except through a few special resets for three factions.

## Agenda
1. Scope (what has a reputation) · 2. Earning and losing · 3. Thresholds · 4. Spread between districts · 5. Removal · 6. Presentation and tier names

## 1 · Scope — decided 2026-10-18
**Option B: per district AND per major cross-district group.**
- Every Concordia district has its own Fame and Infamy (plus each DLC city or region).
- A short list of **non-geographical groups** also has its own Fame and Infamy, so that helping or harming a group that exists across districts is rewarded or punished.
- **Rejected:** districts only (too simplistic; it cannot reward or punish choices about non-geographical groups) and per-faction for everything, which would be a copy of Fallout: New Vegas and would disrupt the cohesion and internal consistency of the world (developer's reasoning).
- **The rule for which groups get a track:** a cross-district group gets its own Fame and Infamy only once it is a **confirmed faction with real quests and real choices attached.**
- **The list itself is deliberately left open.** The developer will not create or finalize factions until the whole ULM/CST/RWBEM process is finished for the entire country and then for all the districts of Concordia, then create factions together from that data. Reason: the current faction list is extremely small, and new information tends to get forced into existing factions. So the existing faction files (Eyes of Gold, Veilkeepers and so on) are not treated as the list.

## 2 · Earning and losing — decided 2026-10-18
A combination of the first four proposals; the fifth is wanted but needs more attention later.
1. **Five size tiers, Fallout-style** (very minor, minor, average, major, very major). The exact point values per tier **depend on the context of the situation** and may differ (not necessarily 1/2/4/7/12 everywhere).
2. **Each quest outcome and deed names the districts (and groups) it affects, with a size for each.** Points are not credited only to where the deed happened (for example, a Capricorn disruption can cost reputation with Cancer and Taurus).
3. **Witness rule:** crimes and hacks add Infamy only when someone sees them or they are traced (consistent with the traceability rules). Unseen acts add no Infamy.
4. **Both counters can rise at once:** an action can add Fame to one district and Infamy to another, or both to the same one (the Libra example).
5. **Modifiers (skills, traits, perks scale gains by percentage, "whichever is higher: +1 or n%")** — liked in principle, **deferred**: needs more attention on how exactly it would be implemented.

## 3 · Thresholds — decided 2026-10-18
**Option C: thresholds are set as shares of what each district (or group) can actually give**, for example Range 1 at about 15%, Range 2 at about 45%, Range 3 at about 80% of the total obtainable points. The real numbers are filled in once each district's content is written. Note: Range 0 means "below the first threshold," so the first Infamy threshold acts as a district's tolerance for misbehavior before Idolized is lost.
**Whether Fame and Infamy thresholds may differ within a district: undecided.** Looked at later in design and development (developer: "not totally sure yet").

## 4 · Spread between districts — decided 2026-10-18
**Option C: designer-tagged word of mouth.** There is no automatic spread rule. A deed can be tagged "word travels," meaning it also reaches named districts at reduced value; in the story, Leyline chatter carries the news (Leyline, the national social network, still has no designed mechanism). Everything else stays within the districts a deed names (decision 2).

## 5 · Removal — decided 2026-10-18
**Option B: rare, designed atonement.** Reputation does not decay with time and cannot be bought off. A few specific, costly, story-gated acts (for example one per district, tied to that district's own questline) can drop the Infamy range by one step, and they leave a visible mark so the history is not erased. Rejected: permanent with no exceptions, and time decay. **The developer notes this will need an enormous amount of additional design, planning, world-building and story writing, and judges it an excellent addition to the game.** The atonement acts are written along with each district's content; for now only the principle is recorded.

## 6 · Presentation and tier names — decided 2026-10-18
- **Presentation: Option A.** The player sees tier names per district and group, never raw points; dialogue, prices and attitudes carry the rest. (Raw numbers may exist in a debug view for testing.)
- **Tier names: keep the Fallout: New Vegas names for now,** to be gone over again later (added to the later rename pass).

## Still open after this session
Whether Fame and Infamy thresholds differ within a district; the percentage modifiers (decision 2, item 5); the actual point values per tier in each context; the atonement acts (one per district, with a visible mark); the cross-district group list (waits for faction creation after the ULM/CST/RWBEM process); the exact UI; whether the player can see a "how close" hint (not chosen); whether the tier names are reskinned.

## All six decisions made and applied 2026-10-18.
