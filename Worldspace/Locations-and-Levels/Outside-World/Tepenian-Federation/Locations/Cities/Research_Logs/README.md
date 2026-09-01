# Research Logs — one per location

**Standing convention, established 2026-08-30 at the developer's direction, during the Zhongshan Run 3 cold
pass.**

> **"When doing web research for building and developing locations, have a separate, distinct, dedicated file
> for each particular location that keeps a record of exactly what it was that was researched in order to find
> some-such-and-such-whatever particular piece(s) of information. That way, any time it ever becomes necessary,
> future iterations can refer back to things and possibly do further, deeper investigative research, if such a
> thing turns out to be necessary."**

---

## The problem this solves

**A finished culture pass shows its conclusions and hides its evidence.** A finding says *"the city smells
different at its two ends"* and gives no way to discover that this came from a line about the Dålk glacier's
calving surges in a geomorphology paper. **So the next session cannot:**

- **re-check a claim** against what the source actually said;
- **go deeper on a source that clearly had more in it**;
- **tell the difference between a fact that was researched and one that was assumed**;
- **avoid re-running a search that has already been run**, or re-mining a pick already mined;
- **find the threads that were deliberately left hanging** — which are usually the most valuable material
  available, and which vanish completely once a pass is written up.

**A research log is the provenance layer.** The pass is what was concluded; this is what was actually looked at.

## What goes in one

**One file per location**, named `[Location]_Research_Log.md`, appended to across sessions — **never rewritten.**

Per research session, record:

1. **The date, and the pass/context** it was run for — and **at what point in the procedure**, since
   `00_RUNBOOK.md` Step 3 requires research to run *after* the capability profile names the deficit.
2. **The deficit or question being researched against.** Research with no target produces interesting material
   with nowhere to attach.
3. **⭐ The exact search strings used.** Verbatim. This is the single most reusable thing in the file — it lets a
   later session reproduce, vary, or deepen the search instead of guessing at it.
4. **The sources returned and actually used**, with links.
5. **A fact-by-fact table: what came back → which finding it became.** Including the facts that became nothing.
6. **What was WITHHELD** *(real, usable, deliberately held back — say what it was held for)* and what was
   **OMITTED** *(genuinely did not fit — say why)*. `04` Gate 7 requires this distinction anyway; recording it
   here makes it durable.
7. **Divergences from source** — where the location deliberately does *not* follow its inspiration. Per the
   standing rule, **divergence stated is stronger than resemblance implied.**
8. **⭐ Open threads.** Sources surfaced but not read; questions not chased; picks not exhausted. **With what
   each might yield.** This is the section future sessions will use most.

## Rules

- **Append, never overwrite.** A superseded finding's research is still evidence about how the finding was
  reached, and Gate 0 exists because status claims drift.
- **Record the search string even when the search failed.** A query that returned nothing useful saves the next
  session from running it.
- **Do not put conclusions here.** This file holds *what was looked at*. The pass holds *what was concluded*.
  Keeping them separate is also what keeps this file admissible as input under `05` §6.1 — **a research log is
  attributes, not conclusions, and a later cold run may read it.**
- **Non-city locations get one too** — districts, subnets, structures, corridors, orbital locations. Store it
  with that location's own material; the convention is universal, only the folder changes.

## Index

| Location | Log | Last session |
|---|---|---|
| **Zhongshan** | `Zhongshan_Research_Log.md` | 2026-08-30 — Run 3 cold pass. 6 queries; 3 picks + physical site + 2 forcing-function comparanda. **7 open threads recorded**, incl. the unread ASMA 6 management plan |
| **Janbogo** | `Janbogo_Research_Log.md` | 2026-08-31 — Run 9 cold pass. 2 search queries + 3 fetches (1 failed, HTTP 402); Jang Bogo Station's real staffing/scale and its historical namesake. **5 open threads recorded**, incl. an unfused downfall-by-overreach parallel deliberately deferred to a later filter test |
