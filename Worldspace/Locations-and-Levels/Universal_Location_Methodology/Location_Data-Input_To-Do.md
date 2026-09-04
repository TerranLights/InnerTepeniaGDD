# LOCATION DATA-INPUT TO-DO — ranked by how many cities are missing the field

**Drafted 2026-09-03.** **Tally taken from `ULM_Input_Available_Audit.md`; the bar is
`ULM_Input_Required_Reference.md`.** *(All three files live in this folder and are read together.)*

> ## THE RANKING RULE, stated so it can be checked
> ***Priority = the number of cities missing that field.*** **More cities missing it ⇒ higher priority.**
> **Where two fields tie, the tie-break is stated explicitly in the row.** ***No other weighting is applied***
> — impact, effort and interest are deliberately NOT in the ranking, so the order is reproducible by anyone
> re-running the count.

> ### ⚠ CENSUS — STRUCK FROM THIS LIST ENTIRELY *(developer ruling, 2026-09-03)*
>
> **What the two censuses actually are, stated plainly — developer, verbatim:**
>
> | | |
> |---|---|
> | **Census I** | ***"fully and entirely on Earth (i.e., in Antarctica)"*** |
> | **Census II** | ***"Antarctica after some have begun colonizing space (beginning in Low-Earth Orbit)"*** |
>
> ***"That's literally all it is."*** **Census II is not a gap, is not tracked, and is not relevant to what a
> city is like** — *"those are just pre- and post-orbital colonization."*
>
> ### ⭐ THE CONSEQUENCE, AND IT IS A SIZING RULE, NOT A BOOKKEEPING NOTE
> ***"Therefore, Census I will ALWAYS be a larger number, therefore that's the number we calculate by (since a
> particular city needs to be able to accommodate that many people at any one single time)."***
>
> **So Census I is not merely the earlier snapshot — it is the PEAK LOAD the built city must physically
> hold.** **`Census I` is COMPLETE, 37 of 37, so the census contributes nothing to this list.**
>
> **This is independently consistent with `00_RUNBOOK.md` §C.6's standing convention (M-137):** *every
> process-derived figure in this corpus baselines on Census I regardless of which census a location's own
> narrative frame uses.* ***Two different routes, same denominator.***
>
> ⭐ **And it fully specifies item 1.** The density check is `Census I ÷ extent`. **The numerator exists for
> every city. The missing half is extent, and only extent.**

---

# THE RANKING

> ### ⚠⚠ THE RANKING RULE HAS A BLIND SPOT — read this before working the list top-down
> ***Ranking by "how many cities are missing it" systematically OVER-ranks cheap, optional fields and
> UNDER-ranks blocking ones.*** **The count is a good first cut. It is not a priority order on its own.**
>
> | | |
> |---|---|
> | **Over-ranked** | a Tier 3 *optional* field absent from 33 cities scores above a Tier 1 *spine generator* absent from 1 |
> | **Under-ranked** | **Founding population** sits near the bottom on a count of 1 — **and it is a `G4` spine input.** Its city cannot build a three-generator profile without it |
>
> **Two fields have already been REMOVED on this basis** *(see §Removed)*. **`National medical` at #4 is the
> next candidate and is flagged advisory in place.** ***When the count and the tier disagree, the tier wins.***

| # | Field | Cities missing | Tier | Tie-break / note |
|--:|---|--:|---|---|
| **1** | **EXTENT / AREA** | **37** | `T2-8` | tie at 37 — **first because it is the only blocker that disables an entire QA gate**, and because it is a `RESERVED` developer decision nothing else can route around |
| **2** | **Differentiation table column** | **37** | `04` Part III | tie at 37 — second because a pass can proceed without it; it degrades the anti-convergence guard rather than blocking a phase |
| **3** | **Research log** | **33** | `Step 3.7` | **the loss is PERMANENT**: a log is the only input that stays admissible to a later cold run, so an un-logged search is provenance destroyed, not deferred |
| ~~**4**~~ | ~~**Monthly climate table**~~ | ✅ **0** | `T1-G2` | ✅ **CLOSED 2026-09-04 — 37/37, plus 6 new complete climate classes** |
| ~~5~~ | ~~Named in `Airports.md`~~ | ~~6~~ | `T1-G5` | ✅ **RESOLVED 2026-09-03 — all 37 now explicitly stated; file reconciles 11+3+23=37.** See §5 |
| ~~6~~ | ~~Named in `Highways.md`~~ | ~~3~~ | `T1-G5` | ✅ **RESOLVED 2026-09-03 — developer-confirmed; was never a gap.** See §6 |
| **7** | **Founding population** | **1** | `T1-G4` | ⭐ **count says last; TIER says otherwise — this is a `G4` SPINE input.** Work it early despite the count |
| **8** | DoI Half B row | **1** | `T1-G3` | — |
| **9** | Robot culture file | **1** | `T2-5` | ⏸️ **blocked, not open** — see §Blocked |

