# DerivationMechanisms: normalization plan (written 2026-10-29, nothing moved)

**This is tracking, so it lives in this repo (Inner Tepenia GDD), not in `DerivationMechanisms`.** It records what I found when I read the new repo and proposes how to sort it out. **No file was moved, edited or deleted in either repo to produce it.**

## The principle (developer, 2026-10-29)
The `DerivationMechanisms` repo is for **instructions and methodology that apply across every work of media in the whole Sci-Fi / Tepenian Universe**. **Tracking and results stay in the repo where the work happens.** Example: whichever city the ULM runs on next is written to the Inner Tepenia GDD, never to `DerivationMechanisms`. The method lives there; the results live here.

## What I found

### 1 · The new repo already holds project data, and it is on GitHub
- Its remote is `https://github.com/TerranLights/DerivationMechanisms.git`, and local `main` equals `origin/main` (commit `4fa5a61`), so **everything copied in is already pushed.** Its `.gitignore` says the repo is **public**. I could not check the visibility itself (the `gh` tool is not installed here).
- The commit "Copy existing derivation mechanisms in" brought in Inner Tepenia run data: the 178 KB rulings log, the master process tracker, the city input audit and gaps, the datasheet trackers and coverage reports, the Santa Luce population scenario, the 601 KB methodology-observations file (which names every city), the CST and RWBEM progress files, and the Casey-based Pre-Trip template. **Taking them out of the working tree later will not remove them from git history.** Whether to purge the history (a force-push) is the developer's decision; I have not done anything.

### 2 · Classification of the ULM folder (129 tracked files)
| Bucket | What it is | Files | KB |
|---|---|--:|--:|
| **M** | Universal method (move byte-identical) | 48 | 740 |
| **X** | Mixed: method plus this project's bindings (split first) | 11 | 1,270 |
| **T-U** | Generic tool (parametrize paths, then move) | 8 | 78 |
| **T-P** | Project tool (stays) | 16 | 323 |
| **P** | Project data, tracking, rulings, results (stays) | 30 | 829 |
| **C** | Tepenian-canon summaries used as inputs (decision needed) | 16 | 112 |

*Per-file table at the end of this document. The 168 files the GDD git-ignores (graphify output, scratch) were not copied and are not counted.*

### 3 · Why moving method files is hazardous (inbound references)
- `00_RUNBOOK.md` is named by about **421 files outside the folder** and `03_The_Phase_Spine.md` by **274**; the 38 cities' Pre-Trip sheets and datasheets cite them by **absolute path and line number**. Moving a file byte-identical keeps every line number valid and only the path prefix changes; **splitting a file shifts lines**, which the existing `Tools/remap_line_citations.py` can repair (one run per file per base commit; it does not read bold-wrapped numbers, and prose line references such as "lines 522–540" need hand fixes, as I found for Santa Luce).
- The tools locate everything relative to this repo's folders (`REPO = ...` computed from the script's own location), so a tool moved elsewhere stops working until its paths are parametrized.
- The mixed files carry this project's **registry**: the runbook's section C and the spine's MUST OPEN lists name absolute GDD paths. Those belong in the GDD as a **project bindings** file; the rest belongs in `DerivationMechanisms`.

### 4 · Duplicates inside the new repo (hash comparison)
| Pair | Result |
|---|---|
| Enneagram: GDD copy (60 files) vs Timeline copy (41) | by file name 8 are common: 5 identical, 3 differ; 19 exist only in the GDD copy; none only in the Timeline copy |
| Character methodology: GDD (14) vs Timeline (35) | 11 common names, **none identical**; 3 only GDD, 20 only Timeline |
| Character methodology: Timeline (35) vs Novel (21) | 12 common names, **none identical** |
| Character methodology: GDD (14) vs Novel (21) | 13 common, 7 identical, 6 differ |
| Story structure: Novel vs Timeline definitions | one file each; different names, **not compared yet** |
The CST and RWBEM folders in `DerivationMechanisms` also hold `CST_Progress.md`, `RWBEM_Progress.md` and the input-availability files, which are **tracking** under the principle above.

