# Handwave register

**Created 2026-10-06. Developer-ruled.** See `02_Design_Brief.md` §8 for the rule. An entry covers its own mechanism
only. Anything not on this list obeys known physics.

| # | Handwave | What is waved | What is NOT waved | Source |
|--:|---|---|---|---|
| H-1 | **Nanotech gel brains** | How a malleable gel brain gives a robot full, complete consciousness and sentience | The body. A robot is human-shaped and has mass, heat, charge, joints and a radiation tolerance. She cannot fly, survive vacuum without preparation beyond what canon grants, or ignore thermal balance. | Developer, 2026-10-06. Canon: `Robot_Physiology_and_Cultural_Practices.md` ("a malleable, ever-changing gel brain"). |

## Developer rulings that shape the physics (not handwaves)

| # | Ruling | Date | Effect |
|--:|---|---|---|
| RL-1 | **Robots are radiation-vulnerable, equivalently to humans for shielding purposes, "for different reasons".** A robot doing an EVA would still wear a suit, **for radiation protection, not for oxygen**. Even the earliest robot-only station must therefore be **radiation-shielded to the degree a human requires.** Developer's words: "probably safe to say"; recorded as a ruling unless corrected. | 2026-10-11 | Answers C-32 (a robot is **not** radiation-immune). Largely answers C-5: the body's electronics sit inside the same shielding. **Its basis is the gel brain**, whose tolerance is unspecified in canon: electronics alone would tolerate much more than a human (see `classes/01_Robot-Only_Staging_Station.md` §4). It sets the dose budget for every class with robot residents. **Open:** the numeric dose budget (what "the degree a human requires" is, per orbit and dwell time), and how much radiation protection a suit actually gives (not yet researched). |

**Candidate handwaves** (proposed by a class or a research file, not yet accepted). Each needs a developer ruling.

Each is tagged **bend** (physics would have to give if the scene is shown as imagined) or **cost** (physics holds, but a
mechanism, mass, power or duty cycle must be accepted and shown). Source: `research/robot_body_in_space.md` §7 (2026-10-11).
**None is accepted.** The research file's numbered sources and derived figures (D-/S- numbers) are cited there.

| # | Candidate | Tag | What the fiction would have to settle |
|--:|---|---|---|
| C-1 | **Rejecting a full day's body heat through human-sized skin in vacuum** at a body temperature that skin and clothing survive | bend as imagined; cost with a mechanism | A heavy-work body in sunlight needs a heat-rejection mechanism beyond skin radiation (an expendable-fluid sublimator, a deployable radiator) or a duty cycle that rests it in shade. A "walks in vacuum all day in sunlight" scene needs an explicit mechanism. |
| C-2 | **Surviving a lunar or Mars night without a heat source** | cost | A bare body cannot do it on a battery. It needs a blanket-grade insulating layer under realistic clothing, or a radioisotope or reactor heat source. Realistic skin rated only to about -45 °C is outside its range for the night. |
| C-3 | **Realistic polymer skin and fabric that is also vacuum-safe** | cost | Ordinary skin-grade silicone and clothing fabric are not shown to meet outgassing and flammability screening without selection. A materials choice the fiction must make (space-grade silicone skin; fabrics like Nomex). |
| C-4 | **A body that works for years without servicing joints** | bend | Fluid-lubricated precision gears wore out in tens of hours of walking duty under assumed conditions, and even long-lived space robots are repaired by swapping parts. A fiction with routine part replacement does not bend this. |
| C-5 | **Radiation-hard body control electronics at human scale with commercial-grade performance** | bend | The gel brain (H-1) is waved. Motor control, sensors and power conditioning are electronics. Surviving repeated trapped-belt crossings without heavy shielding and without rad-hard performance penalties would bend the shielding-mass and hardened-part-speed bounds. |
| C-6 | **Recharging from a distance without large apertures or heating** | bend | Wireless power at meter range needs body-size coils and dissipates most energy as heat. Microwave power at tens of meters needs square-meter apertures. A robot that "plugs into the air" at long distance would bend this. |
| C-7 | **Charging a Li-ion pack outdoors in the cold** | cost | Charging below about -10 °C damages cells. Outdoor charging at Antarctic temperatures needs a warmed pack or another chemistry; none is flight-proven in the sources found. |
| C-8 | **Clothing that is cloth-like in air and insulating in vacuum** | cost | Cosmetic clothing gives no insulation in vacuum. Insulating clothing must be vacuum-grade multilayer insulation, which behaves like a stagnant gas pocket in air. |

**From `research/moon_lagrange_and_comparables.md` §7 (2026-10-11).** Proposals only; none accepted. The agent notes most of these
are engineering extrapolations, not violations of physics.

