# Run 14 — Shirayuki, cold — ⛔ HALTED IN PHASE 0, SPINE-LEVEL CONTAMINATION

**Date:** 2026-09-03 · **Subject:** Shirayuki · **Parent:** Mirny subnet · **Intended frame:** Second Interwar,
pre-war (Census II baseline) · **Status:** ⛔ **HALTED — awaiting a developer ruling under `00_RUNBOOK.md` §C.5**

---

# 1. What was done correctly, and it was not enough

**`COLD_RUN_CHECKLIST.md` was followed exactly, in order.** Every control held:

| Step | Result |
|---|---|
| 0 — name the subject, read nothing about it | ✅ subject taken from the developer, not derived from a file |
| 1 — review exists? | ✅ `CONFIRMED`; **pin re-verified, all three rows matched exactly** |
| 2–4 — dispatch / memory / no `ls` | ✅ **skipped legitimately** — the `CONFIRMED` path pays for these |
| 5 — runbook in full, then `01`–`05` skipping flagged ranges | ✅ `02` **340–378** and `05` **180–250** skipped; **neither boundary probed** |
| 6 — exposure ledger | ✅ kept from the first read; 8 entries + 3 leak notes |
| 7 — run specifics | ✅ `RESUME_HERE.md` **top box only** (70 of ~750 lines) |
| 8 — Phase 0 | ⛔ **halted mid-step** |

