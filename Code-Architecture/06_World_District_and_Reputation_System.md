# World, District & Reputation System

Depends on `02_Objects_and_Data_Resources.md`'s `DistrictResource` and `ReputationEvent` Resources. Full
non-code design reference for the reputation model itself:
`Game-Mechanics/Core-Mechanics/Reputation_System.md`.

---

## DistrictManager (Autoload)

Tracks the project's own two-axis Fame/Infamy model: each district maintains two independent raw point
totals (Fame, Infamy), each bucketed into one of 4 Ranges (0-3), with the *combination* of both ranges
producing one of 16 named tiers — not an average, not a single blended number. A player can be genuinely
both loved and hated by the same district at once.

**Per-district difficulty, not a shared constant.** The raw point thresholds marking where a district's Fame
or Infamy track crosses from Range 0→1, 1→2, 2→3 live on that district's own `DistrictResource`
(`fame_range_thresholds`, `infamy_range_thresholds` — see `02_Objects_and_Data_Resources.md`), not hardcoded
here. Some districts are easy to win over; others take real, sustained effort for the same named tier —
same principle as Fallout: New Vegas's NCR vs. Great Khans. Exact per-district values are still an open
design question (`Reputation_System.md`); the thresholds referenced below are whatever that district's own
Resource specifies, not a project-wide default.

```gdscript
class_name DistrictManager extends Node

var fame_points: Dictionary = {}    # {district_id: int} — raw Positive/Fame points
var infamy_points: Dictionary = {}  # {district_id: int} — raw Negative/Infamy points

var power_grid: PowerGridState
var identity_fragmentation: float = 0.0  # 0-100, increases with re-specs

func get_fame_range(district_id: StringName) -> int:
    # Returns 0-3, bucketed against THIS district's own thresholds
    var district = DataManager.get_district(district_id)
    var points = fame_points.get(district_id, 0)
    return _bucket(points, district.fame_range_thresholds)

func get_infamy_range(district_id: StringName) -> int:
    var district = DataManager.get_district(district_id)
    var points = infamy_points.get(district_id, 0)
    return _bucket(points, district.infamy_range_thresholds)

func _bucket(points: int, thresholds: Array[int]) -> int:
    if points >= thresholds[2]: return 3
    elif points >= thresholds[1]: return 2
    elif points >= thresholds[0]: return 1
    return 0

func modify_reputation(district_id: StringName, fame_delta: int, infamy_delta: int) -> void:
    if fame_delta != 0:
        fame_points[district_id] = max(0, fame_points.get(district_id, 0) + fame_delta)
    if infamy_delta != 0:
        infamy_points[district_id] = max(0, infamy_points.get(district_id, 0) + infamy_delta)

    # Ripple to allied/rival districts — each axis ripples independently.
    # Exact ripple proportions (0.3 / 0.2 below) are illustrative placeholders,
    # same "not yet tuned" status as the range thresholds themselves.
    var district = DataManager.get_district(district_id)
    for ally in district.ally_districts:
        if fame_delta != 0:
            fame_points[ally] = max(0, fame_points.get(ally, 0) + int(fame_delta * 0.3))
        if infamy_delta != 0:
            infamy_points[ally] = max(0, infamy_points.get(ally, 0) + int(infamy_delta * 0.3))
    for rival in district.rival_districts:
        # A rival district reacts to good standing with its rival as its own small Infamy bump —
        # your good name with their opponent makes them a little warier, not friendlier.
        if fame_delta != 0:
            infamy_points[rival] = max(0, infamy_points.get(rival, 0) + int(fame_delta * 0.2))

    EventBus.emit_signal("reputation_changed", district_id)

# The real 16-cell grid from Reputation_System.md — row = Infamy range, column = Fame range.
# Terminology itself (whether these exact names survive into Tepenia's own voice) is flagged
# in that file as still undecided — treat these as the current working names, not locked copy.
const TIER_GRID: Array = [
    # Fame:     0            1                        2                          3
    ["neutral",     "accepted",              "liked",                   "idolized"],           # Infamy 0
    ["shunned",     "mixed",                 "smiling_troublemaker",    "good_natured_rascal"], # Infamy 1
    ["hated",       "sneering_punk",         "unpredictable",           "dark_hero"],           # Infamy 2
    ["vilified",    "merciful_thug",         "soft_hearted_devil",      "wild_child"],          # Infamy 3
]

func get_reputation_tier(district_id: StringName) -> StringName:
    var fame_range = get_fame_range(district_id)
    var infamy_range = get_infamy_range(district_id)
    return TIER_GRID[infamy_range][fame_range]

func add_identity_fragmentation(amount: float) -> void:
    identity_fragmentation = clampf(identity_fragmentation + amount, 0.0, 100.0)
    EventBus.emit_signal("fragmentation_changed", identity_fragmentation)
    if identity_fragmentation >= 75.0:
        EventBus.emit_signal("fragmentation_critical")
```

### The Full Tier Grid (reference)

Reproduced from `Reputation_System.md` for quick lookup — this is the actual content `TIER_GRID` encodes,
not a separate/simplified version of it.

| Infamy ↓ / Fame → | **Range 0** | **Range 1** | **Range 2** | **Range 3** |
|---|---|---|---|---|
| **Range 0** | Neutral | Accepted | Liked | Idolized |
| **Range 1** | Shunned | Mixed | Smiling Troublemaker | Good-Natured Rascal |
| **Range 2** | Hated | Sneering Punk | Unpredictable | Dark Hero |
| **Range 3** | Vilified | Merciful Thug | Soft-Hearted Devil | Wild Child |

