# Developer Ruling Queue — live

**Batched decisions awaiting developer authority.** Per `02` Path 6: **this system prepares; it never
decides.** The value added here is not the decision — it is arriving at the decision with the constraints,
precedents, and consequences already laid out, so a ruling takes a minute instead of an evening.

**Batching rule:** these accumulate. **A reserved decision does not need to be made when it is discovered —
only before the work depending on it finishes.** The one exception is a decision blocking an in-flight pass,
which gets raised immediately and separately rather than waiting here.

**Format, per entry:** the question · why it is reserved · what canon already constrains · options with
consequences, where natural · what is blocked, and how badly.

---

## ⚠ DRQ-01 — **WITHDRAWN AND REPLACED, 2026-08-31.** The question was wrong; the date was settled six weeks ago.

> ### The original question should never have been asked
>
> **"What date honors St. Carsten?" was already answered on 2026-07-17** — *"February 17th is formally adopted
> as St. Carsten's Landing, a real civic holiday rather than a loose date people vaguely remember"*
> (`Background-Lore/Cities/Janbogo_Subnet/Cape_Adare/Cape_Adare_Course_of_Events_Suggestions.md` §6), with
> `Cape_Adare_Mega_Init.md` recording it as **"Resolved 2026-07-17."**
>
> **The developer was asked to rule on a decision their own project had already made**, and answered — entirely
> reasonably — *"at this time, I currently have no idea."* **Nobody could have known from the material in front
> of them.**
>
> **How the adoption propagated: it did not.** Checked directly, all three ❌:
>
> | File anyone would actually look in | Carries the adopted date? |
> |---|---|
> | `Specs/Cape_Adare.md` — Open Questions | ❌ still says *"a specific date TBD"* |
> | `Local_Cultures/…/Cape_Adare.md` §26 | ❌ names a **different** observance, *"exact date TBD"* |
> | `Worldspace/National_Holidays.md` — Saints roster | ❌ St. Carsten absent entirely |
>
> **My own failure, recorded:** CGRM Path 1 should have caught this. The project's own investigation skeleton
> requires widening to **a repo-wide grep with no path restriction** — and the answer was sitting in
> `Background-Lore/`, outside the Cities folder entirely. **I searched Cape Adare's own file set and stopped.
> That is a Gate 7 failure on this system's own first ruling-preparation, and it is exactly the blind spot the
> skeleton's concentric-ring rule exists to close.**

---

## 🔴 DRQ-01b — The real question: two files disagree on what the holiday commemorates

**Not a date. A contradiction — and it runs against the city's own stated theology.**

| Source | The observance | Which event |
|---|---|---|
| **Formally adopted 2026-07-17** *(Course of Events §6; Mega-Init)* | **"St. Carsten's Landing," February 17** | **the arrival** |
| **`Local_Cultures` §26** | **"St. Carsten's Wintering"** — *"the city's central civic observance"*; **"The First Landing"** demoted to *"a quieter, secondary observance"* | **the overwintering** |

**⭐ The sharp part, and the reason this needs a real ruling rather than a coin-flip:** the city's own religious
framing takes an explicit position, and it contradicts the adopted holiday. **`Local_Cultures` §18:** St. Carsten
veneration is *"focused specifically on the **act of staying** rather than the act of arriving — Borchgrevink's
significance was never that he came first, but that he was the first to remain through a winter."* **§2 says the
same:** *"He was simply the first person who stayed."*

**So the formally-adopted holiday commemorates the one thing the city's own theology says is not the
significant part.**

**Options:**
- **A — Keep the adopted Landing (Feb 17), fix the theology.** Simplest propagation; but requires softening
  §18's "act of staying" framing, which is well-developed and load-bearing for the city's identity.
- **B — Promote the Wintering to primary, keep the Landing as the secondary observance** exactly as
  `Local_Cultures` §26 already has it. **Preserves the theology intact**; needs a date for the wintering
  *(1 March 1899 — the day the ship sailed north and the ten men were left, verified real-world date — is the
  precise moment "the staying" began)*. The Feb 17 adoption survives as the secondary Landing observance.
