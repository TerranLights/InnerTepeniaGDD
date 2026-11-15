# Amendment log — Mirny review, 2026-11-11

**The recording law (runbook Step 9.5):** snags, dead ends, killed findings and self-corrections, written when they happen.
Governed by `Universal_Location_Methodology/STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md`, Part A. Times come from `date`
readings. Where the run stands is kept in `Universal_Location_Methodology/RUN_PROGRESS_Mirny_Review_then_Casey.md`.

---

- **MR-01 · 05:33** · Run started by the cron firing of job `c33edca4` (morning 1). Warm run (`DR-6` ground for any reader that is
  told to run graphify). Section 1 reads done by 05:34 (runbook in full; amendment rules; standing lines; PRE-TRIP §N; tracker boot
  and resume block; November To-Do §§3–4; rulings log `DR-100` to `DR-135`).
- **MR-02 · snag, dates of the re-runs.** The startup file dates Mirny's last re-runs "2026-11-08 to 11-09". On disk, the QA re-run
  file is named `…_2026-11-09`, but every re-run file was last written on 2026-11-08: the QA re-run at 15:56 (record 16:04), the fresh
  panel at 17:24 (record 17:25) and the readiness re-run at 18:16 (record 18:22); `REPASS_QUEUE_AND_PROGRESS.md` at 18:24. Nothing in
  this folder changed after 2026-11-08 18:24 (`find -newermt`). This review therefore takes "since the re-runs" as after
  2026-11-08 18:24, and lists every change dated 2026-11-09 or 2026-11-10.
- **MR-03 · self-correction, a commit is not a change.** `git log --since=2026-11-09` flags commit `b5824186` (2026-11-10 15:22,
  "Mirny finish run (2026-11-05 to 2026-11-09)…; the three application batches") on Mirny's spec, culture file, six datasheets and the
  symbol registry. The files' own times are 2026-11-08 (spec 14:17; culture file and the six datasheets 11:48), before the re-runs:
  the commit records the corrections applied on 2026-11-08 under `DR-123`. **Not a change since the re-runs.** `git log --since` reads
  commit time, not edit time; the first reading would have listed Mirny's own applied corrections as new.
- **MR-04 · checked, no Mirny line.** Commit `c613fec4` (2026-11-10 15:36, `DR-135`) changes one line of
  `City_Symbolic_Substrate/City_Symbol_Assignments.md`; changed lines naming Mirny: `0` (a count from the diff; the line was not read).
  Commit `354c17f6` changes `City_Relationship_Database.md` at one line in place (another city's entry, `DR-133` item 5; not read, no
  line moved) and `Ports.md` (four lines; the three `DR-133` names are listed in the note).
- **MR-05 · checked.** No file in this folder cites any of `DR-124` to `DR-135` (`grep -l`, zero files), as expected from MR-02:
  the re-runs predate them.
- **MR-06 · dead end, my own path.** The first source sweep looked for `Extent_and_Density_Per_City.md` under `Cities/` and got
  MISSING; the file is in `Universal_Location_Methodology/` (no commit and no uncommitted change since 2026-11-09).
- **MR-07 · snag, the quota tool.** `python3 Tools/web_quota_count.py --help` is not a help flag: it ran on the default tasks folder
  (another session's: 235 transcripts, 11,004 calls). Re-run with `--tasks` on this session's folder: 0 web calls. The startup file
  already says "always pass `--tasks`"; the slip was mine.
- **MR-08 · found, a source change the sweep list did not name.** The startup file's list of sources to `git log` covers this repo;
  the treaty draft lives in the Timeline repo, so a separate `git -C` sweep was run. It found commit `23e5226` (2026-11-09 23:42):
  Article II.2.5 added (note, C2). Without the second repo the review would have recorded `DR-127` item 2 as a ruling with no canon
  text behind it.
- **MR-09 · self-correction in the note.** The note's first draft placed the treaty's second changed line at "Article II.3.2 (now
  L54 region)", inferred from the diff's hunk header. The line is Article IV.2 paragraph 2, L76 (grep of the current file).
  Corrected before anything read the note.
