# Inner Tepenia — Technical Architecture Document
**Version 0.1 | Engine: Godot 4.x | Languages: GDScript + C++ (GDExtension)**

---

## 1. Overview & Guiding Principles

This document defines the technical blueprint for *Inner Tepenia* — how the game's systems are structured in code, how they communicate with each other, and in what order they should be built.

**Core principles:**
- Data-driven everywhere possible. Perks, skills, items, districts, and abilities are defined in Godot Resources (`.tres`), not hardcoded.
- Mod-friendly by design. Internal systems use Resources; mod-facing systems expose JSON loaders that override or extend base data.
- Build in layers. Each system must be testable in isolation before being wired to others.
- C++ only where it matters. Performance-critical inner loops (pathfinding, damage calculation, grid queries) live in GDExtension. Everything else is GDScript.

---

## 2. Project Structure

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
│   ├── skills/               # SkillResource .tres files
│   ├── traits/               # TraitResource .tres files
│   ├── items/                # ItemResource .tres files
│   ├── abilities/            # AbilityResource .tres files
│   ├── districts/            # DistrictResource .tres files
│   └── characters/           # CharacterResource .tres files (NPCs)
├── mods/                     # JSON override folder (mod-facing)
├── scenes/
│   ├── combat/               # CombatArena, GridManager, TurnManager
│   ├── ui/                   # HUD, CharacterCreation, Inventory, etc.
│   ├── world/                # Districts, transitions, player home
│   └── characters/           # Player, NPC, companion scenes
├── scripts/
│   ├── core/                 # GameState, EventBus, SaveManager
│   ├── character/            # CharacterStats, SkillSystem, PerkSystem
│   ├── combat/               # APManager, CombatManager, DamageCalc
│   ├── world/                # DistrictManager, FactionManager, RadioManager
│   └── ui/                   # All UI controllers
└── autoloads/                # Global singletons
```

---

## 3. Autoloads (Global Singletons)

These are always available everywhere in the game. Keep them lean.

| Autoload | Purpose |
|---|---|
| `GameState` | Current game phase, active scene, global flags |
| `EventBus` | Decoupled signal relay — systems talk through here |
| `SaveManager` | Save/load serialization |
| `DataManager` | Loads and caches all Resource (.tres) data |
| `AudioManager` | Music, SFX, district radio management |
| `DistrictManager` | Active district, faction reputations, power grid state |

---

# Inner Tepenia — Technical Architecture Document

**Version 0.2 | Engine: Godot 4.x | Languages: GDScript + C++ (GDExtension)**

---

## 1. Overview & Guiding Principles

... (existing content unchanged) ...

## 6. Character System

... (existing content unchanged) ...

## 7. World, Grid & Movement System

This section defines how the world is spatially represented, how characters move, and how the camera presents the game. The goal is to combine the tactical precision of classic CRPGs with the smooth, weighty motion of modern titles like *Baldur’s Gate 3* and *Wasteland 3*.

### 7.1 Core Philosophy
- **Tactical clarity** (grid-based AP costs, readable positioning, line-of-sight).
- **Modern motion feel** (smooth animations, intelligent pathing, responsive camera).
- **District personality** — the circular color-coded layout of Concordia should feel distinct and beautiful from the chosen camera perspective.

### 7.2 Grid System Recommendation: Hexagonal + Navmesh Hybrid

**Recommended approach**: Use a **hexagonal grid** as the logical/tactical layer combined with a **navmesh** for visual movement.

**Why Hex over Square?**
- Consistent distance between adjacent tiles (no diagonal penalty weirdness).
- More natural flanking and positioning in combat.
- Better suits the organic/sci-fi architecture of many districts (hydroponics, industrial clutter, Frostlands, undergrid tunnels).
- Cleaner AP calculations.

**How the Hybrid Works**
- **Hex Grid Layer** (logical/rules layer):
  - All AP costs, range calculations, line-of-sight, and tactical highlighting are based on clean hex tiles.
  - This keeps the system precise, speedrun-friendly, and easy to balance.
- **Navmesh Layer** (visual/feel layer):
  - A navigation mesh defines actual walkable space.
  - Characters follow smooth, curved, intelligent paths around obstacles (furniture, pipes, debris, other characters, hydroponic planters, etc.).
  - Movement *looks* fluid and modern (like BG3), but the **final AP cost** is snapped to the nearest valid hex tile count.
- **Result**: Beautiful, weighty animations + perfect tactical precision.

**Exploration vs Combat**
- **Exploration mode**: Real-time movement (WASD or click-to-move) with full fluid animation and navmesh pathing. No AP cost.
- **Combat mode**: Switches to strict turn-based AP system. Players see a glowing path preview with exact AP cost. Characters then execute the movement with smooth animation blending.

### 7.3 Camera System
- **Primary view**: Modern 3D isometric (rotatable around a central axis, similar to *Wasteland 3* with added smoothness).
- Players can freely orbit the party for cinematic district views while retaining strong tactical readability.
- Support for a dedicated **tactical top-down mode** (toggleable, similar to BG3’s “O” key) for precision during complex fights.
- Camera should support:
  - Smooth zooming and panning
  - Slight cinematic tilt
  - Height-aware following (ramps, undergrid entrances, multi-level districts)

## References to Detailed Systems

- **Movement, Camera & Grid System** → See [`Game-Mechanics/Core-Mechanics/Movement_Camera_and_Grid_System.md`](Movement_Camera_and_Grid_System.md)

### 7.4 Mitigating Straight Walls in Indoor Areas (Hex Grid Challenge)
Hex grids can look awkward with perfectly rectangular rooms. Recommended mitigations (in order of preference):

1. **Art-First Approach (Recommended)**  
   Build rooms with natural straight walls and rectangular shapes. The hex grid is an invisible or subtle overlay underneath. Walkable space is determined by whether the *center* of a hex lies inside the room. The navmesh handles precise collision.

2. **Grid Rotation**  
   Rotate the hex orientation per map so one flat side aligns with major wall directions where possible.

3. **Hybrid Grid Zones**  
   Use hex grid for organic/outdoor areas (Frostlands, gardens, undergrid) and switch to square grid (or offset “hexaquad” tiles) for very strict rectangular interiors if needed. Provide clear visual transitions.

4. **Design Philosophy**  
   Embrace slightly more organic or larger-scale interiors where it fits the lore (e.g., open medical wards in Cancer, cluttered factories in Capricorn). This plays to hex strengths while still allowing straight-walled rooms via the art-first method.

5. **Visual Polish**  
   Make the hex grid subtle or toggleable (“G” key). Use environmental details, floor patterns, and lighting to guide the eye rather than relying on visible grid lines.

### 7.5 Animation & Pathing Priorities
- High-quality animation blending and inverse kinematics (foot placement on uneven terrain, ramps, snow, etc.).
- Contextual animations (brushing snow, ducking under pipes, interacting with medical equipment, etc.).
- Excellent pathfinding that avoids other characters and dynamic obstacles.
- Pre-visualized movement paths with real-time AP cost display (like BG3).

### 7.6 Integration Points
- **DistrictResource** should include fields for preferred grid behavior or camera presets if needed.
- **CombatManager** and **APManager** read from the hex grid for costs.
- **DistrictManager** can influence pathfinding costs (e.g., difficult terrain in Frostlands or damaged areas during power crises).
- Save system must serialize current grid position (hex coordinates) + visual transform.

---

## 8. Next Implementation Priorities (Technical)

1. Core data resources (already started)
2. Character stats + AP system
3. Grid + Navmesh hybrid + basic movement
4. Camera system (rotatable isometric + tactical view)
5. Combat manager + damage calculation
6. District loading and transitions
7. Save/Load system

---

*Document will continue to evolve as systems are prototyped.*

---
# continuation of pre-update notes:
---

## 4. Data Resources

All game data is defined as typed Godot Resources. This enables editor inspection, type safety, and trivial save/load.

### 4.1 MachineStats Resource
```gdscript
class_name MachineStats extends Resource

