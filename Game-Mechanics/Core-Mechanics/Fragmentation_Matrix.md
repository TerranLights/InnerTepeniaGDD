# Fragmentation Matrix

**Release scope, confirmed 2026-07-24:** this entire system — the Bond/Grief axes, the 16-cell grid, The
Long Vigil and its companion-questline pathlines, residual player-mechanic echoes, "glitchy" re-spec effects,
and its Endings tie-ins — is **Launch-exclusive, not part of Early Access.** See
`Dev-Road-Map/Early_Access_vs_Launch_Content_Split.md` Category 2 for the reasoning.

**Source:** structurally parallel to `Reputation_System.md`'s two-axis Fame/Infamy model, developed
2026-07-23 at the developer's explicit request — a system for tracking how individual companions (and
companion-adjacent characters — Calethina tracks Bond/Grief despite occupying no companion slot, see
below) and whole districts/factions react to the player's Identity Fragmentation history (see
`Player_Re-Spec_-_Complete_Design.md`), independent of the player's own single global IF meter
(`Storyline/Endings/Secret-Endings/Identity_Fragmentation_Endings.md`). Where the IF meter measures the
player's own instability, the Fragmentation Matrix measures what *other people* carry about it — and,
critically, it is **not a single scale**, for exactly the same reason Fame/Infamy isn't.

**Where this differs from the Reputation Matrix:** Fame/Infamy is a moral-favorability read (good deeds vs.
bad). The Fragmentation Matrix isn't — neither axis is "good" or "bad" to hold. It measures something closer
to attachment and memory than to approval.

---

## The Two-Axis Model

- **Bond** — Range 0 through Range 3. How much this companion or district has embraced the player's
  *current* configuration. Accrues through continued interaction, consistency, and positive beats since the
  last re-spec.
- **Grief** — Range 0 through Range 3. How much unresolved feeling remains over a *specific earlier*
  configuration this entity actually knew. Seeded at the moment of a re-spec and **does not shrink just
  because Bond grows** — embracing who you are now doesn't require finishing grieving who you were.

The tier an entity actually holds is the *combination* of both axes, exactly like Fame/Infamy — not an
average, not a single blended number. An entity can be simultaneously maxed on both at once (**The Long
Vigil**, bottom-right cell) — a real, distinct, permanent state, not a contradiction the system resolves.

**A clean structural property this produces for free:** a companion recruited *after* the player's last
re-spec never knew the earlier self, so their Grief axis is structurally locked at 0 — they can only ever
occupy the top row of the grid. Nothing needs to be written to enforce this; it falls straight out of the
axis definition.

---

## Seeding Grief: The Formula

**Grief seeded at a re-spec = Relationship-Depth Markers × Personality Grief-Multiplier**

Reuses existing or already-planned systems rather than inventing new tracking:

### Relationship-Depth Markers (Companions)

- **History Points** accumulated with that companion (the FNV-style invisible-accumulation mechanic flagged
  in `TODO.md`, not yet designed in general but a ready-made input here).
- Companion-questline stage completed.
- Romance-questline stage completed, if romance was started.
- Current approval/trust level, if tracked.

**Special-case marker — Direct Participation Count, Calethina only (2026-07-23).** Confirmed: Calethina
tracks Bond/Grief despite occupying no companion slot and being explicitly excluded from companion-system
code (`Companion_System.md`'s "Calethina: Not a Companion" section) — companion-object status is not a
prerequisite for this matrix. Her Grief seeds differently than an ordinary companion's: rather than
(or alongside) relationship-depth markers built from external interaction, she has a marker no other
character has — **the number of re-specs she has personally performed on the player at Calethina's Lab.**
She isn't just present for the loss of a previous self the way a companion is; she is the one who *performed
the procedure that caused it*, every time. This is a direct, first-hand, repeated participation in the act
itself, not a relationship built around observing its aftermath — already textually established in
`Player_Re-Spec_-_Complete_Design.md`'s "Calethina's arc through repeated re-speccing" (professional on the
first visit → she asks why on the second → grief by the third+ → something that only fully resolves in
relation to the Devotion ending). That existing prose arc is, in effect, an unformalized description of her
own climb up the Grief axis — this system just gives it mechanical teeth.

### Relationship-Depth Markers (Districts/Factions)

- The district's own **Fame/Infamy history** (`Reputation_System.md`) *as it stood at the moment of the
  re-spec* — a district that held the player at Idolized before a re-spec that abandoned whatever earned
  that status has a much larger relationship-depth marker than a district that barely knew the player.
  Reuses the existing two-track reputation system as the input rather than building a parallel tracker.

### Personality Grief-Multiplier

