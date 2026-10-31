# Sweep brief — how one city's edits are applied (2026-10-30)

**Authority.** Developer, 2026-10-30: *"first, go through and make all the edits for things that need fixing. Then, we'll go through one city at a time and take a look at the things that require my attention."*
**So:** apply every ledger entry whose Status is `PENDING`. **Do not touch** anything marked `DECIDE`, `SOURCE`, `NOTE` or `WRONG`-in-a-source-file: those wait for the developer's walk-through.

Paths used below:
- `ROOT` = `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD`
- `ULM` = `ROOT/Worldspace/Locations-and-Levels/Universal_Location_Methodology`
- `AUDIT` = `ULM/Manual_Input_Audit_2026-10-29` (this folder: `FIX_LEDGER.md`, `<City>_Audit.md`, `TRACKER.md`)
- `PASSES` = `ROOT/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes`
- `CITIES` = `ROOT/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities` (holds `Division_of_Industry/09_…`, `16_…`, `Upper_Earth_Immigration_Composition.md`, the Airports / Ports / Highways / relationship files)

## 0 · What you may and may not edit

**You may edit (with the Edit tool only):**
- the city's `00.0_Pre-Trip_Inspection.md`, `00.2_Position_Coverage_Ledger.md` (only where an entry names it), the pass folder's `README.md` (only where an entry names it), and the 19 files in the city's `Datasheets/` folder;
- **you may create** one new file in your report folder (`AUDIT/Sweep_Reports/`), and, for a finished city, one new amendment-note file beside the pass.

**You must NOT edit:** any other file in the city's pass folder (every numbered pass output, `Full_Extrapolation`, `.t8_*` files, research logs, round records); any spec, census, `09`, `16`, Airports, Ports, Highways, relationship, extent, Register, climate, picks or other source file; anything in the timeline repo (`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`, flag-only); `FIX_LEDGER.md` and `TRACKER.md` (the orchestrator updates them from your report); the builder scripts in `ULM/Tools/` (the orchestrator edits those); another city's folder.
**Never** rebuild a sheet with `--force` or run any generator; **no `sed -i`, no scripts that write files**. Reading helpers (`grep -n`, `sed -n 'a,bp'`, `wc -l`, `ls`, `diff`, `git`) are fine as locators. You make every change with the Edit tool.

