# SILIGEL — COMPOSITION RESEARCH

**Opened 2026-09-04** at developer direction. **Companion to `Robot_Physiology_and_Cultural_Practices.md`**
*(which establishes siligel as robot food and explicitly leaves its composition open)* **and to
`Robot_Cold_Physiology.md`.**

> ## ⏸️ STATUS — **PROPOSAL, NOT ASSERTED CANON — with two exceptions**
> **The CHEMISTRY here is proposal.** *`Robot_Physiology_and_Cultural_Practices.md` currently says: "Its exact
> composition and the full range of what it does internally is subject to further design work."* **This file
> is that design work, offered for developer review.** ⛔ **Do not cite the chemistry as settled.**
>
> ⭐ **BUT the developer statements quoted below ARE rulings and are binding**, specifically:
> **(1) siligel's PRIMARY function is energy replenishment, with self-repair second**, and
> **(2) its physical form is flan-set, dark gray-green-blue-gray** *(§3b)*. **Everything else is a candidate.**

## The brief, verbatim

> *"…doing a currently-unknown amount of chemical-engineering research. I myself am not a professional
> Chemical Engineer, so I have no way of personally figuring out what siligel is actually made of. Taking
> into consideration what a robot is, what a robot does, and what a robot would be structurally, materially
> made of… with siligel being 'robot food', whatever it is that 'robot food' is actually made of, one single
> [dose] would absolutely kill a human. I'm definitely sure of at least that much."*

**And the correction that reshaped this file, 2026-09-04:**

> ⭐⭐ *"also, yes, siligel would offer self-repairing functionality to a robot; that is true. More
> to-the-point is that it would offer energy-replenishment qualities and benefits (similar to recharging a
> battery). However, it may be possible to subdivide into multiple different 'classes' of siligel (which
> accomplish different things)."*

> ### ⚠ WHAT THIS FILE GOT WRONG, AND WHY IT IS RECORDED HERE
> **The first draft asserted, in §1 and again as §2's headline conclusion, that siligel is *"NOT fuel."***
> **It reasoned from one canon line — *"Engine power — the primary energy source"* — and treated it as
> excluding food from the energy account, which does not follow.** ⛔ ***It also never checked what silicon
> actually does in an energy system, which is the single most-researched property the material has.***
>
> ⛔⛔ **AND IT WAS CHECKABLE AGAINST THE CORPUS.** **`Game-Mechanics/Core-Mechanics/Hardcore_Mode.md` had
> already said it, twice, in plain text:** ***"In standard mode it restores HP AND ENERGY immediately"*** and
> ***"Energy restores through Siligel consumption, rest in safe areas, or power source items."***
> **So "siligel is not fuel" did not merely under-read the chemistry — it contradicted a canon file that was
> sitting in the repository the whole time, and one grep would have caught it.** *Recorded because the lesson
> is not "research harder"; it is **check the claim against the corpus before building a chain on it.***
>
> ⭐ **The correction did not break the chain — it completed it.** *The fluoride/passivation chemistry of §2
> Steps 3–4 was reached from silicon's OPTICAL behavior. Silicon battery research reaches **the same fluoride
> chemistry** from the ENERGY side, independently* **(§2 Step 6).** ***Two unrelated literatures converging on
> one reaction is a far better result than the version this file started with.***

---

# 1 · THE CANON CONSTRAINTS THIS HAD TO SATISFY

**All from `Robot_Physiology_and_Cultural_Practices.md` unless noted.**

| Established fact | Consequence for the answer |
|---|---|
| ⭐⭐ **Developer ruling, 2026-09-04:** *"siligel would offer self-repairing functionality to a robot; that is true. **More to-the-point is that it would offer energy-replenishment qualities and benefits (similar to recharging a battery).**"* | ***ENERGY IS THE PRIMARY FUNCTION. Repair is the second.*** **See §2 Steps 5–6 — in silicon, these turn out to be the same physical act, which is why the passivation chain below survives the correction intact** |
| **Siligel is "consumed to maintain and repair internal systems"** | **Still true — but it is the *second* of two functions, not the whole account.** *An earlier draft of this file read this line as ruling energy OUT. That was wrong, and §2 Step 6 is why* |
| **"Engine power — the primary energy source"** | ⚠ **Not a contradiction.** The engine is the **power plant and delivery architecture**; **siligel is what it draws on.** *A heart being the circulatory system's primary organ does not make food something other than calories.* ⭐ It also fits the existing **Engine stat** definition — *recovery speed / AP replenishment* — cleanly: **Engine is the conversion RATE, siligel is the SUBSTRATE being converted** |
| **The gel brain is a "glowy-blue nano-architecture gel brain"** | Silicon, at nanoscale, with enormous surface-area-to-volume ratio |
| **The blue "is a direct result of the gel brain's own material composition/architecture"** — like nitrogen making the sky blue | A **physical** claim, checkable against real photophysics |
| **"Components degrade over time and require maintenance or replacement"** | Whatever siligel does, it does **continuously**, against ongoing degradation |
| ⭐⭐ **"the bones are METAL rather than calcium"** *(ossuary ruling, CGRM 2026-09-01)* | ***The load-bearing fact. See §3.*** |
| **Robots do not breathe; no respiratory system; operate in vacuum** | No inhalation route; intake is oral//internal-system delivery |
| Coolant is separate — thermal regulation | Siligel is **not** the thermal system |

