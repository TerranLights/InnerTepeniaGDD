# Hacking and Traceability System

**Design inspiration**: Cyberpunk 2077 access points / quickhacking — adapted for Inner Tepenia's turn-based, stat-governed structure. Unlike CP2077, Inner Tepenia adds a persistent **traceability** layer: hacking is never consequence-free by default, and becoming truly untraceable requires serious investment.

---

## Hackable Target Types

The world contains a variety of hackable entities, each with their own security level and consequence profile.

| Target Type | Examples | Security Profile |
|-------------|----------|-----------------|
| **Open nodes** | Public terminals, civilian info kiosks | Level 0 — no gate, low stakes |
| **Antennas** | Broadcast towers, relay dishes | Level 1 — low gate, city-wide reach |
| **Access points** | Local network hubs, building entry nodes | Level 1–2 — moderate gate |
| **Terminals** | District admin, faction offices, shops | Level 2–3 — variable by location |
| **Closed networks** | Faction intranets, private systems | Level 3–4 — moderate–high gate |
| **Arcanet nodes** | Arcanet backbone infrastructure | Level 3–5 — variable, can be critical |
| **Security systems** | Cameras, locks, alarms, automated turrets | Level 2–4 — responds to breach immediately |
| **Critical infrastructure** | Power grid control, life support, Calethina's systems | Level 5–6 — extreme gate, major consequences |

---

## Access Requirements — The OR Gate

Hack targets are **half-gated**: the player needs to meet **either** a Calculation stat threshold **or** an Arcanet Navigation & Hacking skill threshold (or both). Meeting one is enough to attempt. Meeting neither means the interface doesn't respond — the system is simply beyond the player character's current capability to read.

**Example threshold pairs:**

| Security Level | Calculation (OR) | Hacking Skill (OR) | Notes |
|---------------|-----------------|-------------------|-------|
| Level 0 | — | — | Open to everyone |
| Level 1 | C 2 | Hacking 15 | Basic civilian systems |
| Level 2 | C 4 | Hacking 30 | Standard commercial / low-faction |
| Level 3 | C 5 | Hacking 50 | Enhanced / restricted civilian |
| Level 4 | C 7 | Hacking 75 | Hardened faction / military-adjacent |
| Level 5 | C 8 | Hacking 90 | Military / high-value infrastructure |
| Level 6 | C 9 | Hacking 100 | Critical city infrastructure — may require additional perks or quest access |

**Meeting both thresholds** (stat AND skill) unlocks additional options within the hack: deeper access, more actions available, faster completion, or the ability to leave secondary payloads.

---

## Traceability — The Default State

**All hacks are traceable by default.** This is a hard design rule, not a starting assumption to be revised.

When a hack is performed, the target system logs a record. How quickly that record is read and acted upon depends on:
- The security level of the system (higher = faster response)
- Whether anyone is actively monitoring the target
- The player character's skill level (higher Hacking skill = subtler signature)
- The type of action performed (passive data read vs. active manipulation vs. sabotage)

**Traceability consequences** (scaled by severity):
- Local NPCs may become suspicious or hostile
- Faction reputation may take a hit (the faction whose system was breached)
- Security level of the area increases for a period
- Enemies or guards may be alerted
- For high-level systems: city-wide alerts, faction bounties, or permanent reputation damage

**Passive vs. active hacking:**
- *Passive* (reading data, listening to traffic) generates a lighter trace than *active* (manipulating systems, planting code, disrupting operations).
- Even passive hacks on sensitive systems can trigger consequences if the system is being actively monitored.

---

## Traceability Reduction — Progression

The path from "always caught" to "truly invisible" requires deliberate investment.

| Stage | Means | Effect |
|-------|-------|--------|
| **Default** | No investment | All hacks traceable; consequence probability based on skill vs. system level |
| **High Hacking skill** | Arcanet Navigation & Hacking 60–75 | Reduced trace signature; passive hacks on Level 1–2 systems may not register |
| **Data Ghost perk** | C 7, Hacking 55 | Trace risk significantly reduced; passive hacks on Level 1–2 systems have high chance of no trace; active hacks still leave a signature |
| **Ghost in the Machine perk** | Level 24+, C 7, Hacking 90 | **Completely untraceable** on all Level 0–3 systems (C ≤5 / Hacking ≤50 requirement); see perk details below |
| **High-level targets** | Level 4–6 systems | Even Ghost in the Machine does not cover these; they remain traceable without additional future perks or questline access |

---

## Ghost in the Machine — Perk Reference

*Full entry in `Regular_Perks_-_Level-Up.md`.*

- **Prerequisites**: Level 24+, Calculation 7+, Arcanet Navigation & Hacking 90+
- **Effect**: Any hack on a system with a Calculation requirement of 5 or below **OR** a Hacking skill requirement of 50 or below is completely untraceable — no log entry, no signature, no consequence.
- **Scope**: Covers all Level 0–3 systems. Level 4–6 systems (C 7+ / Hacking 75+ requirement) remain traceable.
- **Design intent**: Makes a dedicated master hacker effectively invisible to most of the city's civilian and low-faction infrastructure. High-security targets — military systems, faction command networks, critical grid infrastructure — remain risky even at peak capability.

---

## Design Notes

- Traceability creates a consistent reason to care about Calculation and Hacking investment even outside of "can I access this at all" gating. A low-skill character who brute-forces their way into a system will still leave evidence behind.
- The OR gate (stat OR skill) means two distinct build paths are both valid: a high-Calculation character with moderate Hacking, and a moderate-Calculation character who has deeply invested in the Hacking skill. Both can reach the same systems, but through different routes.
- This system pairs naturally with the Stealth & Infiltration skill and Nerve (psychological composure under surveillance). A full infiltration build might combine hacking untraceability with physical stealth to move through the world entirely off the grid.
- Specific hack actions (what you can *do* once inside a system) are content and quest design territory — this document covers access and traceability only.