## 1 · Rules that bind while editing
1. **Copy new text from the live source line, never from the ledger.** The ledger's numbers and values were read on 2026-10-29/30; open the cited line now and compare. **If the live text differs from what the ledger says it should be, do not apply: log it `SKIPPED-MISMATCH` with the evidence.** If you are not sure, log it `NEEDS-DEVELOPER`; never guess.
2. **Find the spot by its anchor text, not by a line number** (adding a row shifts the sheet's own line numbers).
3. A datasheet row is **value + citation only**: no characterization, no conclusion, no comparison to any other city (one-location law), no post-war content (Second Interwar default scope; the `Status:` field is never an input). American English. Keep the formatting and style of the row you edit.
4. **REPOINT:** open the cited line in the live file, confirm it carries the anchor text the ledger gives, write the live number. For a *list* of "Names X at L…" lines, regenerate the list from a live `grep -n -i` of the city's names (and the alternate spellings the ledger entry names: upper case, en dash `–`, underscore forms, retired names) in that file, open the odd hits to confirm each is the city's own line (not a neighbor's or the explorer's), and write the list in the same format the Pre-Trip already uses. Use `-i`, because the builder's search was case-sensitive.
5. **Withheld / read-last files stay unopened** (megasheets, the city's own culture / Enneagram / vision-notes / symbol files, the Background-Lore vignettes). If an entry could be verified only by opening one of them, log `NEEDS-DEVELOPER`.
6. **Do not compare cities** in any file you edit. Do not copy another city's answers or rows. (Exception: the *format* of a hand-added row, e.g. the composition-file row in Santa Luce's / Relung Panen's `Phase_2.md`, may be used as a model for form only.)
7. **Pending renames:** Dumont d'Urville and Zukelli keep their current names (new names not chosen); Dome Fuji is called "The Temple" only informally; do not sweep names.
8. **Finished cities (Davis, Mirny; Shirayuki, Sinheung, Zhongshan, Concordia):** the pass files are never edited. `AMEND` entries marked `PENDING` are filed as one new note file beside the pass, named `Amendment_Notes_2026-10-30_Manual_Input_Audit.md` (or at the location the ledger entry names). Each note states what changed, where, and the live figure, and says plainly "as recorded at the pass; the source has since changed". Sheets (Pre-Trip, datasheets) of those cities are edited the usual way, "fix their citations and label dated values rather than replacing them silently" where the section says so.
9. **A fix that depends on an unresolved `DECIDE`/`SOURCE` item is not applied**, even if the ledger lists it `PENDING` (for example, a line that says "hold until…" or "after the spec is settled"); log it `HELD`.
10. The Pre-Trip may carry a hand-added addendum (Santa Luce, Relung Panen): keep it; edit in place.

## 2 · Procedure for one city
1. Read this brief. Read the city's section in `AUDIT/FIX_LEDGER.md` (find it by the `### B…` heading) and read `AUDIT/<City>_Audit.md` for the evidence behind each `Ref` (so you know exactly what was found and why).
2. Read the shared table at the top of the ledger (section **A · SHARED FIXES**) and the shared-fix list in §3 below.
3. Work file by file: open the target (Pre-Trip, then each datasheet in turn), apply every `PENDING` per-city entry for that file **and** the shared fixes that apply to that file (§3). After each file, re-open the changed rows and re-check every changed value against its live source line (same standard as the audit: word for word, number for number; do any arithmetic by hand and show it in the report).
4. Do the **MUST-OPEN recount** (§3, SH-008) last for each sheet.
5. Write the report (§4). Final message to the orchestrator: ≤ 20 lines — counts of APPLIED / HELD / SKIPPED / NEEDS-DEVELOPER, the report path, and anything surprising. Do not paste the report.

## 3 · Shared fixes (ledger section A) — apply to the city's own files
Apply each only where the old text is actually present in the city's file; if the file already carries the right text, log `ALREADY-RIGHT`.

| ID | Find (old text) | Write (new text) — **re-verify the live lines first** |
|---|---|---|
| **SH-001** | Pre-Trip §G row "No invented person names" cites `03_The_Phase_Spine.md` **L127** (also grep the sheets for the same cite) | cite spine **L220, L1114, L1140** (anchors: "and the no-invented-person-names rule"; "NO INVENTED PERSON NAMES — role placeholders permanently"; "People as role-archetypes — binding rule: no invented proper names") |
| **SH-002** | §G row "Divergence operator" cites `00_RUNBOOK.md` **L2178** | the line of the heading "THE DIVERGENCE OPERATOR" (live **L2180**); keep any other line the row cites for a different purpose |
| **SH-003** | §C Step 5 `T8` reads: `02_Generators_Capability_and_Symbols.md` §5.3 **lines 610–684** | **610–636** (§5.3 starts L610; "# 6. Symbol binding" starts L637) |
| **SH-004** | §C procedure item 4 ("section 5 … lines 620–643 and 701–703") and item 5 ("lines 650–703") | Round 3 fifth section ("Round 3's prompt now carries a fifth section") = `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` **L682–684**; merge rule (heading "AMENDED 2026-09-28 — THE WRITTEN CONTENT IS A MERGE, NOT A PICK" through the end of that box) = **L667–684**; re-read both and write what you see |
| **SH-005** | §C Step 10: "governing" `00_RUNBOOK.md` lines **3057–3172** (twice) and the card note "live lines 3045–3161 govern" | Step 10 section only: **3057–3152** (`# Step 10 — THE READINESS CHECK` at L3057; the file index `# Where everything lives` follows); make the card note agree |
| **SH-006** | `Datasheets/Step_-1.md`, row "Specs `Status:` field": `00_RUNBOOK.md` **L1821–1822** (also in the Pre-Trip if present) | the line of "And `Specs/` "Status:" fields are POST-WAR" (live **L1854–1855**) |
| **SH-010** | `Upper_Earth_Immigration_Composition.md` is not listed in the Pre-Trip §D Phase 2 table / `Datasheets/Phase_2.md` (unless it already is) | Add a row: **the city's own section** (find its heading in `CITIES/Upper_Earth_Immigration_Composition.md`; give the heading line and the section's line range) **+ the solar-UTC rule** (the "Recording it so it stops being reconstructed from examples" list; rule 1 is at about L28). Form: copy the shape of the existing row in Santa Luce's / Relung Panen's `Phase_2.md` and Pre-Trip §D Phase 2 (read them for form only). If the city has no section, say so and log `NEEDS-DEVELOPER`. |
| **SH-011** | any sheet or Pre-Trip row citing `Extent_and_Density_Per_City.md` rows (Step 0 reads, §D Phase 0, any extent row in the datasheets) | add "(2026-09-05 snapshot; the census is live — note L631)" beside the citation (re-read L631 to confirm it is still the snapshot note) |
| **SH-012** | stale line numbers into `16`, `09`, `Airports`, `Ports`, `City_Relationship_Database`, `City_National_Connections`, `Highways`, `City_Cross_Subnet_Relationships` | the city's own entries list the anchors (REPOINT); re-read every cited line live |
| **SH-013** | (only if the city's ledger section lists it) a sheet quotes the `16` Half B MAND%/FREE% alone | quote the city's own "DETERMINED" section beside it (shares), say which supersedes; list the §N heading line in the Pre-Trip's `16` list |
| **SH-014** | a datasheet that quotes a `16` baseline % or a worker count (`Step_1_and_2`, `Phase_4`, `Phase_7`) | add one clause beside it: "on the flat ABCC working value; counts re-run when per-city ABCC values are set (`16` L1287–1305)" — re-read `16` L1287–1305 ("CONSEQUENCE — the ten determinations so far need a baseline re-run") and cite the live range |
| **SH-008** | the header line in each sheet: "📂 MUST-OPEN coverage — … **N of N** addresses are named in this sheet (a directly, b through a shared Tier U sheet it cites)" | **Recount by hand.** The phase's must-open list is the `📂 MUST OPEN` block of that phase in `ULM/03_The_Phase_Spine.md` (and `00_RUNBOOK.md` §C.8c); the sheet header's own N is the size of that list (confirm). Count an address as covered **only if a row of the sheet transcribes or cites it by its full path / full file name** — not by a shared base name (e.g. `Casey.md`), not only inside a "known missing" / "not copied" list. Write the true "k of N", the direct / via-Tier-U split, and change "checked 2026-10-23" to "recounted by hand 2026-10-30". In the report, list each address with the row that covers it (or "not covered"). |

**Held (decisions pending — do not change):** SH-007 (the `01` "line 65" coordinate in `06`-copying rows: leave as is, log `HELD`), SH-009 (the "N-line file" counts: leave as is), SH-015…SH-017, SH-019 (Tier U sheets; orchestrator).

## 4 · The report
Create `AUDIT/Sweep_Reports/<City>_Sweep.md` containing:
- header: city, date 2026-10-30, who (sub-agent), what was read;
- **table** `ID | Result | File | Old → New (short) | Check` — one row per ledger entry and per shared fix applied. `Result` ∈ `APPLIED`, `ALREADY-RIGHT`, `PARTIAL` (say what's left), `HELD` (depends on a DECIDE), `SKIPPED-MISMATCH` (live text differs; give the evidence), `NEEDS-DEVELOPER`;
- **MUST-OPEN recount table** (§3, SH-008) for every sheet: address → covering row (or "not covered"), resulting "k of N";
- **New findings** (anything wrong that the ledger did not list; do not fix unless it sits inside the entry you are applying — just describe it with file and line);
- **Files edited** (full list of paths).

## 4a · Lessons from the first run (Halley, 2026-10-30) — apply them
- **The city's own `16` "DETERMINED" section.** If the city has one (upper-case heading, `## N. ✅ <NAME> — DETERMINED`) and the ledger section does not list SH-013 for it: add its heading line to the Pre-Trip's `16` line lists (your `grep -n -i` finds it), mark it "the city's own upper-case heading", and report it under `NEEDS-DEVELOPER` (do **not** quote its shares beside Half B on your own).
- **SH-014 range.** At last check the text of `16`'s "CONSEQUENCE" block ran **L1287–L1304** (L1305 is blank). Cite what you see live.
- **A meta row elsewhere in a sheet** that restates a coverage count ("11 of 11 … exist on disk") and now disagrees with the recounted header: leave it and report it.
- **Where k < N**, the header names the uncovered addresses; also list them in your report under New findings ("rows missing for must-open addresses") — they are gaps for the developer to decide on, not for you to fill.
- A judgment call in the recount (for example a directory-qualified short form such as `READER/Halley.md`) is marked ⚑ in the report.

## 5 · Do not
- Do not read other cities' files except the shared source lines you must verify; do not carry anything from one city to another.
- Do not commit. Do not run `graphify`; this is a targeted edit job at known anchors, not codebase exploration.
