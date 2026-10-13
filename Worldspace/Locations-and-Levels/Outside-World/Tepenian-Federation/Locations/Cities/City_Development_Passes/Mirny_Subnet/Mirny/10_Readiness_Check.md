# Mirny · Step 10 — The Readiness Check

**Pass:** Mirny · ULM · Step 10 · reading half written 2026-10-12 (three T8 readers A, B, C; Round 2 UNANIMOUS 3/3 files, 9/9 field sets; Round 3 6/6 CONSISTENT), file-system half and the merge on 2026-10-12 evening and 2026-10-13 morning. Round records, raw output and the double-check: `10b_T8_Rounds_Step_10.md`.

**Standing: PROPOSED. Step 10 run; awaiting developer review. This record does NOT declare the Mirny pass complete.** The governing principle is **verify, do not assert** (`00_RUNBOOK.md` Step 10): where a check could not be run, it says so, and where it fired, it says that. Nothing was fixed or banded by this step: every fix below is a proposal for the developer.

**Subject of the contamination checks.** The runbook runs items 1–1c against **the NEXT pass's subject**, and the developer has not named it. The three un-run cities of the Mirny subnet in the tracker are **Casey, Kunlun and Vostok** (Vostok is being renamed Ariun Nuur: both names were scanned). **Mirny is not a subject.** If a different city runs next, items 1, 1a and 7 must be re-run for it.

**Law of one location.** No other city's pass, culture file or row was opened. The index and the manifest name other cities and were read for the scan only; the pre-seeded folders were counted and listed by file name only.

---

## 1 · The eleven items (fourteen checks), with evidence

