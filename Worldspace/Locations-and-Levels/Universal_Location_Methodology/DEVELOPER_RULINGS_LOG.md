# DEVELOPER RULINGS LOG

> ## ⛔ WHY THIS FILE EXISTS
>
> **There was no rulings log.** Developer rulings were recorded wherever the conversation happened to be —
> measured 2026-09-13: **17** mentions in `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`, **14** in
> `00_RUNBOOK.md`, and the rest scattered across six more files. **A pass had no single place to check what it
> was bound by.**
>
> ⭐ **This is the same failure the `R-` docket had** *(see `City_Development_Passes/DOCKET.md`)*: a correct
> record, stored where nobody would look for it. **The fix is the same — one file, one line per item, written
> in the same turn the ruling is given.**
>
> ⚠ **Prior rulings are NOT yet back-filled here.** This log starts 2026-09-13. **Until back-filled, it is
> additive — it does not supersede or contain the earlier rulings**, which remain in `00_RUNBOOK.md`,
> `CLAUDE.md` and the observations file. **Do not read an absence here as an absence of a rule.**

---

# 2026-09-13

## `DR-1` · ⛔ **ROBOT ELEMENTALS — PULLED BACK FROM CANON** *(six of eight)*

**Developer, verbatim:**

> *"In terms of the city symbols … I'd like to review the Elementals that I didn't create (i.e., the ones other
> than Electricity and Electromagnetism), so that their in-universe meanings are more characteristically
> consistent with the universe these characters live in. So therefore, there's a strong possibility that the
> other Elementals will almost certainly gain different meanings, so **let's pull back on canon for the Robot
> Elementals specifically**."*

| | |
|---|---|
| ⛔ **Pulled back — MEANINGS not canon, under review** | **Earth · Air · Fire · Water · Wood · Metal** |
| ✅ **Unaffected — developer-authored** | **Electricity · Electromagnetism** |
| ✅ **NOT pulled back — and for a stronger reason than exemption** | **`Planetary_Symbols.md`** |

### ⭐ `Planetary_Symbols.md` is DEVELOPER-AUTHORED THROUGHOUT — the reason matters

**Developer, verbatim:**

> *"The reason why I'm not pulling back on the Planetary Symbols is because **I personally hand-authored all of
> them myself, so there's nothing to review**."*

⭐⭐ **This is not "the ruling happened not to name it." It is an affirmative statement of provenance, and it is
the strongest kind available** — *the developer wrote every entry.* **`05` §6.2's line is the test:
*"An outside process may propose; it may not settle."* Here the developer settled, originally, for all of it.**

**Consequences, which run further than this ruling:**

- ⛔ **`Planetary_Symbols.md` is RATIFIED.** Not by banner, not by root-table membership, not by use — **by
  authorship.** ⚠ **Root-table bookkeeping is still the developer's to do** *(`05` §6.3 rule 6: "the developer
  extends this list; a pass may not")*, **but the substance is settled and a pass may rely on it.**
- ⭐ **The two halves of `G1` now carry DIFFERENT weights, and a pass must not average them.**

| `G1` half | Source | Standing |
|---|---|---|
| **Planet** | `Planetary_Symbols.md` | ✅ **developer-authored, ratified** — readable for meaning |
| **Element** | `Robot_Elementals.md` | ⛔ **six of eight under review** — meaning is `RESERVED` |

> ⚠ **So `G1` is not uniformly weak; it is LOPSIDED.** A pass that records G1 as a single grade — *"THIN"*,
> *"corroboration-tier"* — **loses this distinction and will under-read the Planet half.** ⭐ **Record the two
> halves separately, always.** *(This also sharpens Reader B's Round 3 point that `Earth + Earth` "resolves to
> one term": the doubling is real, but **one of the two tokens is solid canon and the other is in flux** — the
> pair is not thin in one uniform way.)*

### What is pulled back, precisely

⭐ **The MEANINGS are pulled back. The ASSIGNMENTS are not the subject of this ruling.** Which city carries
which element still stands in `City_Symbol_Assignments.md`; **what that element MEANS in-universe is under
review and is expected to change.**

**Operative effect on every ULM/CST/RWBEM pass, immediately:**

- ⛔ **No pass may derive a finding from an Elemental's meaning** for the six under review. Not as a ground, not
  as corroboration, not as a prompt.
- ⛔ **`G1`'s Element half is RESERVED.** `05` §3's rule applies: the methodology must not decide it.
  *(`02` §6.0's instruction — "read definitions from the system's own files, never from the names" — **cannot
  be followed** for these six, because the file it points to is no longer canon. Reading meaning from the bare
  word "Earth" is exactly what that instruction forbids.)*
