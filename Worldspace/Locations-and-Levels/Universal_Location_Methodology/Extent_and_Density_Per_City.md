# EXTENT & DENSITY — PER-CITY WORKING FILE

**Opened 2026-09-05.** **Companion to `Extent_and_Area_APPROACH.md`** *(that file is the METHOD; this one is
the DATA and the per-city resolutions)*.

> ## ⭐⭐ WHAT THIS FILE IS
> **The first `Gate 11` run in the project's history, and the record of working each city out.**
> `04` Gate 11: ***"Divide the population by the area. That is the whole technique."*** — and on why it is
> trusted: ***"the part that fired was the part that was ARITHMETIC… it is the only part of this gate that
> does not run on the same faculty that produced the error."***
>
> ⛔ **Cities are worked ONE AT A TIME.** *Developer instruction, 2026-09-05.*
> ✅ **1 of 11 resolved — Port Lockroy, §4.** ⏳ **Next: Dumont d'Urville** *(§5)*.

---

# 1 · ⛔⛔ THE PREMISE THIS RUN CORRECTED

> **Developer, 2026-09-05, on where the eleven "island cap" figures came from:**
> ***"I just made a judgement call, without actually checking the amount of land area (and that was true
> about all of them), so now, there's a possibility that we might need to check again."***

**So the caps are NOT area-derived.** ⛔ **They cannot anchor extent work — they are prior guesses at the same
quantity, and calibrating extent against them is `Extent_and_Area_APPROACH.md` §1's forbidden move: derive
extent from density, and Gate 11 returns the assumption instead of checking it.**

## ⭐ THE DIRECTION OF INFERENCE, STATED ONCE
### **AREA first → DENSITY second → the CAP revised if it fails.** *Never the reverse.*

⚠ **And "island cap" is not a number.** *It is a label applied to eleven cities. **Only Palmer City's has a
documented figure — 364,000 combined** (`to-be-integrated/Population_Balancing_Math_Notes.md`).*

---

# 2 · ⭐⭐⭐ THE RESULT — Gate 11, eleven cities, 2026-09-05

**Population is Census I COMBINED** *(humans + robots — the peak load a site must physically hold)*.
**Area is the island's total area** — 🔬 *researched, sourced in §6* — **not its ice-free fraction, per the
standing correction that ICE IS BUILDABLE.**

| City | Island | Area km² | Population | **Density /km²** | Verdict |
|---|---|--:|--:|--:|---|
| ⛔⛔ **Port Lockroy** | **Goudier I.** | **0.024** | 128,887 | **5,370,292** | ***4.3× Kowloon Walled City*** |
| ⛔⛔ **Dumont d'Urville** | **Île des Pétrels** | **0.33** | 453,334 | **1,373,739** | ***above Kowloon*** |
| ⛔ **Sayowa** | **East Ongul I.** | **~1.5** | 225,376 | **150,251** | **3.3× Manila** |
| ✅ **Signy** | Signy I. | 19 | 188,694 | **9,931** | ⭐ plausible |
| ✅ **Marambio** | Seymour I. | ~78 | 570,269 | **7,311** | ⭐ plausible |
| ⚠ **Sejong** | King George I. | 1,150 | 644,833 | **561** | *nearly empty* |
| ⚠ **Juan Carlos** | Livingston I. | 798 | 386,692 | **485** | *nearly empty* |
| ⚠ **Fort McMurdo** | Ross I. | 2,460 | 445,310 | **181** | *rural* |
| ⚠ **Scott** | Ross I. *(shared)* | 2,460 | 386,011 | **157** | *rural* |
| ⚠ **Palmer City** | Anvers I. | 2,432 | 332,808 | **137** | *rural* |
| ⚠ **Rothera** | Adelaide I. | 4,663 | 317,449 | **68** | ***sparser than farmland*** |

**Reference points:** **Kowloon Walled City historical peak 1,255,000/km²** · **Manila, densest real city,
46,178/km²** · **Paris 20,000** · **Singapore 8,000**

