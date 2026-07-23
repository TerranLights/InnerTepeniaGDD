# Scalable Graphics & Hardware Tiers

Builds directly on `05_Grid_Movement_and_Camera.md`'s `CameraController` — the camera-freedom scaling
described here adjusts that same controller's pitch/zoom ranges per hardware tier, it doesn't replace it.

**Design Philosophy: every tier is genuinely good. No player is punished.**

---

## Core Philosophy

> The story, systems, characters, and world are identical across all tiers. Only the presentation scales.

A player on Low is not playing a lesser game — they're playing a version optimized for their hardware. A
player on Ultra isn't getting a different game, just more visual fidelity and camera freedom. If a design
decision only works on High or Ultra, it needs reconsidering. If a piece of environmental storytelling only
reads clearly from ground level with a free camera, it needs to also read clearly from the constrained
overhead angle everyone starts at.

---

## Hardware Tier Targets

| Tier | CPU | GPU | VRAM | RAM | Storage |
|---|---|---|---|---|---|
| **Low** | AMD Ryzen 3 / Intel i3 (dual-core) | GTX 1050 / RX 570 | 4GB | 8GB | HDD acceptable |
| **Medium** | AMD Ryzen 5 / Intel i5 (6-core) | GTX 1660 Super / RX 580 | 6GB | 16GB | SSD recommended |
| **High** | AMD Ryzen 7 / Intel i7 (8-core) | RTX 3070 / RX 6700 XT | 8GB | 16GB | SSD strongly recommended |
| **Ultra** | AMD Ryzen 9 / Intel i9 (12-core+) | RTX 4080 / RX 7900 XT | 16GB+ | 32GB | NVMe SSD recommended |

---

## Camera Tier Definitions

Camera behavior scales with hardware tier and can be manually overridden in settings, independent of the
graphics preset. All four tiers use the same `CameraController` from `05_Grid_Movement_and_Camera.md` — only
its pitch/zoom range constants change.

### Low — Constrained Camera (Default)
- Pitch range: -70° to -40° (overhead to moderate angle)
- Full 360° horizontal rotation
- Zoom range: 12m to 25m
- Edge scrolling / WASD panning enabled
- No cinematic zoom-to-ground capability
- Asset streaming optimized for constrained view frustum

### Medium — Extended Camera
- Pitch range: -75° to -25° (slightly wider than Low)
- Full 360° horizontal rotation
- Zoom range: 10m to 30m
- Edge scrolling / WASD panning enabled
- Minor cinematic dips toward angled view during dialogue
- **BG3-style up-close dialogue camera shots: stretch goal only, not guaranteed.** Implement if
  performance allows once Medium-tier dialogue scenes are actually profiled; every dialogue scene must also
  read and stage correctly *without* it, since Medium can't be relied on to have it.
- Asset streaming still primarily optimized for overhead angles

### High — Semi-Free Camera
- Pitch range: -85° to -15° (near-overhead to strongly angled, not quite ground level)
- Full 360° horizontal rotation
- Zoom range: 8m to 35m
- Edge scrolling / WASD panning enabled
- **BG3-style up-close dialogue camera shots — required on this tier.** Close facial framing during
  conversations, not just "more dramatic angles" — this is a firm requirement, not a nice-to-have.
- Dynamic asset streaming for wider view range

### Ultra — Full Free Camera (BG3-Style)
- Pitch range: -90° to 0° (fully overhead to near ground level)
- Full 360° horizontal rotation
- Zoom range: 5m to 40m
- Edge scrolling / WASD panning enabled
- **BG3-style up-close dialogue camera shots — required on this tier**, same requirement as High. Note this
  means the camera is *capable of* framing a close, static shot on the current speaker — not that the camera
  needs to move around or roam during the conversation itself. The "full cinematic camera freedom" below
  refers to exploration only.
- Full cinematic camera freedom during exploration
- Maximum asset streaming budget, full LOD range active

**Note on controls across tiers:** the click-to-move / right-click-examine / WASD-pans-camera scheme from
`05_Grid_Movement_and_Camera.md` doesn't change between tiers — only how *far* the camera can pitch and zoom
changes. A Low-tier player still controls the game identically to an Ultra-tier player, just within a
tighter camera-freedom window.

