# The "But / Therefore" Method — Lore & Culture Design Rules

**Companion document to `But_Therefore_Quest_Design_Method.md`** (same folder), adapting the same
Parker/Stone technique from *plot* (player-facing beats) to *history* (how a place got to be the way
it is). Brought in 2026-07-15, most immediately for city lore, with the explicit intent to scale up to
subnet- and nation-level lore once city-scale work is further along — see
`project_dlc_quest_design_plan` memory for the session context.

**Status:** a reusable method, not itself lore. Nothing here is canon. Stays in `to-be-integrated/`
until proven useful in practice — see that folder's own review-and-extract TODO item.

---

## 1. The core rule, applied to history instead of plot

A history built out of "And Then" is a list of facts in chronological order: *the city was founded by
X, and then it grew, and then it developed Y cuisine, and then it built Z architecture, and then the
war came.* Every individual fact can be true and the whole thing can still read as inert — a
Wikipedia infobox with paragraphs around it, not a place that feels like it was actually lived in.

A history built out of "But / Therefore" makes every later fact a **consequence of an earlier
complication**: the founders wanted one thing, **but** the site/population/circumstance pushed back,
**therefore** they adapted in a specific way, **but** that adaptation created its own new tension
generations later, **therefore** the culture kept moving. This is the same rule as the quest-design
document, aimed at a different kind of beat: not "what does the player do next," but "what did this
population have to do next, and why."

---

## 2. The same two functions, doing lore-specific work

- **"Therefore" = the practical response.** A population facing a real circumstance (climate,
  inherited infrastructure, a demographic shift, a war) does something specific about it. That
  specific response — not the circumstance alone — is what becomes "culture." This is already how
  this project's own 7-point generative framework works (see
  `Cities/Founding_Nation_Bug_Investigation_Methodology.md`, Section 2) — "Therefore" is the
  connective tissue between physical circumstance and the practice that actually results from it.
