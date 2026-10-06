# RESUME HERE: OOLSD library

**Written 2026-10-06 ~14:10, because the weekly allotment was at 99 % and the 5-hour window at 92 %. An interruption of
days is possible.** Read this file first. Update the status lines in place.

## Two threads are open. Do not mix them.

### Thread 1: the OOLSD library (this folder)
Developer-confirmed model: Classes, Instances, Late Binding. Read `README.md`, then `02_Design_Brief.md`.

| Done | File |
|---|---|
| ✅ | `README.md`, `01_Inventory_Universal_vs_Antarctic.md`, `02_Design_Brief.md`, `03_Pointer_Manifest.md`, `04_Handwave_Register.md` |
| ✅ | `research/_BRIEF.md` (the shared research brief; **final, never amended**) |
| ⏳ | Three research files, written by background agents. See below. |
| ⏸️ | The developer is downloading Isaac Arthur subtitle files into `research/_inputs/` (empty at 14:09). |

**Research agents (dispatched ~13:55 on 2026-10-06, same brief, one file each).** Each wrote its file first and appends
as it goes, so a stopped agent leaves usable material. At 14:09 the files held 99, 308 and 107 lines.

| File | Topic | Agent ID |
|---|---|---|
| `research/leo_and_orbital_habitats.md` | LEO, rotating habitats, microgravity, electronics and machines in vacuum | `a1df57f8b7829bfe9` |
| `research/mars_venus_and_transfer.md` | Mars, Venus, Earth–Mars and Earth–Venus transfer | `a5936119cee82df3e` |
| `research/belt_jupiter_saturn_and_deep_transit.md` | Belt, Jupiter, Saturn, propulsion, power | `aefab0ec44b5074a5` |

**On resume, for each file:**
1. Count what it holds against the brief's nine sections (Scope · SEARCH LOG · Findings · Conflicts · Derived · Constraints ·
   Candidate handwaves · Open threads · Rejected sources). A file with all nine and a closing line is **complete**.
2. **Incomplete, agent alive:** `SendMessage` to its agent ID: *"Resume: continue exactly the task in the brief from where
   your file ends. Nothing in the brief has changed."* That is a resume, not an amendment (`00_RUNBOOK.md` §C.2).
3. **Incomplete, agent gone:** re-dispatch that topic alone, with `_BRIEF.md` and the same checklist. Its own file tells it
   what is already covered. The topic checklists are in the dispatch prompts, summarized here:
   - **LEO file:** LEO environment and radiation; machines and electronics in vacuum; microgravity health; spin-gravity
     physics and the O'Neill cylinder, Stanford torus and Von Braun wheel concepts; delta-v and transport; space elevators
     and fountains.
   - **Mars/Venus file:** Mars surface, orbit and resources; Earth–Mars transfer; Venus surface and cloud layer; Earth–Venus
     transfer; terraforming figures (flag speculative).
   - **Belt/Jupiter/Saturn file:** Belt; Jupiter's radiation and moons; Saturn, Titan, Enceladus; deep transit and
     propulsion; power scaling; a short interstellar-precursor note.
4. **After all three are complete,** the orchestrator (not the agents) does the review:
   - read each file's *Candidate handwaves*, and propose each to the developer. Do **not** add any to `04_Handwave_Register.md`
     without a ruling;
   - read each file's *Conflicts* and *Open threads*;
   - **spot-check** a sample of the high-confidence figures by opening the cited source;
   - then, and only then, start filling class **invariants** in `02_Design_Brief.md` §1 (fields 4–7). **No figure enters a
     class that is not in a reviewed research file.**

## What to do next, in order, once research is complete

1. Review the three research files (above).
2. Add `research/_inputs/` material, if present: use it for scope and leads, and check every number against a primary
   source. Isaac Arthur is a secondary source.
3. Draft **one** class declaration end to end, to prove the template: suggested first = **O'Neill Cylinder** (canon stage 2,
   most research, and the least dependent on the neo-cultures). Show it to the developer before drafting more.
4. Work the `01_Inventory…` §4 list (the locnames check, STRIP of `03`'s address blocks, the "district" vocabulary, the
   four uninspected tools). These are mechanical and can be done at any hour.
5. Locate the file stating the Cryptograph Helix timeline and the Greater Tepenia outline (`03_Pointer_Manifest.md` §B, the
   largest gap).

## Open decisions (none blocks the above)

- **Type by era:** is a type change (Interstitial → Corridor) the same instance in a new frame, or a new instance?
- **Class granularity:** one class with the body as a slot, or a subclass per body? *Deliberately undecided; decide as we go.*
- **The Federation above orbit:** does any national layer sit above Mars instances in canon?
- **The inherited open items** in `02_Design_Brief.md` §5 (12 million versus 10,104,964; the human-heavy tilt).

## Standing rules (so a new session does not need to ask)

- **Pointers now, copies at handoff.** Consumer order: CurrentNovelDocs (LEO), Cryptograph Helix, later Outer Tepenia.
- **No physical figure from recall.** No named Mars nations, no demonyms, no stereotypes. Stock names come from Inner Tepenia's
  cities and subnets, never from present-day nations.
- **Physics fidelity:** only the enumerated handwaves are exempt (`04_Handwave_Register.md`). Nanotech gel-brain consciousness
  is the only one. A robot's body obeys physics.
- **Exodus phrasing:** a proportion of the population leaves, and *among those who leave*, most left in peacetime. It is not that
  most of the country left.
- **No level-scaling.** American English.
- **This folder is logistics, so it is any-hour work.** Deriving a *specific* location is not. That is the ULM, and it keeps its
  05:00–14:59 hours law.

## The other thread: Mirny, Step 4

**Phase 8 is done. Phase 9 (Populations) is next.** Its authority is `Universal_Location_Methodology/MASTER_Process_Tracker.md`,
`📍 RESUME HERE`. Say *"Continue the city run."* The Phase 8 checkpoint
(`…/Mirny_Subnet/Mirny/.t8_Phase8_CHECKPOINT.md`) is fully ticked. Phase 9 is **restricted-hours** work (05:00–14:59, wrap-up
13:59) and needs a fresh window.
**One pending item for the developer** from Phase 8: the axis was decided against the vote count, as "Prepared, not
predicted" (`04_Phase_08_Making.md`, Merge provenance and Snag 12). Their call if they prefer "Native at the door".
**Uncommitted:** everything written this session is in the working tree. Nothing is committed.
