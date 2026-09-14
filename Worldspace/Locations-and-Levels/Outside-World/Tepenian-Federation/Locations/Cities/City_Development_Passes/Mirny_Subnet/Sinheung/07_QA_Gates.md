# Step 7 — QA · **ALL SEVENTEEN GATES**

**Location:** Sinheung · **Frame:** Second Interwar · **Run mode:** WARM · **Run:** 2026-09-07
**Source:** `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md`

> ⛔ **RAW SCAN OUTPUT IS PASTED, NEVER SUMMARIZED.** *`CLAUDE.md`: "Self-audit error in this project has run in
> ONE direction — toward flattering the pass — on every occasion it has been measured."*
> ⚠ **And every hit is INSPECTED, never trusted from its count** *(`00_RUNBOOK.md` Step 7: a plausible number
> does not invite suspicion the way a zero does)*.

---

# GATE 0 — **Does the completion claim match the file?**

**Files present, `ls -1 *.md`:**
```
00_Frame · 01_Inherited · 02_Spine · 03_Research
04_Phase_02 · 04_Phase_03 · 04_Phase_04 · 04_Phase_05 · 04_Phase_06
04_Phase_07 · 04_Phase_08 · 04_Phase_09 · 04_Phase_10
05_Reconciliation · 09.5_Log · 09.6_Input_Audit · README
```
✅ **PASS.** **Phases 2–10 and Step 5 exist as files, not as claims.** ⚠ **Steps 6–10 were in progress when this
gate ran; the tracker says so rather than claiming completion.**

---

# GATE 1 — **Coverage**

✅ **PASS.** *All eleven phases written; Phase 5 written mid-spine as required; no phase silently skipped.*
⚠ **Declared limit:** `Phase 1`'s content lives in `01_Inherited.md` + `02_Spine.md` rather than a `04_Phase_01`
file — **a naming difference, not a coverage gap.**

---

# GATE 2 — **General population**

⚠ **The live risk was `Phase 9` `B.1`/`B.2`** — *population claims that are really claims about one role.*

| Check | Result |
|---|---|
| **Is the `2.46 pp` retention finding written as a population claim?** | ✅ **No** — *it is explicitly scoped to "a modest minority," with `81.87%` who stayed described as ordinary* |
| **Is `45%` fabrication written as "everyone builds chambers"?** | ✅ **No** — `Phase 8` `A.1` states outright: ***"most people in the fabrication sector here will never touch a chamber"*** |
| **Is the Standard written as a professional practice or as general life?** | ✅ **General** — *`Phase 8` `C.2` extends it to domestic objects; `8f` to ordinary speech* |
| ⚠ **Music** | ✅ **General answer written FIRST**; the vivid re-cut work-song scoped hard as a minority practice at one site |

✅ **PASS** — *and this gate's recorded failure mode (a narrow vivid practice offered as the general case) was
pre-empted in `Phase 8` by writing the general answer before the interesting one existed.*

---

# GATE 3 — ⛔⛔ **INTERNAL CONTRADICTION — THIS GATE FIRED**

**Raw:**
```
00_Frame.md:38   | EXTENT | ⛔⛔ NO DECLARED EXTENT — and that is CORRECT, not a gap.
00_Frame.md:158  An ice-free oasis: ... the city's own extent `107 km²`.
```

> ## ⛔ **THE FRAME CONTRADICTED ITSELF, IN THE SAME FILE, 120 LINES APART.**
> **`107` is the `@10k` column — the area this city WOULD require at band density — not an extent it has.**
> **The `EXTENT` row was corrected earlier the same day; ⛔ *this line was missed*, so the correction landed on
> one row and left the other asserting the retracted figure.**

✅ **FIXED 2026-09-07.** ⭐ **And the real datum is spine-grade rather than clerical:** *the city needs
`96–137 km²`; the whole shared oasis is `~34–40 km²`* — **a `2.4×` to `4.0×` shortfall.** ***It stands mostly
not on rock, which is `Step 3.6`'s first fact.***

⚠ **The transferable form: a correction applied to a TABLE ROW does not reach the PROSE that repeats it.**

---

# GATE 4 — **Swap test** *(peer-free form)*

⛔ **The spec's form — *"swap for its nearest comparable"* — cannot be run: that is a peer as a control.**
✅ **`CLAUDE.md`'s peer-free form used instead**, which it records as *strictly stronger*:
***"would satisfying this replace something SPECIFIC TO THIS PLACE with something that could be true anywhere?"***

**Run in full at `Phase 9` `9E`. Result: `5` findings unswappable, `1` swappable and correctly pre-tagged
surface** *(near-parity, a census fact used only as a floor)*.
✅ **PASS.**

---

# GATE 5 — **Cross-location consistency** *(THE LAW OF ONE LOCATION)*

