# EXTENT / AREA — HOW TO APPROACH IT

**Created 2026-09-04**, at developer direction, after the climate block closed at 37/37 and left
**`T2-8` EXTENT/AREA as the last unaddressed required input.**

> ## THE STANDING SITUATION
> **Not one of the 37 cities has a declared extent, area, footprint or land-take.** `01` §2 requires **two
> bands declared, population *and* extent** — *"when they diverge, the divergence is characterizing."*
> `01` §6's declaration block has a mandatory `**Extent band:**` line. `00_RUNBOOK.md` Step 2 item 6 orders
> the division and calls it *"the cheapest plausibility check in the methodology."*
>
> ⛔ **It has never been runnable for any city in the project.**

---

# 1 · ⛔⛔ THE TRAP — **DO NOT DERIVE EXTENT FROM DENSITY**

**The tempting shortcut: pick a density archetype per city, divide Census I by it, record the result as
extent.** ***This destroys the only thing extent is for.***

> ### Why — `04` Gate 11's own verdict on its single successful catch
> ***"Divide the population by the area. That is the whole technique."*** — and on why it worked:
> ***"the part that fired was the part that was ARITHMETIC… it is the only part of this gate that does not
> run on the same faculty that produced the error."***

**If area is computed from an assumed density, then `population ÷ area` returns the assumption.** **The one
instrument in the methodology that is immune to the author's own blind spots would begin confirming them
instead.** ⛔ ***Extent must come from a source independent of population.***

**Corollary:** ⭐ **density is an OUTPUT to be checked, never an input to be chosen.**

---

# 2 · ⛔ THE STANDING CORRECTION — **ICE IS BUILDABLE**

**Developer correction, restated 2026-09-04:** *"'building area' is not restricted to 'ice-free'; it's
limited by actual physical/geographical/geological conditions/settings."*

**This is established canon, not a permission being sought:**

| City | Built on |
|---|---|
| **Halley** | **the Brunt Ice Shelf** — its own spec records that it *risks eventually calving off into the ocean*, which is why the Halley subnet's Arcanet nexus sits at Sanay instead |
| **Neumayer** | ***"built on the Ekström Ice Shelf rather than on bedrock, which has structural implications for long-term city stability"*** |

> ⚠ **Six cities have a real-world area figure and NONE of them is a city extent** — Cape Adare (2.94 km²
> cape) · Denison (1.11 km² ASMA) · Davis (~400 km² oasis) · Lazar (~34 km² oasis) · Sayowa (~4–5 km²
> island) · Sinheung (~34 km² hills). ***They measure the real-world SITE, not the city, and they bound
> nothing.*** **A prior version of the audit called them "upper bounds on habitable land." That was wrong,
> and it is the exact misreading this section exists to prevent.**

---

# 3 · ⭐ RECOMMENDED APPROACH — **SETTLEMENT-FORM TYPOLOGY FIRST, DIMENSIONS SECOND**

***Classify what shape each city physically CAN be. Then extent follows from the form plus the site's own
dimensions — and density falls out as an output.***

## ⭐ The corpus already contains a partial version of this

**`Official_Population_Census.md` annotates ELEVEN cities "island cap"** *(corrected 2026-09-05 — see §7b)* —
**Sejong · Marambio · Dumont d'Urville · Fort McMurdo · Juan Carlos · Scott · Palmer City · Rothera · Sayowa ·
Signy · Port Lockroy.** ***That is a settlement-form constraint already doing real work in the census.***
**This approach generalizes what is already there rather than importing something new.**

> ⛔ **This line previously named six cities and included Zukelli, which carries no such annotation.** *One
> false inclusion, six omissions, in the single piece of corpus evidence this section rests on.* ⚠ **Verified
> by field position in the census table, 2026-09-05** — *an earlier grep matched subnet names in the wrong
> column and returned a longer, also-wrong list.*

## Candidate forms

| Form | What binds it | Cities |
|---|---|---|
| **ISLAND-CAPPED** | finite land; a hard ceiling regardless of engineering | the six already annotated |
| **RIDGE-LINEAR** | builds *along* a spine and cannot widen | Abowasa · Princess Elisabeth · Sanay *(nunatak sites)* |
| **OASIS-BOUNDED** | ice-free basin, lake catchments, surrounding ice margin | Larsemann trio · Davis · Lazar |
| **SHELF-SPREADING** | flat and effectively unlimited — ***until the calving margin*** | Halley · Neumayer · Belgrano |
| **VALLEY-SPANNING** | must bridge rather than spread | ⭐ **Denison** — already canon |
| **PLATEAU-OPEN** | almost no lateral constraint; **cold and altitude bind instead of terrain** | Concordia · Vostok · Dome Fuji · Kunlun · Amundsen |

