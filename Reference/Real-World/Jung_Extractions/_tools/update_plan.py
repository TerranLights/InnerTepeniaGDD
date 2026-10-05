#!/usr/bin/env python3
"""update_plan.py -- (re)write EXTRACTION_PLAN_2026-10-04.md from _tools/units.json and the files that exist on disk.

A unit counts as DONE when its output file exists and is over 3,000 bytes. Run after every wave:
    python3 Reference/Real-World/Jung_Extractions/_tools/update_plan.py
Prints the next wave (up to 5 not-done units, Jung first) so a fresh session knows exactly where to resume.
"""
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
UNITS = json.loads((HERE / "units.json").read_text(encoding="utf-8"))
PLAN = HERE.parent / "EXTRACTION_PLAN_2026-10-04.md"
WAVE = 5
TEXTDIR = os.environ.get("TEXTDIR", "/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/"
                                    "462f6b67-5cf4-4e6a-9bd4-27aaf5e5b77e/scratchpad/text")


def done(u):
    p = ROOT / u["out_file"]
    return p.exists() and p.stat().st_size > 3000


def main():
    order = sorted(UNITS, key=lambda u: (u["id"][0] != "J", u["id"]))
    waves = [order[i:i + WAVE] for i in range(0, len(order), WAVE)]
    nd = sum(done(u) for u in order)
    L = []
    L.append("# Jung and Enneagram extraction plan (2026-10-04)\n")
    L.append("**Developer directive, 2026-10-04:** data-extract ALL remaining materials relating to **Carl Jung** (needed in multiple "
             "contexts, settings and media, not only Inner Tepenia) and **the Enneagram**; pick up with Jung first. A separate "
             "subagent builds the shopping list of unreadable files (`Books_Shopping_List.md`, repo root).\n")
    L.append(f"**Progress: {nd} / {len(order)} units written (ALL DONE 2026-10-05 if equal; then see Book_Extraction_Index.md Section 4c).** Waves are 5 agents each (the library's established limit); "
             "write the files, then re-run `_tools/update_plan.py` to tick boxes.\n")
    L.append("## What was found (the survey of `to-be-integrated/books/`, 2026-10-04)\n")
    L.append("- **Zodiac: all 8 books are ALREADY extracted** (2026-08-29) into `Worldspace/Locations-and-Levels/Concordia-City/Districts/"
             "Zodiac_Personality_Substrate/` (22 files: 12 signs, Ophiuchus, 7 thematic slices, application). Nothing to do.")
    L.append("- **Enneagram (10 books):** *The Wisdom of the Enneagram* Parts I and II mined; *The Complete Enneagram* (Chestnut) chapters 3 to 11 "
             "mined; *Personality Types* partly mined (see `Worldspace/Enneagram/README.md`). **NOT extracted: Rohr & Ebert, Stabile, Palmer, "
             "Blair, Whitmoyer-Ober, Hall, Gomez**, plus *Wisdom* Part III, the rest of *Personality Types*, and Chestnut's chapters 1 to 2 and back matter. "
             "Found by title and author search of the whole repo (nothing outside the Enneagram folder mentions them).")
    L.append("- **Jung (`Reference/Materials/books/philosophy/Carl Gustav Jung/`):** only *Man and His Symbols* is partly extracted (pp. 18 to 158). "
             "*Aion*, *Modern Man in Search of a Soul*, *Symbols of Transformation*, *Synchronicity*, *The Undiscovered Self* are untouched and have "
             "good text layers. **The two *Collected Works, Complete Digital Edition* files are 9-byte placeholders (empty).** "
             "**The *Red Book* has no text layer but its pages OCR (OCR of the whole book is in progress; see below).**")
    L.append("- Also in `to-be-integrated/books/`: 18 character-craft books (extracted into the DRAFT files; Warner "
             "*Building Character Arcs* is not, and Lauther's depth is unknown), 12 programming books, `PTSD/` (extracted), `x-trash/` (science and some craft duplicates), plus "
             "*Sixguns and Society* (Wright) and *The Biology of Horror* (Morgan), which appear only on the Weekly To-Do.\n")
    L.append("## Where things go\n")
    L.append("- Jung: `Reference/Real-World/Jung_Extractions/<Book>_Extraction_PartNN_of_MM.md` (one file per part).")
    L.append("- Enneagram: `Worldspace/Enneagram/Source_Book_Extractions/<Book>_Extraction_PartNN_of_MM.md` (new folder; the Enneagram README is "
             "NOT edited; adding a row for these is a pending suggestion).")
    L.append("- Every file is research, not canon. Agent rules: `_AGENT_INSTRUCTIONS.md`. Index rows: `Reference/Real-World/Book_Extraction_Index.md` "
             "(add rows when units finish).\n")
    L.append("## How to resume (after a window reset)\n")
    L.append("```bash\ncd \"" + str(ROOT) + "\"\npython3 Reference/Real-World/Jung_Extractions/_tools/update_plan.py   # ticks boxes from the files on disk; prints the next wave\n```")
    L.append(f"The agents read page-marked text copies in `{TEXTDIR}`. **If that directory is gone**, rebuild it: "
             "`python3 Reference/Real-World/Jung_Extractions/_prep_text.py <out_dir>` (all sources except the Red Book), then set `TEXTDIR` "
             "to that directory when running `update_plan.py` and use it in the agent assignments. Unit definitions (line ranges) are in "
             "`_tools/units.json`; if you rebuild the text, line numbers may differ slightly, so rebuild units with `_tools/build_units.py` "
             "(edit its `S` path first).\n")
    L.append("**Dispatch rule:** `general-purpose` subagents, background, **5 per wave**; each agent gets: its unit row below, the shared "
             "`_AGENT_INSTRUCTIONS.md`, the text file and line range, the original source path, and the exact output path. "
             "Before re-dispatching any unit after a reset: run `ListAgents` and check the output file (an agent reported as failed may be suspended).\n")
    L.append("## Waves\n")
    for w, ws in enumerate(waves, 1):
        wd = all(done(u) for u in ws)
        L.append(f"### Wave {w} {'✅' if wd else ''}\n")
        L.append("| | Unit | Book and part | Range | Words | Output |\n|---|---|---|---|---:|---|")
        for u in ws:
            rng = f'{"PDF p." if u["label"] == "p" else "EPUB s."}{u["first"]}-{u["last"]} (lines {u["line_start"]}-{u["line_end"]})'
            L.append(f'| {"[x]" if done(u) else "[ ]"} | **{u["id"]}** | {u["title"][:62]} (part {u["part"]}/{u["of"]}) | {rng} | {u["words"]:,} | `{u["out_file"].split("/")[-1]}` |')
        L.append("")
    L.append("## IF THE SESSION IS INTERRUPTED (window limit, 2026-10-04 to 05): restart checklist\n")
    L.append("1. `cd` to the repo, run `python3 Reference/Real-World/Jung_Extractions/_tools/update_plan.py` (ticks boxes from the files on disk).")
    L.append("2. Run `ListAgents` and look at each unit's output file. An agent shown as failed/limit-hit may be SUSPENDED and still write its file; "
             "do not re-dispatch a unit whose file exists or whose agent is alive.")
    L.append("3. Keep at most 5 extraction agents running at once (Jung first, then Enneagram). Start the next not-done units from the wave table; "
             "the prompt pattern is: read `_AGENT_INSTRUCTIONS.md`, then the unit's text file + line range + source path + output path (see `_tools/units.json`).")
    L.append("4. **OCR jobs are killed by an interruption.** Check with `pgrep -af ocr_resume` and the page counts, then resume (they append): "
             "`python3 _tools/ocr_resume.py \"<Red Book pdf>\" <scratch>/text/redbook_ocr/redbook.txt 1 404 --workers 3 --dpi 150` and "
             "`python3 _tools/ocr_resume.py \"<Man and His Symbols pdf>\" <scratch>/text/man_and_his_symbols_ocr.txt 156 319 --workers 3 --dpi 200 --psm 1`.")
    L.append("5. **J13 and J14 (Man and His Symbols) must read the OCR text**, `<scratch>/text/man_and_his_symbols_ocr.txt` (NOT `man_and_his_symbols.txt`: its text layer is "
             "letter-spaced with no word boundaries and interleaved columns). Find each unit's page range with the `=== PDF PAGE n (OCR) ===` markers: "
             "J13 = PDF pp. 156-232 (von Franz, 'The Process of Individuation'); J14 = pp. 228-319 (Jaffe and Jacobi, to the end).")
    L.append("6. **Other open items:** the shopping-list subagent writes `Books_Shopping_List.md` (repo root); AFTER it finishes, add the item **Jung's OWN "
             "'Synchronicity: An Acausal Connecting Principle' (CW 8 or the Princeton paperback)**, because the library file labeled Jung's *Synchronicity* is actually "
             "Joseph Cambray's 2009 study (extracted as `Cambray_Synchronicity_Study_Extraction.md`). Then add rows to `Book_Extraction_Index.md` "
             "(Section 4 / 4b, and the Zodiac substrate, which the index omits), mention the footnote/endnote findings below, and commit.\n")
    L.append("- **Findings so far (2026-10-04):** *Symbols of Transformation* endnotes are in its back matter (J10 captured them; chapter assignments inferred); "
             "J09 reported pp. 725-979 as bibliography/index; the PDF has no footnotes at page bottoms. Aion paragraph numbers are partly inferred (OCR damage). "
             "Agents' self-reported word counts run LOW vs. `wc -w`.\n")
    L.append("## Pending and open\n")
    L.append("- **The Red Book: CORRECTED 2026-10-04 (from the shopping-list audit).** It is NOT image-only: PDF pages 224-402 (172 pages) "
             "carry a good text layer with the full English translation; pages 14-223 are calligraphic facsimile (OCR is garbage, nothing to "
             "extract). **Do not OCR it.** Extract with `pdftotext -layout -f 224 -l 402 <Red Book pdf>`, add page markers (use `_prep_text.py` "
             "logic), split into 2-3 units of about 45,000 words, and run them as normal units. The OCR job was stopped.")
    L.append("- **`Man and His Symbols` units (J13, J14):** DONE; they used a clean OCR of PDF pp. 156-319 (the text layer is letter-spaced).")
    L.append("- **After the last wave:** add rows to `Book_Extraction_Index.md` (Sections 4 and 8), update its pick-up list, commit.")
    PLAN.write_text("\n".join(L) + "\n", encoding="utf-8")
    nxt = [u for u in order if not done(u)][:WAVE]
    print(f"{nd}/{len(order)} done. Next wave: {', '.join(u['id'] for u in nxt) or 'none'}")


if __name__ == "__main__":
    main()
