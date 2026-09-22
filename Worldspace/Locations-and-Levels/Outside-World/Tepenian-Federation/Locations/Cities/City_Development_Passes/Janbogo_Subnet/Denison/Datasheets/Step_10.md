# Denison — Datasheet · Step 10 (The Readiness Check)

> **Tier U — `06_Worked_Example_Provenance.md`'s stated content.** The memory index and
> `00_RUNBOOK.md` §Step 10 change too often / require too much judgment to pre-stage.

Citation: `Corpus_Reference_Sheets/Step_10_Readiness_Check_Full_Text_Quick_Reference.md`, in full.

**Governing principle: VERIFY, DO NOT ASSERT.** Run before declaring a pass complete or before
handing off.

| Section | What it checks |
|---|---|
| 10.1 Contamination surface | Scan auto-loaded memory, required reading, and the file tree for the NEXT location's name — not this one's |
| 10.2 Path and structure integrity | Every path named in the handoff exists; the next run's output folder does not already exist |
| 10.3 Record integrity | Gate 0 outward: does every tracker's completion claim match what the files actually contain? |

**Denison-specific check to run when this step fires:** confirm `06_Worked_Example_Provenance.md`
does not carry a Denison worked example — checked once for this datasheet build, **zero hits**.

**Not mechanical / not included here:** any actual readiness-check run against Denison's own
completed pass — none of this exists until Denison's own Step 10 actually runs.