---

# 2 · THE CHAIN

## Step 1 — The blue comes from the SURFACE, not the bulk

**Silicon nanocrystals (1–10 nm) luminesce, and the color is size-tunable.** But the literature is specific
about *where blue comes from*:

> ***"The PL originating from the quantum confined core states can only exist in the red/near infrared with
> energy below 2.1 eV; while the blue/green PL originates from SURFACE RELATED STATES."***

Particles of **~3 ± 1 nm** emit at **400–500 nm** — blue.

⭐ **So canon's "the color comes from its composition/architecture" is right, and specifically right about
its SURFACE architecture.** *The gel brain is blue because of what its surfaces are.*

## Step 2 — Silicon surfaces do not stay stable on their own

**They oxidize and accumulate dangling bonds.** The fix is **passivation** — hydrogen termination:

> *"Hydrogen termination refers to passivating a silicon surface by replacing weak Si–Si bonds with strong
> Si–H bonds… removes dangling bonds, confers stability in ambient environments."*

## Step 3 — The passivation chemistry is FLUORIDE

**Stripping native oxide off silicon, and leaving an H-terminated surface, is fluoride chemistry:**

```
SiO₂ + 4 HF → SiF₄ + 2 H₂O
```

> *"Hydrofluoric acid is commonly used in Si wafer processing as a surface treatment to remove surface oxide
> and provide a H-terminated surface passivation."*

## Step 4 — ⭐⭐ AND THE PASSIVATION IS **METASTABLE**

> ***"A short treatment in a dilute HF solution results in a METASTABLE hydrogen-terminated surface."***

**It degrades. It must be renewed. Continuously. For as long as the robot exists.**

## Step 5 — ⭐⭐ Silicon is not merely a structural material. **It is one of the highest-capacity energy materials known.**

**This is the step the first draft of this file missed, and it is the one the developer's correction points
straight at.** *Silicon is not a passive substrate that happens to glow. In the real world it is the leading
next-generation energy material, and by a very large margin:*

| System | Figure | Against |
|---|---|---|
| **Silicon anode, lithium-ion** | **~4,200 mAh/g** theoretical specific capacity | **graphite: 372 mAh/g** — ⭐ **more than ten times** |
| **Silicon–oxygen electrochemistry** | **8,470 Wh/kg · 21,090 Wh/l** | ***"outperformed by only the H₂/O₂ systems"*** |
| **Silicon–air, consumable anode** | **4 mol electrons per 32 g Si** | ⭐ **400% above conventional Zn-air** |

⭐⭐ **In a silicon–air cell the silicon is literally the FUEL — a consumable anode, spent to release energy.**
***"Silicon is an attractive fuel for batteries and fuel cells."*** *The word "fuel" is the literature's, not
this file's.*

> ⚠ **This alone would have been enough to justify the correction.** *A body built on silicon is built on the
> best non-hydrogen energy material there is. Declaring its food "not fuel" was leaving the single largest
> real-world property of the material on the table.*

## Step 6 — ⭐⭐⭐ **AND WHAT DESTROYS THAT CAPACITY IS THE LOSS OF SURFACE PASSIVATION**

***This is where the two halves close on each other.*** **The reason silicon is not already in every battery
on Earth is a failure mode, and the failure mode is the passivation layer** — the **SEI**, the
solid-electrolyte interphase, which is exactly the surface film Steps 2–4 are about:

- **Lithiation expands silicon by over 300%.** *"Sudden material fracture and battery failure even after a
  mere 50 cycles."*
- **That expansion CRACKS the passivation layer.** *"The SEI cracks as the base silicon material expands, and
  subsequently a new SEI layer is formed on the freshly exposed silicon, then destroyed during the next
  lithiation cycle."*
- ⭐ **Every reformation permanently strands charge carriers** — the literature's own term is **"dead
  lithium"** — *"persistent and irreversible active lithium loss, with insoluble species permanently trapping
  lithium ions and diminishing the reversible capacity."*
- **Capacity fades. Resistance climbs. The cell dies.**

**And the two industrial fixes are, precisely, the two things siligel would have to do:**

