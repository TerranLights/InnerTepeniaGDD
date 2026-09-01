# Resolution Log — live, append-only

**What was acquired, how, from where, and what was deliberately left unchased.** Append-only; **written as the
work happens, never reconstructed afterward.**

**Why this file earns its place rather than being bookkeeping:** a finished pass publishes conclusions and
buries evidence. Without this log, a later session cannot re-check a claim against its source, cannot tell a
researched fact from an assumed one, re-runs searches already run — and loses every thread deliberately left
hanging, which is routinely the richest material the work produced.

---

## Entry schema

```
### CGRM-nnn — <the gap, in one sentence>
**Date:** YYYY-MM-DD   **Scope:** <location / person / subsystem>   **Path:** <1–7>
**Cheaper paths ruled out:** <which, and why — required, not optional>

**Method** — whichever applies to the path used:
- Path 1/3: the exact file and section the answer came from
- Path 2:   the formula, its inputs, and where each input was verified AT ITS OWN SOURCE
- Path 4/5: the exact search strings, verbatim, and the sources with links
- Path 6/7: the developer's own words, verbatim

**Result:** <what was acquired>
**KIND:** attribute / conclusion / decision        **Destination:** <file, section>
**Marker applied:** yes / not-required             **Provenance tag written:** yes
**Gates run:** <which of the six, and what each found>

**Open threads — noticed and NOT chased:**
- <what, and what it might yield>
```

**The open-threads field is not optional and is not a courtesy.** An unchased thread is fine; a *silently*
unchased thread is indistinguishable from one that was never noticed at all, which defeats the whole point of
logging.

---

## Entries

### CGRM-019 — How are Tepenian cities laid out? *(new gap, raised and closed within the run)*

**Date:** 2026-08-31 **Scope:** project-wide **Path:** 6 — developer ruling
**Origin:** raised *during* CGRM-009, when the question "could the city occupy the whole peninsula?" turned out
to depend on an unstated general model. **Registered as its own gap rather than folded into CGRM-009**, because
its answer binds every city, not one.

**Method — the developer's own words, verbatim:**
> *"it may be possible for Tepenian cities to use ice-free zones (in the circumstances where they're available)
> as 'downtown core', and iced zones as 'outer areas' or 'suburbs' or something vaguely, roughly to that
> effect. Because 'suburb' doesn't necessarily need to equal 'residential'. A fine example of this is Los
> Angeles. There's the actual city of Los Angeles, there's downtown West Hollywood, and then there's Greater
> Los Angeles (which is technically, officially suburbs, while still being full of industry, music, food,
> culture, and activity)."*

**Result.** **Ice-free terrain sizes a city's downtown core, not its total extent.** Iced terrain beyond it is
outer area — larger, less dense, and **not merely residential**: working, living territory on the Greater-Los-
Angeles pattern.

**⚠ This corrected an error made earlier in this same run — recorded, not quietly dropped.** CGRM-009 reported
Cape Adare at 357,160/km² as **6.7× implausible**. **That reading was wrong**, because it divided the whole
population by the *core* and treated the result as the city's density. **Under the correct model the
implausibility dissolves completely.** What survives is better than what was lost: the 2.94 km² cape is now
understood as **the smallest documented downtown core in Tepenia against a very large population** — a real
characterizing fact rather than an arithmetic alarm.

**The transferable lesson, worth more than the ruling:** **an arithmetic check is only as good as the frame it
assumes.** Gate 3 verified the inputs, the formula, and the comparison set, and every one of those was
correct — **the error was in what the numerator and denominator meant.** *(This is the acquisition-side echo of
a failure this project has already recorded in derivation work: a census parse that indexed the wrong column
and returned 33 plausible rows, a sensible mean, and a sensible spread, all wrong, without erroring.)*
**Proposed Gate 3 addition: before trusting a derived figure, state what the numerator and denominator each
actually represent.**

