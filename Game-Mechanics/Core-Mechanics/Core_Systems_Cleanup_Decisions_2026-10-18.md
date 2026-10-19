# Core Systems quick cleanup — decisions log

**Started 2026-10-18.** Developer rulings from going through the core-systems cleanup items one at a time. **All seven items were decided and the edits were applied on 2026-10-18** (AP base file, AP perks file, quest tracking file, and the three Neural Overclock documents for the Hyperthread rename).

## 1 · How Engine reduces movement cost — decided 2026-10-18

- **Agility sets the base** number of tiles per turn through the AP pool (1 AP per tile), as in Fallout 1 and 2 (recollection: 1 AP per hex, AP from Agility). **Engine adds to it, it does not replace it.**
- **Engine's own effect: free movement tiles** = floor((Engine − 5) ÷ 2) per turn (0 at Engine 5–6, 1 at 7–8, 2 at 9–10). **Kept as is.** The "Engine 8 = 2–3 free tiles" example in the AP file is wrong against the formula and must be corrected.
- **The "1 AP per 1.5 tiles" mechanic is dropped** (it would cause awkward math later). The perk that carried it (currently "Efficient Exosuit"; **the developer plans to rename it**) is replaced by a different perk:
  - **Multi-rank movement perk, based on Nerve** (not Engine), so builds are not tied entirely to Agility and Engine.
  - **Each rank adds movement tiles: +1 tile, or +10% of the character's total movement tiles, whichever is higher.** (For typical pools of 8 to 13 tiles this is a flat +1 per rank; the percentage matters only for larger pools, such as during Framejacking.)
  - **Movement only** (not general AP, cannot be spent on attacks).
  - **Ranks live inside the one perk, as in Fallout** (especially New Vegas): there is one minimum requirement for the perk; **no higher stat is needed for later ranks**; the player may take multiple ranks. Number of ranks and the Nerve minimum to be set when the perk is written (suggested 3 ranks, Nerve 6+).
- **Rounding** is no longer an issue (the whole-number tile bonus removes it).

## 2 · Nerve modifier at Nerve 10 — decided 2026-10-18
**Option A: keep the formula floor((Nerve − 5) ÷ 2) as written.** Values: Nerve 1–2 = −2, 3–4 = −1, 5–6 = 0, 7–8 = +1, 9–10 = +2. The "+2 or +3" wording in the AP file is corrected to +2.

## 3 · "Machine 7+" and the AP perk list — decided 2026-10-18
- The AP perks file's perk list had drifted from the authoritative list (`Perks/Regular_Perks_-_Level-Up.md`). **The authoritative list is the single source of truth.**
- The four overlapping perks (Grim Reaper Protocols, Rapid Fire Protocols, Precision Strike, Undergrid Runner) become short pointers to the authoritative entries. Grim Reaper therefore reads Might 6 and Agility 6, refunding 3 AP.
- The eight AP-file-only perks (Action Protocols, High-Output Protocols, Efficient Exosuit, Siligel Optimization, Overclock Surge, Field Expedient Reload, Quick Pockets, Emergency Systems) stay in the AP file but are marked **"proposed, not yet in the perk list"**, each needing proper requirements (stat plus skill) in the perk list's format before being added. The new Nerve movement perk is added to the same proposed list.
- **Developer note:** several perks, traits and skills (including the skill named "Tactical Grid Combat") will be renamed and possibly replaced later.

## 4 · Duplicate list numbering in the AP perks file — decided 2026-10-18
Renumber the "Future Perk / Trait Options" list 1 to 7 in order (AP-to-Movement Conversion, Carry-Over AP, Fatigue / Overheat, Free Actions, Overclock / Emergency Mode, Movement as a Separate Resource, Momentum System). Nothing elsewhere refers to the old numbers. **Left open:** entry 6 (a separate Movement Points pool) conflicts with the single Agility-based AP pool chosen in item 1; the developer approved the renumbering only, so entry 6 is **not** marked "not adopted". **Developer, 2026-10-18: "we'll tackle the separate movement pool later."**

## 5 · Quest tracking: how an interruption is handled — decided 2026-10-18
**Option 1, the split.** The **tracked quest** (a specific quest, or deliberately nothing) changes **only by the player's own action.** A separate, temporary **objective prompt** handles time-sensitive events and never touches the tracked quest. **Any new quest that comes up is added to the quest log but remains untracked.** The return-stack approach stays on file only as a fallback if the prompt proves too cramped. *(Developer: "that's definitely the fix.")*

## 6 · Quest tracking: default state — decided 2026-10-18
- **The opening quest** (leaving Calethina's lab; Calethina asks the player to fetch something, tentatively a data drive, which may change once the questline is worked out): **whether it is tracked is decided by the player's dialogue choice with Calethina**, as in Fallout: New Vegas when Doc Mitchell sends the player to Sunny Smiles, except that New Vegas gives no choice and Inner Tepenia does. **If the player agrees to fetch the drive, the quest is tracked; if the player says "maybe, if there's time," it is not.** The tracked quest still changes only by the player's own action; a dialogue answer is such an action.
- **(a) Applies to every quest offered in dialogue, everywhere:** agreeing tracks it; a non-committal answer adds it to the log untracked; quests that start without dialogue (a phone call, entering a region) always arrive untracked.
- **(b) Default when nothing is tracked: Option B.** The tracker stays empty, and the quest log shows a small marker on the most recently updated quest. It suggests, it never selects.

## 7 · The name "Overclock" — decided 2026-10-18 (developer took the recommendations)
- **The third mode of the cyberware system (the Calculation mode) is renamed.** The system keeps the name "Neural Overclock." The mode's new name: **Hyperthread** (recommended; the developer accepted the recommendation, so it can still be changed). Other candidates considered: Overdrive, Throughput, Cascade.
- **The perk and trait names** that use "Overclock" (Overclock Surge, Overclocked Prototype, Engine Overclocker, Overclocked Aggression) are **left for the developer's planned perk/trait rename pass**; a one-line note in the AP file says they are unrelated to the cyberware implant. The Aries district's "overclock / burnout" culture is a separate, legitimate usage and stays.
- **Added to the later list:** the same system is written up in three places that disagree (`Core-Mechanics/Neural_Overclock.md`, `Character-Creation/Cyberpunk-2077-Style_Functionalities_Summary.md`, `Combat/Signature_Abilities.md`): durations 1–3 versus 3–5 turns, and the 8-point stat gate appears in only one. They need consolidating into one document.

## All seven items decided and applied 2026-10-18.
