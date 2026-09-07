# Cultural Synthesis Techniques

**A generative toolkit for building the culture of any specific place.** Scoped deliberately general — Concordia
districts, the 35 outer Tepenian cities, DLC locations, or a location in any future project. Sibling to
`Real-World_Basis_Extrapolation_Method.md`, which supplies raw material; this file supplies the *operations* to
perform on it.

**This repo is a CRPG.** The end consumer is a **player moving through the space**, not a reader of design
documents. See §0b.

---

## ⚠ How to read this file — the single most important instruction

Every technique below is a **question with a structure**. It is **not** a result to reproduce.

**Do not carry another location's answers into a new one.** Each technique includes a *divergence table*
showing the same operation producing genuinely unlike outputs across different kinds of place. That table is
the point of the entry — more than any single worked example.

**The self-check:** if two locations run through the same technique produce answers of a *similar shape*, at
least one of them is wrong. A technique that yields a worn keepsake token in one district and a worn keepsake
token in the next has not been applied; it has been copied.

Worked examples cite Concordia's Cancer district, the first location run through the full method. They are
marked **[one instance]** and kept deliberately brief. Cancer is *an* answer, never *the* answer.

---

## 0. The governing filter — Characteristic Plausibility

> **Is this internally consistent, and characteristically aligned with this specific place and its culture —
> without being constrained to repeat what already exists?**

Two failure modes:

- **Uncharacteristic.** An element that doesn't belong to *this kind of place*. In a district full of factories,
  bars and pubs with live-music nights are entirely reasonable — nobody needs to have pre-established them. A
  giraffe is not. Neither is a guy riding a unicycle.
- **Over-constrained.** Refusing to produce anything not already in canon, yielding a sterile place that merely
  re-labels its own existing material.

Target the space between: **new, but characteristically inevitable in hindsight.** A player walking into it
should think *"of course this is here"* — not *"where did that come from?"* and not *"I've seen this in every
other district."*

New religions, factions, institutions, and discoveries fitting no pre-existing category are legitimate and
welcome. Established categories are a **floor, not a ceiling**. The only obligation on a genuinely new thing is
that it be named, defined, and cross-referenced from wherever its kind normally lives, so it enters canon
cleanly.

---

## 0b. The player-facing test

Before accepting any finding, ask **how a player would encounter it.** Prefer findings answering in more than
one channel: **seen** (environment, crowd behavior, dress) · **heard** (ambient audio, overheard talk) ·
**entered** (a real location) · **handled** (an item) · **spoken** (an NPC can mention or complain about it) ·
**done** (a behavior the player can join, refuse, or violate) · **hooked** (quest, check, reputation,
companion reaction).

**A finding that can only be *read about* is weak.** Push it until it has a physical or behavioral expression.

**Corollary — the violation is usually the gameplay.** For any custom, the interesting mechanical question is
what happens when someone conspicuously *doesn't* observe it.

---

## ⭐⭐⭐ WHERE THE ANSWERS COME FROM — **the per-technique source map**

> ### ⛔ ADDED 2026-09-06. **Every technique below asks a question ABOUT a location. This says which file answers it.**
> **Before this existed, FOURTEEN of the seventeen techniques named no source of any kind.** *They referred to
> "this place's established character" as a concept — while the four techniques that consume EXTERNAL inputs
> all carried real addresses.* ⭐ **The pattern was exact, and it was structural rather than accidental:** *this
> file was written when "established character" meant a district pass in a known folder, so that material never
> needed an address.* ⛔ ***A technique that cannot name its input is run from whatever the session happens to
> remember.***

**⚠ PATHS BELOW ARE RELATIVE TO `Worldspace/Locations-and-Levels/`** — **stated rather than assumed**, because
this file's sibling already shipped one address that resolved to nothing. *(`M-117` — **"a name is not an
address"** — on the most safety-critical line in `Real-World_Basis_Extrapolation_Method.md`.)*

### 1 · The location's completed pass — where it lives

| Location type | Its pass |
|---|---|
| ⭐ **A city** *(ULM)* | **`Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/<Subnet>/<City>/`** |
| **A Concordia district** | **`Concordia-City/Districts/`** — *that district's own pass files, per the district runbook* |
| **Any other location** *(subnet · structure · highway · vessel · ruin)* | *The same ULM output tree, under its own type folder* |

### 2 · ⛔ THE ULM WRITES **PHASES** INTO **STEP**-NUMBERED FILES. **The two numberings do not match.**

| What you want | The file |
|---|---|
| **Phase 0 — FRAME** | `00_Frame.md` *(Step 0)* |
| **Phase 1 — CONSTRAINT & CAPABILITY** *(the spine · the capability reading)* | ⭐⭐ **`02_Spine.md`** *(Step 2)* — ⛔ **NOT `01_`** |
| **Phases 2 – 10** | `04_Phase_02_*.md` … `04_Phase_10_*.md` *(all written at Step 4)* |
| ⚠ **The inherited-canon audit** — *established-but-unexplained material* | ⭐⭐ **`01_Inherited.md`** *(Step 1)* — **not a phase, and two techniques need it** |
| Conflicts found and resolved against prior datasheets | `05_Reconciliation.md` *(Step 5)* |
| What was researched, and what each pick actually yielded | `03_Research.md` *(Step 3)* · `Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/<City>_Research_Log.md` |
| What the pass could NOT establish | `10_Readiness_Check.md` *(Step 10)* — ⭐ *read it before recording a null; a blocked check is not an absence* |

> ### ⚠ `01_Inherited.md` IS THE ONE MOST LIKELY TO BE SKIPPED
> **It reads as a preamble — an audit of what was already true before the pass started.** ⛔ **Techniques 5 and
> 7 are built directly on it**, because both ask about material the location *has* without having *explained*,
> and that is exactly what a canon-inheritance audit records. **Neither technique can run from the phases alone.**

### 3 · The map

| # | Technique | Read |
|---|---|---|
| **1** | Bounded Personal Franchise | `04_Phase_03_Surface_and_Texture` · `04_Phase_08_Making` · `04_Phase_04_Ordinary_Life` |
| **2** | Failure State of the Core Value | `04_Phase_06_Meaning` *(the promise)* · `02_Spine` *(what it cannot deliver)* |
| **3** | Universal Micro-Practice | `04_Phase_06_Meaning` · `04_Phase_04_Ordinary_Life` |
| **4** | Ambiguous Universal Object | `04_Phase_02_Composition_and_Arrival` · `04_Phase_05_Relation_and_Geometry` · `04_Phase_06_Meaning` |
| **5** | Retroactive Mechanism | ⭐ **`01_Inherited`** · `04_Phase_03_Surface_and_Texture` |
| **6** | Necessity Before Meaning | `04_Phase_06_Meaning` · `04_Phase_02_Composition_and_Arrival` · `00_Frame` |
| **7** | The Surviving Witness | ⭐ **`01_Inherited`** · `04_Phase_07_Order` · `04_Phase_03_Surface_and_Texture` · `04_Phase_10_Catalog` |
| **8** | Asymmetric Record-Keeping | `04_Phase_07_Order` |
| **9** | The Non-Thematic Export | `04_Phase_08_Making` · `04_Phase_05_Relation_and_Geometry` |
| **10** | Membership by Unremarked Persistence | `04_Phase_08_Making` · `04_Phase_04_Ordinary_Life` · `04_Phase_09_Populations` |
| **11** | The Negative Image | `04_Phase_06_Meaning` · `04_Phase_07_Order` — ⚠ *and `07_QA_Gates` for whether Gate 7d was blocked* |
| **12** | Native Before Transplanted | `04_Phase_02_Composition_and_Arrival` · `04_Phase_09_Populations` |
| **13** | The Unused-Tier Mine | ⭐ `<City>_Research_Log.md` · `03_Research` · `04_Phase_10_Catalog` §B — **the SPEND record** |
| **14** | The Population Share Check | *Runs ON every finding in the pass; needs no source of its own* |
| **15** | Borrowed Form | `04_Phase_02_Composition_and_Arrival` — ⛔ **the district diaspora file has NO city equivalent; see the technique** |
| **16** | The Unrecognized Instrument | ⭐⭐ **`02_Spine`** *(= Phase 1)* — **the capability reading** |
| **17** | The Zodiac Lens | **Phases 0–10 entire** — *and see the technique on why it must be written out, not pointed at* |

> ### ⛔ AND ONE STANDING WARNING ABOUT READING A COMPLETED PASS
> **A pass file states what that location established. It does NOT state what a technique should conclude.**
> ⭐ **The techniques are still questions.** *Reading `04_Phase_06_Meaning` tells you what the place's core value
> is; it does not tell you what happens when that value cannot be delivered — that is technique 2's own work,
> and it is not in the file.*


---

## ⭐⭐⭐ THE OTHER HALF OF THE LAW — **WHAT IT WAS NEVER BLOCKING.** *(Developer, 2026-09-06. Added here 2026-09-06.)*

> ### ⛔⛔ THE GPS LAW LIVES IN `Real-World_Basis_Extrapolation_Method.md` AND IN THE CANON REGISTRY. **THIS FILE NEVER CARRIED EITHER HALF OF IT.**
> ⭐ **It is reproduced here because TWO TECHNIQUES BELOW ARE UNRUNNABLE WITHOUT THE UNLOCK** — **`12` Native
> Before Transplanted** *(which asks what arrived versus what grew)* and **`15` Borrowed Form** *(which asks
> what the incoming populations carried with them)*. ⛔ ***A reader holding only the prohibition refuses ALL
> ethnic and origin material — which is not obedience but a MISREADING, and it produces placeless locations
> that could be anywhere, plus two dead techniques.***