@export var might: int = 5
@export var agility: int = 5
@export var calculation: int = 5
@export var humanity: int = 5
@export var investigation: int = 5
@export var nerve: int = 5
@export var engine: int = 5

func get_base_ap() -> int:
    return 6 + int(agility / 2.0)

func get_nerve_modifier() -> int:
    return int((nerve - 5) / 2.0)

func get_total_ap() -> int:
    return get_base_ap() + get_nerve_modifier()

func get_free_movement_tiles() -> int:
    return max(0, int((engine - 5) / 2.0))

func get_skill_points_per_level() -> int:
    var inv_modifier: int = _get_investigation_modifier()
    return max(3, 2 + int(calculation / 2.0) + int(nerve / 2.0) + inv_modifier)

func get_skill_max(governing_stat_value: int) -> int:
    return 30 + ((governing_stat_value - 1) * 10)

func get_base_dt() -> int:
    return int((engine * 2.5) + (might * 1.5))

func get_base_dr() -> int:
    return calculation * 2

func _get_investigation_modifier() -> int:
    match investigation:
        10: return 3
        8, 9: return 2
        6, 7: return 1
        5: return 0
        4: return -1
        2, 3: return -2
        1: return -3
    return 0
```

### 4.2 SkillResource
```gdscript
class_name SkillResource extends Resource

