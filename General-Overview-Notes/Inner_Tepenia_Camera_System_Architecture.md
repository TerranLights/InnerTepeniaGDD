# Inner Tepenia — Camera System Architecture
**Architecture Supplement to Technical Architecture Document v0.1**
**Reference Feel: Wasteland 3 (semi-free isometric, constrained rotation)**

---

## 1. Design Goal

The camera should feel like **Wasteland 3** — a semi-free isometric perspective that:
- Maintains a primarily overhead-ish default angle that reads clearly for tactical turn-based combat
- Allows constrained rotation (not full 360° ground-level freedom like BG3)
- Supports smooth zoom within a readable overhead range
- Never makes the player feel "lost" in the world or lose tactical readability
- Feels modern and cinematic compared to a fully locked classic isometric camera

This is distinct from:
- **True locked isometric** (Fallout 1/2) — no rotation at all
- **Full free camera** (BG3) — unrestricted pitch and zoom to ground level

---

## 2. Camera Parameters

These are starting values to be tuned during development:

```gdscript
# Rotation
const MIN_ROTATION_Y: float = 0.0       # degrees horizontal
const MAX_ROTATION_Y: float = 360.0     # full horizontal rotation allowed
const MIN_PITCH: float = -70.0          # degrees — most overhead
const MAX_PITCH: float = -30.0          # degrees — most angled (never ground level)
const DEFAULT_PITCH: float = -55.0      # degrees — default Wasteland 3-ish angle
const ROTATION_SPEED: float = 120.0     # degrees per second

# Zoom
const MIN_ZOOM: float = 8.0             # metres — closest zoom
const MAX_ZOOM: float = 30.0            # metres — furthest zoom
const DEFAULT_ZOOM: float = 18.0        # metres — default distance
const ZOOM_SPEED: float = 5.0           # metres per scroll tick

# Movement (following the player/active unit)
const FOLLOW_SPEED: float = 8.0         # lerp speed when recentering
const EDGE_SCROLL_SPEED: float = 15.0   # units per second when edge scrolling
const EDGE_SCROLL_MARGIN: float = 20.0  # pixels from screen edge to trigger scroll
```

---

## 3. Scene Structure

```
CameraRig (Node3D)          — moves horizontally to follow player/cursor
└── CameraArm (Node3D)      — handles rotation and pitch
    └── SpringArm3D         — handles zoom and collision avoidance
        └── Camera3D        — the actual camera
```

Using a `SpringArm3D` is important — it automatically pushes the camera forward if something solid (a wall, ceiling, terrain) is between the camera and its target, preventing the camera from clipping into geometry.

---

## 4. CameraController Script

```gdscript
class_name CameraController extends Node3D

# ── References ──────────────────────────────────────────────────────────────
@onready var camera_arm: Node3D = $CameraArm
@onready var spring_arm: SpringArm3D = $CameraArm/SpringArm3D
@onready var camera: Camera3D = $CameraArm/SpringArm3D/Camera3D

# ── State ────────────────────────────────────────────────────────────────────
var current_zoom: float = DEFAULT_ZOOM
var target_zoom: float = DEFAULT_ZOOM
var current_pitch: float = DEFAULT_PITCH
var is_rotating: bool = false
var follow_target: Node3D = null
var free_roam: bool = false  # true when player is manually panning

# ── Constants ────────────────────────────────────────────────────────────────
const MIN_PITCH: float = -70.0
const MAX_PITCH: float = -30.0
const DEFAULT_PITCH: float = -55.0
const MIN_ZOOM: float = 8.0
const MAX_ZOOM: float = 30.0
const DEFAULT_ZOOM: float = 18.0
const ZOOM_SPEED: float = 5.0
const ROTATION_SPEED: float = 120.0
const FOLLOW_SPEED: float = 8.0
const EDGE_SCROLL_SPEED: float = 15.0
const EDGE_SCROLL_MARGIN: float = 20.0

func _ready() -> void:
    spring_arm.spring_length = current_zoom
    camera_arm.rotation_degrees.x = current_pitch

func _process(delta: float) -> void:
    _handle_zoom(delta)
    _handle_rotation(delta)
    _handle_edge_scroll(delta)
    _handle_follow(delta)

# ── Zoom ─────────────────────────────────────────────────────────────────────
func _handle_zoom(delta: float) -> void:
    current_zoom = lerp(current_zoom, target_zoom, delta * 10.0)
    spring_arm.spring_length = current_zoom

func zoom_in() -> void:
    target_zoom = clampf(target_zoom - ZOOM_SPEED, MIN_ZOOM, MAX_ZOOM)

func zoom_out() -> void:
    target_zoom = clampf(target_zoom + ZOOM_SPEED, MIN_ZOOM, MAX_ZOOM)

# ── Rotation ─────────────────────────────────────────────────────────────────
func _handle_rotation(delta: float) -> void:
    if not is_rotating:
        return
    var mouse_delta = _get_mouse_delta()
    # Horizontal rotation — full 360 allowed
    rotation_degrees.y -= mouse_delta.x * ROTATION_SPEED * delta
    # Vertical pitch — constrained
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

# ── Edge Scrolling ───────────────────────────────────────────────────────────
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

# ── Combat Mode ───────────────────────────────────────────────────────────────
func on_turn_started(active_unit: Node3D) -> void:
    set_follow_target(active_unit)
    free_roam = false

func on_combat_ended() -> void:
    set_follow_target(EventBus.get_player_node())

# ── Helpers ───────────────────────────────────────────────────────────────────
func _get_mouse_delta() -> Vector2:
    return Input.get_last_mouse_velocity() * 0.001

func _is_in_combat() -> bool:
    return GameState.current_phase == GameState.Phase.COMBAT

func reset_to_default_angle() -> void:
    current_pitch = DEFAULT_PITCH
    camera_arm.rotation_degrees.x = current_pitch
    target_zoom = DEFAULT_ZOOM
```