---

# 1. EXTENT / AREA — **37 of 37**

**No city has a declared built extent.** **`01` §2 requires two bands declared, population *and* extent;
`01` §6's declaration block has a mandatory `**Extent band:**` line; `00_RUNBOOK.md` Step 2 item 6 orders the
division and calls it *"the cheapest plausibility check in the methodology."***

> **`04` Gate 11's ONLY recorded catch came from that division, and `04`'s own verdict is that the part which
> fired *"was the part that was arithmetic… the only part of this gate that does not run on the same faculty
> that produced the error."*** ***The one instrument immune to the author's own blind spots cannot be run for
> any city in the project.***

**Six cities have an area figure and NONE of them is a city extent** — each measures the real-world *site*:
Cape Adare (2.94 km² cape) · Denison (1.11 km² ASMA) · Davis (~400 km² oasis) · Lazar (~34 km² oasis) ·
Sayowa (~4–5 km² island) · Sinheung (~34 km² hills). **They measure the real-world SITE, not the city.**

> # ⛔⛔ STANDING CORRECTION — **ICE-FREE AREA IS NOT A CONSTRAINT ON CITY EXTENT.**
> **Developer correction, 2026-09-03, after this error recurred across sessions:**
> ***"For some reason, you have incredible difficulty understanding me when I tell you that it's not
> necessary to only build on non-iced earth."***
>
> ### ⛔ TEPENIAN CITIES BUILD ON ICE. This is established canon, not a permission being sought.
> | City | Built on |
> |---|---|
> | **Halley** | **the Brunt Ice Shelf** — and its own spec records that it *risks eventually calving off into the ocean*, which is why the subnet's Arcanet nexus was placed at Sanay instead |
> | **Neumayer** | ***"built on the Ekström Ice Shelf rather than on bedrock, which has structural implications for long-term city stability"*** |
>
> ### Therefore the six figures above BOUND NOTHING
> **An ice-free oasis, a cape, an ASMA zone and an island are facts about the real-world research site.**
> ***They are not a ceiling on where a Tepenian city may be built, how far it may extend, or how many people
> it may hold.*** **A prior version of this section called them *"upper bounds on habitable land"* — that
> was wrong, and it is the exact misreading the developer is correcting.**
>
> **⚠ The recurrence is the reason this is written as a standing block rather than a footnote.** ***Assuming
> bedrock-only construction is an unstated real-world assumption smuggled into a fictional setting that has
> already ruled otherwise*** — the same class as `Disciplines/Real-World_Basis_Extrapolation_Method.md`'s
> standing principle: **a real-world basis is a COORDINATE, never a CAUSE.**
>
> ### ⏸️ DENSITY AND EXTENT ARE DEFERRED — developer instruction, 2026-09-03
> ***"The issue of density has to be addressed another time… we leave that for some other time later."***
> **Do not derive, propose, or assume an extent figure in the meantime.** **This item stays ranked #1 and
> stays OPEN.**

**⚠ Already producing a live, unresolved implausibility:** **Sayowa's own spec has run the division and
recorded *"225,376 people on ~4–5 km² is ~50,000/km² — the implausibility…"*** and **Cape Adare's spec says
outright *"the exact figure is a worldbuilding decision, not an arithmetic one."***

