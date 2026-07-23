# Objects & Data Resources

---

## What counts as an "object" here, and the two shapes it takes

Godot doesn't have a single universal "object" the way some engines do — everything ultimately inherits from
Godot's base `Object` class, but in practice this project only ever uses two concrete shapes, and picking the
right one for a given piece of data is one of the more consequential decisions in this whole architecture:

**`Resource`** — pure data, no presence in the scene tree, no `_process()` loop. A `Resource` is what
something *is*: a district's stats, a perk's requirements, a character's full stat block. Resources are
trivially serializable (this is what makes save/load simple — see `07_Save_System.md`), can be inspected and
edited directly in the Godot editor as `.tres` files, and can be shared by reference (many NPCs can point at
the same `PerkResource` without duplicating it). **Every piece of game content — perks, skills, traits,
abilities, districts, reputation events, and a character's full stat/data block — is a Resource.** This is
the single most load-bearing convention in the project: it's what "data-driven everywhere possible" (see
`00_Overview_and_Project_Structure.md`) actually means in practice.

**`Node` (and its 3D/2D variants)** — has a presence in the scene tree, can run `_process()`/`_physics_process()`
every frame, can have children, can be positioned in the world. A Node is what something *does* or *is doing
right now*: `APManager` (manages a live AP pool during an active turn), `CameraController` (an actual object
in the 3D scene), `NPCCombatState` (a specific NPC's live hostility state machine). **Systems, live game
state, and anything with a physical presence in the world are Nodes.**

**The practical rule used throughout this folder:** if it needs to be saved, edited by a designer, or shared
identically across many instances, make it a `Resource`. If it needs to run logic every frame, hold a
scene-tree position, or manage something happening *right now*, make it a `Node`. Most systems pair one of
each — a `CharacterData` Resource (the data) is read by a `PlayerCharacter` Node (the thing in the scene that
applies that data to an actual mesh and responds to input).

---

## How inheritance works here

Godot's inheritance is straightforward single-inheritance, declared with `extends`, and every custom type
gets a `class_name` so it can be referenced elsewhere without a file path:

```gdscript
class_name MachineStats extends Resource
```

This reads as: `MachineStats` is a new type, and it inherits everything `Resource` provides (serialization,
editor inspection, reference-sharing) — then adds its own fields and functions on top. The same pattern
applies to Nodes:

```gdscript
class_name PlayerCharacter extends CharacterBody3D
```

`PlayerCharacter` inherits `CharacterBody3D`'s built-in physics/movement behavior, then adds `character_data`,
morph-target application, and whatever else is specific to a playable character.

**Where deeper inheritance chains matter:** rather than a deep chain of custom subclasses, this project
mostly uses **composition over inheritance** — a `CharacterData` Resource *contains* a `MachineStats`
Resource and a `CharacterAppearance` Resource as fields, rather than `CharacterData` inheriting from either.
This keeps each piece independently reusable (an NPC's data can reuse `MachineStats` without needing
everything else a full player character carries) and avoids the classic problem of a rigid inheritance tree
that doesn't bend when a new combination shows up later. **The one place a real "is-a" inheritance
relationship exists in what's designed so far** is `PlayerCharacter extends CharacterBody3D` (a player
character genuinely *is a* physics body with extra behavior layered on) — everything else in
`03_Character_System.md` and beyond favors composition.

---

## Core Data Resources

### MachineStats

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

### SkillResource

```gdscript
class_name SkillResource extends Resource

@export var id: StringName
@export var display_name: String
@export var description: String
@export var category: StringName  # "technical", "social", "combat", etc.
@export var governing_stats: Array[StringName]  # ["calculation", "investigation"]
@export var primary_stat: StringName  # Used for skill cap calculation
```

### PerkResource

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

### TraitResource

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

### AbilityResource (Signature Abilities)

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

### DistrictResource

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

