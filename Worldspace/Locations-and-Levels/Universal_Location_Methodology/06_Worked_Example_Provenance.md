# Worked-Example Provenance — which rules carry which location's answers

**Added 2026-08-30, after Zhongshan Run 3, to solve a problem that run created.**

---

# The problem

**A methodology improves by absorbing worked examples.** A rule stated abstractly is advice; the same rule with
*"here is the pass where this went wrong and here is the number that caught it"* is procedure. **Run 3's findings
were written back into `00`–`05` and `00f` in exactly that form, and the files are much stronger for it.**

**But the methodology read is MANDATORY** *(project `CLAUDE.md`, and `00_RUNBOOK.md` Step 1)*. So:

> ### ⚠ **A cold run on location X will be handed X's own prior conclusions by the very files it is required to
> read before it may open anything else.**

**This is finding M-4 at maximum severity, and it bites hardest in exactly the case the developer most wants to
run: the SAME location again, to isolate a methodology change as the variable.**

---

# The rule

> ## Read every rule. Skip the worked examples belonging to YOUR OWN subject location.
>
> **A worked example is evidence for a rule, not an input to a pass.** A pass needs the rule. **It must not
> take the example's *content* as a starting point when the example is about the location it is writing.**
>
> **Three obligations:**
>
> 1. **Before the mandatory read, check this manifest for your subject location.** If it appears, note which
>    sections are quarantined *for you specifically* — everyone else reads them normally.
> 2. **Read the rule; stop at the example.** The rules are written to stand without their examples; where one
>    does not, that is a defect in the rule and should be recorded.
> 3. **If you cannot avoid absorbing an example** — some are inline and unavoidable — **tag every finding that
>    matches it `[SELF-ORIGINATED]`** per `05` §6.1, and treat the match as **corroboration, never derivation.**
>
> ### ⚠ Obligation 2 was previously unrunnable, and the fix is now structural, not procedural
> **Found 2026-08-31, from a real case: "stop at the example" presumes a reading mechanism that can omit a
> mid-file section while still reading the rule around it.** No such mechanism exists for a linear file read —
> a cold session (or a human skimming the file) sees the whole page, rule and worked example together, in one
> pass. A session following obligation 2 in good faith was exposed to a manifested example anyway, purely
> because the file-reading tool has no way to skip a paragraph.
>
> **The fix, applied 2026-08-31: location-specific worked examples now live in a separate per-location archive
> file** (e.g. `Test_Runs/Zhongshan_Extracted_Worked_Examples.md`), **cross-referenced from the rule by a bare
> pointer, not quoted inline.** A cold session can now genuinely decline to open the archive file — obligation
> 2 is mechanically achievable going forward, for any example added under this convention. **This is now the
> required form for a new worked example, not merely a suggestion**: add the rule's general form to the rule
> file, add the concrete instance to that location's own archive file, and link one to the other. Obligation 3
> (tag and treat as corroboration) still governs the older examples predating this fix, and any case where a
> genuinely unavoidable inline illustration remains necessary for the rule to be legible at all.

**And the reciprocal obligation on anyone updating the methodology: add your worked examples to this manifest in
the same commit.** An unmanifested example is invisible contamination for the next same-location run.

> **Why not simply anonymize the examples?** **Because M-4 established that anonymizing is worse.** An unnamed
> worked case *("a city famous for being the place people move to…")* contaminates just as effectively and
> **removes the reader's ability to know they have been contaminated.** **A named example can be quarantined;
> an unnamed one is absorbed as general knowledge.** **Name them, and manifest them.**

---

# MANIFEST

## Zhongshan — added 2026-08-30 from Run 3 *(cold, complete)*

**A cold pass on Zhongshan must skip the example content in every row below.** The rule in each case stands
without it.

