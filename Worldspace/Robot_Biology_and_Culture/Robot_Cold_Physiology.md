# ROBOT COLD PHYSIOLOGY — what extreme cold actually costs a robot

**Created 2026-09-04**, at developer direction, out of the 37-city climate pass.
**Companion to `Robot_Physiology_and_Cultural_Practices.md`** — that file establishes what robots *are*;
this one establishes what deep cold *does to them*.

> ## ⭐ WHY THIS FILE EXISTS
> **Canon already establishes that robots are unaffected by the conditions that kill humans at Kunlun and
> Dome Fuji** — *"no respiratory system and different thermal-regulation physiology."* **That is true and
> stays true. It is not the same as "cold is free."**
>
> ***Altitude costs a robot nothing. Cold costs a robot a great deal — just along completely different
> axes than it costs a human.*** **Developer framing, 2026-09-04:** *"a huge part of it is being able to
> recharge, and how quickly cold-exposure depletes HP."*

---

# 1 · RECHARGING — the hard constraint

**This is the primary cost, and it is not a slower version of ordinary charging. It is a different
problem.**

> ### ⛔ THE GOVERNING FACT
> **Charging a cold cell below freezing causes lithium plating — metallic lithium deposits on the anode,
> permanently reducing capacity.** ***This is irreversible damage, not a temporary penalty.*** Safe cold
> charging requires cutting charge current to **5–10% of capacity** — **ten to twenty times slower.**

## The three-way trade-off

**A robot needing charge in the Frostlands chooses between three bad options.** *No option is free; this is
the shape of the decision.*

| Option | What it costs | When it is correct |
|---|---|---|
| **Warm the cells first, then charge normally** | **Spends stored energy to obtain energy** | When you still have reserve to spend |
| **Charge cold at 5–10% rate** | **10–20× the time**, exposed throughout | When you have time and shelter but no reserve |
| **Charge cold at full rate anyway** | ⛔ **PERMANENT maximum-capacity loss** | Emergency only — you are trading your future for your present |

## ⭐⭐ THE DEATH SPIRAL — the mechanic everything else hangs on

**Warming your own cells costs energy. Below some charge threshold, you no longer have enough energy to
warm them enough to charge safely.**

> ***Let your charge fall too far in deep cold and you cannot recover on your own. At all.***

**This single fact supplies, without any of it having to be invented:**
- **Why the Frostlanders maintain warmed charging shelters as infrastructure** — not hospitality, necessity
- **Why "properly equipped" has a concrete meaning** — it means never crossing that threshold
- **Why a stranded robot is genuinely stranded**, and why rescue is a real category of work
- **Why a well-prepared traveler may legitimately not need local help** — and why an unprepared one is not
  merely uncomfortable but unrecoverable

---

# 2 · TWO SEPARATE PENALTIES ON THE SAME RESOURCE

**Keep these distinct. They behave differently and should read differently.**

| | **Capacity reduction** | **Plating damage** |
|---|---|---|
| **Reversible?** | ⭐ **Yes** — warm up and it returns | ⛔ **No. Never** |
| **Cause** | Ambient cold, continuously | One bad charging decision |
| **Magnitude** | **−20–30% near freezing** · **down to 50–60% at −20 °C** · far worse at Frostlands ambient | Cumulative, permanent |
| **Reads as** | *The tank is smaller while you are cold* | *The tank is smaller forever* |

⭐ **A temporary squeeze and a permanent scar on the same bar.** *The interesting play is in never letting
the first force you into the second.*

## Output sag — a third, separate effect

**Cold causes voltage sag under load: peak deliverable power falls even with charge remaining.**
**A cold robot cannot lift, sprint or strike as hard as a warm one at identical charge.**
*Burst capability degrades independently of total reserve — three numbers, not one.*

---

# 3 · MECHANICAL EFFECTS

| Effect | Physics | Consequence |
|---|---|---|
| **Embrittlement** | Below the ductile-to-brittle transition temperature, materials fracture where they would otherwise deform | ⚠ **Impact damage becomes disproportionate.** A knock that dents at −10 °C **cracks** at −50 °C. *The damage type changes, not just the amount* |
| **Lubricant failure** | Below ~−40 °C standard greases *"exhibit properties similar to a solid, with catastrophic results"* | Joints stiffen; bearings and seals fail; **seizure is a real failure mode** |
| **Elastomer glass transition** | Seals lose flexibility and crack | **Coolant leaks** — and a coolant leak in deep cold is a compounding failure |

---

# 4 · ⭐⭐ THE INVERSION — a robot is safer MOVING than resting

**A working robot generates heat. That heat is exactly what keeps its cells in usable range and its
lubricants liquid.**

> ***Stopping is the dangerous act.*** **Cooling means capacity collapse, stiffening joints, and — past the
> threshold — the death spiral.**

⭐ **This is the exact opposite of human cold survival, where you shelter, still yourself and conserve.**
**A human who keeps moving in extreme cold exhausts themselves; a robot who stops moving strands
themselves.**

### What that gives the Frostlands

**A physical discipline that is genuinely robot, not borrowed from human mountaineering:** *staged
movement, no long halts outdoors, warmth budgeted as motion rather than hoarded as stillness.* **A
Frostlander robot does not find a sheltered spot and wait out a bad stretch. They keep working, because
working is what keeps them alive.**

*This is the sort of practice that should show in how Frostlanders carry themselves even indoors, and in
what they find alarming about outsiders' habits.*

---

# 5 · WHAT THIS MEANS FOR THE PLAYER

**The player is canonically a robot** *(build chosen at character creation; always a robot)*. Therefore:

