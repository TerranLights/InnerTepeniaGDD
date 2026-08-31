# ▶ RESUME HERE — Universal Location Methodology test runs

**Paused 2026-08-30, deliberately, by developer decision.** **Read this file first. It is written for a session
that has no memory of the previous work, which is the entire point.**

---

# 1. Why this was paused — the reason matters more than the status

**A re-run by the same session that performed the first run is not an independent test.** The author retains
the first run's findings in working memory and will inevitably re-notice them, so any "second pass" is partly
recall wearing the costume of derivation. **No protocol fixes this from inside the same session.**

**The developer's solution: close the session and resume cold.** A fresh session genuinely cannot remember,
which converts a contaminated re-run into a real one.

> ### ⚠ THE ONE RULE THAT MAKES THIS WORTH DOING
>
> **DO NOT OPEN THESE BEFORE WRITING YOUR OWN PASSES:**
> - `2026-08-30_Tri-Cities/` — **all of it.** This is Run 1's output.
> - `2026-08-30_Tri-Cities_Run2_Single-Location/01_Zhongshan.md` — Run 2's contaminated Zhongshan pass.
> - The three cities' `Local_Cultures/Mirny_Subnet/*.md` spec sheets, their
>   `City_Enneagram_Personalities/` reads, and `Tri-Cities_Overlap_and_Distinguishing_Guide.md`.
>   **These are prior culture-pass CONCLUSIONS and are inadmissible as input** per `05` §6.1.
>
> **Read all of the above ONLY AFTER your own findings are written**, as a check. **A match is corroboration;
> a mismatch is a finding site.** Opening them first destroys the experiment and produces a confident,
> coherent, worthless result.

---

# 2. Current state

| Item | Status |
|---|---|
| **The methodology itself** | **Updated and committed** (`0b226a9`). Single-location-first architecture, peer-free/peer-required split, kind-scoped circularity rule, census-change generator, Phase 5 reweighting, and 9 other changes from Run 1 are all incorporated. **Use it as it now stands.** |
| **Run 1** — `2026-08-30_Tri-Cities/` | **Complete for Phases 0, 1 and 5 only.** A three-city **co-write**. Its own files declare it exceptional. |
| **Run 2** — `..._Run2_Single-Location/` | **Protocol written; Zhongshan pass written; Sinheung and Shirayuki NOT started.** **Contaminated** — same session as Run 1. |
| **Observations** | `2026-08-30_Tri-Cities/OBSERVATIONS_and_Methodology_Findings.md` — **the single shared file for all runs.** |

---

# 3. What to do next — the exact task

**Create a new folder: `2026-08-30_Tri-Cities_Run3_Cold/`**

**Run all three cities — Zhongshan, Sinheung, Shirayuki — as separate single-location passes, cold.**
*(All three, not just the two unwritten ones: Run 2's Zhongshan is contaminated, so re-running it cold gives a
directly comparable third data point on the same city.)*

**For each city, in this order, finishing one completely before opening the next:**

1. **Read the methodology first** — `../../00_RUNBOOK.md` in full, then `01`, `02`, `03`, `04`, `05`.
   *(`CLAUDE.md` requires this and it is not optional.)*
2. **Run the `05` §7 pre-flight**, including the new **Configuration** and **provenance** lines.
3. **Read canon in the Step 0.4 triage order** — specs → symbol assignment → census *(and population change
   across both censuses)* → founding → physical-infrastructure attributes → **culture files LAST, as a check.**
4. **Write Phases 0 through 10.** Tag findings **`[new]`** / **`[re-derived]`** where you can tell.
5. **Then, and only then**, open the withheld conclusion files and record matches and mismatches.

**Cross-comparison last**, after all three exist — not during.

## The admissible input files *(safe to open at any time)*

