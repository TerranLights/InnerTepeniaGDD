# AUDIT AGENDA — 2026-09-16, after 15:00

**Two tasks, both set by the developer during the Davis run. ⛔ Neither starts before 15:00.**

> ### ⚠⚠ ORDERING CONSTRAINT — read this first
> **Task A contaminates the orchestrator for Davis.** `Zhongshan_Opus`, `Shirayuki` and `Zhongshan_Sonnet` are
> all **Mirny-subnet siblings of Davis**, and Davis's Step 4 is unfinished *(Phases 6–10 outstanding)*.
> ⇒ **After Task A, Davis's remaining phases may NOT be written by the orchestrator directly** — they go to
> **T8 dispatch, three isolated readers per phase, orchestrator synthesising only.** **ONE LOCATION is held at
> the reader layer.** *(Developer ruling 2026-09-16; recorded in `…/Davis/README.md`.)*
> ⭐ **Anything Davis-side written BEFORE 15:00 is clean by construction and needs no dispatch.**

---

## TASK A — audit the two completed sibling passes

| Target | Scope |
|---|---|
| **`Zhongshan_Opus`** | **24 files — a COMPLETE pass**, Steps −1 → 10. ⚠ **Also the project's official quality bar**, so a defect here is likely a defect in the instrument, not in one city |
| **`Shirayuki`** | **23 files — a COMPLETE pass**, Steps 0 → 10, plus an enrichment review and an input audit |
| **`Zhongshan_Sonnet`** | **9 files — held at Phase 3** |

## TASK B — double-check the quick-reference sheets for **Mirny** and **Casey**

