# Amendment-layer rules — amending a pass after it is written

> **Created 2026-11-04 at the developer's direction:** the amendment-layer rules live in a separate file beside
> the runbook, not in a new runbook section (`DR-117` item 3, `DEVELOPER_RULINGS_LOG.md`). **`00_RUNBOOK.md`
> carries a one-line pointer to this file just before its "# Where everything lives" table.** The rules below
> come from the lessons of the amendment layer and repass of 2026-11-04 (`Research_Logs/Lessons_Into_Rules_Draft_2026-11-04.md`,
> approved row by row on 2026-11-04; the change itself is recorded as `M-319` in
> `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`).

## What this file governs

**The amendment layer: everything written about a pass after the pass itself is written.** That is:

- **Amendment pieces** — a re-derivation of one phase or step, written as a new file appended beside the pass,
  never a rewrite of it.
- **Amendment notes and notices** — what is true now, where a pass's text no longer matches its sources.
- **Pointer lines** — a line in an existing file that sends its reader to an amendment.
- **Registers** — the lists that scope which findings an amendment has to re-derive.
- **Dockets** — proposed corrections, held for the developer's word.

## The standing rulings this file sits inside

**These are rulings, not new rules; they are stated here so that no amendment work has to reconstruct them.**

| Ruling | What it says | Where |
|---|---|---|
| `DR-101` | **A finished pass's files are never edited.** Changes in its sources are recorded in its amendment note. | `DEVELOPER_RULINGS_LOG.md` L1673–1679 |
| `DR-102` | **Nothing already recorded is reworded to carry its own history.** An amendment note states the current fact with its source address, not what the text used to say; the history stays in git and in the drift reviews; entry IDs stay stable, because other files cite them. | L1681–1687 |
| `DR-74` | **Each amendment piece runs with three readers and the usual rounds**, and its output is appended beside the pass, never a rewrite. Pieces after the first may use trimmed reading lists; that trimming applies to amendment pieces only, never to the city runs. | L1404–1410 |
| `DR-116` item 2 | **A pointer line at the end of an old file is a pass-file edit:** it is applied only when the dockets are applied, and `DR-101` is to be reconciled then. | L1814 |

## The rules

### 1 · A scoping register is itself a derivation

**A register that scopes a re-derivation is itself a derivation:** it gets the same three-reader check before any
piece is planned from it, and its "by citation" rows count as unread rows. *(Added 2026-11-04, `M-302`; amendment layer.)*

### 2 · A draft register is where to look, never a budget

**A draft register is where to look, never what to budget a piece by.** Each register section is replaced by the
verified piece's result in the same unit that verifies it. *(Added 2026-11-04, `M-316`/OBS-13; amendment
layer.)*

### 3 · Notices and pointers go at the END of a file

**Notices and pointers added to an existing file go at the END of the file, never the head, so no cited line
moves**, and only where a ruling permits the edit at all (`DR-101`; `DR-116` item 2). A notice sweep includes the
record and readiness-check files. *(Added 2026-11-04, `M-308`/OBS-5; amendment layer.)*

### 4 · A notice or pointer line gets a second reader

**A notice or pointer line written into an existing pass file is read by a second reader before it is committed,**
against the whole finding it touches, not only the sentence it names. Such a line is written only where a ruling
permits the edit at all (rule 3). *(Added 2026-11-04, `M-303`; amendment layer.)*