**Note on the dialogue camera specifically:** this is a separate concern from the exploration/combat
pitch-zoom ranges above — it's about what `05_Grid_Movement_and_Camera.md`'s `CinematicCameraController`
actually does once dialogue camera control is handed to it. **Required on High and Ultra: the camera must be
*capable of* framing close, static up-close shots on the current speaker** (BG3-style close facial framing) —
this is about shot framing, not about the camera moving around or roaming during the conversation itself.
Medium gets it only if profiling shows it's actually affordable there — a stretch goal, not a commitment. Low
does not get up-close dialogue shots at all; dialogue on Low uses the standard exploration camera angle,
consistent with Low's whole "same game, simpler presentation" design philosophy. Every dialogue scene must be
authored to read correctly on Low's plainer camera first, with the up-close shots on High/Ultra layered on
top as enhancement, never as the only way a scene was designed to be read.

---

## Graphics Settings Per Tier

### Shadows

| Setting | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Shadow Quality | Baked only | Low dynamic | Medium dynamic | High dynamic |
| Shadow Distance | N/A | 20m | 40m | 80m |
| Shadow Map Size | N/A | 1024px | 2048px | 4096px |
| Soft Shadows | Off | Off | On | On |
| Ambient Occlusion | Off | Off | SSAO | HBAO |

### Lighting

| Setting | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Dynamic Lights | 4 max | 8 max | 16 max | Unlimited |
| Volumetric Fog | Off | Off | On (light) | On (full) |
| Bloom | Off | Low | Medium | High |
| Light Shafts | Off | Off | On | On |
| Emissive Glow | Simple | Simple | Full | Full + bloom |
| Global Illumination | Baked | Baked | SDFGI (Godot 4) | SDFGI + reflections |

### Textures

| Setting | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Texture Resolution | 512px max | 1024px max | 2048px max | 4096px max |
| Texture Filtering | Bilinear | Bilinear | Trilinear | Anisotropic 16x |
| Normal Maps | Off | On (simple) | On (full) | On (full) |
| Specular Maps | Off | Off | On | On |
| Texture Streaming | Aggressive | Moderate | Light | Minimal |

### Geometry & LOD

| Setting | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Draw Distance | 60m | 100m | 150m | 250m |
| LOD Bias | Aggressive | Moderate | Low | Minimal |
| NPC Density | 50% | 75% | 100% | 100% + crowds |
| Foliage/Detail | Off | Low | Medium | High |
| Reflection Probes | 1 per zone | 2 per zone | 4 per zone | 8 per zone |

### Post-Processing

| Setting | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Anti-Aliasing | Off / FXAA | FXAA | TAA | TAA + MSAA |
| Depth of Field | Off | Off | Subtle | Full cinematic |
| Motion Blur | Off | Off | Off | Optional |
| Color Grading | Basic LUT | Basic LUT | Full LUT | Full LUT |
| Chromatic Aberration | Off | Off | Off | Optional |
| Screen Space Reflections | Off | Off | On | On (high quality) |

### Aurora Australis (Signature Visual Feature)

The aurora australis is a key visual identity element of Concordia and gets special treatment across tiers —
it should always be present and beautiful, even on Low.

| Setting | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Aurora Rendering | Flat shader, 2 layers | Volumetric, 3 layers | Volumetric, 5 layers | Full volumetric, 8 layers |
| Aurora Animation | Simple sine wave | Smooth animation | Full fluid simulation | Full fluid + light interaction |
| Aurora Lighting | No scene lighting | Subtle ambient tint | Dynamic ambient light | Full dynamic scene lighting |
| Aurora Reflection | Off | Off | In water/puddles | Full reflections |

> **Design note:** the aurora is visible from every district, at every tier. On Low it should still be
> gorgeous, just simpler — a player seeing it over the Aries power core should still feel something. Don't
> let it become a flat skybox texture.

---

## GraphicsSettingsManager (Autoload)

