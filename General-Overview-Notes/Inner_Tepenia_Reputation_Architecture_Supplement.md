# Inner Tepenia — Reputation & Hostility System
**Architecture Supplement to Technical Architecture Document v0.1**

---

## Overview

This supplement defines the data structures and runtime logic for the district reputation and hostility system. It pairs directly with `DistrictManager` in the main architecture document and covers:

- `ReputationEvent` resource (how actions are defined)
- Hostility trigger logic
- Ripple effects to allied/rival districts
- Identity Fragmentation interactions

---

## 1. ReputationEvent Resource

Every action that affects reputation is defined as a `ReputationEvent` resource. This keeps the system fully data-driven — quest designers and modders define events in `.tres` files without touching code.

```gdscript
class_name ReputationEvent extends Resource

@export var id: StringName

# Which district this event primarily affects
@export var primary_district: StringName

# Delta applied to primary district (-100 to +100)
@export var reputation_delta: int

# If true, triggers immediate hostility regardless of current rep
@export var triggers_immediate_hostility: bool = false

# Cultural category — used for NPC reaction dialogue selection
# Matches the pattern from District_Hostile_Actions.md
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

---

## 2. Example ReputationEvents

These correspond directly to the hostile actions defined in `District_Hostile_Actions.md`.

### Cancer — Stealing medicine meant for the sick
```gdscript
# data/reputation_events/cancer_steal_medicine.tres
id = "cancer_steal_medicine"
primary_district = "cancer"
reputation_delta = -40
triggers_immediate_hostility = true
violation_category = "care_and_stability"
display_description = "Stole medical supplies designated for vulnerable residents."
justification_hint = "Critical medicine may have been needed for a companion or to prevent a larger outbreak."
morally_ambiguous = true
permanent_infamy = false
fragmentation_increase = 0.0
```

### Aries — Sabotaging power infrastructure
```gdscript
# data/reputation_events/aries_sabotage_grid.tres
id = "aries_sabotage_grid"
primary_district = "aries"
reputation_delta = -60
triggers_immediate_hostility = true
violation_category = "strength_and_output"
display_description = "Sabotaged critical power infrastructure endangering workers."
justification_hint = "May have been preventing a worse catastrophic overload or forcing a necessary safety shutdown."
morally_ambiguous = true
permanent_infamy = true
fragmentation_increase = 0.0
```

### Pisces — Snitching on criminal operations
```gdscript
# data/reputation_events/pisces_snitch.tres
id = "pisces_snitch"
primary_district = "pisces"
reputation_delta = -75
triggers_immediate_hostility = true
violation_category = "systems_and_rules"
display_description = "Informed on major criminal operations to outside authorities."
justification_hint = "The operation may have been harming innocents or threatening city stability."
morally_ambiguous = true
permanent_infamy = true
fragmentation_increase = 0.0
```

### Taurus — Helping restore a family home (positive)
```gdscript
# data/reputation_events/taurus_restore_home.tres
id = "taurus_restore_home"
primary_district = "taurus"
reputation_delta = 25
triggers_immediate_hostility = false
violation_category = ""
display_description = "Helped a family repair and reinforce their ancestral home."
justification_hint = ""
morally_ambiguous = false
permanent_infamy = false
fragmentation_increase = 0.0
```

---

## 3. ReputationEventProcessor

The runtime system that applies events and handles all side effects.

```gdscript
class_name ReputationEventProcessor extends Node

func apply_event(event: ReputationEvent, player_data: CharacterData) -> void:
    var district_manager = get_node("/root/DistrictManager")

    # Apply primary reputation change
    district_manager.modify_reputation(event.primary_district, event.reputation_delta)

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

## 4. Hostility State Machine (NPC side)

Each NPC has a simple state machine that responds to hostility signals.

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

## 5. Reputation Thresholds

These map numeric reputation values to named tiers used throughout the game for dialogue, quest access, and armor/augmentation availability.

```gdscript
# In DistrictManager
func get_reputation_tier(district_id: StringName) -> StringName:
    var rep = get_reputation(district_id)
    if rep >= 80:   return "idolized"
    elif rep >= 50: return "respected"
    elif rep >= 20: return "accepted"
    elif rep >= -19: return "neutral"
    elif rep >= -49: return "unwelcome"
    elif rep >= -79: return "hated"
    else:            return "enemy"
```

| Tier | Range | Effect |
|---|---|---|
| Idolized | 80–100 | Capstone quest unlocked, unique armor available, district-wide ally NPCs |
| Respected | 50–79 | Discounts, quest access, positive ambient dialogue |
| Accepted | 20–49 | Normal trade and interaction |
| Neutral | -19–19 | Default state, no special treatment |
| Unwelcome | -50–-20 | Suspicious NPCs, higher prices, some quests locked |
| Hated | -80–-50 | Refused service, ambient hostility, some NPCs attack on sight |
| Enemy | -100–-81 | All NPCs attack on sight, district effectively closed off |

---

## 6. Integration with Re-Spec System

Re-spec events are a special category of `ReputationEvent` that also carry `fragmentation_increase`. The district where the re-spec occurs gains reputation (you trusted them with your identity), while rival districts may lose reputation.

```gdscript
# data/reputation_events/respec_scorpio_rebirth.tres
id = "respec_scorpio_rebirth"
primary_district = "scorpio"
reputation_delta = 30
triggers_immediate_hostility = false
violation_category = ""
display_description = "Underwent the Rebirth Ritual in Scorpio."
justification_hint = ""
morally_ambiguous = false
permanent_infamy = false
fragmentation_increase = 15.0  # Identity Fragmentation increases significantly
```

The `fragmentation_increase` values by method (suggested):

| Re-Spec Method | District | Fragmentation Increase |
|---|---|---|
| Calethina's Lab | Central Hub | 5.0 |
| Virgo Deep Purge | Virgo | 12.0 |
| Aries Forge Rebuild | Aries | 18.0 |
| Aquarius Lattice Swap | Aquarius | 20.0 (+ random variance) |
| Pisces Market Rebuild | Pisces | 22.0 |
| Scorpio Rebirth Ritual | Scorpio | 25.0 |
| Crisis/Environmental | Various | 10.0–30.0 (random) |

At **75+ Fragmentation**, `fragmentation_critical` fires on `EventBus` — unique questlines unlock, certain NPCs react with fear or fascination, and some dialogue options become permanently unavailable.

At **100 Fragmentation**, a unique ending branch opens.

---

## 7. Where This Fits in the Build Order

This system is implemented across two phases:

**Phase 5 (World Systems):**
- `ReputationEvent` resource class
- `ReputationEventProcessor`
- `DistrictManager.modify_reputation()` ripple logic
- Reputation tier calculation

**Phase 6 (Re-Spec System):**
- Fragmentation meter UI
- Re-spec `ReputationEvent` definitions
- `fragmentation_critical` event hooks
- NPC reactions to permanent infamy flags

---

*Supplement to Inner_Tepenia_Technical_Architecture.md. Commit both to GDD repo together.*