- **C — Both are primary, deliberately.** A two-part civic season running 17 Feb → 1 March: the arrival, then
  the moment of being left. **Cheapest reconciliation — nothing already written has to be wrong.**

**Recommendation: B or C.** Both preserve §18; C additionally makes every existing file correct as written.
*(Flagging honestly: my earlier independent recommendation also favored the wintering, so treat this as a
consistent bias of mine rather than two separate confirmations.)*

**What is blocked:** propagation to all three stale files, and St. Carsten's addition to the national Saints
roster — which should happen in the same pass, whichever way this rules.

---

## ~~DRQ-01 — the original prepared groundwork, retained for the record~~

**Status: `deferred` — deliberately left open, at the deciding authority's own request. This is a correct
outcome, not an unresolved one** (LAW A: an open gap is not a defect). **The groundwork below stays warm** —
the four dated options, their differing meanings, and the recommendation are already prepared, so whenever this
is picked up the decision costs a minute rather than an evening. **That is exactly what the groundwork is for.**

**Do not re-prepare this entry, and do not press it.** It is not waiting on information; it is waiting on the
developer, by their own explicit choice.

**One thing worth carrying forward when it *is* picked up:** whichever date is chosen, that ruling is also the
natural moment to add St. Carsten to `National_Holidays.md`'s own Saints roster, where he is currently missing
despite Cape Adare's Specs already using the honorific.

**Registry row CGRM-004 → `deferred` (still RESERVED, still queued, explicitly not-now).**

---

## DRQ-01 — the prepared groundwork, retained warm

**The question.** What date does Tepenia use to honor St. Carsten?

**Why reserved.** An official observance date is an arbitrary civic choice. Nothing derives it; no research
produces it. **Authority only.**

**What canon already constrains.**
- The **Tepenian Saints** framework exists and is real, national-scale canon (`Worldspace/National_Holidays.md`):
  pre-war Antarctic explorers venerated *"for unknowingly preparing the home that exiles would later need,"*
  honorific using the **first name**. Existing roster: St. Robert (Scott), St. Ernest (Shackleton), St. Roald
  (Amundsen), St. Douglas (Mawson), St. Richard (Byrd).
- **⚠ St. Carsten is NOT yet in that roster**, despite Cape Adare's own Specs file using the honorific as
  established. **Whatever date is chosen, the ruling is also the natural moment to add him formally** — this is
  a real, concrete gap in a national reference file, surfaced by ULM Run 7.
- **Tepenian Independence Day is June 21** — a fixed point already on the calendar to avoid colliding with.
- Real-world dates, verified 2026-08-31 *(Wikipedia: Southern Cross Expedition; Antarctic Heritage Trust)*.

**Options — four different meanings, not four arbitrary dates.**

| | Date | What the observance would *mean* |
|---|---|---|
| **A** | **17 Feb 1899** — the *Southern Cross* reaches Cape Adare | **The arrival.** Honors the decision to come. |
| **B** | **1 March 1899** — the ship sails north, leaving ten men behind | **The staying.** The moment they became, in the sources' own phrase, *"the most isolated people on earth."* ⭐ **Best fit for the framework's own wording**, which venerates the first person who *stayed*, and for Cape Adare's own established civic identity of precedence-by-remaining. |
| **C** | **2 Feb 1900** — departure, having survived the winter | **The proof.** Honors survival rather than commitment. |
| **D** | A date tied to **Nicolai Hanson's grave** | **The cost.** Hanson died during that winter and was the first person buried on the Antarctic continent — see the open thread below. |

**Recommendation, offered not assumed: B.** It is the only option whose meaning matches both the Saints
framework's stated basis and Cape Adare's own established "first to stay, not first to arrive" identity.

**What is blocked.** Cape Adare's Phase 6 observance content (ULM Run 7 recorded it as a genuine null and
declined to invent a date); the completeness of `National_Holidays.md`'s own roster. **Neither is urgent;
both are cheap to close once ruled.**