---

## 5. Input Map

These actions should be registered in Godot's Input Map (Project Settings → Input Map):

| Action Name | Default Binding | Behaviour |
|---|---|---|
| `camera_rotate_hold` | Middle Mouse Button | Hold to rotate camera |
| `camera_zoom_in` | Scroll Wheel Up | Zoom toward minimum distance |
| `camera_zoom_out` | Scroll Wheel Down | Zoom toward maximum distance |
| `camera_recenter` | Home Key / Middle Click | Snap back to follow active unit |
| `camera_rotate_left` | Q | Rotate camera left (keyboard alt) |
| `camera_rotate_right` | E | Rotate camera right (keyboard alt) |
| `camera_pitch_up` | (optional) | Tilt toward more overhead |
| `camera_pitch_down` | (optional) | Tilt toward more angled |

---

## 6. Combat vs Exploration Behaviour

### Exploration Mode
- Freely follows the player character
- Edge scrolling enabled — player can pan away from character
- Recenter button brings camera back
- Full rotation and zoom available

### Combat Mode
- Camera pans to the newly active unit at the start of each turn
- Edge scrolling disabled by default
- Player can still manually rotate and zoom to assess the battlefield
- Recenter button snaps back to active unit
- On turn end, camera follows next active unit

### Cutscenes / Dialogue
- Camera control handed off to a `CinematicCameraController`
- Player input disabled
- Returns smoothly to gameplay camera on exit

---

## 7. Character Movement Feel

To match the Wasteland 3 fluid movement feel rather than rigid tile-snapping:

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

Key points:
- Characters move **smoothly along a path** rather than snapping tile-to-tile
- The path is still grid-based and AP-costed — the visual movement is animated fluidly between grid positions
- Rotation faces the direction of travel, giving characters natural-feeling movement

---

## 8. Where This Fits in the Build Order

Slips into **Phase 1** as a dedicated step:

**Updated Phase 1 — Foundation:**
1. Godot orientation: scenes, nodes, signals, GDScript basics
2. Simple isometric tilemap prototype (movement only, no combat)
3. **Camera system prototype** — implement `CameraController`, tune parameters to match Wasteland 3 feel
4. Wire character movement to camera — click to move, camera follows smoothly
5. Basic GDExtension hello-world (get C++ pipeline working)

Getting the camera feel right early is important — it affects how environments are designed, how UI is positioned, and how combat reads on screen.

---

## 9. Performance Notes

The Wasteland 3-style constrained camera is significantly more performance-friendly than a full BG3-style free camera because:

- Environments can be optimised for a known range of viewing angles
- Occlusion culling is more predictable
- LOD transitions are less jarring because camera distance range is bounded
- Shadow maps can be sized for expected view distance rather than worst-case ground-level zoom

This aligns well with the minimum hardware target (Ryzen 3, GTX 1050, 8GB RAM).

---

*Supplement to Inner_Tepenia_Technical_Architecture.md. Commit alongside main architecture document and reputation supplement.*
