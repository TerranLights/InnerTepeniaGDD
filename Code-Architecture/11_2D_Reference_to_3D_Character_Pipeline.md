# 2D Reference-to-3D Character Pipeline

**Confirmed 2026-07-23 — this is not a hypothetical tool category, it's the real production pipeline for
the entire companion cast.** The companions in Inner Tepenia are not separately-designed 3D characters with
concept-art support — **the dolls themselves, as they already exist in every
`Worldspace/Characters/Dolls/**/Reference_Images/` folder, ARE the companion characters.** Their visual
identity is already locked in as 2D reference images; the production task is converting that existing 2D
identity into a real-time 3D model, not designing a new character from a blank page.

**Scale:** 75 `Reference_Images/` folders currently exist across the Dolls tree (recruitable companions,
past-history figures, off-world/MIA characters, etc.) — this is a cast-wide pipeline need, not a one-off.

**Composition, confirmed by the developer 2026-07-23:** the large majority of reference images across the
corpus are real photography; some (not most) are AI-generated. No illustrated 2D art confirmed anywhere in
the corpus (see the filename-heuristic correction below) — the practical pipeline need is overwhelmingly a
photo-to-3D (and AI-render-to-3D) problem, not an illustration-to-3D one.

---

## The Reference Material Is Not Uniform — a Real Finding, With One Correction Already Made

Checked directly across several characters' `Reference_Images/` folders. Confirmed source-material types
found so far:

- **AI-generated images** — e.g. Kendra Heinrich's folder (`"Kendra the goddess - standing in a Sci-Fi
  setting..." [v.03], [v.04]...`) — prompt-as-filename with version-iteration numbering, photorealistic
  render style.
- **Real photography** — e.g. Seica Cenilaithe's folder (`5A8A0973-1.jpeg`, `5A8A1202.jpeg`...), genuine
  Canon camera file-numbering from an actual photoshoot; and Ayako Hayashi's folder
  (`black dress FZfTeWmVQAAVV17.jpg`, `black dress s121998930727217230_p403_i59...`) — **confirmed by the
  developer to be real photography of a physical doll/figure, not illustration**, despite the
  Pixiv/social-platform-style filenames.

**Correction, same session:** an earlier draft of this file guessed Ayako's images were illustrated 2D art
based on the filename pattern alone (Pixiv-style posting-ID filenames). That guess was wrong, and the
developer corrected it directly. **The lesson to keep: filename origin (which platform an image was
downloaded from) does not reliably indicate whether the content itself is a photograph or an
illustration** — Pixiv and similar platforms host photography (including doll/figure photography) as well
as illustration. Determining actual source-material type requires looking at the image content itself, not
inferring from filename conventions. No confirmed illustrated 2D art has actually been found in this corpus
yet — that category may not exist in practice among the current reference images, though it hasn't been
exhaustively ruled out either.

**Why this still matters for tool choice, even without a confirmed illustration case:** photo-to-3D and
illustration-to-3D remain different problem domains in general, and it's still worth checking each
character's actual reference images directly (not their filenames) before assuming which tool category
fits. Tools built around real/photorealistic faces (Reallusion Headshot, most general image-to-3D services) are
tuned for the first two categories. Illustrated/anime-style source material is a different pipeline
territory (the VRChat/VTuber avatar-creation space has its own tools and conventions built specifically
around turning 2D illustrated character art into 3D models) and should not be assumed to work well through
a photo-oriented tool without checking first. **Practical implication: which tool gets used should be
decided per-character (or per source-material category), not as one blanket choice for the whole cast.**

---

## Tool Landscape

**General-purpose image-to-3D:** Meshy AI, Tripo3D, CSM.ai, Rodin (Hyper3D/Deemos). Feed in one or more 2D
images, get back a textured mesh. Typically **unrigged, and topology is usually messy** (a 2D image can't
see a character's back/sides, so the tool has to guess at unseen geometry) — expect a retopology pass
before this is animation-ready.

**Photorealistic character-specific:** Reallusion's **Headshot** plugin (for Character Creator) takes a 2D
photo and fits a 3D likeness onto an *already-rigged* CC4 base body — the one tool in this space that
skips the "unrigged mesh" problem entirely, at least for the head/likeness. Best fit for the photographic
and AI-generated categories confirmed above — which, as far as checked so far, may cover the whole corpus.

**Illustrated/anime-style source material:** low priority given the confirmed composition above (large
majority photography, some AI-generated, no confirmed illustrated art) — no specific tool needed yet. If an
illustrated case ever does turn up, the VTuber/VRChat avatar space is the natural place to look first, since
2D-illustration-to-3D-avatar is already a mature, well-precedented pipeline there.

---

## How This Relates to the DAZ Studio Pipeline (`10_Character_Asset_Pipeline.md`)

**Open question, not yet resolved.** Two pipelines now exist on paper — DAZ Studio (build a character from
scratch inside DAZ, already-rigged output) and this one (start from an existing 2D reference image, AI-
generate a 3D approximation, likely unrigged). Possible relationships between them, none chosen yet:
- **Split by character:** companions with existing reference art use this pipeline; new NPCs/crowd
  characters without pre-existing 2D art get built directly in DAZ instead.
- **Hybrid:** use DAZ to construct a base body/likeness approximating a reference image's proportions,
  rather than relying on AI mesh generation for the body — potentially higher quality and already rigged,
  at the cost of more manual likeness-matching effort per character.
- **Fully separate:** this pipeline replaces DAZ for every companion; DAZ is used elsewhere or not at all.

Whichever direction this goes, **Blender remains the shared cleanup stage either way** — retopology,
material rebuild, and rigging (via Blender's own tools or an auto-rigger like Mixamo, since general
image-to-3D output isn't pre-rigged the way DAZ's is) all happen there before Godot import, same as the
DAZ pipeline's own cleanup stage.

---

## Open Questions

- Which specific tool(s) actually get used for the photographic/AI-generated majority — not yet tested
  against this project's actual reference images.
- The DAZ-vs-this-pipeline relationship (see above) — not yet decided.
- Whether multiple reference images per character (most Doll folders have several, though rarely a clean
  front/back/side turnaround) meaningfully improve output quality with the tools eventually chosen — expected
  to help, per general image-to-3D best practice, but not tested against this project's own material yet.
- Rigging route for AI-generated meshes specifically (Blender manual rig vs. Mixamo auto-rig) — not decided.
- Commercial licensing terms for whichever AI generation tool(s) get chosen — same caution as the DAZ
  pipeline's own licensing note, but likely more unsettled/variable for AI-generated output specifically.