> ### ⭐ Open thread, surfaced during this groundwork and deliberately NOT acted on
>
> **Nicolai Hanson died at Cape Adare during the 1899 winter and was buried there — the first human burial on
> the Antarctic continent**, with an iron cross mounted on a boulder above the grave.
>
> **Why this is flagged rather than used:** ULM Run 7's Phase 6 recorded *"Death and the dead"* as a complete
> null — *"no admissible material addresses this at all"* — and declined to invent anything. **That null was
> correct for in-fiction canon and remains correct.** But the real-world basis contains a grave, a first
> burial, and a marker, at a location whose entire established identity is *firstness* — which is exactly the
> shape of material a Path 4 research pass could turn into genuine canon.
>
> **Not pursued here, deliberately: this session is building the system, not running it** (`00` Step 1 —
> scope discipline; Gate 6). Recorded so it is not lost.

---

## ✅ DRQ-02 — Highway maintenance authority — **RULED 2026-08-31**

> ### The ruling, verbatim
>
> *"for DRQ-02, I would say Hybrid, yes. Generally speaking, overall, the highway system is mostly, generally
> centralized, but also has distributed as well as localized elements. So, it's something of a combination of
> all three."*

**Resolution: hybrid — and richer than the option offered.** The queued Option C proposed a two-tier split
(trunk routes federal, spurs local). **The actual ruling is three tiers operating simultaneously**: a
predominantly centralized system with genuine distributed *and* localized elements layered into it. **Not
"centralized with exceptions" — a combination of all three.**

**Deposited:** `Locations/Infrastructure/Highways.md`, new "Maintenance Authority" section.

### ⚠ This ruling revises an existing finding, and that was stated rather than silently overwritten

ULM Run 6 assumed **fully distributed, non-centralized** maintenance provisionally, and flagged everything
resting on it. **Under this ruling, its Phase 7b "nobody has authority to declare the road open or closed"
finding is wrong as stated — but the behavior it described survives for a better reason:** central authority
exists and is simply too remote to exercise in time on a plateau route with no resident population, so
practical decision-making devolves locally. **Revised from *"no authority exists"* to *"authority exists, at a
distance that makes it inoperative in the moment."***

**And the pass's related findings come out stronger, not weaker.** Its informal go/no-go caller — independently
corroborated by the Zodiac Lens's Aries result — is *more* interesting when there is a real authority somewhere
that cannot be reached in time than when there is no authority at all.

**Registry row CGRM-013 → closed. Log: `Resolution_Log.md` CGRM-013.**

---

## ~~DRQ-02 — original queue entry, retained for the record~~

**The question.** Who maintains Tepenia's highways — a central federal authority, or the cities and subnets
each route touches?

**Why reserved.** It binds **all eleven highways** and implies a piece of the Federation's own administrative
structure. Beyond one location's pass to decide.

**What canon already constrains.**
- Hwy 7-ext has confirmed construction dates (**2611–2614**) — the only highway with them — so *someone*
  organized and executed construction at scale.
- Subnets are **Arcanet** regions. Nothing establishes them as civil-administrative units, so "the subnet
  maintains it" would be a new claim, not an extension of an existing one.
- ULM Run 6 proceeded on an explicit **provisional assumption of distributed, non-centralized maintenance**,
  and flagged every finding resting on it.

**Options and their consequences — this one genuinely changes existing findings.**

| | Ruling | Consequence |
|---|---|---|
| **A** | **Centralized federal infrastructure authority** | Produces a named institution, a budget, and a chain of accountability. **Would invalidate Run 6's Phase 7b finding** ("nobody is empowered to declare the road open or closed") and its derived "enforcement without an enforcer" axis. |
| **B** | **Distributed among adjacent cities/subnets** | Confirms Run 6's provisional assumption; its governance findings stand as written. |
| **C** | **Hybrid** — trunk routes federal, spurs local | Hwy 37 is a trunk route, so this resolves *as A* for Run 6's purposes while leaving spur roads local. |

**What is blocked.** Highway 37's Phase 7 governance findings are **provisional until this is ruled** — they
are currently load-bearing for that pass's "enforcement without an enforcer" axis, which is one of its stronger
results. **This is the highest-stakes item in this queue.**

---

