# ULM INPUT-AVAILABLE AUDIT — what each of the 37 chartered cities is MISSING

**Measured 2026-09-03.** **Basis of reference: `ULM_Input_Required_Reference.md`, in this folder.**
**Read them as a pair — that file is the bar; this file is the measurement.**

> ## ⚠ LAYER: **PROJECT.** This file names every city and is not part of `01`–`05`.
> **LAW 0 is not restated here.** *(It is carried in full in `ULM_Input_Required_Reference.md` and in every
> ULM instruction file.)* ***This is a measurement artifact, not an instruction file*** — the practice of
> copying LAW 0 verbatim exists so a procedure is never run without its governing law, and a data table is
> not a procedure. **The one line that does bind a reader here: a gap is not a defect. Several below are
> deliberate.**

> ### ⛔ ADMISSIBILITY — declared, not assumed
> **This file records PRESENCE and ABSENCE of inputs, plus file addresses. It states no conclusion about
> any city's character, capability or identity.** **Absences are explicitly ADMISSIBLE** *(`00_RUNBOOK.md`
> §C.1 — "Open threads — these are gaps, not answers")*. ***But per `05` §6.1d, no file is safe by
> category.*** **A cold run wanting this file gets it mapped first.**
> **⚠ And note what it IS: a corpus-wide compilation. `§C.3` — a compilation pass contaminates its
> compiler against every location it covers — applies to the session that BUILT this.**

> ## ⚠⚠ SCOPE CORRECTIONS APPLIED 2026-09-03 — **read before using any number below**
>
> **This file is the raw MEASUREMENT record and is preserved as measured.** ***Four fields in it have since
> been struck from scope. Their rows and per-city entries below are STALE and must not be worked from.***
> **Full reasoning: `Location_Data-Input_To-Do.md` §Removed.**
>
> | Field | Status | Why |
> |---|---|---|
> | **Census II** | ⛔ struck — **not a gap** | *developer ruling:* Census I is Antarctica entire; Census II is Antarctica after orbital colonization begins. **Only Census I matters — it is the peak load a city must physically hold.** `Census I` is complete 37/37 |
> | **Notable figures** | ⛔ struck — **circular by construction** | a notable figure requires understanding the city's nature, which is the ULM's own OUTPUT. `05` §2.4 hazard 3 fires automatically |
> | **Concept art** | ⛔ struck — **Tier 3 optional** | its input value exists only if it PRECEDES the pass; made after, it is illustration. Production pipeline, not worldbuilding debt |
> | **National medical** | ⛔ struck — ***the metric was invalid*** | the source names **3 national institutes**, not 37 city entries. **12 of the 15 "present" were free-text false positives** |

---

# 0. How this was measured, and where the instrument was wrong

**Built by script, not by reading** — `04` Part IV and M-101: *a script sees the text and reports only a
classification; it is incapable of the "didn't look hard enough" failure.* **Every figure below is a
mechanical test over all 37 specs and every aggregate source named in the registry.**

### ⚠ Three instrument defects were found and fixed BEFORE these numbers were recorded
**Recorded per Step 9.5 rule 3 — *never compress a negative result into a positive one*. Each of these
would have produced a confident wrong answer:**

| Defect | Wrong answer it gave | Cause |
|---|---|---|
| Concept-art test matched **filenames** | **0 of 37** — a total-gap claim that was false | art is stored in per-city *directories*; most hold only `.gitkeep` |
| Monthly-climate test v2 counted **empty rows** | **37 of 37 present** — flattering, and wrong | a city with *no table at all* has zero empty rows, so it scored as complete |
| Census-II test matched **free text** | **37 of 37 present** | four cities appear only in *footnotes* saying they are absent |

> ***The second defect ran in the flattering direction — which is the direction self-audit error in this
> project has run on every occasion it has been measured.*** **It was caught only because the two runs
> disagreed (30 vs 37) and the discrepancy was chased rather than reconciled to the newer number.**

---

# 1. CORPUS-WIDE RESULT — worst first