# Per-district difficulty curve: raw point thresholds marking where a district's own
# Fame/Infamy tracks cross from Range 0→1, 1→2, 2→3 (see 06_World_District_and_Reputation_System.md's
# two-axis grid). NOT uniform across districts — some districts are easy to win over,
# others take real dedication (same principle as Fallout: New Vegas's NCR vs. Great Khans
# requiring very different point totals for the same named tier). Exact per-district values
# are an open design question (Game-Mechanics/Core-Mechanics/Reputation_System.md) — the
# numbers below are illustrative placeholders only, not canon.
@export var fame_range_thresholds: Array[int] = [20, 50, 80]
@export var infamy_range_thresholds: Array[int] = [20, 50, 80]
```

### ReputationEvent

Every action that affects district reputation is defined as one of these — this keeps the reputation system
fully data-driven, same as everything else here: quest designers and modders define events in `.tres` files
without touching code. Full runtime behavior (the processor that applies these, the NPC hostility state
machine that reacts to them) is in `06_World_District_and_Reputation_System.md`; this is just the data shape.

**Two separate tracks, not one signed value.** Reputation here follows the project's own established
two-axis Fame/Infamy model (`Game-Mechanics/Core-Mechanics/Reputation_System.md`, itself adapted from Fallout:
New Vegas's reputation chart): a **Positive/Fame** track and a **Negative/Infamy** track per district,
accumulating independently and never canceling each other out. Each axis buckets into one of 4 Ranges
(0-3), and the *combination* of both ranges — not an average — produces one of 16 named tiers (Neutral,
Accepted, Liked, Idolized, Shunned, Mixed, Smiling Troublemaker, Good-Natured Rascal, Hated, Sneering Punk,
Unpredictable, Dark Hero, Vilified, Merciful Thug, Soft-Hearted Devil, Wild Child — full grid and lookup
logic in `06_World_District_and_Reputation_System.md`). A player can be genuinely both loved and hated by
the same district at once (Wild Child is the extreme case, both axes maxed simultaneously) — helping the
sick in Cancer while also having been caught stealing medicine doesn't average out to "neutral," it means
Cancer's people hold both feelings simultaneously, exactly as intended. A single signed field can't
represent that state at all, so each event carries **both** a positive delta and a negative delta (usually
only one is non-zero, but nothing prevents an event carrying both — e.g. a costly-but-good-faith action that
both earns trust and causes real harm). Note also that the *raw point thresholds* separating one Range from
the next are per-district data (`DistrictResource.fame_range_thresholds`/`infamy_range_thresholds`), not a
shared constant — some districts are easy to win over, others take real dedication, same principle as FNV's
NCR vs. Great Khans.

```gdscript
class_name ReputationEvent extends Resource

@export var id: StringName

# Which district this event primarily affects
@export var primary_district: StringName

# Two independent tracks — see note above. Neither ever reduces the other.
@export var positive_delta: int = 0  # 0 to 100
@export var negative_delta: int = 0  # 0 to 100

# If true, triggers immediate hostility regardless of current standing
@export var triggers_immediate_hostility: bool = false

# Cultural category — used for NPC reaction dialogue selection
# Matches the pattern from Worldspace/.../Hostility/District_Hostile_Actions.md
@export var violation_category: StringName
# "care_and_stability", "identity_and_self", "strength_and_output",
# "progress_and_truth", "systems_and_rules", "endurance_and_function"

# Human-readable description for the journal/reputation log
@export var display_description: String

# Justification text (shown if player inspects the event in their log)
@export var justification_hint: String

# Whether this event can be committed with good-faith intent
# Drives whether the game presents a moral warning before the action
@export var morally_ambiguous: bool = false

# Infamy: if true, this event is permanently visible on the player's record
# (NPCs can reference it by name forever)
@export var permanent_infamy: bool = false

# Optional: Identity Fragmentation increase (for re-spec events)
@export var fragmentation_increase: float = 0.0
```

**Example instances** (illustrating how these map onto real established content — full detail on the
hostility trigger list itself in `Worldspace/Locations-and-Levels/Concordia-City/Districts/Hostility/District_Hostile_Actions.md`):

```gdscript
# data/reputation_events/cancer_steal_medicine.tres
id = "cancer_steal_medicine"
primary_district = "cancer"
positive_delta = 0
negative_delta = 40
triggers_immediate_hostility = true
violation_category = "care_and_stability"
display_description = "Stole medical supplies designated for vulnerable residents."
justification_hint = "Critical medicine may have been needed for a companion or to prevent a larger outbreak."
morally_ambiguous = true
permanent_infamy = false
fragmentation_increase = 0.0
```

```gdscript
# data/reputation_events/taurus_restore_home.tres
id = "taurus_restore_home"
primary_district = "taurus"
positive_delta = 25
negative_delta = 0
triggers_immediate_hostility = false
violation_category = ""
display_description = "Helped a family repair and reinforce their ancestral home."
justification_hint = ""
morally_ambiguous = false
permanent_infamy = false
fragmentation_increase = 0.0
```
