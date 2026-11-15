# Round record — Casey · Step 3 (Research)

**Output:** `03_Research.md` (618 lines). Casey's warm ULM run under `STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md` Part B item 3: three readers, Round 2, Round 3, one fresh merge writer (`M-246`), the quotation audit run before this record, the American English sweep. Everything in the output is PROPOSED. Record written 2026-11-11 12:03 by `scratchpad/casey/tools/casey_round_record.py`.

## Round 0 — the reading list and the frozen briefs

Briefs `.t8_03_Step_3_brief_A.md`, `_B.md`, `_C.md` (written new for Casey; standing lines 1–6, 10, 11 verbatim). The list, `.t8_required_03_Step_3.txt`:

```
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md :: 2569-2661
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md :: 557-586
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/02_Spine.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_Inspiration_Place_Research_R1.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_Inspiration_Place_Research_R2.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00_Frame.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/01_Inherited.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Amendment_2026-11-11.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Step_3.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/City_and_District_Research_Topics.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Book_Extraction_Index.md
/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md :: 1707-1715
```

## Round 1 — three readers, each in a private staging folder

| Reader | Agent ID | Output (copied here) | Lines |
|---|---|---|---|
| A | `a7e16e62a7faa42ae` | `.t8_03_Step_3_readerA.md` | 554 |
| B | `a4f28907673cf77b0` | `.t8_03_Step_3_readerB.md` | 521 |
| C | `af1da46fbd6b61db4` | `.t8_03_Step_3_readerC.md` | 568 |

## Round 2 — `Tools/triple_read_verify.py` (last change 2026-11-03), raw output, whole (70 lines)

