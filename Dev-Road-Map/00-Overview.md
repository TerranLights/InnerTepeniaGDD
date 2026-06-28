# Inner Tepenia — Development Roadmap

## What This Is

A structured development roadmap for the Inner Tepenia GDD, derived from a full-repository audit (June 2026) cross-referenced against design principles from Fallout 1, Fallout 2, and Fallout: New Vegas.

This roadmap covers GDD work only — it is not a production or implementation plan. It orders and prioritizes the design documents, decisions, and written content that remain before the GDD is complete enough to hand to an implementation team. Every item here is writing, design thinking, or a decision — not code.

---

## How to Read This

**The roadmap is split into seven phases**, each in its own file:

| File | Phase | What It Covers |
|------|-------|----------------|
| `02-Blocking-Decisions.md` | Pre-Phase | Three decisions that must be made before anything else |
| `03-Phase-1-Foundations.md` | Phase 1 | Fix tentative systems; establish naming conventions everything else depends on |
| `04-Phase-2-Factions-and-Spirituality.md` | Phase 2 | Robot religions (5) + faction design (9); these gate the endings |
| `05-Phase-3-Characters.md` | Phase 3 | All named character completion — scaffold characters and TBN characters |
| `06-Phase-4-Perks.md` | Phase 4 | Perk system completion — all six missing perk categories |
| `07-Phase-5-Quests-and-Story.md` | Phase 5 | Calethina questline, Planetary Split Brain, main story completion, side content |
| `08-Phase-6-World-Depth.md` | Phase 6 | Pre-war city culture, Long Night War parameters, historical detail |
| `09-Phase-7-Long-Term.md` | Phase 7 | DLC planning, deferred world-building, polish |

The **Fallout Design Reference** (`10-Fallout-Design-Reference.md`) is a design analysis document, not a phase. Consult it when working on any specific system to check how Fallout handled it and what Inner Tepenia should adopt, adapt, or reject.

The **Completion Matrix** (`01-Completion-Matrix.md`) is the single-source status table. Update it as work is completed.

---

## Current State (June 2026 Audit)

**Overall completion: ~50–55%** of GDD content written to final or near-final quality.

What is solid:
- All 13 Concordia district designs (cultural texture, history, architecture, inter-district dynamics)
- MACHINE stat system and skill list (44 skills) — with the exception of Might and Nerve (marked TENTATIVE)
- Action points, progression formula, traits, character creation framework
- Main story structure (Acts 1–3 with 10 beats, branching paths)
- Endings framework (all 6 categories; 3 of 12 Faction Devotion endings finalized)
- 6 companion characters with complete profiles, backstories, and questlines
- Minmax build framework (all 35 MACHINE stat combinations mapped)
- Eyes of Gold faction (fully designed)
- District Quest NPCs (44 NPCs across 13 district quests)
- District Internal Conflict Quests, Consequence Web, Unity of Opposites

What is incomplete, in priority order:
1. Three blocking decisions (see `02-Blocking-Decisions.md`)
2. Might/Nerve stat design (TENTATIVE)
3. 7 district proper names (in-world signage names for Cancer, Taurus, Leo, Scorpio, Aries, Capricorn, Libra)
4. Robot religions (5 named, none fully designed)
5. 9 faction designs (block 9 of 12 Faction Devotion endings)
6. 11 TBN characters (named only, no personality or questlines)
7. 6 scaffold characters (backstory exists, personality and voice absent)
8. Perk system (61/160 level-up perks; 5 of 7 earned perk categories not yet created)
9. Calethina questline (deliberately deferred)
10. Planetary Split Brain questline
11. Pre-war city culture (5+ cities need cultural sketches)
12. Long Night War historical parameters

---

## Guiding Principles for This Roadmap

### Order follows dependency
Nothing in a later phase should be designed before the things it depends on. Faction questlines cannot be written until factions are designed. Companion perks cannot be written until companion questlines are complete. The order is not arbitrary.

### The robot experience is the north star
The two creative principles governing all the creator's work: **what is the nature of consciousness among robots** and **what is the nature of love between robots and humans**. Every design decision should be evaluated against these — not as a checklist, but as the philosophical water the work swims in. When a design choice has multiple equally valid options, choose the one that gives the robot experience more texture and specificity.

### Bittersweet-only
No clean resolutions. The Unity of Opposites principle governs all conflict design. When a faction is designed, the question is not "what do they want" but "what do they need that only their opposition can provide." When a quest is written, the question is not "what is the good ending" but "what is the best outcome that is still bittersweet."

### Fallout New Vegas wins on conflicts
When Fallout 1/2 and FNV design approaches conflict, FNV is canonical reference. See `10-Fallout-Design-Reference.md` for specific guidance on quest structure, dialogue, perks, faction design, and companion design.

### Systems before content
A perk that references a system that isn't finalized is a perk that will need to be rewritten. A quest that references a faction that isn't designed is a quest built on sand. Systems and frameworks before the content that fills them.

---

## Dependencies Map

```
Blocking Decisions
    └── Phase 1 (Foundations)
            ├── Phase 2 (Factions + Spirituality)
            │       ├── Phase 3 (Characters) ← also depends on Phase 1
            │       ├── Phase 4 (Perks) ← also depends on Phase 3
            │       └── Phase 5 (Quests + Story) ← depends on Phase 2 + 3
            └── Phase 6 (World Depth) ← can run parallel to Phase 3–5
Phase 7 (Long-Term) ← depends on Phase 5 + 6
```

Phases 3 and 4 can be worked on in parallel once Phase 2 begins. Phase 6 can be worked on concurrently with Phases 3–5. Phase 7 is strictly last.
