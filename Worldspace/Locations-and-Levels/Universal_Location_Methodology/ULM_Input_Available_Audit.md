# ULM INPUT-AVAILABLE AUDIT — what each of the 37 chartered cities is MISSING

**Measured 2026-09-03. ⭐ RE-MEASURED 2026-09-04 (second pass) — §1, §1b, §3 and §5 all re-derived from the
spec files, not carried forward.** **Basis of reference: `ULM_Input_Required_Reference.md`, in this folder.**
**Read them as a pair — that file is the bar; this file is the measurement.**

> ## ⭐⭐ WHERE IT STANDS, IN ONE BLOCK — **2026-09-04, second re-measure**
>
> | | Count |
> |---|---|
> | ⭐⭐ **INPUT PREP REMAINING** | ***TWO. Developer ruling, 2026-09-04.*** **① `Ports.md`** *(empty — §4e)* · **② `EXTENT / AREA`** *(0/37 — §2)*. ⛔ ***"once … those [are done] … we'll start actually synthesizing locations via the ULM."*** |
> | ⏸️ **Deferred out of input prep** | **`G6` defining event** *(24/37 — belongs with city HISTORIES, later)* · **`RESEARCH LOGS`** *(5/37 — **an output of synthesis, not an input to it**)* |
> | ✅ **Closed since the first measurement** | **monthly climate** *(30→37)*, **the whole 13-field climate block**, **founding population** *(36→37)*, **symbol pair** *(35→36)*, ⭐ **`T1-G5` network position — BOTH halves, 37/37**, **inspiration picks** *(36→37, alias fix)*, **DoI Half B** *(36→37, stale row)*, **both registry fixes** |
> | ⛔⛔ **Registry addresses found BROKEN** | **THREE, all M-117** — `Highways.md` *(sibling-path, fixed 2026-09-03)* · `READER/` *(alias-keyed)* · ⭐ **`World_History_Reference.md` *(7-line forwarding stub; content moved repos 2026-07-11)*, found 2026-09-04** |
> | ⛔ **Struck from scope — not gaps** | **Census II · notable figures · concept art · national medical** *(2026-09-03)* **+ the differentiation table** *(2026-09-04)* |
> | ⏸️ **Deliberately paused — not gaps to fill** | **Abowasa** *(blocked upstream on its founding-nation fix)* · **Concordia** *(district methodology)* |
>
> ⭐ **The first measurement listed 12 problem rows. Five were struck as invalid metrics, four closed, and
> what remains is two.** ⚠ ***And one of the two — extent — is a developer ruling, not a research task.***

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
| ~~**Differentiation table column** `04` Part III~~ | — | — | ⛔ **STRUCK 2026-09-04 — NOT A GAP, and this row was a category error.** **The cities' own table says so in its own header** *(`Cross_City_Culture_Differentiation_Table.md`, created 2026-09-04)*: ***"NOT A PREREQUISITE. This file is FILLED IN during location synthesis, not before it… Do not record its emptiness as a gap."*** **It contributes nothing to the first city and everything to the thirty-seventh.** ⚠ **This row previously ranked #3 in §5 — that ranking was wrong.** *See §5's revision note* |
| ~~**Research log** `Step 3.7`~~ | **5** | ~~32~~ **n/a** | ⛔ **NOT A PREREQUISITE — developer ruling, 2026-09-04:** ***"research logs get done while actually synthesizing locations."*** **The log is an OUTPUT of a pass, produced during it.** *A city with no log is a city that has not been synthesized yet — which is every city, and is the normal state before the work starts.* ⛔ **Do not record its absence as an input gap.** ⚠ *The Step 3.7 instruction still stands in full: **every** pass writes one.* |
| ~~**Concept art** `T2-7`/`T3-18`~~ | ~~4~~ **37 dirs · 5 with images** | ~~33~~ | ⛔ **STRUCK 2026-09-03** *(Tier 3 optional; input value exists only if art PRECEDES the pass)*. ⚠⚠ **BUT THE STATED REASON WAS FALSE, corrected 2026-09-04:** this row claimed the layout is *"BY SUBNET, not by city… any per-city count is structurally meaningless."* ***It is `<Subnet>/<City>/` — subnet AND city.*** **A per-city count is well-defined: 37/37 directories exist, 5 hold images** *(Concordia · Dome Fuji · Palmer City · Rothera · Sanay)*. *Struck either way, so nothing downstream changes — but the reason was wrong. See `ULM_Input_Required_Reference.md` §J* |
| ~~National medical/care entry~~ | ~~15~~ | ~~22~~ | ⛔ **STRUCK 2026-09-03 — the metric was invalid.** *The source names **3 national institutes**, not 37 city entries; 12 of the 15 "present" were free-text false positives* |
| ~~**Notable figures** `T3-01`~~ | ~~26~~ | ~~11~~ | ⛔ **STRUCK 2026-09-03 — circular by construction**, and the count was untrustworthy besides *(placeholder test returned 0, TBD test returned 32)* |
| ~~**Monthly climate table** `T1-G2`~~ | ~~30~~ **37** | ~~7~~ **0** | ✅ **CLOSED 2026-09-04 — and the row is now far bigger than it was.** See the **CLIMATE BLOCK** immediately below |
| ~~Named in `Airports.md` `T1-G5`~~ | ~~31~~ **37** | ~~6~~ **0** | ✅ **CLOSED — and it was already closed when this audit was written.** *`Airports.md` was rewritten **2026-09-03** with an **"Everything Else Has No Air Access — all 23, named"** section that replaced an `"…and others"` catch-all and enumerated **exactly the six cities this row flagged** — {{Abowasa}}, Cape Adare, Denison, Esperanza, Port Lockroy, Signy. The file's own note says those six *"carried no explicit statement either way."** ⭐ **All 37 now resolve: 10 host · 3 served-not-host · 23 named as having none.** ⚠ *Same-day miss: the fix and the measurement were both 2026-09-03* |
| ~~**Census II figures** `T0-3`~~ | ~~33~~ | ~~4~~ | ⛔ **STRUCK 2026-09-03 — not a gap.** *Only Census I matters; it is the peak load a city must physically hold, and it is complete 37/37* |
| Symbol pair `T1-G1` | **36** | **1** | ✅ **Amundsen Station added 2026-09-04 — Neptune + Electromagnetism**, with a full derivation section in the assignments file. ⛔ **Only Concordia remains** *(district methodology)*; **Abowasa is explicitly excluded in-file** pending its founding-nation fix. ⚠ *The prior '3 absent, all three deliberate' was only verifiable for Abowasa — Amundsen's absence carried no note either way, and turned out to be an omission rather than a decision.* |
| ~~Named in `Highways.md` `T1-G5`~~ | ~~34~~ **37** | ~~3~~ **0** | ✅ **CLOSED 2026-09-04.** *`Highways.md` now carries a **"Cities With No Highway Access — all 3, named"** section: **Juan Carlos · Sejong · Signy**, with the verified island distances and the 0.93 km Picnic Passage comparison.* ⭐ **It was never a data gap** — the reasoning already existed in all three specs under `**Highway access:**`; it was simply absent from the file `G5` actually reads. **They are exactly and only the three cities carrying `**Access type:** NONE`** |
| ⭐⭐ **`T1-G5` NETWORK POSITION — the whole input** | **37** | **0** | ✅✅ **FULLY CLOSED 2026-09-04.** *Both halves now resolve for all 37: `Airports.md` (10 host · 3 served-not-host · 23 declared none) and `Highways.md` (34 named · 3 declared none).* ⛔ ***But see §4e — the sea network those declarations hand off to is undocumented*** |
| ~~Founding population `T1-G4`~~ | ~~36~~ **37** | ~~1~~ **0** | ✅ **CLOSED 2026-09-04 — Denison.** ⚠ **The data was never missing; it was UNADDRESSABLE** — held as prose inside the `Settled:` paragraph, so a sweep for the literal `**Founding population:**` field reported a false gap. *Now a proper field; presence test recorded on `T1-G4`.* |
| ~~Inspiration picks `T2-4`~~ | ~~36~~ **37** | ~~1~~ **0** | ⛔⛔ **THIS ROW WAS WRONG IN ALL THREE PARTS — corrected 2026-09-04.** *It read "1, structural," meaning Amundsen Station.* ***The picks exist, there are SEVEN, tiered 3 PRIMARY / 2 SECONDARY / 2 SUPPORTING — richer than most cities.*** **They were unreachable because the heading was keyed `Amundsen-Scott Station`** — the only entry in that file under its REAL-WORLD name, and the only one under a non-subnet heading. ⭐ **Same defect class as `Climate Data/READER/`. FIXED: heading now carries both names.** *Full account: `ULM_Input_Required_Reference.md` §J* |
| ⏸️ **`G6` defining event** `T1-G6` | **24** | **13 — DEFERRED** | ⛔⛔ **THE ADDRESS WAS WRONG TWICE. Now measured properly, 2026-09-04.** *This row read "36/1, missing Shirayuki" — wrong: `G6` pointed at `## Current Status / Destruction`, `## Legacy` and `## Connection to Concordia`, **all three POST-WAR** and inadmissible under the Second Interwar default, so the 36 "present" were false positives. **The first fix then pointed at the GDD's `World_History_Reference.md`, which is a 7-line FORWARDING STUB naming zero cities** (content moved to the Timeline repo 2026-07-11).* ✅ **Address now absolute, to the real 346-line file + the Second Interwar era directory.** ⛔ **13 cities are named in NEITHER: Abowasa · Esperanza · Halley · Marambio · Mirny · Princess Elisabeth · Rothera · Sanay · Sayowa · Shirayuki · Signy · Sinheung · Troll.** ⏸️ **DEFERRED — developer ruling 2026-09-04:** ***"that's a problem for another time, once we start figuring out the actual histories of cities. So, for now, we don't need to worry about 'defining events'."*** ⭐ **`02` supports deferring it specifically: `G6` scores LOW on Absence — the only generator that does. A missing `G6` yields nothing, unlike `G4`, where the absences ARE the yield. So these 13 run on the other seven generators rather than running short.** |
| ~~DoI Half B row `T1-G3`~~ | ~~36~~ **37** | ~~1~~ **0** | ✅ **CLOSED — stale row, corrected 2026-09-04.** *The missing one was Abowasa; it **is** in `16_Per_City_Three_Tier_Run.md`'s Half B table, keyed `{{Abowasa}}` with placeholder braces* |
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

