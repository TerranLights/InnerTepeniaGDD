# Early Access vs. Launch — Content Split

**What this is:** a working answer to a release-strategy question, not a GDD design document — what can feasibly be justified as exclusive to the full "Launch" release, held back from Early Access. Written 2026-07-10.

**The plan this answers:** release Inner Tepenia in Early Access first — partly to raise funds for hiring professional 3D animators, voice actors, and bands/musicians — then later release the actual, complete, proper game (not Early Access). DLCs wait until after that full launch; they are not part of this question at all, since they're already understood to come later.

---

## 1. The three things funding is directly for

These are the cleanest, most easily justified Launch-exclusive items, because they map directly onto what the Early Access money is actually raised to pay for:

- **Voice acting.** Early Access ships text-only, or with a companion or two temp-voiced as a taste of what's coming. Full voice acting for every companion and major NPC arrives at launch.
- **3D animation polish.** Early Access ships with functional but simpler rigging/mocap; launch brings the professional animation pass, especially on companion romance scenes and combat.
- **Original music.** Early Access ships with stock/royalty-free or placeholder tracks; launch brings in the actual bands/composers for the game's various musical textures — Leo's music scene, Naizelle d'Edjordoś's Heavy Metal/Industrial background, Zhongshan's Sino-Russian classical fusion, Pink Lucy's Warm Circuit sound, and so on. This is the easiest of the three to market directly to players — "hear the real bands" is a tangible, legible launch feature in its own right, not just an internal production milestone.

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

### Tentative Early Access Companions — shortlist, not a decision, established 2026-07-10

Cross-referenced the full base-game roster against the main quest's own current beat structure (`Storyline/Main-Story/Main_Story-Hook_Progression.md`), which is explicit that the story routes the player through nearly every district before the climax, with Leo called out by name as "entirely optional/side content" and Libra never given its own beat at all. Companions whose home district sits on that critical path, and whose own design doesn't flag them as deliberately hard to find, are the players most likely to organically meet a companion candidate during a first playthrough — which makes them the natural shortlist to draw the eventual 3-4 Early Access companions from:

- **IT-068 "Flora"** — Capricorn (Beat 2; her own file frames her as an early guide to that district)
- **Favi della Torre** — Taurus (Beat 1, the actual starting district)
- **Seica Cenilaithe** — Scorpio (Beat 4)
- **Vosora Lashár Tanslock** — Gemini (Beat 5)
- **Michelle Stanton** — Gemini (Beat 5); also independently the trigger NPC for DLC 1, likely the single most guaranteed-to-meet character in the base roster
- **Lyuba Baranova** — Aries (Beat 9, the Power Core — the main quest's own plot epicenter)

**This is a shortlist of possible options, not a decision.** No selection among these 6 has been made. Three companions (Ji-Eun Kim, Naizelle d'Edjordoś, Fenny) live in districts also on the critical path but are deliberately designed to require more than passive presence to actually meet (Ji-Eun is explicitly in hiding; Naizelle is the most reclusive companion in the roster; Fenny has no signal line and "doesn't warm up") — worth keeping in view as a second-tier option if the shortlist above needs to expand. Villena Hiresvett, "Pink Lucy," and Ayako Hayashi (all Leo) are excluded from this shortlist specifically because Leo sits outside the main quest's own critical path entirely, per the story's own design notes — nothing here rules them out for Early Access on other grounds (e.g., deliberately drawing attention to optional content), it only reflects that they wouldn't be met "very very very likely" through the main quest alone.

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