@export var id: StringName
@export var display_name: String
@export var description: String
@export var category: StringName  # "technical", "social", "combat", etc.
@export var governing_stats: Array[StringName]  # ["calculation", "investigation"]
@export var primary_stat: StringName  # Used for skill cap calculation
```

### 4.3 PerkResource
```gdscript
class_name PerkResource extends Resource

@export var id: StringName
@export var display_name: String
@export var description: String
@export var max_ranks: int = 1
@export var perk_type: StringName  # "level_up", "challenge", "unique"
@export var stat_requirements: Dictionary  # {"calculation": 7, "investigation": 6}
@export var skill_requirements: Dictionary  # {"arcanet_navigation": 55}
@export var effects: Array[PerkEffect]
```

### 4.4 TraitResource
```gdscript
class_name TraitResource extends Resource

@export var id: StringName
@export var display_name: String
@export var description: String
@export var bonuses: Array[StatModifier]
@export var penalties: Array[StatModifier]
@export var bonus_description: String
@export var penalty_description: String
```

### 4.5 AbilityResource (Signature Abilities)
```gdscript
class_name AbilityResource extends Resource

@export var id: StringName
@export var display_name: String
@export var governing_stat: StringName  # "agility", "might", "calculation"
@export var base_duration_turns: int
@export var after_effect_turns: int
@export var ap_cost: int
@export var effects: Array[AbilityEffect]
@export var after_effects: Array[AbilityEffect]
@export var humanity_modifies_severity: bool = true
```

### 4.6 DistrictResource
```gdscript
class_name DistrictResource extends Resource

@export var id: StringName
@export var display_name: String
@export var archetype: StringName  # "nurturing", "industrial", etc.
@export var zodiac: StringName     # "cancer", "aries", etc.
@export var ally_districts: Array[StringName]
@export var rival_districts: Array[StringName]
@export var radio_genre: String
@export var armor_style: StringName
@export var respec_method_id: StringName
@export var power_grid_priority: int  # 1-12, used in energy crisis calculations
```

---

## 5. Character System

### 5.1 CharacterData (the master record)
```gdscript
class_name CharacterData extends Resource

@export var character_name: String
@export var is_player: bool = false
@export var machine_stats: MachineStats
@export var skills: Dictionary  # {skill_id: current_value}
@export var tagged_skills: Array[StringName]
@export var traits: Array[StringName]
@export var perks: Dictionary  # {perk_id: current_rank}
@export var level: int = 1
@export var current_hp: float
@export var max_hp: float
@export var current_integrity: float  # Identity Fragmentation meter (0-100)
@export var active_signature_ability: StringName = ""
@export var appearance: CharacterAppearance
@export var district_reputations: Dictionary  # {district_id: reputation_value}
```

### 5.2 CharacterAppearance (body customization)
```gdscript
class_name CharacterAppearance extends Resource

