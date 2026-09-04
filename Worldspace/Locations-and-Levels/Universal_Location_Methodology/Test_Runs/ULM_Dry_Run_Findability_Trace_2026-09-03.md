# ULM DRY-RUN FINDABILITY TRACE — Shirayuki as the model case

**Run 2026-09-03, at the developer's direction. RE-RUN FROM THE BEGINNING after the first attempt was found
to be tracing the wrong thing.** **Purpose, in the developer's own words:**

> ***"Right now, you're not actually 'doing' the ULM… what you're doing is going through the ULM, one step at
> a time, AS IF you were actually deriving and synthesizing a location. If you execute an instruction and the
> information is present, then great. If you execute an instruction and you're UNABLE TO FIND the
> information, that's extremely important to know."***

> ## ⚠ WHAT THIS IS AND IS NOT
> **An INSTRUMENT TEST, not a location pass.** ***No culture derived, no finding synthesized, no phase
> written.*** **Each entry records only: what an instruction demanded, which instruction demanded it, whether
> it could be reached.**
>
> **⛔ NOT A COLD RUN, and could not be.** **The test requires resolving every address — the exact thing a
> quarantine forbids.** ***That is the finding behind the findings: the ULM's own findability has never been
> checkable by the sessions that actually use it.***

> ### ⚠⚠ WHY THIS FILE WAS RE-RUN — the first attempt traced the WRONG ARTIFACT
> **Attempt 1 walked each city spec against `Specs/_TEMPLATE.md` and reported every absent section as a
> missing input.** ***That is not the methodology.*** **The template covers the whole city record across all
> eras; the ULM declares ONE era and makes much of that record inadmissible.** **Three "gaps" were the frame
> working correctly** *(see §RETRACTED)*. **This run walks `00_RUNBOOK.md`'s own Step sequence instead.**

---

# ✅ SUMMARY

| Result | n |
|---|--:|
| ✅ **Found where the instruction said it would be** | **24** |
| ⚠ **Found, but only via a route no instruction names** | **4** |
| ⛔ **NOT FOUND — the instruction cannot be executed** | **6** |
| 🔴 **Found, but CONTRADICTORY between two ratified sources** | **1** |
| ⛔⛔ **The instruction DELIVERED something it exists to prevent** | **1** |
| ❌ **False finding from attempt 1, retracted** | **1** |

> **⚠ Attempt 1 reported 4 blockers. This run finds 6 — and only 2 are the same.** ***Walking the template
> found gaps that were not gaps and missed blockers that were.***

---

# ❌❌ FINDING −1 — **RETRACTED IN FULL. Pass 3's headline finding was wrong, and wrong twice over.**

> ## ⛔ WHAT IT CLAIMED
> **That 19 of 37 cities are "Band 5", that `01` §2.2 therefore requires them to be decomposed into
> sub-locations, that none are, and that this is a corpus-wide structural failure.**

## ⛔ Developer ruling, 2026-09-03: ***"None of those things should factor into the ULM process."***
## ⛔ And: ***"'Concordia alone is decomposed' is not even relevant."***

### Two separate errors, and the second is the one that matters

**1. An imported assumption treated as binding.** **`01` §2's scale-band apparatus — the bands, the
">50,000 must be decomposed" threshold, the "above 1M it has a statistical shape rather than a culture"
framing — is GENERALIZED FROM THE DISTRICT METHODOLOGY**, whose native case was one district inside one
city. ***It was applied to Tepenian cities as though it governed them.*** **A Tepenian city is derived as a
city, whatever its headcount.**

**2. ⛔⛔ CONCORDIA WAS USED AS THE YARDSTICK.** **The finding only READ as a gap because outer cities were
measured against the capital** *(«Concordia is decomposed and they are not»)*. ***That comparison is not
merely unhelpful — it is the thing the developer has now ruled out three times in one session:***

| Ruling | Form it took |
|---|---|
| *"'Connection to Concordia' is IRRELEVANT"* | **a spec SECTION** |
| *"A location gets synthesized on its own terms, on its own merit"* | **the general principle** |
| *"'Concordia alone is decomposed' is not even relevant"* | **an ANALYTICAL COMPARISON** |