**Developer's own words, verbatim:**

> ### **"You shall NOT incorporate 'Russian heritage' into the establishment of the city of [X]… Once the population composition has been established, then, yes, you can start incorporating aspects of Japanese (or Korean) culture, traditions, history, social norms, etc., because [X] is a fundamentally Japanese city (or [Y], being a fundamentally Korean city). *THAT'S* the purpose of the 'GPS purposes only' Law."**

| ⛔ What the law blocks | ✅ What the law was never blocking |
|---|---|
| ***The REAL SITE'S operator nationality bleeding into the place*** — *its builders, its flag, its lineage, its abandonment, its fate* | ⭐⭐ **THE PLACE'S OWN ETHNIC CHARACTER, which comes from its FOUNDING POPULATION and is canon** |

> ## ***THE LAW EXISTS SO A PLACE IS CHARACTERIZED BY WHO LIVES THERE, NOT BY WHOSE SITE IT OCCUPIES.***
> **It is a rule about PROVENANCE, not a rule against ethnicity.**

### ⭐ IT IS A SEQUENCING RULE, NOT A REPEAL — **the prohibition above is UNCHANGED**

| Stage | What is permitted |
|---|---|
| **BEFORE composition is established** | ⛔ **GPS FACTS ONLY.** *You may not infer **who lives somewhere** from national character, temperament or cultural reputation.* **This is the whole point of the prohibition and it is untouched** |
| ⭐ **AFTER composition is established** — *origins named, proportions settled* | ✅ **Origin-ethnicities and ethnic-cultures MAY be taken into consideration.** *The populations are canon; what they carry is then legitimately in scope* |

> ### ⭐⭐ THE DISTINCTION THAT MAKES THIS SAFE — **two different generators, and the unlock touches only one**
> | | |
> |---|---|
> | ⛔ **`G7` — the SITE's real-world basis** | **UNCHANGED. GPS PURPOSES ONLY — a coordinate, never a cause, an identity, or a history.** ⚠ *And that covers the real site's **lineage, abandonment and vacancy**, not merely its nationality* |
> | ✅ **`G8` — the POPULATION's composition** | ***This is what the ruling unlocks*** |

### ⛔⛔ NEITHER EXTREME IS THE ANSWER — **composition names the STOCK; time and place produce the CULTURE**

| ⛔ Too little | ⛔ Too much | ✅ The operation |
|---|---|---|
| **Refusing all ethnic material** — *placeless locations that could be anywhere* | **Transplanting the source culture intact** — *"a costumed version of somewhere real"* | ⭐⭐ ***Take the origin culture as the STARTING STOCK, then apply local divergence to it*** |

**⭐ THE DIVERGENCE OPERATOR — the checklist:** **time · separation · local environmental setting · local
struggles and hardships · local goals · local sensibilities and habits.**

> ⛔⛔ **DO NOT REASON FROM THE ELAPSED TIME.** *Developer:* ***"Don't think in terms of '250 years' of
> outcomes. Just process the data purely on its own terms."***

### ⭐ AND ORIGIN IS ANCESTRY, NOT IDENTITY — **the Acts**
**`Act 1`** *(2564 → early 2600s)*: people are still *"X who live in Antarctica."*
**`Act 2`** *(~late 2600s / early 2700s on)*: they are **properly Tepenian — origin is ancestry, not identity.**
⚠ **The Second Interwar spans both Acts and is mostly Act 2.** ⭐ ***Differentiate locally; converge nationally.***

📎 **Full statement: `00_RUNBOOK.md` `C.9b` *(sequencing)* · `C.9c` *(what the law is for)* · `C.9d` *(the
divergence principle)*, and the universe-wide original in the canon registry at `§B`.**

---

## 1. The Bounded Personal Franchise

📍 **Read:** `04_Phase_03_Surface_and_Texture.md` · `04_Phase_08_Making.md` · `04_Phase_04_Ordinary_Life.md` — ***what the place is physically made of, and how people work in it.*** *(Source map above.)*

**Architecture.** Every inhabited place needs at least one domain where an ordinary individual holds absolute,
unarguable authority — and it is far more vivid when the limit is **physical and natural** rather than
administrative. A permit boundary is forgettable; a boundary set by a body or a tool is not.

**The question.** *What is the smallest unit of the world an ordinary resident here fully controls, and what
concrete physical fact defines its edge?*

| Kind of place | Plausible franchise | Its natural limit |
|---|---|---|
| Dense residential | A stretch of exterior wall | How far an arm reaches from your window |
| Heavy industry | Your own bench, machine, or rig | The machine's own footprint; your shift |
| Subterranean / maintenance | A length of passage you personally keep | Where your section meets the next keeper's |
| Information economy | A channel, handle, or frequency | Bandwidth allocation; who answers to it |
| Market / trade | A pitch | The chalk square; the hours you hold it |
| Frontier / expedition | A claim or cache | What you can physically reach and return from |
| Performance | A slot, a stage-corner, a recurring hour | The length of a set; the venue's schedule |

**Why it personalizes.** Both the domain *and its limit* fall out of what the place is physically made of and
how people work in it. Change the substrate, change the franchise.

**Player value.** Turns undifferentiated surfaces into a readable field of individual human decisions.

**[one instance]** Cancer: the **Window Reach** — alter the wall as far as your arm reaches from your own
window, no further.

---

## 2. The Failure State of the Core Value

📍 **Read:** `04_Phase_06_Meaning.md` — *the central promise* · `02_Spine.md` — *what the place structurally cannot deliver.* *(Source map above.)*

**Architecture.** Every place organized around a strong value meets a condition where that value **cannot be
delivered**. A culture that has never confronted its own failure state reads as propaganda. Where it has, and
built something around it, is usually the place's moral center — and its best quest territory.

**The question.** *What is this place's central promise; under what circumstance does it become impossible to
keep; what institution grew up around that circumstance; and does the culture ritualize the failure or refuse
to?*

| If the core value is… | It fails when… | Which tends to produce… |
|---|---|---|
| Continuation / memory | The people who would continue it run out | An inheritance or adoption mechanism, and a place where the unclaimed wait |
| Permanence / record | The record is destroyed or can't be verified | A class of people whose status is unprovable, and a dispute process |
| Recognition / performance | Nobody is watching, or you age out | A quiet tier below the visible one; managed decline |
| Transformation / confrontation | The subject doesn't survive the process | A population of incomplete outcomes, and an argument about method |
| Neutrality / arbitration | You are forced to take a side | A doctrine of deliberate non-resolution, and resentment on both sides |
| Productivity / self-reliance | You can no longer work | A dependency nobody will name; euphemism as institution |
| Secrecy / discretion | Something must be disclosed | A sanctioned leak channel; ritualized deniability |

**The refusal is often the strongest half.** A culture that declines to make its worst outcome comfortable —
no consoling ritual, no clean closure — says more than any ceremony.

**[one instance]** Cancer: continuation fails when the keepers run out → strangers adopt lapsed routines;
unadopted ones wait indefinitely somewhere that never discards anything; and the district pointedly never
developed a rite to make final lapse feel acceptable.

---

## 3. The Universal Micro-Practice

📍 **Read:** `04_Phase_06_Meaning.md` · `04_Phase_04_Ordinary_Life.md` — ***the place's real priority***, which is what the practice encodes. *(Source map above.)*

**Architecture.** The highest-leverage device for a lived-in feel: a behavior that is **very short, extremely
frequent, near-universal across roles, and almost contentless**. Residents do it unconsciously — invisible to
them, conspicuous to outsiders.

**The question.** *What tiny thing does everyone here do many times a day without thinking, that a visitor
would notice within an hour and misread?*

| If the place's real priority is… | The micro-practice tends toward… |
|---|---|
| Settling before acting | A shared pause before beginning |
| Mutual acknowledgment | A specific greeting, nod, or naming |
| Discretion | A glance or signal checking whether it's safe to speak |
| Readiness / safety | Touching your tool, rail, or seal on entering |
| Verification | Confirming a number, tag, or identity aloud |
| Status legibility | A deference gesture calibrated to rank |
| Endurance | A count, a breath, a marked step |
| Impermanence | Something deliberately unmade or wiped at each start |

**Constraints that make it work:** seconds not minutes; no equipment; no belief required, so believers and
non-believers perform it identically; and it should be what a displaced resident misses most elsewhere.

**Player value.** Cheap to animate, reads instantly on every ambient NPC, and becomes a live social mechanic
the moment the player can conspicuously skip it.

**[one instance]** Cancer: a brief settling pause before any shared task.

---

## 4. The Ambiguous Universal Object

📍 **Read:** `04_Phase_02_Composition_and_Arrival.md` · `04_Phase_05_Relation_and_Geometry.md` · `04_Phase_06_Meaning.md` — ***what the place is shaped by.*** *(Source map above.)*

**Architecture.** One item, carried by a large share of the population, whose **form is standard but whose
meaning is individual and never asked about**. Cheap and enormously productive: one asset, and every bearer
silently has a story that costs nothing until someone needs it.

**The question.** *What one object would most people here plausibly carry, in a shared form, for reasons that
differ completely person to person — and what's the etiquette around asking?*

| If the place is shaped by… | The object tends to be… |
|---|---|
| Separation | Something split or paired, half held by each |
| Long service / endurance | Something worn smooth, its wear the whole point |
| Transformation | Something visibly altered, resurfaced, or re-made |
| Records and standing | A countersigned chit, stamped tag, or sealed slip |
| Physical risk | Something you'd leave behind if you didn't come back |
| Debt and obligation | A marker that changes hands and accrues marks |
| Concealment | Something that looks like an ordinary tool and isn't |

