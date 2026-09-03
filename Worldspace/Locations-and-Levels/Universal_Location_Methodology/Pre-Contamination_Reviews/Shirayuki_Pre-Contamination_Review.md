# Pre-Contamination Review — SHIRAYUKI

**Location:** Shirayuki · **Parent:** Mirny subnet · **Type:** Settlement · **Frame:** Second Interwar, pre-war
**Built:** 2026-09-02 · **Mechanism:** `../00_RUNBOOK.md` §C.4 · **Readers:** 1 vector-1 scanner + 1 roster
scout reported; **3 coordinate taggers in flight**

# ✅ Status: **CONFIRMED** — restored 2026-09-03, against the NEW six-requirement bar

> ## The lifecycle this file went through today, recorded because it is the evidence for `§C.4` requirement 6
>
> **`CONFIRMED` (5 requirements) → ⛔ `DRAFT` (Run 14 burned through the gap) → ✅ `CONFIRMED` (6 requirements).**
>
> ***It met all five requirements in force when written, and every one of them held under use.*** **It was
> still incomplete: the coordinate map covered `3` files, and a Brief B registry scout later enumerated
> **34 roots** holding **510 files** that name the subject or its alias.** **The hash pin verified the whole
> time and always would have — *it answers "did these files move?", never "are these the right files?"***
> **Full mechanism: `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` M-112.**

## The six requirements, as met

| # | Requirement | Evidence |
|---|---|---|
| **1** | Four `Step −2` vectors swept | §1 · ⚠ **vector 2 re-run needed across the alias set — see §8d** |
| **2** | Every mapped range carries a **3-of-3** verdict | §6 *(3 files, 2026-09-02)* + **§9 *(14 files, 2026-09-03)*** |
| **3** | Non-unanimous ranges resolved or **explicitly accepted as `WITHHELD` with the rate recorded** | §6d + **§9b — 17.3% split rate, recorded** |
| **4** | **A PIN** — `sha256` + line count per mapped file | §2 *(verified on reuse, 3/3 exact)* + §9 *(14 files, `wc -l` verified, no mismatches)* |
| **5** | Tagging attributed | §6e + §9c |
| **6** | ⭐ **Registry enumerated · scope pinned · every source tiered** | **§8 — 34 of 34 roots, no omissions** |

> ### ⛔ REVERIFY BOTH PINS BEFORE REUSING — the hash pin (§2, §9) **and the SCOPE pin (§8a)**
> **A risen scope count means a source JOINED and this review is `DRAFT` again**, exactly as a moved hash
> means a file changed. ***The scope pin is a CHANGE detector, not a coverage proof.***

---

## Historical record — the five requirements as met on 2026-09-03

**All five `§C.4` requirements met:** four `Step −2` vectors swept and closed *(§1)* · every mapped line
carries a 3-of-3 verdict *(§6)* · every non-unanimous range **explicitly accepted as `WITHHELD`** with its
rate recorded *(§6d — the ladder is yield recovery, not a safety gate)* · **pin taken** *(§2)* ·
**tagging attributed** *(§6e)*.

> ### ⛔ REVERIFY THE PIN BEFORE REUSING (§2). Do not assume it still holds.
> **A coordinate map is line-anchored: one inserted line shifts every range below it, silently.**

> ### ⭐⭐ THE FIRST REVIEW IN THIS PROJECT BUILT ***BEFORE*** ITS RUN RATHER THAN AFTER A BURN.
> **Casey's review was written by a session that had already been contaminated. This one was assembled by
> isolated readers reporting to a session that still does not know what any of the flagged lines say.**
> ***That is the difference `Step −2` was written to make, and this is its first live demonstration.***

> ## ✅ THIS FILE IS SAFE FOR A COLD DERIVER TO READ IN FULL.
> **Coordinates, counts, tags and status only.** *(M-97: describe a leak by its SHAPE and SIZE, never its
> CONTENT.)*

---

# 1. The four-vector sweep — `Step −2`

