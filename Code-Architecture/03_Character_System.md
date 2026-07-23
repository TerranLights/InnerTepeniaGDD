# Character System

Depends on `02_Objects_and_Data_Resources.md`'s `MachineStats` Resource.

---

## CharacterData (the master record)

Every character in the game — player or NPC — has one of these. It's a `Resource`, not a `Node`: it's pure
data, serializable, and can exist and be edited before any scene ever loads it.

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

## CharacterAppearance (body customization)

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

# Body colors and markings
@export var primary_color: Color = Color.WHITE
@export var secondary_color: Color = Color.GRAY
@export var marking_pattern: int = 0
```

## PlayerCharacter (the in-scene node)

This is where the `Resource`/`Node` split from `02_Objects_and_Data_Resources.md` becomes concrete: the scene
node reads from a `CharacterData` Resource and applies it to an actual mesh in the world.

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

**Why morph targets specifically:** industry-standard approach for body customization, GPU-efficient, and
works with any armor/clothing layered on top without needing separate meshes per body-shape combination.
