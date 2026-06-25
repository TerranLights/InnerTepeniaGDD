# Movement, Camera & Grid System

**Last Updated:** June 2026

This document details the spatial representation, movement, camera, and pathfinding systems for *Inner Tepenia*.

---

## 1. Design Goals

- **Tactical precision** — Clear, predictable AP costs and positioning for turn-based combat.
- **Modern, satisfying movement** — Smooth, weighty, and responsive animation similar to *Baldur’s Gate 3*.
- **Strong district atmosphere** — The circular, color-coded districts of Concordia should look beautiful and distinct.
- **Speedrun / minmax friendly** — Grid rules must remain clean and readable.

---

## 2. Grid System: Hexagonal + Navmesh Hybrid

**Recommended:** Hexagonal grid as the **logical / rules layer**, combined with a **navmesh** for the **visual / movement layer**.

### Why Hex Grid?
- Every adjacent tile has identical distance (no awkward diagonal math).
- More natural flanking and positioning in combat.
- Better suited to organic sci-fi environments (hydroponic gardens, industrial clutter, Frostlands, undergrid tunnels).
- Cleaner AP calculations overall.

### How the Hybrid Works
- **Hex Grid Layer** (Rules):
  - AP cost, range, line-of-sight, cover, and tactical highlighting are all calculated on clean hex tiles.
- **Navmesh Layer** (Feel):
  - Characters follow smooth, intelligent, curved paths around obstacles.
  - Movement animation is fluid and cinematic (like BG3).
  - Final AP cost is snapped to the hex grid for perfect consistency.

**Exploration Mode**  
Real-time movement (WASD + click-to-move) with full navmesh pathing. No AP cost.

**Combat Mode**  
Turn-based. Player sees glowing path preview with exact AP cost. Character then executes smooth animated movement.

---

## 3. Camera System

- **Primary View**: Modern rotatable 3D isometric (similar to *Wasteland 3*, but smoother).
- Players can freely orbit the party for cinematic shots of the districts.
- Toggleable **Tactical Top-Down Mode** (like BG3’s “O” key) for maximum clarity during complex fights.
- Features:
  - Smooth zooming, panning, and slight cinematic tilt.
  - Height-aware camera (ramps, multi-level areas, undergrid entrances).
  - District-specific camera presets (e.g., slightly lower angle in dense indoor areas).

---

## 4. Handling Straight Walls in Indoor Rooms

Hex grids can clash with rectangular architecture. Mitigation strategies (in priority order):

1. **Art-First Approach (Recommended)**  
   Build rooms with natural straight walls. Hex grid is an invisible/subtle overlay. Navmesh defines precise walkable space. Hex centers determine AP costing.

2. **Grid Rotation**  
   Rotate hex orientation per map so one flat side aligns with primary wall directions.

3. **Hybrid Grid Zones**  
   Use hex outdoors / organic areas and square (or offset) grid in very strict rectangular interiors when necessary, with smooth transitions.

4. **Design Approach**  
   Favor larger, more open or organic interiors where possible (medical wards in Cancer, factories in Capricorn, etc.).

5. **Visual Polish**  
   Make the combat grid subtle or toggleable (default off, hotkey “G”). Use floor patterns, lighting, and props to guide player intuition.

---

## 5. Animation & Pathing Priorities

- High-quality animation blending and inverse kinematics (good foot placement on snow, ramps, uneven floors).
- Contextual animations (brushing snow, ducking under pipes, interacting with medical equipment).
- Excellent obstacle avoidance and formation following.
- Pre-visualized movement paths with real-time AP cost feedback.

---

## 6. Integration Notes

- **APManager** reads from the hex grid.
- **DistrictResource** can contain optional grid/camera overrides.
- **CombatManager** uses hex-based tactical calculations.
- Save system stores both hex coordinate + visual position.

---

**Status:** Ready for implementation planning.  
**References:** Baldur’s Gate 3 (motion feel), Wasteland 3 (camera + grid hybrid).