```
required files: 13
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2569-2661] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/02_Generators_Capability_and_Symbols.md  [range 557-586] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_Inspiration_Place_Research_R1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_Inspiration_Place_Research_R2.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00_Frame.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/01_Inherited.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/00.1_Step_MINUS-1_Amendment_2026-11-11.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Step_3.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/City_and_District_Research_Topics.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Book_Extraction_Index.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md  [range 1707-1715] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — each reader continued by `SendMessage` with the other two outputs

| Reader | Reply (copied here) | Lines |
|---|---|---|
| A | `.t8_03_Step_3_round3_readerA.md` | 178 |
| B | `.t8_03_Step_3_round3_readerB.md` | 178 |
| C | `.t8_03_Step_3_round3_readerC.md` | 229 |

**Verdicts, as each reply's own verdict lines state them: all six CONSISTENT.** Each reply's sections 5 and 6 (disposition differences; recomputed figures) went to the merge writer whole.

## The merge — one fresh writer (`M-246`)

Agent `afa5ade36b7b2e2b3`; brief `.t8_03_Step_3_merge_brief.md`; output `03_Research.md`.

## Quotation audit — raw output, whole (110 lines; `.t8_03_Step_3_quotation_audit_raw.txt`)

```
pass audited : Casey
corpus mode  : default (own pass excluded)
corpus files : 7119   chars: 114,937,763
files audited: 03_Research.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 105
NOT FOUND in corpus: 84
  of those, in TABLE CELLS : 1
  of those, in PROSE       : 83

  [03_Research.md:37]           one buoy drifted out following an early october breakout
  [03_Research.md:37]           drifted across the vincennes bay polynya during a breakup event beginning 12 october
  [03_Research.md:37]           drifted westward following breakup on 19 november, crossing the vincennes bay polynya on 21 november
  [03_Research.md:37]           drifted out of the fast ice on 1 november and crossed the vincennes bay polynya on 2 november
  [03_Research.md:37]           150-200 km of sea ice separating the polynya from the open-ocean ice edge
  [03_Research.md:37]           forms on the near-coastal ocean off each of the three
  [03_Research.md:38]           is the least supported part of the leg (b; c in round 3): no source read says when a ship can pass the pack at this coast. s2-26 (
  [03_Research.md:47]           duration is in general more highly correlated to ice advance rather than retreat across most of east antarctica
  [03_Research.md:47]           within this coastal zone, the largest variability in days of retreat and ice season duration coincides with polynya locations
  [03_Research.md:47]           areas of low sea ice variability in the coastal zone correspond to regions of fast ice
  [03_Research.md:56]           coastal polynyas are recurring regions of open water within sea ice
  [03_Research.md:56]           sea ice break-up potential by locally generated wind waves in a polynya
  [03_Research.md:56]           appear to be sufficiently steep to break the ice at the polynya edge
  [03_Research.md:63]           (a-15); household groceries, construction materials and municipal equipment were left on the dock at the transfer port (b-12)
  [03_Research.md:63]           (a-15, b-12, c-8); a local voice in the article
  [03_Research.md:72]           https://en.wikipedia.org/wiki/northern delivery ( sourced , c-10; re-read a-r3-5)
  [03_Research.md:72]           controlled by the state and financed from the national budget
  [03_Research.md:72]           shipping costs currently account for 70% of the final price of fuel
  [03_Research.md:88]           after 5-month wait, forced fuel ration, barge arrives in st. paul
  [03_Research.md:95]           klondike gold rush national historical park, https://home.nps.gov/klgo/learn/historyculture/tonofgoods.htm ( sourced , b-48): the 
  [03_Research.md:104]           accident in alchevsk may boost communal reform
  [03_Research.md:104]           right now we're wearing our winter coats in our apartments
  [03_Research.md:104]           ukraine to evacuate children from freezing city
  [03_Research.md:104]           reports said heating has been restored to about one-third of alchevsk 45,000 residents
  [03_Research.md:135]           northern russian fishing and hunting hut: modern rules and transgressions
  [03_Research.md:135]           the hut, which usually has several owners, is considered an object of the customary law
  [03_Research.md:135]           joint ownership and maintenance of huts are regulated by the rules established by the community
  [03_Research.md:135]           violation of these rules entails the closure of the huts
  [03_Research.md:135]           conflicts both within the community and between the community and the strangers
  [03_Research.md:148]           ( 02 spine.md l103) holds on the nautical measure, but the months are late october to mid-february , not november to february; cou
  [03_Research.md:156]           meltwater hampers summer sledding season in greenland
  [03_Research.md:156]           it was so warm during the day, and the snow was so soft, that we switched to night kiting
  [03_Research.md:156]           daytime heat also forced a shift in schedule
  [03_Research.md:165]           frá þeim tíma mega 12 ára börn og yngri vera úti til klukkan 22.00
  [03_Research.md:165]           on november 30, 2025 the navigation in saint petersburg was finished
  [03_Research.md:165]           the new navigation season will open on april 10, 2026
  [03_Research.md:174]           sleep in the land of the midnight sun and polar night: the tromsø study
  [03_Research.md:183]           there is an annual average wind speed of 25km per hour. gale winds are predominantly from the east, off the polar ice cap. blizzar
  [03_Research.md:183]           the very strong katabatic flow appears to be related to the production of a supply of cold air inland from casey
  [03_Research.md:183]           the approach of a strong cyclonic system toward the coast and a blocking system downstream
  [03_Research.md:193]           precipitation as rain has been recorded in the summer and recently in july 2008 and july 2009
  [03_Research.md:200]           antarctica's newest research station holds a lesson for snowy cities
  [03_Research.md:200]           the need for constant vehicle access to stage expeditions also meant the building had to sit on the ground
  [03_Research.md:200]           in a climate where blizzards can last for days, a wind deflector reduces the amount of effort needed to clear the snow
  [03_Research.md:200]           quantifying snow drift on arctic structures: a case study at summit, greenland, using uav-based structure-from-motion photogrammet
  [03_Research.md:200]           wind speeds as low as 6 m/s (13 mph) can entrain and move snow
  [03_Research.md:210]           alaska science forum, 25 january 1988, https://www.gi.alaska.edu/alaska-science-forum/snow-wont-stay-still ( sourced , a-52)
  [03_Research.md:210]           a fence completed in 1982 controls drifts at a second village
  [03_Research.md:210]           water in wainwright is currently hauled by tank truck from lakes
  [03_Research.md:217]           så snart det kommer tilstrekkelig med snø til at vi får fokkskavler og mister sikta
  [03_Research.md:217]           (last until spring); fixed departures for safety
  [03_Research.md:217]           (the contractor knows how many cars go out onto the plateau)
  [03_Research.md:217]           (they can filter out cars and drivers not equipped for the winter). (b) nina berglund
  [03_Research.md:217]           newsinenglish.no, 6 april 2021, https://www.newsinenglish.no/2021/04/06/storms-stranded-holiday-motorists/ ( sourced , b-30, c-20)
  [03_Research.md:217]           travellers must check in with the firehouse prior to departure and again upon return
  [03_Research.md:235]           nuclear weapons journal issue 2, 2009, pp. 20-21, los alamos, https://cdn.lanl.gov/files/nwj2-09 62c62.pdf ( sourced , read to sta
  [03_Research.md:235]           most personnel involved with the original production process were no longer available
  [03_Research.md:235]           some of the historical design records were vague and that some of the new equipment was equivalent, but not identical, to the old 
  [03_Research.md:235]           historical information indicated that occasionally there were production problems with fogbank for which the root cause could not 
  [03_Research.md:235]           the historical fogbank production process was unknowingly based on this essential chemical being present in the feed material. as 
  [03_Research.md:235]           https://en.wikipedia.org/wiki/fogbank ( sourced , b-32, c-32; re-read b-r3-2)
  [03_Research.md:235]           implicitly relied upon in a downstream process
  [03_Research.md:235]           nnsa spent 69 million to address fogbank production problems
  [03_Research.md:235]           nnsa did not lose the recipe for fogbank or forget how to produce it
  [03_Research.md:244]           share techniques, tricks, quick fixes, errors in the documentation, schematics
  [03_Research.md:244]           telling a story of a machine's failure is necessary to gain proper advice from a colleague
  [03_Research.md:244]           rocketdyne even sought to capture the knowledge inside the heads of the people who designed and manufactured the engines
  [03_Research.md:269]           super-diversity vs. assimilation: how complex diversity in majority-minority cities challenges the assumptions of assimilation
  [03_Research.md:269]           children of immigrants nowadays no longer integrate into the majority group, but into a large amalgam of ethnic groups
  [03_Research.md:269]           https://en.wikipedia.org/wiki/suriname ( sourced , first 100,000 of 290,764 characters, b-36): 2012 census, the largest group 27.4
  [03_Research.md:269]           an official language prevailing in government, business, media and education; an english-based creole as a widely used lingua fran
  [03_Research.md:269]           immigrants continued to speak their native tongues
  [03_Research.md:280]           bailey peninsula is an area of rock exposures and permanent snow and ice fields lying between newcomb bay and o'brien bay, two kil
  [03_Research.md:280]           https://en.wikipedia.org/wiki/windmill islands ( sourced , a-49, b-39): the group is
  [03_Research.md:295]           cold monomictic lakes and ponds occur throughout the windmill islands region in bedrock depressions and are usually ice-free durin
  [03_Research.md:295]           (a-69); two large lakes lie 500 m west of the protected area (c-38). (b) mcminn 2000
  [03_Research.md:295]           ice cover ( 0.5 m) was almost as thick as the lake depth
  [03_Research.md:304]           it closes for around six weeks at the height of summer, due to warmer temperatures causing sub-surface melt
  [03_Research.md:330]           reno divorce history (university of nevada, reno), https://renodivorcehistory.org/themes/law-of-the-land/how-it-worked/ ( sourced 
  [03_Research.md:330]           https://renodivorcehistory.org/ p 159 ( sourced , a-54, b-46): six months at statehood (1864); one year in 1913, after which
  [03_Research.md:345]           the state is planning on setting up shelters where truck drivers can pull over in the extreme weather
  [03_Research.md:416]  [CELL]  the least supported part (no source gives ship passage). the spine stands; its opening clause reads as variable and two-staged, an
  [03_Research.md:559]           the next). b: the cluster about a fifth, health care larger than transport and warehousing. round 3: both stand by measure
  [03_Research.md:563]           ( .t8 03 step 3 readerc.md l188). b (round 3): no admitted line says so. written: not carried; c's

⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Triage of the misses** (agent `orchestrator`; table `.t8_03_Step_3_quotation_triage.md`): 84 misses: 62 DOT (60 by script, 2 by hand), 22 CONNECTIVE, 0 SELF, **0 MISQUOTE**. Nothing changed by the triage.

## American English sweep — raw output, whole

```
### Before the fix (15 hits; 03_Research.md and Casey_Research_Log.md)
03_Research.md:63:cancelled
03_Research.md:63:cancelled
03_Research.md:88:cancelled
Casey_Research_Log.md:52:cancelled
Casey_Research_Log.md:53:cancelled
Casey_Research_Log.md:53:cancelled
Casey_Research_Log.md:120:cancelled
Casey_Research_Log.md:120:cancelled
Casey_Research_Log.md:121:cancelled
Casey_Research_Log.md:121:cancelled
Casey_Research_Log.md:175:cancelled
Casey_Research_Log.md:177:cancelled
Casey_Research_Log.md:209:metres
Casey_Research_Log.md:268:cancelled
Casey_Research_Log.md:330:cancelled
### Fixed: 8 in own words (cancelled → canceled: 03_Research.md L63, L88; Casey_Research_Log.md L52, L53, L120, L121, L175, L330). Kept by rule: URL slugs and logged search strings.
### After the fix (7 hits, all in a URL slug or a logged search string)
03_Research.md:63:cancelled
Casey_Research_Log.md:53:cancelled
Casey_Research_Log.md:120:cancelled
Casey_Research_Log.md:121:cancelled
Casey_Research_Log.md:177:cancelled
Casey_Research_Log.md:209:metres
Casey_Research_Log.md:268:cancelled
```