| File | Section | What the example reveals about Zhongshan |
|---|---|---|
| `02` | **§4.0** *(shape is input-set dependent)* | Its two opposite shape readings; that its known institutions are all maintenance obligations |
| `02` | **§4**, the `cost-absent` row | Its shape; its characteristic failure mode |
| `02` | **§4.1**, the `diffuse`-prevents-a-witness note | Its deficit address, and the reasoning behind it |
| `02` | **G8** worked case *(retained from Run 1)* | **Shirayuki's** retention figure — quarantined for a *Shirayuki* pass, not a Zhongshan one |
| `01` | **§5.3a #1**, the own-eras upgrade | **Its entire Phase 5b three-era answer, in full** — the most damaging single entry here |
| `03` | **Phase 8C**, the general-population note | Its music finding, both the wrong version and the corrected one |
| `04` | **Gate 6** note | That its swap-test partner produced a canon collision |
| `04` | **Gate 9** second-pass note | **Its membership mechanism and the shadow inside it, in full** |
| `04` | **Gate 11** first-fire note | **Its population, area, and density figures**, and that its texture was wrong |
| `04` | **Gate I** count note | Its Originated:Inflected ratio and its national-observance finding |
| `04` | **Part IV**, cold-read note | Its two canon bugs *(the polar-night and exile-duration figures)* |
| `00_RUNBOOK` | **Status note**; **Step 2.4**, **Step 2.6**; **Step 3.7** | Its overall verdict and the density check |
| `00f` | **`unmet`/`declined` split** | Its panel counts |
| `05` | **§6.1a–c** | Which of its input files were contaminated and how |

### ⚠ And the honest assessment for a Zhongshan re-run

**This manifest is long, and skipping every row still leaves a Run 4 partially contaminated** — the rules
themselves now encode Zhongshan-shaped lessons *(a shape called `cost-absent` exists because of it; Gate 11 now
says "divide population by area" because of it)*.

> **So a Zhongshan Run 4 is NOT a clean replication and must not be reported as one.** It is a **methodology-delta
> test**: *given an author who knows the improved procedure but has quarantined the prior findings, what does the
> improved procedure surface that the old one did not?* **That is a real and valuable question — it is simply a
> different question from Run 3's.**
>
> **The genuinely clean test of the updated methodology is a location that has never been passed.**
> **Run both, and do not confuse their results.**

---

## Zhongshan — added 2026-08-31 from Run 4 *(cold, incomplete — Phases 0–7 + gates + panel; Phases 8–10, Gate 6,
and the differentiation table not run)*

**A future cold pass on Zhongshan must ALSO skip the content below**, in addition to everything already
manifested from Run 3 above. Run 4 produced its own worked-example-quality content, mostly in the methodology
rule files' observations log rather than in `00`–`05` themselves (since Run 4 did not implement its findings
back into the rules — see its Step 9 note), but two items are genuine contamination risk if read as examples:

| File | Section | What the example reveals about Zhongshan |
|---|---|---|
| `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | **M-25** | The specific own-eras axis chosen for Run 4's Phase 5b ("what does 'the claim' mean, at founding vs. now") and its two-state result |
| `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | **M-26** | Zhongshan's Census I→II figures and the correct Status reading (`Living`, not `Growing` or `Declining`) |
| `Test_Runs/2026-08-30_Zhongshan_Run4_Cold_Methodology-Delta/` | **all of it** | Run 4's full Phase 1–7 content: the capability shape (STANDING COST populated by G2+G4, not `cost-absent`), the highway-tri-junction relational finding, the no-arrival-scene/no-Saint "untested legitimacy" Phase 6 finding, the water-basin shadow and its language-redirect Denying-Innocent-One verdict |

**If `01`, `04`, or `00f` are later edited to absorb Run 4's M-25/M-26 findings as worked examples** (per Step
9.4's still-outstanding implementation task), **add the relevant section to the table above in the same
commit** — this is the same reciprocal obligation `06` already states, applied to itself a second time.

---

# ⚠ THE OTHER CHANNEL: AUTO-LOADED MEMORY

**Added 2026-08-30, after a readiness check found this and nothing else would have.**

**Every quarantine instrument in this methodology — the do-not-open lists, `05` §6.1, the manifest above —
assumes a session *chooses* to open a file.** They govern **pull**.

> ## **Memory is PUSH. It arrives before you have decided anything, and no do-not-open list can intercept it.**

**The measured case.** A memory entry recording the *technique* of applying Enneagram sub-classifications to a
city's personality had inlined **its own results** — each Tri-City's three-axis verdict, plus one of the
cluster's signature axis phrases verbatim. **It was indexed in the auto-loaded memory index.** A cold pass on
that city would have been handed the withheld Enneagram read, and the single most damaging entry on its own
quarantine list, **before opening a single canon file.**

**Ten further memory entries carried culture-conclusion vocabulary about the same cluster.**

## The rules, now standing

1. **A memory entry about a location must record ATTRIBUTES and STATUS, never culture-pass conclusions.**
   Founding mechanism, dates, names, census, corrections made, what is still open — yes.
   *"Its character is X," "its temperament reads as Y,"* a personality triple, a signature phrase — **no.**
   **Point to where the conclusion lives instead.** *(`project_universal_location_methodology_test_runs` has
   followed this deliberately from the start and is the model.)*