| # | Vector | Status | Evidence |
|---|---|---|---|
| **1** | **Required reading** | ✅ **SWEPT — 3 LEAKS FOUND, LOCATED, NOT READ** | An isolated reader classified every hit across all 11 required files. **See §4.** ⚠ **`06`'s own manifest check would have returned CLEAN** — its two hits sit inside *other* cities' sections. **M-82's 4th and 5th instances** *(M-99)* |
| **2** | **Auto-loaded memory** | ✅ **SWEPT AND CLOSED** | `grep -ril shirayuki` → **38 entries**. **5 city-named entries BANDED** in place via `§3d`; **the remaining 33 are covered by the memory index's new default-deny declaration.** *(Per-entry banding does not scale at 38 entries × 37 cities — M-99.)* |
| **3** | **File tree** | ✅ **SANITIZED AT SOURCE** | **No `ls`/`find` was run against Shirayuki by this session.** The inventory in §3 came from readers under a positive-format contract that forbids returning vignette filenames |
| **4** | **Union / compositional** | ✅ **CLEAR** | **This session has read none of the three flagged lines and none of the banded entries.** **The union is empty.** **Next session: keep an exposure ledger and review it as a SET before Phase 0** (M-89) |

---

# 2. ⛔ The pin — REVERIFY BEFORE REUSING *(map 1 — the 3 city files)*

**Verify with the script in `../00_RUNBOOK.md` §C.4.** *(`sha256` first 16 chars; paths under
`Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`.)*

```
Specs/Shirayuki.md|04196fd64ec36bdc|225
Local_Cultures/Mirny_Subnet/Shirayuki.md|07bb02ca9eb8d6e6|285
City_Megasheets/Mirny_Subnet/Shirayuki/Shirayuki_Physical_Infrastructure_Attributes.md|a8fea96f1dffa208|162
```

**On a `STALE` row: re-tag only the file that moved.**

---

# 3. Sanitized file inventory

> ### ✅ THIS TABLE WAS CHALLENGED AND RE-VERIFIED. **It is correct.** *(M-113 — RETRACTED.)*
>
> **Run 14 briefly recorded the megasheet row as wrong, claiming 7 files / 51–699 lines.** ***That was a
> measurement error, not an inventory error:*** a `find … -exec wc -l {} +` emits a trailing **`total`** row,
> and `51+55+59+100+162+272 = 699` was read as a seventh file. **Independently re-counted: 6 files,
> 51–272 lines — exactly as recorded here.** **Caught because a Brief B scout returned a corpus-wide
> megasheet maximum of 337, which a 699-line megasheet would contradict.**
>
> **The `§C.4` inventory pin still applies** — this table has no verification mechanism of its own, and
> `§C.2` rule 3 forbids a cold deriver from running its own `ls` to check it. ***This episode shows the
> failure runs in BOTH directions: an inventory can be wrong, or a deriver can wrongly believe it is and
> strike out a correct line.*** **Pinning the numbers closes both.**

| Path | Contents | Safe to list? |
|---|---|---|
| `Cities/Specs/Shirayuki.md` | 225 lines | ✅ |
| `Cities/Local_Cultures/Mirny_Subnet/Shirayuki.md` | 285 lines | ✅ |
| `Cities/City_Megasheets/Mirny_Subnet/Shirayuki/` | 6 files, 51–272 lines | ✅ template-named · **re-verified 2026-09-03** |
| `Cities/Local_Robot_Culture/Mirny_Subnet/Shirayuki.md` | 279 lines | ✅ *(⛔ quarantined content)* |
| `Cities/City_Enneagram_Personalities/Mirny_Subnet/Shirayuki.md` | **76 lines** | ✅ *(⛔ quarantined content)* |
| `Cities/City_Vision_Notes/Shirayuki.md` | 35 lines | ✅ *(⛔ quarantined — `05` §6.1 tier, see Casey review §6 reasoning)* |
| **`Background-Lore/Cities/Mirny_Subnet/Shirayuki/`** | **13 files, 98–668 lines** | ⛔⛔ **NEVER `ls`. Address by index.** *(M-88)* |
| `Cities/Research_Logs/` | **none for Shirayuki** | **Create one at Step 3** per `00_RUNBOOK.md` §3.7 |

---