# Morph target values (0.0 - 1.0)
@export var breast_size: float = 0.5
@export var bust_width: float = 0.5
@export var waist_size: float = 0.5
@export var hip_size: float = 0.5
@export var leg_length: float = 0.5
@export var leg_thickness: float = 0.5
@export var shoulder_width: float = 0.5
@export var face_preset: int = 0

# Equipment slots
@export var head_slot: StringName = ""
@export var torso_slot: StringName = ""
@export var legs_slot: StringName = ""
@export var feet_slot: StringName = ""
@export var accessory_slot: StringName = ""

# Chassis colors and markings
@export var primary_color: Color = Color.WHITE
@export var secondary_color: Color = Color.GRAY
@export var marking_pattern: int = 0
```

### 5.3 CharacterBody3D (the in-scene node)
The scene node reads from `CharacterData` and applies morph targets:
```gdscript
class_name PlayerCharacter extends CharacterBody3D

@export var character_data: CharacterData
@onready var mesh_instance: MeshInstance3D = $MeshInstance3D
@onready var animation_tree: AnimationTree = $AnimationTree

func _ready() -> void:
    apply_appearance(character_data.appearance)

func apply_appearance(appearance: CharacterAppearance) -> void:
    var mesh = mesh_instance.mesh as ArrayMesh
    mesh_instance.set_blend_shape_value(
        mesh.find_blend_shape_by_name("breast_size"), appearance.breast_size)
    mesh_instance.set_blend_shape_value(
        mesh.find_blend_shape_by_name("hip_size"), appearance.hip_size)
    # ... all other morph targets
    _apply_equipment(appearance)

func _apply_equipment(appearance: CharacterAppearance) -> void:
    # Swap equipment mesh children based on slot values
    pass
```

---

## 6. Combat System

### 6.1 System Overview

```
CombatArena (scene root)
├── GridManager          — isometric grid, pathfinding, tile queries
├── TurnManager          — initiative order, turn cycling
├── CombatUILayer        — HUD, AP display, targeting overlay
└── Combatants (group)
    ├── PlayerCharacter
    └── EnemyCharacter (x N)
```

### 6.2 APManager
Attached to each combatant. Manages the current AP pool per turn.

```gdscript
class_name APManager extends Node

signal ap_changed(current: int, maximum: int)
signal turn_started(ap: int)

var current_ap: int = 0
var maximum_ap: int = 0
var free_movement_tiles: int = 0

func initialize(stats: MachineStats) -> void:
    maximum_ap = stats.get_total_ap()
    free_movement_tiles = stats.get_free_movement_tiles()

func start_turn() -> void:
    current_ap = maximum_ap
    emit_signal("turn_started", current_ap)

func spend(amount: int) -> bool:
    if current_ap < amount:
        return false
    current_ap -= amount
    emit_signal("ap_changed", current_ap, maximum_ap)
    return true

func end_turn() -> void:
    current_ap = 0
```

### 6.3 DamageCalculator (C++ via GDExtension)
The damage formula is performance-critical and runs in C++:

```cpp
// tepenia_core/damage_calculator.cpp
static float calculate_final_damage(
    float base_damage,
    float dr,           // as percentage 0-100
    float dt,
    float penetration_flat,
    float penetration_percent
) {
    // Apply flat penetration
    float effective_dt = max(0.0f, dt - penetration_flat);
    // Apply percentage bypass
    effective_dt *= (1.0f - penetration_percent);
    // Cap DR at 85%
    float capped_dr = min(dr, 85.0f);
    // Apply DR then DT
    float after_dr = base_damage * (100.0f - capped_dr) / 100.0f;
    float after_dt = after_dr - effective_dt;
    // Apply 15% floor
    float minimum = base_damage * 0.15f;
    return max(after_dt, minimum);
}
```

GDScript calls this via the GDExtension binding:
```gdscript
var final_damage = TepeniaDamage.calculate_final_damage(
    base_damage, target_dr, target_dt,
    weapon.penetration_flat, weapon.penetration_percent
)
```

### 6.4 SignatureAbilityManager
```gdscript
class_name SignatureAbilityManager extends Node