**Raw — ranking language:**
```
04_Phase_08_Making.md:287   "...and unlike the works, nobody is on a clock inside it"
05_Reconciliation.md:23,85  quotes the DATASHEET's "rank 16th / 11th" while proposing to strike them
09.5_Log.md:310             "...unlike the Standard it can pardon"
03_Research.md:26           quotes RWBEM Step F on cold-run admissibility
```
**Raw — roster superlatives:**
```
00_Frame.md:159             "coldest months avg −22 °C"
04_Phase_04:113 · 04_Phase_07:546 · 09.5_Log ×3   "highest in corpus"
```

**Every hit inspected:**

| Hit | Verdict |
|---|---|
| *"unlike the works" · "unlike the Standard"* | ✅ **INTERNAL** — *comparing two things inside this city* |
| `05_Reconciliation` rank quotes | ✅ **CORRECTIONS** — *the docket proposes striking them* |
| `00_Frame` **"coldest months"** | ✅ **THIS CITY'S OWN CLIMATOLOGY** — *its own coldest months, not a rank* |
| **"highest in corpus"** ×5 | ✅ **ALL are the correction notes recording that the phrase was DROPPED** from `04` §3 |

✅ **PASS — `0` live cross-city comparisons.** ⭐ **Neighbors appear only as RELATION** *(a shared port, a supply
direction, a design origin, a structural consultancy)*, **and every one survives the one-sentence test.**

---

# GATE 6 — **Duplicate institutions**

⏸️ **TERMINAL, NOT IN-RUN.** *Ruled 2026-09-06: it requires siblings' completed material.* ⛔ **Not run, and its
absence is correct rather than a skip.**

---

# GATE 7 — **Research accounting**

| Pick | Disposition | What it gave |
|---|---|---|
| **Daegu** *(textile lock-out)* | ⭐ **CHANGED A FINDING** | *the ownership-by-modification frame the spine's deficit needed* |
| **Córdoba / the `Torino`** | ⭐⭐ **CHANGED A FINDING** | ***ownership by accumulated modification*** — **the direct answer to "a city that builds to someone else's design," and the backbone of `Step 3.6`** |
| **Volgograd / Kahn** | ⭐⭐ **CHANGED A FINDING** | ***"the route out is PEOPLE who can design, not the design"*** — **which located the originating capacity in the ice trades rather than the Institute** |

**`3` of `3` picks changed findings** *(`100%`)*. ⚠ **The gate warns `100%` should be suspected of counting
ornament as change.** ⭐ **Inspected: all three are load-bearing — remove any one and `Step 3.6` does not
resolve.** ✅ **But the honest note is that the pick count is LOW (3), so the ratio is weak evidence either way.**

⏸️ **`Step 3`'s own open threads remain open and are recorded** *(whose `Mark IV` revisions; the ATCM management
plan governing three stations on one site)*.
✅ **PASS, with the low-N caveat stated.**

---

# GATE 8 — **Standout recorded**

✅ **PASS.** ⭐⭐⭐ **The standout is recorded and is not a decoration:**
***the Standard has no office because an office could not do the job — freeze-thaw failure is deferred and
displaced, so only the maker is ever positioned to know.***
⭐ **Independently corroborated at `Step 5` by the datasheet's `§6a`, written years earlier by a different
instrument.**

---

# GATE 9 — **Asymmetry** *(second pass, on findings written AFTER Step 1)*

| Finding | Does the mechanism run both ways? |
|---|---|
| **The Standard** | ✅ **YES, and it is the pass's core** — *condemns, cannot pardon; **`Phase 7` `B.6` prices the sanction and finds it survivable but unappealable*** |
| **The threshold** | ✅ *Both directions written — public outer, private inner* |
| ⭐ **The verdict-return sorting** | ✅ **Both sides written** — *deferred-verdict trades AND immediate-verdict trades, neither as the failure case* |
| ⚠ **The counterculture** | ✅ **AMENDED at `Step 5`** — *withdrawal is available, and the reason it is unpunished is written* |
| ⛔ **The re-cut command** | ⚠ **ONE-SIDED BY CANON** — *canon states the obligation and names no party.* ✅ **Recorded as a gap in canon, not filled** |

✅ **PASS.**

---

# GATE 10 — **The Review Panel**

⏸️ **RUNS AS `Step 8`.** *Not yet convened at the time of this gate.*

---

# GATE 11 — **Plausibility**

