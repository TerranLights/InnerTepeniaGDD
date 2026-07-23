# Build Order & Key Decisions

Consolidates the "where this fits in the build order" notes scattered across every other file in this folder
into one sequence, plus the rationale behind this architecture's biggest calls.

---

## Build Order

Build these systems in sequence. Each must be testable before the next begins — this is the same "build in
layers" principle from `00_Overview_and_Project_Structure.md`.

### Phase 1 — Foundation (Learn Godot)
1. Godot orientation: scenes, nodes, signals, GDScript basics
2. Simple isometric tilemap prototype (movement only, no combat)
3. **Camera system prototype** — implement `CameraController` (`05_Grid_Movement_and_Camera.md`), tune
   parameters to match the target feel
4. Wire character movement to camera — click-to-move, camera follows smoothly, WASD pans independently
5. Basic GDExtension hello-world (get the C++ pipeline working)
6. `GraphicsSettingsManager` autoload skeleton (`08_Scalable_Graphics_and_Hardware_Tiers.md`) — preset
   switching and config save/load, camera mode switching working end-to-end

### Phase 2 — Character System
7. `MachineStats` resource + stat allocation UI (`02_Objects_and_Data_Resources.md`)
8. Skill point calculation, skill cap system
9. Tag skill selection
10. Trait selection
11. Character Creation screen (end-to-end flow)
12. `CharacterAppearance` + morph target application in-scene (`03_Character_System.md`)

### Phase 3 — Combat Core
13. `GridManager` (C++): grid representation, pathfinding, LOS (`05_Grid_Movement_and_Camera.md`)
14. `APManager`: turn start, spend, discard at end of turn (`04_Combat_System.md`)
15. `TurnManager`: initiative, turn cycling
16. `DamageCalculator` (C++): full DT/DR formula
17. Basic attack flow (move → attack → damage → next turn)
18. Armor and frame system
19. `NODETargetingSystem`: body part selection, hit chance, cycle cost

### Phase 4 — Combat Depth
20. `SignatureAbilityManager`: Framejacking, Rage, Overclock
21. Ammo types and penetration
22. Status effects (Joint Lock, Overheat, EMP, etc.)
23. Perks that interact with combat

### Phase 5 — World Systems
24. `DistrictManager`: Fame/Infamy tracking, ripple effects (`06_World_District_and_Reputation_System.md`)
25. `ReputationEvent` resource class + `ReputationEventProcessor`
26. Reputation tier lookup (the 16-cell grid)
27. `PowerGridState`: allocation, stability, blackout
28. `RadioManager`: per-district music crossfade
29. District scene transitions

### Phase 6 — Re-Spec System
30. Identity Fragmentation meter (see `project_identity_fragmentation_review_flagged` memory — substantial
    existing design material to review before implementing, not a from-scratch build)
31. Calethina's Lab (base re-spec)
32. District-specific re-spec methods
33. Visual/audio feedback per method
34. NPC reaction hooks
35. Fragmentation meter UI
36. Re-spec `ReputationEvent` definitions
37. `fragmentation_critical` event hooks
38. NPC reactions to permanent infamy flags

### Phase 7 — Content & Polish
39. Quest system scaffolding
40. Dialogue system
41. Save/load (`07_Save_System.md`)
42. Main story structure (Act 1 → Climax)
43. Mod JSON loader (override/extend base Resources)
44. Tune all per-tier graphics values against actual in-game scenes
45. Implement auto-detect logic properly against real hardware
46. Build the settings UI
47. First launch experience
48. Per-district environment nodes tagged for quality scaling

---

## Key Technical Decisions & Rationale

| Decision | Rationale |
|---|---|
| Godot Resources over JSON internally | Type safety, editor inspection, native serialization |
| JSON for mod-facing data | Human-readable, no engine dependency for modders |
| C++ for grid + damage | Hot paths called every frame/every attack — GDScript too slow |
| EventBus for cross-system signals | Decouples systems; district reputation change doesn't need to know about UI |
| `CharacterData` as a Resource | Trivially serializable for save/load; passable between scenes |
| Morph targets for body customization | Industry-standard approach; GPU-efficient; works with any armor layered on top |
| Separate `PowerGridState` resource | Encapsulates the core story mechanic; easy to serialize and query |
| Identity Fragmentation in `DistrictManager` | It's a world-state value, not a character stat — persists across re-specs by design |
| Two independent Fame/Infamy tracks, not one signed value | A player can be genuinely both loved and hated by the same district at once; averaging or canceling would erase that state entirely |
| Per-district Fame/Infamy range thresholds, not a shared constant | Some districts are easy to win over, others take real dedication — same principle as Fallout: New Vegas's NCR vs. Great Khans |
| WASD pans the camera, click-to-move drives the character | A necessary consequence of the free-rotating camera — if WASD moved the character, "forward" would mean something different every time the camera rotated |
| Constrained-by-default camera, freedom scales with hardware tier | Lower tiers get a more performance-friendly, still-good camera; higher tiers get full freedom — nobody is stuck with a worse *game*, just a narrower camera window |