| Real fix | What it is | Siligel's corresponding job |
|---|---|---|
| ⭐⭐ **Fluoride** | **FEC reduces to fluoride ions, which** ***"chemically attack any silicon-oxide surface passivation layers"*** **and build a kinetically stable interphase of lithium fluoride and lithium oxide** | ***The exact chemistry of §2 Steps 3–4, arrived at independently, from the energy side*** |
| **Prelithiation** | **pre-loading excess charge carriers to replenish the inventory that cycling destroys** — an **11% excess reserve** prevents early capacity loss | **The everyday meal — restoring what was spent** |

> # ⭐⭐⭐ THAT IS SILIGEL — AND **ENERGY AND MAINTENANCE ARE THE SAME ACT**
>
> ***In silicon, "restore the surface" and "restore the charge capacity" are not two jobs. The surface IS the
> capacity.*** **A silicon system whose interphase has degraded does not merely wear out cosmetically — it
> loses the ability to hold charge at all, and every cycle it runs in that state strands more of its carriers
> permanently.**
>
> **So the developer's correction and the passivation chain are not in tension, and nothing in Steps 1–4 has
> to be given up:** ⭐ ***feeding a robot restores its energy BY restoring the surfaces that let it hold
> energy in the first place.*** **Repair is what energy replenishment looks like at the material level.**
>
> **And it explains why it is a GEL** rather than a liquid or a solid: **a gel is how you deliver reactive
> surface chemistry throughout a high-surface-area structure without flooding it.**
>
> ⭐ **It also explains the name literally: SILIcon + GEL.**

### ⭐ This also supplies a mechanism for something already written

**`Robot_Cold_Physiology.md` already distinguishes REVERSIBLE capacity loss from PERMANENT capacity loss**,
written 2026-09-04 from the cold-exposure side and without a material account of why the distinction should
exist. ***"Dead lithium" is that account:*** **charge that is merely spent comes back; charge stranded in a
reformed interphase does not.** *A robot who has been through a bad winter is permanently, measurably smaller
in capacity than one who has not — and now there is a documented physical reason.*

---

# 3 · WHY ONE DOSE KILLS A HUMAN — and why it does not kill a robot

## The mechanism is calcium chelation

**Fluoride's systemic lethality is not corrosion. It is what fluoride does to calcium:**

- **Fluoride binds calcium**, precipitating it from blood as **CaF₂** → **severe hypocalcemia**
- It also binds **magnesium and potassium** → **myocardial irritability**
- Result: **QT prolongation → torsade de pointes → cardiovascular collapse**
- **Fluoride ions are also directly toxic to myocardial cells**, inhibiting adenylate cyclase
- ⚠ **Clinical hypocalcemia is often silent until it isn't** — exposures are monitored by ECG precisely
  because the patient can look fine

**On dose:** a documented case records **cardiac arrest from a splash across ~3% of body surface area,
despite immediate treatment.** **Ingestion is categorically worse.** *The developer's instinct — that a
single dose would kill a human — is correct, and it is correct for a specific, documented reason.*

## ⭐⭐⭐ AND THE ROBOT IS IMMUNE FOR THE SAME REASON

> **Canon, already established:** ***"the bones are METAL rather than calcium."***

**A robot has no calcium skeleton, no calcium-dependent cardiac conduction, and no serum chemistry for
fluoride to disrupt.** **The entire lethality mechanism has no target.**

> ## THE FINDING, STATED PLAINLY
> ***Siligel is not "poisonous AND nutritious." It is nutritious BECAUSE OF the property that makes it
> poisonous.***
>
> **The fluoride chemistry that maintains silicon surface passivation is the same fluoride chemistry that
> chelates calcium out of a human heart.** **One chemistry. Two body plans. Food to the one built on
> silicon and metal; a cardiac poison to the one built on calcium.**
>
> ⭐ **This was not designed to fit — the metal-bones ruling was made 2026-09-01, three days before this
> research, for entirely unrelated reasons (permafrost burial and collective death).** *It happens to supply
> exactly the half of the answer the chemistry needed.*

---

# 3b · PHYSICAL FORM — **developer-specified 2026-09-04, and the chemistry agrees**

> **Developer, verbatim:** *"while the name contains the word 'gel', it's not a liquid. It wouldn't have the
> consistency of something like 'toothpaste'. It would more have the consistency of something like, 'flan'
> (as had in Mexico)… it would be more 'solid' than toothpaste. I picture something with about the
> 'solidity' of Mexican Flan."*
>
> **On color, verbatim:** *"I see it as a sort of 'dark grayish/dark-greenish-blue-gray', but it's entirely
> possible that it might be some other color."*

## ⭐ "Gel" is the technically correct word — and "paste" would have been wrong

