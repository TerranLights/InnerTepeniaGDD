# STEM/Biology Cataloging Checklist

**Purpose:** resumable, granular tracking for the STEM/Biology (~160 file) cataloging pass that is the one
major gap in `Book_TOC_Master_Reference.md`. Background sub-agents kept hitting a hard weekly/session API
cap mid-run (multiple consecutive failures, 2026-07-19), so this folder is now being worked **one task at a
time, directly, sequentially** rather than via parallel agent fan-out. Update this file as each folder
completes, then fold the results into `Book_TOC_Master_Reference.md`'s STEM/Biology section.

**Status legend:** ✅ done · 🟡 in progress · ⬜ not started · (dropped) — developer said not needed

---

## Folders in scope

| # | Folder | Files | Status | Notes |
|---|---|---|---|---|
| 1 | `bioinformatics/` (top-level) | 2 | ✅ | Already deep-extracted for Vostok, see `Vostok_Genetics_Research/01_` and `02_` |
| 2 | `Genetics/DNA [Genetic] Computing/` | 12 | ✅ | Done via agent — full catalog in `Book_TOC_Master_Reference.md` |
| 3 | `Genetics/basics/` | 10 | ✅ | Done via agent |
| 4 | `Genetics/docs/` | 2 | ✅ | Done via agent (2 journal articles, incl. Adleman's 1998 Sci Am piece) |
| 5 | `Memetics/` (not under STEM/Biology, but flagged same session) | 14 | ✅ | Done via agent |
| 6 | `Genetics/nanotech/` | 4 | ✅ | Done via direct read — 3 TOCs captured, 1 (*Nanotechnology in Biology and Medicine*, Vo-Dinh) exceeds 100MB, title only |
| 7 | `Genetics/Ecological Genetics/` | 6 (5 books + 1 txt) | ✅ | Done via direct read — all 5 books captured |
| 8 | `Genetics/recombination/` | 4 | ✅ | Done via direct read — all 4 accounted for (3 read, 1 djvu duplicate unreadable) |
| 9 | `Genetics/synthetics/` | 4 | ✅ | Done via direct read — all 4 captured |
| 10 | `Genetics/forensics/` | 9 | ✅ | Done via direct read — all 9 forensic-DNA texts captured |
| 11 | `Genetics/identification/` | 5 | ✅ | Done via direct read — all 5 captured |
| 12 | `Genetics/shit for later/` | 7 | ✅ | Done via direct read — 5 read, 2 exceed 100MB (title only) |
| 13 | `Genetics/Bioinformatics/` (subfolder, distinct from #1) | 19 | ✅ | Done via direct read — 1 duplicate (skipped, already in `identification/`), 18 unique books all captured |
| 14 | `Genetics/` top-level files | 18 | ✅ | Done via direct read — all 18 books captured |
| 15 | `STEM/Biology/` top-level files | 16 | ✅ | Done via `pdftotext` (much faster than image-Read for text-layer PDFs) + salvaged partial data from the failed background agent's log. 1 file (Manga Guide to Molecular Biology) exceeds 100MB/no text layer, title only |
| 16 | `Evolutionary Studies (Biology and Psychology)/` top-level | 14 | ✅ | Done via `pdftotext`. Developer confirmed 2026-07-19 several of the sex-focused titles ("Why Women Have Sex" x2, etc.) aren't necessary to pursue deeply — light/partial cataloging only on those, no further effort spent |
| 17 | `.../The Handbook of Evolutionary Psychology, 2 Volumes` | 2 | ✅ | Done via `pdftotext` (2nd Ed, distinct from the 1st Ed single-volume also in the top-level folder) |
| 18 | `.../primates/` | 23 | (dropped) | Developer confirmed 2026-07-19: "not necessary... that's for a totally different project altogether" |
| 19 | `Why is the Penis Shaped Like That - Jesse Bering` | 2 | (dropped) | Developer confirmed 2026-07-19: "isn't necessary" |

## STATUS: ALL IN-SCOPE STEM/Biology TASKS COMPLETE (2026-07-19)

Every folder in this checklist is now ✅ or explicitly (dropped) by the developer. Fold this into
`Book_TOC_Master_Reference.md` and mark the STEM/Biology section there as fully done.

---

## Working method

1. Take the next ⬜ folder in order.
2. `ls` it if not already listed in detail above.
3. Read each file's first ~10-15 pages (small batches of Read calls per turn is fine — this isn't the
   session-limit-triggering pattern, direct main-thread Read calls have kept working throughout).
4. Flag `.epub`/`.djvu` as unreadable (title from filename only); flag anything over ~100MB as size-limit
   exceeded (title from filename only).
5. Update this checklist's status to ✅ and add a one-line note.
6. Fold the resulting catalog entries into `Book_TOC_Master_Reference.md`'s STEM/Biology section, replacing
   the placeholder text for that subfolder.
7. Move to the next ⬜ folder.

Do not re-attempt background-agent delegation for this folder tree unless the developer says the session
cap has reset — it failed twice in a row (first the original 10-way fan-out, then a second smaller-batch
attempt) with the identical "session limit" error.