> ## ⭐ THE RULE THIS PRODUCES — now written into the methodology
> ***CONCORDIA IS NOT A BASELINE, A YARDSTICK, A CONTROL, OR A COMPARISON CLASS FOR ANY OTHER LOCATION.***
> **Not for scale, not for structure, not for completeness, not for how developed its material is.**
> **See `00_RUNBOOK.md` §C.8d.**
>
> **Why the error is easy and therefore worth a rule:** ***Concordia is the best-documented location in the
> project*** — 301 district files, a full substrate, an Ultra Megasheet. **Anything measured against it looks
> deficient**, which makes it the most available and most misleading comparison in the corpus.

### What survives the retraction
**Only this, and it is small:** *`Official_Population_Census.md` Section B supplies a Census I figure for
every city, so the Tier 0 "population magnitude" input is present and correct.* **Nothing follows from it
about bands, decomposition, or phase substitution.**

---

*(historical — the retracted claim's working, retained per Step 9.5 rule 2: "solving a problem privately is
how a methodology stays broken")*

**Two passes filled in "population band" without computing it. The third computed it.**

| | |
|---|---|
| **Instruction** | `01` §2 — ***"the single most consequential declaration"*** · `01` §6 — the block's `**Population band:**` line |
| **Demanded** | which scale band this location occupies |
| **Result** | 🔴 **Shirayuki = 1,178,313 → BAND 5 (Regional).** ***And the corpus does not record a band for any city.*** |

## The distribution across all 37, computed from Census I

| Band | Cities | `01` §2.1's own verdict on its assumptions |
|---|--:|---|
| **5 — Regional** *(>1M)* | **19** | ⛔ ***"Mostly fail"*** |
| **4 — Urban** *(50k–1M)* | **17** | ⚠ *"Hold, but incomplete"* |
| **3 — Institutional** | **1** *(Amundsen Station)* | ✅ *"All hold"* — **and `01` names this "the district methodology's native band"** |

***Exactly one Tepenian city sits in the band this methodology's assumptions were built for.***
**Largest: Lazar, 2,620,319. Even Concordia is 1,015,947.**

## What `01` §2.2 requires at these thresholds — and none of it has been done

- **Above ~50,000 — decomposition is MANDATORY:** *"a location **must** be decomposed into sub-locations,
  each of which gets its own pass, and the parent's pass covers only what is genuinely shared plus the
  pattern of variation."* ⛔ **36 of 37 cities are above this line. `Local_Cultures/` holds ONE FILE PER CITY.
  Zero outer-city files carry district, quarter, ward or sector sections. Only Concordia is decomposed.**
- **Above ~1M — the unit of analysis changes:** *"the location no longer has a culture; it has a statistical
  shape… A Band 5 pass that reads like a Band 3 pass has committed the scale error."* ⛔ **19 cities.**
- **`03` §0.1's matrix changes the PHASES at Band 5** — Phase 4 → distribution, Phase 8 → delegate, Phase 2 →
  distribution, Phase 10 → delegate. **None of that has ever been applied.**
- **`04` Gate F check 2 exists to catch exactly this** and cannot fire, because **no band is ever declared.**

> ## ⛔ AND THE DECLARATION ITSELF IS ABSENT CORPUS-WIDE: **0 of 37 specs record a scale band.**
> ***So the scale error is invisible by construction.*** **A pass cannot commit it knowingly, cannot be
> caught committing it, and has no field in which to get it right.**

## ⚠ THE INTERNAL TENSION — and it is why this has no clean instruction today

**`01` §2.2 says a Band 4+ location MUST be decomposed.**
**`01` §5.4 gives the per-category machinery — *Uniform · Patterned · Delegated* — but opens with *"A pass on
a Band 4+ location **that contains sub-locations**…"***

> ***So for a 1.2-million-person city with no sub-locations, §2.2 says the corpus is wrong and §5.4 does not
> apply. Neither produces a runnable instruction for the pass in front of you.***

**⚠ And this may be the METHODOLOGY's error rather than the corpus's.** **An enclosed hostile-environment
city may genuinely be one continuous structure** — ***`Inspirational-Influences.md` gives Denison a PRIMARY
pick of Kowloon Walled City, "a single organism rather than separate buildings," and RÉSO as secondary.***
**If that is the Tepenian norm, the 50,000 threshold — inherited from a methodology whose native case was a
district of one city — may simply not transfer.** ***This is a developer ruling, not a pass's call.***

### What is cheap and unblocked right now
**Add a `**Population band:**` line to all 37 specs and `_TEMPLATE.md`, computed from Census I** — the same
shape as the `Access type:` field added the same day. **It costs nothing, it is pure arithmetic, and it makes
Gate F check 2 runnable for the first time.** ***It does not decide the threshold question; it makes the
question visible.***

---

# ⛔⛔ FINDING 0 — Required reading carries an ANONYMIZED worked case about the subject

| | |
|---|---|
| **Instruction** | `CLAUDE.md` + `Step −2` item 5 — ***"read `00`–`05` and the disciplines IN FULL"*** |
| **Demanded** | the methodology's rules |
| **Also delivered** | ***a spine-tier conclusion about Shirayuki*** |

**`05_The_Input_Contract.md` §2.4:**
- **L286** — *"a location whose institutions grew into a draw strong enough that people **make excuses to be
  able to move there** — and whose **symbolic outlier status** is the attraction itself rather than a cost."*
- **L317–318** — *"a city famous for being the place people move to, which retained **61.8%** against a
  **71.9%** national mean — **third-lowest of thirty-three**. **The pull that fills it is the pull that
  emptied it.**"*

**Shirayuki's symbol rationale:** *"A natural **OUTLIER** — a place people will **MAKE EXCUSES TO BE ABLE TO
MOVE TO**."* ***Same phrase.*** **`06` L77 confirms: *"Shirayuki's retention figure."***

### Why this outranks every other finding here
1. ⛔ **The alias sweep is structurally blind to it.** An independent checker swept 13 files × 8 aliases:
   `alias_hit_total = 0`, two methods, positive control. ***The result was correct. The leak remains.***
2. ⛔ **`00_RUNBOOK.md` L232 quotes THIS CASE as its example of the violation** — M-4: *"Do NOT anonymize
   instead of moving… an unnamed one is absorbed as general knowledge."* ***The rule names it, illustrates it
   with this city, and the instance is still live in the file the rule governs.***
3. ⛔ **`06` misfiles it** — L77 says `02`; it is in `05`.
4. **Tier: SPINE** *(pull/push disposition + retention rank + a capability verdict)*. **`§C.5`: no partial
   credit.**

**Fix:** move both passages to `Worked_Examples_Archive/`, leave a bare pointer, correct `06` L77, and **add a
SHAPE-based detection pass to `Step −2`** — a distinctive statistic, a quoted phrase, a *"a city famous
for…"* construction. **Nothing in the methodology currently looks for these.**

---

# ⛔ THE SIX BLOCKED INSTRUCTIONS

## 1. `Step 0.1` — the declaration block cannot be completed
**`01` §6 mandates an `**Extent band:**` line; `01` §2 requires BOTH bands declared.**
⛔ **No extent figure exists for Shirayuki or for any of the 37 cities.** *(Census I = **1,178,313** is
present; only the denominator is missing.)*

## 2. `Step 2` item 6 — the cheapest check in the methodology cannot run
***"Divide population by extent. One division; no interpretation."*** **`04` Gate 11's ONLY recorded catch
came from this**, and `04` says the half that fired *"was the part that was arithmetic… the only part that
does not run on the same faculty that produced the error."* ⛔ **Unrunnable — same missing denominator.**

## 3. ⭐ `Step 0.6` — **THE PARENT IS UNWRITTEN, AND THERE IS NOWHERE TO REGISTER THE ASSUMPTION**
**`01` §5.2 requires the provisional-inheritance protocol, ending in rule 5: *"Register the assumption where
the parent's eventual pass will see it. An assumption recorded only in the child's file is an assumption the
parent will contradict."***

⛔ **The Mirny subnet has no pass and no subnet-level document.** **What exists is `Local_Cultures/Mirny_Subnet/`
— a FOLDER OF ITS CHILDREN — and `City_Master_Reference/Mirny_Subnet_Reference.md`, which is an INDEX and is
`WITHHELD` from a cold run by `§C.1`.**

> ***So the instruction names a destination that does not exist.*** **There is no subnet-level file, no
> registry row for one, and no convention for where a child's provisional assumptions about its subnet
> should live.** **Consequence: `04` **Gate P** *(parent reconciliation)* **can never run for any of the 37
> cities**, because no parent has been written to run it.

## 4. ⭐ `Step 0.3` / `Step 9.3` — **NO COMPLETION TRACKER EXISTS TO RECONCILE AGAINST**
**`Step 0.3`: *"Run Gate 0 — reconcile any completion claim against the file."*** **`Step 9.3`: *"Update
whatever tracker claims completion."***
⛔ **There is no ULM city-completion tracker.** A search returns only a district `00_Index.md`, an
`Investigation_Loop_Round2_Tracker.md`, and a prior run's own status file.
> **`04` calls Gate 0 *"the cheapest gate, highest yield."*** ***It has no target.*** **And Step 9.3 instructs
> an update to a file that does not exist — so a completed pass leaves no completion record anywhere.**

## 5. `Step 6` / `Step 9.2` — the differentiation instrument is empty
**`CLAUDE.md`: read the row BEFORE writing a category, add the column in the SAME COMMIT.**
⛔ **`02_Cross_City_Industry_Differentiation_Table.md`: 12 industry rows, ZERO content, 4 named columns
against a `(…32 more)` placeholder.** **The mandated check passes vacuously.**

## 6. `G2` monthly climate — the generator is present but thin
**`03` §0.3 Phases 1 and 3 demand climate data.** ⛔ **`### Annual Climate` heading present, `0` monthly
rows, no `Climate type` field.** ⚠ **Partly recoverable — see Finding B.**

---

# 🔴 FINDING 7 — `G8` CONTRADICTS ITSELF ACROSS TWO **RATIFIED** ROOTS

| Source | Says | Ratified by `05` §6.3 rule 6? |
|---|---|---|
| **`Specs/Shirayuki.md`** *(Founding Population Re-Resolution, 2026-07-06)* | **Japan PRIMARY 36.27%**, China Significant 7.18% | ✅ `Cities/Specs/` is a ratified ROOT |
| **`Official_Population_Census.md` §I** | **PRIMARY: China**, Japan in Significant | ✅ named a ratified root by the same rule |

**⚠ The census also contradicts ITSELF** — its own note states *"Japan re-tiered to Primary at 36.27%"* above
a table that was never updated.

> ## ⛔ NO RULE IN THE ULM ADJUDICATES BETWEEN TWO RATIFIED ROOTS.
> **`§A`'s rank order handles universe-vs-project and canon-vs-proposal. It does not handle this.**
> ***A pass running `G8` gets opposite answers depending on which file it opens first.*** **The spec is more
> specific and more recent and is almost certainly right — "almost certainly" is not a rule.**

---

# ⚠ FINDINGS A–D — found, but only by a route no instruction named

| # | Instruction | What was demanded | How it was actually reached |
|--:|---|---|---|
| **A** | `03` §0.3 Ph 1/3 — "climate data" | monthly climate | **`Reference/Real-World/Climate Data/READER/`, keyed by REAL-WORLD STATION** — `Bharati_TBD.md`. **A search on "Shirayuki" returns nothing.** Registered nowhere before 2026-09-03; the master city index recorded the folder as *"the empty `Climate Data`"* |
| **B** | *(same)* | precip · daylight · range | ⛔ **Not in READER at all — 0 of 37 files carry them.** Temperature only. **Daylight is DERIVABLE from latitude; the rest needs research** |
| **C** | `Step −2` — enumerate the registry | every canon root | **`§C.7` and `§C.9` were absent from the root list in all three briefs.** Fixed 2026-09-03 |
| **D** | `§C` — network position | `Highways.md` | **The registered path did not exist.** Fixed 2026-09-03 |

---

# ✅ FOUND AND CLEAN — 24 instructions

**`Step −1` · `05` §7 pre-flight.** **Tier 0 — 4/4**: designation *(Shirayuki 白雪)* · position *(Bharati
site, Larsemann Hills, Prydz Bay)* · **Census I 1,178,313** · parent *(Mirny)*. **Tier 0b** — frame supplied
by the standing default, `§C.8a`. **Tier 1 — six clean generators against a required minimum of three**, so
the pass proceeds: `G1` *(Uranus + Fire; members only — the rationale column is conclusion-tier, `05` §6.1c)*
· `G3` · `G4` · `G5` *(`Access type: ON`)* · `G6` *(founding-era events — see below)* · `G7` *(4 tiered
picks)*.

**`Step 0.2`** — all five `Disciplines/` copies present. **`Step 0.4`** — all six reading layers available in
the mandated order. **`Step 0.5`** — `Developer_Ruling_Queue.md` present; **5 open DRQs identifiable**, of
which **DRQ-08 · DRQ-09 · DRQ-10 touch this pass** *(the food/export layer, Phase 7a)*. **`Step 1`** — 13
inherited files including a `Full_Extrapolation`.

**`Step 3`** — `Shirayuki_Research_Log.md`, 103 lines *(one of only four cities with one)*; `Research_Logs/
README.md` carries the convention.

**`Step 4` per-phase canon targets — all eleven resolve.** Phase 5's three relationship files carry Shirayuki
*(18 · 3 · 8 mentions)* · Phase 6 `Factions/Robot_Religions/` (6 files) + `National_Holidays.md` · Phase 7
`Division_of_Industry/` with its carve-out header · Phase 8 `Robot_Biology_and_Culture/` +
`Weapons_and_Tools_Philosophy.md` · Phase 9 all three universe-repo sources · Phase 10
`Enneagram_Character_Index.md` + `Zodiac_Personality_Substrate/` (22 files).

**`Step 5`** — the close-pass docket at `03` §0.4. **`Step 7`** — Gate 6's siblings written and available at
Step 7 *(Sinheung · Zhongshan · a Tri-Cities region file and an overlap/distinguishing guide)*; Gate C's
three tiers all reachable now the sibling-project paths are fixed. **`Step 8`** — `Disciplines/00f`.
**`Step 9.5`** — `OBSERVATIONS_and_Methodology_Findings.md`, **5,509 lines, 129 entries, continuous to
M-139**.

### ⚠ Two of attempt 1's "findings" were MY OWN instrument errors, corrected here
- **"OBSERVATIONS has 8 entries"** — a bad grep pattern. **It has 129.**
- **"`G6` NOT FOUND"** — see §RETRACTED. **`G6` is available**: founding, the Jeju-do allocation, migration
  and interwar events, from `## Founding`, `World_History_Reference.md`, **U** `Timeline Eras/`, and
  `Background-Lore/Cities/Janbogo_Subnet/…`-style vignettes. ***The Long Night War is the frame's terminus,
  not an event inside it.***

---

# ❌ RETRACTED — attempt 1's Finding 3 was wrong

**It claimed `G6` was unfindable because Shirayuki's spec has no `## Current Status / Destruction`, no
`## Legacy`, no `## Connection to Concordia`.** ***All three are CORRECTLY absent.***

**Developer, verbatim:** ***"For the purposes of deriving a location, 'Current Status / Destruction' is
IRRELEVANT. SECOND INTERWAR PERIOD."*** · ***"'Connection to Concordia' is IRRELEVANT. A location gets
synthesized on its own terms, on its own merit."***

**Why the error happened:** the tracing session had `§C.8a` in context and had quoted its post-war warning an
hour earlier — **but `§C.8a` governed the `**Status:**` FIELD and said nothing about the SECTIONS**, and the
trace was checking against the TEMPLATE. **Absent an explicit exclusion list, "in the template, not in the
file" reads as a gap.**

**✅ Fixed the same day:** `§C.8a` now carries an **EXCLUSION LIST** naming all three, stating a spec lacking
them is **complete for ULM purposes**, that their presence is not permission to read them either, and what
`G6` actually draws on instead.

> ## ⭐ The generalizable finding, worth more than the false one
> ***A frame declaration does not merely DATE a pass. It makes some existing, canon, well-written material
> INADMISSIBLE.*** **Name those sections explicitly or two opposite errors follow, both of which have now
> occurred here: a pass READS them as supply (M-45), or an audit reads their ABSENCE as a gap (this trace).**

---

# WHAT THE RE-RUN ESTABLISHES

**The per-phase canon targets are genuinely sound** — 24 of 36 instructions resolved exactly as written, and
every one of the eleven Phase rows in `§C.8c` reaches real material. ***The failures are not distributed;
they cluster in four kinds:***

1. **Per-city artifacts nobody created** — extent, the monthly table, the differentiation column.
2. **Destinations the methodology names that do not exist** — ⭐ *the new class this re-run found*: **a
   parent to register assumptions with, and a tracker to record completion in.** **Both are instructions
   pointing at nothing.**
3. **Addresses that were wrong or unregistered** — four, all now fixed, none visible to a reader.
4. ⛔ **One contamination channel the methodology's own detection cannot see.**

> ## The two lines to carry out of this document
> ***An alias sweep proves a file does not NAME your subject. It cannot prove the file does not DESCRIBE
> your subject.***
>
> ***And an instruction can fail not because the data is missing, but because the PLACE IT NAMES was never
> built. Gate P and Step 9.3 have never once been runnable, and nothing reported it, because a pass that
> cannot do a step simply moves on.***