- ✅ **`G1`'s Planet half remains readable** from `Planetary_Symbols.md`, at whatever tier ratification leaves it.
- ⚠ **This strengthens, not weakens, the existing `05` §6.1c demotion.** G1 was already corroboration-tier and
  already excluded from `02`'s rule of three. **No generator count changes anywhere.**

### ⚠ Downstream, flagged not acted on

**Twelve files reference `Robot_Elementals`.** Two matter:

- **`Zhongshan_Opus/04_Phase_06_Meaning.md`** — the pass the developer declared **OFFICIAL** on this same date
  *(see `MASTER_Process_Tracker.md` §"OFFICIAL ≠ CANON")*. **If the six meanings change, that Phase 6 may need
  revisiting.** ⭐ **This is not a problem; it is the "official ≠ canon" distinction doing its job on day one** —
  the pass is an exemplar of *method*, and its *content* was always pending developer review.
- **`Concordia-City/Districts/Zodiac_Personality_Substrate/A_Elements.md`** — the district methodology's element
  layer. ⚠ **Scope check needed: does this ruling reach the district substrate, or only the city Elementals?**
  → **`DR-1a`, open.**

**Davis is directly affected: its element is `Earth`, one of the six.**

---

## `DR-2` · ⛔ **"SCRIP" IS NOT CANON AND NEVER WAS**

**Developer, verbatim:**

> *"Definitely 'scrip' is not a thing, I never suggested it; you came up with that yourself. So yes, it has
> absolutely no place in the Tepenian universe."*

✅ **Verified clean, 2026-09-13: 0 occurrences repo-wide** *(word-boundary search, excluding `script` /
`description` / `transcript` and kin).* Removed in commit `e938061`, 2026-08-30 — whose message reads
*"remove 'scrip'"*.

> ⭐ **Keep the provenance, because it is the instructive part.** *"Scrip" was an **assistant invention**. It
> was not proposed by the developer, it reached a canon file, and it required a dedicated removal pass to get
> out. **That is `05` §8's named failure mode** — *"a blank in a template reads as an instruction to fill it …
> it was a blank that got filled and then cited"* — and it is the reason the **REQUESTED** category exists:
> ***a pass that ends with three well-formed requests has done real work; a pass that ends with three quiet
> inventions has done damage that is invisible until someone else contradicts it.***

**Standing boundary. Do not reintroduce, and do not reach for a synonym that does the same job.**

---

## `DR-3` · ⏸️ **SUBNET-LOCAL CURRENCIES, THEN HARMONIZATION — FUTURE WORK, HARD-GATED**

**Developer, verbatim:**

> *"While on the topic of money, I had an idea recently that, in the very early stages of the Tepenian
> Federation (let's say, the very first one to three generations, before people began finding common ground and
> unifying), **each individual subnet had roughly what was its own local 'currency'**, which would've been based
> on how that particular socio-geopolitical entity understood the concept of its own economy, inter-city trade,
> and what had value. Then later, as the country unified socially and culturally (in addition to politically, as
> per the Falkland Treaty), **they had to start harmonizing their money system.** This is something that
> absolutely **cannot be accomplished until all 38 cities have fully and completely undergone the ULM, CST, and
> RWBEM.** So this is definitely a task for the future."*

| | |
|---|---|
| **Shape** | Early Federation *(first 1–3 generations)*: **per-subnet local currencies**, each grounded in how that socio-geopolitical entity understood **its own economy, inter-city trade, and what had value.** Later: **harmonization**, driven by social and cultural unification, not only the political union of the Falkland Treaty |
| ⛔ **Gate** | **ALL 38 cities complete through ULM + CST + RWBEM.** Not "most." Not "the subnet in question." **All 38, all three.** |
| **Why the gate is real** | A subnet's currency is downstream of **what its cities valued and traded** — which is precisely what these three methodologies determine. **Writing the currency first would invert the derivation** and force 38 cities to conform to a money system invented before they existed |

⛔ **Until the gate opens, early-Federation currency is `RESERVED`** *(`05` §3)*. **A city pass must not invent
its subnet's early money, its unit, its backing, or its harmonization story.** ✅ It **may** record what a place
*values and trades* — that is the input the future pass will need, and gathering it is the point of running
these methodologies first.

⚠ **Interacts with existing canon** — an energy-backed → regional + trade-standard currency history is already
recorded. **This ruling adds the early per-subnet layer beneath it; it does not obviously replace it.**
**Reconciling the two is part of the future task, not a present one.** → **`DR-3a`, open.**

