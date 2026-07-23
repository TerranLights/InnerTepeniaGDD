# Overview & Project Structure

---

## Guiding Principles

- **Data-driven everywhere possible.** Perks, skills, items, districts, abilities, and reputation events are
  defined in Godot Resources (`.tres`), not hardcoded. A designer or modder should be able to add or tune
  content without touching a script.
- **Mod-friendly by design.** Internal systems use Resources; mod-facing systems expose JSON loaders that
  override or extend base data (see `09_Build_Order_and_Key_Decisions.md` for where this lands in the build
  order — it's a Phase 7 concern, not a foundation-phase one).
- **Build in layers.** Each system must be testable in isolation before being wired to others — the AP system
  should work with a dummy stat block before it's wired to real combat; the camera should work on an empty
  gray-box level before real environments exist.
- **C++ only where it matters.** Performance-critical inner loops — pathfinding, damage calculation, grid
  queries — live in GDExtension. Everything else is GDScript.

---

## Project Structure

This is the actual Godot project's file tree, not this GDD repo's own structure — a separate project entirely,
once building starts.

```
InnerTepenia/
├── addons/                   # GDExtension C++ library (compiled)
│   └── tepenia_core/
├── assets/
│   ├── audio/                # Music, SFX, radio streams by district
│   ├── characters/           # Base meshes, rigs, morph targets
│   ├── environments/         # District tilemaps, tilesets
│   └── ui/                   # Fonts, icons, theme resources
├── data/
│   ├── perks/                # PerkResource .tres files
│   ├── skills/                # SkillResource .tres files
│   ├── traits/                # TraitResource .tres files
│   ├── items/                 # ItemResource .tres files
│   ├── abilities/              # AbilityResource .tres files
│   ├── districts/              # DistrictResource .tres files
│   ├── reputation_events/      # ReputationEvent .tres files
│   └── characters/             # CharacterResource .tres files (NPCs)
├── mods/                      # JSON override folder (mod-facing)
├── scenes/
│   ├── combat/                # CombatArena, GridManager, TurnManager
│   ├── ui/                    # HUD, CharacterCreation, Inventory, etc.
│   ├── world/                 # Districts, transitions, player home
│   └── characters/            # Player, NPC, companion scenes
├── scripts/
│   ├── core/                  # GameState, EventBus, SaveManager
│   ├── character/              # CharacterStats, SkillSystem, PerkSystem
│   ├── combat/                 # APManager, CombatManager, DamageCalc
│   ├── world/                  # DistrictManager, FactionManager, RadioManager
│   └── ui/                     # All UI controllers
└── autoloads/                 # Global singletons
```

This tree is the reference every other file in this folder assumes when it says where something "lives" —
e.g. `01_Global_State_and_Autoloads.md`'s autoloads live in `autoloads/` and `scripts/core/`; a `DistrictResource`
lives in `data/districts/`.