```
Cities/Specs/{Zhongshan,Sinheung,Shirayuki}.md
Cities/City_Symbolic_Substrate/{Planetary_Symbols,Robot_Elementals,City_Symbol_Assignments}.md
Cities/Official_Population_Census.md                    ← Sections II and III; see the trap below
Cities/City_Megasheets/Mirny_Subnet/*/[City]_Physical_Infrastructure_Attributes.md
Background-Lore/Cities/Mirny_Subnet/*/                  ← vignettes = events, admissible
Cities/Local_Cultures/Mirny_Subnet/Tri-Cities_Region.md ← founding/amalgamation history only
```

---

# 4. Traps already paid for — do not rediscover these

1. **The census columns are `humans | robots | combined` at split-indices 4, 5, 6.** Index 3 is **Subnet**.
   An off-by-one here returns plausible, sensible, wrong numbers **without erroring**. **Hand-check one row
   against the file before trusting any figure.**
2. **Census I and II are BOTH pre-war.** The header says so explicitly. The drop between them is **orbital
   emigration, not war loss.** Retention = CensusII/CensusI.
3. **Read symbols from `Planetary_Symbols.md`, never from the name.** This project's **Saturn is "Mystery ·
   doesn't care to be fully known · no actual cohesion"** — derived from astronomy, *nothing* like
   astrological Saturn. Assuming otherwise inverts the whole reading.
4. **Score every quantitative claim against all 33 cities (z-score), not against the other two.** A
   human-vs-robot retention gap looked like a strong finding across three cities and evaporated at z ≈ 0.4
   nationally.
5. **The universe repo is OUTSIDE this repo** — `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`.
   A repo-local search will report "not found" confidently and wrongly.
6. **Verify before claiming novelty.** Two "canon never noticed this" claims in Run 1 were false, **and both
   were about the most interesting findings.** Treat any such claim as presumptively false until scanned, and
   run a proof-of-hit first so a zero is trustworthy.
7. **American English throughout** — standing global instruction. *(40 files elsewhere in the repo still carry
   British spellings; flagged, not fixed, since some may be quotations.)*

---

# 5. Canon facts settled, so they need no re-deriving

- **The Tri-Cities are Zhongshan (Chinese), Sinheung (Korean), Shirayuki (Japanese)** — Larsemann Hills, Mirny
  subnet, ~0.3–8 km apart, one shared airport, one Hwy 4/22/110 tri-junction, all founded by one Jeju-do court
  partition. *(An older memory saying "Soyuz" is stale; Soyuz was a retired placeholder for Sinheung.)*
- **Frame for these passes: pre-unification, Orbital Era, pre-war.** The three merge de facto ~2688 and
  legally by the ~2780s; the war is 2812. **The post-unification single-city pass is a separate document.**
- **Symbols:** Zhongshan = Saturn + Metal · Sinheung = **Uranus** + Electricity · Shirayuki = **Uranus** + Fire.
  **Sinheung and Shirayuki share a planet** — recorded in `Local_Robot_Culture/.../Shirayuki.md:271`, and
  **absent from the cluster's own differentiation guide.**
- **RESERVED — do not decide:** Sinheung's final in-universe name · the unified city's name · whether
  "Alternative Culture" belongs to Shirayuki alone · the disposal-of-the-dead mechanism · all proper names of
  people.

---

# 6. What the comparison is FOR

**Run 1 = co-write. Run 3 = cold single-location. Same three cities, same canon, different method.**

**The questions:**
1. **Does the single-location layout surface material the co-write missed?** *(Run 2's contaminated Zhongshan
   suggests yes — it reached the attribute canon the co-write never opened. **Needs cold confirmation.**)*
2. **What does the co-write buy that is worth its cost?** Run 1's regional finding required three simultaneous
   profiles and may be genuinely unavailable otherwise.
3. **How much of Run 1 was real derivation vs. author preference?** **Only a cold run can answer this**, and it
   is the reason the session was closed.

**Record everything in the shared observations file, including self-corrections** — the developer has asked
for those specifically, twice.
