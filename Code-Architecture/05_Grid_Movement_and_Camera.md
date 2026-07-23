# Grid, Movement & Camera System

Full companion design doc (non-code): `Game-Mechanics/Core-Mechanics/Movement_Camera_and_Grid_System.md`.
This file is that system's actual code-structure counterpart. Camera-freedom scaling by hardware tier is a
separate concern — see `08_Scalable_Graphics_and_Hardware_Tiers.md`, which builds directly on top of the
`CameraController` defined here.

---

## Core Philosophy

- **Tactical clarity** — grid-based AP costs, readable positioning, line-of-sight.
- **Modern motion feel** — smooth animations, intelligent pathing, responsive camera.
- **District personality** — Concordia's circular district layout should feel distinct and beautiful from
  the chosen camera perspective. **Note:** the "color-coded" wheel seen in dev-facing map diagrams is a
  reference/legibility convention for planning purposes only — it is *not* a literal in-game visual design.
  Each district's own actual distinctiveness in-world comes from its architecture, materials, lighting, and
  atmosphere, not from a cartoonish color-per-district scheme.

---

## Controls & Input Scheme

Modeled directly on Baldur's Gate 3's own control scheme, made necessary by the free-rotating camera (see
Camera System, below):

- **Keyboard (W/A/S/D): moves the camera**, not the player character — forward/backward/left/right relative
  to current camera facing. This is a deliberate consequence of the rotating camera: if WASD moved the
  character instead, "forward" would mean something different every time the camera rotates, which BG3
  avoids by dedicating WASD to the camera entirely.
- **Left-click: click-to-move.** This is the *only* way the player character moves — click a point on the
  navmesh (or an interactable/NPC) and the character paths there via `PlayerMovementController` (below), grid
  -costed underneath the same as any other movement.
- **Right-click: examine/interact.** Context-sensitive — inspects or interacts with whatever's under the
  cursor, distinct from the left-click move command.

This applies during exploration specifically; combat mode's click-to-target/click-to-move-with-AP-preview
behavior (see `04_Combat_System.md`) works the same way, just with an AP cost readout attached.

---

## Grid System: Hexagonal + Navmesh Hybrid

**Why hex over square:** consistent distance between adjacent tiles (no diagonal-penalty weirdness), more
natural flanking/positioning in combat, better suits the organic/sci-fi architecture of many districts
(hydroponics, industrial clutter, the Frostlands, undergrid tunnels), and cleaner AP calculations.

**How the hybrid works:**
- **Hex Grid Layer** (logical/rules layer) — all AP costs, range calculations, line-of-sight, and tactical
  highlighting are based on clean hex tiles. Keeps the system precise, speedrun-friendly, and easy to balance.
- **Navmesh Layer** (visual/feel layer) — a navigation mesh defines actual walkable space. Characters follow
  smooth, curved, intelligent paths around obstacles (furniture, pipes, debris, other characters, hydroponic
  planters, etc.). Movement *looks* fluid and modern, but the final AP cost is snapped to the nearest valid
  hex tile count.
- **Result:** beautiful, weighty animation with perfect tactical precision underneath.

**Exploration vs. combat:**
- **Exploration mode** — click-to-move (see Controls & Input Scheme, above), full fluid animation and
  navmesh pathing, no AP cost.
- **Combat mode** — switches to strict turn-based AP. Players click a destination and see a glowing path
  preview with exact AP cost before committing; characters then execute the movement with smooth animation
  blending.

### GridManager (C++ via GDExtension)

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
var result = GridManager.find_path(from_tile, to_tile, free_tiles)
var path: Array[Vector2i] = result.path
var ap_cost: int = result.ap_cost