⚠ **Assigning a form is a RULING, not research.** *Research without the typology produces numbers with
nothing to attach them to. Do the typology first.*

---

# 4 · WHAT ACTUALLY CONSTRAINS BUILDABLE AREA

**Since ice is buildable, the real limits are surface mass balance, ice dynamics and terrain.**

### ⭐⭐ 4.1 Accumulation vs ablation — *and this is the climate work, applied*

**In an ACCUMULATION zone, anything built is BURIED. In an ABLATION/scoured zone, the surface lowers and
foundations EXPOSE.**

> ### ⭐ Byrd is already canon for exactly this
> ***"founded underground before it existed on the surface"*** — **buried by snow accumulation, grew
> downward, surfaced later.** ***That is not a quirk of Byrd's history. It is the physics of a
> high-retention site, and it should be predictable from the retention figure.***

**The per-city retention figures are already computed** and sit in each spec's `Precipitation regime` block:
`Reference/Real-World/Climate Data/Precipitation_Falls_vs_Lands.md`. **A ~90%-retention plateau city and a
~38%-retention katabatic margin city face opposite foundation problems**, and that difference should shape
what "extent" even means for each.

### 4.2 The rest

| Constraint | Effect on extent |
|---|---|
| **Ice flow velocity** | ⭐ **a city on moving ice DEFORMS over 250 years.** Amundsen Station drifts ~10 m/yr with the ice |
| **Calving margin** | a hard outer limit on shelf-spreading cities — **Halley's own spec already says it risks calving off** |
| **Crevasse fields** | unbuildable, or bridge-only |
| **Slope / gradient** | steep ice slopes and nunatak walls |
| **Katabatic drainage paths** | building in the channel is **Denison's entire identity** — see `Precipitation_Falls_vs_Lands.md` §Regimes |
| **Meltwater and lakes** | the Larsemann Hills hold **150+ lakes across 40 km²** — catchments are not building land |
| **Bedrock depth / ice thickness** | anything anchored rather than floating |
| **Altitude** | ⚠ *human* limit, not a terrain limit — see `…/Concordia-City/Concordia_Altitude_and_Atmosphere.md` |

---

# 5 · TWO STRUCTURAL RECOMMENDATIONS

## 5.1 ⭐ Extent needs a VERTICAL COMPANION — a footprint alone is meaningless

**A density figure cannot discriminate without knowing whether the city is three storeys or forty.**

> ⭐ **Denison's spec has already run this.** **1.11 km² · ~34 levels if the valleys are spanned · ~69 if
> built on the ridges alone** — *"spanning the valleys is what makes the population fit, so the load-sharing
> structure is not an aesthetic choice, it is the only arrangement that works."*

***Declare `Extent band` and `Built mode` together, or Gate 11 still cannot discriminate.***

## 5.2 BANDS, NOT POINT VALUES

**`01` §2 asks for an extent *band*.** ⛔ **Resist a spurious "14.7 km²."** A band is honest about the
precision actually available, and **still catches order-of-magnitude errors — which is all Gate 11 has ever
caught.**

---

# 6 · WHERE TO START — the two extremes, because they calibrate the middle

| Start with | Why |
|---|---|
| ⭐ **Denison** | **the worst density case in the corpus** — naive ~960,000/km², nearly 3× worse than the Cape Adare figure that was already rejected as implausible. **And it already has a researched megastructure answer** sitting flagged in its spec |
| ⭐ **The six "island-capped" cities** | **hard physical ceilings already annotated in the census.** If the method cannot produce a defensible number where the constraint is unambiguous, it will not work anywhere |

**Getting the method right on both extremes calibrates everything between them.**

## ⚠ Live implausibilities already recorded, waiting on this

- **`Specs/Sayowa.md`** has already run the division: ***"225,376 people on ~4–5 km² is ~50,000/km² — the
  implausibility…"***
