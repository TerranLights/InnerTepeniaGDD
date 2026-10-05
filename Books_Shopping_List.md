# Inner Tepenia — Books Shopping List

Books whose **file is present in the library but holds no usable data**. Counterpart to `Books_TODO.md` (which lists
books never acquired); this file lists books that were "acquired" but are broken. Built 2026-10-04 from an automated
audit of all 2,444 library files, then verified by hand. Nothing here is canon; it is an acquisition worklist.

Roots audited: `Reference/Materials/books/` and `to-be-integrated/books/`.

---

## 1. Summary

**Audit counts (2,444 files):**

| Status | Files | Meaning |
|---|---:|---|
| OK | 2,292 | Has a text layer (or EPUB/DjVu text) |
| SCAN_OCR_OK | 86 | No text layer, but OCR of sampled pages works |
| OTHER | 44 | Not text-audited (38 zips, 4 AZW3, 2 MOBI) |
| STUB | 16 | Under 2 KB (2 Jung placeholders, 14 tiny source-code zips) |
| EMPTY | 6 | No text layer and sampled OCR returned almost nothing (5 titles; one is a duplicate copy) |
| CORRUPT / EPUB_EMPTY / DJVU_NOTEXT | 0 / 0 / 0 | None found |

**Result: the shopping list is short. One title is genuinely missing: the two 9-byte *Collected Works of C. G. Jung,
Complete Digital Edition* placeholders (P1).** Every other flagged file turned out to be readable by eye, a legitimate
tiny archive, or already replaced by a second copy. **The Red Book is not a shopping-list item** (see section 3).

**Verified by hand (all of the following were opened, rendered, listed or header-checked, not judged from the CSV):**
all 6 EMPTY files; all 16 STUB files (the 14 zips were opened and tested); all 44 OTHER files (38 zips tested with
`zipfile`, the 6 MOBI/AZW3 files header-checked for DRM and text length); the Red Book (every page's text-layer status
counted, 12 pages rendered and read, translation pages compared against fresh OCR); 8 of the 86 SCAN_OCR_OK files
(re-OCRed at a middle page); plus a new full-page pass over all 2,097 "OK" PDFs (see section 5) that surfaced 23 files
worth a second look, of which 6 were examined by eye.

**Two audit findings that corrected earlier notes in the repo:**
- `Reference/Real-World/Jung_Extractions/EXTRACTION_PLAN_2026-10-04.md` says the Red Book "has no text layer." That is
  true of the 223 facsimile pages only; **172 pages carry a text layer** (the whole typeset English translation).
- `Reference/Real-World/Book_TOC_Master_Reference.md` (Jung section) calls the Aion EPUB "unreadable." It is not:
  the EPUB holds about 775,000 characters of text (326 files, Princeton CW vol. 9 markup) and the audit marks it OK.

---

## 2. THE SHOPPING LIST

| Priority | Title | Author | Edition / year | Current file path (relative to repo root) | What is wrong | What to acquire | Replacement already present? |
|---|---|---|---|---|---|---|---|
| **P1** | *The Collected Works of C. G. Jung* (Bollingen Series XX), "Complete Digital Edition" | C. G. Jung; trans. R. F. C. Hull; eds. Sir Herbert Read, Michael Fordham, Gerhard Adler, William McGuire | Princeton University Press, 20 volumes (incl. Vol. 19 General Bibliography and Vol. 20 General Index), 1953 to 1979 (print); digital edition of the same set | `Reference/Materials/books/philosophy/Carl Gustav Jung/The Collected Works of C.G. Jung - Complete Digital Edition/The Collected Works of C.G. Jung - Complete Digital Edition.epub` and `.../The Collected Works of C.G. Jung - Complete Digital Edition.pdf` | Both files are 9-byte placeholders (a failed download). No data. | The full 20-volume set, or at minimum the volumes in the breakdown below. Buy the Princeton University Press print or e-book volumes, or borrow from a library. (A library catalog lists ISBN 9781400851065 for the Bollingen XX e-book; confirm before ordering.) | **Partly.** Only CW 5 and CW 9 part ii are in the library (see breakdown). The set as a whole is not. |