var active_ability: AbilityResource = null
var turns_remaining: int = 0
var in_after_effect: bool = false
var after_effect_turns_remaining: int = 0

func activate(ability: AbilityResource, stats: MachineStats) -> void:
    active_ability = ability
    var humanity_factor = _get_humanity_factor(stats.humanity)
    turns_remaining = ability.base_duration_turns + humanity_factor.duration_bonus
    in_after_effect = false
    _apply_effects(ability.effects, stats, humanity_factor)

func on_turn_end() -> void:
    if active_ability == null:
        return
    if not in_after_effect:
        turns_remaining -= 1
        if turns_remaining <= 0:
            in_after_effect = true
            after_effect_turns_remaining = active_ability.after_effect_turns
            _apply_effects(active_ability.after_effects, null, null)
    else:
        after_effect_turns_remaining -= 1
        if after_effect_turns_remaining <= 0:
            _clear_ability()

func _get_humanity_factor(humanity: int) -> Dictionary:
    # Higher humanity = more stable, reduced after-effects
    # Lower humanity = more power, worse after-effects (Hardcore Mode)
    if humanity >= 8:
        return {"duration_bonus": 1, "power_multiplier": 0.85, "after_effect_reduction": 0.5}
    elif humanity <= 3:
        return {"duration_bonus": -1, "power_multiplier": 1.25, "after_effect_reduction": -0.5}
    return {"duration_bonus": 0, "power_multiplier": 1.0, "after_effect_reduction": 0.0}
```

### 6.5 NODE Targeting System
```gdscript
class_name NODETargetingSystem extends Node

signal target_selected(target: Node, body_part: StringName, hit_chance: float)
signal targeting_cancelled()

var is_active: bool = false
var processing_cycles_cost: int = 0

func activate(attacker_stats: MachineStats) -> void:
    is_active = true
    # Slow time / enter focused analysis mode
    Engine.time_scale = 0.2
    _scan_for_weak_points(attacker_stats)

func calculate_hit_chance(
    attacker: MachineStats,
    weapon_skill: int,
    body_part: StringName,
    distance: float
) -> float:
    var base = (attacker.investigation * 4) + (attacker.calculation * 2)
    var agility_bonus = int(attacker.agility * 0.5)
    var nerve_bonus = int((attacker.nerve - 5) * 1.5)
    var body_part_penalty = _get_body_part_penalty(body_part)
    var distance_penalty = int(distance * 2.0)
    return clampf(
        base + agility_bonus + nerve_bonus + weapon_skill - body_part_penalty - distance_penalty,
        5.0, 95.0
    )

func calculate_cycle_cost(body_part: StringName, distance: float, attacker: MachineStats) -> int:
    var base_cost = _get_base_cost(body_part)
    var distance_mod = int(distance * 0.5)
    var investigation_discount = int(attacker.investigation * 0.3)
    return max(1, base_cost + distance_mod - investigation_discount)

func _get_body_part_penalty(body_part: StringName) -> int:
    match body_part:
        "head_sensor": return 25
        "power_core": return 30
        "neural_core": return 35
        "torso": return 0
        "joints": return 15
        "limbs": return 10
        "weak_point": return -10  # bonus for scanned weak points
    return 0

func deactivate() -> void:
    is_active = false
    Engine.time_scale = 1.0
```

---

## 7. Grid System (C++ via GDExtension)

The isometric grid and pathfinding run in C++ for performance:

```cpp
// tepenia_core/grid_manager.cpp
class GridManager : public Node {
    // A* pathfinding on isometric grid
    // Tile queries: is_walkable, get_cover_value, get_tile_type
    // AP cost calculation for movement paths
    // Line-of-sight checks for targeting
};
```

GDScript interface:
```gdscript
# Get movement path and AP cost
var result = GridManager.find_path(from_tile, to_tile, free_tiles)
var path: Array[Vector2i] = result.path
var ap_cost: int = result.ap_cost

