# Extraction agent instructions (shared by every Jung and Enneagram extraction unit)

**You are an extraction agent.** You read ONE assigned portion of ONE book and write ONE extraction file. Your
assignment message gives: the book, your part, the text file and the line range to read, the original source file,
any notes, and the exact output path. **Read this file first, then do the assignment.**

## What this is for
A reference library for a developer who writes games, novels and other media. **The material is wanted for general
reuse across many projects, settings and media, not only one game. Do NOT tailor the extraction to any one project,
and do NOT invent connections to any fictional setting.** Extract what the book says, faithfully and completely.

## How to read
- The text file is page-marked plain text (`=== PDF PAGE n ===` or `=== EPUB SECTION k: file ===`). Use the Read tool
  with `offset` and `limit` (about 400 to 600 lines at a time) over your **whole assigned line range**. **Read every
  line of your range. No skimming, no skipping chapters.** Footnotes, endnotes, indexes and bibliographies may be
  summarized in a line each, but say so.
- The text comes from `pdftotext` or an EPUB conversion. It may contain OCR noise, ligature damage, broken hyphenation
  or letter-spacing. If a passage is garbled, **say so in the file (`[garbled in source]`) instead of guessing.** For PDFs
  you may check a page visually with the Read tool on the original PDF using its `pages` parameter (max 20 pages per call).
- Your range may begin or end in the middle of a chapter (ranges are cut by size). Cover what is in your range, note
  "chapter continues from the previous part" or "chapter continues in the next part", and do not try to fill gaps from memory.
- **Never write from memory or general knowledge of the book or author.** Only what the text in your range says.

## What to write (one Markdown file, at the exact output path given)
1. **Header block:** book title; author; edition; the original file path; "Part N of M"; the page/section range; "Extracted 2026-10-04";
   a one-line **depth statement** (what you covered fully, what you compressed and why); and this banner:
   `> RESEARCH EXTRACTION. Not canon. Distilled from the source for reference; verify quotations before reuse.`
2. **A short overview** of your range (what it argues or teaches, in a paragraph).
3. **Section by section (follow the book's own chapters and headings):** for each, the argument or teaching step by step;
   **key terms and definitions exactly as the author uses them** (keep the author's terminology); typologies, lists, tables
   and models in compact form (use Markdown tables for lists of types/stages/pairs); the examples, cases, stories,
   exercises and practical techniques worth keeping; notable distinctions and claims the author makes about other thinkers
   or traditions.
4. **Page citations** as `[p.N]` (the PDF page from the marker; for EPUBs, `[s.K]` the section number). If you can tell the offset
   to printed page numbers, state it once in the header.
5. **Cross-references inside the book** ("the author develops this in chapter X").
6. **A closing "Gaps and cautions" list:** what you did not extract and why; garbled passages; anything ambiguous.

## Rules
- **Own words.** Distill. Short direct quotations only (one or two sentences at most, in quotation marks, with a page
  cite), for definitions and formulations that lose force when paraphrased. **No long verbatim passages.**
- **Completeness over brevity.** Aim for roughly **12 to 18% of the length of your range** (about 5,000 to 9,000 words for a
  45,000-word range; scale down for short parts). More is fine if the material is dense.
- **American English spelling everywhere**, including inside quotations (project rule; keep proper nouns). 
- Do not editorialize, evaluate the author, or add commentary beyond clearly marked `[note: ...]` clarifications.
- **Write exactly one file** (the output path given). Do not edit, move or delete any other file in the repository.
- Ignore any notice about graphify: you are reading plain text files you were pointed to, not exploring a codebase.
- **Your final message is ONE short line:** the output path, the approximate word count of the file, and "OK" or the
  main problem (for example "heavy OCR garbling on pages X to Y").