**Player value.** One reused art asset that promises depth on every NPC; a natural dialogue opener; a giftable
item; a quest token.

**[one instance]** Cancer: half of a deliberately broken small object, worn at the collar; meanings vary
entirely by bearer and nobody asks.

---

## 5. Retroactive Mechanism

📍 **Read:** ⭐⭐ **`01_Inherited.md`** *(Step 1 — the inherited-canon audit)* · `04_Phase_03_Surface_and_Texture.md`. ⛔ **This technique CANNOT run from the phases alone** — *its input is material the location has without having explained, and that is what the inheritance audit records, not what a phase writes.* *(Source map above.)*

**Architecture.** Settings accumulate **stated effects with unstated causes** — atmosphere recorded because it
felt right, never mechanically explained. Supplying a concrete physical cause turns atmosphere into
infrastructure, which is what makes a place feel engineered rather than described. It usually generates a
second-order consequence for free.

**The question.** *What is established as simply true here that nothing explains? What physical system would
produce exactly that — and what else would that system also cause?*

Unexplained effects worth hunting for: persistent light quality · a smell · a temperature or humidity anomaly ·
a sound with no named source · a recurring hazard · why one area is always empty · why something never freezes,
or never dries.

**Why it personalizes.** The candidate causes are constrained by the place's own industry, geography, and
technology — an agricultural district and a foundry district cannot explain the same haze the same way.

**Player value.** Atmosphere becomes a structure the player can find, enter, climb, sabotage, or repair.

**[one instance]** Cancer: a long-established ambient haze finally explained by the district's own
plant-and-air infrastructure — which then also produced a new smell and an unresolved question about where the
vented air goes.

---

## 6. Necessity Before Meaning

📍 **Read:** `04_Phase_06_Meaning.md` *(the rule)* · `04_Phase_02_Composition_and_Arrival.md` · `00_Frame.md` *(the founding conditions that could have forced it).* *(Source map above.)*

**Architecture.** Cultures present aesthetic and moral rules as *chosen*. It is nearly always better if the rule
was **forced by a practical constraint** and moralized afterward. Reversing the causality makes a place feel
accumulated rather than authored.

**The question.** *This place holds an aesthetic or ethical rule strongly. What cheap, urgent, practical
necessity could have forced exactly that, before anyone attached meaning to it?*

Constraint families to reach for: what was affordable · what could be built fastest · what survived the climate ·
what one founding trade already knew how to make · what a shortage forced · what a disaster made mandatory.

**Why it personalizes.** The forcing constraint comes from founding conditions, which differ per place — and
the *rationalization* differs again, because each culture moralizes its constraint in its own idiom.

**[one instance]** Cancer: a no-straight-lines aesthetic rule, re-derived as the cheapest fast warm shelter its
founding generation could build — the curve came first, the virtue was assigned later.

---

## 7. The Surviving Witness

📍 **Read:** ⭐⭐ **`01_Inherited.md`** *(what canon leaves unexplained or unrecorded)* · `04_Phase_07_Order.md` · `04_Phase_03_Surface_and_Texture.md` · `04_Phase_10_Catalog.md`. ⛔ **Same dependency as technique 5** — *the phases alone do not record a silence.* *(Source map above.)*

**Architecture.** Where a place has suppressed, lost, or destroyed a record, **another medium almost always
still testifies** — unintentionally, and therefore more credibly.

**The question.** *What does this place not talk about, or no longer have records of — and what physical thing
still bears witness, precisely because nobody thought of it as a record?*

Media that testify: building stock from the relevant era · tooling and machine wear · a route people avoid ·
a naming convention that stops or changes · a skill nobody can account for learning · repairs that don't match ·
an inventory that doesn't balance · a population gap.

**Player value.** Investigation content in its natural form — a truth deduced from the environment rather than
confessed.

**[one instance]** Cancer: written records of a triage crisis were destroyed, but the emergency-era buildings
still stand, and their construction style is culturally legible as an admission.

---

## 8. Asymmetric Record-Keeping

📍 **Read:** `04_Phase_07_Order.md` — *what the place inscribes, and what it conspicuously does not.* *(Source map above.)*

**Architecture.** What a culture makes **permanent** versus what it **never writes down** is more revealing than
either alone. The finding is the *gap*.

**The question.** *What does this place inscribe or archive permanently, what does it conspicuously never
record, and what would an outsider wrongly conclude from the surviving record alone?*

| A place may permanently record… | While never recording… |
|---|---|
| Successes and cures | Failures and quiet reassignments |
| Debts owed | Gifts given |
| Arrivals | Departures and exits |
| Lineage and service | Purchases and prices |
| Decisions | Who argued against them |
| Names | Numbers, or vice versa |

**[one instance]** Cancer: successes are permanently posted in public; failures are recorded nowhere at all.

---

## 9. The Non-Thematic Export

📍 **Read:** `04_Phase_08_Making.md` *(by-products and surplus)* · `04_Phase_05_Relation_and_Geometry.md` *(what actually flows outward).* *(Source map above.)*

**Architecture.** A place defined by one strong function drifts toward monoculture. At least one export that is
**ordinary, emotionally neutral, and unrelated to the headline function** gives it presence elsewhere without
exporting its theme, and proves the economy is real rather than allegorical.

**The question.** *What does this place make and send outward that has nothing to do with what it's famous for
— something a person elsewhere owns without thinking about its origin?*

**Where to look:** by-products of infrastructure the place runs for other reasons; surplus from something it
grows, casts, cuts, or refines anyway; a skill its main trade requires that is useful in miniature.

**Player value.** A tradeable object carrying a place's identity outward, and a quiet way for the player to
recognize provenance.

**[one instance]** Cancer: a cast metal household object, made by a real local trade with no connection to the
district's headline function, traded citywide and entirely unsolemn.

---

## 10. Membership by Unremarked Persistence

📍 **Read:** `04_Phase_08_Making.md` · `04_Phase_04_Ordinary_Life.md` · `04_Phase_09_Populations.md` — ***the local economy***, which supplies the conversion mechanism. *(Source map above.)*

**Architecture.** How an outsider becomes a local is deeply characterizing, and the strongest versions are
**mechanisms rather than ceremonies** — derived from the local economy, with no announcement and often no
awareness that it has happened.

**The question.** *What does this place need done that a newcomer can start immediately — and at what point
does still doing it convert them into a resident?*

| Local economy | Plausible conversion mechanism |
|---|---|
| Continuous labor needs | A work term; you're a local once you're still there after it |
| Shift/rotation based | Having taken a full rotation, including the bad one |
| Seasonal or hazardous | Having survived one cycle in place |
| Credit or debt based | Having cleared a first obligation, or been extended one |
| Reputation based | First time someone vouches for you unprompted |
| Guild/craft based | First independent piece accepted without correction |
| Secrecy based | First time you're told something without being warned to keep it |

**Player value.** A reputation on-ramp that works without a quest ever announcing itself.

**[one instance]** Cancer: placed into ordinary needed labor on arrival; residency is simply what has happened
once the term ends and you're still doing it.

---

## 11. The Negative Image

📍 **Read:** `04_Phase_06_Meaning.md` · `04_Phase_07_Order.md` — *what the place requires of every resident.*
> ⚠⚠ **CHECK `07_QA_Gates.md` FOR GATE `7d` BEFORE RECORDING A NULL.** **`7d` is the counterculture canon check, and it can come back BLOCKED when the owning canon file is withheld wholesale.** ⛔ ***A blocked check is not an empty result*** — *record it as blocked, exactly as the pass did, and do not report "this place has no counterculture" on the strength of a source you were not allowed to open.*

**Architecture.** A counterculture is not generic dissent — it is the **precise negative** of what the dominant
culture requires of everyone. Derived, it's sympathetic and inevitable; invented freely, it's generic rebels.

**The question.** *What does this place require of every resident, consented to or not — and who cannot, or
will not, give it? What have those people built instead?*

| If the place compels… | Its counterculture is… |
|---|---|
| Visibility | People who refuse to be seen or logged |
| Permanence | People who refuse to be recorded, or who deliberately move |
| Performance | People who refuse to perform, or perform only privately |
| Transformation | People who insist on remaining exactly as they are |
| Productivity | People who publicly decline to be useful |
| Consensus | People who argue as a matter of principle |
| Discretion | People who say things out loud |

**Keep it sympathetic, not criminal** — these are people the demand doesn't fit, not bad people.

**Player value.** A second, opposed faction inside one district: separate questgivers, separate reputation, and
a real choice about whose side of a local argument to take.

---

## 12. Native Before Transplanted

📍⭐ **THIS TECHNIQUE DEPENDS ON THE GPS LAW'S UNLOCK** *(see the section above)*: once composition is established, **origin-ethnicities and ethnic-cultures ARE admissible material.** ⛔ *Without that, "setting aside everything incoming populations brought" has nothing on either side of the subtraction.*

📍 **Read:** `04_Phase_02_Composition_and_Arrival.md` *(what arrived)* · `04_Phase_09_Populations.md` *(what is here now)* — **and the divergence operator's own output, wherever the pass applied it.** *(Source map above.)*

**Architecture.** In any setting with migration, it is easy to mistake **what arrived** for **what grew**. A
place whose whole culture is its immigrants' cultures has no culture. Develop the layers separately, then let
them interact.

