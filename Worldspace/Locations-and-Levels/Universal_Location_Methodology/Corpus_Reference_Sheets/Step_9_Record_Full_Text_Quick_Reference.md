# Step 9 (Record) — Full Text Quick Reference

> ⭐ **Tier U — corpus-wide, identical for every city.** Extracted from `00_RUNBOOK.md` §"Step 9" and
> §9.5 (L2986–L3056; §9.5 at L3017), re-read against the live text 2026-10-30 (the earlier version cited L2941–2999 and listed four actions). **Nothing below is city-specific.**

## The five required actions

1. **Append the QA block and the Review Panel block.**
2. **Confirm the location's own ENTRY in its differentiation set is written and in the same commit.** *(Reconciled
   2026-10-21, `M-298`.)* The entry is WRITTEN at Step 6, on the UNANIMOUS verdict, as the Pre-Trip's Step 6 row says;
   Step 9 CONFIRMS it is present and commits it in the same commit as the Step 9 record. Name it by the table's own
   shape: the CITY table holds one ROW per city (`Cross_City_Culture_Differentiation_Table.md`); the DISTRICT table
   holds one COLUMN per district (`Cross_District_Differentiation_Table.md`). Never mix the two words inside one
   table. A city pass writes only its own row and never reads another's. One AXIS per cell, never the content.
   Cities → the destination table named in `Differentiation_Instrument_Quick_Reference.md`. ⚠ **And if this pass noticed anything about
   ANOTHER city, record that here too** — propagation is part of the finding, not a follow-up. (A symbol
   collision was once noticed correctly, filed in one city's own culture file, and never reached the guide
   whose entire job was catching it.)
3. **Update whatever tracker claims completion** — per Gate 0, list what the file actually contains, not a
   summary claim. *(Added 2026-10-21, `M-287`.)* A city's tracker row carries each phase's status, PROPOSED or
   confirmed, in the same one line, so an overclaim cannot hide behind "Step 4 done." ⛔ **But put the finding in the OBSERVATIONS LOG, not in the tracker** (`M-109`). Gate 0's
   concern is overclaiming completion, not a license to write substance into a queue. A tracker entry is: what
   remains to be done, one line, plus a pointer to where the detail lives. The finding itself goes to
   `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` and nowhere else. If you've written more than ~3 lines
   into a tracker, you're writing in the wrong file.
4. **If this pass changed the methodology, update those files in the same commit**, and record what was
   learned and on which location. A methodology change that does not update the runbook has not been made — the
   next pass will follow the runbook, not the commit message.
5. **Discharge every deferral to "the pass's close."** *(Added 2026-10-21, `M-291`; Mirny's Phase 2 snag 1 and
   Phase 3 snag 12 deferred a sweep of line-anchored citations to the close, and no step listed it.)* Run the
   stale-anchor and span sweep over the pass's own files: every citation by line number or span is re-checked
   against the file as it now stands, because edits shift lines. Record what moved. This step discharges any
   phase's "sweep at the close" deferral; a deferral that no step names is a hole.

## §9.5 — the recording law: log everything that happened, not everything that worked

**Developer instruction, 2026-08-30 (Run 3, Zhongshan), stated twice in one session. Binding on every pass, not only test runs.**
Shared log: `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`.

Record every finding — "finding" does not mean "successful technique." It means: ways of achieving results,
snags, problems, unintended blockages, etc.

**What that covers in practice:**
- Techniques that worked — and *why*, not merely that they did.
- Snags — anything that slowed the pass, however trivial-seeming.
- Problems and unintended blockages — a step that could not be run, and what stopped it.
- Contradictions between two instructions inside the methodology. (Run 3 found three.)
- Dead ends, and the exact point at which each died.
- Killed findings — an attractive result destroyed by its own evidence. **The most valuable entries in the
  file.** Run 1's best moment was a finding killed by its own arithmetic; Run 3's was the same.
- Self-corrections — written as *what you believed · why it was wrong · what changed it*.
- Environmental and tooling obstacles — a hook, a stale index, a missing file, a conflicting rule.
- Anything merely unclear, even where the guess turned out right.

**Three procedural rules, each already violated at least once:**
1. **Write it when it happens.** Precision decays; a snag logged hours later has lost the file, the wording,
   and the reason it mattered.
2. **Log the failure even when you routed around it.** Solving a problem privately is how a methodology stays
   broken.
3. **Never compress a negative result into a positive one.** *"Checked the census, all fine"* destroys what
   *"the parse read the wrong column and returned plausible numbers; only a printed row caught it"* preserves.

**Numbering:** `M-n` continuous across ALL runs, never restarted per run — recurrence across runs is much
stronger evidence than a single sighting, and only continuous numbering makes it visible.

> **The location is the whetstone; the methodology is the deliverable.** A pass that produces a beautiful
> location and a thin observations log has failed at the thing it was for.

## ⛔ The one genuinely dynamic item — not a datasheet candidate, a live counter instead

The "next `M-` number" lookup changes every time a session records a finding — a static datasheet entry would
be stale by the time it's read. Recommendation: a single live-maintained counter file, refreshed on each new
finding, not a per-city artifact. Not built here.