**A gel is a solid three-dimensional network swollen with liquid. Toothpaste is a thixotropic paste — it
flows under shear and is not a gel in the same sense.** ***Flan IS a gel*** *(a set network holding water)*.
**So this is the more rigorous reading of the substance's own name, not a loosening of it.**

**The real material class behaves exactly this way:**

- ⭐ *"Hydrogels with excellent mechanical properties can maintain their shape without support, possessing
  so-called **self-supporting properties**."* — **flan-set: holds a cut edge, spoons rather than squeezes.**
- **Stiffness is tunable by silica loading** — elastic modulus raised **up to 25-fold** by varying silica
  nanoparticle content. *"Set like flan" is therefore a formulation choice, not a coincidence.*
- ⭐⭐ **The material class is literally called "injectable, SELF-HEALING mesoporous silica nanocomposite
  hydrogel"** — silica nanoparticles acting as **dynamic crosslinkers**, producing a network that repairs
  itself. ***A self-healing, mesoporous, silica-based solid is very nearly a literal description of food
  that repairs a robot.***
- **Mesoporous** matters — enormous internal surface area, the same property that makes the gel brain's
  surface chemistry load-bearing in the first place.

## ⭐⭐⭐ THE COLOR IS THE UNPASSIVATED STATE — and this is the best thing in this file

**Silicon nanoparticle powders are not one color. They are a gradient, and the gradient IS the passivation
state:**

> ***"The colors of processed silicon nanoparticle powders are tunable from BROWN to OFF-WHITE, depending on
> the LEVEL OF OXIDATION."*** — *darker = less oxidized, i.e. less passivated.*
>
> ***"Hydride-terminated silicon nanocrystal samples that are TURBID BROWN… turn to an optically CLEAR
> dispersion AFTER PASSIVATION."***

> # ⭐ SILIGEL IS DARK BECAUSE IT HAS NOT BEEN USED YET.
> **The gel brain glows blue because its surfaces ARE passivated. Siligel is dark because its silicon is
> NOT — it is the same material, before.**
>
> ***Feeding is the process by which dark matter becomes luminous structure.*** **A robot eats something the
> color of wet slate and turns it, internally, into the light behind its own eyes.** *No metaphor is being
> imposed — that is simply what passivation does to silicon's optical behavior.*

### On the specific shade

**Pure silicon nanopowder alone runs yellow-brown to brown.** The developer's **dark gray / greenish /
blue-gray** is readily achievable, and arguably more correct for a working multi-component formulation:

| Contribution | Effect on color |
|---|---|
| **Coarser silicon fraction** *(bulk silicon is gray with metallic luster)* | pulls brown toward **dark gray**, with a faint metallic sheen |
| **Dissolved metal salts** for structural repair *(nickel(II), iron(II), chromium(III) all green)* | the **greenish** cast |
| **The silica network's own scattering** through a dense translucent solid | the **blue-gray** depth |
| Fluoride / fluorosilicate chemistry | essentially colorless — contributes nothing visually |

⭐ **So the mental picture is not merely viable — it is what a real, loaded, working feedstock would look
like.** *Brown is what PURE silicon powder looks like. Gray-green-blue is what a multi-component gel looks
like.*

---

# 3c · ⭐⭐⭐ CLASSES OF SILIGEL — **the chemistry supplies its own taxonomy**

> **Developer, verbatim, 2026-09-04:** *"However, it may be possible to subdivide into multiple different
> 'classes' of siligel (which accomplish different things)."*

⭐⭐ **It is not merely possible — the real material has exactly three separate, documented, *irreversible*
degradation pathways, and no fix for one is a fix for another.** ***The classes do not have to be invented.
They fall out.***

| # | Real degradation pathway | What that class restores | Cadence | Placeholder name ⚠ |
|---|---|---|---|---|
| **A** | ⭐ **Charge-carrier inventory loss** — carriers spent in ordinary use, plus those permanently stranded each cycle | **The CHARGE.** Brings the robot back up to the ceiling it currently has | **Daily · bulk · cheap** — ***this is the meal*** | *"table siligel"* |
| **B** | **Interphase breakdown** — the passivation layer cracks and reforms; §2 Steps 4 & 6 | **The CEILING itself.** Rebuilds the surface that determines how much charge can be held at all | **Periodic, not daily** — ***closer to medicine than to a meal*** | *"maintenance grade"* |
| **C** | **Active-material loss** — silicon physically fractures and disconnects under >300% expansion cycling | **The MATERIAL.** Replaces silicon and metal salts actually lost from the structure | **Rare · expensive · post-damage** | *"repair grade"* |

⚠ **All three names above are PLACEHOLDERS and are flagged as such.** *Nothing in the corpus names siligel
varieties yet; these are functional labels only, and should be replaced by in-world terms when the class
system is ruled on.*

