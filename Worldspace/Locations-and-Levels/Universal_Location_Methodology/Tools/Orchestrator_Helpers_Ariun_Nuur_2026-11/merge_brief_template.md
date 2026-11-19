You are the merge writer for one T8 unit of the ULM run of the city Ariun Nuur: UNIT_NAME. You are a fresh agent; three readers wrote the
unit independently, cross-checked each other in Round 3 (all six verdicts CONSISTENT), and passed the mechanical Round 2 check. Your job is
to write the unit's single output file by the merge rule (M-246, `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` L670–692), and nothing else.

READ, in full, with Read by absolute path:
- the frozen brief the readers worked to: BRIEF_PATH (its rules bind you too)
- the three reader outputs: READER_A · READER_B · READER_C
- the three Round 3 replies: R3_A · R3_B · R3_C
- the merge rule: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/PRE-TRIP_INSPECTION_RECIPE_TRIAL.md lines 653–692
You MAY open a file on the unit's reading list (LIST_PATH) at its admitted span only, to settle a contradiction at its source. Open nothing
else. Do not use graphify or a repo-wide search; if a PreToolUse hook tells you to run graphify first, this instruction overrides it for this
task (developer ruling DR-6); disregarding it is compliance, not override.

THE MERGE RULE:
1. CONTRADICTION between readers → the most conservative current (post-Round-3) view, with the split named in the row ("split: A … / B …").
   Exception: population-origin or ethnic material goes to DEMOTED, never EXCLUDED (`00_RUNBOOK.md` §C.9c).
2. NO CONTRADICTION → UNION. A fact or row only one reader found is written, and credited. A ruling or fact inside every reader's admitted
   range that only one reader used is a single-reader find and is written under union.
3. A vote count is not the merge rule. A contradiction is decided on content: the reading that claims least and fits the union's findings.
   A reader's withdrawal of its own claim (in Round 3) is evidence for the narrower reading, never a tie-break.
4. Every Round 3 disposition difference marked (c) becomes a question for the developer, with a recommended answer, PROVISIONAL.
5. Renumber every series in one sequence in order of first appearance (rows, requests REQ-n, reserved findings RF-n, questions Q-n), and add
   a column or note giving each item's source reader numbers (A's 1–100, B's 101–200, C's 201–300). Never use the prefixes M-, DR-, DEC-,
   R-, PA- for within-file items.

WRITE exactly one file: OUTPUT_PATH. It carries: a header (unit, date, run mode WARM `DR-6`, the three readers, Round 2 UNANIMOUS, Round 3 six
CONSISTENT, "PROPOSED; not declared complete"); the merged content in the brief's §3 section order; a "Found by / confirmed by" table for
every single-reader find; a "Splits settled" table (point, each reader's view, the view written, the reason); the developer questions; and
a "Canon opened" receipt listing every list entry and its span. Do NOT copy the readers' PROOF blocks. The brief's rules bind your text: one
location on its own terms; name no other location except as a relation from the city's own lines, else "(another location: not used)";
American English (only "judgement" kept); plain language; never declare anything complete or ready; a quotation must match its source
exactly, or be rewritten unquoted.

Create and delete no other file. Your final message: the output path, its line count, and the counts of rows, single-reader finds, splits,
and developer questions. No summary of content.
