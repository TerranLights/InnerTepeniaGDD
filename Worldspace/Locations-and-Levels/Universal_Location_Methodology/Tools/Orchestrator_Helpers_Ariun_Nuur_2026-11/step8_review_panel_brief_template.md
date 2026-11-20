# T8 Round 1 brief — Ariun Nuur, ULM Step 8 (the Review Panel), sub-unit {U} of 3 — FROZEN at dispatch, 2026-11-20

You are one of three independent readers (A, B, C) of sub-unit {U}. You will not see the others' work until Round 3. This brief is final; no
part of it will be amended while you work (`00_RUNBOOK.md` L933–951). If anything in it cannot be satisfied, say so in your output; do not
guess past it.

**Why the step is split.** The Review Panel reads the finished pass, which is more than one reader holds. It runs as three sub-units by
files: **R1** (the frame, the spine, Phases 2–4), **R2** (Phases 5–8), **R3** (Phases 9–10 and the Step 5 reconciliation). Every sub-unit
also reads the spine's shape (its §5), so every panel knows what the whole place is claimed to be. **You are sub-unit {U}: {SCOPE}.** Run
the whole panel over your files; the merge writer joins the three panels into one.

## 0 · Before anything else
1. **Create your output file first**, at the path given to you in your dispatch message (your own private staging folder), **with the
   Write tool**, and write to it only with Write and Edit. Create and delete no other file anywhere.
2. Start it with a `## 0 · Reading log`. Log each list entry as you finish reading it.
3. The reading list is `.t8_required_08_Step8{U}.txt` in the pass folder
   `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/`.
   **The list has {N} entries:** 1 the runbook's Step 8 (L2978–3005); 2 the Review Panel method, `Disciplines/00f_Review_Panel.md` (two
   lines naming other places cut); 3 the Step 8 datasheet; 4 the position-coverage ledger; 5 **Step 7's errata** (the section of
   `07_QA_Gates.md` that lists them); 6 `DR-143`; {ENTRIES}; then the orchestrator's findings index (navigation only).
   **The pass files are admitted at spans that leave out their bookkeeping sections.** Read the list file itself with Read before you begin.
   You may use `wc -l` and `sed -n 'Np'` on a listed file, inside its admitted range, only to check a count or a positional line. **No
   `grep`, `awk` or other command on any file, your own output file included.**
4. You MAY open a pass file outside your sub-unit at a range of at most 60 lines that one of your files cites, and the spec at a range of at
   most 60 lines a pass file cites; log each such read. Nothing else off the list. ⛔ Never open the city's culture, robot-culture or
   personality files, another city's files, the differentiation table, `Test_Runs/`, or `Worked_Examples_Archive/`.

## 1 · Standing lines (copied from `T8_Standing_Brief_Lines.md`; the wording is the contract)
{STANDING}

## 2 · Rules of this run (binding)
- **Step 7's errata are facts** (runbook Step 8: *"Step 7's errata enter the Review Panel's brief as facts, each with its source line, and
  the panel runs on the corrected statements"*). Where a pass line has an erratum, the panel reads the corrected statement, not the line.
- **One location, on its own terms.** Never compare Ariun Nuur with any other city, rank it, or use another city as a baseline. Never name
  another location, except a relation from the city's own lines (its subnet, the Mirny subnet; a road, a port, an airport).
- **The peer-free test decides whether to refuse an objection** (runbook Step 8): *"Would satisfying this objection replace something
  SPECIFIC TO THIS PLACE with something that could be true anywhere?"* If yes, refuse it. **Whether a refusal is `unmet` or `declined`**
  is `00f`'s self-knowledge test (L744–753): an `unmet` must name an admitted or ruled line that shows the place knowingly holding the
  thing; the pass's own coinage cannot be that line; a refusal grounded only in national canon is `declined`. **Never use `00f`'s older
  district wording** (*"more like the other twelve"*, L638): it needs a sibling set and is unrunnable in a city run.