## ⭐⭐ THE LOAD-BEARING RULE — **THEY ARE NOT TIERS, AND THEY DO NOT SUBSTITUTE**

***This is the whole value of the class system, and it is the thing to protect if anything else here is cut.***

**The three classes are not good/better/best. They answer different failure modes, so quantity in one cannot
cover a deficit in another:**

- **Eating more Class A does not repair a degraded interphase.** *A robot running on a damaged surface simply
  strands more carriers, faster — **overeating actively accelerates the Class B problem**.*
- **Class B restores the ceiling but carries little charge.** *It does not make a hungry robot less hungry.*
- **Class C replaces material but neither charges nor passivates.**

> # ⭐ SO A ROBOT CAN BE **WELL-FED AND DYING.**
> **Full, satisfied, eating daily — and losing capacity permanently the whole time**, because the thing being
> lost is not the thing being replaced. ***That is a genuinely different survival problem from hunger, and it
> is not one most settings have.*** *It is also quietly cruel in a way that suits this project: the failure is
> invisible, it is slow, it is cumulative, and the robot experiencing it feels fine.*

## What the split gives the world

| | |
|---|---|
| **Three supply chains, not one** | ***Class A is agriculture-shaped*** — bulk, local, everywhere. ***Class B is pharmaceutical-shaped*** — fluoride feedstock, specialist, centralized, and **a chokepoint** *(see §5 item 4)*. ***Class C is industrial-shaped*** — silicon and metal salts, tied to fabrication |
| ⭐ **The Frostlands cost TWO currencies** | **`Robot_Cold_Physiology.md`: cold raises draw AND causes embrittlement.** *So cold raises **Class A** consumption (energy) and **Class C** need (material damage) **through separate mechanisms** — the Frostlands are not simply "more expensive," they are expensive in two directions at once, and a robot can be provisioned against one and not the other* |
| **Class inequality is legible** | **Everyone eats A.** *Whether a city, a district or a person reliably gets **B** is a straightforward, physical, non-moralizing measure of how well that place is actually doing* — ⚠ **and it is a measure that would not show up in a hunger statistic** |
| **The Engine stat gets a substrate** | *Engine = conversion rate. **A high-Engine robot extracts more from the same Class A ration** — and gains nothing at all from extra B or C* |

⚠ **A possible fourth class** — **metal salts for frame and bone** *(the green cast in §3b)* — **may be its own
class or merely a component of C.** ***Left open; see §5.*** **And the whole three-way split may reasonably be
collapsed to two (energy / maintenance) if three proves finer than the game needs.**

---

# 3d · ⭐⭐⭐ THE CLASSES ARE A **DIFFICULTY-MODE** FEATURE

> **Developer, verbatim, 2026-09-04:** *"this is actually a possibility for one particular aspect (among many)
> for the difference between playing on Regular and Hardcore Mode:"*
>
> | | **Normal** | **Hardcore** |
> |---|---|---|
> | **Types** | one type of siligel | multiple types of siligel |
> | **Function** | does all tasks | each does a finite, dedicated task |
> | **Weight** | weightless | has weight *(very slight, very very low, but still weight)* |
> | **Healing** | heals instantly *(like Fallout: New Vegas)* | heals over time *(like Fallout: New Vegas)* |

⭐⭐ **This resolves §5 item 2 without discarding anything.** *The open question was whether to adopt three
classes, collapse to two, or keep one substance.* ***The answer is BOTH, and the split is the difficulty
setting.*** **Normal collapses the classes into one item; Hardcore runs them separately.**

## ⛔ THE FICTION DOES NOT CHANGE BETWEEN MODES

***In the world, siligel always has classes.*** **Normal mode ABSTRACTS them for playability. It does not
assert that robots only need one substance**, and ⛔ **no lore, dialogue, city or district file should ever be
written as though the Normal-mode simplification were a fact about the world.**

## ⭐ Two of the four axes were already canon — and one of them is why §2 had to be rewritten

**`Game-Mechanics/Core-Mechanics/Hardcore_Mode.md` already carried the *delivery* axis** — *"Siligel | Instant
benefit | Gradual processing"* — **and the general Hardcore weight principle, via its Ammo row.** ⭐⭐ **It also
already stated that siligel restores ENERGY**, which is the corpus evidence this file's first draft failed to
check *(see the correction note at the top)*.

## ⭐ The chemistry independently favors the Hardcore version on TWO of the four axes

