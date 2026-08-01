# Early Access vs. Launch — Content Split

**What this is:** a working answer to a release-strategy question, not a GDD design document — what can feasibly be justified as exclusive to the full "Launch" release, held back from Early Access. Written 2026-07-10.

**The plan this answers:** release Inner Tepenia in Early Access first — partly to raise funds for hiring professional 3D animators, voice actors, and bands/musicians — then later release the actual, complete, proper game (not Early Access). DLCs wait until after that full launch; they are not part of this question at all, since they're already understood to come later.

---

## 1. The three things funding is directly for

These are the cleanest, most easily justified Launch-exclusive items, because they map directly onto what the Early Access money is actually raised to pay for:

- **Voice acting.** Early Access ships text-only, or with a companion or two temp-voiced as a taste of what's coming. Full voice acting for every companion and major NPC arrives at launch.
- **3D animation polish.** Early Access ships with functional but simpler rigging/mocap; launch brings the professional animation pass, especially on companion romance scenes and combat.
- **Original music.** Early Access ships with stock/royalty-free or placeholder tracks; launch brings in the actual bands/composers for the game's various musical textures — Leo's music scene, Naizelle d'Edjordoś's Heavy Metal/Industrial background, Zhongshan's contemplative Chinese classical tradition *(corrected 2026-07-13 — previously "Sino-Russian classical fusion"; Zhongshan is singularly Chinese-founded, not a Sino-Russian fusion — see `Specs/Zhongshan.md`)*, Pink Lucy's Warm Circuit sound, and so on. This is the easiest of the three to market directly to players — "hear the real bands" is a tangible, legible launch feature in its own right, not just an internal production milestone.

---

## 2. Content completeness, not just polish