A per-character (or per-district) constant. **Critically, this is not a measure of how emotionally intense
a character is in general — it's a measure of how that specific psychology interprets the loss of a
previous self**, which can diverge sharply from general emotional intensity. Derived from material already
written for every companion (Enneagram profile, established worldview, backstory) rather than a new
freeform stat picked in isolation.

**Calibration examples, worked against three existing companions (2026-07-23):**

- **Ayako Hayashi — high multiplier.** SP4w5, explicitly "processes grief by turning it into action rather
  than expression," and her whole arc is built around one wound: being present and unable to save someone
  she loved. A companion she's bonded with disappearing into a re-spec recreates the exact shape of that
  wound — watching someone become unreachable while she's helpless to stop it. This isn't "she's an
  emotional character" — it's that this specific mechanic reactivates her defining trauma.
- **Seica Cenilaithe — low multiplier, despite being a genuinely high-grief character overall.** She carries
  permanent, unresolved grief for her husband, and "Grief Recognition" is a named trait precisely because
  she recognizes it so intimately in others. What lowers her multiplier *for this specific mechanic* is her
  Goth community's philosophy: "transformation should be sacred rather than clinical; death should be
  honored rather than therapized." Her grief is over a violent, involuntary loss inflicted on her. A
  player's re-spec is a chosen transformation, which her tradition's own lens reframes as something to
  witness and honor, not mourn. Same person, opposite read, because the multiplier tracks interpretation of
  loss, not raw emotional intensity.
- **Kendra Heinrich — low multiplier, for a third, distinct reason.** An assertive, instinctive 8w7 whose
  psychology is built around present demonstrated capability and earned respect ("Respect is the
  precondition for everything with a Type 8"), not backward-looking attachment. She doesn't orient toward
  who you used to be — she evaluates who you are now. Her established "Absolute Loyalty" trait (near-
  unconditional once earned) suggests a *high* Bond-accrual rate once triggered — proof the two axes are
  genuinely independent: a low Grief-multiplier doesn't cap Bond. Her one hard trigger (turning hostile if
  the player harms innocents) is a separate absolute trait-lock outside this matrix entirely, not something
  Bond/Grief needs to model.

- **Calethina — the highest multiplier in the game, and the clearest case of all.** She isn't a bystander to
  the player's fragmentation, she's frequently its direct cause, and she watches it happen with full
  understanding of what each change costs, every single time. Her own arc already escalates exactly the way
  a maxed multiplier would predict — professional distance, then asking why, then open concern, then grief,
  then something at Critical IF that's only fully legible next to the Devotion ending's own emotional core.
  Combined with the Direct Participation Count marker above, she's positioned to reach The Long Vigil (or its
  outer edge) faster and more inevitably than any ordinary companion — which fits a character whose entire
  narrative function is watching someone she helped build become, repeatedly, someone else.

**Four characters, four different reasons for where the multiplier lands, no forced pattern** — a good sign
the mechanic reads character rather than applying a flat rule.

### District Grief-Multiplier — cross-checked against existing per-district reactions

The "Rebuilt Marker" reaction lines already written per district in `Player_Re-Spec_-_Complete_Design.md`
map onto this grid without needing new material invented:

- **Taurus, Cancer** — "Loss... isn't that person" — the only two that read as genuinely **high-Grief**.
  Consistent with the existing IF-Unstable-state text calling these the districts that "value continuity."
- **Aries, Scorpio** — respect/initiation framing — **high-Bond, low-Grief**. They care about the outcome,
  not the person left behind.
- **Aquarius, Gemini, Leo** — curiosity/data/aesthetics — **low-Grief**, Bond driven by novelty rather than
  intimacy.
- **Sagittarius, Capricorn, Pisces** — pragmatism/efficiency/calling-card — purely **utility-driven Bond**,
  near-zero Grief.
- **Virgo** — "how controlled were yours" — mild Grief (concern for lost stability), low Bond until proven
  otherwise.
