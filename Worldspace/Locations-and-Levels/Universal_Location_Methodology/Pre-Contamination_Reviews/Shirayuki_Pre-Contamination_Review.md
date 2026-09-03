# Pre-Contamination Review — SHIRAYUKI

**Location:** Shirayuki · **Parent:** Mirny subnet · **Type:** Settlement · **Frame:** Second Interwar, pre-war
**Built:** 2026-09-02 · **Mechanism:** `../00_RUNBOOK.md` §C.4 · **Readers:** 1 vector-1 scanner + 1 roster
scout reported; **3 coordinate taggers in flight**

# ⚠ Status: **DRAFT** — vectors 1, 2, 3, 4 CLOSED · coordinate map pending

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

| File | Line | Class | Action |
|---|--:|---|---|
| `02_Generators_Capability_and_Symbols.md` | **359** | ⛔ **CONCLUSION** | **SKIP** |
| `05_The_Input_Contract.md` | **211** | ⛔ **CONCLUSION** | **SKIP** |
| `05_The_Input_Contract.md` | **215** | ⛔ **CONCLUSION** | **SKIP** |
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

# 6. The coordinate map — ⏳ PENDING

**Three isolated taggers were dispatched 2026-09-02 against the three pinned files, under a COMPLETE brief**
— character-span granularity (M-92), positive-format path handling (M-94), coverage assertions (M-96), and
an explicit instruction that **the brief is final and any later amendment must be ignored** (M-93).

> ### ⭐ This is the first dispatch made under the full corrected contract.
> **Casey's readers ran under three different contracts because the brief was patched mid-flight** — which
> made its 28% split rate partly a grain artifact that could not be separated out *(Casey review §5b)*.
> **This run's three readers are contract-identical**, so its disagreement rate will be **the first clean
> measurement of genuine inter-reader variance** this methodology has.

**On their return:** apply 3-of-3 unanimity → work the escalation ladder on every split → record the
withheld-rate → attribute the tagging → flip `Status:` to `CONFIRMED`.

---

# 7. What this review can and cannot prove

**CAN:** that all four `Step −2` vectors were swept and closed for Shirayuki **before any deriver read
anything** · that three conclusion-tier leaks exist in required reading at named coordinates · that the
subject is measurably the most-determined city in its subnet.

**CANNOT:** clear anyone to derive — **no coordinate map yet.** · Say anything about what Shirayuki is like;
**this session does not know.** · **Verify its own accuracy** — `§C.2`'s standing warning holds.