var has_los: bool = GridManager.has_line_of_sight(attacker_pos, target_pos)
```

### Mitigating Straight Walls in Indoor Areas (Hex Grid Challenge)

1. **Art-first approach (recommended).** Rooms built with natural straight walls; hex grid as invisible/subtle
   overlay; walkable space determined by whether a hex's *center* lies inside the room.
2. **Grid rotation.** Rotate hex orientation per map to align with major wall directions where possible.
3. **Hybrid grid zones.** Hex for organic/outdoor areas; square (or "hexaquad") for strict rectangular
   interiors, with clear visual transitions.
4. **Design philosophy.** Lean into organic/larger-scale interiors where lore supports it (open medical wards
   in Cancer, cluttered factories in Capricorn).
5. **Visual polish.** Subtle/toggleable hex grid ("G" key); environmental detail and lighting guide the eye
   instead of visible grid lines.

### Animation & Pathing Priorities

High-quality animation blending/IK (foot placement on uneven terrain, ramps, snow); contextual animations
(brushing snow, ducking under pipes, interacting with medical equipment); pathfinding that avoids other
characters and dynamic obstacles; pre-visualized movement paths with real-time AP cost display.

### Integration Points

- `DistrictResource` may include fields for preferred grid behavior or camera presets.
- `CombatManager`/`APManager` read from the hex grid for costs.
- `DistrictManager` can influence pathfinding costs (difficult terrain in the Frostlands, damaged areas
  during power crises).
- Save system must serialize current grid position (hex coordinates) plus visual transform.

---

## Camera System

**Design goal — reference feel: Wasteland 3** (semi-free isometric, constrained rotation) as the default/Low
tier, scaling up toward a full BG3-style free camera at the Ultra hardware tier — see
`08_Scalable_Graphics_and_Hardware_Tiers.md` for the tier scaling itself.

- Primarily overhead-ish default angle, reads clearly for tactical turn-based combat.
- Constrained rotation by default (not full 360° ground-level freedom).
- Smooth zoom within a readable overhead range.
- Never lets the player feel "lost" or lose tactical readability.

Distinct from **true locked isometric** (no rotation at all) and **full free camera** (unrestricted pitch/zoom
to ground level — the Ultra-tier ceiling) at either end.

### Camera Parameters (base values, tuned during development)

```gdscript
const MIN_ROTATION_Y: float = 0.0
const MAX_ROTATION_Y: float = 360.0
const MIN_PITCH: float = -70.0
const MAX_PITCH: float = -30.0
const DEFAULT_PITCH: float = -55.0
const ROTATION_SPEED: float = 120.0

const MIN_ZOOM: float = 8.0
const MAX_ZOOM: float = 30.0
const DEFAULT_ZOOM: float = 18.0
const ZOOM_SPEED: float = 5.0

const FOLLOW_SPEED: float = 8.0
const KEYBOARD_PAN_SPEED: float = 15.0    # W/A/S/D camera pan
const EDGE_SCROLL_SPEED: float = 15.0     # mouse-at-screen-edge pan
const EDGE_SCROLL_MARGIN: float = 20.0
```

### Scene Structure

```
CameraRig (Node3D)          — moves horizontally to follow player/cursor
└── CameraArm (Node3D)      — handles rotation and pitch
    └── SpringArm3D         — handles zoom and collision avoidance
        └── Camera3D        — the actual camera
```

`SpringArm3D` matters because it automatically pushes the camera forward if something solid is between the
camera and its target, preventing clipping into geometry.

### CameraController

```gdscript
class_name CameraController extends Node3D

@onready var camera_arm: Node3D = $CameraArm
@onready var spring_arm: SpringArm3D = $CameraArm/SpringArm3D
@onready var camera: Camera3D = $CameraArm/SpringArm3D/Camera3D

var current_zoom: float = DEFAULT_ZOOM
var target_zoom: float = DEFAULT_ZOOM
var current_pitch: float = DEFAULT_PITCH
var is_rotating: bool = false
var follow_target: Node3D = null
var free_roam: bool = false

func _ready() -> void:
    spring_arm.spring_length = current_zoom
    camera_arm.rotation_degrees.x = current_pitch

