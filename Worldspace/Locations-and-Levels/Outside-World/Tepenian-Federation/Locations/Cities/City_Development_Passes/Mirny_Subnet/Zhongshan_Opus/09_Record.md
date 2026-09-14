# STEP 9 — RECORD

**Zhongshan · ⭐ OPUS ARRAY · 2026-09-11 · Frame: Second Interwar (2564–2812)**

> **Required files read in full for this step:** `00_RUNBOOK.md` Step 9 + §9.5 ·
> `Stepwise_Execution/01_Spine/S11_Step_9_Record.md` *(117 lines)*. **Both.**

---

# 1 · THE QA BLOCK AND THE REVIEW PANEL BLOCK

⚠ **The instruction says *"append"*, and this pass's structure is FLAT — one file per step, by developer
instruction** *(`README.md`: "organize by subnet/city/city-files, instead of by process")*. **So the two blocks
are their own files rather than appended sections, and the Review Panel's output block is reproduced inside
`08` in `00f` §8's exact template.** ✅ **Recorded as a structural difference, not a skip.**

| Block | Where | Contains |
|---|---|---|
| **QA** | **`07_QA_Gates.md`** *(438 lines)* | **All 17 gates.** *15 run, `10` routed to Step 8, `P` N/A with a reason.* ⛔ **Three fired: `11`, `I`, and the seeded `R-25`.** **Raw scan output pasted throughout, including the runs that were invalid** |
| **Review Panel** | **`08_Review_Panel.md`** | **6 Flat Archetypes + Passer-Through + Neighbor + the Lover faculty.** *Life Arcs run, 3 silences. Shadow bench run. Four-corner check passed.* **Dispositions: accepted 11 · noted 3 · rejected 0 · refereed 1 · unmet 1 · declined 2** |

---

# 2 · THE DIFFERENTIATION ROW — ✅ **already added at Step 6, verified here**

```
=== Cross_City_Culture_Differentiation_Table.md ===
rows mentioning this city : 9
file length              : 142 lines
```

✅ **Nine rows, added in Step 6's own commit as the instruction requires.** ⭐ **One AXIS per cell, never the
content.** ⛔ **Write-only: no other city's cell was read or printed at any point in this pass**
*(`THE LAW OF ONE LOCATION`, developer ruling 2026-09-06)*.

## ⚠ 2b · PROPAGATION — *"if this pass noticed anything about ANOTHER city, record that here too"*