**KIND:** decision **Destination:** `Cities/Overview.md` — new "How Tepenian cities are laid out" section
*(chosen over a per-city Spec because it binds all 35)*; Cape Adare's Spec updated to apply it and to record
the correction
**Marker applied:** not required **Provenance tag:** yes, both
**Gates:** G1 ✅ · G2 ✅ decision→general reference · G5 ✅ · G6 ✅ two deposits, both required by the ruling's
own scope

**Open threads:**
- **Does every city's outer area develop equally?** Not asked. The model permits variation and does not
  require it.
- **Does core/outer carry civic or administrative meaning**, or is it purely descriptive? Undetermined.
- **31 of 35 city Specs still state no extent**, so most cities have neither a core figure nor an outer
  boundary. **The model is now available to them; the figures are not.**

---

### CGRM-009 — Cape Adare's land area *(the run's most substantial result)*

**Date:** 2026-08-31 **Scope:** Cape Adare **Path:** 4 (research) → 2 (derivation)
**Cheaper paths ruled out:** Path 1 first — **no city Spec, infrastructure file, or census file states an area
for Cape Adare anywhere.** Path 2 alone was impossible without a real-world figure to derive from. So: research
first, then derive.

**Method.** Search: `Cape Adare Adare Peninsula Antarctica area size square kilometers Ridley Beach dimensions`.
Sources: [Cape Adare — Wikipedia](https://en.wikipedia.org/wiki/Cape_Adare) · [Adare Peninsula —
Wikipedia](https://en.wikipedia.org/wiki/Adare_Peninsula) · [BirdLife
IBA](https://datazone.birdlife.org/site/factsheet/cape-adare-iba-antarctica/map) · [ATS site
guidelines](https://guidelines.ats.aq/GuideLinePDF/fe5fd16a-eee3-4577-9fbf-3fcbf4b3b082/Cape%20Adare_2021_e.pdf).
Then a Path 1 sweep of all city Specs for existing area figures — **found four** (Davis, Lazar, Fort McMurdo,
Sinheung), which supplied a real comparison basis instead of an invented one.

**Result.** Cape proper = **2.94 km²**; Adare Peninsula = **74 km** long; Ridley Beach ≈ **1.9 km per side**.
**Derived:** at 1,050,051 people the cape proper yields **357,160/km² — 6.7× Tepenia's densest city** (Lazar,
53,058/km² in the 34 km² Schirmacher Oasis) and ~7.8× the densest real city on Earth. **The settled extent must
therefore run onto the peninsula: ~20 km² to match Tepenia's densest, ~39 km² to match the mean of the three
known.**

**⭐ Also surfaced a project-wide pattern nobody had named:** the four Specs that state an extent all state it
as **the ice-free terrain the city occupies**, not a built footprint — and Fort McMurdo's Spec explicitly treats
land area as *capping* population ("island cap" in the census). **Tepenian city extent is an ice-free-terrain
claim.** That is the frame Cape Adare's own figure should eventually be set in.

**KIND:** attribute *(real measurements, and an arithmetic constraint derived from them)*
**Destination:** `Specs/Cape_Adare.md` → Geographic Basis, new "Physical extent" subsection
**Marker applied:** not required **Provenance tag:** yes
**Gates:** G3 ✅ inputs verified at own sources, arithmetic hand-checked, scored against the full known set not
a single neighbor · G4 ✅ no nationality claim involved · G5 ✅ tagged · G7 ✅ the four comparison figures were
read, not grep-counted

**⚠ Deliberately NOT closed:** **the exact extent.** ~20–40 km² is a bounded *range*; picking a value is a
worldbuilding decision, not an arithmetic one. **The floor is now established (the cape alone is implausible by
~7×); the value is not.**

**Open threads:**
- **31 of 35 city Specs still state no extent at all** — the same Gate 11 blocker will recur on every one of
  them. A project-wide extent pass is a real, well-defined, high-value job.