- **Six dispositions:** accepted · noted · rejected · refereed · unmet · declined. Every objection gets one, with its reason.
- **The Neighbor From Across the Line** is cast from a **relation in the city's own lines** (a road's far end, the subnet, a port or
  airport the files name), by role, never by a place name, and speaks only of **relation** (what this place needs from elsewhere, what
  flows, in which direction), never *"unlike"* or *"more than"*. **If no standpoint can be found in your files, the position cannot be cast:
  record that as a result** (`00f` L757–764), and do not substitute another neighbor.
- **The Lover faculty's question, every time:** *is this place alive, and could anyone love it?* Give the verdict for your files in one
  line under the heading `### The Lover faculty, late`, as `Late Lover-faculty verdict ({U}): <verdict>`, and set it beside Phase 6's early
  verdict (the `T5 - EARLY LOVER FACULTY:` line, Phase 6 L506, which every sub-unit may open at that one line). ⛔ **Do not begin any line
  of your output with `T5 - LATE LOVER FACULTY:`;** only the merge writes that marker.
- **The panel does not check plausibility** (`00f` L785–804); Gate 11 did. **Rule 1:** a position with nothing to say says nothing; never
  manufacture an objection. **Rule 3:** a position is not guaranteed what it wants. **The four-corner check** (`00f` §5) before you accept
  your run.
- **The waiting topics** (government and justice wait for the DCI; faith, holidays, dishes, music, dress, games, slang and drinking wait for
  the CST) are **not** objected to as if the pass should have written them. A position may say what it would want there; the disposition is
  `noted`, sent on to the waiting stage.
- **The national tower** by role only; **no demonyms**; **no invented person names** (cast by role: *a night keeper's child*, never a
  name); **no web call**; **American English** (only "judgement" kept); **plain language**; never declare anything complete or ready.
  Number your items in your own range: A from 1, B from 101, C from 201.

## 3 · The task — run the panel over your files
{TASK}

For **every position**, write: the casting (by role) · the objection **in the position's own voice** (or *no comment*) · its kind
(addition · inconsistency · doubt) · the lines it rests on (file and line) · the disposition with its reason · for `unmet`, the admitted or
ruled line that shows the place knowingly holding the thing. Then: **the Passer-Through's result** (PASS · fails as the shadow written as
the surface · fails as no legible face) · **Life Arcs, Faculties and Shadows consulted, with silences and acquittals** (a conditional
acquittal states what would make it guilty) · **refereed conflicts** · **the four-corner check** · **panel-derived findings, PROPOSED**
(each tagged as panel-derived, or as strengthening an existing finding, with the finding's id) · **the standout**: does the panel change
what Step 5 named the strongest finding (SC-1)? · **the late Lover-faculty verdict** · **requests and questions** (each question with a
recommended answer, PROVISIONAL) · the counts by disposition, with each `unmet`'s ground (never as a measure of the place).

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
1. **Recorded in this pass:** the Step −1 contract through Step 7, each a T8 unit, all PROPOSED; questions from `DEC-708` on stand on their
   recommended answers, PROVISIONAL (source: `RUN_PROGRESS_Ariun_Nuur.md`; no admitted line).
2. **Step 5's strongest finding is SC-1** (the physical core: heat paid at every place a body stops), its named leg contradicted in part by
   tier-3 lines only (source: `05_Reconciliation.md`; on R3's list).
3. **Step 7 ran Gates 0–9, 11, C, F, I, P and G; Gate 10 is this step** (source: `07_QA_Gates.md`, its verdict table; entry 5 holds its
   errata).
4. **The early Lover-faculty verdict** is Phase 6 L506 (source: that line).
5. **No web call** (the session's web budget is nearly spent).

## 5 · Hand back
Your final message is a **receipt only**: your output file's path, its line count, the casting in one line, the counts by disposition, the
Passer-Through's result, the late Lover-faculty verdict, whether the standout changes, the counts of panel-derived findings, requests and
questions, and `MANIFEST: read <k> of {N} entries; not reached — <entries or "none">`. Nothing else.
