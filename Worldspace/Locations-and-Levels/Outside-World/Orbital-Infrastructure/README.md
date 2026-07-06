# Orbital Infrastructure

**Status: scaffolding only, established 2026-07-05 — this folder is context-setting for now, not yet developed at content depth.**

## Purpose

This folder is the single, shared source of truth for everything happening in Tepenian orbital space (low Earth orbit, primarily) — station types, population, key figures, and the timeline of how people got there. It exists to serve three separate downstream projects without duplicating the same lore three times:

1. **Inner Tepenia (this game)** — eventual in-game lore sources: audio logs, text entries, NPC dialogue about characters currently in orbit, conversations with NPCs whose friends or family escaped to orbit before or during the Long Night War.
2. **A planned novel series** — spans post-colonization of Mars through the frontier edges of colonizing Jupiter, heading toward eventually exploring (and colonizing) Saturn. Its founding population is explicitly the Tepenians already established here: the ~12 million who left during the later portion of the Second Interwar Period, plus however many escaped during the Long Night War itself.
3. **A planned TV series** — spans the entire Second Interwar Period (arrival on Antarctic shores through the Concordia refugee migration). A different, earlier slice of the timeline than either Inner Tepenia or the novel series, but drawing on the same orbital buildout history for its own later chapters.

The developer's plan: two new, separate GitHub repos (one per non-game project) will each pull from this same folder rather than maintaining their own copies of this lore.

## What already exists elsewhere (read these first)

This folder should build on, not duplicate, lore already established in the main GDD:

- **`Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md`** and related files — the 3-stage orbital build-out order: robot-only staging stations first, then O'Neill Cylinders as the primary long-term residence structure, then Von Braun Wheels as mobile/expansion-crew infrastructure (not a competing permanent-residence option). See `project_orbital_infrastructure_stages` memory.
- **`Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`, `Orbital_Infrastructure_Mass_Budget.md`, `Von_Braun_Wheel_Mass_Budget.md`, `Design_Efficiency_Comparison.md`** — the physical/engineering math already worked out: how Amundsen Tower moved people to orbit, station mass budgets, and design efficiency comparisons between structure types.
- **`Cities/Official_Population_Census.md`** — the actual population numbers this all has to be consistent with. As of the 2026-07-05 correction: Census II orbital population is **10,104,964 combined** (5,136,822 human / 4,968,142 robot, ~50.8% human / 49.2% robot) — about 31.6% of Tepenia's total population at the time the Long Night War began. This is the number the novel series' "12 million Second Interwar-era escapees" figure needs to be reconciled against (they aren't the same population — the 12M is specifically late-Second Interwar-period departures, a subset or a different accounting than the full pre-war orbital census; this reconciliation is itself an open item, see below).

## Still open — nothing below this line is decided yet

- Reconciling the "12 million Tepenians who left during the later Second Interwar Period" (novel series' founding figure) against the Census II orbital population (10,104,964) — same population counted differently, or genuinely different numbers? Needs a decision.
- What specific station types exist beyond the already-established three (staging stations, Cylinders, Wheels) — is that the complete list, or are there others by the novel series' much later timeframe (post-Mars-colonization)?
- Named/specific orbital settlements, if any — right now the lore only establishes structure *types*, not individual named locations analogous to Tepenia's Antarctic cities.
- Population national/ethnic composition of the orbital population — already a separate flagged task, see `TODO.md`'s "Orbital population — national/ethnic composition map" entry.
- Key figures/characters who are (or were) in orbit — none established yet.
- Timeline detail connecting Inner Tepenia's present-day (~2822–2827) to whatever later point the novel series' Mars-colonization era begins.

## Planned structure (not yet built)

Likely future files in this folder, once content development starts:
- Station types and architecture (expanding on Cylinders/Wheels/staging stations)
- Population and migration waves (who went up, when, and why — connecting Second Interwar-era voluntary migration to Long Night War evacuation)
- Notable orbital locations, if/when any get named
- Timeline bridging Inner Tepenia's present day to the novel series' much-later Mars/Jupiter/Saturn era

Nothing under "Planned structure" should be built out until the developer says so — this README exists to mark the folder's purpose and cross-reference what's already established, not to start inventing new content.