**The three mapped files were never opened directly.** A script (`§C.2`'s script-as-isolated-reader, M-101)
emitted only the 3-of-3 admissible lines with withheld ranges stubbed as coordinates. **Line counts matched
the pin: 225 / 162 / 285.**

---

# 2. How it burned — `Step −2` vector 5, previously unnamed

**Phase 0 needed G3 industry figures.** **`00_RUNBOOK.md` §C.6 — added 2026-09-03 — registers
`Division_of_Industry/` as the strongest G3 supply in the project and gives the address explicitly.**
***One `grep` for the subject's name, in the file the runbook had just instructed the pass to open, returned
conclusion-tier content.***

**Described by SHAPE and SIZE only, per M-97 — 6 fragments, across ~10 returned lines:**

| # | Tier | Shape of the fragment |
|---|---|---|
| 1 | ✅ attribute | per-city three-tier figures; a sector percentage and headcount |
| 2 | ✅ attribute | a sector-provider classification; restates the founding mechanism already in `Specs/` |
| 3 | ⚠ conclusion | a comparative claim setting the subject's economic asset against other cities' |
| 4 | ⛔ **SPINE** | **a developer quotation stating the subject's own developmental ARC** — what it was at founding versus what it became |
| 5 | ⛔ **SPINE** | **a derived mechanism linking the subject's two principal sectors** |
| 6 | ⚠ conclusion | a one-word category signature, inside a list of every city's signature |

**Fragments 4 and 5 are `§C.5` spine items** — the founding tension, and a capability mechanism. **`§C.5` is
explicit: *"There is no partial credit and no middle tier."*** ***This run is not cold.***

> ### ⚠ The exposure was NOT caused by carelessness, and recording it as carelessness would hide the finding.
> **The pass was following the runbook's own registry, at the address the runbook gives, for a generator the
> runbook requires.** ***The instruction to open the source and the quarantine that should have covered it
> live in the same file and do not know about each other.***

**Full analysis: `OBSERVATIONS_and_Methodology_Findings.md` M-112 (the channel, six links) · **M-113
(RETRACTED — a false finding by this run, and the retraction is the more useful entry)** · M-114/M-116 (the
graph index) · M-115 (the tier vocabulary) · M-117 (paths) · M-118 (aliases).**

---

# 3. Measured surface — counts only

| Registered source | Files naming the subject | Hit-lines | Mapped? |
|---|--:|--:|:--:|
| The `§C.4` coordinate map | **3** | — | ✅ 3-of-3 unanimous |
| `Division_of_Industry/` | 7 | 28 | ⛔ no |
| `City_Master_Reference/` *(no extract for this subnet)* | 5 | 22 | ⛔ no |
| `City_Megasheets/<subject>/` | 6 of **7** files | 51 | ⛔ 1 of 7 |

***101 hit-lines across 18 files sat outside a review reading `CONFIRMED`, whose pin verified.***

**⛔ A second claim made here earlier — that the review's §3 inventory undercounted the megasheet folder —
was FALSE and is retracted.** **The folder holds 6 files, 51–272 lines, exactly as the inventory says.** The
"699-line file" was a `wc -l` **`total`** row misread as a file. **See M-113, rewritten as a retraction.**

---

# 4. Work banked before the halt — **all of it attribute-tier, all of it survives**

**None of the following is downstream of the leak. It was derived from the admissible map, the census, the
symbol system files and the highways registry, all before the `Division_of_Industry` grep.** It is recorded so
a successor session inherits it rather than re-deriving it.

## 4a. Tier 0 — the pass can start

| Input | Value |
|---|---|
| Designation | **Shirayuki (白雪)**, "white snow" — named 2026-07-08; placeholder fully retired |
| Position | **Larsemann Hills, Prydz Bay ~69°24'S 76°11'E** — the former Bharati Station site; **1–2 km from Sinheung**, immediately adjacent to Zhongshan |
| Population magnitude | **728,324** at Census II → **Band 4 (Urban)** *(was 1,178,313 → Band 5 at Census I)* |
| Parent | **Mirny subnet** *(reassigned from Mawson 2026-07-05 on real-world geography)* |

## 4b. Generators available — **six**, and G1 is corroboration-tier by rule

| | Generator | Status |
|---|---|---|
| **G1** | Uranus + Fire | ⚠ **available but `[SELF-ORIGINATED]`** — `05` §6.1c: all 34 city assignments are provenance-downstream of a prior personality read. **Usable as corroboration, never as one of the three independent generators** |
| **G2** | Larsemann Hills ice-free oasis: exposed bedrock, meltwater lakes, Prydz Bay maritime access, **mild by Tepenian standards** | ✅ independent |
| **G3** | Education-centered economy; the Institute of Applied and Fine Arts; the Bharati Gallery Halls | ⚠ **partly compromised — this is the generator the leak arrived through** |
| **G4** | **Jeju-do diplomatic allocation** — an Upper Earth court assigned the unoccupied site to Japan pre-exile; settled 2564. **One of only two cities founded this way** (Sinheung is the other, allocated to Korea) | ✅ independent |
| **G5** | **Hwy 4's eastern terminus**, at a tri-junction with Hwy 110's and Hwy 22's endpoints — **the same physical junction shared with Zhongshan and Sinheung** | ✅ independent |
| **G8** | Japan 36.27% Primary; Australia 8.76 / Russia 8.61 / South Korea 7.89 / China 7.18 / Germany 4.93 Significant; 11 Notable nations | ✅ independent |

## 4c. ⭐ The G8 arithmetic — **the strongest thing this run produced, and it is uncontaminated**

**`02` §G8's retention instrument, run across all 33 cities present in both censuses, z-scored against the
full set per rule 1 rather than against the local group.**

**Census I → II is *pre-war relocation to orbit*, not loss — the census states its own limits outright:**
*"Population is conserved between Census I and Census II — nobody was born or died in the transition; they
relocated."* **Parse hand-verified against the raw row before use** (`00_RUNBOOK` Step 7): fields 5/6/7 =
576,469 / 601,844 / 1,178,313, matching `Specs/` exactly.

| City | Census I | Census II | Retention | z |
|---|--:|--:|--:|--:|
| **Sinheung** *(1–2 km away)* | 1,069,350 | 888,292 | **83.07%** | **+1.41** |
| **Zhongshan** *(immediately adjacent)* | 1,279,433 | 996,684 | **77.90%** | **+0.76** |
| *corpus mean (33 cities)* | | | *71.87%* | *0.00* |
| **SHIRAYUKI** | 1,178,313 | 728,324 | **61.81%** | **−1.26** |

> ### **Three cities share one ice-free oasis, one climate, one highway junction — and span 2.67 standard
> deviations of retention. G2 is held constant by construction. Whatever produced the divergence is not
> physical.**
>
> **Sharper still: Shirayuki and Sinheung share the *identical* founding mechanism** — both Jeju-do
> allocations, one decade, one geology, 1–2 km apart. **G4 is held constant too.** ***The corpus has handed
> this methodology a near-controlled comparison, and 21 points of retention separate the pair.***

**And the human/robot split — Shirayuki is the subnet's outlier in direction, not only in magnitude:**

| City | human retention | robot retention | delta |
|---|--:|--:|--:|
| **Shirayuki** | **58.31%** | **65.17%** | **+6.86 pp** |
| Sinheung | 84.33% | 81.87% | −2.46 pp |
| Zhongshan | 82.66% | 73.26% | −9.40 pp |
| Davis | 77.61% | 57.87% | −19.74 pp |

**Its humans left harder than its robots did.** *(Casey, +19.87 pp, is the only larger same-direction gap.)*

> ⚠ **Tag on any retention finding: `[CORROBORATION-TIER]`.** `06` line 77 records that this subject's
> retention figure once stood as a worked example in `02` §G8. **The ledger flagged it before the arithmetic
> was run.** The *figure* was re-derived here independently; the *interest* of the figure was not.

## 4d. Frame calls already settled

- **Temporal frame: Second Interwar, Census II baseline (pre-war).** Per `01` §4.1 and the standing project
  rule, **`Specs/`'s "Damaged; partially operational" is a POST-WAR status and was excluded as an input.**
- **Status: `Living`, not `Declining`** — `01` §3's migration note applies exactly: the drop is out-migration
  to a **documented destination inside the setting's own future** (the orbital tier, via Amundsen Tower).
  **The migration is stated in prose rather than given a status value.**
- **Configuration: EXCEPTIONAL.** Deepest design-tool coverage and fewest open TBDs of all eight Mirny cities
  — **the fourth consecutive best-case Settlement.** Findings will not generalize to a thin location.
- **Band 5 → Band 4 across the census pair** — the location crossed `01` §2.2's 4↔5 threshold *downward*.
  **Flagged as a live Phase 1 question, not yet answered.**

## 4e. ⚠ Standing obligation the successor inherits

**`02` §4.0 fires here and has not been discharged.** The admissible map admits the subject's known
institutions (the Institute, the Gallery Halls, the gallery district). **§4.0 rule 3 requires the shape be
read TWICE — once with known institutions admitted, once with them quarantined — because the shape follows
arithmetically from the input set.** **Neither reading has been run.**

---

# 5. The ruling required — `§C.5` offers exactly two options and forbids a third

| Option | What it means here |
|---|---|
| **A — declare WARM and continue** | Legitimate and precedented. **Loses the M-35 evidence class**: a warm pass cannot demonstrate blind convergence against withheld material, which is usually the whole point of a consistency run |
| **B — hand the derivation to a fresh session; this session extends the review** | `§C.3`'s pairing. **This session is now the best available map-builder and the worst available deriver.** The gap M-112 found — 18 unmapped files — is exactly the work it is now suited for, and doing it makes the successor's run cheap |
| ~~C — semi-cold~~ | ⛔ **Forbidden.** *"A 'semi-cold' run is a warm run wearing a cold run's credibility"* |

> ### ⚠ And `§C.5`'s closing warning applies directly: **do not solve this by switching subjects.**
> **Vectors are corpus-wide.** Switching to Casey or another city **trades a MEASURED contamination for an
> UNMEASURED one**, which is worse, because only the first can be declared.

**Recommendation: B.** **The pass lost is one location. The finding gained (M-112) invalidates the scope of
every pre-contamination review in the project, including Casey's — and it was only findable by a run that had
done everything right and been burned anyway.**
