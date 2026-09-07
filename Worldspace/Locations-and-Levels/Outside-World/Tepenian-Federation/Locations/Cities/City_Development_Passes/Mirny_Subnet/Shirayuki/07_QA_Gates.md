# Shirayuki — ULM **Step 7 · QA — ALL GATES**

**Run 2026-09-06.** **Piece 17.**

> ⭐ **THIS FILE IS THE OFFICIAL, CURRENT DATA.**

> ## ⛔⛔ **RAW SCAN OUTPUT IS PASTED, NEVER SUMMARIZED.**
> **`CLAUDE.md` non-negotiable:** *"Self-audit error in this project has run in **one direction — toward
> flattering the pass — on every occasion it has been measured** (four instances across two districts, after
> the rule against it was already written)."*

---

# ⭐⭐⭐ RESULT UP FRONT: **ONE GATE FIRED, AND IT CAUGHT REAL DEFECTS**

| | |
|---|---|
| ⛔ **FIRED** | **The American-English scan — FIVE hits, all introduced during the re-run prose** |
| ✅ **Passed** | **the other fifteen** |
| ⏸️ **Terminal / not run** | **Gate 5's sibling half · Gate 6's against-siblings half · Gate 10 (= Step 8)** |
| ⚠ **Limitation found in a gate itself** | ⭐ **Gate 11 is partly TAUTOLOGICAL here — see `G11`** |

---

# LETTERED GATES — *run on the frame and the inputs*

## Gate C — CANON CHECK, FEDERATED ✅ **PASS, with a docket**

**Run in full at `05_Reconciliation.md`.** *The read-last Cultural Spec Sheet opened; 12 confirmations, 6
conflicts, all stated with reconciliations.* ⭐ **Output: a nine-row PROPOSED-CORRECTION DOCKET.**
⚠ **Two canon-internal discrepancies logged and NOT adjudicated:** *precipitation `148.9` vs `~159 mm`* ·
*`Local_Cultures` §3 vs `Specs/` on the wind.* ⏸️ **`DRQ-10`–`DRQ-14` open.**

## Gate F — FRAME INTEGRITY ✅ **PASS**

**Declared: type · state · era · parent · population band · extent band · subject continuity · run mode ·
configuration · what the frame cannot prove.** ⭐ **The band crossing and the `~2780s` merger are both declared
rather than hedged.** ⚠ *`DRQ-10` open on the band; it is flagged, not silently resolved.*

## Gate I — INHERITANCE CLASSIFICATION ✅ **PASS**

**All four classes assigned at `01` §5** — ⭐ **and Act-stamped**, *per the finding that the class boundary
moves across the Act transition* **(`M-157`)**. ✅ **`Aggregated` recorded as an honest `n/a`.**

## Gate P — PARENT RECONCILIATION ✅ **PASS**

**Three parents declared and distinguished** *(network · political · de facto)*, ⭐ **plus a fourth arriving at
the merger.** ✅ **Nothing `Determined` is used to characterize the city** — *the peer-free form is stated at
`00_Frame.md` §3.*

## Gate G — GENERATOR HONESTY ✅ **PASS**