> **`04` III.0: *propagation is part of the finding, not a follow-up.*** *(A symbol collision was once noticed
> correctly, filed in one city's own culture file, and never reached the guide whose job was catching it.)*

⛔ **This pass noticed nothing about another CITY'S CULTURE — by construction, since it never read one.**
✅ **What it did notice is three defects in SHARED DATASHEETS, which propagate to every city that uses them:**

| Ref | What | Affects |
|---|---|---|
| ⭐⭐ `R-30` | **`Division_of_Industry/05` §3's density benchmark** — *flagged unreconciled in its own text, and disagreeing with `Extent_and_Density_Per_City.md` by `7.9×`–`11.3×`* | ⛔ **Every city pass that quotes a density** |
| ⚠ `R-13` | **`Highways.md` L318:** *"`Ports.md` exists and is EMPTY (0 bytes)"* — **it is 706 lines** | Any pass reading Hwy routing |
| ⚠ `R-14` | **`Highways.md`'s "Hitchhiking-Valid Highways" list omits `Hwy 22`**, against a developer ruling of 2026-09-10. ⚠ *And the file's own node rule then requires stopping places along the transcontinental interior* | Any pass on that corridor |

⛔ **NONE APPLIED.** *Developer datasheets are not this pass's to edit; all three are docketed as proposed
corrections.*

---

# 3 · TRACKERS UPDATED — ⛔ **and deliberately NOT marked complete**

> **Gate 0's concern is OVERCLAIMING COMPLETION.** **`M-109`: a tracker entry is what remains to be done, one
> line, plus a pointer. The finding goes in the observations log and nowhere else.**

| File | Before | After |
|---|---|---|
| **`ULM_Run_Progress.md`** L372 | `\| **Zhongshan** \| · \| · \| …` *(13 dots)* | **Steps `−1`–`8` ✅ · Step `9` ▶ · Step `9.5` ✅ · Step `10` ·** |
| **`MASTER_Process_Tracker.md`** L239 | `\| Zhongshan \| · \| · \| · \| ✅ \|` | **One line: steps done, Step 10 pending, the Sonnet array held, and a pointer here** |

> ## ⛔⛔ WHY NEITHER SAYS "COMPLETE"
> **1 · `Step 10 — THE READINESS CHECK` has not run**, and `CLAUDE.md` names it one of two standing steps that
> are *"easy to skip and not optional"* — ***"verify, do not assert; on its first use it caught the largest
> hole in the anti-contamination protocol."***
> **2 · ⚠ THERE ARE TWO ARRAYS.** **`Zhongshan_Sonnet/` sits at Phase 3 and is deliberately untouched** — *a
> Sonnet/Opus divergence fork.* ⛔ ***Which array is canonical is an open developer question, and a tracker
> row reading "Zhongshan ✅ COMPLETE" would answer it silently.***
>
> ⭐ **The subnet header's `1 / 8 ULM COMPLETE` is therefore left UNCHANGED.**

---

# 4 · METHODOLOGY CHANGES — **made in the same commit, per `CLAUDE.md`: *"Both, or neither"***

| Change | Where | What was learned, and on which location |
|---|---|---|
| ⭐⭐ **`04` Part V — Instruments on Trial** *(182 ln)* + **`Tools/quotation_audit.py`** | `Universal_Location_Methodology/` | **On Zhongshan (city 3): four quotation defects, ALL in table cells, none in prose — layout pressure, not carelessness.** ⭐ **And the methodology named "the quotation audit" 15 times while defining it ZERO times** |
| ⭐⭐ **`04` Part V.2 — The Handoff Ledger** *(154 ln)* + **`Tools/handoff_audit.py`** | Same | **On Zhongshan: the `§H` sweep was formally enumerated in `3` of `8` eligible phases.** ⭐ **A skipped sweep sheds the axis's own blind spot, and the `Lover faculty` passed only on repaired material** |
| ✅ **`00_RUNBOOK.md`** — an `ON TRIAL, NOT BINDING` pointer to both | Same | *Point-of-use registration, per `M-121`* |

> ### ⭐⭐⭐ **AND BOTH TRIALS STATE A FALSIFICATION CONDITION IN ADVANCE**, which `04` Part IV says *"costs nothing and is the one that has never been done."* **This is the first time it has been done.**
>
> ⛔ **Both are TESTS, not rules.** **A pass that ignores them is not in violation.** ⛔ **`Zhongshan_Opus` is
> the BASELINE and must not be corrected; `Zhongshan_Sonnet` must not run either.**

---

# 5 · `09.5_Log.md` — ✅ **WRITTEN**

**Five self-corrections · five killed findings · seven instrument failures · six blockages · six internal
methodology contradictions · three tooling obstacles · eight techniques that worked.**
⭐ **The `G6` disposition transcribed verbatim, as `04.9` §7 instructed.**
⚠ **Two entries record failures found in the pass's OWN earlier self-reports** — *the recording law working on
the recorder.*

---

# 📋 EXECUTION LOG

**Location:** Zhongshan *(Opus array)*  **Date:** 2026-09-11  **Frame:** Second Interwar (default)

| # | What the instruction demanded | Where it said to look | Found? | Raw evidence |
|--:|---|---|:--:|---|
| 1 | Append the QA block | this pass | ✅ | `07_QA_Gates.md`, 438 ln, 17 gates, raw output pasted |
| 2 | Append the Review Panel block | this pass | ✅ | `08_Review_Panel.md`, `00f` §8 template reproduced |
| 3 | Differentiation row, same commit | `Cross_City_Culture_Differentiation_Table.md` | ✅ | `grep -c "Zhongshan"` → **9**; added at Step 6 |
| 4 | Propagation to other cities | `04` III.0 | ✅ | **0 culture findings** *(never read one)*; **3 shared-datasheet defects** docketed — §2b |
| 5 | Update whatever tracker claims completion | `ULM_Run_Progress.md` · `MASTER_Process_Tracker.md` | ✅ | Both edited; ⛔ **neither marked complete** — §3 |
| 6 | Methodology change → runbook, same commit | `04` · `00_RUNBOOK.md` · `Tools/` | ✅ | Parts V and V.2, two tools, one runbook pointer — §4 |
| 7 | §9.5 recording law | `09.5_Log.md` | ✅ | Written; `G6` verbatim; 8 sections |
| 8 | Number `M-n` continuously | `Test_Runs/OBSERVATIONS…` | ⛔ | **CANNOT BE FOLLOWED AS WRITTEN** — see below |

## ⛔ Anything the instruction demanded that could NOT be found

```
=== highest M- number with an ENTRY in OBSERVATIONS_and_Methodology_Findings.md ===
171  172  173

=== distinct M numbers 170+ anywhere in the ULM ===
M-170  M-171  M-172  M-173  M-205  M-208

=== are M-205 / M-208 DEFINED anywhere? ===
(no results)
```

> ⛔⛔ **`M-205` and `M-208` are cited in `00_RUNBOOK.md` and defined nowhere. The log ends at `M-173`, leaving a
> `31`-number gap.** ⚠ **And `M-208` is LOAD-BEARING — it is the authority cited for the Step 4 close-out
> check, the check that caught this pass's own `G6` omission.**

## ⚠ Anything I had to decide that the instruction did not state — ⛔ *each is a developer question, not a judgment call*

| | Decision taken | Why, and what I did not do |
|---|---|---|
| **1** | **New entries numbered from `M-209`** | *The only value that cannot collide and does not restart.* ⛔ **I did NOT renumber anything, fill the `174–204` gap, or write entries for `M-205`/`M-208`** |
| **2** | **Trackers updated but NOT marked complete** | *Step 10 is unrun and there are two arrays.* ⛔ **I did NOT decide which array is canonical** |
| **3** | **The QA and Panel "blocks" are separate FILES** | *The pass's flat structure is a developer instruction.* ✅ *Recorded as a structural difference* |

**Verdict:** ☑ **step complete** ☐ blocked

> ### ⚠ BEFORE REPORTING, THE TWO THAT ARE ALWAYS FORGOTTEN
> ☑ **Did this step change the methodology?** → ✅ **Yes — Parts V and V.2, two tools, the runbook pointer.**
> **Six entries proposed for the shared log at `09.5` §10, numbered from `M-209`.**
> ☑ **Did I modify any file?** → ✅ **Yes.** ⏸️ **`graphify update .` is owed** *(`CLAUDE.md`)* — **batched,
> not per-edit, per the standing preference.**

---

# ✅ STEP 9 — CLOSED

## Canon opened *(`M-171` receipt)*

| ✅ OPENED | Extent |
|---|---|
| **`00_RUNBOOK.md` Step 9 + §9.5** | In full |
| **`S11_Step_9_Record.md`** | **All 117 lines** |
| **`Cross_City_Culture_Differentiation_Table.md`** | ⛔ **COUNTED ONLY** — *`grep -c` for this city's own rows.* **No other city's cell read or printed** |
| **`ULM_Run_Progress.md` · `MASTER_Process_Tracker.md`** | This city's rows and their column headers |
| **`Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`** | ⛔ **NUMBERING ONLY** — *`grep` for the `M-` ceiling and the file's tail structure.* **Not read as input** |

## Refused, and why

| ⛔ REFUSED | Why |
|---|---|
| **The three `Test_Runs/` bodies for this city** | **ZERO INTAKE, whole pass duration** *(`00.1` L30, `00.0` L173)*. ⭐ **They reopen once this pass closes** |
| **`City_Megasheets/`** | Withheld corpus-wide |
| **Every other city's differentiation cell** | `THE LAW OF ONE LOCATION` |
| **Writing `M-205`/`M-208` entries** | ⛔ **Not mine to invent.** *A developer question* |
| **Editing `Highways.md`, `Specs/`, `Division_of_Industry/`** | **Developer datasheets.** *Proposed corrections docketed instead* |

⛔ **`Step 10 — THE READINESS CHECK` opens next** — *`CLAUDE.md`:* ***"verify, do not assert; on its first use
it caught the largest hole in the anti-contamination protocol."*** **It is the last step, and it is the one
this pass has the most reason to run honestly.**