- **MR-10 · self-correction, caught by a reader.** The note's section A and the classifier's brief listed `DR-132` as a process
  ruling of the same days. Its text (rulings log L1958) covers two other cities' pointer lines only, so it does not carry. The
  classifier flagged it and kept `DEC-224`, `DEC-269` and `DEC-270` untouched; the note was corrected (section A, section E).
- **MR-11 · checked, a reader's open flag.** The classifier could not settle whether amendment rule 6 bears on `DEC-245`'s option C.
  Orchestrator read rule 6 (L61–63) and the entry (L549–553): it does not; untouched stands (note, section G).
- **MR-12 · self-correction, partial reads.** The first print of the cited lines cut each at 260 characters, and section F's first
  draft completed four quotations in brackets from the locator's table and marked three more "per the locator". Each was then read
  on the line itself (05:53) and the note now quotes only what the lines say. The ST14 L662 check first failed in the shell's
  `ugrep` wrapper ("exceeds complexity limits", the same snag the locator logged) and was re-run with `/usr/bin/grep`.
- **MR-13 · method, one reader per item and the verifier.** `Tools/triple_read_verify.py` takes exactly three outputs (L297–300).
  For a one-reader item check, the reader's output is passed in all three slots; the verdict then reports that one reader's PROOF
  fields only. Recorded so a later reader does not read "UNANIMOUS" as three readers.