**Needs:** a developer ruling — `05` §3 RESERVED, because it binds every location and a pass may not settle it.
**Sensitivity: HIGH.** Density is the premise of texture findings across the corpus.

**Cities:** all 37.

> ## ⭐⭐ THE RULING IS PROBABLY ONE NUMBER, NOT THIRTY-SEVEN
>
> **`density = Census I ÷ extent`.** **Census I is complete for all 37 and is now defined as the PEAK LOAD the
> city must physically hold.** ***So the two unknowns are locked together, and fixing either one derives the
> other for the entire corpus at once.***
>
> | Rule this | And this falls out arithmetically |
> |---|---|
> | **A plausible DENSITY band** *(or a per-tier band)* | **extent, for all 37** — `extent = Census I ÷ density` |
> | **EXTENT from real geography** *(ice-free bedrock available)* | **density, for all 37** — and it will be very high |
>
> ### ⚠ And the second option is partly forced already, which is what makes this urgent
> **For several cities extent is NOT free — it is bounded above by real ice-free land:** **Denison 1.11 km²**
> *(its own spec notes the true bedrock figure is LESS)* · **Cape Adare 2.94 km²** · **Sayowa ~4–5 km².**
> **Against Census I populations in the hundreds of thousands, those bounds force extreme density whether
> anyone rules on it or not.**
>
> ### ⭐ THE CORPUS MAY ALREADY CONTAIN THE ANSWER — and it points at "extreme density is correct"
> ***`Inspirational-Influences.md` gives Denison a PRIMARY pick of **Kowloon Walled City** — annotated in the
> file itself as "reaching the highest population density ever recorded," with 300+ towers so interlinked that
> "the whole thing functioned as a single organism rather than separate buildings."*** **Its SECONDARY pick is
> Montreal's RÉSO — 32 km of interconnected climate-shielded tunnels "used by 500,000+ people daily."**
>
> > **So a hyper-dense, vertically-stacked, single-continuous-structure city is not an accident in this
> > setting. It is a deliberate, documented design intent for at least one city — and it is exactly what an
> > enclosed hostile-environment settlement on 1 km² of bedrock would have to be.**
>
> ### ⚠ Which means Sayowa's flagged "implausibility" may not be an error at all
> **~50,000/km² is roughly Kowloon's real historical density.** ***If extreme density is the Tepenian norm,
> Sayowa's number is not a bug to fix — it is a characterizing fact that has been sitting mislabeled as a
> problem.*** **`05` §5 asks what changes if the answer comes back differently, and here the two answers are
> opposite in kind:** *a density ruling either RETIRES that flag as correct-and-characterizing, or confirms it
> as a real population/geography conflict needing population revision.* **Nothing else on this list has that
> property.**

# 2. DIFFERENTIATION TABLE COLUMN — **37 of 37**

**`02_Cross_City_Industry_Differentiation_Table.md` holds 12 industry rows, 4 named city columns against a
`*(…32 more)*` placeholder, and ZERO content in any cell.** **`CLAUDE.md` requires the relevant row be read
BEFORE writing a category and the city's column added in the SAME COMMIT** — *"the only mechanical guard
against thirteen districts quietly converging."* ***At city scale the guard is currently empty.***

**Needs:** either populate it, or mark it explicitly unbuilt so the mandated check is not run against nothing.

**Cities:** all 37.

# 3. RESEARCH LOG — **33 of 37**

**Standing developer instruction since 2026-08-30** *(`Step 3.7`; convention in `Research_Logs/README.md` and
`Disciplines/Real-World_Basis_Extrapolation_Method.md` Step F)*. **Records the exact search strings verbatim,
sources used, a fact-by-fact *what came back → which finding it became* table, withheld vs. omitted,
divergences from source, and open threads.**

> ### ⭐ Why this ranks above concept art at the same count
> **A research log is the ONLY input that stays admissible to a later cold run on the same location** — it
> records attributes, never conclusions. ***So an unwritten log is not deferred work; it is provenance
> permanently destroyed.*** **And it loses every deliberately-unpursued thread, which the runbook records as
> "routinely the best material the research produced."**