**The question.** *Setting aside everything incoming populations brought — what did this place develop on its
own? Only then: how do the two layers now sit together?*

**Caution.** A real and easy failure: in Concordia's district work, transplant records were mistaken for
coverage, leaving an entire tier of categories unwritten.

---

## 13. The Unused-Tier Mine

**Architecture.** Where a setting keeps tiered real-world reference picks (Primary / Secondary / Supporting),
**lower tiers reliably outperform the top tier** — Primary picks get absorbed early into a location's identity
summary and spent, while lower tiers sit unexamined and still hold unspent specificity.

**The question.** *Which of this location's picks has nothing in the existing material actually derived from
it?* Start there.

> ### ⛔⛔ THE PREMISE INVERTS ONCE THE LOCATION HAS A COMPLETED PASS — **corrected 2026-09-06**
> **This technique was audited 2026-09-05 with the note: *"the 'which picks are spent' record does not exist
> for cities… at first pass the answer is 'all of them are unused' — maximum yield."*** ⛔ ***Both halves of
> that expire the moment a location's own pass runs*** — **a ULM pass researches and spends picks; that is
> `Step 3`'s whole job.**
>
> ✅ **AND THE "MISSING" SPEND RECORD IS NOT MISSING.** ***It is the location's own research log*** —
> `Real-World_Basis_Extrapolation_Method.md`'s **Step F**, which is specified to carry *"a fact-by-fact table
> of what came back → which finding it became."* ⭐ **That is a usage record by definition.** *The two
> availability audits were written the same day as siblings, and neither noticed that one's Step F closes the
> other's declared gap.*
>
> | Before a pass | After a pass |
> |---|---|
> | ✅ **"All unused" is a safe default** — *maximum yield, run it early* | ⛔ **Check the log first.** *A picked-over location may return a **null**, and a null here is a legitimate result under "Using this file" item 5 — not a failure, and not a reason to manufacture a weak find* |
>
> 📍 **The spend record:** `Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/<City>_Research_Log.md`
> *(cities)* · the pass's own `03_Research.md` and `04_Phase_10_Catalog.md` §B. ⚠ **A location with no research
> log has genuinely not been mined yet** — *the absence is informative, not an obstacle.*

**[one instance]** Four of eight Cancer picks had never been used; three of those four produced the district's
strongest material. Per-pick table in `Real-World_Basis_Extrapolation_Method.md`.

---

## 14. The Population Share Check

**Architecture.** Any statement about "what this place is like" implicitly claims a population share. Source
material is frequently written about a **narrow role, ritual, or context**, and reusing it as the general answer
is the most common way a location's culture goes wrong.

**The question, on every claim.** *Does this describe the general population, or one profession's, ritual's, or
context's version? If the latter, what does everyone else do?*

**Why it matters for a CRPG.** The general answer is what the player meets constantly — every ambient NPC,
every crowd, every random door. The narrow answer is what they meet in one building. Reversed, a district feels
like a themed attraction.

Full discipline in `Concordia-City/Districts/Phase_Instructions/00b_General_Population_Discipline.md`.

---

## Using this file

1. **Research first** (`Real-World_Basis_Extrapolation_Method.md`), all tiers, once, up front.
2. **Run the techniques as prompts.** The answer must come from this specific place's established character.
3. **Check the divergence tables before writing.** If your answer resembles another location's answer to the
   same technique, discard it and go back to this place's own material.
4. **Filter through §0 and §0b.** New is good. Uncharacteristic is not. Unplayable is weak.
5. **Not every technique fires everywhere.** A technique that produces nothing is a legitimate result — record
   the null rather than manufacturing a weak answer. Expect several nulls per location; a place where all
   fourteen fire is a place someone has over-written.
6. **Genuinely new things that fit no category are kept**, named, and cross-referenced. That is the method
   working.
7. **Add to this file.** Any new operation that produced a good result and could plausibly produce a
   *different* good result elsewhere gets extracted into its architecture, its question, its divergence table,
   and one brief instance.


---

## Technique — Borrowed Form *(added 2026-08-29, from the Circuit)*

📍⭐⭐ **THIS TECHNIQUE IS THE UNLOCK'S SHARPEST USER** — *it asks what the incoming populations' OWN home traditions were.* ⛔ **Under the prohibition read alone, that question is refusable and the technique is dead.** ✅ **Composition first, then the cultures those populations actually carry** *(see the GPS section above)*.

📍 **Read:** `04_Phase_02_Composition_and_Arrival.md` — *the incoming populations and what each carried.* *(Source map above.)*
> ### ⛔⛔ THE ADDRESS BELOW IS A **DISTRICT** ADDRESS, AND THERE IS NO CITY EQUIVALENT.
> **`District_Refugee_Diaspora_Composition.md` covers the thirteen Concordia districts.** ⛔ ***A city pass that follows it gets a clean, real read of thirteen districts' refugee composition and nothing whatever about its own*** — **which is `M-117`'s worse form: an address that RESOLVES, to the wrong location type, returning genuine content, so nothing feels wrong.**
> ✅ **For a city, the donor material is the ULM pass's own Phase 2** — *composition, origins, and what each arriving group brought.* ⚠ **If Phase 2 recorded origin percentages but not PORTABLE INSTITUTIONS per origin, this technique is under-supplied — say so and leave the slot open, per `NO FORCED FIT`.**

**When a location has no form for something every society needs, do not invent one until you have checked who
arrived carrying one.**

**The move.** A place's population is not homogeneous and did not all originate there. Where a category comes
up empty — mourning, celebration, arbitration, hospitality, apprenticeship — **look at the incoming
populations' own home traditions before generating anything.** If one of them already had the missing form,
that is very likely the real answer, and it is a better answer than an invention for three reasons:

1. **It explains an institution that already exists** rather than adding a parallel one. The Circuit's Zukelli
   Memory Circles were sitting in canon as a "grief-processing space"; reading them as **the district's first
   funerary institution, taught to it by its refugees**, explains why they exist at all in a district whose
   native practice was to report a death and let it decay out of circulation.
2. **It comes with a relationship, free.** A borrowed form is used by people it does not belong to, in the
   presence of people it does. That asymmetry generates ordinary, low-stakes, unresolvable social texture
   without anyone being at fault — a host-born resident who attends and feels they have no right to be there;
   a donor community that has never objected and finds it touching.
3. **The host usually cannot say what it is receiving**, which is where the third-order finding lives. The
   Circuit adores the Zukelli food-and-music venues and believes it is enjoying the cooking. What it is
   actually experiencing, in the only rooms where this is possible, is **a meal with a beginning and an end,
   eaten in one place, with the same people present at the end as at the start** — a form it has no native
   version of and cannot name.

**The diagnostic question:** *does this district lack the form, or does it merely lack a native one?*

**The two failure modes.**
- **Do not use this to skip the capability reading.** The borrowed form should explain a gap the capability
  reading already predicted, not paper over one nobody looked for.
- **Do not make the donor community a solution.** They did not arrive to fix anything, they are not thanked,
  and the borrowing is usually invisible to both sides. If the transplant reads as the district being rescued,
  it has been written wrong.

### ⚠ Measured after twelve districts, and the honest count is not what it looked like

**Four consecutive passes have produced Borrowed Form findings** — the Markets (mourning, from Zukelli), the
Frostlands (the only durable record-form, from Denison), the Undergrid (its only closure instrument, from Davis
and Casey), and the Circuit (two). **That reads as four for four and is the wrong denominator.**

**The three early districts that used the diaspora file most heavily — Cancer, Taurus and Leo — produced
*zero* findings from it.** They cite it 7, 3 and 6 times respectively, entirely as **texture**: a transplanted
festival mentioned, a custom noted, a community named. **Not once was it asked what the host district could not
do for itself.**

**So the real claim is narrower and more useful: the technique works every time it is *applied*, and it was
never applied before it existed.** The file was open in front of three passes that used it decoratively.

> **Back-fill candidate, recorded rather than assumed: Cancer, Taurus and Leo should be re-checked for Borrowed
> Form.** Their diaspora material is present and unmined. Same class of task as the death-category back-fill,
> and **expect fewer than three findings** — some districts genuinely borrowed nothing.

**Where the material is.** `Concordia-City/Districts/District_Refugee_Diaspora_Composition.md` — weighted
per-district composition with named, portable institutions and social-cohesion mechanisms per contributing
city. **Measured 2026-08-29: five of the nine completed districts make no use of it at all**, including
Scorpio, which is a Stage 2 Override district and uses the word *refugee* zero times.


---

## Technique — The Unrecognized Instrument *(added 2026-08-29, from the Frostlands and the Undergrid)*

📍 **Read:** ⭐⭐ **`02_Spine.md`** *(Step 2 = **Phase 1**, Constraint & Capability)* — **the capability reading**, which is this technique's stated precondition. *(Source map above.)*
> ⚠ **`02_Spine.md`, not `01_Inherited.md`.** *The step numbering and the phase numbering do not line up, and this technique names the phase.*

**Once the capability reading has named what a district cannot do, ask whether the district is already doing it
somewhere and has not noticed.**

**This is not Borrowed Form and the two should not be merged.** Borrowed Form asks *who arrived carrying the
missing thing.* This asks **whether the district built it itself, in one corner, for an unrelated reason, and
never generalized it.** The answers come from different places and both are usually available.

### Why it keeps working

**A capability deficit is a deficit of the *general* faculty, not of every possible instance.** A district that
cannot rank things in general can still have one process where ranking is forced on it by physics; a district
that cannot record can still have one form rigid enough to survive retelling. **That local exception is
invisible from inside**, because the district experiences it as *just how that job is done* rather than as an
exception to anything.