| # | Candidate | Tag | What the fiction would have to settle |
|--:|---|---|---|
| C-9 | **A permanently inhabited lunar or Lagrange-point structure with no resupply** | cost (exceeds every observed record) | Every closed-habitat comparable has resupply, make-up gas or spares. The ISS spares-to-system-mass ratio is 7.1 for one subsystem over 1,200 days. A habitat needing no spares for years needs reliability far beyond any record. |
| C-10 | **A mass driver feeding an L5 habitat as a normal industry** | cost (undemonstrated) | No mass driver beyond a table-top prototype exists. SP-413's catcher, track tolerance and launch accuracy are paper values. A nearside driver's payloads do not arrive at L2 at near-zero velocity, so a catcher must absorb momentum. |
| C-11 | **Regolith as a free building material and oxygen source** | bend if "free" | Oxygen is 30–45 wt% of minerals but costs 63–126 MJ/kg and 38 t of ilmenite soil per metric ton. Needs the energy-and-mass budget. |
| C-12 | **Helium-3 as an economic export** | bend | At 4–20 ppb, and with fusion not demonstrated, Crawford finds the claims exaggerated. |
| C-13 | **Large lunar volumes at comfort without shielding mass** | cost | Measured dose behind 1 g/cm² is 2.6 times the ISS. Kilometer-scale lava-tube settlement is plausible only if tube shielding is verified, and the evidence is thin. |
| C-14 | **A propellant-free "parking spot" at L1, L2 or L3** | bend | Those points are unstable; only L4/L5 are stable, and only in particular orbits. |
| C-15 | **Lunar-night energy at the equator without nuclear or stored energy** | cost | About 355 hours of darkness. Polar near-continuous-light cases were not researched. |

**From `research/life_support_lowg_power_structures.md` §7 (2026-10-11).** Proposals only; none accepted.

| # | Candidate | Tag | What the fiction would have to settle |
|--:|---|---|---|
| C-16 | **Closed ecology at a few square meters of crops per person** | bend | Theoretical minimum 3–5 m² per person needs 1,000 µmol/m²/s, perfect absorption and 3.6 kW of electricity per person. The best measured wheat yield needed 30 m² and 15 kW per person. Lunar Palace needed 30 m² for 73% of food mass; Biosphere 2 needed 250 m². |
| C-17 | **Loops closed to 100% for years** | bend | The ISS recovers 98% of water (with a repeatedly repaired demonstration unit) and 50% of oxygen from CO₂. Lunar Palace reached 98.2% material closure for 370 days with solids only 67% closed. Design leakage is 0.05–0.14% of the atmosphere per day. |
| C-18 | **Children gestated, born and raised in low gravity or spin** | bend (untested) | Never tested in any mammal for a full gestation, never in a human. Normal development is an assumption. **Check against canon on artificial wombs (see the Demographics memory entry); I have not read that file, so the interaction is unverified.** |
| C-19 | **Partial gravity as a cure-all** | bend | The only orbital partial-g evidence is 35-day mouse studies at 1/6 g and 1 g, where 1/6 g kept muscle mass but not fiber type. A settlement at 0.1–0.4 g that needs no exercise is unsupported. |
| C-20 | **Spin radii of kilometers with ordinary shell materials** | cost | A 3.2 km, 1 g cylinder with 4.5 t/m² contents needs about 5.6 t/m² of 4340-class steel. A 16 km cylinder passes the stress check only with a rotating shell on near-frictionless bearings against a fixed structure, which no source shows. |
| C-21 | **Free electrical power per person at O'Neill's 120 kW** | cost | At ISS array performance (64 W/m²) that is about 1,900 m² of collector per person, plus the same heat to radiate. Real habitats read use 5–15 kW per person. |
| C-22 | **Printed or sintered regolith as the pressure shell** | bend | Measured strengths are 5–22 MPa for small pieces. A pressurized shell needs a continuous membrane in tension. The ESA design uses an inflatable inside the printed shell. |
| C-23 | **Regolith shielding that is cheap** | cost | Moving and holding hundreds to thousands of kg/m² needs machines, power and time. No source gives a placement rate. |
| C-24 | **Dust-free interiors** | bend | Apollo dust disabled suit bearings in three days and entered the cabin. Layered defenses reduce it and are not shown to eliminate it. |
| C-25 | **A radiator-free or low-temperature heat sink** | bend (Stefan-Boltzmann) | A 300 K surface radiates at most 459 W/m² per face. Moving tens of kilowatts per person without large or hot radiators breaks the law. |
| C-26 | **Zero-reaction-mass spin-up or despin** | bend | Angular momentum must go somewhere: reaction mass, a counter-rotating mass, a tether exchange or the planet's magnetic field. |

