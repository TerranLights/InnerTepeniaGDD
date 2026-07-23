# Global State & Autoloads

---

## What "global" actually means in this project

Godot's mechanism for global state is the **Autoload** (also called a singleton) — a script registered in
Project Settings that gets instantiated once, lives at a fixed path (`/root/GameState`, `/root/EventBus`,
etc.), and stays alive for the entire session regardless of which scene is currently loaded. Anything that
needs to survive a scene change (moving from one district to another, entering/leaving combat, opening a
menu) or that multiple unrelated systems need to reach without being handed a reference to each other has to
either live in an Autoload or be reachable through one.

**Everything else is local** — state that belongs to one scene, one node, or one object instance, and simply
doesn't exist once that scene is unloaded or that object is freed. A specific NPC's current `NPCCombatState`
(see `06_World_District_and_Reputation_System.md`) is local: it belongs to that NPC's own node in that
district's scene, and there's no reason any other system should reach it directly rather than through a
signal. A `CameraController`'s current zoom level is local to that camera rig.

**The test used throughout this folder:** if losing the value when a scene unloads would break something (a
saved game, a cross-district reputation total, the player's own stats), it's global and belongs in an
Autoload. If it's just describing the current moment of one specific thing on screen, it's local and belongs
on that thing's own node.

**A second, related test:** anything that many unrelated systems need to read or modify — reputation, power
grid state, the player's save data — should be global specifically so those systems never need a direct
reference to each other. A combat encounter shouldn't need to know how the UI displays AP; it emits a signal
on `EventBus` and lets whatever's listening (usually something local to the UI scene) react. This is why
`EventBus` itself is the most important Autoload in the whole project — it's the mechanism that keeps every
other system decoupled from every other system.

---

## The Autoload Roster

These six are always available everywhere in the game. Keep the list lean — anything that doesn't need to
survive a scene change or be reached by unrelated systems shouldn't be here.

| Autoload | Purpose |
|---|---|
| `GameState` | Current game phase (exploration/combat/dialogue/cutscene), active scene, global flags |
| `EventBus` | Decoupled signal relay — systems talk through here, never directly to each other |
| `SaveManager` | Save/load serialization (full detail: `07_Save_System.md`) |
| `DataManager` | Loads and caches all Resource (`.tres`) data |
| `AudioManager` | Music, SFX, district radio management |
| `DistrictManager` | Active district, faction reputations, power grid state (full detail: `06_World_District_and_Reputation_System.md`) |

A seventh, `GraphicsSettingsManager`, is also global but scoped specifically to hardware-tier/camera-mode
settings — see `08_Scalable_Graphics_and_Hardware_Tiers.md` for its own definition.

---

## EventBus Signal Catalog

Every cross-system communication in the game goes through this one Autoload. A system that wants to react to
something happening elsewhere connects to the relevant signal; it never holds a direct reference to the
system that fired it.

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

# Reputation / Hostility (see 06_World_District_and_Reputation_System.md)
signal reputation_event_fired(event: Resource)
signal district_hostility_triggered(district_id: StringName, category: StringName)
signal npc_bark(npc: Node, text: String)

# Movement (see 05_Grid_Movement_and_Camera.md)
signal movement_completed()

# Graphics (see 08_Scalable_Graphics_and_Hardware_Tiers.md)
signal graphics_settings_changed(tier: int)
```

**Why this is a signal catalog and not a Dictionary of loose string names:** typed signals declared on a
single Autoload give every other system autocomplete and compile-time checking against typos — a
`"combta_ended"` misspelling fails immediately rather than silently never firing. Every system in this
folder that says "emits a signal" or "listens for a signal" is referring back to this list; if a new system
needs a new cross-system event, it gets added here, not invented ad hoc somewhere else.