| # | Item | Result | Evidence |
|--:|---|---|---|
| **1** | Scan the auto-loaded memory index for the next subject | **FIRES — one line needs a fix or a band** | Six index lines name a subject: **L103** Kunlun, **L109** the rename line (Ariun Nuur; its *Vostok* is the district), **L113** Kunlun, **L121** Kunlun and Vostok, **L122** Kunlun and Vostok, **L124** Vostok. Five are attribute-only (L103 borderline). **L124** (the Vostok bioinformatics link) is classed **CHARACTER-STATEMENT** by the conservative rule (readers A and B; C conceded in Round 3): it states an industry identity in pushed text, and `06` L315 ranks a city's sector with its rationale as conclusion-tier. **Casey has no index hit.** See §2 |
| **1a** | Scan the required reading (`00`–`06`, `README`, `Disciplines/`) for the subject's name, return line numbers, manifest in `06` | **FIRES — five unmanifested hits** | Normalized scan, hits as file:line:token only: `01`–`05`, `README`, all six `Disciplines/` files: **0 hits**. `00_RUNBOOK.md`: **L9, L1332, L2218** (Casey), **L1958** (Vostok), **L2073–L2074** (Kunlun, Vostok). `06`: the 11 Casey lines (L292, 294, 311, 312, 313, 314, 315, 319, 328, 329, 332). `06` manifests the Casey anecdote at `00` §C.3 (L311) but **none of L9, L2218, L1958, L2073–L2074**. All five are attribute-level (an anecdote, a worked type row, a research-folder bearing, a founding comparison), not character statements, so they need manifest rows, not removal |
| **1b** | The file tree the next run must navigate: titled with a claim? | **PASS** | Casey, Kunlun and Vostok each hold 22 files in 2 folders (the Pre-Trip, the position ledger, `README`, 19 datasheets), identical file names across the three, all step-based (`Step_5.md`, `Phase_7.md`): none titled with a claim. The Mirny folder's names are step-based. (Contents were not read.) |
| **1c** | Grep this step's own new prose for the subjects | **PASS, one note** | Today's new files `Symbol_Review_2026-10-13.md`, `09_Record.md`, `09.5_Log.md`, `09b`: **0 hits**. `ULM_AUTORUN_HANDOFF.md` (2 lines) and `ULM_AUTORUN_STATE.md` (hits at log lines 84 and 87) name the subjects as **scope** (shape). One log line quotes the title of index line L124; that is a pointer to the leak, not its content, but it should not enter any subject's required reading |
| **2** | Update `06` with worked examples this pass added to the methodology | **PASS (none added)** | `git status` over `Universal_Location_Methodology/`: only `MASTER_Process_Tracker.md` and `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` are modified; `00_RUNBOOK.md`, `06`, `Disciplines/` and `Tools/` show no diff. The observations entries M-283 to M-298 name no subject. **But** `06` L310 (a Casey row naming `01` §1 line 65) is **stale**: `01` now has 0 hits, which also resolves the `06` L310 against L362–L364 contradiction the readers raised |
| **3** | The quarantine list was built by rule, not by recall | **N/A for this pass; cannot be verified for the next** | Mirny was run **WARM** (`00.1` L3), whose input contract is a line-by-line admitted/excluded table built by T8. No cold quarantine list exists yet for a next subject |
| **4** | Open the header of every admissible file for its cited sources | **N/A until the next run's admissible list exists** | Not re-opened for Mirny's list (T8 verified each entry) |
| **5** | The corpus-wide retrieval layer is flagged unusable | **PASS (cold runs only)** | `Test_Runs/COLD_RUN_CHECKLIST.md` L291–L296, L336–L341, L401 and `CLAUDE.md`'s carve-out flag it; the hook still fires, and ignoring it is compliance only inside a cold run or for an isolated reader. This warm pass used no graph, with the hook notices disregarded under the project instruction |
| **6** | Every path named in the handoff exists | **PASS** | 20 of 20 backticked paths in `ULM_AUTORUN_HANDOFF.md` resolve (raw output in `10b`) |
| **7** | The next run's output folder does NOT already exist | **FIRES (a contradiction of two instructions)** | `Mirny_Subnet/Casey`, `/Kunlun`, `/Vostok` already exist, each **pre-seeded** with 22 files (1,142 lines in Casey) by the Pre-Trip and datasheet scaffolding. The runbook (§10.2 item 7) calls a pre-seeded folder a contamination risk and a status lie; the Pre-Trip and datasheet practice creates exactly that. Not a contamination finding (the names are generic); the two instructions disagree |
| **8** | The shared observations file sits outside every quarantined folder | **FIRES for a cold run, holds for a warm one** | It lives in `Test_Runs/`, which a cold run closes whole until Step 7 (`00_RUNBOOK.md` L66; also L2792, *everything excludes `Test_Runs/`*). A warm pass reads and writes it (as this one did) |
| **9** | Gate 0 outward: every tracker completion claim against the files | **PASS with two notes** | Every file the Mirny tracker row and LAST TOUCHED line name exists, with line counts listed in `10b`. The Step −1 to 3 round records (`00.1b`, `00b`, `01b`, `02b`, `03b`) are in `Archive/ULM_Records/…/Mirny/` (`DR-27`, README L49), not the pass folder. Notes: the city row ticks every phase with no PROPOSED mark (`Q-141`); and this step must not yet be ticked complete |
| **10** | Findings were IMPLEMENTED, not merely recorded | **FIRES** | Of the observations M-247 to M-298, **only M-246 is cited in any rule file** (`00_RUNBOOK.md`, `04`, the Pre-Trip recipes, `Datasheet_and_PreTrip_Tracker.md`). The next pass follows the rules, not the log. The 19 proposals MP-1 to MP-19 are PROPOSED; the `DR-56` consequences are not yet applied |
| **11** | The handoff states what the next run CANNOT prove | **DONE** | Added to `ULM_AUTORUN_HANDOFF.md` (*What this handoff cannot prove*); the limits are in §4 below |

## 2 · The auto-loaded index (item 1), by reading

