# Character Asset Pipeline

**Confirmed 2026-07-23:** character models are created in **DAZ Studio** first, then relocated to
**Blender** for cleanup and tidying, then imported into **Godot**. This is a production-pipeline note, not a
code-architecture one in the strict sense, but lives in this folder alongside the other "how it's actually
built" documentation.

---

## The Pipeline

1. **DAZ Studio** — character creation (Genesis 8/9 base figures, morphs, textures, posing). DAZ figures
   ship already rigged — see Rigging, below.
2. **Blender**, via the **Diffeomorphic Daz to Blender** bridge — the standard route in, since it carries
   over morphs and materials far more cleanly than a raw FBX/glTF export straight out of DAZ Studio. This is
   the cleanup/tidying stage:
   - **Decimation/retopology.** DAZ meshes are render-oriented (tens of thousands of polygons even before
     subdivision) and need reducing for real-time use.
   - **Material rebuild.** DAZ's Iray/3Delight shaders don't translate to Godot's material system at all —
     textures carry over, but materials need rebuilding as Godot `StandardMaterial3D`s (or a custom shader),
     typically easiest to at least start in Blender.
   - **Rig cleanup** — see below.
3. **Godot** — final import as glTF/GLB. Godot doesn't function as a rigging/cleanup tool itself; whatever
   skeleton and mesh state exists at Blender export time is what Godot receives.

---

## Rigging

**DAZ Genesis 8/9 figures come pre-rigged** — a full skeleton and skin weights are already part of the base
figure, which is how DAZ's own posing and animation tools work in the first place. The Diffeomorphic bridge
carries that existing skeleton into Blender intact. **Rigging from scratch is not a step in this pipeline.**

What *does* typically need doing in Blender, as part of the same cleanup stage:
- **Facial rig simplification.** DAZ's skeleton includes an extensive bone-driven facial rig built to power
  its own expression-dial system — often more bones than a real-time engine needs, worth pruning/simplifying
  here rather than carrying the full DAZ facial rig into Godot as-is.
- **Cross-character rig consistency — open question, not yet decided.** Whether every character should share
  one common rig/bone-naming structure (so a single authored animation set — walk, idle, combat cycles —
  can be retargeted across the whole companion roster) or whether each character simply keeps DAZ's native
  rig independently. This has real production-time implications depending on how much animation reuse is
  planned across the roster; decide once that's clearer, don't default to either answer.

---

## Open Questions

- Cross-character rig consistency (see above).
- Whether decimation targets should vary by the hardware-tier LOD system already established in
  `08_Scalable_Graphics_and_Hardware_Tiers.md`, or whether one decimated asset serves all tiers.
- DAZ asset licensing — purchased figures/morphs/textures are generally fine to use *in* a shipped
  commercial game, but not to redistribute as raw assets; terms vary per asset and DAZ's EULA has changed
  over time, so verify current terms for whatever specific base content gets used before committing to it.