**From `research/gap_retry_mars_venus_jupiter.md` §7 (2026-10-11).** Proposals only; none accepted.

| # | Candidate | Tag | What the fiction would have to settle |
|--:|---|---|---|
| C-27 | **Intact, large, safe Martian lava tubes** | assumption | No tube has been seen from inside, no roof thickness is measured, and SHARAD has not detected one. A tube settlement needs the tubes to exist at the assumed width, to stay up under unmeasured stresses, and to be reachable. |
| C-28 | **A 1 atm, 20 °C floating habitat on Venus** | bend | The two numbers sit at different altitudes: 1 bar at about 50 km is about 70 °C; 20 °C at about 56 km is about 0.5 bar. A habitat at either needs a pressure or temperature difference. Landis's large-envelope lift tonnages are unverified. |
| C-29 | **Terraforming Venus or Mars in a plausible time** | bend | Venus needs about 2.5×10²⁸ J (Landis 2011). Mars lacks the CO₂ inventory (Jakosky and Edwards). A terraformed planet needs an energy source or inventory physics does not provide. |
| C-30 | **Rapid unshielded travel to Jupiter's moons** | bend | The dose numbers require mass shielding in g/cm² that scales with stay length. Stays near Europa are dose-limited; Callisto's orbit lies outside the main belts. |
| C-31 | **Mars gravity as good as Earth's for a lifetime** | unknown | No human or large-animal data at 0.38 g exist. |
| C-32 | **A robot body immune to radiation** | bend | Electronics fail in total-dose terms (50–300 krad(Si) design values), well below the Europa lander's unshielded 1.7 Mrad(Si). Same limit as C-5. |

**From `research/waste_heat_utilization.md` §7 (2026-10-11).** These are **claims a fiction might make about reusing heat, which the research does
not support as stated.** None is accepted. Each says what would have to be true. (Origin: the developer's question of whether a station could reuse
the heat it must reject.)

| # | Claim | Tag | What the research says |
|--:|---|---|---|
| C-33 | **A station runs its machines on its own waste heat** | bend | Room-temperature heat has a Carnot factor of only 5–25 % against realistic radiators; real devices convert about 1–12 %; the engine's own radiator is more than twice the area of simply radiating the heat. Needs a hot source (reactor, concentrated solar) or an accepted loss. |
| C-34 | **Endothermic chemistry cools the station** | cost | Only if the product is exported or stored out of the station; otherwise the heat returns when the product is used. The ISS electrolyzer releases about 66 % of its input as heat. |
| C-35 | **Thermochemical splitting or solid-oxide electrolysis on loop waste heat** | bend (forbidden by temperature) | Needs 800–950 °C. |
| C-36 | **Regolith ISRU on waste heat** | bend | The reactions run at 900–1,900 °C; at most about 4 % of an ilmenite plant's energy could come from a source below 100 °C. |
| C-37 | **A heat pump removes the radiator problem** | bend | It cuts the radiator by a factor of at most 0.4–0.9 for the temperatures studied, adds up to 1.2 kW of heat per kW lifted; a lab heat pump with a 70 K lift gave a COP of 0.1–0.6. |
| C-38 | **Phase-change walls or tanks store a lunar night cheaply** | cost | At system-level 48.8 kJ/kg the mass is about 26 t per kW over 354 h. |
| C-39 | **Robots shed their heat into the station loop for reuse** | cost | The heat can be collected by cold plates, but it is below about 90 °C, mostly below 60 °C, tens to hundreds of watts per body; useful only for the low-grade uses (distillation, drying, melting ice). |
| C-40 | **Absorption refrigeration or membrane distillation on 40–60 °C heat** | unverified | No opened primary source. |
| C-41 | **Venting hot gas to dump process heat** | bend | Venting mass loses the closed-loop inventory; radiation is the only heat exit that keeps mass. |

**Cross-reference.** C-1 and C-25 (shedding heat in vacuum) stand: the research confirms that every watt a settlement uses becomes a watt it must radiate,
and that waste-heat reuse **does not remove the radiator**.

**Note.** C-3, C-7 and C-8 bear directly on canon you have already ruled: robots wear clothing and coats and gloves, and have
realistic skin where interaction happens. They do not contradict it. They say the fiction must pick a mechanism, such as
a warmed pack or space-grade skin, for the clothed robot to be physical.

**Already settled by canon, listed so nobody re-asks:** robots are vacuum-capable and have no respiratory system
(`RP`; see the runbook's §C.10 table). Whether that holds under radiation, thermal extremes and microgravity is a
**physics question this library must answer from sources.** It is not itself a handwave.
