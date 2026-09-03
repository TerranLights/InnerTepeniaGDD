# Pre-Contamination Review — SHIRAYUKI

**Location:** Shirayuki · **Parent:** Mirny subnet · **Type:** Settlement · **Frame:** Second Interwar, pre-war
**Built:** 2026-09-02 · **Mechanism:** `../00_RUNBOOK.md` §C.4 · **Readers:** 1 vector-1 scanner + 1 roster
scout reported; **3 coordinate taggers in flight**

# ✅ Status: **CONFIRMED** — 2026-09-03

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

# 2. ⛔ The pin — REVERIFY BEFORE REUSING

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

| Path | Contents | Safe to list? |
|---|---|---|
| `Cities/Specs/Shirayuki.md` | 225 lines | ✅ |
| `Cities/Local_Cultures/Mirny_Subnet/Shirayuki.md` | 285 lines | ✅ |
| `Cities/City_Megasheets/Mirny_Subnet/Shirayuki/` | 6 files, 51–272 lines | ✅ template-named |
| `Cities/Local_Robot_Culture/Mirny_Subnet/Shirayuki.md` | 279 lines | ✅ *(⛔ quarantined content)* |
| `Cities/City_Enneagram_Personalities/Mirny_Subnet/Shirayuki.md` | **76 lines** | ✅ *(⛔ quarantined content)* |
| `Cities/City_Vision_Notes/Shirayuki.md` | 35 lines | ✅ *(⛔ quarantined — `05` §6.1 tier, see Casey review §6 reasoning)* |
| **`Background-Lore/Cities/Mirny_Subnet/Shirayuki/`** | **13 files, 98–668 lines** | ⛔⛔ **NEVER `ls`. Address by index.** *(M-88)* |
| `Cities/Research_Logs/` | **none for Shirayuki** | **Create one at Step 3** per `00_RUNBOOK.md` §3.7 |

---

# 4. ⛔ Required-reading SKIP LIST — the three lines, located and unread

> ## ⛔⛔ CORRECTED 2026-09-03 — SKIP RANGES, NOT LINES. See M-103.
>
> **The line-only version of this table was insufficient and it burned Run 13's own deriving session.**
> ***A worked example is not a self-contained leak: the RULE it illustrates is stated in the surrounding
> prose, and the rule is the more portable half.*** **Skipping line 359 while reading 355–358 delivered the
> whole analytical claim, minus only the city's name — which the file's structure supplies anyway.**
>
> ### ⚠ **DO NOT READ ADJACENT LINES TO "VERIFY THE BOUNDARY." That verification IS the exposure.**
> **Trust the range below. The reader that built it is the only party able to see both sides.**

| File | **SKIP RANGE** | Class | Action |
|---|--:|---|---|
| `02_Generators_Capability_and_Symbols.md` | **§4.1 entire — from the `## 4.1` heading through the end of the PEER-FREE address-axis subsection *(covers L359 and the rule statement it exemplifies)*** | ⛔⛔ **CONCLUSION-EXAMPLE** | **SKIP THE WHOLE SUBSECTION.** Its rule is recoverable from `00_RUNBOOK.md` Step 2 item 5 without the example |
| `05_The_Input_Contract.md` | **211** | ⛔ **CONCLUSION** | **SKIP** — verify whether this is also example-bearing before trusting a line-only skip |
| `05_The_Input_Contract.md` | **215** | ⛔ **CONCLUSION** | **SKIP** — same caution |
| `06_Worked_Example_Provenance.md` | 77 | ATTRIBUTE | none — inside another city's section |
| `06_Worked_Example_Provenance.md` | 161 | ANECDOTE | none |
| `00`, `01`, `03`, `04`, `README`, `Cultural_Synthesis_Techniques.md`, `Real-World_Basis_Extrapolation_Method.md`, `00b`, `00d`, `00f` | — | **CLEAN — verified, not assumed** | none |

**Read `02` and `05` in two `Read` calls each, skipping the flagged line.** **Do not "read carefully past
it"** — `05` §6.1a rule 1 is about exposure, not intent.

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

**CANNOT:** clear anyone to derive — **no coordinate map yet.** · Say anything about what Shirayuki is like;
**this session does not know.** · **Verify its own accuracy** — `§C.2`'s standing warning holds.