## Proposed order (nothing started)
1. **Freeze.** Decide that no new project data goes into `DerivationMechanisms` from now on (tracking, rulings, per-city results stay in the project repo). *(Needs your OK; costs nothing.)*
2. **History question first.** Decide whether the already-pushed project data stays in public history, or is purged (history rewrite and force-push; outward-facing and irreversible, so yours to order).
3. **Remove the project data from the working tree of `DerivationMechanisms`** (the P and T-P buckets above, the progress files, the Casey template) in one commit, once step 2 is decided.
4. **One canonical version per duplicated method** (Enneagram, character methodology, story structure): a read-only diff report per pair (an agent job), then your rulings on which text wins; the Timeline's "perfect canon only" law means no method is merged there.
5. **Split the mixed files** (bucket X): a method file in `DerivationMechanisms` and a **project bindings** file in the GDD, then run the remap tool across the 38 cities' sheets, testing on Santa Luce first. Do this only when **no run is in flight**.
6. **Parametrize the generic tools** (bucket T-U) to take a method root and a project root, then move them.
7. **Rewrite the path prefix** in the cities' sheets with a script (not a rebuild, which would drop hand additions), update `Repo_Scope.md`, `~/.claude/CLAUDE.md` (the Enneagram path), the memory notes and the graphify graph.
**Timing option:** steps 5 to 7 change paths and lines that today's prepared runs cite. Either do them **before** the runs (the runs then cite the new paths) or **after the first wave** (one rewrite later). I lean toward after, because the remap is safest when nothing is in flight and the first wave will show what the runs really cite; steps 1 to 4 can happen now.

## Decisions for the developer
1. Freeze (step 1): yes or no.
2. The pushed history (step 2): leave, or purge.
3. Where the `Corpus_Reference_Sheets/` (bucket C, 16 summaries of Tepenian canon) belong: `DerivationMechanisms/Data_Reference`, or stay with the project, or the Timeline.
4. Timing of steps 5 to 7: before or after the first run wave.
5. Whether `DEVELOPER_RULINGS_LOG.md` stays whole in the GDD (my reading: yes, its `DR-` entries are project rulings; its method-level rulings get restated in the method files).

