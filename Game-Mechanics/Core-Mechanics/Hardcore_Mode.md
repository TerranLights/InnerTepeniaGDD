# Hardcore Mode — Inner Tepenia

*This document is partially complete. Core mechanic structure and South Pole DLC interactions are confirmed. Full Hardcore mode design requires further development — flagged for a dedicated design session.*

---

## Design Philosophy

> # ⭐⭐⭐ THE GOVERNING STANDARD — **developer ruling, 2026-09-04**
>
> > ***"I don't want to make it so that, 'oh, well, now you need to worry about eating and drinking and
> > sleeping and shit'. No. I want Hardcore Mode to fundamentally CHANGE THE WAY THAT YOU PLAY THE GAME."***
>
> **The test every Hardcore system must pass, stated as one question:**
>
> ## ⛔ Does it change HOW THE PLAYER PLAYS — or does it just add another meter to watch?
>
> **A system that makes the player *manage more* is a chore. A system that makes the player *decide
> differently* is Hardcore.** ⭐ **The reference case is the siligel class split** *(below)*: **it does not add
> a number, it changes what a resource IS** — one stack becomes several things that look alike, do different
> jobs, and cannot cover for each other.
>
> ⚠ **This ruling OVERRIDES the paragraphs below where they conflict, and it applies retroactively to every
> system already on this page.** *See the audit immediately following.*

**Standard mode makes Inner Tepenia dangerous. Hardcore mode makes it consuming.**

In standard mode, consequences are immediate and direct: damage, resource cost, death. The world fights the player.

In Hardcore mode, consequences compound over time through degradation systems. The world doesn't just fight the player — it wears them down. Systems that are fine in isolation become lethal in combination. The South Pole is where this distinction is sharpest: what Kendra could not survive alone is survivable with preparation and support — but Hardcore mode narrows that margin significantly.

---

## Standard vs. Hardcore — The Core Distinction

| System | Standard Mode | Hardcore Mode |
|---|---|---|
| Thermal exposure | Direct HP damage in cold areas | HP damage + component degradation over time |
| Coldshock | Reduces Siligel efficiency; reversed by shelter | Same, plus additional system failures at stages 3–5 |
| Structural collapse | Damage on direct hit | Near-misses also risk component damage |
| Magnetic anomalies | Navigation/targeting/HUD disruption | + Prolonged exposure corrupts memory integrity |
| Blizzard events | Visibility reduction | + Environmental seal stress; extended exposure causes system errors without shelter |
| Ammo | Weightless | Has weight (affects carry capacity decisions) |
| Companions | Can be downed and revived | Can permanently die |
| Siligel — delivery | Instant benefit | Gradual processing (benefit delivered over time, not instantly) |
| ⭐ **Siligel — classes** *(added 2026-09-04)* | **ONE type. It does every job** | **MULTIPLE types, each with a finite, dedicated function — and *none substitutes for another*** |
| ⭐ **Siligel — weight** *(added 2026-09-04)* | **Weightless** | **Has weight** — *very slight, very low per dose, but nonzero* |

---

## ⚠ AUDIT — **every system in the table above, against the governing standard, 2026-09-04**

***Run honestly. Several systems on this page do not currently pass.***