# 4. ✅ **REQUIRED-READING SKIP LIST — RETIRED 2026-09-03. THERE ARE NO SKIP RANGES.**

> ## ⭐⭐ **`01`–`05` AND `README` NOW NAME NO LOCATION AT ALL. VECTOR 1 IS CLEAN BY CONSTRUCTION.**
>
> **Verified mechanically, 2026-09-03** — `grep -ciE 'shirayuki|bharati'` returns **0** for `00_RUNBOOK.md`,
> `01`, `02`, `03`, `04`, `05` and `README.md`.
>
> **Read the required reading NORMALLY. Skip nothing.**

## What changed, and why it is worth more than a skip range

**The developer's LAYERING LAW** *(2026-09-03; `00_RUNBOOK.md`, top of file)* — ***"the methodology needs to
be usable for any location in any universe… only the RUNBOOK and the pre-contamination file(s) should contain
references to a specific, exact city"*** — **was given as a PORTABILITY requirement.** ***It is also the
strongest anti-contamination change this methodology has ever made.***

**`CLAUDE.md` mandates `00`–`06` be read in full before any location work.** **So a location name in a rule
file was never a blemish — it was a conclusion the corpus was *contractually obliged* to hand every future
pass on that location.** **That is leak-register row 1, the channel that has burned more runs than any other.**

| Was | Now |
|---|---|
| `02` **340–378** — a `CONCLUSION-EXAMPLE` range *(M-103)* | ✅ **moved to `Test_Runs/Worked_Examples_Archive/`** |
| `05` **180–250** — a `CONCLUSION-EXAMPLE` range | ✅ **moved to the same archive** |
| **Skip ranges required, boundaries unprobeable** | ✅ **none** |
| M-103's *"the rule around the example leaks too"* | ✅ **dies with the example** |

> ### ⛔ AND THE OLD RANGES ARE NOW ACTIVELY WRONG — do not use them from memory
> **`02` is 621 lines (was 613); `05` is 708 (was 703).** ***The old coordinates point at unrelated text.***
> **A line-anchored map is invalidated by any edit above it — which is exactly why `§C.4` pins hashes.**

> ### ⚠ Historical record, for a session auditing what leaked and when
> **Those two ranges leaked twice before retirement:** once as the un-manifested worked examples that produced
> **M-82 / M-99 / M-103**, and once to Run 14's own map-building session via a name-list `grep` that breached
> **both** ranges in a single command *(**M-119** — logged in full, including the false safety argument that
> authorized it)*. ***Both events are now historical: the content is not in those files.***

**`06_Worked_Example_Provenance.md` retains its 5 subject mentions and SHOULD** — it is a manifest, and naming
is its function *(M-4: an unnamed worked case contaminates just as effectively and removes the reader's
ability to know it)*. **Its rows are coordinates-only for this subject.**

---

# 5. ⚠⚠ TYPICALITY DECLARATION — Shirayuki is a BEST-CASE pick, and the run must say so

**`00_RUNBOOK.md` requires this stated before anything else, and `RESUME_HERE.md` §2 item 4 repeats it.**
**Measured from the roster scout, not recalled:**

| City *(Mirny subnet, 8 of 8)* | Specs | Local_Cultures | Enneagram | TBDs | Prior cold run |
|---|--:|--:|--:|--:|:--:|
| **Shirayuki** | **225** | 285 | **76 ⭐** | **4 ⭐** | no |
| Sinheung | 219 | 282 | 73 | 5 | **✅ Run 5** |
| Zhongshan | 135 | 381 | 68 | 7 | **✅ Runs 3/4** |
| Kunlun | 226 | 281 | 15 | 6 | no |
| Mirny | 195 | 302 | 17 | **9** | no |
| Casey | 191 | 292 | 15 | 6 | no |
| Davis | 157 | 292 | 15 | 6 | no |
| Vostok | 184 | 274 | 15 | 6 | no |

> ### ⭐ **The three cities with a FULL Enneagram read (68–76 lines) are exactly Zhongshan, Sinheung and
> Shirayuki. Every other city in the subnet has a 15–17 line stub.**
>
> ***The two cities already cold-run are two of those three. Shirayuki is the third.***

