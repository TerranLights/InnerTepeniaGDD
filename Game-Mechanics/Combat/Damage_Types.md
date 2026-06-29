# Damage Types

Inner Tepenia uses a "firm sci-fi" damage type system adapted from BG3's 13-type framework, translated into grounded physics/chemistry/engineering. Types drive resistances/vulnerabilities, build variety, and environmental hazards. They integrate with the DT/DR layered armor system, AP economy, MACHINE stats, and district themes.

**Design integration:**
- MACHINE stats modulate damage of specific types (Engine → thermal/energy endurance; Might → kinetic soak; Calculation → EMP/system optimization; Nerve/Humanity → neural/psychic effects)
- Anti-robot vs. anti-human specialization creates meaningful build diversity
- District environments naturally concentrate specific types — finding a type often means going to its district
- Power-grid story reactivity: destabilizing Aries increases Lightning/EMP/Plasma hazards city-wide

---

## Physical Damage Types (Kinetic/Impact)

The baseline of most conventional weapons. Dominant in grounded ballistics, projectiles, and melee.

**Bludgeoning** — Blunt force trauma, concussive impact, shockwaves. Strong vs. armored/plated targets and structures; DoT from internal bruising/crushing. In-world: hammers, mauls, explosive shockwaves, industrial presses (Capricorn), gravitic impacts.

**Piercing** — Penetrating trauma from projectiles or pointed implements. High damage vs. unarmored targets; AP ammo synergy. In-world: needles, AP rounds, railgun darts, monofilament, undergrid maintenance tools (Virgo).

**Slashing** — Shearing/cutting trauma. Good vs. unarmored targets, can target joints and exposed components on robots. Less dominant due to advanced armor prevalence. In-world: blades, monowire, industrial saws, high-velocity fragments.

---

## Elemental / Energy Damage Types

More exotic or environmental. Strong thematic ties to tech, industry, and Antarctic conditions.

**Acid (Corrosive/Chemical)** — Material dissolution or chemical burns. Strong DoT; armor degradation over time (bypasses some DT). In-world: industrial chemicals/solvents (Capricorn), battery leaks, bioweapon residues, black market weapons (Pisces).

**Cold (Cryogenic/Thermal-Low)** — Freezing, embrittlement, hypothermia equivalent. Slows movement/AP; embrittles armor (increased vulnerability to kinetic follow-up). In-world: cryo weapons, Antarctic exposure (Sagittarius Frostlands), power grid cooling system failures.

**Fire / Thermal (Heat/Combustion)** — Burning, heat transfer. DoT, panic, forced movement. Interpreted as high-energy thermal discharge rather than open flame. In-world: plasma torches, contained plasma (Aries power core), laser thermal effects, geothermal vents, incendiary munitions.

**Force (Kinetic/Concussive)** — Raw energy dump, often shockwave-like. Reliable baseline damage; good for knockback and structure destruction. In-world: explosives, mass drivers, railgun impacts, gravitic/acceleration weapons.

**Lightning (Electrical/Electromagnetic Current)** — Current flow, arcing, system overload. Chain effects on conductive targets; stun/DoT. In-world: tasers, high-voltage arcs, railgun rails, cyberware feedback, power surges (Aries grid).

**Necrotic (Biological Decay / Entropy Acceleration)** — Tissue/system degradation. Strong DoT or max HP reduction; reinterpreted as molecular disassembly or accelerated cellular entropy rather than supernatural "life drain." In-world: engineered pathogens, radiation-induced necrosis, targeted nanites (Scorpio district flavor, industrial contaminants).

**Poison (Toxic/Chemical/Biological Agents)** — Systemic toxicity. DoT with varied effects: paralysis, organ damage. In-world: industrial toxins, bioweapons, siligel contaminants, black market chems (Pisces). Less effective vs. sealed robots unless delivered via nanites.

**Psychic / Neural (Cognitive/Interface Disruption)** — Mental or neural overload. Affects Nerve/Humanity/Calculation stats; causes confusion or control loss. Reinterpreted as electromagnetic or chemical neural attack, sensory overload, or interface hacks. In-world: neural disruptors, sonic infrasound (Cymaticist tie-in), interface hacks, hallucinogenic agents.

**Radiant (Electromagnetic Radiation / Coherent Energy)** — High-energy photons or particle effects; ionization or thermal excitation. Precision damage; good vs. specific materials. In-world: laser weapons, reactor leaks, high-energy particle beams (Aquarius). Not "holy light."

**Thunder (Sonic/Acoustic Pressure)** — Pressure waves from sound or explosions. AoE, disorientation, structural damage. In-world: sonic weapons, explosive shockwaves, infrasound (disruption without lethality), industrial vibration (Cymaticist faction synergy, Virgo maintenance).

---

## Additional Sci-Fi Damage Types

Filling gaps for Inner Tepenia's specific setting beyond the BG3 baseline.

**Radiation (Ionizing)** — Alpha/beta/gamma/neutron exposure causing cellular/DNA damage. Delayed DoT plus long-term debuffs rather than instant damage. Distinct from Radiant (more penetrating/biological). In-world: post-war contamination zones, Aries power infrastructure leaks.

**EMP / Disrupt (Electromagnetic Pulse/Interference)** — High-intensity EM fields disrupting electronics without primary thermal/kinetic damage. Stuns/disables robots and cyberware; area denial. Strong anti-tech tool; pairs with Lightning but more systemic. In-world: hacking-adjacent or grid-related builds.