| System | Verdict | Why |
|---|---|---|
| **Companion permanent death** | ⭐⭐ **PASSES HARDEST** | **Changes who you bring, whether you take the risky opening, whether you fight at all.** *Nothing to watch — it changes every combat decision* |
| ⭐ **Siligel classes + weight** | ⭐⭐ **PASSES — the reference case** | **Changes what a resource is.** *Non-substitutability means you can be well-supplied and still unable to fix what is wrong* |
| **Siligel gradual delivery** | ⭐ **PASSES** | **Kills mid-combat chugging.** *Healing moves from "during the fight" to "before it and after it" — a different way of approaching every encounter* |
| **Ammo weight** | ⭐ **PASSES** | *Proven in New Vegas: it changes which weapons you actually carry, not merely how much you carry* |
| **Structural collapse — near-misses** | ⭐ **PASSES** | **You can no longer tank the environment.** *Hazards must be genuinely avoided, which changes movement and positioning* |
| **Magnetic anomalies — memory integrity** | ⭐ **PASSES** | ***It degrades CHECKS*** *(Calculation, Investigation, dialogue options) — so it attacks non-combat solutions specifically. **The build you rely on stops working**, which is a play change, not a meter* |
| ⚠ **Thermal exposure — component degradation** | ⚠ **WEAK — needs rework** | *"Same damage, plus a slow number." **Adds a meter.*** ⭐ **Fix available:** `Robot_Cold_Physiology.md` establishes ***a robot is safer MOVING than RESTING*** in cold. **That inverts the standard RPG instinct to hole up and recover — a genuine play change already sitting on file, unused here** |
| ⚠ **Coldshock stages 3–5** | ⚠ **WEAK — needs rework** | *More penalties on an axis that already has penalties. **Escalation is not transformation.*** **Fix direction:** tie it to *which siligel class* it impairs, so it changes what the player must carry rather than how fast a bar fills |
| ⚠ **Blizzard — seal stress** | ⚠ **WEAK** | *Visibility loss plus errors. **Consider instead making blizzards change what routes exist**, not how fast a meter fills* |
| ⛔ **Power Consumption** | ⛔ **FAILS AS WRITTEN** | ***The file literally says "Equivalent to hunger/thirst."*** **That is precisely, verbatim, the thing the governing standard rejects.** ⭐ **It should not be deleted — it should be re-derived** so that energy changes *route planning, engagement choices, and whether resting is safe*, rather than draining a bar |

> ### ⭐ THE PATTERN IN THE AUDIT
> **Every system that PASSES changes a DECISION** — *what to carry, who to bring, whether to engage, which
> route to take.* **Every system that FAILS or is WEAK is a DEGRADATION RATE** — *a bar that fills, watched
> rather than played around.*
>
> ⛔ ***So the failing systems are not failing because they are too easy or too harsh. They are failing because
> they are survival meters, and survival meters are the exact genre convention this ruling rejects.***

---

## Robot-Specific Hardcore Systems

**Standard Fallout Hardcore mechanics (hunger, thirst, sleep) apply to biological characters. The protagonist
of Inner Tepenia is a robot.** The robot-side systems are below.

> ⛔ **These are NOT "robot equivalents of hunger and thirst," and must not be designed as such.** *Per the
> governing standard, a robot analogue of a survival meter is still a survival meter.* ⭐ **Each system here
> earns its place only by changing how the player plays** — **and by that test, the ones flagged in the audit
> above do not yet.**

### Siligel — Robot Food
**Siligel is robot food.** Not lubricant, not blood, not a structural fluid — nutritional input. In standard mode it restores HP and energy immediately. In Hardcore mode, Siligel processes gradually — the benefit is delivered over time rather than instantly, making combat healing less reliable.

> ## ⭐⭐ THE FOUR-AXIS SILIGEL SPLIT — **developer proposal, 2026-09-04**
>
> | | **Normal** | **Hardcore** |
> |---|---|---|
> | **Types** | **one type of siligel** | **multiple types of siligel** |
> | **Function** | **does all tasks** | **each does a finite, dedicated task** |
> | **Weight** | **weightless** | **has weight** *(very slight, very very low, but still weight)* |
> | **Healing** | **heals instantly** *(like Fallout: New Vegas)* | **heals over time** *(like Fallout: New Vegas)* |
>
> ⚠ **PROPOSAL, not yet ruled.** *Two of the four axes — delivery and the general Hardcore weight principle —
> were already established in this file. The **classes** and **siligel-specific weight** axes are new.*

#### ⭐ Why this is the strongest Hardcore lever in the file

**Every other Hardcore system on this page makes an existing number worse.** *Thermal exposure adds
degradation; anomalies add memory corruption; wear adds a maintenance cost.* ***The class split does something
different: it changes what a resource IS.***

> **In Normal, siligel is a stack.** *One consumable, one number, spend it on whatever hurts.*
> **In Hardcore, siligel is an INVENTORY PROBLEM** — several things that look alike, do different jobs, and
> **cannot cover for each other.**

#### ⛔ The rule that makes it hard — **non-substitutability**