func _process(delta: float) -> void:
    _handle_zoom(delta)
    _handle_rotation(delta)
    _handle_keyboard_pan(delta)
    _handle_edge_scroll(delta)
    _handle_follow(delta)

func _handle_zoom(delta: float) -> void:
    current_zoom = lerp(current_zoom, target_zoom, delta * 10.0)
    spring_arm.spring_length = current_zoom

func zoom_in() -> void:
    target_zoom = clampf(target_zoom - ZOOM_SPEED, MIN_ZOOM, MAX_ZOOM)

func zoom_out() -> void:
    target_zoom = clampf(target_zoom + ZOOM_SPEED, MIN_ZOOM, MAX_ZOOM)

func _handle_rotation(delta: float) -> void:
    if not is_rotating:
        return
    var mouse_delta = _get_mouse_delta()
    rotation_degrees.y -= mouse_delta.x * ROTATION_SPEED * delta
    current_pitch = clampf(
        current_pitch - mouse_delta.y * ROTATION_SPEED * delta,
        MIN_PITCH, MAX_PITCH
    )
    camera_arm.rotation_degrees.x = current_pitch

func start_rotation() -> void:
    is_rotating = true
    free_roam = true

func stop_rotation() -> void:
    is_rotating = false

# ── Keyboard Pan (W/A/S/D moves the CAMERA, never the player character) ──────
func _handle_keyboard_pan(delta: float) -> void:
    var input_dir = Vector3.ZERO
    var forward = -camera.global_transform.basis.z
    forward.y = 0
    forward = forward.normalized()
    var right = camera.global_transform.basis.x
    right.y = 0
    right = right.normalized()
    if Input.is_action_pressed("camera_pan_forward"):   # W
        input_dir += forward
    if Input.is_action_pressed("camera_pan_backward"):  # S
        input_dir -= forward
    if Input.is_action_pressed("camera_pan_left"):       # A
        input_dir -= right
    if Input.is_action_pressed("camera_pan_right"):      # D
        input_dir += right
    if input_dir != Vector3.ZERO:
        free_roam = true
        global_position += input_dir.normalized() * KEYBOARD_PAN_SPEED * delta

# ── Edge Scrolling (mouse at screen edge, same effect as keyboard pan) ──────
func _handle_edge_scroll(delta: float) -> void:
    if _is_in_combat() and not free_roam:
        return
    var viewport_size = get_viewport().get_visible_rect().size
    var mouse_pos = get_viewport().get_mouse_position()
    var scroll_dir = Vector3.ZERO
    var forward = -camera.global_transform.basis.z
    forward.y = 0
    forward = forward.normalized()
    var right = camera.global_transform.basis.x
    right.y = 0
    right = right.normalized()
    if mouse_pos.x < EDGE_SCROLL_MARGIN:
        scroll_dir -= right
    elif mouse_pos.x > viewport_size.x - EDGE_SCROLL_MARGIN:
        scroll_dir += right
    if mouse_pos.y < EDGE_SCROLL_MARGIN:
        scroll_dir += forward
    elif mouse_pos.y > viewport_size.y - EDGE_SCROLL_MARGIN:
        scroll_dir -= forward
    if scroll_dir != Vector3.ZERO:
        free_roam = true
        global_position += scroll_dir.normalized() * EDGE_SCROLL_SPEED * delta

# ── Follow Target ────────────────────────────────────────────────────────────
func _handle_follow(delta: float) -> void:
    if follow_target == null or free_roam:
        return
    global_position = global_position.lerp(
        follow_target.global_position,
        delta * FOLLOW_SPEED
    )

func set_follow_target(target: Node3D) -> void:
    follow_target = target
    free_roam = false

func recenter_on_target() -> void:
    free_roam = false

func snap_to_target() -> void:
    if follow_target:
        global_position = follow_target.global_position
        free_roam = false

func on_turn_started(active_unit: Node3D) -> void:
    set_follow_target(active_unit)
    free_roam = false