- **What the header covers.** In *cold* runs every `project_*` entry is withheld by default and discovery is by `grep -ril`, filenames only (`MEMORY.md` L3–L6). **It does not cover:** the index lines themselves (already pushed before any decision), the `reference_*` and `feedback_*` files that **L113** and **L122** point to, any non-cold session, the archive and catalog files named at L5–L6, or aliases (a scan for the new city name finds only L109; **L121, L122 and L124 still use the old name**).
- **Casey memory (item 1, files not just the index).** Three conclusion-tier files are named by `06` L314: `project_casey_recheck.md`, `project_casey_bug_check_resolved.md` and `project_pink_lucy_migration_resolved.md`. Checked today: **all three carry the contamination banner immediately after the frontmatter** (banner text dated 2026-09-02). Minor: the frontmatter `description` of the first two states a result (*genuinely flat population, developer-confirmed*) above the banner; descriptions are not pushed, but they are shown when a memory is chosen.
- **Wider memory surface.** 97 of the 343 memory files mention a subject name (filenames only; not read). The index and the three banded files were checked; the rest were not classified (R-186).

## 3 · What fired, and who decides

1. **`MEMORY.md` L124** (item 1): fix or band the index line itself (a banner inside the target file cannot cover an index line). Developer's call; I have **not** edited the index.
2. **Manifest rows** (item 1a): propose five `06` rows by coordinate and tier, plus annotation of the stale L310. `06` is a methodology file, so this waits for the developer.
3. **Pre-seeded folders** (item 7): amend the runbook (the ULM's *output* files must not exist; scaffolding may) or move the scaffolds. Developer's call.
4. **Observations file location** (item 8): matters only for cold runs; a cold run cannot write the log without breaking its quarantine (the original `M-0` problem).
5. **Recorded, not implemented** (item 10): decide which of MP-1 to MP-19 go into the rules before the next city.

## 4 · What this check cannot prove (item 11)

- **A zero proves only what the scan could see.** The normalized scan covers `00`–`06`, `README` and `Disciplines/`; it does not cover the other required reading a cold run might add, nor wrapped phrases beyond the normalization used.
- **Memory is pushed at the index and pulled at the files.** Only the index and three banded files were checked; 97 files mention a subject.
- **The subject is assumed.** Casey, Kunlun and Vostok/Ariun Nuur stand in for a city not yet named.
- **The default-deny header is partial** (cold only, `project_*` only).
- **It cannot clean a session already exposed.** This session read the index lines, the manifest rows and the Division of Industry siting table for Mirny's own purposes, so it should not run any of the three cities as a cold run. Nor should any session that opened the shared per-city file `Division_of_Industry/16_Per_City_Three_Tier_Run.md` whole: **the Mirny pass opened it only at admitted spans** (Phase 4: L109–134, L241–248, L275; Phase 7: L1–139, L241–248, L275, L445–465, L2105–2173; Mirny's row and its §20), but that file also holds **a Mirny section (L2105–L2173)**, so it is a vector for the next runs.
- **Retrieval layers cannot honor a quarantine.** The check confirms they are flagged, not that no one used them.
- **Line coordinates drift** as files grow; every coordinate here is valid at 2026-10-13.
- **Classifications are one reader's judgment per entry,** and self-audit has erred toward the flattering side: the three-way merge is the control, and the conservative value won (L124).
- **This record and the readers' files are themselves 1c surfaces:** they name the subjects and quote index fragments. Keep them out of any subject's required reading.
- **Nothing here is Mirny-complete.** The pass is not finished by its own closing test (the lived middle is empty), `DR-56` changes the strongest finding's premises, and Phases 7–9 are unratified.

## 5 · Nulls · Reserved findings · Requests · Questions · Provisional assumptions · Snags

### Reserved findings (S10-RF-n)
- **S10-RF-1:** L124's referent is ambiguous (the city, or the district that keeps the name Vostok); treated as the city by the conservative reading. `[A,B,C]`
- **S10-RF-2:** the header's default-deny leaves holes (index text, `reference_*`, `feedback_*`, non-cold sessions, aliases). `[A,B,C]`
- **S10-RF-3:** zeros in `06` for Kunlun and Vostok closed nothing: the runbook itself names them (L1958, L2073–L2074). `[A; confirmed by the scan]`
- **S10-RF-4:** `16_Per_City_Three_Tier_Run.md` is a shared per-city vector for every city in it, including Mirny's §20; the two structural fixes (split per city, or an isolated reader) are still *neither in place* (`06` L333–L337). `[A,B,C]`
- **S10-RF-5:** `00_RUNBOOK.md` L3078 still says the required-reading check *failed three times*, while `06` L349 and L378 record later instances. `[B,C]`