- **MR-14 · snag.** The first replacement script stopped on a quotation-mark mismatch in the F-2 text and wrote nothing, while MR-12/MR-13 and the progress line were appended in the same command. Re-run with the exact text: all seven replacements applied; no bracketed completion is left.
- **MR-15 · the item-check round is set up.** Sixteen briefs and reading lists generated by one script
  (`scratchpad/mirny_review/tools/make_item_briefs.py` with `brief_template.md`), written beside this file as
  `.review_F-<n>_brief.md` and `.review_F-<n>_required.txt`; no placeholder left in any brief (grep: 0 files); the F-2 brief read
  end to end before dispatch (standing line 24); each reader has its own staging folder (`scratchpad/mirny_review/items/F-<n>/`).
  **The note is frozen for the round** (it is every reader's first entry): sha256[:16] `bb80ee4399f65819`, 135 lines. Nothing edits it until all
  sixteen outputs are in and checked. Two waves of eight, to keep the load and any cut-off small.
- **MR-16 · Round 2 failure, F-9.** The first run of the verifier on the F-9 reader failed two fields: the census entry's LLAST (the reader wrote `---` for a blank last line) and the rulings-log entry's LMID (the middle line across three spans). Same-reader repair requested under `DR-117` item 2, one field at a time, no value supplied; the first run is kept (`.review_F-9_round2_raw_FIRSTRUN.txt`).
- **MR-17 · F-9 cleared after repair.** The reader repaired both fields by hand and logged each repair above its PROOF blocks (its output L119–121); Round 2 re-run: UNANIMOUS (one reader in all three slots), no ⛔ line. Both runs kept.
- **MR-18 · item round closed (06:14).** All sixteen item outputs in and Round 2 cleared; the note was unfrozen and section H appended (verdicts and the piece plan). The note before the edit hashed `bb80ee4399f65819` (frozen value `bb80ee4399f65819`: unchanged through the round); after: `55b0633c0fe429a8`, 176 lines. It is frozen again for the pieces.
- **MR-19 · pieces set up (06:18).** Eighteen briefs (three per piece) and six reading lists generated by `make_piece_briefs.py` from `piece_template.md` (`.t8_review_<piece>_brief_<A|B|C>.md`, `.t8_review_<piece>_required.txt`); no placeholder left (the script asserts it); the ARR reader-A brief read before dispatch (standing line 24). Two lists were widened after checking the item readers' cited lines: ARR gains Phase 2 L55–80 (the generator line) and Phase 5 to L300 (P5-25 at L278); FREE gains Phase 4 L185–200 and Phase 7 from L150. Disjoint numbering per reader: docket `<piece>-D1/D101/D201`, questions `<piece>-Q1/Q101/Q201`. First batch ARR, LANG, COMP (nine readers); then OWN, FREE, NODE.
- **MR-20 · snag, a reader wrote outside its staging folder.** FREE reader A created a read-only PROOF comparison script at `scratchpad/checks/proofcheck.py` (outside its staging folder, against its brief's §0) and reported it itself; it is recorded in its output's section 6. The file is in the session scratchpad, not the repo; it is left in place (the hook blocks `rm`) and not used by anything. A read-only comparison of PROOF fields is what standing line 11 asks for; standing line 1 still requires the fields to be copied by hand, and Round 2 checks them against the sources either way.
- **MR-21 · snag, readers writing check files.** OWN reader B wrote two scratch comparison files inside its own staging folder (`.src_check.txt`, `.mine_check.txt`) to check its PROOF fields read-only, and reported it. Inside its own staging folder, so no other reader can see them; left in place. Two readers (FREE A, OWN B) independently built tools to check their PROOF fields: the brief asks for a read-only comparison (standing line 11) and gives no sanctioned place to do it. Proposed for the rules: allow scratch check files inside the reader's own staging folder.
- **MR-22 · snag, the COMP merge writer wrote a scratch file** (`scratchpad/rows.txt`, a copy of spec L32–40 and L60–67 used to re-run the readers' 17-row arithmetic) outside the repo and reported it; left in place, used by nothing else. Third instance of a worker needing a scratch place the brief does not give (MR-20, MR-21).
- **MR-23 · self-correction, my sweep pattern.** The first American English sweep pattern used open stems (`realis\w*` and the like), so it flagged "realism" six times in COMP; "characteristic", "specialist" and "-ism" words would also have hit. The stems now take only British verb and noun endings (-ise, -ised, -ising, -isation…); LANG and COMP re-swept with the corrected pattern.
- **MR-24 · snag, the NODE merge writer wrote a scratch script** (`scratchpad/qcheck.py`, a read-only check of its 60 quoted fragments against their cited lines, all found) outside the repo and reported it; left in place. Fourth instance (MR-20 to MR-22): workers keep building their own read-only checks. It also reported a harness "file changed on disk" notice after its first append, with contents matching what it wrote.
- **MR-25 · three misquotations fixed by the orchestrator, FREE.** The triage found 3 MISQUOTE (all docket cells where the merge set its own proposed wording in quotation marks; none misreports a source): FREE L278 gains the word "about" so it matches the piece's own L181; L288 and L292 are rewritten unquoted, marked "as proposed wording". The audit was re-run after the fix (raw file replaced; the first run's count was 37 NOT FOUND).
- **MR-26 · a series prefix in a within-file key, OWN.** The OWN merge labeled its two reserved items `RF-OWN-1` and `RF-OWN-2`; standing line 17 forbids within-file keys that start with a series prefix (RF- is one). Renamed in place to `OWN-RS-1`, `OWN-RS-2` (every occurrence, by sed) before any check or record read the file. The merge brief did not name a key for reserved items; it should.
- **MR-27 · six misquotations fixed by the orchestrator, OWN.** The triage found 6 MISQUOTE, all in the merge's section 3.6 test list (L334–L342): sentences the merge reworded or spliced from two readers and set in quotation marks with reader credit. None misreports a source line. Each is now written unquoted and marked "(merged wording, unquoted)", per standing line 13; the audit was re-run after the fix (first run: 46 NOT FOUND). Pattern across the six pieces: 9 misquotations, every one a merge writer putting its own composed wording in quotation marks. Proposed for the merge brief: "never set your own or a combined wording in quotation marks".