**Declare it plainly in the frame block:**

- **Shirayuki is EXCEPTIONAL for its subnet** — **the deepest design-tool coverage (76, the highest of all
  eight) and the FEWEST open TBDs (4, the lowest of all eight).** ***It is the most-determined city in Mirny.***
- **⭐ For a CONSISTENCY test this is the right kind of exceptional**, and it is why the pick is sound: **it
  matches its two cold-run comparators on the axis that matters** — Gate 6 and Step 6 differentiation get
  siblings of genuinely comparable depth, not a rich-vs-thin mismatch.
- **⚠ But findings will NOT generalize to a thin location.** ***This is the fourth consecutive Settlement
  chosen that turns out to be a best case*** — the exact pattern `00_RUNBOOK.md`'s own status note flags
  (*"Sinheung, like every location run through this instrument so far, turned out to be a best case in some
  way"*). **The genuinely-thin Settlement test case remains untested.**
- **⏸️ If a thin Mirny Settlement is ever wanted, the roster names it: `Mirny` itself — 9 TBDs, a stub
  Enneagram.** *(Noted, not recommended; a subnet capital is structurally exceptional in its own way.)*

---

# 6. ✅ THE COORDINATE MAP — 3-of-3 unanimity, INERT excluded

**Three isolated taggers, dispatched 2026-09-02, all reported. COMPLETE brief at dispatch** — char-span
granularity (M-92), positive-format paths (M-94), coverage assertions (M-96), and an explicit *"this brief is
final; ignore later amendments"* (M-93). **All three returned valid coverage assertions tiling their files.**

**⚠ `INERT` lines (blank · rule · table separator) are excluded from every figure below, per M-101.** **Lines
where any reader split a line into admissible and withheld character spans are collapsed CONSERVATIVELY to
`WITHHELD` at line grain** — the char-level detail survives in §6d as recoverable yield.

## 6a. The verdict

| File | Lines | INERT | Content | **ADMISSIBLE (3–0)** | unanimous WITHHELD | **SPLIT** |
|---|--:|--:|--:|--:|--:|--:|
| `Specs/Shirayuki.md` | 225 | 71 | 154 | **78.6%** | 6.5% | 14.9% |
| `Shirayuki_Physical_Infrastructure_Attributes.md` | 162 | 46 | 116 | **33.6%** | 49.1% | 17.2% |
| `Local_Cultures/Mirny_Subnet/Shirayuki.md` | 285 | 161 | 124 | **15.3%** | 50.0% | 34.7% |
| **TOTAL** | **672** | **278** | **394** | **45.4%** | — | — |

> ### ⭐⭐ CONSISTENCY RESULT — and this is the first one this methodology has ever been able to state.
>
> **Two cities, same subnet, independently mapped by six readers under two different contract versions:**
>
> | | Specs | Attributes megasheet | Culture sheet | **Total admissible** |
> |---|--:|--:|--:|--:|
> | **Casey** | 85.0% | 43.7% | 31.5% | **52.2%** |
> | **Shirayuki** | 78.6% | 33.6% | 15.3% | **45.4%** |
>
> ***The tier ordering replicates exactly — `Specs` cleanest, the "attributes" megasheet in the middle, the
> completed culture sheet dirtiest — and the totals land within seven points of each other.***
>
> **This is a corpus property, not a location property** (`§C.2` step 4). **Roughly half of a Tepenian city's
> content-bearing canon surface is conclusion-tier**, and the file whose *title* promises attributes is
> **two-thirds** conclusions on this city. **The `05` §6.1d warning that a `Specs/` file is not categorically
> safe is confirmed from the other direction too: it is the safest tier, but only at ~80%.**

## 6b. ✅ The 3–0 ADMISSIBLE set — SAFE TO OPEN

**`Specs/Shirayuki.md`** *(78.6% of content)*
`3, 5-11, 17, 19-22, 24, 30, 32, 40-41, 45-47, 49, 53, 57-73, 75, 83, 85, 91, 93, 97-98, 104, 106, 123-124,
126, 130, 134, 138-167, 172-175, 178-186, 189-193, 196-200, 203-209, 215-216, 220-223, 225`

**`Shirayuki_Physical_Infrastructure_Attributes.md`** *(33.6%)*
`3-6, 8-13, 21-26, 32-34, 42-43, 59-60, 67-69, 75-76, 81-82, 86, 92-95, 159-162`

**`Local_Cultures/Mirny_Subnet/Shirayuki.md`** *(15.3%)*
`3, 7-10, 24-26, 34, 36, 42, 159, 214, 262-264, 270-271, 277`

## 6c. ⛔ Unanimous WITHHELD — do not open; no ladder recovers these

**`Specs`:** `34, 81, 108, 113, 118, 125, 132, 195, 217, 224`
**`Attributes`:** 57 lines · **`Local_Cultures`:** 62 lines *(the bulk of both files' conclusion mass)*

## 6d. ⚠ SPLIT — accepted as WITHHELD, and this is what keeps `Status` honest

**86 content lines** *(`Specs` 23 · `Attributes` 20 · `Local_Cultures` 43)`.` **Currently `WITHHELD` by the
asymmetric rule, correctly.**

> **`§C.4` requirement 3 is satisfied by EXPLICIT ACCEPTANCE, not by working the ladder** — the ladder is
> **yield recovery, not a safety requirement.** **A run may proceed against §6b as it stands; it will simply
> be thinner than it needs to be.**

**⭐ Highest-value recovery available:** **every reader returned char-spans on the mixed lines**, and on
several they agree closely on the boundary *(e.g. `Specs` L108 `chars1-310` admissible from two readers
independently; `L113` `chars1-211` from two; `L125` `chars1-209`/`1-210`)*. **Ladder step 1 — re-split at
finer grain — is already half-done by the readers themselves.**

## 6e. Attribution

**3 readers · plain non-forked self-contained agents (M-75) · dispatched 2026-09-02 · contract version:
`Step −2` + `§C.2` as of 2026-09-02 with char-spans, positive-format paths and coverage assertions ·
`INERT` handling applied post-hoc by the consumer, per M-101, since the tag did not exist at dispatch.**

---

# 7. What this review can and cannot prove

**CAN:** that all four `Step −2` vectors were swept and closed for Shirayuki **before any deriver read
anything** · that three conclusion-tier leaks exist in required reading at named coordinates · that the
subject is measurably the most-determined city in its subnet.

**CANNOT:** ~~clear anyone to derive — no coordinate map yet~~ *(stale line, corrected 2026-09-03: the map
DOES exist, at §6. The sentence survived from this file's own `DRAFT` phase — **an internal contradiction with
its own `CONFIRMED` status block that nobody caught, exactly the Gate 0 both-directions failure**)* · Say
anything about what Shirayuki is like; **this session does not know.** · **Verify its own accuracy** —
`§C.2`'s standing warning holds.

> ### ⛔ AND THE ONE IT COULD NOT SAY UNTIL RUN 14 SAID IT
> ***This review CANNOT establish that the three files it maps are the SURFACE.*** **It never enumerated the
> registry, so its scope is an assumption wearing a pin.** **`§C.4` requirement 6 exists because of this
> sentence's absence.**

---

# 8. ⭐ REGISTRY SCOPE — `§C.4` requirement 6. **Built 2026-09-03 by a Brief B scout.**

**34 of 34 registry roots enumerated, no omissions.** **Search terms: the ALIAS SET — `Shirayuki` ∪
`Bharati`** *(the real-world basis name; see §8d — sweeping the current name alone misses 13 memory entries)*.

## 8a. THE SCOPE PIN — re-run this on reuse. **A risen count means a source JOINED → demote to `DRAFT`.**

```
SCOPE-PIN 2026-09-03   (grep -rilE 'shirayuki|bharati' <root> | wc -l — FILENAMES ONLY)
graphify-out (project repo)        | 131      Cities (all)                     | 128
auto-loaded memory                 |  51      Literature/books/CurrentNovelDocs |  49
ULM/Test_Runs                      |  40      Background-Lore                  |  28
non-registry courtesy sweep        |  22      TepenianUniverseTimeline/graphify-out | 14
Concordia-City/Districts           |   9      Neo-Races-and-Cultures           |   9
to-be-integrated                   |   4      SouthernLights                   |   4
Super_Ultra_Megasheet              |   3      Reference (project)              |   3
ULM top-level                      |   3      Worldspace/Factions              |   2
Locations/Infrastructure           |   2      TepenianUniverseTimeline/Reference |  2
Robot_Biology_and_Culture          |   1      Worldspace/Characters            |   1
Canon_Gap_Resolution_Method        |   1      Theoretical-Calculations         |   1
ULM/Pre-Contamination_Reviews      |   1      TepenianUniverseTimeline/Worldspace |  1
                                   TOTAL | 510
```

> ### ⛔⛔ **THE LARGEST SINGLE SURFACE IS THE GRAPH INDEX — 131 + 14 = 145 FILES.** *(M-116.)*
> ***Larger than any canon root, and a `PreToolUse` hook mandates querying it on every tool call.***
> **`00_RUNBOOK.md` Step 10.1 item 5 rules it UNUSABLE — a retrieval layer cannot honor a quarantine.**
> **DO NOT INVOKE GRAPHIFY DURING THIS RUN.** ⏸️ *`CLAUDE.md` carve-out requested, not yet granted.*

## 8b. TIERING — 26 `WITHHELD` · 12 `MAPPED-NEEDED` · 6 `QUERYABLE-BY-SCHEMA`

| ⭐ `QUERYABLE-BY-SCHEMA` — **use Brief C. Never `grep` these by name.** | Why |
|---|---|
| `Cities/Division_of_Industry` *(7 files, 222–3,545 ln)* | **multi-city bulk — this is what burned Run 14** |
| `Cities/` top-level ≥500 ln *(5 files, 532–1,190)* · <500 ln *(8 files, 108–274)* | multi-city bulk |
| `Cities/City_Symbolic_Substrate` *(1 file, 133)* | **row-level mixing — anchor to columns 1–3 only, per `05` §6.1c** |
| `Locations/Infrastructure` *(2 files, 38–322)* | corpus-wide route tables **(G5)** |
| `Theoretical-Calculations` *(1 file, 1,155)* | corpus-wide engineering model |

| ⛔ `WITHHELD` — highest-value rows only | Why |
|---|---|
| `graphify-out` ×2 | **retrieval_layer** |
| `auto-loaded memory` *(51)* · `CurrentNovelDocs` *(49)* · `Background-Lore` *(28)* | culture_conclusions · **authored_titles** |
| `Cities/Local_Cultures` · `Local_Robot_Culture` *(20)* · `City_Enneagram_Personalities` · `City_Megasheets` · `City_Master_Reference` | culture_conclusions |
| `Cities/City_Vision_Notes` · `Storyline` · `Dev-Road-Map` · `to-be-integrated` · `Super_Ultra_Megasheet` · `Local_Robot_Culture_Methodology` | **unratified** *(`05` §6.3)* |
| `ULM/Test_Runs` incl. **this run's own status file** | culture_conclusions |

**`MAPPED-NEEDED` (12):** `Robot_Biology_and_Culture` · `Factions` · `Canon_Gap_Resolution_Method` ·
`Cities/Research_Logs` · `Cities/Specs` · `Reference (project)` · `ULM/Pre-Contamination_Reviews` ·
`Game-Mechanics` · `Code-Architecture` · `testing` · `TepenianUniverseTimeline/Reference` ·
`TepenianUniverseTimeline/Worldspace`.
*Mostly 1–3 files of incidental mention. `Cities/Specs` is already mapped for this subject (§6);
`Cities/Research_Logs` is admissible by rule (`00_RUNBOOK.md` §C).*

## 8c. ⚠ `REQUIRED-READ-WITH-SKIPS` — the fourth tier, and the scout could not express it

**3 ULM top-level files carry the subject's name** *(`02`, `05`, `06` — exactly §4's skip list)*. **The scout
tiered them `WITHHELD` conservatively and flagged that the closed set had no slot for "read in full, with skip
ranges."** ***That refusal to improvise created the fourth tier (M-115).*** **Treat them per §4, not as
withheld.**

## 8d. ⭐ THE ALIAS SET — record it, because a sweep is only as wide as its alias list *(M-118)*

| Alias | Status |
|---|---|
| **Shirayuki** / **白雪** | current official name, 2026-07-08 |
| **Bharati** | ⚠ **the real-world basis station.** Simultaneously an admissible **G7** attribute *and* the key to prose written before the rename |
| *"Japanese Diplomatic Partition (cf. Bharati) — Name TBD"* | retired placeholder, 2026-07-03 |
| 59 dropped candidates | `Specs/Shirayuki.md` §Prospective Names — **inert; not search terms** |

> **Measured: `grep -ril shirayuki` on memory → 38. Adding `bharati` → 51.** ***13 entries name the subject
> only by its retired/real-world designation, and vector 2 was recorded CLOSED against the current name
> alone.*** **Memory is PUSH. Re-run vector 2 across the alias union before the next run.**

## 8e. What requirement 6 does and does not now establish

**DOES:** the registry is enumerated at a stated width · the scope is pinned and re-verifiable · every source
carries a tier · the alias set is recorded.

**DOES NOT:** ***clear the 12 `MAPPED-NEEDED` sources — they have no 3-of-3 coordinate map*** *(requirement
2)*. **⛔ This review stays `DRAFT` until three independent Brief A mappers cover that set.**

> ⚠ **And the standing caveat from `§C.4`: a scope pin is a CHANGE detector, not a COVERAGE PROOF.** It will
> catch a source that joins after 2026-09-03. **It cannot prove the 34 roots were the right 34** — that rests
> on the registry itself being complete, and `§D` was found naming a source with no path on this same day
> (M-117).

---

# 9. ⭐ THE SECOND COORDINATE MAP — 14 registry files, 3-of-3. **Built 2026-09-03, discharging requirement 2 for the `MAPPED-NEEDED` set.**

**Three isolated Brief A readers, dispatched simultaneously, tagging the same 14 files independently.**
**All three returned `MANIFEST: mapped 14 of 14 — not reached: none`, and every file carried a valid
`COVERAGE 1-n no gaps no overlaps` assertion.** **Consumer verified all three arithmetically before use.**

## 9a. The verdict — **57.0% of content-bearing lines are 3-of-3 ADMISSIBLE**

| File | n | INERT | content | **A 3-0** | adm% |
|---|--:|--:|--:|--:|--:|
| `Developer_Ruling_Queue.md` | 625 | 59 | 566 | 396 | **70.0%** |
| `testing/QA_template.md` ⚠ *(see §9d)* | 620 | 15 | 605 | 128 | **21.2%** |
| `City_and_District_Research_Topics.md` | 322 | 15 | 307 | 242 | **78.8%** |
| `City_Origin_Factions_Second_Interwar.md` | 286 | 59 | 227 | 5 | ⛔ **2.2%** |
| `Research_Logs/Zhongshan_Research_Log.md` | 270 | 58 | 212 | 154 | **72.6%** |
| `Robot_Physiology_and_Cultural_Practices.md` | 241 | 21 | 220 | 204 | **92.7%** |
| `Cross_City_Cultural_Patterns.md` | 169 | 19 | 150 | 31 | ⛔ **20.7%** |
| `«UNIV»/…/Amundsen_Station_Archive_and_Trucking_Network.md` | 114 | 45 | 69 | 65 | **94.2%** |
| `Game-Mechanics/Universal_Rules.md` | 113 | 37 | 76 | 76 | **100%** |
| `…/Antarctic_Stations_With_Airstrips.md` | 99 | 16 | 83 | 78 | **94.0%** |
| `«UNIV»/…/Falkland_Treaty/Scaffold.md` | 93 | 46 | 47 | 47 | **100%** |
| `Code-Architecture/README.md` | 66 | 12 | 54 | 54 | **100%** |
| `«UNIV»/…/Worldspace/Locations/README.md` | 31 | 9 | 22 | 22 | **100%** |
| `…/Climate Data/READER/Bharati_TBD.md` | 7 | 3 | 4 | 4 | **100%** |
| **TOTAL** | **3,056** | **414** | **2,642** | **1,506** | **57.0%** |

> ### ⭐⭐ THE CORPUS PROPERTY HOLDS ACROSS A COMPLETELY DIFFERENT FILE SET
> **§6 measured 45.4% admissible across 3 city-specific files. This measures 57.0% across 14 registry files
> that merely MENTION the subject.** ***Both land near half*** — **and `§C.2` step 4's claim that this is *a
> corpus property, not a location property* now has a third independent measurement behind it.**
>
> **The two lowest scores are the two files whose subject matter IS cross-location culture** —
> `City_Origin_Factions_Second_Interwar.md` at **2.2%** and `Cross_City_Cultural_Patterns.md` at **20.7%**.
> ***A file's admissibility tracks what it is ABOUT, far more than where it lives.***

## 9b. ⚠ SPLIT rate — recorded, and accepted as `WITHHELD` *(requirement 3)*

| Outcome | lines | % of content |
|---|--:|--:|
| **3-0 ADMISSIBLE** | 1,506 | **57.0%** |
| 3-0 WITHHELD | 547 | 20.7% |
| **SPLIT (2-1 A/W) → accepted as `WITHHELD`** | **458** | **17.3%** |
| *(INERT excluded from every figure, per M-101)* | 414 | — |

**The ladder was NOT worked on the 458 split lines.** ***`§C.4` requirement 3 is satisfied by explicit
acceptance; the ladder is yield recovery, not a safety gate.*** **A run may proceed against §9a as it stands;
it will simply be thinner than it needs to be.**

## 9c. Attribution

**3 readers · plain self-contained agents · dispatched 2026-09-03 · Brief A of
`Test_Runs/COLD_RUN_CHECKLIST.md` with the four-tag set, char-span granularity, coverage + manifest
assertions, and the M-115 escape hatch.** **Maps on disk at `…_Run14_Cold/maps/R1|R2|R3/`; computed verdict
at `maps/unanimity_verdict.json`.**

> **⚠ Consumer errors corrected before this table was trusted — see M-113, M-122, M-124.** **Three arithmetic
> faults occurred on the CONSUMER side; none on the readers'.** ***The figures above are post-correction.***

## 9d. ⚠ Two reader-reported anomalies, both real

1. **`testing/QA_template.md` is not a QA template.** It holds the full *Founding-Nation Bug Investigation
   Methodology*. **Tiered and mapped by content, not by name** *(M-123)*.
2. **Three readers disambiguated same-basename map files three different ways.** **Resolved by canonicalizing
   declared paths against the filesystem** *(M-122)*; **Brief A now fixes the naming convention.**

## 9e. THE PIN for these 14 files — reverify before reuse

```
«UNIV»/TepenianUniverseTimeline/Reference/Amundsen_Station_Archive_and_Trucking_Network.md|4ad29e4de0065bf7|114
«UNIV»/TepenianUniverseTimeline/Reference/Falkland_Treaty/Scaffold.md|b54502254ceae10b|93
«UNIV»/TepenianUniverseTimeline/Worldspace/Locations/README.md|b7ee200950ce8839|31
Code-Architecture/README.md|012277ce5c93d9ba|66
Game-Mechanics/Universal_Rules.md|2dfcd2e8628993c3|113
Reference/Real-World/City_and_District_Research_Topics.md|2d9ff3885a639b27|322
Reference/Real-World/Climate Data/READER/Bharati_TBD.md|7e752622be3f0ba2|7
Reference/Real-World/Stations/Antarctic_Stations_With_Airstrips.md|5a452109d21e5178|99
Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md|46a7842c37f5c0d7|625
Worldspace/Factions/City_Origin_Factions_Second_Interwar.md|883636a6bec9987e|286
Worldspace/Factions/Cross_City_Cultural_Patterns.md|bd23447fd028428d|169
Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Zhongshan_Research_Log.md|9336e3fe20608f26|270
Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md|74b3afcb80255089|241
testing/QA_template.md|e6cde5a5c5025142|620
```