- **Full companion roster.** Early Access could ship with a genuine subset — the most fully-designed companions at the time of release — while the remaining companions complete during the Early Access development window and land at 1.0. This is the single most common Early Access pattern in the industry (Baldur's Gate 3 shipped Act 1 only during EA; Hades and Slay the Spire both grew their full cast and content during their own EA periods).
- **Post-romance mini-questlines and Significant Object rewards** (see `Worldspace/Design_Principles.md` Section III). Easy to stage: base romance arcs ship in Early Access, the deeper post-romance layer arrives as a launch addition.
- **Full companion home designs.** Interiors could ship simplified during Early Access, fully realized at launch.
- **Endgame/completionist content** — New Game+, achievements, a final full perk-cycle balance pass.
- **"Throw anything" support — confirmed Launch-exclusive, 2026-07-23.** Early Access ships the scoped-down
  thrown-blades-only system (`Game-Mechanics/Combat/Throwing_Weapons.md`); a full Baldur's Gate 3-style
  "any item can be thrown" system is confirmed for Launch specifically, not Early Access. Reasoning: it's a
  genuinely larger-scope system requiring extensive planning and execution in its own right (every throwable
  item needs its own weight/damage/behavior handling, not just blades), not a case of the blade system simply
  needing more polish — closer in kind to the full companion roster/companion homes pattern above (ship the
  scoped version first, the fuller version at launch) than to Category 1's funding-gated items or Category 3's
  stability-gated ones.
- **The Fragmentation Matrix and everything it feeds — confirmed Launch-exclusive, 2026-07-24.** The Bond/
  Grief two-axis system (`Game-Mechanics/Core-Mechanics/Fragmentation_Matrix.md`), and everything that
  inherits from it — the 16-cell grid, The Long Vigil and its companion-questline pathlines, residual
  player-mechanic echoes, "glitchy" re-spec effects, and its own Endings tie-ins — ships at Launch only, not
  Early Access. Same reasoning as "throw anything" above: this is a genuinely large, cross-cutting system
  (touches every companion's relationship tracking, the re-spec mechanic, and a whole Secret-Endings category)
  rather than something that just needs more polish, so it's held back in full rather than shipping a
  scoped-down version. Early Access's own reduced companion roster (see below) makes this a clean cut besides
  — there's little value in a partial Fragmentation Matrix built around only 3-4 companions when the system's
  own depth comes from being tracked across the full roster.

### Resolved 2026-07-10: Romance stays in Early Access, but with a reduced roster

**Decision:** romance questlines are NOT held back for Launch after all. The developer's own reasoning, on reflection: companion romance is one of the biggest draws and word-of-mouth generators in this genre (see Baldur's Gate 3's own Early Access, where romance content was a major part of what got people talking), and it's also one of the project's own two north-star creative questions (see `user_creative_principles` — the nature of love between robots and humans). Hiding it entirely from Early Access would risk hiding the thing most likely to win over the exact audience the funding drive depends on.

**The actual Early Access scope, instead:** a small handful of recruitable companions — roughly 3-4 — get their full romance arcs (including full Gate 1/Gate 2/Gate 3 design, signal lines, and romance beats) included in Early Access, at whatever voice/animation/music polish level the rest of Early Access ships at (per Category 1 above — likely text-only or minimally voiced, simpler animation, placeholder music). The **full companion roster** (all remaining companions, their own romance arcs, and any post-romance mini-questlines) is what's actually held back for Launch — not the *mechanic* of romance itself, just its full breadth.

**Still open:** which 3-4 companions make up that Early Access subset. Worth choosing from among the characters whose romance designs are already most complete in `Game-Mechanics/Core-Mechanics/Companion_System.md` and `Design_Principles.md` (as of 2026-07-10, this includes at minimum Favi della Torre, Villena Hiresvett, Naizelle d'Edjordoś, Seica Cenilaithe, Ji-Eun Kim, Vosora Lashár Tanslock, Michelle Stanton, Fenny, Flora, Pink Lucy, Ayako Hayashi, and Lyuba Baranova — all already have full romance designs written), but the actual selection is a separate decision, not made here.

### Tentative Early Access Companions — shortlist, established 2026-07-10, revised same day against the new beat structure

Cross-referenced the full base-game roster against the *revised* main quest beat structure (`Storyline/Main-Story/Main_Quest_Revised_Beat_Structure_TENTATIVE.md`), which routes the player through every district except Leo (explicitly optional) before the climax. Companions whose home district sits on that critical path, and whose own design doesn't flag them as deliberately hard to find, are the players most likely to organically meet a companion candidate during a first playthrough:

- **IT-068 "Flora"** — Capricorn (Beat 1). **DEFERRED to Launch.** See the Flora/Michelle substitution note below.
- **Favi della Torre** — Taurus (Beat 2). **CONFIRMED for Early Access, 2026-07-10** — distinctively Type 6 (sniper/field-operative archetype), not a personality-overlap risk with any other confirmed EA companion.
- **Seica Cenilaithe** — Scorpio (Beat 3). **DEFERRED to Launch, 2026-07-10.** See the Type-8 slot resolution below.
- **Vosora Lashár Tanslock** — Gemini (Beat 4). **DEFERRED to Launch.** See the Vosora substitution note below.
- **Michelle Stanton** — Gemini (Beat 4). **CONFIRMED for Early Access, 2026-07-10**, replacing Flora as the first confirmed slot — see below.
- **Lyuba Baranova** — Aries (Beat 8, the Power Core — the main quest's own plot epicenter). **CONFIRMED for Early Access, 2026-07-10**, filling the Type-8 slot — see below.

**Flora deferred to Launch; Michelle confirmed in her place, 2026-07-10.** Flora and Michelle Stanton read as near-identical in personality type and job (both craft/repair-coded, both landing in similar thinking-competency territory) — see `Flora/Michelle Overlap` note in `TODO.md`. Rather than designing a new companion to create variety, the developer chose to simply not have both in Early Access at once. Flora's own recruitment is structurally tied to the opening Thermal Distribution Junction 12 diagnostic (Calethina's likely opening task, "The Heating Grid Failure") — in Early Access, the repair crew the player finds there is led by a **non-recruitable human NPC** instead of Flora; Flora's own version of that scene, and her recruitment, become Launch content. Michelle takes over as the confirmed Early Access companion instead: she's already the single most guaranteed-to-meet character in the base roster (per the revised beat structure's Beat 4 design — she's structurally necessary to diagnose the grid crisis's data-corruption layer, not just incidentally nearby), so her presence in Early Access costs nothing in critical-path exposure while resolving the overlap.

**Vosora Lashár Tanslock deferred to Launch, revised 2026-07-10.** Vosora is co-located with Michelle in Gemini/Beat 4 and runs the recovery-side half of the same Great Corruption investigation Michelle runs from the slow-verification side. Rather than having both Gemini companions present in Early Access, Vosora's own recruitment and questline become Launch content. **Substitution for Early Access:** a discoverable data-stash of Vosora's own investigation notes, placed somewhere in Gemini the player is likely to find, continuing the Great Corruption breadcrumb trail toward wherever it leads without Vosora herself appearing as a live NPC. This mirrors the Flora/Junction-12 substitution above — a findable trace of the character's own thread stands in for the character, in Early Access only.

**Lyuba Baranova confirmed for the final Early Access slot; Seica Cenilaithe deferred to Launch, 2026-07-10.** Both are 8w7 Sexual, so this was a single "Type 8" slot rather than a personality-variety question between the two of them directly. The deciding factor: TCY-25 "Rui" (9w1 Self-Pres) — newly confirmed recruitable the same day — also lives in Scorpio, the same district as Seica. Deferring Seica to Launch alongside Rui keeps Scorpio's own companion representation as a Launch-era two-doll pairing (8w7 and 9w1, genuine personality variety within the same district) rather than splitting it awkwardly across Early Access and Launch. Lyuba, in Aries, has no such district overlap with any other confirmed or pending companion, making her the cleaner Early Access pick for overall roster distribution across districts.

Three further companions (Ji-Eun Kim, Naizelle d'Edjordoś, Fenny) live in districts also on the critical path but are deliberately designed to require more than passive presence to actually meet (Ji-Eun is explicitly in hiding; Naizelle is the most reclusive companion in the roster; Fenny has no signal line and "doesn't warm up") — worth keeping in view as a second-tier option if the shortlist needs to expand. Villena Hiresvett, "Pink Lucy," and Ayako Hayashi (all Leo) are excluded from this shortlist specifically because Leo sits outside the main quest's own critical path entirely, per the story's own design notes — nothing here rules them out for Early Access on other grounds, it only reflects that they wouldn't be met "very very very likely" through the main quest alone.

**Caveat:** this shortlist is only as reliable as the beat structure it's drawn from, which the developer has already flagged as sparse/not finalized — recheck against whichever districts end up load-bearing if Act 2's branching order changes.

---

## 3. Things that are genuinely hard to do well before the game is finished

- **Full localization** (see `Dev-Road-Map/Localization_Language_List.md`'s own Tier 1 list — Chinese, Spanish, Russian, German, Japanese, Portuguese, French, with Korean as a strong thematic case). Translating a game that's still actively changing wastes translator budget on content that will be rewritten; this is standard industry practice as a launch-only item, not a corner being cut.
- **Final balance pass** across leveling, perks, MACHINE stats, and combat difficulty — generally wants the full content set in players' hands before the numbers get locked down.
- **Accessibility features** (subtitle timing, colorblind modes, control remapping) — usually a late-stage polish pass once the UI itself has stabilized.
- **Mod support — confirmed Launch-exclusive, developer decision 2026-08-01.** Same underlying logic as localization above: a mod API/toolset needs to be built against a stable interface, and Early Access content (systems, data structures, companion rosters, the still-evolving Fragmentation Matrix and similar cross-cutting mechanics) keeps changing under active development. Shipping modding support during Early Access risks breaking mods with every content update, or freezing internal systems prematurely just to keep modders' work stable — neither is a good trade. Full Launch is the natural point to open this up, once the underlying systems it hooks into have actually settled.

---

## 4. Marketing-legible "this is the real release" signals

Steam achievements and trading cards, a proper finalized opening cinematic, finished box art/key art — all cheap to justify, and useful for the "this is now a finished product" messaging that separates a full launch from Early Access in players' own minds, distinct from the underlying content questions above.

**Photo Mode — confirmed Launch-exclusive, developer decision 2026-07-17.** Fits this category cleanly: it's only genuinely worth having once character models, animations, and environments are past the "functional but simpler" Early Access baseline described under Category 1 — a photo mode built around Early Access-tier art assets would be showcasing exactly the polish level the game is still raising funds to improve. It's also a natural companion to the other items in this category (finalized key art, a polished opening cinematic) as a "this is the real release" signal in its own right.

---

## 5. Demo vs. Early Access — these are two different things, chained together

Added 2026-07-23, in response to a direct question about how a free Demo would actually differ from the paid
Early Access plan already laid out above.

- **Price.** Demo is free, always. Early Access is paid — the actual revenue mechanism funding the three
  items in Category 1 (voice acting, animation, music).
- **Scope and lifespan.** A Demo is a **fixed, curated slice** — a short vertical slice (most likely the
  opening sequence, e.g. the Thermal Distribution Junction 12 diagnostic beat) frozen at a specific polish
  level, that doesn't grow or change based on feedback. Early Access is a **genuine, evolving subset of the
  real game** — the actual companion roster, romance arcs, and content described in Categories 1-3 above,
  expected to expand over months as development continues toward 1.0.
- **Saves/progress.** Demo saves generally do **not** carry into the full game (Steam treats it as a separate
  depot tied to the main store page). Early Access saves **do** carry forward into Launch — same app, same
  depot, just an earlier point in its life.
- **Feedback loop.** Early Access explicitly invites player feedback as a real development input. A Demo's
  purpose is conversion, not iteration — it isn't rebuilt in response to what players say about it.
- **Purpose.** The Demo's job is building wishlist velocity (see `Steam_Launch_Strategy_and_AI_Disclosure.md`
  Section 2) and getting into Steam Next Fest. Early Access's job is converting that wishlist momentum into
  actual sales that fund the rest of production.

**How this chains together for Inner Tepenia specifically:** the Demo comes *first*, chronologically — a
small, free taste with no companion romance necessarily included, timed around a Steam Next Fest. Early
Access follows, as the actual paid product described throughout this file.

**Still open:** what exactly the Demo's vertical slice contains, and its own timing relative to the Early
Access launch — not decided yet, just distinguished from Early Access here.

---

## Recommendation

Lead marketing and backer messaging with Category 1 specifically (voice, animation, music) — it's the most emotionally legible pitch to an Early Access audience, since it maps directly onto what their money is actually funding. Categories 2 and 3 are normal, well-precedented industry practice and won't read as a bait-and-switch to players, but they're secondary to the direct funding story Category 1 tells on its own.

**Updated 2026-07-10:** this recommendation still holds, with one refinement — don't let the Category 1 polish-deferral logic accidentally justify deferring romance content itself. Romance arcs for a small (3-4) companion subset should ship in Early Access at whatever polish level the rest of the game ships at; only the *remaining* companions and their romance content are deferred to Launch. See the resolved note under Category 2, above.