# 3. PER-CITY GAPS — **rebuilt 2026-09-04 from the second re-measure**

> ## ⚠⚠ THIS SECTION WAS THE STALEST PART OF THE FILE
> **§1 and §1b were updated on 2026-09-04 as fields closed. §3 was not.** ***It went on listing monthly
> climate for seven cities, founding population for Denison and the symbol pair for Amundsen — all of which
> had already been closed and marked closed twelve lines further up in the same file.***
>
> **It also listed the four fields struck from scope on 2026-09-03** *(Census II · notable figures · concept
> art · national medical)* **under every city they applied to, so a reader working from §3 would have worked
> on struck metrics.**
>
> ⭐ **Recorded rather than quietly repaired, per Step 9.5.** ***The failure shape: a summary table and its
> per-item detail maintained separately, with only the summary kept current.*** **The detail is where the
> work actually gets picked up from, so this is the more damaging half to leave stale.**

**Rebuilt to list ONLY live, in-scope gaps.** *Struck fields are excluded entirely. Closed fields are
excluded entirely.* **`↳ structural`** *marks an absence that is correct by design and must never be 'fixed'.*
**`↳ paused`** *marks one deliberately held, not neglected.*

---

## ⭐ THE DEFAULT CASE — **32 of 37 cities have exactly ONE live gap, and it is the same one**