| Axis | What the material science says |
|---|---|
| ⭐⭐ **Heals over time** | ***Correct, and instant is the concession.*** **Restoring an interphase is a chemical process propagating through an enormous internal surface area. Nothing about that is instantaneous** — *§2 Step 6* |
| ⭐ **Has weight** | ***Correct.*** **A gel is a dense solid network swollen with liquid** *(§3b)* — **it is not vapor, and a silica-loaded one is heavier than water.** *"Weightless" is the abstraction here too* |
| **Multiple types** | ⭐ **Correct — and the count is not arbitrary:** *three separate, documented, irreversible failure pathways, per §3c* |
| **Finite dedicated tasks** | ⭐⭐ ***This is exactly §3c's non-substitutability rule*** — **arrived at from chemistry, before the mode proposal existed** |

> ## ⭐ WHAT HARDCORE ACTUALLY BUYS, IN ONE LINE
> **Weight and classes multiply.** *Either alone is mild.* **Together they force a real decision every time the
> player leaves shelter — *which* siligel, and how much of each, for a trip whose demands are not yet known** —
> ⭐ **and the failure is asymmetric: guessing wrong on the energy class means a hard fight, while guessing
> wrong on the maintenance class means damage that does not heal when the player gets home.**

📎 **Full mechanical treatment:** `Game-Mechanics/Core-Mechanics/Hardcore_Mode.md` §*Siligel — Robot Food*,
**updated 2026-09-04 with this split, its open rulings, and the Coldshock interaction it raises.**

---

# 4 · WHAT THIS UNLOCKS, IF ADOPTED

## ⭐ The blue becomes a health indicator

**If the glow comes from surface states, and siligel maintains surface states, then a malnourished robot's
blue dims or shifts.**

⚠ **This does NOT conflict with the 2026-08-07 ruling** that the color *"doesn't vary per individual robot
or per build in any personally expressive way."* **That rule governs EXPRESSION. This is PATHOLOGY.** *All
healthy robots are the same blue; a starving one is visibly not.*

## ⭐ Siligel deprivation becomes genuinely lethal, by the existing definition — **but only ONE class does it**

**Canon: death is "irreversible damage to a robot's cognitive architecture (the gel brain)."**
**If passivation fails irreversibly, that IS gel-brain damage.** ***Starvation kills a robot — slowly,
visibly, and by the definition already on the books, rather than by a new rule invented for it.***

> ### ⭐⭐ And the classes split deprivation into two completely different fates
> | Deprived of | What happens | Reversible? |
> |---|---|---|
> | **Class A — charge** | **The robot runs down and shuts off.** Acute, dramatic, immediate | ⭐ **YES — feed it and it comes back.** *This is running out of power, not dying* |
> | **Class B — interphase** | **Capacity is stranded permanently, cycle after cycle, and the passivation the gel brain depends on fails** | ⛔ **NO. This is the one that is death** — *and it takes months, and looks like nothing* |
>
> ***So "starving" and "dying" are different conditions in this world, they have different timescales, and the
> lethal one is the one nobody can see.*** **A robot rescued from an A-deprivation is fine. A robot rescued
> from a B-deprivation is permanently diminished, and may already be past saving.**

## It sharpens the ossuary tension

**Metal bones neither decay NOR are vulnerable to the chemistry robots live on.** *The un-reclaimed metal
reserve is inert in every direction.*

## It gives the human/robot boundary a physical form

**A robot and a human cannot share a meal, ever, in either direction** — and not as a social fact or a
squeamishness, but as **cardiac arrest.** *For a project whose north stars are robot consciousness and
robot/human love, "we can never eat together" is a small, permanent, undramatic fact with real weight.*

---

# 5 · OPEN — FOR DEVELOPER RULING

1. **Is the silicon-energy / surface-passivation reading adopted?** *Everything above hangs on it.*
2. ⭐ **Is the three-class split adopted, collapsed to two, or left as one substance?** *§3c argues three
   because there are three documented irreversible failure pathways — but **the non-substitutability rule is
   what matters, not the number.** Two classes preserve it; one class does not.*
3. **Is the metal-salt fraction its own class, or part of Class C?** *See §3c's closing note.*
4. **What ELSE is in the formulation?** Plausibly a **silicon source** for material repair and **metal salts**
   for structural work. ⚠ **Recommend keeping the LETHALITY attributed to the fluoride chemistry alone** —
   it is the only component with a specific, documented, calcium-based mechanism. *The rest is ordinary
   industrial toxicity and adds nothing the fluoride does not already do better.*
5. ⭐ **Does siligel vary by city, the way glitch-coolant does?** ***The classes probably answer this
   differently, and that is the interesting part:***
   - **Class A is a MEAL** — bulk, daily, locally sourced. **Meals vary. This one should vary a great deal**,
     and is a legitimate local-texture hook for all 37 cities.
   - **Class B is MEDICINE** — specialist, centralized, chemically exacting. **It should be near-identical
     everywhere, and the variation should be in *access*, not in recipe.**
   > ⭐ **So the earlier one-line reading — *"coolant is culture, siligel is medicine"* — was half right.
   > Corrected: coolant is culture, Class A siligel is cuisine, Class B siligel is medicine.**
