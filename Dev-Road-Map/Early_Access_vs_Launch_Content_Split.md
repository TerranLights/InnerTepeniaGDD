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

---

## 4. Marketing-legible "this is the real release" signals

Steam achievements and trading cards, a proper finalized opening cinematic, finished box art/key art — all cheap to justify, and useful for the "this is now a finished product" messaging that separates a full launch from Early Access in players' own minds, distinct from the underlying content questions above.

---

## Recommendation

Lead marketing and backer messaging with Category 1 specifically (voice, animation, music) — it's the most emotionally legible pitch to an Early Access audience, since it maps directly onto what their money is actually funding. Categories 2 and 3 are normal, well-precedented industry practice and won't read as a bait-and-switch to players, but they're secondary to the direct funding story Category 1 tells on its own.

**Updated 2026-07-10:** this recommendation still holds, with one refinement — don't let the Category 1 polish-deferral logic accidentally justify deferring romance content itself. Romance arcs for a small (3-4) companion subset should ship in Early Access at whatever polish level the rest of the game ships at; only the *remaining* companions and their romance content are deferred to Launch. See the resolved note under Category 2, above.
