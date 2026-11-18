# Differentiation Instrument — Quick Reference

> ⭐ **Tier U — corpus-wide, identical for every city.** Feeds every city's Step 6. Copied word for word from
> `04_QA_Gates_and_Differentiation.md` Part III (**L423–L526**; Part IV begins at L530) and `00_RUNBOOK.md` §"Step 6"
> (**L2897–L2934**; Step 7 begins at L2936), as of 2026-11-18. **Nothing below is city-specific — it is the
> same for all 38 cities and does not need re-extraction per city.**
> *(Re-copied 2026-11-18: the earlier version, re-read 2026-10-30, cited L420–L526 and L2886–L2921, was trimmed under an "Extracted in full" title, and lacked Step 6's two 2026-11-04 rules, `M-273` and `M-272`. The version before that cited L417–517 and L2843–2892. Sheet notes, marked as such, follow the copy.)* *(Re-copied in part 2026-11-18, `DR-142` item 2: `04` L518 and L526 amended in place, re-copied word for word at sheet L106 and L114; no line moved.)* *(Re-copied in part 2026-11-18, `DR-142` item 2 as corrected 2026-11-18 (substitutes 3 and 4 only): `04` L520 and L526 and `00_RUNBOOK.md` L2903 and L2914 amended in place, re-copied word for word at sheet L108, L114, L124 and L135; no line moved.)*

---

# Part III — The differentiation instrument

# ⛔⛔⛔ PART III IS **WRITE-ONLY** DURING A ULM / CST / RWBEM PASS — **RULED 2026-09-06**

> > ### **"In terms of your interpretation of Part III's 'anti-convergence' rule, yes, this is something we'll check for and decide at the very end. During the course of the ULM/CST/RWBEM, just follow the data wherever it leads for one single location on its own terms, and we'll worry about differentiation later."** *(Developer, 2026-09-06.)*

| | During a per-location pass | ⏸️ At the TERMINAL check |
|---|---|---|
| **Adding this location's row** | ✅ **REQUIRED, same commit as the finding** *(Step 9 unchanged)* | — |
| **Reading another location's row** | ⛔⛔ **FORBIDDEN** | ✅ **This is the whole job** |
| **III.2 step 1, "before writing a category, read its row"** | ⛔ **REVOKED in-run** | ✅ **Restored** |
| **III.4 substitutes** | ✅ **The ordinary path, for EVERY location** | — |

> ### ⭐ WHY THE TABLE STILL GETS FILLED — **it is the terminal check's only input**
> ***A write-only table is not a dead table; it is a table under construction.*** **`04` Part III already
> half-said this:** *"the table is FILLED DURING synthesis… it contributes nothing to the first city and
> everything to the thirty-seventh."* ⭐ **The ruling adopts that sentence literally and drops the half that
> contradicted it.** ⛔ **A pass that reads a neighbor's row writes AROUND that neighbor — and
> writing-around-a-neighbor is still a neighbor-shaped decision, which is convergence arriving by the door
> marked anti-convergence.**

> **⚠ And this Part was ALREADY peer-required — an enhancement, not the core.** Per `00_RUNBOOK.md`, the
> methodology's unit is **one location**, and **most passes will have no sibling set at all.** A pass without
> one is not failing this Part; it is running **III.4**, which is the ordinary path. **Do not treat a missing
> differentiation table as a missing gate.** ⭐ **As of the ruling, EVERY pass runs III.4** — the peer-free
> path is no longer the majority case, it is the only case.

> ### ⚠ SCOPE — **`ULM / CST / RWBEM` only. The district instrument is untouched.**
> **`Cross_District_Differentiation_Table.md` and the district runbook keep read-before-write**, on a
> 13-district corpus that is already complete. ⛔ **Do not harmonize the two.**

## III.0 ⚠ "Noticed somewhere" is not "available where it is needed"

**Added 2026-08-30 from a verified instance.** A differentiation instrument only works if the findings that
distinguish its members have actually **reached** it.

**The measured case.** Two cities in one three-city cluster were assigned **the same planetary symbol**. The
collision *was* noticed — recorded in one city's robot-culture file, correctly, months earlier. **But the
cluster's own purpose-built differentiation guide contained zero mentions of symbols, planets, or elements.**
The one file whose entire job was keeping those three cities apart did not know.

> **So, when a differentiation instrument exists, check that it is current:**
> 1. **Has anything been established about these locations since the instrument was last updated?** Symbol
>    assignments, census revisions, founding corrections, and renames are the usual stragglers.
> 2. **A finding recorded in a file nobody consults during differentiation is not doing differentiation work.**
> 3. **Propagation is part of the finding, not a follow-up.** Per Step 9, the row goes in **the same
>    commit** — and so does anything discovered about a *sibling* along the way.

## III.1 What it is

**One file per sibling set**, listing **each completed location's answer per category**, so a new location can
be checked against a single file read instead of re-reading every sibling's full document.

**It exists because the check gets more expensive with every location completed and would otherwise quietly
stop being run** — and because it has already failed once in this project, when two districts were given nearly
the same food custom a day apart.

**Structure:** one section per category most at risk of collision; one row per location; the capability shape
and deficit-address table first, because that is what everything else descends from.

## III.2 How to run it

> ⛔ **STEPS 1–2 ARE TERMINAL-ONLY as of 2026-09-06. Do not run them inside a per-location pass.**
> ✅ **In-run, jump to III.4 and add your own row.**

1. ⏸️ **Before writing a category**, read its row.
2. ⏸️ **If your answer rhymes with any entry, either differentiate it explicitly and inline — in the finding
   itself — or change it.** A prose assurance that "this is different" is not checkable and does not survive the
   next pass; **write the comparison as a table on at least four axes**, and include the **tense** axis — *where
   and when the loss happens* — which is the one most often skipped and the one that most often separates two
   locations that otherwise look identical.
3. **Name the axis the category answers on**, in bold. ⏸️ *Confirming that no completed sibling already uses
   it is TERMINAL-ONLY, like steps 1–2.* **Different content is not differentiation; a different question is.**
4. **After completing a location, add its row in the same commit.**

## III.3 Sibling sets of different sizes

> ⏸️ **TERMINAL-ONLY for a ULM / CST / RWBEM pass** (the 2026-09-06 ruling above). In-run, every location takes
> the III.4 path.

| Set size | How to run it |
|---|---|
| **Large** (20+) | Full table, with all columns present. |
| **Medium** (5–20) | Full table; expect most pairs to eventually be compared directly. |
| **Two** | **Write them together.** Two locations holding one faculty at opposite extremes are each other's exact remedy — and **the remedy is unacceptable**, because taking it means conceding the other's authority over that faculty. Writing them months apart wastes the sharpest contrast available. |
| **One** *(no siblings)* | See below. |

## III.4 The no-sibling case

**The district methodology never faced this. Several location types face it routinely** — a unique station, a
sole polity, a one-off megastructure.

**Four substitutes, in order of strength:**

1. **Its own earlier states.** A location with history is its own sibling set across time: differentiate the
   present frame against the founding frame and the crisis frame. ~~**Usually available, and the strongest.**~~ ⛔ **Not run inside a pass: recorded as deferred to after the pass** (`DR-142` item 2; a pass captures a place at its height, `DR-136` item 6, `DR-137` item 10).
2. **The nearest analogous location at another scale.** A unique station against the cities; a unique polity
   against its own sub-units. ⛔ **Not run inside a pass: it reads another location, so it belongs to the terminal differentiation check** (`DR-142` item 2, as corrected 2026-11-18; `Run_Modes_Warm_and_Cold.md` L127).
3. **Real-world comparables**, with divergence stated explicitly per the source-not-specification rule.
4. **The generator-conflict method** (`02` §5) — which needs no sibling set at all, and is a large part of why
   this methodology runs three generators instead of one.

> **A location with no siblings is at elevated risk of reading like the author's defaults**, because nothing is
> pushing back. **Say so in the pass**, and run substitutes 3 and 4 only; record substitute 1 as deferred to after the pass, and do not run substitute 2 in a pass, since it reads another location (`DR-142` item 2, as corrected 2026-11-18; `Run_Modes_Warm_and_Cold.md` L127; a pass captures a place at its height, `DR-136` item 6, `DR-137` item 10). *(Was: ~~"and run substitute 1 without fail"~~; then, earlier on 2026-11-18, ~~"and run substitutes 2 to 4"~~.)*

---

# Step 6 — Differentiate — ⭐ **WRITE-ONLY, as of 2026-09-06**

> ### 📂 REQUIRED READING FOR THIS STEP
> - **`04_QA_Gates_and_Differentiation.md`, Part III (the differentiation instrument)** — the governing file
>   for this whole step. **III.0** (a differentiation instrument only works if findings actually reach it —
>   the measured case is a symbol collision noticed once and never propagated) · **III.4** (the no-sibling
>   substitutes, ~~run for every location as of the ruling below~~ 3 and 4 run for every location as of the ruling below; 1 is recorded as deferred to after the pass; 2 is not run in a pass, `DR-142` item 2, as corrected 2026-11-18) · **III.2/III.3** (now terminal-only, per the
>   table below — read them to know what is *not* run in-run, not only what is).

> ### ⛔⛔⛔ THE STEP DID NOT DISAPPEAR. **ITS DIRECTION REVERSED.**
> > ### **"During the course of the ULM/CST/RWBEM, just follow the data wherever it leads for one single location on its own terms, and we'll worry about differentiation later."** *(Developer, 2026-09-06.)*
>
> | ⛔ Was | ⭐ Now |
> |---|---|
> | *Read the relevant rows **before** writing each category* | ⛔ **Do not read any other location's row. Ever.** |
> | *Differentiate inline in the finding itself* | ⛔ **Revoked** — there is nothing in-run to differentiate against |
> | *Check the most recently written sibling first* | ⛔⛔ **Revoked** — this was the sharpest form of the forbidden move |
> | *If there is no sibling set, run the substitutes* | ✅ **Run `04` III.4's substitutes 3 and 4 (real-world comparables; the generator-conflict method) for every location, and say in the pass that you did; record substitute 1 (its own earlier states) as deferred to after the pass; do not run substitute 2, which reads another location** (`DR-142` item 2, as corrected 2026-11-18; `Run_Modes_Warm_and_Cold.md` L127; a pass captures a place at its height, `DR-136` item 6, `DR-137` item 10) *(was: ~~"Run `04` III.4's substitutes ALWAYS, for every location"~~)* |
> | — | ✅ ⭐ **ADD THIS LOCATION'S OWN ROW, same commit** *(Step 9.2, unchanged; the city table holds one row per city, the district table one column per district)* |
>
> ⏸️ **The reading half returns at the TERMINAL differentiation check**, run once on the finished corpus.
> **See `00_RUNBOOK.md` → THE LAW OF ONE LOCATION.** ⚠ **District passes are out of scope and keep
> read-before-write.**

> ### ⭐ THE ADDRESSES — added 2026-09-04, because this instrument had none for cities
> | Set | File |
> |---|---|
> | ⭐ **The 37 cities** | **`/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Cross_City_Culture_Differentiation_Table.md`** *(created 2026-09-04 — the cities had NO Part III instrument until then; only the districts did)* |
> | The 13 districts | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Cross_District_Differentiation_Table.md` |
> | ⚠ **NOT this instrument** | `…/Cities/Division_of_Industry/02_Cross_City_Industry_Differentiation_Table.md` — **a different guard for a different pass** *(the necessary-industries bulk run)*. **Both exist; neither replaces the other** |
>
> ⛔ **CELLS HOLD THE AXIS, NEVER THE CONTENT.** *"Different content is not differentiation; a different
> question is."*
> ✅ **Check each cell against the source's own count and slots, not against a reader's reading of them, and keep the narrowest cell.** *(Added 2026-11-04, `M-273`; Mirny Step 6.)*
> ⚠ **The table is FILLED DURING synthesis, not before it.** ***It is not a prerequisite and its emptiness is
> not a gap*** — it contributes nothing to the first city and everything to the thirty-seventh.
>
> ⭐ **Write the row blind:** back the table up, find the insertion point by its first-column label, assert that label and the column count before inserting, and compare with the backup afterward (only the inserted lines may differ). Print headings and column counts only, never another row's first cell. *(Added 2026-11-04, `M-272`; Mirny Step 6.)*

---

## Sheet notes (not source text)

- **Row or column — by the table's own shape** *(`00_RUNBOOK.md` Step 9 item 2, L3012–L3014; `M-298`)*: the CITY
  table (`Cross_City_Culture_Differentiation_Table.md`) holds one ROW per city; the DISTRICT table holds one COLUMN
  per district. Never mix the two words inside one table. `04` Part III, above, says "row" throughout; for the
  district table read "column". *(corrected 2026-11-18: this note said Part III "says 'column' throughout; for a
  city read 'row'", which no longer matches the source; `04` L431–L496.)*
- **"The 37 cities"** in the Step 6 address table above is the source's wording, a lag in the runbook: the
  corpus is 38 cities, as this sheet's header says. The destination file is the same.