***The classes are not quality tiers. Quantity in one cannot cover a deficit in another.*** **A player can be
carrying plenty of siligel and still be unable to fix what is actually wrong.** *That is a genuinely different
failure state from "ran out of healing items," and it is the point of the whole system.*

#### ⭐⭐ Weight and classes MULTIPLY — this is the real difficulty delta

**Neither axis is very punishing alone.** *A slight per-dose weight is trivial; carrying three consumables
instead of one is mild bookkeeping.* ⭐ **Together, they force a real decision every time the player leaves
shelter: *which* siligel, and how much of each, for a trip whose demands are not yet known.**

> **And the failure is asymmetric.** *Guessing wrong on the combat class means a hard fight. **Guessing wrong
> on the maintenance class means damage that does not heal when the player gets home.*** **That is what
> converts a supply decision into a survival decision** — and it is exactly the "consuming rather than
> dangerous" distinction this file's Design Philosophy already claims as Hardcore's identity.

#### The fiction does not change between modes

⛔ **IMPORTANT.** ***In the world, siligel always has classes.*** **Normal mode ABSTRACTS them into a single
item for playability — it does not assert that robots only need one substance.** *No lore, dialogue, or
location file should ever be written as though the Normal-mode simplification were a fact about the world.*

⭐ **And the fiction favors Hardcore on the healing axis too:** *restoring a robot's internal surface chemistry
is a chemical process that propagates through a high-surface-area structure over time. **Gradual is the
physically accurate version; instant is the concession.***

> ### 📎 The proposed classes and the chemistry behind them
> **`Worldspace/Robot_Biology_and_Culture/Siligel_Composition_Research.md` §3c** derives a **three-class
> taxonomy** — *charge · interphase · structural* — from **three separate documented failure pathways in real
> silicon systems**, along with the non-substitutability rule above. ⚠ **That file is research, not canon**,
> and the class COUNT is open — *three, two, or some other number.*

#### ⚠ Open interaction — Coldshock and the classes

**The Coldshock spiral below reduces "Siligel efficiency."** ⭐ **With classes, that needs a target: efficiency
of *which* class?** *The likely answer is the energy class specifically — which would tie Coldshock directly to
the **Engine** stat (conversion rate) and to the recharge trade-off in
`Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md`.* ⛔ **Not ruled. Flagged.**

### Coldshock and Siligel Efficiency
The Coldshock condition (see `DLC_01_Echoes_of_Amundsen.md` for full stage table) reduces how much benefit the player gets from consuming Siligel. The cold impairs the protagonist's ability to process nutrition efficiently.

This creates a compounding spiral specific to the South Pole DLC:
1. Cold exposure → Coldshock accumulates
2. Coldshock → Siligel provides diminishing returns
3. Diminishing Siligel returns → need more food to maintain function
4. Resources are scarce → getting more food is difficult
5. Difficulty → more combat and exposure → more cold

In Hardcore mode, this spiral is tighter and faster than in standard mode. Getting out of cold and into shelter is not just good practice — it is mandatory resource management.

### Power Consumption