## ✅ DRQ-03 — Do highways get real-world inspiration picks? — **RULED 2026-08-31**

> ### The ruling, verbatim — both parts
>
> *"in terms of whether highways get real-world inspirational picks, I'm not really sure that's necessary,
> because a road will be dependant upon the context it's in, and that context will already be established by
> the worldbuilding"*
>
> **And, immediately after — the completing half:**
>
> *"not just the two locations it connects, but also what sort(s) of environmental setting(s) it runs through.
> A road's surroundings will be equally important as the sites it connects to each other"*

**Resolution: Option B — no per-highway inspiration picks.** The reasoning is sharper than the option framing
below and **the reasoning is the part that generalizes**: it is not that a corridor *lacks* a real-world basis.
It is that **a corridor's character is already fully determined by two things the worldbuilding has
established** —

| | Maps to |
|---|---|
| **What it connects** — its endpoints, junctions, and what flows between them | **G5**, network position |
| **What it runs through** — the environmental settings along its length, *equally important* | **G2**, physical & environmental constraint |

— so a separate inspiration pick would add a further influence to something not short of one.

> ### ⭐ The verbatim rule proved itself on its own first use, in miniature
>
> **This entry's first draft recorded only the first half of the ruling** and paraphrased the context as *"the
> places it connects."* **That paraphrase silently dropped the environmental half** — half the actual claim —
> until the developer supplied it. **`02` Path 6's rule that a paraphrased ruling is a lost ruling was written
> the same day and was validated within the hour, on the very first ruling this system received.** Recorded
> rather than quietly corrected.

**What this ratifies, and what it changes.**
- **Ratifies** ULM Run 6's actual practice: Highway 37 was derived from physical constraint, network position,
  and defining event, with a real-world comparable (the South Pole Traverse) used only for **physical
  texture** — road surface, convoy form, seasonal usability — never for character. **That split turns out to
  be exactly right, and is now the rule rather than an improvisation.**
- **Converges with a finding Run 6 reached independently**, from the opposite direction: that Phase 5
  (Relation & Geometry) is the *primary* phase for a Corridor, because a corridor is constituted by its
  relations. **The developer's reasoning and the cold pass's structural finding are the same claim arrived at
  two different ways** — the strongest kind of corroboration this project recognizes.
- **Changes** the standing expectation for G7 on Corridor-type locations: **an absent real-world inspiration
  is correct for the type, not a gap to be filled.**

**Deposited** *(per `03` §2 — a DECISION, deposited to the canon homes a consumer would actually check)*:
1. `Cities/Inspirational-Influences.md` — a scope note recording that highways deliberately have no entries,
   so a future session finds the *reason* rather than an absence.
2. `Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md` §G7 — the type-level rule.

**Registry row CGRM-015 → closed.** **Log entry: `Resolution_Log.md` CGRM-015.**

---

## ~~DRQ-03 — original queue entry, retained for the record~~

**The question.** Should the eleven highways receive `Inspirational-Influences.md`-style real-world picks, as
cities and districts already do?

**Why reserved.** By the project's own established nine-step pipeline, **inspiration picks are developer-
supplied** — the pipeline's own wording is that once the developer brings a location's list, the research is
then Claude's job. The picks themselves are an authored input.

**What canon already constrains.** `Inspirational-Influences.md` covers cities; `District-Inspirational-
Influences.md` covers districts. **No highway entries exist for any of the eleven.**

**Options.** **A** — per-highway picks, enabling Path 4 research for any future Corridor pass. **B** — no
picks; corridors derive from physical and network generators only. **C** — one shared set for Tepenian road
infrastructure generally, rather than eleven separate lists.

**What is blocked.** G7 (real-world inspiration) for any future Corridor-type location pass. **Run 6 worked
around this by selecting its own comparable — the real South Pole Traverse — and flagging it explicitly as
self-chosen rather than canon-designated.** That workaround is sound but should not become the silent norm.

---

## ✅ DRQ-04 — Hitchhiking-valid status for Highway 37 — **RULED 2026-08-31**