```
$ grep -nE "\b(STANDING COST|GRUDGING TOLERANCE|capability profile)\b" <17 pass files> | grep -v '`'
02_Spine.md:103:| **STANDING COST** | ⚠⚠ **THIN.** *A claim settled by treaty does not need renewing…
02_Spine.md:104:| **GRUDGING TOLERANCE** | ⭐ **Asking why you are here.** *Nobody forbids the question…
02_Spine.md:119:| **GRUDGING TOLERANCE** | ⭐ **Leaving by road.** *Not forbidden — but from a terminus…
02_Spine.md:134:| **STANDING COST** | ⚠⚠ **THIN.** ***A protected plurality costs nothing to maintain…
02_Spine.md:148:> # ⛔⛔ THE STRUCTURAL RESULT: **STANDING COST IS PHYSICAL, WITH ONE NAMED EXCEPTION.**
03_Research.md:445:> **The rule:** *run it after the capability profile is complete.*…
04_Phase_02_Composition_and_Arrival.md:337:GRUDGING TOLERANCE quadrant, and Phase 2 is not that quadrant.**
```

⭐ **VERDICT: all seven hits are legitimate.** *Six are row labels inside `02_Spine.md`'s own quadrant tables —
**the generator's output, correctly labeled as such** — and one is a methodology citation in `03`, one a
cross-reference in Phase 2.* ⛔ **Zero occurrences inside a claim about the city.**

---

# NUMBERED GATES

## Gate 0 — COMPLETION CLAIM ✅ **PASS**

**Claimed complete: Steps 0–6, Phases 0–10.** ✅ **Verified by file listing, not asserted:**

```
$ ls -1 04_Phase_*.md
04_Phase_02_Composition_and_Arrival.md   04_Phase_07_Order.md
04_Phase_03_Surface_and_Texture.md       04_Phase_08_Making.md
04_Phase_04_Ordinary_Life.md             04_Phase_09_Populations.md
04_Phase_05_Relation_and_Geometry.md     04_Phase_10_Catalog.md
04_Phase_06_Meaning.md
```

⭐ **Phases 0 and 1 live in `00_Frame.md` and `02_Spine.md` by design, and both files say so.**
⛔ **NOT claimed complete: Steps 8, 9, 10 · CST · RWBEM.**

## Gate 1 — COVERAGE ✅ **PASS**

**Nine phase files + two carried phases = eleven.** ⭐ **Every phase ANSWERED, not merely present** — *each
carries an axis, a nulls section, and a "what this cannot prove."*

## Gate 2 — GENERAL POPULATION ✅ **PASS**

⭐ **`00b` applied at every phase, and it fired usefully twice:**
- **`04_Phase_07` §7a — the arithmetic test.** *`25% × 801,070 = ~200,270 people`.* ⛔ **"Two hundred thousand
  people is not artists"** → ***the sector was WIDENED, not shrunk.***
- **`04_Phase_02` §C and `04_Phase_08` throughout** — *general answer written FIRST; the signature instance
  scoped inside it and `[SET-B]`-tagged.*

## Gate 3 — INTERNAL CONTRADICTION ✅ **PASS** *(and it caught one during the re-run)*

⭐ **Read Ordinary Life against Phases 1–10.** ✅ **No live contradiction.**
⚠ **One was found and fixed mid-pass, and is recorded rather than hidden:** *`04_Phase_04` §4's "most days are
moderate and unremarkable" contradicted Phase 3's corrected wind seasonality.* ✅ **Resolved to the DIAL.**
⚠ **A second, in `04z` §10, was found at RE-RUN 13:** *the file asserted five eliminations that its own
appended audit had struck one section later.* ✅ **Resolved.**

## Gate 4 — SWAP TEST ⭐ **RUN IN ITS CONSTITUTIVE FORM**

> ⛔ **The literal form — *"would this survive being moved to another location?"* — is a comparison instrument
> and is TERMINAL** *(`M-156`)*. ⭐ **The peer-free form asks what a finding REQUIRES.**

| Finding | Requires |
|---|---|
| **"Nothing here is old; things are only well-kept"** | ✅ **five facts of this site** *(`04_Phase_06` §A.1)* |
| **The window; three workloads, one intersection** | ✅ **this latitude's light and this site's katabatic seasonality** |
| **Keptness matters more than kind** | ✅ **a grading system living in a vocabulary, not an institution** |
| **The pipeline delivers people to the worse ground** | ✅ **finite inherited rock + a nationally-drawing intake institution** |
| ⛔ **"Egalitarian, skewed toward robots"** | ⛔ **NOTHING LOCAL — the national baseline.** ✅ **Labeled as inherited context, never as a finding** |

## Gate 5 — CROSS-LOCATION CONSISTENCY ⏸️ **SPLIT**

✅ **The peer-free half RAN:** *this pass's relation material is internally consistent and consistent with
`Ports.md`, `Airports.md`, `Highways.md` and `City_Relationship_Database.md`.* ⭐ **One canon defect found and
queued — `DRQ-14`.**
⏸️ **The sibling half is TERMINAL** *(it requires siblings' completed material)*. ⛔ **Not run.**

## Gate 6 — DUPLICATE INSTITUTIONS ⏸️ **SPLIT**

✅ **WITHIN-LOCATION half RAN.** *Does the pass name two institutions that are the same institution twice?*
⛔ **No.** *The university, the drainage run, the materials yard, the known lee and the haul road are
distinct objects.*
⏸️ **The AGAINST-SIBLINGS half is TERMINAL** *(`M-156`)*. ⛔ **Not run, and not deferred to Step 7 either.**

## Gate 7 — RESEARCH ACCOUNTING ✅ **PASS**

**Six sessions in `Research_Logs/Shirayuki_Research_Log.md`, with verbatim search strings.**
**20 searches: 15 productive · 1 dead end *(recorded with the point at which it died — the query, not the
sources)* · 1 blocked-then-rescinded · 1 partial · 2 near-duplicates.** ⭐ **Every pick recorded as used or
rejected, and unrun alternatives logged.**

## Gate 8 — STANDOUT RECORDED ✅ **PASS**

> # **THE STRONGEST THING THIS PASS PRODUCED:**
> ## ***"Nothing here is old. Things are only well-kept."***
> **A city with no reachable antiquity — physically, foundationally, ethnically, and even in the one era that
> is its own — finds its standard of worth in the only temporal register available to it.**
> ⭐⭐ **And it turned out to be what canon's own `Ashiato` scene is named after.**

## Gate 9 — ASYMMETRY ✅ **PASS**

**Run as an instrument at `01` §4 on seven inherited findings — four fired, three did not, and the
non-firings are recorded with reasons.** ⭐ **Every threshold finding in the pass states which way it runs:**
*the Jeju-do gate · the departure gate *(direction corrected)* · the admission gate · the keptness axis · the
berthing queue.*

## Gate 10 — THE REVIEW PANEL ⏸️ **= STEP 8. Not run here.**

## Gate 11 — ⭐⭐ PLAUSIBILITY. **Population ÷ extent. One division, no interpretation.**

```
$ python3 <gate 11>
  Larsemann ice-free rock                  40.0 km2   (shared, 3 cities)
  Shirayuki share  0.334                 13.4 km2
  Census I   1,060,482          on rock:       79,377 /km2
  Census II    655,492          on rock:       49,064 /km2
  @ 10,000/km2  required footprint   106.0 km2  ->  rock  12.6%   ICE  87.4%
  @  7,000/km2  required footprint   151.5 km2  ->  rock   8.8%   ICE  91.2%

  hand-check one row against the source:
    518,822 + 541,660 = 1,060,482   spec says 1,060,482   OK
    302,512 + 352,980 = 655,492     spec says   655,492   OK
    1,060,482 - 655,492 = 404,990   departures   OK
