# Jung and Enneagram extraction plan (2026-10-04)

**Developer directive, 2026-10-04:** data-extract ALL remaining materials relating to **Carl Jung** (needed in multiple contexts, settings and media, not only Inner Tepenia) and **the Enneagram**; pick up with Jung first. A separate subagent builds the shopping list of unreadable files (`Books_Shopping_List.md`, repo root).

**Progress: 38 / 38 units written (ALL DONE 2026-10-05 if equal; then see Book_Extraction_Index.md Section 4c).** Waves are 5 agents each (the library's established limit); write the files, then re-run `_tools/update_plan.py` to tick boxes.

## What was found (the survey of `to-be-integrated/books/`, 2026-10-04)

- **Zodiac: all 8 books are ALREADY extracted** (2026-08-29) into `Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/` (22 files: 12 signs, Ophiuchus, 7 thematic slices, application). Nothing to do.
- **Enneagram (10 books):** *The Wisdom of the Enneagram* Parts I and II mined; *The Complete Enneagram* (Chestnut) chapters 3 to 11 mined; *Personality Types* partly mined (see `Worldspace/Enneagram/README.md`). **NOT extracted: Rohr & Ebert, Stabile, Palmer, Blair, Whitmoyer-Ober, Hall, Gomez**, plus *Wisdom* Part III, the rest of *Personality Types*, and Chestnut's chapters 1 to 2 and back matter. Found by title and author search of the whole repo (nothing outside the Enneagram folder mentions them).
- **Jung (`Reference/Materials/books/philosophy/Carl Gustav Jung/`):** only *Man and His Symbols* is partly extracted (pp. 18 to 158). *Aion*, *Modern Man in Search of a Soul*, *Symbols of Transformation*, *Synchronicity*, *The Undiscovered Self* are untouched and have good text layers. **The two *Collected Works, Complete Digital Edition* files are 9-byte placeholders (empty).** **The *Red Book* has no text layer but its pages OCR (OCR of the whole book is in progress; see below).**
- Also in `to-be-integrated/books/`: 18 character-craft books (extracted into the DRAFT files; Warner *Building Character Arcs* is not, and Lauther's depth is unknown), 12 programming books, `PTSD/` (extracted), `x-trash/` (science and some craft duplicates), plus *Sixguns and Society* (Wright) and *The Biology of Horror* (Morgan), which appear only on the Weekly To-Do.

## Where things go

- Jung: `Reference/Real-World/Jung_Extractions/<Book>_Extraction_PartNN_of_MM.md` (one file per part).
- Enneagram: `Worldspace/Enneagram/Source_Book_Extractions/<Book>_Extraction_PartNN_of_MM.md` (new folder; the Enneagram README is NOT edited; adding a row for these is a pending suggestion).
- Every file is research, not canon. Agent rules: `_AGENT_INSTRUCTIONS.md`. Index rows: `Reference/Real-World/Book_Extraction_Index.md` (add rows when units finish).

## How to resume (after a window reset)

```bash
cd "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD"
python3 Reference/Real-World/Jung_Extractions/_tools/update_plan.py   # ticks boxes from the files on disk; prints the next wave
```
The agents read page-marked text copies in `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/462f6b67-5cf4-4e6a-9bd4-27aaf5e5b77e/scratchpad/text`. **If that directory is gone**, rebuild it: `python3 Reference/Real-World/Jung_Extractions/_prep_text.py <out_dir>` (all sources except the Red Book), then set `TEXTDIR` to that directory when running `update_plan.py` and use it in the agent assignments. Unit definitions (line ranges) are in `_tools/units.json`; if you rebuild the text, line numbers may differ slightly, so rebuild units with `_tools/build_units.py` (edit its `S` path first).

**Dispatch rule:** `general-purpose` subagents, background, **5 per wave**; each agent gets: its unit row below, the shared `_AGENT_INSTRUCTIONS.md`, the text file and line range, the original source path, and the exact output path. Before re-dispatching any unit after a reset: run `ListAgents` and check the output file (an agent reported as failed may be suspended).

## Waves

### Wave 1 ✅

| | Unit | Book and part | Range | Words | Output |
|---|---|---|---|---:|---|
| [x] | **J01** | Aion: Researches into the Phenomenology of the Self (Collected (part 1/3) | PDF p.1-137 (lines 2-6391) | 51,682 | `aion_Extraction_Part01_of_03.md` |
| [x] | **J02** | Aion: Researches into the Phenomenology of the Self (Collected (part 2/3) | PDF p.138-239 (lines 6392-11538) | 43,592 | `aion_Extraction_Part02_of_03.md` |
| [x] | **J03** | Aion: Researches into the Phenomenology of the Self (Collected (part 3/3) | PDF p.240-374 (lines 11539-17754) | 37,483 | `aion_Extraction_Part03_of_03.md` |
| [x] | **J04** | Modern Man in Search of a Soul (part 1/2) | EPUB s.1-2 (lines 2-507) | 37,734 | `modern_man_Extraction_Part01_of_02.md` |
| [x] | **J05** | Modern Man in Search of a Soul (part 2/2) | EPUB s.3-4 (lines 508-1019) | 48,475 | `modern_man_Extraction_Part02_of_02.md` |

### Wave 2 ✅

| | Unit | Book and part | Range | Words | Output |
|---|---|---|---|---:|---|
| [x] | **J06** | Symbols of Transformation (Collected Works vol. 5) (part 1/5) | PDF p.1-210 (lines 2-7256) | 44,135 | `symbols_of_transformation_Extraction_Part01_of_05.md` |
| [x] | **J07** | Symbols of Transformation (Collected Works vol. 5) (part 2/5) | PDF p.211-448 (lines 7257-13939) | 42,818 | `symbols_of_transformation_Extraction_Part02_of_05.md` |
| [x] | **J08** | Symbols of Transformation (Collected Works vol. 5) (part 3/5) | PDF p.449-653 (lines 13940-21344) | 45,392 | `symbols_of_transformation_Extraction_Part03_of_05.md` |
| [x] | **J09** | Symbols of Transformation (Collected Works vol. 5) (part 4/5) | PDF p.654-979 (lines 21345-33774) | 40,070 | `symbols_of_transformation_Extraction_Part04_of_05.md` |
| [x] | **J10** | Symbols of Transformation (Collected Works vol. 5) (part 5/5) | PDF p.980-1273 (lines 33775-44734) | 42,692 | `symbols_of_transformation_Extraction_Part05_of_05.md` |

### Wave 3 ✅

| | Unit | Book and part | Range | Words | Output |
|---|---|---|---|---:|---|
| [x] | **J11** | Synchronicity: Nature and Psyche in an Interconnected Universe (part 1/1) | PDF p.1-163 (lines 2-5768) | 49,261 | `Cambray_Synchronicity_Study_Extraction.md` |
| [x] | **J12** | The Undiscovered Self (with Symbols and the Interpretation of  (part 1/1) | EPUB s.1-23 (lines 2-1524) | 54,633 | `undiscovered_self_Extraction_Part01_of_01.md` |
| [x] | **J13** | Man and His Symbols (REMAINING sections) (part 1/2) | PDF p.156-232 (lines 6254-10013) | 107,954 | `man_and_his_symbols_Extraction_Part01_of_02.md` |
| [x] | **J14** | Man and His Symbols (REMAINING sections) (part 2/2) | PDF p.228-319 (lines 9801-14440) | 148,078 | `man_and_his_symbols_Extraction_Part02_of_02.md` |
| [x] | **J15** | The Red Book: Liber Novus, English translation and apparatus ( (part 1/5) | PDF p.224-264 (lines 2-2823) | 46,098 | `redbook_Extraction_Part01_of_05.md` |

### Wave 4 ✅

| | Unit | Book and part | Range | Words | Output |
|---|---|---|---|---:|---|
| [x] | **J16** | The Red Book: Liber Novus, English translation and apparatus ( (part 2/5) | PDF p.265-297 (lines 2824-5124) | 45,867 | `redbook_Extraction_Part02_of_05.md` |
| [x] | **J17** | The Red Book: Liber Novus, English translation and apparatus ( (part 3/5) | PDF p.298-330 (lines 5125-7597) | 46,904 | `redbook_Extraction_Part03_of_05.md` |
| [x] | **J18** | The Red Book: Liber Novus, English translation and apparatus ( (part 4/5) | PDF p.331-364 (lines 7598-9972) | 45,235 | `redbook_Extraction_Part04_of_05.md` |
| [x] | **J19** | The Red Book: Liber Novus, English translation and apparatus ( (part 5/5) | PDF p.365-383 (lines 9973-11394) | 26,415 | `redbook_Extraction_Part05a_of_05.md` |
| [x] | **J20** | The Red Book: Liber Novus, English translation and apparatus ( (part 5/5) | PDF p.384-402 (lines 11395-12464) | 18,424 | `redbook_Extraction_Part05b_of_05.md` |

### Wave 5 ✅

| | Unit | Book and part | Range | Words | Output |
|---|---|---|---|---:|---|
| [x] | **E01** | The Enneagram: A Christian Perspective (part 1/3) | PDF p.1-66 (lines 2-2761) | 40,577 | `rohr_ebert_Extraction_Part01_of_03.md` |
| [x] | **E02** | The Enneagram: A Christian Perspective (part 2/3) | PDF p.67-127 (lines 2762-5776) | 44,754 | `rohr_ebert_Extraction_Part02_of_03.md` |
| [x] | **E03** | The Enneagram: A Christian Perspective (part 3/3) | PDF p.128-206 (lines 5777-9532) | 35,242 | `rohr_ebert_Extraction_Part03_of_03.md` |
| [x] | **E04** | The Path Between Us: An Enneagram Journey to Healthy Relations (part 1/1) | PDF p.1-191 (lines 2-6124) | 49,218 | `stabile_Extraction_Part01_of_01.md` |
| [x] | **E05** | The Enneagram in Love and Work: Understanding Your Intimate an (part 1/3) | PDF p.1-184 (lines 2-7570) | 48,040 | `palmer_Extraction_Part01_of_03.md` |

### Wave 6 ✅

| | Unit | Book and part | Range | Words | Output |
|---|---|---|---|---:|---|
| [x] | **E06** | The Enneagram in Love and Work: Understanding Your Intimate an (part 2/3) | PDF p.185-323 (lines 7571-13573) | 42,282 | `palmer_Extraction_Part02_of_03.md` |
| [x] | **E07** | The Enneagram in Love and Work: Understanding Your Intimate an (part 3/3) | PDF p.324-440 (lines 13574-18413) | 34,677 | `palmer_Extraction_Part03_of_03.md` |
| [x] | **E08** | The Enneagram for Relationships: A Guide to Personality Types  (part 1/1) | EPUB s.1-33 (lines 2-1146) | 35,622 | `blair_Extraction_Part01_of_01.md` |
| [x] | **E09** | The Enneagram for Relationships: Transform Your Connections wi (part 1/1) | EPUB s.1-50 (lines 2-1595) | 38,184 | `whitmoyer_ober_Extraction_Part01_of_01.md` |
| [x] | **E10** | The Enneagram in Love: A Roadmap for Building and Strengthenin (part 1/1) | EPUB s.1-79 (lines 2-1684) | 36,032 | `hall_Extraction_Part01_of_01.md` |

### Wave 7 ✅

| | Unit | Book and part | Range | Words | Output |
|---|---|---|---|---:|---|
| [x] | **E11** | The Enneagram: Understand Your Personality Type and How It Can (part 1/1) | EPUB s.1-22 (lines 2-7051) | 58,080 | `gomez_Extraction_Part01_of_01.md` |
| [x] | **E12** | Personality Types: Using the Enneagram for Self-Discovery (part 1/4) | EPUB s.2-15 (lines 2-1339) | 51,662 | `personality_types_Extraction_Part01_of_04.md` |
| [x] | **E13** | Personality Types: Using the Enneagram for Self-Discovery (part 2/4) | EPUB s.16-18 (lines 1340-2308) | 47,737 | `personality_types_Extraction_Part02_of_04.md` |
| [x] | **E14** | Personality Types: Using the Enneagram for Self-Discovery (part 3/4) | EPUB s.19-21 (lines 2309-3271) | 45,479 | `personality_types_Extraction_Part03_of_04.md` |
| [x] | **E15** | Personality Types: Using the Enneagram for Self-Discovery (part 4/4) | EPUB s.22-32 (lines 3272-6799) | 43,123 | `personality_types_Extraction_Part04_of_04.md` |

### Wave 8 ✅

| | Unit | Book and part | Range | Words | Output |
|---|---|---|---|---:|---|
| [x] | **E16** | The Wisdom of the Enneagram, PART III (Chapters 16-17, the spi (part 1/1) | PDF p.351-401 (lines 17431-19923) | 21,741 | `wisdom_part3_Extraction_Part01_of_01.md` |
| [x] | **E17** | The Complete Enneagram: 27 Paths to Greater Self-Knowledge, FR (part 1/2) | PDF p.1-57 (lines 1-1845) | 19,732 | `chestnut_front_Extraction_Part01_of_02.md` |
| [x] | **E18** | The Complete Enneagram, BACK MATTER after Chapter 11 (conclusi (part 2/2) | PDF p.363-449 (lines 13373-16555) | 34,569 | `chestnut_back_Extraction_Part02_of_02.md` |

## IF THE SESSION IS INTERRUPTED (window limit, 2026-10-04 to 05): restart checklist

1. `cd` to the repo, run `python3 Reference/Real-World/Jung_Extractions/_tools/update_plan.py` (ticks boxes from the files on disk).
2. Run `ListAgents` and look at each unit's output file. An agent shown as failed/limit-hit may be SUSPENDED and still write its file; do not re-dispatch a unit whose file exists or whose agent is alive.
3. Keep at most 5 extraction agents running at once (Jung first, then Enneagram). Start the next not-done units from the wave table; the prompt pattern is: read `_AGENT_INSTRUCTIONS.md`, then the unit's text file + line range + source path + output path (see `_tools/units.json`).
4. **OCR jobs are killed by an interruption.** Check with `pgrep -af ocr_resume` and the page counts, then resume (they append): `python3 _tools/ocr_resume.py "<Red Book pdf>" <scratch>/text/redbook_ocr/redbook.txt 1 404 --workers 3 --dpi 150` and `python3 _tools/ocr_resume.py "<Man and His Symbols pdf>" <scratch>/text/man_and_his_symbols_ocr.txt 156 319 --workers 3 --dpi 200 --psm 1`.
5. **J13 and J14 (Man and His Symbols) must read the OCR text**, `<scratch>/text/man_and_his_symbols_ocr.txt` (NOT `man_and_his_symbols.txt`: its text layer is letter-spaced with no word boundaries and interleaved columns). Find each unit's page range with the `=== PDF PAGE n (OCR) ===` markers: J13 = PDF pp. 156-232 (von Franz, 'The Process of Individuation'); J14 = pp. 228-319 (Jaffe and Jacobi, to the end).
6. **Other open items:** the shopping-list subagent writes `Books_Shopping_List.md` (repo root); AFTER it finishes, add the item **Jung's OWN 'Synchronicity: An Acausal Connecting Principle' (CW 8 or the Princeton paperback)**, because the library file labeled Jung's *Synchronicity* is actually Joseph Cambray's 2009 study (extracted as `Cambray_Synchronicity_Study_Extraction.md`). Then add rows to `Book_Extraction_Index.md` (Section 4 / 4b, and the Zodiac substrate, which the index omits), mention the footnote/endnote findings below, and commit.

- **Findings so far (2026-10-04):** *Symbols of Transformation* endnotes are in its back matter (J10 captured them; chapter assignments inferred); J09 reported pp. 725-979 as bibliography/index; the PDF has no footnotes at page bottoms. Aion paragraph numbers are partly inferred (OCR damage). Agents' self-reported word counts run LOW vs. `wc -w`.

## Pending and open

- **The Red Book: CORRECTED 2026-10-04 (from the shopping-list audit).** It is NOT image-only: PDF pages 224-402 (172 pages) carry a good text layer with the full English translation; pages 14-223 are calligraphic facsimile (OCR is garbage, nothing to extract). **Do not OCR it.** Extract with `pdftotext -layout -f 224 -l 402 <Red Book pdf>`, add page markers (use `_prep_text.py` logic), split into 2-3 units of about 45,000 words, and run them as normal units. The OCR job was stopped.
- **`Man and His Symbols` units (J13, J14):** DONE; they used a clean OCR of PDF pp. 156-319 (the text layer is letter-spaced).
- **After the last wave:** add rows to `Book_Extraction_Index.md` (Sections 4 and 8), update its pick-up list, commit.
