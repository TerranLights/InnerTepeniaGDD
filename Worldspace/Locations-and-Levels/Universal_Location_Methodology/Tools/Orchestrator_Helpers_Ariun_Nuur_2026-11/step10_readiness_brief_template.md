# T8 Round 1 brief — Ariun Nuur, ULM Step 10 (THE READINESS CHECK) — FROZEN at dispatch, 2026-11-20

You are one of three independent readers (A, B, C). You will not see the others' work until Round 3. This brief is final; no part of it will
be amended while you work (`00_RUNBOOK.md` L933–951). If anything in it cannot be satisfied, say so in your output; do not guess past it.

**The governing principle: VERIFY, DO NOT ASSERT** (runbook L3083–3091). "Ready" is a claim and needs evidence like any other.

## 0 · Before anything else
1. **Create your output file first**, at the path given to you in your dispatch message (your own private staging folder), **with the
   Write tool**, and write to it only with Write and Edit. Create and delete no other file anywhere.
2. Start it with a `## 0 · Reading log`. Log each list entry as you finish reading it.
3. The reading list is `.t8_required_10_Step10.txt` in the pass folder
   `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/`.
   **The list has {N} entries:** 1 the runbook's Step 10 (L3080–3177) and its run-modes row (L3189); 2 the Step 10 datasheet; 3 the auto-loaded memory index
   (`MEMORY.md`); 4 the worked-example provenance manifest at its rule sections and this city's own section; 5 the orchestrator's
   next-run name scans (`.t8_Step10_scans.md`); 6 the orchestrator's handoff path check (`.t8_Step10_paths.md`); 7 this run's handoff file
   (two lines naming other locations cut); 8 the Step 9 record at its trackers, methodology and deferral sections{REC_SPAN}; then the
   orchestrator's findings index (navigation only). Read the list file itself with Read before you begin. You may use `wc -l` and `sed -n
   'Np'` on a listed file, inside its admitted range, only to check a count or a positional line. **No `grep`, `awk` or other command on
   any file, your own output file included.**
4. **To discharge a deferral handed to Step 10** you MAY open the pass file it stands in at a range of at most 60 lines, and the file it
   points to at a range of at most 60 lines, and you MAY check whether a named path exists with `ls -d <path>` (existence only); log each.
   ⛔ Never open: another location's files or pass folder (the next run's folder included; the orchestrator's scan gives its counts);
   any memory file other than the index (entry 3); the city's culture, robot-culture or personality files; the differentiation table;
   `Test_Runs/`; `Worked_Example_Archive/`.

## 1 · Standing lines (copied from `T8_Standing_Brief_Lines.md`; the wording is the contract)
{STANDING}

## 2 · Rules of this run (binding)
- **10.1 runs against the NEXT pass's subject, not this one** (runbook L3096). The next location in run order is the subject of the run in
  the week of 2026-11-29 (entry 3). **Work from the orchestrator's scans (entry 5): line numbers, counts, file names only.** Never open a
  file that names that location to read its content, and **write that location's name nowhere in your output except where a scan line
  forces it** (call it "the next subject"). Its run is a WARM run (entry 3); say which 10.1 items a warm run requires and which it does not
  (`Run_Modes_Warm_and_Cold.md` is summarized in the runbook's row at L3189, on your list; do not open the file).
- **10.2 and 10.3 run on this pass and its handoff.** "The handoff" here is this run's handoff file (entry 7) and the status lines Step 9
  drafted (entry 8 §4).
- **Discharge every deferral handed to Step 10** (entry 8 §6's rows marked *handed on* to Step 10): for each, do it if it is a check you
  can make from the admitted lines or an existence check; otherwise hand it on, with its line, to the developer (as a question), to a named
  later stage (the DCI, the CST, the terminal differentiation check, the next methodology commit), or to the next session. **Never close a
  deferral as done by assertion.**
- **One location, on its own terms.** Never compare Ariun Nuur with any other city. **The national tower** by role only; **no demonyms**;
  **no invented person names**; **no web call**; **American English** (only "judgement" kept); **plain language**; **never declare
  anything complete or ready**: report what was verified and what was not. Refer to the developer as *they*. Number your items in your own
  range: A from 1, B from 101, C from 201.

## 3 · The task — run 10.1, 10.2 and 10.3, item by item
For **each of the eleven items** (runbook L3096–3162): the item's question in one line · what you checked (entry and line) · the
evidence · the result: **VERIFIED** (with the evidence) · **NOT VERIFIED** (what is missing) · **FAILS** (what is wrong, and the fix,
PROPOSED) · **N/A** (with the reason, e.g. a cold-run-only item for a warm next run). Then: **the deferrals handed to Step 10** (a table,
every row: its line, what was done, the result or where it went); **what the next session cannot prove** (item 11, written plainly);
**requests and questions** (each question with a recommended answer, PROVISIONAL).

**Your PROOF blocks, one per list entry, LAST in your output, after every other section, with nothing written after them, in exactly this
form:**
```
### PROOF: <absolute path, exactly as the list gives it, before any ` :: `>
LRANGE: <the admissible range you were bound to, or FULL>
LINES: <your own count OF THE ADMITTED SET>
L1: <exact text of the FIRST admissible line, verbatim, with nothing before it>
LMID: <exact text of the MIDDLE admissible line ((N+1)//2 within the set), verbatim>
LLAST: <exact text of the LAST admissible line, verbatim; if it is blank, leave the value empty>
QUOTE: <one load-bearing sentence, exact, from inside the admissible range>
```
No line numbers inside the fields; a blank line's value is left empty, never described. For a multi-span range the admitted set is the spans
concatenated in list order.

## 4 · Orchestrator-verified results
1. **Recorded in this pass:** the readiness check (a check), Step −1 through Step 9, each a T8 unit, all PROPOSED; nothing confirmed by
   the developer (source: entry 8 §4).
2. **The next run's pass folder exists and holds 22 files, none with an output-shaped name** (entry 5, §7: a count; no file was opened).
3. **The shared observations file sits outside every pass folder** (entry 5, §8).
4. **This pass added no worked example to the methodology's rule files**; its method changes (`DR-144`'s copies of LAW 0-P, filed
   2026-11-20) are statements of a law, not a city's answers (source: entry 8 §5). Check it against entry 8.
5. **No web call.**

## 5 · Hand back
Your final message is a **receipt only**: your output file's path, its line count, the result per item (1, 1a, 1b, 1c, 2–11), the counts
of Step 10 deferrals (done · handed on, by destination), requests and questions, and `MANIFEST: read <k> of {N} entries; not reached —
<entries or "none">`. Nothing else.
