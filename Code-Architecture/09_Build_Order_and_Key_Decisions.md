# Build Order & Key Decisions

Consolidates the "where this fits in the build order" notes scattered across every other file in this folder
into one sequence, plus the rationale behind this architecture's biggest calls.

---

## Build Order

Build these systems in sequence. Each must be testable before the next begins — this is the same "build in
layers" principle from `00_Overview_and_Project_Structure.md`.

**Revised 2026-08-16 — logic-first, not visual-first.** The previous version of this order started with camera
and tilemap work (learning Godot's rendering side) before most of the actual game logic existed to test against
it. `12_Text_Based_Testing_Harness.md` makes a better order possible: every system that's really about *rules*
rather than *rendering* — stats, skills, checks, dialogue branching, combat resolution, world/reputation state
— can be built and fully validated as a numbered-menu text interface first, in both a terminal and a browser,
using the exact same GDScript/C++ classes the 3D game will use later. The new Phase 0 below pulls those pieces
forward from where they used to sit (old Phases 2 through 7); the phases after it keep their original systems
but now focus on the *visual/UI* layer for logic that's already proven correct, rather than building logic and
visuals simultaneously. Nothing here is a new system — it's the same systems, reordered around what actually
needs a screen to validate versus what doesn't.

### Phase 0 — Text-Based Logic Harness (headless, no visuals)
Full detail: `12_Text_Based_Testing_Harness.md`. Exit criteria: a complete text playthrough — one companion's
dialogue tree, one combat encounter, basic world navigation with working checks and reputation feedback — runs
correctly via `godot --headless` in a terminal and via the same project's HTML5 export in a browser, before any
camera/3D/graphics work begins.
1. `TextInterfaceController` — the shared numbered-menu renderer (input: a list of options with optional
   check-annotations; output: the player's selection) that Dialogue, Combat, and World navigation will all
   drive, and that the real 3D UI will eventually stand in front of without changing anything behind it
2. `MachineStats` resource + skill/perk/trait data structures (`02_Objects_and_Data_Resources.md`) — logic
   only, no Character Creation screen yet
3. `DialogueManager` + Topic/Condition/Effects data structures matching the `Dialogue/` folder's schema
   (`to-be-integrated/Dialogue_Tree_Spreadsheet_Setup_Guide.md`) — load a real sheet, render it as a numbered
   menu, branch on choice, exactly like the worked dialogue example in `12`
4. Minimal world-state model: "where am I, who's in the area," numbered travel/interaction actions — a new
   content type, not yet designed beyond the example in `12`
5. Combat core logic, data only: `GridManager`'s data model (position, pathfinding, LOS — no tilemap
   rendering), `APManager`, `TurnManager`, `DamageCalculator`, `NODETargetingSystem` — presented as numbered
   action menus (move, attack, target NODE, use item)
6. `DistrictManager`/`ReputationEventProcessor` + reputation tier lookup — logic only, printed as text feedback
7. Minimal in-memory quest-flag/reputation state — not full save-file serialization (`07_Save_System.md` stays
   its own later phase), just enough for the dialogue schema's Conditions/Effects columns to mean something
   during text testing
8. Full end-to-end text playthrough proving the numbered-menu paradigm and the underlying data-driven
   Resources work correctly together

### Phase 1 — Visual Foundation (Learn Godot's rendering side)
Now explicitly the point where Phase 0's already-proven logic gets its first real visual presentation layer,
not where logic and rendering get learned simultaneously.
9. Godot orientation: scenes, nodes, signals, GDScript basics (if not already covered getting Phase 0 running)
10. Simple isometric tilemap prototype (movement only, no combat)
11. **Camera system prototype** — implement `CameraController` (`05_Grid_Movement_and_Camera.md`), tune
    parameters to match the target feel
12. Wire character movement to camera — click-to-move, camera follows smoothly, WASD pans independently
13. Basic GDExtension hello-world (get the C++ pipeline working, if not already needed for Phase 0's
    `GridManager`/`DamageCalculator` data-model work)
14. `GraphicsSettingsManager` autoload skeleton (`08_Scalable_Graphics_and_Hardware_Tiers.md`) — preset
    switching and config save/load, camera mode switching working end-to-end

### Phase 2 — Character System (visual/UI layer)
15. Character Creation screen (end-to-end UI flow), built on top of Phase 0's already-proven stat/skill/perk/
    trait logic — the screen is new, the rules it's presenting aren't
16. `CharacterAppearance` + morph target application in-scene (`03_Character_System.md`)

### Phase 3 — Combat Visual Layer & Depth
Phase 0 already proved the resolution math (AP spend, damage formula, hit chance, NODE targeting) is correct.
This phase wires that proven logic to the real grid/camera/combat scene and adds the remaining content-heavy
depth that wasn't required just to validate the core loop.
17. `GridManager`'s visual/tilemap layer wired to the already-proven data model
18. Basic attack flow, now in the real combat scene (move → attack → damage → next turn)
19. Armor and frame system
20. `SignatureAbilityManager`: Framejacking, Rage, Overclock
21. Ammo types and penetration
22. Status effects (Joint Lock, Overheat, EMP, etc.)
23. Perks that interact with combat

### Phase 4 — World Systems (visual/audio layer)
Reputation logic itself was proven in Phase 0; this phase is the presentation and remaining systems that were
never primarily about rules.
24. `PowerGridState`: allocation, stability, blackout — logic can move to Phase 0 if it turns out to be as
    text-testable as reputation was; visual/UI feedback stays here regardless
25. `RadioManager`: per-district music crossfade
26. District scene transitions
27. Reputation UI (feeding off the already-proven `ReputationEventProcessor`/tier lookup)

### Phase 5 — Re-Spec System
28. Identity Fragmentation meter (see `project_identity_fragmentation_review_flagged` memory — substantial
    existing design material to review before implementing, not a from-scratch build). Threshold/event logic
    is a Phase 0 candidate the same way reputation was, if it proves out that cleanly.
29. Calethina's Lab (base re-spec)
30. District-specific re-spec methods
31. Visual/audio feedback per method
32. NPC reaction hooks
33. Fragmentation meter UI
34. Re-spec `ReputationEvent` definitions
35. `fragmentation_critical` event hooks
36. NPC reactions to permanent infamy flags

### Phase 6 — Content & Polish
37. Quest system scaffolding — flag/stage tracking beyond what Phase 0 needed minimally for dialogue testing
38. Dialogue system — full content authoring plus remaining polish (voice-over hooks, animation triggers);
    core branching/check logic already proven in Phase 0
39. Save/load (`07_Save_System.md`)
40. Main story structure (Act 1 → Climax)
41. Mod JSON loader (override/extend base Resources)
42. Tune all per-tier graphics values against actual in-game scenes
43. Implement auto-detect logic properly against real hardware
44. Build the settings UI
45. First launch experience
46. Per-district environment nodes tagged for quality scaling

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
| Text-based numbered-menu harness before any visual work (`12_Text_Based_Testing_Harness.md`) | Godot runs headless and exports to HTML5, so the harness uses the exact same GDScript/C++ logic classes the 3D game will — validating dialogue, checks, combat resolution, and world/reputation state doesn't require a second implementation, just a swapped presentation layer, and catches logic bugs before they're entangled with rendering/camera bugs |