> ## ⭐⭐⭐ THE FINDING — **THE LABEL FAILS IN BOTH DIRECTIONS AT ONCE**
> **The eleven islands span a 194,000-fold range in area** *(Goudier 0.024 km² → Adelaide 4,663 km²)* **and
> were given one shared label.** ***So "island cap" is not a cap: it is a name applied to a set with no shared
> numeric property.***
>
> ⛔ **Three are physically impossible.** ⚠ **Six are nearly empty** — *Fort McMurdo and Scott together put
> 831,321 people on Ross Island at **338/km²**, which is a county rather than a city.*
> ⭐ **Only Signy and Marambio land in a sane range, and only because their islands happen to be mid-sized.**
>
> ***The constraint binds the cities with room and lets the cities with none run to impossible figures.***

## ⭐ THE CALIBRATION THIS PRODUCES — **the first one derived from area rather than intuition**

> ### **The plausible band sits around 7,000 – 10,000 /km².**
> **Signy (9,931), Marambio (7,311) and Dumont d'Urville-on-its-archipelago (9,067) all land there
> independently, from three different island geometries.** ⭐ **That is a real anchor for
> `Extent_and_Area_APPROACH.md` §7's band widths — and unlike the caps, it is not circular.**

---

# 3 · ⚠ TWO SOFTENINGS, BEFORE ANY CITY IS REVISED

### ⭐ 3.1 Dumont d'Urville probably is not a failure — it has DENISON'S structure
**Île des Pétrels is 0.33 km², but the Géologie Archipelago it sits in extends over ~50 km².**
**453,334 / 50 = 9,067/km²** — ***squarely in the plausible band.***
⭐ **That is archipelago-spanning, the same form worked at Denison** *(`Extent_and_Area_APPROACH.md` §7b)*.
⚠ **Likely the intended reading. Confirm rather than revise.**

### ⛔ 3.2 Port Lockroy has NO such rescue — see §4

---

# 4 · ✅ PORT LOCKROY — **RESOLVED 2026-09-05.** *City #1 of 11.*

> ## ✅ DEVELOPER RULING
> ***"set the population of Port Lockroy to a randomly-generated value anywhere between 600 to 1,000 people.
> Whatever number has to be subtracted, mark that as an overflow to eventually be redistributed to another
> city (or possibly multiple other cities)."***
>
> ### ⭐ DRAWN: **929**

| | Was | **Now** |
|---|--:|--:|
| **Census I** | 63,338 H / 65,549 R / **128,887** | **457 H / 472 R / 929** |
| **Census II** | 53,703 H / 42,203 R / **95,906** | **387 H / 304 R / 691** |
| **Density on Goudier** *(0.024 km²)* | ⛔ **5,370,292/km²** — *4.3× Kowloon* | ⭐ **38,708/km²** — **0.84× Manila** |
| **Ground per person** | **0.2 m²** | **25.8 m²** |

⚠ **Method:** *human/robot ratio preserved; Census II scaled from the Census I figure with this city's own
retention rate intact (74.4109% → 74.3811%), per the standing convention that population adjustments preserve
source composition rather than reshaping it.*

## ⭐⭐ Why 929 works where 128,887 did not

**At 929 people Goudier supports a two-storey settlement covering most of the island with ~31 m² of floor
each** — *a comfortable apartment, no megastructure, no stacking, no engineering heroics.* **Which is what a
200 × 120 m rock in a sheltered harbor physically is.**

> ### ⭐⭐⭐ AND IT MAKES THE SPEC SELF-CONSISTENT FOR THE FIRST TIME
> **Every qualitative statement in `Specs/Port_Lockroy.md` already described something tiny** — *"a genuinely
> tiny island," "no room to decentralize," "no realistic underground vault potential," "no mountainous
> terrain," "Tepenia's second-smallest city."* ***Only the number disagreed.***

⚠ **Port Lockroy is now the smallest settlement in Tepenia**, below Amundsen Station's 6,857.
⭐ **And no spanning to Wiencke Island was needed** — *the option identified as the last remaining escape is
left unused, and remains available if the figure is ever revisited upward.*

## ⛔⛔ THE OVERFLOW — held, not deleted

| Census | Humans | Robots | **Combined** |
|---|--:|--:|--:|
| **I** | 62,881 | 65,077 | **127,958** |
| **II** | 53,316 | 41,899 | **95,215** |

📎 **Ledger: `Official_Population_Census.md` §D-OVERFLOW.** ⚠ **The Palmer subnet and national TOTAL rows are
deliberately short by these amounts until redistribution** — *recomputing them now would erase the record that
the population is owed somewhere.*