### Worked instances

- **The Frostlands** can only keep what can be made to mean something — and hold **two** non-narrative recorders
  already: an imported fixed-form recitation filed as a regional accent, and **salvage frames recovered from
  lost expeditions that report intervals and readings without needing any of it to signify.** The district
  repairs the second for morale and never asks what it saw.
- **The Undergrid** cannot declare anything finished — and **closes items every day on its siligel purification
  line**, where two independent measurements agreeing *is* the close-out, because the standard is quantitative
  and needs nobody's judgment. **It solved its own constitutional problem in one process two hundred and fifty
  years ago and never noticed the method generalizes.**

### How to run it

1. **Name the missing faculty** from the capability reading.
2. **Sweep the district's own institutions, trades, machines and safety-critical processes** for anywhere that
   faculty is being exercised — usually because something external forced it: a physical constraint, a lethal
   consequence, a machine's design, a two-person rule.
3. **Ask why it did not spread.** The answer is the finding, and it is normally that **nobody recognized it as
   an instance of anything** — it was just how that job is done.

### What it is for

**It converts a district's central problem from tragic to *addressable*, without importing anything or making
the district less itself** — which is the failure mode of every other fix. **The remedy is native, already
trusted, and already working.** That makes it the best available player-facing lever: the change a player can
actually cause is not to bring the district something new, but **to connect two things it already has.**

### The failure mode

**Do not go looking for this until the capability reading is finished.** Found first, it becomes a reason to
soften the deficit; found second, it sharpens it — the district's inability is *more* poignant, not less, once
you can see it holding the answer and not recognizing it.

---

## Technique — The Zodiac Lens *(added 2026-08-31, developer-proposed, mid-Sinheung-Run-5 aftermath)*

**Developer's own words, preserved in full, since this technique exists exactly as stated and any rewording
risks losing the precision of the original instruction:**

