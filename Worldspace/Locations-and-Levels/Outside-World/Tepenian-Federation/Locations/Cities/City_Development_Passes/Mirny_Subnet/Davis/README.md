# Davis — development pass

**Folder opened 2026-09-05. ▶ RUNNING — Steps −1, 0 and 1 COMPLETE. Step 2 is next.** *(2026-09-14, 14:00.)*

> ## ⏸️ WHERE THIS PASS STOPPED, AND WHY — read before resuming
> **Step 2 (BUILD THE SPINE) was dispatched and its three `T8` readers were killed mid-read by a session rate
> limit. ⛔ ZERO reader output was written — verified against disk, not assumed from the notification.**
> **Nothing is lost except the in-flight reads.** ⛔ **It was NOT re-dispatched, deliberately:** the re-run
> would have landed inside the operating-hours wrap-up window *(14:00–14:59)*, and the law forbids opening a
> new step there — ***least of all the step the runbook calls "the step everything else hangs on."***
>
> ### ✅ TO RESUME — everything needed is already prepared
> | | |
> |---|---|
> | **Reader file list** | `…/scratchpad/davis_step2_required_files.txt` — **10 entries, verified** ⚠ *scratchpad is session-local; rebuild from `R-12` below if gone* |
> | ⛔ **Do NOT use the Pre-Trip's Step 2 block** | It sends Step 2 to the **Phase-2** row-set. **Step 2 is PHASE 1.** See **`R-12`** |
> | **Two bounded schema extractions**, not reads | `Division_of_Industry/16` Half B *(Davis's row + which framing it encodes)* · `Extent_and_Density_Per_City.md` *(does a Davis extent figure exist at all)*. **Both are organized by city and carry other cities' conclusions — closed until Step 6** |
> | ⚠ **Expect item 6 to be BLOCKED** | *Divide population by extent* — the extent band is `UNDETERMINED`. **"It cannot run as specified" is the correct result. Do not invent a denominator** |
> | ⛔ **Time-critical, unresolved** | The **"chosen / selected"** ambiguity — the ratified spine wording may bake **election** in. **Resolve before the spine is written, not after** |

> ## ⭐ THE PROTOCOL, IN ONE LINE
> **One piece at a time · displayed AND written in the same turn · developer clarifies · the clarified result
> feeds the next piece.** ⛔ **THERE IS NO TIME LIMIT.** *Full statement at the top of any tracker.*

> ⚠ **This README previously read "Empty by design" with five files present, and predicted a layout this pass
> has already diverged from.** ⭐ **Rewritten 2026-09-13 to LIST what the folder contains rather than predict
> it** — the same defect `Gate 0`'s outward check fired on in another pass's Step 10. *Implementing a finding
> rather than re-recording it.*

---

## ⏸️⏸️ ON COMPLETION OF THIS PASS — QUEUED WORK, DO NOT START EARLY

> ### ⛔ **SHIRAYUKI TARGETED REVIEW**
> **Developer instruction, 2026-09-13:** *"After we've completed Davis, then go back and do the targeted review
> on Shirayuki — but that's a task for later, not now."*
>
> **TRIGGER: this pass's `10_Readiness_Check.md` passes.** ⛔ **Not before.**
> **Full brief:** `…/Universal_Location_Methodology/MASTER_Process_Tracker.md` §"QUEUED — SHIRAYUKI TARGETED
> REVIEW".
>
> ⚠ **A REVIEW, not a re-run.** That pass measures well structurally — `3` gates fired, `16` raw output blocks,
> all six Review Panel dispositions used with **`unmet` 7 and `declined` 7, more than `accepted`.** **What it
> lacks is a Step −1 input contract**, and this pass's Step −1 found **11 contaminated lines inside a range
> that looked clean.** Four checks: reconstruct Step −1 · re-declare the band under `DR-4` ·
> adjudicate `06_Differentiation.md` against the write-only ruling · tracker accuracy.

---

## Files in this folder NOW

| File | Piece | |
|---|---|---|
| `00.0_Pre-Trip_Inspection.md` | Coordinates, run mode, per-step address book, laws, exclusions | ✅ |
| `00.1a_RULING_Vision_Notes_and_Specs_L135-181.md` | The admissibility ruling — vision notes struck; `L143` admitted | ✅ |
| `00.1b_T8_Rounds_Step_MINUS-1.md` | `T8` Rounds 1–3, raw. **The evidence `00.1` rests on** | ✅ |
| `00.1_Step_MINUS-1_Input_Contract.md` | **ULM Step −1** — written on verified unanimous consensus | ✅ |
| `00.1_SUPERSEDED_single-reader_2026-09-11.md` | ⚠ The earlier single-reader run. **Procedurally invalid, substantively sound** — kept as the only direct measurement of what `T8` adds | 📎 |
| **`00_Frame.md`** | **ULM Step 0** — type · bands · status · frame · parent · run mode. **`Settlement`, zero modifiers · Band 5 (Census I, `DR-4`) · extent `UNDETERMINED` · `LIVING` · `EXCEPTIONAL`.** Written on 3-round unanimous consensus | ✅ |
| **`00b_T8_Rounds_Step_0.md`** | `T8` Rounds 1–3 for Step 0, raw. **The evidence `00_Frame.md` rests on** — incl. the two verifier defects that produced a FALSE failure | ✅ |

## Files still to appear

| File | Piece |
|---|---|
| `01_Inherited.md` | ULM Step 1 — what canon already says, and its epistemic status ▶ **IN PROGRESS** |
| `02_Spine.md` | ULM Step 2 — the capability profile, ≥3 generators |
| `03_Research.md` | ULM Step 3 — targeted at what Step 2 named ⚠ *search strings go in the city's Research Log* |
| `04_Phase_00…10_*.md` | ULM Step 4 — one file per phase |
| `05_Reconciliation.md` | ULM Step 5 — and the CLOSE pass |
| ⛔ `06_Differentiation.md` | **WILL NOT EXIST, correctly** — Step 6 is **WRITE-ONLY** as of 2026-09-06; the column goes into the shared table, not into a file here |
| `07_*` | ULM Step 7 — the 17 gates |
| `08_Review_Panel.md` | ULM Step 8 — six dispositions |
| `09_Record.md` · `09.5_Log.md` | ULM Step 9 — ⚠ **the recording law: snags, dead ends, killed findings, self-corrections** |
| `10_Readiness_Check.md` | ULM Step 10 — ⚠ **verify, do not assert** |
| `CST_*` · `RWBEM_*` | Cultural Synthesis · Real-World Basis Extrapolation |

⭐ **Flat, not foldered by process** — *developer instruction: "organize by subnet/city/city-files, instead of
by process, since all the answers will be related to each other anyway."*

---

## This city's sources — **inputs, not outputs. Do not overwrite.**

⚠ **Absolute paths** — relative ones misroute a reader who opens this file from anywhere else.

| | |
|---|---|
| **Spec** | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Davis.md` ⛔ **RANGED — see `00.1` §4** |
| **Census** | `…/Cities/Official_Population_Census.md` — **Census I governs** *(`DR-4`)* |
| ⏸️ **Local culture** | `…/Cities/Local_Cultures/Mirny_Subnet/Davis.md` — **READ LAST, at Step 5, as a CHECK** |
| ⏸️ **Local robot culture** | `…/Cities/Local_Robot_Culture/Mirny_Subnet/Davis.md` — **READ LAST, at Step 5, as a CHECK** |
| ⛔ ~~**Vision notes**~~ | ~~`…/Cities/City_Vision_Notes/Davis.md`~~ — **STRUCK corpus-wide, developer ruling 2026-09-13** *(`00.1a` §4.1)*. ⭐ Nothing lost: `Specs/Davis.md` **L143** is a strict superset, on better provenance |
| **Research log** | `…/Cities/Research_Logs/Davis_Research_Log.md` ⚠ **does not exist yet — Step 3 creates it** |
| **Picks to mine** | `…/Cities/Inspirational-Influences.md` ⚠ **not an enumerated ratified root → DEMOTED** |
| ⛔ **Megasheets** | **WITHHELD from every run** — *due to be rewritten* |

📎 **Progress:** `MASTER_Process_Tracker.md` · `ULM_Run_Progress.md` · `CST_Progress.md` · `RWBEM_Progress.md`
📎 **Binding rulings:** `DEVELOPER_RULINGS_LOG.md` · **Docket:** `../../DOCKET.md`
*(all under `…/Universal_Location_Methodology/` except the docket)*