```

✅ **CLEARS.** *Extent is not area-constrained — the coastline ruling and the standing "ice is buildable"
ruling both apply.* ⭐ **The division's real product is `87–91% ON ICE`.**

> ## ⚠⚠ AND A LIMITATION IN THE GATE ITSELF, FOUND BY RUNNING IT
> **`79,377 /km²` for Shirayuki on its rock share is *numerically identical* to `79,360 /km²` for the whole
> cluster on the whole oasis** *(within rounding)*. ⛔ **That is not a corroboration. It is a TAUTOLOGY.**
> ***The apportionment is population-share, so per-city density is forced to equal cluster density by
> construction, and the division cannot falsify anything about the share.***
> ⭐ **What IS non-tautological, and what the gate genuinely tests here:** **the CLUSTER figure** *(`3.17M` on
> `40 km²`)* **and the ICE RATIO** *(`87–91%`)* — **neither of which depends on the apportionment.**
> ⚠ **`DRQ-11` is the real question, and Gate 11 cannot substitute for it.** ⭐ **Recorded because Gate 11 is
> the project's only falsifying gate, and knowing where it is blind matters.**

---

# ADDITIONAL STANDING SCANS

## ⛔ AMERICAN ENGLISH — **THE ONE GATE THAT FIRED**

```
$ grep -nEi "\b(neighbour|colour|behaviour|favour|honour|licence|defence|grey|labelled|modelling|
              travelling|storey|mould|practise|analogue|centre|metre|catalogue|whilst|amongst|
              learnt|towards|programme|kilometre)[a-z]*\b" <17 pass files>