2. **A technique memory records the technique, not its results.** The results have a home in the repo, where a
   quarantine can actually govern reading them.
3. **Where an entry genuinely needs the conclusion** — a rule taught by worked example, a bug-check log —
   **it carries a contamination banner immediately after its frontmatter**, so the warning arrives in the same
   block as the content. Three entries now do.
4. **Before any cold run, scan memory for the subject location** and check that every hit is either
   attribute-only or banner-warned. **It is a two-minute check and nothing else performs it.**
   > **This is now `00_RUNBOOK.md` Step 10.1, item 1 — a standing step, not a suggestion.** Step 10 runs in
   > both directions: **outbound** at the end of a pass, by whoever hands off; **inbound** at the start, by the
   > session receiving it. **Both halves scan memory, because the outbound author can fix an entry and the
   > inbound reader can only band it.**

**Current state for Zhongshan / Sinheung / Shirayuki:** one technique entry rewritten to withhold its results ·
one entry surgically stripped of a leaked personality triple · **four entries banner-warned** *(a fourth,
`project_refugee_affinity_verification_pass.md`, found and banded 2026-08-31 during Run 5's inbound check — see
M-32)* · the rest verified attribute-only.

## Sinheung — added 2026-08-31 from Run 5 *(cold, complete — all eleven phases, sixteen gates, Review Panel)*

**A future cold pass on Sinheung must skip the example content in every row below.** The rule in each case
stands without it.

| File | Section | What the example reveals about Sinheung |
|---|---|---|
| `02` | **§4.1**, the new "in a neighbor's present" address row | Sinheung's own founding-claim deficit, in full — the worked case named in that row |
| `03` | **Phase 6 §C**, the fourth death-outsourcing reason | Sinheung's own asymmetric-record-keeping/output-legitimacy reasoning |
| `03` | **Phase 9D**, the "not a target ratio" clarification | Not itself Sinheung-specific content, but adjacent to Phase 9's "made here/made elsewhere" robot finding and the output-proven cross-population axis — both quarantined for a Sinheung re-run |
| `00_RUNBOOK` | Status note's Gate 6 convergence-mode addition | Sinheung's own central finding and its word-for-word match against the withheld culture sheet |
| `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | **M-35, M-36, M-37** | Sinheung's central finding, its Zhongshan-comparison reconciliation, and its Phase 6 death-outsourcing reasoning, all in full |
| `Test_Runs/2026-08-31_Sinheung_Run5_Cold/` | **all of it** | Sinheung's complete Phase 0–10 content, all sixteen gates, and the full Review Panel run |

## Highway 37 — added 2026-08-31 from Run 6 *(cold, complete — all eleven phases, sixteen gates, Review Panel,
base Zodiac Lens; the Elemental/Planetary Cross-Check extension deliberately deferred)*

**A future cold pass on Highway 37 must skip the example content in the row below.** The rule stands without
it. **Note this run's own structural difference from every prior entry on this page:** Highway 37 had no
completed culture pass before this run, so there is no *pre-existing* content to quarantine from earlier
sessions — only this run's own output, listed here for the benefit of any *later* same-location re-run.

| File | Section | What the example reveals about Highway 37 |
|---|---|---|
| `01_Frame_Typology_and_Inheritance.md` | **§4.1**, "THE DEFAULT FRAME IS NEUTRAL" | Cites this run's own mid-pass correction (an early draft defaulted to the post-war frame unasked) as the rule's origin case, including the corrected Frame Declaration's own content |
| `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | **M-43 through M-49** | This run's inbound-check results, its shape/input-set boundary case, the frame correction, the axis-naming and asymmetry gate catches, the minigame-derivation move, and the empty-quarantine structural note |
| `Test_Runs/2026-08-31_Highway37_Run6_Cold/` | **all of it** | Highway 37's complete Phase 0–10 content, all sixteen gates, the full Review Panel run, and the base Zodiac Lens |

## Cape Adare — added 2026-08-31 from Run 7 *(cold, complete — all eleven phases, sixteen gates, Review Panel;
the Zodiac Lens deliberately deferred to a future follow-up pass)*