| Input | Have | Missing | Verdict |
|---|--:|--:|---|
| **EXTENT / AREA** `T2-8` | 0 | **37** | ⛔⛔ **TOTAL GAP — and it disables the only self-verifying check in the methodology.** See §2 |
| **Differentiation table column** `04` Part III | 0 | **37** | ⛔ **Table exists with 12 industry rows and ZERO content in any of them.** `CLAUDE.md` requires the row be read before writing a category and the column added in the same commit |
| **Research log** `Step 3.7` | 4 | **33** | ⛔ **Standing developer instruction since 2026-08-30.** 4 of 37 |
| **Concept art** `T2-7`/`T3-18` | 4 | **33** | ⛔ 33 cities have an empty placeholder folder. Phase 3 texture + Phase 10 catalog run blind |
| National medical/care entry | 15 | **22** | ⚠ informational — a national institute roster; absence is not necessarily a gap |
| **Notable figures** `T3-01` | 26 | **11** | ⚠ 11 cities carry the unfilled `**[Name]**` template placeholder |
| ~~**Monthly climate table** `T1-G2`~~ | ~~30~~ **37** | ~~7~~ **0** | ✅ **CLOSED 2026-09-04 — and the row is now far bigger than it was.** See the **CLIMATE BLOCK** immediately below |
| Named in `Airports.md` `T1-G5` | 31 | **6** | ⚠ 6 — may be legitimately air-isolated; needs a positive 'no airport' statement |
| **Census II figures** `T0-3` | 33 | **4** | ⚠ 4 — confirmed by the census's own note |
| Symbol pair `T1-G1` | **36** | **1** | ✅ **Amundsen Station added 2026-09-04 — Neptune + Electromagnetism**, with a full derivation section in the assignments file. ⛔ **Only Concordia remains** *(district methodology)*; **Abowasa is explicitly excluded in-file** pending its founding-nation fix. ⚠ *The prior '3 absent, all three deliberate' was only verifiable for Abowasa — Amundsen's absence carried no note either way, and turned out to be an omission rather than a decision.* |
| Named in `Highways.md` `T1-G5` | 34 | **3** | ⚠ 3 — may be legitimately road-isolated |
| ~~Founding population `T1-G4`~~ | ~~36~~ **37** | ~~1~~ **0** | ✅ **CLOSED 2026-09-04 — Denison.** ⚠ **The data was never missing; it was UNADDRESSABLE** — held as prose inside the `Settled:` paragraph, so a sweep for the literal `**Founding population:**` field reported a false gap. *Now a proper field; presence test recorded on `T1-G4`.* |
| Inspiration picks `T2-4` | 36 | **1** | ✅ 1, structural |
| DoI Half B row `T1-G3` | 36 | **1** | ⚠ 1 |
| Robot culture file `T2-5` | 35 | **2** | ✅ **2, both deliberately PAUSED — not gaps to fill.** **Concordia** — district methodology, not the city one. ⛔ **Abowasa — BLOCKED on an upstream canon fix**, not on effort: its whole premise rests on a *"Finnish and Swedish exiles, jointly"* founding that the project's own First Interwar turnover history does not support surviving intact *(`TODO.md` §377; developer-confirmed, same bug class as Sejong's Hangul fix)*. **The fix touches the city's NAME, demonym, dual-national trait and Turku Remembrance holiday** — *"Abowasa" is literally Aboa + Wasa, and the build tracker already marks the name provisional.* ⚠ **Running the pass now would need a full redo.** |
| Local culture file `T2-1` | 36 | **1** | ✅ 1, structural |
| Megasheet `T2-1` | 36 | **1** | ✅ 1, structural |
| Enneagram read `T2-5` | 36 | **1** | ✅ 1, structural |
| Census I figures `T0-3` | 37 | **0** | ✅ complete |
| National origin composition `T1-G8` | 37 | **0** | ✅ complete |
| Relationship files `T2-6` | 37 | **0** | ✅ complete |
| Master reference entry | 37 | **0** | ✅ complete |
| Notable locations `T3-10` | 37 | **0** | ✅ complete |

---