**HAVE (4):** Janbogo · Shirayuki · Sinheung · Zhongshan
**MISSING (33):** Abowasa, Amundsen Station, Belgrano, Byrd, Cape Adare, Casey, Concordia, Davis, Denison,
Dome Fuji, Dumont d'Urville, Esperanza, Fort McMurdo, Halley, Juan Carlos, Kunlun, Lazar, Marambio, Mawson,
Mirny, Neumayer, Palmer City, Port Lockroy, Princess Elisabeth, Rothera, Sanay, Sayowa, Scott, Sejong, Signy,
Troll, Vostok, Zukelli

# 4. ~~MONTHLY CLIMATE TABLE~~ — ✅ **CLOSED 2026-09-04**

> ## ✅ **37 of 37.** And the row grew rather than merely closing.
>
> **Also now complete at 37/37:** `Avg High (day)` · `Mean` · `Avg Low (night)` · `Precip` ·
> `Precip Probability` · `Daylight` · **solstice min/max** · ⭐ **precipitation regime**
> *(falls / lands / lost, and a WIND-vs-COLD statement per city)* · ⭐ **per-column provenance** ·
> ⭐ **Access type**.
>
> **Still open, and NOT research tasks:** monthly `Rec High`/`Rec Low` at **25 complete / 9 partial /
> 3 none**; `Prevailing winds` missing in 3; `Record extremes` header missing in 7.
> ⛔ **Abowasa, Dome_Fuji, Princess_Elisabeth and Cape_Adare need PROXY RULINGS** — the nearest stations
> are 240–430 km away, and the 2026-09-04 pass exhausted BAS READER, NOAA NCEI (68 stations), published
> climate boxes in five languages and the national met services. **The data does not exist to be found.**
>
> **Full detail:** `ULM_Input_Available_Audit.md` §1b · `Reference/Real-World/Climate Data/Climate_Data_Corpus_Audit_2026-09-04.md`
>
> *Historical record of the original gap follows.*

## ~~Original entry — 7 of 37~~

**These 7 specs have no monthly table at all** — the `### Annual Climate` block exists, but the 12-row
Month/Temp/Precip/Daylight table is absent entirely. **`T1-G2`, the near-universal primary generator.**

> ### ⭐ PART OF THIS IS ALREADY SOURCED — but measure the claim before relying on it
> **`/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Climate Data/READER/`
> holds 37 per-city files** — **BAS READER, WMO 1991–2020 standard normals, with citation.** ***Registered in
> `00_RUNBOOK.md` §C.9 and at the point of use in §C.8c Phases 1 and 3 — it had been registered NOWHERE.***
>
> ⛔ **MOST FILES ARE NAMED FOR THE REAL-WORLD STATION, NOT THE CITY** — `Aboa.md` ·
> `Princess_Elizabeth.md` *(note the `z`)* · `Sejong.md`. ***A search by Tepenian name can return nothing
> and conclude the climate data is absent.*** **Reachable through the ALIAS SET.**
> *(`Bharati_TBD.md` was renamed `Shirayuki.md` 2026-09-04, closing that one.)*
>
> ### ⚠ AND IT CLOSES ONE COLUMN OF SIX, NOT THE TABLE — checked, 2026-09-03
> ***An earlier statement in this session that READER "already holds the data" for six of the seven was too
> strong, and is corrected here.*** **All 37 files were checked: `0` contain precipitation or daylight.**
>
> | Template column | Source |
> |---|---|
> | **Avg Temp (°C)** | ✅ **READER** — authoritative, cited |
> | **Avg Daylight (hrs)** | ⭐ **DERIVABLE — astronomy, not measurement.** Computable from latitude, which the specs already carry in `**Based on:**` |
> | Temp Range · Avg Precip · Precip Probability · Notes | ❌ **still requires research** |
>
> **⛔ DENISON HAS NO READER FILE, and no real-world climate source anywhere in the repo.** ***It is the only
> one of the seven that is unsourced*** — and it is simultaneously the sole city missing **founding
> population**, a Tier 1 spine generator. **Denison is the corpus's weakest-covered city on two axes at once.**

**MISSING (7):** Denison, Juan Carlos, Port Lockroy, Scott, Shirayuki, Zhongshan, Zukelli