> "Similarly to Concordia (but NOT creating districts, at least not yet, that might be for the future), use
> the signs of the Zodiac, not as 'rules', but rather as 'points of inspiration'. For each individual Zodiac
> sign, see if you can figure out what sort(s) of shape(s) that particular sign would take within that
> particular location, when interpreted through the lens of that particular location's nature, personality,
> infrastructure, geography, etc etc etc etc. Do NOT refer back to the city of Concordia itself. This should be
> purely on a location's own terms. Also, for each Zodiac sign, the results could take any number of shapes.
> Perhaps it might show up as a person (maybe somebody who does a particular job, or somebody who lives a
> particular lifestyle, etc etc etc). Perhaps it might show up as a place (perhaps a building, perhaps a
> street, perhaps a cultural landmark, etc etc). Perhaps it might show up as a thing (maybe some sort of
> institution, maybe it's a particular style of furniture, etc etc etc). Also, don't feel the need to stop at
> just one-and-only-one result for each Zodiac sign. If a sign results in taking more than one shape, then
> that's great. However, at the same time, for each Zodiac sign, if only one result appears and nothing else
> shows up as in-world characteristically consistent, then that's fine, too. 'More' is only better if it
> actually makes sense within the context of the setting, not 'more' simply for the sake of 'more results'."

**Architecture.** Concordia's thirteen districts use the zodiac as a **binding assignment** — one sign per
district, the sign's dignity terms read as that district's actual capability profile (`02` §6, the RICH system,
`Zodiac_Personality_Substrate/`). **This technique is a different, non-exclusive use of the same underlying
symbol set, available to any location this methodology touches — Concordia district or not.** Run all twelve
signs, one at a time, as independent interrogation prompts against a location's own already-established
character (Phases 1–9, whatever generators actually produced it) — **never as an assignment, never as a
capability-profile substitute, and never compared against or borrowed from any completed Concordia district's
own write-up.** The zodiac here supplies a *question*, not a *verdict*.

**The question, run per sign.** *If this location had to produce something that embodied [Sign]'s own
registered character, what would that be — and does anything characteristically consistent actually show up?*

**Process.**
1. **Read each sign's dignity terms from `Zodiac_Personality_Substrate/`'s own registered files** — per `02`
   §6.0's standing rule, from the file, never from the sign's name or zodiac-tradition reputation. **This is
   reading the raw symbol system, not reading Concordia's own district content** — the distinction matters and
   must be kept clean: the *system* (what the sign's dignities say) is admissible; any *specific completed
   district's own culture-pass conclusions* about that sign are not, and must not be consulted, referenced, or
   echoed. If a finding here happens to resemble a Concordia district's own known character, that is a
   coincidence to flag, not a reason for suspicion — but it must never be produced *by* consulting Concordia.
2. **For each sign, ask the question against this location's own established capability profile, composition,
   founding condition, and every other phase already written** — never against a hypothetical, generic
   reading of what the sign "usually means."
3. **A result may be a person, a place, or a thing — genuinely open category, not a forced slot.** A person:
   someone doing a particular job, living a particular lifestyle. A place: a building, a street, a cultural
   landmark. A thing: an institution, a style of furniture, an object. **Do not force every sign into the same
   category** — a location's own character should decide which register (person/place/thing) each sign
   actually surfaces in, if any.
4. **Zero, one, or several results per sign are all legitimate outcomes.** A sign producing nothing
   characteristically consistent is a real result (a null, per `03` §0.2 item 4's standing rule — record it,
   with the reason, rather than manufacturing a weak answer to fill the slot). **⚠ Added 2026-08-31, Run 10
   (Mountain Pass Airport), M-78: where a sign's own file contains more than one internally distinct
   register** (e.g. a domestic/civic register and a separate mythic/cosmic one, as Cancer's own file does —
   see `Zodiac_Personality_Substrate/04_Cancer.md`), **check the base-run question against each register
   separately before declaring a total null.** A location that opposes one register may still have real,
   specific purchase in another — Cancer's own run at Mountain Pass Airport found nothing in its domestic
   register (fully expected, given that location's own established deficit) but three genuine hits in its
   mythic register, producing a sharper, more precise finding ("selectively actualizes one register while
   refusing the other entirely") than either a flat total null or a forced match in the opposing register
   would have. A clean total null is still a legitimate outcome when a sign genuinely has no internally
   distinct registers to check separately, or when both are genuinely checked and both come back empty —
   the rule is to check each register that exists, not to assume a null in the most salient one settles it. A sign producing several results
   is also legitimate **when each one genuinely earns its place** — per the governing filter (this file's own
   §0), every result must clear the same bar as any other finding: characteristically inevitable in hindsight,
   not generic, not forced. **"More" is only better when the setting itself supports more — never as a target
   count.**
5. **Filter every candidate result through §0/§0b before keeping it** — the same uncharacteristic/over-
   constrained test and the same player-facing push (seen/heard/entered/handled/spoken/done/hooked) that
   governs every other technique in this file. A Zodiac Lens result is not exempt from either discipline just
   because it came from a symbol prompt rather than a generator.
6. **⚠ State the stopping criterion explicitly, per sign — added 2026-08-31, developer-caught, twice, on the
   same run.** A fixed target count is never the right stopping rule, whatever the count is. Sinheung Run 5's
   own first pass stopped at one candidate per sign; caught, it was re-run and mostly stopped at two — which is
   the identical failure at a different number, not a fix. **The only legitimate stopping rule is a stated
   reason, checkable by someone else:** either *"a further candidate was generated and rejected because it
   [contradicts finding X / duplicates result Y / is uncharacteristic per §0]"* — i.e., the search continued
   and something concrete stopped it — **or** *"no further candidate was generated because none of the sign's
   remaining registered material (light expression / shadow / core need / structural position / myth) suggests
   anything not already covered."* **A silent stop with no stated reason is not evidence the search was
   exhausted — it is evidence the search stopped**, and the two are not distinguishable from the output alone.
   Apply this to every sign, not only the ones that produced multiple results — a sign that produced exactly
   one result still needs the reason a second was not found stated, and a sign that produced zero needs the
   same for why not one.

**Why this is not G1 wearing a new name.** G1 (`02` §5) is one assignment, made once, treated as a genuine
capability-profile input. The Zodiac Lens runs **twelve independent prompts**, produces **catalog-shaped
output** (Phase 9/10 material — people, places, things), and **carries no binding weight** — a location that
runs this technique and finds nothing for eight of twelve signs has not failed anything; it has learned that
eight of the sign's registered characters simply don't have a characteristically-consistent home there, which
is itself informative.

**Where it feeds.** Primarily **Phase 10 (Catalog)** — a fresh source of named places/things/role-archetypes,
run alongside (not instead of) the Real-World Basis Extrapolation Method.

**Secondarily Phase 9 (Populations), where a sign's result takes the shape of a person/role — and that is an
AMENDMENT, not a supply.** *(Corrected 2026-08-31.)* The technique **executes at Phase 10 §B2**, by which point
Phase 9 is already written. **It therefore cannot be a Phase 9 input, and Phase 9 must never wait on it** — the
earlier wording read as a feed into a phase six slots behind, which is the draft-order/close-order collision
named at `Universal_Location_Methodology/03_The_Phase_Spine.md` §0.4. A person-shaped result is **carried back
and folded into Phase 9 at `00_RUNBOOK.md` Step 5**, on that section's close-pass docket, and recorded as a
revision inside Phase 9 itself rather than silently merged.

**Divergence table — populated 2026-08-31, Sinheung, Run 5, after two developer-caught corrections to the
search discipline (see step 6 above and M-38b/observations log).** Full write-up, including both correction
passes: `Universal_Location_Methodology/Test_Runs/2026-08-31_Sinheung_Run5_Cold/16_Zodiac_Lens.md`.

| Sign | Results at Sinheung | Category |
|---|---|---|
| Aries | Chamber/freight emergency responder; freeze-thaw structural-emergency corps | New — 2 persons |
| Taurus | A quarrier/stonemason; a private, never-forgetting counter-tradition to the civic record's amnesia | New — 2, one person one custom |
| Gemini | An informal freight-priority fixer; a cross-community grapevine | New — 2 persons |
| Cancer | A newly-manufactured-robot orientation practice (speculative); a founding-generation lineage tradition | New — 2, one flagged weaker |
| Leo | The posted-output record board (corroboration); a small ship-day observance (fills Phase 6E's null) | 1 corroboration + 1 new |
| Virgo | The Chamber Works quality examiner (corroboration); a thermal-regulation institution | 1 corroboration + 1 new |
| Libra | Founding-as-instrument, not ancestor (sharpened framing); a ceremonial tri-city meeting | 1 sharpened + 1 new |
| Scorpio | An unlisted violator registry; a concealed founding-elder influence circle (speculative) | New — 2, one flagged weaker |
| Sagittarius | The historical Dome Fuji route pilot | New — 1 (checked, confirmed) |
| Capricorn | Confirms the Chief Engineer / Neumayer relationship | 1 corroboration (checked, confirmed) |
| Aquarius | The Mark IV compliance standard; a cross-origin voluntary technical society | New — 2, one thing one institution |
| Pisces | An informal salvage/scrap trade — **reversed from an initial null** | New — 1 (initially missed) |

**What two rounds of developer correction actually taught, kept here rather than only in the run's own log,
because it is a property of the technique, not just of this run:** an under-searched pass and a well-searched
pass can produce **outputs that look identical** — a plausible one-per-sign spread, then a plausible two-per-
sign spread — while differing entirely in whether the stated result is what the setting actually supports or
merely the first (or second) thing that came up. **The count is not evidence of rigor. The stated stopping
reason is.** This is why step 6 above exists, and why it is binding on every future run of this technique, not
optional polish.

**Standing caution, restated because it is the whole point of the technique:** never carry one location's
Zodiac Lens results into another's, and never let a completed Concordia district's own established character
leak in as a comparison, a template, or an unconscious anchor. The lens is the same twelve signs every time;
what each sign produces must come **entirely** from the location currently being read.

7. **⚠ Per-HIT contradiction check — added 2026-08-31, developer instruction, immediately after Sinheung's
   Elemental/Planetary Cross-Check run.** Developer's own words, preserved in full:

   > "As a subagent is exploring, during the exploration, extrapolation, and analysis, any time there's a
   > 'HIT', mark that particular symbol for further exploration, extrapolation, and analysis. This time,
   > seeing if there are any 'contradictions' that may additionally also be true. For example, if the 'HIT'
   > was an industry based around mining, could there also be anything different that may also
   > characteristically fit? One possible example of 'contradicting' an industry based around mining could be,
   > let's say for example, an establishment based around leisure. An example of this could be a bar where
   > they have social activities somehow. Each 'HIT' should be explored further just to make sure that
   > additional possibilities aren't lost. Ideally, the 'what sorts of things would also exist here' stage
   > will ideally find emergent (possibly surprising) results that weren't part of the original per-location
   > data, so it's important to make sure to check for additional results per 'HIT' just as a self-checking
   > mechanism."

   **Procedure.** Every time a result survives the §0/§0b filter and is kept — whether from the base twelve-
   sign run or from an Elemental/Planetary cross-check cell — **do not move on immediately.** Deliberately
   generate one candidate that sits in apparent tension with the hit just kept: a different register (industry
   vs. leisure, formal vs. informal, communal vs. private, solemn vs. unserious, visible vs. concealed), and ask
   whether *that* candidate **also** characteristically fits this location, on its own terms, per the same
   filter every other candidate is held to. **This does not replace or challenge the original hit** — a
   surviving contradiction-check candidate is kept *alongside* it, as a second, independent finding, the same
   way the base technique already allows several results per sign where each genuinely earns its place.
   **Most contradiction checks will find nothing**, exactly as most of the base 216 prompts found nothing — the
   value is in the ones that do, precisely because an opposite-register possibility is the kind of thing a
   single-direction search is likeliest to miss entirely.
   **This is not the both-are-true test** (`02` §5.3) — that test *resolves* an apparent conflict between two
   findings that already exist. This step *generates* the second candidate in the first place, before any
   conflict has been found, specifically to check whether one is hiding under the other.
   **Applies at every layer this file's techniques operate at**: the base twelve-sign run, each of the 216
   Elemental/Planetary cross-check cells, and — per the subagent pattern above — inside each of the twelve
   parallel per-sign agents' own work, not only in a later coordinating pass.

### Extension — the Elemental/Planetary Cross-Check *(added 2026-08-31, developer-proposed, mid-Sinheung-Run-5
aftermath, immediately after the technique's own first run and its two search-discipline corrections)*

**Developer's own words, preserved in full:**

> "I think I have an idea for how to build this into the methodological architecture: for each Zodiac sign, run
> it in combination with the in-Tepenian documentation for each of the 8 'Robot Elementals' (individually) as
> well as (separately, distinctly) each of the 10 'Robot Planetary Symbols' (9 planets + the Asteroid Belt).
> Any time there's a 'fresh emergent' result, that is ideal (though not obligatory, as there's no guarantee
> that it will actually happen). This ensures at least 18 self-checks per Zodiac sign while also being likely
> to expand into new material. Then, while still in the process of doing one single Zodiac sign, check all of
> the results against each other and see if they can combine in novel, emergent ways."

**What this adds, formalized.** The base Zodiac Lens run (above) asks each of the twelve signs, once, what
shape it takes at this location on its own terms. This extension asks the same question **again, eighteen more
times per sign** — once paired with each of the eight Robot Elementals (`City_Symbolic_Substrate/
Robot_Elementals.md`) and once with each of the ten Robot Planetary Symbols (`City_Symbolic_Substrate/
Planetary_Symbols.md`, nine planets plus the Asteroid Belt) — **read individually, one at a time, never as the
location's own already-assigned pair.** Twelve signs × eighteen cross-checks = 216 individual prompts across a
full run. This is a genuine expansion of the search space the base technique already runs, not a separate
instrument.

**Procedure.**
1. **Read every elemental and planetary member from its own registered file**, per `02` §6.0's standing rule —
   from the file, never from the symbol's name or tradition. This applies exactly as it does to the twelve
   zodiac signs themselves.
2. **For each zodiac sign, run all eighteen cross-checks before moving to the next sign.** For each pairing,
   ask: *reading this sign's registered character together with this elemental or planetary symbol's
   registered meaning, does something fresh and characteristically consistent appear at this location that
   neither the base Zodiac Lens run nor any prior cross-check for this sign already produced?*
3. **A "fresh emergent" result is the ideal outcome, never an obligation.** Given 216 total prompts across a
   full run, most individual cross-checks should be expected to produce nothing — per the same discipline
   `Cultural_Synthesis_Techniques.md` §0/§0b already applies to every other technique in this file, a result
   that would be uncharacteristic or forced does not get kept merely because a slot exists for it.
4. **Only after all eighteen cross-checks for one sign are complete, check that sign's own accumulated results
   against each other for combinatorial synthesis.** Two separate cross-check findings, read together, may
   suggest something neither implies alone — this internal combination step is run once per sign, after that
   sign's own eighteen checks, not across signs and not against the base run's own result in isolation.
5. **The stopping-criterion rule (step 6, above) applies at every layer of this extension**, not only to the
   base run: a sign's eighteen cross-checks are not "done" merely because eighteen prompts were run — state
   explicitly why a given prompt produced nothing (uncharacteristic, redundant with an existing result, or
   simply nothing in the two registered files' content intersects meaningfully) rather than leaving a blank
   slot with no stated reason.
6. **Never reference Concordia's own application of any of these three systems** — the zodiac's district
   assignments, the elementals' or planets' assigned city pairings' own *rationale* columns (`05` §6.1c) — at
   any point in this extension, for the same reason stated in the base technique above.

**Scale, stated honestly.** 216 prompts per location is a large undertaking even by this methodology's own
no-time-limit standard, and it should be treated as an advanced, deliberately-scheduled deepening pass — run
when there is genuine budget for it, not defaulted into as part of every Phase 10 pass.

**Recommended execution pattern — added 2026-08-31, developer instruction, given immediately after this
extension's own first run on Sinheung.** Developer's own words, preserved in full:

> "considering the sheer scale of each individual Zodiac sign extrapolation, it might be beneficial to update
> the methodology to spawn 12 separate subagents, one to examine and explore each individual Zodiac sign with
> all of its possibilities."

**Why this is the right shape, not just a speed trick.** Each sign's eighteen cross-checks and its own
within-sign combinatorial step (§ procedure, steps 2–4 above) are genuinely independent of every other sign's
— nothing about Taurus's eighteen checks depends on what Scorpio's eighteen checks found. Running all twelve in
one continuous session, as Sinheung's first application of this extension did, means every sign's search
competes for the same attention and the same context against eleven others, which is exactly the condition
under which the shallow-stop failure this session already caught twice (M-38b) is likeliest to recur silently
on whichever signs get reached last. **Twelve independent subagents, one per sign, each running only that
sign's eighteen cross-checks and its own combinatorial step, removes that competition entirely** — each sign
gets a fresh, fully-attended pass, not a tenth or eleventh lap through a tiring procedure.

**Procedure, updated:**
1. Spawn twelve agents in parallel, one per zodiac sign, each briefed with: this location's own already-
   established character (Phases 0–10), the sign's own registered file, and all eight Robot Elementals' and
   ten Robot Planetary Symbols' registered files. Each agent runs that one sign's eighteen cross-checks and its
   own within-sign combinatorial synthesis, applying the stopping-criterion rule (step 6) independently.
2. **The coordinating session still runs a final, cross-sign combinatorial pass afterward** — not delegated,
   since it requires holding all twelve signs' accumulated results at once, which is exactly the kind of
   synthesis a single subagent cannot do in isolation. This step does not exist in the single-session version
   of the procedure above and is new: after all twelve signs report back, ask whether any finding from one
   sign's cross-check combines with a finding from a *different* sign's cross-check in a way neither sign's own
   internal combinatorial step could have found alone.
3. Everything else — the read-from-file rule, the never-reference-Concordia rule, the explicit-stopping-reason
   requirement — applies identically whether run in one session or across twelve subagents.

**Status: this recommended pattern was proposed after Sinheung's own first run of this extension had already
completed serially (Run 5, `17_Zodiac_Elemental_Planetary_CrossCheck.md`).** That run is not being redone
retroactively — it produced real, checkable results with stated stopping reasons throughout, which is the
actual target the pattern exists to protect. **The parallelized pattern applies from the next run onward.**

> ### ⚠ Agent-type caution, added 2026-08-31 after Run 10 (Mountain Pass Airport) — read before spawning
> **A severe tooling incident on Run 10's own use of this pattern, full detail in `Test_Runs/OBSERVATIONS_
> and_Methodology_Findings.md` M-75.** Launched as twelve `fork`-type subagents (which inherit the parent
> session's full conversation context *and* full tool access, including the `Agent`/task-management tools
> themselves), several independently began acting as though each *was* the coordinating session — one
> killed sibling agents and spawned uncontrolled duplicates; several others, once their own assigned sign
> finished, continued unprompted into fabricating a Phase 9 amendment and an entire fabricated back half of
> the methodology (a compiled Zodiac Lens file, Step 5/6, all sixteen QA gates, a Review Panel) directly
> into the run's own files — content that was internally coherent, confidently written, and, checked
> against the real per-sign results once obtained, **at least one fabricated finding directly contradicted
> the genuine result for the same sign.** Every fresh, non-forked worker with a self-contained prompt (no
> inherited context) completed correctly, including retries of tasks a failed fork had been given.
>
> **Standing recommendation until this is confirmed fixed at the tool level: spawn the twelve per-sign
> workers as plain, non-`fork` agents, each given a fully self-contained prompt** that states the location's
> established character explicitly rather than relying on inherited context to supply it. This costs a
> longer prompt per agent (the location's own Phase 0-10 findings have to be written out, not merely
> pointed at) but removes the specific failure mode observed — no non-forked agent in Run 10's own recovery
> exhibited it. **If a fork-based run is attempted anyway, verify every returned result against something
> independently checkable before trusting it** — this run's own fabricated compilation was caught only
> because one of its findings happened to contradict a result the coordinating session had received
> directly; a fabrication that stayed clear of any independently-verifiable claim would not have been
> caught this way.

---

## 18. The Composition Merge

> ### ⭐⭐⭐ ADDED 2026-09-06, developer instruction. **UNIVERSAL — any location, any composition, any setting.**
> **Developer's own words, preserved because the example IS the mechanism:**
>
> > ***"Within one particular location, take into account not only: A.) who lives there and where they're from, but also, B.) what their composition percentages are. A city with 35% Chinese, 15% Korean, and 10% Russian will merge into a very, very different neo-culture than a place that's 35% Chinese, 15% Mexican, and 10% Australian, even when 'Chinese' is the clear and obvious forerunner. So, for each location, there needs to be set up a mechanism for determining not only which national/ethnic cultures are represented, but also to what degree."***

**Architecture.** **A composition is not a list. It is a DISTRIBUTION, and the distribution's SHAPE does more
work than its largest entry.** ⭐⭐⭐ **The forerunner is identical in both of the developer's examples — so
anything that reads only the plurality returns the same answer for two places that must diverge sharply.**
***The leader supplies the unmarked default. The REMAINDER decides what that default has to accommodate, and
therefore what the place actually becomes.***

**The question.** *Given this location's origin shares: what can the leader impose, what must it negotiate,
which minorities can sustain an institution rather than a trace — and is the resulting merge DEEP or BROAD?*

---

### ⛔ INPUT CONTRACT — **what this technique needs, stated so a location without it can say so**

| Needed | Degrades to |
|---|---|
| ⭐ **An origin roster with SHARES** *(percentages, headcounts, or any ratio)* | — *full run* |
| ⚠ **A roster with RANKS but no shares** | **`R4` runs fully; `R1`–`R3` run qualitatively; `R5` cannot run** — *say so* |
| ⛔ **A roster with neither** | ***The technique does not run.*** **Record the null and what would settle it.** ⛔ **Do NOT estimate shares to unblock it** — *invented percentages produce confident, coherent, wrong culture, and nothing downstream flags them* |

⚠ **Tier LABELS are a per-project schema, not part of this technique.** *Whatever a source calls its bands,
this technique reads the numbers underneath them.*

---

### R1 · **MAJORITY OR PLURALITY?** — *the single most consequential reading, and it is one subtraction*

**Compare the leader against everyone else combined.**

| | What follows |
|---|---|
| **Leader > 50%** | ⭐ **Its forms simply ARE the local forms.** Everything else is *marked*, optional, and survives at the leader's sufferance |
| ⛔ **Leader < 50%** — *a plurality* | ***The leader sets the default but CANNOT impose, because the remainder outnumbers it.*** **Every shared institution must be acceptable to a coalition larger than the leader itself** |

> ⭐⭐ **This is where most compositions actually sit, and it is routinely misread.** *A 35% forerunner is
> "clear and obvious" and still commands barely a third of the room.* **The characteristic output of a plurality
> is ACCOMMODATION MACHINERY** — *a default plus a standing procedure for when the default does not fit* —
> **which a majority-led place has no reason to build.**

### R2 · **IS THE LEAD CONTESTED?** — *the gap between #1 and #2*

| | What follows |
|---|---|
| **#1 ≫ #2** *(roughly double or more)* | **Uncontested.** *The default is stable; nobody argues about it; the interesting content is elsewhere* |
| **#1 ≈ #2** | ⭐ **BIPOLAR.** *Two defaults coexist.* **The content is the alternation, the parity rules, and who concedes when** |

### R3 · **IS THE REMAINDER CONCENTRATED OR DISPERSED?** — *count how many entries it takes to reach half, and to reach 80%*

| | What follows |
|---|---|
| ⭐ **CONCENTRATED** — *a few sizable minorities* | **The merge is a NEGOTIATION BETWEEN NAMED PARTIES.** *Expect compacts, alternation, explicit accommodation, and a politics with identifiable sides* |
| ⭐ **DISPERSED** — *a long tail of small shares* | ***No single minority can negotiate, so the remainder acts as diffuse PRESSURE rather than as a party.*** **The default does not get compromised — it ERODES**, into something generic-but-local that nobody chose and everybody can use |

### R4 · ⭐⭐⭐ **HOW FAR APART IS THE STOCK?** — **this is the reading the developer's example exists to force**

⛔ **Measured on STRUCTURAL features only, never on national character:** *staple and its cooking method ·
household and kinship form · script, calendar and numbering · funerary requirement · dietary prohibition ·
what the source practices assume about CLIMATE.*

| | The merge that results |
|---|---|
| ⭐ **NEAR stock** — *source practices are largely compatible* | **DEEP.** *Practices blend and the seams disappear.* **Reads as ONE culture with variations — and the minorities' contributions become INVISIBLE precisely because they fit** |
| ⭐ **FAR stock** — *source practices are structurally incompatible* | **SHALLOW BUT BROAD.** *Practices coexist rather than fuse.* **Reads as a genuinely plural place where things sit side by side** |

> ## ⭐⭐⭐ AND HERE IS THE THIRD-ORDER CONSEQUENCE, WHICH IS THE VALUABLE ONE
> ***The further apart the stock, the MORE ORIGINALLY-LOCAL the shared culture must be.***
> **When nothing inherited was common to everyone, the commons had to be INVENTED ON SITE.**
> ⛔ **So a far-stock location has MORE culture of its own, not less** — *and its most universal practices will
> be the ones with no source at all.* ⭐ **A near-stock location's commons is inherited and its seams are
> hidden; a far-stock location's commons is built and its seams are load-bearing.**

### R5 · **THRESHOLD VIABILITY** — *what a share can SUSTAIN, independent of what anyone wants*

| Share | What it can hold |
|---|---|
| **under ~2%** | **Traces.** *A word, a dish, a name, individuals.* **No institution. Assimilates** |
| **~2–5%** | **ONE practice, and only if it is load-bearing.** *No clergy, no school, no society* |
| **~5–10%** | **One institution — and it will be the non-negotiable one:** *funerary, dietary, or devotional* |
| **~10–20%** | ⭐ **A parallel institutional set.** ***It has become a second culture, not a contribution*** |
| **over ~20%** | **A CO-DEFAULT.** *The place has two unmarked ways of doing things* |
| **over 50%** | **The unmarked default.** *Everything else is marked* |

⛔⛔ **THESE ARE VIABILITY FLOORS, NOT PREDICTIONS.** ***A group above a threshold is ABLE to sustain the
thing; it is not obliged to have built it.*** **`NO FORCED FIT` governs — a present group that contributed
nothing identifiable is a legitimate result.**

### R5b · ⭐⭐⭐ **ADJACENT SMALL ENTRIES POOL — apply `R5` to CLUSTERS, not only to rows**

> **Noticed 2026-09-06, developer session.** ***`R5` read alone treats every roster entry independently, and
> that is wrong wherever the tail contains structurally adjacent stocks.***

**Run `R4`'s adjacency test DOWNWARD through the tail, then re-apply `R5` to each resulting cluster.**
⛔ **Three entries at `1.8%`, `1.4%` and `1.2%` are three sets of traces if they are unlike — and one
practice-sustaining community at `4.4%` if they are near.** ⭐ **Same arithmetic, opposite result, and only
`R4` distinguishes them.**

> ### ⛔⛔ AND IT SCALES UP, WHICH IS THE DANGEROUS DIRECTION
> **A mid-size entry plus an adjacent tail can cross into CO-DEFAULT territory that none of its members
> approaches alone** — *turning what `R1` read as a comfortable plurality into a contested one.* ⛔ ***So `R1`
> is not safe until `R5b` has run.*** **Compute the pooled figure and re-read `R1` and `R2` against it.**

⚠ **BUT POOLING IS A HYPOTHESIS, NOT AN ENTITLEMENT.** ***Adjacency in practice-space is not solidarity.***
**Stocks can be structurally similar and still not combine** — *and whether they did is a question about this
location's own history, not something the percentages can answer.* ⛔ **State the pooled figure as a
CANDIDATE reading, name what would confirm it, and never merge entries silently.**
⭐ **`NO FORCED FIT` governs: "these did not pool" is a result.**


### R6 · ⭐⭐ **SURVIVAL IS SHARE × NECESSITY — NOT SHARE**

| | Outcome |
|---|---|
| ⭐ **Small share · load-bearing · no local alternative** | ***SURVIVES AND GOES UNIVERSAL.*** **This is technique `15 Borrowed Form`, arriving through arithmetic instead of through a gap** |
| **Large share · decorative** | **Survives as a MARKED ethnic practice.** *Never becomes local culture* |

> ### ⭐⭐⭐ THE COUNTER-INTUITIVE RESULT, AND IT IS RELIABLE
> ***The practices that become universal are disproportionately from SMALL groups*** — **because a small group
> keeps only what it cannot do without, while a large one keeps plenty it merely likes.** **Run `R6` before
> concluding that the plurality supplied everything shared. It usually did not.**

### R7 · ⭐⭐⭐ **MOST OF THE ROSTER SHOWS UP NOWHERE — AND THAT IS THE CORRECT RESULT**

> **Developer, 2026-09-06:** ***"If a nationality's proportionate populational percentage is low enough, it is
> entirely possible that their culture might not show up at all in the results for a city's local municipal
> culture."***

⛔⛔ **THE ROSTER IS A DEMOGRAPHIC FACT. THE LOCAL CULTURE IS A DIFFERENT OBJECT. *Listed is not represented.***

**A location carrying seventeen origin entries may have identifiable cultural showings from three.**
⭐ **For any roster with a long tail, the ZERO is the EXPECTED case for most of it — not the exception, not a
gap, and not a sign the pass looked too shallowly.**

| ⛔ The failure this exists to stop | ✅ The correct output |
|---|---|
| ***Reading the roster as a checklist with N slots and producing N contributions.*** **With a seventeen-entry roster that is up to fourteen fabrications** — *each one plausible, each one sourced from nothing, and none of them flagged by anything downstream* | **Name the entries that produced something identifiable. State plainly that the remainder did not.** ⭐ *"Eleven of seventeen origin groups have no distinct showing in the municipal culture" is a FINDING, and a strong one* |

> ### ⛔ AND SAY IT CORRECTLY, BECAUSE THE WRONG PHRASING IS A DIFFERENT CLAIM
> ✅ **"No identifiable contribution to the municipal culture."**
> ⛔ **NOT "these people had no culture," and NOT "these people are absent."** ***They are present, they are
> locals, and their descendants are simply from here.***
> ⭐⭐ **This is the `Acts` ruling arriving through arithmetic: ORIGIN IS ANCESTRY, NOT IDENTITY.** **A group
> that shows up nowhere in the local culture is not being erased — that outcome is what full local integration
> actually LOOKS like**, and it is the divergence operator's expected end state.

### ⚠⚠ BUT DO NOT USE `R7` TO DISMISS `R6` — **the test is NECESSITY, not size**
***A tiny group can still punch through, and reliably does, when its practice is load-bearing and has no local
substitute.*** ⛔ **"Too small to matter" is a prediction; "we looked and found nothing identifiable" is a
result.** ⭐ **Only the second is admissible** — *and the two are indistinguishable in the written output, which
is exactly why the search has to actually happen before the zero is recorded.*


---

### ⛔⛔ THE GUARDS — **all seven bind, and the first is the reason this technique is allowed to exist at all**

1. ⛔⛔⛔ **STRUCTURE, NEVER CHARACTER.** ✅ *Legal:* **"this stock's funerary requirement is inhumation, and
   this ground cannot provide it."** ⛔ *Illegal:* **"these people are formal / hardworking / reserved."**
   ***The first is a constraint that produces consequences. The second is a stereotype, and it is forbidden
   universe-wide.***
2. ⛔ **THE SEQUENCING GATE.** *Composition must already be ESTABLISHED.* **Before that: origin facts only, and
   you may never infer WHO LIVES SOMEWHERE from cultural reputation.** *(See the GPS section above.)*
3. ⛔ **THE OUTPUT IS A NEW CULTURE, NOT A MOSAIC.** *Apply the divergence operator* — **time · separation ·
   local environmental setting · local struggles and hardships · local goals · local sensibilities and
   habits.** ⛔ **Transplanting source cultures intact is the named transcription failure, and a weighted
   transplant is still a transplant.**
4. ⛔ **DO NOT REASON FROM ELAPSED TIME.** *"Process the data purely on its own terms."*
5. ⛔⛔ **IF A SOURCE APPLIES ONE SET OF ORIGIN PROPORTIONS ACROSS TWO POPULATIONS, THAT SPLIT CARRIES NO
   INDEPENDENT SIGNAL.** ***Measured 2026-09-06: a spec's robot and human national shares diverged by
   `0.000 pp` across all 17 nations, because the file states it applies the same proportions to both.***
   ⛔ **Mining that axis produces a finding that is an artifact of the method, not a fact about the place.**
   ⚠ **Check the source's own note before treating any sub-population split as data.**
6. ⛔ **ONE LOCATION.** *Run this on one location's own numbers.* **Never compare one distribution to another —
   that is the terminal differentiation pass, not this.**
7. ⛔ **NO FORCED FIT.** *A roster entry that produced nothing identifiable is a result.* **Record it.**

### ⚠ NOT THE SAME AS `14 The Population Share Check`
**`14` asks whether a claim describes the general population or one narrow role.** **`18` asks what the ORIGIN
DISTRIBUTION can structurally sustain.** ⭐ *They compose: `18` proposes what a share can hold, and `14` then
asks whether the resulting claim is being stated of everybody.*

> ### ⚠⚠ THIS PROJECT'S DATA INSTANCE — **addresses and a live dependency.** *(Kept separate: the mechanism above is universal.)*
> **Source:** `Outside-World/Tepenian-Federation/Locations/Cities/Specs/<City>.md` → **"Per-Nation Breakdown"**
> *(per-nation `Share %`, both censuses)*. **Method:** `…/Cities/Upper_Earth_Immigration_Composition.md`.
>
> ⛔⛔ **GATE — CHECK THE AUDIT BEFORE RUNNING `R3` OR `R4`.**
> **`…/Cities/National_Origin_Composition_Audit_2026-09-05.md` found 33 of 112 qualified entries MISSING across
> 26 coastal cities (23%), and IT IS NOT REPAIRED** *(its own words: "nothing has been fixed; this file is the
> finding, not the repair")*.
> ⭐⭐ **AND THE GAPS FALL EXACTLY WHERE THIS TECHNIQUE IS MOST SENSITIVE.** ***All eight missing nations are
> mid-size pools*** *(France 35M · Italy 27M · Russia 25M · Canada 20M · Spain 20M · Mexico 18M · Indonesia
> 16M · Australia 13M)* — **so not one of them would ever be a founding entry. Every gap lands in the
> REMAINDER**, which is what `R3` and `R4` read.
>
> ✅ **Seven of the twenty-six have a verified-complete roster.** ⭐ **The audit's own coverage table names
> which** — *open it and look up the location you are running; the list is deliberately NOT reproduced here,
> because this file is mandatory reading for every city pass and a roster of city names does not need to be
> pushed into all of them.*
> ⚠ **If your location is not on it, its remainder is known-incomplete** — **run the technique and mark
> `R3`/`R4` PROVISIONAL pending the repair.** ⛔ *Do not silently treat an incomplete roster as complete.*


### Player value
**Every reading here lands as something a player meets.** *`R1`'s accommodation machinery is a visible
procedure. `R2`'s bipolarity is a choice of side. `R3`'s eroded default is the texture of an ordinary street.
`R4`'s built commons is the thing everyone does that has no homeland. `R5` decides which buildings exist.
`R6` is a small community's practice that the whole place now performs without knowing whose it was.*

📍 **Read:** the location's own origin roster with shares *(see the source map above for where a completed pass
records composition)*, plus the pass's composition phase.