> ### The ruling, verbatim
>
> *"I would say, 'partially'. That being, people perhaps may hitchhike at specific nodes. That being, nobody
> 'stands on the side of the road holding up a sign'. Rather, it may be possible to wait inside of the Tepenian
> equivalent of something like 'diners' or 'gas stations' or 'rest stops' or something vaguely to that effect,
> and socialize with passers-through who make a stop there (for whatever reason). Granted, this may end up
> taking much longer to hitch a ride, but it's much more realistic than simply standing on the side of the road
> near the entrance to a highway"*

**Resolution: partial — via a general rule that turned out to be far bigger than the question asked.**

### ⭐ This ruling closed a different, older gap as a side effect

**`Highways.md` had carried a flagged open question since 2026-07-05:** *"Exact in-world reasoning for why
hitchhiking works on these particular routes (traffic density, cultural norms, freight-truck culture, something
else) not yet developed — flagged for future design."* **The ruling answers it directly and for the entire
network**, not just for Hwy 37. **This is the design proposal's "gaps closed for one scope generalize to
others" claim, validated on the system's second ruling.**

**The general rule now in canon:** hitchhiking is **node-based, never roadside** — you wait inside a stopping
place and get a ride by socializing with people who stopped for their own reasons. **In Antarctic conditions
the roadside version isn't merely unglamorous, it isn't survivable**, which supplies the physical reason the
node model is the only realistic one. Slower, and deliberately so.

**The emergent finding for Hwy 37 specifically**, produced by combining the ruling with Run 6's existing work:
**"hitchhiking-valid" is a claim about nodes, not pavement — and Hwy 37's entire interior has exactly one node,
Mountain Pass Airport.** Dome Fuji, Kunlun and Vostok are cities on the route rather than roadside stops; the
Hwy 22 dual-junction is a bare crossing. **So Hwy 37 is the hardest route in Tepenia to hitchhike without being
formally closed to it** — a single-point proposition, not a roadside one.

**Deposited:** `Highways.md` — the network-wide rule (replacing the 2026-07-05 open question) **and** Hwy 37's
own entry. **Registry row CGRM-016 → closed. Log: `Resolution_Log.md` CGRM-016.**

---

## ~~DRQ-04 — original queue entry, retained for the record~~

**The question.** Is Hwy 37 hitchhiking-valid?

**Why reserved.** A gameplay/canon flag the developer has set explicitly for other routes. Not derivable.

**What canon already constrains.** Hitchhiking is established as valid on **Hwys 7, 4, 110, 2, and the
Marambio–Rothera segment**; `Highways.md` marks several inline. **Hwy 37 carries no flag either way.**

**Options.** **A** — yes, consistent with other long routes. **B** — no. **C** — conditional/seasonal.

> **Worth knowing before ruling: Run 6 independently produced real in-fiction support for B**, without having
> been asked to. Its findings — a Band-0 corridor with no resident population along its length, an elevation
> profile that never returns below ~3,200 m after its first quarter, and a seasonal closure during the deep
> polar night — make casual hitchhiking implausibly dangerous in a way the coastal routes are not. **A cold
> pass arrived at a reason; the flag is still the developer's to set.**

**What is blocked.** Minor — a catalog and gameplay detail only.

---

## Ruled and closed

*(none yet)*

**When a ruling is made:** record it **verbatim** — a paraphrased ruling is a lost ruling, since the
developer's own wording repeatedly carries distinctions a summary drops — then deposit per `03` §2, close the
registry row, and log it.

---

## 🔵 DRQ-05 — {{Bunger Hills City}}: open questions left by the single-approach ruling

**Raised 2026-09-01, at developer instruction ("mark it for future review"). Not urgent; batched.**
**Context and full groundwork:** `Cities/Bunger_Hills_City_-_Development_Brief.md`.

**Already ruled and closed** *(recorded here so the queue is not misread as open)*: the city exists · Mirny
subnet · **single-approach from Casey** · **a named spur, not a numbered highway.**

### 5a — ⭐ Was the Denman crossing never attempted, or attempted and failed?

**The single-approach ruling leaves the western approach permanently unbuilt. It does not say why.**