### Requests (R-180 onward; none blocking)
- **R-180:** fix or band `MEMORY.md` L124 and sweep the old city name at L121, L122 and L124 (waits for the held rename sweep after the Mirny pass). *Developer.*
- **R-181:** propose `06` manifest rows for `00` L9, L1332 (already covered by L311), L1958, L2073–L2074 and L2218, and annotate or retire the stale `06` L310. *Developer approval (methodology file).*
- **R-182:** decide item 7 (pre-seeded folders) and item 8 (observations file in `Test_Runs/`): amend the runbook text or the practice.
- **R-183:** decide which of MP-1 to MP-19 (and which observations M-247 to M-298) are implemented in the rules before the next city.
- **R-184:** an isolated reader to classify the memory files behind the six index lines and the other files that mention a subject (not read here).
- **R-185:** run the accumulation-shape follow-up to the safeguard probe (see R-177).

### Questions (Q-145 onward; none blocking)
- **Q-145:** does index L124 mean the city (now Ariun Nuur) or the district that keeps *Vostok*?
- **Q-146:** may the index's city lines that still say *Vostok* (L121, L122, L124) be swept now, or with the held rename sweep?
- **Q-147:** does the header's `project_*` default-deny count as the contamination banner that item 1 requires?
- **Q-148:** which city runs next? Items 1, 1a and 7 must be re-run if it is none of the three.
- **Q-149:** index L113 (*Kunlun 19-nation*) is census composition only, not a founding claim (founders live only in the Register): confirm.

### Provisional assumptions (PA-96 onward)
- **PA-96:** *Vostok* at L121 and L122 is the city under its old name; L124 is treated as the city. *Overturned by:* Q-145.
- **PA-97:** Highway 37 entries in `06` and index L121 are a highway, not a subject hit.
- **PA-98:** `MEMORY.md` is as read on 2026-10-12; index lines change between sessions.
- **PA-99:** the subjects are Casey, Kunlun and Vostok/Ariun Nuur because no next city is named.

### Snags and self-corrections
1. **Reader deviations, disclosed by the readers:** reader C ran one un-normalized `grep` on the two admitted files after reading them (it caught its own miss of Casey L313); reader A ran `grep -n -i` on the same two files and one `sed` line; reader B read runbook L3134, one line outside its range, and drew nothing from it. The brief said not to run scans. `[A,B,C]`
2. **The Read tool's phantom last line:** reader C on `MEMORY.md` (L152) and `06` (L430); reader A on the runbook range. Counts set by `wc -l`.
3. **Harness git status:** readers A and B cited the session-start `git status` as a labeled out-of-scope fact; the orchestrator verified it directly (item 2).
4. **Round 3 conceded:** reader C's L124 (attribute-only) to A and B's CHARACTER-STATEMENT; reader B's *plus its rationale* wording was softened (the line names the industry and a link, not a mandate).
5. **Corrections to Step 9:** this step found the safeguard probe **had been run** on 2026-10-11 (nine tests, all passed); Step 9 and the tracker's L360 had said it was pending. Corrected in `09.5_Log.md`, `09_Record.md` and the tracker.
6. **The runbook's text for item 1** (L3074) lists the CST and RWBEM copies in `Disciplines/` that `DR-14` removed from ULM reads; the item 1a scan opened them mechanically for subject names only (hits as file:line:token; no content was read or displayed) and found 0 hits. Recorded as a deviation from the spirit of `DR-14`.

**T4 - SHED:** this step had no use for the subjects' own files, their megasheets, culture sheets or determinations, the memory files behind the index lines, any other city's pass, the Division of Industry's per-city sections, and the symbol and sign layers.
