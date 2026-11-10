# Lessons into the rules: draft for the developer (written 2026-11-09)

**Status: APPLIED 2026-11-09 on the developer's word ("apply the decisions I've made"), as drafted, with two departures recorded in `M-320`: row 7 was written into `Amendment_Layer_Rules.md` (rule 6), not into the runbook's Step −1 section, because the rule it extends is written in no rule file and a runbook insertion moves every cited line; rows 1 to 5 are lines 21 to 25 of `T8_Standing_Brief_Lines.md` part B, and row 6 is rule 5 of `Amendment_Layer_Rules.md`.** *(Original status, kept for the record: draft, not applied, no rule file edited.)* At the Davis walkthrough of 2026-11-09 the developer approved writing the process lessons of that run into the rules (six rows) and the numbering-frame rule (one row). As with the earlier lessons (`DR-116` item 4, `DR-118`), the wording is shown first; it is applied, with the hash-checked script and no commit, only on the developer's word. Tags name no location (`DR-118` item 2).

**Not approved, so not drafted:** making the project's own character folders a mandatory Phase 10 sweep target (the developer left that one out on 2026-11-09).

**Also done today, not a rule row:** the reader-list tool (`Tools/make_t8_required_list.py`) now skips table rows that the Pre-Trip marks forbidden (a status cell with the stop sign and WITHHELD or RESOLVES TO NOTHING ADMISSIBLE) and reports each as a comment. Checked on Davis: Phase 2's list went from 10 entries to 9, the other nine lists are byte-identical to before. The original is kept at `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/02217f86-adf1-470f-9f2c-3f08264e7c4a/scratchpad/tool_test/make_t8_required_list.ORIGINAL.py`.

## The rows

| # | Proposed rule text | Where it would go | What it came from |
|---|---|---|---|
| 1 | **When a reading list includes a ruling, scan the rulings log for any later ruling that answers a question the included ruling lists as "not decided", and add the later ruling to the list.** | `T8_Standing_Brief_Lines.md`, part B (lines for the orchestrator) | A ruling that settled four composition rows was missing from two reading lists; the Phase 2 readers caught it in Round 3 |
| 2 | **State a pass's ground by reading the pass's own lines, never from a summary of it.** A brief that paraphrases a ground from a summary has to be checked against the lines before it is dispatched. | `T8_Standing_Brief_Lines.md`, part B | Briefs misstated a pass's ground or a citation: one was written from a drift review's summary, not from the pass lines, and the readers found it (the run's log, entry on errors in my own briefs) |
| 3 | **Give each reader its own private staging folder.** Two readers never share one. | `T8_Standing_Brief_Lines.md`, part B | In the one-reader checks, one reader noticed another reader's output file in the shared staging folder (and did not open it); two readers also left helper scripts there. The re-derivation pieces then used one folder per reader |
| 4 | **Generate one brief, and read it end to end before any reader is dispatched.** Regenerate every brief if the generator changes. | `T8_Standing_Brief_Lines.md`, part B | A template printed a literal placeholder instead of the piece name; found only by reading a generated brief before dispatch |
| 5 | **A brief that relies on a standing answer cites the developer's verbatim words in the entry that records them for this location**, never an entry that records the same words for another location. | `T8_Standing_Brief_Lines.md`, part B | A brief cited a ruling item that records "the rulings as they stand govern" against another location |
| 6 | **A record states what a tool returned, and what a piece says on a line the orchestrator has read. It never carries the orchestrator's own paraphrase of a piece.** | `Amendment_Layer_Rules.md`, new rule 5 | The orchestrator described two pieces from one-line summaries and had to correct the records after reading them |
| 7 | **A numeric read spec names the commit or the line count it was computed against**, so a reader can tell pass-time numbering from current numbering. | The Step -1 text of `00_RUNBOOK.md`, beside the rule that a contract publishes a numeric read spec (the entry `M-224` in the observations log); the exact insertion point is located when it is applied | The Step -1 contract's published read spec was in pass-time numbering; on today's spec it would read two struck lines and miss 27 admitted lines |

## What applying would be

1. The developer's word on the wording above (as written, changed, or struck row by row).
2. One hash-checked script run over the files named in the last-but-one column, with a preview first, as on 2026-11-04.
3. A new observation entry recording the change, and a rulings-log entry.
4. No commit without the developer's word.

*The seventh lesson of the Davis run (the helper scripts were written against Davis's paths and would have to be made general before another city uses them) is a build task, not a rule, and is not drafted here.*