| Option | What it makes Tepenia |
|---|---|
| **Never attempted** | A nation that read the survey and declined. Sober, unromantic |
| **⭐ Attempted and failed** | A nation that tried to bridge 11–16 km of crevassed, fast-moving ice over the deepest canyon on Earth **and lost.** Leaves an **abandoned works site on the western approach** — a considerable location, and a monument |

**"We tried, and the ice won" is a different national character from "we never bothered."** Both are good;
they are not the same. **Not decided.**

### 5b — The spur's parent highway *(minor)*

**Recommended: Hwy 110** — it is the coastal route that declined the coast here, and the spur is exactly the
deviation it did not make. Alternatives: Hwy 2, or the Hwy 110 × Hwy 2 junction complex. **All three meet at
Casey; the practical difference is small.**

### 5c — The city's name

**Candidates from the real site:** `Dobrowolski` · `Oazis` · `Bunger` · `Figurnoye` · `Edgeworth David`.
*Noting only that "Oazis" is the site's original station name and literally means oasis.* **The spur takes the
city's name automatically once settled** (cf. the Sayowa Spur), so this ruling resolves two things at once.

### 5d — ⭐ The walled-off ecosystem *(flagged by the developer as wanted)*

**Real-world basis:** there is open scientific speculation that **seals and penguins may be trapped behind the
Shackleton Ice Shelf as unique isolated populations**, with research ongoing into whether they still travel
between the marine inlets and the open sea. **The sea entered the oasis before ~7.7 ka BP**, so isolation on
that order is plausible.

**Why it is worth more than a nature note — it is three things at once:**
1. **A research industry** *(and it connects to Vostok's genetics program and the Cryptograph Helix
   bioinformatics thread).*
2. **A food resource** — but a **fragile** one. An isolated population can be fished out. It cannot be
   replenished.
3. **⭐ An ethical problem with no clean answer: a genetically unique population that is also edible**, sitting
   next to **the one city in Tepenia that is not short of anything.** A place with no scarcity problems, handed
   the one resource it could destroy by using.

**Not decided. Marked for exploration rather than ruling** — this may want a full pass rather than a verdict.

### ⏸️ DRQ-07 — Where do the Institutes' SATELLITE CAMPUSES go?

**Raised 2026-09-01 at developer direction. Structure settled, siting deliberately deferred.**
**Full groundwork:** `Cities/National_Medical_and_Care_Institutes.md` §"Throughput and Structure".

**Already settled:** national throughput *(~21,000 medical + ~3,400 robot-care graduates per year)* · **feeder
structure** *(foundational training distributed, advanced and qualifying stages at the main institute)* ·
**rolling intake and graduation** tied to seasonal transport windows · **cohort residency** *(you go to
Esperanza and do not come home for four years, because you cannot)*.

**Why satellites at all — it is NOT capacity.** One campus handles Esperanza's ~37,800 standing students
comfortably. **The drivers are ACCESS** *(a Kunlun student travels ~5,000 km)* **and RESILIENCE** *(every
medic originating in three cities means cutting one off kills people six to ten years later)*.

**Open questions:**
- **How many, at what level, and how distributed?** One per subnet? Per institute per subnet? A single shared
  foundational campus per region covering all three disciplines?