> ## ⛔⛔ FLAGGED FOR REWORK — **fails the governing standard, 2026-09-04**
> **The first bullet below says *"Equivalent to hunger/thirst."*** ***That is verbatim the design the developer
> ruling rejects*** — *"I don't want to make it so that, 'oh, well, now you need to worry about eating and
> drinking and sleeping and shit'."*
>
> ⭐ **Do not delete this system — RE-DERIVE it.** **Energy is load-bearing** *(it is what siligel restores, and
> `Siligel_Composition_Research.md` §2 makes it the material's primary property)*. **What has to change is the
> SHAPE:** ⛔ **not a bar that drains**, but ⭐ **a constraint that alters decisions** — *how far you can commit
> from a recharge point, whether you run or fight, which route is survivable, and* ⭐⭐ ***whether resting is
> even safe*** *(`Robot_Cold_Physiology.md`: **in cold, a robot is safer moving than resting** — an inversion
> of the standard RPG recovery instinct, and exactly the kind of thing the ruling asks for).*
>
> **The bullets below are RETAINED AS THE OLD DESIGN, pending that rework.**

- ⛔ ~~Equivalent to hunger/thirst~~ — **rejected framing, see above**
- High-intensity operation (sustained combat, running, heavy system use) depletes energy reserves faster than low-intensity movement
- Running dry does not kill instantly — it degrades performance in escalating steps before shutdown: Might penalties → Agility penalties → system failures → shutdown
- Energy restores through Siligel consumption, rest in safe areas, or power source items
- *Full design for power consumption tiers: TBD*

### Thermal Regulation
- The protagonist's thermal management systems are stressed by extreme cold
- In standard mode: thermal exposure causes HP damage
- In Hardcore mode: sustained cold also degrades the thermal regulation component itself — meaning the protagonist becomes *less able to handle cold* the longer they're exposed without recovery time
- Recovery requires not just reaching shelter but spending time there

### Memory Integrity
- Extended high-stress operation without a consolidation cycle (rest) degrades processing
- Low integrity effects: slower Calculation-dependent checks, Investigation thresholds harder to meet, occasional dialogue option mis-fires
- Not catastrophic immediately, but accumulating — and in the South Pole, rest opportunities are scarce
- Recovery: consolidation cycle in a safe location (the South Pole has very few of these)
- Magnetic anomaly zones (see DLC_01) accelerate memory integrity loss during prolonged exposure

### Component Wear
- In standard mode, equipment degrades but the protagonist's body systems are stable
- In Hardcore mode, specific body systems wear with use:
  - Agility-related components from sustained combat
  - Engine-related from extended exertion without rest
  - Thermal regulation from cold exposure
- Component wear creates maintenance requirements that don't exist in standard mode
- Unaddressed component wear eventually causes the associated stat to drop until repaired

---

## Companion Permanent Death (Hardcore)

Same as Fallout: New Vegas Hardcore mode. Companions who are downed and not revived in time are permanently dead.

**South Pole DLC implication:** Kendra Heinrich can be killed during the DLC before she joins the player as a companion. This is a permanent loss — she does not become available after the DLC if she died during it. This represents one of the highest stakes in any Hardcore playthrough.

---

## Further Development Required

The following aspects of Hardcore mode are undesigned and require a dedicated session:

### ⛔ FIRST — the rework queue from the 2026-09-04 audit

- [ ] ⛔ **RE-DERIVE Power Consumption** so it changes decisions rather than draining a bar — **it currently fails the governing standard outright**
- [ ] ⚠ **Rework Thermal exposure** — *candidate already on file: **in cold, resting is more dangerous than moving** (`Robot_Cold_Physiology.md`), which inverts the standard recovery instinct*
- [ ] ⚠ **Rework Coldshock stages 3–5** — *escalating penalties are not a play change; tie it to **which siligel class** it impairs instead*
- [ ] ⚠ **Rework Blizzard events** — *consider having blizzards **change which routes exist**, rather than filling a stress meter*
- [ ] ⭐ **Re-run this audit on every NEW Hardcore system before it is written** — *the one question: does it change how the player plays, or add something to watch?*

### Then

- [ ] ⭐ **Siligel class count and names** — three is proposed *(`Siligel_Composition_Research.md` §3c)*; two may play better. **Names there are explicit placeholders**
- [ ] ⭐ **Per-class weight values** — *"very slight, very very low"* needs an actual number, and it must stay low enough that the constraint is a decision rather than a tax
- [ ] **Which class Coldshock impairs** *(see the Coldshock interaction note above)*
- [ ] **Whether the Normal-mode single siligel is the energy class specifically, or a merged abstraction of all classes**
- [ ] Full power consumption tier system (depletion rates, penalty thresholds, recovery rates)
- [ ] Component wear repair mechanics (where, how, cost)
- [ ] Memory integrity consolidation mechanics (time required, location requirements)
- [ ] Interaction between all Hardcore systems simultaneously (compound failure states)
- [ ] Hardcore-specific items, perks, and traits
- [ ] Whether Hardcore mode is toggled at game start or can be changed mid-game
- [ ] Hardcore mode achievements / recognition
- [ ] Difficulty scaling adjustments specific to Hardcore (if any)
- [ ] How Hardcore interacts with the re-spec system (Identity Fragmentation under compound stress)