---

## `DR-4` · ⛔⛔ **CENSUS I IS THE GOVERNING FIGURE. SPREADS AND SUB-LOCATIONS ARE DEFERRED.**

**Developer, verbatim:**

> *"First, we figure out the **base-level, fundamental facts** about these places (i.e., going through the
> process of the ULM, CST, and RWBEM), and then **once that's all done**, then we can start figuring out things
> like 'spreads', 'sub-locations', etc etc etc, and so on."*
>
> *"**Everything is assumed with Census I, because that's the maximum size per city that each city needs to
> accommodate.**"*

### 4.1 The population figure — CENSUS I, corpus-wide

⭐ **The rationale is a DESIGN rationale, not a frame rationale:** Census I is **the maximum size each city must
be built to accommodate.** A city designed to its smaller figure cannot hold its larger one; the reverse is
merely slack.

**For Davis:** **Census I = 1,158,314 → Band 5 (Regional).** *(Census II = 781,596 → Band 4.)*

> ⛔ **THIS OVERRIDES A UNANIMOUS READER RECOMMENDATION, AND THAT IS RECORDED RATHER THAN SMOOTHED.** All three
> T8 readers independently recommended **Band 4 on Census II**, reasoning that Census II is the latest pre-war
> baseline and that no Census III exists. **They were reasoning about which snapshot the frame should describe.
> The developer is reasoning about what the city must be built to hold.** ⭐ **Different question, and the
> developer's is the governing one** — the methodology exists to serve a playable world, not the reverse.

### 4.2 `01` §2.2's "must" is DEFERRED — an explicit override

`01` §2.2 states two obligations that this ruling suspends:

| Threshold | What `01` requires | Status under `DR-4` |
|---|---|---|
| **3→4** *(~50,000)* | *"a location **must** be decomposed into sub-locations, each of which gets its own pass"* | ⏸️ **DEFERRED** |
| **4→5** *(~1M)* | *"the location no longer has a culture; **it has a statistical shape** … the unit of analysis changes to spread and modes"* | ⏸️ **DEFERRED** |

⛔ **Both are deferred until all 38 cities have completed ULM + CST + RWBEM.**

> ⭐ **The sequencing logic, and it is sound:** ***you cannot write a distribution before you know what is being
> distributed.*** A spread needs values to be a spread *of*; sub-locations need a city whose internal variation
> is already understood. **Decomposing 38 cities before knowing any of them would produce 38 sets of invented
> internal structure, each one a fact the later passes would be forced to honor.**

⚠ **Recorded as an override, not as a silent divergence.** `01` §2.2 says **"must."** A pass that quietly did
otherwise would be diverging from a binding instrument with no record of why. **This log is the record.** The
obligations are **suspended, not cancelled** — they resume when the gate opens.

**What a pass DOES do in the meantime:** write the location at the level of **base-level fundamental facts** —
what is true of the place, its generators, its constraints, its function, its composition — **declaring Band 5
where the figure is Band 5, without performing the Band 5 distributional analysis.** ⚠ **And it must say so**,
so a later reader knows the analysis was deferred by ruling rather than missed.

---

## `DR-5` · ⭐ **PRIORITY AND PACE — REAFFIRMED**

**Developer, verbatim:**

> *"Running through the ULM now, then the CST, and then the RWBEM is our top priority, and **don't do it
> 'fast'. I don't want you to do it 'fast'. What I want is for you to get it *RIGHT*.**"*

**Reaffirms `LAW 0 — DEPTH OVER SPEED`** *(`CLAUDE.md`, `00_RUNBOOK.md`)*: ***"There is no credit for finishing
quickly. Completion is not the goal; a place somebody could live in is the goal. The QA gates can confirm a
pass is not wrong; none of them can tell you it is thin."***

⛔ **Operating protocol, unchanged:** **one piece at a time · displayed AND written in the same turn · no time
limit.**

---

# OPEN, ARISING FROM THESE RULINGS

| | Question | Owner |
|---|---|---|
| **`DR-1a`** | Does the Elementals pullback reach the **district** substrate (`Zodiac_Personality_Substrate/A_Elements.md`), or only the city Elementals? | ⏸️ developer |
| **`DR-3a`** | How does the early per-subnet currency layer reconcile with the existing energy-backed → regional + trade-standard history? | ⏸️ **future — gated behind all 38 × 3** |
| — | Back-fill prior developer rulings into this log from `00_RUNBOOK.md`, `CLAUDE.md`, and the observations file | ⏸️ **not mid-pass** |