# 5. ✅ RESOLVED — AIR ACCESS STATED FOR ALL 37 *(was 6 unstated)*

> ### ✅ CLOSED 2026-09-03. **`Airports.md` now reconciles: 11 hosts + 3 served-not-host + 23 no-access = 37.**
> **Verified mechanically — every city in exactly one list, no overlaps, no strays.** **The `"…and others"`
> catch-all is gone; the six previously-unstated cities are named.** **Three pieces of canon were established
> in the process** *(Mawson subnet zero-airport · Palmer City's two-era air-disconnection · Signy reachable by
> neither road nor air)*, **and a `Served, Not Host` category was created for Juan Carlos, Sejong and
> {{Abowasa}}.**
>
> ⭐ **Finding recorded there:** ***the file had contradicted itself three times, and the third contradiction
> was created BY the fix for the second*** — a correction note reading *"Juan Carlos is deliberately NOT
> listed here"* stopped being true the moment a table existed to list it in. **The cause each time was a
> PROSE CARVE-OUT for a case with no row.** **A count table that reconciles to 37 now makes the file audit
> itself.**

---

## *(historical — the state that prompted the fix)*

**The network itself is COMPLETE and reconciles 1:1 with the developer's map images — ten markers, ten rows.**
**13 of 37 cities have air access.** ***The gap is not missing airports; it is missing STATEMENTS.***

**`Airports.md`'s "Everything Else Is Highway-Only" paragraph enumerates ~18 cities by name and then says
"and others."** **These six fall into "and others" and carry no explicit statement either way:**

**UNSTATED (6):** Abowasa · Cape Adare · Denison · Esperanza · Port Lockroy · Signy

**`04` Gate C: *"Name the paths, or the negative result does not count."*** **Fix: replace the catch-all with
the six named, each carrying `no host airport` or `no host airport; served via <X>`.**

## ✅ CONFIRMED 2026-09-03 — **the Mawson subnet has NO airports. Developer-confirmed.**

**Mawson subnet — Dome Fuji · Mawson · Sayowa — is the ONLY subnet with zero air access.** *(Halley has two:
Troll, Belgrano. Palmer three. Mirny two. Janbogo one. Byrd one.)* ***This is deliberate and characterizing,
not a gap.***

> ### ⭐ TWO CONSEQUENCES, flagged for whoever runs these passes — NOT derived here
> **Recorded as pointers because this is a canon audit, not a pass.** *(`05` §6.1 — conclusions are read last
> and read as a check.)*
>
> 1. **The whole subnet is road-dependent, and its road gateway is a SPUR city.** **Sayowa holds the
>    three-way Sayowa Junction — Hwy 4 · Hwy 7-ext · Hwy 37 — and does not sit on it**, reaching it by the
>    dedicated Sayowa Spur. **Its own §15 carries fabrication and *trucking & dispatch*.** ***An entire subnet
>    whose only gateway is a city that owns a junction it stands beside.***
> 2. ⚠ **Dome Fuji is a PILGRIMAGE site.** `Official_Population_Census.md`: its population is *"Tepenia's most
>    devout adherents of 'Ice Cold Buddhism' (placeholder name), drawn to Dome Fuji from across the continent
>    as a pilgrimage/gathering site."* ***With no air access anywhere in the subnet, every pilgrim arriving
>    from across the continent makes that journey overland*** — up Hwy 37 across the plateau, or in via the
>    Sayowa Junction. **A pilgrimage that is necessarily long, overland and seasonal is a different
>    institution from one that is not.** **⛔ Do not resolve this here — it is Phase 5/Phase 6 material for
>    Dome Fuji's own pass, and the placeholder faith name is unratified.**

## ✅ ALL THREE MAP-CHECKABLE QUESTIONS ANSWERED — 2026-09-03, developer