# Check line of sight
var has_los: bool = GridManager.has_line_of_sight(attacker_pos, target_pos)
```

---

## 8. World & District System

### 8.1 DistrictManager (Autoload)
```gdscript
class_name DistrictManager extends Node

# Reputation: -100 (Hated) to +100 (Idolized)
var reputations: Dictionary = {}  # {district_id: int}
var power_grid: PowerGridState
var identity_fragmentation: float = 0.0  # 0-100, increases with re-specs

func get_reputation(district_id: StringName) -> int:
    return reputations.get(district_id, 0)

func modify_reputation(district_id: StringName, delta: int) -> void:
    reputations[district_id] = clampi(
        reputations.get(district_id, 0) + delta, -100, 100)
    # Ripple to allied/rival districts
    var district = DataManager.get_district(district_id)
    for ally in district.ally_districts:
        reputations[ally] = clampi(
            reputations.get(ally, 0) + int(delta * 0.3), -100, 100)
    for rival in district.rival_districts:
        reputations[rival] = clampi(
            reputations.get(rival, 0) - int(delta * 0.2), -100, 100)
    EventBus.emit_signal("reputation_changed", district_id)

func add_identity_fragmentation(amount: float) -> void:
    identity_fragmentation = clampf(identity_fragmentation + amount, 0.0, 100.0)
    EventBus.emit_signal("fragmentation_changed", identity_fragmentation)
    if identity_fragmentation >= 75.0:
        EventBus.emit_signal("fragmentation_critical")
```

### 8.2 PowerGridState
```gdscript
class_name PowerGridState extends Resource

# 0.0 = no power, 1.0 = full power, per district
@export var district_power: Dictionary = {}
@export var grid_stability: float = 1.0  # Global stability 0-1
@export var blackout_active: bool = false

func allocate_power(district_id: StringName, amount: float) -> void:
    district_power[district_id] = clampf(amount, 0.0, 1.0)
    _recalculate_stability()
    EventBus.emit_signal("power_grid_changed", district_id, amount)

func _recalculate_stability() -> void:
    var total_allocated = district_power.values().reduce(func(a, b): return a + b, 0.0)
    var max_output = 12.0  # One unit per district at full power
    grid_stability = clampf(1.0 - (total_allocated / max_output - 0.8), 0.0, 1.0)
```

### 8.3 RadioManager
```gdscript
class_name RadioManager extends Node

var current_station: StringName = ""
var district_stations: Dictionary = {}  # Loaded from DistrictResources

func enter_district(district_id: StringName) -> void:
    var district = DataManager.get_district(district_id)
    _fade_to_station(district.id)

func _fade_to_station(district_id: StringName) -> void:
    AudioManager.crossfade_music(
        district_stations.get(district_id),
        1.5  # fade duration seconds
    )
    current_station = district_id
```

---

## 9. Save System

```gdscript
class_name SaveManager extends Node

const SAVE_PATH = "user://saves/"
const SAVE_VERSION = 1

func save_game(slot: int) -> void:
    var save_data = {
        "version": SAVE_VERSION,
        "timestamp": Time.get_unix_time_from_system(),
        "character": _serialize_character(),
        "world": _serialize_world(),
        "flags": GameState.global_flags,
    }
    var file = FileAccess.open(SAVE_PATH + "slot_%d.sav" % slot, FileAccess.WRITE)
    file.store_string(JSON.stringify(save_data))

func _serialize_character() -> Dictionary:
    var cd = GameState.player_character_data
    return {
        "machine_stats": _stats_to_dict(cd.machine_stats),
        "skills": cd.skills,
        "tagged_skills": cd.tagged_skills,
        "traits": cd.traits,
        "perks": cd.perks,
        "level": cd.level,
        "current_hp": cd.current_hp,
        "integrity": cd.current_integrity,
        "reputations": cd.district_reputations,
        "appearance": _appearance_to_dict(cd.appearance),
        "identity_fragmentation": DistrictManager.identity_fragmentation,
    }
