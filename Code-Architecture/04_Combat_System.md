# Combat System

Depends on `02_Objects_and_Data_Resources.md`'s `MachineStats` Resource.

---

## System Overview

```
CombatArena (scene root)
├── GridManager          — isometric grid, pathfinding, tile queries (C++, see 05_Grid_Movement_and_Camera.md)
├── TurnManager          — initiative order, turn cycling
├── CombatUILayer        — HUD, AP display, targeting overlay
└── Combatants (group)
    ├── PlayerCharacter
    └── EnemyCharacter (x N)
```

---

## APManager

Attached to each combatant. Manages the current AP pool per turn — a local Node, not global (see
`01_Global_State_and_Autoloads.md`'s global/local test: this belongs to one combatant, in one encounter, and
ceases to matter the moment that encounter ends).

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

---

## DamageCalculator (C++ via GDExtension)

The damage formula is performance-critical (called on every single attack, potentially many times per
combat round) and runs in C++ rather than GDScript — the one clear case in this whole architecture where the
"C++ only where it matters" principle actually applies.

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

---

## SignatureAbilityManager

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

---

## NODE Targeting System

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