| # | Question | Answer |
|--:|---|---|
| **1** | No marker at the six unstated cities? | ✅ **Confirmed by the file's own 1:1 reconciliation** — ten markers, ten rows, against both map images. **No further marker exists.** All 23 no-access cities are now named |
| **2** | Abowasa — served via Troll? | ✅ ***"Air access via either Troll or Belgrano. The earlier point-of-contact is Troll."*** **Now a `Served, Not Host` row.** ⚠ **The city's name remains provisional** |
| **3** | Palmer City — `SEA-LINK` and no airport? | ✅ **Confirmed, with a two-era reason that is new canon** — early **incapacity** *("didn't have the materials and infrastructure")*, later **deliberate policy** *("kept 'air-disconnected'… to make it harder for anyone from Upper Earth with ill intentions to sneak in")*. **Necessity Before Meaning, occurring in canon** |

> ### ⚠ THIS BLOCK WAS STALE FOR PART OF THE SESSION — logged, not quietly fixed
> **It read "STILL OPEN — three map-checkable questions" after all three had been answered.**
> ***That is the fourth stale self-report found in this audit***, alongside the census's Denison note, `§D`'s
> *"all verified to exist,"* and `Airports.md`'s *"Juan Carlos is deliberately NOT listed here."*
> **Gate 0 fails in both directions, and "still open" is the direction nobody checks** — an over-claim of
> completion gets caught; **an under-claim just quietly wastes the next session's time.**

# 6. ✅ RESOLVED — NAMED IN `Highways.md` *(was 3 of 37; **never a gap**)*

**Closed 2026-09-03 on developer confirmation, verbatim:** ***"Some cities that do NOT have highway access
are: Signy, Juan Carlos, Sejong. The rest of them either are directly on / next to, or have some sort of
connecting road that links to, a highway."***

**Three-way agreement: the developer, the three specs, and this audit all name the same three cities.**
***`Highways.md`'s silence about them is CORRECT*** — they are not on the network. **The positive statement
required by Gate C already existed; it lives in each city's own spec, not in the network file.** *(My presence
test looked in the wrong file — a scoping error in the instrument, not a gap in the corpus.)*

> ### ⭐ WHAT CAME OUT OF CLOSING IT — a new closed-set field on all 37 specs
> **The A/B/C distinction the developer drew is a real `G5` generator and existed only as prose.**
> ***A regex classifier misread it twice*** — flagging **Concordia** *(a genuine tri-junction)* and
> **Denison** *(on Hwy 183)* as spurs, both times by matching a DIFFERENT city's connecting road named in the
> same sentence. **If a regex cannot read it, neither can a pass.**
>
> **`**Access type:**` was therefore added to all 37 specs and to `_TEMPLATE.md`, carrying one token:**
>
> | Token | n | |
> |---|--:|---|
> | **`ON`** | 24 | on a mainline, incl. junctions and termini |
> | **`SPUR`** | 9 | connecting road, ramp, or off-road spur |
> | **`SEA-LINK`** | 1 | **Palmer City** — boat crossing from a highway ramp |
> | **`NONE`** | 3 | Juan Carlos · Sejong · Signy |
>
> **Why it matters beyond tidiness:** **`02` G5's distinctive yield is ASYMMETRY.** ***An `ON` city has
> traffic passing through it; a `SPUR` city is a terminus where every arrival is deliberate.*** **Opposite
> relational conditions — and until now unreadable.**

> ### ✅ THE REGISTRY-PATH DEFECT FROM THIS SECTION IS NOW FIXED — 2026-09-03
> **`00_RUNBOOK.md` §C registered this file at `…/Cities/Locations/Infrastructure/Highways.md`, a path that
> does not exist** *(`Infrastructure/` is a **sibling** of `Cities/`)*. ***Corrected in §C on developer
> authorization; the row now carries the correction note and the `Access type:` pointer.*** **Verified: the
> corrected path resolves, and no stale reference remains outside the files documenting the defect.**

# 7. FOUNDING POPULATION — **1 of 37** ⭐ **highest TIER on this list**

**`T1-G4` — a SPINE generator.** The `**Founding population:**` field is unfilled. **`02` G4: *the absences
are the yield — what the founding generation did not bring is very often a permanent hole.*** **`05` §2.2
requires three independent Tier 1 generators or the capability profile cannot be built.**

> ***Ranked 8th by count and 1st by tier.*** **This is the clearest instance of the blind spot flagged at the
> head of this file: one city, one field — and without it that city is a generator short of a spine.**