**Wild Child** (Fame Range 3 + Infamy Range 3 simultaneously) already has dedicated, fully-designed content
elsewhere — see `Storyline/Endings/Secret-Endings/Wild_Child_Endings.md` (WC-1 through WC-4) and its use as a
recommended companion-questline route pattern in `Companion_System.md`.

---

## PowerGridState

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

---

## RadioManager

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

## ReputationEventProcessor

The runtime system that applies `ReputationEvent` Resources (see `02_Objects_and_Data_Resources.md`) and
handles all side effects.

```gdscript
class_name ReputationEventProcessor extends Node

func apply_event(event: ReputationEvent, player_data: CharacterData) -> void:
    var district_manager = get_node("/root/DistrictManager")

    # Apply both Fame/Infamy tracks
    district_manager.modify_reputation(
        event.primary_district, event.positive_delta, event.negative_delta)

    # Trigger immediate hostility if flagged
    if event.triggers_immediate_hostility:
        _trigger_hostility(event.primary_district, event.violation_category)

    # Apply permanent infamy flag
    if event.permanent_infamy:
        _record_permanent_infamy(event, player_data)

    # Apply identity fragmentation if present
    if event.fragmentation_increase > 0.0:
        district_manager.add_identity_fragmentation(event.fragmentation_increase)

    # Log to player journal
    EventBus.emit_signal("reputation_event_fired", event)

    # Show moral warning if ambiguous (before confirming action)
    # Note: this check happens BEFORE apply_event is called — see DialogueSystem

func _trigger_hostility(district_id: StringName, category: StringName) -> void:
    # Notify all NPCs in the current district scene
    EventBus.emit_signal("district_hostility_triggered", district_id, category)
    # NPCs listen to this signal and switch to hostile state
    # Reaction dialogue is selected based on violation_category

func _record_permanent_infamy(event: ReputationEvent, player_data: CharacterData) -> void:
    if not player_data.permanent_infamy_flags.has(event.id):
        player_data.permanent_infamy_flags.append(event.id)
        # NPCs can query this list to reference specific past actions in dialogue
        # e.g., "I heard what you did to the Undergrid. Don't expect help from us."
```

---

## NPCCombatState (Hostility State Machine)

Each NPC has a simple state machine that responds to hostility signals — local to that NPC's own node, not
global (see `01_Global_State_and_Autoloads.md`'s global/local test). Distinct from the district-wide
Fame/Infamy tiers above: this is one specific NPC's own immediate combat-readiness state, triggered by a
hostility event in their home district.

```gdscript
class_name NPCCombatState extends Node

enum State { NEUTRAL, WARY, HOSTILE, FLEEING }

var current_state: State = State.NEUTRAL
var home_district: StringName = ""
var violation_category_reactions: Dictionary = {
    "care_and_stability": "You monster — those supplies were for children!",
    "identity_and_self": "You had no right to do that here!",
    "strength_and_output": "You could have killed us all!",
    "progress_and_truth": "Do you have any idea what you just destroyed?!",
    "systems_and_rules": "You just signed your own death warrant.",
    "endurance_and_function": "We keep this city alive. And you just spat on that."
}

func _ready() -> void:
    EventBus.connect("district_hostility_triggered", _on_hostility_triggered)

func _on_hostility_triggered(district_id: StringName, category: StringName) -> void:
    if district_id != home_district:
        return
    current_state = State.HOSTILE
    _bark(violation_category_reactions.get(category, "Get away from here!"))

func _bark(text: String) -> void:
    # Play voiced line or display floating text
    EventBus.emit_signal("npc_bark", self, text)
```

---

## Integration with the Re-Spec System

Re-spec events are a special category of `ReputationEvent` that also carry `fragmentation_increase`. The
district where the re-spec occurs gains Fame (you trusted them with your identity); rival districts may gain
Infamy, independently — each axis moves on its own, same as everywhere else in this system.

```gdscript
# data/reputation_events/respec_scorpio_rebirth.tres
id = "respec_scorpio_rebirth"
primary_district = "scorpio"
positive_delta = 30
negative_delta = 0
triggers_immediate_hostility = false
violation_category = ""
display_description = "Underwent the Rebirth Ritual in Scorpio."
justification_hint = ""
morally_ambiguous = false
permanent_infamy = false
fragmentation_increase = 15.0  # Identity Fragmentation increases significantly
```

Suggested `fragmentation_increase` values by method (illustrative, not yet tuned):

| Re-Spec Method | District | Fragmentation Increase |
|---|---|---|
| Calethina's Lab | Central Hub | 5.0 |
| Virgo Deep Purge | Virgo | 12.0 |
| Aries Forge Rebuild | Aries | 18.0 |
| Aquarius Lattice Swap | Aquarius | 20.0 (+ random variance) |
| Pisces Market Rebuild | Pisces | 22.0 |
| Scorpio Rebirth Ritual | Scorpio | 25.0 |
| Crisis/Environmental | Various | 10.0-30.0 (random) |

At **75+ Fragmentation**, `fragmentation_critical` fires on `EventBus` — unique questlines unlock, certain
NPCs react with fear or fascination, and some dialogue options become permanently unavailable. At **100
Fragmentation**, a unique ending branch opens.