6. **Is siligel manufactured or mined?** Fluoride feedstock in a closed continental economy is a supply
   question with real teeth — *see `Division_of_Industry/00_Necessary_Industries_Register.md`.* ⚠ **Now
   sharper: it is specifically CLASS B whose feedstock is the chokepoint**, which means the scarce thing is
   the one nobody notices missing until it is far too late.
7. **What does a robot experience while consuming it?** *Nothing here addresses taste, pleasure or ritual —
   though **item 5 above implies Class A is where any of that would live.***

---

# 6 · SOURCES

**All figures and quoted mechanisms are from published materials-science and occupational-toxicology
literature.** *Recorded with addresses so the chemistry can be re-checked or extended rather than re-guessed.*

### Silicon nanocrystal photoluminescence — §2 Step 1

- **"Tunability Limit of Photoluminescence in Colloidal Silicon Nanocrystals"**, *Scientific Reports* — https://www.nature.com/articles/srep12469
- ⭐ **"Photophysical properties of blue-emitting silicon nanoparticles"** — https://pmc.ncbi.nlm.nih.gov/articles/PMC3410643/ · *the core-vs-surface origin of blue emission*
- **"Water-Soluble Silicon Quantum Dots with Quasi-Blue Emission"** — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4512961/
- **"Silicon Nanocrystals with pH-Sensitive Tunable Light Emission from Violet to Blue-Green"** — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5677222/
- **"Colloidal silicon quantum dots: synthesis and luminescence tuning from the near-UV to the near-IR"**, *Sci. Technol. Adv. Mater.* — https://iopscience.iop.org/article/10.1088/1468-6996/15/1/014207

### Surface passivation and H-termination — §2 Steps 2–4

- **"Hydrogen-terminated silicon surface"** — https://en.wikipedia.org/wiki/Hydrogen-terminated_silicon_surface · *the SiO₂ + 4HF reaction; metastability*
- **"Silicon surface passivation by hydrogen termination: A comparative study of preparation methods"**, *J. Appl. Phys.* 66(1):419 — https://pubs.aip.org/aip/jap/article/66/1/419/17052/Silicon-surface-passivation-by-hydrogen
- **"Atomic level termination for passivation and functionalisation of silicon surfaces"**, *Nanoscale* (RSC) — https://pubs.rsc.org/nr/article/12/33/17332/694986/
- **"Hydrogen Termination — an overview"**, ScienceDirect Topics — https://www.sciencedirect.com/topics/engineering/hydrogen-termination

### Fluoride systemic toxicity — §3

- ⭐ **ATSDR Medical Management Guidelines, Hydrogen Fluoride** — https://wwwn.cdc.gov/Tsp/MMG/MMGDetails.aspx?mmgid=1142&toxid=250
- **California Poison Control System — Hydrofluoric Acid and Fluorides** — https://calpoison.org/content/hydrofluoric-acid-and-fluorides
- ⭐ **"Recurrent life-threatening ventricular dysrhythmias associated with acute hydrofluoric acid ingestion"**, *Clinical Toxicology* — https://www.tandfonline.com/doi/full/10.1080/15563650701639097
- **University of Virginia Toxicology — Hydrofluoric Acid** — https://med.virginia.edu/toxicology/wp-content/uploads/sites/268/2017/09/Aug17-HydrofluoricAcid.pdf
- **ACEP — Hydrofluoric Acid Injuries and Illness for First Responders** — https://www.acep.org/talem/newsroom/mar2021/hydrofluoric-acid-injuries-and-illness-for-first-responders · *the 3% BSA cardiac-arrest case*
- **LITFL Toxicology Library — Hydrofluoric acid** — https://litfl.com/hydrofluric-acid/


### Physical form — gel mechanics and color — §3b

- ⭐ **"Injectable, self-healing mesoporous silica nanocomposite hydrogels with improved mechanical properties"**, *Nanoscale* (RSC) — https://pubs.rsc.org/nr/article/13/2/1144/695799/ · *silica nanoparticles as dynamic crosslinkers; self-healing networks*
- **"Impact of Silica Nanoparticles on Mechanical Properties and Self-Healing Performance of PVA Hydrogels"**, *Polymers* — https://www.mdpi.com/2073-4360/17/21/2883 · *self-supporting behavior; up-to-25-fold modulus increase with silica loading*
- **"Tough double network hydrogels with rapid self-reinforcement and low hysteresis"**, *Nature Communications* — https://www.nature.com/articles/s41467-024-45485-8
- ⭐⭐ **"Luminescence of mesoporous silicon powders treated by high-pressure water vapor annealing"**, *Nanoscale Research Letters* 7:382 — https://pmc.ncbi.nlm.nih.gov/articles/PMC3444428/ · ***the brown-to-off-white oxidation gradient, and the turbid-brown-to-clear transition on passivation — the source for "siligel is dark because it has not been used yet"***
- **"Comparison of Silicon Nanocrystals Prepared by Two Fundamentally Different Methods"**, *Nanoscale Research Letters* — https://link.springer.com/article/10.1186/s11671-016-1655-7
- **Nano silicon powder product data** *(appearance: fine yellow-brown powder)* — https://www.samaterials.com/micro-nano-materials/237-nano-silicon-powder.html