**MISSING (1):** Denison

# 8. DoI HALF B ROW — **1 of 37**

**`T1-G3`, the strongest `G3` supply in the project.** **Absent from the 37-city run in
`16_Per_City_Three_Tier_Run.md`.** *(Consistent with item 12 — the same city is paused.)*

**MISSING (1):** Abowasa

---

# ❌ REMOVED FROM THE LIST — **not input requirements. Do not re-add them.**

**Three fields were removed on 2026-09-03 after being ranked #4, #5 and #6 by raw count.** ***Two were
developer scoping decisions; the third was MY MEASUREMENT ERROR.*** **Record the reasoning in all three cases,
because a future session reading the audit top-down will otherwise re-derive them as gaps.**

## ❌ NOTABLE FIGURES *(was #6, 11 of 37)* — **CIRCULAR BY CONSTRUCTION**

**Developer's ruling, and it is a methodology finding rather than a scope cut:**

> ***"In order for there to be 'notable figures', we need a solid understanding of a particular given city's
> either history or fundamental nature, and we can't figure out a place's history without understanding its
> nature, and 'understanding its nature' is the whole and entire point of the ULM. Therefore, having 'notable
> figures' as a requirement will just produce an infinite loop of failure."***

**The ULM already carries this hazard and never generalized it.** **`05` §2.4, hazard 3 on particulars:**
*"Circularity. If the character's backstory was itself written from this location's culture pass, feeding it
back is self-confirmation."*

> ### The generalization, which is the actual finding
> **Hazard 3 is written as an EDGE CASE — "if the backstory happened to come from the pass."** ***For a city
> with no independently-authored figures, it is not an edge case. It is the only available path*** — the sole
> way to obtain one is to write it from the pass's own reading of the city, which makes hazard 3 fire
> **automatically, every time.** **That is `05` §6.1's defining failure: *planting your own seed and then
> finding it*, and the result is "perfectly coherent and contains no information."**

**Two further rules already point the same way:** **`05` §3 RESERVES proper names of people to the developer**,
and **Phase 10 §C keeps people as role-archetypes with no invented proper names.** ***A notable figure is
Phase 10 OUTPUT, not Tier 3 input.***

> ### ⚠ What survives, and it is narrow
> **`T3-01` remains valid as OPPORTUNISTIC testimony where a character was authored INDEPENDENTLY** — a
> companion or historical figure written by someone who was not thinking about this city *(`05`'s non-circular
> case; the same Mode A/Mode B split the district folder found in the counterculture-seed technique)*.
> **Where such a figure exists, interrogate it: *what must be true of this place for them to have become who
> they are?*** ***Where one does not exist, do not manufacture one to fill the field.***

## ❌ CONCEPT ART *(was #4, 33 of 37)* — **Tier 3 optional; moved to the production pipeline**

**`05` §2.4 is explicit that no Tier 3 particular is required.** **Nothing blocks without it.**

**Three reasons it does not belong in a worldbuilding-input backlog:**

1. **Its claimed value is EXTERNALITY** — `05`: *"it constrains, which is the point."* ***But commissioned or
   generated art reflects the brief it was given.*** **It hands the designer their own defaults back in a
   nicer format**, which is precisely the drift `01` §5.3a warns about. **A photograph of the real station IS
   external — and that channel already exists via `G7` and `Reference/Real-World/`.**
2. **`G2` supplies the same constraint far more rigorously** — real terrain, real climate, real wind speeds,
   none of which negotiate. **`02` rates `G2`'s externality "highest" on the whole stack.**
3. ### ⭐ **Its input value exists ONLY if it precedes the pass.**
   ***Made afterward it is illustration — pleasant, and worth zero as a generator.*** **So "backfill 33
   folders" is not coherent as worldbuilding work: art is either made before those passes or it is not an
   input at all.**

**Status: real ART-DIRECTION work for a CRPG, on a different pipeline and a different schedule.** **The 33
empty `.gitkeep` folders are scaffolding for unscheduled work, NOT 33 items of debt.**
*(Have: Sanay · Dome Fuji · Palmer City · Rothera — 5 images each.)*