### Collected Works: what the library already holds, and what to buy first

"Present" means a readable, complete-looking file exists elsewhere in the library under the Jung folder.

| CW vol. | Title | In library? | Priority | Why it matters here |
|---|---|---|---|---|
| 5 | *Symbols of Transformation* | **Present**: `Reference/Materials/books/philosophy/Carl Gustav Jung/Symbols of Transformation - Jung, Carl Gustav [1952].pdf` (1,273 pp, Hull translation, good text layer) | none needed | Extraction plan units J06 to J10 |
| 9 pt. ii | *Aion: Researches into the Phenomenology of the Self* | **Present** in three files under `.../Carl Gustav Jung/Aion-- researches into the phenomenology of the self/` (EPUB, a 363 pp PDF, and a 374 pp "Collected Works... Aion" PDF) | none needed | Already being extracted (J01 to J03) |
| 9 pt. i | *The Archetypes and the Collective Unconscious* | **Absent** | **P1, first** | The archetype texts (Shadow, Anima/Animus, Self, Mother, Trickster, Persona). Anchors the archetype layer the extraction plan only reaches secondhand through *Man and His Symbols* |
| 6 | *Psychological Types* | **Absent** | **P1** | The type system (introversion/extraversion, four functions); the library has only the short essay "A Psychological Theory of Types" inside *Modern Man in Search of a Soul* |
| 7 | *Two Essays on Analytical Psychology* | **Absent** | **P1** | Persona, anima/animus, collective unconscious, individuation in Jung's own compact form |
| 8 | *The Structure and Dynamics of the Psyche* | **Absent** | **P1** | Contains "On the Nature of the Psyche," "The Transcendent Function," and the "Synchronicity: An Acausal Connecting Principle" essay. **Note: the file in the library named *Synchronicity ... Carl Gustav Jung.pdf* is by Joseph Cambray (2009), not Jung**, so Jung's own synchronicity text is absent |
| 12 | *Psychology and Alchemy* | **Absent** | **P1** | Individuation symbolism, mandalas, dream series; feeds the symbol and transformation material |
| 14 | *Mysterium Coniunctionis* | **Absent** | **P1** | Alchemical union of opposites; the capstone of the late work |
| 11 | *Psychology and Religion: West and East* | **Absent** | **P1** | Relevant to the robot-religion and belief-consequence work (Answer to Job, the Trinity, Eastern texts) |
| 13 | *Alchemical Studies* | **Absent** | P1 (after the above) | Alchemy, the Philosophical Tree, commentary on *The Secret of the Golden Flower* |
| 10 | *Civilization in Transition* | **Partly**: *The Undiscovered Self* (EPUB, Princeton 2010) reprints its title essay; the rest is absent | P1 (lower) | Essays on society, mass-mindedness, flying saucers, the modern West |
| 16, 17 | *The Practice of Psychotherapy*; *The Development of Personality* | **Absent** | P1 (lower) | Transference, the stages of life, child and family psychology |
| 15 | *The Spirit in Man, Art, and Literature* | **Absent** | P1 (lower) | Psychology and poetry, Joyce's *Ulysses*, Picasso |
| 18 | *The Symbolic Life: Miscellaneous Writings* | **Absent** | P1 (lower) | Late, accessible essays and seminars |
| 19, 20 | *General Bibliography*; *General Index* | **Absent** | P1 (reference only) | Needed only to resolve CW cross-references and section numbers (§) cited throughout the library's Jung material |
| 1 to 4 | Psychiatric Studies; Experimental Researches; Psychogenesis of Mental Disease; Freud and Psychoanalysis | **Absent** | P3 | Early clinical and Freud-era work; low value for this project |

Items from Jung's own pen that are **not** in the Collected Works and are also absent from the library: *Memories,
Dreams, Reflections* (Jung and Aniela Jaffe), the *Black Books* (Philemon Series), and the seminar volumes. These are
outside the scope of this audit and listed only so they are not mistaken for the Collected Works.

---

## 3. Present but needs OCR / only readable by eye (NOT on the shopping list; no purchase needed)

### 3a. The Red Book, and the other files the audit flagged EMPTY

