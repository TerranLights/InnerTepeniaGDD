# MASTER PROCESS TRACKER — all 38 cities × 3 processes

**Opened 2026-09-05.** ⭐ **The one file that answers "how far along is city X?"**


# ⭐⭐⭐ SESSION BOOT — **what a fresh session does, in order, before anything else**

> ## The developer only has to say:
> # > **"Continue the city run."**
> *Everything below is this file's job, not theirs. If that line was said, you are already in the run.*

| # | Do this | Why |
|--:|---|---|
| **1** | ⛔ **Read `00_RUNBOOK.md` IN FULL.** *Not skimmed, not searched* | **Project law — `CLAUDE.md`.** *Every failure recorded in this methodology was found during work that looked small* |
| **2** | **Read the `📍 RESUME HERE` block below** | It names the live **city** and the live **piece** |
| **3** | **Open that city's own tracker row** — `ULM_Run_Progress.md`, `CST_Progress.md` or `RWBEM_Progress.md` | The per-piece detail the master grid does not carry |
| **4** | **Look the piece up in `ULM_Piece_Index.md`** | One line on what it is, and which file is authoritative on running it |
| **5** | **Open the city's output folder** — `Cities/City_Development_Passes/<Subnet>/<City>/` | Read its `README.md` and whatever pieces are already written. ⚠ **The clarified results of prior pieces are the input to this one** |
| **6** | ⭐ **Run exactly ONE piece.** *Display it AND write it, in the same turn* | The operating protocol above. ⛔ **THERE IS NO TIME LIMIT** |
| **7** | **Update the `📍 RESUME HERE` block and the grid** | *A piece is not closed until the tracker says so* |

