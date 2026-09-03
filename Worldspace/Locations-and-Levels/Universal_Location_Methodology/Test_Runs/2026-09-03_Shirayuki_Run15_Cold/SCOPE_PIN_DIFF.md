# SCOPE PIN DIFF — §8a *(Run 14, 2026-09-03)* vs. Run 15 scout *(2026-09-03, later same day)*

**Verdict: the pin DOES NOT CLEANLY VERIFY, but not for the reason the headline numbers suggest.**
**Review demoted to `DRAFT` under `§C.4` requirement 2 — not requirement 6.**

| | §8a baseline | Run 15 | |
|---|--:|--:|---|
| Roots | 34 | **38** | ⚠ **different partition — the totals are NOT comparable** |
| Files | 510 | **471** | ⚠ see below |

## 1. Where the partitions align, the counts are IDENTICAL — 17 roots, zero drift

`Cities (all)` **128 = 128** *(Run 15 splits it 116 + `C.1` 5 + `C.6` 7)* · `CurrentNovelDocs` **49 = 49** ·
`Background-Lore` **28 = 28** · `Neo-Races-and-Cultures` **9 = 9** · `to-be-integrated` **4 = 4** ·
`SouthernLights` **4 = 4** · `Super_Ultra_Megasheet` **3 = 3** · `Reference (project)` **3 = 3** ·
`Factions` **2 = 2** · `Locations/Infrastructure` **2 = 2** · `UNI/Reference` **2 = 2** ·
`Robot_Biology_and_Culture` **1 = 1** · `Characters` **1 = 1** · `Canon_Gap_Resolution_Method` **1 = 1** ·
`Theoretical-Calculations` **1 = 1** · `UNI/Worldspace` **1 = 1** · `UNI/graphify-out` **14 = 14**.

> ***This is the meaningful result: no canon source joined.*** **The pin's actual job — change detection —
> comes back clean everywhere it can be evaluated.**

## 2. The four movements, all explained, none a foreign source

| Root | Δ | Cause |
|---|--:|---|
| `GDD/graphify-out` | 131 → **135** | **graph rebuilt** *(a dated `2026-09-03` build folder exists)*. `WITHHELD`, **never opened** |
| `ULM` *(Test_Runs + Pre-Contamination + top-level)* | 44 → **49** | ⚠ **self-inflicted** — Run 14's own cleanup, plus **this run's two files**. A cold run's scope pin counts the run |
| `Concordia-City` | 9 → **10** | §8a swept only `…/Districts`; Run 15 swept the whole root |
| `Storyline` **17** · production tree **7** | *(absent)* | §8a folded these into an unlabeled *"non-registry courtesy sweep, 22"*. **24 vs 22 — a 2-file residue that cannot be resolved without a name search, so it is NOT resolved** |

**The 510 → 471 fall is an artifact, not a shrinkage:** §8a's total included `auto-loaded memory` **51**, which
Run 15 correctly did **not** sweep *(`STEP −3` blackout; memory is not a canon root in `§B`/`§C`/`§C.1`/`§C.6`/`§D`)*.

> ### ⚠ A scope pin whose partition is not itself pinned cannot be re-verified.
> **Two competent scouts, one day apart, on the same corpus, produced 34 roots and 38 roots.** ***The pin
> records counts but not the root LIST that produced them, so a partition change is indistinguishable from a
> content change.*** **`§8a`'s own instruction — "a risen count means a source JOINED" — is unfalsifiable in
> that state.** **Fix: pin the root list, not just the per-root counts.**

---

# 3. ⛔ THE ACTUAL BLOCKER — six sources the review does not cover

***Requirement 6 (registry enumerated) survives. Requirement 2 (every mapped source has a 3-of-3 verdict)
does not.***

## 3a. Four `Cities/` top-level files are `MAPPED-NEEDED` **with no coordinate map**

`Inspirational-Influences.md` · `Station_to_City_Map.md` · `Overview.md` ·
`National_Medical_and_Care_Institutes.md`

**§8b never tiered these individually** — it tiered `Cities/ top-level` **in bulk by line count**
*(`≥500 ln (5 files)` · `<500 ln (8 files)`)* and called the whole band `QUERYABLE-BY-SCHEMA`.
**Run 15's scout opened them and found four that the deriver must READ.**

> ### ⭐ This is M-123 generalizing. **§8b routed by SIZE where M-123 forbids routing by NAME.**
> ***Both are metadata-routing.*** **A bulk tier assigned from a line count is exactly as blind as one
> assigned from a filename, and it misroutes in both directions for the same reason.**

## 3b. Two sources re-tiered `QUERYABLE-BY-SCHEMA` → `MAPPED-NEEDED`

`City_Symbolic_Substrate/` *(133 ln)* and `Theoretical-Calculations/` *(1,155 ln)*.
⚠ **Two scouts disagree here, and the disagreement is not resolvable by inspection.** **§8b's reasoning was
explicit and good** *(row-level mixing → anchor to columns 1–3; corpus-wide engineering model)*, **and the
checklist itself prefers `QUERYABLE` for large mostly-other-location files.**

## 3c. Divergences that are the MISSING FIFTH TIER, not hazard judgments

`Code-Architecture/` *(§9: **100%** admissible)* · `testing/` *(§9: 21.2%)* · `Dev-Road-Map/` · `TODO.md` ·
`DONE.md` — **all `WITHHELD` in Run 15.** ***The scout named this itself as `BRIEF-PROBLEM` 2:*** no member of
the closed four-tier set means *"names the subject, supplies no canon, poses no hazard."* **Per the M-115
escape hatch it took the conservative value.** **Read the withheld-rate accordingly — it is inflated, and
`§C.4` treats that rate as a finding about the corpus.**

---

# 4. Scout `BRIEF-PROBLEM`s — all four are methodology defects, two are live bugs

| # | Finding | Severity |
|---|---|---|
| **1** | **`00_RUNBOOK.md` §D carries two dead paths** under the line *"Absolute paths, all verified to exist 2026-09-03."* ***M-117 recurring inside the fix for M-117.*** A pass trusting §D gets a **false zero** | ⛔ **live bug — fix `§D`** |
| **2** | **The closed tier set has no value for "irrelevant."** Forces production/engineering material to `WITHHELD`, inflating the statistic | ⛔ **methodology gap** |
| **3** | **`§C.1`'s split extracts do not cover this subject's subnet** — extracts exist for two subnets only, so `City_Master_Reference/` is `WITHHELD` whole **with no admissible route to its attribute half** | ⚠ **supply gap for THIS run** |
| **4** | **M-123 is live, not historical** — `testing/QA_template.md` is a full duplicate of a canon-tree methodology file; **two further name/content mismatches** caught the same way | ✅ **control working as designed** |

---

# 5. ✅ Two independent confirmations worth recording

1. **The megasheet inventory dispute (M-113) is now settled three ways.** §3 recorded **6 files, 51–272**;
   Run 14 briefly claimed 7 files / 51–699 and retracted; **Run 15's scout independently returns 6 files,
   51–272.** ***The retraction was correct.***
2. **`Background-Lore/…/Shirayuki/` = 13 files** *(§3)* **reconciles exactly** with Run 15's split of
   `2 files (150–668)` + `Course_of_Events 11 files (98–103)`. **No `ls` was run by the deriver in either case.**