- **⭐ Which cities host them.** Candidates already suggested by canon: **Shirayuki** *(second education-export
  city — educ 20% against a 2.0% own need)*, **Mawson** and **Casey** *(subnet hubs)*, **Lazar** *(largest
  city; the Halley subnet's population center)*.
- **Co-located or separate disciplines?** Shared is cheaper; separate preserves the distinct traditions the
  three institutes are built on.
- **⚠ THE REAL TRADE-OFF: does a satellite dilute the bond?** The cohort-forged identity exists *because*
  students are sealed in together for years. **Distribute foundational training and that weakens.**
  **Resilience and identity pull against each other, and the siting decision is where that gets settled.**
- **The plateau problem.** Vostok, Kunlun and Dome Fuji are least able to send students *and* least able to
  host a campus. **They may simply be permanently dependent — a fact worth using rather than solving.**

---

### DRQ-06 — Are either humans or robots EXCLUDED from particular job roles?

**Raised 2026-09-01. ⏸️ Explicitly open — the developer has stated they have not decided and currently have
no view.** *"I honestly haven't figured that out yet. I currently have no idea."*

> **⚠ BLOCKS NOTHING. Do not chase this to close it.** Industry *demand* is keyed to population and is
> unaffected by who staffs the roles *(see `Cities/Division_of_Industry/08` §4.4)*. **The arithmetic runs
> identically whichever way this lands.**

**⭐ And the answer is probably not a single rule — it is a distribution.** Canon already establishes that
cities differ sharply on exactly this axis: **Kunlun and Dome Fuji forbid humans outright.** So this may have
**38 different answers rather than one** — **differentiation, not inconsistency** — resolving gradually, city
by city, as culture work proceeds. **No central ruling is required, now or possibly ever.**

**Where the question actually bites** *(everywhere else — power plants, water treatment, construction, admin —
probably nobody has an opinion)*:

- **⭐ The mirror pair the setting has already put on the table without resolving either:**
  **(a)** The **Sinheung Institute** trains counselors *"whose discipline is a robot's inner life."* Somebody
  provides intimate emotional care **to** robots — is that somebody a robot or a human?
  **(b)** Its inverse: **robot maintenance is physically invasive** — opening a body, servicing internals.
  **The robot equivalent of surgery.** Who is permitted to do that?
- **Obstetrics and midwifery** — a robot delivering human infants.
- **Childcare** — robots raising human children.
- **Mortuary work** — robots handling human dead.

**Relevant standing canon:** egalitarian human-robot relations skewed robot · Kunlun/Dome Fuji forbid humans ·
robots have religions, arts, drinking culture, counselors and clothing · robot/human love is a stated project
north-star. **Nothing in that set forbids either population from any trade; it simply has never been asked.**

### ⭐ PARTIAL ANSWER — 2026-09-01. Not an exclusion. A PREFERENCE GRADIENT.

**The first real answer to this question arrived sideways, while setting robot maintenance rates.**
`[CGRM 2026-09-01 · Path 6 · developer ruling]`

> *"A robot seeking their equivalent of 'medical attention' will probably (though perhaps not always, not
> invariably) want to be treated by another robot, simply due to their own familiarity with robot physiology.
> …a human will probably also want to be treated by a robot, though for different reasons, being: the
> knowledge that a robot is able to reach a much finer degree of exacting precision than a human (with human
> hands)."*

**⭐ Both populations prefer robot practitioners — for different reasons.** Robots for **familiarity**
*(shared physiology)*; humans for **precision** *(finer motor capability than human hands)*.

> ## **So medicine in Tepenia skews robot, for everyone.** **Not a rule, not an exclusion — a gradient**,
> and explicitly "not always, not invariably," which leaves room for individual variation and for cities that
> do it differently.

**Three consequences:**
1. **Demand is unchanged; staffing is not.** The human healthcare sector (54 per 1,000 humans) would be
   substantially robot-staffed. **This is the demand/supply split doing exactly what it was separated for.**
2. **⭐ A reversal worth using: robots, whose leisure was once granted by loving humans on Upper Earth, are now
   the ones providing the care humans depend on.** *(See `Robot_Biology_and_Culture/
   Robot_Physiology_and_Cultural_Practices.md` §Downtime, Recharging and Leisure.)*
3. **It also fixed the maintenance rate.** Robot precision is why B3 sits at 1-per-80 rather than nearer the
   human 1-per-18.5 — **high-touch care delivered by high-efficiency practitioners.**

**Still open:** everything else on this question — obstetrics, childcare, mortuary work, and whether any city
diverges. **The gradient is established for medicine only.**

---

### 5e — What 43 years of dormancy did to the place

**Now load-bearing rather than decorative:** hard access is what explains the emptiness, so the dormancy is no
longer a curiosity — it is the reason the site was available. **Every other Tepenian city was founded on
something working.** This one was founded on a place that had been dark for two generations. **The most
promising unexplored thread in the brief; not a ruling, a pass waiting to happen.**