```gdscript
class_name GraphicsSettingsManager extends Node

enum Tier { LOW, MEDIUM, HIGH, ULTRA }
enum CameraMode { CONSTRAINED, EXTENDED, SEMI_FREE, FULL_FREE }

var current_tier: Tier = Tier.LOW
var current_camera_mode: CameraMode = CameraMode.CONSTRAINED
var settings: Dictionary = {}

func _ready() -> void:
    _load_settings()
    apply_tier(current_tier)

func apply_tier(tier: Tier) -> void:
    current_tier = tier
    settings = _get_tier_settings(tier)
    _apply_shadow_settings()
    _apply_lighting_settings()
    _apply_texture_settings()
    _apply_lod_settings()
    _apply_post_processing()
    _apply_aurora_settings()
    # Camera mode follows tier by default unless manually overridden
    if not _is_camera_manually_overridden():
        apply_camera_mode(_get_default_camera_mode(tier))
    _save_settings()
    EventBus.emit_signal("graphics_settings_changed", tier)

func apply_camera_mode(mode: CameraMode) -> void:
    current_camera_mode = mode
    var camera = get_node("/root/CameraController")
    match mode:
        CameraMode.CONSTRAINED:
            camera.set_pitch_range(-70.0, -40.0)
            camera.set_zoom_range(12.0, 25.0)
        CameraMode.EXTENDED:
            camera.set_pitch_range(-75.0, -25.0)
            camera.set_zoom_range(10.0, 30.0)
        CameraMode.SEMI_FREE:
            camera.set_pitch_range(-85.0, -15.0)
            camera.set_zoom_range(8.0, 35.0)
        CameraMode.FULL_FREE:
            camera.set_pitch_range(-90.0, 0.0)
            camera.set_zoom_range(5.0, 40.0)
    _save_settings()

func _get_default_camera_mode(tier: Tier) -> CameraMode:
    match tier:
        Tier.LOW: return CameraMode.CONSTRAINED
        Tier.MEDIUM: return CameraMode.EXTENDED
        Tier.HIGH: return CameraMode.SEMI_FREE
        Tier.ULTRA: return CameraMode.FULL_FREE
    return CameraMode.CONSTRAINED

func auto_detect_tier() -> Tier:
    # Godot 4 exposes some hardware info via RenderingServer
    var vram_mb = RenderingServer.get_rendering_info(
        RenderingServer.RENDERING_INFO_VIDEO_MEM_USED) / 1048576
    var cpu_count = OS.get_processor_count()
    if vram_mb < 5000 or cpu_count <= 2:
        return Tier.LOW
    elif vram_mb < 7000 or cpu_count <= 6:
        return Tier.MEDIUM
    elif vram_mb < 12000 or cpu_count <= 8:
        return Tier.HIGH
    return Tier.ULTRA

func _apply_shadow_settings() -> void:
    match current_tier:
        Tier.LOW:
            RenderingServer.directional_shadow_atlas_set_size(0, false)
        Tier.MEDIUM:
            RenderingServer.directional_shadow_atlas_set_size(1024, false)
        Tier.HIGH:
            RenderingServer.directional_shadow_atlas_set_size(2048, true)
        Tier.ULTRA:
            RenderingServer.directional_shadow_atlas_set_size(4096, true)

func _apply_post_processing() -> void:
    var env = _get_world_environment()
    if env == null:
        return
    match current_tier:
        Tier.LOW:
            env.glow_enabled = false
            env.ssao_enabled = false
            env.sdfgi_enabled = false
        Tier.MEDIUM:
            env.glow_enabled = true
            env.glow_intensity = 0.3
            env.ssao_enabled = false
            env.sdfgi_enabled = false
        Tier.HIGH:
            env.glow_enabled = true
            env.glow_intensity = 0.6
            env.ssao_enabled = true
            env.sdfgi_enabled = true
        Tier.ULTRA:
            env.glow_enabled = true
            env.glow_intensity = 1.0
            env.ssao_enabled = true
            env.sdfgi_enabled = true
            env.ssr_enabled = true

func _get_world_environment() -> Environment:
    var env_node = get_tree().get_first_node_in_group("world_environment")
    if env_node and env_node is WorldEnvironment:
        return env_node.environment
    return null

func _load_settings() -> void:
    var config = ConfigFile.new()
    if config.load("user://graphics_settings.cfg") == OK:
        current_tier = config.get_value("graphics", "tier", Tier.LOW)
        current_camera_mode = config.get_value("graphics", "camera_mode",
            _get_default_camera_mode(current_tier))

func _save_settings() -> void:
    var config = ConfigFile.new()
    config.set_value("graphics", "tier", current_tier)
    config.set_value("graphics", "camera_mode", current_camera_mode)
    config.set_value("graphics", "camera_manually_overridden",
        _is_camera_manually_overridden())
    config.save("user://graphics_settings.cfg")

func _is_camera_manually_overridden() -> bool:
    return current_camera_mode != _get_default_camera_mode(current_tier)

func _get_tier_settings(tier: Tier) -> Dictionary:
    match tier:
        Tier.LOW:
            return {
                "max_dynamic_lights": 4, "draw_distance": 60.0,
                "npc_density": 0.5, "texture_max_size": 512, "aurora_layers": 2,
            }
        Tier.MEDIUM:
            return {
                "max_dynamic_lights": 8, "draw_distance": 100.0,
                "npc_density": 0.75, "texture_max_size": 1024, "aurora_layers": 3,
            }
        Tier.HIGH:
            return {
                "max_dynamic_lights": 16, "draw_distance": 150.0,
                "npc_density": 1.0, "texture_max_size": 2048, "aurora_layers": 5,
            }
        Tier.ULTRA:
            return {
                "max_dynamic_lights": 999, "draw_distance": 250.0,
                "npc_density": 1.0, "texture_max_size": 4096, "aurora_layers": 8,
            }
    return {}
```

