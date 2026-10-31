# Step 10 (The Readiness Check) — Full Text Quick Reference

> ⭐ **Tier U — corpus-wide, identical for every city.** Extracted from `00_RUNBOOK.md` §"Step 10"
> (L3057–L3152), re-read against the live text 2026-10-30 (the earlier version cited L3001–3089 and carried the superseded item 7). **Nothing below is city-specific** — the actual scans (item 1's memory/
> reading/filename checks) are run against the NEXT city, not the one whose datasheet cites this sheet.

**Standing step, added 2026-08-30 at the developer's direction. Run before declaring a pass complete and before
handing off to another session.**

> **The governing principle: VERIFY, DO NOT ASSERT.** *"Everything is ready"* is a claim, and it requires
> evidence like any other. The check exists because a handoff feels finished long before it is, and because the
> person best placed to declare readiness is the one who can no longer see what they have absorbed. On its
> first use it caught the single largest hole in the anti-contamination protocol — it is not a formality.

## 10.1 — Contamination surface (run against the NEXT pass's subject location, not this one's)

1. **⚠ Scan auto-loaded memory for the subject location** *(the check that found M-21)*. Every hit must be
   attribute-only (founding, dates, names, census, corrections, open questions) or carry a contamination
   banner. An entry stating the place's character, temperament, personality triple, or a signature phrase is a
   live vector, because memory is *pushed* into a session rather than pulled by it. Fix the entry or band it.
   > There are at least three push vectors, not one: memory, **the required reading itself** (1a), and
   > **filenames** (1b).

   **1a. Scan the REQUIRED READING for the next subject's name** — `00`–`06`, `README`, and everything in
   `Disciplines/` (the ULM's own copies — originals withheld). Return line numbers, band or neutralize every
   hit, manifest it in `06`. `CLAUDE.md` mandates these files be read in full, so a worked example naming the
   next subject is a guaranteed leak with a mandatory delivery mechanism. This has now failed three times —
   M-82 (Sanay), and twice more on Run 12 — which is why Step −2 has a reader scan them rather than trusting `06`.

   **1b. Sanitize the file tree.** Check whether any file or folder the next run must navigate is *titled* with
   a claim about the location. If so, the handoff carries sanitized paths — directory, file count, line counts
   — never the filenames.

   **1c. Grep your own new prose for the subject's name, before committing.** For every hit ask: does this
   state the leak's SHAPE, or its CONTENT? Shape is the lesson; content is the leak. *"Eleven titles, four
   naming civic facts"* teaches everything; the four facts teach nothing and contaminate. (M-97 — the rule
   against vector 1 recreated vector 1, inside the section documenting vector 1, in the same session that
   fixed it. No gate caught it; it surfaced only because the developer asked the session to account for its own
   exposure.) Why this needs to be mechanical rather than an exhortation: a rule that leaks is more persuasive
   than one that does not, because it shows its evidence. The incentive runs toward contamination.

2. **Update `06_Worked_Example_Provenance.md`** with any worked examples this pass added to the methodology. An
   unmanifested example is invisible contamination for the next same-location run.
3. **Confirm the quarantine list was built by RULE, not by recall** — `05` §6.1's content split applied section
   by section. A list assembled from memory is written by the one person who has already read everything.
4. **Open the header of every file on the admissible list and check its own cited sources.** A file that cites
   a withheld document is downstream of it, whatever its filename says. Seconds per file, and it would have
   caught both of Run 3's contamination events.
5. **Confirm any corpus-wide retrieval layer is flagged as unusable** — a graph, an embedding index, a
   full-text search cannot honor a quarantine, because quarantine is provenance and retrieval is content.

## 10.2 — Path and structure integrity

6. **Every path named in the handoff exists** — admissible and withheld alike. A withheld path that has moved
   is a quarantine hole.
7. **The next run's OUTPUT files do NOT already exist.** A pass creates its own output (`00_Frame.md`, `01`…`10`
   and their round records). **Scaffolding MAY be pre-seeded** *(2026-10-21, developer-approved at the Mirny Step 10
   review; `M-299`)*: the Pre-Trip sheet, the Position-Coverage ledger, `README.md` and the `Datasheets/` set are
   inputs, not output, and a warm run needs them. **For a COLD run the folder's contents are still a contamination
   surface** (leak-register row 5, filenames as theses; Step −2 sanitized paths), so a cold run delegates the listing
   and reads only the sanitized form. A pre-seeded folder that holds *output* is still a contamination risk and a
   status lie.
8. **The shared observations file sits OUTSIDE every quarantined folder**, or the next run cannot write to it
   without breaking its own quarantine *(M-0)*.

## 10.3 — Record integrity

9. **Run Gate 0 outward:** does every tracker's completion claim match what the files actually contain? List
   what the file contains, never a summary claim.
10. **Confirm findings were IMPLEMENTED, not merely recorded.** A finding logged in the observations file and
    absent from the rule it should have changed has not been made — the next pass follows the rules, not the
    log.
11. **Check the handoff states what the next run CANNOT prove**, as well as what it can. A run whose limits are
    undeclared will be over-read.

## What it caught the first time it was run

Asked whether a handoff was ready, the honest response was to check rather than answer — and the check found
that a memory entry recording an analytical *technique* had inlined its own per-city results, including a
withheld personality read and a quarantined axis phrase, verbatim, in the auto-loaded index. Ten further entries
carried conclusion vocabulary about the same cluster. The declaration "everything is prepared" would have been
wrong, and the cold run it authorized would have produced a confident, coherent, contaminated result.
