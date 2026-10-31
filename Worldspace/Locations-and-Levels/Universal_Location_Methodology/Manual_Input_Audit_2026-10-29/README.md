# Manual input audit, city by city (started 2026-10-29)

**Why.** Developer, 2026-10-29: *"go through the Pre-Trip and the instant-reference files for all the cities. Don't use a script; go one city at a time. For each city, check that (1) that city's ULM is able to access all the information it requires, and (2) every piece of that information is accurate and correct. Don't worry about doing it quickly. I want you to really check thoroughly and make sure everything is right."*

**What this is.** A hand check by reading. The earlier checks (`Tools/verify_city_sheets.py`, `check_must_open_coverage.py`, `audit_city_inputs.py`) were scripts; this audit does not use any script to decide a pass or fail. Files are opened with the Read tool, cited lines are looked up and compared by eye, and the result is written in plain words.

**What is recorded.** One file per city in this folder (`<City>_Audit.md`) and a tracker (`TRACKER.md`). Findings are only *logged* here. **No existing datasheet, Pre-Trip sheet, spec or other source is edited by this audit** unless the developer says so (standing rule: create freely, ask before changing existing files). A proposed fix is written beside each finding.

## The method for each city

**Part 1 — Can the ULM reach everything it needs?**
1. Read the city's whole Pre-Trip sheet (`00.0_Pre-Trip_Inspection.md`), section by section: A identity and aliases, B run mode, C per-step address book, D per-phase canon, E carve-outs, F exclusions, G laws, H handoff sweep, I verification block, J open rulings, and any hand-added addendum.
2. Check the alias set against the city's own spec (current name, real-world basis name, retired placeholder names, folder names that keep an old name).
3. For every address in sections C and D: confirm the file or folder really exists, is the *right* file (not a lookalike or a stub), and that the tier (mapped, withheld, queryable-by-schema, read-last) and any carve-out are right for that source.
4. Compare each phase's list against the authoritative must-open list (`00_RUNBOOK.md` §C.8c / the `📂 MUST OPEN` blocks in `03_The_Phase_Spine.md`) and against the requirement list (`ULM_Input_Required_Reference.md`: Tier 0, Tier 1 generators G1–G8, Tier 2, extent). A required input with no address, or an address with no content behind it, is a finding.
5. Check that every Pre-Trip row records *where*, never *what* (no findings, no characterization, no copied content).

**Part 2 — Is every piece of the information right?**
1. Read the city's primary sources in the original, not through the datasheet: its spec, its census rows, its composition rows, its Founding Register row, its climate file, its Division of Industry rows, its entries in the highway, airport and port files, its relationship entries, its extent row, its inspiration picks entry, its symbol assignment.
2. Read all 19 datasheets in full (`Step_-1`, `Step_0`, `Step_1_and_2`, `Step_3`, `Step_5`–`Step_10`, `Phase_2`–`Phase_10`). For every row, open the cited line and compare the value word for word (numbers, names, units, dates, quotes). A row passes only when the value matches the live line.
3. Check that the cited line is the *right* one (the city's own row, not a neighbor's), that the citation range is complete (a list cut short is a finding), and that the line numbers still land after today's edits.
4. Check each source for its own correctness where it can be checked: internal arithmetic (shares sum, counts match the census, density, retention), agreement between spec, census, composition and the other files, real-world facts at the coordinates (station name, position, climate) against the records already on disk, renamed or superseded wording, and wording that breaks a standing law (post-war content in a datasheet, another city's answers, a conclusion in a value-and-citation sheet, a founder not in the Register).
5. Anything checked only against the file on disk and not against the outside world is labelled so. A real-world fact is checked on the web only when the files cannot settle it, and the search is logged.

**Severity words.** `BLOCKS` (the run cannot proceed or would proceed on a wrong input) · `WRONG` (a value that does not match its source or reality) · `STALE` (was right, an edit since moved it) · `GAP` (a required input is missing or unreachable) · `NOTE` (cosmetic, or a decision for the developer). A pass with no finding in a row is written as checked, not left blank.

## Finished cities are in scope too (developer, 2026-10-29)
*"Don't forget to check the cities we've already done, because things might possibly have changed since then."* Davis, Mirny, Shirayuki, Sinheung, both Zhongshan folders and Concordia are audited for **drift since their pass was run** (rows 35–39 and rows 4 and 6 of `TRACKER.md`): the city's spec, census rows, composition rows, climate, Division of Industry row, highway/airport/port entries, Founding Register row, and every ruling made after the pass. Finished pass files are never edited; the ledger records an `AMEND` note for each. Any Pre-Trip or datasheet that exists for them is checked the usual way.

## The fix ledger and the final sweep (developer instruction, 2026-10-29)
Every edit a city needs is written into **`FIX_LEDGER.md`** (one section per city, plus a shared section) **as soon as it is found**. **No sheet or source is edited during the audit.** After the last city is checked, **one sweep applies everything** in the order the ledger states (decisions, source fixes, builder text, values/rewording/additions, line re-pointing last). **Anything that needs the developer's attention is logged as `DECIDE` and settled at the sweep** (developer: *"if there's anything that requires my attention, we'll address that during the sweep at the end"*): the audit does not stop to ask.

## Rules this audit keeps
- One city at a time; never compare one city with another in a city's file. Shared files are read for that city's own rows only.
- Withheld and read-last material (the city's own culture sheets, megasheets, reserved questions) is **not opened**; the audit confirms only that the Pre-Trip and datasheets handle it correctly.
- American English. No commit unless the developer asks.
- The audit reads any hour (it is source checking, not a ULM pass), but it never writes culture or derivation about a place.
