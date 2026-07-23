# Save System

Depends on `02_Objects_and_Data_Resources.md` (`CharacterData`, `CharacterAppearance`) and
`06_World_District_and_Reputation_System.md` (`DistrictManager`'s Fame/Infamy points and Identity
Fragmentation).

---

## SaveManager (Autoload)

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

func _serialize_world() -> Dictionary:
    return {
        "fame_points": DistrictManager.fame_points,
        "infamy_points": DistrictManager.infamy_points,
        "power_grid": DistrictManager.power_grid,
        "current_district": GameState.active_district_id,
    }
```

**Why `CharacterData`/`CharacterAppearance` as Resources matters here** (see `02_Objects_and_Data_Resources.md`):
trivially serializable, passable between scenes, and inspectable in the editor — this is the concrete payoff
of "data-driven everywhere possible." Nothing about save/load required a bespoke serialization format because
the underlying data was never hardcoded to begin with.