- **`Specs/Cape_Adare.md`** says outright: ***"the exact figure is a worldbuilding decision, not an
  arithmetic one."***

---

# 7 · WHAT IS RESEARCH AND WHAT IS RULING

| Ruling *(developer)* | Research *(can be gathered)* |
|---|---|
| **Settlement form per city** | buildable terrain and slope at each real-world site |
| **Built mode** — vertical, spanning, subsurface, sprawling | **ice thickness, flow velocity, calving-margin position** |
| **Band widths** — what counts as COMPACT vs EXTENSIVE | **accumulation vs ablation** *(already done — see §4.1)* |
| **Whether Tepenian engineering exceeds real-world limits, and by how much** | crevasse fields, lake catchments, drainage channels |

⭐ **The research half is tractable** — the same archives that closed the climate block *(BAS, NOAA NCEI,
PANGAEA, ASMA management plans)* carry ice thickness, flow and terrain data. **The ruling half is not
research and should be settled first.**

---

# 7b · ⭐⭐ DENISON — **worked 2026-09-05. The calibration case, and the first correction it produced.**

**§6 nominated Denison as the place to start, on the grounds that it is the worst density case in the corpus.
It was worked first, and it behaved as predicted.**

## What the site actually is

🔬 **Cape Denison is ~1.5 km wide and ~1 km inland, rising to meet the icecap at ~40 m**, and its structure is
**four rocky ridges running SSE–NNW separated by three valleys**:

| Feature | Geology | Buildable? |
|---|---|---|
| **The four ridges** | **gneiss and schist** — Gondwana-age metamorphic basement | ✅ **competent rock** |
| **The three valleys** | ⛔ **ice, snow and glacial moraine**, with small glacial lakes and summer melt streams | ⛔ **not ground** |

> ⭐ **This is WHY the spec's answer is *spanning* rather than filling.** *You cannot found in a valley whose
> floor is moraine over ice with a lake in it. You anchor in gneiss on one ridge and gneiss on the next.*
> **The megastructure is not an aesthetic choice — the geology forbids the alternative.**

## ✅ DEVELOPER RULING — the city spans ridges, valleys AND the islands

***"the city of Denison spans the four ridges, the three valleys, and the 30-or-so small islands… built
similarly to something along the lines of Venice/Mestre."***

⭐⭐ **The Mackellar Islands lie 3 km north — ~30 islands and rocks, 346 ha (3.46 km²) including intervening
sea.** ⭐⭐⭐ **And the reference is quantitatively exact, not merely thematic: the Venice–Mestre causeway is
roughly 4 km, and the Cape–Mackellar gap is 3 km.** *Same span, therefore the same kind of city — one
municipality, two halves of opposite character.*

⚠ **But it inverts Venice historically.** *There the islands came first and the mainland is expansion.* **Here
the cape is the founding rock and the islands are where you go when 1.11 km² fills up** — which gives a
three-stage growth story driven entirely by geology: ***settle the ridges → span the valleys → span to the
islands.***

## ⛔⛔ THE ENVELOPE IS FINAL — there is no third expansion

🔬 **Commonwealth Bay is ~48 km wide and holds *"limited ice-free bedrock… small rocky capes, offshore
islands, and isolated nunataks."*** **The inventory, from Cape Denison:**

| | Distance | |
|---|--:|---|
| ⭐ **Mackellar Islands** | **3 km** | ***the last thing that is still city*** |
| **Cape Hunter** | 15 km W | small promontory |
| **Whetter Nunatak** | 15 km ENE | *"small rock outcrop"* |
| **Blair Islands · Cape Gray** | ~40–48 km E | the bay's far side |
| **Madigan Nunatak** | 33 km S of Cape Gray | isolated, above the ice sheet |

> ## ⭐⭐⭐ A 3 km HOP, THEN A 12 km CLIFF.
> **3 km of spanning is a bridge network — walkable, continuous, a city. 15 km of spanning is a supply line
> nobody lives on.** ***Those are different objects.*** **Everything past Mackellar is a satellite — a quarry,
> a relay, a wind station — never a district.**
>
> ⛔ **So Denison is the corpus's clearest case of a city that CANNOT SPREAD, ONLY STACK.** *Every further
> person goes up or down. There is no third direction.*

## The numbers

