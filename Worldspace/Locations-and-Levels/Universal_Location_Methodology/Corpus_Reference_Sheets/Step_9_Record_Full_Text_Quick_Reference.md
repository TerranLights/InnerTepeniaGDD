# Step 9 (Record) — Full Text Quick Reference

> ⭐ **Tier U — corpus-wide, identical for every city.** Copied word for word from `00_RUNBOOK.md` §"Step 9" and
> §9.5, **L3006–L3076** (Step 9 heading at L3006, §9.5 at L3039, Step 10 begins at L3080), as of 2026-11-18. **Nothing below is city-specific.**
> *(Re-copied 2026-11-18: the earlier version, re-read 2026-10-30, cited L2986–L3056 with §9.5 at L3017, was a paraphrase under a "Full Text" title, and lacked the three 2026-11-04 additions, `M-287` in item 3, `M-314`/OBS-11 in item 5 and `M-307`/OBS-3 under killed findings. The earlier version before that cited L2941–2999 and listed four actions.)*

---

# Step 9 — Record

1. Append the **QA block** and the **Review Panel block**.
2. **Confirm the location's own ENTRY in its differentiation set is written and in the same commit.**
   ⭐ *(Reconciled 2026-10-21, Mirny handoff decision 13, group C; `M-298`.)* **The entry is WRITTEN at Step 6, on
   the UNANIMOUS verdict, as the Pre-Trip's Step 6 row says; Step 9 CONFIRMS it is present and commits it in the
   same commit as the Step 9 record.** *Name it by the table's own shape: the CITY table holds one ROW per city
   (`Cross_City_Culture_Differentiation_Table.md`); the DISTRICT table holds one COLUMN per district. Never mix the
   two words inside one table. A city pass writes only its own row and never reads another's.* *(Correction, same
   day: the first wording of this item called the city's entry a "column"; the city table's rows are cities.)* **Cities → `…/Cities/Cross_City_Culture_Differentiation_Table.md`** *(full path in Step 6)*.
   **Districts → `Cross_District_Differentiation_Table.md`.** ***One AXIS per cell, never the content.***
   ⚠ **And if this pass noticed anything about ANOTHER city, record that here too** — `04` III.0:
   ***propagation is part of the finding, not a follow-up.*** *(A symbol collision was once noticed correctly,
   filed in one city's own culture file, and never reached the guide whose entire job was catching it.)*
3. Update whatever tracker claims completion — **per Gate 0, list what the file actually contains, not a summary
   claim.** ⭐ *(Added 2026-10-21, `M-287`.)* **A city's tracker row carries each phase's status, PROPOSED or
   confirmed, in the same one line, so an overclaim cannot hide behind "Step 4 done."**
   > ### ⛔ **BUT PUT THE FINDING IN THE OBSERVATIONS LOG, NOT IN THE TRACKER.** *(M-109.)*
   > **Gate 0's concern is OVERCLAIMING COMPLETION. It is not a license to write substance into a queue.**
   > ***A tracker entry is: what remains to be done, one line, plus a pointer to where the detail lives.***
   > **The finding itself goes to `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` and nowhere else.**
   > **If you have written more than ~3 lines into a tracker, you are writing in the wrong file.**
   > **Before the record is committed, check the tracker's lines for this location: one line plus a pointer each, no finding in them.** *(Added 2026-11-04, `M-287`.)*
4. **If this pass changed the methodology, update these files in the same commit**, and record **what was
   learned and on which location.** A methodology change that does not update the runbook has not been made —
   the next pass will follow the runbook, not the commit message.
5. ⭐ **Discharge every deferral to "the pass's close."** *(Added 2026-10-21, `M-291`; Mirny's Phase 2 snag 1 and
   Phase 3 snag 12 deferred a sweep of line-anchored citations to the close, and no step listed it.)* **Run the
   stale-anchor and span sweep over the pass's own files: every citation by line number or span is re-checked
   against the file as it now stands, because edits shift lines.** Record what moved. This step discharges any
   phase's "sweep at the close" deferral; a deferral that no step names is a hole.
   **A deferral that names any step, not only the close, reaches that step's brief as a line to discharge.** That step may close it as "not applicable" only by stating why the deferred check no longer applies. *(Added 2026-11-04, `M-314`/OBS-11; Mirny Phase 6 to Step 8.)*

## 9.5 — THE RECORDING LAW: log everything that happened, not everything that worked

**Developer instruction, 2026-08-30 (Run 3, Zhongshan), stated twice in one session. Binding on every pass, not
only on test runs.** The shared log is
**`Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`**, which carries the full statement.

> **Record every finding — and "finding" does not mean "successful technique."** It means, in the developer's
> own enumeration: **ways of achieving results, snags, problems, unintended blockages, etc., etc., etc.**

**What that covers in practice:**

- **Techniques that worked** — and *why* they worked, not merely that they did.
- **Snags** — anything that slowed the pass, however trivial-seeming.
- **Problems and unintended blockages** — a step that could not be run, and **what stopped it.**
- **Contradictions between two instructions inside this methodology.** *(Run 3 found three.)*
- **Dead ends**, and the exact point at which each died.
- **Killed findings** — an attractive result destroyed by its own evidence. ***The most valuable entries in the
  file.*** Run 1's best moment was a finding killed by its own arithmetic; Run 3's was the same.
  - **Class each killed finding as *killed by evidence* or *killed for want of an admitted line*; only the second may be revived by a later ruling or source.** A kill stays in the record. When a ruling later settles it, add a status pointer beside the record, never a rewrite. *(Added 2026-11-04, `M-307`/OBS-3; Mirny repass.)*
- **Self-corrections** — written as *what you believed · why it was wrong · what changed it.*
- **Environmental and tooling obstacles** — a hook, a stale index, a missing file, a `CLAUDE.md` rule that
  conflicts with a rule in here.
- **Anything merely unclear**, even where the guess turned out right.

**Three procedural rules, each already violated at least once:**

1. **Write it when it happens.** Precision decays; a snag logged hours later has lost the file, the wording, and
   the reason it mattered.
2. **Log the failure even when you routed around it.** **Solving a problem privately is how a methodology stays
   broken.**
3. **Never compress a negative result into a positive one.** *"Checked the census, all fine"* destroys what
   *"the parse read the wrong column and returned plausible numbers; only a printed row caught it"* preserves.

**Number entries `M-n` continuously across all runs; never restart per run** — recurrence across runs is much
stronger evidence than a single sighting, and only continuous numbering makes it visible.

> **The location is the whetstone; the methodology is the deliverable.** **A pass that produces a beautiful
> location and a thin observations log has failed at the thing it was for.**

---

## Sheet note (not runbook text) — the one genuinely dynamic item, not a datasheet candidate, a live counter instead

The "next `M-` number" lookup changes every time a session records a finding — a static datasheet entry would
be stale by the time it's read. Recommendation: a single live-maintained counter file, refreshed on each new
finding, not a per-city artifact. Not built here.