- ⭐ **Altitude gates the player NOT AT ALL.** No respiratory system; the Concordia altitude problem is
  invisible to them. *See `…/Concordia-City/Concordia_Altitude_and_Atmosphere.md`.*
- ⭐ **Cold gates the player substantially** — but through **charge, output and structural integrity**,
  never through breath or warmth-as-comfort.
- ⭐ **A properly equipped player may legitimately not need Frostlander help.** *Developer intent,
  2026-09-04.* **The locals may notice and comment on how well prepared a player is** — and the readable
  signals are specific: **thermal management for the cells, a charging plan, sealed joints, and the
  discipline of not stopping.**
- ⚠ **And the inverse should read too:** *a player kitted for a katabatic coast — drift shovels, whiteout
  lines, aerodynamic shelter — is carrying dead weight here, and a Frostlander would clock that as
  inexperience just as fast as being underdressed.*

---

# ⚠ OPEN — NOT INVENTED HERE

1. ⭐ **THE GEL BRAIN.** **Siligel's behavior at −50 °C is unestablished** — whether it has a freezing or
   glass-transition point, and **whether cognition degrades before the body does.** ***Potentially the most
   interesting constraint in this entire file:*** a robot whose *thinking* slows in the cold is a different
   character problem from one whose joints stiffen. **Developer ruling required; deliberately not assumed.**
2. **Numeric rates** — how fast charge actually depletes per unit time at a given ambient — are a balance
   question, not a physics one. The physics above sets the *shape*; the tuning is a design decision.
3. **Whether plating damage is repairable at a facility** *(cell replacement)* and at what cost — this
   determines whether it is a permanent character consequence or an expensive errand.
4. **Coolant behavior in deep cold.** Robots normally need to *shed* heat; in the Frostlands that inverts.
   Whether coolant thickens, and whether the normal cooling system becomes a liability, is unestablished.

---

# SOURCES

**All figures in this file are real engineering values, not invented for the setting.** *Recorded with
addresses so the physics can be re-checked or extended rather than re-guessed.*

### Battery behavior in cold — §1 and §2

- ⭐ **Battery University, BU-410: "Charging at High and Low Temperatures"** — https://www.batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures/
  · *the lithium-plating mechanism; why sub-freezing charging causes permanent damage*
- ⭐ **RELiON, "Using Lithium Batteries in Cold Weather"** — https://www.relionbattery.com/knowledge/using-lithium-batteries-in-cold-weather
  · ***the 5–10%-of-capacity safe cold-charge current — the source of the 10–20× figure***
- **"Capacity loss"**, Wikipedia — https://en.wikipedia.org/wiki/Capacity_loss
  · *plating → capacity drop, internal shorts, irreversible damage*
- **Bonnen Batteries, "Battery Capacity vs Temperature"** — https://www.bonnenbatteries.com/battery-capacity-vs-temperature-how-temperature-affects-lithium-ion-battery-capacity/
  · **−20–30% near freezing; 50–60% of normal at −20 °C**
- **"From Range Loss to Recovery — Cold Weather Challenges and Design Strategies for Commercial Electric Vehicle Fleets"** — https://arxiv.org/pdf/2512.00541
  · *pre-conditioning/warming strategies — the real-world analogue of the warm-then-charge option*
- *Voltage sag under load in cold:* WattCycle — https://www.wattcycle.com/blogs/news/how-do-weather-conditions-affect-lithium-battery-performance

### Materials and mechanical failure — §3

- ⭐ **Nord-Lock Group, "Impact of Extreme Temperatures on Metallic Materials"** — https://www.nord-lock.com/en-us/learnings/knowledge/2019/extreme-temperatures/
  · *ductile-to-brittle transition; loss of ductility with falling temperature*
- **"Managing Cold Temperature and Brittle Fracture Hazards in Pressure Vessels"**, *Journal of Failure Analysis and Prevention* — https://link.springer.com/article/10.1007/s11668-015-0052-3
  · *DBTT near or above operating ambient in ordinary steels*
- **"Embrittlement"**, Wikipedia — https://en.wikipedia.org/wiki/Embrittlement
- ⭐ **Klüber Lubrication, "Lubricant Challenges in Extreme Cold Environments"** — https://www.klueber.com/us/en/company/newsroom/news/lubricant-challenges-in-extreme-cold-environments/
  · ***below −40 °C lubricants "exhibit properties similar to a solid — with catastrophic results"***
- **FUCHS, "Low Temperature Grease Selection Guide"** — https://www.fuchs.com/us/en/low-temperature-grease-selection-guide-for-bearings-gears-and-centralized-lubrication-systems/
  · *thickener stiffening; seal compatibility (NBR/FKM); leakage*
- **"Low-Temperature Rheology and Thermoanalytical Investigation of Lubricating Greases"**, *Lubricants* 10(1):1 — https://www.mdpi.com/2075-4442/10/1/1
  · *glass transition and pour point in greases*

### Setting-side inputs

- **Frostlands ambient conditions** — `Specs/Concordia.md` *(−52.7 °C mean annual; 2.8 m/s; PLATEAU regime)*
- **Why the plateau is calm rather than merely cold** — `Reference/Real-World/Climate Data/Precipitation_Falls_vs_Lands.md`
- **Robots do not breathe; Kunlun/Dome Fuji human exclusion** — `Robot_Physiology_and_Cultural_Practices.md`
- **The human half of the same problem** — `…/Concordia-City/Concordia_Altitude_and_Atmosphere.md`

*Full research record including verbatim search strings: `…/Locations/Cities/Research_Logs/Climate_Data_Research_Log.md`, Session 8.*