**A future cold pass on Cape Adare must skip the example content in the rows below.** The rules stand without
them. **Note this run's own real, substantial quarantine** (unlike Highway 37's vacuous one) — a future
same-location re-run also needs the admissibility table in `00_Frame_and_PreFlight.md` §2, not only this page.

| File | Section | What the example reveals about Cape Adare |
|---|---|---|
| `05_The_Input_Contract.md` | **§6.1d**, "A `Specs/` file is not categorically safe either" | Cites this run's own self-caught contamination event in full — the Character & Culture section's own content, and the reasoning that corrected it |
| `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | **M-50 through M-54** | This run's quarantine-build catches, the near-miss on fabricated scan output, the neutral-frame stress test, and the input-scarcity-vs-methodology-failure diagnostic |
| `Test_Runs/2026-08-31_CapeAdare_Run7_Cold/` | **all of it** | Cape Adare's complete Phase 0–10 content, all sixteen gates, and the full Review Panel run |
| **`Worldspace/Canon_Gap_Resolution_Method/03_Deposit_Discipline.md`** | **§1's worked table — already fenced** | Cape Adare's own conclusion content (civic character, pace, instrumentation), used there to teach the attribute/conclusion classification. **Fenced with `<!-- CGRM:CONCLUSION-TIER -->` markers**, so it can be excluded mechanically rather than by noticing: `awk '/CGRM:CONCLUSION-TIER:START/{skip=1; next} /CGRM:CONCLUSION-TIER:END/{skip=0; next} !skip' <file>` |
| `Worldspace/Canon_Gap_Resolution_Method/00_RUNBOOK.md` | **LAW B** | The Cape Adare deposit chain narrated in full, as the recorded failure grounding that law |
| `Worldspace/Canon_Gap_Resolution_Method/Test_Runs/2026-08-31_Seed_CapeAdare_and_Highway37.md` | **all of it** | Cape Adare's and Highway 37's triaged gap lists — the *questions*, not answers, but a re-run should not be handed its predecessor's framing of what was missing |

> ### ⚠ A second system now carries Cape Adare examples, and this is why it is listed here
> **Added 2026-08-31.** The Canon Gap Resolution Method was built the same day Run 7 finished, and its founding
> recorded failure *is* the Cape Adare deposit chain — so its rule files necessarily discuss Cape Adare's own
> conclusion content. **That made a second methodology into a contamination vector for the same location**,
> which is exactly the problem this manifest exists to track. **The content was fenced at the time of writing
> rather than after the fact**, and is registered here so a future cold pass finds it through the check it
> already runs, rather than having to know that a second system exists.

## Mountain Pass Airport — added 2026-08-31 from Run 10 *(cold, complete — all eleven phases, sixteen gates,
Review Panel; first Installation-type location run under this methodology)*

**A future cold pass on Mountain Pass Airport must skip the example content in the rows below.** The rules
stand without them. **Note this run's own structural difference from every prior entry on this page**:
Mountain Pass Airport had no completed culture pass before this run (nor any Specs/Local_Culture file of
its own at all), so there is no *pre-existing* content to quarantine from earlier sessions — only this run's
own output, plus the tooling-incident record, listed here for the benefit of any *later* same-location
re-run.

| File | Section | What the example reveals about Mountain Pass Airport |
|---|---|---|
| `Cultural_Synthesis_Techniques.md` | The Zodiac Lens's own §4 stopping-criterion note ("Added 2026-08-31, Run 10... M-78") | Cancer's own selective-actualization finding, in full — its specific mythic-register hits and the domestic-register null |
| `Cultural_Synthesis_Techniques.md` | The Elemental/Planetary Cross-Check's own agent-type caution note | The fork-cascade tooling incident's own specific detail, including the fabricated Libra finding and the real recovery method |
| `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | **M-74 through M-80** | This run's own neutral-frame catch, the chamber-departure and governance-vacuum convergences in full, the Gate I Independence Day catch, and the Type-fidelity result |
| `Test_Runs/2026-08-31_MountainPassAirport_Run10_Cold/` | **all of it** | Mountain Pass Airport's complete Phase 0-10 content, the full Zodiac Lens (all twelve signs), all sixteen gates, and the full Review Panel |

## Sanay (and the Sanay Maritime Shipping Port specifically) — added 2026-08-31 from Run 11 *(cold, complete —
all eleven phases, sixteen gates, Review Panel, base Zodiac Lens; the first pass on a NAMED SUB-LOCATION whose
parent is a fully-developed Settlement)*