## ❌ NATIONAL MEDICAL / CARE ENTRY *(was #4, "22 of 37")* — ⛔ **THE METRIC WAS MEASURING NOTHING**

> ### ⚠ This is a self-correction, not a scoping decision. The number was wrong, not merely unimportant.

**`National_Medical_and_Care_Institutes.md` is NOT a per-city roster.** **It is canon establishing exactly
THREE national institutes** — **Esperanza** *(settled medicine; flagship Pediatrics)*, **Belgrano**, and
**Sinheung** *(Cybernetics and Robotic Care)* — declared canon by developer ruling 2026-09-01.

**The file's own reasoning makes the other 34 absences CORRECT BY DESIGN:**

> *"Care delivery cannot be centralized… **Every city staffs its own clinicians, always.**"* — **training is
> centralized precisely BECAUSE delivery cannot be.** *"Every medic, nurse, field responder and robot-care
> technician in the Federation was made in Tepenia — and, in practice, made at one of these three institutes."*

**So the true figure is `3 of 37 host an institute`, and `34 correctly do not`.** ***My test counted whether a
city's name appeared ANYWHERE in the prose of a document about three institutes*** — which caught incidental
mentions like *"nobody treats a Vostok patient from Concordia"* and *"Davis can be supplemented by fishing
fleets."* **Twelve of the fifteen "present" cities were false positives.**

> ### ⛔ THIS IS THE THIRD INSTRUMENT DEFECT OF THE SAME FAMILY IN ONE AUDIT
> **Free-text mention mistaken for structured membership.** **The other two:** the **Census II** test *(four
> cities scored present because they appear in footnotes saying they are absent)* and the original
> **concept-art** test *(matched filenames, not directories)*.
>
> ***All three produced a confident number that no reader could have distinguished from a real one.*** **The
> lesson is `04` Part IV's, arriving a third time: *a mechanical scan is worthless until you have proved it
> could have found a hit* — and for a MEMBERSHIP question, the proof is that the test anchors to the
> structure that expresses membership (a table row, a heading, a folder), never to the name appearing.**

**⏸️ One genuine open item survives inside that file and is NOT a per-city input gap:**
**§"FOR FUTURE REVIEW — where the satellite campuses actually go."** *(A canon question, tracked there.)*

---

# ⏸️ BLOCKED — real gaps, but not open work

| Field | City | Blocked on |
|---|---|---|
| **Robot culture file** `T2-5` | **Abowasa** | **its founding-nation fix**, paused per standing project practice — the same pause that excludes it from the symbol assignments |

---

# ⛔ STRUCTURAL — **NOT to-do items. Do not "fix" these.**

**Every one is correct by design and was verified rather than assumed.**

| Field | City | Why it is correct |
|---|---|---|
| Symbol pair | **Concordia** | the capital uses the **zodiac district substrate**, not the Planet+Element city system |
| Local culture · Megasheet · Enneagram · Robot culture | **Concordia** | **301 district files** under `Concordia-City/Districts/` — the district methodology owns it |
| Symbol pair | **Abowasa** | **deliberately paused** pending its founding-nation fix; stated in the file itself |
| Symbol pair · Inspiration picks | **Amundsen Station** | **a research and relay outpost, not a residential city** — the census says so explicitly |

---

# ✅ COMPLETE — 37 of 37, nothing to do

**Census I figures · National origin composition (`G8`) · Geographic basis · Settled date · Significance ·
Economy & Industry section · Highway-access field · Based-on designation · Inspiration picks *(bar Amundsen)* ·
Notable locations · Open questions · Relationship files · Master reference entry · City vision notes.**

> ### ⚠ THE PATTERN WORTH READING OFF THIS LIST
> **Every COMPLETE field has a single aggregate owner** — one file with a row per city. **Every field at or
> near ZERO needs a PER-CITY artifact** — a research log, an art folder, a table column, an extent figure.
>
> ***That is not thirty-seven separate oversights. It is one structural fact: a missing ROW in a shared table
> is visible, and a FILE that was never created is not.*** **`05` §7's pre-flight is run BY a pass ABOUT the
> single city it is writing, so nothing in the methodology has ever asked this question across the corpus.**