# 1b. ⭐ CLIMATE BLOCK — **re-measured 2026-09-04, after the full corpus pass**

**What was one stale row is now nine measured ones.** *Every figure below re-derived from the spec files
today, not carried forward.*

| Climate input | Have | Missing | Verdict |
|---|--:|--:|---|
| **Monthly climate table** `T1-G2` | **37** | 0 | ✅ complete — was 30/7 |
| **Mean · Avg High (day) · Avg Low (night)** | **37** | 0 | ✅ complete |
| ⭐ **Rec High · Rec Low** *(all 12 months)* | **37** | 0 | ✅ **CLOSED 2026-09-04** — was 17, then 25. See below |
| **Precip · Precip Probability · Daylight** | **37** | 0 | ✅ complete |
| **Prevailing winds** | **37** | 0 | ✅ closed — all with *measured, site-specific* data |
| **Record extremes** *(header)* | **37** | 0 | ✅ closed |
| **Polar night · Midnight sun · Solstice min/max** | **37** | 0 | ✅ complete |
| **Climate type · Mean annual temp · Temperature range · Annual precipitation** | **37** | 0 | ✅ complete |
| ⭐ **Precipitation regime** *(falls / lands / lost / WIND-vs-COLD)* | **37** | 0 | ✅ new class, complete |
| ⭐ **Per-column provenance** | **37** | 0 | ✅ new class, complete |
| ⭐ **Access type** `T1-G5` | **37** | 0 | ✅ new field, complete |

> # ⭐⭐ THE CLIMATE BLOCK IS CLOSED. **Every field, all 37 cities.**
> *One stale row on the morning of 2026-09-04 became **thirteen complete ones**.*

## How the last, hardest field closed — monthly record extremes, 17 → 25 → 37

| Source | Gave |
|---|---|
| Published climate boxes | the first **17** — *kept in preference to everything below; they cover longer periods* |
| **NOAA NCEI GSOM** *(monthly `EMXT`/`EMNT`, 68 Antarctic stations)* | to **25** |
| ⭐ **NOAA NCEI GHCN-Daily** *(daily `TMAX`/`TMIN`)* | **nine cities at once** — Rothera *(was 3/12)*, Lazar, Mirny, Zhongshan, Shirayuki, Sinheung, Kunlun, Sejong, Cape Adare |
| ⭐⭐ **PANGAEA — IMAU Antarctic AWS network** *(Van Tiggelen et al. 2025)* | **the last two.** `AWS16` **IS Princess Elisabeth's own station** *(0 km, 92,670 hourly obs)*; `AWS05` is **~10 km from Abowasa at matching elevation** *(117,567 obs)* |
| GHCN-Daily `AYW00087701` Adare Hallett | **Cape Adare's July**, which its 75 km proxy never recorded |

## ⛔⛔ THE DATA-QUALITY WORK WAS THE REAL CONTENT — three filters, right on the third

**Raw archive data is not clean, and the first two attempts to clean it were wrong in opposite directions.**