**Plasma (Ionized Matter)** — Superheated ionized gas combined with electrical effects. High damage plus secondary effects (burn + arc). Distinct from Fire (more exotic, containment issues) and Lightning (more localized). In-world: advanced weapons, containment breaches in power/experimental districts.

**Nanotech / Molecular Disassembly** — Targeted or self-replicating nanites breaking molecular bonds. Armor-ignoring DoT or precision destruction; bypasses some DT. In-world: Aquarius experimental labs, industrial nanites, advanced black market applications.

**Gravitic / Inertial (Acceleration/Tidal Forces)** — Extreme G-forces or manipulated acceleration and gravity. Knockback, crushing, disorientation; good for heavy weapons or environmental hazards. *Implementation TBD — designated as possible rather than confirmed.*

**Neural / Interface (System Attack)** — Direct attack on neural implants or robot control systems. Feedback loops, OS corruption, control loss, error states. Synergizes with Investigation (hacking) and Calculation. Refined variant of Psychic/Neural specifically targeting machine systems.

---

## Specialization Summary

### Anti-Robot (Strong vs. Machines, Electronics, Chassis)

These exploit electronics, conductive materials, logic/control systems, and physical structure.

| Type | Primary Effect |
|------|---------------|
| EMP / Disrupt | Primary hard counter; fries circuits, disables/stuns robots |
| Lightning | Overloads systems, arcing feedback into power sources |
| Acid (Corrosive) | Degrades metal, plastics, chassis over time |
| Radiation | Damages sensors, memory/storage, electronics |
| Plasma | Melts and disrupts contained systems and materials |
| Neural / Interface | Hacks or overloads robot OS, causes control loss |
| Cold (Cryogenic) | Embrittles metal, increases kinetic follow-up damage |
| Slashing | Targets joints, wiring, cabling, exposed components |

*Robots typically resist or ignore Poison and classical biological Necrotic unless delivered via nanites or specialized carriers.*

### Anti-Human (Strong vs. Organic Tissue, Biology, Psychology)

These exploit biology, cells, nerves, psychology, and soft tissue.

| Type | Primary Effect |
|------|---------------|
| Poison (Toxic/Biological) | Systemic toxicity; organ/nerve/blood damage |
| Necrotic (Biological Decay) | Cell death, tissue necrosis, molecular degradation |
| Radiation | Cellular/DNA damage, acute or long-term effects |
| Psychic / Neural | Nerve overload, disorientation, psychological disruption |
| Fire / Thermal | Burns to flesh and organic material |
| Acid (Corrosive) | Chemical burns and tissue dissolution |
| Bludgeoning | Crushes bones, organs, soft tissue |
| Thunder (Sonic) | Acoustic pressure waves, internal trauma |

*Humans are largely resistant to pure EMP/Disrupt unless heavily cyber-augmented.*

### Shared / Versatile (Effective Against Both)

| Type | Notes |
|------|-------|
| Force (Kinetic/Concussive) | Universal blunt trauma or shockwave damage |
| Piercing | Good penetration against both armor and flesh |
| Radiant (Laser/Coherent Energy) | Precision thermal/ionization; different secondary effects per target |
| Gravitic / Inertial | Crushing forces affect structures and bodies alike (if implemented) |

*Cold and Fire/Thermal also have crossover potential in extreme environments.*

---

## District Availability

Where each damage type is most commonly found, acquired, or encountered.

### Anti-Robot Types

| Type | Primary Districts |
|------|------------------|
| EMP / Disrupt | Aquarius, Gemini, Aries, Virgo |
| Lightning | Aries, Capricorn, Aquarius, Gemini |
| Acid (Corrosive) | Capricorn, Pisces, Virgo, Aquarius |
| Radiation | Aries, Aquarius, Capricorn, Scorpio |
| Plasma | Aries, Aquarius, Capricorn |
| Neural / Interface | Gemini, Aquarius, Scorpio, Pisces |
| Cold (Cryogenic) | Sagittarius, Virgo, Aquarius, Aries |
| Slashing | Capricorn, Pisces, Virgo, Leo |

### Anti-Human Types

| Type | Primary Districts |
|------|------------------|
| Poison (Toxic/Biological) | Pisces, Capricorn, Scorpio, Cancer |
| Necrotic (Biological Decay) | Scorpio, Pisces, Capricorn, Virgo |
| Psychic / Neural | Scorpio, Gemini, Aquarius, Leo |
| Fire / Thermal | Aries, Capricorn, Pisces, Leo |
| Bludgeoning | Taurus, Leo, Capricorn, Sagittarius |
| Thunder (Sonic) | Leo, Scorpio, Virgo, Aquarius |

### Shared Types

| Type | Primary Districts |
|------|------------------|
| Force (Kinetic/Concussive) | Aries, Capricorn, Sagittarius, Taurus |
| Piercing | Aries, Pisces, Capricorn, Sagittarius |
| Radiant (Laser/Coherent Energy) | Aquarius, Aries, Gemini, Capricorn |
| Radiation | Aries, Aquarius, Capricorn, Scorpio |
| Gravitic / Inertial | Aquarius, Aries, Capricorn |

---

## Balance Notes

- Many types carry secondary effects (stun, armor degradation, DoT, movement penalties) that enhance their thematic strength beyond raw damage numbers
- District environments and power-grid choices amplify availability: destabilizing Aries increases Lightning/EMP/Radiation risks city-wide; favoring Aquarius floods the market with experimental gear
- District armor augments provide player customization for specific resistances: industrial plating (Capricorn) strong vs. Acid/Corrosive; experimental dispersion (Aquarius) vs. Radiation/EMP
- Mixed robot-and-human enemy groups reward adaptability; pure specialization works best in district-specific content
