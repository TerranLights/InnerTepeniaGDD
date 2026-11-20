# T8 Round 1 brief — Ariun Nuur, ULM Step 7 (QA: the gates), sub-unit {U} of 3 — FROZEN at dispatch, 2026-11-20

You are one of three independent readers (A, B, C) of sub-unit {U}. You will not see the others' work until Round 3. This brief is final; no
part of it will be amended while you work (`00_RUNBOOK.md` L933–951). If anything in it cannot be satisfied, say so in your output; do not
guess past it.

**Why the step is split.** Step 7 runs the gates over the whole pass, more than one reader holds. It runs as three sub-units by files: **Q1**
(the Step −1 contract, the frame, Steps 1–3, Phases 2–3), **Q2** (Phases 4–8), **Q3** (Phase 4 again for Gate 3, Phases 9–10, Steps 5–6).
**You are sub-unit {U}: {SCOPE}.**

## 0 · Before anything else
1. **Create your output file first**, at the path given to you in your dispatch message (your own private staging folder), **with the
   Write tool**, and write to it only with Write and Edit. Create and delete no other file anywhere.
2. Start it with a `## 0 · Reading log`. Log each list entry as you finish reading it.
3. The reading list is `.t8_required_07_Step7{U}.txt` in the pass folder
   `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/`.
   **The list has {N} entries:** 1 the runbook's Step 7 (L2936–2977); 2 `04` Parts I–II (L96–422: every gate); 3 the gates' full-text
   quick-reference sheet (two lines naming other locations cut); 4 the Step 7 datasheet (the gate index and this city's notes); 5 the Phase 7
   datasheet (the industry figures; two lines naming other locations cut); 6 the extent row and its note (`Extent_and_Density_Per_City.md`
   L625, L631); 7 `DR-143`; {ENTRIES}; then the orchestrator's findings index (navigation only); and last the orchestrator's **mechanical
   sweep** of generator vocabulary over the pass (file:line:term; a hit is not a defect).
   **The pass files are admitted at spans that leave out their bookkeeping sections.** Read the list file itself with Read before you begin.
   You may use `wc -l` and `sed -n 'Np'` on a listed file, inside its admitted range, only to check a count or a positional line. **No
   `grep`, `awk` or other command on any file, your own output file included.**
4. You MAY open a pass file outside your sub-unit at a range of at most 60 lines that one of your files cites, and the spec at a range of at
   most 60 lines a pass file cites; log each such read. Nothing else off the list. ⛔ Never open the city's culture, robot-culture or
   personality files (Step 5 stage B has read them as a check), another city's files, the differentiation table, or `Test_Runs/`.

## 1 · Standing lines (copied from `T8_Standing_Brief_Lines.md`; the wording is the contract)
{STANDING}

## 2 · Rules of this run (binding)
- **One location, on its own terms.** Never compare Ariun Nuur with any other city, rank it, or use another city as a baseline. Never name
  another location, except a relation from the city's own lines (its subnet, the Mirny subnet; a road, a port, an airport).
- **Gate 4's swap partner is a real-world comparable, never a Tepenian city** (the Step 7 datasheet; the law of one location).
- **Gate 6's against-siblings half is TERMINAL and is not run**; run only its within-location half and the substitutes 3 and 4 (real-world
  comparables; the generator-conflict method); substitute 1 is deferred to after the pass; substitute 2 is not run (`DR-142` item 2).
- **Gate 10 is the Review Panel (Step 8)**, not run here. **Gate P** runs on a parent's pass: this city has no written children; record it as
  not applicable, with that reason.
- **Paste raw scan output, whole**, or label an excerpt `raw output, excerpted (N lines omitted, reason)` (runbook L2941). **Verify the
  instrument before trusting any zero.** **Report what Gate 11 cleared as well as what it flagged.** **Hand-check one row** before trusting
  any computed figure (runbook L2953–2957). **No score of any kind in-run** (L2959–2964): this location's own figures only.
- **The station-builder scan looks for denials as well as assertions** (runbook L2944; `DR-19`): a sentence saying the station's builder
  does *not* explain a form is the same violation as one saying it does.
- **The national tower** by role only; **no demonyms**; **no invented person names**; **the waiting topics** (CST, DCI) are not judged as
  if the pass should have written them; **no web call**; **American English** (only "judgement" kept); **plain language**; never declare
  anything complete or ready. Number your items in your own range: A from 1, B from 101, C from 201.

## 3 · The task — run these gates over your files
{GATES}

For **every gate**, write: the gate's question (one line, from entry 2 or 3) · what you checked, file and line · **the raw evidence** (the
lines or counts) · the verdict: **PASS** · **FAIL** (with the fix, PROPOSED; the pass's files are not edited) · **FLAG** (needs a developer
answer) · **NOT RUN** (with the reason) · **N/A** (with the reason). A gate passed on a zero says how the zero was checked.

Then: **errata** (a numbered list of every FAIL, each with its source line and the corrected statement, PROPOSED: these enter the Review
Panel's brief as facts, runbook L2983); **requests and questions** (each question with a recommended answer, PROVISIONAL).

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
1. **Recorded in this pass:** the Step −1 contract through Step 6, each a T8 unit, all PROPOSED; questions from `DEC-708` on stand on their
   recommended answers, PROVISIONAL (source: `RUN_PROGRESS_Ariun_Nuur.md`; no admitted line).
2. **Step 5's strongest finding is SC-1** (the physical core: heat paid at every place a body stops), its named leg contradicted in part by
   tier-3 lines only (source: `05_Reconciliation.md`, on Q3's list).
3. **The mechanical sweep** (the last entry) was made by the orchestrator's script over every pass file through Step 5 (768 hits); check the
   hits in your own files only.
4. **The extent row** (entry 6) gives this city's built extent at two densities; Gate 11's density sub-check divides the population by it
   (the Step 7 datasheet's note).
5. **No web call** (the session's web budget is nearly spent).

## 5 · Hand back
Your final message is a **receipt only**: your output file's path, its line count, the verdict per gate (PASS · FAIL · FLAG · NOT RUN · N/A),
the errata count, requests and questions, and `MANIFEST: read <k> of {N} entries; not reached — <entries or "none">`. Nothing else.