| File | Verdict | What is and is not recoverable |
|---|---|---|
| `Reference/Materials/books/philosophy/Carl Gustav Jung/The Red Book-- Liber Novus - Carl Gustav Jung.pdf` (404 pp, 154 MB; *The Red Book: Liber Novus*, ed. Sonu Shamdasani, trans. Mark Kyburz, John Peck, Sonu Shamdasani, W. W. Norton, 2009, the large Philemon Series edition) | **NOT a shopping-list item. The English text is complete and usable. Mixed file.** | **Pages 224 to 402 (about 172 pages with a text layer; 258-259, 287-289 and 362-363 are plates or blank): the whole typeset English apparatus and translation.** Sonu Shamdasani's Introduction, Editorial Note, *Liber Primus* ("The Way of What Is to Come" through "Resolution"), *Liber Secundus* (through the "Finis" of the Draft), the *Scrutinies*, and Appendices A to C (the *Septem Sermones* are discussed and quoted in the appendix pages). `pdftotext` returns about 1.27 million characters from these pages; the text-layer quality is good (minor errors such as "grpt" for "great"), and fresh Tesseract OCR matches it (OCR is slightly better on curly quotes and Greek). Pages 6 to 13 (Preface, Acknowledgments) are typeset with no text layer and OCR cleanly. **Not recoverable as text: pages 14 to 223 (about 210 pages), the facsimile of Jung's calligraphic manuscript.** These are full-page paintings and Gothic-style German calligraphy; OCR returns garbage (confirmed on pages 20 and 25). Readable only by a person who reads that script. This costs nothing in English content, because the same passages are translated in the typeset section (*Liber Primus* and *Liber Secundus*), which also gives the folio numbers for matching a translation to its facsimile page. The images themselves (the paintings) are art, not data. **Do not run a full-book OCR from page 1: pages 1 to 223 are wasted effort.** Use `pdftotext` on pages 224 to 402 and OCR on pages 6 to 13. Optional, not needed: the Norton *Reader's Edition* (ISBN 9780393089080) is a cleaner text-only version. |
| `Reference/Materials/books/music theory and composition/The Study of Orchestration - Samuel Adler (3rd Ed) [2002].pdf` (852 pp; W. W. Norton, 3rd ed., 2002) | Readable by eye, OCR-hostile (page 300 viewed) | A scan of a book that is half music notation (score excerpts); the text is legible, the notation is not text-recoverable and never will be. A small dark spine shadow runs down the left edge. OCR of body text gives ~250 chars/page because most pages are scores. No purchase needed. |
| `Reference/Materials/books/STEM/CSIT/Software Engineering/Essentials-Of-Software-Engineering [3rd Ed].pdf` (333 pp; Frank Tsui, Orlando Karam, Barbara Bernal; Jones & Bartlett, 3rd ed.) | Readable by eye, OCR-hostile (page 100 viewed: sharp, clean text) | The page is stored at a tiny nominal size (127 x 157 pt) so the audit's 150 dpi OCR returned nothing. Re-rendered at 400 dpi, OCR works on body pages; preface pages OCR poorly. Fully legible by eye. |
| `Reference/Materials/books/STEM/CSIT/interviews/Dynamic Programming for Coding Interviews-- A Bottom-Up Approach to Problem Solving - Meenakshi, Kamal Rawat [2017].pdf` (136 pp; Notion Press, 2017) | Readable by eye; OCR works at 200 dpi (page 60 OCR returned full prose) | Same cause: small nominal page size starved the audit's OCR. No purchase needed. |
| `Reference/Materials/books/STEM/CSIT/AWS/gen/Hardening-AWS-Environments-And-Automating-Incident-Response-For-AWS-Compromises.pdf` (95 pp) | Readable by eye (page 30 viewed) | A slide deck exported from a browser (Skia/PDF). Slides carry little text and screenshots; the audit's low character count is real content density, not damage. No purchase needed. |
| `Reference/Materials/books/STEM/math/Linear Algebra Books/Basic Linear Algebra  (2nd Ed).pdf` and the identical copy at `.../STEM/math/algebra/linear algebra/Basic Linear Algebra  (2nd Ed).pdf` (T. S. Blyth and E. F. Robertson, Springer Undergraduate Mathematics Series, 2nd ed.) | **The PDF is a 1-page cover only (271 KB): genuinely empty. But a replacement is already present.** | **Replacement already present:** `Reference/Materials/books/STEM/math/Linear Algebra Books/Basic Linear Algebra  (2nd Ed).djvu` (245 pages, about 340,000 characters of text, same title and edition; a byte-identical copy is in `.../STEM/math/algebra/linear algebra/`). Not a shopping item. The cover-only PDFs can be ignored. |