- Fort McMurdo's "island cap" implies a **land-constrained population model** that may already be implicit
  across the census. Not investigated.

---

### CGRM-011 & CGRM-018 — Universe-repo canon checks *(Cape Adare; Highway 37)*

**Date:** 2026-08-31 **Path:** 1 — cross-reference **Cheaper paths ruled out:** none cheaper exists.

**Method.** Deliberate cross-repo search at
`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/` — **outside this repo, so a
repo-local search cannot see it.** Grepped both subjects across the universe repo's `*.md`.

**Result — both CLEAN, no contradictions.** Cape Adare: 3 hits (Janbogo/Ross subnet membership; site predating
the exile; a documentation-coverage note) — all consistent with `Specs/Cape_Adare.md`. Highway 37: Kunlun's
"real physical highway link exists via Hwy 37" and Mountain Pass described as a Vostok–Kunlun joint venture on
Hwy 37, powered by Tower-grid overflow — **consistent with ULM Run 6 in every particular.**

**One difference noted and explicitly NOT filed as a conflict:** the universe repo describes Mountain Pass in
past tense ("since-defunct"), while Run 6 wrote it alive. **That is the same location at two frames, which `01`
§4 already governs — two documents, not a contradiction.**

**KIND:** n/a — verification, no deposit **Destination:** none
**Gates:** G1 ✅ nothing closed prematurely · G6 ✅ in scope
**Effect:** **both ULM runs listed "universe-repo check not run" as an open REQUESTED item. Both are now
closed clean** — the cheapest closure in this run, and it retires a named gate gap in two separate passes.

**Open threads:** the universe repo was searched for the two subject names only, not for related concepts
(Janbogo subnet, Adélie rookeries, the Cradle network). A wider sweep might find more.

---

### CGRM-006 — Robot food/maintenance baseline for Cape Adare *(the gap collapsed)*

**Date:** 2026-08-31 **Path:** 1 — cross-reference **Cheaper paths ruled out:** none cheaper exists.

**Method.** Read `Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md`, §"Consumption
— Robot Equivalents."

**Result — the question did not need answering.** A project-wide baseline already exists: **siligel** (robot
food) and **coolant** (robot drink), with robot coffee and glitch-coolant as specialty formulations. **The file
also already supplies an explicit per-city variation framework** — a bohemian-varied vs. working-class-strong
potency axis — stating outright that it *"gives every Tepenian city with a meaningful robot population a
plausible, characterful local drinking scene without needing to invent one from scratch each time."*

**So ULM Run 7's REQUESTED item was malformed rather than unanswered.** The baseline was never missing; what
remains is the much smaller question of *where Cape Adare sits on an existing axis*.

**KIND:** n/a — no deposit needed **Destination:** none

**⚠ The axis placement was deliberately NOT made, and this is a boundary call worth recording.** Placing Cape
Adare on the variety/potency axis is **a conclusion derived from the location's established character — which
is synthesis work, not acquisition.** It belongs to a Phase 8 pass or Cape Adare's pending Zodiac Lens
follow-up, not to this system. **This system found that the input exists and handed the derivation back.**

**Open threads:** the same collapse likely applies to other cities' "robot culture" REQUESTED items across the
project — the baseline may already answer several of them.

---

### CGRM-016 — Is Highway 37 hitchhiking-valid?

**Date:** 2026-08-31 **Scope:** Highway 37 *(ruling binds the whole network)* **Path:** 6 — developer ruling
**Cheaper paths ruled out:** 1–5 inapplicable. A canon flag the developer sets explicitly for other routes;
not discoverable by cross-reference, derivation, or research. Correctly RESERVED at triage.