**A future cold pass on Sanay, the Sanay Shipyard/Maritime Shipping Port, or any other named sub-location of
Sanay must skip the example content in the rows below.** The rules stand without them.

> ### ⚠ This entry closes a real gap this run itself found (M-82), not merely adds a new one
> **`02_Generators_Capability_and_Symbols.md` §6.3's pairing-relation worked-examples table has cited Sanay's
> own symbol assignment — Jupiter + Electromagnetism, "orthogonal to complementary... it holds the Arcanet
> nexus" — since before this run, and it was NEVER manifested here.** Run 11 discovered this the hard way,
> reading it as required pre-Phase-1 material with no manifest entry to warn it off. **This row is therefore
> retroactive** — the example predates Run 11, but the manifest omission does not, and it is fixed now.

| File | Section | What the example reveals about Sanay |
|---|---|---|
| `02_Generators_Capability_and_Symbols.md` | **§6.3**, the pairing-relation worked-examples table | Sanay's own symbol pair (Jupiter + Electromagnetism) and its derived rationale ("orthogonal to complementary... holds the Arcanet nexus, where the two registers meet exactly") — **pre-existing content, not added by Run 11; the manifest gap it exposed is what Run 11 found and fixed (M-82)** |
| `05_The_Input_Contract.md` | **§6.1a**, the line/character-anchoring sub-rule (M-83) | Cites the exact line numbers of `02` §6.3's Sanay example (line 562 admissible, lines 563-564 inadmissible) as its own worked case |
| `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | **M-82 through M-86** | This run's two contamination events (the `02` §6.3 exposure; the prep document's own descriptive-section exposure), the line-anchoring mitigation technique, the Band-0-vs-presence self-correction, and the seven-sign Zodiac Lens convergence on the port's manual/workaround dual-authority mechanism, all in full |
| `Test_Runs/SanayShipyard_ColdRun_Prep_2026-08-31.md` | **the descriptive "not a virgin location" section specifically** (NOT its own 22-step line-ranged reading sequence, which remains safe and is the intended path) | Quotes withheld-file conclusion fragments directly — "a Guangzhou-Canton-System bounded-contact zone," "'function over sentiment'... a defended civic value" — flagged as M-85; **a future session should follow this document's own numbered reading sequence, never its descriptive framing prose, if picking up Sanay again** |
| `Test_Runs/2026-08-31_SanayMaritimeShippingPort_Run11_Cold/` | **all of it** | The port's complete Phase 0-10 content, all sixteen gates, the full base Zodiac Lens (all twelve signs) with its cross-sign synthesis, and the full Review Panel |

## Casey — added 2026-09-02 from Run 12 *(cold run ABANDONED before Phase 0 — contaminated at the starting line; the session continued as a map-builder, not a deriver)*

> ### ⚠⚠ A FUTURE COLD PASS ON CASEY MUST SKIP THE LINES BELOW. **They were live and un-manifested when Run 12
> read them as `CLAUDE.md`-mandated required reading, and they are two of the four vectors that burned it.**

> ### ⭐ THIS ENTRY IS WRITTEN AS COORDINATES ONLY — AND THAT IS A CHANGE TO THIS FILE'S OWN FORMAT
>
> **Every row above carries a *"What the example reveals about \[location]"* column that restates the leaked
> content in order to describe it.** ***That column is M-85's failure mode built into the manifest's own
> schema*** — a session checking `06` for its subject, exactly as `RESUME_HERE.md` §3a item 2 instructs, is
> handed the very conclusions the entry exists to warn it away from. **The check contaminates the checker.**
>
> **This entry therefore names the coordinate and the TIER, never the content.** **Recommended for all future
> entries; existing rows left as they are rather than rewritten, since their locations are already spent.**

| File | Coordinate | Tier of what sits there | Action |
|---|--:|---|---|
| `00_RUNBOOK.md` | **§C.2, return-contract table** | **Conclusion — a civic-character claim, in the form of an illustrative section title** | ✅ **NEUTRALIZED 2026-09-02** — replaced with a bracketed generic placeholder. **No longer a leak; row retained as the record** |
| `01_Frame_Typology_and_Inheritance.md` | **§1, line 65** *(the Status-modifier table, `Resettled` row)* | **Frame-tier, with an evaluative gloss** — a Type modifier, plus a judgment about the corpus rather than about the city | ⚠ **RETAINED DELIBERATELY.** Genuinely useful methodology guidance, and a modifier a cold pass declares from `Specs/` at Step 0.1 anyway. **Skip line 65; do not delete** |
| `00_RUNBOOK.md` | **§C.3** | **None** — names Casey only as the subject of the contamination anecdote | No action |
| `Test_Runs/Casey_ColdRun_Prep_2026-09-02.md` | **all of it** | **None — verified.** The prep document is coordinates and rules throughout and leaked nothing. **It was written against M-85 and it held** | **Safe. It remains the intended entry path** |
| `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` | **M-87 – M-92** | **Names the vectors and the classes; states no Casey finding** | Safe |
| **The auto-loaded memory directory** | `project_casey_recheck.md` · `project_casey_bug_check_resolved.md` · `project_pink_lucy_migration_resolved.md` | **Conclusion — civic character and named Tier-3 particulars** | ✅ **BANDED 2026-09-02** |
| **`Background-Lore/Cities/Mirny_Subnet/Casey/Course_of_Events/`** | **the FILENAMES, not the contents** | **Conclusion — eleven authored titles, each a thesis** | ⚠ **NEVER `ls` THIS FOLDER.** Address by index; **11 files, 91–143 lines each.** See M-88 |

## Shirayuki — added 2026-09-02, PRE-EMPTIVELY, by a `Step −2` vector-1 sweep before the run *(no run yet)*

> ### ⭐ THE FIRST ENTRY IN THIS FILE CREATED BEFORE ITS LOCATION WAS RUN, RATHER THAN AFTER IT WAS BURNED.
> **Every entry above was written retroactively, by a session that had already been exposed.** **This one was
> written by an isolated reader that returned line numbers and a classification, to a session that still has
> no idea what is on those lines.** *(M-99.)*

> ### ⚠⚠ AND IT PROVES THIS FILE CANNOT BE THE FRONT LINE.
> ***`06` had no Shirayuki section. Its only two Shirayuki hits sit inside OTHER cities' entries.***
> **So the manifest check `RESUME_HERE.md` §3a item 2 prescribes would have returned CLEAN** — while three
> live conclusion-tier leaks sat in `02` and `05`. **M-82's fourth and fifth instances.** **Run the `Step −2`
> reader sweep; use this table as the durable record, never as the check.**

| File | Coordinate | Class | Action |
|---|--:|---|---|
| `02_Generators_Capability_and_Symbols.md` | ~~line 359~~ | ✅ **REMOVED 2026-09-03** | **No action — moved to `Test_Runs/Worked_Examples_Archive/`** |
| `05_The_Input_Contract.md` | ~~lines 211, 215~~ | ✅ **REMOVED 2026-09-03** | **No action — moved to the same archive** |
| `06_Worked_Example_Provenance.md` | line 77 | ATTRIBUTE | No action — inside another city's section |
| `06_Worked_Example_Provenance.md` | line 161 | ANECDOTE | No action |
| **auto-loaded memory** | 5 city-named entries | conclusion-tier | ✅ **BANDED 2026-09-02**; 33 further entries covered by the index's standing default-deny declaration |
| `00`, `01`, `03`, `04`, `README`, `Cultural_Synthesis_Techniques.md`, `Real-World_Basis_…`, `00b`, `00d`, `00f` | — | **CLEAN — verified, not assumed** | None |

> ### ⭐⭐ THIS ENTRY'S SKIP LIST IS NOW EMPTY — and that is the LAYERING LAW's first result
> **Developer instruction, 2026-09-03:** ***`01`–`05` and `README` name NO location, ever*** — worked
> instances move to `Test_Runs/Worked_Examples_Archive/`, reached by a bare pointer. **Verified mechanically:
> `grep -ciE '<subject>|<alias>'` returns 0 for `00`–`05` and `README`.**
>
> ***For THIS subject the rule files now deliver nothing*** — and M-103's *"the rule around the example leaks
> too"* problem dies with the example. **⛔ But vector 1 is NOT closed (M-125):** it sweeps `00`–`06` plus the
> disciplines, and **215 location-naming lines remain outside the six audited files.** **Keep running it.**
>
> ⛔ **The retired ranges are also now WRONG:** `02` is 621 lines (was 613), `05` is 708 (was 703).
> ***Do not apply them from memory.***

**Live coordinate maps and full status: `Pre-Contamination_Reviews/Shirayuki_Pre-Contamination_Review.md`
— §6 (3 city files) and §9 (14 registry files), both 3-of-3, both pinned.**

## *(Add further locations here as they are absorbed into the methodology.)*