- **Libra, Hub** — "which version of you agreed to which commitments," "aligned with now" — doesn't cleanly
  fit either axis. Modeled as a **suppressor on Bond** (an entity that can't trust the player's consistency
  won't fully bond with the current configuration) rather than a third axis — keeps the system a true
  two-axis parallel to Fame/Infamy instead of scope-creeping past it.

11 of 13 districts fall out cleanly from material that already existed; Libra/Hub is the one real edge
case, resolved without breaking the two-axis rule.

---

## The Full Grid

**No color-coding legend, unlike the Reputation Matrix.** Fame/Infamy's 🟢/🔴/⚪ legend is a moral-
favorability read that doesn't apply here — Grief isn't a bad thing to have accumulated, it's simply a true
thing. The names carry the read instead.

| Grief ↓ / Bond → | **Range 0** | **Range 1** | **Range 2** | **Range 3** |
|---|---|---|---|---|
| **Range 0** | **Blank Slate** — doesn't know you well enough, in any version, to have formed real feelings either way. | **Familiar** — at ease with who you are now; never knew a version worth missing. | **Trusted** — real trust built with exactly one version of you: this one. | **Devoted** — wholly given to who you are today, uncomplicated by who you used to be. |
| **Range 1** | **Distant** — something about who you were lingers as a small ache; the current you hasn't closed the gap. | **Uncertain** — a little fondness for now, a little unresolved feeling about before; hasn't settled. | **Reconciled** — has made real peace with the change; still thinks of the earlier version sometimes, without it souring this one. | **Faithful Despite** — completely given to who you are now, and still, quietly, sometimes misses who you were. |
| **Range 2** | **Estranged** — the loss weighs heavier than any relationship with who's here now; increasingly feels like company with a stranger. | **Torn** — real mourning for a self that's gone, real if tentative connection to the one that replaced it. | **Steadfast Mourner** — holds both fully: real closeness with now, real grief for before, neither one cancelling the other. | **Unwavering** — devoted entirely to the person in front of them, and still carrying real, unresolved grief for the one who isn't. |
| **Range 3** | **Haunted** — cannot separate you from who you used to be; every interaction with now is filtered through what was lost. | **Grieving Stranger** — a small, fragile connection to now, overwhelmed by a much larger unresolved grief for before. | **Holding On** — real trust in who you are now is the only thing keeping the grief for who you were from becoming something worse. | **The Long Vigil** — total devotion to the current you, total unresolved grief for who's gone — carried simultaneously, permanently, without contradiction. |

16 total named combinations. Row = Grief tier, column = Bond tier; read the cell where they intersect.

---

## The Long Vigil (Grief Range 3 + Bond Range 3)

This is the Fragmentation Matrix's own Wild Child: not just a flavor name, a deliberately load-bearing
extreme state, dual-purpose depending on who holds it:

- **A companion at The Long Vigil** unlocks a **Long-Vigil-only personal-questline pathline** — content
  reachable no other way, because it requires a companion who both fully embraced who the player is now
  *and* never stopped grieving who they left. See individual companion README files for candidates (Ayako
  Hayashi flagged first, 2026-07-23, given how directly this state maps onto her own established wound).
  See `Companion_System.md`'s Personal Questline Design Rule for the recommended-pattern writeup.
- **A district at The Long Vigil** contributes toward the citywide **Long Vigil Endings** tier count — see
  `Storyline/Endings/Secret-Endings/Long_Vigil_Endings.md`, structured identically to `Wild_Child_Endings.md`
  (tiered by how many districts simultaneously hold the state).

---

## Implementation Notes

- **Per-cell dialogue is required, not optional** — same standing law already governing the Rebuilt Marker
  and romance-variant dialogue ("no generic reaction," `Player_Re-Spec_-_Complete_Design.md`). Every
  companion needs a written response for whichever of the 16 cells they can actually reach. Not all 16 are
  reachable by every companion — one recruited after the player's last re-spec can only ever occupy the top
  row (Grief locked at 0).
- **Districts carry four numbers, not two** — Bond/Grief layers on top of the existing Fame/Infamy tracking,
  it doesn't replace it.
- **Mechanical thresholds** (exact point values, decay/growth rates for Bond, whether Grief can ever be
  partially soothed short of a full "Reconciled"-style narrative beat) are not yet designed — this file
  formalizes the structure and the seeding formula, not the moment-to-moment numbers.
- **Not every companion or district needs bespoke Personality/Institutional Grief-Multiplier values before
  the system can ship** — start with companions whose personal questlines are furthest along (Ayako, Seica,
  Kendra already calibrated above) and extend gradually, the same incremental approach used for the district
  re-spec methods' own TBD numeric gaps.

## Open Design Questions

- Exact numeric thresholds for Range 0-3 on both axes.
- Whether Grief can ever be narratively resolved down a tier (a "Reconciled"-triggering scene, for instance)
  or whether it is genuinely permanent once seeded, mirroring the IF meter's own "cannot be reduced" rule.
- Full Personality/Institutional Grief-Multiplier values for the remaining companions and the 11 districts
  not yet explicitly calibrated above.
- Whether Bond can decay from neglect, or only grows — not yet decided.
- **Flagged 2026-07-23, deliberately deferred, not urgent:** a dedicated design pass for "Long Vigil companion
  ending perks" generally — once more companions have their own Long-Vigil-only pathlines (Ayako's "The
  Second Garment" is the first, see her `Questlines/Personal_Questline_Summary.md`), go through and formally
  design each one's actual mechanical perk rather than leaving them as narrative sketches. Not something to
  start now — flagged for whenever the broader companion Long Vigil pathline set exists to draw a real
  pattern from.