**Method — the developer's own words, verbatim:**
> *"I would say, 'partially'. That being, people perhaps may hitchhike at specific nodes. That being, nobody
> 'stands on the side of the road holding up a sign'. Rather, it may be possible to wait inside of the Tepenian
> equivalent of something like 'diners' or 'gas stations' or 'rest stops' or something vaguely to that effect,
> and socialize with passers-through who make a stop there (for whatever reason). Granted, this may end up
> taking much longer to hitch a ride, but it's much more realistic than simply standing on the side of the road
> near the entrance to a highway"*

**Result.** **Hitchhiking is node-based, never roadside — network-wide, not a Hwy 37 exception.** You wait
inside a stopping place and get a ride by socializing with people who stopped for their own reasons. Slower by
design. **In Antarctic conditions the roadside version is not survivable**, which supplies the physical reason
this is the only realistic model.

**⭐ Closed a second, older gap as a side effect.** `Highways.md` had carried a flagged open question since
2026-07-05 — *"exact in-world reasoning for why hitchhiking works on these particular routes... not yet
developed."* **The ruling answers it for the entire network.** Nobody asked for that; it fell out of asking
about one highway.

**Emergent finding, from combining the ruling with Run 6's existing work:** "hitchhiking-valid" is a claim
about **nodes, not pavement** — and Hwy 37's entire interior has **exactly one node** (Mountain Pass Airport).
Dome Fuji, Kunlun and Vostok are cities on the route, not roadside stops; the Hwy 22 dual-junction is a bare
crossing. **Hwy 37 is therefore the hardest route in Tepenia to hitchhike without being formally closed to it.**

**KIND:** decision **Destinations:** `Locations/Infrastructure/Highways.md` — the network-wide rule (replacing
the 2026-07-05 open question) **and** Hwy 37's own route entry
**Marker applied:** not required — decision **Provenance tag written:** yes, both
**Gates run:** Gate 1 ✅ correctly RESERVED, not self-closed · Gate 2 ✅ kind/destination match · Gate 5 ✅
tagged · Gate 6 ✅ two deposits, both in scope; the network-level deposit is the ruling's own stated scope, not
creep

**Open threads — noticed and NOT chased:**
- **What a Tepenian roadside node actually *is*** — the developer named diners/gas stations/rest stops as
  analogues, not as canon. **The node type itself is undefined**, and defining it is a real acquisition job
  (likely Path 7 or 4). It would also retroactively enrich the four other hitchhiking-valid routes.
- **Whether nodes exist on routes not marked hitchhiking-valid**, and if so why hitchhiking doesn't happen at
  them. Not asked.

---

### CGRM-013 — Who maintains Tepenia's highways?

**Date:** 2026-08-31 **Scope:** Highway 37 *(ruling binds all eleven highways)* **Path:** 6 — developer ruling
**Cheaper paths ruled out:** 1–5 inapplicable. A structural claim about the Federation's own administration,
binding well beyond one location. Correctly RESERVED at triage.

**Method — the developer's own words, verbatim:**
> *"for DRQ-02, I would say Hybrid, yes. Generally speaking, overall, the highway system is mostly, generally
> centralized, but also has distributed as well as localized elements. So, it's something of a combination of
> all three."*

**Result.** **Three tiers operating simultaneously**, not two: predominantly centralized, with genuine
distributed *and* localized elements layered in. **Richer than the queued option**, which had proposed a
two-tier trunk-federal/spur-local split. **Practical consequence for remote routes: central authority exists
but distance attenuates it** — on a plateau route with no resident population, the localized tier is what
actually operates, because the center is too far away to make a timely call.

**⚠ Revises an existing finding — stated, not silently overwritten.** ULM Run 6's Phase 7b *"nobody has
authority to declare the road open or closed"* is **wrong as stated**, but the behavior it observed survives
for a better reason. **Revised to: authority exists, at a distance that makes it inoperative in the moment.**
The pass's informal go/no-go caller (corroborated independently by its Zodiac Lens Aries result) is
**better grounded** under this ruling than under the original assumption.