04_Phase_04_Ordinary_Life.md:116:...and the act at its centre is one canon calls tenderness.
03_Research.md:400:> BREAK from the paternal workshop — learning amongst other artisans,"...
04_Phase_03_Surface_and_Texture.md:254:...the phase's centre of gravity...
04_Phase_03_Surface_and_Texture.md:364:...a labelled inference that winter might be calm...
04_Phase_08_Making.md:109:> ***And to practise unheard, you go into the wind.***
04_Phase_07_Order.md:174:..."prevented the worst excesses of opportunistic behaviour."...
```

⛔ **SIX HITS ACROSS FIVE FILES.** ⚠ ***All were introduced during the re-run and consolidation prose —
after a full-corpus sweep had already been run and verified clean earlier the same session.***
⭐ **This is exactly the failure the standing rule predicts:** *"the failure is **drift, not ignorance**…
British forms creep in specifically during **long analytical prose**, and each instance reads as normal in
context."*
⚠ **Two of the six sit inside verbatim research quotations** — ✅ **corrected anyway; the rule is absolute and
names quotations explicitly.**

```
$ # after fix
(exit 1 — ZERO HITS)
```

## ✅ COMPARISON LANGUAGE — **THE LAW OF ONE LOCATION**

```
$ grep -nE "z = |z-score|corpus mean|26 of 37|worst in|best-grounded|alone in its oasis|
            only city with|nth of|2\.67 standard|than its neighbou?rs|unlike (Sinheung|Zhongshan|
            Davis|Sayowa)" <17 pass files>
04z_Post-Ruling_Enrichment_Review.md:270:| **`02` §G8's z-score rule** | ⛔ **No score of any kind in-run** |
```

✅ **ONE HIT, AND IT IS A MENTION, NOT A USE** — *naming the instrument that was ruled on.* ⛔ **Removing it
would make the record false.** ⭐ *Same mention/use distinction that kept three files out of the English sweep.*

## ✅ PLACEHOLDER FLAGGING

```
$ grep -nE "Reiko Tashiro|Momoka Ishihara|Bunger Hills City" <17 pass files>
04_Phase_02:240: discharge to `{{Bunger Hills City}}`.
01_Inherited.md:79: The 2026-09-05 ruling released −10% to `{{Bunger Hills City}}`,
05_Reconciliation.md:183: the −10% discharge to `{{Bunger Hills City}}` was proportional…
04_Phase_08:173: proprietor (`Momoka Ishihara` — ⛔ PLACEHOLDER, re-flagged)
00_Frame.md:319: 2. Notable figures — `Ambassador Reiko Tashiro` and `Momoka Ishihara` are PLACEHOLDERS
00_Frame.md:321: 3. `{{Bunger Hills City}}` — placeholder name; braces stay until ruled
04_Phase_10:18: `Momoka Ishihara` · `Ambassador Reiko Tashiro` | PLACEHOLDERS. Re-flagged
04_Phase_10:226: `Ambassador Reiko Tashiro` | PLACEHOLDER. Not finalized. Re-flagged on this reuse
04_Phase_10:227: `Momoka Ishihara` | PLACEHOLDER. `[SET-B · M-143]`
```

✅ **PASS.** *Braces preserved on `{{Bunger Hills City}}` at every occurrence; both person placeholders flagged
at every substantive reuse, per the standing rule.*

## ✅ NO INVENTED PERSON NAMES *(Phase 10's binding rule)*

```
$ grep -nE "^\| *\*\*[A-Z][a-z]+ [A-Z][a-z]+\*\*" 04_Phase_10_Catalog.md
(exit 1 — zero hits)
```
✅ **PASS.** *All `C.3` entries are role-archetypes. The only person names in the file are the two flagged
placeholders and one canon character, all in `§31`.*

---

# WHAT STEP 7 CANNOT PROVE

- ⛔ **Gate 5's and Gate 6's sibling halves did not run.** *Terminal.*
- ⛔ **Gate 11 is partly tautological here** *(above)* — **it cannot test the apportionment.**
- ⛔ **Gate 3 read a complete file, but the pass's own `[DERIVED]` claims are not testable by scan** —
  *they are testable only by canon or by a ruling.*
- ⚠ **The `7d` counterculture canon check remains BLOCKED** *(the owning file is withheld wholesale)*.
- ⚠ **Gate C's docket is PROPOSED, not applied.**

---

📎 **Next: `Step 8 — The Review Panel`** *(= Gate 10)*. **Six dispositions:** `accepted · noted · rejected ·
refereed · unmet · declined`. ⭐ **And the `unmet` test in its peer-free form:** *"would satisfying this
objection replace something SPECIFIC TO THIS PLACE with something that could be true anywhere?"*
📎 `09.5_Log.md` · `05_Reconciliation.md` · `Research_Logs/Shirayuki_Research_Log.md`