## Per-file classification of the ULM folder
| File (relative to `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`) | KB | Bucket | Reason |
|---|--:|---|---|
| `Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md` | 6 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md` | 11 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Doll_Representation_Categories_Quick_Reference.md` | 2 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Falkland_Treaty_Quick_Reference.md` | 10 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Founders_and_Renames_Quick_Reference.md` | 11 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/No_National_Stereotypes_Quick_Reference.md` | 5 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Phase_7_Roster_and_Model_Files_Quick_Reference.md` | 7 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/QA_Gates_Full_Text_Quick_Reference.md` | 12 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Review_Panel_Full_Text_Quick_Reference.md` | 17 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md` | 10 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Robot_Religions_Roster_Quick_Reference.md` | 1 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` | 3 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Social_Contract_Term_Quick_Reference.md` | 4 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Step_10_Readiness_Check_Full_Text_Quick_Reference.md` | 5 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Step_9_Record_Full_Text_Quick_Reference.md` | 4 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `Corpus_Reference_Sheets/Zodiac_Signs_Quick_Reference.md` | 4 | C | summary of Tepenian canon used as a Tier U input; universe data, not method; decision needed |
| `01_Frame_Typology_and_Inheritance.md` | 40 | M | universal method; move byte-identical |
| `02_Generators_Capability_and_Symbols.md` | 58 | M | universal method; move byte-identical |
| `04_QA_Gates_and_Differentiation.md` | 65 | M | universal method; move byte-identical |
| `05_The_Input_Contract.md` | 55 | M | universal method; move byte-identical |
| `Disciplines/00b_General_Population_Discipline.md` | 16 | M | universal method; move byte-identical |
| `Disciplines/00d_Shadow_Proportion_Discipline.md` | 14 | M | universal method; move byte-identical |
| `Disciplines/00f_Review_Panel.md` | 56 | M | universal method; move byte-identical |
| `Disciplines/Cultural_Synthesis_Techniques.md` | 83 | M | universal method; move byte-identical |
| `Disciplines/README.md` | 7 | M | universal method; move byte-identical |
| `Disciplines/Real-World_Basis_Extrapolation_Method.md` | 34 | M | universal method; move byte-identical |
| `Extent_and_Area_APPROACH.md` | 22 | M | universal method; move byte-identical |
| `Naming_Drift_Typology_GUIDELINE.md` | 10 | M | universal method; move byte-identical |
| `PRE-TRIP_INSPECTION_RECIPE.md` | 14 | M | universal method; move byte-identical |
| `Run_Modes_Warm_and_Cold.md` | 9 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S01_Step_MINUS-1_The_input_contract_before_the_frame.md` | 6 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S02_Step_0_Frame.md` | 10 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S03_Step_1_Audit_what_is_inherited.md` | 5 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S04_Step_2_Build_the_spine.md` | 6 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S05_Step_3_Research_aimed_at_what_Step_2_named.md` | 11 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S06_Step_4_Write_the_phases.md` | 11 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S07_Step_5_Reconciliation_and_the_CLOSE_pass.md` | 15 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S08_Step_6_Differentiate.md` | 7 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S09_Step_7_QA.md` | 6 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S10_Step_8_The_Review_Panel.md` | 5 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S11_Step_9_Record.md` | 8 | M | universal method; move byte-identical |
| `Stepwise_Execution/01_Spine/S12_Step_10_THE_READINESS_CHECK.md` | 10 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G01_Gate_0_Does_the_completion_claim_match_the_file_Chea.md` | 4 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G02_Gate_1_Coverage.md` | 5 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G03_Gate_2_General_population.md` | 4 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G04_Gate_3_Internal_contradiction.md` | 4 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G05_Gate_4_Swap_test.md` | 4 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G06_Gate_5_Cross_location_consistency.md` | 4 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G07_Gate_6_Duplicate_institutions.md` | 8 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G08_Gate_7_Research_accounting.md` | 4 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G09_Gate_8_Standout_recorded.md` | 4 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G10_Gate_9_Asymmetry.md` | 5 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G11_Gate_10_The_Review_Panel.md` | 4 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G12_Gate_11_Plausibility.md` | 6 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G13_Gate_C_Canon_check_federated.md` | 8 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G14_Gate_F_Frame_integrity.md` | 5 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G15_Gate_I_Inheritance_classification.md` | 6 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G16_Gate_P_Parent_reconciliation.md` | 4 | M | universal method; move byte-identical |
| `Stepwise_Execution/02_Gates/G17_Gate_G_Generator_honesty.md` | 4 | M | universal method; move byte-identical |
| `T8_Standing_Brief_Lines.md` | 7 | M | universal method; move byte-identical |
| `Test_Runs/COLD_RUN_CHECKLIST.md` | 28 | M | universal method; move byte-identical |
| `ULM_At_A_Glance.md` | 8 | M | universal method; move byte-identical |
| `ULM_Diagnosis_and_Accuracy_Approaches.md` | 17 | M | universal method; move byte-identical |
| `ULM_Piece_Index.md` | 14 | M | universal method; move byte-identical |
| `AUDIT_AGENDA_2026-09-16_after-1500.md` | 7 | P | project run data, tracking, rulings or results; stays |
| `CST_Progress.md` | 17 | P | project run data, tracking, rulings or results; stays |
| `City_Input_Audit_2026-10-21.md` | 81 | P | project run data, tracking, rulings or results; stays |
| `City_Input_Gaps_2026-10-27.md` | 19 | P | project run data, tracking, rulings or results; stays |
| `Cultural_Synthesis_Input_Availability.md` | 6 | P | project run data, tracking, rulings or results; stays |
| `DEVELOPER_RULINGS_LOG.md` | 179 | P | project run data, tracking, rulings or results; stays |
| `Datasheet_Citations_To_Reread_2026-10-21.md` | 10 | P | project run data, tracking, rulings or results; stays |
| `Datasheet_Coverage_Report_2026-10-23.md` | 14 | P | project run data, tracking, rulings or results; stays |
| `Datasheet_and_PreTrip_Tracker.md` | 17 | P | project run data, tracking, rulings or results; stays |
| `Extent_and_Density_Per_City.md` | 47 | P | project run data, tracking, rulings or results; stays |
| `Location_Data-Input_To-Do.md` | 34 | P | project run data, tracking, rulings or results; stays |
| `MASTER_Process_Tracker.md` | 71 | P | project run data, tracking, rulings or results; stays |
| `Population_Scenario_Santa_Luce_Redistribution_2026-10-28.md` | 16 | P | project run data, tracking, rulings or results; stays |
| `Pre-Contamination_Reviews/Casey_Pre-Contamination_Review.md` | 14 | P | project run data, tracking, rulings or results; stays |
| `Pre-Contamination_Reviews/Shirayuki_Pre-Contamination_Review.md` | 49 | P | project run data, tracking, rulings or results; stays |
| `RWBEM_Progress.md` | 11 | P | project run data, tracking, rulings or results; stays |
| `RealWorld_Basis_Input_Availability.md` | 5 | P | project run data, tracking, rulings or results; stays |
| `T8_Standard_Entries.json` | 81 | P | project run data, tracking, rulings or results; stays |
| `Test_Runs/ARCHIVED_RUNS.md` | 0 | P | project run data, tracking, rulings or results; stays |
| `Test_Runs/RUN_LOG.md` | 38 | P | project run data, tracking, rulings or results; stays |
| `Test_Runs/Worked_Examples_Archive/Cancer.md` | 7 | P | project run data, tracking, rulings or results; stays |
| `Test_Runs/Worked_Examples_Archive/Districts_Borrowed_Form.md` | 2 | P | project run data, tracking, rulings or results; stays |
| `Test_Runs/Worked_Examples_Archive/Pull_Push_Durability.md` | 4 | P | project run data, tracking, rulings or results; stays |
| `Test_Runs/Worked_Examples_Archive/README.md` | 2 | P | project run data, tracking, rulings or results; stays |
| `Test_Runs/Worked_Examples_Archive/Shirayuki.md` | 2 | P | project run data, tracking, rulings or results; stays |
| `Test_Runs/Worked_Examples_Archive/Sinheung.md` | 7 | P | project run data, tracking, rulings or results; stays |
| `Test_Runs/Worked_Examples_Archive/Symbol_Pairings.md` | 2 | P | project run data, tracking, rulings or results; stays |
| `Test_Runs/Zhongshan_Extracted_Worked_Examples.md` | 11 | P | project run data, tracking, rulings or results; stays |
| `ULM_Input_Available_Audit.md` | 42 | P | project run data, tracking, rulings or results; stays |
| `ULM_Run_Progress.md` | 34 | P | project run data, tracking, rulings or results; stays |
| `Tools/audit_city_inputs.py` | 15 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/build_datasheets.py` | 62 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/build_inspiration_research_queue.py` | 4 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/build_pretrip.py` | 70 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/check_founders_against_register.py` | 11 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/check_must_open_coverage.py` | 10 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/climate_reader_check.py` | 10 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/complete_datasheets.py` | 13 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/drafting_tracker_set.py` | 1 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/inspiration_tracker_set.py` | 1 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/map_books_to_topics.py` | 8 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/pretrip_ledger_template.md` | 0 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/pretrip_template_casey_2026-09-30.md` | 95 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/rename_sweep_held_files.py` | 9 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/rename_sweep_live_files.py` | 5 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/verify_city_sheets.py` | 9 | T-P | tool depends on this project's city table and folders; stays |
| `Tools/build_t8_standard_entries.py` | 5 | T-U | tool is generic but locates files relative to this repo; parametrize paths, then move |
| `Tools/handoff_audit.py` | 7 | T-U | tool is generic but locates files relative to this repo; parametrize paths, then move |
| `Tools/make_t8_required_list.py` | 18 | T-U | tool is generic but locates files relative to this repo; parametrize paths, then move |
| `Tools/phase_discipline_check.py` | 8 | T-U | tool is generic but locates files relative to this repo; parametrize paths, then move |
| `Tools/quotation_audit.py` | 10 | T-U | tool is generic but locates files relative to this repo; parametrize paths, then move |
| `Tools/remap_line_citations.py` | 9 | T-U | tool is generic but locates files relative to this repo; parametrize paths, then move |
| `Tools/triple_read_verify.py` | 19 | T-U | tool is generic but locates files relative to this repo; parametrize paths, then move |
| `Tools/web_quota_count.py` | 2 | T-U | tool is generic but locates files relative to this repo; parametrize paths, then move |
| `00_RUNBOOK.md` | 253 | X | registry tables (section C) and examples carry this project's absolute addresses and city names |
| `03_The_Phase_Spine.md` | 91 | X | MUST OPEN lists carry this project's absolute addresses |
| `06_Worked_Example_Provenance.md` | 38 | X | worked examples are Tepenia cities |
| `Mechanical_Extraction_Field_Guide.md` | 38 | X | names project files and cities |
| `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` | 84 | X | a trial run on one city; recipe part universal |
| `README.md` | 17 | X | describes this folder as a project file set |
| `Stepwise_Execution/README.md` | 7 | X | pointer file |
| `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | 608 | X | 601 KB: method findings (M-numbers) accrued from Tepenia runs |
| `Test_Runs/RESUME_HERE.md` | 65 | X | run resume notes plus method pointers |
| `ULM_Input_Required_Reference.md` | 60 | X | requirements are universal; the address column is this project's |
| `WHY_CITIES_ARE_THE_ROOT.md` | 9 | X | universe-specific argument |
