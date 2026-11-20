# T8 Round 1 brief — Ariun Nuur, ULM Step 9 (Record) — FROZEN at dispatch, 2026-11-20

You are one of three independent readers (A, B, C). You will not see the others' work until Round 3. This brief is final; no part of it will
be amended while you work (`00_RUNBOOK.md` L933–951). If anything in it cannot be satisfied, say so in your output; do not guess past it.

## 0 · Before anything else
1. **Create your output file first**, at the path given to you in your dispatch message (your own private staging folder), **with the
   Write tool**, and write to it only with Write and Edit. Create and delete no other file anywhere.
2. Start it with a `## 0 · Reading log`. Log each list entry as you finish reading it.
3. The reading list is `.t8_required_09_Step9.txt` in the pass folder
   `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/`.
   **The list has {N} entries:** 1 the runbook's Step 9 and §9.5 (L3006–3079); 2 this run's entries in the observations log (L8839–8855,
   for the next `M-` number and the form); 3 the Step 9 datasheet; 4 the pass's snag log `09.5_Log.md`; 5 Step 7's header and verdict
   table (`07_QA_Gates.md` L1–57); 6 the Review Panel's output, `08_Review_Panel.md`{PANEL_SPAN}; 7 Step 6's *Propagation* section
   (`06_Differentiation.md` L329–341); 8 the position-coverage ledger; 9 the orchestrator's deferral list (`.t8_Step9_deferrals.md`);
   10 the orchestrator's anchor sweep with its hand triage (`.t8_Step9_anchor_sweep.md`); 11 the trackers' lines for this city
   (`.t8_Step9_trackers.md`). Read the list file itself with Read before you begin. You may use `wc -l` and `sed -n 'Np'` on a listed file,
   inside its admitted range, only to check a count or a positional line. **No `grep`, `awk` or other command on any file, your own output
   file included.**
4. **To discharge a deferral** (task 3 below) you MAY open the pass file a deferral line stands in, at a range of at most 60 lines around
   that line, and the file it points to at a range of at most 60 lines; log each such read. Nothing else off the list. ⛔ Never open the
   city's culture, robot-culture or personality files, another city's files, the differentiation table, or `Test_Runs/` beyond entry 2.

## 1 · Standing lines (copied from `T8_Standing_Brief_Lines.md`; the wording is the contract)
{STANDING}

## 2 · Rules of this run (binding)
- **One location, on its own terms.** Never compare Ariun Nuur with any other city or name another location, except a relation from the
  city's own lines.
- **Gate 0 outward (runbook Step 9 item 3, `M-287`, `M-109`):** a tracker line says what the files contain, one line plus a pointer, each
  step's status PROPOSED or confirmed; **no finding in a tracker** (findings go to the observations log). **Never declare anything
  complete or ready.** Nothing in this pass is confirmed by the developer yet; every step is PROPOSED.
- **The recording law (§9.5):** snags, dead ends, killed findings (classed *killed by evidence* or *killed for want of an admitted line*),
  self-corrections (*what was believed · why it was wrong · what changed it*), tooling obstacles, unclear points; never compress a negative
  result into a positive one. **Number new entries from `M-417`**, continuously.
- **Paste raw tool output whole**, or label an excerpt `raw output, excerpted (N lines omitted, reason)`.
- **The national tower** by role only; **no demonyms**; **no invented person names**; **no web call**; **American English** (only
  "judgement" kept); **plain language**. Number your items in your own range: A from 1, B from 101, C from 201.

## 3 · The task
1. **The QA block and the Review Panel block (item 1).** Say what each block must carry when appended to `09_Record.md` (the verdict table
   from entry 5; the panel's output block from entry 6), and check that each source block is whole and consistent with its own file's
   header (counts, numbering, the `T5 - LATE LOVER FACULTY:` line present exactly once in entry 6). Report any defect.
2. **The differentiation entry (item 2).** The orchestrator confirms the city's ten rows are present in the table (§4 item 3: you never
   open the table). Check that Step 6's *Propagation* section records what was noticed and where, without naming any other location or its
   content. Say whether anything noticed in this pass about another location still needs recording, and where.
3. **Discharge every deferral addressed to Step 9, Step 10 or the pass's close (item 5, `M-291`, `M-314`).** For each line on entry 9:
   say whether it is a deferral to this step (many lines only mention a step), and if so, discharge it (do it, if it is a check you can make
   from the admitted lines), or close it as "not applicable" with the reason, or hand it on (to Step 10, to the developer as a question, or
   to a named later stage), with the line. Do not skip a line; a deferral that no step names is a hole.
4. **The anchor sweep (item 5).** Re-check the orchestrator's triage on entry 10 against the files it names (open each cited line, within
   §0 item 4's limit), and say whether any citation moved. Hand-check at least one row yourself.
5. **The trackers (item 3).** From entry 11 and what the pass's files contain, write the **one-line status** each tracker should carry for
   this city (MASTER tracker; RUN_PROGRESS), listing each step's state (PROPOSED), with a pointer; flag any existing tracker line that
   overclaims or carries a finding.
6. **Methodology (item 4) and the recording law (§9.5).** From entry 4 (the pass's snag log, AN-1 on) and the round records' procedural
   events the log points to, draft the **observations-log entries** this pass still owes, from `M-417`, in entry 2's form (one paragraph
   each: what happened, on which unit, the lesson; tagged *snag*, *instrument*, *method note*, *self-correction*, *killed finding* or
   *dead end*). Include at least: the findings index's missed heading forms and the generator sweep's blind spots (Step 7); a stage-B
   PROOF-form failure that a brief's "usual form" caused (Step 5); the exact-field helper's misreading of digits in a file name; the Review
   Panel run split by files (Step 8) and what it cost or showed. **Say for each whether it changes a rule** and, if so, which file and line
   the change belongs in (PROPOSED; the methodology files are not edited by this step).
7. **Requests and questions** (each question with a recommended answer, PROVISIONAL).

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
1. **Recorded in this pass:** the Step −1 contract through Step 8, each a T8 unit, all PROPOSED (source: `RUN_PROGRESS_Ariun_Nuur.md`, entry
   11's extract).
2. **The next observations-log number is `M-417`** (source: entry 2's last entry is `M-416`).
3. **The city's ten rows are present in `Cities/Cross_City_Culture_Differentiation_Table.md`**: `grep -c '^| Ariun Nuur |'` on the table
   printed {ROWCOUNT} (a count only; no other row was read).
4. **The deferral list and the anchor sweep are mechanical** (their commands are in their headers); a zero or a miss in them is the
   instrument's, and says so.
5. **No web call.**

## 5 · Hand back
Your final message is a **receipt only**: your output file's path, its line count, the counts of deferrals (deferral to this step ·
discharged · closed not applicable · handed on · not a deferral), whether any anchor moved, the tracker lines in one line each, the
number of observations-log entries drafted (and the last `M-` number), requests and questions, and
`MANIFEST: read <k> of {N} entries; not reached — <entries or "none">`. Nothing else.