> # ⛔ A RESEARCH LOG. **That is the whole list for most of the corpus.**

**Every city has one EXCEPT these five, which already hold logs:**
**Janbogo** · **Mawson** · **Shirayuki** · **Sinheung** · **Zhongshan**

⚠ **`EXTENT` is missing for all 37 and is deliberately NOT repeated per city** — it is a single developer
ruling, recorded once in §2, not thirty-seven research tasks.

---

## THE EXCEPTIONS — **every city with anything beyond the research log**

| City | Additional live gap | Kind |
|---|---|---|
| ⛔ **Abowasa** | **DoI Half B row** `T1-G3` · symbol pair `T1-G1` ↳ *paused* · robot culture file `T2-5` ↳ *paused* | ⛔⛔ **ALL THREE ARE BLOCKED UPSTREAM, NOT OPEN WORK** — see the block below. *(Its `Airports.md` entry is now present — **served via Troll or Belgrano**, developer-confirmed 2026-09-03.)* |
| **Amundsen Station** | inspiration picks `T2-4` ↳ *structural* | relay outpost, not a residential city |
| **Concordia** | symbol pair · local culture file · robot culture file · megasheet · enneagram read — **all** ↳ *structural* | **capital — runs the zodiac DISTRICT substrate**, 301 files under `Concordia-City/Districts/`. ⛔ **Not the city methodology. Never 'fill' these** |