**Raw, recomputed from source:**
```
Census I        467,272 human + 495,143 robot = 962,415
robot share     51.45%   human 48.55%
workforce       728,779   (robots + 0.5*humans)
three-tier      40.7 + 26.7 + 32.6 = 100.0
land            needs 96-137 km2 vs oasis 34-40 km2  ->  2.4x to 4.0x short
retention       H 84.33% / R 81.87%   spread +2.46pp
```
✅ **PASS.** ⭐ **The population ÷ ground division is what this gate exists for, and here it produced a finding
rather than a check: *the city does not fit on its own rock*.**
⚠ **One figure carried with a flag: the three-tier percentages are PROVISIONAL** *(`16`'s own standing rule)*,
**and every Division-of-Industry headcount predates the `−10%` census ruling** *(`DRQ-17`)*.

---

# GATE C — **Canon check, federated**

**All three tiers named with paths, per the gate's own requirement that a negative result without paths does not count:**

| Tier | Searched |
|---|---|
| **1 · UNIVERSE** | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/` — ✅ **opened deliberately.** *`Laws_of_Robotics.md`, `Robot_Universals/` Ch. 13–14, `Doll_Representation_Categories.md`, `No_National_Stereotypes` via `§C.9b/c`, `Worldspace/Characters/`* |
| **2 · PROJECT** | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/` — *specs, census, climate, Division of Industry, robot biology, factions, relationships, the national institutes, the currency* |
| **3 · SIBLINGS** | `/home/kuroskalacs/Documents/Doll-Fi/media/games/` — ⏸️ **not swept.** *Declared, not claimed* |

⚠ **Thin-file redirect check:** ✅ **run** — *`World_History_Reference.md` is a 7-line stub here and 344 lines upstream.*
⛔⛔ **AND THIS GATE FIRED HARD DURING THE PASS, TWICE:**
1. **`Phase 9` had opened NONE of its three universe-tier robot sources**, and produced a false headline finding.
2. **`Phase 5` had opened none of its three relationship files**, and missed a canon consultancy bearing on `Step 3.6`.
✅ **Both closed. Full record: `09.6_Input_Audit.md`.** ⏸️ **`16` targets remain open and are docketed there.**

---

# GATE F — **Frame integrity**

| Check | Result |
|---|---|
| **Frame declared** | ✅ **Second Interwar, 2564–2812** |
| ⛔ **`Status:` / `Current Status` / `Connection to Concordia` / `Legacy` excluded** | ✅ **None used as input** |
| ⭐ **Alive-in-frame** | ✅ **Mountain Pass pre-flagged at `Step 1`.** ⭐ **AND `Step 5` caught a second: *Denison is alive in-frame*, so there are THREE chamber manufacturers, not two** |
| ⛔ **Post-war material excluded** | ✅ *The datasheet's §30 Long Night War damage is docketed as out-of-frame* |

✅ **PASS.**

---

# GATE I — **Inheritance classification**

✅ **PASS.** *`Step 1` audited 9 inherited findings and tiered them; **7 were one-sided** and are recorded as
such.* ⭐ **`Step 5` added the tier ruling that matters most: the culture datasheet is TIER 3 — derived — and
does not automatically outrank the pass.**

---

# GATE P — **Parent reconciliation**

| | |
|---|---|
| **Parent** | **The Mirny subnet, and above it the Federation (Band 6)** |
| **What the parent needs from this city** | ⭐ **Two national roles: FABRICATION and robotic MEDICINE** — *the chamber apparatus, and one of three sources of all robotic care* |
| ⚠ **Provisional assumptions about an unwritten parent?** | ✅ **NONE load-bearing.** *`Step 5`'s strongest-finding check confirms the pass's best finding rests on measured climate and canon, not on a parent assumption* |

✅ **PASS.**

---

# GATE G — **Generator honesty**

| Check | Result |
|---|---|
| **At least three generators, run independently?** | ✅ **Five: `G2` `G3` `G4` `G5` `G8`** |
| ⚠ **Are they genuinely independent?** | ✅ *Physical constraint, function, founding, network position and composition are not one fact wearing five hats* |
| **Each run to a full profile before comparison?** | ✅ **Yes** |
| ⭐ **Shape reported WITH its input set?** | ✅ **`COST-DOMINANT`, imposed rather than voluntary, on the admitted-input set** — *`02` §4.0's requirement met* |
| ⛔ **`G1` used as an independent generator?** | ✅ **No** — *symbol assignments are provenance-downstream of a personality read, so corroboration-tier only* |

✅ **PASS.**

---

# ▶ VERDICT

| | |
|---|---|
| **Gates run** | **15 of 17** |
| ⏸️ **Not run, correctly** | **Gate 6** *(terminal)* · **Gate 10** *(= Step 8, next)* |
| ⛔ **FIRED** | ⭐ **Gate 3** — *the Frame contradicted itself on extent.* **Fixed** |
| ⛔ **FIRED during the pass** | ⭐⭐ **Gate C, twice** — *two phases had not opened their required canon.* **Both closed; one had produced a FALSE finding* |
| ✅ **Passed** | **Gates 0 · 1 · 2 · 4 · 5 · 7 · 8 · 9 · 11 · C · F · I · P · G** |

📎 **Next: `Step 8` — THE REVIEW PANEL.**