## Notes

**Second output: the research log.** `Cities/Research_Logs/Casey_Research_Log.md` (new file, 522 lines; one session entry, 215 rows). Written by the same merge writer under the same brief.

**Search strings, verbatim: `scratchpad/casey/tools/check_log_strings.py`, run after the merge (raw, whole, `.t8_03_Step_3_logstring_check_raw.txt`):**

```
  .t8_03_Step_3_readerA.md: 71 rows
  .t8_03_Step_3_readerB.md: 60 rows
  .t8_03_Step_3_readerC.md: 62 rows
  .t8_03_Step_3_round3_readerA.md: 6 rows
  .t8_03_Step_3_round3_readerB.md: 10 rows
  .t8_03_Step_3_round3_readerC.md: 6 rows
checked 215 strings; missing 0
```

Re-run after the spelling fix: `checked 215 strings; missing 0`.

**The research log's own quotation audit** (`--files ../../../Research_Logs/Casey_Research_Log.md --own-pass`), raw output, whole (`.t8_03_Step_3_quotation_audit_log_raw.txt`):

```
pass audited : Casey
corpus mode  : default (own pass excluded)
corpus files : 7119   chars: 114,937,763
files audited: Casey_Research_Log.md
own-pass mode: a quotation may also be found in this pass's OTHER files (never in its own file)

=== POSITIVE CONTROLS ===
  [easy                      ] FOUND     a terminus is nobody's midpoint
  [HARD - blockquote wrap    ] FOUND     A pass may not proceed to Step 5 with a NEVER CITED row
  [HARD - outside Worldspace ] FOUND     Paste raw QA scan output into the QA block. Never summa
  [HARD - case mismatch      ] FOUND     YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR Y
  [HARD - long wrapped       ] FOUND     Different content is not differentiation; a different q

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

=== QUOTATION AUDIT ===
fragments tested (single-line, ellipsis-split, >=7 words): 5
NOT FOUND in corpus: 0
  of those, in TABLE CELLS : 0
  of those, in PROSE       : 0


⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and
  connective prose captured between two adjacent quotations, both show here.
  Confirm each at source before calling it a defect.
```

**Web calls** (each reader's own count): Round 1, A 71, B 60, C 62 (of 80 each); Round 3, A 6, B 10, C 6 (of 15 each); 215 in all, every one a row of the log. Session total by `Tools/web_quota_count.py --tasks <this session's tasks folder>` at 11:28: `WebSearch: 134 | WebFetch: 97 | TOTAL: 231` (of 1,000).

**Spelling:** the sweep covers both outputs; 8 own-word hits fixed, 7 kept (URL slugs and logged search strings, never changed). The before-and-after raws are `.t8_03_Step_3_amer_sweep_raw.txt` and `.t8_03_Step_3_amer_sweep_after_raw.txt`, combined in `.t8_03_Step_3_ame_sweep_raw.txt`.

**Snags (the recording law).** (1) Reader A, Round 3: wrote a temporary arithmetic script in its staging folder and deleted it, against "create no other file" (its reply, snag 4). (2) Readers A and B kept fetched source text and a script in their staging folders in Round 1 (`readerA/scripts`, `readerB/src_summit`, `readerB/src_voermans`, `readerB/sun.py`): inside their staging folders, as the brief allows. (3) My first version of the string checker took column 3 of every table under a "## 3" heading; it would have read the wrong tables in the Round 3 replies, so it was rewritten to find the column whose header says "verbatim" under a search-log or web-calls heading before the merge returned (counts then matched every reader's stated total). (4) The research log folder's `README.md` index has no Casey row; the merge brief barred edits to it, and it is not added here (Casey log, CL-17).

**Not run on this unit, and why:** the handoff audit and the phase-discipline check work on Step 4's phase files; they run from Phase 2 on. This record does not grow after its line counts were taken (standing line 8).
