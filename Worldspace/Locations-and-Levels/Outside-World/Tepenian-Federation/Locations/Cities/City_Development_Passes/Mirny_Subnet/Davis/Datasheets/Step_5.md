# Davis — Datasheet · Step 5 (Reconciliation)

> ⛔⛔⛔ **SUPERSEDED, 2026-09-21 — DAVIS'S PASS HAS ACTUALLY RUN.** This datasheet was pre-staged input for a
> pass that had not started; Davis's real Step 5 output lives at `05_Reconciliation.md` in this city's own pass
> folder. **Do not consult this file for Davis's reconciliation work.** Retained below as a record only, with
> one line removed that overstepped copy-paste scope: a prediction about how future cities' own passes would
> fare, which is not something any source states — see `Mechanical_Extraction_Field_Guide.md` if that class of
> finding needs recording.

> ## ⛔⛔⛔ A GATE STANDS BEFORE THIS STEP — **run it FIRST.** *(added 2026-09-16)*
> **`00_RUNBOOK.md` L2682 — the `M-208` CLOSE-OUT CHECK: *"run once, after Phase 10, before moving to Step
> 5."*** ***"A pass may not proceed to Step 5 with a `⛔ NEVER CITED` row that nobody has looked at and
> explained."***
>
> ```bash
> PASS_DIR="City_Development_Passes/<Subnet>/<City>"
> for g in G1 G2 G3 G4 G5 G6 G7 G8; do
>   hits=$(grep -l "Generators used:.*$g\b" "$PASS_DIR"/04_Phase_*.md 2>/dev/null | wc -l)
>   printf '%-4s %s\n' "$g" "$([ "$hits" -gt 0 ] && echo "OK — cited in $hits phase(s)" || echo "⛔ NEVER CITED")"
> done
> ```
>
> ⚠⚠ **DAVIS FAILED THIS 8/8 ON FIRST RUN** — **no phase file carried a `Generators used:` line at all**, and
> Step 4 had already been declared complete. ***A receipting defect, not a coverage one.***
> ✅ **RESOLVED 2026-09-16:** receipts added to Phases 6–10; **7 of 8 now `OK`**; **`G6`'s legitimate-null
> disposition written once into `09.5_Log.md` §1.3**, so the check passes clean on re-run.

> ⛔⛔ **OTHERWISE DELIBERATELY EMPTY — NOT AN OVERSIGHT.** The only slot in the full 22-file inventory that is
> fully blocked, not merely undone.

## Why nothing is staged here

`Local_Cultures/Mirny_Subnet/Davis.md` and `Local_Robot_Culture/Mirny_Subnet/Davis.md` are **read-last, as a
CHECK** — per `00.0_Pre-Trip_Inspection.md` §B: *"In a warm run nothing enforces it mechanically — this file is
the enforcement."* Pre-staging their content, however mechanical the transcription would be, defeats the one
thing keeping them from contaminating every earlier phase. This is the Field Guide's own sequencing exclusion,
applied without exception.

| Category | Status |
|---|---|
| `Local_Cultures/Mirny_Subnet/Davis.md` | Confirmed to EXIST (filename only, per `00.0` §F) — ⛔ never opened before Step 5 |
| `Local_Robot_Culture/Mirny_Subnet/Davis.md` | Confirmed to EXIST (filename only, per `00.0` §F) — ⛔ never opened before Step 5 |
| The deferred own-eras three-way set, the Zodiac Lens's person-shaped amendment, the strongest-finding check | All genuinely require prior phases' content and this step's own timing — not mechanical, not pre-stageable |

**When Step 5 actually opens:** read both files for the first time as a check against everything already
written, per `00_RUNBOOK.md` §"Step 5" §5.3/§6.1/§6.3.