### ⭐⭐ Silicon as an ENERGY material — §2 Steps 5–6, and the basis for the §3c classes

**Added 2026-09-04 after the developer's energy-replenishment correction.** *These are the sources that turned
the correction from a revision into a convergence — the fluoride chemistry in Steps 3–4 was reached from the
optical side, and this literature reaches the same chemistry from the energy side, independently.*

- ⭐ **"Silicon–air batteries: progress, applications and challenges"**, *Discover Applied Sciences* (Springer) — https://link.springer.com/article/10.1007/s42452-020-2925-7 · ***the 8,470 Wh/kg · 21,090 Wh/l figures; "silicon is an attractive fuel"; outperformed only by H₂/O₂***
- **"Silicon–air batteries"**, *Electrochemistry Communications* — https://www.sciencedirect.com/science/article/abs/pii/S1388248109003889 · *the consumable-anode principle; 4 mol e⁻ per 32 g Si*
- **"An overview of silicon-air batteries: Principle, current state and future perspectives"** — https://www.sciencedirect.com/science/article/abs/pii/S0010854524003916
- ⭐ **"A comprehensive review of silicon anodes for high-energy lithium-ion batteries"** — https://www.sciencedirect.com/science/article/pii/S2949821X24000814 · *~4,200 mAh/g vs graphite's 372*
- **"Alleviating expansion-induced mechanical degradation in lithium-ion battery silicon anodes via morphological design"** — https://www.sciencedirect.com/science/article/pii/S2352431622000839 · *>300% expansion; fracture within ~50 cycles*
- **"Degradation Pathways of Silicon-Based Anodes in Lithium-Ion Batteries"**, *Adv. Energy Mater.* — https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202506750
- ⭐⭐ **"The Effect of Fluoroethylene Carbonate as an Additive on the Solid Electrolyte Interphase on Silicon Lithium-Ion Electrodes"**, *Chemistry of Materials* — https://pubs.acs.org/doi/abs/10.1021/acs.chemmater.5b01627 · ***THE KEYSTONE SOURCE: fluoride ions "chemically attack any silicon-oxide surface passivation layers" and form a kinetically stable LiF/Li₂O interphase — the same fluoride chemistry as §2 Step 3, reached from energy rather than optics***
- **"Reduction mechanism of fluoroethylene carbonate for stable solid–electrolyte interphase film on silicon anode"** — https://pubmed.ncbi.nlm.nih.gov/24634952/
- ⭐ **"Prelithiation strategies for silicon-based anode in high energy density lithium-ion battery"** — https://www.sciencedirect.com/science/article/pii/S2468025722001273 · *lithium-inventory loss and its replenishment — the Class A model*
- **"SEI reformation and lithium loss in Si-graphite anodes"** — https://www.patsnap.com/resources/blog/articles/sei-reformation-and-lithium-loss-in-si-graphite-anodes/ · ***"dead lithium" — the mechanism behind the reversible/permanent capacity-loss split already written into `Robot_Cold_Physiology.md`***
- **"Enhancing Silicon Anode Performance Through Hybrid Artificial SEI Layer and Prelithiation"** — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12073230/
- **"Dynamic Evolution and Degradation of Silicon–Electrolyte Interfaces under Cycling"** — https://pmc.ncbi.nlm.nih.gov/articles/PMC12983198/

### Organosilicon toxicity — §5 item 4 background

- **"Toxicity of Silicon Compounds in Semiconductor Industries"**, *J. Occupational Health* 40(4):270 — https://academic.oup.com/joh/article/40/4/270/7270628
- **"Acute and subchronic inhalation toxicity of tetraethoxysilane (TEOS) in mice"**, *Archives of Toxicology* — https://link.springer.com/article/10.1007/s002040050069

> ### ⚠ SCOPE NOTE
> **This file describes a MATERIAL CLASS and a published toxicological MECHANISM, at the level found in
> occupational-safety training and poison-control references.** ***It contains no formulation, no
> concentrations, no preparation route, and nothing actionable*** — **and it should stay that way.** The
> worldbuilding needs to know *what siligel is and why it is lethal to humans*; it does not need, and should
> not acquire, anything further.