> ### ⛔⛔ ABOWASA — **four gaps, ONE cause. Do not work any of them.**
> **Its premise rests on a *"Finnish and Swedish exiles, jointly"* founding that the project's own First
> Interwar turnover history does not support surviving intact** *(`TODO.md` §377; developer-confirmed, same
> bug class as Sejong's Hangul fix)*. **The fix touches the city's NAME, demonym, dual-national trait and
> Turku Remembrance holiday** — *"Abowasa" is literally **Aboa + Wasa**, and the build tracker already marks
> the name provisional.*
>
> ⚠ ***Running any of the four now would need a full redo.*** **Fixing the founding nation closes all four at
> once, and it is the highest-leverage single item in the corpus after extent.**

---

## ⭐ WHAT THIS SECTION LOOKED LIKE BEFORE, AND WHY THE DIFFERENCE MATTERS

| | First measure *(2026-09-03)* | Second *(2026-09-04)* |
|---|---|---|
| **Cities with 4+ listed gaps** | **35 of 37** | **1** *(Abowasa — all blocked)* |
| **Distinct field classes listed** | **12** | **4** *(research log · 2 infrastructure rows · Half B)* |
| **Cities whose only gap is the research log** | 0 | ⭐ **32** |

> **The corpus did not improve by that much in one day.** ***Most of the difference is that five metrics were
> invalid or out of scope and four fields genuinely closed.*** **The first measure was not measuring the
> right things** — *which is itself the finding, and is why §0's instrument-defect record exists.*


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

### 4e. ⛔⛔ **`Ports.md` IS EMPTY — 0 BYTES — and closing `T1-G5` is what exposed it**

**`Locations/Infrastructure/Ports.md` exists, sits beside `Highways.md` and `Airports.md` in the same
registered folder, and contains nothing at all.**

> ### ⭐ It was invisible until the negatives were declared
> **This audit tests `Airports.md` and `Highways.md`. It never tested `Ports.md`, because no input row points
> at it.** ***And the two files it does test both resolved cleanly*** — every city now has a positive
> statement. **But four of those statements resolve TO THE SEA:**
>
> | City | Where its access statement now points |
> |---|---|
> | **Juan Carlos** | maritime + Machu Picchu Airport |
> | **Sejong** | maritime + Machu Picchu Airport |
> | ⛔ **Signy** | ***maritime ALONE*** — no road, no air |
> | **Palmer City** | Hwy 1 ramp, then ***"a boat crossing… not a road"*** |
>
> ⛔ **So `G5` is complete in the sense that every city has an answer, and incomplete in the sense that one of
> the answers leads somewhere with no content.** ***A pass following the chain gets a clean, confident,
> correctly-formed handoff into an empty file.*** **That is Gate C's own failure shape** — *a search of a
> space that structurally cannot contain the answer* — **reached this time by a route that looks like
> success.**

⚠ **NOT resolved here, and possibly not a defect:** *the file may be empty on purpose, the way several
absences in this audit turned out to be.* ⛔ **But it is now load-bearing for four cities and must be
explicitly ruled either way rather than left as an untested 0-byte file in a registered folder.**

---

# 5. WHAT TO FIX FIRST

> # ⭐⭐ DEVELOPER RULING, 2026-09-04 — **THE ORDER FOR 2026-09-05 IS SET**
>
> > ***"tomorrow, first, we need to address `Ports.md`, because that's extremely important. Then, once
> > that's done, we'll go through and establish 'Extent / Area'."***
>
> | | |
> |---|---|
> | **1st** | ⛔ **`Ports.md`** *(§4e)* — **developer-designated "extremely important."** *It surfaced only hours before this ruling, and it outranks everything below* |
> | **2nd** | **EXTENT / AREA** *(§2)* |
>
> ⚠⚠ **BEFORE the extent session can produce anything, `Extent_and_Area_APPROACH.md` §7's FOUR RULINGS must
> be made** — **settlement form per city · built mode · band widths · whether Tepenian engineering exceeds
> real-world limits and by how much.** ***That file's §8 forbids deriving any figure until they are.***
> ⭐ **So the extent session opens with rulings, not with research.** *Start there or the day stalls at the
> first city.*

**The table below is this audit's own analytical ranking, retained for reasoning. ⭐ The ruling above
overrides its ordering.**

> ### ⭐ REVISED 2026-09-04 — **four of the original six are gone.** *Two were done, two were invalid.*
>
> | Original | What happened |
> |---|---|
> | ~~**2** — registry fixes~~ | ✅ **BOTH DONE.** *`§C`'s Highways path corrected 2026-09-03; `Climate Data/READER/` now registered in `§C.9` and in the Step 1 / Step 3 canon targets, **with the alias-keying warning attached*** |
> | ~~**3** — populate the differentiation table~~ | ⛔ **INVALID — it was never a prerequisite.** *The cities' table states in its own header that it is filled DURING synthesis and that its emptiness must not be recorded as a gap. **Ranking it third was the error***, and it is corrected in §1 |
> | ~~**5** — Census II for four cities~~ | ⛔ **STRUCK** — *only Census I matters, and it is 37/37* |
> | ~~**6** — monthly climate for the 7~~ | ✅ **DONE 2026-09-04 — 37/37**, along with twelve further climate fields *(§1b)*. *The notable-figures half was struck* |

| # | Action | Why first |
|---|---|---|
| **1** | ⛔ **Rule an EXTENT figure per city** *(developer decision — `05` §3: this binds many locations, so a pass may not decide it)* | Unblocks the `**Extent band:**` line, Gate 11's arithmetic, and the population/extent divergence finding — **for all 37 at once**. Already producing a live implausibility at Sayowa. ⭐ **Approach written: `Extent_and_Area_APPROACH.md`. It is BLOCKED ON THE §7 RULINGS, not on research** |
| **2** | ⛔ **Fix ABOWASA's founding nation** | ⭐ **The highest-leverage single item after extent: it closes FOUR of that city's gaps at once** *(symbol pair · robot culture file · DoI Half B · and possibly the city's NAME)*. **Everything about Abowasa is parked behind it**, and it is the same bug class as Sejong's Hangul fix, which is already solved and can be followed |
| ~~**3**~~ | ~~Backfill research logs~~ | ⏸️ **REMOVED from input prep, 2026-09-04 — *"research logs get done while actually synthesizing locations."*** *They are written BY a pass, not before it.* ⚠ **The Step 3.7 instruction is unchanged: every pass writes one, and it stays the only input admissible to a later cold run** |
| ~~**4**~~ | ~~Write one paragraph into `Highways.md`~~ | ✅ **DONE 2026-09-04 — `T1-G5` is fully closed.** *Section written: "Cities With No Highway Access — all 3, named."* |
| **4** | ⛔ **Rule on `Ports.md`, which is EMPTY (0 bytes)** — *see §4e* | ⭐ **Newly surfaced 2026-09-04, and it is the direct consequence of closing `G5`.** **Four cities are sea-dependent** *(Juan Carlos · Sejong · Signy · Palmer City)* **and both infrastructure files now hand them off to a maritime network that has no content.** ⚠ **Signy is reachable by sea ALONE.** *Either it is a real gap or the file is empty on purpose — but `G5` now points at it, so it cannot stay unmarked* |

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

> # ⛔⛔ THE CATEGORY ERROR THIS AUDIT KEPT MAKING — **named 2026-09-04, after the third instance**
>
> ***This file repeatedly counted OUTPUTS OF SYNTHESIS as INPUTS TO IT, and ranked them as blocking work.***
>
> | Counted as a gap | Actually |
> |---|---|
> | **Differentiation table** *(ranked #3)* | **filled DURING synthesis** — its own header says *"NOT A PREREQUISITE… Do not record its emptiness as a gap"* |
> | **Research logs** *(ranked #3 after the above was struck)* | ⭐ **written BY a pass** — *"research logs get done while actually synthesizing locations"* |
> | **Concept art** | its own struck-note says it — *"input value exists only if it PRECEDES the pass; made after, it is illustration"* |
>
> ⭐⭐ **All three occupied the top of the priority list at some point. None of them was ever input prep.**
> **Together they accounted for most of the corpus's apparent incompleteness** — *research logs alone were
> "32 missing," the single largest number in the original table.*
>
> > ### THE TEST, so this stops recurring
> > ***Would a pass READ this to write the location, or WRITE it while doing so?*** **Read it → input.
> > Write it → not a gap, and never a prerequisite.** ⛔ **An empty artifact of the second kind is not
> > evidence of incompleteness. It is evidence that the work has not started**, which is the state input prep
> > exists to end.

> ## ⭐ ADDENDUM 2026-09-04 — **the finding survived the re-measure, and got sharper**
>
> **Two of the four examples above were struck** *(concept art, the differentiation table)*, **so the claim
> could have collapsed. It did not.** ***What is left is the cleanest possible version of it:***
>
> | | |
> |---|---|
> | **Aggregate-owned fields** | ⭐ **Census I · symbols · influences · Half B · relationships · and now the ENTIRE 13-field climate block — all 37/37** |
> | **Per-city-artifact fields** | ⛔ **research logs 5/37 · extent 0/37** |
>
> **The climate block is the proof, not the exception.** *It went 30→37 and then added twelve more complete
> fields in a single day* — **because it is a table with a row per city, and a missing row is visible.**
> ***Research logs have moved by one file in five days, because a missing file is not.***
>
> ⛔⛔ **AND THIS FILE JUST DEMONSTRATED THE SAME FAILURE ON ITSELF.** **§1 was kept current as fields closed;
> §3 — the per-city detail, the part work is actually picked up from — was left listing seven closed climate
> gaps, a closed founding population, a closed symbol pair and four struck fields.** ***A summary row is
> visible. Detail two hundred lines below it is not.*** **Same shape, one file, four weeks apart.**
