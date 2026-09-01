# Census Basis — RULED: **CENSUS I** — 2026-09-01

> ## ✅ DEVELOPER RULING. `[CGRM 2026-09-01 · Path 6 · developer ruling]`
>
> *"We should begin with Census I, because Census II is post-orbital numbers."*
>
> *"Census I is the benchmark number set, because **we need to know that the various cities can actually house
> their peak numbers**, and then, post-orbital expedition, the cities would become less populated (which will
> render the cities **'emptier' than their earlier peak numbers**)."*
>
> ### **Files 03, 04 and 05 were computed on Census I and are CORRECT as written. No recomputation needed.**

## ⭐ The reasoning is the important part: Census I is a CAPACITY constraint, not just a bigger number

**A city must be built to house its peak.** Extent, housing, domes, water plant, heat, sanitation — **every
one is sized to the largest population the city ever held**, and none of it shrinks afterward.

> ## **Build for peak, then depopulate.**
> **Census I = what the city was BUILT FOR.** **Census II = who was still in it.** The infrastructure does not
> follow the people up the Tower.

**So the sizing test is: can the site physically hold Census I?** If yes, the city works — and every later,
smaller figure fits inside that answer automatically.

---

# 1. What the investigation was, and what it found

**A density figure would not reconcile:** CGRM-009 records Lazar at **53,058/km²** in the 34 km² Schirmacher
Oasis, but Census I gives **2,620,319 ÷ 34 = 77,068/km²**. The investigation traced the gap to its cause.

**Tepenia has two pre-war censuses, both inside the Second Interwar Period:**

| | **Census I** ✅ | Census II |
|---|---|---|
| Era | **Pre-Orbital** (2564 → ~2688) | Orbital (~2688 → 2812) |
| Taken | early Federation | *"immediately before the Long Night War"* |
| Surface humans | **15,623,523** | 10,486,701 |
| Surface robots | **16,403,077** | 11,434,935 |
| Surface total | **32,026,600** | 21,921,636 |

**The difference is neither birth nor death.** The census states it outright: ***"Population is conserved
between Census I and Census II — nobody was born or died in the transition; they relocated."*** **Decades of
orbital migration via Amundsen Tower moved ~38.8% of humans and ~36.2% of robots off-surface.**

## The ruling, and why it is the right one

> **Census II is a DEPLETED surface population** — the count remaining after a third of the country went up
> the Tower. **The Division of Industry describes these cities as full, working places, so it uses the fuller
> figure.** Census I is the Federation at its populated extent; Census II is what was left on the ground.

---

# 2. ⚠ Consequence: do NOT use 53,058/km² as a density ceiling