func on_combat_ended() -> void:
    set_follow_target(EventBus.get_player_node())

func _get_mouse_delta() -> Vector2:
    return Input.get_last_mouse_velocity() * 0.001

func _is_in_combat() -> bool:
    return GameState.current_phase == GameState.Phase.COMBAT

func reset_to_default_angle() -> void:
    current_pitch = DEFAULT_PITCH
    camera_arm.rotation_degrees.x = current_pitch
    target_zoom = DEFAULT_ZOOM
```

### Input Map

Register these in Godot's Input Map (Project Settings → Input Map):

| Action Name | Default Binding | Behaviour |
|---|---|---|
| `camera_pan_forward` | W | Pan camera forward |
| `camera_pan_backward` | S | Pan camera backward |
| `camera_pan_left` | A | Pan camera left |
| `camera_pan_right` | D | Pan camera right |
| `move_to_point` | Left Mouse Click | Move player character to clicked point (click-to-move) |
| `examine_interact` | Right Mouse Click | Examine/interact with whatever's under the cursor |
| `camera_rotate_hold` | Middle Mouse Button | Hold to rotate camera |
| `camera_zoom_in` | Scroll Wheel Up | Zoom toward minimum distance |
| `camera_zoom_out` | Scroll Wheel Down | Zoom toward maximum distance |
| `camera_recenter` | Home Key / Middle Click | Snap back to follow active unit |
| `camera_rotate_left` | Q | Rotate camera left (keyboard alt) |
| `camera_rotate_right` | E | Rotate camera right (keyboard alt) |
| `camera_pitch_up` | (optional) | Tilt toward more overhead |
| `camera_pitch_down` | (optional) | Tilt toward more angled |

### Combat vs. Exploration Behavior

**Exploration:** camera pans via WASD or mouse-edge-scroll; click-to-move drives the character; recenter
brings camera back to the player; full rotation/zoom available.

**Combat:** camera pans to the newly active unit each turn start; WASD/edge-scroll disabled by default;
manual rotate/zoom still available; recenter snaps to active unit; follows next unit on turn end.

**Cutscenes/dialogue:** handed off to a `CinematicCameraController`; player input disabled; returns smoothly
on exit.

---

## Character Movement Feel

Triggered exclusively by `move_to_point` (left-click), never by direct keyboard input — see Controls & Input
Scheme, above.

```gdscript
class_name PlayerMovementController extends Node3D

@export var move_speed: float = 5.0
@export var rotation_speed: float = 10.0

var target_position: Vector3
var is_moving: bool = false
var current_path: Array[Vector3] = []

func move_along_path(path: Array[Vector3]) -> void:
    current_path = path
    is_moving = true

func _process(delta: float) -> void:
    if not is_moving or current_path.is_empty():
        return
    var target = current_path[0]
    var direction = (target - global_position)
    direction.y = 0
    if direction.length() < 0.1:
        current_path.pop_front()
        if current_path.is_empty():
            is_moving = false
            EventBus.emit_signal("movement_completed")
        return
    global_position = global_position.move_toward(target, move_speed * delta)
    if direction.length() > 0.01:
        var target_rotation = atan2(direction.x, direction.z)
        rotation.y = lerp_angle(rotation.y, target_rotation, rotation_speed * delta)
```

Key points: characters move smoothly along a path rather than snapping tile-to-tile; the path is still
grid-based and AP-costed underneath — only the *visual* movement is animated fluidly between grid positions;
rotation faces the direction of travel for natural-feeling movement.

---

## Performance Notes

The constrained-by-default camera is significantly more performance-friendly than a full free camera at
every tier below Ultra, because environments can be optimized for a known range of viewing angles, occlusion
culling is more predictable, LOD transitions are less jarring with a bounded camera-distance range, and
shadow maps can be sized for expected view distance rather than worst-case ground-level zoom. This aligns
with the minimum hardware target (see `08_Scalable_Graphics_and_Hardware_Tiers.md`).