- **"But" = the reversal that keeps a history honest.** Founders arrive expecting one outcome, **but**
  something — the environment, later immigration, a war, a diplomatic decision made on their behalf —
  pushes the story somewhere they didn't plan for. **This is, structurally, the single most important
  beat in almost every Tepenian city's own founding-to-present arc already on record**, because it's
  the exact hinge the whole country-wide culture re-check was built to protect: a city's real-world
  *founding station operator* (bucket #1, GPS-only) is never allowed to be the thing that explains
  present-day culture on its own — there has to be a genuine "but" between founding and present, where
  the *actual, current population* (bucket #2) took over as the causal engine. A city whose lore skips
  that "but" is exactly the kind of city this whole project's bug-hunt kept finding problems in.

---

## 3. The failure mode: lore that lists facts instead of causing them

The exact bug class this whole project spent the last two days hunting — unsupported tier
annotations, stale demographic assumptions in creative sections, a cuisine or music section that
names a nation with no supporting text anywhere in the Founding Story — is what happens when a city's
lore is written as an And Then list instead of a But/Therefore chain. If a "therefore" doesn't
actually trace back to a real "but," the resulting sentence is an assertion with nothing underneath
it, which is precisely what a tier-annotation audit or a Local_Cultures re-read keeps catching. **The
discipline in this document, applied at write time, is a direct structural defense against that whole
bug class** — not a new rule, but the generative half of the same rule the investigation methodology
enforces after the fact.

---

## 4. Worked example, using already-established Tepenia lore

Applying this to Belgrano's already-written "Boneyard Times" history (see
`Local_Cultures/Halley_Subnet/Belgrano.md`, `Worldspace/Factions/City_Origin_Factions_PostWar_Refugee.md`)
to show the chain that's already implicitly there, made explicit:

> Belgrano was founded as a working Argentine Air Force base — a population defined by operational
> discipline, runway maintenance, function over comfort. **But** unlike its neighbors, Belgrano
> survived the Long Night War intact — no single geographic reason protects it the way Sanay's
> bedrock or Lazar's sheer scale do, which is itself still an open question (see `TODO.md`, "Belgrano's
> Wartime Status"). **Therefore** the post-war community expected the disciplined, functioning
> institution they'd always had to simply continue. **But** the institution itself didn't survive the
> peace — infrastructure failure, population loss, and severed supply lines eroded it over decades,
> even though the city itself never fell. **Therefore** the discipline persisted anyway, as habit and
> inheritance rather than active institutional purpose — people who "still function like an airbase
> crew, because that's the only civic template Belgrano ever had, but there's no chain of command left
> to answer to." **But** the mechanic subculture that once served the Air Force's own vehicles is now
> one of the only things in the Boneyard Times that's genuinely load-bearing again — keeping old
> Rastras running is real, earned standing, independent of the founding discipline it descended from.
> **Therefore** Belgrano's present-day culture is a population still living out an institutional
> reflex whose institution is gone, with exactly one skill from that era that never stopped mattering.

Notice this required no new invention — every fact is already on record. What the chain does is show
*why* those facts belong in that order, and why the culture reads as earned rather than assigned. A
city whose write-up can't be re-told this way — where the facts don't actually depend on each other —
is a city whose lore is still mostly And Then.

---

## 5. Plot — or rather, History — Schematics

### 5a. The Founding-to-Present Causal Spine (default city/place template)

```
FOUNDING CIRCUMSTANCE  — real-world station/site inherited; who arrived and why (GPS-only fact,
                          per bucket #1 — this is a starting condition, never the final explanation)
   │
   ▼ BUT
COMPLICATION            — the environment, the site, or the population itself didn't match what
                          the founders expected or intended
   │
   ▼ THEREFORE
FOUNDING-ERA RESPONSE    — the specific thing this population did about it; this becomes the
                          city's earliest civic character (the load-bearing move, per the
                          7-point framework's Section 2, item 3)
   │
   ▼ BUT
HISTORICAL TURNING POINT — later immigration, a treaty, a war, a redistribution — something
                          shifts who the population actually is or what the city actually does
                          (this is where bucket #2's own current population becomes the real
                          causal subject, if it hasn't already)
   │
   ▼ THEREFORE
PRESENT-DAY CULTURE      — the current, tracked population's own lived response to everything
                          above — never the founding nation's temperament, always this
                          population's own history of solving real problems
   │
   ▼ BUT
OPEN TENSION             — an honest, still-live question the culture hasn't resolved (a real
                          Open Questions entry, not a plot hook manufactured for its own sake)
```

**Design check:** if you can delete the Historical Turning Point and the Present-Day Culture section
doesn't need to change, the turning point isn't load-bearing — it's decoration, and the city's culture
is still quietly resting on the Founding-Era Response (or worse, on the founding nation) alone.

### 5b. The Demographic Reversal (for the founding-nation-vs-current-population case specifically)

A narrower, more targeted version of 5a for the single most common shape in this project's own city
lore — a station's real-world operator is not the city's own current causal population:

```
REAL-WORLD OPERATOR     — the nation that physically built the station (bucket #1; a GPS fact,
                          stated once, then set aside)
   │
   ▼ BUT
THE MECHANISM            — pick the one that's actually true for this city, don't default to the
                          first one that comes to mind:
                          — organic dilution (later immigration outpaces the founders, e.g. Sayowa)
                          — diplomatic allocation (an Upper Earth institution assigned the site to
                            a different nation entirely, e.g. Shirayuki/{{Korean city}}'s Jeju-do
                            mechanism)
                          — two-settlement coalescence (an adjacent, unrelated population absorbs
                            an unoccupied site, e.g. Lazar)
                          — total succession (the founding population leaves entirely; a new,
                            unrelated population arrives later for its own reasons, e.g. Dome Fuji)
   │
   ▼ THEREFORE
CURRENT CAUSAL POPULATION — whichever population the mechanism above actually produced — this,
                          and only this, is allowed to explain present-day culture
```

**Design check:** if the "mechanism" step is missing or unstated, the city is at risk of exactly the
bug class this whole project's founding-nation sweep exists to catch. Naming the mechanism explicitly,
in-lore, is what turns "GPS coincidence" into an actual causal chain a reader can follow.

### 5c. The Lore Beat Worksheet

```
Place: ___________________________     Scale: [ ] City  [ ] Subnet  [ ] Nation

FOUNDING CIRCUMSTANCE:   ______________________________________________
   BUT                   ______________________________________________
COMPLICATION:            ______________________________________________
   THEREFORE             ______________________________________________
FOUNDING-ERA RESPONSE:   ______________________________________________
   BUT                   ______________________________________________
HISTORICAL TURNING POINT: _____________________________________________
   THEREFORE             ______________________________________________
PRESENT-DAY CULTURE:     ______________________________________________
   BUT                   ______________________________________________
OPEN TENSION:            ______________________________________________

Self-check: does every "THEREFORE" line trace back to the "BUT" directly above it, or did it
sneak in a fact that isn't actually caused by anything? If the latter, that's an unsupported
claim waiting to be caught in the next integrity check — fix it now, not later.
```

---

## 6. How this interacts with the project's own existing frameworks

This method doesn't replace anything already established — it's the sequencing discipline underneath
tools that already exist:

- **The three-way GPS/population/temperament distinction** (`Founding_Nation_Bug_Investigation_Methodology.md`,
  Section 1) — the "But" in Section 5b above *is* this distinction, written as a narrative hinge
  instead of a checklist rule.
- **The 7-point generative framework** (same doc, Section 2) — items 1-3 map onto 5a's Founding
  Circumstance → Complication → Response; items 4-6 map onto the Historical Turning Point and
  Present-Day Culture stages; item 7 (real-world echo, applied last, as flavor) belongs *after* the
  chain is built, never as a substitute for it.
- **The investigation methodology's own bug patterns** — nearly every named pattern in that document
  (unsupported tier annotations, stale demographic assumptions, methodology-level GPS violations) is
  what a broken or missing But/Therefore link looks like once it's already been written and shipped.
  Using this method at design time is cheaper than catching the gap at audit time.

---

## 7. Scaling to subnet- and nation-level lore

The developer's own stated plan is to start with cities and move to the country level once that's
further along. The schematic doesn't need to change shape — only the scale of "Founding Circumstance"
and "Historical Turning Point" does:

- At **subnet scale**, the Founding Circumstance becomes something like a subnet's own settlement
  pattern (e.g. Halley subnet's shared South African shipping-partner arrangement), and Historical
  Turning Points are subnet-wide events (a redistribution, a war-damage pattern shared across member
  cities — see e.g. `Mirny_Cross_City_Patterns.md`'s own "one-principle war-damage logic" as an
  example of exactly this kind of subnet-scale causal spine, already written, just not yet framed this
  way explicitly).
- At **nation scale**, the same shape applies to the First and Second Interwar Periods, the Long Night
  War itself, and the Planetary Split Brain — each of which already functions as a "But" reversal at
  national scale (the Falkland Treaty's founding intention, **but** the Long Night War, **therefore**
  the Split Brain's fractured post-war reality). The Second Interwar Period's own flagged-but-unresolved
  "Break into Two (~2614)" item (`TODO.md`) is a natural first candidate for this scale of work, once
  it starts.

The worksheet in Section 5c already has a Scale field for exactly this reason — use the same
process regardless of which level you're working at.