**CGRM-009's density work — and the extent table deposited in `Specs/Cape_Adare.md` — are computed on
Census II.** *(That table's own header reads "| City | Ice-free terrain | km² | **Census II** | People per
km² |".)* **On the Census I basis this pass now uses, every one of those density figures is roughly 1.45×
higher.**

| | Census II *(CGRM-009 basis)* | **Census I *(this pass's basis)*** |
|---|--:|--:|
| **Lazar** — Tepenia's densest, 34 km² | 53,058/km² | **77,068/km²** |
| **Tri-Cities** — 40 km² | 65,333/km² | **88,177/km²** |

**⚠ Minor inconsistency to be aware of, not to relitigate here:** a city's *extent* does not change between
censuses — only its population does — so Cape Adare's deposited ~20–40 km² range remains valid. **But its
stated densities, and any comparison drawn against them, are Census II figures.** **Flagged so the two bases
are never mixed in one calculation again, which is exactly the error this investigation started from.**

*(Related, same class: Cape Adare's §15 Division of Industry correction cites a population of `1,050,051` —
its Census II figure. Whether existing §15 prose should be restated on the Census I basis is a separate
question, not raised here.)*

---

# 3. The density question, answered on the Census I basis

**Lazar at 77,068/km² and the Tri-Cities at 88,177/km² are roughly 2.7× and 3.1× Manhattan (~28,000/km²), and
1.7× and 1.9× Manila (~46,000/km², the densest real city proper).**

**They are high, but they are not absurd** — because **Tepenian cities are enclosed and vertical in a way real
cities are not.** `City_Logistics.md` establishes for Concordia that *"many districts have multiple levels:
upper dome levels, ground level, and Undergrid levels below,"* with the Undergrid carrying transit,
maintenance, storage **and habitation.**

| | Footprint density | **Per level, at 5 effective levels** | Real-world equivalent |
|---|--:|--:|---|
| **Lazar** *(34 km²)* | 77,068/km² | **~15,400/km²** | ≈ Paris (~20,000) |
| **Tri-Cities** *(40 km²)* | 88,177/km² | **~17,600/km²** | ≈ Paris |

> ## ✅ **The oases CAN house their Census I peaks without expanding at all.** Footprint density and living
> density are not the same number in a multi-level enclosed city, and per-level the figures are ordinary.

**Ice-founded expansion therefore becomes a design CHOICE rather than a repair** *(`05` §3)*. It is still
worth taking, because it buys comfort at the peak and produces the **rock-core / ice-periphery status
gradient** — but the cities are viable either way, and **nothing was ever broken.**

---

# 3.5 ⭐ The consequence the ruling creates: every Tepenian city ends up a third empty

**Follow "build for peak, then depopulate" forward.** Infrastructure sized for Census I; **38.8% of humans and
36.2% of robots then leave up the Tower.** Nothing is demolished. So by the eve of the Long Night War:

> ## **Every city in Tepenia is carrying roughly a third more built volume than it has people to fill.**

**Nationally that is 10.1 million people's worth of housing, corridor, dome and services standing empty** —
before the war does anything at all.

**Three consequences worth taking further:**

1. **⭐ Sealed districts inside living cities.** Empty volume in Antarctica is not neutral — **you either keep
   heating it or you shut it off.** Both are decisions with costs, and shutting it off produces **explorable,
   abandoned, *interior* space inside cities that are still inhabited.** That is a level-design asset the
   setting gets for free, and it is quite different from war ruins: **nothing violent happened there. Everyone
   just left.**
2. **⚠ It raises the baseline civic load per capita — a real effect on this model.** Peak-sized domes, pipes,
   heat and structure must be maintained by a workforce reduced by ~37%. **The same burden, fewer shoulders.**
   So a Census II §15 would show a *higher* baseline percentage than the Census I §15 this pass is computing —
   **not because the city got harder to run, but because it kept its whole body and lost a third of its
   muscle.** *(Not modeled here; flagged as a real, derivable follow-on.)*
3. **A visible national mood.** A country that can see, in dark windows and closed corridors, that a third of
   itself went somewhere else — **and could not follow.** *(Interacts with the orbital-infrastructure work in
   the Governing Priority Sequence's Stage 3.)*

---

# 4. ⭐ A real gap this investigation uncovered, independent of the ruling

**Census II has 33 city rows. Census I has 37. Four cities have no Orbital Era figures at all:**

> ## **Byrd · Vostok · Kunlun · Dome Fuji**

*(Kunlun and Dome Fuji were added to Census I on 2026-07-04 and evidently never propagated; Byrd's and
Vostok's absence is unexplained.)*

**This does not affect the Division of Industry pass**, which now uses Census I throughout. **But it is a
genuine hole in the census** and it will bite anything that reads Census II — including the already-deposited
Cape Adare extent work, which compares against a set missing four cities.

**A canon-sanctioned fix already exists:** Concordia had this exact problem on 2026-07-04 and it was solved by
applying the **aggregate Census I→II retention rates — `61.23% human, 63.82% robot`.** Applying the same
method gives **Byrd 235,708 · Vostok 245,068 · Kunlun 78,785 · Dome Fuji 35,147.**

> **⚠ Open question worth a ruling before anyone uses those:** would **Kunlun and Dome Fuji** — robot-only,
> extreme-altitude, astronomically-purposed — have participated in orbital migration at the national average
> rate? **A robot-only observatory city may have had no reason to send anyone up, or every reason.** The flat
> rate is a defensible placeholder, not an answer.

**Recorded here rather than acted on. Not this pass's job.**