### 3b. Partly image-only pages found by the new full-page pass (no purchase needed)

The audit samples a few pages; it cannot see a book whose text layer covers only part of it (the Red Book is exactly
that case). A full pass over all 2,097 "OK" PDFs counted pages with under 40 characters of text:

| File | Pages without text | Verdict |
|---|---|---|
| `Reference/Materials/books/STEM/Neuroscience/Principles_of_Neurobiology_-_Liqun_Luo_(1st_Ed)_[2016].pdf` | 504 of 694 | **Real finding.** Interleaved image-only pages (page 30 viewed: full typeset body text with a figure, no text layer); the "Further reading" and index pages have text. Needs OCR for about 73 percent of the book; readable by eye. Not a purchase. |
| `Reference/Materials/books/music theory and composition/Adam Kadmon Grimoire series/The Keyboard Grimoire A Complete Guide for the Guitarist and Keyboardist by Adam Kadmon.pdf` | 109 of 206 | Chord diagrams and keyboard graphics by nature (the sibling Grimoire PDFs are already in the SCAN_OCR_OK list). Not viewed page by page. |
| The C++/Linux group: `C-Templates-The-Complete-Guide.pdf` (three copies), `Ubuntu_Unleashed_2019...` (two copies), `Embedded Linux Systems with the Yocto Project`, `Linux_Essentials_for_Cybersecurity`, `A Practical Guide to Linux Commands`, `Beyond-the-C++-Standard-Library...Boost` (two copies), `CompTIA Linux+ XK0-004`, `Effective_C++_Digital_Collection`, `Mastering-Linux-Kernel-Development`, `Learn C the Hard Way`, `Deep-Learning-with-TensorFlow`, `Blockchain-Easiest-Ultimate-Guide`, `Mastering Linux Shell Scripting`, `24 Patterns for Clean Code`, `From Mathematics to Generic Programming`, `C++ Programming ... Malik (8th Ed)` | 25 to 62 percent of pages each | Almost certainly web-to-PDF page-break overflow: the text exists but runs over onto a page that carries only a line or two of code (two such pages viewed in *C++ Templates* and *Effective C++*: each showed 1 to 4 lines of code and nothing else). Text is intact. Not a purchase. Not every file in this group was viewed. |

### 3c. The 86 SCAN_OCR_OK files

All 86 are PDFs with no text layer but OCR that works. They are mostly STEM/programming titles, the Thomas Sowell
set, Schopenhauer's *World as Will and Representation* (2 vols), Joseph Campbell's *Masks of God* Vol. 3, Moore and
Gillette's *King, Warrior, Magician, Lover*, Brown's *Human Universals*, Seger's *Creating Unforgettable Characters*,
Will Wright's *Sixguns and Society*, and the Adam Kadmon guitar books. **Eight were re-OCRed by hand at a middle page
(King-Warrior-Magician-Lover 844 words, Human Universals 427, Masks of God 574, Schopenhauer 501, Creating Unforgettable
Characters 748, Buddhist Analysis of Matter 190, Sixguns and Society 266, Patterns in the Mind 399): all usable.** None
needs buying; all would only benefit from a one-time OCR pass if their text is ever extracted. The full list is in the
audit CSV (status `SCAN_OCR_OK`).

### 3d. Flagged by size but legitimate

- **14 "STUB" zips** under `Reference/Materials/books/STEM/CSIT/Cpp/basics/Bartosz Milewski - C++ In Action, Industrial Strength Programming/source code/`
  (`Input.zip`, `Stack.zip`, `calc1.zip`, `ctree.zip`, `dynstack.zip`, `hash.zip`, `list.zip`, `seq.zip`, `stubs.zip`,
  `string.zip`, `tree.zip`, `value.zip`, `world1.zip`, `worlds.zip`): each is a valid zip (1 to 5 source files, 1 to 5 KB
  uncompressed). They are small code samples, not failed downloads.