| Attempt | Failure |
|---|---|
| **1. Per-station percentiles** | ⛔ too coarse — passed a **+17.2 °C APRIL reading at 71°S** |
| **2. Per-month percentiles** | ⛔ caught that, but began **clipping genuine records** *(Rothera's real −39.1 °C)* |
| ⭐ **3. Gap rule** — reject an extreme only if separated from the next value by **>6 °C** | ✅ **correct** |

> ### ⭐ WHY THE GAP RULE WORKS, stated so it can be reused
> ***A genuine record sits in a continuous tail. An instrument error sits alone.***
> **Rothera's −39.1 °C has a 3.9 °C gap and is real. Cape Phillips' +20.4 °C June reading has a 21.9 °C
> gap and is not.** **10 isolated readings rejected across the set; every legitimate record preserved.**

⚠ **Two further traps, both of which would have silently corrupted all nine GHCN-Daily cities:**
- **GHCN-Daily stores TENTHS of a degree.** Raw values read **+120 °C** and **−391 °C**. *Caught by sanity
  check, not by assumption.*
- ⛔ **The GHCN feed for Wasa (11 km from Abowasa) is CORRUPT** — 111 of 1,904 daily means below −60 °C at a
  366 m nunatak. **It was refused rather than filtered** *(the bad values are 7% of the record, enough to
  shift the percentiles themselves)*. ⭐ **PANGAEA's clean AWS record for the same site later gave −45.4 °C,
  confirming the refusal was correct.**

> ## ⚠⚠ A REGIME MISCLASSIFICATION, found by the same search — recorded, not quietly fixed
> **`Davis` was classified KATABATIC MARGIN. The operating authority states plainly that Davis is *away
> from the katabatic wind*** — far enough from the ice sheet, with Vestfold Hills rock moderating the local
> climate. ***A katabatic label was simply wrong.***
>
> **Reclassified to `ICE-FREE OASIS`** *(retention 38% → 45%)*, and its WIND-vs-COLD statement rewritten:
> **neither hazard dominates, and that is what distinguishes it** — *the problem at Davis is dryness and
> isolation, not violence.*
>
> ⚠ **The other 36 regime assignments are the same kind of judgement call** — made from latitude,
> elevation and the presence of a katabatic regime. **This is the first one an authoritative source has
> contradicted.** *They stand, but they are inferences, not measurements.*

> ### ⚠ The 3 with no monthly records have **no station within range**
> **Abowasa** *(nearest 312 km)* · **Dome_Fuji** *(240 km)* · **Princess_Elisabeth** *(430 km)*.
> **These same three are the only cities still missing a `Record extremes` header, for the same reason.**
> **Plus `Cape_Adare`, which has no station and no assigned proxy at all.**
> ***These are PROXY RULINGS, not research tasks.*** **Do not re-open them as searches** — the 2026-09-04
> pass exhausted BAS READER, NOAA NCEI *(68 Antarctic stations)*, published climate boxes in five
> languages, and national met services. **The data does not exist to be found.**

## ⛔ Two rows in §1 above are NOT reliably measured — corrected note, 2026-09-04

**Both were re-tested today and both tests were wrong. Recorded rather than quietly repaired.**

| Row | Problem |
|---|---|
| **Notable figures** | The `**[Name]**` placeholder test returns **0**; a TBD/placeholder test returns **32 of 37**. **The §1 figure of 26/11 is not trustworthy.** ⭐ *Moot either way — the developer STRUCK this requirement* |
| **Concept art** | ⛔ **`City_Concept-Art/` is organized BY SUBNET, not by city** — 8 directories, 21 files. **Any per-city count of it is structurally meaningless.** ⭐ *Also struck by the developer* |

> ⚠ **This is the THIRD variant of the same measurement bug in one day** *(after the concept-art
> filename-vs-directory error and the monthly-climate empty-row error)*. **The pattern: a test written from
> an assumed file layout rather than a verified one.** ***Look at the directory before counting it.***

---

# 2. ⛔⛔ THE HEADLINE GAP — **EXTENT. 0 of 37, and it breaks the one gate that has ever worked.**

> ### ⭐ THE APPROACH IS NOW WRITTEN — `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Area_APPROACH.md`
> **Settlement-form typology first** *(the census's existing "island cap" annotations generalized)*, **then dimensions.** ⛔ **And the trap it exists to prevent: DO NOT DERIVE EXTENT FROM DENSITY** — that makes Gate 11 tautological and turns the methodology's only author-independent instrument into one that confirms the author. ⭐ **Density is an OUTPUT to be checked, never an input to be chosen.**

**Not one of the 37 cities has a declared extent, area, footprint or land-take.**

### Why this is the worst single finding in the audit

**`01` §2 requires TWO bands declared, not one** — *"the population band and the extent band… when they
diverge, the divergence is characterizing."* **`01` §6's declaration block has a mandatory `**Extent band:**`
line. `00_RUNBOOK.md` Step 2 item 6 orders the division and calls it *"the cheapest plausibility check in the
methodology."*** And `04` Gate 11 records:

> ***"Divide the population by the area. That is the whole technique."*** — **Gate 11's ONLY recorded catch,**
> and `04`'s own verdict on it: *"the part that fired was the part that was **arithmetic**… it is the only
> part of this gate that does not run on the same faculty that produced the error."*

***So the single instrument in this methodology that is not vulnerable to the author's own blind spots cannot
currently be run for any city in the project.***

### Six cities have an area figure. **None of them is a city extent.**

**Every one is a REAL-WORLD SITE area — the physical basis, not the Tepenian settlement:**

| City | What the figure actually measures |
|---|---|
| **Cape Adare** | the cape / Important Bird Area — **2.94 km²** |
| **Denison** | the Cape Denison ASMA zone — **1.11 km²**, and the spec notes the true ice-free area is *less* |
| **Davis** | the Vestfold Hills ice-free oasis — **~400 km²** |
| **Lazar** | the Schirmacher Oasis — **~34 km²** |
| **Sayowa** | East Ongul Island — **~4–5 km²** |
| **Sinheung** | the Larsemann Hills — **~34 km²** |

> ### ⭐ TWO SPECS HAVE ALREADY HIT THIS, INDEPENDENTLY, AND SAID SO
> - **Cape Adare's own spec:** *"the exact figure is a worldbuilding decision, not an arithmetic one —
>   ~20–40 km² is the…"* — **the gap is named and left open.**
> - **Sayowa's own spec has already run Gate 11's division:** *"225,376 people on ~4–5 km² is **~50,000/km²**
>   — the implausibility…"* ***That is Gate 11 firing, in a spec file, with no extent canon to resolve it
>   against.***
>
> **This is not a hypothetical gap. It has already produced at least one live, unresolved implausibility.**

### What to do with it — it is a `REQUESTED` output, per `05` §5

**A well-formed request states four things.** Here they are:
1. **What is missing:** a declared built extent (km²) per city — settlement footprint, not the real-world
   site's area.
2. **Which phase is blocked:** Phase 0 cannot fill the `**Extent band:**` line; **Gate 11's arithmetic check
   cannot run at all**; `01` §2's population/extent divergence finding is unavailable everywhere.
3. **What was done instead:** nothing — no pass can substitute for it, and the six site areas above are
   facts about the real-world SITE, not the city.

> ### ⛔⛔ THESE FIGURES BOUND NOTHING — standing correction, developer, 2026-09-03
> ***"It's not necessary to only build on non-iced earth."***
> **Tepenian cities build ON ICE, and canon already says so: Halley sits on the Brunt Ice Shelf; Neumayer is
> *"built on the Ekström Ice Shelf rather than on bedrock."*** ***So ice-free area is NOT a ceiling on a
> city's extent or population.*** **An earlier version of this line called them "upper bounds on habitable
> land" — that was the error, and it has recurred across sessions.** **Full note:
> `Location_Data-Input_To-Do.md` §1.** ⏸️ **Density and extent are DEFERRED by developer instruction.**
4. **Sensitivity:** ⚠ **high, and it may invalidate existing texture.** Sayowa's own numbers already imply a
   density near the densest cities on Earth. **Densities are the premise of texture findings across the
   corpus** *(`04`: "before trusting any texture claim, price it against a density figure")*.

---


---

# 3. PER-CITY GAPS, BY SUBNET

**A city with no line under it is missing nothing this audit tests.** ***That is not the same as being
complete*** — every city is missing `EXTENT`, which is listed once in §2 rather than 37 times here.
**`↳ structural`** marks an absence that is correct by design and must not be 'fixed'.

## Palmer Subnet — Antarctic Peninsula

**Esperanza**
- differentiation column `04 III`
- named in Airports.md `T1-G5`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Juan Carlos**
- monthly climate table `T1-G2`
- differentiation column `04 III`
- named in Highways.md `T1-G5`
- notable figures `T3-01`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Marambio**
- differentiation column `04 III`
- notable figures `T3-01`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Palmer City**
- differentiation column `04 III`
- research log `Step 3.7`

**Port Lockroy**
- monthly climate table `T1-G2`
- differentiation column `04 III`
- named in Airports.md `T1-G5`
- notable figures `T3-01`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Rothera**
- differentiation column `04 III`
- notable figures `T3-01`
- research log `Step 3.7`

**Sejong**
- differentiation column `04 III`
- named in Highways.md `T1-G5`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Signy**
- differentiation column `04 III`
- named in Highways.md `T1-G5`
- named in Airports.md `T1-G5`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

## Halley Subnet — Queen Maud Land / Weddell Sea

**Abowasa**
- symbol pair `T1-G1`  ↳ *structural — **deliberately paused** pending its founding-nation fix — stated in the file*
- DoI Half B row `T1-G3`
- differentiation column `04 III`
- named in Airports.md `T1-G5`
- notable figures `T3-01`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`
- robot culture file `T2-5`

**Belgrano**
- differentiation column `04 III`
- notable figures `T3-01`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Halley**
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Lazar**
- differentiation column `04 III`
- notable figures `T3-01`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Neumayer**
- differentiation column `04 III`
- notable figures `T3-01`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Princess Elisabeth**
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Sanay**
- differentiation column `04 III`
- notable figures `T3-01`
- research log `Step 3.7`

**Troll**
- differentiation column `04 III`
- notable figures `T3-01`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

## Byrd Subnet — Marie Byrd Land

**Byrd**
- Census II figures `T0-3`
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

## Janbogo Subnet — Ross Sea

**Cape Adare**
- differentiation column `04 III`
- named in Airports.md `T1-G5`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Concordia**
- symbol pair `T1-G1`  ↳ *structural — capital — uses the zodiac district substrate, not the Planet+Element city system*
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`
- local culture file `T2-1`  ↳ *structural — capital — 301 district files under `Concordia-City/Districts/`*
- robot culture file `T2-5`  ↳ *structural — capital — district-level robot culture*
- megasheet `T2-1`  ↳ *structural — capital — district megasheets + Ultra Megasheet*
- enneagram read `T2-5`  ↳ *structural — capital — district-level Zodiac substrate*

**Denison**
- monthly climate table `T1-G2`
- founding population `T1-G4`
- differentiation column `04 III`
- named in Airports.md `T1-G5`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Dumont d'Urville**
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Fort McMurdo**
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Janbogo**
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`

**Scott**
- monthly climate table `T1-G2`
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Zukelli**
- monthly climate table `T1-G2`
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

## Mawson Subnet — East Antarctic Indian Ocean Coast

**Dome Fuji**
- Census II figures `T0-3`
- differentiation column `04 III`
- research log `Step 3.7`

**Mawson**
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Sayowa**
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

## Mirny Subnet — Wilkes Land / East Antarctic Plateau

**Casey**
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Davis**
- differentiation column `04 III`
- notable figures `T3-01`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Kunlun**
- Census II figures `T0-3`
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Mirny**
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Shirayuki**
- monthly climate table `T1-G2`
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`

**Sinheung**
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`

**Vostok**
- Census II figures `T0-3`
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

**Zhongshan**
- monthly climate table `T1-G2`
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`

## Amundsen Station — South Pole (inter-subnet relay; no subnet)

**Amundsen Station**
- symbol pair `T1-G1`  ↳ *structural — relay outpost, not a residential city*
- inspiration picks `T2-4`  ↳ *structural — relay outpost, not a residential city*
- differentiation column `04 III`
- concept art `T2-7`/`T3-18`
- research log `Step 3.7`

---

# 4. REGISTRY AND SOURCE DEFECTS found while auditing

**Four, all verified. Each is the kind that returns a confident wrong answer rather than an error.**

### 4a. ✅ **FIXED 2026-09-03** — a registry address that did not exist, on `G5`, the row every pass needs
**`00_RUNBOOK.md` §C registered `…/Cities/Locations/Infrastructure/Highways.md`.** ***That path did not
exist.*** **Real address: `…/Locations/Infrastructure/Highways.md` — `Infrastructure/` is a SIBLING of
`Cities/`.** **M-117 recurring inside the registry**, and Gate C's own recorded failure shape: *a pass
searches a space that structurally cannot contain the answer and gets a clean negative.*
**Corrected in §C on developer authorization; the row now carries the correction note. Verified to resolve.**

### 4b. ⭐ AN UNREGISTERED CANON SOURCE — and it is keyed by ALIAS, not by city name
**`Reference/Real-World/Climate Data/READER/` holds 37 per-city climate files.** ***It appears nowhere in the
canon registry `§B`–`§D`, and nowhere in `03` §0.3's Phase 1 or Phase 3 canon targets*** — both of which name
"climate data" as a required class without an address.

> **And most files are named for the REAL-WORLD STATION, not the Tepenian city** — `Aboa.md`, `Sejong.md`.
> *(`Bharati_TBD.md` → `Shirayuki.md`, 2026-09-04.)*
> ***A pass searching this folder for its subject's city name finds nothing and concludes the climate data is
> absent.*** **It is reachable only through the alias set (`Step −2` item 1a, M-118), which is exactly the
> mechanism that exists for this and has never been pointed at a canon folder.**

### 4c. A STALE SELF-REPORT IN THE CENSUS — Gate 0, failing in the flattering direction's opposite
**`Official_Population_Census.md` states: *"Denison… is therefore not yet included in Section III."***
***Denison IS in Section III, at row 16.*** **The note is stale.** **Gate 0's rule — *check the target, never
the claim; it fails in both directions* — catching a file under-reporting itself.**

### 4d. THE DIFFERENTIATION TABLE IS SCAFFOLDING, AND `CLAUDE.md` TREATS IT AS LIVE
**`02_Cross_City_Industry_Differentiation_Table.md` has 12 industry rows, 4 named city columns against a
`*(…32 more)*` placeholder, and ZERO content in any cell.** **`CLAUDE.md` requires the relevant row be read
BEFORE writing a category and the city's column added in the SAME COMMIT** — *"the only mechanical guard
against thirteen districts quietly converging."* ***The guard is currently empty at city scale.***

---

# 5. WHAT TO FIX FIRST

**Ordered by what unblocks the most work, not by how many cities are affected.**

| # | Action | Why first |
|---|---|---|
| **1** | ⛔ **Rule an EXTENT figure per city** *(developer decision — `05` §3: this binds many locations, so a pass may not decide it)* | Unblocks the `**Extent band:**` line, Gate 11's arithmetic, and the population/extent divergence finding — **for all 37 at once**. Already producing a live implausibility at Sayowa |
| **2** | **Fix the `§C` Highways address; register `Climate Data/READER/` with an alias note** | Two one-line registry edits that stop two classes of false-negative canon check |
| **3** | **Populate the differentiation table**, or mark it explicitly unbuilt | `CLAUDE.md` currently mandates a check against an empty instrument — the guard reads as running while doing nothing |
| **4** | **Backfill research logs** — 4 of 37 | Standing instruction since 2026-08-30. Also the only input that *stays admissible to a later cold run*, so every missing log is permanently lost provenance |
| **5** | **Census II for Byrd, Vostok, Kunlun, Dome Fuji** | `G8`'s retention technique — *"who left when leaving became possible"* — needs two snapshots. These four have one |
| **6** | **Monthly climate for the 7** · **notable figures for the 11** | Ordinary backfill against a known template |

> ## ⚠ THE FINDING BEHIND THE FINDINGS
>
> **The complete columns in §1 are the ones with a single aggregate owner** — census, influences, symbols,
> Half B, the relationship files. ***Every one of them is complete or near-complete.***
>
> **The empty columns are the ones that need a PER-CITY artifact** — research logs, concept art, the
> differentiation table, extent. ***Every one of them is at or near zero.***
>
> **That is not thirty-seven separate oversights. It is one structural fact:** *this corpus is excellent at
> filling a table that already has a row for every city, and has no mechanism that notices when a per-city
> artifact was never created.* **A missing row in an aggregate file is visible. A missing file is not.**
>
> ***The ULM's own input contract has no completeness check — `05` §7's pre-flight is run BY a pass, ABOUT
> the one city it is writing.*** **Nothing in the methodology ever asked this question across the corpus
> until it was asked by hand today.**