---

## Settings UI Structure

```
Graphics Settings
├── Preset
│   ├── [Auto-Detect]         ← runs auto_detect_tier() on click
│   ├── Low
│   ├── Medium
│   ├── High
│   └── Ultra
│
├── Camera Mode               ← independent of graphics preset
│   ├── Constrained [default on Low/Medium]
│   ├── Extended
│   ├── Semi-Free
│   └── Full Free (BG3-style) [default on Ultra]
│   └── [i] Note: Full Free requires High/Ultra for best performance
│
└── Advanced (expandable)
    ├── Shadow Quality
    ├── Dynamic Lights
    ├── Ambient Occlusion
    ├── Bloom
    ├── Volumetric Fog
    ├── Anti-Aliasing
    ├── Draw Distance
    ├── NPC Density
    ├── Texture Quality
    ├── Aurora Quality
    └── [Reset to Preset Defaults]
```

**UX notes:** Camera Mode is always independently adjustable regardless of graphics preset — a Low player
who wants to try Full Free camera can enable it, the game warns about performance but doesn't block them.
Auto-Detect runs on first launch and suggests a preset the player can override immediately. Advanced settings
allow granular mixing (e.g., Ultra shadows but Low NPC density). Changes apply in real-time with a "Revert in
15 seconds" safety timer, like most modern games.

---

## First Launch Experience

```gdscript
func _on_first_launch() -> void:
    # 1. Run hardware detection
    var detected_tier = GraphicsSettingsManager.auto_detect_tier()

    # 2. Show detection result to player
    # "We detected your hardware and suggest: MEDIUM settings
    #  Camera: Extended
    #  You can change these at any time in Settings."

    # 3. Offer quick options
    # [Use Suggested Settings]  [Let Me Choose]  [Start on Low]

    # 4. Apply and save
    GraphicsSettingsManager.apply_tier(detected_tier)
```

The first launch screen should be warm and reassuring, not a wall of technical options: *"We've got you.
Here's what we think works best for your machine. You're in control."*

---

## Environmental Design Rules for All Tiers

- **Color palette carries the atmosphere**, not just lighting. Scorpio's crimson and violet should read even
  with baked flat lighting on Low. (This is an art-directed mood palette for one specific district, not a
  literal per-district color-coding scheme — see the note in `05_Grid_Movement_and_Camera.md`'s Core
  Philosophy about the dev-facing map diagram's colors not being an in-game visual design.)
- **Silhouettes matter on Low.** The distinctive shape of the Aries power core chimneys, the Virgo tunnel
  arches, the Leo amphitheater — these should be immediately readable shapes even without dynamic lighting.
- **Aurora is always present**, at every tier — Concordia's signature sky. Scales in complexity, never
  disappears.
- **NPCs are never absent on Low** — reduced in density (50%) but districts still feel inhabited. An empty
  Taurus district breaks immersion regardless of hardware.
- **Sound design compensates where visuals scale down.** On Low, where volumetric fog and dynamic lights are
  off, rich ambient audio (Virgo's mechanical hum, Aries's rumbling furnaces, Leo's distant music) carries
  atmosphere the visuals can't.

---

## The Promise to the Player

> Whether you're playing on a seven-year-old laptop or a brand new high-end rig, you are playing the same
> game. The same story. The same world. The same choices that matter. We just make sure it looks its best on
> whatever you have.