```

---

## 10. EventBus Signals

All cross-system communication goes through the EventBus autoload:

```gdscript
class_name EventBus extends Node

# Combat
signal combat_started(combatants: Array)
signal combat_ended(result: StringName)
signal turn_changed(active_combatant: Node)
signal damage_dealt(target: Node, amount: float, damage_type: StringName)
signal combatant_defeated(combatant: Node)

# Character
signal level_up(new_level: int)
signal perk_unlocked(perk_id: StringName)
signal skill_increased(skill_id: StringName, new_value: int)
signal respec_completed(method: StringName)
signal appearance_changed()

# World
signal district_entered(district_id: StringName)
signal reputation_changed(district_id: StringName)
signal power_grid_changed(district_id: StringName, new_value: float)
signal blackout_started()
signal blackout_ended()
signal fragmentation_changed(value: float)
signal fragmentation_critical()

# Story
signal quest_updated(quest_id: StringName, stage: StringName)
signal faction_relationship_changed(faction_id: StringName, new_value: int)
signal major_choice_made(choice_id: StringName)
```

---

## 11. Build Order

Build these systems in sequence. Each must be testable before the next begins.

### Phase 1 — Foundation (Learn Godot)
1. Godot orientation: scenes, nodes, signals, GDScript basics
2. Simple isometric tilemap prototype (movement only, no combat)
3. Basic GDExtension hello-world (get C++ pipeline working)

### Phase 2 — Character System
4. `MachineStats` resource + stat allocation UI
5. Skill point calculation, skill cap system
6. Tag skill selection
7. Trait selection
8. Character Creation screen (end-to-end flow)
9. `CharacterAppearance` + morph target application in-scene

### Phase 3 — Combat Core
10. `GridManager` (C++): grid representation, pathfinding, LOS
11. `APManager`: turn start, spend, discard at end of turn
12. `TurnManager`: initiative, turn cycling
13. `DamageCalculator` (C++): full DT/DR formula
14. Basic attack flow (move → attack → damage → next turn)
15. Armor and chassis system
16. `NODETargetingSystem`: body part selection, hit chance, cycle cost

### Phase 4 — Combat Depth
17. `SignatureAbilityManager`: Framejacking, Rage, Overclock
18. Ammo types and penetration
19. Status effects (Joint Lock, Overheat, EMP, etc.)
20. Perks that interact with combat

### Phase 5 — World Systems
21. `DistrictManager`: reputation, ripple effects
22. `PowerGridState`: allocation, stability, blackout
23. `RadioManager`: per-district music crossfade
24. District scene transitions

### Phase 6 — Re-Spec System
25. Identity Fragmentation meter
26. Calethina's Lab (base re-spec)
27. District-specific re-spec methods
28. Visual/audio feedback per method
29. NPC reaction hooks

### Phase 7 — Content & Polish
30. Quest system scaffolding
31. Dialogue system
32. Save/load
33. Main story structure (Act 1 → Climax)
34. Mod JSON loader (override/extend base Resources)

---

## 12. Key Technical Decisions & Rationale

| Decision | Rationale |
|---|---|
| Godot Resources over JSON internally | Type safety, editor inspection, native serialization |
| JSON for mod-facing data | Human-readable, no engine dependency for modders |
| C++ for grid + damage | Hot paths called every frame/every attack — GDScript too slow |
| EventBus for cross-system signals | Decouples systems; district reputation change doesn't need to know about UI |
| `CharacterData` as a Resource | Trivially serializable for save/load; passable between scenes |
| Morph targets for body customization | Industry-standard approach; GPU-efficient; works with any armor layered on top |
| Separate `PowerGridState` resource | Encapsulates the core story mechanic; easy to serialize and query |
| Identity Fragmentation in `DistrictManager` | It's a world-state value, not a character stat — it persists across re-specs by design |

---

*This document should be committed to the GDD repo and updated as implementation decisions are made.*
