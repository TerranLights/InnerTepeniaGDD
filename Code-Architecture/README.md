# Inner Tepenia — Code Architecture
**Engine: Godot 4.x | Languages: GDScript + C++ (GDExtension) | Status: pseudocode-level design, no implementation yet**

---

## What this folder is

This is Inner Tepenia's **code structure** — not code itself, but the level below it: what would
traditionally be called pseudocode. The game's own design docs (`Storyline/`, `Worldspace/`, `Game-Mechanics/`)
describe *what* the game is. This folder describes *how it would actually be built* — global vs. local state,
what the objects are and how they inherit from each other, where each system's logic would physically live in
the project's file tree, and how systems talk to each other at runtime.

Consolidated 2026-07-22 from four files that had accumulated separately in `General-Overview-Notes/`
(`Inner_Tepenia_Technical_Architecture.md`, `Inner_Tepenia_Camera_System_Architecture.md`,
`Inner_Tepenia_Reputation_Architecture_Supplement.md`, `Inner_Tepenia_Scalable_Graphics_and_Camera_Tiers.md`)
into one properly organized home, reorganized by system rather than by when each piece was written, with two
genuinely new files added (`01` and `02`) that answer the organizing questions directly rather than leaving
them implicit in scattered examples.

## How to read this folder

| File | Covers |
|---|---|
| `00_Overview_and_Project_Structure.md` | Guiding principles, the actual folder/file layout the Godot project itself would use |
| `01_Global_State_and_Autoloads.md` | What counts as global here, why, and the full Autoload roster + EventBus signal catalog |
| `02_Objects_and_Data_Resources.md` | What counts as an object, how inheritance works in this project, and every core Resource definition |
| `03_Character_System.md` | CharacterData, CharacterAppearance, the in-scene PlayerCharacter node |
| `04_Combat_System.md` | AP system, damage calculation (C++), signature abilities, NODE targeting |
| `05_Grid_Movement_and_Camera.md` | Hex+navmesh hybrid grid, pathfinding, the camera rig, movement feel |
| `06_World_District_and_Reputation_System.md` | DistrictManager, power grid, radio, the full reputation/hostility event system |
| `07_Save_System.md` | Save/load serialization |
| `08_Scalable_Graphics_and_Hardware_Tiers.md` | Four hardware tiers, camera-freedom scaling, graphics settings |
| `09_Build_Order_and_Key_Decisions.md` | The order systems get built in, and the rationale behind the biggest architectural calls |
| `10_Character_Asset_Pipeline.md` | DAZ Studio → Blender → Godot character asset pipeline; where rigging actually happens |
| `11_2D_Reference_to_3D_Character_Pipeline.md` | Converting the existing companion reference-image dolls into 3D models; AI image-to-3D tool landscape; relationship to the DAZ pipeline (open) |

## Standing rules for this folder

- **This is not implementation.** Nothing here should be treated as final, tested, or locked — it's a map for
  when actual coding starts, expected to be revised as real building surfaces problems no pseudocode pass can
  predict.
- **Data-driven, always.** Perks, skills, items, districts, abilities, and reputation events are Godot
  Resources (`.tres`), not hardcoded values — this is the single most load-bearing decision in the whole
  folder and every other file assumes it.
- **C++ only where profiling would actually justify it** — grid pathfinding and the damage formula are the
  two confirmed cases (hot paths called every frame or every attack). Everything else is GDScript by default;
  don't reach for GDExtension without a concrete performance reason.
- **Godot Fallout Precedence Law applies here too, loosely** — where a real technical decision needs a
  reference point and none exists yet, prefer whatever's simplest to build and revise later over a clever
  solution that's harder to change once real content is built on top of it.

## What's still missing (not yet covered by any file here)

This folder currently covers character stats, combat, the grid/camera/movement stack, world/district/
reputation state, saving, and graphics scaling — all migrated from prior work. **Not yet designed at all:**
the quest/dialogue system's own data structures and state tracking, the UI layer (menus, HUD, inventory,
character creation screens as actual scene/script structure), the perk/trait/ability *content* pipeline
beyond the Resource shape itself, companion-specific systems (approval, romance gates, personal
questlines as code), the Godot object field for Concordia-refugee sub-district tracking (blocked on
Sinheung/Shirayuki's final names per `TODO.md`), and the mod-facing JSON override loader. Extend this
folder with new numbered files as those get designed, following the same "what's global, what's an
object, where does it live, how does it get built" shape as the files already here.