> ⛔⛔ **NOT AN EVENT.** ***Nobody left Port Lockroy.*** **A figure was corrected and the difference is parked.
> No receiving city gains a community, a memory, or an origin story from it.** *(The standing rule:
> the census is a record, and its editing history is not events.)*

## 📎 What this sets for the remaining ten

⭐ **Port Lockroy is the smallest island in the set, so it establishes the floor.** **At 0.024 km² supporting
929 people (38,708/km²), the same density logic gives rough ceilings elsewhere** — *e.g. **Sayowa** on East
Ongul's ~1.5 km², **62× the area**, lands near **58,000** against its current 225,376.*
⚠ **That is an ILLUSTRATION, not a rule.** ***Each city is still worked on its own site.***

---

# 5 · ⏸️ QUEUE — worked one at a time, in this order

| # | City | Why it is here |
|--:|---|---|
| ~~**1**~~ | ✅ **Port Lockroy** | ✅ **RESOLVED 2026-09-05 → 929** *(§4)*. Overflow **127,958 / 95,215** held |
| **2** | **Dumont d'Urville** | ⛔⛔ above Kowloon on its home island — ⭐ *but §3.1 likely resolves it* |
| **3** | **Sayowa** | ⛔ 150,251/km², and its own spec already flags 50,084/km² as *"the implausibility"* |
| **4** | **Rothera** | ⚠ **68/km² — the emptiest.** *The opposite failure, and it needs the same attention* |
| **5** | **Palmer City** | ⚠ 137/km² — ⭐ **and it is the ONE city with a documented cap (364,000)** |
| **6** | **Fort McMurdo + Scott** | ⚠ **worked together — they share Ross Island** *(338/km² combined)* |
| **7** | **Juan Carlos · Sejong** | ⚠ 485 and 561/km², both on large glaciated islands |
| **8** | **Signy · Marambio** | ✅ **plausible — confirm and use as the band anchor** |

⚠ **Denison is NOT in this queue** — *it is not island-capped, it was worked separately
(`Extent_and_Area_APPROACH.md` §7b), and its population is **flagged for reduction, deliberately held** until
these eleven give it something to calibrate against.*

⛔ **The other 26 cities are out of scope for this file so far.**

---

# 6 · 🔬 SOURCES — island areas, 2026-09-05

| Island | Area | Source |
|---|--:|---|
| **Adelaide I.** *(Rothera)* | **4,663 km²** | https://en.wikipedia.org/wiki/Adelaide_Island |
| **Ross I.** *(Fort McMurdo, Scott)* | **2,460 km²** | https://en.wikipedia.org/wiki/Ross_Island |
| **Anvers I.** *(Palmer City)* | **2,432 km²** | https://en.wikipedia.org/wiki/Anvers_Island |
| **King George I.** *(Sejong)* | **1,150 km²**, **<10% ice-free** | https://en.wikipedia.org/wiki/King_George_Island_(South_Shetland_Islands) |
| **Livingston I.** *(Juan Carlos)* | **798 km²** | https://en.wikipedia.org/wiki/Livingston_Island |
| **Seymour I.** *(Marambio)* | **~78 km²** — *21 km long, 3–8 km wide; with James Ross I. **the largest ice-free surface known in Antarctica*** | https://www.britannica.com/place/Seymour-Island-Weddell-Sea · https://en.wikipedia.org/wiki/Seymour_Island |
| **Signy I.** *(Signy)* | **19 km²**, much permanently ice-covered | https://en.wikipedia.org/wiki/Signy_Island |
| **East Ongul I.** *(Sayowa)* | **~1.5 km²** — *2 km long, ~1 km across* ⚠ *the spec says ~4–5 km², which may include West Ongul* | https://en.wikipedia.org/wiki/East_Ongul_Island |
| **Île des Pétrels** *(Dumont d'Urville)* | **0.33 km²**; **Géologie Archipelago ~50 km²** | https://en.wikipedia.org/wiki/Petrel_Island_(Antarctica) · https://en.wikipedia.org/wiki/G%C3%A9ologie_Archipelago |
| ⛔ **Goudier I.** *(Port Lockroy)* | **0.024 km² — 200 m × 120 m** | https://en.wikipedia.org/wiki/Goudier_Island |

⚠ **Areas are TOTAL island area, not ice-free area** — *per the standing developer correction that building
area is not restricted to ice-free ground.* **Where the ice-free fraction is known it is noted, because it
bears on the built-mode ruling even though it does not bound the extent.**