| Envelope | Density | Levels for Paris-like density per level |
|---|--:|--:|
| **Cape only** — 1.11 km² | ⛔ **960,489/km²** | ~48 |
| ⭐ **Cape + Mackellar** — **~4.96 km²** | **~215,000/km²** — **4.7× Manila** | ⭐ **~10** |

⚠ **4.96 km² is ENVELOPE, not land** — *it includes three moraine valleys and the water between thirty
islands.* **The figure assumes the megastructure; it is not "tall buildings on available ground."**

## ⏸️ AND THE POPULATION IS FLAGGED FOR REDUCTION

> ***Developer, 2026-09-05: "mark Denison for future number-reduction, once we have a better idea of other
> cities."***

⛔ **Not reduced. Held deliberately** — *reducing the worst case in isolation would set a precedent with
nothing calibrating it.* ⭐ **Until then, ~215,000/km² over ~5 km² at ~10 levels is a usable CEILING for §7's
band widths: whatever COMPACT means, it has to accommodate this.**
*(Flagged in `Official_Population_Census.md` both rows, and in `Specs/Denison.md`.)*

## ⛔ A CORRECTION TO THIS FILE, found while working Denison

**§3 claims the census annotates six cities *"island cap"* — Fort McMurdo, Dumont d'Urville, Juan Carlos, Port
Lockroy, Scott, Zukelli — and calls that the settlement-form typology already doing real work.**
***That list is wrong: one false inclusion and six omissions.*** **The census annotates ELEVEN:**

**Sejong · Marambio · Dumont d'Urville · Fort McMurdo · Juan Carlos · Scott · Palmer City · Rothera · Sayowa ·
Signy · Port Lockroy** — ⛔ **and Zukelli is NOT among them.**

⚠ **Corrected in §3 2026-09-05.** *Recorded rather than quietly fixed: this file's single piece of
corroborating corpus evidence was wrong, and it is the list meant to seed the typology.*

---

# 8 · ⏸️ STATUS

**DEFERRED BY DEVELOPER RULING, 2026-09-03:** *"The issue of density has to be addressed another time…"*
**Reopened for approach-design 2026-09-04; no extent figure has been derived, proposed or assumed for any
city.** ⛔ **Do not derive one until the §7 rulings are made.**

> ## ⭐⭐ SCHEDULED — **2026-09-05, developer ruling 2026-09-04**
> > ***"tomorrow, first, we need to address `Ports.md`… Then, once that's done, we'll go through and
> > establish 'Extent / Area'."***
>
> **This work is SECOND in the queue, after `Ports.md`.** *(`Ports.md` is a 0-byte file in a registered
> infrastructure folder that four sea-dependent cities now resolve to — see `ULM_Input_Available_Audit.md`
> §4e.)*
>
> ### ⛔ OPEN THIS SESSION WITH THE §7 RULINGS. **Not with research.**
> **All four are developer decisions and every one of them gates the work below it:**
>
> | # | Ruling | What stalls without it |
> |---|---|---|
> | **1** | **Settlement form per city** | ⛔ **Everything.** §3: *"Research without the typology produces numbers with nothing to attach them to"* |
> | **2** | **Built mode** — vertical · spanning · subsurface · sprawling | §5.1 — **a footprint alone is meaningless.** Denison already proves it: *1.11 km² is ~34 levels spanned, ~69 on ridges alone* |
> | **3** | **Band widths** — what counts as COMPACT vs EXTENSIVE | §5.2 — without them there is nothing to declare on the `**Extent band:**` line |
> | **4** | **Whether Tepenian engineering exceeds real-world limits, and by how much** | The multiplier every figure is computed against |
>
> ⭐ **Recommended first two cities once the rulings exist: Denison and the six island-capped** *(§6)* —
> **the two extremes, because they calibrate everything between them.**
>
> ⛔⛔ **And the trap, restated because it is the one that would waste the whole session:
> DO NOT DERIVE EXTENT FROM DENSITY** *(§1)*. **Density is an OUTPUT to be checked, never an input to be
> chosen.**

**Related addresses:**
`ULM_Input_Required_Reference.md` → `T2-8` · `ULM_Input_Available_Audit.md` §2 *(the headline gap)* ·
`Location_Data-Input_To-Do.md` §1 *(ranked #1)* ·
`Reference/Real-World/Climate Data/Precipitation_Falls_vs_Lands.md` *(retention, per city)*