**KIND:** decision **Destination:** `Locations/Infrastructure/Highways.md`, new "Maintenance Authority" section
**Marker applied:** not required — decision **Provenance tag written:** yes
**Gates run:** Gate 1 ✅ · Gate 2 ✅ · Gate 5 ✅ · Gate 6 ✅ in scope — the Run 6 revision was *flagged in the
deposit*, not edited into Run 6's own Test_Runs folder, per LAW B's "never write into a consumer's run folder"

**Open threads — noticed and NOT chased:**
- **The three tiers are named but not divided.** Which decisions sit at which tier is undefined — who sets
  standards, who funds, who schedules, who calls a closure. **A real follow-up job**, and the natural input for
  any future pass touching Federation infrastructure administration.
- **Whether the same hybrid model governs other national infrastructure** (Arcanet, power, ports). Not asked;
  do not assume.

---

### CGRM-015 — Should highways receive real-world inspiration picks?

**Date:** 2026-08-31 **Scope:** Highway 37 *(ruling binds all corridors)* **Path:** 6 — developer ruling
**Cheaper paths ruled out:** 1–5 all inapplicable. The question is not *what is the answer* but *whether the
category should exist* — a scope decision with an author, not a fact discoverable by cross-reference,
derivation, or research. Correctly RESERVED at triage.

**Method — the developer's own words, verbatim, both parts:**
> *"in terms of whether highways get real-world inspirational picks, I'm not really sure that's necessary,
> because a road will be dependant upon the context it's in, and that context will already be established by
> the worldbuilding"*
>
> *"not just the two locations it connects, but also what sort(s) of environmental setting(s) it runs through.
> A road's surroundings will be equally important as the sites it connects to each other"*

**Result.** **No per-corridor inspiration picks.** A corridor's character is already fully determined by two
equally-weighted contexts the worldbuilding has established — **what it connects** (G5, network position) and
**what it runs through** (G2, physical constraint). Real-world comparables remain legitimate for a corridor's
*physical texture* only, never its character.

**KIND:** decision **Destinations:** `Cities/Inspirational-Influences.md` (scope note, so a future session
finds the reason rather than an absence) · `Universal_Location_Methodology/02_Generators_Capability_and_
Symbols.md` §G7 (the type-level rule, where a Corridor pass will actually look)
**Marker applied:** not required — a decision, not conclusion-tier **Provenance tag written:** yes, both
**Gates run:** Gate 1 — correctly RESERVED, not prematurely closed by this system ✅ · Gate 2 — kind is
`decision`, destinations match ✅ · Gate 5 — tagged and greppable ✅ · Gate 6 — two deposits, both in scope;
ULM `02` edit is the consumer-facing half of the same ruling, not scope creep ✅

**Open threads — noticed and NOT chased:**
- **The ruling plausibly extends past Corridors to other non-Settlement types.** A Structure, a Natural
  feature, or a Network locus may have the same property — character determined by context rather than by an
  independent real-world analog. **Not asked, not assumed, not deposited.** Worth raising as its own ruling
  if a future pass runs one of those types.
- **`District-Inspirational-Influences.md` was not checked** for whether it carries an equivalent scope
  question. Out of this scope.

> ### ⭐ What this first entry demonstrated about the system itself
> **The verbatim-recording rule proved necessary within an hour of being written.** This entry's first draft
> paraphrased the ruling's context as *"the places it connects"* — silently dropping the environmental half,
> which is half the actual claim. The developer supplied the missing half unprompted. **`02` Path 6's warning
> that a paraphrased ruling is a lost ruling was validated on the very first ruling this system processed.**

> **One thread is already recorded elsewhere and belongs here when it is eventually worked:** the Nicolai
> Hanson grave at Cape Adare — the first human burial on the Antarctic continent — surfaced during
> groundwork for DRQ-01 and deliberately not pursued, since that session was building this system rather than
> running it. See `Developer_Ruling_Queue.md` DRQ-01's own open-thread note.