- **38 other zips** (AWS exercise files, C++ and JavaScript project code, Ansible source code, the two World Geologic Atlas
  sheet images, *Tidy Text Mining*, *Tyrannical Minds* PDF+EPUB with a 317-page, 684,000-character PDF inside) all passed
  `zipfile` integrity testing.
- **6 MOBI/AZW3 files** (*Hacking with Kali Linux*, *Power User Guide: Linux Tricks*, *CentOS 7 Server Deployment Cookbook*,
  *CISSP in 21 Days*, *Our Mathematical Universe* in AZW3 and in MOBI): valid `BOOKMOBI` headers, encryption flag 0 (no
  DRM), 198 KB to 5.5 MB of text each. Text was not extracted and read; header only.

---

## 4. Could not verify

- **Completeness of books.** This audit checks for no-data files, not for truncated or incomplete books (a book with
  its last chapters missing looks "OK"). Not checked. **One truncation was found afterward, by the extraction of the Red
  Book (2026-10-05): the library's Red Book PDF ends mid-sentence in Appendix C at PDF p.402 (pp.403 and 404 are a blank page
  and the back cover), so the tail of the book (the rest of Appendix C and any notes, bibliography and index) is missing from
  this copy. The English text through the *Scrutinies* and Appendices A and B is complete.** Not a purchase for the visionary
  text; a complete copy (for example the Norton *Reader's Edition*, ISBN 9780393089080, if its scope matches) would restore the
  apparatus. Other books may be truncated in the same way and were not checked.
- **Three PDFs timed out in the full-page pass** (300 s each): *C++ Crash Course* (Josh Lospinoso, 2019) and two copies of
  Carey's *Organic Chemistry* (10th ed.). They passed the original audit's sampling; their full-page status is unknown.
- **The 2,292 "OK" files** rest on the audit's page sampling (plus, for PDFs, the new full-page blank-page count).
  EPUB and DjVu "OK" results (155 and 40 files) were not re-checked beyond the Aion EPUB and one spot check.
- **Not every file in the 3b C++/Linux group was viewed.** Two pages from two files were viewed; the rest are inferred.
- **MOBI/AZW3 text** was header-checked only, not read.
- **Keyboard Grimoire** (3b) was not viewed page by page.
- **Bibliographic details** for the Collected Works volumes and the Red Book come from the files' own metadata and
  first pages, plus one web lookup each for the Bollingen series structure and the Norton ISBN. The e-book ISBN above is
  from a library catalog listing and its exact scope (single volume or set) was not confirmed.
- **Edition years** for the Tsui/Karam/Bernal and Adler books are not printed on the pages I read; confirm the exact year
  and publisher before buying a replacement (neither needs one).

---

## 5. How the audit was done

An automated script walked every file under the two library roots (2,444 files) and classified it: PDFs by
`pdfinfo`/`pdftotext` (text layer present, characters per page on sampled pages, falling back to Tesseract OCR of
sampled pages at 150 dpi if there is no text layer); EPUBs by unzipping and counting text; DjVu by `djvutxt`; files under
2 KB as STUB; unopenable files as CORRUPT; zips, MOBI and AZW3 as OTHER (not audited). The results are in
`/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/462f6b67-5cf4-4e6a-9bd4-27aaf5e5b77e/scratchpad/audit.csv`
(columns: path, size, ext, status, detail), produced by `.../scratchpad/audit.py`; a copy of the script is kept in the
repo at `Reference/Real-World/Jung_Extractions/_tools/audit_library.py`. The CSV lives in a session scratch directory
and may be gone after a reset; re-run the script to regenerate it. The hand verification and the full-page blank-page
pass (`fullpass.py`, `fullpass.csv`, same scratch directory) were added on top of the audit afterward; the latter's
method is simply "run `pdftotext` on every page of every OK PDF and count pages with fewer than 40 characters."