| Target | Scope |
|---|---|
| **`…/Mirny/Datasheets/`** | **19 files** — built this session |
| **`…/Casey/Datasheets/`** | **19 files** — built this session |
| ⚠ **`Corpus_Reference_Sheets/*_Quick_Reference.md`** | **The Tier U sheets** — include them. **`Falkland_Treaty_Quick_Reference.md` already proved to carry a corpus-wide error** *(its article transcription was correct and its SUMMARY elided the residual clause)*, **and every city reads these** |
| ⭐⭐ **NEW — `Division_of_Industry_Reliability_Quick_Reference.md`** | **Created 2026-09-16, single-reader, NOT T8-verified.** ⛔ **T8 it.** ⚠ **It was corrected once already within an hour of being written** *(its §2 first repeated `README`'s own over-broad sentence that `DRQ-09` blocks every export figure; §2a now states the precise failing term)*. **Re-check that the ✅-citable column is right — an over-blocking gate costs real findings** |

> ### ⭐⭐ TASK B ADDENDUM — **the carve-out sweep, added 2026-09-16**
> **Grep every city's datasheets for food/industry figures and confirm each one is on the ✅ side of the gate.**
> **At the time the gate was written, ZERO of 57 datasheets across three cities carried the carve-out.**
> ✅ **Now wired into:** all three `Phase_7.md` and all three `Phase_4.md`.
> ⛔ **Still to check:** every OTHER phase's datasheet in all three cities, and `Zhongshan_Opus` / `Shirayuki` /
> `Zhongshan_Sonnet`'s completed passes — **their Phase 4 and Phase 7 predate the gate entirely.**

> ### ⭐⭐ WHY TASK B IS LIKELY TO FIND THINGS — the strongest single reason
> **Mirny's and Casey's datasheets were built from the Field Guide's CATEGORY LIST, not from each phase's own
> MUST-OPEN list in `03_The_Phase_Spine.md`.** **Davis's were built the same way — and Davis's proved to have
> real omissions THREE separate times in one day:**
>
> | Phase | What the datasheet missed |
> |---|---|
> | **3** | **`Davis_Geosciences_Research/` entirely** — which turned out to be the phase's richest input, *and* its two full writeups live one directory above the folder |
> | **4** | **`National_Economy_and_Currency.md`** marked ⏸️ *"NOT YET EXTRACTED"* · **`11_Caloric_Rebuild_and_Livestock_Tier.md` absent entirely** |
> | **5** | **`Geothermal_Heating.md` absent entirely** *(a 198-line zero that turned out load-bearing)* · **`Ports.md` present only as "file exists"**, without Davis's actual row or tier |
>
> ⇒ ***The same method produced Mirny's and Casey's sheets. Expect the same class of omission.***

---

## WHAT TO CHECK FOR — the same five shapes in both tasks

| # | Shape | The test |
|--:|---|---|
| **1** | ⛔⛔ **Undeveloped canon treated as characterizing absence** | ***Does a source AFFIRM this absence, or has no source addressed it yet?*** **Only the first may be characterized.** ⚠ *Developer's words: "those details 'don't exist' because we haven't figured them out yet."* **Watch for future-tense authorial notes** — *"once X exists," "a natural first-time…," "TBD"* — **being read as settled facts** |
| **2** | ⛔ **A summary trusted instead of its source** | **Twice measured 2026-09-16.** *(a)* A treaty clause's **fourth, residual ground read past** — *"or otherwise established their life among the robot population."* *(b)* A research checklist's one-liner trusted over the extraction it pointed at, **which had TESTED AND WITHDRAWN the very mechanism the one-liner named.** ⭐ **Both times the narrow reading was the MORE VIVID sentence** |
| **3** | ⛔ **Unsettled design asserted as fact** | **The energy-backed currency.** ⛔ **Nothing about what the money is backed by is settled at any stage** — `DR-3`, hard-gated. **Check every economic claim in both passes.** ⚠⚠ **NEW SITE, found 2026-09-16: `Division_of_Industry/10_Validation_Findings_2026-09-01.md` L263 asserts *"a nation whose currency is denominated in guaranteed grid capacity"* — the killed claim, live in a file stamped RELIABLE.** ⇒ ***The claim is loose in the corpus beyond `National_Economy_and_Currency.md`. Sweep for it, do not assume containment*** |
| **3b** | ⛔ **GPS trap — site namesake used characterologically** | ⚠ **NEW, 2026-09-16.** **`16_Per_City_Three_Tier_Run.md`'s per-city Notes blocks read real-world site NAMESAKES as character** *(e.g. "a navigator and enabler, not a flag-planter")*. ⛔ **A real site's builder, lineage and namesake are a COORDINATE ONLY.** **Check whether any completed pass absorbed one** |
| **4** | ⚠ **A datasheet row reporting a SOURCE'S EXISTENCE instead of the CITY'S ROW in it** | *"`Ports.md` present"* is not *"here is this city's entry, and its tier is `CONSTRUCTED` — rebuilt every year, paid forever."* ⭐ **The second is the one that does work** |
| **5** | ⚠ **MUST-OPEN coverage** | **Walk each phase's MUST-OPEN list from `03_The_Phase_Spine.md` against what the datasheet actually lists.** ⛔ **A folder's data is not the same as the files inside the folder — chase its index's pointers** |

---

## ALREADY DONE — do not redo

- ✅ **The Falkland Art. II.2.3 correction** *(prior association with the robot population, NOT a relationship
  requirement)* **has already been propagated** to the Tier U sheet and to **Davis's, Mirny's and Casey's**
  `Phase_2.md` datasheets.
- ✅ **Davis's own full pass was audited for shape 1 on 2026-09-16** — Steps −1 → Phase 5 plus all datasheets.
  **One real violation found** *(Phase 5's headline, withdrawn)*, **one borderline line tightened** *(§5a)*.
  **Everything else traced to explicit source text, arithmetic necessity, or was already hedged.**

## WHERE FINDINGS GO

- **Corpus-wide defects** → `Mechanical_Extraction_Field_Guide.md` *(shapes 1 and 2 are already recorded there)*.
- **Methodology defects** → `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`, **numbered `M-n` continuously**.
- ⛔ **Not into a tracker.** *`M-109`: a tracker entry is one line plus a pointer; more than ~3 lines is the
  wrong file.*