> # ⏸️ PENDING SEQUENCING DECISION — **BREADTH-FIRST vs DEPTH-FIRST.** *(Developer, 2026-09-06, thinking aloud — NOT yet ruled.)*
> > ***"Instead of going all the way from beginning-to-end through the entire process [ULM → CST → RWBEM] one city at a time, what I should do is process all the cities through the ULM first, and then… we'll have a massive list of test options to choose from."***
>
> | ✅ For breadth-first | ⚠ Against |
> |---|---|
> | **A full pool of composition profiles to pick test cases from** *(the developer's own reason)* | ⛔ **It defers the feed-forward check by 37 cities.** *The protocol's step 4 is "the clarified result is the input to the next piece" — depth-first tests the `ULM → CST` handoff immediately* |
> | ⭐⭐ **INSTRUMENT STABILITY — the strongest argument.** *2026-09-06 alone changed the instruments heavily (`DRQ-15`, the GPS clarification, technique `18`, the source map).* **Depth-first means city 1 and city 20 run different CST versions and nothing records which.** *Breadth-first runs each LAYER under one version* | ⚠ *A handoff defect found after 38 passes is expensive — and 2026-09-06 is the evidence: CST could not locate ULM output at all, and that surfaced because the developer asked, not because a check caught it* |
> | ⭐ **The `ONE LOCATION` law is easier to keep** — *no city's CST output exists while any city's ULM runs, so there is nothing downstream to leak* | |
> | ⭐ **The terminal differentiation check needs the whole corpus regardless** | |
>
> ### 💡 SUGGESTED TWEAK — *offered, not decided*
> **Run `CST` ONCE on the one city whose ULM is complete, as a pipeline validation. Then switch to
> breadth-first for the remaining 37.** ⭐ *Proves the handoff, and that city is also a strong composition test
> case in its own right — the corpus's most dominant-plurality profile at `4.1:1`.*

## ⛔ STANDING FACTS — **already ruled. Do NOT re-derive, re-audit, or re-raise these.**

| | |
|---|---|
| **Mode** | ⭐ **WARM, all 38.** *Cold is the validation instrument; warm is the production instrument, and the validation evidence is already banked* |
| **Step −1 · Tier 0** | ✅ **38/38.** *It will pass. The first real work on any city is **Step 0*** |
| **Temporal frame** | ✅ **Second Interwar, 2564–2812**, global. No city claims an exception |
| **Generators** | ✅ **G2 · G3 · G4 · G5 · G8 at 38/38** against a threshold of 3. **No city is short** |
| **`G6` defining event** | ⏸️ **Deferred corpus-wide.** ⛔ **Do not report it as a gap** |
| **Extent** | ✅ **Closed.** *13 cities declared; the other 25 are closed by the coastline ruling, not pending.* ⛔ **Do not open a "finish the rest" task** |
| ⛔ **`City_Megasheets/`** | **WITHHELD from every run** — *the whole tree, due to be rewritten* |
| ⛔ **Other cities' conclusions** | **Stay closed until Step 6** — *not for quarantine, but so **Gate 6** has something independent to test* |
| **Research logs** | ⚠ **5/38, and that is fine** — *a log is an **output** of a pass, not an input. Create one when that city's pass first researches something* |

---

> # ⭐⭐⭐ THE OPERATING PROTOCOL — **ONE PIECE AT A TIME. DISPLAY IT *AND* WRITE IT.**
> **Developer instruction, 2026-09-05, stated verbatim because a procedure that paraphrases its governing
> rule will be run without it:**
>
> > **"You should do one individual, singular piece/bit at a time. Display the results. I'll clarify wherever
> > needed. Then, take those results and run those through the subsequent piece/bit. This will be a painfully
> > slow process, but it's likely to produce the best, most accurate results."**
> >
> > **"Also, in addition to displaying the results of each piece/bit, additionally write them to file."**
> >
> > ⭐⭐⭐ **"Also, additionally, make sure to note that THERE IS NO TIME LIMIT. I don't want you to just spit
> > out an answer 'quickly'. What I want from you is to do it *RIGHT*."**
>
> ## The loop, and it does not vary
> | | |
> |---|---|
> | **1 · ONE PIECE** | *One step, one phase, one gate, one technique, one lettered sub-step. **Never two because they seem related.*** |
> | **2 · DISPLAY *AND* WRITE** | ⭐⭐ **BOTH, in the same turn.** *Show the result in full **and** persist it.* ⛔ **Not display-then-write-on-approval, and not write-then-summarize** — ***the displayed text and the written text are the same text*** |
> | **3 · CLARIFY** | **The developer corrects, redirects, or confirms.** ⭐ *Corrections **amend what was written**; the file is the running record, not a reward for approval* |
> | **4 · FEED FORWARD** | **The clarified result — not the draft — is the input to the next piece** |
>
> ⭐ **Why both:** *displaying alone loses the work between turns; writing alone hides it from review.* **The
> file is durable and the display is reviewable, and the protocol needs each for a different reason.**
>
> ## ⛔ WHAT THIS FORBIDS
> **Batching pieces · running ahead "to save a round trip" · writing a file and then merely summarizing it ·
> presenting a finished multi-phase block for approval · treating silence as confirmation.**
>
> ## ⛔⛔⛔ THERE IS NO TIME LIMIT. **NONE.**
> ***Do not optimize for turn count, token count, response length, or apparent momentum.*** **A piece takes as
> long as it takes.** ⛔ **"Enough to write something plausible" is not the threshold** — *that is the exact
> threshold `LAW 0` names and warns against accepting.*
>
> ⚠ **If a piece needs six searches, run six.** **If it needs to sit unresolved and be flagged instead of
> answered, flag it.** ***An honest "this is not settled, here is what would settle it" is a better result than
> a fast, tidy, wrong one*** — **and a fast tidy wrong one is expensive later, everywhere, in work that cannot
> be fixed without redoing the foundation.**
>
> ⭐ **"Painfully slow" is the developer's own word for it, and it is the DESIGN, not a cost to be optimized
> away.** ***It is `LAW 0` — depth over speed — expressed as a turn structure:*** **"There is no credit for
> finishing quickly. Completion is not the goal; a place somebody could live in is the goal."**
>
> ⚠ **And it is the direct countermeasure to this project's own measured failure mode** — *self-audit error
> "has run in ONE direction — toward flattering the pass — on every occasion it has been measured."*
> **A result shown in full, in the same turn it is written, cannot be quietly flattered afterward.**

---

> # 📍 RESUME HERE
> **CITY:** ⭐ **SHIRAYUKI** *(Mirny)* · **PIECE:** ⏭️ **ULM `Step 3` — Research, aimed at what Step 2 named**
> **LAST TOUCHED:** **2026-09-06 — `Step 0`, `Step 1` and `Step 2` all closed.**
> *Written: `00_Frame.md`, `01_Inherited.md`, `02_Spine.md`, `09.5_Log.md`. Logged: `M-142`–`M-148`.*
> ⭐⭐ **SHIRAYUKI IS THE CITY THAT BURNED RUNS 13, 14 AND 15** *(three cold runs, no phase written — the WARM
> ruling for all 38 cities was learned here)*. **Run 14's banked work is inherited and verified in
> `01_Inherited.md` §2.**
> ⭐ **THE SPINE:** *a city with unusual **slack**, which spent it on the one thing its weather erodes — and
> which cannot account for itself, because it never had to.* ✅ **Gate 11 cleared inside `Step 2.6`.**
> ✅ **THE THREE OPEN QUESTIONS ARE NOW FILED FOR REVIEW** *(developer instruction, 2026-09-06)* —
> **`DRQ-10`** band crossing · **`DRQ-11`** rock allocation · **`DRQ-12`** ratified-root list, in
> `Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md`. ⛔ **`DRQ-11` must be answered ONCE for
> all three Larsemann cities** — *Sinheung and Zhongshan are both scheduled this week.*
> 📂 **RESULTS ARE SAVED TO** `Cities/City_Development_Passes/<Subnet>/<City>/` — *by place, not by process.*
> ⛔ **UPDATE EVERY TIME A PIECE CLOSES.** *This block is the only thing that has to be read to resume.*

---

> # ⭐⭐ RUN ORDER AND SCOPE — **developer ruling, 2026-09-06**
>
> | | |
> |---|---|
> | **Order** | ⭐ **GEOGRAPHIC, BY SUBNET** — *finish one subnet before starting the next.* ⛔ **Not alphabetical**; the tables below stay alphabetical for lookup only |
> | **Now** | **MIRNY SUBNET.** *Shirayuki: **ULM COMPLETE** 2026-09-06.* ✅ ***CST ready — `DRQ-15` resolved: 29 extract cards hand-synced*** |
> | **Pace** | **Roughly ONE CITY PER DAY.** *"Over the course of the week, we'll complete the Mirny subnet, one day, one city at a time"* |
> | ⏸️ **CONCORDIA** | **EXCLUDED for now** — *"for the current time being, we're currently ignoring Concordia"* |
> | ⏸️ **{{Bunger Hills City}}** | **SAVED FOR LATER** — *"I'd like to save it for later"*. ⚠ *Also `DRQ-05` OPEN* |
> | **Everything else** | ✅ *"the rest of them should be ready for processing"* |
>
> **Mirny subnet, this week — 8 cities** *(9 minus {{Bunger Hills City}})*: ▶ **Shirayuki** ·
> Casey · Davis · Kunlun · Mirny · Sinheung · Vostok · Zhongshan.

## Legend
| | |
|:-:|---|
| **·** | not started · **▶** in progress · **✅** done · **⏸️** deliberately deferred · **n/a** does not apply |

⚠ **Research log** is shown because it is **Step F of the RWBEM and marked "not optional"** — *a city with a
tick there has had real research recorded against it.*

## ⚠ THESE THREE ARE NOT NECESSARILY SEQUENTIAL — **and that is a developer call, not an assumption**
**The CST's Zodiac Lens runs *"against a location's own already-established character (Phases 1–9)"*, and the
RWBEM was written for **district Phase 6 — the Thematic Breadth Catalog**, whose ULM equivalent is
**Phase 10 — CATALOG**.** ***So on the evidence both are instruments used INSIDE a ULM pass, near its end —
not two successor stages after it.*** ⏸️ **Whether they are run nested or as separate later enrichment passes
is unruled. Tracked as three columns so either reading works.**

> ## ⭐⭐ ORGANIZED BY SUBNET — **developer instruction, 2026-09-06**
> ***"Organize the Master Process Tracker by subnet. That way we can take a quick survey of not only which
> cities, but also which geographical areas/regions are done."***
> **The subnets are listed in a GEOGRAPHIC SWEEP** — *Peninsula → east around the coast → Ross Sea →
> West Antarctica → Pole* — **not alphabetically**, so an unfinished region is visible as a gap rather than as
> scattered rows. ⛔ **Do not re-sort this table alphabetically.**

## 1a · 🗺️ SUBNET ROLLUP — **the survey view. Read this first.**

| | Subnet | Region | Cities | In scope | **ULM** | **CST** | **RWBEM** | Logs |
|:-:|---|---|--:|--:|:-:|:-:|:-:|--:|
| | **Palmer** | Antarctic Peninsula & South Shetlands *(~55–65°W)* | 8 | 8 | 0/8 | 0/8 | 0/8 | 0 |
| | **Halley** | Weddell Sea & Dronning Maud Land *(~30°W–15°E)* | 8 | 8 | 0/8 | 0/8 | 0/8 | 0 |
| | **Mawson** | Enderby & Mac. Robertson Land *(~40–70°E)* | 3 | 3 | 0/3 | 0/3 | 0/3 | 1 |
| ▶ | ⭐ **MIRNY** | **Prydz Bay → Wilkes Land** *(~70–110°E)* | **9** | **8** | ▶ **0/8** *(1 started)* | 0/8 | 0/8 | **3** |
| | **Janbogo** | Ross Sea, Victoria Land & Dome C *(~140–170°E)* | 8 | 7 | 0/7 | 0/7 | 0/7 | 1 |
| | **Byrd** | West Antarctic interior *(~120°W)* | 1 | 1 | 0/1 | 0/1 | 0/1 | 0 |
| | **Amundsen** | ⭐ South Pole — *inter-subnet* | 1 | 1 | 0/1 | 0/1 | 0/1 | 0 |
| | **TOTAL** | | **38** | **36** | **0 done · 1 started** | **0** | **0** | **5** |

⚠ **"In scope" is 36, not 38** — *`Concordia` and `{{Bunger Hills City}}` are held out by the ruling above.*

---

## 1b · 📋 THE CITY GRID, BY SUBNET

### 🏔️ PALMER — *Antarctic Peninsula & South Shetlands* · 0 / 8

| City | **ULM** | **CST** | **RWBEM** | Log |
|---|:-:|:-:|:-:|:-:|
| Esperanza | · | · | · | · |
| Juan Carlos | · | · | · | · |
| Marambio | · | · | · | · |
| Palmer City | · | · | · | · |
| Port Lockroy | · | · | · | · |
| Rothera | · | · | · | · |
| Sejong | · | · | · | · |
| Signy | · | · | · | · |

### 🧊 HALLEY — *Weddell Sea & Dronning Maud Land* · 0 / 8

| City | **ULM** | **CST** | **RWBEM** | Log |
|---|:-:|:-:|:-:|:-:|
| Abowasa | · | · | · | · |
| Belgrano | · | · | · | · |
| Halley | · | · | · | · |
| Lazar | · | · | · | · |
| Neumayer | · | · | · | · |
| Princess Elisabeth | · | · | · | · |
| Sanay | · | · | · | · |
| Troll | · | · | · | · |

### ⛰️ MAWSON — *Enderby & Mac. Robertson Land* · 0 / 3

| City | **ULM** | **CST** | **RWBEM** | Log |
|---|:-:|:-:|:-:|:-:|
| Dome Fuji | · | · | · | · |
| Mawson | · | · | · | ✅ |
| Sayowa | · | · | · | · |

### ⭐▶ MIRNY — *Prydz Bay → Wilkes Land* · **ACTIVE** · 0 / 8 *(1 started)*

| City | **ULM** | **CST** | **RWBEM** | Log |
|---|:-:|:-:|:-:|:-:|
| ▶ **Shirayuki** | ✅ **ULM COMPLETE** *(Steps −1–10, 22 files)* | ✅ **READY** *(`DRQ-15` resolved)* | · | ✅ **+S6** |
| Casey | · | · | · | · |
| Davis | · | · | · | · |
| Kunlun | · | · | · | · |
| Mirny | · | · | · | · |
| Sinheung | · | · | · | ✅ |
| Vostok | · | · | · | · |
| Zhongshan | · | · | · | ✅ |
| ⏸️ *{{Bunger Hills City}}* | ⏸️ **held** | ⏸️ | ⏸️ | · |

> ⭐ **Three of this subnet's cities — Shirayuki, Sinheung, Zhongshan — share ONE 40 km² ice-free oasis and
> ONE climate** *(the Larsemann Hills)*. ⛔ **The climate differentiates none of them**, and together they are
> the largest urban mass in Tepenia. **Whoever runs the other two: `00_Frame.md` §5 records what this
> configuration does to transferability.**

### 🌋 JANBOGO — *Ross Sea, Victoria Land & Dome C* · 0 / 7

| City | **ULM** | **CST** | **RWBEM** | Log |
|---|:-:|:-:|:-:|:-:|
| Cape Adare | · | · | · | · |
| Denison | · | · | · | · |
| Dumont d'Urville | · | · | · | · |
| Fort McMurdo | · | · | · | · |
| Janbogo | · | · | · | ✅ |
| Scott | · | · | · | · |
| Zukelli | · | · | · | · |
| ⏸️ *Concordia* | ⏸️ **held** | ⏸️ | ⏸️ | · |

### ❄️ BYRD — *West Antarctic interior* · 0 / 1

| City | **ULM** | **CST** | **RWBEM** | Log |
|---|:-:|:-:|:-:|:-:|
| Byrd | · | · | · | · |

### 🧭 AMUNDSEN — *South Pole, inter-subnet* · 0 / 1

| City | **ULM** | **CST** | **RWBEM** | Log |
|---|:-:|:-:|:-:|:-:|
| Amundsen Station | · | · | · | · |

**Totals:** ULM **0 / 38 complete · 1 started** · CST 0/38 · RWBEM 0/38 · research logs 5/38.

📎 Per-process detail: `ULM_Run_Progress.md` · `CST_Progress.md` · `RWBEM_Progress.md`
📎 What the pieces are: `ULM_Piece_Index.md` · input availability: `Cultural_Synthesis_Input_Availability.md` · `RealWorld_Basis_Input_Availability.md`
